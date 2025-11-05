from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    roll_no = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField()
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name},{self.roll_no},{self.age},{self.email}"
