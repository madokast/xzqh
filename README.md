# xzqh

历史行政区划代码（1980-2023）。从 https://www.mca.gov.cn/n156/n186/index.html 拉取数据。

- resolve_code(code) 解析最新（2023年）的行政区划代码
- resolve_code(code， year) 解析指定年份的行政区划代码

```
import xzqh
print(xzqh.resolve_code(110101)) # ('北京市', '', '东城区')
print(xzqh.resolve_code(110201)) # ('', '', '')
print(xzqh.resolve_code(110201, 1980)) # ('北京市', '', '昌平县')
```

