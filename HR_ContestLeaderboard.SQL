SELECT h.hacker_id, h.name, SUM(topScore) as totalScore
FROM Hackers h
JOIN (
    SELECT hacker_id, MAX(score) as topScore
    FROM Submissions
    GROUP BY hacker_id, challenge_id
) s
ON h.hacker_id = s.hacker_id
GROUP BY h.hacker_id, h.name
HAVING SUM(topScore) > 0
ORDER BY SUM(topScore) DESC, h.hacker_id ASC;
