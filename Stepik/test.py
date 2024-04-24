from google.oauth2.credentials import ServiceAccountCredentials
from googleapiclient.discovery import build
from slack_sdk import WebClient
import time

# Учетные данные для доступа к Google Drive API
creds = ServiceAccountCredentials.from_json_keyfile_name('PATH/TO/CREDENTIALS.json')

# Создание клиента для Google Drive API
drive_service = build('drive', 'v3', credentials=creds)

# ID папки, которую нужно мониторить
folder_id = 'FOLDER_ID'

# Предыдущий список папок (для сравнения)
prev_folders = set()

# Учетные данные для доступа к Slack API
slack_client = WebClient(token='SLACK_BOT_TOKEN')

def check_new_folders():
    # Получение списка файлов/папок в нужной папке
    results = drive_service.files().list(
        q=f"'{folder_id}' in parents",
        fields="nextPageToken, files(id, name)"
    ).execute()

    # Обработка новых папок
    current_folders = set()
    for file in results.get('files', []):
        if file.get('mimeType') == 'application/vnd.google-apps.folder':
            folder_name = file.get('name')
            if folder_name.startswith('Dev_Build_') and folder_name not in prev_folders:
                # Отправка уведомления в Slack
                slack_client.chat_postMessage(channel='CHANNEL_ID', text=f'Новая папка: {folder_name}')
            current_folders.add(folder_name)

    # Обновление предыдущего списка папок
    prev_folders.clear()
    prev_folders.update(current_folders)

# Запуск проверки каждые 5 минут
while True:
    check_new_folders()
    time.sleep(300)