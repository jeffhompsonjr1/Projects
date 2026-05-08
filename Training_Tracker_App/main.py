from models import TrainingItem
from storage import save_training_item, save_skills_matrix
from skills_matrix import update_selected_skills, skills_matrix

annies_lab = TrainingItem(
    title="Annie's Lab nginx container",
    date="2026-05-06",
    category="Personal Project",
    description="Built a containerized nginx test site.",
    time_spent_minutes=90,
    skills_used=["Linux Administration", "Containers", "Networking", "Documentation"],
    evidence="Lab notes and working localhost site"
)

print(annies_lab.to_dict())
print(annies_lab.summarize())
update_selected_skills(annies_lab.skills_used)

from storage import save_training_item # type: ignore
save_training_item(annies_lab)