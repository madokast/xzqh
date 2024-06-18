import xzqh
print(xzqh.resolve_code(110101)) # ('北京市', '', '东城区')
print(xzqh.resolve_code(110201)) # ('', '', '')
print(xzqh.resolve_code(110201, 1980)) # ('北京市', '', '昌平县')
