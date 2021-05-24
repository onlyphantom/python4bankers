PRAGMA table_info(records);

ALTER TABLE records
RENAME COLUMN term_cat TO term_category;

PRAGMA table_info(records);