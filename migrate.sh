#

set -e

if [ "$(id -u)" -ne 0 ]; then
    echo "You must be root to run this script."
    exit 1
fi

source /opt/netbox/venv/bin/activate

echo "Applying migrations for firewall_objects..."
python /opt/netbox/netbox/manage.py makemigrations firewall_objects
python /opt/netbox/netbox/manage.py migrate firewall_objects

echo "Migration completed successfully."