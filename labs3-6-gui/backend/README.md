Для запуска backend части: 
1. **python -m venv venv** - установка виртуального окружения
2. Активация виртуального окружения:
    - **source venv/bin/activate** - для Linux
    - **venv\Scripts\activate** - для Windows
3. **pip install -r requirements.txt** - установка всех необходимых библиотек
4. **uvicorn main:app** - запуск веб-сервера