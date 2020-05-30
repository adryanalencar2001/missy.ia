import telegram

class TelegramModule():
	"""docstring for TelegramModule"""
	def __init__(self, missy):
		self.missy = missy
		self.config = self.missy.confmdl.module_config("telegram")
		self.sintaxe = self.missy.sinmdl("null")
		self.bot = telegram.Bot(token=self.config.conf['token'])

		