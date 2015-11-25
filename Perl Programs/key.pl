#! /usr/bin/perl 
while(10) {

use feature ':5.10';
while(10) {
$input = <>; #this creats an infinite loop
last if $input eq "exit/n"; #exit loop when user presses exit then enter
open(FILE, ">>log.txt");
print FILE $input;
}
close FILE;

}