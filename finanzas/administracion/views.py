from .permissions import administradorPost
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework import response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import *


class CategoriaController(generics.ListCreateAPIView):
    queryset = CategoriaModel.objects.all()
    serializer_class=CategoriaSerializer
      

    def get(self, request):
        respuesta=self.serializer_class(
            instance=self.get_queryset(), many=True)
        return Response({
            'success':True,
            'content':respuesta.data,
            'message':None
          })
    def post(self, request):
        nuevaCategoria=self.serializer_class(data=request.data)
        if nuevaCategoria.is_valid():
            nuevaCategoria.save()
            return Response({
             'success':True,
             'content':nuevaCategoria.data,
             'message':'Usuario creado exitosamente'
           }, status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'content': nuevaCategoria.errors,
                'message': 'Error al crear el nuevo Usuario'
            }, status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        categoria= self.get_queryset(id)
        categoria.delete()
        return Response({
            'success':True,
            'content':None,
            'message':'se elimino correctamente'
        })        

class RegistrarUsuarioController(generics.CreateAPIView):
    serializer_class = RegistroUsuarioSerializer

    def post(self, request):
        nuevoUsuario = self.serializer_class(data=request.data)
        if nuevoUsuario.is_valid():
            nuevoUsuario.save()
            return Response({
                'success': True,
                'content': nuevoUsuario.data,
                'message': 'Usuario creado exitosamente'
            }, status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'content': nuevoUsuario.errors,
                'message': 'Error al crear el nuevo Usuario'
            }, status.HTTP_400_BAD_REQUEST)

class RegistrarGastoController(generics.CreateAPIView):
    queryset = GastosModel.objects.all()
    serializer_class=GastosEscrituraSerializer
    permission_classes=[IsAuthenticated]  
    permission_classes=[IsAuthenticatedOrReadOnly,administradorPost]
    def get(self, request):
        respuesta=self.serializer_class(
            instance=self.get_queryset(), many=True)
        return Response({
            'success':True,
            'content':respuesta.data,
            'message':None
          })
    def post(self, request):
        nuevaGasto=self.serializer_class(data=request.data)
        if nuevaGasto.is_valid():
            nuevaGasto.save()
            return Response({
             'success':True,
             'content':nuevaGasto.data,
             'message':'Gasto creado exitosamente'
           }, status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'content': nuevaGasto.errors,
                'message': 'Error al crear el nuevo Gasto'
            }, status.HTTP_400_BAD_REQUEST)

