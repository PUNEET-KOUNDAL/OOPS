#class
class employees :
    # special method/magical method or / dunder method =  constructor 
    def __init__(self) :
        #data or attribute 
        self.id = 0 
        self.salay =0 
        self.designation = 'sde'

    #method 
    def travel(self,destination) :
        print(f"employee is now travelling to {destination}")


# object or instance
sam = employees ()
sam.id= 9


#printing attribute
print(sam.id)

#printing method
print(sam.travel('kerala'))

