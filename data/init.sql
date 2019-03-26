CREATE DATABASE shoppingbasket;

USE shoppingbasket;

CREATE TABLE IF NOT EXISTS `User` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `status` enum('active','disable','deleted') default 'active',
  PRIMARY KEY (`id`),
  UNIQUE KEY(`email`)
);

CREATE TABLE IF NOT EXISTS `Product` (

  `id` int(11) NOT NULL auto_increment,   
  `name` varchar(250) NOT NULL ,
  `description` varchar(250) NOT NULL default '',       
  `code` varchar(50)  NOT NULL ,     
  `price`  float(11) NOT NULL default '0', 
  `image`  varchar(100) NOT NULL default '',
  `status` enum('active','disable','deleted') default 'active',
   PRIMARY KEY  (`id`),
   UNIQUE KEY(`code`)
);


CREATE TABLE IF NOT EXISTS `Basket` (

  `id` int(11) NOT NULL auto_increment,   
  `userid` int(11) NOT NULL default '0',       
  `sessionid` varchar(250)  NOT NULL default '0',     
  `productcode`  varchar(50) NOT NULL,     
  `qty` int(11)  NOT NULL default '0',    
  `status` enum('active','disable','deleted') default 'active',
   PRIMARY KEY  (`id`)
);

INSERT INTO `User` (`firstname`, `lastname`, `email`, `status`) 
	VALUES ('Muhamamad ', 'Umair', 'engrumair_sabir@yahoo.com', 'active');

INSERT INTO `User` (`firstname`, `lastname`, `email`, `status`) 
	VALUES ('Peter ', 'Ahrens', 'peter@bigpoint.com', 'active');

INSERT INTO `Product` (`name`, `description`,`code`, `price`, `image`, `status`) 
	VALUES ('test product one', 'this is just for test', 'ski45tz', '45', 'vxcvsdfsfsfwe543335345353rsdffscxvxvvxv', 'active');

INSERT INTO `Product` (`name`, `description`,`code`, `price`, `image`, `status`)  
	VALUES ('test product two', 'this is just for test','vcxdfe345', '28', 'vxcvsdfsfsfwe543335345353rsdffscxvxvvxv', 'active');

INSERT INTO `Product` (`name`, `description`,`code`, `price`, `image`, `status`)  
	VALUES ('test product three', 'this is just for test','fdsd33435', '10', 'vxcvsdfsfsfwe543335345353rsdffscxvxvvxv', 'disable');

INSERT INTO `Product` (`name`, `description`,`code`, `price`, `image`, `status`) 
	VALUES ('test product four', 'this is just for test', 'fdfdsd34345', '23', 'vxcvsdfsfsfwe543335345353rsdffscxvxvvxv', 'deleted');


INSERT INTO `Basket` (`userid`, `sessionid`, `productcode`, `qty`, `status`) 
	VALUES ('1', 'sdsfsxcxyxxcsdasdwqeqadwdaycyxcycx', 'fdsd33435', '1', 'active');

INSERT INTO `Basket` (`userid`, `sessionid`, `productcode`, `qty`, `status`) 
	VALUES ('1', 'sdsfsxcxyxxcsdasdwqeqadwdaycyxcycx', 'vcxdfe345', '3', 'deleted');

INSERT INTO `Basket` (`userid`, `sessionid`, `productcode`, `qty`, `status`) 
	VALUES ('2', 'vcxvdfsfderwwrtrgfhfghgfhf', 'fdsd33435', '2', 'active');

