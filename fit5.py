import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from matplotlib.font_manager import FontProperties


def run():
    df = pd.read_csv('./data/datos.csv') 
    
    def f1(x, a0, a1, a2, a3, a4, a5):
        return a0 + a1*x + a2*(x**2) + a3*(x**3) + a4*(x**4) + a5*(x**5)

    results, cov = curve_fit(f1, df['T'], df['E'])
    print(results)


    x = np.linspace(0,13,100)   
    
   
    fig, ax = plt.subplots()
    ax.scatter(df['T'], df['E'], marker = 'o', color='red', label="Puntos Exp.")
    ax.plot(x,f1(x,results[0], results[1], results[2], results[3], results[4], results[5]), label="$E_{T}(T) = -25.84 + 18.05 T - 4.77 T^{2} + 0.59 T^{3} + 0.02 T^{4} + 7.85 x 10^{-4}T^{5}$", linewidth=2)
    plt.xlim(2,15)
    plt.ylim(-50,850)
    plt.legend(loc='upper left')
    plt.xlabel("T [kK]", fontsize='large', fontweight='bold')
    plt.ylabel("E [MW/m²]", fontsize='large', fontweight='bold')
    plt.show()

if __name__ == "__main__":
    run()