#!/usr/bin/env python3
"""Module defining a VerboseList that notifies on modifications."""


class VerboseList(list):
    """A list subclass that prints messages when modified."""

    def append(self, item):
        """Add an item and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print the count of items added."""
        items_added = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(items_added))

    def remove(self, item):
        """Print notification before removing an item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Print notification before popping an item."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
