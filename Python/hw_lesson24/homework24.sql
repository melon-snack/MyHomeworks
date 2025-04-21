-- Homework

-- 1. Лысые злодеи из 90-х годов
SELECT name, FIRST_APPEARANCE, Year, APPEARANCES FROM MarvelCharacters
WHERE
    AND HAIR = 'Bald'
    AND ALIGN = 'Bad Characters'
    AND Year BETWEEN 1990 AND 1999

-- 2. Герои с тайной идентичностью и необычными глазами
SELECT name, FIRST_APPEARANCE, year, EYE FROM MarvelCharacters
WHERE
    Year IS NOT NULL
    AND FIRST_APPEARANCE IS NOT NULL
    AND EYE IS NOT NULL
    AND identify = 'Secret Identity'
    AND EYE IS NOT 'Blue Eyes'
    AND EYE IS NOT 'Brown Eyes'
    AND EYE IS NOT 'Green Eyes'

-- 3. Персонажи с изменяющимся цветом волос
SELECT name, HAIR FROM MarvelCharacters
WHERE HAIR = 'Variable Hair'

-- 4. Женские персонажи с редким цветом глаз
SELECT name, EYE FROM MarvelCharacters
WHERE
    EYE = 'Gold Eyes'
    AND SEX = 'Female Characters'
    OR EYE = 'Amber Eyes'
    AND SEX = 'Female Characters'

-- 5. Персонажи без двойной идентичности, сортированные по году появления
SELECT name, FIRST_APPEARANCE, Year FROM MarvelCharacters
WHERE
    identify = 'No Dual Identity'
ORDER BY Year DESC

-- 6. Герои и злодеи с необычными прическами
SELECT name, ALIGN, HAIR FROM MarvelCharacters
WHERE
    ALIGN = 'Good Characters'
    AND HAIR IS NOT NULL
    AND HAIR IS NOT 'Brown Hair'
    AND HAIR IS NOT 'Black Hair'
    AND HAIR IS NOT 'Blond Hair'
    AND HAIR IS NOT 'Red Hair'
    OR ALIGN = 'Bad Characters'
    AND HAIR IS NOT NULL
    AND HAIR IS NOT 'Brown Hair'
    AND HAIR IS NOT 'Black Hair'
    AND HAIR IS NOT 'Blond Hair'
    AND HAIR IS NOT 'Red Hair'

-- 7. Персонажи, появившиеся в определённое десятилетие
SELECT name, FIRST_APPEARANCE, Year FROM MarvelCharacters
WHERE
    Year BETWEEN 1960 AND 1969