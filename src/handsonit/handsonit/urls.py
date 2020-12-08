"""handsonit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from pages.views import home_view, flinfo_view, binfo_view
from register.views import signup_view, activated_view
from account.views import account_view

urlpatterns = [
    path('', home_view, name='home'),
	path('freelancer/', flinfo_view, name='flinfo'),
	path('business/', binfo_view, name='binfo'),
	path('signup/<int:is_business>/', signup_view, name='signup'),
    re_path(r'^activate/(?P<uidb64>[-+@\w]+)/(?P<token>[-+@\w]+)/', activated_view, name='activate'),
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('account/', account_view, name='account'),
]
