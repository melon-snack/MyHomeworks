-- Homework

-- 1. Лысые злодеи из 90-х годов
SELECT name, FIRST_APPEARANCE, Year, APPEARANCES FROM MarvelCharacters
WHERE
    HAIR = 'Bald'
    AND ALIGN = 'Bad Characters'
    AND Year BETWEEN 1990 AND 1999

-- 2. Герои с тайной идентичностью и необычными глазами
SELECT name, FIRST_APPEARANCE, year, EYE FROM MarvelCharacters
WHERE
    Year IS NOT NULL
    AND FIRST_APPEARANCE IS NOT NULL
    AND EYE IS NOT NULL
    AND identify = 'Secret Identity'
    AND EYE != 'Blue Eyes'
    AND EYE != 'Brown Eyes'
    AND EYE != 'Green Eyes'

-- 3. Персонажи с изменяющимся цветом волос
SELECT name, HAIR FROM MarvelCharacters
WHERE HAIR = 'Variable Hair'

-- 4. Женские персонажи с редким цветом глаз
SELECT name, EYE FROM MarvelCharacters
WHERE
    (SEX = 'Female Characters'
    AND EYE = 'Gold Eyes')
OR
    (EYE = 'Amber Eyes'
    AND SEX = 'Female Characters')

-- 5. Персонажи без двойной идентичности, сортированные по году появления
SELECT name, FIRST_APPEARANCE, Year FROM MarvelCharacters
WHERE
    identify = 'No Dual Identity'
ORDER BY Year DESC

-- 6. Герои и злодеи с необычными прическами
SELECT name, ALIGN, HAIR FROM MarvelCharacters
WHERE
    (ALIGN = 'Good Characters'
    AND HAIR IS NOT NULL
    AND HAIR != 'Brown Hair'
    AND HAIR != 'Black Hair'
    AND HAIR != 'Blond Hair'
    AND HAIR != 'Red Hair')
OR 
    (ALIGN = 'Bad Characters'
    AND HAIR IS NOT NULL
    AND HAIR != 'Brown Hair'
    AND HAIR != 'Black Hair'
    AND HAIR != 'Blond Hair'
    AND HAIR != 'Red Hair')

-- 7. Персонажи, появившиеся в определённое десятилетие
SELECT name, FIRST_APPEARANCE, Year FROM MarvelCharacters
WHERE
    Year BETWEEN 1960 AND 1969

-- 8. Персонажи с уникальным сочетанием цвета глаз и волос
SELECT name, EYE, HAIR FROM MarvelCharacters
WHERE
    EYE = 'Yellow Eyes'
    AND HAIR = 'Red Hair'

-- 9. Персонажи с ограниченным количеством появлений
SELECT name, APPEARANCES FROM MarvelCharacters
WHERE
    APPEARANCES < 10

-- 10. Персонажи с наибольшим количеством появлений
SELECT name, APPEARANCES FROM MarvelCharacters
ORDER BY APPEARANCES DESC
LIMIT 5