import plotly.express as px

from die import Die

die_1 = Die()
die_2 = Die(10)

results = []

for roll in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequencies.append(results.count(value))

title = "Results of 50000 rolls of D6 and D10 die"
labels = {"x": "Result", "y": "Frequency"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
#fig.write_html('RollsOfD6andD10.html')