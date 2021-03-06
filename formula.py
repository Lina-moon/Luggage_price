import numpy as np
import csv
import math

"""
The formula itself
"""
def culcarea(a, b_1, x_1):
    answer = float((np.log(math.exp(a+b_1 * x_1)) - b_1 * x_1 * np.log(math.fabs(x_1))) / (x_1 * (np.log(math.exp(a+b_1 * x_1)))))
    return answer

def csv_reader(file_obj):
    """
    Read a csv file
    and put all its values in the formula
    """
    reader = csv.reader(file_obj)
    global huge
    huge = (float(0))
    cost = 0
    for row in reader:
        smaler = culcarea(variables[1], variables[2], float(row[0])*variables[3])
        if smaler > huge:
            huge = smaler
            cost = row[0]
    return cost


def WTP_culc(x_1, b_1, a):
    answer = float(1/(a+x_1*b_1))
    return answer


def Revenue_culc(MS, WTP, Price):
        revenue = math.exp(MS) * math.exp(WTP) * math.exp(Price)
        return revenue


""" /// Obtaining data from txt file ///  """

indata = open('input.txt', 'r')
kprice = alpha = betta = knumber = MS = float(0);
variables = [kprice, alpha, betta, knumber, MS]
lines =[]
for text in indata:
    lines += str(text)
indata.close
for i in range(6):
    start = lines.index('[')
    end = lines.index(']')
    j = start + 1
    if i!=0 :
        s =""
        while j != end:
            s +=lines[j]
            j+=1
        variables[i-1] = float(s)
    lines.pop(start)
    lines.pop(end-1)

# Check of the variables:

for i in range(5):
    print(variables[i])

# Creation of the CSV file:

a = []
for i in range(10000):
    a.append(np.random.uniform(variables[0]-(0.6), variables[0]+(0.6)))
np.savetxt('distribution.csv', a, delimiter=',', fmt='%f')

# Open CSV:
csv_path = "distribution.csv"
with open(csv_path, "r") as f_obj:
    variables[0] = csv_reader(f_obj)

print("Optimal cost is: ", variables[0])
Price = np.log(variables[3] * float(variables[0]))
print("Optimized revenue is: ", Revenue_culc(np.log(variables[4]), WTP_culc(Price, variables[2], variables[1]), Price))
