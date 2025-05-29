# Test Results and Evaluation

## Testing Strategy

We tested our system using a variety of input scenarios for different fields and challenge preferences. The system was evaluated based on correctness, usability, and responsiveness.

Test cases covered:
- Different user interest levels (low to high)
- Multiple fields: Arts, Computer Science, Engineering, Business
- Varied challenge preferences (light to tough)
- Multiple time availabilities

## Sample Test Cases

| Interest | Challenge | Field            | Time (hrs/day) | Recommended Courses                   |
|----------|-----------|------------------|----------------|----------------------------------------|
| 9        | Tough     | Computer Science | 3              | Intro to AI, Web Dev                   |
| 5        | Light     | Arts             | 2              | Intro to Sketching, Design Principles  |
| 8        | Moderate  | Business         | 2              | Business Fundamentals, Marketing       |
| 6        | Tough     | Engineering      | 4              | Engineering Mechanics, Electrical Engg |

## Observations
- Fuzzy logic adapts well to subjective inputs like challenge preference.
- Genetic Algorithm returns different course sets for different inputs while obeying constraints.
- Time clashes are successfully avoided.
- Credit limit is never exceeded.

## Performance
- Runs under 1 second on local machine for small course sets (≤ 10).
- Suitable for interactive use.

## Limitations
- Course dataset is static; no integration with real-time academic data.
- Course prerequisites are not handled.
- Time availability input is collected but not fully used for pruning.

## Future Improvements
- Use study time input to eliminate courses with high time requirements.
- Add instructor preferences or peer ratings.
- Suggest multiple schedules or rank them.
- Integrate with university systems (LMS/portal) for real-time data.
