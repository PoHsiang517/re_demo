import time
import json
import requests
from datetime import datetime

def get_reservoir_stat():
    r = requests.get('https://www.taiwanstat.com/waters/latest')
    return r.json()[0]

def reservoir_now():
    reservoir_stat = get_reservoir_stat()
    replies = []
    for reservoir_name in ['翡翠水庫', '石門水庫']:
        r = reservoir_stat[reservoir_name]
        total = float(r['baseAvailable'])
        updated_at = r['updateAt']
        percentage = r['percentage']
        try:
            diff = float(r['daliyNetflow'])
            diff_percentage = diff / total * 100
            estimated_remain_days = percentage // diff_percentage
            up_or_down = '上升' if diff < 0 else '下降'
            replies.append((
                'text', f'{reservoir_name} 百分比：{percentage:.1f}%\n'
                    f'昨日水量{up_or_down}：{diff_percentage:.2f}% 預測剩餘天數：{estimated_remain_days}天\n'
                    f'更新時間：{updated_at}'
            ))
        except ValueError:
            replies.append((
                'text', f'{reservoir_name} 百分比：{percentage:.1f}%\n 昨日水量變化無法讀取，無法預測剩餘天數\n'
                    f'更新時間：{updated_at}'
            ))

    replies.append(('text', '其他水庫資訊請參考 https://water.taiwanstat.com/'))
    print(replies)
    return replies

reservoir_now()