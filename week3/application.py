from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
   return render_template("index.html")

@app.route("/application-form")
def application_form():
	return render_template("/application-form.html")

@app.route("/application", methods=["POST"])
def application():
	first_name = request.form.get("firstname")
	last_name = request.form.get("lastname")
	salary = request.form.get("salary")
	num_salary = int(salary)
	job = request.form.get("job")
	return render_template("application.html", firstname=first_name, lastname=last_name, salary=num_salary, job=job)

if __name__ == "__main__":
    app.run(debug=True)