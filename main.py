inventory=["-","-","-","-"]
map=[["f1","f2","f3","f4","f5","f6","roof"]
     ,["enterance","shop","training","outlook","street","town","home"]]
items=[["","","","","","",""]
     ,["","","","","","coin","sword"]]
playerx=6
playery=1

def move(direction):
    global playerx
    global playery
    if direction=="west":
        if playerx>0:
            playerx-=1  
    elif direction=="east":
        if playerx<6:
            playerx+=1
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
    print (playerx)
    print(playery)


def upgrade (inventory,size):
    newinventory=[]
    if size>len(inventory):
        for i in range(size):
            if i<len(inventory):
                newinventory.append(inventory[i])
            else:
                newinventory.append("-")
    return newinventory

def pickup(item):
    global inventory
    for i in inventory:
        if i=="-":
            if item not in inventory:
                inventory[i]=item
        #     else:
        #         print("already found")
        # else:
        #     print("no space")
    print(inventory)
    return inventory

game=True

while game:
    text=input("> ")
    command=text.split()
    if "move" in text:
        move(command[1])
    elif "look" in text:
        print("You look around, and find a "+items[playery][playerx]+".")
    elif "pickup" in text:
        pickup(items[playery][playerx])
    elif "inventory" in text:
        print (inventory)
    elif "buy" in text:
        if "coin" in inventory:
            if playery==1 and playerx==1:
                upgrade(inventory,6)
    elif "say" in text:
        if command[1]== "password":
            if playerx==2 and playery==0:
                upgrade(inventory,8)


                
# move("west", playerx, playery)
# move("east", playerx, playery)
# print (upgrade(inventory,6))