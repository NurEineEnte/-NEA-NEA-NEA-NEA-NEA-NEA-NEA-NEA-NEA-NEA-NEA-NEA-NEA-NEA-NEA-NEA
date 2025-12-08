import sqlite3



con = sqlite3.connect("simulatorDB.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS accounts")

create_table_query = """
    CREATE TABLE accounts(
        accountID int KEY NOT NULL,
        username VARCHAR(30) NOT NULL,
        password VARCHAR(10) NOT NULL,
        accountType VARCHAR(1) NOT NULL,
        questionAnswer VARCHAR(10) NOT NULL,
        questionID int KEY
    );
"""
cur.execute(create_table_query)

cur.execute("DROP TABLE IF EXISTS securityQuestions")
create_table_query = """
    CREATE TABLE securityQuestions(
        questionID INT KEY NOT NULL,
        question VARCHAR(255) NOT NULL        
    );
"""
cur.execute(create_table_query)

cur.execute("""
INSERT INTO securityQuestions VALUES
    (1, "Which city were you born in?"),
    (2, "What was the name of your first pet?"),
    (3, "What is your favourite food?")           
    ;
""")

con.commit()

cur.execute("DROP TABLE IF EXISTS accountstats")
create_table_query = """
    CREATE TABLE accountstats(
        accountID INT KEY NOT NULL,
        playtime INT NOT NULL,
        objectsPlaced int NOT NULL        
    );
"""
cur.execute(create_table_query)

searchResult = cur.execute("SELECT * FROM securityQuestions")
print(searchResult.fetchall())

insert_data_query = """
INSERT INTO accounts VALUES(1, "testing123", "1203", "T", "1230", 1);
"""
cur.execute(insert_data_query)
con.commit()


insert_data_query = """
INSERT INTO accountstats VALUES(1, 0, 4);
"""
cur.execute(insert_data_query)
con.commit()

searchResult = cur.execute("SELECT * FROM accounts WHERE accountID = 1")
print(searchResult.fetchone())
searchResult = cur.execute("SELECT * FROM accountstats WHERE accountID = 1")
print(searchResult.fetchone())

con.close()