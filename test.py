from rerisk.pricing.black_scholes import black_scholes

# Black-Scholes test 
price = black_scholes(500, 500, 1, 0.05, 0.5)
print("Option price: ", price)