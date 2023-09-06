from django.db import models

# Create your models here.
class personal_information(models.Model):
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.content

class profesional_details(models.Model):
    details=models.TextField(max_length=2000)

    def __str__(self):
        return self.details

class Projects(models.Model):
    projects_name=models.TextField(max_length=2000)

    def __str__(self):
        return self.projects_name

