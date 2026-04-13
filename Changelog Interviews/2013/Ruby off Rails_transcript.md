[0.00 --> 13.14]  welcome back everyone this is the changelog where remember support a blog and podcast
[13.14 --> 16.44]  podcast that cover looks fresh and what's new in open source you can check out the blog at
[16.44 --> 22.46]  the changelog.com and the past shows at five by five dot tv slash changelog uh the show is
[22.46 --> 28.18]  by myself uh adam stakoviak and as i mentioned in the preamble if you're listening live i got a
[28.18 --> 35.82]  special co-host on the show today tim smith tim say hello hello hello to you yes um if you're a
[35.82 --> 39.94]  long-time listener of the show you know that you can tune in live every tuesday at five central
[39.94 --> 45.60]  standard time however today we are broadcasting a little tiny bit early because of some uh post
[45.60 --> 52.20]  show quickness that i gotta do but this is episode number 96 and we're joined today by jesse wagemott
[52.20 --> 59.92]  he is a fellow rubyist and runs this very cool mentorship slash teaching slash uh course for
[59.92 --> 65.64]  rubyists it's called ruby off rails how how awesome a name is that but jesse welcome to the show my
[65.64 --> 71.90]  friend hi thanks for having me yeah man um let's let's see where do we where do we begin with your
[71.90 --> 77.66]  story so let's talk about i guess the the quickest and most easiest thing is is to do maybe a better
[77.66 --> 82.54]  introduction than i can do for yourself maybe tell the listeners who you are for those who may not
[82.54 --> 91.88]  know who you are sure so i'm a freelance programmer consultant in i live in texas and i've been working
[91.88 --> 105.74]  with ruby and rail since 2007 um and i went full-time on it in 2009 and have just been crazy happy um so
[105.74 --> 113.84]  what what what i wanted to do with with ruby off rails uh was bring that happiness to everybody
[113.84 --> 121.64]  um and so it was like okay how can i you know how can i do that in a way that makes everybody happy
[121.64 --> 130.04]  right and right and so um so yeah so that's the the concept of ruby off rails is to just focus on the
[130.04 --> 137.16]  ruby side of rails uh rails brings the people um but to really become an expert in rails you really
[137.16 --> 144.00]  need to learn the language in addition to the framework that's a um something that especially
[144.00 --> 149.44]  people that are just beginning to learn let's say their first year or two years of working with ruby
[149.44 --> 156.04]  or trying to get you know into a web developer space where they're developing rails applications and
[156.04 --> 161.36]  you know they hear these buzzwords and they want to kind of uh join this join this i guess clan so
[161.36 --> 169.08]  to speak of of uh of uh crazy programmers uh um they get they get to have some fun they're like i
[169.08 --> 175.76]  gotta learn this thing called rails and they forget that uh that is actually ruby on rails meaning that
[175.76 --> 181.58]  you know ruby is the framework and it's built on our sorry rails is i got that backwards see see i bet
[181.58 --> 187.84]  right exactly you know you got uh you got rails and that's the framework and it's built on top of
[187.84 --> 194.22]  a language called ruby which is a beautiful elegant uh very expressive language which you know to me
[194.22 --> 199.58]  that's one of the funnest things about programming in ruby and and maybe you can speak to some of your
[199.58 --> 206.14]  history because you're also a c-sharp developer done some cgi stuff god forbid php you know and other
[206.14 --> 211.46]  things i mean programming in ruby is much different right i mean in comparison to those languages
[211.46 --> 221.08]  yeah it absolutely i mean i started doing web design in college like back in the late 90s right and
[221.08 --> 230.58]  um and that was php and cgi and pearl uh and you know that really wasn't wasn't very much fun right
[230.58 --> 239.86]  like they hadn't ironed out most of the kinks and then the at least at the time in texas all of the
[239.86 --> 246.34]  paying gigs were microsoft based gigs and so i spent a fair amount uh you know from
[246.34 --> 258.86]  2000 to 2007 working on straight dot net applications um and so the experience of developing a dot net app
[258.86 --> 265.40]  is much different than developing a rails app um you know and and so with
[265.40 --> 273.32]  so yeah i mean so seeing all of the different ways that that you can develop these web systems
[273.32 --> 281.84]  some systems try and hide everything from you and then rails doesn't really i mean you you can do so
[281.84 --> 289.54]  many things and what powers almost all of that is the uh the power of of of ruby right being able to
[289.54 --> 295.74]  change stuff at runtime and pass code around using blocks like all of those things build together to
[295.74 --> 304.60]  give you the ability for what everybody's been able to write with rails yeah blocks are uh a super
[304.60 --> 312.56]  powerful thing in ruby for sure um i i did want to uh mention also because i i just dawned on me as we
[312.56 --> 318.30]  were talking there that i hadn't really properly introduced my co-host this special guest co-host
[318.30 --> 323.14]  either because i kind of did in the preamble and i said i would do it in the show but tim you're on
[323.14 --> 328.84]  the show too you and i think the cool thing is that uh having you on the show um today as a co-host
[328.84 --> 334.56]  is kind of neat because jesse is a teacher you're doing some stuff with tim likes to teach so i guess uh
[334.56 --> 340.62]  you would call yourself a teacher right tim i guess but i mean i don't need any introduction the show's
[340.62 --> 344.90]  not about me it's about uh i want people to know who you are i don't want you to just like to sit
[344.90 --> 351.26]  here and not get introduced properly i mean tim smith at the east wing that's very nice of you thank
[351.26 --> 357.00]  you yeah well yeah i'm a nice guy and plus you're also learning ruby too right yeah and you know this
[357.00 --> 363.50]  is this is uh the reason why i was so excited to to be on this particular show um because jesse i i
[363.50 --> 370.16]  just i want to commend you first of all for for you know venturing off into teaching people things
[370.16 --> 376.74]  because i think that is very that's a very good thing um and and especially as the education
[376.74 --> 382.08]  landscape changes over time um you know we're going to need more things like this where you can
[382.08 --> 387.82]  just learn online and and and support a person like you that is teaching these things on your own
[387.82 --> 394.20]  um and second of all i i i'm very very impressed with the design of the site i think it's very very
[394.20 --> 401.76]  nice and very simple um so i i i'm looking to learn more about what you're doing oh awesome awesome i
[401.76 --> 407.22]  mean thank thank you for both of those that's uh that's fantastic thanks um yeah the the education
[407.22 --> 416.84]  space is really just exploding right now with different opportunities for how things can like how
[416.84 --> 424.04]  people can learn um there's everything from the intensive come just for six or 12 weeks in person
[424.04 --> 432.50]  and then there's the massive open enrollment systems like through stanford and um coursera and stuff like
[432.50 --> 440.90]  that um so i mean the range there of all intensive somebody with you you know 10 hours a day to nobody
[440.90 --> 451.12]  with you at all uh it it it's so great to have that wide range of choices about what you can afford
[451.12 --> 458.22]  both on a monetary and a time schedule um and what really fits with how you want to spend your time
[458.22 --> 465.38]  um so i mean i i'm really excited to just be a part of it well since we're i guess we're teeing off
[465.38 --> 471.38]  we were talking a bit there about the expressiveness of ruby and uh i guess the joys of programming
[471.38 --> 478.88]  in ruby versus c sharp or um php or cgi and these are all i mean i've done some stuff in php but not
[478.88 --> 484.62]  in c sharp or cgi i think i looked at cgi early enough in ruby's days to know that that was somewhere
[484.62 --> 489.56]  in there and now i think ruby kind of extract that's away from from me having to ever look at it again but
[489.56 --> 497.08]  um i i personally have never programmed in cgi but um we're talking i guess more so about
[497.08 --> 505.06]  i guess your primary is this your primary thing you do now ruby off rails so i i spend about half
[505.06 --> 512.92]  my time on it and the other half i spend on consulting with with various people right so so
[512.92 --> 519.00]  um like i'll help people either upgrade rails apps or or work on a ruby app or something like that
[519.00 --> 527.88]  um and and so i spend a fair amount of my time on ruby off rails the curriculum is pretty much set
[527.88 --> 536.00]  at this point um couple times a month i may update a a lesson but the majority of the time i'm spending
[536.00 --> 543.18]  with students so students come and they submit like pull requests based on the episode and then we
[543.18 --> 549.50]  talk it over and and really try and develop a relationship with each other so that we can
[549.50 --> 555.40]  help and say hey did you know that there's this cool thing called map in ruby and we go over and
[555.40 --> 565.20]  a lot of it's spent like learning by doing um and then seeing like what else is possible so that's kind of
[565.20 --> 571.84]  what how the time is spent yeah i uh remember talking to you before about the mentorship side of this and
[571.84 --> 578.24]  i have to see that there's a brand new section on your home page now called mentorship yeah uh i when
[578.24 --> 584.56]  when we talked uh you said hey you know that didn't really pop that mentorship was uh a part of
[584.56 --> 591.30]  like a really big part of the of the offering so i said oh that's so that's so ridiculous that i that i
[591.30 --> 598.54]  um didn't focus on it and so yeah it's probably it i did i added a big section on it sort of going over
[598.54 --> 605.14]  sample homework that people get and then um sort of a sample pull request that shows like the back
[605.14 --> 611.42]  and forth and back and forth um that you that that you take um which is i i should say that i don't
[611.42 --> 618.38]  think i could do this course without like github's pull requests i think that was just a just a
[618.38 --> 625.32]  fantastic way to to visualize code and be able to comment on it i just i can't get over how it's
[625.32 --> 630.54]  amazing though right i mean even not just in this particular space of being able to volley back
[630.54 --> 635.74]  and forth uh different comments about the code and comment down to a line item and even include
[635.74 --> 642.66]  morse code samples in that um you know that's that's really neat it's how it's also works in the open
[642.66 --> 647.62]  source landscape and i guess is most of this stuff that you're doing in mentorship is it private is
[647.62 --> 653.02]  it in private repos you've made or is it your your uh students kind of making their own repos and
[653.02 --> 659.14]  you're commenting on them yeah so so it's um it's not private repos so any of the code is just mit
[659.14 --> 665.86]  um uh license and i don't i don't hide it but i don't publicize it either uh except for right now
[665.86 --> 671.58]  i guess right um but everybody knows now right so but there's a ruby off rails uh organization on
[671.58 --> 678.14]  github and like all the code's just there so students just go to the episode after watching it and fork
[678.14 --> 684.78]  it to their repository and then uh submit a pull request with their changes and then we comment on
[684.78 --> 692.04]  that pull and then we just never um merge the pull request right but um right but but yeah so so uh
[692.04 --> 700.04]  it's all out there and uh and then what i like about this is student a can go see what student b did
[700.04 --> 706.54]  yes and and i've seen collaboration between the two of them also uh i so like i i never thought
[706.54 --> 710.42]  about that and it's it's happening and i think it's very cool that student a collaborating with
[710.42 --> 716.04]  student b was or at least seeing some of their code and what they've done beforehand and maybe not so
[716.04 --> 723.00]  much um i i don't know if i didn't whenever it happened to me i guess in this scenario i was working
[723.00 --> 731.04]  on one of the things from jumpstart lab they had um i think it was the trying to recall which
[731.04 --> 736.48]  which tutorial it was that uh that they had done it was micro blogger and i was doing some stuff with
[736.48 --> 742.58]  it and you know i'm still um you know learning to be a bit more proficient in things and um you know
[742.58 --> 746.68]  i i know none of the different methods you can do but i hadn't really thought about doing it
[746.68 --> 751.52]  quite the way this other person had done so i'd seen in the repo there's other students who had
[751.52 --> 755.32]  submitted their work and you can see what they had done and i was like oh that's really neat and i
[755.32 --> 759.36]  kind of like gleaned forward a little bit but learned enough from their code so that whenever
[759.36 --> 764.04]  i was later on in a lesson i didn't have to go back and like do the copy paste kind of sort of thing it
[764.04 --> 769.24]  was more like i had read it and learned it and was able to reapply it from memory without having to
[769.24 --> 774.80]  to to kind of go back to but it was nice to kind of peel back the curtain a little bit and see it
[774.80 --> 780.60]  see a little further ahead in the lesson basically yeah for sure um you know there's always that
[780.60 --> 791.60]  um that inclination right to to just look at the the correct answer um and so people have to be
[791.60 --> 798.78]  you know not do that right um but the the real answer is that there's no right answer in programming
[798.78 --> 804.30]  right there's a zillion ways you could do it and man yeah i guess what is well you know i guess what
[804.30 --> 809.80]  is the the most efficient way to do something isn't always the the best way is it's the sometimes the
[809.80 --> 815.60]  most expressive way like the most efficient might read really weird but uh and more expressive you
[815.60 --> 821.46]  know single line versus you know three lines uh method for example could be a lot more expressive
[821.46 --> 828.78]  yeah we i just had a example today that i was uh commenting on somebody's work and uh they had
[828.78 --> 836.08]  created a hash that had like uh all of the days of the week like one and monday two and tuesday
[836.08 --> 844.46]  and so on and then later on they they were writing out like one tuesday too so it wasn't quote unquote
[844.46 --> 852.94]  dry uh and and so i was i wrote like a a way to show them how you could keep it dry and i looked back
[852.94 --> 860.14]  at it and i said this is just this is a little bit crazy to keep it like this like future you is going
[860.14 --> 866.28]  to come and read this and not have any idea what it is at first glance yeah um and so it was a good
[866.28 --> 876.66]  lesson uh to me to hopefully to to the student in like um just following the rules sometimes doesn't
[876.66 --> 881.78]  make a lot of sense like you should understand them and then know when to break them right so
[881.78 --> 889.52]  this this thing you're doing is obviously called ruby off rails and i think that before i introduced
[889.52 --> 895.22]  tim and i kind of derailed us for a second there because i wanted to make sure everybody knew who
[895.22 --> 902.70]  tim was tim you got introduced right yes yes all right everybody knows tim that's good um sorry
[902.70 --> 907.86]  about that tim but can i can i ask a quick question before we move on here only if it's super quick
[907.86 --> 914.78]  of course yeah uh one of one of the things that i that i find so fascinating um like like adam pointed
[914.78 --> 922.96]  out was the mentorship aspect of of your teaching um and i think that that is that is a huge differentiator
[922.96 --> 927.96]  right because i mean if you look at the other people that are the the big players that are teaching
[927.96 --> 935.82]  ruby or or rails um you look at someone like code school or you look at someone like uh like treehouse
[935.82 --> 942.12]  uh there really isn't any personal interaction between the teachers and the students and that
[942.12 --> 948.60]  and you know that's an experience that if you learn online you kind of miss out on if you were to learn
[948.60 --> 959.32]  in person um my my question would be what what motivated you to to decide to take the time to mentor the
[959.32 --> 965.66]  students because you know that does take time and that does take money on your part i guess yeah uh to
[965.66 --> 972.82]  to take that time and dedicate it to them yeah right on um so i started ruby off rails uh because
[972.82 --> 981.06]  before i was doing one-on-one trainings with people uh so i help with the the houston ruby group now and
[981.06 --> 986.62]  people would come and say i want to learn can we do some trainings and so we'd you know like a set of
[986.62 --> 995.28]  10 or something trainings and and i'd uh so so that was my um point of view from it right i was looking
[995.28 --> 1001.20]  at it as me training somebody and being able to give like one-on-one feedback to how they were
[1001.20 --> 1007.06]  learning because each of them would learn differently um and and and so it was more of
[1007.06 --> 1012.16]  like a tutoring relationship uh so we'd come and like just start from scratch and write code and we'd
[1012.16 --> 1013.72]  talk about it and
[1013.72 --> 1024.78]  so i had a couple people that didn't like the ruby part they would be like dude i just want my rails
[1024.78 --> 1034.66]  right and they say like that too yeah so yeah they were surfers um and and so after a couple of
[1034.66 --> 1040.96]  months it was it was really predictable about who was going to have success and who was was going to
[1040.96 --> 1049.92]  reach a point where their rails was really more like copying code out of stack overflow or rails casts
[1049.92 --> 1057.82]  or or whatever right like it never got there for them and so i i was looking at it's like you know
[1057.82 --> 1064.40]  rails is like this dialect of ruby so it's it's it's its own thing and you can stay totally with the
[1064.40 --> 1070.62]  rails and you can be fantastically productive but if you really want to learn like if you want to
[1070.62 --> 1077.84]  become take that expert level right i and really become proficient i think that you have to learn
[1077.84 --> 1083.34]  the ruby part and so that that's what i was seeing the people that learned ruby could excel at rails at a
[1083.34 --> 1090.24]  much faster pace and they weren't frustrated by rails and since they learned tdd throughout the whole
[1090.24 --> 1098.22]  process um they weren't they were positive about testing in rails whereas the rails people just
[1098.22 --> 1104.32]  never wanted to test at all um and so i was able to see that happen enough where i was like okay i think
[1104.32 --> 1112.98]  this is this is a thing um and so that's why i i started looking and i was like i don't just want
[1112.98 --> 1119.52]  to put content out there and not see anything i think there needs to be tests and so i iterated
[1119.52 --> 1124.70]  over it and i said well it could just be they submit tests and if i've got code if i've got tests and they
[1124.70 --> 1132.22]  pass then okay they get a green light and everybody's happy right um but i i sort of felt that it was
[1132.22 --> 1138.68]  missing that personal touch so to speak right it was missing that opportunity to have someone ask
[1138.68 --> 1146.04]  questions and really say hey i see what you're doing here but you should really be doing it this
[1146.04 --> 1150.18]  way which is what you do when you're sitting there to together like this is where it came from so
[1150.18 --> 1155.80]  sitting down with people from the houston ruby group or uh friends you meet that want to learn
[1155.80 --> 1161.02]  ruby and they're like hey jesse can you teach me or show me the ropes and so that's kind of where
[1161.02 --> 1167.10]  ruby off rails came from was and this idea of how you can um build it was from this sort of
[1167.10 --> 1173.32]  hands-on approach from the get-go yeah exactly that's exactly right and so that's that's what
[1173.32 --> 1180.04]  i took it from and so it just always it just always seemed that that made a lot of sense right um it
[1180.04 --> 1187.98]  wasn't till later that i discovered uh hey you're tying the total income you can make with the uh total
[1187.98 --> 1196.96]  students that you have right right um and i said you know what that's great um that uh what i'm
[1196.96 --> 1205.26]  it's more of a premium class so to speak um you know we really teach the intermediate level stuff
[1205.26 --> 1211.96]  um and so we've recently added like beginner classes but the main course is we're building
[1211.96 --> 1220.98]  applications in ruby um and so i the the people that complete it and do everything um they go on and
[1220.98 --> 1228.72]  they're they're they're really happy and so i'm happy to have this personal touch on it
[1228.72 --> 1234.70]  it uh it's called ruby off rail so tim i'm really glad you asked the question you did because it kind
[1234.70 --> 1240.20]  of prefaced um and i think jesse even answered my question kind of within tim's question which
[1240.20 --> 1246.98]  um which basically was to to try to for those that are listening that may just be stumbling on ruby or
[1246.98 --> 1251.42]  have been hearing about rails and they're not really sure what it is or maybe they're really
[1251.42 --> 1255.48]  you know they've been using ruby for a while and they just never dove in and truly learn a language
[1255.48 --> 1263.08]  like what the point is of ruby off rails so if you plan to do rails applications or develop something
[1263.08 --> 1269.72]  with rails what is the point of you know the ruby part or learning ruby you know not so much before
[1269.72 --> 1276.64]  but really being proficient in ruby versus just learning the rails way yeah so so i think that that's
[1276.64 --> 1284.62]  it's a great question um and and like why right um and and and it comes down to i think you really
[1284.62 --> 1290.84]  need to learn your tools if you want to take that next step so i don't think that it's enough that you
[1290.84 --> 1299.72]  just learn how rails does javascript to really know javascript um and it's the same with testing it's
[1299.72 --> 1306.54]  the same with say object-oriented design uh and creating really maintainable software i think that
[1306.54 --> 1318.18]  the rails way makes sense in most sort of base camp type systems and where the the people that
[1318.18 --> 1326.94]  i've consulted with have trouble is that there can only be one base camp so if you deviate too far
[1326.94 --> 1332.90]  from that some of the techniques that's the rails way stop making sense and and at that point you
[1332.90 --> 1340.28]  really are programming you're not just plugging stuff into rails and and that's not to say that
[1340.28 --> 1348.62]  rails is bad at all right i love it um but i do think that if you understand more the theory and you
[1348.62 --> 1358.02]  understand say what a module is and you know what the difference are in in your ruby methods and how to
[1358.02 --> 1365.14]  effectively use meta programming um i think that that type of stuff really has a benefit because
[1365.14 --> 1371.68]  suddenly you can start writing your own gems right that's not this magical secret like you can start
[1371.68 --> 1381.48]  writing individual little services um and so i think that that is the reason why is so that you can do more
[1381.48 --> 1390.12]  with your rails than just what rails can do out of the box i think you bring up an amazingly good point
[1390.12 --> 1398.32]  with that because it's it's um i guess it goes back to you know that old saying teach a man how to fish
[1398.32 --> 1405.86]  and he'll eat forever but if you get a fish he'll eat for a day i know that that's i totally butchered that
[1405.86 --> 1414.66]  saying but but um but i i guess the the point is that by teaching someone ruby which is the foundation
[1414.66 --> 1421.96]  of which rails is built on um they're they're learning the basics of of how to think within ruby
[1421.96 --> 1429.44]  and therefore can can do you know wonders with rails and who knows maybe even other frameworks that are
[1429.44 --> 1436.70]  built on ruby yeah for sure i i absolutely agree uh and i think um i think the quote that you're
[1436.70 --> 1442.96]  looking for is uh goes something like um if you fix somebody's pro program uh they were only mad for a
[1442.96 --> 1450.42]  day but if you teach them how to program they're mad for the rest of their life um that's true yeah um
[1450.42 --> 1457.56]  but no like uh i i do think that suddenly you can write little one-off ruby scripts whereas before you're
[1457.56 --> 1465.30]  you know you know just clicking around all the time and then you can you can bring up quick little
[1465.30 --> 1473.84]  sinatra apps um yeah and and and so you know i do think that that it really does help and i don't
[1473.84 --> 1481.26]  think you're going to get all you can out of ruby on rails unless you learn ruby i remember um when we
[1481.26 --> 1489.08]  launched and um it i got so much feedback from people that that were saying i can't i don't i didn't even
[1489.08 --> 1493.38]  know there were people that didn't know ruby and then there were a bunch of other people that that
[1493.38 --> 1500.14]  were saying yes this is how you're supposed to i wish that i could go back and um and learn ruby first
[1500.14 --> 1506.94]  and that's that's um that's why i was really taking um i really enjoyed the concept of ruby
[1506.94 --> 1512.06]  off rails because that's like so you'd mentioned when the show started how long you've been working
[1512.06 --> 1521.38]  in ruby and honestly i've been designing developing different things in the ruby landscape for many
[1521.38 --> 1528.84]  many years like i bet you the first thing i did with ruby was back in like 2006 2007 but i hadn't
[1528.84 --> 1532.98]  really done a lot of programming in ruby i've done various things here and there but nothing major
[1532.98 --> 1540.22]  but i've kind of like been learning i guess along the way and uh what i really appreciate about i
[1540.22 --> 1547.94]  guess just this concept of learning ruby in order to learn rails better was that it just totally makes
[1547.94 --> 1553.28]  sense to you know why would you want to learn like i guess in a lot of cases you might think of the
[1553.28 --> 1558.74]  rails way as a shortcut right because there's a lot of magic you know in air quotes magic and rails
[1558.74 --> 1564.58]  that's there for a good reason like you said it's a good thing because once you're a proficient
[1564.58 --> 1569.00]  enough developer anything that you do often enough you want to learn how to automate you know within
[1569.00 --> 1574.92]  reason obviously um and that's what a lot of what rails does with various things that it does with
[1574.92 --> 1579.70]  different methods that are only available in rails and different idioms that are only in root in in
[1579.70 --> 1584.28]  rails they're not you know they're not like ruby things they're rails things but i thought i want to
[1584.28 --> 1590.18]  learn ruby and learn the depths of ruby and really learn to appreciate the language for what it is
[1590.18 --> 1596.58]  uh before i learn something that has been built on it to better learn like you said you know launch
[1596.58 --> 1603.08]  something simple with sinatra or you know anything else and timid you mentioned um being able to work
[1603.08 --> 1609.24]  with another framework that's been written in ruby to not just be isolated to rails you know to kind of
[1609.24 --> 1616.16]  get that full breadth of of knowledge from from the uh the real the ruby world yeah right on um i
[1616.16 --> 1625.96]  i i i started around the same time i remember seeing rails and it was and i went out and um i was like
[1625.96 --> 1634.18]  wow and my wow moment was when i saw like find by username right where um where i was like wait you
[1634.18 --> 1639.68]  didn't write that method and they're like i know that's the thing and i'm like whoa right like my
[1639.68 --> 1647.70]  is the magic part that is yeah yeah and and so uh i remember that moment where i was like oh so that's
[1647.70 --> 1652.44]  how it works when you finally saw that it's method missing right stuff like that right and and then
[1652.44 --> 1659.04]  you're like whoa and i remember somebody the the same person that that told me like showed me rails
[1659.04 --> 1663.24]  was like a lot of people come for the rails but they stay for the ruby and i had no idea what that
[1663.24 --> 1669.30]  meant um but i think it's absolutely true um so yeah so so i went out and i bought like agile web
[1669.30 --> 1674.64]  development and rails uh and built like a social network um that that was my uh that was my first
[1674.64 --> 1683.94]  thing and it's still running um what's it called oh we eat so and as as the is the style of the time
[1683.94 --> 1690.68]  there are two t's so it's w-e-e-a-t-t which is like horrible for search engine optimization um but it's
[1690.68 --> 1697.52]  there uh and so if you need if you need to share your recipes with uh friends and family you can
[1697.52 --> 1702.50]  you can have private recipes protected recipes that share with your family i mean this whole
[1702.50 --> 1709.36]  whole idea is ridiculous right but nice um but uh but i was like yes and i had a spreadsheet uh that
[1709.36 --> 1715.14]  that showed that i was going to be the next dig um oh is that right yeah so if it grows at this
[1715.14 --> 1720.52]  and i can get the white dollars i'm gonna be awesome um how'd that work out but uh okay well
[1720.52 --> 1729.90]  i outlasted dig uh so um i mean they're they're back obviously but um but uh but um but yeah so so
[1729.90 --> 1737.42]  it's it's still running uh i upgraded it a couple different times um but but you know i barely look
[1737.42 --> 1743.02]  at it right um but we've got all our recipes there and so whenever we want to make our uh our pizza
[1743.02 --> 1750.26]  or like the fajitas like we pull it up and say oh okay so um it so yeah being able just to create
[1750.26 --> 1756.00]  little stuff like that and host it on heroku it's uh it's crazy if as you compare to what it took to
[1756.00 --> 1764.72]  get a site online in 2002 so when you look at the i guess the learning we talked a little bit earlier
[1764.72 --> 1770.42]  in the show about um others that do learning and the depth that they do or do not go into holding
[1770.42 --> 1776.02]  the student's hand you know when you just when you look at the the landscape of learning programming
[1776.02 --> 1782.02]  not just ruby but learning programming um how do you see that shifting as someone that's been doing
[1782.02 --> 1786.18]  ruby off rails for a while and been personally mentoring people how do you see the shift from
[1786.18 --> 1792.90]  let's say someone who you know i i meet people sometimes that are like oh i want to get into
[1792.90 --> 1797.52]  web development so i've got to go to school to get my css my cs degree i almost said css
[1797.52 --> 1802.06]  because it's just a habit but um i want to get my cs degree and i'm like well i don't think you
[1802.06 --> 1806.56]  have to do that to learn how to build stuff on the web i think that there's that's a that's one path
[1806.56 --> 1812.12]  but is that the right path for you you know there's a lot of different paths out there and you'd
[1812.12 --> 1815.80]  mentioned some that are really in depth some that hold your hand some that don't hold your hand some
[1815.80 --> 1821.56]  that you know what is the right path i mean how does someone begin to if they're wanting to learn
[1821.56 --> 1827.46]  where do they begin to go how do you begin to identify what best fits that's such a good question i mean
[1827.46 --> 1833.58]  i remember i first saw programming in college and it wasn't even a cs degree it was in business
[1833.58 --> 1838.90]  school and they just made you take a programming class and i remember that point at which it clicked
[1838.90 --> 1847.68]  and i was like wow right um i think a lot of people do that uh most of the programmers that i meet that
[1847.68 --> 1853.40]  have been doing it for a while it's it's almost like the the profession chooses them than like just
[1853.40 --> 1862.06]  deciding well i guess i'll be a programmer um i don't know if if it really works for people that
[1862.06 --> 1868.72]  that just want to do it just as a job um what do you guys think about that i'm i'm curious like
[1868.72 --> 1876.52]  can't i'm people can but it is this profession for for just people that just want a job
[1876.52 --> 1883.66]  yes and i think it is for people it can be for people who just want a job because uh you know
[1883.66 --> 1888.90]  we're getting into psychology here but you know if you're an introvert versus an extrovert you know
[1888.90 --> 1895.26]  you can be very introverted as a programmer right you you don't have to be social and code on get up you
[1895.26 --> 1899.76]  don't have to do those things but and you know you can get a job a cozy job that you you're really
[1899.76 --> 1904.12]  proficient at and just kind of just chill there and do that thing get paid whatever get benefits and
[1904.12 --> 1909.50]  just go into work nine to five program fix you know whatever the case might be and then you have
[1909.50 --> 1913.94]  you know you're you're out of the box people i'm not even sure how i can give as an example that just
[1913.94 --> 1920.30]  want to learn every language you touch uh maybe i don't know who would be a good example of somebody
[1920.30 --> 1925.18]  who can't just do that but i mean yeah i think the the gamut is wide open for
[1925.18 --> 1933.26]  mark warman sam sophis all those people that make me sick that make you sick okay i can i can buy that
[1933.26 --> 1939.22]  absolutely um so so i guess uh after my little tangent there uh the question was you know how
[1939.22 --> 1949.48]  does all of this end up shaping um the the education landscape i think that it to be a web developer
[1949.48 --> 1960.46]  right and soon probably a mobile developer um that college in the traditional sense doesn't prepare
[1960.46 --> 1970.20]  you for that i don't think um i think that if you go to school right a university and you learn
[1970.20 --> 1978.04]  computer science and you graduate with a cs degree that's prepared you to really think about hard
[1978.04 --> 1984.84]  problems in programming not necessarily how to run rails right not how to get node up and running or
[1984.84 --> 1991.08]  look at go or anything like that it didn't i don't think it touches on much of that um it just teaches
[1991.08 --> 1998.54]  you more of how to design how to really be able to do programming languages so it's it's sort of do you
[1998.54 --> 2007.80]  want to use or or do you want to create programming languages so most of the mass amount of programmers
[2007.80 --> 2014.76]  out there use frameworks right um and so for them i think it absolutely makes sense to
[2014.76 --> 2023.38]  you know whether you learn by books or whether you learn like face to face to not necessarily
[2023.38 --> 2030.06]  do college for that degree there are reasons to go to college um but i don't think college to web
[2030.06 --> 2040.26]  developer is a direct direct line um and so for those people you can look at the the the suite of
[2040.26 --> 2047.40]  programs that are out there learning how to program um and and really start there and once you get the
[2047.40 --> 2054.00]  logic down and then you get a little bit of design and you get some of the um some javascript and
[2054.00 --> 2061.32]  html and you learn ruby and rails and then you can start to learn some of the foundations of programming
[2061.32 --> 2068.84]  right and and can sort of iterate over that and become better over time um so you can start that
[2068.84 --> 2078.38]  process uh at 13 right and and then just be creating um and then being able to see the code
[2078.38 --> 2087.80]  of open source projects uh is such a differentiator from working with open source and not um being
[2087.80 --> 2096.66]  able just to open up rails and see how they implemented some link to function um is so great
[2096.66 --> 2101.26]  as compared to a closed source system i think that like being able to look at this and see how people
[2101.26 --> 2106.88]  are implementing stuff gives you ideas for how you can implement stuff uh it really is this cycle
[2106.88 --> 2113.86]  um so i think that it all just plays together of people being able to learn on their own and then
[2113.86 --> 2121.68]  work with other people and help other people learn you see and it's for those reasons that i don't feel
[2121.68 --> 2131.78]  that this is necessarily a job for people that want to do just nine to five i don't think you can be
[2131.78 --> 2138.86]  a good programmer and not and not love it well i guess that's subjective though because
[2138.86 --> 2147.44]  your love versus someone else's love could be it's all relative right there's no there's no black and
[2147.44 --> 2156.20]  white on that one yeah i i can understand that there are people that straight nine to five don't read
[2156.20 --> 2161.80]  about programming don't think about programming outside of their um outside of their time at work
[2161.80 --> 2168.38]  um i can understand that there are people like that i cannot imagine being yeah exactly that's that's a
[2168.38 --> 2174.22]  definitely good point there we go yeah that's a good way of putting it right um i think these kinds
[2174.22 --> 2179.40]  of ruby off rails is certainly for somebody who's looking to be better someone who's looking to really
[2179.40 --> 2186.20]  show their passion for learning programming or learning ruby specifically or being mentored
[2186.20 --> 2193.56]  because you know i don't know how many students you have but uh you know i truth be told we live in
[2193.56 --> 2199.36]  the same city we've probably only seen each other a small handful of times jesse but right i mean i mean
[2199.36 --> 2204.60]  and i you know i heard about ruby off rails through just like indirect chinos we probably share together but
[2204.60 --> 2209.78]  and i can't imagine that you have like 20 000 students for example right i mean it's not
[2209.78 --> 2215.96]  you know crazy big but it's it's definitely getting a lot of traction and someone who is going to choose
[2215.96 --> 2223.22]  to go and uh become a student of ruby off rails become uh you know let you be their coach and you can
[2223.22 --> 2230.42]  mentor them there it's somebody who really wants to enjoy programming somebody who wants to up their game
[2230.42 --> 2234.66]  a bit somebody and even as some of the things you say here on your home page is like to add more
[2234.66 --> 2240.08]  dollars to their salary to become worth more because the more skills you gain the more proficient you are
[2240.08 --> 2245.28]  you know the the more value you can provide to somebody whether it's you doing consulting you
[2245.28 --> 2251.16]  running your own company or you working for somebody yeah absolutely right like i think that the the
[2251.16 --> 2259.80]  person that like the student that ends up signing up and and really just nailing the whole course
[2259.80 --> 2267.24]  is someone who's driven um and someone that can sit down and devote like whatever schedule works for
[2267.24 --> 2274.28]  them say uh like once a week like okay i'm gonna watch this hour-long episode and uh and then i'm gonna
[2274.28 --> 2281.98]  like really tackle um the the homework at whatever level they feel feel comfortable at so it's that person
[2281.98 --> 2289.78]  that really wants to um to to get better right is is really driven i think so so i
[2289.78 --> 2297.32]  guess what i was gonna mention is that um that about halfway through so so i've been doing it for
[2297.32 --> 2309.10]  a year uh i started a scholarship for women and uh student developers um and so this was around i i was
[2309.10 --> 2317.24]  saying that there is a gender gap gap in in our industry right and and we've seen a lot of good in the
[2317.24 --> 2325.10]  last year but we've still got a long way to go and so the scholarship is like 80 off the the course and
[2325.10 --> 2336.02]  so um i i it really helps to to encourage uh you know women and students to to to join and to and
[2336.02 --> 2344.06]  to really nail it um and so that's been um pretty successful in the in the last year um but so as far
[2344.06 --> 2353.88]  as like how many students i think we just crossed 150 um over the the full year um and so so yeah so
[2353.88 --> 2361.32]  so a lot of people have taken taken me up on it and so i i've i've liked um you know getting to know
[2361.32 --> 2367.56]  everybody and uh and seeing everybody make my code better yeah i wanted to ask you about that because
[2367.56 --> 2372.20]  i mean that's definitely been a hot topic for the past few years just between diversity
[2372.20 --> 2378.88]  and you know you got the term i think it's been mentioned a couple times here we try to
[2378.88 --> 2383.94]  i guess not so much avoid drama on the show we just try to focus on the things that are positive but
[2383.94 --> 2389.78]  that doesn't mean that we want to not talk about touchy subjects because we just try to be i guess the
[2389.78 --> 2395.96]  straight line down the middle and not try to um be opinionated but more so shine the spotlight on the
[2395.96 --> 2400.96]  people that are doing really cool things in open source and software development and extract what
[2400.96 --> 2405.22]  we can but um you wrote a post on this actually you know it was called the one where i have to explain
[2405.22 --> 2409.48]  why i want diversity in our field and i think that this is something that's been talked about quite a
[2409.48 --> 2417.34]  bit um and you'd mentioned it's a fan of the show ash dryden um she was treated horribly sarah parmenter
[2417.34 --> 2423.06]  uh somebody you hadn't even spoken to was treated horribly and then this is what spawned the desire to do
[2423.06 --> 2428.96]  this is was this post way before this scholarship that you opened up or is it you know just before
[2428.96 --> 2440.06]  i think it was the i think the scholarship was available for maybe a month or two before okay so
[2440.06 --> 2448.04]  it wasn't the that that post did not say hey i should do the scholarship right i've been seeing those
[2448.04 --> 2456.20]  things around um and and i've just been thinking like hey i can do something what can i do and so
[2456.20 --> 2464.38]  this was before rails girls existed um and so i was like well i have this thing and if people learn ruby
[2464.38 --> 2469.48]  they can make more money and if they can make more money then you know they can make more decisions
[2469.48 --> 2475.98]  about their life um and so i said all right so what i'll do is we'll have some people that can do it
[2475.98 --> 2482.54]  for free and then others give a big discount and so we kept going with the discount um and and you
[2482.54 --> 2489.44]  know to to try and encourage behavior just to yeah try and make people feel more welcome i like the way
[2489.44 --> 2497.82]  you said that though like what can i do right and i think that um just to be as openly and honestly as
[2497.82 --> 2504.80]  possible about the i guess the topic really is that it's obviously uh gender slided where it's more of a
[2504.80 --> 2510.18]  male dominant uh industry there's many of us who really really want to make that more diverse
[2510.18 --> 2516.32]  um but being able to like for example here at the change law like i've been looking for ways that we
[2516.32 --> 2523.60]  can do that a bit more we have uh one woman writer on our on our uh and we've talked about her plenty
[2523.60 --> 2528.86]  i work with her at pure charity she's super awesome awesome woman awesome programmer awesome everything
[2528.86 --> 2535.94]  her name is beverly nelson but you know sometimes i feel like um you can kind of get in this deer in
[2535.94 --> 2542.08]  the headlights kind of stance to the subject because you don't want to fall on the wrong side accidentally
[2542.08 --> 2549.38]  you know it's it i don't know if that's an easy way to put it but indirectly somehow you do something
[2549.38 --> 2555.88]  that offends not because you really try to but just you know something didn't come out right or you
[2555.88 --> 2562.24]  said something that like you you know for example a formality might be to say hey guys when you don't
[2562.24 --> 2569.68]  really mean hey guys you mean hey guys and gals it's funny because uh uh win and i we used to do this
[2569.68 --> 2577.72]  um this course at uh at lone star ruby conference called design eye for the dev guy and gal and we
[2577.72 --> 2582.40]  actually had and it was kind of cool because it's kind of a texas thing right and gal right but you
[2582.40 --> 2587.30]  know it's just it's a very touchy line but i like the idea of what you said which is you know what
[2587.30 --> 2594.16]  can i do and i think more people can stand up and say that what can i do to show um you know show that
[2594.16 --> 2601.10]  i want diversity or to help enhance it or to do whatever i can personally do to make that a priority
[2601.10 --> 2610.68]  for you know our community yeah i totally i totally agree with that um because there there's a huge
[2610.68 --> 2617.96]  difference between noticing that something should be done and you know taking the stance that you have
[2617.96 --> 2624.10]  where it's like you know um let me actually do something instead of just tweet about it you know
[2624.10 --> 2631.38]  what i mean yeah because there's uh there are countless people that that will talk about it on
[2631.38 --> 2638.32]  on twitter and and because it is a an important issue and it is a hot issue um more more recently
[2638.32 --> 2645.56]  maybe because we just barely noticed i don't know but i mean it's it's uh it's something
[2645.56 --> 2651.92]  completely different when you say look i'm gonna do something proactive and try to make a change
[2651.92 --> 2660.84]  100 on uh on one of your posts i'm just curious if you still honor this because uh you said it's 80
[2660.84 --> 2668.24]  and here it says tl dr i am offering 100 scholarship to the six-week ruby off rails class for up to
[2668.24 --> 2673.28]  five women software developers apply here are you still if someone applies to that are you honoring
[2673.28 --> 2682.82]  100 just curious so i right now i don't know how to make it happen with the year-round sign up anytime
[2682.82 --> 2689.40]  you want scholarship um so what i mean by that is when it started it was once a quarter oh okay so
[2689.40 --> 2696.64]  and and so it made sense that each time that i did it i could pick five students that that um you know
[2696.64 --> 2703.54]  have them apply and and and pick five students that would get a full scholarship and and we didn't
[2703.54 --> 2711.22]  have the 80 off at that point and so we added the 80 off i think the or i did the the next quarter
[2711.22 --> 2717.32]  and then in the last it so what's would have started in june would have been another course right
[2717.32 --> 2723.52]  another episode and i changed it to available anytime start when you want do it at your own pace
[2723.52 --> 2729.20]  you're not limited to 12 weeks anymore and the downside of that as least as that i've seen is
[2729.20 --> 2736.00]  is i didn't quite know how to do the full scholarship um and so i've been playing with some ideas there
[2736.00 --> 2742.82]  um but yeah i think if anybody emailed me right so if anybody wants to email me like we'll talk and
[2742.82 --> 2748.46]  and we can make it happen um but i don't have the mechanics down there yet of how to do that
[2748.46 --> 2756.22]  gotcha um it could be as simple as just ask for it um and we can see right um but i don't know i i
[2756.22 --> 2762.82]  don't know yet so on the topic of of this scholarship both for students as well as women what has been
[2762.82 --> 2767.68]  you know give us some success stories from this or even you know fail stories i don't know a good
[2767.68 --> 2773.00]  story from from how you've seen you being able to do something and what the impact has been
[2773.00 --> 2785.58]  i've seen let's see some of the what for the i've seen more success with people that pay 20 percent
[2785.58 --> 2796.36]  than i have with the full scholarship um and i don't quite know if if if i can draw conclusions to that
[2796.36 --> 2803.18]  other than maybe if i got something for totally free i wouldn't put much value in it but if i pay
[2803.18 --> 2808.80]  for it even if it's just a little bit right and i value it a little bit more but i've seen that um
[2808.80 --> 2816.98]  but i i let's see otherwise i've i've seen some of some of the women students take and like at a higher
[2816.98 --> 2824.44]  rate than the men finish the course and um and like totally knock it out um so
[2824.44 --> 2832.92]  and then i've seen some of them go on to work at other places um and and so i'm excited about that
[2832.92 --> 2844.26]  uh about about seeing success like playing a small part in in their success um and so you know i tend
[2844.26 --> 2850.34]  to follow and talk to them on twitter and stuff like that and so yay students that kind of brings up a
[2850.34 --> 2858.10]  uh i guess the backfill of that question which is placement you know if you are um you know if you
[2858.10 --> 2865.48]  are a teacher and you have many students it would make sense that um that others who are employers
[2865.48 --> 2871.38]  would come to potentially you to see who are the next candidates coming out of your most recent courses
[2871.38 --> 2877.60]  that would be great applicants for these positions i have open yeah absolutely and so
[2877.60 --> 2882.24]  a couple times in the past people have done that like hey i'm looking for people especially people
[2882.24 --> 2892.12]  that know and and like ruby um you know what what can we do um and so you know you make instructions
[2892.12 --> 2899.92]  and ask people if they're interested uh you know like most of the conversations that go that way
[2899.92 --> 2905.46]  uh the number of people that are looking for jobs is much less than the number of people that are
[2905.46 --> 2912.28]  hiring for jobs um so that that seems to be one constant well that's a good thing right yeah
[2912.28 --> 2917.44]  absolutely um it is a good thing yeah because because i remember certainly what it was like in
[2917.44 --> 2928.60]  2002 and three right or um where them be rough times yeah them yeah so on uh on that note then of
[2928.60 --> 2934.04]  helping people get placed do you you know for those who are you know listening that are fans of the
[2934.04 --> 2938.42]  changelog in this show and they happen to be running a company they have some positions open and let's
[2938.42 --> 2943.96]  say they have some ruby positions or rails positions open you know what how would they reach out to you
[2943.96 --> 2950.28]  what is the process of like getting on the proverbial list to to be notified of like new applicants and is
[2950.28 --> 2955.34]  this something that you're going to be formally introducing as like i imagine this has got to be a
[2955.34 --> 2960.70]  revenue opportunity for you as well that's interesting i um right now it's totally informal
[2960.70 --> 2969.04]  um so i may change that like you're suggesting to uh to something else i'd like to be able to do
[2969.04 --> 2975.00]  something like jeff casimir is doing with uh with their g school program where you see
[2975.00 --> 2983.38]  um they have at the end of their course they can bring companies in and show off and really um show off
[2983.38 --> 2989.40]  the the projects and the the students and say hey you should hire these people right i i think that
[2989.40 --> 2996.50]  would be so fantastic um and so probably what i need to do a a better job of is getting the word
[2996.50 --> 3002.78]  out there more about ruby off rails and then sort of completing that cycle um but let's say that right
[3002.78 --> 3009.74]  now there are people that that want to hire people email me at uh jesse j-e-s-s-e at rubyoffrails.com
[3009.74 --> 3015.82]  and um and i'll hook you up yeah i think it's an important thing because i mean it kind of completes
[3015.82 --> 3020.54]  the cycle right i mean one you got into it because you have a heart for teaching and mentoring and
[3020.54 --> 3028.42]  you kind of got uh you iterated i guess into it because you were doing it so well um you know
[3028.42 --> 3033.70]  for for a number of years and it came to a point where you're like let's actually make this into a
[3033.70 --> 3038.46]  course that scales a little better um and now you're kind of at that point and it it would even
[3038.46 --> 3044.88]  be as a value add for me to you know to take like you had mentioned your most premium course
[3044.88 --> 3049.28]  um and i want to go back and and look at what that is actually before
[3049.28 --> 3057.34]  which uh i think you have what um a ruby sort of the applied ruby theory which is like your your
[3057.34 --> 3062.34]  mainline course and you probably get sticker shot from this sometimes at least whenever i first looked
[3062.34 --> 3066.96]  at it i was like whoa but then again like i said i didn't realize that uh mentorship was such a huge
[3066.96 --> 3073.68]  component of it so you've got your your premium course which is like almost what almost 500 bucks
[3073.68 --> 3079.12]  but uh you know if you're a student or a woman you can apply for a little bit less um but i guess the
[3079.12 --> 3084.36]  point there is is that you know you kind of iterated to get to that point and but a value add of of me
[3084.36 --> 3089.84]  saying okay well i'll shell out 500 bucks you know get you as a great mentor be able to go through
[3089.84 --> 3094.82]  all these different courses and get homework and really focus on this but out the other side i know
[3094.82 --> 3101.50]  jesse has also not only helped me learn the the ruby and rails ways but i'm also learning how or i'm
[3101.50 --> 3106.76]  also getting an opportunity at the end of potentially just walking into a good opportunity i'm still
[3106.76 --> 3111.54]  having to obviously do what i gotta do but you know you've kind of teed up some opportunities
[3111.54 --> 3114.56]  yeah i think that's a great idea i'd definitely take that down
[3114.56 --> 3121.32]  so we have uh two common questions and i kind of miss andrew on this one because uh tim you don't know
[3121.32 --> 3128.26]  the questions but um normally uh on the show we we wrap things up by asking for i guess for a call
[3128.26 --> 3132.96]  to arms you know you got a wide landscape of programmers out there uh newbie programmers
[3132.96 --> 3139.06]  well well to fit programmers but you know in what way um you know with ruby off rails or any other
[3139.06 --> 3145.18]  open source program or i guess project you're working on um you know how can people lift up what
[3145.18 --> 3151.22]  you're doing how can people take part in or do more with whatever you're doing um so it's interesting
[3151.22 --> 3157.14]  i uh i wrote down here what i when you told me about the the call to arms uh with open source and
[3157.14 --> 3163.34]  stuff like that and so what i wrote was um that i recommend that everybody either join a rails girls
[3163.34 --> 3174.20]  um so this is a local organization that goes out and hand and does free workshops to teach uh both women
[3174.20 --> 3181.32]  and and you know but mostly women uh but men can come too if they bring a uh a somebody that wants to
[3181.32 --> 3188.54]  learn and and so these workshops are free and they're great so join one or start one uh find one and
[3188.54 --> 3196.18]  coach at one uh or just donate to one so like i'll find uh if i hear about one and i'll ask like hey
[3196.18 --> 3201.80]  how you doing and then you know like donate like buy breakfast for everybody or something um and so
[3201.80 --> 3207.70]  that that works with me for hey these people obviously have um you know an interest in ruby so
[3207.70 --> 3215.50]  then we know we do a coupon or um you know stuff like that so i recommend everybody uh it you know go to
[3215.50 --> 3222.36]  one or look at what tutorials they have and and learn and and submit and help with that um so along
[3222.36 --> 3231.72]  that is try and create like just getting started tutorials for people and then and then have them
[3231.72 --> 3238.76]  and then you know blog about them i know that a lot of times we like to write posts that are you know
[3238.76 --> 3246.02]  10 000 words long and and our uh treatises about like you know about like the intro dissertations
[3246.02 --> 3255.04]  yeah um but but if you're like what works great the um adam you mentioned it earlier is the jumpstart
[3255.04 --> 3263.14]  labs tutorials um those are fantastic i think those are really really good i love the the pace that
[3263.14 --> 3269.60]  jeff teases up with um i don't know if jeff is the sole maker of those i know he's got a steve klabnik
[3269.60 --> 3276.20]  uh also part of the changelog here he's a teacher at g school so i don't know if other teachers uh at
[3276.20 --> 3281.70]  jumpstart take part or g school take part but i love the pace that those are those are really great
[3281.70 --> 3289.40]  yeah so fantastic and so like create stuff like that that helps yeah you know and and say what they
[3289.40 --> 3294.32]  are you know are is this for beginners or is this for intermediate or the expert i think that that's
[3294.32 --> 3301.82]  some of what's missing um about that that's out there um okay so that's that's mine that's yours
[3301.82 --> 3308.36]  i also want to add something to that because you mentioned rails girls and uh for those who are fans
[3308.36 --> 3313.64]  of the changelog here in houston for one if you see me around say hi uh two rails girls is coming to
[3313.64 --> 3320.96]  houston july 26th to 27th so you can actually go to rails rails girls.com slash houston of course
[3320.96 --> 3328.16]  and rsvp on facebook uh to do that as jesse mentioned uh you uh you're welcome if you're a
[3328.16 --> 3333.50]  man but you got to bring a woman uh who wants to code so that's uh that's i think that's a prerequisite
[3333.50 --> 3338.32]  right something like that that's exactly right um yeah and i think the other cool question we get to
[3338.32 --> 3343.90]  ask on this show which i think is you know uh we we kind of joked in the the pre-call about it could
[3343.90 --> 3348.70]  be a top 10 list if you wanted it could be uh like david letterman style you know count down from 10 to
[3348.70 --> 3355.08]  one if you want if you've got 10 great but uh who is your programming hero okay so i had three and i
[3355.08 --> 3361.70]  tried to cut it cut any one of them down and uh and i it it just couldn't couldn't happen so number
[3361.70 --> 3369.22]  one is aaron patterson so tender love on on twitter um and so i mean he's just been tirelessly making
[3369.22 --> 3375.54]  rails better and he's also got like a slew of other projects um and and so like what he's been doing in
[3375.54 --> 3381.24]  the rails code base crazy awesome um and then he's really been pushing the state of the art of pun
[3381.24 --> 3389.68]  driven development i mean if you just go and look at his uh um repositories on github i mean they just
[3389.68 --> 3396.66]  make you laugh um so i just saw something on twitter i think it was something pun driven something
[3396.66 --> 3403.56]  recently like literally sgi about fell over laughing i'm pretty sure that's it i did not make that up i
[3403.56 --> 3412.06]  saw that i saw that on twitter um and okay so number two is uh is yahooda cats so for someone who has not
[3412.06 --> 3419.36]  been programming all that long to to been involved in like merv jquery rails 3 and ember i mean it's just
[3419.36 --> 3428.98]  crazy um crazy talented so um so yeah props that and then last is uh is uncle bob um and so i mean i
[3428.98 --> 3433.98]  just hope that i can be programming in 30 years telling everybody uh that they're doing it wrong
[3433.98 --> 3442.18]  um you know something like hey back in my day we had to worry about memory and threads um so uh so yeah
[3442.18 --> 3449.08]  that that that's my three there you go um i'm gonna i guess tee up a maybe a brand new question for the
[3449.08 --> 3454.66]  show which is if you weren't programming in ruby or i guess for future guests this be if you weren't
[3454.66 --> 3462.30]  programming in whatever language is your choice which would you be programming in so um i've got
[3462.30 --> 3470.20]  three that i'm looking at right now trying to decide which one i really want to um dive into um so this
[3470.20 --> 3475.86]  i guess i'm gonna not answer your question but i will talk about three programming languages one is uh
[3475.86 --> 3484.94]  is go um that my trouble with go is it's uh is it's syntax coming from ruby it sort of grates on me
[3484.94 --> 3491.96]  but it is the camel case to get you it's not so much the camel case but it's the uh it's the colon
[3491.96 --> 3500.72]  equals to do assigns uh i i spent some time um in delphi and it brings up it brings up bad memories
[3500.72 --> 3511.04]  um and but it does like straight performance wise um i mean it just it just nails it so um i think to
[3511.04 --> 3518.90]  learn to not learn that would be um not a wise decision in the next you know couple years uh other
[3518.90 --> 3526.72]  than that i really like uh elixir right is a is a fun little language on top of erlang um and then
[3526.72 --> 3535.06]  the last as all ruby programmers eventually talk about is closure um and so so what's interesting
[3535.06 --> 3542.82]  about that right is like two functional languages so that's sort of my next um you know thing to
[3542.82 --> 3549.94]  tackle and to to to to look at very cool well just it's definitely been uh fun having you on the show
[3549.94 --> 3554.50]  um i think it's really awesome that you're like tim had said you know you're you're kind of
[3554.50 --> 3561.92]  being the teacher being the mentor and and maybe even being the placement person um for some future
[3561.92 --> 3567.58]  students that you have um uh it's been obviously great having you on the show we we broadcast this
[3567.58 --> 3573.34]  show live every tuesday at five i know the show was aired a little earlier than normal but that
[3573.34 --> 3578.56]  happens sometimes so catch us next tuesday at five we're not sure on the guest yet and i know
[3578.56 --> 3584.94]  andrew's pinning down a couple new guests but uh definitely tune in so thanks jesse to you for
[3584.94 --> 3591.24]  joining us and tim especially thanks for you to be a guest host today it's definitely fun having
[3591.24 --> 3594.62]  on the show so let's say goodbye guys bye bye
[3594.62 --> 3595.12]  you
