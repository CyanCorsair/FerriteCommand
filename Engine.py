import Core

class Engine(object):
	
	'''setupPhases = {'setupAI':Core.gameSetup().createAI(), 
					'setupHuman':Core.gameSetup().createPlayer(), 
					'start':Core.gameSetup().startGame(),
					'load':Core.gameSetup().loadGame()}

	turnDict = {'t_start':Core.turnStructure().turnStart(),
				'mid':Core.turnStructure().turnMid(), 
				'end':Core.turnStructure().turnEnd(), 
				'playerswap':Core.turnStructure().playerChange()}'''
	
ferrusgame = Core.gameSetup()
ferrusgame.setupGame()