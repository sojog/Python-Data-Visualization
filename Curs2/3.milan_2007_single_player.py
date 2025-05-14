import matplotlib.pyplot as plt
import matplotlib.image as mpimg


folder_name = "Milan2007"
first_image = folder_name + "/" + "09.Kaka.png"

figure, axis  = plt.subplots()

imagine = mpimg.imread(first_image)
axis.imshow(imagine)

plt.show()


