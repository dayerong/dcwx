#### **dcwx -- 微信个人订阅号在日常运维方面的开发应用**

``` 
基于Python 2.7
```

- 如何搭建一个基础的微信公众号后台，可以自行搜索一下。我的是未通过认证的个人订阅号，接口权限很少。


- 截图如下：

```
关注订阅号后，如果没有授权，用户无法使用其功能。必须由管理员创建授权账户，然后通过此账户与密码进行“注册”。
```

![image](https://github.com/dayerong/dcwx/blob/master/screenshots/png-1.png?raw=true)

```
验证账户与密码无误，后台数据库会收集用户的openid，此后就无需再输入，账户被授权，可以开始使用功能。
```
![image](https://github.com/dayerong/dcwx/blob/master/screenshots/png-2.png?raw=true)
![image](https://github.com/dayerong/dcwx/blob/master/screenshots/png-3.png?raw=true)
![image](https://github.com/dayerong/dcwx/blob/master/screenshots/png-4.png?raw=true)
![image](https://github.com/dayerong/dcwx/blob/master/screenshots/png-5.png?raw=true)
![image](https://github.com/dayerong/dcwx/blob/master/screenshots/png-6.png?raw=true)
![image](https://github.com/dayerong/dcwx/blob/master/screenshots/png-7.png?raw=true)

```
普通用户无法使用管理员权限的功能指令，输入【admin】会提示非管理员。
```

![image](https://github.com/dayerong/dcwx/blob/master/screenshots/png-8.png?raw=true)
![image](https://github.com/dayerong/dcwx/blob/master/screenshots/png-12.png?raw=true)

```

管理员权限的用户可以使用更高权限的指令，比如重启服务等。

此处是由管理员创建新的账户，也就是授权普通用户可以使用。
```

![image](https://github.com/dayerong/dcwx/blob/master/screenshots/png-9.png?raw=true)
![image](https://github.com/dayerong/dcwx/blob/master/screenshots/png-10.png?raw=true)

```
发出指令，重启指定服务器的系统服务。
```

![image](https://github.com/dayerong/dcwx/blob/master/screenshots/png-11.png?raw=true)



- 还可以结合ansible开发一些自动化功能。


```
调用ansible服务器发出指令重启关闭系统。
```
![image](https://github.com/dayerong/dcwx/blob/master/screenshots/png-13.png?raw=true)

---
