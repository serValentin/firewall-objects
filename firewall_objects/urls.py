from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("firewall-objectss/", views.FirewallObjectsListView.as_view(), name="firewallobjects_list"),
    path("firewall-objectss/add/", views.FirewallObjectsEditView.as_view(), name="firewallobjects_add"),
    path("firewall-objectss/<int:pk>/", views.FirewallObjectsView.as_view(), name="firewallobjects"),
    path("firewall-objectss/<int:pk>/edit/", views.FirewallObjectsEditView.as_view(), name="firewallobjects_edit"),
    path("firewall-objectss/<int:pk>/delete/", views.FirewallObjectsDeleteView.as_view(), name="firewallobjects_delete"),
    path(
        "firewall-objectss/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="firewallobjects_changelog",
        kwargs={"model": models.FirewallObjects},
    ),
)
