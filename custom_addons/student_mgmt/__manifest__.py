{
    'name': 'Student Management System',
    'version': '1.0',
    'summary': 'Manage student records',
    'description': """
        Student Management System
        =========================
        A simple module to manage student details:
        - Student Name
        - Date of Birth
        - Parent's Name
        - Address
        - Class
    """,
    'category': 'Education',
    'author': 'Mohan',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
    ],
    'installable': True,
    'application': True,
}
