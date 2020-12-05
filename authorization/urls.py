from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView

from authorization import views

app_name = 'authorization'

urlpatterns = [
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='authorization/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
