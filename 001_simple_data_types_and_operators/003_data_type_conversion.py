# Data type conversion in Python
int_var = 500
float_var = 50.9
string_var_num = '123.2'
string_var_txt = 'Hello world'

# Converting data types
# Convert 'int' into 'float' and backwards
print(int_var, type(int_var))
int_var = float(int_var)
print(int_var, type(int_var))
#
# print(float_var, type(float_var))
# float_var = int(float_var)
# print(float_var, type(float_var))
#
# # Convert 'str' into 'float' or 'int'
# print(string_var_num, type(string_var_num))
# string_var_num = float(string_var_num)
# print(string_var_num, type(string_var_num))
#
# print(string_var_num, type(string_var_num))
# string_var_num = int(string_var_num)
# print(string_var_num, type(string_var_num))
#
# # # Impossible conversion (will cause error)
# # print(string_var_txt, type(string_var_txt))
# # string_var_txt = int(string_var_txt)
# # print(string_var_txt, type(string_var_txt))
#
# # Converting into 'boolean'
# # 'int' into 'bool' - 0 will turn into 'False' other numbers into 'True'
# print(int_var, type(int_var))
# int_var = bool(int_var)
# print(int_var, type(int_var))
#
# # 'float' into 'bool' - 0.0 will turn into 'False' other numbers into 'True'
# print(float_var, type(float_var))
# float_var = bool(float_var)
# print(float_var, type(float_var))
#
# # 'str' into 'bool'
# str_var = 'True'
# # str_var = 'true'
# # str_var = 'Hello world!'
# # str_var = 'False'  # Will still return 'True'
# # str_var = ''  # Only empty 'str' will return 'False'
#
# print(str_var, type(str_var))
# str_var = bool(str_var)
# print(str_var, type(str_var))
