# sysu-gymbook-simulator Version-2.0
优化很多，配置完成后运行代码即可，可多人使用
---
# ***<font color=yellow>免责声明！</font>比较简陋，仅供<font color=yellow>学习</font>使用！***
---
# 前端

## 1.环境配置 （windows）
- nvm安装，方便控制node环境: https://github.com/nvm-sh/nvm
- 使用nvm管理node版本,自己查一下安装16.18.1:https://titangene.github.io/article/nvm.html (nvm install v16.18.1)
- 检查一下node和npm的版本 node -v， npm -v
- 我的npm version: 9.6.2，但这个应该不影响，node版本一致就行
- 然后运行 npm install，安装相应的package，只要不影响运行，有一点错误应该没问题，传package太慢了，手动安一下吧。
  
## 2.前端启动运行
- npm run serve （运行成功应该会有网址显示）
---
# 后端
- 运行run.py文件，缺什么包就pip install一下，没有什么复杂的配置，应该很少受到python 版本的影响，如果实在不行，换个高一点的python版本。
- 运行成功会有网址显示
- 把vue.config.js里面的target对应的网址换成后端的网址
---
# 转发到手机端访问
- Ngrok: https://dashboard.ngrok.com/get-started/setup/windows
- 下载一个，按照网站的教程，把前端的网址转发即可

# 使用说明
- 例子：
- ![](https://github.com/Yuanky123/SYSU-gymbook-simulator/blob/main/472835aeabb244e41fc7aae634ee2e0a.gif)
- 使用的时候把前后端以及转发都开启
- 输入名字，密码，学号，第一次使用需要先点注册，再点击登录
- 后面再使用直接点登录就好了
- 没有自动更改日期，最好随用随开，用完就关
---
# 可能的问题
- 1.如果npm install的时候出错，比较难搞，要查查配下环境
- 2.转发后的网址需要手机断掉校园网才能正常访问
- 3.再次声明，仅供学习，谨慎使用
- 4.感觉功能挺全了，应该不会再更新了

# 感谢
- 参考：https://github.com/cihat/twitter-clone
- Co-author: https://github.com/linhh29
