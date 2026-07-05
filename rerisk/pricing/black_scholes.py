# Numpy utilized for logarithms, square roots, and exponential functions
# Scipy.stats for cumulative distribution function
import numpy as np
from scipy.stats import norm


# Computes the price of a European call option using Black-Scholes option model
def black_scholes(stock_price, strike_price, time, rate, vol):
    if(time <= 0 or vol <= 0):
        raise ValueError("Time and Volatility must be > 0")
    
    # d1 is the volatility scaled logarithmic distance between current price and strike price under risk-neutral measure
    # d2 shifts d1 down by one volatility deviation to determine the risk-neutral probability of expiring in the money
    d1 = cd1(stock_price, strike_price, time, rate, vol)
    d2 = cd2(stock_price, strike_price, time, rate, vol)

    # The theoretical call price, calculated by the expected value of acquiring the asset minus the present value of paying the strike price at expiry
    price = (((stock_price * norm.cdf(d1)) - (strike_price * np.exp(-rate * time) * norm.cdf(d2))))

    return price

def cd1(stock_price, strike_price, time, rate, vol):
    return (np.log(stock_price/strike_price) + (rate + 0.5 * (vol ** 2)) * time) / (vol * np.sqrt(time))

def cd2(stock_price, strike_price, time, rate, vol):
    d1 = cd1(stock_price, strike_price, time, rate, vol)
    return (d1 - (vol * np.sqrt(time)))
