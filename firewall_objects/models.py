from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from django.core.exceptions import ValidationError

class FirewallObjects(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:firewall_objects:firewallobjects", args=[self.pk])

class FirewallObjectScopeTag(NetBoxModel):
    firewall_object = models.ForeignKey(
        "FirewallObjects",
        on_delete=models.CASCADE,
        related_name="scope_tag_assignments",
    )
    scope = models.ForeignKey(
        "Scopes",
        on_delete=models.PROTECT,
        related_name="firewall_object_assignments",
    )
    scopetags = models.ForeignKey(
        "ScopeTags",
        on_delete=models.PROTECT,
        related_name="firewall_object_assignments",
    )

    class Meta:
        ordering = ("firewall_object", "scope", "scopetags")
        unique_together = ("firewall_object", "scope", "scopetags")

    def __str__(self):
        return f"{self.firewall_object} | {self.scope} | {self.scopetags}"

    def clean(self):
        super().clean()
        if self.scopetags and self.scope and self.scopetags.scope_id != self.scope_id:
            raise ValidationError({"scopetags": "Selected ScopeTags does not belong to this Scope."})

    def get_absolute_url(self):
        return self.firewall_object.get_absolute_url()


class Scopes(NetBoxModel):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    description = models.TextField(max_length=250, blank=True)


    class Meta:
        ordering = ("name",)
        verbose_name = "Scope"
        verbose_name_plural = "Scopes"


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:firewall_objects:scopes", args=[self.slug])

class ScopeTags(NetBoxModel):
    scope = models.ForeignKey(
        to="firewall_objects.Scopes",
        on_delete=models.CASCADE,
        related_name="scope_tags"
    )
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        ordering = ("scope", "name")
        unique_together = ("scope", "name")

    def __str__(self):
        return f"{self.scope} - {self.name}"

    def get_absolute_url(self):
        return self.scope.get_absolute_url()