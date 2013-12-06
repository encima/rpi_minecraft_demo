import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create(address='localhost', port=4711)
#Get the location of our character
loc = mc.player.getPos()
#We pass the starting x,y,z and the end x,y,z. All the blocks in that grid will be replaced by air.
mc.setBlocks(loc.x-5, loc.y-5, loc.z-5, loc.x+5, loc.y+5, loc.z+5, block.AIR)
