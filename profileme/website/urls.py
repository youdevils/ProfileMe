from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("", views.WhoAmI.as_view(), name="WhoAmI"),
    path("results/", views.Results.as_view(), name="Results"),
]
