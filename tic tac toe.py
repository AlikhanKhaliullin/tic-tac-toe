fields=[["-","-","-"], ["-","-","-"], ["-","-","-"]]
def show():
    print(f"""
  0 1 2
0 {fields[0][0]} {fields[0][1]} {fields[0][2]}
1 {fields[1][0]} {fields[1][1]} {fields[1][2]}
2 {fields[2][0]} {fields[2][1]} {fields[2][2]}
""")
global x
global y
def wincheck():
    windesk=[[0,0,0,1,0,2],[1,0,1,1,1,2],[2,0,2,1,2,2],[0,0,1,0,2,0],[0,1,1,1,2,1],[0,2,1,2,2,2],[0,0,1,1,2,2],[2,0,1,1,0,2]]
    for i in windesk:
        if fields[i[0]][i[1]] == fields[i[2]][i[3]]==fields[i[4]][i[5]] and fields[i[0]][i[1]]!="-":
            print(f"win {fields[i[0]][i[1]]}")
            break
def repeate(x,y,c):
    if fields[x][y] == "x" or fields[x][y] == "o":
        print("Уже занято")
        while True:
            x=int(input())
            y=int(input())
            if fields[x][y] == "x" or fields[x][y] == "o":
                print("Уже занято")
            else:
                break
    fields[x][y]=c

show()

while True:
    print("ВВодят x")
    x=int(input())
    y=int(input())
    repeate(x,y,"x")
    show()
    wincheck()
    print("ВВодят y")
    x=int(input())
    y=int(input())
    repeate(x,y,"o")
    show()
    wincheck()
