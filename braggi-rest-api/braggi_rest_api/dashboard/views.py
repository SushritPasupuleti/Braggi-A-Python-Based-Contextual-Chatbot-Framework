from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_api.Braggi_Engine import Run
from django.template import Context, loader
from django.http import HttpResponse


class DashboardHomeView(LoginRequiredMixin, TemplateView):
    login_url = '/api-admin/login/'
    redirect_field_name = '/api-admin/login/'

class TrainView(TemplateView):
    template_name="dashboard/success.html"
    login_url = '/api-admin/login/'
    redirect_field_name = '/api-admin/login/'

    def get(self, request):
        self.train()
        return render(request, 'dashboard/success.html', {'Operation': 'Training'})

    def train(self):
        Run.Run_Model('admin-override-input=null', Trained=False)

class ChatListView(TemplateView):
    template_name="dashboard/chat_logs.html"
    login_url = '/api-admin/login/'
    redirect_field_name = '/api-admin/login/'