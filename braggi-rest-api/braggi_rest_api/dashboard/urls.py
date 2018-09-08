from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from dashboard.views import DashboardHomeView, TrainView, ChatListView

urlpatterns = [
    url( r'^login/$', LoginView.as_view(template_name="dashboard/login.html"), name="login"),
    url(r'^retrain-model/$', TrainView.as_view(), name="retrain-model"),
    url(r'^see-chats/$', ChatListView.as_view(), name="see-chats"),
    url( r'^', DashboardHomeView.as_view(template_name="dashboard/home.html")),
]