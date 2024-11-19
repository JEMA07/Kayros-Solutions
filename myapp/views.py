from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Projects, Task
from django.shortcuts import get_object_or_404
from .forms import taskform, CreateNewProject
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required

  
#creacin de Usuarios
def Singup(request):
   if request.method == 'GET':
       return render(request, 'login/Singup.html', {
      'form': UserCreationForm
   })
    
   else:
      if request.POST['password1'] == request.POST['password2']:
         try:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('signin')
           #guardar los datos cuando cumpla los 
         except:
            return render(request, 'login/Singup.html', {
      'form': UserCreationForm,
      'error': 'usurio ya exites'
   })
      
      return  render(request, 'login/Singup.html', {
      'form': UserCreationForm,
      'error': 'password do not match'
   })
  
         
       
     
   
  
 

    
         
       

#esta estructura del projectos y tareas



# Create your views here.
def vista(request):
   #vis = Projects.objects.all()
   title = 'Curso de Djang!!'
   return render(request, 'home.html', {
      'title': title
   })
   #return render(request, 'home.html')

def about(request):
   return render(request, 'projects/about.html')

def projec(request):
   #RECORRERMOS LOS OBJETO DE LA CLASE MODEL PROJECTS
   query = request.GET.get('query')
   if query:
      project = Projects.objects.filter(name__icontains=query)
   else:
      project = Projects.objects.none()
   
   
   return render(request, 'projects/projects.html', {
      'project':project,
      'error':'no se encontro resulatdao'
   })

@login_required
def Tasks(request):
  # task = get_object_or_404(Task, id=id)
   task = Task.objects.filter(user=request.user, datecomplet__isnull=True)
   return render(request, 'projects/task.html', {
      'task':task
   })
   #mostrar tareas completadas
@login_required
def Tasks_completed(request):
  # task = get_object_or_404(Task, id=id)
   task = Task.objects.filter(user=request.user, datecomplet__isnull=False).order_by(
      '-datecomplet'
   )
   return render(request, 'projects/task.html', {
      'task':task
   })
   
#funciones de competado eliminar update
@login_required
def task_complet(request, id):
   task =get_object_or_404(Task, pk=id)
   if request.method == 'POST':
      task.datecomplet = timezone.now()
      task.save()
      return redirect('task')
#funcion delete
@login_required
def task_delete(request, id):
   task =get_object_or_404(Task, pk=id)
   if request.method == 'POST':
      task.delete()
      return redirect('task')
  
@login_required   
def create_task(request):
   if request.method == 'GET':
      return render(request, 'projects/create_task.html',{
            'form': taskform()   
            })
   else:
      try:
         form= taskform(request.POST)
         new_task = form.save(commit=False)
         new_task.user = request.user
         new_task.save()
         return redirect('task')
      except ValueError:
         return render(request, 'projects/create_task.html',{
            'form': taskform(),
            'error': 'please provide valida data '   
            })
         
      
      #SHOW INTERFACE
   
   
@login_required   
def task_detail(request, id):
   if request.method == 'GET':
      task = get_object_or_404(Task, pk=id)
      form=taskform(instance=task)
      return render(request, 'projects/task_detail.html',{'task':task, 'form':form})
   else:
      try:
         task =get_object_or_404(Task, pk=id)
         form=taskform(request.POST, instance=task)
         form.save()
         return redirect('task')
      except ValueError:
         return render(request, 'projects/task_detail.html',{'task':task, 'form':form})

         
@login_required
def create_project(request):
   if request.method == 'GET':
      return render(request, 'projects/create_project.html', {
         'form': CreateNewProject()
      })
   else:
      Projects.objects.create(name=request.POST['name'])
      return redirect('project')
#funciones que permirte recorrer por id los projectos y las tareas que le corresponde a es projecto
#filter que es y para que sirve
@login_required
def project_detail(request, id):
   pro = get_object_or_404(Projects, id=id)
   tasks1 = Task.objects.filter(project_id=id)
   return render(request, 'projects/detail.html',{
      #estos son diccionarios
      'project': pro,
      'task':tasks1
   })
      
@login_required 
 #cerrar secion
def cerrar_secion(request):
    logout(request)
    return redirect('home')
 
 #singin
def signin(request):
   if request.method == 'GET':
      return render(request, 'singin/singin.html',{
      'form':AuthenticationForm
   })
   else:
      use =authenticate(request, username=request.POST['username'], password=request.POST['password'])
      print(request.POST)
      #validar si no esta vacio el usuario
      if use is None:
            return render(request, 'singin/singin.html',{
           'form':AuthenticationForm,
           'error':'username or password is incorrect'
             })
      else:
         login(request, use)
         return redirect('task')
         
     