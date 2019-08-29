from django.db import models


class Poets(models.Model):
    p_id = models.IntegerField()
    name = models.CharField(max_length=50)
    pic = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    biography = models.TextField()

    def __str__(self):
        return self.name
