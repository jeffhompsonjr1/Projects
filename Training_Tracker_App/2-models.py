class TrainingItem:
    """Represents a training item with details about the training session."""
    def __init__(self, title, date, category, description, time_spent_minutes, skills_used, evidence):
        self.title = title
        self.date = date
        self.category = category
        self.description = description
        self.time_spent_minutes = time_spent_minutes
        self.skills_used = skills_used
        self.evidence = evidence

    def summarize(self):
        """Returns a summary card of the training item."""
        return f"Task:{self.title}\nDate:{self.date}\nCategory:{self.category}\nDescription:{self.description}\nTime Spent (minutes):{self.time_spent_minutes}\nSkills Used:{', '.join(self.skills_used)}\nEvidence:{self.evidence}"
    

"""Example instance of TrainingItem and its summary."""
annies_lab = TrainingItem("LAMP Stack Setup", "2026-04-29", "System Administration", "Set up a LAMP stack on a Linux server", 180, ["Linux Administration", "Documentation", "Web Services"], "http://localhost/annies_lab")
print(annies_lab.summarize())