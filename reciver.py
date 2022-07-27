from flask import Flask, request, abort
import mariadb
import sys

app = Flask(__name__)

try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="facebook"
    )
    print ("Connected to Database")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
cur = conn.cursor()
conn.autocommit = True

#The main webhook this is what puts the message into the database
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        #Get the data from the request
        data = request.json

        #Split the data into the different parts
        username = data['username']
        message = data['message']

        #Insert the data into the database
        sql = "INSERT INTO messages (message, username) VALUES (%s, %s)"
        val = (message, username)
        cur.execute(sql, val)
        conn.commit()
        return 'success', 200
    else:
        abort(400)

#This is the webhook that gets the message from the database
@app.route('/sender')
def sender():
    #Get the data from the database
    cur.execute("SELECT message, username FROM idk ORDER BY id DESC LIMIT 1;")
    myresult = cur.fetchall()
    for x in myresult:
        #Sends the databack to the sender
        return(x[1] + ': ' +  x[0])
if __name__ == '__main__':
    app.run(host="0.0.0.0")
