import mcpi.minecraft as minecraft
import sys

mc = minecraft.Minecraft.create(address='localhost', port=4711)
#Same as before, but now we can provide arguments to the game and it will say that instead
if len(sys.argv) > 0:
	mc.postToChat(sys.argv[1])
