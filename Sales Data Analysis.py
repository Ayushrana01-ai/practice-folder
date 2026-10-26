
# Sales Data Analysis Project

products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse"]
sales = [30000, 50000, 500, 300, 1500]

total_sales = sum(sales)
average_sales = total_sales / len(sales)
highest_sale = max(sales)

best_index = sales.index(highest_sale)
best_product = products[best_index]

print("SALES DATA ANALYSIS")
print("-------------------")

for i in range(len(products)):
    print(products[i], ":", "₹", sales[i])

print("-------------------")
print("Total Sales: ₹", total_sales)
print("Average Sales: ₹", round(average_sales, 2))
print("Highest Sale: ₹", highest_sale)
print("Best-Selling Product:", best_product)
