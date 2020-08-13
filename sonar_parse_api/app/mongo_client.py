from pymongo import MongoClient

class MongoManager:
	__instance = None
	def __init__(self, user, password, host, db_name, port, authSource='admin'):
		self.user = user
		self.password = password
		self.host = host
		self.port = port
		self.db_name = db_name
		self.authSource = authSource
		if MongoManager.__instance != None:
			raise Exception("Error initializing mongo client")
		else:
			self.uri = 'mongodb://' + self.user + ':' + self.password + '@'+ self.host + ':' + self.port + '/' + self.db_name + '?authSource=' + self.authSource
			MongoManager.__instance = MongoClient(self.uri)
	@staticmethod 
	def getInstance(user, password, host, db_name, port, authSource='admin'):
		if MongoManager.__instance == None:
			MongoManager(user, password, host, db_name, port, authSource='admin')
		return MongoManager.__instance
