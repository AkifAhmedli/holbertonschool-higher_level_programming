#!/usr/bin/env python3
"""Module demonstrating multiple inheritance with Fish and Bird classes."""


class Fish:
    """Parent class representing a fish."""

    def swim(self):
        """Print swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat message."""
        print("The fish lives in water")


class Bird:
    """Parent class representing a bird."""

    def fly(self):
        """Print flying message."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Subclass inheriting from both Fish and Bird."""

    def fly(self):
        """Override the fly method."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override the swim method."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override the habitat method."""
        print("The flying fish lives both in water and the sky!")
