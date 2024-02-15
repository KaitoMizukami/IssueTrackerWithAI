from django.urls import path

from .views import CreateTeamView, EnterTeamView

app_name = 'teams'

urlpatterns = [
    path('create/', CreateTeamView.as_view(), name='create'),
    path('enter/', EnterTeamView.as_view(), name='enter'),
]