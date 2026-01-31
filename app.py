from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

FILE_PATH = r"C:\Users\saidi\OneDrive\Desktop\chidduvilas\di.txt"


class Data:
    def __init__(self, name, age, emp_id, salary, company):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.salary = salary
        self.company = company

    def __repr__(self):
        return (f"name={self.name}, age={self.age}, "
                f"id={self.emp_id}, salary={self.salary}, "
                f"company={self.company}")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        emp_id = request.form["emp_id"]
        salary = request.form["salary"]
        company = request.form["company"]

        d = Data(name, age, emp_id, salary, company)

        with open(FILE_PATH, "a") as f:
            f.write(str(d) + "\n")

        return redirect(url_for("index"))

    return render_template("ii.html")

if __name__ == "__main__":
    app.run(debug=True)
