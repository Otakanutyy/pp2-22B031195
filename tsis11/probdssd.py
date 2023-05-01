import csv
import psycopg2 as pgsql

connection=pgsql.connect(host="localhost", dbname="postgres", user="postgres", 
                         password="Mengobrat2003", port=5432)
cur=connection.cursor()


import psycopg2 as pgsql

connection = pgsql.connect(host="localhost", dbname="postgres", user="postgres", password="Mengobrat2003", port=5432)
cur = connection.cursor()

# Function that returns all records based on a pattern
cur.execute("""CREATE OR REPLACE FUNCTION search_from_pb_by_pattern(pattern character varying)
RETURNS SETOF PhoneBook
AS
$$
SELECT *
FROM PhoneBook
WHERE name ILIKE '%' || pattern || '%' OR surname ILIKE '%' || pattern || '%' OR number::text ILIKE '%' || pattern || '%';
$$
LANGUAGE sql;
""")

# Procedure to insert new user by name and phone, update phone if user already exists
cur.execute("""CREATE OR REPLACE PROCEDURE insert_to_pb(a character varying, b character varying, c integer)
LANGUAGE sql
AS $$
INSERT INTO PhoneBook (surname, name, number)
VALUES (a, b, c)
ON CONFLICT (name, surname)
DO UPDATE SET number = EXCLUDED.number;
$$;
""")

# Procedure to insert many new users by list of name and phone. Use loop and if statement in stored procedure.
# Check correctness of phone in procedure and return all incorrect data.
cur.execute("""CREATE OR REPLACE PROCEDURE insert_list_to_pb(users PhoneBook[])
LANGUAGE sql
AS $$
DECLARE
    i INT;
    num INT;
BEGIN
    FOR i IN 1..array_length(users, 1) LOOP
        BEGIN
            num := users[i].number;
        EXCEPTION WHEN OTHERS THEN
            RAISE EXCEPTION 'Incorrect phone number';
        END;
        
        INSERT INTO PhoneBook (surname, name, number)
        VALUES (users[i].surname, users[i].name, num);
    END LOOP;
END;
$$;
""")

# Function to querying data from the tables with pagination (by limit and offset)
cur.execute("""CREATE OR REPLACE FUNCTION paginating(a integer, b integer)
RETURNS SETOF PhoneBook
AS $$
SELECT *
FROM PhoneBook
ORDER BY surname
LIMIT a
OFFSET b;
$$
LANGUAGE sql;
""")

# Procedure to deleting data from tables by username or phone
cur.execute("""CREATE OR REPLACE PROCEDURE delete_from_pb(a character varying, b character varying)
LANGUAGE sql
AS $$
DELETE FROM PhoneBook
WHERE name = b AND surname = a;
$$;
""")

# Executing
cur.execute("""CALL insert_to_pb('fromp', 'tosql', 465465654);""")
cur.execute("""SELECT * FROM search_from_pb_by_pattern('lol');""")
print(cur.fetchall())
cur.execute("""CALL insert_to_pb('pip', 'pup', 66);""")
cur.execute("""SELECT * FROM paginating(5, 2);""")
print(cur.fetchall())
cur.execute("""CALL delete_from_pb('fromp', 'tosql');""")
cur.execute("""CALL insert_list_to_pb('{{"toqayev", "qasym", 12345}, {"nazarbayev", "nursultan", 46465}, {"idont", "know", 46451}}'::PhoneBook[]);""")

connection.commit()
cur.close()
connection.close()
