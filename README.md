# NAVIlauncher

Лаунчер Minecraft с каталогом клиентов, аккаунтами и автообновлением.

## Скачать
Свежий exe — в разделе Releases: https://github.com/zakatik642-pixel/navi-launcher/releases/latest

## Каталог клиентов
Список читается из `catalog.json` в этом репозитории, архивы клиентов лежат в
[zakatik642-pixel/navi-catalog](https://github.com/zakatik642-pixel/navi-catalog/releases).

## Помощник (ИИ)
Вкладка «ПОМОЩНИК» работает офлайн: подсказывает установку клиентов, обновление,
Java, память, ник, роли и разбор ошибок.

Свободные ответы включаются ключом OpenAI-совместимого API в `%APPDATA%\NAVIlauncher\config.json`
(в публичной сборке — `config-user.json`):

```json
{
  "ai_api_key": "sk-...",
  "ai_base_url": "https://api.openai.com/v1/chat/completions",
  "ai_model": "gpt-4o-mini"
}
```

`ai_base_url` и `ai_model` необязательны. Без ключа помощник отвечает локально и никуда не ходит.
