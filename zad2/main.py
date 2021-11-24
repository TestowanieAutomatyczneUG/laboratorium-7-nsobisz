class Password:
    def validPassword(self, haslo):
        """Takes two integers and adds them together to produce the result

        >>> c.validPassword("zaq1@WSX")
        True
        >>> c.validPassword("asdsad@#$213123HUIHI")
        True
        >>> c.validPassword("a@3E")
        False
        >>> c.validPassword("2323232231")
        False
        >>> c.validPassword("2323232#$#%#231")
        False
        >>> c.validPassword("1")
        False
        >>> c.validPassword("w")
        False
        >>> c.validPassword("%")
        False
        >>> c.validPassword("wasasafewfwf")
        False
        >>> c.validPassword("wasas234afewfwf")
        False
        >>> c.validPassword("W")
        False
        >>> c.validPassword("WSDFWEFW")
        False
        >>> c.validPassword("WSDFWEF1212W")
        False

        >>> c.validPassword(2)
        Traceback (most recent call last):
            File "C:/Users/Natalia/Desktop/lab07/main.py", line 34, in <module>
                print(c.validPassword(2))
            File "C:/Users/Natalia/Desktop/lab07/main.py", line 19, in validPassword
                raise TypeError("Invalid type: {}".format(type(haslo)))
        TypeError: Invalid type: <class 'int'>
        >>> c.validPassword([])
        Traceback (most recent call last):
            File "C:/Users/Natalia/Desktop/lab07/main.py", line 34, in <module>
                print(c.validPassword([]))
            File "C:/Users/Natalia/Desktop/lab07/main.py", line 19, in validPassword
                raise TypeError("Invalid type: {}".format(type(haslo)))
        TypeError: Invalid type: <class 'list'>
        >>> c.validPassword({})
        Traceback (most recent call last):
            File "C:/Users/Natalia/Desktop/lab07/main.py", line 34, in <module>
                print(c.validPassword({}))
            File "C:/Users/Natalia/Desktop/lab07/main.py", line 19, in validPassword
                raise TypeError("Invalid type: {}".format(type(haslo)))
        TypeError: Invalid type: <class 'dict'>
        >>> c.validPassword(1.2)
        Traceback (most recent call last):
            File "C:/Users/Natalia/Desktop/lab07/main.py", line 34, in <module>
                print(c.validPassword(1.2))
            File "C:/Users/Natalia/Desktop/lab07/main.py", line 19, in validPassword
                raise TypeError("Invalid type: {}".format(type(haslo)))
        TypeError: Invalid type: <class 'float'>


        """

        if type(haslo)!=str:

            raise TypeError("Invalid type: {}".format(type(haslo)))

        else:
            contains_digit = any(map(str.isdigit, haslo))
            is_upper = any(map(str.isupper, haslo))
            special_ch = any(not h.isalnum() for h in haslo)
            if len(haslo)<8:
                return False
            elif contains_digit and is_upper and special_ch:
                return True
            else:
                return False


if __name__ == "__main__":

    import doctest
    doctest.testmod(extraglobs={'c': Password()})
