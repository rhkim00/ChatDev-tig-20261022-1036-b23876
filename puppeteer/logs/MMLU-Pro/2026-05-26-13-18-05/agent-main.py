def calculate_total_end_tables():
    production_data = [
        {"employees": 8, "end_tables_per_employee": 16},
        {"employees": 21, "end_tables_per_employee": 23},
        {"employees": 7, "end_tables_per_employee": 27},
        {"employees": 4, "end_tables_per_employee": 29}
    ]
    total_end_tables = 0
    for data in production_data:
        total_end_tables += data["employees"] * data["end_tables_per_employee"]
        print("Calculating end tables produced by", data["employees"], "employees at a rate of", data["end_tables_per_employee"], "end tables per employee.")
    return total_end_tables

print("Total end tables produced:", calculate_total_end_tables())