import unittest, json
from src.transformation import Transformation

data_source = {
		"username": "root",
		"password": "root",
		"host": "mongodb",
		"db": "sonar",
		"port": "27017",
		"source": "src/data/dataset.json"
	}

extracted_data = {
		"data": "test",
		"host": "45.60.10.105",
		"ip": "45.60.10.105",
		"path": "/",
		"port": "30443",
		"subject": {
			"C": "US",
			"ST": "Delaware",
			"CN": "test.incapsula.com",
			"O": "Incapsula Inc",
			"L": "Dover"
		},
		"vhost": "45.60.10.105"
	}

class TestTransform(unittest.TestCase):

	def test_transform_pre(self):
		transform = Transformation("mongo", data_source)
		self.assertFalse(transform.transformed, "Expected Transformation to be False")

if __name__ == '__main__':
	unittest.main()