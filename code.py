import csv
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("c134.csv")

temp_distance=[]

for distance in df.distance:
  if distance <= 100:
    temp_distance.append(True)
  else:
    temp_distance.append(False) 

is_dist=pd.Series(temp_distance)
star_dist=df[is_dist]
print(len(star_dist))

star_dist.reset_index(inplace=True,drop=True)
star_dist.shape

temp_gravity=[]

for gravity in star_dist.gravity:
  # gravity=round(gravity)
  # print(gravity)
  if gravity <= 5 and gravity >= 1:
    temp_gravity.append(True)
  else:
    temp_gravity.append(False)

is_gravity=pd.Series(temp_gravity)
final_stars=star_dist[is_gravity]
final_stars.shape
final_stars.reset_index(inplace=True,drop=True)
final_stars.to_csv("filter_data.csv")