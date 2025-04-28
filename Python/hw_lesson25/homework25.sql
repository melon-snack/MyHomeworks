-- Homework
-- marvel_not_normal.db предоставлен в предыдущем задании

-- Основные задания

-- 1. Общее количество персонажей по статусу
SELECT ALIVE, COUNT(*) AS status_count
FROM MarvelCharacters
WHERE ALIVE IS NOT NULL
GROUP BY ALIVE
ORDER BY status_count DESC;

-- 2. Среднее количество появлений персонажей с разным цветом глаз
SELECT EYE AS color, AVG(APPEARANCES)
FROM MarvelCharacters
WHERE EYE IS NOT NULL
GROUP BY EYE
ORDER BY AVG(APPEARANCES) DESC;
