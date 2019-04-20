from django.shortcuts import render
from .models import Student,Notification,Events,BlogsWithMedia,BlogsWithoutMedia
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
def IndexView(request):
    not1=Notification.objects.filter(year='1')
    not2=Notification.objects.filter(year='2')
    not3=Notification.objects.filter(year='3')
    not4=Notification.objects.filter(year='4')
    return render(request,'web/index.html',{'not1':not1,'not2':not2,'not3':not3,'not4':not4})

def Basic(request):
    return render(request,'web/basic.html')
# =====================Student========================
class DetailStudent(generic.DetailView):
    model=Student
    template='web/student_detail.html'

class CreateStudent(CreateView):
    model=Student
    fields=['name','rollnumber','branch','photo','discription','year']

class UpdateStudent(UpdateView):
    model = Student
    fields = ['name', 'rollnumber', 'branch', 'photo', 'discription', 'year']

class DeleteStudent(DeleteView):
    model=Student
    success_url=reverse_lazy('start')
# =====================Student========================
#   =====================Notification====================
class PushNotification(CreateView):
    model=Notification
    fields=['message','writeup','year']


class ViewNotification(generic.DetailView):
    model=Notification
    template='web/detailnotification.html'

class SeeNotification(generic.ListView):
    template='web/notification_list.html'
    context_object_name='all_notification'
    def get_queryset(self):
        return Notification.objects.all()

class PopNotifictaion(DeleteView):
    model=Notification
    success_url=reverse_lazy('index')
#   =====================Notification====================
# =========================Events=========================
class AllEvents(generic.ListView):

    template='web/events_list.html'
    context_object_name='all_events'

    def get_queryset(self):
        return Events.objects.all()

class DetailEvent(generic.DetailView):
    model=Events
    template="web/events_detail.html"

class CreateEvent(CreateView):
     model=Events
     fields=['type','date','time','venue','discription','poster','name']

class UpdateEvent(UpdateView):
    model = Events
    fields = ['type', 'date', 'time', 'venue', 'discription','poster','name']

class DeleteEvent(DeleteView):
    model = Events
    success_url=reverse_lazy('event-list')

    success_url=reverse_lazy('events')
# =========================Events=========================
def login(request):
    if request.method == 'POST':
        login_data = request.POST.dict()
        username = login_data.get("username")
        password = login_data.get("password")
        if (username=="admin" and password=="password123"):
          return  render(request,'web/adminindex.html')
        else:
           return render(request,'web/login.html')
    else:
       return render(request,'web/login.html')
def contact(request):
    return render(request,'web/team.html')
    # =========================================blogs========
class CreateBlogW(CreateView):
    model=BlogsWithoutMedia
    fields=['bloggername','blogsubject','blog']
class CreateBlog(CreateView):
    model=BlogsWithMedia
    fields=['bloggername','blogsubject','blog','blogmedia']

class BlogW(generic.ListView):

    template='web/events_list.html'
    context_object_name='all_blogw'

    def get_queryset(self):
        return BlogsWithoutMedia.objects.all()

class Blog(generic.ListView):

    template='web/events_list.html'
    context_object_name='all_blog'

    def get_queryset(self):
        return BlogsWithMedia.objects.all()

def flex(request):
        return render(request,'web/blogswitch.html')


def resource(request):
        return render(request,'web/resource.html')