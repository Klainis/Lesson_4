from django.urls import path, include
from .views import index

urlpatterns = [
	path('lesson_4', index, name='lesson_4'),
]