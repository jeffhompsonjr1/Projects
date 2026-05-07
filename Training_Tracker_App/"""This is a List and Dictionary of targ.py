"""This is a List and Dictionary of target skills and definitions"""

skills_list = ("Linux Administration", "Windows Administration", "Networking", "Python Automation", "Bash Automation", "IaC / Terraform", "Ansible",
               "Containers", "Azure Cloud", "CI/CD","Monitoring & Troubleshooting","Security & Compliance", "Documentation")

""" Skills matrix template, captures a dictonary nested in a dictionary"""

skills_matrix = {
    "Linux Administration":{
        "Description":"Can manage and troubleshoot Linux systems, including installation, configuration, and maintenance.",
        "Current Score":0,
        "Target Score":5,
        "Evidence Types":['RHEL tasks', 'Ubuntu tasks', 'LAMP stack setup', 'Linux troubleshooting','SSH configuration','System monitoring'],
        "Evidence Count":0
    },
    'Windows Administration':{
        "Description":"Can manage and troubleshoot Windows systems, including installation, configuration, and maintenance.",
        "Current Score":0,
        "Target Score":5,
        "Evidence Types":['Windows Server tasks', 'Active Directory management', 'PowerShell scripting', 'Windows troubleshooting','Group Policy configuration','System monitoring'],
        "Evidence Count":0
    },
    'Networking':{
        "Description":"Can design, implement, and troubleshoot network infrastructures, including routing, switching, and security.",
        "Current Score":0,
        "Target Score":5,
        "Evidence Types":['Network design', 'Router configuration', 'Switch configuration', 'Firewall setup','Network troubleshooting','VPN configuration'],
        "Evidence Count":0

    },
    'Python Automation':{
        "Description":"Can develop Python scripts to automate tasks, manage systems, and integrate with APIs.",
        "Current Score":0,
        "Target Score":5,
        "Evidence Types":['Python scripting', 'API integration', 'Automation projects', 'Python troubleshooting','Task automation','Data processing'],
        "Evidence Count":0
    },
    'Bash Automation':{
        "Description":"Can create Bash scripts to automate tasks, manage systems, and perform administrative functions.",
        "Current Score":0,
        "Target Score":5,
        "Evidence Types":['Bash scripting', 'Task automation', 'System management', 'Bash troubleshooting','Cron jobs','Log management'],
        "Evidence Count":0
    },
    'IaC / Terraform':{
        "Description":"Can use Infrastructure as Code (IaC) tools like Terraform to provision and manage cloud resources.",
        "Current Score":0,
        "Target Score":5,
        "Evidence Types":['Terraform projects', 'Cloud resource provisioning', 'IaC implementation', 'Terraform troubleshooting','Infrastructure management','Cloud automation'],
        "Evidence Count":0
    },
    'Ansible':{
        "Description":"Can use Ansible to automate configuration management, application deployment, and task automation.",
        "Current Score":0,
        "Target Score":5,
        "Evidence Types":['Ansible playbooks', 'Configuration management', 'Application deployment', 'Ansible troubleshooting','Task automation','Infrastructure management'],
        "Evidence Count":0
    },
    'Containers':{
        "Description":"Can design, deploy, and manage containerized applications using tools like Docker and Kubernetes.",
        "Current Score":0,
        "Target Score":5,
        "Evidence Types":['Docker projects', 'Kubernetes deployments', 'Container orchestration', 'Container troubleshooting','Microservices architecture','Container security'],
        "Evidence Count":0
    },
    'Azure Cloud':{
        "Description":"Can design, implement, and manage cloud solutions using Microsoft Azure services.",
        "Current Score":0,
        "Target Score":5,
        "Evidence Types":['Azure projects', 'Cloud resource management', 'Azure services implementation', 'Azure troubleshooting','Cloud security','Cost optimization'],
        "Evidence Count":0
    },
    'CI/CD':{
        "Description":"Can design and implement Continuous Integration and Continuous Deployment (CI/CD) pipelines using tools like Jenkins, GitLab CI, or Azure DevOps.",
        "Current Score":0,
        "Target Score":5,
        "Evidence Types":['CI/CD pipeline implementation', 'Jenkins projects', 'GitLab CI projects', 'Azure DevOps projects','Pipeline troubleshooting','Automation of software delivery'],
        "Evidence Count":0
    },
    'Monitoring & Troubleshooting':{
        "Description":"Can implement monitoring solutions and troubleshoot issues across systems, networks, and applications.",
        "Current Score":0,
        "Target Score":5,
        "Evidence Types":['Monitoring implementation', 'Troubleshooting projects', 'System monitoring', 'Network monitoring','Application monitoring','Incident response'],
        "Evidence Count":0
    },
    'Security & Compliance':{
        "Description":"Can implement security best practices and ensure compliance with industry standards and regulations.",
        "Current Score":0,
        "Target Score":5,
        "Evidence Types":['Security implementation', 'Compliance projects', 'Vulnerability assessments', 'Security troubleshooting','Incident response','Policy development'],
        "Evidence Count":0
    },
    'Documentation':{   
        "Description":"Can create clear and comprehensive documentation for systems, processes, and projects.",
        "Current Score":0,
        "Target Score":5,
        "Evidence Types":['Technical documentation', 'Process documentation', 'Project documentation', 'Documentation troubleshooting','Knowledge base articles','User guides'],
        "Evidence Count":0
    }
}
def calculate_score(evidence_count):
    """ Function to update score based on evidence count"""
    if evidence_count == 0:
        return 0         
    elif evidence_count <= 2:
        return 1
    elif evidence_count <= 4:
        return 2
    elif evidence_count <= 7:
        return 3
    elif evidence_count <= 11:
        return 4
    else:
        return 5

def update_multiple_skills():
    """ Function show info of completed task and update evidence count"""
    evidence_count = 0
    print("Enter a task(s) from the skills_list")
    """This loop prints the skills list"""
    for skills in skills_list:
        print(f'\t{skills}') 
    """This input captures the skill performed and evidence of task performed"""       
    skills = input("Enter skill(s) performed: ")
    assessed_skills = []
    while skills != "done":
        if skills in skills_list:
            assessed_skills.append(skills)
        else:
            print(skills, "not found")
            skills = input("")
            
    print("Evidence types for", skill)
    if skill in skills_matrix:
        """info variable is the skill matrix key for the dictionary nested in the dictionary."""
        info = skills_matrix[skill]
        for evidences in info['Evidence Types']:
            print(f'\t{evidences}')
        evidence = input("Enter evidence of task performed, type 'done' when finished: ")
        while evidence != "done":
            if evidence in info['Evidence Types']:      
                info['Evidence Count'] += 1
            evidence = input("Enter evidence of task performed, type 'done' when finished: ")
        info['Current Score']=calculate_score(info['Evidence Count'])
        print(f"Skill: {skill}\nDescription: {info['Description']}\nCurrent Score: {info['Current Score']}\nTarget Score: {info['Target Score']}\nEvidence Count: {info['Evidence Count']}")
    else:
        print(skill, "not found")
    return evidence_count


 
show_skill_info()