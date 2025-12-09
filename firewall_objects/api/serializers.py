from netbox.api.serializers import NetBoxModelSerializer
from ..models import FirewallObjects, Scopes, ScopeTags

class FirewallObjectsSerializer(NetBoxModelSerializer):
    class Meta:
        model = FirewallObjects
        fields = ('name',)

class ScopesSerializer(NetBoxModelSerializer):
    class Meta:
        model = Scopes
        fields = ('name', 'slug', 'description')

class ScopeTagsSerializer(NetBoxModelSerializer):
    class Meta:
        model = ScopeTags
        fields = ('id', 'display', 'scope', 'name', 'created', 'last_updated')
        brief_fields = ('id', 'display', 'name')