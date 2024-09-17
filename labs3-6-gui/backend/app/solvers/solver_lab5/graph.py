def generate_data_for_graphik(x, y, interpolation_func):
    xs, ys = [], []
    dx = 0.1
    a = x[0] - dx
    b = x[-1] + dx
    i = a
    while i <= b:
        xs.append(i)
        ys.append(interpolation_func(x, y, i))
        i += dx
    return xs, ys


# def plot_interpolation(xs, ys, interpolation_func, interpolation_label, value, x, y, frame):
#     fig, ax = plt.subplots()
#     ax.plot(xs, ys)
#     ax.set_title(interpolation_label)
#     ax.scatter(value, interpolation_func(x, y, value), color='blue')
#     ax.scatter(x, y, color='red')
#     ax.set_xlabel("X")
#     ax.set_ylabel("Y")
#
#     canvas = FigureCanvasTkAgg(fig, master=frame)
#     canvas.draw()
#     canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
