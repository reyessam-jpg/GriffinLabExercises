import pandas as pd
import numpy as np

item = ["A","B","C","D","E"]
cost = np.array([0.12, 2.11, 1.96, 0.42, 0.88])
price = np.array([0.45, 8.99, 13.99, 1.99, 1.15])
stock = np.array([452, 9846, 354, 6512, 987])

inv = {
    "Item" : item,
    "Cost" : cost,
    "Price" : price,
    "Stock" : stock
}
invdf = pd.DataFrame(inv)
print(invdf)

sale_val = stock @ price
sv = np.round(sale_val, 2)
cost_tot = stock @ cost
ct = np.round(cost_tot, 2)
profit = sale_val - cost_tot
p = np.round(profit, 2)

print(sv, ct, p, sep="\n")