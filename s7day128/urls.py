"""s7day128 URL Configuration

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

from api.views import AuthView

from app01.views import users, StudentsView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/$', AuthView.as_view()),
    url(r'^users/', users),      # FBV=Function Base View
    url(r'^students/', StudentsView.as_view()),  # CBV=Class Base View
]
