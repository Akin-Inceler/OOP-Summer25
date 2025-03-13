students = [
    {
        'first_name': 'Akin',
        'last_name': 'Inceler',
        'index_number': '35525',
        'nationality': 'Turkey',
        'starting_date': '01.09.2024',
        'courses': 'mathematic,physics,software'
    },
    {
        'first_name': 'Dom',
        'last_name': 'Tornetto',
        'index_number': '38546',
        'nationality': 'USA',
        'starting_date': '01.09.2024',
        'courses': 'mathematic,physics,software'
    },
    {
        'first_name': 'Yagami',
        'last_name': 'Fukushota',
        'index_number': '35824',
        'nationality': 'Japan',
        'starting_date': '01.09.2024',
        'courses': 'mathematic,physics,software'
    }
]

for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}, Index: {student['index_number']}")