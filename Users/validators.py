from django.forms import ValidationError
from itertools import cycle
#validadoders --->funcion
#             --->clases

class MaxSizeImgValidator:
    def __init__(self,max_file_size=5):
        self.max_file_size=max_file_size
    #validador:obtienen lo que el usuario inyecta al form
    def __call__(self, value):
        size=value.size
        max_size=self.max_file_size*1048576

        if size > max_size:
            raise ValidationError(f'El tamaño maximo del archivo debe ser {self.max_file_size}MB')
        return value
        
