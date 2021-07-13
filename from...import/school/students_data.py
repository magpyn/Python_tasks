
students = [
    {
        "name": "Jakub",
        "subjects_results": [
            {
                "subject": "matematyka",
                "grades": [2, 4, 5, 1, 3, 5]
            },
            {
                "subject": "fizyka",
                "grades": [3, 5, 3, 2, 2, 1]
            }
        ]
    },
    {
        "name": "Mikołaj",
        "subjects_results": [
            {
                "subject": "matematyka",
                "grades": [3, 2, 5, 5, 4, 3]
            },
            {
                "subject": "fizyka",
                "grades": [3, 4, 3, 2, 1, 3]
            },
            {
                "subject": "historia",
                "grades": [2, 3, 3, 2, 4, 2]
            }
        ]
    }
]


def find_student_by_name(name):
    for student in students:
        if student["name"] == name:
            return student


def if_student_in_school(name):
    if not find_student_by_name(name):
        return False
    return True