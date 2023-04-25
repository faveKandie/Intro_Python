# import csv

# list_data = []
# temperature = []
# live = 0
# with open("weather_data.csv") as file1:
    # contents = csv.reader(file1)
    # for row in contents:
        # list_data.append(row)
        # rate = list_data[live]
        # live += 1
        # if rate[1] != "Temp": 
            # temperature.append(int(rate[1]))
    # #to get a column in the csv into a list using for loop
    # print(f"\n{temperature}")

#to express the csv file as a row and column form
import pandas

#to access it in pandas form  from the csv file and express it in a tabular form 
data = pandas.read_csv("weather_data.csv")
print(data)
#to hold a row in pandas form
read = data["Temp"]
#--print(type(data))

print(f"\n{data}")
#--print(f"\n{read}")

#to extract an entire coloumn from csv file in panda form
temp_data = data["Temp"]
#to extract an entire row from csv file in panda form
randname = data[data.Day == "Sunday"]
print(f"\n{randname}\n")

#to convert the csv file in pandas form into a python dictionary using the ".to_dict()" function
datadict = data.to_dict()
print(datadict)

#to get a column in the csv into a list using the ".to_list()"function
temp_data = data["Temp"].to_list()
print(temp_data)

#to get the length of a list do: len(listname)
#to get the sum of integers in a list, do: sum(listname)

#to get the average of a column using for loops
sand = 0
for n in temp_data:
    rand = n
    sand += rand
num_temp = len(temp_data)
average_temp = sand / num_temp
print(average_temp)

#to get the average of a column using ".mean()" function
print(data["Temp"].mean())#it must be done using the main variable holding the full csv file

#to obtain the highest value in a csv panda file integer column, do ".max()" function
print(data["Temp"].max()) 

#to obtain the highest value i csv file in panda form using for loop        
highest = 0
for r in temp_data:
    if r > highest:
        highest = r

#to print the column with the highest temperature after determining maximum temp using .max() function         
print(len(temp_data))
rare = data["Temp"].max()
rode = data["Temp"].min()

for n in range(0, len(temp_data)):
    if temp_data[n] == rare:
        rade = ((rare * 9/5) + 32)
        temp_data[n] = rade
    if temp_data[n] == rode:
        blade = ((rode * 9/5) + 32)
        temp_data[n] = blade

dict = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 
    'Temp': [12, 14, 15, 14, 21, 22, 24], 
    'Condition': ['Sunny', 'Rain', 'Rain', 'Cloudy', 'Sunny', 'Sunny', 'Sunny']
    }
    
dict["Temp"] = temp_data
print(dict)
data = pandas.DataFrame(dict)
data.to_csv("weather_data.csv")
print(data)
# print(temp_data)
       

#to print the column with the highest temperature after determining maximum temp using for loop
for n in data["Temp"]:
    if n == highest:
        wed = data[data.Temp == highest]
        print(wed)

#to get a particular column information for a particular row, do:
Monday = data[data.Day == "Monday"]
print(f"\n{Monday.Condition}") #the dot is like a pass to accessing contents of something

data_dict = {
    "name": ["Uju", "Red", "Sam"],
    "age": ["19", "18", "21"]
    }
#to convert a python dictionary to be expressed as panda tabular form
date = pandas.DataFrame(data_dict)
print(date)
    
date.to_csv("new_data.csv")

#series -- requires reference from the main source i.e the main variable holding the entire csv file in panda form...
#...the desired column is access by doing varname1["rowname"].func
         