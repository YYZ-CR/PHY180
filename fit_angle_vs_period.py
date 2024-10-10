import fit_black_box_ap as bb

def quadratic(t, a, b, c):
    return a*t**2 + b*t + c

filename="sorted_angle_vs_period.txt"
x, y, xerr, yerr = bb.load_data(filename)
#y, x, yerr, xerr = bb.load_data(filename)

# Now we make the plot, displayed on screen and saved in the directory, and print the best fit values
bb.plot_fit(quadratic, x, y, xerr, yerr)

