# _*_ coding: utf-8 _*_

#调试模式是否开启
DEBUG = True
#数据库追踪模式关闭
SQLALCHEMY_TRACK_MODIFICATIONS = False

#mysql数据库连接信息,这里改为自己的账号
SQLALCHEMY_DATABASE_URI = "mysql://root:password@localhost:3306/happyballtest"
