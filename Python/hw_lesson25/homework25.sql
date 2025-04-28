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

-- 3. Максимальное количество появлений у персонажей с определенным цветом волос
SELECT HAIR AS color, MAX(APPEARANCES)
FROM MarvelCharacters
WHERE HAIR IS NOT NULL
GROUP BY HAIR
ORDER BY MAX(APPEARANCES) DESC;

-- 4. Минимальное количество появлений среди персонажей с известной и публичной личностью
SELECT identify, MIN(APPEARANCES)
FROM MarvelCharacters
WHERE identify = 'Public Identity'
GROUP BY identify
ORDER BY MIN(APPEARANCES) DESC;

-- 5. Общее количество персонажей по полу
SELECT SEX, COUNT(*) AS sex_count
FROM MarvelCharacters
WHERE SEX IS NOT NULL
GROUP BY SEX
ORDER BY sex_count DESC;

-- 6. Средний год первого появления персонажей с различным типом личности
SELECT identify, AVG(Year)
FROM MarvelCharacters
WHERE identify IS NOT NULL
GROUP BY identify
ORDER BY AVG(Year) DESC;

-- 7. Количество персонажей с разным цветом глаз среди живых
SELECT EYE AS color, COUNT(*) AS eye_count
FROM MarvelCharacters
WHERE
    EYE IS NOT NULL
    AND ALIVE = 'Living Characters'
GROUP BY EYE
ORDER BY eye_count DESC;

-- 8. Максимальное и минимальное количество появлений среди персонажей с определенным цветом волос
SELECT HAIR AS color, MAX(APPEARANCES), MIN(APPEARANCES)
FROM MarvelCharacters
WHERE HAIR IS NOT NULL
GROUP BY HAIR;
