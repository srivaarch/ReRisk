# Numpy for sqrt & exp
# Scipy for probability density function
import numpy as np
from scipy.stats import norm

# cd1 and cd2 functions from black_scholes for calculation
from rerisk.pricing.black_scholes import cd1, cd2

# Delta is the sensitivity of an option price to the stock price. 
# A 0.5 delta means that for every $1 the stock price goes up, the option price is expected to move $0.50.
def delta(stock_price, strike_price, time, rate, vol):
    d1 = cd1(stock_price, strike_price, time, rate, vol)
    return norm.cdf(d1)

# Gamma is the sensitivity of delta to the stock price, measuring how quickly delta changes as the stock price changes.
def gamma(stock_price, strike_price, time, rate, vol):
    d1 = cd1(stock_price, strike_price, time, rate, vol)
    return (norm.pdf(d1) / (stock_price * vol * np.sqrt(time)))

# Vega is the sensitivity of the option price to the volatility, measuring how quickly the option value changes when IV changes.
# A higher Vega means the option is more sensitive to price changes.
def vega(stock_price, strike_price, time, rate, vol):
    d1 = cd1(stock_price, strike_price, time, rate, vol)
    return (stock_price * norm.pdf(d1) * np.sqrt(time))

# Theta is the sensitivity of the option price to time, measuring how the option value changes as it reaches time-to-expiry.
# Typically a negative value to reflect 'time decay'.
def theta(stock_price, strike_price, time, rate, vol):
    d1 = cd1(stock_price, strike_price, time, rate, vol)
    d2 = cd2(stock_price, strike_price, time, rate, vol)

    first_term = ((-stock_price * norm.pdf(d1) * vol) / (2 * np.sqrt(time)))
    second_term = (-rate * strike_price * np.exp(-rate * time) * norm.cdf(d2))

    return first_term + second_term


# Rho is the sensitivity of the option price to the risk-free rate, measuring how the option value changes as rates change.
def rho(stock_price, strike_price, time, rate, vol):
    d2 = cd2(stock_price, strike_price, time, rate, vol)
    return (strike_price * time * np.exp(-rate * time) * norm.cdf(d2))
