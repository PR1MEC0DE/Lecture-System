
# Lecture System

## Overview
This project implements a small object-oriented system based on the `Lecture` object designed in Lab 1.  
It models how lectures, courses, students, and classrooms interact.

## Classes
- **Lecture**: stores details about a lecture, manages attendees, and prints lecture information.
- **Course**: holds multiple lectures.
- **Student**: represents a student who can attend lectures.
- **Classroom**: represents a physical location for lectures.

## Diagram (from Lab 1)
![Diagram](A_pair_of_Class_Diagram_illustrations_depict_objec.png)

## Reflection
Compared to Lab 1, the following changes were made:
- Added constructor methods (`__init__`) and simple `print()` actions.
- Added relationships between classes (e.g., Course → Lecture → Student).
- Gave each class a practical behavior to make the system interactive.

## AI Feedback
The AI suggested adding a `Professor` class and a `Schedule` system.  
I decided **not** to include them yet to keep the example minimal and readable.

## Bonus Feedback
A colleague suggested renaming `add_attendee` to `register_student` for clarity.  
I didn’t change it because the current name matches the lecture context better.
