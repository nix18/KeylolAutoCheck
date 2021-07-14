# KeylolAutoCheck
其乐论坛（keylol.com）简易自动签到脚本

# 使用方法

   
   
          前提：
   
             python3.7及以上 
   
             pip或conda安装urllib，requests，bs4
             
             
          步骤：
         
            1、main.py中填写cookie_str（通过浏览器登录keylol.com, F12 Network标签下获取），
               user_page（keylol个人信息页面，如https://keylol.com/suid-123456 ），
               plus_key（[www.pushplus.plus](http://www.pushplus.plus/) 的token）
      
            2、python main.py
            
            3、可通过crontab或云函数定时执行
            
            
# Licence

[Apache Licence](https://github.com/nix18/KeylolAutoCheck/raw/master/LICENSE)


# 作者博客

[Moecola.com](https://moecola.com)
