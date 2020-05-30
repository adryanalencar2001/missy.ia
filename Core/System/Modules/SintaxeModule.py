import json

class SintaxeModule(object):

	def __init__(self, sintaxe_file=""):
		self.sintaxe_file = sintaxe_file
		self.sintaxe_data = json.loads(open("App/Sintaxe/"+str(sintaxe_file)+".json").read())

	def get_object_name(self):
		return [self.sintaxe_data["object"]]

	def get_function_activate(self):
		return [self.sintaxe_data["methods"]]


# [('testando', 'NN'), ('o', 'MD'), ('reconhecimento', 'VB'), ('de', 'FW'), ('voz', 'FW')]
# [('Nice', 'NNP'), ('Acender', 'NNP'), ('luz', 'NN')]
# [('Acender', 'NNP'), ('luz', 'NN'), ('do', 'VBP'), ('corredor', 'NN')]
# [('apagar', 'NN'), ('luz', 'NN'), ('do', 'VBP'), ('corredor', 'NN')]
# [('Enviar', 'NNP'), ('mensagem', 'NN'), ('para', 'NN'), ('Alisson', 'NNP')]
# [('Enviar', 'NNP'), ('mensagem', 'NN'), ('para', 'NN'), ('Wesley', 'NNP')]
# [('apagar', 'NN'), ('luz', 'NN'), ('do', 'VBP'), ('corredor', 'NN')]
# [('ligar', 'NN'), ('televisão', 'NN')]
# [('desligar', 'NN'), ('televisão', 'NN')]
# [('positivo', 'NN')]
# [('listar', 'NN'), ('dispositivos', 'NN')]
# [('categorizar', 'NN'), ('minha', 'NN'), ('fala', 'NN')]
# [('Ligar', 'NNP'), ('para', 'NN'), ('mamãe', 'NN')]
# [('selfie', 'NN'), ('no', 'DT'), ('Instagram', 'NNP')]
# [('ligar', 'NN'), ('do', 'VBP'), ('celular', 'JJ'), ('para', 'NN'), ('mamãe', 'NN')]
# [('telegram', 'NN'), ('para', 'NN'), ('mamãe', 'NN')]
# [('ligar', 'NN'), ('do', 'VBP'), ('telegram', 'VB'), ('para', 'NN'), ('mamãe', 'NN')]
# [('dispositivos', 'NN'), ('em', 'NN'), ('casa', 'NN')]
# [('listar', 'NN'), ('dispositivos', 'NN'), ('em', 'NN'), ('casa', 'NN')]