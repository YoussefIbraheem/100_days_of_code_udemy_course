import pandas

file = pandas.read_csv("Squirrel_Data.csv")

count_upon_color = file.value_counts("Primary Fur Color")

color_data_dict = {
    "Fur Color" : count_upon_color.keys().to_list(),
    "Count": count_upon_color.to_list(),
}

color_data_frame = pandas.DataFrame(color_data_dict)

color_data_frame.to_csv("squirrel_count.csv")


