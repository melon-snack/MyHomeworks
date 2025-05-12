-- Homework
-- Создание таблицы мастеров
CREATE TABLE IF NOT EXISTS Masters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    middle_name TEXT,
    phone TEXT
);

-- Создание таблицы услуг
CREATE TABLE IF NOT EXISTS Services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE,
    description TEXT,
    price INTEGER
);

-- Создание таблицы записи на услуги
CREATE TABLE IF NOT EXISTS Appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    дата DATE DEFAULT CURRENT_TIMESTAMP,
    master_id INTEGER DEFAULT NULL,
    status TEXT,
    FOREIGN KEY (master_id) REFERENCES Masters(id) ON DELETE SET DEFAULT ON UPDATE CASCADE
);
