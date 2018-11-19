-- MySQL dump 10.13  Distrib 8.0.13, for macos10.14 (x86_64)
--
-- Host: localhost    Database: schedule
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `BATCHES`
--

DROP TABLE IF EXISTS `BATCHES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BATCHES` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATCHES`
--

LOCK TABLES `BATCHES` WRITE;
/*!40000 ALTER TABLE `BATCHES` DISABLE KEYS */;
INSERT INTO `BATCHES` VALUES (2,'БКЛ-153');
/*!40000 ALTER TABLE `BATCHES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BUILDINGS`
--

DROP TABLE IF EXISTS `BUILDINGS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BUILDINGS` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Address` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BUILDINGS`
--

LOCK TABLES `BUILDINGS` WRITE;
/*!40000 ALTER TABLE `BUILDINGS` DISABLE KEYS */;
INSERT INTO `BUILDINGS` VALUES (1,'Старая Басманная ул., д. 21/4');
/*!40000 ALTER TABLE `BUILDINGS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CLASSES`
--

DROP TABLE IF EXISTS `CLASSES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `CLASSES` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CLASSES`
--

LOCK TABLES `CLASSES` WRITE;
/*!40000 ALTER TABLE `CLASSES` DISABLE KEYS */;
INSERT INTO `CLASSES` VALUES (1,'Компьютерная лингвистика и информационные технологии'),(3,'Базы данных'),(4,'Программирование');
/*!40000 ALTER TABLE `CLASSES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CLASSROOMS`
--

DROP TABLE IF EXISTS `CLASSROOMS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `CLASSROOMS` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Number` int(11) DEFAULT NULL,
  `Address` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CLASSROOMS`
--

LOCK TABLES `CLASSROOMS` WRITE;
/*!40000 ALTER TABLE `CLASSROOMS` DISABLE KEYS */;
INSERT INTO `CLASSROOMS` VALUES (1,505,1),(3,503,1),(4,502,1),(5,321,1);
/*!40000 ALTER TABLE `CLASSROOMS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SCHEDULE`
--

DROP TABLE IF EXISTS `SCHEDULE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `SCHEDULE` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Date_Time` datetime DEFAULT NULL,
  `Teacher` text,
  `Batch` int(11) DEFAULT NULL,
  `Classroom` int(11) DEFAULT NULL,
  `Building` int(11) DEFAULT NULL,
  `Class` int(11) DEFAULT NULL,
  `Student` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SCHEDULE`
--

LOCK TABLES `SCHEDULE` WRITE;
/*!40000 ALTER TABLE `SCHEDULE` DISABLE KEYS */;
INSERT INTO `SCHEDULE` VALUES (6,'2018-11-19 14:10:00','Литвинов Денис Владимирович',2,505,1,4,2);
/*!40000 ALTER TABLE `SCHEDULE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STUDENTS`
--

DROP TABLE IF EXISTS `STUDENTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `STUDENTS` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` text,
  `Batch` int(11) DEFAULT NULL,
  `Email` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STUDENTS`
--

LOCK TABLES `STUDENTS` WRITE;
/*!40000 ALTER TABLE `STUDENTS` DISABLE KEYS */;
INSERT INTO `STUDENTS` VALUES (2,'Глазунов Евгений Владимирович',2,'glaz.dikobraz@gmail.com');
/*!40000 ALTER TABLE `STUDENTS` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-20  0:33:23
