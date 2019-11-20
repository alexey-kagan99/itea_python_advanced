class File(object):

    def __init__(self, name, method):
        self.file_obj = open(name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(' Exception was analyzed ')
        self.file_obj.close()

        return True


with File('file_name.txt', 'w') as opened_file:
    opened_file.undefined_function('Hello')
