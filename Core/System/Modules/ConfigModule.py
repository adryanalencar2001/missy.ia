import json

class ConfigModule():
	
	"""ConfigModule response system configs"""	
	def __init__(self, path="App/Config/Conf.json"):
		self.path = path
		self.json_file = open(self.path)
		self.conf = json.loads(self.json_file.read())

	def sintax_config(self, file):
		return ConfigModule("App/Sintaxe/"+str(file)+".json")

	def module_config(self, file):
		return ConfigModule("App/Config/Module/"+str(file)+".json")

	def get_conf(self, key):
		return self.conf[key]

	def set_conf_val(self, key, val):
		self.conf[key] = val;
		temp = open(self.path,"w")
		temp.write(json.dumps(self.conf))

		return True