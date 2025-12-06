#!/usr/bin/env python3
"""
polymorphism_demo.py
Demonstrates polymorphism and method overriding with Shape, Rectangle, and Circle classes.
"""
import math

class Shape:
    """Base class for all geometric shapes."""
    def area(self):
        """
        Base method for area calculation. Must be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must override the area() method.")

class Rectangle(Shape):
    """Represents a rectangle, inheriting from Shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Overrides area() to calculate the rectangle's area."""
        return self.length * self.width

class Circle(Shape):
    """Represents a circle, inheriting from Shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Overrides area() to calculate the circle's area (π * radius²)."""
        return math.pi * (self.radius ** 2)

# The provided main.py script will demonstrate the polymorphic behavior