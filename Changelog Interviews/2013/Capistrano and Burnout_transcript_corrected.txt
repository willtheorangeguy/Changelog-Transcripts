[0.00 → 14.92] welcome back everyone this is the changelog we're a member supported blog podcast and weekly email
[14.92 → 19.94] that covers what's fresh and what's new in open source check out the blog at the changelog.com
[19.94 → 26.04] our past shows at five by five dot TV slash changelog and subscribe to our weekly email
[26.04 → 30.84] it's called the changelog weekly we ship it out every Saturday, and it covers everything that hits
[30.84 → 37.16] our open source radar you can subscribe at the changelog.com slash weekly this show is hosted by
[37.16 → 42.88] myself Adam static and also my partner crime Andrew Thorpe Andrew say hello how's it going
[42.88 → 48.82] I'm I'm perfect I think uh we had a joke in a previously recorded version of this that was
[48.82 → 52.94] really awesome that won't get told now and I'm kind of bummed about that just, just so you know
[52.94 → 60.56] don't worry no one needs to know no one needs to know but uh this is episode 110 and today's show
[60.56 → 66.88] is sponsored by two sponsors today I'm pretty happy about this digital ocean and top towel um top
[66.88 → 70.60] towel is one of our latest sponsors I'm going to tell you a bit more about them late in the show
[70.60 → 76.58] but real quick they connect startups businesses and organizations to a growing network of elite
[76.58 → 81.58] engineers around the world so stay tuned we'll tell you more about them, but digital ocean is a fan
[81.58 → 87.58] favourite they've been helping us uh for quite some time uh big supporters of open source big
[87.58 → 92.32] supporters of the changelog, but you know them you love them and today I want to tell you about their
[92.32 → 97.94] by the hour pricing plans a cool thing about digital ocean servers is that you can spin up a cloud server
[97.94 → 104.50] by the hour if you only need a server to test an app for a short while the smallest one costs just 0.7
[104.50 → 110.68] cents per hour that's right 0.7 cents per hour you get to put the servers for only as long as you need to
[110.68 → 115.32] and not pay any extra but if this is the first time you're hearing about digital ocean they're a
[115.32 → 119.66] simple cloud hosting provider they're dedicated to offering the most intuitive way to spin up a cloud
[119.66 → 125.28] server you can create a cloud server in 55 seconds and pricing plans are at five bucks per month or by
[125.28 → 132.84] the hour 0.7 cents per hour and uh you get 512 of ram 20 gigs of SSD one CPU one terabyte transfer
[132.84 → 138.10] they have data centres in Amsterdam New York and San Francisco, and you can try them out today
[138.10 → 145.22] for free that's right for free use the code the changelog October when you sign up it's the changelog
[145.22 → 150.88] October that'll get you ten dollars of hosting credit which is equal to two months free spin up your
[150.88 → 157.98] cloud server today at digitalocean.com and lee hamlet is joining us today or is it hamlet
[157.98 → 165.10] it's hamley I was right there you go awesome big score lee you are joining us you are the
[165.10 → 171.64] maintainer of Cristiano we got a fun-filled show lineup so Andrew just take us away bud yeah so once
[171.64 → 176.62] again we're joined with lee hamlet uh the maintainer of Cristiano has been maintaining the project for
[176.62 → 184.04] quite some time now um while I think everybody well maybe not everybody a lot of people in open source
[184.04 → 189.80] obviously have heard of Cristiano have you if not used it um but I'm sure there are plenty of people
[189.80 → 195.30] out there uh that have never heard of it or that have not used it so lee why don't you give us an
[195.30 → 199.94] introduction to who you are you know kind of where you come from and then a little bit about Cristiano
[199.94 → 207.94] what it is and um some history yeah so absolutely my um personal kind of background as
[207.94 → 214.50] self-taught jack of all trades developer um started my early career writing horrible pearl stuff and
[214.50 → 219.18] converting a lot of that stuff to Ruby on Rails realizing things were nicer on the other side of the
[219.18 → 224.48] fence and that's when I got stuck into ruby in general and um the very early version of rails i
[224.48 → 230.42] think version two was pretty new when I got started um around the same time we were looking for a way to
[230.42 → 235.68] get these apps deployed of course deploying rails hurt a lot more than deploying pearl or PHP or some of
[235.68 → 242.78] the other stuff and uh back in what I guess 2006 2007 or something Cristiano was pretty new
[242.78 → 249.12] didn't have a great deal of documentation around, and we were really keen on using it so as we began
[249.12 → 254.88] to use it I began to write documentation and handbooks and answering questions on mailing lists
[254.88 → 263.16] and everything else and um eventually the original author jams buck who worked for 37 signals had a
[263.16 → 267.98] kind of breakdown burnout I don't know what exactly, but he wanted to spend more time with his family
[267.98 → 274.58] and was looking for someone to take over maintainer ship so that was me as a not very experienced
[274.58 → 282.42] ruby developer uh maintaining kind of infant project back then and um yeah Cristiano just
[282.42 → 287.40] kind of snowballed from there the following version of rails had it as a default in the gem file a lot
[287.40 → 292.64] more people got introduced to it from there, and it's always been it's always had a very close
[292.64 → 297.08] relationship with rails and even in version four Cristiano standing right there in the gem file is the
[297.08 → 303.04] kind of recommended way to go if you're going to deploy things um for anyone who doesn't know
[303.04 → 308.18] what Cristiano is about which I guess is unlikely if you're in the ruby world it's
[308.18 → 316.76] it's its a ruby DSL for specifying tasks to run uh on one or more remote servers specifically
[316.76 → 322.54] targeted at doing application level deployment not really server provisioning or that kind of stuff
[322.54 → 328.12] but specifically making a directory on the server for the current release synchronizing everything with
[328.12 → 332.96] git checking it out linking shared files that shouldn't be checked in like database configs and
[332.96 → 340.22] whatever else and um in the end restarting everything uh it's always been very, very tied
[340.22 → 346.88] to rails and very, very tied to ruby and um it's been rewritten recently uh was released I don't know
[346.88 → 352.06] something like 10 weeks ago now maybe a little bit less and um it's been rewritten from the ground up
[352.06 → 357.40] so that it could be useful for other frameworks particularly PHP there are a lot of guys deploying
[357.40 → 364.66] WordPress with Cristiano which is kind of funny yeah that is nice that's a little yeah that's unique
[364.66 → 368.98] that's cool to hear i actually I wasn't aware of that maybe we can get to get into that a little bit
[368.98 → 375.70] but um Cristiano you mentioned kind of has a had a relatively big change and a lot of stuff came about
[375.70 → 381.80] this I think you know with um the post that you wrote and uh the release announcement came back in
[381.80 → 387.34] June so Cristiano version 3 released 10 weeks ago uh why don't you kind of give us a rundown of
[387.34 → 392.74] um the major differences and that was the first major release in about five years right so um
[392.74 → 397.44] huge release and why don't you kind of give us a rundown of what was Cristiano version 3 and
[397.44 → 403.88] why did uh why did it why was it five years between the major releases uh-huh so one of the big reasons
[403.88 → 409.66] that Cristiano went unchanged for so long was that it basically worked for most people and there were a lot
[409.66 → 416.88] of situations making small changes to Cristiano itself where all of a sudden people's deployments
[416.88 → 421.94] were breaking sites were falling offline, and it was because of very trivial things uh such as we
[421.94 → 427.70] changed some shell escaping to fix Unicode issues that were reported by German users and that broke
[427.70 → 432.84] shell escaping and people relying on having spaces and path names deploying to Windows servers with
[432.84 → 439.18] sig win and all kinds of other weird stuff so it seemed like whichever way we went with version 2
[439.18 → 447.80] we couldn't make everyone happy and when I say we's mostly myself and a few people who've come
[447.80 → 454.00] and gone over the years um I don't know whether that's because I'm not very hospitable as a host or
[454.00 → 460.22] whether it's really just not very much fun working on this stuff and um of course when Cristiano was
[460.22 → 466.72] written uh rake existed but was very immature in order to write Cristiano James also had to write
[466.72 → 475.16] net sh in order to actually be able to speak the ssh protocol and he also wrote SCP and FDP drivers
[475.16 → 484.26] with pure ruby and um well all of that stuff's really complex and there was no easy way to change
[484.26 → 490.12] things there was no culture of gem files or bundler or any of this kind of stuff until fairly recently i
[490.12 → 495.72] would say the last 18 months to two years it's become the norm for people to kind of lock their
[495.72 → 500.68] dependencies Cristiano starting to be that thing that people put in their gem file now and
[500.68 → 507.82] the kind of whole structure has been put in place by the community which has allowed me to make
[507.82 → 514.54] a big break and say look this has been hurting for way too long and I need to make a big break and
[514.54 → 519.26] actually we were able to cut Cristiano down from thousands of lines of code and now I think it's
[519.26 → 525.36] about I don't know 1500 maybe and that's because we're leaning on rake we're leaning on a driver
[525.36 → 532.10] called ssh kit which I extracted from it's a slightly nicer library of a net ssh, and it's a lot more
[532.10 → 538.68] modular now it's a lot simpler and one of the biggest changes is that it now no longer ships with any rails
[538.68 → 544.76] assumptions so the rails support has been moved out to a Cristiano rails gem and that itself is
[544.76 → 550.92] split into two pieces uh migrations and uh assets which was a big thing that always frustrated me
[550.92 → 558.02] because I will not use the rails' asset pipeline so yeah I've read your uh laments about the asset
[558.02 → 562.76] pipeline many times now so that's that's definitely not something that you try and keep secret
[562.76 → 569.50] uh no I mean i I have to be careful because one of the things that um kind of drove my burnout was
[569.50 → 574.86] people being disrespectful towards Cristiano in the very early days some guys came out with a tool
[574.86 → 581.62] called Vlad and Vlad was kind of git push base deployment as far as I remember and their tagline
[581.62 → 588.44] was Vlad sucks less than Cristiano and yeah uh you know it's cool to poke fun at projects which don't
[588.44 → 593.64] really agree with what you're trying to do but uh you know there's years and years and years of work
[593.64 → 597.42] gone into pretty much everything we use in open source, and we have to remember that
[597.42 → 605.02] is that part of the poisonous people sapping your energy as you have said is that part
[605.02 → 613.52] of it or is it something else altogether um I would say um I don't I don't want to kind of overstate
[613.52 → 620.30] how difficult it is or understate how difficult it is but I think Cristiano sits right on the
[620.30 → 625.48] boundary where things get complicated rails is very very very friendly very beginner-friendly
[625.48 → 630.90] um I think it's a bit less beginner-friendly than it has been in the past, but it's still fairly easy
[630.90 → 636.56] for guys to throw together a blog in a couple of days with very little programming experience and
[636.56 → 641.72] then of course everyone says hey do you know this thing Cristiano you can deploy in minutes it's
[641.72 → 648.24] super easy, and then they slam into this incredible learning curve where they have to understand
[648.24 → 655.14] git, and they have to understand ssh keys, and they also have to understand Unix permissions and
[655.14 → 662.14] file mode creation and what the executable bit means in different directories and all of a sudden they
[662.14 → 669.74] don't understand why sudo doesn't work why stuff is working in ssh, and it's not working Cristiano and
[669.74 → 677.54] all of this stuff is incredibly complex and stuff that seasons developers we learn that stuff
[677.54 → 684.26] bit by bit over years and years and years and years and years and I think if you've been on a good run
[684.26 → 688.66] you've just built your tiny little toy application you're having a great time, and then you need to
[688.66 → 694.26] deploy it you hit all of these incredible issues and the first place you go is GitHub, and you open
[694.26 → 701.84] in issues saying pretty much all of them that we see uh hey it doesn't work for me, and they never tell
[701.84 → 706.38] you, and they don't have these guys they don't know that they're not telling you the most important thing
[706.38 → 714.62] which is that they installed ruby uh from aptitude, and it needs pseudo access to it to do anything
[714.62 → 720.04] and guys who are new to this stuff they have no idea that that stuff's important they don't know
[720.04 → 727.10] that they don't know, and we have to kind of triage those guys which I would say is something like
[727.10 → 734.46] 60 or 70 percent of every support query we get is somebody who just didn't know that whatever you
[734.46 → 742.40] can't use RVM or Cristiano doesn't behave the same way as an interactive ssh or I don't know
[742.40 → 747.80] specifically another issue we run into all the time is ssh keys and people say hey well I can push and
[747.80 → 753.26] pull from GitHub why do I need another set of keys for the server, and you can tell them hey you know
[753.26 → 759.38] you don't you can use agent forwarding, or you can say just look go on the server generate another key
[759.38 → 767.80] put it on GitHub it's a you mentioned at one point and uh I don't remember where exactly I read
[767.80 → 772.50] it at, but you said the future of deployments was in like the know platform as a service type of
[772.50 → 777.66] thing and um how do you feel I mean just kind of hearing what you're saying I think there's a lot
[777.66 → 784.70] of um I mean yeah I've spoken to you obviously now a couple of times and I think that you have a passion
[784.70 → 789.66] for open source and a relatively positive outlook but you obviously have uh some things that have
[789.66 → 793.44] kind of burned you how do you feel about like the Heroku of the world that do just like the one
[793.44 → 799.78] step get deployments and stuff like that for those types of users yeah I mean i uh I have to say i
[799.78 → 805.46] really like Heroku the stuff that they've built is incredible and the kind of engineering behind
[805.46 → 810.02] that platform is just amazing and I have the feeling that all the guys who work there have
[810.02 → 814.96] an amazing job, and they love every minute of it that's just rainbows and unicorns in my head because
[814.96 → 820.30] everything they're doing is the stuff that I wish everybody could do because it just looks cool
[820.30 → 830.22] um, but it's another black box and I would say for the most part in our industry black boxes are
[830.22 → 836.72] totally okay you know there's most of us can get by with active record and just treat the database as
[836.72 → 842.24] a black box and trust that it does what it says it's going to do and if it doesn't then we're really in
[842.24 → 849.98] trouble and I work on kind of bigger applications um I'm a consultant day-to-day and some of my
[849.98 → 857.58] clients have got kind of 350 big incredibly powerful servers and incredibly powerful you know
[857.58 → 865.68] multi-data centre failover situation setups and for that kind of stuff Heroku is never going to be the
[865.68 → 872.46] correct solution but right for you know like the guys from rap genius I think as far as I know it's a
[872.46 → 877.30] fairly typical rails app they're paying Heroku something incredible like twenty thousand dollars a
[877.30 → 882.40] month or something was on hacker news, and it works for them, it's a black box they have the money they
[882.40 → 891.12] can afford it so it's perfect, and the black box isn't a big problem and a black box that just works
[891.12 → 897.24] is much better than a kind of digital ocean sorry to pick on your sponsor but their VMS are great
[897.24 → 904.10] but you have to know what you're doing with them and that's kind of where everything falls down, and it's
[904.10 → 908.46] the same with anything if you're going to use a tool you have to at least understand basically how
[908.46 → 913.50] it works and Heroku if you don't mind I can plug one thing real quick just on their behalf they are
[913.50 → 917.94] doing some really cool stuff around helping the community document that stuff too like they have
[917.94 → 922.16] this community centre and they obviously they know they know that I'm not like sticking up for
[922.16 → 927.26] them but just, just so it's clear like they want to help educate so they're like totally on
[927.26 → 931.26] board with what you're talking about like it's for some people you don't know like I went in and I was
[931.26 → 935.90] hacking on a VM with docker on it and I messed around and I played with it but how I got there
[935.90 → 940.48] because I'm not at DevOps how I got there was reading a tutorial, but it was very thoroughly done
[940.48 → 945.10] and they pay 50 bucks for you to do it so they do want to like help people get to the understanding
[945.10 → 951.54] too yeah and I think that's really important and that's um that comes back to kind of why there's
[951.54 → 957.04] been no big issues uh big changes rather on castrato over the last few years is that I was focusing
[957.04 → 964.64] kind of wastefully it seems on education and trying to tell like everybody who came along all
[964.64 → 969.08] the hundreds of them look this is what you're doing wrong this is how it works in theory yes I know you
[969.08 → 974.58] think the tilde should be expanded, but you know that magic thing that happens when you type tilde and
[974.58 → 981.16] push tab that it is not Linux that's your shell and your shell's not there when you're using capstan
[981.16 → 986.70] whatever else um all kinds of weird issues like that, and it really comes down to education and
[986.70 → 992.14] there will be the guys who have the time and the energy to learn and there'll be the guys who don't
[992.14 → 998.44] and yeah it's kind of time is money or money is time and if you have the money I think Heroku is pretty
[998.44 → 1005.34] expensive, and it's a black box go ahead and use it and if you really need a tool, and you know what
[1005.34 → 1011.68] you're doing then go ahead read a tutorial use your knowledge anyway and build something around
[1011.68 → 1017.44] capstan I mean it's its really a tricky tool because we try really, really hard to make sure
[1017.44 → 1024.12] that whatever for example the RVM integration does its best to figure out which weird way you installed
[1024.12 → 1032.38] RVM and make sure everything just works, but we can't do it perfectly, and it's these edges
[1032.38 → 1037.70] where people have fallen down weird cracks and edge cases that you never imagined
[1037.70 → 1044.02] those are the vocal minority, and they're the guys you hear from they're the guys complaining that
[1044.02 → 1050.30] whatever they installed RVM via aptitude as well because they read it on a tutorial somewhere and
[1050.30 → 1057.18] the tutorial was from 2008, and you know they don't know what they're doing wrong they're following
[1057.18 → 1062.36] a tutorial that somebody told them about, or they found by via Google, and they're just
[1062.36 → 1070.20] trying to ship an app, and unfortunately you very rarely hear from the guys who are being
[1070.20 → 1076.18] successful, and it wasn't at all that's a bummer man they should speak up you know hop in there and
[1076.18 → 1081.76] create a praise issue right yeah well you one thing that, and we'll get into this one thing that I think
[1081.76 → 1087.94] uh people tend to do is like if you look at the issues on like a project like Cristiano and I think
[1087.94 → 1092.58] this is the frustrating thing, and maybe you can speak to it but like somebody will experience
[1092.58 → 1097.78] something maybe it's a bug maybe it's you know them not understanding what's going on or a feature
[1097.78 → 1103.80] that Cristiano just is never going to like even attempt to solve for you know any number of reasons right
[1103.80 → 1109.14] there's like infinite amounts of chances and somebody will come and report it uh with very
[1109.14 → 1114.94] little you know they give you very little information they give you very little um you know like context and all that
[1114.94 → 1121.70] but then like a hundred people will come and comment plus one and that's it so like it's a ton of
[1121.70 → 1125.46] pressure for the person that's maintaining this be like yeah this is also affecting me this is
[1125.46 → 1129.04] affecting me, and it's like the whole crowd just starts raising their hand this is affecting me
[1129.04 → 1134.34] but nobody's giving you context or information on how to solve it and oh by the way it's an open
[1134.34 → 1138.42] source project so if it's affecting this many people somebody can step up and attempt to solve it
[1138.42 → 1144.28] in a way that you know follows the contribution guidelines and to me when I see as a consumer
[1144.28 → 1148.82] of open source when I go to a project and I see something like that, and it's you know it's not just
[1148.82 → 1153.56] Cristiano it's all over the place it almost makes me sad because I'm like well I wish I had tons
[1153.56 → 1157.76] of time when I could jump in and try and help solve these problems you know that aren't affecting
[1157.76 → 1162.70] me but like with this you know one project that I just happen to just be perusing through the
[1162.70 → 1169.06] issues just to see what's going on it's like why don't more people even make an effort or an attempt
[1169.06 → 1173.26] to try and solve the problem what do you think I mean how do you feel when you see those new issues
[1173.26 → 1178.72] come in with just tons of plus ones on them yeah I mean that's um that's been a big driver behind
[1178.72 → 1187.04] uh the rewrite actually is prior to the rebuild um Cristiano was incredibly complicated we had this
[1187.04 → 1193.48] weird kind of automatic variable lookup with fetch and set with defaults and lambdas and everything
[1193.48 → 1198.80] else and that was really complex we had some really complex concurrency code, and we also had a really
[1198.80 → 1208.20] complex self-baked DSL which also was kind of weird and also internally most of the stuff inside
[1208.20 → 1214.24] Cristiano used load instead of require and historically there were some good reasons for that but it also
[1214.24 → 1220.32] just made things really weird so whenever somebody came to contribute there were basically no tests
[1220.32 → 1227.02] the code was incredibly complex not very well organized by modern standards I think when it was
[1227.02 → 1233.50] originally architected there was no kind of best practices around how to structure a gem how to test
[1233.50 → 1240.76] it and everything else and James did a great job really so it was you know it's a five or maybe six or
[1240.76 → 1246.16] seven-year-old code base so it's really no wonder that it was ready to be rewritten and a big driver
[1246.16 → 1253.76] behind the rewrite was to keep it as small as possible and use stuff which people were familiar with so
[1253.76 → 1262.08] now as I say Cristiano is on top of ssh kit and ssh kit lies on top of net ssh which is the
[1262.08 → 1267.08] the low level ruby driver, and it's kind of awkward because you have to do stream handling and error handling
[1267.08 → 1273.76] event stuff, so ssh kit is you can you know you can connect to a server and run something in one line
[1273.76 → 1278.42] of code you don't have to worry how it works but if you do need to see how it works the whole of ssh
[1278.42 → 1285.62] kits like 700 lines of code um and Cristiano is just the synchronization stuff on top of that so it
[1285.62 → 1292.08] brings the default uh tasks you need for rails it brings some structure like uh setup tear down
[1292.08 → 1298.78] hooks for various places in the deployment and as well as I said earlier Cristiano is also tiny
[1298.78 → 1305.44] including all the test cases it's like way less than 2 000 lines of code I think and so to kind of
[1305.44 → 1312.12] mitigate this barrier to entry that people have contributing to complex projects version 3 is
[1312.12 → 1320.02] really designed to be approachable and I don't know if it's a general kind of fear of getting involved
[1320.02 → 1326.00] in projects, but we haven't seen really the level of adoption in new contributors that we would
[1326.00 → 1330.70] have liked we've we've picked up a couple of guys who are doing amazing work on the plugins for RVM
[1330.70 → 1337.86] run from ch ruby and also bundler and rails they're getting tons of pull requests and tons of little fixes
[1337.86 → 1344.06] and I think that's in part because it's now so much simpler and uh even ssh kit is getting fixes as well
[1344.06 → 1350.86] but there's no real big changes being pushed for Cristiano um one guy is doing some great work in
[1350.86 → 1354.66] fact I don't want to name names but everybody who's contributing is doing a great job and
[1354.66 → 1361.60] the level of contribution has definitely increased but also the number of kind of silly issues has
[1361.60 → 1366.46] increased as well uh which is probably a documentation issue on my part because there's a lot of people
[1366.46 → 1369.56] showing up saying hey I did this in version two, and now it doesn't work in version three
[1369.56 → 1376.12] yeah right it's a new version we tried our best did you maybe consider reading the documentation
[1376.12 → 1382.04] and they always say hey no I just expected it to work so I think go to the semantic versioning website
[1382.04 → 1386.94] right I mean you're always going to run into those guys, and we've had an incredible number of people
[1386.94 → 1392.00] coming along saying hey why did you rewrite version two was working perfectly for me now everything's
[1392.00 → 1398.80] broken, and you really have to bite your tongue with those guys because you know just whatever stick with
[1398.80 → 1405.68] version two you know yeah oh Cristiano was written for you don't you remember right now you talked
[1405.68 → 1413.08] about um I think you said you know you brought up the RBM and RVM uh ch ruby and stuff I've heard I've
[1413.08 → 1417.18] seen and i, and we'll get into a little bit of the burnout stuff but I've seen you say that one of the
[1417.18 → 1423.62] major um problems you faced in this project and just in general with ruby is the lack of
[1423.62 → 1430.28] standardization around things like um uh I mean the know the ruby version management stuff like
[1430.28 → 1437.92] that ruby gems like it was an it's its an it's great work it's a know kind of it solved a lot
[1437.92 → 1442.30] of problems, but it maybe wasn't you know it's not very standard and ruby failed to kind of really lean
[1442.30 → 1448.24] on like standards in some of these areas um kind of can you kind of speak to that a little bit and
[1448.24 → 1456.68] kind of expand yeah I mean um RBM and RVM are two great examples because one of them was built to be
[1456.68 → 1462.46] tiny and do as little as possible, and the other one was built to be as comprehensive and all things
[1462.46 → 1472.70] to all people as each other and they both basically fulfill the same job um and again i I'm very keen to
[1472.70 → 1477.50] stress they're both really cool projects and we're in contact with the maintainers from both
[1477.50 → 1485.28] projects to help keep the Cristiano integration tight and I think the biggest thing I mean Cristiano
[1485.28 → 1491.52] isn't magic right I mean the basic premise is that you have a release that's time stamped or
[1491.52 → 1495.36] individual somehow that you can roll back to sure you could do the same thing with git but
[1495.36 → 1501.00] the main thing is the current sim link the shared directory and linking everything so the biggest
[1501.00 → 1506.48] win from Cristiano is the best practice, and you can have this Cristiano style deploy
[1506.48 → 1514.26] with chef or puppet or Ansible or salt stack or any of these other tools, but the best thing is we've
[1514.26 → 1521.72] all pretty much agreed on how you should deploy a rails app pretty much and if you go a level lower
[1521.72 → 1527.20] and you start to speak about kind of interpreters and ruby environments and databases and everything
[1527.20 → 1533.34] else the people who work at that level have also kind of standardized if you use red hat then it's
[1533.34 → 1540.88] yum if you use Ubuntu or Debian then it's aptitude or if you know is we have solutions for this stuff
[1540.88 → 1547.36] already in production environments and I think in a lot of small companies or a lot of one-man shops
[1547.36 → 1552.44] they've written the application they're a developer they're just not interested in the server and there's
[1552.44 → 1559.06] an open source project promising to make all the problems go away and so people naturally gravitate
[1559.06 → 1567.44] towards those things and that's okay, but it's not the way the operating system is expecting that to
[1567.44 → 1573.52] work it's not the way your shell is expecting that to work its kind of a hack because it's relying on
[1573.52 → 1584.28] scripting sourcing dot files and environment files, and it's kind of very unfunny and I know that term
[1584.28 → 1591.72] means different things to different people but um yeah I mean it's its a nice workaround in a lot
[1591.72 → 1597.02] of ways and in a lot of ways it's not i I'm actually a big fan of the RVM binary wrappers
[1597.02 → 1602.90] because that speaks to me a little bit more as like as a Unix guy I mean you're modifying the path
[1602.90 → 1610.00] there's a shim executable which just makes things work, and you don't really have to worry about shell
[1610.00 → 1615.42] state having the right stuff sourced it's its just about the path and everything else is irrelevant
[1615.42 → 1621.54] and that seems to me to be the best way to do things but I've been around servers for like 15
[1621.54 → 1629.10] years now so you know I have a lot more history in that area than somebody that's maybe just going
[1629.10 → 1633.30] through their first getting started with rails book and then wanting to put something online so
[1633.30 → 1642.00] it's difficult because we try and support most of the same use cases, but you know we're never going
[1642.00 → 1649.28] to have 100 coverage and in fact speaking about edge cases we actually have one guy who's contributed
[1649.28 → 1656.96] a fix for ssh kit, and he's deploying from Polaris which is weird anyway um onto a Windows machine and
[1656.96 → 1662.94] his Windows machine is running PHP WordPress I don't know what web server he's using, but he's running
[1662.94 → 1668.06] sig win specifically so that he can have an ssh server specifically so that he can deploy with
[1668.06 → 1674.26] Cristiano and that's got to be the farthest out use case I've ever had you know, and it works for him
[1674.26 → 1680.76] and that's amazing work yeah yeah well lets uh let's take just a minute and pause give our
[1680.76 → 1686.90] our sponsor top towel a shout-out they'll be sponsoring the show for the next month uh gotta give
[1686.90 → 1695.08] a huge shot I mean i have to admit i if no one has heard of top towel, and it's spelled t-o-p-t-a-l top
[1695.08 → 1699.86] towel like it's in top talent uh I had a chance to kind of meet up with our co-founder and CTO Brendan
[1699.86 → 1706.18] and I was just at first I was a little skeptical I wasn't sure what to expect um uh but Brandon helped
[1706.18 → 1709.60] me understand who they are what their mission is and i have to say these guys are the real deal they're
[1709.60 → 1714.60] they're engineers from top to bottom they're not uh they're they're non they're not non-technical
[1714.60 → 1718.52] recruiters trying to your know for lack of better terms pimp developers they're a network of
[1718.52 → 1723.82] engineers who work with some awesome clients and I was kind of surprised too Andrew because we linked
[1723.82 → 1728.98] out to them uh to their engineering blog recently that we had a post explaining python implementations
[1728.98 → 1733.68] that IAN wrote and uh so they've got an awesome blog to go with it but for those of you out there
[1733.68 → 1739.30] who are freelancing or for those of you out there who like to who would like to test freelancing or even
[1739.30 → 1744.32] try out a no risk freelance like project while maintaining your full-time position you know
[1744.32 → 1750.06] there are a lot of twitter bios I read that that say I do x by day and do x by night and that x by
[1750.06 → 1754.92] night might be like meteor node.js or rails or whatever and if you want to do that that by night
[1754.92 → 1759.38] thing uh you got to check out top towel uh you can work on special projects with companies like
[1759.38 → 1764.54] Airbnb RC audio you could do it remotely on a beach Andrew I know you're a fan of that
[1764.54 → 1772.54] or anywhere in the world on many beaches yeah i know you actually have so um and many others
[1772.54 → 1777.40] they're they got a very high touch very close relationship with these types of companies
[1777.40 → 1784.24] um head to top towel.com slash developer right now click on join the best and when I say join the best
[1784.24 → 1790.46] they literally mean join the best because they want their clients to work with only the best
[1790.46 → 1797.06] senior engineers that are smart enthusiastic and driven uh not just yes people Andrew I know you and
[1797.06 → 1801.64] i both kind of don't really care for yes people but uh they want you to be able to say no if you're
[1801.64 → 1806.38] working on a project, and they're doing something silly um you know you have to say hey this is a bad
[1806.38 → 1810.54] decision they want people to work with them that are like this and because they want the
[1810.54 → 1814.92] best of their clients they've got a well-thought-out four-stage screening process that begins with
[1814.92 → 1821.18] something very personal a Skype conversation face-to-face the call includes um I'm sorry the form front
[1821.18 → 1826.24] end from front to from front to back the entire screening process includes an English speaking test a
[1826.24 → 1832.78] personality test uh timed algorithm test technical interviews with core top towel engineers as well
[1832.78 → 1836.86] as a test project but once you've made it through the screening process the sky's the limit and if
[1836.86 → 1842.06] you think you have what it takes head to top.com slash developer right now tell them the changelog
[1842.06 → 1846.76] sent you, and you will be well taken care of uh and do me a favour too I want to get feedback from
[1846.76 → 1851.58] those of you who try this out um and you if you're going there, and you're going to apply to send me an
[1851.58 → 1856.22] email Adam at the changelog.com let me know what your feedback is and what your experience is
[1856.22 → 1859.72] because we're really excited about working with top towel, and we want you to have the best experience
[1859.72 → 1865.92] possible but uh go to top towel.com slash developer that's t-o-p-t-a-l.com slash developer
[1865.92 → 1873.98] to get started and apply and uh Andrew I know you got some uh good questions waiting for lease I'll give
[1873.98 → 1880.34] it back to you yeah so you talked a little bit about the uh version management um things like
[1880.34 → 1885.42] that when you are a little bit earlier in the show you brought up the Vlad uh Vlad the deployed I think
[1885.42 → 1891.46] is what it was called it'll play on Vlad the impaler but um glad the deployed and their tagline was uh
[1891.46 → 1898.72] it sucks less than capstan I remember a few years ago when RBM first came out Wayne from RVM this is
[1898.72 → 1905.86] hard to say RV when RBM came out Wayne Seguin from RVM uh kind of tongue twister yeah kind of freaked out
[1905.86 → 1911.64] a little bit you know maybe it was due to some back and forth and it was like you know he'd put all
[1911.64 → 1916.94] this work into RVM and then when RBM came out a lot of people were saying oh finally because RVM
[1916.94 → 1924.22] sucks so bad as if like you know like RVM was just it came with ruby and it was no, no it was
[1924.22 → 1928.74] like robots that built it and no time was put into it so he got you know real upset about that and
[1928.74 → 1933.18] there was just some drama that went back and forth when Vlad came out sounds like it was kind of the
[1933.18 → 1937.78] same for you did you feel the same way at the time that Wayne did maybe like were there any thoughts
[1937.78 → 1941.26] in your head like ah screw it I'm done with Cristiano that you know people whatever forget
[1941.26 → 1947.32] it moves on yeah I mean that's definitely um you know that thought definitely runs through your head
[1947.32 → 1952.80] even if it's only for a split second there's um actually a book that was given to me by a colleague
[1952.80 → 1958.20] way back when that actually happened called where's my cheese uh Andrew if you're out there probably you
[1958.20 → 1965.10] remember it uh, uh he well the author of the book basically talks about how there's kind of two ways
[1965.10 → 1970.14] to approach the situation and whether it be your cheese whatever that means in your life and
[1970.14 → 1973.88] somebody comes along and moves it or takes it away from you, and you can either react by
[1973.88 → 1980.40] like upping your game going and finding something new or just being bitter that somebody took what
[1980.40 → 1986.72] you had away from you and I think you mean who moved my cheese right is that the name of it
[1986.72 → 1993.26] somewhere right um it's definitely worth a read I mean it's like what 20 pages long or something
[1993.26 → 1997.32] it's tiny you absolutely have to read this book any person in life has to read this book
[1997.32 → 2004.86] yeah right for sure and um and that's a kind of natural reaction is to be bitter that somebody
[2004.86 → 2009.84] is so disappointed with your tool that they wrote their own, and then you say wait hold on I'm a hacker
[2009.84 → 2015.20] that's pretty much what I do every day right I mean that's why Cristiano exists because whatever
[2015.20 → 2021.26] bash scripting sucked or Cristiano exists because there was no passenger mod rails back then or
[2021.26 → 2027.56] you know there's a bunch of stuff that we replace every day you know people switch to Regis because
[2027.56 → 2034.24] Postgres sequel isn't good enough on key value store stuff or whatever and if it's not a winner
[2034.24 → 2040.04] takes all game, but you do have to show respect for the other people in your space I mean
[2040.04 → 2046.72] it's kind of a big battle it's not even a battle because they solve different use cases but between
[2046.72 → 2053.16] chef and puppet you know DevOps guys love to argue about which is better, but the point is they both
[2053.16 → 2061.06] suck in their own special ways, and they're both amazing so it's its a really tough one um I do have
[2061.06 → 2065.82] a particular bone to pick with any project that calls another project out by name and says it sucks
[2065.82 → 2073.96] less than that other thing yeah um but on the other hand do that yeah exactly, and it's a lack of respect
[2073.96 → 2081.60] and that's that's what really sucks because the guy who's writing the new one has no expectations he can
[2081.60 → 2088.16] write whatever he wants and in the position of kind of being in the dominant space you're you're dealing
[2088.16 → 2093.56] with people all day every day who are using this stuff who rely on it companies who are built around it
[2093.56 → 2100.52] in the case of early engine yard and Cristiano uh, and you're kind of most of the work I do on
[2100.52 → 2106.44] Cristiano now is community support mailing list support kind of triaging bug stuff I don't write
[2106.44 → 2112.08] code anymore which is okay um because the project's moving in the right direction and I have some great
[2112.08 → 2121.20] contributors now um and that's fine and speaking about RVM actually I have to mention it was announced
[2121.20 → 2125.54] today I don't know when it was exactly, but it was on hacker news today that engine yard are
[2125.54 → 2132.76] discontinuing their sponsorship of RVM and because of that or at least related to that the maintainer
[2132.76 → 2138.60] of RVM is using I don't know which uh fundraising self-starting platform it is, but he's trying to
[2138.60 → 2146.04] raise money to rewrite RVM and if you use RVM if you had benefit out of it then you should definitely
[2146.04 → 2150.78] support that isn't it didn't they just drop they just dropped support for robins and I thought I was
[2150.78 → 2156.02] thinking that's a couple of weeks old no that's that is new so that's RVM Michael pilot recently
[2156.02 → 2161.32] that's that's uh that's a bummer we'll, we'll uh Michael if you're listening we'll do whatever we
[2161.32 → 2167.70] can to help you out man yeah well you yeah I mean I don't know I look at something like
[2167.70 → 2173.46] Vlad and and and Cristiano specifically I mean what did deployment look like before Cristiano right
[2173.46 → 2178.16] I mean you kind of mentioned it like it sucked to deploy rails applications early on
[2178.16 → 2184.18] and so Cristiano comes out solves the problem with kind of no map right I mean there 's's
[2184.18 → 2188.66] just you're you're kind of in a cave by yourself trying to figure out how to solve this problem that
[2188.66 → 2194.00] that like everybody's having, but nobody has a solution to so sure you have your shortcomings and
[2194.00 → 2199.16] and fail you know failures and over the years you can kind of learn like you said you get stuck
[2199.16 → 2204.58] almost like this is not the ideal way to solve this problem but so many people are relying on this
[2204.58 → 2208.78] that we can't just up and pull the rug out from under them and change everything so somebody new
[2208.78 → 2212.60] comes along, and they're like oh hey yeah like you said we have no expectations we can do whatever we
[2212.60 → 2219.14] want so, and we have all the have a map now right we see the solution we see the problems and the
[2219.14 → 2225.44] successes so we can bring in the successes solve the problems without anyone blaming us and then say
[2225.44 → 2230.04] hey look how much better we are than them and to me, I think like you said that's a lack of respect but
[2230.04 → 2235.24] but more than that it's a lack of like even understanding that without the person that
[2235.24 → 2240.86] you're saying that they suck without that person you would either not be able to solve the problem
[2240.86 → 2245.62] at all, or you would have the exact same growing pains and problems that they had in the first place
[2245.62 → 2252.26] yeah right I mean at least the point is that you um you have a solution that sucks but at least you
[2252.26 → 2259.20] have a solution right and so anyway it's its a whole bigger issue about kind of how people
[2259.20 → 2266.14] I think it's a question about quality that we expect from open source um which is just incredible
[2266.14 → 2271.20] now I think we have higher demands from open source than we do of commercial software because open
[2271.20 → 2278.90] source is so good for the most part and uh it's a kind of its something about expectation management and
[2278.90 → 2287.26] and just understanding what's reasonable as I said I think the biggest magic about Cristiano isn't
[2287.26 → 2291.84] the code it's not the way it's implemented or the cool stuff I did with threading or anything else it's
[2291.84 → 2297.58] it's purely to say look this is pretty much if you're a contractor if you're a rails' developer
[2297.58 → 2304.34] if something happens, and you're the guy who's on call you probably have at least a clue how it's deployed
[2304.34 → 2310.78] basically I mean it's going to be different site to site but at least you have an idea what crazy
[2310.78 → 2315.12] something somebody might have done I mean there's still going to be those times you log in and somebody
[2315.12 → 2321.48] left unicorn running in a tmux session, and you have no idea how to restart stuff, but that's not the
[2321.48 → 2327.88] norm anymore and I think five or six years ago that was the norm um and I'm glad that we're away from
[2327.88 → 2333.12] that so right I'm really excited about the stuff that's coming out about containerization and
[2333.12 → 2341.12] specifically docker is amazing um but I think there's always going to be you know that those pieces of
[2341.12 → 2346.50] software are going to fill the same void that Heroku is filling there's going to be probably tens of
[2346.50 → 2350.66] thousands of people that say hooray containers now we don't have to use Cristiano anymore
[2350.66 → 2357.90] and um then they'll remember that they use a mac and like c and docker only runs on Linux and
[2357.90 → 2364.98] then they're going to need something to script their build server so um you know things will improve
[2364.98 → 2370.92] things there's always something and right exactly and um that's kind of the pitch with version
[2370.92 → 2375.82] three of Cristiano is to say look we basically know how to do this now it's a really tiny tool
[2375.82 → 2383.10] use it if it works for you don't use it if it doesn't work for you uh and there's much less to
[2383.10 → 2389.20] learn I mean we've kind of shrunk the footprint of the whole project and tried to make it this thing
[2389.20 → 2394.40] that you could just pick up and use without the steep learning curve because it's not going to be the
[2394.40 → 2401.92] norm for that much longer yeah so I want we don't have a ton of time left I want to kind of get into
[2401.92 → 2408.86] your specific uh burnout and then we also maybe talk a little bit about harrow um you wrote
[2408.86 → 2415.32] in the Cristiano mailing list a few weeks ago uh about just kind of some displeasure and and and
[2415.32 → 2420.44] just feeling overwhelmed and honestly just uh burnt out which I think I mean you've been doing
[2420.44 → 2426.88] Cristiano for what would you say about six years now so um I mean sheesh I feel like you
[2426.88 → 2432.82] had burned out much sooner than that so uh props for holding on for dear life that long but um
[2432.82 → 2437.70] you put you posted some stuff you know we don't need to get into all the negatives, but you posted
[2437.70 → 2442.30] some stuff that you just said basically like Cristiano is a great tool general purpose or ruby is a
[2442.30 → 2446.86] great language I love the environment but here are some things that have been troublesome and one of the
[2446.86 → 2451.90] big ones was you know what we talked about before with the issues but I want to get into one of the
[2451.90 → 2457.54] comments that on that thread specifically and I won't mention him, but he basically said lee I feel
[2457.54 → 2462.14] terrible for never having posted so much as a word of thanks for your effort dedicated to Cristiano
[2462.14 → 2470.06] over the years and is that not it in a nutshell like you only hear the negative right and then and these
[2470.06 → 2475.34] people and at the end of his post he said um I want you to know that Cristiano has been a cornerstone
[2475.34 → 2480.68] of the trade that has paid my bills for the last six or seven years, so everything's worked for him
[2480.68 → 2485.78] he's he's used if it's worked he's been pleased with it probably if things haven't worked he's
[2485.78 → 2490.18] figured out a way around it figured out how to solve it himself um you know overall positive
[2490.18 → 2494.84] experience well of course you're not going to hear from this guy uh unfortunately you're you'll hear
[2494.84 → 2499.52] from the person that you know has a problem getting set up in the first place or has a problem
[2499.52 → 2506.56] you know like you said with um using I don't know using some weird build of ruby that he got
[2506.56 → 2511.64] from somewhere else, or you'll hear that stuff the negative so what do you think do you think it could
[2511.64 → 2516.20] have it could be different for you if is you would hear kind of both sides of it like the people that
[2516.20 → 2520.60] were thrilled about what you're doing and very happy with everything and kind of the positive
[2520.60 → 2526.88] reinforcement rather than only hearing the negative side yeah definitely and that was um so when I wrote
[2526.88 → 2531.96] the mailing list post there was a real chance I was just going to kind of do like why the lucky
[2531.96 → 2536.54] stiff did a few years ago just to lead everything off GitHub let the community and gone yeah yeah
[2536.54 → 2541.80] right exactly let the community pick up the pieces they did a great job last time and somebody would
[2541.80 → 2546.18] have stepped up to fill the void and who knows maybe they'd do a much better job that I was doing but
[2546.18 → 2553.96] most of the reason I stayed around was I took a couple of days after that mailing list post and just
[2553.96 → 2560.98] tried not to do anything and came back to about 120 emails from people exactly like the quote you just
[2560.98 → 2567.94] read out people saying you know um I'm a deployment consultant i I go around I earn my living helping
[2567.94 → 2573.88] people with Cristiano recipes I don't maybe that's a bad thing because it's so broken but um you know
[2573.88 → 2581.18] nice people telling me that they never even considered that it was just for the most part one guy with a
[2581.18 → 2587.66] couple of people helping out from time to time building this tool which is the kind of cornerstone
[2587.66 → 2592.42] of pretty much every rails' deployment in the world I would guess I mean Heroku changed that a bit but
[2592.42 → 2599.12] at least I think we're approaching something like six million downloads that gets skewed a little bit by
[2599.12 → 2604.18] bundler I don't know if it's really up or down or whatever else but I mean that's that's a lot of
[2604.18 → 2614.16] people and I would say up until six months ago I was basically alone 10 months of the year working
[2614.16 → 2617.86] on this and then there would be someone around for a few weeks helping with a couple of specific
[2617.86 → 2625.92] issues there were some great contributions for rails from um from Nathan broad bent specifically
[2625.92 → 2630.40] around the asset pipeline stuff when that came out for rails three, but there's been nobody kind of
[2630.40 → 2636.64] by my side helping the whole time and um I've been really lucky that through building Cristiano
[2636.64 → 2642.86] three I've been connected with tom Clements who I think he's CTO or lead developer on the beach in the
[2642.86 → 2649.44] UK, and they use Cristiano for everything, and they always have done and as soon as he knew that I needed
[2649.44 → 2655.42] some help uh he's now stepped up, and he's basically written kind of 30 or 40 percent of the new version of
[2655.42 → 2662.76] Cristiano which is incredible um there's also another guy called KER chart I'm not very good
[2662.76 → 2666.60] with Russian names but I hope I pronounced that correctly, and he stepped up and wrote all the
[2666.60 → 2671.80] integrations for bundler and RVM and every other weird thing you've ever seen, and he's doing an
[2671.80 → 2679.24] amazing job of support so knowing those two guys are there knowing that I can look in my inbox c25
[2679.24 → 2684.38] issue notifications from GitHub and ignore all of them because they'll be taken care of
[2684.38 → 2687.58] that's an amazing feeling and I've never had that over the last few years
[2687.58 → 2695.02] so you reached out to the community kind of like almost an uh you know a distress call like hey I'm
[2695.02 → 2699.58] I'm drowning here I think your exact words were I'm coming apart at the seams and the response you
[2699.58 → 2705.10] got was overwhelmingly positive uh so you were thinking maybe a 410 gone but through the
[2705.10 → 2709.00] response you got you're still here you're still working on this and sounds like you've gotten
[2709.00 → 2713.74] some reinvigoration to keep moving forward and some help to kind of lift you up because I mean
[2713.74 → 2718.32] we all know like you can't do any of this by yourself for so long I mean again I'm shocked
[2718.32 → 2721.94] that you've been doing this by yourself for as long as you have, and you're still here at all
[2721.94 → 2729.32] um but I don't know that that's a that's an open source win um maybe that maybe the lesson learned is
[2729.32 → 2735.28] to not wait until you're literally coming apart at the seams and or I guess figuratively coming apart
[2735.28 → 2741.04] at the seams and um a little bit early on in the process maybe could have benefited you to reach
[2741.04 → 2747.08] out and kind of maybe share some of those sentiments earlier maybe yeah definitely and I think that's um
[2747.08 → 2752.60] it's some kind of stigma we live in a world where the only people we hear about are the super famous
[2752.60 → 2759.48] Mark Zuckerberg and the kind of success stories from 37 signals, and we don't really spare much
[2759.48 → 2764.26] thought for the guys who put an incredible amount of work and never get a thank you for anything
[2764.26 → 2770.20] and that's something that I've changed since my burnout is whenever I'm opening an issue and I'm
[2770.20 → 2774.60] writing some stuff with the go language right now and I've actually run into three bugs in the go
[2774.60 → 2781.26] standard library, and you know this is written by rob pike, and he's programming god and all of these
[2781.26 → 2786.38] brad Fitzpatrick and the other guys they're amazing and i kind of don't believe that I've really found
[2786.38 → 2791.22] bugs so whenever I'm approaching those guys I'm like yeah guys I'm pretty I'm pretty sure I'm just
[2791.22 → 2798.48] holding it wrong, but maybe there's maybe a bug, and it really affects the way that I'm communicating
[2798.48 → 2804.44] with the maintainers of the projects that I rely on and um I'd like to encourage a culture of people
[2804.44 → 2814.36] asking for help being open about being real human beings and not trying to provide this image of being
[2814.36 → 2818.66] the genius programmer who ships everything perfect every time because it's just not realistic
[2818.66 → 2823.98] yeah if you talk to every you know therapist psychologist out there pretty much everything
[2823.98 → 2830.10] in life comes down to pride versus humility and sounds like not sounds like but the truth is a
[2830.10 → 2834.60] lot of us developers could use a lot more humility and sacrifice a lot more of the pride um
[2834.60 → 2841.78] just for your not for the uh not just for you know the sake of the person I'm speaking to but
[2841.78 → 2846.02] for yourself as well I mean you know if I'm is I'm willing to be honest with people and talk about my
[2846.02 → 2850.42] struggles and development and the things that I don't know then guess what I have an opportunity
[2850.42 → 2856.34] to learn and if i wear my pride shield proud and I know everything then guess what I'm
[2856.34 → 2860.40] going to fake it and I'm not going to learn and I think that you know for all of us um we could
[2860.40 → 2865.04] approach these situations with some humility to really learn, and then you know potentially make
[2865.04 → 2869.64] everyone's life better and I think you said a good point like maybe it would be helpful
[2869.64 → 2873.34] for all the developers when you're opening issues and open source to read the contribution
[2873.34 → 2878.70] guidelines to read the issue guidelines to you know to lead with a positive right you're thankful
[2878.70 → 2882.74] that this person is even going to look at your issue I mean we rewrite with like the expectation
[2882.74 → 2890.22] of like hey uh the reason like you're you're going to fix this because it's your fault and you
[2890.22 → 2895.24] screwed this up so fix it, and it's like maybe if we approached it more from a like hey everything
[2895.24 → 2899.22] you're doing is incredible um here's something that's happening I'm not sure if maybe I'm doing
[2899.22 → 2904.44] something stupid, or you know maybe it's lack of understanding but anything I can do to help you
[2904.44 → 2908.86] out let me know I mean I feel like if that was the general mindset with issues probably would solve a
[2908.86 → 2916.16] lot of the burnout problem yeah definitely and I've been well actually kind of stupid I've I ran into a
[2916.16 → 2922.76] couple of bugs as well with go language with the post Postgres driver and um I've been communicating
[2922.76 → 2928.04] with those guys about two specific issues and I ran into a third issue and I've been working with
[2928.04 → 2932.72] them for basically a week trying to figure out what we were what was going wrong and we
[2932.72 → 2937.26] couldn't reproduce it, and we couldn't reproduce it couldn't reproduce it, and it turned out to be
[2937.26 → 2944.12] some weird deadlocking issue because I had a recursive Jason marshalling thing which was a really stupid
[2944.12 → 2950.50] typo on my part and uh i I mailed those guys and said look this is really embarrassing but i completely
[2950.50 → 2955.96] screwed up and uh those guys were cool about it, they said hey look great well thanks for the bug reports
[2955.96 → 2961.12] on the other two things that's we're going to take care of those sometime, and you know hey at least
[2961.12 → 2967.68] we know we didn't screw up it's your fault so yeah yeah um I like that and I think I'm very lucky to
[2967.68 → 2973.32] have had the good dialogue with those guys um but I think the assumption that open source software is
[2973.32 → 2979.00] perfect, and therefore it should work is kind of unrealistic, but we've gone in that direction because
[2979.00 → 2985.26] everything has gotten to be so good yeah and um it's up the game for the rest of us it's great that
[2985.26 → 2991.60] we have to up our games it's its great that guys like tom and Kerr and i we have to write great
[2991.60 → 2998.28] software it pushes us it makes us grow, but it also puts a lot of pressure on us right well running out
[2998.28 → 3003.34] of time real quick give us the pitch for hard or hard how do you say that and what is it and uh
[3003.34 → 3010.26] kind of where what we should be looking for yeah, so this is um based well based on the fact that
[3010.26 → 3015.74] I didn't write Cristiano originally I've never really felt like I earned the right to commercialize
[3015.74 → 3020.56] it or find a way to commercialize it and a lot of the feedback I had after the burnout was
[3020.56 → 3026.08] you know find a way find a way to make this sustainable find a way to work on it full-time
[3026.08 → 3032.62] and an idea that's been brewing in my mind for a long time is something some people may remember
[3032.62 → 3039.76] Sebastiano it's a very old uh completely obsolete now version of Cristiano that you could run on
[3039.76 → 3043.84] the web so it didn't integrate with your app or anything, but it was a website you could host somewhere
[3043.84 → 3050.98] click a button and Cristiano would do its thing and um so I've been working on this together with tom
[3050.98 → 3057.24] and hard is going to be a hosted Cristiano for teams but also will provide build environments so
[3057.24 → 3063.98] you can think of it somewhere between kind of Jenkins or Travis CI where it will have an up-to-date
[3063.98 → 3067.70] list of whatever's going on in your repository you'll be able to see your branches you're staging
[3067.70 → 3073.28] environments it will help to manage ssh keys for your users and your team members or maybe some
[3073.28 → 3078.88] contractors you have it will also take care of all the audit logging and everything else, and you'll be
[3078.88 → 3084.54] able to schedule deploys there's some really cool stuff about kind of team ssh debugging sessions
[3084.54 → 3091.84] right in the browser over web sockets it's an attempt at making everything that is cool about
[3091.84 → 3097.62] GitHub Travis and Jenkins all of that online collaborative stuff bringing it to deployment and
[3097.62 → 3102.86] firmly in the knowledge that this Cristiano style deployment eventually will be replaced by
[3102.86 → 3111.64] containerization hard will run any rake task any build script you have so it will also be perfect for
[3111.64 → 3117.46] people who want to script the building of Debian files or rpm or even scripting containers or
[3117.46 → 3123.14] whatever else and I think that's important I want to keep it very affordable and very cheap
[3123.14 → 3128.44] probably going to follow the Travis model where you get kind of a crazy number of stuff for free
[3128.44 → 3134.42] up front and probably most people never see a bill but for any companies who are getting value out
[3134.42 → 3138.40] of it that I want it to be worth it and I want it to make Cristiano sustainable
[3138.40 → 3144.60] and um it's a kind of promise from my side of the community that Cristiano will always remain
[3144.60 → 3152.88] kind of priority on emit licensed open source and will never be proprietary uh of course I couldn't
[3152.88 → 3159.04] make it that way even if I wanted to um but I'm really hoping that hard will be successful we have
[3159.04 → 3164.84] about 500 people signed up for the alpha already which is kind of overwhelming um but I'm excited
[3164.84 → 3170.42] uh it's working pretty well for us and amazing timing is that we were having real hard times with
[3170.42 → 3175.62] the kind of RPC for repository access checking and web hooks and everything we have to be really
[3175.62 → 3180.92] careful with people's ssh keys and security tokens so we were doing everything in sandboxed virtual
[3180.92 → 3189.04] machines and well frankly that sucked um sorry to everybody who's involved with virtual box uh but then
[3189.04 → 3194.28] docker came along and docker has made everything amazing so that's another classic open source win story
[3194.28 → 3202.60] awesome so hard is it how do you pronounce it hard or harrow its harrow uh I think there's a
[3202.60 → 3206.52] school in England called harrow a private school, but it's also a farming implement it's the thing you
[3206.52 → 3211.90] use after you plow the fields to get it ready for planting plus it sounds cool so yeah so you've
[3211.90 → 3216.48] plowed the fields with Cristiano, and you're ready for planting right something like that so you're
[3216.48 → 3221.90] well you're you're going to be um uh harvesting the money out of their wallets
[3221.90 → 3229.04] that's that's not what's written in the business plan but yeah, yeah, so the website is harrow
[3229.04 → 3234.46] h-a-r-r-o-w dot i-o you can sign up for the alpha and uh you can keep an eye on it's going to be
[3234.46 → 3240.18] pretty cool I think yep and uh we're totally open to feedback I mean it's its pretty early we have all
[3240.18 → 3245.42] of the structure in place but if people want to tell us how they want to do this stuff then
[3245.42 → 3251.56] we're really open to making the workflows really flexible awesome so once again that's
[3251.56 → 3260.10] h-a-r-r-o-w dot i-o uh so we're running out of time here for our new listeners uh we ask same
[3260.10 → 3264.80] questions at the end of every show so for the sake of brevity I won't explain it and let's ask them
[3264.80 → 3269.98] now lee for a call to arms uh something you'd like to see the community kind of help out with
[3269.98 → 3276.70] Cristiano yeah so first on a wider topic just respect your open source guys thank them from
[3276.70 → 3282.42] time to time uh fewer plus ones and GitHub issues and when it comes to Cristiano just
[3282.42 → 3289.06] tell us what doesn't work for you but uh try and give us enough information to help you that would be
[3289.06 → 3295.44] my number one request gotcha so be precise to give context with your issues when you open them
[3295.44 → 3300.04] definitely because very often we can close them straight away and tell you exactly what you did
[3300.04 → 3304.72] wrong, and otherwise it can take a few days bouncing back and forward to find out that you know whatever
[3304.72 → 3312.20] you forgot to put a gem in your gem file so right cool um if you weren't doing this I don't know what
[3312.20 → 3317.58] this is but maybe hero Cristiano uh maybe some of your consulting what would you be doing instead
[3317.58 → 3322.06] oh I don't know I think if it wasn't for open source I probably would have thrown my
[3322.06 → 3326.90] life away and I'd be like sitting on a couch somewhere with no job playing video games so
[3326.90 → 3331.80] living the dream in other words living the dream yeah right I mean I owe my entire career to open
[3331.80 → 3337.46] source um through getting involved at a young age I have no formal university education or something so
[3337.46 → 3343.48] yeah i without open source in general I don't know what I would do which is probably why I'm still
[3343.48 → 3351.16] doing open source cool uh programmer hero somebody that's influenced you greatly
[3351.16 → 3358.20] uh James buck definitely I know that's kind of soppy to say that because I took over his project but
[3358.20 → 3366.04] I think he got out yeah right uh took over it's not all mine now but uh I think he got out at the
[3366.04 → 3372.10] right time he got out for the right reasons I think when I look back at the situation he must have been
[3372.10 → 3378.26] in and the way he must have been feeling he made the right decision against what's a very strong pull
[3378.26 → 3385.30] from the community to stay and stay responsible and stay answerable to the community, and he was very
[3385.30 → 3390.62] bold and standing up against that and going prioritizing his family and his health which i
[3390.62 → 3397.40] think is important uh other than that every guy who ever wrote any line of software I ever used because
[3397.40 → 3404.38] again we wouldn't be doing what we're doing without you um, and it's amazing its amazing that we can
[3404.38 → 3410.06] build the stuff we build on top of the shoulders of giants on hundreds of millions of lines of code
[3410.06 → 3415.80] in countless languages, and it's incredible that it all works together you mentioned the health
[3415.80 → 3421.92] part with James, and you know that's that's much respect too because those are seriously hard
[3421.92 → 3427.02] decisions when you absolutely love your craft, and it doesn't mean that you don't love your family
[3427.02 → 3432.60] equally, but it's you know it's like that's your passion it's kind of your art you know it's you
[3432.60 → 3439.78] know coding isn't and developing isn't just hacking its you know it's an art form right and to give
[3439.78 → 3446.10] that up so he must love his family tons which is super awesome and very respectable too right yeah and i
[3446.10 → 3453.20] think for a lot of people uh especially myself I mean i I count myself first as programmer hacker engineer
[3453.20 → 3460.84] and to admit publicly that I'm struggling to hold everything together with the thing by which I define
[3460.84 → 3468.38] myself that's tricky and actually doing it was the best thing I ever did and the sense of kind of weight
[3468.38 → 3474.48] of your shoulders is incredible and I think we all need to you know we're human beings we're sons and
[3474.48 → 3480.78] daughters and husbands and boyfriends and girlfriends first and the stuff we do open source it's all digital
[3480.78 → 3487.30] it's all ephemeral if we just cease to exist one day it would continue or not and the world would go
[3487.30 → 3492.56] on, and it's important to keep the perspective yeah I'm glad you mentioned that too because we're going
[3492.56 → 3498.14] to link out to that in the show notes, so anyone can uh kind of catch up on their own but I totally felt
[3498.14 → 3503.14] that like as I was reading your words i just kind of could feel the angst that you needed to get it
[3503.14 → 3508.90] out, but it was painful you know that that so I can only imagine you know the deliberation you must
[3508.90 → 3514.88] have been going through when you were writing this I might just drop this project and what that means
[3514.88 → 3519.70] for you know for you and the community and what kind of feedback you might get and I mean obviously
[3519.70 → 3524.10] you came on the show to talk about some of the details around that so we won't go back into it but
[3524.10 → 3529.34] that will be linked out in the show notes but lee I want to thank you for coming on the show
[3529.34 → 3535.24] man we really appreciate you just um sticking in there taking the time to come on the show and share
[3535.24 → 3542.04] your story and your history and uh lift James up who's a developer programming hero for you and
[3542.04 → 3547.46] just um all that you do and sharing I know it's sometimes it's not always the easiest thing to do
[3547.46 → 3553.34] but um you know the fact that you get up and do it every day and that you love it is uh is awesome
[3553.34 → 3558.10] and we certainly appreciate you allowing us to stand up on your shoulders and the code that you've
[3558.10 → 3564.22] helped lead get written so um definitely want to thank you for joining us and Andrew awesome show
[3564.22 → 3568.28] bro thank you so much for doing this and you the listeners for listening to this show we
[3568.28 → 3573.04] absolutely could not do this without you uh and to mention a couple others digital ocean and top
[3573.04 → 3578.26] tile they're supporting the show making it possible with digital ocean I want to remind you to take
[3578.26 → 3584.96] advantage of that ten dollar hosting credit and to do so you can use the code the changelog October
[3584.96 → 3589.30] that's the changelog October I know it's about to be November so if you're listening to this in November
[3589.30 → 3594.42] it's probably going to still work and if it doesn't hit up support so don't worry about that
[3594.42 → 3600.30] uh they do send uh stickers around the world so no matter where you're at whether you're in Australia
[3600.30 → 3606.04] uh if you're in Europe or you're here in the U.S. email Barry at digital ocean.com he'll ship you
[3606.04 → 3612.44] some stickers to decorate your laptop, and thanks to top for being an awesome new sponsor and they
[3612.44 → 3618.10] will be sponsoring the next few shows so certainly appreciate their support join the top towel worldwide
[3618.10 → 3623.08] network and work with some awesome people anywhere in the world beach wherever right Andrew I mean
[3623.08 → 3630.10] beach is kind of the best place to be but top.com slash developer to apply, and we mentioned their
[3630.10 → 3635.66] their engineering blog if you haven't caught up with this yet go check it out uh it's top.com slash blog
[3635.66 → 3642.58] we were recently um we recently featured them on the changelog and I think in the last week's weekly
[3642.58 → 3648.30] we had a spot in there for them too so if you're a subscriber to weekly uh we thank you for that as
[3648.30 → 3654.64] well and if you're not gone to changelog uh the changelog.com slash weekly and subscribe today but
[3654.64 → 3660.56] awesome show guys let's say goodbye see you later goodbye
[3660.56 → 3666.42] you
[3666.42 → 3666.70] you
[3666.70 → 3668.54] you
[3668.54 → 3683.82] you
[3683.82 → 3713.80] Thank you.
