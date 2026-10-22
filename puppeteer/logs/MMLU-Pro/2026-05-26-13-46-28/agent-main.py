from fractions import Fraction

high_price = '19(3/8)'
low_price = '18(3/4)'

high_fraction = Fraction(high_price.replace('(', '').replace(')', '').replace('/', '.'))
low_fraction = Fraction(low_price.replace('(', '').replace(')', '').replace('/', '.'))

average_price = (high_fraction.numerator * low_fraction.denominator + low_fraction.numerator * high_fraction.denominator) / (2 * high_fraction.numerator * low_fraction.denominator)
option_price = average_price * 0.95

print('High Price Fraction:', high_fraction)
print('Low Price Fraction:', low_fraction)
print('Average Price:', average_price)
print('Option Price is: $', round(option_price, 6))