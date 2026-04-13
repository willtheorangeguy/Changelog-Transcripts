[0.00 → 13.20] welcome back everyone this is the change log where remember support a blog and podcast
[13.20 → 16.86] take up with fresh and what's new in open source you can check out the blog at the
[16.86 → 22.66] changelog.com slash nothing in our past show I don't know why I said nothing check out the
[22.66 → 27.08] blog at the channel.com and our past shows at 5x5.tv slash changelog there's the slash
[27.08 → 32.84] the show's host by myself Adam Stokowski and Andrew Thorpe you're in aloha town man what's up
[32.84 → 37.08] hey how's it going yeah we're uh down in Waikiki beach in Hawaii I think this is the
[37.08 → 43.14] the first changelog that's being recorded out of Hawaii yeah that's that is a that's amazing and
[43.14 → 47.78] speaking of listening to the changelog continue live every Tuesday at 5 p.m Central Standard Time
[47.78 → 54.04] right here on 5x5 and this is episode number 92, and today we're joined by none other than mike
[54.04 → 59.06] parameter he's a rubies known for gems such as sidekick if you haven't used that you're wrong
[59.06 → 66.48] dolly and lunch uh welcome to the show mike thanks for having me guys so just to clarify mike is it
[66.48 → 73.16] parameter or Pelham or how do you say that it's param got it just like Birmingham Alabama
[73.16 → 82.24] Birmingham yeah my favourite person to say Birmingham Alabama uh is um is Brandon Mathis man he
[82.24 → 86.00] he I love the way he says he's been on the show before too and I don't know if you know him but
[86.00 → 92.76] he uh does octopuses oh sure yeah yeah he says Birmingham the best in my opinion
[92.76 → 99.34] well side note yeah I don't know how uh Alabama folks pronounce it but uh if they pronounce the
[99.34 → 101.26] ham then they're they're obviously doing it wrong
[101.26 → 111.38] speaking of uh of things just uh going right and wrong but uh good to have you on the show uh
[111.38 → 115.56] but wanting to have you on the show for a long time you know we uh at pure trader we use sidekick
[115.56 → 120.24] and as a matter of fact um it was pretty neat when we first started to use it because it was so fast
[120.24 → 126.40] it made us change things quite a bit but um because it would just run through jobs it's super easy
[126.40 → 132.10] but um for those who may not be familiar with who you are uh give the listeners a intro to whom
[132.10 → 139.22] you are mike sure um well I'm an I consider myself a rubbish at this point uh I've been doing ruby for
[139.22 → 145.28] about seven years uh before that I was doing java for almost a decade um but I'm a long time
[145.28 → 152.76] open source enthusiast and developer um and ruby just happens to be my tool of choice these days
[152.76 → 158.44] so yeah I've been working on uh you know the first thing I was really known for in the community
[158.44 → 164.56] was probably meccas client I took that over about five or six years ago and uh and polished it up
[164.56 → 172.80] and then uh from there i I moved on to dolly uh because i I wanted to um sort of write the next
[172.80 → 180.48] generation of meccas client, and then you said for go ahead you said for a while you've actually been
[180.48 → 184.86] writing software for you know a long time I mean I guess in comparison to maybe some people come on
[184.86 → 190.68] the show my first open source project that I released the source code for was 18 years ago
[190.68 → 197.50] oh and what was that if you don't mind me asking it was an application launcher for windows nt35
[197.50 → 206.32] wow yeah you go and and and that was back when I didn't know of any open source out there was
[206.32 → 211.70] really no windows source code available for you to use as sort of reference when you were building
[211.70 → 219.10] things so i uh i all I had was the MSDN documentation so I just wrote this little tool and put the
[219.10 → 226.24] source code up um on my website and this was um i you know I was in college at the time and
[226.24 → 231.60] when you're in college you're doing research projects and sort of everything's open source because
[231.60 → 237.92] you're you're an academic you know there's no commercial aspect to what you're doing so i I put
[237.92 → 244.06] uh the source code out for this little windows application out there and uh yeah just went uh
[244.06 → 251.82] open source and windows at that time uh was non-existent it was all shareware I didn't even I guess I mean
[251.82 → 256.32] I haven't always been in the open source community, but that's kind of neat to think about 18 years ago
[256.32 → 261.46] what open source was like and how drastically different the landscape has become with not just GitHub
[261.46 → 267.88] but just democrat uh democratizing sharing code, and you know everything from the movement GitHub
[267.88 → 272.82] has started with sharing code and GID and all that stuff but well it's pretty wild to think about that
[272.82 → 278.82] you're showing your age, and perhaps I'm showing my age because uh GitHub wasn't the first revolution
[278.82 → 284.52] the first revolution for me uh was sourceforge.net you know yeah they're they're a popular punching bag
[284.52 → 290.76] these days but uh you know I joined them I think within about the first month of them going public
[290.76 → 296.42] and that was a revolution too because before then you had to set up your own CBS server you had you
[296.42 → 303.66] um distributed tarballs through a ftp site generally having this software as a service
[303.66 → 309.16] uh and for free to the community was really revolutionary it seemed like you really had to
[309.16 → 312.98] want to be a part of the community at that point right I mean you really had to push to get in because
[312.98 → 319.46] of the the know the barrier was not quite as low as it is today uh yeah and I think each
[319.46 → 324.06] uh you know SourceForge lowered the barrier to some extent and GitHub has lowered it even further
[324.06 → 330.26] that's just you know that's uh improvements over the lifetime of uh a community I guess you could
[330.26 → 335.46] say yeah SourceForge is like you said it's kind of the popular thing to be the punching bag but
[335.46 → 340.06] there's something to be said about a service that's lasted as long as they have I mean you'll
[340.06 → 345.02] still see a project sometimes that is on SourceForge and I think I don't know if iterm2 is
[345.02 → 350.00] still on there, but it was on there for the longest time so it's still around, and it's still definitely
[350.00 → 355.28] uh kicking which is there's something to be said about anything on the web that lasts that long you
[355.28 → 360.60] know yeah well you know like anything their heart was certainly in the right place at the start
[360.60 → 368.78] and um you know it just entropy has you know taken it down over the years to where uh you know the
[368.78 → 376.14] the UI was let's just say not great and uh you know there were ads everywhere and it was obvious
[376.14 → 381.00] that the user was not the customer we were just eyeballs for their ads, and they just happened to
[381.00 → 387.40] be in the developer space and that's why GitHub sort of ate their lunch that's a pretty unique
[387.40 → 392.20] little thing you just said there because one of the one of the ways we I don't I don't know if you're
[392.20 → 396.86] a long-time listener and follower of the change law but um we kind of had a dark period this past year
[396.86 → 401.94] around August to December, and it was just kind of reorganization and whatnot when we
[401.94 → 409.44] relaunched um we decided not to put ads on the site um and a bunch of other decisions, but we tried to
[409.44 → 414.70] I guess and if you didn't know this the change log is member supported so if you're listening
[414.70 → 421.04] um you can go to the change log.com slash membership and sign up to support what we're doing we
[421.04 → 426.76] have writers that uh cover all sorts of open source and I'm sure we've even covered psychic at uh at one
[426.76 → 431.44] point in time and right actually not recently we uh we had a nice post from Kelly martin one of the
[431.44 → 435.50] guys that works with us a pure charity covered psychic so I think even in there he was talking
[435.50 → 441.08] about how fast it was so it's just uh pretty well, but you'd mentioned who the customer is and I think
[441.08 → 447.34] that's that's pretty it's pretty neat to look at how GitHub has changed uh you know their focus
[447.34 → 452.88] on open sources helping developers be better developers and helping code be more shareable
[452.88 → 460.26] more workable you know more liberated I guess is the easiest way to say it right yeah it's uh
[460.26 → 467.46] it's really kind of revolutionized well again you've got revolutions every five or ten years it
[467.46 → 472.80] seems like but um they've been certainly the latest revolution and by all accounts they're a huge
[472.80 → 479.94] success so why don't we go ahead and this is great conversation why don't we go ahead and jump into the uh
[479.94 → 485.62] the meat of the call uh, and so we're we kind of want to talk about sidekick um and kind of what it
[485.62 → 490.88] is and not necessarily just how fast it is, but you know why is it yeah why is it so fast I think
[490.88 → 496.38] uh mike if you don't mind I think a good thing to start with is why don't you give us a little bit of
[496.38 → 502.04] a not I don't know lesson on what uh message passing and message processing or message processing is and
[502.04 → 505.80] and how it's been handled in ruby traditional and what makes sidekick different
[505.80 → 511.96] sure um yeah I mean I was thinking about this weekend and how to describe sidekick
[511.96 → 518.86] i my current best thoughts around how to describe sidekick is it's an it's a background processing
[518.86 → 522.34] framework um i I think of it kind of like
[522.34 → 531.74] did we lose mike I think so I'm here I pressed the mute button now my microphone accidentally sorry
[531.74 → 537.62] about that guys try again so sidekick is a framework for background processing kind of like
[537.62 → 545.18] rails is a framework for web applications and I try to provide all the sort of all the tools necessary
[545.18 → 553.46] to build an application that has a non-trivial asynchronous processing component to it
[553.46 → 560.64] and so that's that's sort of what shapes the design um and the directions that I go
[560.64 → 568.46] with regard to sidekick features and functionality um the know when you get right down to it uh
[568.46 → 575.72] sidekick's competition is gyms like delayed job and rescue q classic uh those sorts of gyms
[575.72 → 583.68] um but sidekick uh is different from those three in that it is explicitly multithreaded
[583.68 → 590.42] instead of running one thread per process and having each process one job at a time
[590.42 → 597.36] you're processing many jobs uh concurrently and that's really where it gets a speed sidekick is
[597.36 → 604.58] not any faster than rescue if you change sidekick's concurrency to be one but if you're use if you're
[604.58 → 612.20] using sidekick in its default mode it's going to process 25 jobs concurrently which means that if
[612.20 → 618.38] you have one rescue process and one sidekick process sidekick's going to ultimately go 25 times faster
[618.38 → 624.58] all other things being equal of course and that's where it gets its speed is the concurrency and the
[624.58 → 630.66] multi-threading so the idea of a message processing so for anyone who doesn't know like
[630.66 → 634.26] if there's something that you want to push off into the background that you don't want to you know
[634.26 → 639.98] take time for let's say on user create you want to send an email you would push that into a queue to
[639.98 → 644.56] be to be processed in the background so that it doesn't take you know take up time on the
[644.56 → 651.38] front end for the user to wait for those emails to be sent correct exactly anything you want to do
[651.38 → 658.74] asynchronously um is uh is a possibility to push into sidekick uh let me give you an example you
[658.74 → 665.74] gave the example of an email that's a great example any third-party call that we do um here at my
[665.74 → 672.40] full-time job here at the climb uh we try to push that into a sidekick job so that we don't have explicit
[672.40 → 680.56] third-party network dependencies in our application execution um sidekick has this full-featured robust
[680.56 → 686.62] retry mechanism so if a job fails sidekick will actually retry it and when you've got a third-party
[686.62 → 691.60] network call the network could be down that uh that third party could be down for maintenance
[691.60 → 696.36] there 's's any number of reasons why that call could fail and so having a retry mechanism
[696.36 → 704.40] for uh asynchronous processing is critical in my opinion yeah that retry mechanism you talk about is
[704.40 → 710.36] is fascinating and I think if you've maybe come from you know rescue or delay job and moved to
[710.36 → 716.00] sidekick which i I think a lot of people have it's kind of uh you have to it could almost be a gotcha
[716.00 → 723.66] so the idea is that if the job fails there's a what do you call it an uh in between retries queue
[723.66 → 730.74] but in between retries the amount of time increases it's an exponential back off right, so the idea is
[730.74 → 737.32] what is what is the amount of time between the first retry it's 15 seconds and then the between
[737.32 → 742.16] the last and second to last how long would you wait uh I think it's like I think it's like three
[742.16 → 749.04] days right, so the idea is that if is you're not like it gives you a lot of time to fix it and then
[749.04 → 752.88] it also deals with the case and like you said you know network issue or something like that that's
[752.88 → 757.08] going to resolve itself very quickly and so that's something that we had to get used to up here
[757.08 → 762.06] charity because I mean we I think we maybe jumped the gun a little bit and just started using side
[762.06 → 766.68] quick side quick hey that's a good name we just started using side because of this you know the
[766.68 → 771.00] potential speed boost we could get and there were a few gotchas you know that we kind of had to just
[771.00 → 777.24] learn and the retry one uh while it's its I mean it's a lifesaver in every case it definitely
[777.24 → 780.68] was something we had to make sure we read about to understand what was happening
[780.68 → 787.96] the other gotcha that I think has you've actually documented in the wiki that people have
[787.96 → 793.16] had to deal with is the uh idea the after commit thing can you kind of talk about that a little bit
[793.16 → 801.14] yeah of course the uh the gotcha is that a lot of people want to perform background processing on
[801.14 → 807.04] a newly created database record so you create a new user record, and now you want to send them email
[807.04 → 815.64] so generally what you do there is you create the user and then fire off a background job with that
[815.64 → 821.46] user's ID to sidekick and then sidekick will look up that user and then email them
[821.46 → 829.12] the problem is that sidekick is so fast that sometimes that user creation transaction has not
[829.12 → 836.94] actually committed such that the sidekick database connection still can't see that user object and so
[836.94 → 845.28] it'll throw an exception saying no such user exists and then 15 seconds later when sidekick retries that job
[845.28 → 853.50] now it'll exist, and now it'll work, so people find themselves often seeing errors that immediately fix
[853.50 → 859.54] themselves and generally that's because of this problem where you need to move the creation of that
[859.54 → 867.36] sidekick job into an after commit callback so that you know that the depth that the user record has been
[867.36 → 872.52] committed and is visible to everybody else in the database before the sidekick job is created
[872.52 → 879.74] yeah so basically it's not necessarily a gotcha it's just like I said it's something that you have to
[879.74 → 885.38] just be aware of and it is tends to fix itself for people that never actually address the problem
[885.38 → 890.76] because of the exponential back off on the retry queue which is pretty cool that exponential back off
[890.76 → 895.84] seems I mean just from an outsider who doesn't do much of what you guys are talking about I'm still
[895.84 → 902.40] kind of in the early echelon of uh being a true hacker I suppose but um you said 15 seconds and the
[902.40 → 908.72] next retry is days later right no, no it's exponential back off which means it is does 15 seconds then 30
[908.72 → 916.12] seconds then a minute and then and then five minutes and so it'll, it actually does about 25 retries
[916.12 → 923.80] at ever-increasing delays was that after that last retry if it fails on that last retry what
[923.80 → 930.48] happens to the job it actually calls a callback on your worker if it's defined called retries exhausted
[930.48 → 936.50] and if it and if you don't have that callback it just discards the job assuming that it'll never
[936.50 → 941.46] succeed so you can address the problem of it failing 25 times however you want basically
[941.46 → 949.40] exactly yeah that's that's pretty cool so I think we talked a little bit about it but I would love
[949.40 → 955.10] to kind of talk about so was the main reason that you decided to create this and even though there
[955.10 → 960.34] were solutions like delayed job and rescue out there was to take advantage of the growing popularity in
[960.34 → 965.54] the multithreaded room environment well there was a couple of reasons why I wanted to build
[965.54 → 973.26] sidekick performance was certainly probably number one i I worked on rescue for a customer
[973.26 → 980.58] um i previous to my current job I was a consultant at carbon five which is a consultancy in San Francisco
[980.58 → 987.40] and they had a had a client which um was using rescue, and they were doing thousands of jobs
[987.40 → 992.88] and they had I think 10 different machines that were just dedicated to running rescue
[992.88 → 998.82] and they were actually using Ruby which is the worst of both worlds because the JVM is this
[998.82 → 1004.62] big behemoth and the way you achieve efficiency through the JVM is you run it a lot of threads but
[1004.62 → 1010.54] rescue is single threaded, and it forks so now you have these JVM processes which are gigantic and
[1010.54 → 1017.12] they're single threaded so it's its absolutely horrible for efficiency reasons so what I did is
[1017.12 → 1024.72] actually um I patched rescue to be multithreaded, and they went from 10 machines down to one machine
[1024.72 → 1033.52] because we could leverage threads right and uh so once I saw that sort of kind of benefit I realized
[1033.52 → 1040.16] there had to be a market for some improvement here, and so I started building sidekick since then I've
[1040.16 → 1047.86] uh you know there have been other reasons why I think sidekick is a great leap forward i I think
[1047.86 → 1053.18] another big one is the fact that rescue is rather bare bones in its basic configuration it doesn't
[1053.18 → 1059.52] have a lot of extensions it doesn't have a lot of APIs it's really just I process jobs on a queue and
[1059.52 → 1066.14] that's basically it sidekick just has a lot more like scheduled jobs it has the whole retry system
[1066.14 → 1073.74] uh it's just, and it's got a full uh meta API so that you can actually uh query Regis for all the
[1073.74 → 1078.80] different jobs and queues and workers and what they're doing currently it's just got a lot more
[1078.80 → 1085.32] features to it and so uh that's that's another big reason why I felt that with rescue I had to
[1085.32 → 1092.96] bring in 10 or 15 different plugins just to get a decent uh full functional system so you kind of
[1092.96 → 1100.06] talked about you were working at carbon 5 um, and you started sidekick what was it like when you
[1100.06 → 1104.08] this is an interesting thing because I think this might you might be the first person that
[1104.08 → 1110.30] started working on an open source project at a past employee or past employer then continued working
[1110.30 → 1116.74] on this through you know whatever you were doing until your current employment situation so what was
[1116.74 → 1121.04] what was that like just the just starting this project when you were working somewhere else
[1121.04 → 1127.24] let me sorry go ahead you're you're um let me correct you the timeline's actually wrong i
[1127.24 → 1134.46] started sidekick when I left carbon 5 I had uh I think two weeks downtime when I was moving from San
[1134.46 → 1140.40] Francisco to Portland and during those two weeks of downtime i I wrote the first version of sidekick
[1140.40 → 1147.66] basically i I didn't I was basically you know i I quit on Friday and on Saturday morning I was like
[1147.66 → 1153.66] well what do I do um nice well that that multithreaded rescue thing was pretty awesome and
[1153.66 → 1158.42] I haven't had a lot of time to build it why don't I build it, and so I just started working on it there
[1158.42 → 1168.36] so uh so yeah it the the the impetus the idea came from working with a client of carbon 5s
[1168.36 → 1174.56] but I actually started it after I had left okay gotcha so what was the so you have this
[1174.56 → 1181.88] sidekick the gem you also have sidekick pro when did the uh idea to fork that into its own uh service
[1181.88 → 1193.28] come about so when i wrote sidekick the first couple months um I had a having been a long
[1193.28 → 1200.08] time open source person I'm not a 20-year-old guy that can afford to spend his nights and weekends on
[1200.08 → 1208.70] everything on stuff just uh just to learn stuff um I have a family and a wife and kid, and so I wanted
[1208.70 → 1216.62] I wanted people to be able to pay me for what I was doing uh and so when sidekick first came out I gave
[1216.62 → 1224.14] people the um the ability to pay for a license basically I released it as LGPL and then I allowed
[1224.14 → 1229.98] people to pay me 50 bucks to get a commercial license if their lawyers didn't like it and this
[1229.98 → 1235.62] brought in a couple of hundred bucks but at the end of the day it was chump change compared to the
[1235.62 → 1243.88] hours I was actually spending on sidekick so at that point um you know you there's a fork in the road and
[1243.88 → 1249.52] you really have to decide what you want to do here with a lot of big open source projects they go the
[1249.52 → 1254.80] consulting route um take ember for instance is one currently and of course my sequel is a long
[1254.80 → 1259.92] time one where you have this open source core project, but then you have a services and consulting and
[1259.92 → 1266.98] training around it that also brings in money and so I had to decide well do I want to be a
[1266.98 → 1273.10] consultant and try and drum up business and maybe hire people and start a company around this
[1273.10 → 1281.04] or or or what do I want to do and when it came down to it, I just didn't want to do that I enjoy my
[1281.04 → 1287.08] job right here I enjoy having free time with my family I didn't want to start a startup you know
[1287.08 → 1293.16] one man startup to try and uh and try and build this thing so I decided to go the product route and
[1293.16 → 1299.46] actually try to build a premium product on top of the open source foundation and that's really what
[1299.46 → 1307.96] sidekick pro is it's a set of functionality that extends the free open source version
[1307.96 → 1318.84] with some really valuable capabilities and that's uh that's where I think um I think a lot of open
[1318.84 → 1326.92] source people who are uh who want to spend months and years maintaining projects you know they need to
[1326.92 → 1331.10] they need to get paid for their time it's its a valuable resource that they're providing to the to
[1331.10 → 1337.22] the community and I don't think there's anything wrong with uh either uh accepting either building
[1337.22 → 1342.14] some sort of value-added product on top of the open source or um you know asking for like get tips
[1342.14 → 1346.82] and that sort of thing so that's that's been a that's been kind of an interest of mine over the last
[1346.82 → 1353.54] few months is how do we make uh open source not only valuable to young people who are trying to
[1353.54 → 1358.44] learn and wanting to hack on weekends on small projects but also longer term bigger projects
[1358.44 → 1364.32] that really entire communities are relying on like rails like sidekick like um you know maybe
[1364.32 → 1371.86] Sinatra and those sorts of uh those sorts of gyms, so a lot of people do this kind of thing like
[1371.86 → 1377.28] you know you have Regis, and you have Regis to go which is just a know providing Regis as a
[1377.28 → 1382.36] service, but sidekick pro is a little different in that you actually enhanced sidekick and added some
[1382.36 → 1387.70] functionality not just providing purely sidekick as a service in and of itself so what is the
[1387.70 → 1394.98] functionality that you added to pro to make it pro right so the there 's's a couple big features
[1394.98 → 1402.50] that pro has on top of sidekick the first one is this notion of a batch so you can create a set of jobs
[1402.50 → 1411.54] which when all those jobs are complete the can have callbacks called, or you can have
[1411.54 → 1423.06] notifications sent out um and that that is really valuable from an uh scatter gather kind of
[1423.06 → 1429.84] standpoint if you think about um some work being done you want to and if you think of sidekick
[1429.84 → 1437.24] uh really tries to be uh a framework for building concurrency into your application so that you can
[1437.24 → 1443.22] parallelize a lot of work, but the problem is that by parallelizing things asynchronously you don't
[1443.22 → 1449.54] know when anything is done right it's you want to receive an email for instance when your thousand
[1449.54 → 1455.44] jobs are done, but you can't do that with normal the base sidekick and that's what a batch allows you
[1455.44 → 1462.26] to express is you say I want to create a batch of these thousand jobs and when all thousand are complete
[1462.26 → 1469.26] email me or call this method so that's that's the first feature that that sidekick pro gives
[1469.26 → 1477.24] you the uh the second feature is uh reliability the sidekick tries to be as reliable as possible
[1477.24 → 1483.94] but there are native extensions and ruby VM bugs that cause the ruby VM to simply crash
[1483.94 → 1491.10] and there's nothing sidekick can do about that except to change the way that it enqueues jobs
[1491.10 → 1500.22] in Regis and so pro offers you an alternative way of enqueuing such that if sidekick crashes
[1500.22 → 1509.46] that job is still in Regis, and it's not lost because with the base sidekick when you pop a job off to work
[1509.46 → 1516.62] on if it's popped off into memory, and it's its gone it's gone from Regis so if that job does not
[1516.62 → 1525.00] if the VM crashes that job is lost, so those are two of the big uh features that
[1525.00 → 1532.40] people have been buying pro for right so it's kind of the best of both worlds anyone uh who is a
[1532.40 → 1537.58] know not I wouldn't say anyone but you know most people who are experienced ruby developers could
[1537.58 → 1542.44] probably develop sidekick pro, or you know something because of the foundation that sidekick offers
[1542.44 → 1549.54] but the amount of time it would take makes that 500 cost to get sidekick pro like you said seem like
[1549.54 → 1555.06] chump change right so it's absolutely worth spending that money if you need those utilities
[1555.06 → 1562.22] it's funny I've gotten many people saying that sidekick pro is too cheap and I've gotten a couple a
[1562.22 → 1567.58] couple people saying that sidekick pro is that's ridiculous how dare you charge 500 for that thing
[1567.58 → 1574.64] but yeah like you say when you think about the cost of a ruby freelancer a good freelancer is
[1574.64 → 1581.54] going to cost you know 100 150 an hour so you're talking you know three to five hours
[1581.54 → 1586.92] of a good developer's time, and you get this functionality and if it solves a problem for you
[1586.92 → 1594.20] you know you pay the money literally you have it 10 minutes later and the problem solved so
[1594.20 → 1599.66] so, so yeah I mean the reality is there are a lot of businesses out there that are willing to pay a
[1599.66 → 1605.16] couple hundred bucks to make a problem go away immediately I had um a customer at rails cone
[1605.16 → 1613.06] who found that uh his sidekick processes were crashing, and he was losing jobs and I told him
[1613.06 → 1618.68] listen you can continue to sidekick, but you're going to have to debug why this crash is
[1618.68 → 1624.52] happening and time is of the essence here because you're losing jobs every day when these
[1624.52 → 1630.62] things crash the alternative is pay 500 bucks and make the problem go away yeah you know it's not the
[1630.62 → 1635.56] sidekick code that's causing the crashes it's something in the application in the gyms that it's using
[1635.56 → 1642.34] that's causing it to crash right so that that's out of my control i you know I'm I'm sorry i i I feel bad
[1642.34 → 1650.28] that you that the process is crashing i I certainly hate it when it happens to me but um, but you pay a
[1650.28 → 1656.08] couple hundred bucks and the problem goes away because you know you restart sidekick pro and the
[1656.08 → 1661.94] jobs just start processing again right could I be asked a question that might be maybe everyone else is
[1661.94 → 1665.74] thinking of this when they're when they're listening to talk about this but since sidekick is open source
[1665.74 → 1670.90] and um I guess you are the core committer of course that you're the creator of it but
[1670.90 → 1677.34] is it plausible or is it possible for someone to fork it add similar functionality to sidekick pro and
[1677.34 → 1683.36] and kind of do that like sends a pull request would you accept that would you accept things that
[1683.36 → 1690.94] mimic or recreate sidekick pro functionality well that's a great question um you know you could fork you
[1690.94 → 1695.60] could fork sidekick and as long as you do what's legal under the license you know it's its
[1695.60 → 1700.40] fair game I think there 's's a difference between it wouldn't be cool of course don't do
[1700.40 → 1704.20] this anybody I was going to say there's a difference between what's moral and what's ethical yeah
[1704.20 → 1708.58] I'm not saying anybody should do that I'm first I wouldn't say anybody should do I'm just
[1708.58 → 1713.90] wondering if that is you thought about that if that's a concern really i I actually did um
[1713.90 → 1719.24] but I think the amount of time it would take to create the features is non-trivial
[1719.24 → 1725.16] such that you know if you want the features just pay for it is your time really
[1725.16 → 1734.36] so um so worth so little that you're willing to spend you know 20 30 50 hours to rebuild this
[1734.36 → 1741.80] feature um and then and then release it to the public you know i I don't know that really
[1741.80 → 1747.90] makes a lot of sense and like I said it may be legal under the license but yeah at
[1747.90 → 1752.76] the end of the day it's just not very cool um I work really hard and spend a lot of hours on
[1752.76 → 1758.24] base sidekick giving that away for free for someone to just sort of copy the features and
[1758.24 → 1764.92] release it and sort of eat my lunch um you know it just doesn't seem very friendly can we talk about
[1764.92 → 1770.26] your lunch for a little bit I'm just curious since this is 500 bucks a pop I'm not you don't have to
[1770.26 → 1773.80] give out any exact numbers I'm just curious how successful this has been for you since uh
[1773.80 → 1781.40] because it's half a grand I well I've it's been for sale for I think eight months now and I'm I'm
[1781.40 → 1790.28] nearing 100 customers wow nice so I wanted to ask you actually that you kind of uh hit on it a
[1790.28 → 1795.34] little bit Adam and I wanted to ask you has anyone else released sidekick as a service be it the pro
[1795.34 → 1802.36] version or other features or just the base sidekick or anything that's an interesting question and
[1802.36 → 1810.62] certainly when I was thinking about where to go with sidekick um doing sidekick as a service it was
[1810.62 → 1817.54] one of the directions I thought um there's a company out there called iron Io I think it's called
[1817.54 → 1825.62] that does message processing as a service um and so it is definitely is possible to do it
[1825.62 → 1832.08] my biggest issue is simply that I have to provide an execution environment for people's
[1832.08 → 1839.74] worker code so the ruby code has to execute on my sidekick servers, and you know that
[1839.74 → 1845.88] means that you have to sandbox ruby and there's you basically have the same problem that Heroku has
[1845.88 → 1851.96] which is your have possibly a malicious application running on your server, so there's this whole sandbox
[1851.96 → 1857.40] that you need to build and that's non-trivial right and I didn't I didn't know how to do that and i
[1857.40 → 1862.60] didn't to be honest didn't really have a lot of interest in building it so that sort of deep fixed
[1862.60 → 1870.12] that idea gotcha I wanted to roll back I meant to ask you this a minute ago um subsists love semantics
[1870.12 → 1875.76] right, and they love to spend tons of hours arguing about what's the right way to do something what's
[1875.76 → 1880.66] the ruby way what's the rails way right so now I wanted to ask this before we were talking about
[1880.66 → 1888.44] rescue so let me get this in real quick the perform method in rescue um it was a class method right and
[1888.44 → 1892.16] in sidekick you decided to do it as an instance method I was hoping you could kind of elaborate
[1892.16 → 1899.94] on why you chose that sure to me that's a fundamental decision due to the multithreaded nature of sidekick
[1899.94 → 1905.32] the reality is when people write code they're going to use instance variables
[1905.32 → 1912.34] simply because they're not going to pass method arguments to every single method necessarily
[1912.34 → 1920.04] in the class that they're using so when you use instance variables in an instance you're
[1920.04 → 1924.96] multithreaded safe but when you use instance variables in a class method you are extremely
[1924.96 → 1933.98] thread unsafe and so the reason why I designed it that way is because I'm trying to guide people
[1933.98 → 1942.10] to writing ruby code that is multithreaded safe and will work well in sidekick and so using a
[1942.10 → 1951.16] a class method perform would immediately cause threading problems for almost everyone as far as i
[1951.16 → 1958.40] as far as I'm concerned so yeah that I had to change that to make people's code safer gotcha so like
[1958.40 → 1963.92] you can assume being a ruby is there was an uh as you put it a fundamental decision as to why it was
[1963.92 → 1971.36] that and not that you just willy-nilly chose that so it's good to know yeah exactly uh so being
[1971.36 → 1977.58] has there been any interest in the rescue or delayed job or any of those camps to kind of mimic sidekick
[1977.58 → 1985.18] and go multithreaded or have you heard about anything like that uh I've heard rumours here and
[1985.18 → 1992.76] there of rescue 2.0 being under development and them wanting to provide sort of pluggable concurrency
[1992.76 → 1999.00] you know you could use a forking model, or you could use a threaded model or maybe a hybrid approach
[1999.00 → 2004.98] I'm not sure um but I don't know what the latest of that is um as far as I know i I mean i
[2004.98 → 2009.90] heard those rumours a year ago and I don't know if is they've made any progress or what i certainly
[2009.90 → 2015.82] haven't heard of or i I don't know what the latest is with regard to rescue 2.0 gotcha
[2015.82 → 2021.52] and I haven't I haven't uh kept up with delayed job at all so I don't I don't I certainly
[2021.52 → 2029.76] went when I'm beyond that well i when I was uh when I was building sidekick initially i certainly
[2029.76 → 2036.02] trolled through their readies looking for features that were cool and uh stuff that I could uh
[2036.02 → 2042.70] that I could sort of liberate and reuse myself in sidekick, and you know from delayed job I took the
[2042.70 → 2048.32] delay method uh because I thought that was a great idea and um and certainly from rescue
[2048.32 → 2055.10] heavily influenced sidekicks uh data formats in Regis and the initial sort of way it worked
[2055.10 → 2061.12] right for anyone listening that was not intended to be a shot at delayed job uh just I think that
[2061.12 → 2066.10] we've kind of we used a job and well I look at it similar to how we were talking about the source
[2066.10 → 2072.52] forge and yeah the things delayed job was like a lifesaver for us um at one point, and they've been
[2072.52 → 2077.08] around for so long now but I think the ruby community loves to go with the hot and fresh and
[2077.08 → 2082.12] the new whatever that is so so so sidekick is hot and fresh but for those who maybe just
[2082.12 → 2087.70] uh just learning ruby or just getting started how does one choose one of these three delayed job
[2087.70 → 2092.62] rescue or sidekick do you just jump in right into sidekick or is it so fast that you just can't
[2092.62 → 2097.46] you know hold it down you've got to maybe try something else to keep it slow for a bit maybe not
[2097.46 → 2103.64] worry about the after commits and stuff there's like any sort of software decision
[2103.64 → 2109.62] you have to evaluate you know what's out there and what's appropriate for you a lot of people don't
[2109.62 → 2114.32] want to use sidekick because they don't want to bring in Regis for instance right a lot of people
[2114.32 → 2120.56] choose q classic because they're already on Heroku they're already on Postgres they literally need
[2120.56 → 2127.32] to add nothing except the gym and a couple ruby classes and that's it and that's perfectly
[2127.32 → 2132.80] okay you know sidekick isn't perfect for everyone I use Regis because I think it offers an amazing
[2132.80 → 2138.68] amount of functionality uh so you know you just have to decide what's appropriate for you q classic
[2138.68 → 2145.98] is great if all you want is Postgres yeah because you kind of graduate as you know as you begin to
[2145.98 → 2152.04] learn like you'd mentioned earlier Andrew those that are seasoned subsists um you know they have
[2152.04 → 2158.58] certain things about them, you know a class versus an instance or those types of things and um
[2158.58 → 2163.10] yeah I feel like you know even me as I learn ruby and as I get deeper into learning rails
[2163.10 → 2169.20] and using it that i kind of graduate into certain things like oh I should use this versus that
[2169.20 → 2173.50] and I just wondered what the know what the process might be there, and it's a good point
[2173.50 → 2178.38] mentioning Postgres and even being able to use it on Heroku and not having to do extra things to
[2178.38 → 2183.30] utilize sidekick well and there's something to be said too Kenneth writes on one of our previous shows
[2183.30 → 2188.86] talked about the tribal knowledge that these communities develop right, so sidekick was birthed
[2188.86 → 2195.00] out of that's a weird way to put it, but it was born out of a need right that rescue was not necessarily
[2195.00 → 2200.98] solving and so a lot of people who were using rescue said oh this is what I need so you migrate to
[2200.98 → 2207.70] sidekick so somebody who's just now coming to the community they might, you know see these are all
[2207.70 → 2212.20] my choices and I don't know which one to pick but somebody who's been doing message processing for the
[2212.20 → 2218.40] last you know eight years has kind of followed the trend as the needs have grown and the solution has
[2218.40 → 2223.78] been you know created in the sense of sidekick versus rescue versus delayed job and the different
[2223.78 → 2228.58] technology so there is something to be said about that you know and so when a newcomer
[2228.58 → 2234.58] I mean I would venture to say that when a newcomer jumps into the community their choice will most
[2234.58 → 2241.14] often be whatever is recommended to them from the people they ask and so you know I mean for me
[2241.14 → 2248.20] personally yeah for me personally like I am gonna typically recommend sidekick because of the trend
[2248.20 → 2252.14] and multi-threading and where you can go with it and the amount of you know efficiency that's gained
[2252.14 → 2257.16] from it and um you know that's just kind of the way it goes it's that tribal knowledge that the
[2257.16 → 2262.52] communities develop well since you mentioned it like that I mean is um, and we're kind of talking
[2262.52 → 2267.34] about this what's the overhead for those that might want to use sidekick you'd mentioned the need to
[2267.34 → 2272.38] utilize Regis and stuff like that I don't I'm not shaving I don't I know I don't use Regis but uh
[2272.38 → 2277.38] at least not yet but what is the overhead of adding Regis to your application stack and
[2277.38 → 2285.86] uh getting up and running with that i I think that Regis is a pretty amazing piece of work
[2285.86 → 2293.60] um anti-res is a pretty awesome developer open source wise I mean very knowledgeable you know
[2293.60 → 2300.16] the community uh loves to argue about you know cap theorem and what have you around his work but
[2300.16 → 2306.32] you know at the end of the day Regis has been amazingly reliable and hasn't given us a single
[2306.32 → 2314.92] problem so I'm I'm a big fan of Regis in general um adding Regis to your application is pretty darn
[2314.92 → 2321.08] simple I mean Regis is almost as simple as geocached as far as I'm concerned in terms of setting it up
[2321.08 → 2328.54] and running it um and then you just point uh just point sidekick to it, and you're done um
[2328.54 → 2335.48] there's really not a lot of administrative overhead to Regis and that's on purpose that's one of the
[2335.48 → 2341.72] reasons why I chose Regis is I wouldn't be you know I wouldn't ever think to use something like
[2341.72 → 2347.76] for instance Cassandra as a data store for sidekick just because it's so complex to set up, and you know
[2347.76 → 2354.54] it's really designed to run on many machines well sidekick needs to be able to scale from a single
[2354.54 → 2362.64] person running on one machine to uh to you know an application running on a dozen you know
[2362.64 → 2371.74] dozens of machines so uh you know Regis kind of fits that bill pretty well so the I've
[2371.74 → 2377.70] used lunch dolly and sidekick all in different times of my life and one thing that's interesting
[2377.70 → 2384.30] to me and i maybe you can kind of speak on this a little bit is sidekick has by far been the most
[2384.30 → 2390.64] popular of the tools you've created um even though all of them have served a need you know at some level
[2390.64 → 2396.46] for me so what do you think it is about sidekick that has made it so popular compared to you know
[2396.46 → 2405.68] other projects that you've done well you know when it comes right down to it um lunch is just a little
[2405.68 → 2412.40] it's just a little command line tool that solves a very, very basic problem um it's not it's not uh
[2412.40 → 2422.22] it's not solving big problems that people have um you know every single day right in in in terms of
[2422.22 → 2429.52] their application and how to build their business uh dolly is basically just another it's an it's a
[2429.52 → 2437.12] faster teacake client, but it basically connects your application to teacake there 's's no there's
[2437.12 → 2442.46] no way to spin it and make it more than it really is there sidekick on the other hand is like I said
[2442.46 → 2449.76] I've tried to make it into this framework for background jobs and a lot of people uh who are
[2449.76 → 2457.78] developing rails apps need to process things asynchronously and I've tried to add as many
[2457.78 → 2466.18] features and bits of functionality to sidekick to make it extremely useful while also maintaining its
[2466.18 → 2475.28] as simple as possible to get started and also keep it high performance gotcha, so there's uh
[2475.28 → 2483.64] sidekick really solves a problem of how do I make my application something that is asynchronous
[2483.64 → 2490.28] friendly and and and highly performant so it's the size of the problem and the size of the know
[2490.28 → 2496.16] potential audience that's creating the popularity and that makes sense I think so I think
[2496.16 → 2505.34] yeah what about girl Friday and how I guess this is it kind of built on top of sidekick or what
[2505.34 → 2513.36] is girl Friday and how is it different so my the last couple of years of my ruby open source have
[2513.36 → 2518.36] kind of been focused on scalability and performance and certainly geocached as part of that my work with
[2518.36 → 2524.20] teacake client and dolly but another problem that I was solving over and over and over at all the ruby
[2524.20 → 2528.74] companies that I was working for was how do you do background work how do you do asynchronous processing
[2528.74 → 2536.20] efficiently because I wrote a system for a company called five runs that I worked for six or seven years
[2536.20 → 2543.76] ago and this background processing thing was called Bert, and it was called Bert because it was a q
[2543.76 → 2550.10] that was in the database and guess what it was basically like delayed job except before delayed job
[2550.10 → 2557.52] came out and so when I moved to my next company after five runs I wrote this thing called jobber
[2557.52 → 2565.34] and it was a background processing worker that pulled jobs um I forget where it pulled them out of if it
[2565.34 → 2570.62] pulled them out of the database or what but as you can see there's a trend here is every company I've
[2570.62 → 2577.68] been going to I've been working on these asynchronous processing systems, and they've always sort of been less
[2577.68 → 2586.52] less than uh what I needed to build in the long run in the case of Bert jobber the database is not
[2586.52 → 2591.10] the right place to put uh the q, and they were single threaded so they weren't terribly efficient
[2591.10 → 2599.24] um and so when I went to carbon five and worked with this client that had the rescue problem I saw
[2599.24 → 2603.88] I'm solving the same problem over and over and over and so that's sort of where sidekick came from
[2603.88 → 2614.10] girl Friday was sort of a different stab at solving the same problem the girl Friday runs inside your
[2614.10 → 2623.26] rails process so it uses threads also but instead of being a separate process that uses Regis as sort
[2623.26 → 2629.84] of a data exchange between the processes girl Friday was literally a set of threads running within your
[2629.84 → 2635.36] rails process and your rails code could just hand jobs to those worker threads, and it would process
[2635.36 → 2642.92] them in the background ultimately there were some implementation details that I got wrong in girl
[2642.92 → 2651.14] Friday that made it a little more painful to maintain than I really wanted and also I realized that
[2651.14 → 2657.84] keeping the worker threads in the rails process wasn't necessarily the right solution
[2657.84 → 2667.56] so that's when i sort of focused took my focus away from girl Friday and started focusing on a new
[2667.56 → 2675.00] project that is sidekick gotcha so I don't want to I want to bring this up and I don't want it to
[2675.00 → 2680.16] seem awkward or anything, but we had a little back and forth on uh twitter a while ago when I mentioned
[2680.16 → 2685.08] something about the tone and some of the responses to the pull request can be kind of aggressive
[2685.08 → 2689.88] and you actually responded to me well I didn't actually even mention you, but you responded to
[2689.88 → 2693.92] it and said it was a definite weakness of yours, and you've tried to be better about that
[2693.92 → 2700.62] over the last few months uh did you experience flack from the community and how did you respond to that
[2700.62 → 2708.88] and how do you feel like you've kind of grown from that yeah it's its something that I struggle
[2708.88 → 2714.16] with and I see other people struggle with and certainly the internet is something that can turn into a flame
[2714.16 → 2721.16] fest at the drop of a hat um you know people need to realize and and and I'm one of those people
[2721.16 → 2727.80] that people have a bad day some people are in completely different mindsets and don't see
[2727.80 → 2734.56] your viewpoint and so that's something I struggle with um I try to provide really quick support and try
[2734.56 → 2739.34] to respond quickly to people's support issues, but sometimes that means that I might give a glib answer
[2739.34 → 2746.12] or make a joke that is perhaps you know of tone for really um isn't as professional as I should
[2746.12 → 2751.68] be so that's something I struggle with and I think a lot of open source people struggle with that
[2751.68 → 2755.82] you know we're we're logical people, and so we think our words are going to be taken logically
[2755.82 → 2763.34] and and and oftentimes readers take things emotionally instead so um that's something that I've tried to
[2763.34 → 2769.36] to tone down and just try to stay as professional as possible when I'm when I'm helping
[2769.36 → 2777.08] people in issues um but yeah for sure there's been times when I've um you know let loose a response that
[2777.08 → 2783.46] you know i I wished I could have taken back 30 seconds later yeah I think the most important
[2783.46 → 2791.14] thing I think that everyone can say you know everyone can say you know things that they don't mean or that
[2791.14 → 2795.00] aren't the nicest things or aren't the most professional things to say but I think the most
[2795.00 → 2799.08] important thing is the ability to you know self-evaluate and determine if you need to adjust
[2799.08 → 2803.50] that and I think that's something I respected that you said to me when you said that that was a
[2803.50 → 2808.56] weakness and something you're trying to be better about I think the ability to see uh you know critically
[2808.56 → 2815.44] at yourself is a very good thing so I applaud you for that yeah, thanks you really have to know
[2815.44 → 2821.02] where your strengths and weaknesses are and my strength is code and so that's what I tend to focus
[2821.02 → 2827.48] on and part of managing an open source project is dealing with people and interacting with
[2827.48 → 2834.20] people and helping your customers and helping your users and that's something that uh you know I'm
[2834.20 → 2842.00] I'm just not an I'm not a community support person necessarily um by a profession or by um
[2842.00 → 2849.56] um by skill set I guess so um i I hope the community bears with me and tries to take
[2849.56 → 2856.46] what I say not necessarily personally, or maybe you know forgives me um a little bit if something
[2856.46 → 2861.32] seems off kilter it certainly is not do you think that uh these types of situations though might
[2861.32 → 2866.30] uh suppress some people from releasing certain things to the open source community because of
[2866.30 → 2870.50] it's kind of like you know for designers they have dribbled you know show and tell there and
[2870.50 → 2875.74] you know for developers and hackers like us, it's you know GitHub is that playground for us
[2875.74 → 2880.78] where we release our code there we want to share we want to improve you think it helps you or makes
[2880.78 → 2887.16] you want to suppress some things or others maybe i I definitely think that that's a factor um I mean i
[2887.16 → 2893.30] I've talked to a lot of people over the years who when I say um you know you should blog more
[2893.30 → 2899.72] because blogging it helps you write it helps you collect your ideas helps you think and a lot of
[2899.72 → 2903.70] people tell me well I don't know what I'd say or I don't know how to you know I don't really have
[2903.70 → 2911.18] an opinion that I think people would value um and for sure I think a lot of younger developers who
[2911.18 → 2916.96] might hold me or somebody else in esteem they're going to be really worried about how the community
[2916.96 → 2925.50] and their heroes might perceive them um so yeah i think a lot of open source people
[2925.50 → 2931.78] are a little hard thick-skinned shall we say and um and a lot of people with thinner skin
[2931.78 → 2937.60] they don't have the i yeah they I wish they had the courage to stand up and just try it
[2937.60 → 2943.00] um but yeah sometimes the community can be a little rough you know look at you know hacker news
[2943.00 → 2948.10] you post an open source project that you want to show off to the community and
[2948.10 → 2955.58] 50 will be positive but that 50 that are negative is rough yeah don't read the comments yeah those
[2955.58 → 2958.64] the one you know those are the ones you're going to remember at the end of the day you're not going
[2958.64 → 2962.82] to remember the good ones you're going to remember the bad ones and that's unfortunate, but that's a
[2962.82 → 2969.46] part of life um I wish it wasn't the case and I've said some stuff before you know uh
[2969.46 → 2976.20] Mitchell Hashimoto of vagrant fame uh i unwittingly uh said something negative about
[2976.20 → 2981.90] some open source project he put out years ago and he reminded me of it and my jaw dropped
[2981.90 → 2989.64] and I couldn't be prouder that he moved on past my negativity and went on to do you know
[2989.64 → 2996.62] awesome stuff um, and it just shows you that you know I try to be positive, but you sometimes know
[2996.62 → 3002.06] people are jerks, and we're all human man you know we are all human and in the digital world
[3002.06 → 3006.88] when you put words out there you're right I mean because I can read your joke and I'm like was he
[3006.88 → 3014.04] just talking crap about me or was that a joke and uh like Andrew at pure charity he's the jokester so
[3014.04 → 3020.16] you're never really sure how to take in but um you know, and it's the case, and it's kind of a bummer but
[3020.16 → 3027.06] I think what one thing you said that rings true for me is just reminded people that you know it's
[3027.06 → 3031.48] like the clerk when you go to get a pack of gum or something like that you're not sure if not saying
[3031.48 → 3035.00] hello to them is going to give them a crappy day, and they're going to be a jerk to their wife or to
[3035.00 → 3038.62] their girlfriend or to their mother you know you got to be nice to everybody, and sometimes you're
[3038.62 → 3043.66] just not sure what type of day somebody's in, and you may be in the perfect day, and they're in
[3043.66 → 3050.78] you know just a bad place you know you never know right so one of the things that we encourage
[3050.78 → 3055.46] people to do we obviously have the changelog we love open source, and we try to encourage people to
[3055.46 → 3061.32] to contribute but you your right people are a lot of times hesitant to you know start a whole project
[3061.32 → 3065.92] and contribute all the source code to open you know to GitHub or whatever so that everyone can see it and
[3065.92 → 3072.78] critique it so what we try and do is encourage people to you know jump into other projects and you
[3072.78 → 3078.24] know submit pull requests um so on that note do you have any call to arms that uh you would like
[3078.24 → 3082.86] the community to kind of get involved with sidekick to maybe some features or something you would like
[3082.86 → 3093.02] to see um anytime people ask me that i kind of i kind of tell them uh if I think of a feature I'm
[3093.02 → 3098.38] gonna I'm the type of guy that's just going to go that night and start to implement it um what I'd love
[3098.38 → 3105.92] to see and what I've tried to provide in sidekick is a framework and APIs for building um asynchronous
[3105.92 → 3111.90] processing and I just want to see what people can do with it because oftentimes the coolest stuff that
[3111.90 → 3116.84] people come up with is stuff that i just never would have thought of in a million years and so
[3116.84 → 3124.78] I've seen 10 or 20 gems built on top of sidekick at this point and i just I love to hear stories about
[3124.78 → 3131.62] what people have built on top of sidekick I've I've got at rails comp this year I talked to a handful of
[3131.62 → 3139.10] of sidekick users that were processing over a billion jobs a month with sidekick which I think is awesome
[3139.10 → 3145.98] um, and so I just love to hear those sorts of stories and love to see kind of what cool
[3145.98 → 3153.34] things people have built on it so I don't I don't have any brilliant ideas for people to to to add to
[3153.34 → 3159.12] sidekick but I'd love to see what you could do with it so just be creative as you find a need solve it
[3159.12 → 3164.98] and yeah and blog about it and let me know about it, I'd love to I'd love to give you publicity
[3164.98 → 3171.60] um about the cool things that you're building on that note if you don't mind me asking Andrew I'm
[3171.60 → 3174.66] curious mike what you thought about Kelly's post on the changelog about sidekick
[3174.66 → 3182.48] uh remind me again it was uh it was something about like the three or four yeah he says earn a
[3182.48 → 3186.94] sidekick black belt by breaking a few boards and his very first point was sidekick is too darn fast
[3186.94 → 3192.04] um yeah that's that's that's a great compliment
[3192.04 → 3201.20] um yeah you actually uh straightened out some confusion we had on manually retrying failed
[3201.20 → 3206.06] jobs um was that I guess this is you know was that something that has always been there in the
[3206.06 → 3212.34] failed job in the retry queue yeah in fact that's that's one of the confusions that i sort of have
[3212.34 → 3220.18] in how people use sidekick is I'm not sure if people just don't read the documentation or what but I've got
[3220.18 → 3226.18] a wiki with tons of documentation that goes through each of the big major features that psychic has and how
[3226.18 → 3235.20] to use it and people have wanted to turn off retries they've they've built gems that um add different
[3235.20 → 3243.84] types of failure handling and i just I don't necessarily understand um why they're trying to
[3243.84 → 3250.02] do that I think of the retry mechanism as awesome as designed and that's I use it myself everywhere
[3250.02 → 3255.76] so I'm not sure where they're coming from so I don't know if it's just a matter of they didn't
[3255.76 → 3262.86] read about sidekick's own built-in retry mechanism or if they have some sort of functional need to
[3262.86 → 3268.20] where they can't retry, or they need to do retries manually or something like that but yeah that was
[3268.20 → 3273.34] that was one of the confusing points i had about that blog post is sidekick's retry mechanism is awesome
[3273.34 → 3279.78] and built-in and just, and it works by default so I wasn't clear why that point needed to be made at
[3279.78 → 3286.34] all yeah I don't know I mean I remember when we started using it um there was it was the idea
[3286.34 → 3292.46] that we couldn't find failed jobs and I don't know maybe we're just um I'm not sure why it
[3292.46 → 3300.52] happened but uh maybe it may have arisen from once they if we weren't utilizing that um retries exhausted
[3300.52 → 3305.06] callback they were gone you know who knows now it's been a while but Kelly's probably in the back
[3305.06 → 3311.88] back channel too just like no this is why you know well the sidekick uh retry queue is fully
[3311.88 → 3317.40] visible in the web UI so if you have the web UI hooked up, and you want to see failed jobs just
[3317.40 → 3323.48] click on the retries tab, and it's, and it's all fully listed right there right, and you can run
[3323.48 → 3330.12] individual retries um manually like right now you can say if you fix a bug that caused a retry a job to
[3330.12 → 3337.92] fail you can deploy that code and then go into the retry retries tab and click on the job and just run
[3337.92 → 3343.26] it immediately, or you can wait for the exponential back off to sort of just naturally rerun the job
[3343.26 → 3348.38] right what about a programmer hero programming hero do you have one
[3348.38 → 3360.06] oh who do I have um tony Archer obviously is fundamental to sidekick success he know he's the
[3360.06 → 3369.66] the founder and project lead for the celluloid project, and he's done an amazing job of really
[3369.66 → 3378.36] improving ruby's concurrency story and sidekick is heavily multithreaded but um doesn't
[3378.36 → 3384.00] half it doesn't the code base really doesn't contain any mutates at all and I am a much better
[3384.00 → 3389.76] person for that um when you build an application a multithreaded application with
[3389.76 → 3396.82] celluloid you just don't need to use mutates and by virtue of not having to do locks your
[3396.82 → 3404.12] multithreaded code becomes much easier to reason about and much easier to write and maintain so he's
[3404.12 → 3412.54] he's my hero and celluloid has certainly been um critical to sidekick success um some other
[3412.54 → 3421.32] guy guys that and or girls that might be my heroes um Jeremy cheaper I think is an awesome um you know
[3421.32 → 3427.34] he's been doing rails core Ruby on Rails maintenance for years now and every time I meet that guy he's
[3427.34 → 3432.70] just incredibly knowledgeable about everything and yet he just sort of programs in the background and
[3432.70 → 3440.06] keeps a pretty low profile but uh i I wish I could be as knowledgeable as uh as him about ruby in
[3440.06 → 3447.44] general yeah it's uh I was taking a back a little bit by your some of your background too I didn't
[3447.44 → 3453.08] realize that in addition to being a ruby as you're also a motorcycle racer that's not something often
[3453.08 → 3461.04] you find on somebody's bio um yeah i I have an I have a sport bike and uh I live about five miles away
[3461.04 → 3467.20] from a racetrack here in Portland so i I take my uh my bike to the racetrack about once a month
[3467.20 → 3474.98] generally and I do what's called track days so basically pay the money pay some
[3474.98 → 3482.16] money to uh go around the track as fast as I want all day wow man so like literally all day uh yeah they
[3482.16 → 3491.08] they basically you're you're broken into three groups uh fast medium and slow, and you decide which
[3491.08 → 3495.66] group you go into, and then you get 20 minutes an hour, and then they just rotate every hour and they
[3495.66 → 3502.24] do that for eight hours a day that's going to be pretty wild yeah it's its a lot of fun i I hit 170
[3502.24 → 3509.38] um down the front straight away last time I was there and nearly saw my life flash before my eyes
[3509.38 → 3515.58] wow so not only is your cycle fast your psychic is fast as well are your cycle is fast as well
[3515.58 → 3521.26] exactly yeah that's um it's its really great having you on the show like thank you so much for taking
[3521.26 → 3526.52] time out of your day to join us I mean it's its really been great for me to hear a lot of this
[3526.52 → 3531.06] and for the listeners listening out there that want to use sidekick or like what is that sidekick
[3531.06 → 3535.00] thing again you know I heard change all the say it's really fast but I'm not really sure about it so
[3535.00 → 3541.08] really awesome for you to come on the show and schooling us on sidekick and uh message queuing
[3541.08 → 3548.14] but uh for those of you listening follow mike on GitHub and twitter he's m parameter this is show number 92
[3548.14 → 3554.60] you can find show notes at changelog or sorry the uh at 5x5.tv slash changelog slash 92
[3554.60 → 3560.12] hold off my game today I'm not really sure why but uh let's close this show out say goodbye
[3560.12 → 3563.00] see you later thanks so much mike thanks guys
