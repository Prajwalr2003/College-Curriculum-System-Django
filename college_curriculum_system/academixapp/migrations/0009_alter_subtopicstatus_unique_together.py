# Generated by Django 5.0.2 on 2024-03-17 21:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academixapp', '0008_alter_subtopicstatus_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subtopicstatus',
            unique_together={('user', 'subtopic')},
        ),
    ]