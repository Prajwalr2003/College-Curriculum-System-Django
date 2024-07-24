from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Unit, Subtopic, Enrollment, SubtopicStatus
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from authentication.models import Profile
from django.urls import reverse

# Create your views here.

def index(request):
    course = Course.objects.all()
    return render(request, 'academixapp/index.html', {'course':course})

@login_required(login_url='auth:login')
def add_course(request):
    instructor = request.user
    if request.method == 'POST':
        course = Course.objects.create(
            course_title = request.POST['course_title'],
            course_desc = request.POST['course_desc'],
            course_branch = request.POST['course_branch'],
            course_year = request.POST['course_year'],
            course_img = request.FILES['course_img'],
            course_benefit = request.POST['course_benefit'],
            course_req = request.POST['course_req'],
            instructor = instructor,
        )
        return redirect(reverse('academixapp:add_syllabus', kwargs={'slug': course.slug}))
    
    return render(request, 'academixapp/add_course.html')

def courses(request, course_branch):
    course_list = Course.objects.all()
    return render(request, 'academixapp/courses.html',{'course_list':course_list, 'course_branch':course_branch})

def view_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST' and request.user.is_authenticated:
        enrollment_exist = Enrollment.objects.filter(user=request.user, course=course).exists()
        if enrollment_exist:
            messages.info(request, "You have already enrolled in this course")
        else:
            enrollment = Enrollment(user=request.user, course=course)
            enrollment.save()
            return redirect('academixapp:enrolledcourses')

    return render(request, 'academixapp/view_course.html', {'course':course})

def edit_course(request, slug):
    course = Course.objects.get(slug=slug)
    if request.method == 'POST':
        course_title = request.POST.get('course_title','')
        course_desc = request.POST.get('course_desc','')
        course_branch = request.POST.get('course_branch','')
        course_year = request.POST.get('course_year','')
        course_img = request.FILES.get('course_img','')
        course_benefit = request.POST.get('course_benefit','')
        course_req = request.POST.get('course_req','')
        
        course.course_title = course_title
        course.course_desc = course_desc
        course.course_branch = course_branch
        course.course_year = course_year
        if course_img:
            course.course_img = course_img
        course.course_benefit = course_benefit
        course.course_req = course_req
        course.save()
        return redirect(reverse('academixapp:add_syllabus', kwargs={'slug': course.slug}))
    return render(request, 'academixapp/editcourse.html', {'course':course})
  
def delete_course(request, slug):
    course = Course.objects.get(slug=slug)
    course.delete()
    return redirect('academixapp:mycourses')

@login_required(login_url='auth:login')
def add_syllabus(request, slug):

    course = get_object_or_404(Course, slug=slug)
    
    if request.method == 'POST':
        course = Course.objects.get(slug=slug)
        unit_titles = []
        subtopic_titles = []

        for key, value in request.POST.items():
            if key.startswith('unit_titles_'):
                unit_number = key.split('_')[2] 
                unit_titles.append(value)
                subtopic_number = 1
                subtopic_key = f'unit_{unit_number}_subtopic_titles_{subtopic_number}'
                unit_subtopics = [value]
                while subtopic_key in request.POST:
                    unit_subtopics.append(request.POST[subtopic_key])
                    subtopic_number += 1
                    subtopic_key = f'unit_{unit_number}_subtopic_titles_{subtopic_number}'
                subtopic_titles.append(unit_subtopics)

        for unit_title, unit_subtopics in zip(unit_titles, subtopic_titles):
            unit = Unit.objects.create(title=unit_title, course=course)
            for subtopic_title in unit_subtopics:
                Subtopic.objects.create(title=subtopic_title, unit=unit)

        return redirect('academixapp:mycourses')
    
    return render(request, 'academixapp/add_syllabus.html', {'course': course})

@login_required(login_url='auth:login')
def editprofile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        contact_number = request.POST.get('contact_number', '')
        roll_number = request.POST.get('roll_number', '')
        year = request.POST.get('year', '')
        branch = request.POST.get('branch', '')

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        profile, created = Profile.objects.get_or_create(user=user)
        profile.contact_number = contact_number
        profile.roll_number = roll_number
        profile.year = year
        profile.branch = branch
        profile.save()

        return redirect('auth:myprofile')

    return render(request, 'academixapp/editprofile.html')

@login_required(login_url='auth:login')    
def mycourses(request):
    added_course = Course.objects.filter(instructor=request.user)
    return render(request, 'academixapp/mycourse.html', {'added_course':added_course})

@login_required(login_url='auth:login')
def enrolledcourses(request):
    enrolled_courses = Enrollment.objects.filter(user=request.user)
    return render(request, 'academixapp/enrolledcourses.html', {'enrolled_courses': enrolled_courses})

def delete_enrollment(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    enrollment.delete()
    return redirect('academixapp:enrolledcourses')

def update_subtopic_status(request):
  if request.method == 'POST':
    # Get data from the request body
    subtopic_id = request.POST.get('subtopic_id')
    new_status = request.POST.get('new_status')

    try:
      # Fetch the subtopic object
      subtopic = Subtopic.objects.get(pk=subtopic_id)
      # Update the subtopic status
      subtopic.status = new_status
      subtopic.save()
      # Return success response
      return JsonResponse({'message': 'Subtopic status updated successfully!'})
    except Subtopic.DoesNotExist:
      # Handle case where subtopic is not found
      return JsonResponse({'error': 'Subtopic not found'}, status=404)
    except Exception as e:
      # Handle other errors
      print(f"Error updating subtopic status: {e}")
      return JsonResponse({'error': 'An error occurred while updating status'}, status=500)
  else:
    # Handle non-POST requests (e.g., GET)
    return JsonResponse({'error': 'Invalid request method'}, status=405)




