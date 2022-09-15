# importing useful modules 
import csv
import pandas as pd
import glob
import os

# -----------------------------------------------------------------------------------------------------------
# optional step to merge all files 
# merging the files


# joined_files = os.path.join("*.csv")
  
# A list of all joined files is returned
# joined_list = glob.glob(joined_files)
  
# Finally, the files are joined
# df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
# df.to_csv('mergedfile.csv',index = False)

# ----------------------------------------------------------------------------------------------------------------

# intialize set and dict 
# for geting unique value of name from the data
name = set()

# dictionary dict would contain the dates on which student was present as its value(stored as set) and 
# student name as key 
# ex : {"Naman":(2/18/2022,1/03/2021,..... , ...,)
dict = dict()

# creating dictionary that will store the data for each student
attendance = {"Name":["Total No Days Present","Total No of Working Days","Attendance Percentage"]}

# opening merged csv file
with open('mergedfile.csv','r') as file:
    data = csv.reader(file)

    next(data)
    for line in data:
        name.add(line[0])

for line in name:
    dict[line.capitalize()] = set()

with open('mergedfile.csv','r') as newfile:
    newdata = csv.reader(newfile)

    next(newdata)

    for line in newdata:
        dict[line[0].capitalize()].add(line[2].split()[0])


#  logic to find total Number of working days 
s = 0
for i in dict:
    s = max(s,len(dict[i]))


# appending all information to be displayed in attendance dictionary
for line in dict:
    attendance[line] = []
    attendance[line].append(len(dict[line]))
    attendance[line].append(s)
    attendance[line].append((len(dict[line])/s)*100)


df = pd.DataFrame(attendance)
df1 = df.T


# writing data in .csv file
df1.to_csv("Final Attendance.csv",index="False")

# optional method(for tkinter project)
# os.remove("mergedfile.csv")
# os.remove("Final Attendance.csv")





