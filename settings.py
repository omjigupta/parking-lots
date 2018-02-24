class Settings():
    '''
    1. For inputs from file,        Change _INPUT_FILE_OR_TERM = 1  (Default)
       For inputs from terminal,    Change _INPUT_FILE_OR_TERM = 0
    2. Change file path by changing  _INPUT_FILE_PATH
    '''
    def __init__(self):
        self._INPUT_FILE_OR_TERM = 0
        self._INPUT_FILE_PATH = 'input.txt'

    def get_input_type(self):
        return self._INPUT_FILE_OR_TERM

    def get_input_file(self):
        return self._INPUT_FILE_PATH
