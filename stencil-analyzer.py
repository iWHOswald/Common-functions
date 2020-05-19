import re
import pandas as pd

stencil_list = []
stencil_points = []
stencil_location = []
stencil_all_points = []
all_avg_coords = []
point_out2 = []
all_avg_coords_time = []
all_points = []

# this function does everything. to run it, goto bottom, and change the file name in the last line.

def stencil_analyzer(stencil):
    for i, line in enumerate(open(stencil,encoding='utf-8-sig')): # input your file - save your stencil as a TXT
        for match in re.finditer('<ROI name="(.+?)" st', line): # find the names of compounds
            stencil_list.append(str(match.group())[11:-4])  #store names in list
        for match in re.finditer('<Points>(.+?)</Points>', line):   # find point values
            stencil_in = str(match.group())[8:-9].split(",") # split them up
            stencil_out = [int(i) for i in stencil_in]
            stencil_out = stencil_out[: -2 or None] #remove the last two as you only need first 2 values to calculate RT
            stencil_all_points.append(stencil_in)  #  this is the 4 points
            #stencil_points.append(stencil_out)  #  this is the 2 points needed to find the approx X coord of the stencil
        for match in re.finditer('      <Point id="(.+?)</Point>', line): #find the actual coordinates for each stencil
            point_in = str(match.group()) #convert point to string
            more = re.findall("\d+\.\d+", point_in) #extract the floats - i.e. coordinates
            point_out = [float(i) for i in more]    #split the x and y coords to only get x
            point_out = point_out[: -1 or None]     #remove the y coord
            point_out = str(point_out)[1:-1]        #convert x to str to remove the apostrophes
            point_out2.append(point_out)            # store the x axis values in array

    for i in range(len(stencil_all_points)):        #iterate thru the x values to calculate the location of center of stencil (x-axis)
        if i == 0:
            avg_coords = (float(point_out2[i]) + float(point_out2[i+1])) / 2    #get the x-axis location coordinate of hte middle of stencil
            all_avg_coords.append(avg_coords)   #store in array
        else:
            if i >= len(point_out2)-4:  #terminate the
                pass
            else:
                avg_coords = (float(point_out2[i*4]) + float(point_out2[(i*4)+1])) / 2
                all_avg_coords.append(avg_coords)

        avg_coords_time = avg_coords * 60
        all_avg_coords_time.append(avg_coords_time)

    df = pd.DataFrame(stencil_list, columns=['Compound name'])
    df.insert(1, "stencil points", stencil_all_points, True)
    #df.insert(2, "stencil coords", all_points, True)
    df.insert(2, "avg x coords", all_avg_coords, True)
    df.insert(3, "avg RT", all_avg_coords_time, True)
    df.to_csv(str(stencil) + '.csv',encoding='utf-8-sig')

stencil_analyzer("TEST_STENCFULL2.txt") # simply type in your txt file here. will save the file with same name as stencil 
