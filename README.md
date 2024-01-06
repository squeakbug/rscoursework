## Рекомендательная система по подбору произведений искусства с естественно-языковым интерфейсом, распознающим 15 фраз)

### Конфигурация

Создать файл `.env` по пути `recomendation_service/.env` со следующим содержимым:
```
TOKEN=<YOUR_TELEGRAM_TOKEN>
DATA_PATH_ROOT="../data"
```

### Сборка образа

```
docker compose build 
```

### Запуск

```
docker compose up -d
```
