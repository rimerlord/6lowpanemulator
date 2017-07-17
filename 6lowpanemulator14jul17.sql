-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 14, 2017 at 03:29 PM
-- Server version: 5.5.55-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `6lowpanemulator`
--
CREATE DATABASE IF NOT EXISTS `6lowpanemulator` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `6lowpanemulator`;

-- --------------------------------------------------------

--
-- Table structure for table `register`
--
-- Creation: Jul 13, 2017 at 10:19 AM
--

DROP TABLE IF EXISTS `register`;
CREATE TABLE IF NOT EXISTS `register` (
  `euid` int(7) NOT NULL AUTO_INCREMENT,
  `info` text NOT NULL,
  `cli_name` text NOT NULL,
  `idle` int(11) DEFAULT '0',
  `sequence` int(11) NOT NULL,
  `address` int(11) NOT NULL,
  PRIMARY KEY (`euid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`euid`, `info`, `cli_name`, `idle`, `sequence`, `address`) VALUES
(2, 'rfd1', 'rfd1', 0, 241, 5001),
(3, 'rfd3', 'rfd3', 0, 93, 5003);

-- --------------------------------------------------------

--
-- Table structure for table `rfd`
--
-- Creation: Jul 13, 2017 at 09:30 AM
--

DROP TABLE IF EXISTS `rfd`;
CREATE TABLE IF NOT EXISTS `rfd` (
  `sno` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `info` text NOT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `rfd`
--

INSERT INTO `rfd` (`sno`, `name`, `info`) VALUES
(1, 'rfd1', 'rfd1'),
(2, 'rfd2', 'rfd2'),
(3, 'rfd3', 'rfd3');

-- --------------------------------------------------------

--
-- Table structure for table `trust_auth`
--
-- Creation: Jul 13, 2017 at 09:38 AM
--

DROP TABLE IF EXISTS `trust_auth`;
CREATE TABLE IF NOT EXISTS `trust_auth` (
  `sno` int(11) NOT NULL AUTO_INCREMENT,
  `client_name` text NOT NULL,
  `val_inval` text NOT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `trust_auth`
--

INSERT INTO `trust_auth` (`sno`, `client_name`, `val_inval`) VALUES
(1, 'rfd1', 'is valid'),
(2, 'rfd2', 'is invalid'),
(3, 'rfd3', 'is valid');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
