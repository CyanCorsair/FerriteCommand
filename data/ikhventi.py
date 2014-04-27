#Ikhventi race file

import RaceBP, Buildables, Ships, Technology, Soldiers, Colonies

class ikhventiRace(RaceBP.baseRace):
	def __init__(self):
		self.name = "The Ikhventi"
		self.traits = ()
		
	def createStartingColonies(self):
		pass
		
	#List of ikhventi structures
	class ikhventi_Habitat(Buildables.baseStructure):
		def __init__(self):
			self.built = 0
			self.buildtime = 4
			self.name = "Basic Habitat"
			
	#List of ikhventi ships
	class ikhventi_Colonyship(Ships.shipBase):
		def __init__(self):
			self.name = "Inhabiter"
			self.type = "Corvette"
			self.health = 10
	
	buildables_list = {'structures':{'habitat':ikhventi_Habitat()},
					'vessels':{'colony ship':ikhventi_Colonyship()}}