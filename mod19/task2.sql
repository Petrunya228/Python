SELECT students.full_name, avg(assignments_grades.grade)
FROM students
JOIN assignments_grades ON assignments_grades.student_id = students.student_id
GROUP BY students.student_id
ORDER BY avg(assignments_grades.grade) DESC
LIMIT 10

