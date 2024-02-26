from absParameter import AbsParameter
import numpy as np  # math operations
import numpy.random as npr  # random
from scipy.stats import norm
import math


class upCall(AbsParameter):
    def __init__(self, r, s0, sigma, T, K, n, N):
        self.interest_rate, self.spot, self.sigma, self.maturity, self.strike, self.timeValue, self.MCnumber = r, s0, sigma, T, K, n, N
        self.Spaths = None

    def description(self):
        return f"Black sholes model with r={self.interest_rate}, S0 ={self.spot}, sigma={self.sigma}, T ={self.maturity}, K ={self.strike}, TimeValueNumber={self.timeValue}, MonteCarloNumber={self.MCnumber}"

    def simulation(self):
        r, s0, sigma, T, K, n, N = self.interest_rate, self.spot, self.sigma, self.maturity, self.strike, self.timeValue, self.MCnumber

        delta = float(T / n)
        G = npr.normal(0, 1, size=(N, n))
        # Log returns
        LR = (r - 0.5 * sigma ** 2) * delta + np.sqrt(delta) * sigma * G
        # concatenate with log(S0)
        LR = np.concatenate((np.log(s0) * np.ones((N, 1)), LR), axis=1)
        # cumsum horizontally (axis=1)
        LR = np.cumsum(LR, axis=1)
        # take the expo Spath matrix
        spaths = np.exp(LR)
        self.Spaths = spaths

    def priceSimulation(self):
        self.simulation()
        St, r, s0, sigma, T, K, n, N = self.Spaths, self.interest_rate, self.spot, self.sigma, self.maturity, self.strike, self.timeValue, self.MCnumber
        price = np.exp(-r * T) * np.maximum(St - K, 0)[:,-1].mean()
        payoff = np.exp(-r * T) * np.maximum(St - K, 0)[:,-1]
        sigma = np.std(payoff)  # standard deviation estimator  (ecart type de monte_carlo)
        error = 1.96 * sigma / np.sqrt(N)
        parameter = [price, sigma, error]
        return parameter
