
from CallOption import UpCall,UpAndIn,UpAndOut
from Displayer import displayerPut,displayerCall
from PutOption import DownAndIn,DownAndOut,DownPut
import numpy as np

def main():
    HighBarrier = 115
    LowBarrier = 95
    r, S0, sigma, T, K, N, n = 0.05, 100, 0.2, 1, 95, 1000, 252
    # CALL
    my_call = UpCall.upCall(r, S0, sigma, T, K, n, N)
    my_call.description()
    param = my_call.priceSimulation()
    displayerCall.Displayer.display_price(param)
    print("\n")

    # Up and In
    my_call_UpAndIn = UpAndIn.UpAndInCall(r, S0, sigma, T, K, n, N,HighBarrier)
    my_call_UpAndIn.description()
    param_UpAndIn = my_call_UpAndIn.priceSimulation()
    displayerCall.Displayer.display_price(param_UpAndIn,"Up and In call option")
    print("\n")

    # Up and Out
    my_call_UpAndOut = UpAndOut.UpAndOutCall(r, S0, sigma, T, K, n, N, HighBarrier)
    my_call_UpAndOut.description()
    param_UpAndOut = my_call_UpAndOut.priceSimulation()
    displayerCall.Displayer.display_price(param_UpAndOut, "Up and Out call option")


    # Put
    print("\n\n")
    my_put = DownPut.downPut(r, S0, sigma, T, K, n, N)
    my_put.description()
    print("\n")
    param = my_put.priceSimulation()
    displayerPut.Displayer.display_price(param)
    print("\n")

    # Down and In
    my_put_DownAndIn = DownAndIn.DownAndInPut(r, S0, sigma, T, K, n, N, LowBarrier)
    my_put_DownAndIn.description()
    param_DownAndIn = my_put_DownAndIn.priceSimulation()
    displayerPut.Displayer.display_price(param_DownAndIn, "Down and In put option")
    print("\n")

    # Up and Out
    my_put_DownAndOut = DownAndOut.DownAndOutPut(r, S0, sigma, T, K, n, N, LowBarrier-20)
    my_put_DownAndOut.description()
    param_DownAndOut = my_put_DownAndOut.priceSimulation()
    displayerPut.Displayer.display_price(param_DownAndOut, "Down and Out put option")



if __name__ == "__main__":
    main()