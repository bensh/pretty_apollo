#!/usr/bin/python
'''
Copyright (c) 2019, Ben Marks @bensh
All rights reserved.

Author and Apollo moficiations: Ben Marks | @bensh
Original Apollo Author: Sarah Edwards | @iamevltwin | mac4n6.com

'''
import subprocess, os, argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="\
	\t\tPretty APoLLO\
	\n\n\tTakes output from APoLLO, adds spacing and makes it easier to read compared to \
	\n\tthe standard output of the data column in SQL or CSV.\
	\n\tSQL and CSV are still output for verification of original data.\
	\n\tCan be used in interactive mode for all options, or headless mode (--head)\
	\n\twhich uses yolo mode for platform and version.\
	\
	\n\n\tStandard: python pretty_apollo.py\
	\n\n\tHeadless: python pretty_apollo.py --head -o sql|csv -mod_dir PATH_TO_MODULES PATH_TO_DATA\
	\
	\n\n\tAuthor and Apollo modifications: Ben Marks | @bensh\
	\n\tOriginal Apollo Author: Sarah Edwards | @iamevltwin | mac4n6.com",
		formatter_class=RawTextHelpFormatter)
parser.add_argument('--head', action='store_true',  help="Use headless non interactive mode which runs as yolo")
parser.add_argument('-o', choices=['sql','csv'], required=False, action="store", help="sql=SQLite or csv=CSV")
parser.add_argument('-mod_dir',required=False, action="store", help="Path to Module Directory")
parser.add_argument('data_dir', nargs="?", help="Path to Data directory, either full file dump or directory of extracted databases, it is recursive.")

args = parser.parse_args()

def create_files():
	filename = 'apollo_raw.txt'
	outfile = 'apollo_process.txt'

	if os.path.isfile('apollo_process.txt'):
		os.remove('apollo_process.txt')

	f = open(filename, "r")
	o = open(outfile,"a")
	for ln in f:   

		str = ln.replace('[','')
		new_str = str.split(']')
		str = '\n'.join(new_str) 
		o.write(str)
		
	print 'Done\n '
	print 'Data prettfied to apollo_pretty.txt '
	print out + ' file also created for ' + plat + ' running version ' + ver
	f.close()
	o.close()
	os.remove('apollo_raw.txt')

if args.head:
	out = args.o
	mod = args.mod_dir
	file = args.data_dir
	if file is None:
		print 'Path to data directory needs to be supplied, see -h for details'
	else:
		print '\nRunning Apollo'
		os.system('python apollo_txt.py -o ' + out + ' -p yolo -v yolo ' + mod + ' ' + file)
		create_files()
	
else:
	while True:
		out = raw_input('Output format {sql|csv}: ').lower()
		if out not in ["sql", "csv"]:
			print '\t*** Value blank or not valid **'		
		else:
			break

	while True:
		plat = raw_input('Platform {ios|mac|yolo}: ').lower()
		if plat not in ["ios", "mac", "yolo"]:
			print '\t*** Value blank or not valid **'
		else:
			break

	while True:
		ver = raw_input('iOS version {8|9|10|11|12|yolo}: ').lower()
		if ver not in ["8", "9", "10", "11", "12", "yolo"]:
			print '\t*** Value blank or not valid **'
		else:
			break
			
	while True:
		mod = raw_input('Module directory: ') 
		if file is "":
			print '\t*** Value blank or not valid **'
		else:
			break

	while True:
		file = raw_input('Data path directory: ') 
		if file is "":
			print '\t*** Value blank or not valid **'
		else:
			break

	print '\nRunning Apollo'
	os.system('python apollo_txt.py -o ' + out + ' -p ' + plat + ' -v ' + ver + ' "' + mod + '" "' + file + '"')
	create_files()




