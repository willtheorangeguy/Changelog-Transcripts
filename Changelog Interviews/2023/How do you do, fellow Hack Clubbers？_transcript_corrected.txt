[0.00 → 11.26] what's up welcome back this week on the changelog we're talking to Zach Lotta the founder of hack
[11.26 → 18.18] club at 16 Zach tested out of high school and moved to sf to join yo as their first engineer
[18.18 → 23.82] put your hands up if you remember yo yo after playing a key role at to he founded
[23.82 → 30.14] hack club to help teen hackers start coding clubs around the world today teen hackers can meet IRL
[30.14 → 37.50] online at a hackathon or leverage hack club bank as a fiscal sponsor to create their own organization
[37.50 → 44.04] hack club has the support of the likes of tom Preston Warner co-founder of GitHub Quinn slack
[44.04 → 51.50] CEO and co-founder of source graph and even Elon Musk wow more than 25 000 teen hackers from all
[51.50 → 57.84] of the world meet online every single day at hack club.com and today Zach shares the behind the
[57.84 → 64.14] scenes of this cool movement a massive thank you to our friends and our partners at fast and fly
[64.14 → 71.36] this podcast got you fast because quickly well they're fast globally check them out at fastly.com
[71.36 → 77.22] and our good friends over at fly.io well they help us put our app and our database close to our users
[77.22 → 81.20] with no ops make sure you check them out at fly.io
[81.20 → 95.12] what's up friends this episode is brought to you by dev cycle you probably heard about testing in
[95.12 → 101.86] production dark launches kill switches or even progressive delivery all these practices are
[101.86 → 107.36] designed to help your team ship code faster reduce risk and to continuously improve your customers
[107.36 → 112.74] experience and that's exactly what dev cycles feature management platform enables they offer
[112.74 → 118.88] feature flags feature opt-in real-time updates, and they seamlessly integrate with popular dev tools
[118.88 → 125.74] with client-side and server-side SDKs for every major language they even offer usage-based pricing
[125.74 → 131.68] to make feature flagging more accessible to the entire team and I'm here with Jonathan Norris co-founder
[131.68 → 138.10] and CTO of dev cycle so Jonathan I've heard great things about using feature flags but I've also
[138.10 → 143.50] heard they can become tech debt how true is this that's a great point feature flags can quickly become
[143.50 → 149.62] tech debt is one of my common sayings and how we deal with that is that we fundamentally believe that
[149.62 → 154.16] feature flags should be as easy to remove from your code as they are to add to your code and that's kind
[154.16 → 158.74] of one of the core design principles that we're going towards is to try to make it as easy as possible
[158.74 → 162.90] for you to know which flags you should remove from your code and which flags you should keep
[162.90 → 168.20] and making it automatic to actually remove those flags from your code base, and so we've actually
[168.20 → 173.98] already built tools into our CLI and our GitHub integrations to automatically remove flags from your
[173.98 → 179.50] code base for you and make a PR that says hey here's a PR remove this flags no longer being used
[179.50 → 183.96] from your code base, and you can choose to merge it or not so that's another thing that yeah i fundamentally
[183.96 → 188.82] believe that like yes flags can become tech debt, and we've got to work on that full developer
[188.82 → 194.48] workflow from end to end that it's great that it's super easy to add flags to your code base but your
[194.48 → 199.54] flag should be visible to you all throughout your development pipeline everywhere from you ride to
[199.54 → 204.90] your CLI to your git repository to your alerting and monitoring system, and then we should tell you when
[204.90 → 209.48] you should remove those flags from your code base and help you clean them up automatically so it's just as
[209.48 → 214.34] important to clean them up as it is to create flags easily very cool thank you Jonathan so dev cycle
[214.34 → 219.90] is very developer centric in terms of how it integrates into your workflows very team centric in terms of
[219.90 → 225.62] its pricing model because this is usage-based pricing means everyone on your team can play a role in feature
[225.62 → 231.50] flags they also have a free forever tier zero dollars so you can try out feature flags yourself
[231.50 → 239.18] in your environment check them out at devcycle.com slash changelog again devcycle.com slash changelog
[239.18 → 268.72] we're here with Zach Lotta Zach you reached out late last year sometime I want to see you
[268.72 → 274.36] actually called us did you call us yeah yeah I called your number on your website that's right man
[274.36 → 280.52] you're one of the few and one of the proud that actually take the phone number put it into a phone
[280.52 → 287.24] and make it ring and then somebody answers and that somebody is almost always me because jarred doesn't
[287.24 → 292.90] have this connection like I don't I'm not going to answer I can forward a call to you jarred, but it does it
[292.90 → 298.36] goes to me usually because I set it up forever ago it's grasshopper turn something else I don't know what
[298.36 → 305.24] it is but yeah we have a phone number and Zach called us which was the coolest, so maybe this is
[305.24 → 310.98] related I actually noticed today Zach as I was on your website hackclub.com that in the footer there
[310.98 → 315.82] you got a phone number in your footer and I thought either Zach likes to get phone calls or maybe he was
[315.82 → 321.22] inspired by Adam actually answering or maybe that pre-existed I don't know it was your 800 number was
[321.22 → 325.28] that a new thing or did that pre-exist this phone call you made no we've had it for a few years but
[325.28 → 330.76] it rings my phone number among others on the team nice and yeah I mean i I think that it's important
[330.76 → 336.14] that you can get in touch with a human and i I think that the beauty of technologies allows us to
[336.14 → 341.40] take away all the things that robots can do to let us focus on the things that humans can do
[341.40 → 346.80] and I think that human to human connection is kind of important yeah for sure how did you feel
[346.80 → 353.36] whenever I answered the call like a human given your position well I think you were driving
[353.36 → 359.60] and you were like who is this why are you calling and uh, and then we got to do it and I was like oh
[359.60 → 364.78] my god i I'm so excited to be talking to you one-on-one you know so I was excited when you picked
[364.78 → 370.72] up and the reason I called was every few months a bunch of teenagers at hack club come together to
[370.72 → 376.20] build some sort of open source project, and we had just shipped one of our most recent projects which
[376.20 → 382.28] was an open source game console called spake it's super cool it's like a combination of a piece
[382.28 → 387.56] of hardware it's like a custom PCB or that you can hold, and it's an online game engine that's like
[387.56 → 392.06] perfect for people who are just starting to get involved in programming with game development
[392.06 → 397.14] and we were reaching out to a few different folks Hathaway did a profile um it fronts page
[397.14 → 401.34] hacker news it was getting popular in different parts of open source community so I was reaching out
[401.34 → 405.76] because I want to share with you, I recall that I like those phone calls and I'm sorry because
[405.76 → 411.52] sometimes I get those calls and I always answer because I can't answer I have to answer and
[411.52 → 417.82] then sometimes I forget like that it's potentially this number our business number calling and I'm like
[417.82 → 423.48] why are you calling who's this again but either way we did have we talked for like 30 or 40 minutes
[423.48 → 429.28] and I was just like man you all have something cool happening at hack club I found out about you, I think
[429.28 → 433.56] by way of Quinn slack he was on founders talk a while back and I know that if I understand correctly
[433.56 → 438.50] tom Preston Warner one of the co-founders of GitHub is an investor I believe you can correct me if I'm
[438.50 → 443.30] wrong but like I knew of hack club to some degree and I was like I was happy that you called basically
[443.30 → 447.20] you know long term i was like after we were in the call with you, I was like man this is uh
[447.20 → 453.14] this is exciting i I mean we've always been a fan of the younger hacker generation jarred i both have
[453.14 → 459.12] children so we aspire to have you know children who respect technology and understand it and can
[459.12 → 464.32] use it the same way we do it if not better hopefully better yeah, but we love the past
[464.32 → 470.12] present and future hacker generation just as well as anybody so awesome yeah, and you know Quinn and
[470.12 → 475.24] tom have both been incredible supporters of the mission as a non-profit we rely on the generosity
[475.24 → 481.78] of the technology community to make hack club free and available to teenagers today and both tom and
[481.78 → 485.66] Quinn have been founding board members of hack club they've been involved since the very beginning
[485.66 → 491.08] and really so much of the amazing work happening in the community would not be possible without
[491.08 → 496.38] either of them so big thank you to both of them anybody else you can name us since we're naming Quinn
[496.38 → 501.28] and tom anybody else you can name that's founding board members or integral folks that are you know
[501.28 → 506.44] helping the mission of hack club yeah i mean the beauty of hack club is hack club isn't me it's not the
[506.44 → 511.64] staff at headquarters it's not you know our board members it's the community of teenagers all over the
[511.64 → 516.90] country of the world that make this open source movement possible and there are hundreds and now
[516.90 → 522.76] over a thousand you know teenagers who develop and spend their time every week building the communities
[522.76 → 528.06] and projects that they themselves want to have and want to participate on, and they're the ones who
[528.06 → 533.88] really make hack club possible you know we're very lucky to have a great donor community we operate
[533.88 → 540.14] with 100 transparent finances so anyone the public a teenager you know anyone curious can go to
[540.14 → 546.94] bank.hackclub.com slash HQ, and you can literally see our bank account balance every transaction every
[546.94 → 552.30] donor you know our supporters range from people who have built prominent open source projects in
[552.30 → 558.76] their free time like the guy who created city up from the jailbroken iPhone jay freeman he's a monthly
[558.76 → 562.50] supporter of hack club there are a number of technology founders that are supporters of hack club
[562.50 → 568.40] Elon Musk is a big supporter of hack club and really all of these different people are coming together
[568.40 → 574.40] because they have had their lives touched in a way where it transformed them in some way shape and
[574.40 → 579.54] form through technology, and they want to make that something that's free and available, and you know
[579.54 → 584.56] something that's more supported for the next generation of hackers and makers and doers and
[584.56 → 589.02] really thank you both for having me on and a chance to kind of share more of the hack club mission with
[589.02 → 594.24] the broader audience it takes a big tent to i think reach lots and lots and lots of young people
[594.24 → 599.88] yeah and our partners are so much more than uh you know open source contributors or donors it's like
[599.88 → 605.02] we rely on people like you to get the word out as well so thank you yeah happy to have you on i know
[605.02 → 610.26] that uh jarred i was looking through our transcripts and i was looking for hack club like how have we
[610.26 → 615.94] talked thank the good lord we've got these beautiful open source black and white anybody can
[615.94 → 621.46] contribute transcripts of our podcast because they're even a treasure trove for us even i was on episode
[621.46 → 627.62] 369 of the changelog here this show with Quincy Larson five years of free code camp and on that show
[627.62 → 632.46] Quincy was talking about you know the financial viability of free code camp and what they had done
[632.46 → 637.88] before they kind of got their situation in order so to speak to take better donations and have a more
[637.88 → 645.14] financially sound funnel i suppose to support the cause and Zach you'd be happy to know that i don't
[645.14 → 649.02] know if you know Quincy personally, but he's a fan of you, and before they were taking donations
[649.02 → 653.44] themselves directly they were suggesting you know women who code or hack club and this is directly
[653.44 → 658.92] from and hacker dojo this is directly from the transcript so he was suggesting donations to you
[658.92 → 666.14] all as well as a by proxy supporter that's cool yeah and um a huge thank you to Quincy and the
[666.14 → 671.54] broader free code camp community i don't know if they know how big the impact of that at the time was
[671.54 → 676.56] when they added us to their donate page i was 17 on my own i think i had one team member
[676.56 → 682.98] so desperately trying to make hack club something that existed in the world and that single donate
[682.98 → 689.06] page on their site drove more donations than any other source that year wow, and it literally meant
[689.06 → 694.56] that we could pay rent so really thank you so much to him and i know we have a lot of crossovers and
[694.56 → 699.38] collaboration in our communities uh free code camp is amazing that's beautiful that's beautiful
[699.38 → 705.66] well let's dive into your story a little bit you know Silicon Valley and tech people the lore of the
[705.66 → 712.52] founder has a lot of like college dropout vibes and i was happy to see that you have one-upped the
[712.52 → 717.24] founders of many Silicon Valley companies with this who drops out of college anybody can drop out of
[717.24 → 722.82] college Zach actually drops out of high school his freshman year to get this thing going you want to tell
[722.82 → 728.12] that story yeah sure so you know by my way of background I'm Zach I'm the founder of hack club
[728.12 → 734.38] and i grew up in southern California where both my parents were social workers my mom worked in foster
[734.38 → 739.46] care and my dad in homelessness and i went to public schools so like most schools in America still
[739.46 → 745.78] today didn't offer any classes and i was really lucky enough to be part of i think one of the first
[745.78 → 750.70] generations that really didn't know a world without the internet and when i would get home from school
[750.70 → 756.24] starting in like third grade i would just like i could not pull myself away from the computer
[756.24 → 761.74] it felt like oh my god like this is where the secrets of the universe lie and when i realized that
[761.74 → 766.34] you could learn how to code and not just consume stuff from the computer but we one of the creators
[766.34 → 772.84] that was the most exciting interesting idea and I'm like somehow i have to figure out how to be one of
[772.84 → 778.68] these wizards that know how to do this and i you know got involved i taught myself after school on the
[778.68 → 786.78] internet and when i made it to high school i felt so incredibly lonely because it felt like the one thing
[786.78 → 792.20] i wanted to do with all my time which was make things with code was also the one thing i could do
[792.20 → 798.06] at the one place where i had to spend all my time which was school and i think generally i kind of
[798.06 → 802.56] had felt like you know there's this whole path that's set up for young ambitious people first you do x and
[802.56 → 809.62] you do y then you do z and i always felt like a bit of a misfit within that and i ended up dropping
[809.62 → 815.38] out of high school after my freshman year i moved to San Francisco when i was 16 to become a programmer
[815.38 → 820.08] i helped make one game that became the most popular game at the app store at the time it's
[820.08 → 824.00] called football heroes you can still download it i was like a junior programmer on the team and
[824.00 → 829.92] probably held us back more than i contributed and that was like an incredibly meaningful chance to
[829.92 → 835.82] work on a real piece of software for the first time and then i helped build an app called yo which
[835.82 → 839.92] was like uh it was like Facebook Messenger but the only word you could send to people was the word yo
[839.92 → 844.80] and the idea was like what if we build an app that's like so silly so ridiculous that it can become
[844.80 → 851.40] viral just from that premise guys something interesting just happened so i downloaded
[851.40 → 856.64] with need's bro app out of curiosity and found it very sticky I've never felt like i was anyone's bro
[856.64 → 862.00] before the only people who have used that term with me were assailants but um i started bring
[862.00 → 866.96] people and getting bro back and all of a sudden I'm bros with all kinds of people including a guy
[866.96 → 872.94] from brans come ventures brans come that's a solid shop so we broad about this and that and then
[872.94 → 877.94] when he heard i worked at pie piper he got excited he tripled like my bro, and he asked about meeting
[877.94 → 883.74] us jarred what'd you tell him um i was waiting a bit to bro him back so that i don't seem over
[883.74 → 892.96] eager bro him back bro him back bro him we're not dead yet guys and that just absolutely blew up and
[892.96 → 897.58] became the number one app on the app store i remember that what year was that that was 2014
[897.58 → 902.64] okay and there were like the BBC was doing stories about how people in Israel were using yo
[902.64 → 907.06] for like, but people know like missile strikes that were happening i mean it was really
[907.06 → 911.70] crazy now did they develop morse code style ways of being more complicated or is it literally they
[911.70 → 916.30] just say yo and that meant there was a missile strike do you know it was you get a get a yo
[916.30 → 920.74] from an account called like you know Israel missile strike alert or something like that they just said yo
[920.74 → 927.52] it's like i am Groot i am Groot he says like i am Groot yeah he means everything that's all he says
[927.52 → 933.22] but people take away different things for sure yeah totally and that was like the most ridiculous
[933.22 → 939.08] introduction i think to the world of technology i mean we literally had Marc Andreessen write an
[939.08 → 943.00] article about one bit communication I'm like we ourselves i think we're still like trying to figure
[943.00 → 948.60] out if we were serious about this or not and i used the money from those two opportunities i had
[948.60 → 952.30] which for me felt like an enormous amount of money but really in the grand scheme of things was like
[952.30 → 958.72] $25,000 to start hack club to really try and create the sort of community that i so desperately
[958.72 → 965.56] wish I had when I was a teenager and hack club today is a network of over 25,000 teenage programmers
[965.56 → 971.24] from all over the world we're in all 50 states we're in 38 countries around the world there's after
[971.24 → 976.60] school hack clubs in high schools there's amazing open source projects built by our community I mean if you
[976.60 → 981.72] use an iPhone or an android phone or anything that runs I mean you literally run code written by
[981.72 → 988.30] hack clubbers every single day and some of the things that alumni do are just amazing and i I think the
[988.30 → 996.00] the broader mission of the organization is like every day thousands of young people are having some sort
[996.00 → 1002.24] of spark with technology where they're like oh my god I can be a creator and not just a consumer that is
[1002.24 → 1007.26] the most exciting idea on the planet and then there's just absolutely nothing to help them carry
[1007.26 → 1014.40] that forward and I think we want to live in a world where you know in the same way you can pursue
[1014.40 → 1018.30] varsity sports or the same way you can pursue different subjects as a teenager where you make
[1018.30 → 1022.90] that like the primary thing you do outside of class we want to live in a world where there's an ecosystem
[1022.90 → 1027.80] for the coders and for the makers and for the doers where you can make building things for the joy of it
[1027.80 → 1033.52] the primary thing you do outside of class as a teenager and I think that ultimately when I think
[1033.52 → 1039.70] about the long term like I think young people today need a new cultural institution that really works
[1039.70 → 1044.52] for them, it needs to be something that's positive we're gaining real skills we're connected with
[1044.52 → 1050.28] like-minded people across zip codes and I want to live in a world where half club can become as ubiquitous
[1050.28 → 1056.74] and as universal and as culturally foundational for young people today as groups like the grill and boy scouts
[1056.74 → 1061.82] have been for young people in the past and I think young people need this, and they want it, and they're
[1061.82 → 1067.42] trying to find it and um when you look at what happens in the community I mean it's amazing what
[1067.42 → 1071.62] teenagers are capable of when we really give them belief and support and create a community
[1071.62 → 1079.22] take that put that on a t-shirt really long that's all I can put on a t-shirt I want to put everything on
[1079.22 → 1083.62] a t-shirt jarred that's my thing yeah you do I want to put on a t-shirt yeah for real though I mean like
[1083.62 → 1091.54] that's wow we don't quite embody what you do Zach we are there in spirit because you know we say like
[1091.54 → 1097.04] that's one of the reasons why we have the explicit tag not on our shows we bleep out you know curse
[1097.04 → 1101.76] words and things like that because not just for that younger generation but just to make sure that
[1101.76 → 1107.86] everybody who can listen to podcasts and gain value from this you know that that's possible, but it's
[1107.86 → 1113.02] also for those folks out there that are either young and listening to our show teenagers and making
[1113.02 → 1118.04] sure that they're included and welcome but also those parents or aunts and uncles or whatever
[1118.04 → 1122.74] might be listening to our shows with younger generations in the car either by us most of
[1122.74 → 1127.14] they get interested, but it's also just like you know that protective layer, but we want to make
[1127.14 → 1132.60] sure that everyone is welcome to this community this change on community that we have and whatever
[1132.60 → 1136.54] it is currently and wherever it will go in the future we're not out there doing hackathons and doing
[1136.54 → 1140.52] the things you're doing, but we're definitely there in spirit that's why I thought when that phone call
[1140.52 → 1145.06] happened that I was talking about in the first part of the show like I knew we had to get you on the
[1145.06 → 1150.22] show I knew we had to kind of dig into your personal story I did not know this is a terrible researcher of
[1150.22 → 1155.92] me I did not know about to kind of reminds me of bro from Silicon Valley but I did not know about your
[1155.92 → 1160.50] involvement in you know and that's kind of like the cherry on top of this little cake we got here
[1160.50 → 1165.64] called Zach well I'm really happy to be here with you guys, and thank you for saying that
[1165.64 → 1183.22] what's up this episode is brought to you by postman our friends at postman help more than 25 million
[1183.22 → 1190.24] developers to build test debug document monitor and publish their APIs and I'm here with Arnold
[1190.24 → 1197.24] API handyman at postman so Arnold postman has this feature called API governance, and it's supposed
[1197.24 → 1203.96] to help teams unify their API design roles, and it gets built into their tools to provide linting and
[1203.96 → 1211.22] feedback about API design and adopted best practices but I want to hear from you what exactly is API
[1211.22 → 1217.12] governance and why is it important for organizations and for teams I think it's a little bit different from
[1217.12 → 1223.70] what people are used to because for most people API governance is a kind of the API police i really
[1223.70 → 1231.04] see it otherwise API governance is about helping people create the right APIs in the right way in
[1231.04 → 1237.44] order not just for the beauty of creating right APIs beautiful APIs but in order to have them do that
[1237.44 → 1244.32] quickly efficiently without even thinking about it and ultimately help their organization achieve what
[1244.32 → 1249.08] they want to achieve but how does that manifest how does that actually play out in organizations
[1249.08 → 1255.90] the first facet of API governance will be having people look at your APIs and ensure they are
[1255.90 → 1262.12] sharing the same look and feel as all of our APIs in the organization because if you're all of your
[1262.12 → 1267.42] APIs look the same once you have learned to use one you move to the next one and so you can use it
[1267.42 → 1274.76] very quickly because you know every pattern of action and behaviour, but people always focus too
[1274.76 → 1281.24] much on that, and they forget that API governance is not only about designing things the right way
[1281.24 → 1287.64] but also helping people do that better and also ensuring that you are creating the right API so you
[1287.64 → 1295.46] can go beyond that very dumb API design review and help people learn things by explaining you know you
[1295.46 → 1300.16] should avoid using that design pattern because it will have bad consequences on the consumer on
[1300.16 → 1306.82] implementation or performance or whatsoever and also by the way why are you creating this API what
[1306.82 → 1313.00] it is supposed to do and then through the conversation help people realize that maybe they are not having
[1313.00 → 1319.58] the right perspective creating their API they are just exposing complexity in our workings instead of
[1319.58 → 1325.80] providing a valuable service that will help people, and so I've been doing API design reviews for
[1325.80 → 1332.32] quite a long time and slowly, but surely people shift their mind from oh I don't like API governance
[1332.32 → 1338.70] because they're here to tell me how to do things to hey actually I've learned things and I'd like to
[1338.70 → 1346.30] work with you but now I realize that I'm designing better APIs and I'm able to do that alone so I need
[1346.30 → 1353.30] less help less support for you so yeah it's really about having that progression from people seeing
[1353.30 → 1360.62] governance as uh I have to do things that way to I know how to do things the correct way and before
[1360.62 → 1367.46] all that I need to really take care about what API I'm creating uh what is its added value how it helps
[1367.46 → 1373.46] people very cool thank you Arno okay the next step is to check out postman's API governance feature for
[1373.46 → 1379.18] yourself create better quality APIs and foster collaboration between development teams and API
[1379.18 → 1384.74] teams head to postman.com slash changelawpod sign up and start using postman for free today again
[1384.74 → 1387.58] postman.com slash changelawpod
[1387.58 → 1392.08] you
[1403.46 → 1413.08] I hate to do it because Adam will derail this conversation but if I just pull that thread on
[1413.08 → 1418.90] the Silicon Valley thing bro right is that bro that is that yo that was to wasn't it like
[1418.90 → 1424.80] they're basically riffing on you aren't they and that's to you Zach yeah yeah um i I mean i when i
[1424.80 → 1430.66] first moved to San Francisco I was 16 and I was living in a house of college dropouts who were all you
[1430.66 → 1435.88] know three or four years older than me which felt like enormous at the time, and we would have
[1435.88 → 1439.46] different, and we were all different people trying to make it in Silicon Valley in some way shape or
[1439.46 → 1445.68] form and when the TV show came out we started watching the episodes as they streamed each week
[1445.68 → 1452.06] together and when season two hit the first episode we kind of had this oh my god moment because it was
[1452.06 → 1458.54] about they got a bunch of people together at the AT&T stadium in San Francisco for like a silly VR type
[1458.54 → 1463.10] event and one of the people in the house like ran that event like that she was an associate at the
[1463.10 → 1467.26] firm that put that together we were like this is getting too close to real life and then the
[1467.26 → 1471.92] following week in the second episode of season two they did an episode where one of the plot lines was
[1471.92 → 1477.52] about this ridiculous app called bro where the only we can send is word bro they get tons of VC money
[1477.52 → 1483.84] it totally blows up I think we're going to have to crunch our burn rate again even with the 50 000
[1483.84 → 1488.22] from tech crunch we're not going to last very long wait wait wait no, no no Richard said we were gonna
[1488.22 → 1494.66] split that money right 10 000 each I don't think we can afford to do that anymore I just donated
[1494.66 → 1500.58] five thousand dollars to my cousin wait's kickstarter campaign he's trying to get an app called bro off
[1500.58 → 1505.80] the ground bro it's the messaging app that lets you send the word bro to everyone else who has the app
[1505.80 → 1513.96] so it's exactly like the to app yes but less original and i for so for me, I was hired as a first
[1513.96 → 1518.98] engineer on it and my job was to make it something that could process millions of uh push notifications
[1518.98 → 1523.94] quickly, and we were trying to figure out what the real business behind it would be, but it was just
[1523.94 → 1529.62] this like completely ridiculous you know larger than life kind of moment and introduction and I feel
[1529.62 → 1536.72] like that era of Silicon Valley of like 2012 to 2018 like I feel so lucky to play the small part in that
[1536.72 → 1541.08] because that was a really magical time I think everyone felt like anything was possible and that was
[1541.08 → 1546.24] before a lot of the cynicism today had kind of set in, and it's interesting working with hack clubbers
[1546.24 → 1551.68] because you know as teenagers are into technology today they read the articles about the cynicism they
[1551.68 → 1557.82] read the articles about you know maybe all this isn't so good, and it's interesting because i I think that
[1557.82 → 1563.44] you know young people want to feel like they can go on an adventure they want to do the really exciting
[1563.44 → 1568.06] interesting things and in some ways I think it's starting to feel like a lot of the paths that are open
[1568.06 → 1572.48] and technology are feeling a little closed off and I think that's part of where the excitement around
[1572.48 → 1576.26] things like AI and whatnot are where it's like oh my god like there's this new exciting thing
[1576.26 → 1583.14] that hasn't really been you know walked yet as a path for sure what's interesting is how uncanny that
[1583.14 → 1589.04] was to your life at the moment I mean how could you be watching Silicon Valley in season two episode
[1589.04 → 1594.60] two comes out it's like basically I mean it's riffing on what you had done with yo I mean it's totally
[1594.60 → 1599.38] I mean they're trying to mimic what happened in real life in real life Silicon Valley what's even
[1599.38 → 1605.10] cooler is how that went on to play like bro was acquired by a different company, and they sold to
[1605.10 → 1611.32] somebody else and Majid I believe is his name Dinesh's cousin who this is all like playing out in real
[1611.32 → 1615.52] life and this may be to some degree like part of your life he ends up with like 60 million dollars as
[1615.52 → 1622.18] part of this acquisition like so this silly idea this to slash bro app was acquired by somebody else and
[1622.18 → 1627.94] they were acquired by somebody else and here's Dinesh trying to you know essentially do well in
[1627.94 → 1635.54] Silicon Valley and get rich his cousin gets rich and that money fuelled them to buy hold later on
[1635.54 → 1639.98] and like if it was part of the entire story of like the whole story arc of Silicon Valley
[1639.98 → 1646.34] and that was season six like this silly app to slash bro I haven't seen that season yet Adam I'm sorry
[1646.34 → 1651.90] don't spoil the end well you say you're not going to do it watch it already jerry well I reserve
[1651.90 → 1655.40] the right to act like I'm going to do it and be disappointed I mean definitely don't have to
[1655.40 → 1662.72] watch it now okay well they're okay well spoiler alert delayed my bad rewind yeah it just played a
[1662.72 → 1667.08] critical role basically and like this silly thing played a critical role and that's just so wild
[1667.08 → 1672.46] because I mean I guess one of the pushbacks when I ask people they've seen this TV show is like I can't
[1672.46 → 1677.16] watch it is too close to real life, and it's kind of like traumatic and I guess in your case it was
[1677.16 → 1683.54] probably not traumatic but uh maybe it was what do you think well I mean after those two episodes we
[1683.54 → 1687.26] all felt like we had to stop watching it because it felt like a parody that was too close I haven't
[1687.26 → 1691.96] watched past season two because i just after that I was like this is crazy to spoil it for both of us
[1691.96 → 1697.90] here's me ruining it for both of you then i I had no idea it played a larger role later in the
[1697.90 → 1703.40] story well I mean the actual application itself but I suppose the ramifications of the
[1703.40 → 1709.22] app being created the silliness that it was it became so critical to the long-term story of
[1709.22 → 1713.82] Silicon Valley the show so actually I hear in season eight there's going to be a hack club have you heard
[1713.82 → 1718.10] this yeah season well they're coming back for season seven, and they're beginning with hack club
[1718.10 → 1724.00] yeah that's why I picked eight I figured I'd go way out there on a limb it's going to be for elementary
[1724.00 → 1728.88] school when you two talk to people like how are you hearing people talk about the future of tech
[1728.88 → 1733.30] for young people because and how are you hearing people talk about the cynicism as well
[1733.30 → 1737.30] good question I guess I don't hear many people talking about the future of tech for young people
[1737.30 → 1744.82] right so they aren't I guess to us at least and maybe that's some of it is selection bias the closest
[1744.82 → 1751.48] I've gotten so far is my son is in GT, and he's uh he's in first grade, and he's getting to play with
[1751.48 → 1756.06] three-year printers, and he's got you know special classes he goes to that are like gifted and talented
[1756.06 → 1762.86] is a program you have to get uh selected into you test for it and things like that, and you just learn
[1762.86 → 1767.66] at a different pace you learn differently and I haven't seen the cynicism but I guess what I have
[1767.66 → 1772.88] seen or I guess what I've interpreted from this is in this world of hack club or in this world where you
[1772.88 → 1778.42] want to live in a world where this kind of thing is available whether it's GT or a hack club type thing
[1778.42 → 1783.48] they're very similar in nature not the exact same because GT is more focused on like all things
[1783.48 → 1789.12] rather than just some coding i have to imagine that at some point you have a lack of educators right
[1789.12 → 1796.06] that's got to be you know one you've got you know political oversight, and you know financial funding
[1796.06 → 1800.58] for schooling and just different stuff like that that sort of gets limited, but you know it's great
[1800.58 → 1804.88] to get the program out there, but you have to have the right kind of people involved to lead the
[1804.88 → 1809.96] classes and smart enough to lead the classes because like this stuff moves so fast I guess
[1809.96 → 1816.44] my personal citizens might be okay great Zach you've got people buying into this idea of
[1816.44 → 1823.24] a hack club or a GT type thing for schools but how do you then get the educators in place to ensure
[1823.24 → 1828.68] that it is actually functions totally I mean this is what everyone on the education side is trying to
[1828.68 → 1834.22] figure out, and it's a huge challenge because on one hand if you spend a lot of time training someone
[1834.22 → 1838.74] as a teacher to learn how to code so they can teach it their job opportunities and the potential
[1838.74 → 1844.16] salaries are just so much larger outside of that, so there's a real you know one of the biggest
[1844.16 → 1848.76] problems of the computer science education space right now is hiring teachers and one thing that's
[1848.76 → 1854.32] unique about hack club is that there are no teachers everything within our community is led by
[1854.32 → 1859.42] teenagers for teenagers and that really came out of my own experience being a 16-year-old being like
[1859.42 → 1864.18] wait a second like I can run hackathons I can, you know create these spaces that I want to be a part of
[1864.22 → 1872.14] and I think with that vibe inside the community you get this kind of interesting dynamic where in the
[1872.14 → 1877.86] same way you see this kind of like competitive uh or semi-competitive dynamic at open source where
[1877.86 → 1881.84] you know everyone's trying to build the best JavaScript web, and you see these new things popping
[1881.84 → 1886.06] out people forming opinions you see some things that lots of people get behind we see a lot of the
[1886.06 → 1890.04] same dynamics in hack club where it's everyone wants to run the best hack everyone wants to run the
[1890.04 → 1893.98] best hack club and people are sharing their learnings, but there's this almost competitive
[1893.98 → 1900.10] vibe to make your thing the best and I think that what that means is that when you are a teenager
[1900.10 → 1905.58] and you're a part of hack club you're always seeing new stuff at each event, and you're always seeing new
[1905.58 → 1910.90] stuff in each meeting like you don't have to wait for the state standards to be updated so you can learn
[1910.90 → 1915.48] JavaScript instead of java like if it's cooler to teach JavaScript people are just going to do
[1915.48 → 1919.68] JavaScript in all their meetings and stuff like that one thing I've been thinking about, and we're
[1919.68 → 1926.20] trying to figure out right now is around the role of AI and when I think about the operations of hack
[1926.20 → 1932.46] club today we are only possible because of the open source community and I think a lot of developers
[1932.46 → 1938.28] today take open source as a concept for granted it's like oh yeah obviously all the technology that
[1938.28 → 1944.10] we use in the software world is open source by default but in my view that was something that was only
[1944.10 → 1949.84] really possible because 20 to 40 years ago a handful of individuals had some radical ideas
[1949.84 → 1956.46] worked really, really hard to build foundational technology a foundational ethos around open source
[1956.46 → 1961.18] and we're really benefiting from it today and I think something I'm seeing from a lot of hack
[1961.18 → 1965.94] clubbers is they're excited about stuff like AI, but it's so much less approachable than things like
[1965.94 → 1970.44] web development because you need expensive GPU clusters a lot of the stuff is quite impenetrable
[1970.44 → 1975.24] not all the interest in stuff happening is being open source and I'm curious on for both of you
[1975.24 → 1980.06] how do we create a world where the future of AI and some of this new tech is going to be fully open
[1980.06 → 1985.00] and something that's by the people for the people rather than owned by the few that's a big question
[1985.00 → 1989.34] we just talked about that a couple of weeks back with Simon Willison, and we are seeing open source
[1989.34 → 1995.80] moves into the space I think one of the most hopeful messages that I've learned of late with regarding
[1995.80 → 2002.26] large language models is that it doesn't it doesn't have to get continually larger in order for them
[2002.26 → 2008.22] to be really, really good especially once you are able to plug and play different info sources into
[2008.22 → 2013.18] them they get to a point where they can be good enough to go find answers and not have them all
[2013.18 → 2019.80] baked in by training and that's going to hopefully democratize access to running your own language
[2019.80 → 2025.24] models on your own hardware we're already seeing the software get out there for running these things on
[2025.24 → 2031.50] commodity devices and so there are also open source efforts in this space that are like you know
[2031.50 → 2037.42] six months eight months a year behind the bleeding edge which in a competitive landscape is not good
[2037.42 → 2044.12] enough but over the arc you know the s curve of technology quality increase I can't put that phrase
[2044.12 → 2049.74] together, but you know that curve of innovation eventually you get to the tail end of it and the
[2049.74 → 2054.82] open source stuff can be right there alongside the proprietary stuff you know lacking certain
[2054.82 → 2060.72] data sources of course so I don't have like an answer like we need to take steps one two and three in
[2060.72 → 2068.20] order to do this but i I am hopeful now more than I was three months ago four months ago because we're
[2068.20 → 2074.08] actually starting to see pretty good open source alternatives pop up yeah stuff like alpaca and
[2074.08 → 2083.00] alpaca and let me just grab my notes there's a new one uh nope it's just an open tab I don't have it
[2083.00 → 2087.74] just an open tab well there is lots of effort in this front you know it's the critical mass right now
[2087.74 → 2094.16] like it's the hype curve slash you know rapid innovation curve, and you know there's a lot happening in this
[2094.16 → 2100.92] moment and I think it's you know it's been compared to you know the invention of the iPhone the invention of
[2100.92 → 2106.16] the internet in terms of like its criticalness of the long-term future of i I would even say not
[2106.16 → 2111.12] just computing but humanity you know like this is going to change this is going to change everything
[2111.12 → 2117.70] like we just did the show with Simon that you're referencing son Willison, and you know on there I said
[2117.70 → 2124.40] it's already changed so much for me, you know it's its kind of given me I guess confidence in a way
[2124.40 → 2129.74] because you know you can search on the internet for a solution to x, but you have to rely upon somebody
[2129.74 → 2134.44] else ever having that problem, and then you also have to have the time and the willingness to sort of
[2134.44 → 2141.34] like search until the answer is found and that might live in docs that might live in a forum post or
[2141.34 → 2146.70] wherever it might be, and these language models are perfect at like matching pattern matching
[2146.70 → 2153.88] and things like that and so within an instant you know ChatGPT or copilot x or Cody or what have you
[2153.88 → 2160.64] can pretty much get you to like at least when it comes to programming answers to keep giving you
[2160.64 → 2165.10] direction it may not be the final production version of it Simon mentioned how he has scaffolded like
[2165.10 → 2170.80] the majority of a python based application or website or something like that, and he said well sure this
[2170.80 → 2176.24] isn't my final production code, but it's almost there it needs that final human touch to kind of get it past
[2176.24 → 2182.18] everything else and I'm I'm just hopeful that even though we're at that moment where there's innovation
[2182.18 → 2189.14] and there's the hype train so to speak that somewhere in there's enough that has said open source is
[2189.14 → 2196.14] one that it makes sense to make this free and available to humanity because we talked about that
[2196.14 → 2200.96] before again with Simon like if it's locked behind one organization's hands, or you know will there be
[2200.96 → 2205.94] a great consolidation yeah that's quite possible you know that's that's still quite possible but I'm
[2205.94 → 2211.74] hopeful that this last decade or more like even of this show we began this show in 2009
[2211.74 → 2217.20] right alongside of GitHub being founded like GitHub was founded in 2008, and we saw open source moving
[2217.20 → 2221.46] fast we said we got to keep up, and we started the blog we started the show and here we are almost 14
[2221.46 → 2226.74] years later still riding this open source train so to speak and I think it's one like it said
[2226.74 → 2231.58] it's kind of you take it for granted almost that it's going to be open source I'm hoping that
[2231.58 → 2237.60] truth and the power that that truth brings carries forward into this AI world that there's some
[2237.60 → 2242.88] open models that we can all adopt and will I do it of course not but am I hopeful I think I am
[2242.88 → 2248.94] yeah and the really hard math and statistics side of things are hard also for practitioners who are
[2248.94 → 2254.78] like working in the industry and so of course it's going to be overwhelming to youngsters coming to
[2254.78 → 2260.08] these things, but it's also overwhelming to us, you know quote unquote mature adults who are like
[2260.08 → 2265.36] working in software development we're very intimidated by those things but I think what we're finding is
[2265.36 → 2271.32] that a lot of the really difficult concepts are being you know lowered down to a place where
[2271.32 → 2275.62] you don't have to know exactly how this works, but you do have to know how to leverage it and that's i
[2275.62 → 2280.24] think the power of abstractions right and I think ultimately what you have is a person who learns how
[2280.24 → 2284.86] to leverage things and then as they're going about leveraging I know some people hate the term leverage
[2284.86 → 2290.26] but I'm using it in its literal sense here as you're doing that you know you run into problems and
[2290.26 → 2293.68] you get to a point where you've you've crossed the bounds of what you understand and what you
[2293.68 → 2298.74] don't understand and that's where just like natural you know autodidacts take over and you
[2298.74 → 2303.82] learn what you need to learn in order to get to that next phase and eventually over time you become
[2303.82 → 2309.30] the expert but I think that very much in the spirit of hat club Zach is that there are no teachers there
[2309.30 → 2314.28] right so I mean it's a lot of people who are at least willing to learn on their own or to be with
[2314.28 → 2319.34] other people who learn was that part of the mix from the start you're like we're not going to have
[2319.34 → 2324.66] teachers we're just going to hang out like I guess maybe backing up a step what's the exact
[2324.66 → 2331.28] structure like what is hat club operationally today is it I know it's hackathons but what else is there
[2331.28 → 2337.06] for people to actually interact with yeah so that club today is a few key programs the first is that
[2337.06 → 2342.44] there's a massive online community it's all ran through slack there are 25 000 teenagers that are a
[2342.44 → 2347.62] part of it we're about to cross 10 million messages sent, and it's one of the most active online
[2347.62 → 2353.14] discussion spaces for teenage coders anywhere and the discussions range from like what it's like
[2353.14 → 2358.32] being a teenager to like people do really highly technical stuff in their like one of the projects
[2358.32 → 2364.46] that was built now a few years ago by hack clubber was called nearly.js it's a parsing library for
[2364.46 → 2371.78] JavaScript it is now downloaded 2 million times a week on NPM and jQuery is downloaded 6 million times
[2371.78 → 2377.60] a week on NPM just to give that some perspective and this is something where it's like
[2377.60 → 2381.54] that was built by an 18-year-old at the time in their hack club meetings and talking about some
[2381.54 → 2385.36] of that work on the hacks of slack as they were doing it the second part of hack club is just
[2385.36 → 2390.42] hackathons, so these are 24 hours long coding marathons that happen on weekends, and they're
[2390.42 → 2396.78] all teenager organized there's roughly 50 to 100 that happen a year regionally and those are all led by
[2396.78 → 2402.10] teenagers the third is there are hundreds of after school hack club chapters where teenagers get
[2402.10 → 2407.38] together weekly to code together these tend to be more beginner oriented because again over 50
[2407.38 → 2411.68] percent of high schools in the U.S. don't offer a single coding class and in a lot of the schools
[2411.68 → 2417.78] were in like this is the coding thing that exists and what's cool is like when you come to a meeting
[2417.78 → 2423.14] it's not like you're signing up for a semester long commitment as a young person you're just seeing
[2423.14 → 2427.94] is coding something I'm into for an hour and as a result like you're also writing code that's
[2427.94 → 2433.34] meaningful and relevant to you, you're like shipping a project every week so it's like real contextual
[2433.34 → 2439.40] everything you're doing and then finally and this is where like you know the areas where I think
[2439.40 → 2444.70] hack club is fascinating and like it's unique is like we are really the first major
[2444.70 → 2451.56] educational organization structured and formed after the internet was already existed and what that
[2451.56 → 2455.78] means is that the hack the internet is part of hack club's DNA in a way where you look at other
[2455.78 → 2459.80] organizations they're still kind of trying to figure out how the internet affects their organizing
[2459.80 → 2465.26] and one thing that happens at hack club is anytime teenagers run into problems internal tools that are
[2465.26 → 2470.14] open source get built by the community that everyone starts using and that brings me to our final program
[2470.14 → 2476.42] which we call hack club bank and this is a financial tool it's almost like stripe atlas but for
[2476.42 → 2481.70] non-profits where if you want to start a non-profit or if you need a way to receive donations and we
[2481.70 → 2485.64] originally formed it because our teenagers kept trying to run these events that had no way to receive
[2485.64 → 2489.20] money because if you're under the age of 18 you can't open a bank account in most of the country
[2489.20 → 2494.76] it's a financial tool if you go to hackclub.com slash bank worth one click you can receive you get
[2494.76 → 2500.64] 51c3 non-profit status you can receive donations you get physical cards for spending funds you can you
[2500.64 → 2505.72] know manage it with your team and now there's a thousand and ten organizations many of them led by
[2505.72 → 2511.80] teenagers that run through hack club bank and there are millions of dollars that we process on behalf of
[2511.80 → 2516.42] these groups all over the country each year, so those are kind of our key programs today, so there's
[2516.42 → 2522.00] online community there are clubs there are hackathons there's hack club bank, and then we also do seasonal
[2522.00 → 2527.32] events and activities like one thing we did a few months ago was we did a project called winter
[2527.32 → 2533.48] hardware wonderland if you go to hackclub.com slash winter, or you did an open call, and we said hey if
[2533.48 → 2537.70] you're a teenager, and you want to build a hardware project you've never done that before buying
[2537.70 → 2542.88] components is expensive so we'll buy we'll buy all the components you need up to 250 dollars per
[2542.88 → 2547.60] project if you submit a pull request to this GitHub repo with your stuff if you meet the requirements
[2547.60 → 2553.08] and what and in total we had hundreds of projects built from like dozens of countries all over the
[2553.08 → 2558.68] world the projects ranged from like there was this one student I think in Greece who built a plant soil
[2558.68 → 2563.82] monitoring system for their parents garden that like helps you understand if like the soil has the right
[2563.82 → 2569.16] you know components and the right setup to grow the plants that you try to grow to like there's
[2569.16 → 2573.06] this one student in New York city who built a foldable kayak from scratch they want to get into
[2573.06 → 2578.60] woodworking so like they wanted that it's kind of crazy their final video submission was them
[2578.60 → 2585.10] in the kayak in the Hudson and there was like everything in between yeah it works, so those are
[2585.10 → 2590.38] that's kind of a high level overview and there's always new stuff happening like one of the things we're
[2590.38 → 2598.50] about to launch is a math game called sign writer if you go to sign writer.com s-i-n-e writer.com
[2598.50 → 2603.92] that's going to go live this Friday and that's this beautiful math game that a handful of teenagers
[2603.92 → 2608.40] and an engineer on our team have built together it's kind of like if you ever play with the ti-84
[2608.40 → 2613.16] or if you ever played a graphing calculators or now for young people today if you like demos
[2613.16 → 2617.84] this is like the ultimate game for you, and it's there's always stuff like this happening in the
[2617.84 → 2623.92] community to get involved super cool let me close a loop on that open tab uh free dolly 2.0 was
[2623.92 → 2631.50] just released today from Databricks the world's first truly open instruction tuned LLM, so this is
[2631.50 → 2640.00] a LLM open source and available uh to anybody with the opportunity of giving it you know instructions
[2640.00 → 2646.08] so that just another example alpaca a big one what's his name again this is called dolly 2.0 from the
[2646.08 → 2651.76] Databricks team they just uh released it today oh man they missed the opportunity to call it open
[2651.76 → 2656.90] dolly like hello dolly they said free dolly so I'm either just compensator or you know they're
[2656.90 → 2661.62] they're wanting to have the word free, and they're like free willy maybe anyway that's true free willy
[2661.62 → 2665.76] I just wanted to close that loop since I left it hanging open and I found my open tab
[2665.76 → 2671.48] let's focus in that's a lot of different programs man like different wings of hat club at this point
[2671.48 → 2675.82] let's let's talk about the after school program because I think there's so much potential power
[2675.82 → 2681.30] in that you know you got kids that don't you know fit in with the sports maybe they don't fit in with
[2681.30 → 2685.48] the drama team maybe they don't want to do this that or the other thing a lot of times if you don't
[2685.48 → 2692.10] have anything after school you end up merely either like bored at home watching TV or worse out getting
[2692.10 → 2697.46] in trouble, and so i am after school program for around technology I think is just spectacular how does
[2697.46 → 2702.54] that work you mentioned it's teenager run how do people find out about it how do the kids
[2702.54 → 2709.04] get involved and then how do you start one yeah well, so that clubs are groups of teenagers that get
[2709.04 → 2715.34] together weekly after school usually there's like five to 15 teenagers each club and the purpose of
[2715.34 → 2719.54] this is they're like mini hackathons that happen every week at your school if you're a teenager and you
[2719.54 → 2724.34] want to start a club you just go to hackclub.com there's a whole registration process we really work with
[2724.34 → 2729.90] everyone who wants to now we have what we kind of call internally like a club in a box setup where
[2729.90 → 2734.20] there's a whole set of open source materials that range from workshops so you can do inside your
[2734.20 → 2738.64] club meetings to marketing materials so we print millions of stickers that we ship to clubs all over
[2738.64 → 2744.62] the world and you if you do this you'd be joining this global community of other clubs all over the
[2744.62 → 2750.54] country all over the world we're all on the same mission as you and I think that for a lot of teenagers
[2750.54 → 2755.50] you don't really know other people that share your love and interest for technology or maybe if you
[2755.50 → 2760.40] have that first spark you don't really know what that like best way to get started is and we really
[2760.40 → 2765.12] believe in the hacker way which is that if you want to learn how to code the best way to do it is just to
[2765.12 → 2771.82] start writing code, and you know i I think that a lot of kinds of education programs around technology can
[2771.82 → 2777.34] try to be very elite where hack is not elite at all like we don't believe anyone is born with some
[2777.34 → 2781.86] special abilities that make you better at coding than others like we think your ability and as a
[2781.86 → 2787.60] coder is just a function of how many hours you spend coding and if you start a club, or you join a
[2787.60 → 2791.56] club at your school and come together weekly every week you're writing code for at least an hour
[2791.56 → 2797.52] that's a great entry point into the broader hack club ecosystem and the reason why we have all these
[2797.52 → 2801.94] other things that are happening in hack club too is that if you're a club member it's not super
[2801.94 → 2806.26] exciting just to come together weekly, and you write code the same group of people you want to feel part of
[2806.26 → 2810.72] something a lot larger than yourself so if you're part of a club you're going to hackathons happening
[2810.72 → 2817.02] near you there's online stuff you're participating in kind of whole gamut of stuff but the best way
[2817.02 → 2821.72] to start is just go to hackclub.com and check it out I love that so how do you reach schools and
[2821.72 → 2827.80] teenagers who have no idea that hack club exists it seems like there's probably a lot of those and
[2827.80 → 2831.98] there's probably like that perfect prototype teenager who's at their school wishing for something
[2831.98 → 2837.76] like this, but they're just not aware are there ambassador programs are there ways is there ways
[2837.76 → 2843.22] for adults to like to help this mission without necessarily start because you can't start a hack
[2843.22 → 2847.82] club but could you make help with awareness because like a lot of our listeners and myself for instance
[2847.82 → 2852.92] we can't start hack clubs, but we would love to help spread the word somehow are there official or
[2852.92 → 2859.64] better ways of doing that yeah the reason why everything at hack club is student-led is because that is a
[2859.64 → 2864.64] found the model that works best through that probably the best way if you're an adult and wanting to
[2864.64 → 2870.52] help support hack club in your community or if you have kids that are interested in technology is to go
[2870.52 → 2875.84] to hackclub.com and there's an email list at the bottom that you can sign up for what we found is the
[2875.84 → 2881.06] the best way to help new people get into the ecosystem is every roughly two to three months will launch some
[2881.06 → 2886.78] sort of new product that teenagers can engage with directly one I mentioned earlier was Sprague which was
[2886.78 → 2891.96] that open source game console another one is sign writer which we're doing now another one that's coming
[2891.96 → 2898.02] up is we're building this like open source almost like CNC machine where it's you know fully 3d printed
[2898.02 → 2903.70] it's really cheap to build and with all these projects there's some element of like if you're a teenager
[2903.70 → 2909.14] and you're an individual, and you do some action that's educational in nature where for example a sprig if
[2909.14 → 2914.20] you build a game, and you ship it we'll ship you a free console so the parts to build your own with the new
[2914.20 → 2917.76] drawing machine if you know we're doing like a generative art thing where if you make some
[2917.76 → 2921.68] general piece of art using code and ship it we'll then ship you all the components you need to build
[2921.68 → 2926.10] your own machine that can actually produce that art so signing up to that email list sharing those
[2926.10 → 2929.98] things with the young people in your life that tends to be a great entry point in the hack club
[2929.98 → 2935.76] because starting a club out the gate that's like a big commitment and clubs only really succeed or fail
[2935.76 → 2941.26] at schools based on the student leadership, and sometimes we'll get like you know like a parent or like a
[2941.26 → 2944.94] teacher will be like I really want to make a hack club start at my school, and they'll start meetings
[2944.94 → 2948.54] or something like that, but they don't really have that teenager that falls in love with it and really
[2948.54 → 2953.24] wants to make it their own and what happens is it always fizzles out after a few months like you have
[2953.24 → 2957.74] to have that charismatic leader on the ground so that's where we have this kind of other entry points
[2957.74 → 2962.80] for people into the hack club ecosystem yeah what you see on that home page or at least the landing page
[2962.80 → 2968.72] for it says don't run your coding club alone make it a hack club so I guess the secret model really is
[2968.72 → 2973.54] don't be alone when you do this you know something that um and jarred I don't know if you were in a
[2973.54 → 2978.78] fraternity when you were in college or not but I know my wife she was in a sorority, and she had a
[2978.78 → 2985.98] sorority mom, and she's like our surrogate grandmother to this day like she's super close in our life I wonder
[2985.98 → 2991.52] if you can have or if you've thought about models where you can involve a sorority mom to a sorority isn't
[2991.52 → 2996.52] there to sort of guide the sorority they don't run it, but they're there to sort of help with adult things
[2996.52 → 3002.18] I suppose you know and to be a guide and to be a mentor to be you know an inspiration to some degree
[3002.18 → 3010.06] with those younger folks in that club basically sorority fraternity similar in nature have you guys
[3010.06 → 3015.60] considered how is that the extent that you let adults sort of play roles like I get it you know
[3015.60 → 3021.06] they're going to fizzle out if you don't have a teenager who's really charismatic as you said and
[3021.06 → 3026.56] you know involved is there a model where like there's a sorority mom type person that can play a
[3026.56 → 3032.36] role right now that happens unofficially but I love the idea we don't have anything kind of formal to
[3032.36 → 3037.50] facilitate that but I love the idea of figuring out how to do that I mean when I think about my own
[3037.50 → 3043.30] story like I feel so lucky to have met adult mentors as a teenager because I think if you don't
[3043.30 → 3046.86] know any adults that do the thing you want to do it's really hard to picture yourself doing it
[3046.86 → 3052.36] and we see this particularly among the young women in our community, and we do have some specific
[3052.36 → 3057.26] programs like for example we have a new partnership with the girl scouts where we're we're partnering
[3057.26 → 3062.38] with different girl scouts regional councils we just did our first one in New York city to run events
[3062.38 → 3068.02] that are like 12-hour coding days for local girl scouts that area ran by hack clubbers, and then we'll put
[3068.02 → 3074.16] together a dinner afterwards to pair hack clubbers with female mentors and that has been a really
[3074.16 → 3079.24] effective model so far and I love the idea of growing that into something a little more formal
[3079.24 → 3084.32] right now the way most teenagers hear about get hack club is we pair with a few different
[3084.32 → 3090.26] organizations in the space namely GitHub is probably our number one server partner where
[3090.26 → 3095.60] they will send out blasts to every student on GitHub about hack club usually every other month or so
[3095.60 → 3100.96] and we partner with them on a lot of our programs and then secondly we work with first robotics
[3100.96 → 3107.00] they're the largest engineering education program in the country uh they have 600 000 students across
[3107.00 → 3111.20] America and the world that do like robotics and stuff like that if you've ever seen a teenager
[3111.20 → 3115.38] doing robotics they're probably part of first, and they're starting to roll out hack club materials to
[3115.38 → 3120.76] a lot of their teams because they have teenagers that want to do more coding but I love that idea of
[3120.76 → 3126.96] of having some more formal mentorship models well I mean to give a role really i I totally get that it
[3126.96 → 3132.66] needs to be you know teenager ran totally get that even teaches them responsibility I mean like it you
[3132.66 → 3137.22] know this thing doesn't a hack club unless you show up and the folks that you've connected with
[3137.22 → 3143.02] show up and make it a thing here are some folks that will be you know assistive with the process of
[3143.02 → 3147.56] running it, or you know maybe there's an adult required for x I don't know whatever but something
[3147.56 → 3154.80] where you got that osmosis from older to younger generation seems to be like a thing now jarred I'm
[3154.80 → 3159.82] thinking too with our audience like sure we don't have a teenager audience by any means but I bet you
[3159.82 → 3163.64] got a lot of parents in this audience right somebody's listening right now thinking gosh i
[3163.64 → 3168.04] got kids and I care about hack club probably both yeah I'd love to find a way where we can help you
[3168.04 → 3173.84] Zach to be similar to GitHub or uh first robotics to just I don't know how we can do that necessarily
[3173.84 → 3179.52] without just being like hey let's just put you on blast but somehow incorporate something to share
[3179.52 → 3185.68] with audience because I'm sure we've got if not parents they're godmothers or uncles or aunts or
[3185.68 → 3192.28] whatever to younger generation folks in their lives that matter, and they're going to share the idea
[3192.28 → 3198.36] and the model of hack club with them thank you yeah that would be amazing and we know kind of like
[3198.36 → 3203.46] I mentioned at the beginning for everyone listening and for both you as well like hack club is a
[3203.46 → 3209.68] volunteer led community and a non-profit that is here because you know all of us involved have had
[3209.68 → 3214.20] some experience where technology has touched us in a personal way, or it's made us a different person
[3214.20 → 3220.16] today than we would have been without it and like that is something that is so important for us as a
[3220.16 → 3227.38] society to give as a gift to the next generation and hack club is like you know such a gift when someone
[3227.38 → 3232.68] is looking for it so spreading the word helping young people become aware of it so often we'll hear
[3232.68 → 3236.82] stories from a young person well they're like oh my god my mom told me about this and I've been
[3236.82 → 3240.76] looking for something like hack club for years I didn't even realize there were other people my age
[3240.76 → 3247.80] that shared my love for this the beauty I think of separating it from an official school thing is the
[3247.80 → 3254.16] freedom that you have to sort of like partner up, and it only happens if there's uh motivation right
[3254.16 → 3258.96] like you, you're not going to force hack club into a world where it doesn't need to exist it kind of
[3258.96 → 3265.04] happens because the idea of hack club makes sense and that it's ran by you know the folks who are
[3265.04 → 3269.40] really interested I just think like maybe the hurdle I thought you may have faced earlier like I said
[3269.40 → 3274.82] before was like the educators but clearly that's not necessary because you have sort of individually
[3274.82 → 3280.60] ran hack clubs but that's kind of probably the beauty of it is it doesn't have to be like this
[3280.60 → 3285.58] staple this is a funded program into x, and then it gets falls by the wayside the next thing you know
[3285.58 → 3290.40] it's sort of like not what it began as like you had great ambition for the thing but eventually it
[3290.40 → 3295.44] just turned into this not hack club essentially yeah I mean imagine if to start open source project
[3295.44 → 3299.16] you had to get a grant first and approval from five different people like there would be no open
[3299.16 → 3305.36] source community that would be crazy like I think that the way I think about it is I think in education
[3305.36 → 3311.16] there are basically two models of learning one model is high floor low ceiling this is a traditional
[3311.16 → 3315.54] school and a traditional school day when you have guarantees on what everybody's going to learn you have a
[3315.54 → 3319.46] textbook you have curriculum you have tests you have ways to make sure everyone leaves
[3319.46 → 3325.44] with certain competencies, but it's very challenging for folks to go off that like default path and then
[3325.44 → 3329.66] I think you know there's a second type of learning model where you have a low floor and a high ceiling
[3329.66 → 3334.50] where it's hard to give certain guarantees of what some people will get out of the program but those
[3334.50 → 3341.22] who want to go really really really far can and I think open source as a model is a low floor high ceiling
[3341.22 → 3347.34] model and I think that the future of education is blending both of those and I think that you know
[3347.34 → 3351.58] the beauty of hack club is that since it is opted this is something that teenagers really want to be
[3351.58 → 3356.58] a part of since we don't really have a captive audience in the same way that a lot of classrooms do
[3356.58 → 3360.48] like you know if you're a hack club like you actually want to be there and if for some reason
[3360.48 → 3365.14] you want to be there you just don't show up anymore and that's totally fine it means that when you as a
[3365.14 → 3370.26] teenager get involved you're connecting with other teenagers that are also opting in and making that choice to be
[3370.26 → 3374.38] there and I think the internet kind of it's interesting when you think about what the future
[3374.38 → 3379.46] of learning will look like I think one of the biggest transformations that's happened in education
[3379.46 → 3384.72] and learning in the past you know 15 years that still isn't really being talked about is so much
[3384.72 → 3390.38] of our institutions of learning are built around solving the access problem how do we simply get all
[3390.38 → 3395.74] this information that we want people to learn in front of them and available to them and worldwide we've
[3395.74 → 3402.18] built in my view an incredibly effective really amazing top-down one-to-many distribution mechanism
[3402.18 → 3408.18] where like we've made so that like basically entire societies literate it's amazing but with the internet
[3408.18 → 3413.54] we have this new thing where the access problem is really solved every person who has access to a phone
[3413.54 → 3417.30] and the internet has access to literally all of human history and knowledge in our pockets
[3417.30 → 3423.28] and the new challenge of education and learning is not just how do we simply get people access it's like how do we get
[3423.28 → 3428.94] people to spend their time unlocking the secrets of the universe rather than doom-scrolling through twitter
[3428.94 → 3435.20] and i I think the answer is you know you make it fun you make it community oriented you make it something
[3435.20 → 3440.36] where you know I think the thing that we've really realized with hat club and a lot of other people
[3440.36 → 3444.94] who are pursuing these models have realized is that learning and making things and manipulating the world
[3444.94 → 3450.82] around you that is like a fundamentally human and satisfying thing that we've been doing since the dawn of our
[3450.82 → 3456.08] species and once you help someone realize like oh my god like I can do this through coding I can do this
[3456.08 → 3460.58] through this other subject and like get really deep into something on the internet it is so much more
[3460.58 → 3465.98] exciting so much more compelling so much more fun than like watching Netflix, and it's like addictive
[3465.98 → 3471.48] like you literally can't pull yourself away from it and I think the question of learning in the future
[3471.48 → 3476.08] is like how do we make learning fun and I think we'll see a lot more models like hat club I think hat club
[3476.08 → 3480.64] needs to be a lot better to better provide that experience for the people where you know we're
[3480.64 → 3482.50] touching them but not totally having that yet
[3482.50 → 3503.82] what's up friends this episode is brought to you by CIQ the founding sponsor and partner of rocky Linux
[3503.82 → 3510.36] enterprise Linux the open source community way and I'm here with Gregor chertier the founder and CEO of
[3510.36 → 3517.46] CIQ and the creator of rocky Linux so Greg I know that a lot of people are still sort of catching up to
[3517.46 → 3524.90] some degree with what went down with CentOS the red hat acquisition and just the massive shift that
[3524.90 → 3531.34] required everyone using CentOS to do give me a give me a glimpse into what happened there we've seen a
[3531.34 → 3536.36] number of cases in the open source community where projects were pivoted due to business agenda or
[3536.36 → 3542.30] commercial needs we saw that happen with centos was one of the primary one of the biggest
[3542.30 → 3548.94] enterprise operating systems ever people were using it all over the place enterprise organizations
[3548.94 → 3556.30] and professional it teams were all leveraging CentOS for CentOS to be stripped away from the community
[3556.30 → 3562.80] and removed as a suitable option to meet their needs created a massive pain point and a gap within
[3562.80 → 3568.26] the industry as one of the founders of CentOS I really took this to heart and I wanted to ensure
[3568.26 → 3576.34] that this does not happen again and that is what we created with rocky Linux and the RESF okay you
[3576.34 → 3584.26] mentioned the RESF what is that and what is its relationship to rocky Linux the RESF is the rocky
[3584.26 → 3591.54] enterprise software foundation, and it is an organization that we created to hold ourselves
[3591.54 → 3597.50] responsible to what it is that we've promised that we're going to do with the community it is community
[3597.50 → 3604.88] run it is community led we have a board of directors which comprises a number of people that have a
[3604.88 → 3610.90] huge amount of experience both with Linux and open source and community and from this organization
[3610.90 → 3618.50] we solidify the governance of how we are to manage rocky Linux and any other projects that come and
[3618.50 → 3624.84] join in this vision sounds good great I love it so enterprise Linux the open source way the community
[3624.84 → 3632.08] way has a home at rocky Linux and the RESF check it out and learn more at rocky linux.org
[3632.08 → 3637.08] slash changelog again rocky linux.org slash changelog
[3637.08 → 3656.22] can we uh break down the flow of getting started I guess then because you got step one is application
[3656.22 → 3662.78] you start by telling you know you all hack club themselves you know who you are who's leading it
[3662.78 → 3667.86] etc then you have an onboarding call which i have to imagine is like the funnest time ever for somebody
[3667.86 → 3673.32] at what you call hack club HQ you help on a Zoom call with someone and I assume that's just to connect
[3673.32 → 3677.72] the dots to make sure they're a real human being, and they're not trying to gain I can only imagine the
[3677.72 → 3683.08] fraud waste and abuse you must have in this process, but we'll set that aside to focus on what's
[3683.08 → 3687.24] actually mattering here but then the next one is the first meeting so like you, you said
[3687.24 → 3693.44] before a hack club in a box walk us through that flow how that works and that first meeting to the
[3693.44 → 3699.02] 10th meeting how do you ensure without overly hand-holding the process that this is successful
[3699.02 → 3704.24] and it has the right tooling and that there's a similarity or is there a similarity to hack club
[3704.24 → 3710.70] to hack club is it does it even matter to have similarity yeah totally I mean I think the first thing
[3710.70 → 3715.14] to understand is like clubs are a part of hack club, but they're not like the primary thing like I would
[3715.14 → 3721.68] say maybe only 25 percent of students in a club are actually in a club or engaged in a club okay and
[3721.68 → 3726.82] that was a transformation that the pandemic really had we were almost entirely clubs before that
[3726.82 → 3733.12] and once the pandemic hit we like you know I think we're very early to realize that things were going
[3733.12 → 3738.62] to be totally different, and we also saw that the space was arranged in such a way where we thought
[3738.62 → 3742.82] every other organization every school was going to try and do exactly what they were doing in person
[3742.82 → 3747.32] but in Zoom calls instead and like that's a terrible idea like what's going to be best for the internet
[3747.32 → 3752.50] is totally different from what's best in person, and we really double down on like how do we build an
[3752.50 → 3756.68] amazing online community how do we build an amazing opportunity for people to contribute to hack club
[3756.68 → 3762.08] beyond clubs how do we build like different flows for people and in the first few months of pandemic
[3762.08 → 3768.24] our community grew 700 because so many people from other spaces were finding hack club as like a space
[3768.24 → 3773.00] where there was stuff happening that made sense on the internet for clubs specifically a lot of it's
[3773.00 → 3776.94] actually student-led so like if you're a teenager, and you're like I want to start a hack club or I want
[3776.94 → 3781.98] to start a club you applied you fill that out a lot of that is just basically just stick stuff on our
[3781.98 → 3785.54] end and make sure that when we send you all the material physically because we actually you know send
[3785.54 → 3790.28] physical materials in a lot of cases you're going to be able to benefit from that we accept everyone we can
[3790.28 → 3794.46] the real flow and the real magic happens when you join the slack and when you join the community
[3794.46 → 3799.18] and what happens is after you apply you get an invitation you join the community, and you're talking
[3799.18 → 3804.70] with other teenagers your age from other schools that are doing the exact same thing as you and
[3804.70 → 3810.34] what's so cool about that is you know there's this to kind of get just like on a more of a society level
[3810.34 → 3815.16] there is this piece in the air times recently that talked about how like cross zip code friendships
[3815.16 → 3820.16] like are one of the number one predictors of whether someone will rise in like social
[3820.16 → 3825.16] class like do they have friends in other social classes and I think it's such a shame that our
[3825.16 → 3830.26] education system today is so highly dependent on what zip code you have to be born in and you really
[3830.26 → 3835.56] don't interact much at all with teenagers from other locations even though they might share your
[3835.56 → 3839.84] same interests so the coolest thing with hack club is like when you join and when you get involved and
[3839.84 → 3844.06] when you know getting started with starting your club you're talking to other teenagers that are
[3844.06 → 3847.26] already doing that activity successfully you see what it can look like you're having one-on-one
[3847.26 → 3851.42] conversation you ask some questions in the public channels you're getting on Zoom calls of people
[3851.42 → 3855.02] where they're really walking you through things you're getting invites to hackathons where suddenly
[3855.02 → 3858.66] you're not like this one weird teenager at your school that has this interest where you're struggling
[3858.66 → 3862.84] to find support you're like part of a whole community of people that share your love share your
[3862.84 → 3868.72] passion share your interests more tangibly like you know most hack clubs are pretty focused on
[3868.72 → 3874.66] how do we simply get people in the room and how do we make coding a really fun one-hour activity
[3874.66 → 3879.30] because our thesis is like look if you come in and have a great time you're going to come in again
[3879.30 → 3885.26] next week it's like a party how do you make it fun and what we focus on in hack club meetings is
[3885.26 → 3889.78] shipping something because there's nothing more satisfying than having an idea and making something
[3889.78 → 3894.84] that you didn't think you were capable of doing possible so that first meeting that every hack club
[3894.84 → 3900.12] leader has their goal is how do I get 25 plus people in the room and how do I make sure every single
[3900.12 → 3904.56] person that I bring leaves the room having actually made a real project with a real URL by
[3904.56 → 3909.52] making real code even if they don't understand all the code that they wrote, and you know we have
[3909.52 → 3913.72] a lot of like training materials and stuff like that but like i I would say the beauty of it is
[3913.72 → 3918.74] really where you're connecting with teenagers from other schools where you're seeing them do it
[3918.74 → 3923.00] successfully, and you're realizing that like you're not this weird person on your own you're part of
[3923.00 → 3927.68] this broader community this broader movement of people your age that share that love share that passion
[3927.68 → 3933.08] share that interest can we get into the community weeds for a moment because I'd love to have your
[3933.08 → 3940.46] take on slack as a platform for this community I noticed on the web page you say slack it's kind
[3940.46 → 3945.88] of like discord so you're explaining to your potential members that it's like discord which is something
[3945.88 → 3950.60] that they must be more familiar with we have a slack that we've been on for years now right, and it's
[3950.60 → 3956.78] you know thousands and less than 10 000 but enough people where it's like okay moving this would be
[3956.78 → 3962.84] difficult but there are things about slack that we don't love and I'm just curious if you're loving
[3962.84 → 3966.92] slack if that was a choice that you made that you now regret or if there's a partnership there or
[3966.92 → 3972.12] what's your take on slack for communities of this size yeah well first I'll say thank you slack for
[3972.12 → 3976.38] doing slack to hack club um because there's no way we can afford it there you go so that that's
[3976.38 → 3981.94] only part of it, but it's been fascinating because so for me when I was a teenager I was on IRC
[3981.94 → 3986.82] and I was kind of on the later days of IRC most of you I talked to were like oh you should have seen
[3986.82 → 3993.26] it in the early 2000s, or you should have seen in the 90s it was so awesome and with slack we started
[3993.26 → 3998.22] our slack in 2015 so like we really were there right at the beginning I remember when slack left
[3998.22 → 4003.52] beta like we were one of the very first users on it, and you know discord didn't exist, yet later we saw
[4003.52 → 4009.64] discord emerge and we early on had a lot of conversations whether we made sense to
[4009.64 → 4014.40] move the hack club community to discord and what's interesting today is like teenagers do not know
[4014.40 → 4018.12] what slack is they've literally never heard of it for almost every teenager who comes into hack club
[4018.12 → 4022.40] it's the first time they've heard of slack they're familiar with discord all their friends use discord
[4022.40 → 4026.50] they all have group chats on discord and stuff like that because if you have friends who have android
[4026.50 → 4033.44] phones and iPhones i the best way to boot group chat is through discord so with that I think slack is
[4033.44 → 4038.94] better for communities and discord is depending on your community the reason why we haven't switched to
[4038.94 → 4045.00] discord is for a few reasons the first is that if we were to have the hack club community be on discord
[4045.00 → 4051.12] the network that you're part of is discord and the server you're on is hack club so like when you have
[4051.12 → 4056.42] interactions discord it's set up in such a way to pull you outside your individual server as much
[4056.42 → 4060.96] as possible as when you dm someone you don't dm someone within the context of that server you dm them
[4060.96 → 4066.28] you know in the context of discord and what that means is that as soon as people make friends or have
[4066.28 → 4071.34] some sort of connection rather than contribute back to your community because you actually can't make
[4071.34 → 4074.78] your own channels and discord and stuff like that you have to have the admins make the channels or
[4074.78 → 4078.52] you can have some really clever bot thing which is extremely confusing for people who aren't like
[4078.52 → 4083.94] really deep in the weeds with discord you go off and make your own server and hack club only works
[4083.94 → 4088.80] because teenagers are like building the spaces they want within the hack club sphere to make it better
[4088.80 → 4094.02] for everyone it's like a positive sum game where discord we thought that the dynamic would be such that
[4094.02 → 4098.56] there'd be a lot of value pulled out of hack club put into the discord network rather than kept within the
[4098.56 → 4104.32] hack club community the other thing that we like more about slack than discord is that and this is maybe a
[4104.32 → 4111.46] little specific to our community but since teenagers don't know what slack is we are the only for most of that
[4111.46 → 4118.24] we are the only slack workspace that they are in and that means that as a result there's basically the hack club
[4118.24 → 4124.38] app on every hack club or stone and the hack club app on every hack club or computer without us like there's no way
[4124.38 → 4130.64] we can afford to build you know like a hack club app or get people to use it being a small nonprofit without lots of
[4130.64 → 4138.28] engineers the last thing I'll say on this is that slack given that it's meant for companies has extensive APIs
[4138.28 → 4145.78] you heavily customize a slack experience and in a way that you just can't with discord and as a result there's like all this
[4145.78 → 4150.34] magic that happens in a club that I think wouldn't be happening if it was through discord one good
[4150.34 → 4155.14] example of this is like you know a couple of years ago some hack clubbers decided to make a channel for the
[4155.14 → 4159.12] count to a million where they said you know what let's count to a million together one message at a time
[4159.12 → 4164.78] you're not allowed to put two numbers in a row and like this whole ecosystem of bots emerged around like
[4164.78 → 4169.54] enforcing the rules having leaderboards seeing who's doing well and that's the sort of thing that can't
[4169.54 → 4174.62] happen on discord because people can't make their own channels so I would say the reason why we stick with
[4174.62 → 4179.70] slack instead of discord is do we think of hack club as its own ecosystem not as one part of the
[4179.70 → 4185.66] broader discord ecosystem I didn't quite consider that the pandemic would have hit you guys like that
[4185.66 → 4189.76] that totally makes sense now in retrospect because I just wasn't thinking about that's the before times
[4189.76 → 4195.30] you know and I'm its post pandemic to some degree in a lot of ways, and so I'm like okay that never
[4195.30 → 4200.60] happened I just forget that two years or whatever it was right it's just gone so I'd forgotten that you
[4200.60 → 4205.50] know getting together people face to face was a challenge, and now it's less so now it's still a
[4205.50 → 4211.14] challenge because you still have concerns and issues but it says down here events on zoom that don't
[4211.14 → 4215.98] suck you got AMS you got hack night you got minecraft you got community funds so like you're doing what you
[4215.98 → 4224.10] would have normally done in the hour after school in remote ways or distributed ways i have to imagine that's
[4224.10 → 4230.00] help with growth but also just with inventiveness now like with the whole zip code idea I agree with
[4230.00 → 4234.60] that like the social possibility for a human being that knows somebody beyond their own zip code has
[4234.60 → 4241.64] got to be greater and I'd love to like to dig into the stats behind that, but this lets you join a cohort
[4241.64 → 4246.58] my wife right now is in a book club for like the last year or so she started to lead it, and it's been
[4246.58 → 4250.32] one of the most positive things I've ever seen happen in her life this book club has become like
[4250.32 → 4257.68] sisters to her and uh and like I'm seeing this idea of like clubs, and you need to belong somewhere
[4257.68 → 4262.42] and as a kid like where do you belong initially right or as a teenager well you've got your home
[4262.42 → 4267.04] base you've got your family right and that's obviously where you fit unless you don't fit and
[4267.04 → 4272.30] you have home issues and that's just an absolute shame the next place you fit obviously is school
[4272.30 → 4277.24] because that's by nature sort of forced on you as a child you have no other choice but to go to school
[4277.24 → 4281.52] you want to learn but is that the place you want to go maybe not, but you are forced to go to school
[4281.52 → 4285.68] so you have that following in that group where else do you get it at you get sports or other things
[4285.68 → 4291.02] like jerry was saying like chess club drama club sports etc but if you don't fit in those things you
[4291.02 → 4296.66] need somewhere to belong and this I think is such an interesting way like if you're in this world where
[4296.66 → 4303.84] coding or technology matters to you, you don't have to have an after-school program you could just go
[4303.84 → 4309.60] online and join the slack no matter where you're at and join with these AMS or the minecraft thing
[4309.60 → 4313.86] or the whatever it might think to be across zip codes and meet some people that's so cool but
[4313.86 → 4319.16] events on zoom that don't suck is the premise there but that's so cool that you can like do
[4319.16 → 4324.42] hack club but not have to be in person well we're building on that like when you think you know and
[4324.42 → 4329.40] that was a huge realization we had during the pandemic we were like oh snap like this is way better
[4329.40 → 4334.26] and actually helps people have better in-person experiences too it also means that the perpetual
[4334.26 → 4338.74] challenge pre-pandemic was how do we have a relationship as hack club as a brand and as a
[4338.74 → 4343.18] like right HQ with members because we have this intermediary who are leaders and there's this
[4343.18 → 4348.16] chat both the best part and the worst part of hack club is that every year all of our most experienced
[4348.16 → 4351.64] people become alumni because you don't go to high school to stay there forever you go to high school
[4351.64 → 4355.78] to graduate and on one hand that means there's always room for fresh blood there's always new
[4355.78 → 4360.16] leadership opportunities there's always like new voices in the room but on the other hand it means
[4360.16 → 4364.60] that it's very hard to build up institutional knowledge, and we had basically thrown the towel
[4364.60 → 4368.54] and we're like you know what like after the leader graduates that club's dead someone else is
[4368.54 → 4372.78] willing if someone else wants to they can restart a club without school, and we consider a new club
[4372.78 → 4375.92] not a continuous just same one because nobody wants to inherit something you want to be the
[4375.92 → 4381.44] founder of your own thing for sure yeah and what we realized post-pandemic was like wow actually
[4381.44 → 4386.72] hack club where like with a lot of education groups or a lot of you know similarly structured
[4386.72 → 4392.06] things like the scouts if you ask the question of what is the fundamental unit of this thing it's
[4392.06 → 4396.48] the group it's either like the fundamental unit of schools is a classroom the fundamental unit of
[4396.48 → 4402.32] scouts is a true the fundamental unit of hack club was the club, but that's simply if you think about it
[4402.32 → 4406.26] like that's a constraint of physical world because you can only have relationships with so many people
[4406.26 → 4410.70] when you're going through the internet the fundamental unit can be the individual, and we've really
[4410.70 → 4414.48] shifted the hack club approach to be something where you know you don't need to be part of a
[4414.48 → 4418.86] club you don't need to like to run a club you can engage a hack club directly as an individual and if
[4418.86 → 4423.16] you later start a club or try on a club that's great, but we don't really recommend that as a starting
[4423.16 → 4428.12] point anymore and that's where things like you know one of the best call to actions right now is
[4428.12 → 4434.42] if you're a teenager, and you want to make a video game go to hackclub.com slash sprig there's its a
[4434.42 → 4438.54] really awesome really fun way to get started game development and if you ship a game you get a free
[4438.54 → 4444.06] console that that's open source mailed to you for free, and we have lots and lots and lots of call
[4444.06 → 4448.72] actions like that we do now and those have been great ways for people to get involved in the
[4448.72 → 4453.28] community and I think the future of education is like more things where the fundamental unit of the
[4453.28 → 4460.48] interaction is the individual rather than the group so a large online community of 25 000 plus
[4460.48 → 4465.60] teens or post teens I assume you can probably continue to hang out you don't get you don't get
[4465.60 → 4471.50] booted at age 20 do you get to hang out still you don't get booted but the social expectations you
[4471.50 → 4475.38] should make room for people kind of age out eventually that makes sense but what I'm aware
[4475.38 → 4482.06] of thinking is like how much time and effort and distraction I guess perhaps is involved with
[4482.06 → 4488.72] moderation because you know teenagers can get rambunctious I remember myself when I was a teen you
[4488.72 → 4492.86] know you wouldn't want me in your slack necessarily is that been a problem or there have been a lot of
[4492.86 → 4496.74] incidents is it not an issue or do you have a lot you have a team that just sits around, and you know
[4496.74 → 4501.58] make sure everybody's abiding by the code of conduct and doing what they're supposed to do
[4501.58 → 4506.80] yeah so at this point with all the different programs that we have I I would say there's
[4506.80 → 4511.56] probably somewhere between 50 and 100 teenagers that kind of have like official positions in some
[4511.56 → 4516.06] way shape or form helping make what happened and a handful of those positions are on the moderation
[4516.06 → 4520.86] team in the community most of the stuff is pretty minor I mean we have a pretty robust code of
[4520.86 → 4526.50] conduct and um we're we're pretty I think proactive in our moderation approach like
[4526.50 → 4531.06] sorry but backup's not a democracy we have certain things that we're okay with so things we're not
[4531.06 → 4536.20] okay with, and it's not going to be decided by consensus it's like you put the foot down so most
[4536.20 → 4540.58] things get nipped in the butt early I'd, I'd say we have some sort of moderation incident like every
[4540.58 → 4546.12] other month or something like that, and really you know I think one thing that's a little unique about
[4546.12 → 4551.96] us is that since we work with teenagers like change is fundamentally part of what it means to
[4551.96 → 4555.80] be a teenager yeah so a lot of communities you know you get permanently banned you get permanently
[4555.80 → 4559.64] kicked out, and we're like no like we're never going to give you a chance again we're in hat club our
[4559.64 → 4563.78] whole moderation approach is built on this idea that you know people grow people change and the
[4563.78 → 4568.86] thing that we primarily look for is good faith behaviour so like to answer your question like I don't
[4568.86 → 4573.92] think we have anything that that's very extensive as issues occasionally some stuff blow up
[4573.92 → 4579.14] but the beauty of hat club is that people also tend to self-moderate one thing we see that a lot
[4579.14 → 4582.70] of teenagers get a lot of value out of hat club and one thing they like a lot about hat club
[4582.70 → 4588.36] is in a lot of online spaces and this really I think accelerated towards the end of the pandemic
[4588.36 → 4592.82] people begin to realize that it's easier to get attention through being outrageous and through being
[4592.82 → 4598.74] helpful right and particularly in spaces where like you know you're gathering over some technical
[4598.74 → 4602.64] interests you would see very loud people dominating a lot of the conversations
[4602.64 → 4608.68] and I think one thing teenagers really like about that club is that our two values and our online spaces
[4608.68 → 4614.58] are one wholesome and two being technical so if you're a teenager where like you just want a low
[4614.58 → 4620.08] drama space to like to build as a coder get recognition work with other people catch other like-minded people
[4620.08 → 4625.76] hat club is a very wholesome place and people are invested in keeping it a wholesome place, and we're very
[4625.76 → 4630.28] deliberate about making sure that the only way to rise in like the social hierarchy of the community
[4630.28 → 4635.94] is through contributing being helpful giving more than you take rather than being loud outrageous
[4635.94 → 4642.24] etc and um I think that those are values that you know compound over time as yeah as you all them
[4642.24 → 4649.04] I love that emphasis on wholesome because uh you know technology is very powerful and especially when
[4649.04 → 4653.60] you start to learn how to wield it you know i I used the word leverage earlier, and you are operating at
[4653.60 → 4658.60] high leverage right you can do a lot with a little and I know that it's tantalizing and sometimes cool
[4658.60 → 4666.02] to do things that are perhaps malicious like because you can like prank sinister like oh we
[4666.02 → 4670.22] can get it with this because I know how, and it's easy to get riled up around those things these bad
[4670.22 → 4675.54] ideas that float somebody floats a bad idea it's not but if you have wholesome as a core value and I'm
[4675.54 → 4678.86] not sure if this actually weaves its way through your code of conduct or not because I haven't read it but
[4678.86 → 4684.70] certainly your moderation teams and your leadership which will emphasize these things like those bad
[4684.70 → 4689.78] ideas that sound good, and maybe they'll be funny maybe be interesting it'd be hard to do
[4689.78 → 4694.56] they're if they're doing damage they're not wholesome so like having wholesome as this core
[4694.56 → 4700.52] part of what hack club is I think will go a long way to combat what is your know kind of natural for
[4700.52 → 4705.38] young people when they have some power that they find is like doing things along the fringes of
[4705.38 → 4711.14] of damaging so I think that's going to serve you well thank you yeah and I think that like
[4711.14 → 4716.76] you know when i think about the long-term mission of hack club i I think values and being
[4716.76 → 4720.64] a space where young people can find really positive values and that and actually like
[4720.64 → 4726.20] like so often when you're in programmer spaces particularly as a young person the people who
[4726.20 → 4731.64] are more technical will be kind of cynical or be like a little mean or be a little like you
[4731.64 → 4736.52] know uh short-tempered or stuff like that particularly I think though the people who tend to be more
[4736.52 → 4740.22] technical than you would hang out and spend time if people are younger than them and kind of want
[4740.22 → 4744.62] to be put in that mature position I'm sure both of you have experienced that with others in some
[4744.62 → 4749.10] way shape or form I think it's really important that there's a path that's like very we were like
[4749.10 → 4754.32] I can be really successful and really ambitious and like really want to be someone who writes myself
[4754.32 → 4760.12] under the pages of history and I can be a nice wholesome positive person and when you look at
[4760.12 → 4764.50] groups like the girl or boy scouts I think they do a really great job with that like you know you
[4764.50 → 4768.12] talk to anyone who made it to an eagle scout, and they're like yeah like they all up their pretty
[4768.12 → 4773.38] consistently good people and have shared values and talk about how that experience really helped
[4773.38 → 4778.38] them become the person they are today and I think a lot of young ambitious people right now
[4778.38 → 4782.38] particularly because of things like the college application process I don't know how old your
[4782.38 → 4788.54] kids are but are you in that stage with them yet or no oldest is turning 15 soon I go 15 down
[4788.54 → 4794.72] to four so I go from 18 down to three yeah so okay you've experienced some of this son
[4794.72 → 4800.66] or maybe are currently experiencing sure I think for like a lot of young people who are very ambitious
[4800.66 → 4805.60] the path that they see to being successful which I think is reinforced through things like the college
[4805.60 → 4812.88] application process the way to succeed is to basically lie cheat exaggerate and steal and I think that
[4812.88 → 4819.30] you know our ambitious colleges are turning a generation of young ambitious people into like
[4819.30 → 4826.04] sociopaths and I think one thing yeah, and it's crazy I mean i I don't know how much you've dug into
[4826.04 → 4831.72] it, but it's like that when we saw the George Santos stuff happen we were like yeah like this is literally
[4831.72 → 4838.64] what like Stanford is asking for it's like crazy and i I think that we hope to you know hack club can
[4838.64 → 4843.72] help be part of a path where people kind of feel like they don't need to do that but can still be
[4843.72 → 4847.62] successful at those ages that that like values component is very important to our community
[4847.62 → 4854.80] well where does it go from here you seem to be off to a good start you got a base you got supporters
[4854.80 → 4861.66] you have a lot of programs there's excitement there's infrastructure there's you know the core
[4861.66 → 4867.62] is there and so what happens next or what are you trying to accomplish is it just get this into the
[4867.62 → 4875.06] wheelhouses of more people is it build and become bigger than the current offerings what's next
[4875.06 → 4882.18] yeah I mean so today you know if you're a young person, and you have that spark with technology
[4882.18 → 4887.96] there are very few things to support you in doing that, and we want to live in a world where right
[4887.96 → 4892.10] now there's about 15 million high school students in the U.S. I want to live in a world where about a
[4892.10 → 4896.48] million of them can kind of choose that hacker maker path to be the primary thing they're doing
[4896.48 → 4902.08] outside of class and I want hack club to meaningfully contribute to building an ecosystem where there's a
[4902.08 → 4905.72] bunch of different touchpoints that they're a part of that are supporting them on that path
[4905.72 → 4912.26] today like I would say when you look at all of our different programs there are probably about 25 000
[4912.26 → 4917.42] teenagers around the world who would say like yeah like hack club's like a meaningful part of what's
[4917.42 → 4923.12] going on for them like they would identify as that but like that's a tiny percentage and a tiny fraction
[4923.12 → 4927.20] of the number of people would love to be a part of hack club if they simply heard of it
[4927.20 → 4932.60] so the way I see it is like we need to grow a hack club to be something that every young person
[4932.60 → 4936.70] who wants to be who wants to be a part of it knows about it knows the right things about it
[4936.70 → 4941.50] and has the right folks to become a part of the community and I want to live in a world where you
[4941.50 → 4947.58] know like every high school has a group of teenagers where like this is our thing they're nice kind people
[4947.58 → 4954.94] with really positive values and where you know if you are someone who kind of you know wants to pursue
[4954.94 → 4958.82] this thing like there's a path for you, I felt like I had to drop out of high school and move hundreds
[4958.82 → 4964.48] of miles away from home to find my people and find that path for myself and I feel like I mostly got
[4964.48 → 4969.30] lucky in being able to find that and like this is something that change like coding is something that
[4969.30 → 4974.12] changes lives it shouldn't be something that's left to chance and like it's important that those of
[4974.12 → 4978.48] us who've been lucky enough to kind of be the beneficiaries of the current technology revolution
[4978.48 → 4983.48] that we give that gift to the next generation and make sure these they see that path for themselves too
[4983.48 → 4989.46] one more Silicon Valley reference I have to bring it up I'm sorry but does this act like an incubator
[4989.46 → 4995.00] in any way shape or form have you gotten to the point where you've got folks or young folks or
[4995.00 → 5000.72] teenagers or whatever label you apply to those I think you call them hack lovers that they get to a
[5000.72 → 5005.96] point where they're like you know what I'm I'm aging out and I'm going to create this thing, and they need
[5005.96 → 5013.38] not so much venture capital necessarily but maybe angels or pre-seed or early seed or like
[5013.38 → 5018.72] are you at a point where you actually are helping to assist in that next trajectory which is like
[5018.72 → 5022.84] hey I was I needed a place to belong when I was young I needed a place to learn I needed to make
[5022.84 → 5027.10] friends and I did all that and hack club served me well and now I'm at a point where I'm at a launch
[5027.10 → 5032.94] point and I was in the hack club for lack of better terms incubator like early Bachman's incubator
[5032.94 → 5037.78] and I'm ready to I'm ready to spread my wings and create my to app or my bro app or whatever it might
[5037.78 → 5043.72] be what's what's the scenario for you yeah, so today our oldest alumni are in their probably early 20s
[5043.72 → 5047.64] and it's been fascinating seeing what hack lovers do there's a number of hack club along who
[5047.64 → 5052.18] raise like millions of dollars for startups and are doing like really serious stuff and again like
[5052.18 → 5056.30] there's a handful of hack club along who have built open source projects that are now used by like
[5056.30 → 5061.56] millions and millions and millions of people I think that the primary purpose of hack club is and
[5061.56 → 5067.12] should it always be to help young people become the best versions of themselves once you turn 18 I think
[5067.12 → 5071.78] there's like a really great network of support and stuff like that afterwards and I think that if
[5071.78 → 5077.06] we're going to do you know I'm I think that like the one thing that will kill the org is focus so it's
[5077.06 → 5082.28] like let's pick one thing try to make it the most amazing beautiful incredible gift that you've ever
[5082.28 → 5088.64] experienced for people age you know 13 to 18 and then afterwards maybe we'll have some alumni support but
[5088.64 → 5093.64] I don't really want half club to be an incubator because the problem with being an incubator is that
[5093.64 → 5098.08] the people who are in power get to choose who gets opportunities and who don't
[5098.08 → 5102.04] and hack club only works because everyone is building the spaces that they themselves want
[5102.04 → 5106.12] if suddenly there's a dynamic where you like got more by being friends with staff or like doing
[5106.12 → 5110.62] certain things i I think it would make hack club feel a lot more competitive a lot less community
[5110.62 → 5115.26] driven and there's already so many spaces like that like go to Y Combinator Y Combinator is great and
[5115.26 → 5118.86] there are a bunch of hack lovers who go to what kind of Y Combinator like just do that like there's a ton of
[5118.86 → 5122.88] stuff like that already and I think that we would just end up doing a lower quality version of it
[5122.88 → 5127.70] I was thinking more on the naturalness of it less like the explicit like hey we are an incubator and
[5127.70 → 5135.76] more like just by nature of your mission you've got to incubate to some degree, and you know like a
[5135.76 → 5140.94] like a coding school or a boot camp like there may be on the other side of that they may partner up with
[5140.94 → 5145.48] opportunities for example I just wondered if that was because you've got connections like tom
[5145.48 → 5151.02] Preston Warner he is very into funding startups and other folks are into seed investing I know
[5151.02 → 5156.00] quin slack is an angel to several startups I'm sure, and you've got friends in that area would just make
[5156.00 → 5162.14] sense I would think to not so much implicitly you know say that okay since you're a hack clubber you
[5162.14 → 5168.98] get x opportunity but more like just by natural operation you're going to incubate some opportunity for
[5168.98 → 5172.82] somebody I just wonder if there was anything that you're doing around that front or just we're connecting
[5172.82 → 5178.72] those dots for folks yeah like nothing official at this stage because again like i I want
[5178.72 → 5184.00] the role of hack club to be to help you become the best version of yourself if we're like the
[5184.00 → 5188.42] thing is by pathos a human network right there are thousands of people involved inevitably like board
[5188.42 → 5192.74] members like tom get connected with certain with some hack clubbers and stuff like that but I'm not
[5192.74 → 5197.18] the one making the connections and his it's like actually like one of the key things you learn
[5197.18 → 5201.70] at hack club is how to send perfect cold emails if you're running a hackathon and that is a skill that
[5201.70 → 5206.24] really serves you later on oh yeah for sure um, and you know there's a really robust alumni network
[5206.24 → 5210.96] like there's a handful of hack clubbers who run like a series of group houses in San Francisco and
[5210.96 → 5216.26] stuff like that so it's like there's all like you know it's its a broad world and I think that
[5216.26 → 5220.22] i I want to have to be like the like I don't know something that feels a little wrong to me if
[5220.22 → 5224.50] about like staff going out of our way to connect certain people and not others I think it would change
[5224.50 → 5230.94] today, and it'd make it a little more transactional I think yeah i I appreciate the focus we have a
[5230.94 → 5236.32] saying right here keep the main thing the main thing and there's nothing worse in life than a
[5236.32 → 5240.82] focused person who's distracted because they're not focused anymore right I love the fact that you
[5240.82 → 5245.30] have that focus and that's good because I mean that gives you your north star right and anytime you
[5245.30 → 5250.10] like that's that's even for us one of our north stars around here is slow and steady now slow and
[5250.10 → 5254.04] steady doesn't necessarily mean that you're literally going slow because to go steady you have to go to
[5254.04 → 5260.30] pace that makes sense to keep the thing steady so slow is just a term to say as fast as it needs to be
[5260.30 → 5265.32] to remain steady, and we find ourselves you know not being steady anymore and going too fast we say
[5265.32 → 5269.04] slow down and check yourself so that's how we keep our focus around here to some degree
[5269.04 → 5274.66] and uh that's great that you have that response because you're focused thank you I'm glad we had
[5274.66 → 5279.44] you on to share more of the story I was curious myself want to dig into what you're doing we didn't
[5279.44 → 5283.96] talk too much about sprig and the PCB that was there, but we did enough I suppose is there anything
[5283.96 → 5288.92] else in closing you want to share anything else that's left unsaid go to GitHub.com
[5288.92 → 5294.90] slash hack club slash scrape go to GitHub.com slash hack club slash sign writer go to hack club.com
[5294.90 → 5298.24] and sign up for the email list for every three months you're going to email about a cool new
[5298.24 → 5303.92] open source project you know what we see is like there are so many young people who are hungry and
[5303.92 → 5307.80] sharing one of these things with the young person in their life could be the thing that you know
[5307.80 → 5312.86] helps them find their people helps them find their path and um you know helps them be part of a
[5312.86 → 5317.32] community that they might have been looking for a long time, and it takes a big tent you know and
[5317.32 → 5322.72] again I think might be the last thing is like if you're listening to this, and you wish you had
[5322.72 → 5327.58] something at hack club as a teenager give that gift to a teenager today, and you know a lot of our support
[5327.58 → 5332.08] well literally all of our all of hack club is made possible and free for teenagers through donors
[5332.08 → 5337.20] so you know give five dollars a month at hack club.com slash donate you'll really be helping make this
[5337.20 → 5341.52] possible for a new generation of young people too very cool yeah we'll link that up in the show notes
[5341.52 → 5347.70] definitely want to encourage donations as necessary yeah I can't imagine we have a large
[5347.70 → 5352.36] teenager audience but certainly want to encourage the ones who are here and those who are parents or
[5352.36 → 5358.04] loved ones of teenagers then please follow Zach's advice we'll link everything up in the show notes
[5358.04 → 5363.86] as you would expect so check that out Zach thanks so much for taking the time to come on we appreciate it
[5363.86 → 5368.88] thank you both again, and really thank you both for everything you do for open source I followed the
[5368.88 → 5373.58] changelog and would check it often as a teenager after you launched um you actually featured one of
[5373.58 → 5378.36] my projects I built when I was like 15 and that was like the most exciting thing ever is that right
[5378.36 → 5383.64] which one was yeah it was a git ignore tool it just it was a CLI tool that generate git ignores for
[5383.64 → 5389.00] you I think it was just like one of the go projects that I got a few stars that day another one was ssh
[5389.00 → 5395.04] iron I think you did it's like a's a little game that you can if you type ssh space ssh iron
[5395.04 → 5401.96] dot Zach Lotta z-a-c-h-l-a-t-t-a dot com in your terminal it drops into like a multiplayer iron
[5401.96 → 5407.54] game written go I think those are the two that you had on your site and um that was really
[5407.54 → 5411.94] that I think that was like one of the first times I'd ever seen my stuff on someone else's site so
[5411.94 → 5416.52] thank you both for the work you do and for supporting the ecosystem I would not be coding
[5416.52 → 5421.20] today if it wasn't for the open source movement and I know you two do a lot to help make that possible
[5421.20 → 5426.08] thank you for saying that I know what's getting featured in news next week jarred ssh iron
[5426.08 → 5432.10] we'll re-up that sucker we'll bring it back we'll bring it back it's a multiplayer iron in your
[5432.10 → 5436.22] terminal that's so cool it looks cool too sounds like something I would have covered at some point
[5436.22 → 5441.20] definitely give it another shout out next week on news why not right that's right well Zach thanks for
[5441.20 → 5445.02] being a follower all these years and man I appreciate you seeing that, and it's so cool to like
[5445.02 → 5449.88] we never really quantify our impact you know we never slow down enough we're always
[5449.88 → 5454.80] sort of champing at the bit for the next thing or the next urgent thing or the next right thing or
[5454.80 → 5461.66] whatever your next thing might be, and we don't often stop to not smell the roses but quantify our
[5461.66 → 5466.94] impact and I appreciate so much like having you on this show so many years later but also throughout
[5466.94 → 5474.16] your journey having you know some shape or form of impact to you and that's just honestly such a
[5474.16 → 5478.64] cool thing thank you for that well of course so you're the people who did the hard works thank you
[5478.64 → 5482.14] we'll have a wonderful rest of your days thank you so much thank you Zach
[5482.14 → 5490.68] okay seriously how cool is that how cool is it to be out here doing your thing for the better part of
[5490.68 → 5499.76] 15 years 14 years is how old will be the end of this year in November and during that time during all
[5499.76 → 5507.24] of this we impacted Zach Lotta and look what Zach did like isn't that just so humbling that you can put
[5507.24 → 5515.26] something out there show up consistently for 14 years and have impact I love it got the warm and
[5515.26 → 5519.28] fuzzier over here you know I'm saying I got the warm and fuzzier speaking of warm and fuzzier thank
[5519.28 → 5526.32] you so much to fast fly and also type sense for having our back and of course to break master
[5526.32 → 5532.86] cylinder those beats they're banging and of course to you hey jarred mentioned in news this week by the way
[5532.86 → 5539.00] did you check out changelog news, yet we've turned it into a podcast slash newsletter companion instead
[5539.00 → 5546.12] of changelog weekly going out on Sundays we now ship changelog news the podcast and changelog news the
[5546.12 → 5552.12] newsletter at the same time on Mondays if you're subscribed to this feed already well hey you get
[5552.12 → 5558.34] it already, but you may not get the newsletter so go to changelog.com slash news and get the newsletter
[5558.34 → 5564.58] you don't want to miss it okay that's it this show's done thank you again for tuning in we'll see you next week
[5564.58 → 5566.58] you
