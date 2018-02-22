'''class Time:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if hours < 0:
            self._hours = 0
        elif hours > 23:
            self._hours = 23
        else:
            self._hours = hours

    def get_minutes(self):
        return self._minutes

    def set_minutes(self, minutes):
        if minutes < 0:
            self._minutes = 0
        elif minutes > 59:
            self._minutes = 59
        else:
            self._minutes = minutes

    def get_seconds(self):
        return self._seconds

    def set_seconds(self, seconds):
        if seconds < 0:
            self._seconds = 0
        elif seconds > 59:
            self._seconds = 59
        else:
            self._seconds = seconds


def main1():
    time = Time()
    hours = int(input("Please enter hours: "))
    minutes = int(input("Please enter minutes: "))
    seconds = int(input("Please enter seconds: "))
    time.set_hours(hours)
    print(time.get_hours())
    time.set_minutes(minutes)
    print(time.get_minutes())
    time.set_seconds(seconds)
    print(time.get_seconds())


if __name__ == "__main__":
    main()
'''

class Time:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0

    def get_hours(self):
        return self.__hours

    def set_hours(self, hours):
        if hours < 0:
            self.__hours = 0
        elif hours > 23:
            self.__hours = 23
        else:
            self.__hours = hours

    hours = property(get_hours, set_hours)

    def get_minutes(self):
        return self.__minutes

    def set_minutes(self, minutes):
        if minutes < 0:
            self.__minutes = 0
        elif minutes > 59:
            self.__minutes = 59
        else:
            self.__minutes = minutes

    minutes = property(get_minutes, set_minutes)

    def get_seconds(self):
        return self.__seconds

    def set_seconds(self, seconds):
        if seconds < 0:
            self.__seconds = 0
        elif seconds > 59:
            self.__seconds = 59
        else:
            self.__seconds = seconds

    seconds = property(get_seconds, set_seconds)

def main():
    time = Time()
    hours = int(input("Please enter hours: "))
    minutes = int(input("Please enter minutes: "))
    seconds = int(input("Please enter seconds: "))
    time.hours = hours
    print(time.hours)
    time.minutes = minutes
    print(time.minutes)
    time.seconds = seconds
    print(time.seconds)


if __name__ == "__main__":
    main()



