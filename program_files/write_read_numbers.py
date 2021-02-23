from random import randint
import matplotlib.pyplot as plt

# create file writer, if file does not exist it is created
# if file exists it will be overwritten
file = open('integers.txt', 'w')

for i in range(1, 501):
    file.write(str(randint(1, i)) + "\n")
file.close()

integers = []
file = open('integers.txt', 'r')

for value in file.readlines():
    # strip removes \n character
    integers.append(int(value.strip()))
file.close()
# generating a color using rgb values and optional alpha (transparency)
plt.plot(integers, color = (.5, 0, .2, .8))
# needed to display graphs if not in notebook
plt.show()
