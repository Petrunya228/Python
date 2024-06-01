SELECT avg(assignments_grades.grade), assignment_text
FROM assignments_grades
JOIN assignments ON assignments_grades.assisgnment_id = assignments.assisgnment_id
WHERE assignment_text LIKE '%прочитать%' OR assignment_text LIKE '%выучить%'
GROUP BY assignment_text