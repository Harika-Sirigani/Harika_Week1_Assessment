import math
def get_input():
    weight= float(input("enter weight :"))
    height =float(input("enter height : "))
    return round((weight/height**2),2)

def BMI_calculator(bmi):
    if bmi <18:    
        print ("underweight")
    elif bmi<25:
        print("Normal")
    elif bmi<30:
        print("Overweight")
    else:
        print("obese")
        
def main():
    weight,height = get_input()
    bmi = weight,height
    print(BMI_calculator(bmi))
    
main()