[0.00 → 16.54] let's do if it's go time welcome to go time your source for diverse discussions from all around
[16.54 → 22.62] the go community connect with us on the socials we're on Twitter at go time FM and on mastodon
[22.62 → 28.82] at go time at changelog. Social thank you to our friends at fast go time ships fast globally
[28.82 → 34.42] because quickly is fast globally that's how it works check them out at fastly.com and to fly
[34.42 → 40.84] deploy your app servers and database close to your users no ops required learn more at fly.io
[40.84 → 43.30] okay here we go
[43.30 → 55.70] hello everyone and welcome to go time today I am joined by Carson gross Carson you want to say hi
[55.70 → 60.64] everybody how's it going everybody great to be here excited to talk a little bit about
[60.64 → 66.70] how you can do more work and go so Carson describes himself as a greybeard programmer he's the creator
[66.70 → 71.24] of HTML which we're going to be talking about today he's also the creator of hyperscript and
[71.24 → 77.66] grugbrain.dev we're also joined by Chris jams who's an unemployed bum, but he is looking for work if
[77.66 → 83.94] anybody's hiring Chris also wrote learn go with tests Chris how are you doing I'm doing great I'm
[83.94 → 88.30] really excited to be on the show I'm very HTML curious so I'm excited to talk about it and learn
[88.30 → 95.30] more sounds good, and lastly we have Dave wicks who are a wannabe greybeard and an employed bum who
[95.30 → 100.22] likes to fix I don't know if he likes to, but he fixes typos and learn go with tests, and he's
[100.22 → 104.76] unnecessarily belligerent on Twitter, and he's written a lot of javascript yeahs I feel like this
[104.76 → 108.66] podcast is going downhill we've got somebody who writes JavaScript and an unemployed bum
[108.66 → 115.98] I think you have to be is it possible to be overly belligerent on Twitter I'm not sure uh
[115.98 → 120.52] how could you be kind on Twitter I'm not sure i just I walk into these things too often
[120.52 → 127.70] all right, so today the goal is to talk about HTML which Carson created, but before we get into that i
[127.70 → 133.70] wanted to talk a little bit about sort of the history of how we've come to learn to develop web
[133.70 → 138.58] applications and sort of how they've evolved over time so that people understand how we kind of
[138.58 → 143.50] got to the state that web applications are in today and why these different technologies have
[143.50 → 148.28] been created to help us because I think it's going to help us understand like where HTML fits into the
[148.28 → 153.80] whole equation so I guess starting off whoever wants to take this where did you guys start with
[153.80 → 158.26] like developing web applications what did they look like or rather what did that process look like
[158.26 → 163.50] I'll just start off I'd be interested to hear what Chris and Dave went through as well but I started
[163.50 → 171.62] pretty early on in the late 90s doing web development and back then it was CGI stuff so
[171.62 → 178.98] you just used pearl or bash or whatever you could and uh you created you know a little dynamic website
[178.98 → 186.38] a little bit of dynamicism with using a CGI gateway so very unstructured compared to what you have today
[186.38 → 192.52] I actually ended up getting a lot more interested in something called applets which were Java-based
[192.52 → 199.64] like their kind of in some sense very similar to spas it was more of a there was a sandbox around
[199.64 → 206.44] them so it wasn't as interactive with the browser but I ended up going kind of that direction for a
[206.44 → 213.66] while before i sort of when j2e when the java world sort of embraced the web and all that stuff came
[213.66 → 219.88] up then I started doing what would be recognizable web programming to today's developers so that's kind of
[219.88 → 224.70] that's how I got into it so if I remember correctly weren't applets supposed to be the future of web
[224.70 → 229.54] applications there wasn't that the big pitch they could run anywhere and yeah they were there was
[229.54 → 235.40] flash too which a lot of sorts of the design side of the world was really did a lot of work with um kind
[235.40 → 240.36] of you know today's developers might think of like canvas what a canvas is thought of that but with a
[240.36 → 246.82] really elaborate API within if it's funny that I've ended up becoming such an ambassador for hypermedia
[246.82 → 254.28] because in the mid-2000s I gave up on the web and i I used something called java web start which it was a
[254.28 → 260.60] way to deliver thick clients to customers over the net and so it was a way to build thick client
[260.60 → 268.22] applications network applications and I came back to the web sort of after that phase and uh I'm sorry to
[268.22 → 272.70] appreciate more for what it was but I do think it's a little funny that i sort of went through this
[272.70 → 278.14] you know i kind of saw it very early didn't like it went and did thick client stuff and then came
[278.14 → 283.00] back with like oh there's actually something to this so when you were working with like the CGI type
[283.00 → 287.62] pages was it similar to like PHP in the sense of like it's mostly a HTML page with like little
[287.62 → 295.50] snippets of code inside of it yeah imagine PHP but like without the elegance okay it's like a hacky
[295.50 → 303.10] version of PHP okay Chris yeah so I also started making my first website in the late 90s but I was
[303.10 → 308.90] 14 you're 14 years old at the time and I was extremely cool so I made a website about pro wrestling
[308.90 → 315.56] and I did it on a thing called geo cities um which was a thing that yahoo kind of made available for free
[315.56 → 320.92] where you could upload your own HTML files and make a website I didn't know programming or anything
[320.92 → 325.84] like that I could view source I figured out how to view source and I just went to other websites
[325.84 → 330.62] and more or less covered it all together what I find interesting now is that yeah that seems like
[330.62 → 335.28] an archaic way of making websites but actually if I reflect on it that's basically how my current blog
[335.28 → 342.36] works I have HTML files the only real difference is that we have CSS now to style things whereas at that
[342.36 → 351.48] time it was all inline styles, but the basic tech really was kind of the same you know like 24 25
[351.48 → 356.58] years later so when you were doing that was that back when designing a web page usually meant like a
[356.58 → 363.30] big table, and you like cut up images yeah there was no such thing as like CSS layouts there were no
[363.30 → 370.08] jokes about entering DIVS it was all making tables with nested tables and also there was a technique
[370.08 → 377.98] called spacer images used to artificially create space on your page with images which is quite an
[377.98 → 382.78] interesting way of I guess in a way it's quite ingenious but obviously seems absolutely appalling
[382.78 → 387.40] these days, but it worked you know to say I think I've actually done that like later in my career like
[387.40 → 392.56] not that long ago because I was just like settings like trying to design something I'm like I know this
[392.56 → 397.28] works from whenever I first learned and I'm like whatever this will work for the time being and I'll fix it
[397.28 → 403.32] later so also on geo cities have you ever checked out neo cities' no what's that I think it's supposed
[403.32 → 408.50] to be like a recreation of sort of what geo cities was but I've never actually used it enough to really
[408.50 → 414.28] know for sure I just remember seeing it somewhere at one point do they have the fire GIFs I hope so
[414.28 → 420.18] but I don't know it's the only thing that matters as far as I'm concerned I was absolutely rocking the
[420.18 → 427.06] fire GIFs flamingtext.com was just incredible to me like I couldn't imagine technology greater than
[427.06 → 431.50] that yeah it was amazing I also remember like the scrolling marquee text which was on like
[431.50 → 437.54] every geo cities website so some good features there I was really worried that this conversation
[437.54 → 441.10] is just going to be people talking about how wonderful the old days were you know just a lot
[441.10 → 446.66] of reminiscing like oh now I'm just like oh my god it was hell there was definitely some downsides
[446.66 → 454.04] every time period has its highs and its lows so continuing my journey so I eventually did learn
[454.04 → 459.48] to program at least somewhat and I think like the first biggish website I worked on was a PHP website
[459.48 → 463.84] so that was doing something a bit more dynamic right it was like putting things from a database
[463.84 → 471.08] and stuff but at that point CSS still wasn't well-supported I seem to recall so you still had this
[471.08 → 476.64] issue of like even though like I could do some programming and stuff in order to generate HTML on the
[476.64 → 481.86] server I was like writing PHP which was putting inline styles into markup right and I think for
[481.86 → 487.44] me like in my view a big step forward for web development was when CSS became a lot better
[487.44 → 493.28] supported not only because it sort of gave you a more a simpler way of styling things but it also
[493.28 → 498.90] meant that the work you did on the server was suddenly a lot simpler because instead of you know
[498.90 → 504.40] creating HTML of inline styles you were just creating like HTML which was actually made the job a lot
[504.40 → 509.34] simpler for me that was like a moment where web development started feeling a bit more productive
[509.34 → 515.92] than it was before all right so we've got i don't want to say static pages, but we have like server-side
[515.92 → 521.50] rendered pages with PHP and these different things and then at some point the web started pushing
[521.50 → 526.82] towards this i guess more interactive version of it and the first place i really remember like at least
[526.82 → 531.08] it has like a sticking impression in my head is with flash I'm sure there's like you mentioned
[531.08 → 535.20] applets which i believe were doing something similar so i guess do any of you have experience
[535.20 → 540.66] developing with flash like to have you okay I'm getting a bunch of head shakes no so I'm assuming
[540.66 → 546.02] not but for anybody who's out there who's younger who maybe doesn't remember this flash used to be the
[546.02 → 551.58] way that like every game on the internet was made so you'd go to these pages that had these pretty
[551.58 → 557.02] well-built games that would run on flash, and you could do all these interactive things and i think
[557.02 → 561.68] that's kind of what led the way for like what we now view as like a application being built into
[561.68 → 565.70] the browser so now it's pretty common like you have Google Docs, and you have all these things but i
[565.70 → 569.84] think back when the web was created the idea of thinking that you could actually have a text editor
[569.84 → 575.50] inside your browser was kind of crazy at the time i don't you guys did you guys have that same
[575.50 → 580.60] impression when you were first starting yeah i think there was definitely early on there was a big
[580.60 → 588.80] disconnect between rich content and then hypermedia content so hypermedia stuff was relatively and still
[588.80 → 595.70] is in many cases today pretty basic forms with some pretty simple form controls at the most
[595.70 → 601.04] elaborate you know is often just hypermedia documents you're clicking around in and then there was this
[601.04 → 608.50] other world that had much richer event handling, and typically it was canvas based or there was some
[608.50 → 613.30] infrastructure built on top of a pretty raw canvas that you had access to and so that's what flash
[613.30 → 619.10] gave you, and it lets you do much lower level graphics programming and actually flash was I mean
[619.10 → 624.38] in many ways flash was a really cool is a really cool technology to go back and look at because it had
[624.38 → 629.66] a lot of very interesting things going on inside of it so some low level as well as high level tools
[629.66 → 635.28] for building these things i always think i think flash is one of the great tragedies of the early web
[635.28 → 640.84] in lots of ways not in terms of writing it but because so much extraordinary content got built
[640.84 → 646.98] in flash i can think of hundreds of websites i used to visit in flash games everywhere and these
[646.98 → 650.78] are now inaccessible nobody can see these things any more nobody can play them anymore nobody can
[650.78 → 656.00] visit them because they're built on a platform that just went away just really sad you know
[656.00 → 660.66] did all of those sites shut down like if i were to boot up a ancient computer with an old browser
[660.66 → 665.62] are there any other sites still working i think you might be able to get to home star runner
[665.62 → 671.68] if that rings any bells that do i could watch him check his email that's about it
[671.68 → 680.16] okay so now we have I guess what we considered modern web applications which to many people are just maybe
[680.16 → 686.58] web applications, so things like Gmail and Google Docs and pretty much anything you're used to seeing
[686.58 → 692.42] online that feels like an interactive page so i guess when you think modern web apps i guess how do
[692.42 → 698.18] you guys see them being built what is like the traditional approach well i would say today the
[698.18 → 705.94] default approach is going to be a React based front end talking to a back end over using Jason
[705.94 → 714.20] some sort of Jason API that's sort of the standard approach that i see most people taking so i don't know
[714.20 → 719.20] if you want to call that the traditional web application architecture but i would definitely
[719.20 → 723.52] say it's the most common thing that i see online now there are obviously plenty of websites that are
[723.52 → 728.80] being built different ways either with view or you know whatever's developed or something like that
[728.80 → 735.04] but by and large i think if i is you were to ask 10 web developers what's the standard way to build
[735.04 → 742.36] they would say that and tom might i think has a blog post about that saying this is the standard way
[742.36 → 748.02] today that most people build websites so i don't know if Chris and David would agree with that
[748.02 → 753.22] i don't think it's its not the way i would choose to build a website, but it's definitely the way i get
[753.22 → 758.40] paid to build a website yep it's very rare you get a technology choice in many companies outside
[758.40 → 764.84] react you'd be directed to you know here's the stack get to react going please use exciting feature
[764.84 → 769.12] number seven that's been added in the time since you last used to use React, but that's something else to
[769.12 → 774.90] talk about and uh you know build your back end service make it restful and air quotes there for
[774.90 → 780.38] people who can't see a camera and uh, and you know build the front end using lots of React components
[780.38 → 785.54] yeah that's pretty much what you get these days you know I'm sure people use angular or other things
[785.54 → 792.50] but i don't think that's got the same reach these days yeah i would agree that i think that is if
[792.50 → 796.48] people think about what's modern i think that's what pops in their head like as you said it could be a
[796.48 → 799.98] different JS or JavaScript front end of some sort, but it's going to be something in that
[799.98 → 805.62] realm that's going to be pretty similar and I've even seen people using what is it gRPC because
[805.62 → 809.48] there are some services allow you to use gRPC in different ways whether it's like setting up some
[809.48 → 813.80] sort of front end that translates to Jason or like just having something that automatically handles that
[813.80 → 819.96] for you but for the most part it's roughly the same idea and i guess GraphQL is mixed in there
[819.96 → 824.62] it's still returning Jason, but it's just like a slightly different approach i guess to getting your data
[824.62 → 831.46] yeah it's a technology to layer on top of the j science and i would say you know David mentioned
[831.46 → 837.98] restful i would say GraphQL is a step away from restfulness and more towards a generalized query
[837.98 → 844.22] language which i think makes sense because you know in my opinion the spa approach is a thick client
[844.22 → 850.00] you're effectively building a thick client like i was trying to do in java swing back in the day
[850.00 → 855.30] and uh when you start building a thick client you have different needs from your network protocol
[855.30 → 860.18] than what the web provides out of the box, and you want general you know something like a general
[860.18 → 866.60] query language like SQL gives you on the back end so GraphQL starts to make a lot of sense and then
[866.60 → 872.64] why even use Jason you know use Google serialization technology or whatever so when somebody goes to
[872.64 → 878.56] actually build an application using this modern approach I'm assuming you've all had some experience
[878.56 → 882.22] with it or if not you've at least talked to developers who have what does it actually look
[882.22 → 885.40] and feel like in practice because i feel like in theory it's one of those things that sounds
[885.40 → 889.40] great it's like you've got the server it's separated you've got the front end, and it's all
[889.40 → 895.84] going to just interact beautifully but i guess my experience has been slightly varied so how has
[895.84 → 899.62] that been for you guys what does that experience feel like i think to be fair a lot of time you can
[899.62 → 904.76] feel very productive i think if you can get to that sweet spot where everything's set up correctly
[904.76 → 909.88] and you've got the correct blend of the various libraries and frameworks everything else it can
[909.88 → 916.86] feel productive but for me whenever I'm working in these systems i feel like I'm having to
[916.86 → 924.02] hold a lot of knowledge about react in order to get some work done and i think it's quite easy to
[924.02 → 928.56] create something that's not very good in this one, so a classic is almost like quite a lot of time you
[928.56 → 933.34] can go to a React website and if it hasn't been written correctly you know it won't be optimized so
[933.34 → 938.00] therefore you'll download like 30 legs of JavaScript or something like that, or maybe they've made a
[938.00 → 942.34] mistake and if you try and press the back button it doesn't work correctly and always people will say
[942.34 → 947.68] well there's React router and there's all these other things but to me, i start to feel exhausted
[947.68 → 954.26] in this world because it's just another thing i have to learn you know coming back to when i was first
[954.26 → 960.06] making websites when i was 14 i didn't have to worry about the browser history or the back button
[960.06 → 965.64] it just worked out of the box because it's the browser takes care of that but when you go into
[965.64 → 971.12] this world of having these fat clients what you tend to be doing is throwing away a lot of
[971.12 → 976.52] the functionality that the browser gives you, and then you're having to either re-implement it itself
[976.52 → 982.24] or at least know enough to bring the particular version of a particular library in order to plug into
[982.24 → 987.94] your thing so that it will still work like a browser I think for me that's the exhausting thing about it
[987.94 → 994.00] like there's no doubt that like spas have a good fit for a number of things, but it's a lot of
[994.00 → 999.76] complexity you have to take on, and you know we're on version 18 of React now I think what's interesting
[999.76 → 1005.38] is that go and React are basically the same age in terms of like you know I mean I know reacts as a
[1005.38 → 1009.40] as a framework or a library and go as a programming language, but it's interesting to me that they're both
[1009.40 → 1016.94] the same age and yet like go's path has been very small simple evolution I've never felt like I've had to
[1016.94 → 1022.34] relearn go whereas like with react at first I was doing class components and then suddenly that was
[1022.34 → 1027.46] the wrong thing to do and I should be doing functions instead and no one could really articulate
[1027.46 → 1033.42] why other than people having a big distaste for o as far as I could tell so yeah I think it's just a
[1033.42 → 1037.96] lot to take on i I think particularly for some projects where I feel like it's just not you just
[1037.96 → 1043.54] don't need all that complexity yeah i so i I came to web development very late in my software
[1043.54 → 1047.94] development very late in my life I was uh 35 I went to a boot camp because I hated marketing
[1047.94 → 1053.80] which is still reasonable and uh I got lucky in lots of ways so I hit the inflection point I learned
[1053.80 → 1060.94] to build my web apps using server-side rendering rails I learned Sinatra as ruby developer lots of
[1060.94 → 1066.26] boot camps are, and it was basically the second thing I worked on was a React app ultimately the
[1066.26 → 1072.14] first thing I worked on front end HTML sprinkler JavaScript lots of server-side rendering and then ever
[1072.14 → 1076.38] since then it's been on and off react and every time I've come back to it every time I had to do
[1076.38 → 1080.78] it is again like take a month break take three months or four months to go back into this comeback
[1080.78 → 1086.54] had to start again had to start literally all over again you know all of a sudden inline styles comes
[1086.54 → 1090.94] in out you know we're going to put the styles over here now everything's uh we're using hooks
[1090.94 → 1094.72] which as far as I can tell it's just a sneaky way of getting state into your application rather than
[1094.72 → 1099.30] say you've got objects, but you know that's fine, and then you know every time I stop doing that and you
[1099.30 → 1104.08] build something with server-side rendering it's still the same doing the same things I was doing
[1104.08 → 1110.54] way back in uh probably 2015 2014 the first way I learned it whereas React has just been a constant
[1110.54 → 1117.18] battle just to stay ahead and also to produce exactly the same websites this is the real disaster
[1117.18 → 1123.04] it's just as far as I could tell the websites I was building in react with react I don't know which
[1123.04 → 1127.68] version it was then eight maybe ten are going to be exactly the same things as every iteration is
[1127.68 → 1135.26] so yeah I feel like I'm in some sort of uh horrible samsara of React development the pain just
[1135.26 → 1143.16] never ends yeah, but you know please hire me to build your React websites yeah my so after the early
[1143.16 → 1148.68] stuff I got back into web development and I was working in rails in the mid 2000s because that's
[1148.68 → 1155.46] what everyone who was doing a startup was building them in at the time and um that was right when react
[1155.46 → 1160.78] came out and what I noticed about react and i you know was like oh this is new and interesting has
[1160.78 → 1166.82] some relation to some of the big client style programming I did previously but what I noticed
[1166.82 → 1173.78] about it was that we started building up a big JavaScript front end like a separate code base and I think a lot
[1173.78 → 1179.88] of people take that for granted today, but that wasn't the case earlier on previously you worked primarily
[1179.88 → 1185.78] in a back-end language and I'm not a huge fan of JavaScript I've come to terms with it is has its
[1185.78 → 1192.52] good aspects but at the time I was much stronger in my distaste for JavaScript, and we just started
[1192.52 → 1198.76] growing this big JavaScript code base and I didn't want to deal with that so the motivation for intercooler
[1198.76 → 1207.40] JS which was the sort of initial version of human back in 2013 was this sense that you know what I know
[1207.40 → 1213.88] rails and I like rails and I want to stay in rails but I still want more interactivity and so how can
[1213.88 → 1221.32] I do that in such a way that I can still do most of my UI work in rails using rails emulating which i
[1221.32 → 1227.16] knew pretty well instead of having this you know big front end code base I think you've seen that
[1227.16 → 1232.64] that same pressure the people that I noticed when you start having this big JavaScript code base it puts
[1232.64 → 1238.66] pressure on you to have JavaScript on the back end too because why have two different programming
[1238.66 → 1243.78] languages why not have the same programming language and share for example domain logic between the front
[1243.78 → 1249.88] end and the back end and so forth validation logic all that sort of stuff so that was a big motivator for
[1249.88 → 1258.02] me was I just I didn't want to take on this big JavaScript front end code base I was working by myself we
[1258.02 → 1264.60] didn't have a front end back end split, and so i kind of had to do both and i just I couldn't I
[1264.60 → 1270.80] couldn't keep reacting in my head and still remember everything I needed to remember about rails so
[1270.80 → 1276.32] just to make sure I have this right you didn't want to work on a big JavaScript application so you built
[1276.32 → 1282.32] another JavaScript application yeah it is ironic that in order to avoid writing JavaScript I've written
[1282.32 → 1288.44] quite a bit of JavaScript so it got worse after that though maybe we'll talk we'll talk about
[1288.44 → 1293.52] hyperscript that was a lot of JavaScript to avoid writing JavaScript Carson I think one of the things
[1293.52 → 1298.76] you mentioned is really worth reiterating is the fact that with that JavaScript front end and with
[1298.76 → 1303.18] a separate back end which tends to happen fairly often one of the things that can also be hard is
[1303.18 → 1308.78] that smaller teams or solo developers can struggle to sort of build applications with that setup because
[1308.78 → 1312.90] like you said they have to know so much more and I know like the first project I worked on with a
[1312.90 → 1318.20] react front end what always killed me was that we had one person who knew the React side and everybody
[1318.20 → 1323.30] else there was like four developers who knew the back end and for us to make changes even if it was
[1323.30 → 1327.00] something tiny the back end would be a bunch of code, but then there'd be a small two-line
[1327.00 → 1330.52] change on the front end but to figure out how to do that and to make sure it got done correctly
[1330.52 → 1336.14] was always a struggle because that one person was so overwhelmed that they rarely had the time to sit
[1336.14 → 1339.38] down and explain to us like this is what you need to do to get it running locally and this is what you
[1339.38 → 1345.68] need to do to test it all so it was just kind of tough all around and I think sometimes people can
[1345.68 → 1349.62] look at the technology and think oh this is great, but they can ignore like maintenance costs and like
[1349.62 → 1354.74] whether it's going to change their velocity and things like that it can speed you up in
[1354.74 → 1360.02] some ways but I think you have to have the team that's like designed around that yeah what you're kind of
[1360.02 → 1365.34] touching on is the idea of full stack development and I think one of the really nice things about
[1365.34 → 1370.56] early web development is that it was full stack you were responsible for not only the business logic
[1370.56 → 1376.02] and often the database queries and all the rest of it, although you often added DBA to help you but
[1376.02 → 1381.80] you also were responsible for the front end and there was a sense of completeness in your work what
[1381.80 → 1387.98] Marx calls if it was not alienated labour like you didn't just screw one bolt into a car that was
[1387.98 → 1393.56] going out the front door or whatever you built the whole car so you built the whole feature, and you could
[1393.56 → 1398.04] point at it, and you could click being able to interact with something on a screen is a really
[1398.04 → 1403.20] satisfying aspect of computer programming and when you have this front end back end split I think you
[1403.20 → 1409.08] kind of split the brain a little bit and enter into at times a little bit of a dissociative state where
[1409.08 → 1414.30] you just you don't have this sense of completeness in your development that you can have if you're able
[1414.30 → 1421.20] to do full stack development, and you know there are arguments that that's good at times you know you're producing a
[1421.20 → 1428.62] generic API maybe in Jason or whatever the argument is specialization and all that sort of stuff but at
[1428.62 → 1434.32] the same time I think it does it rob velocity because you don't you know you can have miscommunication
[1434.32 → 1440.30] you're waiting on them there they have other things they need to do whatever it is as soon as you split a
[1440.30 → 1446.32] particular complete feature into two sides you just introduce friction in all sorts of different ways
[1446.32 → 1451.42] you know this is a little maybe a little bit out there but I would say I think some of it is actually
[1451.42 → 1455.86] sort of spiritual aspect there's a spiritual aspect like this sense of completeness and
[1455.86 → 1461.46] satisfaction with a feature that is hard to achieve if you don't have something like full stack
[1461.46 → 1466.38] development at least for me that's what I've found if I recall correctly I believe it was bill
[1466.38 → 1471.64] Kennedy was on the podcast not long ago, and he told a story about how he built this back end for
[1471.64 → 1475.46] somebody who was building the front end feature and then later when he sat down to try to figure out like
[1475.46 → 1479.02] how they would build the front end he realized that what he provided them on the back end was
[1479.02 → 1483.86] just terrible for what they were trying to build, and he asked them like why did you not tell me
[1483.86 → 1488.26] that this was the case and the front end developer basically just said we just deal with what we're
[1488.26 → 1493.38] given, and he basically sat down with them and redesigned it all but I think like you said like
[1493.38 → 1497.76] another downside people forget is if you aren't involved in the whole process sometimes you design
[1497.76 → 1502.80] what isn't a great thing you know like isn't a great back end for the front end just because
[1502.80 → 1505.94] that's what's easiest for you, and you don't really realize what they need or what they're going to
[1505.94 → 1510.88] have to show data wise, and it ends up causing more work in some ways yeah rather than you know
[1510.88 → 1516.26] actually having it be much more effective than you like you expected I guess yep, and you can also you
[1516.26 → 1522.40] can't optimize across the entire stack like if you provide a generic API this is why there's so much
[1522.40 → 1527.86] pressure to adopt GraphQL because it kind of gets you out of the business of having to predict
[1527.86 → 1533.64] what your front end needs are like they can do whatever they want to now and so that's where a
[1533.64 → 1538.46] lot of that pressure comes from to just give them a generic API and then let them figure it out
[1538.46 → 1543.72] but if you have full stack development this is a is one of the wonderful features of hypermedia
[1543.72 → 1549.48] in particular HTML is an I would call it a hypermedia oriented language, but we're in a hypermedia oriented
[1549.48 → 1556.88] library I should say but hypermedia because of the way it works lets you be much more dramatic in your
[1556.88 → 1562.72] changes to your back end because you're you're consuming if it's just one it's all one hypermedia
[1562.72 → 1570.44] system and so um you're able to tune what you do with that hypermedia response much more
[1570.44 → 1575.18] extensively and for yourself because you're on both sides of the wire so it opens up a lot of
[1575.18 → 1580.44] opportunities to optimize systems that aren't there when there's this hard break between the front end
[1580.44 → 1585.70] and back end, and you have to submit a ticket to get an API updated, or you have to look at a ticket
[1585.70 → 1590.36] that's been submitted to update your API, and maybe you get it done in a couple of weeks or whatever now
[1590.36 → 1595.08] I want to get this button on this screen in this spot I wanted to do this thing on the back end and
[1595.08 → 1600.32] you're done in 10 minutes instead of a back and forth and whatever maybe a week later it works
[1600.32 → 1605.46] having that ability is really, really nice you know being able to hit refresh in a browser and have it
[1605.46 → 1610.70] work it's pretty magical I would even say you would mention that like GraphQL was kind of this push for
[1610.70 → 1615.62] like design the back end once and let the front end people sort of just make it work even like when
[1615.62 → 1621.10] people talked about building a restful and air quotes a server like or an API I feel like that
[1621.10 → 1625.94] was kind of revolving around that same mindset of like if you base this around resources they can call
[1625.94 → 1629.96] the endpoints they need to get the resources, and it ignores the fact that like on a lot of pages you
[1629.96 → 1634.36] need information from like six different resources so like you get to these pages where like the front
[1634.36 → 1638.62] end developers only option is like let me make six different API calls yeah but like if you're designing
[1638.62 → 1642.40] it from front to back you're going to be like well that's kind of silly why don't we just send all the
[1642.40 → 1647.10] data in one query you know one query and have it there, and it's kind of weird how we've gotten to
[1647.10 → 1650.88] this point where people build applications that way and they kind of optimize things around that
[1650.88 → 1656.16] when in reality if you were to sit down and think about how you're designing an API for a specific page
[1656.16 → 1659.60] you'd be like well I want to give them all the data in one request I don't want to like to make them
[1659.60 → 1665.18] make six requests yeah that's right, and it was so on the back end the way we used to think about that was we
[1665.18 → 1670.58] want to minimize the number of database queries we make right you've got a database it has tables in
[1670.58 → 1676.44] whatever form it has, and you wanted to issue we were always like five or fewer queries before we get
[1676.44 → 1681.86] out the door ideally like two or three queries would be even better and to do that SQL has to have you
[1681.86 → 1686.14] know you'd have to use some pretty sophisticated SQL with a lot of joins, and you know sophisticated
[1686.14 → 1692.20] collection and build up your data structure whatever it was, but that was done in order to optimize the
[1692.20 → 1698.38] performance of a given page and I think that as front-end developers with these SBA frameworks get
[1698.38 → 1702.18] more and more into it what they're going to find is they're going to need something as expressive
[1702.18 → 1708.22] as SQL to do this stuff efficiently right they're in the same boat they don't want a bunch of
[1708.22 → 1712.04] queries being issued on the back, and they don't want a bunch of you know hitting a bunch of endpoints to
[1712.04 → 1716.88] wire together an UI, and so they're running into the same problem which I think is where GraphQL
[1716.88 → 1720.38] that's where GraphQL kind of emerged from is that particular problem
[1720.38 → 1745.90] hello friends this is jarred here to tell you about changelog plus over the years many of our most
[1745.90 → 1752.42] diehard listeners have asked us for ways they can support our work here at changelog we didn't have
[1752.42 → 1758.80] an answer for them for a long time, but finally we created changelog plus a membership you can
[1758.80 → 1765.86] join to directly support our work as a thank-you we save you some time with an ad-free feed sprinkle
[1765.86 → 1773.32] in bonuses like extended episodes and give you first access to the new stuff we dream up learn all about
[1773.32 → 1779.64] it at changelog.com slash plus you'll also find the link in your chapter data and show notes
[1779.64 → 1785.32] once again that's changelog.com slash plus check it out we'd love to have you with us
[1785.98 → 1796.84] so you created what's now HTML how does that sort of fit into this equation or can you just describe
[1796.84 → 1803.40] what HTML is for somebody who's not familiar like I said HTML is a hypermedia oriented library so it's
[1803.40 → 1810.04] a JavaScript library, but it's a JavaScript library that basically completes HTML is the way I would say
[1810.04 → 1818.56] it so HTML is a hypermedia we're all used to it and really the only hypermedia controls in HTML are
[1818.56 → 1824.60] anchor tags, so links like you used to clicking on and then forms which you used to you know if you've used
[1824.60 → 1829.08] a more traditional web application you're used to filling out drop-downs and check boxes and clicking
[1829.08 → 1837.98] submit and what HTML does is it takes those two basic elements of HTML and then generalizes them
[1837.98 → 1845.62] using attributes that you can put in your HTML so if you want with HTML you can make any element
[1845.62 → 1854.02] make a http request to the back end a get or a put or a post or a deleted or whatever you have access
[1854.02 → 1860.84] to all the http actions which is in contrast with just vanilla HTML unfortunately and then what makes
[1860.84 → 1867.20] HTML special or I think where it really improves on HTML is that you can take the response that comes
[1867.20 → 1873.28] back from the server which will be HTML content, and you can place it anywhere you want in the document
[1873.28 → 1879.60] so you don't have to replace the whole page and I think that that's sort of the crux of why people
[1879.60 → 1887.72] moved away from the original web model to spas to JavaScript heavy applications it's a big part of
[1887.72 → 1894.26] it in any event is that they're in the traditional web applications you have this big clunky click
[1894.26 → 1901.06] submit in a form and then there's a big page refresh the whole page often flashes you lose your scroll
[1901.06 → 1908.58] state there's often not a very good indicator what's going on and so forth and so that led older HTML based
[1908.58 → 1914.74] applications have this very clunky feel associated with them and newer spas would update the Dom kind
[1914.74 → 1921.04] of in memory and that would make them feel much smoother so what HTML does is it allows you to update
[1921.04 → 1928.00] the Dom in line, but it does that with a HTML exchange with the server so in that sense it's much more like
[1928.00 → 1935.50] the older apps, but it has a feel more modern single page applications so that's the big idea with
[1935.50 → 1943.06] HTML in practice you end up annotating your HTML with attributes that are HTML specific so if you
[1943.06 → 1950.02] wanted a button to issue a put to slash update you would have on your button tag you would say he put
[1950.02 → 1957.42] equals as an attribute he put equals and then in quotes slash update and that would when that button
[1957.42 → 1962.80] was clicked on issue a put to that URL with whatever information happened to be around it
[1962.80 → 1968.48] and since we're using attributes we're not writing JavaScript HTML is JavaScript but when you're an
[1968.48 → 1975.36] HTML user you're just using attributes in HTML and so that means you're just annotating your HTML
[1975.36 → 1983.38] which means that traditional emulating technologies like PHP or like ghost templates or what it rails
[1983.38 → 1989.32] era templates and all that sort of stuff those all suddenly are relevant again because you can take
[1989.32 → 1994.32] those, and they're not just sort of afterthought they're actually you actually annotate those with
[1994.32 → 2000.20] the interactivity that you want from your system Carsten maybe you could quickly explain what
[2000.20 → 2006.06] hypermedia is in a little bit more layman's terms sure and also relate it to rest because a few of us
[2006.06 → 2011.34] have been a bit snooty about rest already yeah so I think it's probably worth us laying out what we feel
[2011.34 → 2018.16] rest actually is and why that's important and maybe like contrast it to sure the spa approach of sort of
[2018.16 → 2025.04] building web applications yeah I'm happy to nerd out on that absolutely so um hypermedia all
[2025.04 → 2030.52] hypermedia is a media so in the case of HTML which is hypermedia we're all most familiar with
[2030.52 → 2037.34] it's a media that has what are called hypermedia controls in it and the classic hypermedia control
[2037.34 → 2044.20] is an anchor tag or a link and when you have an anchor tag a HTML document it makes that document
[2044.20 → 2048.94] non-linear right early on that was the big deal about hypermedia is that you're not just reading
[2048.94 → 2054.88] a document you're interacting with it, you can follow links to other documents, and you know that's
[2054.88 → 2062.32] the idea of this web and then the form tag which I think came on along in html2 introduced this idea of
[2062.32 → 2067.36] updating actually you're interacting with it was more than just following links around in academic
[2067.36 → 2073.40] documents which is where the web sort of started out now suddenly with this form tag you had the ability
[2073.40 → 2079.60] to actually pass a significant amount of information up to a server and update the notion
[2079.60 → 2087.52] of updating content on the web was baked into HTML and so HTML has sort of these two core hypermedia
[2087.52 → 2094.34] controls these two core ways of interacting with the document in a non-linear manner and that's why HTML is
[2094.34 → 2101.02] hypermedia and so people recognize that this was a new and interesting technical approach to things
[2101.02 → 2106.66] the idea had been kicking around for a while but Roy fielding who did a lot of the initial work
[2106.66 → 2113.00] in the Apache project on a lot of the early web technologies he wrote a thesis or a dissertation i
[2113.00 → 2120.12] should say for his PhD and uh in that he coined this term rest that we've been sort of talking about
[2120.12 → 2126.64] and so what he tried to do in his dissertation it's a very academic language unfortunately but what he tried
[2126.64 → 2133.30] to do was discuss how's the web different from other network architectures that have been adopted
[2133.30 → 2139.44] before so he'd been in technology for a while so he was familiar with the older thick client model
[2139.44 → 2146.36] of network applications it was very common in say the 1980s before the web came along so he wrote this
[2146.36 → 2152.30] dissertation to contrast how's this web thing different from that and the term that he came up with
[2152.30 → 2158.14] to describe the web was rest representation state transfer as a network architecture as a system
[2158.14 → 2166.50] architecture and uh it's unfortunately a pretty academic language but the crux uh rest in my opinion
[2166.50 → 2171.90] is this he defined it in terms of constraints, but the crux was this thing called the uniform interface
[2171.90 → 2179.06] and boy how can I summarize this in a layman's term as quickly as I can but the core idea and what's
[2179.06 → 2184.38] interesting about HTML is when you get a HTML document from a server you have no idea what the
[2184.38 → 2189.68] content is going to say in it is could have links it could have a form that does some action
[2189.68 → 2195.58] whatever the browser when it asks for a particular URL doesn't have any idea what content is going to
[2195.58 → 2201.94] come back in that URL it just knows it's going to be HTML so it's going to render that HTML and let the
[2201.94 → 2208.32] user select from the hypermedia controls that are on the page and so there's this fascinating
[2208.32 → 2214.86] aspect of hypermedia where you stream down not just the data but also the operations on the data
[2214.86 → 2222.02] together comes down in one sort of complete package and by doing that then the user can see oh here's a
[2222.02 → 2226.82] new action or here's I want to delete this thing or I want to update it or whatever, but the user selects
[2226.82 → 2234.04] the actions from the hypermedia and that's in contrast with Jason so Jason typically you would get
[2234.04 → 2239.56] down just sort of the raw information about say a contact or a bank account a client-side template
[2239.56 → 2245.88] would be responsible for turning that into an UI and the clients I would have to know okay for updating
[2245.88 → 2252.28] customers i I need to issue a post to this URL it would all be encoded in your application code
[2252.28 → 2260.04] and so that's the big distinction between Jason like a Jason style data API and a hypermedia
[2260.04 → 2266.04] response that you would get in a hypermedia system, and it's ironic the reason we've been saying sort
[2266.04 → 2272.64] of rest in quotes when we're talking about Jason is that these days people would describe the Jason API
[2272.64 → 2277.96] as restful they probably wouldn't even describe the hypermedia API as an API they would just say
[2277.96 → 2283.26] that's just a web page what are you talking about that's not an API that's unfortunate, but that's just
[2283.26 → 2289.28] the way the industry has gone there's a long story behind that there's an essay up on the HTML website
[2289.28 → 2295.92] on the htmx.org slash essays page called how did rest come to mean the opposite of rest
[2295.92 → 2301.04] that you can read which sort of like goes into the detail the gory details of how that happened
[2301.04 → 2307.28] technically, but that's the big idea so that's what a hypermedia is it's media that has hypermedia
[2307.28 → 2314.28] controls inside of it typically links and forms and HTML and then a restful system a restful system
[2314.28 → 2320.16] architecture is something that has a bunch of constraints on it one of which is it using a hypermedia
[2320.16 → 2327.38] for server communication so as a go developer in practice what that really means is that rather than
[2327.38 → 2334.00] creating some Jason data API with some data in it and then tossing it over the wall to the front end
[2334.00 → 2338.72] friends who then have to know that oh if is this field has this particular flag that means you should
[2338.72 → 2345.28] show this or if it has this flag you should show this instead you're now in control of this and you
[2345.28 → 2352.16] present the controls by in practice doing again all the way back to the late 90s your web server
[2352.16 → 2358.10] returns HTML yep, and we let the browser take care of showing those controls that's right because I think
[2358.10 → 2362.92] a big downside of the fat client approach is like yeah you have to put these rules on the client
[2362.92 → 2367.28] but quite often you have to put it in the server as well just in case someone just tries to if there's
[2367.28 → 2372.64] some shenanigans right like if i I know if I have a bank account thing that has like a zero balance
[2372.64 → 2378.92] I may not show a withdrawal button right but I need to have that logic sealed up in the server and in
[2378.92 → 2384.18] the client yeah so yeah that's an excellent point you do have to have that logic on both sides of the
[2384.18 → 2389.42] wire and that's there's a technical reason for that the browser is not a trusted execution environment
[2389.42 → 2396.38] right it's open you just have no guarantees about it and so any computation that you do on the
[2396.38 → 2402.48] client side has to be redone and re-verified on the server side and so if you've got a bunch of
[2402.48 → 2406.72] front-end JavaScript logic again there's that pressure well I'm going to rewrite all that logic
[2406.72 → 2411.94] and go ah no I don't want to do that so maybe we'll just fine we'll just bite the bullet, and we'll use
[2411.94 → 2417.02] node on the back end too and as go developers you probably don't want to hear that as a ruby
[2417.02 → 2421.60] developer I didn't want to hear it so that's a reason why a hypermedia based approach
[2421.60 → 2428.12] is helpful because all you move all your logic onto the back end, and you exchange hypermedia
[2428.12 → 2434.60] with the server it is ironic and i again you know you keep saying this but if you've built just a web
[2434.60 → 2441.30] app with just HTML documents you've built a more restful system than the vast majority of Jason API
[2441.30 → 2446.86] developers have because you're using an actual hypermedia and so you actually do satisfy the
[2446.86 → 2451.94] constraints that Roy fielding laid out in his dissertation so just using HTML is all it takes
[2451.94 → 2457.52] once you do that you don't have to like worry about levels of Richardson maturity or any of that
[2457.52 → 2462.82] whatever all that crazy stuff was you just build an app using HTML, and it's going to be a restful
[2462.82 → 2467.90] system by its nature I do think it's worth noting that like I don't think it's the worst thing in the
[2467.90 → 2472.34] world like the way rest is used now I think it's not terrible to use it in that other way just
[2472.34 → 2477.04] because it's kind of become synonymous with that across the entire web industry so like I know I'm
[2477.04 → 2481.00] guilty of this like I teach programming type stuff and sometimes I'll use it in that way because i
[2481.00 → 2486.16] know that's what they're going to run into even if it's not technically accurate so it's kind of i am
[2486.16 → 2491.54] pretty cautious in the sense that I'm like there's no like this is the correct definition of restful
[2491.54 → 2494.48] based on like at least based on like what they're going to read on the web they're going to see like
[2494.48 → 2500.06] 100 different answers so I think a lot of people are used to this idea of like rest is sort of
[2500.06 → 2505.10] resource oriented endpoints and like you're using http methods that are associated with that
[2505.10 → 2509.88] and I think understanding this is a good thing but I do agree with you that it is kind of
[2509.88 → 2515.84] disappointing that people act like they're being restful fanatics when in reality they're like so
[2515.84 → 2520.48] far like it's diverged and evolved so much at this point that it's like yeah kind of weird place to
[2520.48 → 2526.96] be in or to get like really hung up in it, I guess yeah I don't I would recommend no listeners get hung
[2526.96 → 2532.58] up on if it is hilarious at this point and that's the way to treat it like the situation is
[2532.58 → 2538.60] hopeless, but it's not serious you know it's just like it's perfect to waste like a good hour
[2538.60 → 2543.28] half an hour at work oh yeah just to argue about what rest is if you're looking for somebody doing a
[2543.28 → 2550.26] room yeah keep it in your back pocket for that annoying engineer oh no that's not rest Carsten you
[2550.26 → 2554.52] mentioned it's a really sparks of thoughts that what we're dealing here when we said hypermedia
[2554.52 → 2559.50] is there's something that contains the data and also its behaviour at the same time well this is
[2559.50 → 2562.70] you should be ringing bells in almost every developer's head this is what we're talking
[2562.70 → 2567.94] about as objects almost in terms of traditional classical object-oriented programming yeah these two
[2567.94 → 2572.88] disciplines if you like having hypermedia and having objects do they suit each other quite well
[2572.88 → 2578.28] I think that they have a lot of they share a lot of characteristics it's hard because when you talk
[2578.28 → 2584.84] about a hypermedia system the client is the browser, and so we have web browsers now which are these
[2584.84 → 2590.56] incredible pieces of software and have all this incredible technology baked into them to make hypermedia
[2590.56 → 2595.12] work and the crazy thing about a browser if you take a step back and think about it for a second
[2595.12 → 2603.28] is that you can use this one piece of software this one network client to talk to a bank a pet food store
[2603.28 → 2610.42] a car automobile dealer a calendar an email client like you're an email so you can talk to anything
[2610.42 → 2617.50] anything at all what that shows is the power of hypermedia now it became so powerful that people
[2617.50 → 2623.46] actually started using it as just like a VM for almost thick client style applications which is what
[2623.46 → 2630.22] the spa world really sort of became I think, so its power was almost it was so powerful it almost undid
[2630.22 → 2634.64] the advantages of hypermedia or maybe transcended depending on how you want to think about it
[2634.64 → 2641.26] but early on in particular when browsers first came out this idea of like one universal network
[2641.26 → 2648.74] client that can talk to any application over this crazy hypermedia technology was really, really novel
[2648.74 → 2652.88] and it still is I mean you know again I think if you just take a step back and think about that
[2652.88 → 2657.26] that's unique if you told someone in 1980 you know what you're going to be using the same piece
[2657.26 → 2664.62] software to access your news your bank your calendar this stuff called email and all this stuff they
[2664.62 → 2667.38] would have looked at your cross hide they wouldn't have known what you were talking about unless they
[2667.38 → 2671.40] happened to be in one of the small research groups that was looking into this sort of stuff
[2671.40 → 2677.56] so it does have a lot of overlap conceptually I think with object-oriented programming, and it has a lot
[2677.56 → 2683.52] of flexibility that comes along with that style data hiding all that sort of stuff it just it's a really
[2683.52 → 2688.72] interesting technology I certainly didn't appreciate it when I first was doing web development to be
[2688.72 → 2692.76] honest I didn't really appreciate it until I built intercooler i just kind of made intercooler because
[2692.76 → 2697.66] I wanted to do I just didn't want to deal with JavaScript, but it was as i when I put it out there
[2697.66 → 2702.00] as an open source project some people who understood hypermedia a lot better than I did started saying
[2702.00 → 2707.68] hey this is really neat because this is still restful, but you're getting more interactivity out of HTML that's
[2707.68 → 2713.18] really cool and then that sort of sent you know i kind of given up on rest at that point because
[2713.18 → 2719.24] like a lot of people I was pretty alienated by the rest purity spirals that you saw online in like the
[2719.24 → 2725.24] mid-2000s, but you know when people started telling me hey this is very restful I went back and looked
[2725.24 → 2731.88] at the concept and finally understood it and uh appreciated the web platform a lot more once I did
[2731.88 → 2737.48] so we've talked about how HTML is kind of allows us to do something similar to what you do with react but
[2737.48 → 2742.24] you know using this traditional HTML and actually having full control over the whole thing are there
[2742.24 → 2746.82] any downsides to this approach versus you know any of the other approaches out there or just downsides
[2746.82 → 2754.24] in general yeah so again I'm I'm going to just point people to the essays page on HTML I have an essay
[2754.24 → 2760.26] on when to pick hypermedia and when to not when to use it when to not use it and the hypermedia approach
[2760.26 → 2767.24] is great in situations when you want to minimize complexity it's a simpler model than managing a
[2767.24 → 2772.18] bunch of complex front-end and back-end state have to synchronize one another, and you can actually
[2772.18 → 2777.88] accomplish quite a bit with it, you go to htmx.org slash examples you'll there are a bunch of examples
[2777.88 → 2782.34] of user interfaces built with that technology and some of them are probably going to be richer than
[2782.34 → 2788.96] your listeners probably expect, but there are times when a hypermedia approach isn't going to work well
[2788.96 → 2794.92] and so the classic example that I give is something like google sheets where when you have a Google sheet
[2794.92 → 2799.12] in front of you, and you've got a cell here and updating that can have this cascading effect
[2799.12 → 2805.84] across the entire UI that is something that is not going to be very amenable to a hypermedia exchange
[2805.84 → 2811.78] where you make a big server side call re-render on the clients or on the server side and then
[2811.78 → 2819.28] stream the updated UI state back to the front end so if you have a highly dependent UI where the UI
[2819.28 → 2826.48] dependencies aren't sort of enclosed in a natural hierarchy of elements on a screen then HTML isn't
[2826.48 → 2831.84] going to be a good approach if you have a really modal like if you have a lot of like modal state
[2831.84 → 2837.72] the web isn't really a state you know one of the characteristics of restful systems that
[2837.72 → 2843.38] where fielding pointed out was statelessness they're supposed to be stateless even cookies really if you
[2843.38 → 2848.84] read about if you have a purist take on his dissertation shouldn't be allowed or not cookies
[2848.84 → 2855.44] but sessions excuse me sessions stored on the server side but if you have a lot of front end state that
[2855.44 → 2860.58] you're really attached to like I really want to do this update with a modal and a modal on top of a modal
[2860.58 → 2866.32] and then just you know it's modals all the way down that kind of UI isn't going to necessarily play
[2866.32 → 2872.16] particularly well with a hypermedia approach it's doable but as you start getting more sophisticated
[2872.16 → 2877.42] with hypermedia you'll, you'll probably end up using events a lot to make those UIs work properly
[2877.42 → 2882.80] and that's a more complicated solution so that those I think are the big ones to think about than
[2882.80 → 2889.24] on the practical side when I wouldn't use the hypermedia approach is when your business just won't allow
[2889.24 → 2896.76] you to do it the reality is that react is the standard today and as much as I like HTML you know
[2896.76 → 2901.80] if someone would come to me and say hey I don't know anything about programming and I want a front end job
[2901.80 → 2906.86] what should I learn I'm going to tell them learn to react because if you go to you know indeed.com and
[2906.86 → 2912.64] do a search for reacting there's going to be 30 000 jobs in your local area if you do a search for HTML
[2912.64 → 2919.30] there's going to be zero jobs so I think there's a practical reason to consider you know we're all
[2919.30 → 2924.42] developers we all have careers that we have to consider as well and so uh from that perspective
[2924.42 → 2928.08] I think react is certainly a much safer bet than something like HTML
[2928.08 → 2954.68] js party is a weekly celebration of JavaScript and the web, so fun is at the heart of every episode
[2954.68 → 2961.36] we play games like front end feud i have to go with the big o opera I know it's a wild card but i just
[2961.36 → 2971.18] feel like it might be hanging on show me opera oh three strikes, and you're out discuss and analyze
[2971.18 → 2976.72] the news in the immediate term I'm really excited about those hyper developer productivity tools like
[2976.72 → 2982.32] copilot that just automate the boring stuff for you explain technical concepts to each other like
[2982.32 → 2989.50] were five did that make sense yeah man no magical sawdust muffin fairies, so your muffin is your
[2989.50 → 2994.40] function or variable yeah your muffin started down in the sawdust because you defined it later
[2994.40 → 3000.90] yeah you defined it down there, but actually it got hoisted up sure okay I did my best debate hot topics
[3000.90 → 3006.00] like should websites work without JavaScript I'm going to appeal to authority and read some quotes at this
[3006.00 → 3013.18] time okay I've lost complete control of this panel go ahead okay the first book no code is faster
[3013.18 → 3020.56] than code interview amazing devs like rich Harris uncraving and many more CSS is one of those languages
[3020.56 → 3026.28] that is very easy to pick up quickly and learn things like how to change a text colour, but it is very
[3026.28 → 3032.12] tricky to master this is JS party listen and subscribe today we'd love to have you with us
[3032.12 → 3039.98] so I guess next I wanted to talk a little bit about somebody who wants to get into using HTML and
[3039.98 → 3045.30] we're assuming our listeners are go developers so what are some tips for sort of going about and trying
[3045.30 → 3052.06] it out any advice I guess yeah so uh HTML is going to play really well with go and just the templates
[3052.06 → 3056.14] that are available and go out of the box there is I should have written it down before and there is
[3056.14 → 3063.62] someone who did a go web framework oh boy I'm blanking on it right now that has HTML baked into
[3063.62 → 3069.16] it I'll have to dig that up and send it along afterwards but the nice thing about HTML is that
[3069.16 → 3075.18] because it's using hypermedia you're going to be able to do your work mainly in go depending on how
[3075.18 → 3078.92] sophisticated you are you may have to write some front end scripting, but you're going to be able to
[3078.92 → 3085.34] primarily focus your logic on the back end go and I think that probably the best thing to do if you
[3085.34 → 3091.84] wanted to play around with HTML is gone and look at the examples htmx.org slash examples and just
[3091.84 → 3096.78] re-implement them in go using go as the server side for them, and they're pretty straightforward
[3096.78 → 3102.44] and so I think that you can grab those and re-implement them in an afternoon and get pretty
[3102.44 → 3108.32] proficient with HTML pretty quickly yeah again the idea with HTML is you're just going to annotate
[3108.32 → 3116.26] your HTML and so like if you were is you wanted to do autocomplete for a text box for example
[3116.26 → 3122.20] then you're going to end up putting two or three attributes on that text box saying when someone
[3122.20 → 3128.92] had when a key up occurs effectively I want you to issue a get to this URL and then take the results
[3128.92 → 3136.44] and jam that into this DIV down below, and you would do that by ID use the ID of the DIV down below use a
[3136.44 → 3141.16] CSS selector for that so that would be like say three or four maybe attributes that you would
[3141.16 → 3146.64] have to put on an input, and you could have it suddenly issuing an http request which you could
[3146.64 → 3152.80] catch and go and return a table of results that match that, and it'll all start sort of magically
[3152.80 → 3158.16] working so HTML really builds on you do have to know HTML a little bit so that's another thing I would
[3158.16 → 3164.36] say to maybe go developers is picked up some base HTML knowledge but once you have that you should be able
[3164.36 → 3168.68] to get stuff done pretty quickly has anyone tried picking it up and just playing around with it, I'd
[3168.68 → 3174.82] be curious what your impression was yeah, yeah so um before Christmas I just decided to give it a go
[3174.82 → 3180.00] on a Saturday morning make a to-do app you know not the most revolutionary thing in the world but
[3180.00 → 3186.40] I had something that you could look at it and think it was a spa you know in terms of like there was no
[3186.40 → 3191.70] page reloads I had drag and drop I could add things remove things delete things I had search
[3191.70 → 3196.46] honestly I did in a couple of hours I do think the examples on the AMX website are excellent
[3196.46 → 3202.74] they really do kind of give you a kind of it's almost like a menu of just common stuff that you
[3202.74 → 3209.86] have to do on a website like edit in place reorder things so it really is excellent and I think for me
[3209.86 → 3216.38] the other thing to bear in mind is that whilst the net complexity is reduced with this approach at least
[3216.38 → 3222.46] in a lot of cases you are going from a sort of thinnish server to a slightly fatter server
[3222.46 → 3228.50] so your go web server is going to be doing more so you need to think about the way you kind of
[3228.50 → 3233.90] structure your code you need to make sure you keep your controllers really skinny don't have too much
[3233.90 → 3239.94] business logic leaking in I definitely spend some time having a look at the go standard library HTML
[3239.94 → 3246.94] template package documentation because again it's got really simple examples as a how to generate HTML
[3246.94 → 3251.14] on the server and once you get familiar with that honestly you can drive out some really rich looking
[3251.14 → 3257.58] applications very quickly it's really satisfying it just feels like so much friction suddenly disappeared
[3257.58 → 3263.14] and I can just get stuff done yeah I second all of that I actually took a old-fashioned
[3263.14 → 3268.12] service I've rendered out because I've been I like building to-do applications in as many different
[3268.12 → 3275.26] languages as possible and uh I took that and tried to homily it basically I tried to add HTML to the
[3275.26 → 3280.58] roots of it, and again it was just a very simple experience you know the emulating stuff was already
[3280.58 → 3286.02] there it was already all in go, but it was just very smooth yeah what I found very interesting about
[3286.02 → 3293.52] doing it was it further improved the application structure it necessitated improvements in the way it
[3293.52 → 3300.10] was structured because much as when bill Kennedy was like building his little CLI app to basically drive
[3300.10 → 3305.52] out what he felt were behavioural problems or data issues with the back end he built for the front end
[3305.52 → 3310.68] by dwelling more in the front end by working there you start building a better back end as well
[3310.68 → 3317.10] things start getting cleaner more obvious more usable because they're getting used in the front so yeah
[3317.10 → 3323.80] it's a delight is what I would say good I actually find myself grinning and quite happy when the thing
[3323.80 → 3328.36] that you think is going to work you think oh yeah that should be something like that oh it just does
[3328.36 → 3336.04] it just works never has that happened to me with react yeah I was going to say that this whole episode
[3336.04 → 3340.24] felt quite sort of theoretical in a lot of ways but I think it's really important to say that like
[3340.24 → 3345.90] it's so much fun honestly I find it a lot of fun working with HTML, and it's just it feels like a
[3345.90 → 3349.66] weight off my shoulders I feel like I'm going to be productive but yeah it's honestly it's fun yeah
[3349.66 → 3354.34] I'd really recommend anyone just to give it a go it's a different way of thinking hypermedia is a
[3354.34 → 3360.60] different mindset and there's a there's almost a leglike satisfaction when things snap together
[3360.60 → 3366.54] right with it that I find that just doesn't come up with other approaches to building web apps for
[3366.54 → 3370.96] whatever reason I'm obviously partial towards it but I agree with that and one thing you know one
[3370.96 → 3375.74] thing I do want to say Dave about what you were mentioning where the front end can improve the
[3375.74 → 3381.96] back end code is that one of the strengths of hypermedia is that because you're streaming down
[3381.96 → 3388.02] the data and the actions associated with the data you can actually be much more dramatic in your
[3388.02 → 3395.08] restructuring of your application you can change the URL layout of your application very dramatically if
[3395.08 → 3399.00] you're building hypermedia based application which is not the case obviously with a Jason based
[3399.00 → 3404.40] application with Jason based APIs you have to version it you have to be very stable and all that
[3404.40 → 3411.06] one of the strengths of hypermedia is that it is very flexible because the actions are coming down
[3411.06 → 3416.14] with the data that they operate on if you decide that an action no longer exists or there's some
[3416.14 → 3421.46] other condition or whatever it is you can completely change things around and completely change you're the
[3421.46 → 3426.52] way your back end generates the HTML and the front end client that you know the browser doesn't care
[3426.52 → 3431.36] it just renders the HTML so it gives you this flexibility that you don't have if you adopt a
[3431.36 → 3437.48] Jason API unless it's not a public Jason API, so the hypermedia approach really is very flexible
[3437.48 → 3444.26] that's a big advantage of it that was pointed out by fielding in his dissertation okay I think that
[3444.26 → 3450.54] wraps it up for the HTML discussion we do have time to do unpopular opinions though so are you guys up
[3450.54 → 3454.10] for that oh yeah I've got a fun one heck yeah okay
[3454.10 → 3477.00] okay so who wants to kick us off with an unpopular opinion oh go on then everybody was really eager
[3477.00 → 3481.70] until I played the theme song and then everybody went silent no, no i I want Chris to go first because
[3481.70 → 3487.36] I think uh I think his will be well no I'll do mine first then because I like going first okay so mine
[3487.36 → 3491.68] isn't so much an opinion as a conspiracy theory which I'd like to inflict upon everybody since it
[3491.68 → 3499.56] infected my brain a few years ago and I call this the spa conspiracy the idea is this that the reason
[3499.56 → 3506.84] that all a front-end development has moved over to fit clients JavaScript applications is to make
[3506.84 → 3513.48] sure that we always have to have JavaScript enabled in our browsers which enable make sure that the large
[3513.48 → 3520.10] corporations who are I should point out the developers of the single page apps so they can
[3520.10 → 3526.46] track us yeah so basically google made angular in order to make sure we turn on JS in order to make
[3526.46 → 3532.66] sure google tracking cookies could execute properly same for Facebook you might notice that many of the
[3532.66 → 3539.36] other frameworks I think of svelte here is also regional design was to visual advertising so make
[3539.36 → 3544.78] sure which also requires JavaScript to run so there you go there's my unpopular opinion the entirety of
[3544.78 → 3550.58] the last 10 years of front-end frameworks is all there to make sure that google can follow you on the
[3550.58 → 3556.42] web I mean I don't really believe it but you kind of do yeah maybe i kind of do
[3556.42 → 3563.26] there's some kind of do there's plausible deniability right you have to stand by it Dave like you turn
[3563.26 → 3568.62] JavaScript on you said we could yeah you said we could follow us now because you wanted more
[3568.62 → 3573.48] JavaScript, and we are now at a point where the web is essentially unusable unless you turn on JavaScript
[3573.48 → 3581.88] so it worked yep so the only thing that would like possibly debunk this is that I believe remix is
[3581.88 → 3586.96] supposed to be designed so that it mostly works without JavaScript still I don't know if you looked
[3586.96 → 3592.74] at it remix. Run I think is the website but uh it's like a JavaScript front end that a lot of their like
[3592.74 → 3599.02] goals were to make it so that like core normal HTML type things all work and that company was started by
[3599.02 → 3603.84] like a smaller group of developers, but it was bought by I think who bought it was it Shopify yeah
[3603.84 → 3608.66] man somebody acquired them so I'm curious to see if that's one of those companies that uh
[3608.66 → 3614.68] goes away from that goal remix is interesting it's a fascinating idea I do have to say it is a little
[3614.68 → 3622.38] confusing how HTML has made, so little progress in the last 20 years like why hasn't HTML gotten any
[3622.38 → 3629.44] better as a hypermedia it's obviously gotten you know new widgets and canvas new APIs in JavaScript
[3629.44 → 3636.02] but as a hypermedia it's been pretty frozen in time now since you know html2 so it's easy to
[3636.02 → 3641.46] develop a conspiratorial angle on the thing for sure there was a time when it was I think it was
[3641.46 → 3646.42] apple that wanted to sort of like HTML was the future for apps like that's kind of how they were
[3646.42 → 3651.82] and I think if that had actually been the future like that it panned out that way I think it would
[3651.82 → 3658.42] have developed a lot more but I think in reality like for whatever reason apps with proprietary
[3658.42 → 3662.54] programming languages is basically what ended up being the case, and now we're coming to the
[3662.54 → 3667.42] realization that oh HTML actually is strong enough now to like actually build a lot of apps so we've
[3667.42 → 3672.34] kind of come full circle so maybe it'll start to get developed again but who knows I was going to say
[3672.34 → 3679.38] that all http HTML doesn't even meet http right you can't even use I'd say the vast majority of the
[3679.38 → 3685.50] HTP verbs in HTML right so you know it doesn't even meet the hypermedia you know the hypertext transfer
[3685.50 → 3690.66] protocol all it's missing is like components and being able to do the rest of those methods and
[3690.66 → 3695.28] maybe a few bits and pieces here and there which HTML is cover, and you know I find it weird that
[3695.28 → 3701.16] it got stunted like that it's just weird I would love it if HTML the functionality or at least the
[3701.16 → 3708.32] concepts of HTML were folded into the browser into the HTML spec because you know just to me that makes
[3708.32 → 3713.32] it makes sense you just want a more powerful hypermedia you want the ability to have more than just
[3713.32 → 3720.22] links and forms that do stuff and more than just clicks and submits to trigger them events wise and
[3720.22 → 3726.54] then like you said you should be able to issue put and delete and patch and all that stuff as well from
[3726.54 → 3732.12] HTML why can't you do that and then the last thing is taken the response and stick it into something else
[3732.12 → 3738.10] in the page instead of this big refresh you know I think you know they could do that in one release
[3738.10 → 3745.74] pretty easily and uh it would make HTML a much more powerful development tool and HTML could go
[3745.74 → 3751.98] away and I could relax a little bit more it is always weird to me though that like especially it's
[3751.98 → 3756.30] like somebody who's teaching other people you go teach about all these http methods and then when
[3756.30 → 3760.22] you're showing them HTML you're like by the way none of these work so you just have to post everything
[3760.22 → 3765.50] and just make different endpoints for it doesn't make any sense so it's like it's kind of frustrating
[3765.50 → 3769.86] in that sense it's like why'd you teach me this well you should know it, but you aren't going to
[3769.86 → 3774.04] use it right now I'm introducing you to the disappointment that comes with web development
[3774.04 → 3781.62] this is your introduction to the psychological beatings you're going to take for the next 20 years
[3781.62 → 3786.82] what you get excited about what could be and then somebody yanks it away I still remember feeling about
[3786.82 → 3791.36] that about form posts are still like this is like eight years ago seeing it as it's like what
[3791.36 → 3796.78] still bugs me well the worst part is you'll see forms that have method equals post, and you're like
[3796.78 → 3801.38] oh I can change that yeah it's like no you can change it again it does two things what
[3801.38 → 3813.22] oh god Chris what is your unpopular opinion all right I believe the earth is flat no uh no more
[3813.22 → 3818.50] conspiracy theories so imagine you start a new project with uh I don't know half a dozen developers
[3818.50 → 3825.88] and the first thing you do is you write 10 go interfaces describing the lumps of code that you
[3825.88 → 3830.70] think you're going to need to solve this problem, and then you divide them up between everyone and say
[3830.70 → 3835.38] you know go implement those interfaces, and we'll stick everything together in a few weeks time
[3835.38 → 3841.86] you'd probably rightly question my judgment with this approach because surely this is premature
[3841.86 → 3847.36] abstraction like how do I know that the design is correct how we know these interfaces are what we need
[3847.36 → 3853.82] and is it not risky for us to work so independently at first we're not going to go into integration hell
[3853.82 → 3858.84] and yet there are loads of teams out there who will start a project with microservices
[3858.84 → 3864.88] and that is just like what I just described, but it's even worse because the distributed system on top of
[3864.88 → 3869.38] all of these assumptions that you're making so whatever mistakes you've made in your design
[3869.38 → 3873.74] are so much harder to fix than if it was just in a single code base
[3873.74 → 3879.14] and my unpopular opinion maybe it's not unpopular I don't know but I believe in a vast majority of
[3879.14 → 3885.00] cases you should start rather than starting a project by drawing on a whiteboard 100 microservices
[3885.00 → 3890.70] just start with a monolith just start with like one code base because if you make mistakes in your
[3890.70 → 3896.60] assumptions it's so much easier to fix within a single code base than if you've just scattered it into a
[3896.60 → 3901.90] million services and if you can write a good monolith then you'll be able to break it out into
[3901.90 → 3907.78] separate distributed services when you actually need to distribute this work and I guess my second
[3907.78 → 3911.32] unpopular opinion on top of it which is kind of the same is as if you can't write a good monolith
[3911.32 → 3917.66] you're going to write a dreadful microservice architecture to me the skill it's the same skill
[3917.66 → 3921.82] set to do both so if you can't do a good model if you can't do good microservices in my view
[3921.82 → 3926.52] so what would the counterargument to that be like are people just imagining that they can just
[3926.52 → 3932.64] have a hideous microservice because it's small like they don't need to design that code well I don't
[3932.64 → 3938.54] I'm asking like have you talked to others about it the counterargument that I hear online is that
[3938.54 → 3946.40] microservices don't solve a technical problem they solve an organizational problem, and so they allow a
[3946.40 → 3954.30] particular unit within a business to deploy sort of independently I don't buy that argument, but that's
[3954.30 → 3960.68] what I hear uh when people defend the microservice architecture I like Chris, and it sounds like
[3960.68 → 3968.62] everyone here i I am not a huge fan of microservices so I'm on your side in this unpopular opinion well to
[3968.62 → 3973.22] be fair I'm not against microservices I'm just against microservices at a start of a project
[3973.22 → 3980.08] and I do kind of buy the kind of organizational sort of aid if you like I guess the thing is I've worked
[3980.08 → 3986.78] in enough organizations where we've organized ourselves terribly and Conway's law is just like
[3986.78 → 3991.42] hurting us so much because our organization dictates our architecture and our architecture is garbage
[3991.42 → 3996.90] and to me like when you start with microservices what you're kind of doing is you're saying we
[3996.90 → 4001.72] understand how we need to organize ourselves before we've written any code and to me that strikes me as
[4001.72 → 4007.50] a very kind of waterfall style thinking of we can just design everything perfectly and then just do it
[4007.50 → 4012.82] and we'll execute brilliantly but in practice most of the time when you're building something you don't
[4012.82 → 4016.96] know enough about it at first you need to live in the domain a bit and write some code and iterate
[4016.96 → 4020.92] on it and feel what it feels like and then start to understand what the problem is a bit better
[4020.92 → 4026.38] then you can start doing your fun design stuff if anybody's interested in the whole microservices as
[4026.38 → 4031.54] organizational tool my colleague at my current business salt pay we are hiring
[4031.54 → 4037.32] sure we got a bonus for that Adam he gave a fantastic talk at gopher con London earlier this year
[4037.32 → 4042.12] about how that works I'll see if I can find the link for that, but it was uh it was really
[4042.12 → 4047.56] wild i sort of disagree, but his argument was really convincing that by using microservices you
[4047.56 → 4053.14] actually force an organization to talk to each other properly rather than that it drives communication
[4053.14 → 4058.40] basically failures to integrate your microservices properly that the difficulty of communication across
[4058.40 → 4063.10] the network boundaries are only really solved by having a good social communication between the
[4063.10 → 4069.28] teams and the rest of the organization, so yeah makes you address those social problems rather than
[4069.28 → 4077.52] hide them away in a monolith maybe it's hard for me to give like real good feedback on this I guess
[4077.52 → 4082.94] because like I've been self-employed or working with teams less than five people for like the last
[4082.94 → 4088.10] decade so I haven't worked on a large team with like microservices and I've been lucky enough to be in
[4088.10 → 4092.36] these small teams where like we have a monolith glorious, and it's real fast like sounds fantastic
[4092.36 → 4096.86] like yeah we can iterate quickly and everybody's good with it and like that's great so like when
[4096.86 → 4101.00] I hear about a microservices structure I'm just like yeah I don't need that and I really don't want
[4101.00 → 4105.16] to mess with it when I don't need it for sure but I mean that's also because I know anytime you try
[4105.16 → 4109.38] something new I'm bound to make mistakes so like I know if I went and designed something with
[4109.38 → 4114.14] microservices right now it would not be that good I could probably jump into a code base with it and help
[4114.14 → 4117.24] do some stuff but I don't think I would set it up correctly from the get-go
[4117.24 → 4122.74] Carson do you have an unpopular opinion you'd like to share oh well no I'm just right about
[4122.74 → 4130.08] everything so my unpopular opinion so I've got a web we can take a poll on that yeah yeah take a
[4130.08 → 4134.92] poll on uh twitter and see what the results are on that one it would not be good for me that's okay
[4134.92 → 4140.06] I say are you married I'm a contrarian because if so HTML may be just one long sorry I was gonna
[4140.06 → 4145.30] suggest that HTML might be just one really long unpopular opinion you know yeah that's true
[4145.30 → 4152.90] library yeah boy it's a target rich environment here but uh the one that I wanted to mention
[4152.90 → 4161.54] is I've got a website called grugbrain.dev which is a joke website of mine that's sort of like my
[4161.54 → 4170.32] experience in programming over the last 20 plus 26 seven years now and uh boy even longer than that
[4170.32 → 4178.96] but anyway one of the things that I mentioned in there is this idea of the fear of looking dumb
[4178.96 → 4188.50] and my unpopular opinion is that in technology a huge number of technical decisions are either made
[4188.50 → 4196.80] or not objected to out of a fear of looking dumb, so someone comes in with an architecture
[4196.80 → 4204.42] role decision or some code decision or whatever, and it's crazy you know and there's a bunch of
[4204.42 → 4211.00] engineers in there looking at it going man that looks crazy to me but if I say so I'm gonna look
[4211.00 → 4216.00] dumb I'm gonna look like I'm not smart enough to understand what they're doing, and so I'm gonna
[4216.00 → 4223.20] keep quiet about it and uh I think that that is a problem in general in technology, and it's
[4223.20 → 4228.08] understandable because it is a pretty brutal industry we rely on our intellect quite a bit
[4228.08 → 4233.68] and there's this you know there's ageism and if you come across as not being intelligent it can be
[4233.68 → 4239.64] really detrimental to your career but I think that unfortunately it uh ends up in a lot of situations
[4239.64 → 4245.62] leading to bad architectural outcomes and bad code outcomes because people are unwilling to say
[4245.62 → 4252.64] this is too crazy let's do it a simpler way if at all possible so that's that's my unpopular opinion
[4252.64 → 4258.84] don't you know the fear of looking dumb ends up driving a lot of technical decisions I like to
[4258.84 → 4265.12] think that I lead by example by constantly saying dumb things but seriously i I don't think that
[4265.12 → 4271.12] should be unpopular at all I think it's spot on I think it's so important for everyone to try and
[4271.12 → 4276.32] create this kind of safe environments where people are unafraid to speak their minds even if they
[4276.32 → 4281.08] think that what they're saying is dumb because quite often it isn't like I think a lot of the time
[4281.08 → 4285.82] my experience has been almost with like junior engineers like the ones who are so cool I don't
[4285.82 → 4291.24] have a have very little experience often ask questions that just make you look at it slightly
[4291.24 → 4295.20] differently, and you think to yourself oh, thank goodness this person was here asking that question
[4295.20 → 4300.40] yeah because if they hadn't, we would have gone down a horrible path yep do you think that um like
[4300.40 → 4304.42] turnover at companies contributes to that the fact that if you've been in a company for three years
[4304.42 → 4308.94] and you know your co-workers for that long I feel like it's easier to speak up oh yeah but when you're
[4308.94 → 4313.56] new to a team you definitely do not want to speak up and look like the weird idiot who just joined and
[4313.56 → 4318.00] doesn't know what he's doing I think this is one of the reasons why the prevailing kind of thought
[4318.00 → 4323.50] around sort of teams is that stable teams are really important, and you shouldn't like when we're talking
[4323.50 → 4328.26] about these big organizations I certainly don't subscribe to the view that we should view developers
[4328.26 → 4333.00] as this kind of interchangeable cogs that we can just like reconfigure teams on the fly and
[4333.00 → 4336.90] because i just completely forgets the social aspects of software engineering about the fact that
[4336.90 → 4342.36] it's valuable to have a really healthy and open working relationship with your colleagues but
[4342.36 → 4346.98] you don't get that for free like you can't just suddenly trust a new colleague that you've just
[4346.98 → 4352.62] met after a day it takes time and I feel very strongly about this sort of thing actually you know
[4352.62 → 4357.84] there's all these layoffs in tech right now and I guarantee you that's increasing the number of bad
[4357.84 → 4362.34] technical decisions that are allowed to slip through because everyone's keeping their head down
[4362.34 → 4370.26] and so some lunatic can come in just the dumbest idea or not the dumbest but a very complex solution
[4370.26 → 4374.26] and everyone's no one's going to say anything they just want to keep their heads down keep their job
[4374.26 → 4379.72] understandably and so if you're in a senior engineering position where you're safe where you
[4379.72 → 4384.44] know you're safe you have a lot of credibility in your organization I think it's very valuable to your
[4384.44 → 4390.34] organization to say things like man this seems really complicated or boy I don't understand that
[4390.34 → 4394.10] especially in front of younger developers and developers that aren't as comfortable
[4394.10 → 4401.14] because if you can use your social standing in your company to develop that lack of fear
[4401.14 → 4406.10] I think you're going to end up with better technical decisions being made as an organization
[4406.10 → 4412.32] absolutely I tell I try to leave my example on that front but also I tell every junior I've
[4412.32 → 4416.26] worked with their job is to ask questions you know their job isn't to write code they're not going to
[4416.26 → 4420.48] be amazing at it to begin with their job is to get better and so their job is to ask all the
[4420.48 → 4425.10] questions in every meeting ever what they don't understand why they think something is wrong why
[4425.10 → 4430.00] they think something is stupid because that's how they make everybody better just being on that
[4430.00 → 4435.38] on the ball on that stuff I love it I love being asked really difficult questions or really dumb
[4435.38 → 4442.04] questions because it makes me look dumb sometimes because I am dumb sometimes it's just good to go back to
[4442.04 → 4446.26] like the drawing board and think like why did I decide this and just to reiterate it and make
[4446.26 → 4451.12] sure something hasn't changed since you made that decision and Chris I completely agree with you with
[4451.12 → 4455.78] the like interchangeable part I think it's kind of nuts that like we instinctively know this with like
[4455.78 → 4459.34] a sports team you can't just take one player out and replace with another and expect the team to be
[4459.34 → 4465.76] just as good but like we expect it to work with software where like every decision builds more and more
[4465.76 → 4471.14] like technical debt and all this other stuff and having people you can work with and like understand how
[4471.14 → 4475.56] they're going to make decisions and different stuff can be really valuable but I guess that's
[4475.56 → 4479.58] probably part of the reason why I haven't worked for a big team in a long time I'm very spoiled in
[4479.58 → 4486.12] that sense okay I think that's it for this episode Carson thank you for joining us Chris and Dave how
[4486.12 → 4491.80] about you john do you have an unpopular no unpopular opinions today no have not even had time to think
[4491.80 → 4498.94] about unpopular opinions I'll let you guys take the limelight there sounds good all right I will play us out
[4498.94 → 4509.24] that is go time for this week thanks for listening if you dig the show share it with your friends and
[4509.24 → 4514.80] colleagues and if you get a lot of value out of it return some value with a changelog plus
[4514.80 → 4520.08] membership ditch the ads get closer to the metal with bonuses and extended episodes and directly
[4520.08 → 4527.00] support go times continued production learn more at changelog.com slash plus thanks once again to
[4527.00 → 4531.80] our friends at fast and fly for partnering with us to bring you go time check out what they're up
[4531.80 → 4538.80] to at fastly.com and fly.io and to our mysterious friend brake master cylinder for keeping our beat
[4538.80 → 4546.16] supply on and popping next time on go time Matt and johnny are joined by carl Johnson our what's new in
[4546.16 → 4553.58] go correspondent to discuss all the goodies in the recent go 1.20 release stay tuned for that I hear Matt
[4553.58 → 4559.26] even breaks out the guitar so you don't want to miss it we'll have that episode ready for you next week
[4559.26 → 4559.58] you
