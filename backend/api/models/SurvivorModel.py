from django.db import models


class SurvivorModel(models.Model):
    class Meta:
        db_table = 'survivors'
    
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3)
    sex = models.CharField()
    longitude = models.CharField()
    latitude = models.CharField()
    state = models.BooleanField(default=False)
    countAlerts = models.IntegerField(default=0)

    def __str__(self):
        return self.name
