import sys
import time
from termcolor import colored
import dns.resolver
import dns.query
import dns.zone
import random
import socket
import os

usage = '''
   ___           ___  __        __   
  / _ \___  ___ / _ )/ /__ ____/ /__ 
 / // / _ \(_-</ _  / / _ `/ _  / -_)
/____/_//_/___/____/_/\_,_/\_,_/\__/ 
                                     
	https://github.com/SxNade
'''
us = 'usage :: python3 zone.py <domain>\n'

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

def zone_tsfr(domain, name_server):
	os.system(f'host -l {domain} {name_server}')


for dmn in ns_server_list:
	print(colored(f"[+] Attempting Zone Transfer Against {dmn}", 'green', attrs=['bold']))
	zone_tsfr(domain, dmn)
	print(colored("\n========================================================================", 'blue', attrs=['bold']))
