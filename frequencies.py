"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
def frequencies(items):
    frequencies = {}
    # Your code goes here
    for value in items:
        if not isinstance(value,str):
            value=str(value)
        if not value in frequencies:
            frequencies[f'{value}']=1
        else:
            frequencies[f'{value}']=frequencies[f'{value}']+1
    return frequencies
