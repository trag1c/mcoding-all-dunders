class Appliance:
    """
    An Appliance object can be either on and off.

    A call to the object will result in switching the state 
    of the Appliance object. 
    
    """
    def __init__(self, name:str, is_on:bool = False) -> None:
        """Initialize the Appliance object
        
        name: str
            Name of the Appliance

        is_on: bool = False
            Initial state of the Appliance
        """

        self.name = name
        self.state = is_on
        
    def switch(self):
        """Switch the state of the Appliance """
        self.state = not(self.state)

    def status(self) -> str:
        """Return a message with current status of the Appliance"""
        message = "ON" if self.state else "OFF"
        return f"\tThe {self.name} is {message}"  

    def __call__(self) -> str:
        """Switch the state of the Appliance and return it's status"""

        # Switch the appliance state
        self.switch()

        # Returns a message with the status
        return self.status() + "\t(from __call__)"
    
    def __repr__(self) -> str:
        return self.status() + "\t(from __repr__)"

def main():

    # Initialize the appliances
    tv = Appliance("room TV")
    pc = Appliance("office PC", is_on=True)

    print("*** TV ***")
    print(f"{tv =:}")      # __repr__
    print(f"{tv() =:} ")   # __call__
    print(f"{tv() =:} ")   # __call__
    print(f"{tv() =:} ")   # __call__

    print("\n*** PC ***")
    print(f"{pc =:}")      # __repr__
    print(f"{pc() =:} ")   # __call__


if __name__ == "__main__":
    main()