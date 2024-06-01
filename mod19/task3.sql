SELECT teachers.full_name, avg(assignments_grades.grade)
FROM assignments_grades
JOIN assignments ON assignments_grades.assisgnment_id = assignments.assisgnment_id
JOIN teachers ON teachers.teacher_id = assignments.teacher_id
GROUP BY teachers.teacher_id
ORDER BY avg(assignments_grades.grade) DESC
LIMIT 1
