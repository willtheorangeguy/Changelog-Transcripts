[0.00 → 16.24] welcome back everyone this is the change log and I'm your host Adam stikowiak this is episode 152
[16.24 → 21.58] and on today's show jarred and I are talking to two awesome developers behind typescript at
[21.58 → 27.88] Microsoft Jonathan turner and Andes Habsburg Jonathan is the program manager and Andes is
[27.88 → 34.50] the language architect so we go deep sit back and listen as jarred and I get schooled on this
[34.50 → 42.04] typed based superset of JavaScript we have three awesome sponsors for the show today code ship
[42.04 → 48.06] top towel and digital ocean we'll tell you a bit more about top towel and digital ocean later in
[48.06 → 54.28] the show, but our friends at code ship have this new feature wild card deployments now you can get
[54.28 → 60.16] more flexible deployment workflows with wild card deployment pipelines that trigger if a branch
[60.16 → 65.90] starts with a certain prefix you can do this it's super easy use one deployment configuration for
[65.90 → 72.56] multiple branches and automatically deploy your feature your release your QA etc branches to the
[72.56 → 77.62] corresponding environments it's the perfect feature for allowing your team to be super flexible
[77.62 → 83.38] and how you want to work and how your workflows should work for you as always code ship is free
[83.38 → 88.76] to get started by trying out their free plan which includes 100 builds a month and five
[88.76 → 95.66] private projects use the offer code the changelog podcast to get 20 off any plan you choose for
[95.66 → 101.42] three months head to code ship.com slash the changelog to get started and now on to the show
[101.42 → 111.46] all right everyone we're back we got Jonathan turn on the line Andes Habsburg he uh he's done some
[111.46 → 116.08] cool stuff Andes we'll let you tell a bit in the in here in a second or two, but we also have
[116.08 → 121.70] jarred on the call today talking about typescript jarred are you excited I'm excited man second time we
[121.70 → 128.16] have Microsoft people on the changelog recently so it's blowing my mind it's a new Microsoft, and we'll find
[128.16 → 133.60] more I'm sure Jonathan let's start with you um introduce yourself if you don't mind talk about
[133.60 → 137.50] uh you know who you are at Microsoft what you do and then angels will follow up with you after
[137.50 → 143.78] after Jonathan sure thing, so my name is Jonathan turner I'm the program manager at Microsoft on the
[143.78 → 150.66] typescript team, so program manager is kind of like I don't know the glorious cat herder so i kind of
[150.66 → 157.86] I know right uh I run the design meetings I do a lot of connections out to clients and kind of
[157.86 → 163.66] try to gather all the requirements to make sure we're on the right track and just what about you
[163.66 → 173.00] uh I'm Andes Habsburg and I'm an um technical fellow at Microsoft um and uh these days I'm working
[173.00 → 180.06] on typescript but I've spent many years over a decade working on botnet and c sharp and before that I was
[180.06 → 188.44] at Boland for about 13 years and worked on Turbo Pascal and Delphi and lots of other things yeah
[188.44 → 193.32] jarred in our pre-call you had some pretty unique uh asks for Andrews anything in particular on
[193.32 → 198.06] Delphi as we in the pre-call we kind of determined it's not Delphi it depends on which side of the
[198.06 → 203.34] the Atlantic you live on if it's Delphi or Delphi so what else I'm just saying I'm apparently a Brit
[203.34 → 209.96] at heart or something because Delphi just sounds right to me always has so uh I've been corrected
[209.96 → 215.24] I stand corrected I'm going to try to say Delphi um because Andes if you say it's Delphi I'll go
[215.24 → 221.86] with Delphi although to the guy who invented the GIF I'm not going to relent on that one I'm not gonna
[221.86 → 226.78] call it I'm not going to call it a GIF sorry fella but for you Andes I'll definitely go with Delphi
[226.78 → 234.00] yeah I was wondering um with your history um and on the Wikipedia page for typescript uh you're kind
[234.00 → 238.24] of named as I don't know the inventor of typescript or at least the person who kind of started inside
[238.24 → 245.48] of Microsoft we're curious how that came about um if it was your idea if somebody approached you
[245.48 → 250.52] if there was a core team at the beginning maybe just give us a backstory of your role at Microsoft
[250.52 → 256.50] and how typescript has been involved in it yeah no I mean typescript is obviously a team
[256.50 → 262.72] effort and I would say i I lead the team as sort of the architect for the language and i I also work
[262.72 → 271.52] in actively on the compiler um the project probably trying to think well we went public in October
[271.52 → 276.88] of 2012 I remember that I was trying to think back the other day when we started it was probably well
[276.88 → 285.08] it must have been sometime in 2011 probably late 2011 um and we sort of had this on and off
[285.08 → 291.74] conversation about what are we going to do going forward for JavaScript um we saw increasingly
[291.74 → 297.16] that people were writing larger and larger applications in-house as well as externally
[297.16 → 305.20] um in JavaScript just because you know that's sort of like the only cross-platform game left in town
[305.20 → 312.42] right and um people were finding uh certainly in-house that it's hard to maintain these large apps
[312.42 → 318.22] uh as they get beyond a certain size it just becomes incredibly hard to keep it all in your head
[318.22 → 325.86] and when you want to do uh refactorings or anything of a larger nature you know it's its
[325.86 → 331.22] it's like playing with landmines to refactor a JavaScript code base because you can never really
[331.22 → 337.18] be certain that you have tests to cover everything and if you pick the name for a property like say text
[337.18 → 342.26] or whatever then there's millions of things called text and how do you know that you're getting the
[342.26 → 348.84] right ones and and and people basically were trying to solve this problem in a variety of different ways
[348.84 → 355.02] we saw like at Google for example they have get or quit as they called it early on which was the idea
[355.02 → 360.18] there is you author in java and then you cross-compile it to JavaScript and that allows you to get the
[360.18 → 366.14] grown-up tooling of java and the java ecosystem, but it allows you to run it in the browser
[366.14 → 372.80] and we actually had a project in-house that was similar in nature called script sharp that office
[372.80 → 379.34] uh has used for a number of their large projects um, and we were sort of toying with the
[379.34 → 384.58] idea boy should we productize that maybe or but then the more we thought about it the more we felt
[384.58 → 390.74] that hey if is is you really want to do something in a community like JavaScript you really
[390.74 → 396.58] should aim to be best of breed you know you really should aim to solve the problems on the
[396.58 → 403.62] on the community's terms not on your terms so to speak and so you know we try to put our
[403.62 → 408.44] JavaScript hat on and go well what is it that what is it that a JavaScript programmer would want here for
[408.44 → 414.46] their large apps, and it's clearly not to substitute a different language but rather it's to remedy you
[414.46 → 420.38] those things that are missing in JavaScript and at the time you know now before Emma script 6 that
[420.38 → 428.58] was things like classes and modules um but also and interfaces, but also you know static typing
[428.58 → 436.22] you know the ability to actually describe you know hey this function yeah it takes three parameters uh
[436.22 → 440.62] but by the way I could also tell you what the types of those parameters are supposed to be and then
[440.62 → 447.46] maybe you could check it for me instead of just blowing up at runtime um and so that was sort
[447.46 → 453.76] of the genesis of typescript was really is there a way we could add all of those things to
[453.76 → 460.00] JavaScript without actually messing with its core value proposition you know which is that it runs
[460.00 → 465.82] everywhere and is there a way we could do it so that you can maximally leverage all the goodness
[465.82 → 472.76] that already existed in the JavaScript uh ecosystem you know I mean that you guys know us as well
[472.76 → 478.48] as we that there's just an enormous amount of effort being poured into JavaScript in the open source
[478.48 → 485.30] community around frameworks for for JavaScript right I mean the classic example is jQuery but then
[485.30 → 491.68] you know beyond that it's just been astounding how many different frameworks there are and so part of
[491.68 → 499.00] our design sort of our key design goal was to make sure that we could leverage all of that or that
[499.00 → 505.10] you wouldn't have to give up all of that um and that again you know led us basically to design a
[505.10 → 513.18] superset of JavaScript that compiles to plain JavaScript and then I mean I think from there on it was
[513.18 → 518.58] really just sort of execution right I think that that was sort of like the core insight there was
[518.58 → 525.58] let's not try to let's not try to make your code in JavaScript by having you coding something else
[525.58 → 531.02] because that's just never that's just never gonna leverage the knowledge that you already
[531.02 → 536.56] have and typescript really is it is just like coding in JavaScript I mean if you look at your method
[536.56 → 544.12] bodies they are exactly the same code because mostly we can infer the types for you um it's really just
[544.12 → 549.00] the sort of surrounding fluff like you know you can put type annotations on your parameters and
[549.00 → 554.74] and whatever, and you can write declaration files for existing frameworks so we can pick up the static
[554.74 → 561.70] type information that way so it was October 2012 when um it first went public like you said it was probably
[561.70 → 566.44] one or two years before that you guys were working on it internally did you have internal teams
[566.44 → 574.28] using it um either in production or in research um prior to that public launch yeah it's been about
[574.28 → 581.08] three teams that were using it prior to it going public um one of those teams has now grown to become
[581.08 → 588.84] what's called Monaco it's like an ID in the web browser um part of Visual Studio online uh so that's
[588.84 → 594.32] that's been kind of cool to watch that they've they've been Gooding since like long before it was public
[594.32 → 600.64] and have been tracking along with us as we've grown they've been growing as well yeah and then the uh
[600.64 → 607.40] the f12 tools in uh Internet Explorer uh were written in typescript uh before we had gone public
[607.40 → 614.40] uh and I think we have some Asher properties that also used us uh before we went out yeah
[614.40 → 620.50] yeah so what would you say just estimating the time span between ideation of let's do this superset
[620.50 → 625.70] of JavaScript with type annotations and having something working usable that your teams were
[625.70 → 631.26] using it internally we're talking six months a year um how long that yeah somewhere
[631.26 → 637.30] somewhere in that range yeah yeah I would say yeah I mean we started there you know you always get
[637.30 → 644.92] there in circuitous ways right I mean you know in the beginning the vision i just
[644.92 → 650.48] laid out wasn't actually that clear you know, and we thought well maybe then also you know a key
[650.48 → 659.88] aspect is going to be having the VM use this type information to more efficiently execute the code
[659.88 → 667.22] and that's still an interesting idea, but it turned out not to be the sort of design pivot that we
[667.22 → 674.92] maybe thought in in in the beginning um I mean in a sense like becoming less ambitious made us better
[674.92 → 681.82] able to focus right once we started thinking tooling is the important part write es6 and make good tooling
[681.82 → 687.72] work on top of it so error checking and navigating to your code and I show up some of this and like the
[687.72 → 693.50] NG cone talk and if you guys saw it yeah but like you can just kind of quickly bounce around your code
[693.50 → 700.08] base doing refactoring renaming and it's really like Andrew's just saying you're still just, just playing with
[700.08 → 704.92] JavaScript with a little bit of extra help yeah I guess maybe that question jarred might be
[704.92 → 710.28] a little bigger than that so Microsoft's been changing quite a bit over the last I'd say year
[710.28 → 716.10] at least that I can tell from the outside uh, but you know adopting open source seeing and embracing
[716.10 → 721.54] open source a lot more embracing the community embracing pull requests on GitHub um and I'm wondering
[721.54 → 729.90] what role typescript plays in the future of Microsoft's direction like being HTML CSS JavaScript
[729.90 → 736.06] focused in the operating system and on the phone and elsewhere how do you know how to top down this
[736.06 → 740.08] come did it come from top down did it come from bottom up to see here's how we're solving solutions
[740.08 → 745.20] or solving these problems but also sort of Microsoft's general direction for product
[745.20 → 752.72] yeah it's its funny it's its not that it came it's neither top down nor bottom up it sort of
[752.72 → 760.60] organically came from people who were more affinities with areas that that that are in the open source
[760.60 → 768.04] space do you know what I mean it's like HTML JavaScript CSS whatever is very affinities with
[768.04 → 772.64] open source I would say because it's cross-platform it runs everywhere that's sort of its bread and butter
[772.64 → 777.92] right and it's its almost ridiculous to think about doing anything in that space without
[777.92 → 785.12] doing it open source um but over time that has gotten truer and truer for more and more areas
[785.12 → 791.08] right as you know it all sort of started with developers started like very developer technologies
[791.08 → 797.72] and now it's sort of spread into more and more you know throughout the software ecosystem if is is you
[797.72 → 806.96] will I think I mean we were early uh with you know on a Microsoft timescale if you will with
[806.96 → 813.96] open source and um and a lot of our learnings we have shared with other groups in the company
[813.96 → 819.96] and and and now you know certainly in the division we sit in the developer division uh the
[819.96 → 825.18] default answer here is that it's open source unless you have good reasons why it shouldn't be
[825.18 → 831.84] uh and that's a big that's a big turnaround from where we were you know and that was certainly
[831.84 → 838.44] not the default when we started with typescript um but I will say I mean uniformly even at that time
[838.44 → 844.54] people sort of realized that we have to we have to do this it's more a question of how you know because
[844.54 → 851.26] this is a big company with a lot of engineering culture that that was just done differently right and
[851.26 → 858.82] and if you don't just change it overnight and I would say even for us, you know like we sort of
[858.82 → 864.72] we sort of stumbled into open source in the beginning a little bit you know we hosted on
[864.72 → 872.00] complex because that was Microsoft's open source uh, uh repository right then, but that's not really where
[872.00 → 875.82] that community is, and you come to realize that, and you come to realize so they're sort of like doing
[875.82 → 881.40] open source and then there's doing open source the open source way and the latter takes a while to
[881.40 → 886.70] learn right I mean or there's just a culture there like is in any vibrant community and then you
[886.70 → 892.62] sort of gotta experience it in order to to to live it right just to speak to your point about how early
[892.62 → 899.20] inside Microsoft you all were as far as open sourcing like you said October 2012 uh recently we had on the
[899.20 → 905.64] .net core team uh that's episode 134 and that was like December 2014 was when that show aired they had
[905.64 → 910.44] open source .net announced the open sourcing of it uh sometime before that but within six months
[910.44 → 917.02] so there's 2014 versus 2012 you guys were definitely one of the earlier teams was there a decision to be
[917.02 → 921.58] made or was it just a fact of like was there even a discussion like this is going to be open source or
[921.58 → 927.60] was that something that you all had to come to I think it was you know to to to the people
[927.60 → 933.36] that were part of that decision I think it was clear to everyone that there's no way we're going
[933.36 → 940.72] to appeal to the JavaScript community if we're not open source um I mean we might appeal to
[940.72 → 948.16] a slice of the JavaScript community i.e. the slice that uses Microsoft tooling but that wasn't really
[948.16 → 953.58] the slice that we wanted to appeal to we wanted to broadly appeal to the JavaScript community and
[953.58 → 959.62] and really sort of deliver value in that community right and I think we all understood
[959.62 → 966.72] that that had that that had to mean open source uh it just had to and does that speak to
[966.72 → 971.94] your sensibilities because languages that you've had you know parted in the past Delphi proprietary
[971.94 → 977.58] at least the compiler is I'm not sure is the specification for Delphi open source or is that all
[977.58 → 986.48] proprietary stuff I don't know that there was one well there's your answer then um no it was not
[986.48 → 991.00] open I mean the heck open source hadn't been invented at the time I don't think you know so
[991.00 → 996.46] there was just no way it could be I mean an open source it's its stuff was around I mean
[996.46 → 1002.94] what year was that early 90s sure yeah yeah but I mean Delphi goes all the way back to
[1002.94 → 1009.06] Turbo Pascal was in 83 right I mean and then and then Delphi sort of grew out of that but yeah i
[1009.06 → 1015.02] i ecosystem there was an open source going on back then in the 90s when Delphi was having its
[1015.02 → 1023.36] heyday right I'm not sure i because i I wasn't here yeah yeah yeah okay um but either way
[1023.36 → 1030.76] you know it's um I mean the world has changed right I mean and and and it's just you know back, back then
[1030.76 → 1037.26] that was sort of how you you bootstrap yourself as a company you know and i I will say
[1037.26 → 1044.36] that the one thing I think that that Turbo Pascal and Dan Delphi both did was they um I mean turbo
[1044.36 → 1051.44] pascal at the time delivered a product that probably was an order of magnitude more efficient and cost an
[1051.44 → 1057.58] order of magnitude less than its competition right and so it maybe wasn't free, but it was
[1057.58 → 1065.62] pretty close to free it was 50 bucks where the competition was 500 bucks um and uh, and it ran at
[1065.62 → 1072.08] least 10 times faster than the competition right so so so it it definitely it changed
[1072.08 → 1079.96] things or if you know in in in other ways right um today it's its funny how we sell software
[1079.96 → 1085.02] and how open source is financed because obviously ultimately someone has to foot the bill right but
[1085.02 → 1091.08] but that's a different discussion right, but it's its it's yeah yeah that's a discussion
[1091.08 → 1097.46] we have often on changelogs we're often talking to you know small startups who are trying to
[1097.46 → 1103.60] bootstrap a company and do open source or do open source and it's still something that people
[1103.60 → 1109.98] are trying to figure out like is this even viable to have a purely open source company um so yeah huge
[1109.98 → 1115.24] discussions and interesting things but let's let's reel it back in and get back to where you guys
[1115.24 → 1122.40] are at because in 2012 you announced went public recently you know here we are in 2015 we've seen
[1122.40 → 1126.64] kind of I don't know if I call it a groundswell quite yet, but it's getting there were all of a
[1126.64 → 1133.26] sudden adoption is starting to really ramp up we have um angular 2 um announcing it'll be typescript
[1133.26 → 1140.76] driven dojo 2 definitely others what can you attribute that to is it just takes time
[1140.76 → 1146.10] uh how was it received let's stop there for a second how was it received when you guys first went public
[1146.10 → 1151.20] it was a mix of enthusiasm and suspicion
[1151.20 → 1158.18] i remember the first day when we went public we were watching all the social media and the
[1158.18 → 1164.98] twitter, and you know whatever the twitter uh and I'm I'm watching a stream of just negative just one
[1164.98 → 1170.32] after another and then another stream of positive I'm like oh my gosh, and you know this is what it's
[1170.32 → 1176.98] like to jump right into the pool and get feedback immediately, and it was interesting to
[1176.98 → 1183.78] kind of see once people started playing with it there was definitely a trickle maybe a trickle at first
[1183.78 → 1188.02] of people playing with it saying I'm never going to use this but I'm going to try it for five minutes
[1188.02 → 1194.50] and then after that going oh, oh I get it I get why they did this is actually kind of cool
[1194.50 → 1202.28] um and I think it took time for people to get over yes it's Microsoft right okay get over that try it
[1202.28 → 1206.80] yeah and kind of move towards something of like it's just a tool it's just the tool for doing
[1206.80 → 1210.64] JavaScript and web programming and stuff when you say that it seems like there's a little bit of
[1210.64 → 1215.38] suspicion there you know maybe the initial reaction was like why is Microsoft doing something
[1215.38 → 1221.84] open source, and you know in the vein of JavaScript especially back 2012 when we had no
[1221.84 → 1228.50] there's no precedence of Microsoft doing you know large-scale open source projects no and our track
[1228.50 → 1234.86] track record and JavaScript perhaps wasn't the best at that time either so yeah I mean it's its
[1234.86 → 1243.70] you know you i I always felt like uh you gotta earn it you know and i i I was uh I was not
[1243.70 → 1250.86] surprised that we got the reaction that we did I was actually fairly uh happy that we got as
[1250.86 → 1258.04] much positive reaction to it as as as we did um and I've always just believed but hey you know we're
[1258.04 → 1261.98] just going to stick to it, we're going to deliver some some some good product here we're going to do
[1261.98 → 1266.40] some good engineering we're going to try and solve the problem because I think we had the right idea
[1266.40 → 1271.88] for how to solve it, and then it'll, they'll come well maybe they won't but lets but we're going to
[1271.88 → 1277.06] believe that they'll come and then and now they're starting to come you now and then but but
[1277.06 → 1282.86] we've done a lot of hard work you know, and we've tried to listen uh to the community and we but
[1282.86 → 1288.46] we've also tried to have a point of view on how to solve this problem you know we're not we're not
[1288.46 → 1293.94] turning it into a kitchen sink which is very easy to do in the JavaScript space too because there's
[1293.94 → 1299.94] there's a new technology or a new framework or a new methodology born every day right and so you sort of
[1299.94 → 1304.82] got to stick to your gun on certain areas or guns on certain areas but but then still listen
[1304.82 → 1310.90] uh to the feedback um I think also one thing that I think we did right was
[1310.90 → 1319.72] to self-host and dog food from day one a lot of these transpires well now they're not but in the
[1319.72 → 1327.04] beginning you know early on like wit uh and and and script sharp were they target JavaScript but
[1327.04 → 1331.36] they're not written in JavaScript, and they don't actually live and breathe the JavaScript community
[1331.36 → 1338.18] to do you know what I mean and i I felt that I felt that we had to do that um and the other thing i
[1338.18 → 1345.34] would say that i I think was a guiding principle was that we're not just writing a compiler here and
[1345.34 → 1352.16] then we're not really doing this we're we're doing this because it ultimately enables us to build
[1352.16 → 1357.94] great tooling, and we're not just going to open source the compiler we're going to open source
[1357.94 → 1362.60] the tooling because it's it really the high order a bit here is the tooling it's the fact that
[1362.60 → 1370.22] you can get safe refactoring code navigation find all references go to definition etc you know and
[1370.22 → 1378.80] then and these are just like productivity must-haves today in on large projects right um and they're
[1378.80 → 1385.88] all powered by this knowledge that the compiler has but if you lock it up in a black box you know
[1385.88 → 1392.00] that is just a command line tool then you're not really solving the problem right um so you have to
[1392.00 → 1398.48] you have to like actually make your compiler into an API and you have to architect your compiler so that it can
[1398.48 → 1406.04] be super incremental and super lazy in how it is does its work so that it can deliver answers in
[1406.04 → 1415.40] sub 100 millisecond time even on a 200 000 line project right which you know honestly if you'd
[1415.40 → 1419.78] asked me five years or 10 years ago I would have I would have just said that it's just never going
[1419.78 → 1426.46] to be possible in JavaScript, but it turns out it is um what's and so that was sort of that was sort
[1426.46 → 1431.98] of a bet you know that we took there on on the technology and on our own ability to do it you
[1431.98 → 1439.40] know but it's its it's worked out what's different um you know what didn't you expect five
[1439.40 → 1442.96] or ten years ago when you said that was not possible JavaScript just the browser wars or
[1442.96 → 1451.08] the hardware has increased or what is it I think the the the order of magnitude um improvements in the
[1451.08 → 1458.22] VMS I don't think I don't think we all saw that coming it's quite a and I'll give credit to the
[1458.22 → 1464.44] v8 team and and and Lars uh bach and the work they did in Orcus is just amazing you now and then
[1464.44 → 1468.86] and now we're all doing it you know but they really sort of pioneered something there that was
[1468.86 → 1475.06] quite, quite impressive yeah it's kind of a shining example of that rising tide you know brings all the
[1475.06 → 1480.52] ships up because once that competition got really kicked off and all parties got involved it was
[1480.52 → 1486.50] fun to watch yeah from our side and just it is amazing what you can do in JavaScript now that even
[1486.50 → 1494.46] three or four years ago was just impossible and possibly slow yeah no that yeah no i to this
[1494.46 → 1502.98] day I am still i I am still you know there are days when I go wow that's amazing well let's pause
[1502.98 → 1508.38] there then let's let's dive into some amazing stuff, but before we do that lets take a break and hear a
[1508.38 → 1514.16] word from one of our awesome sponsors we'll be right back you've heard me talk about top towel several
[1514.16 → 1520.64] times in this podcast and top towel is by far the best place to work as a freelance software
[1520.64 → 1526.46] developer well they have this term elite engineer and that defines the kind of software developer
[1526.46 → 1532.82] that works at top towel I had a chance to sit down and talk to Brendan banished the co-founder and coo
[1532.82 → 1539.28] of top towel and I asked him Brendan what is an elite engineer take a listen an elite engineer for us
[1539.28 → 1544.58] as somebody who satisfies all the technical requirements um that you would need in a great
[1544.58 → 1549.48] developer if you're working at like uh like a Google or Facebook but then a top towel you have
[1549.48 → 1554.68] to add this extra layer on top of it to make sure that people are mature enough and professional
[1554.68 → 1560.28] enough to be totally self-directed and so making sure that they take a tremendous amount of uh pride in
[1560.28 → 1566.44] their work and that they're accountable and very, very communicative because in remote freelancing
[1566.44 → 1571.26] that's sometimes just as important as being technically competent all right if Brendan got
[1571.26 → 1575.74] you excited about being an elite engineer at top towel head to top towel.com slash developers
[1575.74 → 1582.78] that's t-o-p-t-a-l.com slash developers to learn more and tell them the change load sent you
[1582.78 → 1590.96] all right uh so we've been talking heavily and as you got some deep subjects you took there i almost
[1590.96 → 1596.14] wanted to vein off on several different directions but I think let's circle around language
[1596.14 → 1602.66] design of typescript uh it's a super set of JavaScript what else can you describe
[1602.66 → 1606.70] for typescript to sort of take us into the conversation around language design
[1606.70 → 1612.84] I think you know I mean so sort of the the the things maybe that are interesting to observe about
[1612.84 → 1619.74] it is that traditionally type systems have sort of been an on or an off thing you know you either
[1619.74 → 1625.58] had your dynamic language with which had no type system or at least not an observable type system
[1625.58 → 1633.12] um and everything was just dynamic, or you would be programming in a proper statically type programming
[1633.12 → 1638.80] language say like c sharp or java or c plus or c or whatever and everything would be statically
[1638.80 → 1643.82] typed so it was either you were either on or you were off on types I think the thing that's
[1643.82 → 1649.72] interesting about typescript is that it is an optionally typed or a gradually typed system
[1649.72 → 1656.58] you know you we've turned to switch into a dial you can dial up the types it's the dial starts at zero
[1656.58 → 1662.66] and that's just JavaScript, and you can literally rename all your JavaScript files to dot TS and just run
[1662.66 → 1668.22] them through our compiler, and you'll get a bunch of errors, but our errors aren't really errors they're all
[1668.22 → 1674.26] warnings right because the output we produce is indeed exactly the same files that came in because
[1674.26 → 1679.68] there were no type annotations to remove right so in so when the dials at zero we sort of
[1679.68 → 1685.74] function as a linter if you will that we do our best effort on inference um but in the absence of any type
[1685.74 → 1690.78] annotations you know there's only so much we can infer but based on those inferences we'll give you some
[1690.78 → 1696.96] errors right but then as you dial it up, and you add type annotations then more and more stuff comes alive
[1696.96 → 1703.08] and and and you, but you can sort of leave the dial wherever you want right you can use jQuery or
[1703.08 → 1708.96] whatever a bunch of JavaScript frameworks just as JavaScript, and then you can on the side
[1708.96 → 1713.52] provide the type information or not provide the type information and if you provide the type information
[1713.52 → 1719.30] in a declaration file then the tool can do more things for you like statement completion and so forth
[1719.30 → 1724.68] but it's perfectly happy for you to not do it, and then it's just dynamically typed um
[1724.68 → 1731.46] and that's sort of been an interesting world to navigate uh because no one had really done that
[1731.46 → 1736.14] before you know and that I know it was all or nothing right like you had to jump yeah exactly
[1736.14 → 1743.10] yeah yep and so that was a fascinating design point and uh I think we learned a lot from
[1743.10 → 1747.42] it I think the other thing that i I would say that that has been interesting from a language design
[1747.42 → 1756.36] perspective is that typescripts type system isn't about providing absolute waterproof guarantees that
[1756.36 → 1766.08] that these types are correct we're not provably correct we're just correct enough because ultimately
[1766.08 → 1771.90] when you start with a dynamic language where something could be of type any then you have a
[1771.90 → 1777.82] Swiss cheese right, and it's its just about plugging as many of the holes as is feasible it's not about
[1777.82 → 1785.42] plugging every hole right and traditionally uh java and c sharp and a lot of other languages have
[1785.42 → 1792.82] been about plugging every hole and providing strict guarantees and that's that's obviously useful but it
[1792.82 → 1797.76] but it lands you in a different place right and there's but if you think about it for JavaScript
[1797.76 → 1801.82] there's no way that we could ever land there right because that decision has already been made the
[1801.82 → 1808.50] runtime system is dynamic, but it turns out that there's still a lot of goodness you can get from having
[1808.50 → 1815.88] types um a lot of goodness right in the tooling um even if the types are not provably correct
[1815.88 → 1822.04] there's one other that I would probably add to that list that i I like which is the structural type
[1822.04 → 1829.72] yes, yes so traditionally in op and Los systems you're what's called anomaly typed you've got the
[1829.72 → 1834.76] class name, and you're like all right I'm going to subclass this class name, and it's its every time
[1834.76 → 1839.66] you're checking the types you're checking that these names are matching but in JavaScript everything is
[1839.66 → 1845.74] very loose-goosey I can make an object literal I can pass it in or I can instantiate a class as an
[1845.74 → 1851.68] object and pass that in and for us everything we just look at the inside of the type it's the
[1851.68 → 1856.86] structures match you know if it walks like a duck and quacks like a duck you know kind of that kind
[1856.86 → 1864.62] of thing and that makes it so easy to kind of extend existing systems and grow systems in a really
[1864.62 → 1870.32] flexible way that doesn't require these deep inheritance hierarchies yeah it's really lightweight
[1870.32 → 1876.50] and it's really nice yeah it's its much truer to the underlying truth of JavaScript which is which
[1876.50 → 1883.08] is very dynamic right so first I think making it a strict superset of JavaScript
[1883.08 → 1888.42] as far as adoption is concerned is kind of a brilliant move because now I can dip my toe in the
[1888.42 → 1893.50] water right and I can opt in when I want to as opposed to a big rewrite or having to make a big
[1893.50 → 1898.98] decision up front to use typescript or plain old JavaScript but when I opt into those type annotations
[1898.98 → 1907.70] it sounds like the biggest wins are in tooling which are valid nice wins of course do you also
[1907.70 → 1912.64] have performance wins or is it because the runtime itself is still dynamic um you can't do any compile
[1912.64 → 1920.22] time uh performance because it's not probably correct well I mean it's its it's so you're
[1920.22 → 1925.86] right that you you you I would say it's tooling, but it's of course also correctness right then and
[1925.86 → 1932.12] you know right sort of the notion that you can sleep better at night because some system actually
[1932.12 → 1936.68] like tried to validate your code here and told you about a bunch of problems that otherwise you would
[1936.68 → 1942.66] have found that as you ran the app one of the nice things on the typescript team is we had the creator
[1942.66 → 1948.42] of the chakra runtime engine the JavaScript engine for Internet Explorer so he was helping us early on
[1948.42 → 1955.52] the code that the compiler generated so the classes and whatnot the corresponding code that
[1955.52 → 1960.80] they output he was looking at that and saying all right for this to be optimized we should do it
[1960.80 → 1966.90] slightly differently and so his input meant that if you're writing against the know class
[1966.90 → 1974.16] syntax and whatnot in typescript you're getting very performant JavaScript on the outside the carry
[1974.16 → 1980.80] from that is that the v8 team took the typescript compiler and put it into their test suite so it wasn't
[1980.80 → 1986.56] just i.e. now you have uh Google Chrome getting all the performance benefits from those patterns
[1986.56 → 1993.08] hmm well that's interesting for sure beyond type annotations obviously that's your that's your flagstone
[1993.08 → 1997.76] feature there uh you know the name typescript it's all about type annotations are there any other
[1997.76 → 2005.76] big features that typescript adds to JavaScript um that are nice to have I I think i I would
[2005.76 → 2012.00] sum it up as we do two things one is types and all the great tooling and correctness proving that
[2012.00 → 2018.48] that comes from that and the other is delivering features from the future today basically giving you
[2018.48 → 2025.20] the ability to run down level or compile to down level right um I mean we started out with with with
[2025.20 → 2030.40] delivering a bunch of es6 features but allowing you to compile them down level to es5 and es3
[2030.40 → 2038.24] uh like classes and arrow functions and so forth right and now of course now Emma script
[2038.24 → 2045.12] itself is catching up uh and es6 is almost ratified it's going to happen in a month or two and we
[2045.12 → 2051.04] are catching up also in that we now support pretty much the full es6 language, but now we're also
[2051.04 → 2056.72] delivering features from the future again because we're we're starting to spike uh implementations of
[2056.72 → 2063.28] decorators um and async await and some of the other features that are being considered for Emma script
[2063.28 → 2070.88] seven, and it's really sort of a repeat n plus one here uh of the same of the same phenomenon right because
[2070.88 → 2078.64] the truth is that that even as even when Emma and a version of Emma script gets ratified it takes years
[2078.64 → 2087.52] for that to actually permeate throughout the JavaScript ecosystem in some places it permeates
[2087.52 → 2092.56] quickly like on the server where you can where you can arrange your own execution environment just
[2092.56 → 2098.64] by installing a new version of node or whatever right then you can pretty rapidly adopt but in the
[2098.64 → 2104.96] browser I mean you don't really have control of that, and it takes three four years before you can I mean
[2104.96 → 2112.96] even today you can't necessarily say that you require Emma script five right I mean and we certainly
[2112.96 → 2119.20] I mean it's getting truer and truer right but look at when did Emma script five come out right I mean
[2119.20 → 2125.76] that we're talking about what is it what is it in 2009 right I mean I think that silver just had their
[2125.76 → 2133.44] vote for i.e. support like a week or two ago to whether they should remove early versions of i so that is
[2133.44 → 2136.96] that's still a little conversation that the long-term support guys are still having
[2137.84 → 2143.44] so the reality probably is that it's going to be somewhere between three and five years before you
[2143.44 → 2152.88] can assume Emma script six and that means until then you're going to need a transpired or a down
[2152.88 → 2159.36] leveller right and typescript delivers both in one and that's a that's a pretty compelling combination
[2159.36 → 2166.56] I mean both that and the types right how do you guys decide on which features are going to go in
[2166.56 → 2172.16] these early features so let's talk you know ES uh seven which you know they're just now figuring some
[2172.16 → 2176.64] things out some are probably going to go in some aren't you know I'm just looking at a compatibility
[2176.64 → 2181.12] table there are some features I've never even heard of reflect dot realm apparently that's a
[2181.12 → 2187.36] proposed feature for es7 how do you decide when stuff goes in because you get in a situation where
[2187.36 → 2191.36] all of a sudden you add let's say you add support for reflect dot realm and don't ask me what that
[2191.36 → 2195.44] means but let's say you guys add that to typescript and then none of the know it doesn't get
[2195.44 → 2200.24] ratified or none of the browsers actually are ever going to support it do you guys pull it do you just
[2200.24 → 2204.96] wait until you're sure something's going to go in how do you deal with that yeah so, so first
[2204.96 → 2210.08] I think reflect dot realm is actually probably uh a runtime library feature so that one
[2210.64 → 2216.32] isn't that hard and the runtime library features generally speaking you can just polyfill, and it's
[2216.32 → 2222.48] it's its it's its a pretty established uh sort of scheme for how you deal with that um
[2223.52 → 2228.96] other features like modules for example modules were late to land in es6 you could argue that they
[2228.96 → 2235.28] haven't fully landed yet either because the standard doesn't actually include a spec for a module loader
[2235.28 → 2241.84] and which ultimately means you know you're going to be dependent on someone externally to provide
[2241.84 → 2249.84] that loader and then now with those well sometimes we have to guess right I mean in typescript
[2249.84 → 2256.16] when we realized early on that hey we're going to need some sort of module system one of the biggest
[2256.16 → 2262.32] problems of JavaScript is the lack of modular compilation one of the things that was powering node.js
[2262.32 → 2269.20] was you know the common JS modules and require JS in the browser and AMD modules and was sort of
[2269.20 → 2274.00] becoming the norm for large-scale JavaScript application development which is where we wanted
[2274.00 → 2281.20] to go so we had to have modules so we had to sort of do the best guess effort of where modules were
[2281.20 → 2287.44] going to go and try to make try to make our syntactic footprint as small as possible and then just go with
[2287.44 → 2293.12] it and then let it ride out and that's what we did, and then it turns out we shot pretty close to the
[2293.12 → 2300.16] target um, but it's not just, but it didn't land uh because those the current proposal didn't even
[2300.16 → 2306.64] exist at the time um so now we've aligned, and it turns out that we can support both, and we can just
[2306.64 → 2312.08] you know I mean we're not going to take stuff away I mean I've always I've always been a big believer in
[2312.64 → 2316.72] backwards compatibility if you look at all of my work and all the languages I've worked on they've
[2316.72 → 2324.24] pretty much always been backwards compatible because if you give up backwards compatibility you
[2324.24 → 2328.64] also give up your community and now the community can go shop around, and maybe they'll come with you
[2328.64 → 2333.60] or maybe they won't, you know but listen you've got to be you've got to bring them along and honestly
[2333.60 → 2338.96] it's the responsible thing to do too people have a huge investment in their code and so
[2339.84 → 2344.64] so we're going to continue support what we previously supported, but then we're also
[2344.64 → 2350.40] supporting Emma script 6 modules, and we expect people to migrate to that uh fully you know over
[2350.40 → 2356.24] time but uh so it's its doable you end up with a little bit of baggage, and you can park it
[2356.24 → 2361.44] under a compiler switch or something you know, and it's its it's fun it's its it was the right thing to
[2361.44 → 2366.88] do I think, but we are definitely committed to tracking the standards i I should say that
[2368.00 → 2373.68] and you can certainly see that in our work too even when you disagree with them yeah oh yeah
[2374.64 → 2380.00] hey some of the things in the module system uh today I may not necessarily agree with but
[2380.00 → 2384.64] there it is and that that's water under the bridge right I mean we participate in the
[2384.64 → 2391.92] standardization effort too so you know right that, but it's, but yeah so is there a canonical place to
[2391.92 → 2398.24] go for people to find these are the features that typescript adds that you know may or may not be
[2398.24 → 2405.36] available in es6 or in the browsers today do you guys have a place oh like on top of on top of the
[2405.36 → 2411.44] type system and on top of the JavaScript standard stuff like the additional features yeah or even
[2411.44 → 2415.36] you know features that have not quite been standardized yet or are in the process that
[2415.92 → 2420.88] you know you could perhaps use this in chrome today, but you can use it in typescript, and it'll
[2420.88 → 2430.32] you know it'll handle everything well i I mean all the type system is of course a feature that
[2430.32 → 2437.04] we add right and all the notation for how you write down interface types and union types and tuple
[2437.04 → 2442.16] types and blah blah blah and how does type inference work and how the generics work and all of that stuff
[2442.80 → 2450.32] is of course on top and something that we spec in our language specification um if you're
[2450.32 → 2455.84] curious about like yes seven features there's the on the GitHub site there's the road map right and
[2455.84 → 2460.96] we kind of roughly sketch out I mean even okay you don't know exactly where which feature is going
[2460.96 → 2466.16] when but we've got a rough idea for you know this version and the next version so we kind of put
[2466.16 → 2471.52] that on the road map yeah the road there's a link to a road map on the there's a link to a road map on
[2471.52 → 2478.16] the on the typescript front page on GitHub so oh cool perfect that's helpful yeah
[2478.16 → 2485.44] so let's talk a little bit about the compiler and the implementation of the compiler one thing you
[2485.44 → 2491.68] said earlier enters which was kind of piqued my interest is about the compilers API yeah and how
[2491.68 → 2496.40] important that was told us about that and then also tell us like how it's implemented is it in
[2496.40 → 2502.00] typescript I think you said it is but just because give us some of the details of the compiler okay it is
[2502.00 → 2507.60] in typescript yes I mean like I said we we we believe in dark booting and then, and we've actually we've had
[2507.60 → 2512.64] several versions of the compiler, but they were all written in typescript uh that the one that's
[2512.64 → 2517.52] that's there now and that's on GitHub and the one that we're that we're currently shipping um
[2518.56 → 2527.20] is uh it's about I'm going to say probably 32 000 lines or thereabouts for the core compiler itself and
[2527.20 → 2534.32] then another 15 to 20 000 lines for the language service about 50 000 lines uh all up um
[2534.32 → 2541.52] um, um before Andrews has a chance to be a little humble he wrote most of the new version of the
[2541.52 → 2546.00] compiler so he was just kind of brainstorming ways that we could be faster and lighter weight
[2546.64 → 2551.52] and uh in his free time was coming up with these ideas I was like guys like I think we should go this
[2551.52 → 2558.96] direction I'm like no we don't need to rewrite it we just released 1.0 and I said no, no i I think
[2558.96 → 2564.00] that's the way we should go and sure enough as it started coming together it was like five times
[2564.00 → 2569.60] faster than the original 1.0 compiler so he deserves a lot of credit for that, and it's like pretty much
[2569.60 → 2575.36] rewritten already by the time he had brought in you guys the uh the results like was there
[2575.36 → 2580.88] a big effort after that, or it was pretty much done well I mean i yeah i I started it's its actually
[2580.88 → 2586.16] kind of interesting because there are a couple of things first of all that i I would say about how
[2586.16 → 2590.32] the compiler is currently implemented one actually sort of general observation about
[2590.32 → 2596.96] compiler writing these days which is there's sort of the way that the universities will teach you
[2596.96 → 2602.56] how to write compilers and then there's the way that you have to write a compiler today for it
[2602.56 → 2606.64] to be relevant, and they're they're actually a little bit divergent right now because
[2607.52 → 2612.56] universities tend to still teach you the classic way of writing a compiler with you know you have
[2612.56 → 2618.96] a scanner and a parser, and you probably use some lair generator you know to generate your parser and
[2618.96 → 2624.96] then you have your code generator, and it's then there's this thing called speed and performance that
[2624.96 → 2633.36] you don't get to um but even more importantly there's this thing called incrementality
[2633.36 → 2641.28] that is an absolute must for a compiler that you can build into an IDE in an IDE when you're sitting
[2641.28 → 2646.48] there typing code let's say you're in a 15 000 line JavaScript file that's part of a 50 000 line
[2646.48 → 2652.96] project which so happens to be how say our compiler works right and I type food dot I want to see
[2652.96 → 2659.60] immediately what could I type here and I'm not if it takes more than 100 milliseconds I'm going to get
[2659.60 → 2667.36] annoyed now delivering meaningful semantically correct answers in 100 milliseconds is simply impossible
[2667.36 → 2672.08] with the way schools teach you how to write compilers you got to go about it completely differently
[2672.08 → 2677.36] you got to be much more incremental in your data structures you got to think about different problems
[2678.32 → 2685.76] your type system has to be implemented in a very, very lazy manner that produces just the right amount
[2685.76 → 2692.88] of information on demand as opposed to binding everything up front and then knowing the answer to everything
[2692.88 → 2699.20] even though i actually only need the answer to this over here right now so that that's that's interesting
[2699.20 → 2706.80] and there are a lot of learnings there that i think uh are interesting um with a with an editor
[2706.80 → 2714.32] too um and this is kind of obvious once I say it but as you're typing most of your program isn't correct
[2714.32 → 2719.28] while you're typing right so your language service has to be resilient to the fact that
[2719.28 → 2724.16] thing you're having errors left and right because everything's in transition, and then you stop
[2724.80 → 2730.64] you've hit a stopping right literally a single character typed at the right place in your editor
[2730.64 → 2736.88] can profoundly and completely change the meaning of your program right now most characters don't
[2738.24 → 2742.40] but sometimes they do you know like you start a comment here and the rest of your file becomes a
[2742.40 → 2748.16] comment or this identifier becomes another name and now all of a sudden it doesn't shadow another
[2748.16 → 2753.92] identifier and 10 000 references bind to a different symbol do you know what I mean or just like all
[2753.92 → 2761.92] these subtle things and it turns out that doing that incrementally it's a challenging problem and
[2761.92 → 2769.12] you can very quickly go astray in oh well I'm going to keep all these tables that backlink to this and
[2769.12 → 2772.64] then I'm going to try to incrementally update them and then before you know it
[2772.64 → 2779.28] you're generating so much information that that is so subtle in the way that it interacts you know
[2779.28 → 2786.40] that you die a quick death right and you really have to be pretty you have to you have
[2786.40 → 2791.20] to think about this problem hard you know to get it to be fast uh especially in JavaScript
[2793.60 → 2797.20] i never really thought about it like that that's that sounds like a really hard problem
[2797.20 → 2802.88] no I've never had a song it's a fun problem it's an it's a fun problem i and and and uh and I think
[2802.88 → 2807.76] we we we I mean I'm not going to say that we've solved all, but we're we do we're doing pretty well
[2808.32 → 2812.72] in our compiler right now one of the one of the things that Andrews was talking about before
[2812.72 → 2816.96] addition to the compiler we have this language service that's open source and people can play
[2816.96 → 2822.32] with, and we put out we put that out a couple of years ago and people started doing things like
[2822.32 → 2829.76] adding support to eclipse um more recently there's been a plugin for Adam the typescript team has
[2829.76 → 2835.36] written one for sublime, and it's its kind of neat that this thing is kind of proving itself out in a
[2835.36 → 2841.20] way right we're sticking it in all these text editors and ides and getting a nice rich experience yeah
[2842.32 → 2848.72] but so some of the stuff we do in the compiler is um we've actually learned a lot um over the
[2848.72 → 2854.16] the years from say functional programming if is you look at how our compiler is is is built
[2854.16 → 2860.08] internally it is very much relies on immutable data structures and incremental updating of immutable data
[2860.08 → 2868.88] structures we also strangely in the compiler itself we generally don't use classes uh the compiler is
[2868.88 → 2876.40] just written as a bunch of nested functions and interface declarations so in that sense it is sort of
[2876.40 → 2882.00] uses the other way of coding in JavaScript you know where you write functions and then
[2882.00 → 2888.96] functions return objects that contain function pointers, and you make closure over local
[2888.96 → 2896.88] state and so forth, so our entire type checker is a single function and that function just returns out
[2896.88 → 2901.52] a callback interface that you can ask questions on, and then it'll lazily go about its work but
[2901.52 → 2906.48] but it's and one single function closure and if you want to have three type checkers that's fine
[2906.48 → 2910.72] you call the function three times now you have three separate type checkers that are maintaining
[2910.72 → 2918.16] their own separate state internally and um so it's uh yeah so it's its it's interesting in uh
[2919.44 → 2924.88] in that sense but I will say too that that is you know like when we talk about JavaScript
[2924.88 → 2931.20] the good parts that is one of the very good parts about JavaScript is that Brendan got uh he got it right
[2931.20 → 2938.32] when it came to uh functions and and and uh and closures and sort of the functional aspects of the
[2938.32 → 2942.96] language then there are other things that are not so great, but that is a super great thing
[2943.52 → 2949.36] and it really does work very, very well and now with the VMS that that that have gotten good at
[2949.36 → 2955.84] optimizing that as well it is a remarkably productive way to code uh i I'm really enjoying it yeah
[2955.84 → 2960.96] I'm sitting here listening to your knowledge here and I'm going to get a little bit upstream
[2960.96 → 2966.80] perhaps a little bit meta because I'm thinking about uh our universities and the things that we're
[2966.80 → 2973.20] taught how to write a compiler in university right and how there are very few people who have the
[2973.20 → 2978.40] skill set and experience to you know retool a compiler in their free time and have a 5x speed improvement
[2978.40 → 2983.68] um and no doubt and there's that was like based on years of your experience of writing compilers
[2984.32 → 2989.60] how do we institutionalize some of this knowledge that that few people have how do we pass it down
[2989.60 → 2995.28] to the next group of people who um need to be writing compilers 10 years from now 15 years from now
[2996.00 → 3001.44] um have you put thought into that is it just too hard of a problem or no i something else we can be doing
[3001.44 → 3008.24] well I think that the best thing that we possibly could do is open source right I mean and that's what
[3008.24 → 3013.28] we're doing yeah good point source code for this compiler you get hey you can have it right now just
[3013.28 → 3019.52] go clone the git repository and there it is, and it's not very I mean it's its 50 000 lines that's not
[3020.48 → 3025.04] I mean it's its a lot of lines, but it's not that many lines I mean you you can find your way
[3025.04 → 3031.20] around in it, you can see how it's done exactly i was just going to say the same thing I reading
[3031.20 → 3038.00] code and talking through code with people that are knowledgeable we can't, you can't get away
[3038.00 → 3043.68] from that and because it's open source, and you have these communities maybe we supplement the
[3043.68 → 3048.80] the formal education with go work on this open source project and contribute to it yeah I think
[3048.80 → 3054.40] that's a very meaningful way to do it yeah because that will force you to actually understand how it
[3054.40 → 3059.36] works such that you can contribute right well not only the not only the technical side of that too
[3059.36 → 3063.04] but also the community side of that like you said earlier it's a culture you know you said there's
[3063.04 → 3067.52] open source there's the real open source way you know yeah I think part of institutionalizing that
[3067.52 → 3073.52] jarred is as you're talking about in contributing to open source is not only getting the code right but
[3073.52 → 3078.72] also interacting with the community of what the community needs from the from what you're producing
[3079.76 → 3084.96] yeah yeah well said well let's pause here for our sponsor break we get back we're going to
[3084.96 → 3090.72] get back to adoption and why we've had you know all of these large projects adopted, and then we'll talk
[3090.72 → 3095.52] about in the small like how could I adopt it what are the steps i have to take so we'll pause here
[3095.52 → 3102.48] and I'll be right back good news our friends at digital ocean are opening up a brand new European
[3102.48 → 3110.40] region in Frankfurt Germany the first in Germany fra1 is now open the new region features their latest
[3110.40 → 3117.52] cloud spec and the full range of digital ocean features including metadata core OS and IP version 6
[3117.52 → 3123.20] something else that's cool is due to its placement on the German commercial internet exchange which is
[3123.20 → 3128.80] the largest internet exchange point worldwide by peak performance this region will serve Germany and
[3128.80 → 3134.56] its neighbouring countries with unparalleled connectivity and speed the story of the German startup community
[3134.56 → 3140.08] is tremendous and digital ocean is hoping by launching this new region they can play a part in supporting the
[3140.08 → 3146.32] innovation and awesomeness that's happening in Germany so definitely check out fra1 for those
[3146.32 → 3152.00] subscribing to digital ocean for the first time use our promo code changelog April or changelog may
[3152.00 → 3157.68] to get a 10 hosting credit when you sign up head to digitalocean.com to get started and now back to the show
[3159.60 → 3165.76] all right we are back talking typescript there have been a few large projects that have announced
[3166.40 → 3173.52] that they will be typescript in their next major releases the biggest one being angular which will be
[3173.52 → 3180.48] angular 2 will be written in typescript and then also dojo 2 will be written in typescript if you
[3180.48 → 3186.80] guys had to guess or if you had some insight into why now and maybe even some insights into if you were
[3186.80 → 3191.68] involved at all in the angular decision or if that was completely on their end I'm interested to hear
[3192.96 → 3199.36] how it's taken a few years but maybe what's led to the increase in adoption lately I can take a
[3199.36 → 3204.24] I'll try to take a stab at that one all right so I think one of the one of the things that we've
[3204.24 → 3211.12] seen in the last six months um now that es6 is becoming close to ratified is this excitement in
[3211.12 → 3217.36] the community around es6 like it's at the point now where it's deafening, but six months ago like the
[3217.36 → 3224.96] the movers and shakers were looking at um these projects that could be done with es6 you've got modules
[3224.96 → 3230.00] you've got classes you've got a new way of writing JavaScript that just wasn't possible before
[3230.56 → 3237.60] so as a library author when you're thinking what is my API going to be like you know six months
[3237.60 → 3242.24] from now or two years from now what is the new set of libraries that are going to be built look like
[3242.24 → 3248.08] and I think as a library author you want always to be at that edge when you're showing that yes we've
[3248.08 → 3254.80] got all this stuff there's no reason to go on to some something new we can do it here so i I would
[3254.80 → 3260.24] say that that's probably what started kicking off people thinking about what does the API look like
[3260.24 → 3266.96] now that um es6 is getting a lot of traction there's a lot of interest in making sure that the API
[3266.96 → 3273.68] has fit really well with that uh as far as typescript I mean typescript has been there kind of building
[3273.68 → 3280.00] up like we've been saying since 2012 we've been slowly building momentum um and beating on this
[3280.00 → 3288.16] drum of like es6 is great, and you can get that plus some good tooling last year when uh the
[3288.16 → 3295.60] angular team announced ad script uh at the NG Europe conference um they were talking about yes
[3296.32 → 3301.68] having es6 is great and then having types is great, and then they also wanted this separation of
[3301.68 → 3307.04] concerns idea called annotations, and after they announced that we kind of reached out to them
[3307.04 → 3314.08] and said well that sounds great let's talk about that so me and Andes and some of the engineers
[3314.08 → 3319.76] flew down and talked to them and said you know what can we do like can we just take our ideas
[3319.76 → 3325.36] and kind of merge the philosophies and come up with a typescript that's even stronger and capable of
[3325.36 → 3331.28] working with these really rich libraries so we've been working with the angular team for about six
[3331.28 → 3335.28] months now yeah, and it's it was great actually I mean getting in a room together you
[3335.28 → 3340.16] you very quickly discover you're all just engineers and you really all think about the problem the
[3340.16 → 3347.36] same way and then that you have the same values you know and then and for them types is very
[3347.36 → 3353.28] relevant you now and then and es6 for sure, and then you know we sort of had both and there
[3353.28 → 3358.48] were some things we didn't have like annotations, and so we worked with them on that and uh and
[3358.48 → 3363.68] pulled in some other folks from the JavaScript community and came up uh or hitched on to the
[3363.68 → 3372.40] the decorators um uh proposal for es7 um, and we worked with uh Yehuda cats who do timber and rob Eisenberg
[3373.12 → 3378.08] that did the Randall and is working on a new project called Aurelia and tried to get everyone
[3378.08 → 3383.68] thinking along okay what is this separation of concerns feature look like you know some people are coming
[3383.68 → 3389.44] up from a metadata point of view like annotations on like python point of view for decorators now can
[3389.44 → 3395.76] we make a single thing so that's been that's been an interesting challenge it's nice to see everybody
[3395.76 → 3400.96] coming together one of the things that I was really bullish on a few years ago was the WebKit project
[3400.96 → 3407.20] and just seeing you know people I guess a political term stepping across the aisle uh you know Microsoft and
[3407.20 → 3414.24] google here working together on typescript with angular um seems like a lot of good can come out
[3414.24 → 3421.68] of that yeah no i i I'm certainly hoping I mean so far I think a lot already has come out of it yeah
[3422.16 → 3427.52] but uh yeah absolutely um it's been a great it's good it's good it's a great team they're fun to work
[3427.52 → 3431.28] with yeah super fun work with, and it's been a lot of learning experience because we're coming up from
[3431.28 → 3437.04] two different angles and can sit in a room and talk the same language it's cool I like the point you
[3437.04 → 3443.20] you made there Andrews about just the fact that uh you're all engineers you know you're all people
[3443.20 → 3448.40] in the end and even going back to your comment earlier about the commitment to open source and
[3448.40 → 3453.76] doing it the right way that way I mean when you take your flags down, and you're talking about just
[3453.76 → 3459.36] open source and in general to the world you kind of have to be like jarred said stepping across the
[3459.36 → 3464.96] aisle you can't let your badge sort of stop you from committing towards the future of what's
[3464.96 → 3471.92] good for the source code yeah yeah it's kind of something that Yehuda said uh last episode 151
[3471.92 → 3475.52] in fact you mentioned you had a cat so we had him on last show he was talking about rust with Steve
[3475.52 → 3482.96] flank and uh I had mentioned that rust is a Mozilla research project, and it is um, and he made the
[3482.96 → 3489.28] point of saying it is a Mozilla research project but Mozilla embraces the open source model, and they've
[3489.28 → 3495.20] done a perfect job of making it a community effort, and it's not all about Mozilla it's about
[3495.20 → 3500.00] an open source project that will forward the goals of Mozilla as well as the goals of perhaps their
[3500.00 → 3505.84] competitors um but the entire ecosystem, and we have to come together around those these projects and
[3505.84 → 3511.44] you know everybody benefits from it there's also there are benefits from competition as well so it kind of
[3511.44 → 3517.28] goes both ways um it's nice when people come together it's also nice when they compete heavily um
[3517.28 → 3523.36] kind of we can kind of win in both scenarios so let's talk about getting started from uh from a
[3523.36 → 3528.32] layman's perspective if not with the angular team or the dojo team but let's just say I'm just
[3528.32 → 3534.64] writing my own JavaScript I'm an application developer maybe let's take it from the uh from in the Microsoft
[3534.64 → 3540.00] camp as far as tooling goes and then maybe in like the node camp as far as tooling goes how do I get
[3540.00 → 3546.96] started with typescript so if you're a Microsoft developer probably the easiest way is just to install visual
[3546.96 → 3555.76] studio um so starting with Visual Studio 2013 update 2 uh typescripts has been in the box so you
[3555.76 → 3561.68] start up an application, and you can immediately start up a typescript application template and go from
[3561.68 → 3568.88] there if you're coming at it from open source uh point of view you can NPM install typescript and use
[3568.88 → 3576.56] the typescript compiler uh straight from NPM of course it's its all JavaScript right so all the all
[3576.56 → 3580.40] this typescript is compiled away, and we've got JavaScript so you could if you wanted you could
[3580.40 → 3586.40] just clone the repo and run the typescript compiler straight from the clone repo, and you'll have the
[3586.40 → 3594.40] most bleeding uh up-to-date uh typescript i i I will say too that that that one of the things because
[3595.04 → 3601.60] because we focused really hard on making the language service uh language services open source we now have
[3601.60 → 3609.52] uh a number of really high quality plugins for all the popular editors out there so if you're using
[3609.52 → 3617.68] um uh say sublime text or adam.io then there are excellent plugins for those editors there are
[3617.68 → 3625.92] plugins for eclipse uh there's JetBrains has very good support in WebStorm for typescript, and they're
[3625.92 → 3633.04] actually keeping up with all the evolution in the language um uh, and they offer a number of great
[3633.04 → 3640.64] refactoring tools in there as well so, so by and large I mean there 's's perfect coverage
[3640.64 → 3647.28] for typescript across the board in development tools and ideas yeah and like to build tools like grunt
[3647.28 → 3653.60] and gold right as you dig into you know whatever your favourite flavour is you can find a growing
[3653.60 → 3659.12] number of typescript plugins for these various systems i we should mention too you know one of
[3659.12 → 3665.60] the probably one of the biggest treasure troves uh of information for typescript is an uh is a GitHub
[3665.60 → 3672.48] repository uh repository called definitely typed um I don't know you guys have looked at it but I saw that
[3673.28 → 3679.92] this is something that happened entirely organically uh in the OSS community and it is it's its so
[3679.92 → 3686.56] warned my heart to see it happening too is you know people very quickly after we uh um
[3687.20 → 3694.24] shipped the first version of typescript realized that wow uh I can actually go write these declaration
[3694.24 → 3699.92] files for existing JavaScript frameworks and then get a much better experience when I'm using the
[3699.92 → 3708.32] framework in typescript, and we provided some rudimentary declaration files for jQuery and node
[3708.32 → 3713.60] and a few I think backbone we had a little bit, and you know, but it wasn't a lot and then of
[3713.60 → 3720.08] course we've written down all the type definitions for the JavaScript runtime library and the HTML Dom
[3720.08 → 3726.88] but that was really all we had in the beginning, and now we have this repository that is that that is
[3726.88 → 3734.88] I think now close to a thousand frameworks I kid you not one thousand different frameworks have pretty good
[3734.88 → 3740.16] coverage and some of them have very, very high quality definition files up there and there are
[3740.16 → 3746.40] provisioning tools now like TSD that allows you to just say hey today I'm going to use jQuery with ember
[3746.40 → 3751.52] and this one and that one just like NPM it'll provision your project with all the correct declaration
[3751.52 → 3758.08] files and lo and behold you get super high quality statement completion as you're authoring your code you
[3758.08 → 3764.00] you know just magically right, and it's its fantastic and that's entirely a community effort
[3764.64 → 3770.56] and i I just think that is like that truly speaks to the power of open source there is no way
[3770.96 → 3776.08] that a single entity could have done that that is something that only a community can do yeah having
[3776.08 → 3778.08] written the jQuery one that took me weeks
[3780.72 → 3783.52] yeah that's spectacular we'll definitely link that up in the show notes
[3783.52 → 3787.68] yeah, and you said it you said it well there and there's that like this is the kind of stuff
[3787.68 → 3791.44] that happens in the open source community that you just couldn't have predicted it you didn't have to
[3791.44 → 3797.52] ask for it somebody wanted if it was a good idea and everybody just starts pitching in into their little
[3797.52 → 3802.48] wheelhouse you know if you're into uh Sammy JS, or you're into
[3803.12 → 3806.80] crypt or like whatever you happen to be into in such a huge JavaScript community
[3807.44 → 3811.60] um you just play your part, and then you have this great community resource spectacular
[3811.60 → 3818.16] yeah exactly yeah so what about learning so that's how you get technically started but what if I don't
[3818.16 → 3823.68] have any idea what type annotations are or I want to learn how to write them and where do I go for that
[3824.48 → 3828.16] so there's a there are a couple of resources on the website that you can use to get started
[3828.72 → 3834.16] um we've got some samples so if you is just staring at code is the easiest way for you to learn
[3834.96 → 3838.40] you can go and there's a sample section on the website, and you look through that and there's
[3838.40 → 3845.60] each of them are fairly small um examples of using node or using jQuery just enough to kind of
[3846.32 → 3854.32] get you started uh there's also a handbook uh the handbook tries in plain English as best as I've been
[3854.32 → 3862.16] able to write plain English uh to walk you through the various features and the 1.0 uh the 1.0 language
[3862.16 → 3867.36] and we'll, we'll be kind of revising that um here shortly to kind of pull it up to date with the
[3867.36 → 3873.52] later versions of language but if you read through that you there are tons of examples uh tons of plain
[3873.52 → 3879.76] text to kind of understand um, and you know maybe to call it the spec if you are the kind of person
[3879.76 → 3884.32] that really likes to dig into the details there's the typescript spec, and you can read that and
[3884.32 → 3891.12] really understand it in a deep level speaking of the spec I noticed that was in a PDF is that spec
[3891.12 → 3895.76] ever going to be open source on GitHub or is it already open source and this is compiled from a
[3895.76 → 3902.80] repo or something it's its it's well it's available in three different ways as a doc file as a PDF
[3902.80 → 3910.16] file and in Markdown so it it's its on there if you just go to the front page on our GitHub site and
[3910.16 → 3915.20] then link there's a link to the language specification and that's a markdown a single markdown file so okay
[3915.20 → 3921.92] guys I'll leave that up then yeah so next up let's talk about the future a little bit um you have a
[3921.92 → 3928.16] roadmap on the website that you told us about uh maybe kind of just verbalize the roadmap a little
[3928.16 → 3935.20] bit and tell us um where typesets at as far as I think we are at a 1.4 release and 1.5 is in alpha
[3935.20 → 3942.80] or beta and then kind of what you guys see you go into next sure so the 1.5 release is going to
[3942.80 → 3948.64] close a lot of the gaps that we had in es6 compatibility I think after 1.5 there's only a
[3948.64 → 3956.08] couple of features left class expressions um generators that we'll need to add to kind of
[3956.08 → 3962.24] finish up the es6 compatibility so that's that's kind of a nice milestone for us to actually be
[3962.24 → 3968.40] able to say yes we are a superset of JavaScript and that superset is a superset of es6 um we're
[3968.40 → 3974.24] looking at es7 features Andrews mentioned async away earlier that's going to be fun for kind of
[3974.24 → 3981.12] the promise programming uh style to be able to have nice clean uh async away code we've been
[3981.12 → 3987.76] talking more recently about things like JSX and exploring JSX support um there's a pull request
[3987.76 → 3993.52] now if people want to kind of hop on and help out and give us their feedback we would love that so um
[3993.52 → 4000.40] so definitely do that and decorators is another one yeah so um, but basically we're
[4000.40 → 4008.24] like 1.4 is is is the version that's out there now 1.5 is imminent you know within a month or two
[4008.24 → 4016.32] um we plan to ship that 1.6 will be the one that that rounds out a few more of the missing features
[4016.32 → 4024.08] and then finally 2.0 will be done with es6 and the es7 things that we so far have
[4024.64 → 4028.88] have on our roadmap but then I'm sure by then we'll, we'll have dreamt up some more work you know but so
[4028.88 → 4037.84] um it just keeps on coming it is seems i I know that we're talking now about doing something
[4037.84 → 4045.52] around uh module bundling also to make it easier to consume es6 modules in a browser environment which
[4045.52 → 4052.08] today requires you to use an external module loader, and you know, so there's like there 's's a ton of
[4052.08 → 4058.32] stuff we can do uh, and we can of course always do more IDE features and and and so there's no
[4058.32 → 4064.32] shortage yeah exactly I mean one of the things with the JavaScript committee um is that they're
[4064.32 → 4072.40] now on a one-year cadence so every year they're going to revise uh Emma script so es7 is next and
[4072.40 → 4077.36] es8 is the following year I mean we're going to be busy just keeping up and being a super set
[4077.36 → 4083.28] uh with a nice rich type system and tooling that that builds on top of that so is it fair to say
[4083.28 → 4087.20] the type system is pretty much done, and now it's just going to be in maintenance mode, and now it's
[4087.20 → 4091.20] just keeping up or is there additional things that you can do to make the type system better over time
[4091.20 → 4096.32] as well oh no there are definitely things we can do to make the type system better you can always make
[4096.32 → 4103.04] type systems better um I mean we were talking with the flow guys about union types, and they're like
[4103.04 → 4108.64] great if you have an if statement, and then you check what the type is in that if statement you
[4108.64 → 4113.68] know in the body of the if what the type is and as we're brainstorming with them, we're like oh that's
[4113.68 → 4118.64] that's a no-brainer let's throw that in there too um so as people do explorations I think the
[4118.64 → 4122.64] type system is just as organic as such a JavaScript language it's going to grow and kind of
[4122.64 → 4129.44] incorporate patterns and whatnot uh that we can yeah yeah we're sort of always on the lookout for
[4129.44 → 4136.32] you know why did I have to put a typecast here why did I have to have this annotation, or you know
[4136.32 → 4141.20] could is there a way we get rid of that uh you know so is there a way you could capture this
[4141.84 → 4148.00] this pattern or this idiom you know in the type system so we could better you know sort of
[4148.00 → 4154.64] understand it without you having to annotate anything um so that and that's going to be ongoing plus
[4154.64 → 4160.24] you know whenever a new feature is introduced in the language we have to sort of work out the type
[4160.24 → 4165.92] theory behind that feature right and get that integrated into typescript so there's always that
[4165.92 → 4174.00] angle to it as well we've got uh 1.5 it's an Alfie just announced that about 20 days ago you got your
[4174.00 → 4179.84] roadmap which is I love your roadmap too by the way it's great that how it's linking out to issues that
[4179.84 → 4185.68] have commentary from you all in the community sort of feeding back into this I think it's a really
[4185.68 → 4191.84] great way to line out a road not, not just uh straight up text but when we're talking about the
[4191.84 → 4198.56] roadmap and future versions of typescript what do we let's have some fun and hypothesize uh each of you
[4198.56 → 4203.20] towards what the future of typescript might be where would we be at in a year what we'll be
[4203.20 → 4210.40] talking about for typescript well I mean i i I'll be a little bit pedestrian i I still think we're
[4210.40 → 4216.88] going to be talking a lot about es6, and we're going to be talking a lot about modules because es6 isn't
[4216.88 → 4221.92] quite done when it comes to to to modules you know they've spec'd the language syntax, but they haven't
[4221.92 → 4228.56] actually spec'd the underlying runtime loader semantics um and so there's still a whole
[4228.56 → 4235.60] bunch of gyrating going on in the community around that right now uh I think some of the new es7
[4235.60 → 4241.92] features we're going to be looking at we're going to be looking at different uh development tools to
[4241.92 → 4250.40] integrate with uh maybe deeper integration with build systems and sort of this whole the whole cycle of
[4251.44 → 4257.60] I edit something and now I click on my browser I want to see the result over there and shortening
[4257.60 → 4263.76] that as much as possible right and making the compilation step as automatic and as and as and as
[4263.76 → 4269.84] ephemeral as possible right is something that we're gonna that we're going to keep iterating on um
[4269.84 → 4275.44] for sure um are there any particular uh adoptions of typescript that you're looking forward to liking
[4275.44 → 4280.64] uh is there anyone out there that is a perfect candidate for it that if they were listening to the show
[4280.64 → 4285.92] right now you know they would, you would put them on your radar essentially to say you all should adopt
[4285.92 → 4294.72] typescript well I think you know anyone who has more than say 10 or 20 000 lines of JavaScript in
[4294.72 → 4301.20] their app really owe it to themselves to take a look at this because it really is a time saver i
[4302.24 → 4307.36] i I will say you know like just you know the project that we work on daily which is the
[4307.36 → 4312.96] typescript compiler itself but it but in a sense it's just a large JavaScript app right it's a 50 000
[4312.96 → 4318.88] line JavaScript app I shudder to think what it would be like to write that without types i I don't
[4318.88 → 4325.52] I can't even I mean I can't even imagine I mean because we refactor that so much right and that's
[4325.52 → 4330.72] what gives us our agility and the ability to keep up with all of these features and these new
[4330.72 → 4335.28] things that are happening it's like that you can trust the system you can go okay well I'm gonna now
[4335.28 → 4339.60] I'm going to refactor this class or this interface or this function into these two things and I'm gonna
[4339.60 → 4345.60] rename these properties and boom boom boom done and now i get all this time back that I can
[4345.60 → 4353.60] use to creatively think about the problem instead of doing the manual labour that it otherwise turns into
[4353.60 → 4361.20] right yeah and to me that is just like that's just bread and butter I mean you just gotta do that if you
[4361.20 → 4367.92] want to stay competitive you know so yeah we have a few closing questions I share with you all via email
[4367.92 → 4373.92] that uh we got several, but we're only going to do two today um and the first uh we could take turns
[4373.92 → 4378.72] and we can start with you but who is your programming hero
[4382.00 → 4386.24] yeah Jonathan and I were actually we're talking about that at lunch i I think you know if I have to
[4386.24 → 4391.92] think back on my career and who had the sort of biggest impact and then launched me into this
[4391.92 → 4399.44] whole thing it's probably uh the inventor of pascal uh Niklaus bird um who's uh i i I was fondly
[4399.44 → 4405.52] recounting and Ben Jonathan knows the book too his book called uh algorithms but plus data structures
[4405.52 → 4412.24] equals programs um one of my favourite computing books I remember reading it cover to cover and
[4412.24 → 4418.88] understanding every word in there it just made so much sense it is so simple that's how I learned about
[4418.88 → 4424.24] hash tables which i I didn't know about when I first wrote the first version of Turbo Pascal
[4425.12 → 4429.84] and then I read about these things called hash tables I'm wow that what really and then I went
[4429.84 → 4436.56] and implemented another compiler went twice as fast and I'm like awesome you know so it's its that
[4436.56 → 4441.12] to me that was just that was good stuff you now and then his career has been amazing
[4441.12 → 4448.72] he's had a huge impact on our computer science uh and on my career yeah wow what about you Jonathan
[4448.72 → 4455.52] uh see he took my answer did I really oh I'm sorry no it's fine it's fine when we were talking at
[4455.52 → 4462.16] lunch uh I was like you know Klaus bird is like one of the guys that really stuck to his guns and said
[4462.16 → 4469.36] look simplicity is important programmer productivity is important to don't complicate it put them as close
[4469.36 → 4475.84] to solving their problem as they can and let them rip and that's why pascal is so easy to implement
[4475.84 → 4482.32] as a language so writing a compiler for it is really easy but learning it is really easy um and
[4482.32 → 4489.36] his thoughts like he never left that as he made each one like module and over on he was still
[4489.36 → 4496.64] always all about trying to find the simplest way to solve the problems and i you know whether
[4496.64 → 4502.64] his particular aesthetic is something that really fits you know you like i just have to
[4502.64 → 4509.68] respect his philosophy and kind of what he brought yeah yeah uh something else someone else that i
[4509.68 → 4517.52] like because he's entertaining us Simon Payton Jones one of the inventors of pascal uh is uh really
[4517.52 → 4524.16] fun to listen to really fun to kind of get excited about what is possible in programming languages um i
[4524.16 → 4530.32] always i always kind of fall back to him sometimes all right we got uh our last question is bringing
[4530.32 → 4536.00] it back to typescript here I guess is uh you can either answer it together or individually whatever
[4536.00 → 4542.08] makes sense, but it's pretty simple but um I guess we may have answered it to a degree but how can the
[4542.08 → 4546.96] community listening in so and as you answered anybody who's got 20 000 lines of JavaScript needs to
[4546.96 → 4554.16] look at typescript um but in other ways how can the community step in and either take part do
[4554.16 → 4561.28] something with it or help out with typescript how can the community begin to support and show support
[4561.28 → 4569.52] back to you all and move the mission forward well i you know I invite anyone who cares to
[4569.52 → 4577.12] come join us on GitHub and put up pull requests or and and and and and and speak up on issues you
[4577.12 → 4583.84] know or post new issues you know our new requests for features that's a great way we are all up
[4583.84 → 4590.64] there we live and breathe our daily programming lives on GitHub uh so we're very easy to
[4591.20 → 4596.16] to reach that way um and there's all these community stuff like Andrew's just talking about
[4596.16 → 4600.88] definitely types get on there if there's a library that you love that you don't see yeah, or you know
[4600.88 → 4605.44] there 's's like little errors that you can fix I mean it's going to be trivial to fix the DTS file
[4605.44 → 4610.72] you just go in and say oh no the type is actually this not this um, and you're you're going to help yourself
[4610.72 → 4618.48] and others um all the editors and whatnot just using these tools and then sending feedback
[4618.48 → 4623.36] um and making even better tools I think anything in the roadmap that somebody can take part in under
[4623.36 → 4628.40] the 1.5 is an alpha now, but you got things like uh exposing new editor interface to TS server is that
[4628.40 → 4635.28] something that is better served by the core team or better served by those that can are you looking
[4635.28 → 4642.88] for adoption support growth where can people I guess is that a good place to look at I think both
[4642.88 → 4648.80] I mean i I think it is whatever strikes your fancy if is is you have an editor that you're
[4648.80 → 4653.68] implementing, and you have a plug-in model or for it or you have a favourite editor, and then you know
[4653.68 → 4660.00] how to write plug-ins for that editor maybe write a typescript plug-in and try to use our new TS server
[4660.00 → 4666.80] infrastructure for that which is what we used for the sublime uh plugin uh for example or if you're
[4666.80 → 4672.88] interested in compilers or ides or whatever you know come to the other side and help, help us out you
[4672.88 → 4678.48] know with your favourite feature, or you know if you're interested in programming language design
[4678.48 → 4683.28] I mean one of the things that we've done in the last year or so when we moved to GitHub was we put
[4683.28 → 4687.84] all this programming language design we were kind of doing behind closed doors we're like enough
[4687.84 → 4693.68] all of it goes on GitHub so all the languages are all the language design is now done on issues in
[4693.68 → 4701.36] GitHub, and you can jump in and kind of give your two cents on if this feature you know fits with the
[4701.36 → 4705.68] kind of problem space or if there are little gotchas and you realize what the gotchas are, and you can
[4705.68 → 4710.80] let us know it's all kind of out there for people to comment I noticed when I was looking at one of
[4710.80 → 4715.68] your um actually the TS server one that you mentioned the issue out there you have a
[4715.68 → 4724.00] label of CLI or CLA not required is there a CLA required at some point uh yeah, so there's uh when
[4724.00 → 4730.56] you contribute code to the typescript code base uh you sign a contributor license agreement um and
[4730.56 → 4735.52] there's a there's a little robot behind the scenes that it's checking all the pull requests
[4735.52 → 4739.28] coming in we're trying to make it a little less noisy than it being on every single pull request
[4740.40 → 4744.88] that's something else we talked about too I believe it was with go when I was talking to
[4745.52 → 4751.04] Andrew Durand he was talking about how they um let me go back to my notes on that one they're using a
[4751.04 → 4759.60] particular external feature if it's called Garrett g-e-r-r-i-t-t I believe or i-t um, and it's
[4759.60 → 4767.12] an external code review system that kind of builds into um a CLA thing because they have a special CLA for
[4767.68 → 4772.96] contributors, so yeah probably have similar problems you look at that listen that show or talk to Andrew
[4772.96 → 4778.88] he'll probably help out okay that sounds interesting well that's it for the closing questions um i
[4778.88 → 4785.68] think you know we zoom back out typescript seems really neat because it's something you can begin
[4785.68 → 4792.64] using today without having to really fully adopt it and sort of inch your way in as you get more and
[4792.64 → 4798.40] more courageous into the typescript world so pretty exciting to have this conversation with you guys
[4798.40 → 4804.88] is there anything else that you want to mention before we tail out and close the show um now can't
[4804.88 → 4810.40] think of anything I think we covered a bunch of stuff here i i I really appreciate the uh opportunity
[4810.96 → 4815.20] on the show here I think this was you guys on Twitter where can people follow you at oh yeah no we're
[4815.20 → 4822.88] we're uh we're both on Twitter yeah what's your handle my handle is a Heidelberg a h-e-j-l-s-b-e-r-g
[4822.88 → 4831.12] and mine is at j-n-t-r-n-r and there's also the typescript uh project has its own at typescript
[4831.12 → 4837.28] link, so feel free to follow those or ask us questions through twitter good deal um and one
[4837.28 → 4842.72] thing actually now that I have time to kind of ask your audience if there are people in the audience
[4842.72 → 4849.28] that are big typescript fans or big typescript users um recently we just started putting little
[4849.28 → 4853.44] logos on the typescript website to kind of show off all the people that are typescript fans the
[4853.44 → 4859.04] batch collect yeah so we're trying to kind of show off you know here 's's the here's our showcase
[4859.60 → 4866.48] so if your project or if your company is big typescript users um let us you know let us put your
[4866.48 → 4871.60] logo up there and kind of show off that uh you're doing all this typescript awesome that's the friends
[4871.60 → 4878.32] of typescript if I'm that's right yeah awesome well definitely uh fun having you guys on the show today
[4878.32 → 4883.44] um I know we had several conversations earlier to get this show on there and I'm glad it finally
[4883.44 → 4888.40] worked out to get timing there we had spring break we had several things so finally got you guys on the
[4888.40 → 4895.60] call today um in the future for listeners of the change law we have a show planned to talk about 17
[4895.60 → 4902.32] years of curl with uh Daniel Steinberg, and we're also going to have that conversation on roots and bedrock
[4902.32 → 4906.80] I was sick this week you're listening to this in the future and I'm talking about in the past but
[4906.80 → 4911.36] long story short I was sick so we don't actually have a show that uh that we shipped for roots so
[4911.36 → 4916.24] there was a break there, and we had the typescript show instead so uh thanks to the sponsors and
[4916.24 → 4921.68] thanks to all you for listening and uh with that fellas let's say goodbye
[4921.68 → 4935.12] bye
[4935.12 → 4965.10] I love you.
