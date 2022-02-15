def val_checker(valid_check):
   def check_val(func):
      def wrap(*args):
         print('---------')
         result = func(*args)
         if args:
            for i in args:
               if not valid_check(i):
                  raise ValueError
         return result
      return wrap
   return check_val


def validation(x):
   if isinstance(x, int) and x >= 0:
      return True
   return False


@val_checker(validation)
def calc_cube(x):
   """Возведение числа в третью степень"""
   return x ** 3


#result = val_checker(calc_cube(7))

print(calc_cube(5))
# print(calc_cube())
print(calc_cube(-7))
#print(calc_cube('ss'))

# ---------
# 125
# ---------
# Traceback (most recent call last):
#   File "C:\PythonProjects\pythonProject\Python_tasks.git\Reznik_Alexandr_dz_8\task_8_4.py", line 31, in <module>
#     print(calc_cube(-7))
#   File "C:\PythonProjects\pythonProject\Python_tasks.git\Reznik_Alexandr_dz_8\task_8_4.py", line 9, in wrap
#     raise ValueError
# ValueError

