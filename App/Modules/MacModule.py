import json
import serial
import time

class MacModule():
	"""docstring for MacModule"""
	def __init__(self, missy):
		self.missy	= missy
		self.config = self.missy.confmdl.module_config("macsniffer")
		self.sintaxe = self.missy.sinmdl("macsniffer")
		self.serial = serial.Serial(self.config.conf["port"], self.config.conf["boundrate"], timeout = 1)

	def get_instagram(self):
		address = []
		now = time.time()
		timeout = now + self.config.conf["timeout"]
		while time.time() < timeout:
			try:
				readOut = json.loads(self.serial.readline().decode('utf-8'))
				print("MAC: "+readOut['source']+" Signal: "+str(readOut['RSSI']))
				if readOut['source'] in self.config.conf["maclist"] and not readOut['source'] in address:
					address.append(readOut['source'])
			except Exception as e:
				print(e)
				pass

		self.serial.flush() #flush the buffer
		profiles = {}
		print(address)
		for mac in address:
			temp = json.loads(self.missy.InstagramModule.get_user_profile(self.config.conf['maclist'][mac]))
			telegramcnf = self.missy.TelegramModule.config
			self.missy.TelegramModule.bot.send_photo(telegramcnf.conf['update_id_owner'], temp['user']['profile_pic_url'], caption=temp['user']['full_name'])
