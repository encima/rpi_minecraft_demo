import mcpi.minecraft as minecraft
import mcpi.block as block

class MegaMinecraft:

	def __init__(self, mc):
		self.mc = mc

	def move_player(self, x, y, z):
		self.mc.player.setPos(x, y, z)

	def chat(self, msg):
		self.mc.postToChat(msg)

	def clearArea(self, x, y, z):
		self.mc.setBlocks(x-5, y-5, z-5, x+5, y+5, z+5, block.AIR)

	def build_tower(self, x, y, z):
		#We build a tower in front of the player
		self.mc.setBlocks(x-3, y, z-3, x+3, y+9, z+3, block.STONE_BRICK)

mc = minecraft.Minecraft.create(address='localhost', port=4711)
mm = MegaMinecraft(mc)
mm.chat('Hello')
x, y, z = mc.player.getTilePos()
mm.move_player(x + 10, y + 10, z + 10)
