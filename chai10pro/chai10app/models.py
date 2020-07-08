from django.db import models

# Create your models here.
class Candidates(models.Model):
    CandidateID = models.CharField(max_length=30)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    PhoneNum= models.CharField(max_length=30)
