"""Программа, угадывающая загаданное компьютером число
за минимальное количество попыток
"""

import numpy as np                      


def game_core(number: int = 1) -> int:
    """Функция для угадывания числа за минимальное количество попыток

    Args:
        number (int, optional): Число угадывания. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    # Локальные переменные 
    predict = np.random.randint(1, 101) 
    count = 0
    max_p = 101
    min_p = 1
    
    # Алгоритм, угадывающий загаданное число
    while predict != number:
        count += 1
        if predict > number:
            max_p = predict + 1
            predict = np.random.randint(min_p, max_p)
        else:
            min_p = predict - 1
            predict =  np.random.randint(min_p, max_p)
    
    return count


def score_game(random_predict) -> int:
    """Среднее количество попыток на угадыввание числа за 1000 подходов

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    np.random.seed(1) # Фиксируем seed для воспроизводимости кода
    
    # Локальные переменные
    count_ls = [] 
    random_array = np.random.randint(1, 101, size=(1000)) 
    
    for i in range(len(random_array)):
        count_ls.append(random_predict(random_array[i]))
        
    score = int(np.mean(count_ls))  
    
    print(f'Среднее количетсво попыток для угадывания числа = {score}')
    
score_game(game_core)