from CallOption.UpCall import upCall
import numpy as np   # math operations
import numpy.random as npr # random
from scipy.stats import norm
import math

class UpAndInCall(upCall):
    def __init__(self, r, s0, sigma, T, K, n, N, B):
        super().__init__(r, s0, sigma, T, K, n, N)
        self.Barrier = B

    def description(self):
        super().description()
        print(f"Up and In Call with Barrier :{self.Barrier}")

    def priceSimulation(self):
        super().simulation()
        St, r, s0, sigma, T, K, n, N, B = self.Spaths, self.interest_rate, self.spot, self.sigma, self.maturity, self.strike, self.timeValue, self.MCnumber, self.Barrier

        condition =  St[:,-1] > B
        price = np.exp(-r * T) * (np.maximum(St - K, 0)[:,-1]*condition).mean()
        payoff = np.exp(-r * T) * np.maximum(St - K, 0)[:,-1]*condition
        sigma = np.std(payoff)  # standard deviation estimator  (ecart type de monte_carlo)
        error = 1.96 * sigma / np.sqrt(N)
        parameter = [price, sigma, error]
        return parameter