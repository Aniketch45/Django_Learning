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
    
'''python manage.py shell
 from studapp.models import Student
>>> Student.objects.create(first_name="Aniket",last_name="Chafekar",roll_no='49',age='21',email="Abc1234@gmail.com",dob='2004-12-02',address="Vaijpur")
    Student.objects.all()
    Student.objects.filter(age='19')
    Student.objects.all().order_by('roll_no')
     Student.objects.all().order_by('-roll_no')
      s1=Student.objects.get(roll_no='3')
>>> s1.delete()'''