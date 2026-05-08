"""1. Take a TrainingItem object  2. Convert it using training_item.to_dict() 3. Save it into data/training_items.json"""
import json
import os
def save_training_item(training_item):
    """Saves a training item dictionary to a JSON file."""
    file_path = "data/training_items.json"

    # Ensure the data directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Load existing training items if the file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            training_items = json.load(file)
    else:
        training_items = []

    # Append the new training item and save back to the file
    training_items.append(training_item.to_dict())
    with open(file_path, "w") as file:
        json.dump(training_items, file, indent=4)

def save_skills_matrix(skills_matrix): 
    """Saves a skills matrix dictionary to a JSON file."""
    file_path = "data/skills_matrix.json"

    # Ensure the data directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Load existing skills matrix if the file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            existing_matrix = json.load(file)
    else:
        existing_matrix = {}

    # Update the existing matrix with the new skills matrix and save back to the file
    existing_matrix.update(skills_matrix)
    with open(file_path, "w") as file:
        json.dump(existing_matrix, file, indent=4)
   
    