import shapefile
import os
import pandas as pd
from pandas import DataFrame
import numpy as np
import json

sf = shapefile.Reader("./lrnf000r18a_e/lrnf000r18a_e.shp")

sample_size = 2228867
ERROR_X = 0.01
ERROR_Y = 0.01
TEST_X = 7723764.146965375
TEST_Y = 1547160.1080739326

x_coord = -71.253019
y_coord = 47.82534

result_list = []
result_counter = 0

# xx = sf.shape(2139111)
# print(xx.points)
# print(xx.bbox)


class_code_counter = 0
class_code_list = []
success_counter = 0
fail_counter = 0
# for i in range(1000):
#     try:
#         r = sf.record(i)
#         s = sf.shape(i)
#         temp = s.points
#         if(r['CLASS'] == '25'):
#             class_code_counter += 1
#             class_code_list += temp
#         success_counter += 1
#     except:
#         fail_counter += 1

# print(success_counter)
# print(fail_counter)
# print(class_code_counter)
# print(class_code_list)


r = sf.record(2139111)
# s = sf.shape(2139111)
print("loading")
print(r['CLASS'])
# print(s.points)
# for i in range(sample_size):
# try:
#     coords = sf.shape(int(2139111))
#     if TEST_X >= coords.bbox[0] and TEST_X <= coords.bbox[2] and TEST_Y >= coords.bbox[1] and TEST_Y <= coords.bbox[3]:
#         # for j in range(len(coords.points)):
#         #     coords_x = coords.points[j][0]
#         #     coords_y = coords.points[j][1]
#         #     if
#         # r = sf.record(int(i))

#         result_list.append(coords.points)
#         result_counter += 1
# except:
#     pass

# print(result_counter)
# fh = open("./searcher_result.json", "w")
# fh.write(json.dumps(result_list))
# fh.close()

# with open("./searcher_result/searcher_result_coords.json") as json_file1:
#     test = pd.DataFrame(json.load(json_file1), columns=['x', 'y'])
# test = test[['x', 'y']]

# for i in range(len(test)):
#     if (x_coord >= test.iloc[i]['x'] - ERROR_X) and (x_coord <= test.iloc[i]['x'] + ERROR_X) and (y_coord >= test.iloc[i]['y'] - ERROR_Y) and (y_coord <= test.iloc[i]['y'] + ERROR_Y):
#         result_list.append(list(test.iloc[i]))
#         result_counter += 1

# print(result_counter)
