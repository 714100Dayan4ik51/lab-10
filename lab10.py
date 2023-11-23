import random
import logging

# Настройка логгирования
logging.basicConfig(filename='guessing_game.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def guess_number(N, k):
    logging.info(f"Начинаем игру с  N={N} и k={k}")
    secret_number = random.randint(1, N)
    logging.info(f"Загаданное число: {secret_number}")

    for i in range(k):
        user_guess = int(input(f"Введите вашу {i + 1}-ю попытку: "))
        logging.info(f"Попытка пользовотеля: {user_guess}")

        if user_guess < secret_number:
            print("Загаданное число больше.")
            logging.info("Загаданное число больше введенного чсла пользователя.")
        elif user_guess > secret_number:
            print("Загаданное число меньше.")
            logging.info("Загаданное число меньше введенного чсла пользователя.")
        else:
            print("Вы угадали! Поздравляем!")
            logging.info("Пользователь угадал число.")
            return

    print("Попытки закончились. Загаданное число:", secret_number)
    logging.info("Закончились попытки.")


try:
    N = int(input("Введите верхнюю границу диапазона (целое число): "))
    k = int(input("Введите количество попыток (целое число): "))
    logging.info(f"Введена верхняя граница N: {N}")
    logging.info(f"Введенно количество попыток k: {k}")
    guess_number(N, k)
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите целое число.")
    logging.error("Ошибка ввода.")
except Exception as e:
    print("Произошла ошибка:", e)
    logging.error("Произошла ошибка.")
