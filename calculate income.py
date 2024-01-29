income = int(input('Taxable income:'))
tax_payable = 0


if income <= 10000:
    tax_payable= 0

elif income <= 20000:
    remain = income - 10000
    tax_payable = remain * 10 / 100
else:
    tax_payable = 0
    tax_payable = 10000 * 10 / 100
    tax_payable += (income - 20000) * 20 / 100

print('Tax payable is:', tax_payable)