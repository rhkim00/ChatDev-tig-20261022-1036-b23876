def calculate_reconciliation_statement(statement_balance, checkbook_balance, missing_checks, service_charge):
    # Calculate the total of missing checks
    total_missing_checks = sum(missing_checks)
    print('Total of Missing Checks: $', round(total_missing_checks, 2))

    # Calculate the reconciliation statement balance
    reconciliation_balance = statement_balance + total_missing_checks - service_charge

    return reconciliation_balance

# Define the given values
statement_balance = 1810.50
checkbook_balance = 1685.75
missing_checks = [60.80, 40.30, 25.00]
service_charge = 1.35

# Calculate the reconciliation statement balance
reconciliation_balance = calculate_reconciliation_statement(statement_balance, checkbook_balance, missing_checks, service_charge)

print('Reconciliation Balance Calculation:')
print('Statement Balance: $', round(statement_balance, 2))
print('Checkbook Balance: $', round(checkbook_balance, 2))
print('Service Charge: $', round(service_charge, 2))
print('Reconciliation Balance = Statement Balance + Total Missing Checks - Service Charge')
print('Reconciliation Statement Balance: $', round(reconciliation_balance, 2))