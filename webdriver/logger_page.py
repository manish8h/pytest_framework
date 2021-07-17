
class LoggerClass():

    @staticmethod
    def writeFile(filename, message):
        file1 = open(filename, "a")
        file1.write(message)
        file1.close()
