from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Счетчик для подсчета количества обращений к /time endpoint'у
time_requests_count = 0

# Список для хранения информации о каждом обращении к /time endpoint'у
time_requests_info = []


# Endpoint для получения текущего времени
@app.route('/time', methods=['GET'])
def get_current_time():
    global time_requests_count
    global time_requests_info

    # Увеличиваем счетчик обращений к /time endpoint'у
    time_requests_count += 1

    # Записываем информацию о текущем обращении
    time_requests_info.append({
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

    # Возвращаем текущее время
    return jsonify({'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})


# Endpoint для получения статистики обращений к /time endpoint'у
@app.route('/statistics', methods=['GET'])
def get_time_requests_statistics():
    global time_requests_count

    # Возвращаем количество обращений к /time endpoint'у
    return jsonify({'time_requests_count': time_requests_count})


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
