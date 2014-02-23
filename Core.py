from sys import stdin, exit
from random import choice
import Player, Colonies

player_list = []
game = True

class gameSetup(object):
	def __init__(self):
		self.max_players = 0
		self.player_limit = 12
		self.starting_era = 0
		self.players = 0
	
	def setupGame(self):
		self.decision = raw_input("Do you wish to start a new game or load one? \n>")

		if 'new game' in self.decision:
			self.createPlayer()
		else:
			print 'That is invalid.'
	
	def createPlayer(self):
		global player_list
	
		self.input = raw_input("Please enter your desired player name: \n>")
		vars()[self.input] = Player.Player(self.input)
		self.input_race = raw_input("""Please choose a race to play: 
		1. Humans
		2. Ikhventi \n>""")
		if self.input_race in Player.races:
			vars()[self.input].race = Player.races[self.input_race]
			print vars()[self.input].race.name
			vars()[self.input].owned_colonies.append(Colonies.Colony("earth city", vars()[self.input]))
			for self.i in vars()[self.input].owned_colonies:
				print "You are starting with %s" % self.i.name
				print self.i.owner
		else:
			print "Race not found. Try again."
		player_list.append(vars()[self.input])
		print "Do you wish to include another?"
		self.input = raw_input("> ")
		if self.input == "yes":
			self.createPlayer()
		else:
			print "Then we shall set up the A.I."
			self.createAI()
				
	def createAI(self):
		global player_list
		self.i = 0
		self.ai_names = ['bob', 'bill', 'jebediah', 
		'john', 'is', 'kill', 'tom']
		
		print "How many A.I players do you want?"
		
		self.max_players = raw_input("> ")
		self.max = int(self.max_players)
		if self.max < self.player_limit:
			print "Setting up A.I."
			while self.i < self.max:
				vars()[self.i] = Player.Player(choice(self.ai_names))
				vars()[self.i].is_ai = True
				player_list.append(vars()[self.i])
				self.i += 1
			print player_list
			print "Begin game? (Y/N)"
			self.startGame()
		else:
			print "Over the player limit. Try again."
			self.createAI()
	
	def startGame(self):
		self.input = raw_input("> ")
		if self.input == "yes" or self.input == "y":
			turnStructure().__init__()
		elif self.input == "no" or self.input == "n":
			exit(0)
		else:
			print "Wut?"

class turnStructure(object):
	def __init__(self):
		global player_list
		global game
	
		while game:
			for self.current_player in player_list:
				self.turnStart()

	
	def turnStart(self):
		self.current_player.turn += 1
		self.current_player.buildAdvance()
		print "----------------"
		print "It is now %s's turn %i." % (self.current_player.name, self.current_player.turn)
		print "Beginning %s's turn. \n" % self.current_player.name
		if self.current_player.is_ai == False:
			#Calculate new resources, building queues. Echo updates.
			self.turnMid()
		else:
			#Calculate new resources, building queues. Echo updates.
			self.ai_turnMid()

	def turnMid(self):
		self.input = raw_input("Choose what to do. \n> ")
	
		if "end turn" in self.input:
			self.turnEnd()
		elif "build" in self.input:
			self.choice = raw_input("Do you wish to build a vessel or a structure? \n>")
			if self.choice == "structure":
				self.current_player.buildOrderStructure()
			elif self.choice == "vessel":
				self.current_player.buildOrderVessel()
			self.turnMid()
		elif "colonize" in self.input:
			self.col_location = raw_input("Choose a location to found the colony at. \n>")
			for self.i in starsystem.bodylist: #Requires edits
				if self.col_location == starsystem.bodylist.name: #This too
					self.col_location = self.i
					self.col_name = raw_input("Now choose a name for the colony. \n>")
					self.new_colony = Colonies.Colony(self.col_name, self.current_player, self.col_location)
					self.current_player.owned_colonies.append(self.new_colony)
				else:
					print "This planet does not exist."
					self.turnMid()
			self.turnMid()
		elif "cancel" in self.input:
			self.turnMid()
		else:
			print "u wot m8?"
			self.turnMid()
			
	def ai_turnMid(self):
		print "I am an A.I named %s. \n" % self.current_player.name
		print "----------------"
		self.turnEnd()

	def turnEnd(self):
		#Resolve remaining resources and queued moves.
		pass