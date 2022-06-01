from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from .manager import UserManager

# Create your models here.
class User(AbstractUser):
    username=None
    first_name=models.CharField(null=True, max_length=11, default="x")
    last_name=models.CharField(null=True, max_length=11, default="x")
    email=models.EmailField(unique=True, null=False)
    phone_no=models.CharField(max_length=11, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    objects=UserManager()
    REQUIRED_FIELDS=[]

class Program(models.Model):
    program = models.CharField(max_length=110)

    def __str__(self) :
        return self.program

class Department(models.Model):
    department = models.CharField(max_length=110)
    program = models.ForeignKey(Program, on_delete=models.RESTRICT )

    def __str__(self) :
        return self.department

class Club(models.Model):
    club = models.CharField(max_length=110)

    def __str__(self) :
        return self.club

YEAR_CHOICES = (
    ('FIRST','First Year'),
    ('SECOND','Second Year'),
    ('THIRD','Third Year'),
    ('FOURTH','Fourth Year'),
)

class Year(models.Model):
    year = models.CharField(max_length=110, choices=YEAR_CHOICES)

    def __str__(self) :
        return self.year

class College(models.Model):
    college = models.CharField(max_length=122)
    address = models.CharField(max_length=250)
    university = models.CharField(max_length=20)

    def __str__(self) :
        return self.college

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    college = models.ForeignKey(College,  on_delete=models.RESTRICT)
    program = models.ForeignKey(Program,  on_delete=models.RESTRICT)
    department = models.ForeignKey(Department,  on_delete=models.RESTRICT)
    year = models.ForeignKey(Year,  on_delete=models.RESTRICT)

    def __str__(self) :
        return self.user

class Staffadmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    college = models.ForeignKey(College,  on_delete=models.RESTRICT)
    program = models.ForeignKey(Program,  on_delete=models.RESTRICT)
    department = models.ForeignKey(Department,  on_delete=models.RESTRICT)
    year = models.ForeignKey(Year,  on_delete=models.RESTRICT)
    club = models.ForeignKey(Club,  on_delete=models.RESTRICT)

    def __str__(self) :
        return self.user

class Events(models.Model):
    event = models.CharField(max_length=110)
    college = models.ForeignKey(College,  on_delete=models.RESTRICT)
    date_time = models.DateTimeField()
    tg_audience = models.CharField(max_length=225)
    event_desc = models.CharField(max_length=700)
    venue = models.CharField(max_length=200)
    
    def __str__(self) :
        return self.event

class Event_reg(models.Model):
    eventuser = models.ForeignKey(Profile, on_delete=models.RESTRICT)
    event = models.ForeignKey(Events, on_delete=models.RESTRICT)
    
    def __str__(self) :
        return self.eventuser

class Notice(models.Model):
    notice_title = models.CharField(max_length=225)
    notice_date = models.DateTimeField()
    notice_desc = models.CharField(max_length=225)
    notice_college = models.ForeignKey(College, on_delete=models.RESTRICT)
    notice_dept = models.ForeignKey(Department, on_delete=models.RESTRICT)
    notice_year = models.ForeignKey(Year, on_delete=models.RESTRICT)

    def __str__(self) :
        return self.notice_title

class Notes(models.Model):
    notes_subject = models.CharField(max_length=265)
    notes_college = models.ForeignKey(College, on_delete=models.RESTRICT)
    notes_dept = models.ForeignKey(Department, on_delete=models.RESTRICT)
    notes_year = models.ForeignKey(Year, on_delete=models.RESTRICT)

    def __str__(self) :
        return self.notes_subject

class Qpaper(models.Model):
    qpaper_subject = models.CharField(max_length=265)
    qpaper_college = models.ForeignKey(College, on_delete=models.RESTRICT)
    qpaper_dept = models.ForeignKey(Department, on_delete=models.RESTRICT)
    qpaper_year = models.ForeignKey(Year, on_delete=models.RESTRICT)

    def __str__(self) :
        return self.qpaper_college

class Placement(models.Model):
    company_name = models.CharField(max_length=265)
    qpaper_dept = models.ForeignKey(Department, on_delete=models.RESTRICT)
    qpaper_year = models.ForeignKey(Year, on_delete=models.RESTRICT)

    def __str__(self) :
        return self.company_name

