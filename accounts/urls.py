from django.urls import include, path

from accounts import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("signup/", views.SignupPageView.as_view(), name="signup"),
]
