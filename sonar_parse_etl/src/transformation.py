from src.mongo_client import MongoDB
import json
import pandas as pd

class Transformation:
    def __init__(self, dataSource, dataSet):
        self.data = dataSet
        self.client = MongoDB(
            dataSet["username"], 
            dataSet["password"],
            dataSet["host"],
            dataSet["db"],
            dataSet["port"]
        )
        self.transformed = False
        
    def transform(self, dataset_records):
        dataset_records_list = []
        for data in dataset_records:
            json_data = json.loads(data)
            dataset_records_list.append(json_data)
        df = pd.DataFrame(dataset_records_list, columns=json_data.keys())
        if not df.empty:
            self.transformed = True
            self.client.insert_into_db(df, 'Sonar_Records')


