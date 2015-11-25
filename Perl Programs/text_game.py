#! /usr/bin/python
print('Welcome')
name = raw_input('Enter your name\t')
print('Hello ' + name)
weapon = raw_input('pick a weapon from this list to start your fucking awesome adventure [sword, bat, dildo]\t')
start = True
while start:
	if weapon.lower() == 'sword':
		print('You have picked up a kick ass flaming sword')
		weapon =  raw_input('Name your sword: \t')
		start = False
	elif weapon.lower() == 'bat':
		print('You have picked up a classic wooden bat (boring)')
		weapon =  raw_input('Name your bat: \t')
		start = False
	elif weapon.lower() == 'dildo':
		print('You have picked up a fucking purple dildo you pervert!')
		print('You can not play this game, you fucking freak!')
		weapon =  raw_input('Just fucking with you, you are sill a pervert, pick a name for your dildo:\t')
		start = False
	else:
		print('please pick a weapon from the list jackass!')
		start = True

startgame = raw_input('Well ' + name ' you have named your weapon ' + weapon + ', now that shit is done with, want to begin [y,n]')

if startgame.lower() == 'yes' or 'y' or 'ye' or 'ys':
	hitpoint = 10
	print('Right, lets get started!')
else:
	print('Okay, prick... Thanks for wasting my time, fuck off!')