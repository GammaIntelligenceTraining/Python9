from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['Names', 'Age', 'City']
table.add_row(["Алекс", 20, "Москва"])
table.add_row(["Боб", 25, "Москва"])
table.add_row(["Саша", 30, "Минск"])
table.add_row(["Петя", 23, "Киев"])
table.add_row(["Вася", 67, "Москва"])

table.align = 'l'
table.sortby = "City"
print(table)