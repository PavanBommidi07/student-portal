from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=20)
    marks = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name
