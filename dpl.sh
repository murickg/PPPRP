# Сборка образов
docker build -t murick/flask-app -f dockerfile1 .
docker build -t murick/script -f dockerfile2 .

# Пуш образов в Docker Hub или другой репозиторий
docker push murick/flask-app
docker push murick/script

# Применение манифестов конфигураций
kubectl apply -f /Users/muradgamzatov/Desktop/ppprp/app_deployment.yaml
kubectl apply -f /Users/muradgamzatov/Desktop/ppprp/clusterip.yaml
kubectl apply -f /Users/muradgamzatov/Desktop/ppprp/script_deployment.yaml
