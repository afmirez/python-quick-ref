# Object Oriented Programming
# Programming paradigm that structures software around entities (objects) that 
# encapsulate both state (data, attributes) and behavior (methods, functions) 
# under a well-defined interface.

# Abstraction: Define relevant features while hiding implementation details.
# Encapsulation: Bundling data and methods in one object while restricting 
#                external access to protect and maintain its internal state.
# Inheritance: Mechanism for a class (subclass) to reuse and extend the 
#              behavior/structure of another class (superclass).
# Polymorphism: Ability for the same message (method call) to trigger different 
#               behaviors depending on the receiving object.


#------------------------------------------------------------------------------#
# Built-in decorators 
# Built-in decorators for classes that adjust method/attribute behavior:

# - @staticmethod: Defines a method bound to the class, not its instance.
class NinjaTools:
    @staticmethod
    def kunai_count(a, b):
        return a + b
res = NinjaTools.kunai_count(5, 3)

# - @classmethod: Defines a method bound to the class, receiving cls as first arg.
class Ninja:
    village = "Konoha"

    @classmethod
    def from_name(cls, name):
        return cls(name)

    def __init__(self, name):
        self.name = name
naruto = Ninja.from_name("Naruto")
print(naruto.name, naruto.village) 

# - @property: Turns a method into a read-only attribute (can add setter/deleter).
class Ninja:
    def __init__(self, name, missions):
        self.name = name
        self._missions = missions

    @property
    def rank(self):
        return "Genin" if self._missions < 10 else "Chunin"

naruto = Ninja("Naruto", 7)
print(naruto.name, naruto.rank)

#------------------------------------------------------------------------------#
# *** CLASS ***
# Classes are blueprints for creating objects. A class defines a set of attributes 
# and methods that the created objects (instances) can have.

# NOTE: Python has no real access modifiers, only conventions:
#   public: attribute
#   protected: _attribute
#   private: __attribute (name mangling)

class Pirate:
    specie = "Human" # Class attribute. Shared across all instances of the class.

    # The constructor `__init__` initializes the instance attributes.
    # `self` refers to the current instance, giving access to its attributes and methods.
    def __init__(self, name, age, bounty):
        self.name = name
        self._age = age     
         self.__bounty = bounty 
    
    def introduce(self):
        return f"I am {self.name}, {self.age} years old, with a bounty of {self.bounty}."

    def __str__(self):
        # Defines the human-readable string representation of the object.
        return f"Pirate(name={self.name}, age={self._age}, bounty={self.__bounty})"

    @property
    def bounty(self):
        return self.__bounty 
    
    @bounty.setter
    def bounty(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Bounty must be a non-negative integer")
        self.__bounty = value
    
    @classmethod
    def get_specie(cls):
        return cls.specie

    @abstractmethod
    def role(self):
        """This method must be implemented by subclasses to define the pirate's role."""
        pass

    


# A class can inherit from one or multiple classes (single or multiple inheritance).
class Captain(Pirate):
    def __init__(self, name, age, bounty, crew_size):
        super().__init__(name,age,bounty) # Calls the parent class constructor
        self.crew_size = crew_size

    def introduce(self):
        # Polymorphism: same method name but different behavior in the subclass.
        return f"""I am Captain {self.name}, leader of a crew of {self.crew_size}, 
                with a bounty of {self.bounty}."""
    
    def role(self):
        return "Captain - responsible for leading the crew and making strategic decisions."

#------------------------------------------------------------------------------#
# *** OBJECTS ***
# Class instance that stores its own data.

# Object instantiation
luffy = Pirate("Monkey D. Luffy", 19, "1,500,000,000")
print(luffy.bounty)   # Calls the @property getter
luffy.bounty = "2,500,000,000" # Calls the setter

