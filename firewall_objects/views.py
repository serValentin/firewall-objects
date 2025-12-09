from django.db.models import Count

from django_tables2 import RequestConfig
from netbox.views import generic
from . import filtersets, forms, models, tables

# FirewallObjects Views
class FirewallObjectsView(generic.ObjectView):
    queryset = models.FirewallObjects.objects.all()
    def get_extra_context(self, request, instance):
        # Get all scope tag assignments for this firewall object
        assignments = models.FirewallObjectScopeTag.objects.filter(
            firewall_object=instance
        )

        # Instantiate the table with the queryset
        assignments_table = tables.FirewallObjectScopeTagTable(assignments)

        # Let django-tables2 configure pagination/sorting
        RequestConfig(request).configure(assignments_table)

        return {
            "assignments_table": assignments_table,
        }

class FirewallObjectsListView(generic.ObjectListView):
    queryset = models.FirewallObjects.objects.all()
    table = tables.FirewallObjectsTable


class FirewallObjectsEditView(generic.ObjectEditView):
    queryset = models.FirewallObjects.objects.all()
    form = forms.FirewallObjectsForm


class FirewallObjectsDeleteView(generic.ObjectDeleteView):
    queryset = models.FirewallObjects.objects.all()


# Scopes Views
class ScopesView(generic.ObjectView):
    queryset = models.Scopes.objects.all()
    lookup_field = 'slug'


class ScopesListView(generic.ObjectListView):
    queryset = models.Scopes.objects.all()
    table = tables.ScopesTable
    template_name = "firewall_objects/scopes_list.html"


class ScopesEditView(generic.ObjectEditView):
    queryset = models.Scopes.objects.all()
    form = forms.ScopesForm


class ScopesDeleteView(generic.ObjectDeleteView):
    queryset = models.Scopes.objects.all()


# ScopeTags Views
class ScopeTagsEditView(generic.ObjectEditView):
    queryset = models.ScopeTags.objects.all()
    form = forms.ScopeTagsForm

    def get_initial(self):
        initial = super().get_initial()
        scope_id = self.request.GET.get('scope')
        if scope_id:
            initial['scope'] = scope_id
        return initial

class ScopeTagsDeleteView(generic.ObjectDeleteView):
    queryset = models.ScopeTags.objects.all()

    def get_return_url(self, request, obj=None):
        if obj and obj.scope:
            return obj.scope.get_absolute_url()
        return super().get_return_url(request, obj)


# Firewall objects connection scope:tag
class FirewallObjectScopeTagEditView(generic.ObjectEditView):
    queryset = models.FirewallObjectScopeTag.objects.all()
    form = forms.FirewallObjectScopeTagForm

    def get_initial(self):
        initial = super().get_initial()
        firewall_object_id = self.request.GET.get("firewall_object")
        if firewall_object_id:
            initial["firewall_object"] = firewall_object_id
        return initial


class FirewallObjectScopeTagDeleteView(generic.ObjectDeleteView):
    queryset = models.FirewallObjectScopeTag.objects.all()

    def get_return_url(self, request, obj=None):
        if obj and obj.firewall_object:
            return obj.firewall_object.get_absolute_url()
        return super().get_return_url(request, obj)
