# 这是一款聊天内容记录插件,只负责记录聊天内容.
需要用到mysql数据库
# pymysql库的安装
```
pip install pymysql
```
# 插件数据脚本
```sql
CREATE TABLE `chat_logs` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `content` varchar(255) DEFAULT NULL COMMENT '聊天内容',
  `group_number` varchar(255) DEFAULT NULL,
  `group_name` varchar(255) DEFAULT NULL,
  `qq` varchar(255) DEFAULT NULL,
  `nickname` varchar(255) DEFAULT NULL,
  `mark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5093 DEFAULT CHARSET=utf8 COMMENT='聊天记录表';
```

# 修改对应的数据库配置
```
    # 连接数据库  
    connect = pymysql.Connect(  
        host='localhost',  
        port=3306,  
        user='root',  
        passwd='root',  
        db='it_work_db',  
        charset='utf8'  
    ) 
```