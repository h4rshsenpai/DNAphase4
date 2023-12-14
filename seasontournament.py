import globals
from validators import *
from columnar import columnar

def insertSeason():
    try :
        x = input("Enter the season :").strip()
        y = x.replace(" ","")
        x = y
        if(ValidateSeasonYear(x) == False):
            print("Wrong Format for season")
            return False
        query = "INSERT INTO SEASON (season_year) VALUES ('%s')" %  (x)
        print(query)
        globals.cur.execute(query)
        globals.con.commit()
        print("Inserted season into database")
        return True
       
    except Exception as e:
        globals.con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return False
        
def getAllTournaments():
    try:
        query = "SELECT * FROM TOURNAMENT"
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ['Tournament Name', 'Number of Participants', 'Tournament Type']
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


def getTournamentTeamsBySeason():
    try:
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
            query = "SELECT CLUB.club_name,no_of_win,no_of_draw,no_of_loss,goals_for,goals_against FROM CLUB INNER JOIN PLAYED_IN_LEAGUE ON CLUB.club_id=PLAYED_IN_LEAGUE.club_id AND season_year='%s' AND tournament_name='%s'" % (season_year, tournament_name)
        else:
            query = "SELECT CLUB.club_name,no_of_win,no_of_draw,no_of_loss,stage_of_exit FROM CLUB INNER JOIN PLAYED_IN_KNOCKOUT ON CLUB.club_id=PLAYED_IN_KNOCKOUT.club_id AND season_year='%s' AND tournament_name='%s'" % (season_year, tournament_name)
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        if tournament_type == 0:
            headers = ["Club name", "W", "D", "L", "GF", "GA"]
        else:
            headers = ["Club name", "W", "D", "L", "Stage of Exit"]
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
