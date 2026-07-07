# Numpy for linspace, arrays
# Matplotlib for graphing data
import numpy as np
import matplotlib.pyplot as plot

# Greeks functions
from rerisk.pricing.greeks import delta, gamma, vega, theta, rho

def main():
    # Array of 250 different stock prices
    stock_prices = np.linspace(50, 150, 250)
    strike_price = 100
    time = 1
    rate = 0.05
    vol = 0.2

    # Arrays of each greek across different stock prices
    deltas = np.array([delta(stock_price, strike_price, time, rate, vol) for stock_price in stock_prices])
    gammas = np.array([gamma(stock_price, strike_price, time, rate, vol) for stock_price in stock_prices])
    vegas = np.array([vega(stock_price, strike_price, time, rate, vol) for stock_price in stock_prices])
    thetas = np.array([theta(stock_price, strike_price, time, rate, vol) for stock_price in stock_prices])
    rhos = np.array([rho(stock_price, strike_price, time, rate, vol) for stock_price in stock_prices])

    # Plot data
    fig, axis = plot.subplots(5, 1, figsize=(10, 10))

    # plot.axvline used to reference the strike price where 'at-the-money' is

    # Delta
    axis[0].plot(stock_prices, deltas)
    axis[0].axvline(strike_price, linestyle="--")
    axis[0].set_title("Delta vs Stock Price")
    axis[0].set_xlabel("Stock Price")
    axis[0].set_ylabel("Delta")

    # Gamma
    axis[1].plot(stock_prices, gammas)
    axis[1].axvline(strike_price, linestyle="--")
    axis[1].set_title("Gamma vs Stock Price")
    axis[1].set_xlabel("Stock Price")
    axis[1].set_ylabel("Gamma")

    # Vega
    axis[2].plot(stock_prices, vegas)
    axis[2].axvline(strike_price, linestyle="--")
    axis[2].set_title("Vega vs Stock Price")
    axis[2].set_xlabel("Stock Price")
    axis[2].set_ylabel("Vega")

    # Theta
    axis[3].plot(stock_prices, thetas)
    axis[3].axvline(strike_price, linestyle="--")
    axis[3].set_title("Theta vs Stock Price")
    axis[3].set_xlabel("Stock Price")
    axis[3].set_ylabel("Theta")

    # Rho
    axis[4].plot(stock_prices, rhos)
    axis[4].axvline(strike_price, linestyle="--")
    axis[4].set_title("Rho vs Stock Price")
    axis[4].set_xlabel("Stock Price")
    axis[4].set_ylabel("Rho")

    plot.tight_layout()
    plot.show()

if __name__ == "__main__":
    main()




