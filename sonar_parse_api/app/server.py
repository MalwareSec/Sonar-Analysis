from app.base_handler import BaseHandler
from pymongo import MongoClient
import json
import ast 

class HealthCheck(BaseHandler):
	def initialize(self, objApi):
		self.objApi = objApi

	def get(self):
		self.write({'response': '200 OK!'})

class GetRecords(BaseHandler):
	def initialize(self, objApi):
		self.objApi = objApi

	def mongo_client(self, config):
		uri = 'mongodb://' + config["username"] + ':' + config["password"] + '@'+ config["mongo_url"] + ':' + config["mongo_port"] + '/' + config["db"] + '?authSource=admin'
		client = MongoClient(uri)
		return client.sonar

	def post(self):
		if (self.request.body):
			records_list = []
			data = json.loads(self.request.body)
			search = data["search"]
			db = self.mongo_client(self.objApi["config"])
			records_query = db["Sonar_Records"].find({'subject.CN':{'$regex': search}})
			for record in records_query:
				record_dict = {}
				record_dict["ip_address"] = record["ip"]
				record_dict["port"] = record["port"]
				record_dict["host"] = record["host"]
				record_dict["vhost"] = record["vhost"]
				record_dict["organizational_unit"] = record.get('subject', {}).get('O', {})
				record_dict["common_name"] = record["subject"]["CN"]
				records_list.append(record_dict)
			
			self.set_status(200)
			self.write({"Records": records_list})
