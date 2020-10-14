from django.db import models
from django.contrib.auth.models import User

import uuid 


class Categoria(models.Model):
    descripcion = models.CharField(max_length=60,
                                    help_text='Descripcion de la Categoria')
    autor = models.ForeignKey(User,
                                on_delete=models.PROTECT,
                                help_text='Seleccione el autor de la categoria')
    
    def __str__(self):
        return self.descripcion


class Publicacion(models.Model):
    id = models.UUIDField(primary_key= True, editable=False, default=uuid.uuid4)
    titulo = models.CharField(max_length=200,
                                help_text='Escriba el titulo de la publicacion')
    contenido = models.TextField(max_length=20000,
                                 help_text='Escriba el contenido de la publicacion')
    autor = models.ForeignKey(User,
                                on_delete=models.PROTECT,
                                help_text='Seleccione el autor de la categoria')
    f_pub = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Publicacion')
    categorias = models.ManyToManyField(Categoria,
                                        help_text='Seleccione las categorias')
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Publicacion'  
        verbose_name_plural = 'Publicaciones'
        ordering = ['-f_pub'] 

