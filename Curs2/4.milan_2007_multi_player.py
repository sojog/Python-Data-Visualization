import matplotlib.pyplot as plt
import matplotlib.image as mpimg


folder_name = "Milan2007"
first_image = folder_name + "/" + "09.Kaka.png"

figure, axis  = plt.subplots(nrows=1, ncols=2)

imagine = mpimg.imread(first_image)
axis[1].imshow(imagine)

plt.show()


