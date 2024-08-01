from django.urls import path
from academixapp import views

app_name = 'academixapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-course/', views.add_course, name='add_course'),
    path('add-syllabus/<slug:slug>', views.add_syllabus, name='add_syllabus'),
    path('courses/<str:course_branch>/', views.courses, name='courses'),
    path('view-course/<slug:slug>', views.view_course, name='view_course'),
    path('edit-course/<slug:slug>', views.edit_course, name='edit_course'),
    path('delete-course/<slug:slug>', views.delete_course, name='delete_course'),
    path('mycourses/',views.mycourses, name='mycourses'),
    path('myprofile/',views.myprofile, name='myprofile'),
    path('enrolledcourses/',views.enrolledcourses, name='enrolledcourses'),
    path('delete-enrollment/<int:enrollment_id>/', views.delete_enrollment, name='delete_enrollment'),
    path('all-courses', views.all_courses, name='all_courses'),
    path('instructors', views.all_instructors, name='all_instructors'),
    path('notfound', views.notfound, name='notfound'),
]