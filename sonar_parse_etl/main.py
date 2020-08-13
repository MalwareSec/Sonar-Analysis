from src.engine import Engine
import json
        
if __name__ == '__main__':
    etl_data = json.load(open('src/data/data_config.json'))
    for dataSource, dataSet in etl_data['data_sources'].items():
        main_obj = Engine(dataSource, dataSet)