from flask import Flask, request, jsonify
from flask_cors import CORS
from geneticalgo import run_ga

app = Flask(__name__)
CORS(app)

@app.route("/recommend", methods=["POST"])
def recommend_courses():
    data = request.get_json()
    interest = int(data["interest"])
    difficulty = int(data["difficulty"])
    field = data.get("field", "Computer Science")
    time = int(data.get("time", 1))  

    best_courses = run_ga(interest, difficulty, field)

    result = []
    for course in best_courses:
        result.append({
            "code": course["code"],
            "name": course["name"],
            "difficulty": course["difficulty"],
            "suitability": course["suitability"],
            "credits": course["credits"]
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
