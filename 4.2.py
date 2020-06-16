import math
import numpy as np
import matplotlib.pyplot as plt

x = 1000
a = 24693
c = 3967
K = 2**17

uVal = []
count = 0
itterations = 300000
while count < itterations:

    x = (a * x + c) % K
    uVal.append(x / K)

    count = count + 1

# for i in uVal:
#     print(i)

mN = [10, 30, 50, 100, 150, 250, 500, 1000]
results = []


for n in mN:
    for iid in range(0, 110):
        tempResults = []
        for w in range(0, n):
            tempResults.append((n,
                                math.sqrt((-2 * math.log(1 - uVal.pop(0))) / ((1 / 57)**2))))
        results.append((n, sum([pair[1] for pair in tempResults]) / n))  # M_n

ycord = [pair[1] for pair in results]
print("Average: ", np.mean(ycord))
print("Sqrt of Standard Deviation: ", math.sqrt(np.std(ycord)))

count = 0
for point in ycord:
    if point - np.mean(ycord) < 10:
        count += 1

print("Probability of p: " + str(count / 880))
i=0
with open('results.txt', 'w') as file:
    file.write('\n'.join(str(value) for value in results[:-1:]))
    i+=1

plt.rc('font', family='serif')
plt.title('Mean over Sample Size')
plt.scatter(*zip(*results))
plt.axhline(np.mean(ycord), color='black')
plt.axhline(np.mean(ycord) - 10, color='black')
plt.axhline(np.mean(ycord) + 10, color='black')
plt.ylabel(r'$M_n(x)$')
plt.xlabel(r'$n$')
plt.xticks(np.arange(0, 1000, 50))
plt.show()

# Print out all results
# count = 0
# for i in results:
#     print(str(count) + ": " + str(i))
#     count += 1