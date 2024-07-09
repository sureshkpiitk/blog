from django.urls import path

from auth.views import UserView

urlpatterns = [
    path("", UserView.as_view())
]
