import mcpi.minecraft as minecraft

def tp_player(x,y,z):
	#If getPos gets the position, what does setPos do?
	print 'teleporting'
	mc.player.setPos(x+20, y+40, z+20)

mc = minecraft.Minecraft.create(address='localhost', port=4711)
x,y,z = mc.player.getPos()
#Call tp_player method
tp_player(x,y,z)
