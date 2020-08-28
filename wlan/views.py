import json

from django.shortcuts import render
from django.shortcuts import HttpResponse

from wlan.wlanlist import get_scanner
# import wlan.wlanlist as wl
import wlan.conf as conf
import wlan.shell as shell


# Create your views here.
def index(request):
    wifi_scanner = get_scanner()
    access_points = wifi_scanner.get_access_points()
    print(access_points)
    jsonstr = json.dumps(access_points)
    print('all wifis:', jsonstr)
    ssid_dic = {}
    for v in access_points:
        ssid_dic[v['ssid']] = v['quality']
    ssid_dic_sort = sorted(ssid_dic.items(), key=lambda item: item[1], reverse=True)
    ssid_arr = []
    for ssid in ssid_dic_sort:
        ssid_arr.append(ssid[0])
    # return HttpResponse("I'm here")
    return render(request, "wlan.html", {"ssid_arr": ssid_arr})


def connect(request):
    ssid = ""
    password = ""
    if request.method == "POST":
        ssid = request.POST.get("ssid", None)
        password = request.POST.get("password", None)
        conf.create_conf(ssid, password)
    print("received params: ", ssid, password)
    shell.run_bash()
    return HttpResponse("OK")
