#Author :: SxNade :: https://github.com/SxNade/DnsBlade ::: SxNade@protonmail.com
#The Code for Zone Transfers was also to be written with the support of dns library but due to some Errors with that host command is used !! YAYAYAA we can use host
# command to also get the name servers ya i KNOw but I wanted to make it independent of host:: but due to some Errors It went Half-way Down LOL ...THIS IS IT!!

import sys
import time
from termcolor import colored
import dns.resolver
import dns.query
import dns.zone
import random
import socket
import os
import re

usage = '''
   ___           ___  __        __   
  / _ \___  ___ / _ )/ /__ ____/ /__ 
 / // / _ \(_-</ _  / / _ `/ _  / -_)
/____/_//_/___/____/_/\_,_/\_,_/\__/ 
                                     
	https://github.com/SxNade
		(For Linux)
'''
us = 'usage :: python3 dnsblade.py <domain>\n'

if len(sys.argv) < 2:
	print(colored(usage, 'red', attrs=['bold']))
	print(us)
	sys.exit()

print(colored(usage, 'red', attrs=['bold']))
print(colored("[+] Initiating Zone Transfer", 'green', attrs=['bold']))
print(colored("=================================================================================================", 'blue', attrs=['bold']))
time.sleep(2)

domain = sys.argv[1]	# Domain name

ns_server_list = []
def ns_server(domain):
	for rdata in dns.resolver.resolve(domain, 'NS'):
		ns = []
		count1 = 0
		while count1 < (len(rdata.target) - 1):
			ns.append(random.randint(0,9))
			count1 += 1
		count = 0
		while count < (len(rdata.target) - 1):
			p = str((rdata.target[count]).decode('utf-8'))
			ns[count] = p
			#ns_server_list.append(ns)
			count += 1
		i = 0
		domn = ""
		while i < len(ns):
			domn += ("." + ns[i])
			i += 1
		domn = domn.replace('.', '', 1)
		ns_server_list.append(domn) 
		ns = []

ns_server(domain)

print(colored("\n[+] Found Name Servers", 'green', attrs=['bold']))
print(ns_server_list)
print(colored("\n-----------------------------------------------------------------------------------", 'blue', attrs=['bold']))

def zone_tsfr(domain, name_server_ip):
	os.system(f'host -l {domain} {name_server_ip}')

for ns_name in ns_server_list:
	store = os.popen(f"host {ns_name}").read().strip()
	ns_name_ip_list = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", store)
	final_ip = ns_name_ip_list[0]
	print(colored(f"[+] Attempting Zone Transfer Against {ns_name}", 'green', attrs=['bold']))
	zone_tsfr(domain, final_ip)
	print(colored("\n========================================================================", 'blue', attrs=['bold']))

