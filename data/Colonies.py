#Colony file

import humans, ikhventi

class Colony(object):
	def __init__(self, name, owner, location, baseSize, baseType, anomalies):
		self.name = name
		self.location = location
		self.owner = owner
		self.baseSize = baseSize
		self.baseType = baseType
		self.anomalies = anomalies
		
		self.buildings = []
		self.build_list = []
		
		self.food_income = 0
		self.power_income = 0
		self.matter_income = 0
		
		self.used_luxuries = []
		self.used_strategics = []
		self.luxuries = []
		self.strategics = []
		
	def buildActionStructure(self):
		#Receives order from Player class instance, and begins building.
		print """Specify what you wish to build:
		1. Habitat
		2. Power Station
		3. Farm
		4. Factory
		"""
		
		self.structure = raw_input("> ").lower()
		self.to_build = self.owner.race.buildables_list['structures'][self.structure]
		if self.to_build in self.build_list:
			print "You are already building this. Choose another or cancel."
		elif self.to_build in self.buildings:
			print "This building already exists. Choose another or cancel."
		else:
			self.build_list.append(self.to_build)
			print "Now building %s" % self.to_build
			
	def buildActionVessel(self):
		#Receives order from Player class instance, and begins building.
		print """Specify what you wish to build:
		1. Colony Ship
		2. Assault Frigate
		3. Interceptor Wing
		4. Bomber Wing
		"""
		
		self.vessel = raw_input("> ").lower()
		self.to_build = self.owner.race.buildables_list['vessels'][self.vessel]
		self.build_list.append(self.to_build)
		print "Now building %s" % self.to_build
	
	def buildUpdate(self):
		#Runs when Player instance announces a turn update
		for self.buildable in self.build_list:
			self.buildable.built += 1
			if self.buildable.built == self.buildable.buildtime:
				print "%s has finished building." % self.buildable.name
				self.buildings.append(self.buildable)
				self.build_list.remove(self.buildable)
			else:
				print "%i turns remain until %s is built." % (
														(self.buildable.buildtime - self.buildable.built),
														self.buildable.name)
				continue

class habitColony(Colony):
	pass

class spaceColony(Colony):
	pass

class outpostColony(Colony):
	pass

class listeningPost(spaceColony):
	pass
