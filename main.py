import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

GraySquirels = data[data["Primary Fur Color"] == "Gray"]
BlackSquirels = data[data["Primary Fur Color"] == "Black"]
CinnamonSquirels = data[data["Primary Fur Color"] == "Cinnamon"]

print("The amount of Gray squirrels in the Central Park is =", len(GraySquirels))
print("The amount of Black squirrels in the Central Park is =", len(BlackSquirels))
print("The amount of Cinnamon squirrels in the Central Park is =", len(CinnamonSquirels))
