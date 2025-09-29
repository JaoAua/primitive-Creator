import maya.cmds as cmds

def createObjects(prim):
	if prim == 'cube':
		cmds.polyCube()
	elif prim == 'cone':
		cmds.polyCone()
	elif prim == 'sphere':
		cmds.polyShpere()
	else:
		cmds.polyTorus()