"""This is a List and Dictionary of target skills and definitions"""

skills_list = ("Linux Administration", "Windows Administration", "Networking", "Python Automation", "Bash Automation", "IaC / Terraform", "Ansible",
               "Containers", "Azure Cloud", "CI/CD","Monitoring & Troubleshooting","Security & Compliance", "Documentation")

""" Skills matrix template, captures a dictonary nested in a dictionary"""

skills_matrix = {
    "Linux Administration":{
        "Description":"Can manage and troubleshoot Linux systems, including installation, configuration, and maintenance.",
        "Current Score":0,
        "Target Score":5,
        "Evidence Count":0
    }
}


def show_skill_info():
    """ Function show info of completed task and update evidence count"""
    evidence_count = 0
    print("Enter a tasks from the skills_list")
    for skills in skills_list:
        print(f'\t{skills}')        
    skill = input("Enter skill performed: ")
    if skill in skills_matrix:
        info = skills_matrix[skill]
        info['Evidence Count'] += 1
        evidence_count = info['Evidence Count']
        info['Current Score']=calculate_score(info['Evidence Count'])
        print(f"Skill: {skill}\nDescription: {info['Description']}\nCurrent Score: {info['Current Score']}\nTarget Score: {info['Target Score']}\nEvidence Count: {info['Evidence Count']}")
    else:
        print(skill, "not found")
    return evidence_count

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
 
show_skill_info()




            


        
        
        
