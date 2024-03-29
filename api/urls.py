from django.urls import path
from .views import RegisterView, LoginView, TestView
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('history/', TestView.as_view()),
]

