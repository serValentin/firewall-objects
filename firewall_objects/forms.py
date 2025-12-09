from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm

from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import FirewallObjects, Scopes, ScopeTags, FirewallObjectScopeTag

class FirewallObjectsForm(NetBoxModelForm):
    class Meta:
        model = FirewallObjects
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields["tags"]  # Remove Netbox tags


class ScopesForm(NetBoxModelForm):
    class Meta:
        model = Scopes
        fields = ('name', 'slug', 'description'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields["tags"]  # Remove Netbox tags


class ScopeTagsForm(NetBoxModelForm):
    class Meta:
        model = ScopeTags
        fields = ('scope', 'name', 'slug')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields["tags"]  # Remove Netbox tags


class FirewallObjectScopeTagForm(NetBoxModelForm):
    class Meta:
        model = FirewallObjectScopeTag
        fields = ("firewall_object", "scope", "scopetags")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields["tags"]  # Remove Netbox tags

        scope = self.initial.get("scope") or self.data.get("scope")

        if scope:
            try:
                scope = Scopes.objects.get(name=scope)
                self.fields['scopetags'].queryset = ScopeTags.objects.filter(scope_id=scope.id)
            except Scopes.DoesNotExist:
                self.fields['scopetags'].queryset = ScopeTags.objects.none()
        else:
            self.fields['scopetags'].queryset = ScopeTags.objects.none()