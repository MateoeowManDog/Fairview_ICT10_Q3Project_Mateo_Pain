from flask import Flask, render_template, request

app = Flask(name)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if len(username) < 7:
            message = "Username must contain at least 7 characters."
        elif len(password) < 10:
            message = "Password must be at least 10 characters long."
        elif not any(c.isalpha() for c in password):
            message = "Password must contain at least one letter."
        elif not any(c.isdigit() for c in password):
            message = "Password must contain at least one number."
        else:
            message = "Account successfully created!"

    return render_template("signup.html", message=message)


@app.route("/teamchecker", methods=["GET", "POST"])
def teamchecker():
    message = ""

    if request.method == "POST":
        registration = request.form.get("registration")
        medical = request.form.get("medical")
        grade = request.form.get("grade")
        section = request.form.get("section")

        if not registration or not medical or not grade or not section:
            message = "❌ Please complete all fields."
        else:
            grade = int(grade)

            if registration == "yes":
                if medical == "yes":
                    if 7 <= grade <= 10:
                        if grade == 7:
                            team = "Blue Bears"
                        elif grade == 8:
                            team = "Red Bulldogs"
                        elif grade == 9:
                            team = "Yellow Tigers"
                        else:
                            team = "Green Hornets"

                        message = f"🎉 Congratulations! You are eligible! Team: {team} | Grade {grade} - {section}"
                    else:
                        message = "❌ Only Grades 7-10 are eligible."
                else:
                    message = "❌ You need medical clearance."
            else:
                message = "❌ Please complete online registration."

    return render_template("teamchecker.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)