# PHP虚拟环境

该项目是使用python开发的php虚拟环境


值得注意的是，会自动向虚拟环境注入单独的composer和pecl

如果你想添加更多的php环境，可用在Package目录下创建一个对应的版本号，放入二进制可执行文件，你需要将``php.ini``中的路径使用``{{$realpath}}``来替换



如果你喜欢这个项目就给个star

用法和conda大体一致
## 创建一个虚拟环境
``
baseyun create -n project -v 8.0.2
``

## 查看可用的php版本
``
baseyun show --do php
``

## 查看所有虚拟环境
``
baseyun show --do env
``

## 删除一个虚拟环境
``
baseyun remove -n project
``

## 激活虚拟环境
``
baseyun activate project
``

## 退出虚拟环境
``
baseyun deactivate project
``

Author:wlkjyy <wlkjyy@vip.qq.com|3139505131>
