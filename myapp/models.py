from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=100)

    #metodo para cambiar el metodo de lectura 
    #desde el admin no salgo object si no el nombre real
    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)#cada projecto le correponde una tarea
    datecomplet = models.DateTimeField(null=True,blank=True)
    important = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    #saber que tarea le corresponde a cada usuario
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return f"{self.title} - {self.project.name} - by {self.user.username}"
        #return self.title +'-'+ self.project.name + '- by'+ self.user.username

