"""Top-level package for NetBox firewall-objects Plugin."""

__author__ = """Valentin Dahlén"""
__email__ = "valentin.automation@gmail.com"
__version__ = "0.1.0"


from netbox.plugins import PluginConfig


class FirewallObjectsConfig(PluginConfig):
    name = "firewall_objects"
    verbose_name = "NetBox firewall-objects Plugin"
    description = "NetBox plugin for firewall-objects"
    version = "0.1.0"
    base_url = "firewall_objects"


config = FirewallObjectsConfig
