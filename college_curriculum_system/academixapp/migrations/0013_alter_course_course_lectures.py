# Generated by Django 5.0.2 on 2024-07-31 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academixapp', '0012_course_course_credit_course_course_lectures_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_lectures',
            field=models.IntegerField(default=0),
        ),
    ]
