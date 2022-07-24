if __name__ == '__main__':
    data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        data.append([name, score])
        
    sorted_score = []
    for x, y in data:
        sorted_score.append(y)
    sorted_score = sorted(set(sorted_score))
    second_lowest = sorted_score[1]
    
    sorted_name = []
    for x, y in data:
        if y == second_lowest:
            sorted_name.append(x)
    sorted_name = sorted(sorted_name)
    
    for i in sorted_name:
        print(i)
   

   #assets/9-NestedLists/2022-07-24-14-14-05.png