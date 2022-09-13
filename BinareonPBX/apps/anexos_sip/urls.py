from django.urls import path
from apps.anexos_sip.views import (
    registro_api_view,
    anexo_api_view, 
    anexo_detail_view,
    anexo_eliminar_view,
    telefono_api_view,

    )

urlpatterns = [
    #REGISTRO DE ANEXOS
    path('registro/', registro_api_view, name='Registro'),
    #LISTADO DE ANEXOS
    path('lista/', anexo_api_view, name='Listar'),
    path('lista/<int:pk>/', anexo_detail_view, name='Detalle'),
    path('eliminar/<int:pk>/', anexo_eliminar_view, name = 'Eliminar'),
    path('telefono', telefono_api_view, name = 'telefono'),


]