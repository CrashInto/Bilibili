# Bilibili
以我的英雄学院为例，实现B站弹幕抓取，并进行存储
===========
## 了解网页结构
* 第一步：观察B站上这个番的地址，分成三个不同的类。分别对应第一季，第二季以及第三季。03    65      60        对应每一季的第一集尾部地址。
* 第二步：每一季对应的首部不一样。分别为：
    https://www.bilibili.com/bangumi/play/ep1156 | https://www.bilibili.com/bangumi/play/ep2058 | https://www.bilibili.com/bangumi/play/ep2001
>方法:Create_episode_url传入首部地址，集数，开始尾部地址，生成每一集对应的地址
* 第三步：请求每一集的地址，捕获构造每一集对应弹幕地址的部分内容cid
>通过方法：Parse_episode实现，还抓取了每一集的title
* 第四步：请求弹幕地址，抓取弹幕
>Get_danmu
* 第五步：抓取结果保存到数据库，保存的内容有集的titl和弹幕内容。
>Save_to_mongo
