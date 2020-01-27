#!/usr/bin/python3
"""
comment
"""


class Base:
    """Class Base"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """function comments"""
        if id != None: 
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects
           
        
        
    
    
