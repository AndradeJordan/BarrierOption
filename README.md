## Barrier Option Pricing Project
# Introduction
This project implements a Python framework for **pricing barrier options** using ***Monte Carlo simulation methods***. 
**Barrier options** are a type of financial derivative whose payoff depends on whether the underlying asset's price reaches or exceeds a certain level (the barrier) during the option's lifetime. 
This project provides classes for pricing various types of barrier options, including ***Up-and-In, Up-and-Out, Down-and-In, and Down-and-Out options***.

# Features
- **Modular Design :** The project is organized into separate modules for call options and put options, with each module containing classes for different types of barrier options.
- **Monte Carlo Simulation :** Barrier option prices are calculated using Monte Carlo simulation methods, providing accurate pricing estimates for complex derivative contracts.
- **Option Types :** Various types of barrier options are supported, including *Up-and-In Call, Up-and-Out Call, Down-and-In Put, and Down-and-Out Put options.*
- **Price Display :** The project includes a display module to present the pricing results of each option type.

# Usage
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the __main__.py script to execute the pricing simulations for different barrier option types.
4. View the pricing results displayed in the console.

 # Example
```python
# Initialize parameters
r, S0, sigma, T, K, N, n = 0.05, 100, 0.2, 1, 95, 1000, 252

# Up-and-In Call option with a barrier of 115
my_call_UpAndIn = UpAndIn.UpAndInCall(r, S0, sigma, T, K, n, N, 115)
param_UpAndIn = my_call_UpAndIn.priceSimulation()
displayerCall.Displayer.display_price(param_UpAndIn, "Up-and-In Call option")

```
# Conclusion 
The Barrier Option Pricing Project provides a comprehensive framework for pricing barrier options using Monte Carlo simulation techniques. 
It offers flexibility in modeling different types of barrier options and allows users to accurately estimate their prices based on specified parameters.
