import pandas as pd
import matplotlib.pyplot as plt
from colour import Color
import matplotlib as mpl

##### this function plots a vertical bar graph with a color gradient interpolated between two colors.

def PlotBar(file):

    data = pd.read_csv(file)
    for i in range(len(data)): # this loop will iterate thru dataset and remove %s so that only floats are left
        data.iat[i,1] = float(data.iat[i,1][:-1]) #remove % and convert to float
        if data.iat[i,1] <= 5:
            data.iat[i, 1] = data.iat[i,1] + 0.5 # this artificially boosts some of the low conc values, just so they
            # are actually visible (entirely an aesthetic effect)
    data = data.sort_values(by=['conc'], ascending=False) # sort the data in descending order

    # this function interpolates between two colors to generate a gradient for the bar graph
    bar_colors = [0,0,0,0,0,0,0,0,0,0] #initialize an array to store the color values
    dark_green = Color("#003e17")  #your first color as hex code
    colors = list(dark_green.range_to(Color("#f4ec16"), 10)) #generate a list of colors for the bar graph
    for i in range(len(colors)): # iterate and transpose the values in the list to an array
        bar_colors[i] = str(colors[i])
    print(bar_colors) #sanity check to make sure your values look reasonable


    ######## plot your graph #########

    mpl.rcParams['axes.spines.left'] = False # turn off axes left
    mpl.rcParams['axes.spines.right'] = False # turn off axes right
    mpl.rcParams['axes.spines.top'] = False # turn off axes top

    data.plot(kind='bar', x='canna', y='conc',color=(bar_colors),legend=None) #set the x and y axes data, and set colors from above
    plt.yscale('linear')
    plt.ylabel("") # set y axis label (none in this case)
    plt.xlabel("") # set x axis label (none in this case)
    plt.tick_params(labelleft=False, labelbottom=False, left=False)
    #plt.axis('off') turn off entire frame + axes

    plt.tight_layout()
    # plt.savefig("FIG_BA.svg", dpi=300, transparent=False)
    plt.show()

PlotBar("TEST_THC.csv")
