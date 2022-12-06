CREATE TABLE contacts (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	title VARCHAR(30),
	organization VARCHAR(50)
);

CREATE TABLE items (
	contact VARCHAR(50),
	contact_id INT,
	contact_type_id INT,
	contact_category_id INT
);

CREATE TABLE contact_types (
	id INT PRIMARY KEY, 
	contact_type VARCHAR(30)
);

CREATE TABLE contact_categories (
	id INT PRIMARY KEY, 
	contact_category VARCHAR(30)
);

INSERT INTO contacts (first_name, last_name, title, organization)
VALUES ('Erik', 'Eriksson', 'Teacher', 'Utbildning AB'),
('Anna', 'Sundh', '',''),
('Goran', 'Bregovic', 'Coach', 'Dalens IK'),
('Ann-Marie', 'Bergqvist', 'Cousin',''),
('Herman', 'Appelkvist','','')

SELECT * FROM contacts;

INSERT INTO items (contact, contact_id, contact_type_id, contact_category_id)
VALUES ('011-12 33 45', 3, 2, 1),
('goran@infoab.se', 3, 1, 2),
('010-88 55 44', 4, 2, 2),
('erik57@hotmail.com', 1, 1,1),
('@annapanna98', 2, 4, 1),
('077-563578', 2, 2,1),
('070-156 22 78', 3, 2, 2)

 
 INSERT INTO contact_types (id, contact_type)
 VALUES(1, 'Email'),(2, 'Phone'), (3, 'Skype'), (4,'Instagram');
 
 INSERT INTO contact_categories(id, contact_category)
 VALUES(1, 'Home'), (2,'Work'), (3, 'Fax');
 
INSERT INTO contacts(first_name, last_name, title, organization)
VALUES('Sebastian', 'Ström', '', ''), ('Cristiano', 'Ronaldo', '', '')

SELECT id AS unused_contact_types FROM contact_types
EXCEPT
SELECT contact_type_id FROM items;

CREATE VIEW view_contacts AS  
SELECT first_name, last_name, contact, contact_type, contact_category
FROM contacts, items, contact_types, contact_categories;

SELECT * FROM contacts, items, contact_types, contact_categories;

//

SELECT * FROM contacts
CROSS JOIN items
CROSS JOIN contact_types
CROSS JOIN contact_categories;
