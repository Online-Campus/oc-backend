from django.db import models

# Create your models here.
class Date(models.Model):
  exam_link = models.TextField()
  holiday_link = models.TextField()
  academic_link = models.TextField()