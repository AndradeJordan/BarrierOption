import matplotlib.pyplot as plt
from scipy.stats import describe
import numpy as np


class Displayer:
    def scenario(St, cp_scenario, B=None):
        if B is None:
            plt.plot(St[: cp_scenario, :].T)
            plt.grid(True)
            plt.xlabel('Time step (t)')
            plt.ylabel('Underlying (S)')
            plt.legend("Scenario (St) On BSM")
            plt.tight_layout()
            plt.show()
        else:
            plt.plot(St[: cp_scenario, :].T)
            plt.grid(True)
            plt.xlabel('Time step (t)')
            plt.ylabel('Underlying (S)')
            plt.legend("Scenario (St) On BSM")
            plt.tight_layout()
            plt.show()

    def display_price(price, tag=""):
        if tag == "Up and In call option" or tag == "Up and Out call option":
            print(f"Price of the {tag} by Simulation is {price[0]}")
            print("On the confidence interval [ ", price[0] - price[2], " ", price[0] + price[2], " ]")
        elif tag == "":
            print(f"Price of the call by Simulation is {price[0]}")
            print("On the confidence interval [ ", price[0] - price[2], " ", price[0] + price[2], " ]")
        else:
            raise ValueError(f"You need to take an option called 'Up and In call option' or 'Up and Out call option' ")



