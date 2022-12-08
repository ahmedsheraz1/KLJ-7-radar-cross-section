Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from multiprocessing import Process
p = Process(target=print, args=[150])
p.run()
150
p = Process(target=print, args=(100,))
p.run()
100
