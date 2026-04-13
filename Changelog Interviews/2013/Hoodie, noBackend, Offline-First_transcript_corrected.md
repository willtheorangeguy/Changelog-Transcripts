[0.00 → 15.10] welcome back everyone this is the changelog we're a member supported blog podcast and weekly email
[15.10 → 20.44] that covers what's fresh and what's new in open source you can check out the blog at the changelog.com
[20.44 → 27.00] our past shows at 5by5.tv slash changelog and subscribe to the changelog weekly it's our weekly
[27.00 → 32.26] email covering everything that hits our open source radar you can subscribe at the changelog.com
[32.26 → 37.44] slash weekly, and we ship that every Saturday morning so you can enjoy your Saturday in bliss
[37.44 → 42.44] learning about the new and fun stuff in open source but uh this show is hosted by myself Adam
[42.44 → 48.44] static and Andrew Thorpe and just say hello yo what's going on it's a good week man I'm excited
[48.44 → 52.98] to uh to have this show man I've been wanting to talk about this topic for a while but uh
[52.98 → 59.18] good time yeah i kind of dropped the ball on it, I actually well I asked uh Karen if we could
[59.18 → 63.78] do this a few months ago, and he said yeah sure email me some information totally forgot about it
[63.78 → 69.60] oh man uh we'll have to apologize my apologies we'll get a true apology to Karen here in a bit
[69.60 → 76.22] when we talk to him but uh this is episode 111 and today's show is sponsored by digital ocean
[76.22 → 82.20] and also top towel we'll tell you a bit more about top towel here in just a bit but uh quick mention
[82.20 → 88.20] for them, they connect startups businesses and organizations to a growing network of elite
[88.20 → 93.24] engineers around the world and they're hoping that you're that elite engineer so stay tuned for
[93.24 → 98.08] a mention here in a bit later on the show for them but digital ocean a fan favourite and certainly
[98.08 → 104.36] a fan of open source as well as a huge supporter for the changelog so we're always excited to tell you
[104.36 → 109.14] what they're up to but if this is the first time you're hearing about them digital ocean is a simple
[109.14 → 114.60] cloud hosting provider built for developers so if that's you're a developer they build it just
[114.60 → 119.90] for you like literally just for you pricing plans started only five bucks a month for a half a gig of
[119.90 → 127.24] ram 20 gigs of SSD drive space one CPU and one terabyte of transfer and digital ocean has data centres
[127.24 → 133.00] not only here in the United States in New York and San Francisco but also across the pond where not far from
[133.00 → 137.22] where Caitlin is at in the answer down uh digital ocean has a lot of features that really help
[137.22 → 142.54] developers get their apps launched as quickly as possible they have uh servers with full root access
[142.54 → 147.90] so the moment you spin it up full root access you get you can deploy that in 55 seconds and for a
[147.90 → 155.48] faster launch you can spin them up with a Ruby on Rails uh install docker or even ghost which we had on
[155.48 → 162.92] the show back in 105 already pre-installed so applications rate for from one click additionally they offer
[162.92 → 168.84] features that have a vast collection I'm sorry they also offer a vast collection of tutorials that
[168.84 → 173.00] cover configuring and optimizing your service so if you're like me, you spin up that server, and you're
[173.00 → 177.74] like I don't know where to go they've got pretty much a tutorial for every configuration whether it's
[177.74 → 183.04] a lamp stack or it's ingenue or whatever it is they've literally got a tutorial to cover your back and
[183.04 → 188.18] get you up get you up and running but uh we have a brand-new promo code for uh for this month of
[188.18 → 193.88] November and I think maybe for a couple more months, but this one is changelog sent me
[193.88 → 198.92] I'll repeat that one more time changelog sent me uh you can try digital ocean today for free using
[198.92 → 203.60] that promo code which will get you ten dollars of hosting credit or basically two months free
[203.60 → 208.82] head to digitalocean.com to get started and thank you to digital ocean for your support
[208.82 → 215.82] um today we're joined by Caleb McMahon he is uh from hoodie he's he's rocking it out and as Andrew
[215.82 → 220.46] mentioned he's got a little apology to say so maybe we can start there Andrew well I don't know
[220.46 → 225.68] I think I already apologized to Caleb personally but yeah he uh he was excited to come on the show
[225.68 → 230.84] I think the first time too and i uh I told him maybe it was a good thing because some
[230.84 → 236.92] pretty big news for uh hoodie last week or so yeah so maybe it's going to get him on now but yeah why don't
[236.92 → 242.52] you go ahead Caleb and uh just kind of introduce yourself and hoodie and what you're doing
[242.52 → 253.28] sure um so hello from sunny England uh I'm Caleb McMahon, and you may know me from kind of node.js land
[253.28 → 261.32] if you do any node work um I've kind of done work with the async module node unit various other things
[261.32 → 270.50] in node and now I'm doing work with the hoodie team and working on hoodie which is what we like to call
[270.50 → 278.66] kind of no back-end project and what we mean by that is that it lets you build um complete
[278.66 → 284.26] applications complete data-driven applications um without worrying about the back-end so entirely
[284.26 → 292.68] using front-end JavaScript so no back-end that is something that that is at nobackend.org is that
[292.68 → 297.40] something that you guys have participated in or just like a kind of mindset you're buying into
[297.40 → 303.50] um well that website was set up by Gregor who's also kind of one of the founders of hoodie
[303.50 → 309.04] uh, and it's kind of it's an idea that we're trying to put out there to uh I suppose discuss
[309.04 → 313.96] some of the things that we've thought about in the hoodie project more widely and how they apply
[313.96 → 319.06] in various other spaces, and so we are not the only provider of what we would call
[319.06 → 325.64] a no back-end solution, but we want to kind of really explore what that means for web development
[325.64 → 330.20] uh you know it turns out there's quite a few interesting things that happen when you consider
[330.20 → 339.80] your application as being separate from the back-end uh so I mean for one it's quite empowering uh
[339.80 → 347.30] so we often we have this idea in the hoodie project of a jQuery developer uh and what we mean by
[347.30 → 354.22] that is someone who can you know design great sites do you know great interactions on the front end
[354.22 → 360.16] but doesn't necessarily know everything about um all the back-end technologies the full stack
[360.16 → 364.00] because you know what happens if you're a front-end developer, and you want to do
[364.00 → 371.48] a web app you could design it uh you can make some really nice interface but as soon as you
[371.48 → 380.28] have to hook up um you know persistence emails um payments all that kind of stuff all of a sudden
[380.28 → 385.88] you have to learn about my sequel you have to learn about PHP you have to be able to administer Linux or
[385.88 → 390.00] find a service that will do that, and it's you know it may as well be rocket science at that point
[390.00 → 395.44] uh I mean you know it's its just way too much to learn it's its not you know it's not you're not
[395.44 → 404.80] interested it's not your job uh and so by making it accessible to developers that just aren't
[404.80 → 411.94] interested in all that stuff we're hoping that um one we can empower people to participate in making
[411.94 → 417.12] the web that wouldn't otherwise be able to and that's that's an important thing I sometimes think
[417.12 → 422.06] we forget most of us are full stack developers or you kind of do a bit of front end a bit of back end
[422.06 → 428.06] um you know programming is a really empowering thing to be able to do and the more people that
[428.06 → 434.86] can participate in making the web the better it's going to be for all of us um so that's that's
[434.86 → 440.88] kind of one nice thing about approaching web apps in a slightly different way right and the no
[440.88 → 444.72] back end so a little bit of a misnomer right it's not that there is no back end it's that there
[444.72 → 451.22] is it's a generic you're not creating the back end there's no back end yeah you're creating its a
[451.22 → 454.94] generic back end and some assumptions are made right and I think that they're they're valid
[454.94 → 460.38] assumptions, and it hits the know most use cases which are there's user accounts there's like
[460.38 → 466.38] some sort of data store emails you know then there's some more I don't know more specific uh
[466.38 → 471.28] higher level stuff which is like sharing data between people payments all that stuff but
[471.28 → 476.76] you're making assumptions right and so somebody had to come up with these ideas and say all right
[476.76 → 481.64] the generic back end has to support this this this and this is that right yeah exactly I mean
[481.64 → 487.82] ultimately this is a discussion about platforms really um it's an it's not no back end
[487.82 → 492.64] it's a pre-packaged back end that we're providing, and you're right we have to kind of second guess
[492.64 → 497.46] what people want, but you know 90 percent of the time it's its really easy to guess what
[497.46 → 501.82] people want from a web app that you know they want accounts they want storage all that kind of stuff
[501.82 → 508.88] yeah um but i I think where the no back end part comes in is really how you design your
[508.88 → 515.38] application so what we want to do is kind of disentangle the app from all the implementation
[515.38 → 521.78] details of sending emails and all that kind of stuff right if you could think in terms of
[521.78 → 528.00] the intent of your application rather than you know all the messy details of actually doing it
[528.00 → 533.84] um then you get much cleaner code I mean you get much kind of smaller code for a start which is great
[533.84 → 542.32] for maintaining software um but also I think it's more portable because instead of saying oh
[542.32 → 548.38] okay I need to download some dependencies maybe node mailer I need to set up some kind of email
[548.38 → 554.60] service or find one to pay for online I need to point node mailer at the MTV server so I can send
[554.60 → 561.48] an email instead of getting kind of bogged down in all the actual um deployment details you can just
[561.48 → 569.72] say hoodie dot email dot send uh from the front end and that's that's just the way your app kind of
[570.40 → 577.78] um specifies its intent right so I think at it's called no back end, and we'll get into hoodie
[577.78 → 581.48] specifically but just kind of laying a foundation it's called no back end so that's kind of obviously
[581.48 → 587.24] like an I don't know a play on the no SQL stuff and the data store part of no back end which
[587.24 → 593.58] I would argue is probably the most important other than user accounts um it kind of relies on
[593.58 → 597.84] no SQL to an extent right because you just have to be able to store kind of arbitrary data instead
[597.84 → 604.48] of modelling the data specifically in like a relational database yeah absolutely I mean if you look at the
[604.48 → 611.12] team we all kind of have a couch dB background, so there 's's some there's definitely some no SQL
[611.12 → 616.74] couch dB influence in the design we've used for hoodie um, and it turns out that's a perfect
[616.74 → 623.06] design for this kind of API right because um especially if you've been doing couch apps which
[623.06 → 629.24] you know um the original design for hoodie kind of came out of the couch app idea you had to do some
[629.24 → 634.48] quite crazy things in order to make permissions work and sign up and um making it all secure from
[634.48 → 638.20] the front end, and so we've actually had quite a lot of practice at doing things that
[638.20 → 643.68] um seem kind of crazy to most people at the time right think you know things like being able to
[643.68 → 647.82] write to a database from the front end you know most people would kind of throw their hands
[647.82 → 653.26] up in the air and scream and run away at that point a year ago that was like people looked at that as
[653.26 → 657.60] just a pipe dream that would never happen right exactly but most of our team a year ago we were all
[657.60 → 664.24] doing it right we were deploying apps doing that and that's the difference so okay this is a've had
[664.24 → 669.02] this kind of assist I don't know if system is right where architecture, but we have the spec being
[669.02 → 674.30] no back end and then kind of the implementation being hoodie so uh can you talk about like where
[674.30 → 679.24] what come you know what comes first the chicken or the egg so with hoodie and no back end kind of
[679.24 → 687.54] what was the order of operations for that, so chronologically hoodie came first I think yeah um but
[687.54 → 694.86] i I think in terms of goals no back end is the bigger goal for us uh you know if someone comes
[694.86 → 701.22] along and builds another hoodie that's way better than that's great yeah you know mission accomplished
[701.22 → 706.30] we don't have to do any more work yeah I mean it's a spec driven by implementation right so you kind
[706.30 → 711.00] of proven the concept with hoodie, and then you can kind of generalize it into the no back end spec to
[711.00 → 717.06] kind of promote this sort of development that I mean that really kind of we talked about this with the
[717.06 → 723.08] um uh open karma stuff like it kind of bridges the gap between front end uh well kind of between
[723.08 → 728.14] designer front end and back end right like it makes it a lot easier for people to do the whole stack
[728.14 → 735.58] or to not have to worry about the whole stack so that's that's good and so hoodie is the
[735.58 → 740.46] implementation that's driving no back end for you guys right now um before we talk about hoodie is
[740.46 → 745.10] there any other uh do you guys know of anyone else that's kind of that's running with the no back
[745.10 → 749.82] end stuff and working in kind of like competition to hoodie um there are certainly
[749.82 → 756.28] competing ideas out there um when it comes to actually implementing the specs and the ideas
[756.28 → 761.84] that we've come up with in no back end no not really not that I'm aware of um but in terms of
[761.84 → 768.02] competing ideas back end as a service has been around for a while now and that's things like um i
[768.02 → 773.00] suppose firebase um if you're familiar with that that's kind of a real-time back end that's quite
[773.00 → 779.12] popular um the various other ones mostly targeted at mobile so if you're a mobile app developer you
[779.12 → 783.32] don't really want to have to come up with the whole server just to do a high score table or something
[783.32 → 788.48] right and so there are quite a few services that do user accounts and storage and a bunch of back
[788.48 → 795.42] end stuff for you as a service there are very few actually open source things that you can run
[795.42 → 802.18] yourself though right uh, and also they have a slight excuse me they have a slight uh
[803.80 → 809.62] slightly different approach uh in the way they target users I think we're trying to make it
[809.62 → 814.82] accessible to the front end developer they are targeting people who already do development but
[814.82 → 821.56] perhaps just don't want to develop the back end this time that's like me, it's like that's like me in a
[821.56 → 826.90] much I mean that's you know i I plug this um if you're a subscriber to the changelog weekly mentioned
[826.90 → 832.54] that in the intro but if you subscribe to that uh we did cover this in issue nine uh about a month
[832.54 → 838.22] back and the open source moves fast we try to keep up with as best as we possibly can too but um
[838.22 → 844.68] Kaylin you presented it uh you presented hoodie not long ago too at uh lx js and you kind of had a
[844.68 → 849.84] nice presentation there Jan is also on your team you mentioned team, and you all were building this stuff
[849.84 → 855.66] a year ago and doing this uh you know right into the database from the front end a year ago who is
[855.66 → 860.82] the team behind and kind of what's the give a shout-out to the team i guess and kind of give some
[860.82 → 864.96] lay of the land of what they've done or what you all have done over the past couple years to kind of
[864.96 → 873.48] get you to where you're at now sure so um well I've already introduced myself uh mostly a node.js and
[873.48 → 881.02] couch TV background there's Jan who was kind of um one of the core people in couch TV these days
[881.02 → 887.00] he's lots of people will know Jan already he goes to lots of conferences and speaks and um
[887.00 → 890.58] is very kind of very good at hooking us up with the right people in the community
[890.58 → 899.60] um there's Alex who's also in Berlin where Jan is uh he's kind of like a designer kind of front
[899.60 → 904.52] developer background which is very useful to us in the team uh to have someone with that perspective
[904.52 → 910.76] and he does a lot of work on the um the admin interface and kind of influencing the API uh there's
[910.76 → 918.44] Gregor who in a way kind of came up with the original idea um in that it kind of grew out of a project
[918.44 → 924.40] called minutes.io which was um a minute taking app that Gregor wrote, and it was originally implemented
[924.40 → 931.46] as a couch app um so running on couch dB, and he ran into some limitations and had to do some
[931.46 → 937.34] redesign and eventually coming up with the right way of doing that is what became hoodie later on
[937.34 → 944.82] um there's also Lena who is our kind of uh she's does all the writing for hoodie so the communications
[944.82 → 950.08] the blog posts that kind of stuff uh keeps us on track and the communication stuff so it's great to
[950.08 → 956.96] have her on the team that really helps um, and also we have Sven who was in London but now has also
[956.96 → 963.34] moved to Berlin uh who's just kind of turned up one day and contributed loads of code uh, and now he's
[963.34 → 969.34] well he seems to be doing everything it's great he's actually Sven is also isn't he on the Bauer team as
[969.34 → 974.72] well that's right yeah, and we'll be having Bauer on in a few weeks um oh cool maybe next week I can't
[974.72 → 979.86] remember exactly but yeah, so this is pretty neat so you have a team of six that are working on hoodie
[979.86 → 987.46] are you guys full-time or um you have a weekly sponsor for hoodie which I think it's public
[987.46 → 993.20] knowledge it's a thousand euros a week is the rate is that right um yeah I think last time I checked
[993.20 → 1000.50] yeah so that obviously isn't enough to pay six people so how does like that work with you guys are you
[1000.50 → 1007.44] guys sure all full-time or what's that like uh increasingly we're working on it um much, much closer
[1007.44 → 1015.52] to full-time uh we're all kind of uh lucky in the sense that we can mix up our work uh we all
[1015.52 → 1020.80] do a bit of freelance and some other things to kind of keep things running smoothly um but increasingly
[1020.80 → 1028.30] we're doing just more and more hoodie work and that has been sponsors um kind of paid for so far by
[1028.30 → 1035.72] sponsorship uh, so our first sponsor was nonet if you look it up on the blog we have a kind of big blog
[1035.72 → 1042.20] post about nonet they gave us um a grant that let us build the plugin architecture uh which is kind
[1042.20 → 1047.86] of a huge thing we released recently perhaps we'll talk about that a little bit later uh and
[1047.86 → 1054.48] then we have the yeah the commit sponsors which is a know a fascinating idea I haven't seen
[1054.48 → 1060.30] any other projects do this uh so what you can do is you can um sponsor the team for a week
[1060.30 → 1066.02] and we will put a banner up on the home page saying this week is sponsored by you know whoever
[1066.02 → 1073.48] uh we will also kind of tweet your message and say you know thanks for sponsoring us uh but
[1073.48 → 1078.88] interestingly we will also put your message in our commits, and so we have a system in place with all
[1078.88 → 1085.68] the core committers that um we will update our commit message so the first you usually know on um
[1085.68 → 1090.30] a git commit the first line is kind of the key information and then below that you can have
[1090.30 → 1097.76] additional stuff yeah so inside the extended info we will put your um sponsor message and so this week
[1097.76 → 1102.82] we are sponsored by human JavaScript uh, and so they have if you look at our commits for this week that
[1102.82 → 1109.76] you will see the um sponsor message in there, and it will link to um the human JavaScript book uh so
[1109.76 → 1114.64] yeah it's its really that's a super neat idea I like the idea honestly it's its uh I don't know i
[1114.64 → 1118.20] wonder how the rest of the community feels about that like if you got any feedback on like
[1118.20 → 1123.70] issues or whatever or line level commits or line level comments or whatever about oh what's this
[1123.70 → 1129.34] doing here at first but I think it's a unique I think we have to be creative in this world because
[1129.34 → 1134.82] we all know open source is hard we all know that open source doesn't exactly get you know in this case
[1134.82 → 1140.48] um you know sponsored by everybody in the world, or you know we don't have the engineers to facilitate
[1140.48 → 1145.04] you know ruinous or whatever forever you know that's going to end at some point so we have to
[1145.04 → 1149.78] be creative in the way we know kind of line up these kinds of new technologies and sponsor the
[1149.78 → 1155.22] people making them so I think this is a huge uh thing, and it's I think it's pretty neat yeah you
[1155.22 → 1158.46] guys are kind of pioneering it and trying I'm sure you're trying I mean you're trying a couple different
[1158.46 → 1162.90] methods so you guys can kind of you know you're going to prove concepts and all over the place
[1162.90 → 1167.48] with hoodie with the app itself with you know fundraising and stuff like that we like to think big that's what it
[1167.48 → 1172.02] so i I want to ask because I'm sure a lot of people are wondering this so what is hoodie like
[1172.02 → 1177.80] where does that name come from what does it mean oh well um the name kind of predates me but I've heard
[1177.80 → 1187.72] this story um it's uh so um Jan and Greg and uh possibly Alex I'm not sure about that time were
[1187.72 → 1191.76] trying to come up with a name, and it was um very difficult to kind of come up with a new thing I think
[1191.76 → 1195.56] at the time it was called couch apps the next generation or something like that
[1195.56 → 1200.70] yeah, and we wanted something that was just a temporary name we wanted something more snappy
[1200.70 → 1207.06] uh and at some point yang got up and uh said oh you know I'm just going to get my hoodie because he's
[1207.06 → 1213.26] going to leave, and he goes ah hoodie that's perfect um, and he said okay if we can get hood.ie as a
[1213.26 → 1219.62] domain name then we'll have it and it was available that's awesome yeah that's cool we have a really cool
[1219.62 → 1224.80] domain meshes like that it's we at a company that I've I worked at before we struggled with uh or we
[1224.80 → 1229.30] talked about a lot we created our own brand similar to hoodie I mean nothing like hoodie but
[1229.30 → 1234.24] you know same kind of idea where the name of our company kind of meant nothing and we kind
[1234.24 → 1239.86] of bumped we ran into a lot of obstacles like you're trying to educate people on what your company does
[1239.86 → 1245.10] uh with a name that might not have anything to do with what you do so there was some um you know
[1245.10 → 1249.68] struggles there ultimately we ended up rebranding with a name that made more sense and we kind of found
[1249.68 → 1254.16] some growth there have you guys run into anything like that where people are like I don't know what
[1254.16 → 1258.12] hoodie is and kind of you know throw you out at first glance just because of the name or anything
[1258.12 → 1264.84] um well that's that's an interesting one uh so far the feedback I've had has been pretty positive but
[1264.84 → 1268.62] then I guess if they threw out the project at first glance we would never have heard from them
[1268.62 → 1275.52] yeah um interestingly in the UK hoodies are um there's kind of like a political headline
[1275.52 → 1283.28] associated with hoodies as petty criminals so it's uh I get interesting responses here but in most
[1283.28 → 1289.04] other countries no yeah that reminds me of Canada they got uh if you're a goof in Canada
[1289.04 → 1292.12] Canadians out there you know what I'm talking about I'm not going to mention this because it's a
[1292.12 → 1298.74] pretty derogatory thing but if you're a goof it's not good yeah I don't want I think we should move
[1298.74 → 1304.92] along I don't know what we're talking about here, so quiet yeah so let's talk about the news with hoodie
[1304.92 → 1309.82] which was the plug-in system and I think that's kind of what re-sparked I was like oh yeah I forgot
[1309.82 → 1314.26] about hoodie I need to reach out to him again so let's talk about the plug-in system and your path
[1314.26 → 1319.64] to get that done with uh what was it NL what was it called nl net and let's talk about what
[1319.64 → 1327.46] what is the plug-in system and how did that kind of come about um yeah, so the plug-in system is a
[1327.46 → 1334.34] way for you to extend hoodie functionality and that means extending the back end so you can kind of hook
[1334.34 → 1340.70] node.js workers into our data store, and you get change events on tasks, and you can kick off things
[1340.70 → 1348.14] like sending emails or whatever um also you can extend the front-end API so that's that's not
[1348.14 → 1351.76] something that usually happens with plugins you know usually it's kind of back-end code or something
[1351.76 → 1357.72] like that in the case of a framework um, but it was really important to us that the API is kind of like
[1357.72 → 1365.72] the first place that's that's where the beginnings of all our code is um so whenever
[1365.72 → 1370.66] we come up with a feature we start with the API first we have this idea of um this concept called
[1370.66 → 1376.72] dream code, and so we like to sit down and just write out what we want to do in terms of perfect
[1376.72 → 1382.20] code in our heads at least, and then we think really hard about how we can make that possible
[1382.20 → 1387.18] and sometimes you know the implementation is really difficult, but it starts with a really nice
[1387.18 → 1393.22] simple API um so it's important to us that plugins also extended the front-end code so you could
[1393.22 → 1401.10] expose these beautiful APIs uh, and thirdly you can extend the admin interface which is called pocket
[1401.10 → 1407.50] so you just drop some HTML and JavaScript and stylesheets or whatever into a folder, and it will
[1407.50 → 1414.32] get served up in our admin panel so you could also as well as being able to send emails you can also
[1414.32 → 1422.32] have a dashboard that says how many were sent or whatever yeah so the NL net kind of sponsored this
[1422.32 → 1428.54] this idea of plugins with you guys yeah well the thing with plugins was it's its a big chunk of work
[1428.54 → 1433.84] to kind of rewrite a bunch of the back-end architecture and lots of other things to make
[1433.84 → 1440.88] plugins happen um and the thing was we couldn't drag it out for too long because it would have
[1440.88 → 1447.88] invalidated a lot of other um community effort on the other side so you know if we're accepting
[1447.88 → 1452.06] pull requests on one branch of code, and we're doing plugins on another you know they're going to get
[1452.06 → 1456.60] out of sync, and it just creates headaches for us so it's important to be able to do it um as quickly
[1456.60 → 1462.18] as possible and actually dedicate enough time to get it right and communicate it properly and write
[1462.18 → 1467.22] documentation all that kind of stuff uh and so the money from a let meant that we could
[1467.22 → 1475.22] really focus on that for you know several weeks at a time and get out the door gotcha did you have
[1475.22 → 1479.96] any kind of backlash with it getting out of sync or did you kind of take that challenge on and
[1479.96 → 1487.60] beat it i I think it went fine yeah so no big problems to speak of awesome so I was looking for
[1487.60 → 1493.60] a tweet and this is one thing I think that i you guys wrote the I think it was a blog post you
[1493.60 → 1500.48] wrote about offline first and it is like sparked this just frenzy of I mean I saw like hoodie
[1500.48 → 1505.64] on tweet on Twitter just like blow up all of a sudden and I think that one of the first ones i
[1505.64 → 1511.46] read was Ethan Marco wrote gushed excitedly about this whole offline first deal on like one of those
[1511.46 → 1517.66] blogs the kids are talking about obviously that's Ethan talking like Ethan, but kind of the point is
[1517.66 → 1523.06] you sparked this huge frenzy when you guys did offline first can talk about that what was
[1523.06 → 1528.58] that like and is that kind of the biggest kind of news headline you guys have gotten so far
[1528.58 → 1537.68] um sure I don't know if it's the biggest yet I hope it is I mean that's great um yeah we like coming
[1537.68 → 1542.44] up with concepts I think we are used to doing things in quite strange ways in our team we have we
[1542.44 → 1548.88] quite a special connection of people and um it's really fun being able to actually discuss it with
[1548.88 → 1555.20] the whole community at large so it's great when we get this kind of response uh offline first is
[1555.20 → 1560.94] I mean it's amazing it's not a thing already that's I keep thinking this with hoodie
[1560.94 → 1565.46] projects you know how come people aren't doing offline first already you know every time I go on
[1565.46 → 1571.20] the tube in London and I lose connection how come people don't do offline first that's crazy yeah um
[1571.20 → 1575.96] whereas you know now we have the tools available in the browser we have local storage we have indexed
[1575.96 → 1582.34] dB um in our case you know there's pouch so we can do couch dB replication direct from the browser
[1582.34 → 1590.38] um I mean you could even include JS git from Tim Caswell you could replicate um git repositories
[1590.38 → 1598.24] whatever uh, so there are loads of tools available now to do really powerful offline experiences um and to
[1598.24 → 1604.94] think of your data the same way offline as online is a fascinating thing and that's something
[1604.94 → 1609.68] that we're all used to doing in the couch dB community because um we've had this idea of local
[1609.68 → 1616.94] apps running on couch for a long time when you replicate data between nodes uh and so you know
[1616.94 → 1623.24] the idea of treating your data the same whether you're online or offline is kind of amazing it's not
[1623.24 → 1629.82] just you know we don't we don't want it to just be some cached read-only copy of the data it's like
[1629.82 → 1635.32] oh I'm offline but at least I can see what I had we want you to be able to continue to write new things
[1635.32 → 1640.56] record to-do items or calendar appointments and for it to synchronize when you get a connection back
[1640.56 → 1645.64] um, and you know we have the tools to do that now we should really be thinking in terms of offline first
[1645.64 → 1652.66] uh and so on of the guiding principles in hoodie is that all the APIs that um we have in terms of in
[1652.66 → 1657.62] hoodie are based on a very simple mechanism that means you can continue to use them if you're offline
[1657.62 → 1661.64] so obviously if you're offline, and you try to send an email it's not going to send
[1661.64 → 1668.80] but we will record in your local storage the fact that you uh intend to send an email and once you get
[1668.80 → 1672.52] a connection it will synchronize up to the hoodie server and hoodie will send it
[1672.52 → 1678.18] can you can somebody let's say I got a couple questions about this let's say somebody kind of
[1678.18 → 1684.42] wants to push into that queue uh when they're offline and then, and they decide I guess it doesn't
[1684.42 → 1687.78] really make sense, but they decide they no longer want to do that is there any way for them to like
[1687.78 → 1694.76] manage that queue yeah so um the queue is just your user database so I should probably explain something
[1694.76 → 1700.16] about the architecture of hoodie at this point um when you sign up every user gets their own
[1700.16 → 1705.16] personal database um and that's in couch we create a database, and it's just assigned to you
[1705.16 → 1710.80] and no one else can read it, but you can read and write to it and that's where we synchronize all your
[1710.80 → 1718.82] data to and so when you're working offline you are you can create um task documents in the case of
[1718.82 → 1724.16] sending an email and these are special documents that have like a prefixed id that kind of indicate
[1724.16 → 1730.18] that it's a task, and they get picked up by the plugins in the back end um and so if you wanted to
[1730.18 → 1734.80] send an email then cancel it what would happen is you would create the task document in your personal
[1734.80 → 1741.78] offline version of your data database um then you could potentially cancel it and delete it, and it would
[1741.78 → 1747.30] send it up to the server, but it would say by the way this was deleted so gotcha
[1747.30 → 1753.82] another thing you one of the on the blog post the big bold aside says we can't keep building apps
[1753.82 → 1759.08] with a desktop mindset of permanent fast connectivity where a temporary disconnection or slow service is
[1759.08 → 1764.72] regarded as a problem and communicated as an error uh that's true obviously on an on like a cell phone
[1764.72 → 1769.28] or something you said you get on the tube which I'm an ignorant American I believe that's like the
[1769.28 → 1776.30] train or the metro, and it's subway yeah and um you lose connection and all of a sudden like
[1776.30 → 1781.48] your apps stop working so let me ask you're kind of have two different directions that both are
[1781.48 → 1786.08] improving right so you want to go offline first but at the same time as our world is dedicated to
[1786.08 → 1791.42] making it so that you wouldn't lose your service when you get on the tube so offline first is
[1791.42 → 1796.14] incredible, and it's, and it's awesome but you kind of want both of those things right the goal is to
[1796.14 → 1800.92] never be offline if you don't want to be and if you are offline to support that and not kind of
[1800.92 → 1809.68] not be an exceptional case true um you know the more connectivity we get the better, but we are so
[1809.68 → 1816.04] far away from ubiquitous you know broadband I mean it's so far down the line as you know looking at
[1816.04 → 1821.84] looking at how things are right now um we've got an awful long way to go, and it's not it's not good
[1821.84 → 1827.96] enough to just kick the can down the road and wait so um in terms of my own background I've been
[1827.96 → 1833.20] consulting on offline web apps for a couple of years um and that's been in quite remote places
[1833.20 → 1838.22] so I've done things in the kind of far north of Canada and worked with charities out in Africa and
[1838.22 → 1843.82] obviously in those places they're quite a long way off getting reliable internet connections um
[1843.82 → 1848.42] uh you know in the case of the north um the Northwest Territories where I did a project
[1848.42 → 1852.64] they have a satellite for their internet connection which is your know it's pretty expensive
[1852.64 → 1858.30] um, but it's its reasonable uh if it goes down they have to fly an engineer out it might take a
[1858.30 → 1863.30] couple of days uh you know there's for people like that there isn't really an alternative
[1863.30 → 1869.64] um on the horizon anytime soon and these people a lot and because of the offline first kind of not
[1869.64 → 1875.28] not really existing until you know recently, or you know you've been recently saying the last few years
[1875.28 → 1880.62] um man these people when things go down they just sit idle for a few days right I mean they just
[1880.62 → 1886.06] kind of just for lack of better words are just kind of screwed yeah exactly I mean you know how
[1886.06 → 1892.90] bad it is if GitHub goes down for an hour or two uh you know it's its it's crazy there's no need for it
[1892.90 → 1898.64] cool so yeah offline first the solution is use something like hoodie and be able to maintain
[1898.64 → 1904.56] state even if they're not connected, and it's not exceptional case any more exactly and I think there's
[1904.56 → 1911.94] there's kind of also a bigger point here um in kind of the idea of empowering users
[1911.94 → 1918.92] is also tied up with the idea of being able to go offline so I like to think of being you know we have
[1918.92 → 1923.04] view source to look at your markup your CSS your JavaScript I would love to be able to do that with my
[1923.04 → 1932.06] data um and so separating your data from the kind of hosted back end is quite an empowering thing to
[1932.06 → 1937.84] think about I mean you're probably aware of uh unhasted and their remote storage that's that's
[1937.84 → 1944.28] taking a very similar approach and thinking in terms of your data is a separate entity right
[1944.28 → 1951.12] yeah it's an uh I don't know I look at it and I look at services and I look at like the tools that
[1951.12 → 1955.70] are available but i I don't know that I well I guess you're saying you know there would
[1955.70 → 1959.26] necessarily there would be a good front end for that for a user to kind of be able to look at that
[1959.26 → 1964.88] stuff when you talk about view source I mean isn't that more targeted at the developer
[1964.88 → 1970.10] anyway I mean most people don't even know that there's a such thing as a source oh sure yeah i
[1970.10 → 1977.38] mean um I'm not necessarily saying everyone is going to be inspecting their Jason data right um that's
[1977.38 → 1983.34] not going to happen but um the more people that do the better right uh when I used to work at a large
[1983.34 → 1988.14] company, and it used they use Lotus Notes are you familiar with Lotus Notes oh unfortunately I am yeah
[1988.14 → 1995.88] yeah some a fairly unpopular groupware um piece of software it's its often just used for email
[1995.88 → 2001.30] which is a shame because it actually has this these great um kind of replicating databases that
[2001.30 → 2007.98] you can take offline, and so I remember working in this company, and you could um take essentially an
[2007.98 → 2014.14] app it was an app with some data associated with it uh you could replicate it offline um onto my laptop
[2014.14 → 2019.50] and I could just play with it, I could change things around I could um modify stuff and I didn't have to
[2019.50 → 2025.44] worry about messing with the data because it was my copy um and i I thought that was really empowering
[2025.44 → 2031.90] and it in that organization it really worked we had um you know little apps running on a box under the
[2031.90 → 2040.04] desk in someone's cubicle that would um organize the Christmas party or for booking holidays uh if you know
[2040.04 → 2046.42] it was great and I would love to see increased hackability of the web I think one of the problems
[2046.42 → 2051.60] that we have at the minute is we think of the web in terms of full stacks, and so we have the back end
[2051.60 → 2057.14] and the front end it's all really tightly integrated and the problem with that is you can't make changes at
[2057.14 → 2063.84] any point in that stack without recreating the full thing and that's why you know you have these um
[2063.84 → 2070.76] you have to download an entire VM to run a piece of software I don't know if you tried setting up
[2070.76 → 2076.76] things like git lab it you know it takes a while it's a real pain um, and you know the more independent
[2076.76 → 2083.00] we can think of the front end from the app but also the app from the back end and all the infrastructure
[2083.00 → 2091.22] the more opportunity there is to play around and have fun with it speaking of having fun with it lets uh
[2091.22 → 2095.16] let's pause for a minute I'm not sure if that's a good transition or not but I liked it yes kind of
[2095.16 → 2101.50] awkward uh let's pause for a minute give a shout-out to our sponsor top towel not sure if uh is you've
[2101.50 → 2105.36] heard of top before, but they'll be sponsoring the show for the next few months or sorry the next
[2105.36 → 2111.66] few next few weeks my bad it's just uh Frisian slip there uh but for those of you who are freelancing
[2111.66 → 2115.62] which might be it might be everybody I don't know I don't know who freelances out there but uh for
[2115.62 → 2121.50] those of you who are freelancing or would like to test out freelancing or even try out a no risk
[2121.50 → 2125.52] kind of freelance like project while maintaining your full-time position you have to check out top towel
[2125.52 → 2132.62] uh you can work on special projects with companies like Airbnb RC idiom and many others you can work
[2132.62 → 2138.32] remotely or as Andrew likes to do work on a beach or pretty much anywhere in the world because it's the
[2138.32 → 2143.26] kind of opportunities they offer at top towel you can get started uh today head to top towel.com
[2143.26 → 2149.74] slash developer that's t-o-p-t-a-l dot com slash developer and click join the best and because
[2149.74 → 2154.32] they want to work with only the best senior engineers they've got a well-thought-out four
[2154.32 → 2159.42] stage screening process that begins with a personal call via Skype to get to know who you are and
[2159.42 → 2164.20] introduce you to top towels mission to see if you're a fit from end to end the entire screening
[2164.20 → 2170.94] process includes an English speaking test timed algorithm tests uh technical interviews with core
[2170.94 → 2178.76] top towel engineers as well as a test project but once you've made it through their rigorous screening
[2178.76 → 2184.58] process the sky is the limit if you think you have what it takes head to top towel.com slash
[2184.58 → 2191.70] developer that's t-o-p-t-a-l dot com slash developer to get started tell them the changelog sent you if you
[2191.70 → 2197.12] apply please email me Adam at the changelog.com I want to hear about your experience but uh top towel.com
[2197.12 → 2206.94] slash developer, so no back end no database offline so I wanted to the reason I got into the asking
[2206.94 → 2213.60] about the uh viewing your data kind of on the front end I'm looking at your website and one of the
[2213.60 → 2218.14] things that I see I like the way that you guys are doing the uh the features and who is it for
[2218.14 → 2224.10] kind of it's complete it's your next it's planned I think that's a neat idea it's a little I think I don't
[2224.10 → 2227.82] think there's anything marked as your next, or we're on if it's hard for me to kind of see the light yellow
[2227.82 → 2235.20] from the bright yellow but anyway uh planned who is it for is designers with basic front end skills
[2235.20 → 2241.88] so you guys are already kind of completed it for node developers and front end developers um it's planned
[2241.88 → 2246.74] for designers with basic front end skills what would you say those basic front end skills are
[2246.74 → 2255.98] um so we have the idea of a hypothetical uh jQuery developer and so um perhaps you're a designer and
[2255.98 → 2261.94] you can code up an interaction um you can kind of make a few basic things happen on the front
[2261.94 → 2269.38] end, but you're not implementing complex um algorithms in JavaScript on the front end that's all
[2269.38 → 2274.86] gotcha so you're so that this is increasingly what kind of the world is moving to for designers which is
[2274.86 → 2278.72] you have to be able to pretty much do you know mock-ups and prototypes and understand a little
[2278.72 → 2283.78] bit of jQuery so essentially you're saying like I mean the goal in a year you know a year from now
[2283.78 → 2290.48] three years from now then it could just be every designer is able to build a hoodie app well uh that's
[2290.48 → 2295.98] an ideal to strive towards right I mean every step we take in that direction is a good thing in my
[2295.98 → 2301.34] opinion the more people that get to create apps the better apps we'll have so let me ask you I think a lot
[2301.34 → 2307.20] of my designer friends so I don't know let me rephrase a lot of my developer friends when you
[2307.20 → 2312.94] don't understand something your first inclination is you know RTFM right read the docs figure out what's
[2312.94 → 2317.90] going on solve the problem and I don't think there's anything wrong with my designer friends
[2317.90 → 2322.28] but a lot of times that's not their first thought to read the doc so how do you guys kind of accomplish
[2322.28 → 2327.36] that how do you get you're the designers to uh go through and read the tutorials read the docs figure
[2327.36 → 2333.32] out how to solve their problem that's an interesting question I'm not sure I read the docs
[2333.32 → 2341.02] to be honest nice um I think you know for people like that it's its more about creating
[2341.02 → 2346.90] and they'll learn through creating something that they want to create that's that's why that's the
[2346.90 → 2352.20] reason they're programming it's not for the love of programming necessarily um, but it's because they
[2352.20 → 2359.68] have a dream of this perfect app, and they want to just make that happen and so the more closely
[2359.68 → 2365.06] we can align what we provide with just getting things done I think the more successful we'll be
[2365.06 → 2371.42] right and when you speak to is it is so easy to get up and running with hoodie that that barrier of
[2371.42 → 2379.32] getting started is almost um almost gone now when I say easy like I understand homebrew and I understand
[2379.32 → 2384.58] how to install modules with NPM right I understand what's happening with that stuff so is there any um
[2384.58 → 2389.86] is there any desire to like I don't know maybe have like a standalone install or anything that kind
[2389.86 → 2394.96] of makes it easier for people to get started um yeah we certainly want to make it easier for people
[2394.96 → 2401.64] to get started I mean at the minute it's its what you would call a developer preview, and we're
[2401.64 → 2407.28] basically expecting you to be some kind of node.js developer or comfortable with Linux or using homebrew
[2407.28 → 2410.40] or something like that I was going to say because you're obviously getting started off with
[2410.40 → 2416.02] brew you have to you know you got homebrew in place you got NPM in place and I know even there's a lot
[2416.02 → 2422.54] of assumptions already yeah I mean even for us one of our top hit um one of our top hit articles I think
[2422.54 → 2428.22] over the last couple of months has been how to get node installed, and it's like if that's like the number
[2428.22 → 2433.06] one search we're getting hits for people are wanting to know how, and it's not exactly easy for
[2433.06 → 2440.46] uh what Andrew's talking about this you know your designer buddies absolutely um so in the
[2440.46 → 2447.30] longer term we definitely want to tackle that uh there are a few options available uh one it might
[2447.30 → 2452.76] be to look at uh offering a hosted platform or perhaps a variety of hosts offering hoodie that would
[2452.76 → 2459.30] be great too um so that you could just click, and you're up and running um another option might be
[2459.30 → 2465.78] that we offer things like VMS or docker or something like that gotcha um and in terms of
[2465.78 → 2472.32] the node developer because we're based on couch dB um we've actually been experimenting a little bit
[2472.32 → 2477.86] with the idea of running pouch dB on top of level dB so if you're a node developer you're probably
[2477.86 → 2484.14] familiar with level dB it's a key value store from Google, but it has great uh node.js bindings
[2484.14 → 2488.74] and so what that would mean is we could potentially get to a stage where the installation process is
[2488.74 → 2494.82] NPM install hoodie and that would be fantastic so um there are lots of things we could look into
[2494.82 → 2499.08] uh it's certainly not going to stay the way it is that's well that's one good thing about the way
[2499.08 → 2503.98] you're doing it now though however is that I think you know Angie early in the show you touched on
[2503.98 → 2509.00] Bauer coming on the show soon and things like that and I think as we start to see more and more of
[2509.00 → 2515.26] these front-end tools becoming more accessible to, or you know using NPM for example to install
[2515.26 → 2519.60] uh packages and all this different stuff like it's becoming more and more accessible because of things
[2519.60 → 2524.48] like grunt and Bauer they're pushing front-end developers or front-end designers as you say
[2524.48 → 2531.44] um to start to get into more developer-issue things and having homebrew in place and having NPM in place
[2531.44 → 2536.74] is getting more and more common for the I think you're at least your initial like you said a developer
[2536.74 → 2542.32] preview that initial stint of people you want to have tried out hoodie and you know take on
[2542.32 → 2548.52] this flag and run with it yeah for early adopters I think it's reasonable to tell you
[2548.52 → 2555.74] have NPM installed uh you know, or you can use git or something like that um one other option that
[2555.74 → 2562.62] we discussed at one point was the idea of um so one of the workflows I really enjoyed was um google
[2562.62 → 2567.62] analytics so a lot of front-end developers are really comfortable with the idea of copying and
[2567.62 → 2572.00] pasting a snippet of code and just putting it into their site however they host it normally whether
[2572.00 → 2580.68] they ftp it to some shared hosting or whatever and um I really like the idea of offering um a hoodie
[2580.68 → 2585.24] tag so you get a little snippet of hoodie code you paste that into your site wherever that is
[2585.24 → 2589.84] wherever you're comfortable hosting it and all of a sudden you can talk to a hoodie back end I mean
[2589.84 → 2597.14] that would be that would be really nice um design and with cores and various other tools that that's
[2597.14 → 2604.04] potentially achievable yeah so we talked about uh you guys just kind of released plugins that was
[2604.04 → 2611.48] November 3rd so just a couple of days ago um but what are you guys doing now and what is the future we
[2611.48 → 2615.72] talked about kind of some pipe you know not pipe dreams but kind of like bigger picture future plans
[2615.72 → 2621.36] so what's like the immediate future look like for hoodie um well right now we're all kind of busy
[2621.36 → 2627.80] off doing talks and various other workshops and things um so I'll be at icon next week in San Francisco
[2627.80 → 2633.56] uh so we'll Gregor so if you're around there come say hello um Jan will be up in Vancouver
[2633.56 → 2639.92] uh so in the immediate future we're all kind of busy doing that the next to-do item in terms of
[2639.92 → 2647.54] creating hoodie is probably going to be on the admin interface um so uh we really like these
[2647.54 → 2652.78] kind of nice small panels that you get in admin interfaces with all the graphs and all that kind
[2652.78 → 2658.34] of stuff people like numbers and whizz graphs and so um you know if you can just kind of click a
[2658.34 → 2662.94] button you get a back end uh you start creating users, and you get stats and all that kind of stuff
[2662.94 → 2668.50] just by default that would be fantastic um so yeah i think admin interface is the next big thing
[2668.50 → 2675.32] do you guys have your sponsors lined up for the next few weeks um yeah I think so I don't know i
[2675.32 → 2681.28] don't handle the sponsorship myself but uh so I just wanted to plug if you're interested in
[2681.28 → 2688.26] sponsoring hoodie development just go to hood.ie sponsoring.html get some information and help, help
[2688.26 → 2696.08] this project grow yeah absolutely thanks very much so for those of you that are new we ask the same
[2696.08 → 2700.00] three questions at the end of every week we need to name these questions we need to come up with uh
[2700.00 → 2705.08] the common questions I don't know the common questions that is the uh that is the work the
[2705.08 → 2709.66] working name the common questions until we come up with something better but yeah we'll go ahead and
[2709.66 → 2718.18] ask them here um the first one Caitlin is for kind of call to arms so uh something you would like to
[2718.18 → 2725.80] see the community kind of get involved with and help out um sure so I think um the most useful thing
[2725.80 → 2732.82] you could do if you're interested in the project is to um come along have a look at the APIs discuss
[2732.82 → 2739.10] the whole concept of no back end and just try out the code if you're a node.js developer, and you want
[2739.10 → 2745.66] to really get your hands dirty then please have a think about doing some plugins uh so we're really
[2745.66 → 2752.36] nice on plugins right now we just have like the small core things uh users email um we're working
[2752.36 → 2757.68] on doing uh data sharing between users uh, so there are loads of things that you could potentially
[2757.68 → 2763.56] implement uh all kinds of services that you might want to integrate with on the back end um so plugin
[2763.56 → 2769.10] developers is the big thing we need how do you get involved with plugin development
[2769.10 → 2777.00] um so you can if you go to hoodie HQ on GitHub there's a whole load of repositories there you'll
[2777.00 → 2783.78] find a few examples we tend to prefix everything with uh hoodie dash plugin uh if you want to ask us
[2783.78 → 2791.00] questions then we're on free node so if you join um hash hoodie on free node we're usually in there and
[2791.00 → 2795.80] someone will help you out uh we're really excited when people want to write plugins so we'll be very
[2795.80 → 2801.88] friendly to you awesome so hoodie plugins that's yeah that's something we didn't get into much this
[2801.88 → 2806.12] time but maybe we can have you guys on when it starts to grow and kind of talk about the ecosystem
[2806.12 → 2813.32] a little bit more sure uh second question is for if you weren't doing this what would you be doing
[2813.32 → 2821.28] I would probably be working on one of the thousand other ideas I have in my head for uh open source
[2821.28 → 2827.42] projects uh the great thing about working with this team is that they kind of help keep me on track with
[2827.42 → 2833.40] one specific thought for a long period of time which is nice um but i I'd love to give a really
[2833.40 → 2838.54] balanced answer you know like I'd be off sailing or travelling the world but I'm just going to be programming
[2838.54 → 2844.82] I love programming well if you're maybe if you're being paid to do all of your open source ideas you
[2844.82 → 2848.78] could be sailing and doing them you know in the middle of the ocean on a boat somewhere sure yeah you
[2848.78 → 2853.76] know especially since you would have offline access all the time so if anyone wants to sponsor me to
[2853.76 → 2859.26] sail around the world and program than uh get in touch yeah it's hood.ie slash sponsoring dot no just
[2859.26 → 2866.18] kidding uh cool, so the last one is for a programmer hero so somebody that has been influential in your
[2866.18 → 2872.72] life that's that's a tricky one I meet so many great programmers every day I think every programmer is
[2872.72 → 2879.44] better than me so I always have something to learn um but for a specific example I think I'm going to go
[2879.44 → 2887.62] with uh jerry Sussman so one of the guys behind scheme along with guy steel i um, but also he was
[2887.62 → 2893.66] involved in the sick the structure and interpretation of computer programs I think programming is all about
[2893.66 → 2900.58] communication and if you're able to communicate really well um in terms of you know the clarity of
[2900.58 → 2905.34] designing a language like scheme but also um if you've not seen the video lectures the MIT
[2905.34 → 2912.42] um videos of sick then you should definitely watch that um anyone who has the gift of kind of
[2912.42 → 2918.26] communicating clearly in code I'm in or of I think that's fantastic yeah the book structure and
[2918.26 → 2922.10] interpretation of computer programs we uh I remember when I went through my computer science program
[2922.10 → 2928.44] in college we read that book, and we called it the sick book I think that we didn't I wish I would
[2928.44 → 2933.10] be able to go through and read and take all my courses again now with the appreciation and kind
[2933.10 → 2938.32] of education knowledge that I've gained over the years I think I would enjoy that uh much more this
[2938.32 → 2946.10] second time around well um perhaps I just enjoy it because I didn't do computer science yeah, yeah maybe
[2946.10 → 2952.04] it was a little bit more of an uh homework assignment than uh than a know reading yeah if someone
[2952.04 → 2955.00] if someone sat me down and forced me to read it I'd probably hate it
[2955.00 → 2960.76] awesome yeah so hoodie is uh you guys are definitely growing and um I think we could
[2960.76 → 2965.46] talk about it for hours I say that with most of our guests because most of our guests are awesome
[2965.46 → 2969.90] just like hoodie uh but for the sake of keeping it you know under an hour or so I think we're going to have
[2969.90 → 2975.88] to let you go but yeah I definitely am excited to see kind of where this thing grows and to
[2975.88 → 2981.14] keep a track keep an eye on it if you guys want to follow hoodie they do have a hoodie weekly
[2981.14 → 2989.70] which is weekly.hood.ie, and you can find them on Twitter at hoodie HQ well-spoken man yeah
[2989.70 → 2998.26] yeah, thanks so much for having me so Caitlin uh yeah I mean I think the thing that's kind of
[2998.26 → 3003.74] neat I think just to kind of summarize this is like this idea of being able to build apps pretty quickly
[3003.74 → 3008.48] uh you know and this front end, or you know front end kind of focus I was thinking about
[3008.48 → 3012.64] Ender game Andrew from earlier when you were mentioning in hip chat saying front Ender but
[3012.64 → 3017.54] uh but being able to build an app in just a few days pretty quickly and not have to think about
[3017.54 → 3021.94] you know the back end and servers and all this stuff I mean what you guys are doing at hoodie are super
[3021.94 → 3026.06] super cool and Andrew you mentioned it earlier for anybody listening out there that wants to sponsor
[3026.06 → 3031.66] these guys you know definitely look into that this is a cool neat technology Kaylin you're
[3031.66 → 3036.76] out there and yawn and the rest of the team are out there giving talks at various um you know
[3036.76 → 3042.10] either conferences or local communities or whatever um you know user groups and whatnot I mean
[3042.10 → 3046.14] support these guys what they're doing it's super neat Kaylin thank you for coming on the show to
[3046.14 → 3051.62] to kind of share with us this idea of no back and this idea of offline first and for you the listeners
[3051.62 → 3058.00] um definitely check it out we'll have a bunch of links in the show notes um we've mentioned yon a
[3058.00 → 3062.60] couple times he's been on the show twice before once way back in the day when when when and I were over
[3062.60 → 3067.74] there in Austin uh for a south by southwest long ago there was a no sequels pack down that was
[3067.74 → 3073.00] a little dated but I'm sure entertaining nonetheless um and yon has been on the show talking about couch
[3073.00 → 3078.78] dB before as well so I've got links out to that and a bunch of cool stuff but Kaylin thanks for
[3078.78 → 3084.10] joining us this show for sure and uh well I also want to just thank our sponsors uh digital ocean and
[3084.10 → 3088.84] top towel if you're um if you haven't used digital ocean yet, and you want to take advantage of them
[3088.84 → 3092.42] they have a ten dollar hosting credit with us, I mentioned earlier in the show that the
[3092.42 → 3099.12] the code you want to use is changelog sent me that's changelog sent me whenever you go through
[3099.12 → 3103.46] the process of creating your account uh and putting in your credit card information there's a little
[3103.46 → 3106.88] spot there to put that code in their go ahead and throw them there they'll give you a ten dollar
[3106.88 → 3111.86] hosting credit and if for some reason it doesn't work out or doesn't actually apply to don't worry don't
[3111.86 → 3116.72] go on Twitter and be upset just email their support is like super quick I was emailing
[3116.72 → 3122.66] their support last night because I was setting up a slice for myself which is awesome um and if you
[3122.66 → 3127.90] are a fan of what they're doing, and you're going to be at launch hackathon at tell is going to be
[3127.90 → 3133.14] there if you've read any of their tutorials at tell is likely one of the ones that's that's written
[3133.14 → 3136.62] them I know that everyone I've been reading of their tutorials that's been written by at tell so
[3136.62 → 3142.18] at tell is uh is one of their main communications contacts at digital ocean she'll be at launch hackathon
[3142.18 → 3147.10] that's uh I think that's next week uh wait what day is today's the seven that's like this
[3147.10 → 3152.80] weekend November 8th through 10th um and if you want stickers email Barry at digital ocean.com
[3152.80 → 3157.84] I'll send them to you uh just tell me your address but uh I want to thank also top towel uh join
[3157.84 → 3164.02] top towels network of awesome engineers all around the world and uh go to top towel.com
[3164.02 → 3171.22] slash developer to apply that's t-o-p-t-a-l.com slash developer to apply and uh yeah that's that's
[3171.22 → 3175.46] it for this show Angie thanks so much for a really awesome show and Caitlin thank you so much for
[3175.46 → 3181.84] taking the time to join us today so let's say goodbye see you guys later yeah, thanks for having me
[3194.02 → 3204.74] you
