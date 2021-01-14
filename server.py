import socket, time, os, discord, threading, sys
from PIL import Image 
import pyautogui as pg


file_name = 'screenshot_shot.png'

token = "??????????????????????????????????????????????????????????????????????????????????????????????????"

finished = False

class Bot(discord.Client):		
		async def abort_off(self):
			print("Finished")
			await self.logout()

		def handle_command(self, message):
			if message.content.lower() == 'hide win':
				if os.sys.platform == 'win32':
					pg.hotkey("win", 'down')
					pg.hotkey("win", 'down')
				else:
					pg.hotkey('option', 'command', 'm')
			if message.content.lower() == 'close win':
				if os.sys.platform == 'win32':
					pg.hotkey("alt", 'f4')
				else:
					pg.hotkey('option', 'command', 'w')
			if message.content.lower() == 'pause':
				pg.hotkey('space')
		async def on_message(self, message):
			if(message.author == self.user):
				return

			if (finished) or (message.content.lower() == 'stop') or (message.content.lower() == 'off'):
				await self.abort_off()
				
			if (message.content.lower() != 'start'):
				self.handle_command(message)
			else:
				print("Got screenshot")
				img = pg.screenshot() 
				img.save(file_name, "PNG")
				await message.channel.send(file=discord.File(file_name))

bot = Bot()
print("Inited")
bot.run(token)
