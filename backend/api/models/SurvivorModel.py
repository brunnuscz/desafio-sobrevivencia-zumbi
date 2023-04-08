from django.db import models


class SurvivorModel(models.Model):
    class Meta:
        db_table = 'survivors'
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    longitude = models.FloatField()
    latitude = models.FloatField()
    contaminated = models.BooleanField(default=False)
    reports = models.IntegerField(default=0)

    def __str__(self):
        return self.name
