import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create(address='localhost', port=4711)
x,y,z = mc.player.getTilePos()
mc.setBlock(x+5, y, z, block.STONE)
