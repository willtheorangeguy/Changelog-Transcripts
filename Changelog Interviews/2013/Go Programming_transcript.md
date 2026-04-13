[0.00 --> 9.52]  this episode is part of a remastered greatest hits collection and features rob pike and
[9.52 --> 23.26]  andrew durand talking about go we are joined today by rob pike and andrew durand from google
[23.26 --> 27.30]  to talk about all things go the language that is so welcome to the show guys
[27.30 --> 33.98]  hello yeah we're excited and we've heard a lot of interest uh around go in the last you know
[33.98 --> 40.62]  a couple years but it seems like in the last um you know six months we've had a lot of people
[40.62 --> 44.88]  hitting this up hey you guys should cover more go you guys you know should get some some people
[44.88 --> 51.54]  from go on the uh on the show so why don't we uh kind of get started and talk about just for the
[51.54 --> 56.32]  people that may have heard of it but don't know much about it what can you guys give us a little
[56.32 --> 63.22]  bit of an introduction to the language so well go is a language that was released in november 2009
[63.22 --> 71.36]  so about three three and a half years ago nearly four and um basically it's a it's a language that
[71.36 --> 77.04]  sort of sits in the middle ground between low-level languages like c and your sort of scripting
[77.04 --> 82.98]  language like python or ruby um but it's a statically typed language so it gives you all of the sort of
[82.98 --> 88.76]  safety that comes with that um and it has uh some concurrency primitives that make it easy to model
[88.76 --> 98.06]  um concurrent programs processes um but uh and a nice system of interfaces um which makes it easy to
[98.06 --> 106.30]  to uh write composable software um but it's also a very simple language so unlike a really heavyweight
[106.30 --> 111.08]  language like c++ which has pretty much any feature you could imagine and they're adding more every day
[111.08 --> 118.14]  go has a much more uh minimal philosophy where we we put only the things that we thought were really
[118.14 --> 124.78]  essential into the language um and so as a result i think the the real selling point of go is that it
[124.78 --> 130.58]  provides a a great developer experience um everything we try to make everything as consistent as possible
[130.58 --> 137.20]  and uh so it's a lot easier to to keep all of the state that you need to to write software in your head
[137.20 --> 144.22]  at one time um it's kind of a difficult thing to summarize because i can i can tell you a list of
[144.22 --> 151.20]  things that go is or go isn't but um really i think it's the the experience that makes go um what it is
[151.20 --> 157.50]  the last few days i've been uh using go for a personal project which surprisingly i haven't been able to do
[157.50 --> 162.34]  very much of at all but the last few days i've been having fun doing some stuff and i i need to connect to
[162.34 --> 167.76]  some old software i wrote many years ago and i had got to do kind of an ab comparison of the code i was
[167.76 --> 174.14]  writing in go versus the c code from 20 years ago that did similar things and it was it was an
[174.14 --> 178.90]  interesting comparison because i remember very much writing the old c version of this stuff and how
[178.90 --> 183.80]  long it took and how difficult it was and this is a time when i was probably as experienced in c
[183.80 --> 189.58]  programming as just about anybody but i find that the go code ends up being you know a third to a half as
[189.58 --> 195.92]  long on the page um it takes me an order of magnitude less to get it right once it compiles
[195.92 --> 202.14]  it's probably correct and bug free um and so the productivity i've been feeling is is really really
[202.14 --> 206.58]  high but then this morning i was noticing when i was running my test the entire test suite took eight
[206.58 --> 213.70]  milliseconds to run um and so it's it's productive for me but it's also productive for the computer and
[213.70 --> 217.94]  i think that's that's the thing that's that's drawing people into the language they just feel like
[217.94 --> 223.44]  once they finally try it out they're pleasantly surprised with how productive they feel and how
[223.44 --> 231.36]  fast everything runs not just their own world but the computer as well yeah so obviously speed is kind
[231.36 --> 237.18]  of a always a top priority but it seems like uh you know a lot of the questions that i've seen just kind
[237.18 --> 242.24]  of you know perusing the internet for things all things go related seems like a lot of questions i see
[242.24 --> 247.90]  are things that you know why doesn't go do x or why doesn't go support y right so as you said
[247.90 --> 253.22]  it kind of seems to imply that the language like has had simplicity kind of as a core value would i
[253.22 --> 258.88]  mean would you agree with that absolutely um but when when you ask why doesn't it have something
[258.88 --> 265.14]  that's kind of a strange question because i mean you can answer it you have to give me specifics you
[265.14 --> 270.02]  know why doesn't have x or y but the thing you should be asking is given that it doesn't have this
[270.02 --> 275.26]  thing how do you expect me to solve this particular problem i have right and we can always answer that
[275.26 --> 280.92]  question more productively than just saying why some particular feature is missing the thing is
[280.92 --> 288.92]  that although it turned out to be very popular with a lot of ruby and python programmers we came
[288.92 --> 297.48]  from a much more system side of the world mostly writing in c and c plus plus and we tried to reduce the
[297.48 --> 302.62]  number of things in the language down to a set where we could precisely control the semantics of the
[302.62 --> 306.74]  language the semantics of the implementation we wanted to have a language that we could completely
[306.74 --> 313.60]  keep in our heads that any two go programmers would be as you know you have the same language
[313.60 --> 318.88]  they're using so if you know having worked in c and c plus plus for many years especially c plus plus
[318.88 --> 323.92]  if i see someone else's c plus plus program you know three quarters of the time i have to go look
[323.92 --> 328.14]  at the reference manual to see what this feature is they're using because i've never been you know
[328.14 --> 332.86]  i may not even know what it is or i may be unfamiliar with it or i've never used it in practice
[332.86 --> 338.50]  uh and that's a really awful state to be in and i've never written a lot of ruby but i've heard
[338.50 --> 343.16]  similar things about ruby that it's very hard to read a ruby program not that the language is big
[343.16 --> 348.86]  but that there's so many different ways you can say effectively the same thing and we want to go to be
[348.86 --> 354.76]  much more direct that not necessarily there's only one way to do it um i hope a language is never that
[354.76 --> 359.86]  restrictive but that however you choose to do it i can read it and quickly understand what it is
[359.86 --> 365.08]  you're trying to get done and that by by me and you i don't just mean me and you i might mean me
[365.08 --> 369.36]  and me six months from now coming back to code i've forgotten about yeah it's very important i'd be able
[369.36 --> 372.92]  to read code later that i wrote six months ago because i don't have it in my head anymore
[372.92 --> 380.96]  yeah i mean when and i think it's a good point when people ask the question why doesn't go do
[380.96 --> 385.44]  whatever it is whether they're talking about exceptions or generic types or you know things
[385.44 --> 390.62]  like that the answer that the community seems to give them is you know well hey here's what you're
[390.62 --> 394.50]  trying to do so you don't need that to solve this problem here's the solution here's how you could
[394.50 --> 399.20]  solve this problem and i think that that's something that kind of happens organically and and the
[399.20 --> 403.46]  community itself kind of grows up around it with that mindset and i think go has kind of captured
[403.46 --> 409.14]  that for systems developers which is a which is a good a good uh you know maybe a separation from
[409.14 --> 414.46]  what the uh history of these languages has been so that's a that's a good thing for sure i think
[414.46 --> 418.44]  one thing that's worth noticing and something that people don't think about a lot is that
[418.44 --> 428.38]  go places a lot of emphasis on uh constructing uh well specified and kind of pure apis so it gives you a
[428.38 --> 433.08]  lot of language features that are specifically designed to make it like the system of interfaces for
[433.08 --> 440.44]  example the packaging system the way uh names are exported or or unexported from package namespaces
[440.44 --> 446.82]  all these features are designed to make it easy to specify a good api and i think that uh go really
[446.82 --> 452.32]  pushes programmers to think about api design um but then once you're actually doing the implementation
[452.32 --> 457.64]  it's it's nice for implementing stuff um but because it lacks some of the meta programming
[457.64 --> 466.08]  stuff you find in a lot of scripting languages or even in c++ um you might find that the rather than
[466.08 --> 471.56]  being able to don't repeat yourself to the utmost extreme you might have to copy and paste a bit of
[471.56 --> 478.70]  code here and there um instead of sharing it in some central place um and so i think uh in some places go
[478.70 --> 484.64]  forces you to do a little bit more work on the implementation side but i think that the benefits as far
[484.64 --> 490.46]  as comprehensibility are concerned um far outweigh the the drawbacks on that side so i think that's
[490.46 --> 495.06]  something that newcomers to go have to sort of adjust to is that you know if they don't have their
[495.06 --> 500.06]  favorite pet feature from another language that lets them avoid writing the same for loop twice
[500.06 --> 505.66]  um they kind of just have to deal with that right people coming to go from other languages come with
[505.66 --> 510.38]  a way of solving problems that they're used to and a set of principles that they believe are
[510.38 --> 517.14]  sacrosanct from their environment and go probably doesn't really address either of those but instead
[517.14 --> 523.78]  substitutes a different way of looking or at things or building software and one of the things you have
[523.78 --> 529.20]  to learn when you move to go is to to release yourself from some of those old ways of working
[529.20 --> 535.54]  not because they're incorrect but because they're not the best way to get it done and go go is weird in
[535.54 --> 542.44]  this respect when we first uh announced it back in 2009 there was a fair bit of negativity on the
[542.44 --> 548.12]  response to the language because people looked at it and didn't see anything interesting and or saw
[548.12 --> 554.68]  things or didn't see things they expected to see there's a fair bit of sort of negative press about it
[554.68 --> 560.46]  there's a fair bit of positive stuff too but i think it was mostly negative but over time um people
[560.46 --> 568.44]  started using it um becoming familiar with it and realizing that go is actually surprisingly good
[568.44 --> 574.76]  because although it doesn't look like there's very much there what is there combined so powerfully
[574.76 --> 580.40]  that what seems like a very simple and kind of dull language when you read the spec is actually
[580.40 --> 586.24]  incredibly powerful and productive because it has a fairly strong set of totally orthogonal features
[586.24 --> 592.56]  that combine really easily to build really really strong software very quickly that's something that's
[592.56 --> 597.46]  very hard to see when you read the spec you really have to use the language to to feel it and i think
[597.46 --> 604.20]  the reason it's been catching on lately is that the community of users has grown enough that people
[604.20 --> 607.44]  are telling one another about you know this language you heard about it's actually you know a lot of fun
[607.44 --> 611.86]  you should try it convincing their friends to try it and there's kind of a runaway effect going on
[611.86 --> 618.26]  and it's finally nice to see uh that sort of growth happen by sort of word of mouth and people happily
[618.26 --> 622.94]  talking about this language and how to use it and why it's different because it's not gratuitously
[622.94 --> 627.62]  different it's different for a reason yeah it's it's kind of what i was hitting on before about the
[627.62 --> 632.26]  organic growth that that go has kind of seemed to garner which is like you know the community is
[632.26 --> 637.54]  growing it rather than it being forced down anybody's throat which i think you know the the fact that
[637.54 --> 643.96]  the the reason that i you know just as some you know some lonely old developer in over in the states
[643.96 --> 648.90]  the reason that i have heard about go has been from people that i know and respect and you know
[648.90 --> 653.98]  am friends with and work with like recommending that i check it out and look into it and and that's
[653.98 --> 659.16]  something that i don't know what it is that you guys captured to get that with go but that's something
[659.16 --> 664.94]  that you know i think kind of encourages the community to be more supportive and more um integrated
[664.94 --> 668.62]  rather than this you know fragmentation that you might see in some of the other languages that
[668.62 --> 673.22]  you know have been around for so long i think there are a couple of reasons why the language
[673.22 --> 680.44]  worked like that that that are worth mentioning um it was mostly designed by uh ken thompson robert
[680.44 --> 687.56]  greaser and myself who are at least in one case literally a gray beard um we'd been programming for a long
[687.56 --> 693.64]  time we tried many different systems uh and we kind of knew what was good and bad in the programming
[693.64 --> 699.14]  environments that we'd used and and what we tried to do was to reduce uh reduce it down we're all
[699.14 --> 704.82]  minimalists by nature and so it's very important that we construct something that was small and
[704.82 --> 709.66]  simple and easy but we're also pragmatists we write code that works we like things that work
[709.66 --> 716.06]  and the combination of pragmatism and minimalism is i wouldn't say unique to go but it's certainly
[716.06 --> 724.38]  very strongly expressed in go um another feature of the design process is that ken and robert and i
[724.38 --> 729.40]  are all very different um you know robert comes from a background that is very different from the one
[729.40 --> 734.28]  ken comes back from and ken and i overlapped a little bit at bell well we have overlapped a lot at bell
[734.28 --> 738.80]  labs but our backgrounds are very different and so we have three very different takes on what's what matters
[738.80 --> 744.42]  in programming and when we were designing the language one of the essential point of the language
[744.42 --> 750.48]  design was that anything that went into the language had to be agreed as necessary by all three of us
[750.48 --> 756.48]  it was designed entirely by consensus by three very different people and as a result everything that
[756.48 --> 760.92]  went in felt absolutely necessary no matter where you were coming from no matter what your background
[760.92 --> 765.22]  was or what you thought was important in program development um now of course it doesn't cover the
[765.22 --> 770.36]  entire space of what people think is important but i think it it really mattered to have such
[770.36 --> 775.10]  different viewpoints come in and yet arrive at a consensus i think that's why the language
[775.10 --> 780.94]  manages to succeed even though it seems fairly simple and and it's that everything that went in
[780.94 --> 787.38]  went in after a lot of thought a lot of discussion and a very different analysis from from people with
[787.38 --> 793.74]  very different backgrounds it's also you know it's not supposed to be like a a neat cool language it's
[793.74 --> 799.98]  supposed to be it's it's very utilitarian in design it was designed to do to solve the problems that
[799.98 --> 803.54]  we had at work right i mean yeah and you're not you're not language designers we're not language
[803.54 --> 808.18]  designers by nature we're we're programmers we happen to know how to build language implementations
[808.18 --> 813.80]  and so yeah i mean we were working at google we were unhappy with the development environment we had
[813.80 --> 821.20]  um we felt unproductive and we wanted to be productive again and the specific problems we were trying
[821.20 --> 825.88]  to solve were those forced on us by the google environment internally and the c plus plus
[825.88 --> 831.38]  language in particular i talked at length at this at a splash keynote last year that you can you can
[831.38 --> 838.06]  find online pretty easily um but what was interesting what was surprising to me very pleasantly surprising to
[838.06 --> 844.22]  me was although we came from that very specific sort of problem space the thing that resulted seems to be
[844.22 --> 849.80]  generally useful and very popular in a in a wide variety of contexts we thought of it and in fact
[849.80 --> 854.16]  initially branded it as a systems language but it's pretty clear it's not a systems language
[854.16 --> 859.14]  alone it's a general purpose programming language that people could have used to do a lot of very
[859.14 --> 867.08]  very different things cool so we kind of took a deep dive into what what the uh what the language
[867.08 --> 871.84]  is and what's the purpose of it but you know we didn't really kind of talk about you guys at all so
[871.84 --> 875.86]  if you guys wouldn't mind just kind of circling back and for in the sake of filling in some gaps can
[875.86 --> 879.20]  you kind of give us just a little bit of an introduction to who each of you are and what
[879.20 --> 886.60]  your kind of role is with the project um well i'm rob pike i am a physicist by training um but ended up
[886.60 --> 891.58]  working at bell labs research in the computing science department for many years that was the lab that
[891.58 --> 896.96]  developed unix i wasn't involved in the early unix as i came in there shortly after research version
[896.96 --> 903.54]  seven came out but i was intimately involved in in the research uh editions of unix that followed
[903.54 --> 910.06]  version 8 version 9 version 10 you probably don't know what any of those are um but then uh very much
[910.06 --> 917.56]  like with go uh ken and i started talking in the 80s about you know unix wasn't really wasn't able to
[917.56 --> 920.70]  grow anymore the way that we wanted to and so we started talking about other things we could
[920.70 --> 926.36]  think about ways to sort of rejigger the models that we had and deal with networking and graphics
[926.36 --> 932.56]  better and so on and plan 9 from bell labs came out of that work um i think plan 9 is a very
[932.56 --> 936.96]  interesting system it never caught on you can argue about why it didn't catch on i don't want to have
[936.96 --> 943.30]  that argument um but i think that the ideas in it are still very relevant and um have some of them
[943.30 --> 948.04]  have made it into other places linux has some of the critical ideas from plan 9 but not nearly enough
[948.04 --> 953.96]  um and then you know we worked on that for a while then you know business markets changed and we had
[953.96 --> 959.80]  to do something much more uh commercial we did this system called uh inferno which was a sort of set
[959.80 --> 966.74]  top box system and an interesting virtual machine language that ran on it called limbo um which happened
[966.74 --> 972.22]  to have the bad luck to come out exactly the same time as java and given the sun's marketing machinery was
[972.22 --> 977.94]  much better than uh at&t's and lucents uh it never really saw the light of day the way that we'd
[977.94 --> 985.34]  like it to um but then i um the world collapsed because people didn't understand how telecom growth
[985.34 --> 990.50]  worked and so in the early 2000s i was looking for a job and google seemed like the interesting place
[990.50 --> 996.90]  to go um and i think that was a good call on my part and so i've been at google for about 10 years
[996.90 --> 1004.30]  now working originally on things largely behind the scenes um systems infrastructure the stuff behind
[1004.30 --> 1009.02]  that little tiny text entry box you see but stuff that i really can't talk about very much because
[1009.02 --> 1012.94]  it's kind of how you know it's part of the secret sauce although i was a very small part of the
[1012.94 --> 1018.26]  machinery and then you know as i said about five years ago we started being unhappy with
[1018.26 --> 1026.34]  um working in c plus plus working on 10 million line pieces of code and trying to think about better
[1026.34 --> 1032.70]  ways to do stuff so um although i'm not a language designer by nature i actually solved a number of
[1032.70 --> 1039.30]  problems through my career by designing custom languages so we proposed doing another one to
[1039.30 --> 1042.74]  solve google's problems and that's pretty much what i've been doing for the last few years
[1042.74 --> 1049.26]  so what is your role on the pro on the actual maintaining of the language itself now look like
[1049.26 --> 1055.74]  um i spend a fair bit of my time basically dealing with the open source community writing i tend to
[1055.74 --> 1061.90]  think of myself more as a library guy as far as go is concerned um do a lot of library work uh tooling
[1061.90 --> 1067.90]  i've written some of the stuff that'll be in 1.2 when it comes out um but i'm just one of the
[1067.90 --> 1075.66]  what we call core members of the team here um google pays me to work on go among other things and it's a
[1075.66 --> 1083.50]  really a privilege to be able to do that absolutely um and my name is andrew durand and um i'm an
[1083.50 --> 1089.74]  australian as you can probably tell from my bizarre accent that reminds me of as often as possible um
[1089.74 --> 1096.38]  i i i sort of started working for internet companies as a teenager as a programmer and have just kind of
[1096.38 --> 1100.94]  uh moved around in the industry in australia working in a variety of environments in different
[1100.94 --> 1107.02]  languages um none of which is particularly noteworthy but it was certainly a good experience
[1107.02 --> 1114.38]  um and then uh just around when go was released uh my friend uh pamela fox um was sitting near rob she
[1114.38 --> 1119.02]  was a googler her father was my advisor as a graduate student by the way that's total luck
[1119.02 --> 1125.02]  nothing to do with any of this no um but she you know was in developer relations she knew that the
[1125.02 --> 1130.86]  go team was looking for somebody to be um a developer relations person on go which is someone
[1130.86 --> 1136.38]  who's basically a public interface between a google project and the outside world um and she said yeah
[1136.38 --> 1139.98]  you should you should get involved with this go thing and i was like i don't know this go language
[1139.98 --> 1148.38]  looks pretty weird uh maybe i guess i could see um and you know interviewed uh met some of the team
[1149.50 --> 1153.50]  i got really excited about it got the job and within you know a few months was
[1153.50 --> 1161.58]  uh totally immersed in the go world and having a great time um and so my my role in in the team
[1161.58 --> 1166.22]  is as i said to be sort of a public face for the project to a degree i mean i give a lot of talks
[1166.22 --> 1173.26]  um i write the go blog um i spend a lot of time arguing with people on hacker news and reddit and
[1173.26 --> 1180.06]  stuff like that i'm just trying to make sure that our positions are well understood um as a team as a
[1180.06 --> 1185.42]  project i work with people in the community i also maintain a few of the tools some related to
[1185.42 --> 1191.10]  documentation and like our presentation software and um and also work on parts of the standard
[1191.10 --> 1195.58]  library and tool chain and produce the binary distributions and all those all these kind of like
[1196.30 --> 1203.50]  uh pieces that that make go easier for developers to use so i'm really just there making sure that we
[1203.50 --> 1208.38]  don't lose sight of our users but it's it's actually a kind of unusual role for someone in my position at
[1208.38 --> 1215.90]  google because most people with my job description at this company um work with an internal uh google
[1215.90 --> 1221.34]  engineering team and the community that uses that product say like the app engine team and people
[1221.34 --> 1226.70]  who use app engine but um for me i work with this group of people who are also in the open source
[1226.70 --> 1231.58]  community so i kind of have um it's my job's actually a lot easier in many ways because if people
[1231.58 --> 1235.34]  have questions about our development process i can just point them to the development mailing list and
[1235.34 --> 1240.22]  they can see exactly how we're doing the work as we're doing it there are no no secrets really
[1240.78 --> 1244.78]  one thing we haven't mentioned that i think should be made clear here is that go is a truly open
[1244.78 --> 1251.50]  source project all the development happens in the open um and as i like to say google imports the open
[1251.50 --> 1256.78]  source project for its internal go development not the other way around so it's really it's a truly open
[1256.78 --> 1261.34]  source project if if google you know suddenly decided they didn't like us working on this and they pulled
[1261.34 --> 1265.58]  the plug there would still be a thriving community of open source developers on the project it's not
[1265.58 --> 1271.50]  a it's it's not a google branded project in any way it's just that google's you know like likes having
[1271.50 --> 1276.38]  us work on it because it helps them for its own development work but it's truly an open source project
[1277.26 --> 1282.38]  yeah you you actually hit on something i noticed that the golang.org website doesn't have any google
[1282.38 --> 1286.22]  branding on it at all yeah they actually wouldn't let us we wanted to put google branding on it when we
[1286.22 --> 1290.22]  launched and they said no you can't and now i realize that was actually very smart of them
[1290.22 --> 1295.10]  yeah it's actually really a good idea because it's not a google project in in any formal sense
[1295.10 --> 1300.46]  and you know we have we have uh many contributors from outside google that work on the project
[1300.46 --> 1306.30]  every day and um you know to put a google google name on it would would kind of detract from
[1306.86 --> 1311.10]  the huge huge efforts from the open source community there are far more committers outside
[1311.10 --> 1316.22]  google than inside at this point far far more yeah so well about four years ago when you guys were on
[1316.22 --> 1319.98]  the when you rob were on the show uh previously i think you said that there were six
[1319.98 --> 1324.78]  people maybe six or seven people in google that were working on the project so how many people in
[1324.78 --> 1330.78]  google now are working on the project i don't know not a lot more maybe twice that yes it's still a
[1330.78 --> 1337.74]  very small project from from google's point of view i mean but the the community itself is much larger
[1337.74 --> 1342.86]  that's around that's for sure oh yeah yeah uh yeah there are thousands of people out there and many
[1342.86 --> 1347.66]  many companies every morning i get up there's some new blog that's gone up from some company i haven't
[1347.66 --> 1352.22]  heard of talking about how they're using go internally it's really gratifying i'm i'm really
[1352.22 --> 1358.46]  personally pleased because i think that um you know we we saw certain development problems we were
[1358.46 --> 1362.30]  trying to deal with and we've you know word a language to try to make them better which
[1363.10 --> 1366.54]  on the face of it sounds kind of crazy it doesn't sound like the language is the problem
[1367.02 --> 1371.90]  um but it is and i talk about that a lot in the splash talk um but it's nice to see that other
[1371.90 --> 1377.34]  companies have have found the same consequences of switching to go that they actually are productive
[1377.34 --> 1382.38]  their software is safe and efficient and it's actually really rewarding one of the things that
[1382.38 --> 1388.06]  doesn't get talked about at go very much um i did mention in the splash talk last year quite a bit but
[1388.06 --> 1395.34]  it's really the only place is that the problems we were facing developing software at google were
[1395.34 --> 1401.82]  problems of development in the large software constructed of many millions or even tens of millions of
[1401.82 --> 1407.74]  lines of code thousands of engineers working on it actively uh large-scale deployments you know
[1407.74 --> 1414.62]  many instances of a binary running in production those those are things that the languages really
[1414.62 --> 1420.14]  any of the language i know hasn't explicitly been designed to address and go was designed to make
[1420.14 --> 1426.30]  that kind of development process more productive and there's a lot of reasons of there's a lot of
[1426.30 --> 1432.54]  features in a language that are explicitly designed around programming in the large even though when
[1432.54 --> 1438.78]  you're using the language from day to day you don't really feel it that way how dependency works uh rules
[1438.78 --> 1446.46]  about how naming works in the global space um properties of the the production tool chain a lot of things
[1446.46 --> 1453.90]  that really are about making the large-scale software development process very productive surprisingly it turns out
[1453.90 --> 1457.98]  that also makes small scale development much nicer too but that wasn't our goal
[1459.98 --> 1465.02]  so your goal as you've stated was kind of you were frustrated with the the state of the language that
[1465.02 --> 1471.42]  you guys were using internally so you developed this and how inside of google how have you seen the
[1471.42 --> 1476.62]  adoption of go and in the sense that you know what other projects that you can talk about are you guys
[1476.62 --> 1483.34]  using internally that maybe you didn't expect to see uh kind of go work for well i don't know uh so probably
[1484.30 --> 1489.66]  okay so first of all um to answer the question about usage i mean goes usage inside google is is
[1489.66 --> 1493.98]  substantial and growing all the time i mean understandably we have a colossal code base and
[1493.98 --> 1498.46]  it's not like we're going around rewriting it um but there's a lot of greenfield development being done
[1498.46 --> 1504.22]  in go um a lot of people are doing v2s of things in go um and it's it's really exciting to see all that work
[1504.22 --> 1511.34]  happening um but the growth is spectacular yeah it is we've we've got graphs and and you know they're nice to
[1511.34 --> 1514.46]  look at unfortunately you know it's all confidential so we can't share numbers or anything
[1514.46 --> 1521.90]  um but uh as far as surprises i mean it it sort of comes back to that original point of
[1521.90 --> 1525.82]  uh it originally being pitched as a systems language you know like rob and the team were
[1525.82 --> 1530.78]  thinking about the problems they were solving and how go might be applied to those um but then you
[1530.78 --> 1535.50]  know we have probably some of the surprising areas are like in our operations teams who built a lot of tools
[1535.50 --> 1541.82]  in python which was also one of google's canonical languages um when go came along they were like
[1541.82 --> 1549.74]  oh geez well this is way way nicer to write tools in because um the like static typing and the concurrency
[1549.74 --> 1557.10]  primitives um give them the right sort of palette of tools to write really reliable um software and so
[1557.10 --> 1562.14]  if you're writing a if you're in an ops team and you're writing a tool that reaches out to 10 000 servers and
[1562.14 --> 1568.54]  changes the configuration somewhere um i think go is a much better suited tool for that task than python
[1568.54 --> 1574.62]  and so we saw a lot of growth in that area very early on because these are really small tools um
[1574.62 --> 1579.34]  that have a narrow scope and easy to write in a short period of time so that i think that was a surprise
[1579.90 --> 1584.54]  one thing is happening lately which is gratifying although it doesn't help go directly
[1584.54 --> 1589.18]  is that a lot of the libraries particularly in other languages particularly c++ are being redesigned
[1589.18 --> 1594.86]  internally to be more like the go libraries that we wrote and i take that as being a vote of confidence
[1594.86 --> 1598.54]  in our approach if not you know for a language because because to be honest there are systems you
[1598.54 --> 1604.46]  you can't for one reason or another just replace with a go program you can't you know some things have uh
[1604.46 --> 1608.94]  you know too low latency requirements that the garbage like the language can't handle or there's just
[1608.94 --> 1614.86]  too much code that exists already in c++ or java and you can't just throw it away and start over but it's nice to
[1614.86 --> 1620.38]  see that the internally there's been a lot of influence on the environment from go even from
[1620.38 --> 1625.50]  people who are not using go itself and that's pretty pretty gratifying it's really worth saying
[1625.50 --> 1631.50]  that it's it's not just dissatisfaction with any particular language that drove go it was also
[1631.50 --> 1637.34]  dissatisfaction with the environment in which those languages existed and uh so we're talking about build
[1637.34 --> 1646.30]  systems the way code is organized and you know with something like c++ you you can't uh you can't do
[1646.30 --> 1652.54]  what we do in go which is uh go source code defines all the information that you need to know about its
[1652.54 --> 1658.46]  dependencies and so you don't need make files or google's equivalent of make files yeah you don't need
[1658.94 --> 1666.46]  all this kind of metadata to actually build projects um and so with go we demonstrated that that that could be
[1666.46 --> 1674.54]  done um but you simply can't do that in c++ or java or even python um and so uh you know internally
[1674.54 --> 1680.62]  at google if you write a go program you can run a program that generates the the make file for that
[1680.62 --> 1686.70]  for that go program and so you no longer as a go programmer at google need to worry about a whole section of
[1686.70 --> 1694.70]  of um google's development process and so we're sort of demonstrating that that the your programming
[1694.70 --> 1699.58]  environment your world as a program can be simpler with go and a lot of that is starting to catch on
[1699.58 --> 1706.30]  right the um standard google build system is an amazing piece of technology it lets you build 100
[1706.30 --> 1712.78]  million line c++ programs reasonably efficiently but it takes minutes uh and it involves you know a cloud
[1712.78 --> 1717.74]  build system with many many servers doing distributed builds and lots of caching of source code and object
[1717.74 --> 1724.86]  code it's incredibly sophisticated and large scale system um whereas uh go program of of scale can
[1724.86 --> 1729.26]  easily be built on a single computer you don't need any of that and i think that's an interesting sort of
[1730.30 --> 1735.58]  data point in this whole thing ironically in order to work inside the google code base go has to run in
[1735.58 --> 1740.46]  the distributed build system because everything else does too and so it's kind of weird but using go
[1740.46 --> 1747.66]  inside google 3 is much nicer than using c++ inside the google world but um you it's it's not as nice
[1747.66 --> 1752.46]  as it is using in isolation because you have to integrate it into this other build system which is
[1752.46 --> 1757.42]  designed for languages that don't provide the kind of support that go does for efficient compilation
[1757.42 --> 1762.38]  it's still pretty efficient but it's not the same level of smoothness ironically it can often be faster
[1762.38 --> 1767.18]  to just disable the distributed compilation part when building pure go stuff if you can get away with
[1767.18 --> 1771.74]  it although if you're using the libraries to work in the google code base you usually can't do that
[1772.46 --> 1776.30]  but still people are using go inside google a lot because it is just so much more productive
[1777.82 --> 1783.34]  can you talk about like what specific things inside google are i mean is are there anything that you can
[1783.34 --> 1789.02]  actually kind of say is using go that that we might know about now sure well a popular example is
[1789.02 --> 1794.94]  youtube um they have a project called vitess which is uh essentially a load balancing solution from my
[1794.94 --> 1801.10]  sql they're a really heavy my sql user and as you can imagine um youtube does a lot of a lot of
[1801.10 --> 1807.34]  database activity involved in running youtube um and sitting between uh youtube's users the front-end
[1807.34 --> 1815.98]  software and um the mysql databases is a cluster of this process called vitess um that basically shards
[1816.70 --> 1823.66]  and and directs mysql queries to the correct replicas and so on and that's an open source project
[1823.66 --> 1828.54]  that's why i can talk about it um but that handles some colossal amount of traffic at the moment and
[1828.54 --> 1835.26]  every youtube page you go to talks to this thing yeah and uh it's actually they were a pretty early
[1835.26 --> 1840.94]  user of go and because of their scale um they really pushed the go run time and we made a lot of
[1840.94 --> 1846.14]  improvements and um fixed a lot of issues early on as a result of their use i remember one change to
[1846.14 --> 1851.82]  the run time got their system to run eight times faster they were a really good user to have yeah
[1851.82 --> 1856.22]  and they probably weren't upset about that change either no but they needed it because they were
[1856.22 --> 1860.62]  they were having scaling issues and you know we had to deliver having a real customer like that is a
[1860.62 --> 1867.42]  very important part of developing a system like this another example is the download server dl.google.com
[1867.42 --> 1871.42]  which you you might not know about but it's the thing that does that delivers you know chrome
[1871.42 --> 1878.22]  binaries to your world um connects to eclipse does android sdk downloads stuff like that it actually
[1878.22 --> 1883.50]  handles a staggering amount of traffic um and it was a c plus plus binary that was quite well written
[1883.50 --> 1888.86]  very clean program written about five six years ago something like that maybe even more the very
[1888.86 --> 1894.70]  important program but um what happens in in any kind of large code base like this is uh you know
[1894.70 --> 1900.54]  developers move around projects code kind of rots because the development environment it runs in
[1900.54 --> 1906.94]  changes libraries it's connected to change and so over time in order to keep up with things mostly by
[1906.94 --> 1913.74]  uh sort of the process by which as brad fitzpatrick once said uh things turn to shit uh the code is no
[1913.74 --> 1919.82]  longer really capable of of handling its job anymore it just and and a rewrite was necessary none of the
[1919.82 --> 1926.46]  original authors were still involved in the project um and uh brad complained on internal main list that
[1926.46 --> 1932.30]  you know this thing is is not working very well uh well he was doing an apt get and it was waiting five
[1932.30 --> 1938.30]  minutes to receive the headers from the servers right and so he just literally volunteered i'll i'll
[1938.30 --> 1943.18]  help you guys rewrite it but you have to do it and go and after a couple of meetings they said okay we will and so
[1943.90 --> 1950.46]  brad uh joined the team for several months uh really a month was the core project they completely rewrote it to be
[1950.46 --> 1957.66]  completely like bit level feature compatible with the old binary except that it was all written in go it was cleaner smaller faster uh
[1957.66 --> 1963.34]  uh used less memory had much better latency characteristics and was much easier to maintain
[1963.34 --> 1968.94]  and also as a result of this rewrite um was able to be adapted much better to the current infrastructure
[1968.94 --> 1973.90]  and so it now is a very different serving model than it used to but that came after the rewrite this
[1973.90 --> 1979.74]  is a consequence of the rewrite rather than the reason for the rewrite um but uh that's a i mean again
[1979.74 --> 1984.38]  that's another server running inside google that that handles a staggering amount of traffic but is
[1984.38 --> 1990.30]  entirely go and uh the people on the team are are very very happy with the result yeah one really
[1990.30 --> 1994.22]  great thing about that particular he gave a talk about it actually yeah he gave a talk which you can
[1994.22 --> 2000.86]  find at talks.golang.org um at oscon this year um but one really nice thing about that project is that
[2000.86 --> 2012.38]  uh the the because brad is also the maintainer of goes http stack um that that server uses goes http stack
[2012.38 --> 2016.14]  so it's exactly the same thing that serves all that traffic is the same thing that you can use in your
[2016.14 --> 2023.26]  projects um written in go and a lot of the you know when when we deployed it and exposed it to this
[2023.26 --> 2030.14]  this large amount of traffic we were able to improve uh you know the the performance of the http stack
[2030.14 --> 2037.82]  and also um release uh an open source project called GrooveCache which um we just published a couple of weeks ago
[2037.82 --> 2045.18]  um and that that sort of is the the distributed caching system um for the download server um that
[2045.18 --> 2049.42]  now anybody can use in their go programs and it's actually you should check it out it's github.com
[2049.42 --> 2055.98]  slash golang slash group cache this yeah the standard library with go is extremely good for doing this
[2055.98 --> 2061.58]  kind of work and when when dl.google.com was announced as being now on go a lot of people said well what
[2061.58 --> 2066.06]  framework did you use for web development for this and the answer is well we just use the standard library
[2066.06 --> 2070.78]  um and a lot of people were surprised i think at that the idea that a language would come with an
[2070.78 --> 2076.94]  http server server in the library capable of handling this kind of throughput but it does it's probably
[2076.94 --> 2082.54]  one of the really nice things about go is is simply when it was created because a lot of the languages
[2082.54 --> 2086.70]  that are around today were written at least 10 years ago and their standard libraries were built at
[2086.70 --> 2092.54]  least 10 years ago and the world was actually quite a different place then um the idea of having a you know
[2092.54 --> 2098.70]  10 years ago when you deployed a web service you would put it uh behind apache you know by default
[2099.10 --> 2105.50]  that was just what you did as a web developer um but now it's totally commonplace to just deploy your
[2105.50 --> 2111.42]  own server that speaks http um and sort of go grew up in that world you know we have a json encoder
[2111.42 --> 2117.34]  decoder in the standard library you know that didn't even exist at the time that uh ruby or python were
[2117.34 --> 2122.46]  created and so we really go has the advantage of of being more contemporary in that sense yeah if you
[2122.46 --> 2127.82]  want to write a web server that like serves the directory tree just you know like a basic example
[2127.82 --> 2133.82]  it's about 10 lines of go code for the whole thing um because the library just has you know these rich
[2133.82 --> 2138.70]  kind of things also it's got really good crypto support built into the standard library so it can do tls and
[2139.26 --> 2144.78]  kind of cryptographic stuff which is again sort of more important now than was thought like 10 years ago
[2144.78 --> 2150.38]  so it's a it's a modern language as much it's not a modern language in the sense that it has every
[2150.38 --> 2154.94]  modern language feature you've ever heard of but it's a modern language in the sense that the language
[2154.94 --> 2160.22]  plus its libraries tend to be make it very easy to solve the kind of problems that modern development has
[2162.70 --> 2166.22]  a little bit earlier you said that you can kind of one of the goals was to be able to keep the whole
[2166.22 --> 2173.26]  language in your head um is it still that way now would you say oh yeah definitely it's a very small spec
[2173.26 --> 2179.02]  relatively speaking um it's about 50 pages when you print it out and a number of people have said
[2179.02 --> 2183.58]  they've enjoyed reading it because it's actually like easy to understand just as a document
[2185.18 --> 2189.26]  i usually where does document sorry go ahead i was just gonna say i usually say that you can become
[2189.26 --> 2194.06]  sort of productive and go in a weekend and you can become fully confident and go within a couple of
[2194.06 --> 2200.14]  months um it's there's really not a huge amount to learn um most of what you learn in the long tail
[2200.14 --> 2205.58]  is just idioms and small little tricks and things and the library yeah and the libraries yeah but but
[2205.58 --> 2212.38]  you can you can become proficient at reading any go code in a matter of weeks weeks yeah less
[2213.58 --> 2218.06]  depends on how quickly you like yeah there's a there's an online resource for learning the language to get
[2218.06 --> 2225.02]  you started at tour.golang.r t-o-u-r.golang.org which is an online system that lets you run go code right in
[2225.02 --> 2229.50]  the browser and go step by step through learning the basics of the language it's a really effective
[2229.50 --> 2235.90]  tool for for getting started gotcha so you said you're working on 1.2 right now is that right yes
[2236.46 --> 2242.54]  well we just so we just released 1.1.2 which is the okay it's not very it's not very exciting
[2242.54 --> 2247.26]  it's got bug fixes but it was yesterday so i've got to mention it oh nice so the the exciting release
[2247.26 --> 2252.14]  though from what i've gathered was the 1.1 release right that was a very very heavy performance increase
[2252.14 --> 2257.50]  is there yeah but i think the really important release was 1.0 um because uh if you look at if
[2257.50 --> 2263.98]  you go to trends.google.com and look look up golang um you can see this incredible growth that occurred
[2263.98 --> 2269.58]  right around the time 1.0 was released the point about 1.0 was at that point we committed to keeping
[2269.58 --> 2275.82]  programs uh compatible that as as we continue to develop even if we found mistakes we wish were
[2275.82 --> 2279.90]  different we were not going to break your code anymore um before then it was a very active process
[2279.90 --> 2284.06]  as we futzed around and tried to understand what the right things were to do but at 1.0 we said
[2284.06 --> 2289.02]  that's it the language is designed the libraries are designed they will continue to maybe grow but
[2289.02 --> 2294.70]  we're not going to break your programs anymore um and as a result uh people were much more willing to
[2294.70 --> 2300.46]  commit to using it because they're they're they didn't have to track a moving target um right and
[2300.46 --> 2305.82]  it had a huge increase in the growth of the system after that and that was a really really important
[2305.82 --> 2310.62]  step to take and the run-up to it was exciting because we do we basically made a huge list of
[2310.62 --> 2313.98]  all the things we didn't like and we went through them we argued about what we should fix and what
[2313.98 --> 2318.30]  we shouldn't fix and did a lot of interesting development work uh andrew and i gave a talk at
[2318.30 --> 2323.90]  i think it was oscon two years ago about um how this process worked it's actually kind of interesting
[2323.90 --> 2329.10]  development effort on its own um and so that was a big deal but then you're right 1.1 was it was a
[2329.10 --> 2333.74]  performance release we got enormous improvement particularly in the runtime a little bit in the compiler
[2333.74 --> 2341.02]  uh some benchmarks ran massively faster typical speed up i said was something like 30 to 40 percent
[2341.02 --> 2345.66]  for our ordinary program um and performance work continues it's getting better all the time
[2346.22 --> 2352.54]  um and uh we expect 1.2 will have at least modest performance improvements for some for some things
[2352.54 --> 2358.62]  yeah 1.2 will have at least something like 30 40 improvement for networking on windows
[2358.62 --> 2366.06]  um gotcha and there's actually surprising amount of people using windows and go yeah windows for us
[2366.06 --> 2370.86]  was a really good open source story because the entire windows development work was done in the
[2370.86 --> 2376.78]  open source community we uh are not windows developers we're not familiar with it and the open source
[2376.78 --> 2381.26]  community did all of the work to port go to windows and it has been it's been tremendous to watch
[2382.30 --> 2385.82]  and i think actually more people use it on windows anywhere else at this point the downloads are
[2385.82 --> 2390.22]  certainly really really high well i think interestingly go has a lot of usage in china
[2390.94 --> 2395.10]  and i think a lot of the people in china a lot of the windows users are based in china as well
[2396.22 --> 2401.74]  um and actually one of the main contributors who worked on yeah on windows for shangomar is
[2401.74 --> 2409.74]  is based in china as well um so i don't know much longer maybe i'd like to move here um yeah so the the
[2409.74 --> 2415.42]  1.1 release was a performance thing uh some some benchmarks are like 10x although that was pretty unusual
[2415.82 --> 2421.58]  um and then 1.2 a lot of the focus has been on tooling there's some interesting new tools coming out
[2422.38 --> 2427.74]  in one one of the things that makes go interesting from my point of view not necessarily for everyone's
[2428.14 --> 2435.66]  um is that the language comes with libraries that understand go programs so you can uh there's a parser
[2435.66 --> 2440.70]  there's a lexer there's a new type checker which has just appeared and it's possible to write really
[2440.70 --> 2446.38]  interesting programs that that do things to go programs on the fly um to you know rewrite the
[2446.38 --> 2452.38]  source code or analyze it study it different ways existing tools like the go formatter and go fix and
[2452.38 --> 2457.98]  go doc are written on top of that but there's a spate of new tools coming out um building on that stuff
[2457.98 --> 2461.74]  that are they're pretty interesting and a bunch of those will be part of the 1.2 distribution
[2463.58 --> 2468.46]  gotcha when do you think that 1.2 will come out around what time it's slated to be released on
[2468.46 --> 2473.90]  december 1st or is it november 1st it's december 1st and then feature freeze is beginning of september
[2473.90 --> 2479.74]  and then we soak it until december yeah i mean we may we may cut the release before then if it's
[2479.74 --> 2488.30]  stable enough um but uh so there was a there was a gap of a year or more 14 months between 1.0 and 1.1
[2488.86 --> 2493.58]  and we really wanted to want to close that gap so after 1.1 we announced the plan to do the next
[2493.58 --> 2501.26]  release in six months um and that's december 1st um and uh we really want to kind of even make that
[2501.26 --> 2505.66]  a bit shorter and have you know a sort of three month period of flurry development and then like
[2505.66 --> 2511.90]  a one month stabilization period um and then and then cut because uh go doesn't we don't do any branch
[2511.90 --> 2517.34]  development um we maintain a release branch which is you know at the moment that's 1.1.x
[2517.34 --> 2522.62]  um but we only apply like absolutely critical fixes to that branch um there's never any new features
[2522.62 --> 2527.42]  um and we're very conservative about what we release because we take the stability really seriously
[2527.42 --> 2535.02]  um but we sort of copped a bit of criticism for not having a development branch in a stable branch and
[2535.02 --> 2542.38]  uh pushing more stuff into the stable branch um but really you know in our experience is kind of uh
[2542.38 --> 2549.34]  uh if you have that kind of situation you end up with a lot of people uh just using the the the
[2550.86 --> 2555.34]  either one of the branches and the development one doesn't get enough attention or the stable branch
[2555.34 --> 2562.62]  just doesn't get used and so uh we kind of have this just single mainline development approach which
[2562.62 --> 2567.66]  means that uh cutting stable releases is of paramount importance we'd like to get to the point of doing
[2567.66 --> 2573.26]  three solid stable releases a year i mean it looks it looks like we're we're heading towards
[2573.26 --> 2578.70]  that we're gonna be the last release was very painful it took us about four months of stabilization
[2578.70 --> 2582.78]  because after we got all the features in there were so many there was just such dramatic changes
[2582.78 --> 2587.18]  to the runtime for performance that there were a lot of secure bugs that cropped up we also don't
[2587.18 --> 2592.14]  want to go through that again started doing started doing performance work way too close to when we
[2592.14 --> 2596.30]  wanted yeah because i was on vacation and it started when i wasn't around to yell don't do that
[2596.30 --> 2601.26]  so this this time it should be a lot smoother for us i don't think the users outside noticed any of
[2601.26 --> 2609.10]  this but for us it was pretty frantic gotcha so if you don't mind i'd like to kind of i picked some of
[2609.10 --> 2614.86]  the questions off of your faq and uh you know about around language specifics and design and i know we
[2614.86 --> 2618.62]  talked a little bit about it but i'd like to kind of get into a few of them and just kind of get some uh
[2618.62 --> 2624.70]  see what you guys your thoughts are on them um so that one of the ones that i that kind of jumped out
[2624.70 --> 2632.62]  to me was in the in the faq uh i saw you guys had written it says also uh sorry also although go
[2632.62 --> 2637.42]  has static types the language attempts to make types feel lighter weight than in typical object
[2637.42 --> 2642.14]  oriented languages can you kind of elaborate on that what do you mean by that um yeah there's a
[2642.14 --> 2649.74]  couple of things that are important there um you there's a feeling in the community from from
[2649.74 --> 2655.10]  python and ruby world that static types is a bad idea because they learned what static typing is
[2655.10 --> 2661.02]  from languages that did it badly like c and c plus plus and java where it feels like you're you're
[2661.02 --> 2664.22]  you're filling in some bureaucratic form every time you want to start writing a program
[2664.86 --> 2670.22]  um i had a bit of an epiphany about a year ago when i realized that in the last decade testing has become
[2670.22 --> 2675.98]  hugely recognized as a critical part of software development and ironically it wasn't all that big a deal
[2675.98 --> 2681.02]  until you know there were advocates for it but it didn't really catch on as an important feature
[2681.02 --> 2685.74]  until you know the last decade or so and the realization i had was that was for that was
[2685.74 --> 2691.66]  triggered by the dynamic languages community using tests to do their type checking for them that they'd
[2691.66 --> 2695.10]  write this dynamic languages and then write tests to make sure that the strings never turn into lists
[2695.10 --> 2700.22]  and vice versa and it's kind of backwards static checking gives you that right at compile time your
[2700.22 --> 2704.94]  program won't compile if you try to do that kind of thing and so that means that the testing can be
[2704.94 --> 2710.46]  functional rather than type checking and and that actually makes you have to write fewer tests but
[2710.46 --> 2716.22]  get just as good a coverage of your your test your your software so the problem with static type
[2716.22 --> 2721.18]  checking is that you want to make it not feel cumbersome you don't want to write you know public
[2721.18 --> 2727.74]  static final foo equals new foo dot foo of foo dot this foo dot that you want to just say what you mean
[2727.74 --> 2734.46]  and there's one way in which go does that is it has this notion of initialize with type so if i say
[2734.94 --> 2741.50]  uh x colon equals and then some expression that's a declaration of a variable called x
[2741.50 --> 2746.78]  which whose value comes from the initialized agent value but whose type is also statically determined
[2746.78 --> 2751.90]  by the type of that initialized value and so if you want to declare a new foo you just say foo
[2751.90 --> 2756.94]  colon equals new foo and you're done you've got you don't have to write foo four or five times on that
[2756.94 --> 2762.78]  line to get it to work it's a little thing but it has a huge effect on the horizontal width of your
[2762.78 --> 2767.90]  program and therefore how much you know how many keystrokes you know that kind of typing you have
[2767.90 --> 2772.54]  to do um it's a small thing but it makes a big deal another one is the use of interfaces we've
[2772.54 --> 2778.62]  talked about that a little bit but i think the most important one is that um java in particular and c
[2778.62 --> 2784.14]  plus plus as well were the dominant languages in the late 90s and the programmers who came out of
[2784.14 --> 2790.70]  the education then learned to design by constructing type hierarchies and i think that's a really
[2790.70 --> 2794.46]  interesting model for software development but i don't think it's a particularly productive one
[2795.18 --> 2801.26]  and go doesn't have a type hierarchy at all the the language the language's types are not constructed
[2801.26 --> 2807.90]  as being inherited from one another it's instead a totally flat space of types and it sounds like
[2807.90 --> 2812.54]  a crazy model but the the interface the way interfaces work makes that all work beautifully
[2813.34 --> 2818.86]  um it has very different feel you tend to write go programs based on what you want done rather than
[2819.42 --> 2822.70]  what the structure of the type system is for the problem you're trying to solve
[2823.18 --> 2828.86]  and so there's just a lot less structure to a program this has a big effect on software development
[2828.86 --> 2834.14]  because if you want to write a large job application the first thing you have to do is design the type
[2834.14 --> 2839.18]  hierarchy and then you start writing a bunch of code that's dependent on that hierarchy and if you
[2839.18 --> 2844.14]  find out a month into the project that the type hierarchy isn't right it's actually sort of too hard to
[2844.14 --> 2849.82]  change so you tend to just sort of work around it and and go that way um it's even more true in the
[2849.82 --> 2854.22]  long term you know six months or a year from now you may need to put a new feature in it doesn't fit
[2854.22 --> 2858.70]  because the type hierarchy isn't right so you you find a way to force it in that's very complicated
[2858.70 --> 2863.58]  it doesn't work very well um and i think that that's just an upside down way of programming i think
[2863.58 --> 2868.70]  it's much better to think about what the functionality is and and and develop your software that way and have
[2868.70 --> 2873.90]  the types fit into the design of the software rather than the other way around and go encourages
[2873.90 --> 2879.82]  that model and as a result although it's a very uh subjective thing i think that go program design
[2879.82 --> 2887.58]  is much more fluid than it is in these uh inheritance driven design systems i think yeah i'm sorry i was
[2887.58 --> 2891.98]  going to say the the interfaces that you that that was probably the one thing that jumped off the screen
[2891.98 --> 2898.14]  at me when i'm reading about go is the way that go handles interface is very unique um you know i you
[2898.14 --> 2901.10]  don't have to struggle through multiple inheritance you don't have to struggle through things that you
[2901.10 --> 2904.62]  know are very frustrating so it's that's one of the things i think that's probably so attractive
[2904.62 --> 2912.70]  to developers uh but i mean it doesn't seem like the way that go handles interfaces is like you know
[2913.26 --> 2919.90]  um it seems like almost like a duh like why aren't more languages doing that and and why do you think
[2919.90 --> 2924.22]  that there aren't more languages come out that that kind of find that middle ground of you know maybe
[2924.22 --> 2929.50]  not the type hierarchy that you're used to it but maybe not also just just all generics you know
[2929.50 --> 2933.34]  what do you think it is about go that you're one of the only that seems to do interfaces that way
[2933.90 --> 2940.62]  i think it's because of the people who designed it uh didn't think that that way of design made a lot
[2940.62 --> 2946.78]  of sense i think it's just a bias i mean i admit it's a bias but but there's also a kind of orthodoxy
[2946.78 --> 2952.06]  about object-oriented you know you must have inheritance you must have public and private you know there's
[2952.06 --> 2959.66]  a kind of idea about this is how oop is done um and go doesn't give you a lot of those tools
[2959.66 --> 2965.02]  because they just weren't seen as necessary um well actually not seen as necessary is wrong it was
[2965.02 --> 2970.78]  seen as harmful we thought it actually made program development harder and and that's why and what
[2970.78 --> 2976.22]  what mattered is in object-oriented programming to us is the idea of interfaces and i've said this many
[2976.22 --> 2981.90]  times i wrote the plan 9 kernel uh with a lot of help from ken and although it's entirely
[2981.90 --> 2987.90]  written in c it's an extremely heavily object-oriented system and in the strongest possible
[2987.90 --> 2993.26]  sense because every single computable thing in that kernel or on the network or distributed across
[2993.26 --> 2999.18]  the network implements exactly the same interface it has 14 methods and everything does those exact
[2999.18 --> 3004.30]  14 methods and that's that is where all the power of plan 9 comes from is that uniformity of interface
[3004.86 --> 3010.94]  and i think uh go not explicitly but you know it's not a coincidence takes exactly the same
[3010.94 --> 3016.22]  approach the way interfaces work what matters is not how something does or who its parent is or who
[3016.22 --> 3021.42]  its children are but what it actually does and the way you say what something does is you write down
[3021.42 --> 3027.10]  the methods that it implements and call that an interface gotcha i cut you off a minute ago
[3027.10 --> 3030.70]  andrew were you going to say something oh i can't remember now okay
[3030.70 --> 3037.42]  no problem i don't i can't say why people haven't done this i mean it's just that's not for me to say
[3037.82 --> 3043.50]  i hope that you know russ and i said long ago russ cox who joined the project a couple years after
[3043.50 --> 3049.18]  we started maybe less uh he said uh you know if go dies at least we've got the interface idea out
[3049.18 --> 3053.58]  there and people will start to pick up on it and i hope that's true i hope not that go die i'm glad to
[3053.58 --> 3057.66]  know that the interface stuff yeah i'm glad to know i'm not the only developer that that was like a huge
[3057.66 --> 3063.66]  sigh of relief for when i saw that that that just was very exciting to me um another thing that i
[3063.66 --> 3068.62]  noticed and i think we talk a lot about on the show actually about um it's kind of you know it's
[3068.62 --> 3073.18]  like an ongoing joke amongst a lot of developers and that's like or not joke but i don't know if it's a
[3073.18 --> 3077.90]  debate or not but people talk about exceptions for control flow and so we've talked about that with a
[3077.90 --> 3082.86]  few guests on the show and you know everyone generally has the same idea that that's a horrible idea
[3082.86 --> 3087.90]  but you guys kind of took it a step further and go doesn't have exceptions so can you talk about that
[3087.90 --> 3094.38]  a little bit well i guess it comes down to you know what what the word exception implies exceptional
[3094.38 --> 3101.74]  and i don't know about most people's programs but my programs error states is is often the common case
[3101.74 --> 3109.34]  you know you or 50 of the time or whatever i mean handling errors is what most programs spend a lot of time
[3109.34 --> 3117.66]  doing um and so i think uh i think nigel uh made a really nice point the other day is that there's
[3117.66 --> 3126.94]  this kind of continuum of four states um where on the one hand uh you favor uh wait so there's favoring
[3127.58 --> 3136.70]  uh weak error handling or robust error handling on one axis and then you have uh uh what is it uh
[3136.70 --> 3142.78]  uh i don't remember this conversation oh well but anyway i should i should anyway the point is that
[3142.78 --> 3147.98]  uh you can you can kind of be really brief in your error handling and kind of omit it entirely so
[3147.98 --> 3153.18]  python is very exception heavy it uses exception to indicate exceptions to indicate a lot of things
[3153.18 --> 3158.62]  and that's great if you just want to write a short script and do x y and z and just have it blow up if
[3158.62 --> 3166.38]  if x y and z doesn't happen correctly and so on the uh in that case you know uh that's really optimized
[3166.38 --> 3171.50]  for the small situation but then if you want to handle any of those potential error states you need
[3171.50 --> 3178.62]  to wrap almost everything that you do in a try catch block um and but in go there's only one way
[3178.62 --> 3183.90]  to handle those errors and that is just to to write an if statement and check an error return value
[3184.54 --> 3190.46]  um and so it means that in throughout go code you always see the error handling it's always right there
[3190.46 --> 3196.94]  it's never uh some invisible control flow that you get with exceptions i'd like to add to that in two
[3196.94 --> 3204.46]  ways first you know if exceptions crash your program and you you can't afford to have servers crashing
[3204.46 --> 3208.70]  it's fine to use exceptions on a page of code if you want to don't mind if the program doesn't work
[3208.70 --> 3212.30]  very well because you're just doing a simple little test but if you're running something in production
[3212.30 --> 3216.62]  you can't have these these stack unwinding things happening all the time it's very unsafe
[3216.62 --> 3221.58]  unpredictable and it's just it's just bad design and in fact internally uh google does not use
[3221.58 --> 3226.14]  exceptions in its c++ development we just think it's too they're too dangerous that's an interesting
[3226.14 --> 3232.14]  point on its own the other thing to say about error handling is touching on something andrew said
[3232.14 --> 3237.18]  errors are common they happen all the time i mean you get you you can't open a file oops you know
[3237.74 --> 3243.26]  i shouldn't panic when that happens i should instead just just do something with that result and so
[3243.26 --> 3249.90]  errors are such a uniform and common piece of computing that in go we just made them be a value
[3249.90 --> 3254.30]  an error is just a value in the language like an integer or a string it's a thing called an error
[3254.30 --> 3258.78]  and it's a computable value and the thing about the way error handling works in go is errors are just
[3258.78 --> 3263.02]  normal things they occur all the time and you have the entire programming language at your disposal
[3263.02 --> 3267.90]  to decide what to do with them you can put methods on them you can wrap them you can you can do ifs on them
[3267.90 --> 3272.14]  you can do for loops over them if you want whatever you pretty print them whatever it is you have the entire
[3272.14 --> 3276.70]  language there to compute with an error value because you need to you need you get an error you
[3276.70 --> 3281.42]  got to deal with it if errors are handled entirely by exceptions they're this mysterious background
[3281.42 --> 3286.46]  force that you don't get to compute with you have to use these special control values special i mean
[3286.46 --> 3291.66]  special control structures it inverts your program they look very strange on the page you can't just
[3291.66 --> 3295.26]  say here's an error i want to i want to think about this error for a minute write code about it
[3295.98 --> 3301.66]  so go is actually just just really puts a stake in the sand that says errors are ordinary they should be
[3301.66 --> 3307.26]  values you should compute with them and yeah you have to put if error checks every every once in a
[3307.26 --> 3311.90]  while but that's forces you to think about the errors when they happen rather than throw them up the
[3311.90 --> 3317.66]  chain and hope you don't crash and you know if you actually do like a comparison a direct comparison
[3317.66 --> 3323.26]  between you know a programming language that uses exceptions and go that actually handles all the
[3323.26 --> 3329.18]  errors in a robust way i don't think the verbosity argument really holds up no it doesn't i think it's
[3329.18 --> 3334.22]  if anything it's equivalent often i've seen go be shorter and much more comprehensible yeah yeah
[3335.02 --> 3339.90]  the multi return or the multi-value returns kind of is the crucial kind of linchpin to that working
[3339.90 --> 3345.74]  though what do you think absolutely i mean it's not not just for error handling i mean multi-value
[3345.74 --> 3355.42]  returns is extremely useful yeah that's the i i'm a fan as a rubyist i'm a fan of multi-value returns for
[3355.42 --> 3361.34]  sure sure um so i think we could we could talk about this like forever i mean i just love hearing
[3361.34 --> 3367.02]  you guys talk about go and and it's exciting and encouraging to me to to get started um what what
[3367.02 --> 3375.42]  would you say quickly what would you kind of say the future of go looks like i just think it's it's more
[3375.42 --> 3381.42]  go code in more places um the more people use go the more libraries people write the broader its
[3381.42 --> 3387.90]  potential use cases are um i don't think there are any real limits as to what go is useful for
[3387.90 --> 3393.10]  i think um you know where people may have reservations about garbage collection or so on
[3393.10 --> 3399.90]  and latency sensitive environments i think that all of these problems can be essentially solved um and
[3399.90 --> 3406.06]  i'd like to see go on more platforms um doing more things for more people i know that's an extremely
[3406.06 --> 3412.22]  broad and vague response but um the reality is is that goes a general purpose language and so
[3412.22 --> 3417.82]  the the vision of go as as goes future is correspondingly general yeah and i think it's
[3417.82 --> 3422.54]  happening um ken thompson and i are astronomy fans and we've written between us a fair bit of
[3422.54 --> 3427.26]  astronomical software and ken's been thinking about writing some again and i was looking around on the
[3427.26 --> 3431.98]  web and uh i found this package that written i think someone at either the harvard observatory or
[3431.98 --> 3436.94]  the smithsonian observatory had written this this suite of astronomical algorithms in go and it's
[3436.94 --> 3441.98]  beautiful code it's beautifully written beautifully documented really well thought out and i and it was
[3441.98 --> 3447.90]  really a you know very happy moment for me to realize here's the software that i actually want to use
[3447.90 --> 3451.90]  that's written in the world that we built and you know the open source community has given it back to
[3451.90 --> 3457.58]  me and i'm so happy that i can use this stuff to to build the thing i'm working on it's really it's really
[3457.58 --> 3463.34]  wonderful to see this happen but in in the near term i think uh the real place we're seeing a lot of
[3463.34 --> 3470.06]  growth with go usage is in the sort of devops communities i mean you one recent go project that's really
[3470.06 --> 3477.34]  exciting is called docker which is a software suite for managing um linux containers essentially so it's
[3477.34 --> 3485.90]  great for deploying and compartmentalizing uh processes running on servers um and i think the these uh
[3485.90 --> 3494.70]  kinds of systems deployment and uh infrastructure uh tooling is is a real growth area for go i think
[3494.70 --> 3501.42]  particularly goes concurrency stuff and it's um sort of closeness to the machine um make it really
[3501.42 --> 3505.74]  well suited to to doing this kind of stuff it's like you can write stuff so you can write the kind
[3505.74 --> 3510.14]  of tools that you would have written in c except most tools are actually fairly high level they just
[3510.14 --> 3514.14]  need to be able to make system calls and do things that c is particularly good at but i think go is
[3514.14 --> 3519.74]  really um making strong inroads into that kind of sphere yeah docker is an interesting case because
[3519.74 --> 3524.22]  it's it's catching on it's it seems to be getting a lot of attention people are really happy with it
[3524.22 --> 3528.30]  but it's all written in go and nobody talks about the fact it's written in go and that's great like
[3528.30 --> 3532.30]  yeah that's a that's great it's not just talking about as a thing not that oh this thing happens to
[3532.30 --> 3537.26]  where you can go it's a thing that's great on its own and i love that we actually had uh we had
[3537.26 --> 3541.34]  solomon on the show uh from dot cloud about two months ago and he was talking about docker
[3541.34 --> 3546.70]  and yeah he was able to basically i mean we we obviously talked a little bit about go but um
[3546.70 --> 3553.34]  you know he he he was just talking about the power of docker and you know just hearing about a a project
[3553.34 --> 3558.38]  that's being used as heavily as docker and in production in places that docker you know is being
[3558.38 --> 3564.22]  used and and the language itself was not a a problem and not something that you had to defend i think is
[3564.22 --> 3569.18]  a is a big uh milestone for the language i think those days are behind us we don't have to defend it anymore like that
[3569.18 --> 3577.10]  gotcha yeah so like i said i feel like maybe we could uh we could talk about this for hours but
[3577.10 --> 3581.74]  i think maybe that that is for our listeners that are kind of interested in it maybe that that means
[3581.74 --> 3585.82]  they need to go sit on some of these talks you guys talk about so much right you'll put some links
[3585.82 --> 3592.70]  on the web page with this right so they know where to go to see resources yep yeah so um yeah we will do
[3592.70 --> 3598.30]  you do you have any talks coming up that that you'd like to kind of talk about oh so coming up uh in
[3598.30 --> 3606.22]  april next year is go for con in denver colorado which is the the world's first pure go conference
[3606.22 --> 3613.98]  uh large-scale pure go conference um and uh rob and i will both be delivering keynotes there and uh
[3613.98 --> 3618.38]  they've just opened their call for papers and so there'll be a bunch of other go people involved in
[3618.38 --> 3621.82]  that and should be a lot of fun and it's organized entirely by the open source community
[3621.82 --> 3628.86]  which is fantastic with this it's great that's good yeah no i'm really excited about that awesome
[3629.26 --> 3636.78]  so for our listeners that are uh new to uh the show we do a thing every every show we ask kind
[3636.78 --> 3641.42]  of the same three questions at the end of the show um we'll go ahead and ask them now um andrew the
[3641.42 --> 3647.42]  first question is for you and it is for a call to arm so what in the community would you like to see
[3647.42 --> 3652.46]  kind of people contribute to or jump around to specifically to go i just want people to build
[3652.46 --> 3662.22]  more stuff um and the cooler it is the better i mean uh a lot of the the great work in uh go tools
[3662.22 --> 3666.38]  and libraries is driven by people scratching their own inches and that's just how it tends to work in
[3666.38 --> 3674.94]  the open source community um and yeah i just uh i think you know that the time to the time has come to
[3674.94 --> 3680.06]  really just just build and build and that's going to be go's greatest strength moving forward it's
[3680.06 --> 3686.94]  the community that's building things what about you rob anything to add to that i agree except i would
[3686.94 --> 3692.14]  also add that um they should be creative you know i mean go is a different language it's a different
[3692.14 --> 3696.62]  world it gives you a different way of thinking uh don't just build the same things you used to build
[3696.62 --> 3704.70]  you know have have fun be creative surprise us with the things you can do awesome so if you
[3704.70 --> 3710.46]  weren't working on go or specifically uh maybe even at google what would you guys see yourself doing
[3711.34 --> 3718.70]  um i personally if i wasn't at google or working on go um i'd like to be using go but specifically
[3718.70 --> 3724.70]  i'd probably be building music technology either software or hardware or preferably a combination of
[3724.70 --> 3730.46]  both um music's been a passion of mine for a long time it's always been something that's going along in
[3730.46 --> 3734.46]  the background but i think you know if the next thing comes along it will hopefully be in that sphere
[3736.46 --> 3741.26]  if i were working on go and presuming it didn't exist i would probably be doing what i used to do
[3741.26 --> 3748.06]  which was you know systems infrastructure stuff and c and c plus plus and being feeling unproductive and
[3748.06 --> 3755.50]  thinking about maybe trying to find a way to do better awesome and our last question is for a
[3755.50 --> 3759.58]  programming hero just somebody that has been influential in your life and andrew you're not
[3759.58 --> 3765.66]  allowed to say rob but if you want to give us a uh someone else well um you know i'm sort of surrounded
[3765.66 --> 3770.78]  by people who do heroic stuff all the time so it's kind of hard to choose one and so in thinking about
[3770.78 --> 3775.50]  it you know i i would probably go back to like one of my childhood inspirations as a programmer which is
[3775.50 --> 3783.02]  john carmack um you know playing his games and and seeing what was possible on those really low-end pcs
[3783.82 --> 3788.78]  um was incredibly inspiring and you know at that time i was doing graphics programming and
[3789.50 --> 3793.98]  seeing what he did just made me realize you know holy shit there's just so much more that you can do
[3793.98 --> 3798.86]  with with so little and you know even to this day he continues to push the state of the art so he's
[3798.86 --> 3803.66]  truly an extraordinary guy he's pretty cool yeah he helped you learn how to cut monsters heads off with
[3803.66 --> 3809.90]  chainsaws right when he was working on quake when we plan nine we exchanged the occasional late night
[3809.90 --> 3816.38]  email it was it was really fun to talk to him it was really good uh what about you rob um i have
[3816.38 --> 3820.78]  similar privileges there's lots of people i could mention i'd like to mention two people that you
[3820.78 --> 3827.02]  probably never heard of that you should know about uh one is my old boss doug mackleroy who was uh
[3827.02 --> 3831.42]  when i first got to the labs i i asked around you know who are the smart people here ken said well
[3831.42 --> 3835.98]  nobody's smarter than doug and he's right doug is an amazing guy he invented a couple of things you
[3835.98 --> 3843.02]  might have heard of uh pipes uh macro assemblers um but he also just had this brilliant way of thinking
[3843.02 --> 3848.06]  about stuff that i found really inspirational he was the he was the voice behind unix that never really
[3848.06 --> 3853.10]  appeared much in public and never wrote a lot that people saw although he wrote introductions without
[3853.10 --> 3857.98]  attribution to a lot of manuals and stuff but he had a huge effect on on the growth of unix and and
[3857.98 --> 3864.38]  his his people just love him and uh he's he's a retired professor now at dartmouth and you go
[3864.38 --> 3868.78]  there and you can find accolades from the students and so on the other person i'd like to mention
[3868.78 --> 3873.42]  somebody i didn't actually know very well i knew him a little bit but i think he was an amazing guy
[3873.42 --> 3879.66]  and he died a few years ago his name was david wheeler uh he was at manchester he worked on edsac later he
[3879.66 --> 3885.02]  was a cambridge student and was an advisor for some really important people um but when he was uh at
[3885.02 --> 3891.50]  manchester in 49 50 51 he and morris wilkes uh programmed up that thing um they invented
[3891.50 --> 3898.54]  subroutine libraries linkers assemblers and all kinds of other stuff uh and he pretty much invented
[3898.54 --> 3904.62]  computer science as far as i'm concerned he later had a an office in cambridge full of uh filing
[3904.62 --> 3909.10]  cabinets and students would come in and say oh i had this really great idea and here it is and and
[3909.10 --> 3913.02]  dave would say oh it is a really good idea and he'd go to his file cabinet open up and find you know
[3913.02 --> 3917.58]  handwritten notes from 1953 with the same idea but expanded in much more detail and
[3917.58 --> 3922.62]  theorems proven and stuff he was a really amazing guy and he he and morris wilkes came up with a book
[3922.62 --> 3928.30]  with entitled something like preparation of programs for a digital computer it's a bunch of early papers
[3928.30 --> 3934.14]  about the edsac and for those of you who have worked only in the web era it's really i think in your
[3934.14 --> 3939.50]  interest to go back and read how how clever some of the guys long before that really were david wheeler
[3939.50 --> 3945.26]  is an example of that yeah there was a quote in my when i went to college in one of my uh
[3945.26 --> 3949.34]  classrooms there was a quote from i think it was from david wheeler but it's it was something along
[3949.34 --> 3953.10]  the lines of you can solve every problem with another level of indirection yeah that's something
[3953.10 --> 3958.46]  like that yeah yeah i remember that that's good so that's awesome well thanks guys so much for coming
[3958.46 --> 3963.90]  on the show uh i mean the amount of time and effort you guys are putting into this i think is going to
[3963.90 --> 3969.42]  do wondrous things for developers all over the world um you know from china to the states you know
[3969.42 --> 3975.26]  or for people down in australia that say xyz and say uh that's something that you don't hear every
[3975.26 --> 3981.90]  day we should give shout outs to uh the swedes as well who seem to be really getting into go and i
[3981.90 --> 3986.46]  also like to give shout outs to the other members of the go team both internally and externally because
[3986.46 --> 3990.22]  this go would not be anything like what it is today without the incredible contributions of
[3990.22 --> 3995.02]  of people all around the world both inside google because the team is actually global
[3995.66 --> 3999.02]  even though it's small and also to the open source community who've been just so
[3999.58 --> 4004.30]  great at making things happen for us awesome that's it for today's show thanks so much guys
[4004.30 --> 4009.02]  for coming on it was a pleasure to chat with you guys and uh i look forward to the next time i see
[4009.02 --> 4012.54]  you guys maybe i can uh bump into y'all at a conference and pick your brains about what you
[4012.54 --> 4016.46]  guys are doing this is tremendous stuff so thanks so much for coming on with us today thanks
[4016.46 --> 4021.90]  for welcome come to gopher con
[4034.38 --> 4034.46]  you
