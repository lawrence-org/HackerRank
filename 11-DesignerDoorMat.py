size = input().split()
row = int(size[0])
column = int(size[1])

pattern = ".|."
count = 1
for index in range(row):
    if index < int(row/2):
        num = int((column - count*3)/2)
        print('-'*num + pattern*count + '-'*num)
        count += 2
    if index == int(row/2):
        print('-'*int((column-7)/2) + "WELCOME" + '-'*int((column-7)/2))
    if index > int(row/2):
        count -= 2
        num = int((column - count*3)/2)
        print('-'*num + pattern*count + '-'*num)
   
#assets/11-DesignerDoorMat/2022-07-24-18-21-08.png