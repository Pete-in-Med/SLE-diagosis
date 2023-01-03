# SLE-diagosis
## **版本一(6/27)**  
* 將SLE的診斷過程初步分成四個項目
(分別是ANA classification、input patient data、confirm data、dealing with data)  
* 功能包含
1. 輸入不論大寫或小寫，都可以成功輸入(upper.())
2. 輸入錯誤值時，可以使程式重新再跑一遍(while 迴圈)
3. 提供confirm data 步驟，讓輸入者可以確定自己的資料是否正確
4. 可算出不同臨床科別中最嚴重的項目(max、for、zip函數)

* 需優化
1. 代數名稱過於冗長
2. 前面list部分輸入有錯誤
3. 程式碼過於重複，需要精簡
4. output的細節處理

## **版本二(7/3)**
After the 06/27 meeting  
* 將SLE的診斷過程，增加了最後一個步驟，詳細的output，因此現在總共分為五個步驟  
* 新增的功能包含
1. 函數中有兩個情況會直接跳出，結束整個運行。(sys.exit())
第一、當ANA value 是 missing value 的時候；第二、當confirm data 發現錯誤的時候。
畢竟ANA value missing 時，就沒有得到SLE 的可能性；confirm data 發現錯誤，結果也不可能是對的。相信這個功能的增加，可以大幅減少輸入的時間。
2. 改善過於冗長的變數名稱，精簡code
3. 在input process 中，增加多一個輸入的選項，也就是NI(no information)
4. 比較優美的print 出需驗證的dictionary，這樣可以比較好做閱讀(.pprint())
5. 在處理各項資料的最大值時，利用迴圈簡化code(for、max、zip)
6. 增加output數值，包含main cause、missing value，可以使醫師能進行後續的檢查和診斷

## **版本三(7/20)**
After the (7/4) meeting
* 和版本二相比，再引入了SLEDAI輔助診斷，因此現在已增加為六個步驟
* 新增的功能包含
 >功能的新增
  1. 感謝上次會議中主任所提供的建議。這次利用SLEDAI，當患者確定診斷為SLE時，可以分辨出其嚴重程度
  2. 感謝上次會議中PGY學長所提供的建議。這次的程式多了打包成fuction的環節，也多利用註解，讓修改變數變得容易且明瞭 
  3. 在輸入的方面增加了兩個功能。第一、根據自身經驗，發現輸入的時候常容易沒輸入而直接按下enter鍵，因此設置了當不小心按下enter鍵可重新輸入的情況；第二、增加B鍵，讓填錯的時候可以回去重新填寫。
  4. 新增蛋白尿的判斷環節，讓輸入者不用自行判斷蛋白尿是否異常，只要輸入病人的蛋白尿數值，系統可自行判斷(如同文隆老師在會議中所提及，如此的改變降低此系統對於輸入者的醫療知識需求門檻，臨床中即使是實習生或是護理師都可以輸入。增加此系統的價值)
 >功能的優化
  1. 利用打包function來大幅精簡程式碼(特別是輸入、驗證此兩個步驟)
  2. 利用Numpy來處理資料。感謝文隆老師的建議，利用Numpy和矩陣來處理數據，不僅系統速度可以提升，也可以有更多元的函數可以幫助程式開發者處理數據
  3. 利用formatted string來減緩print的過程過於攏長且多步驟的問題，也增加程式碼的可讀性
 >輸出的改善
  1. 輸出的部分增加(包含總分、main cause占比、reference)
  2. 多增加註解來增進使用體驗(NI stands for no information)
  3. ANA value部分，改變敘述，"診斷還不足以是SLE"


## **版本四(8/19)**
After the (7/21) meeting
* 新增的功能包含
>功能的新增
 1. 如果病人已經被診斷為SLE，便可直接進行SLEDAI的判定；反之，若還沒被診斷為SLE，那麼就根據前面判斷的結果，確定是否進行SLEDAI的評估
>特殊情況的因應
 1. 修正之前有關Renal biopsy的bug
 2. 如果遇到輸入者在第一次輸入就輸入b(也就是back)的狀況，本系統已可完善解決，並提醒輸入者
 3. 如果碰到全部總分為0，也就是全部negative的狀況，系統已可以處理這個狀況(之前會因為佔比公式的總分在分母，而此狀況中，分母為0，而造成了error的情形)
>輸出的改善
  1. 將最高分佔比項目由main cause轉換為the highest proportion of the score
  2. 印出clinical data和immunology的個別分數
  3. 印出SLEDAI的參考資料
  4. 解決dictionary會自動排序的問題
 


## **版本五**
1. 已和宏杰整合，負責與使用者互動介面部分
2. 打包packages，簡化程式碼
