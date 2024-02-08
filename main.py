inventory=[]
map=[["f1","f2","f3","f4","f5","f6","roof"]
     ,[["enterance"],["shop"],["training"],["outlook"],["street"],["town"],["home"]]]
playerx=6
playery=1

def move(direction):
    if direction=="west":
        if playerx>0:
            playerx-=1  
    elif direction=="east":
        if playerx<6:
            player+=1
    elif direction=="north":
        if map[playerx][playery]=="enterance":
            playery-=1
    elif direction=="south":
        if map[playerx][playery]=="f1":
            playery+=1
    print(playerx)
    print(playery)

move("west")