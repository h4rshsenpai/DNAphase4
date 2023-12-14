import globals
from validators import *
from columnar import columnar

def getAllClubs():
    try:
        query = "SELECT * FROM CLUB"
        #print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ['Club ID', 'Name', 'Home Ground', 'Foundation Year', 'Street Address', 'Zip Code', 'City', 'Country']
        data = []
        for res in result:
            try:
                q = "SELECT * FROM ZIP_MAP WHERE zip_code='%s'" % (res["zip_code"])
                globals.cur.execute(q)
                zip_map = globals.cur.fetchone()
                res["city"] = zip_map["city"]
                res["country"] = zip_map["country"]
            except:
                res["city"] = ""
                res["country"] = ""
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

def insertClub():
    try:
        row = {}
        print("Enter Club details: ")
        row["club_name"] = input("Enter club name:").strip()
        row["foundation_year"] = input("Enter Foundation year of club:").strip()
        row["city"] = input("Enter the City the club belongs to:").strip()
        row["street_address"] = input("Enter the street Address of the club headquarters:").strip()
        row["zip_code"] = input("Enter the zip code of the club headquarters:").strip()
        row["home_ground"] = input("Enter the home ground :").strip()
        row["country"] = input("Enter the home country:").strip()
        if(ValidateNationality(row["country"])== False):
            print("Not a valid Country Name")
            return False
        
        globals.cur.execute('SELECT * FROM ZIP_MAP')
        temp = globals.cur.fetchall()
        flag = False
        for t in temp:
            if((t["zip_code"]) == (row["zip_code"])):
                flag = True
                break
        if(flag == False):
            query1 = "INSERT INTO ZIP_MAP (zip_code,city,country) VALUES ('%s', '%s', '%s')" % (row["zip_code"],row["city"],row["country"])        
            print(query1)
            globals.cur.execute(query1)
            globals.con.commit()
        query = "INSERT INTO CLUB (club_name,home_ground,foundation_year,zip_code,street_address) VALUES ('%s', '%s', '%s', '%s', '%s')" %  (row["club_name"], row["home_ground"], row["foundation_year"], row["zip_code"],row['street_address'])
        print(query)
        globals.cur.execute(query)
        globals.con.commit()
        print("Inserted CLUB into database")
        return True
  
    except Exception as e:
        globals.con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return False
    

def searchClub():
    try:
        name = input("Enter search term:").strip()
        name = '%' + name + '%'
        query = "SELECT * FROM CLUB WHERE club_name LIKE '%s'" % name
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ['Club ID', 'Name', 'Home Ground', 'Foundation Year', 'Street Address', 'Zip Code', 'City', 'Country']
        data = []
        for res in result:
            try:
                q = "SELECT * FROM ZIP_MAP WHERE zip_code='%s'" % (res["zip_code"])
                globals.cur.execute(q)
                zip_map = globals.cur.fetchone()
                res["city"] = zip_map["city"]
                res["country"] = zip_map["country"]
            except:
                res["city"] = ""
                res["country"] = ""
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

def deleteClub():
    try :
        x = int(input("Enter club_id of the Club to be deleted").strip())
        query1 = "DELETE FROM TRANSFER WHERE club_from_id = %d " % (x)
        query7 = "DELETE FROM TRANSFER WHERE club_to_id = %d " % (x)
        query = "DELETE FROM CLUB WHERE club_id = %d " % (x)
        query2 = "DELETE FROM MANAGES WHERE club_id = %d " % (x)
        query3 = "DELETE FROM OWNS WHERE club_id = %d " % (x)
        query4 = "DELETE FROM PLAYED_IN_KNOCKOUT WHERE club_id = %d " % (x)
        query5 = "DELETE FROM PLAYED_IN_LEAGUE WHERE club_id = %d " % (x)
        query6 = "DELETE FROM PLAYED_FOR WHERE club_id = %d " % (x)
        
        globals.cur.execute(query1)
        globals.cur.execute(query2)
        globals.cur.execute(query3)
        globals.cur.execute(query4)
        globals.cur.execute(query5)
        globals.cur.execute(query6)
        globals.cur.execute(query7)
        globals.cur.execute(query)
        globals.con.commit()
        print("Club Deleted")
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to Delete")
        print(">>>>>>>>>>>>>", e)
        return False


def getClubPlayersBySeason():
    try:
        club_id = int(input("Enter club id:").strip())
        season_year = input("Enter a season year (20XX-YY):").strip()
        query = "SELECT PLAYER.player_name,minutes_played,goals,assists,clearances,tackles,red_cards,yellow_cards,saves FROM PLAYER INNER JOIN PLAYED_FOR ON PLAYER.player_id=PLAYED_FOR.player_id AND season_year='%s' AND club_id=%d" % (season_year, club_id)
        print(query)
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

def getPlayersSoldByClub():
    try:
        x = int(input("Enter the id of the club whose outgoing transfers you want:").strip())
        query = "SELECT * FROM TRANSFER WHERE club_from_id = %d " % (x)
        globals.cur.execute(query)
        temp = globals.cur.fetchall()
        headers = ['player_name','transfer_from','tranfer_to','agent_name','transfer_fee','agent_fee','date_of_transfer']
        data = []
        
        for t in temp:
                ll = {}
                query = "SELECT club_name FROM CLUB WHERE club_id = %d " % (int(t["club_from_id"]))
                globals.cur.execute(query)
                r1 = globals.cur.fetchone()
                ll["transfer_from"] = r1["club_name"]
                query = "SELECT club_name FROM CLUB WHERE club_id = %d " % (int(t["club_to_id"]))
                globals.cur.execute(query)
                r1 = globals.cur.fetchone()
                ll["transfer_to"] = r1["club_name"]
                query = "SELECT player_name FROM PLAYER WHERE player_id = %d " % (int(t["player_id"]))
                globals.cur.execute(query)
                r1 = globals.cur.fetchone()
                ll["player_name"] = r1["player_name"]
                query = "SELECT name FROM AGENT WHERE agent_id = %d " % (int(t["agent_id"]))
                globals.cur.execute(query)
                r1 = globals.cur.fetchone()
                ll["agent_name"] = r1["name"]
                ll["transfer_fee"] = t["transfer_fee"]
                ll["agent_fee"] = t["agent_fee"]
                ll["date_of_transfer"] = t["date_of_transfer"]
                lllist = list(ll.values())
                data.append(lllist)
        table = columnar(data, headers)
        print(table)
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False

                   
            
def getPlayersBoughtByClub():
    try:
        x = int(input("Enter the id of the club whose outgoing transfers you want:").strip())
        query = "SELECT * FROM TRANSFER WHERE club_to_id = %d " % (x)
        globals.cur.execute(query)
        temp = globals.cur.fetchall()
        headers = ['player_name','transfer_from','tranfer_to','agent_name','transfer_fee','agent_fee','date_of_transfer']
        data = []
        
        for t in temp:
                ll = {}
                query = "SELECT club_name FROM CLUB WHERE club_id = %d " % (int(t["club_from_id"]))
                globals.cur.execute(query)
                r1 = globals.cur.fetchone()
                ll["transfer_from"] = r1["club_name"]
                query = "SELECT club_name FROM CLUB WHERE club_id = %d " % (int(t["club_to_id"]))
                globals.cur.execute(query)
                r1 = globals.cur.fetchone()
                ll["transfer_to"] = r1["club_name"]
                query = "SELECT player_name FROM PLAYER WHERE player_id = %d " % (int(t["player_id"]))
                globals.cur.execute(query)
                r1 = globals.cur.fetchone()
                ll["player_name"] = r1["player_name"]
                query = "SELECT name FROM AGENT WHERE agent_id = %d " % (int(t["agent_id"]))
                globals.cur.execute(query)
                r1 = globals.cur.fetchone()
                ll["agent_name"] = r1["name"]
                ll["transfer_fee"] = t["transfer_fee"]
                ll["agent_fee"] = t["agent_fee"]
                ll["date_of_transfer"] = t["date_of_transfer"]
                lllist = list(ll.values())
                data.append(lllist)
        table = columnar(data, headers)
        print(table)
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False

def getAllClubTransfers():
    try:
        x = int(input("Enter the ID of the club whose transfers you want : ").strip())
        data = []
        
        query = "SELECT * FROM TRANSFER WHERE club_from_id = %d OR club_to_id = %d " % (x,x)
        globals.cur.execute(query)
        temp = globals.cur.fetchall()
        headers = ['player_name','transfer_from','tranfer_to','agent_name','transfer_fee','agent_fee','date_of_transfer']
    
        for t in temp:
                ll = {}
                query = "SELECT club_name FROM CLUB WHERE club_id = %d " % (int(t["club_from_id"]))
                globals.cur.execute(query)
                r1 = globals.cur.fetchone()
                ll["transfer_from"] = r1["club_name"]
                query = "SELECT club_name FROM CLUB WHERE club_id = %d " % (int(t["club_to_id"]))
                globals.cur.execute(query)
                r1 = globals.cur.fetchone()
                ll["transfer_to"] = r1["club_name"]
                query = "SELECT player_name FROM PLAYER WHERE player_id = %d " % (int(t["player_id"]))
                globals.cur.execute(query)
                r1 = globals.cur.fetchone()
                ll["player_name"] = r1["player_name"]
                query = "SELECT name FROM AGENT WHERE agent_id = %d " % (int(t["agent_id"]))
                globals.cur.execute(query)
                r1 = globals.cur.fetchone()
                ll["agent_name"] = r1["name"]
                ll["transfer_fee"] = t["transfer_fee"]
                ll["agent_fee"] = t["agent_fee"]
                ll["date_of_transfer"] = t["date_of_transfer"]
                lllist = list(ll.values())
                data.append(lllist)
        table = columnar(data, headers)
        print(table)
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False

    

def getClubNetSpent():
    try:
        val = int(input("Enter the club_id of the club whose net spend you are interested in: ").strip())
        query = "SELECT SUM(transfer_fee) AS spent FROM TRANSFER WHERE club_to_id = %d " % (val)
        globals.cur.execute(query)
        
        
        res = globals.cur.fetchone()
        plus = 2.00
        if(res["spent"] == None):
            plus = 0.00
        else:
            plus = float(res["spent"])
        
        query = "SELECT SUM(transfer_fee) AS got FROM TRANSFER WHERE club_from_id = %d " % (val)
        globals.cur.execute(query)
        res = globals.cur.fetchone()
        
        minus = -2.00
        if(res["got"] == None):
            minus = 0.00
        else:
            minus = float(res["got"])
        
        total = float(plus-minus)
        query = "SELECT club_name FROM CLUB WHERE club_id = %d " %(val)
        globals.cur.execute(query)
        res = globals.cur.fetchone()
        clubname = res["club_name"]
        ans = "Net Spend of %s is %f " % (clubname,total)
        print(ans)
    
    except Exception as e:
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False
    
def getClubPerformanceInTournament():
    try:
        club_id = int(input("Enter club ID:").strip())
        tournament_type = int(input("Enter 0 for leagues and 1 for knockout tournaments:").strip())
        if tournament_type != 0 and tournament_type != 1:
            print("Invalid input")
            return False
        tournament_name = input("Enter tournament name:").strip()
        q = "SELECT * FROM TOURNAMENT WHERE tournament_name='%s' AND tournament_type='%s'" % (tournament_name, ("League" if tournament_type == 0 else "Knockout"))
        globals.cur.execute(q)
        tournament = globals.cur.fetchone()
        if tournament is None:
            print("Not a valid tournament")
            return False
        season_year = input("Enter a season year (20XX-YY):").strip()
        q = "SELECT * FROM SEASON WHERE season_year='%s'" % season_year
        globals.cur.execute(q)
        season = globals.cur.fetchone()
        if season is None:
            print("Not a valid season year")
            return False
        if tournament_type == 0:
            query = "SELECT CLUB.club_name,no_of_win,no_of_draw,no_of_loss,goals_for,goals_against FROM CLUB INNER JOIN PLAYED_IN_LEAGUE ON CLUB.club_id=PLAYED_IN_LEAGUE.club_id AND season_year='%s' AND tournament_name='%s' AND CLUB.club_id=%d" % (season_year, tournament_name, club_id)
        else:
            query = "SELECT CLUB.club_name,no_of_win,no_of_draw,no_of_loss,stage_of_exit FROM CLUB INNER JOIN PLAYED_IN_KNOCKOUT ON CLUB.club_id=PLAYED_IN_KNOCKOUT.club_id AND season_year='%s' AND tournament_name='%s' AND CLUB.club_id=%d" % (season_year, tournament_name, club_id)
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchone()
        if tournament_type == 0:
            headers = ["Club name", "W", "D", "L", "GF", "GA"]
        else:
            headers = ["Club name", "W", "D", "L", "Stage of Exit"]
        data = [list(result.values())]
        print(table)
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False