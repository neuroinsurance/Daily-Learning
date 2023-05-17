from random import randint

#collect information on type of company
user = input("what does your company do? ")
company_type = input("is your company going to be a holding company? ")
revenue = input("what is your annual revenue in thousands? ")

#change name of company to reflect if its operational or holding company
if company_type == "yes":
    holding_company = str(" Holdings.ltd")
    print(f"Your companies name is {user + holding_company}")
    user_name = user + holding_company 
else:
    operating_company = str("Operations.ltd")
    print(f"Your companies name is {user + operating_company}")
    user_name = user + operating_company
print(user_name)

#randomly try and predict their revenues
num = randint(1,3)
if str(num) == revenue:
    print(f"Your company {user_name} generates {str(num)}k in revenue per year! We gussed correctly!!")
else:
    print(f"We guessed wrong and thought your company made {num}k in revenue. But it really made {revenue}k. We will do better next time... hopefully.")



