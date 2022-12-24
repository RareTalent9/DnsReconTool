#!/usr/bin/python3
import argparse, os, sys, subprocess
parser=argparse.ArgumentParser(description="DNS Recon")
parser.add_argument("-d", type=str, help="Type domain", required=True)
parser.add_argument("-reconall", help="Type domain", required=False, action="store_true")
a=parser.parse_args()
def callA():
	print("Address Mapping Record is :")
	os.system("host -t A {}".format(a.d))
def reconall():
	print("*******************************************************************")
	print("Address Mapping Record (A) is: ")
	os.system("host -t A {}".format(a.d))
	ip=subprocess.getoutput("host -t A {}".format(a.d))
	ptr=ip.split()
	list = []
	for i in range(3,len(ptr),4):
		list.append(ptr[i])
	print("***************************************************************************************************************")
	print("IPv6 records: ")
	os.system("host -t AAAA {}".format(a.d))
	print("***************************************************************************************************************")
	print("Start of Authority records (SOA):")
	os.system("host -t SOA {}".format(a.d))
	print("***************************************************************************************************************")
	print("Mail Exchanger (MX) records are: ")
	os.system("host -t MX {}".format(a.d))
	print("***************************************************************************************************************")
	print("Text Records (TXT, if any): ")
	str=subprocess.getoutput("host -t MX {}".format(a.d))
	x=str.split()
	os.system("host -t TXT {}".format(x[6]))	
	print("***************************************************************************************************************")
	print("Name Server records (NS): ")
	os.system("host -t NS {}".format(a.d))
	print("***************************************************************************************************************")
	print("Reverse lookup pointer (PTR) records")
	for j in list:
		os.system("host -t PTR {}".format(j))
	print("***************************************************************************************************************")
if a.d != "None" and a.reconall == False:
	callA()
elif a.reconall == True:
	reconall()

else:
	print("ERROR")
