from django.db import models

class Expense(models.Model):
  name = models.CharField(max_length = 200, blank=False)
  source = models.CharField(
    max_length = 1,
    choices = (
      ('F','Flight'),
      ('C','Car Rental'),
      ('H','Hotel')
    )
  )
  amount = models.DecimalField(
    max_digits = 15,
    decimal_places = 2,
    default = 0
  )
  date = models.DateField()

  def __unicode__(self):
    return self.name
