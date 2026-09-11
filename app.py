from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Grade Calculator</title>
</head>
<body>
    <h1>Student Grade Calculator</h1>

    <form method="POST">
        <label>Student Name:</label>
        <input type="text" name="name" required><br><br>

        <label>Python Mark:</label>
        <input type="number" name="python" min="0" max="100" required><br><br>

        <label>Git Mark:</label>
        <input type="number" name="git" min="0" max="100" required><br><br>

        <label>Docker Mark:</label>
        <input type="number" name="docker" min="0" max="100" required><br><br>

        <button type="submit">Calculate</button>
    </form>

    {% if result %}
    <hr>
    <h2>Result</h2>
    <p>Student Name: {{ name }}</p>
    <p>Total: {{ total }}</p>
    <p>Average: {{ average }}</p>
    <p>Grade: {{ grade }}</p>
    <p>Result: {{ result }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        name = request.form["name"]
        python_mark = int(request.form["python"])
        git_mark = int(request.form["git"])
        docker_mark = int(request.form["docker"])

        total = python_mark + git_mark + docker_mark
        average = total / 3

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        result = "PASS" if average >= 50 else "FAIL"

        return render_template_string(
            HTML,
            name=name,
            total=total,
            average=round(average, 2),
            grade=grade,
            result=result
        )

    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)