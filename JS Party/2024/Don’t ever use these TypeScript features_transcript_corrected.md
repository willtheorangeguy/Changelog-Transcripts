[0.00 → 14.28] this is js party your weekly celebration of JavaScript and the web check us out on the web
[14.28 → 23.54] at jsparty.fm there you'll find lists of our recommended and popular episodes clips aka js party
[23.54 → 29.72] the good parts and a request form so you can let us know what you want to hear about on the pod
[29.72 → 35.80] big thanks to our partners at fly.io over three million apps have launched on fly
[35.80 → 42.08] deploy yours in five minutes learn how at fly.io okay hey it's party time you all
[42.08 → 58.38] hello world it's your internet friends
[58.38 → 62.94] here with another js party nick needed is in the house what's up nick
[62.94 → 71.84] ahoy hoy to you how's life how's everything it's an it's a whirlwind of delight oh I thought
[71.84 → 77.34] you're going to go for ghoulish overkill again like you did last episode but a whirlwind of light
[77.34 → 84.48] sounds better than ghoulish overkill Chris Miller is also here bone skull how are you doing all right
[84.48 → 90.66] hope everybody's having a nice weekday whatever weekday it is well whatever weekday it is where
[90.66 → 96.30] you're listening we hope it's good where we are recording its Friday which tends to be of all the
[96.30 → 103.30] weekdays one of the best doesn't it definitely top three yes for sure top five i would hazard
[103.30 → 109.40] to say top three as well, well we have a fun docket today we're going to talk some news we're going to
[109.40 → 117.20] play a song, and we're going to uh discuss Node.js because that's what we do around here on the
[117.20 → 126.22] JavaScript and web dev party show that you're listening to starting right away with SPAC the
[126.22 → 134.66] next generation you know Star Trek was a pretty good show but TNG was a great show especially if you
[134.66 → 139.54] skip season one and go straight to season two where they really caught their stride and figured
[139.54 → 145.30] it out nick response you open your mouth i was shocked that you said that and then i just
[145.30 → 151.92] remember trying to start TNG and season one like the q episode whatever the first one I fell asleep
[151.92 → 159.26] four times it's so bad what podcast am I on right now what do you guys why Star Trek the next
[159.26 → 164.52] generation does that have to do with anything because I just said we're talking about SPAC the next
[164.52 → 170.66] generation JavaScript bundler and I was making a pop culture reference to Star Trek the next
[170.66 → 180.40] generation oh have you seen that show Chris yes do you like TNG yeah how do you feel about season one
[180.40 → 186.74] I don't know the worst season I would hazard even though I don't last time I watched it was when it
[186.74 → 193.04] was on TV okay oh wow that's when I watch it too and then I try to go back and I thought as I try to do
[193.04 → 197.42] with Seinfeld start at season one, episode one, and it's like yeah you can skip season one of Seinfeld
[197.42 → 201.78] also you know it takes a little while for these shows to really like find themselves and catch their
[201.78 → 206.56] stride and I just feel like as a public service announcement I'm just telling folks skip season
[206.56 → 212.98] one start at season two you're going to enjoy that the next generation SPAC a JavaScript bundler
[212.98 → 217.56] written in can you guys guess which language this is going to be written in it's a next generation
[217.56 → 222.14] ruby that would be last generation that would be the original Star Trek
[222.14 → 227.68] oh I thought it was spec sorry no SPAC s-p-a-c-a that's a good guess though
[227.68 → 235.18] um it's not space nine it's not voyager it's written in rust come on guys you could have guessed
[235.18 → 241.46] that right written one to all next generation JavaScript build tools are written in rust aren't
[241.46 → 249.84] they yeah I mean you kind of have to it's pretty much what's happening do you though I mean
[249.84 → 255.28] I think if you want GitHub stars you absolutely if you want to be next generation you have to
[255.28 → 263.12] write it in rust yeah but I guess but aren't things just fast enough no apparently not because the SPAC
[263.12 → 271.16] team didn't think so they have written this bundler in rust it's compatible with the webpack API
[271.16 → 277.42] and ecosystem, and it is 10 times faster than webpack
[277.42 → 286.04] neither you guys care do you Chris is like I haven't used webpack in years I know of webpack
[286.04 → 293.06] okay and uh Nick's like I just use typescript all the time i just you know I'm excited and I don't
[293.06 → 299.20] want to like it's awesome it's awesome that it's rewritten in that but if we start seeing webpack
[299.20 → 305.50] configs pop up again like what is this all for I still have a webpack config I'm excited because
[305.50 → 310.24] I still have a webpack config you have to move to meet baby yeah you're on the meet train I just didn't
[310.24 → 315.84] want to rewrite anything like I didn't want to touch my config so I just continue to use webpack and it
[315.84 → 322.68] builds everything in about three seconds perhaps but I'm thinking like 300 milliseconds that would be
[322.68 → 326.72] 10x faster wouldn't it what are you going to do with those 2.7 seconds
[326.72 → 333.84] you know how many times that you compile it compounds nick it compounds I mean before long
[333.84 → 340.42] it's going to be an entire minute of savings wells you know it may not be that exciting to us right but
[340.42 → 349.52] there are a ton of people still using webpack which you know I can't, I can't speak to how much of a
[349.52 → 358.00] drop-in replacement it is i I can't imagine it would maybe it just works but um you know
[358.00 → 364.20] certainly if you can speed things up and you don't have to go in there and change a bunch of
[364.20 → 369.74] stuff oh yeah that's great yeah good news yeah that is a good point like I was totally not thinking
[369.74 → 375.10] of it from that point i was totally thinking like oh here comes the return of 400 line config files
[375.10 → 380.92] oh you think they've gone somewhere no they're still around yeah if you still have those
[380.92 → 388.40] around then you just get these benefits for free yeah that's great actually, so this is pitched as a
[388.40 → 394.08] tool for enterprises and many have been using this, so this is built by the
[394.64 → 403.38] byte dance team of TikTok fame right isn't byte dance TikTok yes, yes and so it's used at TikTok
[403.38 → 411.14] it's also used at places like Microsoft Amazon intuit discord and others so lots of big webpack
[411.14 → 416.58] configs probably floating around those organizations and yeah like you said if you can just not have to
[416.58 → 424.24] rewrite anything and take your three-second compilation down to 300 milliseconds why not but
[424.24 → 430.90] even better take your 13-second one down to 1.3 seconds if I'm doing my divisions by 10 accurately
[430.90 → 438.46] that's a pretty good win for relatively free right yeah definitely all right well congrats on the
[438.46 → 445.12] SPAC team for hitting their 1.0 and uh hopefully if you didn't hear about it before, and you have a
[445.12 → 452.64] big fat slow webpack config in your life you can make it a big fat fast webpack config with SPAC
[452.64 → 465.40] moving on to our favourite server-side runtime Node.js have you heard of it yes you have how about
[465.40 → 471.62] typescript have you heard of it oh yeah node and typescript are like good friends now they've
[471.62 → 476.54] tightened their relationship we talked about it last time nick was all in a tizzy about it
[476.54 → 483.04] he called an emergency pot over this because node added support for stripping the typescript types
[483.04 → 488.10] which means you can write typescript, and it will ignore it and just run it like JavaScript right
[488.10 → 495.10] which is a step without a build step and as of node version 22.7 which I think is probably the
[495.10 → 502.34] release right after 21 if incrementing things works the way it used to uh there's another new flag
[502.34 → 510.14] it's called experimental not strip types transform types and uh what does this do well nobody knows
[510.14 → 516.48] no just kidding its possible now to enable this transformation of typescript only syntax into
[516.48 → 523.82] JavaScript code which allows support for typescript features such as enum or enum if you will and
[523.82 → 530.70] namespace so I assume there's something about these nick that they can't get stripped or yeah those are
[530.70 → 538.54] to well enum specifically is like the way that it writes if it's creating this like complex looking
[538.54 → 546.74] object in typescript okay to emulate that so that you can still have like the enum like calling
[546.74 → 553.20] of that enum everywhere like you know uh direction. North or whatever, and it'll be an object called
[553.20 → 559.22] direction that has a north property on it that then has a string or whatever value for it this will
[559.22 → 563.72] transform it if it works like typescript it'll just transform it into that object which is great
[563.72 → 567.98] so it's the kind of thing you couldn't strip because it's useful code like you're going to be
[567.98 → 572.02] using that I just want to I'm trying to understand why you transform it instead of just strip it
[572.02 → 578.12] because it's not a type it's you know I'm special in that it's not it can't be stripped okay because
[578.12 → 584.20] it actually just it compiles down to a JavaScript object a JavaScript object I see there's
[584.20 → 589.60] continuum that is stripped what's continuum do that would like if you had a value it'll just
[589.60 → 596.96] replace it at compile time with whatever the value is I see likewise I think namespace is uh
[596.96 → 606.82] another I assume they just treat it like an object like an object create null type object and you just
[606.82 → 612.26] throw properties in there, but that also would need to be compiled down you cannot strip a namespace
[612.26 → 619.16] fair so if this was a two-phase adoption of typescript support phase one would have been
[619.16 → 624.18] well let's strip all the types we can just strip and now phase two would be there are a few edge cases
[624.18 → 629.42] or things that you can't strip because they have to be actually included in the compiled product and
[629.42 → 636.88] so now let's go ahead and add support for transforming them into JavaScript at build time or at node not
[636.88 → 644.72] build time but node run time and now that's there so no uh no emergency pod for this one, but he's
[644.72 → 651.48] he's still smiling he's he's still grinning because it further deepens typescript support in node
[651.48 → 659.68] however this is an experimental flag which means don't rely on it because it may go away oh
[659.68 → 667.02] I thought I just meant it's going to be normal later no that is not what experimental means a lot of
[667.02 → 675.72] things most things that are experimental become stable you know right some things go bye-bye so you
[675.72 → 683.72] need to be careful if you want to rely on experimental flags I'm also kind of part of team don't ever use
[683.72 → 689.48] these features in typescript uh the enum in namespace or yeah okay why is that I don't like
[689.48 → 697.14] that enum specifically are they're like opaque right so you have to if I want to use a string value
[697.14 → 704.40] a literal like a string literal union is better than me having to also import this object to
[704.40 → 710.84] set the same string value essentially I'm just lazy so you're against enum as a feature
[710.84 → 717.06] in general not as a typescript feature as a yeah as like a list of hard-coded strings I would rather
[717.06 → 722.74] just have a list of hard-coded strings yeah I don't think that you get the type benefit any
[722.74 → 727.62] additional type benefit from that maybe you get some refactoring benefit, but it's not that much
[727.62 → 733.98] okay and Chris you were in agreement with Nick's premise is it for the same reason yeah I mean I don't
[733.98 → 745.26] use them i you know if I want to refer to something by a variable name like I will make a object and
[745.26 → 753.82] and call it coast and import that and just use the know food. Bar or whatever I want to use
[753.82 → 761.58] yeah it, and then you know you can extract a type from that easily like type of key of and then there
[761.58 → 767.70] you go okay you're all set and namespace similar logic namespace used to be module like that's yeah
[767.70 → 772.42] before modules were a thing in JavaScript it was module, and then they renamed it to namespace and
[772.42 → 780.46] i I never used it once they're they're basically not needed any more you know ESM and the whole
[780.46 → 787.90] module system essentially just it just supersedes it, but certainly there's probably some old
[787.90 → 792.84] typescript code that's using namespace I think typescript itself used it for a long time
[792.84 → 798.46] I think they might have switched away from it, but it's it as far as I understand that and
[798.46 → 804.84] or maybe enum is regretted like we probably shouldn't have done that but
[804.84 → 809.94] you know namespace was kind of well we need something so we're going to have to do this
[809.94 → 814.64] and it's just kind of a vestige at this point gotcha
[814.64 → 831.20] okay friends I'm here in the breaks with Annie sexton over at fly, and you know we use fly here
[831.20 → 836.46] at changelog we love to fly it is such an awesome platform, and we love building on it but for those
[836.46 → 843.02] who don't know much about fly what's special about building on fly gives you a lot of flexibility
[843.02 → 849.42] like a lot of flexibility on multiple fronts and on top of that you get so I've talked a lot about
[849.42 → 855.64] the networking and that's obviously one thing, but there are various data stores that we partner with
[855.64 → 862.08] that are really easy to use um actually one of my favourite partners is Tigris I can't say enough good
[862.08 → 867.22] things about them when it comes to object storage I've i never in my life thought I would have so many
[867.22 → 873.62] opinions about object storage but I do now Tigris is a partner of fly, and it's s3 compatible object storage
[873.62 → 879.94] that basically seems like it's a CDN but is not it's basically object storage that's globally distributed
[879.94 → 885.62] without needing to actually set up a CDN at all it's its like automatically distributed around the world
[885.62 → 891.62] um, and it's also incredibly easy to use and set up like creating a bucket is literally one command
[891.62 → 897.06] so it's partners like that I think are this sort of extra icing on top of fly that really
[897.06 → 902.72] makes it sort of the platform that has everything that you need so we use Tigris here at changelog
[902.72 → 909.16] are they built on top of fly is this one of those examples of being able to build on fly yeah so Tigris
[909.16 → 914.20] is built on top of fly's infrastructure and that's what allows it to be globally distributed I do have a
[914.20 → 921.06] video on this but basically the way it works is whenever like let's say a user uploads an asset to
[921.06 → 926.54] a particular bucket well that gets uploaded directly to the region closest to the user whereas
[926.54 → 930.62] with a CDN there's sort of like a centralized place where assets need to get copied to and then
[930.62 → 935.02] eventually they get sort of trickled out to all the different global locations whereas with Tigris
[935.02 → 939.78] the moment you upload something it's available in that region instantly, and then it's eventually
[939.78 → 944.74] cached in all the other regions as well as it's requested in fact with Tigris you don't even have to
[944.74 → 949.90] select which regions things are stored in you just get these regions for free and then on top of that
[949.90 → 957.00] it is so much easier to work with i I feel like the way they manage permissions the way they handle
[957.00 → 964.16] bucket creation making things public or private is just so much simpler than other solutions um and the
[964.16 → 968.02] good news is that you don't actually need to change your code if you're already using s3 it's s3
[968.02 → 972.28] compatible so like whatever SDK you're using is probably just fine and all you got to do is update
[972.28 → 979.48] the credentials so it's super easy very cool thanks Annie so fly has everything you need over three million
[979.48 → 985.86] applications including ours here at changelog multiple applications have launched on fly boosted
[985.86 → 993.44] by global any cast load balancing zero configuration private networking hardware isolation instant wire
[993.44 → 998.90] guard VPN connections push button deployments that scale to thousands of instances it's all there for
[998.90 → 1006.00] you right now deploy your app in five minutes go to fly.io again fly.io
[1006.00 → 1018.92] I triple e spectrum which I believe is a website and a used to be a publication it might even still be
[1018.92 → 1028.88] kind of magazine from I triple e a journal if you will yes have published on the 22nd of august
[1028.88 → 1038.18] the top programming languages of 2024 and python wins so surprise what's that to do with
[1038.18 → 1045.08] js party well java second place that's we're halfway there we're halfway to JavaScript third place
[1045.08 → 1055.92] JavaScript with 0.4451 that would be I guess 44 percent of respondents I suppose I haven't gone deep on
[1055.92 → 1062.94] this data set but then what's interesting is c plus comes in and forth which fine it's its just been
[1062.94 → 1070.56] there forever and then fifth are you ready for it typescript this is why I pulled this story in because
[1070.56 → 1076.28] hey we're getting screwed people we should be higher up the list I mean typescript and JavaScript
[1076.28 → 1081.84] it's all the same thing isn't it nick I was going to say if you just add those two together then it's like
[1081.84 → 1089.08] 0.6 something that's what I'm saying we could be we could be number I guess not number one we could
[1089.08 → 1094.34] be number two we could beat java which honestly we're beating java aren't we beating java are we
[1094.34 → 1100.08] on three billion devices probably I would think so anywhere that java is running there's a web browser
[1100.08 → 1105.80] right that's a large assumption that I can't exactly process I'm like is that right I don't know
[1105.80 → 1112.92] there are a lot of caveats in their perhaps clicking through this horrible website I've found the
[1112.92 → 1119.10] methodology, and it looks kind of skewed towards academia just for what it's worth well it is i
[1119.10 → 1123.62] triple e spectrum so that that would make some sense because their audience is more formalized and
[1123.62 → 1132.62] academic some major proportion of the very few sources that they use are in academia so
[1132.62 → 1140.62] rounding out the top 10 you have SQL not a language it's a language the l stands for language
[1140.62 → 1148.52] but is it a programming language is SQL Turing complete it probably is uh is it a programming
[1148.52 → 1156.62] language it's kind of not it's a declarative query language but whatever followed by c sharp go
[1156.62 → 1166.36] good old-fashioned c and then hey HTML baby it's official HTML is a programming language even the
[1166.36 → 1175.04] academics will confess it I won't argue with that I will with SQL my wife has to do SQL for her job
[1175.04 → 1181.02] yeah and I'm always like oh you should learn more programming, and she's like no I hate it because I hate
[1181.02 → 1191.52] SQL I'm like don't base it on SQL right have you introduced her to llama 3.1 uh no because I don't
[1191.52 → 1197.54] really write SQL anymore I write plain English SQL that gets turned into actual SQL and that's been
[1197.54 → 1202.14] pretty nice that's been a life improvement for me, I mean that's what alms have done in my life is like
[1202.14 → 1207.90] you know copy and paste SQL you know you don't actually author it directly which has been an improvement
[1207.90 → 1214.10] because I use it all the time but just you know is it an inner join is it a left outer join how do i
[1214.10 → 1220.52] you know like gosh who has time for that not me but I do have time to say here's what I'm looking at
[1220.52 → 1224.46] and then I get a query that's close enough, and then you can tweak it from there so maybe she would
[1224.46 → 1233.84] benefit from that hey word are you an elixir guy yes it's 35th ouch well you know that's academia
[1233.84 → 1239.00] they don't know what they're doing just kidding it's beaten out by assembly more people writing
[1239.00 → 1250.48] raw assembly than they're writing elixir that's kind of embarrassing well I'm sorry oh gosh yeah
[1250.48 → 1256.76] well it's not the most popular language, but it doesn't make it bad what's ABAP sounds like a
[1256.76 → 1263.60] acronym does anybody know what that means that is what a b a p a b a p I've never heard of that
[1263.60 → 1268.74] in my life and I've heard almost every tech acronym there is advanced business application
[1268.74 → 1278.34] programming according to Claude ah okay this looks like a sap thing oh okay yeah I think this survey
[1278.34 → 1287.52] is invalid I think you've proven it I mean you know if people do this for a living then I think it
[1287.52 → 1296.70] counts mac helps put food on the table you know I had my first encounter with uh with Django a few
[1296.70 → 1301.54] months ago oh really which was my first encounter with python for the most part aside from Arduino
[1301.54 → 1308.02] like simple Arduino stuff and I was like trying to get it running and upgrade things and I'm like how
[1308.02 → 1313.56] the heck are dependencies managed in this do you know where they put dependencies in python
[1313.56 → 1321.60] requirements.txt requirements.txt yes i I felt like I was blown away I'm like you're so disappointed
[1321.60 → 1328.54] yeah don't you like text files nick I mean you know Jason files are just text files with a different
[1328.54 → 1335.30] file extension no, but my editor knows how to syntax highlighted Jason file I bet it knows how to do
[1335.30 → 1341.64] requirements.txt too not mine okay well you have to install the python extension or something
[1341.64 → 1347.26] the syntax yeah i that I always thought that was uh what's the word I don't know rudimentary or
[1347.26 → 1353.80] it's probably from the late 90s yeah oh that's been around forever yeah yeah that's how Chris and i
[1353.80 → 1359.58] both knew it and every year somebody comes up with a new way to do package management
[1359.58 → 1366.46] in python yes I've had lots of conversations about package management in python and I've been told by
[1366.46 → 1371.50] Brett cannon who's the closest friend who does python he used to be on the steering council or
[1371.50 → 1377.66] whatever that pipe is the way to go so after he told me that I just quit wondering what to do and
[1377.66 → 1382.16] like I use pipe all the time not because it's best but because Brett cannon told me it's the way to go
[1382.16 → 1388.42] so that was just good for me wait what's pipe he didn't tell me that part
[1388.42 → 1398.80] pipe is a version a package installer like pip which is the was a python package installer that you
[1398.80 → 1404.80] probably know of only it installs everything locally and so it's all siloed and stuff and not
[1404.80 → 1409.86] like system-wide and so it's a nice way of just like because a lot of times when you're installing
[1409.86 → 1414.36] python stuff you're not really writing python I mean I'm not I'm just like I want to use this tool
[1414.36 → 1418.82] that happens to be written in python, and so I want to install it on my system I don't want to like
[1418.82 → 1424.50] screw up whatever apple's doing with python on my system I just feel like if you install it
[1424.50 → 1429.50] the pip way you're just like blowing your user local away, or you're just like I don't know I'm
[1429.50 → 1434.90] going to break something that apple doesn't want me to break but pipe is like put it all in your own
[1434.90 → 1439.48] little I think it's your home directory or something you know let homebrew deal with it if you just
[1439.48 → 1444.82] need to use like a python script a lot of python scripts you can't just brew install if is they're
[1444.82 → 1451.80] good you should be able to it's like the brew install python dash whatever it is
[1451.80 → 1457.10] brew install python dash no, no no, no no that's that's the name of the package we'll
[1457.10 → 1463.06] just start with gotcha I will go on record to say that probably five tools that I've tried to
[1463.06 → 1468.18] install this year mostly around trying to use language models and whisper and stuff like this
[1468.18 → 1474.20] for transcriptions have not had brewed install they've all just been like pip install and i just
[1474.20 → 1480.00] I get nervous and I'd like wild west yeah well the python's packaging story has never been solid
[1480.00 → 1486.52] hence requirements.txt good language though Nick did you enjoy your time with white space significance
[1486.52 → 1493.48] why would anybody do that give me those sweet curly braces the sweet embrace it's cleaner dude you just
[1493.48 → 1497.64] indent you're going to indent anyway I know why not just make the indent matter
[1497.64 → 1504.08] it's a good question my eyes just don't scan after using curly braces for
[1504.08 → 1509.94] every other year of my life my programming years don't you use tabs though I don't I don't
[1509.94 → 1515.54] even know any personally don't you use tabs over spaces whatever prettier changes it too I don't even
[1515.54 → 1520.38] care any more okay well the reason I ask that is because you can make those tabs real big yeah
[1520.38 → 1526.34] and that indentation is real significant I actually used to show significant white space like yeah in my
[1526.34 → 1533.06] like I'd had invisible characters displayed for tabs and spaces and all that sure and after just like
[1533.06 → 1537.88] becoming so comfortable with prettier just rewriting everything I was like why do I even care
[1537.88 → 1541.88] why do I need to see this anymore because if i accidentally type a tab it's going to go away
[1541.88 → 1550.02] as soon as I save so sure I think that's fair but not in python not in YAML not in Lua etc etc etc
[1550.02 → 1555.60] etc Lua is a language that I really like that I guess doesn't have curly braces as much
[1555.60 → 1562.66] dude lua is indexed by one yeah so I have a hard time even just a just even giving it the
[1562.66 → 1569.94] time of day but I mean who indexes their arrays by in by one literally just Lua when like in
[1569.94 → 1576.48] today's world where I'm not like you're way less inclined in any other language to write a for loop
[1576.48 → 1582.34] i I would say would you agree uh in what language no in any language to write a for loop
[1582.34 → 1588.08] wouldn't you use like a for each method or a some other iterator method or have you ever
[1588.08 → 1593.66] written go it's all for loops goes entirely for loops they have no other iteration techniques
[1593.66 → 1595.14] that's why I haven't written go
[1595.14 → 1603.98] I use for loops in elixir there's also there are all kinds of iterators but every once in a while like
[1603.98 → 1608.26] the for loop is actually pretty functional, but you don't actually have index references there either
[1608.26 → 1612.54] so you can if you want them yeah, but it's a different kind of for loop it's not like a
[1612.54 → 1618.50] zero index for loop c plus I mean come on man aren't you polyglot you're ever writing anything
[1618.50 → 1626.22] besides typescript I'm writing PHP now but my point is zero indexed yeah, but my point is I don't care
[1626.22 → 1630.92] about the zero index I never am like you don't do for loops trying to get at the zeroth index I'll get
[1630.92 → 1637.22] I'll like push or pop or what is it unshifty or like you use some method to get at it
[1637.22 → 1643.16] unshifty isn't that destructive yes no don't ever do that dude you're gonna totally regret that move
[1643.16 → 1650.88] immutable mutations' no I'm kidding I'm kidding immutability please I don't want to mutate my
[1650.88 → 1655.12] that was my problem with ruby is there are so many different ways to mutate the current thing that i
[1655.12 → 1660.30] I did it on accident a bunch you know and I'm like oh crap just monkey patch a new way to do it and
[1660.30 → 1666.04] then exactly ruby is the best programming language if you don't need to show this code to anybody
[1666.04 → 1671.68] because you can just monkey patch like the core objects and have all very nice utilities for
[1671.68 → 1675.28] yourself and like just don't ever share that because no one's going to know how it's working but
[1675.28 → 1682.26] it's very malleable and makes writing like stuff very enjoyable as long as it's not to be
[1682.26 → 1687.98] collaborated on everything's just in method missing right well you can definitely do that too yeah I think
[1687.98 → 1694.40] nick is right about Lua at least i I've written a fair amount of Lua and have never worried about that
[1694.40 → 1700.06] like I don't worry about the index about the one index no, no you never for you never do a for loop
[1700.06 → 1705.48] and then you had to start with one no I don't use a for loop they have like okay some I can't think of
[1705.48 → 1710.78] the syntax off the top of my head but like there 's's some method or some like language construct
[1710.78 → 1717.44] to just like loop through everything without me having to explicitly get access to the nth index of
[1717.44 → 1723.92] the object or of the table to get at something like it'll just give me you know an iterator to
[1723.92 → 1729.58] go through it so you're saying it's inconsequential yes and I'm saying why they do it then what's the
[1729.58 → 1736.10] point like why don't you just conform to the other languages man that's that's true I guess I'm actually
[1736.10 → 1740.28] I mean I've I've heard great things about Lua never written any Lua I just like to make fun of it
[1740.28 → 1746.48] because of that, but it's a came over to it because of neo vim and I like I really like it for that and
[1746.48 → 1751.50] now I use it for a bunch of other things I started is it just is it configuring neo vim or is it like
[1751.50 → 1758.16] extending it configuring it yep so you probably don't do very much looping there anyway I do
[1758.16 → 1763.54] actually like what would you loop over in your config I have like oh all your plugins
[1763.54 → 1771.46] yeah for each plugin I would install it, but then it's like looping through things like uh
[1771.46 → 1777.06] looping through like the set of language servers that I want to set up and doing specific things
[1777.06 → 1781.62] for specific ones, or you know things like that so it's like an array and the array is only just
[1781.62 → 1785.66] typescript, and it just loops over if it's like sets up the typescript server, and you're done pretty
[1785.66 → 1793.34] much pretty all right fair enough moving on now that we've covered languages that aren't web
[1793.34 → 1797.88] development languages although I'm sure you can run all this language in a web browser
[1797.88 → 1804.36] via Wasm or some other technique transpiration of course we don't have to do that we have pretty
[1804.36 → 1809.28] good languages in our browsers now actually i was trying to remember but that Lua stuff and
[1809.28 → 1817.24] then I remembered oh I stopped using Lua because i kind of hated it and what i ended up doing
[1817.24 → 1823.32] instead was using this thing called moon script which is like coffee script for Lua oh wow
[1823.32 → 1828.72] yeah so you're drinking it yeah you're putting some uh moon script additional stuff in your Lua
[1828.72 → 1833.90] moon script huh moon script, and you hated moon script, or you hated Lua so you went for moon script
[1833.90 → 1839.92] I didn't like Lua it's a little too uh I don't know they they they don't use like many sigils
[1839.92 → 1847.58] you know what I mean they don't use like curries or braces so much it's uh it can be kind of verbose
[1847.58 → 1854.44] I got type sick of typing function essentially the word function the word function and so moon
[1854.44 → 1859.30] script stops that from happening moon script I still write out the word function when I'm writing
[1859.30 → 1866.28] JavaScript my mouth is agape right now it is agape for our listeners it's just you know I'm old and
[1866.28 → 1871.42] I've been writing function for 20 years I'm just going to keep writing it now there are times when I need
[1871.42 → 1877.20] the facilities of the fat arrow, and so I'll use that function style like the closures and stuff but
[1877.20 → 1884.98] I just write function so in Lua it looks like four key uh comma value in something or other and that's
[1884.98 → 1890.54] your that's your iterator four key comma value and that key starts with one yeah well it's a
[1890.54 → 1895.28] you're you're in for a hash you don't need to use it's all tables it's all yeah it's all tables
[1895.28 → 1903.72] okay it's the holy SAS Ben I'm looking at this moon script and you really this is way more
[1903.72 → 1908.82] significant white space you must like significant white space Chris, but it has like arrow
[1908.82 → 1915.44] functions so I was like more comfortable what were you writing this for oh god satisfactory plugins
[1915.44 → 1923.36] what's satisfactory plugins are like good enough like mods like it's like plugins for a satisfactory mod
[1923.36 → 1930.44] written in their Lua but I use moon script anyway but I've written stuff for like compute
[1930.44 → 1934.78] computer do you know what satisfactory is and I'm ignorant or are we both in the dark here
[1934.78 → 1941.22] what's satisfactory Chris satisfactory is a factory building game um like factor, and you automate
[1941.22 → 1948.14] things, but there are's a modding scene of course, and it gets all sure complex if you like
[1948.14 → 1952.28] that sort of thing yeah Lua really has its niche in like game embeddable game
[1952.28 → 1959.12] yeah I've written Lua stuff for computer craft or open computers and minecraft as well
[1959.12 → 1965.34] minecraft scripting API nowadays JavaScript baby it's all JavaScript I know that because i just
[1965.34 → 1969.84] interviewed it's both written in JavaScript, and you can use JavaScript of course there's other
[1969.84 → 1977.44] languages as well wait what the mine scripts the minecraft API the scripting API mine script
[1977.44 → 1981.86] minecraft you know the game minecraft is that what you said minecraft that's what I was talking about
[1981.86 → 1988.00] minecraft it's all JavaScript now what are you talking about minecraft the scripting API okay
[1988.00 → 1996.68] minecraft is written in java, and it's also rewritten in c plus right 100 the minecraft scripting
[1996.68 → 2002.32] API like all the modding stuff that you can do inside of minecraft is JavaScript oh right i just
[2002.32 → 2007.10] interviewed the two guys that run the show over there oh yeah yeah yeah, and you can use JavaScript
[2007.10 → 2013.96] it's not no you can use JavaScript to write mine script minecraft mods, but some people do some people
[2013.96 → 2019.64] don't 100 I'm just saying you don't need to use Lua anymore or moon script well you do if you want
[2019.64 → 2027.86] to write programs for computer craft I'm talking about minecraft computer craft is a minecraft mod
[2027.86 → 2034.56] written in I don't care because it doesn't matter to me but it is provides like an operating system
[2034.56 → 2042.18] and all the code you write is Lua okay that's what that's the kind of minecraft scripting you like to
[2042.18 → 2047.90] do is computer craft so is this an is this you install minecraft, and then you mod it with computer
[2047.90 → 2053.58] craft, and then you mod computer craft with Lua yes okay but to solve all of your problems there is a
[2053.58 → 2064.82] typescript to Lua compiler bam nick wins again and maybe somebody's written some Lua for computer
[2064.82 → 2070.50] craft that transpire like you can write JavaScript to write computer craft code I'd probably somebody
[2070.50 → 2077.16] has done this if a typescript to Lua converter exists then certainly it's possible and i
[2077.16 → 2082.08] didn't know that and so now I'm going to go back to my moon script and rewrite it in typescript bam i
[2082.08 → 2086.06] support this, so nick really just made your days I mean this made it all worthwhile for you to show
[2086.06 → 2093.96] up for this particular show because now you can just ditch moon script forever I feel like everybody's
[2093.96 → 2100.78] ditched moon script I've never heard of moon script but I'm looking at the syntax and I like
[2100.78 → 2105.10] significant white space this looks like a nice little language you would yeah it's just kind of
[2105.10 → 2110.44] like coffee script yeah and I liked coffee script as well I thought it was very energizing
[2110.44 → 2134.98] okay party people this one's for you, I've got just 30 seconds to tell you about Wix studio the
[2134.98 → 2143.44] web platform for freelancers agencies and enterprises so here are a few things you can do in 30 seconds or
[2143.44 → 2152.44] less on studio number one integrate extend and write custom scripts in a VS Code based IDE to leverage zero
[2152.44 → 2159.78] setup dev test and production environments three ship faster with an AI code assistant and four work
[2159.78 → 2166.40] with Wix headless APIs on any tech stack Wix studio is for devs who build websites sell apps go headless
[2166.40 → 2173.16] or manage clients well my time is up, but the list keeps going on step into Wix studio and see for yourself
[2173.16 → 2178.24] go to wix.com studio once again wix.com studio
[2178.24 → 2190.50] okay let's talk more node Chris you had thoughts on all right nodes test runner please open up this conversation
[2190.50 → 2199.20] so that's that's when this was announced I was like this is a bad idea because what's the idea of node
[2199.20 → 2208.40] putting a test runner in itself uh I having experience uh maintaining a test runner there's all these edge cases
[2208.40 → 2215.38] and terrible things, and it's its not it's not the easiest egg to crack right, and so I was kind of concerned
[2215.38 → 2221.86] about the maintenance burden but I don't know if that's ever going to be a problem or not
[2221.86 → 2229.68] um certainly the people who know what those edge cases are if it's going to be anybody it's going
[2229.68 → 2234.80] to be those who work on node core, and so I think they're well suited to handling some of those things
[2234.80 → 2244.76] but I picked it up recently and to write some tests instead of mocha and um i was happy with
[2244.76 → 2253.14] if it's um you know it's not so restrictive in that you with some test runners they don't give
[2253.14 → 2259.26] you test suites you only get tests and they don't give you they discourage hooks or whatever
[2259.26 → 2265.06] and you get all that stuff in nodes test runner and that was really all I needed and so um
[2265.06 → 2272.28] yeah it works great with uh i I haven't tried the new typescript stripping thing
[2272.28 → 2280.84] with it but like if is you use something like TSX no problem you can combine it with a like c8 or
[2280.84 → 2285.04] something to get your coverage you know much like mocha it doesn't have a lot of bells and whistles
[2285.04 → 2294.92] however node I think 20 20 or 22 i think it arrived in 18 I may be wrong anyway one of it
[2294.92 → 2301.70] was either 20 or 22 added some mocks and spies and stuff there's like a mocking API now and that works
[2301.70 → 2306.90] pretty well and that was one of the things that was kind of missing and so wait yeah I'm happy with
[2306.90 → 2312.86] that that's just like in node native wow yeah yeah there's like a whole mocking API now does it work
[2312.86 → 2320.40] with ESM in like being able to mock like other modules like that was one thing that that node that
[2320.40 → 2325.90] I was wondering like you know it's been so long I'm trying to like to remember but there was do you know
[2325.90 → 2332.88] what I'm going to say no okay, but it's its actually pretty easy to do that nowadays um you can
[2332.88 → 2342.38] register a loader on the fly and have it do those things okay so there it's its an it's a different
[2342.38 → 2350.34] separate system but yeah you can do that sort of thing I haven't needed to yet and I can report back
[2350.34 → 2356.46] uh if I ever do which I'm sure I will eventually but yeah the mocking stuff works great
[2356.46 → 2363.08] assert is still assert which is not super, but you know there are other assertion libraries out there
[2363.08 → 2370.04] too and yeah I'm pleased with it, I'm happy it's there um you know the more adoption it gets the more
[2370.04 → 2376.04] terrible things that people are going to try to do with it and so who knows if that's going
[2376.04 → 2382.10] to become an issue later but for now I'm really happy with it works great and kudos to Colin and
[2382.10 → 2389.72] the rest who have been working on I think uh Rafael or something too but um yeah happy with that
[2389.72 → 2397.14] nodes test runner cool related discussion that we got cable's opinion on recently and I love your
[2397.14 → 2403.94] opinion Chris kind of going up a level what belongs in node and what doesn't like what is your particular
[2403.94 → 2412.28] opinion on shoving a bunch of stuff into node versus keeping that relatively slim and allowing
[2412.28 → 2417.42] third-party developers to innovate etc like do you have a strong opinion one or the other on
[2417.42 → 2424.30] where things belong inside of something like node I know what goes too far like the python standard
[2424.30 → 2431.44] library had something like an iTunes module built into it and that goes too far right yeah but I'm not
[2431.44 → 2438.20] I'm not like a small core advocate necessarily I'm I'm an advocate for whatever you know people
[2438.20 → 2444.00] commonly do that it would be it would make sense to do out of the box and um you know over the past
[2444.00 → 2452.44] couple years I think the that sentiment is kind of become more popular, and we've seen additions of
[2452.44 → 2460.10] things that you know the team five years ago wouldn't have considered adding right, and so I'm I'm happy with
[2460.10 → 2465.40] the direction and yeah I think it's uh I think it's good I think there's you know there's lobbing
[2465.40 → 2472.12] in the core now so yeah you know, so the stuff like that gotta have lobbing I say that seriously
[2472.12 → 2477.54] yeah I'm generally the same as I haven't been I probably been tracking nodes progress more in the
[2477.54 → 2484.26] last two years than ever in my life and generally like almost all the decisions I see them making I'm like
[2484.26 → 2489.64] yeah good decision like I feel like they're making sound choices and I feel like it's really
[2489.64 → 2498.30] like steady progress over the last 18–24 months so I tend to agree with you yeah, and you know and
[2498.30 → 2505.68] maybe some of that has to do with competition from Dino and bun but regardless uh you know
[2505.68 → 2511.86] they're doing a good job yeah by the way Dino too right around the corner and Ryan doll right around
[2511.86 → 2517.52] the corner on JS party as well we'll be getting them back on around the launch of Dino 2 which i
[2517.52 → 2524.48] think is September late September anyway let's close up unless nick did you have anything to say
[2524.48 → 2529.06] about node test runner or anything that Chris just said, so this was written from scratch I'm just
[2529.06 → 2534.84] curious like you know you have experience with uh mocha obviously like would there ever been
[2534.84 → 2540.54] precedent to just like to slurp up something like mocha and make it a first class thing no it was I mean it
[2540.54 → 2549.06] was from scratch and i I think uh nothing uh really fulfilled the requirements I think that
[2549.06 → 2557.78] they wanted um it was either like too much or not enough or it was mocha was too much, or it was
[2557.78 → 2566.74] Jacky uh so you know too Jacky yeah so you know it makes sense to it would not make sense to pull a
[2566.74 → 2573.46] mocha into core now because yeah you don't want to do that, but there are you know it wouldn't
[2573.46 → 2578.92] necessarily make sense to pull I don't know most of the test runners nowadays are going to have
[2578.92 → 2585.00] all those bells and whistles and out of the box and no test trigger doesn't have those things and
[2585.00 → 2592.68] similarly to mocha um but uh yeah so yeah they did write it i I don't think I don't think anything
[2592.68 → 2598.94] out there was suitable to pull in just speaking from speculation my opinion yeah sure that's awesome
[2598.94 → 2603.92] like you said things like this you know what especially when I want to do like something quick
[2603.92 → 2609.80] and one-off having to like I don't know there's just like a mental barrier to having to add something
[2609.80 → 2614.92] else and then configure that and then go whereas like if it's just built in it's like oh there's no
[2614.92 → 2621.40] barrier I can just write my tests in this case or glob I can glob without having to jump through a bunch
[2621.40 → 2628.84] of hoops for that that's really no config file no config file that's nice very, very nice well let's
[2628.84 → 2636.86] finish up this episode on a musical note one thing I've always loved is the cross-section of software
[2636.86 → 2645.60] development and culture whether it's music movies video games art we featured all kinds of things over
[2645.60 → 2654.84] the years on our shows maybe you recall nested loops a JavaScript band from back in the day that
[2654.84 → 2661.36] would rap over JS generated beats, and we had them on the show and featured some of their music of course
[2661.36 → 2669.48] I've done features of standard out the rapper who's a software development rapper uh probably the only one
[2669.48 → 2677.76] on earth who has some actually perfect music and most recently I found out about the tc39 song
[2677.76 → 2684.76] this comes by way of Bruce Lawson who works at the Vivaldi browser which Chris you're rocking Vivaldi
[2684.76 → 2691.22] today huh yeah are you a fan of this browser yes good browser what do you like about it is has
[2691.22 → 2698.92] some fancy things and if it's not like it doesn't slurp data like chrome and yeah yeah I like it
[2698.92 → 2704.82] very cool so you have bone skulls endorsement of Vivaldi Bruce works there, and he recently travelled to
[2704.82 → 2712.80] Amsterdam earlier this summer to help MCs nation conference out there and uh he says on his blog
[2712.80 → 2720.40] naturally the open ceremony required a JS pop group which is a sub-genre of K-pop which is a sub-genre
[2720.40 → 2727.04] of pop and uh they did an apparently a carefully choreographed dance routine, and they lip-synced
[2727.04 → 2732.14] the song, and he's got some pictures on his blog post which we'll link up as well, but they have an
[2732.14 → 2740.72] original song uh that he wrote can we hear the song yes is that too much setup for you yes gosh
[2740.72 → 2745.84] you're curmudgeon all right here's the song by Bruce Lawson tc39 song Chris
[2745.84 → 2760.92] I get so excited writing JavaScript I'm pretty easy going but now I use strict
[2760.92 → 2768.60] when I first began I was in callback hell then I met you, and now it all goes well
[2768.60 → 2777.74] I love you when my tests pass meet me in the moonlight and extend my class you always keep
[2777.74 → 2784.76] your promises from the start now you've shot your bat arrow straight to my heart
[2784.76 → 2794.98] oh tc39 I'm so glad you're mine say you will be with me till the end of time oh tc39
[2794.98 → 2800.78] you're so sublime your specs are the best my tc39
[2800.78 → 2809.42] all right so shout out to Bruce there you have it check out Vivaldi check out brucelawson.co.uk
[2809.42 → 2816.90] we'll link it up and uh let him know if you like the tc39 song all right that is our show for today
[2816.90 → 2820.22] any final words Chris no nick
[2820.22 → 2828.80] I feel like this is becoming a new routine you do I'm not sure if we need to form yeah put you on
[2828.80 → 2834.06] the spot, and then you crumble that's kind of our thing recently it's very easy yeah it's easy for
[2834.06 → 2840.64] you it's easy for me as well all right thanks for hanging out on behalf of nick nisi and Christopher
[2840.64 → 2847.34] bone skull Hitler and js party I'm jarred, and we will talk to you all next week
[2847.34 → 2871.06] thanks for listening to js party we love that you choose to spend time with us each week if you want
[2871.06 → 2877.10] some free stickers now's your time to act during the month of September I'm trading change logs sticker
[2877.10 → 2884.64] packs for thoughtful five-star reviews or blog posts about the pod write something nice screenshot it
[2884.64 → 2892.16] or it didn't happen and send it to jarred at changelog.com that's j-e-r-o-d at changelog.com
[2892.16 → 2898.56] with your mailing address what are you waiting for an engraved invitation next up on the pod cable and
[2898.56 → 2904.90] myself sit down with Chris shank to explore how tools can help us learn to create and think better
[2904.90 → 2912.34] stay tuned for that, but first another thank you to our sponsors Wix and fly.io to our beat freak
[2912.34 → 2918.58] in residence break master cylinder and to sentry use code changelog for 100 bucks off the team plan
[2918.58 → 2924.66] on sing up that is all for now but come back and party with us again next week
[2924.66 → 2934.66] game on
[2934.66 → 2934.70] game on
