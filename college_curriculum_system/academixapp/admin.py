from django.contrib import admin
from .models import Course, Unit, Subtopic, Enrollment, SubtopicStatus

# Register your models here.
admin.site.register(Course)
admin.site.register(Unit)
admin.site.register(Subtopic)
admin.site.register(Enrollment)
admin.site.register(SubtopicStatus)