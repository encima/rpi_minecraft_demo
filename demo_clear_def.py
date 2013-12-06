import mcpi.minecraft as minecraft
import mcpi.block as block

# Same as before, but we use a method here.

def destroy_area(starting_loc, offset):
	mc.setBlocks(starting_loc.x-offset, starting_loc.y-offset, starting_loc.z-offset, starting_loc.x+offset, starting_loc.y+offset, starting_loc.z+offset, block.AIR)

if __name__ == "__main__":
	mc = minecraft.Minecraft.create(address='localhost', port=4711)
	# Call the method and the code above is executed
	destroy_area(mc.player.getPos(), 5) 
