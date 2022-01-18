import random as rd
import math
import statistics
def genie(prob, choice):
    k = rd.randrange(0, 100)
    if k <= prob:
        if choice == 'B':
            M = 1000000
        else:
            M = 0
    else:
        if choice == 'B':
            M = 0
        else:
            M = 1000000
    return M
def main():
    choice = ['B', 'AB']
    n = math.floor(rd.randrange(0,2))
    M = genie(90, choice[n])
    money = [M, 1000 + M]
    earning = money[n]
    return [choice[n], earning]
def export():
    data = main()
    with open('data_newcomb.txt', 'r') as f:
        existingData = f.read()
        f.close()
    with open('data_newcomb.txt', 'w') as f:
        f.write(existingData + '\n' + str(data[0]) + '\t\t'+ str(data[1]))
        f.close()
def run():
    with open('data_newcomb.txt','w') as f:
        f.write('Choice' + '\t' + 'Earning')
        f.close()
    for i in range(10000):
        export()
 
def analyse():
    choice = []
    earning = []
    logic = []
    with open('data_newcomb.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            choice.append(line[:2].strip())
            earning.append(line[2:].strip())
        f.close()
    choice.pop(0)
    earning.pop(0)
  
    with open('data_newcomb.txt', 'a') as f:
        f.write('\n\n' + 'B: ' + str(choice.count('B')) + '\n' + 'AB: ' + str(choice.count('AB')))
        f.close()
    B = []
    AB = []
    for i in range(len(choice)):
        if choice[i] == 'B':
            B.append(int(earning[i]))
        else:
            AB.append(int(earning[i]))
    with open('data_newcomb.txt', 'a') as f:
        f.write('\n\n' + 'Mean earning (Expected Utility): ' + str(statistics.mean(B)) + '\n' + 'Mean earning (Strategical Dominance): ' + str(statistics.mean(AB)))
        f.write('\n\n' + 'Standard Deviation (Expected Utility): '+ str(statistics.stdev(B)) + '\n' + 'Standard Deviation (Strategical Dominance): ' + str(statistics.mean(AB)))
        f.close()
run()
analyse()
