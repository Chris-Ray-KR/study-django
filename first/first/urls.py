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
class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


from django.http import HttpResponse
def methodView(request):
    if request.method == 'GET':
        html = "<html><body>It is now</body></html>"
    return HttpResponse(html)

from django.views.generic import View
class MyView(View):
    def get(self, request):
        # 뷰 로직 작성
        return HttpResponse('result')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', HomeView.as_view()),
    url(r'^$', methodView),
]
