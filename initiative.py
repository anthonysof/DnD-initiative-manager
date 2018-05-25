import random
from random import randint
import sys

players = []
initiatives = []
flag = True
final = {}
choice = ""
while True:
	print "Read from file y/n ? "
	choice = raw_input()
	if choice == "y" or choice == "n":
		break
	else:
		print "Invalid input, try again."

if choice == "n":
	print "Give me number of players: "
	n = int(raw_input())

	for i in range(n):
		print "Give me name of player: "
		players.append(raw_input())
		print "Give me his init bonus"
		initiatives.append(int(raw_input()))
else:
	filename = raw_input("Give me name of file: ")
	filestring = ""
	try:
		with open(filename) as filein:
			lista = []
			for line in filein:
				filestring += line.replace("\n"," ")
			lista = filestring.split(" ")
			index = 0
			for item in lista:
				if index%2 == 0:
					players.append(item)
				else:
					initiatives.append(int(item))
				index += 1
		f.close()

	except IOError:
		print "File doesnt exist. Try again..."


while True:
	final = {}
	monsters = []
	initiatives2 = []
	players2 = []
	choice = ""
	print "1. initiate encounter \n0. Exit"
	choice = raw_input()
	if choice == "0":
		sys.exit()
	elif choice == "1":
		print "give me number of dm creatures: "
		try:
			n = int(raw_input())
		except ValueError:
			continue
		for init in initiatives:
			rng = random.SystemRandom()
			initiatives2.append(init+rng.randint(1,20))

		for i in range(n):
			print "give me dm: "
			monsters.append(raw_input())
			print "give me his initiative: "
			initiatives2.append(int(raw_input()))
		
		players2 = players + monsters
		final = zip(players2, initiatives2)
		final = dict(final)
		print final
		for key, value in reversed(sorted(final.iteritems(), key = lambda(k,v): (v,k))):
			print str(key)+" "+str(value)
	else:
		continue



