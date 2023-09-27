DataList = []
with open("Files/Data.txt", "r") as f:
  Data = f.readlines()

  for line in Data:
    DataList.append(int(line.rstrip()))


print(DataList)