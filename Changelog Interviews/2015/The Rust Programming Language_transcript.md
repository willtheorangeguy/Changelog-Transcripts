[0.00 --> 16.16]  welcome back everyone this is the change log and i'm your host adam stachowiak this is episode 151
[16.16 --> 21.68]  and on today's show we're talking to steve klabnik and yehuda cats finally having a conversation
[21.68 --> 28.08]  about rust on this podcast lots of deep conversation around the underpinnings of this
[28.08 --> 33.58]  awesome new system language from mozilla research we have four awesome sponsors for today's show
[33.58 --> 39.64]  code ship app quality bundle top towel and digital ocean we'll tell you a bit more about
[39.64 --> 43.90]  app quality bundle and top towel as well as digital ocean later in the show but our friends
[43.90 --> 49.68]  at code ship released a brand new feature called parallel ci and they want to give it to you today
[49.68 --> 57.56]  absolutely for free a 14 day free trial to test out 20 test pipelines with parallel ci
[57.56 --> 62.78]  it's a brand new feature you can split your test commands into up to 10 test pipelines this lets you
[62.78 --> 67.98]  run your test suite in parallel and drastically reduce the time it takes to run your builds
[67.98 --> 74.38]  but with this special offer you're getting 20 test pipelines that's 20 times faster than you could have
[74.38 --> 79.62]  ever built your test suite before the integrate with github and bitbucket of course you can deploy
[79.62 --> 86.00]  to cloud services like heroku aws and many more again get started today for free absolutely for free
[86.00 --> 91.74]  or if you're upgrading use our offer code when you upgrade to a pain plan the changelog podcast is
[91.74 --> 98.06]  that code use it to get 20 off any plan you choose for three months head to codeship.com
[98.06 --> 100.78]  slash the changelog to get started and now on to the show
[100.78 --> 108.78]  all right we're back we got steve klapnik on the call yahuda caps on the call and the awesome
[108.78 --> 115.28]  infamous jared santo what's up guys excited to be here excited to talk some rust did you know you were
[115.28 --> 121.94]  infamous jared i just got infamous you just made me so so guys we've been wanting to talk about rust
[121.94 --> 127.46]  for so long steve i think we you were helping kind of coordinate the call way back maybe uh i want to
[127.46 --> 133.16]  say late last year sometime but it just wasn't good timing so today is sort of perfect timing because
[133.16 --> 140.42]  we're recording this on april 3rd 2015 and today is the day that you guys released 1.0 beta for for
[140.42 --> 145.02]  us so it's a it's a big day it's a good day right yeah it's it's been great so far not only has it been
[145.02 --> 149.32]  a long time in terms of getting a show about rust but i used to actually post new rust projects to
[149.32 --> 154.64]  the changelog like two years ago yeah so it's very very long time and i've just been so overwhelmed i
[154.64 --> 159.84]  haven't been doing that lately but we've picked up your slack a little bit we got a weekly email we
[159.84 --> 164.90]  ship out now called changelog weekly so we've we've been sprinkling rust in there as we can as we get a
[164.90 --> 172.24]  chance to so um you know how about you man how are you today i'm good i'm also uh sprinting head
[172.24 --> 178.66]  first with uh ember 2.0 so i'm sort of doing ember 2.0 and rust 1.0 at the same time which gives me
[178.66 --> 182.50]  less time than i would like for either and i'm really eager for both of those to be done so i can
[182.50 --> 189.32]  get back to a sane open source pace again yeah and i have json api 1.0 which is related to 1.0
[189.32 --> 194.90]  it's just a lot of stuff for us yeah yeah that kind of leads right into the opening for us which
[194.90 --> 200.88]  is that you're both core team members on many projects and i guess we can take it one at a time
[200.88 --> 206.70]  sort of introduce uh yourselves to to those who may not know you but also sort of what role you play
[206.70 --> 210.82]  in the rust project and then how that correlates to other projects you're working on so i guess
[210.82 --> 216.02]  uh you know pick who wants to go first i guess steve you can go first all right so i am tremendously bad
[216.02 --> 221.72]  at bios but hello i'm steve if you don't know uh what's up with me i used to do a lot of ruby work
[221.72 --> 228.26]  uh but then i found rust and have sort of transitioned to doing rust uh first of all full time for mozilla
[228.26 --> 234.10]  uh but also i did it as a hobby for like two years before that started um i'm in charge of documentation
[234.10 --> 239.84]  on the rust project and yeah it was made a part of the core team uh not only from having a large amount
[239.84 --> 243.98]  of contributions but also to like acknowledge that documentation is a really really important
[243.98 --> 248.18]  thing and we should like have someone involved in making decisions that affect documentation so
[248.18 --> 254.72]  yeah i've been doing open source for a while uh also like steve mostly in the ruby but also
[254.72 --> 259.88]  javascript space um i got involved in rust actually because a couple years ago uh the product that i work
[259.88 --> 265.20]  on at work needed something that was significantly more performant but also embeddable and i got involved
[265.20 --> 270.82]  in rust pretty much at the perfect time right after it stopped having an identity crisis the identity
[270.82 --> 276.06]  crisis was over but before much of the work had gotten done uh to make it the awesome language
[276.06 --> 283.36]  that is now and so mostly i got involved because i was a really big early user and um i'm glad rust
[283.36 --> 287.56]  uh involved me as a user it's something that i care a lot about in my open source projects is having
[287.56 --> 291.88]  people involved in the in the project that are part of the decision making process that are just
[291.88 --> 297.20]  there because they're heavy users um so i contribute a little bit but i'm more the voice of
[297.20 --> 304.00]  the practitioner um and and definitely the kind of usage that i use rust for is a little bit different
[304.00 --> 308.44]  than the kind of usage that is involved in like writing the standard library or the compiler or
[308.44 --> 313.22]  whatever one of the dangers of a bootstrap compiler is you make a programming language that's really
[313.22 --> 318.16]  good at making compilers so we wanted to make sure that we had a broader set of use cases than just
[318.16 --> 322.36]  building the rust compiler itself which is why servo is important but also the stuff that you is doing
[322.36 --> 329.20]  is very important no steve i'm interested uh i think i first came across rust back when you first
[329.20 --> 334.18]  published rust for rubyists um which i went back in time and checked that your i think your first
[334.18 --> 342.50]  commit on that was december 22nd 2012 so yep uh talk about an early adopter what was it about rust
[342.50 --> 348.64]  way back in the day that initially got you excited so in college most of my friends actually did
[348.64 --> 354.86]  operating systems phds eventually and uh we had started to work on an operating system at that time
[354.86 --> 359.20]  we knew that c and c plus plus had some problems and d was a really big thing so we actually worked
[359.20 --> 365.18]  on building an operating system back in d1 back in the college days and uh i sort of found the web and
[365.18 --> 369.72]  went into ruby and sort of left the system space but they kind of continued doing that and i'd always
[369.72 --> 373.22]  remembered that for later and i've always sort of had a love for low-level programming even though it's
[373.22 --> 377.74]  not what i've done in my work in the last couple years so i was at home visiting my parents for
[377.74 --> 382.70]  christmas and uh there's not a lot to do in the middle of nowhere where i'm from and so i was like
[382.70 --> 389.54]  cruising the internet and found this announcement about rust uh 0.5 being released and uh i was like
[389.54 --> 393.22]  oh this is systems programming language i haven't done that in forever like i would love to get into
[393.22 --> 399.82]  this let me check it out and i found that the tutorial while it explains what to do like after i
[399.82 --> 404.58]  read it i didn't know how to write a rust program like i read it all i sat down at an editor i was like
[404.58 --> 410.58]  i what do i do from here so i just got in the irc room and i started asking dumb questions like
[410.58 --> 414.94]  literally like how do you hello world and like things like that and then wrote them all out into
[414.94 --> 420.22]  what became rust for rubyists so that was sort of that christmas break um and i found the language
[420.22 --> 424.40]  really charming i found all the people that were involved really fantastic and so i just kind of
[424.40 --> 432.18]  stuck with it from there so rust is a mozilla project or mozilla research um and you work now at
[432.18 --> 438.00]  mozilla on it can you maybe speak on their behalf of like why rust what was the point what's the win
[438.00 --> 443.02]  for mozilla and what's the thrust of the project do you know about the pwn to own browser competition
[443.02 --> 447.72]  that happens yeah they don't last very long yeah they don't last very long but what's interesting
[447.72 --> 453.28]  is if you look at what the vulnerabilities are so uh this i'm not as familiar with this most recent
[453.28 --> 457.76]  one because i've been studying the last one a lot more but in the in the not the one that just
[457.76 --> 463.30]  ended but the one before that uh firefox had four remote code execution vulnerabilities and all of
[463.30 --> 470.22]  those were due to um errors like iterator invalidation and use after free and this kind of memory unsafety
[470.22 --> 477.92]  situation so mozilla with firefox and other projects writes a lot of c++ and they feel the pain of c++
[477.92 --> 485.44]  in many ways and so part of the uh the reason to fund rust development was to like figure out if they could
[485.44 --> 490.48]  write a good programming language that would make them be able to write web browsers that are safer
[490.48 --> 495.62]  but while not sacrificing performance so historically programming languages have sort of given you this
[495.62 --> 502.40]  trade-off of we give you maximum control but then you have to double check everything versus we don't give
[502.40 --> 507.92]  you much control but everything is safe by default uh and so rust is trying to break that dichotomy down
[507.92 --> 514.94]  and give you a language that gives you both things yeah so uh so i don't work for mozilla um you said
[514.94 --> 520.24]  rust is a mozilla project uh one thing i really like about the mozilla research team is how much
[520.24 --> 525.68]  they care about making projects they they work on at mozilla be real community projects and obviously
[525.68 --> 531.18]  that's pretty rough because uh if you have five full-time people working on something and then you
[531.18 --> 536.78]  have a community there's an actual tension between those things but uh i've i've really enjoyed how much
[536.78 --> 544.36]  the team there has has looked to diversify the group uh and increase the number of people involved
[544.36 --> 549.80]  who are not just people working at mozilla um obviously rust has a bunch of phds working on it
[549.80 --> 554.72]  um and that that ends up being important to solve the kinds of problems that steve was just talking about
[554.72 --> 561.78]  before rust uh existed the the whole story of what rust is was just an academic concept um and rust is
[561.78 --> 566.88]  really the first time that that it became put into use as a production language um so that that's
[566.88 --> 572.06]  important and does involve hiring some phds to do some research work but i've also really enjoyed how
[572.06 --> 578.38]  much the mozilla team and and the mozilla research organization has how much time they spent getting
[578.38 --> 583.24]  people who are not at mozilla being important members of the decision making process of governance and
[583.24 --> 588.60]  all that so you hit it when did you first come across it and how long did it take you between
[588.60 --> 593.20]  finding it you know hit your radar and being like wow i'm gonna build something with this
[593.20 --> 599.78]  yeah so i i knew dave herman from mozilla research he was a friend of mine and so i knew that the rust project
[599.78 --> 605.60]  existed conceptually um and like a lot of other people i was looking for an excuse to use rust but i never
[605.60 --> 610.70]  really had any good ones uh and the product that i was working on at work uh it's called skylight
[610.70 --> 617.24]  it's a production management it's a performance monitoring app for rails apps and so uh one of the things
[617.24 --> 620.86]  that we do is we just have a thing that runs inside your rails app collects data and sends it to
[620.86 --> 625.38]  our server so that's just something that that we have to write and so the first version of that like
[625.38 --> 630.68]  you would expect was written in ruby and that version would basically go and would monkey patch
[630.68 --> 635.54]  your stuff or use that to support notifications or whatever and then it would uh get the information
[635.54 --> 641.32]  sent to the server and pretty early on we discovered that we had some bad memory usage problems
[641.32 --> 645.92]  um this is something that a lot of our users reported we could impact especially pathological
[645.92 --> 652.60]  cases we could end up using 100 or 200 megabytes of memory but even you know 20 30 40 50 megabytes
[652.60 --> 658.06]  of memory is a lot of memory to ask someone to give up to monitor their application um so i was
[658.06 --> 663.18]  basically tasked with getting the memory management story under control so i went in there and i looked
[663.18 --> 669.06]  at the ruby application really evaluated it and i was able i made some good progress i was able to get
[669.06 --> 673.40]  the memory usage down i was able to fix some of the pathological cases but the process of doing that
[673.40 --> 677.16]  made me realize that i simply didn't have the control over the memory usage that i would need
[677.16 --> 682.50]  to keep this maintained and then every anytime anybody ever touched the rails app or sorry the
[682.50 --> 686.74]  ruby app there was a good chance that they would have significant regression because i had to do really
[686.74 --> 693.58]  black magic stuff to even get some modest improvements so uh carl at the time one of our
[693.58 --> 698.62]  co-founders had started to do an experiment to write uh the agent in c++ and he actually made some
[698.62 --> 703.76]  good progress but uh i personally don't trust my c++ code and i was extremely nervous about
[703.76 --> 708.62]  having us as a team maintain code that could in theory set fault in production right so it was
[708.62 --> 713.02]  fairly important to us if we're asking people to run code that that code not be able to explode
[713.02 --> 718.78]  um so i started uh poking around at rust and i basically yeah i said you know rust is still pretty
[718.78 --> 724.18]  new but i i'm pretty sure i can get a you know prototype of a small piece an mvp which is just the part
[724.18 --> 728.94]  that serialized and deserialized the data structures into protobufs and sent them to our server i think
[728.94 --> 734.00]  i can get that part done in you know a week or two and so i i said if i can get it done then we should
[734.00 --> 738.70]  make further progress so i spent a week or two and i was successful at doing that part um actually that
[738.70 --> 742.50]  the reason i did that part was that that part in ruby was one of the worst parts of the system it was
[742.50 --> 748.16]  the one that was most bad of memory and so pretty quickly we were able to take this uh fairly
[748.16 --> 754.00]  memory heavy thing in ruby rewrite it rust and ship the native binary to our users um the reason
[754.00 --> 758.06]  we that i was really interested in rust and the reason why carl was interested in c++ was that
[758.06 --> 764.54]  i had a lot of experience embedding javascript runtimes in ruby um both spider monkey and then later on v8
[764.54 --> 771.02]  i worked on those projects and embedding a gc inside of another gc is just asking for never-ending pain
[771.02 --> 776.96]  so having a language that we could use without any gc whatsoever and have it do quote-unquote manual
[776.96 --> 782.92]  memory management was very attractive so uh the tldr is i had a really big problem which was
[782.92 --> 788.24]  write this agent uh and have it use less memory and i was able even at that point to get up and
[788.24 --> 791.28]  running with something that worked and gave us value in a pretty short amount of time
[791.28 --> 796.74]  and and so something that was very very memory uh had good memory usage didn't have a gc
[796.74 --> 802.04]  was very fast and also that i could chip with very low risk of seg faults in a short period of time
[802.04 --> 808.48]  awesome so steve was excited you was excited anytime you guys are excited the rest of us tend to get a
[808.48 --> 816.92]  little bit excited uh let's maybe maybe a lot of it let's talk about the language um it's defining
[816.92 --> 821.86]  features and i'm going to kind of turn to steve since it's your job to like write the docs and to
[821.86 --> 827.48]  to explain it to us noobs and then you can just kind of hop in and help out uh wherever you think he
[827.48 --> 834.52]  needs it so rest defining feature is memory safety without garbage collection steve can can you unpack
[834.52 --> 840.26]  that for us sure so uh in the beginning there were programming languages that sort of let you do
[840.26 --> 844.60]  whatever you want right like assembly code uh we'll start from that level of distraction obviously you
[844.60 --> 849.00]  know this started even before that with machine code yada yada don't want to get in there but uh
[849.00 --> 855.06]  things like assembly uh and the languages that came right after it uh gave you this low level access
[855.06 --> 859.92]  to memory and the problem with giving you that low level access is that you can do bad things
[859.92 --> 863.94]  uh and this is because naturally a processor just does bad things right like when you teach a person
[863.94 --> 867.44]  programming one of the first things you learn is that computers are not smart they're actually
[867.44 --> 871.96]  stupid and they do exactly what you tell them to even if what you tell them to do is just terribly wrong
[871.96 --> 877.58]  one of the innovations that came along actually uh in originally in the list paper uh by john mccarthy
[877.58 --> 883.18]  was this idea of a garbage collector and uh so instead of you managing memory manually through pointers
[883.18 --> 887.74]  you would ask garbage collector for memory and it would give it to you and then you're done with it it would
[887.74 --> 892.90]  automatically figure out how to get rid of that memory so fast forward you know 50 years this is
[892.90 --> 897.80]  a very common thing most of us work in languages that are garbage collected but garbage collectors
[897.80 --> 902.84]  like all things in engineering have upsides and downsides and there are certain domains in which
[902.84 --> 907.72]  a garbage collector's downside is completely unacceptable and there's other domains in which a garbage
[907.72 --> 912.14]  collector's downsides might not be as good as their upsides even if it's still possibly usable
[912.14 --> 916.96]  so in those domains where it's absolutely impossible you pretty much need a language like
[916.96 --> 922.52]  in modern days c or c plus plus that do not have one built into the language um and so rust is trying
[922.52 --> 927.26]  to tackle that sort of space because when you're building a web browser you need a ton of performance
[927.26 --> 932.96]  people expect their css transitions to be really snappy and like javascript to operate very quickly and so
[932.96 --> 938.04]  performance you know really really matters a lot and so in that context a gc is not really an
[938.04 --> 942.76]  acceptable mountain of latency there's other ones too like for example uh if you're implementing a
[942.76 --> 947.00]  programming language and you want to write a garbage collector uh it's much nicer if you're not
[947.00 --> 951.32]  fighting with a host language as a garbage collector so you may want to use one or if you're writing a
[951.32 --> 957.32]  triple a game uh you know when you need to have 60 frames a second uh a gc pause is unacceptable
[957.32 --> 960.92]  there's just all sorts of domains where this kind of thing happens i mean i think you hear this case
[960.92 --> 966.82]  actually interesting so maybe let's talk about that for a moment yeah so our domain is just we're already
[966.82 --> 972.00]  we're embedding into a language that already has a garbage collector and cycles between two languages with a
[972.00 --> 977.96]  garbage collector uh pretty much cause leaks no matter how careful you are especially if both
[977.96 --> 983.94]  languages have closures so if you're writing in uh trying to embed javascript in ruby or go in ruby
[983.94 --> 990.02]  or interoperating between like java 8 and ruby the only way that that ends up working correctly is if
[990.02 --> 995.30]  both parts of the system are talking to the same memory management system um so if you're for example
[995.30 --> 1000.52]  jruby the correct solution is that jruby doesn't come with its own garbage collector jruby uses the host
[1000.52 --> 1004.32]  garbage collector that's one strategy that you can use and that works fine if you're embedding
[1004.32 --> 1009.28]  your language inside of another language right but in this case where ruby is the host language
[1009.28 --> 1013.18]  which means that we don't and we probably don't want the thing that we're embedding to use ruby's
[1013.18 --> 1019.38]  garbage collector right we're writing lower level code so the only real solution is to have the thing
[1019.38 --> 1023.16]  that we're embedding use the system's memory management the system's memory management is malloc
[1023.16 --> 1030.04]  right so that's the way to avoid causing uh conflicts but of course now if the only option
[1030.04 --> 1034.36]  that you have is malloc now you're writing extremely low level code that has the possibility of taking
[1034.36 --> 1041.28]  down the entire process with you so uh in my in my case we could have written in a modern dialect of c++
[1041.28 --> 1048.18]  which does a certain amount of work to make this plausible but i as a programmer i just don't trust
[1048.18 --> 1053.86]  myself to write code that never crashes and so i wasn't willing to write i wasn't willing to basically
[1053.86 --> 1058.18]  go to nasa levels of engineering just to write a thing that collected information from your reels app
[1058.18 --> 1063.42]  and i really wanted some uh to use a language that would that would give us guarantees about that stuff
[1063.42 --> 1068.82]  so we if rust didn't exist i think we would have had a deep struggle inside of the company because
[1068.82 --> 1073.74]  i think there was a strong pressure to use c++ because that would give us the guarantees that we
[1073.74 --> 1078.04]  needed in terms of performance but a bunch of the rest of us were like you know who's going to
[1078.04 --> 1081.24]  maintain that how are we going to make sure we don't crash who's going to take the support tickets
[1081.24 --> 1085.44]  from the guy that's complaining that we're segregating that process um and so rust was
[1085.44 --> 1089.50]  really came it came just at the right time for us because it allowed us to say we're going to be
[1089.50 --> 1092.68]  able to have low level control we're going to be able to use the systems memory management
[1092.68 --> 1098.04]  but we're also going to have a absolute confidence that the program we write doesn't take down the host
[1098.04 --> 1101.76]  with it and and we're not the only people that are writing programs with this problem pretty much
[1101.76 --> 1107.50]  any c extension in ruby has this kind of problem and i would imagine that over time more and more
[1107.50 --> 1112.52]  cases where people are using c effectively as a glue layer or as an embedding language more and
[1112.52 --> 1117.32]  more people will move to rust just as a strictly better c yeah and so that's like that's like the
[1117.32 --> 1122.00]  drawbacks of the gc angles it sort of leads right into that so memory safety without garbage
[1122.00 --> 1127.18]  collection means that we give you this degree of safety that you're not going to screw things up
[1127.18 --> 1133.02]  without needing to use the gc to do it so i think that's probably a good spot for us to pause and
[1133.02 --> 1137.58]  hear from a sponsor when we come back i want to hear exactly how it gives us this memory safety
[1137.58 --> 1141.14]  without garbage collection so let's uh let's pause we back in a sec
[1141.14 --> 1147.26]  i want to share a more personal note today with you about our awesome sponsor top towel
[1147.26 --> 1151.92]  you've heard us talk about top towel several times for long-time listeners you know that top towel
[1151.92 --> 1156.18]  has been supporting the show for the better part of a year to a year and a half now
[1156.18 --> 1161.84]  if you want to go to their website while i'm talking here it's t-o-p-t-a-l.com it's one of
[1161.84 --> 1166.96]  the best places to work as a freelance software developer we've been working with top towel like i
[1166.96 --> 1171.24]  said for about a year year and a half now and over this year and a half i've gotten to know
[1171.24 --> 1176.48]  their co-founder brendan very very well i love what they're doing for the software development
[1176.48 --> 1181.28]  community they care deeply about software developers having awesome engagements to work on
[1181.28 --> 1185.86]  and they also care about awesome engagements having really awesome software engineers to work
[1185.86 --> 1189.98]  with them so they really make the marriage between a business with great opportunities
[1189.98 --> 1195.38]  and an engineer needing great opportunities to work on they make that marriage possible
[1195.38 --> 1200.38]  well we took our relationship to the next level and went there ourselves we're building something
[1200.38 --> 1204.98]  very cool behind the scenes here to change law to power the future of what we're becoming you're
[1204.98 --> 1209.06]  going to love what we're doing we hired a software engineer through top towel his name's
[1209.06 --> 1213.66]  so if you're a member and you're in the members of the slack room say hi to hafail he's in there
[1213.66 --> 1219.18]  but i wanted to tell you just how deeply we care about our relationship with top towel and how much we
[1219.18 --> 1224.24]  trust who they are and if you're freelancing right now as a software developer and you're looking for a
[1224.24 --> 1229.64]  way to work with top clients maybe even us on projects that are interesting to you challenging
[1229.64 --> 1236.14]  and using the technologies you want to use i will go as far to say that top towel is the place for you
[1236.14 --> 1243.94]  head to top towel.com slash developers that's top towel.com slash developers learn more and tell
[1243.94 --> 1249.72]  them the change law sent you all right steve and you know we're talking memory safety without garbage
[1249.72 --> 1255.60]  collection sounds like rust has that as a defining feature um you said it has it but like how does it
[1255.60 --> 1259.98]  actually work can i i'll just jump in and say one thing and then let steve answer it in more detail
[1259.98 --> 1264.42]  which is what i wrote a blog post about this called uh rust means never having to close the socket
[1264.42 --> 1269.22]  which i would recommend people read to get more details about this stuff beyond what we'll talk
[1269.22 --> 1274.72]  about here but one thing that was pretty uh like a pretty big aha for me when i started writing rust
[1274.72 --> 1280.48]  is that garbage collection is actually pretty awesome at managing the resource called memory so garbage
[1280.48 --> 1285.86]  collection is able to say when i create a new you know if i create 5k memory and i no longer need it
[1285.86 --> 1291.38]  it will get cleaned up but garbage collection is actually very bad at closing resources like files
[1291.38 --> 1297.98]  locks and things like this and uh if you if you ever wrote c++ which it turns out most people who
[1297.98 --> 1303.58]  wrote write ruby didn't there's actually a pretty nice system in in c++ and other language and a bunch
[1303.58 --> 1309.32]  of other languages which basically will uh automatically manage resources in the same way that memory is
[1309.32 --> 1315.20]  managed uh unfortunately in c++ that comes at the cost of of a lack of safety which basically makes it a
[1315.20 --> 1321.28]  non-starter for uh for people who are trying to write safe line writing safe language but the i didn't
[1321.28 --> 1325.34]  really occur to me before that while i had this awesome strategy for dealing with memory management
[1325.34 --> 1329.60]  basically i just you know i just did something that new i got a new thing and when i was done with it
[1329.60 --> 1334.16]  got cleaned up but if i started to use a file or if i started to use a lock i suddenly had to do
[1334.16 --> 1339.70]  all this manual work to make sure it got cleaned up and if i if i use a socket outside of the area where i was
[1339.70 --> 1343.96]  allowed to use it just like if i tried to use memory outside the area i'm allowed to use it in c or c++
[1343.96 --> 1348.26]  i would get weird errors and it just didn't occur to me that one of the trade-offs for having a
[1348.26 --> 1351.70]  garbage collector which is very good at managing memory is that suddenly i have to do all this
[1351.70 --> 1358.44]  manual work to manage sockets and other kinds of resources files and things like that so uh steve
[1358.44 --> 1364.68]  can answer the original question uh yeah that was a good detour though so it's it's important while
[1364.68 --> 1368.96]  we're sort of characterizing c++ is this like completely no holds barred oh my god what's going to
[1368.96 --> 1373.36]  happen zone obviously these are problems that c++ programmers have to deal with right
[1373.36 --> 1378.78]  so they have this solution and some terminology they've come up with um that we sort of have gone
[1378.78 --> 1383.38]  back and forth on the actual usefulness of but i guess what i will i'll approach the problem in this
[1383.38 --> 1389.02]  way so when you in when you make a new variable uh and again we'll stick to memory even though as you
[1389.02 --> 1393.08]  had mentioned this is applicable to everything not just memory um in some ways the non-memory stuff is
[1393.08 --> 1398.18]  cooler but whatever you gotta start somewhere when you say like i want a variable uh that variable
[1398.18 --> 1403.10]  lives for a certain amount of scope right so it's valid from where you declare the variable until
[1403.10 --> 1408.06]  that variable goes out of scope and at that point is when you either if you're in a manual
[1408.06 --> 1411.94]  situation you have to clean it up yourself or if you're in a garbage collector it will detect that
[1411.94 --> 1417.36]  like it's dropped out of scope and then uh clean up the memory um and so this is called by c
[1417.36 --> 1422.22]  and c++ programmers um a lifetime so the amount of time which is sort of weird because it's really
[1422.22 --> 1428.04]  based on lexical scoping generally speaking that a variable is like valid so a lot of the most
[1428.04 --> 1433.44]  pernicious problems happen in c and c++ where you have a pointer to some sort of thing and then the
[1433.44 --> 1437.80]  thing you're pointing to goes out of scope and therefore the memory is freed and now you have
[1437.80 --> 1444.52]  point a pointer to invalid memory so what rust actually does is it basically understands both the
[1444.52 --> 1450.26]  scope that variables go into and out of and what things are pointers to those things and it's able to
[1450.26 --> 1455.66]  at compile time tell you oh hey that variable is going to go to scope and therefore this pointer
[1455.66 --> 1461.28]  would be invalid so this is going to be an error um and we call that this system of ownership and
[1461.28 --> 1465.76]  borrowing which is sort of formalizes these semantics but that's sort of the basic idea is that
[1465.76 --> 1471.12]  rust is able to statically determine uh how what stuff is in scope and what stuff is out of scope
[1471.12 --> 1478.82]  it's doing it all at compile time correct yes so there there are some things uh there are some more
[1478.82 --> 1482.58]  advanced things you can do to like make those checks be at runtime but the core of the system
[1482.58 --> 1488.02]  is an entirely compiled time check that is no runtime overhead whatsoever so you get the exact
[1488.02 --> 1493.64]  same assembly code as if you had written correct c but you don't you get the compiler checks to make
[1493.64 --> 1498.52]  sure that you're doing the right thing and one thing that was pretty mind-blowing to me uh well one
[1498.52 --> 1502.80]  thing that was pretty mind-blowing to me so i you know i write ruby code and javascript code and i'm used
[1502.80 --> 1507.48]  to like closures all over the place and pointers all over the place and however many references that you
[1507.48 --> 1511.40]  could possibly want pointing to the same thing and aliasing and all this stuff i was used to all
[1511.40 --> 1516.48]  that stuff so i when i first started writing rust and i learned that the basic model of rust is that
[1516.48 --> 1522.48]  some some pointer only has one owner at a time and if i want to give it to somebody else i have to give
[1522.48 --> 1527.06]  it to someone else and stop using it or i can lend it to somebody else for a fixed period of time and
[1527.06 --> 1530.32]  then they can't hold on to afterwards i thought that this would be extremely restrictive i thought that
[1530.32 --> 1534.52]  it would be very very difficult to program in this way and in fact that's effectively what the
[1534.52 --> 1539.36]  academics who came up with this idea thought they thought uh this is like a cool idea but it's
[1539.36 --> 1544.86]  extremely restrictive it'd be very hard to program in it um and one of the things that i i have found
[1544.86 --> 1549.72]  as i've written a lot of rust code now is that a shocking amount of the code that you already write
[1549.72 --> 1554.64]  including code with closures including code with you know pointers structures that you put stuff
[1554.64 --> 1560.50]  stuff into and all this stuff actually can be described in terms of ownership and borrowing and that
[1560.50 --> 1564.68]  when you start thinking about things in terms of ownership and borrowing the structure of your code
[1564.68 --> 1569.68]  becomes a lot clearer right so um one thing that you may have been able to suss out from what we said
[1569.68 --> 1575.58]  is that it's almost impossible in rust it is impossible in rust effectively to cause a traditional
[1575.58 --> 1580.62]  kind of memory leak because traditional kinds of memory leaks are caused by let's say i have a reference
[1580.62 --> 1585.18]  to something and you have a reference to it i don't know when i'm i can clean it up and you don't know
[1585.18 --> 1590.52]  when you can clean it up so from a local perspective nobody knows when the right time to clean something
[1590.52 --> 1596.06]  up is and and you can get into situations where nobody nobody is correctly freeing the memory and so
[1596.06 --> 1600.10]  you just get a leak and this can happen even in a garbage collected language with complicated enough
[1600.10 --> 1605.30]  situations but in rust there's never a situation where two of us think that we own the pointer right
[1605.30 --> 1609.60]  i either i own the pointer and i let you borrow it or you own the pointer and you let me borrow it
[1609.60 --> 1615.48]  but only one of us is responsible for cleaning it up and in rust neither of us actually has to do the
[1615.48 --> 1621.14]  manual cleaning up it's just an automatic uh it's an automatic reflection of these rules right so
[1621.14 --> 1625.44]  whoever owns the pointer is responsible for cleaning it up and the compiler will do that cleaning up
[1625.44 --> 1631.94]  automatically for you so i was just i was just amazed after i i wrote uh you know 10 or 20 000 lines
[1631.94 --> 1636.86]  of rust code including the big complicated program which is cargo and the pretty complicated program
[1636.86 --> 1642.72]  which is skylight at how infrequently it turned out that i wanted to go use something that let me
[1642.72 --> 1647.74]  get more dynamic rules like how often the static set of rules work perfectly for what i needed
[1647.74 --> 1656.86]  so you have ownership and only the thing that owns a piece of memory can write to it or read to it or
[1656.86 --> 1662.54]  both uh so that that's actually see if you can go ahead so the the it's actually a little bit
[1662.54 --> 1668.20]  different than that the the owner is the person who is responsible for deallocating that resource
[1668.20 --> 1675.12]  so like whenever they're finished with it they get rid of it uh they have like they have like 777
[1675.12 --> 1680.40]  permissions on it right like they have root permissions for that for that object they can do
[1680.40 --> 1685.56]  whatever thing they want to do um to it and once they're finished they're responsible for doing the
[1685.56 --> 1689.96]  cleanup and in this case rust inserts that cleanup code for you um but that's like when you say the
[1689.96 --> 1694.70]  when you say the person do you mean like the variable or the thread or the variable sorry
[1694.70 --> 1700.32]  yeah this is a discussion that's hard to have over words it's like oh it makes it a lot yeah it is
[1700.32 --> 1704.38]  the way i think about is that the scope that created it so when you make a variable you you by
[1704.38 --> 1709.82]  definition have to create it inside of some scope in code right that scope in code is the thing that's
[1709.82 --> 1714.54]  responsible for cleaning it up so if you make a variable and then don't do anything else with that
[1714.54 --> 1719.84]  variable and then the scope of code that you created in uh is finished that variable will get
[1719.84 --> 1725.30]  cleaned up um but you are allowed since you created it to give it to somebody else and if you give it
[1725.30 --> 1730.02]  to someone else the same rule applies right it will uh it gets cleaned up when their scope of code is
[1730.02 --> 1736.00]  left and this turns it's a recursive concept so it's sort of hard to see uh how effective it is but
[1736.00 --> 1740.62]  basically what that ends up meaning is that if you look at any piece of code you can tell by looking
[1740.62 --> 1746.76]  at it whether or not exactly which things that came into it will be cleaned up when you leave it
[1746.76 --> 1750.68]  because either you didn't give it to somebody else or you did right those are the only options either
[1750.68 --> 1753.98]  you gave it you transfer ownership to somebody else or you didn't transfer ownership to somebody else
[1753.98 --> 1759.68]  and that's true at every local point every local scope in the program so what's the process of
[1759.68 --> 1764.02]  transferring ownership like what's the semantics around that so transferring ownership actually is
[1764.02 --> 1768.30]  pretty cool yeah it's just the default way that you give something to something else in rust so if i
[1768.30 --> 1773.68]  write a function that says this is a function that takes like a string let's say and i call that
[1773.68 --> 1779.18]  function with a string that is me transferring ownership and there's also uh the ampersand operator
[1779.18 --> 1786.04]  in rust which is uh the reference how references are referred to in c or c plus plus if you use that
[1786.04 --> 1791.74]  then you're lending it so uh effectively the story the transferring ownership is not like
[1791.74 --> 1797.06]  like a complicated api like a channel or something like that transferring ownership is just done by
[1797.06 --> 1802.40]  calling a function that tries to take ownership and the way you take ownership is that you take uh
[1802.40 --> 1807.90]  you take a value without the ampersand and if you take a value with the ampersand then you uh
[1807.90 --> 1811.68]  you're basically just promising that you won't hang on to it after the point at which you return
[1811.68 --> 1817.76]  right so so uh borrowing is kind of like borrowing with real things right so you uh if i transfer
[1817.76 --> 1821.22]  ownership i'm saying hey you have access to it now and you can do whatever you want and i don't care
[1821.22 --> 1825.66]  anymore lending is saying hey you i'm lending you this thing but you got to give it back to me when you
[1825.66 --> 1829.60]  return you can't hang on to it later like in a closure or something like that there are also
[1829.60 --> 1834.72]  mutability and immutability rules to make sure that there's no concurrency issues there too um just
[1834.72 --> 1840.08]  to like mention that that's part of it as well yeah so mutability is actually interesting because
[1840.08 --> 1845.26]  mutability and rust is actually a different concept to this and the whole mutability question is just
[1845.26 --> 1852.00]  the concept of uniqueness which is that only one thing can mutate something at a time so uh if if i
[1852.00 --> 1855.92]  give you access to something to mutate and i also give steve access to something to mutate
[1855.92 --> 1860.28]  that's bad that means that you guys can write on top of each other and can't have any expectations
[1860.28 --> 1865.00]  about what could happen you could crash right but i can give you access to something to mutate and then
[1865.00 --> 1870.14]  later on give it to steve to read or i can give all of you a copy of a thing to read and that's fine
[1870.14 --> 1875.06]  right i just can't give i can't give somebody access to something to write and anybody else access
[1875.06 --> 1880.56]  to write or read at the same time and that's also totally static a compiler figures out whether you're
[1880.56 --> 1886.40]  doing that or not and yells at you if you're doing the wrong thing so this probably this probably lends
[1886.40 --> 1892.22]  itself pretty well into the concurrency story steve could you talk about that yeah so uh rust actually
[1892.22 --> 1897.36]  has a bunch of really interesting and unique concurrency uh things just about it in general so
[1897.36 --> 1902.96]  the first one is that um the question that's on everybody's mind with regards to concurrency
[1902.96 --> 1906.92]  today is like what's your threading story do you have channels and that kind of thing
[1906.92 --> 1913.46]  so what i mentioned is that uh originally well i shouldn't uh i'll do it that way fine it's like
[1913.46 --> 1916.82]  you can always pick the way to tell the story right so i'll give you a little bit of history
[1916.82 --> 1923.56]  rust used to have both one-to-one and end-to-m threading built in and the problem with that is
[1923.56 --> 1927.94]  that the abstraction layer that let you choose like you could basically say in your rust program
[1927.94 --> 1931.86]  this rust program will use one-to-one threading or this one will use end-to-m threading and it was an
[1931.86 --> 1936.50]  abstraction so you just you would just pick so then that overhead meant that green threads were not
[1936.50 --> 1941.12]  actually like significantly more lightweight than regular threads and since rust is a systems
[1941.12 --> 1945.50]  programming language you need to have access to systems threads but like end-to-m threading is a
[1945.50 --> 1952.62]  runtime kind of issue so we made the decision to switch to just one-to-one threading so by in rust right as
[1952.62 --> 1957.76]  of right now by default it's just got one-to-one threading built in now there's a whole bunch of like
[1957.76 --> 1962.34]  discussion you get into around that for example like on linux threads spawn a lot faster than you may
[1962.34 --> 1967.00]  have expected in the past and so like it's not that end-to-m is inherently superior or inferior
[1967.00 --> 1970.76]  to one-to-one but we just got one-to-one right now you can actually write end-to-m threading as a
[1970.76 --> 1975.58]  library because rust is a low enough level programming language that io is a library concern not really a
[1975.58 --> 1982.16]  language concern so um there's several people including uh one of the people at um tilde who's
[1982.16 --> 1989.18]  like writing alternate io libraries that give you other concurrency models etc um but what's important
[1989.18 --> 1994.16]  about rust concurrency is is that we have certain types built into the type system that have certain
[1994.16 --> 1999.52]  concurrency properties and the standard library uses those to ensure correctness which means that
[1999.52 --> 2004.60]  if you write an alternate io library you can also gain the same level of safety with your concurrency
[2004.60 --> 2010.14]  that we do built into the language so for example rust has a channel abstraction that's entirely written
[2010.14 --> 2014.48]  in library code and you can use channels if you'd like those channels are great but if for some reason
[2014.48 --> 2019.48]  you don't like the way that we implemented channels so like our channels are uh multi-producer single
[2019.48 --> 2023.98]  consumer channels if you wanted multi-producer multi-consumer channels you would need to write
[2023.98 --> 2028.80]  your own but because the channel is a library type and not built into the language you could get the same
[2028.80 --> 2034.68]  safety guarantees around them uh that we have which is really really cool and the latest example of
[2034.68 --> 2039.86]  something that we did uh is you can actually i've been meaning to write a blog post about this i don't have a
[2039.86 --> 2044.34]  good link for more explanation but at some point i'll have something for you you can actually uh do
[2044.34 --> 2050.36]  mutable concurrency over stack allocated data and prove that it's safe and not have uh race conditions
[2050.36 --> 2055.52]  in it which is well data races um which is super impressive and really hard to explain without code
[2055.52 --> 2060.86]  so i'll just like drop that as a thing uh i have like we have like very strong very good safety
[2060.86 --> 2064.66]  guarantees around concurrency that are really fantastic i'm sure you've got more to say yeah
[2064.66 --> 2070.70]  ultimately the the ownership story is basically exactly what you want for for data right so i typically
[2070.70 --> 2074.32]  i mean everyone knows that shared mutable state is the root of all evil when it comes to
[2074.32 --> 2080.24]  concurrency and a lot of languages try to solve that by restricting your ability to have
[2080.24 --> 2086.62]  shared state or mutable state and ross basically says shared mutable state is indeed bad but shared
[2086.62 --> 2092.44]  state is fast and also often very intuitive so what we're going to do is we're going to prevent we're
[2092.44 --> 2096.76]  going to use the ownership system to stop you from sharing and mutating at the same time right so
[2096.76 --> 2100.78]  the ownership system with the same ownership system that you already learned for doing single
[2100.78 --> 2108.04]  threaded programs is also perfect for multi-threaded programs uh so if as long you can uh as steve
[2108.04 --> 2114.14]  sort of alluded to you can write a program that uh you know does a fork join model and as long as
[2114.14 --> 2121.12]  all 10 of those things that are uh all 10 of the things that are forked that are forking uh only read
[2121.12 --> 2126.28]  the data that's totally safe and the rust ownership system knows how to uh think about that um and if you
[2126.28 --> 2131.36]  want to uh have a fork join system where you have 10 things that are each mutating something as long
[2131.36 --> 2136.70]  as you don't give them the same thing to mutate that's also fine right and so basically what rust
[2136.70 --> 2143.08]  said what rust sort of the innovation of rust is that rust has this really uh robust ownership story
[2143.08 --> 2147.54]  um ownership and borrowing and ownership and borrowing is pretty awesome for reasoning about
[2147.54 --> 2151.88]  things it's awesome for performance it's awesome for letting you allocate things in the right place
[2151.88 --> 2155.84]  either the heap or the stack whatever's appropriate but it's also really awesome for letting you do
[2155.84 --> 2159.94]  things on a lot of different threads and not have to worry that those that those different threads are
[2159.94 --> 2164.22]  going to be stomping all over each other because things have things only own the things that they
[2164.22 --> 2168.56]  they should own right and rust already guarantees that you only have a unique owner one unique owner
[2168.56 --> 2173.84]  per thing so that's that's basically perfect and the awesome thing is that this ownership system is not
[2173.84 --> 2179.24]  um it's not a dynamic thing so like in javascript for example there's also an ownership system
[2179.24 --> 2184.28]  and you can pass things to another thread uh and the other thread can do something with it and pass
[2184.28 --> 2188.68]  it back um but in javascript every single time you pass something around you have to do all these
[2188.68 --> 2194.28]  dynamic checks and that means that there's a lot of a lot of extra overhead to enforcing a pretty good
[2194.28 --> 2200.08]  a pretty good rule right um and in rust because of the fact that the ownership system is entirely static
[2200.08 --> 2205.72]  the actual cost is no different than doing shared memory concurrency in c or c plus plus but you have
[2205.72 --> 2211.62]  guarantees about what can happen because of because of the underlying model so i think the tldr is just
[2211.62 --> 2216.10]  when you start learning rust like the ownership system feels pretty daunting but it turns out that
[2216.10 --> 2220.32]  it's effectively one concept that you have to learn and then it unlocks all these superpowers that let
[2220.32 --> 2225.82]  you write really fast and complicated code safely it's also really just generally like you know
[2225.82 --> 2231.38]  everyone's terrified of writing concurrent code because it's very difficult uh and rust makes many
[2231.38 --> 2236.34]  concurrency errors be compile time errors which is just mind-blowing the first couple times that you
[2236.34 --> 2242.96]  see it for sure well let's take a break here we'll hear from another sponsor and then we get back i'm
[2242.96 --> 2247.66]  gonna give you guys a chance to think during the sponsor break uh what's your favorite feature besides
[2247.66 --> 2251.98]  ownership and all that it implies we'll have each of you a chance to answer that question when we get
[2251.98 --> 2260.28]  over 400 000 developers have deployed digital oceans cloud digital ocean is simple cloud hosting built
[2260.28 --> 2266.02]  for developers in 55 seconds you'll have full root access to a cloud server and it just doesn't get
[2266.02 --> 2270.96]  any easier than that pricing plans start out affordably at five dollars a month for half a
[2270.96 --> 2278.02]  gig of ram 20 gigs of ssd drive space one cpu and one terabyte of transfer all digital ocean servers run
[2278.02 --> 2284.92]  on blazing fast ssds with tier one bandwidth and come with private networking use the promo code
[2284.92 --> 2292.52]  changelog april to get a 10 hosting credit when you sign up again changelog april 10 bucks when you sign
[2292.52 --> 2300.38]  up new accounts only head to digitalocean.com to get started and now back to the show all right we are
[2300.38 --> 2306.00]  back steve we've talked about ownership we've talked about how that kind of spreads its way through the
[2306.00 --> 2311.72]  whole system and gives you lots of wins um the memory safety stuff the security stuff surely there's
[2311.72 --> 2316.64]  other facets to rust what's another feature that is exciting to you yeah there's tons of cool stuff
[2316.64 --> 2321.64]  that's the most unique ones that tends to be the one we talk about most often my personal favorite pet
[2321.64 --> 2326.70]  feature that is other languages but the rust has a really interesting take on is closures so you
[2326.70 --> 2332.30]  alluded to this a little bit earlier but uh rust actually has because the ownership is still involved
[2332.30 --> 2337.96]  in closures but like the point is is that because of that system rust closure implementation feels just
[2337.96 --> 2342.72]  like ruby's closures so for example like let's just talk about a classic example and see you have a
[2342.72 --> 2347.24]  for loop with an array and you want to add one thing to every element of the array right so normally
[2347.24 --> 2352.74]  you're doing this like low level like i equals zero i plus plus you know all that kind of shenanigans
[2352.74 --> 2358.20]  to deal with this loop managing overhead because you don't want to pay the cost of a full closure and a
[2358.20 --> 2362.98]  function call and all that kind of stuff that's indirect um but due to the lvm's optimizations
[2362.98 --> 2367.54]  and the way you've implemented closures in rust you wouldn't write a for loop like you wouldn't see
[2367.54 --> 2372.20]  you write a for loop like you would well not a for loop but you can write a for loop in ruby but
[2372.20 --> 2376.94]  you could also use an iterator as the most important part so the closure is an iterator system ends up
[2376.94 --> 2382.62]  giving it a super high level feel but thanks to the implementation details we're actually able to
[2382.62 --> 2387.54]  in an optimized build compiled of the same assembly language that you would get out of a for loop
[2387.54 --> 2392.14]  um if you were doing the low level stuff so it like it gives you this really high level feel
[2392.14 --> 2397.20]  while still giving you low level performance and so yeah to me closures are like a super cool way
[2397.20 --> 2402.92]  and the way that they're implemented is is amazing and without it does that without having the problem
[2402.92 --> 2408.48]  of like well i guess there there's a few different kinds of closures and rust is the short version of
[2408.48 --> 2412.46]  what i'm saying but the the effect of that is that you can have a closure that basically does
[2412.46 --> 2416.92]  represent synchronous stuff and that does that handles the ownership story it handles the borrowing
[2416.92 --> 2420.84]  story basically automatically you don't really have to think about what's exactly happening
[2420.84 --> 2425.38]  with the closure like you might that you like you might expect from a low level memory managed
[2425.38 --> 2430.34]  language and it could do things like oh you didn't capture any variables in this closure so i'm just
[2430.34 --> 2434.06]  going to implement it as a regular function with no environment overhead and like stuff like that
[2434.06 --> 2438.78]  which is really impressive i think the point is that in like javascript the point i was trying to
[2438.78 --> 2443.56]  make is that in javascript a closure is sometimes used for like a loop which can inline everything and
[2443.56 --> 2448.44]  just run it right now and sometimes it's used for like a callback and those are basically the
[2448.44 --> 2453.06]  same thing in javascript so you can't it's hard to figure out what exactly is going on in rust you
[2453.06 --> 2457.38]  can tell you can tell ahead of time like this is a closure that's going to be used later it's going
[2457.38 --> 2461.60]  to be used on a thread later so the rules about ownership are more restrictive versus this is a
[2461.60 --> 2466.00]  this is a closure that's running right now because it's a you know mapping over an array and that
[2466.00 --> 2469.44]  the rules about that are much less restrictive you can basically do whatever you want in there
[2469.44 --> 2475.62]  so how do you know the difference do they just look different or context uh so sometimes a lot
[2475.62 --> 2480.78]  of it's inferred um some of it is that when you take a closure you can say like for example this
[2480.78 --> 2484.40]  is a closure that will only run one time and if it's something's a closure that can only run one time
[2484.40 --> 2488.34]  that means you can transfer ownership into the closure uh now the person who wrote the closure
[2488.34 --> 2492.66]  doesn't have to think about that the person who takes the closure has to say i'm only going to use
[2492.66 --> 2497.78]  this one time right so there's there's a few different uh kind of flavors of closure um and they're
[2497.78 --> 2501.92]  mostly described at the at the person who's taking them the person who's calling them just writes a
[2501.92 --> 2506.92]  regular closure like you would in ruby and you get exactly the right set of ownership rules that you
[2506.92 --> 2513.12]  would want awesome so uh we're gonna move on and talk about some security stuff but i'll just open the
[2513.12 --> 2518.10]  open the floor here anything else feature wise that you guys are super excited so i one thing we didn't
[2518.10 --> 2525.70]  talk about at all which is kind of mind-blowing to me is the type system um so i i i wrote a lot of ruby
[2525.70 --> 2530.72]  in javascript for a long time i pretty much didn't write considerable amount of code with types forever
[2530.72 --> 2536.04]  um i don't really like java's type system at all the first few times i had to write java felt like
[2536.04 --> 2541.00]  there was a lot of ceremony that's not to say rust doesn't have ceremony of course of course any
[2541.00 --> 2545.46]  language of the type system does but one thing that i really like about rust type system is that
[2545.46 --> 2551.32]  it takes from a lot of sort of what is well known about expressiveness to get to a point where
[2551.32 --> 2557.38]  and and this is still sort of a someday thing but you can see a world where the expressiveness of
[2557.38 --> 2561.04]  what you can do with the rust type system is pretty close to the expressiveness of what you can do with
[2561.04 --> 2567.46]  a dynamic language um while being totally uh safe and fast and my favorite example of this is
[2567.46 --> 2572.28]  in a dynamic language when you write code that's polymorphic in other words let's say you take a
[2572.28 --> 2577.80]  function you take something and you call to string on it that to string is just looked up at runtime and it
[2577.80 --> 2580.98]  calls the right to string that's what polymorphism is all about right
[2580.98 --> 2585.10]  um in rust what you would do is you would say something like i take a function that implements
[2585.10 --> 2590.74]  to string and so far that's not that interesting java has that uh you know go has interfaces but
[2590.74 --> 2594.96]  in rust the normal way that you say i take a function that implements to string uh what that
[2594.96 --> 2599.52]  does is every single time you call it it creates an optimized function that is optimized for the exact
[2599.52 --> 2604.70]  uh for the exact type that you've called it with and so instead of it going and looking up at
[2604.70 --> 2608.94]  runtime and trying to find that to string function which has some costs and also eliminates inlining
[2608.94 --> 2613.92]  right if you have to look something up at runtime you of course can't inline it uh in rust you you're
[2613.92 --> 2618.00]  getting a specialized version of that function for exactly the the thing that you called it with this
[2618.00 --> 2623.00]  called monomorphization and what that means is that not just that you avoid the overhead of going and
[2623.00 --> 2627.84]  finding the function but that you can inline and that's actually how uh steve's trick with calling
[2627.84 --> 2631.88]  dot map on an iterator and having that inline all the way to an to assemble to the right kind of
[2631.88 --> 2636.86]  assembly the way that that works is that every step of the way you're actually calling functions that are
[2636.86 --> 2641.42]  uh that are generic and they're implemented in a way that's very easy to to write specialized
[2641.42 --> 2644.90]  versions so you write the specialized version but that now that you have a specialized version you
[2644.90 --> 2648.58]  can apply other optimizations and by the time you're done writing running all the optimizations
[2648.58 --> 2654.46]  you have something that's as fast as writing it by hand which is pretty nice okay one more point on
[2654.46 --> 2659.24]  security i know you know the whole point is safety plus speed i want to ask one question about
[2659.24 --> 2663.30]  security and then we'll move on to some other stuff because we're uh we're cruising right along here
[2663.30 --> 2669.66]  the whole point is that we can't shoot ourselves in the foot with memory management is it a panacea
[2669.66 --> 2676.74]  using rust can you just feel 100 safe or can you still possibly you know write some code that's
[2676.74 --> 2682.94]  going to be exploitable so not every error is a memory safety error right so rust's definition of
[2682.94 --> 2688.52]  unsafe is very careful to talk about memory safety only and that means that like rust applications will
[2688.52 --> 2693.18]  definitely invariably have security issues it's not perfect that said it does address the
[2693.18 --> 2698.94]  vast majority of significant like terrifying secured errors because the biggest ones are usually
[2698.94 --> 2704.40]  memory safety related or i mean that means segfault right so like if you can segfault then you're
[2704.40 --> 2708.68]  talking about a memory safety error right so that's a very common way to get remote code execution is to
[2708.68 --> 2712.96]  have a segfault and then you know or stack overflow and like a kind of shenanigans and like it just you
[2712.96 --> 2717.88]  know that's not going to happen in rust code um but there are other kinds of errors that can cause
[2717.88 --> 2723.12]  problems and you know we don't we don't necessarily although we do try to help with that you know no
[2723.12 --> 2728.92]  nobody's perfect right i mean i think it's it's worth i think what steve said is basically correct
[2728.92 --> 2735.76]  which is that rust eliminates memory safety issues but i think it's easy to forget how important that
[2735.76 --> 2740.84]  ends up being um so most people are used to writing in ruby or javascript and in ruby and javascript
[2740.84 --> 2746.86]  you simply cannot segfault unless there's a terrifying bug in your program and in rust that is also true
[2746.86 --> 2751.88]  except that in rust you're stack allocating things and have direct control over memory and you don't have a gc
[2751.88 --> 2758.68]  and it's honestly like the first until you realize like i just wrote a really complicated thing and
[2758.68 --> 2764.86]  it's impossible for the segfault and really think about that it's really hard to to get it but i but
[2764.86 --> 2769.18]  i think it's it's it's saying something it's saying something that you can write something that is as
[2769.18 --> 2773.22]  complicated as the program you wrote in ruby you didn't have to write any malic or free code
[2773.22 --> 2780.90]  and it gets as fat it's basically as fast as well-written c++ code but can't can't segfault
[2780.90 --> 2787.60]  can't crash can't have memory vulnerabilities can't out of bounds error right this is you have to like
[2787.60 --> 2795.10]  meditate on it to really get it but but just because it feels just because it feels so natural when you're
[2795.10 --> 2798.74]  doing it it's like oh i'm used to writing ruby code and i'm writing a closure of course i can't
[2798.74 --> 2802.80]  like well it doesn't feel weird except that the thing that you're doing is actually quite weird
[2802.80 --> 2810.12]  like the effect is quite strange so you heard earlier in the call you mentioned and i know i've been
[2810.12 --> 2814.10]  silent for here for a bit i just know that a lot of this stuff is much deeper than i can go so i've
[2814.10 --> 2820.72]  kind of been playing uh back filter uh support but one thing you talked about which uh was pretty
[2820.72 --> 2827.14]  important you to mention was the the idea of cargo what role that plays in to crates so you've got
[2827.14 --> 2833.74]  crates.io a couple different terms here for new users of rust what do crates what are crates and
[2833.74 --> 2839.68]  what role does cargo play in that sure so um as people probably know i worked on the bundler package
[2839.68 --> 2846.64]  manager for ruby and the cargo package manager for rust and i think and i obviously use notes i'm
[2846.64 --> 2851.84]  familiar pretty familiar with npm and one thing that i think people may have under may underestimate if
[2851.84 --> 2856.72]  they're not deeply involved in one of these ecosystems is how important getting a good package
[2856.72 --> 2861.66]  management story that makes it easy to add dependencies has been i think bundler helped
[2861.66 --> 2867.64]  a lot if people people who didn't use ruby before bundler might forget how few dependencies that were
[2867.64 --> 2872.94]  relative to how many there are now and npm also sort of opened the door if you use any npm project
[2872.94 --> 2877.36]  you probably have hundreds and hundreds of dependencies i think in ruby it's usually like
[2877.36 --> 2882.94]  50 to 100 dependencies and that that's actually somewhat extraordinary and so uh when i went to work
[2882.94 --> 2886.80]  rust one of the first things that i wanted was to make sure that the ideas that came out of
[2886.80 --> 2892.96]  bundler and npm basically ideas that would make it easy to have a large a large ecosystem of packages
[2892.96 --> 2898.94]  and also to allow a lot of the innovation to happen outside of the standard library that's something that
[2898.94 --> 2902.38]  i cared a lot about and there's this is actually a thing that not everyone agrees with right there are
[2902.38 --> 2906.72]  programming languages i think python and go are good examples of this where they think it's really
[2906.72 --> 2911.26]  really important to have a rich batteries included standard library and mostly uh most of the core
[2911.26 --> 2915.10]  innovation happens in the standard library and one of the things i liked about rust when i got
[2915.10 --> 2920.48]  involved early on was even at that point there was a there was a lot of interest in taking things that
[2920.48 --> 2926.30]  were hard-coded like the garbage collection type or um exactly how uh smart pointers work and make
[2926.30 --> 2932.22]  them things that you could experiment with in in in the ecosystem right as libraries um so first that
[2932.22 --> 2938.16]  was just making them libraries in rust itself but by by having cargo and creates.io a lot of the things
[2938.16 --> 2942.30]  that used to be in the standard library are still maintained by the core team but are now cargo
[2942.30 --> 2950.06]  packages and this is this is sort of an idea that i think got got uh explored by both bundler and npm
[2950.06 --> 2954.20]  and a lot of other package managers that came out around that time and what was really awesome about
[2954.20 --> 2958.48]  working on cargo for me was that i got to say okay let's take a look at sort of the effect of that
[2958.48 --> 2964.20]  like how did semver play into that semver turns out to be pretty important npm like adds the idea of
[2964.20 --> 2969.32]  having duplication right allowing you to have version 1.x of underscore and 2.x of underscore
[2969.32 --> 2974.00]  and having them both work in the same program and rust allows you to do that so how can we how can we
[2974.00 --> 2980.06]  do that how can we do without having massive binary sizes where you have like 57 copies of the glob package
[2980.06 --> 2985.38]  in in your npm projects right people who write uh who write rust programs probably care about binary
[2985.38 --> 2991.50]  size you don't want servo to be four gigabytes large right so um what what's awesome for me about
[2991.50 --> 2996.50]  cargo is that it was at least for me the first opportunity to really go start from scratch in
[2996.50 --> 3000.74]  building a package ecosystem that would take advantage of the fact that rust itself is very good
[3000.74 --> 3007.70]  at letting people do things in user space but also look at like how rust how sorry how bundler and npm
[3007.70 --> 3015.28]  uh made community a thing i uh also github of course right so like npm and bundler both came out around
[3015.28 --> 3020.86]  the time that github was becoming popular but i got to work on cargo after that was over after github is
[3020.86 --> 3025.40]  already popular people know how github works um and and so i i think people the way people should
[3025.40 --> 3032.14]  think about cargo um is that cargo is is basically building on what we learned from the first generation
[3032.14 --> 3036.48]  after github so it's like attempting to be a second generation after github package manager
[3036.48 --> 3042.30]  that is awesome and i think this is like for me this is like the big news about open source is that
[3042.30 --> 3047.86]  this works like you can have a packet ecosystem you can have user land experimentation um and you can make
[3047.86 --> 3054.22]  you can make that work in the context of a big a big ecosystem you know one thing that uh something
[3054.22 --> 3059.34]  you said that you would remind me back to 131 we had you and tom on to talk about the road to ember
[3059.34 --> 3063.66]  2.0 was this that how you've learned from and i think it just seems like common knowledge but
[3063.66 --> 3068.22]  you've learned from things that happened elsewhere in other communities that were done well
[3068.22 --> 3072.66]  and implemented in the current community that you're doing your work in so in this case
[3072.66 --> 3077.28]  learning from github learning from npm in terms of a package package manager in the community and
[3077.28 --> 3083.74]  the importance here in rust um i just sort of made me reference back to to that i'm just also
[3083.74 --> 3091.38]  wondering if we could expect the cargo ink uh no definitely no cargo ink um but i think i think it's
[3091.38 --> 3096.34]  interesting that so dhh a long time ago had a blog post that said why there is no rails ink and
[3096.34 --> 3100.32]  that's still like i never actually print it out and put it on my wall but i kind of want to print
[3100.32 --> 3105.02]  that out and put it on my wall um about open source we do too yeah we go back to that one so
[3105.02 --> 3110.48]  that's like really like really important to me but when rails was first coming out it actually
[3110.48 --> 3116.06]  wasn't entirely clear how collaboration across the ecosystem was supposed to work like it's one thing
[3116.06 --> 3120.94]  to have like github is awesome github lets people collaborate but dependencies are a real thing right
[3120.94 --> 3124.52]  if you can't have uh if you can't have a thing that depends on something that depends on something
[3124.52 --> 3128.94]  else that depends on something else you can't actually build that high and so uh
[3128.94 --> 3134.18]  between all the things that happened over the past five years we've gone from when i started
[3134.18 --> 3139.20]  doing open source where it was like a huge project to add a dependency so certainly adding a dependency
[3139.20 --> 3144.22]  of a dependency was was almost intractable and then a dependency of a dependency of a dependency was
[3144.22 --> 3148.90]  basically like no literally nobody ever did that in the in the open source communities that i was part
[3148.90 --> 3154.14]  of to now where it's sort of it's the way it works right you expect to be able to build large stacks
[3154.14 --> 3158.36]  of your land of distractions you expect to not need betters included in the core you expect the
[3158.36 --> 3163.16]  core to stay small and nimble and focus on capabilities um this is also like the extensive
[3163.16 --> 3168.92]  web manifesto is trying to make that the way the web works and this is like i think it's kind of like
[3168.92 --> 3173.62]  to me the singularity right it's like figuring out that you can totally change the shape of iteration
[3173.62 --> 3178.30]  the iteration is not just uh like you can change the speed of iteration by making people work faster
[3178.30 --> 3184.18]  but you can only change the shape of iteration if the actual process of iteration changes and in our
[3184.18 --> 3188.52]  case having dependencies and dependencies dependencies making it so that anybody can work
[3188.52 --> 3193.32]  collaboratively work together like the shape of iteration has changed significantly and it's making
[3193.32 --> 3197.72]  things go much faster and that's awesome so i was happy to be able to make that a part of rust
[3197.72 --> 3202.30]  because i think like for me like the mind the most mind-blowing thing about rust we didn't talk about
[3202.30 --> 3207.82]  at all is the fact that you can have a browser like a web browser servo that is built using
[3207.82 --> 3212.56]  of the library package manager like the language is package manager you the way you build servos you
[3212.56 --> 3217.38]  download you get clone and then you run cargo build and that's like the way you build anything
[3217.38 --> 3222.06]  else and like what does that mean it means that they extract all kinds of stuff from inside servo
[3222.06 --> 3226.24]  their coding library their image processing these are all just off-the-shelf libraries that anyone
[3226.24 --> 3230.36]  can use for their own projects and they're all built together put together using the same approach
[3230.36 --> 3235.32]  and that like that's new like c++ doesn't have that c doesn't have that it's like a totally new thing
[3235.32 --> 3242.16]  so i guess fast forwarding a little bit to today a great day today april 3rd this is from the core
[3242.16 --> 3246.56]  team the whole entire rust core team so there is no byline that says steve wrote this yahuda wrote
[3246.56 --> 3253.80]  this or someone else wrote this a great announcement today rust 1.0 beta um what does it mean i guess
[3253.80 --> 3259.82]  you got 172 contributors for this release what does it mean for the community to have 1.0 here what
[3259.82 --> 3264.02]  does it mean to when you put the label beta on there in terms of what's out there now and how it
[3264.02 --> 3268.98]  would be used so the big step here is that historically speaking we've only had one release
[3268.98 --> 3274.98]  of the compiler and that's nightly every night a new compiler comes out um with today's release beta
[3274.98 --> 3279.22]  there's now two versions of the compiler the nightly version which continues to be put out every night
[3279.22 --> 3284.22]  and then the beta version which was released today uh tomorrow there will be a new nightly but there will
[3284.22 --> 3290.68]  probably not be a new beta um and so the way that this works is uh six weeks from now probably
[3290.68 --> 3294.62]  probably there's some there's some i want to hand wave slightly you know if we find something
[3294.62 --> 3300.34]  catastrophic we fix it immediately or whatever but the idea is that six weeks from today there will
[3300.34 --> 3306.04]  be a release of one point rust 1.0 final and so what happens at that point is the beta becomes the final
[3306.04 --> 3312.20]  and the nightly on that night becomes the new beta so so like nightly turns along every single night
[3312.20 --> 3317.44]  and then every six weeks we have a new release of the like pre-testing branch and then the actual
[3317.44 --> 3322.20]  release branch and so uh that's the first thing is this is the first step towards those kind of like
[3322.20 --> 3327.20]  train model which was originally pioneered by you know chrome and firefox and it's also used in ember
[3327.20 --> 3333.46]  um but the other thing that's a side effect of that is the beta channel comes with stability guarantees
[3333.46 --> 3340.08]  which we have never ever guaranteed basically any kind of stability whatsoever over the eight years of
[3340.08 --> 3346.72]  rust's development and so that's like the big major changes is that we're saying we still may change
[3346.72 --> 3353.26]  some small things but basically this is representative of the actual 1.0 final release which will have
[3353.26 --> 3358.94]  total backwards well total maybe a little strong but like drop-in replacement like 1.1 should be a
[3358.94 --> 3364.70]  drop-in replacement for 1.0 so we're offering very strong backwards compatibility guarantees yeah i think
[3364.70 --> 3370.06]  one way to think about it is that 1.0 beta is actually not different from 1.1 beta or 1.2 beta or 1.2
[3370.06 --> 3375.62]  and uh for people who are not familiar steve talked about this but this is basically how browsers
[3375.62 --> 3380.72]  work and in my view this is the future like ember does it now rust does it in my view this is this is
[3380.72 --> 3385.14]  how you should do it how you should i'll be doing it for all my projects in the future it's awesome so
[3385.14 --> 3391.44]  but the the basic idea that there is uh you ship every six weeks but you also ship a staggered beta
[3391.44 --> 3396.12]  release and that beta release is extremely stable it's only the features that have been approved that
[3396.12 --> 3399.70]  are actually ready to go and you're just getting some feedback you have these you have nightlies that
[3399.70 --> 3404.72]  people can subscribe to and and the really awesome thing for me about all this stuff is that it lets
[3404.72 --> 3410.58]  people subscribe to a channel that is appropriate for their level of stability uh reliance right so
[3410.58 --> 3414.82]  some people might be unwilling to ever have instability they need to just keep rolling and
[3414.82 --> 3419.84]  those people should just use the the release channel right but some people want the new features as soon
[3419.84 --> 3423.70]  as they're basically ready maybe there's not they're not stability guaranteed yet but they're basically
[3423.70 --> 3427.60]  ready those people choose the beta channel and some people really want to be bleeding edge those people
[3427.60 --> 3431.82]  to use the nightly channel and the thing that's awesome about this is that it doesn't you can the
[3431.82 --> 3436.96]  the core team itself just does all their work on master right so this we it used to be that this
[3436.96 --> 3441.60]  sort of trade-off between how stable unstable you need to be was the decision that you have to finally
[3441.60 --> 3446.42]  tune you have to finally hone as a core team to figure out what exactly you want to do and the real
[3446.42 --> 3452.96]  genius of the chrome uh model which is what started this all is that it lets people self-select into a
[3452.96 --> 3457.30]  stability set that they want if someone uses nightly they can't complain if things broke that's what
[3457.30 --> 3462.34]  they signed up for right but if someone uses stable you know that they really care about stability um
[3462.34 --> 3466.72]  and that's something that as a person working who's worked on a lot of open source like being able to
[3466.72 --> 3471.22]  know that people have signed up for the thing that they're getting is pretty mind-blowing it's pretty
[3471.22 --> 3477.84]  awesome you put on uh on that note on the six week release cycle i think it's been only a couple weeks
[3477.84 --> 3482.86]  about three weeks it seems maybe two weeks since you tweeted about it and then to your discourse for ember
[3482.86 --> 3489.52]  uh a question was posed is the six week six weeks release cycle too frequent what's been some of the
[3489.52 --> 3494.36]  feedback from the community and i guess some of the core contributors to ember and how it i guess it
[3494.36 --> 3500.00]  might play here to rust and then as steve said every project he'll ever do yeah so it's actually really
[3500.00 --> 3504.26]  interesting because the thing that's kind of funny about the six week release cycle so six weeks is not
[3504.26 --> 3509.84]  very long um yeah the idea behind six week the six week release cycle is that unless you've done
[3509.84 --> 3515.42]  something catastrophically wrong uh people can just keep upgrading every release so every you know
[3515.42 --> 3521.12]  every six weeks people can spend a few hours at most an upgrade i say a few hours because in javascript
[3521.12 --> 3526.82]  the dynamism means that people accidentally rely on private apis all the time but in general that's
[3526.82 --> 3532.56]  like a short quick update people can just like schedule as part of their sprint and be happy and that's
[3532.56 --> 3535.90]  that's something that has actually worked out pretty well for ember i would say even on that thread
[3535.90 --> 3541.90]  most people said it's awesome i basically just upgrade and it's fine yeah um the thing that's
[3541.90 --> 3547.18]  kind of unfortunate about it is that that does mean that if you're a person who can't upgrade every
[3547.18 --> 3551.94]  release there isn't really any good guidance for you about what else might be a good process right so
[3551.94 --> 3556.30]  if you don't if you can't schedule every six weeks to do an upgrade or if you have very very extreme
[3556.30 --> 3561.10]  stability requirements or if you're using unstable features you know you're doing private stuff or you're
[3561.10 --> 3565.74]  building an add-on that does private stuff right it may not be so obvious to you what the right story is so
[3565.74 --> 3570.02]  i think probably what we're going to do and this is something we just talked about in the core team
[3570.02 --> 3575.28]  meeting today um i think probably what we're going to do is we're going to create a release every four
[3575.28 --> 3581.26]  releases or so so that'll be like twice a year and that release is a release that we say is going to
[3581.26 --> 3585.30]  be stable now it's a little funny because all of our releases are stable we follow semver right so
[3585.30 --> 3591.02]  all our releases are stable so really all we're saying is if you're like this is a good release for you to
[3591.02 --> 3595.66]  stick on we'll maintain backwards compatibility i will we'll continue to do security patches to
[3595.66 --> 3601.44]  that release uh for a while and um perhaps the most interesting one and this may or may not end
[3601.44 --> 3606.98]  up being important in rust is we have a policy in ember that any private api that's heavily used if
[3606.98 --> 3611.18]  it turns out that we have to change it we don't just change it off the bat we do a two-step deprecation
[3611.18 --> 3615.58]  right so we do a deprecation in one release and then the next release we'll remove it just so that
[3615.58 --> 3619.50]  people know that we're going to do that and so maybe one thing that we'll do with the with this
[3619.50 --> 3625.02]  uh more long-term release processes will say we won't remove something until the deprecation has
[3625.02 --> 3629.62]  crossed over one of these kind of cycles but sort of the funny thing is and this is like the
[3629.62 --> 3634.18]  conversation we had the core team meeting today was everyone was like i don't really see how this is
[3634.18 --> 3637.80]  significantly different from what we're doing right now and my point to them was it's not
[3637.80 --> 3642.72]  significantly different it's just a way of telling people it's a way of being clear to people that what
[3642.72 --> 3646.74]  we're doing right now enables this style of really of updating whatever you want people are so used to the
[3646.74 --> 3651.72]  idea that an upgrade is who knows how long it's who knows how complicated who knows how messy
[3651.72 --> 3656.20]  that yeah the idea of upgrading every six weeks seems crazy so all we're really going to probably
[3656.20 --> 3660.46]  be saying with this process is you know we'll give you a rolled up change log which is pretty easy
[3660.46 --> 3666.64]  and we we it is actually safe to do this which was all it was already true but we weren't saying it
[3666.64 --> 3674.18]  right it's probably in the the existing processes to make them more foundational and explanatory to the
[3674.18 --> 3679.32]  community trying to prop themselves up around ember and then how's it as this same six-week
[3679.32 --> 3685.32]  release cycle plays into rust and and any other uh project that sort of picks this up i can see that
[3685.32 --> 3690.00]  definitely how that's you know just formalizing what's already in place what's pretty awesome about
[3690.00 --> 3696.54]  rust i think rust may have less trouble because rust is has such strong typing i suspect that some
[3696.54 --> 3700.52]  of the kinds of issues that we've seen with ember where people end up using private apis and we end up
[3700.52 --> 3706.16]  getting stuck i suspect those will happen less where just because if you break something things
[3706.16 --> 3710.30]  don't compile so you find out very fast like the canary build will it won't be like people will
[3710.30 --> 3715.38]  live along it will fail to compile and then it's not easy to go in you know poke in at the internals
[3715.38 --> 3721.04]  of something somebody doesn't want you to poke in at so i my hypothesis is that the kinds of
[3721.04 --> 3726.30]  deprecations that we have to do in ember of private features will be fewer and more far between in rust
[3726.30 --> 3731.54]  than they were in ember well if uh if you're listening now stay excited because we're going
[3731.54 --> 3737.06]  to take a quick break uh we're going to rewind a little bit and kind of go maybe to noob level
[3737.06 --> 3741.50]  talking about getting started those are just picking up rust and then we're going to hypothesize a little
[3741.50 --> 3746.74]  bit about the future steve's got something particularly he wants to talk about um let's take a quick break
[3746.74 --> 3753.08]  to listen to a sponsor we'll come right back today's show is sponsored by app quality bundle if you haven't
[3753.08 --> 3759.08]  heard of this yet you got to check it out it's a time limited deeply discounted bundle of web services
[3759.08 --> 3767.74]  for building better mobile and desktop apps this offer for this expires on april 15th 2015 so if it's
[3767.74 --> 3773.86]  after that date and you're listening to this it's too late there's a time limit to buy but not a time
[3773.86 --> 3781.86]  limit to use what do you get well first off you're going to save 89 on a year of century run scope code
[3781.86 --> 3788.76]  climate circle ci and ghost inspector when combined together each of those services give you complete
[3788.76 --> 3794.06]  app quality coverage from mobile to web and here's the best part what would normally cost you well over
[3794.06 --> 3802.70]  nine thousand dollars you're going to get for 999 that's an 89 huge savings beyond the deeply
[3802.70 --> 3809.36]  discounted price once you purchase it it won't expire this is perfect for new projects projects that are
[3809.36 --> 3814.14]  growing up and need end-to-end quality coverage from mobile to web or for development shops taking
[3814.14 --> 3819.48]  care of clients and their services so there's only really one caveat to mention and this that is
[3819.48 --> 3824.52]  strictly for new accounts only there might be some exceptions to this rule but you'll have to check the
[3824.52 --> 3830.30]  fine print or get in touch with them if you've got a specific question check it out at build better
[3830.30 --> 3834.76]  dot software that's right build better dot software now back to the show
[3834.76 --> 3841.96]  all right we're back uh getting started um i've got some ideas on where people might get started
[3841.96 --> 3846.24]  because you know i can google right but steve where should we pick this up at you got pretty
[3846.24 --> 3851.22]  neat idea on maybe where this could be where this can begin yeah so this is sort of a segue from the
[3851.22 --> 3855.72]  last uh chunk that we were talking about and then i will give you an exactly but uh one of the things
[3855.72 --> 3860.36]  that rust is doing and that i think you and i are both trying to do with rust is to bring a lot of the
[3860.36 --> 3865.28]  concepts that web programmers are used to doing into this space systems programming that no one
[3865.28 --> 3870.50]  has done before and you gave this talk at gogaruko which i really thought was really fantastic and has
[3870.50 --> 3874.24]  something that matters for this getting started aspect so i know a lot of the people listed the
[3874.24 --> 3878.64]  changelog and a lot of people that like follow me on twitter are dynamic language programmers that have
[3878.64 --> 3882.88]  never done compiled statically typed languages before they've never done low-level programming before
[3882.88 --> 3888.56]  and so there's this really interesting comparison between what node did and what i hope rust does for
[3888.56 --> 3893.76]  systems so one of the things that node enabled was an entire generation of programmers who had only
[3893.76 --> 3898.82]  ever been front-end devs quote-unquote they'd only done a little bit of jquery and it enabled them to
[3898.82 --> 3904.58]  write back-end code and that was like a new superpower for them like this whole group of people now have
[3904.58 --> 3908.54]  this ability to do this brand new thing in computing and we've seen a ton of really fantastic things
[3908.54 --> 3914.14]  sort of fall out of that with these new people getting excited and so what i'm hoping is that if you've
[3914.14 --> 3919.90]  never done systems programming before that rust will be able to help ease you into doing this kind
[3919.90 --> 3924.44]  of low-level programming and so i don't have all these resources in place yet but one of the things
[3924.44 --> 3928.02]  that's going to be important for the future of rust and that i hope to get done in the next six weeks
[3928.02 --> 3933.82]  is to actually have documentation specifically around uh you've never been a systems programmer
[3933.82 --> 3939.56]  before let's teach you systems programming as well as rust and then you know not just oh you already
[3939.56 --> 3944.24]  are a super hardcore c plus plus hacker here's what you need to know about how rust works and so i think
[3944.24 --> 3948.34]  that's a really important thing one thing that you can bet will happen is the exact same thing that
[3948.34 --> 3952.40]  happened with node which is that there's all these people out there who are already systems programmers
[3952.40 --> 3955.90]  just like there were all these people who are already back-end programmers and they didn't get the
[3955.90 --> 3960.98]  enabling power of node and so people you'll hear people say i don't understand why rust is so important
[3960.98 --> 3964.86]  i could do all this stuff with c plus plus like look at my c plus plus code i'm already doing all the
[3964.86 --> 3969.04]  things rust already does and those people will be missing the point they'll be missing the point that rust
[3969.04 --> 3973.58]  is enabling people who previously couldn't write c plus plus write c plus plus it's not i mean it will
[3973.58 --> 3980.40]  help people who uh who don't want to as you did before right and it will help people who unlike node i
[3980.40 --> 3986.88]  think it actually is genuinely uh an improvement for c plus plus writers pretty much strictly a strict
[3986.88 --> 3991.54]  improvement but i but i think people will miss the point you will you can expect that people will miss
[3991.54 --> 3995.48]  the point because this is the story of enabling technologies anytime there's a technology that enables a
[3995.48 --> 3998.88]  group of people who weren't good at something to do something other people are already
[3998.88 --> 4002.34]  doing the people who are already doing it say i don't see the point of this this seems pointless
[4002.34 --> 4007.02]  and something like do you really want all these people coming in and for me the answer is always yes
[4007.02 --> 4012.10]  i always want all these people who felt intimidated by technology to go in and actually have the power
[4012.10 --> 4016.94]  to do the right thing or have the power to do things with it and that's something that i've already
[4016.94 --> 4022.32]  seen happen for myself with rust and i expect to see it with a bigger group so on that on that angle
[4022.32 --> 4027.44]  the getting started thing so the what's uh the best place to get started and of course i have slight
[4027.44 --> 4032.58]  amount of bias in this is uh we actually have a large amount of documentation on the rust website
[4032.58 --> 4038.28]  uh that i call the book or the rust programming language and so this is what my baby uh it's what
[4038.28 --> 4042.70]  i work on the most of the time so you wrote this this is yours i mean other people it helps
[4042.70 --> 4046.28]  okay i have done the vast majority of the work i was trying to figure it out because that was
[4046.28 --> 4050.78]  one of the first on my list of getting started like i found this and i found a few other things but
[4050.78 --> 4055.66]  i was very impressed by the organization uh and also the writing behind the cell thank you
[4055.66 --> 4060.16]  uh so one of the things that uh is it's still you know maybe by the time the show gets actually
[4060.16 --> 4064.50]  published i have a little bit of these things in place but uh i want you to be able to start reading
[4064.50 --> 4068.70]  this and they'll give you a little project that you'll build together um so right now it sort of
[4068.70 --> 4073.34]  takes a syntactical approach of like explaining the syntax of rust and it'll get you started with those
[4073.34 --> 4078.34]  basics um but due to some shenanigans um i pulled the project that used to be there and i have a better
[4078.34 --> 4083.10]  one um that's going to be a tutorial that's coming out and so that will uh hopefully be a nice way to
[4083.10 --> 4087.66]  get started if you don't know what you want to write in rust um so yeah the book is the most up-to-date
[4087.66 --> 4091.84]  and comprehensive documentation that we have part of the reason why it's up-to-date is that the
[4091.84 --> 4098.16]  documentation tools we have actually run the code in the documentation as a test so if something in the
[4098.16 --> 4104.20]  compiler changes uh it will actually break the documentation um and so it's been kept up to date
[4104.20 --> 4110.52]  sheerly because commits don't pass unless it is also up-to-date uh so um there's of course one or
[4110.52 --> 4115.28]  two areas where that's not true etc hand wave yada yada but it's generally speaking the most correct
[4115.28 --> 4120.44]  and up-to-date documentation there's also another project that we uh have it's rust by example.com
[4120.44 --> 4124.94]  this is originally written by a community member and then it was sort of donated to the rust core team
[4124.94 --> 4129.86]  when he decided he didn't want to work on it anymore and it's more of a like small snippets of code
[4129.86 --> 4135.68]  like a tapas kind of like approach um and i frankly need to give it a little more love but
[4135.68 --> 4139.68]  it's still pretty good and i make sure every night i have a build that tests against nightly
[4139.68 --> 4143.98]  and i make sure that it's been up to date so those two resources are the big primary ones
[4143.98 --> 4149.12]  and the ones that are most accurate unfortunately when you're trying to go towards a release there's
[4149.12 --> 4152.96]  always those last minute changes you're sort of sneaking in the last two weeks i've seen a bunch
[4152.96 --> 4157.80]  of breaking changes that means that and also over the alpha period there were a bunch of changes that
[4157.80 --> 4162.56]  have made a lot of the other documentation that exists on the web kind of obsolete you'll need a
[4162.56 --> 4167.38]  little bit of hand holding going with those um but another great resource for learners is the irc
[4167.38 --> 4174.02]  channel that we have in uh hashtag rust pound rust i guess in the in the old old terms oh man wow i just
[4174.02 --> 4181.56]  betrayed myself by saying hashtag um using too much twitter but the point is is that uh the the rust chat
[4181.56 --> 4187.48]  room is a wonderful welcoming friendly place for people to ask even the most basic questions about rust
[4187.48 --> 4193.76]  um if people are jerks i will kick them um basically we're encouraging people like i i want
[4193.76 --> 4197.70]  people to feel comfortable absolutely asking any question whatsoever and we have a ton of really
[4197.70 --> 4202.66]  great people that are around that will help um if you get stuck so if you do use a bit of
[4202.66 --> 4207.60]  documentation or like a blog post that's a little out of date oftentimes jumping an irc someone can tell
[4207.60 --> 4211.84]  you oh yeah you just need to tweak the name of that function or like oh this changed that type or
[4211.84 --> 4217.88]  something like that and so those um that's also a really fantastic resource for like up-to-date uh
[4217.88 --> 4222.78]  things hopefully now that beta is released we'll start having more broad community initiatives that are
[4222.78 --> 4228.02]  actually uh you know accurate um but a lot of people understandably have been sort of holding off on
[4228.02 --> 4234.90]  their projects until this stable thing actually happens so aside from aside from rc uh do you have a
[4234.90 --> 4239.92]  discourse under that uh something else that surface was the subreddit on uh for us it seemed like
[4239.92 --> 4243.32]  there was at least a place where there's a lot of interaction and maybe even where new announcements
[4243.32 --> 4248.02]  are happening the for example the betas mentioned there which was submitted by you steve yeah yeah
[4248.02 --> 4254.52]  so uh we have two official forums uh they're both discourse instances uh one is at users.rustlang.org
[4254.52 --> 4258.82]  and that's intended for just general discussion about people who are using rust and then there's
[4258.82 --> 4263.70]  internals.rustlang.org which is used to develop the language itself so we have those two things split
[4263.70 --> 4268.72]  out just so that you know hello world questions don't interfere with like deep type theory questions
[4268.72 --> 4273.08]  and you know you can pay attention to however much uh of those two things we have some people
[4273.08 --> 4277.60]  that only read the internals discussion and some people that only read users obviously uh reddit does
[4277.60 --> 4282.94]  exist although uh i'm a reddit hater so i try not to talk about it as much as possible um but the
[4282.94 --> 4288.04]  reddit the rust subreddit is a shining example of all the things that reddit is not um it is also a
[4288.04 --> 4294.04]  nice wonderful friendly welcoming place uh as opposed to the rest of reddit it seemed nice i was surprised
[4294.04 --> 4299.66]  i was like this is kind of cozy in here i like the rust subreddit a lot i think people should also
[4299.66 --> 4304.08]  realize that there's a bit of a clash of cultures in the rust community which is there's a bunch of
[4304.08 --> 4309.32]  people who are writing rust because they were c++ hackers and they really want uh rust to be a better
[4309.32 --> 4314.04]  c++ and then there's a bunch of people that came in because they're being enabled to be systems
[4314.04 --> 4319.38]  programmers for the first time and so if you come in uh if you come into a conversation and you say
[4319.38 --> 4323.72]  something from the perspective of being a higher level programmer and you get a bunch of stuff thrown at you
[4323.72 --> 4329.40]  from the perspective of being a c++ hacker don't let don't let that discourage you i i've definitely
[4329.40 --> 4335.28]  seen it happen occasionally maybe more than occasionally in some cases i would say assume
[4335.28 --> 4339.80]  that the person who is talking to you is saying that because they feel passionately about wanting
[4339.80 --> 4344.80]  rust to be a replacement for c++ but also assume that you don't need to understand necessarily right
[4344.80 --> 4349.64]  away everything that they're saying in order to be a effective rust programmer and and importantly you
[4349.64 --> 4353.50]  might have some insights on the ergonomics of the thing that's being discussed that a person who
[4353.50 --> 4358.84]  is who is so used to the pain and suffering of c++ might not be able to see when we originally
[4358.84 --> 4363.92]  pitched cargo none of the hardcore c++ crowd believed that they would be using it and by now
[4363.92 --> 4368.62]  they're all basically using it right they're depending upon it yeah yeah so both of these sort
[4368.62 --> 4373.44]  of groups we sort of have three camps in the rust world there's the like functional people the dynamic
[4373.44 --> 4377.94]  programming people and the c++ people and all three of them have different like pros and cons to offer
[4377.94 --> 4382.28]  each other in terms of their perspective and experience so it's been pretty cool to see those three
[4382.28 --> 4390.70]  groups sort of coalesce um so last week we had zach zapala on the show he's the ceo of spark.io it's an
[4390.70 --> 4396.92]  open source hardware company doing dev kits for wi-fi and cellular um that's episode 150 if you're
[4396.92 --> 4401.90]  interested but in the post show we told him we're talking with you guys this week and he was quite
[4401.90 --> 4409.10]  excited about rust and he was kind of hypothesizing on uh embedded rust and getting excited about that
[4409.10 --> 4415.60]  in fact he pointed us to a project called zinc yep which is an experimental attempt to write an arm stack
[4415.60 --> 4420.76]  according to them um we'll link that up in the show notes as well we want to kind of look at the future
[4420.76 --> 4426.14]  right now you know there's a we're at 1.0 beta and we've talked about what all that means but i'd like to
[4426.14 --> 4433.30]  take a chance to let you guys kind of prognosticate what you see rust doing going forward what you know
[4433.30 --> 4438.98]  little niches will it um disrupt and where will it play well and where won't it so maybe start with
[4438.98 --> 4446.18]  you and then steven can take a shot as well so i can give my my wistful hopes for the future uh which
[4446.18 --> 4452.62]  is i think rust is pretty awesome because the ownership system means that most code that you write
[4452.62 --> 4458.38]  actually only cares about the abstract notion of reference and not exactly how it was allocated
[4458.38 --> 4462.38]  that's like a core concept of rust so i could definitely imagine in the future having a world
[4462.38 --> 4467.36]  where people are able to write application layer code that's either reference counter or gc even
[4467.36 --> 4474.84]  um but it talks to a lower like a framework layer that's extremely performance that you so i sort of
[4474.84 --> 4479.70]  think about rails right rails because application layer is written in ruby the framework layer is
[4479.70 --> 4484.40]  written in ruby but ruby has real performance limitations and if you start to write rails in c++
[4484.40 --> 4489.32]  or c and someone jumped in to understand they'd be like oh my god i have no idea what's going on
[4489.32 --> 4493.64]  please write this in ruby but because rust is sort of has sort of this natural layer where
[4493.64 --> 4499.78]  uh it it uh separates allocation the cost of allocation from the details of how you actually
[4499.78 --> 4504.02]  work with the objects i can easily imagine someone writing a rails that was very fast very efficient
[4504.02 --> 4509.24]  very low level and worked with um the ownership system but then the glue code on top
[4509.24 --> 4515.76]  the application layer code was very was much more loose was gc or reference counter based and that
[4515.76 --> 4519.92]  sort of thing is exciting there's a lot of work that's left to be done um that's not something
[4519.92 --> 4525.58]  someone could start doing today uh there's language features that are still left but i i think um i say
[4525.58 --> 4529.48]  this and i'm sure that we're gonna get a bunch of rust people that say that's impossible you shouldn't
[4529.48 --> 4533.90]  get people's hopes up but i i can imagine happening and i want i want to see something like that happening
[4533.90 --> 4542.74]  i i've been sort of thinking about the the release of 1.0 is like an event horizon like all of my
[4542.74 --> 4549.62]  hypothesizing about what may happen post-release are sort of like not important the most important
[4549.62 --> 4554.50]  thing is eye on the prize heads down like ship the best possible 1.0 that i can possibly ship
[4554.50 --> 4558.64]  because you only get one chance at a first impression i've been joking that i can't wait for
[4558.64 --> 4562.76]  the six-week release cycle to start kicking in for real because like this is the only stressful
[4562.76 --> 4567.32]  releases that we'll have is today and six weeks from today and every release after that is just
[4567.32 --> 4572.48]  like oh yeah this is just a friday like no big deal um so i've admittedly been thinking a little bit
[4572.48 --> 4577.64]  less about the future because i've been so focused on you know the immediate presence um i think that
[4577.64 --> 4581.98]  if i had to say overall it would definitely be much more social kind of aims than it is like specific
[4581.98 --> 4587.26]  technical aims i would love to see rust start to be used to teach operating systems classes and
[4587.26 --> 4594.16]  colleges we've already had one instance of that happen um and i would love to see rust make a lot
[4594.16 --> 4599.30]  of more people uh understand that low-level programming is not inherently harder than high-level
[4599.30 --> 4603.38]  programming uh this could be a whole other show so i won't get into that a whole lot more but i think
[4603.38 --> 4606.70]  that different people have different aptitudes and some people think that low-level programming is
[4606.70 --> 4611.46]  easier than web programming because web programming is actually very complicated so um i would like to
[4611.46 --> 4616.94]  see like a new generation of people get interested in doing sort of systemsy stuff and i think that
[4616.94 --> 4622.28]  we'll be able to like help them out with that um so that's sort of my big focus more than a
[4622.28 --> 4627.76]  specific technical thing i'm interested in the social good that we can do uh and also like you
[4627.76 --> 4633.68]  know rewriting libraries that need to be safe in a safer language will do a lot of good in the world
[4633.68 --> 4640.46]  too hopefully so awesome man sounds like really cool stuff unfortunately we're running low on time
[4640.46 --> 4643.94]  here so we're going to do a few of our closing questions and we'll probably split them up
[4643.94 --> 4649.94]  give yahuda one i'll give steve one um one question we ask maybe i'll pitch this one to steve
[4649.94 --> 4656.84]  is wait if you had a call to arms to the open source community with regard to rust and you wanted them to
[4656.84 --> 4661.30]  do something to help out to get involved what would you say what's the best way what should people be
[4661.30 --> 4667.76]  doing i would say give it a try uh write down what you think whether or not it's positive or negative
[4667.76 --> 4675.32]  although uh you know try to be constructive please for my ego insanity uh and uh leave a like a post in
[4675.32 --> 4679.84]  our users forum um which you know this is a discourse you can sign in with github or twitter you don't even
[4679.84 --> 4684.96]  need to make like a real account or anything and just let us know what you think um this next six weeks
[4684.96 --> 4690.02]  is going to be largely about polish and so we can only polish off the sharp edges that you help us find
[4690.02 --> 4694.82]  so there are undoubtedly a lot of them um i've already submitted two pull requests today to fix
[4694.82 --> 4699.68]  tiny things um but yeah like just just straight up honest feedback and giving a good shot would be
[4699.68 --> 4707.74]  wonderful awesome uh next question this one's for you huda you guys are kind of uh leaders in finding
[4707.74 --> 4715.16]  new things and kind of steve found rust before i had any idea what what the heck it was um and so
[4715.16 --> 4718.64]  we're always interested with our guests like what's on your radar of course you've been deeply
[4718.64 --> 4723.92]  embedded into ember and into the rust uh ecosystems but do you have anything else that's kind of
[4723.92 --> 4728.08]  tantalizing you a project that you're interested in or if you have a free weekend that you'd want
[4728.08 --> 4735.96]  to hack on that perhaps folks haven't heard of so mostly i do web stuff okay and i think i think uh
[4735.96 --> 4739.34]  maybe i'll just answer this generically with platitudes because i don't i don't actually have
[4739.34 --> 4745.26]  any specific project okay but but uh i think people underestimate the web over and over and over again
[4745.26 --> 4750.90]  um and i think we're in the middle of another wave i think something like 2011 was the last big wave of
[4750.90 --> 4756.06]  features that really fundamentally shifted how people use the web um so things like web workers
[4756.06 --> 4763.62]  uh typed arrays index db flexbox these are all things that i think if you go look back you can see
[4763.62 --> 4768.56]  that those are fundamental game changers some of them made as in just possible um but of course when
[4768.56 --> 4773.42]  they happen people say oh those guys they're taking a document format and cramming on random blah blah blah blah
[4773.42 --> 4778.74]  blah blah whatever whatever people say um and i think we're in the middle of another wave um so
[4778.74 --> 4786.28]  there's things like uh more work on asmjs service worker the houdini project which is doing some work
[4786.28 --> 4792.88]  to expose more of css uh directly to users a bunch of things like that that i think are going to end up
[4792.88 --> 4798.90]  being important um and it's i find it interesting that it's not when i look back it's not like there's
[4798.90 --> 4803.84]  any one it's it's people are kind of expected to either be totally stagnant or changing all the time
[4803.84 --> 4809.62]  and i kind of see waves so uh i guess keep an eye out for like what's going to happen over the next
[4809.62 --> 4814.94]  year or two on the web and if you want to think about what's coming next on the web you should
[4814.94 --> 4818.98]  think about how to take advantage of the things that are coming and not be so cynical about them
[4818.98 --> 4825.10]  very good answer um well it's been definitely been having been uh definitely been fun having
[4825.10 --> 4829.56]  you guys here on the show today i know this has gone a little longer than maybe our norm is but
[4829.56 --> 4834.88]  for those long shows this is about right in the good range where we kind of camp out in so um
[4834.88 --> 4837.80]  definitely want to thank you guys for taking the time to come on and talk about rust definitely
[4837.80 --> 4842.78]  excited about where it's going keep in touch with us we definitely want to help however we can to
[4842.78 --> 4849.88]  uh encourage those who haven't yet tried rust to try rust and give constructive polite graceful
[4849.88 --> 4854.64]  feedback um because that's what's that's the world needs right you can't be mean you gotta
[4854.64 --> 4859.50]  there's nice there's too many people being jerks on get up issues right all directions and i would
[4859.50 --> 4864.82]  like if that not happened anymore yes totally agree totally agree with um and we echo that and we
[4864.82 --> 4869.74]  ask the entire community for the same thing we do have a couple shows coming up i'm going to tease
[4869.74 --> 4876.52]  the next one so i guess to to you who does mention back to the web this is going to the platform i
[4876.52 --> 4883.22]  think that's pretty strong out there it's called wordpress we're talking to roots.io sage a very
[4883.22 --> 4889.16]  cool starter theme and bedrock which is a modern wordpress stack we're talking to ben word and scott
[4889.16 --> 4896.92]  walkinshaw about that we had some awesome sponsors for this show code ship at quality bundle which is a
[4896.92 --> 4903.36]  time limited super awesome bundle it expires on april 15th so take a listen to that uh top towel
[4903.36 --> 4909.70]  in digital ocean whom absolutely love what we do here but thanks to steve and yahuda and jared and
[4909.70 --> 4916.10]  all the awesome listeners the members and for now let's say goodbye everybody bye thanks guys
[4916.10 --> 4927.48]  bye
[4927.48 --> 4929.54]  you
[4929.54 --> 4959.52]  I love you
