# 3D重建项目-计设前端界面

[![simpleui](https://img.shields.io/badge/developing%20with-Simpleui-2077ff.svg)](https://github.com/newpanjing/simpleui)
[![django](https://img.shields.io/badge/developing%20with-Django-276fe1)](https://github.com/django/django)
[![python](https://img.shields.io/badge/python-%3E=3.7.x-green.svg)](https://www.python.org/)
[![CSDN](https://img.shields.io/badge/CSDN-%E5%92%B8%E9%B1%BC%E5%92%B8-66ccff)](https://blog.csdn.net/qq_43724306)

## 依赖库安装：

```
pip3 install django-tinymce simpleui 
pip3 install django==2.2
```

## 修改配置项：

修改 `./Reconstruction3D/settings.py` 文件中 `ALLOWED_HOSTS` 的内容

`ALLOWED_HOSTS = ['*']` 时，为全部放行

## 测试用账号：

| 学号 | 用户名  | 密码  | 等级     |
| ---- | ------- | ----- | -------- |
| 0    | admin   | admin | 管理员   |
| 2    | test111 | 123   | 普通用户 |

## 更新日志：

### Version 1.0 preview

1. 完成了大部分页面的基本制作

### Version 2.0 stable

1. 因为index页面资源文件、路径无法加载等原因，弃用原index.html文件，重新绘制
2. 补齐第二展区
3. 补齐外链

### Version2.1 hotfix

1. 暂时解决了网站掉线的问题
2. 解决了icon未加载问题
3. 通过更换cdn加快了各页面的加载速度
4. 优化了标签头显示内容

### Version2.2 stable

1. 加入了论坛系统
2. 加入了登录系统
3. 修改了footer样式
4. TODO：更换图片

### Version2.21 hotfix

1. 添加了评论框
2. 更改了标题
3. 更改了首页图片

### Version3.11 stable

1. 网页整体结构调整：flask->django
2. 增加后台数据库

### Version3.2 Preview

1. 增加了登录逻辑
2. 基本理清Django框架思路

### Version3.3 Preview

1. [ ] 用户逻辑基本实现闭环，网站动态化进度50%
2. [ ] 上线了未完成的后台系统
3. [ ] 更改了登录界面

### Version3.4 Preview

1. 用户评论库完成，还剩前端上传
2. 后端修改

### Version3.5 Preview

1. 完成了评论逻辑

### Version3.6 Preview

1. 完善了注册和登录逻辑

### Version3.7 Stable

1. 完善了点赞逻辑
2. 完善了前端界面
3. 完善了后端修改

### Version3.8 HotFix

1. 更改了数据库内容
2. 修正了登录跳转逻辑
3. 修正了时区问题

### Version3.81 HotFix

1. 更改了登录界面的背景
2. 评论id自增

### Version3.82 HotFix

1. 增加了内嵌网页
2. 微调了部分样式

### Version3.83 HotFix

1. 增加了详情页的导航
2. 增加了返回首页按钮
3. 增加了文章间跳转按钮

![3.83修改1](https://pic.imgdb.cn/item/60a210a26ae4f77d35793cba.jpg)

![3.83修改2](https://pic.imgdb.cn/item/60a211ad6ae4f77d35844008.jpg)

![3.83修改3](https://pic.imgdb.cn/item/60a21a296ae4f77d35d958dc.jpg)

### Version3.9 Stable

1. 完成了用户修改个人信息页面
2. 增加了首页用户头像
3. 增加了用户所在学院
4. 增加了后台页的icon

![](https://pic.imgdb.cn/item/60a2898d6ae4f77d35dce6eb.jpg)

![](https://pic.imgdb.cn/item/60a29a2a6ae4f77d35d16a9c.jpg)

![](https://pic.imgdb.cn/item/60a289e16ae4f77d35e1f6ba.jpg)

![](https://pic.imgdb.cn/item/60a28ba56ae4f77d35fdf9b2.jpg)

### Version 4.0 Stable

1. (用户)评论管理删除与恢复
2. 登录逻辑修改-登录后必须完善个人信息
3. 个人信息修改bug修复-name问题
4. 将导航栏进行了整理
5. 修改了BBS评论的布局，美化了点赞样式
6. BBS划分为热评和时评
7. 修复管理后台-普通用户未鉴权问题

![](https://pic.imgdb.cn/item/60a3d1666ae4f77d35401a3f.jpg)

![](https://pic.imgdb.cn/item/60a3d2906ae4f77d3550e631.jpg)

![](https://pic.imgdb.cn/item/60a3d2bd6ae4f77d355368e2.jpg)

![](https://pic.imgdb.cn/item/60a3d3016ae4f77d35574b01.jpg)

### Version 4.1 Stable

1. 前端静态页面大修，调整了文案和页面分布，调整了宽度不一致问题
2. 增加了文件下载，调整了模型链接
3. 调整了文章页面sidebar的对齐样式
4. 解决了用户管理的表头问题
5. 解决了页面底部按钮在移动端显示不正常问题
6. 修改了管理员界面后台头像显示问题
7. 调整了注册逻辑：只能用学号注册，注册后初始用户名为 `用户+学号`

![](https://pic.imgdb.cn/item/60a530486ae4f77d3570231b.jpg)

![](https://pic.imgdb.cn/item/60a5d15b6ae4f77d35865c13.jpg)

![](https://pic.imgdb.cn/item/60a5d1826ae4f77d35879f5a.jpg)

### Version 4.1 Stable

1. 冗余代码删除
2. 整理css、js多余调用
3. 修复了修改个人信息中无密码漏洞
4. 优化了管理员404时右上角显示
5. 增加了修改个人信息页面的头像预览
6. 修改了导航栏配色
7. 修复了注册时错学号无法反馈的bug
8. 更改了后台主题，调整了输入框大小

![](https://pic.imgdb.cn/item/60a684e46ae4f77d35213e95.jpg)

![](https://pic.imgdb.cn/item/60a685296ae4f77d35244c5a.jpg)

![](https://pic.imgdb.cn/item/60a7280c6ae4f77d359503ca.jpg)

![](https://pic.imgdb.cn/item/60a75e6f6ae4f77d353ddbb3.jpg)
