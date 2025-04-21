-- Homework

-- 1. Лысые злодеи из 90-х годов
SELECT name, FIRST_APPEARANCE, Year, APPEARANCES FROM MarvelCharacters
WHERE
    AND HAIR = 'Bald'
    AND ALIGN = 'Bad Characters'
    AND Year BETWEEN 1990 AND 1999