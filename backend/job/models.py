from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.geos import Point
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.gis.db import models as gismodels
from django.contrib.auth.models import User
from datetime import *
# Create your models here.

def return_date_time():
    now = datetime.now()
    return now + timedelta(days=10)

class JobType(models.TextChoices):
    Permanent = 'Permanent'
    Temporary = 'Temporary'
    Internship = 'Internship'

class Education(models.TextChoices):
    Bachelor = 'Bachelor'
    Master = 'Master'
    PhD = 'PhD'

class Industry(models.TextChoices):
    Business = 'Business'
    IT = 'Information Technology'
    Banking = 'Banking'
    Education = 'Education'
    Telecommunication = 'Telecommunication'
    Other = 'Other'

class Experience(models.TextChoices):
    NO_EXPERIENCE = 'No Experience'
    ONE_YEAR = 'One Year'
    TWO_YEARS = 'Two Years'
    THREE_YEARS_PLUS = 'Three Years Above'

class Job(models.Model):
    tittle =models.CharField(max_length=200, null=True)
    description =models.CharField(null=True)
    email = models.EmailField(null=True)
    address =models.CharField(max_length=100, null=True)
    jobType = models.CharField(max_length=10, choices=JobType.choices, default=JobType.Permanent)
    education = models.CharField(max_length=10, choices=Education.choices, default=Education.Bachelor)
    industry = models.CharField(max_length=30, choices=Industry.choices, default=Industry.Business)
    experience = models.CharField(max_length=20, choices=Experience.choices, default=Experience.NO_EXPERIENCE)
    salary = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)], default=1)
    positions = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True)
    point = gismodels.PointField(default=Point(0.0, 0.0))
    lastDate = models.DateTimeField(default=return_date_time)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)