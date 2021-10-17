#Calculating Kinetic Energy(E) given Mass(m) and Velocity (v)
#E = 1/2*m*v**2

def Kinetic_Energy():

    print("Calculating Kinetic Energy of an object given the mass ")
    print("of the object and thevelocity at which the object is moving.")
    print()
    print("E=1/2(MV^2)")
    
    print()
    print()

    mass=eval(input("The mass of an object is:"))
    print()
    velocity=eval(input("The object is moving at a velocity of:"))
    print()
    Energy=(1/2*mass*velocity**2)
    print()
    print("Enery",Energy,"joules")

Kinetic_Energy()
            
