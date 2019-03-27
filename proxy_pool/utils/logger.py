# coding=utf-8
import logging
import os

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(CURRENT_PATH, os.pardir + os.path.sep + os.pardir)
LOG_PATH = os.path.join(ROOT_PATH, 'log')

# db logger
# 创建名为"db"的记录器
db_logger = logging.getLogger("db")
db_logger.setLevel(logging.DEBUG)
# 创建级别为DEBUG的日志文件处理器
file_handler = logging.FileHandler(os.path.join(LOG_PATH, "db.log"))
file_handler.setLevel(logging.DEBUG)
# 创建级别为DEBUG的控制台日志处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
# 创建格式器，加到日志处理器中
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
# 将文件处理器和控制台处理器加入记录器
db_logger.addHandler(file_handler)
db_logger.addHandler(console_handler)

# proxy_getter logger
# 创建名为"proxy_getter_logger"的记录器
proxy_getter_logger = logging.getLogger("proxy_getter")
proxy_getter_logger.setLevel(logging.DEBUG)
# 创建级别为DEBUG的日志文件处理器
file_handler = logging.FileHandler(os.path.join(LOG_PATH, "proxy_getter.log"))
file_handler.setLevel(logging.DEBUG)
# 创建级别为DEBUG的控制台日志处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
# 创建格式器，加到日志处理器和控制台处理器中
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
# 将文件处理器和控制台处理器加入记录器
proxy_getter_logger.addHandler(file_handler)
proxy_getter_logger.addHandler(console_handler)

# proxy_check logger
# 创建名为"proxy_check_logger"的记录器
proxy_check_logger = logging.getLogger("proxy_check")
proxy_check_logger.setLevel(logging.DEBUG)
# 创建级别为DEBUG的日志文件处理器
file_handler = logging.FileHandler(os.path.join(LOG_PATH, "proxy_check.log"))
file_handler.setLevel(logging.DEBUG)
# 创建级别为DEBUG的控制台日志处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
# 创建格式器，加到日志处理器和控制台处理器中
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
# 将文件处理器和控制台处理器加入记录器
proxy_check_logger.addHandler(file_handler)
proxy_check_logger.addHandler(console_handler)
