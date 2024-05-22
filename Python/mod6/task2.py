import getpass
import logging
import re

logger=logging.getLogger('password')

def is_strong_password(password):
    with open('words.txt', 'r') as file:
        words = file.read().lower().split()
        for word in words:
            if len(word) > 4 and word == password.lower():
                return False
        return True


def input_passowrd():
    logger.debug('начало')
    password:str=getpass.getpass()
    if not password:
        logger.warning('пустой пароль')
        return False
    try:
        a=is_strong_password(password)
        if a== True:
            logger.debug('все хорошо')
            return True
    except ValueError as ex:
        logger.exception('incorrect password', exc_info=ex)
    return  False

if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG)
    count_number =3
    while count_number >0:
        if input_passowrd():
            exit(0)
        count_number-=1
        if count_number > 0:
            print(f'У вас осталось {count_number} попыток.')
    logger.error('триждый ввели неправильный пароль')
    exit(1)