from libs.setup_logger import setup_logger


def logger_setup(cfg):
    """ Instantiates the logger by calling the function setup_logger() in the lib setup_logger.py"""

    micro_service_name = "ayomi_test"
    logger = setup_logger(cfg.LOGS_DIR, micro_service_name, debug_verbosity=cfg.LOG_VERBOSITY)
    if logger[0]:
        log = logger[1]
    elif logger[0] is False:
        print(("Unable to instantiate logs due to exception: {}. Exiting.".format(logger[1])))
        exit(1)
