from django.db import models


class pro(models.Model):
    name = models.CharField(max_length=500)
    job = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.name