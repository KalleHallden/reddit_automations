import sys
import subprocess 
import os

ip = "192.168.0.255"
device = "192.168.0.28:"

proc = subprocess.Popen(["ping", ip],stdout=subprocess.PIPE)
while True:
  line = proc.stdout.readline()
  if not line:
    break
  #the real code does filtering here
  connected_ip = line.decode('utf-8').split()[3]

  if connected_ip == device:
      subprocess.Popen(["say", "Kalle just connected to the network"])
