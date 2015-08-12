#!/usr/bin/python

# simple script to extract private keys from binary files
# created by Hanno Boeck
# License: CC0 / Public domain

import sys,subprocess,re,os

if len(sys.argv)!=3:
	print("Usage:")
	print("\tgetkey.py [input] [output]")
	sys.exit()

f = open(sys.argv[1])

s = f.read()

i=0
for pp in re.finditer('\x30\x82', s):
	f.seek(pp.start())
	key = f.read(8192)

	p = subprocess.Popen(['openssl','pkey','-inform','der'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out = p.communicate(input=key)
	if p.returncode == 0:
		print("found private key, written to %s-%i" % (sys.argv[2], i))
		of = open("%s-%i" % (sys.argv[2], i),"w");
		of.write(out[0])
		i+=1
