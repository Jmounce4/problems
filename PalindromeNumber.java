/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package leetcodesolutions;

/**
 *
 * @author Julian
 */
public class PalindromeNumber {
    public boolean isPalindrome(int x) {
       int temp = x;
       int r = 0;
       int newNumber = 0;
        while (x > 0) {
     r =( x % 10);
     newNumber = (newNumber*10)+r;
     x = x / 10;
}
 if (newNumber == temp){
     return true;
 } else{
     return false;
 }
    }
}
