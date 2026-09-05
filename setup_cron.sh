#!/usr/bin/env bash
pkg install -y cronie
(crontab -l 2>/dev/null; echo "0 */6 * * * python $(pwd)/m82_macro_engine.py && python $(pwd)/m82_telegram_bot.py >> $(pwd)/cron_execution.log 2>&1") | crontab -
crond
echo "✅ Cron Service activo y ejecutándose en segundo plano."
