create table `Species` (
	`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name` VARCHAR(50) NOT NULL
);
insert into `Species` (id, name) values (1, "Procyon cancrivorus");
insert into `Species` (id, name) values (2, "Aonyx cinerea");
insert into `Species` (id, name) values (3, "Pitangus sulphuratus");
insert into `Species` (id, name) values (4, "Nannopterum harrisi");
insert into `Species` (id, name) values (5, "Tamiasciurus hudsonicus");

create table `Owners` (
	`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`first_name` VARCHAR(50) NOT NUll,
	`last_name` VARCHAR(50) NOT NULL,
	`email` VARCHAR(50) NOT NULL
);
insert into `Owners` (id, first_name, last_name, email) values (1, "Jarrett", "Thunder", "jthunder0@amazon.de");
insert into `Owners` (id, first_name, last_name, email) values (2, "Charline", "Manton", "cmanton1@china.com.cn");
insert into `Owners` (id, first_name, last_name, email) values (3, "Lura", "Cornbell", "lcornbell2@ning.com");
insert into `Owners` (id, first_name, last_name, email) values (4, "Bo", "Pearn", "bpearn3@hp.com");
insert into `Owners` (id, first_name, last_name, email) values (5, "Veronike", "Hellings", "vhellings4@utexas.edu");
insert into `Owners` (id, first_name, last_name, email) values (6, "Yule", "Tilmouth", "ytilmouth5@nps.gov");
insert into `Owners`(id, first_name, last_name, email) values (7, "Agata", "Vasilmanov", "avasilmanov6@fema.gov");
insert into `Owners` (id, first_name, last_name, email) values (8, "Irvin", "Folshom", "ifolshom7@mapquest.com");
insert into `Owners` (id, first_name, last_name, email) values (9, "Jeanna", "Dyas", "jdyas8@amazon.co.uk");
insert into `Owners` (id, first_name, last_name, email) values (10, "Ulick", "Drinkhill", "|udrinkhill9@wsj.com");

create table `Snakes` (
	`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name` VARCHAR(50) NOT NULL,
	`owner_id` INT NOT NULL,
	`species_id` INT NOT NULL,
	`gender` VARCHAR(50) NOT NULL,
	`color` VARCHAR(50) NOT NULL
);
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (1, "Annot??e", 2, 2, "Female", "Turquoise");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (2, "Lor??ne", 1, 1, "Male", "Green");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (3, "Aliz??e", 8, 1, "Female", "Blue");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (4, "Oc??ane", 7, 1, "Male", "Khaki");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (5, "Alm??rinda", 4, 4, "Male", "Yellow");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (6, "Ath??na", 3, 5, "Female", "Violet");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (7, "B??n??dicte", 8, 2, "Male", "Mauv");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (8, "Sol??ne", 2, 3, "Male", "Yellow");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (9, "A??", 6, 4, "Female", "Goldenrod");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (10, "Andr??a", 9, 5, "Male", "Turquoise");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (11, "No??mie", 6, 2, "Male", "Crimson");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (12, "Gwena??lle", 4, 1, "Male", "Puce");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (13, "Oc??ane", 9, 5, "Male", "Turquoise");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (14, "B??reng??re", 5, 2, "Female", "Turquoise");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (15, "Lys??a", 7, 2, "Male", "Fuscia");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (16, "M??ghane", 1, 2, "Male", "Crimson");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (17, "L??onore", 5, 1, "Female", "Yellow");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (18, "Ana??l", 6, 5, "Female", "Puce");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (19, "N??lie", 7, 1, "Female", "Pink");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (20, "B??atrice", 9, 1, "Female", "Green");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (21, "G??sta", 5, 2, "Female", "Mauv");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (22, "Cl??lia", 5, 3, "Male", "Purple");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (23, "M??ng", 2, 5, "Female", "Khaki");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (24, "Ang??lique", 2, 1, "Female", "Mauv");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (25, "Aim??e", 10, 2, "Female", "Pink");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (26, "Marie-fran??oise", 2, 1, "Female", "Green");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (27, "T??n", 4, 2, "Female", "Teal");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (28, "Andr??anne", 5, 4, "Female", "Green");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (29, "St??phanie", 8, 5, "Female", "Purple");
insert into `Snakes` (id, name, owner_id, species_id, gender, color) values (30, "Li??", 7, 1, "Female", "Maroon");