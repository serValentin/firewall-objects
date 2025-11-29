from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class FirewallObjectsView(generic.ObjectView):
    queryset = models.FirewallObjects.objects.all()


class FirewallObjectsListView(generic.ObjectListView):
    queryset = models.FirewallObjects.objects.all()
    table = tables.FirewallObjectsTable


class FirewallObjectsEditView(generic.ObjectEditView):
    queryset = models.FirewallObjects.objects.all()
    form = forms.FirewallObjectsForm


class FirewallObjectsDeleteView(generic.ObjectDeleteView):
    queryset = models.FirewallObjects.objects.all()
