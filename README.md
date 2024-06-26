# 在庫チェッカー

このプロジェクトは、指定されたウェブサイトの在庫状況を定期的にチェックし、在庫がある場合にデスクトップ通知を送信するアプリケーションです。

## 特徴

- 定期的な在庫チェック
- 在庫状況に基づくデスクトップ通知
- 設定ファイルによるカスタマイズ

## 前提条件

このプロジェクトを実行する前に、以下のライブラリがインストールされている必要があります。

- Python 3.6+
- requests
- lxml
- plyer

これらのライブラリは、以下のコマンドを使用してインストールできます。
Python をまだインストールしていない場合は、以下の公式サイトからインストールしてください。

[Python 公式サイト](https://www.python.org/downloads/)

インストールが完了したら、以下のコマンドを使用して必要なライブラリをインストールしてください。

```bash
pip install -r requirements.txt
```

## 設定

プロジェクトのルートディレクトリに `config.json` ファイルを作成し、以下のように設定します。

```json
{
  "URL": "https://example.com/product",
  "EXE_SECOND": 30
}
```

- `URL`: 在庫をチェックする商品のページの URL。
- `EXE_SECOND`: 次に在庫チェックを行う秒数。

## 使用方法

プロジェクトディレクトリで以下のコマンドを実行してください。

```bash
python stock_checker/src/check_stock.py
```

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は `LICENSE` ファイルを参照してください。
