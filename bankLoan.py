def eligibility(sal,age,credit_score):
    reason=""
    if sal >= 25000 and age >=18 and age <=35 and credit_score >=750:
        return "Eligible"
    if sal < 25000:
        reason += ("Salary is less than 25000")
    if age < 18 or age > 35:
        reason += ("age is not between 18 and 35")
    if credit_score < 750:
        reason += ("credit score is less than 750")
    return reason

def get_input():
    sal = int(input("enter sal"))
    age = int(input("enter age"))
    credit = int(input("enter credit"))
    return sal,age,credit
    
def main():
    sal,age,credit = get_input()
    print(eligibility(sal,age,credit))
    
main()