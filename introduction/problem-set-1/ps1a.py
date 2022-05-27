"""
Solution for problem set 1 part a
https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/mit6_0001f16_ps1/
"""
portion_down_payment = 0.25
current_savings = 0
r = 0.04
print('Enter your annual salary:',end=' ')
annual_salary = float(input())
print('Enter the percent of your salary to save, as a decimal:',end=' ')
portion_saved = float(input())
print('Enter the cost of your dream home:',end=' ')
total_cost = float(input())

down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary/12
total_month = 0
while current_savings<down_payment:
    current_savings+=current_savings*r/12
    current_savings+=monthly_salary*portion_saved
    total_month+=1
print('Number of months:',total_month,end=' ')