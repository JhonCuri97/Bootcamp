from rest_framework import serializers
from apps.anexos_sip.models import sip_buddies
from apps.sip_telefono.models import sip_telefono

class SipTelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = sip_telefono
        fields = ('id_marca_telefono','id_modelo_telefono','no_mac')
    
    def create(self,validated_data):
        telefono = sip_telefono.objects.create(**validated_data)
        return telefono
    
    def update(self,instance,validated_data):
        instance.id_marca_telefono = validated_data.get('id_marca_telefono',instance.id_marca_telefono)
        instance.id_modelo_telefono = validated_data.get('id_modelo_telefono',instance.id_modelo_telefono)
        instance.no_mac = validated_data.get('no_mac',instance.no_mac)
        instance.save()
        return instance

class AnexoRegistrarSerializer(serializers.ModelSerializer):
    telefono = SipTelefonoSerializer(required=False)
    class Meta:
        model = sip_buddies
        fields = (
            #BASICO
            'name','accountcode','secret','callerid','mailbox','context',
            #AVANZADO
            'grabacion','callgroup','pickupgroup','allow','tls_srtp','openvpn',
            #APROVISIONAMIENTO
            'num_vlan','telefono'            
        )

    def create(self,validated_data):
        nuevo_sip = sip_buddies.objects.create(**validated_data)
        return nuevo_sip    
    
    def update(self,instance,validated_data):
        
        instance.name = validated_data.get('name',instance.name)
        instance.accountcode = validated_data.get('accountcode',instance.accountcode)
        instance.secret = validated_data.get('secret',instance.secret)
        instance.callerid = validated_data.get('callerid',instance.callerid)
        instance.mailbox = validated_data.get('mailbox',instance.mailbox)
        instance.context = validated_data.get('context',instance.context)
        instance.grabacion = validated_data.get('grabacion',instance.grabacion)
        instance.callgroup = validated_data.get('callgroup',instance.callgroup)
        instance.pickupgroup = validated_data.get('pickupgroup',instance.pickupgroup)
        instance.allow = validated_data.get('allow',instance.allow)
        instance.tls_srtp = validated_data.get('tls_srtp',instance.tls_srtp)
        instance.openvpn = validated_data.get('openvpn',instance.openvpn)
        instance.num_vlan = validated_data.get('num_vlan',instance.num_vlan)
        instance.save()

        telefono_data = validated_data.pop('telefono')        
        tel = instance.telefono
        tel.id_marca_telefono = telefono_data.get('id_marca_telefono',tel.id_marca_telefono)
        tel.id_modelo_telefono = telefono_data.get('id_modelo_telefono',tel.id_modelo_telefono)
        tel.no_mac = telefono_data.get('no_mac',tel.no_mac)
        tel.save()
        return instance 
    
#Listar anexos
class AnexoListarSerializer(serializers.ModelSerializer):
    telefono = SipTelefonoSerializer(required=False)

    class Meta:
        model = sip_buddies
        fields = ('name', 'callerid', 'context','telefono')

    def create(self,validated_data): 
        telefono_data = validated_data.pop('telefono', None)         
        sip = sip_buddies.objects.create(**validated_data)
        sip.save()

        for tel in telefono_data:
            sip_telefono.objects.create(
                telefono=validated_data[id_marca_telefono]
            )
        return sip
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.callerid = validated_data.get('callerid',instance.callerid)
        instance.context = validated_data.get('context',instance.context)
        instance.save()
        
        telefono_data = validated_data.pop('telefono')        
        tel = instance.telefono
        tel.id_marca_telefono = telefono_data.get('id_marca_telefono',tel.id_marca_telefono)
        tel.id_modelo_telefono = telefono_data.get('id_modelo_telefono',tel.id_modelo_telefono)
        tel.no_mac = telefono_data.get('no_mac',tel.no_mac)
        tel.save()
        return instance 



#id_marca_telefono = serializers.CharField(source ='id_marca_telefono.no_marca_telefono')
#id_modelo_telefono = serializers.CharField(source ='id_modelo_telefono.no_modelo_telefono')
        """
        sip = sip_buddies.objects.create(
            name = validated_data['name'],
            callerid = validated_data['callerid'],
            context = validated_data['context']
        )
        for telefon in telefono_data:
            sip_telefono.objects.create(**telefono_data, sip=sip)
        """