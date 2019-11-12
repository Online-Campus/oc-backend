from django.contrib.auth.models import BaseUserManager

class ProfileManager(BaseUserManager):
  use_in_migrations = True

  def _create_user(self, password, **extra_fields):
    if not password:
      raise ValueError('Err!')
    user = self.model(**extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, password, **extra_fields):
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(password, **extra_fields)

  def create_superuser(self, password, **extra_fields):
    extra_fields.setdefault('is_superuser', True)
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True.')
    return self._create_user(password, **extra_fields)  