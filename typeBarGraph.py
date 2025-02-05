
import matplotlib.pyplot as plt
import pandas as pd


#Read the data into pandas dataFrames
dfPokeData = pd.read_csv("pokemonInfo.csv")
dfTypeColors  = pd.read_csv("typeColors.csv")


#Count how many times a type shows up in Pokedex
totalTypeCount = dfPokeData["Type 1"].value_counts().to_frame()
totalTypeCount["count2"] = dfPokeData["Type 2"].value_counts()
totalTypeCount["total"] = totalTypeCount["count"] + totalTypeCount["count2"]

#Make the color list
typeColors = []
typeColorsDark = []
for color in dfTypeColors.itertuples():
  if("GEN 7 — SM" in color.Gen and "inium" not in color.Gen):
    typeColors.append(color.colors[:7])
    #Turns the hex color into a darker rgb tuple
    typeColorsDark.append(tuple((int(color.colors[:7][i+1:i+3], 16)/500)  for i in (0, 2, 4)))

#Add colors to the dataFrame
#The color list is alphabetical, so sort the totals dataframe to be alphabetical by type
totalTypeCount = totalTypeCount.sort_values(by= "Type 1")
totalTypeCount["typeColors"] = typeColors
totalTypeCount["darkTypeColors"] = typeColorsDark


#Force a size for the figure
plt.rcParams['figure.figsize'] = [16,6]

#Prepare the figure
fig, (axs1, axs2) = plt.subplots(1,2)


#Make the actual bars for first chart
axs1.bar(totalTypeCount.index, totalTypeCount["count"], color = totalTypeCount["typeColors"], width = 1, edgecolor='black', linewidth=2)
axs1.bar(totalTypeCount.index, totalTypeCount["count2"], color = totalTypeCount["darkTypeColors"], bottom = totalTypeCount["count"], width = 1, edgecolor='black', linewidth=2)

#Mark first axes
axs1.tick_params(axis='x', labelrotation=75, length = 2)
axs1.set_title("Pokemon primary and secondary\n type prevalence as of 1025 Pokemon (alphabetical)")
axs1.set_xlabel("Types")
axs1.set_ylabel("Count")

#Sort by total and do it again for the second chart
totalTypeCount = totalTypeCount.sort_values(by= "total")

#Make the actual bars for second chart
axs2.bar(totalTypeCount.index, totalTypeCount["count"], color = totalTypeCount["typeColors"], width = 1, edgecolor='black', linewidth=2)
axs2.bar(totalTypeCount.index, totalTypeCount["count2"], color = totalTypeCount["darkTypeColors"], bottom = totalTypeCount["count"], width = 1, edgecolor='black', linewidth=2)

#Mark the second axes
axs2.tick_params(axis='x', labelrotation=75, length = 2)
axs2.set_title("Pokemon primary and secondary\n type prevalence as of 1025 Pokemon (sorted)")
axs2.set_xlabel("Types")
axs2.set_ylabel("Count")
