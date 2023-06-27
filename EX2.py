reg_hours = 40
reg_rate = 18.25
ov_rate = 27.78

workhours = int(input('Enter your work hours: '))
print(workhours)

regular_wage = reg_hours * reg_rate

if workhours <= 40:
    print('Total Wages:',workhours * reg_rate)
    

if workhours > 40:
    overtime_hours = workhours - 40
    overtime_wage = overtime_hours * ov_rate
    print('Regular Charge:',40 * reg_rate)
    print('Overtime Charge:',overtime_wage)
    print('Total Wages;',overtime_wage + regular_wage)

