import fit_black_box_at as bb

def expon(t, a, b):
    return a*bb.np.exp(-t/b)

filename="sorted_angle_vs_time.txt"
x, y, xerr, yerr = bb.load_data(filename)
#y, x, yerr, xerr = bb.load_data(filename)

bb.plot_fit(expon, x, y, xerr, yerr)


