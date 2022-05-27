from django.db import models


class Parameter(models.Model):
    parameter = models.CharField(max_length=12, unique=True)

    class Meta:
        ordering = ('parameter',)

    def __str__(self):
        return self.parameter
