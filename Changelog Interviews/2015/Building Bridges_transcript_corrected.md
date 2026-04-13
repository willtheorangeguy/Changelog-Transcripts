[0.00 → 17.18] welcome back everyone this is the changelog and I'm your host Adam stankowiak this is episode 157
[17.18 → 23.02] and on today's show we're joined by a special guest host Beverly nelson you've seen Beverly
[23.02 → 29.90] around the blog she has done some awesome stuff in the learning section a more recent article for
[29.90 → 36.28] her is get resources for visual learners if you haven't seen that post check the show notes for it
[36.28 → 43.48] we're also joined by Sarah Allen Sarah is most known for her work to diversify ruby with rails
[43.48 → 49.98] bridge she co-founded that in 2009 and also bridge foundry, but we dive deep into Sarah's history of
[49.98 → 56.30] programming such wealth of knowledge loved having Sarah on the show we have three awesome sponsors
[56.30 → 64.06] for the show code ship top tout and digital ocean code ship is our first sponsor very hosted
[64.06 → 71.00] continuous delivery service focusing on speed security and customizability it's all about
[71.00 → 77.16] helping you and your team focus on your code while automating your delivery workflows you can set up
[77.16 → 82.70] continuous integration in a matter of seconds and automatically deploy your code when your tests
[82.70 → 87.50] have passed code ship supports your GitHub and your bet bucket projects so no worries there
[87.50 → 92.64] you can get started today with code ships free plan should you decide to go with a premium plan
[92.64 → 99.14] you can save 20 off any plan you choose for three months by using this code the change law podcast
[99.14 → 105.46] use that code and get 20 off any plan you choose for three months head to code ship.com
[105.46 → 109.64] slash the change law to get started tell them we sent you and now on to the show
[109.64 → 118.34] hey everybody Adam here from the change log I'm joined today by Sarah Allen and Beverly nelson
[118.34 → 124.86] Sarah you uh been lining up this call for a while Beverly you helped line it up uh just some quick
[124.86 → 131.90] introductions from my side Beverly you work on the uh change log team writing and now being on the
[131.90 → 138.80] podcast and Sarah you uh and Beverly work together outside this stuff actually in uh with your
[138.80 → 144.32] with the with bridge founder something you founded to help uh move tech learning move
[144.32 → 151.12] forward uh so welcome to the show thank you it's great to be here and I guess Sarah let's start with
[151.12 → 155.26] you with some quick introductions so for those who may not know who you are how do you introduce yourself
[155.26 → 161.18] well I've been in the software industry for over 20 years most of the time as an individual
[161.18 → 168.38] contributor developer um also as a technical leader and um early in my career I did a little bit of UI
[168.38 → 176.88] design and now i um lead a product team um working for the United States federal government at a group
[176.88 → 183.96] called 18f I have to say that I do not speak for the federal government and um with that disclaimer
[183.96 → 193.22] I'm speaking in my personal capacity um uh I am a leader of bridge foundry the leader of bridge
[193.22 → 198.40] foundry which is an organization that started out as rails bridge which I co-founded with Sarah may
[198.40 → 206.58] um and the open workshops project and um and then a few years ago we refactored the organization
[206.58 → 213.24] and created bridge foundry which is dedicated to all the different technologies and um
[213.24 → 220.92] in my other hat that I wear is I have a startup company that I work on the side called mighty verse
[220.92 → 228.58] so many things wow lots of things the serial innovator is what I read somewhere about you is that uh
[228.58 → 234.48] seems to be true right yeah that's the name I came up with because um people always call themselves
[234.48 → 241.78] serial entrepreneurs and I like making things, and sometimes they're companies, and sometimes they're
[241.78 → 247.94] open source projects, or sometimes they're other things and uh so Beverly you helped line up this
[247.94 → 253.86] call uh good friends with Sarah work with her with uh with bridge foundry we work together at pure
[253.86 → 259.56] charity so that's that's obviously uh nothing that's hidden you've worked with uh me on the change log
[259.56 → 265.90] one of your posts recently was a very big post get resources for visual learners you love teaching so
[265.90 → 272.26] I don't know if I did your intro for you, but it could be to a degree that sums it up I would say
[272.26 → 277.16] definitely I'm a ruby developer and I just have a tremendous passion for learning and making
[277.16 → 282.84] information accessible especially for those who may be in an area that's not diverse enough to have
[282.84 → 287.96] technology easily accessible and so it's a personal gain of my personal mission just to really expose
[287.96 → 290.90] that to as many people as possible and give them the opportunities that I was given
[290.90 → 301.16] so I feel like this call isn't exactly um isn't exactly just about you know your efforts collectively
[301.16 → 307.08] the two of you together around diversity not so much just for women but also for all walks of life
[307.08 → 312.24] all races of life uh the under the underrepresented but also about the work you're doing an open
[312.24 → 318.88] source and Sarah I'm really interested about uh about your history um in software development you've
[318.88 → 324.22] been around for a while I'm not saying you're old I'm 36 but I've got some history, and you've got
[324.22 → 328.50] some history so I'm really curious to like to go back in you're past a bit can we go back in your past to
[328.50 → 335.04] maybe um you know some fun times I guess when did this all begin for you well I started programming
[335.04 → 342.92] when I was 12 oh okay um my mom brought home an apple 2 um she'd been laid off from teaching
[342.92 → 349.76] and decided that she was going to sell computers which is a huge departure from for her and um she
[349.76 → 355.12] really wanted to learn about them and I was very lucky that I had school off the day after it arrived
[355.12 → 362.86] and at that time um apple 2's came with a manual that told you how to kind of open it and get started
[362.86 → 368.90] and then it came up with a second book that taught you basic so I just walked went through the book and
[368.90 → 374.86] typed stuff into the command line and learned how to make the computer do things and I think it's a
[374.86 → 383.06] very sad thing that nowadays it's very inaccessible to get started coding I think it's a great thing that
[383.06 → 387.66] computers are more accessible for people who don't want to code, but now you have to install all this
[387.66 → 394.26] stuff onto your computer just to write code and I think that's pretty unfortunate yeah I guess so
[394.26 → 400.60] what's the I guess the kind of marrying that against the setup to develop ruby I guess on a Mac is
[400.60 → 407.60] that what you mean yeah I mean anything you know if you we have these graphical user experiences and
[407.60 → 419.22] um you have to install special editions to get to the terminal on a Mac um, and often it's just hard to
[419.22 → 425.90] get started in the early days of apple and Macintosh there were things like hyper card you know there
[425.90 → 432.12] was um there was basic there were all these things that were built in that allowed um people to kind
[432.12 → 439.98] of access the underbelly of the machine or do a little hacking in a friendly way and that um value
[439.98 → 448.84] system of really allowing people to modify and change and invent things with computers seems to be
[448.84 → 458.90] um a less accessible than it was you know in the early days so I guess you have a pretty awesome
[458.90 → 467.02] handle right ultrasounds, and you've even gone as far on your site to explain uh what an ultrasounds is
[467.02 → 472.48] but for those who don't want to go to that URL and read your awesome copy about what an ultrasounds
[472.48 → 478.82] is which I totally enjoyed uh what is an ultrasounds can you tell us now um it's an um very large
[478.84 → 485.16] dinosaur so I did I'm not sure that I was um I didn't give it a lot of forethought when I came
[485.16 → 490.94] up with this handle because i I'm not sure that I should have picked being a very large dinosaur when
[490.94 → 499.40] it comes to working in tech um because there are biases against people who are older but uh I did uh
[499.40 → 507.82] i when i first um I needed to have a domain name that was unique and I had a son was four and a half
[507.82 → 513.46] years old at the time and going through this major dinosaur phase and the ultrasounds I had recently
[513.46 → 521.78] learned about so um I picked that as a domain name and then I was experimenting with a bunch of
[521.78 → 527.60] what are now called social networks but at the day we know sort of called themselves you know sort
[527.60 → 533.22] of consumer computer assisted collaborative work I think was what people called it or something like
[533.22 → 539.18] that, and so I would need Sarah is a common name and Sarah Allen actually is a common name so
[539.18 → 545.10] I would put ultrasounds as the name for all these different things that I was experimenting with
[545.10 → 553.24] um realizing only later that that would then become my actual name on the internet it's crazy though right
[553.24 → 558.04] like it, I guess I'm going to say back in the day because I chose the same thing back in the day
[558.04 → 563.52] I was adamstack.com I never was my full name because my last name is nine letters and as soon
[563.52 → 568.96] as you see nine letters you're like uh I can't pronounce your name so I was just Adam stacks and
[568.96 → 575.80] so you know your kind of choose your handle to a degree um but nowadays, it's a bit more explicit right
[575.80 → 582.36] when you join the web basically social anything anytime you make a presence on the web you're asked
[582.36 → 588.14] what is your username and so sometimes people have several uh sometimes people have aliases because
[588.14 → 593.64] they're they're like catfish or whatever um but some of us are pretty explicit about who we are we and
[593.64 → 600.00] we kind of state that out there so you sort of did it accidentally to a degree yeah and then and now of
[600.00 → 606.02] course it's um it's very convenient because as long as I'm relatively early in this whatever it is
[606.02 → 614.26] usually allosaurus is a unique name so let's talk a bit about uh I guess past the apple 2 past basic
[614.26 → 619.90] at what point did it become real for you, you know like you're a kid you were 12 but at what point
[619.90 → 625.80] were you like i I want to do this for a living I like this stuff I could do something with it at what
[625.80 → 631.68] point did that happen for you, it wasn't until after I graduated from college I'd actually gotten a
[631.68 → 638.64] computer science degree and co-founded a company before I decided that this was actually what i
[638.64 → 648.46] wanted to do how's that happen well i um I went to Brown University and I was kind of really interested
[648.46 → 654.88] in studying language but I ended up wanting to get a visual arts degree and I was really interested in
[654.88 → 660.90] studio art but I didn't think that that was um if I was paying all this money for college I should do
[660.90 → 666.08] something practical so I did I studied computer science as a backup um because I figured I could
[666.08 → 674.02] always get a job programming and um and then I decided not to do art full-time because I wanted
[674.02 → 681.60] not to compromise my art um and I had this theory that if I was a programmer by day that I would have
[681.60 → 688.26] time to do art um which I did probably for one year of my career but as um I think we all know it can
[688.26 → 696.62] be a little all-consuming to be a programmer yes so i um a bunch of my friends um who graduated a half
[696.62 → 701.14] a year before me were starting this company we called the company of science and art which was a
[701.14 → 710.66] very good fit for me and i um I joined the know the founding team of this company and still you
[710.66 → 714.90] know we were building software but I didn't think that this was what I was going to do with my life
[714.90 → 724.24] and then um it was only I was answering a tech support call and um because we all took turns
[724.24 → 728.22] you know playing tech support um there were only eight of us at the company and this was probably
[728.22 → 736.84] like a year later and um there somebody had bought our software and had a question about like what it
[736.84 → 742.10] could do and I had helped write the manual I was very proud of myself and I said oh you just turn to
[742.10 → 751.42] page 34, and you can see right there that it does whatever and um the guy said wow I didn't know
[751.42 → 759.20] computers could do that, and he said I just bought this software as a lark um I thought maybe it would
[759.20 → 767.60] be helpful but I was not convinced that this was even possible and I was really struck by that because
[767.60 → 774.94] it was something like um you know our software you could then it would do um audio and like
[774.94 → 783.40] synchronized graphics and audio off um CD-ROM and this was like connecting um something like
[783.40 → 793.96] macro mine director to play our um audio and video triggered from something mechanical so nowadays like
[793.96 → 798.50] that's mom and apple pie everybody realizes that you know the internet of things you can connect
[798.50 → 808.34] things and sensors to computers but um even then I knew that that was possible it never occurred to me
[808.34 → 814.72] that there was anybody who was literate who would have a computer who would not realize that this was
[814.72 → 821.60] possible right that just maybe it was you know took a bunch of work to make it to make the connections
[821.60 → 827.84] happen, and maybe it wasn't practical like maybe it wasn't worth the expense of doing it, but it was
[827.84 → 835.52] certainly possible and that there was somebody who thought that maybe it wasn't possible and then i
[835.52 → 843.58] thought of all the things that I can think of that I know are possible like i just know it
[843.58 → 850.26] because of all the things that I now and then I can imagine these things that other people can't
[850.26 → 856.50] imagine because they don't think they're possible blows your mind yeah so I just started at a
[856.50 → 863.38] relatively young age thinking about all the things that I knew were possible that other people could
[863.38 → 869.20] maybe they didn't have access to those like even those ideas, and maybe it was my responsibility
[869.20 → 876.50] or opportunity to make some of those things and we just um we ship a weekly email called change
[876.50 → 881.64] all weekly and this isn't a plug for that, but it's awesome you should sign up for it um we just
[881.64 → 888.96] shipped this latest issue and I'm going to it right now because um I was really excited to put this
[888.96 → 895.22] this one post in their in particular, and it was about is coding the new literacy and that's actually
[895.22 → 900.52] the one it was uh it was actually that's actually the title of it, and it was a mother Jones uh post but
[900.52 → 904.98] it was from back in the day and I'm glad they didn't have it time stamped well enough so that when
[904.98 → 910.20] people get there you can like to judge it based on its date uh because it was such a great article about
[910.20 → 917.04] how you know I think what you're talking about and correct me if I'm wrong but being that code
[917.04 → 923.24] is a new literacy when you understand how the phone in your pocket works, and you can make something for
[923.24 → 932.22] it is like it changes your life because you could never do that before right and even further back you
[932.22 → 937.68] couldn't even imagine that something could do you know the aha moment where you're mentioning where
[937.68 → 942.40] you're on that customer service call like how could you not know that's possible I know it's possible
[942.40 → 946.64] why can't you know it's possible, and it's just it's so mind-blowing to see the gap there between
[946.64 → 953.08] those who know what's possible and those who don't and the literacy gap in between and look how close
[953.08 → 958.36] Sarah came to not having that at all you know what if her mom didn't start selling computers what if
[958.36 → 962.48] she had decided not to go ahead and go forward with programming you know those things and even
[962.48 → 966.82] for me, I had a similar circumstance where I was introduced to programming at a very young age
[966.82 → 971.36] and I think back that was a catalyst moment for me what if that had never been shown to me would
[971.36 → 975.38] I've been a completely different person, and it's turned out to be you know absolutely essential and
[975.38 → 979.52] something that I enjoy so much and enjoy sharing with others, but it was because somebody exposed it to
[979.52 → 983.86] me and let me see what programming was all about and let me see the chances of being able to
[983.86 → 989.88] create and so definitely having that opportunity I hate that it was a chance for many people in the
[989.88 → 998.22] past and I think there's a real uh initiative to change that yeah I agree I think that um I think
[998.22 → 1003.70] everybody should learn to code for the same reasons that I think everybody should understand photosynthesis
[1003.70 → 1010.98] you know like it's not like I use this in my daily life like I don't really use chemistry or
[1010.98 → 1017.32] um maybe i you could argue that I use physics because you know gravity makes a difference in
[1017.32 → 1023.82] my life but um there are so many things that I learned in grade school that just helped me make decisions
[1023.82 → 1029.50] about the world you know they helped me understand global warming, and they helped me understand
[1029.50 → 1036.10] why you know I think I should pay taxes for certain things that you know protect our, and you know that
[1036.10 → 1042.74] I think there should be laws that protect our environment and um it may help me reason about
[1042.74 → 1048.42] the world and I think coding is like one of those things I don't think everybody needs to be a software
[1048.42 → 1055.08] developer but everybody right yes should be able to have these tools right that's what I tell so many
[1055.08 → 1062.30] people too I meet people who are very you know either one intellectual naturally or educated and I'm like
[1062.30 → 1066.78] you would be a really awesome programmer I could just tell based on how you think, and it's not so
[1066.78 → 1071.52] much that hey you should go and program for a living, but it'd be kind of neat to sit down and learn
[1071.52 → 1079.08] HTML CSS and JavaScript as a start potentially and just like understand like you said before what's
[1079.08 → 1083.66] possible you know I think that people don't really grasp that and I wish more people got it
[1083.66 → 1092.38] yeah I agree I also think that um it I do I like you sometimes I meet people, and you can kind of see
[1092.38 → 1096.86] how their brain works, and you're like wow I have an instinct that you'd be good at this and like it
[1096.86 → 1105.12] but I also think that it's really hard to tell who's going to be good at programming based on other
[1105.12 → 1111.16] characteristics I have this theory that if you took a hundred people that there would always be a
[1111.16 → 1118.30] certain percentage of them who are good at coding like I don't know whether it's 20 or 50 or 80
[1118.30 → 1126.24] but it's not a hundred percent like and I think it has a lot to do with how whether people love it
[1126.24 → 1132.96] um there's like this crazy gratification that some of us get when you're like wow it works oh my gosh
[1132.96 → 1140.72] it's like magic and not everybody has that amazing thrill when it works um but I think there's some
[1140.72 → 1146.86] percentage of people right for whom they have that it's exciting its fun there it like clicks
[1146.86 → 1152.26] through your brain in a certain way and it has nothing to do with whether you're good at math
[1152.26 → 1158.64] it has nothing to do with any particular attribute that I've ever been able to see it's just that some
[1158.64 → 1167.88] people love it and have that like special spark of this is what they know it all makes sense to
[1167.88 → 1176.18] them and you know and I think that so many people are just not even exposed to it that you would just
[1176.18 → 1182.12] never know it and that's what's so fun about these work weekend workshops we do that people learn it and
[1182.12 → 1186.32] some people they just end up like okay well I have this skill that I didn't have before and that's good
[1186.32 → 1193.44] um and then other people it changes their whole world I'm going to take a break here in a minute or so
[1193.44 → 1199.44] to cover a sponsor, but before we do that I want to ask you one question and then dive deep into
[1199.44 → 1205.20] what you're doing at bridge foundry and the question is since you mentioned it uh the love
[1205.20 → 1210.54] moment with programming at what point can you remember when did you fall in love with it, and you're
[1210.54 → 1214.66] like I'm never leaving this is my thing this is what I'm doing what was that moment for you
[1214.66 → 1223.34] well I think it's interesting because I always loved doing it but I didn't value it and I think
[1223.34 → 1230.52] that um I always felt when I was um a kid and programming that it was like doing a crossword
[1230.52 → 1235.92] puzzle or like those I used to always love those blacksmith puzzles where they're physical puzzles and
[1235.92 → 1244.02] you try to get the try to kind of unhook the loops from each other um but I never occurred to
[1244.02 → 1256.90] me that I could or should spend my day job doing something that was so fun and i i I believe that
[1256.90 → 1263.12] like kind of i was inculcated, and maybe it was just how things were in the 80s like if you were going to
[1263.12 → 1270.20] do something meaningfully for with your life that that wasn't necessarily something that could be as
[1270.20 → 1277.94] so joyful, and so I assumed that it was something that I would just have to do in my spare time
[1277.94 → 1285.50] periodically just for entertainment um and that I couldn't connect it to um something that would be
[1285.50 → 1290.32] actually meaningful in the world um which I think was terribly short-sighted because of course computers
[1290.32 → 1296.02] can even then like could affect pretty positive change in the world but um but I wasn't really exposed
[1296.02 → 1303.34] to that I wasn't exposed to how powerful computers could be solving real important problems that was
[1303.34 → 1309.56] you know for whatever reason that wasn't something that I was exposed to until you know I was in my 20s
[1309.56 → 1314.92] I guess on that note let's take a quick break we'll hear from uh one of our awesome sponsors
[1314.92 → 1320.22] making this show possible and when we get back we're going to talk about bridge foundry so we'll be right back
[1320.22 → 1326.86] you've heard me talk about top towel several times in this podcast but today is different I've got a
[1326.86 → 1333.16] special treat for you, I went out and spoke with a listener who a year ago had never heard of top towel
[1333.16 → 1338.68] he listened to the show just like you're doing right here right now today and heard us talk about
[1338.68 → 1344.26] top towel and what they're all about, and he decided to get in touch, and now he's living the dream as a
[1344.26 → 1349.62] freelance software developer with top towel his name is Daniel Alton and I sat down and I talked with him, I said
[1349.62 → 1356.80] hey what is it that you love most about top towel take a listen well for me the thing about top towel
[1356.80 → 1362.78] which I thought would be very hard for me personally as I transitioned to a more consulting role
[1362.78 → 1368.76] uh was the way I would have access to new clients and what quality of those would be
[1368.76 → 1375.22] so I found that I've had access to awesome clients through top towel, and it hasn't been that hard to
[1375.22 → 1380.96] find because they have a lot of choice and even more than that uh there's enough choice and i I can
[1380.96 → 1386.84] actually be a little selective about what kinds of things I want to be working on so I use that as a
[1386.84 → 1392.82] way to sort of hone my skills, and you know go towards the technology that I think are worth investing in
[1392.82 → 1398.40] for the future so whether it's you know including new front-end frameworks or doing a little DevOps
[1398.40 → 1404.46] work on the side i I usually am able to find clients who are had the needs of the things I want to get
[1404.46 → 1410.94] better at so that's been that's been truly useful all right that was Daniel Alton a listener of the
[1410.94 → 1417.86] change log and also a freelance software developer with top towel if you want to follow in Daniel's
[1417.86 → 1427.58] footsteps go to top towel.com slash developers that's t-o-p-t-a-l.com slash developers to learn
[1427.58 → 1434.22] more about what top towel is all about and tell them the change log sent you all right we're back
[1434.22 → 1440.66] bridge foundry I'm excited about this because I've heard so much from Beverly about the work you guys do
[1440.66 → 1448.22] um there's we had Sarah may on the show episode 146 so for those listening we'll have that link in
[1448.22 → 1453.98] the show notes, but it's easy to type in changelaw.com slash 146 uh we talked about particularly in that
[1453.98 → 1459.34] show we talked about minding the gap we also talked about uh a little bit of bridge foundry but also
[1459.34 → 1466.10] rails bridge and this outreach and this education and uh serving the underrepresented um where should we
[1466.10 → 1472.20] begin the conversation around bridge foundry well maybe begin with the the the core workshops that
[1472.20 → 1478.92] you know that's really the thing that took off and has made this organization grow um we had this
[1478.92 → 1487.70] insight that um when we started it was about um really overcoming gender diversity in the ruby community
[1487.70 → 1494.76] and that you know very simple insight that maybe if we wanted women to more women in our community we
[1494.76 → 1503.48] should teach them the technology that we're using and i um had done a lot of reading on the statistics
[1503.48 → 1514.72] and knew that um in that in proprietary software in corporations typically you see um about 20 to 25
[1514.72 → 1522.28] percent women programmers um in open source you see two to three percent women programmers or women
[1522.28 → 1529.06] contributors of any kind it's kind of even worse than you know um not just having women programmers but
[1529.06 → 1536.38] now women in the community and um but if you do the math and I knew sort of roughly how bit how many
[1536.38 → 1543.86] ruby programmers there were um it was likely and probably still is today that there are more women
[1543.86 → 1550.22] programmers in the Bay Area than there are ruby programmers so I figured hey if we could just convert some
[1550.22 → 1556.64] of them it would be easy to get 50 50 easy yeah I say in quotes um to have 50 50 women and men in the
[1556.64 → 1560.04] ruby community and if you start with a small community you can do really powerful things
[1560.04 → 1564.80] um so we start with this idea well let's just teach women and Sarah was really passionate about
[1564.80 → 1571.34] um teaching people who couldn't code um, and so I said okay you teach that class I'll teach the
[1571.34 → 1577.10] um women programmers because I feel like I'm going to get to like a quicker outcome of actually having
[1577.10 → 1584.26] one peers if I start with women java developers or women c sharp developers or whatever um and we
[1584.26 → 1591.70] thought it would be really hard to find women um to take this workshop that we had dreamed up and um
[1591.70 → 1597.80] we spent like three weeks uh trying to figure out where we were going to post this and we um we both
[1597.80 → 1603.02] tweeted about it, and she posted on this mailing list called um San Francisco women of the web and in less
[1603.02 → 1610.64] than 24 hours we had a wait list wow and back I mean you guys might remember this was I I think 2007
[1610.64 → 1622.56] and it was common for people to say um oh maybe women don't want a code you know this is this arcane
[1622.56 → 1628.62] thing and it just might be that there are fewer women who are interested and the fact that we had
[1628.62 → 1633.32] these workshops, and we'd had them um we had them every other month and there was always a wait list
[1633.32 → 1641.88] and in San Francisco we've just consistently had 20 to 60 person wait lists for these events that we've
[1641.88 → 1651.18] been having for like seven years um it's unbelievable so really in just a few months people stopped saying
[1651.18 → 1659.18] that demand was a problem, and it really transformed how people thought about um you know the problems
[1659.18 → 1666.44] with diversity um but it really changed how you know kind of i felt as a woman in the field like i
[1666.44 → 1675.10] stopped um i would just routinely be in these groups with um you know 50 women coding and coming from
[1675.10 → 1680.80] like some of them were amazing technologists who just didn't happen to know rails and um, and it was
[1680.80 → 1685.30] really fun and really transformative for me personally i think as well as for the community
[1685.30 → 1690.26] um and if you hear Sarah may talk she gave this great presentation in December of that year
[1690.26 → 1697.04] where um we were both keeping stats of the ruby meetups, and they went from three percent women to 18
[1697.04 → 1703.72] percent women in um less than six months so tell me something Sarah about how you made the jump to
[1703.72 → 1708.46] because this is something that people have asked me not only how you made the jump from doing just rails
[1708.46 → 1713.22] to bridge foundry is now offering um, and you can probably name them i know we've got the mobile
[1713.22 → 1719.18] bridge i know we've got uh most recently an angular i believe um but how did you how did that go from
[1719.18 → 1724.54] just one particular technology to others and then I'm curious about how people if they say i want to do
[1724.54 → 1729.56] this for example i want to bring a new technology to my area you know what would I what would I do what
[1729.56 → 1735.74] are the next steps for that that's a great question um actually from the get-go we was sort of
[1735.74 → 1740.80] controversial that we called that rails bridge because we um one of the other projects that we
[1740.80 → 1750.72] started at the time i was um teaching ruby to um uh to kids um elementary school students and um but
[1750.72 → 1754.84] we decided to call it rails bridge because it was really grew out of people in the rails' community
[1754.84 → 1763.32] that wanted to change things, and we didn't think of it from the get-go is only about rails the reason
[1763.32 → 1767.30] we picked rails for the workshops is not only that was the most of what Sarah and i were doing
[1767.30 → 1774.16] but it was very hot at the time to be doing rails, and it's not like now there's been a lot of
[1774.16 → 1782.88] kind of learn to code marketing um you know president Obama um has given you know mentioned this a lot
[1782.88 → 1789.32] and we've had a lot of um new organizations really promote the value of learning to code
[1789.32 → 1796.60] um, but that was not at all true uh when we started so it was really important to latch on to something
[1796.60 → 1806.58] that had its own momentum and um but what we did very intentionally is we made all the materials
[1806.58 → 1816.66] open source, and we said hey anybody can take these materials do what you want and the only um
[1816.66 → 1823.64] guideline we set is that if in order to call it a rails bridge workshop it has to be free, and it has
[1823.64 → 1830.32] to be targeted at outreaching to some community that's underrepresented in tech which turns out to
[1830.32 → 1837.52] be like the majority of people in the world so it's not that hard um but what we saw is all of
[1837.52 → 1844.22] these spinoff groups so um there were like three different python groups there was star there was um
[1844.22 → 1851.34] the Boston python workshops which is very um popular, and they did a great job in reaching out to the python
[1851.34 → 1857.66] community and actually um create i think the individuals who did that had um transformative effects
[1857.66 → 1863.76] in you know affecting conference speakers and in a lot of different ripple effects that were very
[1863.76 → 1871.30] exciting to see um, and we actually have a funny story because i did a workshop in Cambridge um i think
[1871.30 → 1877.42] in our first year, but it didn't really catch on in the Boston ruby community until after the Boston python
[1877.42 → 1883.40] workshops, and then they were so inspired by seeing the Boston python workshops that we um ended up with a
[1883.40 → 1890.86] Boston ruby community that's very, very strong um and so really from the beginning we had a vision of it
[1890.86 → 1899.22] being um any technology but i think because we had rails in the name people who were coming from a
[1899.22 → 1904.10] different technology that was you know substantively different from rails felt like they needed to
[1904.10 → 1909.20] create their own separate organization, and so we saw that happening, and we really saw that there was
[1909.20 → 1916.96] this potential for really sharing um you know what i call the meta stuff you know the how to make a
[1916.96 → 1926.90] workshop and the teaching guidelines and um they this sort of viral workshop phenomenon um is
[1926.90 → 1935.20] something that is transcends the technology so a few years ago we decided to um create bridge foundry as
[1935.20 → 1941.02] which is really just a renaming of the umbrella organization that we'd always envisioned to house
[1941.02 → 1947.56] things that were not just rails and then renaming rails bridge to be just the workshop component of it
[1947.56 → 1952.82] that was focused on the rails workshops, and we're still in the midst of that refactor because we still
[1952.82 → 1957.24] do front-end workshops that are under rails bridge, and you know things like that we're still sorting
[1957.24 → 1965.12] things out but um, but it's pretty easy to um create a new bridge we have um closure bridge really
[1965.12 → 1970.20] took off in the last year that's closure with a j which is really exciting to have a functional
[1970.20 → 1977.82] language join the family because i feel like if you learn um a functional language and an object-oriented
[1977.82 → 1983.98] language and a web application framework you kind of have the bunch of the key components that you
[1983.98 → 1991.92] need to um be a powerful software developer today and then um with mobile bridge um i think that also
[1991.92 → 1999.90] kind of rounds out the family where people are learning um native code um and device code with java and
[1999.90 → 2010.40] um Objective-C so um so to start a new bridge you just email hello at bridge foundry.org we're working on
[2010.40 → 2018.80] having the guidelines be posted um but the best way to get a sense of um how it works is to go to
[2018.80 → 2024.30] uh one of these bridge workshops wherever you are and if you want to check one out you can go to
[2024.30 → 2034.28] bridgetroll.org and um most of the um different technologies post their workshops there and um
[2034.28 → 2039.14] and the process is pretty easy basically we'll have a conversation about like do you really understand
[2039.14 → 2043.60] like what we're trying to do here because it's most of it's written down, but it's written down in a
[2043.60 → 2049.42] lot of different places, and we're working on ways to make that kind of the documentation be more
[2049.42 → 2055.16] comprehensive so a lot of it is transmitted through kind of the oral tradition about talking the
[2055.16 → 2060.82] mission and do you understand it and um are you going to move things forward in this direction and if
[2060.82 → 2070.18] we if we're aligned in philosophy then um you then fork um one of the different um organizations on
[2070.18 → 2076.78] GitHub and um angular bridge did this most recently by just forking the mobile bridge materials
[2076.78 → 2086.82] and um we have a very collaborative process we like the um the GitHub issues um mechanism yeah for um
[2086.82 → 2096.46] sharing openly and so even though i think it's i don't love calling workshops issues yes stories i you
[2096.46 → 2103.64] know i wish we were using um i wish GitHub would change their nomenclature um not only for um for
[2103.64 → 2109.10] that before for sure but also for open source projects everything isn't an issue um but anyhow
[2109.10 → 2116.70] we use that, and it's very easy to tag people, and it's completely transparent, so anybody can come
[2116.70 → 2123.38] join the organizing team for workshop and um i think that's a real that's a breakthrough that um
[2123.38 → 2128.58] Rachel Myers innovated and then all the different um bridges are starting to um
[2128.58 → 2134.10] uh use those techniques which i think is really exciting and that's been super helpful for me as
[2134.10 → 2139.84] well because i actually was tagged on something for a rails bridge that was regionally close to me but
[2139.84 → 2144.28] not necessarily in my state or even in my town, but it was something that i could provide assistance on
[2144.28 → 2148.82] and because everything is transparent it's not stuck in someone's email box so this collaboration
[2148.82 → 2154.16] is you know it's truly a community helping to organize these workshops and um something else
[2154.16 → 2158.50] that i think is really nice is all the curriculum is open source, so people can contribute to it and
[2158.50 → 2165.00] they can, I've seen lots of rails bridge forks in the past for the curriculum there and so um i think
[2165.00 → 2169.94] that's been really helpful to see that and something else I was going to ask you to share Sarah is that
[2169.94 → 2175.00] this is really a culmination of the stone soup illustration that you've shared on your blog before because
[2175.00 → 2179.50] we're all bringing what we have as a talent and essentially to really better the community and
[2179.50 → 2185.06] and to teach them um do you mind sharing how that's really manifested with the stone soup illustration
[2185.06 → 2191.20] yeah absolutely I mean I feel like often um putting a workshop together is like that it's very
[2191.20 → 2198.42] intimidating I mean to put on an event especially because most of our volunteers are developers they're
[2198.42 → 2204.22] individual contributors who um know how to write code, and they're inspired to share what they know
[2204.22 → 2212.08] but most of them have not put on an event or approached a company about donating space or
[2212.08 → 2217.92] you know god forbid talk to ask for somebody for money for sponsoring something and so each of these
[2217.92 → 2227.90] things seems a big hurdle and often all we need is somebody to say okay I will organize it and then um
[2227.90 → 2234.02] and then it's much easier for somebody to help than it is for somebody to do and I think this
[2234.02 → 2243.00] was most it was best illustrated by um somebody I got a tweet one day from um uh I can't remember who
[2243.00 → 2248.82] was first whether it was liana Leah or um Mary Colbert from Boston who said hey how do we have a
[2248.82 → 2252.60] rails bridge workshop in Boston this was the very first one that actually took place in Cambridge
[2252.60 → 2261.08] um and I said well my family's there if you organize a workshop then I'll come teach and
[2261.08 → 2268.60] based on that you know I was like I'll bring a rock let's make soup there you know we found
[2268.60 → 2275.58] ta sum space all the things came together and every single person who was involved some
[2275.58 → 2282.52] some people did an awful lot of work, but it's that impetus somebody has to say okay I will step
[2282.52 → 2290.10] up I will bring the first space or I will be the first teacher I will um you know in the case of a
[2290.10 → 2293.28] new bridge I will write some pot like lunch or something like that you know it's like everybody
[2293.28 → 2300.70] brings something and everybody eats exactly many hands make light work yes, yes for sure well that's neat
[2300.70 → 2308.42] um I guess another question i I have for you is uh your passion for the underrepresented
[2308.42 → 2316.04] um not only uh gender-based or race-based but even down to children you love kids
[2316.04 → 2321.26] yeah I mean a lot of it doesn't love kids right who doesn't love kids well some people don't
[2322.12 → 2328.48] um I have a child I have a boy child which is also comes from one like I didn't want to do things
[2328.48 → 2331.84] just for girls because I would never want to do something that he couldn't be a part of
[2331.84 → 2344.40] um and I also see how there's true i by no means ever want to diminish anyone's enthusiasm for doing
[2344.40 → 2351.86] this great work but if you have a boy child there's actually fewer things these days um to bring them to
[2351.86 → 2358.34] to get them enthusiastic about technology because there are a lot of girls only programs now but there
[2358.34 → 2366.12] um are you know there are fewer programs um that are inclusive of boys which is kind of an odd
[2366.12 → 2374.68] thing um because I mean only 10 years ago that all the things were um were not even if they weren't
[2374.68 → 2381.20] targeted at boys they feel that way if it's going to be mostly boys um so I think we just need to
[2381.20 → 2388.10] be balanced in our approach and make it so that these opportunities are available for everyone
[2388.10 → 2397.78] um and I'm also very painfully aware that a lot of the work we do is really available to people who are
[2397.78 → 2406.08] quite well off um if you know again not to diminish the fact that there is very real sexism in the world
[2406.08 → 2413.82] and there are a lot of women who you know maybe um they have a lot of resources, but they still can't
[2413.82 → 2421.88] find a job because of barriers in the workplace um but then there are people who um have the aptitude
[2421.88 → 2429.50] for this work, and they don't have a laptop can't come to a workshop and um when we were doing the very
[2429.50 → 2436.22] first year of rails bridges I was really struck by like is this the work that I want to be doing with
[2436.22 → 2445.72] my life like teaching coding to um you know people with of privilege um and a very good friend of mine
[2445.72 → 2453.20] David Bogart um who I know from high school said to me well maybe what you're doing is you're first
[2453.20 → 2462.54] doing this work in the community that you know the people that you are most like and most have access
[2462.54 → 2471.92] to and um and then if you're successful, and you know in you make this transformative you will then
[2471.92 → 2478.30] have a lot of volunteers who can then take this further, and it's very, very exciting to start seeing
[2478.30 → 2485.96] that now um there's a volunteer here in San Francisco Michelle Glasser who's um looking at
[2485.96 → 2492.90] you know are there places in San Francisco, and we've identified a few of them that are teaching
[2492.90 → 2502.54] um like word and excel and PowerPoint to people who don't have computers and maybe there's an
[2502.54 → 2508.28] opportunity for partnership there maybe we could um you know teach coding classes in their lab
[2508.30 → 2517.60] labs um because I think that um we have to go beyond just teaching people to write words on
[2517.60 → 2527.20] computers um I think this just such an opportunity to broaden our group of makers to all the people in
[2527.20 → 2534.36] the world and if we don't do that we will not solve the problems that we need to solve to fix
[2534.36 → 2540.74] the um the planet we're on uh or all the damage we're doing to the planet we're on I should say
[2540.74 → 2545.34] I'm reminded that every day you know I don't know about you but I watch vice news on HBO here once
[2545.34 → 2551.58] in a while, and they had this episode recently about uh this myth called global warming uh I'm not sure
[2551.58 → 2556.90] which side of the fence you stand on, but it seems so scientifically clear and so visibly clear that we
[2556.90 → 2562.36] have some serious issues, and they may or not be able to be solved by us by reducing carbon emissions
[2562.36 → 2566.90] and things like that but there is a problem and there is something to be solved there and
[2566.90 → 2572.76] yet people can still turn a blind eye to this changing earth we're on and still do crazy stuff
[2572.76 → 2579.76] uh you know adjacent to that was a topic in India and how they have really poor sewage system
[2579.76 → 2585.62] and they have how they have public defecation like it's crazy how there's such severe conditions in the
[2585.62 → 2594.04] world, and we're just you know I guess bubbled people say privileged and I'm I'm almost I'm weary
[2594.04 → 2599.18] of that because I know I'm privileged but at the same time there are some things in my past because I'm
[2599.18 → 2606.76] white I'm a male um but I grew up poor I should not be here where I'm at today and if I told you my
[2606.76 → 2611.82] story you'd cry but I got a crazy story, and it wasn't privileged my whole life even though I'm white
[2611.82 → 2616.44] and I'm a male and I feel like we're in these bubbles you know it's like you said touch the
[2616.44 → 2620.40] people you can that you have most access to once you've proven the concept or proven your
[2620.40 → 2627.18] your ability move on to or have a ton of volunteers to go to the next step yeah I'm really glad you
[2627.18 → 2632.38] said that because, and thank you for um kind of sharing a little bit of your personal story
[2632.38 → 2638.82] because I mean that's one of the things that I'm always um so moved by the people who attend these
[2638.82 → 2647.48] workshops um one of the things that we always do is um provide coffee in the morning and snacks and
[2647.48 → 2653.36] lunch, and we have an after party where the volunteers get drink tickets and everybody goes out and
[2653.36 → 2659.84] socializes and that's really I've always thought that was important because it keeps people there
[2659.84 → 2667.34] in this social environment um but after one workshop we got this feedback of somebody who said
[2667.34 → 2676.24] that they um would not have been able to afford to eat except that the food was provided and so
[2676.24 → 2682.66] it was very it was incredible to them because it was such an equalizer whereas normally you know if
[2682.66 → 2687.30] they go they either have to not eat or you know everybody else goes out to eat, and they can't join
[2687.30 → 2694.34] and um i I remember writing this blog post called the psychology of abundance
[2694.34 → 2699.38] abundance and I think that's so important for creating a great learning environment
[2699.38 → 2706.56] is not feeling you know this desperate feeling of like of scarcity right I think that that inhibits
[2706.56 → 2716.88] our creativity and for to just for one day to give everybody that feeling of there's food here for me there are
[2716.88 → 2724.96] people here for me, I've got all the things and the only thing that I have to overcome is that very
[2724.96 → 2734.80] challenging gap from what I don't know to what I do know and um I can, i get the same everything
[2734.80 → 2740.02] as everybody else for this one day and I think that that's just such a precious thing I'd like I wish
[2740.02 → 2746.14] everybody in the world had that yeah I think that's something um that is really tremendous about the
[2746.14 → 2751.12] workshops is that it really is an equalizer and one of the things that's really great about the whole
[2751.12 → 2756.12] stone soup concept and everybody in your area giving what you can or doing what you can for your local
[2756.12 → 2763.52] region you know for example Sarah can't do anything in Florida um she can, but she's not in proximity to
[2763.52 → 2768.66] Florida I'm I'm here this is a circle that I can impact I'm not in San Francisco I can't impact her
[2768.66 → 2775.04] circle, but she can and one of the things that i I do like is that because we're connected by the
[2775.04 → 2779.62] internet because we have these workshops because we have GitHub she's also helped me to be more
[2779.62 → 2785.66] sensitive to really the people that we look up to and the heroes that we have and Sarah you wrote a
[2785.66 → 2791.28] post about being an ally I don't know if you recall that um that started out about talking being
[2791.28 → 2796.50] privileged and things like that I would love it if you'd share more about your experience and just
[2796.50 → 2800.34] focusing on even diversifying your heroes and looking to different people even in different
[2800.34 → 2806.56] sectors uh because I think that's tremendous it really helps us to grow I like that post by the
[2806.56 → 2811.04] way that was really yeah it's a great post isn't it thanks that actually came out of um
[2811.04 → 2818.62] Martin Luther king day and um every year for mighty verse for the last I don't know three or four years
[2818.62 → 2824.30] we do um we've been taking the I have a dream speech and translating it into another language and
[2824.30 → 2831.20] doing recordings of different voices and um you know as we all know the past year has been
[2831.20 → 2842.36] a rough year for race in America um it has just come I mean I have just such empathy for um you know
[2842.36 → 2848.22] people who have a different experience of me and who don't feel safe in their own cities um you know
[2848.22 → 2853.16] and as a woman I've you know there are certainly a lot of places that I don't feel safe but um it's just
[2853.16 → 2860.88] it can't be compared to being a black person in America and um there were a number of articles the
[2860.88 → 2869.32] two weeks before um Martin Luther king day about the um Santa classification of dr Martin Luther king
[2869.32 → 2880.16] and that he's like somehow um you know safe uh black hero, and it's and that there's only certain
[2880.16 → 2887.28] speeches and parts of speeches that are retold and that you know the I have a dream speech that has
[2887.28 → 2894.60] been at least in some people's um thinking appropriated by um white America and then I was
[2894.60 → 2901.06] like oh no I'm doing this um whole thing around I have a dream and I felt it was really important to
[2901.06 → 2909.62] write about this other perspective and um and I think that I have this voice which can be heard by
[2909.62 → 2917.86] white people easier than um than you know other voices I think we're all get a chance to be change
[2917.86 → 2922.82] agents and I think that's sort of the role you play because somebody just said there was that you have
[2922.82 → 2929.96] um paraphrasing because it's kind of broke my mind but that you have access to white people's minds i
[2929.96 → 2935.62] guess how did you say it well I think that I can be heard, or you can be heard okay that's yeah sorry i
[2935.62 → 2946.50] don't remember exactly how I said it but that um I think that I am of a culture and
[2946.50 → 2955.78] I like even though that in some ways I'm a marginalized um I'm in a marginalized community
[2955.78 → 2965.22] in my wider community I'm a woman I have um you know certain attributes I'm now a little older
[2965.22 → 2974.10] i I'm a mom like these are things that um you know not everybody who is a software engineer
[2974.10 → 2982.94] think highly of but at the same time as I'm marginalized in some circles in other circles
[2982.94 → 2994.14] I'm given undue weight and undue respect not undue but uneven you know i I got a computer science degree
[2994.14 → 3000.60] I went to an Ivy League school I started programming when I was 12 you know like these are all these
[3000.60 → 3006.42] attributes that some people I think are overvalued right it's not that I don't think they should be
[3006.42 → 3012.64] valued it's just that I think people who taught themselves to code when they're 25 should be as
[3012.64 → 3019.30] respected as somebody who went through four years of a CS degree, and so we need to just take
[3019.30 → 3026.88] advantage of the know the platforms that we have to um as you say make change
[3026.88 → 3033.72] though Sarah the one thing I'm noticing though is that you allow the things that marginalize you
[3033.72 → 3039.26] to describe you not define you right like you're not boxed in by them, they're part of who you are
[3039.26 → 3045.84] they don't make up who you are they're not your identity yeah I think it's um I mean it took me a long
[3045.84 → 3059.30] time to get to that space um and I think that it's it for a long time i um I worried about um that I was
[3059.30 → 3066.02] being like too female a little quiet voice a little shy voice for a long time and that I really tried to
[3066.02 → 3078.02] change who I was and how I behaved um so that I would not be um have my ideas um uh boxed in by how
[3078.02 → 3086.34] people perceived me and then I think certainly growing up and being a parent and um being a mom
[3086.34 → 3096.00] I've grown to really cherish you know these different parts of my me and um luckily uh was able to
[3096.00 → 3102.34] seek out people who celebrate the know how we're all different from each other and that
[3102.34 → 3108.56] and largely through the work of rails bridge and bridge foundry had a chance to meet and interact
[3108.56 → 3117.46] with this completely different community that is hundreds of thousands of people inside the software
[3117.46 → 3124.68] community that actually values the things that I value and I used to think that it was
[3124.68 → 3133.42] 0.001 or something like it was so rare for me to interact with people who shared my values that i
[3133.42 → 3140.04] thought that it was too much for me to expect that I could work with these people that um that I felt
[3140.04 → 3148.08] like I had to you know hide my values under a bushel, but you know um it's not that way and I think that's
[3148.08 → 3154.66] very exciting that's a good uh time to take a pause real quick and hear from a sponsor our uh last bunch of
[3154.66 → 3159.86] the show here we'll break for a minute come back Beverly's got a pressing question for you that I'm
[3159.86 → 3164.08] excited to hear about so when we get back Beverly will take over so just a sec
[3164.08 → 3171.16] I have yet to meet a single person who doesn't love digital ocean if you've tried digital ocean
[3171.16 → 3177.36] you know how awesome it is and here at the changelog everything we have runs on blazing fast
[3177.36 → 3183.56] SSD cloud servers from digital ocean and I want you to use the code changelog when you sign up today
[3183.56 → 3190.50] to get a free month run a server with one gig of ram and 30 gigs of SSD drive space totally for free
[3190.50 → 3197.52] on digital ocean use the code changelog again that code is changelog use that when you sign up for a
[3197.52 → 3202.24] new account head to digitalocean.com to sign up and tell them the changelog sent you
[3202.24 → 3209.70] all right we're back Beverly what uh what do you have on your side over there
[3209.70 → 3215.24] the primary question is so I've really benefited from hearing a lot of your experience so if you
[3215.24 → 3220.82] are talking to somebody who is in an area who maybe they're not in San Francisco maybe they're in a
[3220.82 → 3225.54] smaller area North Carolina or something like that, and they hear this, and they're inspired to impact
[3225.54 → 3231.14] their area or to make sure that software is more available um, and they don't want it to be by chance
[3231.14 → 3235.50] what are the things that you would suggest that they do you know where they are like what is an
[3235.50 → 3240.32] action step that they could take today to start making themselves uh available to other people or
[3240.32 → 3245.66] to serve their community or to make information accessible where they are well I think that um
[3245.66 → 3251.36] wherever anybody is there is opportunity to volunteer and reach out and teach what you know
[3251.36 → 3258.12] so if you don't if you're excited about this and there are things you don't know, and you want to learn
[3258.12 → 3265.74] um there are a lot of great online resources but I'm a huge fan of connecting in person with your local
[3265.74 → 3275.72] community I think that those ties um can be very, very powerful so um there are a lot of different groups
[3275.72 → 3281.42] doing this kind of work but I would also encourage you to you know don't be afraid to start things
[3281.42 → 3293.24] um there I think just look out at your local meetups go out there and um and check out
[3293.24 → 3300.84] all the different things happening in your community and um and the things happening online
[3300.84 → 3307.18] and look for the opportunities to meet like-minded people and get yourself a support system too
[3307.18 → 3313.88] you know I think that that's really important that um that there's a balance and one of the things
[3313.88 → 3321.98] that I've found for myself and I've seen in other people is that by doing this work it gives back
[3321.98 → 3328.20] and if you're feeling drained by it then I think you need to strike a balance where you're also getting
[3328.20 → 3333.88] support, and you're finding a way where you can strike that balance where you're getting
[3333.88 → 3341.70] enriched by the work that you do as well as doing it and I think too we sometimes have this vision of
[3341.70 → 3345.52] oh I've got to have a workshop with 50 people or I've got to have a workshop with 30 people or
[3345.52 → 3350.92] something like that, and it's really not true because one of the things that um I remember reading about
[3350.92 → 3355.28] your teaching kids rails bridge that was one of the first things when I started teaching kids
[3355.28 → 3360.58] that I looked to as a resource because now I teach a monthly tech club for homeschoolers and
[3360.58 → 3365.44] we've used some of that material and some of the ideas that you expressed a long time ago in that
[3365.44 → 3370.28] in those posts and things and something that people need to realize is they could have a know
[3370.28 → 3374.34] coffee table meetup in fact the first rails bridge workshop it actually probably wasn't an officially
[3374.34 → 3378.82] sanctioned workshop, but literally there were three of us around a kitchen table and I said let's go
[3378.82 → 3383.34] through the curriculum together because you know they wanted to get started they couldn't go for
[3383.34 → 3387.66] and there was no minimum I mean it wasn't an official workshop, but you don't have to have
[3387.66 → 3391.26] this formal thing the lovely thing about open source is that the curriculum is available
[3391.26 → 3395.32] and you can impact your community, and you've been such a good example of that of just starting
[3395.32 → 3401.14] just doing something, and you know uh just being free to go ahead and try something different
[3401.14 → 3408.72] and impact your community that way yeah I would also underscore that there need to be no official
[3408.72 → 3416.02] sanction correct if it's free if you're doing it in your community um, and you're teaching others it's a
[3416.02 → 3423.54] you know you can um use all the materials and do the work and um it's a wonderful thing and absolutely
[3423.54 → 3430.68] um and yeah and I started teaching kids just you know my kids elementary school and um doing things
[3430.68 → 3435.40] small scale first the other thing that's great about teaching kids and I would highly recommend
[3435.40 → 3442.82] is I taught I practiced the lessons with my kid and two of his friends and then I let them be
[3442.82 → 3454.64] um ta's and kids getting kids to teach kids I think is the most amazing thing because they will learn
[3454.64 → 3460.86] so much through teaching and giving them that responsibility is um I think the best thing that
[3460.86 → 3465.50] you can give to them, and they have no fear that was something that you shared with me after we had our
[3465.50 → 3471.02] rails bridge team and my kind of post notes debrief as I was going through it was like they were willing
[3471.02 → 3476.62] to experiment and try in ways that the adults were not, and we hadn't entirely every it was under 18
[3476.62 → 3482.20] it was uh roughly 7th to 12th graders who did the rails big workshop, and it was amazing it was amazing
[3482.20 → 3485.14] to see, and then they would help each other, and then they would teach each other a little bit it was
[3485.14 → 3490.34] really, really amazing to see that kids are so awesome
[3490.34 → 3500.08] uh so Sarah I've been uh it was sort of last minute too as I'm prepping the notes to prepare
[3500.08 → 3504.42] for this call I was thinking you know what would be a profound question to ask you in addition to some
[3504.42 → 3508.36] of our awesome closing questions we'll ask you as well but what's a good profound question that i
[3508.36 → 3514.24] can ask you that would get something futuristic to get you to hypothesize about the future or what
[3514.24 → 3519.26] isn't there that should be there, and the question is what's missing in software that you wish was there
[3519.26 → 3524.14] that either you're actively trying to add or hope to one day be able to add
[3524.14 → 3533.06] software community not just tech wise but just in this space we're in open source things you're involved
[3533.06 → 3540.12] in yeah I think that's a good question um I think there's um like a few different angles on it
[3540.12 → 3549.24] I think um the biggest thing that's um missing in the world today um is great places to work
[3549.26 → 3560.96] um I have been really um fortunate in working with really amazing teams um and largely because I sought
[3560.96 → 3567.88] them out I think that there's a lot of people who um I talk to women all the time who um are leaving
[3567.88 → 3574.22] the workforce um not the workforce just leaving computing um they've decided they or they're
[3574.22 → 3581.60] coming back through the workshops right um so I think that the biggest thing that we need
[3581.60 → 3586.76] is workplaces where people respect each other regardless of what they look like or their
[3586.76 → 3593.88] backgrounds um or how they came to be computer programmers and um and I think we need this
[3593.88 → 3599.58] everywhere right this is not just a problem amongst um software developers but I think we have a
[3599.58 → 3609.30] unique opportunity in tech to fix it because people the entry points are so low in terms of
[3609.30 → 3615.36] um not having to have a formalized background to get into it is still takes a lot of hard work to get
[3615.36 → 3623.50] into it but um but I think we have a tremendous opportunity to transform the workplace into a place
[3623.50 → 3628.46] where people actually respect each other regardless of their background so that's the biggest thing
[3628.46 → 3638.38] that is not missing but not as ubiquitous as I think it should be and then the other thing which I think ties
[3638.38 → 3652.14] into the entry point um is that I think that every computer and every device should come with software that lets you hack it
[3652.14 → 3664.06] um I think that um it should not be uh it shouldn't require you to install extra stuff to um write simple code that controls
[3664.06 → 3670.70] your computer or your device so does that mean that you're pro android and anti-apple
[3670.70 → 3682.12] I well I'm a big fan of um apple's uh software and hardware uh, but it is um I think Steve Wozniak
[3682.12 → 3689.00] um had a great influence on the early mac and early apple and um and I think that
[3689.00 → 3696.34] something's been lost there that iOS must upset you then to a degree because like it does take
[3696.34 → 3701.38] a computer and extra software to do anything with it like you can't do much from the actual device
[3701.38 → 3706.36] well it's bigger than that it was actually against their terms of service to develop
[3706.36 → 3718.08] any app that allowed the end user to code until like a year or two ago, so apple creates policies
[3718.08 → 3729.62] that makes it harder for third-party developers to make this accessible, and you know that's changing
[3729.62 → 3736.22] but um, but it needs to change more so for those who are long-time listeners of the show know that
[3736.22 → 3740.64] we have a few questions we like to ask the end of the show we're going to ask two today uh we're not
[3740.64 → 3745.80] going to do several of them uh but one I want to ask you in particular that sort of contrast against
[3745.80 → 3752.12] something you might say in response uh to your on being an allay post when you said name your heroes
[3752.12 → 3758.00] and you said seriously make a list of your top 10 if they were mostly one race class or gender find
[3758.00 → 3762.48] some more heroes, and we have a question we like to ask people which is who's your programming hero
[3762.48 → 3766.46] i I guess we can open that up to be any hero but I'd like to see if you can name 10
[3766.46 → 3773.90] um well I'll name six actually I don't know all of their names um but the programming heroes are
[3773.90 → 3785.00] the women who program the ENIAC so um in 1945 um there were two um engineers who created um one of
[3785.00 → 3794.58] the first maybe the first digital computer which was the ENIAC and they um it was built to um solve
[3794.58 → 3803.56] these um parabolic equations to uh I think they were they would to do the trajectory of an um of the
[3803.56 → 3812.04] ballistics uh you know for the for World War ii and before the computer they had um women who they
[3812.04 → 3820.42] would hire um who were math majors they um recruited to use slide rules to create these books
[3820.42 → 3826.46] of um you know sort of you would have like the angle that the gun was pointed and what kind
[3826.46 → 3831.82] of munition it was and like the wind speed and these different um inputs, and then it would say
[3831.82 → 3839.80] um like how they would set up um these uh you know the guns in order to point the artillery
[3839.80 → 3850.72] at the enemy and um in actually in the early um 1900s they um they would call these women who would
[3850.72 → 3857.50] do math computers there's a great book called if computers were human or when computers were human sorry
[3857.50 → 3865.56] anyhow um they took six of the best computers, and they told them that they had a new assignment for
[3865.56 → 3874.58] them and they gave them the wiring diagrams the schematics of the computer and of the new machine
[3874.58 → 3882.54] and they said that they needed to figure out how to wire up the inputs and outputs in order to make
[3882.54 → 3887.86] it does the same calculations that they had been doing the slide rules and these six women were the
[3887.86 → 3896.70] very first programmers um and I was just I'm looking up um Kay McNulty and um jean Jennings
[3896.70 → 3903.48] um invented the subroutine um which was like oh we won't have to plug in these wires to make these
[3903.48 → 3909.82] connections as many times we could reuse this um little bit of logic and um you know they invented
[3909.82 → 3916.54] loops and all of these you know sort of very common programming structures today that um they were
[3916.54 → 3923.06] doing programming by like connecting you know wires to sockets and I think those are my heroes they were
[3923.06 → 3932.44] doing things that were actually hard and then um after we know when all this stuff became public um
[3932.44 → 3938.58] they were not even mentioned in any of the articles that's not cool that's not cool that's not cool
[3938.58 → 3946.22] what's very exciting is um 50 years later um Kathy Lyman did a lot of research and surfaced
[3946.22 → 3952.76] these stories and um in the last 10 years there's been a number of articles about this amazing work
[3952.76 → 3959.94] that these women did and um and I just love to hear about the early days of um you know women and men
[3959.94 → 3965.12] when they were you know inventing things and creating things that now we take for granted
[3965.12 → 3970.64] so we have one other question that we wanted to ask to Sarah and that is um and I know a little
[3970.64 → 3975.30] bit of this because I'm already involved somewhat with bridge foundry but uh even if you're not
[3975.30 → 3978.94] somebody who's going to ta you don't necessarily have a technology that you want to put forward and
[3978.94 → 3983.90] you want to go ahead and share what would you say is a good call to arms for bridge foundry or if
[3983.90 → 3987.84] somebody wants to step in and help, and maybe they're a designer, or maybe they're just a community
[3987.84 → 3991.74] innovator like I have a friend who's really great at just planning parties, and so she's perfect at
[3991.74 → 3996.04] helping with workshops because she's good at the logistics um what would you say to someone like
[3996.04 → 4001.22] that are some uh things that they should see about contributing to or ways that they might be able to
[4001.22 → 4005.22] help their community even if they're not a programmer, and they aren't starting a new workshop or creating
[4005.22 → 4013.36] curriculum well I think that there's we need all the things right that um people who can organize
[4013.36 → 4021.10] logistics and organize events are precious and amazing people and um there's it turns out that
[4021.10 → 4026.76] we've had an easier time finding teachers and TAS than the other skills, and maybe it's because you
[4026.76 → 4032.20] know we're finding people who are like us and that's always easier but um you know and or maybe
[4032.20 → 4038.14] we're just not you know getting the word out effectively but um but the people who know who are willing
[4038.14 → 4044.56] to step up, and you know do the logistics side of things and put up events and um and the other thing
[4044.56 → 4050.34] is I think people who are willing to write the stories who are willing to show up at an event and take
[4050.34 → 4058.02] photos and write a blog post I believe that if more people even just knew what was happening
[4058.02 → 4063.70] with all of these workshops and the programmers teaching programmers, and you know people becoming
[4063.70 → 4072.34] new programmers every weekend that that would transform the world as much as our doing the work itself
[4072.34 → 4076.38] because a lot of it is just like we started talking about the beginning
[4076.38 → 4083.76] you know knowing it's possible knowing it's an option is half the battle and making accessible
[4083.76 → 4089.78] to everybody that's really that's really the angle yeah making it you know I mean like I look at these i
[4089.78 → 4095.76] think about like these you know sort of young musicians who you hear these amazing um young people
[4095.76 → 4104.40] you know from all walks of life right who are coming out of you know poverty or um different
[4104.40 → 4110.16] backgrounds where maybe they wouldn't think of um being a programmer, and they're so creative I think
[4110.16 → 4115.92] those are people who should be like making mobile apps and um I'd like to you know I'd like us to be
[4115.92 → 4123.74] reaching everybody well that's uh that's certainly true for sure well it's um it's been a pleasure
[4123.74 → 4130.30] having you on the show finally Sarah very excited about what you're working on um very awesome for you to
[4130.30 → 4135.04] give us your time today to sort of dive deep not only into some of your passions but also to
[4135.04 → 4139.92] share some of your backstory about who you are and what makes ultrasaurus
[4139.92 → 4146.90] I've uh I've been uh very curious about you know who you are and what where you've come from so
[4146.90 → 4151.42] I appreciate uh being privileged enough to sit here and have this conversation with you
[4151.42 → 4155.82] and Beverly thank you so much for making this possible to just kind of
[4155.82 → 4160.54] aligning the stars with us and Sarah and just sharing what you do sharing the ways that you work
[4160.54 → 4166.92] uh with bridge foundry in your area um is there anything else you want to cover before we tail
[4166.92 → 4171.32] off because if not I'm gonna I'm going to go through our rundown of going out and that'll be it
[4171.32 → 4180.40] oh I think just one more plug um we would love to have more open source contributors to bridge troll
[4180.40 → 4187.72] which is our open source registration system we would love designers and developers people who
[4187.72 → 4196.28] want to write up stories of how it's used um or screencasts for new organizers so whatever um part of
[4196.28 → 4203.40] um the software development process that you might be excited to contribute with um go to um to GitHub
[4203.40 → 4209.24] um in the rails bridge organization there's um a bridge troll repo and um lots of instructions
[4209.24 → 4215.12] about how to get started and join our Google group, and we'd love to have you awesome yeah we talked
[4215.12 → 4219.46] about that a little bit on Sarah's show she mentioned the same thing so you guys are in sync
[4219.46 → 4224.40] on uh on promoting uh contributions to that so we'll link it up in the show notes for sure
[4224.40 → 4230.52] um because that's what we do around here right excellent so just for those who are listening
[4230.52 → 4237.50] uh what did I say this episode number was 157, so this is episode 157 go to changelog.com
[4237.50 → 4242.90] slash 157 everything we talked about heroes and all will be in there we'll do all the digging for
[4242.90 → 4247.20] you don't worry about wrecking your car because you're trying to type down the URL it's not going
[4247.20 → 4253.26] to happen don't do that just go to our show notes, and you'll be taken care of uh thanks to all the
[4253.26 → 4257.98] listeners for listening to the show thanks to our sponsors code ship top towel and digital ocean
[4257.98 → 4264.16] for being awesome and supporting the show next week we have uh an awesome show as well every
[4264.16 → 4270.34] week is an awesome show single page apps with uh Henrik and i I haven't practiced pronouncing his
[4270.34 → 4276.10] last name but I think it's Porter, or it's horse I haven't asked but uh if anybody here knows correct
[4276.10 → 4281.20] me please uh but other than that I think that's the end of the show so let's say goodbye everybody
[4281.20 → 4283.66] bye-bye thank you so much thank you
[4283.66 → 4286.14] you
[4286.14 → 4290.14] you
[4290.14 → 4292.14] you
[4292.14 → 4294.14] you
[4294.14 → 4296.14] you
[4296.14 → 4298.14] you
[4298.14 → 4302.14] you
[4302.14 → 4304.14] you
[4304.14 → 4306.14] you
[4306.14 → 4308.14] you
[4308.14 → 4310.14] you
[4310.14 → 4311.14] you
[4311.14 → 4311.16] you
[4311.20 → 4341.14] you
[4341.14 → 4341.16] you
