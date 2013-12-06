import mcpi.minecraft as minecraft
import mcpi.block as block

def build_tower(x,y,z):
	#We build a tower in front of the player
	mc.setBlocks(x-3, y, z-3, x+3, y+9, z+3, block.STONE_BRICK)

mc = minecraft.Minecraft.create(address='localhost', port=4711)
#Here we grab the x y and z coordinates of the player
x,y,z = mc.player.getTilePos()
build_tower(x,y,z)
