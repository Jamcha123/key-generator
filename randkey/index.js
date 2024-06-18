import fs from 'fs';
import {} from 'crypto';

export default class generator{
    genKey(wordlist, length){
        if(typeof(wordlist) != "string"){
            throw new Error(wordlist + " is nor a string")
        }
        if(typeof(length) != "number"){
            throw new Error(length + " is not a number");
        }
        if(Number.isInteger(length) == false){
            throw new Error(length + " is not a integer");
        }
        let ans = ""
        let words = "" + wordlist + "".toString()
        for(let i = 0; i != length; i++){
            ans += words[Math.floor(Math.random() * words.length + 0)]
        }
        return ans
    }
}