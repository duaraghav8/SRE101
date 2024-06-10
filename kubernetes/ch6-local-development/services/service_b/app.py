from flask import Flask, jsonify
import mysql.connector
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)


def get_db_connection():
    connection = mysql.connector.connect(
        host='mysql',
        user='root',
        password='password',
        database='sre101'
    )
    return connection


def populate_mysql_data():
    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS test_table')
    cursor.execute('CREATE TABLE test_table (name VARCHAR(255), title VARCHAR(255))')

    query = "INSERT INTO test_table (name, title) VALUES (%s, %s)"
    cursor.execute(query, ('raghav', 'sre'))
    cursor.execute(query, ('alice', 'devops engineer'))
    cursor.execute(query, ('bob', 'platform engineer'))
    cursor.execute(query, ('deadpool', 'x man'))

    conn.commit()
    conn.close()


@app.route('/data', methods=['GET'])
def get_data():
    app.logger.info("Sending request for data to MySQL")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test_table')
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)


if __name__ == '__main__':
    # Populate MySQL with dummy data so that it is
    # available when the api controller attempts to read it.
    populate_mysql_data()

    app.run(host='0.0.0.0', port=5001)








