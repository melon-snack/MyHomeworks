-- Homework
-- marvel_not_normal.db предоставлен в предыдущем задании

-- Основные задания

-- 1. Общее количество персонажей по статусу
SELECT ALIVE, COUNT(*) AS status_count
FROM MarvelCharacters
WHERE ALIVE IS NOT NULL
GROUP BY ALIVE
ORDER BY status_count DESC;