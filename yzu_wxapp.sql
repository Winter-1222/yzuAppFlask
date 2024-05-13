/*
 Navicat Premium Data Transfer

 Source Server         : wangdong
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : yzu_wxapp

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 13/05/2024 22:43:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version`  (
  `version_num` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`version_num`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('7b5faa0bdb4e');

-- ----------------------------
-- Table structure for homework_progress
-- ----------------------------
DROP TABLE IF EXISTS `homework_progress`;
CREATE TABLE `homework_progress`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `homework_id` int NOT NULL COMMENT '作业ID',
  `department` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '部门',
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '姓名',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '内容',
  `created_at` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of homework_progress
-- ----------------------------
INSERT INTO `homework_progress` VALUES (1, 11, '计科2001', '王冬', '首次留下作业', '2024-05-12 17:51:11');
INSERT INTO `homework_progress` VALUES (2, 11, '计科2001', '王冬', '来办公室喝茶', '2024-05-12 21:15:29');
INSERT INTO `homework_progress` VALUES (3, 11, '计科2001', '王冬', '2117办公室', '2024-05-12 21:16:57');
INSERT INTO `homework_progress` VALUES (4, 11, '计科2001', '王冬', '测试', '2024-05-12 21:18:16');
INSERT INTO `homework_progress` VALUES (5, 11, '计科2001', '王冬', '测试123', '2024-05-12 21:18:41');
INSERT INTO `homework_progress` VALUES (6, 11, '计科2001', '王冬', '测试延迟', '2024-05-12 21:19:55');
INSERT INTO `homework_progress` VALUES (7, 9, '计科2001', '王冬', '首次留下作业', '2024-05-12 19:00:00');

-- ----------------------------
-- Table structure for suggestions
-- ----------------------------
DROP TABLE IF EXISTS `suggestions`;
CREATE TABLE `suggestions`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '学号',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '意见标题',
  `is_public` tinyint(1) NOT NULL COMMENT '是否公开',
  `contact` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '联系方式',
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '问题描述',
  `category_id` int NOT NULL COMMENT '分类ID',
  `created_at` datetime NOT NULL COMMENT '创建时间',
  `status` tinyint(1) NOT NULL COMMENT '作业状态',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of suggestions
-- ----------------------------
INSERT INTO `suggestions` VALUES (1, '1', '怎么入党？', 1, '110', '入党！', 1, '2024-05-11 13:32:44', 0);
INSERT INTO `suggestions` VALUES (2, '1', '11', 0, '11', '11', 1, '2024-05-11 13:39:04', 0);
INSERT INTO `suggestions` VALUES (3, '1', '11', 1, '`1', '1', 1, '2024-05-11 14:01:09', 0);
INSERT INTO `suggestions` VALUES (4, '1', '12', 0, '123', '123', 1, '2024-05-11 14:03:17', 0);
INSERT INTO `suggestions` VALUES (5, '1', '222', 0, '222', '222', 2, '2024-05-11 18:59:36', 0);
INSERT INTO `suggestions` VALUES (6, '1', '1213', 0, '2134', '124214', 1, '2024-05-11 18:59:49', 0);
INSERT INTO `suggestions` VALUES (7, '1', '123123', 0, '124124', '4214', 2, '2024-05-11 19:00:04', 0);
INSERT INTO `suggestions` VALUES (8, '202805122', '关于转正时间', 1, '13913791122', '预备党员转正。', 1, '2024-05-11 19:58:50', 0);
INSERT INTO `suggestions` VALUES (9, '202805122', '什么时候放暑假？', 1, '110', '123', 2, '2024-05-12 15:04:38', 0);
INSERT INTO `suggestions` VALUES (11, '202805122', '五一后的上课时间', 1, '110', '五一后下午第一节课是14:30吗？', 2, '2024-05-12 17:51:11', 0);

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '账号',
  `password` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '密码',
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '姓名',
  `role` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '角色',
  `department` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '部门',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, '202805122', 'yzu123', '王冬', 'admin', '计科2001');
INSERT INTO `users` VALUES (2, '1', '1', '1', '1', '智能2001');
INSERT INTO `users` VALUES (3, 'user', '1', '测试', 'stu', '计科2002');

SET FOREIGN_KEY_CHECKS = 1;
