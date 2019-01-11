

```python
content = "returnInfo=true&composeId=1537858918284&content=%E8%BF%99%E6%98%AF%E4%B8%80%E4%B8%AA%E5%8F%91%E5%BE%80%E6%96%B0%E6%B5%AA%E9%82%AE%E7%AE%B1%E7%9A%84%E6%B5%8B%E8%AF%95%E9%82%AE%E4%BB%B6%EF%BC%8C%E5%B8%A6%E9%99%84%E4%BB%B6%E3%80%82%0D%0A%E5%90%B4%E6%89%BF%E8%8D%A3&isHtml=false&priority=3&saveSentCopy=true&requestReadReceipt=false&uploadMode=normal&lettercontent=&supportAutoNormal2Trs=false&isSchedule=false&isSource=false&sendMailWithSms=false&sendMailWithSmsMode=&smimeEncrypt=false&smimeSign=false&showOneRcpt=false&autosaveHitCounter=false&account=cwu+%3Ccwu@fudan.edu.cn%3E&to=%2213601927008%22%3C13601927008@sina.cn%3E%2C&smsAddrs=&cc=&bcc=&subject=Test+mail+1&attachment=1&attachment_1_type=upload&attachment_1_displayName=%E5%8F%82%E8%80%83%E7%BD%91%E7%AB%99%E5%88%97%E8%A1%A8.pdf&attachment_1_deleted=false&attachment_1_size=60365&localAttach1=&btnAddAttach=0&btnCreateImg=0&signSet=-1&chkSaveToSent=on&year=2018&month=9&day=26&hour=15&compinfo_minute=1"
```


```python
contentList = content.split('&')
```


```python
import urllib.parse
for item in contentList:
    it = item.split('=')
    data = urllib.parse.unquote(it[1])
    print(it[0],":",data)
```

    returnInfo : true
    composeId : 1537858918284
    content : 这是一个发往新浪邮箱的测试邮件，带附件。
    吴承荣
    isHtml : false
    priority : 3
    saveSentCopy : true
    requestReadReceipt : false
    uploadMode : normal
    lettercontent : 
    supportAutoNormal2Trs : false
    isSchedule : false
    isSource : false
    sendMailWithSms : false
    sendMailWithSmsMode : 
    smimeEncrypt : false
    smimeSign : false
    showOneRcpt : false
    autosaveHitCounter : false
    account : cwu+<cwu@fudan.edu.cn>
    to : "13601927008"<13601927008@sina.cn>,
    smsAddrs : 
    cc : 
    bcc : 
    subject : Test+mail+1
    attachment : 1
    attachment_1_type : upload
    attachment_1_displayName : 参考网站列表.pdf
    attachment_1_deleted : false
    attachment_1_size : 60365
    localAttach1 : 
    btnAddAttach : 0
    btnCreateImg : 0
    signSet : -1
    chkSaveToSent : on
    year : 2018
    month : 9
    day : 26
    hour : 15
    compinfo_minute : 1



```python
def newdate(year, month, date, hour, minute, second):
    result = str(year) + str(date) + str(hour) + str(minute) + str(second)
    return result
```


```python
mailContent = [{
'addT':'"WU Chengrong" <13601927008@sina.cn>',
'add':'WU Chengrong',
'icon':{
'm_icon':'UNREAD',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgkTBFKpyHeThQABsP',
'fid':1,
'size':27957,
'from':'"WU Chengrong" <13601927008@sina.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'课程测试邮件',
'sentDate':newdate(2018,8,25,14,59,12),
'receivedDate':newdate(2018,8,25,15,1,57),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'attached':'true'},
'hmid':'<000301d4549d$4f09d4b0$ed1d7e10$@sina.cn>'}},
{
'addT':'"科学出版社李海" <663241303@qq.com>',
'add':'科学出版社李海',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYTBFKp0sKMFwAAsg',
'fid':1,
'size':17090,
'from':'"科学出版社李海" <663241303@qq.com>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'科学出版社—专著出版',
'sentDate':newdate(2018,8,25,11,2,56),
'receivedDate':newdate(2018,8,25,11,3,58),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<tencent_4E9B0A069B37090F0701AB3D34E27B06A906@qq.com>'}},
{
'addT':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'add':'cs_keyan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQITB1Kp0sKK4gAAmU',
'fid':1,
'size':50994,
'from':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'to':'"谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud>',
'subject':'Fw: 关于举办“上海科创中心建设”报告的通知',
'sentDate':newdate(2018,8,25,10,59,43),
'receivedDate':newdate(2018,8,25,10,59,47),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<201809251059434977752@fudan.edu.cn>'}},
{
'addT':'"wmfu" <wmfu@fudan.edu.cn>',
'add':'wmfu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggTCFKpyHde4QAAmq',
'fid':1,
'size':4199,
'from':'"wmfu" <wmfu@fudan.edu.cn>',
'to':'cremiy@163.com',
'subject':'Re: Fw:推免生咨询',
'sentDate':newdate(2018,8,25,10,33,1),
'receivedDate':newdate(2018,8,25,10,33,7),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<7cce93fa.4b91c.1660e929e8f.Coremail.wmfu@fudan.edu.cn>',
'ref':'<6fc541c5.48107.16603dc6774.Coremail.cwu@fudan.edu.cn>'}},
{
'addT':'"Andrew fu" <zgbzlm@yeah.net>',
'add':'Andrew fu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcTBFKp0sJ5QQAAsC',
'fid':1,
'size':608664,
'from':'"Andrew fu" <zgbzlm@yeah.net>',
'to':'cwu@fudan.edu.cn',
'subject':'RE：工信中心邀请函',
'sentDate':newdate(2018,8,25,9,54,18),
'receivedDate':newdate(2018,8,25,9,54,22),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<4c3f8146.6ae.1660e6f2ac4.Coremail.zgbzlm@yeah.net>'}},
{
'addT':'"余莉萍" <17210240022@fudan.edu.cn>',
'add':'余莉萍',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgSBFKp0sI6eAAAs2',
'fid':1,
'size':2717,
'from':'"余莉萍" <17210240022@fudan.edu.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'来自《信息安全导论》助教',
'sentDate':newdate(2018,8,24,22,38,12),
'receivedDate':newdate(2018,8,24,22,38,18),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<8b6cb79.4a66e.1660c042ec8.Coremail.17210240022@fudan.edu.cn>'}},
{
'addT':'"沈建蓉" <jrshen@fudan.edu.cn>',
'add':'沈建蓉',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcSD1Kp0sI5iQAAmA',
'fid':1,
'size':522366,
'from':'"沈建蓉" <jrshen@fudan.edu.cn>',
'to':'"weihui" <weihui@fudan.edu.cn>, "cwu" <cwu@fudan.edu.cn>, "jwu" <jwu@fudan.edu.cn>, "wuyijian" <wuyijian@fudan.edu.cn>, "yhwu" <yhwu@fudan.edu.cn>, "xxiaochun" <xxiaochun@fudan.edu.cn>, "shawyh" <shawyh@fudan.edu.cn>, "xiezp" <xiezp@fudan.edu.cn>, "yunx" <yunx@fudan.edu.cn>, "xuyx" <xuyx@fudan.edu.cn>, "xyxue"',
'subject':'本学期学位申请程序',
'sentDate':newdate(2018,8,24,22,34,3),
'receivedDate':newdate(2018,8,24,22,34,9),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<201809242233035672455@fudan.edu.cn>'}},
{
'addT':'"17307130324" <17307130324@fudan.edu.cn>',
'add':'17307130324',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYSBFKp0sHonAAAsN',
'fid':1,
'size':5372,
'from':'"17307130324" <17307130324@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'关于信息安全导论的教学ppt',
'sentDate':newdate(2018,8,24,9,59,48),
'receivedDate':newdate(2018,8,24,9,59,50),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<3C966A30-4D51-4F43-9A26-70ABB98F363C@fudan.edu.cn>'}},
{
'addT':'"余莉萍" <17210240022@fudan.edu.cn>',
'add':'余莉萍',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgESBFKpyHbC4gAAsw',
'fid':1,
'size':1636,
'from':'"余莉萍" <17210240022@fudan.edu.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'祝老师中秋节快乐~',
'sentDate':newdate(2018,8,24,9,54,20),
'receivedDate':newdate(2018,8,24,9,54,23),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<7014a586.4959b.1660948d755.Coremail.17210240022@fudan.edu.cn>'}},
{
'addT':'"余莉萍" <lipingyuu@163.com>',
'add':'余莉萍',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgERBFKpyHaizQAAm8',
'fid':1,
'size':5553,
'from':'"余莉萍" <lipingyuu@163.com>',
'to':'"13307130375" <13307130375@fudan.edu.cn>, "13307130390" <13307130390@fudan.edu.cn>, "14307130308" <14307130308@fudan.edu.cn>, "16307110240" <16307110240@fudan.edu.cn>, "16307110300" <16307110300@fudan.edu.cn>, "16307110315" <16307110315@fudan.edu.cn>, "16307110511" <16307110511@fudan.edu.cn>, "16307130213"',
'subject':'来自《信息安全导论》TA',
'sentDate':newdate(2018,8,23,22,25,32),
'receivedDate':newdate(2018,8,23,22,25,36),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true'},
'hmid':'<3bf0c26b.7d3f.16606d239c3.Coremail.lipingyuu@163.com>'}},
{
'addT':'"lkjh lkjh" <lkjhlkjh1919@gmail.com>',
'add':'lkjh lkjh',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgIQBFKpyHZScgAAsx',
'fid':1,
'size':13826456,
'from':'"lkjh lkjh" <lkjhlkjh1919@gmail.com>',
'to':'',
'subject':'Fwd: 主题：2018年9月21日星期五 ……【周末快乐！】',
'sentDate':newdate(2018,8,23,0,12,11),
'receivedDate':newdate(2018,8,23,1,18,48),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<CAOm1Td0dH-ZsczFTgw2vbXY3wMTfqC5Atzf6i3KHzBumOWHy-w@mail.gmail.com>',
'ref':'<34e15060.b26e0a.16601b47811.Coremail.mnb201010@163.com>'}},
{
'addT':'"szhang" <szhang@fudan.edu.cn>',
'add':'szhang',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcQDlKp0sFPpwAAmY',
'fid':1,
'size':13883,
'from':'"szhang" <szhang@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>, "严明" <myan@fudan.edu.cn>, "曾剑平" <zjp@fudan.edu.cn>',
'subject':'Fw: 张世永教授，邀请您参加2018年第七届全国网络与信息安全防护峰会',
'sentDate':newdate(2018,8,22,16,21,20),
'receivedDate':newdate(2018,8,22,16,21,23),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true'},
'hmid':'<64339db4.1573b.166005e6d16.Coremail.szhang@fudan.edu.cn>'}},
{
'addT':'"ResearchGate" <no-reply@researchgatemail.net>',
'add':'ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgcQBFKpyHYkEgAAsi',
'fid':1,
'size':26404,
'from':'"ResearchGate" <no-reply@researchgatemail.net>',
'to':'"Chengrong Wu" <cwu@fudan.edu.cn>',
'subject':'Chengrong, we think you may have missed a citation of your research',
'sentDate':newdate(2018,8,22,14,59,8),
'receivedDate':newdate(2018,8,22,15,6,34),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<20180922065908.84EF48093@mr109.researchgate.net>'}},
{
'addT':'"上海大学计算机学院推免生" <cremiy@163.com>',
'add':'上海大学计算机学院推免生',
'icon':{
'm_icon':'FORWARDED',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgcQBFKpyHYM9wAAsv',
'fid':1,
'size':6806,
'from':'"上海大学计算机学院推免生" <cremiy@163.com>',
'to':'cwu@fudan.edu.cn',
'subject':'推免生咨询',
'sentDate':newdate(2018,8,22,10,58,3),
'receivedDate':newdate(2018,8,22,10,58,4),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'forwarded':'true'},
'hmid':'<50bce9ac.42ad.165ff3672c9.Coremail.cremiy@163.com>'}},
{
'addT':'"Springer" <springer@newsletter.springer.com>',
'add':'Springer',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgUPBFKpyHX0sgACsO',
'fid':1,
'size':59204,
'from':'"Springer" <springer@newsletter.springer.com>',
'to':'cwu@fudan.edu.cn',
'subject':'分享您的数据经验，有机会赢得1000元礼品卡',
'sentDate':newdate(2018,8,22,9,20,28),
'receivedDate':newdate(2018,8,22,9,27,7),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<01020165fedd1d4e-9b09c23e-5fe7-44ba-9b36-322f06712b2e-000000@eu-west-1.amazonses.com>'}},
{
'addT':'"ResearchGate" <no-reply@researchgatemail.net>',
'add':'ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggPBFKpyHW1jAAAs+',
'fid':1,
'size':21062,
'from':'"ResearchGate" <no-reply@researchgatemail.net>',
'to':'cwu@fudan.edu.cn',
'subject':'Adnen El Amraoui uploaded a full-text citing you',
'sentDate':newdate(2018,8,21,21,11,1),
'receivedDate':newdate(2018,8,21,21,16,29),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<20180921131101.7531E1000801C@mr98.researchgate.net>'}},
{
'addT':'"CCF会员部" <ccfmk@membership.ccf.org.cn>',
'add':'CCF会员部',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgPBFKp0sDWTQAAsw',
'fid':1,
'size':279844,
'from':'"CCF会员部" <ccfmk@membership.ccf.org.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'CCF近期活动推送（第3期）',
'sentDate':newdate(2018,8,21,19,44,34),
'receivedDate':newdate(2018,8,21,20,45,2),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'inlineAttached':'true'},
'hmid':'<00fe158b3672$1adec0da$dd873e50$@jhhygheev>'}},
{
'addT':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'add':'cs_keyan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgPB1Kp0sCbvgAAmN',
'fid':1,
'size':49493,
'from':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'to':'"谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud>',
'subject':'Fw: Fw: 科学卫星的发展及国际化应用研讨会（10.22日下午）',
'sentDate':newdate(2018,8,21,15,15,7),
'receivedDate':newdate(2018,8,21,15,15,4),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<201809211515073291739@fudan.edu.cn>'}},
{
'addT':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'add':'cs_keyan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgEPB1KpyHV1zQAAm1',
'fid':1,
'size':903093,
'from':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'to':'"谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud>',
'subject':'Fw: 关于推荐2018年度“中国高等学校十大科技进展”候选项目的通知',
'sentDate':newdate(2018,8,21,15,13,53),
'receivedDate':newdate(2018,8,21,15,13,52),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<201809211513531833067@fudan.edu.cn>'}},
{
'addT':'"ResearchGate" <no-reply@researchgatemail.net>',
'add':'ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgPBFKp0sCcEAAAsn',
'fid':1,
'size':25581,
'from':'"ResearchGate" <no-reply@researchgatemail.net>',
'to':'"Chengrong Wu" <cwu@fudan.edu.cn>',
'subject':'Chengrong, you were cited by an author from Université d\'Orléans',
'sentDate':newdate(2018,8,21,15,7,53),
'receivedDate':newdate(2018,8,21,15,16,38),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<20180921070753.437E6300040DA@mr60.researchgate.net>'}},
{
'addT':'"ResearchGate" <no-reply@researchgatemail.net>',
'add':'ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYPBFKp0sCQ6AAAsd',
'fid':1,
'size':21974,
'from':'"ResearchGate" <no-reply@researchgatemail.net>',
'to':'cwu@fudan.edu.cn',
'subject':'Chengrong, did this researcher author this publication?',
'sentDate':newdate(2018,8,21,14,17,8),
'receivedDate':newdate(2018,8,21,14,26,32),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<20180921061708.811F22006529D@mr57.researchgate.net>'}},
{
'addT':'"中国农业银行" <e-statement@creditcard.abchina.com>',
'add':'中国农业银行',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgMPBFKpyHVnjwAAsk',
'fid':1,
'size':100797,
'from':'"中国农业银行" <e-statement@creditcard.abchina.com>',
'to':'cwu@fudan.edu.cn',
'subject':'中国农业银行金穗信用卡电子对账单',
'sentDate':newdate(2018,8,21,14,8,7),
'receivedDate':newdate(2018,8,21,14,12,22),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<5BA48AC7.010617.18948@HQsPVL-ZDTD-A01>'}},
{
'addT':'"何加林" <czhejialin@163.com>',
'add':'何加林',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgkPDlKpyHVGaQAAmj',
'fid':1,
'size':34490,
'from':'"何加林" <czhejialin@163.com>',
'to':'caoyu@fudan.edu.cn, xiucao@fudan.edu.cn, mmchi@fudan.edu.cn, wnchen@fudan.edu.cn, chenlf@fudan.edu.cn, xqchen@fudan.edu.cn, tbchen@fudan.edu.cn, bhchen@fudan.edu.cn, yijiachen@fudan.edu.cn, chenrh@fudan.edu.cn, chenc@fudan.edu.cn, chenyq@fudan.edu.cn, dingx@fudan.edu.cn, dingsf@fudan.edu.cn, kydai@fudan.edu.cn, fu',
'subject':'《电与磁的材料问题》',
'sentDate':newdate(2018,8,21,10,31,27),
'receivedDate':newdate(2018,8,21,11,17,34),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<50a39f2b.42b4.165f9f7bcab.Coremail.czhejialin@163.com>'}},
{
'addT':'"上海市科学技术委员会" <infomail@newsletter.stcsm.gov.cn>',
'add':'上海市科学技术委员会',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgPBFKp0sBhdwAAs9',
'fid':1,
'size':38330,
'from':'"上海市科学技术委员会" <infomail@newsletter.stcsm.gov.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'科技服务信息专递第四百五十四期',
'sentDate':newdate(2018,8,21,10,28,43),
'receivedDate':newdate(2018,8,21,10,34,10),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<20180921022846.02DF7742F03@mx130.sx67.email-deliver.com>'}},
{
'addT':'"ResearchGate" <no-reply@researchgatemail.net>',
'add':'ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcPBFKp0sBY8QAAsN',
'fid':1,
'size':20833,
'from':'"ResearchGate" <no-reply@researchgatemail.net>',
'to':'"Chengrong Wu" <cwu@fudan.edu.cn>',
'subject':'Chengrong, you have 1 more citation',
'sentDate':newdate(2018,8,21,9,47,55),
'receivedDate':newdate(2018,8,21,9,56,24),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<20180921014755.2B5FB92C8@mr94.researchgate.net>'}},
{
'addT':'"Fan Wu" <fwu@cs.sjtu.edu.cn>',
'add':'Fan Wu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgIPEVKpyHVeGAAAme',
'fid':1,
'size':741304,
'from':'"Fan Wu" <fwu@cs.sjtu.edu.cn>',
'to':'CCF-Shanghai@cs.sjtu.edu.cn',
'subject':'[CCF-Shanghai] FW: 回复： CNCC2018报名情况统计及组团福利',
'sentDate':newdate(2018,8,21,9,38,1),
'receivedDate':newdate(2018,8,21,13,25,8),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'inlineAttached':'true'},
'hmid':'<006901d4514b$bca712d0$35f53870$@cs.sjtu.edu.cn>',
'ref':'<20180921011307.BD2FD4140091@webmail.sinamail.sina.com.cn>'}},
{
'addT':'"古短愛" <tri.945125@gmail.com>',
'add':'古短愛',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgQPBFKpyHUmAAACsv',
'fid':1,
'size':3250706,
'from':'"古短愛" <tri.945125@gmail.com>',
'to':'cwu@fudan.edu.cn',
'subject':'э乔石痛批政法委周И=永v康',
'sentDate':newdate(2018,8,21,9,12,1),
'receivedDate':newdate(2018,8,21,9,13,27),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<CAHQk4=342ya4+Bp+3-Q5fHbVN_YPhYq9YcDdxn1hSX=9qyjMdw@mail.gmail.com>'}},
{
'addT':'"Bank of America" <Bank of America>',
'add':'Bank of America',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgQPBFKpyHUmAAABss',
'fid':1,
'size':10979,
'from':'"Bank of America" <Bank of America>',
'to':'cwu@fudan.edu.cn',
'subject':'Bank of America alert : Your account has been locked',
'sentDate':newdate(2018,8,21,7,46,21),
'receivedDate':newdate(2018,8,21,9,2,13),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true'},
'hmid':'<20180920234607.9C453740B8C@mail.aspirelearning.org>'}},
{
'addT':'"CCF Digital" <ccfdigital@ccfdigital.cn>',
'add':'CCF Digital',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQUOBFKp0r-5qAAAsJ',
'fid':1,
'size':58292,
'from':'"CCF Digital" <ccfdigital@ccfdigital.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'CCF技术动态【2018第292期】',
'sentDate':newdate(2018,8,20,19,14,34),
'receivedDate':newdate(2018,8,20,19,31,30),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<00e282943116$97ba0a16$4cd15788$@nmcpytw>'}},
{
'addT':'"yuhunmin@163.com" <yuhunmin@163.com>',
'add':'yuhunmin@163.com',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgUOBFKpyHS+WwAAsv',
'fid':1,
'size':37713,
'from':'"yuhunmin@163.com" <yuhunmin@163.com>',
'to':'cwu@fudan.edu.cn, csx1030@163.net',
'subject':'yuhunmin@163.com',
'sentDate':newdate(2018,8,20,17,54,1),
'receivedDate':newdate(2018,8,20,17,54,5),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<5BA36E3C.40B9DB.04431@m50-134.163.com>'}},
{
'addT':'"wanghuimin" <wanghm@fudan.edu.cn>',
'add':'wanghuimin',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggOBFKpyHSs2AAAmz',
'fid':1,
'size':12537,
'from':'"wanghuimin" <wanghm@fudan.edu.cn>',
'to':'"曹瑜" <caoyu@fudan.edu.cn>, fangxf@fudan.edu.cn',
'subject':'Re: Re: 关于保密学院物业管理人员安排事宜',
'sentDate':newdate(2018,8,20,16,29,24),
'receivedDate':newdate(2018,8,20,16,29,29),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<409046b1.41c41.165f61916e8.Coremail.wanghm@fudan.edu.cn>',
'ref':'<201809201451281118223@fudan.edu.cn>'}},
{
'addT':'"wanghuimin" <wanghm@fudan.edu.cn>',
'add':'wanghuimin',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgMOBFKpyHSatQAAmj',
'fid':1,
'size':24680,
'from':'"wanghuimin" <wanghm@fudan.edu.cn>',
'to':'"曹瑜" <caoyu@fudan.edu.cn>',
'subject':'Re: Re: 搬迁费用支付事宜',
'sentDate':newdate(2018,8,20,15,8,40),
'receivedDate':newdate(2018,8,20,15,8,44),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<39251434.4149f.165f5cf305e.Coremail.wanghm@fudan.edu.cn>',
'ref':'<61a417f7.2cf32.165d66b46d5.Coremail.wanghm@fudan.edu.cn>,<201809141305000707386@fudan.edu.cn>,<29b3bda8.2e33e.165d747146e.Coremail.wanghm@fudan.edu.cn>,<201809181101255664612@fudan.edu.cn>,<4d807a06.3ac5d.165ecbac2fb.Coremail.wanghm@fudan.edu.cn>,<201809201445400183802@fudan.edu.cn>'}},
{
'addT':'"曹瑜" <caoyu@fudan.edu.cn>',
'add':'曹瑜',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggOE1KpyHSV2QAAmc',
'fid':1,
'size':11828,
'from':'"曹瑜" <caoyu@fudan.edu.cn>',
'to':'"wanghuimin" <wanghm@fudan.edu.cn>, "方旭峰" <fangxf@fudan.edu.cn>',
'subject':'Re: 关于保密学院物业管理人员安排事宜',
'sentDate':newdate(2018,8,20,14,51,29),
'receivedDate':newdate(2018,8,20,14,51,31),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<201809201451281118223@fudan.edu.cn>'}},
{
'addT':'"曹瑜" <caoyu@fudan.edu.cn>',
'add':'曹瑜',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgOE1Kp0r+5TQAAm2',
'fid':1,
'size':24674,
'from':'"曹瑜" <caoyu@fudan.edu.cn>',
'to':'"wanghuimin" <wanghm@fudan.edu.cn>',
'subject':'Re: 搬迁费用支付事宜',
'sentDate':newdate(2018,8,20,14,45,40),
'receivedDate':newdate(2018,8,20,14,45,42),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<201809201445400183802@fudan.edu.cn>',
'ref':'<61a417f7.2cf32.165d66b46d5.Coremail.wanghm@fudan.edu.cn>,<201809141305000707386@fudan.edu.cn>,<29b3bda8.2e33e.165d747146e.Coremail.wanghm@fudan.edu.cn>,<201809181101255664612@fudan.edu.cn>,<4d807a06.3ac5d.165ecbac2fb.Coremail.wanghm@fudan.edu.cn>'}},
{
'addT':'"wanghuimin" <wanghm@fudan.edu.cn>',
'add':'wanghuimin',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgOE1Kp0r+30gAAmn',
'fid':1,
'size':17920,
'from':'"wanghuimin" <wanghm@fudan.edu.cn>',
'to':'"曹瑜" <caoyu@fudan.edu.cn>',
'subject':'搬迁费用支付事宜',
'sentDate':newdate(2018,8,20,14,38,58),
'receivedDate':newdate(2018,8,20,14,39,2),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<1dd2c7f4.411a3.165f5b3fdf4.Coremail.wanghm@fudan.edu.cn>',
'ref':'<61a417f7.2cf32.165d66b46d5.Coremail.wanghm@fudan.edu.cn>,<201809141305000707386@fudan.edu.cn>,<29b3bda8.2e33e.165d747146e.Coremail.wanghm@fudan.edu.cn><201809181101255664612@fudan.edu.cn><4d807a06.3ac5d.165ecbac2fb.Coremail.wanghm@fudan.edu.cn>'}},
{
'addT':'"wanghuimin" <wanghm@fudan.edu.cn>',
'add':'wanghuimin',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcOBFKp0r+zXwAAm2',
'fid':1,
'size':4687,
'from':'"wanghuimin" <wanghm@fudan.edu.cn>',
'to':'"姚晓枝" <xzyao@fudan.edu.cn>',
'subject':'关于保密学院物业管理人员安排事宜',
'sentDate':newdate(2018,8,20,14,19,58),
'receivedDate':newdate(2018,8,20,14,20,2),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<57b58b99.40f9a.165f5a29785.Coremail.wanghm@fudan.edu.cn>'}},
{
'addT':'"计算机学院人事" <cs_renshi@fudan.edu.cn>',
'add':'计算机学院人事',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgEODVKpyHRxiQAAm-',
'fid':1,
'size':28005,
'from':'"计算机学院人事" <cs_renshi@fudan.edu.cn>',
'to':'"颜波" <byan@fudan.edu.cn>, "吴承荣" <cwu@fudan.edu.cn>, "肖川" <cxiao@fudan.edu.cn>, "朱崇湘" <cxzhu@fudan.edu.cn>, "叶 德建" <dejianye@fudan.edu.cn>, "王放" <fangwang@fudan.edu.cn>, "王国平" <gpwang@fudan.edu.cn>, "张建国" <jgzhang@fudan.edu.cn>, "周健敏" <jmz0806@163.com>, "张军平" <jpzhang@fudan.edu.cn>, "吴杰" <jwu@fudan.edu.cn>, "叶家"',
'subject':'关于2018年度下半年党政管理岗位公开招聘的通知',
'sentDate':newdate(2018,8,20,12,11,2),
'receivedDate':newdate(2018,8,20,11,28,20),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<2018092010580822663923@fudan.edu.cn>'}},
{
'addT':'"计算机学院" <cs_school@fudan.edu.cn>',
'add':'计算机学院',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgOCVKp0r+OHgAAmI',
'fid':1,
'size':807146,
'from':'"计算机学院" <cs_school@fudan.edu.cn>',
'to':'"汪 卫" <weiwang1@fudan.edu.cn>, "王 放" <fangwang@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 新" <xinw@fudan.edu.cn>, "王 雪平" <>',
'subject':'复旦大学货物零星采购实施细则（暂行）（0910征求意见稿）',
'sentDate':newdate(2018,8,20,10,50,4),
'receivedDate':newdate(2018,8,20,10,50,7),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<tencent_5F81FECAF46C85EAD53C0B1D@qq.com>'}},
{
'addT':'LAKAKA@mail.iwmsme.org',
'add':'LAKAKA',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgMOBFKpyHRklQAAs9',
'fid':1,
'size':82577,
'from':'LAKAKA@mail.iwmsme.org',
'to':'cwu@fudan.edu.cn',
'subject':'第二届iwmsme2018征集原创优质稿件由IOP conference series出版',
'sentDate':newdate(2018,8,20,10,23,58),
'receivedDate':newdate(2018,8,20,10,31,12),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<01010165f4ca87c0-e06c85a4-23d9-4f35-bad8-40c16c946ff9-000000@us-west-2.amazonses.com>'}},
{
'addT':'"LJQ" <jsgnljq@163.com>',
'add':'LJQ',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcOBFKp0r9-zwAAsq',
'fid':1,
'size':4439,
'from':'"LJQ" <jsgnljq@163.com>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re:已提交的论文',
'sentDate':newdate(2018,8,20,9,49,14),
'receivedDate':newdate(2018,8,20,9,49,15),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<774656d0.3bce.165f4aaba48.Coremail.jsgnljq@163.com>',
'ref':'<001201d45082$c043b3e0$40cb1ba0$@fudan.edu.cn>'}},
{
'addT':'"wmfu" <wmfu@fudan.edu.cn>',
'add':'wmfu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'HIGH',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgQNDlKpyHO8vwAAmG',
'fid':1,
'size':75176,
'from':'"wmfu" <wmfu@fudan.edu.cn>',
'to':'18210240027@fudan.edu.cn, 18210240038@fudan.edu.cn, 18210240123@fudan.edu.cn, 18210240136@fudan.edu.cn, 18210240075@fudan.edu.cn, 18210240173@fudan.edu.cn, 18210240110@fudan.edu.cn, 18210240262@fudan.edu.cn, 18210240237@fudan.edu.cn, 18210240252@fudan.edu.cn, 18210240146@fudan.edu.cn, 18210240082@fudan.edu.cn',
'subject':'转发学院: 关于2018年中秋节期间若干工作安排的通知－望大家注意实验室中秋假期的安全！',
'sentDate':newdate(2018,8,19,14,17,34),
'receivedDate':newdate(2018,8,19,14,17,41),
'priority':1,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<76a1ba93.3d1a5.165f07a0aa4.Coremail.wmfu@fudan.edu.cn>',
'ref':'<7fbb2e2b.1ab18.165c158bebf.Coremail.wmfu@fudan.edu.cn>'}},
{
'addT':'"计算机学院" <cs_school@fudan.edu.cn>',
'add':'计算机学院',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggNCVKpyHOQcQAAmv',
'fid':1,
'size':16841,
'from':'"计算机学院" <cs_school@fudan.edu.cn>',
'to':'"汪 卫" <weiwang1@fudan.edu.cn>, "王 放" <fangwang@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 新" <xinw@fudan.edu.cn>, "王 雪平" <>',
'subject':'关于2018年中秋节期间若干工作安排的通知',
'sentDate':newdate(2018,8,19,10,26,19),
'receivedDate':newdate(2018,8,19,10,26,22),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<tencent_F4B910811ED13DDDF78B432C@qq.com>'}},
{
'addT':'zxzj@sheitc.gov.cn',
'add':'zxzj',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQENBFKp0r6yMQAAsd',
'fid':1,
'size':19180,
'from':'zxzj@sheitc.gov.cn',
'to':'cwu@fudan.edu.cn',
'subject':'上海市经济和信息化委员会项目评审邀请函',
'sentDate':newdate(2018,8,19,10,12,47),
'receivedDate':newdate(2018,8,19,10,14,20),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<1082356494.412.1537323177626.JavaMail.zxzjadmin@zxzjwebnew>'}},
{
'addT':'"CFP Conference" <cfp.conference2016@GMAIL.COM>',
'add':'CFP Conference',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggNBFKpyHOOwgAAsP',
'fid':1,
'size':71039,
'from':'"CFP Conference" <cfp.conference2016@GMAIL.COM>',
'to':'BIGDATA@LISTS.DREXEL.EDU',
'subject':'IEEE BigData 2018 Call for Workshop Papers and Posters',
'sentDate':newdate(2018,8,19,9,26,14),
'receivedDate':newdate(2018,8,19,10,19,11),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<CAEvuEAuH3OORG_BQ_XBTTA1yO=VS7btzpDa6_2SYbJDaOgYdog@mail.gmail.com>'}},
{
'addT':'"ResearchGate" <no-reply@researchgatemail.net>',
'add':'ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgMBFKp0r5hXQAAsq',
'fid':1,
'size':64338,
'from':'"ResearchGate" <no-reply@researchgatemail.net>',
'to':'"Chengrong Wu" <cwu@fudan.edu.cn>',
'subject':'Wei Wang published an article',
'sentDate':newdate(2018,8,18,22,4,33),
'receivedDate':newdate(2018,8,18,22,11,37),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<20180918140433.7AD798003F5D@mr78.researchgate.net>'}},
{
'addT':'"sicase@sicase.org" <sicase@sicase.org>',
'add':'sicase@sicase.org',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgIMBFKpyHMzOQAAsC',
'fid':1,
'size':12082,
'from':'"sicase@sicase.org" <sicase@sicase.org>',
'to':'cwu@fudan.edu.cn',
'subject':'Re:[2019 Seoul Conference Invitation]*Applied Science*Engineering',
'sentDate':newdate(2018,8,18,21,9,48),
'receivedDate':newdate(2018,8,18,21,14,45),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<01000165eccd1790-791ed0ac-1127-4e3c-9e3b-e00f277d2179-000000@email.amazonses.com>'}},
{
'addT':'"wanghuimin" <wanghm@fudan.edu.cn>',
'add':'wanghuimin',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYME1Kp0r5WNAAAmt',
'fid':1,
'size':30559,
'from':'"wanghuimin" <wanghm@fudan.edu.cn>',
'to':'"吴承荣" <cwu@fudan.edu.cn>',
'subject':'复旦大学国家保密学院暨国家保密教育培训基地上海分基地总结（2016-2018）',
'sentDate':newdate(2018,8,18,21,5,43),
'receivedDate':newdate(2018,8,18,21,5,50),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<8806abe.3ad3e.165ecc95930.Coremail.wanghm@fudan.edu.cn>'}},
{
'addT':'"wanghuimin" <wanghm@fudan.edu.cn>',
'add':'wanghuimin',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcMBFKp0r5TXgAAmU',
'fid':1,
'size':15450,
'from':'"wanghuimin" <wanghm@fudan.edu.cn>',
'to':'"曹瑜" <caoyu@fudan.edu.cn>, "吴承荣" <cwu@fudan.edu.cn>',
'subject':'Re: Re: Re:_Re:_专项经费项目预算模板---9.14',
'sentDate':newdate(2018,8,18,20,49,47),
'receivedDate':newdate(2018,8,18,20,49,54),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<4d807a06.3ac5d.165ecbac2fb.Coremail.wanghm@fudan.edu.cn>',
'ref':'<61a417f7.2cf32.165d66b46d5.Coremail.wanghm@fudan.edu.cn>,<201809141305000707386@fudan.edu.cn>,<29b3bda8.2e33e.165d747146e.Coremail.wanghm@fudan.edu.cn><201809181101255664612@fudan.edu.cn>,<201809181101255664612@fudan.edu.cn>'}},
{
'addT':'"计算机学院人事" <cs_renshi@fudan.edu.cn>',
'add':'计算机学院人事',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgYMDVKpyHMBzQAAmJ',
'fid':1,
'size':1381943,
'from':'"计算机学院人事" <cs_renshi@fudan.edu.cn>',
'to':'"颜波" <byan@fudan.edu.cn>, "吴承荣" <cwu@fudan.edu.cn>, "肖川" <cxiao@fudan.edu.cn>, "朱崇湘" <cxzhu@fudan.edu.cn>, "叶 德建" <dejianye@fudan.edu.cn>, "王放" <fangwang@fudan.edu.cn>, "王国平" <gpwang@fudan.edu.cn>, "张建国" <jgzhang@fudan.edu.cn>, "周健敏" <jmz0806@163.com>, "张军平" <jpzhang@fudan.edu.cn>, "吴杰" <jwu@fudan.edu.cn>, "叶家"',
'subject':'【重要通知】关于2019年度公派出国计划申报的通知',
'sentDate':newdate(2018,8,18,17,17,31),
'receivedDate':newdate(2018,8,18,16,34,53),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<2018091817173138477117@fudan.edu.cn>'}},
{
'addT':'"wmfu" <wmfu@fudan.edu.cn>',
'add':'wmfu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggMCFKpyHLlXgAAm0',
'fid':1,
'size':6464,
'from':'"wmfu" <wmfu@fudan.edu.cn>',
'to':'"xuwuxing" <by70_by70@aliyun.com>',
'subject':'Re: Fw:中矿大信息安全专业推免生徐武兴',
'sentDate':newdate(2018,8,18,14,25,17),
'receivedDate':newdate(2018,8,18,14,25,22),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<590896d2.39155.165eb5abd64.Coremail.wmfu@fudan.edu.cn>',
'ref':'<276f87a0.3129f.165e0039e5c.Coremail.cwu@fudan.edu.cn>'}},
{
'addT':'"wmfu" <wmfu@fudan.edu.cn>',
'add':'wmfu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'HIGH',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQIMDlKp0r4GCwAAmb',
'fid':1,
'size':7453,
'from':'"wmfu" <wmfu@fudan.edu.cn>',
'to':'"wmfu" <wmfu@fudan.edu.cn>',
'subject':'提醒－Re: 兹定于9月19日（周三）上午9时在逸夫楼407室，迎新2018级全体研究生，请课题组老师和2018级全体新生参加！NiSL-Sept-12-2018',
'sentDate':newdate(2018,8,18,14,14,58),
'receivedDate':newdate(2018,8,18,14,15,4),
'priority':1,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<439ccdce.39059.165eb514c35.Coremail.wmfu@fudan.edu.cn>',
'ref':'<2ae1c403.24f56.165cca154c5.Coremail.wmfu@fudan.edu.cn>'}},
{
'addT':'"julie-zhu" <sjtu-julie@sjtu.edu.cn>',
'add':'julie-zhu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggMBFKpyHLdkgAAsM',
'fid':1,
'size':7603,
'from':'"julie-zhu" <sjtu-julie@sjtu.edu.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'上海交大高教院课题组诚邀您参与高校科研人才评价政策认同情况调查',
'sentDate':newdate(2018,8,18,13,51,29),
'receivedDate':newdate(2018,8,18,13,53,18),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<706515315.6491482.1537249889850.JavaMail.jetty@sc-10_9_50_67-webapi>'}},
{
'addT':'"曹瑜" <caoyu@fudan.edu.cn>',
'add':'曹瑜',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQUME1Kp0r3fSgAAma',
'fid':1,
'size':15051,
'from':'"曹瑜" <caoyu@fudan.edu.cn>',
'to':'"wanghuimin" <wanghm@fudan.edu.cn>',
'subject':'Re: Re:_Re:_专项经费项目预算模板---9.14',
'sentDate':newdate(2018,8,18,11,1,26),
'receivedDate':newdate(2018,8,18,11,1,27),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<201809181101255664612@fudan.edu.cn>',
'ref':'<61a417f7.2cf32.165d66b46d5.Coremail.wanghm@fudan.edu.cn>,<201809141305000707386@fudan.edu.cn>,<29b3bda8.2e33e.165d747146e.Coremail.wanghm@fudan.edu.cn>'}},
{
'addT':'"沈建蓉" <jrshen@fudan.edu.cn>',
'add':'沈建蓉',
'icon':{
'm_icon':'NORMAL',
'p_icon':'HIGH',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgELEFKpyHJZoQAAmh',
'fid':1,
'size':13166,
'from':'"沈建蓉" <jrshen@fudan.edu.cn>',
'to':'"chenyq" <chenyq@fudan.edu.cn>, "ygj" <ygj@fudan.edu.cn>, "hbkan" <hbkan@fudan.edu.cn>, "lijt" <lijt@fudan.edu.cn>, "limb" <limb@fudan.edu.cn>, "weili-fudan" <weili-fudan@fudan.edu.cn>, "xpqiu" <xpqiu@fudan.edu.cn>, "zjtan" <zjtan@fudan.edu.cn>, "weiwang1" <weiwang1@fudan.edu.cn>, "wangfei" <wangfei@fudan.ed>',
'subject':'请评审您的学生的学位论文和项目视频',
'sentDate':newdate(2018,8,17,21,39,7),
'receivedDate':newdate(2018,8,17,21,39,13),
'priority':1,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<201809172138073675559@fudan.edu.cn>'}},
{
'addT':'"LJQ" <jsgnljq@163.com>',
'add':'LJQ',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQELBFKp0r1pEQAAsj',
'fid':1,
'size':215828,
'from':'"LJQ" <jsgnljq@163.com>',
'to':'"cwu@fudan.edu.cn" <cwu@fudan.edu.cn>',
'subject':'IP地址跳变机制抗扫描能力评估4',
'sentDate':newdate(2018,8,17,19,16,41),
'receivedDate':newdate(2018,8,17,19,16,43),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<4f42796c.dae4.165e73f2a61.Coremail.jsgnljq@163.com>'}},
{
'addT':'"龚洁" <gongjie@fudan.edu.cn>',
'add':'龚洁',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQILEVKp0r1Y-QAAmo',
'fid':1,
'size':1479,
'from':'"龚洁" <gongjie@fudan.edu.cn>',
'to':'"阚海斌" <hbkan@fudan.edu.cn>, "ylzhao" <ylzhao@fudan.edu.cn>, "cwu" <cwu@fudan.edu.cn>, "bhchen" <bhchen@fudan.edu.cn>, zhengxq@fudan.edu.cn',
'subject':'明天推免面试通知（调整）',
'sentDate':newdate(2018,8,17,17,35,59),
'receivedDate':newdate(2018,8,17,17,36,4),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<723d5422.360a1.165e6e2faab.Coremail.gongjie@fudan.edu.cn>'}},
{
'addT':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'add':'cs_keyan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgYLB1KpyHId6wAAm-',
'fid':1,
'size':133830,
'from':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'to':'"谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud>',
'subject':'Fw: 转发科技部国际合作司关于征集中国－黑山政府间科技合作委员会第3届例会交流项目的通知',
'sentDate':newdate(2018,8,17,15,37,27),
'receivedDate':newdate(2018,8,17,15,37,32),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<201809171537273745444@fudan.edu.cn>'}},
{
'addT':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'add':'cs_keyan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgkLB1KpyHId3AAAmH',
'fid':1,
'size':129707,
'from':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'to':'"谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud>',
'subject':'Fw: 转发科技部国际合作司关于征集中泰（国）政府间科技合作联委会短期交流项目的通知',
'sentDate':newdate(2018,8,17,15,37,6),
'receivedDate':newdate(2018,8,17,15,37,12),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<201809171537059343253@fudan.edu.cn>'}},
{
'addT':'"tang@e-neurons.net" <tang@e-neurons.net>',
'add':'tang@e-neurons.net',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgQLBFKpyHIYxgAAsW',
'fid':1,
'size':1630373,
'from':'"tang@e-neurons.net" <tang@e-neurons.net>',
'to':'"丁瑞浩" <dingruihao23@163.com>, "陆新" <eluxin@139.com>, "游红俊" <snowolf8271@sina.com>, "杭玲" <linda.hang@dbappsecurity.com.cn>, "蒋涛" <5670545@qq.com>, "阮伟" <ruanwei@zju.edu.cn>, "王雪怡" <wangxueyi@sjtu.edu.cn>, "徐巍" <xuweisome@sjtu.edu.cn>, "崔涛" <cuitao@catr.cn>, "张第" <zhangdi49@chinaunicom.cn>, "冯四风" <feng_sifeng@1>',
'subject':'拟联[2018]3号：关于拟态核心专利授权协议（2018修订版）的通知',
'sentDate':newdate(2018,8,17,15,17,16),
'receivedDate':newdate(2018,8,17,15,17,34),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<2018091715105848666049@e-neurons.net>'}},
{
'addT':'"计算机学院工会" <cs_gonghui@fudan.edu.cn>',
'add':'计算机学院工会',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYLCFKp0r02CQAAmv',
'fid':1,
'size':8022,
'from':'"计算机学院工会" <cs_gonghui@fudan.edu.cn>',
'to':'"汪 卫" <weiwang1@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 雪平" <wangxp@fudan.edu.cn>, "王 毅敏" <yiminwang@fudan.edu.cn>, "王"',
'subject':'关于2018年下半年办理工会会员服务卡的通知',
'sentDate':newdate(2018,8,17,14,44,44),
'receivedDate':newdate(2018,8,17,14,44,50),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<4e9f8ef1.34fba.165e6462f8b.Coremail.cs_gonghui@fudan.edu.cn>'}},
{
'addT':'"余莉萍" <17210240022@fudan.edu.cn>',
'add':'余莉萍',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgULBFKpyHH1CAABs2',
'fid':1,
'size':8361,
'from':'"余莉萍" <17210240022@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: 关于信息安全导论作业的打分',
'sentDate':newdate(2018,8,17,12,22,20),
'receivedDate':newdate(2018,8,17,12,22,24),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<7402cbe2.344e1.165e5c3d2c2.Coremail.17210240022@fudan.edu.cn>',
'ref':'<000801d44e3a$723f5590$56be00b0$@fudan.edu.cn>'}},
{
'addT':'"luzhihui" <lzh@fudan.edu.cn>',
'add':'luzhihui',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgULBFKpyHH1CAAAs3',
'fid':1,
'size':30897,
'from':'"luzhihui" <lzh@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: RE: RE: 数荃公司的项目想约大家讨论一下',
'sentDate':newdate(2018,8,17,12,5,32),
'receivedDate':newdate(2018,8,17,12,5,34),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<201809171205326981254@fudan.edu.cn>',
'ref':'<006701d44bfc$4cb725e0$e62571a0$@fudan.edu.cn>,<201809170802023413445@fudan.edu.cn>,<000001d44e29$071fb090$155f11b0$@fudan.edu.cn>,<201809171148321769004@fudan.edu.cn>,<000d01d44e3a$d6953780$83bfa680$@fudan.edu.cn>'}},
{
'addT':'"luzhihui" <lzh@fudan.edu.cn>',
'add':'luzhihui',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgLBFKp0rzzxwADsk',
'fid':1,
'size':20407,
'from':'"luzhihui" <lzh@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: RE: 数荃公司的项目想约大家讨论一下',
'sentDate':newdate(2018,8,17,11,48,32),
'receivedDate':newdate(2018,8,17,11,48,34),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<201809171148321769004@fudan.edu.cn>',
'ref':'<006701d44bfc$4cb725e0$e62571a0$@fudan.edu.cn>,<201809170802023413445@fudan.edu.cn>,<000001d44e29$071fb090$155f11b0$@fudan.edu.cn>'}},
{
'addT':'"gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn>',
'add':'gongjie@fudan.edu.cn',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYLEVKp0rztaAAAmN',
'fid':1,
'size':4077,
'from':'"gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn>',
'to':'"阚海斌" <hbkan@fudan.edu.cn>, "赵运磊" <ylzhao@fudan.edu.cn>, "吴承荣" <cwu@fudan.edu.cn>, "吕智慧" <lzh@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>',
'subject':'周二本科推免资格面试通知',
'sentDate':newdate(2018,8,17,8,43,51),
'receivedDate':newdate(2018,8,17,8,43,52),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<201809170842514162506@fudan.edu.cn>'}},
{
'addT':'"luzhihui" <lzh@fudan.edu.cn>',
'add':'luzhihui',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcKBFKp0rzQHQADsT',
'fid':1,
'size':9943,
'from':'"luzhihui" <lzh@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: 数荃公司的项目想约大家讨论一下',
'sentDate':newdate(2018,8,17,8,2,4),
'receivedDate':newdate(2018,8,17,8,2,5),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<201809170802023413445@fudan.edu.cn>',
'ref':'<006701d44bfc$4cb725e0$e62571a0$@fudan.edu.cn>'}},
{
'addT':'"xu jingnan" <xujn@fudan.edu.cn>',
'add':'xu jingnan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQIKBFKp0rybTwAAsM',
'fid':1,
'size':11261,
'from':'"xu jingnan" <xujn@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'回复: 回复: 一个软件著作权，之前没有提交的',
'sentDate':newdate(2018,8,16,13,27,23),
'receivedDate':newdate(2018,8,16,13,27,23),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<2018091613262378578624@fudan.edu.cn>',
'ref':'<003501d44bd1$c84a7d40$58df77c0$@fudan.edu.cn>,<2018091612291955657622@fudan.edu.cn>'}},
{
'addT':'"xu jingnan" <xujn@fudan.edu.cn>',
'add':'xu jingnan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgMKBFKpyHFrmQABs+',
'fid':1,
'size':6916,
'from':'"xu jingnan" <xujn@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'回复: 一个软件著作权，之前没有提交的',
'sentDate':newdate(2018,8,16,12,30,29),
'receivedDate':newdate(2018,8,16,12,30,28),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<2018091612291955657622@fudan.edu.cn>',
'ref':'<003501d44bd1$c84a7d40$58df77c0$@fudan.edu.cn>'}},
{
'addT':'"携程旅行网" <recommend@lists4.ctrip.com>',
'add':'携程旅行网',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgMKBFKpyHFrmQAAs-',
'fid':1,
'size':30167,
'from':'"携程旅行网" <recommend@lists4.ctrip.com>',
'to':'cwu@fudan.edu.cn',
'subject':'抢199元低价出游！更有900元旅游首单券等您来拿！',
'sentDate':newdate(2018,8,16,10,51,53),
'receivedDate':newdate(2018,8,16,11,4,2),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<20180916025153.7DD2D6C3F34@mx7.ey1info.ctrip.com>'}},
{
'addT':'"Lbj Wei" <weilbj6@gmail.com>',
'add':'Lbj Wei',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYJBFKp0rxsLQAAse',
'fid':1,
'size':12456570,
'from':'"Lbj Wei" <weilbj6@gmail.com>',
'to':'',
'subject':'Fwd: 主题：2018年9月14日星期五 ……【周末快乐！】',
'sentDate':newdate(2018,8,16,0,36,19),
'receivedDate':newdate(2018,8,16,1,45,51),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'attached':'true'},
'hmid':'<CAAMf=PXdd5bvZ5VzfzWog=TJqFfDCUbk8j2qKhtgGA4NGewqkA@mail.gmail.com>',
'ref':'<CAEcH=zjuzaE7TbYu0cLLafkFfip3SYJ8fOQBTwrPxW4=G0LC3Q@mail.gmail.com>'}},
{
'addT':'"xuwuxing" <by70_by70@aliyun.com>',
'add':'xuwuxing',
'icon':{
'm_icon':'FORWARDED',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgkJBFKpyHETUAABsG',
'fid':1,
'size':4458706,
'from':'"xuwuxing" <by70_by70@aliyun.com>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'中矿大信息安全专业推免生徐武兴',
'sentDate':newdate(2018,8,15,16,10,8),
'receivedDate':newdate(2018,8,15,16,10,13),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'attached':'true',
'forwarded':'true'},
'hmid':'<c1f568c0-71f0-4349-93ac-4803171a3bdf.by70_by70@aliyun.com>'}},
{
'addT':'"何加林" <czhejialin@163.com>',
'add':'何加林',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgYJDlKpyHDrAQAAmq',
'fid':1,
'size':1338109,
'from':'"何加林" <czhejialin@163.com>',
'to':'caoyu@fudan.edu.cn, xiucao@fudan.edu.cn, mmchi@fudan.edu.cn, wnchen@fudan.edu.cn, chenlf@fudan.edu.cn, xqchen@fudan.edu.cn, tbchen@fudan.edu.cn, bhchen@fudan.edu.cn, yijiachen@fudan.edu.cn, chenrh@fudan.edu.cn, chenc@fudan.edu.cn, chenyq@fudan.edu.cn, dingx@fudan.edu.cn, dingsf@fudan.edu.cn, kydai@fudan.edu.cn, fu',
'subject':'《电学理论的物质矛盾》',
'sentDate':newdate(2018,8,15,8,35,52),
'receivedDate':newdate(2018,8,15,9,22,5),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true',
'inlineAttached':'true'},
'hmid':'<29946c0.1a7e.165daa7c456.Coremail.czhejialin@163.com>'}},
{
'addT':'"Fan Wu" <fwu@cs.sjtu.edu.cn>',
'add':'Fan Wu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'LOW',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgIBVKp0rvxPgAAmZ',
'fid':1,
'size':738136,
'from':'"Fan Wu" <fwu@cs.sjtu.edu.cn>',
'to':'CCF-Shanghai@cs.sjtu.edu.cn',
'subject':'[CCF-Shanghai] CNCC2018报名情况统计及组团福利',
'sentDate':newdate(2018,8,14,23,12,23),
'receivedDate':newdate(2018,8,15,2,2,56),
'priority':5,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'inlineAttached':'true'},
'hmid':'<001a01d44c3d$56e65a40$04b30ec0$@cs.sjtu.edu.cn>'}},
{
'addT':'"汪钰颖" <17210240209@fudan.edu.cn>',
'add':'汪钰颖',
'icon':{
'm_icon':'REPLIED',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggIBFKpyHCaDwADsT',
'fid':1,
'size':595894,
'from':'"汪钰颖" <17210240209@fudan.edu.cn>',
'to':'"吴承荣老师" <cwu@fudan.edu.cn>',
'subject':'Splunk应用效果图',
'sentDate':newdate(2018,8,14,21,52,44),
'receivedDate':newdate(2018,8,14,21,52,47),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'attached':'true',
'replied':'true'},
'hmid':'<609c190d.2f15c.165d85af616.Coremail.17210240209@fudan.edu.cn>'}},
{
'addT':'"CCF会员部" <ccfmk@membership.ccf.org.cn>',
'add':'CCF会员部',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggIBFKpyHCaDwABsR',
'fid':1,
'size':95273,
'from':'"CCF会员部" <ccfmk@membership.ccf.org.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'CNCC“早鸟票”倒计时（9月21日结束）',
'sentDate':newdate(2018,8,14,18,32,7),
'receivedDate':newdate(2018,8,14,18,46,35),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<0052a77a6bfa$7d36ee35$6c5b2fa9$@ljhzets>'}},
{
'addT':'"龚洁" <gongjie@fudan.edu.cn>',
'add':'龚洁',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYICFKp0ru0vwAAme',
'fid':1,
'size':609986,
'from':'"龚洁" <gongjie@fudan.edu.cn>',
'to':'"曾剑平" <zjp@fudan.edu.cn>, "陈利锋" <chenlf@fudan.edu.cn>, "池明旻" <mmchi@fudan.edu.cn>, "陈彤兵" <tbchen@fudan.edu.cn>, "陈伟男" <wnchen@fudan.edu.cn>, "曹袖" <Xiucao@fudan.edu.cn>, "陈学青" <xqchen@fudan.edu.cn>, "陈阳" <chenyang@fudan.edu.cn>, "Chen" <yijiachen@fudan.edu.cn>, "陈雁秋" <chenyq@fudan.edu.cn>, "丁向华" <dingx@fudan.e>',
'subject':'本科教学评估材料上报（更新）',
'sentDate':newdate(2018,8,14,17,46,23),
'receivedDate':newdate(2018,8,14,17,46,31),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'attached':'true'},
'hmid':'<7d50e358.a8e8.165d7796aa6.Coremail.gongjie@fudan.edu.cn>',
'ref':'<2018091416235797127717@fudan.edu.cn>'}},
{
'addT':'"wanghuimin" <wanghm@fudan.edu.cn>',
'add':'wanghuimin',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgMIBFKpyHCHqQAAmg',
'fid':1,
'size':31491,
'from':'"wanghuimin" <wanghm@fudan.edu.cn>',
'to':'"曹瑜" <caoyu@fudan.edu.cn>, "吴承荣" <cwu@fudan.edu.cn>, "吴杰" <jwu@fudan.edu.cn>',
'subject':'Re: Re: 专项经费项目预算模板---9.14',
'sentDate':newdate(2018,8,14,16,51,24),
'receivedDate':newdate(2018,8,14,16,51,26),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<29b3bda8.2e33e.165d747146e.Coremail.wanghm@fudan.edu.cn>',
'ref':'<61a417f7.2cf32.165d66b46d5.Coremail.wanghm@fudan.edu.cn><201809141305000707386@fudan.edu.cn>,<201809141305000707386@fudan.edu.cn>'}},
{
'addT':'"gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn>',
'add':'gongjie@fudan.edu.cn',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgUIDlKpyHCCcwAAmz',
'fid':1,
'size':389007,
'from':'"gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn>',
'to':'"曾剑平" <zjp@fudan.edu.cn>, "陈利锋" <chenlf@fudan.edu.cn>, "池明旻" <mmchi@fudan.edu.cn>, "陈彤兵" <tbchen@fudan.edu.cn>, "陈伟男" <wnchen@fudan.edu.cn>, "曹袖" <Xiucao@fudan.edu.cn>, "陈学青" <xqchen@fudan.edu.cn>, "陈阳" <chenyang@fudan.edu.cn>, "Chen" <yijiachen@fudan.edu.cn>, "陈雁秋" <chenyq@fudan.edu.cn>, "丁向华" <dingx@fudan.e>',
'subject':'本科教学评估材料上报',
'sentDate':newdate(2018,8,14,16,24,58),
'receivedDate':newdate(2018,8,14,16,25,1),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<2018091416235797127717@fudan.edu.cn>'}},
{
'addT':'"ResearchGate" <no-reply@researchgatemail.net>',
'add':'ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgQIBFKpyHBu5wAAsA',
'fid':1,
'size':26075,
'from':'"ResearchGate" <no-reply@researchgatemail.net>',
'to':'"Chengrong Wu" <cwu@fudan.edu.cn>',
'subject':'Chengrong, you were recently cited by an author from Universiti Putra Malaysia',
'sentDate':newdate(2018,8,14,14,46,20),
'receivedDate':newdate(2018,8,14,14,51,37),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<20180914064620.363BB2006B6BB@mr63.researchgate.net>'}},
{
'addT':'"sfding" <dingsf@fudan.edu.cn>',
'add':'sfding',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQEIBFKp0ruN0AABsC',
'fid':1,
'size':31799,
'from':'"sfding" <dingsf@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: RE: [重要通知]关于网上评审2019春工程硕士论文的通知',
'sentDate':newdate(2018,8,14,14,43,29),
'receivedDate':newdate(2018,8,14,14,43,30),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<718a3159.2d7a9.165d6d1f77b.Coremail.dingsf@fudan.edu.cn>',
'ref':'<007c01d44bcc$60b7d920$22278b60$@fudan.edu.cn><003b01d44bd8$687fc490$397f4db0$@fudan.edu.cn>,<003b01d44bd8$687fc490$397f4db0$@fudan.edu.cn>'}},
{
'addT':'"计算机学院工会" <cs_gonghui@fudan.edu.cn>',
'add':'计算机学院工会',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcICFKp0ruLCwAAmU',
'fid':1,
'size':29951,
'from':'"计算机学院工会" <cs_gonghui@fudan.edu.cn>',
'to':'"汪 卫" <weiwang1@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 雪平" <wangxp@fudan.edu.cn>, "王 毅敏" <yiminwang@fudan.edu.cn>, "王"',
'subject':'2018年复旦大学教工象棋个人赛比赛通知及报名表',
'sentDate':newdate(2018,8,14,14,21,51),
'receivedDate':newdate(2018,8,14,14,21,54),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<ffa3e6.2d5cd.165d6be297b.Coremail.cs_gonghui@fudan.edu.cn>'}},
{
'addT':'"sfding" <dingsf@fudan.edu.cn>',
'add':'sfding',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgUIBFKpyHBoEgAAsy',
'fid':1,
'size':31741,
'from':'"sfding" <dingsf@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: RE: [重要通知]关于网上评审2019春工程硕士论文的通知',
'sentDate':newdate(2018,8,14,14,11,32),
'receivedDate':newdate(2018,8,14,14,11,33),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<6d08077d.2d4cf.165d6b4b84d.Coremail.dingsf@fudan.edu.cn>',
'ref':'<007c01d44bcc$60b7d920$22278b60$@fudan.edu.cn><003b01d44bd8$687fc490$397f4db0$@fudan.edu.cn>,<003b01d44bd8$687fc490$397f4db0$@fudan.edu.cn>'}},
{
'addT':'"gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn>',
'add':'gongjie@fudan.edu.cn',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQIIBFKp0ruFvAAAmk',
'fid':1,
'size':8815,
'from':'"gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn>',
'to':'"吴承荣" <cwu@fudan.edu.cn>',
'subject':'回复: 下周二免推生面试网络空间安全学科的老师名单',
'sentDate':newdate(2018,8,14,13,55,3),
'receivedDate':newdate(2018,8,14,13,55,5),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<201809141354036317711@fudan.edu.cn>',
'ref':'<004b01d44be9$bab56420$30202c60$@fudan.edu.cn>'}},
{
'addT':'"CCF会员部" <ccfmk@membership.ccf.org.cn>',
'add':'CCF会员部',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYIBFKp0ruBEgABsL',
'fid':1,
'size':96576,
'from':'"CCF会员部" <ccfmk@membership.ccf.org.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'CCF邀请您一起壮大会员队伍',
'sentDate':newdate(2018,8,14,13,17,21),
'receivedDate':newdate(2018,8,14,13,30,31),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<0003c98c5bb9$49075ede$37e2df9c$@njswku>'}},
{
'addT':'"wanghuimin" <wanghm@fudan.edu.cn>',
'add':'wanghuimin',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgIIBFKpyHBaRQAAmQ',
'fid':1,
'size':23843,
'from':'"wanghuimin" <wanghm@fudan.edu.cn>',
'to':'"吴承荣" <cwu@fudan.edu.cn>',
'subject':'专项经费项目预算模板---9.14',
'sentDate':newdate(2018,8,14,12,51,19),
'receivedDate':newdate(2018,8,14,12,51,20),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<61a417f7.2cf32.165d66b46d5.Coremail.wanghm@fudan.edu.cn>'}},
{
'addT':'"上海市科学技术委员会" <infomail@newsletter.stcsm.gov.cn>',
'add':'上海市科学技术委员会',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgEIBFKpyHBQaAAAs0',
'fid':1,
'size':37570,
'from':'"上海市科学技术委员会" <infomail@newsletter.stcsm.gov.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'科技服务信息专递第四百五十三期',
'sentDate':newdate(2018,8,14,11,41,16),
'receivedDate':newdate(2018,8,14,11,46,6),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<20180914034118.4F1C374473A@mx130.sx67.email-deliver.com>'}},
{
'addT':'lfjin@fudan.edu.cn',
'add':'lfjin',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYIBFKp0rtXsAAFs7',
'fid':1,
'size':6046,
'from':'lfjin@fudan.edu.cn',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: 下周二免推生面试，各位老师是否能够参加？',
'sentDate':newdate(2018,8,14,11,23,55),
'receivedDate':newdate(2018,8,14,11,23,56),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<2b17af15.2caef.165d61b4369.Coremail.lfjin@fudan.edu.cn>',
'ref':'<000001d44a93$5b4b81b0$11e28510$@fudan.edu.cn>'}},
{
'addT':'"复旦专利" <fudanzhuanli@fudan.edu.cn>',
'add':'复旦专利',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYIBFKp0rtXsAAEs6',
'fid':1,
'size':1023223,
'from':'"复旦专利" <fudanzhuanli@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'HyperGuard云平台安全审计监管系统',
'sentDate':newdate(2018,8,14,10,9,18),
'receivedDate':newdate(2018,8,14,10,9,20),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'attached':'true'},
'hmid':'<46898366.2c2c1.165d5d6f330.Coremail.fudanzhuanli@fudan.edu.cn>'}},
{
'addT':'"ResearchGate" <no-reply@researchgatemail.net>',
'add':'ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYIBFKp0rtXsAACs8',
'fid':1,
'size':20825,
'from':'"ResearchGate" <no-reply@researchgatemail.net>',
'to':'"Chengrong Wu" <cwu@fudan.edu.cn>',
'subject':'Chengrong, people are reading your work',
'sentDate':newdate(2018,8,14,9,44,13),
'receivedDate':newdate(2018,8,14,9,51,31),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<20180914014413.1102A300008E7@mr61.researchgate.net>'}},
{
'addT':'"dingsf" <dingsf@fudan.edu.cn>',
'add':'dingsf',
'icon':{
'm_icon':'NORMAL',
'p_icon':'HIGH',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgQIAlKpyHA2sAAAmJ',
'fid':1,
'size':25209,
'from':'"dingsf" <dingsf@fudan.edu.cn>',
'to':'kydai@fudan.edu.cn, hwfeng@fudan.edu.cn, lijt@fudan.edu.cn, ylzhao@fudan.edu.cn, xuyx@fudan.edu.cn, chenc@fudan.edu.cn, chenrh@fudan.edu.cn, hbkan@fudan.edu.cn, cfsha@fudan.edu.cn, zjp@fudan.edu.cn, wdzhao@fudan.edu.cn, liy@fudan.edu.cn, yunx@fudan.edu.cn, limin@fudan.edu.cn, pengxin@fudan.edu.cn, zhengxq@fudan.ed',
'subject':'[重要通知]关于网上评审2019春工程硕士论文的通知',
'sentDate':newdate(2018,8,14,9,43,46),
'receivedDate':newdate(2018,8,14,9,38,59),
'priority':1,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<007c01d44bcc$60b7d920$22278b60$@fudan.edu.cn>'}},
{
'addT':'"ResearchGate" <no-reply@researchgatemail.net>',
'add':'ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgQHBFKpyG-kEgAAsv',
'fid':1,
'size':21769,
'from':'"ResearchGate" <no-reply@researchgatemail.net>',
'to':'cwu@fudan.edu.cn',
'subject':'Mostafa Alksher uploaded a full-text citing you',
'sentDate':newdate(2018,8,13,21,23,5),
'receivedDate':newdate(2018,8,13,21,31,38),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<20180913132305.277C12C005963@mr81.researchgate.net>'}},
{
'addT':'"szhang" <szhang@fudan.edu.cn>',
'add':'szhang',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggHDlKpyG-h5wAAmZ',
'fid':1,
'size':9477640,
'from':'"szhang" <szhang@fudan.edu.cn>',
'to':'"Wu Jie" <jwu@fudan.edu.cn>, "cwu" <cwu@fudan.edu.cn>, "严明" <myan@fudan.edu.cn>',
'subject':'Fw: 古河会长访问复旦行程表，solize公司中文介绍',
'sentDate':newdate(2018,8,13,21,18,49),
'receivedDate':newdate(2018,8,13,21,18,56),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<54060b81.9140.165d3158d53.Coremail.szhang@fudan.edu.cn>'}},
{
'addT':'"office" <office.journal46@rediffmail.com>',
'add':'office',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggHBFKpyG-YVgAAsb',
'fid':1,
'size':3879,
'from':'"office" <office.journal46@rediffmail.com>',
'to':'xujj@suda.edu.cn, zhengkai@suda.edu.cn, minzhang@suda.edu.cn, wangzh@hit.edu.cn, jwu@fudan.edu.cn, cwu@fudan.edu.cn, chenyanjiao@whu.edu.cn, yinxy@nwu.edu.cn, zhang.j4@sustc.edu.cn, gracelq628@hnu.edu.cn, yuhong.guo@careton.ca, csgjwang@gmail.com, ychencs@whu.edu.cn, 450867607@qq.com, xxxyczl@csu.edu.cn, pp960712@',
'subject':'Best Ranking Journal',
'sentDate':newdate(2018,8,13,20,13,4),
'receivedDate':newdate(2018,8,13,20,25,27),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<20180913121304.30705.qmail@f5mail-224-163.rediffmail.com>'}},
{
'addT':'"ResearchGate" <no-reply@researchgatemail.net>',
'add':'ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQEHBFKp0rr1wwABsn',
'fid':1,
'size':21377,
'from':'"ResearchGate" <no-reply@researchgatemail.net>',
'to':'cwu@fudan.edu.cn',
'subject':'Congratulations Chengrong, you reached a milestone',
'sentDate':newdate(2018,8,13,20,12,13),
'receivedDate':newdate(2018,8,13,20,21,35),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<20180913121213.D23BE30003385@mr60.researchgate.net>'}},
{
'addT':'invitation@confcfp.org',
'add':'invitation',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQEHBFKp0rr1wwAAsm',
'fid':1,
'size':4644,
'from':'invitation@confcfp.org',
'to':'cwu@fudan.edu.cn',
'subject':'Invited speaker invitation to Wu, Chengrong',
'sentDate':newdate(2018,8,13,20,1,37),
'receivedDate':newdate(2018,8,13,20,5,28),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<01000165d2ceddb4-c4a42998-1acd-49af-8d3e-cf9e1d4236e7-000000@email.amazonses.com>'}},
{
'addT':'"赵运磊" <ylzhao@fudan.edu.cn>',
'add':'赵运磊',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcHBFKp0rrDrAAAs5',
'fid':1,
'size':5765,
'from':'"赵运磊" <ylzhao@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: 下周二免推生面试，各位老师是否能够参加？',
'sentDate':newdate(2018,8,13,15,32,49),
'receivedDate':newdate(2018,8,13,15,32,53),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<5e81da81.8936.165d1d8c4ef.Coremail.ylzhao@fudan.edu.cn>',
'ref':'<000001d44a93$5b4b81b0$11e28510$@fudan.edu.cn>'}},
{
'addT':'"Min Yang" <m_yang@fudan.edu.cn>',
'add':'Min Yang',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYHBFKp0rq+ngAAm3',
'fid':1,
'size':9308,
'from':'"Min Yang" <m_yang@fudan.edu.cn>',
'to':'"\'cwu\'" <cwu@fudan.edu.cn>',
'subject':'RE: 下周二免推生面试，各位老师是否能够参加？',
'sentDate':newdate(2018,8,13,15,14,46),
'receivedDate':newdate(2018,8,13,15,14,48),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<000001d44b31$73c46b00$5b4d4100$@fudan.edu.cn>',
'ref':'<000001d44a93$5b4b81b0$11e28510$@fudan.edu.cn>'}},
{
'addT':'Hellen@mk.iceeep.org',
'add':'Hellen',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQkGBFKp0rpihAACs9',
'fid':1,
'size':16967,
'from':'Hellen@mk.iceeep.org',
'to':'cwu@fudan.edu.cn',
'subject':'Forthcoming conference in November, 2018--Energy and Environment',
'sentDate':newdate(2018,8,13,8,14,28),
'receivedDate':newdate(2018,8,13,8,20,56),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<01010165d0477315-1431996c-eef9-42ca-8d68-b101bbbacc12-000000@us-west-2.amazonses.com>'}},
{
'addT':'"ZengJianping" <zjp@fudan.edu.cn>',
'add':'ZengJianping',
'icon':{
'm_icon':'REPLIED',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggGBFKpyG8GiQAAsb',
'fid':1,
'size':6548,
'from':'"ZengJianping" <zjp@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: 下周二免推生面试，各位老师是否能够参加？',
'sentDate':newdate(2018,8,12,21,22,18),
'receivedDate':newdate(2018,8,12,21,22,25),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'replied':'true'},
'hmid':'<1b42b9d9.7766.165cdf260cb.Coremail.zjp@fudan.edu.cn>',
'ref':'<000001d44a93$5b4b81b0$11e28510$@fudan.edu.cn>'}},
{
'addT':'"luzhihui" <lzh@fudan.edu.cn>',
'add':'luzhihui',
'icon':{
'm_icon':'REPLIED',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcGBFKp0rogSAABs+',
'fid':1,
'size':9806,
'from':'"luzhihui" <lzh@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: 下周二免推生面试，各位老师是否能够参加？',
'sentDate':newdate(2018,8,12,20,47,53),
'receivedDate':newdate(2018,8,12,20,47,56),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'replied':'true'},
'hmid':'<201809122047444882765@fudan.edu.cn>',
'ref':'<000001d44a93$5b4b81b0$11e28510$@fudan.edu.cn>'}},
{
'addT':'"hbkan" <hbkan@fudan.edu.cn>',
'add':'hbkan',
'icon':{
'm_icon':'REPLIED',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggGBFKpyG79ugAAsS',
'fid':1,
'size':1897,
'from':'"hbkan" <hbkan@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re:下周二免推生面试，各位老师是否能够参加？',
'sentDate':newdate(2018,8,12,20,25,34),
'receivedDate':newdate(2018,8,12,20,41,2),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'replied':'true'},
'hmid':'<4d7b562d.265f9.165cdbe70aa.Coremail.hbkan@fudan.edu.cn>',
'ref':'<000001d44a93$5b4b81b0$11e28510$@fudan.edu.cn>'}},
{
'addT':'"szhang" <szhang@fudan.edu.cn>',
'add':'szhang',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgEGDlKpyG7TRgAAmD',
'fid':1,
'size':32316,
'from':'"szhang" <szhang@fudan.edu.cn>',
'to':'"Wu Jie" <jwu@fudan.edu.cn>, "cwu" <cwu@fudan.edu.cn>, "严明" <myan@fudan.edu.cn>',
'subject':'Fw: Re: RE: Solize　Engineering 公司介绍',
'sentDate':newdate(2018,8,12,17,1,8),
'receivedDate':newdate(2018,8,12,17,1,12),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<314075f9.25b7b.165cd034779.Coremail.szhang@fudan.edu.cn>'}},
{
'addT':'dongling@fudan.edu.cn',
'add':'dongling',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgMGBlKpyG6+5gAAmE',
'fid':1,
'size':424131,
'from':'dongling@fudan.edu.cn',
'to':'xujiayin@fudan.edu.cn, sklge@fudan.edu.cn, wei_xu@fudan.edu.cn, wqlu@fudan.edu.cn, "沈莹" <math_research@fudan.edu.cn>, "王晓娟" <wangxiaojuan@fudan.edu.cn>, "张春艳" <zcy6250@163.com>, "zhaojiayuan" <zhaojiayuan@fudan.edu.cn>, "崔晓丽" <cpslab@fudan.edu.cn>, "李文静" <liwj@fudan.edu.cn>, "上海市现代应用数学重点实验室" <sklcam@fudan.edu>',
'subject':'转发: 关于开展《大学和科研机构开展科学传播活动现状调查》的函',
'sentDate':newdate(2018,8,12,15,31,2),
'receivedDate':newdate(2018,8,12,15,31,7),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<43176e11.25150.165ccb0c761.Coremail.dongling@fudan.edu.cn>'}},
{
'addT':'"wmfu" <wmfu@fudan.edu.cn>',
'add':'wmfu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'HIGH',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgMGDlKpyG67EwAAm8',
'fid':1,
'size':4181,
'from':'"wmfu" <wmfu@fudan.edu.cn>',
'to':'18210240027@fudan.edu.cn, 18210240038@fudan.edu.cn, 18210240123@fudan.edu.cn, 18210240136@fudan.edu.cn, 18210240075@fudan.edu.cn, 18210240173@fudan.edu.cn, 18210240110@fudan.edu.cn, 18210240262@fudan.edu.cn, 18210240237@fudan.edu.cn, 18210240252@fudan.edu.cn, 18210240146@fudan.edu.cn, 18210240082@fudan.edu.cn',
'subject':'兹定于9月19日（周三）上午9时在逸夫楼407室，迎新2018级全体研究生，请课题组老师和2018级全体新生参加！NiSL-Sept-12-2018',
'sentDate':newdate(2018,8,12,15,14,9),
'receivedDate':newdate(2018,8,12,15,14,14),
'priority':1,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<2ae1c403.24f56.165cca154c5.Coremail.wmfu@fudan.edu.cn>',
'ref':'<7fbb2e2b.1ab18.165c158bebf.Coremail.wmfu@fudan.edu.cn>'}},
{
'addT':'"计算机学院" <cs_school@fudan.edu.cn>',
'add':'计算机学院',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQEGCVKp0rm1NwAAmd',
'fid':1,
'size':14064,
'from':'"计算机学院" <cs_school@fudan.edu.cn>',
'to':'"汪 卫" <weiwang1@fudan.edu.cn>, "王 放" <fangwang@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 新" <xinw@fudan.edu.cn>, "王 雪平" <>',
'subject':'【重要通知】关于各项经费执行进度要求的通知',
'sentDate':newdate(2018,8,12,13,37,36),
'receivedDate':newdate(2018,8,12,13,37,42),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<tencent_357E9E54FEAADECCF508962C@qq.com>'}},
{
'addT':'"LJQ" <jsgnljq@163.com>',
'add':'LJQ',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgEGBFKpyG55tAABsQ',
'fid':1,
'size':166061,
'from':'"LJQ" <jsgnljq@163.com>',
'to':'"cwu@fudan.edu.cn" <cwu@fudan.edu.cn>',
'subject':'IP地址跳变机制抗扫描能力评估3',
'sentDate':newdate(2018,8,12,11,48,59),
'receivedDate':newdate(2018,8,12,11,49,1),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true',
'inlineAttached':'true'},
'hmid':'<59690eb7.626e.165cbe57f8f.Coremail.jsgnljq@163.com>'}},
{
'addT':'"赵运磊" <ylzhao@fudan.edu.cn>',
'add':'赵运磊',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgEGBFKpyG55tAAAsR',
'fid':1,
'size':10299,
'from':'"赵运磊" <ylzhao@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: FW: 教学团队设备采购注意事项',
'sentDate':newdate(2018,8,12,10,56,30),
'receivedDate':newdate(2018,8,12,10,56,33),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<6ce1e372.23b71.165cbb56f3b.Coremail.ylzhao@fudan.edu.cn>',
'ref':'<201809111618553468929@fudan.edu.cn><001301d449aa$661f6af0$325e40d0$@fudan.edu.cn>,<001301d449aa$661f6af0$325e40d0$@fudan.edu.cn>'}},
{
'addT':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'add':'cs_keyan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggGB1KpyG54gQAAmv',
'fid':1,
'size':547883,
'from':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'to':'"谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud>',
'subject':'Fw: 【项目申报】科技部关于发布国家重点研发计划“现代服务业共性关键技术研发及应用示范”重点专项2018年度定向项目申报指南的通知',
'sentDate':newdate(2018,8,12,10,51,29),
'receivedDate':newdate(2018,8,12,10,51,30),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<201809121051286177234@fudan.edu.cn>'}},
{
'addT':'"wmfu" <wmfu@fudan.edu.cn>',
'add':'wmfu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggGDlKpyG503QAAm2',
'fid':1,
'size':38454,
'from':'"wmfu" <wmfu@fudan.edu.cn>',
'to':'szhang@fudan.edu.cn, ypzhong@fudan.edu.cn, jwu@fudan.edu.cn, cwu@fudan.edu.cn, gpwang@fudan.edu.cn, jliang@fudan.edu.cn, lzh@fudan.edu.cn, zjp@fudan.edu.cn, jwye@fudan.edu.cn, myan@fudan.edu.cn, wmfu@fudan.edu.cn',
'subject':'通信学会通知：Fw: 转发: Fw:学术年会论文交流安排',
'sentDate':newdate(2018,8,12,10,34,57),
'receivedDate':newdate(2018,8,12,10,35,0),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<456bf288.23935.165cba1b7db.Coremail.wmfu@fudan.edu.cn>'}},
{
'addT':'"Yang Weidong" <yweidong@gmail.com>',
'add':'Yang Weidong',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcGDFKp0rmJ0QAAmE',
'fid':1,
'size':28117,
'from':'"Yang Weidong" <yweidong@gmail.com>',
'to':'"xuxiaoyin" <xuxiaoyin@fudan.edu.cn>',
'subject':'Re: 关于申请新金博研究用房的请示',
'sentDate':newdate(2018,8,12,10,13,17),
'receivedDate':newdate(2018,8,12,10,13,33),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<CAHBYjnuBgcOuV=YrRYvuqHkgdYO2Zc0Fpx=BTZj7NYpRVH-=tA@mail.gmail.com>',
'ref':'<CAHBYjnv3opkycD2dTZxDLjYEd61tDbNoqwfq0__HTEKTuhf7HA@mail.gmail.com><CAHBYjntVjiTzxfGMSRTicogtwya=0ts8JmSxtZ60Ssz4nCqRpg@mail.gmail.com><80E835F1-C79E-4754-A0D7-0E1975C004DE@fudan.edu.cn>,<80E835F1-C79E-4754-A0D7-0E1975C004DE@fudan.edu.cn>'}},
{
'addT':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'add':'cs_keyan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgIGB1KpyG5jyAAAm3',
'fid':1,
'size':21448,
'from':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'to':'"谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud>',
'subject':'Fw: 科技部基础研究中心张峰处长报告通知',
'sentDate':newdate(2018,8,12,9,18,12),
'receivedDate':newdate(2018,8,12,9,18,12),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<201809120918120952351@fudan.edu.cn>'}},
{
'addT':'Alisa@mk.icmeie.com',
'add':'Alisa',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggFBFKpyG5F6wACs6',
'fid':1,
'size':10712,
'from':'Alisa@mk.icmeie.com',
'to':'cwu@fudan.edu.cn',
'subject':'IOP出版+EI&CPCI检索，第二届 机械、电子和工业工程国际学术会议-邀请函- Lu, ZH',
'sentDate':newdate(2018,8,12,5,10,59),
'receivedDate':newdate(2018,8,12,5,11,3),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<01010165ca791ce0-f5e753f3-e8a0-4025-955a-31d3cfc47947-000000@us-west-2.amazonses.com>'}},
{
'addT':'"julie-zhu" <sjtu-julie@sjtu.edu.cn>',
'add':'julie-zhu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQUFBFKp0rlecQAAs6',
'fid':1,
'size':7581,
'from':'"julie-zhu" <sjtu-julie@sjtu.edu.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'上海交大高教院课题组诚邀您参与高校科研人才评价政策认同情况调查',
'sentDate':newdate(2018,8,12,4,49,27),
'receivedDate':newdate(2018,8,12,4,51,47),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<1290745704.2750649.1536698967813.JavaMail.jetty@sc-10_9_111_219-webapi>'}},
{
'addT':'"xuxiaoyin" <xuxiaoyin@fudan.edu.cn>',
'add':'xuxiaoyin',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcFBFKp0rkOegAAmj',
'fid':1,
'size':7256,
'from':'"xuxiaoyin" <xuxiaoyin@fudan.edu.cn>',
'to':'"Yang Weidong" <yweidong@gmail.com>',
'subject':'Re: 关于申请新金博研究用房的请示',
'sentDate':newdate(2018,8,11,18,8,51),
'receivedDate':newdate(2018,8,11,18,8,54),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<80E835F1-C79E-4754-A0D7-0E1975C004DE@fudan.edu.cn>',
'ref':'<CAHBYjnv3opkycD2dTZxDLjYEd61tDbNoqwfq0__HTEKTuhf7HA@mail.gmail.com><CAHBYjntVjiTzxfGMSRTicogtwya=0ts8JmSxtZ60Ssz4nCqRpg@mail.gmail.com>,<CAHBYjntVjiTzxfGMSRTicogtwya=0ts8JmSxtZ60Ssz4nCqRpg@mail.gmail.com>'}},
{
'addT':'"赵运磊" <ylzhao@fudan.edu.cn>',
'add':'赵运磊',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQEFBFKp0rj9rAAAsB',
'fid':1,
'size':10590,
'from':'"赵运磊" <ylzhao@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: FW: 教学团队设备采购注意事项',
'sentDate':newdate(2018,8,11,16,47,34),
'receivedDate':newdate(2018,8,11,16,47,41),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<5abb231d.213c3.165c7d07e01.Coremail.ylzhao@fudan.edu.cn>',
'ref':'<201809111618553468929@fudan.edu.cn><001301d449aa$661f6af0$325e40d0$@fudan.edu.cn>,<001301d449aa$661f6af0$325e40d0$@fudan.edu.cn>'}},
{
'addT':'"晓春肖" <xxiaochun@fudan.edu.cn>',
'add':'晓春肖',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgIFBFKpyG3jWwAAsn',
'fid':1,
'size':12892,
'from':'"晓春肖" <xxiaochun@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: 教学团队设备采购注意事项',
'sentDate':newdate(2018,8,11,16,37,48),
'receivedDate':newdate(2018,8,11,16,37,51),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<CCC51D0A-9D88-4E30-93F6-A4D29A01257F@fudan.edu.cn>',
'ref':'<201809111618553468929@fudan.edu.cn><000e01d449aa$507bb6e0$f17324a0$@fudan.edu.cn>,<000e01d449aa$507bb6e0$f17324a0$@fudan.edu.cn>'}},
{
'addT':'"szhang" <szhang@fudan.edu.cn>',
'add':'szhang',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgFDlKp0rj36QAAmN',
'fid':1,
'size':3921937,
'from':'"szhang" <szhang@fudan.edu.cn>',
'to':'"Wu Jie" <jwu@fudan.edu.cn>, "严明" <myan@fudan.edu.cn>, "cwu" <cwu@fudan.edu.cn>',
'subject':'Fw: Solize　Engineering 公司介绍',
'sentDate':newdate(2018,8,11,16,26,7),
'receivedDate':newdate(2018,8,11,16,26,17),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<d958198.532f.165c7bcdaef.Coremail.szhang@fudan.edu.cn>'}},
{
'addT':'"gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn>',
'add':'gongjie@fudan.edu.cn',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgFCVKp0rj2nQAAm-',
'fid':1,
'size':4046,
'from':'"gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn>',
'to':'"汪卫" <weiwang1@fudan.edu.cn>, "黄萱菁" <xjhuang@fudan.edu.cn>, "张亮" <lzhang@fudan.edu.cn>, "张玥杰" <yjzhang@fudan.edu.cn>, "吴承荣" <cwu@fudan.edu.cn>, "唐志强" <zqtang@fudan.edu.cn>, "张建国" <jgzhang@fudan.edu.cn>, "张向东" <zxd@fudan.edu.cn>',
'subject':'教学团队设备采购注意事项',
'sentDate':newdate(2018,8,11,16,19,55),
'receivedDate':newdate(2018,8,11,16,19,55),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<201809111618553468929@fudan.edu.cn>'}},
{
'addT':'"沈建蓉" <jrshen@fudan.edu.cn>',
'add':'沈建蓉',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggFBlKpyG3I0AAAmP',
'fid':1,
'size':13326,
'from':'"沈建蓉" <jrshen@fudan.edu.cn>',
'to':'"曹袖" <xiucao@fudan.edu.cn>, "陈辰" <chenc@fudan.edu.cn>, "陈荣华" <chenrh@fudan.edu.cn>, "陈伟男" <wnchen@fudan.edu.cn>, "陈学青" <xqchen@fudan.edu.cn>, "陈雁秋" <chenyq@fudan.edu.cn>, "陈阳" <chenyang@fudan.edu.cn>, "陈翌佳" <yijiachen@fudan.edu.cn>, "池明旻" <mmchi@fudan.edu.cn>, "kydai" <kydai@fudan.edu.cn>, "丁向华" <dingx@fudan.>',
'subject':'硕士论文学院预审',
'sentDate':newdate(2018,8,11,14,46,11),
'receivedDate':newdate(2018,8,11,14,45,5),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<2018091114295609349220@fudan.edu.cn>'}},
{
'addT':'"dingsf" <dingsf@fudan.edu.cn>',
'add':'dingsf',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcFAlKp0rjR1gAAmX',
'fid':1,
'size':13793,
'from':'"dingsf" <dingsf@fudan.edu.cn>',
'to':'kydai@fudan.edu.cn, hwfeng@fudan.edu.cn, lijt@fudan.edu.cn, ylzhao@fudan.edu.cn, xuyx@fudan.edu.cn, chenc@fudan.edu.cn, chenrh@fudan.edu.cn, hbkan@fudan.edu.cn, cfsha@fudan.edu.cn, zjp@fudan.edu.cn, wdzhao@fudan.edu.cn, liy@fudan.edu.cn, yunx@fudan.edu.cn, limin@fudan.edu.cn, pengxin@fudan.edu.cn, zhengxq@fudan.ed',
'subject':'关于邀请您参加在职工程硕士论文评审的通知',
'sentDate':newdate(2018,8,11,13,46,38),
'receivedDate':newdate(2018,8,11,13,41,52),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<009001d44992$cf1771a0$6d4654e0$@fudan.edu.cn>'}},
{
'addT':'Ms_wu0521@mk.febm.org',
'add':'Ms_wu0521',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQQFBFKp0riRowACsl',
'fid':1,
'size':8363,
'from':'Ms_wu0521@mk.febm.org',
'to':'cwu@fudan.edu.cn',
'subject':'经管--FEBM2018—内蒙古.呼和浩特',
'sentDate':newdate(2018,8,11,9,58,23),
'receivedDate':newdate(2018,8,11,10,1,53),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<01010165c659e048-920ab1d6-8231-4472-a7cf-203f1821a170-000000@us-west-2.amazonses.com>'}},
{
'addT':'"Frontiers Oncology Editorial Office" <oncology.editorial.office@frontiersin.org>',
'add':'Frontiers Oncology Editorial Office',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggEBFKpyG1QEgABsX',
'fid':1,
'size':5905,
'from':'"Frontiers Oncology Editorial Office" <oncology.editorial.office@frontiersin.org>',
'to':'cwu@fudan.edu.cn',
'subject':'Frontiers: Your manuscript submission - 421127',
'sentDate':newdate(2018,8,10,23,21,30),
'receivedDate':newdate(2018,8,10,23,31,35),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<5B968E3C.00D998.30444@fudan.edu.cn>'}},
{
'addT':'"Online Submissions" <noreply@indersciencemail.com>',
'add':'Online Submissions',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggEBFKpyG1QEgAAsW',
'fid':1,
'size':3264,
'from':'"Online Submissions" <noreply@indersciencemail.com>',
'to':'"Zhanwei Cui" <zwcui14@fudan.edu.cn>, "Jianping Zeng" <zjp@fudan.edu.cn>, "Chengrong Wu" <cwu@fudan.edu.cn>, "Prof. Dr. Eldon Y. Li" <eli@calpoly.edu>',
'subject':'Editorial Review Notification - IJICS_160328',
'sentDate':newdate(2018,8,10,23,18,36),
'receivedDate':newdate(2018,8,10,23,25,22),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<01acee212fe090e61ff11e4f27eaa048@www.inderscience.com>'}},
{
'addT':'Yang@mk.ssphe.org',
'add':'Yang',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYEBFKp0rg7DgAAsj',
'fid':1,
'size':12086,
'from':'Yang@mk.ssphe.org',
'to':'cwu@fudan.edu.cn',
'subject':'Conference on Social Science, Education and Humanities Research-三亚-11.25-27',
'sentDate':newdate(2018,8,10,19,20,53),
'receivedDate':newdate(2018,8,10,19,20,58),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<01010165c3367ecc-b6a75300-5ec3-4053-8513-0055ccff3821-000000@us-west-2.amazonses.com>'}},
{
'addT':'"夏毅" <18210240217@fudan.edu.cn>',
'add':'夏毅',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgUEBFKpyGz+0QABs2',
'fid':1,
'size':2457,
'from':'"夏毅" <18210240217@fudan.edu.cn>',
'to':'"吴承荣老师" <cwu@fudan.edu.cn>',
'subject':'新生工作会议安排确认',
'sentDate':newdate(2018,8,10,16,46,24),
'receivedDate':newdate(2018,8,10,16,46,34),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true'},
'hmid':'<56cf7092.1cd3a.165c2a911f5.Coremail.18210240217@fudan.edu.cn>'}},
{
'addT':'"jsgnljq" <jsgnljq@163.com>',
'add':'jsgnljq',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggEBFKpyGza9wACs6',
'fid':1,
'size':8156,
'from':'"jsgnljq" <jsgnljq@163.com>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'回复：RE: 本周三研究生工作安排会议',
'sentDate':newdate(2018,8,10,15,15,46),
'receivedDate':newdate(2018,8,10,15,15,49),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true'},
'hmid':'<tencent_A9482048257D984C67B5D18B@qq.com>',
'ref':'<001301d448b9$78977b10$69c67130$@fudan.edu.cn>'}},
{
'addT':'"Zhou, Huijing (WorldQuant)" <Huijing.Zhou@worldquant.com>',
'add':'Zhou, Huijing (WorldQuant)',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgUEBFKpyGz+0QAAs3',
'fid':1,
'size':62616,
'from':'"Zhou, Huijing (WorldQuant)" <Huijing.Zhou@worldquant.com>',
'to':'"\'cwu@fudan.edu.cn\'" <cwu@fudan.edu.cn>',
'subject':'WorldQuant 世坤咨询（北京）有限公司 2018-2019年度秋季招聘',
'sentDate':newdate(2018,8,10,15,3,20),
'receivedDate':newdate(2018,8,10,15,49,38),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'inlineAttached':'true'},
'hmid':'<B9F8D5E98F95D6429642DDE76E403B85A370B7@PWSSIDEXMBX002.AD.MLP.com>'}},
{
'addT':'"陈蕾" <chenlei@hzbook.com>',
'add':'陈蕾',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggEBFKpyGza9wABs5',
'fid':1,
'size':579332,
'from':'"陈蕾" <chenlei@hzbook.com>',
'to':'Cwu@fudan.edu.cn',
'subject':'教师节快乐—机械工业出版社华章分社陈蕾',
'sentDate':newdate(2018,8,10,11,8,24),
'receivedDate':newdate(2018,8,10,13,8,28),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'inlineAttached':'true'},
'hmid':'<49f8948c.6840.165c173a048.Coremail.chenlei@hzbook.com>'}},
{
'addT':'"wmfu" <wmfu@fudan.edu.cn>',
'add':'wmfu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'HIGH',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggECFKpyGy-UwAAm1',
'fid':1,
'size':51335,
'from':'"wmfu" <wmfu@fudan.edu.cn>',
'to':'18210240027@fudan.edu.cn, 18210240038@fudan.edu.cn, 18210240123@fudan.edu.cn, 18210240136@fudan.edu.cn, 18210240075@fudan.edu.cn, 18210240173@fudan.edu.cn, 18210240110@fudan.edu.cn, 18210240262@fudan.edu.cn, 18210240237@fudan.edu.cn, 18210240252@fudan.edu.cn, 18210240146@fudan.edu.cn, 18210240082@fudan.edu.cn',
'subject':'转发讲座通知： 明天11(日）上午9点40分讲座（详见邮件网址）在逸夫楼407， 望大家准时参加！祝新学期快乐、进步！NiSL-傅维明',
'sentDate':newdate(2018,8,10,10,39,3),
'receivedDate':newdate(2018,8,10,10,39,14),
'priority':1,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<7fbb2e2b.1ab18.165c158bebf.Coremail.wmfu@fudan.edu.cn>',
'ref':'<36cdb4bb.13b9c.165b1c5a691.Coremail.wmfu@fudan.edu.cn>'}},
{
'addT':'"余莉萍" <17210240022@fudan.edu.cn>',
'add':'余莉萍',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQIEBFKp0rfEDAAAsV',
'fid':1,
'size':5416,
'from':'"余莉萍" <17210240022@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re:RE: RE: RE: 来自下学期《信息安全导论》课程助教',
'sentDate':newdate(2018,8,10,10,11,34),
'receivedDate':newdate(2018,8,10,10,11,44),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<10fef239.1a7fb.165c13f9793.Coremail.17210240022@fudan.edu.cn>',
'ref':'<000601d448a1$543b3d50$fcb1b7f0$@fudan.edu.cn>'}},
{
'addT':'"jsgnljq" <jsgnljq@163.com>',
'add':'jsgnljq',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgQDBFKpyGyWdgABs-',
'fid':1,
'size':3021,
'from':'"jsgnljq" <jsgnljq@163.com>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'祝吴老师教师节快乐',
'sentDate':newdate(2018,8,10,8,33,6),
'receivedDate':newdate(2018,8,10,8,33,11),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<tencent_E759448C5C43305C00094FA7@qq.com>'}},
{
'addT':'"FDU Security" <security@fudan.edu.cn>',
'add':'FDU Security',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYJCVKp0rdA6gAAbz',
'fid':1,
'size':80520,
'from':'"FDU Security" <security@fudan.edu.cn>',
'to':'security@fudan.edu.cn',
'subject':'恶意邮件警报：电子邮件包含“Unable to/Cannot show/display this message”消息',
'sentDate':newdate(2018,8,9,14,45,23),
'receivedDate':newdate(2018,8,9,17,56,42),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<419aee3b.1884e.165bd13ea55.Coremail.security@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"余莉萍" <17210240022@fudan.edu.cn>',
'add':'余莉萍',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgEDBFKpyGwyjgAAsn',
'fid':1,
'size':19664,
'from':'"余莉萍" <17210240022@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: RE: RE: 来自下学期《信息安全导论》课程助教',
'sentDate':newdate(2018,8,9,13,29,58),
'receivedDate':newdate(2018,8,9,13,30,1),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<74ebc0f6.18654.165bccedd68.Coremail.17210240022@fudan.edu.cn>',
'ref':'<60dc4a35.569ea.164783e1ac9.Coremail.17210240022@fudan.edu.cn><000901d41756$f3f65360$dbe2fa20$@fudan.edu.cn><76459c99.95e1.165a257e94d.Coremail.17210240022@fudan.edu.cn><000c01d444ba$54e64550$feb2cff0$@fudan.edu.cn>,<000c01d444ba$54e64550$feb2cff0$@fudan.edu.cn>',
'rootid':'1tbiAggSBFKpyGh6FQAAso'}},
{
'addT':'"wanghuimin" <wanghm@fudan.edu.cn>',
'add':'wanghuimin',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgIDDFKpyGwn-AAAmL',
'fid':1,
'size':1669,
'from':'"wanghuimin" <wanghm@fudan.edu.cn>',
'to':'"许晓茵" <xuxiaoyin@fudan.edu.cn>, "王晓阳" <xywangcs@fudan.edu.cn>, "薛向阳" <xyxue@fudan.edu.cn>, "吴杰" <jwu@fudan.edu.cn>, "吴承荣" <cwu@fudan.edu.cn>, "张世永" <szhang@fudan.edu.cn>, "叶家炜" <jwye@fudan.edu.cn>',
'subject':'保密学院班子会通知',
'sentDate':newdate(2018,8,9,12,26,58),
'receivedDate':newdate(2018,8,9,12,27,2),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true'},
'hmid':'<52fe8387.184fb.165bc9531f8.Coremail.wanghm@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"孙玉齐" <16300240013@fudan.edu.cn>',
'add':'孙玉齐',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgcDBFKpyGv88AADsV',
'fid':1,
'size':3337,
'from':'"孙玉齐" <16300240013@fudan.edu.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'Re: 来自"孙玉齐" <16300240013@fudan.edu.cn>的邮件',
'sentDate':newdate(2018,8,9,10,36,37),
'receivedDate':newdate(2018,8,9,10,39,31),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true'},
'hmid':'<43465f6f-160c-0394-9b4a-234c923a07e0@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"jwye@fudan.edu.cn" <jwye@fudan.edu.cn>',
'add':'jwye@fudan.edu.cn',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgcDBFKpyGv88AABsX',
'fid':1,
'size':3516462,
'from':'"jwye@fudan.edu.cn" <jwye@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'云审计截图',
'sentDate':newdate(2018,8,9,10,8,52),
'receivedDate':newdate(2018,8,9,10,8,53),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'attached':'true'},
'hmid':'<201809091008518213441@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"郝建伟" <hjw_cmpbook@126.com>',
'add':'郝建伟',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQMCBFKp0rbmUQACsu',
'fid':1,
'size':9942,
'from':'"郝建伟" <hjw_cmpbook@126.com>',
'to':'cwu@fudan.edu.cn',
'subject':'祝您教师节快乐！-机械工业出版社郝建伟 ',
'sentDate':newdate(2018,8,9,9,0,0),
'receivedDate':newdate(2018,8,9,9,2,6),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<149ab1d3.2c41.165b1da251e.Coremail.hjw_cmpbook@126.com>',
'rootid':''}},
{
'addT':'"linda jane" <antomes1758@gmail.com>',
'add':'linda jane',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgECBFKpyGu-2AABs7',
'fid':1,
'size':13999986,
'from':'"linda jane" <antomes1758@gmail.com>',
'to':'',
'subject':'Fwd: 主题：2018年9月7日星期五 ……【周末快乐！】',
'sentDate':newdate(2018,8,9,0,41,57),
'receivedDate':newdate(2018,8,9,1,15,34),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<CACKqrNWg0LuNCY2ftao_X-DoJcLqp4Hts3eBvxKzuLoFTTz9Fg@mail.gmail.com>',
'ref':'<728998e3.1595.165b9c6e3f2.Coremail.mnb201010@163.com>',
'rootid':''}},
{
'addT':'"ResearchGate" <no-reply@researchgatemail.net>',
'add':'ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQUCBFKp0raqvwAAsI',
'fid':1,
'size':19958,
'from':'"ResearchGate" <no-reply@researchgatemail.net>',
'to':'cwu@fudan.edu.cn',
'subject':'A researcher is following your updates on ResearchGate',
'sentDate':newdate(2018,8,8,15,53,39),
'receivedDate':newdate(2018,8,8,16,1,47),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<20180908075339.115918000159@mr70.researchgate.net>',
'rootid':''}},
{
'addT':'"Yang Weidong" <yweidong@gmail.com>',
'add':'Yang Weidong',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYCBFKp0ralfAAAmH',
'fid':1,
'size':39035,
'from':'"Yang Weidong" <yweidong@gmail.com>',
'to':'"薛 向阳" <xyxue@fudan.edu.cn>, "王晓阳X. Sean Wang" <xywangCS@fudan.edu.cn>, "吴 承荣" <cwu@fudan.edu.cn>, "xuxiaoyin" <xuxiaoyin@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>',
'subject':'Re: 关于申请新金博研究用房的请示',
'sentDate':newdate(2018,8,8,15,10,14),
'receivedDate':newdate(2018,8,8,15,10,29),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'attached':'true'},
'hmid':'<CAHBYjntVjiTzxfGMSRTicogtwya=0ts8JmSxtZ60Ssz4nCqRpg@mail.gmail.com>',
'ref':'<CAHBYjnv3opkycD2dTZxDLjYEd61tDbNoqwfq0__HTEKTuhf7HA@mail.gmail.com>',
'rootid':'1tbiAQYBBFKp0rZRuwAAm3'}},
{
'addT':'"Yang Weidong" <yweidong@gmail.com>',
'add':'Yang Weidong',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgCBFKp0raitgAAsE',
'fid':1,
'size':11084,
'from':'"Yang Weidong" <yweidong@gmail.com>',
'to':'"吴 承荣" <cwu@fudan.edu.cn>',
'subject':'Re: 关于申请新金博研究用房的请示',
'sentDate':newdate(2018,8,8,14,47,41),
'receivedDate':newdate(2018,8,8,14,47,55),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<CAHBYjntE5wabFit0jKwoDPJFayQG_mZhpqjR0UhHV9+FXwHQfA@mail.gmail.com>',
'ref':'<CAHBYjnv3opkycD2dTZxDLjYEd61tDbNoqwfq0__HTEKTuhf7HA@mail.gmail.com><001501d44735$3f316eb0$bd944c10$@fudan.edu.cn>,<001501d44735$3f316eb0$bd944c10$@fudan.edu.cn>',
'rootid':'1tbiAQYBBFKp0rZRuwAAm3'}},
{
'addT':'"何加林" <czhejialin@163.com>',
'add':'何加林',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYCDlKp0raLfwAAmg',
'fid':1,
'size':1638088,
'from':'"何加林" <czhejialin@163.com>',
'to':'caoyu@fudan.edu.cn, xiucao@fudan.edu.cn, mmchi@fudan.edu.cn, wnchen@fudan.edu.cn, chenlf@fudan.edu.cn, xqchen@fudan.edu.cn, tbchen@fudan.edu.cn, bhchen@fudan.edu.cn, yijiachen@fudan.edu.cn, chenrh@fudan.edu.cn, chenc@fudan.edu.cn, chenyq@fudan.edu.cn, dingx@fudan.edu.cn, dingsf@fudan.edu.cn, kydai@fudan.edu.cn, fu',
'subject':'《电与磁的理论缺陷》',
'sentDate':newdate(2018,8,8,9,39,32),
'receivedDate':newdate(2018,8,8,10,26,32),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true',
'inlineAttached':'true'},
'hmid':'<2f782420.269f.165b6d58aaf.Coremail.czhejialin@163.com>',
'rootid':''}},
{
'addT':'iwmsme2018@mail.iwmsme.org',
'add':'iwmsme2018',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQUBBFKp0rZZ+wABs9',
'fid':1,
'size':69935,
'from':'iwmsme2018@mail.iwmsme.org',
'to':'cwu@fudan.edu.cn',
'subject':'Good papers are welcome to submit to IWMSME2018 and published by IOP conference series',
'sentDate':newdate(2018,8,8,4,17,39),
'receivedDate':newdate(2018,8,8,4,24,39),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<01010165b5aed899-1edfc4c5-0581-4a5c-84f6-1e47ae45e768-000000@us-west-2.amazonses.com>',
'rootid':''}},
{
'addT':'"Yang Weidong" <yweidong@gmail.com>',
'add':'Yang Weidong',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYBBFKp0rZRuwAAm3',
'fid':1,
'size':37321,
'from':'"Yang Weidong" <yweidong@gmail.com>',
'to':'"薛 向阳" <xyxue@fudan.edu.cn>, "王晓阳X. Sean Wang" <xywangCS@fudan.edu.cn>, "吴 承荣" <cwu@fudan.edu.cn>, "xuxiaoyin" <xuxiaoyin@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>',
'subject':'关于申请新金博研究用房的请示',
'sentDate':newdate(2018,8,7,22,42,6),
'receivedDate':newdate(2018,8,7,22,42,31),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<CAHBYjnv3opkycD2dTZxDLjYEd61tDbNoqwfq0__HTEKTuhf7HA@mail.gmail.com>',
'rootid':''}},
{
'addT':'"匡翔宇" <xykuang16@fudan.edu.cn>',
'add':'匡翔宇',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQQBBFKp0rYHhQAAsd',
'fid':1,
'size':7361,
'from':'"匡翔宇" <xykuang16@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: RE: 匡翔宇的论文初稿 烦请吴老师审阅',
'sentDate':newdate(2018,8,7,15,6,45),
'receivedDate':newdate(2018,8,7,15,6,46),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<2ac52385.15049.165b2dac02d.Coremail.xykuang16@fudan.edu.cn>',
'ref':'<4f31f46f.13056.165af6bdf32.Coremail.xykuang16@fudan.edu.cn><003e01d44675$b547da50$1fd78ef0$@fudan.edu.cn>,<003e01d44675$b547da50$1fd78ef0$@fudan.edu.cn>',
'rootid':'1tbiAgQABFKpyGpmTwABsz'}},
{
'addT':'"宋昊" <16210240081@fudan.edu.cn>',
'add':'宋昊',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgEBBFKpyGr3UQABs4',
'fid':1,
'size':15907882,
'from':'"宋昊" <16210240081@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: RE: 论文 (0904)',
'sentDate':newdate(2018,8,7,14,23,22),
'receivedDate':newdate(2018,8,7,14,23,25),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<7e3ce1c7.14c8c.165b2b30aba.Coremail.16210240081@fudan.edu.cn>',
'ref':'<1b06cfff.97b5.165a26d47c3.Coremail.16210240081@fudan.edu.cn><002d01d444cb$ea631980$bf294c80$@fudan.edu.cn>,<002d01d444cb$ea631980$bf294c80$@fudan.edu.cn>',
'rootid':'1tbiAgYSBFKpyGh+iwAAs8'}},
{
'addT':'"luzhihui" <lzh@fudan.edu.cn>',
'add':'luzhihui',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgEBBFKpyGr3UQAAs5',
'fid':1,
'size':1670521,
'from':'"luzhihui" <lzh@fudan.edu.cn>',
'to':'"吴承荣" <cwu@fudan.edu.cn>',
'subject':'沙箱简介',
'sentDate':newdate(2018,8,7,14,9,41),
'receivedDate':newdate(2018,8,7,14,9,45),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<201809071409414433833@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"wmfu" <wmfu@fudan.edu.cn>',
'add':'wmfu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYBCFKp0rXulQAAmp',
'fid':1,
'size':2751,
'from':'"wmfu" <wmfu@fudan.edu.cn>',
'to':'"Gao Qiyuan" <GQQQy@outlook.com>',
'subject':'Re: Fw:【研究生推免】',
'sentDate':newdate(2018,8,7,13,16,30),
'receivedDate':newdate(2018,8,7,13,16,31),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<77f1060e.147c2.165b275cff1.Coremail.wmfu@fudan.edu.cn>',
'ref':'<37b599b1.13086.165af738288.Coremail.cwu@fudan.edu.cn>',
'rootid':'1tbiAgcABFKpyGogWgAEsm'}},
{
'addT':'"计算机学院工会" <cs_gonghui@fudan.edu.cn>',
'add':'计算机学院工会',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgcBDlKpyGrdeQAAm3',
'fid':1,
'size':6889,
'from':'"计算机学院工会" <cs_gonghui@fudan.edu.cn>',
'to':'"汪 卫" <weiwang1@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 雪平" <wangxp@fudan.edu.cn>, "王 毅敏" <yiminwang@fudan.edu.cn>, "王"',
'subject':'教师着装礼仪及基础搭配讲座通知',
'sentDate':newdate(2018,8,7,12,5,28),
'receivedDate':newdate(2018,8,7,12,5,30),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<405222f7.144a6.165b234c955.Coremail.cs_gonghui@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"上海市科学技术委员会" <infomail@newsletter.stcsm.gov.cn>',
'add':'上海市科学技术委员会',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYBBFKp0rXMHQABsO',
'fid':1,
'size':35013,
'from':'"上海市科学技术委员会" <infomail@newsletter.stcsm.gov.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'科技服务信息专递第四百五十二期',
'sentDate':newdate(2018,8,7,11,33,33),
'receivedDate':newdate(2018,8,7,11,39,11),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<20180907033334.EAA8C7437AD@mx130.sx67.email-deliver.com>',
'rootid':''}},
{
'addT':'"携程旅行网" <recommend@lists4.ctrip.com>',
'add':'携程旅行网',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQMBBFKp0rXJXAAAsO',
'fid':1,
'size':29980,
'from':'"携程旅行网" <recommend@lists4.ctrip.com>',
'to':'cwu@fudan.edu.cn',
'subject':'恭喜您获赠1950元国家周超值大礼包！更有五折神券限时抢',
'sentDate':newdate(2018,8,7,10,50,21),
'receivedDate':newdate(2018,8,7,10,56,9),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<20180907025021.3AFD21A211C@mx5.ey1info.ctrip.com>',
'rootid':''}},
{
'addT':'"ResearchGate" <no-reply@researchgatemail.net>',
'add':'ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggBBFKpyGqwQgACsm',
'fid':1,
'size':20839,
'from':'"ResearchGate" <no-reply@researchgatemail.net>',
'to':'"Chengrong Wu" <cwu@fudan.edu.cn>',
'subject':'Chengrong, you have 1 more citation',
'sentDate':newdate(2018,8,7,9,40,36),
'receivedDate':newdate(2018,8,7,9,46,31),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<20180907014036.3E95C2005D276@mr87.researchgate.net>',
'rootid':''}},
{
'addT':'"匡翔宇" <xykuang16@fudan.edu.cn>',
'add':'匡翔宇',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgQABFKpyGpmTwABsz',
'fid':1,
'size':2266437,
'from':'"匡翔宇" <xykuang16@fudan.edu.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'匡翔宇的论文初稿 烦请吴老师审阅',
'sentDate':newdate(2018,8,6,23,6,46),
'receivedDate':newdate(2018,8,6,23,6,49),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'attached':'true'},
'hmid':'<4f31f46f.13056.165af6bdf32.Coremail.xykuang16@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"higo@FDU" <lijiading@fudan.edu.cn>',
'add':'higo@FDU',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgQABFKpyGpmTwAAsy',
'fid':1,
'size':12882,
'from':'"higo@FDU" <lijiading@fudan.edu.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'学院2018年迎新大会邀请函',
'sentDate':newdate(2018,8,6,21,36,36),
'receivedDate':newdate(2018,8,6,21,36,38),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<C4AB49CA-8FD9-41AC-B0D5-C9D77D8A14CE@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"ResearchGate" <no-reply@researchgatemail.net>',
'add':'ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQMABFKp0rVl8gAAsN',
'fid':1,
'size':21907,
'from':'"ResearchGate" <no-reply@researchgatemail.net>',
'to':'cwu@fudan.edu.cn',
'subject':'Amir Herzberg, an author you cited, uploaded a full-text to: Introduction to Cyber-Security, Part I: Applied Cryptography...',
'sentDate':newdate(2018,8,6,21,13,36),
'receivedDate':newdate(2018,8,6,21,21,25),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<20180906131336.C81FA91CE@mr109.researchgate.net>',
'rootid':''}},
{
'addT':'"Gao Qiyuan" <GQQQy@outlook.com>',
'add':'Gao Qiyuan',
'icon':{
'm_icon':'FORWARDED',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgcABFKpyGogWgAEsm',
'fid':1,
'size':356111,
'from':'"Gao Qiyuan" <GQQQy@outlook.com>',
'to':'"cwu@fudan.edu.cn" <cwu@fudan.edu.cn>',
'subject':'【研究生推免】',
'sentDate':newdate(2018,8,6,18,53,34),
'receivedDate':newdate(2018,8,6,18,53,41),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'attached':'true',
'forwarded':'true'},
'hmid':'<BY1PR0701MB1224D68E705A15DACA85A57DB3010@BY1PR0701MB1224.namprd07.prod.outlook.com>',
'rootid':''}},
{
'addT':'"CCF会员部" <membership@ccf.org.cn>',
'add':'CCF会员部',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgcABFKpyGogWgABsj',
'fid':1,
'size':27698,
'from':'"CCF会员部" <membership@ccf.org.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'温馨提醒：第7、8期《中国计算机学会通讯》已于8月28日陆续寄出',
'sentDate':newdate(2018,8,6,15,3,33),
'receivedDate':newdate(2018,8,6,15,17,23),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<00950b6196ae$b32ce816$be97cba0$@lu>',
'rootid':''}},
{
'addT':'"LJQ" <jsgnljq@163.com>',
'add':'LJQ',
'icon':{
'm_icon':'REPLIED',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgkABFKpyGn4tAAAsZ',
'fid':1,
'size':173111,
'from':'"LJQ" <jsgnljq@163.com>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re:RE: Re:回复：RE: 关于地址跳变机制抗扫描能力的评估论文需要9月10日投出',
'sentDate':newdate(2018,8,6,11,4,28),
'receivedDate':newdate(2018,8,6,11,4,30),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'attached':'true',
'replied':'true',
'inlineAttached':'true'},
'hmid':'<35744a51.563e.165acd69344.Coremail.jsgnljq@163.com>',
'ref':'000001d4433c$b9052d50$2b0f87f0$@fudan.edu.cn<000001d4433c$b9052d50$2b0f87f0$@fudan.edu.cn><tencent_8A15F3C9259FC4B12D9F474F@qq.com><79f6b5b1.3a60.1659f2d97a7.Coremail.cwu@fudan.edu.cn><6796230f.8d07.165a86b3f14.Coremail.jsgnljq@163.com><000601d444e2$b0fc9d30$12f5d790$@fudan.edu.cn>',
'rootid':'1tbiAQYHAFKp0q2dpwAAm+'}},
{
'addT':'"计算机学院" <cs_school@fudan.edu.cn>',
'add':'计算机学院',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgcACVKpyGnx-gAAmZ',
'fid':1,
'size':10493,
'from':'"计算机学院" <cs_school@fudan.edu.cn>',
'to':'"汪 卫" <weiwang1@fudan.edu.cn>, "王 放" <fangwang@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 新" <xinw@fudan.edu.cn>, "王 雪平" <>',
'subject':'学院迎新大会',
'sentDate':newdate(2018,8,6,10,31,3),
'receivedDate':newdate(2018,8,6,10,31,5),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true'},
'hmid':'<tencent_3AC59E4EF72C835405A3B2FF@qq.com>',
'rootid':''}},
{
'addT':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'add':'cs_keyan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgcAB1KpyGnoIQAAmR',
'fid':1,
'size':202985,
'from':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'to':'"谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud>',
'subject':'转发: 关于转发8月若干国家自然科学基金委项目指南的通知',
'sentDate':newdate(2018,8,6,9,45,9),
'receivedDate':newdate(2018,8,6,9,45,8),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<201809060945095250338@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'add':'cs_keyan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgAB1Kp0rTmXwAAmq',
'fid':1,
'size':217482,
'from':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'to':'"谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud>',
'subject':'Fw: 【指南征求意见】关于对科技创新2030—“新一代人工智能”重大项目 2018年度项目申报指南征求意见的通知',
'sentDate':newdate(2018,8,6,9,27,39),
'receivedDate':newdate(2018,8,6,9,27,37),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<201809060927395577516@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"Zhang Shiyong via ResearchGate" <no-reply@researchgatemail.net>',
'add':'Zhang Shiyong via ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgITBFKpyGm77gAAsY',
'fid':1,
'size':21088,
'from':'"Zhang Shiyong via ResearchGate" <no-reply@researchgatemail.net>',
'to':'cwu@fudan.edu.cn',
'subject':'Zhang Shiyong thinks you\'re the author of this publication',
'sentDate':newdate(2018,8,6,1,4,47),
'receivedDate':newdate(2018,8,6,1,11,33),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'report':'true'},
'hmid':'<20180905170447.51CAC100004B1@mr58.researchgate.net>',
'rootid':''}},
{
'addT':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'add':'cs_keyan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgUTB1KpyGljTwAAml',
'fid':1,
'size':8185,
'from':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'to':'"谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud>',
'subject':'关于第一届 “先进计算与防御技术” 学术会议',
'sentDate':newdate(2018,8,5,14,29,37),
'receivedDate':newdate(2018,8,5,14,29,37),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<2018090514293740411015@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"LJQ" <jsgnljq@163.com>',
'add':'LJQ',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgQTBFKpyGlV0wABsM',
'fid':1,
'size':2526091,
'from':'"LJQ" <jsgnljq@163.com>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re:Re:回复：RE: 关于地址跳变机制抗扫描能力的评估论文需要9月10日投出',
'sentDate':newdate(2018,8,5,14,28,45),
'receivedDate':newdate(2018,8,5,14,28,48),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<6796230f.8d07.165a86b3f14.Coremail.jsgnljq@163.com>',
'ref':'000001d4433c$b9052d50$2b0f87f0$@fudan.edu.cn<000001d4433c$b9052d50$2b0f87f0$@fudan.edu.cn><tencent_8A15F3C9259FC4B12D9F474F@qq.com><79f6b5b1.3a60.1659f2d97a7.Coremail.cwu@fudan.edu.cn>,<79f6b5b1.3a60.1659f2d97a7.Coremail.cwu@fudan.edu.cn>',
'rootid':'1tbiAQYHAFKp0q2dpwAAm+'}},
{
'addT':'"cgjh" <cgjh@fudan.edu.cn>',
'add':'cgjh',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggTBFKpyGk5nAABsj',
'fid':1,
'size':145275,
'from':'"cgjh" <cgjh@fudan.edu.cn>',
'to':'"吴承荣" <cwu@fudan.edu.cn>',
'subject':'关于国家公派留学成果统计的通知',
'sentDate':newdate(2018,8,5,10,59,0),
'receivedDate':newdate(2018,8,5,10,59,10),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<7360e7e6.d15c.165a7ab3645.Coremail.cgjh@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn>',
'add':'gongjie@fudan.edu.cn',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggTBFKpyGk5nAAAsi',
'fid':1,
'size':273964,
'from':'"gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'回复: RE: 本科上课通知',
'sentDate':newdate(2018,8,5,10,12,56),
'receivedDate':newdate(2018,8,5,10,12,55),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<201809051011559369355@fudan.edu.cn>',
'ref':'<2018083014405724018688@fudan.edu.cn>,<001101d444bc$f99c2f90$ecd48eb0$@fudan.edu.cn>',
'rootid':'1tbiAgMNBFKpyGWGFQACsP'}},
{
'addT':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'add':'cs_keyan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgkTB1KpyGk3CwAAm5',
'fid':1,
'size':52151,
'from':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'to':'"谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud>',
'subject':'Fw: 【紧急】各院系教师在国际机构及期刊任职情况汇总',
'sentDate':newdate(2018,8,5,10,1,42),
'receivedDate':newdate(2018,8,5,10,1,42),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<201809051001422469263@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"朱迅" <17210240029@fudan.edu.cn>',
'add':'朱迅',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQUTBFKp0rQ3fAAAsF',
'fid':1,
'size':17315,
'from':'"朱迅" <17210240029@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: RE: RE: 关于18-19学年《网络攻击与防御技术》课程助教的工作',
'sentDate':newdate(2018,8,5,10,1,0),
'receivedDate':newdate(2018,8,5,10,1,2),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<13f63450.cbed.165a7761cd0.Coremail.17210240029@fudan.edu.cn>',
'ref':'<2cf64a1a.564a0.164754644cd.Coremail.17210240029@fudan.edu.cn><000301d41756$4351d610$c9f58230$@fudan.edu.cn><1aa0fd1e.97ac.165a26cfe4a.Coremail.17210240029@fudan.edu.cn><001401d44424$b0f7faa0$12e7efe0$@fudan.edu.cn>,<001401d44424$b0f7faa0$12e7efe0$@fudan.edu.cn>',
'rootid':'1tbiAQgSBFKp0rN+twAAsM'}},
{
'addT':'"wanghuimin" <wanghm@fudan.edu.cn>',
'add':'wanghuimin',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQETE1Kp0rQ3HQAAm3',
'fid':1,
'size':51544,
'from':'"wanghuimin" <wanghm@fudan.edu.cn>',
'to':'"吴承荣" <cwu@fudan.edu.cn>',
'subject':'Fw: 多媒体设备拆迁费用清单',
'sentDate':newdate(2018,8,5,9,59,18),
'receivedDate':newdate(2018,8,5,9,59,20),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<7e6142b8.cbca.165a7748fc1.Coremail.wanghm@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"余莉萍" <17210240022@fudan.edu.cn>',
'add':'余莉萍',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgITBFKpyGkuSwABsp',
'fid':1,
'size':18731,
'from':'"余莉萍" <17210240022@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: RE: RE: 来自下学期《信息安全导论》课程助教',
'sentDate':newdate(2018,8,5,9,49,9),
'receivedDate':newdate(2018,8,5,9,49,11),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<3b5b758f.cae0.165a76b459a.Coremail.17210240022@fudan.edu.cn>',
'ref':'<60dc4a35.569ea.164783e1ac9.Coremail.17210240022@fudan.edu.cn><000901d41756$f3f65360$dbe2fa20$@fudan.edu.cn><76459c99.95e1.165a257e94d.Coremail.17210240022@fudan.edu.cn><000c01d444ba$54e64550$feb2cff0$@fudan.edu.cn>,<000c01d444ba$54e64550$feb2cff0$@fudan.edu.cn>',
'rootid':'1tbiAggSBFKpyGh6FQAAso'}},
{
'addT':'"meiyi ma" <mm5tk@virginia.edu>',
'add':'meiyi ma',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgSBFKp0rQWgQACsX',
'fid':1,
'size':48508,
'from':'"meiyi ma" <mm5tk@virginia.edu>',
'to':'cwu@fudan.edu.cn',
'subject':'Invitation to submit your work to 2018 Safethings',
'sentDate':newdate(2018,8,5,6,22,36),
'receivedDate':newdate(2018,8,5,6,29,9),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<CAPQohmCSJbYVR3qwA=52GdTDg9joPSdc9q--Rd=HnKi-WR25pQ@mail.gmail.com>',
'rootid':''}},
{
'addT':'"ResearchGate" <no-reply@researchgatemail.net>',
'add':'ResearchGate',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgSBFKp0rQIiwAAsB',
'fid':1,
'size':56334,
'from':'"ResearchGate" <no-reply@researchgatemail.net>',
'to':'"Chengrong Wu" <cwu@fudan.edu.cn>',
'subject':'Chengrong, we found new jobs you may be interested in',
'sentDate':newdate(2018,8,5,1,7,33),
'receivedDate':newdate(2018,8,5,1,16,28),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'report':'true'},
'hmid':'<20180904170733.CDD1510001062@mr62.researchgate.net>',
'rootid':''}},
{
'addT':'"赵瑜" <15307130435@fudan.edu.cn>',
'add':'赵瑜',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQESBFKp0rPHfAAAs3',
'fid':1,
'size':10453,
'from':'"赵瑜" <15307130435@fudan.edu.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'Re:RE: 关于推免生专业和方向的疑问',
'sentDate':newdate(2018,8,4,17,9,27),
'receivedDate':newdate(2018,8,4,17,9,29),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<d8j9bd2lieauoob6ia2t5s13.1536052167394@email.android.com>',
'ref':'<000f01d44424$8dc69460$a953bd20$@fudan.edu.cn>',
'rootid':'1tbiAggQBFKpyGdrFwAAs2'}},
{
'addT':'"ZengJianping" <zjp@fudan.edu.cn>',
'add':'ZengJianping',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQkSBFKp0rO85AAAsc',
'fid':1,
'size':3575,
'from':'"ZengJianping" <zjp@fudan.edu.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'拟态项目下半年工作总结',
'sentDate':newdate(2018,8,4,16,21,18),
'receivedDate':newdate(2018,8,4,16,21,20),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<3b2b0b50.aff2.165a3abeeac.Coremail.zjp@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"计算机学院工会" <cs_gonghui@fudan.edu.cn>',
'add':'计算机学院工会',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYSDlKp0rOw9QAAmE',
'fid':1,
'size':775758,
'from':'"计算机学院工会" <cs_gonghui@fudan.edu.cn>',
'to':'"汪 卫" <weiwang1@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 雪平" <wangxp@fudan.edu.cn>, "王 毅敏" <yiminwang@fudan.edu.cn>, "王"',
'subject':'上海市教育工会提供义务法律咨询 及 中国农业银行致敬教师校园行活动 的通知',
'sentDate':newdate(2018,8,4,15,26,5),
'receivedDate':newdate(2018,8,4,15,26,8),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<3fc7156.aac9.165a3795f16.Coremail.cs_gonghui@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"wmfu" <wmfu@fudan.edu.cn>',
'add':'wmfu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'HIGH',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggSDlKpyGiQvwAAmi',
'fid':1,
'size':32457,
'from':'"wmfu" <wmfu@fudan.edu.cn>',
'to':'16210240043@fudan.edu.cn, 16210240045@fudan.edu.cn, 16210240049@fudan.edu.cn, 16210240064@fudan.edu.cn, 16210240067@fudan.edu.cn, 16210240081@fudan.edu.cn, 16210240090@fudan.edu.cn, 16110240017@fudan.edu.cn, 16110240004@fudan.edu.cn, 16210240069@fudan.edu.cn, 17210240057@fudan.edu.cn, 17210240261@fudan.edu.cn',
'subject':'提醒：本周五9月7日学院注册－上周通知有误，以近日学院邮件通知为准，特此更正，望大家准时注册！9月7日上午9:00~11:00和下午13:00~16:00准时前来注册，注册地点：张江校区计算机学院院办104室。',
'sentDate':newdate(2018,8,4,12,14,42),
'receivedDate':newdate(2018,8,4,12,14,44),
'priority':1,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<46a08e5c.9e86.165a2ca2b04.Coremail.wmfu@fudan.edu.cn>',
'ref':'<46968f1b.3e8e.15f37ae8700.Coremail.wmfu@fudan.edu.cn><72c3ce5e.2a58c.160585beeab.Coremail.wmfu@fudan.edu.cn><11ed1a36.2f127.1609d230944.Coremail.wmfu@fudan.edu.cn><5a4baafc.9bf2.160b5d56e0e.Coremail.wmfu@fudan.edu.cn><181f565b.3c1a.165794592a0.Coremail.wmfu@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"wmfu" <wmfu@fudan.edu.cn>',
'add':'wmfu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYSCFKp0rOPMQAAm5',
'fid':1,
'size':5577,
'from':'"wmfu" <wmfu@fudan.edu.cn>',
'to':'"夏毅" <18210240217@fudan.edu.cn>',
'subject':'Re: 新生实验室报道',
'sentDate':newdate(2018,8,4,11,59,49),
'receivedDate':newdate(2018,8,4,11,59,50),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<b68febb.9e07.165a2bc887e.Coremail.wmfu@fudan.edu.cn>',
'ref':'<38b27eac.71d1.1659e3f70d6.Coremail.18210240217@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"宋昊" <16210240081@fudan.edu.cn>',
'add':'宋昊',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgYSBFKpyGh+iwAAs8',
'fid':1,
'size':15733630,
'from':'"宋昊" <16210240081@fudan.edu.cn>',
'to':'"吴承荣" <cwu@fudan.edu.cn>',
'subject':'论文 (0904)',
'sentDate':newdate(2018,8,4,10,33,15),
'receivedDate':newdate(2018,8,4,10,33,18),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<1b06cfff.97b5.165a26d47c3.Coremail.16210240081@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"朱迅" <17210240029@fudan.edu.cn>',
'add':'朱迅',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgSBFKp0rN+twAAsM',
'fid':1,
'size':11335,
'from':'"朱迅" <17210240029@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: RE: 关于18-19学年《网络攻击与防御技术》课程助教的工作',
'sentDate':newdate(2018,8,4,10,32,56),
'receivedDate':newdate(2018,8,4,10,32,57),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<1aa0fd1e.97ac.165a26cfe4a.Coremail.17210240029@fudan.edu.cn>',
'ref':'<2cf64a1a.564a0.164754644cd.Coremail.17210240029@fudan.edu.cn><000301d41756$4351d610$c9f58230$@fudan.edu.cn>,<000301d41756$4351d610$c9f58230$@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"余莉萍" <17210240022@fudan.edu.cn>',
'add':'余莉萍',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggSBFKpyGh6FQAAso',
'fid':1,
'size':12214,
'from':'"余莉萍" <17210240022@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: RE: 来自下学期《信息安全导论》课程助教',
'sentDate':newdate(2018,8,4,10,9,55),
'receivedDate':newdate(2018,8,4,10,9,56),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<76459c99.95e1.165a257e94d.Coremail.17210240022@fudan.edu.cn>',
'ref':'<60dc4a35.569ea.164783e1ac9.Coremail.17210240022@fudan.edu.cn><000901d41756$f3f65360$dbe2fa20$@fudan.edu.cn>,<000901d41756$f3f65360$dbe2fa20$@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"曹瑜" <caoyu@fudan.edu.cn>',
'add':'曹瑜',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQcSDFKp0rNtgAAAmv',
'fid':1,
'size':8298,
'from':'"曹瑜" <caoyu@fudan.edu.cn>',
'to':'"厉家鼎" <lijiading@fudan.edu.cn>, "彭 鑫" <pengxin@fudan.edu.cn>, "汪 卫" <weiwang1@fudan.edu.cn>, "王 晓阳" <xywangCS@fudan.edu.cn>, "吴 杰" <jwu@fudan.edu.cn>, "许晓茵" <xuxiaoyin@fudan.edu.cn>, "薛 向阳" <xyxue@fudan.edu.cn>, "张 玥杰" <yjzhang@fudan.edu.cn>, "赵 一鸣" <zhym@fudan.edu.cn>, "朱 扬勇" <yyzhu@fudan.edu.cn>, "张向东" <xdz>',
'subject':'【邯郸校区，周五上午9点】学院新学期工作会议通知',
'sentDate':newdate(2018,8,4,9,8,11),
'receivedDate':newdate(2018,8,4,9,8,12),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<201809040908093649669@fudan.edu.cn>',
'ref':'<201809030928594890689@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'add':'cs_keyan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQMSB1Kp0rNsrgAAmP',
'fid':1,
'size':52792,
'from':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'to':'"谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud>',
'subject':'Fw: 关于珠海复旦创新研究院项目征集的通知（预申报截止日期：9月14日）',
'sentDate':newdate(2018,8,4,9,4,25),
'receivedDate':newdate(2018,8,4,9,4,25),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<201809040904245631521@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"赵瑜" <15307130435@fudan.edu.cn>',
'add':'赵瑜',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgQRBFKpyGgvkwABs1',
'fid':1,
'size':4075,
'from':'"赵瑜" <15307130435@fudan.edu.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'Re: 关于推免生专业和方向的疑问',
'sentDate':newdate(2018,8,4,0,0,25),
'receivedDate':newdate(2018,8,4,0,0,29),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<pgdh0i1hjivqcnon0qs1ocg4.1535990425612@email.android.com>',
'ref':'<1eccc345.2fd0.1659d9e7602.Coremail.cwu@fudan.edu.cn>',
'rootid':'1tbiAggQBFKpyGdrFwAAs2'}},
{
'addT':'"jsgnljq" <jsgnljq@163.com>',
'add':'jsgnljq',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgURBFKpyGgpmQAAs5',
'fid':1,
'size':6729,
'from':'"jsgnljq" <jsgnljq@163.com>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'回复：Re:回复：RE: 关于地址跳变机制抗扫描能力的评估论文需要9月10日投出',
'sentDate':newdate(2018,8,3,20,3,18),
'receivedDate':newdate(2018,8,3,20,3,22),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<tencent_006A582DBDF8E5297B0415C4@qq.com>',
'ref':'<000001d4433c$b9052d50$2b0f87f0$@fudan.edu.cn><79f6b5b1.3a60.1659f2d97a7.Coremail.cwu@fudan.edu.cn>',
'rootid':'1tbiAQYHAFKp0q2dpwAAm+'}},
{
'addT':'"szhang" <szhang@fudan.edu.cn>',
'add':'szhang',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgURDlKpyGgWPAAAmp',
'fid':1,
'size':217499,
'from':'"szhang" <szhang@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Fw:  Re: 教育部工程中心评估PPT与答辩回执',
'sentDate':newdate(2018,8,3,17,48,30),
'receivedDate':newdate(2018,8,3,17,48,35),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'attached':'true'},
'hmid':'<7fec2c01.38a2.1659ed56638.Coremail.szhang@fudan.edu.cn>',
'rootid':'1tbiAggRDlKpyGe1hwAAmz'}},
{
'addT':'"szhang" <szhang@fudan.edu.cn>',
'add':'szhang',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQURDlKp0rMR3AAAmM',
'fid':1,
'size':212782,
'from':'"szhang" <szhang@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':' Re: 教育部工程中心评估PPT与答辩回执',
'sentDate':newdate(2018,8,3,17,10,57),
'receivedDate':newdate(2018,8,3,17,10,59),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'attached':'true'},
'hmid':'<6ebfb959.7cf5.1659eb305e2.Coremail.szhang@fudan.edu.cn>',
'rootid':'1tbiAggRDlKpyGe1hwAAmz'}},
{
'addT':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'add':'cs_keyan',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQIRB1Kp0rMJBAAAmC',
'fid':1,
'size':2830856,
'from':'"cs_keyan" <cs_keyan@fudan.edu.cn>',
'to':'"谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud>',
'subject':'Fw: 图书馆 中科2018年07-08期外文新书目',
'sentDate':newdate(2018,8,3,16,27,48),
'receivedDate':newdate(2018,8,3,16,27,53),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'attached':'true'},
'hmid':'<201809031627480503173@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"wmfu" <wmfu@fudan.edu.cn>',
'add':'wmfu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgcRCFKpyGgBuAAAm+',
'fid':1,
'size':19389,
'from':'"wmfu" <wmfu@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: RE: Re: Re: 统计KBH2301132/003项目的研究生经费发放',
'sentDate':newdate(2018,8,3,16,13,42),
'receivedDate':newdate(2018,8,3,16,13,43),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true'},
'hmid':'<40cae569.77cd.1659e7e9af7.Coremail.wmfu@fudan.edu.cn>',
'ref':'<000501d4433d$77826f90$66874eb0$@fudan.edu.cn><6d5c99f3.6a2b.1659df13cfc.Coremail.wmfu@fudan.edu.cn><7d62a185.3215.1659e072d6b.Coremail.wmfu@fudan.edu.cn><371f9d42.6f47.1659e27922d.Coremail.wmfu@fudan.edu.cn><000c01d4435a$99c35520$cd49ff60$@fudan.edu.cn>',
'rootid':'1tbiAQYRBFKp0rLU4wAAs+'}},
{
'addT':'"计算机学院" <cs_school@fudan.edu.cn>',
'add':'计算机学院',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgERCVKpyGf3TwAAm3',
'fid':1,
'size':38422,
'from':'"计算机学院" <cs_school@fudan.edu.cn>',
'to':'"汪 卫" <weiwang1@fudan.edu.cn>, "王 放" <fangwang@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 新" <xinw@fudan.edu.cn>, "王 雪平" <>',
'subject':'关于开展2018-2019年度教师公寓复审与租赁协议续签工作的通知',
'sentDate':newdate(2018,8,3,15,53,36),
'receivedDate':newdate(2018,8,3,15,53,39),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true',
'attached':'true'},
'hmid':'<tencent_0A5E3AC4119A33B6F0F0F4AB@qq.com>',
'rootid':''}},
{
'addT':'"周荃" <16210240049@fudan.edu.cn>',
'add':'周荃',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQURBFKp0rLqIAABsB',
'fid':1,
'size':10578,
'from':'"周荃" <16210240049@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: RE: 关于地址跳变机制抗扫描能力的评估论文需要9月10日投出',
'sentDate':newdate(2018,8,3,15,53,32),
'receivedDate':newdate(2018,8,3,15,53,33),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'read':'true'},
'hmid':'<dd8defa.760e.1659e6c2563.Coremail.16210240049@fudan.edu.cn>',
'ref':'<000001d4433c$b9052d50$2b0f87f0$@fudan.edu.cn>',
'rootid':'1tbiAQYHAFKp0q2dpwAAm+'}},
{
'addT':'"wmfu" <wmfu@fudan.edu.cn>',
'add':'wmfu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggRCFKpyGfeTgAAmX',
'fid':1,
'size':9761,
'from':'"wmfu" <wmfu@fudan.edu.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'Re: Re: Re: 统计KBH2301132/003项目的研究生经费发放',
'sentDate':newdate(2018,8,3,14,38,38),
'receivedDate':newdate(2018,8,3,14,38,39),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<371f9d42.6f47.1659e27922d.Coremail.wmfu@fudan.edu.cn>',
'ref':'<000501d4433d$77826f90$66874eb0$@fudan.edu.cn><6d5c99f3.6a2b.1659df13cfc.Coremail.wmfu@fudan.edu.cn><7d62a185.3215.1659e072d6b.Coremail.wmfu@fudan.edu.cn>,<7d62a185.3215.1659e072d6b.Coremail.wmfu@fudan.edu.cn>',
'rootid':'1tbiAQYRBFKp0rLU4wAAs+'}},
{
'addT':'"szhang" <szhang@fudan.edu.cn>',
'add':'szhang',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQMRDlKp0rLfogAAm7',
'fid':1,
'size':9705,
'from':'"szhang" <szhang@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Fw: Re: 教育部工程中心评估PPT与答辩回执',
'sentDate':newdate(2018,8,3,14,37,4),
'receivedDate':newdate(2018,8,3,14,37,6),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<6c7620d4.6f1a.1659e262340.Coremail.szhang@fudan.edu.cn>',
'rootid':'1tbiAggRDlKpyGe1hwAAmz'}},
{
'addT':'"jsgnljq" <jsgnljq@163.com>',
'add':'jsgnljq',
'icon':{
'm_icon':'REPLIED',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAgQRBFKpyGfdigABsR',
'fid':1,
'size':9652,
'from':'"jsgnljq" <jsgnljq@163.com>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'回复：RE: 关于地址跳变机制抗扫描能力的评估论文需要9月10日投出',
'sentDate':newdate(2018,8,3,14,34,46),
'receivedDate':newdate(2018,8,3,14,34,49),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'replied':'true'},
'hmid':'<tencent_8A15F3C9259FC4B12D9F474F@qq.com>',
'ref':'000001d4433c$b9052d50$2b0f87f0$@fudan.edu.cn<000001d4433c$b9052d50$2b0f87f0$@fudan.edu.cn>',
'rootid':'1tbiAQYHAFKp0q2dpwAAm+'}},
{
'addT':'"wmfu" <wmfu@fudan.edu.cn>',
'add':'wmfu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQgRCFKp0rLZVAAAmG',
'fid':1,
'size':7218,
'from':'"wmfu" <wmfu@fudan.edu.cn>',
'to':'"wmfu" <wmfu@fudan.edu.cn>',
'subject':'Re: Re: 统计KBH2301132/003项目的研究生经费发放',
'sentDate':newdate(2018,8,3,14,3,15),
'receivedDate':newdate(2018,8,3,14,3,18),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<7d62a185.3215.1659e072d6b.Coremail.wmfu@fudan.edu.cn>',
'ref':'<000501d4433d$77826f90$66874eb0$@fudan.edu.cn><6d5c99f3.6a2b.1659df13cfc.Coremail.wmfu@fudan.edu.cn>,<6d5c99f3.6a2b.1659df13cfc.Coremail.wmfu@fudan.edu.cn>',
'rootid':'1tbiAQYRBFKp0rLU4wAAs+'}},
{
'addT':'"wmfu" <wmfu@fudan.edu.cn>',
'add':'wmfu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYRBFKp0rLU4wAAs+',
'fid':1,
'size':4968,
'from':'"wmfu" <wmfu@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: 统计KBH2301132/003项目的研究生经费发放',
'sentDate':newdate(2018,8,3,13,39,17),
'receivedDate':newdate(2018,8,3,13,39,18),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<6d5c99f3.6a2b.1659df13cfc.Coremail.wmfu@fudan.edu.cn>',
'ref':'<000501d4433d$77826f90$66874eb0$@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"赵瑜" <15307130435@fudan.edu.cn>',
'add':'赵瑜',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggRBFKpyGe8xwACsy',
'fid':1,
'size':3845,
'from':'"赵瑜" <15307130435@fudan.edu.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'Re: 关于推免生专业和方向的疑问',
'sentDate':newdate(2018,8,3,12,38,17),
'receivedDate':newdate(2018,8,3,12,38,19),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<mrgg4e08vuui8h4peso4khce.1535949497020@email.android.com>',
'ref':'<1eccc345.2fd0.1659d9e7602.Coremail.cwu@fudan.edu.cn>',
'rootid':'1tbiAggQBFKpyGdrFwAAs2'}},
{
'addT':'"Computers & Security" <EviseSupport@elsevier.com>',
'add':'Computers & Security',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggRBFKpyGe8xwAAsw',
'fid':1,
'size':5524,
'from':'"Computers & Security" <EviseSupport@elsevier.com>',
'to':'cwu@fudan.edu.cn',
'subject':'Your co-authored submission',
'sentDate':newdate(2018,8,3,11,9,27),
'receivedDate':newdate(2018,8,3,11,13,53),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<010201659d681007-828fef28-6f9f-47ed-b75f-74338fd25ac3-000000@eu-west-1.amazonses.com>',
'rootid':'1tbiAgELBFKpyGSIfgAAst'}},
{
'addT':'"szhang" <szhang@fudan.edu.cn>',
'add':'szhang',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggRDlKpyGe1hwAAmz',
'fid':1,
'size':7369,
'from':'"szhang" <szhang@fudan.edu.cn>',
'to':'"cwu" <cwu@fudan.edu.cn>',
'subject':'Re: 教育部工程中心评估PPT与答辩回执',
'sentDate':newdate(2018,8,3,10,37,13),
'receivedDate':newdate(2018,8,3,10,37,16),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<3a09d4e8.2da4.1659d4a8c94.Coremail.szhang@fudan.edu.cn>',
'ref':'<001a01d442c7$e53c5ad0$afb51070$@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"曹瑜" <caoyu@fudan.edu.cn>',
'add':'曹瑜',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYRDFKp0rKgtgAAmX',
'fid':1,
'size':5674,
'from':'"曹瑜" <caoyu@fudan.edu.cn>',
'to':'"厉家鼎" <lijiading@fudan.edu.cn>, "彭 鑫" <pengxin@fudan.edu.cn>, "汪 卫" <weiwang1@fudan.edu.cn>, "王 晓阳" <xywangCS@fudan.edu.cn>, "吴 杰" <jwu@fudan.edu.cn>, "许晓茵" <xuxiaoyin@fudan.edu.cn>, "薛 向阳" <xyxue@fudan.edu.cn>, "张 玥杰" <yjzhang@fudan.edu.cn>, "赵 一鸣" <zhym@fudan.edu.cn>, "朱 扬勇" <yyzhu@fudan.edu.cn>, "张向东" <xdz>',
'subject':'【会议预通知】新学期工作会议预通知',
'sentDate':newdate(2018,8,3,9,29,0),
'receivedDate':newdate(2018,8,3,9,29,1),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true'},
'hmid':'<201809030928594890689@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"赵瑜" <15307130435@fudan.edu.cn>',
'add':'赵瑜',
'icon':{
'm_icon':'REPLIED',
'p_icon':'NORMAL',
'att_icon':'',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'2:1tbiAggQBFKpyGdrFwAAs2',
'fid':1,
'size':2195,
'from':'"赵瑜" <15307130435@fudan.edu.cn>',
'to':'cwu@fudan.edu.cn',
'subject':'关于推免生专业和方向的疑问',
'sentDate':newdate(2018,8,2,22,39,51),
'receivedDate':newdate(2018,8,2,22,39,53),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'replied':'true'},
'hmid':'<101a3262.4f52.1659ab9c7eb.Coremail.15307130435@fudan.edu.cn>',
'rootid':''}},
{
'addT':'"Jie Wu" <jwu@fudan.edu.cn>',
'add':'Jie Wu',
'icon':{
'm_icon':'NORMAL',
'p_icon':'NORMAL',
'att_icon':'ATTACHED',
'avs_icon':'UNSCANED',
'flagged_icon':'flagged_false'},
'item':{
'id':'1:1tbiAQYQBFKp0rJpHgAAs-',
'fid':1,
'size':24833,
'from':'"Jie Wu" <jwu@fudan.edu.cn>',
'to':'"\'cwu\'" <cwu@fudan.edu.cn>',
'subject':'',
'sentDate':newdate(2018,8,2,22,13,27),
'receivedDate':newdate(2018,8,2,22,12,28),
'priority':3,
'backgroundColor':0,
'antiVirusStatus':'unscaned',
'label0':0,
'flags':{
'popRead':'true',
'read':'true',
'attached':'true'},
'hmid':'<000601d442c7$1ea12770$5be37650$@edu.cn>',
'rootid':''}}]
```


```python
mailCount = 0
for item in mailContent:
    mailCount += 1
    term = item['item']
    tid = term['id']
    tfrom = term['from']
    tto = term['to']
    tsubject = term['subject']
    tsentdate = term['sentDate']
    treceivedate = term['receivedDate']
    print('\n第',mailCount,'封邮件：',
          '\nid:', tid,
          '\nfrom:', tfrom,
          '\nto:', tto,
          '\nsubject:', tsubject,
          '\nsentdate:', tsentdate,
          '\nreceivedate:', treceivedate)
print('\n邮箱的邮件列表中总共有',mailCount,'封邮件')
```


    第 1 封邮件： 
    id: 2:1tbiAgkTBFKpyHeThQABsP 
    from: "WU Chengrong" <13601927008@sina.cn> 
    to: cwu@fudan.edu.cn 
    subject: 课程测试邮件 
    sentdate: 201825145912 
    receivedate: 20182515157
    
    第 2 封邮件： 
    id: 1:1tbiAQYTBFKp0sKMFwAAsg 
    from: "科学出版社李海" <663241303@qq.com> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: 科学出版社—专著出版 
    sentdate: 20182511256 
    receivedate: 20182511358
    
    第 3 封邮件： 
    id: 1:1tbiAQITB1Kp0sKK4gAAmU 
    from: "cs_keyan" <cs_keyan@fudan.edu.cn> 
    to: "谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud> 
    subject: Fw: 关于举办“上海科创中心建设”报告的通知 
    sentdate: 201825105943 
    receivedate: 201825105947
    
    第 4 封邮件： 
    id: 2:1tbiAggTCFKpyHde4QAAmq 
    from: "wmfu" <wmfu@fudan.edu.cn> 
    to: cremiy@163.com 
    subject: Re: Fw:推免生咨询 
    sentdate: 20182510331 
    receivedate: 20182510337
    
    第 5 封邮件： 
    id: 1:1tbiAQcTBFKp0sJ5QQAAsC 
    from: "Andrew fu" <zgbzlm@yeah.net> 
    to: cwu@fudan.edu.cn 
    subject: RE：工信中心邀请函 
    sentdate: 20182595418 
    receivedate: 20182595422
    
    第 6 封邮件： 
    id: 1:1tbiAQgSBFKp0sI6eAAAs2 
    from: "余莉萍" <17210240022@fudan.edu.cn> 
    to: cwu@fudan.edu.cn 
    subject: 来自《信息安全导论》助教 
    sentdate: 201824223812 
    receivedate: 201824223818
    
    第 7 封邮件： 
    id: 1:1tbiAQcSD1Kp0sI5iQAAmA 
    from: "沈建蓉" <jrshen@fudan.edu.cn> 
    to: "weihui" <weihui@fudan.edu.cn>, "cwu" <cwu@fudan.edu.cn>, "jwu" <jwu@fudan.edu.cn>, "wuyijian" <wuyijian@fudan.edu.cn>, "yhwu" <yhwu@fudan.edu.cn>, "xxiaochun" <xxiaochun@fudan.edu.cn>, "shawyh" <shawyh@fudan.edu.cn>, "xiezp" <xiezp@fudan.edu.cn>, "yunx" <yunx@fudan.edu.cn>, "xuyx" <xuyx@fudan.edu.cn>, "xyxue" 
    subject: 本学期学位申请程序 
    sentdate: 20182422343 
    receivedate: 20182422349
    
    第 8 封邮件： 
    id: 1:1tbiAQYSBFKp0sHonAAAsN 
    from: "17307130324" <17307130324@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: 关于信息安全导论的教学ppt 
    sentdate: 20182495948 
    receivedate: 20182495950
    
    第 9 封邮件： 
    id: 2:1tbiAgESBFKpyHbC4gAAsw 
    from: "余莉萍" <17210240022@fudan.edu.cn> 
    to: cwu@fudan.edu.cn 
    subject: 祝老师中秋节快乐~ 
    sentdate: 20182495420 
    receivedate: 20182495423
    
    第 10 封邮件： 
    id: 2:1tbiAgERBFKpyHaizQAAm8 
    from: "余莉萍" <lipingyuu@163.com> 
    to: "13307130375" <13307130375@fudan.edu.cn>, "13307130390" <13307130390@fudan.edu.cn>, "14307130308" <14307130308@fudan.edu.cn>, "16307110240" <16307110240@fudan.edu.cn>, "16307110300" <16307110300@fudan.edu.cn>, "16307110315" <16307110315@fudan.edu.cn>, "16307110511" <16307110511@fudan.edu.cn>, "16307130213" 
    subject: 来自《信息安全导论》TA 
    sentdate: 201823222532 
    receivedate: 201823222536
    
    第 11 封邮件： 
    id: 2:1tbiAgIQBFKpyHZScgAAsx 
    from: "lkjh lkjh" <lkjhlkjh1919@gmail.com> 
    to:  
    subject: Fwd: 主题：2018年9月21日星期五 ……【周末快乐！】 
    sentdate: 20182301211 
    receivedate: 20182311848
    
    第 12 封邮件： 
    id: 1:1tbiAQcQDlKp0sFPpwAAmY 
    from: "szhang" <szhang@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn>, "严明" <myan@fudan.edu.cn>, "曾剑平" <zjp@fudan.edu.cn> 
    subject: Fw: 张世永教授，邀请您参加2018年第七届全国网络与信息安全防护峰会 
    sentdate: 201822162120 
    receivedate: 201822162123
    
    第 13 封邮件： 
    id: 2:1tbiAgcQBFKpyHYkEgAAsi 
    from: "ResearchGate" <no-reply@researchgatemail.net> 
    to: "Chengrong Wu" <cwu@fudan.edu.cn> 
    subject: Chengrong, we think you may have missed a citation of your research 
    sentdate: 20182214598 
    receivedate: 20182215634
    
    第 14 封邮件： 
    id: 2:1tbiAgcQBFKpyHYM9wAAsv 
    from: "上海大学计算机学院推免生" <cremiy@163.com> 
    to: cwu@fudan.edu.cn 
    subject: 推免生咨询 
    sentdate: 20182210583 
    receivedate: 20182210584
    
    第 15 封邮件： 
    id: 2:1tbiAgUPBFKpyHX0sgACsO 
    from: "Springer" <springer@newsletter.springer.com> 
    to: cwu@fudan.edu.cn 
    subject: 分享您的数据经验，有机会赢得1000元礼品卡 
    sentdate: 20182292028 
    receivedate: 2018229277
    
    第 16 封邮件： 
    id: 2:1tbiAggPBFKpyHW1jAAAs+ 
    from: "ResearchGate" <no-reply@researchgatemail.net> 
    to: cwu@fudan.edu.cn 
    subject: Adnen El Amraoui uploaded a full-text citing you 
    sentdate: 20182121111 
    receivedate: 201821211629
    
    第 17 封邮件： 
    id: 1:1tbiAQgPBFKp0sDWTQAAsw 
    from: "CCF会员部" <ccfmk@membership.ccf.org.cn> 
    to: cwu@fudan.edu.cn 
    subject: CCF近期活动推送（第3期） 
    sentdate: 201821194434 
    receivedate: 20182120452
    
    第 18 封邮件： 
    id: 1:1tbiAQgPB1Kp0sCbvgAAmN 
    from: "cs_keyan" <cs_keyan@fudan.edu.cn> 
    to: "谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud> 
    subject: Fw: Fw: 科学卫星的发展及国际化应用研讨会（10.22日下午） 
    sentdate: 20182115157 
    receivedate: 20182115154
    
    第 19 封邮件： 
    id: 2:1tbiAgEPB1KpyHV1zQAAm1 
    from: "cs_keyan" <cs_keyan@fudan.edu.cn> 
    to: "谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud> 
    subject: Fw: 关于推荐2018年度“中国高等学校十大科技进展”候选项目的通知 
    sentdate: 201821151353 
    receivedate: 201821151352
    
    第 20 封邮件： 
    id: 1:1tbiAQgPBFKp0sCcEAAAsn 
    from: "ResearchGate" <no-reply@researchgatemail.net> 
    to: "Chengrong Wu" <cwu@fudan.edu.cn> 
    subject: Chengrong, you were cited by an author from Université d'Orléans 
    sentdate: 20182115753 
    receivedate: 201821151638
    
    第 21 封邮件： 
    id: 1:1tbiAQYPBFKp0sCQ6AAAsd 
    from: "ResearchGate" <no-reply@researchgatemail.net> 
    to: cwu@fudan.edu.cn 
    subject: Chengrong, did this researcher author this publication? 
    sentdate: 20182114178 
    receivedate: 201821142632
    
    第 22 封邮件： 
    id: 2:1tbiAgMPBFKpyHVnjwAAsk 
    from: "中国农业银行" <e-statement@creditcard.abchina.com> 
    to: cwu@fudan.edu.cn 
    subject: 中国农业银行金穗信用卡电子对账单 
    sentdate: 2018211487 
    receivedate: 201821141222
    
    第 23 封邮件： 
    id: 2:1tbiAgkPDlKpyHVGaQAAmj 
    from: "何加林" <czhejialin@163.com> 
    to: caoyu@fudan.edu.cn, xiucao@fudan.edu.cn, mmchi@fudan.edu.cn, wnchen@fudan.edu.cn, chenlf@fudan.edu.cn, xqchen@fudan.edu.cn, tbchen@fudan.edu.cn, bhchen@fudan.edu.cn, yijiachen@fudan.edu.cn, chenrh@fudan.edu.cn, chenc@fudan.edu.cn, chenyq@fudan.edu.cn, dingx@fudan.edu.cn, dingsf@fudan.edu.cn, kydai@fudan.edu.cn, fu 
    subject: 《电与磁的材料问题》 
    sentdate: 201821103127 
    receivedate: 201821111734
    
    第 24 封邮件： 
    id: 1:1tbiAQgPBFKp0sBhdwAAs9 
    from: "上海市科学技术委员会" <infomail@newsletter.stcsm.gov.cn> 
    to: cwu@fudan.edu.cn 
    subject: 科技服务信息专递第四百五十四期 
    sentdate: 201821102843 
    receivedate: 201821103410
    
    第 25 封邮件： 
    id: 1:1tbiAQcPBFKp0sBY8QAAsN 
    from: "ResearchGate" <no-reply@researchgatemail.net> 
    to: "Chengrong Wu" <cwu@fudan.edu.cn> 
    subject: Chengrong, you have 1 more citation 
    sentdate: 20182194755 
    receivedate: 20182195624
    
    第 26 封邮件： 
    id: 2:1tbiAgIPEVKpyHVeGAAAme 
    from: "Fan Wu" <fwu@cs.sjtu.edu.cn> 
    to: CCF-Shanghai@cs.sjtu.edu.cn 
    subject: [CCF-Shanghai] FW: 回复： CNCC2018报名情况统计及组团福利 
    sentdate: 2018219381 
    receivedate: 20182113258
    
    第 27 封邮件： 
    id: 2:1tbiAgQPBFKpyHUmAAACsv 
    from: "古短愛" <tri.945125@gmail.com> 
    to: cwu@fudan.edu.cn 
    subject: э乔石痛批政法委周И=永v康 
    sentdate: 2018219121 
    receivedate: 20182191327
    
    第 28 封邮件： 
    id: 2:1tbiAgQPBFKpyHUmAAABss 
    from: "Bank of America" <Bank of America> 
    to: cwu@fudan.edu.cn 
    subject: Bank of America alert : Your account has been locked 
    sentdate: 20182174621 
    receivedate: 2018219213
    
    第 29 封邮件： 
    id: 1:1tbiAQUOBFKp0r-5qAAAsJ 
    from: "CCF Digital" <ccfdigital@ccfdigital.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: CCF技术动态【2018第292期】 
    sentdate: 201820191434 
    receivedate: 201820193130
    
    第 30 封邮件： 
    id: 2:1tbiAgUOBFKpyHS+WwAAsv 
    from: "yuhunmin@163.com" <yuhunmin@163.com> 
    to: cwu@fudan.edu.cn, csx1030@163.net 
    subject: yuhunmin@163.com 
    sentdate: 20182017541 
    receivedate: 20182017545
    
    第 31 封邮件： 
    id: 2:1tbiAggOBFKpyHSs2AAAmz 
    from: "wanghuimin" <wanghm@fudan.edu.cn> 
    to: "曹瑜" <caoyu@fudan.edu.cn>, fangxf@fudan.edu.cn 
    subject: Re: Re: 关于保密学院物业管理人员安排事宜 
    sentdate: 201820162924 
    receivedate: 201820162929
    
    第 32 封邮件： 
    id: 2:1tbiAgMOBFKpyHSatQAAmj 
    from: "wanghuimin" <wanghm@fudan.edu.cn> 
    to: "曹瑜" <caoyu@fudan.edu.cn> 
    subject: Re: Re: 搬迁费用支付事宜 
    sentdate: 20182015840 
    receivedate: 20182015844
    
    第 33 封邮件： 
    id: 2:1tbiAggOE1KpyHSV2QAAmc 
    from: "曹瑜" <caoyu@fudan.edu.cn> 
    to: "wanghuimin" <wanghm@fudan.edu.cn>, "方旭峰" <fangxf@fudan.edu.cn> 
    subject: Re: 关于保密学院物业管理人员安排事宜 
    sentdate: 201820145129 
    receivedate: 201820145131
    
    第 34 封邮件： 
    id: 1:1tbiAQgOE1Kp0r+5TQAAm2 
    from: "曹瑜" <caoyu@fudan.edu.cn> 
    to: "wanghuimin" <wanghm@fudan.edu.cn> 
    subject: Re: 搬迁费用支付事宜 
    sentdate: 201820144540 
    receivedate: 201820144542
    
    第 35 封邮件： 
    id: 1:1tbiAQgOE1Kp0r+30gAAmn 
    from: "wanghuimin" <wanghm@fudan.edu.cn> 
    to: "曹瑜" <caoyu@fudan.edu.cn> 
    subject: 搬迁费用支付事宜 
    sentdate: 201820143858 
    receivedate: 20182014392
    
    第 36 封邮件： 
    id: 1:1tbiAQcOBFKp0r+zXwAAm2 
    from: "wanghuimin" <wanghm@fudan.edu.cn> 
    to: "姚晓枝" <xzyao@fudan.edu.cn> 
    subject: 关于保密学院物业管理人员安排事宜 
    sentdate: 201820141958 
    receivedate: 20182014202
    
    第 37 封邮件： 
    id: 2:1tbiAgEODVKpyHRxiQAAm- 
    from: "计算机学院人事" <cs_renshi@fudan.edu.cn> 
    to: "颜波" <byan@fudan.edu.cn>, "吴承荣" <cwu@fudan.edu.cn>, "肖川" <cxiao@fudan.edu.cn>, "朱崇湘" <cxzhu@fudan.edu.cn>, "叶 德建" <dejianye@fudan.edu.cn>, "王放" <fangwang@fudan.edu.cn>, "王国平" <gpwang@fudan.edu.cn>, "张建国" <jgzhang@fudan.edu.cn>, "周健敏" <jmz0806@163.com>, "张军平" <jpzhang@fudan.edu.cn>, "吴杰" <jwu@fudan.edu.cn>, "叶家" 
    subject: 关于2018年度下半年党政管理岗位公开招聘的通知 
    sentdate: 20182012112 
    receivedate: 201820112820
    
    第 38 封邮件： 
    id: 1:1tbiAQgOCVKp0r+OHgAAmI 
    from: "计算机学院" <cs_school@fudan.edu.cn> 
    to: "汪 卫" <weiwang1@fudan.edu.cn>, "王 放" <fangwang@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 新" <xinw@fudan.edu.cn>, "王 雪平" <> 
    subject: 复旦大学货物零星采购实施细则（暂行）（0910征求意见稿） 
    sentdate: 20182010504 
    receivedate: 20182010507
    
    第 39 封邮件： 
    id: 2:1tbiAgMOBFKpyHRklQAAs9 
    from: LAKAKA@mail.iwmsme.org 
    to: cwu@fudan.edu.cn 
    subject: 第二届iwmsme2018征集原创优质稿件由IOP conference series出版 
    sentdate: 201820102358 
    receivedate: 201820103112
    
    第 40 封邮件： 
    id: 1:1tbiAQcOBFKp0r9-zwAAsq 
    from: "LJQ" <jsgnljq@163.com> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re:已提交的论文 
    sentdate: 20182094914 
    receivedate: 20182094915
    
    第 41 封邮件： 
    id: 2:1tbiAgQNDlKpyHO8vwAAmG 
    from: "wmfu" <wmfu@fudan.edu.cn> 
    to: 18210240027@fudan.edu.cn, 18210240038@fudan.edu.cn, 18210240123@fudan.edu.cn, 18210240136@fudan.edu.cn, 18210240075@fudan.edu.cn, 18210240173@fudan.edu.cn, 18210240110@fudan.edu.cn, 18210240262@fudan.edu.cn, 18210240237@fudan.edu.cn, 18210240252@fudan.edu.cn, 18210240146@fudan.edu.cn, 18210240082@fudan.edu.cn 
    subject: 转发学院: 关于2018年中秋节期间若干工作安排的通知－望大家注意实验室中秋假期的安全！ 
    sentdate: 201819141734 
    receivedate: 201819141741
    
    第 42 封邮件： 
    id: 2:1tbiAggNCVKpyHOQcQAAmv 
    from: "计算机学院" <cs_school@fudan.edu.cn> 
    to: "汪 卫" <weiwang1@fudan.edu.cn>, "王 放" <fangwang@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 新" <xinw@fudan.edu.cn>, "王 雪平" <> 
    subject: 关于2018年中秋节期间若干工作安排的通知 
    sentdate: 201819102619 
    receivedate: 201819102622
    
    第 43 封邮件： 
    id: 1:1tbiAQENBFKp0r6yMQAAsd 
    from: zxzj@sheitc.gov.cn 
    to: cwu@fudan.edu.cn 
    subject: 上海市经济和信息化委员会项目评审邀请函 
    sentdate: 201819101247 
    receivedate: 201819101420
    
    第 44 封邮件： 
    id: 2:1tbiAggNBFKpyHOOwgAAsP 
    from: "CFP Conference" <cfp.conference2016@GMAIL.COM> 
    to: BIGDATA@LISTS.DREXEL.EDU 
    subject: IEEE BigData 2018 Call for Workshop Papers and Posters 
    sentdate: 20181992614 
    receivedate: 201819101911
    
    第 45 封邮件： 
    id: 1:1tbiAQgMBFKp0r5hXQAAsq 
    from: "ResearchGate" <no-reply@researchgatemail.net> 
    to: "Chengrong Wu" <cwu@fudan.edu.cn> 
    subject: Wei Wang published an article 
    sentdate: 20181822433 
    receivedate: 201818221137
    
    第 46 封邮件： 
    id: 2:1tbiAgIMBFKpyHMzOQAAsC 
    from: "sicase@sicase.org" <sicase@sicase.org> 
    to: cwu@fudan.edu.cn 
    subject: Re:[2019 Seoul Conference Invitation]*Applied Science*Engineering 
    sentdate: 20181821948 
    receivedate: 201818211445
    
    第 47 封邮件： 
    id: 1:1tbiAQYME1Kp0r5WNAAAmt 
    from: "wanghuimin" <wanghm@fudan.edu.cn> 
    to: "吴承荣" <cwu@fudan.edu.cn> 
    subject: 复旦大学国家保密学院暨国家保密教育培训基地上海分基地总结（2016-2018） 
    sentdate: 20181821543 
    receivedate: 20181821550
    
    第 48 封邮件： 
    id: 1:1tbiAQcMBFKp0r5TXgAAmU 
    from: "wanghuimin" <wanghm@fudan.edu.cn> 
    to: "曹瑜" <caoyu@fudan.edu.cn>, "吴承荣" <cwu@fudan.edu.cn> 
    subject: Re: Re: Re:_Re:_专项经费项目预算模板---9.14 
    sentdate: 201818204947 
    receivedate: 201818204954
    
    第 49 封邮件： 
    id: 2:1tbiAgYMDVKpyHMBzQAAmJ 
    from: "计算机学院人事" <cs_renshi@fudan.edu.cn> 
    to: "颜波" <byan@fudan.edu.cn>, "吴承荣" <cwu@fudan.edu.cn>, "肖川" <cxiao@fudan.edu.cn>, "朱崇湘" <cxzhu@fudan.edu.cn>, "叶 德建" <dejianye@fudan.edu.cn>, "王放" <fangwang@fudan.edu.cn>, "王国平" <gpwang@fudan.edu.cn>, "张建国" <jgzhang@fudan.edu.cn>, "周健敏" <jmz0806@163.com>, "张军平" <jpzhang@fudan.edu.cn>, "吴杰" <jwu@fudan.edu.cn>, "叶家" 
    subject: 【重要通知】关于2019年度公派出国计划申报的通知 
    sentdate: 201818171731 
    receivedate: 201818163453
    
    第 50 封邮件： 
    id: 2:1tbiAggMCFKpyHLlXgAAm0 
    from: "wmfu" <wmfu@fudan.edu.cn> 
    to: "xuwuxing" <by70_by70@aliyun.com> 
    subject: Re: Fw:中矿大信息安全专业推免生徐武兴 
    sentdate: 201818142517 
    receivedate: 201818142522
    
    第 51 封邮件： 
    id: 1:1tbiAQIMDlKp0r4GCwAAmb 
    from: "wmfu" <wmfu@fudan.edu.cn> 
    to: "wmfu" <wmfu@fudan.edu.cn> 
    subject: 提醒－Re: 兹定于9月19日（周三）上午9时在逸夫楼407室，迎新2018级全体研究生，请课题组老师和2018级全体新生参加！NiSL-Sept-12-2018 
    sentdate: 201818141458 
    receivedate: 20181814154
    
    第 52 封邮件： 
    id: 2:1tbiAggMBFKpyHLdkgAAsM 
    from: "julie-zhu" <sjtu-julie@sjtu.edu.cn> 
    to: cwu@fudan.edu.cn 
    subject: 上海交大高教院课题组诚邀您参与高校科研人才评价政策认同情况调查 
    sentdate: 201818135129 
    receivedate: 201818135318
    
    第 53 封邮件： 
    id: 1:1tbiAQUME1Kp0r3fSgAAma 
    from: "曹瑜" <caoyu@fudan.edu.cn> 
    to: "wanghuimin" <wanghm@fudan.edu.cn> 
    subject: Re: Re:_Re:_专项经费项目预算模板---9.14 
    sentdate: 20181811126 
    receivedate: 20181811127
    
    第 54 封邮件： 
    id: 2:1tbiAgELEFKpyHJZoQAAmh 
    from: "沈建蓉" <jrshen@fudan.edu.cn> 
    to: "chenyq" <chenyq@fudan.edu.cn>, "ygj" <ygj@fudan.edu.cn>, "hbkan" <hbkan@fudan.edu.cn>, "lijt" <lijt@fudan.edu.cn>, "limb" <limb@fudan.edu.cn>, "weili-fudan" <weili-fudan@fudan.edu.cn>, "xpqiu" <xpqiu@fudan.edu.cn>, "zjtan" <zjtan@fudan.edu.cn>, "weiwang1" <weiwang1@fudan.edu.cn>, "wangfei" <wangfei@fudan.ed> 
    subject: 请评审您的学生的学位论文和项目视频 
    sentdate: 20181721397 
    receivedate: 201817213913
    
    第 55 封邮件： 
    id: 1:1tbiAQELBFKp0r1pEQAAsj 
    from: "LJQ" <jsgnljq@163.com> 
    to: "cwu@fudan.edu.cn" <cwu@fudan.edu.cn> 
    subject: IP地址跳变机制抗扫描能力评估4 
    sentdate: 201817191641 
    receivedate: 201817191643
    
    第 56 封邮件： 
    id: 1:1tbiAQILEVKp0r1Y-QAAmo 
    from: "龚洁" <gongjie@fudan.edu.cn> 
    to: "阚海斌" <hbkan@fudan.edu.cn>, "ylzhao" <ylzhao@fudan.edu.cn>, "cwu" <cwu@fudan.edu.cn>, "bhchen" <bhchen@fudan.edu.cn>, zhengxq@fudan.edu.cn 
    subject: 明天推免面试通知（调整） 
    sentdate: 201817173559 
    receivedate: 20181717364
    
    第 57 封邮件： 
    id: 2:1tbiAgYLB1KpyHId6wAAm- 
    from: "cs_keyan" <cs_keyan@fudan.edu.cn> 
    to: "谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud> 
    subject: Fw: 转发科技部国际合作司关于征集中国－黑山政府间科技合作委员会第3届例会交流项目的通知 
    sentdate: 201817153727 
    receivedate: 201817153732
    
    第 58 封邮件： 
    id: 2:1tbiAgkLB1KpyHId3AAAmH 
    from: "cs_keyan" <cs_keyan@fudan.edu.cn> 
    to: "谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud> 
    subject: Fw: 转发科技部国际合作司关于征集中泰（国）政府间科技合作联委会短期交流项目的通知 
    sentdate: 20181715376 
    receivedate: 201817153712
    
    第 59 封邮件： 
    id: 2:1tbiAgQLBFKpyHIYxgAAsW 
    from: "tang@e-neurons.net" <tang@e-neurons.net> 
    to: "丁瑞浩" <dingruihao23@163.com>, "陆新" <eluxin@139.com>, "游红俊" <snowolf8271@sina.com>, "杭玲" <linda.hang@dbappsecurity.com.cn>, "蒋涛" <5670545@qq.com>, "阮伟" <ruanwei@zju.edu.cn>, "王雪怡" <wangxueyi@sjtu.edu.cn>, "徐巍" <xuweisome@sjtu.edu.cn>, "崔涛" <cuitao@catr.cn>, "张第" <zhangdi49@chinaunicom.cn>, "冯四风" <feng_sifeng@1> 
    subject: 拟联[2018]3号：关于拟态核心专利授权协议（2018修订版）的通知 
    sentdate: 201817151716 
    receivedate: 201817151734
    
    第 60 封邮件： 
    id: 1:1tbiAQYLCFKp0r02CQAAmv 
    from: "计算机学院工会" <cs_gonghui@fudan.edu.cn> 
    to: "汪 卫" <weiwang1@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 雪平" <wangxp@fudan.edu.cn>, "王 毅敏" <yiminwang@fudan.edu.cn>, "王" 
    subject: 关于2018年下半年办理工会会员服务卡的通知 
    sentdate: 201817144444 
    receivedate: 201817144450
    
    第 61 封邮件： 
    id: 2:1tbiAgULBFKpyHH1CAABs2 
    from: "余莉萍" <17210240022@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: 关于信息安全导论作业的打分 
    sentdate: 201817122220 
    receivedate: 201817122224
    
    第 62 封邮件： 
    id: 2:1tbiAgULBFKpyHH1CAAAs3 
    from: "luzhihui" <lzh@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: RE: RE: 数荃公司的项目想约大家讨论一下 
    sentdate: 20181712532 
    receivedate: 20181712534
    
    第 63 封邮件： 
    id: 1:1tbiAQgLBFKp0rzzxwADsk 
    from: "luzhihui" <lzh@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: RE: 数荃公司的项目想约大家讨论一下 
    sentdate: 201817114832 
    receivedate: 201817114834
    
    第 64 封邮件： 
    id: 1:1tbiAQYLEVKp0rztaAAAmN 
    from: "gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn> 
    to: "阚海斌" <hbkan@fudan.edu.cn>, "赵运磊" <ylzhao@fudan.edu.cn>, "吴承荣" <cwu@fudan.edu.cn>, "吕智慧" <lzh@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn> 
    subject: 周二本科推免资格面试通知 
    sentdate: 20181784351 
    receivedate: 20181784352
    
    第 65 封邮件： 
    id: 1:1tbiAQcKBFKp0rzQHQADsT 
    from: "luzhihui" <lzh@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: 数荃公司的项目想约大家讨论一下 
    sentdate: 201817824 
    receivedate: 201817825
    
    第 66 封邮件： 
    id: 1:1tbiAQIKBFKp0rybTwAAsM 
    from: "xu jingnan" <xujn@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: 回复: 回复: 一个软件著作权，之前没有提交的 
    sentdate: 201816132723 
    receivedate: 201816132723
    
    第 67 封邮件： 
    id: 2:1tbiAgMKBFKpyHFrmQABs+ 
    from: "xu jingnan" <xujn@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: 回复: 一个软件著作权，之前没有提交的 
    sentdate: 201816123029 
    receivedate: 201816123028
    
    第 68 封邮件： 
    id: 2:1tbiAgMKBFKpyHFrmQAAs- 
    from: "携程旅行网" <recommend@lists4.ctrip.com> 
    to: cwu@fudan.edu.cn 
    subject: 抢199元低价出游！更有900元旅游首单券等您来拿！ 
    sentdate: 201816105153 
    receivedate: 2018161142
    
    第 69 封邮件： 
    id: 1:1tbiAQYJBFKp0rxsLQAAse 
    from: "Lbj Wei" <weilbj6@gmail.com> 
    to:  
    subject: Fwd: 主题：2018年9月14日星期五 ……【周末快乐！】 
    sentdate: 20181603619 
    receivedate: 20181614551
    
    第 70 封邮件： 
    id: 2:1tbiAgkJBFKpyHETUAABsG 
    from: "xuwuxing" <by70_by70@aliyun.com> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: 中矿大信息安全专业推免生徐武兴 
    sentdate: 20181516108 
    receivedate: 201815161013
    
    第 71 封邮件： 
    id: 2:1tbiAgYJDlKpyHDrAQAAmq 
    from: "何加林" <czhejialin@163.com> 
    to: caoyu@fudan.edu.cn, xiucao@fudan.edu.cn, mmchi@fudan.edu.cn, wnchen@fudan.edu.cn, chenlf@fudan.edu.cn, xqchen@fudan.edu.cn, tbchen@fudan.edu.cn, bhchen@fudan.edu.cn, yijiachen@fudan.edu.cn, chenrh@fudan.edu.cn, chenc@fudan.edu.cn, chenyq@fudan.edu.cn, dingx@fudan.edu.cn, dingsf@fudan.edu.cn, kydai@fudan.edu.cn, fu 
    subject: 《电学理论的物质矛盾》 
    sentdate: 20181583552 
    receivedate: 2018159225
    
    第 72 封邮件： 
    id: 1:1tbiAQgIBVKp0rvxPgAAmZ 
    from: "Fan Wu" <fwu@cs.sjtu.edu.cn> 
    to: CCF-Shanghai@cs.sjtu.edu.cn 
    subject: [CCF-Shanghai] CNCC2018报名情况统计及组团福利 
    sentdate: 201814231223 
    receivedate: 2018152256
    
    第 73 封邮件： 
    id: 2:1tbiAggIBFKpyHCaDwADsT 
    from: "汪钰颖" <17210240209@fudan.edu.cn> 
    to: "吴承荣老师" <cwu@fudan.edu.cn> 
    subject: Splunk应用效果图 
    sentdate: 201814215244 
    receivedate: 201814215247
    
    第 74 封邮件： 
    id: 2:1tbiAggIBFKpyHCaDwABsR 
    from: "CCF会员部" <ccfmk@membership.ccf.org.cn> 
    to: cwu@fudan.edu.cn 
    subject: CNCC“早鸟票”倒计时（9月21日结束） 
    sentdate: 20181418327 
    receivedate: 201814184635
    
    第 75 封邮件： 
    id: 1:1tbiAQYICFKp0ru0vwAAme 
    from: "龚洁" <gongjie@fudan.edu.cn> 
    to: "曾剑平" <zjp@fudan.edu.cn>, "陈利锋" <chenlf@fudan.edu.cn>, "池明旻" <mmchi@fudan.edu.cn>, "陈彤兵" <tbchen@fudan.edu.cn>, "陈伟男" <wnchen@fudan.edu.cn>, "曹袖" <Xiucao@fudan.edu.cn>, "陈学青" <xqchen@fudan.edu.cn>, "陈阳" <chenyang@fudan.edu.cn>, "Chen" <yijiachen@fudan.edu.cn>, "陈雁秋" <chenyq@fudan.edu.cn>, "丁向华" <dingx@fudan.e> 
    subject: 本科教学评估材料上报（更新） 
    sentdate: 201814174623 
    receivedate: 201814174631
    
    第 76 封邮件： 
    id: 2:1tbiAgMIBFKpyHCHqQAAmg 
    from: "wanghuimin" <wanghm@fudan.edu.cn> 
    to: "曹瑜" <caoyu@fudan.edu.cn>, "吴承荣" <cwu@fudan.edu.cn>, "吴杰" <jwu@fudan.edu.cn> 
    subject: Re: Re: 专项经费项目预算模板---9.14 
    sentdate: 201814165124 
    receivedate: 201814165126
    
    第 77 封邮件： 
    id: 2:1tbiAgUIDlKpyHCCcwAAmz 
    from: "gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn> 
    to: "曾剑平" <zjp@fudan.edu.cn>, "陈利锋" <chenlf@fudan.edu.cn>, "池明旻" <mmchi@fudan.edu.cn>, "陈彤兵" <tbchen@fudan.edu.cn>, "陈伟男" <wnchen@fudan.edu.cn>, "曹袖" <Xiucao@fudan.edu.cn>, "陈学青" <xqchen@fudan.edu.cn>, "陈阳" <chenyang@fudan.edu.cn>, "Chen" <yijiachen@fudan.edu.cn>, "陈雁秋" <chenyq@fudan.edu.cn>, "丁向华" <dingx@fudan.e> 
    subject: 本科教学评估材料上报 
    sentdate: 201814162458 
    receivedate: 20181416251
    
    第 78 封邮件： 
    id: 2:1tbiAgQIBFKpyHBu5wAAsA 
    from: "ResearchGate" <no-reply@researchgatemail.net> 
    to: "Chengrong Wu" <cwu@fudan.edu.cn> 
    subject: Chengrong, you were recently cited by an author from Universiti Putra Malaysia 
    sentdate: 201814144620 
    receivedate: 201814145137
    
    第 79 封邮件： 
    id: 1:1tbiAQEIBFKp0ruN0AABsC 
    from: "sfding" <dingsf@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: RE: [重要通知]关于网上评审2019春工程硕士论文的通知 
    sentdate: 201814144329 
    receivedate: 201814144330
    
    第 80 封邮件： 
    id: 1:1tbiAQcICFKp0ruLCwAAmU 
    from: "计算机学院工会" <cs_gonghui@fudan.edu.cn> 
    to: "汪 卫" <weiwang1@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 雪平" <wangxp@fudan.edu.cn>, "王 毅敏" <yiminwang@fudan.edu.cn>, "王" 
    subject: 2018年复旦大学教工象棋个人赛比赛通知及报名表 
    sentdate: 201814142151 
    receivedate: 201814142154
    
    第 81 封邮件： 
    id: 2:1tbiAgUIBFKpyHBoEgAAsy 
    from: "sfding" <dingsf@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: RE: [重要通知]关于网上评审2019春工程硕士论文的通知 
    sentdate: 201814141132 
    receivedate: 201814141133
    
    第 82 封邮件： 
    id: 1:1tbiAQIIBFKp0ruFvAAAmk 
    from: "gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn> 
    to: "吴承荣" <cwu@fudan.edu.cn> 
    subject: 回复: 下周二免推生面试网络空间安全学科的老师名单 
    sentdate: 20181413553 
    receivedate: 20181413555
    
    第 83 封邮件： 
    id: 1:1tbiAQYIBFKp0ruBEgABsL 
    from: "CCF会员部" <ccfmk@membership.ccf.org.cn> 
    to: cwu@fudan.edu.cn 
    subject: CCF邀请您一起壮大会员队伍 
    sentdate: 201814131721 
    receivedate: 201814133031
    
    第 84 封邮件： 
    id: 2:1tbiAgIIBFKpyHBaRQAAmQ 
    from: "wanghuimin" <wanghm@fudan.edu.cn> 
    to: "吴承荣" <cwu@fudan.edu.cn> 
    subject: 专项经费项目预算模板---9.14 
    sentdate: 201814125119 
    receivedate: 201814125120
    
    第 85 封邮件： 
    id: 2:1tbiAgEIBFKpyHBQaAAAs0 
    from: "上海市科学技术委员会" <infomail@newsletter.stcsm.gov.cn> 
    to: cwu@fudan.edu.cn 
    subject: 科技服务信息专递第四百五十三期 
    sentdate: 201814114116 
    receivedate: 20181411466
    
    第 86 封邮件： 
    id: 1:1tbiAQYIBFKp0rtXsAAFs7 
    from: lfjin@fudan.edu.cn 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: 下周二免推生面试，各位老师是否能够参加？ 
    sentdate: 201814112355 
    receivedate: 201814112356
    
    第 87 封邮件： 
    id: 1:1tbiAQYIBFKp0rtXsAAEs6 
    from: "复旦专利" <fudanzhuanli@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: HyperGuard云平台安全审计监管系统 
    sentdate: 20181410918 
    receivedate: 20181410920
    
    第 88 封邮件： 
    id: 1:1tbiAQYIBFKp0rtXsAACs8 
    from: "ResearchGate" <no-reply@researchgatemail.net> 
    to: "Chengrong Wu" <cwu@fudan.edu.cn> 
    subject: Chengrong, people are reading your work 
    sentdate: 20181494413 
    receivedate: 20181495131
    
    第 89 封邮件： 
    id: 2:1tbiAgQIAlKpyHA2sAAAmJ 
    from: "dingsf" <dingsf@fudan.edu.cn> 
    to: kydai@fudan.edu.cn, hwfeng@fudan.edu.cn, lijt@fudan.edu.cn, ylzhao@fudan.edu.cn, xuyx@fudan.edu.cn, chenc@fudan.edu.cn, chenrh@fudan.edu.cn, hbkan@fudan.edu.cn, cfsha@fudan.edu.cn, zjp@fudan.edu.cn, wdzhao@fudan.edu.cn, liy@fudan.edu.cn, yunx@fudan.edu.cn, limin@fudan.edu.cn, pengxin@fudan.edu.cn, zhengxq@fudan.ed 
    subject: [重要通知]关于网上评审2019春工程硕士论文的通知 
    sentdate: 20181494346 
    receivedate: 20181493859
    
    第 90 封邮件： 
    id: 2:1tbiAgQHBFKpyG-kEgAAsv 
    from: "ResearchGate" <no-reply@researchgatemail.net> 
    to: cwu@fudan.edu.cn 
    subject: Mostafa Alksher uploaded a full-text citing you 
    sentdate: 20181321235 
    receivedate: 201813213138
    
    第 91 封邮件： 
    id: 2:1tbiAggHDlKpyG-h5wAAmZ 
    from: "szhang" <szhang@fudan.edu.cn> 
    to: "Wu Jie" <jwu@fudan.edu.cn>, "cwu" <cwu@fudan.edu.cn>, "严明" <myan@fudan.edu.cn> 
    subject: Fw: 古河会长访问复旦行程表，solize公司中文介绍 
    sentdate: 201813211849 
    receivedate: 201813211856
    
    第 92 封邮件： 
    id: 2:1tbiAggHBFKpyG-YVgAAsb 
    from: "office" <office.journal46@rediffmail.com> 
    to: xujj@suda.edu.cn, zhengkai@suda.edu.cn, minzhang@suda.edu.cn, wangzh@hit.edu.cn, jwu@fudan.edu.cn, cwu@fudan.edu.cn, chenyanjiao@whu.edu.cn, yinxy@nwu.edu.cn, zhang.j4@sustc.edu.cn, gracelq628@hnu.edu.cn, yuhong.guo@careton.ca, csgjwang@gmail.com, ychencs@whu.edu.cn, 450867607@qq.com, xxxyczl@csu.edu.cn, pp960712@ 
    subject: Best Ranking Journal 
    sentdate: 20181320134 
    receivedate: 201813202527
    
    第 93 封邮件： 
    id: 1:1tbiAQEHBFKp0rr1wwABsn 
    from: "ResearchGate" <no-reply@researchgatemail.net> 
    to: cwu@fudan.edu.cn 
    subject: Congratulations Chengrong, you reached a milestone 
    sentdate: 201813201213 
    receivedate: 201813202135
    
    第 94 封邮件： 
    id: 1:1tbiAQEHBFKp0rr1wwAAsm 
    from: invitation@confcfp.org 
    to: cwu@fudan.edu.cn 
    subject: Invited speaker invitation to Wu, Chengrong 
    sentdate: 20181320137 
    receivedate: 20181320528
    
    第 95 封邮件： 
    id: 1:1tbiAQcHBFKp0rrDrAAAs5 
    from: "赵运磊" <ylzhao@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: 下周二免推生面试，各位老师是否能够参加？ 
    sentdate: 201813153249 
    receivedate: 201813153253
    
    第 96 封邮件： 
    id: 1:1tbiAQYHBFKp0rq+ngAAm3 
    from: "Min Yang" <m_yang@fudan.edu.cn> 
    to: "'cwu'" <cwu@fudan.edu.cn> 
    subject: RE: 下周二免推生面试，各位老师是否能够参加？ 
    sentdate: 201813151446 
    receivedate: 201813151448
    
    第 97 封邮件： 
    id: 1:1tbiAQkGBFKp0rpihAACs9 
    from: Hellen@mk.iceeep.org 
    to: cwu@fudan.edu.cn 
    subject: Forthcoming conference in November, 2018--Energy and Environment 
    sentdate: 20181381428 
    receivedate: 20181382056
    
    第 98 封邮件： 
    id: 2:1tbiAggGBFKpyG8GiQAAsb 
    from: "ZengJianping" <zjp@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: 下周二免推生面试，各位老师是否能够参加？ 
    sentdate: 201812212218 
    receivedate: 201812212225
    
    第 99 封邮件： 
    id: 1:1tbiAQcGBFKp0rogSAABs+ 
    from: "luzhihui" <lzh@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: 下周二免推生面试，各位老师是否能够参加？ 
    sentdate: 201812204753 
    receivedate: 201812204756
    
    第 100 封邮件： 
    id: 2:1tbiAggGBFKpyG79ugAAsS 
    from: "hbkan" <hbkan@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re:下周二免推生面试，各位老师是否能够参加？ 
    sentdate: 201812202534 
    receivedate: 20181220412
    
    第 101 封邮件： 
    id: 2:1tbiAgEGDlKpyG7TRgAAmD 
    from: "szhang" <szhang@fudan.edu.cn> 
    to: "Wu Jie" <jwu@fudan.edu.cn>, "cwu" <cwu@fudan.edu.cn>, "严明" <myan@fudan.edu.cn> 
    subject: Fw: Re: RE: Solize　Engineering 公司介绍 
    sentdate: 2018121718 
    receivedate: 20181217112
    
    第 102 封邮件： 
    id: 2:1tbiAgMGBlKpyG6+5gAAmE 
    from: dongling@fudan.edu.cn 
    to: xujiayin@fudan.edu.cn, sklge@fudan.edu.cn, wei_xu@fudan.edu.cn, wqlu@fudan.edu.cn, "沈莹" <math_research@fudan.edu.cn>, "王晓娟" <wangxiaojuan@fudan.edu.cn>, "张春艳" <zcy6250@163.com>, "zhaojiayuan" <zhaojiayuan@fudan.edu.cn>, "崔晓丽" <cpslab@fudan.edu.cn>, "李文静" <liwj@fudan.edu.cn>, "上海市现代应用数学重点实验室" <sklcam@fudan.edu> 
    subject: 转发: 关于开展《大学和科研机构开展科学传播活动现状调查》的函 
    sentdate: 20181215312 
    receivedate: 20181215317
    
    第 103 封邮件： 
    id: 2:1tbiAgMGDlKpyG67EwAAm8 
    from: "wmfu" <wmfu@fudan.edu.cn> 
    to: 18210240027@fudan.edu.cn, 18210240038@fudan.edu.cn, 18210240123@fudan.edu.cn, 18210240136@fudan.edu.cn, 18210240075@fudan.edu.cn, 18210240173@fudan.edu.cn, 18210240110@fudan.edu.cn, 18210240262@fudan.edu.cn, 18210240237@fudan.edu.cn, 18210240252@fudan.edu.cn, 18210240146@fudan.edu.cn, 18210240082@fudan.edu.cn 
    subject: 兹定于9月19日（周三）上午9时在逸夫楼407室，迎新2018级全体研究生，请课题组老师和2018级全体新生参加！NiSL-Sept-12-2018 
    sentdate: 20181215149 
    receivedate: 201812151414
    
    第 104 封邮件： 
    id: 1:1tbiAQEGCVKp0rm1NwAAmd 
    from: "计算机学院" <cs_school@fudan.edu.cn> 
    to: "汪 卫" <weiwang1@fudan.edu.cn>, "王 放" <fangwang@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 新" <xinw@fudan.edu.cn>, "王 雪平" <> 
    subject: 【重要通知】关于各项经费执行进度要求的通知 
    sentdate: 201812133736 
    receivedate: 201812133742
    
    第 105 封邮件： 
    id: 2:1tbiAgEGBFKpyG55tAABsQ 
    from: "LJQ" <jsgnljq@163.com> 
    to: "cwu@fudan.edu.cn" <cwu@fudan.edu.cn> 
    subject: IP地址跳变机制抗扫描能力评估3 
    sentdate: 201812114859 
    receivedate: 20181211491
    
    第 106 封邮件： 
    id: 2:1tbiAgEGBFKpyG55tAAAsR 
    from: "赵运磊" <ylzhao@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: FW: 教学团队设备采购注意事项 
    sentdate: 201812105630 
    receivedate: 201812105633
    
    第 107 封邮件： 
    id: 2:1tbiAggGB1KpyG54gQAAmv 
    from: "cs_keyan" <cs_keyan@fudan.edu.cn> 
    to: "谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud> 
    subject: Fw: 【项目申报】科技部关于发布国家重点研发计划“现代服务业共性关键技术研发及应用示范”重点专项2018年度定向项目申报指南的通知 
    sentdate: 201812105129 
    receivedate: 201812105130
    
    第 108 封邮件： 
    id: 2:1tbiAggGDlKpyG503QAAm2 
    from: "wmfu" <wmfu@fudan.edu.cn> 
    to: szhang@fudan.edu.cn, ypzhong@fudan.edu.cn, jwu@fudan.edu.cn, cwu@fudan.edu.cn, gpwang@fudan.edu.cn, jliang@fudan.edu.cn, lzh@fudan.edu.cn, zjp@fudan.edu.cn, jwye@fudan.edu.cn, myan@fudan.edu.cn, wmfu@fudan.edu.cn 
    subject: 通信学会通知：Fw: 转发: Fw:学术年会论文交流安排 
    sentdate: 201812103457 
    receivedate: 20181210350
    
    第 109 封邮件： 
    id: 1:1tbiAQcGDFKp0rmJ0QAAmE 
    from: "Yang Weidong" <yweidong@gmail.com> 
    to: "xuxiaoyin" <xuxiaoyin@fudan.edu.cn> 
    subject: Re: 关于申请新金博研究用房的请示 
    sentdate: 201812101317 
    receivedate: 201812101333
    
    第 110 封邮件： 
    id: 2:1tbiAgIGB1KpyG5jyAAAm3 
    from: "cs_keyan" <cs_keyan@fudan.edu.cn> 
    to: "谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud> 
    subject: Fw: 科技部基础研究中心张峰处长报告通知 
    sentdate: 20181291812 
    receivedate: 20181291812
    
    第 111 封邮件： 
    id: 2:1tbiAggFBFKpyG5F6wACs6 
    from: Alisa@mk.icmeie.com 
    to: cwu@fudan.edu.cn 
    subject: IOP出版+EI&CPCI检索，第二届 机械、电子和工业工程国际学术会议-邀请函- Lu, ZH 
    sentdate: 20181251059 
    receivedate: 2018125113
    
    第 112 封邮件： 
    id: 1:1tbiAQUFBFKp0rlecQAAs6 
    from: "julie-zhu" <sjtu-julie@sjtu.edu.cn> 
    to: cwu@fudan.edu.cn 
    subject: 上海交大高教院课题组诚邀您参与高校科研人才评价政策认同情况调查 
    sentdate: 20181244927 
    receivedate: 20181245147
    
    第 113 封邮件： 
    id: 1:1tbiAQcFBFKp0rkOegAAmj 
    from: "xuxiaoyin" <xuxiaoyin@fudan.edu.cn> 
    to: "Yang Weidong" <yweidong@gmail.com> 
    subject: Re: 关于申请新金博研究用房的请示 
    sentdate: 20181118851 
    receivedate: 20181118854
    
    第 114 封邮件： 
    id: 1:1tbiAQEFBFKp0rj9rAAAsB 
    from: "赵运磊" <ylzhao@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: FW: 教学团队设备采购注意事项 
    sentdate: 201811164734 
    receivedate: 201811164741
    
    第 115 封邮件： 
    id: 2:1tbiAgIFBFKpyG3jWwAAsn 
    from: "晓春肖" <xxiaochun@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: 教学团队设备采购注意事项 
    sentdate: 201811163748 
    receivedate: 201811163751
    
    第 116 封邮件： 
    id: 1:1tbiAQgFDlKp0rj36QAAmN 
    from: "szhang" <szhang@fudan.edu.cn> 
    to: "Wu Jie" <jwu@fudan.edu.cn>, "严明" <myan@fudan.edu.cn>, "cwu" <cwu@fudan.edu.cn> 
    subject: Fw: Solize　Engineering 公司介绍 
    sentdate: 20181116267 
    receivedate: 201811162617
    
    第 117 封邮件： 
    id: 1:1tbiAQgFCVKp0rj2nQAAm- 
    from: "gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn> 
    to: "汪卫" <weiwang1@fudan.edu.cn>, "黄萱菁" <xjhuang@fudan.edu.cn>, "张亮" <lzhang@fudan.edu.cn>, "张玥杰" <yjzhang@fudan.edu.cn>, "吴承荣" <cwu@fudan.edu.cn>, "唐志强" <zqtang@fudan.edu.cn>, "张建国" <jgzhang@fudan.edu.cn>, "张向东" <zxd@fudan.edu.cn> 
    subject: 教学团队设备采购注意事项 
    sentdate: 201811161955 
    receivedate: 201811161955
    
    第 118 封邮件： 
    id: 2:1tbiAggFBlKpyG3I0AAAmP 
    from: "沈建蓉" <jrshen@fudan.edu.cn> 
    to: "曹袖" <xiucao@fudan.edu.cn>, "陈辰" <chenc@fudan.edu.cn>, "陈荣华" <chenrh@fudan.edu.cn>, "陈伟男" <wnchen@fudan.edu.cn>, "陈学青" <xqchen@fudan.edu.cn>, "陈雁秋" <chenyq@fudan.edu.cn>, "陈阳" <chenyang@fudan.edu.cn>, "陈翌佳" <yijiachen@fudan.edu.cn>, "池明旻" <mmchi@fudan.edu.cn>, "kydai" <kydai@fudan.edu.cn>, "丁向华" <dingx@fudan.> 
    subject: 硕士论文学院预审 
    sentdate: 201811144611 
    receivedate: 20181114455
    
    第 119 封邮件： 
    id: 1:1tbiAQcFAlKp0rjR1gAAmX 
    from: "dingsf" <dingsf@fudan.edu.cn> 
    to: kydai@fudan.edu.cn, hwfeng@fudan.edu.cn, lijt@fudan.edu.cn, ylzhao@fudan.edu.cn, xuyx@fudan.edu.cn, chenc@fudan.edu.cn, chenrh@fudan.edu.cn, hbkan@fudan.edu.cn, cfsha@fudan.edu.cn, zjp@fudan.edu.cn, wdzhao@fudan.edu.cn, liy@fudan.edu.cn, yunx@fudan.edu.cn, limin@fudan.edu.cn, pengxin@fudan.edu.cn, zhengxq@fudan.ed 
    subject: 关于邀请您参加在职工程硕士论文评审的通知 
    sentdate: 201811134638 
    receivedate: 201811134152
    
    第 120 封邮件： 
    id: 1:1tbiAQQFBFKp0riRowACsl 
    from: Ms_wu0521@mk.febm.org 
    to: cwu@fudan.edu.cn 
    subject: 经管--FEBM2018—内蒙古.呼和浩特 
    sentdate: 20181195823 
    receivedate: 20181110153
    
    第 121 封邮件： 
    id: 2:1tbiAggEBFKpyG1QEgABsX 
    from: "Frontiers Oncology Editorial Office" <oncology.editorial.office@frontiersin.org> 
    to: cwu@fudan.edu.cn 
    subject: Frontiers: Your manuscript submission - 421127 
    sentdate: 201810232130 
    receivedate: 201810233135
    
    第 122 封邮件： 
    id: 2:1tbiAggEBFKpyG1QEgAAsW 
    from: "Online Submissions" <noreply@indersciencemail.com> 
    to: "Zhanwei Cui" <zwcui14@fudan.edu.cn>, "Jianping Zeng" <zjp@fudan.edu.cn>, "Chengrong Wu" <cwu@fudan.edu.cn>, "Prof. Dr. Eldon Y. Li" <eli@calpoly.edu> 
    subject: Editorial Review Notification - IJICS_160328 
    sentdate: 201810231836 
    receivedate: 201810232522
    
    第 123 封邮件： 
    id: 1:1tbiAQYEBFKp0rg7DgAAsj 
    from: Yang@mk.ssphe.org 
    to: cwu@fudan.edu.cn 
    subject: Conference on Social Science, Education and Humanities Research-三亚-11.25-27 
    sentdate: 201810192053 
    receivedate: 201810192058
    
    第 124 封邮件： 
    id: 2:1tbiAgUEBFKpyGz+0QABs2 
    from: "夏毅" <18210240217@fudan.edu.cn> 
    to: "吴承荣老师" <cwu@fudan.edu.cn> 
    subject: 新生工作会议安排确认 
    sentdate: 201810164624 
    receivedate: 201810164634
    
    第 125 封邮件： 
    id: 2:1tbiAggEBFKpyGza9wACs6 
    from: "jsgnljq" <jsgnljq@163.com> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: 回复：RE: 本周三研究生工作安排会议 
    sentdate: 201810151546 
    receivedate: 201810151549
    
    第 126 封邮件： 
    id: 2:1tbiAgUEBFKpyGz+0QAAs3 
    from: "Zhou, Huijing (WorldQuant)" <Huijing.Zhou@worldquant.com> 
    to: "'cwu@fudan.edu.cn'" <cwu@fudan.edu.cn> 
    subject: WorldQuant 世坤咨询（北京）有限公司 2018-2019年度秋季招聘 
    sentdate: 20181015320 
    receivedate: 201810154938
    
    第 127 封邮件： 
    id: 2:1tbiAggEBFKpyGza9wABs5 
    from: "陈蕾" <chenlei@hzbook.com> 
    to: Cwu@fudan.edu.cn 
    subject: 教师节快乐—机械工业出版社华章分社陈蕾 
    sentdate: 20181011824 
    receivedate: 20181013828
    
    第 128 封邮件： 
    id: 2:1tbiAggECFKpyGy-UwAAm1 
    from: "wmfu" <wmfu@fudan.edu.cn> 
    to: 18210240027@fudan.edu.cn, 18210240038@fudan.edu.cn, 18210240123@fudan.edu.cn, 18210240136@fudan.edu.cn, 18210240075@fudan.edu.cn, 18210240173@fudan.edu.cn, 18210240110@fudan.edu.cn, 18210240262@fudan.edu.cn, 18210240237@fudan.edu.cn, 18210240252@fudan.edu.cn, 18210240146@fudan.edu.cn, 18210240082@fudan.edu.cn 
    subject: 转发讲座通知： 明天11(日）上午9点40分讲座（详见邮件网址）在逸夫楼407， 望大家准时参加！祝新学期快乐、进步！NiSL-傅维明 
    sentdate: 20181010393 
    receivedate: 201810103914
    
    第 129 封邮件： 
    id: 1:1tbiAQIEBFKp0rfEDAAAsV 
    from: "余莉萍" <17210240022@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re:RE: RE: RE: 来自下学期《信息安全导论》课程助教 
    sentdate: 201810101134 
    receivedate: 201810101144
    
    第 130 封邮件： 
    id: 2:1tbiAgQDBFKpyGyWdgABs- 
    from: "jsgnljq" <jsgnljq@163.com> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: 祝吴老师教师节快乐 
    sentdate: 2018108336 
    receivedate: 20181083311
    
    第 131 封邮件： 
    id: 1:1tbiAQYJCVKp0rdA6gAAbz 
    from: "FDU Security" <security@fudan.edu.cn> 
    to: security@fudan.edu.cn 
    subject: 恶意邮件警报：电子邮件包含“Unable to/Cannot show/display this message”消息 
    sentdate: 20189144523 
    receivedate: 20189175642
    
    第 132 封邮件： 
    id: 2:1tbiAgEDBFKpyGwyjgAAsn 
    from: "余莉萍" <17210240022@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: RE: RE: 来自下学期《信息安全导论》课程助教 
    sentdate: 20189132958 
    receivedate: 2018913301
    
    第 133 封邮件： 
    id: 2:1tbiAgIDDFKpyGwn-AAAmL 
    from: "wanghuimin" <wanghm@fudan.edu.cn> 
    to: "许晓茵" <xuxiaoyin@fudan.edu.cn>, "王晓阳" <xywangcs@fudan.edu.cn>, "薛向阳" <xyxue@fudan.edu.cn>, "吴杰" <jwu@fudan.edu.cn>, "吴承荣" <cwu@fudan.edu.cn>, "张世永" <szhang@fudan.edu.cn>, "叶家炜" <jwye@fudan.edu.cn> 
    subject: 保密学院班子会通知 
    sentdate: 20189122658 
    receivedate: 2018912272
    
    第 134 封邮件： 
    id: 2:1tbiAgcDBFKpyGv88AADsV 
    from: "孙玉齐" <16300240013@fudan.edu.cn> 
    to: cwu@fudan.edu.cn 
    subject: Re: 来自"孙玉齐" <16300240013@fudan.edu.cn>的邮件 
    sentdate: 20189103637 
    receivedate: 20189103931
    
    第 135 封邮件： 
    id: 2:1tbiAgcDBFKpyGv88AABsX 
    from: "jwye@fudan.edu.cn" <jwye@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: 云审计截图 
    sentdate: 2018910852 
    receivedate: 2018910853
    
    第 136 封邮件： 
    id: 1:1tbiAQMCBFKp0rbmUQACsu 
    from: "郝建伟" <hjw_cmpbook@126.com> 
    to: cwu@fudan.edu.cn 
    subject: 祝您教师节快乐！-机械工业出版社郝建伟  
    sentdate: 20189900 
    receivedate: 20189926
    
    第 137 封邮件： 
    id: 2:1tbiAgECBFKpyGu-2AABs7 
    from: "linda jane" <antomes1758@gmail.com> 
    to:  
    subject: Fwd: 主题：2018年9月7日星期五 ……【周末快乐！】 
    sentdate: 2018904157 
    receivedate: 2018911534
    
    第 138 封邮件： 
    id: 1:1tbiAQUCBFKp0raqvwAAsI 
    from: "ResearchGate" <no-reply@researchgatemail.net> 
    to: cwu@fudan.edu.cn 
    subject: A researcher is following your updates on ResearchGate 
    sentdate: 20188155339 
    receivedate: 2018816147
    
    第 139 封邮件： 
    id: 1:1tbiAQYCBFKp0ralfAAAmH 
    from: "Yang Weidong" <yweidong@gmail.com> 
    to: "薛 向阳" <xyxue@fudan.edu.cn>, "王晓阳X. Sean Wang" <xywangCS@fudan.edu.cn>, "吴 承荣" <cwu@fudan.edu.cn>, "xuxiaoyin" <xuxiaoyin@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn> 
    subject: Re: 关于申请新金博研究用房的请示 
    sentdate: 20188151014 
    receivedate: 20188151029
    
    第 140 封邮件： 
    id: 1:1tbiAQgCBFKp0raitgAAsE 
    from: "Yang Weidong" <yweidong@gmail.com> 
    to: "吴 承荣" <cwu@fudan.edu.cn> 
    subject: Re: 关于申请新金博研究用房的请示 
    sentdate: 20188144741 
    receivedate: 20188144755
    
    第 141 封邮件： 
    id: 1:1tbiAQYCDlKp0raLfwAAmg 
    from: "何加林" <czhejialin@163.com> 
    to: caoyu@fudan.edu.cn, xiucao@fudan.edu.cn, mmchi@fudan.edu.cn, wnchen@fudan.edu.cn, chenlf@fudan.edu.cn, xqchen@fudan.edu.cn, tbchen@fudan.edu.cn, bhchen@fudan.edu.cn, yijiachen@fudan.edu.cn, chenrh@fudan.edu.cn, chenc@fudan.edu.cn, chenyq@fudan.edu.cn, dingx@fudan.edu.cn, dingsf@fudan.edu.cn, kydai@fudan.edu.cn, fu 
    subject: 《电与磁的理论缺陷》 
    sentdate: 2018893932 
    receivedate: 20188102632
    
    第 142 封邮件： 
    id: 1:1tbiAQUBBFKp0rZZ+wABs9 
    from: iwmsme2018@mail.iwmsme.org 
    to: cwu@fudan.edu.cn 
    subject: Good papers are welcome to submit to IWMSME2018 and published by IOP conference series 
    sentdate: 2018841739 
    receivedate: 2018842439
    
    第 143 封邮件： 
    id: 1:1tbiAQYBBFKp0rZRuwAAm3 
    from: "Yang Weidong" <yweidong@gmail.com> 
    to: "薛 向阳" <xyxue@fudan.edu.cn>, "王晓阳X. Sean Wang" <xywangCS@fudan.edu.cn>, "吴 承荣" <cwu@fudan.edu.cn>, "xuxiaoyin" <xuxiaoyin@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn> 
    subject: 关于申请新金博研究用房的请示 
    sentdate: 2018722426 
    receivedate: 20187224231
    
    第 144 封邮件： 
    id: 1:1tbiAQQBBFKp0rYHhQAAsd 
    from: "匡翔宇" <xykuang16@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: RE: 匡翔宇的论文初稿 烦请吴老师审阅 
    sentdate: 2018715645 
    receivedate: 2018715646
    
    第 145 封邮件： 
    id: 2:1tbiAgEBBFKpyGr3UQABs4 
    from: "宋昊" <16210240081@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: RE: 论文 (0904) 
    sentdate: 20187142322 
    receivedate: 20187142325
    
    第 146 封邮件： 
    id: 2:1tbiAgEBBFKpyGr3UQAAs5 
    from: "luzhihui" <lzh@fudan.edu.cn> 
    to: "吴承荣" <cwu@fudan.edu.cn> 
    subject: 沙箱简介 
    sentdate: 2018714941 
    receivedate: 2018714945
    
    第 147 封邮件： 
    id: 1:1tbiAQYBCFKp0rXulQAAmp 
    from: "wmfu" <wmfu@fudan.edu.cn> 
    to: "Gao Qiyuan" <GQQQy@outlook.com> 
    subject: Re: Fw:【研究生推免】 
    sentdate: 20187131630 
    receivedate: 20187131631
    
    第 148 封邮件： 
    id: 2:1tbiAgcBDlKpyGrdeQAAm3 
    from: "计算机学院工会" <cs_gonghui@fudan.edu.cn> 
    to: "汪 卫" <weiwang1@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 雪平" <wangxp@fudan.edu.cn>, "王 毅敏" <yiminwang@fudan.edu.cn>, "王" 
    subject: 教师着装礼仪及基础搭配讲座通知 
    sentdate: 2018712528 
    receivedate: 2018712530
    
    第 149 封邮件： 
    id: 1:1tbiAQYBBFKp0rXMHQABsO 
    from: "上海市科学技术委员会" <infomail@newsletter.stcsm.gov.cn> 
    to: cwu@fudan.edu.cn 
    subject: 科技服务信息专递第四百五十二期 
    sentdate: 20187113333 
    receivedate: 20187113911
    
    第 150 封邮件： 
    id: 1:1tbiAQMBBFKp0rXJXAAAsO 
    from: "携程旅行网" <recommend@lists4.ctrip.com> 
    to: cwu@fudan.edu.cn 
    subject: 恭喜您获赠1950元国家周超值大礼包！更有五折神券限时抢 
    sentdate: 20187105021 
    receivedate: 2018710569
    
    第 151 封邮件： 
    id: 2:1tbiAggBBFKpyGqwQgACsm 
    from: "ResearchGate" <no-reply@researchgatemail.net> 
    to: "Chengrong Wu" <cwu@fudan.edu.cn> 
    subject: Chengrong, you have 1 more citation 
    sentdate: 2018794036 
    receivedate: 2018794631
    
    第 152 封邮件： 
    id: 2:1tbiAgQABFKpyGpmTwABsz 
    from: "匡翔宇" <xykuang16@fudan.edu.cn> 
    to: cwu@fudan.edu.cn 
    subject: 匡翔宇的论文初稿 烦请吴老师审阅 
    sentdate: 2018623646 
    receivedate: 2018623649
    
    第 153 封邮件： 
    id: 2:1tbiAgQABFKpyGpmTwAAsy 
    from: "higo@FDU" <lijiading@fudan.edu.cn> 
    to: cwu@fudan.edu.cn 
    subject: 学院2018年迎新大会邀请函 
    sentdate: 20186213636 
    receivedate: 20186213638
    
    第 154 封邮件： 
    id: 1:1tbiAQMABFKp0rVl8gAAsN 
    from: "ResearchGate" <no-reply@researchgatemail.net> 
    to: cwu@fudan.edu.cn 
    subject: Amir Herzberg, an author you cited, uploaded a full-text to: Introduction to Cyber-Security, Part I: Applied Cryptography... 
    sentdate: 20186211336 
    receivedate: 20186212125
    
    第 155 封邮件： 
    id: 2:1tbiAgcABFKpyGogWgAEsm 
    from: "Gao Qiyuan" <GQQQy@outlook.com> 
    to: "cwu@fudan.edu.cn" <cwu@fudan.edu.cn> 
    subject: 【研究生推免】 
    sentdate: 20186185334 
    receivedate: 20186185341
    
    第 156 封邮件： 
    id: 2:1tbiAgcABFKpyGogWgABsj 
    from: "CCF会员部" <membership@ccf.org.cn> 
    to: cwu@fudan.edu.cn 
    subject: 温馨提醒：第7、8期《中国计算机学会通讯》已于8月28日陆续寄出 
    sentdate: 2018615333 
    receivedate: 20186151723
    
    第 157 封邮件： 
    id: 2:1tbiAgkABFKpyGn4tAAAsZ 
    from: "LJQ" <jsgnljq@163.com> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re:RE: Re:回复：RE: 关于地址跳变机制抗扫描能力的评估论文需要9月10日投出 
    sentdate: 2018611428 
    receivedate: 2018611430
    
    第 158 封邮件： 
    id: 2:1tbiAgcACVKpyGnx-gAAmZ 
    from: "计算机学院" <cs_school@fudan.edu.cn> 
    to: "汪 卫" <weiwang1@fudan.edu.cn>, "王 放" <fangwang@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 新" <xinw@fudan.edu.cn>, "王 雪平" <> 
    subject: 学院迎新大会 
    sentdate: 2018610313 
    receivedate: 2018610315
    
    第 159 封邮件： 
    id: 2:1tbiAgcAB1KpyGnoIQAAmR 
    from: "cs_keyan" <cs_keyan@fudan.edu.cn> 
    to: "谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud> 
    subject: 转发: 关于转发8月若干国家自然科学基金委项目指南的通知 
    sentdate: 201869459 
    receivedate: 201869458
    
    第 160 封邮件： 
    id: 1:1tbiAQgAB1Kp0rTmXwAAmq 
    from: "cs_keyan" <cs_keyan@fudan.edu.cn> 
    to: "谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud> 
    subject: Fw: 【指南征求意见】关于对科技创新2030—“新一代人工智能”重大项目 2018年度项目申报指南征求意见的通知 
    sentdate: 2018692739 
    receivedate: 2018692737
    
    第 161 封邮件： 
    id: 2:1tbiAgITBFKpyGm77gAAsY 
    from: "Zhang Shiyong via ResearchGate" <no-reply@researchgatemail.net> 
    to: cwu@fudan.edu.cn 
    subject: Zhang Shiyong thinks you're the author of this publication 
    sentdate: 201861447 
    receivedate: 2018611133
    
    第 162 封邮件： 
    id: 2:1tbiAgUTB1KpyGljTwAAml 
    from: "cs_keyan" <cs_keyan@fudan.edu.cn> 
    to: "谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud> 
    subject: 关于第一届 “先进计算与防御技术” 学术会议 
    sentdate: 20185142937 
    receivedate: 20185142937
    
    第 163 封邮件： 
    id: 2:1tbiAgQTBFKpyGlV0wABsM 
    from: "LJQ" <jsgnljq@163.com> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re:Re:回复：RE: 关于地址跳变机制抗扫描能力的评估论文需要9月10日投出 
    sentdate: 20185142845 
    receivedate: 20185142848
    
    第 164 封邮件： 
    id: 2:1tbiAggTBFKpyGk5nAABsj 
    from: "cgjh" <cgjh@fudan.edu.cn> 
    to: "吴承荣" <cwu@fudan.edu.cn> 
    subject: 关于国家公派留学成果统计的通知 
    sentdate: 2018510590 
    receivedate: 20185105910
    
    第 165 封邮件： 
    id: 2:1tbiAggTBFKpyGk5nAAAsi 
    from: "gongjie@fudan.edu.cn" <gongjie@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: 回复: RE: 本科上课通知 
    sentdate: 20185101256 
    receivedate: 20185101255
    
    第 166 封邮件： 
    id: 2:1tbiAgkTB1KpyGk3CwAAm5 
    from: "cs_keyan" <cs_keyan@fudan.edu.cn> 
    to: "谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud> 
    subject: Fw: 【紧急】各院系教师在国际机构及期刊任职情况汇总 
    sentdate: 2018510142 
    receivedate: 2018510142
    
    第 167 封邮件： 
    id: 1:1tbiAQUTBFKp0rQ3fAAAsF 
    from: "朱迅" <17210240029@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: RE: RE: 关于18-19学年《网络攻击与防御技术》课程助教的工作 
    sentdate: 201851010 
    receivedate: 201851012
    
    第 168 封邮件： 
    id: 1:1tbiAQETE1Kp0rQ3HQAAm3 
    from: "wanghuimin" <wanghm@fudan.edu.cn> 
    to: "吴承荣" <cwu@fudan.edu.cn> 
    subject: Fw: 多媒体设备拆迁费用清单 
    sentdate: 2018595918 
    receivedate: 2018595920
    
    第 169 封邮件： 
    id: 2:1tbiAgITBFKpyGkuSwABsp 
    from: "余莉萍" <17210240022@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: RE: RE: 来自下学期《信息安全导论》课程助教 
    sentdate: 201859499 
    receivedate: 2018594911
    
    第 170 封邮件： 
    id: 1:1tbiAQgSBFKp0rQWgQACsX 
    from: "meiyi ma" <mm5tk@virginia.edu> 
    to: cwu@fudan.edu.cn 
    subject: Invitation to submit your work to 2018 Safethings 
    sentdate: 2018562236 
    receivedate: 201856299
    
    第 171 封邮件： 
    id: 1:1tbiAQgSBFKp0rQIiwAAsB 
    from: "ResearchGate" <no-reply@researchgatemail.net> 
    to: "Chengrong Wu" <cwu@fudan.edu.cn> 
    subject: Chengrong, we found new jobs you may be interested in 
    sentdate: 201851733 
    receivedate: 2018511628
    
    第 172 封邮件： 
    id: 1:1tbiAQESBFKp0rPHfAAAs3 
    from: "赵瑜" <15307130435@fudan.edu.cn> 
    to: cwu@fudan.edu.cn 
    subject: Re:RE: 关于推免生专业和方向的疑问 
    sentdate: 2018417927 
    receivedate: 2018417929
    
    第 173 封邮件： 
    id: 1:1tbiAQkSBFKp0rO85AAAsc 
    from: "ZengJianping" <zjp@fudan.edu.cn> 
    to: cwu@fudan.edu.cn 
    subject: 拟态项目下半年工作总结 
    sentdate: 20184162118 
    receivedate: 20184162120
    
    第 174 封邮件： 
    id: 1:1tbiAQYSDlKp0rOw9QAAmE 
    from: "计算机学院工会" <cs_gonghui@fudan.edu.cn> 
    to: "汪 卫" <weiwang1@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 雪平" <wangxp@fudan.edu.cn>, "王 毅敏" <yiminwang@fudan.edu.cn>, "王" 
    subject: 上海市教育工会提供义务法律咨询 及 中国农业银行致敬教师校园行活动 的通知 
    sentdate: 2018415265 
    receivedate: 2018415268
    
    第 175 封邮件： 
    id: 2:1tbiAggSDlKpyGiQvwAAmi 
    from: "wmfu" <wmfu@fudan.edu.cn> 
    to: 16210240043@fudan.edu.cn, 16210240045@fudan.edu.cn, 16210240049@fudan.edu.cn, 16210240064@fudan.edu.cn, 16210240067@fudan.edu.cn, 16210240081@fudan.edu.cn, 16210240090@fudan.edu.cn, 16110240017@fudan.edu.cn, 16110240004@fudan.edu.cn, 16210240069@fudan.edu.cn, 17210240057@fudan.edu.cn, 17210240261@fudan.edu.cn 
    subject: 提醒：本周五9月7日学院注册－上周通知有误，以近日学院邮件通知为准，特此更正，望大家准时注册！9月7日上午9:00~11:00和下午13:00~16:00准时前来注册，注册地点：张江校区计算机学院院办104室。 
    sentdate: 20184121442 
    receivedate: 20184121444
    
    第 176 封邮件： 
    id: 1:1tbiAQYSCFKp0rOPMQAAm5 
    from: "wmfu" <wmfu@fudan.edu.cn> 
    to: "夏毅" <18210240217@fudan.edu.cn> 
    subject: Re: 新生实验室报道 
    sentdate: 20184115949 
    receivedate: 20184115950
    
    第 177 封邮件： 
    id: 2:1tbiAgYSBFKpyGh+iwAAs8 
    from: "宋昊" <16210240081@fudan.edu.cn> 
    to: "吴承荣" <cwu@fudan.edu.cn> 
    subject: 论文 (0904) 
    sentdate: 20184103315 
    receivedate: 20184103318
    
    第 178 封邮件： 
    id: 1:1tbiAQgSBFKp0rN+twAAsM 
    from: "朱迅" <17210240029@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: RE: 关于18-19学年《网络攻击与防御技术》课程助教的工作 
    sentdate: 20184103256 
    receivedate: 20184103257
    
    第 179 封邮件： 
    id: 2:1tbiAggSBFKpyGh6FQAAso 
    from: "余莉萍" <17210240022@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: RE: 来自下学期《信息安全导论》课程助教 
    sentdate: 2018410955 
    receivedate: 2018410956
    
    第 180 封邮件： 
    id: 1:1tbiAQcSDFKp0rNtgAAAmv 
    from: "曹瑜" <caoyu@fudan.edu.cn> 
    to: "厉家鼎" <lijiading@fudan.edu.cn>, "彭 鑫" <pengxin@fudan.edu.cn>, "汪 卫" <weiwang1@fudan.edu.cn>, "王 晓阳" <xywangCS@fudan.edu.cn>, "吴 杰" <jwu@fudan.edu.cn>, "许晓茵" <xuxiaoyin@fudan.edu.cn>, "薛 向阳" <xyxue@fudan.edu.cn>, "张 玥杰" <yjzhang@fudan.edu.cn>, "赵 一鸣" <zhym@fudan.edu.cn>, "朱 扬勇" <yyzhu@fudan.edu.cn>, "张向东" <xdz> 
    subject: 【邯郸校区，周五上午9点】学院新学期工作会议通知 
    sentdate: 201849811 
    receivedate: 201849812
    
    第 181 封邮件： 
    id: 1:1tbiAQMSB1Kp0rNsrgAAmP 
    from: "cs_keyan" <cs_keyan@fudan.edu.cn> 
    to: "谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud> 
    subject: Fw: 关于珠海复旦创新研究院项目征集的通知（预申报截止日期：9月14日） 
    sentdate: 201849425 
    receivedate: 201849425
    
    第 182 封邮件： 
    id: 2:1tbiAgQRBFKpyGgvkwABs1 
    from: "赵瑜" <15307130435@fudan.edu.cn> 
    to: cwu@fudan.edu.cn 
    subject: Re: 关于推免生专业和方向的疑问 
    sentdate: 201840025 
    receivedate: 201840029
    
    第 183 封邮件： 
    id: 2:1tbiAgURBFKpyGgpmQAAs5 
    from: "jsgnljq" <jsgnljq@163.com> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: 回复：Re:回复：RE: 关于地址跳变机制抗扫描能力的评估论文需要9月10日投出 
    sentdate: 2018320318 
    receivedate: 2018320322
    
    第 184 封邮件： 
    id: 2:1tbiAgURDlKpyGgWPAAAmp 
    from: "szhang" <szhang@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Fw:  Re: 教育部工程中心评估PPT与答辩回执 
    sentdate: 20183174830 
    receivedate: 20183174835
    
    第 185 封邮件： 
    id: 1:1tbiAQURDlKp0rMR3AAAmM 
    from: "szhang" <szhang@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject:  Re: 教育部工程中心评估PPT与答辩回执 
    sentdate: 20183171057 
    receivedate: 20183171059
    
    第 186 封邮件： 
    id: 1:1tbiAQIRB1Kp0rMJBAAAmC 
    from: "cs_keyan" <cs_keyan@fudan.edu.cn> 
    to: "谈子敬" <zjtan@fudan.edu.cn>, "陶晓鹏" <xptao@fudan.edu.cn>, "汪卫" <weiwang1@fudan.edu.cn>, "王飞" <wangfei@fudan.edu.cn>, "王欢" <wanghuan@fudan.edu.cn>, "王鹏" <pengwang5@fudan.edu.cn>, "王新" <xinw@fudan.edu.cn>, "王雪平" <wangxp@fudan.edu.cn>, "王智慧" <zhhwang@fudan.edu.cn>, "王轶彤" <yitongw@fudan.edu.cn>, "王晓阳" <xywangCS@fud> 
    subject: Fw: 图书馆 中科2018年07-08期外文新书目 
    sentdate: 20183162748 
    receivedate: 20183162753
    
    第 187 封邮件： 
    id: 2:1tbiAgcRCFKpyGgBuAAAm+ 
    from: "wmfu" <wmfu@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: RE: Re: Re: 统计KBH2301132/003项目的研究生经费发放 
    sentdate: 20183161342 
    receivedate: 20183161343
    
    第 188 封邮件： 
    id: 2:1tbiAgERCVKpyGf3TwAAm3 
    from: "计算机学院" <cs_school@fudan.edu.cn> 
    to: "汪 卫" <weiwang1@fudan.edu.cn>, "王 放" <fangwang@fudan.edu.cn>, "王 飞" <wangfei@fudan.edu.cn>, "王 国平" <gpwang@fudan.edu.cn>, "王 欢" <wanghuan@fudan.edu.cn>, "王慧敏" <wanghm@fudan.edu.cn>, "王 李霞" <wanglx@fudan.edu.cn>, "王 鹏" <pengwang5@fudan.edu.cn>, "王晓阳" <xywangCS@fudan.edu.cn>, "王 新" <xinw@fudan.edu.cn>, "王 雪平" <> 
    subject: 关于开展2018-2019年度教师公寓复审与租赁协议续签工作的通知 
    sentdate: 20183155336 
    receivedate: 20183155339
    
    第 189 封邮件： 
    id: 1:1tbiAQURBFKp0rLqIAABsB 
    from: "周荃" <16210240049@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: RE: 关于地址跳变机制抗扫描能力的评估论文需要9月10日投出 
    sentdate: 20183155332 
    receivedate: 20183155333
    
    第 190 封邮件： 
    id: 2:1tbiAggRCFKpyGfeTgAAmX 
    from: "wmfu" <wmfu@fudan.edu.cn> 
    to: cwu@fudan.edu.cn 
    subject: Re: Re: Re: 统计KBH2301132/003项目的研究生经费发放 
    sentdate: 20183143838 
    receivedate: 20183143839
    
    第 191 封邮件： 
    id: 1:1tbiAQMRDlKp0rLfogAAm7 
    from: "szhang" <szhang@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Fw: Re: 教育部工程中心评估PPT与答辩回执 
    sentdate: 2018314374 
    receivedate: 2018314376
    
    第 192 封邮件： 
    id: 2:1tbiAgQRBFKpyGfdigABsR 
    from: "jsgnljq" <jsgnljq@163.com> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: 回复：RE: 关于地址跳变机制抗扫描能力的评估论文需要9月10日投出 
    sentdate: 20183143446 
    receivedate: 20183143449
    
    第 193 封邮件： 
    id: 1:1tbiAQgRCFKp0rLZVAAAmG 
    from: "wmfu" <wmfu@fudan.edu.cn> 
    to: "wmfu" <wmfu@fudan.edu.cn> 
    subject: Re: Re: 统计KBH2301132/003项目的研究生经费发放 
    sentdate: 2018314315 
    receivedate: 2018314318
    
    第 194 封邮件： 
    id: 1:1tbiAQYRBFKp0rLU4wAAs+ 
    from: "wmfu" <wmfu@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: 统计KBH2301132/003项目的研究生经费发放 
    sentdate: 20183133917 
    receivedate: 20183133918
    
    第 195 封邮件： 
    id: 2:1tbiAggRBFKpyGe8xwACsy 
    from: "赵瑜" <15307130435@fudan.edu.cn> 
    to: cwu@fudan.edu.cn 
    subject: Re: 关于推免生专业和方向的疑问 
    sentdate: 20183123817 
    receivedate: 20183123819
    
    第 196 封邮件： 
    id: 2:1tbiAggRBFKpyGe8xwAAsw 
    from: "Computers & Security" <EviseSupport@elsevier.com> 
    to: cwu@fudan.edu.cn 
    subject: Your co-authored submission 
    sentdate: 2018311927 
    receivedate: 20183111353
    
    第 197 封邮件： 
    id: 2:1tbiAggRDlKpyGe1hwAAmz 
    from: "szhang" <szhang@fudan.edu.cn> 
    to: "cwu" <cwu@fudan.edu.cn> 
    subject: Re: 教育部工程中心评估PPT与答辩回执 
    sentdate: 20183103713 
    receivedate: 20183103716
    
    第 198 封邮件： 
    id: 1:1tbiAQYRDFKp0rKgtgAAmX 
    from: "曹瑜" <caoyu@fudan.edu.cn> 
    to: "厉家鼎" <lijiading@fudan.edu.cn>, "彭 鑫" <pengxin@fudan.edu.cn>, "汪 卫" <weiwang1@fudan.edu.cn>, "王 晓阳" <xywangCS@fudan.edu.cn>, "吴 杰" <jwu@fudan.edu.cn>, "许晓茵" <xuxiaoyin@fudan.edu.cn>, "薛 向阳" <xyxue@fudan.edu.cn>, "张 玥杰" <yjzhang@fudan.edu.cn>, "赵 一鸣" <zhym@fudan.edu.cn>, "朱 扬勇" <yyzhu@fudan.edu.cn>, "张向东" <xdz> 
    subject: 【会议预通知】新学期工作会议预通知 
    sentdate: 201839290 
    receivedate: 201839291
    
    第 199 封邮件： 
    id: 2:1tbiAggQBFKpyGdrFwAAs2 
    from: "赵瑜" <15307130435@fudan.edu.cn> 
    to: cwu@fudan.edu.cn 
    subject: 关于推免生专业和方向的疑问 
    sentdate: 20182223951 
    receivedate: 20182223953
    
    第 200 封邮件： 
    id: 1:1tbiAQYQBFKp0rJpHgAAs- 
    from: "Jie Wu" <jwu@fudan.edu.cn> 
    to: "'cwu'" <cwu@fudan.edu.cn> 
    subject:  
    sentdate: 20182221327 
    receivedate: 20182221228
    
    邮箱的邮件列表中总共有 200 封邮件



```python
contractInfo = [{
'id':'154',
'groups':[],
'EMAIL;PREF':'ypzhong@fudan.edu.cn',
'FN':'\'ypzhong\'',
'rev':67},
{
'id':'40',
'groups':[],
'EMAIL;PREF':'caoyu@fudan.edu.cn',
'FN':'\'曹瑜\'',
'rev':15},
{
'id':'34',
'groups':[],
'EMAIL;PREF':'cns@fudan.edu.cn',
'FN':'\'复旦大学国家保密学院\'',
'rev':15},
{
'id':'35',
'groups':[],
'EMAIL;PREF':'jqma@fudan.edu.cn',
'FN':'\'马 建庆\'',
'rev':15},
{
'id':'38',
'groups':[],
'EMAIL;PREF':'sunxiaoxia@fudan.edu.cn',
'FN':'\'孙笑侠\'',
'rev':15},
{
'id':'39',
'groups':[],
'EMAIL;PREF':'wanghm@fudan.edu.cn',
'FN':'\'王慧敏\'',
'rev':15},
{
'id':'37',
'groups':[],
'EMAIL;PREF':'xywangCS@fudan.edu.cn',
'FN':'\'王晓阳\'',
'rev':15},
{
'id':'36',
'groups':[],
'EMAIL;PREF':'xyxue@fudan.edu.cn',
'FN':'\'薛向阳\'',
'rev':15},
{
'id':'32',
'groups':[],
'EMAIL;PREF':'12307130381@fudan.edu.cn',
'FN':'12307130381',
'rev':14},
{
'id':'30',
'groups':[],
'EMAIL;PREF':'13210240012@fudan.edu.cn',
'FN':'13210240012',
'rev':12},
{
'id':'61',
'groups':[],
'EMAIL;PREF':'13300240001@fudan.edu.cn',
'FN':'13300240001',
'rev':30},
{
'id':'62',
'groups':[],
'EMAIL;PREF':'13300240002@fudan.edu.cn',
'FN':'13300240002',
'rev':30},
{
'id':'63',
'groups':[],
'EMAIL;PREF':'13300240004@fudan.edu.cn',
'FN':'13300240004',
'rev':30},
{
'id':'64',
'groups':[],
'EMAIL;PREF':'13300240006@fudan.edu.cn',
'FN':'13300240006',
'rev':30},
{
'id':'65',
'groups':[],
'EMAIL;PREF':'13300240007@fudan.edu.cn',
'FN':'13300240007',
'rev':30},
{
'id':'66',
'groups':[],
'EMAIL;PREF':'13300240008@fudan.edu.cn',
'FN':'13300240008',
'rev':30},
{
'id':'67',
'groups':[],
'EMAIL;PREF':'13300240009@fudan.edu.cn',
'FN':'13300240009',
'rev':30},
{
'id':'68',
'groups':[],
'EMAIL;PREF':'13300240010@fudan.edu.cn',
'FN':'13300240010',
'rev':30},
{
'id':'69',
'groups':[],
'EMAIL;PREF':'13300240011@fudan.edu.cn',
'FN':'13300240011',
'rev':30},
{
'id':'70',
'groups':[],
'EMAIL;PREF':'13300240012@fudan.edu.cn',
'FN':'13300240012',
'rev':30},
{
'id':'71',
'groups':[],
'EMAIL;PREF':'13300240014@fudan.edu.cn',
'FN':'13300240014',
'rev':30},
{
'id':'72',
'groups':[],
'EMAIL;PREF':'13300240015@fudan.edu.cn',
'FN':'13300240015',
'rev':30},
{
'id':'73',
'groups':[],
'EMAIL;PREF':'13300240016@fudan.edu.cn',
'FN':'13300240016',
'rev':30},
{
'id':'74',
'groups':[],
'EMAIL;PREF':'13300240017@fudan.edu.cn',
'FN':'13300240017',
'rev':30},
{
'id':'75',
'groups':[],
'EMAIL;PREF':'13300240018@fudan.edu.cn',
'FN':'13300240018',
'rev':30},
{
'id':'76',
'groups':[],
'EMAIL;PREF':'13300240019@fudan.edu.cn',
'FN':'13300240019',
'rev':30},
{
'id':'77',
'groups':[],
'EMAIL;PREF':'13300240020@fudan.edu.cn',
'FN':'13300240020',
'rev':30},
{
'id':'78',
'groups':[],
'EMAIL;PREF':'13300240021@fudan.edu.cn',
'FN':'13300240021',
'rev':30},
{
'id':'79',
'groups':[],
'EMAIL;PREF':'13300240022@fudan.edu.cn',
'FN':'13300240022',
'rev':30},
{
'id':'80',
'groups':[],
'EMAIL;PREF':'13300240023@fudan.edu.cn',
'FN':'13300240023',
'rev':30},
{
'id':'81',
'groups':[],
'EMAIL;PREF':'13300240024@fudan.edu.cn',
'FN':'13300240024',
'rev':30},
{
'id':'82',
'groups':[],
'EMAIL;PREF':'13300240025@fudan.edu.cn',
'FN':'13300240025',
'rev':30},
{
'id':'83',
'groups':[],
'EMAIL;PREF':'13307130027@fudan.edu.cn',
'FN':'13307130027',
'rev':30},
{
'id':'84',
'groups':[],
'EMAIL;PREF':'13307130046@fudan.edu.cn',
'FN':'13307130046',
'rev':30},
{
'id':'85',
'groups':[],
'EMAIL;PREF':'13307130058@fudan.edu.cn',
'FN':'13307130058',
'rev':30},
{
'id':'86',
'groups':[],
'EMAIL;PREF':'13307130084@fudan.edu.cn',
'FN':'13307130084',
'rev':30},
{
'id':'87',
'groups':[],
'EMAIL;PREF':'13307130085@fudan.edu.cn',
'FN':'13307130085',
'rev':30},
{
'id':'88',
'groups':[],
'EMAIL;PREF':'13307130086@fudan.edu.cn',
'FN':'13307130086',
'rev':30},
{
'id':'89',
'groups':[],
'EMAIL;PREF':'13307130100@fudan.edu.cn',
'FN':'13307130100',
'rev':30},
{
'id':'90',
'groups':[],
'EMAIL;PREF':'13307130107@fudan.edu.cn',
'FN':'13307130107',
'rev':30},
{
'id':'91',
'groups':[],
'EMAIL;PREF':'13307130120@fudan.edu.cn',
'FN':'13307130120',
'rev':30},
{
'id':'92',
'groups':[],
'EMAIL;PREF':'13307130137@fudan.edu.cn',
'FN':'13307130137',
'rev':30},
{
'id':'93',
'groups':[],
'EMAIL;PREF':'13307130140@fudan.edu.cn',
'FN':'13307130140',
'rev':30},
{
'id':'94',
'groups':[],
'EMAIL;PREF':'13307130159@fudan.edu.cn',
'FN':'13307130159',
'rev':30},
{
'id':'95',
'groups':[],
'EMAIL;PREF':'13307130161@fudan.edu.cn',
'FN':'13307130161',
'rev':30},
{
'id':'96',
'groups':[],
'EMAIL;PREF':'13307130170@fudan.edu.cn',
'FN':'13307130170',
'rev':30},
{
'id':'97',
'groups':[],
'EMAIL;PREF':'13307130195@fudan.edu.cn',
'FN':'13307130195',
'rev':30},
{
'id':'98',
'groups':[],
'EMAIL;PREF':'13307130199@fudan.edu.cn',
'FN':'13307130199',
'rev':30},
{
'id':'99',
'groups':[],
'EMAIL;PREF':'13307130267@fudan.edu.cn',
'FN':'13307130267',
'rev':30},
{
'id':'100',
'groups':[],
'EMAIL;PREF':'13307130268@fudan.edu.cn',
'FN':'13307130268',
'rev':30},
{
'id':'101',
'groups':[],
'EMAIL;PREF':'13307130294@fudan.edu.cn',
'FN':'13307130294',
'rev':30},
{
'id':'102',
'groups':[],
'EMAIL;PREF':'13307130327@fudan.edu.cn',
'FN':'13307130327',
'rev':30},
{
'id':'103',
'groups':[],
'EMAIL;PREF':'13307130342@fudan.edu.cn',
'FN':'13307130342',
'rev':30},
{
'id':'104',
'groups':[],
'EMAIL;PREF':'13307130363@fudan.edu.cn',
'FN':'13307130363',
'rev':30},
{
'id':'105',
'groups':[],
'EMAIL;PREF':'13307130364@fudan.edu.cn',
'FN':'13307130364',
'rev':30},
{
'id':'106',
'groups':[],
'EMAIL;PREF':'13307130370@fudan.edu.cn',
'FN':'13307130370',
'rev':30},
{
'id':'107',
'groups':[],
'EMAIL;PREF':'13307130384@fudan.edu.cn',
'FN':'13307130384',
'rev':30},
{
'id':'108',
'groups':[],
'EMAIL;PREF':'13307130396@fudan.edu.cn',
'FN':'13307130396',
'rev':30},
{
'id':'109',
'groups':[],
'EMAIL;PREF':'13307130410@fudan.edu.cn',
'FN':'13307130410',
'rev':30},
{
'id':'110',
'groups':[],
'EMAIL;PREF':'13307130428@fudan.edu.cn',
'FN':'13307130428',
'rev':30},
{
'id':'111',
'groups':[],
'EMAIL;PREF':'13307130446@fudan.edu.cn',
'FN':'13307130446',
'rev':30},
{
'id':'112',
'groups':[],
'EMAIL;PREF':'13307130475@fudan.edu.cn',
'FN':'13307130475',
'rev':30},
{
'id':'113',
'groups':[],
'EMAIL;PREF':'13307130491@fudan.edu.cn',
'FN':'13307130491',
'rev':30},
{
'id':'114',
'groups':[],
'EMAIL;PREF':'13307130501@fudan.edu.cn',
'FN':'13307130501',
'rev':30},
{
'id':'115',
'groups':[],
'EMAIL;PREF':'13307130525@fudan.edu.cn',
'FN':'13307130525',
'rev':30},
{
'id':'116',
'groups':[],
'EMAIL;PREF':'13307130533@fudan.edu.cn',
'FN':'13307130533',
'rev':30},
{
'id':'127',
'groups':[],
'EMAIL;PREF':'13601927008@sina.cn',
'FN':'13601927008',
'rev':40},
{
'id':'45',
'groups':[],
'EMAIL;PREF':'13601927008m0@sina.cn',
'FN':'13601927008m0',
'rev':20},
{
'id':'42',
'groups':[],
'EMAIL;PREF':'14307130046@fudan.edu.cn',
'FN':'14307130046',
'rev':17},
{
'id':'41',
'groups':[],
'EMAIL;PREF':'14307130064@fudan.edu.cn',
'FN':'14307130064',
'rev':16},
{
'id':'117',
'groups':[],
'EMAIL;PREF':'14307130291@fudan.edu.cn',
'FN':'14307130291',
'rev':30},
{
'id':'118',
'groups':[],
'EMAIL;PREF':'14307130298@fudan.edu.cn',
'FN':'14307130298',
'rev':30},
{
'id':'264',
'groups':[],
'EMAIL;PREF':'574419684@qq.com',
'FN':'574419684',
'rev':100},
{
'id':'247',
'groups':[],
'EMAIL;PREF':'ya45@drexel.edu',
'FN':'An,Yuan',
'rev':83},
{
'id':'131',
'groups':[],
'EMAIL;PREF':'annexian@163.com',
'FN':'annexian',
'rev':44},
{
'id':'160',
'groups':[],
'EMAIL;PREF':'baggage@sina.com',
'FN':'baggage',
'rev':73},
{
'id':'142',
'groups':[],
'EMAIL;PREF':'bkg@pku.edu.cn',
'FN':'bkg',
'rev':55},
{
'id':'130',
'groups':[],
'EMAIL;PREF':'southpoint01002@gmail.com',
'FN':'Bonnie Ainslie',
'rev':43},
{
'id':'161',
'groups':[],
'EMAIL;PREF':'ccf-internet@cernet.edu.cn',
'FN':'ccf-internet@cernet.edu.cn',
'rev':74},
{
'id':'51',
'groups':[],
'EMAIL;PREF':'cfyuan@nju.edu.cn',
'FN':'cfyuan',
'rev':23},
{
'id':'241',
'groups':[],
'EMAIL;PREF':'cgjh@fudan.edu.cn',
'FN':'cgjh',
'rev':77},
{
'id':'266',
'groups':[],
'EMAIL;PREF':'chaxin@fudan.edu.cn',
'FN':'chaxin',
'rev':102},
{
'id':'256',
'groups':[],
'EMAIL;PREF':'chyp@e-neurons.net',
'FN':'chyp@e-neurons.net',
'rev':92},
{
'id':'21',
'groups':[],
'EMAIL;PREF':'13162516735@126.com',
'FN':'cjsypei',
'rev':3},
{
'id':'268',
'groups':[],
'EMAIL;PREF':'cs211@fudan.edu.cn',
'FN':'cs211',
'rev':104},
{
'id':'7',
'groups':[],
'EMAIL;PREF':'cwu@fudan.edu.cn',
'FN':'cwu',
'rev':0},
{
'id':'137',
'groups':[],
'EMAIL;PREF':'Donna.Coombs.1@city.ac.uk',
'FN':'Donna.Coombs.1',
'rev':50},
{
'id':'28',
'groups':[],
'EMAIL;PREF':'support_japanican@gmt.jtb.jp',
'FN':'e路東瀛_JAPANiCAN',
'rev':10},
{
'id':'123',
'groups':[],
'EMAIL;PREF':'kongfanchen1994@gmail.com',
'FN':'Fanchen Kong',
'rev':35},
{
'id':'5',
'groups':[],
'EMAIL;PREF':'fdcit@fudan.edu.cn',
'FN':'fdcitfdcit',
'rev':0},
{
'id':'15',
'groups':[],
'EMAIL;PREF':'fhxu@fudan.edu.cn',
'FN':'fhxu',
'rev':0},
{
'id':'245',
'groups':[],
'EMAIL;PREF':'globesat88@aol.com',
'FN':'globesat88',
'rev':81},
{
'id':'59',
'groups':[],
'EMAIL;PREF':'gongjie@fudan.edu.cn',
'FN':'gongjie@fudan.edu.cn',
'rev':28},
{
'id':'2',
'groups':[],
'EMAIL;PREF':'gpwang@fudan.edu.cn',
'FN':'gpwang',
'rev':0},
{
'id':'22',
'groups':[],
'EMAIL;PREF':'guhaihua@sjtu.edu.cn',
'FN':'guhaihua',
'rev':4},
{
'id':'52',
'groups':[],
'EMAIL;PREF':'hanfei@hep.com.cn',
'FN':'hanfei',
'rev':23},
{
'id':'270',
'groups':[],
'EMAIL;PREF':'hbkan@fudan.edu.cn',
'FN':'hbkan',
'rev':106},
{
'id':'135',
'groups':[],
'EMAIL;PREF':'hljin14@fudan.edu.cn',
'FN':'hljin14@fudan.edu.cn',
'rev':48},
{
'id':'1',
'groups':[],
'EMAIL;PREF':'sailh@263.net',
'FN':'Huang Sheng Hua',
'rev':0},
{
'id':'149',
'groups':[],
'EMAIL;PREF':'jane.yang@ebaotech.com',
'FN':'Jane Yang',
'rev':62},
{
'id':'12',
'groups':[],
'EMAIL;PREF':'jaykee0906@hotmail.com',
'FN':'jaykee0906',
'rev':0},
{
'id':'244',
'groups':[],
'EMAIL;PREF':'jiangxuejinny@gmail.com',
'FN':'jiangxuejin',
'rev':80},
{
'id':'4',
'groups':[],
'EMAIL;PREF':'jliao@fudan.edu.cn',
'FN':'jliao',
'rev':0},
{
'id':'6',
'groups':[],
'EMAIL;PREF':'jwu@fudan.edu.cn',
'FN':'jwu',
'rev':0},
{
'id':'13',
'groups':[],
'EMAIL;PREF':'jwye@fudan.edu.cn',
'FN':'jwye',
'rev':0},
{
'id':'153',
'groups':[],
'EMAIL;PREF':'jxyj@fudan.edu.cn',
'FN':'jxyj',
'rev':66},
{
'id':'133',
'groups':[],
'EMAIL;PREF':'kjrobert144@gmail.com',
'FN':'Kyle Robert',
'rev':46},
{
'id':'138',
'groups':[],
'EMAIL;PREF':'lgsok@163.com',
'FN':'lgs',
'rev':51},
{
'id':'125',
'groups':[],
'EMAIL;PREF':'li_jp@fudan.edu.cn',
'FN':'li_jp',
'rev':38},
{
'id':'50',
'groups':[],
'EMAIL;PREF':'liuwd@mail.tsinghua.edu.cn',
'FN':'liuwd',
'rev':23},
{
'id':'263',
'groups':[],
'EMAIL;PREF':'jsgnljq@163.com',
'FN':'LJQ',
'rev':99},
{
'id':'47',
'groups':['FRIENDS'],
'EMAIL;PREF':'ljl@pku.edu.cn',
'FN':'Lu Junlin',
'rev':22},
{
'id':'139',
'groups':[],
'EMAIL;PREF':'lzh@fudan.edu.cn',
'FN':'luzhihui',
'rev':52},
{
'id':'49',
'groups':[],
'EMAIL;PREF':'lzhang@fudan.edu.cn',
'FN':'lzhang',
'rev':23},
{
'id':'10',
'groups':[],
'EMAIL;PREF':'myan@fudan.edu.cn',
'FN':'myan',
'rev':0},
{
'id':'55',
'groups':[],
'EMAIL;PREF':'myan@fuda.edu.cn',
'FN':'myan',
'rev':25},
{
'id':'19',
'groups':[],
'EMAIL;PREF':'qiandavid1991@gmail.com',
'FN':'qiandavid1991',
'rev':1},
{
'id':'57',
'groups':[],
'EMAIL;PREF':'xueshen@fudan.edu.cn',
'FN':'Sara Xue',
'rev':27},
{
'id':'16',
'groups':[],
'EMAIL;PREF':'sea_bull825169@sina.com',
'FN':'sea_bull825169',
'rev':0},
{
'id':'11',
'groups':[],
'EMAIL;PREF':'shfei@fudan.edu.cn',
'FN':'shfei',
'rev':0},
{
'id':'29',
'groups':[],
'EMAIL;PREF':'sjxcwu@163.com',
'FN':'sjxcwu',
'rev':11},
{
'id':'126',
'groups':[],
'EMAIL;PREF':'sjxcwu@139.com',
'FN':'sjxcwu',
'rev':39},
{
'id':'141',
'groups':[],
'EMAIL;PREF':'sjxcwu@yahoo.com.cn',
'FN':'sjxcwu',
'rev':54},
{
'id':'14',
'groups':[],
'EMAIL;PREF':'szhang@fudan.edu.cn',
'FN':'szhang',
'rev':0},
{
'id':'260',
'groups':[],
'EMAIL;PREF':'wangxq261@126.com',
'FN':'wangxq261',
'rev':96},
{
'id':'269',
'groups':[],
'EMAIL;PREF':'wdyang@fudan.edu.cn',
'FN':'wdyang',
'rev':105},
{
'id':'157',
'groups':[],
'EMAIL;PREF':'weiwang1@fudan.edu.cn',
'FN':'weiwang1',
'rev':70},
{
'id':'134',
'groups':[],
'EMAIL;PREF':'wlhan@fudan.edu.cn',
'FN':'wlhan',
'rev':47},
{
'id':'9',
'groups':[],
'EMAIL;PREF':'wmfu@fudan.edu.cn',
'FN':'wmfu',
'rev':0},
{
'id':'155',
'groups':[],
'EMAIL;PREF':'wuhongmei2727@126.com',
'FN':'wuhongmei2727',
'rev':68},
{
'id':'132',
'groups':[],
'EMAIL;PREF':'xujn@fudan.edu.cn',
'FN':'xujn',
'rev':45},
{
'id':'33',
'groups':[],
'EMAIL;PREF':'xuxiaoyin@fudan.edu.cn',
'FN':'xuxiaoyin',
'rev':15},
{
'id':'152',
'groups':[],
'EMAIL;PREF':'xyjiang@fudan.edu.cn',
'FN':'xyjiang',
'rev':65},
{
'id':'140',
'groups':[],
'EMAIL;PREF':'xzyao@fudan.edu.cn',
'FN':'xzyao',
'rev':53},
{
'id':'267',
'groups':[],
'EMAIL;PREF':'yweidong@gmail.com',
'FN':'Yang Weidong',
'rev':103},
{
'id':'259',
'groups':[],
'EMAIL;PREF':'ylzhao@fudan.edu.cn',
'FN':'ylzhao',
'rev':95},
{
'id':'248',
'groups':[],
'EMAIL;PREF':'yuan.an@drexel.edu',
'FN':'yuan.an',
'rev':84},
{
'id':'44',
'groups':[],
'EMAIL;PREF':'yuanxzhang@fudan.edu.cn',
'FN':'Yuan Zhang',
'rev':19},
{
'id':'159',
'groups':[],
'EMAIL;PREF':'yudm1215@hotmail.com',
'FN':'Yu Dongmei',
'rev':72},
{
'id':'255',
'groups':[],
'EMAIL;PREF':'zhang_li@fudan.edu.cn',
'FN':'Zhang Li',
'rev':91},
{
'id':'53',
'groups':[],
'EMAIL;PREF':'zhanglong@139.com',
'FN':'zhanglong',
'rev':23},
{
'id':'43',
'groups':[],
'EMAIL;PREF':'yangzhemin@fudan.edu.cn',
'FN':'Zhemin Yang',
'rev':18},
{
'id':'144',
'groups':[],
'EMAIL;PREF':'zhouj@cnas.org.cn',
'FN':'zhouj',
'rev':57},
{
'id':'60',
'groups':[],
'EMAIL;PREF':'zhudl@fudan.edu.cn',
'FN':'zhudl',
'rev':29},
{
'id':'3',
'groups':[],
'EMAIL;PREF':'zjp@fudan.edu.cn',
'FN':'zjp',
'rev':0},
{
'id':'8',
'groups':[],
'EMAIL;PREF':'zytian@gmail.com',
'FN':'zytian',
'rev':0},
{
'id':'27',
'groups':[],
'EMAIL;PREF':'11300240002@fudan.edu.cn',
'FN':'蔡一晓',
'rev':9},
{
'id':'253',
'groups':[],
'EMAIL;PREF':'15210240003@fudan.edu.cn',
'FN':'蔡一晓',
'rev':89},
{
'id':'23',
'groups':[],
'EMAIL;PREF':'chenc@fudan.edu.cn',
'FN':'陈 辰',
'rev':5},
{
'id':'46',
'groups':[],
'EMAIL;PREF':'13503827650@139.com',
'FN':'陈福才',
'rev':21},
{
'id':'128',
'groups':[],
'EMAIL;PREF':'qychen13@fudan.edu.cn',
'FN':'陈秋羽',
'rev':41},
{
'id':'58',
'groups':[],
'EMAIL;PREF':'chenrh@fudan.edu.cn',
'FN':'陈荣华',
'rev':27},
{
'id':'136',
'groups':[],
'EMAIL;PREF':'daisj518@163.com',
'FN':'袋鼠',
'rev':49},
{
'id':'239',
'groups':[],
'EMAIL;PREF':'dongyun@shxd.com',
'FN':'董贇',
'rev':75},
{
'id':'147',
'groups':[],
'EMAIL;PREF':'14300240007@fudan.edu.cn',
'FN':'胡天晓',
'rev':60},
{
'id':'252',
'groups':[],
'EMAIL;PREF':'cs_dangban@fudan.edu.cn',
'FN':'计算机科学技术学院党办',
'rev':88},
{
'id':'129',
'groups':[],
'EMAIL;PREF':'cs_school@fudan.edu.cn',
'FN':'计算机学院',
'rev':42},
{
'id':'257',
'groups':[],
'EMAIL;PREF':'cs_gonghui@fudan.edu.cn',
'FN':'计算机学院工会',
'rev':93},
{
'id':'20',
'groups':[],
'EMAIL;PREF':'cs_keyan@fudan.edu.cn',
'FN':'计算机学院科研',
'rev':2},
{
'id':'120',
'groups':[],
'EMAIL;PREF':'cs_renshi@fudan.edu.cn',
'FN':'计算机学院人事',
'rev':32},
{
'id':'54',
'groups':[],
'EMAIL;PREF':'13307130028@fudan.edu.cn',
'FN':'江信舟',
'rev':24},
{
'id':'254',
'groups':[],
'EMAIL;PREF':'jinmingli@fudan.edu.cn',
'FN':'李金明',
'rev':90},
{
'id':'164',
'groups':[],
'EMAIL;PREF':'leeying@mail.hust.edu.cn',
'FN':'李芝棠',
'rev':74},
{
'id':'162',
'groups':[],
'EMAIL;PREF':'zcli@ict.ac.cn',
'FN':'李忠诚',
'rev':74},
{
'id':'148',
'groups':[],
'EMAIL;PREF':'14307130203@fudan.edu.cn',
'FN':'林俊雄',
'rev':61},
{
'id':'158',
'groups':[],
'EMAIL;PREF':'liusq@sheitc.gov.cn',
'FN':'刘山泉',
'rev':71},
{
'id':'145',
'groups':[],
'EMAIL;PREF':'14210240047@fudan.edu.cn',
'FN':'刘巍',
'rev':58},
{
'id':'163',
'groups':[],
'EMAIL;PREF':'lzp@hbu.edu.cn',
'FN':'刘振鹏',
'rev':74},
{
'id':'165',
'groups':[],
'EMAIL;PREF':'zyliu@ict.ac.cn',
'FN':'刘志勇',
'rev':74},
{
'id':'26',
'groups':[],
'EMAIL;PREF':'11300240085@fudan.edu.cn',
'FN':'卢源',
'rev':8},
{
'id':'169',
'groups':[],
'EMAIL;PREF':'mayan@bupt.edu.cn',
'FN':'马严',
'rev':74},
{
'id':'166',
'groups':[],
'EMAIL;PREF':'mah@pku.edu.cn',
'FN':'马皓',
'rev':74},
{
'id':'167',
'groups':[],
'EMAIL;PREF':'mengkurt@bistu.edu.cn',
'FN':'孟坤',
'rev':74},
{
'id':'168',
'groups':[],
'EMAIL;PREF':'lmmeng@bupt.edu.cn',
'FN':'孟洛明',
'rev':74},
{
'id':'171',
'groups':[],
'EMAIL;PREF':'depeiq@buaa.edu.cn',
'FN':'钱德沛',
'rev':74},
{
'id':'172',
'groups':[],
'EMAIL;PREF':'qfl@sdu.edu.cn',
'FN':'秦丰林',
'rev':74},
{
'id':'48',
'groups':[],
'EMAIL;PREF':'lhqin@hust.edu.cn',
'FN':'秦磊华',
'rev':23},
{
'id':'170',
'groups':[],
'EMAIL;PREF':'yichengqu@caecc.com',
'FN':'曲成义',
'rev':74},
{
'id':'249',
'groups':[],
'EMAIL;PREF':'jrshen@fudan.edu.cn',
'FN':'沈建蓉',
'rev':85},
{
'id':'175',
'groups':[],
'EMAIL;PREF':'shenmeng@bit.edu.cn',
'FN':'沈蒙',
'rev':74},
{
'id':'0',
'groups':[],
'EMAIL;PREF':'syj@stcsm.gov.cn',
'FN':'沈蕴婕',
'rev':0},
{
'id':'146',
'groups':[],
'EMAIL;PREF':'shimin@sheitc.gov.cn',
'FN':'施敏',
'rev':59},
{
'id':'24',
'groups':[],
'EMAIL;PREF':'fsong@sei.ecnu.edu.cn',
'FN':'宋富',
'rev':6},
{
'id':'119',
'groups':[],
'EMAIL;PREF':'16210240081@fudan.edu.cn',
'FN':'宋昊',
'rev':31},
{
'id':'173',
'groups':[],
'EMAIL;PREF':'birchsu@139.com',
'FN':'苏金树',
'rev':74},
{
'id':'174',
'groups':[],
'EMAIL;PREF':'sunlimin@iie.ac.cn',
'FN':'孙利民',
'rev':74},
{
'id':'176',
'groups':[],
'EMAIL;PREF':'sunyi@ict.ac.cn',
'FN':'孙毅',
'rev':74},
{
'id':'177',
'groups':[],
'EMAIL;PREF':'sunzhigang@263.net',
'FN':'孙志刚',
'rev':74},
{
'id':'31',
'groups':[],
'EMAIL;PREF':'13381259551@163.com',
'FN':'唐',
'rev':13},
{
'id':'180',
'groups':[],
'EMAIL;PREF':'worldgulit@uestc.edu.cn',
'FN':'唐勇',
'rev':74},
{
'id':'179',
'groups':[],
'EMAIL;PREF':'juntao@seu.edu.cn',
'FN':'陶军',
'rev':74},
{
'id':'178',
'groups':[],
'EMAIL;PREF':'htian@hqu.edu.cn',
'FN':'田晖',
'rev':74},
{
'id':'240',
'groups':[],
'EMAIL;PREF':'zchliao@fudan.edu.cn',
'FN':'同事-廖志成',
'rev':76},
{
'id':'194',
'groups':[],
'EMAIL;PREF':'wangwy@uestc.edu.cn',
'FN':'汪文勇',
'rev':74},
{
'id':'271',
'groups':[],
'EMAIL;PREF':'17210240209@fudan.edu.cn',
'FN':'汪钰颖',
'rev':107},
{
'id':'18',
'groups':[],
'EMAIL;PREF':'11210240111@fudan.edu.cn',
'FN':'王川',
'rev':0},
{
'id':'181',
'groups':[],
'EMAIL;PREF':'freeloam@gmail.com',
'FN':'王丹',
'rev':74},
{
'id':'251',
'groups':[],
'EMAIL;PREF':'14300240005@fudan.edu.cn',
'FN':'王定鑫',
'rev':87},
{
'id':'182',
'groups':[],
'EMAIL;PREF':'wangd01@gmail.com',
'FN':'王栋',
'rev':74},
{
'id':'184',
'groups':[],
'EMAIL;PREF':'wanghua@sdu.edu.cn',
'FN':'王华',
'rev':74},
{
'id':'185',
'groups':[],
'EMAIL;PREF':'whm_w@163.com',
'FN':'王怀民',
'rev':74},
{
'id':'189',
'groups':[],
'EMAIL;PREF':'jxwang@mail.csu.edu.cn',
'FN':'王建新',
'rev':74},
{
'id':'186',
'groups':[],
'EMAIL;PREF':'wjin1985@suda.edu.cn',
'FN':'王进',
'rev':74},
{
'id':'188',
'groups':[],
'EMAIL;PREF':'jswang@tjut.edu.cn',
'FN':'王劲松',
'rev':74},
{
'id':'191',
'groups':[],
'EMAIL;PREF':'mwwang@jxnu.edu.cn',
'FN':'王明文',
'rev':74},
{
'id':'124',
'groups':['FRIENDS'],
'EMAIL;PREF':'13801111946@139.com',
'FN':'王旗',
'TEL;CELL;VOICE':'13801111946',
'rev':37},
{
'id':'193',
'groups':[],
'EMAIL;PREF':'wdwang@bupt.edu.cn',
'FN':'王文东',
'rev':74},
{
'id':'197',
'groups':[],
'EMAIL;PREF':'xfwang.nudt@gmail.com',
'FN':'王小峰',
'rev':74},
{
'id':'195',
'groups':[],
'EMAIL;PREF':'xinw@fudan.edu.cn',
'FN':'王新',
'rev':74},
{
'id':'196',
'groups':[],
'EMAIL;PREF':'xwang8@sjtu.edu.cn',
'FN':'王新兵',
'rev':74},
{
'id':'198',
'groups':[],
'EMAIL;PREF':'wangxw@mail.neu.edu.cn',
'FN':'王兴伟',
'rev':74},
{
'id':'199',
'groups':[],
'EMAIL;PREF':'wang@guet.edu.cn',
'FN':'王勇',
'rev':74},
{
'id':'200',
'groups':[],
'EMAIL;PREF':'zzdxwyan@126.com',
'FN':'王嫣',
'rev':74},
{
'id':'192',
'groups':[],
'EMAIL;PREF':'weiwei@xaut.edu.cn',
'FN':'魏嵬',
'rev':74},
{
'id':'201',
'groups':[],
'EMAIL;PREF':'wenyy@neusoft.com',
'FN':'闻英友',
'rev':74},
{
'id':'183',
'groups':[],
'EMAIL;PREF':'fwu@cs.sjtu.edu.cn',
'FN':'吴帆',
'rev':74},
{
'id':'187',
'groups':[],
'EMAIL;PREF':'jianping@cernet.edu.cn',
'FN':'吴建平',
'rev':74},
{
'id':'190',
'groups':[],
'EMAIL;PREF':'wu@whu.edu.cn',
'FN':'吴黎兵',
'rev':74},
{
'id':'121',
'groups':[],
'EMAIL;PREF':'16210240043@fudan.edu.cn',
'FN':'吴子彦',
'rev':33},
{
'id':'202',
'groups':[],
'EMAIL;PREF':'Xch@buaa.edu.cn',
'FN':'夏春和',
'rev':74},
{
'id':'262',
'groups':[],
'EMAIL;PREF':'13307110174@fudan.edu.cn',
'FN':'夏毅',
'rev':98},
{
'id':'250',
'groups':[],
'EMAIL;PREF':'1131662457@qq.com',
'FN':'响',
'rev':86},
{
'id':'214',
'groups':[],
'EMAIL;PREF':'xiangyz@digitalchina.com',
'FN':'向阳朝',
'rev':74},
{
'id':'213',
'groups':[],
'EMAIL;PREF':'jcxiang@uestc.edu.cn',
'FN':'向渝',
'rev':74},
{
'id':'205',
'groups':[],
'EMAIL;PREF':'newducky@126.com',
'FN':'肖国荣',
'rev':74},
{
'id':'210',
'groups':[],
'EMAIL;PREF':'xiaory@nsfc.gov.cn',
'FN':'肖人毅',
'rev':74},
{
'id':'203',
'groups':[],
'EMAIL;PREF':'Xiedl@bupt.edu.cn',
'FN':'谢东亮',
'rev':74},
{
'id':'204',
'groups':[],
'EMAIL;PREF':'xie@ict.ac.cn',
'FN':'谢高岗',
'rev':74},
{
'id':'209',
'groups':[],
'EMAIL;PREF':'sh@sjtu.edu.cn',
'FN':'谢锐',
'rev':74},
{
'id':'211',
'groups':[],
'EMAIL;PREF':'sharriexie@163.com',
'FN':'谢晓燕',
'rev':74},
{
'id':'207',
'groups':[],
'EMAIL;PREF':'xiekun@hnu.edu.cn',
'FN':'谢鲲',
'rev':74},
{
'id':'246',
'groups':[],
'EMAIL;PREF':'15210240048@fudan.edu.cn',
'FN':'邢璐',
'rev':82},
{
'id':'265',
'groups':[],
'EMAIL;PREF':'17210240051@fudan.edu.cn',
'FN':'徐佳玮',
'rev':101},
{
'id':'208',
'groups':[],
'EMAIL;PREF':'xmw@cernet.edu.cn',
'FN':'徐明伟',
'rev':74},
{
'id':'206',
'groups':[],
'EMAIL;PREF':'xuke@tsinghua.edu.cn',
'FN':'徐恪',
'rev':74},
{
'id':'212',
'groups':[],
'EMAIL;PREF':'yxu@scut.edu.cn',
'FN':'许勇',
'rev':74},
{
'id':'150',
'groups':[],
'EMAIL;PREF':'13210240071@fudan.edu.cn',
'FN':'严立宇',
'rev':63},
{
'id':'220',
'groups':[],
'EMAIL;PREF':'yanwei@net.pku.edu.cn',
'FN':'严伟',
'rev':74},
{
'id':'215',
'groups':[],
'EMAIL;PREF':'ybp@cnic.cn',
'FN':'阎保平',
'rev':74},
{
'id':'216',
'groups':[],
'EMAIL;PREF':'fcyang@bupt.edu.cn',
'FN':'杨放春',
'rev':74},
{
'id':'122',
'groups':[],
'EMAIL;PREF':'jianyang16@fudan.edu.cn',
'FN':'杨健',
'rev':34},
{
'id':'219',
'groups':[],
'EMAIL;PREF':'yangnianhua@suibe.edu.cn',
'FN':'杨年华',
'rev':74},
{
'id':'221',
'groups':[],
'EMAIL;PREF':'yangwu@hrbeu.edu.cn',
'FN':'杨武',
'rev':74},
{
'id':'222',
'groups':[],
'EMAIL;PREF':'yangwang@csu.edu.cn',
'FN':'阳旺',
'rev':74},
{
'id':'218',
'groups':[],
'EMAIL;PREF':'yaolin@dlut.edu.cn',
'FN':'姚琳',
'rev':74},
{
'id':'217',
'groups':[],
'EMAIL;PREF':'534262692@qq.com',
'FN':'叶进',
'rev':74},
{
'id':'151',
'groups':[],
'EMAIL;PREF':'mlye16@fudan.edu.cn',
'FN':'叶美麟',
'rev':64},
{
'id':'223',
'groups':[],
'EMAIL;PREF':'xsyi@mail.neu.edu.cn',
'FN':'易秀双',
'rev':74},
{
'id':'56',
'groups':[],
'EMAIL;PREF':'yudongmei@mail.sic.ac.cn',
'FN':'俞冬梅',
'rev':26},
{
'id':'258',
'groups':[],
'EMAIL;PREF':'653360440@qq.com',
'FN':'在路上',
'rev':94},
{
'id':'228',
'groups':[],
'EMAIL;PREF':'guoqiang@ict.ac.cn',
'FN':'张国强',
'rev':74},
{
'id':'242',
'groups':[],
'EMAIL;PREF':'zhanghs@bjtu.edu.cn',
'FN':'张汉姝',
'rev':78},
{
'id':'230',
'groups':[],
'EMAIL;PREF':'ling@scut.edu.cn',
'FN':'张凌',
'rev':74},
{
'id':'232',
'groups':[],
'EMAIL;PREF':'p-zhang@xjtu.edu.cn',
'FN':'张鹏',
'rev':74},
{
'id':'233',
'groups':[],
'EMAIL;PREF':'zhangsl@nankai.edu.cn',
'FN':'张圣林',
'rev':74},
{
'id':'25',
'groups':[],
'EMAIL;PREF':'11300240089@fudan.edu.cn',
'FN':'张圣喆',
'rev':7},
{
'id':'235',
'groups':[],
'EMAIL;PREF':'zhangyq@gucas.ac.cn',
'FN':'张玉清',
'rev':74},
{
'id':'238',
'groups':[],
'EMAIL;PREF':'zhangzt@nsfc.gov.cn',
'FN':'张兆田',
'rev':74},
{
'id':'243',
'groups':[],
'EMAIL;PREF':'13210240045@fudan.edu.cn',
'FN':'张舟远',
'rev':79},
{
'id':'237',
'groups':[],
'EMAIL;PREF':'zhangzl@swu.edu.cn',
'FN':'张自力',
'rev':74},
{
'id':'224',
'groups':[],
'EMAIL;PREF':'zhp@pku.edu.cn',
'FN':'张蓓',
'rev':74},
{
'id':'225',
'groups':[],
'EMAIL;PREF':'bkzhao@nudt.edu.cn',
'FN':'赵宝康',
'rev':74},
{
'id':'229',
'groups':[],
'EMAIL;PREF':'zhaoh@neusoft.com',
'FN':'赵宏',
'rev':74},
{
'id':'236',
'groups':[],
'EMAIL;PREF':'zyx@newreach.cn',
'FN':'赵邑新',
'rev':74},
{
'id':'234',
'groups':[],
'EMAIL;PREF':'zhaoying@ccsa.org.cn',
'FN':'赵莹',
'rev':74},
{
'id':'261',
'groups':[],
'EMAIL;PREF':'15307130435@fudan.edu.cn',
'FN':'赵瑜',
'rev':97},
{
'id':'226',
'groups':[],
'EMAIL;PREF':'fczhou@mail.neu.edu.cn',
'FN':'周福才',
'rev':74},
{
'id':'227',
'groups':[],
'EMAIL;PREF':'zhouguanghui@vip.sina.com',
'FN':'周广辉',
'rev':74},
{
'id':'143',
'groups':[],
'EMAIL;PREF':'648453833@qq.com',
'FN':'朱玺',
'rev':56},
{
'id':'231',
'groups':[],
'EMAIL;PREF':'liehuangz@bit.edu.cn',
'FN':'祝烈煌',
'rev':74},
{
'id':'17',
'groups':[],
'EMAIL;PREF':'11210240100@fudan.edu.cn',
'FN':'郦丽珍',
'rev':0},
{
'id':'156',
'groups':[],
'EMAIL;PREF':'14300240003@fudan.edu.cn',
'FN':'闫铭',
'rev':69}]
```


```python
peopleCount = 0
for term in contractInfo:
    peopleCount += 1
    tid = term['id']
    tEmailInfo = term['EMAIL;PREF']
    tFN = term['FN']
    print('\n第',peopleCount,'个联系人：',
          '\nid:', tid,
          '\n姓名:', tFN,
          '\n邮件帐号:', tEmailInfo)
print('\n邮箱的联系人列表中总共有',peopleCount,'个联系人')
```


    第 1 个联系人： 
    id: 154 
    姓名: 'ypzhong' 
    邮件帐号: ypzhong@fudan.edu.cn
    
    第 2 个联系人： 
    id: 40 
    姓名: '曹瑜' 
    邮件帐号: caoyu@fudan.edu.cn
    
    第 3 个联系人： 
    id: 34 
    姓名: '复旦大学国家保密学院' 
    邮件帐号: cns@fudan.edu.cn
    
    第 4 个联系人： 
    id: 35 
    姓名: '马 建庆' 
    邮件帐号: jqma@fudan.edu.cn
    
    第 5 个联系人： 
    id: 38 
    姓名: '孙笑侠' 
    邮件帐号: sunxiaoxia@fudan.edu.cn
    
    第 6 个联系人： 
    id: 39 
    姓名: '王慧敏' 
    邮件帐号: wanghm@fudan.edu.cn
    
    第 7 个联系人： 
    id: 37 
    姓名: '王晓阳' 
    邮件帐号: xywangCS@fudan.edu.cn
    
    第 8 个联系人： 
    id: 36 
    姓名: '薛向阳' 
    邮件帐号: xyxue@fudan.edu.cn
    
    第 9 个联系人： 
    id: 32 
    姓名: 12307130381 
    邮件帐号: 12307130381@fudan.edu.cn
    
    第 10 个联系人： 
    id: 30 
    姓名: 13210240012 
    邮件帐号: 13210240012@fudan.edu.cn
    
    第 11 个联系人： 
    id: 61 
    姓名: 13300240001 
    邮件帐号: 13300240001@fudan.edu.cn
    
    第 12 个联系人： 
    id: 62 
    姓名: 13300240002 
    邮件帐号: 13300240002@fudan.edu.cn
    
    第 13 个联系人： 
    id: 63 
    姓名: 13300240004 
    邮件帐号: 13300240004@fudan.edu.cn
    
    第 14 个联系人： 
    id: 64 
    姓名: 13300240006 
    邮件帐号: 13300240006@fudan.edu.cn
    
    第 15 个联系人： 
    id: 65 
    姓名: 13300240007 
    邮件帐号: 13300240007@fudan.edu.cn
    
    第 16 个联系人： 
    id: 66 
    姓名: 13300240008 
    邮件帐号: 13300240008@fudan.edu.cn
    
    第 17 个联系人： 
    id: 67 
    姓名: 13300240009 
    邮件帐号: 13300240009@fudan.edu.cn
    
    第 18 个联系人： 
    id: 68 
    姓名: 13300240010 
    邮件帐号: 13300240010@fudan.edu.cn
    
    第 19 个联系人： 
    id: 69 
    姓名: 13300240011 
    邮件帐号: 13300240011@fudan.edu.cn
    
    第 20 个联系人： 
    id: 70 
    姓名: 13300240012 
    邮件帐号: 13300240012@fudan.edu.cn
    
    第 21 个联系人： 
    id: 71 
    姓名: 13300240014 
    邮件帐号: 13300240014@fudan.edu.cn
    
    第 22 个联系人： 
    id: 72 
    姓名: 13300240015 
    邮件帐号: 13300240015@fudan.edu.cn
    
    第 23 个联系人： 
    id: 73 
    姓名: 13300240016 
    邮件帐号: 13300240016@fudan.edu.cn
    
    第 24 个联系人： 
    id: 74 
    姓名: 13300240017 
    邮件帐号: 13300240017@fudan.edu.cn
    
    第 25 个联系人： 
    id: 75 
    姓名: 13300240018 
    邮件帐号: 13300240018@fudan.edu.cn
    
    第 26 个联系人： 
    id: 76 
    姓名: 13300240019 
    邮件帐号: 13300240019@fudan.edu.cn
    
    第 27 个联系人： 
    id: 77 
    姓名: 13300240020 
    邮件帐号: 13300240020@fudan.edu.cn
    
    第 28 个联系人： 
    id: 78 
    姓名: 13300240021 
    邮件帐号: 13300240021@fudan.edu.cn
    
    第 29 个联系人： 
    id: 79 
    姓名: 13300240022 
    邮件帐号: 13300240022@fudan.edu.cn
    
    第 30 个联系人： 
    id: 80 
    姓名: 13300240023 
    邮件帐号: 13300240023@fudan.edu.cn
    
    第 31 个联系人： 
    id: 81 
    姓名: 13300240024 
    邮件帐号: 13300240024@fudan.edu.cn
    
    第 32 个联系人： 
    id: 82 
    姓名: 13300240025 
    邮件帐号: 13300240025@fudan.edu.cn
    
    第 33 个联系人： 
    id: 83 
    姓名: 13307130027 
    邮件帐号: 13307130027@fudan.edu.cn
    
    第 34 个联系人： 
    id: 84 
    姓名: 13307130046 
    邮件帐号: 13307130046@fudan.edu.cn
    
    第 35 个联系人： 
    id: 85 
    姓名: 13307130058 
    邮件帐号: 13307130058@fudan.edu.cn
    
    第 36 个联系人： 
    id: 86 
    姓名: 13307130084 
    邮件帐号: 13307130084@fudan.edu.cn
    
    第 37 个联系人： 
    id: 87 
    姓名: 13307130085 
    邮件帐号: 13307130085@fudan.edu.cn
    
    第 38 个联系人： 
    id: 88 
    姓名: 13307130086 
    邮件帐号: 13307130086@fudan.edu.cn
    
    第 39 个联系人： 
    id: 89 
    姓名: 13307130100 
    邮件帐号: 13307130100@fudan.edu.cn
    
    第 40 个联系人： 
    id: 90 
    姓名: 13307130107 
    邮件帐号: 13307130107@fudan.edu.cn
    
    第 41 个联系人： 
    id: 91 
    姓名: 13307130120 
    邮件帐号: 13307130120@fudan.edu.cn
    
    第 42 个联系人： 
    id: 92 
    姓名: 13307130137 
    邮件帐号: 13307130137@fudan.edu.cn
    
    第 43 个联系人： 
    id: 93 
    姓名: 13307130140 
    邮件帐号: 13307130140@fudan.edu.cn
    
    第 44 个联系人： 
    id: 94 
    姓名: 13307130159 
    邮件帐号: 13307130159@fudan.edu.cn
    
    第 45 个联系人： 
    id: 95 
    姓名: 13307130161 
    邮件帐号: 13307130161@fudan.edu.cn
    
    第 46 个联系人： 
    id: 96 
    姓名: 13307130170 
    邮件帐号: 13307130170@fudan.edu.cn
    
    第 47 个联系人： 
    id: 97 
    姓名: 13307130195 
    邮件帐号: 13307130195@fudan.edu.cn
    
    第 48 个联系人： 
    id: 98 
    姓名: 13307130199 
    邮件帐号: 13307130199@fudan.edu.cn
    
    第 49 个联系人： 
    id: 99 
    姓名: 13307130267 
    邮件帐号: 13307130267@fudan.edu.cn
    
    第 50 个联系人： 
    id: 100 
    姓名: 13307130268 
    邮件帐号: 13307130268@fudan.edu.cn
    
    第 51 个联系人： 
    id: 101 
    姓名: 13307130294 
    邮件帐号: 13307130294@fudan.edu.cn
    
    第 52 个联系人： 
    id: 102 
    姓名: 13307130327 
    邮件帐号: 13307130327@fudan.edu.cn
    
    第 53 个联系人： 
    id: 103 
    姓名: 13307130342 
    邮件帐号: 13307130342@fudan.edu.cn
    
    第 54 个联系人： 
    id: 104 
    姓名: 13307130363 
    邮件帐号: 13307130363@fudan.edu.cn
    
    第 55 个联系人： 
    id: 105 
    姓名: 13307130364 
    邮件帐号: 13307130364@fudan.edu.cn
    
    第 56 个联系人： 
    id: 106 
    姓名: 13307130370 
    邮件帐号: 13307130370@fudan.edu.cn
    
    第 57 个联系人： 
    id: 107 
    姓名: 13307130384 
    邮件帐号: 13307130384@fudan.edu.cn
    
    第 58 个联系人： 
    id: 108 
    姓名: 13307130396 
    邮件帐号: 13307130396@fudan.edu.cn
    
    第 59 个联系人： 
    id: 109 
    姓名: 13307130410 
    邮件帐号: 13307130410@fudan.edu.cn
    
    第 60 个联系人： 
    id: 110 
    姓名: 13307130428 
    邮件帐号: 13307130428@fudan.edu.cn
    
    第 61 个联系人： 
    id: 111 
    姓名: 13307130446 
    邮件帐号: 13307130446@fudan.edu.cn
    
    第 62 个联系人： 
    id: 112 
    姓名: 13307130475 
    邮件帐号: 13307130475@fudan.edu.cn
    
    第 63 个联系人： 
    id: 113 
    姓名: 13307130491 
    邮件帐号: 13307130491@fudan.edu.cn
    
    第 64 个联系人： 
    id: 114 
    姓名: 13307130501 
    邮件帐号: 13307130501@fudan.edu.cn
    
    第 65 个联系人： 
    id: 115 
    姓名: 13307130525 
    邮件帐号: 13307130525@fudan.edu.cn
    
    第 66 个联系人： 
    id: 116 
    姓名: 13307130533 
    邮件帐号: 13307130533@fudan.edu.cn
    
    第 67 个联系人： 
    id: 127 
    姓名: 13601927008 
    邮件帐号: 13601927008@sina.cn
    
    第 68 个联系人： 
    id: 45 
    姓名: 13601927008m0 
    邮件帐号: 13601927008m0@sina.cn
    
    第 69 个联系人： 
    id: 42 
    姓名: 14307130046 
    邮件帐号: 14307130046@fudan.edu.cn
    
    第 70 个联系人： 
    id: 41 
    姓名: 14307130064 
    邮件帐号: 14307130064@fudan.edu.cn
    
    第 71 个联系人： 
    id: 117 
    姓名: 14307130291 
    邮件帐号: 14307130291@fudan.edu.cn
    
    第 72 个联系人： 
    id: 118 
    姓名: 14307130298 
    邮件帐号: 14307130298@fudan.edu.cn
    
    第 73 个联系人： 
    id: 264 
    姓名: 574419684 
    邮件帐号: 574419684@qq.com
    
    第 74 个联系人： 
    id: 247 
    姓名: An,Yuan 
    邮件帐号: ya45@drexel.edu
    
    第 75 个联系人： 
    id: 131 
    姓名: annexian 
    邮件帐号: annexian@163.com
    
    第 76 个联系人： 
    id: 160 
    姓名: baggage 
    邮件帐号: baggage@sina.com
    
    第 77 个联系人： 
    id: 142 
    姓名: bkg 
    邮件帐号: bkg@pku.edu.cn
    
    第 78 个联系人： 
    id: 130 
    姓名: Bonnie Ainslie 
    邮件帐号: southpoint01002@gmail.com
    
    第 79 个联系人： 
    id: 161 
    姓名: ccf-internet@cernet.edu.cn 
    邮件帐号: ccf-internet@cernet.edu.cn
    
    第 80 个联系人： 
    id: 51 
    姓名: cfyuan 
    邮件帐号: cfyuan@nju.edu.cn
    
    第 81 个联系人： 
    id: 241 
    姓名: cgjh 
    邮件帐号: cgjh@fudan.edu.cn
    
    第 82 个联系人： 
    id: 266 
    姓名: chaxin 
    邮件帐号: chaxin@fudan.edu.cn
    
    第 83 个联系人： 
    id: 256 
    姓名: chyp@e-neurons.net 
    邮件帐号: chyp@e-neurons.net
    
    第 84 个联系人： 
    id: 21 
    姓名: cjsypei 
    邮件帐号: 13162516735@126.com
    
    第 85 个联系人： 
    id: 268 
    姓名: cs211 
    邮件帐号: cs211@fudan.edu.cn
    
    第 86 个联系人： 
    id: 7 
    姓名: cwu 
    邮件帐号: cwu@fudan.edu.cn
    
    第 87 个联系人： 
    id: 137 
    姓名: Donna.Coombs.1 
    邮件帐号: Donna.Coombs.1@city.ac.uk
    
    第 88 个联系人： 
    id: 28 
    姓名: e路東瀛_JAPANiCAN 
    邮件帐号: support_japanican@gmt.jtb.jp
    
    第 89 个联系人： 
    id: 123 
    姓名: Fanchen Kong 
    邮件帐号: kongfanchen1994@gmail.com
    
    第 90 个联系人： 
    id: 5 
    姓名: fdcitfdcit 
    邮件帐号: fdcit@fudan.edu.cn
    
    第 91 个联系人： 
    id: 15 
    姓名: fhxu 
    邮件帐号: fhxu@fudan.edu.cn
    
    第 92 个联系人： 
    id: 245 
    姓名: globesat88 
    邮件帐号: globesat88@aol.com
    
    第 93 个联系人： 
    id: 59 
    姓名: gongjie@fudan.edu.cn 
    邮件帐号: gongjie@fudan.edu.cn
    
    第 94 个联系人： 
    id: 2 
    姓名: gpwang 
    邮件帐号: gpwang@fudan.edu.cn
    
    第 95 个联系人： 
    id: 22 
    姓名: guhaihua 
    邮件帐号: guhaihua@sjtu.edu.cn
    
    第 96 个联系人： 
    id: 52 
    姓名: hanfei 
    邮件帐号: hanfei@hep.com.cn
    
    第 97 个联系人： 
    id: 270 
    姓名: hbkan 
    邮件帐号: hbkan@fudan.edu.cn
    
    第 98 个联系人： 
    id: 135 
    姓名: hljin14@fudan.edu.cn 
    邮件帐号: hljin14@fudan.edu.cn
    
    第 99 个联系人： 
    id: 1 
    姓名: Huang Sheng Hua 
    邮件帐号: sailh@263.net
    
    第 100 个联系人： 
    id: 149 
    姓名: Jane Yang 
    邮件帐号: jane.yang@ebaotech.com
    
    第 101 个联系人： 
    id: 12 
    姓名: jaykee0906 
    邮件帐号: jaykee0906@hotmail.com
    
    第 102 个联系人： 
    id: 244 
    姓名: jiangxuejin 
    邮件帐号: jiangxuejinny@gmail.com
    
    第 103 个联系人： 
    id: 4 
    姓名: jliao 
    邮件帐号: jliao@fudan.edu.cn
    
    第 104 个联系人： 
    id: 6 
    姓名: jwu 
    邮件帐号: jwu@fudan.edu.cn
    
    第 105 个联系人： 
    id: 13 
    姓名: jwye 
    邮件帐号: jwye@fudan.edu.cn
    
    第 106 个联系人： 
    id: 153 
    姓名: jxyj 
    邮件帐号: jxyj@fudan.edu.cn
    
    第 107 个联系人： 
    id: 133 
    姓名: Kyle Robert 
    邮件帐号: kjrobert144@gmail.com
    
    第 108 个联系人： 
    id: 138 
    姓名: lgs 
    邮件帐号: lgsok@163.com
    
    第 109 个联系人： 
    id: 125 
    姓名: li_jp 
    邮件帐号: li_jp@fudan.edu.cn
    
    第 110 个联系人： 
    id: 50 
    姓名: liuwd 
    邮件帐号: liuwd@mail.tsinghua.edu.cn
    
    第 111 个联系人： 
    id: 263 
    姓名: LJQ 
    邮件帐号: jsgnljq@163.com
    
    第 112 个联系人： 
    id: 47 
    姓名: Lu Junlin 
    邮件帐号: ljl@pku.edu.cn
    
    第 113 个联系人： 
    id: 139 
    姓名: luzhihui 
    邮件帐号: lzh@fudan.edu.cn
    
    第 114 个联系人： 
    id: 49 
    姓名: lzhang 
    邮件帐号: lzhang@fudan.edu.cn
    
    第 115 个联系人： 
    id: 10 
    姓名: myan 
    邮件帐号: myan@fudan.edu.cn
    
    第 116 个联系人： 
    id: 55 
    姓名: myan 
    邮件帐号: myan@fuda.edu.cn
    
    第 117 个联系人： 
    id: 19 
    姓名: qiandavid1991 
    邮件帐号: qiandavid1991@gmail.com
    
    第 118 个联系人： 
    id: 57 
    姓名: Sara Xue 
    邮件帐号: xueshen@fudan.edu.cn
    
    第 119 个联系人： 
    id: 16 
    姓名: sea_bull825169 
    邮件帐号: sea_bull825169@sina.com
    
    第 120 个联系人： 
    id: 11 
    姓名: shfei 
    邮件帐号: shfei@fudan.edu.cn
    
    第 121 个联系人： 
    id: 29 
    姓名: sjxcwu 
    邮件帐号: sjxcwu@163.com
    
    第 122 个联系人： 
    id: 126 
    姓名: sjxcwu 
    邮件帐号: sjxcwu@139.com
    
    第 123 个联系人： 
    id: 141 
    姓名: sjxcwu 
    邮件帐号: sjxcwu@yahoo.com.cn
    
    第 124 个联系人： 
    id: 14 
    姓名: szhang 
    邮件帐号: szhang@fudan.edu.cn
    
    第 125 个联系人： 
    id: 260 
    姓名: wangxq261 
    邮件帐号: wangxq261@126.com
    
    第 126 个联系人： 
    id: 269 
    姓名: wdyang 
    邮件帐号: wdyang@fudan.edu.cn
    
    第 127 个联系人： 
    id: 157 
    姓名: weiwang1 
    邮件帐号: weiwang1@fudan.edu.cn
    
    第 128 个联系人： 
    id: 134 
    姓名: wlhan 
    邮件帐号: wlhan@fudan.edu.cn
    
    第 129 个联系人： 
    id: 9 
    姓名: wmfu 
    邮件帐号: wmfu@fudan.edu.cn
    
    第 130 个联系人： 
    id: 155 
    姓名: wuhongmei2727 
    邮件帐号: wuhongmei2727@126.com
    
    第 131 个联系人： 
    id: 132 
    姓名: xujn 
    邮件帐号: xujn@fudan.edu.cn
    
    第 132 个联系人： 
    id: 33 
    姓名: xuxiaoyin 
    邮件帐号: xuxiaoyin@fudan.edu.cn
    
    第 133 个联系人： 
    id: 152 
    姓名: xyjiang 
    邮件帐号: xyjiang@fudan.edu.cn
    
    第 134 个联系人： 
    id: 140 
    姓名: xzyao 
    邮件帐号: xzyao@fudan.edu.cn
    
    第 135 个联系人： 
    id: 267 
    姓名: Yang Weidong 
    邮件帐号: yweidong@gmail.com
    
    第 136 个联系人： 
    id: 259 
    姓名: ylzhao 
    邮件帐号: ylzhao@fudan.edu.cn
    
    第 137 个联系人： 
    id: 248 
    姓名: yuan.an 
    邮件帐号: yuan.an@drexel.edu
    
    第 138 个联系人： 
    id: 44 
    姓名: Yuan Zhang 
    邮件帐号: yuanxzhang@fudan.edu.cn
    
    第 139 个联系人： 
    id: 159 
    姓名: Yu Dongmei 
    邮件帐号: yudm1215@hotmail.com
    
    第 140 个联系人： 
    id: 255 
    姓名: Zhang Li 
    邮件帐号: zhang_li@fudan.edu.cn
    
    第 141 个联系人： 
    id: 53 
    姓名: zhanglong 
    邮件帐号: zhanglong@139.com
    
    第 142 个联系人： 
    id: 43 
    姓名: Zhemin Yang 
    邮件帐号: yangzhemin@fudan.edu.cn
    
    第 143 个联系人： 
    id: 144 
    姓名: zhouj 
    邮件帐号: zhouj@cnas.org.cn
    
    第 144 个联系人： 
    id: 60 
    姓名: zhudl 
    邮件帐号: zhudl@fudan.edu.cn
    
    第 145 个联系人： 
    id: 3 
    姓名: zjp 
    邮件帐号: zjp@fudan.edu.cn
    
    第 146 个联系人： 
    id: 8 
    姓名: zytian 
    邮件帐号: zytian@gmail.com
    
    第 147 个联系人： 
    id: 27 
    姓名: 蔡一晓 
    邮件帐号: 11300240002@fudan.edu.cn
    
    第 148 个联系人： 
    id: 253 
    姓名: 蔡一晓 
    邮件帐号: 15210240003@fudan.edu.cn
    
    第 149 个联系人： 
    id: 23 
    姓名: 陈 辰 
    邮件帐号: chenc@fudan.edu.cn
    
    第 150 个联系人： 
    id: 46 
    姓名: 陈福才 
    邮件帐号: 13503827650@139.com
    
    第 151 个联系人： 
    id: 128 
    姓名: 陈秋羽 
    邮件帐号: qychen13@fudan.edu.cn
    
    第 152 个联系人： 
    id: 58 
    姓名: 陈荣华 
    邮件帐号: chenrh@fudan.edu.cn
    
    第 153 个联系人： 
    id: 136 
    姓名: 袋鼠 
    邮件帐号: daisj518@163.com
    
    第 154 个联系人： 
    id: 239 
    姓名: 董贇 
    邮件帐号: dongyun@shxd.com
    
    第 155 个联系人： 
    id: 147 
    姓名: 胡天晓 
    邮件帐号: 14300240007@fudan.edu.cn
    
    第 156 个联系人： 
    id: 252 
    姓名: 计算机科学技术学院党办 
    邮件帐号: cs_dangban@fudan.edu.cn
    
    第 157 个联系人： 
    id: 129 
    姓名: 计算机学院 
    邮件帐号: cs_school@fudan.edu.cn
    
    第 158 个联系人： 
    id: 257 
    姓名: 计算机学院工会 
    邮件帐号: cs_gonghui@fudan.edu.cn
    
    第 159 个联系人： 
    id: 20 
    姓名: 计算机学院科研 
    邮件帐号: cs_keyan@fudan.edu.cn
    
    第 160 个联系人： 
    id: 120 
    姓名: 计算机学院人事 
    邮件帐号: cs_renshi@fudan.edu.cn
    
    第 161 个联系人： 
    id: 54 
    姓名: 江信舟 
    邮件帐号: 13307130028@fudan.edu.cn
    
    第 162 个联系人： 
    id: 254 
    姓名: 李金明 
    邮件帐号: jinmingli@fudan.edu.cn
    
    第 163 个联系人： 
    id: 164 
    姓名: 李芝棠 
    邮件帐号: leeying@mail.hust.edu.cn
    
    第 164 个联系人： 
    id: 162 
    姓名: 李忠诚 
    邮件帐号: zcli@ict.ac.cn
    
    第 165 个联系人： 
    id: 148 
    姓名: 林俊雄 
    邮件帐号: 14307130203@fudan.edu.cn
    
    第 166 个联系人： 
    id: 158 
    姓名: 刘山泉 
    邮件帐号: liusq@sheitc.gov.cn
    
    第 167 个联系人： 
    id: 145 
    姓名: 刘巍 
    邮件帐号: 14210240047@fudan.edu.cn
    
    第 168 个联系人： 
    id: 163 
    姓名: 刘振鹏 
    邮件帐号: lzp@hbu.edu.cn
    
    第 169 个联系人： 
    id: 165 
    姓名: 刘志勇 
    邮件帐号: zyliu@ict.ac.cn
    
    第 170 个联系人： 
    id: 26 
    姓名: 卢源 
    邮件帐号: 11300240085@fudan.edu.cn
    
    第 171 个联系人： 
    id: 169 
    姓名: 马严 
    邮件帐号: mayan@bupt.edu.cn
    
    第 172 个联系人： 
    id: 166 
    姓名: 马皓 
    邮件帐号: mah@pku.edu.cn
    
    第 173 个联系人： 
    id: 167 
    姓名: 孟坤 
    邮件帐号: mengkurt@bistu.edu.cn
    
    第 174 个联系人： 
    id: 168 
    姓名: 孟洛明 
    邮件帐号: lmmeng@bupt.edu.cn
    
    第 175 个联系人： 
    id: 171 
    姓名: 钱德沛 
    邮件帐号: depeiq@buaa.edu.cn
    
    第 176 个联系人： 
    id: 172 
    姓名: 秦丰林 
    邮件帐号: qfl@sdu.edu.cn
    
    第 177 个联系人： 
    id: 48 
    姓名: 秦磊华 
    邮件帐号: lhqin@hust.edu.cn
    
    第 178 个联系人： 
    id: 170 
    姓名: 曲成义 
    邮件帐号: yichengqu@caecc.com
    
    第 179 个联系人： 
    id: 249 
    姓名: 沈建蓉 
    邮件帐号: jrshen@fudan.edu.cn
    
    第 180 个联系人： 
    id: 175 
    姓名: 沈蒙 
    邮件帐号: shenmeng@bit.edu.cn
    
    第 181 个联系人： 
    id: 0 
    姓名: 沈蕴婕 
    邮件帐号: syj@stcsm.gov.cn
    
    第 182 个联系人： 
    id: 146 
    姓名: 施敏 
    邮件帐号: shimin@sheitc.gov.cn
    
    第 183 个联系人： 
    id: 24 
    姓名: 宋富 
    邮件帐号: fsong@sei.ecnu.edu.cn
    
    第 184 个联系人： 
    id: 119 
    姓名: 宋昊 
    邮件帐号: 16210240081@fudan.edu.cn
    
    第 185 个联系人： 
    id: 173 
    姓名: 苏金树 
    邮件帐号: birchsu@139.com
    
    第 186 个联系人： 
    id: 174 
    姓名: 孙利民 
    邮件帐号: sunlimin@iie.ac.cn
    
    第 187 个联系人： 
    id: 176 
    姓名: 孙毅 
    邮件帐号: sunyi@ict.ac.cn
    
    第 188 个联系人： 
    id: 177 
    姓名: 孙志刚 
    邮件帐号: sunzhigang@263.net
    
    第 189 个联系人： 
    id: 31 
    姓名: 唐 
    邮件帐号: 13381259551@163.com
    
    第 190 个联系人： 
    id: 180 
    姓名: 唐勇 
    邮件帐号: worldgulit@uestc.edu.cn
    
    第 191 个联系人： 
    id: 179 
    姓名: 陶军 
    邮件帐号: juntao@seu.edu.cn
    
    第 192 个联系人： 
    id: 178 
    姓名: 田晖 
    邮件帐号: htian@hqu.edu.cn
    
    第 193 个联系人： 
    id: 240 
    姓名: 同事-廖志成 
    邮件帐号: zchliao@fudan.edu.cn
    
    第 194 个联系人： 
    id: 194 
    姓名: 汪文勇 
    邮件帐号: wangwy@uestc.edu.cn
    
    第 195 个联系人： 
    id: 271 
    姓名: 汪钰颖 
    邮件帐号: 17210240209@fudan.edu.cn
    
    第 196 个联系人： 
    id: 18 
    姓名: 王川 
    邮件帐号: 11210240111@fudan.edu.cn
    
    第 197 个联系人： 
    id: 181 
    姓名: 王丹 
    邮件帐号: freeloam@gmail.com
    
    第 198 个联系人： 
    id: 251 
    姓名: 王定鑫 
    邮件帐号: 14300240005@fudan.edu.cn
    
    第 199 个联系人： 
    id: 182 
    姓名: 王栋 
    邮件帐号: wangd01@gmail.com
    
    第 200 个联系人： 
    id: 184 
    姓名: 王华 
    邮件帐号: wanghua@sdu.edu.cn
    
    第 201 个联系人： 
    id: 185 
    姓名: 王怀民 
    邮件帐号: whm_w@163.com
    
    第 202 个联系人： 
    id: 189 
    姓名: 王建新 
    邮件帐号: jxwang@mail.csu.edu.cn
    
    第 203 个联系人： 
    id: 186 
    姓名: 王进 
    邮件帐号: wjin1985@suda.edu.cn
    
    第 204 个联系人： 
    id: 188 
    姓名: 王劲松 
    邮件帐号: jswang@tjut.edu.cn
    
    第 205 个联系人： 
    id: 191 
    姓名: 王明文 
    邮件帐号: mwwang@jxnu.edu.cn
    
    第 206 个联系人： 
    id: 124 
    姓名: 王旗 
    邮件帐号: 13801111946@139.com
    
    第 207 个联系人： 
    id: 193 
    姓名: 王文东 
    邮件帐号: wdwang@bupt.edu.cn
    
    第 208 个联系人： 
    id: 197 
    姓名: 王小峰 
    邮件帐号: xfwang.nudt@gmail.com
    
    第 209 个联系人： 
    id: 195 
    姓名: 王新 
    邮件帐号: xinw@fudan.edu.cn
    
    第 210 个联系人： 
    id: 196 
    姓名: 王新兵 
    邮件帐号: xwang8@sjtu.edu.cn
    
    第 211 个联系人： 
    id: 198 
    姓名: 王兴伟 
    邮件帐号: wangxw@mail.neu.edu.cn
    
    第 212 个联系人： 
    id: 199 
    姓名: 王勇 
    邮件帐号: wang@guet.edu.cn
    
    第 213 个联系人： 
    id: 200 
    姓名: 王嫣 
    邮件帐号: zzdxwyan@126.com
    
    第 214 个联系人： 
    id: 192 
    姓名: 魏嵬 
    邮件帐号: weiwei@xaut.edu.cn
    
    第 215 个联系人： 
    id: 201 
    姓名: 闻英友 
    邮件帐号: wenyy@neusoft.com
    
    第 216 个联系人： 
    id: 183 
    姓名: 吴帆 
    邮件帐号: fwu@cs.sjtu.edu.cn
    
    第 217 个联系人： 
    id: 187 
    姓名: 吴建平 
    邮件帐号: jianping@cernet.edu.cn
    
    第 218 个联系人： 
    id: 190 
    姓名: 吴黎兵 
    邮件帐号: wu@whu.edu.cn
    
    第 219 个联系人： 
    id: 121 
    姓名: 吴子彦 
    邮件帐号: 16210240043@fudan.edu.cn
    
    第 220 个联系人： 
    id: 202 
    姓名: 夏春和 
    邮件帐号: Xch@buaa.edu.cn
    
    第 221 个联系人： 
    id: 262 
    姓名: 夏毅 
    邮件帐号: 13307110174@fudan.edu.cn
    
    第 222 个联系人： 
    id: 250 
    姓名: 响 
    邮件帐号: 1131662457@qq.com
    
    第 223 个联系人： 
    id: 214 
    姓名: 向阳朝 
    邮件帐号: xiangyz@digitalchina.com
    
    第 224 个联系人： 
    id: 213 
    姓名: 向渝 
    邮件帐号: jcxiang@uestc.edu.cn
    
    第 225 个联系人： 
    id: 205 
    姓名: 肖国荣 
    邮件帐号: newducky@126.com
    
    第 226 个联系人： 
    id: 210 
    姓名: 肖人毅 
    邮件帐号: xiaory@nsfc.gov.cn
    
    第 227 个联系人： 
    id: 203 
    姓名: 谢东亮 
    邮件帐号: Xiedl@bupt.edu.cn
    
    第 228 个联系人： 
    id: 204 
    姓名: 谢高岗 
    邮件帐号: xie@ict.ac.cn
    
    第 229 个联系人： 
    id: 209 
    姓名: 谢锐 
    邮件帐号: sh@sjtu.edu.cn
    
    第 230 个联系人： 
    id: 211 
    姓名: 谢晓燕 
    邮件帐号: sharriexie@163.com
    
    第 231 个联系人： 
    id: 207 
    姓名: 谢鲲 
    邮件帐号: xiekun@hnu.edu.cn
    
    第 232 个联系人： 
    id: 246 
    姓名: 邢璐 
    邮件帐号: 15210240048@fudan.edu.cn
    
    第 233 个联系人： 
    id: 265 
    姓名: 徐佳玮 
    邮件帐号: 17210240051@fudan.edu.cn
    
    第 234 个联系人： 
    id: 208 
    姓名: 徐明伟 
    邮件帐号: xmw@cernet.edu.cn
    
    第 235 个联系人： 
    id: 206 
    姓名: 徐恪 
    邮件帐号: xuke@tsinghua.edu.cn
    
    第 236 个联系人： 
    id: 212 
    姓名: 许勇 
    邮件帐号: yxu@scut.edu.cn
    
    第 237 个联系人： 
    id: 150 
    姓名: 严立宇 
    邮件帐号: 13210240071@fudan.edu.cn
    
    第 238 个联系人： 
    id: 220 
    姓名: 严伟 
    邮件帐号: yanwei@net.pku.edu.cn
    
    第 239 个联系人： 
    id: 215 
    姓名: 阎保平 
    邮件帐号: ybp@cnic.cn
    
    第 240 个联系人： 
    id: 216 
    姓名: 杨放春 
    邮件帐号: fcyang@bupt.edu.cn
    
    第 241 个联系人： 
    id: 122 
    姓名: 杨健 
    邮件帐号: jianyang16@fudan.edu.cn
    
    第 242 个联系人： 
    id: 219 
    姓名: 杨年华 
    邮件帐号: yangnianhua@suibe.edu.cn
    
    第 243 个联系人： 
    id: 221 
    姓名: 杨武 
    邮件帐号: yangwu@hrbeu.edu.cn
    
    第 244 个联系人： 
    id: 222 
    姓名: 阳旺 
    邮件帐号: yangwang@csu.edu.cn
    
    第 245 个联系人： 
    id: 218 
    姓名: 姚琳 
    邮件帐号: yaolin@dlut.edu.cn
    
    第 246 个联系人： 
    id: 217 
    姓名: 叶进 
    邮件帐号: 534262692@qq.com
    
    第 247 个联系人： 
    id: 151 
    姓名: 叶美麟 
    邮件帐号: mlye16@fudan.edu.cn
    
    第 248 个联系人： 
    id: 223 
    姓名: 易秀双 
    邮件帐号: xsyi@mail.neu.edu.cn
    
    第 249 个联系人： 
    id: 56 
    姓名: 俞冬梅 
    邮件帐号: yudongmei@mail.sic.ac.cn
    
    第 250 个联系人： 
    id: 258 
    姓名: 在路上 
    邮件帐号: 653360440@qq.com
    
    第 251 个联系人： 
    id: 228 
    姓名: 张国强 
    邮件帐号: guoqiang@ict.ac.cn
    
    第 252 个联系人： 
    id: 242 
    姓名: 张汉姝 
    邮件帐号: zhanghs@bjtu.edu.cn
    
    第 253 个联系人： 
    id: 230 
    姓名: 张凌 
    邮件帐号: ling@scut.edu.cn
    
    第 254 个联系人： 
    id: 232 
    姓名: 张鹏 
    邮件帐号: p-zhang@xjtu.edu.cn
    
    第 255 个联系人： 
    id: 233 
    姓名: 张圣林 
    邮件帐号: zhangsl@nankai.edu.cn
    
    第 256 个联系人： 
    id: 25 
    姓名: 张圣喆 
    邮件帐号: 11300240089@fudan.edu.cn
    
    第 257 个联系人： 
    id: 235 
    姓名: 张玉清 
    邮件帐号: zhangyq@gucas.ac.cn
    
    第 258 个联系人： 
    id: 238 
    姓名: 张兆田 
    邮件帐号: zhangzt@nsfc.gov.cn
    
    第 259 个联系人： 
    id: 243 
    姓名: 张舟远 
    邮件帐号: 13210240045@fudan.edu.cn
    
    第 260 个联系人： 
    id: 237 
    姓名: 张自力 
    邮件帐号: zhangzl@swu.edu.cn
    
    第 261 个联系人： 
    id: 224 
    姓名: 张蓓 
    邮件帐号: zhp@pku.edu.cn
    
    第 262 个联系人： 
    id: 225 
    姓名: 赵宝康 
    邮件帐号: bkzhao@nudt.edu.cn
    
    第 263 个联系人： 
    id: 229 
    姓名: 赵宏 
    邮件帐号: zhaoh@neusoft.com
    
    第 264 个联系人： 
    id: 236 
    姓名: 赵邑新 
    邮件帐号: zyx@newreach.cn
    
    第 265 个联系人： 
    id: 234 
    姓名: 赵莹 
    邮件帐号: zhaoying@ccsa.org.cn
    
    第 266 个联系人： 
    id: 261 
    姓名: 赵瑜 
    邮件帐号: 15307130435@fudan.edu.cn
    
    第 267 个联系人： 
    id: 226 
    姓名: 周福才 
    邮件帐号: fczhou@mail.neu.edu.cn
    
    第 268 个联系人： 
    id: 227 
    姓名: 周广辉 
    邮件帐号: zhouguanghui@vip.sina.com
    
    第 269 个联系人： 
    id: 143 
    姓名: 朱玺 
    邮件帐号: 648453833@qq.com
    
    第 270 个联系人： 
    id: 231 
    姓名: 祝烈煌 
    邮件帐号: liehuangz@bit.edu.cn
    
    第 271 个联系人： 
    id: 17 
    姓名: 郦丽珍 
    邮件帐号: 11210240100@fudan.edu.cn
    
    第 272 个联系人： 
    id: 156 
    姓名: 闫铭 
    邮件帐号: 14300240003@fudan.edu.cn
    
    邮箱的联系人列表中总共有 272 个联系人



```python

```


```#python

```
