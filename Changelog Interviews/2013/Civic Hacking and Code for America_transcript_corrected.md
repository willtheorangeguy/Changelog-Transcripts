[0.00 → 13.44] welcome back everyone this is the change look where remember supported blog and podcast
[13.44 → 17.42] that covers what's fresh and what's new in open source you can check out the blog at
[17.42 → 22.48] the changelog.com and our past shows at five by five dot TV slash changelog the show is hosted
[22.48 → 29.52] by myself Adam static and also Andrew Thorpe Andrew mayor hey how's it going it is going well
[29.52 → 34.40] you can tune in live to the show every Tuesday at 5 p.m Central Standard Time right here on five by
[34.40 → 40.88] five and this is episode number 95 we're joined by mike Maersk he's the CTO for code for America
[40.88 → 49.24] and Ezra spire I said that wrong Ezra it's spear very close enough spear uh he's also a fellow at
[49.24 → 53.56] code for America code for America is a new kind of public service it's by the people for the people
[53.56 → 58.80] and it's for the 21st century I think it's the coolest line ever uh welcome to the show uh fellas
[58.80 → 64.98] thank you great uh great to be here yeah, thanks so much for having us absolutely so we've uh we've
[64.98 → 69.54] actually had you guys not you guys in particular on the show before but uh back at episode number 65
[69.54 → 76.54] uh we had Eric Michaels over and max Ogden on the show uh talking about code for America great
[76.54 → 82.76] conversation there I'd like to kind of extend that a little bit too but uh um definitely fans of code
[82.76 → 88.22] for America what you guys are doing so why don't we take a minute and uh maybe introduce you guys so
[88.22 → 94.66] mike we'll start with you sure yeah hi um, so my name is Michael Maersk and I'm the chief
[94.66 → 100.06] technology office here at code for America um fairly new here actually I just joined the organization a
[100.06 → 106.12] few months ago and uh prior to that up until the end of last year I was CTO and technical director at
[106.12 → 112.36] stamen design uh design mapping and information visualization firm located here in San Francisco
[112.36 → 118.46] did that for about I want to say nine years and did a lot of work with open source GIS open source
[118.46 → 123.24] geography open source cartography over all that time um been a huge fan of code for America for a
[123.24 → 128.92] number of years we actually hosted the organization uh in our mission district office for its first six
[128.92 → 133.88] months of life so it's kind of great to be here as a proper full-time member now, now so you got some
[133.88 → 138.04] roots then this isn't uh I mean because you just joined the team two months ago right but your
[138.04 → 144.42] your history with code for America goes back pretty far yeah pretty far I've been friendly with Abby and
[144.42 → 150.46] Jen and Megan and everybody else at CFA ever since they first got started cool all right Ezra how about
[150.46 → 157.84] you sure yeah my name is Ezra spear and I'm a fellow here for 2013 at code for America and I think maybe a
[157.84 → 161.48] little bit later we'll describe what that actually means because that it is a pretty interesting and
[161.48 → 167.58] unique kind of position I have but before I was a code for America I started in January I was living in
[167.58 → 173.54] Portland Oregon at and working as a developer at a coffee company called sustainable harvest coffee
[173.54 → 178.54] importers where I was actually building applications to track coffee as it moves around the world
[178.54 → 183.16] increase traceability in that industry it's you know when you hear about coffee you know you think a lot
[183.16 → 187.86] about um roasters and cool coffee shops and stuff but not so much about the people that actually grow
[187.86 → 193.06] the coffee so I was building apps for those folks um even some really cool educational apps used in
[193.06 → 199.16] places like Peru and Tanzania um and now code for America I'm sort of applying the skills i I learned
[199.16 → 203.62] in um in that context and bringing them to local governments around the United States so
[203.62 → 210.22] uh it's a lot of fun and um I'm excited to chat with you guys today yeah absolutely I'm you know maybe
[210.22 → 217.46] um maybe let's open it up like this because I think it's a little um since you know 65 is uh is far
[217.46 → 223.22] back so we've it's been a while since we have this uh topic on the show but um as I understand it code
[223.22 → 231.40] for America is a startup right yeah did uh did you not hear what I said I did yeah you were asking
[231.40 → 235.48] whether code for America is a startup is that right yeah I'm trying to figure out what code for America is
[235.48 → 241.00] I mean I remember the conversation back in the day but um you know it's its it's civic hacking so
[241.00 → 247.30] it's for um it's to you know to develop the technology space for our cities and our government
[247.30 → 253.74] but I'm kind of curious you know is it a startup is it what is the makeup of code for America yeah i
[253.74 → 260.08] mean we're structured around a fellowship program and uh what that means is that every year for the
[260.08 → 266.48] entire calendar year we have a class of 25 to 30 fellows who join us um these are people who apply
[266.48 → 271.82] to join us they go through a fairly rigorous selection process like Ezra did um and they come
[271.82 → 277.22] to us as designers they come to us as developers urban planners and other professions uh typically
[277.22 → 282.40] you know kind of in the middle to early part of their careers looking to make a change or transition
[282.40 → 289.46] into government um on the other side we work with cities who also apply to be code for America cities
[289.46 → 296.40] this year we have a mix of nine cities and counties including New York city um Oakland California
[296.40 → 302.66] Louisville Kentucky Summit County Ohio and a few others um, and they come to us with very specific
[302.66 → 308.16] problems you know some of them want to work on uh things like criminal justice others want to work
[308.16 → 314.20] on economic development still others want to work on food availability and um food banks and things like
[314.20 → 320.02] that, and essentially we create kind of a design camp design process built around this where for 11
[320.02 → 325.16] months out of the year the fellows and cities work together to create a response to some sort of
[325.16 → 331.06] problem that the city is experiencing that could use a technical solution so how many cities usually
[331.06 → 336.04] apply each year uh you know I'm actually not sure I want to say that it's something like 20 or 30 this
[336.04 → 342.66] year um we're currently in the process of narrowing down our selection for the 2014 cities and I think
[342.66 → 348.36] we have it down to a list of something like 10 or so finalists, and so they come to you each year
[348.36 → 354.16] basically with a problem set maybe before the fellowship begins and part of the fellowship this 11 month
[354.16 → 359.24] program is about tackling and solving some of those problems yeah we try to frame the problems in a
[359.24 → 365.40] somewhat general way um so for example a city may want to work on you know economic development but
[365.40 → 369.70] that doesn't mean that they're coming to us with a specific application that they want built we're not
[369.70 → 377.62] like a vendor or a contracting agency uh we work with the cities to figure out what the real nut of the
[377.62 → 382.56] problem is um and then develop solutions based on research that gets performed early on in the
[382.56 → 388.06] fellowship so does one fellowship from one year to another kind of piggyback off of one of those
[388.06 → 394.04] work like did this last year's program kind of bleed into this year's program and then you know
[394.04 → 400.48] on and down the line uh in many cases yeah the fellowships themselves will end at the end of the year
[400.48 → 406.52] um and then some people will stay on in other positions so for example we have uh two folks from last year
[406.52 → 411.76] um who stayed on as a designer in residence and an engineer in residence after completing their
[411.76 → 417.16] fellowship um and in some cases like for example with Philadelphia cities will come back for a second
[417.16 → 422.88] opportunity to work with us um generally speaking the way that the fellowships, and you know the years
[422.88 → 430.04] feed into each other is through our very extensive GitHub repository of projects uh and through the
[430.04 → 434.34] startups and additional projects that fellows go on to do with their work after they're finished with
[434.34 → 442.84] the fellowship that's pretty cool so um let's let's talk about um I guess one of the topics that you'd
[442.84 → 447.76] mentioned when we had a kind of pre-call you talked a lot about um your desire to talk about
[447.76 → 454.68] technical sustainability um as it relates to the different challenges you guys are helping cities
[454.68 → 460.06] that apply to code for America to solve um you know what is some of the number one challenges that cities
[460.06 → 466.08] are I guess facing with technical sustainability yeah I think that there's really kind of a broad
[466.08 → 472.84] set of challenges that cities are facing, but the two top ones probably are um different expectations
[472.84 → 479.64] around technology um and then also different expectations around things like budgets and how
[479.64 → 484.20] many things cost uh so in terms of expectations around technology you know as you might imagine
[484.20 → 490.60] uh the people who join us from industry as fellows are frequently working with application stacks like
[490.60 → 497.30] you know python or Ruby on Rails or node.js you know fairly new fairly modern technologies while on the
[497.30 → 502.62] flip side city its departments tend to be composed of much older technologies so they might be exclusively
[502.62 → 508.18] Microsoft shops um, or they might require that things be built on an oracle database and so forth and so
[508.18 → 513.60] there's a huge sustainability challenge in figuring out how to kind of draw those two worlds together
[513.60 → 518.72] and make sure that the kind of open source methodologies that we use for all of our work
[518.72 → 522.96] uh can be adequately reflected in the environments that cities are deploying in
[522.96 → 529.14] you mentioned uh your GitHub page there um and obviously we kind of know on this show that GitHub
[529.14 → 535.34] kind of represents open source software right so absolutely how much um how much is uh I guess
[535.34 → 542.34] over the years of fellowships how much have you seen open source begin to form and shape and
[542.34 → 548.84] reshape uh ideas for city government it's been colossal I mean we have projects from our very
[548.84 → 554.38] first year of fellowship back in 2011 that are still being worked on and extended and redeployed
[554.38 → 560.22] by fellows today so I think that the idea of open source is something that's really informed the
[560.22 → 571.02] entire fellowship cool you mentioned um people that uh join, or you know apply to be a fellow for
[571.02 → 576.00] this live month program that they're either wanting to make change or get involved with government what
[576.00 → 582.98] are some of the things that um some of the fellows have gone on to do like I know uh, uh Eric and max
[582.98 → 587.16] we mentioned they've been on the show before what they do now I think Eric is actually in Berlin
[587.16 → 593.52] uh I know uh max has been working hard on some other fun stuff in open source and I'm not sure if he does
[593.52 → 599.56] full-time but um those are just two examples but what are others doing I guess as they move on from
[599.56 → 603.58] their fellowship oh they go all over the place it's actually really fun to see we've had a couple
[603.58 → 608.44] fellows from the very first year move on to actual positions in city government over in Boston
[608.44 → 616.00] um we've had a number of fellows especially from last year who have turned their projects via our
[616.00 → 621.90] incubator program into proper startups so they've done applications around blight monitoring in new
[621.90 → 628.22] Orleans or text messaging in the case of textile and have turned those things into startups with like
[628.22 → 634.52] actual revenue and business expectations around them uh in other cases we've seen fellows move on
[634.52 → 639.74] to open source companies and other technology companies uh one of our fellows from last year
[639.74 → 644.10] Jessica lord has actually moved on to GitHub itself so it's kind of interesting seeing a lot of graduates
[644.10 → 650.40] move on there um other people have gone out to companies like Airbnb I think google might be one of
[650.40 → 655.98] them, so people go on to do a lot of interesting stuff from here that's cool I wanted to ask how
[655.98 → 662.06] do the projects actually get like selected and which fellows work on them and like what does that
[662.06 → 666.74] process look like in-house yeah so I mean Ezra you're actually in the midst of the fellowship do
[666.74 → 671.64] you want to maybe talk about it sure yeah so um you know the application process I'm going to put a
[671.64 → 676.12] quick plug out here early at the beginning of the show saying that we're actually looking for fellows
[676.12 → 679.70] for next year right now the applications are due at the end of the month on the 31st
[679.70 → 685.90] code for america.org slash apply um, but fellows come from a variety of backgrounds um we have folks
[685.90 → 690.50] who do you know hardcore software you know front-end back-end developers we have folks who are coming
[690.50 → 694.52] more from a design side or more from government side and the way that our teams are formed they're
[694.52 → 699.60] sort of cross-disciplinary we have uh you know my team has two developers and one designer on it
[699.60 → 705.32] and um we sort of knew coming in um that we were assigned to New York city which is where I'm working
[705.32 → 711.04] and we knew that our project focus was going to be criminal justice and in particular we were looking
[711.04 → 716.46] at a particular part of criminal justice the time between when a person is arrested and when they're
[716.46 → 721.38] sentenced um there's some basically some new theory saying that these are this is sort of the time
[721.38 → 724.94] within the criminal justice system where we can really have the chance to help people
[724.94 → 731.36] stay out of trouble in the future and knowing that um so we sort of all came here in January when
[731.36 → 737.24] the fellowship started um and the process begins with a sort of month-long training process since we
[737.24 → 740.78] all come from so many different backgrounds and a lot of us haven't actually worked in government
[740.78 → 746.24] before it's sort of like a month-long crash course in how government works how open source works
[746.24 → 750.88] um different strategies that have worked and haven't worked in trying to engage with governments
[750.88 → 755.72] we even had a day-long uh negotiation training which sounds like sort of a weird thing but um
[755.72 → 760.70] it really gave our teams uh a good ability to learn how to like talk to people, and we're sort of
[760.70 → 764.84] realizing you know we talk about open source you know in this community like it's sort of just
[764.84 → 769.20] something we know is good but when you're talking with folks that maybe aren't as familiar with it
[769.20 → 774.18] or see it maybe even as something that's threatening the way they do their work um you need to be
[774.18 → 778.50] really cognizant of where they're coming from and how to sort of talk to them and really understand
[778.50 → 782.54] them so that you're not actually just being rude or dismissive of the kinds of needs
[782.54 → 787.58] they have um but in terms of your question of you know how do actually projects get selected
[787.58 → 794.24] um after a month-long training the three you know team members for New York and the uh 20 27
[794.24 → 798.08] fellows this year who are working with nine different cities and counties basically did a
[798.08 → 803.70] month-long inter intensive residency where we flew out to our cities uh we lived there we lived all
[803.70 → 809.52] together in houses in each and our each of our cities and uh basically did a month of uh interviews
[809.52 → 814.86] where we talked with people that work in the city citizens community groups uh in our case uh since
[814.86 → 819.86] we were focused on criminal justice we were talking to uh judges and people in courtrooms and lawyers
[819.86 → 824.54] and those sorts of folks to try to ask the question of what's broken um what's not working what could be
[824.54 → 831.68] better and from there we sort of used a collaborative process of deciding you know what problem we want
[831.68 → 835.82] to tackle and what apps we want to build this is really different by the way from the way that
[835.82 → 842.64] most governments work with technology most of the time um there's some need that people sort of see
[842.64 → 848.36] let's say it's you know drivers licensing um you know data management or something, and then they'll
[848.36 → 853.96] issue a know RFP a request for proposals and vendors will bid on those proposals, and then they'll
[853.96 → 858.82] choose someone that that builds the application to a know potentially enormous spec for a
[858.82 → 862.92] potentially large amount of money, and we're sort of trying to demonstrate that we can look at
[862.92 → 868.62] problems from the ground up use sort of this um agile um idea not just in software development of
[868.62 → 873.86] problem-solving starting with something small building something and testing it to try to solve
[873.86 → 878.78] a small problem and then building off of it um and expanding it to fill other things as well so
[878.78 → 883.74] it's sort of a new idea um with a lot of governments, but folks are starting to get pretty excited about it
[883.74 → 890.14] I'm kind of curious about uh I guess city collaboration you know when I think about
[890.14 → 895.54] you mentioned um you know driver's license and data sets and stuff like that around that and
[895.54 → 902.24] different applications that might make sense um at what point do cities begin to speak at the
[902.24 → 906.92] government level around technology is there some sort of um I mean is that what our national
[906.92 → 911.36] government helps to accomplish or is it up to the cities and individual states to help kind of
[911.36 → 916.48] lift those cities up and speak to one another to maybe have a unified system for dealing with
[916.48 → 922.20] driver's license for example well I think it's sort of a mix um you know think about it this way if
[922.20 → 926.78] you're working at a startup or any other company who's going to make the decisions about technology
[926.78 → 931.48] it'll be the people there um it won't necessarily be anyone telling you what to do there though you
[931.48 → 935.84] might have a sense of what the best practices are in your particular field or industry and I think
[935.84 → 942.74] in government it's largely the same um but because of the way that procurement that's the way that
[942.74 → 947.62] you know government entities select vendors to build software but because of the way that works
[947.62 → 953.08] oftentimes cities and counties and states and the federal government are sort of going it alone
[953.08 → 958.74] and um looking for products that meet their needs um from the open source world we know there's this
[958.74 → 964.44] huge advantage of actually collaborating to solve problems and to build something together but uh in
[964.44 → 968.28] the government world that's a little bit more rare and that's one of the things that we're trying to
[968.28 → 973.74] do at code for America is by working across multiple cities and counties and states at once we can sort of
[973.74 → 980.16] start to see those um similar problems emerge and then find ways to bring people together to look at
[980.16 → 987.70] them together what kind of response do you tend to get from the cities themselves like are they
[987.70 → 993.36] interested excited, or you know what kind of response do you get when you're actually talking
[993.36 → 997.02] with the government of the cities that you're going to be working with in your experience Ezra
[997.02 → 1003.62] well I think um I think you'll have a sort of multitude of responses, and it depends on sort of
[1003.62 → 1006.84] who you're talking to and why because remember city governments are not unified we're talking
[1006.84 → 1011.44] especially in the case of New York city is thousands and thousands of people all with different roles
[1011.44 → 1017.28] and different needs that they have to do for their work um I think most of our cities we
[1017.28 → 1022.04] partner with are ecstatic to be uh participants in the code for America fellowship program and the other
[1022.04 → 1026.94] programs we have because they see us as a way they can do their work better uh
[1026.94 → 1032.58] they have uh things they do whether it's you know driver's licensing or uh you know having a police
[1032.58 → 1036.58] force or any of those other services that we think of when we think of government um but they
[1036.58 → 1040.00] never have enough resources to be able to do everything they possibly want to do, and they see
[1040.00 → 1045.42] technology, and particularly you know our kind of open source technology as a way of doing better
[1045.42 → 1050.70] work maybe for less money and that's awesome when it gets to actually building software though
[1050.70 → 1055.76] it's a little bit more complicated as mike was saying earlier you know folks that run it
[1055.76 → 1060.38] departments have particular methodologies and stacks and things they're they're really comfortable
[1060.38 → 1066.92] with and sometimes us coming in there uh shakes the uh, uh shakes things up a little bit but uh because
[1066.92 → 1073.38] we're sort of usually engaged at a higher level on the political side but also um also working with
[1073.38 → 1077.18] people who are doing their day-to-day work we're usually able to uh to make things work right now
[1077.18 → 1083.48] I'm working with New York I'm in the middle of an uh it processes we're trying to get servers provisioned
[1083.48 → 1088.28] trying to get Linux set up and all that sort of good stuff and I'm used to in my normal life just
[1088.28 → 1093.22] firing up Heroku or getting an ec2 instance or doing what it takes myself just to get the
[1093.22 → 1097.60] infrastructure I need and that's something that um is a little bit harder I think in a larger
[1097.60 → 1103.52] institution like government right now so we're trying to sort of show what's possible uh with a
[1103.52 → 1109.76] small amount of resources yeah and i just I'm like having a little bit of a hard time visualizing so
[1109.76 → 1114.00] essentially you know when this started for you in your first month when you just kind of
[1114.00 → 1120.00] got dropped into New York city um what did you like where did you go what did you do what
[1120.00 → 1124.96] what was your I mean this is so interesting to me but what was your first you know thought of where to
[1124.96 → 1131.14] get started so the way that we work is that uh with each sort of local partner, and we've right
[1131.14 → 1135.82] this year we're working with nine different cities and counties across the United States from New York
[1135.82 → 1141.54] where I am the San Francisco Oakland Las Vegas Summit County Ohio which is the county around Akron
[1141.54 → 1146.42] we're working in a ton of different places and as Mike was saying each one of these governments
[1146.42 → 1153.04] has sort of chosen one topic that they want us to work on for the year um the way that our
[1153.04 → 1158.06] partnerships work is we generally have one or two primary people within the city government who are
[1158.06 → 1164.64] serve as our main contacts and sort of our liaisons um usually one of them is working in the topic
[1164.64 → 1169.96] area that we're working in so in the case of uh Summit County they're doing a project related to
[1169.96 → 1173.48] parks so they have folks in the parks there that they're working with primarily
[1173.48 → 1179.78] um, but then they also have contacts in it or technology departments of those cities as well so
[1179.78 → 1184.44] we have sort of a late liaison both on the sense of understanding the problem and also understanding
[1184.44 → 1190.52] how technology gets built um so when we showed up at the beginning of February our primary contact is a
[1190.52 → 1196.08] fellow uh in New York city government um underneath the mayor's office in an office called the office
[1196.08 → 1200.30] of the criminal justice coordinator and I don't know if you've ever watched lot order or any of
[1200.30 → 1206.34] the other you know New York cop shows yeah but um you know one of the things about criminal justice it is
[1206.34 → 1212.30] so complicated it's especially it's especially complicated as an uh person with no background in
[1212.30 → 1216.86] that system but even I think for lawyers and other people it's pretty complicated and our
[1216.86 → 1222.56] main contact has been working as a lawyer for many years in New York city he understands the system
[1222.56 → 1226.80] really well he's he's been a defence attorney he's worked for the government, and he knows everybody
[1226.80 → 1231.54] and so working with him and with some of our other friends we were able to set up meetings with people
[1231.54 → 1241.82] all across the system so you know police uh courts um uh probation you know district attorneys all the
[1241.82 → 1246.44] sort of players that are involved in the process and and and you know by talking with each of them
[1246.44 → 1252.20] we can start to get a sense of uh of what's going on so what projects specifically have you been
[1252.20 → 1258.48] working on in terms of open source with uh New York so we're still sort of uh figuring out what
[1258.48 → 1264.12] exactly the end result's going to look like I think um a lot of the work that code for America's
[1264.12 → 1268.82] done in the past has been on open data and I think we'll come back to that in a second but um
[1268.82 → 1273.14] you know we're talking about criminal justice we're talking about people who are being arrested
[1273.14 → 1279.28] and who are having some you know really serious things happening in their lives um there's a lot
[1279.28 → 1284.66] of private and sensitive data that is a little bit harder to work with we can't totally do that out
[1284.66 → 1289.82] in the open because we don't um we don't want to share all this data it's not it's not legal to share
[1289.82 → 1297.00] it in many cases and so the kind of work that we're doing is applications that help bring data about
[1297.00 → 1302.76] uh people who are being arrested to folks who can really help them out and um you know working
[1302.76 → 1307.26] alongside the infrastructure that the city has already sort of put together to help make the
[1307.26 → 1313.54] system faster building applications that uh provide new views of data and better streamlined views of
[1313.54 → 1318.34] data to the right people and that's a little bit of a vague answer but um it's sort of building on the
[1318.34 → 1321.60] on the shoulders of the kind of work that's already been happening in New York to
[1321.60 → 1328.58] to make the criminal justice system smoother than it is right now gotcha so you're being named code
[1328.58 → 1333.76] for America and obviously getting involved with government um how do you and maybe this is a
[1333.76 → 1338.82] question better for Michael but how do you kind of get involved on the like ethics side and the
[1338.82 → 1343.46] government side with uh like I would imagine you try to avoid the politics side of things
[1343.46 → 1349.58] yeah that's absolutely right I mean one of the things that we discovered very early on in the
[1349.58 → 1354.90] program three years ago was that we had to be very, very careful about how we interfaced with the
[1354.90 → 1361.08] political side of things uh so what we look for as we do our city selection is the ability to work
[1361.08 → 1365.56] for a current administration that's not for example on its way out due to an upcoming election
[1365.56 → 1372.00] um and one that can actually you know get people into rooms for meetings it's really important that
[1372.00 → 1376.66] fellows like Ezra be able to have access to the people in the city that they need to have access to
[1376.66 → 1383.32] so in terms of politics what we're looking for is someone like a CTO or a CIO or a mayor's chief
[1383.32 → 1387.94] of staff or somebody at that level of government who can basically smooth the runway for us and let
[1387.94 → 1392.94] the people in the city know that you know code for America is coming answer their phone calls
[1392.94 → 1398.52] they're here to help pay attention yeah exactly that's cool I mean at least you have that kind of
[1398.52 → 1404.32] clout to be able to do that I mean as I could imagine that your success uh you know year
[1404.32 → 1411.44] over year has kind of afforded you that that ability too yeah I think so I mean you know
[1411.44 → 1417.60] obviously I'm new here but I've also really had a nice vantage point over the past few years to watch
[1417.60 → 1423.64] how the team has been working um and I think a lot of that success is really encoded in the happiness
[1423.64 → 1430.32] of CIOs and CTOs that have worked with us, you know I've spoken to people like john told from Chicago and
[1430.32 → 1433.80] they've told me that they've just been really thrilled with the code for America mission and
[1433.80 → 1438.42] in a lot of cases it's not even so much about the specific code that gets generated, although that's
[1438.42 → 1444.04] a large part of it um, but it's really about the process that code for America brings it's you know
[1444.04 → 1449.32] being able to spend almost an entire calendar year just focusing on a city's issues and problems and
[1449.32 → 1453.96] working on a variety of different solutions for them and trying to kind of draw connections between
[1453.96 → 1459.20] disparate systems and data sets um that I think is really where a lot of the value comes in it's that
[1459.20 → 1465.06] ability for us to act as sort of lateral thinkers across a government uh where the people that we're
[1465.06 → 1472.14] dealing with are potentially you know members of a hierarchy of sorts you know in it department
[1472.14 → 1477.66] or in the criminal justice department and really unable to forge some of those connections across
[1477.66 → 1483.26] government uh that they would like to, and so we almost become kind of like an I don't know like a
[1483.26 → 1489.06] cut across an organization in a way yeah it's cool because it's almost like the city itself I'm
[1489.06 → 1495.14] sure it's refreshing for to them to be able to actually you know see things start to happen
[1495.14 → 1500.46] without all as much of the red tape and the huge grants that need to go out, and you know this and
[1500.46 → 1507.60] that so to see problems real problems get people dedicated to working on them um just for the sake of
[1507.60 → 1512.08] fixing problems I'm sure is refreshing to those cities that apply yeah that's definitely something
[1512.08 → 1517.50] that we've been seeing across the kind of civic hacking and civic technology world as well is that
[1517.50 → 1521.34] one of the reasons why this is such an interesting space for a lot of these folks is because
[1521.34 → 1527.58] it's a way for them to look at problems at an angle that they haven't really seen them at before
[1527.58 → 1533.78] and that ability to kind of dive in and try solutions in a way that's much more influenced by
[1533.78 → 1539.14] you know like lean and agile methodologies of code applied to civic problems I think is quite
[1539.14 → 1546.16] interesting for them to see has there been any like you know so and I hate to go sports here but
[1546.16 → 1553.52] um you know during the last you know 15 years of sports it's gone from like a gut feeling
[1553.52 → 1559.66] type of atmosphere to more of like a data driven in an uh you know statistic driven world and I'm
[1559.66 → 1564.42] wondering if when people like you guys that are coming into these cities and approaching these
[1564.42 → 1571.74] problems from as you pointed like a data mindset um has there been a reaction from other a response
[1571.74 → 1578.36] from people in the cities to want to go in that direction rather than what politics seem like you
[1578.36 → 1583.66] know government seems like so much as an is a gut feeling and a know uh that sort of driven
[1583.66 → 1590.64] field to switch that up and go into like a statistic and data driven environment yeah the reactions have
[1590.64 → 1597.66] been quite positive I think that um you know the particular kind of data that drives us is really based on
[1597.66 → 1605.50] kind of user research and needs finding exercises so it's about figuring out what a kind of minimum viable
[1605.50 → 1611.72] product or prototype is that we can deploy in that city really early on in the fellowship uh and then
[1611.72 → 1616.50] sort of iterating on that and working on new versions of it so it's really close to the kind of
[1616.50 → 1621.34] you know open source way of doing things where you have a general sense of where you want to go
[1621.34 → 1629.94] um an ability to actually push a piece of code or a design solution or some sort of prototype in that
[1629.94 → 1634.72] direction and then very rapidly gather information about how people are responding to it whether it's
[1634.72 → 1639.68] working for them or whether it's falling on its face oh yeah I mean and you said something there
[1639.68 → 1645.08] when you talked about you know what we in the technology you know world know is the minimum viable product
[1645.08 → 1651.62] and I think that in politics in government that is something that is not even considered most of the time
[1651.62 → 1656.20] right so how often do you hear about these huge grants these huge proposals that go out to accomplish
[1656.20 → 1662.14] these massive tasks and these tasks take you know 10 years and if they make it to completion they took 10
[1662.14 → 1668.18] years but if not they get abandoned at five years and you know these the thought of like a minimum viable
[1668.18 → 1674.06] product it you know it almost seems like if we can get people in the government people in you know the
[1674.06 → 1680.22] public sector to consider solving the minimal you know solving these problems like it's approaching
[1680.22 → 1685.12] a specific problem and solving it with a minimum viable product it almost you know you could
[1685.12 → 1691.12] kind of extrapolate that and say less money could get wasted less you know projects could get abandoned and
[1691.12 → 1695.56] more work could actually be done and if nothing else I would think code for America kind of bringing that
[1695.56 → 1701.58] mindset to uh cities is a very, very positive thing yeah it's really about putting everybody in a position
[1701.58 → 1707.44] where they can learn as quickly as possible uh one of our board members Eric Reese who uh created a lot of the
[1707.44 → 1712.78] terminology around the lean and agile startup talks about the idea of creating uh I think his words are like an
[1712.78 → 1721.74] alternative space for um for doing kind of testing and uh accountability of these things and what he's really
[1721.74 → 1729.26] talking about is a way to you know modify normal expectations around technology being this like you know one huge
[1729.26 → 1733.58] giant release slug that happens at the end of a multi-year process into something where you're
[1733.58 → 1739.86] doing smaller releases more quickly uh you know closer to the gate and then learning from them as you go
[1739.86 → 1742.32] in order to adapt to what the reality is
[1742.32 → 1750.44] yeah this is oddly enough not oddly I mean obviously he's been incredibly influential in this world but I think
[1750.44 → 1754.52] Eric Reese has been mentioned on like four of the last five shows we've done so that's pretty cool
[1754.52 → 1762.20] huge fan of Eric Reese here by the way um mike earlier when we chatted when we're doing soundcheck you mentioned
[1762.20 → 1766.16] a topic that I'm not too familiar with but I'm hoping you can expand on it which is
[1766.16 → 1770.72] something a little closer to your heart being the new CTO at code for America so you mentioned
[1770.72 → 1776.98] deployment environment is one of the points that you want to talk about on the show what did you mean by that
[1776.98 → 1782.60] yeah I've been thinking a little bit about kind of what the environment is that we push our software into
[1782.60 → 1788.52] um and I'm trying to create sort of a language around it or a way of thinking about it that
[1788.52 → 1793.52] encompasses both the technology deployment environment which is to say you know Linux versus
[1793.52 → 1799.72] windows versus rails versus python all that usual kind of stuff um and then also the kind of political
[1799.72 → 1805.18] and emotional and human environment that that lives inside of you know so one of the things that I'm
[1805.18 → 1809.78] looking at in the cities that we're working with is what actually happens to this code afterwards
[1809.78 → 1814.54] and the answer to that question can be a lot of different things you know Ezra could probably talk
[1814.54 → 1818.80] a little bit more about how New York does things, but you know you can imagine that for a city like
[1818.80 → 1824.76] New York I mean they have you know hundreds if not thousands of people that are working in it roles
[1824.76 → 1831.62] and working with databases like oracle and gigantic java based systems you know very classic kind of
[1831.62 → 1837.54] big ass it enterprise kind of stuff um so we're working with New York this year, but then we're also
[1837.54 → 1844.12] working with cities all the way down to the scale of like a South Bend um which is a tiny city with
[1844.12 → 1848.94] something like six people and their it staffs um, and yet they're still very, very interested in kind
[1848.94 → 1853.40] of taking the applications and work that we're doing and running with them uh so we're thinking
[1853.40 → 1857.76] about deployment environments as kind of combination of the technology of where you deploy
[1857.76 → 1861.30] to but then also the sort of political and social environment of where you deploy to
[1861.30 → 1866.54] and so what are what are some of the I guess hurdles you've been able to identify or
[1866.54 → 1872.44] look to overcome soon in your tenure as CTO yeah I think the biggest hurdle that we're
[1872.44 → 1878.52] staring down the barrel of right now is that the know 2013 is a very challenging budget
[1878.52 → 1883.44] environment for basically everyone in any kind of government anywhere in the world um you know i
[1883.44 → 1889.16] talk to some cities that have literally zero dollar training budgets for their it staffs
[1889.16 → 1893.98] I talk to other cities that have no it staffs whatsoever you know just sort of enthusiastic
[1893.98 → 1898.92] people that want to help but aren't really like properly staffed to do things um so I think the real
[1898.92 → 1905.06] challenge that we're thinking about is you know how do you transfer some of what we've seen in the
[1905.06 → 1911.32] open source and startup universes um where things have gotten kind of enormously cheap over the years
[1911.32 → 1917.52] with uh products like Heroku and ec2 and sort of you know push button data services and things like that
[1917.52 → 1922.14] and transfer those to a city environment where they're perhaps used to buying hardware
[1922.14 → 1927.80] and provisioning racked services, and you know paying a lot more money for things so really thinking about
[1927.80 → 1933.46] like you know how do you save these people money and get them a better type of technology deployment
[1933.46 → 1940.30] right if they're dealing with very, very challenging budget situations you mentioned budget there, and it's
[1940.30 → 1945.48] it kind of bleeds into the other topic we want to talk about too which is um the skill gap I guess for
[1945.48 → 1949.98] cities especially as you mentioned earlier like more modern tools like rails or python and you
[1949.98 → 1954.06] mentioned deployment environment that's both the human side and the technology side
[1954.06 → 1959.40] um you know what are you guys seeing in terms of and Ezra filter to chime in too on this but
[1959.40 → 1965.36] um just because you're probably more on the ground um talking to people but what is the skill
[1965.36 → 1971.30] gap problem for cities when it comes to more modern technologies that uh we like uh Andrew mentioned you see
[1971.30 → 1977.80] more of on GitHub these days or in open source that people are using and forking and modifying and
[1977.80 → 1982.34] changing rapidly versus older technologies and some of the more modern development tools what's the
[1982.34 → 1989.70] the gap happening there for cities well I think one of the challenges is that um when you're working for
[1989.70 → 1994.26] a government um I think oftentimes it's easy to become really risk-averse because you hear all these
[1994.26 → 1999.12] sort of stories in the news about government spending too much time working on something or spending too
[1999.12 → 2005.14] much money and um so when you're in that sort of environment you use what you know, and it's hard
[2005.14 → 2009.56] to blame anybody for doing that you don't want to you don't want to get in trouble so um I think a lot
[2009.56 → 2014.08] of times folks that have been in cities for a long time continue to use the things that they know really
[2014.08 → 2021.54] well and so that sort of maybe does not lend itself well to a more rapidly paced uh maybe open source
[2021.54 → 2028.88] based software environment because it just it takes longer for things to filter down um I think in many
[2028.88 → 2033.78] cases people are interested in open source tools but then they say you know who's going to
[2033.78 → 2039.14] support this who can I pay to support this application um after it's after it's deployed
[2039.14 → 2045.92] uh so maybe I wouldn't want to just install WordPress on my server I would want to you know hire someone
[2045.92 → 2051.02] to start and manage the servers that my WordPress instance is deployed on so it's just a little bit
[2051.02 → 2055.64] of a different mindset for one thing um but I think as Mike said before there just isn't a lot
[2055.64 → 2062.90] of budgets for capacity building and for training within it departments as well so it's an uh it's
[2062.90 → 2070.36] a tough it's a tough situation it is a tough situation I mean you've got to see though that um
[2070.36 → 2075.84] uh you know you mentioned the skill gap or nothing skill yet but that you mentioned that the lack of
[2075.84 → 2081.66] budget in some of these cities for training um I'd imagine that meetups might even be flooded with
[2081.66 → 2086.82] people maybe they just don't know where to go is it uh what do you see whenever you talk to
[2086.82 → 2091.52] some people in terms of um some of the newer technologies you're bringing in or that I mean
[2091.52 → 2099.44] is that mainly what code for America helps to establish is moving in more modern things or is it uh
[2099.44 → 2105.72] is it bringing in help that can even help revive some their legacy stuff you know it's got to be a
[2105.72 → 2111.92] combination because in the work the governments are doing their they're using they're doing work
[2111.92 → 2117.02] now, and we don't just want to build things that are going to be totally new that you know
[2117.02 → 2120.84] they're not going to be able to carry over their data from old systems or things like that so I think
[2120.84 → 2126.74] a lot of the sort of emphasis that we've put on are on more strategies than particular
[2126.74 → 2134.04] technologies, so things like open data things like APIs things like tools that help uh computer
[2134.04 → 2140.54] computer systems be a little bit more flexible uh let them work together uh and maybe not be so
[2140.54 → 2147.10] entrenched and static um we've seen an enormous growth in the idea of open data over the last few
[2147.10 → 2152.24] years and basically that's uh the idea that the data that government uses to run itself should be
[2152.24 → 2158.88] available to the public as well uh one of the sort of great examples of open data at work
[2158.88 → 2163.62] is you know these days when you open up your smartphone you go to a new city, and you open up
[2163.62 → 2170.28] Google Maps, and you say I want to go from the airport to my hotel and the phone will tell you
[2170.28 → 2174.54] exactly which bus to take or which train to take and when it's going to come it wasn't always that
[2174.54 → 2180.54] way it's not it's not hard to remember um up until you know a few years ago you had to go on to the
[2180.54 → 2185.88] local transit agency website look through some inscrutable uh timetable if you could even figure out
[2185.88 → 2192.86] which thing to take and um it was pretty difficult but uh a number of years back uh google
[2192.86 → 2198.60] and the transit agency in Portland where I'm from worked together to create a standard called TFS
[2198.60 → 2203.54] that's the general transit feed specification basically it says if you're a transit agency
[2203.54 → 2208.66] you run buses or trains, and you want uh people to be able to know what your schedules are just put
[2208.66 → 2213.62] your data put your schedules in this simple format and publish it online now all of a sudden
[2213.62 → 2219.74] hundreds of transit agencies are in uh Google Maps they're in uh you know in all these other
[2219.74 → 2224.28] applications that people have built to help you get to where you're trying to go, and so we're
[2224.28 → 2230.02] trying to help create more opportunities like this uh one area is in 311 so in New York city and San
[2230.02 → 2235.44] Francisco a lot of other cities you can call 311 to report a problem uh in your city maybe a broken
[2235.44 → 2241.88] street light or a pothole and um a number of different companies have started to build applications that use
[2241.88 → 2248.82] a consistent API uh and can let you know you report a 311 complaint uh from your smartphone without the
[2248.82 → 2253.24] city actually even building anything new at all so we're trying to find ways to help government
[2253.24 → 2259.50] be more like an API more like a platform this is sort of uh Tim o'Reilly's idea of government as a
[2259.50 → 2264.72] platform as I just did a search for TFS I didn't I didn't know that at all, but it seems like it's
[2264.72 → 2270.18] pretty simple data to that the at least the spec looks like it's comma like basically CSV
[2270.18 → 2276.72] you know it's an it's a simple specification but uh in uh
[2277.54 → 2284.42] you know but by more and more different agencies adopting that uh that specification
[2284.42 → 2290.32] becomes really powerful, and it doesn't necessarily even take a lot of work for the for a
[2290.32 → 2295.48] government or an agency to adopt the standard, but it takes sort of the network effect of that thing
[2295.48 → 2301.06] that that thing happening I think we're going to see more and more uh standards like that in um
[2301.06 → 2309.62] in January or February uh cook for America announced uh a standard called life uh that works with yelp and
[2309.62 → 2314.84] food inspection data here in San Francisco so before too long you'll be able to go on yelp and see whether
[2314.84 → 2321.18] the restaurant you're going to meet the food inspection last time they were inspected uh similar
[2321.18 → 2325.24] process is happening right now with housing inspection data so we're trying to be at the
[2325.24 → 2331.38] centre of bringing folks together to come up with these kinds of simple standards and you know you
[2331.38 → 2337.68] mentioned open data is a piece of this and I got uh i have to say that I was pretty excited about
[2337.68 → 2342.62] the traffic spike but also just the topic itself um back in March when we talked about the city of
[2342.62 → 2349.02] Chicago when they were uh they kind of splashed onto GitHub with uh five different data sets probably
[2349.02 → 2354.70] all stemming from the same spec that you're mentioning but um you know the impact it had but
[2354.70 → 2359.62] I thought it's kind of neat the way that they um you know some of the things they had said but one of
[2359.62 → 2365.28] the things they said that stood out the most to me was um when you want to improve our data just fork
[2365.28 → 2370.78] it I mean that's a term that we um I guess modern uh software developers have been enjoying for a while
[2370.78 → 2375.24] with GitHub and the past four or five years and what that's what that's done but I think it's just
[2375.24 → 2381.64] kind of neat to say that you know if you're passionate about uh you know open data for the city of Chicago
[2381.64 → 2388.62] and you want to make a change to some of the data just fork it we talk a lot about that at code for
[2388.62 → 2394.94] America with um uh our founder Jim Paula talks about community as capacity the idea being sort of that
[2394.94 → 2400.60] if uh I think you should mute your computer mike I think we're going to have two
[2400.60 → 2406.18] two streams in from our two computers so can you mute it yeah cool um
[2406.18 → 2412.20] there we go sorry about that that's okay we had some technical difficulties we got mike back in it's
[2412.20 → 2418.24] uh glad to have you back mike so um you know what's one of the things we talk a lot about
[2418.24 → 2423.70] with uh with code for America and sort of our approach is this idea of the community is the capacity
[2423.70 → 2431.10] in um in a lot of cities there aren't resources to you know immediately fix every pothole in the
[2431.10 → 2436.04] street, or you know clean up every corner all at once uh when things are when things are left
[2436.04 → 2440.96] out there but if we can help bring communities together and help citizens themselves be part of
[2440.96 → 2445.40] the process of making things better it helps create more ownership and helps us feel like we're part of
[2445.40 → 2449.84] the cities and counties we're living right um and if we can give people tools to do it in a way
[2449.84 → 2454.88] that's you know legal and right and help people do it the right way then people probably will
[2454.88 → 2459.94] because people care about the places they live and um developers have all these you know
[2459.94 → 2465.10] really particular skills that can help um in even more significant ways sometimes so we want to help
[2465.10 → 2470.80] make that possible yeah I mean just keying off of that it was actually um one of you all's projects
[2470.80 → 2479.00] to adopt a hydrant project that was uh fort and then Chicago turned that into shovels uh adopt a sidewalk
[2479.00 → 2482.64] and it was like you know rather than just stepping over the crack you know you can actually adopt
[2482.64 → 2487.22] that sidewalk and make an impact, and it's this code that kind of stemmed from the things that you all
[2487.22 → 2494.00] are doing to help cities take that ownership it's it kind of reminds me uh Andrew of something that
[2494.00 → 2499.94] we talked about at pure charity long ago which was um I went to this gala for living water here in
[2499.94 → 2505.12] Houston there's this non-profit called living water and when I went there part of what their mission is
[2505.12 → 2511.24] to go into various countries both here and abroad to help bring clean water into place and they
[2511.24 → 2515.94] found that um just going there and putting a well in place wasn't the solution it was going there and
[2515.94 → 2520.58] helping that community lift itself up and understand that they have to take care of the water they have
[2520.58 → 2525.58] to learn how to operate the well and it kind of seems like that's a similar thing in this
[2525.58 → 2533.72] case you know yeah definitely and I think um you know the adopt a hydrant app became adopt a
[2533.72 → 2538.70] shovel and in Hawaii it became adopt the siren they have tsunami alert sirens around the island
[2538.70 → 2544.76] and part of implementing that project it's a rails' app it's available on uh code for America's GitHub page
[2544.76 → 2551.46] uh was training up people in Honolulu about how to deploy rails applications um us fellows generally
[2551.46 → 2555.10] have those kinds of skills, and we're more than happy to share them with anyone who's interested so
[2555.10 → 2560.68] sometimes when there is an application that you know we're building for one purpose someone working
[2560.68 → 2565.20] for a different city or a different organization will see it and think hey I want that but I wish
[2565.20 → 2570.96] I could tweak it this little bit and um you know we think that's the power of open source and
[2570.96 → 2575.92] um we're trying to definitely facilitate that stuff to happen more often it's it kind of goes back to
[2575.92 → 2580.10] that what I mentioned earlier and I asked if is cities are collaborating with other cities, and it's
[2580.10 → 2586.62] this kind of that effect is like um you know Chicago sees what you all are doing with adopt a hydrant and
[2586.62 → 2591.58] then Honolulu sees that and they uh and Andrew that's pretty close to you because you just came
[2591.58 → 2598.86] back from uh vacation there um yeah, but you know just kind of seeing that um you know the
[2598.86 → 2605.10] mentality of forking code and in this case they fork the code base, but they apply it differently
[2605.10 → 2610.88] of adopt xyz and whatever that xyz is something new for that city it's that's really neat too to even
[2610.88 → 2616.68] see that and I'd imagine that the issues for those um those code bases are pretty filled with lots of
[2616.68 → 2622.48] collaboration as well yeah definitely I wanted to jump in the one of the projects that looks like
[2622.48 → 2628.50] it got pretty popular was Honolulu answers and looks like it's I mean it's obviously still going but
[2628.50 → 2634.40] um I think it's neat to see and I wanted to say this before you even uh mentioned that last thing but
[2634.40 → 2640.04] it's its cool because Honolulu answers kind of started to grow and is still growing and then Oakland
[2640.04 → 2644.40] uh forked in and is, and they're doing theirs and Salt Lake City forked in they're doing theirs so
[2644.40 → 2650.18] they're like you know figuring out how to do these like open source um you know forks of these different
[2650.18 → 2654.86] projects I think that's a really neat thing to see that happen that's a that's a good trend that
[2654.86 → 2659.52] I'd like to see continue in our country yeah, thank you that's actually one that we're uh
[2659.52 → 2665.38] particularly proud of um not just because it's gotten forked a couple of times uh but also because
[2665.38 → 2670.62] of the particular kind of social activity that that application engenders um you know the answers
[2670.62 → 2674.82] application basically allows the city to hold write-a-tons where people come in and answer
[2674.82 → 2680.06] questions very directly for the website of the city and so in the case of Oakland where I attended a
[2680.06 → 2685.40] write-a-then or Honolulu where I saw record records of the write-a-then uh what you saw was just
[2685.40 → 2689.62] regular people who actually knew things about the local city government coming together to
[2689.62 → 2693.18] you know talk about what kind of questions people might have of the city website
[2693.18 → 2698.18] and then actually do research and actually write responses to those questions right there at the
[2698.18 → 2703.42] write-a-then so it's built on the hackathon model but in a way that's completely accessible
[2703.42 → 2708.72] to regular people who don't have coding skills uh in the case of the Oakland one I think we attracted
[2708.72 → 2714.40] something like 50 or 60 people throughout the day um on a Saturday afternoon when we were holding
[2714.40 → 2719.40] the write-a-then together and a ton of stuff got answered yeah it's really cool I wish I would have
[2719.40 → 2723.96] I was just in Honolulu uh a few weeks ago would have been nice to have this when I was when I was
[2723.96 → 2731.90] there if I had known about it yeah I like this is that's pretty well I did want to ask
[2731.90 → 2736.38] you though because some of the projects I've been just kind of clicking through um a lot of the
[2736.38 → 2742.86] projects on the code for America uh GitHub page and uh i one thing I did notice was to adopt a hydrant
[2742.86 → 2748.08] uh Eric Michaels over still is committing to that to this day so that's pretty neat he had a pretty
[2748.08 → 2753.50] he had the most recent commit yeah he's he's an uh he's one of those guys that he's just like
[2753.50 → 2759.50] always coding all the time so it's like probably half of the repositories I look at on GitHub the
[2759.50 → 2766.12] most recent commit will be him so but uh no I mean so I've seen you know so I look at most of these
[2766.12 → 2772.48] uh repositories and the majority of them uh you know the the the ones I'm looking at now anyway
[2772.48 → 2776.08] closer to the top the ones that are just kind of seems like they're getting up and running uh the
[2776.08 → 2781.86] majority of the contributions are from what looks like to the team that's working on that city um
[2781.86 → 2790.54] how often do you attract just a non code for America fellow you know to come in and work on a project
[2790.54 → 2796.58] um directly uh without forking it for a specific city you know so for instance like Honolulu answers
[2796.58 → 2801.84] um it seems like it has a lot more contributors than some of the other projects so it would appear
[2801.84 → 2806.26] that maybe some developers that just have a heart for Honolulu or maybe some developers in Honolulu
[2806.26 → 2809.62] got wind of this and said hey I'm going to help out and how often does stuff like that happen
[2809.62 → 2815.86] well for the sort of primary fellowship projects um oftentimes those are sort of really sort of
[2815.86 → 2821.18] researched and run by the fellows themselves um and occasionally people will get pull requests
[2821.18 → 2826.04] and issues open and that's definitely happened a few times this year, but it doesn't happen all that
[2826.04 → 2829.60] often I think we'd love to sort of structure the products in a way that it could be a little bit
[2829.60 → 2833.34] more open to other contributions that people knew what to do but one of the one of the ways that
[2833.34 → 2837.38] people really can get involved and are really involved is with our brigade program
[2837.38 → 2842.72] um started up about a year ago we realized that in a lot of cities around the country
[2842.72 → 2847.24] you know there were sorts of communities coming together to build civic technology on their own
[2847.24 → 2852.56] we wanted to help them out so, and you know Oakland there was open Oakland and New York city there
[2852.56 → 2857.48] was the open NY forum and um now we help them out with what we call the code for America brigade
[2857.48 → 2864.54] which is a sort of community volunteer run group that lets just normal folks become civic hackers
[2864.54 → 2868.88] and we have them up and running in a bunch of different cities around the country all of our
[2868.88 → 2873.48] fellowship cities are sort of working on building them right now this is a way for just normal people
[2873.48 → 2878.36] to be engaged usually there's a know a hack night every week or two um sometimes it's a little
[2878.36 → 2883.74] bit more tech sometimes focused it's a little bit more sort of community organizing focused um and some
[2883.74 → 2887.98] of those organizations have their own GitHub open um a lot of times it's focused on
[2887.98 → 2893.58] redeploying and maintaining applications that come from other places this sort of civic tech community
[2893.58 → 2898.74] is a lot greater than just code for America though um we like to help people get together as much
[2898.74 → 2905.26] as we can and um the brigades are a really awesome way to get more people involved so you can check
[2905.26 → 2910.74] out more about brigades and see where we have them if you're just joining at brigade.codeforamerica.org
[2910.74 → 2915.98] we're also right now in the middle of a civic coding campaign uh the great American civic hack we're
[2915.98 → 2921.56] trying to get more coders involved with working on uh some specific repositories that we think could
[2921.56 → 2926.22] use a little bit of love so if you check out that website I just mentioned you'll see that there's a
[2926.22 → 2930.84] few a few different repositories that are ready for your contribution so if you see is you hear about
[2930.84 → 2936.26] this and want to get involved and maybe can't devote a year to be a member of the next year fellowship
[2936.26 → 2941.62] class it's a really great way to get involved you'd mentioned like the know like the local scene
[2941.62 → 2947.54] um just learning from uh the code for America Twitter account you guys just retweeted something
[2947.54 → 2954.98] from right here in my neck of the woods our mayor here in Houston um uh just announced an implementation
[2954.98 → 2961.40] of a city of Houston hackathon project it's kind of neat that just came up it's uh it's like budget
[2961.40 → 2966.86] boot camp I guess I just learned about this and a few months back we had this um this hackathon here
[2966.86 → 2971.92] and I was like wow this is really neat I missed it sadly because I didn't hear the news, but it's so
[2971.92 → 2977.58] wild to see these kinds of things actually being spawned by local city governments and then like you
[2977.58 → 2984.74] said Andrew just kind of getting the general Joe for lack of better terms or uh or Bette um
[2984.74 → 2991.90] involved in code and then also in civic hacking rather than just uh leveraging only the fellows
[2991.90 → 3000.46] yeah I wanted to ask the project here and i just kind of found this little uh I could run down this
[3000.46 → 3006.62] little monkey I don't know what I'm rabbit trail gosh I'm losing my words here um so blight status
[3006.62 → 3013.22] uh looks like it started in code for America and it, and it got popular with New Orleans and um they
[3013.22 → 3017.38] started a whole company civic industries, and then they're kind of taking this project and expanding
[3017.38 → 3023.08] it into something even more uh is that a trend that you would like to see continue or can you talk
[3023.08 → 3028.68] about you know the ongoing relationship you'll have with the three I imagine the three people that
[3028.68 → 3035.00] are starting civic industries were fellows so uh yeah all three of them were fellows last year
[3035.00 → 3040.10] working on the New Orleans team project and um they're all still here in the office I think they're
[3040.10 → 3044.54] actually finishing up their incubation period pretty soon, but they were one of three startups
[3044.54 → 3050.70] local data and textile or two others from that year uh that were kind of the founding members of
[3050.70 → 3055.10] the incubation initiative that we have where we essentially take what looked like really promising
[3055.10 → 3061.32] applications from the fellows um and turn them into full companies with a little bit of funding and
[3061.32 → 3068.08] runway so you are actually okay so you're you're almost like you said an incubator so you're actually
[3068.08 → 3073.00] watching these and helping them grow uh which is cool then that so that's a way that you can kind
[3073.00 → 3078.38] of you know the fellowship program's really neat and I think it gives the people a good um
[3078.38 → 3084.78] the people you know the fellows like Ezra a good uh you know base but I think that to allow them and
[3084.78 → 3089.18] to help enable them to continue on is kind of a's even a greater calling you know that's just yeah
[3089.18 → 3094.28] exactly I mean the fellowship is you know it's just the one year, and it's really important and
[3094.28 → 3098.32] increasingly important over the years that the fellows that come, and you know give their time
[3098.32 → 3103.54] and work with us for that year have some very concrete new things that they can do and new
[3103.54 → 3107.74] contacts that they can make as a result of their time here uh so we're really interested in figuring
[3107.74 → 3113.86] out you know what kind of companies they move on to what kind of companies they create uh and you
[3113.86 → 3118.16] know with luck government becomes something that's actually attractive to all the different fellows that
[3118.16 → 3121.02] come through here so we're really hoping to see more people go into government proper
[3121.02 → 3126.76] how do you split the teams up like when fellows come in you, you obviously don't want to end up
[3126.76 → 3131.66] with a team of three designers, or you know three data monkeys so how do you kind of split the teams up
[3131.66 → 3139.80] when it happens I think it's a mysterious process involving uh a bulletin board and uh darts but
[3139.80 → 3146.48] no uh we're all sort of uh as fellows we're given a chance to say what we're interested in um
[3146.48 → 3150.96] where we're interested in working and what kinds of skills we have and then the staff sort of
[3150.96 → 3157.62] goes into a room and tries to take our preferences into account and build teams that have a good
[3157.62 → 3163.90] variety of skills on them so uh it was a little bit interesting coming in without knowing the people
[3163.90 → 3169.10] I was going to be working with, but it's worked out pretty well yeah what comes first the fellows or the
[3169.10 → 3175.04] cities well I think we you know it's one of those situations where we all have to be able to
[3175.04 → 3180.50] to get the work get the work done in terms of selection uh right now we're in the process of
[3180.50 → 3184.78] choosing the cities for next year and the fellowship class the fellowship application
[3184.78 → 3189.08] deadline is at the end of the month so we'll start reviewing them later this summer both will be
[3189.08 → 3195.12] announced uh later the fall well and the reason I ask is um you know i I know that you know and in
[3195.12 → 3200.12] my circle of friends I know a lot of people that have hearts for specific cities right whether it's
[3200.12 → 3204.48] where your grandparents are from where you're from you know whatever the reason is and so
[3204.48 → 3210.00] would you be able to let's say you know you get elected into the fellowship program and for all of our
[3210.00 → 3215.66] listeners out there that have an interest in maybe an uh just kind of wavering through life you know
[3215.66 → 3220.24] highly recommend looking into this but if you get into the fellowship program, and then you say hey i
[3220.24 → 3225.52] would really like to work with this city if that city is available uh is that kind of stuff taken
[3225.52 → 3230.54] into account at all it's definitely taken into account but I don't think unfortunately they can
[3230.54 → 3235.38] make any promises so keep that in mind if you only want to be in one place uh it's difficult
[3235.38 → 3240.34] the truth is a lot of the folks the average age of code for beckon fellows this year is I believe
[3240.34 → 3245.40] 30 um maybe even a little bit older than that we have folks who are sort of new to tech people who've
[3245.40 → 3251.46] been around for a long time people coming from big companies like Cisco and google and yahoo and
[3251.46 → 3257.40] places like that so you know we have folks with a incredible breadth and depth of
[3257.40 → 3263.36] experiences and a lot of folks you know are taking a huge pay cut to come here this year we get paid
[3263.36 → 3267.10] thirty-five thousand dollars which for you know a lot of people in the tech industry doesn't sound
[3267.10 → 3271.58] like a lot, but people are here because they are really carry they care a lot about what they're
[3271.58 → 3276.40] doing, and they're passionate so um you know we're really trying to bring in people who have a lot to
[3276.40 → 3283.54] offer yeah and I mean and so how many of the uh fellows do you get that are working in
[3283.54 → 3288.18] another job and you know maybe deciding hey this is something that i just really have a passion for
[3288.18 → 3292.18] and then how many of the applications are you know people that come out of college that have no idea
[3292.18 → 3296.46] where to start and are just trying to figure out how to get started I don't think there's anybody
[3296.46 → 3301.34] this year who's coming straight out of college everybody's worked uh has some significant
[3301.34 → 3307.20] experience uh or expertise that they're bringing to the table uh we have a PhD anthropologist who's
[3307.20 → 3313.44] helping with user research we have uh folks who've worked in health care policy research and data
[3313.44 → 3317.50] analytics and all kinds of different fields so maybe they're not uh maybe they're not too experienced
[3317.50 → 3322.46] on the tech side or on the startup side but uh they everybody comes in with something
[3322.46 → 3327.54] that's not to say if you are coming straight from college you don't have something to bring
[3327.54 → 3332.14] um definitely encourage you to apply if you have questions you can ask about whether you're
[3332.14 → 3337.00] you're qualified but we're looking for folks with a big passion and a big capacity to learn
[3337.00 → 3343.06] that's always good it's always a good need right there to learn that's certainly bridging that skill
[3343.06 → 3348.64] gap piece they're just bringing either learning on the job or for lack of better terms or helping
[3348.64 → 3353.88] educate those that are in cities that are using less modern things that would benefit from more
[3353.88 → 3360.16] modern things you know as one thing that was um uh that mike and I talked about briefly when we
[3360.16 → 3367.90] did sound check earlier um was just kind of going back to Chicago and their open uh their open data
[3367.90 → 3374.18] initiative that they kind of spawned back in March, and you're there in New York um mike mentioned you
[3374.18 → 3378.40] had some interesting things with what you have planned for New York can you share that
[3378.40 → 3384.82] with us yeah I think um New York is a really awesome place to be working on open data because
[3384.82 → 3390.32] about a year ago a year and a half ago or so they passed a law that says that all of their government
[3390.32 → 3397.68] data has to be open and so you can go online right now to nyc.gov slash data and there are
[3397.68 → 3404.64] thousands of different data sets everything from 311 calls to GIS locations of subway entrances to
[3404.64 → 3410.34] all the different trees that they have uh kept track of all over the city, and you can build apps
[3410.34 → 3414.20] on top of them right now it's just open to the public I think what you're going to see over the
[3414.20 → 3420.18] next few months is more and more data sets coming from more and more agencies that you know just
[3420.18 → 3425.36] developers or anybody is going to be able to use for all kinds of different purposes um New York is
[3425.36 → 3430.86] not the only place that's happening Chicago's done a lot of work Seattle San Francisco a lot of cities
[3430.86 → 3436.14] are starting to create these open data portals and creating laws that that make the government
[3436.14 → 3443.16] release this data so it's a really exciting time if you're interested in building applications or using
[3443.16 → 3449.10] civic data uh and I really encourage anybody who's interested just to go with their local city website
[3449.10 → 3455.54] and take a look there's also work happening nationally at data.gov and most many states I know
[3455.54 → 3461.08] Maryland's doing a really great job and other states uh New York state that have all kinds
[3461.08 → 3467.14] of data sets open what about Texas I don't know off the top of my head, but we do have a fellow from
[3467.14 → 3473.14] San Antonio so awesome yeah I'm an obviously I'm a huge fan of Texas and Austin was one of our cities
[3473.14 → 3478.92] last year yeah Texas is usually so good at government though so I figured they'd be like
[3478.92 → 3486.90] they'd be the Chicago you know bummer the Chicago of states yeah well the Chicago in terms of uh
[3486.90 → 3491.26] leading the way I mean they did a really cool thing with I mean we had gotten such a huge traffic
[3491.26 → 3496.16] spike that day I don't know if it was um and I think that's what's fascinating about
[3496.16 → 3501.46] this I think it's a different side of obviously the government and things that we as citizens are
[3501.46 → 3505.78] able to interface with we've you know we don't have lack of power we just have lack of knowledge
[3505.78 → 3510.60] and this open data starts to give us knowledge to either you know make our cities better by doing
[3510.60 → 3516.06] maps, or you know just doing unique cool things with that data I mean you just never know
[3516.06 → 3521.44] and I think that's um it's something I wouldn't mind doing that's why I'm kind of bummed I missed
[3521.44 → 3527.86] Houston's hackathon that was back in May so I'm excited to see the next one and get involved but
[3527.86 → 3533.98] um Andrew we got some cool questions we always ask what uh what are those questions yeah so I mean
[3533.98 → 3538.60] I feel like we could talk about this stuff forever but at some point we have to we have to stop it but
[3538.60 → 3544.68] uh the questions yeah that for the sake of uh people driving home from work the questions uh that we'd like
[3544.68 → 3549.84] to ask and if you are a listener to the changelog you are ready for this if not we're going to ask these
[3549.84 → 3555.72] uh two questions at the end of every show and seeing as we have two uh people on there with us, I will
[3555.72 → 3563.80] let you both answer so it's your lucky day um, but our first question is for a kind of call to arms so
[3563.80 → 3570.50] uh in the projects you're working on or maybe any other projects that code for America you know has worked
[3570.50 → 3576.22] on or just anything what would you like to see the open source community get involved with and help out with
[3576.22 → 3577.72] and I guess I'll ask you first Michael
[3577.72 → 3583.84] sure yeah I think that uh really what we're looking for is help and participation from the open source community
[3583.84 → 3588.00] uh we're trying to improve all the different readies and documentation around our applications
[3588.00 → 3593.76] so if you go to GitHub.com slash code for America take a look there and see if there are any issues you
[3593.76 → 3599.80] can squash or stuff you can help with um another place to look is brigade.codeforamerica.org
[3599.80 → 3605.42] brigade is sort of a wider ranging much larger program that we run with people that are local to
[3605.42 → 3610.44] something like I want to say 25 or maybe even more cities around the U.S. so take a look at brigade and
[3610.44 → 3618.10] see if there's a group near you what about you Ezra anything specific or I would say uh if you're
[3618.10 → 3621.90] interested apply for a code for America fellowship it's been a really awesome opportunity to move to
[3621.90 → 3627.68] San Francisco meet awesome people Tim o'Reilly's around really frequently Eric Reese came and talked
[3627.68 → 3632.64] to us, we get to work with some really amazing government officials all over the country it's a
[3632.64 → 3638.26] pretty good opportunity if you're interested in tech cities' urbanism any of the sort of city-like
[3638.26 → 3644.80] stuff so code for america.org slash apply and applications are uh being accepted through
[3644.80 → 3650.30] 731 I was going to say 731 was so that's that's another reason why I wanted to get you guys on
[3650.30 → 3654.96] the show pretty quickly I know we kind of expedited your we would have we would have had you on the
[3654.96 → 3660.92] show no matter what but uh definitely that timeline was what uh wanted me to get you on um because we
[3660.92 → 3664.78] haven't mentioned yet, but we're gonna not have a show next week Andrew and I are both travelling up to
[3664.78 → 3671.16] our uh our day jobs uh home office so we'll be there doing some hacking ourselves but
[3671.16 → 3676.02] um wanted to get you guys on before that so that we can hope to spike the interest and hope
[3676.02 → 3681.80] um that this peaks some applications coming in so the deadline is July 31st right so the end of this
[3681.80 → 3686.24] month that's right awesome let's start doing it now yeah don't wait till the 30th that's right
[3686.24 → 3692.62] that's right the second question we ask is for a programming hero so somebody that has been
[3692.62 → 3697.38] influential and I'll even let you guys answer a civic hero if you would like, but we typically ask
[3697.38 → 3703.30] for a programming hero so Michael what do you get for sure so my programming hero is Guido van room
[3703.30 → 3708.38] the creator of the python programming language um he's my programming hero both because he's pretty
[3708.38 → 3714.12] awesome at what he does and also because I think I've I've just seen him exercise so many moments of
[3714.12 → 3719.84] admirable restraint in designing the language where it's been created to be this extremely easy to use
[3719.84 → 3727.32] beautiful extensible thing interestingly uh Kenneth writes who is one of our uh frequent co-hosts on
[3727.32 → 3735.76] the show he also said that the bdfl is his programming hero and what about you Ezra
[3735.76 → 3741.36] well I've had a luck to have a bunch of different really awesome mentors and a lot of
[3741.36 → 3744.80] people I really admire so I'm going to go a little bit of a different direction I'm going to choose
[3744.80 → 3749.86] my friend lily who I know from college, and she didn't study computer science or do anything
[3749.86 → 3756.22] particularly techie but since moving out to San Francisco uh she started working in a startup on
[3756.22 → 3761.32] the support role, and she's really spent a ton of time diving straight into learning web development
[3761.32 → 3767.96] she's at dev boot camp right now, and it's really inspired to see how she's um put so much effort and
[3767.96 → 3772.88] energy into learning the skill and more than that she's an active member of a great organization
[3772.88 → 3778.78] here in town called rails bridge which does uh free training programs for people who want to learn
[3778.78 → 3784.46] web development and Ruby on Rails particularly women who as we know are not um as common in our
[3784.46 → 3790.42] industry as they are in the rest of the world so um she's just been doing really great work learning
[3790.42 → 3794.82] and sharing and I just think it's an it's a great uh standard for us to all work towards
[3794.82 → 3799.76] yeah one of our uh co-workers at pure charity Beverly, and we've talked about her a few times she's uh
[3799.76 → 3805.70] she's involved with rails bridge that's a very cool uh movement that we're seeing uh happen so
[3805.70 → 3811.84] totally yeah Beverly is also a fellow change lawyer she hasn't written on this subject yet but I've been
[3811.84 → 3816.26] asking her to talk about uh some of the things they've got going on at her chapter of rails bridges
[3816.26 → 3820.74] because she does the leading and I think she's actually the national leader isn't she Andrew isn't
[3820.74 → 3827.16] she or she's on the board or yeah she's she's uh she's a such a great teacher, and she always has a
[3827.16 → 3833.16] heart for helping people learn so definitely big fans of rails bridge so uh as there make sure you
[3833.16 → 3838.04] get me a link to anywhere I can find lily or help me with her last name so I can make sure we link her
[3838.04 → 3844.72] up in the show notes will do all right well gentlemen thank you so much for uh for joining us on the show
[3844.72 → 3850.08] this has been episode number 95 you can find this show at five by five dot TV slash change log
[3850.08 → 3855.36] slash 95 show notes will be there as well we'll link everything up but uh mike and Ezra thank you
[3855.36 → 3862.72] so much for taking time out of your day to share this um this fun topic of civic hacking and the
[3862.72 → 3868.44] efforts that uh both you guys are doing at code for America and say hello to all the fellows and good
[3868.44 → 3874.32] luck on getting some really awesome uh new fellows in for your program for this year but uh we'll be back
[3874.32 → 3878.64] uh not next week but the week after for another live show every Tuesday at five
[3878.64 → 3885.64] here on five by five so let's say goodbye awesome thank you Adam thank you Andrew thanks so much great
[3885.64 → 3886.44] chatting with you guys
[3886.44 → 3899.08] you
