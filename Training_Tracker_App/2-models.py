class TrainingItem():
    def __init__(self, title, date, category, description, time_spent_minutes, skills_used, evidence):
        self.title = title
        self.date = date
        self.category = category
        self.description = description
        self.time_spent_minutes = time_spent_minutes
        self.skills_used = skills_used
        self.evidence = evidence

    def summarize(self):
        return f"Task:{self.title}\nDate:{self.date}\nCategory:{self.category}\nDescription:{self.description}\nTime Spent (minutes):{self.time_spent_minutes}\nSkills Used:{', '.join(self.skills_used)}\nEvidence:{self.evidence}"
    


training_entry = TrainingItem("Python Training", "2023-10-15", "Programming", "Learn Python basics", 120, ["Python", "Programming"], "https://example.com/evidence").summarize()
print(training_entry)