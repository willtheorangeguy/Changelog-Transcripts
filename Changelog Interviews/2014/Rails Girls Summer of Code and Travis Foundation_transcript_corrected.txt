[0.00 → 15.08] welcome back everyone this is the changelog where a member supported blog podcast and weekly email
[15.08 → 20.06] coming with fresh and what's new in open source check out the blog at the changelog.com
[20.06 → 28.28] our past shows at five by five dot TV slash changelog, and you're listening to episode 122
[28.28 → 34.02] jarred and I talked to Anika lint our and flor does about rails grills summer of code and Travis
[34.02 → 40.98] foundation today's show is sponsored by ninefold code ship and top tau we'll tell you a bit more
[40.98 → 46.78] about code ship and top tau later in the show but our friends at ninefold they're doing some awesome
[46.78 → 52.94] stuff they're they're a high performance platform for deploying and hosting Ruby on Rails applications
[52.94 → 57.92] the platform is built on their own infrastructure with servers in the U.S. and Asia
[57.92 → 64.02] pacific and because they own their entire stack from hardware up they provide you with quantifiable
[64.02 → 70.98] superior performance compared to the competition with more economical scaling they make it extremely
[70.98 → 76.76] easy to deploy rails applications straight from a get repo by either using the online wizard or the
[76.76 → 85.80] infamous CLI command line interface they also offer great support zero downtime deployment SSL Regis teacake
[85.80 → 93.68] load balancers and firewalls for free straight out-of-the-box experience ninefold superior performance
[93.68 → 101.38] and easy deployment with a 30-day free trial just visit ninefold.com slash the changelog to sign up
[101.38 → 112.40] and now on to the show we're joined today by Annika linter and flor trees they are some awesome women in
[112.40 → 118.90] tech doing some cool stuff ruby um rails girl summer code Travis foundation and a ton of other cool stuff
[118.90 → 124.62] but I'll let them do their introductions for themselves Annika why don't you uh why don't you go
[124.62 → 129.98] first give the listeners an idea about who you are and kind of what you're what you're doing these days
[129.98 → 137.60] hi I'm Annika and um I live in Berlin and I studied something totally different I studied
[137.60 → 145.16] linguistic and gender studies and um I started whereas girls Berlin out of interest and because
[145.16 → 152.94] I fell in love with programming at a workshop and from there it was just an um a tiny step to where I'm
[152.94 → 159.70] now and now I'm working at Travis CI and I'm running the Travis foundation and with this I'm
[159.70 → 167.04] organizing where it goes more of code uh the second time now yes Travis CI is also I don't know if
[167.04 → 173.56] you know this uh Annika but Travis CI is a partner of the changelog so for those who are members you
[173.56 → 181.32] can go to the changelog.com slash benefits and redeem your awesome long story short so um flor how about
[181.32 → 186.76] yourself I know you're a long-time listener first-time caller um so to speak for the changelog so
[186.76 → 192.44] who are you and what are you up to yeah I think we tweet about every week right uh whenever
[192.44 → 198.64] I'm listening to the podcast again um so for me this is very exciting um so yeah hi uh my name
[198.64 → 204.84] is flor I live in Berlin right now um but at this very moment I'm in Vienna I used to live here for
[204.84 → 211.46] three years um I started programming about two years ago um going through the real scrolls guides by
[211.46 → 217.24] myself and uh and with my co-workers and that got me so excited that I wanted to get involved in the
[217.24 → 222.34] whole real scrolls community so I've organized about three of them in back in the Netherlands I am from
[222.34 → 229.04] the Netherlands um I'm organizing one in Austria next month and one in Azerbaijan of all places
[229.04 → 237.90] in October um yeah and last year a little bit late on I got um involved in real scrolls summer of code
[237.90 → 243.38] and that was such a great experience that I wanted to join as the as a part of the organizing team
[243.38 → 250.42] again this year, and it's been a blast so far you mentioned tweets and excitement and i have to
[250.42 → 254.88] give a shout-out to the tweet you did just before the show today, and we'll link to it in the show notes
[254.88 → 260.30] um if you go to the tweet, and it's not moving to go to click the actual link where it says go to
[260.30 → 265.28] imager because it's an animated GIF that was just rocking so I love that GIF by the way
[265.28 → 271.34] cool I'm glad you do um yeah you know Anika from your perspective though
[271.34 → 276.00] you'd mentioned that you went to school for linguistics and gender studies and I guess
[276.00 → 282.68] to some degree it's its really shaping where you're at now with rails girls summer of code and
[282.68 → 288.24] and what you're doing with uh Travis foundation and just in general I know that uh there's a lot
[288.24 → 294.56] of conversation around diversity and inclusivity and uh it's a big hot topic right now in tech and
[294.56 → 300.96] to some it's uh it's very real uh in terms of their life but can you give us an idea of maybe
[300.96 → 308.96] where I guess where the idea of rails girls summer code came from I know it's a campaign
[308.96 → 312.66] can you give us some of the backstory of what started this there was a blog post there was
[312.66 → 322.74] a dream give us the backstory um funnily enough I wasn't there when it started but i uh but I can
[322.74 → 331.08] can tell the story pretty uh good by now I guess so um this started with a meeting for um where
[331.08 → 338.00] organizers from rails girls Berlin and coaches met and here in Berlin we were one of the first
[338.00 → 343.72] group actually that after a beginners' workshop from rails girls that we said okay we wanted to
[343.72 → 351.62] continue coding together and to continue learning together so we organized follow-up workshops and we
[351.62 → 358.00] started these study groups, and we encouraged everyone to start their own study group just
[358.00 → 366.22] grab a coach and meet up every week or every second week and keep on learning and swan Fuchs
[366.22 → 373.04] is one of the most active coaches and one of the most active community members here and he
[373.04 → 381.28] started a study group I think two years ago and this is one of the best study groups and most
[381.28 → 387.76] awesome study groups I've ever seen it's called ruby monsters and um yeah, and they were just learning
[387.76 → 393.90] and I think they were just um missing a goal where to learn two words to there was
[393.90 → 401.78] yeah of course you can learn a lot about ruby I guess or like build your own um website and stuff but
[401.78 → 409.56] uh so they met and um and wanted to see what what can we build for women to get even deeper
[409.56 → 415.54] into code and they're the idea of a rails' girl summer of code was born and this is a little bit
[415.54 → 422.48] different from ruby and google summer of code as I understand it because it focuses on learning by
[422.48 → 429.56] doing so have that's the best way to learn right yes, yes it's its actually it's awesome and i of course i
[429.56 → 435.52] haven't done any other summer of code or even this one as a participant but as an organizer the
[435.52 → 442.26] idea is so great to have like have you work on a project and then actually get you deeper into code
[442.26 → 448.36] with uh while working on that project and while you work on that project, and you contribute to open
[448.36 → 454.88] source you are in these three months um you are a full-time programmer, and you can actually see if
[454.88 → 462.30] that's something you would want to get into so we give women the opportunity to kind of see um
[462.30 → 469.72] how this works and if they actually would want to work as a programmer and um to give them a chance to
[469.72 → 475.72] contribute to open source full-time so yeah that was the idea behind red custom of code and then I guess
[475.72 → 482.92] it was such a great idea that they started to work on this right now and when swan fun he gave a
[482.92 → 487.46] lightning talk at a beginners workshop and then a whole organizing team formed around him
[487.46 → 494.20] and they just got started and I think the whole um the whole idea was born in April or something
[494.20 → 502.86] and then they started the crowdfunding campaign last year and within two weeks I guess they had
[502.86 → 509.56] eighty thousand dollars, and they could support uh ten teams to come on board for its custom of code and
[509.56 → 516.22] this whole process wasn't longer than two to three months I guess so this was kind of like
[516.22 → 524.82] yes like a crazy idea crazy dream I was like okay let's just build it and that's that's the
[524.82 → 530.52] amazing story that's the kind of fairy tale kind of thing I like from that story and I actually joined
[530.52 → 537.68] in June uh when privacy I took me on board and i I got on board as a community manager and
[537.68 → 544.40] to organize or help organize for a customer of code with them so that was when I came
[544.40 → 550.00] you touched on one detail I think is kind of important for the listeners and I think it's important
[550.00 → 557.40] for a couple of reasons one is to show uh your perspective um you come to this, and you're an
[557.40 → 564.70] organizer of all of this as a non-developer um, but you said you know earlier in your intro that
[564.70 → 569.32] you fell in love with programming can you talk a little bit about what it is like um
[569.32 → 575.66] organizing and operating in the world where you're not you're not as fluent with some of the lingo or
[575.66 → 580.82] even the language itself um you know can you speak as a non-developer in the position you're in
[580.82 → 583.92] it's a lot of smiling and nodding
[583.92 → 591.84] yes I understand what you mean so um fake it till you make it though right yes I think that's true
[591.84 → 598.16] and you figure out that all the people around you don't know so much that you would think
[598.16 → 603.60] they know they have to google themselves and I'm always like that's my day-to-day right there
[603.60 → 609.04] honestly so that's like come on as when I have this problem or Constantine or whatever and and and
[609.04 → 615.28] and it says this and i I expect them to apparently know and to just know by this minute
[615.28 → 620.24] how they can help me or how they can solve this, and they're like yeah I really don't know so
[620.24 → 627.08] they're like the docs can you go to the docs please yes we all read the documents uh every day
[627.08 → 634.08] yeah totally so um yeah but that that's actually what struck me the most is like okay everybody's
[634.08 → 638.96] kind of no it's not fake it until you make it, but it's like investigate until you're like exactly
[638.96 → 644.24] yeah learn what it is and that's actually what I really love about programming is that you
[644.24 → 649.12] uh you see something and that you don't understand, and then you work on it until you
[649.12 → 655.68] get it fixed and then there's such a rush of excitement um for me every time that I got something right
[655.68 → 661.76] so um it's a constant journey right it's its it never changes that's what I love also about
[662.40 → 667.84] um I guess programming is one side of it but just like building for the web building software period
[667.84 → 675.28] whether it's design or development UX uh UI all the pieces of building software to me is pretty
[675.28 → 680.96] well because you never stop learning and jarred you can probably even jump in here on this because you
[680.96 → 687.20] teach um right now a rails class at interface there in Omaha Nebraska so that's kind of neat because you
[687.20 → 691.28] probably knew a lot when you went in, but you know a lot more now because you got to teach it right
[691.28 → 696.48] yeah and actually one of the things that I tell the students kind of day one is that uh you
[696.48 → 701.12] know one of the secrets of software development and building for the web is that there aren't any
[701.12 → 706.96] know-it-alls like they're even the experts aren't expert because there's a constantly changing
[706.96 → 713.68] environment and there are tons of nuance um evolving best practices, so a lot of the intimidation is just
[713.68 → 718.48] thinking everybody else knows way more and of course when you just get started they do know way
[718.48 → 724.72] more, but you see somebody who's a so-called expert and who can build for the web um, and they're looking
[724.72 → 729.92] at the docs, and they're googling answers, and they can't remember the know the exact syntax of the
[729.92 → 737.12] API and that's kind of an empowering thought um seeing somebody who is um been in the business still
[737.12 → 741.60] having to do things that you're having to do as a beginner, and we're all we all kind of live there
[742.24 → 748.32] yeah flor what's your perspective on I guess you'd mentioned that you're about two years
[748.32 → 753.60] into being a developer is that right yeah that's about right yeah so what is your have you gone
[753.60 → 758.72] through were you one of the participants of the first uh rails girls summer code or what is
[759.52 → 765.20] you know what's your angle to this um no actually I wasn't a participant I was helping out um
[765.20 → 770.32] Annika mainly with some PR and communication stuff um I think one of the reasons that I could actually do
[770.32 → 774.80] that is when I started learning programming I thought it was very important to listen to
[774.80 → 781.68] you know all kinds of podcasts like yours or um like the like ruby rogues for instance
[782.32 → 788.24] and while listening to such podcasts I would pause every time that I didn't understand what they
[788.24 → 793.44] were talking about or I didn't understand the term um and I would look it up and get familiar with this
[793.44 → 798.64] term and I noticed that after a few months you know I have to pause a lot less than I used to do before
[798.64 → 804.80] because you just learn along the way um I've done some talks on learning programming and how you
[804.80 → 810.32] can teach programming in a better way um and this is definitely one of them have them listen to
[810.32 → 817.04] as much as they can get their hands on possibly and have them figure out you know that it's partly
[817.04 → 824.80] talk to talk, but it's but with while talking the talk you learn a lot yeah I feel like the sooner you
[824.80 → 828.72] can just kind of jump in and get your hands dirty so to speak and I think that's what the beauty might be
[829.44 → 835.20] for uh the summer of code is that, and maybe you can correct me if I'm wrong, but it seemed like it
[835.20 → 842.72] it seems like it's pretty focused on um obviously women but um open to everyone not just
[842.72 → 848.72] women, but you know as you said before Annika it's the lens is focused on women but open to all but
[848.72 → 854.80] um mostly on those that are coming in fresh coming in new probably even coming with some inhibitions
[854.80 → 861.52] about you know can I do it is it possible you know all these other intimidations I think you know
[861.52 → 867.68] the deep unknown kind of gives us but um would you say that rails girls summer code is mainly focused at
[868.56 → 875.52] beginners or intermediate what level are you really is the aim um well as a beginner it's
[875.52 → 881.84] probably a little bit too hard uh to actually contribute to an existing open source project
[881.84 → 889.36] or to actually kick off your own so we recommend that you've been learning around like six months at
[889.36 → 896.48] the least programming so like um for example if you have joined the right first beginner workshop and then
[896.48 → 904.32] just like started your study group and met um every week or whatever and just kept on learning
[904.32 → 910.72] because that's that's a little bit that's like the important thing that you never let go and that
[910.72 → 916.32] you are a little bit familiar with the structures of whatever language you want to program in let's
[916.32 → 924.48] say it's probably ruby so that you are familiar with um with the basic things and maybe already know how
[924.48 → 931.76] to use git and stuff so yeah so that's probably the basic uh level we're looking at of course
[931.76 → 940.56] uh we're happy to make exceptions if there are some other criteria that are met and yeah then it
[940.56 → 948.96] goes up for the level I think we have this year some computer science students um who have been studying
[948.96 → 956.88] computer science for some time but haven't been able to get into open source or um yeah it actually means
[956.88 → 963.28] different things like studying computer science doesn't mean you're actually programming because
[963.28 → 970.48] it looks so different um from I don't know country to country or even from city to university
[970.96 → 977.44] what you're actually learning in your university and for uh one story i like very much is
[977.44 → 984.08] about that woman who said yeah okay I study computer science but um only since rails girls I really have
[984.08 → 992.48] fun at it and I understand it and I am I dare to ask questions and um yeah so um we have a lot of
[992.48 → 999.68] levels uh that that people can jump in and raise course of course but yeah probably a total beginner will have
[999.68 → 1007.84] probably a hard time doing three months full-time coding so some uh I guess community involvement
[1007.84 → 1014.72] either watching doing uh observing something will definitely help let's let's maybe um
[1016.16 → 1021.76] I want to mention this too just for those who maybe come into this conversation uh maybe behind the
[1021.76 → 1029.68] curve a little bit so you've got rails girls which is a meet and I'm just uh going based on the
[1029.68 → 1036.56] the details here on the page, but it's its uh worldwide meetups in your local cities that are
[1036.56 → 1045.12] focused on helping women learn Ruby on Rails um educational meetups events all that but
[1045.12 → 1051.20] on top of that you have rails girl summer co which is this summer thing that essentially I think
[1051.20 → 1054.96] last year it might have been a little different but this year you've got 20 students coming in
[1054.96 → 1061.44] totally focusing on open source and essentially spending three months living and breathing ruby on
[1061.44 → 1065.52] rails in open source is that about sum up what summer code is all about
[1065.52 → 1076.88] um I think it's not um if somebody wants to uh program in java or uh PHP that that that depends on
[1076.88 → 1083.44] the project um but uh I'm not sure I think this year we'll probably have a lot of Ruby on Rails
[1083.92 → 1089.76] projects as well but yeah that's uh that's pretty much what vice customer of code is about so just from
[1089.76 → 1094.16] the name I assumed it would be like people trying to contribute back to the know Ruby on Rails
[1094.16 → 1098.40] framework but it sounds like it's just any open source that you want to that you want to do you
[1098.40 → 1104.48] pitch it uh do you have to have a specific goal in mind how do you actually do the whole three-month
[1104.48 → 1114.96] process um as a student yeah as a student okay uh well you have to apply and we have some we ask a lot of
[1114.96 → 1123.44] mentors or people who have open source projects okay um to collect these ideas and proposals in a
[1123.44 → 1131.92] in a repository and so to give the students an idea of what they can contribute to and a lot of students
[1131.92 → 1138.16] have um own ideas of what they want to build and of course it depends on their skill level if
[1138.16 → 1144.00] they uh if they can is they're able to do this and if they have the support of coaches and mentors
[1144.00 → 1150.48] to actually pull this off but um yeah so one story would be you look at the repository then you find
[1150.48 → 1157.28] oh wow bundler sounds nice I want to contribute to that, and then you get in touch with a mentor
[1157.28 → 1162.48] who proposed this, and he will help you, or she will help you very good Annika
[1162.48 → 1168.24] figure out a project floor keeping it straight
[1171.52 → 1178.32] yeah you learn something while talking about it so um yes so you would actually then um
[1179.28 → 1185.44] work out the project plan what your goals would be um in these three months and since you have to apply
[1186.08 → 1190.72] two months before the program starts or even two and a half months for some project that means that
[1190.72 → 1197.12] they actually changed a lot for some newer projects or something so sometimes you can't predict anything
[1197.12 → 1202.72] but uh to give just a structure on what your plans would be and what your goals, and it's really
[1202.72 → 1208.24] essential that you work together with a mentor who's actually running this project because um they know
[1208.24 → 1216.32] this uh and can actually see what is needed what would be a contribution to the community what would be the
[1216.32 → 1223.44] the best thing to work on so rails girls is a global movement, but it's all local workshops and meetups
[1223.44 → 1230.16] um is rails girls summer of code completely online or is there a locality to it to fly off to a far
[1230.16 → 1237.28] away location and code or are you just involved online that'd be cool um that would be really cool I just had
[1237.28 → 1246.08] the image of Iceland in my yeah no um it's international uh, so anybody can apply actually
[1246.08 → 1252.00] uh a lot of organizers are Berlin located so that was where the confusion last year came from if it
[1252.00 → 1258.08] was a Berlin program or whatever, but we had students and teams from all over the world last year and this
[1258.08 → 1266.64] year so we're just asking that you find local support wherever you are as much as you can because
[1266.64 → 1276.48] um like being a newcomer to open source and working remotely with uh with coaches or pairs might be a
[1276.48 → 1283.44] harsh situation so uh we found it's its best if you have a strong local support like with the
[1283.44 → 1288.64] companies for example like we have this year we have companies that said yeah sure you can work here and
[1288.64 → 1295.36] we actually have some coaches you can ping all the time and that's nice and that's that's super cool and
[1295.36 → 1302.48] that uh that worked last year really well with SoundCloud and this year we have uh for example six wonder
[1302.48 → 1309.84] kinder six wonder can I don't know how to say it in English the people that make Wunderlist
[1311.20 → 1320.40] exactly thank you uh for example or rebased in Poland or um yeah some other amazing companies
[1320.40 → 1328.32] that help the students um have a local structure I think last year I'm sorry go ahead
[1328.32 → 1332.72] floor I think last year and this year we had the same sort of confusion that there were some people
[1332.72 → 1338.32] from Australia that would love to join, but we're confused by the name because for them, it's not summer
[1339.68 → 1345.44] yes oh, and it's its not only Australia right there's some other continent where they said yeah it's
[1345.44 → 1350.40] pretty cold right here I don't think I'll ask I ever get summer just uh speaking for an U.S. state
[1350.40 → 1355.20] that's not actually in the continental U.S. right I don't think it's ever summer there and when it is
[1355.20 → 1362.48] it's still winter so there you go let's pause the show for just a minute give a shout-out to our
[1362.48 → 1368.96] sponsors code ship is a hosted continuous deployment service that just works you can easily
[1368.96 → 1374.24] set up continuous integration for your app in just a few minutes and automatically deploy when all your
[1374.24 → 1380.72] tests pass code ship has great support for lots of languages test frameworks as well as notification
[1380.72 → 1386.08] services, and they easily integrate with GitHub Bitbucket and can deploy to cloud services like
[1386.08 → 1392.56] ROK AWS notice google app engine or even your own servers you can get started today with their free
[1392.56 → 1399.28] plan it takes just three minutes head to code ship.io and one more thing to mention for our members
[1399.28 → 1407.60] our awesome members by the way you can save between 284 and 2994 on your first year with code ship so
[1408.00 → 1414.08] make sure you take advantage of that head to the changelog.com benefits to learn more and redeem
[1414.08 → 1419.44] that benefit if you're not a member don't worry it's just 20 bucks a year, and you can support us to
[1419.44 → 1425.76] support open source, and we certainly appreciate that for sure once again go to code ship.io
[1427.92 → 1435.60] um i I am noticing though a short while back I'm still kind of keeping up with some recent events but
[1435.60 → 1442.24] just a few days ago you, you mentioned on the rails' girl summer code blog that there you're announced the
[1442.24 → 1450.24] the first seven teams uh you mentioned projects like diaspora pairing and several other
[1450.24 → 1456.64] kind of neat uh ruby rails based projects uh several coaches that are prominent and open source and have
[1456.64 → 1462.08] kind of been there and kind of help pave the way um Kerry miller's a name I'm seeing just quickly in the
[1462.08 → 1470.64] list uh Eric Michaels over previous uh on the changelog um and a couple others but I try to link
[1470.64 → 1476.40] over to the apply page just kind of just to kind of get an example of what you were asking about
[1476.88 → 1482.88] and I think just to maybe separate some of the confusion it sounds like it's a team um so you
[1482.88 → 1488.08] kind of have to do some self-organizing prior to applying and maybe a little bit of research on which
[1488.08 → 1493.60] project and also making a note for listeners if you're going to the link uh applications are closed
[1493.60 → 1498.88] right now so it seems like um we're a little too close to the finish line to talk about applying
[1498.88 → 1504.64] this year but next year obviously hopefully things come back but what are the I guess all that to say
[1504.64 → 1510.24] well you know what are the details around um making up your team applying what are some of the
[1510.24 → 1515.60] questions that were asked when applying that you kind of look at as criteria was the project selected
[1515.60 → 1521.04] was it the people you know what was it that got you know that made you a team and got you through
[1521.04 → 1529.92] the application process oh that is super different category but I think the basic one is that um you
[1529.92 → 1538.16] have to have a pair so we figured that um the two is the best number on this so you can actually pair
[1538.16 → 1549.36] program and keep each other motivated um and um yeah you have to have a pair and and and and a coach
[1549.36 → 1558.16] that actually or who can actually help you um some hours a day um in the beginning and in the end
[1558.16 → 1565.28] that depends sure you will get a lot more done by yourself, but that's pretty important that you have
[1566.48 → 1573.20] one or more coaches I think one team had six or something that actually depends on if you're at the
[1573.20 → 1582.08] at a company that said yeah sure you have you can have all coaches 24 7 um yeah but what was
[1582.08 → 1586.80] your question the questions I'm thinking of like I'm thinking like the application process and now
[1587.44 → 1593.52] just hearing some of those details you mentioned now I'm thinking about you know it's three months long
[1594.08 → 1599.76] um you know Jerry's question asked about whether it was local or kind of worldwide which is worldwide and
[1599.76 → 1605.84] there's no real location for it so and even some of it will take place you know just you know primarily
[1605.84 → 1612.16] online for a lot of people uh getting involved so now I'm thinking of like what happens when I'm like
[1612.16 → 1617.20] lost I'm in the woods you know what kind of support structures do you have in place uh you know maybe
[1617.20 → 1623.36] what did you learn from last year that's changed for this year to make um completion and making
[1623.36 → 1629.60] being part of a team easier and just not getting lost do you want me to answer that one yeah yes
[1630.48 → 1637.20] I thought so um so like first they all have a mentor for their project right and then there is
[1637.20 → 1644.64] one or more coaches that will help them out that were already predefined um and then so last year we had
[1644.64 → 1651.84] a remote help desk um in IRC where everyone could just log in and help people out if they wanted to do
[1651.84 → 1657.04] yeah that's that's pretty neat uh this year we'll go with campfire to make it a little bit easier for
[1657.04 → 1662.64] the students because we noticed last year at IRC it has a quite steep learning curve apparently for
[1662.64 → 1668.80] for people just starting out um, and we'll be partnering up with a few companies that I cannot
[1668.80 → 1677.28] name yet, but we will really quickly uh that will um that will help us amend the help desk um for a
[1677.28 → 1682.72] longer period of time because we know there's the different time zones and sometimes there were
[1682.72 → 1688.32] no not enough people online to help, help students out when they had a problem so we'll try and have
[1688.88 → 1693.92] have three coaches in there at all times so that you know people are actually you can actually go
[1693.92 → 1699.36] there with all of their questions I think that's very important, and we're determined to make this
[1699.36 → 1709.20] better this year yeah and um if you're lost not in a programming kind of way or learning way um but
[1709.20 → 1718.88] have problems with your I don't know family or teammate or get bullied from a coach or a member any problem
[1718.88 → 1725.84] you might have we have I'm I'm really glad I'm really happy that we are um having this year we have a trust
[1725.84 → 1733.76] committee and that's actually consisting of members that are um involved in the organization I think
[1733.76 → 1740.48] it's Ven and me that you can turn to with all your problems, and we have I think three or four
[1740.48 → 1746.96] external people four yes um that are not involved in the organization so that they can stay impartial
[1746.96 → 1753.60] and then can mediate between the students or the coaches or whoever turns to them with their problems
[1753.60 → 1760.08] and the organization so they can help you figure out any kind of problems you might have and um
[1760.96 → 1768.56] yeah so that we can make sure everybody feels comfortable and not I don't know we want to
[1769.52 → 1776.08] we want to have a safe space, and we'll work uh towards that and I think with the trust committee that's a big
[1776.08 → 1784.32] step to make or to help people feel as comfortable as they might feel in such a program yeah I guess
[1784.32 → 1788.08] you're right because I mean you can get lost on a couple different levels one you can lose just
[1788.08 → 1796.16] motivation maybe you're in the fringes either self-inflicted or you know you mentioned the trust
[1796.16 → 1801.76] part of it where you might be getting bullied or um you know harassed who knows what could
[1801.76 → 1807.04] potentially happen, but then you could also be on a learning curve a little lost and needing some of
[1807.04 → 1812.32] the guidance and obviously having a strong team with strong leaders is going to be you know helpful
[1812.32 → 1817.28] helpful to that so that's that's neat to have that in place especially the real-time communication too
[1817.28 → 1822.56] around like campfire or RC last year because I was just thinking like man when you get in the middle
[1822.56 → 1831.28] of this I know how I sometimes feel with projects um I tend to be an island um just self-induced
[1831.28 → 1838.24] anyway and so when I get lost the only person I really have to cling to is jarred and Andrew
[1838.24 → 1844.40] obviously but um you know a little closer to the heart is my wife so you know I've kind of got my own
[1844.40 → 1849.84] personal support structure that i kind of leverage and cling to so I just wondered what um
[1849.84 → 1856.64] you all are doing for this during that that three months but um another topic I think
[1856.64 → 1864.32] is important to talk about is um I guess the crowdfunding was done you all do crowdfund last
[1864.32 → 1872.32] year too or is this a new thing this year and can you kind of speak to um you know having not only
[1872.32 → 1878.56] corporate sponsors but um I guess those who contribute and those who are part of the community giving
[1878.56 → 1885.36] their own personal dollars to support the cause and essentially um fundraise to pay for
[1886.88 → 1890.24] um I guess what do you what do you call that what's the what's the word for that
[1890.88 → 1895.12] the scholarships yeah I was looking the word gap me for a second but scholarships so I mean you got 19
[1895.12 → 1899.20] scholarships eighty thousand dollars raised right now what's what's the background here on this
[1900.24 → 1905.84] yeah so last year it was a crowdfunding campaign as well so um yeah this was always uh
[1905.84 → 1912.56] achieved by the um achieved by the community, and we have of course some strong leaders uh as companies
[1912.56 → 1921.92] who are giving a lot of money uh like GitHub or google open source or um yeah floor was very heavily
[1921.92 → 1929.52] involved uh with this year so you probably can name some other wonderful companies but uh also of
[1929.52 → 1935.60] course individual donors and this year we even have like an app where you can notch your
[1935.60 → 1941.76] not your family and friends to give more money which is pretty awesome but yeah maybe Flo you can
[1942.32 → 1950.16] tell a bit about that yeah I think what's very exciting is the crowdfunding uh part about it if I speak for
[1950.16 → 1957.44] myself for instance so um i I gave of course I gave some money and I gave some money as well last year
[1957.44 → 1963.12] and for me my motivation is really that when I just entered the ruby world everyone was so
[1963.76 → 1971.12] so nice and so welcoming and everyone wanted to help me um and I found the rails girls guide so helpful
[1971.12 → 1977.12] and uh and the event so helpful that i just really wanted to give back and what we hear from a lot of
[1977.12 → 1982.56] people backing this project is that they similarly also want to give back to the community
[1982.56 → 1991.68] um I think that's what drives the crowdfunding campaign so well and go ahead yeah and the
[1991.68 → 1997.12] connection like last year since then folks was so heavily involved here like all the people that
[1997.12 → 2001.92] loved Travis CI and the work that they did and the involvement they had in the community
[2001.92 → 2011.92] actually um he nudged them all I guess like pulling all-nighters and um and got a lot of awesome
[2011.92 → 2017.44] feedback and that's how it worked last year and this year we have a lot of people that are of course
[2017.44 → 2022.32] saying oh yeah I did it last year I want to do it this year again because this is such a great cause
[2022.32 → 2027.76] and this is where I'm always so in awe and think wow this is such a great community
[2027.76 → 2034.48] so I was going to ask it looks like just tons of support looking just at the sponsorship page
[2034.48 → 2039.84] and how much money has been able to raise is really awesome how much does it cost to send a team through
[2039.84 → 2045.44] or a student um what does the student get for the three months and then I'm curious follow-up
[2045.44 → 2049.36] question curious if cost of living and this kind of things are factored into that at all
[2049.36 → 2061.28] that's a perfect question so we uh calculate uh five thousand us dollars per student okay and
[2061.28 → 2070.80] that's with some buffer um for the um the courses the dollar might uh have or the euro or wherever you
[2070.80 → 2078.48] are that you're getting the money so um that's important and um yeah, and we actually are asking the
[2078.48 → 2085.60] students to calculate the cost themselves and we ask them what they can live off we say okay we
[2085.60 → 2094.08] we can pay you 1.5 thousand us dollars a month not a thousand you can live off oh yeah you're right
[2094.08 → 2102.72] sorry um mathematics she was right I got our calculators out yeah I'm getting my calculator out right now
[2102.72 → 2112.80] okay no and uh yeah, and so we say okay 1.5 is yours if you want it but if you, but we didn't
[2112.80 → 2119.60] do any calculation for any kind of uh country or living costs because I think that depends
[2120.24 → 2125.84] hugely on what your private or like your situation looks if you're a single mom or if you're like
[2125.84 → 2132.32] heavily supported by a family that can actually differ a lot so we ask students themselves to tell us how
[2132.32 → 2139.36] much money they need and then we um we can this is new this year so we can actually if they say okay
[2139.36 → 2145.28] here you can have 100 or 200 euros back we can um give that back to the race goes on of code
[2145.92 → 2151.60] crowdfunding campaign and maybe be able to fund another team spot because we are now short of two
[2151.60 → 2159.52] team spots, and we can use any money so yeah so you're trying to get together as a 20 it's 20 students and
[2159.52 → 2166.32] that would be 10 teams, and you're sitting on eight right yes you have eight you're looking for
[2166.32 → 2171.52] funding for two more um so everybody donate sponsorship is it just donate go to the
[2171.52 → 2177.28] website right is there any harder than that no maybe you should repeat if it's just that easy give us
[2177.28 → 2181.60] money sure what's the website again
[2183.36 → 2189.44] real customer of code.org slash campaign yes if you want to, or you can go to
[2189.44 → 2192.56] real customer of code.org and click on the donate now but
[2195.12 → 2200.88] 80 000 total has been raised so far as jarred kind of recapping what jarred said you got eight teams
[2200.88 → 2206.64] funded currently you got two more teams waiting to get fully funded that's I'm guessing you know
[2206.64 → 2213.84] ten thousand dollars more for going on the average of five thousand um, um five thousand per team so i
[2213.84 → 2222.56] mean this is a success was it so you mentioned last year was um you also crowdfunded last year as well
[2222.56 → 2229.36] did you have a similar outcome or was it less or better was it how does it fare I guess in comparison
[2229.36 → 2240.56] last year was faster I think last year was faster yes but was it less or more money
[2241.84 → 2248.56] yeah it was just faster that the companies uh jumped on board I think maybe this year the companies i
[2248.56 → 2253.52] don't know have some kind of for some companies we came too late they said okay they had to like
[2253.52 → 2258.96] calculate their budget uh already and stuff I don't know how this worked last year maybe there was
[2258.96 → 2268.72] smaller and didn't do the calculation uh part but uh um yeah I don't know, but we have some
[2268.72 → 2274.88] companies lining up I guess that we're still waiting to hear from and um these are the infamous
[2274.88 → 2281.12] ones that uh forehead just mentioned that you can't mention but can kind of mention uh no I think
[2281.12 → 2287.04] she was thinking about the companies that are involved with helping us support okay sorry
[2287.04 → 2291.12] not that I can like hint that they're already a sponsor so
[2292.64 → 2298.64] oh that doesn't come on a teaser campaign
[2302.00 → 2305.92] let's pause the show for just a minute give a shout-out to our sponsor top towel uh you've
[2305.92 → 2309.92] probably heard me mention top towel several times over the last couple of months if you've been a long
[2309.92 → 2314.56] time listener of the show, but we've been working with top towel for quite a while now, and we thought it
[2314.56 → 2319.44] would make some sense to circle back and talk to some of the listeners who've applied to top towel
[2319.44 → 2324.72] and have actually been accepted because only two to three percent of the engineers who apply
[2324.72 → 2332.48] make it past their strict elite engineer process and one of them is an awesome fan an awesome listener
[2332.48 → 2338.40] Daniel Luzon he is in Ottawa Canada a long time fan a long time listen to the changelog, and he's
[2338.40 → 2344.72] now living the dream as an elite engineer at top town I say living the dream because he's now able to
[2344.72 → 2351.44] have 100 control of the types of projects and the technologies he's working on even as well as the
[2351.44 → 2357.28] rate he wants to charge Daniel earns 100 of his income as a top towel engineer, and he wanted me to
[2357.28 → 2363.60] pass on his seal of approval so to speak of the top towel experience and for those of you out there
[2363.60 → 2370.48] who are freelancing right now, or you would like to test out freelancing or even try out a kind of
[2370.48 → 2375.92] no risk freelance like project where you maintain your full-time position you have to check out top
[2375.92 → 2382.08] towel if you think you have what it takes head to top towel.com slash developers to get started and
[2382.08 → 2388.32] tell them the changelog sent you floor you mentioned that you're a long-time listener and on come I'm sure
[2388.32 → 2395.20] that you're becoming a long-time listener but um do either of you by any chance follow um some of the
[2395.20 → 2400.24] some of the content that um Beverly nelson has been putting up on the changelog around learning she's got
[2400.24 → 2408.48] an um a real passion she does a lot of stuff with rails bridge um I think she just ran a course at
[2408.48 → 2415.76] ancient city ruby really, really deep uh passion for teaching Ruby on Rails, and she's got such a heart for
[2415.76 → 2424.80] the beginner level i just totally am impressed and in awe of her patience for it but uh have
[2424.80 → 2429.36] either of you caught up with any of her recent posts I think one of the most recent ones that was
[2429.36 → 2437.60] really a good post um was uh regular expressions without fear and she kind of gives this dissection of
[2438.72 → 2445.60] different resources' regex for fun, and you know some common kind of early problems to solve around
[2445.60 → 2449.68] it but I guess it's kind of a long question to ask you have you caught up with any of the
[2449.68 → 2453.52] the learning content on the channel we try to keep this more regular like once a week so I'm just
[2453.52 → 2461.44] curious yeah everything lands into my reader so I read everything did you tweet about it that's the
[2461.44 → 2467.20] that's the question that's a good question I might have I have actually a call to action for it
[2467.20 → 2473.68] that's not a question I see did you tweet about it, I will I guess
[2476.80 → 2482.08] I feel such pressure there is a lot of pressure there's a lot of pressure
[2483.60 → 2489.68] animated GIF so now you just have to keep producing GIFs of that quality all day every day in it is should
[2489.68 → 2496.40] be okay gosh I've never seen that one either, and it's its uh I was when I saw it I was like that's
[2496.40 → 2504.72] super awesome I love that um I guess I'm not sure if there's um any additional topics that we can bind
[2504.72 → 2511.76] of cover around summer code if there's anything we left out um uh let us know if not I want to talk a
[2511.76 → 2518.16] bit about Travis foundation and just in general the mission around supporting and propping up open
[2518.16 → 2522.64] source obviously that's been our focus here at the changelog for several years now so
[2523.60 → 2527.36] kind of close to our heart but is there anything else we need to cover that we haven't covered on
[2528.32 → 2533.04] summer code that we need to I don't know did you say that everyone can donate now
[2534.32 → 2538.08] everyone can donate we haven't mentioned it everyone can donate
[2539.44 → 2544.88] okay if you're listening to this go to railsgirlssummerofcode.org slash campaign
[2544.88 → 2550.80] uh I think you're suggesting a 75 donation but I think it's you can donate whatever you want
[2550.80 → 2558.80] like 20 bucks you can totally do more do awesome do the exact amount um you can totally do
[2558.80 → 2565.52] more if we don't have any hard feelings about that it's no problem whatsoever and if you're uh you know
[2565.52 → 2570.16] if you're a company listening to this you know if you're a developer working in a company that can
[2570.16 → 2576.00] be a sponsor you know take this to either yourself if you're a decision maker or your boss or your
[2576.00 → 2580.96] team leader or whomever, and you know get some support there's lots of great support here for
[2581.92 → 2588.56] uh rails go summer code and I know um the changelog we we gave a little bit of money as well
[2588.56 → 2592.16] because man we love you guys so yay for the changelog yay
[2592.16 → 2601.52] uh so yes if you didn't get that go and donate right now please and now on to
[2601.52 → 2607.12] Travis foundation so I know I mentioned earlier that uh I've been working with Matías uh for a
[2607.12 → 2612.80] while now Travis CI is a part with the changelog that means that they know they work with us to
[2612.80 → 2617.68] to just make sure that our member base we have a member base that supports the changelog as well
[2617.68 → 2622.16] and so if you're not a member you can become a member now by going to the changelog.com slash
[2622.64 → 2628.56] membership, and it's just 20 bucks a year and with that you support us to support open source in
[2628.56 → 2635.44] addition to that we um we work with uh corporate partners like Travis CI to basically give a
[2635.44 → 2640.64] nice discount to our paid members um for their services and as part of that I've been working with
[2640.64 → 2648.48] Matías for a bit and have wanted to have um you all on the show to talk about Travis foundation and i
[2648.48 → 2654.48] didn't even know until inviting Annika to come on the show to talk about rails girls summer code that
[2654.48 → 2660.16] she runs Travis foundation so that's that's kind of neat, but it's an initiative run by Travis CI because
[2660.16 → 2666.24] they care about open source but uh you know I think one of your current things you're doing now
[2666.24 → 2671.52] is rails girls summer code, but you've got other things in the pipe to work on so kind of give us an
[2671.52 → 2677.12] overview of what Travis foundation is and then maybe what some of the mission is yeah I think Travis
[2677.12 → 2684.80] foundation is a way for the Travis CI team to give something back to the community because they have been
[2684.80 → 2693.12] um been born out of the open source uh community they've they've run a crowdfunding campaign as well
[2693.12 → 2700.16] and were able to build Travis CI with this, so this is their way of actually saying thank you and
[2700.16 → 2707.12] contributing back so I think the tagline speaks for itself it's like making open source
[2707.12 → 2717.20] or even better and um that's like a broad thing or like a super huge goal to have but basically we
[2717.20 → 2726.08] want to support projects that we think are of value to the community and for this we started with open
[2726.08 → 2734.56] source grants where we support people working on awesome open source projects that are with which
[2734.56 → 2745.60] depends on or um or grants as we call it like we did uh RVM um and organized uh the grant uh for them
[2745.60 → 2753.60] which was paid by pay mill and now like simultaneously to some code we are doing coco pots uh we're
[2753.60 → 2760.72] supporting them and the company behind this is SoundCloud who are paying the grant for uh for
[2760.72 → 2768.72] coco pots, and we are like the connector in this so we actually um we're looking at projects or people
[2768.72 → 2774.88] writing us emails and saying hey I have this and that project I'm working on it and i I can't do it
[2776.56 → 2781.92] just in my free time anymore i would love to do this full-time but I need some money for this
[2781.92 → 2789.52] so we look at the project and then um select the ones that we think are really cool and would
[2789.52 → 2794.00] be of great value to the community, and then we look for a company that actually fits
[2794.96 → 2799.68] with this project, and then we pair them up and organize the whole thing, so this is one
[2800.40 → 2806.16] one thing we do with these open source grants then of course the rest got some off code we organized it
[2806.16 → 2815.68] last year and our main organizer this year again and um that actually takes a lot of my time so
[2815.68 → 2827.28] um yeah everything else is um no i I can totally handle everything else and um yeah and then the
[2828.16 → 2837.20] uh we want to foster diversity and open source as well and for that we are um already um working
[2837.20 → 2844.00] together with some conferences and planning on doing this more like to for example get more women on stage
[2844.00 → 2851.12] or make this more make the conference more family friendly or how to reach out to a more diverse
[2851.12 → 2857.60] audience or something like questions that you mentioned earlier are kind of um getting more and
[2857.60 → 2865.04] more important in the scene, and we want to help people work uh work towards that, and they can actually
[2865.04 → 2871.92] approach us and ask us hey I want to do this and that and I don't I don't know how to do this or
[2871.92 → 2877.44] um should we have a code of Conrad or what is a code of Conrad or something like this and there are
[2878.00 → 2886.08] already some great resources out there um like actually Ashley Dryden does a lot of things that I admire
[2886.08 → 2893.76] and she put together some awesome stuff, and we have other women putting up tutorials like how to give a talk and stuff or how to
[2893.76 → 2904.24] uh not be anxious to enter right community where your minority so um yeah that's that's kind of what we
[2904.24 → 2913.68] aim for, and we're still of course it's really, really young I think uh we launched the foundation end of last year
[2913.68 → 2925.04] um we are open to other um yeah ideas or projects we should uh we should support or work together with so
[2925.84 → 2932.64] well I think the grants part is a unique thing and obviously um a specific approach um with
[2932.64 → 2939.12] diversity in tech I think it's an audacious goal anyway to foster diversity but uh in addition to that you got
[2939.12 → 2944.96] friends of the show RVM Michael Paris runs that project now Wayne Seguin was once on the show
[2945.68 → 2951.84] back in the day um when he had I guess not really first started it but earlier in the RVM
[2951.84 → 2958.56] history so you mentioned open source grants I guess the question I have around that is um is it seems
[2958.56 → 2963.28] like there's some sort of application process I think you mentioned SoundCloud in there somewhere and
[2963.28 → 2968.24] you mentioned a project that they are working on its open source can you talk about you know maybe
[2968.24 → 2976.64] you know Travis foundations um I guess the focus on obviously giving out grants, but you know when
[2976.64 → 2982.80] does it happen is it kind of organized how do you go about it is it just like get in touch and
[2982.80 → 2986.72] let us know your woes, and we'll see if we can give you some money what's how does that work
[2986.72 → 2999.36] yeah I would love to say here's the apply button but uh now there's actually no um application process
[2999.36 → 3006.64] you have to go through or some criteria you have to met I think we discuss every project as it
[3006.64 → 3012.80] comes in or every project that we get aware of and I think all this might be a really cool project for
[3012.80 → 3019.84] the open source grants um of course in the future this will get a little bit more um detailed and
[3019.84 → 3025.84] there probably will be an application process but for now this is pretty much shoot us an email and
[3025.84 → 3034.96] and let us now and then um probably I have a Skype call with you um since yeah time is an issue so
[3034.96 → 3043.68] um I'm running the foundation and Constantin has is the CEO and uh vein Fuchs is heavily involved but
[3043.68 → 3051.84] we are all like super tied in so we can't have like 10 projects running right or 10 10 grants running so
[3051.84 → 3060.48] I think for this year we will have all in all we will have three so we had RVM coco pods is running
[3060.48 → 3068.40] right now, and we have one lined up um that we will do the end of the year and that was the one i
[3068.40 → 3074.48] thought I heard you say it was SoundCloud and coco pods yes so it sounds like it's a small batch
[3074.48 → 3080.80] um and the application process isn't quite rigid it's more like email us tell us your story
[3080.80 → 3085.20] and we'll see how we can support that because i have to imagine right now there are a lot of listeners
[3085.20 → 3092.08] we get way more email way more pings on our uh on our GitHub repo that we set up for
[3092.08 → 3097.36] tracking issues basically which is um you know if you're a listener you can go to GitHub.com
[3097.36 → 3103.28] slash the change log slash ping and submit an issue and tell us about your project there is a list uh
[3103.28 → 3110.80] we do have a small bootstrapped uh you know small team I guess jarred right like me, you and a couple other
[3110.80 → 3115.52] people basically me you Andrew Alex those are pretty much the comment around the change
[3115.52 → 3121.52] law these days yep um but i have to imagine there's going to be a lot of people listening to this show
[3121.52 → 3127.44] thinking hmm Travis foundation money to do my project get it should, I go to get it should, I go
[3127.44 → 3131.92] now I'm afraid now I'm afraid to open my med program after this
[3131.92 → 3139.52] oh boy no, no awesome uh shoot us an email we're happy about every cool project
[3140.56 → 3147.28] worst case scenario I mean you can always start uh you know maybe an email list or maybe a regular
[3147.28 → 3152.00] post on the change law that talks about some of the cool projects that you all are funding because
[3152.00 → 3156.64] you know honestly with the change law there's no real I don't know jerry what do you think I mean
[3156.64 → 3161.76] there's no real direct pattern to our content we just try to do whatever we can to promote open
[3161.76 → 3169.60] source whatever we can to promote um its usefulness its community you know my life is better in so
[3169.60 → 3174.16] many ways because of open source not just because of the software itself but because of the people
[3174.16 → 3179.44] and the way that my life has been touched not only by this show but the blog, and you know
[3179.44 → 3183.84] relationships with those that come on the show and every which way you can think of I mean the ripple
[3183.84 → 3189.76] effect is massive, but you know and yeah it's awesome that Travis is doing this yeah seeing I mean we
[3189.76 → 3195.04] we focus a lot on uh open source sustainability as we see you know many people get involved with
[3195.04 → 3200.48] open source, and then you know it's hard to keep that going as it becomes less fun and more burden
[3200.48 → 3206.72] over time um especially when success brings that upon you uh surprisingly even so seeing stuff like
[3206.72 → 3213.68] corporations doing these grants I had not heard of Travis foundation previously um it'd be awesome to have
[3213.68 → 3217.76] this kind of stories be told on the changelog absolutely so we'd be happy to highlight it
[3218.56 → 3224.80] yeah I guess so back into to that jarred is um you mentioned corporations giving and Travis foundation
[3224.80 → 3231.84] so Travis foundation is a 501c3 so it is and it is a non-profit right I think we're working on it yeah
[3232.72 → 3238.48] okay so it's in the process worst case scenario but where does Travis foundation get its money to fund
[3238.48 → 3244.56] these grants is it through Travis CI I'm sure Travis has got to give a decent penny into this but then
[3244.56 → 3249.12] what is the efforts on the backside of this to raise more funds to make these grants possible
[3249.76 → 3255.04] yeah that's why we are working together with uh for example pay mail or SoundCloud so they actually
[3255.04 → 3261.68] give the money to fund the grants okay we organize this yes and Travis CI obviously um
[3261.68 → 3268.08] is giving a lot of money and yeah paying me to do this all uh to organize this oh I'll tell you
[3268.08 → 3272.64] it right here right now on the show and the listeners be ready for it, but we want to do more
[3272.64 → 3278.72] to help facilitate whatever we can around this whether it's a post on the changelog obviously
[3278.72 → 3283.60] this show here helps highlight it quite a bit as well but we want to do whatever we can to either
[3283.60 → 3288.56] help you establish relationships with corporate partners or promote any new grants that are
[3288.56 → 3293.60] being funded like I had no idea that RVM was getting funded through Travis foundation and that's
[3293.60 → 3300.80] that's awesome like Michael does a actually the last not the last show 121 but one episode 120 we
[3300.80 → 3306.72] had postmodern on we got to talk a little bit of shop around changing ruby and uh Unix paradigms of
[3306.72 → 3313.20] is it ch ruby is it ch root or is it change root so all sorts of fun stuff around that, but you know we're
[3313.20 → 3319.36] fans of those pieces of software, and it's its neat to see them get funded and continue to live on too so
[3319.36 → 3327.68] cool thank you uh no I guess no real direct questions on that one, but we are getting close
[3327.68 → 3331.76] to our time jarred is there anything else around Travis that we can talk about before we
[3332.40 → 3338.08] tail off the call I don't think so I'm just excited to see more grants like this going to open source i
[3338.08 → 3343.12] think it's its going to be awesome so I'm I'm excited that they're kind of heading it up, and it sounds
[3343.12 → 3350.32] like um you know other corporations could, can reach out to uh well how do they how do other
[3350.32 → 3356.48] corporations get involved just hit the contact form on foundation.travisci.org or what's the call
[3356.48 → 3363.68] to action there yes, yes um just go to the website yes and then there is contact button then everything
[3363.68 → 3368.72] will work out magically everything will work out magically so floor you the beginning of a wonderful
[3368.72 → 3376.08] story let me ask you work at 89s right yes I do sorry there's a little bit of latency so I keep
[3376.08 → 3382.16] stepping over jarred and Annika so I'm sorry about that guys but um no worries you floor you
[3382.16 → 3386.56] work at 89s, and we've been talking quite a bit about rails grow summer code, and you're heavily involved
[3386.56 → 3391.84] there, but you're not involved in Travis foundation is that right that's that's all right yeah that's
[3392.88 → 3396.56] you know just you know since we haven't heard you for a bit what is your perspective on
[3396.56 → 3402.96] Travis foundation like what excites you um someone that's two years into programming someone that's
[3402.96 → 3410.08] speaking and organizing and leading and teaching software development what are your thoughts on
[3410.08 → 3416.40] you know what Travis foundation is doing for open source okay so um I guess first off working for
[3416.40 → 3421.52] any nines actually enables me to work on rails grow summer of code one day a week so that's pretty cool
[3421.52 → 3428.96] that's awesome yes and then second yeah I actually worked with the Travis foundation and Annika pretty
[3428.96 → 3435.52] closely organizing um the conferences, and they definitely helped me back up the cause of you know
[3435.52 → 3442.24] having more female speakers on board and reaching out to a more diverse audience and I'm very excited
[3442.24 → 3447.36] about that I learned a lot from Annika and from the Travis foundation how they handle this so that's great
[3447.36 → 3456.00] so you're a supporter thumbs up right definitely all right cool well um we have some
[3456.00 → 3460.56] common questions we ask at the tail end of the show that they're they're fun questions sometimes but the
[3460.56 → 3467.84] the first question I'll give to Annika and um you know we generally ask it as a programming hero but
[3467.84 → 3473.92] uh the person doesn't have to be a programmer it could be just a hero I don't say the word just lightly but
[3473.92 → 3480.96] uh could be a hero someone who's uh influenced you someone who's encouraged you someone who's helped
[3480.96 → 3490.56] lead you whomever so who is your hero or programming hero Anika um yeah that's a really, really tough um
[3490.56 → 3497.92] question because I want to name you can name so many people oh I can name yeah the break the rules okay I'm
[3497.92 → 3503.44] going to break the rules and I'm going to be super cheesy but I'm going to say uh one of my heroes is floor
[3504.48 → 3511.52] and um we've never had a hero on this show at the same time by the way no it's its really encouraging
[3511.52 → 3517.28] to see what she's been pulling off how she's organizing conferences and rails girls workshops
[3517.28 → 3526.48] and not uh and not goes crazy and still is super um, um super supportive with everything, and we have
[3526.48 → 3534.64] been working together for not even a year yet and become friends even and that's I don't know
[3534.64 → 3542.32] and I've seen what she works on and how she does it and I'm amazed and always when I'm standing in
[3542.32 → 3547.20] front of a question like oh okay should I go to this conference should I dare should I go to this
[3547.20 → 3553.76] meetup I always think okay yes I should do it because floor is like doing this also what would floor do
[3553.76 → 3563.76] and we need bracelets that is awesome uh she inspired a lot of my um putting myself out there so
[3563.76 → 3574.24] um yes and another woman like I was Lena Hermann that's a German uh developer and i I got to know her i
[3574.24 → 3581.84] think when she was a single mom, and she worked at a company that i um knew, and she was actually a coach
[3581.84 → 3589.12] of the first wales girls workshop in Berlin that I actually was attending of and because I knew that
[3589.12 → 3595.44] she was going to be there I applied I thought okay, okay if she's there I already know somebody
[3595.44 → 3600.72] and this is not going to be so super awkward and she actually um supported me and said yeah you
[3600.72 → 3606.32] should really apply, and she was there when we then started wales girls Berlin and is there
[3606.32 → 3614.16] now for red girls summer of code and helping with a selection comedy, and she has uh she has
[3614.16 → 3621.52] more than one kid I don't know how much, but she's pulling it off and as a as a mom I think that's
[3621.52 → 3627.20] that even gives you I don't know how many super extra points for even like doing volunteer work
[3627.84 → 3635.12] um i I think we all can't that we all we don't have a family yet or at least that I can speak of
[3635.12 → 3642.48] myself I don't have a family yet so I can't imagine how hard it must be to do this next to your family
[3642.48 → 3649.76] work I see how hard it is for me to keep this up and keep up volunteer work and yeah so she's definitely
[3649.76 → 3654.96] a hero that I look up to and I want to be her in whenever I'm a mom
[3654.96 → 3656.96] um
[3658.24 → 3659.52] any more you got just two
[3661.04 → 3664.88] um I'm just messing with you, I got just two I got just two
[3665.52 → 3669.68] these two are how about you uh programming or non-programming hero
[3670.72 → 3679.52] okay I get really awkward around my heroes so I would say that um my heroes are and especially my
[3679.52 → 3686.32] programming heroes are the people that helped me get started learning programming um those are
[3686.32 → 3692.08] Sebastian who's been on the show before with Justine talking about open karma uh he helped me a lot in
[3692.08 → 3698.88] the beginning um tony who was my former co-worker um and Andreas uh they helped me a lot of getting started with
[3698.88 → 3707.92] programming um furthermore like a real big hero was definitely AFN grim um I read all of his books and
[3707.92 → 3713.92] and they inspired me and um taught me, so a lot taught me a lot, and then we were uh speaking at the
[3713.92 → 3721.60] same conference um at our camp last year and I just remember you know i I saw him walking in and I was
[3721.60 → 3728.96] so i I must have acted like a fool because I get really weird when this kind of thing happened
[3729.44 → 3737.28] same sort of thing uh happened when I met uh met from uh WordPress or automatic um I actually had met him
[3737.28 → 3741.68] a few times before, and we had talked before so I could have just you know walked up to him and
[3741.68 → 3747.52] and say something normal um instead I walked by and screamed something like yay WordPress and he
[3748.56 → 3755.20] screamed something back like yay it's very embarrassing and this tends to happen a lot so
[3755.20 → 3760.48] it's funny what you do when you meet like uh you know your hero like this is your hero and
[3760.48 → 3767.28] and you're and instead of being cool you're embarrassed you embarrass yourself that's I hate
[3767.28 → 3773.04] that yeah this happens especially funny maybe it's better not to have maybe it's better not to have
[3773.04 → 3780.00] heroes yeah I was going to say especially funny when with like internet based you know people you look up
[3780.00 → 3785.12] to because they're not exactly used to being known you know in real life for things like if you ran up to
[3785.12 → 3790.08] Brad Pitt, and you're like you're my hero he hears that a hundred times a day right, but you know like
[3790.08 → 3795.44] avid grim like he's at a conference and I'm sure from his perspective it's its probably a bit uh
[3795.44 → 3800.24] it's probably equally awkward for somebody to treat him as if you know they're at a Brad Pitt level
[3800.88 → 3805.04] um that has to be a fun experience of Brad Pitt definitely
[3806.96 → 3811.20] we love avid too at the change law I'm just because we're talking about him, he's also
[3811.20 → 3817.60] uh I guess not him directly but um ruby tapas is a partner with the change log so
[3817.60 → 3823.12] yep um you know we've got several you know developer tools and services as well as learning
[3823.12 → 3828.80] resources and that's one of them so if you're learning ruby, and you're learning ruby with avid
[3828.80 → 3833.04] we have a way through our membership you can save a little bit of money and still give avid the
[3833.04 → 3839.92] business but um I want to tell just a short story about myself I think it's kind of funny because most
[3839.92 → 3847.36] people know me by my voice and um my wife gets to experience this a couple of times and only because
[3847.36 → 3852.88] we're talking about this kind of odd moments but I'll share the other perspective is I'll be
[3853.84 → 3858.16] at a conference which I don't go to too many conferences often I'm just not that involved
[3858.16 → 3864.00] in conferences for whatever reason but um people will hear my voice, and they'll turn around
[3864.00 → 3869.12] and they'll say is that Adam stack because they know me as my twitter and I guess that's just kind
[3869.12 → 3874.80] of how people would go about business, but it's always funny because I'm like you hear my voice
[3874.80 → 3883.12] and you know who I am it's that was that's always the funny part but um let's see what else with
[3883.12 → 3888.08] other questions we have is um is I guess if Andrew were here he'd be yelling me right now because call
[3888.08 → 3892.88] arms at first but let's talk about call to arms I know we've kind of talked quite a bit about rails
[3892.88 → 3898.64] girls summer code Travis foundation we're all excited about um you know the fruits of this
[3898.64 → 3904.00] effort and what it's gonna where it's going to go, but you know today you know when people are listening
[3904.00 → 3908.56] to this show you know within the next week to two weeks besides donating which obviously is a huge
[3908.56 → 3914.56] call to arms but say that again if that's it um you know what is the call to arms for you know either
[3914.56 → 3919.12] summer of code or Travis foundation, and you can individually answer or
[3919.12 → 3922.72] or uh choose your uh or floor
[3925.60 → 3931.76] um okay should I go first um okay so we probably can't say that enough that we
[3932.40 → 3941.12] want you to donate, so this is definitely a call to action but also if is you can't or are not willing
[3941.12 → 3947.28] to give money or don't have so much money to give we are always looking for supporters that can help us
[3947.28 → 3952.72] in the organization part because that's all volunteer work and um or the coaches part like
[3952.72 → 3959.36] we said we are going to have a help desk a remote help desk so if you're a programmer and say yeah
[3959.36 → 3967.20] okay I can hang around campfire some hours um do it awesome just shoot us an email and um yeah just
[3967.20 → 3973.60] get involved and risk as a mouth code it's its a whole community project and yeah this is the call-out to the
[3973.60 → 3980.00] the community also Annika correct me do you feel the same of course I feel the same
[3983.52 → 3990.08] um Annika you have to correct me if I'm wrong but do we have like if someone wants to help out with uh
[3990.08 → 3996.88] with the help desk if they register by their team set can they know say that they want to be in the
[3996.88 → 4003.68] help desk because I know that last year that was the case sure yeah you can say you can check the box
[4003.68 → 4008.80] remote code or help desk code awesome, so then people just have to go to teams.rails girls
[4009.52 → 4016.80] summer of code.org and register as a help Decker that would be awesome help desk or have I heard that
[4016.80 → 4022.80] one before and maybe um if you're a conference organizer, and you definitely want to have some
[4022.80 → 4028.48] great uh rails girls summer of code students in your audience and giving a lightning talk about
[4028.48 → 4034.08] rails girls summer of code um well you're very welcome to give away some free tickets to them
[4034.08 → 4041.44] and maybe even help them with their travels and stay yes absolutely nice I know code front.io is
[4041.44 → 4047.28] is happening right now we just um gave away some tickets' oh it's I thought it was today that's why I'm
[4047.28 → 4052.64] in Vienna right now so there you go so you'll be there we were giving away some tickets there and
[4052.64 → 4057.60] yeah so is there any lightning talks going on there for yes rose go summer code well there is a lightning
[4057.60 → 4064.96] talk uh track and there will be someone probably me talking about rails girls summer of code so yeah
[4065.76 → 4069.36] yeah I'm a member of the team so I can definitely do this conference it's perfect conference
[4070.56 → 4076.08] I'm looking forward to this uh and I guess the last one is uh if you weren't
[4076.08 → 4081.44] I guess running Travis foundation and leading that or if you weren't organizing rails
[4081.44 → 4087.12] girls summer code or participating uh we'll let you go one at a time but what would you be doing if
[4087.12 → 4092.72] you weren't writing ruby or doing the organization of these awesome efforts Annika we'll let you go
[4092.72 → 4098.80] first like for money what would I do for money yeah like well I guess you know what would you
[4099.68 → 4103.36] yeah if you weren't doing that what else would you be doing like would you be your you study
[4103.36 → 4110.16] lingo you study linguistics and um looking back at your profile how do you say that linguistics and
[4110.16 → 4116.40] gender studies so I'd imagine probably something in that range right or maybe not uh yeah maybe not
[4116.40 → 4121.36] because when I finished studying gender studies I said oh no way I'm gonna work in this field
[4121.92 → 4129.60] because it's just too harsh no um yeah I would probably be writing a lot and um and doing
[4129.60 → 4136.16] my own thing my I've been dreaming about starting a co-working space uh forever and have a little
[4136.16 → 4142.56] café there so that's probably where I would be you and I should talk because I've had a similar desire
[4142.56 → 4148.08] but I'm not in a place where that would be possible so I just had a dream as well oh okay yeah let's
[4148.08 → 4152.08] talk I actually wanted to make it a cop well I mean that's kind of cliché though right coffee shop
[4152.08 → 4156.64] and co-working space it's been done before but i kind of wanted to put a little twist on it and
[4156.64 → 4161.68] I got a feeling that Dan Benjamin is one day going to take this idea and run with it and do it better
[4161.68 → 4166.32] than I'll ever do it but here's the idea is that I want to say it out loud yeah don't share
[4168.24 → 4172.08] you should start a secret club, and then we'll make some great co-working space
[4172.08 → 4177.52] I shouldn't tell anybody you want to know tell us the twist after we stop the call okay
[4177.52 → 4182.80] fine I'll tell the callers only if you're listening to this, and you absolutely have to know just email me
[4182.80 → 4187.12] Adam at changelog.com, so everybody's really frustrated
[4188.16 → 4194.00] he's going to say it, but he's not going to do it man uh what about you flor what if you weren't writing ruby
[4194.00 → 4199.52] if you weren't uh attending all the conferences and coaching and organizing all that you do what would
[4199.52 → 4206.48] you be doing if you weren't doing that so um actually I graduated as um as a graphics designer at
[4206.48 → 4212.40] art school in the inlands and then I changed um to doing a lot of sorts of community management work
[4212.40 → 4218.24] and then I changed to becoming a programmer I think I have enough changes in my life so far
[4218.24 → 4223.52] and I'm still getting used to this whole you know uh programming and doing a lot for the developer
[4223.52 → 4231.20] community and which I enjoy a lot um i also really found my way um in this whole tech world uh writing
[4231.20 → 4237.20] technical documentation I love doing this I love writing issues people think I'm crazy for this but i
[4237.20 → 4242.48] really love doing all documentation stuff so um I think I actually found my place already
[4244.08 → 4248.72] nice so you're doing what you would be doing then so if you weren't doing this you would be trying to
[4248.72 → 4256.40] find a way to do what you're doing I'd be crying all the time well at least you're honest that is cool
[4256.40 → 4262.16] yeah you know writing docs and issues are not my forte I don't mind doing them when I have to but
[4262.16 → 4266.96] I do have to commend you on having a passion for that because that's, that's unique now you can
[4266.96 → 4274.00] always ping floor if you don't yeah totally why don't I speak for the entire team here at the
[4274.00 → 4278.64] changelog when I say that it's been a pleasure to have you both on the show this week the work you're
[4278.64 → 4284.80] doing is super important and uh rails grow summer code Travis foundation we want to be a part of that
[4284.80 → 4290.08] future so we want to support you however we can uh this year next year in the years to come so
[4290.08 → 4296.00] whatever we can ever do to support you in both of those missions or even personally just let
[4296.00 → 4301.44] us know reach out you have a friend now um and I also want to give a shout-out to our sponsors
[4301.44 → 4310.40] uh the sponsors of the show are ninefold code ship and top towel and uh we love their support they're
[4310.40 → 4316.32] absolutely great to us code ship and top to happen to be partners as well as sponsors and that means that
[4316.32 → 4321.68] they're uh supporting us in the long term they're investing in the future of the change law to make
[4321.68 → 4326.40] sure that we're always here um doing the work we're doing to support open source, and we thank them for
[4326.40 → 4332.00] that ninefold we hope to have as a partner in the future as well um we'll hope that uh that to come
[4332.00 → 4336.40] but they're awesome companies we absolutely love their support uh and couldn't uh couldn't do this
[4336.40 → 4343.20] without them so um we do have an awesome show lined up next week chad Whitaker the founder of get up is
[4343.20 → 4349.20] going to be on the show uh should be a fantastic conversation if you're not using get up or uh or
[4349.20 → 4354.72] whatnot to kind of crowd fund your work in open source or whatever you're you're doing the people
[4354.72 → 4361.52] you inspire get up.com is uh is a cool thing so next week tune into that until then let's say goodbye
[4361.52 → 4375.52] goodbye bye bye
