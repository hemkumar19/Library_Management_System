-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 13, 2024 at 06:06 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `id` varchar(50) NOT NULL,
  `titale` varchar(100) NOT NULL,
  `edition` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `publish` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `page` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`id`, `titale`, `edition`, `author`, `publish`, `price`, `page`) VALUES
('1111', 'Java Complete Refrance ', 'Seventh Edition', 'Herbert Schildt', '2007', '599', '997'),
('1112', 'Object Oriented Programming with C++', 'Eighth Edition', 'E.Balagurusamy', '2020', '580', '675'),
('1113', 'Programming in C', 'Frist Edition', 'Kamal Prakashan', '2019', '250', '368'),
('1199', 'The Python Book', 'New Edition', 'Rob Mastrodomenico', '2022', '299', '272');

-- --------------------------------------------------------

--
-- Table structure for table `issue`
--

CREATE TABLE `issue` (
  `stdid` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `fathername` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `branch` varchar(100) NOT NULL,
  `year` varchar(100) NOT NULL,
  `semester` varchar(100) NOT NULL,
  `bookid` varchar(100) NOT NULL,
  `titale` varchar(100) NOT NULL,
  `edition` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `publish` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `page` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `issue`
--

INSERT INTO `issue` (`stdid`, `name`, `fathername`, `course`, `branch`, `year`, `semester`, `bookid`, `titale`, `edition`, `author`, `publish`, `price`, `page`, `date`) VALUES
('1212', 'Virendra', 'Mansingh', 'MBA', 'Management', 'Second Year', 'Third Semester', '1199', 'The Python Book', 'New Edition', 'Rob Mastrodomenico', '2022', '299', '272', '2024-04-13');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`) VALUES
('Admin', 'Admin@123'),
('Hitesh', 'Hitesh@123');

-- --------------------------------------------------------

--
-- Table structure for table `return`
--

CREATE TABLE `return` (
  `stdid` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `fathername` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `branch` varchar(100) NOT NULL,
  `year` varchar(100) NOT NULL,
  `semester` varchar(100) NOT NULL,
  `bookid` varchar(100) NOT NULL,
  `titale` varchar(100) NOT NULL,
  `edition` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `publish` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `page` varchar(100) NOT NULL,
  `rdate` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `return`
--

INSERT INTO `return` (`stdid`, `name`, `fathername`, `course`, `branch`, `year`, `semester`, `bookid`, `titale`, `edition`, `author`, `publish`, `price`, `page`, `rdate`) VALUES
('1212', 'Virendra', 'Mansingh', 'MBA', 'Management', 'Second Year', 'Third Semester', '1199', 'The Python Book', 'New Edition', 'Rob Mastrodomenico', '2022', '299', '272', '2024-01-01');

-- --------------------------------------------------------

--
-- Table structure for table `signup`
--

CREATE TABLE `signup` (
  `name` varchar(50) NOT NULL,
  `username` int(50) NOT NULL,
  `password` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `fathername` varchar(100) DEFAULT NULL,
  `course` varchar(50) DEFAULT NULL,
  `branch` varchar(50) DEFAULT NULL,
  `year` varchar(50) DEFAULT NULL,
  `semester` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `fathername`, `course`, `branch`, `year`, `semester`) VALUES
(1111, 'Hemkumar', 'Masram', 'MCA', 'Computer Applicatin', 'Second Year', 'Fourth Semester'),
(1112, 'Hitesh', 'Mulchand', 'MCA', 'Computer Applicatin', 'Second Year', 'Fourth Semester'),
(1113, 'Pushpendra', 'Dhaniram', 'MCA', 'Computer Applicatin', 'Second Year', 'Fourth Semester'),
(1114, 'Kanak', 'Laxman', 'MCA', 'Computer Applicatin', 'First Year', 'First Semester'),
(1212, 'Virendra', 'Mansingh', 'MBA', 'Management', 'Second Year', 'Third Semester');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=234236;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
