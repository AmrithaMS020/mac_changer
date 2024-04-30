#!/user/bin/env python

import subprocess

interface=input("interface >")
new_mac=input("new_mac >")

subprocess.call(["ifconfig", interface,"down"])
subprocess.call(["ifconfig", interface,"hw","ether",new_mac])
subprocess.call(["ifconfig", xxinterface,"up"])
subprocess.call(["ifconfig"])


