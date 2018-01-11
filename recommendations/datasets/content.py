from datasets.base import Dataset


class NewsDataset(Dataset):
    """
    NewsDataset contains dataset from UCI
    """
    def __init__(self):
        self._name = "UCI News Dataset"
        self._download_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00359/NewsAggregatorDataset.zip"

    def download_post_process(self):
        """
        once the file has been downloaded do the following:

        1. uncompress the file
        """
        pass

    def total_instances(self):
        return 0