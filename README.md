# xzqh

历史行政区划代码（1980-2023）。从 https://www.mca.gov.cn/n156/n186/index.html 拉取数据。

- resolve_code(code) 解析最新（2023年）的行政区划
- resolve_code(code， year) 解析指定年份的行政区划
- resolve_history_code(code) 解析行政区划代码，在每年的意义

```
import xzqh
print(xzqh.resolve_code(110101)) # ('北京市', '', '东城区')
print(xzqh.resolve_code(110201)) # ('', '', '')
print(xzqh.resolve_code(110201, 1980)) # ('北京市', '', '昌平县')

print(xzqh.resolve_history_code(110201)) # {1980: ('北京市', '', '昌平县'), 1981: ('北京市', '', '昌平县')}
```

数据按照 (省级,市级,区县级) 元组形式返回，如果没有对应的数据，返回 ('', '', '')。

## 数据管理

原始数据放在 data 目录中，采用 {year}.txt 命名，其中每行满足 ^/d{6} 的会解析为行政区划数据。

运行 create_data_json.py 代码可以生成 data.json 和 data_pretty.json 文件