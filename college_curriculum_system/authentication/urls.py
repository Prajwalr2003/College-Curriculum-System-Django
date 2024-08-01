from django.urls import path
from authentication import views
app_name = 'auth'

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(), name='activate'),
    path('deleteAccount/',views.delete_user, name='delete_user' ),
    path('change-profile-image/', views.change_profile_image, name='change_profile_image'),
    path('remove-profile-image/', views.remove_profile_image, name='remove_profile_image'),
]
