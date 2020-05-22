cp=float(input("Enter Cost Price of product: "))
sp=float(input("Enter Selling Price of product: "))
profit=sp-cp
newsp=sp+(0.05*profit)
print("Profit from this sell:",profit)
print("To increase profit by 5% the selling price should be:",newsp)
