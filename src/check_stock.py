import requests
from lxml import html
from plyer import notification
import time
from datetime import datetime, timedelta
import json
import logging

# ロギングの設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 設定ファイルの読み込み
def load_config():
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        logging.error("設定ファイル 'config.json' が見つかりません。")
        raise
    except json.JSONDecodeError:
        logging.error("設定ファイル 'config.json' の形式が正しくありません。")
        raise

config = load_config()
URL = config['URL']
EXE_SECOND = config['EXE_SECOND']

def get_web_data(url):
    """Webページからデータを取得し、lxmlオブジェクトを返す"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return html.fromstring(response.content)
    except requests.RequestException as e:
        logging.error(f"リクエストエラー: {e}")
        return None

def check_stock_status(tree):
    """在庫状況をチェックし、結果を文字列で返す"""
    if tree is not None:
        elements = tree.cssselect('.variation-caption.empty-stock')
        if elements:
            return elements[0].text_content().strip()
    return None

def notify_stock_status(status):
    """在庫状況に応じて通知を行う"""
    if status == '在庫なし':
        logging.info('在庫なし')
    elif status:
        logging.info('在庫あり！購入可能です。')
        notification.notify(
            title='在庫通知',
            message='在庫あり！購入可能です。',
            app_name='Stock Checker'
        )
    else:
        logging.info('在庫情報の要素が見つかりませんでした。在庫がある可能性があります。')
        notification.notify(
            title='在庫通知',
            message='在庫情報の要素が見つかりませんでした。在庫がある可能性があります。',
            app_name='Stock Checker'
        )

def calculate_next_run_time():
    """次に実行する時間を計算する"""
    now = datetime.now()
    next_run = now.replace(second=EXE_SECOND, microsecond=0)
    if now.second >= EXE_SECOND:
        next_run += timedelta(minutes=1)
    return next_run

def check_stock():
    """在庫を定期的にチェックするメイン関数"""
    while True:
        next_run = calculate_next_run_time()
        time.sleep((next_run - datetime.now()).total_seconds())
        
        tree = get_web_data(URL)
        status = check_stock_status(tree)
        notify_stock_status(status)

if __name__ == '__main__':
    check_stock()