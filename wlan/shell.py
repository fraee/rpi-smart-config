import os
import time


def run_bash():
    sudoPassword = 'raspberry'
    command1 = 'cp -f /home/pi/confs/wpa_supplicant.conf /etc/wpa_supplicant/'
    command2 = 'cp -f /home/pi/confs/dhcpcd.conf /etc/'
    command3 = "/etc/raspap/hostapd/servicestart.sh --action stop"
    command4 = "systemctl start dhcpcd.service"
    out_str1 = os.system('echo %s|sudo -S %s' % (sudoPassword, command1))
    time.sleep(0.1)
    out_str2 = os.system('echo %s|sudo -S %s' % (sudoPassword, command2))
    time.sleep(0.1)
    out_str3 = os.system('echo %s|sudo -S %s' % (sudoPassword, command3))
    time.sleep(6)
    out_str4 = os.system('echo %s|sudo -S %s' % (sudoPassword, command4))
    print("copy cp -f /home/pi/confs/wpa_supplicant.conf /etc/wpa_supplicant/", out_str1)
    print("cp -f /home/pi/confs/dhcpcd_path.conf /etc/", out_str2)
    print("/etc/raspap/hostapd/servicestart.sh --action stop", out_str3)
    print("systemctl start dhcpcd.service", out_str4)
