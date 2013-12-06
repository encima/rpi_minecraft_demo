import mcpi.minecraft as minecraft

#Connect to our running Minecraft game
mc = minecraft.Minecraft.create(address='localhost', port=4711)
#Now we use the mc object to 'talk' to the game, here we add a chat message
mc.postToChat('hello!')

