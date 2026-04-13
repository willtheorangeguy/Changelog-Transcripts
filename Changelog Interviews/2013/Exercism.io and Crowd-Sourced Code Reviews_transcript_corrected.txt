[0.00 → 13.32] welcome back everyone this is the changelog where our members support a blog podcast
[13.32 → 18.14] and weekly email covering what's fresh and what's new in open source check out the blog
[18.14 → 24.28] at the changelog.com our past shows at 5x5.tv slash changelog and subscribe to the changelog
[24.28 → 29.04] weekly it's our weekly email covering everything that hits our open source radar you can subscribe
[29.04 → 35.46] at the changelog.com slash weekly this show is hosted by myself Adam Slovak as well as our
[35.46 → 42.36] managing editor today uh jarred Santa jarred say hello hey how you doing it's its good to have
[42.36 → 46.66] you on the show again it's been what a couple shows so I'm glad to be here as always
[46.66 → 54.22] excited about our guest today yeah me too and uh, uh this is episode 108 and today's show is
[54.22 → 60.36] sponsored by digital ocean uh digital ocean is a simple cloud hosting provider they're dedicated
[60.36 → 66.96] to offering the most intuitive and easy ways to spin up a cloud server users can create a cloud
[66.96 → 72.64] server in literally 55 seconds that's a marketing thing, but it's also the truth literally 55 seconds
[72.64 → 78.60] and uh pricing plans start at only five bucks per month you get half a gig of ram 20 gigs of SSD
[78.60 → 84.44] drive space one CPU and one terabyte of transfer with the recent public launch if you go back a
[84.44 → 90.72] couple shows and listen to episode 105 uh johns o'Nolan was on here talking about ghost and his blogging
[90.72 → 97.72] platform so they just uh did a public launch of ghost and digital ocean is happy to tell you all that
[97.72 → 102.66] they have an official one click ghost image you can literally go and click and boom you got ghost
[102.66 → 108.90] on a SSD drive uh in the cloud so they uh that was created by the makers of ghosts so thanks to
[108.90 → 114.92] Hannah for that you can get a new ghost blog up and running in literally 55 seconds try it out
[114.92 → 121.22] uh use our promo code the changelog October to save 10 bucks go to the uh go to their website
[121.22 → 129.18] digitalocean.com and get started today so uh excited to have our guest on today Katrina Owen she's an
[129.18 → 135.12] instructor at jumpstart lab and maker of exorcism got that pronunciation right which we hope to learn
[135.12 → 139.84] quite a bit about on this show today so Katrina without further ado welcome to the show thank you
[139.84 → 146.76] so where do we begin with you, I mean I feel like we kind of know you from a few blog posts and
[146.76 → 152.30] a few talks and the work you do in the community, but you know tell us a bit about yourself
[152.30 → 157.98] what's the backstory on you so i I'm an accidental developer I actually started out
[157.98 → 165.98] in biology a few years ago wow and got a degree in genetics and absolutely hated the idea of working
[165.98 → 175.50] in a lab so before I even got ever got a job with my genetics degree I started uh helping people out
[175.50 → 182.10] with their websites and kind of messing around with a little bit of a little bit of PHP mostly at first
[182.10 → 186.84] uh and then finally I just knocked on someone's door and said hey would you give me a job, and they did
[186.84 → 194.40] so you studied genetics which I'm sure is a deep subject right I mean that's DNA right
[194.40 → 199.04] but other things I'm sure I'm I'm trust I'm not first and I'll have a degree in that but
[199.04 → 205.36] so you're accidental is this recent how long you've been programming about six years okay
[205.36 → 216.20] um yeah I graduated from university in I guess 2006 and then or 2006 2007 somewhere around there
[216.20 → 225.86] and I think I got my first job as a programmer in 2000 late 2007 wow and from what I understand um
[225.86 → 230.86] you just came here to the U.S. to you live in Denver so we kind of mentioned the intro that
[230.86 → 235.34] you're an instructor which I mean that's pretty freaking neat that you're an instructor six years
[235.34 → 241.66] later after learning the program but jumpstart is uh is not you know just anybody they're really
[241.66 → 248.20] well respected so I mean that's cool jumpstart is awesome jumpstart lab does amaze ruby training
[248.20 → 255.44] rails training that sort of thing some JavaScript uh they're starting to work on some iOS stuff and
[255.44 → 262.42] ops code stuff uh, so there are a lot of fascinating things going on with them so you got out of
[262.42 → 269.38] uh genetics because you didn't want to work at a lab and here I am jumpstart lab good irony
[269.38 → 277.94] nice I was thinking I mean because I guess so what was it about the lab or a lab that kind of turned
[277.94 → 286.06] you off and what ultimately is uh I guess transpires back to that from what you do as a developer so the
[286.06 → 291.20] lab work during college is probably not very similar to the lab work that you would do in an actual lab
[291.20 → 298.40] um, but it's very repetitive lots of waiting lots of just kind of turning a machine on and waiting for
[298.40 → 305.64] four hours for something to replicate and then um looking at it in some way sounds like video rendering
[305.64 → 311.60] or something doesn't it jarred yeah sounds like a bad test suite yeah yeah right and so i
[311.60 → 319.04] just couldn't bear the thought of doing that um I wanted to be a lot more hands-on a lot more like
[319.04 → 324.40] problem-solving on a daily basis rather than spending several years with a hypothesis and trying
[324.40 → 332.48] to make observations that might prove it right or wrong and then what's the ultimate product of
[332.48 → 337.30] doing all that like is it just a yes or no I was right or wrong is there anything like real will change
[337.30 → 343.00] oh yeah you cure cancer and you oh that's that's no big deal right clone people and stuff you know
[343.00 → 348.10] it's its pretty awesome in theory so let's go back to you knocked on someone's door and said give
[348.10 → 356.74] me a job, and they did yeah can you elaborate on that sounds pretty amazing yeah so my uh my resume
[356.74 → 365.78] basically was a bunch of like I helped people do this and I built that, and it's basically you know not
[365.78 → 371.76] very impressive, but then it said and I have a degree in genetics and the CTO looked at it and said you must be
[371.76 → 379.76] pretty smart so I got the job uh and at first all I really was going to do was help them test stuff and
[379.76 → 385.58] write little scripts and debug and whatever but within a very short time I was writing production
[385.58 → 394.22] code so I think it took about three months before I was really productive um absolutely dangerous like
[394.22 → 399.98] uh I wouldn't want to have me as the only developer but on a team of smart people
[399.98 → 406.90] um they absolutely kept me busy and I was um producing content and being useful
[406.90 → 412.92] you had some pretty good guidance then I did yeah yeah and so that's that's a good place to
[412.92 → 416.90] start from and then now you're in the same position now with which we'll talk
[416.90 → 422.04] here in a bit more in detail but exorcism it's really about that uh that crux there which is
[422.04 → 428.32] you know learning um you know writing code practicing and then ultimately the other side of that which is
[428.32 → 432.94] code reviews and stuff like that so I mean it's about doing exercises and keeping it kind of bite
[432.94 → 438.78] size and simple but at the same time dealing with the problem yeah so one of the things I've i
[438.78 → 443.44] I was very frustrated when I was learning how to program because everything seemed
[443.44 → 454.54] so arbitrary like the or confusing or like everything would explain it as though I knew all the things
[454.54 → 460.50] some you know the blog posts would be making assumptions about what I knew or the read me's
[460.50 → 466.96] would be making assumptions about what I knew and often I was just confused and frustrated um a lot of
[466.96 → 473.88] the things when you're picking up programming without any formal background there's at least six
[473.88 → 481.68] years ago there was very little guidance on doing um doing well like programming choosing good names
[481.68 → 487.94] or structuring your code in a good way or writing unit tests and proving that you were that your
[487.94 → 494.94] code was behaving the way you expected it to behave it was all very like copy stuff from JavaScript
[494.94 → 502.72] websites or PHP websites and kind of mess with it until it works and that I found that to be very
[502.72 → 508.36] frustrating and I got kind of obsessed with the whole XP thing I read everything I could find about XP
[508.36 → 513.10] and pair programming and TDD and all of those things and tried to figure out how to make that work
[513.10 → 521.48] um in my environment at work so go ahead jarred good I was going to say so the company that
[521.48 → 526.36] you worked at was not doing XP at the time, and you brought that to the equation, or they were already
[526.36 → 531.68] engaged in it, and you just want to learn more no nobody at the company I was working at did any sort
[531.68 → 538.52] of testing or pairing or any of that um we didn't have a continuous integration server we didn't
[538.52 → 543.22] actually have a test environment when I started working there it was straight to production so I'm
[543.22 → 548.32] trying to just get an idea of your career arc was it from this job to jumpstart lab or has there been
[548.32 → 554.48] things in between there's been one thing in between so at this job the PHP job it was a startup
[554.48 → 562.20] um it was very exciting I stayed there for about two and a half years almost three years and I taught
[562.20 → 568.20] i kind of taught myself how to write tests at that job so I would write tests for everything I did I
[568.20 → 573.20] put together a CI server that I just ran locally and nobody else in the company really cared to run
[573.20 → 579.46] those tests which was I guess fine I mean I just used it to um to help in my own development
[579.46 → 586.64] but after a while I got frustrated with that and decided to move to uh to a different language and
[586.64 → 592.50] in at least find a company where they cared about testing more than they did at the previous
[592.50 → 598.46] company and this was at this at the time when I was also moving back to Norway where i so I studied
[598.46 → 604.12] genetics in Norway moved to la worked at this startup and then moved back to Norway after three years
[604.12 → 611.60] and in Norway I went to a ruby meetup uh and I guess there were probably 15 people there the next
[611.60 → 616.44] day a couple companies called me up and said hey you should come talk to us and so on of those
[616.44 → 623.50] companies hired me on as a developer um and i more or less learned ruby on the job there
[623.50 → 626.48] stayed there for a couple of years two and a half years about
[626.48 → 635.30] and let's see from there I did the talk therapeutic refactoring which uh let me travel around and talk
[635.30 → 642.94] to people and meet people at a bunch of conferences and um I also was kind of done at the company I love
[642.94 → 648.52] the company I worked at in Norway they are absolutely amazing they always come up with great ideas
[648.52 → 655.46] they're always inventing things like new right the latest their latest project is uh taking government
[655.46 → 664.70] map data and using it to show on the web 3d maps of Norway, and then you can select a square of Norway
[664.70 → 673.50] and um click, and you get sent a 3d printed model of the landscape that you selected which is awesome
[673.50 → 679.60] yeah, and so they're always making up things like that um but I felt like I had kind of done what i
[679.60 → 685.40] what I had to do there I had really brought testing in um to the organization that was kind of what i
[685.40 → 693.02] was hired to do and I was ready to move on and I met Jeff from jumpstart lab at a conference and we
[693.02 → 699.78] talked and eventually well he emailed me saying that I should work for him um and that's
[699.78 → 706.32] always nice it's always really nice you should work for me well I have a job now that I really like
[706.32 → 716.28] so uh I spent some time thinking that over and ended up in Denver so is nor I may, I miss it is
[716.28 → 721.80] Norway home or do you just go there for school uh I've been back and forth all my life my mother is
[721.80 → 729.52] nor uh Norwegian okay yeah I understand that uh earlier this year was you're now in Denver which
[729.52 → 734.50] we mentioned a bit ago but so now you're in Denver this is like I guess January time frame or first
[734.50 → 740.52] part of the year time frame you came and officially began to jumpstart and moved I guess you probably
[740.52 → 746.10] don't shorten at the jump jumpstart but so jumpstart lab but um, and now you're in Denver which is an i
[746.10 → 750.94] was just up in Denver in the summer and I love Denver I think it's beautiful and the mountains and
[750.94 → 756.80] just like having that as the backdrop is just amazing for you know just the scene you know yeah
[756.80 → 764.62] yeah it is an amazing place the weather here is absolutely amazing sun sunshine except every once
[764.62 → 771.76] in a while but only for a very short time it will rain or snow so when I was talking to jarred before
[771.76 → 776.64] you, and you keyed off this a little bit you mentioned your talk therapeutic refactoring and
[776.64 → 782.20] kind of the ramifications I guess from that which is I guess more like the result so you kind of
[782.20 → 787.88] gave this talk that was um at uh Cascadia was that the first time you gave it was this the least the
[787.88 → 795.22] most recent time you gave it I gave it at uh Nordic ruby in Stockholm okay, and they don't record
[795.22 → 801.46] bummer yeah right and there were several people at that conference who organized their own conferences
[801.46 → 808.82] and among them Ben blitzing of Cascadia ruby was in the room and he um said that I should fly to
[808.82 → 815.68] wherever that was Seattle and give it there, and it was recorded by confreaks so it ended up both on
[815.68 → 820.92] the confreaks.net or dot com website and YouTube from there I know that jarred kind of put it off a
[820.92 → 825.38] little bit because I guess somebody has suggested him to watch, and he's like I guess I'll watch it
[825.38 → 829.20] whenever, but he watched he was really thrilled about it so I guess talk a little bit about what
[829.20 → 836.66] therapeutic refactoring is when I was working at this ruby job in Norway I felt very stressed out about
[836.66 → 842.20] uh always having to there was always this pressure to ship and there always is because
[842.20 → 848.98] because it's that's what we do that's that's the whole point right and um and i I felt like I was
[848.98 → 855.76] always in so much of a hurry that I didn't really learn very much I'd often be throwing code that i
[855.76 → 862.42] wasn't happy with um into the repository and I felt like I never had time to go back to it
[862.42 → 870.62] and uh after one day I just realized that I wanted to spend time just a little bit of time
[870.62 → 876.50] making sure that something was beautiful I didn't care what, and so I'd come in really early in the
[876.50 → 883.24] morning before anyone else got to work and spend about an hour just writing tests and refactoring
[883.24 → 890.10] some tiny piece of code in the project and I did this on a daily basis for quite a long time probably
[890.10 → 898.08] about a year, and it transformed how I thought about programming in many ways so it's the first
[898.08 → 906.70] thing was that because I was writing tests and refactoring for my own pure pleasure it is bothered me
[906.70 → 912.88] to wait for the test suite to run so waiting for any number of seconds as if anything over a second
[912.88 → 919.78] was very, very frustrating and not pleasurable and I was there just to refactor for the pure pleasure of it
[919.78 → 925.58] so I started looking into how to design my code in such a way that the test suite would be very
[925.58 → 933.06] fast and very responsive and that led me into sort of this refactoring loop that that had this
[933.06 → 943.40] immediate feedback and um and never uh never really took me out of flow so i I ended up in this flow state
[943.40 → 951.38] for a long time, and it was very, very pleasurable it felt very therapeutic I felt um smarter in a way
[951.38 → 957.06] so normally during the day whenever when all the pressure was on i basically just felt like an idiot
[957.06 → 963.50] like I'm not smart enough to do this yeah right and I think we most of us feel like that like I'm i
[963.50 → 970.82] definitely know there are people who don't but um but a lot of us do it's really hard and during the
[970.82 → 976.20] those refactoring sessions I felt like I understood things and I was on top of things and i kind of
[976.20 → 982.40] lost my sense of self, and it was it just felt really nice so I wanted to talk about that and i
[982.40 → 987.88] had a bunch of like code examples that I wanted to share uh with people just because it's always so
[987.88 → 991.96] much fun to go show oh this is what it looked like before, and it was horrible, and now it looks awesome
[991.96 → 1000.50] how many times you've given that talk since uh it's eight maybe wow I'm giving it that's when you know
[1000.50 → 1006.78] you got a good talk is you know first you do if it's not recorded and uh you know that's kind of
[1006.78 → 1011.48] how legends are made did you hear this one oh it wasn't recorded you can't see it you know you
[1011.48 → 1015.82] should have been there, and then you record it you know on confreaks and there it's out there in the
[1015.82 → 1021.40] public for everyone to see and watch and enjoy and spread and then yet people at other conferences
[1021.40 → 1026.48] still ask you to come and give that same one which we can just go to confreaks.com or whatever
[1026.48 → 1032.64] website and watch it and yet people still want to uh see it live and see it again or for the
[1032.64 → 1037.90] first time so that's that's pretty astounding I'm actually going to be giving it again in San
[1037.90 → 1046.60] Francisco on November 1st at flocon yeah so what is it about refactoring that that just
[1046.60 → 1051.90] you know gets nerds excited like nerds like us excited like what is it
[1051.90 → 1057.16] that feeling that therapeutic feeling you said that you had what do you think it is
[1057.16 → 1062.28] that that generates that I have no idea it's such a good question
[1062.28 → 1068.84] because i I mean we all react that way like as you're even talking I'm thinking about refactoring
[1068.84 → 1073.60] I'm like yes there it's kind of like a cleansing feeling like you're taking you know you you you have
[1073.60 → 1079.50] this dirty code that you wrote, and it works, and you know it's its okay the tests pass the code is
[1079.50 → 1086.00] functional right the maybe the product owner is even happy, but it's not like up to I don't know
[1086.00 → 1090.60] what beauty, or it's not up to your standards perhaps and then when you get a chance to do that
[1090.60 → 1097.18] you know it's almost like you're you're taking a shower or something but I'm not sure like what's
[1097.18 → 1102.76] at the core of that feeling she said uh one thing you did say Katrina was flow and i I don't
[1102.76 → 1107.74] know if you're a fan I know that you've done some stuff with uh I think it was java ranch you mentioned
[1107.74 → 1112.16] before so you must be a fan of Kathy sierra, and she talks a lot about flow and the state of flow and
[1112.16 → 1118.74] you know being in that I mean you even said things like I felt smarter you know that's that study of
[1118.74 → 1122.48] the brain if you go and study that stuff you definitely are smart in that moment of
[1122.48 → 1128.12] time because you're at a state of bliss mentally that you know you're just like the super being of
[1128.12 → 1133.92] Katrina you know that's who you are for those that hour that 40 minutes of flow yeah yeah I think
[1133.92 → 1140.96] that's a huge part of it I think another part of it is like I think as a group we tend to enjoy
[1140.96 → 1143.78] obsessing over details yeah
[1143.78 → 1153.80] I mean isn't some of that where uh the bike shedding and yak shaving all come about so
[1153.80 → 1159.04] frequently yeah it's you know the more minuscule the details the more we like to think about and
[1159.04 → 1169.06] and argue about um yeah maybe I think that makes sense i know for me um sometimes when I'm
[1169.06 → 1173.98] isolated and I can kind of lament a little bit with you on that state of bliss for the bit there even
[1173.98 → 1179.90] if it's even if it may not be super useful when I'm done like whatever I've just shipped it might be
[1179.90 → 1186.58] optimizing one line to be easier to read and I can imagine how this is going to change three other
[1186.58 → 1193.08] things I'm working on to make those smaller more readable more bite size more translatable whatever
[1193.08 → 1198.30] the reasons are for it, i I think that that might also be part of the refactoring is like this
[1198.30 → 1203.80] this constant kind of making things better even if it's just for yourself yeah
[1203.80 → 1212.10] so moving from the refactoring over to your project exorcism it seems like that it really is all
[1212.10 → 1218.42] about um I mean it's about code review it's really about refactoring isn't it oh absolutely it totally
[1218.42 → 1225.06] grew out of this love of obsessing over the details and that's why I call it nitpicking on the site like
[1225.06 → 1230.64] all the comments are nitpicks I mean it's its not it's not really bike shedding even though sometimes
[1230.64 → 1239.36] it feels like it yeah because it is can be a profound discussion about what we value in code and why we value
[1239.36 → 1243.18] these things and the discussion becomes fascinating because different people value
[1243.18 → 1248.92] different things or different things in different contexts and so there's a real breadth in those
[1248.92 → 1256.22] discussions there so just backing up can can you uh for the listeners describe exorcism you know what
[1256.22 → 1264.42] its goals are and basically how it works sure, so exorcism is a site where we made up a bunch of
[1264.42 → 1272.26] exercises in the form of a test suite so a test suite for every exercise and the goal the first
[1272.26 → 1277.46] goal is to you download the exercise you get this test suite and the first goal is to make it pass
[1277.46 → 1282.36] write production code that will make the test suite pass, and then you submit that code to the website
[1282.36 → 1290.38] and you get feedback on uh the code that you wrote so names the choices that you've made uh for how you've
[1290.38 → 1298.74] named things the methods the classes if there are many um variable names how which um
[1298.74 → 1304.88] which methods from the core library you've you've chosen or the data structures that you've chosen or
[1304.88 → 1311.26] how you've chosen to arrange the code and I've explicitly said on the site that I'm focusing on
[1311.26 → 1318.36] simplicity and readability and expressive code, but again those are objective those are not
[1318.36 → 1324.62] objective terms they're very subjective and so the discussion it often surrounds around or becomes
[1324.62 → 1335.94] something of well I find this readable um but more interestingly there for example um about
[1335.94 → 1341.42] naming block variables when you're looping for example this idea that well the collection should
[1341.42 → 1346.26] probably be named in the plural and the block verb variable should be the singular of that plural
[1346.26 → 1353.04] rather than saying I have a monkey list and each thing is a monkey it would be monkeys looping
[1353.04 → 1359.46] through a list of monkeys and then each block variable would be the monkey but even beyond that we have
[1359.46 → 1367.22] some fascinating discussions about um the level of abstraction of the name that you might choose so
[1367.22 → 1375.16] if you're um if you have a block variable in an aggregate function some people will call the block
[1375.16 → 1382.48] variable hash like naming it for the underlying data structure other people will call it result or memo or
[1382.48 → 1390.96] accumulator sort of labelling it based on its role in the calculation and then other people will name it
[1390.96 → 1398.76] frequencies or histogram naming it for the meaning the the the thing that it represents in terms of the
[1398.76 → 1406.46] problem not in terms of the calculation or the computation and so these patterns emerge and these discussions
[1406.46 → 1413.20] kind of um by asking why did you name it this way what are the trade-offs that you're considering
[1413.20 → 1422.60] you get a lot of very interesting um perspectives on what expressive code means or what readable actually means
[1422.60 → 1429.58] so all the feedback on the code review is by other users of exorcism right there's not like some
[1429.58 → 1436.34] it's not you there like giving everybody feedback no you don't have like two geniuses giving feedback it's
[1436.34 → 1442.74] uh everybody writes code and then once you have um completed an exercise, and you actually decide on your own
[1442.74 → 1448.22] when you feel like you've completed it you've had enough feedback, and you're done you move on at that point
[1448.22 → 1454.54] you uh gain access to everyone else who has done who is currently doing that same exercise that you
[1454.54 → 1460.60] just completed so you see you're going to see all their code yep and then also the nitpicks on their
[1460.60 → 1468.30] code yes yeah, so the discussion becomes this global thing uh on a per submission basis yep so if i
[1468.30 → 1474.56] understand you're right so you well we jumped a couple steps you got to get the CLI in place and all that
[1474.56 → 1480.40] stuff oh right oh goodness yeah there's its actually really confusing make no mistake it's
[1480.40 → 1488.18] it's right now the UX is absolutely terrible uh I've hired a designer or I'm talking to a design UX
[1488.18 → 1494.06] um company to help me sort that out so yeah the first thing you have to do is you have to install
[1494.06 → 1503.60] a command line uh client which is written in go and so this um communicates with an API on the
[1503.60 → 1511.54] in the web app um and that is to fetch down exercises or submit up exercises uh and then
[1511.54 → 1518.04] once you've submitted it you actually all the feedback happens on the site itself uh and that's
[1518.04 → 1523.82] about it actually it's not very complicated once everything is in place I think it's that first
[1523.82 → 1530.02] kind of uh original kind of ceremony of like getting and now I was you know messing with it last night
[1530.02 → 1534.22] uh, and we'd, we'd actually so for those of you listening that are subscribed to the newsletter
[1534.22 → 1541.04] too we've we've plugged the exorcism in the I think issue eight but uh and I've been meaning to
[1541.04 → 1546.18] get back to it since then because Beverly nelson who does a lot of work with ruby friends and just
[1546.18 → 1551.78] really is thriving in the area of kind of helping people get plugged into the right kind of resources
[1551.78 → 1557.40] to learn I'm always kind of on the lookout for neat tools to kind of suggest to her to check out so
[1557.40 → 1562.84] I was just like waiting for a chance to play with it but um i you know I'd kind of gotten involved
[1562.84 → 1568.94] and even me as I mean I wouldn't say I'm seasoned I'm certainly not brand new, but you know
[1568.94 → 1574.04] even I had a couple stomach blocks so I would uh I'd like to see how that pans out for the
[1574.04 → 1580.00] future, but it was easy to get in place but so once you get your exercise let's say you wrap it up and
[1580.00 → 1586.84] you got no failing tests, and you feel good about it and then you do um exorcism I think is uh
[1586.84 → 1593.38] exorcism what's the ship version of that submit okay so once you submit it, and you get some
[1593.38 → 1597.72] feedback and then once you finally get to a point where you want to complete that is that when you get
[1597.72 → 1603.32] access to nitpicking yes so only you can only nitpick the ones you've done though right
[1603.32 → 1609.28] that's correct okay that's what I want to clarify yeah so i actually this I mean this might change i
[1609.28 → 1616.20] currently I like that I'd like to provide more guidance on what good nitpicking might look
[1616.20 → 1625.68] like um which key areas if it is more useful to focus on or what type of feedback is more
[1625.68 → 1632.32] helpful like I've seen feedback that says great job and I'm like great job how like what do you like
[1632.32 → 1638.08] about it there once when someone said great job I was like well here let me show you how it's done
[1638.08 → 1645.14] and I was like I really like these names because this that and the other I love how the separation
[1645.14 → 1651.92] um you know how the tasks are separated into separate methods that really make sense so i I managed
[1651.92 → 1657.38] to get like a list of eight things that I liked about that code because if you know what someone
[1657.38 → 1663.70] likes about it, you can go and do it again but if you just say great job it's like well I don't know
[1663.70 → 1669.86] what was great about it was all of it great so is this uh is the since you're talking about you know
[1669.86 → 1675.40] how to nitpick is the how to nitpick documentation is that a living document then it's a living document
[1675.40 → 1683.86] uh and right now it's nowhere near done um there I keep seeing new things that I want to address
[1683.86 → 1689.12] and right now the documentation doesn't seem to be the best place to do that so I'm going to work with
[1689.12 → 1697.42] the UX um people to figure out how to present that information in a way that's useful and
[1697.42 → 1702.48] timely like getting that information when you actually are trying to nitpick rather than when
[1702.48 → 1709.70] you decide to go read some documentation so you're a ruby developer you have a command line client
[1709.70 → 1716.56] written in go yes um I think we can talk about that a little bit but first which languages have
[1716.56 → 1722.36] exercises so is it just ruby or can are there other languages supported so it started off as just
[1722.36 → 1728.84] ruby because I was writing it mainly just to give it to my students here in Denver and then one of
[1728.84 → 1734.44] my colleagues started pointing uh porting the exercises to JavaScript and then once I had launched
[1734.44 → 1741.94] it uh someone probably in the second week was like we need elixir and closure so they ported it to
[1741.94 → 1746.52] elixir and closure nice and then someone else said well why don't we have python, and it was like
[1746.52 → 1752.44] because I don't know how to write python, but you're totally welcome to, and so I think now we have uh
[1752.44 → 1761.14] closure elixir ruby JavaScript python and Haskell and somebody is porting it to rust and I'm working on
[1761.14 → 1768.68] the go exercises and somebody is working on uh coffee script a couple of days ago someone said they'd
[1768.68 → 1775.60] start working on the Scala and then I heard someone say uh Objective-C but that's going to take
[1775.60 → 1780.26] a little bit more there's a little bit more ceremony involved in getting that running
[1780.26 → 1786.08] so you're going to start writing the go version and your command lines and go is this a
[1786.08 → 1791.98] a newfound love for you a new language absolutely yeah I really like it um I'm also going to write
[1791.98 → 1799.56] part of the part of the API is going to get um ported over to go instead of ruby um I was at a
[1799.56 → 1807.74] conference uh half a year ago maybe actually almost a year ago is the first time I saw a talk on go and
[1807.74 → 1814.80] it was at native in Sweden um and the talk was by Andrew Durand one of the developers who works at
[1814.80 → 1822.16] google working on the language go and um I immediately liked it but didn't do anything
[1822.16 → 1828.00] about it like i am month later I was busy trying to move to Denver and then I had a new job and all of
[1828.00 → 1835.62] that so i never really got into it and then I was at a conference in Poland um and Andrew gave another
[1835.62 → 1840.96] talk on go at that conference and I was like okay now I really have to do it so I sat down and I went
[1840.96 → 1847.08] through their tour and I started playing around with things and I'm still not anywhere near uh
[1847.08 → 1853.74] competent but i can get a little bit of stuff done and I can um I know enough to pester people to
[1853.74 → 1862.78] help me out so i I'm more able to ask questions so eventually I'll probably I hope to be fluent by the
[1862.78 → 1868.64] time the first go conference here in the states happens so you don't have to go into great detail but
[1868.64 → 1872.86] just at a high level what is it about go that that turned you on what is it that got you
[1872.86 → 1882.76] it's its very it's a small language, and it's very consistent, and it feels very zen minimalistic
[1882.76 → 1890.06] and zen to me so the way ruby is more uh baroque and Shakespearean and expressive and that you can say
[1890.06 → 1896.92] things in a thousand different ways and they all smell just as nice um with go it's more like
[1896.92 → 1905.74] like a very tiny poem zen poem um very concise um and
[1905.74 → 1911.50] and there's kind of just one way to do it right there's just one way to do it and that's kind of a
[1911.50 → 1917.32] relief after you know when I do so much ruby it's really a relief to be on the other end of that
[1917.32 → 1925.30] scale um I'm I'm very excited about the concurrency model in go I'm also very excited about the fact
[1925.30 → 1931.20] that there's no inheritance that all its object-oriented, but it's all through composition so it has
[1931.20 → 1939.12] this incredible focus on the interface um and so the API of your object is very important
[1939.12 → 1946.14] and I really like that I can kind of relate on the there's only one way to do it being attractive
[1946.14 → 1951.90] I'm also a ruby developer and I've loved the freedom that ruby you know gives us to express
[1951.90 → 1959.38] ourselves um and then over time I see actually my tastes in ruby changing um to where something
[1959.38 → 1964.00] that I used to think was a good way of writing ruby now I look at that, and it's its unattractive
[1964.00 → 1969.88] or it's its silly or whatever reason and then I start like porting my ruby over to my new
[1969.88 → 1974.58] my new ruby style and I look at my old style like I can't believe I used to write like that
[1974.58 → 1981.30] and I'm not talking about uh like readability, and so I'm just talking about pure style yeah and uh that's
[1981.30 → 1985.04] after a while that kind of just wears on you, it's like I wish they would just tell me how to write
[1985.04 → 1990.88] it and like to let me think about the problem-solving yeah and uh I know there's use cases for both
[1990.88 → 1996.12] scenarios but that is an attractive thought although I haven't actually got into to try and go yet so
[1996.12 → 2003.22] yeah I really like both I really like both styles or both this really you know very varied and
[2003.22 → 2011.56] and expressive uh craziness that we're we're allowed in ruby and the the the concise expressive
[2011.56 → 2017.48] uh like minimalistic approach that we're that we're encouraged to use and go I've really i really
[2017.48 → 2025.38] like both and I think that they can both inform the other I think when robin and Andrew that you
[2025.38 → 2033.08] mentioned uh that turned you on to go I think it was either in somewhere out there on the ether
[2033.08 → 2039.16] that I've seen this or when they were actually on the show so uh episode 100 we had it was a fun
[2039.16 → 2044.20] episode too because it was episode 100 of the show which was great but um had them on the show and i
[2044.20 → 2048.42] believe it was robbed who said because he was you know one of the founding people to create the language
[2048.42 → 2054.52] was that he wanted it to fit in his head you know like in memory like to, and you sometimes know when
[2054.52 → 2059.58] you're I think jarred you and I've had some side conversations about you know the state of flow
[2059.58 → 2062.76] even like going back to some things you said earlier Katrina like where when you're working
[2062.76 → 2066.74] on something if you can, you've got a lot going on in your brain if you like a text message or a tweet
[2066.74 → 2071.50] or something that kind of breaks that state of flow you kind of lose that mental memory and I think
[2071.50 → 2076.98] that's kind of what uh rob was fighting against when creating the language was to kind of keep it
[2076.98 → 2081.10] like that as well to keep it where you can kind of keep what you're doing in your brain a little
[2081.10 → 2087.50] longer yeah this morning I was pairing with uh with someone, and they introduced me to an
[2087.50 → 2093.46] innumerable method that I had never seen before in ruby, and it's awesome it was exactly what I needed
[2093.46 → 2098.22] but I had totally never seen it even though I've read through I thought all the innumerable methods
[2098.22 → 2104.86] I just had totally missed it I've been doing this for what three years I mean come on you should have
[2104.86 → 2113.16] gotten it by now right that's funny but uh yeah I mean that is the fun I think that's kind of the
[2113.16 → 2117.62] adventurous part of ruby is that there are so many different ways that you could do things but I can
[2117.62 → 2121.70] lament what you're saying jerry where you're like just tell me how to do it the one way so I can
[2121.70 → 2127.04] think about the real problem versus the style that I have to execute this and I can do it 15 ways but
[2127.04 → 2131.76] which way is really the right way to do it and just give me those training wheels I'll go
[2131.76 → 2142.18] so um yeah I guess we talked about go a bit here but so originally the CLI was written in ruby
[2142.18 → 2147.78] right so was it something with ruby that made you change or was it simply to like want to play with go
[2147.78 → 2155.50] to do it in that no so okay so yes the original command line in a client was written in it was a
[2155.50 → 2162.50] ruby gem so it was gem install uh exorcism that worked really well when the only problems were
[2162.50 → 2170.58] in ruby, but now you have people only on exorcism for the closure, and it's really a pain to set up
[2170.58 → 2178.58] like all the ruby like setting up ruby on your machine is actually quite an ordeal especially
[2178.58 → 2184.70] if you don't know ruby um so with the go it's possible to cross compile for all the different
[2184.70 → 2192.76] um operating systems and architectures and people just have to download and install this one binary
[2192.76 → 2199.56] and that's it no dependencies and so on the home page that you have the try it version
[2199.56 → 2205.90] the quickie don't worry about telling us your GitHub uh just do it now I guess version will that
[2205.90 → 2210.36] eventually go away or is that still kind of like or is it dead, and you just haven't removed it yet
[2210.36 → 2216.32] oh the one that says ruby yeah it says it was it's on your home page and says try it and the
[2216.32 → 2222.22] instructions say gem install exorcism you go to attempt directory, and you know totally a mistake
[2222.22 → 2227.78] it should be you it should, I'm going to fix that after the show uh we didn't say that we'll edit that out
[2227.78 → 2236.12] pay no attention to the go client um allows you to do that now okay so I will totally fix that
[2236.12 → 2244.62] thank you hey that's we're here for peer reviews right absolutely so exorcism it seems like it has
[2244.62 → 2250.88] a really great foundation but uh and I've I'm I'm halfway through the bob exercise and having
[2250.88 → 2257.74] fun uh seems like this is a kind of project where you have bigger long-term goals what are
[2257.74 → 2262.52] some of your thoughts on the future of exorcism what you'd like to see more languages more exercises
[2262.52 → 2267.68] more community or is there you know are there changes coming down the road all of the above
[2267.68 → 2273.04] uh I'd like better exercises right now all the exercises that are there were just kinds of made up
[2273.04 → 2280.90] by me while travelling uh hoping to keep my students busy for half an hour and so some of those exercises
[2280.90 → 2287.22] are absolutely excellent and have fascinating problems that they expose and fascinating
[2287.22 → 2293.98] discussions come out of them others have terrible design terrible APIs really boring discussions and
[2293.98 → 2299.64] I'm kind of working on figuring out which exercises are good and which are less interesting so that I can
[2299.64 → 2306.32] par that down but I'd also like new exercises that um expose different types of problems perhaps in
[2306.32 → 2310.80] the different languages like not all the languages need the same exercises because they have very different
[2310.80 → 2317.56] um design constraints and uh different features that you should be able to explore in exercises
[2317.56 → 2325.54] um I'd like more languages I'd like all the languages really um it seems like there are three
[2325.54 → 2333.86] two or three different um I'd say three different reasons to use exercise that that people have told me
[2333.86 → 2338.60] about some people say I'm learning how to program and this is the first time that I'm actually getting
[2338.60 → 2343.80] feedback on the code that I write, and so I'm learning a lot faster so it becomes a type of
[2343.80 → 2349.06] mentorship and then other people are like well I'm fluent in java I just want to figure out how to write
[2349.06 → 2355.84] closure, and so they're using it to try out a new language kind of just for fun and figure out what the idioms
[2355.84 → 2361.82] are in that language as opposed to the language that they're fluent in and some people are doing exercises
[2361.82 → 2367.42] in the language that they use primarily and using it to have really deep discussions about style and
[2367.42 → 2372.22] trade-offs with other people who use that right language on a regular basis
[2372.22 → 2378.72] and I'm logging into the to my home page now on exorcism, and it looks like I got a zero in the
[2378.72 → 2383.48] upper right-hand corner are there some gaming convention or gaming aspects that you've either
[2383.48 → 2391.06] started or is it what is that zero notifications ah no notifications sorry yeah again I'm going to be
[2391.06 → 2398.54] talking to uh UX people to help me clarify all of that I don't actually want gaming uh aspects to
[2398.54 → 2405.62] this I don't it's really hard to do to game things well and encourage the right behaviour, and it's so
[2405.62 → 2413.64] easy to get it wrong and encourage the like really arbitrary wrong uninteresting behaviour and and and
[2413.64 → 2419.22] unhelpful types of competition so I'm gonna I'm trying to avoid that I fully agree with that I was
[2419.22 → 2423.70] actually thinking about that a bit ago I just happened to be studying the characteristics of a
[2423.70 → 2431.92] social network and like my day job I work um at pure charity which I guess is kind of one part social
[2431.92 → 2436.58] network one part crowdsource funding I was just thinking about like different things we've talked
[2436.58 → 2441.94] about and for whatever reason gaming was on my you know the these gaming things that have been
[2441.94 → 2447.34] all the rage that and then have kind of trickled off since then every time i kind of go into
[2447.34 → 2452.94] something that kind of gives me points I'm just like stop that yeah i just it's annoying you know
[2452.94 → 2458.52] don't do that I just want to do it I don't I don't like that stuff it drives me crazy a lot of the
[2458.52 → 2465.46] research around motivation has uh, so someone did some research with like kindergartners where they said
[2465.46 → 2471.74] they gave the kindergartners uh markers so that they could draw and that they would draw things and
[2471.74 → 2476.64] then they started rewarding them for their drawings giving them gold stars or points or whatever
[2476.64 → 2484.28] and those kindergartners stopped drawing unless they were given the rewards like they started
[2484.28 → 2491.04] drawing only if they were going to be rewarded for it and so it took away that internal drive to do
[2491.04 → 2496.74] something for the pleasure of just doing it that's why I hate money right that's why I hate money
[2496.74 → 2501.60] because I mean when you start working only because you want to make the uh the bonzes or whatever
[2501.60 → 2506.58] you know it's kind of it's not cool change your perspective it's even worse on the internet where
[2506.58 → 2512.54] you're you're basically modifying your own behaviour in order to affect like the number in somebody's
[2512.54 → 2518.80] database on some server somewhere across the world you know right now it's a 12 i really
[2518.80 → 2526.24] want that number to be a 13 it's so arbitrary and really valueless um that I get that at the same
[2526.24 → 2532.50] time uh sometimes it can be effective it just you know it is kind of uh putting it to good use
[2532.50 → 2538.38] and I think you're right that there 's's a lot of ways that that's uh that that can be used and
[2538.38 → 2545.98] end up having you know negative effects on your community yeah lets uh let's maybe tail end uh
[2545.98 → 2551.74] one piece here I got a question on i like the learning aspect when it comes to something like
[2551.74 → 2556.68] this so not just learning with exorcism, but you know your specific learning Katrina so you'd
[2556.68 → 2561.20] mentioned before we actually started recording yesterday when we're doing sound check you'd
[2561.20 → 2566.26] mentioned that we're pretty gen you know we're generally pretty bad at giving feedback and you
[2566.26 → 2571.84] kind of wanted to learn so that was also one of the parts that kind of um propelled you to do this so
[2571.84 → 2577.62] what have you what have you learned about feedback and people giving feedback so I mentioned a little bit
[2577.62 → 2583.54] of it earlier I realized that this sort of generic hey great thumbs up uh type of feedback
[2583.54 → 2592.16] isn't helpful because it's not actionable it's not specific um it is doesn't give you something that
[2592.16 → 2598.66] you can use to either repeat it or improve it so the feedback that I really have liked on exorcism
[2598.66 → 2606.50] so far has been feedback that is very specific about the code that is there right now I'm looking at
[2606.50 → 2612.16] this code and I'm seeing that this is repeating over and over is there a way to remove this duplication
[2612.16 → 2619.34] or I'm seeing that the same parameter is passed to all of these methods perhaps there 's's a
[2619.34 → 2626.24] know a second object um where these methods that these methods would belong in so it's looking at the
[2626.24 → 2632.18] the existing code and being very specific and actionable about the things that you see there
[2632.18 → 2640.36] rather than um either just being sort of generically positive hey that's great or um pushing it in
[2640.36 → 2646.44] directions based on some future speculative well maybe new requirements are coming down the line
[2646.44 → 2651.34] like we don't know anything about requirements let's just look at the code that we have and look at
[2651.34 → 2656.02] um the code smells or whatever that we can identify here and address those
[2656.02 → 2663.20] and uh I was just looking at my notes too I also want to glaze over this I was thinking about your
[2663.20 → 2668.32] your counterpart in writing the go seal I use uh I'm not sure if you say his last name so I don't want
[2668.32 → 2674.22] to butcher it but I know his first name is Mike mike gay art yeah he's a developer at pivotal labs
[2674.22 → 2681.68] and uh so we've been ever since he's he's based out of boulder which isn't too far from Denver so
[2681.68 → 2688.08] he comes down to the office that I work at every once in a while, and we've talked about design and
[2688.08 → 2693.30] refactoring and pairing and teaching and a bunch of those things, and he's been working on the cloud
[2693.30 → 2700.70] foundry command line client in go for the past few months uh so he helped me get started with that
[2700.70 → 2707.22] uh wrote all the basic things and then i um basically ask him for feedback when i
[2707.22 → 2712.92] start mucking about with things gotcha and I was just thinking about that because i I knew you had
[2712.92 → 2719.46] a counterpart so when we talk about exorcism is it just you like was you were you the founder of
[2719.46 → 2724.10] it the idea maker and do you have any counterparts so is mike like a long-time partner of this or
[2724.10 → 2730.70] will you play a larger role later on it was no it's just me um a lot of people have contributed
[2730.70 → 2737.52] so I think over a hundred people have contributed commits on GitHub to the actual web uh website
[2737.52 → 2745.44] and several people have um committed to the both the go client and the ruby gem which is now
[2745.44 → 2750.98] deprecated, and it's I think it's just people get kind of excited about the idea and spend a few hours
[2750.98 → 2759.50] doing something that's cool so we're we're probably at the point where we ask these
[2759.50 → 2763.52] common questions and I'm going to ask an uncommon question today because I like to throw curveballs
[2763.52 → 2768.86] here and there but uh you know I think we've kind of answered it a little bit and I'm not going to
[2768.86 → 2773.54] answer for you, I think you may have already answered though but if you weren't uh writing ruby what
[2773.54 → 2778.96] would you be writing I would be writing go and if you weren't writing go what would you be writing
[2778.96 → 2789.18] good one uh Erlang maybe yeah uh throwback to the days of win when win was on the show he used to
[2789.18 → 2796.12] always ask this and I missed this question which was I guess not language specific but project specific
[2796.12 → 2801.94] maybe so what is out there in open source like what project is out there that you wouldn't mind like
[2801.94 → 2807.04] spending a weekend you know forking and tweaking and maybe hacking with you know not like a language
[2807.04 → 2817.44] but just a project itself there are actually quite a few I would love to just go to uh there's
[2817.44 → 2824.62] there's a website that has a list of projects that need help oh really yeah I should look that up i
[2824.62 → 2832.82] cannot remember what it's called um code triage I think does that sound uh doesn't sound at the bell
[2832.82 → 2837.10] but if we don't get it in the show it's okay we'll put in the show notes so if you're listening
[2837.10 → 2843.58] you're like oh man okay I'll find it codes triage.com I'm hanging out there it hasn't rendered yet to the
[2843.58 → 2849.12] browser, but we'll see yeah I'm trying to load it too oh yeah help your favourite open source projects
[2849.12 → 2855.14] I think you have rung a bell yeah so i would just go there and find something that I actually use
[2855.14 → 2862.80] uh and go spend a weekend working on it anything in particular that uh that you may have already earmarked
[2862.80 → 2870.80] um I like Sinatra I use Sinatra a lot, and so I would totally love to spend a weekend just messing
[2870.80 → 2876.02] with Sinatra i have to imagine yeah as an instructor trying to get started quickly it's probably the
[2876.02 → 2881.48] the easiest to get started with like it's just one file right yes, and it's also very easy to explain
[2881.48 → 2886.78] like you explain the web, and then you say yeah we have got verbs, and we have post verbs, and you have
[2886.78 → 2891.48] a method named get and a method named post and there you are cool well I'm anxious to hear your
[2891.48 → 2899.32] answer to this next one which is who is your programming hero sandy metz sandy metz
[2899.32 → 2907.80] has been programming since 1978 uh she's been one of those people who just basically stayed in her cave
[2907.80 → 2914.84] and always programmed until I don't know maybe three four years ago where she went to a conference
[2914.84 → 2925.94] and was um caught in a hallway rant about design so this publisher from Addison Wesley overheard her
[2925.94 → 2932.02] ranting in the hallway at some ruby conference and spent two or three years convincing her to write a
[2932.02 → 2938.40] book yeah which she did and so that book it took her two weeks two years to write it just got published
[2938.40 → 2946.32] in September I think of last year and uh and if it's a book that really changed how I think about
[2946.32 → 2954.96] code the book she's talking about is uh practical yeah practical object-oriented design in ruby
[2954.96 → 2963.40] big fan of that book haven't read it all but big fan of it I'm I'm actually graduating up to it, I'm still
[2963.40 → 2969.56] uh working through eloquent ruby personally but uh and then also front of the show ABD Grimm he uh
[2969.56 → 2977.06] he's got a new book out uh confident ruby which um is just phenomenal or no so confident is the
[2977.06 → 2981.94] one from before no confident ruby is the latest yeah what was the other one because I keep getting
[2981.94 → 2988.96] them mixed up objects on there was uh exceptional okay sorry exceptional confident I love
[2988.96 → 2994.56] his approach to that too so that's pretty neat but another thing I'll recommend quickly um if you
[2994.56 → 2999.84] don't have the time or not into reading these books is to let the ruby rogues read the books as
[2999.84 → 3006.02] Katrina is one on the ruby rogues podcast and then listen to them talk about it for about two hours and
[3006.02 → 3011.28] you feel like you've read the book by proxy is that right quite yeah it's its outstanding we did an
[3011.28 → 3016.08] episode with sandy Metz, and we couldn't all be on there at the same time because six is just too many
[3016.08 → 3021.74] when we also have a guest so I set out that one because they were all such fanboys and totally
[3021.74 → 3027.84] wanted to be on the show and fought to stay on uh for the pretty gracious of you considering
[3027.84 → 3034.48] she's your programming hero, and you set out well i i I've stalked her in real life so I've actually
[3034.48 → 3043.94] met her um avid's confident ruby is going to be our uh our book club book tomorrow when we record
[3043.94 → 3050.98] nice so that that's also coming out soon yeah and if you're uh on that same note we're working with
[3050.98 → 3057.56] uh working on partnering with avid to provide that to our members so the change log is uh
[3057.56 → 3062.44] you know part sponsored part member based or part member supported but uh we have this section
[3062.44 → 3067.58] which is called members benefits which when we partner with people like digital ocean and avid and
[3067.58 → 3073.34] a bunch of other learning and developer resources uh we just work to get you a little bit of a
[3073.34 → 3078.82] discount to it and uh so keep an eye out for that we're working with avid on that so I'm a fan
[3078.82 → 3086.12] of the book but I think it's kind of neat just to kind of tie off on uh on sandy just uh what she says
[3086.12 → 3092.20] there she says if your code is killing you and the joy is gone potter has secure and I'm pretty sure
[3092.20 → 3097.92] that's how you say it right potters Porter okay yeah of course I'd get it wrong quite the name
[3097.92 → 3107.60] yeah right it's uh on pooter.info I think if you uh and I'm not even sure pooter.info is the
[3107.60 → 3113.80] website though pooter.com book pooter.com yeah that's right yeah thank you no worries
[3113.80 → 3119.52] at all but uh yeah I mean Katrina it was great having you on the show I mean I think that uh it
[3119.52 → 3125.20] was just kind of hearing your enthusiasm for refactoring and flow kind of just made me smile
[3125.20 → 3128.26] quite a bit during the show for sure I don't know about you jerry but I was smiling quite a bit
[3128.26 → 3132.64] during the show it's a shame we don't actually do these with our faces showing to the world like
[3132.64 → 3138.28] you know like uh YouTube live or whatever that thing is called but uh because this is a fun show
[3138.28 → 3143.40] but um thank you so much for taking the time to come on the show is there anything else you want
[3143.40 → 3148.90] to riff on real quick before we close out no I think I'm good thank you so much for inviting me yeah
[3148.90 → 3152.92] it's been an honour to have you on the show I know that uh jerry was a fan of yours with that talk
[3152.92 → 3158.54] that we'd mentioned during the show and I'm uh becoming more and more of a fan slash stalker
[3158.54 → 3163.40] whatever you want to call it but uh um yeah that's for sure, but definitely thank you for what you're
[3163.40 → 3169.58] doing with exorcism keep in touch too like whatever's changing whatever's happening get back with us as
[3169.58 → 3176.20] um as you have time I know you're really busy, but we'd love to help you keep um this in front of the
[3176.20 → 3180.26] of the people who are wanting to do a lot of this so whatever updates we can help you
[3180.26 → 3186.76] mention we definitely want to do that but uh for sure and I also want to thank our sponsor for the
[3186.76 → 3191.02] show digital ocean as I mentioned we I've been working with digital ocean for quite a while we're
[3191.02 → 3196.76] working with them over the next few months to kind of help um and just help them spread the news
[3196.76 → 3201.66] to the developer community about some of the awesome um things that they're working on whether
[3201.66 → 3205.22] ways they're supporting the community and one unique thing if you're
[3205.22 → 3211.12] uh really any developer out there whether you have an open source project or something that is
[3211.12 → 3217.62] specific to a server or whatnot they are paying 50 bucks to write tutorials basically I'll put a link
[3217.62 → 3222.58] in the show notes, but you know some examples can actually be used on digital ocean or just how to use
[3222.58 → 3229.02] your open source software so uh one example was how to install WordPress on a lamp stack on Ubuntu which
[3229.02 → 3234.60] I have no idea how to buy verbatim so i kind of go back to a guide every time and somebody got paid to
[3234.60 → 3240.34] write that article and make it really great um everything from we mentioned ghost and their uh
[3240.34 → 3246.04] and their support of ghost, so there's a how-to article on uh ghost and the one click install
[3246.04 → 3251.24] app they have for digital ocean, and we've talked about docker quite a bit we had Solomon hikes on
[3251.24 → 3255.72] the show quite a few backs but uh if you're a fan of docker, and you still want to play with it
[3255.72 → 3259.72] even though if it's not completely stable yet you have a docker application you can play with it
[3259.72 → 3264.02] just makes it really, really easy and as I understand it too Katrina they do some pretty neat
[3264.02 → 3271.44] support with you guys for um jumpstart lab they gave us a hundred instances that we can use as
[3271.44 → 3276.10] we wish any size they're very generous with us very generous and I think that's one part of
[3276.10 → 3280.44] why they've made some inroads into the community so one thing I've heard and this is kind of
[3280.44 → 3285.04] elongated just because i really absolutely love digital ocean but um as I've just heard people
[3285.04 → 3289.32] say well they're they're not that expensive so how can they be good well don't let the price fool you
[3289.32 → 3294.44] they just really want your business because they want to show you how awesome they are um if you're
[3294.44 → 3299.32] the kind of person to that likes to decorate your laptop uh you can email Barry at
[3299.32 → 3305.46] digital ocean.com uh he's gonna just tell him your uh shipping address he's going to ship you some
[3305.46 → 3309.28] digital ocean stickers but I've got a couple links in the show notes I'll put there for you
[3309.28 → 3314.62] uh and I also want to plug the coupon code the promo code we have which is the changelog October
[3314.62 → 3320.50] um and if you use that when you sign up you'll save ten dollars uh but uh that's it for the show
[3320.50 → 3329.12] check out digital ocean at digital ocean.com Katrina what's uh what's your website it's katrina.com k-y-t-r-i-n-y-x
[3329.12 → 3334.32] dot com wow awesome, and we want to thank you once again for coming on the show, and thank you for
[3334.32 → 3339.88] listeners to uh for listening and jarred thank you for uh being awesome the show as well so let's
[3339.88 → 3342.78] let's all say goodbye see ya bye-bye
[3342.78 → 3350.12] so
[3350.12 → 3352.02] you
[3352.02 → 3359.54] you
[3359.54 → 3363.72] you
[3363.72 → 3367.62] you
[3367.62 → 3368.20] you
[3368.20 → 3398.18] Thank you.
