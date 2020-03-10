-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-03-2020 a las 19:27:02
-- Versión del servidor: 10.1.40-MariaDB
-- Versión de PHP: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `compuservi`
--
CREATE DATABASE IF NOT EXISTS `compuservi` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `compuservi`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `computadoras`
--

CREATE TABLE IF NOT EXISTS `computadoras` (
  `id_computadora` int(11) NOT NULL AUTO_INCREMENT,
  `dir_ip` text NOT NULL,
  `puerto` text NOT NULL,
  `Estado` text NOT NULL,
  `servicio` text NOT NULL,
  PRIMARY KEY (`id_computadora`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `computadoras`
--

INSERT INTO `computadoras` (`id_computadora`, `dir_ip`, `puerto`, `Estado`, `servicio`) VALUES
(35, '200.33.171.60', '1122/tcp', 'open', 'availant-mgr'),
(36, '200.33.171.86', '443/tcp', 'open', 'https'),
(37, '200.33.171.86', '445/tcp', 'open', 'microsoft-ds'),
(38, '200.33.171.86', '902/tcp', 'open', 'iss-realsecure'),
(39, '200.33.171.86', '2000/tcp', 'open', 'cisco-sccp'),
(40, '200.33.171.86', '5060/tcp', 'open', 'sip'),
(41, '200.33.171.54', '80/tcp', 'open', 'http'),
(42, '200.33.171.54', '113/tcp', 'closed', 'ident'),
(43, '200.33.171.54', '443/tcp', 'open', 'https'),
(44, '200.33.171.54', '5060/tcp', 'open', 'sip');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
