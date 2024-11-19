from django import forms
from django.forms import ModelForm
from .models import Task
#class CreteNewTask(forms.Form):
#    title = forms.CharField(label="Titulo de la Descripcion", max_length=200)
#   description = forms.CharField(label="Descripcion de la Tarea",widget=forms.Textarea)

class taskform(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','important', 'project']
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'important':forms.CheckboxInput(attrs={'class':'form-check-input'})  
        }



class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Projecto")
    