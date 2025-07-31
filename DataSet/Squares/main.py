import matplotlib.pyplot as plt

inputs = range(1, 1001)
squares = [x**2 for x in inputs]

plt.style.use('seaborn')
fig, ax = plt.subplots()
#plot dots with one color
ax.scatter(inputs, squares, color='red', s=20)

#plot dots with color gradient
#ax.scatter(inputs, squares, c=squares, cmap=plt.cm.Blues, s=20)

#plot line
#ax.plot(inputs, squares, linewidth=3)

#Set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

#Set size of tick labels
ax.tick_params(labelsize = 14)

ax.axis([0, 1100, 0, 1_100_000])
#ax.ticklabel_format(style='plain')

plt.show()
plt.savefig('squares_plot.png')