# 群广告拦截插件
这里群聊拦截广告的插件,需要登录的QQ号,在群里是管理员
# pymysql库的安装
```
pip install pymysql
```
# 插件数据脚本
```
DROP TABLE IF EXISTS `chat_ads`;
CREATE TABLE `chat_ads` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `content` varchar(255) DEFAULT NULL COMMENT '聊天内容',
  `group_number` varchar(255) DEFAULT NULL,
  `group_name` varchar(255) DEFAULT NULL,
  `qq` varchar(255) DEFAULT NULL,
  `nickname` varchar(255) DEFAULT NULL,
  `mark` varchar(255) DEFAULT NULL,
  `keyword` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=1193 DEFAULT CHARSET=utf8 COMMENT='qq群广告记录表';


```
