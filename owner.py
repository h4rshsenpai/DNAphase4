import globals
from validators import *
from columnar import columnar

def getAllOwners():
    try:
        query = "SELECT * FROM OWNER"
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ['Owner ID', 'Name', 'Nationality']
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

def insertOwner():
    try :
        print("Enter Owner details")
        x = input("Enter the Owner Name :").strip()
        y = input("Enter the home country of the owning entity :").strip()
        if(ValidateNationality(y) == False):
            print("Given County is wrong")
            return False

        query = "INSERT INTO OWNER (owner_name,country_origin) VALUES ('%s','%s')" %  (x,y)
        print(query)
        globals.cur.execute(query)
        globals.con.commit()
        print("Inserted owner into database")
        return True
       
    except Exception as e:
        globals.con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return False


def updateOwnerNationality():
    try:
        owner_id = int(input("Enter Owner ID:").strip())
        q = "SELECT * FROM OWNER WHERE owner_id=%d" % (owner_id)
        globals.cur.execute(q)
        owner = globals.cur.fetchone()
        if owner is None:
            print("Not found")
            return False
        newNationality = input("Enter new nationality:").strip()
        if not ValidateNationality(newNationality):
            print("Not a valid nationality")
            return False
        query = "UPDATE OWNER SET nationality='%s' WHERE owner_id=%d" % (newNationality, owner_id)
        globals.cur.execute(query)
        globals.con.commit()

        print("Nationality updated")
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to update")
        print(">>>>>>>>>>>>>", e)
        return False

def deleteOwner():
    try :
        x = int(input("Enter owner_id of the Owner to be deleted").strip())
        query1 = "DELETE FROM OWNS WHERE owner_id = %d " % (x)
        query = "DELETE FROM OWNER WHERE owner_id = %d " % (x)
        
        globals.cur.execute(query1)
        globals.cur.execute(query)
        globals.con.commit()
        print("Owner Deleted")
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to Delet")
        print(">>>>>>>>>>>>>", e)
        return False

    



