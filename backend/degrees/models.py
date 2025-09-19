# backend/degrees/models.py

from django.db import models

class Degree(models.Model):
    student_name = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    degree_title = models.CharField(max_length=255)
    issued_date = models.DateField()
    hash_on_chain = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.student_name} - {self.degree_title}"
