
import json
_Data = None
_curYear = 2023
_startYear = 1980

def resolve_code(code, year=None):
    global _Data
    if _Data is None:
        with open("data.json", mode='r', encoding='utf-8') as f:
            _Data = json.load(f)
    years = _Data.get(str(code))
    if years is None:
        return ("", "", "")
    if year is None:
        year = str(_curYear)
    return tuple(years.get(str(year), ("", "", "")))

def resolve_history_code(code):
    years = dict()
    for year in range(_startYear, _curYear+1):
        coded = resolve_code(code, year)
        if any(coded):
            years[year] = coded
    return years

if __name__ == '__main__':
    print(resolve_code(110101)) # ('北京市', '', '东城区')
    print(resolve_code(110201)) # ('', '', '')
    print(resolve_code(110201, 1980)) # ('北京市', '', '昌平县')

    print(resolve_history_code(110201)) # {1980: ('北京市', '', '昌平县'), 1981: ('北京市', '', '昌平县')}
