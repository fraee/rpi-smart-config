# #!/usr/bin/python
# # coding=utf-8

wpa_supplicant = '''
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
ssid="%s"
psk="%s"
}
'''

dhcpcd = '''
#RaspAP wlan0 configuration
hostname
clientid
persistent
option rapid_commit
option domain_name_servers, domain_name, domain_search, host_name
option classless_static_routes
option ntp_servers
require dhcp_server_identifier
slaac private
nohook lookup-hostname

interface eth0
static ip_address=172.31.27.144/24
static routers=172.31.27.1
static domain_name_servers=172.31.27.1
noipv6
static domain_search=

interface wlan0
auto wlan0
#static ip_address=10.3.141.1
#static domain_name_servers=180.76.76.76
#static routers=172.31.132.1
#static domain_search=
'''

# wpa_supplicant_path = '/Users/Cheney-Li/Desktop/wpa_supplicant.txt'
# dhcpcd_path = '/Users/Cheney-Li/Desktop/dhcpcd_path.txt'

wpa_supplicant_path = '/home/pi/confs/wpa_supplicant.conf'
dhcpcd_path = '/home/pi/confs/dhcpcd.conf'


def create_conf(ssid, password):
    with open(wpa_supplicant_path, 'w') as file_obj:
        file_obj.write(wpa_supplicant % (ssid, password))
    with open(dhcpcd_path, 'w') as file_obj:
        file_obj.write(dhcpcd)

# create_conf('a', 'abc')
