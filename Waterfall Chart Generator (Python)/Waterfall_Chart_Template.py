import matplotlib.pyplot as plt
import numpy as np


def minimized_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # Add more suffixes if you need them
    return '%.1f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])


# x values
labels = [
    'Step1',
    'Step2',
    'Step3',
    'step4',
    'step5',
    'step6',
    'step7',
    'step8',
    'step9',
    'step10',
]

# y values
starting_value = 31801027
starting_label = 'Starting Balance'
ending_label = 'Ending Balance'

values = [
    974029,
    712271,
    -355179,
    -501519,
    -48156,
    -434292,
    -42926,
    31525,
    -259399,
    928594,
]


# Variables that drive the visualization
# Makes the bars touch giving the waterfall plot feel
bar_width = 1.0
# Used to generate the horizontal lines on the plot
line_length = 1.5
# Used to generate the horizontal lines on the plot
line_thickness = 1.5
# Used to label and draw values on the plot
positions = range(len(labels))

# Calculate cumulative values to stack the bars
cumulative_values = [0]
running_total = [values[0]]
for value in values[:-1]:
    cumulative_values.append(cumulative_values[-1] + value)
    running_total.append(running_total[-1] + value)



# Define the colors for the bars (IF =< 0 THEN + Color ELSE - Color)
colors = ['#0076BD' if val >= 0 else '#E13E31' for val in values]


# Generate waterfall chart and define some rules for the plot
fig, ax = plt.subplots(figsize=(10, 6))
plt.box(False)
plt.tick_params(bottom=False, left=False)
ax.get_yaxis().set_visible(False)
# Draws the min and max of the y values (This is so labels display above the bar without any trouble)
plt.ylim(cumulative_values[0]-(np.mean(cumulative_values)*.1) if min(values) == 0 else min(values)*1.05, np.max(cumulative_values)+int(max(cumulative_values)*.2))


# Plot the bars
for i in range(len(values)):
    if i == 0:
        ax.bar(positions[i], values[i], color=colors[i], width=bar_width)
    else:
        ax.bar(positions[i], values[i], bottom=cumulative_values[i], color=colors[i], width=bar_width)


# Add labels
for i in range(len(running_total)):
    if values[i] >= 0:
        ax.text(positions[i], cumulative_values[i] + values[i], minimized_format(values[i]), ha='center', va='bottom', fontweight='bold', fontsize=8)
    else:
        ax.text(positions[i], cumulative_values[i], minimized_format(values[i]), ha='center', va='bottom', fontweight='bold', fontsize=8)


# Beginning horizontal line that shows the starting value
ax.plot([positions[0] - line_length, (positions[0] + positions[1])/ 2], [0, 0], color='black', linewidth=line_thickness)
ax.text(positions[0] - line_length - .1, 0, str(minimized_format(starting_value) + '\n' + starting_label), ha='right', va='center', fontweight='bold', fontsize=8)


# Ending horizontal line that shows the ending value
final_value = running_total[-1]
# If the last value in the waterfall is positive THEN draw horizontal line at top of bar
if values[-1] >= 0:
    ax.plot([(positions[-1] + positions[-2])/ 2, positions[-1] + line_length], [cumulative_values[-1] + values[-1], cumulative_values[-1] + values[-1]], color='black', linewidth=line_thickness)
    ax.text(positions[-1] + line_length + 0.2, cumulative_values[-1] + values[-1], str(minimized_format(starting_value-final_value) + '\n' + ending_label), ha='left', va='center', fontweight='bold', fontsize=8)
# If the last value in the waterfall is negative THEN draw horizontal line at bottom of bar
else:
    ax.plot([(positions[-1] + positions[-2])/ 2, positions[-1] + line_length], [cumulative_values[-1] + values[-1], cumulative_values[-1] + values[-1]], color='black', linewidth=line_thickness)
    ax.text(positions[-1] + line_length + 0.2, cumulative_values[-1] + values[-1], str(minimized_format(starting_value-final_value) + '\n' + ending_label), ha='left', va='center', fontweight='bold', fontsize=8)



ax.set_xticks(positions)
ax.set_xticklabels(labels, rotation=45)



# Add title and labels
ax.set_title('Waterfall Chart')
#ax.set_xlabel('Categories')
#ax.set_ylabel('Values')

plt.tight_layout()
plt.show()
