from django.urls import path

from .views import IssueListView

urlpatterns = [
    path('', IssueListView.as_view(), name='list')
]