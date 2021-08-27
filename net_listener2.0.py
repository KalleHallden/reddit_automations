import nmap
import gi
gi.require_version("Notify",'0.7')
from gi.repository import Notify
Notify.init("Intruder Alert")
from decouple import config
import datetime
notification = Notify.Notification.new("Intruder alert launched",str(datetime.datetime.now().time().strftime("%H:%M")),
                    "account-logged-in")
notification.show()
notification.set_urgency(0)

IP_NETWORK = config("IP_NETWORK")
IP_IPHONE = config("IP_IPHONE")
IP_LAPTOP = config("IP_LAPTOP")
IP_RANGE = config("IP_RANGE")

family = {"your_ip":"brother","mother":"father"}

while_list = ["your_ip",IP_LAPTOP]

nm = nmap.PortScanner()
showed = False
while(True):
    nm.scan(hosts=IP_RANGE, arguments='-n -sP -PE -PA21,23,80,3389')
    for host in nm.all_hosts():
        if host not in while_list and host not in family.keys() and host!=IP_IPHONE:
            notification.update("Intruder Alert!","Device ip: <b>"+str(host)+"</b>",
                    "dialog-error")
            notification.show()
            notification.set_urgency(1)
            showed = False
            print("Intruder")
        if host in family.keys():
            notification.update("Intruder Alert!","Device: <b>"+family[host]+"</b>",
                    "dialog-error")
            notification.show()
            notification.set_urgency(1)
            showed = False
            print("Family")
        if host == IP_IPHONE and showed == False:
            notification.update("Device connected","<b>iPhone: "+str(host)+"</b>",
                    "dialog-apply")
            notification.show()
            notification.set_urgency(1)
            showed = True
            print("Personal")


            

