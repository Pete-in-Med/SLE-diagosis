# SLE-diagosis
## **版本一(6/27)**  
將SLE的診斷過程初步分成四個項目
(分別是ANA classification、input patient data、confirm data、dealing with data)  
功能包含
1. 輸入不論大寫或小寫，都可以成功輸入(upper.())
2. 輸入錯誤值時，可以使程式重新再跑一遍(while 迴圈)
3. 提供confirm data 步驟，讓輸入者可以確定自己的資料是否正確
4. 可算出不同臨床科別中最嚴重的項目(max、for、zip函數)

需優化
1. 代數名稱過於冗長
2. 前面list部分輸入有錯誤
3. 程式碼過於重複，需要精簡
4. output的細節處理


## **版本二(7/3)**
After the 06/27 meeting
將SLE的診斷過程，增加了最後一個步驟，詳細的output，因此現在總共分為五個步驟
新增的功能包含
1. 函數中有兩個情況會直接跳出，結束整個運行。(sys.exit())
第一、當ANA value 是 missing value 的時候；第二、當confirm data 發現錯誤的時候。
畢竟ANA value missing 時，就沒有得到SLE 的可能性；confirm data 發現錯誤，結果也不可能是對的。相信這個功能的增加，可以大幅減少輸入的時間。
2. 改善過於冗長的變數名稱，精簡code
3. 在input process 中，增加多一個輸入的選項，也就是NI(no information)
4. 比較優美的print 出需驗證的dictionary，這樣可以比較好做閱讀(.pprint())
