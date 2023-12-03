from django import forms
from miApp.models import Rifas
class FormVenta(forms.Form):
    id_rifa=  forms.CharField(widget=forms.HiddenInput)
    nombre= forms.CharField()
    email= forms.CharField(required= False)
    telefono= forms.IntegerField()
    numero_compra= forms.IntegerField(min_value=1)
    codigo= forms.CharField()


    id_rifa.widget.attrs['class']='form-control'
    nombre.widget.attrs['class']='form-control'
    email.widget.attrs['class']='form-control'
    telefono.widget.attrs['class']='form-control'
    numero_compra.widget.attrs['class']='form-control'
    codigo.widget.attrs['class']='form-control'

    def clean_numero_compra(self):
        id_rifa = self.cleaned_data['id_rifa']
        numero_compra = self.cleaned_data['numero_compra']

        rifas = Rifas.objects.get(id=id_rifa)
        numeros_disponibles = rifas.numeros_disponibles

        if (numero_compra > numeros_disponibles) :
            raise forms.ValidationError("No hay numeros disponibles ")
        
        return  numero_compra

    
