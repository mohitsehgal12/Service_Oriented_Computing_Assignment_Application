import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database setup
conn = sqlite3.connect('income.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS income (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        source TEXT NOT NULL,
        timestamp DATETIME NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

conn.commit()
conn.close()

income_records = {}


@app.route('/income', methods=['POST'])
def record_income():
    data = request.get_json()

    if 'user_id' in data and 'amount' in data and 'source' in data:
        user_id = data['user_id']
        conn = sqlite3.connect('income.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO income (user_id, amount, source, timestamp) VALUES (?, ?, ?, datetime('now'))",
                       (user_id, data['amount'], data['source']))
        conn.commit()

        cursor.execute("SELECT last_insert_rowid()")
        income_id = cursor.fetchone()[0]

        conn.close()

        return jsonify({"income_id": income_id}), 201
    else:
        return "Invalid income data", 400


@app.route('/income', methods=['GET'])
def list_income():
    data = request.args
    user_id = data.get('user_id')

    if user_id is not None:
        conn = sqlite3.connect('income.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM income WHERE user_id=?", (user_id,))
        income_data = cursor.fetchall()
        conn.close()

        income_list = []
        for income in income_data:
            income_dict = {
                "income_id": income[0],
                "user_id": income[1],
                "amount": income[2],
                "source": income[3],
                "timestamp": income[4],
            }
            income_list.append(income_dict)

        return jsonify(income_list), 200
    else:
        return "Invalid user ID", 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8090, debug=True)
