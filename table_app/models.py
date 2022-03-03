from django.db import models

class TableData(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    distance = models.FloatField(max_length=255)

    def __str__(self):
        return self.name

