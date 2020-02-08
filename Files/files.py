# from contextlib import contextmanager
# import os
#
#
# @contextmanager
# def file_manager(file, mode):
#     try:
#         f = open(file, mode)
#         yield f
#     finally:
#         f.close()
#
#
# with file_manager('text2.txt', 'r') as f:
#     f_contents = f.read()
#     print(f_contents)
#
# print(f.closed)
#
# @contextmanager
# def change_dir(destination):
#     try:
#         cwd = os.getcwd()
#         os.chdir(destination)
#         yield
#     finally:
#         os.chdir(cwd)
#
#
# with change_dir('Sample-Dir'):
#     print(os.listdir())
#     print(os.getcwd())
#
# print(os.getcwd())
#
