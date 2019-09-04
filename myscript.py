# libraries
from collections import Counter
import matplotlib.pyplot as plt 

# open files
file = open("home_ownership_data.csv", 'r')
ownership = file.read()
file.close()
file = open("loan_data.csv", 'r')
loan = file.read()
file.close()

# parsing
rows = ownership.split('\n')[1:]
del rows[len(rows)-1]
ownerlist = [row.split(',') for row in rows]

rows = loan.split('\n')[1:]
del rows[len(rows)-1]
loandict = dict([row.split(',')[:2] for row in rows])

avg = Counter()
count = Counter()

# averaging out for each loan type
for owner in ownerlist:
    avg[owner[1]] += int(loandict[owner[0]])
    count[owner[1]] += 1

for key in avg:
    avg[key] /= count[key]

plt.bar([1, 2, 3], avg.values())
plt.title('Average loan amounts for home ownership')
plt.xlabel('Home ownership')
plt.ylabel('Average loan amount ($)')
plt.show()