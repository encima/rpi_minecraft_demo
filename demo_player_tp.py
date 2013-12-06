import mcpi.minecraft as minecraft

def tp_player(x,y,z):
	#If getPos gets the position, what does setPos do?
	mc.player.setPos(x+20, y+40, z+20)

if __name__ == "main":
	mc = minecraft.Minecraft.create(address='localhost', port=4711)
	x,y,z = mc.player.getTilePos()
	#Call tp_player method
	tp_player(p_loc)
