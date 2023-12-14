import globals
from validators import *
from columnar import columnar


#display the table agent
def getAllAgents():
    try:
        query = "SELECT * FROM AGENT"
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ['Agent ID', 'Name', 'DOB', 'Nationality']
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
        

#insert a new agent in the table agent after taking input from User
def insertAgent():
    try:
        row = {}
        print("Enter agent's details: ")
        row["name"] = input("Enter name: ").strip()
        row["data_of_birth"] = input("Enter Date of Birth (YYYY-MM-DD): ").strip()
        if not ValidateDate(row["data_of_birth"]):
            print("Not a valid date")
            return False
        row["nationality"] = input("Enter nationality: ").strip()
        if not ValidateNationality(row["nationality"]):
            print("Not a valid nationality")
            return False

        query = "INSERT INTO AGENT (name, data_of_birth, nationality) VALUES ('%s', '%s', '%s')" %  (row["name"], row["data_of_birth"], row["nationality"])
        print(query)
        globals.cur.execute(query)
        globals.con.commit()

        print("Inserted agent into database")
        return True

    except Exception as e:
        globals.con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return False

#deletes agent from a database when agent id is given as input
#also returns success if agent id is given wrong
#deletes entries from other tables which references the given agent_id
#except in the case of table PLAYER where it sets the agent_id = NULL
def deleteAgent():
        try :
            x = int(input("Enter agent_id of the agent to be deleted: ").strip())
            query1 = "DELETE FROM AGENT WHERE agent_id = %d " % (x)
            query2 = "DELETE FROM TRANSFER WHERE agent_id = %d " % (x)
            query = "UPDATE PLAYER SET agent_id = NULL WHERE agent_id =  %d" % (x)
        
            globals.cur.execute(query)
            globals.cur.execute(query2)
            globals.cur.execute(query1)
            
            globals.con.commit()
            print("Agent with given Id doesnot exist anymore")
            return True
        except Exception as e:
            globals.con.rollback()
            print("Failed to Delete")
            print(">>>>>>>>>>>>>", e)
            return False

#Updates Nationality of agent whose ID and new nationality is given as input
def updateAgentNationality():
    try:
        agent_id = int(input("Enter Agent ID: ").strip())
        q = "SELECT * FROM AGENT WHERE agent_id=%d" % (agent_id)
        globals.cur.execute(q)
        agent = globals.cur.fetchone()
        if agent is None:
            print("Not found")
            return False
        newNationality = input("Enter new nationality: ").strip()
        if not ValidateNationality(newNationality):
            print("Not a valid nationality")
            return False
        query = "UPDATE AGENT SET nationality='%s' WHERE agent_id=%d" % (newNationality, agent_id)
        globals.cur.execute(query)
        globals.con.commit()

        print("Nationality updated")
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to update")
        print(">>>>>>>>>>>>>", e)
        return False


