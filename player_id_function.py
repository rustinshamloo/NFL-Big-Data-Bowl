
# edit in here, run in terminal, save/push to git on terminal:
#1. git add .
#2. git commit -m "message"
#3. git push

# create function that returns player characteristics (height,weight,etc.) with playerid as input
# the data is in players.csv
# use score function as ex, find all chrs. and turn them into a list
# might have to convert from str to flt, etc.


import csv
# This function returns the characteristics of a player given the nfl id.
def stats(nflId):
    with open('../nfl-big-data-bowl-2021/players.csv') as f:
        mycsv = csv.reader(f)
        for row in mycsv:
            #print(row)
            playerid = row[0]
            if(playerid == nflId):
                player = row
                return [str(player[6]), str(player[1]), str(player[2]), str(player[3]),
                str(player[4]), str(player[5])]
##print(stats(#input nflId))
            
#NOT ALL ARE DEFENSIVE PLAYERS - CLEAN UP: make an array with defensive players
#is this position included in defensive player array? if yes, include. if no, dont 


#next, create function that returns their playerid's, similar to all game ids function



def all_player_ids():
    player_ids = []
    with open('../nfl-big-data-bowl-2021/players.csv') as f:
        mycsv = csv.reader(f)
        for row in mycsv:
            if(row[0] not in player_ids):
                player_ids.append(row[0])
    return player_ids

print(all_player_ids())


#for height - go through each one
# does this cell contain a dash?
#if yes, take number to left of dash, X 12, + to right of dash (might be a separate function)
# birth dates - python package - import dates to find "age today"?
#if not, parse through every time there's 4 digits following each other in a row, then you subtract that from 2020


