import shapefile
import json

sf = shapefile.Reader("./lrnf000r18a_e/lrnf000r18a_e.shp")

hwy_counter = 0
ramp_counter = 0
cross_counter = 0
class_code_counter = 0
fail_counter = 0
success_counter = 0

hwy = []
hwy_list = []
ramp = []
ramp_list = []
cross = []
cross_list = []
class_code = []
class_code_list = []

sample_size = 2228867
bin_size = 200000
bin_last_size = sample_size % bin_size
bin_number = int(sample_size/bin_size+1)


for i in range(sample_size):
    try:
        r = sf.record(int(i))
        s = sf.shape(int(i))
        temp = s.points
        if(r['CLASS'] == '25'):
            class_code_counter += 1
            class_code_list += temp
        success_counter += 1
    except:
        fail_counter += 1

class_code = list(set(class_code_list))

# for j in range(bin_number):
#     print("bin_number: " + str(j))
#     if(j == bin_number-1):
#         record_bin = bin_last_size
#     else:
#         record_bin = bin_size

#     for i in range(record_bin):
#         try:
#             r = sf.record(int(i+j*bin_size))
#             s = sf.shape(int(i+j*bin_size))
#             temp = s.points
#             # if (r['TYPE'] == 'HWY'):
#             #     hwy_counter += 1
#             #     hwy_list += temp
#             # elif(r['TYPE'] == 'RAMP'):
#             #     ramp_counter += 1
#             #     ramp_list += temp
#             # elif(r['TYPE'] == 'CRSSRD'):
#             #     cross_counter += 1
#             #     cross_list += temp
#             if(r['CLASS'] == '25'):
#                 class_code_counter += 1
#                 class_code_list += temp
#             success_counter += 1
#         except:
#             fail_counter += 1

    # hwy += hwy_list
    # ramp += ramp_list
    # cross += cross_list
    # class_code += class_code_list

    # hwy_list = []
    # ramp_list = []
    # cross_list = []
    # class_code_list = []


# hwy = list(set(hwy))
# ramp = list(set(ramp))
# cross = list(set(cross))
# class_code = list(set(class_code))

# fh = open("./hwy/hwy.json", "w")
# fh.write(json.dumps(hwy))
# fh.close()
# fr = open("./ramp/ramp.json", "w")
# fr.write(json.dumps(ramp))
# fr.close()
# fr = open("./cross/cross.json", "w")
# fr.write(json.dumps(cross))
# fr.close()
fc = open("./class_code/class_code.json", "w")
fc.write(json.dumps(class_code))
fc.close()


# print("HWY percentage: " + str(hwy_counter) + "/" + str(sample_size))
# print("RAMP percentage: " + str(ramp_counter) + "/" + str(sample_size))
# print("CROSS percentage: " + str(cross_counter) + "/" + str(sample_size))
print("Class Code: " + str(class_code_counter) + "/" + str(sample_size))
print("Success: " + str(success_counter))
print("No Record or Shape: " + str(fail_counter))
