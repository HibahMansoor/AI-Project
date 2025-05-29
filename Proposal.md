# Project Proposal: Intelligent Course Recommender

## Problem Statement
In modern academic environments, students face a wide variety of course options every semester. 
Selecting the right combination of courses that aligns with their academic interests, skill level, 
time availability, and graduation requirements is a complex task. Many students make choices based on 
guesswork, peer recommendations, or trial and error, which can lead to academic overload, disinterest, or suboptimal performance.
There is a need for an intelligent system that can assist students in making data-driven course selection 
decisions tailored to their preferences and constraints.

## Objectives
- Build a personalized course recommendation system.
- Allow students to input preferences such as:
  - Field of interest (e.g., Arts, Engineering)
  - Desired challenge level
  - Available study time per day
- Evaluate course suitability based on inputs using fuzzy logic.
- Recommend the most optimal set of 2–3 courses using a genetic algorithm.
- Avoid time clashes and limit recommendations to a maximum of 9 credits.

## Chosen AI Techniques
- **Fuzzy Logic**: This technique handles uncertain, vague, and linguistic inputs (e.g., "Easy", "Moderate", "Tough"). 
It helps in calculating how suitable a course is based on how well the course difficulty matches the student's confidence and interest.
- **Genetic Algorithm**: A metaheuristic search technique inspired by natural selection. It helps to find the best course combination that maximizes suitability while satisfying hard constraints like time availability and credit limits.

## Expected Outcomes
- A web-based application with a friendly frontend for student interaction.
- A functional AI backend that processes preferences and returns optimal course suggestions.
- An academic scheduling tool that simplifies decision-making for students and advisors.
