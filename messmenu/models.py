from django.db import models

# Create your models here.
class MessMenu(models.Model):
  monday_breakfast = models.TextField()
  monday_lunch = models.TextField()
  monday_snacks = models.TextField()
  monday_dinner = models.TextField()
  
  tuesday_breakfast = models.TextField()
  tuesday_lunch = models.TextField()
  tuesday_snacks = models.TextField()
  tuesday_dinner = models.TextField()

  wednesday_breakfast = models.TextField()
  wednesday_lunch = models.TextField()
  wednesday_snacks = models.TextField()
  wednesday_dinner = models.TextField()

  thursday_breakfast = models.TextField()
  thursday_lunch = models.TextField()
  thursday_snacks = models.TextField()
  thursday_dinner = models.TextField()

  friday_breakfast = models.TextField()
  friday_lunch = models.TextField()
  friday_snacks = models.TextField()
  friday_dinner = models.TextField()

  saturday_breakfast = models.TextField()
  saturday_lunch = models.TextField()
  saturday_snacks = models.TextField()
  saturday_dinner = models.TextField()

  sunday_breakfast = models.TextField()
  sunday_lunch = models.TextField()
  sunday_snacks = models.TextField()
  sunday_dinner = models.TextField()
