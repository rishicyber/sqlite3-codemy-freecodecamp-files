import sqlite3

#query database and reurn all records
def show_all():
    conn = sqlite3.connect("customer.db")
    curs = conn.cursor()

    curs.execute("select rowid, * from customers")
    items = curs.fetchall()
    for item in items:
        print(item)
        
    conn.commit()
    conn.close()
    
# add one new record to the table
def add_one(first, last, email):
    conn = sqlite3.connect("customer.db")
    curs = conn.cursor()

    params = [first, last, email]
    query = "insert into customers values(?, ?, ?)"
    curs.execute(query, params)
        
    conn.commit()
    conn.close()

# delete a record from a database
def delete_one(id):
    conn = sqlite3.connect("customer.db")
    curs = conn.cursor()

    params = [id]
    query = "delete from customers where rowid = (?)"
    curs.execute(query, params)
        
    conn.commit()
    conn.close()

def add_many(mylist):
    conn = sqlite3.connect("customer.db")
    curs = conn.cursor()

    params = mylist
    query = "insert into customers values(?, ?, ?)"
    curs.executemany(query, params)
        
    conn.commit()
    conn.close()

def email_lookup(email):
    conn = sqlite3.connect("customer.db")
    curs = conn.cursor()

    params = (email,)
    query = "select rowid, * from customers where email = (?)"
    curs.execute(query, params)
    
    items = curs.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()
    