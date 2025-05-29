# System Design Document

## System Architecture

The system follows a modular client-server architecture:

- **Frontend**: HTML, CSS, JavaScript form where students enter their preferences.
- **Backend API**: Python Flask server to handle logic and communicate with frontend.
- **Data Storage**: Static JSON file (`courses.json`) containing course details like name, difficulty, credits, schedule, and field.
- **AI Engine**:
  - Fuzzy logic for suitability scoring
  - Genetic algorithm for optimal course combination


## Input Parameters
- **Field of Interest**: The domain student is interested in (e.g., CS, Arts).
- **Challenge Level**: How difficult/challenging the student prefers their courses.
- **Time Availability**: How many hours/day they can study (for future use).

## Course Data Attributes
- Course Code and Name
- Field (Arts, CS, etc.)
- Difficulty Level (1–10)
- Schedule (e.g., ["Mon 9-11", "Wed 9-11"])
- Credits

## Fuzzy Logic
Used to assign a **suitability score** to each course based on:
- Student interest level
- Preferred challenge
- Actual course difficulty

We define fuzzy sets for each input and use rules like:
- If interest is high and challenge is low → High suitability
- If difficulty is too far from preferred → Low suitability

## Genetic Algorithm
After all courses are scored, we use GA to:
- Randomly generate possible course combinations
- Avoid schedules with time conflicts
- Keep credit total ≤ 9
- Maximize total suitability score

It uses crossover and mutation to improve results over 20 generations.

## Justification for AI Techniques
- **Fuzzy Logic** is ideal for subjective inputs, which can’t be evaluated precisely.
- **Genetic Algorithm** is powerful for solving multi-constraint optimization problems, like course selection with multiple hard and soft constraints.

## Technologies Used
- Python
- Flask
- scikit-fuzzy
- JavaScript
- HTML/CSS
- JSON for data
