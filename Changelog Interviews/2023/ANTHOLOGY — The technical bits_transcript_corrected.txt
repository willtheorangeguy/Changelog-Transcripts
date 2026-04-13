[0.00 → 19.52] this week on the change law we're going back to the hallway track of all things open 2023
[19.52 → 25.40] in Raleigh North Carolina today's episode features high key Lena Vegas co-founder of neon
[25.40 → 32.40] and Postgres hacker talking about well Postgres and of course neon little side note here because
[32.40 → 37.96] neon is actually one of the sponsors of this podcast we met neon at all things open and we
[37.96 → 42.38] pursued them we wanted to use their stuff, and we asked them hey would you be interested in sponsoring
[42.38 → 47.58] us, and they said yes, and it just so happens they're sponsoring this episode this is not intentional
[47.58 → 53.82] just so you know up second is Robert alkali bioinformatics software engineer who's working
[53.82 → 61.70] on bringing desktop applications to the web with Wasm and last up is m Scott ford on the state
[61.70 → 66.32] of fixing bugs and what's been going on with this software consultancy called corgi bites
[66.32 → 73.32] of course a big thank you to our friends and our partners at fast and fly this podcast got to you
[73.32 → 80.18] fast because quickly they are superfast globally check them out at fastly.com and our good friends
[80.18 → 86.08] at fly will help you put your app and your database in 30 plus regions on six continents with no ops
[86.08 → 88.52] check them out at fly.io
[88.52 → 104.50] what's up friends this episode is brought to you by our friends at neon on demand scalability
[104.50 → 111.62] bottomless storage and database branching and I'm here with Nikita shaman co-founder and CEO of neon
[111.62 → 119.32] so Nikita imagine you are a tour guide give me a tour to the world of neon so let's look at a modern
[119.32 → 125.78] developer as people say never bet against JavaScript so more than 50 probability this person is writing
[125.78 → 133.38] JavaScript and typescript using react Next.js deploying their code on a platform like Purcell
[133.38 → 141.92] and really care about design so working with Figma working with a local designer or maybe starting to
[141.92 → 149.10] work with an AI designer and using technology like Purcell just shipped called v0 and then like you got to
[149.10 → 154.90] store data somewhere so you go to neon or use Purcell Postgres which is powered by neon you push a
[154.90 → 162.10] button, and now you're able to write and read from neon and then that kind of just works out of the box
[162.10 → 168.70] the majority of your time you spend crafting your application crafting the front end and then the
[168.70 → 173.80] database is just kind of like it's kind of there and just kind of works, and you don't think too much
[173.80 → 180.64] about it and when you run previews when you run next versions of your software you can send your
[180.64 → 186.42] collaborators your other engineers on your team or your product managers or designers a version of
[186.42 → 191.00] your app the version of the future that you want to debate if you want to comment on, and it's fully
[191.00 → 197.64] sandbox you know from your front end to back end to the database that's like a good part of this world
[197.64 → 203.38] the world is obviously much bigger than just building front end apps there's also back end apps there are
[203.38 → 209.26] python apps there are java apps and all of those things we're perfecting the world for the world that i
[209.26 → 214.94] just described, and we think that the rest of the world will follow uh and the rest of the world is
[214.94 → 223.60] java apps last apps back end apps queues scheduling AWS lambda Kubernetes containers again the tech world
[223.60 → 231.52] of the back end is just enormous but I think perfecting this first world that I described will create a
[231.52 → 236.44] standard in developer experience that the rest of the developer world will just follow so you have
[236.44 → 242.32] oversell Postgres powered by neon you've got neon as an integration to oversell you've got neon out there
[242.32 → 247.72] at neon.tech as self-serve where anybody could just go and sign up and start up right now you're optimizing
[247.72 → 252.66] for this new standard but what's the response been like what's the community saying what's the community's
[252.66 → 260.04] response we are lately onboarding close to 2500 databases a day that's more than one database a
[260.04 → 265.94] minute of somebody in the world coming to neon either directly or through the help of our partners
[265.94 → 272.02] and they're able to experience what it feels like to program against database that looks like a URL and
[272.02 → 277.38] program against database that can support branching and be like a good buddy for you in the
[277.38 → 283.52] software development life cycle so that's exciting and while that's that's exciting the urgency at neon
[283.52 → 288.76] is currently is unparalleled there you go if you want to experience the future go to neon.tech
[288.76 → 294.54] on demand scalability bottomless storage database branching everything you want for the Postgres of the
[294.54 → 297.54] future once again neon.tech
[297.54 → 301.54] so
[301.54 → 306.54] so
[306.54 → 310.54] so
[310.54 → 314.54] so
[314.54 → 316.54] so
[316.54 → 320.54] so
[320.54 → 338.42] let's begin the beginning Postgres yes Postgres 1986 something like that wasn't it forever
[338.42 → 344.62] I mean this released from Berkeley university in 1995 okay I'm not sure how long it was developing the
[344.62 → 349.54] university before that several years I read there are roots back into the 80s but I could be wrong it could be
[349.54 → 356.54] either way that's ancient history right that's a long time ago and yet it's the darling of
[356.54 → 362.54] most developers today Postgres it's become popular like you know when I started to hack on Postgres it
[362.54 → 367.54] was not the case like it was not the most popular one it was not the darling so you would actually have
[367.54 → 373.54] to explain I'm not sure what happened I think post is just matured um, so people used to ask
[373.54 → 377.54] like why Postgres and why not my sequel or something else right but I don't really hear that anymore like
[377.54 → 378.54] it's the default no
[378.54 → 380.54] do you think it could be
[380.54 → 386.54] I think it's a really somewhat technical and then also somewhat drama related like there's been a lot of drama in the
[386.54 → 387.54] sequel space hasn't there
[387.54 → 389.54] like with licensing and
[389.54 → 390.54] yeah
[390.54 → 391.54] yeah
[391.54 → 395.54] shifting like just drama behind the scenes to sort of like make it not very community friendly
[395.54 → 396.54] yeah
[396.54 → 400.54] I mean Postgres is also good very technically you know very good technically but like I wonder if that's also
[400.54 → 402.54] a reason to be like don't go there
[402.54 → 407.54] I'm sure it's a factor Postgres has always had a slightly different community than many other open source projects
[407.54 → 419.54] like it's a truly community driven and not, not like owned by any single company yeah so that's different I think that has helped to keep it alive for a long time so you can't acquire Postgres
[419.54 → 436.54] that being said that community is aging I'm not sure if you may have seen jams governor's recent post on Redmond about the aging Postgres community and how do we actually transition like where do we go from there yeah and there's always new people coming, but it's right I mean the core people who have been
[436.54 → 440.54] who have been added for a long time are definitely aging none of us is getting any younger
[440.54 → 442.54] all right can you summarize some of that jarred
[442.54 → 446.54] well just if you look at the core contributors to Postgres
[446.54 → 449.54] generally speaking they're men in their 50s
[449.54 → 453.54] they're at the know in the fourth quarter of their careers at least
[453.54 → 457.54] maybe they would argue that, but you know they're not in the kickoff stage of a career
[457.54 → 458.54] or halftime
[458.54 → 466.52] or halftime I would argue fourth quarter maybe they say third quarter regardless they're getting on the older age of the spectrum and then like what happens to the
[466.52 → 496.50] project as those very key players retire right move on lose interest it's not dominated by any one person though so there 's's a lot of people working on it and if you look at the wider ecosystem like there's a lot of extensions and there's a lot of stuff happening around Postgres and there's young people there yeah, so there's a lot of potential if we can draw them into to become more active on Postgres itself well neon I mean you and your team I'm not sure your age, but there's fresh we'll call it fresh blood in
[496.50 → 526.50] the ecosystem like here's a brand-new startup yeah relatively couple years old contributing building extension for sure etc for sure that's a and putting my community had on like that's one run reason why I'm excited to work for neon I hope I can actually make a difference on that and bring some new blood to the community as well through the company so you're Postgres guy before neon i I've been a Postgres guy since 2006 I've been working full-time on Postgres okay long different companies
[526.50 → 556.50] what was your criteria for choosing for Postgres well I've never really used Postgres so my background is that I was working on a systems integrator and uh I had some free time on my ad so I've always been a programmer I've always been doing stuff and I'm a big fan of the relational model once I got introduced to SQL and that so I had some free time I was on paternity leave with my daughter, and she was a good sleeper uh so i I was looking around for projects to contribute to or if there was something in the open source world
[556.50 → 586.50] I looked at my book and I looked at my book and I looked at my book and I looked at my book and I looked at databases I looked at my SQL code I looked at Postgres I think I looked at some others, but Postgres was the one that was like easy to read and easy to do it was a pleasure to kind of read through and understand and learn more so I stuck with that one thing we heard yesterday from uh all things open attendee yeah is that back in June of this year I believe on the Postgres mailing list you proposed or maybe not proposed but brought up something that's probably been stirring
[586.50 → 616.48] a significant change to Postgres if it lands or if it happens in a long time you want to tell us about that you must be talking about the multi-treading changing to multi-traded architecture yes so yeah that was uh that that came up in conversation in pgcon at the end of May uh with some other hackers like we were talking about some features and uh like wouldn't it be easier if we had a multi-traded architecture so what i ended up i kind of summarized the discussions, and it seems like there's a rough consensus that if we had
[616.50 → 646.38] like multi-traded architecture would be better at this point, but there's a lot of history of course like multi-pro it's not it's not easy to change to go from multi-process architecture to multithreaded so that might be the thing can you explain the foundational difference between multi-process and multithreaded right so the key difference between multi-process and multithreaded architecture is that when a new connection comes in uh Postgres launches a new process to handle that connection um in a multithreaded architecture you would only launch a new thread and the difference between a process and
[646.38 → 676.32] uh the thread is basically that threads all share the same address space uh in the process uh whereas with processes each process has its own address space and that makes a difference in what you can how easily you can share data or share uh data structures between the connections uh, so multithreaded architecture would make it a lot easier to resize uh things like uh buffer cache uh a lot of other caches that are currently not shared across the connections in Postgres uh that
[676.32 → 706.16] would that would make it easier to share them right does that change the CPU utilization as well it might yeah I mean like if I looked at top but I just see like when Postgres is being pinged just like one line or like if I had eight cores all eight cores lit up yeah so multi-threading wouldn't directly do that like just by switching to multithreaded we wouldn't get that uh Postgres can already multi-utilize multiple cores okay uh by launching multiple processes to process one query right uh, but that was actually when that that parallel query was implemented a few years ago that was
[706.16 → 736.00] actually a lot of effort went into working around the fact that we don't we's a multi-process architecture so we actually have to build a lot of infrastructure to share the data between the processes which would be a lot simpler in multithreaded architecture but uh so I think we could probably do more uh like it would probably speed up the development of multi like parallel query as well, although you know that would be separate projects to do that that's another mailing list post yeah, so multithreaded software has specific requirements
[736.00 → 763.52] in order for it to be thread safe right yeah sure that used to be a problem back in you know 20 years ago when this was probably the first time discussed uh I think if you look at back at the 95 or 96 discussions and I think I've seen some comments saying well Postgres is multi-processed now, but maybe we'll switch to multithreaded later and that was like 25 years ago right uh what was the question well I didn't quite get there but here it is that
[763.52 → 769.64] if you were assuming multi-processed for all these years these 25 years right and not thinking multithreaded I imagine
[769.64 → 777.10] it's not an insignificant change to the software oh sure yeah oh right so thread safety uh that used to be a big deal
[777.10 → 783.68] a long time ago uh but nowadays libraries I mean most software when people is people are writing software now they
[783.68 → 788.14] would start with the multi-thread architecture so that's not really a problem anymore like all the libraries are
[788.14 → 817.26] multithreaded or multi-thread safe there are thread safe versions of everything uh so that was a good argument or would have been a problem 20 years ago not really a problem not really a problem now what are they of course switching you know yeah the existing code uh need to be adapted somehow yeah exactly so that is a problem that's a that's a long problem and that's the whole that's the hard part of all of this really uh changing Postgres itself but also the whole ecosystem to be thread safe most of it probably already would be but how do you know like how do you tell exactly
[817.26 → 828.60] so so so that's going to be the hard part in this to figure out how do you detect the cases where it's where something is not thread safe I mean it seems like this feature is an excellent case study
[828.60 → 847.20] in how a large change to an open source multi organization teamed core team you know introduces an idea agrees on the idea like the governance involved and then the actual work who does it how does it get divvied out and then how
[847.20 → 876.92] does it actually land and transition isn't that a yeah we're really complicated beast yes it is and how does it work we'll see how it ends up uh Postgres doesn't have like a very there's no voting system there's no though uh it is actually hard to even make decisions like that because it's not well-defined how would you do that the rough idea is that you try to find consensus and uh if someone very strongly disagrees then you know then we work through those disagreements uh
[876.92 → 886.18] but yeah it can be hard to pull off big changes like that so but at the end of the day like what really first thing that needs to happen is someone actually needs to do all the work to show
[886.18 → 891.46] I was going to say what's the thing you got the idea out there is any code is are you asking for
[891.46 → 899.26] consensus and then the work well what's the stage of this idea is it just it's just an idea at the moment like I've spent a few
[899.26 → 906.16] hours days maybe thinking about it and uh writing some very preliminary stuff that you know some small
[906.16 → 910.98] changes that we should make anyway just to clean up the code uh but no there's no there's no real concerted
[910.98 → 915.92] effort yet yeah that's going to be a lot of work I mean the first thing to do is to well and what I wanted to
[915.92 → 922.84] do with the uh posting in June was to make sure that I'm not missing some you know uh that i actually
[922.84 → 926.42] understood the right that there is consensus that this would be a good thing if we had it
[926.42 → 931.14] uh and that there is no strong objections from any of the core people on that
[931.14 → 936.16] uh you know otherwise it would be pointless to spend any time on it yeah uh but the next step
[936.16 → 940.92] really needs to be to actually start to write some code to do that uh I don't know if I'm going to do
[940.92 → 946.56] that maybe or maybe I'll have to do it together with the team sure um, but we'll see is that something
[946.56 → 951.16] that would be beneficial for neon I imagine it would be it would be and then neon would be willing to
[951.16 → 956.32] fund the development of yeah I think we yeah so yeah it would benefit neon because
[956.32 → 962.00] we do all the scaling uh and uh that becomes easier if in a multi-traded architecture because
[962.00 → 967.36] that makes it easier to resize some of the uh buffer cash it makes it easier to share some of
[967.36 → 970.64] those cases kind of the same problems that everyone has liked it would benefit everyone
[970.64 → 976.64] uh but yeah for neon that that would really help with the other scaling part gotcha when we had Nikita
[976.64 → 982.74] on the show probably 18 months ago roughly exactly this time last year oh was it I think a year ago
[982.74 → 990.38] he mentioned three or four patches that neon adds to Postgres to customize for your guy's needs and
[990.38 → 994.46] how they were trying to upstream those he wasn't sure if that was ever going to happen, but he thought
[994.46 → 1000.16] you know good chance but takes time etc any update on upstream contributions from your team yeah so
[1000.16 → 1006.08] those patches are still out there not much has happened unfortunately uh the biggest patch we have
[1006.08 → 1010.72] is to do what's called the storage manager API in Postgres which isn't really an API because there
[1010.72 → 1016.88] hasn't really been any other implementations in the past 20 years uh so that patch is still out
[1016.88 → 1021.74] there to make that more pluggable, but there has been no progress so it's with the Postgres community and
[1021.74 → 1025.52] I'm sure other communities have the same problem it's hard to sometimes get attention to these things
[1025.52 → 1030.58] if you know is no one else is really feeling the pain there 's isn't much happening uh although
[1030.58 → 1035.16] on that there have been a lot of good discussions like there are and some other ideas people could do with
[1035.16 → 1041.94] those patches and those uh those APIs uh but yeah nothing has been committed yet the patches are
[1041.94 → 1046.56] essentially the way it writes to disk instead of writing to the disk it writes distributed yeah so
[1046.56 → 1051.16] neon plugs in at a really low level so whenever Postgres would read a page an eight kilobyte page from
[1051.16 → 1057.84] disk uh like we hook in at that point so you read it from elsewhere like from our storage system uh so
[1057.84 → 1063.40] yeah making that having an extension point there in Postgres would help to eliminate those patches that sounds
[1063.40 → 1067.80] like your competitive advantage though neon's competitive advantage like couldn't if that patch
[1067.80 → 1073.02] goes into open source does that become a threat well it's already out there open source anyone can
[1073.02 → 1079.32] already use it uh so that's true and neon you know lives and dies with Postgres hood right okay about
[1079.32 → 1083.96] the community that's what I was trying to get to like if this can be used by the enemy let's just say
[1083.96 → 1088.18] is that a bad thing you know I made peace with that thought a long time ago when I started to work on
[1088.18 → 1092.82] Postgres like it is a liberal license people can take and then yeah do whatever they like with it
[1092.82 → 1097.70] uh I think it speaks to the company though it speaks to the DNA and the outlook of the company which is
[1097.70 → 1105.54] why I asked that it's like yeah sure do people see neon as a player a safe player I don't know a nice
[1105.54 → 1111.22] player in the Postgres world or are you trying to build a proprietary mode I sure hope people see us
[1111.22 → 1115.54] friendly okay that's a better word friendly we want to partner with everyone, and we like to make
[1115.54 → 1122.26] friends right so you're waiting on those particular patches who know Postgres has a project you know
[1122.26 → 1127.62] you say you live and die with it is seems like through its history has had times when it's quote
[1127.62 → 1134.18] unquote fallen behind with features and other people pop up and say you know look at these no
[1134.18 → 1138.66] sequel for instance look at look what we can do with Jason right and then eventually Postgres was like well
[1138.66 → 1144.98] we added all the Jason things, and now we can also do that what's next in that line like what are you
[1144.98 → 1148.90] seeing out there or maybe what you guys are building where it's like Postgres can't do that but people
[1148.90 → 1157.30] are doing it, and now it's going to have to catch up at some point um that's a good question I mean putting
[1157.30 → 1161.46] my knee on how to all those the storage related stuff that we are doing separation of compute and storage
[1162.26 → 1167.54] although that is out there in the open source, so people could take up and run with it, I don't know if
[1167.54 → 1173.22] that will fully take over the world or if that will stay to be uh something that we do we'll see
[1173.22 → 1178.18] I mean, but there are competitors doing similar architectures as well uh then there's all of
[1178.18 → 1183.38] exciting stuff happening with pg vector for example rector service everyone that's a hot topic uh but
[1183.38 → 1187.54] I think that is like I think Postgres is actually doing pretty well there yeah like the pg vector is
[1187.54 → 1194.18] popular, and it will, it keeps you know keeps uh improving at its own pace and that's that's all good
[1194.18 → 1199.62] a similar thing that's with post GIS like Postgres is pretty dominant in the GIS world with that yeah
[1199.62 → 1206.58] good point are those things that when using neon are those things that are like pre-integrated for
[1206.58 → 1213.22] you as a user of neon database or is it like click a box get pg vector how does it work with plugins and
[1213.22 → 1218.98] yeah we just we yeah we provide those extensions you just do create extension, and you get it so you
[1218.98 → 1225.14] just have fulled you have full Postgres access, and you're just doing your thing huh yep okay so geo
[1225.14 → 1231.62] distributed Postgres around the world let's talk about that okay can you do that no we don't do that
[1231.62 → 1236.34] at the moment okay we've been thinking of that we have a lot of good ideas I know you do I remember
[1236.34 → 1241.22] asking about that as well I'd love to hear from your mind what are some ideas around this
[1241.70 → 1247.14] uh so what you could do uh first you can write run read only replicas in different regions
[1247.14 → 1252.82] uh that's the kind of the first step easy step uh with neon we could also run the storage in
[1252.82 → 1258.66] different regions and do the kind of the replication at the lower level okay uh we have no plans for
[1258.66 → 1263.86] multi-master or multiple rider uh systems there are other projects trying to do that, but that's
[1263.86 → 1268.10] always a hard problem and it yeah it introduces a whole new set of problems so we're not going there
[1268.10 → 1274.10] at the moment yeah you have to kind of break the cap theorem to do that people are claiming
[1274.10 → 1278.42] it's possible is there a real demand for that or is it just something that people like me like to
[1278.42 → 1284.98] talk about and ask about i I don't know I haven't really seen very we don't hear a lot of people
[1284.98 → 1290.02] requesting that let's put it that way okay uh people talk about it people you know people ask about it
[1290.02 → 1294.50] but not in a serious way like I don't think we've lost any customers because we don't have it
[1296.10 → 1301.22] given neon today what is the current architecture if you're not geo you know distributed what is the
[1301.22 → 1305.86] architecture when you deploy neon what is the benefits of using it why do people choose neon for
[1306.50 → 1309.54] you know you don't write the dish you write to distribute how does that actually play out what's
[1309.54 → 1314.90] the architecture so the core of the architecture is the separation of compute and storage and then
[1314.90 → 1320.34] we have a control plan that kind of manages those Postgres instances in VMS and there's a proxy there's
[1320.34 → 1327.30] some moving pieces but the so the big differentiator that you get with that architecture is uh it's serverless
[1327.30 → 1331.62] so what we mean by that is that we actually shut down Postgres if you're not using it so that's
[1331.62 → 1336.02] perfect if you're a developer and you don't need to worry about you know forgetting to shut it
[1336.02 → 1342.66] down uh in a nutshell the other thing that the storage system can do is the branching and it uh, uh
[1343.30 → 1348.18] it kind of replaces traditional backups and while archive so you can do point in time query you can
[1348.18 → 1354.18] easily spin up a new Postgres instance against an older point in time start running queries against that
[1354.18 → 1358.18] uh stuff like that the branching is something that is kind of unique, and we hear a lot of good
[1358.18 → 1363.22] things about that people like that if you're is you're a developer you want to create the branch
[1363.22 → 1369.06] of your development database or even your production database uh and do your changes run your PR
[1369.06 → 1375.22] against that uh and when you're done you can forget about it, or you can refresh that right you
[1375.22 → 1381.46] said storage system is that like a different term that sits above the database, so neon is the storage
[1381.46 → 1385.30] system and then there's the database like give me an idea what you mean when you say storage system
[1385.30 → 1392.58] so we wrote a completely new like server software that runs below Postgres and that's it deals with
[1392.58 → 1397.46] those eight kilobyte pages, and it understands the Postgres writer head log format the transaction log
[1397.46 → 1402.74] and parses that so whenever Postgres needs to read a page it goes and fetches the page from the storage
[1402.74 → 1408.10] system instead and there's and there's an interface for that so that's different from just running a
[1408.10 → 1413.78] Postgres on a remote volume because it actually understands about the Postgres uh disk format
[1413.78 → 1419.06] and it can do this uh branching it can do the copy and write uh stuff underneath that that's
[1419.62 → 1425.54] what else is exciting to you right now in the world of Postgres or even beyond well I mentioned pg
[1425.54 → 1429.86] vector already I think that's and that's an exciting thing people are doing a lot of exciting stuff with
[1429.86 → 1438.02] that uh Postgres world there's uh stuff happening with asynchronous Io uh from colleagues
[1438.02 → 1442.66] at Microsoft they're doing work on that so I think that will improve the Io speed and that's
[1442.66 → 1446.50] that's perfect for neon as well like the yeah because we've separated the storage that
[1446.50 → 1451.14] actually helps us a lot so I'm hoping to spend personally some time reviewing those patches to
[1451.14 → 1466.02] to see them go in cool I love it yeah, thanks for talking awesome thank you appreciate it thank you
[1468.02 → 1482.02] so
[1488.50 → 1495.62] so I'm here with IAN with row VP of product management at century so IAN you've got a developer first
[1495.62 → 1500.66] application monitoring platform it shows you what's slowed down to the line of code that's
[1500.66 → 1506.90] very developer friendly, and it's making performance monitoring actionable what are you all doing that's
[1506.90 → 1513.46] new what's what's novel there traditionally in errors what's the strength of century is we've taken
[1514.10 → 1519.14] not a stream of errors and said hey go look at this like all these error codes are flowing into it says
[1519.14 → 1525.22] we actually look at them, we try and fingerprint them and say hey we've actually grouped all these things
[1525.22 → 1531.46] and then we give you everything you need within century to go and solve that error and close that
[1531.46 → 1537.46] out and that's I think driven tons of value for our users and traditionally if you look at performance
[1537.46 → 1542.98] it's not that thing it's you know looking at certain golden signals setting up lots of alerts maintaining
[1542.98 → 1548.34] those alerts grooming those alerts and then detecting them, and maybe you have a war room, and you try and look
[1548.34 → 1554.18] at traces, or maybe you realize oh it's this engineering team that owns it maybe they'll look at logs whatever they have
[1554.18 → 1562.10] available performance is very rotated on detection and then isolating to where the problem may exist
[1562.66 → 1571.30] and root causing is often an exercise left to the user good performance products provide a lot of context and
[1571.30 → 1582.18] details that a experienced uh engineer or DevOps professional can can kind of parse and make sense of and try and get to a hypothesis of what went wrong
[1582.18 → 1591.62] but it's not like that century error experience where it's like here's a stack trace here's all the tags' oh we see it's like this particular set segment of code and
[1591.62 → 1602.18] IAN did the commit that changed that code and do you want to fire your issue and assign it to IAN like it's not like that crisp kind of tight right that we have errors this is breadcrumbs
[1602.18 → 1619.70] right, and we said hey maybe there's no reason why we could do this for performance let's try okay so you took a swing you tried to describe to me how that trial works if I'm is I go to my dashboard now and I enable APM on my application what are the steps
[1619.70 → 1630.30] largely because we kind of encourage you to go and set up uh transaction information when you set up century you probably as a user probably don't need to do much but if you skip that step you do need to configure to send that data
[1630.30 → 1653.02] uh in your SDK and what happens is we start now looking at that information and then when we see a what we call a performance issue we fingerprint that, and we put that into your issues feed which is already where you're looking for error issues right it's not a separate inbox this is the same inbox the same inbox yeah now we obviously give logical filters and if you just want to look at those we do that
[1653.02 → 1670.40] um and for newer users sometimes we detect hey you've probably never seen this before we can kind of we do things because we know we build for math market that bring your attention to it, but it's the same workflow you have for errors today so you don't have to learn something new uh to take advantage of these things
[1670.40 → 1682.60] so you asked the experience so last fall we did the experiment the first one which we called uh m plus one, and we didn't know how it was gone honestly uh but uh people liked it like we kind of know
[1682.60 → 1712.58] people like it when they start tweeting and saying things about it and so um yeah it got traction very cool so if your team is looking for a developer first APM tool to use check out sentry and use the code change law when you sign up, and you're going to get the team plan for free for three months make sure you tell them we sent you because they love hearing from our listeners check them out at sentry.io again sentry.io that's s-e-n-t-r-y dot i-o
[1712.60 → 1742.30] are we started, yet this is the show man all right we're here with Robert alkali hello his second appearance on the changelog apparently allegedly, allegedly sorry that's a better word so apparently also works
[1742.30 → 1750.14] according to to you and with some verifiable memory of mine we talked to you at Oscan probably 2018
[1750.14 → 1760.82] 2017 2017 maybe I would say 2019 yeah okay, and we talked about web assembly we did was this in Europe was it in Europe
[1760.82 → 1767.64] no, no okay it was in Portland well you were in it was in Portland you were there I went to Oscan London one time
[1767.64 → 1775.46] 2018 when that was okay was web assembly a thing then yeah it was uh yeah it was a thing it must have
[1775.46 → 1781.30] been as much as you were into it now okay this is sparking a memory okay isn't it yeah well backstory
[1781.30 → 1787.00] for you Adam is he walked by earlier and we both kind of locked eyes and I was like do I know you and he's
[1787.00 → 1791.64] like do I know you or something, and he's like yeah I think you had and I was like I have no memory of this
[1791.64 → 1797.56] I'm like I know this guy so I have a memorable face jarred and I went to an Oscan together in Austin I want
[1797.56 → 1804.54] to say right probably 2017 Portland in 2018 Portland 2018 that's probably where we met, and then we haven't
[1804.54 → 1810.02] been there since because it stopped yeah so that's why I thought the only Oscan we had been to was in
[1810.02 → 1815.86] Austin so in my memory until this moment have you now inserted one brand new Oscan in my life which i
[1815.86 → 1824.00] went to I definitely went to Portland in 2019 in the summer for sure so yeah because I took my
[1824.00 → 1830.24] daughter and my mom to meet with family and that was Oscan so maybe it's 2019 anyway either way
[1830.24 → 1833.86] neither here nor there history has been painted Robert was there he's probably correct, and we're
[1833.86 → 1838.96] probably wrong he was in the web assembly he's in the bioinformatics yes I am you're still into both
[1838.96 → 1845.58] of these things I surprisingly yes and I don't know what we talked about then specifically but one thing
[1845.58 → 1851.76] that is interesting to me about web assembly is how much promise it has but how much how little
[1851.76 → 1861.04] in my purview practical use it has beyond tinkers or people with very specific needs so just curious
[1861.04 → 1866.38] your perspective on that yeah I think I generally agree with that I think people who think that web
[1866.38 → 1872.00] assembly is going to be used everywhere are just wrong okay it's just not what it's meant for
[1872.00 → 1878.38] it's a very heavy-duty tool like if you have needs for running compute intensive workloads in the
[1878.38 → 1885.06] browser like Figma and photoshop Google Earth all the or bioinformatics I should add all those are great
[1885.06 → 1890.54] applications for web assembly because for the first time you can take code that's not written in JavaScript
[1890.54 → 1897.38] and bring it to the browser but if you're building your typical web application that doesn't have any
[1897.38 → 1905.08] sort of compute any sort of processing audiovisual then you probably don't need it okay that's kind
[1905.08 → 1910.28] of my view on it what about these people that are taking it server side there's a lot of talk about
[1910.28 → 1917.10] that as well I mean do you dip into that area at all a little bit, so there is a lot of excitement
[1917.10 → 1926.04] about that I don't share that excitement okay because here's the thing when you're running
[1926.04 → 1932.60] web assembly in the browser it lets you do something that was previously impossible you just couldn't take
[1932.60 → 1937.20] a c program running in the browser yeah except maybe arms, but that was kind of a precursor
[1937.20 → 1944.84] it lets you do things like SIMD that's also impossible with just JavaScript but once you leave the browser
[1944.84 → 1952.22] you can do whatever you want, so web assembly is one extra alternative to the other hundred you have
[1952.22 → 1959.36] so from that angle like there's a few use cases that I think are pretty valuable for web assembly on the
[1959.36 → 1966.04] server maybe you want to extend your application let's say with plugins, and you want to let users
[1966.04 → 1971.76] write whatever code they want, and you want to execute that securely web assembly is a good sandbox for that
[1971.76 → 1976.18] but then again you're not going to reimplement that yourself you're going to use some other tool
[1976.18 → 1982.98] that may be under the hood uses web assembly to solve that problem okay what kind of stuff are you doing
[1982.98 → 1993.36] so I'm doing mostly web stuff so bringing bioinformatics tools to the web for either building applications that
[1993.36 → 1999.18] analyze data in the browser so that you don't have to figure out bioinformatics dependencies which
[1999.18 → 2007.68] are kind of a mess if you want to keep your data private it's kind of a local only type workflow
[2007.68 → 2014.94] the other thing I'm really interested in is something I'm talking about tomorrow is using web assembly to
[2014.94 → 2022.92] power interactive tutorials for command line tools so that you can, you know instead of when a student logs
[2022.92 → 2029.04] into your website you spin up a container for them that's super expensive you can run these tools in
[2029.04 → 2037.40] the browser give them a similar experience and much, much cheaper for you to host what should we know
[2037.40 → 2043.52] about bioinformatics that makes sense to us what exactly is bioinformatics oh that's a good place
[2043.52 → 2048.54] say that three times fast bioinformatics bioinformatics bioinformatics that was not fast enough that was
[2048.54 → 2057.44] there's a pause in there I'll say it three times slowly please explain, so bioinformatics is using
[2057.44 → 2064.78] computer science and software engineering to analyze biological data okay like DNA yes exactly so for
[2064.78 → 2070.48] example if you're interested in knowing I don't know which diseases you might be at risk for you could
[2070.48 → 2080.08] take a blood draw isolate the DNA sequence it figures out what all the letters are and compare those to a reference
[2080.08 → 2086.62] and you know figure out what's different there, and it has that been associated in the past with some disease
[2086.62 → 2093.94] or something like that rights and so the process of figuring that out the algorithms and the software
[2093.94 → 2099.52] around that is basically bioinformatics so what does it take to take this kind of applications that are like
[2099.52 → 2104.32] probably behind a desktop application right they're probably written in c or for a desktop environment
[2104.32 → 2110.68] and you want to take this kind of applications to the web yeah to essentially open it up where
[2110.68 → 2116.64] you can just go to any platform Linux mac windows is that the is that the reason why yeah yeah and so
[2116.64 → 2124.30] like one example is uh I have this website called fastq.bio so it takes in some data that you get out of an
[2124.30 → 2130.58] instrument and run some really quick data analysis to tell you how good of a quality the data is
[2130.58 → 2136.60] and you know it runs in the browser because that's just super convenient people drag and drop their files
[2136.60 → 2141.66] and they're done they don't have to figure out install it how to set it up and all that stuff so that's one
[2141.66 → 2149.58] use case you wouldn't necessarily do super heavy-duty analysis it's still the browser you're kind of
[2149.58 → 2155.60] limited by what the user has, but it's a nice way to cover a ton of use cases that previously were
[2155.60 → 2162.96] not covered, and you specialize in the Wasm world in bioinformatics in particular like that's where
[2162.96 → 2169.62] your usage of Wasm is in that silo yeah that's that's right okay so I have a tool called bio Wasm
[2169.62 → 2178.02] bio Wasm yes that's pretty cool can you say bio Wasm three times much easier yeah that's true
[2178.02 → 2187.32] speaking of how do you guys pronounce Wasm is it Wasm or Wasm well I call it Wasm okay but
[2187.32 → 2192.64] I'm open to either direction I don't even understand why I call it Wasm but I do call it Wasm
[2192.64 → 2199.60] it's web assembly wasn't yeah it's a Wasm I mean if you should have it called it Wasm
[2199.60 → 2204.10] because I wanted to write me with awesome, but that was just a means to an end right
[2204.10 → 2209.00] but I do call it Wasm I'm not sure why I don't know either I think we may have been on a podcast
[2209.00 → 2212.98] with somebody who seemed to be more knowledgeable than we were and called it Wasm, and so we kept
[2212.98 → 2216.88] going there with him that's true although I think since then it didn't work for Richard hip I mean
[2216.88 → 2221.50] I still call it sequel light that's cool he's definitely more knowledgeable than I am
[2221.50 → 2228.90] about the project yeah so yeah I'll stick with Wasm until I'm convinced otherwise sounds good to me
[2228.90 → 2235.08] yeah now what do you call it I call it Wasm and so why do you call it Wasm because we don't know
[2235.08 → 2240.02] I don't anybody knows well that's the thing sometimes just the first way you hear it is just how you do it
[2240.02 → 2246.68] right what's a weird phenomenon in computer science and podcasting or real life
[2246.68 → 2251.96] conversing is yeah a lot of times with a term or an acronym or whatever it is you've
[2251.96 → 2257.28] never pronounced we'll read it for years guys we'll read it to ourselves for years, and we've never
[2257.28 → 2261.72] actually had to say it to somebody else, and then you have that moment of how do I say this I've been
[2261.72 → 2266.26] reading it for years writing it for years it's a weird moment that we all experienced so maybe we
[2266.26 → 2271.58] just had that with Wasm okay but I'm glad that we're all on the same page that is good we have
[2271.58 → 2276.52] consensus although on our show recently Christina warren did say yes I call it
[2276.52 → 2280.80] jiff, and then she just continued to talk as if we shouldn't stop the world and discuss
[2280.80 → 2284.70] do you remember that well she's here we can get her on the mice again Christina's here I saw her
[2284.70 → 2289.68] downstairs all right want to get her on we'll have to get her hey listen our listeners aka jarred
[2289.68 → 2293.78] listened to this part of the show and was upset because we didn't get the beef about jiff versus
[2293.78 → 2299.04] GIF I was upset at the moment I was, but she talks too fast so I just let it go I thought it was you
[2299.04 → 2305.24] know an appropriate amount of speaking cadence but uh I will agree all right I missed that argument
[2305.24 → 2308.82] let's get back we had better things to cover though we did let's get back to Robert we also
[2308.82 → 2313.96] have better things to cover right now yeah we do we're sidetracked okay so bioinformatics taking
[2313.96 → 2319.00] applications that are for the desktop to the web what kind of applications make the most sense you
[2319.00 → 2323.92] mentioned this one where it sort of does like data analysis yeah you know what does the web need
[2323.92 → 2328.74] what is a user base need of the web that can use this kind of tools in specific to what you know
[2328.74 → 2334.66] and then just in general for what Wasm can actually do yeah so I think for it's pretty similar
[2334.66 → 2341.18] across the board I think for bio you know tools that do some sort of preview of an analysis are
[2341.18 → 2348.54] really useful some analyses are just tiny too like if you're analyzing let's say the genome of
[2348.54 → 2353.90] viruses they're pretty tiny so you could actually just run the whole thing in the browser and so that
[2353.90 → 2361.82] gives you both the advantages not having to install the tools and to do it in a privacy conscious way
[2361.82 → 2369.52] in terms of you know more broadly outside bio because you have audiences that aren't a biologist
[2369.52 → 2375.76] is that right that are what that are not biologists um we haven't surveyed them recently but I think
[2375.76 → 2384.70] that's fair okay I would say we got at least one okay that's good um I guess there are a few categories
[2384.70 → 2390.48] if you have a tool that you already have in another language, and you really want to bring it to the web
[2390.48 → 2397.62] and you don't want to rewrite it all in JavaScript I think that's a great use case yeah if you have a
[2397.62 → 2405.84] slow application that has portions of it that are really heavy JavaScript compute in some cases this is
[2405.84 → 2410.68] something that's also tending to be overplayed this not always happens, but you can get performance
[2410.68 → 2416.58] improvements by switching it off with web assembly, but you can also get worse performance um
[2416.58 → 2422.72] and yeah that's kind of the couple of applications I think are pretty relevant describe worse performance
[2422.72 → 2428.96] is it like because sometimes access is enough and I'll wait because maybe the web is easier and I can't
[2428.96 → 2433.60] install it on my system or I can't because literally I literally can't install the application but I can
[2433.60 → 2440.18] browse the web and I can authenticate on the web yeah so one big thing that I've noticed
[2440.18 → 2446.58] is that when you have a web assembly module, and it needs to communicate a lot back and forth with
[2446.58 → 2454.66] the JavaScript world that is super expensive so if ideally your module takes in a little amount of data
[2454.66 → 2460.58] does a bunch of stuff and returns small amounts of data but if you're constantly returning large trunks
[2460.58 → 2467.88] and that's because um web assembly only understands numbers so like if you pass in strings converts to a
[2467.88 → 2473.18] number pass in an object convert to a number do you know the conversion by any chance like if
[2473.18 → 2480.16] I said the word what what number is that to Wasm oh of course it's 86 comma 112 noes I'm kidding
[2480.16 → 2486.28] it that'd be cool if you knew it would you could have kept going we totally bought it I would
[2486.28 → 2492.76] have been spooked I would have been like oh my gosh well that's cool numbers only so
[2492.76 → 2497.64] the translation layer in between is expensive yeah and so that's actually one way in which you can
[2497.64 → 2504.28] try to optimize the performance is that if you switch off you know some JavaScript with web assembly
[2504.28 → 2511.24] you can try to trim that down uh in order to speed it up yeah makes sense back to your
[2511.24 → 2518.56] current interest of CLI tutorials in the browser yeah are you giving people full-fledged Linux environments
[2518.56 → 2526.80] in the browser or how does it work not yet so right now in the v1 um every tool I have to compile
[2526.80 → 2535.44] to web assembly and then I have this sort of you know extern JS it simulates a console and i kind of
[2535.44 → 2542.00] hook those up together in the future what I'm going to do is actually switch that up with a full-blown Linux
[2542.00 → 2550.16] OS in the browser that's going to be a little slower, but it's going to be worth it for some of
[2550.16 → 2556.24] you know getting some things on there that are otherwise hard to do just by directly compiling
[2556.88 → 2563.44] and the way this is using an open source project called v86 so they wrote essentially
[2563.44 → 2567.68] a CPU emulator in rust, and so they compile that to web assembly and that's kind of how
[2568.32 → 2572.40] they emulate the whole operating system, and it boots up there are a bios there's everything
[2573.04 → 2581.20] it's pretty wild that'd be kind of cool man you can uh can you stimulate any bios or just particular
[2581.20 → 2590.56] bios I honestly don't know what a bio do okay so well it's a basic input output system except for i
[2590.56 → 2596.08] know how to get there in most cases delete delete delete or maybe, maybe one of the f's it could be a f11
[2596.08 → 2600.48] it could be a f10 who knows just hit all the f's I mean if it's you have to watch real fast which was
[2600.48 → 2605.76] a delete right gosh I missed it you know it's like booted up already well I think of that because
[2605.76 → 2611.44] if you can emulate those things you can kind of give something a playground to configure hardware or to
[2611.44 → 2616.08] configure a bio or whatever it might be to be like okay this is how you change the boot order this is
[2616.08 → 2622.56] how you set these two mime drives to be the boot or to the USB or whatever it might be or this is how
[2622.56 → 2627.68] you set up virtualization in you know this particular intel CPU for example those are the
[2627.68 → 2631.92] kind of things that you kind of have to have the hardware to learn until you have the hardware you
[2631.92 → 2635.52] can't learn it, and then you're kind of by yourself you know what I mean if you could do it in an
[2635.52 → 2640.00] environment like that there could be interactivity because you're because you're emulating it you know
[2640.56 → 2646.48] I was mostly thinking like once you're logged in past boot time right yeah this is an interesting
[2646.48 → 2650.24] use case for it yeah it's a black box I mean you go to the forums you'll find zillions
[2650.24 → 2656.08] and I don't mean that like literally zillions but quite a lot of people saying how do you do this
[2656.08 → 2660.96] with these bios or whatever am I you know all the bios out there, and you got somebody showing
[2660.96 → 2665.52] screenshots and that's just so like that's caveman knocking rocks together trying to make fire
[2665.52 → 2671.04] you know you can have this emulator be like this is how it works that would be amazing you know
[2671.04 → 2676.96] I'll send you the hardware it's just here in the browser to play with yeah yeah so once you're logged in
[2676.96 → 2682.80] how uh how leaky is the abstraction right now meaning like right maybe you know what I mean
[2682.80 → 2690.88] I do not know okay what do you mean by leak abstraction what I mean is so for instance a lot
[2690.88 → 2697.20] of text editors have vim mode most vim users will use vim mode for about seven to 12 minutes and be
[2697.20 → 2703.60] like this is not vim I can see all the places where this is not clearly not vim your leaky abstraction is
[2703.60 → 2708.72] not the right term I'm just I just overused that term yeah your emulation ends maybe we call it the
[2708.72 → 2712.72] uncanny valley of what you're actually trying to emulate where it's like yeah this is not good
[2712.72 → 2719.84] enough yeah so if you're using some like cmd instructions that are too fancy that's that won't
[2719.84 → 2725.76] be supported yeah if you're doing multi-threading the emulator doesn't really support that so you'll
[2725.76 → 2732.96] just have to stick to one thread um that's those are kind of big ones you're also just limited by how
[2732.96 → 2739.20] much ram you can use in the browser right um and also like more realistic limitations like if you're
[2739.20 → 2747.92] trying to run some java program I tried this recently it works, but it takes a few minutes yeah just slow
[2747.92 → 2755.68] so you know practice not practical in that case right kind of the 80 20 rule yeah okay how big of a
[2755.68 → 2762.64] performance hit boot up time or load time we'll just call that will it be to switch to this full Linux
[2762.64 → 2766.80] environment and is anybody else doing this currently like loading Linux completely in the browser
[2767.60 → 2774.80] yeah, so there are projects that are using it i I'm not aware of people building tutorial sites
[2774.80 → 2782.96] with it which is a shame because it's a really powerful tool um most tutorial platforms I'm aware
[2782.96 → 2788.96] of tend to do the whole like we'll spin up a container yeah shut it down after a while which is super
[2788.96 → 2795.60] expensive um expensive for them to run for their users yeah yeah and typically what you'll see is
[2795.60 → 2802.16] they'll start hey we have a free tier they'll be like hey uh maybe just you can use it for a few hours
[2803.20 → 2808.48] and then it turns into there's no free tier because we can't support you can't support it long term
[2809.04 → 2814.16] I think about debian just released a new version, and they're I believe the installation process
[2814.16 → 2820.08] changed enough to be talked about so it'd be cool to emulate for Debian when they launch like here's
[2820.08 → 2825.52] how the new installation process works here are the screens that have changed if you're doing like a
[2825.52 → 2830.80] unique disk set and this is how you need to do you know raid or whatever or choose this or that or choose
[2830.80 → 2835.84] ZFS or whatever it might be then you can emulate it in the browser this is like a great example
[2835.84 → 2839.28] of that because you can see it before you actually have to install it, or you can install it, but you have
[2839.28 → 2844.72] to have the hardware and enough hardware to expend on a tutorial right or at least be able to virtualize
[2844.72 → 2848.80] with say Dropbox but maybe Dropbox can't support the latest debut which it can, I'm just saying like
[2848.80 → 2852.96] what if there's something there if you emulate it you can sort of just it's marketing in a way it's
[2852.96 → 2857.12] almost like here's how it works right and if you don't know how it works this is how it works
[2857.76 → 2863.20] i this sounds awesome I can't do these things I want this he's focused on bioinformatics right
[2863.20 → 2867.20] you're teaching specifically this kind of tutorials, but you're playing with xterm.js though right
[2867.20 → 2870.96] right and your platform is beyond right like you could use this generally yeah you can use this
[2870.96 → 2877.68] for anything really um now of course i I am going to add tutorials that are not bio specific like
[2877.68 → 2885.28] git and grips and AWK all these things that I think everybody's the basics yeah core utils so give an
[2885.28 → 2891.44] example of how these tutorials would work then like let's say I have zero idea of how I would use AWK or
[2891.44 → 2896.72] grew yeah, so there's an AWK tutorial right now you can go to sandbox.bio
[2897.68 → 2904.00] and click on the AWK tutorial it basically shows you tutorial contents on the left, and it shows you
[2904.00 → 2911.04] some scenarios like let's say you want to analyze the tab separated file and filter out rows that have
[2912.00 → 2915.36] a number greater than whatever in a column so you can do this sort of things
[2916.80 → 2923.52] AWK by the way is a whole programming language which is amazing you can launch processes
[2923.52 → 2932.72] within it, you can write to files you can like it's quite, quite deep yes yeah uh but yeah so the tutorial
[2932.72 → 2941.44] has these sorts of examples, and then you have uh exercises and so you'll some of them I admit are a bit
[2941.44 → 2948.00] probably too complicated like you're doing a bit too much math for AWK but just to show you how like how
[2948.00 → 2956.80] powerful it is, and you're working in like a emulated environment that is a terminal with an
[2956.80 → 2962.64] emulated version of AWK that's right yeah right it's using new AWK version I don't know five point
[2962.64 → 2971.04] something how do you author these tutorials so some of them I've made up some of them I work with others
[2971.04 → 2978.08] who already wrote text-based tutorials and we kind of bring them into this interactive place and it is kind
[2978.08 → 2985.52] of brings them to life okay describe this interactive place oh I just mean like you know is it like the
[2985.52 → 2993.84] good place the bad place it's a very good place it's a very good place um that that could be the sequel
[2993.84 → 3002.24] very good there you go but yeah so basically we just take the markdown put it into this sandbox.bio
[3002.24 → 3008.72] kind of template and if it uses a tool that I've already compiled to web assembly
[3009.44 → 3013.44] we can just use it directly if not then we have to bang our heads against the wall figure that out
[3013.44 → 3019.76] first and then put it in are these we just had a conversation too what was that conversation about
[3019.76 → 3027.92] jerry gosh uh a cinema kind of similar to this in a way I mean you're it's not tutorial, but it's
[3027.92 → 3033.68] recording what you did so it's almost it's a playback right in an emulation state I mean if
[3033.68 → 3037.92] you can rewind and touch and feel and kind of like delete that'd be kind of cool too it's not quite the
[3037.92 → 3043.28] same, but it's got the similar fidelity yeah the fidelity is there like it's literally the example
[3043.28 → 3048.40] of what was recorded and so this is probably an example of what could be real life so they're very
[3048.40 → 3054.08] similar in that way what am I trying to say though what are you trying to say is embeddings and like
[3054.08 → 3061.12] using this thing to like is this something where you said it's uh sandbox.bio yes okay so that's the
[3061.12 → 3066.48] URL yes that's for the tutorial website and so you're using this to show off tutorials you want
[3066.48 → 3072.56] to show off right correct and can can I author my own tutorials and put them on there or take them and
[3072.56 → 3077.12] do some like how can I if I believe in what you believe in with this thing and I want to do my own
[3077.12 → 3083.60] things I want to show off whatever yeah i so we're not yet at the point where we can, you know have an
[3083.60 → 3088.48] automated system where you can log in and create tutorials but typically the way it works is you
[3088.48 → 3096.32] email me you're like hey no way yeah okay classic collab could you fork the repo or something like
[3096.32 → 3103.04] that and sure yeah yeah and like if you want to just play with having Debian in the browser you could
[3103.04 → 3110.00] also look at the v86 which is what I'm using right to emulate it um, and you could, you know run it
[3110.00 → 3115.76] on your own site or if you want to embed it or all that's possible yeah well I was actually thinking
[3115.76 → 3121.52] about this recently and I just did this with like screenshots I did a fresh installation of because I've
[3121.52 → 3131.20] been messing with Ubuntu 2204 or sorry 2304 and I just did a know I got a redundant OS installation
[3131.20 → 3136.16] I've got two discs I've got a swap I've got a boot you know I've got root all that stuff like that
[3136.16 → 3141.12] and so rather than just choosing one drive I want to have the system be fully redundant by having
[3141.12 → 3147.04] two drives in mirror and I want to I like to show that off either in written but the only way I could
[3147.04 → 3152.08] do it really was like through screenshots and then right around those screenshots now will I do a full
[3152.08 → 3156.96] emulation it'd be kind of cool to have all of what I already have but then at the end or somewhere
[3156.96 → 3162.96] else a sidecar would be like here's literally the environment to go and do just that you've got two
[3162.96 → 3167.52] disks so when you get to that part you can configure these disks, and you can follow my instructions
[3167.52 → 3174.00] so rather than having to pull down a VM or pro MOX or actual hardware you take an USB stick and boot
[3174.00 → 3180.08] up into and do the full thing yourself it's accessibility to what's kind of trivial to some
[3180.08 → 3183.92] redundant OS installation on Linux, but it's there are a lot of steps in there you know there's a lot of
[3183.92 → 3188.32] steps in there and like choosing the partition adding the partitions and giving them the know the
[3188.32 → 3193.20] paths and stuff like that and adding them it's an it's a mess really so I want to do the example
[3193.20 → 3198.32] through screenshots, but the best version of that really would be an interactive playground they could
[3198.32 → 3204.80] do I mean just follow the steps yeah I'd be curious to see if it works with all the configuration of like
[3204.80 → 3212.08] disks and bios and all that combination I think well if if i were doing it what I would, it would
[3212.08 → 3217.68] be the happy path you could only you would only have two disks I mean sure you can go with one disk but
[3217.68 → 3221.92] you would be that's not why you're here you're not here to configure one disk you're here to
[3221.92 → 3227.20] configure two disks in redundancy you know and so it'd be the happy path of being able to configure
[3227.76 → 3233.52] Ubuntu a new system with two disks with redundancy, and it would walk you through all that stuff yeah
[3233.52 → 3238.64] that would be kind of cool because you can literally see what you would see on your screen if you were
[3239.84 → 3245.20] in your home lab doing this or in the environment you're in doing this and to me that's that's like
[3245.20 → 3250.96] empowering yeah because now every system I want to have this like rock solid I'm going to use my own
[3250.96 → 3256.56] tutorial for my future self right this is how you do it Adam you know what I mean yeah I think that
[3256.56 → 3262.96] would be super powerful uh use case for that I'm thinking like aircraft tutorials you know aircraft
[3263.52 → 3269.28] website that we all find eventually yes whenever you're trying anything nick yeah Linux oh and so like
[3269.28 → 3274.72] his he's got really detailed tutorials, but it would be really cool, and they're step by step type this
[3274.72 → 3279.92] type this right it'd be really cool if each one had a button that's like launch an emulation and you
[3279.92 → 3284.32] can follow the tutorial in an emulator yeah that's what I'm talking about see you're where I'm at I am
[3284.32 → 3288.32] where you are I'm connected I went a long way around the lake, and he's like let's just go across the
[3288.32 → 3294.80] lake on a speed boat it's kind of how like how we talk to chat GBT you know yes that's right I get
[3294.80 → 3299.84] straight to the point thank you chat GBT Adam has a very cordial conversation with oh yeah that is
[3299.84 → 3308.08] great insight chat GBT tell me more so like use cases like that I think would be really powerful
[3308.96 → 3312.40] you should do how far away are we from that you should do this man make it a thing
[3313.28 → 3321.12] I would love to but um first I know very little about hardware stuff so oh this would
[3321.12 → 3327.52] need there's that this would need a collaboration of sorts so if you can is you're listening to this
[3327.52 → 3333.28] and you can fill in the gaps where Robert has them email him if you want to collab if you want
[3333.28 → 3341.04] Robert at fork sandbox dot bio uh no that's not his email okay well my email is quite long
[3341.04 → 3345.60] Robert dot Abu Khalil at gmail.com okay there we go we'll throw that in the show notes for folks
[3346.24 → 3354.88] and the repo lives on on github we'll link that up cool stuff man I like it so much
[3354.88 → 3360.40] possibility yeah so much potential and I believe you could do it, and you should do it we should
[3360.40 → 3366.32] let's do it thank you for doing all you've done so far let's do it was mall right thanks for talking
[3366.32 → 3371.44] to us yeah, thanks for sure this was better than the first one I think it was yes I'm sure jarred's
[3371.44 → 3376.88] like I'm sure we'll see if it ships then you'll know if it's good that's true the last one never
[3376.88 → 3381.76] shipped that was terrible too you should diff it if you see is i maybe I just said the same
[3381.76 → 3388.08] thing I don't remember oh yeah transcript it and diff it there's an idea
[3388.08 → 3404.80] what's up friends I'm here with one of our good friends for Ross of Buchan DJ for Ross is the founder
[3404.80 → 3411.52] and CEO of socket you can find them at socket.dev secure your supply chain ship with confidence but
[3411.52 → 3416.72] for Ross I have a question for you what's the problem what security concerns do developers face
[3416.72 → 3421.52] when consuming open source dependencies what does socket do to solve these problems so the problem
[3421.52 → 3427.20] that socket solves is when a developer is choosing a package there's so much potential information they
[3427.20 → 3430.88] could look at right I mean at the end of the day they're trying to get a job done right there's a
[3430.88 → 3435.04] feature they want to implement they want to solve a problem so they go and find a package that looks
[3435.04 → 3439.36] like it might be a promising solution maybe they check to see that it has an open source license that
[3439.36 → 3444.56] it has good docs maybe they check the number of downloads or GitHub stars, but most developers don't
[3444.56 → 3450.32] really go beyond that and if you think about what it means to use a good package to find it to use
[3450.32 → 3454.96] a good open source dependency we care about a lot of other things too right we care about um who is
[3454.96 → 3459.52] the maintainer is this thing well maintained from a security perspective we care about does this thing
[3459.52 → 3463.84] have known vulnerabilities does it do weird things maybe it takes your environment variables
[3463.84 → 3469.04] and it sends them off to the network uh you know meaning it's going to take your API keys your tokens
[3469.04 → 3473.84] like that would be bad uh the unfortunate thing is that today most developers who are choosing
[3473.84 → 3477.44] packages and going about their day they're not looking for that type of stuff it's not really
[3477.44 → 3482.80] reasonable to expect a developer to go and open up every single one of their dependencies and read
[3482.80 → 3488.48] every line of code not to mention that the average NPM package has 79 additional dependencies
[3488.48 → 3493.68] that it brings in so you're talking about just you know thousands and thousands of lines of code and so
[3493.68 → 3499.12] we do that work for the developer so we go out and we fully analyze every piece of their dependencies
[3499.12 → 3503.28] you know every one of those lines of code, and we look for strange things we look for those risks
[3503.28 → 3507.92] that they're not going to have time to look for so we'll find you know we detect all kinds of attacks
[3507.92 → 3513.12] and kinds of malware and uh vulnerabilities in those dependencies, and we bring them to the developer
[3513.12 → 3517.76] and help them when they're at that moment of choosing a package okay that's good so what's the installation
[3517.76 → 3522.24] process what's the getting started socket super easy to get started with so uh we're you know our whole
[3522.24 → 3527.28] team is made up of developers and uh so it's super developer friendly we got tired of using security
[3527.28 → 3532.56] tools that send a ton of alerts and were hard to configure and and and just kind of noisy and so we
[3532.56 → 3537.36] built socket to fix all those problems so we have all the typical integrations you'd expect a CLI
[3537.36 → 3543.68] a GitHub app an API all that good stuff, but most of our users use socket through the GitHub app and
[3543.68 → 3549.12] it's a really fast install a couple clicks you get it going, and it monitors all your pull requests
[3549.12 → 3553.36] and you can get an accurate and kind of in-depth analysis of all your dependencies really high
[3553.36 → 3558.16] signal-to-noise you know it doesn't just cover vulnerabilities it's actually about the full
[3558.16 → 3563.28] picture of dependency risk and quality right so we help you make better decisions about
[3563.28 → 3567.52] dependencies that you're using directly in the pull request workflow directly where you're
[3567.52 → 3570.96] spending your time as a developer you know whether you're managing a small project or a large
[3570.96 → 3575.92] application with thousands of dependencies socket has you covered, and it's pretty simple to use it's
[3575.92 → 3582.56] it's really not a complicated tool very cool the next step is to go to socket.dev install the GitHub
[3582.56 → 3590.72] app or book a demo either works for us again socket.dev that's s-o-c-k-e-t.dev
[3606.88 → 3612.56] so we're here with m Scott ford you have a name like a great novelist have you ever been told that
[3613.28 → 3617.76] uh no I have not been told that m Scott I'm just calling you Scott right yeah just Scott
[3618.32 → 3624.32] yeah what is uh the m Stanford is it Matthew okay yeah it's uh my parents named me Matthew Scott
[3624.32 → 3629.28] but never called me Matthew huh they must have decided later they liked the middle name better
[3629.28 → 3634.32] yeah let's make a mistake there's a story there first name there's a story there somewhere yeah I don't I
[3634.32 → 3641.36] don't I don't know that I ever got the full story, so okay could be a conspiracy yeah you and I go way
[3641.36 → 3651.44] back yeah years and years uh your wife Andrea was a speaker at my conference yep probably a decade ago
[3651.44 → 3657.76] I don't know yep listener of the show I think we communicated I came on your guys podcast legacy
[3657.76 → 3664.24] code rocks legacy code rocks yeah probably a decade ago uh always good to see you I think we've met
[3664.24 → 3669.92] once or twice before but good to have you here not so I met you at sustain I think I was oh yeah
[3669.92 → 3675.20] I think you recorded me and Andrea yeah recorded me and Andrea for that so right on lots of history
[3675.76 → 3684.08] lots and you uh co-own corgi bites yep which is a consultancy well how do you describe yourselves yeah
[3684.08 → 3689.52] so we focus on your know kind of modernization and maintenance and just kind of the joy of making
[3689.52 → 3695.92] improvements to software systems and that's you know we have a team of people who love making
[3697.04 → 3704.80] making code better building out test suites uh fixing bugs paying down technical debt yeah uh yeah
[3704.80 → 3709.60] like i was talking with Adam yesterday like I love fixing bugs like just going through a
[3709.60 → 3716.48] a list of bugs and finding and fixing them that's like so much fun I love bugs dot com
[3717.28 → 3721.76] seriously yeah it was like 4200 bucks but yeah it's available that's still available that's
[3721.76 → 3727.52] affordable yeah it's true and today's well I guess we spent a thousand dollars on changelog.com like
[3727.52 → 3733.76] okay that was yeah because before you was like the changelog.com yeah but if you were really
[3733.76 → 3738.40] passionate about bugs you have the domain it's true I love bugs somebody's out there holding that
[3738.40 → 3742.40] thinking someone's this passionate about bugs they're going to give me available on the market
[3742.40 → 3748.32] this isn't like a broker this is available in the market 4200 yeah it's a premium domain so they're
[3748.32 → 3754.40] holding it as like a premium cost domain well cash is tight these days yeah so corgi bites has been
[3754.40 → 3761.60] a long time business yeah so uh it was founded in 2008 uh I had no idea what I was going to do with
[3761.60 → 3767.68] if it was pretty much just a name and then Andre came on, and we started doing consulting uh we did like
[3768.48 → 3774.48] small little websites at first and didn't really enjoy that and was trying to figure out like you
[3774.48 → 3780.40] know what is it what is that I liked doing and then stumbled in on like i love fixing code I love
[3780.40 → 3785.36] I love turning into a mess into something that looks new so like a brown field into a green field right
[3785.36 → 3790.80] that transformation process is something that I like genuinely enjoy doing so building a company around
[3790.80 → 3796.40] that has been a lot of fun there's people who like brand-new cars and there's people who like to
[3796.40 → 3802.24] restore yeah old cars and those people tend to be different people you know and some people just
[3802.24 → 3808.88] love that well I think like like like for me like i I've sometimes fantasized like if I had enough
[3808.88 → 3818.88] money and time to do it I would probably love getting like a late 1990s era car and like fixing it up
[3818.88 → 3824.80] and turning into an EV like so, so like kind of like it's almost like for me sometimes it's the bridge of
[3824.80 → 3831.20] the old and the new so taking something that's old and breathing new life into it and making it do more
[3831.20 → 3838.48] than it used to making it better than it was before I love it too I mean you and i we found common ground
[3839.04 → 3844.40] I did some rescue projects back when I was consulting I loved it i kind of like being the hero you know
[3844.40 → 3848.72] like this is all bad it's like well here comes jarred he's going to make it better yeah and i think
[3849.44 → 3854.40] for me, it's less about the hero and more about you know there are folks who think it's not possible
[3855.28 → 3858.88] and it's its almost like it's almost like a challenge and like a hold my beer kind of moment
[3858.88 → 3864.56] like right like no this we can turn this around you don't have to start over this can be made
[3864.56 → 3871.04] better what's the gnarliest turnaround you've done maybe in terms of lines of code or time spent or
[3871.04 → 3875.76] you thought you weren't going to be able to do it yeah, so there was a there was a system several years
[3875.76 → 3884.32] ago that you know they were kind of they were on a cloud um a cloud server uh, and they weren't doing
[3884.32 → 3889.60] a very good job keeping this underlying server up to date so I wanted them to I wanted to help
[3889.60 → 3893.52] them move from infrastructure as a service solution to more of a platform as a service solution
[3893.52 → 3897.60] because I thought that the organization would be able to do a better job keeping up with that
[3898.16 → 3902.48] and then they wouldn't have to worry about like OS level updates anymore like they could just kind
[3902.48 → 3910.40] of focus on their code because the OS level updates were way behind um like eight years behind
[3910.40 → 3914.32] like you know they hadn't they hadn't done any Windows updates on this Windows server for like eight years
[3915.20 → 3921.52] and that was a that was a challenging transition it took a lot longer than I thought it would end up
[3921.52 → 3926.96] crediting the client some time because of that and just kind of recognizing that like I thought it
[3926.96 → 3931.60] was going to go easier than it actually turned out to be we kept finding services that were running on
[3931.60 → 3936.56] that server like in the background that we didn't you know we didn't know about and one of them we didn't
[3936.56 → 3944.08] have a source code for uh that was fun to grapple with that as a challenge yeah that was definitely one
[3944.08 → 3953.36] that that was difficult okay long-standing business hits against this recent macroeconomic
[3953.36 → 3958.40] downturn yes it is, and it's gone south huh it has been challenging so we've lost a significant amount
[3958.40 → 3964.16] of our revenue our team is probably about a quarter of the size as it was a year and a half ago
[3965.04 → 3970.56] uh and I've talked with other business owners that have you know companies a similar business model to
[3970.56 → 3977.36] ours software services and there are a lot that have been hit really hard a lot have gone out of
[3977.36 → 3984.88] business uh Andrea said she had read an article with an i I forget who it was I could probably find
[3984.88 → 3990.24] it if you wanted it for show notes, but it had a quote in there that you know there's a like an
[3990.24 → 3996.00] extinction level event for small software companies going on right now, and you know it's you know there's
[3996.00 → 4001.12] a lot more talent on the market so from a services' perspective it's a lot easier for
[4001.12 → 4006.56] companies to hire full-time than it used to be so I think you know there's less motivation to
[4007.20 → 4012.64] work with contractors or stretch your team out that way I also think it's just a way that
[4012.64 → 4018.32] organizations have been trying to cut expenses and cut costs, and you know when you look at a when you
[4018.32 → 4023.76] look at a balance sheet when you look at a profit and loss statement contractors come out of a different
[4023.76 → 4030.48] different part of that than full-time employees do so you know for your investors you know it can look
[4030.48 → 4034.96] like the organization's doing better if you cut those expenses you know kind of further down on the
[4036.08 → 4043.84] further down on the profit statement so yeah I think you know all the economic factors that are going on
[4043.84 → 4053.92] right now so inflation interest rates two wars you know the small medium-sized bank failures I think
[4053.92 → 4058.64] Silicon Valley bank really caused a lot of VCS to really pull back some money I've heard stories of
[4059.52 → 4065.76] companies that were funded with like you know say 30 million dollars had their funding pulled uh and so
[4065.76 → 4070.72] the know the business had to shut down where the investor was just like you know the money I've
[4070.72 → 4076.48] given you I want back or the money I haven't given you, yet you're not getting um so that's you know
[4076.48 → 4080.64] that's definitely a challenge that's going on right now so i kind of think of like
[4080.64 → 4086.80] that VC funding almost as like plankton in an ecosystem and like that dries up and the smaller fish
[4086.80 → 4091.36] get affected first and then and then they're not using services from the bigger fish and then so
[4091.36 → 4096.64] they start to they start to get affected so I think there is that kind of like that ripple effect to the ecosystem
[4096.64 → 4103.68] is that similar to krill plant things like krill yeah yeah the little guys basically the smallest of
[4103.68 → 4108.64] the small that yeah that the whales chase yeah and that drives up, and you got a big wheel that's
[4108.64 → 4113.12] just hungry right the big well the big whale can go without food for a little while, but it's going to
[4113.12 → 4117.68] start to affect it too so and then what does that eat you know it's like oh man my krill is gone
[4118.24 → 4123.60] I guess it'll die we think about this too like how has the market shifted in terms of what it
[4123.60 → 4128.40] perceives as value because when you have less you scrutinize more you think well was that really
[4128.40 → 4135.52] that I just spent my money there because we had the money and yeah we thought it was viable and so
[4135.52 → 4141.04] it was viable and now that we reconsider because I think in the last three years since the pandemic
[4141.04 → 4146.96] we basically the whole globe has been reconsidering almost everything absolutely right and so in a
[4146.96 → 4155.44] reconsideration of what the value is do you think that the value of these rehab projects has changed
[4155.44 → 4160.80] or do you think it's just that there's no money uh I think the value I think the value has changed i
[4160.80 → 4166.88] also think that low code no code platforms have had a factor as well you know it's a lot easier for
[4168.80 → 4172.96] it's its a lot easier to build something kind of quick and dirty that you know might meet your
[4172.96 → 4179.92] immediate needs and maybe do that as an experiment for starting over without having to like engage
[4179.92 → 4185.60] a development team, and you know that's that's a capacity that that's great like you know it will
[4185.60 → 4192.00] be an enabler for business, and so I think like on the larger economic scale that's that's good and you
[4192.00 → 4198.08] know it does kind of affect the organizations that would have helped build the thing that that low
[4198.08 → 4204.40] code no code platform you know is now building instead yeah the um I do think that for the
[4204.40 → 4209.76] maintenance side I predict in the next five years and kind of within the next five years you'll have
[4209.76 → 4214.56] organizations that have really built a lot on top of those low code no code platforms and start to bump
[4214.56 → 4220.24] up against the constraints and want to start to break out, and so I think there'll be a market for
[4221.12 → 4227.52] helping organizations you know move that functionality outside those platforms or find ways to extend
[4227.52 → 4232.48] that functionality maybe through extensions that the vendor provides or things like that where there's
[4233.04 → 4239.68] custom software that needs to be built there yeah I do see that as an opportunity and yeah you
[4239.68 → 4243.92] know that has an effect and I'm sure AI is having an effect at some point as well I don't know how to
[4243.92 → 4249.68] quantify that, and it's you know I imagine it's, and it could just be part of like a wait and see
[4250.56 → 4254.56] on a lot of organizations when they're trying to make hiring decisions or how they're going to grow their
[4254.56 → 4259.12] team maybe they're just waiting to see how productive their teams are going to be and how
[4259.12 → 4265.44] that productivity might change yeah as they start leveraging AI you mentioned in our conversation
[4265.44 → 4273.44] yesterday which was not on the air obviously yeah uh and to some degree even TMI, but you mentioned
[4273.44 → 4278.56] this desire to or the the essentially business model is wrong I'm trying it, and you can fill in the gaps
[4278.56 → 4284.48] the business model is wrong it needs to change, and you consider products yeah in and around what
[4284.48 → 4290.00] you already do but a product that you can buy that has a finite value that's maybe easier to buy even
[4290.00 → 4294.00] yeah because there are a lot of problems that we've seen over the years that many teams have been
[4294.00 → 4300.80] facing and I do think there's a market for building solutions to help teams solve those problems
[4300.80 → 4306.08] themselves without having to hire an outside contractor or an outside team and so there are aspects
[4306.08 → 4313.44] that I think could be productized, and we've gotten started a little bit on on on one product we've
[4313.44 → 4317.76] been working on it for a couple of years don't really have you know we've got like an alpha demo that we've
[4317.76 → 4322.56] shown to people I've gotten some feedback on we're still kind of working we're hoping to have a beta out
[4323.44 → 4327.84] you know probably first quarter next year is kind of realistic for having something that people
[4327.84 → 4332.80] could actually sign up for and give us better feedback on uh that's called freshly it's its around
[4332.80 → 4340.64] um analyzing dependency fresh freshness and looking at how fresh or out of date software dependencies
[4340.64 → 4346.88] are like third-party dependencies most of them open source dependencies, and you know really assessing
[4346.88 → 4353.04] the quality of an application or a project from that perspective we also wanted to be able to assess the
[4354.00 → 4362.24] you know at multiple levels of the mentioned Adam that you're not a big fan of supply chain uh as a
[4362.24 → 4367.68] term for this generally a pejorative like yeah open source is not a supply chain it is a common
[4368.24 → 4373.68] right it's not a supply so we just tap into and get yes it's a negative yeah if you think of like
[4373.68 → 4379.20] if you think about your dependency graph you know I think it would be great to evaluate
[4379.20 → 4385.12] multiple nodes on that dependency graph and not just evaluate your node so how well are the upstream
[4385.12 → 4390.48] projects that you're depending on how well are they keeping up with dependencies that they're managing
[4390.48 → 4395.52] and so I think you know that could be uh some pretty good meta analysis as well a way to maybe even
[4395.52 → 4403.52] measure the health of a project that you're thinking of uh working with and this is the similarity between
[4404.08 → 4409.92] maintenance this idea freshly how old are my dependencies how fresh are my dependencies and this
[4409.92 → 4415.68] aspect of security because a lot of maintenance or even like a refresh on a project like you've
[4415.68 → 4421.12] talked about its kind of a security burden like some of these products might be security-issue
[4421.68 → 4427.60] that you're talking about, and so I think you know having out-of-date dependencies one of the motivations for upgrading them
[4428.16 → 4435.92] is very much to try to avoid security issues that's one of the motivations I think there's also motivation around
[4435.92 → 4442.80] team productivity it's a lot easier to work with the latest version of a library than it is an older version just in terms of finding documentation
[4442.80 → 4447.04] you know when you go look for the documentation for projects you're going to find the latest
[4447.04 → 4451.76] the latest version is going to be easy it's usually findable yeah yeah blog posts are going to usually
[4451.76 → 4458.80] cover more recent versions than what you're working with is has been my experience so uh but yeah on the
[4458.80 → 4464.24] security angle you know that i I think is a big motivator to try to avoid some of those security
[4464.24 → 4468.64] issues and a lot of people we've put the product in front of to kind of give demos they told us in
[4468.64 → 4474.16] addition to just seeing how out of date things are they do want some perspective of how security plays
[4474.16 → 4480.40] a factor so I've taken one of the dependency freshness measures that we're using is called
[4480.40 → 4488.48] Libya, and you can learn more about that at libyr.com and then I've taken a security approach to that and
[4489.36 → 4496.32] built what I call like a liability index which computes a similar metric as Libya, but it looks at instead
[4496.32 → 4500.24] it where Libya looks at the distance and time between the version that you're using and the
[4500.24 → 4506.16] latest version uh the liability index which i I published the liabilityindex.com we haven't
[4506.16 → 4513.28] implemented a version of it yet, but it looks at the version you're using and the distance between
[4513.28 → 4518.16] the next version that doesn't have any vulnerable any published vulnerabilities so you know if the
[4518.16 → 4525.76] version you're on has published vulnerabilities yeah how many years in the future you have to go
[4525.76 → 4530.88] do you have to go in order to find a version that doesn't have any published vulnerabilities and so
[4530.88 → 4535.92] I think that could give more of a kind of security focused approach uh to that and maybe even
[4535.92 → 4541.12] looking at different levels for like you know liability index at the critical level, or you know
[4541.12 → 4546.16] different severity levels so I think that's the thing about source graph like source graph
[4546.16 → 4551.84] is an intelligence platform that helps you understand code part of that understanding is like is my stuff
[4551.84 → 4556.56] vulnerable yeah or prone to vulnerabilities and one of the things that we're trying to do that's
[4556.56 → 4563.20] unique with freshly is not just capture how things are right now but capture how they used to be yeah and
[4563.20 → 4567.12] graphing that over time so this these metrics that were that we're collecting, and we're computing
[4567.84 → 4573.12] we're mining information from the source code repository and computing what these metrics would have been
[4573.12 → 4579.20] like in the past and graphing that information and I think the trend can can really paint a really
[4579.20 → 4584.08] interesting picture for leadership and hopefully get budget for some of these improvement efforts
[4584.88 → 4589.36] something I've seen on a lot of teams is there'll be engineers on the teams who are aware this is a
[4589.36 → 4594.32] problem they want to fix it they don't like that they're living with the status quo, and they feel
[4594.32 → 4598.96] like their leadership hasn't given them enough flexibility to really go in and solve the problem they
[4599.76 → 4604.56] they feel like they're told to obsess over features instead and some of these essential maintenance
[4604.56 → 4611.12] activities get prioritized sure, and you think bubbling that up to somebody with decision-making
[4611.12 → 4617.04] that's my that's my hope is that if is leaders the people who are kind of in control of the
[4617.04 → 4621.84] priorities and people who are in control of funding if they had a better understanding of the problem i
[4621.84 → 4628.32] think they would make different choices I think in a large respect how out of date dependencies are
[4628.32 → 4632.72] is its invisible it's even invisible to the team a lot of times they just kind of like
[4632.72 → 4637.68] you know they pull in a package they start using it, and they move on, and you know it there's not
[4637.68 → 4642.72] really much to help them stay up to date and kind of keep aware of that that's starting to change a
[4642.72 → 4646.56] little bit with pack different package ecosystems I feel like NPM's doing a pretty good job with
[4646.56 → 4652.56] letting people know when things are out of date when they do a know a NPM install uh you know
[4652.56 → 4658.96] NPM outdated is a know a perfect tool set for folks, and it has perfect output, and you know
[4658.96 → 4664.08] and you know it's easy to read and I think more package ecosystems are starting to adopt that
[4664.80 → 4669.52] that strategy and that approach my hope is that that helps and kind of increase awareness
[4670.80 → 4674.96] I really do think it's interesting to see like how well the team has been doing at keeping up
[4675.52 → 4682.48] with that churn and obviously like because of supply chain attacks again like that that's what
[4682.48 → 4687.36] they're called, and the security ecosystem is applying its sorry Adam it's an it's a fun I don't think it's the right
[4687.36 → 4692.16] term, but it is that term so I'm cool with it um well and this is all in conversation because I was
[4692.16 → 4697.68] talking about web socket and how they secure the open source supply chain so we were like I'm like
[4698.80 → 4705.76] you get it so socket security you're talking about socket not web socket gosh I'm such a fool oh socket
[4705.76 → 4713.92] security socket okay suck anyway no worries strike that we'll fix it and um that out like Matt says
[4713.92 → 4720.32] the uh I'll stay in it so I can thank you for helping me out on that, so supply chain attacks are
[4720.32 → 4728.00] definitely a big risk, and you can have an upstream library that gets taken over by a nefarious actor
[4728.64 → 4734.48] and so seeing up with the latest and greatest all the time so just like if you're using the Pentagon
[4734.48 → 4739.36] yeah just merging those in blindly that might not be the best idea because you do make yourself
[4739.36 → 4745.84] vulnerable to some of those vulnerabilities totally you know at the same time you don't
[4745.84 → 4751.68] want to let yourself get months out of date right uh the where's the balance yeah because the with
[4751.68 → 4759.28] the Equifax breach from 2017 that was uh one Apache struts dependency on the date that they were attacked
[4760.32 → 4764.48] they were out of date by two months for the library that had the patch for that vulnerability
[4764.48 → 4770.08] so that the two-month win two-month window for that project and that was a very, very impactful
[4771.52 → 4776.00] you know vulnerability it was a very impactful event it affected a lot of people the freshness
[4776.64 → 4782.48] yeah of that library was stale by two months uh yes right when when you look at when you look
[4782.48 → 4786.48] at that particular vulnerability I don't know if all the vulnerabilities were patched in that release but
[4786.48 → 4793.04] I know that the vulnerability that they were ultimate ultimately exploited on was you know two months
[4793.04 → 4801.20] out of date so and and and I think a lot of it is a lot of teams don't make updating things a regular
[4801.20 → 4806.56] part of their practice it's it tends to be really challenging its it takes a lot of effort to upgrade
[4806.56 → 4811.12] some of these dependencies especially if they include breaking changes right a lot of times software
[4811.12 → 4816.56] systems are really tightly coupled to these dependencies so upgrading them is really non-trivial, and so I think
[4817.12 → 4822.08] you know kind of going back to like martin fowler has a quote where if something is difficult you need to
[4822.08 → 4828.64] do it more often so if is software teams got in the habit of updating dependencies more often and
[4828.64 → 4834.32] kind of doing it as a practice and really you know devoting time or even maybe devoting a team
[4834.32 → 4839.92] member whose job it is to stay on top of this stuff yeah than I think you know that could really help
[4839.92 → 4844.64] help turn things around and keep keeping projects healthier but on the other side the supply chain
[4844.64 → 4849.84] attacks like the event stream one etc yep those hit people who don't have their dependencies pinned to a
[4849.84 → 4854.40] version and their CI is just going to pull the latest exactly and so that's the other side that's
[4854.40 → 4860.72] too fresh yes you know so like what is the right balance it seems like unless you have a known
[4860.72 → 4868.32] vulnerability staying one minor release behind is actually a best practice yeah and once there is
[4868.32 → 4872.40] a known vulnerability now you got to get up to you know immediately to the latest I don't know that
[4872.40 → 4876.80] could be a perfect strategy yeah and yeah I think you know, and it also comes down to risk
[4876.80 → 4881.12] tolerance and different organizations have different levels of risk tolerance you know
[4882.00 → 4885.36] state you know and there are organizations that aren't interested in staying on the bleeding edge
[4885.36 → 4889.68] and I think there is a good argument to be made for if something's not broke then don't fix it just
[4889.68 → 4896.24] because it's old doesn't mean it's bad right um but i I do think that you do have these productivity
[4896.24 → 4901.20] impacts, and you do have these security impacts when you are working with older libraries and
[4901.20 → 4908.16] older versions of frameworks yeah well I mean hopefully these products will be a new breath
[4908.16 → 4912.96] new life into corgi bites yeah I think you know it'll be um a little bit of transformation you know kind
[4912.96 → 4920.88] of like um in the cycle of um you know growth and reinvention and rebirth and I think you
[4920.88 → 4928.32] know that will be you know part of the life cycle this you know we had when we were focused as a
[4928.32 → 4932.80] business on you know building small websites you know like building five page websites
[4932.80 → 4937.36] stuff like that you know that that business model didn't last very long and you kind of the business
[4937.36 → 4942.40] went into an incubation period and was reborn out of that you know this that might be what's
[4942.40 → 4947.12] about to happen again we'll see you never know that does make sense yeah I mean you got to evolve when
[4947.12 → 4952.80] when change happens resilience is change really essentially you got to change with the change that's
[4952.80 → 4959.12] right that wise man once said all right was that you maybe martin fowler I don't know
[4961.04 → 4965.12] well good luck on that change yeah good luck navigating it I appreciate that and the
[4965.12 → 4968.96] product direction I agree with jarred it does sound like the way to go because if you can give I think
[4968.96 → 4977.44] so to an executive in I don't know what time frame something that is authoritative and finite in terms of
[4977.44 → 4984.40] there is lack of freshness, or you're this far behind best practices or some sort of indicator
[4984.40 → 4991.44] that says I'm not hearing it from my developers who in quotes whine right or complain that i lovingly
[4991.44 → 4998.16] trust but really I need this authoritative thing that says hey get your stuff together yeah and trying
[4998.16 → 5005.84] trying to give you engineering teams a way to translate the data that the system is collecting in a
[5005.84 → 5011.52] way that can be easily consumed by their leadership so you know instead of you know having a graph
[5011.52 → 5018.24] with a bunch of data on a web page and then sending you know trying to get your manager
[5018.24 → 5024.16] to log into that instead like generate a PowerPoint deck and write something you can toss into an email
[5024.16 → 5028.40] and forward to somebody and in there can be a link to that dashboard like if somebody wants to
[5028.40 → 5032.56] see the dash here's our vulnerability score or something like that or here's our staleness factor
[5032.56 → 5037.60] right freshness factor or freshly factor or whatever it might be and that could actually be quite good
[5037.60 → 5044.88] at marketing too for you yeah you know because then it becomes maybe a race or a competition of
[5044.88 → 5053.76] sorts with executives or yeah CEO to CEO like hey what's your what's your freshness factor and then help
[5053.76 → 5058.48] you know even within like a organization that might have a portfolio of projects is there projects
[5058.48 → 5062.72] that are doing better than others what you now and then getting curious about the teams that are
[5062.72 → 5067.04] doing better what are they doing differently and is there knowledge that those teams might have
[5067.60 → 5072.56] which might make sense to share with other teams yeah good plan yeah man you should do it
[5072.56 → 5077.68] thanks working on it is just takes time building software it takes time it takes time even with
[5077.68 → 5082.80] like AI's help right it still takes time I can't just hit my fingers and say that's right hey uh hey
[5082.80 → 5087.84] hey GitHub copilot you know build this for me or he yaws code whisperer build this for me right
[5087.84 → 5092.48] you still gotta fix those bugs that it spits out at you that's right well thanks for stopping by
[5092.48 → 5096.40] Scott yeah appreciate you letting me uh chat you bet
[5100.08 → 5108.32] well the year is almost done 2024 is almost here you know it's its the end of a year, and it's that
[5108.32 → 5114.64] time you think man what's next right what's coming next what's next for me what's next for the world
[5114.64 → 5122.00] what's next for tech what's next for software and all the above well I do know what's next for this
[5122.00 → 5128.72] podcast I can say that there is an episode of friends coming out momentarily and then I can also
[5128.72 → 5136.64] say that next week there is an epic episode jarred and I are back for state of the log break master
[5136.64 → 5143.12] cylinder helped us up our game this year even more so than years beforehand where well I'll just I'll
[5143.12 → 5148.40] just save it for the episode let's just say you want to check it out it's the end of the year but
[5148.40 → 5154.88] we're going to be back next year more good stuff more good things and uh I hope you have a safe holiday
[5154.88 → 5161.60] enjoy your family, and it's also good to say thank you right thank you to you of course for listening
[5161.60 → 5168.72] this podcast thanks you to our plus subscribers, and then thank you to fast for supporting us all
[5168.72 → 5176.08] these years and then of course thank you to fly.io and our friends over there for supporting us all
[5176.08 → 5185.60] these years our friends at type sense our friends at century our new friends at neon and everyone in
[5185.60 → 5193.60] in between thank you and of course to the beat freak in residence break master cylinder
[5194.32 → 5200.80] those beats but hey we'll see you soon on friends we'll see you next week for
[5201.44 → 5206.72] state of the log, but that's it this show's done we'll see you very soon
[5215.60 → 5217.28] well
[5231.28 → 5232.88] you
