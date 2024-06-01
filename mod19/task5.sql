SELECT students_groups.group_id, students_count, average_grade_in_group, count_missed_hw, count_repeated_hw, count_passed_hw
FROM students_groups sg
JOIN (
SELECT assignments.group_id, avg(assignments_grades.grade) as average_grade_in_group, sum(assignments_grades.date > assignments.due_date) as count_missed_hw, count(assignments_grades.student_id) - count(DISTINCT assignments_grades.student_id) as count_repeated_hw
FROM assignments
JOIN assignments_grades ON assignments.assisgnment_id = assignments_grades.assisgnment_id
GROUP BY assignments.group_id
) as table_assignments
ON students_groups.group_id = table_assignments.group_id
JOIN (
SELECT students.group_id, count(DISTINCT students.student_id) as students_count, count(DISTINCT students.student_id) - count(DISTINCT assignments_grades.student_id) as count_passed_hw
FROM students
LEFT JOIN assignments_grades ag ON students.student_id = assignments_grades.student_id
GROUP BY students.group_id
) as table_students
ON students_groups.group_id = table_students.group_id
GROUP BY students_groups.group_id


