from machine import RTC

class DateTimeType:
    _day = None
    _month = None
    _year = None
    _hour = None
    _minute = None
    _second = None
    
    def __init__(self, day, month, year, hour, minute, second):
        _day = day
        _month = month
        _year = year
        _hour = hour
        _minute = minute
        _second = second
        self._hastime_value = False
        self._hasdate_value = False
    
    @property
    def day(self):
        return _day
    @day.setter
    def day(self, value):
        if(value > 31) or (value < 0):
            raise ValueError
        else:
            _day = value
    
    @property
    def month(self):
        return _month
    
    @month.setter
    def month(self, value):
        if(value > 12) or (value < 0):
            raise ValueError
        else:
            _month = value
    
    @property
    def year(self):
        return _year
    
    @year.setter
    def year(self, value):
        if(value < 0):
            raise ValueError
        else:
            _year = value
    
    
    def __str__(self):
        return _day
    

class DateTime(DateTimeType):
    def __init__(self):
        self.rtc = RTC()
        
        
    def now(self):
        rtcdtm = self.rtc.datetime()
        dttm = f"{rtcdtm[0]}/{rtcdtm[1]}/{rtcdtm[2]}"
        def strftime(self, format):
            pass
            
        
    def strftime(self, formatstr):
        pass