#! /usr/bin/perl
print "Welcome\n";
print "Enter you name:\t";
$myname = <STDIN>;
chomp($myname);
START:
print "Hello, $ myname pick a weapon from this list to start your fucking awesome adventure [sword, bat, dildo]\n";
$weaponInput = <STDIN>;
chomp($weaponInput);
if (lc($weaponInput) =~ "sword") {
	print "You have picked up a sword of light\n";
	print "Name your sword:\t";
	$swordname = <STDIN>;
	chomp($swordname);	
	$weaponname = $swordname;
}
		elsif (lc($weaponInput) =~ "bat") {
		print "You have picked up a classic wooden bat\n";
		print "Name your bat:\t";
		$batname = <STDIN>;
		chomp($batname);
		$weaponname = $batname;
	}
			elsif (lc($weaponInput) =~ "dildo") {
				print "You have picked up a fucking purple dildo you pervert!\n";
				print "You cannot play this game you fucking freak!\n";
				print "Just fucking with you, you're still a pervert, pick a name for your Dildo:\t";
				$dildoname = <STDIN>;
				chomp($dildoname);
				$weaponname = $dildoname;
			}
else {
	print "please pick a weapon on the list jackass!\n";
	goto START;
}



print "Well $myname you have named your weapon $weaponname, now that shit is done with, want to begin [y,n]\n";
$answerchoice = <STDIN>;
chomp($answerchoice);

$hitpoint = 10;
END:
while($hitpoint > 0) {

if (lc($answerchoice) eq "y" or "yes" or "ye" or "ys") {
	print "Right lets get started!"
}
else {
	print "Okay prick...thanks for wasting my time, fuck off!\n";
}

print <<EOF
You may be aware of other text adventure games.  This game will not be like them.
This game will probably not be as good as them, so don't get your hopes up.
This game will require imagination.  This game will have profanity (if you couldn't tell
already).  Okay...So i guess this is the part where I describe the enviroment for you... 
but that requires to much imagination on my part so why don't you give me a landscape (ofcourse 
you'll have to choice, I don't want to give you to much freedom).
[Urban City or Classic Forest]?
EOF
;
print "\n";
EVO:
$gameEvnviroment = <STDIN>;
chomp($gameEvnviroment);
if(lc($gameEvnviroment) eq "urban city" or "classic forest"){
	
print "$myname enters a mysterious $gameEvnviroment with their $weaponname and sees a Troll (lol you are sooo fucked)\n";
}
else {
	print "I gave you the environments to choice from dumbass, try again...\n";
	goto EVO;
}

print "\nThis is also a good time to introduce a health bar...you have $hitpoint hp\n";

TRL:
print "What do you do? Enter letter choice:\n";
print "a) fuck him up with $weaponname! hoo-rah!\n";
print "b) run like a bitch!\n";
print "c) Throw weapon at the troll whilst running at it, kick him in the balls and I retrieve my $weaponname
and cut that bitches head off.\n";
print "\n";


$trollChoice = <STDIN>;
chomp($trollChoice);

if(lc($trollChoice) eq "a") {
	$hitpoint--;
	print "You managed to kill the Troll...it was hard work, but you didn't win without damage. You loss 1 hp. $hitpoint hp remaining.\n"
}

		elsif(lc($trollChoice) eq "b") {
			$hitpoint--;
			print "You're such a fucking pussy! You escaped the Troll and loss 1 hp for being a bitch. You have $hitpoint hp remaining\n";
	}

			elsif(lc($trollChoice) eq "c") {
				print "Well you should be proud of yourself. You fucked that bitch up and didn't lose any hp.\n";
		}
else {
	print "I told you to fucking enter a letter choice\n";
	goto TRL;
}
FDIRECTION:

if($hitpoint <= 0){
	$hitpoint = 0;
	goto END;
}

elsif($hitpoint >= 10) {
	$hitpoint = 10;	
	print "Maxed hp\n";
}

$hitpoint = $hitpoint;
print "\n$hitpoint hp remaining\n";
print "You enter a 4 way intersection...which way do you want to go?\n";
print "[North, East, West, South]\n";
print "\n";
$firstDirectionInput = <STDIN>;
chomp($firstDirectionInput);

if (lc($firstDirectionInput) eq "north") {
	print "As you head North, you see a mountain.\n";
	print "Do you want to go up the mountain?[y,n]\n";
	my $choice = <STDIN>;
	chomp($choice);
	
	if(lc($choice) eq "y") { #start of choice input
		FIGHT_RUN_DRAGON:
		print "you get to the top and see a dragon, do you want fight it or run? [fight, run]\n";
		my $choice = <STDIN>;
		chomp($choice);
		
		if(lc($choice) eq "fight") { #fight or run
			print "The dragon is too powerful...your a dumbass.  It fucking ripped your body to pieces. You're dead.\n";
			$hitpoint = 0;
		}  #end of fight inout
		
		elsif (lc($choice) eq "run") { #run input
			print "You out run the dragon, but lost 5 hp. You have retured to the 4 way intersection\n";
			print "I suggest you avoid going north again\n";
			$hitpoint -= 5;
			print "You have $hitpoint hp remaining\n";
			
			goto FDIRECTION;	
		} # end of run input
		else { #invalid fight or run input
			print "Invalid command...dick.";
			goto FIGHT_RUN_DRAGON;
		} #end of invalid command
			
		}
		else{
		print "Heres that direction list again \n";
		goto FDIRECTION; #end of north adventure
	}
}# end of north input section
		

	elsif(lc($firstDirectionInput) eq "east") {  #begining of east input
		print "You walk into a silent clearing. \"It's too quiet here\" You tighten your hands around $weaponname \n";
		print "Fog starts creeps in... \a\n";
		print "You start to smell burning flesh.  \"I don't know if I should continue forward\"\n";
		print "Do you want to turn back[y,n]\n";
		my $choice = <STDIN>;
		chomp($choice);
			if(lc($choice) eq "n") { # start of choice
				print "You continue to walk forward and slowly begin to regret your choice\n";
				print "Suddendly a figure begins to appear from within the fog\n";
				SELF:
				print "You realize that you are standing in front of yourself...\n";
				print "a) Walk away slowy and return to the cross roads\n";
				print "b) Attack with $weaponname\n";
				print "c) Have a conversation with yourself\n" ;
				
				$selfChoice = <STDIN>;
				chomp($selfChoice);
				
				if(lc($selfChoice) eq "a") {
					goto SELF;
				}
				
				elsif(lc($selfChoice) eq "b") {
					print "How could you know...by killing yourself you've created a warp in space time.  You're dead.\n";
					$hitpoint = 0;
				}
				
				elsif(lc($selfChoice) eq "c") {
					print "You have a pleasant conversation with yourself.  You recall all your conquest.\n";
					print "As you turn your back the fucker stabs you...you limp away with your life and headback to the cross roads\n";
					print "He's a real ass whole ;)\n";
					print "\n";
					$hitpoint -= 6;
					goto FDIRECTION;					
				}
				
				else{
					print "Pick from the list jackass\n";
					goto SELF;
				}
				
			} # end of choice
			
			else { #if no was seleted
				print "Naviator shakes head...\"pussy\"\n";
				goto FDIRECTION;
			}
			
	} #end of east 




elsif(lc($firstDirectionInput) eq "west") {  #begining of west input
	print "As you begin walking a tree falls on you.\n";
	print "Yeah...I got lazy\n";
	$hitpoint = 0;
		
	} #end of west


elsif(lc($firstDirectionInput) eq "south") {  #begining of south input
	print "A beauty young goddess is in front of you\n";
	print "You and her start to get it in\a\n";
	print "hitpoints go up by 4\n";
	$hitpoint += 4;
	goto FDIRECTION;		
	} #end of south


else{
	print "Invalid direction input\n";
	goto FDIRECTION;
	
}

}#End of while statement


print "GAME OVER BITCH, $hitpoint HP REMAINING\a\n";
$now = localtime();
print "$now\n";