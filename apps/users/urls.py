from django.urls import path
# VIEWS
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [

    path('signUp/', views.SignUp.as_view(), name = 'signup'),
    path('accounts/login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),

]