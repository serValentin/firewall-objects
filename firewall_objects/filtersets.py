from netbox.filtersets import NetBoxModelFilterSet
from .models import FirewallObjects


# class FirewallObjectsFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = FirewallObjects
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
