import json
import os
import ast

class LoadModule():
	"""docstring for LoadModule"""
	
	def __init__(self, config, Missy):
		self.config = config.conf
		self.Missy = Missy

	def load_all_modules(self):
		files = os.listdir(self.config["app_modules_path"])
		temp = []

		self.verify_path()

		for file in files:
			if file.find(".py") > -1:
				parsed = ast.parse(open(self.config['app_modules_path']+str(file)).read())
				classes = [node.name for node in ast.walk(parsed) if isinstance(node, ast.ClassDef)]
				temp.append([str(self.config['app_modules_path']).replace("/",".")+file.replace(".py",""),classes])

		files = temp
		objs = {}


		for package in files:
			mod = __import__(package[0], fromlist=package[1])
			for obj in package[1]:				
				objs[obj] = getattr(mod, obj)

		return objs

	def load_module(self, path, cls):
		mod = __import__(path.replace("/","."), fromlist=[cls])
		mod = getattr(mod, obj)
		self.Missy.add_module(mod, cls)

		return mod

	def verify_path(self):
		if self.config["app_modules_path"][len(self.config["app_modules_path"])-1] != '/':
			self.config["app_modules_path"] += '/'