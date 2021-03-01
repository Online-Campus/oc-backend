from .models import Profile
from rest_framework import serializers
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from string import Template

# HTML templates for emails
verification_subject = Template('Hi $name, please verify your account for Online Campus.')
verification_content = Template('Greetings $name!<br>Please verify your account for Online Campus <a href=\'https://201751025.pythonanywhere.com/auth/verify/$pk\'>here</a>.<br>Regards,<br>Online Campus Team')

# Serializer for student user
class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = '__all__'
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = Profile.objects.create_user(**validated_data)

    # Send verification mail
    mail = Mail(
      from_email='verify@onlinecampus.com',
      to_emails=user.email,
      subject=verification_subject.substitute(name=user.first_name),
      html_content=verification_content.substitute(name=user.first_name, pk=user.pk))

    try:
      # Send mail using Sendgrid
      # API key stored in .env
      sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
      res = sg.send(mail)
    except Exception as e:
      print(e)

    if user.account_type != "student":
      admins = Profile.objects.filter(is_staff=True)
      for admin in admins:
        # TODO: Send emails for admin verification of accounts
        print(admin.email)
    return user

  def validate(self, data):
    if data['first_name'] == '':
      return serializers.ValidationError('First name is a required field')
    if data['last_name'] == '':
      return serializers.ValidationError('Last name is a required field')
    return data

  def update(self, instance, validated_data):
    instance.first_name = validated_data.get('first_name', instance.first_name)
    instance.last_name = validated_data.get('last_name', instance.last_name)
    instance.birth_date = validated_data.get('birth_date', instance.birth_date)
    instance.bio = validated_data.get('bio', instance.bio)
    instance.save()
    return instance
