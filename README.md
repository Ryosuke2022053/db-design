# ナレッジ蓄積・管理ツール


## 対象Wiki
- https://github.com/Ryosuke2022053/db-design/wiki/filesDB%E3%81%AE%E4%BD%9C%E6%88%90
- https://github.com/Ryosuke2022053/db-design/wiki/%E3%83%AD%E3%83%BC%E3%82%AB%E3%83%AB%E3%81%A7%E5%AE%9F%E8%A1%8C%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95

## 担当
- 伊藤 : バックエンド・DB周り・フロントエンド
- 安原 : フロントエンド・UI デザイン

## 作るもの
- [x] ナレッジ蓄積・管理ツール
  - [x] メモ（マークダウン）を共有することができるアプリ

## 競合アプリ
- コンフルエンス（参考）
  - https://www.atlassian.com/ja/software/confluence

## 現在考えられるタスク
- 全体公開するかしないかの設定（シェア機能）
- 画像、メモフォルダの管理
- サンプルコードをもとに UI を作成
- 一覧画面（どのメモにクリックするか）
  - 既存のメモ＆新しく作るメモ＆テンプレート
- 編集画面と表示画面
  - クリックしたあとのメモを表示＆編集（ボタンを押したら編集可能）
- 画像ありにする（colab, qitta などを参考にする）
- 削除ボタン（表示画面）
- ログイン＆ログアウト（既存）

## タスクに対する開発順序
1. UI 作成（一覧画面）（Bootstrap, テンプレートもありかも）やす
2. 自分で書いた MD ファイルを一覧で表示する（一覧画面）
3. 自分で書いた MD ファイルを表示する（表示画面）
4. 表示画面から編集できるようにする
5. 時間があれば検索も含める（タイトル名を DB に insert する必要あり）
