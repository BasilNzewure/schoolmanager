from django.db import models
from django.conf import settings

# Create your models here.

class Courses(models.Model):
    course_categories = (
        ('CIIT', 'Certificate In Information Technology'),
        ('CIJP', 'Certificate In Java Programming'),
        ('ADJT', 'Application Development Using Java Technologies'),
        ('BBTCJP', 'Bin Binary Certified Java Programmer'),
        ('CIWD', 'Certificate In Website Development'),
        ('AWD', 'Advanced Website Development'),
        ('CIPM', 'Certificate In PHP/MySQL Development'),
        ('ADWF', 'Android Development With Flutter'),
        ('BBCCP', 'Bin Binary Certified C++ Programmer'),
        ('DBA', 'Database Administrator [DBA] Oracle 12C'),
        ('CIDM', 'Certificate In Digital Marketing'),
        ('CIPP', 'Certificate In Python Programming'),
        ('BBTCFD', 'Bin Binary Certified Full Stack Developer With Python Django'),
        ('BBTCSE', 'Bin Binary Technologies Certified Software Engineer')
    )

    duration = (
        ('2 Months', '2 Months'), 
        ('3 Months', '3 Months'), 
        ('4 Months', '4 Months'), 
        ('5 Months', '5 Months'), 
        ('6 Months', '6 Months'), 
        ('8 Months', '8 Months'), 
        ('One Year', 'One Year')
        )

    faculty = (
        ('Basil Nzewure', 'Mr Basil Nzewure'), 
        ('Stanley Surname', 'Stanley Surname'), 
        ('Jude Nzewure', 'Jude Nzewure'), 
        ('Chioma Nzewure', 'Chioma Nzewure'), 
        ('Theresa Nzewure', 'Theresa Nzewure')
    )


    id = models.IntegerField(primary_key = True)
    course_name = models.CharField("Course Name", max_length = 100, choices = course_categories)
    duration = models.CharField("Duration", max_length = 100, choices=duration)
    faculty = models.CharField("Faculty", max_length=200, choices=faculty)

    def __str__(self):
        return f"{self.id}, {self.course_name} For {self.duration} By {self.faculty}"


class BookCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    commence_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user}, {self.course} From {self.commence_date} To {self.end_date}"

