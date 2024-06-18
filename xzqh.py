
import json
_Data = None
_curYear = "2023"

def resolve_code(code, year=None):
    global _Data
    if _Data is None:
        with open("data.json", mode='r', encoding='utf-8') as f:
            _Data = json.load(f)
    years = _Data.get(str(code))
    if years is None:
        return ("", "", "")
    if year is None:
        year = _curYear
    return tuple(years.get(str(year), ("", "", "")))

if __name__ == '__main__':
    print(resolve_code(110101)) # ('北京市', '', '东城区')
    print(resolve_code(110201)) # ('', '', '')
    print(resolve_code(110201, 1980)) # ('北京市', '', '昌平县')
