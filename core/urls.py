from django.urls import path
from .views import blackboard_view

urlpatterns = [
    path('', blackboard_view, name='blackboard'),
]
