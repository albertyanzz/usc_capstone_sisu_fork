"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.conf.urls import handler400, handler403, handler500
from django.urls import path
from mysite.sitemaps import StaticViewSitemap

sitemaps = {
    'sitemap': StaticViewSitemap
}

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'', include("blog.urls")),
    re_path('', include('pages.urls')),
    re_path('users/', include('users.urls')), # new
    re_path('users/', include('django.contrib.auth.urls')), # new
    re_path('accounts/', include('allauth.urls')), 
    re_path('', include('enpApi.urls')),  
    re_path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]


# Page Error Handling
# handler400 = 'main.views.handle400'
# handler403 = 'main.views.handle403'
# handler404 = 'main.views.handle404'
# handler500 = 'main.views.handle500'