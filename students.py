students = [
    {
        'first_name': 'Akin',
        'last_name': 'Inceler',
        'index_number': '35525',
        'nationality': 'Turkey',
        'starting_date': '01.09.2024',
        'courses': ['mathematics', 'physics', 'software']
    },
    {
        'first_name': 'Dom',
        'last_name': 'Tornetto',
        'index_number': '38546',
        'nationality': 'USA',
        'starting_date': '01.09.2024',
        'courses': ['mathematics', 'physics', 'software']
    },
    {
        'first_name': 'Yagami',
        'last_name': 'Fukushota',
        'index_number': '35824',
        'nationality': 'Japan',
        'starting_date': '01.09.2024',
        'courses': ['mathematics', 'physics', 'software']
    }
]

def add_student(first_name, last_name, index_number, nationality, starting_date, courses):
    """Adds a new student to the students list."""
    new_student = {
        'first_name': first_name,
        'last_name': last_name,
        'index_number': index_number,
        'nationality': nationality,
        'starting_date': starting_date,
        'courses': courses  # Should be a list
    }
    students.append(new_student)
    print(f"Student {first_name} {last_name} added successfully!")

def display_students():
    """Displays all students in the list."""
    for student in students:
        print(f"Name: {student['first_name']} {student['last_name']}, Index: {student['index_number']}, Courses: {', '.join(student['courses'])}")