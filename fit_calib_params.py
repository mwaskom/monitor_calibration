from __future__ import division, print_function

import matplotlib as mpl
mpl.use("Agg")

import sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def main(arglist):

    # Hardcoded values that correspond to the calibration script."""
    digit_values = [0, 10, 20, 40, 60, 80, 100, 120,
                    140, 160, 180, 200, 220, 240, 255]

    _, fname = arglist
    df = pd.read_csv(fname)
    df["Digit"] = digit_values

    init_params = 2.2, df["Lv"].max(), df["Lv"].min()
    fit_params, _ = curve_fit(expfun, df["Digit"], df["Lv"], init_params)

    f = plot_results(df, *fit_params)
    f.savefig(fname[:-3] + "png")

    gamma, max, min = fit_params

    print("Min luminance: {:.2f} cd/m2".format(min))
    print("Max luminance: {:.1f} cd/m2".format(max))
    print("Gamma value: {:.2f}".format(gamma))

def plot_results(df, gamma, max, min):
    """Generate a figure of the measured luminance and fitted gamma curve."""
    sns.set(style="ticks", font_scale=1.3, color_codes=True)

    f, ax = plt.subplots(figsize=(6, 6))

    ax.scatter(df["Digit"], df["Lv"], s=50, c="b", linewidth=0)
    xx = np.linspace(0, 255, 100)
    ax.plot(xx, expfun(xx, gamma, max, min), color="b")

    text = ("Min: {:.2f} cd/m$^2$\n"
            "Max: {:.1f} cd/m$^2$\n"
            "Gamma value: {:.2f}"
            .format(min, max, gamma))

    ax.text(.1, .7, text, transform=ax.transAxes)

    ax.set(xlim=(-4, 257),
           ylim=(-2, None),
           xticks=list(np.linspace(0, 200, 5)) + [255],
           xlabel="Gun value",
           ylabel="Luminance (cd/m$^2$)")

    sns.despine(trim=True)
    f.tight_layout()
    return f


def expfun(x, gamma, max, min):
    """Function to fit to luminance data."""
    return min + max * (x / 255) ** gamma


if __name__ == "__main__":
    main(sys.argv)
