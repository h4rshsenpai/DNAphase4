import globals
from columnar import columnar
from validators import *

def getTransfersByPriceRange():
    try:
        low = int(input("Enter minimum price:").strip())
        high = int(input("Enter maximum price:").strip())
        query = "SELECT PLAYER.player_name,CLUB_FROM.club_name,CLUB_TO.club_name,AGENT.name,transfer_fee,agent_fee,date_of_transfer\
                FROM TRANSFER\
                INNER JOIN PLAYER ON TRANSFER.player_id=PLAYER.player_id\
                INNER JOIN CLUB CLUB_FROM ON TRANSFER.club_from_id=CLUB_FROM.club_id\
                INNER JOIN CLUB CLUB_TO ON TRANSFER.club_to_id=CLUB_TO.club_id\
                INNER JOIN AGENT ON TRANSFER.agent_id=AGENT.agent_id\
                WHERE transfer_fee>=%d AND transfer_fee<=%d" % (low, high)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ["Name", "From", "To", "Agent", "Transfer fee", "Agent Fee", "Transfer"]
        data = []
        for res in result:
            data.append(list(res.values()))
        table = columnar(data, headers)
        print(table)
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False


def getMaxGoalsPlayerInSeason():
    try:
        season = input("Enter the season you are interested in : ").strip()
        if(ValidateSeasonYear(season) == False):
            print("Season year given is wrong")
            return False
        query = "SELECT * FROM PLAYED_FOR WHERE season_year = '%s' " % (season)
        globals.cur.execute(query)
        res = globals.cur.fetchall()
        size = len(res)
        if(size == 0):
            print("Info for the given season doesnot exist")
            return False
        query = "SELECT MAX(goals) AS z FROM PLAYED_FOR WHERE season_year = '%s'" % (season)
        globals.cur.execute(query)
        res = globals.cur.fetchone()
        query = "SELECT player_id,club_id,goals FROM PLAYED_FOR WHERE season_year = '%s' AND goals = %d " % (season,int(res["z"]))
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        data = []
        headers = ['player_name','club_name','goals']
        for r in result:
            ll = {}
            query = "SELECT player_name FROM PLAYER WHERE player_id = %d " % (int(r["player_id"]))
            globals.cur.execute(query)
            t = globals.cur.fetchone()
            ll["player_name"] = t["player_name"]
            query = "SELECT club_name FROM CLUB WHERE club_id = %d " % (int(r["club_id"]))
            globals.cur.execute(query)
            t = globals.cur.fetchone()
            ll["club_name"] = t["club_name"]
            ll["goals"] = r["goals"]
            resll = list(ll.values())
            data.append(resll)

        table = columnar(data,headers)
        print(table)
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False


def getMaxAssistsPlayerInSeason():
    try:
        season = input("Enter the season you are interested in : ").strip()
        if(ValidateSeasonYear(season) == False):
            print("Season year given is wrong")
            return False
        query = "SELECT * FROM PLAYED_FOR WHERE season_year = '%s' " % (season)
        globals.cur.execute(query)
        res = globals.cur.fetchall()
        size = len(res)
        if(size == 0):
            print("Info for the given season doesnot exist")
            return False
        query = "SELECT MAX(assists) AS z FROM PLAYED_FOR WHERE season_year = '%s'" % (season)
        globals.cur.execute(query)
        res = globals.cur.fetchone()
        query = "SELECT player_id,club_id,assists FROM PLAYED_FOR WHERE season_year = '%s' AND assists = %d " % (season,int(res["z"]))
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        data = []
        headers = ['player_name','club_name','yellow_cards']
        for r in result:
            ll = {}
            query = "SELECT player_name FROM PLAYER WHERE player_id = %d " % (int(r["player_id"]))
            globals.cur.execute(query)
            t = globals.cur.fetchone()
            ll["player_name"] = t["player_name"]
            query = "SELECT club_name FROM CLUB WHERE club_id = %d " % (int(r["club_id"]))
            globals.cur.execute(query)
            t = globals.cur.fetchone()
            ll["club_name"] = t["club_name"]
            ll["assists"] = r["assists"]
            resll = list(ll.values())
            data.append(resll)

        table = columnar(data,headers)
        print(table)
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False


def getMostYellowCardsPlayerInSeason():
    try:
        season = input("Enter the season you are interested in : ").strip()
        if(ValidateSeasonYear(season) == False):
            print("Season year given is wrong")
            return False
        query = "SELECT * FROM PLAYED_FOR WHERE season_year = '%s' " % (season)
        globals.cur.execute(query)
        res = globals.cur.fetchall()
        size = len(res)
        if(size == 0):
            print("Info for the given season doesnot exist")
            return False
        query = "SELECT MAX(yellow_cards) AS z FROM PLAYED_FOR WHERE season_year = '%s'" % (season)
        globals.cur.execute(query)
        res = globals.cur.fetchone()
        query = "SELECT player_id,club_id,yellow_cards FROM PLAYED_FOR WHERE season_year = '%s' AND yellow_cards = %d " % (season,int(res["z"]))
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        data = []
        headers = ['player_name','club_name','yellow_cards']
        for r in result:
            ll = {}
            query = "SELECT player_name FROM PLAYER WHERE player_id = %d " % (int(r["player_id"]))
            globals.cur.execute(query)
            t = globals.cur.fetchone()
            ll["player_name"] = t["player_name"]
            query = "SELECT club_name FROM CLUB WHERE club_id = %d " % (int(r["club_id"]))
            globals.cur.execute(query)
            t = globals.cur.fetchone()
            ll["club_name"] = t["club_name"]
            ll["yellow_cards"] = r["yellow_cards"]
            resll = list(ll.values())
            data.append(resll)

        table = columnar(data,headers)
        print(table)
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False

