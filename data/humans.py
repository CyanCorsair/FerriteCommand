#human race file

import RaceBP, Buildables, Ships, Technology, Soldiers

class humanRace(RaceBP.baseRace):
	def __init__(self):
		self.name = "The Humans"
		self.traits = ()
		
	#List of human structures
	class human_Habitat(Buildables.baseStructure):
		def __init__(self):
			self.built = 0
			self.buildtime = 4
			self.name = "Basic Habitat"

	#List of human ships
	class human_Colonyship(Ships.shipBase):
		def __init__(self):
			self.name = "Settler"
			self.type = "Frigate"
			self.health = 10
			self.built = 0
			self.buildtime = 5
		
	buildables_list = {'structures':{'habitat':human_Habitat()},
					'vessels':{'colony ship':human_Colonyship()}}