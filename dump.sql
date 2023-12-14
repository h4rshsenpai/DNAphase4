-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: sql12.freesqldatabase.com    Database: sql12368590
-- ------------------------------------------------------
-- Server version	5.5.62-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AGENT`
--

DROP TABLE IF EXISTS `AGENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AGENT` (
  `agent_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `data_of_birth` date DEFAULT NULL,
  `nationality` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`agent_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AGENT`
--

LOCK TABLES `AGENT` WRITE;
/*!40000 ALTER TABLE `AGENT` DISABLE KEYS */;
INSERT INTO `AGENT` VALUES (1,'Pere Guardiola',NULL,'Spain'),(2,'Damir Smoljan',NULL,NULL),(3,'Mark Pulisic',NULL,'USA'),(4,'Jorge Messi',NULL,'Argentina'),(5,'Pinhas Zahavi',NULL,'Israel'),(6,'AC Talent',NULL,'Spain'),(7,'Soccer Promaster',NULL,'Portugal'),(8,'Mario Namic',NULL,'Croatia'),(9,'Mino Raiola',NULL,'Italy'),(10,'Dane Rashford',NULL,'England'),(11,'The Player Management',NULL,'Spain'),(12,'Arena 11 Sports Group',NULL,'Germany'),(13,'The Bahia Internacional',NULL,'Spain'),(14,'Kia Joorabchian',NULL,'Great Britain'),(15,'Pablo Barquero',NULL,NULL),(16,'Base Soccer Agency',NULL,'Great Britain'),(17,'Emeka Obasi',NULL,'Nigeria'),(18,'HMH Sport Management',NULL,'Germany'),(19,'Thierry Hazard',NULL,'Belgium'),(20,'Oscar Ribot',NULL,'Spain');
/*!40000 ALTER TABLE `AGENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CLUB`
--

DROP TABLE IF EXISTS `CLUB`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CLUB` (
  `club_id` int(11) NOT NULL AUTO_INCREMENT,
  `club_name` varchar(256) DEFAULT NULL,
  `home_ground` varchar(256) DEFAULT NULL,
  `foundation_year` int(11) NOT NULL,
  `street_address` varchar(256) DEFAULT NULL,
  `zip_code` varchar(256) NOT NULL,
  PRIMARY KEY (`club_id`),
  UNIQUE KEY `club_name` (`club_name`),
  KEY `zip_code` (`zip_code`),
  CONSTRAINT `CLUB_ibfk_1` FOREIGN KEY (`zip_code`) REFERENCES `ZIP_MAP` (`zip_code`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CLUB`
--

LOCK TABLES `CLUB` WRITE;
/*!40000 ALTER TABLE `CLUB` DISABLE KEYS */;
INSERT INTO `CLUB` VALUES (1,'Chelsea','Stamford Bridge',1905,'Fulham Road','SW6 1HS'),(2,'Manchester United','Old Trafford',1902,'26 Sir Matt Busby Way','M16 0RA'),(3,'Manchester City','Etihad Stadium',1880,'Etihad Campus','M11 3FF'),(4,'Arsenal','Emirates Stadium',1886,'75 Drayton Park','N5 1BU'),(5,'Liverpool','Anfield',1892,'Anfield Road','L4 0TH'),(6,'Real Madrid','Santiago Bernabeu',1902,'Avda. de Concha Espina 1','28036'),(7,'Barcelona','Camp Nou',1899,'C. d\'Aristides Maillol','08028'),(8,'Atletico Madrid','Metropolitano Stadium',1903,'Pase Virgen del Puerto 67','28005'),(9,'Bayern Munich','Allianz Arena',1900,'Amtsgericht StraÃŸe','D-81547'),(10,'Borussia Dortmund','Signal Iduna Park',1909,'Strobelallee 50','44139');
/*!40000 ALTER TABLE `CLUB` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `COACH`
--

DROP TABLE IF EXISTS `COACH`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `COACH` (
  `name` varchar(256) NOT NULL,
  `manager_id` int(11) NOT NULL,
  `nationality` varchar(256) DEFAULT NULL,
  `designation` varchar(256) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  PRIMARY KEY (`name`,`manager_id`),
  KEY `manager_id` (`manager_id`),
  CONSTRAINT `COACH_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `MANAGER` (`manager_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `COACH`
--

LOCK TABLES `COACH` WRITE;
/*!40000 ALTER TABLE `COACH` DISABLE KEYS */;
INSERT INTO `COACH` VALUES ('Jody Morris',3,'England','Assistant Manager','1978-12-22'),('Michal Carrick',4,'England','First team Coach','1981-07-21');
/*!40000 ALTER TABLE `COACH` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MANAGER`
--

DROP TABLE IF EXISTS `MANAGER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MANAGER` (
  `manager_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `nationality` varchar(256) DEFAULT NULL,
  `current_club` varchar(256) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  PRIMARY KEY (`manager_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MANAGER`
--

LOCK TABLES `MANAGER` WRITE;
/*!40000 ALTER TABLE `MANAGER` DISABLE KEYS */;
INSERT INTO `MANAGER` VALUES (1,'Ronald Koeman','Netherland','Barcelona','1963-03-21'),(2,'Hansi flick','Germany','Bayern Munich','1965-02-22'),(3,'Frank Lampard','England','Chelsea','1978-06-22'),(4,'Ole Gunnar Solsjkaer','Norway','Manchester United','1973-02-26'),(5,'Jurgen Klopp','Germany','Liverpool','1967-06-16'),(6,'Josep Guardiola','Spain','Manchester City','1971-01-18'),(7,'Mikel Arteta','Spain','Arsenal','1982-03-26'),(8,'Lucien Favre','Switzerland','Borussia Dortmund','1957-11-02'),(9,'Zinedine Zidane','France','Real Madrid','1972-06-23'),(10,'Diego Simeone','Uruguay','Atletico Madrid','1970-04-28'),(11,'Niko Kovac','Croatia',NULL,'1971-08-15'),(12,'Ernesto Valverde','Spain',NULL,'1964-02-09');
/*!40000 ALTER TABLE `MANAGER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MANAGES`
--

DROP TABLE IF EXISTS `MANAGES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MANAGES` (
  `manager_id` int(11) NOT NULL,
  `club_id` int(11) NOT NULL,
  `season_year` varchar(256) NOT NULL,
  `no_of_win` int(11) NOT NULL,
  `no_of_loss` int(11) NOT NULL,
  `no_of_draw` int(11) NOT NULL,
  PRIMARY KEY (`manager_id`,`club_id`,`season_year`),
  KEY `club_id` (`club_id`),
  KEY `season_year` (`season_year`),
  CONSTRAINT `MANAGES_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `MANAGER` (`manager_id`),
  CONSTRAINT `MANAGES_ibfk_2` FOREIGN KEY (`club_id`) REFERENCES `CLUB` (`club_id`),
  CONSTRAINT `MANAGES_ibfk_3` FOREIGN KEY (`season_year`) REFERENCES `SEASON` (`season_year`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MANAGES`
--

LOCK TABLES `MANAGES` WRITE;
/*!40000 ALTER TABLE `MANAGES` DISABLE KEYS */;
INSERT INTO `MANAGES` VALUES (1,7,'2020-21',2,0,0),(2,9,'2019-20',33,2,1),(2,9,'2020-21',3,1,0),(3,1,'2019-20',29,18,8),(3,1,'2020-21',3,2,1),(4,2,'2019-20',34,12,15),(4,2,'2020-21',3,1,0),(5,5,'2019-20',42,8,5),(5,5,'2020-21',4,2,0),(6,3,'2019-20',42,12,5),(6,3,'2020-21',8,1,1),(7,4,'2019-20',16,6,6),(7,4,'2020-21',5,1,0),(8,10,'2019-20',28,11,7),(8,10,'2020-21',3,2,0),(9,6,'2019-20',22,7,11),(9,6,'2020-21',2,0,1),(10,8,'2019-20',24,9,17),(10,8,'2020-21',1,0,2),(11,9,'2019-20',10,3,3),(12,7,'2019-20',16,4,6);
/*!40000 ALTER TABLE `MANAGES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OWNER`
--

DROP TABLE IF EXISTS `OWNER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `OWNER` (
  `owner_id` int(11) NOT NULL AUTO_INCREMENT,
  `owner_name` varchar(256) NOT NULL,
  `country_origin` varchar(256) NOT NULL,
  PRIMARY KEY (`owner_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OWNER`
--

LOCK TABLES `OWNER` WRITE;
/*!40000 ALTER TABLE `OWNER` DISABLE KEYS */;
INSERT INTO `OWNER` VALUES (1,'Abu Dhabi United Group','UAE'),(3,'Stan Kroenke','USA'),(4,'BAMCO, Inc.','USA'),(5,'Lindsell Train Ltd.','UK');
/*!40000 ALTER TABLE `OWNER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OWNS`
--

DROP TABLE IF EXISTS `OWNS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `OWNS` (
  `owner_id` int(11) NOT NULL,
  `club_id` int(11) NOT NULL,
  `stake_percentage` float NOT NULL,
  PRIMARY KEY (`owner_id`,`club_id`),
  KEY `club_id` (`club_id`),
  CONSTRAINT `OWNS_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `OWNER` (`owner_id`),
  CONSTRAINT `OWNS_ibfk_2` FOREIGN KEY (`club_id`) REFERENCES `CLUB` (`club_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OWNS`
--

LOCK TABLES `OWNS` WRITE;
/*!40000 ALTER TABLE `OWNS` DISABLE KEYS */;
INSERT INTO `OWNS` VALUES (1,3,78),(3,4,29.9),(4,2,29.04),(5,2,28.44);
/*!40000 ALTER TABLE `OWNS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PLAYED_FOR`
--

DROP TABLE IF EXISTS `PLAYED_FOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PLAYED_FOR` (
  `player_id` int(11) NOT NULL,
  `club_id` int(11) NOT NULL,
  `season_year` varchar(256) NOT NULL,
  `minutes_played` int(11) NOT NULL DEFAULT '0',
  `goals` int(11) NOT NULL DEFAULT '0',
  `assists` int(11) NOT NULL DEFAULT '0',
  `clearances` int(11) NOT NULL DEFAULT '0',
  `tackles` int(11) NOT NULL DEFAULT '0',
  `red_cards` int(11) NOT NULL DEFAULT '0',
  `yellow_cards` int(11) NOT NULL DEFAULT '0',
  `saves` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`player_id`,`club_id`,`season_year`),
  KEY `club_id` (`club_id`),
  KEY `season_year` (`season_year`),
  CONSTRAINT `PLAYED_FOR_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `PLAYER` (`player_id`),
  CONSTRAINT `PLAYED_FOR_ibfk_2` FOREIGN KEY (`club_id`) REFERENCES `CLUB` (`club_id`),
  CONSTRAINT `PLAYED_FOR_ibfk_3` FOREIGN KEY (`season_year`) REFERENCES `SEASON` (`season_year`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PLAYED_FOR`
--

LOCK TABLES `PLAYED_FOR` WRITE;
/*!40000 ALTER TABLE `PLAYED_FOR` DISABLE KEYS */;
INSERT INTO `PLAYED_FOR` VALUES (1,3,'2019-20',11,0,0,0,0,0,0,0),(1,9,'2020-21',144,1,2,0,0,0,0,0),(2,9,'2019-20',4133,55,10,0,0,0,7,0),(2,9,'2020-21',326,1,3,0,0,0,0,0),(3,7,'2019-20',3810,31,26,0,0,0,7,0),(3,7,'2020-21',180,1,0,0,0,0,0,0),(4,7,'2019-20',2658,21,12,0,0,0,7,0),(4,8,'2020-21',152,2,1,0,0,0,0,0),(5,7,'2019-20',3986,1,0,0,0,0,20,0),(5,7,'2020-21',180,0,0,0,0,0,1,0),(6,8,'2019-20',2483,9,3,0,0,0,6,0),(6,8,'2020-21',237,1,1,0,0,0,1,0),(7,1,'2019-20',2348,11,10,0,0,0,0,0),(7,1,'2020-21',7,0,0,0,0,0,0,0),(8,1,'2019-20',3281,2,3,0,0,1,10,0),(8,1,'2020-21',291,0,0,0,0,0,1,0),(9,2,'2019-20',1608,1,4,0,0,0,2,0),(9,2,'2020-21',153,1,0,0,0,0,0,0),(10,2,'2019-20',3473,22,11,0,0,0,4,0),(10,2,'2020-21',212,2,0,0,0,0,0,0),(11,5,'2020-21',44,0,0,0,0,0,0,0),(11,9,'2019-20',2975,10,2,0,0,0,10,0),(12,5,'2019-20',3270,22,12,0,0,0,7,0),(12,5,'2020-21',260,3,0,0,0,0,1,0),(13,4,'2019-20',2342,2,2,0,0,0,2,0),(13,4,'2020-21',211,0,1,0,0,0,0,0),(14,1,'2019-20',3365,11,9,0,0,0,4,0),(14,4,'2020-21',226,0,2,0,0,0,0,0),(15,3,'2019-20',3709,4,2,0,0,0,13,0),(15,3,'2020-21',405,0,0,0,0,0,0,0),(16,3,'2019-20',3420,1,6,0,0,0,6,0),(16,3,'2020-21',270,0,0,0,0,0,0,0),(17,10,'2019-20',3274,20,20,0,0,0,2,0),(17,10,'2020-21',233,1,2,0,0,0,0,0),(18,10,'2019-20',3483,1,3,0,0,1,9,0),(18,10,'2020-21',436,0,0,0,0,0,2,0),(19,6,'2019-20',1545,1,7,0,0,0,1,0),(19,6,'2020-21',0,0,0,0,0,0,0,0),(20,6,'2019-20',3981,27,11,0,0,0,0,0),(20,6,'2020-21',267,0,1,0,0,0,0,0);
/*!40000 ALTER TABLE `PLAYED_FOR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PLAYED_IN_KNOCKOUT`
--

DROP TABLE IF EXISTS `PLAYED_IN_KNOCKOUT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PLAYED_IN_KNOCKOUT` (
  `tournament_name` varchar(256) NOT NULL,
  `club_id` int(11) NOT NULL,
  `season_year` varchar(256) NOT NULL,
  `no_of_draw` int(11) DEFAULT NULL,
  `no_of_win` int(11) DEFAULT NULL,
  `no_of_loss` int(11) DEFAULT NULL,
  `stage_of_exit` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`tournament_name`,`club_id`,`season_year`),
  KEY `season_year` (`season_year`),
  KEY `club_id` (`club_id`),
  CONSTRAINT `PLAYED_IN_KNOCKOUT_ibfk_1` FOREIGN KEY (`season_year`) REFERENCES `SEASON` (`season_year`),
  CONSTRAINT `PLAYED_IN_KNOCKOUT_ibfk_2` FOREIGN KEY (`club_id`) REFERENCES `CLUB` (`club_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PLAYED_IN_KNOCKOUT`
--

LOCK TABLES `PLAYED_IN_KNOCKOUT` WRITE;
/*!40000 ALTER TABLE `PLAYED_IN_KNOCKOUT` DISABLE KEYS */;
INSERT INTO `PLAYED_IN_KNOCKOUT` VALUES ('UEFA Champions League',1,'2019-20',2,3,3,'Round of 16'),('UEFA Champions League',3,'2019-20',2,6,1,'Quarter-finals'),('UEFA Champions League',5,'2019-20',1,4,3,'Round of 16'),('UEFA Champions League',6,'2019-20',2,3,3,'Round of 16'),('UEFA Champions League',7,'2019-20',3,5,1,'Quarter-finals'),('UEFA Champions League',8,'2019-20',3,5,1,'Quarter-finals'),('UEFA Champions League',9,'2019-20',0,11,0,'Winners'),('UEFA Champions League',10,'2019-20',1,4,3,'Round of 16');
/*!40000 ALTER TABLE `PLAYED_IN_KNOCKOUT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PLAYED_IN_LEAGUE`
--

DROP TABLE IF EXISTS `PLAYED_IN_LEAGUE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PLAYED_IN_LEAGUE` (
  `tournament_name` varchar(256) NOT NULL,
  `club_id` int(11) NOT NULL,
  `season_year` varchar(256) NOT NULL,
  `no_of_draw` int(11) DEFAULT NULL,
  `no_of_win` int(11) DEFAULT NULL,
  `no_of_loss` int(11) DEFAULT NULL,
  `goals_for` int(11) DEFAULT '0',
  `goals_against` int(11) DEFAULT '0',
  PRIMARY KEY (`tournament_name`,`club_id`,`season_year`),
  KEY `season_year` (`season_year`),
  KEY `club_id` (`club_id`),
  CONSTRAINT `PLAYED_IN_LEAGUE_ibfk_1` FOREIGN KEY (`season_year`) REFERENCES `SEASON` (`season_year`),
  CONSTRAINT `PLAYED_IN_LEAGUE_ibfk_2` FOREIGN KEY (`club_id`) REFERENCES `CLUB` (`club_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PLAYED_IN_LEAGUE`
--

LOCK TABLES `PLAYED_IN_LEAGUE` WRITE;
/*!40000 ALTER TABLE `PLAYED_IN_LEAGUE` DISABLE KEYS */;
INSERT INTO `PLAYED_IN_LEAGUE` VALUES ('Bundesliga',9,'2019-20',4,26,4,100,32),('Bundesliga',9,'2020-21',0,1,1,9,4),('Bundesliga',10,'2019-20',6,21,7,84,41),('Bundesliga',10,'2020-21',0,2,1,7,2),('English Premier League',1,'2019-20',6,20,12,69,54),('English Premier League',1,'2020-21',1,2,1,10,6),('English Premier League',2,'2019-20',12,18,8,66,36),('English Premier League',2,'2020-21',0,1,1,4,5),('English Premier League',3,'2019-20',3,26,9,102,35),('English Premier League',3,'2020-21',1,1,1,6,7),('English Premier League',4,'2019-20',14,14,10,56,48),('English Premier League',4,'2020-21',0,2,1,6,4),('English Premier League',5,'2019-20',3,32,3,85,33),('English Premier League',5,'2020-21',0,3,0,9,4),('La Liga',6,'2019-20',9,26,3,70,25),('La Liga',6,'2020-21',1,2,0,4,2),('La Liga',7,'2019-20',7,25,6,88,38),('La Liga',7,'2020-21',0,2,0,7,0),('La Liga',8,'2019-20',16,18,4,51,27),('La Liga',8,'2020-21',2,1,0,6,1);
/*!40000 ALTER TABLE `PLAYED_IN_LEAGUE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PLAYER`
--

DROP TABLE IF EXISTS `PLAYER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PLAYER` (
  `player_id` int(11) NOT NULL AUTO_INCREMENT,
  `player_name` varchar(256) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `nationality` varchar(256) DEFAULT NULL,
  `agent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`player_id`),
  KEY `agent_id` (`agent_id`),
  CONSTRAINT `PLAYER_ibfk_1` FOREIGN KEY (`agent_id`) REFERENCES `AGENT` (`agent_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PLAYER`
--

LOCK TABLES `PLAYER` WRITE;
/*!40000 ALTER TABLE `PLAYER` DISABLE KEYS */;
INSERT INTO `PLAYER` VALUES (1,'Leroy Sane','1996-01-12','Germany',2),(2,'Robert Lewandowski','1988-08-21','Poland',5),(3,'Lionel Messi','1987-06-24','Argentina',4),(4,'Luis Suarez','1987-02-24','Uruguay',1),(5,'Gerard Pique','1987-02-02','Spain',6),(6,'Joao Felix','1999-11-10','Portugal',7),(7,'Christian Pulisic','1998-09-19','USA',3),(8,'Mateo Kovacic','1994-05-06','Croatia',8),(9,'Paul Pogba','1993-03-15','France',9),(10,'Marcus Rashford','1997-10-22','England',10),(11,'Thiago','1991-04-11','Spain',11),(12,'Sadio Mane','1992-04-10','Senegal',12),(13,'Dani Ceballos','1996-08-07','Spain',13),(14,'Willian','1988-08-09','Brazil',14),(15,'Rodri','1996-06-22','Spain',15),(16,'Kyle Walker','1990-05-20','England',16),(17,'Jadon Sancho','2000-03-25','England',17),(18,'Mats Hummels','1998-12-16','Germany',18),(19,'Eden Hazard','1991-01-07','Belgium',19),(20,'Karim Benzema','1987-12-19','France',20);
/*!40000 ALTER TABLE `PLAYER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `POSITIONS`
--

DROP TABLE IF EXISTS `POSITIONS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `POSITIONS` (
  `position_name` varchar(256) NOT NULL,
  `player_id` int(11) NOT NULL,
  PRIMARY KEY (`position_name`,`player_id`),
  KEY `player_id` (`player_id`),
  CONSTRAINT `POSITIONS_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `PLAYER` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `POSITIONS`
--

LOCK TABLES `POSITIONS` WRITE;
/*!40000 ALTER TABLE `POSITIONS` DISABLE KEYS */;
INSERT INTO `POSITIONS` VALUES ('Left Winger',1),('Right Winger',1),('Centre Forward',2),('Centre Attacking Midfielder',3),('False Nine',3),('Right Winger',3),('Centre Forward',4),('Centre back',5),('Box-Box Midfielder',6),('Centre  Midfielder',6),('Centre Attacking midfielder',6),('Centre Forward',6),('False Nine',6),('Left Winger',6),('Right Winger',6),('Second Striker',6),('Left Winger',7),('Right Winger',7),('Box-Box Midfielder',9),('Centre  Midfielder',9),('Centre Forward',10),('Left Winger',10),('Right Winger',10),('Box-Box Midfielder',11),('Centre  Midfielder',11),('Centre Attacking Midfielder',11),('Left Winger',12),('Right Winger',12),('Box-Box Midfielder',13),('Centre  Midfielder',13),('Centre Attacking Midfielder',13),('Left Winger',14),('Right Winger',14),('Centre  Midfielder',15),('Defensive Midfielder',15),('Centre back',16),('Right Back',16),('Left Winger',17),('Right Winger',17),('Centre back',18),('Centre Attacking Midfielder',19),('Left Winger',19),('Centre Forward',20);
/*!40000 ALTER TABLE `POSITIONS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SEASON`
--

DROP TABLE IF EXISTS `SEASON`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SEASON` (
  `season_year` varchar(256) NOT NULL,
  PRIMARY KEY (`season_year`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SEASON`
--

LOCK TABLES `SEASON` WRITE;
/*!40000 ALTER TABLE `SEASON` DISABLE KEYS */;
INSERT INTO `SEASON` VALUES ('2019-20'),('2020-21');
/*!40000 ALTER TABLE `SEASON` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TOURNAMENT`
--

DROP TABLE IF EXISTS `TOURNAMENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TOURNAMENT` (
  `tournament_name` varchar(256) NOT NULL,
  `no_of_participants` int(11) NOT NULL,
  `tournament_type` varchar(256) NOT NULL,
  PRIMARY KEY (`tournament_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TOURNAMENT`
--

LOCK TABLES `TOURNAMENT` WRITE;
/*!40000 ALTER TABLE `TOURNAMENT` DISABLE KEYS */;
INSERT INTO `TOURNAMENT` VALUES ('Bundesliga',18,'League'),('English Premier League',20,'League'),('La liga',20,'League'),('UEFA Champions League',32,'Knockout');
/*!40000 ALTER TABLE `TOURNAMENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TRANSFER`
--

DROP TABLE IF EXISTS `TRANSFER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TRANSFER` (
  `player_id` int(11) NOT NULL,
  `club_from_id` int(11) NOT NULL,
  `club_to_id` int(11) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `transfer_fee` float NOT NULL,
  `agent_fee` float NOT NULL,
  `date_of_transfer` date NOT NULL,
  PRIMARY KEY (`player_id`,`club_from_id`,`club_to_id`,`agent_id`),
  KEY `club_from_id` (`club_from_id`),
  KEY `club_to_id` (`club_to_id`),
  KEY `agent_id` (`agent_id`),
  CONSTRAINT `TRANSFER_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `PLAYER` (`player_id`),
  CONSTRAINT `TRANSFER_ibfk_2` FOREIGN KEY (`club_from_id`) REFERENCES `CLUB` (`club_id`),
  CONSTRAINT `TRANSFER_ibfk_3` FOREIGN KEY (`club_to_id`) REFERENCES `CLUB` (`club_id`),
  CONSTRAINT `TRANSFER_ibfk_4` FOREIGN KEY (`agent_id`) REFERENCES `AGENT` (`agent_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TRANSFER`
--

LOCK TABLES `TRANSFER` WRITE;
/*!40000 ALTER TABLE `TRANSFER` DISABLE KEYS */;
INSERT INTO `TRANSFER` VALUES (1,3,9,2,50000000,3000000,'2020-07-15'),(4,6,7,1,0,0,'2020-09-25'),(7,10,1,3,63000000,6000000,'2019-06-30'),(8,6,1,8,29000000,1000000,'2019-07-01'),(11,9,5,11,29000000,2500000,'2020-09-19'),(13,6,4,13,2500000000,5000000,'2019-07-25'),(14,1,4,14,0,3000000,'2020-08-14'),(15,8,3,15,63000000,9500000,'2019-06-22'),(18,9,10,18,2920000000,5120000,'2019-07-01'),(19,1,6,19,160000000,19500000,'2019-07-01');
/*!40000 ALTER TABLE `TRANSFER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ZIP_MAP`
--

DROP TABLE IF EXISTS `ZIP_MAP`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ZIP_MAP` (
  `zip_code` varchar(256) NOT NULL,
  `city` varchar(256) NOT NULL,
  `country` varchar(256) NOT NULL,
  PRIMARY KEY (`zip_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ZIP_MAP`
--

LOCK TABLES `ZIP_MAP` WRITE;
/*!40000 ALTER TABLE `ZIP_MAP` DISABLE KEYS */;
INSERT INTO `ZIP_MAP` VALUES ('08028','Barcelona','Spain'),('28005','Madrid','Spain'),('28036','Madrid','Spain'),('44139','Dortmund','Germany'),('D-81547','Munich','Germany'),('L4 0TH','Liverpool','England'),('M11 3FF','Manchester','England'),('M16 0RA','Manchester','England'),('N5 1BU','London','England'),('SW6 1HS','London','England');
/*!40000 ALTER TABLE `ZIP_MAP` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-04 18:48:54
