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
	
	def colonizationOrder(self):
		#Returns a list of stellar bodies in a given star system,
		#and then begins colonization.
		print "Specify your chosen star system: \n"
		self.starsys_choice = raw_input("> ").lower()
		for self.i in Starsystems.starsys_list:
			if self.starsys_choice in self.i:
				print "Which stellar body would you like to colonize? \n"
				self.body_choice = raw_input("> ").lower()
				for self.j in self.starsys_choice.bodies:
					if self.body_choice in self.j:
						self.newColonyName = raw_input("Please enter your colony name: ")
						print "Founding colony. \n"
						self.colony = Colonies.Colony(self.newColonyName, self.body_choice, self,
													self.body_choice.size, self.body_choice.type,
													self.body_choice.anomalies)
						self.owned_colonies.append(self.colony)
						print "Founded %s", self.colony.name
						print "Current colonies: ", self.owned_colonies
	
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