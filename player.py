import globals
from validators import *
from columnar import columnar

def getPositions(player_id):
    try:
        positions = ""
        q = "SELECT position_name FROM POSITIONS WHERE player_id=%d" % (player_id)
        globals.cur.execute(q)
        result = globals.cur.fetchall()
        for pos in result:
            positions += pos["position_name"] + " "
        return positions
    except:
        return ""

def getAllPlayers():
    try:
        query = "SELECT * FROM PLAYER"
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ['Player ID', 'Name', 'DOB', 'Nationality', 'Agent Name', 'Positions']
        data = []
        for res in result:
            agent_id = res["agent_id"]
            try:
                q = "SELECT name FROM AGENT WHERE agent_id=%d" % (agent_id)
                globals.cur.execute(q)
                res["agent_id"] = globals.cur.fetchone()["name"]
            except:
                res["agent_id"] = ""
            res["positions"] = getPositions(res["player_id"])
            reslist = list(res.values())
            data.append(reslist)
        table = columnar(data, headers)
        print(table)
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False

def getAllPlayersByStat():
    # return all players filtered by a stat
    try:
        print("Select which statistic to use:")
        print("1. Goals")
        print("2. Assists")
        print("3. Saves")
        print("4. Tackles")
        print("5. Clearances")
        print("6. Red Cards")
        print("7. Yellow Cards")
        print("8. Minutes played")
        
        ch = int(input().strip())
        if ch > 8 or ch < 1:
            print("Invalid choice")
            return False
        
        low = int(input("Enter lower bound:").strip())
        high = int(input("Enter upper bound:").strip())

        season_year = input("Enter season year:").strip()

        stats = ["", "goals", "assists", "saves", "tackles", "clearances", "red_cards", "yellow_cards", "minutes_played"]
        query = "SELECT PLAYER.player_name,minutes_played,goals,assists,clearances,tackles,red_cards,yellow_cards,saves FROM PLAYER INNER JOIN PLAYED_FOR ON PLAYED_FOR.player_id=PLAYER.player_id AND %s>=%d AND %s<=%d AND season_year='%s'" % (stats[ch], low, stats[ch], high, season_year)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ["Name", "Minutes played", "Goals", "Assists", "Clearances", "Tackles", "Red cards", "Yellow cards", "Saves"]
        data = []
        for res in result:
            data.append(list(res.values()))
        table = columnar(data, headers)
        print(table)
        return True
    
    except Exception as e:
        print("Failed to retreive from database")
        print(">>>>>>>>>>>>>", e)
        return False


def getAllPlayersByCountry():
    try:
        cnt = input("Enter the countries whose players you want : ").strip()
        query = "SELECT * FROM PLAYER WHERE nationality = '%s'" % (cnt)
        globals.cur.execute(query)
        res = globals.cur.fetchall()
        headers = ['player_name','player_id','date_of_birth']
        l1=[]
        for z in res:
            lz = list(z.values())
            l1.append(lz)
        table = columnar(l1,headers)
        print(table)
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False



def updatePlayerNationality():
    try:
        player_id = int(input("Enter player ID:"))
        q = "SELECT * FROM PLAYER WHERE player_id=%d" % (player_id)
        globals.cur.execute(q)
        player = globals.cur.fetchone()
        if player is None:
            print("Not found")
            return False
        newNationality = input("Enter new nationality:")
        if not ValidateNationality(newNationality):
            print("Not a valid nationality")
            return False
        query = "UPDATE PLAYER SET nationality='%s' WHERE player_id=%d" % (newNationality, player_id)
        globals.cur.execute(query)
        globals.con.commit()

        print("Nationality updated")
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to update")
        print(">>>>>>>>>>>>>", e)
        return False

def searchPlayer():
    try:
        name = input("Enter search term:")
        name = '%' + name + '%'
        query = "SELECT * FROM PLAYER WHERE player_name LIKE '%s'" % name
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ['Player ID', 'Name', 'DOB', 'Nationality', 'Agent Name', 'Positions']
        data = []
        for res in result:
            agent_id = res["agent_id"]
            try:
                q = "SELECT name FROM AGENT WHERE agent_id=%d" % (agent_id)
                globals.cur.execute(q)
                res["agent_id"] = globals.cur.fetchone()["name"]
            except:
                res["agent_id"] = ""
            res["positions"] = getPositions(res["player_id"])
            reslist = list(res.values())
            data.append(reslist)
        table = columnar(data, headers)
        print(table)
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False

def insertPlayer():
    try:
        row = {}
        print("Enter Player's details: ")
        row["player_name"] = input("Enter name:")
        row["date_of_birth"] = input("Enter Date of Birth (YYYY-MM-DD):")
        if(ValidateDate(row["date_of_birth"]) == False):
            print("Not a valid Date")
            return False
        row["nationality"] = input("Enter nationality:")
        if(ValidateNationality(row["nationality"])== False):
            print("Not a valid Nationality")
            return False
        row["agent_id"] = input("Enter the agent_id :")
        globals.cur.execute('SELECT * FROM AGENT')
        temp = globals.cur.fetchall()
        flag = False
        for i in temp:
            if(int(i["agent_id"]) == int(row["agent_id"])):
                flag = True
                break
        if(flag == True):
            query = "INSERT INTO PLAYER (player_name, date_of_birth, nationality, agent_id) VALUES ('%s', '%s', '%s', %s)" %  (row["player_name"], row["date_of_birth"], row["nationality"], row["agent_id"])
            print(query)
            globals.cur.execute(query)
            globals.con.commit()
            print("Inserted Player into database")
            return True
        else:
            
            print("Agent Id given is wrong")
            return False

    except Exception as e:
        globals.con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return False

def getPlayerStatsBySeason():
    try:
        player_id = int(input("Enter player id:"))
        season_year = input("Enter season year:")
        query = "SELECT PLAYER.player_name,minutes_played,goals,assists,clearances,tackles,red_cards,yellow_cards,saves FROM PLAYER INNER JOIN PLAYED_FOR ON PLAYER.player_id=%d AND season_year='%s'" % (player_id, season_year)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ["Name", "Minutes played", "Goals", "Assists", "Clearances", "Tackles", "Red cards", "Yellow cards", "Saves"]
        data = []
        for res in result:
            data.append(list(res.values()))
        if len(data) > 0:
            for i in range(1,len(data)):
                for j in range(1,9):
                    data[0][j] += data[i][j]
            data = data[0:1]
        table = columnar(data, headers)
        print(table)
    
    except Exception as e:
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False

def getPlayerStatsPer90():
    try:
        print("Select which statistic to show:")
        print("1. Goals")
        print("2. Assists")
        print("3. Saves")
        print("4. Tackles")
        print("5. Clearances")
        print("6. Red Cards")
        print("7. Yellow Cards")
        
        ch = int(input())
        if ch > 7 or ch < 1:
            print("Invalid choice")
            return False

        player_id = int(input("Enter player ID:"))
        season_year = input("Enter season year (20XX-YY):")

        stats = ["", "goals", "assists", "saves", "tackles", "clearances", "red_cards", "yellow_cards"] 
        
        query = "SELECT PLAYER.player_name,SUM(%s),SUM(minutes_played)\
                FROM PLAYED_FOR\
                INNER JOIN PLAYER ON PLAYED_FOR.player_id = PLAYER.player_id\
                WHERE PLAYER.player_id=%d AND PLAYED_FOR.season_year='%s'" % (stats[ch], player_id, season_year)
        
        globals.cur.execute(query)
        result = globals.cur.fetchone()
        try:
            data = list(result.values())
            data[1] = data[1] = 90 * data[1] / data[2]
            data = [data[0:2]]
        except:
            print("No results found")
            return False
        headers = ["Name", stats[ch] + " per90"]
        table = columnar(data, headers)
        print(table)
        return True
    
    except Exception as e:
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False

def getPlayerCareerStats():
    try:
        print("Select which statistic to show:")
        print("1. Goals")
        print("2. Assists")
        print("3. Saves")
        print("4. Tackles")
        print("5. Clearances")
        print("6. Red Cards")
        print("7. Yellow Cards")
        print("8. Minutes played")
        
        ch = int(input())
        if ch > 8 or ch < 1:
            print("Invalid choice")
            return False

        player_id = int(input("Enter player ID:"))

        stats = ["", "goals", "assists", "saves", "tackles", "clearances", "red_cards", "yellow_cards", "minutes_played"] 
        
        query = "SELECT PLAYER.player_name,SUM(%s)\
                FROM PLAYED_FOR\
                INNER JOIN PLAYER ON PLAYED_FOR.player_id = PLAYER.player_id\
                WHERE PLAYER.player_id=%d" % (stats[ch], player_id)
        
        globals.cur.execute(query)
        result = globals.cur.fetchone()
        data = [list(result.values())]
        headers = ["Name", "career " + stats[ch]]
        table = columnar(data, headers)
        print(table)
        return True
    
    except Exception as e:
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False

def deletePlayer():
    try :
        x = int(input("Enter player_id of the Player to be deleted :"))
        query1 = "DELETE FROM PLAYED_FOR WHERE player_id = %d " % (x)
        query = "DELETE FROM PLAYER WHERE player_id = %d " % (x)
        query2 = "DELETE FROM TRANSFER WHERE player_id = %d " % (x)
        query3 = "DELETE FROM POSITIONS WHERE player_id = %d " % (x)
        
        globals.cur.execute(query1)
        globals.cur.execute(query2)
        globals.cur.execute(query3)
        globals.cur.execute(query)

        globals.con.commit()
        print("Player Deleted")
        return True
    except Exception as e:
        globals.con.rollback()
        print("Failed to Delete")
        print(">>>>>>>>>>>>>", e)
        return False

