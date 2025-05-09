import matplotlib.pyplot as plt

print(plt.__doc__)


lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

plt.plot(lista_1, lista_2);

# Instructiunea show trebuie sa existe in fisierele de tip .py, altfel nu se ruleaza
plt.show()