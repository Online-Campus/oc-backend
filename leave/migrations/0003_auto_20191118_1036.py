# Generated by Django 2.2.7 on 2019-11-18 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0002_leave_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(choices=[('submitted', 'Submitted'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='submitted', max_length=20),
        ),
    ]
