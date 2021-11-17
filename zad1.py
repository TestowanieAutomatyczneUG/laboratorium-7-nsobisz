

class FizzBuzz:
    def gamewithDocString(self, liczba):

        """Fizzbuzz game

                >>> f.gamewithDocString(5)
                'Buzz'
                >>> f.gamewithDocString(15)
                'FizzBuzz'
                >>> f.gamewithDocString(3)
                'Fizz'
                >>> f.gamewithDocString("5")
                'Buzz'
                >>> f.gamewithDocString("15")
                'FizzBuzz'
                >>> f.gamewithDocString("3")
                'Fizz'
                >>> f.gamewithDocString(1)
                '"1"'
                >>> f.gamewithDocString("2")
                '"2"'
                >>> f.gamewithDocString([1])
                Traceback (most recent call last):
                    File "H:/nsobisz/Desktop/sobisz/pythonProject7/main.py", line 63, in <module>
                        print(f.gamewithDocString([1]))
                    File "H:/nsobisz/Desktop/sobisz/pythonProject7/main.py", line 45, in gamewithDocString
                        raise TypeError("Invalid type: {}".format(type(liczba)))
                TypeError: Invalid type: <class 'list'>

                >>> f.gamewithDocString(1.1)
                Traceback (most recent call last):
                    File "H:/nsobisz/Desktop/sobisz/pythonProject7/main.py", line 69, in <module>
                        print(f.gamewithDocString(1.1))
                    File "H:/nsobisz/Desktop/sobisz/pythonProject7/main.py", line 51, in gamewithDocString
                        raise TypeError("Invalid type: {}".format(type(liczba)))
                TypeError: Invalid type: <class 'float'>
                >>> f.gamewithDocString((1,2))
                Traceback (most recent call last):
                    File "H:/nsobisz/Desktop/sobisz/pythonProject7/main.py", line 84, in <module>
                        print(f.gamewithDocString((1,2)))
                    File "H:/nsobisz/Desktop/sobisz/pythonProject7/main.py", line 66, in gamewithDocString
                        raise TypeError("Invalid type: {}".format(type(liczba)))
                TypeError: Invalid type: <class 'tuple'>

                >>> f.gamewithDocString("ala")
                Traceback (most recent call last):
                    File "H:/nsobisz/Desktop/sobisz/pythonProject7/main.py", line 83, in <module>
                        print(f.gamewithDocString("ala"))
                    File "H:/nsobisz/Desktop/sobisz/pythonProject7/main.py", line 52, in gamewithDocString
                        liczba1 = int(liczba)
                ValueError: invalid literal for int() with base 10: 'ala'

                >>> f.gamewithDocString({"a":1})
                Traceback (most recent call last):
                    File "H:/nsobisz/Desktop/sobisz/pythonProject7/main.py", line 97, in <module>
                        print(f.gamewithDocString({"a":1})
                    File "H:/nsobisz/Desktop/sobisz/pythonProject7/main.py", line 79, in gamewithDocString
                        raise TypeError("Invalid type: {}".format(type(liczba)))
                TypeError: Invalid type: <class 'dict'>


                >>> f.gamewithDocString(None)
                Traceback (most recent call last):
                    File "H:/nsobisz/Desktop/sobisz/pythonProject7/main.py", line 102, in <module>
                        print(f.gamewithDocString(None))
                    File "H:/nsobisz/Desktop/sobisz/pythonProject7/main.py", line 84, in gamewithDocString
                        raise TypeError("Invalid type: {}".format(type(liczba)))
                TypeError: Invalid type: <class 'NoneType'>


            """

        if type(liczba) == str:
            try:
                liczba1 = int(liczba)
                if liczba1 % 15 == 0:
                    return "FizzBuzz"
                elif liczba1 % 3 == 0:
                    return "Fizz"
                elif liczba1 % 5 == 0:
                    return "Buzz"
                else:
                    p = "\"" + str(liczba) + "\""
                    return p
            except TypeError:
                raise TypeError("Invalid type: {}".format(type(liczba)))
        elif type(liczba) != int:
            raise TypeError("Invalid type: {}".format(type(liczba)))
        elif liczba % 15 == 0:
            return "FizzBuzz"
        elif liczba % 3 == 0:
            return "Fizz"
        elif liczba % 5 == 0:
            return "Buzz"
        else:
            p = "\"" + str(liczba) + "\""
            return p





if __name__ == "__main__":



    import doctest

    doctest.testmod(extraglobs={'f':  FizzBuzz()})
