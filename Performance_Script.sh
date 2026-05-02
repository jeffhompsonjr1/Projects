#!/bin/bash

# This is a script to gather and analyze daily performance of my linux systems.
TIMESTAMP=$(date +%c)
FILE="/Performance_Monitoring/PM_from_$TIMESTAMP.txt"

#Make the directory if it doesnt exist already.
sudo mkdir -p /Performance_Monitoring/
sudo chmod 777 /Performance_Monitoring/

#Header of document
echo -e "\t Performance Monitor Log - $TIMESTAMP" >> "$FILE"
echo "" >> "$FILE"

#Appended Commands
echo -e "\n\t ================== DNF HISTORY  ======================\n" >> "$FILE"
sudo dnf update
dnf history >> "$FILE"

echo -e "\n\t================== FLATPAK APP LIST  ======================\n" >> "$FILE"
flatpak list --app >> "$FILE"

echo -e "\n\t ================== JOURNAL ERRORS LAST 1 HOUR ======================\n" >> "$FILE"
journalctl -p err --since "1 hour ago" >> "$FILE"

echo -e "\n\t ==================== KERNEL ERRORS LAST 1 HOUR ======================\n" >> "$FILE"
journalctl -k -p err --since "1 hour ago" >> "$FILE"

echo -e "\n\t =================== SSH AUTHENTICATION WARNINGS=====================\n" >> "$FILE"
journalctl -u sshd -p warning --since "1 hour ago" >> "$FILE"

echo -e "\n\t===== FAILED SYSTEMD SERVICES =====" >> "$FILE"
systemctl --failed >> "$FILE"

echo -e "\n\t ================== DISK SPACE ======================\n" >> "$FILE"
df -h >> "$FILE"

echo -e "\n\t ================== MEMORY SPACE ======================\n" >> "$FILE"
free -h >> "$FILE"

echo -e "\n\t ================== VOLUME ALLOCATION ======================\n" >> "$FILE"
lsblk /dev/sd* >> "$FILE"

echo -e "\n\t ================== TOP OUTPUT======================\n" >> "$FILE"
top -b -n 1 >> "$FILE"
