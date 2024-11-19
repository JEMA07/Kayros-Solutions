from django.urls import path
from . import views 
#la urls son sistem interno de cada app para recorred los datos que envia 
# el servidor de la app 

urlpatterns = [
   #url de login
   
   path('', views.vista, name="home"),
   path('Singup/', views.Singup, name="singup"),#registrar
   path('logaut/', views.cerrar_secion, name="logaut"),#cerrar cession
   path('signin/', views.signin, name="signin"),#logiarse
   
   #url de paginas
   #seccion de url projecto
   path('about/', views.about, name="about"),
   path('project/', views.projec, name="project"),
   path('project/<int:id>', views.project_detail, name="project_detail"),
   path('create_project/', views.create_project, name="create_project"),
   
   #seccion url tarea
   path('task/', views.Tasks, name="task"),
   path('task_completed/', views.Tasks_completed, name="task_completed"),
   path('task/create_task/', views.create_task, name="create_task"),
   path('task/<int:id>', views.task_detail, name="task_detail"),#este me esta dando ca aos
   path('task/<int:id>/complete', views.task_complet, name="task_complet"),#complet
   path('task/<int:id>/', views.task_delete, name="delete"),#eliminar
   
]
