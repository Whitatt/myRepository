from django.db import models


class djangoClasses(models.Model):# defines the class
    Title = models.CharField(max_length=30) # This defines the title of the classes
    CourseNumber = models.IntegerField() # provides the numbered course
    InstructorName = models.CharField(max_length=30) # this is text string
    Duration = models.DecimalField(max_digits=3, decimal_places=1) # validates that the given value is a decimal


objects = models.Manager() # the model manager


A = djangoClasses(Title='Math', CourseNumber=10, InstructorName='Mr. Jenkins', Duration=1.0)
A.save()
B = djangoClasses(Title='English', CourseNumber=15, InstructorName='Ms. Santos', Duration=1.0)
B.save()
C = djangoClasses(Title='Science', CourseNumber=20, InstructorName='Mr. Farkle', Duration=1.0)
C.save()

# title indicates math in addition to the course number, instr name and duration of class
# repeated 3 times by accident/providing multiple rows and columns.