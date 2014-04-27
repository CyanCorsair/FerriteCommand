import Buildables, Ships, Technology, Soldiers, Colonies

#Race base blueprint
class baseRace(object):
	def __init__(self):
		self.name = ""
		self.traits = ()
		
	def createStartingColonies(self):
		pass
		
	#List of dummy structures
	class base_Habitat(Buildables.baseStructure):
		def __init__(self):
			self.built = 0
			self.buildtime = 4
			self.name = "Basic Habitat"

	#List of dummy ships
	class base_Colonyship(Ships.shipBase):
		def __init__(self):
			self.name = "Settler"
			self.type = "Frigate"
			self.health = 10
			self.built = 0
			self.buildtime = 5