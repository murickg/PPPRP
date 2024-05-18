# ПППРП

## Задание 2

Перевести приложение из предыдущего задания для работы через Istio. Для этого:
* написать скрипт для запуска Istio в вашем кластере, и настройки добавления лейблов для того, чтобы Istio начал автоматически внедрят sidecat контейнеры к вашим приложениям в Kubernetes. Также, в этом скрипте, при запуске Istio в вашем кластере, необходимо указать настройку, которая запрещает внешний трафик по умолчанию, если нет необходимых манифестов.
* написать все необходимые манифесты, чтобы теперь весь входящий трафик шел через Ingress Gateway
* теперь при обращении на endpoint GET /time вашего приложения, оно должно делать запрос на http://worldtimeapi.org/api/timezone/Europe/Moscow и возвращать пользователю значение поля datetime из запроса выше.
* создать манифейсты, которые разрешают внешний трафик на worldtimeapi.org
* в readme проекта опишите куда надо сделать запрос, чтобы получить результат(оставить с предыдущего задания, если ничего не поменялось).


### 1 step

Запуск узла minikube:
```bash
minikube start
```

### 2 step 

Установим Istio
```bash
curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.22.0 TARGET_ARCH=x86_64 sh -
```
Переместимся в каталог пакетов Istio
```bash
cd istio-1.21.0
```
Добавьте клиент istioctl в свой путь
```bash
export PATH=$PWD/bin:$PATH
```
Для этой установки мы используем демонстрационный профиль конфигурации.

```bash
istioctl install --set profile=demo -y --set meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY
```
Добавьте метку пространства имен, чтобы проинструктировать Istio автоматически внедрять прокси Envoy sidecar при последующем развертывании приложения:
```bash
kubectl label namespace default istio-injection=enabled
```
### 3 step

Создание docker-образов и применение манифестов приложения, скрипта и сервиса
```bash
sh dpl.sh
```

### 4 step 

Соединение с нашим LoadBalancer сервисом
```bash
minikube tunnel
```

### 5 step
Во втором терминале получим URL-адрес для подключения к нашему сервису
```bash
minikube service web-service
```
Добавив `/time` или `/statistics` к полученному URL, появится доступ к текущему времени и статистике заходов на сайт  

### 6 step
Чтобы прочитать файл `statistics.txt`, при помощи `kubectl get pods` получим название пода со скриптом.
Дальше вводим 
```bash
kubectl exec -it <pod_with_script_name> -- /bin/bash
cat statistics.txt
```
и получаем доступ к статистике.
