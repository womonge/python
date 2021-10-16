#QUADRATIC EQUATION FORMULA

#ax**2 + bx +c=0

#x= (-b+√(b^2–4ac))/2a and x = (-b-√(b^2–4ac))/2a


def main():

    a=eval(input("What is the value of a?"))
    b=eval(input("What is the value of b?"))
    c=eval(input("What is the value of c?"))

    x1=(-b+((b**2)-(4*a*c))**0.5)/2*a
    x2=(-b-((b**2)-(4*a*c))**0.5)/2*a

    print("x=",x1,"")
    print("x=",x2,"")

main()    
    
