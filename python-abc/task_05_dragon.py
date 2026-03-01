#!/usr/bin/env python3
"""Module demonstrating the use of Mixins for shared functionality."""


class SwimMixin:
    """Mixin to provide swimming functionality."""

    def swim(self):
        """Print a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin to provide flying functionality."""

    def fly(self):
        """Print a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon class that combines swimming and flying capabilities."""

    def roar(self):
        """Print a roaring message unique to the Dragon."""
        print("The dragon roars!")
