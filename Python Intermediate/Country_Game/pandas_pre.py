import pandas
 
road = pandas.read_csv("Squirrel_centralPark.csv")  
#since the .csv document is originally from macintosh file and came in as text file, i resaved it in wps
#...as a .csv file. But it then had quotation marks which i deleted the content and pasted the .txt content of it
#...my npp exec console couldn't decode the .csv file since it was originally macintosh
#i then changed the encoding of that .csv file to "UTF-8-BOM" and added "\ufeff" to the front of the first line
#and it ran.

#to get the number of contents in the gray row
gray_squirrels = len(road[road["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(road[road["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(road[road["Primary Fur Color"] == "Black"])
print(gray_squirrels)
print(cinnamon_squirrels)
print(black_squirrels)

squirrel = {
    "Fur color": ["grey", "cinnamon", "black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
    }
squirr = pandas.DataFrame(squirrel)
print(squirr)
squirr.to_csv("squirrel.csv")

 

