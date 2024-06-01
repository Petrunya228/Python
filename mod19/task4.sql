SELECT max(hw), avg(hw), min(hw)
FROM (
SELECT sum(assignments_grades.date > assignments.due_date) as hw
FROM assignments
JOIN assignments_grades ON assignments.assisgnment_id = assignments_grades.assisgnment_id
GROUP BY assignments.group_id
)

