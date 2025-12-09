import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn

from .models import FirewallObjects, Scopes, ScopeTags, FirewallObjectScopeTag


class FirewallObjectsTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = FirewallObjects
        fields = ("pk", "id", "name", "actions")
        default_columns = ("name",)

class ScopesTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = Scopes
        fields = ("pk", "id", "name", "slug", "actions")
        default_columns = ("name",)

class ScopeTagsTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = ScopeTags
        fields = ("name", "scope",)
        default_columns = ("name",)

class FirewallObjectScopeTagTable(NetBoxTable):
    scope = tables.Column()
    tag = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = FirewallObjectScopeTag
        fields = ("scope", "tag", "actions")
        default_columns = ("scope", "tag")