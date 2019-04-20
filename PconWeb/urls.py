"""PconWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/$',views.IndexView,name='index'),
    path('',views.Basic,name='start'),
    url(r'^student/add/$',views.CreateStudent.as_view(),name='add-s'),
    url(r'^student/(?P<pk>[0-9]+)/$',views.DetailStudent.as_view(),name='detail-s'),
    url(r'^student/(?P<pk>[0-9]+)/delete$',views.DeleteStudent.as_view(),name='delete-s'),
    url(r'^student/(?P<pk>[0-9]+)/update$',views.UpdateStudent.as_view(),name='update-s'),
    url(r'^notification/add$',views.PushNotification.as_view(),name='push'),
    url(r'^notification$', views.SeeNotification.as_view(), name='see'),
    url(r'^notification/(?P<pk>[0-9]+)/delete$',views.PopNotifictaion.as_view(),name='pop'),
    url(r'^notification/(?P<pk>[0-9]+)/$', views.ViewNotification.as_view(), name='see'),
    url(r'^events/add$',views.CreateEvent.as_view(),name='add-event'),
    url(r'^events/(?P<pk>[0-9]+)/delete$', views.DeleteEvent.as_view(), name='delete-event'),
    url(r'^events/(?P<pk>[0-9]+)/update$', views.UpdateEvent.as_view(), name='update-event'),
    url(r'^events/(?P<pk>[0-9]+)/$', views.DetailEvent.as_view(), name='event'),
    url(r'^login$',views.login,name='login'),
    url(r'^events/?P<pk>[0-9]+/delete$', views.DeleteEvent.as_view(), name='delete-event'),
    url(r'^events/?P<pk>[0-9]+/update$', views.UpdateEvent.as_view(), name='update-event'),
    url(r'^events/?P<pk>[0-9]+/$', views.DetailEvent.as_view(), name='event'),
    url(r'^events/$', views.AllEvents.as_view(), name='event-list'),
    url(r'^blogw/add/$',views.CreateBlogW.as_view(),name='abw'),
    url(r'^blog/add/$', views.CreateBlog.as_view(), name='ab'),
    url(r'^blogw/$',views.BlogW.as_view(),name='blw'),
    url(r'^blog/$', views.Blog.as_view(), name='bl'),
    url(r'^contact/$',views.contact,name='con'),
    url(r'^flex/$',views.flex,name='flex'),
    url(r'^reso/$', views.resource, name='reso'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
