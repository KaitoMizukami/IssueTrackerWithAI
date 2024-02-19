from django.urls import path

from .views import CreateTeamView, EnterTeamView, TeamListView, TeamIssueListView, TeamIssueCreateView

app_name = 'teams'

urlpatterns = [
    path('create/', CreateTeamView.as_view(), name='create'),
    path('enter/', EnterTeamView.as_view(), name='enter'),
    path('list/', TeamListView.as_view(), name='list'),
    path('<int:pk>/issues', TeamIssueListView.as_view(), name='issues'),
    path('<int:pk>/issues/create', TeamIssueCreateView.as_view(), name='create-issues'),
]