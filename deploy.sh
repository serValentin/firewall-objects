#  

set -e


GROUP="netbox-share"
USERS=("netbox" "valdah")
HOME_DIR="/home/valdah"
PLUGIN_DIR="$HOME_DIR/firewall-objects"

if [ "$(id -u)" -ne 0 ]; then
    echo "You must be root to run this script."
    exit 1
fi

echo "Ensuring group '$GROUP' exists..."
if ! getent group "$GROUP" >/dev/null; then
  groupadd "$GROUP"
fi

echo "Ensuring users are members of '$GROUP'..."
for u in "${USERS[@]}"; do
  if id "$u" &>/dev/null; then
    if ! id -nG "$u" | tr ' ' '\n' | grep -qx "$GROUP"; then
      usermod -aG "$GROUP" "$u"
      echo "  Added $u to $GROUP"
    else
      echo "  $u is already in $GROUP"
    fi
  else
    echo "  Warning: user '$u' does not exist, skipping" >&2
  fi
done

if [[ -d "$HOME_DIR" ]]; then
  echo "Setting group and permissions on $HOME_DIR..."
  chgrp "$GROUP" "$HOME_DIR"
  chmod 750 "$HOME_DIR"
else
  echo "Warning: $HOME_DIR does not exist, skipping" >&2
fi

if [[ -d "$PLUGIN_DIR" ]]; then
  echo "Setting group and permissions on $PLUGIN_DIR..."
  chgrp -R "$GROUP" "$PLUGIN_DIR"
  chmod -R 750 "$PLUGIN_DIR"
  chmod g+s "$PLUGIN_DIR"
else
  echo "Warning: $PLUGIN_DIR does not exist, skipping" >&2
fi

source /opt/netbox/venv/bin/activate
cd /home/valdah/firewall-objects
pip install -e .



if grep -q "firewall_objects" /opt/netbox/netbox/netbox/configuration.py; then
    echo "firewall_objects is already in configuration.py"
else
    echo "Adding firewall_objects to configuration.py"
    echo >> /opt/netbox/netbox/netbox/configuration.py
    echo "PLUGINS.append('firewall_objects')" >> /opt/netbox/netbox/netbox/configuration.py
fi

if grep -q "DEVELOPER = True" /opt/netbox/netbox/netbox/configuration.py; then
    echo "DEVELOPER mode is already enabled in configuration.py"
else
    echo "Enabling DEVELOPER mode in configuration.py"
    echo >> /opt/netbox/netbox/netbox/configuration.py
    echo "DEVELOPER = True" >> /opt/netbox/netbox/netbox/configuration.py
fi


# Deploy script for firewall-objects NetBox plugin
systemctl restart netbox
systemctl restart netbox-rq

python /opt/netbox/netbox/manage.py makemigrations firewall_objects
python /opt/netbox/netbox/manage.py migrate firewall_objects

echo "Firewall Objects plugin deployed successfully."
