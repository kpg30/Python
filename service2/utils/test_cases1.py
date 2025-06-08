from datetime import timedelta, date
from typing import Any, Dict

class TestCases1:
    
    @staticmethod
    def find_days(n: int) -> date:
        
        return date.today() - timedelta(n)
    
    @staticmethod
    def add_days(n: int) -> date:
        
        return date.today() + timedelta(n)
    
    @staticmethod
    def string_n_times(s: str, n: int) -> str:
        
        return (s * n)
    
    @staticmethod
    def to_dict(keys, values) -> dict[Any , Any]:
        
        return dict(zip(keys, values))
    
    
def main():
    
    print(date.today())
    n = 14
    find_day= TestCases1.find_days(n)
    print(find_day)
    
    n = 14
    find_day= TestCases1.add_days(n)
    print(find_day)
    
    name = 'a'
    count = 5
    string_n_times = TestCases1.string_n_times(name, count)
    print(string_n_times)
    
    keys = ['a','b','c']
    values = ['1','2','3']
    to_dict = TestCases1.to_dict(keys, values)
    print(to_dict)
       
if __name__ == '__main__':
    main()