# NAVIlauncher

Лаунчер Minecraft с каталогом клиентов, аккаунтами, помощником, чатом и музыкой.

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
Чат работает сразу, без настройки: сообщения идут через публичный MQTT-брокер
`broker.hivemq.com` (топик `navilauncher/chat/v1`), резервные — `broker.emqx.io` и
`test.mosquitto.org`. Ключи и сервер не нужны.

История не хранится: участник видит сообщения, отправленные после его подключения.
Брокер публичный, поэтому не пишите туда личное.

Свой сервер (если нужен контроль и история) — `chat/chat_server.py`:

```bash
python chat/chat_server.py 8765
```

и в конфиг лаунчера:

```json
{ "chat_url": "http://<адрес-сервера>:8765/messages" }
```

Если `chat_url` задан, лаунчер использует свой сервер вместо MQTT.

## Музыка
Вкладка «МУЗЫКА»: встроенные радио-потоки (Europa Plus, DFM, Record Chill, SomaFM),
папка «Моя музыка» и любые плейлисты из `music.json` в этом репозитории.

Свои файлы кладутся в `%APPDATA%\NAVIlauncher\music` (mp3, ogg, wav, flac, m4a, aac).

Формат `music.json`:

```json
{
  "playlists": {
    "Ночной дрифт": [
      {"title": "Трек 1", "url": "https://example.com/track1.mp3"}
    ]
  }
}
```
