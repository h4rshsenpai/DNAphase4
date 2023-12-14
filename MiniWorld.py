import subprocess as sp
import pymysql
import pymysql.cursors
import globals
from agent import *
from player import *
from owner import *
from manager import *
from club import *
from coach import *
from seasontournament import *
from stats import *

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """
    # Clubs
    if ch == 11:
        getAllClubs()
    elif ch == 12:
        searchClub()
    elif ch == 13:
        insertClub()
    elif ch == 14:
        getClubPlayersBySeason()
    elif ch == 15:
        getPlayersBoughtByClub()
    elif ch == 16:
        getPlayersSoldByClub()
    elif ch == 17:
        getAllClubTransfers()
    elif ch == 18:
        getClubNetSpent()
    elif ch == 19:
        getClubPerformanceInTournament()
    elif ch == 110:
        deleteClub()
    
    # Players
    elif ch == 21:
        getAllPlayers()
    elif ch == 22:
        searchPlayer()
    elif ch == 23:
        insertPlayer()
    elif ch == 24:
        getAllPlayersByCountry()
    elif ch == 25:
        updatePlayerNationality()
    elif ch == 26:
        getPlayerStatsBySeason()
    elif ch == 27:
        getAllPlayersByStat()
    elif ch == 28:
        getPlayerStatsPer90()
    elif ch == 29:
        getPlayerCareerStats()
    elif ch == 210:
        deletePlayer()
    
    # Managers
    elif ch == 31:
        getAllManagers()
    elif ch == 32:
        insertManager()
    elif ch == 33:
        updateManagerClub()
    elif ch == 34:
        updateManagerNationality()
    elif ch == 35:
        getAllManagersByStat()
    elif ch == 36:
        deleteManager()

    # Agents
    elif ch == 41:
        getAllAgents()
    elif ch == 42:
        insertAgent()
    elif ch == 43:
        updateAgentNationality()
    elif ch == 44:
        deleteAgent()
    
    # Coaches
    elif ch == 51:
        getAllCoaches()
    elif ch == 52:
        insertCoach()
    elif ch == 53:
        updateCoachNationality()
    elif ch == 54:
        deleteCoach()   

    # Owners
    elif ch == 61:
        getAllOwners()
    elif ch == 62:
        insertOwner()
    elif ch == 63:
        updateOwnerNationality()
    elif ch == 64:
        deleteOwner()
    
    # Seasons and Tournaments
    elif ch == 71:
        insertSeason()
    elif ch == 72:
        getAllTournaments()
    elif ch == 73:
        getTournamentTeamsBySeason()

    # Other stats
    elif ch == 81:
        getTransfersByPriceRange()
    elif ch == 82:
        getMaxGoalsPlayerInSeason()
    elif ch == 83:
        getMaxAssistsPlayerInSeason()
    elif ch == 84:
        getMostYellowCardsPlayerInSeason()

    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)

    try:
        us = input("Enter username : ").strip()
        pwd = input("Enter password : ")
        globals.con = pymysql.connect(host='localhost',
                              user= us,
                              password= pwd,
                              db= 'FOOTBALL',
                              port=3306,
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(globals.con.open):
            print("Connected")
        else:
            print("Failed to connect")

        print("Enter any key to CONTINUE or press Q to quit:")
        tmp = input().strip()
        
        if tmp == "Q":
            globals.con.close()
            break

        with globals.con.cursor() as globals.cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                
                # The options presented for database operation
                ch = ""
                print("Enter 0 to Log out")
                print("Select category:")
                print("1. Clubs")
                print("2. Players")
                print("3. Managers")
                print("4. Agents")
                print("5. Coaches")
                print("6. Owners")
                print("7. Seasons and Tournaments")
                print("8. Other Stats")

                ch1 = int(input().strip())
                if ch1 > 8 or ch1 < 0:
                    print("Invalid input")
                    continue

                if ch1 == 0:
                    break
                
                sp.call('clear', shell=True)
                print("Select query:")
                if ch1 == 1:
                    # Clubs
                    print("1. Show all clubs")
                    print("2. Search club")
                    print("3. Insert club")
                    print("4. Display Squad of a Club")
                    print("5. Display Transfer in of a club")
                    print("6. Display Transfer out of a club")
                    print("7. Display all Transfer of a club")
                    print("8. Return Net Spent of a Club")
                    print("9. Show Club results in a tournament")
                    print("10. Delete Club")
                    
                    ch2 = int(input().strip())
                    if ch2 > 10 or ch2 < 1:
                        print("Invalid input")
                        continue


                elif ch1 == 2:
                    # Players
                    print("1. Show all players")
                    print("2. Search player")
                    print("3. Insert player")
                    print("4. Display all players of a country")
                    print("5. Update Nationality of player")
                    print("6. Display Player performance for a season")
                    print("7. Filter players by a given statistic")
                    print("8. Display player stats per 90 minutes")
                    print("9. Display career stats for a given player")
                    print("10. Delete Player")
                    ch2 = int(input().strip())
                    
                    if ch2 > 10 or ch2 < 1:
                        print("Invalid input")
                        continue
                
                elif ch1 == 3:
                    # Managers
                    print("1. Show all managers")
                    print("2. Insert manager")
                    print("3. Update current club of manager")
                    print("4. Update Nationality of manager")
                    print("5. Filter managers by a given statistic")
                    print("6. Delete manager")
                    
                    ch2 = int(input().strip())
                    if ch2 > 6 or ch2 < 1:
                        print("Invalid input")
                        continue

                elif ch1 == 4:
                    # Agents
                    print("1. Show all agents")
                    print("2. Insert agent")
                    print("3. Update Nationality of agent")
                    print("4. Delete agent")

                    ch2 = int(input().strip())
                    if ch2 > 4 or ch2 < 1:
                        print("Invalid input")
                        continue

                elif ch1 == 5:
                    # Coaches
                    print("1. Show all coaches")
                    print("2. Insert coach")
                    print("Update Nationality of coach")
                    print("3. Delete coach")

                    ch2 = int(input().strip())
                    if ch2 > 4 or ch2 < 1:
                        print("Invalid input")
                        continue
                
                elif ch1 == 6:
                    # Owners
                    print("1. Show all owners")
                    print("2. Insert owner")
                    print("3. Update Nationality of owner")
                    print("4. Delete owner")

                    ch2 = int(input().strip())
                    if ch2 > 10 or ch2 < 1:
                        print("Invalid input")
                        continue

                elif ch1 == 7:
                    # Seasons and Tournaments
                    print("1. Insert season")
                    print("2. Show all tournaments")
                    print("3. Display teams in a tournament")

                    ch2 = int(input().strip())
                    if ch2 > 3 or ch2 < 1:
                        print("Invalid input")
                        continue
                
                elif ch1 == 8:
                    # Other stats
                    print("1. Filter transfers by price range")
                    print("2. Show player with most goals")
                    print("3. Show player with most assists")
                    print("4. Show player with most yellow cards")

                    ch2 = int(input().strip())
                    if ch2 > 5 or ch2 < 1:
                        print("Invalid input")
                        continue
                    
                ch = int(str(ch1) + str(ch2))
                dispatch(ch)
                tmp = input("Enter any key to CONTINUE>")

            
        globals.con.close()

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
