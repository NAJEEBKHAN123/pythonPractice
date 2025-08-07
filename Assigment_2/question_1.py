# 1. Write a python program to convert USD to PKR
# Use Case: Useful for travelers & finance applications.
# Input: value (USD $)
# Output: converted value (PKR)


usd_to_pkr = 283

take_amount_in_usd = float(input("Convert USD into PKR: "))

pkr_amount = take_amount_in_usd * usd_to_pkr

print(f"{take_amount_in_usd} USD is equal to {pkr_amount} PKR")