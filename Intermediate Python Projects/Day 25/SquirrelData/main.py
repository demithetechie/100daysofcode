import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = len(data[data['Primary Fur Color'] == "Gray"])
red_squirrels = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrels = len(data[data['Primary Fur Color'] == "Black"])

new_table = {
    "Fur color": ["grey", "red", "black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

smaller_data = pd.DataFrame(new_table)
smaller_data.to_csv("squirrel_count.csv")
