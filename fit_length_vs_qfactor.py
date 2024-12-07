import fit_black_box_length_qfactor as bb

def quadratic(t, a, b, c):
    return a*t**2 + b*t + c

def expon(t, a, b):
    return a*bb.np.exp(-t/b)

def linear(t, a, b):
    return a*t + b

def power(l, k, n):
    return k * l**n

init_guess = (1,1) # guess for the best fit parameters
font_size = 18
xlabel = "Length (m)"
ylabel = "Q Factor"
title = 'Length [m] vs Q Factor'

filename="length_vs_qfactor.txt"
x, xerr, y, yerr = bb.load_data(filename)
#y, x, yerr, xerr = bb.load_data(filename)

# Now we make the plot, displayed on screen and saved in the directory, and print the best fit values
bb.plot_fit(power, x, y, xerr, yerr, init_guess, font_size, xlabel, ylabel, title)

