#  

set -e

if [ "$(id -u)" -ne 0 ]; then
    echo "You must be root to run this script."
    exit 1
fi

sudo groupadd netbox-share
sudo usermod -aG netbox-share netbox
sudo usermod -aG netbox-share valdah

sudo chgrp netbox-share /home/valdah
sudo chmod 750 /home/valdah
sudo chgrp -R netbox-share /home/valdah/firewall-objects
sudo chmod -R 750 /home/valdah/firewall-objects
sudo chmod g+s /home/valdah/firewall-objects

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
