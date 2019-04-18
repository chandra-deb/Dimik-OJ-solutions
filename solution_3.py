number = 1000
tracker = []

for i in range(number, 0, -1):
    tracker.append(i)  
    if len(tracker) == 5:
        for j in tracker:
            print(j, end='\t')
        print()
        tracker = []
