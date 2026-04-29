import ipaddress
import os
import re


def validate_computer_name(name: str) -> bool:
    """Validate Windows computer name rules."""
    if not (1 <= len(name) <= 15):
        return False
    if not re.fullmatch(r"[A-Za-z0-9-]+", name):
        return False
    if name.startswith("-") or name.endswith("-"):
        return False
    if name.isdigit():
        return False
    return True


def validate_ipv4(address: str) -> bool:
    """Validate IPv4 address."""
    try:
        ipaddress.IPv4Address(address)
        return True
    except ValueError:
        return False


def validate_prefix_length(prefix: str) -> bool:
    """Validate CIDR prefix length."""
    try:
        value = int(prefix)
        return 0 <= value <= 32
    except ValueError:
        return False


def validate_drive_letter(letter: str) -> bool:
    """Validate a single drive letter."""
    return bool(re.fullmatch(r"[A-Za-z]", letter.strip()))


def validate_disk_number(disk: str) -> bool:
    """Validate disk number."""
    try:
        value = int(disk)
        return value >= 0
    except ValueError:
        return False


def validate_nonnegative_int(value: str) -> bool:
    """Validate whole number 0 or higher."""
    try:
        return int(value) >= 0
    except ValueError:
        return False


def validate_size_input(size_text: str) -> bool:
    """
    Accept sizes like:
    60GB
    500GB
    1TB
    1.5TB
    """
    return bool(re.fullmatch(r"\d+(\.\d+)?\s*(GB|TB)", size_text.strip(), re.IGNORECASE))


def convert_size_to_bytes(size_text: str) -> int:
    """Convert GB/TB text into bytes."""
    match = re.fullmatch(r"(\d+(\.\d+)?)\s*(GB|TB)", size_text.strip(), re.IGNORECASE)
    if not match:
        raise ValueError("Invalid size format")

    number = float(match.group(1))
    unit = match.group(3).upper()

    if unit == "GB":
        return int(number * (1024 ** 3))
    if unit == "TB":
        return int(number * (1024 ** 4))

    raise ValueError("Unsupported size unit")


def escape_powershell_string(value: str) -> str:
    """Escape double quotes for safe insertion into PowerShell strings."""
    return value.replace('"', '`"')


def get_valid_input(prompt: str, validator, error_message: str) -> str:
    """Prompt until valid input is received."""
    while True:
        value = input(prompt).strip()
        if validator(value):
            return value
        print(f"Invalid input: {error_message}\n")


def get_yes_no(prompt: str) -> bool:
    """Prompt for Y/N and return True/False."""
    while True:
        value = input(prompt).strip().lower()
        if value in ("y", "yes"):
            return True
        if value in ("n", "no"):
            return False
        print("Invalid input: please enter Y or N.\n")


def collect_disk_info():
    """Collect multiple disk definitions from user input."""
    disks = []

    disk_count = int(get_valid_input(
        "How many disks do you want to configure? ",
        validate_nonnegative_int,
        "Enter a whole number 0 or greater."
    ))

    used_disk_numbers = set()
    used_drive_letters = set()

    for index in range(1, disk_count + 1):
        print(f"\n--- Disk {index} ---")

        while True:
            disk_number = get_valid_input(
                f"Enter Disk Number for disk {index}: ",
                validate_disk_number,
                "Disk number must be 0 or higher."
            )
            if disk_number in used_disk_numbers:
                print("Invalid input: That disk number was already used.\n")
            else:
                used_disk_numbers.add(disk_number)
                break

        use_full_disk = get_yes_no(
            f"Use maximum available size for disk {index}? (Y/N): "
        )

        size_text = None
        size_bytes = None

        if not use_full_disk:
            size_text = get_valid_input(
                f"Enter size for disk {index} (example: 60GB or 1TB): ",
                validate_size_input,
                "Enter a size like 60GB or 1TB."
            )
            size_bytes = convert_size_to_bytes(size_text)

        while True:
            drive_letter = get_valid_input(
                f"Enter drive letter for disk {index}: ",
                validate_drive_letter,
                "Enter a single letter like G."
            ).upper()

            if drive_letter in used_drive_letters:
                print("Invalid input: That drive letter was already used.\n")
            else:
                used_drive_letters.add(drive_letter)
                break

        volume_label = input(f"Enter volume label for disk {index}: ").strip()
        while not volume_label:
            print("Invalid input: Volume label cannot be blank.\n")
            volume_label = input(f"Enter volume label for disk {index}: ").strip()

        disks.append({
            "disk_number": int(disk_number),
            "use_full_disk": use_full_disk,
            "size_text": size_text.upper().replace(" ", "") if size_text else None,
            "size_bytes": size_bytes,
            "drive_letter": drive_letter,
            "volume_label": volume_label
        })

    return disks


def build_disk_commands(disks):
    """Build PowerShell commands for all disk operations."""
    if not disks:
        return 'Write-Host "No additional disks selected for configuration." -ForegroundColor DarkYellow'

    commands = []

    for disk in disks:
        disk_number = disk["disk_number"]
        drive_letter = disk["drive_letter"]
        volume_label = escape_powershell_string(disk["volume_label"])
        use_full_disk = disk["use_full_disk"]

        if use_full_disk:
            partition_logic = f'''
Write-Host "Using maximum available size on disk {disk_number}..." -ForegroundColor Yellow
New-Partition -DiskNumber {disk_number} -UseMaximumSize -DriveLetter {drive_letter} -ErrorAction Stop
'''
        else:
            size_text = disk["size_text"]
            size_bytes = disk["size_bytes"]
            partition_logic = f'''
$sizeInfo{disk_number} = Get-PartitionSupportedSize -DiskNumber {disk_number} -ErrorAction Stop
$requestedSize{disk_number} = {size_bytes}
$maxSize{disk_number} = $sizeInfo{disk_number}.SizeMax
$buffer{disk_number} = 5MB

Write-Host "Requested partition size for disk {disk_number}: {size_text}" -ForegroundColor Yellow

if ($requestedSize{disk_number} -gt ($maxSize{disk_number} - $buffer{disk_number})) {{
    Write-Host "Requested size is too close to or greater than available space. Using maximum available size instead." -ForegroundColor DarkYellow
    New-Partition -DiskNumber {disk_number} -UseMaximumSize -DriveLetter {drive_letter} -ErrorAction Stop
}} else {{
    New-Partition -DiskNumber {disk_number} -Size $requestedSize{disk_number} -DriveLetter {drive_letter} -ErrorAction Stop
}}
'''

        command_block = f'''
# Disk {disk_number}
Write-Host "Processing disk {disk_number}..." -ForegroundColor Yellow
$disk{disk_number} = Get-Disk -Number {disk_number} -ErrorAction Stop

if ($disk{disk_number}.IsOffline) {{
    Write-Host "Bringing disk {disk_number} online..." -ForegroundColor Yellow
    Set-Disk -Number {disk_number} -IsOffline $false
}}

if ($disk{disk_number}.IsReadOnly) {{
    Write-Host "Clearing read-only flag on disk {disk_number}..." -ForegroundColor Yellow
    Set-Disk -Number {disk_number} -IsReadOnly $false
}}

$disk{disk_number} = Get-Disk -Number {disk_number} -ErrorAction Stop

if ($disk{disk_number}.PartitionStyle -eq 'RAW') {{
    Write-Host "Initializing disk {disk_number} as GPT..." -ForegroundColor Yellow
    Initialize-Disk -Number {disk_number} -PartitionStyle GPT -ErrorAction Stop
}} else {{
    Write-Host "Disk {disk_number} is already initialized. Skipping Initialize-Disk." -ForegroundColor DarkYellow
}}

{partition_logic}

Write-Host "Quick formatting drive {drive_letter}: as NTFS with label {volume_label}..." -ForegroundColor Yellow
Format-Volume -DriveLetter {drive_letter} -FileSystem NTFS -NewFileSystemLabel "{volume_label}" -Confirm:$false -Force -ErrorAction Stop
'''
        commands.append(command_block)

    return "\n".join(commands)


def build_powershell_script(
    computer_name: str,
    computer_description: str,
    ip_address: str,
    prefix_length: str,
    gateway: str,
    primary_dns: str,
    alternate_dns: str,
    interface_alias: str,
    disks
) -> str:
    """Build the final PowerShell script."""
    disk_section = build_disk_commands(disks)
    safe_interface_alias = escape_powershell_string(interface_alias)
    safe_computer_name = escape_powershell_string(computer_name)

    description_section = ""
    if computer_description:
        safe_description = escape_powershell_string(computer_description)
        description_section = f'''
# Set computer description
Write-Host "Setting computer description..." -ForegroundColor Yellow
Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\LanmanServer\\Parameters" -Name srvcomment -Value "{safe_description}"
'''

    ps_script = f'''# Generated server setup script
# Run this in PowerShell as Administrator

$ErrorActionPreference = "Stop"

# Check for admin rights
$currentUser = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $currentUser.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {{
    Write-Host "This script must be run as Administrator." -ForegroundColor Red
    exit 1
}}

Write-Host "Starting server configuration..." -ForegroundColor Cyan

# Rename computer
Write-Host "Renaming computer to {safe_computer_name}" -ForegroundColor Yellow
Rename-Computer -NewName "{safe_computer_name}" -Force
{description_section}
# Remove existing IPv4 addresses on selected interface except APIPA
Write-Host "Removing existing IPv4 addresses on interface {safe_interface_alias}..." -ForegroundColor Yellow
Get-NetIPAddress -InterfaceAlias "{safe_interface_alias}" -AddressFamily IPv4 -ErrorAction SilentlyContinue |
    Where-Object {{ $_.IPAddress -notlike "169.254*" }} |
    Remove-NetIPAddress -Confirm:$false -ErrorAction SilentlyContinue

# Disable DHCP and set static/manual IP
Write-Host "Setting static IP address..." -ForegroundColor Yellow
Set-NetIPInterface -InterfaceAlias "{safe_interface_alias}" -Dhcp Disabled -ErrorAction SilentlyContinue
New-NetIPAddress -InterfaceAlias "{safe_interface_alias}" -IPAddress "{ip_address}" -PrefixLength {prefix_length} -DefaultGateway "{gateway}" -ErrorAction Stop

# Configure primary and alternate DNS servers
Write-Host "Setting primary and alternate DNS servers..." -ForegroundColor Yellow
Set-DnsClientServerAddress -InterfaceAlias "{safe_interface_alias}" -ServerAddresses ("{primary_dns}","{alternate_dns}") -ErrorAction Stop

# Verify gateway connectivity
Write-Host "Pinging default gateway to verify connectivity..." -ForegroundColor Yellow
if (Test-Connection -ComputerName "{gateway}" -Count 2 -Quiet) {{
    Write-Host "Gateway ping successful. Network connectivity looks good." -ForegroundColor Green
}} else {{
    Write-Host "Gateway ping failed. Check IP settings, VLAN, NIC, or gateway availability." -ForegroundColor Red
}}

# Configure disks
{disk_section}

# Check for Windows Updates at the end
Write-Host "Checking Windows Update service..." -ForegroundColor Yellow
$wuauserv = Get-Service -Name wuauserv -ErrorAction SilentlyContinue

if ($null -eq $wuauserv) {{
    Write-Host "Windows Update service not found." -ForegroundColor Red
}} else {{
    if ($wuauserv.Status -ne 'Running') {{
        Write-Host "Starting Windows Update service..." -ForegroundColor Yellow
        Start-Service wuauserv
    }}

    try {{
        Write-Host "Scanning for available updates..." -ForegroundColor Yellow
        $updateSession = New-Object -ComObject Microsoft.Update.Session
        $updateSearcher = $updateSession.CreateUpdateSearcher()
        $searchResult = $updateSearcher.Search("IsInstalled=0 and Type='Software'")

        Write-Host ("Updates found: " + $searchResult.Updates.Count) -ForegroundColor Green

        for ($i = 0; $i -lt $searchResult.Updates.Count; $i++) {{
            Write-Host (" - " + $searchResult.Updates.Item($i).Title) -ForegroundColor Cyan
        }}
    }}
    catch {{
        Write-Host "Unable to complete update scan. Check network connectivity, update configuration, or WSUS policy." -ForegroundColor Red
        Write-Host $_.Exception.Message -ForegroundColor Red
    }}
}}

Write-Host "Configuration complete." -ForegroundColor Green
Write-Host "A restart is recommended to fully apply the rename." -ForegroundColor Green
'''
    return ps_script


def main():
    """Main program flow."""
    print("=" * 70)
    print(" Windows Server PowerShell Script Builder v4")
    print("=" * 70)
    print()

    computer_name = get_valid_input(
        "Enter Computer Name: ",
        validate_computer_name,
        "Computer name must be 1-15 characters, use letters/numbers/hyphens, and cannot be only numbers."
    )

    computer_description = input("Enter optional Computer Description (press Enter to skip): ").strip()

    ip_address = get_valid_input(
        "Enter Static IP Address: ",
        validate_ipv4,
        "Enter a valid IPv4 address, like 172.17.3.25"
    )

    prefix_length = get_valid_input(
        "Enter Prefix Length (example: 24): ",
        validate_prefix_length,
        "Enter a number from 0 to 32."
    )

    gateway = get_valid_input(
        "Enter Default Gateway: ",
        validate_ipv4,
        "Enter a valid IPv4 address."
    )

    primary_dns = get_valid_input(
        "Enter Primary DNS Server: ",
        validate_ipv4,
        "Enter a valid IPv4 address."
    )

    alternate_dns = get_valid_input(
        "Enter Alternate DNS Server: ",
        validate_ipv4,
        "Enter a valid IPv4 address."
    )

    interface_alias = input('Enter Network Interface Alias (default: Ethernet): ').strip()
    if not interface_alias:
        interface_alias = "Ethernet"

    disks = collect_disk_info()

    ps_script = build_powershell_script(
        computer_name=computer_name,
        computer_description=computer_description,
        ip_address=ip_address,
        prefix_length=prefix_length,
        gateway=gateway,
        primary_dns=primary_dns,
        alternate_dns=alternate_dns,
        interface_alias=interface_alias,
        disks=disks
    )

    output_file = f"{computer_name}_setup.ps1"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(ps_script)

    print("\nPowerShell script generated successfully.")
    print(f"Saved as: {os.path.abspath(output_file)}")


if __name__ == "__main__":
    main()
