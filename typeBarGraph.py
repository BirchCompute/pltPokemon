
import matplotlib.pyplot as plt
import pandas as pd
#Read the data into pandas dataFrames
dfPokeData = pd.read_csv("pokemonInfo.csv")
dfTypeColors  = pd.read_csv("typeColors.csv")
#Count how many times a type shows up in Pokedex
mainTypeCount = dfPokeData["Type 1"].value_counts()
totalTypeCount = mainTypeCount.to_frame()
secondTypeCount = dfPokeData["Type 2"].value_counts()
totalTypeCount["count2"] = secondTypeCount
print(totalTypeCount)
#Make the color list
typeColors = []
for c in dfTypeColors.itertuples():
  if("GEN 7 — SM" in c.Gen and "inium" not in c.Gen):
    typeColors.append(c.colors[:7])

    
#Add colors to the dataFrame
totalTypeCount = totalTypeCount.sort_values(by= "Type 1")
totalTypeCount["typeColors"] = type

Colorsdef hex_to_rgb(hexa):
    hexa = hexa[1:]
    return tuple((int(hexa[i:i+2], 16)/500)  for i in (0, 2, 4))

totalTypeCount["total"] = totalTypeCount["count"] + totalTypeCount["count2"]
#totalTypeCount = totalTypeCount.sort_values(by= "total")
totalTypeCount["lightTypeColors"]  = totalTypeCount["typeColors"]
totalTypeCount["lightTypeColors"] = totalTypeCount["lightTypeColors"].apply(hex_to_rgb)
print(totalTypeCount)

for x in totalTypeCount.itertuples():
    print(x.Index, x.total, end = ", ")fig, axs = plt.subplots()

axs.bar(totalTypeCount.index, totalTypeCount["count"], color = totalTypeCount["typeColors"], width = 1, edgecolor='black', linewidth=2)
axs.bar(totalTypeCount.index, totalTypeCount["count2"], color = totalTypeCount["lightTypeColors"], bottom = totalTypeCount["count"], width = 1, edgecolor='black', linewidth=2)


axs.tick_params(axis='x', labelrotation=75, length = 2)
axs.set_title("Pokemon primary and secondary\n type prevalence as of 1025 Pokemon (alphabetical)")
axs.set_xlabel("Types")
axs.set_ylabel("Count")
