[0.00 → 4.44] I think one of the main appeals of Go is that you don't really need to think about security
[4.44 → 6.36] as much as with other languages.
[6.62 → 12.00] Go is a memory-safe language, unless I'm mistaken, and the compiler is never going to let you
[12.00 → 16.68] do stupid stuff like create an array that is too small and then write stuff that goes
[16.68 → 17.08] out of it.
[17.28 → 18.12] It's just not possible.
[18.12 → 22.98] So it eliminates a lot of bug classes, which we call memory corruptions.
[23.10 → 24.12] It's just not going to happen.
[24.22 → 25.82] You cannot do this to yourself in Go.
[25.82 → 31.68] And it means that all the old school buffer overflows that plagued all the C and C++ programs
[31.68 → 35.66] for dozens of years are not going to ever happen in the Go language.
[35.76 → 40.76] It doesn't mean that the program is going to be perfectly safe from any security issues,
[40.76 → 45.86] but the issues are not going to be related to, oh, I made a programming mistake and there
[45.86 → 46.70] is a bug in my program.
[46.78 → 47.46] It's going to be exploited.
[47.60 → 50.38] It's going to be more related to design issues.
[50.38 → 55.96] What's up, friends?
[56.06 → 58.40] This episode is brought to you by Source graph.
[58.84 → 64.32] With the release of Source graph 4.0 and the Starship event just a few weeks behind us,
[64.52 → 70.12] it is super clear that Source graph is becoming not just Code Search, but a full-on code intelligence
[70.12 → 70.72] platform.
[71.12 → 74.10] And I'm here with Joel Porter, product manager of Code Insights for Source graph.
[74.58 → 79.20] Joel, this move from Code Search to Code Intelligence is a huge deal.
[79.20 → 83.92] How would you explain this feature, Code Insights, if you're just talking to folks in the hallway
[83.92 → 85.56] track of your favourite conference?
[86.18 → 89.74] I would really start with technical because before I was a product manager, I used to be
[89.74 → 90.40] an engineer as well.
[90.68 → 94.42] And it's really cool and exciting just to be able to say, we're going to turn your code
[94.42 → 95.56] base into a database.
[96.06 → 100.12] And the structured language that you need to interact is just the ability to write a code
[100.12 → 101.80] search, you know, literal search.
[101.94 → 102.66] That's totally fine.
[102.80 → 106.08] Regular expression, you know, that'll give you a few more advanced options, even a structural
[106.08 → 106.44] search.
[106.90 → 111.46] But the number of long tail possibilities that unlocks, truly the journey of building
[111.46 → 115.56] this product was just saying, well, we've just unlocked, you know, an infinite number
[115.56 → 116.18] of possibilities.
[116.62 → 120.24] We got to figure out some immediate use cases so we can start to, you know, invest in this
[120.24 → 121.28] product, build it and sell it.
[121.74 → 125.52] But we're only getting started in terms of the number of uses that we're uncovering for
[125.52 → 125.70] it.
[126.04 → 130.04] The story I told you about discovering like version tracking turned out to be a really important
[130.04 → 133.62] use case that wasn't even on our roadmap six months prior to discovering that as we
[133.62 → 136.44] are already planning to launch this product until we talked to enough folks, realized
[136.44 → 139.84] this was a problem and then found, well, oh, that's like a simple regular expression
[139.84 → 143.34] capture group that you can just plug right in because we really built this system to
[143.34 → 145.08] not limit the power of what we built.
[145.18 → 148.06] We don't want to give you like three out-of-the-box templates, and you can only change
[148.06 → 149.18] like one character or something.
[149.28 → 152.18] It's truly like the templates are there to hold your hand and get you started.
[152.30 → 155.76] But if you can come up with anything you want to track in your code base, you can do
[155.76 → 156.46] that with Code Insights.
[156.70 → 157.36] I love it.
[157.40 → 157.86] Thank you, Joel.
[157.86 → 163.68] So right now there is a treasure trove of insights just waiting for you living inside
[163.68 → 164.30] your code base.
[164.46 → 167.32] Your code base is now a queryable database.
[167.38 → 168.34] Thanks to Source graph.
[168.86 → 172.68] This opens up a world of possibilities for your code and the intelligence you can gain from
[172.68 → 172.92] it.
[173.18 → 178.54] A good next step is to go to about.sourcegraph.com slash code dash insights.
[178.72 → 180.02] The link will be in the show notes.
[180.36 → 182.86] See how the teams are using this awesome feature.
[182.86 → 187.94] Again, about.sourcegraph.com slash code dash insights.
[188.30 → 190.58] Again, this link is in the show notes.
[205.74 → 206.58] Let's do it.
[207.28 → 208.22] It's go time.
[208.92 → 210.36] Welcome to go time.
[210.36 → 213.58] Your source for diverse discussions from all around the Go community.
[214.06 → 216.70] Check out our back catalogue at go time.fm.
[217.02 → 221.66] There you'll find the most popular episodes, our favourites, and a request form so you can
[221.66 → 223.90] let us know what you want to hear about on the pod.
[224.26 → 228.80] Special thanks to our partners at Vastly for shipping our shows superfast to wherever you
[228.80 → 229.04] listen.
[229.30 → 230.78] Check them out at fastly.com.
[231.22 → 232.86] And to our friends at fly.io.
[233.22 → 235.20] Host your app servers close to your users.
[235.48 → 236.32] No ops required.
[236.64 → 238.44] Learn more at fly.io.
[238.44 → 239.46] Okay, here we go.
[240.36 → 245.02] Hello, everyone who is joining us today on a Wednesday of the recording.
[245.36 → 249.18] We normally record on a Tuesday, but we have a very special guest, so we need to make a
[249.18 → 250.76] very special event about that.
[251.38 → 252.40] Ian is my co-host today.
[252.48 → 252.82] Hi, Ian.
[253.14 → 253.88] Hey, how are you doing, Natalie?
[254.22 → 254.60] Good.
[254.76 → 257.80] I'm very excited to have Ivan today join us.
[257.92 → 258.16] Yeah.
[258.32 → 259.48] Ivan Kwiatkowski.
[260.02 → 262.10] Also known on Twitter as Justice Rage.
[262.24 → 266.10] You are a senior security researcher at Kaspersky.
[266.10 → 266.58] Yes.
[266.76 → 267.00] Hello.
[267.14 → 268.16] Very happy to be here.
[268.54 → 268.80] Indeed.
[268.96 → 274.78] So I work in the threat intelligence field and my daily work involves looking at malware
[274.78 → 276.36] and writing reports about it.
[276.48 → 281.24] Basically, the activity that I'm involved in is trying to figure out what the attackers
[281.24 → 285.04] are up to, what kind of tools they're using, methodologies, what types of victims they are
[285.04 → 287.10] after, and then we write stuff about it.
[287.66 → 291.76] And our customers read our reports, and then it allows them to figure out whether
[291.76 → 296.58] this group or this group is likely to attack them or not, depending on what type of information
[296.58 → 297.24] that they are after.
[297.46 → 302.36] And if so, how they may defend from those attacks by knowing more about the type of malware
[302.36 → 306.98] that they use, the type of attack vectors that they typically favour, and so on.
[306.98 → 313.98] So really, I spend my day in AIDA Pro most of the time, and sometimes as well, I do give
[313.98 → 319.18] out trainings for reverse engineering, either in universities or for our customers as well.
[319.48 → 324.82] And there is a very cool video that has two parts of you reverse engineering and malware
[324.82 → 328.12] written about a year ago that was written in Go, actually.
[328.40 → 328.74] Absolutely.
[329.10 → 330.88] And that was from the SolarWinds attack.
[331.18 → 331.60] Exactly.
[331.60 → 337.18] This specific example comes from the SolarWinds incident, which I'm pretty sure that most
[337.18 → 341.90] listeners will be aware of because it was such a high media impact case.
[342.20 → 346.64] To make a quick summary about it, what happened was a company called...
[346.64 → 348.08] I always get dogs mixed up.
[348.16 → 351.74] I think the name of the company is SolarWinds, and then the product is Orient IT, but maybe
[351.74 → 352.46] the other way around.
[352.78 → 355.06] I do really get confused about this all the time.
[355.18 → 356.58] I think the way you have it is right.
[356.82 → 357.34] Okay, great.
[357.50 → 359.32] That was really a 50-50 chance there.
[359.32 → 364.80] Anyway, this company got attacked, but it wasn't attacked for the information that it
[364.80 → 370.52] had because it was just a software company, which in itself had little value as an intelligence
[370.52 → 370.94] target.
[371.38 → 377.02] But the thing was that it had a high number of high-profile customers, and these customers
[377.02 → 382.18] were US government entities or big companies in the field.
[382.18 → 388.86] And what the attackers did was they were able to compromise the software build chain, and
[388.86 → 395.00] they were able to insert their own code inside the software that was then pushed to customers.
[395.38 → 399.82] And using this, they were able to create a backdoor that would be automatically deployed
[399.82 → 401.42] at all SolarWinds customers.
[401.42 → 407.84] And then, you know, maybe two weeks or three weeks later, because this very stealthy attack
[407.84 → 412.18] had a very long sleeping time, it stayed dormant for a while to make sure it would remain very
[412.18 → 412.60] stealthy.
[412.74 → 416.02] But after a while, then it would start connecting to the C2 server.
[416.24 → 420.66] And then for all the targets that were deemed interesting by the attacker, they would receive
[420.66 → 424.18] a second stage payload that would allow them to get it to the network and then collect
[424.18 → 425.14] intelligence and whatnot.
[425.14 → 431.82] So the very first stage of the attack was just some modification of the code of the
[431.82 → 432.52] original program.
[432.82 → 434.02] This part was written in .NET.
[434.32 → 439.24] But then the second part, which is called Sun Shuttle, was actually written in Go language.
[439.76 → 444.28] So it was, for me, like the first time I was getting involved in reverse engineering for
[444.28 → 444.96] the Go language.
[445.34 → 446.72] The learning curve was a little steep.
[447.36 → 451.40] But then again, I kind of used this as a learning experience, but also as an example
[451.40 → 456.18] in future reverse engineering courses for other people that might be interested in learning
[456.18 → 459.30] how to, well, how to reverse engineer Go programs.
[459.42 → 463.80] But also, I think if you are a Go enthusiast, reverse engineering can allow you to get to
[463.80 → 468.36] know more about how the language actually works under the hood, which I think is also very
[468.36 → 470.98] interesting from a software development point of view.
[471.42 → 473.90] So that's one like famous example of Go malware.
[474.24 → 477.66] Are there other famous ones written in Go that you can think of off the top of your head?
[477.92 → 478.08] Yeah.
[478.08 → 483.38] So from the same incident, one of the companies that was breached through the Sol winds incident
[483.38 → 485.94] was Mendicant, now belongs to Google.
[486.32 → 489.90] And they were the ones that actually detected that there was something wrong in their network
[489.90 → 490.60] and reported it.
[490.72 → 494.00] And so kudos to them, really a great job on figuring out that something was wrong.
[494.64 → 499.52] But one of the things that the attackers were very interested in was getting access to the
[499.52 → 504.90] tool set that Mendicant was using for their own penetration testing and red teaming engagements.
[504.90 → 509.90] And it so happens that the tools that they were using were actually written in Go language,
[510.06 → 513.76] which I think is fascinating from an analyst perspective.
[514.04 → 519.20] So I think there's an interesting discussion to have about why they chose this language for
[519.20 → 520.72] their own offensive tools.
[521.20 → 527.40] There are a number of other projects on GitHub, which I can probably think of one called Stowaway
[527.40 → 532.02] on the top of my head, which has been also reused and modified by some threat actors.
[532.36 → 534.32] We'll add a link to that in the show notes.
[534.44 → 535.14] That sounds interesting.
[535.34 → 536.06] Yeah, sure.
[536.44 → 537.38] It's a networking tool.
[537.50 → 542.04] It's really something that proxies and stuff in and out of a network that goes between protocols
[542.04 → 542.82] and that kind of stuff.
[542.90 → 543.86] It's written in Go language.
[544.02 → 548.74] Pretty annoying to reverse engineer because it's a lot of Go routines talking to each other.
[548.74 → 551.40] Very hard to figure out how it's architecture.
[551.40 → 557.46] And another example I can think about is I'm not 100% sure, but I do believe that a commercial
[557.46 → 564.72] backdoor called Brut Ratel, which is a big competitor or a new competitor maybe to Cobalt Strike,
[565.12 → 572.68] which places enormous emphasis on evading detection and being able to slip through EDR solutions,
[572.82 → 575.70] et cetera, is also written in Go language, I do believe.
[575.86 → 577.50] But I would have to double-check that.
[577.50 → 581.74] So these are examples of malware families written in Go language.
[581.84 → 584.30] And I think that over time, we're going to see more and more of them.
[584.74 → 586.04] Why do you think we're going to see more and more?
[586.28 → 587.58] Is there a specific reason?
[587.64 → 589.42] You mentioned that they were hard to reverse engineer.
[589.56 → 591.14] Is that part of it or all of it?
[591.36 → 593.54] Yeah, there are a few reasons.
[593.92 → 600.94] The first reason I think is probably related to the ease of use for the developers.
[601.06 → 605.68] I don't mean that Go is easier to program than other languages, but the fact that it generates
[605.68 → 610.74] statically built executables, binaries that are self-contained, that do not need any additional
[610.74 → 613.64] libraries, is kind of very comfortable for attackers.
[614.08 → 617.64] Like, you know, they create their backdoor, they send it to the victim, or, you know, they
[617.64 → 620.52] deploy it at the victim one way or the other, and then it just works, right?
[620.56 → 623.88] You don't have to think about, you know, is this DLL present on the system, or do I have
[623.88 → 626.22] to pull in additional libraries, et cetera?
[626.22 → 631.76] So this is something that makes running programs very easy on victim machines where you do not
[631.76 → 632.58] control the environment.
[632.58 → 636.94] A long time ago, like maybe 10 years ago, it was kind of a problem because you cannot
[636.94 → 639.88] send binaries that are two or three megabytes big to victims.
[640.04 → 644.66] You know if your attack vector is, you know, infected PDF or infected Word documents, then,
[644.76 → 649.14] you know, you cannot really send over email a PDF that ends up being five megabytes big
[649.14 → 651.58] because, you know, back in the day it would be rejected.
[651.82 → 656.46] Or maybe, you know, the victim, you know, has some limit on their mailbox, or maybe they
[656.46 → 660.06] have a slow connection that is not going to be able to retrieve that binary.
[660.06 → 663.78] In Europe or in the US, in the Western world, it used to be fine.
[663.88 → 667.78] But, you know, if you think about victims that are in Third World countries where the
[667.78 → 671.50] internet access is not as good, then it used to be some real, a real issue for attackers.
[671.86 → 676.24] Now that, you know, the internet connectivity is pretty much, well, at least way better in
[676.24 → 680.70] most parts of the world than having backdoors that are, you know, five or 10, maybe 20 megabytes
[680.70 → 682.80] is really not that much of an issue anymore, I think.
[682.80 → 690.18] Then, second very good reason for using Go as an offensive language is going to be that
[690.18 → 694.96] reverse engineering is difficult, which I will get back to, but also all these standard
[694.96 → 700.32] tools that we, as defenders, tend to use in order to figure out quickly if a program is
[700.32 → 703.28] malicious or is not, tend to kind of break with Go language.
[703.66 → 708.10] The reason for this, and it ties into the discussion of why reverse engineering Go is annoying for
[708.10 → 713.16] us is that Go tends to really do its own thing, like the assembly it generates really does not
[713.16 → 714.78] look like any other assembly.
[714.90 → 719.96] It's not like C, or it's not like C++ or Delphi that kind of tend to like to look like distant
[719.96 → 721.78] cousins or even brothers in some cases.
[722.52 → 729.64] Go really does things its own way and all the automated methods for analyzing code statically
[729.64 → 735.92] or all the maybe signatures you can recreate for Go language, et cetera, but all the tools
[735.92 → 740.80] that would try to recognize specific patterns in code are not going to work because the code
[740.80 → 743.52] generated by Go just looks like nothing you've seen before.
[743.52 → 745.12] So that's one reason.
[745.12 → 747.68] And the final reason is reverse engineering.
[747.68 → 754.40] It's really difficult for us because the constructs that are generated by the Go compiler tend to be
[754.40 → 755.76] very unfamiliar to us.
[755.76 → 758.56] And so the learning curve, I would not say it's that steep.
[758.56 → 762.72] Like you mentioned, Natalie, that I had released a few videos about it.
[762.72 → 766.56] I think, you know, by the end of the videos, you can have like a rough idea of how to approach those
[766.56 → 766.96] programs.
[766.96 → 771.28] So it's not that like, it's not like an obstacle that is insurmountable.
[771.28 → 773.36] It's something that eventually you will be able to figure out.
[773.36 → 780.80] But when you've been working on C or like similar looking code as C for 10 years, and
[780.80 → 786.16] sometimes learning something new is not something that you are easily going to do because you are,
[786.16 → 790.32] you have your comfort zone, and then you have to like to discover something different.
[790.32 → 793.52] And maybe you don't like to do this, and maybe you have, you know, 10 easy malware
[793.52 → 795.60] return C that are waiting in the, in the test list.
[795.60 → 799.52] And maybe you're going to work on those first because it will allow you to end your day earlier
[799.52 → 800.08] next Friday.
[800.08 → 800.40] Right.
[800.40 → 805.12] So you, you kind of mentioned that there's assembly differences that make it hard to recognize.
[805.12 → 808.88] Are there any like specific things that you've learned about Go under the hood from that,
[808.88 → 815.20] you know, like that differ from C like how functions are called in the assembly or something like that?
[815.20 → 816.56] Yeah, absolutely.
[816.56 → 820.72] So one of the major differences, it's not really about the assembly itself.
[820.72 → 825.28] It's about, you know, the static aspect of the executables is the fact that all the
[825.84 → 828.32] functions are pulled inside the final binary.
[828.32 → 832.72] And then you have this big program that's two megabytes or three megabytes big just for a
[832.72 → 833.04] print.
[833.04 → 834.08] Hello world.
[834.08 → 836.16] And now it's getting a bit better.
[836.16 → 841.76] I think IDA pro has made significant improvements in its later versions, but maybe two to three years
[841.76 → 845.20] ago when you were opening a Go program, you would have nothing recognized at all.
[845.20 → 851.04] Maybe you would be able to pull a few plugins here and there or Python scripts that may or may not
[851.04 → 851.28] work.
[851.92 → 856.16] And in that case, if you were lucky, you might have been able to create signatures for the
[856.16 → 859.92] well-known functions and maybe start from there, but it was really a huge ordeal.
[859.92 → 861.28] Now it's a bit better.
[861.28 → 867.36] So at least you are starting to get pretty reliably all the references to all the known functions.
[867.36 → 871.52] Beyond this, the calling convention is, well, I'm not going to say it's weird because like,
[871.52 → 873.52] it's, I mean, it's as valid as any other one.
[873.52 → 875.76] It's just not the same one that we are used to seeing.
[876.48 → 881.36] The main difference is that considering that Go can return multiple return values,
[881.92 → 886.72] then you cannot, you know, have the same system as we had to, as we had before.
[886.72 → 890.32] Like for instance, in the C program, the return value goes into EAX and that's it, right?
[890.32 → 891.28] No difference.
[891.28 → 893.76] I mean, the AX register of your CPU.
[893.76 → 897.84] When it comes to Go language, if you have three, four, or, you know, maybe more return values,
[897.84 → 902.24] you know, typically one return value and also some error objects, if I'm not mistaken,
[903.12 → 906.48] then you cannot put all that into a single CPU register.
[906.48 → 907.36] It just doesn't work.
[907.36 → 912.40] And so you tend to get values that, well, in the past, you would have all the arguments being
[912.40 → 917.84] passed through the stack, not through pushes, but direct moves from the, you know, from the
[917.84 → 919.68] value into the stack directly.
[919.68 → 924.40] So the instruction was not pushed, which are these assemblers, they are, you know, automated analysis
[924.40 → 924.64] tools.
[924.64 → 926.88] They just like to see push, push, push, and then call that.
[926.88 → 929.60] That's something that is easy for them to recognize.
[929.60 → 933.76] But Go would just do move this on the stack at this place, move this on the stack at this place,
[933.76 → 935.04] and then you go into another function.
[935.04 → 937.84] It knows because the compiler knows where the stuff ends up.
[937.84 → 938.64] So it figures it out.
[938.64 → 941.44] But you know, the Ida Pro looks at this and is like, what the hell is this?
[941.44 → 943.36] This memory has never been initialized before.
[943.36 → 944.24] I cannot show this to you.
[944.88 → 945.76] That was an issue.
[945.76 → 948.40] And then the return values were given back exactly the same.
[948.40 → 952.64] So the program would just move back all the return values onto the stack as well,
[952.64 → 955.36] at places that it would be able to figure out later.
[955.36 → 958.96] But then when you look at Ida Pro, then, you know, it sees, okay, values being moved on the
[958.96 → 959.20] stack.
[959.20 → 963.68] You go back into the calling function, and then you see references to the stack as well.
[963.68 → 966.96] But you know, the offsets are going to be different because since you are returning from a function,
[966.96 → 968.88] you know, things have shifted a little bit.
[968.88 → 971.44] And so the offsets are not well, do not work well anymore.
[971.44 → 975.68] And so this is like another issue that you have to face, like figuring out where your return values go.
[975.68 → 978.08] It still is, by the way, a terrible nightmare.
[978.80 → 983.12] And finally, there is this other key difference.
[983.12 → 989.04] And this difference is the fact that usually the C compiler and other similar compilers will tend to
[990.00 → 994.24] reserve some space on the stack for specific local variables.
[994.24 → 996.48] And this tends to be very reliable.
[996.48 → 997.84] It doesn't move too much.
[997.84 → 1001.52] So when you have some variable in C, you know, it gets used some part of the program.
[1001.52 → 1003.28] It's at one place on the stack, and then that's it.
[1003.28 → 1007.68] And if the program needs another local variable later on, then there's just another space located
[1007.68 → 1008.80] for this in the stack.
[1008.80 → 1011.52] And the Go compiler tends to be very smart about these things.
[1012.08 → 1016.08] And what it does is if it sees that, you know, there used to be a variable at some place on the
[1016.08 → 1021.04] stack, and it's not used anymore, then it will feel like it's totally okay to reuse the same space
[1021.04 → 1024.16] to store something else later, which makes total sense.
[1024.16 → 1026.24] I mean, do not use more memory than you need to, right?
[1026.24 → 1028.72] But the Go compiler is totally right in doing this.
[1028.72 → 1034.00] But for me, it's really, really a problem because what I do in IDA Pro is I try to figure out where
[1034.00 → 1035.84] the local variables are in the stack.
[1035.84 → 1039.44] I name those positions by saying, okay, this is the error variable.
[1039.44 → 1044.72] This is the I don't know, this is the integer that represents an iteration count or whatever.
[1044.72 → 1047.36] And I name or rename everything I can.
[1047.36 → 1052.48] And then eventually stuff starts to make sense because I know what represents what on the stack
[1052.48 → 1054.88] and I know what the variables are, et cetera.
[1054.88 → 1060.08] But the thing is, if one position on the stack does not consistently represent a specific variable,
[1060.08 → 1062.00] then I cannot rename things anymore, right?
[1062.00 → 1063.60] There's just no way for me to do this.
[1063.60 → 1068.08] And the tools that we have, such as IDA and Pitcher Hydra is going to function the same way.
[1068.08 → 1072.88] It's not going to allow me to say, okay, up to this point, this variable should be named like this.
[1072.88 → 1077.92] And then from there on, then it should have another name and then yet another, et cetera.
[1077.92 → 1082.88] So this is like a very, very difficult thing for us is that, you know, trying to track down variables
[1082.88 → 1086.64] and return values, even arguments is something extremely complex.
[1086.64 → 1090.32] And basically this is the normal flow of how you analyze a program.
[1090.32 → 1094.16] You try to figure out what the variables are, try to look at the functions and how they are called,
[1094.16 → 1095.60] what they return and that kind of stuff.
[1095.60 → 1100.08] And just, you know, doing those simple things that would be the basic operations and building blocks
[1100.08 → 1105.12] of trying to understand what is going on in some random program are in themselves,
[1105.12 → 1110.88] extremely complex operations due to like optimizations that were performed by the Go compiler.
[1110.88 → 1116.00] Now, the last thing I can mention is that since version probably 16.1 or something like this,
[1116.00 → 1120.08] or 1.16, I guess, in Go, the calling convention actually changed.
[1120.56 → 1125.36] And they do things even smarter now, which is pass some arguments through the registers and not through
[1125.36 → 1129.36] the stack. So for me, it doesn't change that much. Actually, it makes things a little bit easier
[1129.36 → 1133.44] because at least, you know, I know argument one is in EX, argument two is in EDX from memory.
[1133.44 → 1137.52] It might not be that one, but, you know, generally it's going to be in a fixed register,
[1137.52 → 1141.04] at least for the two first arguments. And so I know where they are, but that's way better.
[1141.60 → 1146.00] But, you know, overall, this doesn't change this bigger game of renaming things, which is not
[1146.00 → 1151.04] possible anymore. And then when it comes to the quick and easy mode, which is, you know, getting my
[1151.04 → 1156.08] super expensive IDEA Pro license that comes with a decompiler, then, you know, I just open the program,
[1156.08 → 1160.24] press F5, and hopefully you can read whatever's going on in the program. Well, that just doesn't
[1160.24 → 1164.08] work because, you know, the constructs that are generated by the Go compiler, especially,
[1164.08 → 1169.60] I think when it comes to function calls, is totally alien to IDA. And, you know, every time you try to
[1169.60 → 1176.16] decompile code that comes from the Go language, you just end up with something that makes absolutely
[1176.16 → 1183.12] no sense. Because again, IDA tries to recreate pseudo C code and pseudo C code has just no way of
[1183.12 → 1190.00] representing concepts like multiple return values or that kind of stuff. So this is the way that Go
[1190.00 → 1193.44] breaks everything that we hold dear in the reverse engineering world.
[1193.44 → 1198.56] For anybody who didn't watch the video or is not familiar with how to do reverse engineering, I can,
[1199.28 → 1204.96] in simple words, say that roughly you look at the instructions, and then you try to kind of see
[1204.96 → 1210.56] entry point is usually main. So this is probably function main. This is one thing that's being returned.
[1210.56 → 1216.08] And then you kind of try to follow that. Basically, this is what you do when you reverse engineer.
[1216.08 → 1221.12] Yeah. Actually, maybe I can say a few words about what reverse engineering is for people that, you
[1221.12 → 1226.24] know, might not be familiar with it. The general idea is that we try to understand what a program
[1226.24 → 1230.64] does, even though we do not have access to the source code. But this is the typical case for malware,
[1230.64 → 1234.64] because, you know, we cannot call up malware authors and tell them, okay, please show me the code,
[1234.64 → 1238.16] because I don't really understand what's going on there. They just, we don't know where they are.
[1238.16 → 1242.64] They don't want to be found, and they don't want to give us their code anyway. So what we have to do
[1242.64 → 1248.16] then is like, we have no other solution, but to look at the program and see what instructions the
[1248.16 → 1254.08] program is sending to the CPU and then try to figure out from there, based on those instructions
[1254.08 → 1260.00] that are working at the CPU level, what the higher level line of code that might have generated this type
[1260.00 → 1265.04] of instruction might have been. So it's not really, it's not entirely a guessing game because it's sort of a
[1265.04 → 1271.20] mostly exact science, but also it's a very unnatural operation to perform because this
[1271.20 → 1277.68] CPU language was really made for CPUs and machines. And for us humans, like it's extremely difficult to
[1277.68 → 1282.32] understand. Like it's really, it's really not something natural for human beings to read that,
[1282.32 → 1286.96] those instructions. It doesn't make sense to us. And it really requires a lot of effort to figure out
[1286.96 → 1292.16] what the programmer intent was just by looking at those instructions. And so this is why actually we are
[1292.16 → 1296.72] looking for reverse engineers. I mean, not just at Kaspersky, just the whole industry is looking for
[1296.72 → 1301.60] people that are able to do this because it's something that is, that most people find unpleasant.
[1301.60 → 1305.68] And I have to say myself, I do find it unpleasant most of the time, but you know, at the end of the
[1305.68 → 1309.84] day, when I am able to figure out what was actually happening in the program, I feel very good about
[1309.84 → 1316.32] myself. And so this is the reason why I still do this job, but overall, this is kind of a difficult
[1316.32 → 1321.52] thing to do, and it's kind of painful and takes a lot of time to be able to figure out even the
[1321.52 → 1324.88] the simplest programs. Especially when the tooling is not even there for you.
[1324.88 → 1331.68] Yes. Just for some reference, like the ratio between lines of say, Go to assembly,
[1331.68 → 1335.84] do you know what that ratio is? Just like a rough, it's like one to a hundred, one to a thousand, one to...
[1335.84 → 1339.04] It's a good question. It would depend on the complexity of the line. You know, in Go, I'm
[1339.04 → 1343.44] pretty sure that you can do function calls that are chained together in a pretty like in long lines.
[1343.44 → 1348.24] Maybe I'm not sure if it's like the compliant to the official Go styling code or something like this,
[1348.24 → 1353.44] but if you were to do this, then you would have a... I mean, let's take it from the other way. If you
[1353.44 → 1358.40] have some normal looking Go code, like a hello world or something like this, it would probably translate
[1358.40 → 1364.32] into 10 or 15 lines of assembly. So I would say the default would be 15 lines of assembly for one
[1364.32 → 1371.12] line of actual Go code. But then if you get up into lines of codes that are a bit more complex or that
[1371.12 → 1376.16] check or that return multiple return values or function calls, then this can get a bit bigger,
[1376.16 → 1380.16] but this is still going to be the right ballpark. Okay. Yeah. That gives me a good idea.
[1380.16 → 1384.32] What is it for other languages? Like, is it a lot more? Is it a lot less? Is it roughly the same?
[1384.32 → 1391.60] I would say it's probably going to be mostly the same. C++ tends to be very, like, tends to
[1391.60 → 1397.60] generate a lot of codes. It's very comparable to us to Go. C might be a bit more direct. Like the
[1397.60 → 1402.72] translation between C and assembly is going to be a bit more, how would I say it in English? The
[1402.72 → 1407.76] correspondence between C code and the assembly is going to be a bit more direct. That's it. But
[1407.76 → 1413.36] otherwise I would say this is like a common ratio for languages. The problem is not that Go generates
[1413.36 → 1417.60] more assembly. The problem is that the assembly generates, like, is not the one that we are used
[1417.60 → 1422.56] to seeing. And we don't like that. Interesting to see if in one or two years from now, it will be more
[1422.56 → 1428.64] supported and more pattern recognition working. Well, that's the thing, right? It kind of depends on the
[1428.64 → 1434.48] attackers. Like, if we do end up seeing more and more Go tools out there in the wild, then there
[1434.48 → 1440.96] is going to be pressure on the tool authors like IDF, like Hydra, etc. to implement better detection
[1440.96 → 1445.52] and, you know, better support for those languages. I'm pretty sure that since last time I tried using
[1445.52 → 1450.96] the compiler on some Go program, IDA has made improvements, and it's probably not as broken as it
[1450.96 → 1456.56] used to be. But if you keep seeing offensive tools running in Go, then I'm pretty sure that the tools will get better.
[1456.56 → 1461.76] We will still have to figure out how the Go assembly works, especially if it changes again in the future.
[1461.76 → 1466.48] But overall, at least the support in the last years has improved tremendously.
[1466.48 → 1472.24] And I think it will continue to do so, although also in the future, if there is a need to. And I would
[1472.24 → 1476.40] guess that Go is only going to become more prevalent when it comes to offensive software.
[1476.40 → 1478.08] Because of all the reasons that you mentioned.
[1478.08 → 1479.84] Yeah, exactly.
[1479.84 → 1485.92] Some specific questions. You mentioned that you were kind of thinking out loud about the behaviour you see
[1486.56 → 1492.88] in IDA Pro when you were looking at the Go code that you loaded there, or the binary of it that you
[1492.88 → 1498.56] loaded there. So I'm going to describe two things that you mentioned. Tell me how you think if it's
[1498.56 → 1503.36] good, if it's bad, how it is compared to other languages, just as an interesting kind of point.
[1503.36 → 1508.40] It can get too deep, so we'll try to keep it at a slightly higher level for everybody who's out of,
[1508.40 → 1514.40] of, was kind of hearing about this and not very well familiar. So for example, you mentioned that
[1514.40 → 1519.52] keeping to the next instruction lands you in another place in the code of the CPU instruction.
[1519.52 → 1524.08] Yeah, exactly. So this is something that was astounding to me, which is when I reverse
[1524.08 → 1528.88] engineer a program. So you can look at it statically in IDA Pro, which means you display the instructions
[1528.88 → 1533.92] and you read them like a book. Or there's another approach, which is not like opposite, but maybe more
[1533.92 → 1539.04] like a complement to it, which is to look at the program inside the debugger. You know, debugger,
[1539.04 → 1542.56] they just work exactly the same as in the software development world. Like you execute the code
[1542.56 → 1546.56] instruction by instruction or line by line, and you can see the state of the various variables.
[1546.56 → 1550.88] Except for us, you know, we don't have the source code, so it's not lines of code, it's just assembly
[1550.88 → 1556.40] instructions. But we can still watch them execute one by one, and we can see the CPU registers getting
[1556.40 → 1560.56] updated, etc. And when I was doing this with the Go programs, it turned out that I was very surprised to see that
[1560.56 → 1566.48] sometimes I would step from one instruction to the next and I would end up at a totally random place
[1566.48 → 1571.52] somewhere else in the program. And eventually, like by doing some Google searches, etc., I figured out
[1571.52 → 1576.80] that it is actually the... I don't know if it's the Go scheduler that is involved in there, probably it is,
[1576.80 → 1581.76] but there is a garbage collector that is in charge of, you know, freeing the variables that are not
[1581.76 → 1587.12] used anymore. And sometimes it takes priority and starts, you know, freeing stuff. And then once it's
[1587.12 → 1592.00] done running, it takes you back where you were in the program. And so this is something that is super
[1592.00 → 1596.48] jarring for us as reverse engineers, because we are looking at a very specific place in the program.
[1596.48 → 1601.76] We are frowning, looking very concentrated and focused, because we are looking super serious.
[1601.76 → 1606.80] And then we press F7, F7, we step into the next instruction. Suddenly we end up somewhere totally
[1606.80 → 1610.64] different, even though we didn't see any jump instruction. And suddenly it's like, oh, something
[1610.64 → 1615.52] is going on. What's happening with my program there? Because it's not supposed to just go somewhere else.
[1615.52 → 1620.24] Now, once I was able to figure out what was going on and understand that I just have to get out of
[1620.24 → 1624.96] this garbage collector function, and it will take me back exactly where I used to be, and things were
[1624.96 → 1631.28] fine. But initially, it was another one of Go's Idiosyncrasies that felt super alien to me, and
[1631.28 → 1636.32] that, like, I wasn't happy about at first. So that means it's not something, behaviour that you often see
[1636.32 → 1642.00] in other languages? Oh, no, it's something I had never seen before. I know that other languages, they do have
[1642.00 → 1645.92] their own garbage collectors. But when it comes to Java, we don't really have to look at the
[1645.92 → 1652.40] instructions, because Java is compiled to byte code. So we just read the code disassembled, or decompiled
[1652.40 → 1658.08] maybe, and get access to something that looks like the source code. It may be obfuscated, which means that
[1658.08 → 1663.52] it will be modified in a way that the variable names are not there anymore, or it has been specifically
[1663.52 → 1668.56] engineered to be harder to read. But in that case, or for .NET or for Java, we just never have to worry about
[1668.56 → 1673.92] CPU instructions, because they are not that relevant to the language. So Go was, for me,
[1673.92 → 1678.08] a big surprise on that level, because this was the first time I had to encounter debugging a program
[1678.08 → 1684.24] and being taken far away somewhere without even asking. And you know, it kind of happens on a
[1684.24 → 1689.04] regular basis, too. And then one more question about another behaviour that was peculiar that you
[1689.04 → 1694.24] pointed out, that at some point, when you had two following instructions, and they were using the same
[1694.24 → 1698.32] variable, you didn't see the return, but because it was right, the one after or before.
[1698.56 → 1703.92] I'm not sure exactly if I remember exactly the part that you referred to, but what I noticed is,
[1703.92 → 1709.04] yeah, this might be one of the other ways that the compiler in Go is being very smart, which is that
[1709.04 → 1714.08] if you have chained function calls, it turns out, I think that the way that arguments from one
[1714.08 → 1719.20] functions are returned on the stack happened to be the exact place where they would be considered
[1719.20 → 1725.12] as arguments for the next function. So you don't really see the data moving back and forth from the
[1725.12 → 1729.04] functions. It's just, you know, you have chained calls and the compiler knows that whatever was
[1729.04 → 1734.24] returned happens to be at the right place for the next one, etc. So one of these other things that we
[1734.24 → 1739.92] are used to seeing, like we see a function call, we look at the input, we look at what goes in and what
[1739.92 → 1744.48] goes out, basically. This helps us understand what is going on. And with Go, sometimes you just don't see
[1744.48 → 1749.36] that because it's hidden from you. Like the complexity tends to be, well, the complexity is
[1749.36 → 1755.28] still there, but you know, all these operations are masked by the way that the stack is constructed by
[1755.28 → 1759.84] the Go compiler, which again is a perfect thing for Go programmers, because it means that you don't
[1759.84 → 1764.64] have those memory movements that are taking place in the program that are actually not that useful.
[1764.64 → 1770.24] And every time you have a movement that involves the memory in a program, it takes a lot of time. I
[1770.24 → 1777.76] mean, not a lot compared to our human existence. But if you look at how a CPU works, you have the
[1777.76 → 1782.48] CPU that has some memory regions inside of it, which are called the registers. And then you have the RAM
[1782.48 → 1787.52] as well. You know, when you allocate memory in C program with a mallow or C allow, it goes into the RAM.
[1787.52 → 1793.20] Or when you move something into the stack, it's also a region of memory that is on the inside the RAM,
[1793.20 → 1797.44] you know, the RAM stick of the computer. Every time the CPU has to talk to the RAM sticks,
[1798.00 → 1802.40] it has to be an electrical signal that goes from the CPU through a bus to the motherboard. And the
[1802.40 → 1807.84] motherboard understands that it has to request the specific region of data to the RAM sticks. And
[1807.84 → 1812.96] you know, you have to have the response that goes back the same way, converted into electrical signals.
[1812.96 → 1818.72] So it's pretty fast, of course, when it comes to, it's probably in the ballpark of microseconds or
[1818.72 → 1826.16] milliseconds. But compared to just the CPU talking to itself, or moving stuff inside the physical
[1826.16 → 1829.84] area that is the CPU, or just not moving things at all, because they are already in the right place,
[1829.84 → 1834.48] then you get performance increases that I think are pretty significant, especially considering the
[1834.48 → 1838.00] amount of function calls that you have in the program. It's very interesting to hear about this
[1838.00 → 1841.12] from the perspective of somebody who's kind of poking this out from the outside.
[1841.12 → 1846.40] No, this makes me want to dive more into the reverse engineering just to learn more about the internals.
[1857.68 → 1863.52] Hey friends, this episode is brought to you by my friends and potentially your friends too at
[1863.52 → 1868.88] Fire hydrant. And I'm here with Robert Ross, founder and CEO of Fire hydrant. And Robert,
[1868.88 → 1874.56] there are several options out there for incident management, but what is it that makes Fire hydrant
[1874.56 → 1879.36] different? The reason that we think that Fire hydrant is on to something is because we're
[1879.36 → 1885.36] meeting companies really where they are. We face the same problems that every company in the industry
[1885.36 → 1891.28] that is building and releasing software is also facing. So where you want people to be able to sign
[1891.28 → 1897.60] up for Fire hydrant and immediately be able to kick off an incident using the best practices that we've
[1897.60 → 1902.40] built, and we've experienced and have gathered through the other amazing customers that use our tool.
[1902.40 → 1908.00] It really is a very quick time to value. And we want people to have a long jump from where they are
[1908.00 → 1910.88] to where they want to be in incident management.
[1910.88 → 1916.96] I love it. Thank you, Robert. Small teams up to 10 people can get started for free with all Fire hydrant
[1916.96 → 1921.28] features included. There's no credit card required to sign up. They are making it too easy to get
[1921.28 → 1927.04] started. So check them out at firehydrant.com. Again, firehydrant.com.
[1927.04 → 1956.00] So let's maybe move to a bit of a higher level now. Ghost community is kind of big on consistency.
[1956.00 → 1960.40] You know, we have like the linters that keep everything consistent. Go format keeps everything
[1960.40 → 1965.68] consistent. Does that actually help with reverse engineering at all? You think just the only
[1965.68 → 1971.12] one way to do thing and or at the level that you're doing reverse engineering if you think it doesn't
[1971.12 → 1976.32] matter? It's a good question. I have to say I don't know that much about the linter itself. I have
[1976.32 → 1981.76] written a bit of C code myself when I was trying to like look at assembly code and write Go at the same
[1981.76 → 1985.68] time that would generate the same thing. So this is my extent of the experience with the language and I
[1985.68 → 1991.36] really noticed something which is that the Go language is super strict. I have in the past used
[1991.36 → 1996.40] the expression, maybe I think to make you laugh, I was saying you know that in Go if you don't use
[1996.40 → 2001.44] the return values that the program is complaining. If you have unused variables then the program
[2001.44 → 2006.88] complains again, right? And I was saying that to me Go feels a bit like fascist Python. Like it doesn't
[2006.88 → 2011.04] let you do anything that you want except you know if it follows the rules very strictly.
[2011.04 → 2018.40] For us, it doesn't matter too much in the sense that those checks are enforced at the compiler level,
[2018.40 → 2022.80] right? It's something that if the code is not compliant then you will not get a binary at the
[2022.80 → 2028.96] end. So it does not add additional stuff inside the binary and also if there were some variable
[2028.96 → 2033.76] that is unused inside the program then as you reverse engineers we would not care, right? Because we
[2033.76 → 2038.72] would just consider that you know it's not used anymore, or probably the programmer doesn't need it for
[2038.72 → 2044.32] whatever reason, and we would just move on. So for us, it doesn't really change that much although
[2044.32 → 2049.68] knowing about those guarantees kind of allows us to make more informed guesses about what is going
[2049.68 → 2054.64] on in the program. Like for instance when I do see a function that returns multiple return values
[2054.64 → 2060.56] then I am not a Go developer but still I am always going to assume that the last value returned is going
[2060.56 → 2065.52] to be the object or the first one I don't recall, but I will have to check, but I know that since this is
[2065.52 → 2069.60] the normal way that people are supposed to write Go code and since I know that the compiler is going
[2069.60 → 2075.52] to force people to do it even if they don't want to that probably I can base my hypothesis on those
[2075.52 → 2081.44] conventions which is actually pretty helpful in that regard. So would you say that Go is a good language
[2081.44 → 2089.12] to pick up for hacker or for researcher in security? Well I'm not really in the business of helping attackers
[2089.12 → 2094.24] you know being more efficient at writing offensive tools but if I were to then I would guess that
[2094.24 → 2100.96] Go is probably a good language to pick up. Basically anything that is away from the traditional
[2100.96 → 2105.92] languages is going to be more annoying for us because we are less used to it. I think Rust is going to be
[2105.92 → 2110.00] a good choice as well. I haven't looked at Rust too much myself I have a co-worker that did and
[2110.00 → 2117.04] also released some videos and from what he's saying it's like C++ but harder which is a kind of high
[2117.04 → 2125.44] standard to beat. So yeah just Go and Rust would be my advice there, although it's not advice please don't.
[2125.44 → 2131.28] So if those are the kind of the new school ones right Go and Rust what are like historically what
[2131.28 → 2137.04] languages has everyone used on the hacking side and on the research side? Well historically everything
[2137.04 → 2142.16] has been used you know Murphy's law which says that if there is a way to misuse something that is going
[2142.16 → 2148.64] to be misused right, and programming languages have proven time and again that law. The thing is we are
[2149.20 → 2153.76] recipients of whatever the hackers are doing right. We do not get to choose what we are going to work
[2153.76 → 2157.92] on like hackers are going to write their tools, and they're going to choose whatever language
[2157.92 → 2163.20] is familiar for them or whatever language feels comfortable or whatever and this is why we end up
[2163.20 → 2169.04] sometimes facing the most ridiculous stuff like malware written in auto IT. I don't know if you know about
[2169.04 → 2176.48] this it's like a's some weird scripting language that is used for UI testing and basically allows
[2176.48 → 2182.48] you to simulate keystrokes and mouse clicks. Well it turns out people write malware with this as well.
[2182.48 → 2187.92] Anything that has ever been available as a programming language has been one way or the other eventually
[2187.92 → 2194.32] been used for malware. So the thing is this is our bane as reverse engineers which is that we do receive
[2194.32 → 2198.96] malware and whatever it is we have to work on it because at the end of the day our job is to
[2198.96 → 2204.16] figure out what was going on in that specific incident. And so whether it's C or C++ or it's
[2204.16 → 2210.64] Go or Delphi or Pascal or whatever we just have Erlang maybe no Erlang I'm pretty sure there's an Erlang
[2210.64 → 2217.20] malware whatever we receive we have to work on, and so we cannot really afford to be picky about what
[2217.20 → 2223.36] languages we get interested in. We just have to be able to adapt to whatever comes because everything
[2223.36 → 2228.56] will come eventually. So you just mentioned right there like you get your research is on whatever like
[2228.56 → 2233.36] hackers leave behind let that be malware or whatever what other things do people leave behind is it just
[2233.36 → 2240.64] the actual binaries or like are you digging into logs and other things? Yeah, so in a typical incident
[2240.64 → 2246.96] scenario then you would have people that go into what we call forensics mode they will collect all the
[2246.96 → 2252.24] logs they will collect all the hard drives and try to figure out exactly what happened inside the network
[2252.24 → 2257.76] they will collect not just machine logs, but you know DNS logs they will collect whatever event was
[2257.76 → 2263.44] generated by the Windows machines they will collect you know whatever was saved by the HTTP proxy and so
[2263.44 → 2268.00] on all the net flow if it's available usually it's not usually not that much information is actually
[2268.00 → 2271.52] available in case of an incident, but you know that's someone else's problem I'm not an incident
[2271.52 → 2279.52] responder and I have enough stuff to worry about but what I focus on is the actual malware we do have
[2279.52 → 2285.68] information through the antivirus from Kaspersky that gives us information about the execution context so we can
[2285.68 → 2291.12] see that okay this process launched this process etc so we have this type of information but in a bigger
[2291.12 → 2296.56] incident context then you would get a much clearer picture about everything that went on the in the
[2296.56 → 2301.92] victim's network and this whole trove of information would allow you to reconstruct the whole
[2301.92 → 2306.00] timeline of the incident so you would see that you know at this time you had some suspicious
[2306.00 → 2311.36] request on you know some web front end, and then you would see that there is a file created at a later date on the
[2311.36 → 2316.80] same web server, and then you would maybe see some weird suspicious request to the active directory server
[2316.80 → 2322.80] with some golden ticket with a mimic at or something well those kinds of lateral movement methods etc and at the end of the
[2322.80 → 2330.80] day somewhere some attacker would have to drop some binaries to help them either persist on the victim machine or get
[2330.80 → 2337.36] further into the network or deeper because they will try to do whatever they can without deploying anything some very careful
[2337.36 → 2343.52] attackers will not deploy anything on disk, and they will just deploy whatever program that they need inside
[2343.52 → 2348.08] the memory which is very stealthy, but also the machine happens to reboot then you know everything
[2348.08 → 2352.80] that was in the memory just goes away and so if you have no way of coming back onto the victim machine then
[2352.80 → 2357.28] you know all the access that you have deployed is lost some very stealthy attackers will decide that they
[2357.28 → 2365.12] would rather lose access and leave forensic traces on hard drive most of them like 90 99 of them will feel like they would
[2365.12 → 2371.60] rather leave some kind of trace knowing that most people don't look anyway and then leave stuff for
[2371.60 → 2377.60] us to analyze later if we figure out that there was an incident, and you know someone goes there collects
[2377.60 → 2382.24] everything and just sends the binaries back to us you said the incident response teams are the ones that
[2382.24 → 2388.16] collect all that data and all of that yeah exactly so we do have such teams at Kaspersky but most
[2388.16 → 2393.28] cybersecurity companies will have either their internal instance responders or swoop in you know a
[2393.28 → 2399.76] contractor that they know of and that can be called at any hour of the day or the night and that will come, and you know
[2399.76 → 2406.80] just exactly swoop in with the big guns if something weird took place now it doesn't mean that we do not work in
[2406.80 → 2411.76] direct interaction with those teams it means that you know this is their job, and then you know we get we are more back
[2411.76 → 2419.28] office guys where you know we get escalated some stuff, and then we look into it but most of the intelligence that we create
[2419.28 → 2424.32] doesn't actually come from incident response cases I think it would be a good idea if we were able to
[2424.96 → 2430.40] gain more information from that source as well I think it's a very valuable one, but we work mostly
[2430.40 → 2435.60] on the telemetry collected by our antivirus you know all the samples that are suspicious or that are
[2435.60 → 2441.68] uploaded to the cloud for analysis, and then we can also swoop in, but you know very much more quietly
[2441.68 → 2446.80] and look at all this data and see okay this looks interesting because you know we've never seen this before
[2446.80 → 2451.20] or it looks like some malware that we saw 10 years ago, and we haven't seen since, and you have some
[2451.20 → 2456.40] modifications, and then we are interested in what happened since then right, but it's not really our
[2456.40 → 2461.76] work tends to be a bit disconnected from the actual incidents and really more focused on looking at the
[2462.40 → 2467.68] big data lake that we have and try to understand what is relevant inside of it that's cool, thanks for
[2467.68 → 2475.36] that that insight from the other side of this equation what are some tips you can give for writing a secure
[2475.36 → 2481.76] software for people who do go or in general if it's not specific to go it's also useful yeah I think
[2481.76 → 2487.44] one of the main appeals of go is that you don't really need to think about security as much as with
[2487.44 → 2493.44] other languages go is a memory safe language unless I'm mistaken and the compiler is never going to let
[2493.44 → 2498.56] you do stupid stuff like create an array that is too small, and then you know write stuff that goes out
[2498.56 → 2505.04] of it like it's not just not possible so it eliminates a lot of bug classes which we call memory
[2505.04 → 2509.44] corruptions it's just not going to happen you cannot do this to yourself and go, and it means
[2509.44 → 2516.16] that all the old school buffer overflows that plagued all the c and c++ programs for dozens of years by
[2516.16 → 2522.48] now just are not going to ever happen in the go language it doesn't mean that the program is going to be
[2522.48 → 2528.48] like perfectly safe from any security issues, but the issues are not going to be related to oh I made a
[2528.48 → 2533.36] programming mistake and uh there is a bug in my program it's going to be exploited it's going to be
[2533.36 → 2539.92] more related to design issues like the memory safe language does not help you implement a secure
[2539.92 → 2546.08] authentication scheme for instance it doesn't help you write a well-thought-out network protocol I saw
[2546.08 → 2550.96] that go really helps you with cryptography I noticed that it's very difficult to choose algorithms that are
[2550.96 → 2556.96] not safe like by default you can only I don't think you can choose the algorithms and go by like I know you
[2556.96 → 2562.88] can do AES for instance but like the cypher mode or the this kind of stuff tends to be unless I'm
[2562.88 → 2567.04] mistaken you know selected by default for you and the defaults are good so you're not going to be
[2567.04 → 2574.32] making those mistakes but oh yeah the iv something I was working on some code in go that was uh relying
[2574.32 → 2579.52] on AES I was looking at trying to figure out exactly how the iv was generated and so on I was looking
[2579.52 → 2585.20] saying that nowhere in the developer code and doing some research I noticed that it was actually go that
[2585.20 → 2591.76] would by itself generate an iv for the encryption this initialization vector, and then it would append
[2591.76 → 2597.92] it to the uh somewhere in the final encrypted buffer and so usually in other languages this is something you
[2597.92 → 2603.60] would have to do on your own and this is a like a big avenue for making mistakes like if you choose a
[2603.60 → 2608.00] stupid iv like just zeros or if you do not select one at all then you're going to have encryption
[2608.00 → 2613.28] problems go would not let you do this so it's very obvious to me that go was created with
[2613.28 → 2618.48] security in mind not for the developers but by the go creators like they don't want you to shoot
[2618.48 → 2621.84] yourself in the foot, and you know they're going to make sure that there's no way for you to do it
[2621.84 → 2627.60] unless you really want to even though you do have all those kinds of protections cryptography
[2627.60 → 2632.48] like can be misused like you know if you choose a bad key then you know nobody's going to save you from
[2632.48 → 2637.92] that if your protocol doesn't work then again you cannot be protected from it either
[2638.64 → 2645.04] I think it allows people to focus on design flaws instead of programming flaws and this is already
[2645.04 → 2651.04] like a huge burden off the shoulders of developers that is a very interesting insight that's interesting
[2651.04 → 2656.24] I see a lot of complaints outside of kind of the go community just you know like hacker news about
[2656.24 → 2662.56] goes choosing your defaults for like TLS or not letting you do certain things, but that's
[2662.56 → 2666.96] one I'm firmly on board with if I don't want to if I don't need to think about it, I don't want to
[2667.60 → 2672.72] and I don't want to make the mistake would you be able to confidently select your defaults for TLS i
[2672.72 → 2677.20] mean I don't think I would feel comfortable doing this like you have to be like very well versed in
[2677.20 → 2681.84] cryptography to be able to make those kinds of decisions so it's very good that go is not making
[2681.84 → 2688.56] you do this I think in my opinion
[2688.56 → 2700.56] this episode is brought to you by honeycomb find your most perplexing application issues
[2700.56 → 2706.96] honeycomb is a fast analysis tool that reveals the truth about every aspect of your application
[2706.96 → 2712.16] in production find out how users experience your code in complex and unpredictable environments
[2712.16 → 2717.68] find patterns and outliers across billions of rows of data and definitively solve your problems
[2717.68 → 2722.08] and we use honeycomb here at change that's why we welcome the opportunity to add them as one of our
[2722.08 → 2727.60] infrastructure partners in particular we use honeycomb to track down CDN issues recently which we talked
[2727.60 → 2732.72] about at length on the Kaiden edition of the ship it podcast so check that out here's the thing
[2732.72 → 2737.28] teams who don't use honeycomb are forced to find the needle in the haystack they scroll through
[2737.28 → 2741.92] endless dashboards playing whack-a-mole they deal with alert floods trying to guess which
[2741.92 → 2747.04] one matters, and they go from tool to tool playing sleuth trying to figure out how all the
[2747.04 → 2751.92] puzzle pieces fit together it's this context switching and tool sprawl that are slowly killing
[2751.92 → 2758.24] teams effectiveness and ultimately hindering their business with honeycomb you get a fast unified and
[2758.24 → 2764.96] clear understanding of the one thing driving your business production with honeycomb you guess less
[2764.96 → 2770.24] and you know more join the swarm and try honeycomb free today at honeycomb.io
[2770.24 → 2775.36] slash changelog again honeycomb.io slash changelog
[2775.36 → 2802.56] another interesting about your interest in go you kind of mentioned that you started using go because
[2802.56 → 2808.72] malware was thrown at your kind of yeah exactly so I wouldn't say that I've started using go I would
[2808.72 → 2814.16] say that I was forced to learn go not that i I'm unhappy about it, I'm not saying it's a bad thing
[2814.16 → 2820.08] what I'm saying is that I'm not really writing go code myself what I did was I had assembly that was
[2820.08 → 2830.56] generated by the go compiler and I was trying to make heads or tails from it so what I did was I looked at the assembly I was like okay this might be the go code that generated this assembly and then I opened my go ID
[2830.56 → 2838.96] I opened my go IDE and I compiled my code and checked if it was the same on both ends also when I start to
[2838.96 → 2843.92] learn about a language when I want to reverse engineer it I think it's super useful to write some simple
[2843.92 → 2848.48] programs and just compile it and see how it looks in the assembly level you know just create a simple
[2848.48 → 2854.48] stupid c function not c function but a sum function that you know adds to integers, or you know something that
[2854.48 → 2859.92] will allow you to see what types of function calls the program is using what kind of constructs the
[2859.92 → 2864.48] language is generating the things that I had to face there was again the go compiler being way too
[2864.48 → 2871.04] smart for my uses, and it tends to inline all the function calls that are too simple what I mean
[2871.04 → 2875.76] by this is if you have a simple function that does almost nothing, and you call that function than the
[2875.76 → 2880.64] go compiler will be like oh this is not worth a function call what I will do is I will take the code of all
[2880.64 → 2885.04] this function and put it inside the calling function, and you know when you try to look at what
[2885.04 → 2889.60] a function call looks like in assembly then this is not helping you, but the good thing is I was able
[2889.60 → 2894.80] to find the good flags and uh for the compiler to disable opt all optimizations and things kind of
[2894.80 → 2900.32] worked out for me, you mentioned that IDA and which is the main tool you're using and the other tool
[2900.32 → 2907.44] are not really supporting go so if anybody wants to try reverse engineer to get into that but also want to
[2907.44 → 2913.76] do that with go what would you recommend how to do that so if you're going to reverse engineer go
[2913.76 → 2918.56] programs I still think that you don't have much choice there so you're still going to be you're
[2918.56 → 2923.76] still going to have to use either, either pro or fire I want to switch to fire eventually but i
[2923.76 → 2929.76] haven't done so at the moment so I cannot speak too much about its capabilities I'm told that it's being
[2929.76 → 2937.12] improved at a very rapid pace so it's probably a good choice but when it comes to IDA it got better
[2937.12 → 2942.64] right I think that's a few months back maybe a year now you had my good friend uh Juan Andres
[2942.64 → 2947.28] Guerrero sad from central one on the podcast and probably told you about the various plugins that
[2947.28 → 2953.68] he wrote to help people reverse engineer go programs with IDA I also contributed to his repository with
[2953.68 → 2960.96] some script myself that I find useful but overall even though IDA might not be perfect for the job
[2960.96 → 2966.48] it's still one of the two only tools that are available for the job so you still have to
[2966.48 → 2972.96] you know work through it no matter what the thing is I find myself thinking that even though starting
[2972.96 → 2979.28] with reverse engineering go is kind of difficult it turns out that I find myself liking reverse engineering
[2979.28 → 2984.40] go programs way more than c++ programs that tend to be extremely complicated with you know virtual
[2984.40 → 2989.52] function tables and the very complex structures that represent classes and so on because when it comes to the
[2989.52 → 2994.80] go language turns out that it kind of feels like a scripting language in the sense that everything
[2995.44 → 3000.48] ends up being a call to an API function or a call to some function that comes from the go standard
[3000.48 → 3006.16] library and so if you are able to take a debugger, and you know look at all the arguments after you know
[3006.16 → 3012.32] how to do that but if you look at all the arguments of the go functions that are documented by the way and
[3012.32 → 3018.24] look at the return values then actually the meaning of the program tends to manifest itself even though
[3018.24 → 3022.72] you don't really understand all the instructions that are in the middle, and you cannot track you
[3022.72 → 3027.44] know all the stuff going uh here and there so overall like my advice for people that would like
[3027.44 → 3031.68] to get started with go reverse engineering is okay it's going to be very different from what you are
[3031.68 → 3036.72] used to but at the end of the day I think you're going to end up liking it more than you would think
[3037.52 → 3043.04] because it's going to be way easier than it looks how about those listeners that haven't done any
[3043.04 → 3046.72] reverse engineering that want to get started do you have any good resources out there I know that you
[3046.72 → 3050.64] personally have made some videos you want to talk about that a little bit and anything else that
[3050.64 → 3056.16] would be helpful so yeah the videos that I put out are just related to the goal language if you're
[3056.16 → 3060.72] going to get into reverse engineering I would not advise you to start with go not because it's going
[3060.72 → 3067.12] to be harder or anything but because probably the basics of reverse engineering are going to be related to
[3067.12 → 3073.44] traditional c code or traditional assembly code generated by c and so this is going to be like your
[3073.44 → 3078.24] base knowledge of reverse engineering and then once you are comfortable understanding what
[3078.24 → 3085.28] is going on with the c language, and you know all the assembly that you see most places then you can
[3085.28 → 3092.72] move on to other languages and see how they differ from others or etc but I think c is always going to
[3092.72 → 3097.84] be used as a reference for other languages in the sense that when you look at assembly first you try to
[3097.84 → 3102.64] understand it like you would understand c and then if it's different like you adapt from that but if your
[3102.64 → 3107.92] baseline is going to be the go language if they like the one thing you know is go, and then you try
[3107.92 → 3113.44] to recognize whatever you learned with go with another language then you're going to be into trouble
[3113.44 → 3118.48] because whatever you're going to see next is not going to look like anything you saw in go so we do
[3118.48 → 3122.80] have a few courses at Kaspersky but I mean people can check them out if they want there are a few
[3122.80 → 3130.48] interesting uh online courses as well it's something for free which is a beginners’re it's a website it used to be
[3130.48 → 3135.28] free maybe now it's behind a paywall I'm not sure, but it used to be a big, big reverse engineering course
[3135.28 → 3140.72] written by some guy, and it was uh it was amazing you have a book which is called practical malware
[3140.72 → 3147.44] analysis it's a bit old now but I think it's still very much up to date it's from no stock press I think
[3147.44 → 3152.24] for beginners it's going to be a good way to get into the field because it explains everything that is
[3152.24 → 3157.76] going on it provides links to the various tools that you might need etc so a good resource there and
[3157.76 → 3163.92] finally if you want to approach this from the fun angle I can actually recommend perfect steam
[3163.92 → 3169.92] games that allow you to like to get a feel for reverse engineering so one of them is called Turing complete
[3170.48 → 3175.52] and this one is uh like the pitch of this game is you're going to build your own computer and so you
[3175.52 → 3181.84] start with they give you logic gates like a XOR gate or the electric cables basically and based on
[3181.84 → 3187.68] this you have to build a CPU component by component, and then you move on with increasing levels of
[3187.68 → 3194.96] abstraction so it really it's really super helpful to understand how a program works or how a computer
[3194.96 → 3201.20] works it really it allows you to get this uh eye level bird eye view of how a CPU is constructed and
[3201.20 → 3206.40] how it's supposed to operate and knowing how CPUs work is then very, very helpful when you are doing
[3206.40 → 3212.56] reverse engineering, and then you have other games which are from a developer which is called atonics
[3212.56 → 3218.64] and these are like weird puzzle games that are really related to computing problems one of them
[3218.64 → 3224.24] is called a this 100 you have another one called hexagons, and they are dubbed the assembly games you
[3224.24 → 3229.76] didn't know you wanted, and it's actually a very apt description because these games have their own
[3229.76 → 3233.84] weird and limited assembly language, and you have to solve puzzles with them like you have to program
[3233.84 → 3238.40] some sort of small machine in order to make it do stuff, and you have to do this with assembly and
[3238.40 → 3244.88] it forces you to use the language which uh like has the very perfect desired side effect of making
[3244.88 → 3250.56] you learn how CPUs work when we are making you more comfortable handling those uh weird instructions
[3250.56 → 3256.00] by yourself, so these would be my recommendations for people that want to get into it yeah I'd not
[3256.00 → 3261.44] thought about games that sounds I'm going to check those out later actually yeah actually if you are
[3261.44 → 3266.48] working from a university or if you are a teacher somewhere atonics I think the company maybe
[3266.48 → 3271.04] closed doors not too long ago I think they are done making games, or they move on to something
[3271.04 → 3277.36] else, but they used to have a very extensive education program where if you are a university, and you are
[3277.36 → 3282.16] doing an I don't know some computer science degree or something like this you could just send them an
[3282.16 → 3287.04] email, and they would give you access to all their games you know for free basically, and you could use
[3287.04 → 3292.08] them to teach or as teaching aids and I think it's uh like amazing of them and also the games are
[3292.08 → 3297.44] really really really fun I think so they are fun if you like assembly which I think is a pretty biased
[3297.44 → 3302.48] statement on my end but I guess still do recommend them a lot of the things you said they're like a
[3302.96 → 3309.84] cheat sheet for reverse engineering and lots of useful information and I have so many more
[3309.84 → 3314.80] questions about specific things about go and reverse engineering we might have to do another episode
[3314.80 → 3320.72] about this because we are running out of time sure well I can come back whenever you like we will
[3320.72 → 3325.20] prepare our questions we'll ask you about things like generics I will have to prepare those questions
[3325.20 → 3341.12] as well I guess but no problem now it's time for an unpopular opinion
[3349.04 → 3354.32] so Ivan what is your unpopular opinion for us oh my god I totally forgot about that oh it's okay
[3355.52 → 3360.72] the good thing is I do have many unpopular opinions so I'm going to like to give you think on the top of
[3360.72 → 3365.44] my head, and you can tell me what you want to know more about for instance I think that cyberspace is
[3365.44 → 3372.56] never going to be regulated I think that NFTs are a scam I think that there is no political will to
[3372.56 → 3378.24] limit the sale of cyber offence tools that kind of stuff yeah that's I do have a lot of unpopular
[3378.24 → 3381.76] political opinions as well but I don't think I want to inflict that onto you, you've been very nice to me
[3381.76 → 3390.08] what do you think about the European rule about the USB until standardizing uses oh I'm very
[3390.08 → 3398.08] happy about it, I know it's uh some pressure put on some device constructors but I've been carrying
[3398.08 → 3403.28] lots of different chargers for years and I'm super annoyed about this, and you know knowing that we are
[3403.28 → 3409.12] going to switch to like a single USB for every single device makes me extremely, extremely happy
[3409.68 → 3414.08] another unpopular opinion I have which you can add to the list is that I'm not really a big fan of
[3414.08 → 3419.36] apple like not at all I don't like their ecosystem and I'm not going to get into this but one of the
[3419.36 → 3423.20] things I don't like is that people have to pay 40 bucks for like new chargers, and they change
[3423.20 → 3427.68] chargers every time they release a new product and I'm very happy that this is going to cut off this
[3427.68 → 3431.60] revenue stream for them because I think this should have never existed in the first place what do you
[3431.60 → 3435.76] think about all the like the walled systems you know like the Google Play Store and the Apple Store
[3435.76 → 3440.32] and the Amazon store like from a securities' perspective they say it's safer to do you agree
[3440.32 → 3446.32] with that do you yeah this is a very good question I do have very ambiguous feelings about them, I do
[3446.32 → 3451.52] believe that for the security on the security perspective it's kind of a good thing in the sense
[3451.52 → 3456.48] that yeah it's another one of those safeguards that prevent people from doing stupid stuff with their
[3456.48 → 3463.60] devices, and you know having to go to some friends places or more specifically friends of my mom's
[3463.60 → 3468.24] places to debug computers, and you know uninstall malware and fix the printers than I'm very happy
[3468.24 → 3474.16] when you there are protections that prevent them from doing that kind of stuff then again they are not a
[3474.16 → 3480.48] perfect solution either I think the Apple Store in terms of security is uh like pretty good the Google
[3480.48 → 3485.92] store the play store has a bad track record when it comes to hosting malware I'm not saying that they're
[3485.92 → 3490.48] doing a bad job I think it's a very, very difficult job, but the fact of the matter is there are a
[3490.48 → 3497.60] number of apps on the Google Play Store that turned out to maybe not be total malware but some of them
[3497.60 → 3504.08] are but a lot of them are just you know there to collect personal data or that kind of stuff so I think
[3504.08 → 3510.64] a better way of securing those devices is not to control the app stores I think created protections on
[3510.64 → 3516.96] the device level is probably where I would um work so when you look at both iOS and android they are
[3516.96 → 3521.60] doing I think a very good job of or have been doing a very good job at least in the past years of making
[3521.60 → 3526.56] sure that apps will not be able to access anything just because the user clicked okay on a way back
[3526.56 → 3532.24] when they installed the app so I think making sure that all those personal information cannot be
[3532.24 → 3539.84] pulled so easily is going to be like a much better way than you know trying to police all the stores and
[3539.84 → 3544.24] look at all those thousands of apps that are updated there every day which I do not think
[3544.24 → 3551.84] that you can realistically ensure that they are always going to be safe but overall the other issue
[3551.84 → 3556.40] with world gardens which is okay maybe they do provide something with security but also I feel
[3556.40 → 3562.32] like they take away some agency from me as a user right I really like to own the devices that I use
[3562.88 → 3567.52] and having some restrictions that tell me oh you cannot install this app because google says you can't
[3567.52 → 3572.40] or you can uninstall this app also because google says you can't is something that tends to make me
[3572.40 → 3579.20] extremely, extremely angry so you mentioned a lot of unpopular opinions yes the way the twitter works
[3579.20 → 3586.32] for our podcast is that we take an unpopular opinion, and then we make a vote, so there's a poll do
[3586.32 → 3590.96] people agree with you or not and then there's a hall of fame for unpopular opinions and for popular
[3590.96 → 3598.00] unpopular opinions so you listed several which one would you like us to vote on so if I wanted to win
[3598.00 → 3602.48] the contest I guess I would go with the NFT one because I know that this is something very divisive
[3602.48 → 3607.76] and I think that a lot of the audience that you are reaching is going to be probably I'm not going
[3607.76 → 3611.92] to say that they are necessarily going to be on my side but I think they're going to be on the side
[3611.92 → 3616.72] but I think a much more interesting question that I would be actually interested in having the uh the
[3616.72 → 3621.52] community's opinion about is the one about regulation like I do believe that cyberspace is
[3621.52 → 3625.92] never going to be regulated, and maybe I need to say a bit more about this one right so that people
[3625.92 → 3631.12] can figure out for themselves my opinion on this is that you know we have a number of high-level
[3631.12 → 3636.88] discussions taking place at the UN about you know acceptable norms for behaviour in the cyberspace etc and
[3636.88 → 3641.68] you have all those discussions between states where they talk with each other, and they are like okay
[3641.68 → 3646.40] what type of offensive operations are legitimate like for instance espionage is okay but destructive
[3646.40 → 3651.28] attacks are not okay I mean I'm not saying this is right I'm just saying this is probably the kind
[3651.28 → 3655.68] of discussions that they are having, and you know we may have differing opinions on what types of
[3655.68 → 3660.40] attacks are okay and what types are not or even if attacks are okay at all it doesn't matter the thing
[3660.40 → 3667.68] is I do believe that I don't think that we will ever reach an agreement there because well states
[3667.68 → 3675.52] do not have an incentive to regulate cyber offence I think that they have an interest in having a way or
[3675.52 → 3679.92] having some kind of framework that allows them to still conduct operations because when they
[3679.92 → 3684.96] conduct operations they know what they are winning right they have intelligent services that gather
[3684.96 → 3688.88] data they collect it through cyber means they take it back, and so they know that they are able to
[3688.88 → 3693.68] achieve certain results because they have obtained specific information, and they can quantify that
[3694.32 → 3701.28] on the other end when you look at the costs of cyber offence which means all your companies in
[3701.28 → 3705.20] your country that have been breached because there are no, no such norms it's something that's super
[3705.20 → 3710.24] hard to quantify you can never know that you know you lost some contract overseas to sell planes or to
[3710.88 → 3715.76] something else because the cyber means because it's very likely that nobody knows that the breach even
[3715.76 → 3722.08] happened in the first place, so the thing is you look at the balance of risk reward for the decision
[3722.08 → 3727.68] makers, and they see this is what we win with cyber offence which is a lot and what they lose is
[3727.68 → 3732.48] actually it's painless, and also they have no idea what it is and so overall I think that all those
[3732.48 → 3737.44] discussions that are taking place that are saying okay we need to make a safer internet blah blah blah
[3737.44 → 3742.72] are actually possibly being conducted in bad faith because there is no political will to actually stop
[3742.72 → 3747.44] doing this kind of stuff this would be my unpopular opinion especially in the diplomatic circles
[3747.44 → 3753.52] all right you will be tagged, and we will be following the results okay no I'm interested to see the results
[3753.52 → 3758.64] on this one yeah it's an interesting way to think about it yeah I want to know as well cool thank
[3758.64 → 3762.56] you very much for sharing your knowledge your thoughts and your opinions with us this was
[3762.56 → 3768.40] really fascinating we will be very happy to have you again thanks a lot Ivan well thank you very much
[3768.40 → 3773.36] for having me and uh yeah feel free to like to call me up anytime I'll be happy to be back thanks
[3773.36 → 3781.52] IAN for joining it was fun co-hosting together yeah, thanks you guys this was great bye everyone
[3783.76 → 3789.92] if you enjoyed listening at the intersection of go and information security stay tuned for part three
[3789.92 → 3795.36] it's currently scheduled to record live on November 29th and of course go back and listen to part one
[3795.36 → 3802.00] while you're at it that was episode number 205 here's a sampler the stakes have been ratcheting up
[3802.00 → 3806.88] it's really easy to kind of look at it that way, and we don't want to make it like too dark or too
[3806.88 → 3813.84] heady but now this is the playground of also a lot of nation states and a lot of criminals, and you know
[3813.84 → 3819.12] if you're in this in the US it's kind of like the ransomware epidemic is sort of unavoidable right like
[3819.12 → 3824.08] you have to talk about it every day and that's where things get less pretty right like if you're at
[3824.08 → 3829.76] a hospital that can't help folks because all their you know tragically outdated Windows XP systems are
[3829.76 → 3834.80] in a flat network and all of them got popped at the same time that's where you go well yeah that code
[3834.80 → 3841.36] was fun I love the idea of just having these you know kind of hacking superpowers, but there's a side
[3841.36 → 3846.40] to it that isn't quite so cute and I think we're kind of walking that line all the time right where you
[3846.40 → 3851.92] go oh this is fascinating, and you just get wrapped up in the functionality and what someone has been able
[3851.92 → 3858.16] to accomplish, and it's easy to forget like oh well there's this is actually a part of a much
[3858.16 → 3865.68] heavier game listen in at gotime.fm slash 205 or search hacking with go in your podcast app of
[3865.68 → 3872.16] choice it should pop right up thanks once again to our partners at fast and fly.io they help make
[3872.16 → 3878.00] go time possible into the mysterious brake master cylinder go times beats are dope because BMC makes
[3878.00 → 3884.96] dope beats it's as simple as that next time on go time angelica Natalie and Chris welcome tech lawyer
[3884.96 → 3891.28] lewis via to the show to answer the age-old question who owns our code stay tuned I think
[3891.28 → 3894.64] you're going to dig it we'll have that episode ready for you next week
[3906.64 → 3906.72] you
