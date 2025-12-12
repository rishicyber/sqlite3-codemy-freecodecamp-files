import sqlite3

# conn = sqlite3.connect(":memory:") # doesnt save any db file in current folder, deletes it after code finishes
conn = sqlite3.connect("customer.db")

curs = conn.cursor()

def create_customer_table():
    curs.execute("""
            CREATE TABLE customers (
                first_name text,
                last_name text,
                email text
            )         
        """)

# create_customer_table()

# curs.execute("""
#         INSERT INTO customers
#         VALUES('John', 'Elder', 'john@codemy.com')
#         """)
# curs.execute("""
#         INSERT INTO customers
#         VALUES('Tim', 'Smith', 'tim@codemy.com')
#         """)
# curs.execute("""
#         INSERT INTO customers
#         VALUES('Marry', 'Brown', 'marry@codemy.com')
#         """)
    
# many_customers = [
#     ('wes', 'brown', 'wes@brown.com'),
#     ('steph', 'keuwa', 'steph@keuwa.com'),
#     ('dan', 'pas', 'dan@pas.com')
#                   ]
# query = """
#     INSERT INTO customers VALUES(?, ?, ?)
# """
# curs.executemany(query, many_customers)

    
def print_customers():
    curs.execute("""
            SELECT rowid, * FROM customers
            """)
    for row in curs.fetchall():
        print(row)
    
# print_customers()

def update_record():
    curs.execute("""
            UPDATE customers SET first_name = 'Mary'
            where  last_name = 'Brown' and rowid = 5
        """)


# update_record()



def delete_record():
    curs.execute("""
            DELETE FROM customers
            where rowid = 2        
        """)
    
# delete_record()


def order_record():
    curs.execute("""
            SELECT rowid, * FROM customers
            ORDER BY rowid DESC
        """)
    for item in curs.fetchall():
        print(item)

# order_record()





def and_or_record():
    curs.execute("""
        SELECT rowid, * FROM customers
        where last_name like 'Br%' OR rowid = 1 
        """)
    for item in curs:
        print(item)

# and_or_record()


def limit_record():
    curs.execute("""
        SELECT rowid, * from customers
        LIMIT 3
        """)
    for item in curs:
        print(item)

# limit_record()


def drop_table():
    curs.execute("""
            DROP TABLE customers         
        """)

# drop_table()
print()
print()
print_customers()


conn.commit()
conn.close()