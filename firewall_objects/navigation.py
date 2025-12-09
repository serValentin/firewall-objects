from netbox.plugins import PluginMenu, PluginMenuItem
from django.conf import settings
plugins_settings = settings.PLUGINS_CONFIG.get('firewall_objects')

menu_buttons = (
    PluginMenuItem(
        link_text="Firewall Objects",
        link="plugins:firewall_objects:firewallobjects_list",
        permissions=["firewall_objects.FirewallObjectsView"],
    ),
    PluginMenuItem(
        link_text="Scopes",
        link="plugins:firewall_objects:scopes_list",
        permissions=["firewall_objects.scopesView"],
    ),
)

menu_items = menu_buttons