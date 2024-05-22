import logging
import json


class JsonAdapter(logging.LoggerAdapter):# наследник logging.LoggerAdapter
    def process(self, msg, kwargs): # msg-сообщение которое будет логироваться
        # kwargs- словарь с дополнительными аргументами
        json_msg = json.dumps(msg) # преобразование сообщения в json строку
        return json_msg, kwargs


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}',
                        filename='skillbox_json_messages.log')
    #создает экземпляр класса JsonAdapter, который наследует функциональность логгера из
    # logging.LoggerAdapter, и передает ему логгер, полученный с помощью logging.getLogger(name).
    # Это позволяет использовать логгер с функциональностью, определенной в классе JsonAdapter,
    # включая преобразование сообщений в JSON-строки.
    logger = JsonAdapter(logging.getLogger(__name__))

    logger.info('Пример сообщения с двойными кавычками: "экранируем их"')
    logger.info('"example"')
    logger.info('"axaxaxa"')
    logger.info('""')
    logger.info('dog')
    logger.info('dOg')
