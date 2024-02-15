from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView

from .models import Team
from .forms import TeamCreationForm, TeamEnterForm

# Create your views here.
class CreateTeamView(CreateView):
    models = Team
    template_name = 'teams/create.html'
    form_class = TeamCreationForm
    success_url = '/issues/'

    def post(self, request):
        team = Team(name=request.POST['name'], auth_code=request.POST['auth_code'])
        team.save()
        user = request.user
        team.users.add(user)
        team.save()
        return redirect('issues:list')


class EnterTeamView(FormView):
    models = Team 
    template_name = 'teams/enter.html'
    form_class = TeamCreationForm
    success_url = '/issues/'

    def post(self, request):
        auth_code = request.POST['auth_code']
        team_name = request.POST['name']
        team = Team.objects.filter(auth_code=auth_code, name=team_name)
        if team.exists():
            team = team.first()
            user = request.user
            team.users.add(user)
            team.save()
            return redirect('issues:list')
        else:
            return render(request, self.template_name, {'form': self.form_class, 'error': 'Invalid team name or authentication code'})