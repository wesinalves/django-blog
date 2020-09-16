from django.urls import include, path
from . import views

app_name = 'users'

urlpatterns = [
    # Login page
    path('login/', include('django.contrib.auth.urls')),
    
    # Logout page
    path('logout/', views.logout_view, name='logout'),

    # Registration
    path('register/', views.register, name='register'),


    ]