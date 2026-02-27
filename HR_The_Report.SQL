SELECT 
CASE
    WHEN Grade < 8 THEN 'NULL'
    ELSE Name
END AS Name,
Grade, Marks
FROM Students
JOIN Grades
ON Students.Marks BETWEEN Grades.Min_Mark AND Grades.Max_Mark
ORDER BY Grade DESC, 
CASE WHEN Grade >= 8 THEN Name END ASC, 
CASE WHEN Grade < 8 THEN Marks END ASC;
