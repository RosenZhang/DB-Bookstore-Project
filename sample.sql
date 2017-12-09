#book sample 
insert into books values ('Photoshop Elements 9: The Missing Manual','https://images-na.ssl-images-amazon.com/images/I/61SC2Pbc+aL._SL1001_.jpg','paperback','640','English','Photography','Barbara Brundage','Pogue Press','2010','1449389678','978-1449389670',30);
insert into books values ('Where Good Ideas Come From: The Natural History of Innovation','https://images.gr-assets.com/books/1311705993l/8034188.jpg','hardcover','336','Innovation','English','Steven Johnson','Riverhead Hardcover','2010','1594487715','978-1594487711',50);
insert into books values ('The Digital Photography Book','https://images-na.ssl-images-amazon.com/images/I/51vm11Ve5iL._SX332_BO1,204,203,200_.jpg','paperback','219','Photography','English','Scott Kelby','Peachpit Press','2006','032147404X','978-0321474042',50);
insert into books values ('The Great Gatsby','https://www.gannett-cdn.com/-mm-/0c9109c71ea0524d9fe840f91fabd67bb94a26a9/r=537&c=0-0-534-712/local/-/media/USATODAY/USATODAY/2013/05/07/gatsby-mti-jacket-3_4.jpg','hardcover','216','English','Novel','F. Scott Fitzgerald','Scribner','1995','0684801523','978-0684801523',10);
insert into books values ('Davis s Drug Guide For Nurses (book With Cd-rom) And Mednotes: Nurse s Pocket Pharmacology Guide','https://pictures.abebooks.com/isbn/9780803612259-us-300.jpg','hardcover','1482','English','Medicine and Health Science','Judith Hopfer Deglin, April Hazard Vallerand','F. A. Davis Company','2004','0803612257','978-0803612254',20);
insert into books values ('iPhone and iPad Apps for Absolute Beginners (Getting Started)','https://images-na.ssl-images-amazon.com/images/I/41HwMsPKmdL._SX403_BO1,204,203,200_.jpg','paperback','336','English','Database & Big Data','Rory Lewis','Apress','2010','1430227001','978-1430227005',40);
insert into books values ('Statistics for People Who (Think They) Hate Statistics: Excel 2007 Edition','https://images-na.ssl-images-amazon.com/images/I/51G2yC0jYEL._SX348_BO1,204,203,200_.jpg','paperback','424','English','Statistics',NULL,'Sage Publications, Inc','2009','1412971020','978-1412971026',30);
insert into books values ('The Wealth of Nations (Bantam Classics)','https://images-na.ssl-images-amazon.com/images/I/51BQGhex0xL._SX298_BO1,204,203,200_.jpg',NULL,NULL,'English','Economics','Adam Smith','Bantam Classics ','2003','0553585975','978-0553585977',20);
insert into books values ('Frankenstein (Cambridge Literature)','https://images-na.ssl-images-amazon.com/images/I/81MCfbaipLL.jpg','paperback','286','English','literature','Mary Shelley','Cambridge University Press ','1998','0521587026','978-0521587028',40);
insert into books values ('Calculus, 8th Edition','https://images-na.ssl-images-amazon.com/images/I/51jitgi3EaL._SX423_BO1,204,203,200_.jpg',NULL,NULL,'English','Mathematics','Dale Varberg, Edwin J. Purcell, Steven E. Rigdon','Prentice Hall','2000','0130811378','978-0130811379',10);


#order sample :Odate DATETIME(2); copynum; userid; bid
insert into orders values (now(),1,'1','978-1449389670');
insert into orders values (now(),1,'1','978-1594487711');
insert into orders values (now(),3,'2','978-0803612254');
insert into orders values (now(),1,'2','978-1594487711');
insert into orders values (now(),1,'2','978-1412971026');
insert into orders values (now(),1,'3','978-0321474042');
insert into orders values (now(),2,'3','978-0521587028');
insert into orders values (now(),2,'4','978-0684801523');
insert into orders values (now(),1,'4','978-1594487711');
insert into orders values (now(),2,'4','978-1430227005');
insert into orders values (now(),1,'5','978-0803612254');
insert into orders values (now(),2,'5','978-0553585977');
insert into orders values (now(),1,'5','978-0130811379');



#feedback: Fid; rank; Fdate; Fcomment; Feedback_giver; bid
insert into feedback values (null,8,now(),'Adobe’s Elements apps have shown the value of 
taking a quality software brand and providing a more affordable version.','1','978-1449389670');


insert into feedback values (null,5,now(),'This novel sparks the thoughts that life is really best lived 
and known in the suffering and striving.','3','978-0684801523');

insert into feedback values (null,2,now(),'Unfortunately for me I took a class where this book was the required text 
and was forced to read it despite my reluctance.','4','978-1430227005');
 
insert into feedback values (null,9,now(),' can not say it will make anyone like statistics 
but it is better than the usual statistic textbook, for sure. ','2','978-1412971026');

insert into feedback values (null,8,now(),'Books like Wealth of Nations are the sorts of things that set in motion the minds that 
helped build our nation after we declared our independence.','4','978-0553585977');

insert into feedback values (null,6,now(),'It will prove a useful addition to any university collection on the humanities.'
,'3','978-0521587028');

insert into feedback values (null,4,now(),'Needed it for class. I believe this can be used for calc 1-3.'
,'5','978-0130811379');

insert into feedback values (null,10,now(),'Book operates around 5 major concepts:.......','1','978-1594487711');
insert into feedback values (null,2,now(),'Hmm, here we go again. Another \'popular / best selling\' author with a \'great\' book full of \'new\' insights.','2','978-1594487711');
insert into feedback values (null,4,now(),'I tend to avoid reading this kind of book.','4','978-1594487711');
 
#usefulness rating: Fid; score; userid
insert into usefulness_rating values ('1',2,'2');
insert into usefulness_rating values ('2',1,'5');
insert into usefulness_rating values ('2',0,'3');
insert into usefulness_rating values ('8',2,'3');
insert into usefulness_rating values ('8',2,'4');
insert into usefulness_rating values ('8',0,'1');
insert into usefulness_rating values ('9',1,'3');
insert into usefulness_rating values ('9',1,'4');
insert into usefulness_rating values ('9',1,'5');
insert into usefulness_rating values ('10',1,'1');
insert into usefulness_rating values ('10',0,'3');
insert into usefulness_rating values ('10',1,'4');

#transcation data: Tid; Tdate; copynum;bid 
insert into record_transaction values (null,now(),5,'978-1449389670');
insert into record_transaction values (null,now(),10,'978-1594487711');
insert into record_transaction values (null,now(),10,'978-0321474042');
insert into record_transaction values (null,now(),10,'978-0684801523');
