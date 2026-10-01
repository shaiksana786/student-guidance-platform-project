from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    BRANCH_CHOICES = (
        ('CSE', 'Computer Science & Engineering'),
        ('ECE', 'Electronics & Communication Engineering'),
        ('EEE', 'Electrical & Electronics Engineering'),
        ('MECH', 'Mechanical Engineering'),
        ('CIVIL', 'Civil Engineering'),
    )

    YEAR_CHOICES = (
        (1, '1st Year'),
        (2, '2nd Year'),
        (3, '3rd Year'),
        (4, '4th Year'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES, default='CSE')
    year = models.IntegerField(choices=YEAR_CHOICES, default=1)
    roll_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.branch}"


class CareerProgress(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    coding_awareness_visited = models.BooleanField(default=False)
    project_guidance_visited = models.BooleanField(default=False)
    hackathons_visited = models.BooleanField(default=False)
    jobs_internships_visited = models.BooleanField(default=False)
    roadmaps_visited = models.BooleanField(default=False)
    selected_career_goal = models.CharField(max_length=50, blank=True)
    completed_projects = models.IntegerField(default=0)
    certifications = models.IntegerField(default=0)
    internships = models.IntegerField(default=0)

    def __str__(self):
        return f"Progress - {self.student.user.username}"
