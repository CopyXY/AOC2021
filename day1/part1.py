with open(r'C:\Users\shagg\AOC2021\day1\input.txt') as f:
    lines = f.read().splitlines()
    count = 0
    for i in range(0, len(lines)):
         
        if i  > 0:
            # print(lines[i], lines[i-1], lines[i] > lines[i-1])
            if lines[i] > lines[i-1]: 
              
                count += 1
        else:
            print(i)
    
    print(count)