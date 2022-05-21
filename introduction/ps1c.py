print('Enter your annual salary:',end=' ')
initial_annual_salary = float(input())

portion_down_payment = 0.25
current_savings = 0
r = 0.04
total_cost = 1000000
semi_annual_raise = 0.07
total_month = 36

down_payment = total_cost * portion_down_payment
monthly_salary = initial_annual_salary/12
current_month = 0
annual_salary = initial_annual_salary
portion_saved_int_min = 0
portion_saved_int_max = 10000
portion_found = False
bisection_step = 1

while current_month<total_month:
    portion_saved_int = (portion_saved_int_min+portion_saved_int_max)//2
    while current_savings<down_payment:
        current_savings+=current_savings*r/12
        current_savings+=monthly_salary*float(portion_saved_int/10000)
        current_month+=1
        if current_month%6==0:
            annual_salary+=annual_salary*semi_annual_raise
            monthly_salary = annual_salary/12
    if current_month+1==total_month:
        portion_found = True
        break
    annual_salary = initial_annual_salary
    monthly_salary = initial_annual_salary/12
    if current_month<total_month:
        portion_saved_int_max = portion_saved_int
    elif current_month>total_month:
        portion_saved_int_min = portion_saved_int
    if portion_saved_int_max == portion_saved_int_min:
        break
    if portion_saved_int_min>=portion_saved_int_max-1:
        break
    current_month = 0
    current_savings = 0
    bisection_step +=1

if portion_found:
    print('Best savings rate:',float(portion_saved_int/10000))
    print('Steps in bisection search:',bisection_step)
else:
    print('It is not possible to pay the down payment in three years.')
