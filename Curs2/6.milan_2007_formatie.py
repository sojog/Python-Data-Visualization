import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

folder_name = "Milan2007"
# print(os.listdir(folder_name))
file_list = os.listdir(folder_name)
file_list.sort()
file_list = file_list[:11]

##     1
##    1 1 
##   1 1 1
##  1 1 1 1
##     1
figure, axis  = plt.subplots(nrows=5, ncols=7)


layout_jucatori = [
    [None] * 3 + [file_list[10]] + [None] * 3,
    [None] * 2 + [file_list[8]] + [None] + [file_list[9]] +  [None] * 2,
    [None] + [file_list[5]] + [None] + [file_list[6]] +  [None] + [file_list[7]] + [None],
    [file_list[1]] + [None] + [file_list[2]] +  [None] + [file_list[3]] + [None] + [file_list[4]] ,
    [None] * 3 + [file_list[0]] + [None] * 3,
]


for index_row, row in enumerate(layout_jucatori):
    for index_col, column in enumerate(row):
        file_name = layout_jucatori[index_row][index_col]
        if file_name:
            full_file_name = folder_name + "/" + file_name
            imagine = mpimg.imread(full_file_name)
            axis[index_row, index_col].imshow(imagine)
        axis[index_row, index_col].axis("off")
        


plt.show()