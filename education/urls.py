"""education URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from masterdata import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^home/$',views.index,name='index'),
    # url(r'^sd_creation/$',views.sd_creation,name='index'),
    # url(r'^md_creation/$',views.md_creation,name='index'),
    url(r'^listdonor/$',views.listdonor,name='index'),
    url(r'^adddonor/$',views.adddonor,name='index'),
    url(r'^deletedonor/(?P<pk>.*)/$',views.deletedonor,name='index'),
    url(r'^list_sd_creation/$',views.list_sd_creation,name='index'),
    url(r'^add_sd_creation/$',views.add_sd_creation,name='index'),
    url(r'^delete_sd_creation/(?P<pk>.*)/$',views.delete_sd_creation,name='index'),
    url(r'^list_md_creation/$',views.list_md_creation,name='index'),
    url(r'^add_md_creation/$',views.add_md_creation,name='index'),
    url(r'^delete_md_creation/(?P<pk>.*)/$',views.delete_md_creation,name='index'),
    url(r'^editdonor/(?P<pk>.*)/$',views.editdonor,name='index'),
    url(r'^edit_sd_creation/(?P<pk>.*)/$',views.edit_sd_creation,name='index'),
    url(r'^edit_md_creation/(?P<pk>.*)/$',views.edit_md_creation,name='index'),
    url(r'^edit_profile/(?P<pk>.*)/$',views.edit_profile,name='index'),
    url(r'^delete_profile/(?P<pk>.*)/$',views.delete_profile,name='index'),
    url(r'^add_profile/$',views.add_profile,name='index')


    

   
   



]
