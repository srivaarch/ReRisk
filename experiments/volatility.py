# NumPy for arrays, gradient (derivative), and linspace 
# Matplotlib for graphing visualized data   
import numpy as np
import matplotlib.pyplot as plot

# Black-Scholes function
from rerisk.pricing.black_scholes import black_scholes

# Runs a for-loop for each volatility increment to assess the change in price
def vol_sim(stock_price, strike_price, time, rate, vol_range):
    prices = []
    for vol in vol_range:
        prices.append(black_scholes(stock_price, strike_price, time, rate, vol))
    
    # Convert to numpy array for plotting
    return np.array(prices)

# Approximates derivative of d(price)/d(volatility) using finite differences between sampled points
def gradient_sim(prices, vol_range):
    return np.gradient(prices, vol_range)

def main():
    stock_price = 500
    strike_price = 500
    time = 1
    rate = 0.05

    # Gives an array of 50 evenly spaced values from 0.01 to 1
    vol_range = np.linspace(0.01, 1, 50)

    prices = vol_sim(stock_price, strike_price, time, rate, vol_range)
    sensitivity = gradient_sim(prices, vol_range)

    # Plot data with matplotlib

    fig, axis = plot.subplots(2, 1, figsize=(10, 10))
    axis[0].plot(vol_range, prices)
    axis[0].set_title("Option Price vs Volatility")
    axis[0].set_xlabel("Volatility")
    axis[0].set_ylabel("Option Price")

    axis[1].plot(vol_range, sensitivity)
    axis[1].set_title("Sensitivity of Option Price to Volatility")
    axis[1].set_xlabel("Volatility")
    axis[1].set_ylabel("Sensitivity")

    plot.tight_layout()
    plot.show()

if __name__ == "__main__":
    main()