class Extraction:
    @staticmethod
    def extract(dataSet):
        return open(dataSet["source"], encoding="utf8")