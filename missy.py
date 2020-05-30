from Core.System.Modules.LoadModule import LoadModule
from Core.System.Modules.ConfigModule import ConfigModule
from Core.System.Modules.VoiceModule import VoiceModule
from Core.System.Modules.SintaxeModule import SintaxeModule
from Core.System.Modules.NLTKModule import NLTKModule

class Missy():

	def __init__(self):
		self.confmdl = ConfigModule()
		self.loadmdl = LoadModule(self.confmdl, self)
		self.usermodules = None
		self.sinmdl = SintaxeModule
		self.voicemdl = VoiceModule(self.confmdl)


	def load_app(self):
		self.usermodules = self.loadmdl.load_all_modules()
		for key in self.usermodules:
			exec("self."+str(key)+" = self.usermodules['"+str(key)+"'](self)")
		temp = []
		for key in self.usermodules:
			exec("temp.append(self."+str(key)+")")

		self.usermodules = temp	
		self.nltkmdl = NLTKModule(self)

	def add_module(self):
		pass

if __name__ == "__main__":
	missy = Missy()
	missy.load_app()
	while True:
		error, phrase = missy.voicemdl.hear_mic()
		#error, phrase = False, str(input("Entrada:"))
		if error:
			missy.voicemdl.create_audio(phrase)
		else:
			error, ret = missy.nltkmdl.call(phrase)
			if error:
				missy.voicemdl.create_audio(ret)
			else:
				print(ret)


# x='buffalo'    
# exec("%s = %d" % (x,2))
