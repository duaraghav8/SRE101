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
    app.run(host='0.0.0.0', port=5001)








