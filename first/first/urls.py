"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from firstapp.models import userOBJ

class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        #1)
        requested_id = request.POST['login_id']
        requested_pw = request.POST['login_pw']
        """
        for member in userOBJ.objects.all():
            requested_id == member.user
        """
        """
        accinfo = [request.POST['login_id'],request.POST['login_pw']]
        accinfo = []
        accinfo.append(request.POST['login_id'])
        accinfo.append(request.POST['login_pw'])
        if request.POST['login_id'] == userOBJ.user:
        """


class VpsDetail(TemplateView):
    template_name = 'vps_detail.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^vps_detail/', VpsDetail.as_view())
]
