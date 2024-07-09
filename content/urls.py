from django.urls import path

from content import views
from content.views import BlogView

urlpatterns = [
    path("", BlogView.as_view(), name="blog"),
    path("<int:pk>/", BlogView.as_view(), name="get-blog"),
]
