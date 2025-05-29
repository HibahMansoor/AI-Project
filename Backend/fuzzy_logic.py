import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
interest = ctrl.Antecedent(np.arange(0, 11, 1), 'interest')
difficulty_pref = ctrl.Antecedent(np.arange(0, 11, 1), 'difficulty_pref')
course_difficulty = ctrl.Antecedent(np.arange(0, 11, 1), 'course_difficulty')

suitability = ctrl.Consequent(np.arange(0, 11, 1), 'suitability')

# Membership functions
interest.automf(3)
difficulty_pref.automf(3)
course_difficulty.automf(3)

suitability['low'] = fuzz.trimf(suitability.universe, [0, 0, 5])
suitability['medium'] = fuzz.trimf(suitability.universe, [3, 5, 7])
suitability['high'] = fuzz.trimf(suitability.universe, [5, 10, 10])

# Fuzzy rules
rules = [
    ctrl.Rule(interest['poor'] | course_difficulty['good'], suitability['low']),
    ctrl.Rule(interest['average'] & course_difficulty['average'], suitability['medium']),
    ctrl.Rule(interest['good'] & course_difficulty['poor'], suitability['high']),
    ctrl.Rule(difficulty_pref['good'] & course_difficulty['good'], suitability['high'])
]

# Control system
suitability_ctrl = ctrl.ControlSystem(rules)
suitability_sim = ctrl.ControlSystemSimulation(suitability_ctrl)

# Evaluate one course
def evaluate_course(interest_val, difficulty_pref_val, course_diff_val):
    suitability_sim.input['interest'] = interest_val
    suitability_sim.input['difficulty_pref'] = difficulty_pref_val
    suitability_sim.input['course_difficulty'] = course_diff_val
    suitability_sim.compute()
    return round(suitability_sim.output['suitability'], 2)

# Test
if __name__ == "__main__":
    score = evaluate_course(9, 5, 4)
    print(f"Suitability Score: {score}")






