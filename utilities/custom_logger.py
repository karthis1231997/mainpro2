import logging

class LogGen:

    def loggen():
        fileHandler = logging.FileHandler("C:\\Users\\hkarthis\\PycharmProjects\\mainpro2\\logs\\logfiles.log")
        logger = logging.getLogger()
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s',
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger













