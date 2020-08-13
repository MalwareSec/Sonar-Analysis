from src.transformation import Transformation
from src.extraction import Extraction

class Engine:
    def __init__(self, dataSource, dataSet):
        extracted_data = Extraction.extract(dataSet)
        transform = Transformation(dataSource, dataSet)
        transform.transform(extracted_data)