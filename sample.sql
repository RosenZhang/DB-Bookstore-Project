#book sample 
insert into books values ('Photoshop Elements 9: The Missing Manual','https://www.google.com.sg/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwi9nsen0dvXAhUDPY8KHRZVD94QjRwIBw&url=https%3A%2F%2Fwww.amazon.com%2FAdobe-Photoshop-Elements-Win-VERSION%2Fdp%2FB003YGMEAQ&psig=AOvVaw0fLmCM6yxYYPmG3RtKTSeI&ust=1511764909863041','paperback','640','English','Photography','Barbara Brundage','Pogue Press','2010','1449389678','978-1449389673','20');
insert into books values ('Where Good Ideas Come From: The Natural History of Innovation','https://www.google.com.sg/imgres?imgurl=https%3A%2F%2Fimages.gr-assets.com%2Fbooks%2F1311705993l%2F8034188.jpg&imgrefurl=https%3A%2F%2Fwww.goodreads.com%2Fbook%2Fshow%2F8034188-where-good-ideas-come-from&docid=H44zSRceOsMAGM&tbnid=wKLRMTu0MDUbEM%3A&vet=10ahUKEwjA06ef0tvXAhWD6Y8KHeGUA4gQMwg9KAAwAA..i&w=315&h=475&client=safari&bih=738&biw=1280&q=Where%20Good%20Ideas%20Come%20From&ved=0ahUKEwjA06ef0tvXAhWD6Y8KHeGUA4gQMwg9KAAwAA&iact=mrc&uact=8','hardcover','336','Innovation','English','Steven Johnson','Riverhead Hardcover','2010','1594487715','978-1594487712','35');
insert into books values ('The Digital Photography Book','https://www.google.com.sg/imgres?imgurl=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FI%2F51vm11Ve5iL._SX332_BO1%2C204%2C203%2C200_.jpg&imgrefurl=https%3A%2F%2Fwww.amazon.com%2FDigital-Photography-Book-Part-2nd%2Fdp%2F0321934946&docid=_AdVGaSMmHOU4M&tbnid=5EfxEN_jcTC6hM%3A&vet=10ahUKEwjV95L60tvXAhXBNo8KHet2B7AQMwg9KAAwAA..i&w=334&h=499&client=safari&bih=738&biw=1280&q=The%20Digital%20Photography%20Book&ved=0ahUKEwjV95L60tvXAhXBNo8KHet2B7AQMwg9KAAwAA&iact=mrc&uact=8','paperback','219','Photography','English','Scott Kelby','Peachpit Press','2006','032147404X','978-0321474049','55');
insert into books values ('The Great Gatsby','https://www.google.com.sg/imgres?imgurl=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FM%2FMV5BMTkxNTk1ODcxNl5BMl5BanBnXkFtZTcwMDI1OTMzOQ%40%40._V1_UY1200_CR84%2C0%2C630%2C1200_AL_.jpg&imgrefurl=http%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt1343092%2F&docid=RbTRIACQyNVd0M&tbnid=-GjiCJ90J-Gj9M%3A&vet=10ahUKEwjVmY231NvXAhWLp48KHfE4DusQMwjRASgAMAA..i&w=630&h=1200&client=safari&bih=738&biw=1280&q=The%20Great%20Gatsby&ved=0ahUKEwjVmY231NvXAhWLp48KHfE4DusQMwjRASgAMAA&iact=mrc&uact=8','hardcover','216','English','Novel','F. Scott Fitzgerald','Scribner','1995','0684801523','978-0684801520','19');
insert into books values ('Davis s Drug Guide For Nurses (book With Cd-rom) And Mednotes: Nurse s Pocket Pharmacology Guide','https://www.google.com.sg/imgres?imgurl=https%3A%2F%2Fpictures.abebooks.com%2Fisbn%2F9780803612259-us-300.jpg&imgrefurl=https%3A%2F%2Fwww.abebooks.com%2F9780803612259%2FDaviss-Drug-Guide-Nurses-book-0803612257%2Fplp&docid=XS7TporsCCkNTM&tbnid=QdNCNA5RdTZ5gM%3A&vet=10ahUKEwiJyKbM1NvXAhXFto8KHVOsDZMQMwgmKAAwAA..i&w=300&h=480&itg=1&client=safari&bih=738&biw=1280&q=Davis%20s%20Drug%20Guide%20For%20Nurses%20(book%20With%20Cd-rom)%20And%20Mednotes&ved=0ahUKEwiJyKbM1NvXAhXFto8KHVOsDZMQMwgmKAAwAA&iact=mrc&uact=8','hardcover','1482','English','Medicine and Health Science','Judith Hopfer Deglin, April Hazard Vallerand','F. A. Davis Company','2004','0803612257','978-0803612259','26');

#order sample 
insert into orders values (now(),'1','1','978-1449389673');
insert into orders values (now(),'2','2','978-1594487712');
insert into orders values (now(),'1','3','978-0321474049');
insert into orders values (now(),'1','4','978-0684801520');
insert into orders values (now(),'1','5','978-0803612259');

#feedback
insert into feedback values (null,'5',now(),'Adobe’s Elements apps have shown the value of 
taking a quality software brand and providing a more affordable version for mainstream consumers.','1','978-1449389673');

insert into feedback values (null,'3',now(),'The Great Gatsby is a story told by Nick Carraway, who was once Gatsby neighbor,
 and he tells the story sometime after 1922, when the incidents that fill the book take place. ','3','978-0684801520');

#usefulness rating
insert into usefulness_rating values ('1','4','2');
insert into usefulness_rating values ('2','3','5');