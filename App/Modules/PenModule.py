class PenModule():
	"""docstring for PenModule"""
	def __init__(self, missy):
		self.missy = missy
		self.sintaxe = self.missy.sinmdl("caneta")
		pass

	def escrever(self):
		self.missy.voicemdl.create_audio("Diga o que quer escrever")
		erro, phrase = self.missy.voicemdl.hear_mic()
		if erro:
			self.missy.voicemdl.create_audio(phrase)
		else:
			print(phrase)