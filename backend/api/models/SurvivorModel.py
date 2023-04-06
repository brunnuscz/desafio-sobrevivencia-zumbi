from django.db import models


class SurvivorModel(models.Model):
    class Meta:
        db_table = 'survivors'
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    contaminated = models.BooleanField(default=False)
    amountAlerts = models.IntegerField(default=0)

    def __str__(self):
        return self.name
