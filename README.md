# Forensic-Adjacent Password Generator

## Description
This is an independent Python script built during my Week 3 foundations milestone. The program prompts a user for a base phrase and a security level, utilizes advanced shuffling logic to scramble the input text, and injects randomized digits, letters, or symbols to maximize password.

## Programming Concepts Used
- **Custom Functions & Variable Scope**: Segmented logic into dedicated execution areas.
- **Conditional Logic**: Utilized `if/elif/else` streams for security tiering and error handling.
- **External Modules**: Leveraged `random.sample`, `random.choices`, and `string` libraries.
- **Data Structure Manipulation**: Used `"".join()` to transform list outputs back into cohesive strings.

## Future Milestones
- Implement loops to filter out blank spaces from the base phrase.
- Integrate hashing functions (like SHA-256) to simulate secure forensic credential storage.
