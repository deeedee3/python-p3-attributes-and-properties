#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def _init_(self, name= "Unknown", breed="Mutt"):
        self.name = name
        self.breed = breed
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value  
        else:
            print("Name must be string between 1 and 25 characters.")
   
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        self._breed = value