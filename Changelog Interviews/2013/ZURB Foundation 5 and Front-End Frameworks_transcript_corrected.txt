[0.00 → 14.30] welcome back everyone this is the changelog where members support a blog podcast and weekly
[14.30 → 19.36] email that covers what's fresh and what's new in open source check out the blog at the changelog.com
[19.36 → 25.54] which is now hosted on a blazing fast digital ocean SSD cloud server I'm pretty, pretty proud
[25.54 → 29.42] that I'll give you some details here in a bit uh, but our past shows can be found at five by five
[29.42 → 33.40] TV slash changelog, and you can subscribe to our weekly email it's called the changelog weekly
[33.40 → 38.60] we cover everything that hits our open source radar subscribe at the changelog.com slash weekly
[38.60 → 44.22] this show is hosted by myself Adam Staravia and also Andrew Thorpe Andrew say hello yo what's
[44.22 → 49.40] going on kind of had some change of plans this week kind of worked out though right yeah, yeah excited
[49.40 → 53.38] because of it we get to talk about some pretty cool stuff with some cool people here cool stuff
[53.38 → 59.96] cool people all right uh and this is episode 112 and today's show is sponsored by digital ocean and
[59.96 → 66.10] top towel that's t-o-p-t-a-l we'll tell you a bit more about them later in the show but top
[66.10 → 71.72] top connect startups businesses and organizations to a growing network of elite engineers around the world
[71.72 → 77.94] so pretty cool stuff there top.com slash developer if you want to apply uh but digital
[77.94 → 81.86] ocean I'm pretty excited about this so digital ocean has been supporting the show for a bit now we
[81.86 → 86.78] we partnered with them a couple of months back, and you know we've been telling you about digital ocean for
[86.78 → 92.78] quite some time and all the while kind of being envious waiting to get hosted on blazing fast SSD
[92.78 → 98.06] cloud servers and i have to say that this past week we pulled the trigger uh I was a little
[98.06 → 103.20] intimidated because if Andrew like you know me I'm not much of a hacker I'm I'm more of a front-end guy
[103.20 → 111.84] right so I built an Ubuntu server this past week I built a web server it would not have
[111.84 → 116.50] happened unless I got over that intimidation hurdle thanks to digital ocean tutorials they got some
[116.50 → 122.96] really rock solid tutorials on building a lamp stack on uh on Ubuntu so really thrilled about that i kind
[122.96 → 127.62] of got over that so if you're out there, and you're like man I want to use some really cutting edge
[127.62 → 133.50] super awesome hosting and digital ocean sounds just like that well guess what it is but get over that
[133.50 → 136.80] intimidation hurdle because they got some perfect tutorials in the show notes we're going to link
[136.80 → 142.10] out to them uh and I hope to kind of do a digestion of what I've done and kind of what I've learned too
[142.10 → 145.92] and I've learned lots to cool new tricks this week so I can't wait to share them with you and if you
[145.92 → 152.58] got any questions say hello on Twitter or whatever we'll, we'll sync up on it but uh backups snapshots
[152.58 → 160.24] root access resizing of your droplet an awesome simple easy to use dashboard just
[160.24 → 165.36] phenomenal we love digital ocean, and we want you to try digital ocean today for free using our promo code
[165.36 → 171.24] that's changelog sent me that's changelog sent me which will give you a ten dollar hosting credit
[171.24 → 176.40] or two months free so head to digital ocean and uh become awesome today digital ocean.com
[176.40 → 182.18] and we got some awesome people now today Andrew we got uh Jonathan smiley and uh mark hays from
[182.18 → 187.44] curb we're going to hear we're here talking about foundation five and I guess you guys Jonathan
[187.44 → 192.86] you guys got some crazy stuff going on there so uh Andrew kick off the show for us man yeah so like you
[192.86 → 197.84] we're here with uh Jonathan and mark from curb, and we're here to talk about foundation five and also
[197.84 → 201.82] talk about a new project that they got I don't know when they released it so we'll let them kind
[201.82 → 205.70] of kick it off and introduce so uh Jonathan why don't you kind of give us an introduction to whom
[205.70 → 210.56] you and mark are and Mark can kind of weigh into and talk tell us a little bit about curb for those who
[210.56 → 216.20] don't know and what we're going to talk about yeah I can do that uh so hi everybody uh my name is
[216.20 → 221.00] Jonathan smiley I'm one of the partners here at curb uh I'm here with mark hays he's one of our senior
[221.00 → 227.04] engineers uh curb is a product design company in Campbell California we're down at the south end
[227.04 → 232.88] of uh Silicon Valley if you ask all the agencies up in the city that's the uncool end of the valley
[232.88 → 240.34] but whatever screw those guys that's not true yeah um but uh we've been around for curb's actually been
[240.34 → 245.94] around for a little over 15 years now uh I've been with curb for five and mark you've been here for
[245.94 → 250.26] two and a half two and a half before uh we released the first version of foundation feels like a lot
[250.26 → 255.70] longer than two and a half years that you've been here but time flies when you're crazy busy um
[255.70 → 261.00] but uh we've got a number of projects that we have going at any given time uh the ones that were
[261.00 → 266.84] uh that we're going to talk to you guys about uh and that we're we're like neck deep in right now
[266.84 → 272.48] our foundation uh which is an open source framework that we developed a couple of years ago now
[272.48 → 281.06] uh for building responsive websites uh it's it was I think actually the first like basically feature
[281.06 → 286.30] complete responsive framework uh so we've been we've been working on that for a couple of years
[286.30 → 291.32] and we have a all-new version of that coming out on Thursday next week so a week from today
[291.32 → 297.08] actually well a week from today as we're sitting here recording it um that's true that's going to be
[297.08 → 302.84] Thursday it's coming out uh on the 21st uh and then we also just recently released it was only
[302.84 → 309.30] it was ink last week yeah god it feels like long we covered that too we uh it actually wasn't we
[309.30 → 314.58] it was one of us jarred Santa our managing editor he was like Adam do you see this yet and I think
[314.58 → 320.34] uh Andrew I think Kelly's using ink um he was an early adopter showed me this like I think a month
[320.34 → 325.02] back but I think you guys just released then you have like some earlier version of ink though that was
[325.02 → 335.40] like responsive we had an uh so ink is uh ink is like foundation but for emails um we had about a
[335.40 → 340.76] year ago almost a year ago uh we developed some basically responsive email templates just some
[340.76 → 346.04] some basic responsive template files uh that we offered up through our playground we have a
[346.04 → 352.28] playground where we basically just dump like weird interesting code experiments um, but we posted the
[352.28 → 356.40] responsive templates to that, and they've been really, really popular actually over the course of
[356.40 → 362.48] the last about a year I think um and that actually sort of compelled us to create an entire framework
[362.48 → 367.98] out of that uh the templates suffered from a couple big problems one was that since they weren't really
[367.98 → 374.18] frameworkized I guess uh they're a little harder to build your own stuff from scratch they were
[374.18 → 377.90] pretty easy to adapt to whatever purposes you needed, but it was harder to kind of build your own
[377.90 → 384.14] thing uh they also had a huge flaw which is that they didn't work in outlook uh which it turns
[384.14 → 391.52] out is kind of tremendously important for rich emails outlook is still obnoxiously popular and not for us
[391.52 → 398.70] that's good because it's a complete idiot about how it does rich emails' outlook I'm thankful for that
[398.70 → 404.00] though because only half of the people in the jams low weeklies list half of the subscribers we have
[404.00 → 411.32] are all in iOS like nice either an iPhone an iPad or and actually a mac device so we
[411.32 → 418.32] like half of our market is mac that's a that's a phenomenal that's a big win because it's kind of a
[418.32 → 423.82] nightmare to have to support outlook especially if you're doing responsive emails because outlook just
[423.82 → 430.34] doesn't support anything so we had to do a lot of uh a lot of work to get the framework to actually
[430.34 → 436.66] work in outlook, but we did get it to work it actually does work in pretty much every popular
[436.66 → 440.84] email client I think one of the few ones that we really explicitly don't support is lotus so those
[440.84 → 447.90] guys are kind of screwed uh but everybody else we had good to go on our show last
[447.90 → 452.36] week we had he was on talking about uh he was kind of pumping lotus up a little bit he was like you
[452.36 → 456.96] know the email Lotus Notes it kind of sucks, but lotus was notes was really capable of doing some cool
[456.96 → 460.16] things so we got the yin and yang this week we're just bashing lotus apparently
[460.16 → 466.94] yeah it's its an easy target to pick on and I've had to use it before too it's I will to be
[466.94 → 471.86] totally honest I'll give lotus this I'm actually not sure if its email handling is worse than outlooks
[471.86 → 477.48] it might be a little better than outlooks, but it has a pretty small group of users so it does not get
[477.48 → 482.02] a lot of attention yeahs and in some ways though I mean that we've talked about this a few times
[482.02 → 485.80] too they're kind of pioneers right I mean they kind of started to tackle some of this stuff before
[485.80 → 490.68] anyone else was really tackling it so you guys could probably understand well as doing foundation
[490.68 → 494.92] that you run into issues that when you're kind of blazing trails you actually have to figure
[494.92 → 499.20] out how to solve the issues and then the people that come behind you uh they're like the problems
[499.20 → 503.38] are already solved they just put their own spin on those things oh yeah we've we've seen that numerous
[503.38 → 508.82] times there have been a lot of uh a lot of frameworks that have popped up in the wake of foundation
[508.82 → 515.48] uh that in some cases actually started as just straight-up foundation forks uh and then gradually
[515.48 → 520.74] became their own thing which is cool and I mean they do some interesting stuff of their own and
[520.74 → 525.64] we can learn from some of the things that they do and uh it's it must be nice that a lot of the
[525.64 → 530.78] problems are already solved right yeah and that's what we talked about like and maybe you guys can get
[530.78 → 534.52] into this a little bit but um I can't remember off the top of my head right now what we were talking
[534.52 → 538.38] about but when the competitor comes up oh yeah we were talking about Cristiano and Vlad
[538.38 → 545.12] the deployed came up, and they were like their tagline was sucks less than Cristiano and it's like
[545.12 → 550.66] you know that's really taking a shot at somebody who really solved all of your problems that now
[550.66 → 554.94] you're just like you already know the solutions, and you're just making it more efficient and to
[554.94 → 559.48] take a shot like that is to diminish the work that they did to make your life easier at this point
[559.48 → 564.20] and so when those guys come up as foundation you know like you said some are just literally forks of
[564.20 → 567.94] foundation and when they come up, and they start you know advertising as better than
[567.94 → 573.20] foundation then well that's kind of flattering that they're obviously even can you know that
[573.20 → 578.84] you guys are the bane of they're the whole like message of their marketing but at the same
[578.84 → 583.36] time like it's almost like uh biting the hand that feeds you know like you wouldn't be able to do
[583.36 → 589.14] this if we didn't solve the problems for you in the first place yeah there's definitely a degree of
[589.14 → 593.34] that and there's been a couple of times when we've crossed paths with some of the other frameworks
[593.34 → 597.58] and they've kind of I don't want to say they got on our nerves but they kind of got on our nerves
[597.58 → 603.84] and it's like yeah that's that's that's nice, and we're we're glad you're doing your own thing but
[603.84 → 609.52] we're I don't know we're we show some respect young ones kind of or that or we just sort of you know we
[609.52 → 612.92] just sort of like you know play nice and then get off the get off the email or get off phone it's
[612.92 → 619.24] kind of like yeah we're going to destroy that but well since we Andrew you said young ones so let's can we
[619.24 → 623.96] give a perspective on the age of foundation and kind of when it is I know we just are talking
[623.96 → 629.20] about ink and email lotus there, but you know you just kind of talked about frameworks so how old is
[629.20 → 636.54] foundation, so foundation is just over two years old or just about two years old I'm pretty sure I think
[636.54 → 642.40] it came out September 2011 yeah I think it was september 2011 so it's just over two years old now
[642.40 → 649.18] that's version two that that was two years old that was version two yeah versions one actually
[649.18 → 653.60] never saw the light of day we only used it internally here at curb uh and foundation one
[653.60 → 660.80] actually was not responsive um the interesting thing about foundation one and actually foundation's
[660.80 → 666.80] predecessor which was something called the curb coded style guide uh is that the curb coded style guide
[666.80 → 672.02] was actually the uh the genesis of foundation it was also in a lot of ways and I think Mark would
[672.02 → 677.10] probably other mark not this mark different mark would back me up on this uh it was also the genesis
[677.10 → 682.74] of bootstrap uh because bootstrap was actually developed by mark auto who was a designer here
[682.74 → 687.64] at curb when I was when I started and he and I worked on the coded style guide together he went to
[687.64 → 693.50] twitter and created twitter blueprint I didn't know about oh yeah it's there's a whole uh inside baseball
[693.50 → 699.60] thing for this um if yeah is you go back and look at uh the first public release of bootstrap and the
[699.60 → 704.16] first public release of a foundation you'll find that they are extraordinarily similar
[704.16 → 710.40] uh because they came from a very similar they came from the same starting point in fact uh same story
[710.40 → 714.04] with a skeleton which comes up still a little bit now and then which is like an adaptive framework
[714.04 → 721.32] yeah uh skeleton was actually written by a guy named Dave games uh who worked with me on foundation one
[721.32 → 729.82] uh before he left curb and made skeleton uh so it was a whole all three of those frameworks' foundation
[729.82 → 736.16] and skeleton and bootstrap uh in some way or form had their start uh here at curb so we're pretty
[736.16 → 740.38] proud of all that awesome yeah I didn't even know that I mean that's I can imagine you be listening
[740.38 → 744.92] is like whoa I found this out on the change lad that's awesome do you guys say that often is this
[744.92 → 749.82] like we don't say it a lot, and it's we say it a little bit it's kind of its kind of funny because
[749.82 → 755.66] like uh the guy behind uh bootstrap mark auto well there's another guy too uh Jacob uh who works on
[755.66 → 761.42] a lot of JavaScript stuff but uh mark uh we I mean like foundation and bootstrap get compared a lot
[761.42 → 766.92] there are a lot of like articles out there and big you know spreadsheet driven checklists or whatever
[766.92 → 771.18] like what does bootstrap do and what does foundation do and which one would I use or which one is better
[771.18 → 775.80] and most of them end with something along the lines of you know foundation's better for this particular
[775.80 → 778.86] thing and bootstrap's better for this particular thing and everybody thinks we're very
[778.86 → 785.96] confrontational or very I don't know I don't know what the word is angry and violent about the
[785.96 → 790.20] whole thing the funny thing actually is that uh mark auto and I are actually pretty good friends
[790.20 → 798.10] we like play star craft and stuff now, and then he's terrible um but uh we've I mean we've we've kept in
[798.10 → 801.28] touch this whole the whole time for some of the stuff we've been to each other's like launch
[801.28 → 805.78] parties and that kind of stuff so it's at the end of the day I mean there 's's definitely like a
[805.78 → 809.78] competitive angle to some of it and i I'm certainly not going to say that we don't want to beat bootstrap
[809.78 → 815.24] because we do um, but it's at least a reasonably friendly competition it's at least a know
[815.24 → 820.52] everybody wants to make better tools and make it easier to make better stuff so let's all just
[820.52 → 826.04] do our thing and it'll, it'll shake out in the end right I mean it keeps you guys moving too right
[826.04 → 830.16] if it was only you guys then we might not have seen five major releases in the last two years
[830.16 → 835.06] that's true it has definitely kept us moving and we stay pretty aggressive with
[835.06 → 839.78] foundation in fact we already have tentative dates floating around for the next version of foundation
[839.78 → 845.84] so we don't ever want to stop well let's talk a little bit about foundation five so when foundation
[845.84 → 849.96] four came out I mean I personally remember I was like okay a lot of stuff at that point kind of got
[849.96 → 855.28] rolled into foundation um itself I think was that four or three where all the JavaScript stuff got
[855.28 → 861.02] rolled into it, I guess that was four and I remember thinking like okay that that was a pretty
[861.02 → 865.44] big milestone and then foundation five comes around and I'm thinking to myself you know wonder what you
[865.44 → 870.64] guys are going to really be focusing on here and reading the blog post that we'll link to in the
[870.64 → 875.00] show notes that seems like one of the big focuses that you guys are putting into foundation five is
[875.00 → 880.10] speed yeah am I off base there is that right no that's I think that's I'd say that's pretty much the
[880.10 → 885.26] thesis of or the need for speed which one is it speed baby speed we feel
[885.26 → 889.38] the need tell us a little bit about that what is the uh yeah what's the impetus behind that and
[889.38 → 896.56] and um you know what does that mean for the user of foundation five sure so we've with
[896.56 → 901.18] each release of foundation we've tried to have like sort of an overarching you know what's the what's
[901.18 → 904.46] the goal of this release we don't want to just bump the number because we like to bump the number
[904.46 → 910.86] I mean we do like to bump the number um, but we want there to be some sort of reason uh like you were
[910.86 → 917.22] talking about like it was four was uh there were a few big pushes with four one was that we did
[917.22 → 921.24] better integrate all the JavaScript stuff we did a lot of work to actually have the JavaScript
[921.24 → 927.52] components be really integral to the framework uh we also four was uh we had that whole move towards
[927.52 → 932.74] mobile first in foundation four so that was huge that was a big change foundation four was
[932.74 → 936.70] we switched everything to be totally to be everything to be mobile first and that was
[936.70 → 941.32] some of that was driven actually because uh Luke roblewski who literally wrote the book mobile
[941.32 → 946.92] first and has been on the mobile force warpath forever uh is an advisor for zero uh and over the
[946.92 → 953.40] course of a bunch of lunches and stuff he sort of uh bludgeoned uh me into making foundation mobile
[953.40 → 957.60] first which I think was actually it was a good move it was an it was a smart move uh, but he had to
[957.60 → 963.18] really work at it for a little while so with foundation five the thing that we're seeing now is
[963.18 → 967.46] so frameworks have been around for a little while now and there's quite a few of them at this point
[967.46 → 971.30] I mean everybody's seems like everybody's trying to get in the game now like Yahoo's got their own
[971.30 → 975.76] thing coming out that's even separate from GUI they've got pure is them right yeah is yahoo
[975.76 → 981.16] um so they've got pure I think google's even maybe trying to get in the game they've been floating
[981.16 → 985.96] some sort of weird stuff around like they're going to get into this the framework space so everybody's
[985.96 → 990.66] kind of doing their thing, and it's becoming a more mature uh field I guess you could say
[990.66 → 996.28] and so now what we're running up against is that we know at least a little bit of how to do
[996.28 → 1000.80] responsive design, and we know a little bit about how how these frameworks ought to work and how
[1000.80 → 1007.98] they ought to help you build stuff what we haven't seen enough of really is optimization or uh speed
[1007.98 → 1016.60] sort of across the idea of a framework um we want foundation to be fast essentially in a lot of
[1016.60 → 1020.64] different ways not just in terms of how quickly it can be delivered, although we're doing work
[1020.64 → 1025.02] there too or how quickly you know pages can load or what we can do to optimize, although we've done
[1025.02 → 1030.44] some I think pretty interesting stuff in that vein and I can talk about that, but we want
[1030.44 → 1035.38] foundation five to be faster for people to learn we want foundation five to be faster for people to
[1035.38 → 1039.82] actually build with to actually write the code we want that to be faster uh we want it to be faster
[1039.82 → 1046.74] uh when it performs and be more performant uh because we think that since the tools exist now and the
[1046.74 → 1053.42] tools are reasonably well-defined uh what we can really do with foundation uh to help this ecosystem
[1053.42 → 1059.86] along is just lower the barrier to entry even more uh in as much as we can get more people up to speed
[1059.86 → 1065.64] on foundation we can get more people up to speed on uh no pun intended by the way um more people up to
[1065.64 → 1071.56] speed on uh how they're actually going to build stuff and help them build things more quickly uh just so that
[1071.56 → 1076.40] we can have more frankly just have more responsive stuff built and have responsive stuff that's built
[1076.40 → 1082.32] well also be built quickly because the pace of this stuff doesn't slow down like the pace of
[1082.32 → 1088.58] web development especially is preposterously fast I mean we're on foundation five now that's only in
[1088.58 → 1094.78] the space of two years responsive design at all is only about three years old just over three years old
[1094.78 → 1099.40] so this is not like a know we haven't been doing this for like decades or anything like that like
[1099.40 → 1105.22] this has been a little while in fact I realized this when I was uh I was doing a little bit of
[1105.22 → 1110.04] research the other day I actually didn't even quite realize but CSS at all like CSS we're all like
[1110.04 → 1115.60] super used to CSS, and it's like oh CSS obviously we build everything CSS CSS is only about 13 years old
[1115.60 → 1121.98] yeah say 12 yeah like it's its just not that old like I can think back to when very easily when CSS
[1121.98 → 1125.86] came out, and it's like it feels like we've been doing it forever, but we haven't so everything
[1125.86 → 1129.54] I can remember the days when it was still being debated like should we use tables or should we use
[1129.54 → 1136.04] CSS to like style things and like you know Erin Meyer had written some books on it, and he's
[1136.04 → 1140.96] like you know I can remember those days it wasn't very long ago you're right I mean like this is still
[1140.96 → 1146.34] like it's still a baby you know it's still an adolescent barely well it speaks to the kind of
[1146.34 → 1150.58] the industry you can go back and read a lot of those books, and they don't feel outdated now the
[1150.58 → 1156.16] the like obviously the concepts seem outdated because we know better but like if you're new to
[1156.16 → 1160.20] the industry and I've you've all dealt with this right like somebody a friend of yours that
[1160.20 → 1163.54] wants to start learning this stuff is new to the industry, and they go pick up one of these books
[1163.54 → 1168.52] and they're like yeah it's booking from 2004 uh seems good and the information all seems good, and you're
[1168.52 → 1174.40] telling them like you're reading stuff that nobody cares about anymore like in this industry 10 years
[1174.40 → 1180.90] is like uh eons you know right and yeah so it so we're kind of figuring if things are moving this
[1180.90 → 1187.42] quickly and I mean at this point it's like every six months or less like the entire motif of web design
[1187.42 → 1193.68] the entire like approach to how some of this stuff works might change uh we want people to be able to do
[1193.68 → 1198.66] things more quickly and build things more quickly uh so that they can actually get something done before
[1198.66 → 1205.18] everything just passes them by um and that goes double for us because we i would hazard a
[1205.18 → 1209.56] guess that we are probably one of the most prolific shops of writing stuff in foundation obviously because
[1209.56 → 1215.16] it's what we write everything in um, but we do all of our client work in foundation we have anywhere from
[1215.16 → 1221.30] 12 to 16 or so clients at a time um so we do all of our client work in foundation we do all of our
[1221.30 → 1225.64] projects in foundation all of our sites all of our properties are written with foundation or being
[1225.64 → 1230.96] written with foundation uh so we want it to be fast because we have to do it all the time, and we want
[1230.96 → 1237.28] to be more efficient so you say that it's not just the speed of you know optimizing the code itself
[1237.28 → 1242.16] but it's also the speed of learning the speed of you know how long it takes to get up and up and
[1242.16 → 1246.20] running with it so what does that mean for the user like somebody that's familiar with foundation 4
[1246.20 → 1251.92] how will foundation 5 be different for them sure so foundation 5 actually shouldn't be
[1251.92 → 1257.38] that much different from foundation 4 from a user's perspective uh all the naming
[1257.38 → 1264.24] of our JavaScript files and our SAS variables there's very little that changed on that front uh
[1264.24 → 1271.34] the only thing that has changed is the way that you can selectively import parts of foundation uh has
[1271.34 → 1276.28] changed so it's easier to pick and pull what you need from foundation so if you don't need everything
[1276.28 → 1281.68] you don't have to use everything so that's that's probably the biggest point we also have some
[1281.68 → 1287.28] uh additional new components in foundation 5 which we'll talk about a little bit later
[1287.28 → 1293.02] in this program right, but we've been uh I mean as far as like getting people up to speed
[1293.02 → 1298.54] on stuff like we're rewriting all the documentation uh in fact we're in the middle of that right now
[1298.54 → 1304.20] which is going to bring us right up to the wire yeah um you got a week what are you doing wasting
[1304.20 → 1308.70] time on this show yeah I know right we're thinking about the docs that we still have to write
[1308.70 → 1314.26] while we talk to you um, but we're rewriting all the documentation so that that'll be it's going
[1314.26 → 1319.70] to have a lot more uh examples a lot more code stuff that you can pull from uh and just drop right
[1319.70 → 1324.38] into whatever you're working on uh it's its much more it's better organized it's much more verbose
[1324.38 → 1327.52] than what we had before at least as far as just example code that was some feedback that we
[1327.52 → 1331.52] consistently got was you guys describe a lot of the things that's going on in here I want to
[1331.52 → 1335.96] actually just like see it and be able to grab it and drop it um so we're doing a lot of work
[1335.96 → 1342.98] there that's a neat concept too we when we had um remind me of his luck I believe semantic UI
[1342.98 → 1349.60] oh yeah that was a big component of what he talked about with semantic UI was that you know he wanted
[1349.60 → 1354.60] it to be easily to grab like one component or one if you just wanted the grid you can use the grid
[1354.60 → 1359.24] only or if you wanted certain components you can easily pull that, and it didn't have the
[1359.24 → 1365.44] JavaScript and dependencies were separate well enough styles and all that stuff was very um
[1365.44 → 1370.90] compartmentalized really well yeah, and we've done a lot of work for that for foundation five I know
[1370.90 → 1375.58] we've we've tried to make it as fast and easy as possible to say you want to pull in just a
[1375.58 → 1378.88] particular thing I think we even manage all the dependencies and stuff for you now don't we
[1378.88 → 1386.46] yeah is that true for the like what do you guys prefer do you guys prefer the I don't know how to
[1386.46 → 1390.30] describe the standalone installation of foundation or like for a let's say a rails project you
[1390.30 → 1395.44] prefer the gem installation that you guys are using for the rails' installation we use the gym
[1395.44 → 1400.14] just because the asset pipeline takes care of bringing in all the JavaScript and the SAS
[1400.14 → 1407.34] files for us uh but for non-rails projects uh we've been using bower a lot recently uh makes it
[1407.34 → 1413.20] really easy to grab the latest version of uh foundation this is something new we're uh paying
[1413.20 → 1420.22] more attention to with foundation five so but definitely the rails' gym uh is the way to go
[1420.22 → 1425.84] especially so that we don't have uh our designers go in and accidentally muck up the original uh
[1425.84 → 1433.16] foundation or uh JavaScript files which makes upgrading you know potential problem so well that's what i
[1433.16 → 1437.30] kind of what I was going to get into a little bit is the upgrade path so a lot of people who use
[1437.30 → 1441.66] so like specifically we're talking about rails projects or just general people who are using you know
[1441.66 → 1446.36] ruby gems or bundler you know however they're using it they're used to just being able to you know
[1446.36 → 1451.62] bundle update and for the most part it just works and is do you think that that's you said that
[1451.62 → 1456.38] foundation five should be pretty similar to foundation four so is there many many changes that need to
[1456.38 → 1460.80] happen for the upgrade path if you're is you're using like a standard installation so in terms of
[1460.80 → 1466.88] SAS variables no we have introduced some new SAS variables for defining the new uh breakpoints
[1466.88 → 1473.10] that are used for the media queries uh but for the JavaScript we've actually created a shim that
[1473.10 → 1479.62] will include with up until foundation 5.1 that will take care of uh we had a few plugins I'm trying to
[1479.62 → 1485.78] think joyride was one of them where we used camel case to name some variables, and it wasn't consistent
[1485.78 → 1492.12] where we were using underscores everywhere else so we've made everything consistent uh in that sense uh
[1492.12 → 1496.48] but we have a shim that will go through it and uh adjust if you're using the wrong variable names
[1496.48 → 1502.32] it'll adjust the variables for you uh, and we'll include that it will include that up until 5.1 just
[1502.32 → 1508.34] so that if you're using 5.0 things that aren't gonna break right away right and then at 5.1 it'll
[1508.34 → 1512.66] break, and it's up to them to go back and fix all their junk yes, but we have some deprecation notices
[1512.66 → 1517.32] so if you're using foundation you'll actually see in your chrome console if you're using something that
[1517.32 → 1524.34] is deprecated so if you don't see any warnings 5.1 should be just as trivial of an upgrade as 5.0 is
[1524.34 → 1529.56] right and I know when we went from uh so when we went from foundation 3 to foundation 4 we changed a
[1529.56 → 1534.98] lot of just markup syntax uh some of that was because we went mobile first some of that was
[1534.98 → 1539.36] because we just needed to rethink how we were doing some of this stuff um, so there were some
[1539.36 → 1544.02] pretty large philosophical changes I guess in that one there's foundation 4 to 5 has a lot less
[1544.02 → 1549.34] big philosophical changes I guess to it that are in that kind of vein so I know things like the
[1549.34 → 1554.94] grid syntax and that kind of stuff you can leave unchanged uh you'll have some in foundation 5 you'll
[1554.94 → 1559.28] have some more toys to play with um, but you shouldn't have to go through all your markup and
[1559.28 → 1563.90] make a lot of big stringent changes we're going to have a migration guide for 4 to 5 but
[1563.90 → 1568.34] it should be pretty straightforward it shouldn't be like the uh the 3 to 4 uh I don't know if I can
[1568.34 → 1572.26] call it a debacle, but there was at least a decent amount of legwork that had to go into upgrading
[1572.26 → 1576.90] from 3 to 4 4 to 5 should be pretty straightforward yeah now you guys I don't know if you actually
[1576.90 → 1581.34] follow semantic versioning but when you do major changes like that from 3 to 4 it's
[1581.34 → 1585.56] perfectly acceptable to break right it's perfectly acceptable for it not to work the same or to have
[1585.56 → 1591.48] some pains with upgrading but what's interesting to me is for something like foundation I think a lot
[1591.48 → 1596.00] of people are okay with that with other tools but for something like foundation it's just like
[1596.00 → 1601.90] you constantly want the newest because it feels like the newest is leveraging like modern technologies
[1601.90 → 1607.52] so much better than the previous version so I wonder why people aren't as forgiving with foundation
[1607.52 → 1611.26] or something like that when it's a major version change as they would be with another project
[1611.26 → 1617.08] well we have a lot of our uh a lot of people using foundation are using it for client work so
[1617.08 → 1622.38] if somebody is working with foundation part way through, and they encounter an issue, and we need to
[1622.38 → 1628.38] push out fixes for that we want our customers or our users feeling very comfortable just upgrading
[1628.38 → 1633.66] anytime so that they can get the latest and greatest code so you're right we definitely can make
[1633.66 → 1639.68] breaking changes if we absolutely need to but if you don't have to, or you can like to find a way to it
[1639.68 → 1645.44] yeah we it just if i I've been in the position where like even like in rails projects if you upgrade a gem
[1645.44 → 1652.42] and it's a new major version, and it breaks things it's acceptable, but it's still annoying and I don't know
[1652.42 → 1658.82] I always have the I don't know it just gets really annoying especially if I don't have time to I need to upgrade but
[1658.82 → 1665.32] it just yeah yeah it's like a's a double-edged sword right when it fixes a problem that you had to work
[1665.32 → 1670.02] around before, but it breaks something that you're depending on now so it's kind of like you don't know
[1670.02 → 1673.40] whether I should upgrade and spend the time or just still deal with the problem that I'm having now
[1673.40 → 1680.02] yeah exactly I feel like i almost i I almost don't trust the authors as much if I keep making breaking changes
[1680.02 → 1687.14] I'm more inclined to just want to leave uh not use a particular gym anymore if it changes every time
[1687.14 → 1692.36] I bump major versions I was going to say especially you know we talked a little bit earlier like the
[1692.36 → 1697.92] competition level that you're facing in the framework world you know that's the world you're playing in so
[1697.92 → 1703.52] the harder you make the upgrade path or the more bumpy it might be I mean you're going to have some
[1703.52 → 1708.32] changes obviously with the know like Andrew said that are acceptable but if you can minimize that
[1708.32 → 1713.68] you probably stand a chance of like shiny objects not getting their attention right right right and
[1713.68 → 1719.14] it's yeah it's totally a's totally a two-edged sword because we can't, we can't sit on our laurels
[1719.14 → 1723.52] and just like do you know teeny tiny little changes that don't really impact anything because we need to
[1723.52 → 1730.30] keep making big sweeping changes in order to stay ahead of any kind of competition um but anytime we
[1730.30 → 1736.00] do that yeah we risk I mean it's a funnel right everybody who uses a current version of
[1736.00 → 1740.96] foundation when the new one comes out everybody wants to use it we get it's in some cases it's
[1740.96 → 1748.84] it's really sort of aggravating we get so many requests for uh for people who want to use foundation
[1748.84 → 1756.06] for with ancient versions of i.e. like i.e. 7 or i.e. 8 which we don't actually technically support
[1756.06 → 1762.24] but they the funny thing is we actually kept foundation 3 around specifically because foundation
[1762.24 → 1767.72] 3 actually worked in i.e. 8 so if people needed i.e. 8 support we were like look we still have like this
[1767.72 → 1772.62] supported like it was good code like it works well like you can use foundation 3 and what we always
[1772.62 → 1776.92] get is but I don't want to use foundation 3 I want to use foundation 4 I want shiny new exactly i
[1776.92 → 1782.42] want the shiny new thing I just want that to work in i.e. 8, and it's like it is doesn't like it doesn't
[1782.42 → 1787.50] work there like I don't know what to tell you it's like you can use three, or you can try to make
[1787.50 → 1792.98] for work, and it's going to be a world of pain but they all want the shiny new thing they all
[1792.98 → 1796.44] want that to work as far back as they can and I know we're going to get it with foundation 5
[1796.44 → 1801.96] is we'll get can I have foundation 5 that works in i.e. 7 can I have foundation 5 that works in i.e. 8
[1801.96 → 1809.22] and we'll continue to toe the line of well no yeah I mean you're pushing the web forward here right i
[1809.22 → 1813.72] mean that's the point is as long as tools continue to coddle the old web then it doesn't go forward
[1813.72 → 1819.76] right, and it's I never understand that that debate they're always boggling my mind it's its it's a
[1819.76 → 1825.10] difficult it's not an easy decision for us, so this is actually this is the thing that's actually come
[1825.10 → 1829.74] up a lot just with building a framework at all like this is that if you're trying to stay ahead
[1829.74 → 1834.30] of stuff you have to make a lot of decisions where there's not a lot of precedent to fall back on
[1834.30 → 1839.02] so we can't really look around and go oh well this framework decided to drop law and this framework
[1839.02 → 1843.10] decided to keep support for this we kind of have to just forge our own path I guess and then deal
[1843.10 → 1848.12] with whatever the consequences of that are which can be really, really awesome, and it feels
[1848.12 → 1854.00] like you're you know like striding atop the world just you know dominating stuff, and it feels great
[1854.00 → 1859.26] sometimes and then sometimes it's really frustrating like dropping support for i.e. 8 was a difficult
[1859.26 → 1866.18] decision because we do have a lot of people who really want or really need support for that kind
[1866.18 → 1870.32] of browser because they still cater to you know large enterprise they want to use it for
[1870.32 → 1875.58] whatever other kind of stuff they've got going on that necessitates having that kind of support
[1875.58 → 1884.96] but we can't, you know we can't actually make the framework do what we're what we needed to do
[1884.96 → 1890.06] in order for in order to support those actual browsers like we couldn't do mobile first really
[1890.06 → 1894.00] and support i.e. 8 that was actually the killer with i.e. 8 is that i.e. 8 doesn't support media queries
[1894.00 → 1899.46] and for mobile first to work you have to have media queries that kick in on larger and larger screens
[1899.46 → 1904.62] and it's just not going to happen in i.e. 8 so we couldn't, we just couldn't make it work like when we
[1904.62 → 1910.80] went from foundation uh two to foundation three we dropped support for i.e. 7 because i.e. 7 doesn't support
[1910.80 → 1917.24] the uh the border box uh box sizing model, and we use that for literally everything so we had to drop
[1917.24 → 1921.40] support for that we and we got complaints about that, and we'll get complaints about eight, and we'll keep
[1921.40 → 1927.98] getting it um, but it's I mean i I feel bad when someone's like I really want to use foundation
[1927.98 → 1934.42] but I have to support i.e. 8, and it's like well i I wish I could help you but i just oh well can't right
[1934.42 → 1942.84] it's like I wish there was something we could do, but there's just not so sorry uh I feel their I feel
[1942.84 → 1948.28] their pain because we've had to do that too, but that's just the way it goes we're going to pause for just
[1948.28 → 1952.12] a second we'll come back we're going to talk I think we're going to talk a little bit about responsive
[1952.12 → 1956.34] because you kind of touched a bit on that and I think I want to talk a bit about you know what
[1956.34 → 1960.32] you're doing around that with foundation but let's pause for a minute and give a shout-out to our
[1960.32 → 1968.24] uh sponsor number two top towel it's uh they're an awesome sponsor of ours and for those of you who
[1968.24 → 1974.02] are freelancing out there would like to be testing out a freelancing option or even trying out
[1974.02 → 1977.88] you know if you get a full-time position, and you're you're like wow i maybe I would like to
[1977.88 → 1983.40] freelance maybe I can, you know do some fun things with like node or rails or some cool edgy new
[1983.40 → 1988.08] technology, but you don't want to quit your day job so you want to work kind of in a no risk kind of
[1988.08 → 1993.20] freelance like project uh top talk can enable you to do that they're looking for some elite uh senior
[1993.20 → 2000.28] engineers you can work on special projects with companies like Airbnb artsy video and many others
[2000.28 → 2005.62] work remotely on a beach or anywhere in the world it doesn't really matter uh and I read a lot of
[2005.62 → 2010.16] twitter bios out there that say like I do you know this thing you know like whether it's java or
[2010.16 → 2014.98] something else during the day and then at night I'm hacking on or at night I'm a node hacker at night I'm
[2014.98 → 2019.62] a rails hacker whatever well that nighttime thing you can kind of do with top down to get started you
[2019.62 → 2024.68] can head to top.com slash developer and click join the best and because they want to work with only
[2024.68 → 2029.02] the best senior engineers out there they've got a well-thought-out four-stage screening process
[2029.02 → 2033.70] uh it involves a personal Skype conversation to get you started to introduce you to who top
[2033.70 → 2038.38] tile is what their mission is and see if you're a fit and from end to end the entire screening process
[2038.38 → 2044.98] includes an English speaking test a time algorithm test a quick technical interview with top core
[2044.98 → 2050.56] engineers as well as a test project and once you kind of gotten through that that process there the
[2050.56 → 2054.94] sky's the limit uh and if you think you have what it takes to head to top.com slash developer
[2054.94 → 2060.18] right now to get started and tell them the change log sent you and last week when I mentioned this i
[2060.18 → 2064.86] did invite some people to give me some feedback, and we did get a little bit of feedback there which is
[2064.86 → 2068.42] great because it seems that some people are really enjoying their experience with top tile so
[2068.42 → 2074.56] you can email me Adam at the change law.com I want to hear what your experience is like go to
[2074.56 → 2081.66] top tile.com slash developer to get started click the button that says join the best so I know that
[2081.66 → 2087.42] uh um we were talking a little bit about uh responsive web design before the break here
[2087.42 → 2092.52] um Angie did you have any notes on that I know we kind of haven't really dove deeply into it yet
[2092.52 → 2097.64] well I mean obviously everything foundation is responsive and I think ink the same way but
[2097.64 → 2101.30] what I would like to kind of get into because I mean if you're is you're here you're familiar
[2101.30 → 2105.70] with if you've is you're using foundation at this point you're familiar with responsive
[2105.70 → 2112.44] just the idea of responsiveness I'd like to kind of get into foundation five and what's new with
[2112.44 → 2115.80] foundation five and subsequently how you guys have altered the way that you're dealing you know
[2115.80 → 2120.26] you said that there's some different um variables around your break points and stuff like that
[2120.26 → 2124.24] so why don't we talk a little bit about just what's new with foundation five and how it's
[2124.24 → 2130.40] changing how you're dealing with things like responsiveness and stuff sure I think the I'll turn it over
[2130.40 → 2133.56] to mark here to talk about it but I think that probably the biggest thing that we've or at least
[2133.56 → 2137.28] the one that we're we're talking about the most because we're actually pretty excited about it is
[2137.28 → 2142.96] a plugin of ours called interchange uh that we actually we introduced the plugin in foundation
[2142.96 → 2148.66] four but in one particular case and foundation five we've changed it uh pretty dramatically to do a lot
[2148.66 → 2154.18] of really cool stuff, but that's a big one for addressing responsive I'll let mark talk about it
[2154.18 → 2160.88] though oh yeah so interchange that's that's probably one of the bigger components of uh foundation five and
[2160.88 → 2167.54] we've taken the idea of just selectively loading uh an image based on a media query in your device
[2167.54 → 2174.18] since media queries uh we use some JavaScript to do this but since media queries inherently don't allow
[2174.18 → 2179.66] you to prevent an image from being downloaded on a device uh interchange goes in with some JavaScript
[2179.66 → 2185.98] to make that happen so that you don't unnecessarily download multiple images on a small device so we've
[2185.98 → 2193.88] taken the idea uh over to HTML content so we can actually load in external HTML content with
[2193.88 → 2201.30] interchange starting in foundation five so if you have lots of content that may include images and
[2201.30 → 2208.66] all sorts of stuff that is not applicable to a mobile device you could now use interchange to prevent
[2208.66 → 2213.98] that content from ever being pulled down to your device in the first place, so this is going to make
[2213.98 → 2219.14] your websites feel just a little bit faster um so the use case that I like to throw
[2219.14 → 2222.58] out for this and this actually this came from uh from Luke again this came from Luke Pulaski
[2222.58 → 2228.58] um was that if you imagine like on a because if you build things mobile first with foundation and
[2228.58 → 2232.32] foundation is built mobile first so it's obviously encouraged to build things mobile first
[2232.32 → 2237.80] if you're doing a page for example that has like uh has a map or has directions or something like that
[2237.80 → 2241.90] on a mobile device you may just want to load an image you may just want to load a simple
[2241.90 → 2246.68] single you know mobile optimized image for the location, and you may want to have like a link
[2246.68 → 2251.88] to fire up somebody's native mapping application whereas on a desktop you may want to include like
[2251.88 → 2258.74] a full-on interactive google map now in the past there hasn't really been a way on the client side
[2258.74 → 2263.38] or at least you know without delving into back-end device profiling or doing some sort of like HT access
[2263.38 → 2269.74] hackery to say on mobile devices I only want to load this image on larger devices I want to pull in
[2269.74 → 2273.52] you know a full-on google map something that has a lot of assets a lot of requests something that's
[2273.52 → 2279.46] going to be very heavy and taxing on the device um but with interchange now uh in foundation five I can
[2279.46 → 2284.76] actually say for you know for a given media query match for something that's like you know only a
[2284.76 → 2290.38] small device essentially load this particular partial which just includes an image then if we
[2290.38 → 2295.36] detect that this is a larger device this is device that has a larger screen has you know is presumably
[2295.36 → 2300.34] more capable of dealing with a larger request go ahead and load in a different partial load in a
[2300.34 → 2305.14] different HTML section that has the know the actual interactive google map something like that
[2305.14 → 2311.52] so we're taking the concept that we uh that we uh introduced with interchange in foundation four
[2311.52 → 2315.84] which was just loading the right image for the right device now we want to be able to load the
[2315.84 → 2322.76] right just stuff for the right device which has been like a huge thorn in the side of responsive design
[2322.76 → 2327.80] for a long time because it was most obvious with images for a long time because unless you were doing
[2327.80 → 2332.50] stuff on the back end which most people who work with foundation or build stuff with foundation a lot
[2332.50 → 2336.60] of those people don't really actually have any access even to the back end or even really care about
[2336.60 → 2341.28] the back end they're mostly working on the front end there was no way without dealing with the back
[2341.28 → 2346.20] end to say you know I only want to load the right asset for the right type of device so with
[2346.20 → 2352.74] interchange we tried to do that for images um, but this has been a huge problem and mobile devices are
[2352.74 → 2359.20] in some ways they're they're kind of stupid uh which is that if you do want to load the
[2359.20 → 2363.66] right asset you can't even do it by like hiding and showing the right assets because mobile devices
[2363.66 → 2368.66] will load every piece of media that's on that page whether it's shown or not they don't try to do
[2368.66 → 2374.86] anything smart about that they're starting to I think like the dev builds of chrome on android
[2374.86 → 2379.60] or something along those lines will actually try to defer loading media if they're is it detects that
[2379.60 → 2383.58] they're hidden by default, but that's going to be a while till that's any kind of standard and we
[2383.58 → 2388.72] want to just get out ahead of that yeah so interchange is uh one of the larger components
[2388.72 → 2394.22] of foundation five that we've added and the ability to just uh load arbitrary sections of uh arbitrary
[2394.22 → 2399.34] chunks of HTML depending on a certain media query we've tried to make that as straightforward and
[2399.34 → 2403.30] easy for a front end developer as we possibly can, it's actually pretty simple to deal with
[2403.30 → 2408.74] so that was a big one and as this is a funny thing too because if you look at like historically
[2408.74 → 2413.38] speaking with mobile devices as there's been a kind of few things that have happened that have
[2413.38 → 2418.66] contributed ultimately to people paying more money for data which is the data has been become
[2418.66 → 2424.76] increasingly faster right you have access to a much just a much faster connection than you
[2424.76 → 2431.46] used to have so subsequently we've become comfortable with like more like making devices download more
[2431.46 → 2436.40] assets because we're not afraid of them sitting there waiting and then because of you know optimizing
[2436.40 → 2440.36] these assets we'd actually download twice as much because we give we download the mobile version
[2440.36 → 2446.30] and we download the desktop version so all of that contributes to ultimately your little phone in
[2446.30 → 2451.38] your pocket costing you a lot more money and with all the unlimited data plans going away it's just like
[2451.38 → 2456.46] I mean it just it's mind-boggling how the consumer is the one that's taking the hit for all of this
[2456.46 → 2462.96] stuff so interchange kind of in an off way aids that right because you don't have to download all of
[2462.96 → 2467.26] the content that is on the page just because you're trying to show a mobile optimized version
[2467.26 → 2471.80] of something right and I mean, and it's its good for you too as the person who offers the site I mean
[2471.80 → 2475.30] obviously it's good for consumers because they're going to have to wait less they're going to have to pay
[2475.30 → 2479.86] less they're gonna use up less of their data which I think it's actually kind of funny like if you don't
[2479.86 → 2484.30] have an unlimited data plan which a lot of people don't anymore if you have like a newer phone like an
[2484.30 → 2490.74] LTE enabled phone like you can burn through your data in less than five minutes if you're trying
[2490.74 → 2496.58] like you can just I mean I could fire up Netflix or whatever and just start playing you know some
[2496.58 → 2500.36] sort of HD episode of something, and it's going to look great on my phone, and it'll come down in LTE
[2500.36 → 2506.72] speed, and it'll burn through 200 legs in like four minutes yeah it's crazy I did something like that i
[2506.72 → 2511.60] don't remember exactly what it was but I burnt through I was driving from Texas to Nashville where I live at
[2511.60 → 2516.84] and I went through like two and a half gigs on the trip and I was just like you know I don't even
[2516.84 → 2521.20] really it was like streaming audio and just doing different things and like with just data consumption
[2521.20 → 2525.58] I get home, and it's like you've reached 60 percent of your plans like oh my gosh like how did this
[2525.58 → 2531.72] happen it goes so fast, but it's still and even with the speed of like LTE or the speed of like
[2531.72 → 2538.06] newer devices and newer networks you still if you're is you're throwing the weight of every kind of
[2538.06 → 2542.24] asset and every kind of all the stuff that you need onto mobile devices and not really optimizing
[2542.24 → 2547.64] for it people are still going to run into just slow to load pages like the latency is still not
[2547.64 → 2556.98] good the bandwidth is still on average in the U.S. mobile bandwidth is about a fourth or a fourth to a
[2556.98 → 2564.22] sixth so it's about 15 20 15 percent as fast as the average like wired or uh or home Wi-Fi speed
[2564.22 → 2571.64] so it's still it's faster, but it's not like it's crazy fast it's still quite a bit slower than
[2571.64 → 2575.14] other kinds of connections are, and the latency is still pretty high and that's just in the U.S. which
[2575.14 → 2581.00] actually does reasonably well we're not on top of the world by any means um, but we do okay in other
[2581.00 → 2586.34] countries especially in like uh, uh Africa, or you know Eastern Europe any of those kinds of areas or a
[2586.34 → 2593.22] lot of parts of Asia it's much, much slower uh, and you have to contend with much uh much more
[2593.22 → 2599.66] demanding constraints so it's its getting better, but it's still you still have to optimize things
[2599.66 → 2605.30] and there hasn't been a way to easily optimize a responsive site uh for front-end developers we
[2605.30 → 2612.08] would say until now well we also uh that brings up I guess another good point is uh it as even a
[2612.08 → 2617.94] company who's hosting all this large content uh most likely uh we're using Amazon s3 to store
[2617.94 → 2624.42] your images if you're all your users are downloading these large images from your device I mean every
[2624.42 → 2629.68] time somebody downloads an image that they don't look at you're paying the bill for them to do that
[2629.68 → 2637.00] on that note I mean something we covered recently and for subscribers of the change all weekly you'll
[2637.00 → 2644.28] probably remember this we I think it was in issue 13 actually so last the most recent issue we
[2644.28 → 2649.76] talked about pre-browsing which is kind of like a different topic but in the same vein um you know
[2649.76 → 2655.66] what are you guys thoughts on pre-browsing like using the REL tag prefetch to kind of pre-render
[2655.66 → 2661.36] or kind of go prefetch a URL it doesn't quite change you know what interchange is doing which is choosing
[2661.36 → 2667.82] which asset to pull or and whatnot but if it's still in this like front-end optimization I guess even
[2667.82 → 2673.84] somewhat anticipation of what the user wants you know I thought when uh when pre-fetching or the
[2673.84 → 2678.52] know the REL tag for it or whatever became really available to use in any kind of browser which was
[2678.52 → 2683.76] not terribly long ago that was maybe a year ago it was not particularly long ago that it became
[2683.76 → 2691.44] available at all it's a really cool idea that I think has a lot of maybe unexpected ramifications
[2691.44 → 2699.20] and it's a little harder to use than it might seem at first glance I think it's great from a user
[2699.20 → 2703.64] perspective from a user experience perspective I think it's great if you can do it right if you can get it
[2703.64 → 2710.50] right because if you're on a page, and we know with some uh some certainty where you're going
[2710.50 → 2714.54] to go next if that can already be loaded then obviously it's great to click a link and just
[2714.54 → 2719.96] see the next page and not wait for anything that's awesome I almost feel like it could be kind of i
[2719.96 → 2724.12] don't want to deviate the top of if it's kind of a neat thing to think about like if you were hovering
[2724.12 → 2728.76] a particular target you know like the mouse or the and I guess on a touch device this doesn't quite
[2728.76 → 2732.62] apply because you don't really have the hover effect, but you know I mean you kind of lose it there
[2732.62 → 2737.28] which does kind of suck but if you're on a desktop you know you're hovering a particular element you
[2737.28 → 2741.50] might anticipate they're going to click the button and if they do, you can kind of prefetch maybe
[2741.50 → 2746.58] temporarily and start pulling down some assets and if they don't then you know kind of kill
[2746.58 → 2751.46] prefetch so maybe dynamically apply the real tag I just wanted to know what your thoughts are on it
[2751.46 → 2757.92] because it's all around this speed you know your need for speed so the cool thing about it is
[2757.92 → 2762.52] yeah it's like an instance like that where you can either predict based on their behaviour
[2762.52 → 2766.56] where they're probably going to go next then do it that way or uh what we've actually what we've
[2766.56 → 2770.70] actually even tried to do ourselves is to look at analytics and just go okay if they're on this page
[2770.70 → 2776.02] most of the time the next place they go is here so we'll actually try to we'll try to selectively
[2776.02 → 2784.26] apply the prefetch uh property to that page now the downside is that I mean on your laptop at
[2784.26 → 2788.76] your at your office Wi-Fi that's kind of uh to some extent irrelevant whether we get it right or wrong
[2788.76 → 2791.68] I mean if we get it wrong then it's going to be a little bit of a slower load it's faster if we get
[2791.68 → 2796.68] it right but the data and everything like that's kind of uh unnecessary, or it doesn't really make any
[2796.68 → 2801.80] difference on somebody's phone though if we get it wrong we just cost them money yeah
[2801.80 → 2809.74] so true we cost them money we probably cost us money because we're hosting it uh if we're and
[2809.74 → 2814.00] you don't really have any way of predicting like you said like there's no hover so you can't use
[2814.00 → 2817.38] their behaviour to necessarily predict what they're going to do next you could maybe try to use position
[2817.38 → 2822.00] on the page something like that but even then if you're trying to do it predictively god help you
[2822.00 → 2825.82] if you like get it wrong, and you've done it three or four times while they're on the same page
[2825.82 → 2832.16] right then you're just then you're just screwing them um and I think I'd have to actually check but
[2832.16 → 2838.68] I think uh some a lot of mobile browsers if they are prefetching stuff they don't technically consider
[2838.68 → 2844.86] the the the entirety of the sort of like fetching transaction to be done until the prefetching
[2844.86 → 2849.50] is also done which can give the perception that it's also taking a lot longer to load than it really
[2849.50 → 2853.94] is oh wow or at least you'll still see sort of like the little data ticker like on most devices you
[2853.94 → 2857.74] can kind of see when network traffic is happening the page might be fully loaded, but there's still
[2857.74 → 2862.24] something going on and I know there's some people who actually notice that and kind of feel like
[2862.24 → 2868.66] something is not quite right I guess it's almost a little too transparent I think it's a super cool
[2868.66 → 2874.68] idea I think it should probably only be used when you're pretty confident um I think analytics are a
[2874.68 → 2879.24] good way to do that we've done it so that uh I know we've done this in the past with some of our apps
[2879.24 → 2883.58] or with some of our sites is that if our analytics say that if someone's on a certain page
[2883.58 → 2888.26] more than 80 percent more than 90 percent of the time they go to this other page next
[2888.26 → 2895.14] we'll, we can be pretty confident in that, and we'll, we'll potentially take the hit um because it is just
[2895.14 → 2898.78] a really cool experience if you like go to click on something, and it's just there like it's just
[2898.78 → 2905.42] even on a desktop that's cool if it's just like boom it's done it just feels nice um so that can be
[2905.42 → 2909.94] that can be really cool I think it's I think it's interesting tech I think you just have to know what
[2909.94 → 2917.84] you're doing awesome it's kind of a rambling answer to that yeah yeah yeah it was rambling
[2917.84 → 2925.38] no so we're kind of up against it here uh anything else you want to cover in foundation five uh kind
[2925.38 → 2931.56] of a sales pitch before we just briefly mention ink a little bit uh yeah we can like to do a quick
[2931.56 → 2936.58] little laundry list of things just to watch out for in the new uh the new foundation we've finally
[2936.58 → 2942.52] by popular request integrated the off canvas layouts into foundation um which are those uh
[2942.52 → 2946.18] those like uh those patterns where you can have navigation or some other side panel like kind of
[2946.18 → 2950.94] slide in from the side like it's off the screen uh we've done a whole new implementation of that
[2950.94 → 2955.46] that's all hardware accelerated it's actually really smooth it's really cool um and that's actually
[2955.46 → 2959.42] baked into foundation now so we will not have to field any more questions about how to integrate
[2959.42 → 2965.38] it with foundation it'll just be there um that'll be nice uh we've also we've redone like we've
[2965.38 → 2970.90] written tabs there was a lot of stuff about that uh we've written an all new uh actually for the
[2970.90 → 2976.70] the nerdy amongst the audience we've written a new command line interface uh for spinning up stuff in
[2976.70 → 2982.00] foundation which mark knows a lot better than I do, but it's its it's uh it's just a little wrapper
[2982.00 → 2988.94] for creating a new compass project uh so you don't have to type in all the compass create dash
[2988.94 → 2995.02] r reserve foundation using foundation and set up a gym file for yourself which we get a lot of
[2995.02 → 3001.74] questions about so it just helps you to not have to write all those commands you can use our
[3001.74 → 3007.98] CLI and say foundation new and then your project name, and it can take care of the rest for you nice
[3007.98 → 3013.98] you're leveraging Libras is that right uh that's actually so that would be something else we're
[3013.98 → 3020.74] using Libras locally for within the foundation where you put a generated the documentation uh okay so
[3020.74 → 3027.24] now that we've tested foundation and Libras if you wanted to use foundation in a non-ruby project
[3027.24 → 3032.50] we can safely say that Libras is going to work for you there were a few things that we were doing that
[3032.50 → 3038.72] didn't quite I think it was the opacity filter there's some known bug in Libras that it wasn't
[3038.72 → 3044.32] working, but it seems to all work now and if we took our compile times down from about four to five
[3044.32 → 3049.92] seconds to less than half a second absolutely incredible right and then the one last thing that i
[3049.92 → 3053.96] probably well there's two very quickly one is that we've also integrated fast click.js
[3053.96 → 3059.30] uh into the whole thing just because the 300-millisecond delay you get on touch devices when you
[3059.30 → 3064.50] click on stuff it's just super annoying, and it just makes everything feel slow and fast click is actually
[3064.50 → 3069.52] pretty well done and pretty reliable so we went ahead and just integrated that um so that'll just
[3069.52 → 3073.08] hopefully make things just feel snappier when you use foundation to build stuff, and then we've also
[3073.08 → 3078.34] added a medium grid size which people have been clamouring for uh previously we had a small grid size
[3078.34 → 3083.28] and a large grid size you could specify now you can specify when in between uh using just uh just
[3083.28 → 3087.34] classes so that's been integrated across the board, so there's medium sizes for pretty much everything
[3087.34 → 3093.96] now awesome so definitely uh definitely some stuff coming uh pretty much everything there I mean there's
[3093.96 → 3097.94] some stuff that's just by popular request we went ahead and included we wanted to have those components
[3097.94 → 3102.90] but the big thesis is that we're hoping this will be the fastest foundation to use the fastest
[3102.90 → 3107.44] foundation to uh to build with the fastest foundation to learn and the fastest one to actually
[3107.44 → 3112.02] deliver to people so and that comes out next Thursday right comes out next Thursday it comes
[3112.02 → 3116.86] out on the 21st November 21st and actually I can, I'll do this on the podcast thing if you're
[3116.86 → 3121.72] actually in the Silicon Valley area we're having a launch party on the 21st if you let us know at
[3121.72 → 3126.70] verbs somehow you can catch us on Twitter or whatever uh we will extend an invitation to you, and you can
[3126.70 → 3133.08] come get drunk with us awesome get drunk it'd be good foundation exactly well you don't have to get
[3133.08 → 3141.16] drunk you can just watch us nice cool so yeah briefly we talked about ink a little bit uh give us the
[3141.16 → 3146.26] elevator pitch of ink well we don't have a lot of time left so I'll do I can do like the 30 second
[3146.26 → 3152.08] elevator pitch for ink because it's really cool ink is foundation for responsive emails so if you want
[3152.08 → 3157.70] to create rich emails that work on lots of different kinds of devices they will actually
[3157.70 → 3161.98] uh you know they'll actually work basically responsibly if they're on smaller devices you
[3161.98 → 3166.80] can have a grid that actually works that actually reshuffles things and moves things around in a kind
[3166.80 → 3171.90] of a responsive way uh you can use ink to build that we have all the documentation for it and
[3171.90 → 3177.92] everything written up uh you can just find it at zerbs.com slash ink um, but we've started using it for
[3177.92 → 3182.86] all of our newsletters and stuff like that uh it works in pretty much every major uh mail client
[3182.86 → 3188.10] including outlook including ones that don't support responsive stuff at all uh which was no small feat
[3188.10 → 3192.06] and a source of a great deal of stress for uh various people on the team who had to work on that
[3192.06 → 3197.72] um, but it's its pretty cool and email kind of gets the short end of the stick sometimes because it's
[3197.72 → 3204.38] like ew emails um, but email is still like the number one way of actually connecting with an audience and
[3204.38 → 3209.10] it's still one of the absolutely most prevalent like means of communication and staying in touch with
[3209.10 → 3215.54] an audience keeping them engaged rich emails are like kind of big deal but uh ink will has stuff
[3215.54 → 3219.46] already built into it like a grid like foundation it has buttons built in like foundation it has a lot
[3219.46 → 3224.52] of sort of like those components you'd expect from a framework but in an email context so it's its
[3224.52 → 3230.02] the only thing like it that I know of uh, and it's its pretty cool that came out last week
[3230.02 → 3236.58] gotcha so it's that you said this I think right zerbs.com slash ink i-n-k yep it's uh
[3236.58 → 3242.32] we wanted to figure out what would be a word for it which is essentially the way foundation is
[3242.32 → 3246.78] the foundation of building a website we wanted ink to be one of the foundations of writing something
[3246.78 → 3251.66] so ink it was between that and like a pen or a quill or something like that yeah but if we
[3251.66 → 3256.66] called it ink that also gave us the opportunity to have a really cool squid for a mascot yeah that's
[3256.66 → 3260.76] awesome, and he's got in one in each one of his tentacles he's got like a different device
[3260.76 → 3268.22] it's like perfect representation of emails yep so yeah that's uh that's out now it's uh you can
[3268.22 → 3273.92] you can download it and use it there's documentation, and we support it and everything so awesome and
[3273.92 → 3277.80] that's also all open source it's on GitHub you can download the whole repo you can submit pull
[3277.80 → 3282.96] requests everything so it's literally foundation for email I mean it's like the way you guys did
[3282.96 → 3288.88] foundation you put that same amount of care and love into ink and pretty much awesome well
[3288.88 → 3293.14] cool yeah, so these are two cool projects to be on the lookout for just more cool stuff from
[3293.14 → 3298.14] curb it's been about I think two years since the first time uh you guys are on the changelog and
[3298.14 → 3302.64] unlike last time we didn't mention Britney Spears this time so there you go Britney Spears pretty
[3302.64 → 3310.42] well we mentioned her now yeah she's been mentioned um cool yeah so uh for those of you that are
[3310.42 → 3315.70] new we ask the same questions at the end of every episode, and we'll uh go ahead and ask them now so
[3315.70 → 3320.76] Jonathan for a call to arm so you officially release it next week so what would be something
[3320.76 → 3325.16] you'd like to see the community kind of get involved with when it's released uh when foundation
[3325.16 → 3330.38] comes out I would love to have the I would love to have the community really put the screws to
[3330.38 → 3336.12] interchange uh I want to see what all people can actually do with that and I'd love to know if there
[3336.12 → 3343.00] are more ways we can uh do work on the front end to optimize the delivery of responsive sites because
[3343.00 → 3347.46] there's its it's for most people it's just too hard on the back end to actually do most people
[3347.46 → 3352.22] just who are going to do front end stuff they can't do device profiling and HT access hackery and stuff
[3352.22 → 3357.14] on the back end so I want to figure out ways to really optimize this on the front end uh including
[3357.14 → 3361.66] if we can figure out any way, and we've talked about it a little bit here but if anybody has any bright
[3361.66 → 3368.12] ideas on client sideways of optimizing the delivery of assets based on the bandwidth and latency of the
[3368.12 → 3374.82] client that would be amazing cool so any bright ideas there awesome mark anything to add to that
[3374.82 → 3380.94] or anything different uh well I would love to see uh more people get involved on GitHub uh we have we
[3380.94 → 3387.02] already have a pretty active community uh on GitHub uh the issues section and just love seeing people
[3387.02 → 3393.06] get in their answering questions helping us continue to refine foundation and just make it more awesome
[3393.06 → 3398.06] so hoping to see more people get involved and helping us out yeah anybody who wants to get
[3398.06 → 3401.64] on GitHub and help us close out some issues that would be just rad because every issue that
[3401.64 → 3407.40] somebody else closes out is one less thing that makes us go gray so right yeah that's a common a
[3407.40 → 3411.96] common request it's kind of just like a's almost like a secretary of issues somebody to help out with
[3411.96 → 3416.78] just like managing this stuff because it becomes I mean when you're in open source when your project
[3416.78 → 3421.36] gets big enough man just managing the issues and like validating the requests and stuff becomes a
[3421.36 → 3426.20] full-time job and so it's definitely something that people need help with you can't see Mark's face but
[3426.20 → 3433.32] he's going uh-huh because he's had to do that oh god yeah late nights uh I can imagine
[3433.32 → 3438.86] so if you weren't doing uh if you weren't working at curb mark what would you be doing
[3438.86 → 3448.76] uh I would probably be out sailing or mountain biking two sailings in a row that's two sailings in a row
[3448.76 → 3453.64] that's two oh well I hope that doesn't sound cliché but I'm pretty sure Kaylin said he'd be sailing too
[3453.64 → 3459.42] yeah yeah yeah Mark's Mark's got all kinds of stories about adventures on catamarans in the
[3459.42 → 3464.50] in the in the ocean and around some islands and whatnot he's quite the sailor I don't know I was
[3464.50 → 3469.78] at the grenadines earlier this year and uh it was just absolutely magical out there and warm water and
[3469.78 → 3476.38] the best piña coladas you'll ever have awesome what about you Jonathan if I wasn't working at curb
[3476.38 → 3481.02] uh if I wasn't working at curb at all I would actually in a perfect world and if someone
[3481.02 → 3485.28] would give me the 15 million or so if anybody's listening wants to give me some money uh I would
[3485.28 → 3490.38] love to have my own movie theatre actually dude I'm right there with you man yeah yeah
[3490.38 → 3495.16] fantastic we got to find someone who's going to give us about the 10 or 15 million you need to
[3495.16 → 3499.04] build the facility and get all the equipment yes man I would love to build a movie theatre man
[3499.04 → 3504.62] see what we can find that's my that's my not so secret not working at curb dream so just go dig
[3504.62 → 3509.62] up some of those gold bars that you stored in your backyard Adam oh yeah I forgot about those
[3509.62 → 3516.12] you are in Texas yeah that's true if you got some of those I'll come take them yeah uh and then the
[3516.12 → 3520.72] last one is for a programmer hero so Jonathan just someone that's kind of been influential in your life
[3520.72 → 3526.76] career to this point oh programmer hero I don't know if this is cliché for a front-end guy or not but
[3526.76 → 3534.20] Paul iris his a freaking genius um I really like most everything that he's done although I will
[3534.20 → 3538.30] actually have one that is actually I have a different one which is maybe less cliché but i
[3538.30 → 3544.98] really like the guy uh he's actually he's part of the Google uh Chrome dev relations team in England
[3544.98 → 3551.92] actually his name is Jake Archibald uh oh yeah yeah yeah he is uh we he and i both uh spoke at a
[3551.92 → 3560.76] conference in Finland earlier this year uh and his talk was amazing not in partly in the content
[3560.76 → 3565.16] which was all about like animation optimization in modern browsers which was just awesome and like
[3565.16 → 3570.96] some of the best research stuff I've ever seen, but his actual slides were all built in HTML CSS and
[3570.96 → 3574.10] JavaScript and were just like some of the most amazing things I've ever seen like it was incredible
[3574.10 → 3581.20] like the the the things he can do with like animating SVGs with JavaScript along paths and
[3581.20 → 3585.58] like all kinds of just cool stuff I did not even know you could do I thought it was awesome yeah kind
[3585.58 → 3589.72] of a weird tie-in for him, he I follow him on Twitter he's got a name is I think it's like
[3589.72 → 3596.96] Jaffa the cake or something yeah every time he tweets and I see his avatar you know you see the
[3596.96 → 3602.56] avatar is like real small and can barely see him for some reason his picture looks exactly like
[3602.56 → 3607.72] win Netherlands to me and so whenever he tweets I always think it's win tweeting similar with the
[3607.72 → 3611.72] changelog there's something about him that looks, and it's a weird tie-in but yeah you can
[3611.72 → 3615.52] ask Jake about this but the reason he only ever shows like half his face and avatar is the other
[3615.52 → 3624.72] half is hideous uh we can edit that out doesn't worry that's not just um I've told it to space
[3624.72 → 3633.74] it's its really tough uh to name one person i I would say but i I'm going to say Ryan bates uh before
[3633.74 → 3639.48] i I moved down here I used to watch well I still watch his screencast he's been on hiatus for
[3639.48 → 3645.46] the last couple of months now yeah yeah actually the last uh screencast he did was on foundation uh which
[3645.46 → 3652.14] was kind of funny uh but definitely he just I was admired someone who could take a really complex
[3652.14 → 3657.70] subject and break it down and make it seem relatively trivial and easy to learn
[3657.70 → 3665.12] yeah we love Ryan he's a good guy and i uh yeah I don't you know I don't have the the update he wrote just
[3665.12 → 3670.52] a few weeks ago I think about the kind of he's still going on hiatus I'm you know get some
[3670.52 → 3674.50] time all for you but man the community definitely misses his contributions because he does some really
[3674.50 → 3679.70] cool stuff yeah we've been talking about burnout, and it seems like it's a mixture of that and I think
[3679.70 → 3683.52] he was sick for a bit but Ryan if you're listening somehow you're just like chilling listening to the
[3683.52 → 3687.18] change all for whatever reason maybe you are maybe you aren't we wish you well my friend for sure and
[3687.18 → 3691.54] we want to see you back but back better for sure yeah take your time for sure yeah
[3691.54 → 3700.04] awesome cool well that's uh that's a good show man i I'm uh I'm stoked you guys were able to come on
[3700.04 → 3705.22] and talk about foundation five Jonathan I know you made an appearance a while ago, and it's been a while
[3705.22 → 3711.52] since then but you guys have been I mean I think when it talks when we talk about the competition
[3711.52 → 3716.18] of found of frameworks and whatnot I think what the listeners of the show would definitely need to know
[3716.18 → 3720.42] is that like you guys have been in it for the long haul I mean everything from what you guys have been
[3720.42 → 3725.58] doing at curb to what you've been doing with foundation you know you've been committed so if I think
[3725.58 → 3731.52] one thing we do when we choose or make choices to use frameworks or whatever is trust and i and I believe
[3731.52 → 3736.02] you guys have definitely earned the trust of the community and you guys are leaders in many
[3736.02 → 3741.12] ways, and we just appreciate you sharing it with us honestly and then inviting us to contribute that's
[3741.12 → 3746.16] that's super awesome so we want to thank you for taking the time to come on Jonathan and mark for uh
[3746.16 → 3752.12] for sharing their wisdom here for sure and then uh and uh Brian for reaching out and reminding me hey
[3752.12 → 3756.14] that you guys uh announced foundation five which we covered today for you real quick, and we can't wait
[3756.14 → 3761.44] till next Thursday when you release it so well thank you very much we uh we really appreciate
[3761.44 → 3765.30] it, and it's uh it's always fun to come on we uh we were stoked when you reached out and
[3765.30 → 3769.04] wanted to I wanted to talk again it had been a little while so uh thanks for having us it's a good
[3769.04 → 3774.10] timing for sure I think you know honestly yeah we appreciate you guys being so uh so flexible too I mean
[3774.10 → 3779.72] you guys came on so quick yes nailed it for sure yeah we uh yeah yeah we needed a break
[3779.72 → 3785.08] now get back to right well next Thursday you have a big break right you get the get the
[3785.08 → 3790.70] beer party the drink up well you'll uh your launch party oh yeah we'll uh we'll, we'll chill
[3790.70 → 3798.26] out for the party and then I'm sure on Friday we'll be pushing 501 so yeah and also uh
[3798.26 → 3804.54] want to give a shout-out to our sponsors digital ocean and top towel um I mentioned earlier you know
[3804.54 → 3811.38] just about us moving over to blazing I like saying if it's funny right blazing fast SSD cloud servers i
[3811.38 → 3815.06] mean I just think it's it sounds cool for one but I definitely think it's cool so if you've
[3815.06 → 3819.02] been reading the changelog for a while and if you're browsing it right now as you're listening
[3819.02 → 3825.28] to this, and it's much faster much zippier that's why so take advantage of our 10 hosting credit with
[3825.28 → 3830.82] them changelog sent me is how you do it changelog sent me use that when you sign up there's a coupon
[3830.82 → 3835.30] code spot there for some reason that doesn't work out just email support they're awesome they're
[3835.30 → 3841.68] going to get right on it um and then I mentioned the tutorials that uh that I used myself and if you're
[3841.68 → 3847.10] if you're a skilled person in any sort of way, and you can share some knowledge back on how to do
[3847.10 → 3851.98] something with a digital ocean server or how to use a certain piece of open source technology you can
[3851.98 → 3856.04] get paid 50 bucks to write tutorials and uh we'll, we'll have some links in the show notes for that
[3856.04 → 3861.34] but uh also email Barry at digital ocean dot com if you want some stickers he will ship them
[3861.34 → 3867.96] around the world I don't care where you're at he'll send them to you and then top towel uh you got to
[3867.96 → 3871.52] join the top towel network if you're into freelancing and uh you definitely have to
[3871.52 → 3876.24] check them out top towel dot com slash developers to apply work with some awesome people around the
[3876.24 → 3881.56] world uh and if is you haven't, yet they also have a really awesome engineering blog we'll have a link
[3881.56 → 3885.68] for that in the show notes as well, and they've been featured a couple of times on the channel too so
[3885.68 → 3891.02] that's that's been awesome but uh that's it for us, I think I mean I'm just stoked we're on
[3891.02 → 3895.90] digital ocean, and it's superfast uh I'm just I'm I can't believe it I'm I'm excited
[3895.90 → 3902.34] but uh Jonathan mark thanks again for coming on the show and let's say goodbye see you guys later
[3902.34 → 3904.66] thanks guys bye
[3925.90 → 3932.34] you
[3932.34 → 3934.34] you
[3934.34 → 3936.34] you
[3936.34 → 3938.34] you
[3938.34 → 3940.34] you
[3940.34 → 3942.34] you
[3942.34 → 3944.34] you
