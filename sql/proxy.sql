/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50724
 Source Host           : localhost:3306
 Source Schema         : proxy

 Target Server Type    : MySQL
 Target Server Version : 50724
 File Encoding         : 65001

 Date: 30/04/2019 18:23:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for proxy
-- ----------------------------
DROP TABLE IF EXISTS `proxy`;
CREATE TABLE `proxy`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` int(10) UNSIGNED NOT NULL,
  `port` int(11) NOT NULL,
  `type` int(11) NOT NULL,
  `protocol` int(11) NOT NULL,
  `country` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `area` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_valid` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `unique_protocol://ip:port`(`protocol`, `ip`, `port`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 802 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
