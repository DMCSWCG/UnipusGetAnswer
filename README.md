# U_Learn_Answers_Get
自动获取U校园日常作业答案



heaers 中需要填入自己的请求头 



在登陆U校园进入课程界面后按下F12 进入开发者工具选择网络选项 然后刷新界面



随便选择一个选项点击 在旁边出现的小窗中选择消息头找到 User-Agent 和 X-ANNOTATOR-AUTH-TOKEN 这两项全部复制 包括分号后的
放入headers


例如



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/74.0',
    'X-ANNOTATOR-AUTH-TOKEN':'WxzZSwiZXhwIjoxNThlOWM1MCIsImF1ZCI6ImVkeC51bmlwdXMuY24ifQ'
}




注意:前后的字符串需要打单引号



运行，并输入你想要获取答案的Url


仅测试了英语答案的获取，其他的答案获取暂未尝试
