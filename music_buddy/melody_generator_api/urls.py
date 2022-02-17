from django.urls import path
from .views import main
from .views import UserNew
from .views import UserIndex

urlpatterns = [
  path('', main),
  path('users/new', UserNew.as_view()),
  path('users/index', UserIndex.as_view()),
]