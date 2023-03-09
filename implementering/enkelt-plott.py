import matplotlib.pyplot as plt

# x = [0, 1, 2, 3, 4, 5]
# y = [0, 2, 4, 6, 8, 10]

# plt.plot(x,y) # oppretter et plot
# plt.show() # viser plottet

# # plott funksjonen f(x) = 3*x + 2, med x fra 0 til 5

# x1 = [0, 1, 2, 3, 4, 5]
# y1 = [2, 5, 8, 11, 14, 17]

# plt.plot(x1,y1)
# plt.show()

x1 = [0, 1, 2, 3, 4, 5]
y1 = []

for tall in x1:
    y1.append(3*tall + 2)

plt.plot(x1,y1) # plot gjør at det blir en linje
plt.scatter(x1,y1) # scatter gjør at det blir punkter
plt.show()