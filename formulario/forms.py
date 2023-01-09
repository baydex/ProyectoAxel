from .models import Persona
from django import forms


class PersonaForm(forms.ModelForm):
    sexo = forms.ChoiceField(choices=[
            (0, 'Hombre'), 
            (1, 'Mujer'), 
            (2, 'Otro')
            ], 
            widget=forms.RadioSelect, label="¿Cual es tu sexo?")
    nivel_educativo = forms.ChoiceField(choices=[   (0, 'Primaria'), 
                                                    (1, 'Secundaria'), 
                                                    (2, 'Preparatoria'), 
                                                    (3, 'Licenciatura / Ingeniería'),
                                                    (4, 'Maestría / Doctorado'), 
                                                    ], 
                                                    widget=forms.RadioSelect, label="¿Cual es tu nivel educativo?")
    ocupacion = forms.ChoiceField(choices=[         (0, 'Estudiante'), 
                                                    (1, 'Trabajador'), 
                                                    (2, 'Ambas'), 
                                                    (3, 'Ninguna'),
                                                    ], 
                                                    widget=forms.RadioSelect, label="¿Cual es tu ocupación?")
    introvertido_extrovertido = forms.IntegerField(label="Si 1 es introvertido y 10 extrovertido. ¿En donde te encuentras?", widget=forms.NumberInput(attrs={'type':'range', 'step': 1, 'min': 1, 'max': '10'}))
    calmado_nervioso = forms.IntegerField(label="Si 1 es ser calmado y 10 es ser nervioso. ¿En donde te encuentras?", widget=forms.NumberInput(attrs={'type':'range', 'step': 1, 'min': 1, 'max': '10'}))
    mas_importancia = forms.ChoiceField(label="¿A qué le das mas importancia?", choices=[   
                                                    (0, 'Familia'), 
                                                    (1, 'Trabajo'), 
                                                    (2, 'Amigos'), 
                                                    (3, 'Tu mismo'),
                                                    (4, 'Escuela'), 
                                                    ], 
                                                    widget=forms.RadioSelect)
    deporte = forms.ChoiceField(label="¿Cómo te consideras en el deporte?", choices=[           
                                                    (0, 'No haces nada'), 
                                                    (1, 'Poco'), 
                                                    (2, 'Moderado'), 
                                                    (3, 'Mucho'),
                                                    (4, 'Profesional'), 
                                                    ], 
                                                    widget=forms.RadioSelect)
    viajar = forms.IntegerField(label="¿Cuánto interes tienes en viajar?", widget=forms.NumberInput(attrs={'type':'range', 'step': 1, 'min': 1, 'max': 4}))
    videojuegos = forms.IntegerField(label="¿Qué tanto te gustan los videojuegos?", widget=forms.NumberInput(attrs={'type':'range', 'step': 1, 'min': 1, 'max': 4}))
    leer = forms.IntegerField(label="¿Cuánto interes tienes en leer?", widget=forms.NumberInput(attrs={'type':'range', 'step': 1, 'min': 1, 'max': 4}))
    cine = forms.IntegerField(label="¿Cuánto interes tienes en cine?", widget=forms.NumberInput(attrs={'type':'range', 'step': 1, 'min': 1, 'max': 4}))
    amistad = forms.IntegerField(label="¿Qué tan importante es la amistad para ti?", widget=forms.NumberInput(attrs={'type':'range', 'step': 1, 'min': 1, 'max': 4}))
    mascotas = forms.IntegerField(label="¿Cuánto te gustan las mascotas?", widget=forms.NumberInput(attrs={'type':'range', 'step': 1, 'min': 1, 'max': 4}))
    apariencia = forms.IntegerField(label="¿Cuánto cuidas tu apariencia personal?", widget=forms.NumberInput(attrs={'type':'range', 'step': 1, 'min': 1, 'max': 4}))
    salud = forms.IntegerField(label="¿Cuánto cuidas tu salud?", widget=forms.NumberInput(attrs={'type':'range', 'step': 1, 'min': 1, 'max': 4}))
    experimentar = forms.IntegerField(label="¿Cuánto te gusta experimentar cosas nuevas?", widget=forms.NumberInput(attrs={'type':'range', 'step': 1, 'min': 1, 'max': 4}))
    hijos = forms.ChoiceField(label="¿Quiéres tener hijos?", choices=[           
                                                    (0, 'Sí'), 
                                                    (1, 'No'), 
                                                    (2, 'No lo sé'), 
                                                    ], 
                                                    widget=forms.RadioSelect)
    musica = forms.ChoiceField(choices=[
                (0, 'Bad Bunny'), 
                (1, 'Taylor Swift'), 
                (2, 'Drake'), 
                (3, 'The Weeknd'), 
                (4, 'BTS'),
                (5, 'Ed Sheeran'),
                (6, 'Harry Styles'),
                (7, 'Justin Bieber'),
                (8, 'Kanye West'),
                (9, 'Eminem'),
                ], widget=forms.RadioSelect, label="Selecciona 2 artistas")
    sueño = forms.ChoiceField(label="¿Cómo son tus habitos de sueño?", choices=[             
                                                    (0, 'Dormir temprano'), 
                                                    (1, 'Dormir tarde'), 
                                                    (2, 'Irregular'), 
                                                    (3, 'Siestas de día y dormir de noche'),
                                                    ], 
                                                    widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['edad'].label = '¿Cuántos años tienes?'


    class Meta:
        model = Persona
        exclude = ['id', "user"]