[0.00 → 13.38] you're listening to JS party a weekly celebration of JavaScript and the web join our community
[13.38 → 19.68] why don't you at JS party.fm slash community it's a totally free place to hang with like-minded
[19.68 → 25.66] developers from all around the world the best part high signal low noise nice people big thanks
[25.66 → 31.74] to our partners at fly.io launch your app as close to your users as possible that's the ticket find
[31.74 → 35.94] out how at fly.io okay it's party time you all
[35.94 → 60.72] hello JS party listeners uh it's me your host for the week my name is Amal Hussain and this is
[60.72 → 68.94] JavaScript party oh wow that sounds weird JS party um a weekly celebration of JavaScript and the web
[68.94 → 75.88] with me today is like someone who I've missed so dearly um it's been like a while since we've been
[75.88 → 80.54] on a show together we both had a lot of life happening in different ways uh, but I'm just so
[80.54 → 87.44] happy that you're here now and back good life not bad life but anyway so hello Nick welcome
[87.44 → 93.16] ahoy hoy Amal I've missed you too I missed you I missed you a lot so very excited, and we're like
[93.16 → 98.46] we're back together again talking about a really amazing topic today um we're going to be talking
[98.46 → 103.14] about Core Web Vitals, and we're going to be meeting the new kid on the block
[103.14 → 111.14] INP pretty mouthful to say it interaction to next paint um a lot of alphabets are going to be
[111.14 → 117.00] mentioned in today's show, so no alphabets will be harmed hopefully in the making of the show though
[117.00 → 121.84] and so with us today are two very, very special guests we're um really it's an honour to have them
[121.84 → 128.12] here um as kind of true shepherds of I think the Core Web Vitals and the project as a whole
[128.12 → 135.66] Annie Sullivan hello welcome hi nice to be here and Rick Viscous welcome hi thanks for having me
[135.66 → 139.62] yes happy he's happy to have you both here um so if you could tell us a little bit about
[139.62 → 145.78] yourself so Annie you're both on the Chrome team at Google Annie you're a tech lead or technically TL I
[145.78 → 150.04] don't actually know what the T and the L specifically stand for at Google is it like tech lead tech leader
[150.04 → 157.30] tech lead okay yeah you're the tech lead for Core Web Vitals which is huge and amazing and Rick you're
[157.30 → 162.32] a developer relations engineer working exclusively on like web performance so you're really familiar
[162.32 → 168.86] with a lot of the community pains and all the things you do like all the advocacy teaching you have
[168.86 → 175.14] to deal with the rest of us um, so I think we're really excited to have sorry yeah both of you here
[175.14 → 179.36] so I don't know why don't you tell us a little about yourself Annie do you want to start uh yeah, so I'm a
[179.36 → 184.62] software engineer uh on Chrome web platform team I lead the speed metrics team who develops the core
[184.62 → 191.68] vitals metrics and we also uh lead Chrome's uh work with the web performance working group on performance
[191.68 → 198.04] APIs we have a new API called long animation frames but also existing APIs like resource timing and
[198.04 → 205.12] navigation timing very cool and what's it like to like to be a TL on the Chrome team like that feels like
[205.12 → 210.88] a really hard job you know specifically because you're like nerd you're the nerd boss of all
[210.88 → 215.72] the nerds like that it is so much fun I think at Google you don't really get to be the boss of anyone
[215.72 → 221.50] but you get to really um help a lot of people right uh, so my team is awesome and amazing, and they've
[221.50 → 226.20] got all these ideas and just kind of helping them get everything running in the right direction and
[226.20 → 233.08] enabling them to do really, really cool work it's its so much fun so for example we asked Noam on
[233.08 → 240.08] my team to figure out how to make long tasks more debuggable, and you know he came up with this
[240.08 → 244.50] whole real uh thought around that tasks aren't really the right breakdown that we should be looking
[244.50 → 250.54] at frames, and he made this long animation frames concepts and really just being able to support
[250.54 → 255.80] him and getting it out there it's really exciting very, very cool, and you've worked at Google for 19
[255.80 → 262.80] years is that correct uh yeah that's yeah it's been a long fun journey that's amazing yeah that's
[262.80 → 267.44] like another podcast we'll have to have you back tell us about you know what it's like uh to kind
[267.44 → 274.42] of ride that wave I'm sure you have amazing stories and so Rick hello and welcome hi, so please tell us
[274.42 → 280.12] about yourself sure so I lead the web performance developer relations team uh which is part of Chrome
[280.12 → 286.42] and I'm basically responsible for helping developers understand how to make their websites faster and
[286.42 → 292.30] succeed with Core Web Vitals I work a lot with Annie and her team as well as the other uh cross-functional
[292.30 → 297.34] teams that together work to make the web fast that's that's exciting also sounds like a very hard job
[297.34 → 306.04] right Nick like that's that's like ultimate herding cats pretty much that's like you're like talking to
[306.04 → 312.36] to all of us about our JavaScript uh and needing to kind of you know trim some of that so
[312.36 → 317.84] it's like it's our job yeah there is a there is an inherent tension that I feel like
[317.84 → 321.62] developers when I say we need you to make your website faster it's like but what about all of
[321.62 → 326.38] the other things I need to do on my website like I need that JavaScript I need that third party so
[326.38 → 330.60] I guess my job is to convince them that there is that trade-off to make is that what it usually
[330.60 → 336.10] comes down to is uh you should delete some JavaScript and then you'll be good it helps
[336.10 → 342.26] I think we have to really use data to make an effective argument that like you're using it in
[342.26 → 346.42] an inefficient way, or you're not using it at all, and it would help your performance if you removed it
[346.42 → 351.96] my favourite thing to do is like an b test even if just like is it's a local web page test run with
[351.96 → 356.78] and without something I find that really opens up people's eyes to the costs of what they're
[356.78 → 362.66] doing on their website oh my god I just had the most weird mental visual about performance
[362.66 → 368.08] auditors and advocates and engineers like in the sense that like it feels like we're like in the
[368.08 → 374.44] matrix and like JavaScript web developers are just addicted to JavaScript and like you guys are like
[374.44 → 379.64] the agents that just show up and like try to curb the addiction you know just be like to put it down
[379.64 → 386.36] it's possible you can do this you know walk away ship less JavaScript the matrix
[386.36 → 391.96] the matrix version of the bobs from office exactly what would you say you do here JavaScript
[391.96 → 398.64] exactly, exactly oh my gosh well, well Annie and rick we're like thrilled to have you here, and we have
[398.64 → 404.78] a really packed show we have like an I have a very ambitious agenda of talking points we're going to
[404.78 → 410.16] hopefully talk about what are Core Web Vitals you know, and we want to dig into imp which is like
[410.16 → 416.70] going to be a very uh an official Core Web Vitals soon, soon like March soon right like very soon
[416.70 → 422.20] Annie I think weeks away weeks away from being official um so we're gonna you know
[422.20 → 427.68] hopefully get you prepped for that, and we want to talk about the ecosystem and tooling and rollout and
[427.68 → 432.90] all kinds of stuff um you know how do you how do you measure how do you test so lots to discuss over
[432.90 → 438.88] the next hour, but first we wanted to kind of set some definitions briefly um just because you know
[438.88 → 444.98] not everyone's familiar with the way things work under the hood for browsers right, so there are words
[444.98 → 451.34] like main thread event loops long animation frames which Annie used in her intro by the way it's like
[451.34 → 457.74] probably the first time anyone's ever used long animation frames and like or like laughable yeah deep
[457.74 → 464.34] browser internals in their intro so it's like some pretty hardcore nerd needing out Annie, but you know
[464.34 → 468.42] so we want to kind of set some terms so we're going to first start with the first term
[468.42 → 474.54] before we dig in so Annie and rick what are what's the main thread yeah, so the main thread is generally
[474.54 → 480.36] uh where all your code runs when you run JavaScript or when you like to add things to the Dom on a web page
[480.36 → 487.22] and in general the way that the programming model of the web has historically been designed like you
[487.22 → 493.24] run some code, and it just runs immediately and blocks all user interfaces so you'll see a lot
[493.24 → 498.94] of stuff in performance uh guidance don't block the main thread don't hog the main thread break up the
[498.94 → 504.54] main thread get off the main thread, and so we'll talk a lot more about what that means uh for users
[504.54 → 511.10] right and uh why all those things are important yeah great summary so what about event loops
[511.10 → 515.24] how would you define that well I think the best place to send anybody who wants to learn more about
[515.24 → 520.18] the event loop is Jake Archibald's talk it's called in the loop so I still refer back to if it's many
[520.18 → 524.64] years old, but it still holds up uh it's also really effective with the way that it visualizes the event
[524.64 → 529.64] loop it's you can literally think about it like a wheel turning and at any point you're at a different
[529.64 → 535.58] phase in the loop one way that I could describe it is the process that the browser uses to
[535.58 → 541.44] accomplish work that is on the main thread there are tasks that need to be executed there are visual
[541.44 → 545.34] updates that need to happen on the screen and things that happen in between at various times
[545.34 → 551.40] and so the event loop make sure that the tasks keep happening, and the queue is consumed and work
[551.40 → 557.16] happens in a timely fashion I always relate this to like a video game loop whether that's more
[557.16 → 561.92] confusing or less confusing it is makes more sense to me because a video game constantly has to check
[561.92 → 567.48] the status of everything and then issue updates and the browser is doing a lot of the same thing
[567.48 → 572.12] exactly yeah there's work to do and then there are updates that need to happen sometimes there isn't
[572.12 → 576.74] work sometimes there aren't updates and the event loop just turns and doesn't actually do anything
[576.74 → 584.32] when the browser thread is idle, but eventually things will come in for example like a timeout script
[584.32 → 589.78] will just pop in out of nowhere and then get added to the task queue, and it will need to happen and so
[589.78 → 595.12] on the next turn of the event loop you can find out you can discover that work and execute it
[595.12 → 600.70] it really helps to think about the event loop in this way because of like if you ever heard of
[600.70 → 605.66] like the double raft the double request animation frame why is it double why don't you just do it
[605.66 → 612.78] once, and it only clicked until I saw Jake's uh explanation of it and where the request animation
[612.78 → 618.80] frame actually executes right before like the layout and paint work and so by letting it turn
[618.80 → 623.88] twice you can make sure that you update at the time that you expect so it's a helpful model to think
[623.88 → 628.44] about the web browser in the main thread that was a really excellent summary so just wanted
[628.44 → 634.48] to say points rick uh for explaining that in a way that was yeah um much less scary you know and
[634.48 → 638.92] hopefully we can do actually a deep dive on that with Jake I think it's a great topic to dig into
[638.92 → 644.22] like if you take a whole hour really talking about it all right so next on our list what are long
[644.22 → 650.32] animation frames yeah so going back to that concept of like an event loop being like a video game
[650.32 → 655.90] loop right a video game has a frame rate and uh I think we forget a lot a web page also actually has
[655.90 → 661.00] a frame rate it's producing frames when things are animating so like on this video right every
[661.00 → 665.84] every frame of the video the web page is producing a frame uh when we have like an animation it produces
[665.84 → 671.12] a frame when you interact with the page it produces a frame like your button gets highlighted or
[671.12 → 677.96] whatever the menu shows up that that's a frame and so um like the word frame is overloaded like iframe but
[677.96 → 681.78] but here we're talking about an animation frame which is a type of frame uh continually playing
[681.78 → 688.58] and a long animation frame is just one that took kind of too long more than the user would have liked
[688.58 → 695.16] so it's like beyond the threshold of like what's considered like what is it 60 I'm forgetting the
[695.16 → 703.82] metric now 60 frames per second would be like a 16.6 millisecond frame and I think depending on the
[703.82 → 708.94] use case you can have like a different threshold for a long frame a response to a user interaction
[708.94 → 714.50] an individual user interaction all of our user UDR says it should be within 100 milliseconds so
[714.50 → 721.30] if somebody clicked in that frame then really a long frame is over 100 milliseconds if uh you're trying
[721.30 → 727.80] to play a video game it's you know only 16.6 milliseconds, but you know movies run at a
[727.80 → 734.76] lower frame rate uh so that there's like some give in what is expected there and if you do have like
[734.76 → 740.58] a game or a movie you also or an animation you want to have a consistent frame rate it'd be better to run
[740.58 → 745.80] at 20 frames per second than to run at 60 with an occasional giant hiccup yeah no that makes a ton of
[745.80 → 751.44] sense and long animation frames are just kind of a way to say hey what happened when the animation frame
[751.44 → 758.26] was too long yep that makes sense thank you uh next on our list uh another overloaded term in
[758.26 → 762.38] computer science and with browsers responsiveness yeah so I could take yeah, and it's worth maybe
[762.38 → 767.42] noting that like responsiveness means a lot of things in a lot of contexts uh different contexts
[767.42 → 772.54] and maybe we want to focus on like what does it mean in this context you know what I mean exactly yeah
[772.54 → 777.40] in the context of today's conversation exactly we're not talking about responsive web design where
[777.40 → 782.70] if you like to resize your browser window things fluidly fill in so responsiveness in this context
[782.70 → 787.70] is about when the user does something on the page how long does it take for the browser to respond
[787.70 → 794.60] to that input and so you can think of interactions like a key press or a click or a tap on a touch screen
[794.60 → 800.64] as the user intending to do something on the page they expect something to happen near instantly and
[800.64 → 805.94] you mentioned like 100 milliseconds is generally the threshold that we look at, and so we want to make sure
[805.94 → 810.90] that the amount of work that happens between the user doing something and them getting any sort of
[810.90 → 816.12] visual feedback that's just the next frame that paints that happens as quickly as possible ideally
[816.12 → 822.12] under 100 milliseconds but as we'll get to later the metric that we use to measure this is actually
[822.12 → 829.22] permitting 200 milliseconds or less as the responsiveness threshold makes sense and yeah i that was like a
[829.22 → 834.36] trick question for me because i I was like we're going to use the word responsiveness a lot and i really
[834.36 → 842.20] wanted to make sure people knew like what specifically we meant so thank you rick and so our last kind of
[842.20 → 849.40] definition that we want to kind of uh put up front is interactions so what are interactions yeah so
[849.40 → 854.28] going back to like there's different time limits you want on an animation frame depending on what the
[854.28 → 860.68] user is doing a user interaction is you know at the base level it's an interaction with the page
[860.68 → 867.48] and um we're defining this for the purposes of interaction in paint and for the purposes of
[867.48 → 873.74] chrome performance API as what we call a discrete interaction uh that's a tap on a touch screen a click
[873.74 → 880.38] with a mouse or a press on the keyboard and um when my team went to go and make a formal definition
[880.38 → 887.04] for interaction one thing we realized is that like there's actually two user movements there you press
[887.04 → 893.22] the key down, and then you lift your finger up and so when we're counting interactions we're being like
[893.22 → 898.62] super careful not to like to penalize the web page if I took too long to lift my finger up so there's
[898.62 → 904.46] some uh complexity there but overall it's just a tap a click or a key press we're not including
[904.46 → 911.54] continuous interactions like scrolling because those are a lot more complicated to measure and a lot
[911.54 → 916.84] harder for web pages to act upon because uh we have this thing called GPU accelerated scrolling where like
[916.84 → 921.54] a lot of the scrolling isn't controlled by the web page if that makes sense yeah so chrome is kind
[921.54 → 927.48] of under the hood handling that for you wow that's so cool yeah I think i was curious why scrolling
[927.48 → 933.54] was left out I was like that feels like a huge area where we see a lot of bank you know and so thank
[933.54 → 939.16] you for explaining that all right so we're going to dig into like Core Web Vitals now just kind of at a high
[939.16 → 945.76] level we'll get into kind of the specifics uh in a bit more detail next but for now can you either of
[945.76 → 951.16] you kind of broadly define like what are Core Web Vitals right for the person who maybe has never
[951.16 → 956.52] heard of this thing and like why did this concept of Core Web Vitals become a thing in 2020 yeah so
[956.52 → 961.62] Annie maybe I can take what are they and you can give the context on how we got here so core web
[961.62 → 966.72] vitals you could think of as health metrics for the web like the word vital invokes that imagery of like
[966.72 → 972.80] taking your pulse or something like that so we want to make sure that webs the web pages and web
[972.80 → 978.06] experiences that users have been good and healthy and specifically the performance metrics we look
[978.06 → 984.24] at are loading performance and that is measured by the largest content paint metric interaction
[984.24 → 990.70] responsiveness and if you're watching this right now in uh maybe let's say March 2024 or later that
[990.70 → 995.74] metric is interaction to next paint but historically since the core of vital started uh that has been
[995.74 → 1001.54] the first input delay metric and the third one is uh layout stability which is measured by cumulative
[1001.54 → 1006.56] layout shift so Annie do you want to talk about how we got here with core of vitals yeah so I've been
[1006.56 → 1010.80] working on web performance for a really long time before I led core of vitals I led performance
[1010.80 → 1016.94] testing and tooling for chrome and my team and a lot of other teams in chrome were really trying to get
[1016.94 → 1022.76] like the best ground truth for like user experience metrics historically the on load event for the page has
[1022.76 → 1028.38] been the page load time and that has a formal definition of being like the time when all the
[1028.38 → 1032.78] the resources were loaded and the Dom is parsed and all that, and it turns out that it doesn't
[1032.78 → 1038.62] necessarily correlate with what the user's seeing so then we have all these different attempts to get
[1038.62 → 1043.40] closer Dom content loaded is a bit closer it turns out, but it's still like a formal definition that's not
[1043.40 → 1049.84] based on the user speed index is really great, but we can't measure that in the field first paint is actually
[1049.84 → 1054.30] pretty well correlated first conceptual paint is better correlated largest content paint is even
[1054.30 → 1060.40] better correlated but I think as you're listening to this you're like wow that's a lot of stuff right
[1060.40 → 1065.88] and we were just kind of like putting all the stuff out there other people were putting their ideas out
[1065.88 → 1072.28] there which is fantastic but if you try to dig into like web performance and what's important the fact
[1072.28 → 1077.98] that what we're trying to do what we're trying to do is make pages load fast is just totally overwhelmed by
[1077.98 → 1083.06] the fact that there's about seven million ways to measure that and so what we really wanted to do
[1083.06 → 1088.50] with co-op vitals was try and go back and go front and centre what's the user experience we're trying
[1088.50 → 1094.98] to measure and also really centre that around the user in and like ideally we're measuring that in the
[1094.98 → 1101.24] field when you just go and look like locally on your phone or your computer generally as a developer
[1101.24 → 1107.16] we're quite well off and things look great, or maybe we're not including all the um the production
[1107.16 → 1113.22] third parties and stuff like that, so things look great so we wanted to focus on key moments in user
[1113.22 → 1118.86] experience for real users and that's why we really drifted towards this like that's why we decided to
[1118.86 → 1125.66] do this core vitals program I'm curious how when we're thinking about this like the thing that always
[1125.66 → 1130.82] comes to mind immediately for me is something like lighthouse in dev tools i I don't think that
[1130.82 → 1136.62] that's it how do you how do you actually like interact with this stuff as a developer the tools
[1136.62 → 1141.38] that a developer might use to measure their Core Web Vitals yeah so Annie touched on
[1141.38 → 1147.44] uh field data and what that actually means is collecting data from your real users visiting
[1147.44 → 1152.04] your website and seeing how their experiences are distributed because there was no single
[1152.04 → 1158.08] number that can really describe the full diverse spectrum of experiences we assign things like
[1158.08 → 1164.40] percentiles like we'll say the 75th percentile imp experience is some specific number in milliseconds
[1164.40 → 1170.48] but really that's saying 25 percent of them are slower than that so when a developer tries to like
[1170.48 → 1175.74] debug their user experience they'll test it locally they might use a tool like lighthouse, or they might
[1175.74 → 1179.82] use like uh one of Google services like page speed insights that runs lighthouse under the hood
[1179.82 → 1186.34] those tools I would more think about as I know my site is slow how can I make it faster lighthouse will
[1186.34 → 1192.56] give you actionable guidance to say here are some opportunities we've identified but where I think it gets
[1192.56 → 1198.90] confusing is that there's also a lighthouse score and developers love to gamify the score they want
[1198.90 → 1205.02] to get the highest score it's like beating the game to get a hundred percent in lighthouse and that metric
[1205.02 → 1210.18] uh the score itself comes from the performance metrics that are under the hood in lighthouse so you'll get
[1210.18 → 1216.24] for example a speed index score a total blocking time score and all of these things together are computed
[1216.24 → 1222.60] into this aggregate weighted lighthouse performance score I think part of the confusion is that turns
[1222.60 → 1227.34] green people feel like their job is done when really you've just done all the things that lighthouse
[1227.34 → 1233.56] could find that are wrong on your page with whatever the test configuration was uh maybe you just loaded
[1233.56 → 1238.02] the page and didn't interact with it at all you didn't find out what the imp issues are
[1238.02 → 1242.70] you didn't scroll down if you did maybe you would have seen all these layout shifts of uh things loading
[1242.70 → 1247.50] in below the fold so that's what's really so important about field data is to see what are the
[1247.50 → 1251.34] users actually doing and how are they impacted by these performance problems that are almost like
[1251.34 → 1256.40] lying in wait that the tooling might not expose to you should you not think to go and test them yourself
[1256.40 → 1262.12] that's like a really, really great points rick I mean performance measurement is an art like it really
[1262.12 → 1268.26] and a science but like it really is its own field of study right because you really you need to your need to
[1268.26 → 1275.20] basically be a real user um you need to kind of make sure you're testing all the scenarios um really
[1275.20 → 1281.40] thinking about devices latency all this stuff right um what else is happening on that hardware uh
[1281.40 → 1285.38] there are so many different factors and Annie thank you so much for walking us through that like
[1285.38 → 1291.70] that history of like hey there are so many different ways we can kind of gauge like is this turkey cooked
[1291.70 → 1297.30] right like I can, you know put a measure here I can put a measure here like where is the right
[1297.30 → 1303.90] you know place um and so glad we've kind of landed on these three things four things now how has this
[1303.90 → 1309.14] sort of changed over time right because we have the largest comfortable paint which is like seems like
[1309.14 → 1316.44] it's been stable cumulative layout shift as well first input delay seems to be like the kid that's
[1316.44 → 1322.68] on the way out now in favour of imp and so like what other changes have happened over time since 2020
[1322.68 → 1327.22] is this is this it that those are like the kind of the major changes like as far as like
[1327.22 → 1333.54] what is the metrics that we measure we try to keep that as consistent as possible we find that um
[1333.54 → 1340.54] the fewer changes we tell developers about the more able they're able to focus on the things
[1340.54 → 1346.62] that are really important so we try not to make big changes we have really focused very hard on figuring out
[1346.62 → 1352.32] without taking giant changes let's make sure that we can listen to feedback from developers and help
[1352.32 → 1357.24] them act on it so most of the time when we take feedback we're improving our tooling uh, and we're
[1357.24 → 1363.36] improving like debug ability but sometimes um like right after the Core Web Vitals uh announcement we got a
[1363.36 → 1370.40] lot of feedback from frameworks that were doing server-side rendering that uh if you have the LCP exact
[1370.40 → 1376.56] same rendered exactly twice we count the second one instead of the first one and for us, we were like
[1376.56 → 1380.92] what why would you do that, and they were like server-side rendering its kind of a big deal um
[1380.92 → 1385.72] hydration this is really important for performance and if you want people to do this then you need to
[1385.72 → 1392.10] have the measure uh you know like show the second one the first one is when the user actually saw the
[1392.10 → 1398.44] content yeah the user saw the content and then nothing has changed for the user so in that case like that
[1398.44 → 1404.66] was perfect feedback and what we do when we make a change like that is we run like a live experiment
[1404.66 → 1411.44] on chrome traffic, and we can say like how many website scores are actually changing and for that
[1411.44 → 1417.12] change it was way less than one percent of websites were actually impacted, but it was really important
[1417.12 → 1421.72] for people that were trying to make this specific performance improvement to have the metric treat
[1421.72 → 1427.38] that correctly so a lot of the changes that we make or the shifts over time are these tiny
[1427.38 → 1431.82] and subtle things that impact a small percentage of traffic, but they really matter for developers
[1431.82 → 1437.42] that makes sense and so like has there kind of been a case that your team has come across where
[1437.42 → 1443.80] you know everyone looks like the numbers look great on paper right like all these metrics look
[1443.80 → 1449.20] great, but the app still performs poorly like is that an is that a use case like that you have
[1449.20 → 1455.76] come across yet I think not entirely it's you know at some point you can just have a
[1455.76 → 1461.10] an app that's not great right it has great like overall numbers for performance and user experience
[1461.10 → 1468.32] but it's got misleading content it's spammy uh these types of problems still happen uh the reason why
[1468.32 → 1473.06] we have three metrics in that one is because like they kind of balance each other out right like if you
[1473.06 → 1477.66] try to gain largest content paint by popping random stuff in all over the place then you'll have
[1477.66 → 1485.26] bad cumulative layout shift if you try to game it by um freezing the UI then you'll have bad fit or
[1485.26 → 1492.18] bad imp rick any thoughts there yeah I was going to say it would seem like a bug if the app feels slow
[1492.18 → 1496.52] but the metrics are all saying that it's fast and that's really one of the guiding principles of core
[1496.52 → 1504.48] web vitals is that these metrics are grounded in the user experience and as the metric gets worse
[1504.48 → 1510.08] so does the user experience and the other way around as well so we can think that if the user
[1510.08 → 1515.38] experience is poor then, and it's in conflict with the metric we will try to fix that that is something
[1515.38 → 1521.24] that should not happen yeah yeah no that makes sense could it be gamified like uh rick you
[1521.24 → 1525.66] mentioned those scores are like aggregates some score that you mentioned was like an aggregate like good
[1525.66 → 1532.34] is based on like some percentile of how the web performs as a whole in that so I'm just trying to
[1532.34 → 1538.02] think like could I make a could I get a job at like WordPress and make a terrible WordPress plugin
[1538.02 → 1543.26] that just brings down that score for like a majority of the web and then gamify it that way
[1543.26 → 1549.58] why would you do that to make my side look better because it doesn't use I don't know I'm just
[1549.58 → 1554.52] throwing out an example so the I think the distribution thing is about the experiences on your
[1554.52 → 1560.34] own site it's not like where you stand in relation to other websites, and it's really like uh
[1560.34 → 1565.24] everybody's in it just for themselves and evaluated on their own performance got it so don't slow down
[1565.24 → 1569.80] anybody else to make your own site look faster yeah that's so funny yeah rick is like why listen
[1569.80 → 1575.34] like we're developers okay we're here to we're here to push your limits and boundaries okay like you
[1575.34 → 1582.02] guys are the platform right it can be um but speaking of incentives and pushing things forward
[1582.02 → 1588.32] you know so Core Web Vitals do impact SEO right and for me like this is like when that happened I was
[1588.32 → 1594.16] like I just like you know that like GIF or where it's like you have the kid that's like yes
[1594.16 → 1601.08] you know like that was me because I was like finally we have an actual business incentive that's going to
[1601.08 → 1606.96] hopefully drive performance work at all these various companies because you know for a very long
[1606.96 → 1612.06] time they're just it was like this uphill battle trying to sell it to product and business like
[1612.06 → 1616.48] you know we need to work on performance is important right like no one is thinking about
[1616.48 → 1621.22] that it's like this um afterthought you know where like you know the apps shipped and like it's been
[1621.22 → 1626.16] like months and then there's this panic crunch to try to improve performance because there's some user
[1626.16 → 1631.14] feedback coming you know it's like you know we need to bake in kind of performance monitoring into our
[1631.14 → 1637.00] daily process not like you know brush your teeth daily not like once a year right you know
[1637.00 → 1644.80] what I mean and so like can we talk about this like tie to SEO and like I'm like whose idea was that
[1644.80 → 1651.56] like smart yeah so there is a wall between chrome and search and so there's not a lot that
[1651.56 → 1656.46] we can say about the ranking incentive I can quote for you verbatim what it says in the search
[1656.46 → 1661.18] docs gosh darn it you know rick I was hoping you would leak you almost got leaks of trade secrets
[1661.18 → 1666.48] insider information you know there is a doc that I can point you to it's the title of his
[1666.48 → 1671.12] understanding Core Web Vitals and google search results and there's a sentence in there that I think
[1671.12 → 1676.04] is like really clear it says we highly recommend site owners achieve good Core Web Vitals for success
[1676.04 → 1680.40] with search and to ensure a great user experience generally so I want to focus on the last part of
[1680.40 → 1685.28] that sentence which is what I can talk about like ensuring a great user experience generally and
[1685.28 → 1690.80] something what you said Abel was interesting around uh the business value of performance and so my hope
[1690.80 → 1698.12] is that developers and business leads do see the intrinsic benefit of optimizing web performance let's take
[1698.12 → 1703.28] search off the table for a second and just put that over there when you make a website faster it
[1703.28 → 1708.70] basically creates a more frictionless experience for users to use your website if you want them to
[1708.70 → 1713.42] convert in some way to buy your products or to sign up for your newsletter or listen to your podcast
[1713.42 → 1718.78] then having a more frictionless experience is one way to ensure that you can improve your conversion rate
[1718.78 → 1723.70] and so that's that's what we're trying to convey to people with some of the case studies that we've
[1723.70 → 1728.10] shared like other people have succeeded at it other people have had their business metrics that
[1728.10 → 1733.16] they care about maybe that's ad revenue or other sort of things that I mentioned and so web performance
[1733.16 → 1737.40] is just one way of uh I've called it like greasing the funnel if you have a marketing funnel and you
[1737.40 → 1742.12] want to bring people all the way to the end performance is that thing that will make somebody decide that
[1742.12 → 1746.64] they don't want to use your app anymore so anything that you could do to ensure that they have a good
[1746.64 → 1751.90] smooth experience is just good for you, you make more money let's say it's good for your users
[1751.90 → 1755.98] they're happier when they're using your app they're not rage clicking around or anything like that
[1755.98 → 1759.74] and it's good for the web ecosystem as a whole because it's seen as a more healthy
[1759.74 → 1765.60] place for people to do their business yeah I mean it makes perfect sense uh you know there's been
[1765.60 → 1771.16] numerous studies that show this you know very like have very quantifiable data that you know you
[1771.16 → 1777.46] like you improve your performance by this percentage, and you know your revenue suddenly goes up by this
[1777.46 → 1781.76] other percentage right especially for e-commerce websites um you know checkout flows all
[1781.76 → 1786.82] kinds of things right you know um users are dropping off less there's so many actual other incentives
[1786.82 → 1793.52] besides SEO, but it feels like SEO is the thing that really stuck with a lot of businesses and I think
[1793.52 → 1799.56] for me what's exciting is you know you we've had this like upward trend since I think Core Web Vitals
[1799.56 → 1805.92] right like both being able to actually measure like and have some actual direction on like okay i have to
[1805.92 → 1810.52] work on this performance thing like where do I even start right so like having these three uh horse
[1810.52 → 1816.12] heads or whatever that you know these i the alphabet soup you know having that is like helpful and
[1816.12 → 1820.46] than also just being able to measure that over time and then have business support I mean you know so
[1820.46 → 1827.18] it's been I feel like the web has been getting faster despite you know JavaScript apps getting bigger
[1827.18 → 1833.04] you know like so I think that one thing that's been really cool that we didn't really think about
[1833.04 → 1838.28] right is like chrome and search recommend these user experience metrics for good user experience
[1838.28 → 1842.86] right like there's kind of that alignment and then um we have this thing called the core vitals tech
[1842.86 → 1848.92] report that that kind of shows how individual platforms and things are performing on those and
[1848.92 → 1853.78] those platforms sometimes they say hey we've been working really hard on this we have great baseline
[1853.78 → 1858.00] user experience just like google recommends and i I think that's really exciting right that it's its
[1858.00 → 1863.80] it makes it easier to make good choices as a developer as well yeah absolutely, and so I guess
[1863.80 → 1869.66] do Core Web Vitals make sense for every type of website um specifically you know I think
[1869.66 → 1877.64] about games versus you know spas uh versus maps, and you know static sites like the whole kind of
[1877.64 → 1883.56] gamut of web architectures right you know do Core Web Vitals make sense all the time in all of these
[1883.56 → 1889.22] use cases uh so core vitals are designed to provide kind of like a baseline, and they are mostly focused
[1889.22 → 1893.74] on web content so if you're reading the news or an informational article they're really great for
[1893.74 → 1899.60] that and then where it's difficult to just give any sort of metric generically about the user experience
[1899.60 → 1906.00] is any sort of long-lived app right like we're in a web app that's recording a podcast we probably
[1906.00 → 1910.88] care about the frame rate, and you know that's not part of core vitals right so this app should be
[1910.88 → 1917.30] monitoring additional metrics but one thing that I see like I get to look at a lot of like the broad
[1917.30 → 1922.94] data and a lot of people that say i I have a long-lived app the load time doesn't matter because
[1922.94 → 1928.70] people spend a lot of time in it when I actually look at how much time is spent in apps it's a lot
[1928.70 → 1933.56] less than you would guess so i I think if you do have an application, and you do think that core
[1933.56 → 1938.18] vitals aren't relevant like really actually monitor right like how much time do people spend in it
[1938.18 → 1945.46] how many times do people do page loads and really do like a good overview of that and then also think
[1945.46 → 1952.52] about what we do on our team we have core vitals and web performance APIs, and it can be a
[1952.52 → 1957.52] little bit difficult to measure core vitals in JavaScript because we have these lower level APIs
[1957.52 → 1962.80] we give you information about every single interaction not just the one that was the slowest
[1962.80 → 1968.54] we give you information about lots of different paints and the reason why we do that is what if your
[1968.54 → 1973.30] app involved is a chat app and invite involves people typing for hours you probably are going to want to
[1973.30 → 1979.78] have like a lot of metrics about how that went uh differentiate key presses from uh taps and clicks
[1979.78 → 1986.10] and so if core vitals aren't appropriate ideally you know you have a pretty hardcore application and
[1986.10 → 1991.20] you're doing your own performance metrics, but you can still use these APIs that underlie core vitals
[1991.20 → 2015.58] what's up friends I'm here with Conrad offerer from powersync is the sync layer that enables an
[2015.58 → 2022.32] offline first architecture to make your application local first by default real time and reactive so
[2022.32 → 2029.16] comrade the DX the developer experience of adding something new to the stack is always important to
[2029.16 → 2034.88] consider how does power sync integrate into the application one of our goals with parsing is we
[2034.88 → 2038.54] don't want to get in the developer's way we want to provide a composable layer that they can add to
[2038.54 → 2044.00] their stack without being invasive or over complicating their code we try to make it kind of as easy as
[2044.00 → 2048.76] possible to kind of integrate parsing into your stack so the way it works is you hook up what's
[2048.76 → 2053.56] called the parsing service to logical replication in your Postgres database you embed the parsing
[2053.56 → 2058.20] SDK in your app project, and then you wire up the SDK which involves wiring it up to your JWT
[2058.20 → 2063.18] authentication and to your backend API for uploading rights so at the simplest level those are kind of
[2063.18 → 2066.96] the key things that you're going to be doing, and then you essentially get bidirectional data
[2066.96 → 2071.96] syncing and a local first architecture so at this point you have bidirectional syncing of your data you
[2071.96 → 2078.52] have an offline first local first application where do you go from there to do syncing rules
[2078.52 → 2084.96] customization etc from there you can customize things like the sync rules for example to specify which
[2084.96 → 2089.86] data gets synced to which user you can customize things like you know if you need any custom conflict
[2089.86 → 2095.10] resolution you can customize that yeah man power sync sounds pretty cool so you can build local first web
[2095.10 → 2102.36] apps give users instant reactive UX with an in-browser database that keeps itself in sync with any
[2102.36 → 2108.46] backend Postgres no need to wait for network requests complicated caching logic or to maintain
[2108.46 → 2116.34] in-memory state setup is easy removal to try on a generous free plan today at powersync.com
[2116.34 → 2122.34] slash changelog again powersync.com slash changelog
[2122.34 → 2132.42] so let's dig into these metrics so INP being the first one we'd love to kind of focus a little more
[2132.42 → 2138.82] on since it's newer so what is inp standing for interaction to next paint that's what's going to be
[2139.44 → 2145.70] an officially a new core web vital in the upcoming few weeks so we're recording this February 28th
[2145.70 → 2153.34] uh 2024 and so what is INP I'll take it so INP you mentioned interaction to next paint
[2153.34 → 2158.84] it is the responsiveness metric of the trio and the best way to think about it is how quickly the
[2158.84 → 2164.84] page is able to handle user input it looks at all the interactions that happen throughout the
[2164.84 → 2170.42] page lifetime, and it takes approximately the slowest one so if a user has a terrible slow
[2170.42 → 2175.04] interaction experience you can generally think of it as uh that amount of time
[2175.04 → 2180.86] and the thresholds that you can use to think about whether this is good or slow is 200 milliseconds
[2180.86 → 2185.84] and below is considered good anything over 500 milliseconds is a really poor experience
[2185.84 → 2190.08] things in between we categorize as needs improvement there's nothing to say that you
[2190.08 → 2194.74] couldn't have a bucket even more into the tail of if it's slower than a second then it's really
[2194.74 → 2199.90] terrible I find it sometimes helpful to break it up that way but um I say it's approximately
[2199.90 → 2205.78] the slowest because uh it is it does have some built-in tolerances to applications with lots of
[2205.78 → 2210.80] interactions like those chat apps where you're typing and typing so the slowest one in every 50
[2210.80 → 2216.10] interactions is effectively ignored its kind of like a grace interaction maybe that was a fluke it
[2216.10 → 2220.88] doesn't usually happen like that maybe the user forgot about that slow interaction uh in the grand
[2220.88 → 2227.10] scheme of having hundreds of them so um we're not going to get hung up on the absolute slowest there is
[2227.10 → 2232.82] going to be some built-in tolerance so, so like what's a good score and specifically how are
[2232.82 → 2238.62] interactions like I'm uploading a file and that might take I'm uploading a file on Dropbox that
[2238.62 → 2243.92] might take 10 minutes for example right like how do interactions like that you know get weighted
[2243.92 → 2250.44] against like you know i users trying to click a button and like nothing's happening you know yeah so a
[2250.44 → 2255.38] good score is 200 milliseconds and then there's a question of like well if an interaction should be 100
[2255.38 → 2262.00] milliseconds wise 200 a good score there are a couple of reasons for that uh low-end mobile and very low-end
[2262.00 → 2268.42] netbook type things still like the machine might not be capable of a response within 100 milliseconds
[2268.42 → 2274.40] and then the second reason is that we have like multiple interactions right so if you have a lot
[2274.40 → 2281.30] of user interactions we're taking not the worst but almost the worst and so if you're like at 200 for
[2281.30 → 2287.82] for almost the worst like most of those interactions are under 100 uh so that's the reason that 200 is a
[2287.82 → 2293.62] good score and then what about very long interactions that take a really long time uh I think this is where
[2293.62 → 2299.96] we get into like what is interaction to next paint really measuring, and it's right there in the name
[2299.96 → 2308.38] right I click I tap or I press a key and the next paint the next animation frame shows up so I get some
[2308.38 → 2314.48] immediate response and if you think about this um like you press a button and then the button appears
[2314.48 → 2319.38] depressed that's the like the key down response, and then you lift it up, and it like it shows that
[2319.38 → 2325.28] activated state we've actually you know if is you have a really poor imp we've actually seen buttons
[2325.28 → 2331.66] where like you click it and then four seconds later the activated state shows right and that's
[2331.66 → 2337.62] what the UDR actually says people want in 100 milliseconds they don't expect any action that
[2337.62 → 2341.38] they've ever attempted to be completed in 100 milliseconds they expect some feedback like the
[2341.38 → 2346.72] computer is doing something um they expect that very quickly and so that's what interaction the
[2346.72 → 2353.42] next paint measures so what if you do have something that takes a long time a file upload a request to the
[2353.42 → 2359.54] server you should be showing user feedback and keeping the main thread free for the user to like
[2359.54 → 2365.20] know that the site isn't frozen while it's doing that yeah so it's really independent of what you're
[2365.20 → 2370.78] actually doing yeah right it'd be more like if i click a button and I immediately show a spinner
[2370.78 → 2375.78] like that satisfies this yeah and then whatever action I'm actually trying to do like I could be
[2375.78 → 2379.84] throttling that to wait to see if something else comes in for example and I could throttle that for
[2379.84 → 2385.40] two seconds but I would still be safe with the within that if I indicate to the user that something
[2385.40 → 2391.66] has happened yeah and then a lot of people ask me well what about if I just delay everything and i
[2391.66 → 2395.66] never respond to user interactions and the thing is like let's say you have a actually is two
[2395.66 → 2398.98] seconds of solid JavaScript that you're not throttling right like the user is going to click
[2398.98 → 2403.04] again and then the second interaction is going to get frozen waiting for the first one so you're still
[2403.04 → 2408.24] going to get punished on imp so don't do that actually break up your task so you can show a real
[2408.24 → 2412.64] spinner and have it animate yeah and so can you walk us through like why this is better than
[2412.64 → 2420.04] FID uh which is first input delay um and why this is it seems like this is replacing FID is that a
[2420.04 → 2426.08] correct assumption or understanding yeah okay so interaction to next paint why is it replacing vid
[2426.08 → 2432.82] when we started this whole core vitals program we were number one more focused on mobile it was going
[2432.82 → 2437.86] to be mobile only, and we extended to desktop because it was so successful and also interactivity on the
[2437.86 → 2445.22] web was a lot worse so we just wanted to have like a baseline only about 80 percent of sites could meet
[2445.22 → 2453.24] that baseline at launch where first input delay is only the first interaction and the main thread is
[2453.24 → 2457.76] free enough that your interaction starts to get handled by the browser that's all it measures
[2457.76 → 2463.94] and it wants that to happen in a reasonable time frame and a couple of really great things happened
[2463.94 → 2471.52] after the launch of core vitals we extended to desktop but also uh developers uh at scale really
[2471.52 → 2478.44] fixed a lot of problems with first input delay being so slow I think frameworks really uh changed the way
[2478.44 → 2484.72] that they do hydration to allow it to be interrupted by a user input and this uh solved a huge percentage
[2484.72 → 2491.04] of the FID problems also in chrome we identified that like you remember how you're supposed to use a
[2491.04 → 2496.10] meta viewport tag and that'll disable like the tap to zoom where you double tap, and it zooms in the
[2496.10 → 2502.72] page we identified some situations where developers weren't doing that, but we could stop doing the tap
[2502.72 → 2511.18] to zoom anyway so we fixed that problem and with those two problems being fixed most of the interactivity
[2511.18 → 2518.08] at load the delays before the input were resolved, and we actually didn't expect it to go that quickly or to be
[2518.08 → 2523.90] that few problems uh that needed to get solved uh, but we felt like there's still a big problem with
[2523.90 → 2529.10] interactivity on the web if you do look at like just the raw values of interaction in next paint
[2529.10 → 2537.18] one in 100 pages both on mobile and on desktop have a freeze for over a full second when you try to click
[2537.18 → 2541.86] and just see the next frame so we still think there's a lot of work to do which is why we decided that we
[2541.86 → 2548.50] should launch this next metric and let developers know about these problems I have an another question
[2548.50 → 2553.30] I'm just trying to clarify things for myself uh with this but let's say that my site has an awesome
[2553.30 → 2560.30] uh snowing animation that continuously happens does imp get confused by that or does that somehow
[2560.30 → 2566.36] like because it's continuously updating yeah so that's a fascinating question that that has
[2566.36 → 2571.14] like kind of like a deep technical background in chrome as the chrome performance team and especially
[2571.14 → 2575.72] our graphics team is looking at like how could chrome be better over the last years a lot of what
[2575.72 → 2581.64] we've done is we've said like hey you should use CSS animations, or you should use um compositive
[2581.64 → 2587.50] animation so that basically like the compositor is able to make that snow happen no matter what's
[2587.50 → 2592.28] happening on the main thread the wrong way to do it is to have like some JavaScript code that
[2592.28 → 2599.92] slowly moves this the the the snow around and updates the Dom if you do it the wrong way when there is a
[2599.92 → 2605.06] user input, and it takes 100 milliseconds to handle that extra 100 milliseconds is going to get added
[2605.06 → 2611.42] on to your animation right yeah and then also if your animation takes like five milliseconds it's
[2611.42 → 2618.28] going to extend the response to the interaction to like 105 milliseconds and so if you did it the wrong
[2618.28 → 2623.08] way we're going to count it but what we do if you do it the right way and this is why it took a long
[2623.08 → 2629.10] time to develop the metric you have a user interaction and we in chrome like look at what
[2629.10 → 2633.74] changed like what the was there damage to the Dom is what we say like did your interaction
[2633.74 → 2639.94] results in a user a need for a paint, and then we track like which paint that was, and we hook the
[2639.94 → 2646.04] interaction up to the right paint so you can't speed up imp by doing a compositive animation but if you do
[2646.04 → 2651.22] your animations well, and you use the compositor then you're not going to have any penalty on imp okay
[2651.22 → 2657.12] got it I'm just I'm just losing nick in my head like pretty, pretty hard right now but that was an
[2657.12 → 2663.42] awesome question and so um like I think some of the other benefits would probably be that imp isn't
[2663.42 → 2670.08] limited to kind of like the first load right and fit was like because like you know you're not able
[2670.08 → 2675.78] to really measure much after the first load with fit right like it's but like people who are like you
[2675.78 → 2681.20] know in longer sessions there are all kinds of interactions that kind of unfold over time and I feel
[2681.20 → 2686.82] like INS able to kind of capture some of those in a more meaningful way yeah and as much as I said
[2686.82 → 2691.68] before like your sessions aren't as long as you think they are decently long on average
[2691.68 → 2696.94] and you stop breaking hearts stop stop stop telling truths you know everyone has this fantasy of you
[2696.94 → 2702.18] know everyone's that my users are spending hours on my app hours and hours you know it's the first
[2702.18 → 2707.90] thing they do every day they spend about 90 of their time after the page is loaded so they 10 of their
[2707.90 → 2712.86] time is spent loading the page and then 90 of the time is spent after the page is loaded so they
[2712.86 → 2717.52] do spend time, and it's important to capture what's happening while they're using the page right
[2717.52 → 2723.74] right that makes sense so rick what are some common INP pitfalls well really anything that slows down
[2723.74 → 2730.04] your interaction either the event handler itself so when a user clicks, and you have a click handler how
[2730.04 → 2734.90] long does that take to run and also even if your click handler was instantaneous it could still be
[2734.90 → 2739.16] blocked in this like input delay phase because your main thread was just busy doing other stuff
[2739.16 → 2744.08] so i kind of look at it in these two different types of problems where was your interaction slow
[2744.08 → 2749.38] or did it just happen to coincide with some other things going on like I recently equated it to like
[2749.38 → 2754.96] a road having um potholes on it like it's the quality of the road that could also slow down the
[2754.96 → 2760.70] experience or make it a worse experience but also like if your car is just really beat up that could slow
[2760.70 → 2765.14] down your experience and make it worse too so some technically some things that could affect that are
[2765.14 → 2772.76] really huge does if you have like a query selector in your JavaScript, and it needs to either look
[2772.76 → 2777.48] through the Dom or affect lots of things in the Dom it's a function of the number of elements in it and
[2777.48 → 2782.40] so if you have a huge web page the one that I look at most is like the HTML spec itself to really
[2782.40 → 2787.26] test this problem out because it's gigantic like if you try to test that page out you'll hit every sort
[2787.26 → 2791.60] performance bottleneck you can imagine another thing is really just like having too much
[2791.60 → 2796.22] JavaScript it's okay if you need JavaScript to run your app, but it's good to think about it in terms
[2796.22 → 2801.74] of like what needs to happen immediately what's the work that I could defer to later in terms of
[2801.74 → 2808.18] what is needed to render the initial view of the web page things like setting up your analytics maybe
[2808.18 → 2813.48] just have a really lightweight thing to maybe batch up some of the interactions that you need to log back
[2813.48 → 2820.28] or anything that's not going to affect the user interface itself could probably happen later and
[2820.28 → 2826.22] that's also where we come to some of the optimization techniques which are literally setting the priority
[2826.22 → 2829.80] of the work that you want to do on the main thread and that's one way that you could tell the browser
[2829.80 → 2835.30] do this before that this is really critical because it affects the user interface we need it to happen as
[2835.30 → 2839.18] soon as possible versus this is just something that could happen in the background whenever you get to
[2839.18 → 2846.60] it is okay so it's not that I want to uh downplay JavaScript on the web as like the bane of our
[2846.60 → 2851.40] existence in web performance it's really important to having really rich experiences, but it's just about
[2851.40 → 2856.70] using it responsibly and not overloading your page with too much JavaScript because even just to
[2856.70 → 2863.08] download and parse and execute it has its own performance costs and implications and the compilation
[2863.08 → 2866.88] time itself is something that could trip you up even before you get to the part where you have to
[2866.88 → 2872.24] execute it so it's really just being conscientious and tracing your page like looking at what is
[2872.24 → 2876.46] actually happening on the main thread to understand it without it, you're really just guessing and going
[2876.46 → 2882.50] by feel like if I click something is it fast I don't know it was fast to me everybody kind of has their
[2882.50 → 2887.56] own interpretation of it so what's nice is to be able to use objective measures and look at things
[2887.56 → 2893.40] objectively using tracing from like the performance panel of Chrome dev tools to get a perfect idea
[2893.40 → 2898.66] of what is happening at the lower level and is that what you mean by like prioritizing things is like
[2898.66 → 2904.46] there's not like some built-in thing where I can say this is not important go it can run whenever
[2904.46 → 2908.40] you're not busy, but it's more about like looking at what is actually important and making sure that
[2908.40 → 2914.52] that just gets done or gets prioritized like in your own unique way compared to the other thing
[2914.52 → 2919.32] that's not important yeah there are things that you can do as a developer to say this is the point in my
[2919.32 → 2923.68] application code where everything that happens after this could probably wait for till later it
[2923.68 → 2928.32] doesn't have to happen now I would rather have like a paint happen to the screen to show to the user
[2928.32 → 2933.22] and so you could add a yield point in your code like something as easy as a set timeout with zero
[2933.22 → 2937.76] milliseconds is one way of implicitly yielding back to the main thread but that you could do more
[2937.76 → 2943.18] declarative things to say the work that I'm about to do is super high critical priority using something
[2943.18 → 2948.46] like the post task API from the scheduler API and then for whatever you pass in there as arguments
[2948.46 → 2952.72] could be uh setting those different priority levels to make sure that the work is clear to
[2952.72 → 2957.26] the browser uh what relative priority should have with other things even the things that you don't
[2957.94 → 2964.32] explicitly say are um low priority it will fit in with the other work that happens uh like a
[2964.32 → 2970.10] timeout for example a timer fires, and it has to do work I have never looked at the scheduler API
[2970.10 → 2975.80] so this is fascinating yeah it's a pretty cool low level API and I was actually going to say it's a
[2975.80 → 2983.10] fantastic explanation rick is there like a work box equivalent to that uh you know where there are
[2983.10 → 2988.76] some nice like higher level abstractions that developers can use to really you know I would
[2988.76 → 2995.72] say more declaratively you know add this into existing uh web apps frameworks that's libraries
[2995.72 → 3001.34] you know i because I think for me like this is like a missing link for us specifically around
[3001.34 → 3007.52] like our thinking and thought process around how we develop apps right like scheduling is not really
[3007.52 → 3014.48] top of mind, and it's not like a capability or skills gap it's just like it's just not like it's not part
[3014.48 → 3018.82] of the culture not part of the discourse right so we're talking about scheduling here you know how do
[3018.82 → 3024.68] we get this to be more mainstream and more adopted and for me that's through something you download
[3024.68 → 3032.08] through NPM usually you know what I mean like it's the gateway drug um so uh so i I don't know um
[3032.08 → 3036.38] thoughts on this curious well I have good news for you there is something that you could download
[3036.38 → 3042.92] tell me um, so there 's's a polyfill for the scheduler API uh some of the newer features like
[3042.92 → 3047.76] the yield method are available in the polyfill it'll fall back to something like uh set time out if
[3047.76 → 3052.74] needed but yeah you can install this library or the polyfill itself and then get the benefit of
[3052.74 → 3059.40] these APIs by kind of using this wrapper around it so uh it's available in the Google Chrome labs
[3059.40 → 3066.24] organization on GitHub under the repo scheduler polyfill and like when it when the full API would
[3066.24 → 3072.36] be is going to be available across kind of is there like a timeline for like when this is going to be
[3072.36 → 3081.10] available on most browsers or I could speak for chrome um yeah I know that uh the yield API is available
[3081.10 → 3086.86] in origin trial, and we're hoping that it will be available later in 2024 uh in chrome stable I would
[3086.86 → 3092.76] also try to think about whether your framework might be considering itself like helping you schedule and
[3092.76 → 3097.34] prioritize things like react suspense boundaries that they're designed to help you say
[3097.34 → 3102.86] like what's important what needs to show up right away what can be async so i would definitely
[3102.86 → 3106.96] also look at what framework you're using in the documentation around that for scheduling and
[3106.96 → 3112.86] priorities that make sense yeah I think the React team had a whole yeah they're building a scheduling
[3112.86 → 3120.16] API into react which I thought was really ambitious considering I'm like that should happen in a browser
[3120.16 → 3126.36] I think um it's much better for that to happen in a browser because then that's not compute that you're
[3126.36 → 3130.50] fighting like you're not fighting for resources on the main thread you know what I mean so
[3130.50 → 3136.24] and he's nodding for those who can't see any space yeah I do think the teams are talking right
[3136.24 → 3140.46] like the people that work on chrome scheduling definitely talk to the React team and I think
[3140.46 → 3145.84] that the TLDR there is its very complicated yeah yeah I can only imagine I mean and kudos to them for
[3145.84 → 3151.18] even trying to be honest like that's a very ambitious thing to try to do in JavaScript like
[3151.18 → 3156.38] at the JavaScript layer but um yeah but glad to see that uh spec is kind of like moving along
[3156.38 → 3162.00] um in on the standards track and we'll like to put a link to the origin trial for folks or if you're
[3162.00 → 3167.32] interested in um enabling that for your domain so that'll be in the show notes so I think I don't
[3167.32 → 3173.22] know anything else we want to dig into about imp nick any other burning imp related questions I mean
[3173.22 → 3179.10] I guess i you kind of touched on this a little bit i I have one tiny one um which is there like
[3179.10 → 3185.60] can be many imps on a given page and like let's say you have one terrible one like how does that
[3185.60 → 3191.96] affect like your total overall like aggregate score yeah so in general there's almost always
[3191.96 → 3196.40] fewer than 10 interactions on any given page load, but some pages do have a lot of interactions
[3196.40 → 3202.68] and for those page loads we basically like as Rick said earlier we kind of like throw out the top of
[3202.68 → 3207.26] like we take like take the maximum up to 50 and once you get to 50 we throw out the top then once
[3207.26 → 3211.36] you get to 50 again we throw out the last so it's essentially like the 98th percentile
[3211.36 → 3217.14] and the reason we do that is like if is people are interacting with your page 50 100 200
[3217.14 → 3226.12] times they probably uh are forgiving some level of uh outliers, and so we do uh drop the outliers
[3226.12 → 3232.78] oh wow that's so cool that's yeah it's like a cool statistics problem to be solving yeah so I think we
[3232.78 → 3238.70] can move on to like we'll cover these really quickly just for the interest of time but um LCP and CLS
[3238.70 → 3245.46] so LCP is largest content paint you know so you know what is that and what is content here
[3245.46 → 3250.42] like what counts as content on the page as well I think this is more of the traditional web
[3250.42 → 3255.78] performance metric that people would think about in terms of like a loading performance metric so
[3255.78 → 3260.40] largest content paint there are three parts of that we can look at like the fact that it's a
[3260.40 → 3265.66] paint metric means that it's user-centric something actually happened on the screen that a user will
[3265.66 → 3270.22] notice the fact that it's a content paint to distinguish from all the other paints means
[3270.22 → 3275.80] it's not just like the background colour changed uh to a user that's like nice feedback to know that
[3275.80 → 3280.08] the page is loading, but it's not why I came to this website I didn't come here to see what colour
[3280.08 → 3285.02] background colour using, but it's like I came here to read something or I came to you know if I'm reading
[3285.02 → 3290.18] a news article it's helpful to see that the hero image has loaded and so it's the largest piece of
[3290.18 → 3295.94] content that we're using as the measure of the page has loaded to the state where a user might feel
[3295.94 → 3301.90] like it's ready to use this could be your h1 element sometimes it might be a logo or a paragraph
[3301.90 → 3307.76] of text or that hero image so we're trying to use this as a way of saying the user feels like they can
[3307.76 → 3312.66] use the page now what they came here to do can be accomplished from this point forward, and it could
[3312.66 → 3318.74] change so if you look at a filmstrip of how the web page is composed over time sometimes you'll get
[3318.74 → 3323.78] a h1 showing up pretty much immediately but that image takes a couple of seconds to load so initially
[3323.78 → 3330.42] you might get a LCP candidate of that h1 and then that is then uh subsumed by the image once it finally
[3330.42 → 3336.20] loads so it's really like the final LCP candidate that matters to us there are some like corner cases
[3336.20 → 3342.16] where if a user interacts with the page while that image is loading that's a signal to chrome or any of
[3342.16 → 3348.10] the implementations of LCP that the user feels like the page was ready enough to use so we're not going
[3348.10 → 3353.78] to look at any other LCP candidates after that point so what really this is why it really matters
[3353.78 → 3360.66] to look at field data or metrics from real users because then you can see things like the h1 is
[3360.66 → 3365.68] your LCP element some percentage of the time versus the image you can find fascinating user
[3365.68 → 3370.46] behaviour patterns like if somebody arrives at your page from a deep link you might want to prioritize
[3370.46 → 3376.68] the images further down the page and one of the common patterns that we see is lazy loading of images
[3376.68 → 3380.44] images and as a rule of thumb we say well you'd want to lazy load everything below the fold well
[3380.44 → 3384.56] in these corner sometimes cases things that are below the fold are the images that need to load
[3384.56 → 3390.46] immediately and so having that analytics data to know where the common causes of LCP are or like
[3390.46 → 3395.46] the elements themselves is really helpful so LCP is one of those metrics that I think a lot of people
[3395.46 → 3399.84] will immediately identify with as like oh this is a loading performance metric this is what web
[3399.84 → 3404.66] performance is all about, but it's important just to remember this is one of three Core Web Vitals
[3404.66 → 3408.78] metrics, and it's really the combination of all of them that we use to say that this was a good
[3408.78 → 3415.24] experience on the web page so uh just was curious like why something under the fold would need to be
[3415.24 → 3420.30] like when would, could you just double-click into that I don't think it was clear to me like why we
[3420.30 → 3425.04] would need to prioritize an image that's like below the fold right so it's like I think for me like
[3425.04 → 3431.72] when CPU kind of hit the scene it was like really forcing developers to think about focus on you know
[3431.72 → 3436.34] above the fold above the fold right like that's when we really started getting obsessed about like
[3436.34 → 3441.24] okay making sure that like we're loading things and prioritizing what our users can see and there's
[3441.24 → 3446.80] all kinds of rich like metadata tags that started landing in the HTML spec and script tags and image
[3446.80 → 3451.70] like all kinds of stuff to kind of prioritize things but like yeah when would you need to
[3451.70 → 3456.64] prioritize something that's like below is it because it's slow, and it takes time like or something
[3456.64 → 3461.30] else yeah I don't want to give your listeners the impression that like you have to care about every
[3461.30 → 3465.82] image on the page, and they all need to load fast free to cover your bases in a way I only bring that
[3465.82 → 3470.86] up as like a corner case for the times when above the fold content might not be your LCP i that's not
[3470.86 → 3476.18] where your LCP is what you're saying okay so if you have a deep link like somebody copies the link to a
[3476.18 → 3481.06] heading that's halfway down the page and then there's a graphic there to describe like it's a piece of
[3481.06 → 3485.84] documentation or something that's a case where unfortunately on the server side you don't know what that
[3485.84 → 3491.02] URL hash is so you can't really prioritize it dynamically, but you might say well that's going
[3491.02 → 3496.04] to be my LCP element 50 of the time most people arrive at this page from some other website that's
[3496.04 → 3503.16] linking back to it in the deep link down there, and so I might lazy load everything but the top three
[3503.16 → 3507.60] images on the page and then that one that's halfway down because that's just what my analytics tells me
[3507.60 → 3512.62] happens to be the most common LCP candidate yeah no, thank you I think that's what you just said the
[3512.62 → 3515.82] second time around because you know I'm pretty sure you said that the first time around it just
[3515.82 → 3521.80] didn't click for me was uh the like it's the entry point you know like it's how it's how we got
[3521.80 → 3526.96] here right like uh what page like if you're deep linking to another part of the page then you need
[3526.96 → 3532.26] to kind of think differently about what loads first and I think that also plays into like your URL strategy
[3532.26 → 3537.82] and all kinds of um you know things around how are you using query parameters to kind of communicate
[3537.82 → 3543.74] things uh or headers like all kinds of you know there are all kinds of ways to pass along that data to your
[3543.74 → 3548.76] server, but it has to be part of your strategy or else you can't really action on it right very cool
[3548.76 → 3555.10] oh man rick you're like making me think about stuff like that are like that's kind of like it's well i
[3555.10 → 3560.04] mean because you know with performance it's like first very humbling work right, but it's like
[3560.04 → 3567.02] there's this um how do you put it like there's like level one two three you know and I feel like a lot
[3567.02 → 3572.70] of people like kind of once they get started like they kind of zoom through one two three but then
[3572.70 → 3578.56] there's four five six eight nine seven you know what I mean and like those are eight nine seven
[3578.56 → 3583.60] is a funny ordering but um you know that's like that's the stuff that I feel like gets that's where
[3583.60 → 3588.44] you hire performance experts because it's actually really hard to do this well for most like
[3588.44 → 3593.26] for complex web apps you know and this is why like performance again it's its a field of study it is a
[3593.26 → 3599.82] it is a vertical within tech it is like I don't yeah something I think we need to kind of make more
[3599.82 → 3606.28] space for formally within organizations right like it's hard to kind of master it all as just you know
[3606.28 → 3614.86] a quote-unquote regular engineer we work really hard to kind of codify best practices right um so
[3614.86 → 3619.02] for example that that rick came up with one of the things that actually happened was
[3619.02 → 3624.06] like a person in our team had a blog, and it was getting deep linked like this deep technical
[3624.06 → 3629.58] content in the bottom of the page and um they noticed that like they had their own kind of
[3629.58 → 3634.44] implementation of web vitals.js that was logging extra stuff, and then they were like oh it's useful
[3634.44 → 3640.18] it's telling me this right and then we added about well Rick's team added to web vitals.js
[3640.18 → 3646.04] uh here's an attribution section and it kind of like encodes that the things that we all found useful
[3646.04 → 3650.70] and helpful as every as we're talking to lots and lots of people that are debugging this stuff like
[3650.70 → 3655.44] what is floating to the top so in this case if you just look at the attribution part of web vitals.js
[3655.44 → 3661.18] you can get like a lot of ideas about what do people actually find helpful yeah no that makes sense well
[3661.18 → 3666.40] thank you both you're you're both schooling us so we appreciate us and hopefully lots of other
[3666.40 → 3673.02] people so we maybe move on to CLS nick what do you want to know about CLS besides it's also easy to
[3673.02 → 3679.84] pronounce compared to LCP and imp and phi I don't know CLS feels like it rolls off the tongue a little
[3679.84 → 3685.94] bit more easily yeah you know well I guess starting with uh what it stands for I assume it's not clear
[3685.94 → 3696.44] screen it's a cumulative layout shift and so uh going backward layout shift is the kind of like
[3696.44 → 3705.26] unit here uh so what it what we're talking about is an unexpected shift in uh content as the page is
[3705.26 → 3711.56] being laid out so we have an API that reports individually every time the content shifts right
[3711.56 → 3716.20] and it reports that kind of as a fraction of the viewport essentially like half your
[3716.20 → 3724.52] screen moved that's a bad shift 0.5 uh whereas like a tiny little pixel shift could be like 0.01
[3724.52 → 3737.52] and cumulative layout shift just summed over the page lifetime but as we talked about before some
[3737.52 → 3743.08] pages have a really long lifetime like we've all had this uh meeting page up for like over an
[3743.08 → 3749.56] hour and um that's not fair to pages that are long live so we uh rejiggered the algorithm, and we thought
[3749.56 → 3755.24] we actually did a ton of UDR like when are these unexpected shifts the worst for people
[3755.24 → 3761.48] and it's like when there's a big burst of them, and it might happen in like a shorter or longer time
[3761.48 → 3764.98] period, but it's usually over like five seconds either I'm trying to scroll through a news article
[3764.98 → 3770.88] and it's like boom there's a big ad or um I'm loading a page, and it's or there's a single page app
[3770.88 → 3776.90] transition, and it's doing this big like funky thing, and so we basically ended up using a windowing
[3776.90 → 3782.70] algorithm that kind of like as shifts are happening uh within a small time frame to frame
[3782.70 → 3788.84] they pile up into this big window and then eventually we cut it off at five seconds so
[3788.84 → 3795.84] and we take the worst like window of like explosion of layout shift, and we report that as the score for
[3795.84 → 3801.04] the page lib and the reason we cut it off is sometimes people have um like animations that are
[3801.04 → 3805.50] counted as shifts because they're like injecting stuff into the DOM in a really weird way
[3805.50 → 3812.94] so is this where would you be for lack of a better word gamifying this metric by using like a what are
[3812.94 → 3818.96] those things called like a skeleton loader where it's kind of like gray boxes yeah so that's really
[3818.96 → 3823.58] interesting right if your gray boxes are fully aligned to the content the user sees this like
[3823.58 → 3829.78] pop gray boxes content falls into it and when you go and talk to people that have liked you know
[3829.78 → 3835.40] pioneered gray boxes they're like user experience research the users really benefit from these
[3835.40 → 3841.20] boxes like it actually is a user experience benefit um and so it's fascinating sometimes people
[3841.20 → 3845.72] ask me like isn't somebody gaming this by like straight up making their page load faster
[3845.72 → 3852.46] sometimes and I'm like wow i I do think there's a user experience benefit to that type of skeleton
[3852.46 → 3858.88] as opposed to having the content shift in like yeah well I mean instead of like an app shell that's
[3858.88 → 3864.84] like a component shell right and ideally you you you know hopefully know how much space you need for
[3864.84 → 3870.58] that component, and so i I get it and I think the reason why like when skeletons first became
[3870.58 → 3876.74] popular I don't know like seven is years ago like the psychology that was cited behind it was that people
[3876.74 → 3882.66] are more comfortable when they when they know what the shape of the page is going to be you know
[3882.66 → 3888.56] what I mean so they're just like oh don't scare me with like a blank page with a spinner and then
[3888.56 → 3892.88] completely change everything on me no if you're going to show me a loading state show me what I'm gonna
[3892.88 → 3899.30] show me what i can expect right and they're just uh much more like they're less turned by
[3899.30 → 3906.06] like content changes if you give them boxes first you know I'm sorry I don't know why I find this
[3906.06 → 3911.80] hilarious yeah and if you think about you know seven is years ago what we're actually seeing is
[3911.80 → 3915.80] mobile phones showing up in places of the worlds that people didn't have internet before right
[3915.80 → 3921.08] website properties that are international trying to give these people a good experience with a lot
[3921.08 → 3928.06] lower like connection speed right and so those boxes really do help that's where that UDR is based
[3928.06 → 3937.50] right um yeah i just um no respect no disrespect sorry no disrespect not a Freudian slip not no disrespect
[3937.50 → 3944.36] to skeletons um skeletons are great and I feel like Slack was like one of the was it slack Figma um
[3944.36 → 3948.88] envision app I don't know there was like one of those companies like was one of the first that i
[3948.88 → 3954.26] think really kind of started you know doing conference talks on it and like pioneering it um
[3954.26 → 3960.38] you know yeah I think uh they're great I mean you know react built the whole uh API around it right
[3960.38 → 3967.64] suspense so angular's doing the same now so uh you know deferral views and so you know it's exciting
[3967.64 → 3973.44] exciting stuff, so happy users is what we want okay so we have like we could probably be talking for
[3973.44 → 3979.50] another three hours you all um, but we have limited time so we're gonna kind of go into crunch mode here
[3979.50 → 3985.54] and try to land this plane gracefully so rick I'm I'm really curious to kind of if you know we
[3985.54 → 3990.06] can give folks some actionable items so we've talked a little bit about tooling measurement in
[3990.06 → 3995.66] the field versus uh you know quote-unquote lab data right from tools like lighthouse page speed test
[3995.66 → 4001.96] etc so how do you now kind of instead of just like doing this one-off measurement like how do you
[4001.96 → 4009.02] build this into your daily workflow right as a dev team where you are like tracking these Core Web Vitals
[4009.02 → 4015.16] like in your CI builds, and you've got maybe dashboards, or you've got reports going to your VPS like i I don't
[4015.16 → 4022.00] know right, but the whole point is like brush your teeth every day not like when you rsvp calls the
[4022.00 → 4029.58] panic button because some you know bad user feedback came right so how do we how do we get this
[4029.58 → 4035.54] implemented into our workflows as engineers I love that analogy I've also heard it called like eating
[4035.54 → 4041.06] your vegetables yeah having good web performance hygiene yeah so I mean if I could just give one piece
[4041.06 → 4047.94] of advice it would be go check out the documentation on web.dev we have every sort of guide and
[4047.94 → 4052.62] resource you might want to look up about what are the Core Web Vitals how do I improve a specific metric
[4052.62 → 4057.54] what tools should I use so if there's just one entry point make it that the rest of your question could
[4057.54 → 4062.94] be kind of complicated know that we're wrapping up so I'll briefly summarize to say you need to know if
[4062.94 → 4067.48] your website has a performance problem first and foremost before you dive in and start optimizing
[4067.48 → 4073.28] everything the easiest way to do that is using the chrome user experience report I know that
[4073.28 → 4076.98] sounds biased like hey the easiest thing is to use something from chrome but I really do think that
[4076.98 → 4083.50] it's extremely it lowers the barrier to entry to getting real user data it's free first and foremost
[4083.50 → 4089.66] it's really fast, and it's available for over 10 million websites all you have to do is go to
[4089.66 → 4096.68] page speed insights pagespeed.web.dev type in your URL, and we'll tell you how fast it is at the page
[4096.68 → 4102.28] level if it's available if not the origin level which is like the whole website, and so we can tell
[4102.28 → 4108.14] you how your three metrics are doing how the overall assessment is and that is really a good way for you
[4108.14 → 4112.58] to know as a site owner whether you have work cut out for you or not you could also use a tool like
[4112.58 → 4117.42] search console so they have a Core Web Vitals report, and it's also broken down by the metrics and
[4117.42 → 4121.88] I'm pretty sure search console will also notify you if you have a problem in any one of these metrics
[4121.88 → 4126.16] so if you're not actively looking at it then they'll reach out to you and make you aware of it
[4126.16 → 4130.12] but honestly it's what you said earlier about just like doing the right thing from the start
[4130.12 → 4135.74] to make sure that you're not in a space where your users are already having poor experiences and so
[4135.74 → 4140.92] the local testing is really where it starts in an ideal world so once you're creating your
[4140.92 → 4145.32] application or adding new features doing testing locally to make sure that you're not making the
[4145.32 → 4151.82] experience significantly worse so doing things like a b testing doing tracing locally using things
[4151.82 → 4156.68] like throttling just recognizing that the device you're using is not necessarily the device your users
[4156.68 → 4162.20] are using to make sure that you're putting yourself in their shoes and just trying to like slow down
[4162.20 → 4167.44] your network artificially or use a smaller screen size or slow down your CPU in ways that will more
[4167.44 → 4171.16] realistically represent the user experience just to make sure that you are catching these things
[4171.16 → 4177.04] before they happen one tool that I really like to use is the web vitals extension so if you install
[4177.04 → 4182.14] this in chrome it will log to the console in Chrome dev tools what the performance the core
[4182.14 → 4186.92] vitals performance metrics are at any given point, and it also includes this attribution info that any
[4186.92 → 4191.44] mentioned earlier so you could see not only how slow was it but what was causing it to be slow and all
[4191.44 → 4195.60] of the different component phases so that's kind of the quick answer but there are so many other tools
[4195.60 → 4202.12] that I could recommend about um from different rum tooling providers to different lab tools there's
[4202.12 → 4206.20] just so much in the web performance space to help developers it's really just starting with a good
[4206.20 → 4210.82] piece of documentation that uh contains like the wider landscape and for that I'd recommend web.dev
[4210.82 → 4216.28] very cool, and you know hopefully you know we want to make space on this show to kind of talk to
[4216.28 → 4220.90] these you know different companies that produce these performance monitoring tools have them on the show
[4220.90 → 4225.48] um you know there's some really cool stuff that they're doing like for example page speed test has been on my
[4225.48 → 4231.12] list for a while like i I would love to kind of like talk about that um speed curves and not like
[4231.12 → 4237.08] another really cool um like an amazing tool that I would love to kind of have on um on the show uh so
[4237.08 → 4243.72] thank you so much for sharing that rick um and like how like I guess is there an um you know there's no
[4243.72 → 4249.74] like one there's no like magic bullet right I think that's another like takeaway here is like there's
[4249.74 → 4254.86] there's performance work is it's like constant it's like this it's clean like cleaning your house
[4254.86 → 4260.78] it's like never ending you know um and there's like no magic bullet so I think sometimes we're
[4260.78 → 4265.62] reaching for the magic bullet and like you know we just gotta just have to budget for the work instead
[4265.62 → 4271.86] you know yeah I'd also emphasize that it's like kind of like a team effort uh it's up to everybody
[4271.86 → 4277.16] in the entire web ecosystem to make performance better from you the site owner to the framework
[4277.16 → 4282.50] you're using or your cms the browsers that your users are on like there's a lot that chrome is doing
[4282.50 → 4287.44] to make the web faster across all these millions of websites, but everybody needs to understand and
[4287.44 → 4292.96] care about the performance metrics for the entire ecosystem to be lifted that makes sense it's like
[4292.96 → 4298.82] but I guess so for websites that are behind an off wall how does the web vitals report you know help
[4298.82 → 4305.28] those users to surface like I don't I don't I would imagine that they can't, but you tell me you're
[4305.28 → 4309.58] asking like if there's I don't know like facebook.com where you have to be logged in right to experience
[4309.58 → 4314.90] are we able to in a data set like chrome user experience support to measure those experiences
[4314.90 → 4321.48] so the answer is yes at the origin level all of those experiences will be bubbled up to like
[4321.48 → 4327.12] facebook.com, and you could see what percent of your LCP is considered good from all of those other user
[4327.12 → 4333.22] experiences what you can't do is get page level insights in the public data set to say how did a
[4333.22 → 4338.86] user perform on Rick's profile page like that's just a little too much information, and it's its not
[4338.86 → 4342.84] publicly accessible the web page itself and so the data that's made available by
[4342.84 → 4348.36] chrome is not either uh, but this is one of the limitations with public data which is why private
[4348.36 → 4352.88] like first party rum is so important not only because of the visibility of data but the depth
[4352.88 → 4357.92] that you can go into as well to be able to slice through all these diagnostics and also the dimensions
[4357.92 → 4362.68] that you can look at between different uh user populations so it's really necessary to not just
[4362.68 → 4367.46] see am I fast or not but why is really the most important question and for that you need a lot of data
[4367.46 → 4372.72] or good tooling yeah no that makes sense and this is why third-party tools exist you
[4372.72 → 4378.46] know or as you said it first party tools first party for the app you know and you look like
[4378.46 → 4382.52] you wanted to say something so oh no i I just get really excited about that okay
[4382.52 → 4393.48] yeah I think it's its interesting that so many of these tools that both rick and Abel have
[4393.48 → 4399.86] spouted out I didn't know about any of them I've been building for the web for a long time so
[4399.86 → 4405.50] just like i I've unintentionally had blinders on to a lot of these things uh which is probably very
[4405.50 → 4410.84] similar to a lot of developers as well so with that like what we've been talking about is very
[4410.84 → 4416.46] has been very chrome specific uh given the audience here very, very much makes sense but how does
[4416.46 → 4422.20] this translates over to other experiences and other browsers or does it yes this is a really
[4422.20 → 4427.86] great question um my team has really worked hard to try and make it so that every core vital is
[4427.86 → 4433.90] based on an open web standard the standards are all in the web performance working group and uh we are
[4433.90 → 4439.90] seeing Mozilla has done some really fantastic work over the last few years they've got um a big chunk of
[4439.90 → 4446.08] the event timing API implemented, and they've got uh largest content paint API implemented so you
[4446.08 → 4451.32] can get largest content paint in Firefox now, and we're super excited about that and um it's really
[4451.32 → 4455.10] cool one of the things that we do internally in chrome is we try to improve chrome's performance on
[4455.10 → 4460.64] LCP and Firefox is working on that as well and that's that's like really cool to see all the work
[4460.64 → 4467.70] that they're doing on that apple uh and WebKit are not like really as focused on web performance APIs
[4467.70 → 4473.00] and I think that's one thing that we try to communicate to people there's a reason there's
[4473.00 → 4480.72] like a multiple engine right we only control the chromium engine and so if you as a web developer
[4480.72 → 4485.56] really care about WebKit uh supporting this like you need to go tell them because they don't do
[4485.56 → 4491.74] what we tell them otherwise we would just be one engine so uh like if people want to see this in
[4491.74 → 4496.20] WebKit definitely let the WebKit team know I'm not on speaking terms with WebKit right now but
[4496.20 → 4503.00] in general uh yes there's some I mean they're hero ask periodically on Twitter like things like
[4503.00 → 4507.10] that like well what do you want to see yeah I'm just kidding it's not it's not WebKit's fault it's
[4507.10 → 4513.46] just a business decision I'm referring to the whole like EU web apps debacle which whatever different
[4513.46 → 4519.10] show uh so to kind of like you know speaking of other browsers and just in general and I'd say
[4519.10 → 4524.40] community critiques right so we wouldn't, I wouldn't be doing my job if I didn't ask a hard
[4524.40 → 4530.46] question to both of you which is obviously google's business is the web right you know and like a
[4530.46 → 4535.44] healthy web is good for Google's business and luckily those like that's a great incentive to
[4535.44 → 4542.18] have like um for users right like that's that's really for the most part like there's alignment
[4542.18 → 4547.74] there for users and when I think google pushes what I think are really great ideas things like
[4547.74 → 4552.22] Core Web Vitals sometimes there's pushback from the community like oh google's just trying to do
[4552.22 → 4556.92] google things google's just trying to be a bit be a boss of the web and this and that and so I'm
[4556.92 → 4561.98] just curious you know as folks that clearly you know I think have their hearts and minds in the
[4561.98 → 4568.32] right place and their incentives align towards user experiences like how do you all kind of what's your
[4568.32 → 4573.36] what's your response back to that kind of criticism from folks in the community that google's being
[4573.36 → 4578.36] google and Google wants to do google things so I've been in google I think I mentioned it for 19 years
[4578.36 → 4583.42] like I'm here because I'm able to do like huge ambitious projects and I'm able to do those
[4583.42 → 4587.56] things that like really align between me and google improving the user experience on the web
[4587.56 → 4593.32] but at the same time as over the years as we see like different types of criticism I think it's
[4593.32 → 4600.20] really important that like because we're able to do such big massive things that that people do have
[4600.20 → 4605.04] have voices and criticism and that they're able to kind of publicly say either in a standards body
[4605.04 → 4609.56] or just in their Twitter feed or whatever that they're not happy with us that they think we should
[4609.56 → 4614.24] do things differently like we take criticism really seriously, and we think it's really important
[4614.24 → 4620.60] to understand and to process and to take it into account so if people are critical of Google I'm happy
[4620.60 → 4628.00] to listen that's great spoken like a good benevolent leader or I was about to say dictator but I was like
[4628.00 → 4634.80] no wait a second that's not right that's awesome that's that's that's great Andy and yeah I think um
[4634.80 → 4640.64] you know it's a sign of a democracy you know like uh I love the um white house correspondence dinner
[4640.64 → 4645.92] where like everyone gets to openly make fun of the president while the president is also in the room
[4645.92 → 4652.28] like you know that's just the sign of a healthy democracy right so ultimately it's really important
[4652.28 → 4657.38] to be able to push each other and hold each other accountable and be checks and balances for each
[4657.38 → 4662.58] other because like no company no situation no, no entity is perfect we're all better together
[4662.58 → 4667.96] right and so, so thank you for that amazing answer and so rick you want to kind of close us out with
[4667.96 → 4675.68] like a very like Sumbawa like question which by the way earlier when you said like if there's
[4675.68 → 4680.56] one piece of advice I have to give to everyone like I fully was expecting you to say it's where
[4680.56 → 4686.94] where sunscreen I was so confused when you were like talking about performance thing I was like
[4686.94 → 4693.06] wait what about sunscreen you know but rick what I want to know is what do you want everyone
[4693.06 → 4700.12] to know about like why this is important like why this like monumental task this humbling work of web
[4700.12 → 4705.80] performance this never-ending you know what feels like thankless work, but it really isn't you know why
[4705.80 → 4711.00] is this important um why should we care you know why should we care and why should we take on the work of
[4711.00 → 4717.70] making our other stakeholders at work care you know I think to properly answer that I have to talk about
[4717.70 → 4724.10] like the macro and then the micro so at a macro level a faster web is perfect for everybody all
[4724.10 → 4730.64] of the players in the ecosystem benefit from a healthier web and so on a particular website when
[4730.64 → 4735.00] you have a faster site you're going to get more conversions and that's a really effective way to
[4735.00 → 4739.94] convince people who care about web performance or might not care about it yet to invest in it and we
[4739.94 → 4744.42] have all these case studies that we can point out I don't think we've dropped the website who stats
[4744.42 → 4749.22] before, but that is a great place to just send somebody who's maybe on the fence to convince them
[4749.22 → 4756.50] web performance does drive more user engagement and conversions and that's why we're all here doing
[4756.50 → 4760.60] business on the web whatever it might be and I'm using the term business loosely like even like the
[4760.60 → 4764.48] bespoke personal blogs or whatever it might be we're just trying to share content with each other
[4764.48 → 4769.84] and so performance is one of those metrics of user experience, and we want people to be able
[4769.84 → 4774.90] to consume our content in as frictionless a way as possible and it is can come down to other things
[4774.90 → 4779.42] like the design of the page how accessible it is and in some ways performance is a form of
[4779.42 → 4785.72] accessibility because when things are prohibitively slow users cannot access it so that's really the
[4785.72 → 4791.08] micro level is we're trying to provide the best possible experiences for every single user who's
[4791.08 → 4796.56] visiting our site we're going to do the best we can, it's a really hard job to get fast websites 100%
[4796.56 → 4801.74] of the time, but we're that's why we have a 75th percentile we're going to do our best it would be
[4801.74 → 4808.44] great if we could get p90 p100 or p99 even but I think we just have to make every possible user
[4808.44 → 4813.06] experience as fast as it can be, and we don't know unless we're measuring it to be honest so
[4813.06 → 4818.82] we need to measure the user experiences and then share best practices with each other if you have a
[4818.82 → 4823.66] successful case study about how you made your website faster and all the business metrics that you
[4823.66 → 4828.56] saw get faster as a result or sorry not faster but better as a result share that with the community
[4828.56 → 4833.68] because that is really valuable information that will also convince other people and then in this
[4833.68 → 4839.60] viral effect every more and more people will care about performance and not only understand why it
[4839.60 → 4843.18] matters but how to improve it so that's the best piece of advice I could give is to share your
[4843.18 → 4852.22] knowledge share your experiences and sunscreen eat your vegetables and put your sunscreen no um so, so well
[4852.22 → 4858.82] said rick and a rising tide lifts all boats um you know just such a great note to end on and it really
[4858.82 → 4865.48] does take like this collective community knowledge um you know to improve like it's that's the really
[4865.48 → 4872.08] humbling thing about the performance space it's so there's so much to it that you realize that it
[4872.08 → 4877.72] takes a village it takes you know expertise from different people it takes you know it's not
[4877.72 → 4883.70] there's no kind of like there's no hero you know in this story you know like we all have to chip in
[4883.70 → 4890.34] and so thank you both so much for educating us nick didn't you learn a lot I learned a lot I sure did
[4890.34 → 4897.66] learned a ton I've learned yeah there's a lot that I need to go dig into you and everybody else so you
[4897.66 → 4902.64] know you're you are not alone here uh I need to optimize my snowfall
[4902.64 → 4909.84] yes no JavaScript for that yeah and actually speaking of optimization party town like that's
[4909.84 → 4914.34] another show like that's another really cool tool I don't know it's like black magic like they've been
[4914.34 → 4919.24] on my list for a while that I'm like I really want to have them on so but anyway so thank you again
[4919.24 → 4923.74] Annie and rick we're going to have lots of links in the show notes thank you all so much for listening
[4923.74 → 4928.24] where can folks reach you if they want to kind of get in touch or if they have questions like Annie
[4928.24 → 4934.54] do you want to start uh yeah I'm Annie sully on like twitter and threads on LinkedIn yeah I think
[4934.54 → 4940.04] that's the best way to reach out uh rick I'm Rick underscore viscous on Twitter that was during a
[4940.04 → 4944.30] time when I didn't know what the naming convention was for handles on Twitter I was like that's gonna
[4944.30 → 4950.68] say that's so corporate I love if it's like it's like enterprise rick on Twitter love it all right
[4950.68 → 4954.36] everyone have an amazing rest of your day cheers all
[4954.36 → 4974.66] all right that is JS party for this week thanks for listening don't forget to check out our 100%
[4974.66 → 4981.40] free slack community there are over 7 000 curious kind technologists who have already joined in on
[4981.40 → 4987.52] the fun seriously it's one of the web's best places to hang out sign up today at JS party.fm
[4987.52 → 4995.14] slash community thanks once again to our partners at fly.io to the mysterious break master cylinder for
[4995.14 → 5000.84] these dope beats and to sentry use code changelog when you sign up at sentry.io, and they'll give you
[5000.84 → 5007.42] 100 bucks off the team plan that is all for now but come back and party with us again next week
[5007.42 → 5009.58] you
[5009.58 → 5011.58] you
[5011.58 → 5013.58] you
[5013.58 → 5015.58] you
[5015.58 → 5017.58] you
[5017.58 → 5019.58] you
[5019.58 → 5021.58] you
[5021.58 → 5023.58] you
[5023.58 → 5025.58] you
[5025.58 → 5027.58] you
[5027.58 → 5029.58] you
[5029.58 → 5054.32] you
[5054.32 → 5056.32] you
[5056.32 → 5058.32] you
