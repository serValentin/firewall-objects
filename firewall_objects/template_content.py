from netbox.plugins.templates import PluginTemplateExtension

class ScopesListButtons(PluginTemplateExtension):
    model = "firewall_objects.scope"   # <-- use this
    def list_buttons(self):
        return self.render("firewall_objects/scope_list_buttons.html")
template_extensions = [ScopesListButtons]