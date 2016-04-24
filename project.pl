#!/usr/bin/perl
use strict;
use warnings;

print "Enter your name: "; #Asking a question
my $userword = <STDIN>;
chomp $userword;
exit 0 if ($userword eq "");

print "hi $userword \n";

print "lets figure up your tithe for this week";

print "How much did you make? ";
my $paycheck;
chomp $paycheck;
my $tithe = ($paycheck * 0.10);
print "Your tithe is $tithe \n";
