inventory=["sword","shield","-","-"]
map=[["f1","f2","f3","f4","f5","f6","roof"]
     ,["enterance","shop","training","outlook","street","town","home"]]
items=[["","","","","","",""]
     ,["","","","","","coin","sword"]]
playerx=6
playery=1

def move(direction, playerx, playery):
    if direction=="west":
        if playerx>0:
            playerx-=1  
    elif direction=="east":
        if playerx<6:
            player+=1
    elif direction=="north":
        if map[playery][playerx]=="enterance":
            playery-=1
    elif direction=="south":
        if map[playery][playerx]=="f1":
            playery+=1
    else:
        print("Cannot move there!")
        print(direction)
    print("You are at "+str(map[playery][playerx])+".")

def upgrade (inventory,size):
    newinventory=[]
    if size>len(inventory):
        for i in range(size):
            if i<len(inventory):
                newinventory.append(inventory[i])
            else:
                newinventory.append("-")
    return newinventory

game=True

while game:
    text=input("> ")
    command=text.split()
    print (command)
    if "move" in text:
        move(command[1],playerx,playery)
# move("west", playerx, playery)
# move("east", playerx, playery)
# print (upgrade(inventory,6))