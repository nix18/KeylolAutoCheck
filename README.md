# KeylolAutoCheck
其乐论坛（keylol.com）简易自动签到脚本

# 使用方法

  ***本地部署*** 
   
          前提：
   
             python3.7及以上 
   
             pip或conda安装urllib，requests，bs4
             
             
          步骤：
         
            1、main.py中填写cookie_str（通过浏览器登录keylol.com, F12 Network标签下获取），
               user_page（keylol个人信息页面，如https://keylol.com/suid-123456 ），
               plus_key（http://www.pushplus.plus/ 的token）
      
            2、python main.py
            
            3、可通过crontab或云函数定时执行
            
  ***腾讯云函数部署***
          
          1、创建腾讯云函数
          
          2、自定义创建
          
          3、本地上传zip包(https://github.com/nix18/KeylolAutoCheck/releases/download/V1.0/KeylolAutoCheck.V1.0.zip)
          
          4、index.py中填写cookie_str（通过浏览器登录keylol.com, F12 Network标签下获取），
             user_page（keylol个人信息页面，如https://keylol.com/suid-123456 ），
             plus_key（http://www.pushplus.plus/ 的token），部署
               
          5、触发管理->创建定时触发器->自定义触发周期（Cron表达式: 0 0 5 * * * *）->测试完成
            
# Licence

[Apache Licence](https://github.com/nix18/KeylolAutoCheck/raw/master/LICENSE)


# 作者博客

[Moecola.com](https://moecola.com)
