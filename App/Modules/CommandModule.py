import os

class CommandModule():
	"""docstring for ClassName"""
	def __init__(self, missy):
		self.missy = missy
		self.config = self.missy.confmdl.module_config("command")
		self.sintaxe = self.missy.sinmdl("command")

	def exec(self):
		self.missy.voicemdl.create_audio("Diga o comando")
		erro, phrase = self.missy.voicemdl.hear_mic()
		if erro:
			self.missy.voicemdl.create_audio(phrase)
		else:
			phrase = phrase.lower()
			print(phrase)
			if phrase == "ubs":
				phrase = phrase.replace("u","o")
			elif phrase == "desligar":
				phrase = "shutdown now"
			elif phrase == "parar":
				os.system("killall -9 python3")

			if str(phrase) in self.config.conf["allowed_commands"]:
				os.system(str(phrase)+" & exit")
			else:
				self.missy.voicemdl.create_audio("Comando não permitido.")
