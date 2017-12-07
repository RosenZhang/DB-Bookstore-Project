#book sample 
insert into books values ('Photoshop Elements 9: The Missing Manual','https://images-na.ssl-images-amazon.com/images/I/61SC2Pbc+aL._SL1001_.jpg','paperback','640','English','Photography','Barbara Brundage','Pogue Press','2010','1449389678','978-1449389673','20');
insert into books values ('Where Good Ideas Come From: The Natural History of Innovation','https://images.gr-assets.com/books/1311705993l/8034188.jpg','hardcover','336','Innovation','English','Steven Johnson','Riverhead Hardcover','2010','1594487715','978-1594487712','35');
insert into books values ('The Digital Photography Book','https://images-na.ssl-images-amazon.com/images/I/51vm11Ve5iL._SX332_BO1,204,203,200_.jpg','paperback','219','Photography','English','Scott Kelby','Peachpit Press','2006','032147404X','978-0321474049','55');
insert into books values ('The Great Gatsby','https://www.gannett-cdn.com/-mm-/0c9109c71ea0524d9fe840f91fabd67bb94a26a9/r=537&c=0-0-534-712/local/-/media/USATODAY/USATODAY/2013/05/07/gatsby-mti-jacket-3_4.jpg','hardcover','216','English','Novel','F. Scott Fitzgerald','Scribner','1995','0684801523','978-0684801520','19');
insert into books values ('Davis s Drug Guide For Nurses (book With Cd-rom) And Mednotes: Nurse s Pocket Pharmacology Guide','https://pictures.abebooks.com/isbn/9780803612259-us-300.jpg','hardcover','1482','English','Medicine and Health Science','Judith Hopfer Deglin, April Hazard Vallerand','F. A. Davis Company','2004','0803612257','978-0803612259','26');

#order sample 
insert into orders values (now(),'1','1','978-1449389673');
insert into orders values (now(),'2','2','978-1594487712');
insert into orders values (now(),'1','3','978-0321474049');
insert into orders values (now(),'1','2','978-0684801520');
insert into orders values (now(),'1','3','978-0803612259');

#feedback
insert into feedback values (null,'5',now(),'Adobe’s Elements apps have shown the value of 
taking a quality software brand and providing a more affordable version for mainstream consumers.','1','978-1449389673');

insert into feedback values (null,'3',now(),'The Great Gatsby is a story told by Nick Carraway, who was once Gatsby neighbor,
 and he tells the story sometime after 1922, when the incidents that fill the book take place. ','3','978-0684801520');
insert into feedback values (null,'7',now(),'The Great Gatsby is good ','2','978-0684801520');
insert into feedback values (null,'9',now(),'The Great Gatsby is good ','1','978-0684801520');

#usefulness rating
insert into usefulness_rating values ('1','2','2');
insert into usefulness_rating values ('2','1','1');
