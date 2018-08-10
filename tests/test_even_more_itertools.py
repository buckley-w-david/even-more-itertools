from even_more_itertools import __version__
from even_more_itertools import HistoricalIterator


def test_version():
    assert __version__ == '0.1.0'

def test_smaller_than_max():
    collection = HistoricalIterator(range(5), memory=10)
    assert list(collection) == [

