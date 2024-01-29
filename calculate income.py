income = int(input('Taxable income:'))
tax_payable = 0


if income <= 10000:
    tax_payable= 0

elif income <= 20000:
    remain = income - 10000
    tax_payable = remain * 10 / 100
