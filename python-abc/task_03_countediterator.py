#!/usr/bin/env python3
"""Module defining an iterator that counts its iterations."""


class CountedIterator:
    """An iterator wrapper that keeps track of the number of items fetched."""

    def __init__(self, iterable):
        """Initialize the iterator and the counter.

        Args:
            iterable: Any object that can be converted into an iterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the current number of items that have been iterated."""
        return self.count

    def __next__(self):
        """Fetch the next item and increment the counter.

        Raises:
            StopIteration: If there are no more items to fetch.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Ensure the CountedIterator itself is an iterable."""
        return self
