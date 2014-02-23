import Colonies, humans, ikhventi

races = {'humans':humans.humanRace(), 'ikhventi':ikhventi.ikhventiRace()}

class Player(object):
	def __init__(self, name):
		self.name = name
		self.owned_colonies = []
		
		self.tax_rate = 0
		self.total_food = 0
		self.total_matter = 0
		self.total_power = 0
		self.supply = [(self.tax_rate * self.total_food) 
						+ (self.tax_rate * self.total_matter) 
						+ (self.tax_rate * self.total_power)]
						
		self.is_ai = False
		self.turn = 0
		self.race = ""
	
	def buildOrderStructure(self):
		#Looks through list of colonies, issues order to individual colony
		print("Specify the colony you wish to build at: \n")
		for self.i in self.owned_colonies:
			print self.i.name
		self.chosen_colony = raw_input("> ").lower()
		for self.i in self.owned_colonies:
			if self.chosen_colony == self.i.name:
				self.chosen_colony = self.i
				self.chosen_colony.buildActionStructure()
			else:
				print "That is not a valid colony name."
				self.buildOrderStructure()
	
	def buildOrderVessel(self):
		#Looks through list of colonies, issues order to individual colony
		print("Specify the colony you wish to build at: \n")
		for self.i in self.owned_colonies:
			print self.i.name
		self.chosen_colony = raw_input("> ").lower()
		for self.i in self.owned_colonies:
			if self.chosen_colony == self.i.name:
				self.chosen_colony = self.i
				self.chosen_colony.buildActionVessel()
			else:
				print "That is not a valid colony name."
				self.buildOrderVessel()
		
	def buildAdvance(self):
		#Looks through list of colonies that have something in their build list
		#and then calls colony-specific build advance funct
		for self.i in self.owned_colonies:
			self.i.buildUpdate()