class Time:
    def __init__(self):
        '''
        As usual, we are defining our variables here.
        "__hours" will store the hours, "__minutes" will store the minutes, etc.
        The only difference here is the double underscore __, which means
        we don't want to let anyone (the main function) change these variables directly.
        Note that I've removed the parameters after the __init__ function above,
        because this would allow someone to change the object variables directly,
        which is what we are trying to avoid by using properties below.
        '''
        self.__hours = 0
        self.__minutes = 0 # the defaults are still set to 0
        self.__seconds = 0

    def get_hours(self):
        '''
        defining our "getter" as usual here, which we will
        attach to a property below
        '''
        return self.__hours

    def set_hours(self, hours):
        '''
        defining our "getter" as usual here, which we will
        attach to a property below
        '''
        if hours < 0:
            self.__hours = 0
        elif hours > 23:
            self.__hours = 23
        else:
            self.__hours = hours

    '''
    This is where we create the property "hours". The way I see it is we are creating a
    "fake" or "disguised" variable here. Now in the main function we can write:
    time.hours = whatever_hours_we_want
    It's as if "hours" is a variable for the Time class, only now when we set 
    time.hours = something, it is going to SET it in the exact way we told our
    SETTER to do it!
    For example, if we were to write:
    time.__hours = 42,
    it would actually set the __hours variable to 42, which sucks.
    But, if we write:
    time.hours = 42,
    it is going to pass "42" to the set_hours method, and therefore
    it will actually set time.hours = 23 like we want it to. Cool!
    
    Long story short, anybody writing stuff in the main function can go on
    blindly thinking they set time.hours = whatever, but under the hood, they 
    actually set time.__hours = whatever, AND it checked to make sure they didn't 
    put in a stupid number.
    '''
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

    '''
    This is the same concept here, only we are creating the property using different code.
    Here, it is as if there is a time.hours_simple variable. In the main function below,
    we want to print whatever is in this "fake" time.hours_simple variable, but when we 
    we run it, it's actually going to run this function under the hood, and return an
    hour 1-12, like we want.
    '''
    @property
    def hours_simple(self):
        if self.__hours > 12:
            self.__hours -= 12
            return self.__hours
        else:
            return self.__hours
    '''
    Now we create another "disguised" variable called "period", so now we can
    write time.period and it will return a value "AM" or "PM".
    It looks like an object variable, but it's really a function.
    '''
    @property
    def period(self):
        if self.__hours > 12:
            return "PM"
        else:
            return "AM"


    '''
    Here all the magic happens in the main function. Notice that none of these variable actually exist:
    time.hours
    time.minutes
    time.seconds
    time.hours_simple
    time.period
    None of these were ever defined as variables in our Time class.
    We can work with them AS IF they really are variables of the "time" object, but they are actually
    all functions that we have defined and added properties to.
    Neat.
    '''
def main():
    time = Time()
    hours = int(input("Please enter hours: "))
    minutes = int(input("Please enter minutes: "))
    seconds = int(input("Please enter seconds: "))
    time.hours = hours
    print("{} {}".format(time.hours_simple, time.period))
    time.minutes = minutes
    print(time.minutes)
    time.seconds = seconds
    print(time.seconds)


if __name__ == "__main__":
    main()
