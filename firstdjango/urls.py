"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Including my django app called Portfolios, and all its urls. - preferred method, as it encapsulates the portfolio stuff in the portfolio files.
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^blog/', include('blog.urls')),

    #the following would be to directly list a url for a view in the portfolio app - not recommended
    url(r'^$', views.home, name='home'),

]
