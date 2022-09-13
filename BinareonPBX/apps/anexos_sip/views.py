# Create your views here.
from rest_framework.decorators import api_view
from apps.anexos_sip.serializer import (
    AnexoRegistrarSerializer,
    AnexoListarSerializer,
    SipTelefonoSerializer,
    )
from rest_framework.response import Response
from apps.anexos_sip.models import sip_buddies
from apps.sip_telefono.models import sip_telefono
from rest_framework import status

#ejemplo
@api_view(['GET','POST'])
def telefono_api_view(request):
    if request.method == 'GET':
        telfono_sip = sip_telefono.objects.all()
        telfono_sip = SipTelefonoSerializer(telfono_sip,many=True)
        return Response(telfono_sip.data, status=status.HTTP_200_OK) 

#REGISTRO DE ANEXOS
@api_view(['GET','POST'])
def registro_api_view(request):
    if request.method == 'GET':
        anexo_registrar = sip_buddies.objects.all()
        anexo_serializer = AnexoRegistrarSerializer(anexo_registrar,many=True)
        return Response(anexo_serializer.data, status=status.HTTP_200_OK)   
    elif request.method == 'POST':
        anexo_serializer = AnexoRegistrarSerializer(data=request.data)
        if anexo_serializer.is_valid():
            anexo_serializer.save()            
            return Response({
                'isCreated':True,
                'message':'Registro creado satisfactoriamente',
                'data':anexo_serializer.data
            },status=status.HTTP_201_CREATED)
        return Response({
                'isCreated':False,
                'status': status.HTTP_400_BAD_REQUEST,
                'message':"Este registro ya existe",
                'data':anexo_serializer.errors
            })

#LISTADO DE ANEXOS
@api_view(['GET','POST'])
def anexo_api_view(request):
    if request.method == 'GET':
        anexo_listar = sip_buddies.objects.all()
        anexo_serializer = AnexoRegistrarSerializer(anexo_listar,many=True)
        return Response(anexo_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET','PUT','DELETE'])
def anexo_detail_view(request,pk=None):
    anexo = sip_buddies.objects.filter(name=pk).first()    
    if anexo:
        if request.method == 'GET':
            anexo_serializer = AnexoRegistrarSerializer(anexo)
            return Response(anexo_serializer.data,status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            anexo_serializer = AnexoRegistrarSerializer(anexo,data = request.data)
            if anexo_serializer.is_valid():
                anexo_serializer.save()
                return Response({
                    'isCreated': True,
                    'message': "El registro se ha actualizado de manera correcta",
                    'data':anexo_serializer.data
                    },status.HTTP_200_OK)
            return Response({
                'isCreated':False,
                'status': status.HTTP_400_BAD_REQUEST,
                'message':"Error al actualizar",
                'data':anexo_serializer.errors
            }) 

        elif request.method == 'DELETE':
            anexo.delete()
            return Response('Registro eliminado')           


@api_view(['DELETE'])
def anexo_eliminar_view(request,pk=None):
    anexo = sip_buddies.objects.filter(name=pk).first()  
    if request.method == 'DELETE':
        anexo.delete()
        return Response('Registro eliminado')  
    
