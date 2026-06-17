# 8-16 Imports: Using a program that you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

import make_car_function as mcf
car = mcf.make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)