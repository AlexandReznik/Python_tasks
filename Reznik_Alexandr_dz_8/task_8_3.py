from functools import wraps

def type_logger(calc_cube):
   def decorator(*nums, **kwargs):
      for i in nums:
         print('--------')
         print(f'{i}: {type(i)},')
      for args_name, number in kwargs.items():
         print('--------')
         print(f'{args_name}--{number}: {type(number)}')
   return decorator


@type_logger
def calc_cube(x):
   return x ** 3


print(calc_cube(46, 87.89, my_number='678'))


# --------
# 46: <class 'int'>,
# --------
# 87.89: <class 'float'>,
# --------
# my_number--678: <class 'str'>
# None
