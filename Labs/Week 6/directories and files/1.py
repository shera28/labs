import os

path = 'venv\Lib\site-packages'

arr = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
arr2 = [name for name in os.listdir(path)]
arr3 = [name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))]