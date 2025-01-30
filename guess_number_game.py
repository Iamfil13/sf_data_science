import random

# Фиксируем seed для воспроизводимости результатов.
random.seed(50)

def guess_number(target:int = 25):
    """
    Функция угадывает загаданное число с помощью бинарного поиска.
    
    Аргументы:
    target (int) — загаданное число, по умолчанию 25.
    
    Возвращает:
    int — количество попыток, за которое число было угадано.
    """
    low, high = 1, 100

    attempts = 0
    
    while low <= high:
        attempts += 1
        guess = (low + high) // 2  # Бинарный поиск (деление пополам)
        
        if guess == target:
            return attempts
        elif guess < target:
            low = guess + 1
        else:
            high = guess - 1

def evaluate_algorithm(n_trials=1000):
    """
    Функция оценивает среднее количество попыток, необходимых для угадывания числа.
    
    Аргументы:
    n_trials (int) — количество повторений эксперимента (по умолчанию 1000).
    
    Возвращает:
    int — среднее количество попыток.
    """
    # Инициализируем переменную для суммирования попыток
    total_attempts = 0

    # Запускаем эксперимент n_trials раз
    for _ in range(n_trials):
        total_attempts += guess_number()

    return round(total_attempts / n_trials)

# Оценка качества алгоритма
average_attempts = evaluate_algorithm()
print(f"Количество попыток, за которое число было угадано: {guess_number}")
print(f"Среднее количество попыток: {average_attempts}")
