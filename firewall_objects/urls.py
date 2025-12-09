from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views

app_name = "firewall_objects"


urlpatterns = (
    # FirewallObjects
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


    # Scopes
    path("scopes/", views.ScopesListView.as_view(), name="scopes_list",),
    path("scopes/add/", views.ScopesEditView.as_view(), name="scopes_add",),
    path("scopes/<slug:slug>/", views.ScopesView.as_view(), name="scopes",),
    path("scopes/<int:pk>/edit/", views.ScopesEditView.as_view(), name="scopes_edit",),
    path("scopes/<int:pk>/delete/", views.ScopesDeleteView.as_view(), name="scopes_delete",),
    path(
        "scopes/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="scopes_changelog",
        kwargs={"model": models.Scopes},
    ),
    
    # ScopeTags
    path("scope-tags/add/", views.ScopeTagsEditView.as_view(), name="scopetag_add"),
    path("scope-tags/<int:pk>/delete/", views.ScopeTagsDeleteView.as_view(), name="scopetag_delete"),
    path("firewall-objects/<int:pk>/", views.FirewallObjectsView.as_view(), name="firewallobjects"),

    # child model URLs
    path("firewall-objects/scope-tags/add/", views.FirewallObjectScopeTagEditView.as_view(), name="firewallobjectscopetag_add"),
    path("firewall-objects/scope-tags/<int:pk>/edit/", views.FirewallObjectScopeTagEditView.as_view(), name="firewallobjectscopetag_edit"),
    path("firewall-objects/scope-tags/<int:pk>/delete/", views.FirewallObjectScopeTagDeleteView.as_view(), name="firewallobjectscopetag_delete")
)
