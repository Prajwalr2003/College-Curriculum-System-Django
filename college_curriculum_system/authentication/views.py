from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import View
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse
from .models import Profile


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('confirm_password', '')
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('auth:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('auth:signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.is_active = False
                user.save()
                profile = Profile.objects.create(user=user, email=email)
                current_site = get_current_site(request)
                mail_subject = 'Activate your account'
                message = render_to_string('authentication/activate.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': str(urlsafe_base64_encode(force_bytes(user.pk))),
                    'token': default_token_generator.make_token(user),
                })

                print(str(urlsafe_base64_encode(force_bytes(user.pk))))
                to_email = email
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()

                messages.success(request, 'Please check your email to activate your account.')
                return redirect('auth:login')
        else:
            messages.error(request, 'Password does not match')
    
    return render(request, 'authentication/signup.html')

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            print(uid)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            uid = None
            user = None
        
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Your account has been activated successfully.')
            return redirect(reverse('login'))
        
        messages.error(request, 'Invalid activation link. Please contact support for assistance.')
        return render(request, 'authentication/activatefail.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user_type = request.POST.get('student','')

        user = auth.authenticate(username=username, password=password, user_type=user_type)
        
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('auth:login')
    else:
        return render(request, 'authentication/login.html')

@login_required(login_url='auth:login')
def logout(request):
    auth.logout(request)
    return redirect('auth:login')

@login_required(login_url='auth:login')
def change_profile_image(request):
    print("Change Image")
    if request.method == 'POST':
        profile = request.user.profile
        if 'profile_img' in request.FILES and request.FILES['profile_img']:
            profile.profile_img = request.FILES['profile_img']
        profile.save()
        return redirect('auth:myprofile')
    return redirect('auth:myprofile')

@login_required(login_url='auth:login')
def remove_profile_image(request):
    print("Remove Image")
    if request.method == 'POST':
        profile = request.user.profile
        if profile.profile_img and profile.profile_img.name != 'user_images/default.png':
            profile.profile_img.delete(save=False)
        profile.profile_img = 'user_images/default.png'
        profile.save()
        return redirect('auth:myprofile')
    return redirect('auth:myprofile')

@login_required(login_url='auth:login')
def delete_user(request):
    user = request.user
    user.delete()
    auth.logout(request)
    return redirect('auth:login')
