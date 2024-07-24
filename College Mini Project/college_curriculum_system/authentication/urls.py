from django.urls import path
from authentication import views
app_name = 'auth'

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(), name='activate'),
    path('myprofile/',views.myprofile, name='myprofile'),
]
