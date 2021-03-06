# PTT Crawler Library

#### Do you want PTT in Python? import PTT

###### 這是一個專為 PTT 開發者所開發的函式庫
###### 提供完整快速的 PTT 操作
###### 根據網路速度動態調整操作速度、斷線自動恢復
###### 如有功能未能詳盡 歡迎來信告知

如何使用
-------------------
###### 你可以參考範例程式，並佐以 Test.py 裡面有 API 的範例與說明

範例程式
-------------------
###### 歡迎開發者將使用 PTT Crawler Library 的程式連結加入
[汪梯推文機器人](https://github.com/Truth0906/WantedPushCrawler)

[五樓機器人](https://github.com/Truth0906/5FloorBot)

[ID追蹤器](https://github.com/mi99202006/IDTracker)

[文章爬蟲](https://github.com/Truth0906/PostCrawler)

[準點報時機器人](https://github.com/Truth0906/ReportTimeBot)

Demo
-------------------
###### 請參考 Test.py

需求
-------------------
###### Python 3.6.1

相依函式庫
-------------------
###### request
###### BeautifulSoup4
###### progressbar2

版本
-------------------
###### 0.3.170805

API
-------------------

###### logout 登出
###### post PO 文
###### pushByIndex 根據文章編號推文
###### pushByID 根據文章ID推文
###### mail 寄信給使用者
###### getPostInfoByID 根據文章ID 取得文章資訊 內含推文清單
###### getPostInfoByIndex 根據文章編號 取得文章資訊 內含推文清單
###### getNewestPostIndex 取得該看板最新的文章編號
###### getNewPostIndexList 取得上次查詢之後才新增的文章清單
###### giveMoney 給予使用者 P幣
###### getTime 取得 PTT 系統時間
###### getUserInfo 取得該使用者資訊
###### crawlBoard 多線程爬蟲 以多重登入增加爬蟲速度 可傳入 call back 自訂存檔格式
###### getVersion 取得版本資訊

![alt text](http://i.imgur.com/nkyH9fG.png)
