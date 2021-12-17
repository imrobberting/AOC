report_str = open('D:\AOC\Input\Q1.txt', 'r').readlines()
report = list(map(int, report_str))

count = 0
dec = 0

for x in range(len(report)-1):
    print(report[x])
    print(report[x+1])
    print("----")
    if report[x+1] > report[x]:
        count += 1
        print(count)
        print("----")
    else:
        dec += 1
        print(dec)
        print("----")
