#!/bin/bash

LOG_FILE="access.log"
REPORT_FILE="report.txt"

total_requests=$(wc -l < "$LOG_FILE")
unique_ips=$(awk '{print $1}' "$LOG_FILE" | sort -u | wc -l)
methods_count=$(awk '{print $6}' "$LOG_FILE" | tr -d '"' | sort | uniq -c | sort -nr)
popular_url=$(awk '{print $7}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -n 1)


echo "Отчет по логам" > "$REPORT_FILE"
echo "=================" >> "$REPORT_FILE"
echo "Общее количество запросов: $total_requests" >> "$REPORT_FILE"
echo "Количество уникальных IP-адресов: $unique_ips" >> "$REPORT_FILE"
echo "Запросы по методам:" >> "$REPORT_FILE"
echo "$methods_count" >> "$REPORT_FILE"
echo "Самый популярный URL: $popular_url" >> "$REPORT_FILE"
