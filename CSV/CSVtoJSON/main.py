import csv
import json

linenum = 0

jsonDta = {
          "drinks" : (),
          "grains" : (),
          "proteins" : (),
          "fruits" : (),
          "vegetables" : (),
          }

with open("CSV/CSVtoJSON/datasheet.csv") as f:
  reader = csv.reader(f, delimiter = ",")

  for row in reader:
    if linenum == 0:
      pass
    jsonDta.update({f"{row[0]}" : "{row[0].append(row[1])}"})
  

y = json.dump(jsonDta)

print(y)