#! /usr/bin/perl 


my $Label = "Enter social:\t";
print "$Label\n";
chomp(my $Social=<STDIN>);

$pS = \$Social;
sub Hide {
	my $salt = '0...9';
	my $hidden = crypt @pS, $salt; 
	$secret = \$hidden;
}

Hide();

open FILE, ">Data.txt" or die $!;
print FILE "Social: ", $$secret, "\n";
close FILE;