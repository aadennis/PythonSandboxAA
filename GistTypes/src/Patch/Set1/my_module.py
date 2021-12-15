from GistTypes.src.Patch.Set1.db import db_write

def f_a():
    x  = call_db_write()
    return x + 1

# note the indirection for purposes of mocking.
# Originally, this was a direct call to db_write.
def call_db_write():
    return db_write()

if __name__ == '__main__':
    x = f_a()
    print(x)