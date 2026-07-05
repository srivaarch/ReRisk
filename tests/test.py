from rerisk.pricing.black_scholes import black_scholes
from rerisk.pricing.greeks import delta, gamma, vega, theta, rho

stock_price = 500
strike_price = 500
time = 1
rate = 0.05
vol = 0.5

# Black-Scholes test 
print("Option price: ", black_scholes(stock_price, strike_price, time, rate, vol))

# Greeks test
print("Delta: ", delta(stock_price, strike_price, time, rate, vol))
print("Gamma: ", gamma(stock_price, strike_price, time, rate, vol))
print("Vega: ", vega(stock_price, strike_price, time, rate, vol))
print("Theta: ", theta(stock_price, strike_price, time, rate, vol))
print("Rho: ", rho(stock_price, strike_price, time, rate, vol))

