# NAVIlauncher

Лаунчер Minecraft с каталогом клиентов, аккаунтами, помощником и общим чатом.

## Скачать
Свежий exe — в разделе Releases: https://github.com/zakatik642-pixel/navi-launcher/releases/latest

## Каталог клиентов
Список читается из `catalog.json` в этом репозитории, архивы клиентов лежат в
[zakatik642-pixel/navi-catalog](https://github.com/zakatik642-pixel/navi-catalog/releases).

## Помощник (ИИ)
Вкладка «ПОМОЩНИК» работает офлайн: установка клиентов, обновление, Java, память, ник, роли, ошибки.

Свободные ответы включаются ключом OpenAI-совместимого API в `%APPDATA%\NAVIlauncher\config.json`
(в публичной сборке — `config-user.json`):

```json
{
  "ai_api_key": "sk-...",
  "ai_base_url": "https://api.openai.com/v1/chat/completions",
  "ai_model": "gpt-4o-mini"
}
```

## Общий чат
Чат работает через собственный сервер: `chat/chat_server.py` (только стандартная библиотека).

```bash
python chat/chat_server.py 8765
```

Сервер нужно поднять там, куда достают игроки (VPS, домашний ПК с пробросом порта).
Адрес прописывается в конфиг лаунчера:

```json
{ "chat_url": "http://<адрес-сервера>:8765/messages" }
```

Сообщения хранятся в памяти сервера (последние 300) и пропадают при перезапуске.
Без `chat_url` вкладка «ЧАТ» показывает «Чат не настроен».
