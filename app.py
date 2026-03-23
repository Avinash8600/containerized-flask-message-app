from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="messagedb"
)

cursor = db.cursor()

@app.route("/")
def index():
    cursor.execute("SELECT * FROM msg")
    msgs = cursor.fetchall()
    return render_template("index.html", msgs=msgs)


@app.route("/add", methods=["POST"])
def add():
    message = request.form["message"]

    cursor.execute(
        "INSERT INTO msg (message) VALUES (%s)",
        (message,)
    )
    db.commit()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):
    cursor.execute("DELETE FROM msg WHERE id=%s", (id,))
    db.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
