from django.db import models

HOUR = [
    ('1', '1:00'),
    ('3', '3:00'),
    ('5', '5:00'),
    ('7', '7:00'),
    ('9', '9:00'),
    ('11', '11:00'),
    ('13', '13:00'),
    ('15', '15:00'),
    ('17', '17:00'),
    ('19', '19:00'),
    ('21', '21:00'),
    ('23', '23:00'),
]


class Eta1(models.Model):
    date = models.DateField(auto_now=False, blank=False, unique_for_date=True)
    hour = models.TimeField('Hora', choices=HOUR, blank=True)
    parameter = models.ForeignKey(
        'Parameter',
        on_delete=models.CASCADE,
        blank=True
    )


class Parameter(models.Model):
    parameter = models.CharField(max_length=12, unique=True)
    stage = models.ForeignKey(
        'Stage',
        on_delete=models.CASCADE,
        blank=True
    )

    class Meta:
        ordering = ('parameter',)

    def __str__(self):
        return self.parameter


class Stage(models.Model):
    raw = models.DecimalField('Bruta', max_digits=4, decimal_places=2)
    decanted = models.DecimalField('Decantada', max_digits=4, decimal_places=2)
    treated = models.DecimalField('Tratada', max_digits=4, decimal_places=2)
    output = models.DecimalField('saida', max_digits=4, decimal_places=2)

