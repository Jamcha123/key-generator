#pykey 

pyKey is a python cli, random key generator.
Just clone it using ```git clone``` and then run the python3 command with the arguments.

``` python3 index.py -w <wordlist> -l <length> ```

The wordlist (has to be a text file) is for the letters, numbers and symbols you allow the program to use.

The length is how long you want the key to be.

example: 

    ```python3 index.py -w wordlist.txt -l 8``` // will get a random key of 8 length from wordlist.txt