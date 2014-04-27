#Stellar body file

class nonplanetBody(object):
	def __init__(self):
		self.type = None
		self.anomalies = []
		

class planetBody(object):
	def __init__(self):
		self.size = None
		self.type = None
		self.anomalies = []
		self.has_colony = False
		
		self.typeList = ["temperate", "lush", "ocean", "gas", 
						"lava", "ice", "barren", "desert"]
		
		self.anomalyList = ["high_grav", "low_grav", "geo_active",
						"kessler_syndrome", "mag_storms", "no_atmo",
						"sleeper_relics", "malans_relics"]