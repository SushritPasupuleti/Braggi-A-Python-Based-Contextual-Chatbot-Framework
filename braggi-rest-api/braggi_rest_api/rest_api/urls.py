from django.conf.urls import url
from rest_api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^braggi/$', views.conversation_list),
    url(r'^braggi/(?P<pk>[0-9]+)/$', views.conversation_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)