from django.urls import path

from profiles.views import CreateProfileView, AllProfilesView

app_name = "profiles"

urlpatterns = [
    path("create/", CreateProfileView.as_view(), name="create_profile"),
    path("all/", AllProfilesView.as_view(), name="all_profiles"),
]
