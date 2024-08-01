from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Course(models.Model):
    def __str__(self):
        return self.course_title
    
    course_title = models.CharField(max_length=100)
    course_desc = models.TextField()
    course_branch = models.CharField(max_length=100, default='COMPSA')
    course_year = models.CharField(max_length=100, default='FY')
    course_img = models.ImageField(default='default.jpg', upload_to='course_images/')
    course_benefit = models.TextField()
    course_req = models.TextField()
    date_created = models.DateTimeField(default=datetime.now)  
    slug = models.SlugField(unique=True, blank=True, default='')
    course_credit = models.IntegerField(default=0)
    course_tutorial = models.IntegerField(default=0)
    course_lectures = models.IntegerField(default=0)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.course_title)
            self.slug = base_slug
            counter = 1

            while Course.objects.filter(slug=self.slug).exists():
                # Append a unique identifier (counter) to the slug
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

class Unit(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name='units', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Subtopic(models.Model):
    title = models.CharField(max_length=255)
    unit = models.ForeignKey(Unit, related_name='subtopics', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class SubtopicStatus(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Done', 'Done'),
        ('Revisit', 'Revisit'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    class Meta:
        unique_together = ['user', 'subtopic']

    def __str__(self):
        return f"{self.user.username} - {self.subtopic.title} - {self.status}"

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.course_title}"



