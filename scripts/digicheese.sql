-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 29 juil. 2025 à 17:47
-- Version du serveur : 11.5.2-MariaDB
-- Version de PHP : 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `digicheese`
--
CREATE DATABASE IF NOT EXISTS `digicheese` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `digicheese`;

-- --------------------------------------------------------

--
-- Structure de la table `d_client`
--

DROP TABLE IF EXISTS `d_client`;
CREATE TABLE IF NOT EXISTS `d_client` (
  `c_genre` varchar(8) DEFAULT NULL,
  `c_nom` varchar(40) NOT NULL,
  `c_prenom` varchar(30) NOT NULL,
  `c_adresse_1` varchar(50) DEFAULT NULL,
  `c_adresse_2` varchar(50) DEFAULT NULL,
  `c_adresse_3` varchar(50) DEFAULT NULL,
  `c_telephone` varchar(13) DEFAULT NULL,
  `c_email` varchar(255) DEFAULT NULL,
  `c_portable` varchar(13) DEFAULT NULL,
  `c_newsletter` int(11) DEFAULT NULL,
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_fk_ville_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`c_id`),
  KEY `c_fk_ville_id` (`c_fk_ville_id`),
  KEY `ix_d_client_c_nom` (`c_nom`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `d_commande`
--

DROP TABLE IF EXISTS `d_commande`;
CREATE TABLE IF NOT EXISTS `d_commande` (
  `c_date_commande` datetime DEFAULT NULL,
  `c_timbre_client` float DEFAULT NULL,
  `c_timbre_commande` float DEFAULT NULL,
  `c_nombre_colis` int(11) NOT NULL,
  `c_cheque_client` float DEFAULT NULL,
  `c_commentaire` varchar(255) DEFAULT NULL,
  `c_barchive` int(11) NOT NULL,
  `c_bstock` int(11) NOT NULL,
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`c_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `d_commune`
--

DROP TABLE IF EXISTS `d_commune`;
CREATE TABLE IF NOT EXISTS `d_commune` (
  `c_ville` varchar(50) DEFAULT NULL,
  `c_code_postal` varchar(5) DEFAULT NULL,
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_fk_departement_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`c_id`),
  KEY `c_fk_departement_id` (`c_fk_departement_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `d_conditionnement`
--

DROP TABLE IF EXISTS `d_conditionnement`;
CREATE TABLE IF NOT EXISTS `d_conditionnement` (
  `c_libelle` varchar(50) DEFAULT NULL,
  `c_poids` int(11) DEFAULT NULL,
  `c_prix` decimal(10,0) NOT NULL,
  `c_ordre_impression` int(11) DEFAULT NULL,
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`c_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `d_departement`
--

DROP TABLE IF EXISTS `d_departement`;
CREATE TABLE IF NOT EXISTS `d_departement` (
  `code_departement` varchar(3) NOT NULL,
  `nom_departement` varchar(50) DEFAULT NULL,
  `d_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`d_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `d_objet`
--

DROP TABLE IF EXISTS `d_objet`;
CREATE TABLE IF NOT EXISTS `d_objet` (
  `o_libelle` varchar(50) DEFAULT NULL,
  `o_taille` varchar(50) DEFAULT NULL,
  `o_prix_unitaire` decimal(10,0) NOT NULL,
  `o_poids` decimal(10,0) NOT NULL,
  `o_indisponible` int(11) NOT NULL,
  `o_ordre_impression` int(11) NOT NULL,
  `o_odre_affichage` int(11) NOT NULL,
  `o_carte_pub` int(11) NOT NULL,
  `o_points` int(11) NOT NULL,
  `o_ordre_affichage` int(11) NOT NULL,
  `o_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`o_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `d_role`
--

DROP TABLE IF EXISTS `d_role`;
CREATE TABLE IF NOT EXISTS `d_role` (
  `r_nom` varchar(25) DEFAULT NULL,
  `r_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`r_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `d_utilisateur`
--

DROP TABLE IF EXISTS `d_utilisateur`;
CREATE TABLE IF NOT EXISTS `d_utilisateur` (
  `u_nom` varchar(50) DEFAULT NULL,
  `u_prenom` varchar(50) DEFAULT NULL,
  `u_username` varchar(50) DEFAULT NULL,
  `u_date_inscription` date DEFAULT NULL,
  `u_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`u_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `d_utilisateur_role`
--

DROP TABLE IF EXISTS `d_utilisateur_role`;
CREATE TABLE IF NOT EXISTS `d_utilisateur_role` (
  `r_utilisateur_id` int(11) NOT NULL,
  `r_role_id` int(11) NOT NULL,
  PRIMARY KEY (`r_utilisateur_id`,`r_role_id`),
  KEY `r_role_id` (`r_role_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
