#!/usr/bin/env python3
"""Illustrates the difference between @classmethod and @staticmethod."""

class Calculator:
    """A class using static and class methods for arithmetic."""
    
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static Method: Performs addition without access to self or cls."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class Method: Performs multiplication with access to the class (cls)."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b