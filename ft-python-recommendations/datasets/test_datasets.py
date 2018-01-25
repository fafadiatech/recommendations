from datasets.content import NewsDataset
from datasets.collaborative import ML100K

def test_news_dataset_download():
    dataset = NewsDataset()
    assert dataset is not None

    dataset.download_and_unzip()
    dataset.download_post_process()

    assert dataset.total_instances() != 0
    assert dataset.total_instances() == 422418

def test_ml100k_dataset_download_non_test_mode():
    dataset = ML100K(mode="prod")
    assert dataset is not None

    dataset.download_and_unzip()
    dataset.download_post_process()

    assert dataset.total_instances() != 0
    assert dataset.total_instances() == 100000

def test_ml100k_dataset_download_test_mode():
    dataset = ML100K()
    assert dataset is not None

    dataset.download_and_unzip()
    dataset.download_post_process()

    assert dataset.total_instances() != 0
    assert dataset.total_instances() == (90570, 9430)