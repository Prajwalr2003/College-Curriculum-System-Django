# Generated by Django 5.0.2 on 2024-03-17 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academixapp', '0007_subtopicstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopicstatus',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done'), ('Revisit', 'Revisit')], default='Pending', max_length=20),
        ),
    ]