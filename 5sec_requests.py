import requests
import time


# Функция для отправки GET запроса к endpoint'у /statistics и записи результата в файл
def fetch_statistics_and_write_to_file():
    try:
        # Отправляем GET запрос к /statistics endpoint'у нашего веб-приложения
        response = requests.get('http://localhost:5001/statistics')

        # Проверяем успешность запроса
        if response.status_code == 200:
            # Получаем количество обращений к /time endpoint'у из ответа
            time_requests_count = response.json()['time_requests_count']

            # Записываем полученное количество обращений в файл
            with open('statistics.txt', 'a') as f:
                f.write(f'{time_requests_count}\n')
        else:
            print(f'Ошибка при запросе: {response.status_code}')
    except Exception as e:
        print(f'Ошибка: {e}')


# Бесконечный цикл для вызова функции fetch_statistics_and_write_to_file каждые 5 секунд
while True:
    fetch_statistics_and_write_to_file()
    time.sleep(5)
