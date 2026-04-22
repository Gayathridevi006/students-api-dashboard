# students/management/__init__.py       (empty)
# students/management/commands/__init__.py  (empty)

# students/management/commands/seed_students.py
from django.core.management.base import BaseCommand
from students.models import Student

SEED_DATA = [
    {'name': 'Aarav Sharma',  'age': 16, 'grade': '10A', 'email': 'aarav@school.edu'},
    {'name': 'Priya Nair',    'age': 15, 'grade': '9B',  'email': 'priya@school.edu'},
    {'name': 'Rohit Verma',   'age': 17, 'grade': '11C', 'email': 'rohit@school.edu'},
    {'name': 'Sneha Iyer',    'age': 14, 'grade': '8A',  'email': 'sneha@school.edu'},
    {'name': 'Kabir Mehta',   'age': 18, 'grade': '12B', 'email': 'kabir@school.edu'},
    {'name': 'Ananya Reddy',  'age': 16, 'grade': '10C', 'email': 'ananya@school.edu'},
]

class Command(BaseCommand):
    help = 'Seed 6 initial students'

    def handle(self, *args, **kwargs):
        if Student.objects.exists():
            self.stdout.write('Students already seeded. Skipping.')
            return
        for s in SEED_DATA:
            Student.objects.create(**s)
        self.stdout.write(self.style.SUCCESS('✓ Seeded 6 students'))