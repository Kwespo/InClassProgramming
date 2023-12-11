import pandas as pd
import matplotlib.pyplot as plt

# CREATE DATAFRAME
df = pd.DataFrame({
    "days" : [1, 2, 3, 4],
    "stars" : [ 643, 753, 745, 754],
    "shootingStar" : [2, 0, 4, 6],
})
index = [1,2,3]

#printing the data in the database

#print(df.iloc[0]) # prints all of day 1 collum

#print(df.iloc[0][1]) #prints collum 0 (day 1) and row 2 (the 2nd days amount of shooting stars )

#getting the mean of start
#print(df["stars"].mean()) # returns the mean

scatterChart = df.plot.scatter( x = ["days", "days"],
                                y = ["stars", "shootingStar"],
                                title = "Stars per day",
                                xlabel = "Days from 1-4",
                                ylabel = "Stars counted",
                                
                                )

plt.show()