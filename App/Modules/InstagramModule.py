from InstagramAPI import InstagramAPI
import json

class InstagramModule():
	
	def __init__(self, missy):
		self.missy	= missy
		self.config = self.missy.confmdl.module_config("instagram")
		self.sintaxe = self.missy.sinmdl("instagram")
		self.api = InstagramAPI(self.config.get_conf("user"), self.config.get_conf("passwd"))
		self.api.login()

	def fun(self):
		self.api.getSelfUserFeed()
		return json.dumps(self.api.LastJson)

	def get_user_profile(self, username):
		self.api.searchUsername(username)
		return json.dumps(self.api.LastJson)

	def buscar_usuario(self):
		self.missy.voicemdl.create_audio("Por favor, digite o nome de usuário:")
		username = str(input("Escrever: "))
		self.api.searchUsername(username)
		info = json.loads(json.dumps(self.api.LastJson))
		try:
			self.api.getUsernameInfo(info['user']['pk'])
			return json.dumps(self.api.LastJson)
		except:
			self.missy.create_audio("usuário não encontrado.")
			pass
		