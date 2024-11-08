from django.shortcuts import render
from django.http import HttpResponse
from .models import*

# Create your views here.
def about(request):
    return HttpResponse("I am Gopika Mohandas, \nAge is 22")
def self1(request):
    return render(request,'self.html')

def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html',context={'name':'Arjun','age':22})

from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
     return render (request,'home.html')

def services(request):
     return render(request,'service.html')

def basicdtl(request):
        var1={}
        var1['name']='Manu'
        var1['age']='22'
        var1['place']='Ernakulam'
        var1['products']=['Book','2435','Pen']
        var1['gender']= 1
        var1['phone']=3783493
        var1['1']='Female'
        var1['0']='Male'
        var1['car']={'name':'ABCD','model':'NEX1234','brand':'BMW','colour':'Black'}
        return render(request=request,template_name='basicdtl.html',context=var1)
def bootstrap(request):
     return render(request,'bootstrap.html')

def aboutnav(request):
     return render(request,'aboutnav.html')

def contactnav(request):
     return render(request,'contactnav.html')

# def booking(request):
#      return render(request,'booking.html')

def dept(request):
     dict1={
          'dep' : Department.objects.all()   # object.all() - keyword is used to get all datas from models of department model
     }
     return render(request,'dept.html',dict1)

def doc(request):
     dict_doc = {
         'docs': Doctors.objects.all()
     }
     return render(request,'doc.html',dict_doc)
     

# def create_todo(request):
#      if request.method == 'GET':
#           return render(request,'booking.html')
#      elif request.method == 'POST':
#           title1=request.POST['title'] #get method is not used here since it is a mandatory field and it is accessed from 'name' of form as dict using []
#           description1=request.POST.get('des',None) #crud - get, if user enter no values 'None' will be taken, des - obtained from 'name' field of html page
#           rating=request.POST.get('rating',None)
#           status=request.POST.get('status', 'off')
#           if status == 'on':
#                status =True
#           else:
#                status = False
#           todo = Todo(title=title1, desription=description1, rating=rating, status=status) #title -> model field, title1 -> variable created in views
#           return HttpResponse('<h1>Completed</h1>')

def hos_contact(request):
     if request.method == 'GET':
          return render (request, 'contactnav.html')
     elif request.method == 'POST':
          Cont_name=request.POST['Name']
          Cont_num=request.POST['Phone']
          cont=Contact(Name=Cont_name, Phone_Number=Cont_num)
          cont.save()
          return HttpResponse('<h1>Completed</h1>')
     

from .forms import BookingForm


def hos_booking(request):
     if request.method == "POST":
          form =BookingForm(request.POST)
          if form.is_valid():      # is_valid() -> function, check validity of form. eg: Only numbers are entered inside CharField of model 
               form.save()
     form = BookingForm()
     dict_form = {
          'form':form    # 'form' -> variable that pass to html page, form -. FORM ON 86th line
     }
     return render(request,'booking1.html',dict_form)
from django.views.generic import ListView
class DeptListView(ListView):
     model = Department
     template_name = 'department.html'
     context_object_name = 'dept'

from django.views.generic.detail import DetailView
class DeptDetailed(DetailView):
     model=Department
     template_name='depDetail.html'
     context_object_name='dept'


from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
class TaskUpdateView(UpdateView):
     model=Department
     template_name='updatedept.html'
     fields=('dep_name','dep_description')

     def get_success_url(self):
          return reverse_lazy('depdetail', kwargs = {'pk':self.object.id})

     # success_url=reverse_lazy('dept')

from django.views.generic.edit import DeleteView
class TaskViewDelete(DeleteView):
     model = Department
     template_name = 'deptDelete.html'
     success_url = reverse_lazy('dept')



from django.views.generic.edit import CreateView
class TaslViewCreate(CreateView):
     model=Department
     template_name='deptCreate.html'
     fields='__all__'
     success_url=reverse_lazy('dept')

from django.urls import reverse
from .forms import*
from django.shortcuts import render, redirect
def register_user(request):
     if request.user.is_authenticated:
          return redirect('home')
     
     
     form = CustomUserCreationForm()
     if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               print("Registered Successfully")
               return redirect(reverse('login'))
     return render(request, 'register.html', {'form': form})
     
