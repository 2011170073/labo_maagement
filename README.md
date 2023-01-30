# Labo_management
各教員の研究室に設置されている在室や不在を表すサインプレートは手動で操作しなければならず、サインプレートの操作ミスや教員が移動先を変更する場合があるため、訪問者が教員の所在を正しく把握できない問題がありました。  
問題解決のため、教員が研究室から別の場所に移動した際、教員の研究室のサインプレートを自動で変更するシステムを開発。  
以下は、教員の研究室の状態を管理するWebアプリケーションの３つの画面になります。  

1.各教員の研究室の最新の状態ページ(各研究室にタブレットを設置しこのページを表示します)

![スクリーンショット (605)](https://user-images.githubusercontent.com/116270960/215454592-edb967de-04d2-44a6-985f-f86f092ad709.png)

2.各教員の研究室の状態履歴を閲覧できるページ

![スクリーンショット (607)](https://user-images.githubusercontent.com/116270960/215454682-df8c89ac-dc63-48af-857a-e3a43e430410.png)


3.各教員を一覧できるページ(設置されたURLをクリックする事で1と2のページに遷移する)

![スクリーンショット (604)](https://user-images.githubusercontent.com/116270960/215454192-1aab9453-4774-496c-809a-57efd9d7c107.png)

各研究室や講義室、会議室にはカードリーダーを設置し、教員がカードリーダーに教員証をかざした際に、その情報がWebアプリケーションに送信されます。  
送られてきた情報を元に、Webアプリが研究室の状態を変更する、という流れになっています。  


# 使用した技術
- プラットフォーム：Virtual Box
- OS:Linux
- フレームワーク：Django
- ライブラリ：APScheduler
- 言語：Python,HTML/CSS,JavaScript

 

 
## Webアプリのデータベース設計
- status_listsテーブル:どの部屋・どの教員・誰の研究室の3つのカラムを持ち、各教員の研究室の状態ページに用いるテーブル。
- statusテーブル:id=研究室の状態(帰宅・在室・不在・講義中・会議中・他教授の研究室)を表すテーブル。
- teachersテーブル:id=各教員の名前を表すテーブル。
- roomsテーブル:id=各部屋(2号講義棟・会議室1205・白土研究室など)を表すテーブル。
- rooms_statusテーブル:id=各部屋の分類(講義棟・会議室・研究室など)を表すテーブル。  
上記の5つのテーブルを、以下のようにリレーションで繋げる事によってWebアプリケーションで効果的に利用しました。  
![スクリーンショット (631)](https://user-images.githubusercontent.com/116270960/215484603-31c0422b-3bd5-4d26-9a60-932cb82d23ff.png)

   
## 各教員の研究室に設置するカードリーダー
各教員の研究室に設置するカードリーダーについて。  
Raspberry PiとRaspberry Piにて利用できるカードリーダーであるPasoriというモジュールを繋げ、Python言語で教員証IDの読み取りやWebアプリと通信するプログラミングを記述しました。
※以後、このカードリーダーをクライアントシステムと命名

## 動作原理
クライアントシステムが設置されている各部屋にて、教員が教員証をかざした際、その教員ID&部屋情報がWebアプリに送信されます。  
教員ID&部屋情報を受け取ったWebアプリは、研究室の次の状態(在室・不在・講義中など)を判断、教員証・部屋情報・研究室の次の状態をstatus_listsテーブルに保存します。  
各研究室前に設置されている研究室の最新の状態ページは、３秒に一度、JavaScriptによってページをリロードするため、status_listsテーブルにデータが保存された際はその保存に追従します。  

![スクリーンショット (633)](https://user-images.githubusercontent.com/116270960/215484826-3e0554ce-ee6e-429c-adc3-016cd299a3a3.png)



