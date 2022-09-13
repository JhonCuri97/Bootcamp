
from rest_framework import serializers
from apps.anexos_sip.models import sip_buddies
from apps.sip_telefono.models import sip_telefono

class SipTelefonoSerializer(serializers.ModelSerializer):
    id_marca_telefono = serializers.CharField(source ='id_marca_telefono.no_marca_telefono')
    id_modelo_telefono = serializers.CharField(source ='id_modelo_telefono.no_modelo_telefono')
    #grabacion = serializers.CharField(source ='buddies.grabacion')

    class Meta:
        model = sip_telefono
        fields = ('id_marca_telefono','id_modelo_telefono','no_mac')

class AnexoRegistrarSerializer(serializers.ModelSerializer):
    telefono = SipTelefonoSerializer()
    class Meta:
        model = sip_buddies
        fields = (
            #BASICO
            'name',
            'accountcode',
            'secret',
            'callerid',
            
            'telefono'
            
        )
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.accountcode = validated_data.get('accountcode',instance.accountcode)
        instance.secret = validated_data.get('secret',instance.secret)
        instance.callerid = validated_data.get('callerid',instance.callerid)
        instance.save()

        telefono_data = validated_data.pop('telefono')
        if telefono_data:
            for tel_data in telefono_data:
                tel_data_id = sip_telefono.objects.get('id_sip_telefono')
                if tel_data_id:
                    update_order_detail = sip_telefono.objects.get(id=tel_data_id)
                    update_order_detail.no_mac = tel_data.get('no_mac',update_order_detail.no_mac)
                    update_order_detail.save()  
                else:
                    sip_telefono.objects.create(**tel_data, telefono=instance)              
        else:
            pass
        return instance
    
        
    """   
    def get_tel_query(self,obj):
        tel_query = models.sip_telefono.objects.filter(buddies=obj.id)
        serializer = SipTelefonoSerializer(tel_query, many=True)
        return serializer.data
    """
#Listar anexos
class AnexoListarSerializer(serializers.ModelSerializer):
    telefono = SipTelefonoSerializer( )
    class Meta:
        model = sip_buddies
        fields = ('id_sip','name', 'callerid', 'context','telefono')


"""
    id_marca_telefono = serializers.CharField(source ='id_marca_telefono.no_marca_telefono')
    id_modelo_telefono = serializers.CharField(source ='id_modelo_telefono.no_modelo_telefono')
    
    class Meta:
        model = sip_telefono
        fields = ('id_marca_telefono','id_modelo_telefono','no_mac')

"""
"""
            'mailbox',            
            'context',
            #AVANZADO
            'grabacion',
            'callgroup',
            'pickupgroup',
            'allow',
            'tls_srtp',
            'openvpn',
            #APROVISIONAMIENTO
            'num_vlan',
            """