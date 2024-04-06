from django.db import models

# Create your models here.
class Books(models.Model):
    BookID = models.IntegerField(default = None, primary_key=True)
    BookName = models.CharField(default = None, max_length=100)
    NumberOfCopies = models.IntegerField(default = None)



class Members(models.Model):
    MemberID = models.IntegerField(default = None, primary_key=True)
    MemberName = models.CharField(default = None, max_length=100)


class Circulation(models.Model):
    EventType = models.IntegerField(default = None)
    BookId =  models.IntegerField(default = None)
    MemberId = models.IntegerField(default = None)
    Date = models.DateField(default=None)


class CirculationHistory(models.Model):
    EventType = models.IntegerField(default = None)
    BookId = models.IntegerField(default = None)
    MemberId = models.IntegerField(default = None)
    Date = models.DateField(default=None)

    