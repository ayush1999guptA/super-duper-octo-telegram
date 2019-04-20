from django.contrib import admin
from .models import Year,Student,Events,Notification,BlogsWithoutMedia,BlogsWithMedia
admin.site.register(Student)
admin.site.register(Notification)
admin.site.register(Events)
admin.site.register(Year)
admin.site.register(BlogsWithoutMedia)
admin.site.register(BlogsWithMedia)