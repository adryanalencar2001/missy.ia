import nltk

class NLTKModule():
	def __init__(self, missy):
		self.objs = missy.usermodules

	def call(self, phrase):
		runners = {}
		phrase = str(phrase).lower()
		"""
		{ "obj":{
				"points":"int",
				"function":"fun"		
			}
		}

		"""
		for obj in self.objs:
			p=0
			for name in obj.sintaxe.get_object_name()[0]:
				if name in phrase:				
					p+=1
					pf=0 
					f = None
					for fun in obj.sintaxe.get_function_activate()[0]:
						pw = 0
						for word in obj.sintaxe.get_function_activate()[0][fun]:
							if word in phrase:
								pw+=1

						if pw > pf:
							f = fun
							pf = pw

					runners[obj] = {
						"points":pf,
						"function":f
					}
		print(runners)
		win=[0,0,0]
		for obj in runners:
			if runners[obj]["points"] > win[2]:
				win = [obj, runners[obj]["points"], runners[obj]["function"]]

		if win == [0,0,0]:
			return True, "Nenhum módulo encontrado"

		result = getattr(win[0], win[2])()

		return False, result
		#text = nltk.word_tokenize (phrase)
		#nltk.pos_tag(text)
