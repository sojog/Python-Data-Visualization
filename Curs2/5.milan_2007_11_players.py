import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

folder_name = "Milan2007"
# print(os.listdir(folder_name))
file_list = os.listdir(folder_name)
file_list.sort()
file_list = file_list[:11]


figure, axis  = plt.subplots(nrows=1, ncols=11)

for index, file_name in enumerate(file_list):
    imagine = mpimg.imread(folder_name + "/" + file_name)
    axis[index].imshow(imagine)
    axis[index].axis("off")

plt.show()


