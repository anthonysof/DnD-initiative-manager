import random
from random import randint
import sys
import os

class Character:
	name = []
	initiative = 0
	advantage = 0
	def __init__(self, name, initiative):
		self.name = name
		self.initiative = initiative
	def rollInitiative(self):
		if self.advantage == 0:
			rng = random.SystemRandom()
			return self.initiative + rng.randint(1,20)
		elif self.advantage == -1:
			rng1 = random.SystemRandom()
			rng2 = random.SystemRandom()
			return self.initiative + min(rng1.randint(1,20),rng2.randint(1,20))
		else:
			rng1 = random.SystemRandom()
			rng2 = random.SystemRandom()
			return self.initiative + max(rng1.randint(1,20),rng2.randint(1,20))

	def hasAdvantage(self):
		if self.advantage == 0:
			return "Normal"
		elif self.advantage == 1:
			return "Has Advantage!"
		else:
			return "Has Disadvantage!"

def main():
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
			name = raw_input()
			print "Give me his init bonus"
			while True:
				try:
					init = int(raw_input())
					break
				except ValueError:
					print "Integers only!"
			players.append(Character(name, init))
	else:
		filename = raw_input("Give me name of file: ")
		filestring = ""
		try:
			with open(filename) as filein:
				lista = []
				for line in filein:
					filestring += line.replace("\n"," ")
				lista = filestring.split(" ")
				for i in range(0,len(lista),2):
					if i >= len(lista) - 1:
						break
					obj = Character(lista[i],int(lista[i+1]))
					players.append(obj)
			filein.close()
			for player in players:
				print player.name, player.initiative
		except IOError:
			print "File doesnt exist. Try again..."
			sys.exit()


	while True:
		final = {}
		monsters = []
		initiatives2 = []
		players2 = []
		choice = ""
		print "1. initiate encounter \n2. Change modifiers or advantage\n0. Exit"
		choice = raw_input()
		if choice == "0":
			sys.exit()
		elif choice == "1":
			print "give me number of dm creatures: "
			try:
				n = int(raw_input())
			except ValueError:
				continue
			for player in players:
				players2.append(player.name)
				initiatives2.append(player.rollInitiative())

			for i in range(n):
				print "give me dm: "
				players2.append(raw_input())
				print "give me his initiative: "
				initiatives2.append(int(raw_input()))
			
			final = zip(players2, initiatives2)
			final = dict(final)
			os.system('cls' if os.name == 'nt' else 'clear')
			print final
			i = 0
			for key, value in reversed(sorted(final.iteritems(), key = lambda(k,v): (v,k))):
				print str(i+1)+". "+str(key)+" "+str(value)
				i += 1
			print "-------------\n"

		elif choice == "2":
			found = False
			os.system('cls' if os.name == 'nt' else 'clear')

			for player in players:
				print player.name, player.initiative, player.hasAdvantage()
			print "\nEnter name of character to be modified: "
			name = raw_input().lower()
			for player in players:
				if name == player.name.lower():
					modding = name 
					found = True
					modplayer = player
					break
				
			if found:
				while True:
					os.system('cls' if os.name == 'nt' else 'clear')
					print "\nModifying ", player.name, player.initiative, player.hasAdvantage()
					print "1. Modify initiative modifier\n2. Set Advantage/Disadvantage \n0. Go back\n"
					choice = raw_input()
					if choice == "0":
						break
					elif choice == "1":
						print "Give me new initiative modifier: "
						try:
							init = int(raw_input())
						except ValueError:
							print "Integers only!"
							continue
						modplayer.initiative = init
						print modplayer.name, modplayer.initiative 
						raw_input("Enter to continue...")
					elif choice == "2":
						print "\nGive me 'd' for Disadvantage, 'a' for Advantage, anything else for nothing"
						hasAdv = raw_input()
						if hasAdv == 'd':
							modplayer.advantage = -1
						elif hasAdv == 'a':
							modplayer.advantage = 1
						else:
							modplayer.advantage = 0
						print modplayer.name, modplayer.initiative, modplayer.hasAdvantage(),"\n"
						raw_input("Enter to continue...")
					else:
						print "\nInvalid input..."
			else:
				print "\nPlayer not found."



		else:
			continue

if __name__ == '__main__':
	main()

