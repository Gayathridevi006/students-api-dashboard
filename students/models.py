from django.db import models


class Student(models.Model):
    """
    Schema — 6 columns:
      id          → AutoField (PK, auto)
      name        → CharField
      age         → IntegerField
      grade       → CharField  (e.g. "10A")
      email       → EmailField (unique)
      enrolled_at → DateField
    """
    name        = models.CharField(max_length=100)
    age         = models.IntegerField()
    grade       = models.CharField(max_length=10)
    email       = models.EmailField(unique=True)
    enrolled_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'students'
        ordering = ['id']

    def __str__(self):
        return f"{self.name} ({self.grade})"
    
