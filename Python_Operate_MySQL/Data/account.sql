/*
 Navicat Premium Data Transfer

 Source Server         : localhost_MYSQL
 Source Server Type    : MySQL
 Source Server Version : 80013
 Source Host           : localhost:3306
 Source Schema         : student

 Target Server Type    : MySQL
 Target Server Version : 80013
 File Encoding         : 65001

 Date: 06/01/2019 14:23:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account`  (
  `acctid` INT(11)  DEFAULT NULL COMMENT '帐户ID',
  `money`  INT(11)  DEFAULT NULL COMMENT '余额'
 
) ENGINE = InnoDB  DEFAULT CHARACTER SET = utf8;

-- 不能设置为MYISAM,因为MYISAM不支持事务，引擎设为InnoDB 
-- ----------------------------
-- Records of account
-- ----------------------------
INSERT INTO `account` VALUES (11, '110');
INSERT INTO `account` VALUES (12, '10');

SET FOREIGN_KEY_CHECKS = 1;
