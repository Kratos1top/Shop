from django.urls import path
from auth_app.views import RegisterView, LoginView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
]
