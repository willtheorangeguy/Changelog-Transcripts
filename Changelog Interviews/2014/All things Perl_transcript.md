[0.00 --> 14.24]  welcome back everyone this is the change log and i'm your host adam stekowiak this is
[14.24 --> 21.74]  episode 133 today jared and i talked to curtis poe about all things pearl a great conversation
[21.74 --> 27.26]  you're gonna love it this show is sponsored by code ship rack space and status page.io
[27.26 --> 32.58]  we'll tell you a bit more about rack space and status page.io later in the show but our friends
[32.58 --> 38.46]  at code ship are all about continuous integration and delivery as a service you can release more
[38.46 --> 44.34]  frequently get faster feedback and build the product your users need a simple push to a repo
[44.34 --> 49.84]  runs your automated tests and configure deployments from the simple deployments are roku to complex
[49.84 --> 55.34]  deployment pipelines for large infrastructures they can all be set up with ease they even integrate
[55.34 --> 60.54]  with github or bitbucket you can get started today with their free plan setup takes just three minutes
[60.54 --> 67.06]  make sure you use the code the changelog podcast to get a 20 discount for three months on any plane you
[67.06 --> 73.68]  choose head to code ship.io slash the changelog and tell them the changelog sent you and now on to the
[73.68 --> 87.38]  show everybody we're back and today we're joined by curtis ovid uh ovid poe actually he's got a cool
[87.38 --> 92.00]  middle name there's not a real middle name maybe at some point curtis you can mention how you got that
[92.00 --> 98.58]  name it's your internet handle right yes it is i'm here jared's here we're all here with curtis and
[98.58 --> 105.34]  we're going to talk about pearl so we're excited what's uh what's ovid ovid um a long time ago when
[105.34 --> 111.06]  i switched from mainframe development and getting into pearl uh i decided to sign up for the website
[111.06 --> 117.30]  called pearl monks and i happen to tremendously enjoy poetry and when i had to pick a username
[117.30 --> 122.90]  my two top favorite poets were uh an 18th 19th century scottish poet named john davidson
[122.90 --> 129.82]  or the roman poet ovid and john davidson sounded like a very stupid username so i picked the username
[129.82 --> 136.86]  ovid and it just stuck with me for the years i like ovid i wish i had that name and i could be i
[136.86 --> 141.28]  could be a ba with with ovid oh his poetry is phenomenal highly recommended particularly
[141.28 --> 148.16]  translations by peter green so uh that's that's obviously language dependent there but um let's
[148.16 --> 155.90]  give a shout out to to uh robert norris uh he's rob n r-o-b-n on github he actually suggested this
[155.90 --> 160.22]  show via our ping repo so if you don't know it and you're a listener out there we have a weekly email
[160.22 --> 166.80]  we ship we have a featured section in there for pings we get on the ping repo drop an issue in there
[166.80 --> 172.58]  just like robert norris did or rob n on github did uh to suggest us to talk to curtis and talk about
[172.58 --> 178.14]  pearl and kind of bring we've never actually had a pearl specific show on this uh on the podcast
[178.14 --> 183.90]  so we're excited about that but uh every week we feature how many repos we feature jared on in
[183.90 --> 191.30]  weekly uh three three okay so we feature three repos in our weekly email via ping so if you've got
[191.30 --> 195.76]  some awesome repos out there you need some extra traction on drop them in there they might show up
[195.76 --> 199.82]  on the podcast they might show up in the email they might show up on the blog you just never know
[199.82 --> 204.90]  we might even tweet it out so uh with that said let's let's drop into to this conversation with
[204.90 --> 211.06]  curtis curtis you know jared jared and i you know jared back in college you did some pearl work
[211.06 --> 217.32]  i own a few pearls um we probably have a pretty diverse listenership to this uh to this podcast
[217.32 --> 222.36]  that is going to be really adept to programming but maybe not that big of a fan to pearl so what
[222.36 --> 229.38]  do you say to those people who are not huge fans of pearl um i actually don't say anything to them i'm i
[229.38 --> 235.84]  understand that not everyone is going to be able to get into every language and pearl during the late
[235.84 --> 243.38]  1990s early 2000s was you know rightfully called the duct tape of the internet and as the market has
[243.38 --> 250.02]  grown and there was such a low barrier to entry we have a lot of competitors come in and for any
[250.02 --> 255.68]  healthy market of course it's going to shrink our market share and so for a lot of people who didn't
[255.68 --> 261.04]  care for the pearl syntax um they were happy to turn away from it so it's kind of sad because it's
[261.04 --> 265.60]  a fabulous language and we shouldn't let the punctuation characters in there turn people away
[265.60 --> 271.96]  from it but nonetheless you know people have their opinions and just as i understand that i also like
[271.96 --> 277.36]  other diverse languages i i enjoy python i enjoy ruby i i like prologue i think it's fascinating
[277.36 --> 282.76]  uh but i understand not everyone likes everything uh lisp i think is phenomenal language but
[282.76 --> 287.96]  i don't care to program it just because i just find it so frustrating and ugly when i play around
[287.96 --> 293.08]  with it no no offense to lisp programmers out there so i i don't really stress about it much i understand
[293.08 --> 299.26]  that it's not everyone's cup of tea so you've been doing pearl a long time you've written a book on
[299.26 --> 305.32]  pearl you have a consulting company that consults on pearl uh what is it about the language that you fell
[305.32 --> 314.08]  in love with it was an accident um in i think it was 1999 i was a mainframe programmer and i was
[314.08 --> 321.72]  working i was mostly doing cobalt development and one of cobalt's worst strengths is worst abilities is
[321.72 --> 327.00]  dealing with freeform text and that's pretty much all the web is incidentally which is why cobalt even
[327.00 --> 331.00]  though it's tried to it's never broken up the web and there was i was working on a program to
[331.00 --> 338.60]  convert nt csv files into the mainframe fixed width format that cobalt is really comfortable with
[338.60 --> 343.96]  and it was about 150 lines of code and there was a bug and someone didn't understand something called
[343.96 --> 349.66]  the unstring function something we would call split in many modern languages which splits a string on a
[349.66 --> 355.34]  character and i fixed it i got it down to i think like 80 lines of code and this unix sysadmin kept
[355.34 --> 361.46]  telling me you got to check out pearl so i checked it out and i got this 80 line cobalt function down
[361.46 --> 367.12]  to about 10 lines of pearl and that was with error checking and it was actually fairly readable and i
[367.12 --> 371.96]  was thinking my goodness what the heck am i doing and when he eventually left to form his own company
[371.96 --> 378.32]  he said come along i know you can do this and i haven't looked back though the ironic thing is i enjoy
[378.32 --> 384.96]  a lot of other programming languages i program in c assembler variants of basic java ruby python
[384.96 --> 392.18]  but i joined pearl right at the time of the dot-com collapse so i stuck around with pearl for so long
[392.18 --> 397.98]  that after the economy rebounded i found myself in a situation where people would see so much pearl
[397.98 --> 402.80]  on my cv either they didn't want to offer me a position or they would offer me a junior programmer
[402.80 --> 408.54]  salary so i wound up sticking with pearl and i've been specializing in it for about 15 years now
[408.54 --> 414.90]  it seems fitting that the the thing that brought you to pearl it seems to be its its best trait which
[414.90 --> 420.56]  is and what it was designed for right isn't it all about text extraction and manipulation that's
[420.56 --> 427.12]  initially what was going on larry wall uh the creator of pearl uh he originally released it in 1987
[427.12 --> 434.70]  and he was trying to handle a lot of problems that said and awk and other tools were supposed to be
[434.70 --> 440.28]  doing but he wanted to do it in one tool to make it very easy i believe for reporting for nasa as i
[440.28 --> 447.02]  recall and then he eventually released pearl uh open source to the community pearl 1 in 87 and it just
[447.02 --> 454.30]  took off from there it was just so phenomenally easy to hack and pearl i mean today i often find myself
[454.30 --> 458.14]  writing quick bash scripts and as soon as they start to get complicated i say okay forget about
[458.14 --> 463.86]  this and i switch over to pearl because it makes things so easy but at the same time i also specialize
[463.86 --> 470.72]  in extremely large scale uh websites you know database driven uh that use pearl almost exclusively
[470.72 --> 476.26]  as the back end so it's everything from the really tall blue really small blue things that we have
[476.26 --> 480.96]  to the very large scale websites some of the largest e-commerce platforms in the world are driven
[480.96 --> 487.76]  with pearl and it's just amazing how easy it is to shift back and forth like in java i'm not going
[487.76 --> 493.66]  to use java to hack out a small uh small utility for gluing things together it just wouldn't make any
[493.66 --> 499.30]  sense at the same time uh tickle might be great for you know a lot of smaller tools but a lot of people
[499.30 --> 505.22]  complain it doesn't scale as well though again no offense to the tickle community um so it's it just
[505.22 --> 510.92]  really feels fills a sweet spot for me of being able to solve virtually all of what i tend to do
[510.92 --> 518.58]  on a daily basis one of the uh the biggest pearl advocates and fans that i know on the podcast scene
[518.58 --> 523.94]  is john saracusa who um writes pearl you know professionally to this day and loves the language
[523.94 --> 528.74]  and one of the things that he says that's interesting and maybe you can tell me if this uh resonates with
[528.74 --> 535.82]  you is that pearl is really kind of a formalization of the unix way and kind of uh taking those ideas
[535.82 --> 541.00]  of those small tools and those command line tools and wrapping them in kind of a nicer uh language
[541.00 --> 546.62]  is that does that resonate with you or yes it does and i'm actually going to go back to cobalt for just
[546.62 --> 550.84]  a moment if you don't mind there's a reason for that so one of the things fascinating about cobalt
[550.84 --> 557.22]  what made cobalt so powerful and why it stuck along stuck around for so long is because cobalt's not very
[557.22 --> 561.80]  good it's not very powerful it's hard to write big systems in cobalt so what you do is you write
[561.80 --> 566.26]  a small cobalt utility which maybe reads some records from an isam database and stores them
[566.26 --> 572.40]  in the file but you have jcl job controlling which kind of it's tough to describe it doesn't really
[572.40 --> 576.72]  have a good analogy today but jcl would have different steps so you call a step which would
[576.72 --> 581.62]  read that a cobalt program which read the data saved to a file you call another step which would sort
[581.62 --> 586.76]  that file and then the next step might load another program which would read that file
[586.76 --> 592.96]  add some more data in save it and then you call another one which would take that saved file
[592.96 --> 598.64]  pass it on to another system basically it was a unix pipeline and that's part of what made cobalt
[598.64 --> 603.88]  so incredibly powerful because it wasn't powerful so people built a lot of small decoupled tools
[603.88 --> 610.66]  and kind of piped them together with jcl so that worked out very well for me when i was transitioning
[610.66 --> 616.24]  into pearl initially and getting used to the unix model because it was used to the way my mind
[616.24 --> 623.36]  already worked build small tools pipe them together so that's part of the reason why yes i write a lot
[623.36 --> 628.72]  of bash i write a lot of small bash utilities to get stuff done but anytime it starts to become
[628.72 --> 634.10]  painful and bash and anyone who's done enough bash scripting knows what i mean i just switch to pearl
[634.10 --> 639.80]  and i can do the same thing and it winds up being it's not quite as simple as bash but once you get
[639.80 --> 644.06]  to the stuff that bash is you know a little bit weaker on or maybe my bash knowledge isn't as good
[644.06 --> 649.88]  in pearl just makes it so easy to glue all these different tools together to shell out to some of
[649.88 --> 655.60]  their program fetch its results uh you know fork off multiple processes run a whole bunch of stuff
[655.60 --> 661.80]  aggregate them together and push it out there it's just it's lovely it's simple and you know from
[661.80 --> 667.12]  scaling down to that small scale the really tiny things you do up to the big large scale systems
[667.12 --> 673.66]  it's just it's always amazed me how seamlessly it tends to do that let's talk about some of those
[673.66 --> 678.50]  the large scale systems you speak of um do you know any off the top of your head that are like
[678.50 --> 682.24]  you know well-known sites that people may not realize are actually powered by pearl in the back
[682.24 --> 686.08]  end uh depends upon what other people would think of as a well-known site so i live in europe
[686.08 --> 694.18]  and one of the well-known sites over here is booking.com uh until the ipo of alibaba they were the third
[694.18 --> 699.98]  largest e-commerce site in the world after amazon and ebay i mean they're huge they're not as well
[699.98 --> 704.78]  known in the united states but basically they're an online hotel reservation system and they're massive
[704.78 --> 710.44]  and yet almost the entire back end is written in pearl and i remember when i was working for them
[710.44 --> 716.56]  one of my first days there i was walking by this guy and he was hacking on some java and i was surprised
[716.56 --> 721.24]  and i said what are you doing java programming what do we do with java here and he said well we don't
[721.24 --> 725.44]  we're taking all of our java programs and we're converting them to pearl just because it's easier
[725.44 --> 731.58]  to work with which i found rather ironic because sometimes you hear about it going the other way
[731.58 --> 735.24]  around people are converting pearl some of the language and here they're converting from some of
[735.24 --> 739.82]  their language into pearl and it's something very common for them but they just found pearl so easy to
[739.82 --> 747.18]  work with so that's possibly the biggest uh company i know of i work for the bbc also um world's largest
[747.18 --> 753.98]  broadcaster they had 26 000 uh people when i was there and i was working on the central metadata
[753.98 --> 759.50]  repository which basically that was information about you know what their schedules were what
[759.50 --> 765.34]  programs were on telly and i found it rather ironic that me an american who didn't watch tv was telling
[765.34 --> 771.10]  the british people what tv they were going to watch and all of that was managed through their pip system
[771.10 --> 779.46]  all written entirely in pearl and just many many companies like that crowd tilt now known as tilt.com
[779.46 --> 786.26]  which is a popular crowdsourcing system is written entirely in pearl there's actually an mmorpg called
[786.26 --> 792.74]  lacuna expanse which has been written in pearl lots of large-scale systems some are well-known some are less
[792.74 --> 798.98]  well so there's a lot of it out there um yes man it's been a long around a long time there's a lot of it
[798.98 --> 803.92]  out there it has a lot of virtues what is it about it it seems like it's behind it seems like pearl's
[803.92 --> 810.24]  behind the scenes is it just bad marketing or um is it just communities that you know don't necessarily
[810.24 --> 817.08]  overlap uh you know we keep our our thumb on open source and you know we have to go out of our way to
[817.08 --> 821.52]  find pearl open source even though it has been from the very beginning so is it what is it about pearl
[821.52 --> 828.82]  the community is it just small or is this just not vocal um why it's not better known in the
[828.82 --> 836.72]  greater open source community at one time it was obviously late 1990s early 2000 as i mentioned
[836.72 --> 842.48]  pearl was known as the duct tape of the internet because it was virtually everything that you wanted
[842.48 --> 846.72]  to know on the web you know if it wasn't written directly in pearl pearl was supporting behind the
[846.72 --> 851.50]  scenes and that's still often surprisingly true today i work for a number of different companies
[851.50 --> 856.04]  they call me in for all sorts of consulting things and i'm finding pearl all over the place but
[856.04 --> 864.56]  i think part of what happened was uh back around uh around 2000 2001 there was kind of a malaise in
[864.56 --> 870.22]  the pearl community um internally they were still trying to work out some differences um some folks
[870.22 --> 875.50]  were frustrated and there was a famous incident when john orwatt threw a mug at the wall shattered it
[875.50 --> 881.18]  and said we've got to do something different and then the pearl 6 project was born and there was a
[881.18 --> 885.78]  misunderstanding from the beginning it was decided that pearl 6 would be the successor to pearl
[885.78 --> 891.14]  but then it was quickly realized that it couldn't be the successor to pearl and said it would be a
[891.14 --> 896.42]  sister language just as you have you know c sharp is a sister language to java c plus plus is kind of a
[896.42 --> 904.10]  sister language to pearl pearl 6 is a sister language to pearl 5 and a lot of people simply see pearl 5 and
[904.10 --> 910.10]  they don't realize that we have major releases um every year or so um new features powerful features
[910.10 --> 916.14]  being introduced all the time but people just keep seeing pearl 6 and they're not aware that you know
[916.14 --> 921.44]  development's still continuing on pearl 6 that pearl 5 is still tremendous progressing at a tremendous
[921.44 --> 927.64]  pace and internally i actually was doing a lot of work with marketing with pearl and i discovered a
[927.64 --> 932.76]  tremendous amount of hostility from the pearl community for marketing itself um they were just happy
[932.76 --> 939.46]  to sit back and get stuff done and that kind of caused a problem so people outside think that
[939.46 --> 945.06]  pearl 6 is a successor and therefore pearl 5 isn't going anywhere when that's absolutely not true we're
[945.06 --> 951.38]  on pearl 520 right now pearl 522 um you know it's going to be out fairly soon new features being added
[951.38 --> 958.90]  all the time um powerful features and it's a great language but we don't do a great job of talking about
[958.90 --> 964.46]  outside of the community it sounds like some misinformation there sort of stouts you a little bit because
[964.46 --> 970.42]  you want to you obviously want to progress but you don't want to stop the progression and and be like
[970.42 --> 977.10]  that pearl 5 is not going anywhere can you talk a bit about beyond that the the health aspects i guess of
[977.10 --> 984.34]  of of 5 versus 6 or where that's you know what some of the biggest issues are around this 5 versus 6 transition
[984.34 --> 990.28]  well they're entirely separate languages that needs to be understood first of all as i mentioned
[990.28 --> 996.62]  they're sister languages like c shark or java c plus plus two so it's a right turn to lisp yes um
[996.62 --> 1002.72]  there is some work being done to make pearl 5 run inside of pearl 6 but it needs to be understood that
[1002.72 --> 1008.02]  they're not the same language so because we haven't done a great job of communicating that outside and
[1008.02 --> 1014.22]  because a lot of people just see that pearl 5 was released um that was actually back in 1994
[1014.22 --> 1021.46]  that pearl 5 was released uh that was 20 years ago so people aren't aware that pearl 5 20 is not the
[1021.46 --> 1031.16]  same language as pearl 5 pearl 5 code will generally run with a lot of warnings in 5 20 but 5 20 and the
[1031.16 --> 1035.78]  supporting libraries that are available for it such as moose probably the most advanced object-oriented
[1035.78 --> 1040.96]  system you're going to find in any dynamic language today and possibly more advanced than most static
[1040.96 --> 1047.00]  languages i would say fan fabulous tool i i miss that when i program in anything else there are such
[1047.00 --> 1052.12]  wonderful things available for pearl 5 but people outside the community aren't aware of that i would
[1052.12 --> 1057.04]  like to see the pearl community we've done a great job over the past few years of internally getting our
[1057.04 --> 1062.10]  act together healing you know pushing things forward after that malaise of people internally not
[1062.10 --> 1068.24]  understanding the pearl 5 pearl 6 split um but it would be it would be great if we can communicate
[1068.24 --> 1074.54]  that better outside because if people outside of pearl aren't aware of how powerful it is the powerful
[1074.54 --> 1079.62]  web frameworks orms and other tools that we have uh you know we drive a lot of what's called the bio
[1079.62 --> 1083.58]  pearl movement so there's a lot of biological work the research being done with pearl if people
[1083.58 --> 1090.06]  outside aren't aware of that it's harder for them to make the decision to choose that let's pause the show
[1090.06 --> 1094.62]  for just a minute give a shout out to a sponsor rack space has been helping us out they love open
[1094.62 --> 1100.56]  source we love open source uh we've been working with rack space for the past year and uh one of the
[1100.56 --> 1104.52]  things they keep telling me is how much they love open source and that's why they keep sponsoring the
[1104.52 --> 1109.52]  show and making sure that you know how much they care about it and that's also why they're giving you
[1109.52 --> 1116.66]  and everyone else who wants it 50 a month in credit for 12 months that's right 50 a month in credit
[1116.66 --> 1121.92]  for 12 months to explore their open cloud all you got to do is create a developer plus account to get
[1121.92 --> 1128.26]  started go to the changelaw.com slash rack space to get started you get dev to dev support so if you
[1128.26 --> 1133.88]  got complex questions you can talk directly to their developers about their sdks and their apis
[1133.88 --> 1140.08]  they have various services included like monitoring dns auto scaling orchestration private networking the
[1140.08 --> 1146.24]  list goes on there is no usage limits you can use your services as much as you want and you're only
[1146.24 --> 1152.80]  billed for usage beyond 50 a month again they're giving away 50 a month in credit for 12 months
[1152.80 --> 1159.20]  go to the changelaw.com slash rack space to get started and now back to the show yeah something
[1159.20 --> 1162.74]  we have in our notes here too it's i'm going to quote this back to you because this is what you
[1162.74 --> 1168.12]  said you said the pearl community and you've said this too here in the show just not as succinctly as
[1168.12 --> 1172.80]  this um you said the pearl community has been stunningly bad at marketing in this area meaning
[1172.80 --> 1179.82]  um you know this divide between pearl 5 and pearl 6 and just in general what pearls is going to do
[1179.82 --> 1184.48]  today and what it's doing today and jared i think that's something maybe we can even possibly help out
[1184.48 --> 1189.96]  with like you know curtis you mentioned in the bio information you know different areas where pearl
[1189.96 --> 1194.80]  is doing some cool stuff i think it's neat how the changelaw can kind of step in and have curtis on the
[1194.80 --> 1200.50]  show and and talk to you know what probably is we have a large ruby audience a large javascript
[1200.50 --> 1206.30]  audience um to to some people who don't often look at pearl and say oh that's that's neat we should
[1206.30 --> 1213.80]  try that out but maybe there's a a space here where there's some interest to peek up how great is the
[1213.80 --> 1220.66]  divide between the two as far as you know sister languages are they syntactically very similar
[1220.66 --> 1227.92]  or they have huge differences um was pearl 6 was just a huge undertaking uh is it used in production
[1227.92 --> 1232.80]  i'm just having tons of questions pour out of me here uh pick ovid pick any of those and just run
[1232.80 --> 1239.72]  with it because i got so many questions now so if you were to look at maybe an interesting example
[1239.72 --> 1245.92]  would be there are many people who criticize pearl they're unhappy with it people who don't know pearl
[1245.92 --> 1250.52]  they look at it and they just see a bunch of sigils of punctuation characters all over
[1250.52 --> 1256.26]  place many of these people could look at pearl and php and not tell you which is which they're not
[1256.26 --> 1260.40]  going to say anything about php they might have different complaints about php about you know how
[1260.40 --> 1265.84]  it's kind of ad hoc you know unclear interfaces but for the uninitiated you won't see a difference
[1265.84 --> 1270.80]  and yet many people will turn to php over pearl simply because it's just ubiquitous on web servers
[1270.80 --> 1277.20]  and it's so quick and easy to get things started with php uh pearl is extremely powerful um i think in
[1277.20 --> 1282.08]  many respects i i would definitely prefer pearl over php not just because i know it so well but
[1282.08 --> 1285.02]  there's some benefits to some of the things it does i'm not going to get into it i don't want to
[1285.02 --> 1290.08]  fight between languages php is a great thing because it does other stuff well but if you can't tell the
[1290.08 --> 1296.74]  difference from the outside then if you're in the inside you can easily tell the difference for pro 5 and
[1296.74 --> 1301.50]  pro 6 from the outside it's a little bit harder to tell the difference until you start getting into
[1301.50 --> 1305.86]  some of the more advanced features from the inside you're going to see huge differences so they're
[1305.86 --> 1310.92]  definitely sister languages so you would look at pearl 5 code and there's a lot of pearl 5 code
[1310.92 --> 1316.74]  which if it's written carefully will run the same under pearl 6 but the differences quickly diverge in
[1316.74 --> 1322.56]  the cleaner syntax of pearl 6 something we call invariant sigils which really solves a lot of the
[1322.56 --> 1330.02]  problems that new developers in pearl 5 had a lot of the things that are add-ons to pearl 5 today
[1330.02 --> 1335.74]  such as meta programming roles which is probably the greatest advancement object-oriented
[1335.74 --> 1341.18]  programming since simula 67 almost 50 years ago that's going to be baked into the language so many
[1341.18 --> 1348.16]  powerful things about it which either don't exist directly in pearl 5 or would be very hard to implement
[1348.16 --> 1354.04]  tell us about that over this roles thing okay roles this comes from smallpox style traits
[1354.04 --> 1360.50]  and there was a paper called um a brief introduction to traits i believe is the name and it was an
[1360.50 --> 1367.06]  introduction to solving a long-standing problem we had with uh object-oriented programming so in 1967
[1367.06 --> 1373.48]  simula 67 was released and that had classes inheritance polymorphism uh encapsulation and people generally
[1373.48 --> 1381.16]  agreed about all of that except for inheritance inheritance was such a problem so many languages allow
[1381.16 --> 1388.36]  multiple inheritance such as c++ and others but you're often warned not to actually use it other languages such as
[1388.36 --> 1395.66]  java ruby and others say okay multiple inheritance is such a problem we're not going to allow that at
[1395.66 --> 1400.46]  all but here's the alternative and they actually encourage the alternative the problem is the
[1400.46 --> 1407.32]  alternatives such as mixins interfaces yep they have so many built-in problems themselves that they
[1407.32 --> 1412.66]  didn't actually solve the underlying problem so the traits researchers we call them roles in pearl because
[1412.66 --> 1418.32]  traits is actually a term for a different thing what the traits researchers did is they were
[1418.32 --> 1422.66]  funded to investigate the problem come up with solution and what they discovered was classes actually
[1422.66 --> 1429.60]  have two roles as an agent of responsibility your employee class as your system grows has to take
[1429.60 --> 1436.54]  on more and more and more behavior but if you're going to inherit from your employee class then it's an
[1436.54 --> 1441.54]  agent of code reuse and quite often for code reuse we don't want all that behavior we just want little
[1441.54 --> 1446.72]  specific bits and pieces and in fact there's a language called beta which was going to implement
[1446.72 --> 1451.16]  multiple inheritance but when they researched it they found out that almost everyone using multiple
[1451.16 --> 1455.48]  inheritance wasn't for creating more specialized classes it was just to pull out bits and pieces of
[1455.48 --> 1461.04]  parent classes so the reality is for code reuse you actually want smaller code because you just want to pick
[1461.04 --> 1466.06]  out the bits and pieces you need but for class responsibility you need all of that so classes actually serve
[1466.06 --> 1473.40]  to do a role reuse and responsibility and the problem we've had with inheritance and the solutions such as
[1473.40 --> 1481.60]  interfaces and mixins has been you need to decouple those so roles has decoupled them entirely and so classes are
[1481.60 --> 1486.48]  agents of responsibility so an employee might have an employee number but does an employee know how to
[1486.48 --> 1494.88]  serialize itself to xml or json no it doesn't this is a bit of behavior which could be shared amongst classes
[1494.88 --> 1501.06]  which are not necessarily related by inheritance so ruby mixins which actually came from a variant of
[1501.06 --> 1508.90]  lisp called flavors ruby mixins actually properly separate behavior from responsibility but unfortunately
[1508.90 --> 1515.80]  they implemented it via single inheritance so if you mix in a couple of modules into your ruby code and
[1515.80 --> 1521.36]  then you call ancestors you'll find that it's implemented as a single inheritance tree and then you wind up with
[1521.36 --> 1526.90]  strange bugs so in if you have duplicate methods in multiply inherited classes the first class you
[1526.90 --> 1535.06]  inherit from generally wins in ruby the last mixin that you've mixed in wins with roles it's completely
[1535.06 --> 1540.10]  different it says oh i'm sorry you have duplicate methods they have the same name it's going to fail
[1540.10 --> 1544.74]  at composition time close enough to the pile time most people won't notice the difference it'll fail
[1544.74 --> 1549.58]  composition time says i don't know which of these methods you need so you specifically say i want this method
[1549.58 --> 1556.76]  from this role i want this method from that role and you don't have any of those composition issues
[1556.76 --> 1561.90]  that you have with multiple inheritance or mixins or some of the other solutions which are out there
[1561.90 --> 1567.68]  there's a lot more i can say about them but this is one of the finest things about roles it cleanly
[1567.68 --> 1573.36]  separates class responsibility from code reuse and more and more developers are finding out that you can
[1573.36 --> 1579.12]  eliminate inheritance entirely and build an entire large-scale object-oriented system just by
[1579.12 --> 1584.16]  composing different roles and saying i want this behavior that behavior the other behavior and you
[1584.16 --> 1588.52]  get composition safety because you don't have to worry about method conflicts anymore you don't have
[1588.52 --> 1592.56]  to worry about accidentally inheriting a method that you didn't realize that you were inheriting
[1592.56 --> 1599.64]  and it makes things so much simpler it sounds like a pretty big win so is that available in pearl 6 today
[1599.64 --> 1604.80]  it's available in pearl 6 today it's available in pearl 5 via something called moose roles there's some
[1604.80 --> 1610.14]  other role modules out there i have one myself which is actually goes back to the original research
[1610.14 --> 1617.46]  on this there's some guarantees that roles actually provide such as being commutative and associative
[1617.46 --> 1622.84]  basically mathematical guarantees to get around some of the issues that you had with inheritance and
[1622.84 --> 1630.90]  mixins and different systems meet those guarantees in different ways but it's available out there but many
[1630.90 --> 1635.30]  other languages have this i know there's been some experiment with java to do this there's been
[1635.30 --> 1642.30]  some experiments with python to do this i'm pretty sure it's available in ruby javascript has something
[1642.30 --> 1647.36]  i believe called juice which i had heard about i don't know how far along that is which also
[1647.36 --> 1654.20]  makes roles available so there's a wide variety of languages which have adopted it but you know how much
[1654.20 --> 1658.12]  people are actually using it it's hard to say but the pearl community has bought into it wholesale
[1658.12 --> 1663.00]  because it tremendously simplifies your code and makes it much easier to understand
[1663.00 --> 1670.10]  pearl 6 sounds very it sounds very experimental and research oriented is it run by the same group
[1670.10 --> 1678.12]  of folks that are doing the pearl 5 stuff or are they also diverged um yes and no does that help
[1678.12 --> 1685.94]  uh nope please explain i'm glad i can clarify that so lary wall the founder of pearl um has shifted
[1685.94 --> 1692.38]  focus from pearl 5 to pearl 6 and many people now call pearl 6 rakudo just to distinguish it from
[1692.38 --> 1700.58]  pearl 5 would you say rakuda rakudo r-a-k-u-d-o interesting earlier on i was thinking man maybe it just
[1700.58 --> 1706.34]  needs a separate word like a separate term altogether yes and i would like to see that term adopted a
[1706.34 --> 1712.30]  little bit more widely but yeah there's there's a lot of background to that um and pearl 6 the name's
[1712.30 --> 1717.20]  been around for so long that they've stuck with it right so there's that marketing thing about you
[1717.20 --> 1723.42]  know don't shift your name because you'll lose people so possibly that's some of it yeah anyways
[1723.42 --> 1729.76]  you were saying so larry wall uh has shifted his focus from pearl 5 to pearl 6 and has been pushing
[1729.76 --> 1736.84]  it forward and it's just making tremendous strides damian conway uh he wrote uh pearl best practices and
[1736.84 --> 1740.68]  quite a number of other excellent books uh involving pearl including object-oriented pearl
[1740.68 --> 1747.20]  and he has also been doing a huge amount of work with this but many people such as uh patrick michaud
[1747.20 --> 1753.74]  who was heavily involved with php and others carl msak many others have been heavily involved in
[1753.74 --> 1760.26]  pushing pearl 6 along jonathan worthington he was a pearl 5 hacker but mostly focuses on pearl 6 now and
[1760.26 --> 1764.46]  he's been doing a lot of work putting it on the jvm and writing something called more vm
[1764.46 --> 1770.42]  so there's now originally it was a bunch of pearl 5 hackers now there's a completely separate
[1770.42 --> 1775.16]  community of people from a variety of different backgrounds many of them academic many of them
[1775.16 --> 1780.14]  uh basically you know heavily involved in the real world who have been building pearl 6 many of whom
[1780.14 --> 1787.00]  have no background in pearl 5 anymore so is pearl 6 out there in production or is it still kind of at a
[1787.00 --> 1792.30]  at an experimental phase i do know there are some folks who have been using it in production
[1792.30 --> 1798.76]  generally they're using this for smaller tools the sort of small tools that you might uh build shell
[1798.76 --> 1803.34]  scripts for because that's a little bit safer a little bit lower risk uh large-scale systems
[1803.34 --> 1810.64]  are generally not being built in pearl 6 yet um there is more work to be done with the final work for
[1810.64 --> 1817.88]  porting it to more vm and the jvm to finally get a production ready there's more i can say about that
[1817.88 --> 1824.90]  but i don't know how much i'm actually allowed to say uh simply because um for the long time
[1824.90 --> 1829.00]  pearl 6 has always been promised by christmas but we just don't say which one
[1829.00 --> 1835.00]  yeah i'm reading some commentary behind the scenes here just sort of listening to you by the way i love
[1835.00 --> 1841.98]  that explanation of roles versus inheritance that was um really great but some some thoughts here from
[1841.98 --> 1847.90]  reddit i'm not sure that's the best place to go for thoughts but um it seems like people have this
[1847.90 --> 1852.36]  huge question in the brook community about what's happening worth pearl 6 then even specifically
[1852.36 --> 1859.02]  larry wall you've mentioned a couple times and whether or not it's uh they've questioned um the code
[1859.02 --> 1865.50]  quality uh or sorry the language designs not so much code quality but uh some other things happening
[1865.50 --> 1870.84]  there it seems like stepping back to earlier you mentioned this you know maybe it's not so much
[1870.84 --> 1875.18]  marketing maybe it's communication and that's where i feel like having you on the show today and
[1875.18 --> 1880.24]  just sort of getting this bird's eye view from uh someone inside the community that's been there for a
[1880.24 --> 1886.04]  while that's sort of as you said uh by accident to a degree a happy accident that you can sort of
[1886.04 --> 1891.86]  disseminate this idea of what pearl 6 is going to be and what profile is doing currently because
[1891.86 --> 1898.62]  uh to rewind just a tiny bit you mentioned you had a role a role um roles and pearl and i believe
[1898.62 --> 1906.46]  it's role basic is that your is that your version of roles yes there's there's a second traits paper
[1906.46 --> 1912.58]  um let me see the typed calculus no a traits the formal definition i think is the name which despite
[1912.58 --> 1918.56]  the name is actually a fairly easy to read paper which unfortunately i consider to be the traits paper
[1918.56 --> 1923.70]  that no one has ever read but should um and it's absolutely fantastic and it clears up a lot of the
[1923.70 --> 1928.60]  communication i've actually spoken with a number of traits researchers to clarify some of the issues in there
[1928.62 --> 1935.34]  um and traits themselves still have some issues um i should call them roles just because that's what
[1935.34 --> 1940.40]  pearl does they still have some issues because this is programming and in programming we don't have
[1940.40 --> 1945.56]  perfect systems anywhere but they are the best thing to come along and i have worked with you know so
[1945.56 --> 1951.18]  many alternatives and they do solve so many problems but yes i wrote role basic in an attempt to
[1951.18 --> 1958.44]  create a system that goes back to the original definition and truly respects uh some of the rules
[1958.44 --> 1964.92]  such as uh you know being commutative and associative for example if you have a role which uh does json
[1964.92 --> 1973.18]  serialization and you have a role which uh does i don't know yaml serialization and if you compose
[1973.18 --> 1979.18]  both of those roles they should it doesn't matter which order you compose them in unlike you know inheritance
[1979.18 --> 1986.90]  or mixins it's guaranteed you get the same behavior technically it is possible to violate this contract
[1986.90 --> 1995.06]  uh with roles or if you have the role which does json serialization consumes another role which does
[1995.06 --> 2002.70]  marshalling um you might just decide no i'm going to consume my does marshalling role and that is going to
[2002.70 --> 2008.30]  consume the does json and does yaml role so i'll get all of the serialization methods all at once
[2008.30 --> 2014.66]  but in theory according to the original traits research it doesn't matter how you consume those
[2014.66 --> 2020.60]  how you mix and match those in roles it is possible for that contract to be violated depending upon how
[2020.60 --> 2027.44]  you do it it's unusual for this to happen and you know dedicated programmers who know that you know
[2027.44 --> 2031.38]  different methods should actually have different method names are really good about avoiding those
[2031.38 --> 2037.80]  problems but there are still some subtle edge cases but they are in my experience more than an order
[2037.80 --> 2044.44]  of magnitude less than you have the edge cases with mixins and inheritance so you probably do most of
[2044.44 --> 2051.56]  your programming in pearl 5 right yes and this role basic is that what you use for your roles or because
[2051.56 --> 2055.70]  you said this is your version of it there was another one out there you mentioned um but i didn't catch
[2055.70 --> 2063.00]  that one though i use uh there's also a role tiny i use almost exclusively moose role because moose is
[2063.00 --> 2067.64]  the most fully fledged object-oriented system out there and i'm not just talking about for pearl
[2067.64 --> 2074.54]  moose is it brings a lot of the power of you know what we would typically associate with static languages
[2074.54 --> 2081.70]  to dynamic languages so when i declare an attribute such as social security number i can say a social
[2081.70 --> 2086.14]  security number is a and then i can define a very rigid type constraint for what that social security
[2086.14 --> 2090.42]  number is and rather than you know embedding my code with a whole bunch of type checks everywhere
[2090.42 --> 2093.96]  you know is a social security number really fitting the format of social security number
[2093.96 --> 2099.68]  are the first three digits allowed first three digits or not i can simply declare a social security
[2099.68 --> 2103.62]  type have that provide the validation and anything which consumes a social security number
[2103.62 --> 2109.82]  it has to match that type or it's going to fail and this is something you often don't get
[2109.82 --> 2115.68]  with many dynamic languages we tend to play fast and loose with our data but there's so many powerful
[2115.68 --> 2121.52]  things you can do such as lazy evaluation of attributes so you don't create the connection
[2121.52 --> 2126.90]  to the database unless you actually ask for the connection to the database or you know just being
[2126.90 --> 2130.82]  able to list all of your attributes but on top of that you have meta programming so i use meta
[2130.82 --> 2136.84]  programming quite heavily i built something called test class moose which is basically a an x-unit framework
[2136.84 --> 2143.48]  for large scale enterprise class databases if you will and it's being used more and more and what
[2143.48 --> 2150.56]  what i've done with the metadata system within moose is i'm able to inspect the methods to figure out
[2150.56 --> 2155.28]  what test methods are available i'm able to find out what attributes are available i'm able to compose
[2155.28 --> 2160.66]  roles into things so i can have roles defining fixtures so i can easily load fixtures on demand
[2160.66 --> 2167.70]  and if you've never played with meta programming before it is hard to appreciate the power of it
[2167.70 --> 2173.06]  and once you play with meta programming you never want to go back because it makes so many of your
[2173.06 --> 2181.14]  problems so much simpler the cost is the software you build is simpler it is easier to write it is
[2181.14 --> 2185.52]  faster right it's a little bit harder for some other people to understand it because most people
[2185.52 --> 2192.26]  don't understand the concept of meta programming at first it sounds like you uh also i mean you
[2192.26 --> 2196.48]  mentioned testing here a few times in that conversation obviously when you're meta programming
[2196.48 --> 2201.78]  and when you have dynamic languages um testing becomes a huge part of that you know assurance that
[2201.78 --> 2206.38]  things are still working the way that you wanted them to um you said you wrote a test harness that
[2206.38 --> 2211.68]  ships with the language um maybe tell us about the testing story in the pearl community whether it's
[2211.68 --> 2216.52]  tdd style or uh kind of what the just what the community looks like and as far as testing code
[2216.52 --> 2222.94]  goes pearl has possibly i mean ruby talks about themselves just being test infected and they have
[2222.94 --> 2230.86]  nothing on pearl if so cpan the um this is the central archive of pearl code that most developers tend
[2230.86 --> 2237.94]  to push their code towards and if i push my code up to the cpan it's immediately pushed out to the cpan
[2237.94 --> 2243.94]  testers network where people are running the tests for my code on all sorts of different flavors of
[2243.94 --> 2250.18]  linux all sorts of different flavors of windows all sorts of different macs uh on aix on solaris you
[2250.18 --> 2254.00]  name it my code is being tested there with tons of different operating systems tons of different
[2254.00 --> 2258.12]  versions of pearl and i find out very quickly which operating systems which versions of pearl
[2258.12 --> 2265.24]  my tests are failing on and this is for free and this is the sort of thing that enterprise
[2265.24 --> 2272.10]  customers can pay hundreds of thousands of dollars a year for right and there are millions and millions
[2272.10 --> 2278.08]  literally of test reports out there on cpan testers and when you go out there and you pull up
[2278.08 --> 2284.24]  one of the versions of your module and you know my version of this module you know 1.14 happens to fail
[2284.24 --> 2291.72]  on solaris with pearl 516 and then you can go and if you've written your tests well for printing out
[2291.72 --> 2296.36]  good explanations of what's going on with your test you can say oh now i understand what's failing
[2296.36 --> 2300.88]  and even if you don't know solaris you can contact a solaris user or perhaps a person who originally
[2300.88 --> 2306.52]  ran it on their what we call smoke machines they're smokers and say my module failed on your machine with
[2306.52 --> 2311.44]  this version of pearl can you help me with this and you get this powerful free feedback that is
[2311.44 --> 2318.12]  virtually impossible to get otherwise and anytime i upload a new module to the cpan i get hundreds and
[2318.12 --> 2325.76]  hundreds of test reports coming back very quickly and it's just phenomenal and i don't see that other
[2325.76 --> 2331.52]  places if i want to install a module on my local machine i can have the option to run the tests or
[2331.52 --> 2337.44]  not so if i want to run the tests i can see what's going on i can give feedback to the module authors it's
[2337.44 --> 2343.20]  very easy and it's gotten to the point it's very very much frowned upon for popular modules to be
[2343.20 --> 2349.20]  uploaded to cpan without tests and the test coverage is just phenomenal in many of these
[2349.20 --> 2354.60]  modules and it really it's nice for me as a developer when i'm recommending you know use this
[2354.60 --> 2359.34]  new module in your code base because it's going to save you a lot of time and trouble and they say
[2359.34 --> 2363.98]  well is it robust and i can say look at this test suite look at all these test results and all these
[2363.98 --> 2368.76]  different operating systems all these different versions of pearl look at all those green bars there
[2368.76 --> 2374.82]  and it's just fantastic so i love it makes me very happy i did not know that about cpan that
[2374.82 --> 2381.86]  tester what do you call it the test smokers uh the smokers um it's oh my goodness i'm trying to
[2381.86 --> 2388.72]  remember the name um it's something that i've taken for granted for so long to be quite honest uh the
[2388.72 --> 2395.82]  cpan reporters um i would have to go and look up the url offhand but it's you know you can go out
[2395.82 --> 2399.72]  there very quickly and see all of the test reports which are available for all of your modules but
[2399.72 --> 2404.86]  this is free and anything anyone uploads is automatically run through the system by just
[2404.86 --> 2409.84]  dedicated volunteers so it's not something you have to sign up for it's not something you have
[2409.84 --> 2415.58]  to ask for it just automatically happens for you that's awesome you know when i was back in college
[2415.58 --> 2421.12]  and i was doing some pearl um i liked the language i still like it to this day i think you know i saw the
[2421.12 --> 2426.38]  the value especially in the regular expression stuff back then that just was so easy comparative
[2426.38 --> 2432.48]  to what i had done previously um and cpan was always boasted as you know this great thing now as
[2432.48 --> 2439.40]  a fledgling young programmer i'm probably like 2001 2002 man i just could not figure cpan out um i
[2439.40 --> 2443.54]  couldn't even get past like the configure step to get that thing out there i'm just trying to get
[2443.54 --> 2449.44]  somebody else's code on my system um and i'm sure it's an isolated incident but maybe give us
[2449.44 --> 2455.62]  um some background on cpan i know that it's it's much touted as as a great system it sounds like
[2455.62 --> 2461.30]  that the automated testing thing is really cool tell us more about it so the cpan is a comprehensive
[2461.30 --> 2467.52]  pearl archive network and there's a module cpan.pm which comes shipped core with pearl so when you
[2467.52 --> 2474.36]  first download pearl you can run the cpan command cpan all over case and what you experienced was a
[2474.36 --> 2479.74]  a long-standing problem today what it does is it says oh this is the first time you're running cpan
[2479.74 --> 2484.36]  would you like me to configure as much as i can automatically you hit yes and it magically works
[2484.36 --> 2493.08]  that sounds great so that's not what i was having i know yeah basically they they took the trouble to
[2493.08 --> 2498.12]  make the pain go away so i often install new versions of pearl i'm playing around with different things
[2498.12 --> 2503.94]  i set up cpan for the first time and if i select yes um occasionally it might pick a mirror too far
[2503.94 --> 2511.74]  away from me but aside from that it works beautifully and it's not a problem you also have cpan minus
[2511.74 --> 2520.50]  so app cpan so cpan min dot us um that's the site which has a very simple that has a very simple
[2520.50 --> 2525.70]  command that you can run which will allow you to install cpan minus which is kind of like cpan
[2525.70 --> 2530.78]  except it does even less so cpan when it downloads your code it will download all the dependencies run
[2530.78 --> 2535.16]  all the tests and then you have some dependency failing on a test which is completely unrelated to
[2535.16 --> 2541.36]  what you're doing or cpan minus will just take all the pain away and just build your code and install
[2541.36 --> 2546.52]  it for you very quickly and it's very powerful and most of the time it just works wonderfully so we're
[2546.52 --> 2551.68]  actually winding up with multiple different solutions depending upon what your particular needs are how
[2551.68 --> 2555.98]  thorough do you want your test coverage to be are you not worried about that do you want to just
[2555.98 --> 2561.22]  install a simple module quickly most of it's just painless and people don't have to worry about it
[2561.22 --> 2566.24]  anymore so what you discovered was a long-standing complaint but it pretty much doesn't exist today
[2566.24 --> 2573.14]  cool cool i just loaded up cpan minus and it redirected me to a github page which makes me which
[2573.14 --> 2578.98]  makes me wonder like where are y'all at with git and github and having code be publicly available on those
[2578.98 --> 2585.60]  on on github at least yeah embarrassingly enough i just had the same thing yeah is that so is that
[2585.60 --> 2592.36]  not supposed to happen it wasn't happening a few days ago okay so that makes for a very awkward turn
[2592.36 --> 2601.04]  for this conversation or a or a perfectly intended turn yeah in our eyes so many pearl developers are
[2601.04 --> 2607.24]  heavily uh involved in using git so my company actually offers git training also just because it's
[2607.24 --> 2612.38]  incredibly popular and it was interesting that you know i would have svn available for the long time
[2612.38 --> 2617.50]  for the longest time and you know oh you can submit patches to my modules you know via svn or you know
[2617.50 --> 2623.54]  just using the diff patch command whatever um and i could count on the fingers of one hand the number of
[2623.54 --> 2629.92]  patches i would get per year since i switched to doing most of my development and sharing my code on github
[2629.92 --> 2636.02]  i'm getting patches all the time and it's just phenomenal and because the pearl community is very keen
[2636.02 --> 2643.84]  about testing and documentation i'm usually getting patches with full documentation full tests or if
[2643.84 --> 2647.68]  they don't have them people will say you know this is just exploratory to solve this little itch that i
[2647.68 --> 2652.70]  have what do you think and it's a way of collaboration that you know just didn't exist before and i'm very
[2652.70 --> 2657.68]  very pleased about that most of the pearl communities bought into it cool and are those integrated git and
[2657.68 --> 2664.90]  c or github and cpan as far as publishing goes you have you have what are called metafiles available
[2664.90 --> 2673.52]  in your distributions which can say um my bug queue is actually out on github the actual base repository
[2673.52 --> 2679.26]  is on github so if you go out to cpan and someone set up their metafiles correctly you can just click
[2679.26 --> 2684.20]  directly on the source repository and it'll take you over to you know github or click on the bug tracker
[2684.20 --> 2689.38]  instead of the built-in rt trackers that cpan uses it can take you over to the github track tracker
[2689.38 --> 2695.56]  or any other site you want it's not just tied into github specifically it's a generic system saying
[2695.56 --> 2702.08]  this is where my you know source repository actually is this is where my bug tracker actually is and it
[2702.08 --> 2707.48]  just handles it for you but it's very agnostic about the cpan isn't tied into github but it's
[2707.48 --> 2713.34]  probably the most popular alternative today we're gonna pause the show for just a minute give a shout out
[2713.34 --> 2719.88]  to a sponsor status page dot io is a new sponsor for us we're glad to have them it's all about
[2719.88 --> 2726.18]  transparency during downtime and the best way i know to do that is to use status page dot io to create a
[2726.18 --> 2732.14]  status page for your app or your website so you can have an always up and always on way to communicate
[2732.14 --> 2737.64]  to your customers when you're in a bad situation your customers can subscribe to updates you can
[2737.64 --> 2742.84]  broadcast upcoming maintenance windows you can post updates minute by minute hour by hour keeping
[2742.84 --> 2748.58]  everyone informed everyone on the know integration with services like new relic and pingdom allow you
[2748.58 --> 2753.04]  to show off graphs to your customers that they care about you can even embed your system status
[2753.04 --> 2759.36]  within your actual app head to status page dot io to get started it's free to set up launch it when
[2759.36 --> 2766.56]  you're ready and tell them the changelog sent you and now back to the show so as the cpan sort of act as a
[2766.56 --> 2772.76]  registry in that case then more like here's where pro modules go and you can find and install new
[2772.76 --> 2778.52]  pro modules via cpan is that how that works yes that is far and away the most popular option there's
[2778.52 --> 2787.02]  also metacpan.org um with the search right yes and some people like that some people don't uh myself uh i
[2787.02 --> 2792.40]  i think it's interesting but i'm so old school and i'm so used to search cpan.org that i don't even
[2792.40 --> 2797.84]  remember that there's a www cpan.org i just hit search cpan.org i look for the things that i want
[2797.84 --> 2803.86]  i read about them i read the test results i read the code yeah okay i'll use this so in your community
[2803.86 --> 2809.40]  or in your sorry in your opinion what is the the state of the community the pro community in terms of
[2809.40 --> 2815.32]  transitioning the open source work they do have out there to github because you said that
[2815.32 --> 2820.12]  earlier you do some get training and stuff like that what is the state of the pro community as it
[2820.12 --> 2826.82]  relates to github and open source on github and just general availability of of i think what we see
[2826.82 --> 2832.46]  over the last three or four years just more and more and more developers moving to github is just a
[2832.46 --> 2838.62]  a better way to socially code together and pearl's been open source since the beginning so it just seems
[2838.62 --> 2844.12]  like a natural fit for them y'all to eventually move there but what's the state the way it's working right
[2844.12 --> 2851.58]  now is most of the tool chain available for pearl is centered around cpan so cpan is a central
[2851.58 --> 2859.44]  repository for the canonical versions of modules and people use github for collaboration i have a
[2859.44 --> 2864.28]  number of modules which are available out on github for doing various things that i don't have the
[2864.28 --> 2868.16]  latest versions of those modules out on cpan because i want what's on cpan to be a little bit
[2868.16 --> 2873.92]  more stable and if i move it from github to the cpan and i'm not entirely comfortable with it i might
[2873.92 --> 2879.10]  mark it as a developer release so that it won't be installed by default but we use github for
[2879.10 --> 2885.10]  collaboration for sharing for talking about new ideas we use cpan as the central repository so that
[2885.10 --> 2890.22]  when you want to install code or you want to manage your cpan code via pinto or something like that
[2890.22 --> 2896.68]  that you know the one spot to go for that that makes a lot of sense one last question then we'll get
[2896.68 --> 2901.60]  to the close here so it seems like each language especially talking about web uh web programming
[2901.60 --> 2907.14]  languages they all kind of have their killer app you know uh ruby has rails you know you might say
[2907.14 --> 2914.06]  php has wordpress uh javascript has node and you know python has django and and there's alternatives
[2914.06 --> 2919.60]  of course is there like a go-to uh web tool or framework in the pearl community that everybody's
[2919.60 --> 2925.92]  using or is it more kind of diverse it's definitely more kind of diverse there are a number of really
[2925.92 --> 2934.20]  phenomenal tools out there so catalyst is has for the longest time been the default web tool and many
[2934.20 --> 2939.62]  of the clients that i go into today are using catalyst and catalyst is a wonderful framework
[2939.62 --> 2944.64]  mostly based around the concept of mvc but one of the things that differs from some of the
[2944.64 --> 2950.72]  competitors and other languages if you will is that it's agnostic about the mv and c components however
[2950.72 --> 2957.70]  you want to plug those in um do you want to use dbx class for your you know the back end with for the
[2957.70 --> 2962.42]  orm which is going to be backing up whatever your model is eventually going to be do you want to use
[2962.42 --> 2966.86]  rose db do you want to use something different what do you want to have in your view layer to present
[2966.86 --> 2970.96]  things to people you know from the html you know do you want to use template toolkit do you want to use
[2970.96 --> 2977.30]  template xslate do you want to use you know mason what do you want to do is however you want to set it up
[2977.30 --> 2982.94]  so there's a bit more of a learning curve for that but it means you can customize for exactly what you
[2982.94 --> 2988.94]  need there's other things which are extremely popular such as dancer 2 and mojolicious which
[2988.94 --> 2993.32]  have different philosophies which are very easy to use they're lighter weight than catalyst they're
[2993.32 --> 2998.60]  not as fully featured as catalyst but they are so easy to use and so powerful that you know i'm seeing
[2998.60 --> 3005.06]  more and more sites switch over to them and they're really nice when you talk about the orm layer dbx class
[3005.06 --> 3011.16]  is just an absolutely phenomenal orm rose db is also excellent it's not as popular it's just
[3011.16 --> 3018.42]  blazingly fast this is if you like orms i know i know that not everyone does we have an embarrassing
[3018.42 --> 3024.98]  richness of powerful tools because the community pro community has been around so much longer than
[3024.98 --> 3030.84]  many of the other communities that we have a number of very mature products out there but
[3030.84 --> 3036.90]  unfortunately that means if someone says what should i use for you know writing this brilliant
[3036.90 --> 3041.52]  new website that i have you said well you've got this you've got this you've got this and all of them
[3041.52 --> 3048.06]  are excellent all of them have pros and cons and a lot of people i just want that one thing and they
[3048.06 --> 3052.12]  just want to be told what to do and that's a little bit harder to do with pearl because we have
[3052.12 --> 3059.42]  you know an embarrassment of riches if you will excellent excellent so just to preempt the haters
[3059.42 --> 3065.62]  uh yes i realize that no i realize that node is more than just a web thing i just want to get that
[3065.62 --> 3071.26]  out there in case um people thought that that was what i was trying to say um very cool man it sounds
[3071.26 --> 3077.64]  like you guys got a lot going on um every time i talk with somebody on the show i end up being like
[3077.64 --> 3082.96]  i gotta go look into what is going on in this community so uh ovid you did a great job representing
[3082.96 --> 3088.16]  pearl uh yeah do you you said you do consulting you have a book anything you want to uh plug or
[3088.16 --> 3093.86]  promote and while you're here i would say that our company's website is allaroundtheworld.fr
[3093.86 --> 3100.58]  that's because we're based in france we do pearl consulting we really specialize in going into
[3100.58 --> 3105.22]  companies which have older legacy systems and rebuilding them testing them making the modern
[3105.22 --> 3110.66]  systems easier to work on we offer database training get training um i also teach companies
[3110.66 --> 3116.78]  how do you how to use agile appropriately or if they should use agile because that's not always true
[3116.78 --> 3125.84]  and so it's it's kind of oh goodness i can we could spend easily a couple of hours with me going
[3125.84 --> 3132.10]  off about why agile is wonderful and why it is not wonderful and i would follow you both ways
[3132.10 --> 3140.48]  it's yeah because i have some opinions there as well i'm a strong strong agile fan but it's not
[3140.48 --> 3146.46]  always the right choice that's right so we we do a lot of things but mostly it's database get training
[3146.46 --> 3153.18]  uh teaching testing and particularly myself and our other associates going in and fixing people's
[3153.18 --> 3159.68]  legacy data uh pearl systems and making them easier to use it's amazing how much work there is there
[3159.68 --> 3164.08]  any any particular repos you want to mention that you've got on github or anywhere else that uh
[3164.08 --> 3170.28]  that you can use some extra firepower behind like uh some attention to oh my favorite one is
[3170.28 --> 3175.50]  unfortunately a private repo it's uh some a project code named veer which no one's seen but i've
[3175.50 --> 3180.12]  talked about it a lot of my blogs i'm building a text-based mmorpg in pearl
[3180.12 --> 3188.76]  when's that going to get out there i'm hoping to have christmas by christmas i'm hoping to have an
[3188.76 --> 3194.30]  elf out by the end of next year we actually might have a new developer being pulled up in on it this
[3194.30 --> 3199.74]  year uh there's actually been mmorpgs written in pearl before but this one um i found an interesting
[3199.74 --> 3205.48]  niche in the market which is completely uncovered and which was a lot of fun so i'm just building a
[3205.48 --> 3210.92]  science fiction world a true rpg not one of these things you just click around on like bulletin boards
[3210.92 --> 3216.76]  on the web but it's text-based so i'm having a lot of fun with that otherwise i would tell people
[3216.76 --> 3222.96]  check out my test class moose repository if you're interested in pearl and you need to build a large
[3222.96 --> 3230.04]  scale test suite it's much much better than many of the other alternatives out there for the same
[3230.04 --> 3234.14]  reason you wouldn't build a huge website today without choosing an appropriate framework you don't want
[3234.14 --> 3240.30]  to build a huge test suite without choosing an appropriate framework we can't uh we can't
[3240.30 --> 3245.22]  obviously close this show unless we ask the the notorious question which is who is your programming
[3245.22 --> 3249.36]  hero and i figure with uh some of the names you've mentioned today you probably either will repeat
[3249.36 --> 3255.94]  them or you'll have new heroes to mention so um let us know who your hero is oh you're not going to
[3255.94 --> 3265.22]  believe me my programming heroes are my cobalt professors in college um the reason for that is
[3265.22 --> 3271.12]  so my java instructors i remember our very first java instructor she was fresh out of uni and she had
[3271.12 --> 3276.94]  trouble explaining the difference between a class and an instance and it didn't appear that she was a bad
[3276.94 --> 3282.96]  teacher she just seemed a little confused on the concept my second java instructor um i accidentally
[3282.96 --> 3287.92]  turned in some code with some j unit tests and he was confused and kicked it back and said he didn't
[3287.92 --> 3294.18]  understand what that was um i've had this happen with um professors in a number of different programming
[3294.18 --> 3299.32]  languages who's who just didn't have real world experience but the cobalt teachers they had actually
[3299.32 --> 3306.64]  come back in from the field many many years of experience and were able to give a class full of students who
[3306.64 --> 3314.42]  were often you know not very interested or you know not very responsive excellent real world descriptions
[3314.42 --> 3321.10]  of what you need and i still remember the time i was trying to sign up for a c class at a uni and they
[3321.10 --> 3326.40]  told me we don't offer c anymore because the future is object-oriented and c is obsolete
[3326.40 --> 3336.78]  yes completely ivory tower but the cobalt developers they the programmers the professors they understood
[3336.78 --> 3342.36]  that okay it's not the most popular thing out there but they had tons of real world experience which they
[3342.36 --> 3347.26]  were able to communicate in a way that my other professors didn't and they were some of the best
[3347.26 --> 3351.86]  examples i had of what we actually need out there for teaching the next generation of students
[3351.86 --> 3358.70]  the combination between deep theory that is really useful at surprising times but the real world
[3358.70 --> 3366.24]  pragmatism of i gotta get stuff done so they are my programming heroes even though no one knows their
[3366.24 --> 3373.46]  name no one cares about them they're the ones that we need to see a lot more of you know often uh you
[3373.46 --> 3378.88]  know teachers end up being heroes anyways that's just a good thing at least you know on this show reach
[3378.88 --> 3383.86]  back out to them i wonder if uh if they happen to know that uh they're your heroes money chance
[3383.86 --> 3390.64]  but i should find out and contact them what'd you say i said i should find out and contact them at some
[3390.64 --> 3395.66]  point yeah i mean because you know anytime you've touched somebody's life it's it's nice to know because
[3395.66 --> 3400.54]  it's it's sort of like this uh pay it forward you know for teachers they don't always see the fruits of their
[3400.54 --> 3405.04]  labor uh they don't have the luxury of instant gratification you know that's sort of like
[3405.04 --> 3409.90]  plant a seed and it grows over years and years and years and often oftentimes that person goes on
[3409.90 --> 3414.64]  to do great things and i'll be nuts to that person but i know that i've got a couple heroes who are
[3414.64 --> 3420.68]  like that so just saying but okay curtis it's uh it's definitely been a pleasure having you on the
[3420.68 --> 3425.30]  show i think that uh you've given jared and i uh some food for thought so to speak on on the pro
[3425.30 --> 3430.28]  community and the pro ecosystem and how we can sort of support that in in our own way here at the
[3430.28 --> 3436.36]  changelog to just help with this communication and marketing divide of pearl five versus six and
[3436.36 --> 3441.48]  just in general what's happening it seems like you got a lot of fun great things happening that uh
[3441.48 --> 3447.00]  that just need a maybe a clear i don't even i don't even know how to say it but i'm sure there's
[3447.00 --> 3450.36]  some way we can help so we'll we'll do whatever we can to to help you and help the pro community
[3450.36 --> 3454.76]  um we do want to mention a couple sponsors to help make this show possible before we close out
[3454.76 --> 3461.96]  code ship rack space and status page dot io all great sponsors of the show we uh we couldn't do
[3461.96 --> 3467.86]  without their help so uh curtis jared let's uh let's say goodbye adam jared thank you very much
[3467.86 --> 3468.38]  i had a blast
[3484.76 --> 3507.08]  all right guess no bye from jared i forgot to say goodbye
[3507.08 --> 3515.42]  i had to say goodbye real quick goodbye just don't worry about oh i had my thing you've got
[3515.42 --> 3521.76]  to include that in the clip i was muted the podcast i was i was muted i said goodbye to myself
[3521.76 --> 3526.76]  on mute that's funny i'm like i felt like i said goodbye
