from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import ProfileManager

# Account types
ACCOUNT_TYPES = [
  ("student", "Student"),
  ("faculty", "Faculty"),
  ("hostel_staff", "Hostel Staff"),
  ("mess_staff", "Mess Staff"),
]

# User model
class Profile(AbstractUser):
  bio = models.TextField(max_length=256, blank=True)
  birth_date = models.DateField(blank=True, null=True)
  contact_no = models.CharField(max_length=10, blank=True)
  created_at = models.DateTimeField(auto_now=True)
  account_type = models.CharField(max_length=15, choices=ACCOUNT_TYPES, default="student")
  is_verified = models.BooleanField(default=False)
  student_id = models.CharField(max_length=16, blank=True)

  # User custom manager
  objects = ProfileManager()

  class Meta:
    verbose_name = "profile"
    verbose_name_plural = "profiles"

  def __str__(self):
    return "%s %s, %s" % (self.first_name, self.last_name, self.username)