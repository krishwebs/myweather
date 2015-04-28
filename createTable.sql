CREATE TABLE IF NOT EXISTS `temperatures` (
`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
`temperature-1` DOUBLE NOT NULL ,
`temperature-2` DOUBLE NOT NULL ,
`temperature-3` DOUBLE NOT NULL ,
`temperature-4` DOUBLE NOT NULL ,
`pressure` VARCHAR( 22 ) NOT NULL ,
`pressure-sea` VARCHAR( 22 ) NOT NULL ,
`altitude` VARCHAR( 22 ) NOT NULL
) ENGINE = MYISAM ;
