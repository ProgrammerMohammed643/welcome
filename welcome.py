import requests
import time
import json
# ------------ توكن ------------
API_KEY = '7696110235:AAGfHSLfVvH3VUMLahzHNWhHATYuKmxgNkE'
API_URL = f"https://api.telegram.org/bot{API_KEY}/"

def bot(method, datas=None):
    url = API_URL + method
    try:
        response = requests.post(url, data=datas, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Timeout error: The request took too long to complete.")
    except requests.exceptions.ConnectionError:
        print("Connection error: Failed to connect to the server.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
    return None

def handle_update(update):
    message = update.get('message')
    if not message:
        return
    
    from_id = message['from']['id']
    chat_id = message['chat']['id']
    
    if 'new_chat_members' in message:
        for new_member in message['new_chat_members']:
            chat_administrators = bot("getChatAdministrators", {'chat_id': chat_id})
            
            if chat_administrators:
                a_id = ""
                for admin in chat_administrators['result']:
                    if admin['status'] == "creator":
                        a_id = admin['user']['id']
                        break

                user_profile_photos = bot("getUserProfilePhotos", {'user_id': a_id, 'limit': 1})
                file_id = None
                if user_profile_photos and user_profile_photos.get('result'):
                    file_id = user_profile_photos['result']['photos'][0][0]['file_id']

                chat_info = bot("getChat", {'chat_id': a_id})
                if chat_info:
                    chat_title = message['chat']['title']
                    new_member_name = new_member['first_name']
                    msg = f"- نورت ياا قمر 🌗😘🤝 [{new_member_name}](tg://user?id={new_member['id']})\n│ \n└ʙʏ في {chat_title}"

                    keyboard = {
                        "inline_keyboard": [
                            [{"text": "مـالـك الـجـروب⚡️", "url": f"tg://user?id={chat_info['result']['id']}"}],
                            [{"text": "خدني لجروبك والنبي🥺♥️", "url": f"https://t.me/{bot('getMe')['result']['username']}?startgroup=True"}]
                        ]
                    }

                    if file_id:
                        bot('sendPhoto', {
                            'chat_id': chat_id,
                            'photo': file_id,
                            'caption': msg,
                            'reply_to_message_id': message['message_id'],
                            'reply_markup': json.dumps(keyboard),
                            'parse_mode': "Markdown"
                        })
                    else:
                        bot('sendMessage', {
                            'chat_id': chat_id,
                            'text': msg,
                            'reply_to_message_id': message['message_id'],
                            'reply_markup': json.dumps(keyboard),
                            'parse_mode': "Markdown"
                        })

def get_updates(offset=None):
    params = {'timeout': 100, 'offset': offset}
    response = bot("getUpdates", params)
    if response:
        return response.get('result', [])
    return []

def process_updates():
    offset = None
    retry_count = 0
    while True:
        try:
            updates = get_updates(offset)
            for update in updates:
                handle_update(update)
                offset = update['update_id'] + 1
            retry_count = 0
        except requests.exceptions.ConnectionError:
            retry_count += 1
            wait_time = min(60, 5 * retry_count)
            print(f"Connection error. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    process_updates()
