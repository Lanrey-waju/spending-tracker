from django.urls import path, include

from .views import HomePageView

app_mame = "tracker"

urlpatterns = [
    path("", HomePageView.as_view(), name="home")
]
