from django.db import models
from accounts.models import Profile

LEAVE_STATUS = [
  ('submitted', 'Submitted'),
  ('accepted', 'Accepted'),
  ('rejected', 'Rejected')
]

# Create your models here.
class Leave(models.Model):
  owner = models.ForeignKey(Profile, related_name="leave_created_by_owner", on_delete=models.CASCADE, blank=True)
  reason = models.TextField()
  location = models.TextField()
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=20, choices=LEAVE_STATUS, default="submitted")