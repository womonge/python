#Exams
# midterm=x
# endterm =y
# final= 0.4(x)+0.6(y)

def main():
    midterm = eval(input("what is your midterm score?"))
    endterm = eval(input("what is your endterm score?"))
    final= (0.4*midterm)+ (0.6*endterm)
    print("the final score is ",final," %.")


main()


#Calculating final from the values of x,y, and z

def main():
    x=eval(input("What is the value of x?"))
    y=eval(input("What is the value of y?"))
    z=eval(input("What is the value of z?"))
    final=(x**3+x*(y+z)+y**3+z)
    print("The answer is",final,"")

main()



#Calculating the commission given the merchant turnover


def main():
    turnover=eval(input("What is the merchant turnover"))
    commission=(turnover*0.25)
    print("The commission is",commission,"in Kenya Shilings")

main()


#The number of Girls,Women and Men, given the number of Boys

def main():
    Boys=eval(input("What is the number of Boys?"))
    Girls=(Boys*0.45)
    Women=((Boys+Girls)*0.25)
    Men=(Women*1.25)
    print("The number of Girls is",Girls,"")
    print("The number of Women is",Women,"")
    print("The number of Men is",Men,"")

main()

#CALCULATING VELOCITY AND DISPLACEMENT

#v=u+(a*t**2)
#s=u*t+(0.5*a*t**2)
#a=(v**2-u**2/(2*s)
#v=velocity
#u=intial_velocity
#a=acceleration
#s=displacement
#t=time

def main():
    u=eval(input("Initial_velocity="))
    t=eval(input("time_traveled="))
    v=eval(input("velocity="))
    s=eval(input("displacement="))
    a=eval(input("acceleration="))
    velocity=(u+(a*t**2))
    displacement=(u*t+(0.5*a*t**2))
    acceleration=(v**2-u**2/(2*s))
    print("velocity is",velocity,"m/s")
    print("displacement is",displacement,"m")
    print("acceleration is",acceleration,"m/s**2")

main()
    



