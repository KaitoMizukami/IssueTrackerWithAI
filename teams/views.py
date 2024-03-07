from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, ListView
import openai
import os
import environ
from pathlib import Path

from .models import Team, Issue
from .forms import TeamCreationForm, IssueCreateForm

# Create your views here.
class CreateTeamView(CreateView):
    models = Team
    template_name = 'teams/create.html'
    form_class = TeamCreationForm

    def post(self, request):
        team = Team(name=request.POST['name'], auth_code=request.POST['auth_code'])
        team.save()
        user = request.user
        team.users.add(user)
        team.save()
        return redirect('teams:list')


class EnterTeamView(FormView):
    models = Team 
    template_name = 'teams/enter.html'
    form_class = TeamCreationForm

    def post(self, request):
        auth_code = request.POST['auth_code']
        team_name = request.POST['name']
        team = Team.objects.filter(auth_code=auth_code, name=team_name)
        if team.exists():
            team = team.first()
            user = request.user
            team.users.add(user)
            team.save()
            return redirect('teams:list')
        else:
            return render(request, self.template_name, {'form': self.form_class, 'error': 'Invalid team name or authentication code'})


class TeamListView(ListView):
    model = Team
    template_name = 'teams/list.html'

    def get(self, request):
        u = request.user
        t = Team.objects.filter(users=u)
        return render(request, self.template_name, {'teams': t})


class TeamIssueListView(ListView):
    model = Team
    template_name = 'teams/issues.html'

    def get(self, request, pk):
        team = Team.objects.get(pk=pk)
        issues = team.issues.all()
        return render(request, self.template_name, {'issues': issues, 'team': team})
    

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

openai.api_key = env('OPENAI_API')

client = openai.Client(api_key=env('OPENAI_API'))

class TeamIssueCreateView(CreateView):
    form_class = IssueCreateForm
    template_name = 'teams/issue_create.html'
    model = Issue

    def get(self, request, pk):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, pk):
        team = Team.objects.get(pk=pk)
        issue = Issue(
            title=request.POST['title'],
            code=request.POST['code'], 
            description=request.POST['description'], 
            author=request.user
        )
        content = f"Title: {issue.title}\nCode: {issue.code}\nDescription: {issue.description}\n"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful engineer assistant."},
                {"role": "user", "content": content},
            ]
        )
        if "```" in response.choices[0].message.content:
            divied_code = response.choices[0].message.content.split('```')
            issue.chatGPT_response = divied_code[0]
            issue.chatGPT_code = divied_code[1]
        else:
            issue.chatGPT_response = response.choices[0].message.content
        issue.save()
        team.issues.add(issue)
        team.save()
        return redirect('teams:issues', pk=pk)