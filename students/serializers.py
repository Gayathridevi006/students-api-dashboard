from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'grade', 'email', 'enrolled_at']
        read_only_fields = ['id', 'enrolled_at']

    def validate_age(self, value):
        if not (5 <= value <= 25):
            raise serializers.ValidationError("Age must be between 5 and 25.")
        return value