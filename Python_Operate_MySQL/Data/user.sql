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
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`userid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'name1');
INSERT INTO `user` VALUES (2, 'name2');
INSERT INTO `user` VALUES (3, 'name3');
INSERT INTO `user` VALUES (4, 'name4');
INSERT INTO `user` VALUES (5, 'name5');
INSERT INTO `user` VALUES (6, 'name6');
INSERT INTO `user` VALUES (7, 'name7');
INSERT INTO `user` VALUES (8, 'name8');
INSERT INTO `user` VALUES (9, 'name9');
SET FOREIGN_KEY_CHECKS = 1;
