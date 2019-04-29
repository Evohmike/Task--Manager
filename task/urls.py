from django.urls import path
from . import views
urlpatterns = [
    # path('', views.home),
    path('', views.TaskListView.as_view(), name='task_list'),
]
