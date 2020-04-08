"""
Oppgave 7.1 - Planet-klasse
Author: Mohammed Shartaz Mostafa
"""
from math import pi

class Planet(object):  # Defining a class
    def __init__(self, name, radius, mass):  # Magic method, initializes the variables within its scope
        self.name = name
        self.radius = radius
        self.mass = mass

    def density(self):  # Defining a method
        return self.mass/(4/3*pi*self.radius**3)  # Returns the density
    
    def print_info(self):
        # Using string formatting to print the desired information
        print("Name:      {:s}".format(self.name)) 
        print("Radius:    {:g}".format(self.radius))
        print("Mass:      {:g}".format(self.mass))
        print("Density:   {:g}".format(self.density()))

planet1 = Planet("Earth",6371E3, 5.972E24)  # An instance of the Planet class
planet1.population = 7497486172  # Creating an attribute to the instance 

print(planet1.name, "has a population of ", planet1.population)

"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig9>python Planet.py
Earth has a population of  7497486172
"""
