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