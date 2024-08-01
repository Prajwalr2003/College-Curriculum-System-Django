from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    def __str__(self):
        return self.user.username
    
    USER_TYPE_CHOICES = [
        ('STUDENT', 'student'),
        ('TEACHER', 'teacher'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    year = models.CharField(max_length=100, default='')
    branch = models.CharField(max_length=100, default='')
    roll_number = models.CharField(max_length=100)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='')
    profile_img = models.ImageField(default='default.png', upload_to='user_images/')