from django.db import models


class ItemModel(models.Model):
    class Meta:
        db_table = 'items'

    name = models.CharField(max_length=100)
    point = models.IntegerField()

    def __str__(self):
        return self.name
