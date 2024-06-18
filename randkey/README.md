#randkeyjs

randkeyjs is a npm module for generating random keys of a given length.

First, you install it from npm.

Second, you import generator module like so ``` import generator from 'randkeyjs' ```.

initialize it ``` let keys = new generator() ```

use genkey function ``` keys.genkey(wordlist, length) ```.

Wordlist: the charactors that you allow the program to use. 

Length: how long the key should be. 
