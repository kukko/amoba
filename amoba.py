import os
import platform
import sys
def drawTable():
	rendszer=platform.system()
	if (rendszer=="Windows"):
		os.system('cls')
	elif(rendszer=="Linux"):
		os.system('clear')
	rendszer=platform.system()
	print(("{:<"+str(len(str(width))-1)+"}").format("")+"  "+"   ".join([str(i+1) for i in range(0, width)]))
	print((("{:<"+str(len(str(width))-1)+"}").format("")+" "+"+".join(["---" for j in range(0, width)])+"\n").join([("{:<"+str(len(str(width)))+"}").format(str(i+1))+" "+" | ".join(table[i])+"\n" for i in range(0, height)]))
def isWin(char):
	for x in range(0, width):
		cnt=0
		for y in range(0, height):
			if (table[y][x]==char):
				cnt+=1
				if (cnt==winSize):
					return True
			else:
				cnt=0
	for y in range(0, height):
		cnt=0
		for x in range(0, width):
			if (table[y][x]==char):
				cnt+=1
				if (cnt==winSize):
					return True
			else:
				cnt=0
	for y in range(0, height):
		for x in range(0, width):
			cnt=0
			for i in range(0, height-y if height-y<width-x else width-x):
				if (table[y+i][x+i]==char):
					cnt+=1
					if (cnt==winSize):
						return True
				else:
					cnt=0
players=["X", "O"]
width=int(input("Milyen széles legyen a pálya?"))
height=int(input("Milyen magas legyen a pálya?"))
winSize=0
while (winSize<=0 or (winSize>width and winSize>height)):
	winSize=int(input("Hány egybefüggő formát kelljen elérni?"))
	if (winSize>width and winSize>height):
		print("Ekkora egybefüggő forma nem lehetséges ezen a táblán! Szélesség: "+str(width)+" Magasság: "+str(height))
table=[[" " for j in range(0, width)] for i in range(0, height)]
drawTable()
lepesek=0
playerID=0
while (lepesek<width*height):
	currentPlayer=players[playerID]
	x, y=[int(i) for i in str(input("Hova szeretnél rakni? Szóközzel elválasztva írd be a koordinátákat! ("+str(lepesek+1)+")")).split(" ")]
	x-=1
	y-=1
	if (table[y][x]==" "):
		table[y][x]=currentPlayer
		drawTable()
		if (isWin(currentPlayer)):
			print("GYŐZTES: "+currentPlayer)
			sys.exit(0)
		lepesek+=1
		playerID+=1
		if (playerID>=len(players)):
			playerID=0
	else:
		drawTable()
input("")
