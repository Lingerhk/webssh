#### WEB版ssh终端连接器

#### 1. 简介

采用tornado异步处理框架，基于websocket与前端进行数据传输。后端接入使用Nginx反向代理，后端连接使用python的paramiko第三方模块与远程SSH主机进行ssh连接。　　


#### 2. 安装

(1) 配置Nginx:  
    ```
    将/conf/nginx/webssh.conf放到nginx配置文件目录下，重启nginx
    ```

(2) 配置supervisor:  
    ```
    将/conf/supervisor/webssh.ini放到supervisor的配置文件目录下,重启并加载webssh
    ```

(3) 运行成功，可web访问。示例:  http://ssh.s0nnet.com/


#### 3. 配置

webssh的主配置文件在/src/webssh.conf中：
```
# webssh监听的端口，与nginx反向代理端口一致
port = 9520

# 日志配置设置
log_file_prefix = "./logs/webssh_sys.log"
logging = "info"
log_to_stderr = True
log_file_max_size = 2*1024*1024
log_file_num_backups = 7

# xcode配置,防止别人胡乱使用
xcode = "heheda"

# 邮件发送配置
smail = True
username = "test@sina.cn"
password = "test123"
smtpaddr = "smtp.sina.cn"
smtpport = 25
fromaddr = "test@sina.cn"
toaddrs = "s0nnet@sina.com"
```
