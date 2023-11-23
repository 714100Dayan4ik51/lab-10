import random
import logging

# Настройка логгирования
logging.basicConfig(filename='guessing_game.log', level=logging.INFO, format = '%(asctime)s - %(message)s')


def guess_number(N, k):
    logging.info(f"Начинаем игру с  N={N} и k={k}")
    secret_number = random.randint(1, N)
    logging.info(f"Загаданное число: {secret_number}")
