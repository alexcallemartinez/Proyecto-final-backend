from .models import *
from rest_framework import serializers


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoriaModel
        fields = '__all__'



class RegistroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def save(self):
        usuarioCorreo = self.validated_data.get('usuarioCorreo')
        usuarioTipo = self.validated_data.get('usuarioTipo')
        usuarioNombre = self.validated_data.get('usuarioNombre')
        usuarioApellido = self.validated_data.get('usuarioApellido')
        password = self.validated_data.get('password')
        usuarioSueldo = self.validated_data.get('usuarioSueldo')
        is_staff = False
        nuevoUsuario = UsuarioModel(
            usuarioCorreo=usuarioCorreo,
            usuarioTipo=usuarioTipo,
            usuarioNombre=usuarioNombre,
            usuarioApellido=usuarioApellido,
            usuarioSueldo=usuarioSueldo,
            is_staff=is_staff
        )
        # encriptamos la contraseña
        nuevoUsuario.set_password(password)
        nuevoUsuario.save()
        return nuevoUsuario

    class Meta:
        model = UsuarioModel
        # excluimos grupos porque no va a tener acceso al panel administrativo al igual que user_permissions (ambos sirven para indicar que puede hacer en el panel administrativo)
        exclude = ['groups', 'user_permissions'] 

class GastosEscrituraSerializer(serializers.ModelSerializer):
    class Meta:
        model = GastosModel
        fields = '__all__'
