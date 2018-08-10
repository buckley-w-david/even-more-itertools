from collections import deque

__version__ = '0.1.0'

class HistoricalIterator(deque):
    def __init__(self, iterator, maxlen=10):
        super().__init__(maxlen=maxlen)
        self._iter = iterator

    def __iter__(self):
        return self

    def __next__(self):
        result = next(self._iter)
        self.append(result)
        return result

    def __repr__(self):
        return f'HistoricalIterator({self._iter}, maxlen={self.maxlen})'
