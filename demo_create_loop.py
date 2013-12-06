import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create(address='localhost', port=4711)
x,y,z = mc.player.getPos()

#What does this do?
for i in range(1, 5):
	print i
	mc.setBlock(x+i, y, z+i, block.STONE)
