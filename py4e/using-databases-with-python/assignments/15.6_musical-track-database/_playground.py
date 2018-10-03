import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

cur.execute('DROP TABLE IF EXISTS Orgs')

cur.execute('''
CREATE TABLE Orgs (org TEXT, counts INTEGER)''')

for rows in cur.execute(sqlstr):
    orgs = re.findall('@(\w+)', rows[0])
    for org in orgs:

        cur.execute('SELECT counts FROM Orgs WHERE org = ?', (org,))
        rows = cur.fetchone()
        if rows is None:
            cur.execute('INSERT INTO Orgs (org, counts) VALUES (?, 1)', (org,))
        else:
            cur.execute('UPDATE Orgs SET counts = counts + 1 WHERE org = ?', (org,))
        conn.commit()


cur.close()
