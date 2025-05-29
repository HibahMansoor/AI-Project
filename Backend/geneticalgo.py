import random
import json
import os
from fuzzy_logic import evaluate_course

MAX_CREDITS = 9
POP_SIZE = 10
GENERATIONS = 20

def load_courses(selected_field, preferred_level):
    path = os.path.join(os.path.dirname(__file__), "data", "courses.json")
    with open(path, "r") as file:
        all_courses = json.load(file)

    return [
        c for c in all_courses
        if c["field"] == selected_field and abs(c["difficulty"] - preferred_level) <= 3
    ]


def has_schedule_conflict(course1, course2):
    return any(t in course2['schedule'] for t in course1['schedule'])

def is_valid_schedule(schedule):
    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):
            if has_schedule_conflict(schedule[i], schedule[j]):
                return False
    return True

def total_credits(schedule):
    return sum(c['credits'] for c in schedule)

def calculate_fitness(individual, interest, difficulty_pref):
    if not is_valid_schedule(individual):
        return 0
    if total_credits(individual) > MAX_CREDITS:
        return 0

    total_score = 0
    for course in individual:
        score = evaluate_course(interest, difficulty_pref, course['difficulty'])
        course['suitability'] = score
        total_score += score
    return total_score

def generate_individual(courses):
    individual = []
    credits = 0
    random.shuffle(courses)
    for course in courses:
        if credits + course['credits'] <= MAX_CREDITS:
            if not any(has_schedule_conflict(course, c) for c in individual):
                individual.append(course)
                credits += course['credits']
    return individual

def crossover(parent1, parent2):
    combined = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
    return list({c['code']: c for c in combined}.values())

def mutate(individual, courses):
    if not individual:
        return individual
    idx = random.randint(0, len(individual) - 1)
    new_course = random.choice(courses)
    individual[idx] = new_course
    return individual

def run_ga(interest, difficulty_pref, selected_field):
    courses = load_courses(selected_field, difficulty_pref)
    if not courses:
        return []

    population = [generate_individual(courses) for _ in range(POP_SIZE)]

    for _ in range(GENERATIONS):
        population.sort(key=lambda ind: calculate_fitness(ind, interest, difficulty_pref), reverse=True)
        next_gen = population[:2]
        while len(next_gen) < POP_SIZE:
            parent1, parent2 = random.sample(population[:5], 2)
            child = crossover(parent1, parent2)
            if random.random() < 0.3:
                child = mutate(child, courses)
            next_gen.append(child)
        population = next_gen

    best = max(population, key=lambda ind: calculate_fitness(ind, interest, difficulty_pref))
    return best
