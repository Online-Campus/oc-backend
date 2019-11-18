from django.db import models
from accounts.models import Profile

# Create your models here.

COMPLAINT_STATUS = [
  ('submitted', 'Submitted'),
  ('processing', 'Processing'),
  ('closed', 'Closed')
]

# Complaint model
class Complaint(models.Model):
  title = models.CharField(max_length=256, blank=False, null=False,)
  owner = models.ForeignKey(Profile, related_name="created_by_owner", on_delete=models.CASCADE, blank=True)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=20, choices=COMPLAINT_STATUS, default="submitted")
  remark = models.TextField(blank=True)

  def __str__(self):
    return "%s, %s" % (self.title, self.owner.username)