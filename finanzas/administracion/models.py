from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import DecimalField
from .authmanager import UsuarioManager


class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    """Modelo de la base de datos del usuario del sistema"""
    TIPO_USUARIO = [
        (1, 'ADMINISTRADOR'),
        (2, 'USUARIO'),
        
    ]

    usuarioId = models.AutoField(
        primary_key=True,
        unique=True,
        db_column='usuario_id'
    )
    usuarioCorreo = models.EmailField(
        db_column='usuario_correo',
        max_length=30,
        verbose_name='Correo del usuario',
        unique=True
    )
    usuarioTipo = models.IntegerField(
        db_column='usuario_tipo',
        choices=TIPO_USUARIO,
        verbose_name='Tipo del usuario'
    )
    usuarioNombre = models.CharField(
        max_length=45,
        null=False,
        db_column='usuario_nombre',
        verbose_name='Nombre del usuario'
    )
    usuarioApellido = models.CharField(
        max_length=45,
        null=False,
        db_column='usuario_apellido',
        verbose_name='Apellido del usuario'
    )
    password = models.TextField(
        db_column='usuario_contrasena',
        verbose_name='Contraseña del usuario'
    )
    usuarioSueldo=models.DecimalField(
        max_digits=5,
        decimal_places=2,
        db_column='usuario_sueldo',
        null=False
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'usuarioCorreo'
   
    REQUIRED_FIELDS = ['usuarioNombre', 'usuarioTipo', 'usuarioApellido']

    class Meta:
        db_table = 't_usuario'
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

class CategoriaModel(models.Model):
    categoriaId = models.AutoField(
        primary_key=True,
        db_column="categoria_id",
        null=False
    )
    categoriaNombre = models.CharField(
        db_column='categoria_nombre',
        max_length=40,
        null=False,
        verbose_name='Nombre de categoria'
    )
    def __str__(self):
       return self.categoriaNombre
    
    class Meta:
        db_table = 't_categoria'
        verbose_name = 'Categoria'


class GastosModel(models.Model):

    TIPO_PAGO=[
        (1,'EFECTIVO'),
        (2,'TARJETA')
    ]


    gastosId=models.AutoField(
        primary_key=True,
        unique=True,
        db_column='gastos_id'
    )
    gastosFecha=models. DateField(
        db_column='gastos_fecha',
        null=False
    )
    gastosNombreProducto=models.CharField(
        max_length=45,
        null=False,
        db_column='gastos_nombre',
        verbose_name='Nombre del producto'
    ) 
    gastosTipoPago=models.IntegerField(
        db_column='gastos_tipopago',
        choices=TIPO_PAGO,
        verbose_name='Tipo de pago'

    )    
    gastosPrecio=models.DecimalField(
        db_column='gastos_precio',
        max_digits=5,
        decimal_places=2,
        null=False,
        verbose_name='Precio del gasto'
    )
    usuario=models.ForeignKey(
        to=UsuarioModel,
        on_delete=models.PROTECT,
        db_column='usuario_id',
        related_name='usuarioGastos',
        null=False
    )

    categoria=models.ForeignKey(
        to=CategoriaModel,
        on_delete=models.PROTECT,
        db_column='categoria_id',
        related_name='categoriaGastos',
        null=False
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    class Meta:
        db_table = 't_gastos'
        verbose_name = 'Gastos'
