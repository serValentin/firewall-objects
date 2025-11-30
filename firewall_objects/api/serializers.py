from netbox.api.serializers import NetBoxModelSerializer
from ..models import FirewallObjects

class FirewallObjectsSerializer(NetBoxModelSerializer):
    class Meta:
        model = FirewallObjects
        fields = ('name',)