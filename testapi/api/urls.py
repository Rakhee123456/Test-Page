
from django.urls import path
from .views import StudentApiView
urlpatterns = [
    path("",StudentApiView.as_view(),name="student"),

]
