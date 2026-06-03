[ -d "inbox" ] || { echo "Ошибка: папка inbox не найдена"; exit 1; }

mkdir -p logs

# Запускаем Python и одновременно пишем лог в файл
python3 main.py "$@" | tee logs/run.log

# Сохраняем код выхода (0 = успех, остальное = ошибка)
STATUS=$?


# Выводим итог
if [ $STATUS -eq 0 ]; then
    echo "✅ Обработка завершена успешно"
else
    echo "❌ Ошибка при обработке. Статус: $STATUS"
fi


exit $STATUS