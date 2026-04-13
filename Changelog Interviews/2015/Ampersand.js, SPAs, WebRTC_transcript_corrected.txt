[0.00 → 15.82] welcome back everyone this is the change log and I'm your host Adam stekowiak this is episode 160
[15.82 → 23.06] and on today's show it's all about JavaScript single page apps human ways of coding we're
[23.06 → 29.82] talking to Henrik cortège the author of a book called human JavaScript and also a non-framework
[29.82 → 35.24] framework framework for JavaScript called ampersands if you haven't heard of it you got
[35.24 → 40.88] to check it out we talked about that single page apps web RTC we even touched a little bit
[40.88 → 47.10] on http2 so you'll enjoy that piece there we have three awesome sponsors for this show
[47.10 → 54.22] code ship top tout and also dream host our first sponsor is code ship is a hosted
[54.22 → 59.40] continuous delivery service focusing on speed security and customizability for you and your
[59.40 → 65.28] team you can set up continuous integration in a matter of seconds and automatically deploy your
[65.28 → 71.24] code when your tests have passed code ship supports your GitHub and your Bitbucket projects, and you can
[71.24 → 76.14] get started today with code ship's free plan should you decide to go with a premium plan you can use
[76.14 → 83.14] our code to save 20 off any plan you choose for three months the code is the change law podcast again
[83.14 → 89.34] that will get you 20 off any plan you choose for three months head to code ship.com slash the
[89.34 → 91.82] change law to get started and now on to the show
[91.82 → 101.18] all right everybody we're back got a great show for you today one we've been planning on for a bit
[101.18 → 109.08] uh got Henrik cortège on the call today developer at and yet JavaScript well known speaking I mean
[109.08 → 114.62] you're you how many talks have you given this year alone oh sheesh uh I don't know this year's been
[114.62 → 119.66] kind of busy it's probably been four or five or something four or five and so you're sort of
[119.66 → 124.70] you got this one talk that you've been kind of doing a few times or is it several different talks
[124.70 → 129.72] you're doing uh it's a lot of the same messaging but I try to evolve it a little bit each time just
[129.72 → 134.24] because otherwise it gets boring and I get bored with giving it so right gotcha, and then you die
[134.24 → 140.40] and then I die yeah you die it's an inside joke from one of your talks but uh we got jarred on the
[140.40 → 146.46] line here as well jarred what's up buddy excited to talk some more JavaScript I know our loyal
[146.46 → 152.60] listeners love love love the JavaScript so here we are what is this JavaScript thing you speak of
[152.60 → 157.44] um good question it's its some interesting thing on the web I don't know we'll find out I guess
[157.44 → 162.60] all right well this is right up jarred's will camp or uh will house you know not so much that it's not
[162.60 → 170.10] mine, but you know jarred you're you went to NG cone not long ago um what other conferences have
[170.10 → 176.10] you have gone to recently that were around JavaScript uh space city JS with you in Houston that's true
[176.10 → 183.48] I'm also helping organize the Nebraska JS cone uh this summer as well speaking of conferences Henry
[183.48 → 188.50] you got a conference coming up yeah we're doing one called uh real-time cone uh it's one that we did
[188.50 → 194.40] a few years ago, and we took a little break, and we said we'd never do it again and uh we are so
[194.40 → 199.80] it's just kind of about like a lot of real-time web technologies and really kind of trying to be
[199.80 → 204.28] a little bit more uh thinking about what the web should be and what we should be working on rather
[204.28 → 209.20] than just the stuff that we could be doing so what made you change your mind you said you never do it
[209.20 → 216.46] again I'm gonna largely blame Adam bra ult for that uh but uh you know it's just it's just it was a good
[216.46 → 221.48] event we met a bunch of cool people and we just want to do it again so cool and when is that
[221.48 → 226.50] um it's coming up in the fall here i I'd have to put the exact date in the show notes I should
[226.50 → 231.48] I should know but I don't off the top of my head I just don't know from what I saw yeah it's October
[231.48 → 237.68] but we're selling huge tickets right now so uh first kind of batch of tickets is up right now so
[237.68 → 243.66] get a ticket oh that's it that's not that's a pricey ticket it is, but we do a bunch of
[243.66 → 248.22] really cool stuff so like we spend it all we're not trusted me we're not going to make money on this
[248.22 → 253.94] thing this is not a profit thing right yeah yeah it's uh community building just yeah just check
[253.94 → 259.22] out the one that we did last or the last one that we did, and you'll, you'll understand uh why we
[259.22 → 264.84] charge what we charge cool all right well let's do that we like uh we like going to conferences it's a
[264.84 → 272.60] lot of fun so aside from putting on this conference and speaking at conferences um you're also pretty
[272.60 → 280.38] well known for a book you wrote and uh ampersand JS and your work at and yet and some of the things
[280.38 → 285.92] you put out in the open source world where if is you were I guess on the change log stage and you
[285.92 → 290.06] were introducing yourself to an audience that some know you some don't know you how do you introduce
[290.06 → 295.64] yourself oh sheesh uh well so i I mean I'm a web developer right like I think that's kind of the
[295.64 → 301.08] most important thing uh but I use JavaScript to do so um I've been kind of lead JavaScript developer
[301.08 → 307.48] and yet for a while um and I just do a bunch of open source stuff I've got a few hundred open
[307.48 → 314.66] source modules and stuff and uh you know things like uh around web RTC but just a lot of kinds of
[314.66 → 319.12] thinking and talking around how to structure web applications in a way that doesn't like
[319.12 → 325.22] make an absolute mess of your code and so that other people can work on it etc I wrote a book called
[325.22 → 331.06] human JavaScript that kind of attempts to uh encapsulate some of that knowledge um and also
[331.06 → 335.98] kind of training and teaching around those kinds of things as well so I don't know that about sums
[335.98 → 345.50] it up yeah I think and yet you guys are perhaps most uh open source famous for ampersand JS um
[345.50 → 349.40] first is that true or do you guys have a bigger project that just hasn't hit my radar
[349.40 → 355.68] uh well we have one that uh we shared a while ago a while ago called simple web RTC uh that
[355.68 → 360.66] basically just takes um in terms of like number of stars on GitHub that's probably up there as well
[360.66 → 366.64] but okay um but yeah it just kind of makes web RTC something that an average web developer can do
[366.64 → 372.94] without having to like go study how this stuff works too much right so but yeah ampersand is
[372.94 → 378.16] definitely kind of our the thing that I think people have kind of seen the most of so you want
[378.16 → 383.56] to give us the elevator pitch yeah I mean if you take is you think about something like backbone like a lot
[383.56 → 388.36] of people like the patterns and backbone, but there's a lot that backbone doesn't do, and you know coming
[388.36 → 393.10] from kind of the node world we like to split everything up into small modules so what we did
[393.10 → 398.02] is we kind of started with backbone we used to build a bunch on backbone, and then we ended up kind
[398.02 → 402.66] of just forking and doing our own thing so we took uh you know each kind of component that you might
[402.66 → 408.14] have in backbone, and it's published then as its own module uh it's all written in common JS
[408.14 → 415.38] so you have to like to install it with NPM um but as a result you know you end up only kind of shipping
[415.38 → 420.92] what you actually need and people only grab and use the little portion of it that they want um you
[420.92 → 425.44] know we could have just done the whole thing as a bunch of completely separately named things but we
[425.44 → 430.08] just kind of called that ampersand to give it something to kind of wrap it all together I assume
[430.08 → 435.68] the other tie in there is the thing that sits in front of your business name yeah well we rather like
[435.68 → 444.58] the symbol there for some reason but uh it's a good tie and I like that yeah so what's ampersand's
[444.58 → 451.56] relationship to backbone is it inspired by is it a fork is it a rewrite is it the same thing it
[451.56 → 458.08] definitely shares some code uh we uh at first I was just kind of writing a replacement for the
[458.08 → 462.76] models because I wanted models that were a little bit more specific as to what they would contain
[462.76 → 468.80] um so you know unlike backbone models here you have to actually define what you're going to store in a
[468.80 → 474.00] given model you have to at least give it kind of name and a type and then that the idea is that
[474.00 → 478.18] someone else who's kind of new to a project can like jump in and read your models and actually make
[478.18 → 483.96] sense of what's being stored, and you know kind of the state that they have available um but other
[483.96 → 490.24] portions like the router for example are you know much closer to what backbone does, and you know a lot
[490.24 → 494.46] of code you know in some of those cases we know we left the license in because there's so much
[494.46 → 500.36] shared code right so it kind of varied depending on which component but uh definitely if you're kind
[500.36 → 506.56] of from the backbone world you'll feel kind of at home here so Adam and I were talking kind of
[506.56 → 512.84] pre-call about ampersand the modularity versus you know some of the other frameworks and backbone itself
[512.84 → 519.38] um who would you say ampersand is for is it for the beginner is it for the advanced person who
[519.38 → 524.10] is ready to pick and choose who's your core audience um it's definitely not as easy to pick
[524.10 → 528.96] up as something like angular you know I think people who have done this for a little while probably
[528.96 → 534.30] are going to understand it and understand this value a little bit easier um that's not to say
[534.30 → 539.68] though that you couldn't start with this um but I would tend to say you know for the most part
[539.68 → 545.56] it's people who kind of like the patterns in backbone, but they want the modularity and stuff that's
[545.56 → 552.68] that's such a big thing in the node community so um but yeah we the know my favourite thing is
[552.68 → 558.46] that the way people are using this is like they'll just grab various pieces like WhatsApp for example
[558.46 → 563.52] they use just ampersand state that's the only module of ours that they use, and they use React as a view
[563.52 → 568.52] layer and all that um, and then you get you know other companies that are just using like I know some
[568.52 → 575.06] folks at yahoo that only use the router like and to me that's a good like kind of pat on the back that
[575.06 → 579.86] we did something right because that's that's the whole idea it's like you don't have to go all in
[579.86 → 584.68] you can, you know here are a bunch of tools they work nicely together if you want them if you don't just
[584.68 → 590.40] you know pick and choose mix and match with whatever else you want right so react or ampersand
[590.40 → 596.10] view or some other way to do things in the front yeah I mean people have been doing it mixing it up
[596.10 → 601.90] with there's one called riot there's uh r active there's you know a bunch of these like kind
[601.90 → 606.80] of view layer things that I've seen people use ampersand with so the fact that you can kind of
[606.80 → 612.70] pick and choose is I would say one of its key features being so inspired by backbone would you
[612.70 → 616.62] say it's a prerequisite to have some working knowledge of backbone before you're productive
[616.62 → 622.56] or could you just start right in with ampersand I would hope not uh i you know it's possible that we
[622.56 → 626.30] need to do a better job of writing more intra-level guides, but we have some of that stuff on the site
[626.30 → 631.02] and it keeps getting better so um that's something that if you know is you're new, and you're just
[631.02 → 636.40] looking into it, and you're confused like file a bug we want to know because we want to make it more
[636.40 → 644.14] approachable for people who are new so we have to ask um you know every framework uh that
[644.14 → 650.62] comes on we tend to ask this, and it's kind of why why ampersand in light of not just in general but
[650.62 → 656.38] in light of your other options right because there's such a diverse landscape there's so many
[656.38 → 662.36] tools out there right now that it is commonly asked and talked about which one should I choose
[662.36 → 669.28] um so if you had to put it against an ember against an angular or a framework like Aurelia
[669.28 → 673.04] and you say well here's where ampersand really shines and then maybe here's where
[673.04 → 679.58] it's not a great pick could you do both of those um yeah I think so I mean in some ways i kind of hate
[679.58 → 684.92] pitching it or defending it at all because I want it to just kind of stand on its own and like I think
[684.92 → 690.52] the important thing is that people pick tools that that kind of fit how they want to work and that let
[690.52 → 695.88] them be productive uh if for some people that's that's something like angular then, then great if
[695.88 → 700.88] that's meeting all your needs then like stop don't need to you don't need to go replace it right
[700.88 → 706.92] um but I think you know where it does shine is kind of being able to handle and tolerate
[706.92 → 713.82] change over time um you don't have to go all in uh that's kind of you know someone referred to it as
[713.82 → 719.36] kind of fear of commitment framework and i honestly i kind of don't even really like calling
[719.36 → 725.12] it a framework at all uh and i I almost hate myself a little bit for having contributed to this
[725.12 → 730.66] whole kind of range of available options here but uh for us, it was just a matter of like hey here's
[730.66 → 735.36] the stuff that we're using this seems to work pretty well for us let's share it and see what
[735.36 → 740.92] happens, and you know come to find out other people seem to think the same so there are people
[740.92 → 746.82] that have kind of referred to it as an as kind of natural kind of backbone 2.0 sort of thing i
[746.82 → 754.52] wouldn't go that far but uh it's kind of a node flavoured backbone I guess we shared an article in uh
[754.52 → 759.18] we ship a weekly uh email every Saturday called change law weekly I don't know if you subscribe or not
[759.18 → 763.98] but in last I should, it sounds like yeah you definitely should, I don't know why you're not
[763.98 → 769.72] everybody should change law.com slash weekly go sign up for now we'll do um but one of the articles we
[769.72 → 774.18] we share was, and it was the most popular in this latest issue was did you pick the wrong web
[774.18 → 780.16] framework, and it had a question mark and a bang after just to put the extra oomph on the end there
[780.16 → 785.40] right and uh something that might tie into to how you think I think is one thing mentioned here was
[785.40 → 790.98] start with humans rather than saying you know which code base or which framework works best for us and
[790.98 → 795.38] start to start with the people that are actually using it and how the teams work together and how
[795.38 → 800.58] they're going to be using this project long term and think about it that way versus um versus the
[800.58 → 804.94] tech you know start with the humans and would you agree with that statement yeah for sure and I mean
[804.94 → 810.34] you know we do consulting and yet so we get you know we build apps for lots of different types
[810.34 → 815.26] of groups of people, and so we get this question a lot you know like how can I know which tools
[815.26 → 821.52] I'm supposed to use um and I would say the answer is you can't right like how can we predict
[821.52 → 827.44] the future um what we can do is pick tools that like leave us some flexibility and I would say that's
[827.44 → 833.18] kind of my biggest concern with uh some of these like more all-inclusive frameworks is it's
[833.18 → 839.16] you're kind of all in like in some ways and some people are going to hate me for this but in some
[839.16 → 845.10] ways like you know getting perfect at angular is I would think it's almost kind of
[845.10 → 849.70] like getting perfect at flash in some ways like you're kind of going all in on that technology
[849.70 → 856.08] and you're learning that technology uh almost more than you, you know are learning the problems that
[856.08 → 863.50] that that thing solves for you um I think his name is Chris gale his was the former vice president at
[863.50 → 868.58] yammer former vice president of engineering said you know I'm more interested in people's understanding
[868.58 → 874.12] of problems and solutions and I think that tends to be the case so we tend to want to kind of grab
[874.12 → 879.46] something off the shelf that just kind of solves our problems, but that doesn't leave us as prepared
[879.46 → 884.88] when we have to evolve it over time, or you know something else comes along that we're interested in
[884.88 → 891.56] like we're kind of all in, and it's hard to switch, and then we have this kind of almost religious buy-in
[891.56 → 897.56] to the framework that we've subscribed to and I just don't really think anybody wins in that scenario
[897.56 → 902.86] like I think we're better off you know kind of identifying and understanding the problems of building
[902.86 → 907.14] applications in this way and then being able to pick the tools, and then we're in a better spot
[907.14 → 912.78] to evaluate like which solution actually makes sense here and I also like the concept of you know kind
[912.78 → 919.64] of the small modules thing from NPM and only using what you actually need um which then leaves you the
[919.64 → 925.74] option to replace or what have you yeah see I'm on kind of two minds on this because i definitely
[925.74 → 934.54] see the value in modularity and uh dipping your toe in the water we just had uh the Microsoft team
[934.54 → 940.06] the typescript team on recently I think it was uh in 152, and you know typescript seen some adoption
[940.06 → 945.36] because they decided to go with a strict superset of JavaScript and that allows teams to like to dip their
[945.36 → 950.98] toe in the water with typescript, and it's not a huge investment right up front to get into it which
[950.98 → 955.78] sounds like that's some of ampersand's um power is that you can kind of dip your toe in the water
[955.78 → 959.82] and I see the value in that and definitely as you build and things change that's the only thing that
[959.82 → 965.04] we understand software is that things are going to change yeah at the same time I also understand
[965.04 → 970.34] that paradox of choice and oh totally that paralysis that happens when you're just getting started
[970.34 → 977.78] and I need to pick you know 30 different modules that I'm going to go with, and it requires a lot of
[977.78 → 983.32] kind of prerequisite knowledge which i I really don't like either that's something that um like
[983.32 → 986.76] if you've ever been to any of my workshops or anything that's always something I try to kind of
[987.86 → 993.24] just be like hey here's a starting point like if you do this, and you build things in this way
[993.24 → 997.32] then at least you kind of you're accidentally learning the various pieces involved here and
[997.32 → 1002.40] the problems that we're solving um but yeah I think we've made it way too hard to be a new web developer
[1002.40 → 1010.54] like way too hard like it's super frustrating um so i you know and I think I mean if you go read
[1010.54 → 1014.74] hacker news and something you're you're a brand-new developer you think you have to build some like
[1014.74 → 1021.60] crazy isomorphic app or whatever just to start right and like you're just scaring people off before they
[1021.60 → 1026.32] even start uh whereas you know when I was getting into the stuff like when I first saw jQuery and I'm
[1026.32 → 1032.20] like holy crap I can just open a console, and you know see some like little elements flying around the page
[1032.20 → 1037.00] like this is awesome I now feel powerful right and like I think what we're doing for the
[1037.00 → 1044.92] most part is scaring people off more than actually making them feel like they can jump in so what I'm
[1044.92 → 1050.32] kind of interested in is trying to find that balance between like you know giving a new person a
[1050.32 → 1057.30] toolkit that they can just start with uh without having to like grok everything but still have the
[1057.30 → 1062.82] resulting app be something that's you know reasonably performant and is well-structured to the point where
[1062.82 → 1069.02] someone else can jump in and help or whatever um so I think it's a really hard line to walk but uh
[1069.02 → 1075.20] I think we should keep trying interesting the uh the point that you get where you're picking a
[1075.20 → 1079.76] JavaScript framework you've actually already made some decisions right and one of those foundational
[1079.76 → 1086.22] decisions you've made is you're going to be client side rendering um so which yeah sort of you can you
[1086.22 → 1091.52] don't necessarily have to do it all like that but um generally speaking you've decided to separate out
[1091.52 → 1096.84] your API your service side from your client side which that's a big debate as well right
[1096.84 → 1103.68] and yeah I was interested I read a few uh pages of your book uh human JavaScript you have it online
[1103.68 → 1107.72] for free we'll link that up in the show notes uh one of the things you say there which I was a
[1107.72 → 1112.80] surprise coming from you a JavaScript advocate is that for many types of applications building a
[1112.80 → 1118.04] single page app is harder and gives you no additional value I do think there will be a day
[1118.04 → 1124.44] when that that's no longer the case, but we're not there yet yeah I agree I mean you got to realize i
[1124.44 → 1130.74] I wrote that two years ago okay so is it outdated it's not outdated it's just if you know that like
[1130.74 → 1136.94] like you said I do think we're moving towards the time when that's no longer the case right um I am
[1136.94 → 1141.40] going to go and do a second version of the book and when I do, it's going to be talking about uh
[1141.40 → 1148.10] basically recommending that what you do is that you build a kind of static single page apps if you
[1148.10 → 1152.60] will uh where you basically have everything you know your kind of get your whole file structure but
[1152.60 → 1159.22] you compile it down to a set of static assets and uh where you also then pre-render anything ahead of
[1159.22 → 1164.96] time that you know is going to exist at a given URL um I really like that pattern of having like
[1164.96 → 1170.60] kind of drawing that line in the sand like hey we're building this static app and uh I think
[1170.60 → 1176.56] once you get to that it, it can start to feel like you know this is a is a better approach however
[1176.56 → 1182.20] there's still the case where like you know for certain types of apps like why are you doing a
[1182.20 → 1187.28] client-side app anyway like it doesn't really make sense like if you're publishing a news site like why
[1187.28 → 1192.64] on earth would you make it client rendered right I don't I don't understand that uh you know to me
[1192.64 → 1196.56] you're just adding complexity there it's hard enough to get like you know if you're working
[1196.56 → 1202.32] on bbc.com to like to make a something that's going to work on every device ever right that's a hard
[1202.32 → 1207.14] enough of a problem to solve and the primary purpose the reason people are coming to your site
[1207.14 → 1213.50] is to read that content like don't make that don't make me download two megabytes of JavaScript to see
[1213.50 → 1220.18] you know to read your news article right so I think that's where you have to really focus again you
[1220.18 → 1224.56] focus on the user and all those things kind of tend to sort themselves out a little bit it
[1224.56 → 1229.06] becomes clear what you're what you're aiming to do if the answer is to provide this really rich kind
[1229.06 → 1235.06] of application like experience behind a login or something man by all means like write it in
[1235.06 → 1239.74] JavaScript but if you're just publishing content you're doing a blog or whatever like let's not make
[1239.74 → 1244.30] the hard things let's not make the things that can be simple any harder than they need to be
[1244.30 → 1249.46] yeah kind of reminds me of the uh post that martin fowler put out this week monolith first
[1249.46 → 1255.64] did either of you I did read that one yeah and then kind of the synopsis there is that there's
[1255.64 → 1260.96] this trend towards microservices and there are completely legitimate times when microservices are
[1260.96 → 1266.44] the architecture that you want to take on right but oftentimes it's not what you want to take on
[1266.44 → 1272.24] at first because you don't know what you're building or uh you're just over engineering for
[1272.24 → 1275.24] something that may never need it lots of reasons, and he goes in the details I think we'll definitely
[1275.24 → 1282.10] put that one in weekly yeah this Saturday in the queue for it is it great um but like keep it simple
[1282.10 → 1287.94] right and then and then but keep it simple without backing yourself into the corner right I think that's
[1287.94 → 1293.04] kind of what you're advocating there as well which is don't overengineer if your problem that you're
[1293.04 → 1299.58] solving doesn't require a client side rich client then don't start with that just because it's
[1299.58 → 1305.40] you know what people do right yeah totally I mean I think there's again make things as simple as it
[1305.40 → 1312.14] can be software is inherently like difficult there's like the natural state of any code base is entropy
[1312.14 → 1318.92] like we don't again it's its a battle that you have to fight I think is to try to keep things as
[1318.92 → 1322.62] simple as they can be and if you don't you just going to end up with a mess and someone else is gonna
[1322.62 → 1327.68] have to clean it up so generally kind of asked this question a bit earlier but I'm not sure if we
[1327.68 → 1332.76] got a clear enough answer if it was okay I'm not I'm just not sure hold his feet to the fire come
[1332.76 → 1338.14] on well after having this conversation I'm wondering you know what kind of developer does
[1338.14 → 1343.50] ampersand serve then you know how would they choose it over you know things like ember angular react
[1343.50 → 1349.36] Aurelia uh I put react is that react in the notes wasn't there did you replace Durand
[1349.36 → 1356.06] we had Randall in the notes jarred react is not really a great fit there Durand's also you know
[1356.06 → 1360.56] really he's moved on he's moved on there really so that's why I replaced it anyway no what I would
[1360.56 → 1366.08] I mean you it's not all its not one or the other I mean it definitely if you go amber like if you
[1366.08 → 1369.72] use ember you're you're not going to be using any ampersand stuff but like personally I've been
[1369.72 → 1373.82] building a bunch of stuff with ampersand and react and I like it a lot uh where I'm just using
[1373.82 → 1379.20] kind of ampersand to model some data from APIs and what have you and then using the simplicity of the
[1379.20 → 1384.26] of React as a view layer to just kind of re-render at will, and it's its super easy, and it makes things
[1384.26 → 1388.08] you know pretty straightforward so I think you know
[1388.08 → 1395.30] again yeah I'm not going to sit here and like to tell people to like you should use ampersand but for
[1395.30 → 1400.34] some people it really fits uh how they go about building things because it is lets you kind
[1400.34 → 1407.30] of i for example I was just in Las Vegas at future insights live and uh the guy gave came up on stage
[1407.30 → 1412.20] and gave a talk about like you know building front ends without frameworks and he starts out with
[1412.20 → 1417.20] really, really basic like he's like you don't need a model you can use these plain Jason objects
[1417.20 → 1421.26] and then he goes well then you need to put them somewhere in that case maybe like use a collection
[1421.26 → 1426.28] then he starts using he's like oh, and he started with ampersand collection like so now instead of
[1426.28 → 1431.94] having just an array of objects he had an array of small modules that he could or small models that
[1431.94 → 1435.98] he could then observe, and it's like you know that's kind of the mentality like if you start with the
[1435.98 → 1441.16] absolute basics first then you can kind of layer in stuff as you find yourself needing it as
[1441.16 → 1447.58] opposed to like I'm going to use ember for this app that you know you may never need you may never
[1447.58 → 1453.48] use a third of what ember has and has to kind of instantiate for you when you spin it up
[1453.48 → 1460.30] right so i think it's a toolkit you know it is someone said that it's its more like a machine
[1460.30 → 1465.86] shop rather than a hammer like anyone can swing a hammer but if you have a machine shop you can build
[1465.86 → 1471.36] really incredible finely tuned things um so i think that's a little bit more the
[1471.36 → 1477.16] where it fits in so how we name some of the actual individualized modules
[1477.16 → 1482.92] um just thinking for some links and just you know some of the core things you use to build so
[1482.92 → 1489.46] ampersand state for example is basically an observable object, and it doesn't make any assumptions about
[1489.46 → 1496.84] how you're going to use it so um basically you define a set of properties that this thing is going
[1496.84 → 1501.98] to store you say what type it is, and then it will throw type errors if you try to set a value equal
[1501.98 → 1507.30] to something else right it says, and it's the wrong type, and it will fire a change event anytime you
[1507.30 → 1512.08] change that value whether you do it through a set or one thing that we do that's kind of unique is
[1512.08 → 1518.00] like even if you do it via assignment so you say you know model dot property name equals something else
[1518.00 → 1522.68] you'll still get a change event from that uh because we're actually because we're forcing you to
[1522.68 → 1527.42] register which properties it's going to store we create you know these getters and setters
[1527.42 → 1533.36] to actually do that um so as a result you know you end up with this very nice little observable
[1533.36 → 1541.92] object um, and then you know ampersand collection for example is basically it's an observable array
[1541.92 → 1547.86] so you can store plain JavaScript objects in an ampersand collection um but then if you
[1547.86 → 1552.82] want to talk to an API with that collection and get that data from an API you can use ampersand rest
[1552.82 → 1557.56] collection, and then you just add a URL, and you have a fetch method now so you can call fetch and then
[1557.56 → 1565.06] you're kind of in backbone style um collections so um you can kind of you see you can kind of just grab
[1565.06 → 1571.28] what you need um one of the reasons i originally started messing around with kind of splitting this stuff
[1571.28 → 1578.88] out is like i was building this um this touch library and uh what i wanted to do was be able to
[1578.88 → 1584.20] model touch events um and if you've ever done with done this directly in a browser you have to you
[1584.20 → 1589.20] basically get you get a touchdown the touch move and a touch up right or touch end so if you want to
[1589.20 → 1595.24] do something that's like based on a hold action there's a ton of stuff that you have to model there you
[1595.24 → 1601.62] have to know like okay it started at this spot it hasn't moved more than this distance you have to
[1601.62 → 1606.30] set a timer when it first you know when you first put the finger down and then at some point you have
[1606.30 → 1612.68] to notify the code that cares about it that it's now being held right so it's a bit of a complex example
[1612.68 → 1618.32] perhaps but with something like a can take just an ampersand state object to model each touch
[1618.32 → 1623.02] and then you just set you know the properties, and then you can have all these derived properties based
[1623.02 → 1629.86] on you know the values that you set so you can say i have a classic example being i have a full
[1629.86 → 1636.18] name that's based on first name and last name right um, but these things get intelligently fired based
[1636.18 → 1642.46] on changes so if the end calculated result isn't different it's not going to fire a change event on
[1642.46 → 1648.96] the drive property so as a result you can almost kind of do this functional reactive programming style
[1648.96 → 1657.16] uh and have these very concise easy to describe uh state objects that will let you know kind of
[1657.16 → 1663.50] track complex state like that whether it's you know coming from an API or not right hopefully that
[1663.50 → 1667.68] made sense and that's a bit of a bit of a ramble and then view obviously we talked about view a little
[1667.68 → 1673.26] bit earlier it's uh it's not full on react obviously so it's something a bit more right so, but you could
[1673.26 → 1678.76] swap it out for react if you wanted to yeah, yeah, so ampersand view is a bit like it's basically a
[1678.76 → 1684.98] slightly more powerful backbone view um honestly ourselves we've recently been leaning towards just
[1684.98 → 1689.64] using react as a view layer instead and that's that's precisely the functionality that we wanted
[1689.64 → 1696.14] like being able to have the ability to swap things out as we saw fit so um if you like backbone views
[1696.14 → 1700.20] you'll probably like ampersand views if you like to react then you can just use React right
[1700.20 → 1707.64] just sitting here wondering just personally what your personal technical background is as far as did
[1707.64 → 1713.54] you cut your teeth on JavaScript or do you have other languages in your back pocket well i started uh
[1713.54 → 1720.60] years ago when i had no idea i studied business so i didn't study this stuff at all um but i mean i was
[1720.60 → 1726.28] always into computers but i didn't really like program um in my senior year in college i wanted to start a
[1726.28 → 1734.16] business uh that was like this web-based real estate listing thing and uh i couldn't afford to
[1734.16 → 1740.02] hire anybody who was any good to build what i wanted so i was like how hard can this be so i started just
[1740.02 → 1746.62] kind of messing around with it this is like 2005 um at the time i had no idea what to pick i found a
[1746.62 → 1751.82] really great tutorial on lynda.com um building an app with cold fusion so that's what i did
[1751.82 → 1759.10] yeah oh yeah so, but you know but once you kind of pickup a second and a third language
[1759.10 → 1765.72] like you start to see that they're really all the same i uh i did python after that i was really
[1765.72 → 1771.62] into Django for a while um i loved like the cleanliness of python which is something i still
[1771.62 → 1778.12] kind of miss a little bit in JavaScript is like python has pep 8 it's like hey the creator said this is
[1778.12 → 1783.54] how you should write python yeah like it'd be nice to have some of that to some extent right as well
[1783.54 → 1787.70] i like that about go too, or they actually have a tool that you know go format where you can
[1787.70 → 1791.82] run it through and just basically reformats your code according to the standards it's like awesome
[1791.82 → 1795.76] yeah totally, and you don't sit there and argue about this stuff except what i don't like is it
[1795.76 → 1800.42] puts hard tabs in there, and it's like oh no you know so like it's all good as long as you agree
[1800.42 → 1805.96] with my uh with my opinions right no totally i think it's important to recognize though yeah right
[1805.96 → 1810.44] but i think you know recognizing the things that are important to argue right versus things that
[1810.44 → 1816.14] aren't right I've recently gotten really into using um i don't know if you guys know frost um
[1816.14 → 1821.24] does a bunch of crazy web RTC stuff and is big in the node community, but he's he's the guy that did
[1821.24 → 1829.38] web torrent okay how do you how do you uh spell his name f-e-r-o-s-s he also did peer CDN if you ever
[1829.38 → 1835.92] saw that but anyway he had the audacity to create a node module called standard that
[1835.92 → 1842.94] is his set of uh oh nice code style for uh for JavaScript and i just love it I've just started
[1842.94 → 1847.94] using that like i it is didn't match everything that i believed in terms of like how i was
[1847.94 → 1852.80] writing code before it was like i don't care it's got a built-in formatter i don't have to argue with
[1852.80 → 1858.58] anybody like you just make it part of your testing there's no config there's no arguing it's like
[1858.58 → 1866.58] yeah no this isn't the make so no, no yes lint RC no j s INT RC no j s right c src what is that one
[1866.58 → 1870.64] i don't know what that one is its just another one that's the one i think jQuery uses
[1870.64 → 1877.32] if i recall it's actually it's reasonably popular but yeah i haven't I haven't used it much that's
[1877.32 → 1882.38] neat one thing that they do have that's quite cool is that you can kind of have it has a pretty
[1882.38 → 1887.66] powerful formatting stuff so once you define your rules not only can you say if you validate those
[1887.66 → 1892.92] rules you can kind of say reformat my code to meet these rules which is pretty neat you can opt in to
[1892.92 → 1896.70] certain things but not all everything well what I'm saying is you can go the other way you can have
[1896.70 → 1902.20] it formats your code based on the rules that you give it right so it's like it's not just going to tell
[1902.20 → 1907.40] you know shame on you, you didn't follow the rules it's going to also say I'll rewrite your code
[1907.40 → 1913.46] for you to match the style that you defined which is pretty cool that is and standard has a
[1913.46 → 1917.56] formatter now too so that's that's also good is there anything in here that just writes the
[1917.56 → 1924.72] code all together i wish work it on that that's the next step is like you verbally describe
[1924.72 → 1932.46] your application yeah yeah English to JavaScript there you go compiler yeah we can get the dragon
[1932.46 → 1937.04] people you know those people where you talk into the mic, and it types for you oh yeah get them
[1937.04 → 1941.38] involved they'll be excited about that you guys I've never heard of brain to JS because that's
[1941.38 → 1946.20] that's what that is yeah just brain skip the words you don't need the words just straight for the
[1946.20 → 1952.88] brain yeah straight to brain to that's cool brain to JS English is a lossy uh translation yeah
[1952.88 → 1959.48] it's my new library it's coming out in 2020 I'll use it well while we're uh learning a bit more about
[1959.48 → 1965.32] your background Eric lets uh let's let's tease real quick we're going to take a break hear from a
[1965.32 → 1970.86] sponsor but when we come back we're going to hear how you once described yourself so let's let's break
[1970.86 → 1977.16] we'll be right back you've heard me talk about top towel several times in this podcast but today is
[1977.16 → 1983.56] different I've got a special treat for you, I went out and spoke with a listener who a year ago had
[1983.56 → 1988.86] never heard of top towel he listened to the show just like you're doing right here right now today
[1988.86 → 1994.32] and heard us talk about top towel and what they're all about, and he decided to get in touch, and now he's
[1994.32 → 2000.34] living the dream as a freelance software developer with top towel his name is Dana lagoon and I sat down and i
[2000.34 → 2006.54] talked with him, I said hey what is it that you love most about top towel take a listen well for me
[2006.54 → 2012.96] the thing about top towel which I thought would be very hard for me personally as I transitioned to
[2012.96 → 2019.94] a more consulting role uh was the way I would have access to new clients and what quality of those would
[2019.94 → 2026.52] be so I found that I've had access to awesome clients through top towel, and it hasn't been that hard
[2026.52 → 2032.38] to find because they have a lot of choice and even more than that uh there's enough choice and i I can
[2032.38 → 2038.26] actually be a little selective about what kinds of things I want to be working on so I use that as a
[2038.26 → 2044.26] way to sort of hone my skills, and you know go towards the technology that I think are worth investing in
[2044.26 → 2050.06] for the future so whether it's you know including new front-end frameworks or doing a little DevOps work
[2050.06 → 2055.88] on the site i I usually am able to find clients who are had the needs of the things I want to get
[2055.88 → 2062.38] better at so that's been that's been truly useful all right that was Daniel Luzon a listener of the
[2062.38 → 2069.28] change log and also a freelance software developer with top towel if you want to follow in Daniel's
[2069.28 → 2079.02] footsteps go to top towel.com slash developers that's t-o-p-t-a-l.com slash developers to learn
[2079.02 → 2086.00] more about what top towel is all about and tell them the change log sent you all right we're back
[2086.00 → 2093.40] so Henrik you once described yourself as not a good JavaScript developer and that's on your about page
[2093.40 → 2098.24] on the and yet website so it's its in black and white you can't run away from it what made you
[2098.24 → 2102.88] say that why'd you say that because you seem pretty good to me well I mean how do we really
[2102.88 → 2108.26] objectively know anyway right I mean honestly you just put it on your about page that's all you have to
[2108.26 → 2116.62] do no I mean so what happened was uh that's uh i I said that to Adam here at and yet uh shortly after
[2116.62 → 2122.66] I started I hadn't written that much JavaScript and uh you know i just kind of I don't know I've
[2122.66 → 2127.94] been told I have an uh self-deprecating personality anyway so maybe it was just a little bit of that I don't
[2127.94 → 2134.38] know but you no longer call yourself this of course you know I've kind of come to terms
[2134.38 → 2139.20] with the fact that I'm okay at JavaScript there you go so at what point did you start getting
[2139.20 → 2143.96] deeper into JavaScript how many years has it been since you came from cold fusion went to python and
[2143.96 → 2149.48] then now you're where you're at now oh I've basically been writing JavaScript exclusively almost
[2149.48 → 2155.66] for the last five years and the uh when I first joined in, yet we had this really cool project
[2155.66 → 2163.02] they actually were um we were doing this rather intense asset tracking application they had these
[2163.02 → 2169.34] really cool little devices that um they would set up like a terrestrial network and then um they would
[2169.34 → 2176.44] uh be able to track like with super high precision within a small area uh where everything was and
[2176.44 → 2181.24] they needed a web app to do this, and so we actually wrote like a whole job system that would
[2181.24 → 2186.42] process that tons of that incoming data, and then we displayed all this stuff uh in a browser on a live
[2186.42 → 2192.28] map so it'd be the kind of thing where like you could even have someone have a sensor in a briefcase
[2192.28 → 2197.80] and they'd go up the elevators, and we would do things like switch out the uh the floor map based on
[2197.80 → 2203.44] the barometric pressure on these sensors right like it was quite an involved app, and it was very
[2203.44 → 2209.84] uh advanced as far as web apps go for it for its time and uh it was right around the time when
[2209.84 → 2216.30] like we wrote a version of it and then backbone came out we were in the process of basically writing
[2216.30 → 2221.66] our own backbone back then because we knew we needed it and then when that came out it was like
[2221.66 → 2227.50] backbone 0.3 or something I'm like nope we're using this and I just like rewrote the whole app using that
[2227.50 → 2234.30] uh and that was you know I don't know four or five years ago now but um yeah I don't know just been
[2234.30 → 2239.94] doing lots of it since then for version's sake right now the latest production version of backbone
[2239.94 → 2251.22] is 1.2.1 just yeah I'll update so is that app still in production uh yeah actually it is uh it's
[2251.22 → 2256.78] it was for a kind of very sort of private group so it's not like um it's not like something you can
[2256.78 → 2260.70] really go look at I don't think sure which is nice to be able to write software that's still valuable
[2260.70 → 2265.66] you know four or five years later yeah for sure aside from the browser changing and standards
[2265.66 → 2270.98] changing I guess within the browser um you know older JavaScript apps don't have much of a problem
[2270.98 → 2274.70] because they can be served from pretty much anywhere their client side right so you pretty much just deal
[2274.70 → 2281.28] with the evolution of JavaScript and the ever-changing landscape of the web right, right yeah and at the
[2281.28 → 2285.14] time it was unique to have something that was getting that much data pushed to it from
[2285.14 → 2289.76] the server you know through these real-time connections so we had you know we were early users of
[2289.76 → 2295.74] socket AO, and we were using before then it was even kind of these long pulling systems uh using
[2295.74 → 2302.70] Bosch XMPP to do this stuff in the browser uh which was your knowing so I was writing like XMPP plugins and
[2302.70 → 2308.78] stuff five years ago which was interesting so let's hold off on web RTC because I'd like to talk about
[2308.78 → 2315.44] that later just as a standalone topic but aside from that um you know how has the web evolved uh maybe
[2315.44 → 2319.48] from the time that you started even when you were a not so good of a JavaScript developer to
[2319.48 → 2324.48] now and then what are some technologies that are either here or do you know on the fringe of
[2324.48 → 2331.00] of coming up that are exciting for you well I think how it's evolved is it's just gotten complicated
[2331.00 → 2340.34] that's not good no it's not uh I think is that a devolution uh in some ways I think so yeah um but i
[2340.34 → 2346.64] but I think that we are starting to see a shift there and I think you know things like I mean i I think
[2346.64 → 2352.62] react is one of the few like that stands out as like an actual simplifying technology that's appeared
[2352.62 → 2357.42] uh in the last few years that actually make lives better for developers um simply because you don't
[2357.42 → 2361.38] necessarily have to do individual bindings you can just be like hey re-render whenever you want that's
[2361.38 → 2366.74] extremely valuable uh from a complexity standpoint you don't have to keep all that stuff in your head
[2366.74 → 2372.80] in the same way um of course it has its own set of challenges but I think that's um that's been
[2372.80 → 2379.60] one of these like huge uh things that have changed for the better um I totally forgot the second part
[2379.60 → 2384.24] of your question just uh upcoming technologies web technologies es6 stuff whatever is getting you
[2384.24 → 2390.54] excited and yeah you know so I'm writing a bunch of es6 now uh using babble JS as a kind of transpired
[2390.54 → 2396.74] um I think once you get to the point where you have a build step in your application which I would go as
[2396.74 → 2401.42] far as to say that you know we should all be doing that these days the tools have come far enough to
[2401.42 → 2407.76] where there's no reason not to once you have a build step you know it's a pretty inconsequential
[2407.76 → 2413.58] thing to just also sneak in a little transpired in there as well um so you know I've been writing
[2413.58 → 2420.62] es6 exclusively now for the last little bit here and I think um being able to do that it just kind of
[2420.62 → 2427.52] eliminates a little bit of um boilerplate and stuff that we had to do before so I think that's a nice
[2427.52 → 2434.10] change that we're seeing um again like I said before I'm I'm huge on like this whole concept of
[2434.10 → 2440.76] going back to making your entire client side app completely a static set of files I think that's
[2440.76 → 2445.40] I think we're going to see a lot more of that I see a lot more people doing that dramatically simplifying
[2445.40 → 2451.86] operations and stuff as a result because you're back to like transferring files like they uh
[2451.86 → 2457.24] one of the developers from shutter fly was in one of my workshops and they um they went and changed a
[2457.24 → 2462.12] bunch of stuff they built a bunch of stuff with ampersand and uh they compile it all down to a set
[2462.12 → 2469.40] of static assets, and he's like yeah our deployment tool is now sync right which is like you know and
[2469.40 → 2474.74] i in talking to folks from uh Flipkart which is one of the largest e-commerce sites in India
[2474.74 → 2480.64] they actually they have a unique situation there, but they basically do the same thing right they
[2480.64 → 2486.10] they compile everything down to a set of static assets, and then they use web views inside android
[2486.10 → 2492.58] apps to do this stuff but still like they handled their scaling issues by making their clients do more
[2492.58 → 2499.84] stuff wow they had a rather dramatic uh server issue on a very big day for them before and then this is
[2499.84 → 2504.22] how they fixed it so they're passing more stuff off to the client I think we're going to see a lot
[2504.22 → 2510.76] more people doing that as clients become increasingly better run times yeah uh related and maybe perhaps
[2510.76 → 2516.84] a little bit of a tease for next week's show we'll be talking http2 with ilia Gregorio oh he's awesome
[2516.84 → 2521.18] yeah we had him on earlier this year talking about GitHub archive, and we're excited to have him back to
[2521.18 → 2527.32] talk about the update to his book um with now that http2 has been finalizing stuff and that's really
[2527.32 → 2532.10] going to flip the script on a few things with regard to best practices and serving static assets because
[2532.10 → 2539.30] um things that we once were like you know canon truth are no longer true anymore such as you know
[2539.30 → 2545.12] the requirement to concatenate your CSS all into a single file is actually an anti-practice when it
[2545.12 → 2549.46] comes to http2 so I think things are going to be changing, but they're also going to be getting easier
[2549.46 → 2553.32] because now you don't even have to have that build step necessarily to have the performance gains
[2553.32 → 2558.56] sort of but I would still say that you know most of these people that are building these types of
[2558.56 → 2563.56] applications they're you know it's not just a matter of you know five or ten files we're talking
[2563.56 → 2569.62] a couple of hundred files maybe that need to and uh you know I don't know if doing those even if you
[2569.62 → 2575.98] kind of pipeline them in the way that you can with http2 I'm not I'm not entirely sure if it obviates the
[2575.98 → 2581.08] need for a build step um so it'll be kind of interesting to see what happens and that logic has to
[2581.08 → 2585.64] kind of happen somewhere right your server has to be smart enough to know what to send for what
[2585.64 → 2592.46] right um, and so I'm I don't know I haven't seen a ton of like really great open source
[2592.46 → 2599.20] answers to these questions, yet it's quite possible that I just haven't seen them but um but yeah i
[2599.20 → 2603.08] don't know it'll be it'll be fascinating to see what happens yeah I mean you're right
[2603.08 → 2607.82] in the fact that http2 is opt-in so you're still going to have many clients for many years
[2607.82 → 2610.84] that can't speak that language, and you're going to have to provide an optimal experience
[2610.84 → 2617.88] for them as well um I'm pretty sure that, and we'll find out next week we'll ask him this very
[2617.88 → 2624.00] pointedly but I'm pretty sure that um even with many small files it's actually faster not to
[2624.00 → 2629.16] concatenate um, but you're still going to want to minify them so yeah why not yeah doesn't go away
[2629.16 → 2633.18] right the weight you're going to want to shed some of the weight yeah yeah you're still going to
[2633.18 → 2637.74] have a bill step doesn't go away sure but but yeah i I agree I mean just the best practices
[2637.74 → 2641.50] are changing a little bit that's all exactly yeah and I think it's going to be fascinating
[2641.50 → 2647.54] to see how that kind of the tooling steps up to match that I'm quite curious to see how that plays
[2647.54 → 2653.58] out too because i I mean I think performance is one of those things that you know we have to care
[2653.58 → 2660.36] about on the web um and uh we've seen lacking kind of in some of these larger frameworks uh just kind of
[2660.36 → 2665.74] a little bit too heavy so seeing kind of the technologies kind of catch up to enable these
[2665.74 → 2671.14] kinds of things it's interesting yeah yeah we'll see yeah I'll have to pay attention next week too i
[2671.14 → 2676.10] want to hear what you said for sure the uh the other thing around performance is you know we've had a
[2676.10 → 2682.20] move recently uh thinking specifically of Facebook's what's it called instant news yeah instant articles
[2682.20 → 2687.06] or whatever yeah instant articles um where they're basically declaring which is interesting, but they're
[2687.06 → 2691.34] declaring that you know the web isn't fast enough you know we need to be able to cache these news
[2691.34 → 2696.74] articles so that we engage people faster because people want their information right now, or they're
[2696.74 → 2703.54] going to move on um and so specifically around content-based sites right news sites right um
[2703.54 → 2709.64] there's conversation around is it the web technologies and the Dom that's just never going
[2709.64 → 2715.30] to be good enough or is it you know the tools or is it the developers or is it the businesses do you
[2715.30 → 2721.10] have a take on that well I think in their case it's its fairly straightforward I mean fetching and
[2721.10 → 2726.90] and uh caching content ahead of time is going to be dramatically faster and even though they're not
[2726.90 → 2731.04] saying it I would venture to say one of the big reasons they're doing it is they want to control the
[2731.04 → 2735.88] experience of those sites as well the experience of that content um you know a lot of people put so
[2735.88 → 2741.30] much clutter and ads and stuff into these content sites like you get these like links to BuzzFeed or what
[2741.30 → 2747.30] have you and there's just a bunch of you have to sit there and wait for so many unrelated things to
[2747.30 → 2751.62] load before you ever get to see what you're trying to see that I would venture to say that's at least
[2751.62 → 2756.34] in part what they're addressing as well yeah it's not that if they knew that all these sites were
[2756.34 → 2761.38] super well optimized, and you know served content first like I don't I don't think we'd be sitting
[2761.38 → 2766.74] here having this conversation honestly it's not a big concern though for um for those who care about
[2766.74 → 2769.62] like data plans and stuff like that are like fetching data that they don't actually
[2769.62 → 2774.18] one two you're sort of prefetching assuming you're you're going to want this content, and then you're
[2774.18 → 2779.32] sort of like no I don't want it, and you're burning through all your bandwidth yeah I mean arguably right
[2779.32 → 2784.82] that's uh that's a good point um, but obviously that's a choice that they made and I mean I think
[2784.82 → 2790.50] I think a lot of people are experiencing content through the built-in browsers on Facebook these days
[2790.50 → 2797.96] and I would venture to say that you know by grabbing content directly from the publishers that the way that
[2797.96 → 2803.66] they are they're probably minimizing the total amount of size you know file coming through maybe
[2803.66 → 2810.94] but um but I don't know yeah it's hard to say I guess if you're in that Facebook wall world you know
[2810.94 → 2816.16] you're in the app you're not you know it's Facebook it's not a Facebook conversation here but just
[2816.16 → 2821.60] tiny little rant I guess is that you know if you're clicking a link from within Facebook it's
[2821.60 → 2826.90] their anticipation that you're going to want whatever you've clicked and then so they can sort of go to
[2826.90 → 2831.92] that site and prefetch a lot of the data if they need to speed it up is that what this instant
[2831.92 → 2836.86] page thing is jarred or instant article is that like so when you click through the link it's there faster
[2836.86 → 2843.32] than no it's actually like a capturing so Facebook so imagine New York times has an article Facebook is
[2843.32 → 2850.18] going to go grab that cache it and serve their version of that article to everybody um and so it's
[2850.18 → 2856.12] just not any New York times server at all any more yeah they've worked directly with publishers from what i
[2856.12 → 2861.22] understand to kind of get access and uh right so it's not going to be for every link you click
[2861.22 → 2867.00] it's right for specific publishers right and I'm sure there are deals around making sure they still
[2867.00 → 2872.42] have analytics and that kind of stuff but um because those aren't those businesses aren't just foolish
[2872.42 → 2877.30] and I'm sure they're pretty skeptical going into it still but anyway yeah a little bit
[2877.30 → 2881.40] well Hendrick did say earlier it's getting more complicated so it's just proving the truth here
[2881.40 → 2885.56] I think the web is I mean I think it's important to note that the web is getting to be you know
[2885.56 → 2890.66] simply putting your content out there you don't know how it's going to be used I mean with
[2890.66 → 2897.14] more and more devices hitting the internet that are not just you know big desktop screens people are
[2897.14 → 2902.42] extracting content from stuff all over the place and I think you know kind of coming up with ways to
[2902.42 → 2906.98] serve the content in its raw form in a way that still makes sense uh is going to be a bigger deal
[2906.98 → 2911.40] and you know we're seeing a lot more APIs and stuff but to some degree there's people getting
[2911.40 → 2917.98] really stingy about access to those APIs too so yeah we shall see the good old days are ending
[2917.98 → 2925.02] more traffic right remember the days of pop-ups and pop-up blockers I mean pop-up ads were the worst
[2925.02 → 2929.12] right and then browser vendors just solved it they're just like yeah you can't do that anymore
[2929.12 → 2935.02] and nowadays, you know we have these like full page modal things that are like it's the content
[2935.02 → 2939.80] overlay it's not a pop-up it's just like the entire page is taken over by some ridiculously
[2939.80 → 2947.06] off uh off-topic ad right before we can get to the content so it's a struggle because publishers
[2947.06 → 2951.62] need to make money you know put the content out that we want, but they're not really serving us
[2951.62 → 2956.92] it's just a mess yeah for sure so but I think the most part the people that are building like
[2956.92 → 2960.70] JavaScript applications these are not necessarily the problems we're solving you know a lot of times
[2960.70 → 2966.52] the apps that we're building um are things that are more control panel type interfaces like I think
[2966.52 → 2972.80] the whole content conversation uh is a bit different um than at least most people that are
[2972.80 → 2976.58] using these frameworks and tools that we're talking about here are not building those types of sites
[2976.58 → 2982.94] right um hopefully but I think that and I think it's perfectly okay to say that there is a
[2982.94 → 2987.98] different type of application on the web you know I think people get a little riled up about saying
[2987.98 → 2991.76] that there's you know any sort of difference between a web app and a website right like that
[2991.76 → 2998.18] old debate which is super worn and tired but um you know from my perspective it's an it's a fairly
[2998.18 → 3002.20] clean distinction you know depending on what type of experience you're trying to provide to the user
[3002.20 → 3008.60] yeah just to go back again to something that you wrote uh in your book he says building client-side
[3008.60 → 3013.10] apps is often more complicated than a server-side rendered app decide carefully ask yourself is there
[3013.10 → 3017.10] additional benefit for your users are you building something that is open and closed frequently
[3017.10 → 3021.90] are you building an experience how often does the data in the application change do you care if it
[3021.90 → 3026.14] changes while the app is open so I think that speaks well into what you're saying a lot of these
[3026.14 → 3033.34] a lot of applications that are served very well by client-side frameworks are dashboards and data-rich
[3033.34 → 3039.92] things that need to be updating live whether it's pulled or pushed um and the content sites that we're
[3039.92 → 3044.60] complaining about like they actually kind of have it easier they have the simpler side right they just
[3044.60 → 3049.12] need to serve the content and most of the time it's actually you know business constraints that
[3049.12 → 3056.18] are that are causing they just make it hard and annoying yeah on purpose yeah uh to be a developer
[3056.18 → 3062.38] you might end up putting something like back but like I can recall back at pure charity when we were
[3062.38 → 3069.02] doing some different things um you know we were doing service I'd render through a ruby app but we
[3069.02 → 3074.36] were also building backbone on top of it to provide a better richer experience for some of the data there
[3074.36 → 3079.12] so you sort of still do sometimes have that that crossover there when it does happen yeah for
[3079.12 → 3082.64] sure and especially comfort sites that's where it's nice to be able to grab little pieces that
[3082.64 → 3086.70] you need to yeah that's that's another little pitch there for ampersand right like yeah and that's
[3086.70 → 3090.38] how we've seen people use it I know people at Financial Times that have used it for little like
[3090.38 → 3096.20] you know interactive visualizations and stuff right like that are kind of add-ons to otherwise
[3096.20 → 3101.94] static sites and what have you so um you know I think yeah it's definitely it can be used in
[3101.94 → 3108.16] that tool set for sure um but yeah I think a lot of times people are you know most people that do
[3108.16 → 3113.94] this stuff day to day are being asked to build you know these control dashboards and these data input
[3113.94 → 3123.74] systems and stuff right exactly well I think uh I'd like to switch gears to web RTC okay sound good
[3123.74 → 3129.06] maybe lets uh let's take a sponsor now we'll take a break hear from a sponsor, and we get back
[3129.06 → 3133.86] uh we'll talk about web RTC and simple web RTC when we get back
[3133.86 → 3142.94] DreamHost now has managed VPS hosting built for speed and scalability including solid state drives
[3142.94 → 3148.52] and that's awesome these VPS's are built for open source developers and now include one-click
[3148.52 → 3155.66] installs of node.js custom ruby and RVM support speed and more speed is what it's all about
[3155.66 → 3163.14] their VPS servers use SSD hard drives and are 20 faster than traditional SATA drives all virtual
[3163.14 → 3171.42] private servers from DreamHost include SSD storage Ubuntu 1204 LTS web-based control panel scalable ram
[3171.42 → 3176.34] which is super awesome you can go from one gig of ram and easily scale up to eight gigs if you need it
[3176.34 → 3183.90] node.js one-click install ruby version manager unlimited bandwidth unlimited hosted domains unlimited 24 7
[3183.90 → 3189.38] go check them out and learn more at dreamhost.com slash the changelog
[3189.38 → 3198.30] all right everybody we are back we are talking with Henrik Porter about all things JavaScript and web
[3198.30 → 3205.60] and the cool stuff they're doing over at and yet uh ampersand JS and another project you mentioned
[3205.60 → 3213.22] before the break which is simple web RTC Henrik can you tell us uh first of all what's web RTC why is it
[3213.22 → 3219.50] cool and then how does your guy's open source tool play into it sure so web RTC is essentially
[3219.50 → 3228.28] a low latency peer-to-peer networking in the browser so uh you know web sockets is server to browser
[3228.28 → 3236.90] web RTC is browser to browser so you're actually negotiating a direct connection between
[3236.90 → 3242.84] two browsers and then at the point where you have that connection there's no server anymore
[3242.84 → 3250.54] um so you know you can do things like voice and video streaming so you can build you know voice
[3250.54 → 3255.70] and video communications applications, or you can use the web RTC data channel to then send
[3255.70 → 3260.24] you know whatever sort of data you want so you can do things like file transfer what have you
[3260.24 → 3267.20] um but I mean essentially the way that that works is you still need some sort of discovery mechanism
[3267.20 → 3274.16] uh to let these two browsers find each other um so they're typically which is why people kind of get
[3274.16 → 3279.82] confused about this because you need a server somewhere to kind of negotiate and send these
[3279.82 → 3285.30] signalling messages back and forth so that these two browsers can find each other um the cool thing
[3285.30 → 3290.74] about how that technology works however is your know if it can it kind of attempts to discover where you
[3290.74 → 3297.30] are and so if you have two users on the same network uh in theory at least it should be able to
[3297.30 → 3303.26] discover that they are in the same network so when you do data transfer those bits never leave the
[3303.26 → 3310.24] building um so it's its a pretty cool technology I mean it really enables a different set of applications
[3310.24 → 3315.72] to be built on the internet so all of a sudden doing skype in the browser is a viable thing
[3315.72 → 3323.18] um etc so that's kind of I don't know that's probably good of an overall summary as i can
[3323.18 → 3328.82] do awesome yeah it looks like it has kind of unfortunately spotty browser support uh the latest
[3328.82 → 3334.86] chromes and Firefox and opera all seem to support it as well as chrome for android but i.e. safari
[3334.86 → 3342.72] mobile safari and Opera Mini are all reds on the can I use charts yep so what we're doing I mean so
[3342.72 → 3349.54] well first of all that's changing as far as i.e. is concerned okay what happened is um you know
[3349.54 → 3354.84] google basically they created the CRTC standard for all practical purposes I mean there's other
[3354.84 → 3358.88] people involved don't get me wrong but like their kind of the ones that kind of pushed it along early
[3358.88 → 3364.04] on um actually that's not entirely accurate uh Mozilla was pretty heavily involved from the beginning too
[3364.04 → 3371.02] so scratch that from the record but um, but the point is like you know they just kind of pushed it and
[3371.02 → 3378.28] shipped it right like they got it out there and uh it's great for small conversations um if you want
[3378.28 → 3386.56] to do like any sort of type mesh network where every user is connected to everybody else it's fine uh but
[3386.56 → 3393.28] for what they realized is like in order to even build something like Google Hangouts using web RTC
[3393.28 → 3397.44] once you get up to you know I would say more than four or five people
[3397.44 → 3405.86] it stops making sense to have a total mesh network because now you have to upload your video stream to
[3405.86 → 3411.48] every single other person that you're talking to and pretty soon your bandwidth and your local just
[3411.48 → 3415.82] your computer just starts melting down just because it's working so hard right like it's got to encode and
[3415.82 → 3420.86] decode all this video about it is just it gets really crazy right um so if you're going to do any sort of
[3420.86 → 3427.20] larger conference scenario or any kind of broadcast scenario where you have one person sending to a
[3427.20 → 3433.02] larger audience where it's only going one direction you know the kind of the peer connection
[3433.02 → 3442.56] objects that were added to you know chrome's uh API they kind of don't do that well they don't
[3442.56 → 3449.26] handle that case yet well so Microsoft they wanted to implement web RTC, but they're like these are these
[3449.26 → 3454.48] problems that we have in order to be able to build these kinds of applications and uh so they kind of came
[3454.48 → 3458.58] forward with an alternate spec which you know you might make you might make you roll your eyes at
[3458.58 → 3463.68] first, but they actually had perfect reason to and uh so everybody's going to kind of jump over to
[3463.68 → 3470.78] that spec and that's called OTC and that enables a lot more fine-grained control over the various
[3470.78 → 3477.02] pieces so instead of having this like one serves everything pure connection object you get all kinds of
[3477.02 → 3484.28] these more fine-grained control over you can do you know interesting network topologies to make more
[3484.28 → 3489.52] efficient use of the bandwidth that you do have and what have you, so the server is still required
[3489.52 → 3496.44] though right just for uh no so just for discovery right so you can actually do uh once you have a
[3496.44 → 3502.94] connection with somebody you can actually drop the server entirely so as apple showed any interest in
[3502.94 → 3508.64] OTC, or they're still going to be I would say they're not going to do it till anyone makes them
[3508.64 → 3512.54] uh, and you know because let me think about it right like what incentive do they have
[3512.54 → 3518.14] I don't know because they have FaceTime they want you to use FaceTime yeah but Microsoft has Skype
[3518.14 → 3523.88] they want you to use Skype, and they want to build it in the browser so they're, and they're being more
[3523.88 → 3530.68] progressive in my opinion now at least with that stuff um so the and the i.e. team has committed to
[3530.68 → 3536.66] doing this so they will be doing it um in fact some folks on our team are working with them to
[3536.66 → 3544.18] make sure that uh that simple web RTC abstracts the differences so uh even when you know when they do
[3544.18 → 3550.42] show up, and you know as long as you're using simple web RTC all of a sudden you just get i.e. support as
[3550.42 → 3557.02] well um whether that's you know OTC on one end and web RTC on the other the idea is that
[3557.02 → 3563.08] you know we're going to try to abstract all that stuff out so there 's's uh this may be an
[3563.08 → 3569.10] idiot question here but the simple web RTC support both web RTC and the OTC the
[3569.10 → 3575.14] it will it will yeah okay we have to change the name jerry we've talked about that before
[3575.14 → 3581.80] we talked about that with uh Daniel Steinberg as a matter of fact uh lib curl and curl had several
[3581.80 → 3587.30] names in its history so as it evolved and supported different things we're not going to
[3587.30 → 3591.44] URL get is what I think he normally he originally called it and then yeah started doing posts and
[3591.44 → 3595.32] puts and stuff and he's like oh no it was put getting those posts' no I'm just kidding it wasn't
[3595.32 → 3599.88] yeah but he changed the name several times i think it's still going to be where we're
[3599.88 → 3605.02] seeing people are still going to refer to the technology as a whole as web RTC um I don't think
[3605.02 → 3610.30] you know I think that had enough traction I mean there 's's entire like web RTC expos they're
[3610.30 → 3615.18] they're not going to rename them or TC expo i I think people will keep referring to the
[3615.18 → 3620.80] technology as web RTC yeah we're going to keep calling the library simple web RTC um but it
[3620.80 → 3626.18] would just support both basically, so my guess is web RTC was pretty complicated if it required
[3626.18 → 3633.88] a simplification library like your own um yeah I mean it's just you know when I was doing it um
[3633.88 → 3641.28] I hadn't seen anybody do multi-user web RTC um I'd only seen people do you know kind of
[3641.28 → 3647.66] peer-to-peer with a single connection so all I really did was kind of abstract that out into
[3647.66 → 3653.50] you know where you could have multiple connections um and yeah it used to be really messy because it
[3653.50 → 3658.88] was really poorly and inconsistently implemented uh especially getting calls to work between Firefox
[3658.88 → 3665.52] and chrome when I first got that to work I was like I don't know it was kind of it was a celebratory
[3665.52 → 3669.10] moment right like because there was's a bunch of stuff that was different between the two
[3669.10 → 3675.42] implementations, and then they were really moving targets as well because it kept changing you know
[3675.42 → 3682.24] since then uh the library is now maintained by uh Philip Henke and lance stout on our team i really
[3682.24 → 3688.00] haven't done much with it in the last I don't know year or so, but they've been able to as browsers
[3688.00 → 3691.92] have gotten better they've just gone and deleted big sections of code that are no longer needed
[3691.92 → 3701.24] because so much standardized now right yeah so um yeah if it was messy but uh it wasn't it wasn't
[3701.24 → 3705.38] too bad I was kind of surprised that no one else had done it uh at least that I was aware of at the
[3705.38 → 3711.60] time when I released it so are there any cool uh projects out there built on simple web RTC that you
[3711.60 → 3717.72] have heard of um yeah there's you know code share sites uh that would I forget the name of the one
[3717.72 → 3724.10] I'm trying to think of um where you can basically kind of do live coding together uh kind of pairing
[3724.10 → 3729.00] over the web there's cool stuff like that um a bunch of people have come up and told me they built
[3729.00 → 3734.82] stuff with it uh there was one cool example uh was a student at Portland state university who
[3734.82 → 3742.94] hooked it up to um an electron microscope an electron scanning microscope and used that to share their
[3742.94 → 3750.06] microscope with other universities um so they did because you can support multiple videos
[3750.06 → 3754.84] um you know one of the videos would be the actual results coming out of the microscope and then
[3754.84 → 3759.92] the other would be the know the person they're operating it so they could kind of work on stuff
[3759.92 → 3764.04] together even with a single microscope uh different parts of the country or what have you
[3764.04 → 3769.22] um so it's really cool stuff that people have kind of hacked together but I mean the thing that it
[3769.22 → 3776.78] does is like it makes the basic part so simple that you don't really have to know much about what
[3776.78 → 3783.82] web RTC does or how it works to use it um in the same way that socket Io abstracted web sockets when it
[3783.82 → 3789.56] was really poorly implemented I mean it's the same idea here it's like you know it just irons out the
[3789.56 → 3795.04] the differences and gives you a dead simple API uh as soon as you try to kind of break from that
[3795.04 → 3801.24] it's not going to do everything you want it to um but simple web RTC itself you know given kind of our
[3801.24 → 3807.56] approach of building things as modular as we can, it's also comprised of a bunch of little web RTC
[3807.56 → 3814.70] modules so if you go to GitHub.com slash talk there's all these little libraries that that simple
[3814.70 → 3822.94] RTC just requires and uses that are done various portions of this um we recently just gave the web RTC
[3822.94 → 3827.74] name back to the Google folks on NPM because we had one you know a portion of it was just that right
[3827.74 → 3835.32] but how much do they pay you oh nothing just kidding at least on the air nothing
[3835.32 → 3844.88] so talk is an is an or on GitHub what's what is this is different um yeah, so the idea is
[3844.88 → 3851.14] like so we built an app called talkie uh talkie Io, so this is and yet okay yeah this is all and yet
[3851.14 → 3857.82] stuff so what we did is um so talkie Io was it started out as my demo page for simple web RTC
[3857.82 → 3863.18] uh I was just trying to get this thing to work with multi-user video and then so the way that it
[3863.18 → 3868.88] works is you go to talkie Io slash you know insert anything here and as long as someone else is at that
[3868.88 → 3873.34] same URL at the same time they're in the same conversation as you don't have to download
[3873.34 → 3877.96] anything you don't have to sign up you don't have to register you don't have to be logged in it's
[3877.96 → 3883.68] completely anonymous um you know, and it's encrypted peer-to-peer so it's like conceptually it's so
[3883.68 → 3888.58] much easier than setting something like Google Hangouts up right like a lot of people you know
[3888.58 → 3894.60] Fitz around with invitations and all this stuff right so you know meet me at this URL at this time
[3894.60 → 3900.10] is something that people found really useful and so you know we've seen hundreds of thousands of
[3900.10 → 3905.72] people start using this thing, and it's like it's been kind of mind-blowing um what's the performance
[3905.72 → 3911.22] like on it oh it's its quite good because I mean once again if you're doing this in smaller groups
[3911.22 → 3918.16] you can get really nice high quality video um, and we said anything north and four before was
[3918.16 → 3924.08] where you start to get in danger zone yeah it starts to get bad so then what we've done is um we've done
[3924.08 → 3929.92] a second version of this that actually uses a video bridge technology um, and it's called a
[3929.92 → 3936.48] selective forwarding unit, but the idea is that it doesn't it doesn't necessarily you know encode and
[3936.48 → 3942.60] decode video in the middle but what it does is it can kind of it can kind of uh combine things onto
[3942.60 → 3947.40] the same peer connection so that you can do larger groups so we've we've had you know successful calls
[3947.40 → 3955.22] with like 20 people um using our beta version which is at beta.talkie.io um and that's what we're
[3955.22 → 3958.72] doing we're actually in the middle of a kickstarter for that right now trying to get some more
[3958.72 → 3963.90] funding to basically add like recording capabilities and some other fun stuff to that
[3963.90 → 3969.46] um so definitely you know go check that out if you're interested in kind of open communication on
[3969.46 → 3976.48] the web, so the other piece there is that all the pieces that we're using to build talkie are all
[3976.48 → 3982.22] individually open sourced and that's all the stuff that's there in the oak libraries okay I was just
[3982.22 → 3988.38] about to ask is what part of talkie.io is open source or if any yeah, yeah so I mean the
[3988.38 → 3995.42] version that's live right now at talkie.io is using simple web RTC um the next version the one
[3995.42 → 4000.78] that beta.talkie.io is using all these various uh libraries that are there and the other cool thing
[4000.78 → 4008.58] about that is that it can interoperate so it uses uh this is a standard called XMPP for messaging
[4008.58 → 4018.12] underneath which means that you can actually build an alternate service that um that will do uh that you
[4018.12 → 4022.28] could actually call somebody at you know like a talkie service like you can call from one system
[4022.28 → 4027.22] to another system which you know would be kind of like being able to call from Skype to google hangouts
[4027.22 → 4035.16] right so we need to see I think that kind of open federated communication on the web um these are
[4035.16 → 4039.92] things we've come to expect from phones for years yeah the fact that I don't have that hey are you I'm gonna
[4039.92 → 4044.94] call you are you on Verizon or AT&T you know like that that conversation doesn't happen because they
[4044.94 → 4050.26] federate uh, but we're that's exactly what we're doing on the web right now so we want to kind of
[4050.26 → 4059.32] see that go away interesting well we'd like to close the uh the call with some insightful deep
[4059.32 → 4067.56] impactful questions and uh so deep and the first question is who are you can have one or
[4067.56 → 4074.64] many your programming heroes or one hero many heroes i i have a few I think it's hard to pick
[4074.64 → 4082.10] just one honestly um I don't know I've always been a fan of Lauren uh britches who uh who did like
[4082.10 → 4088.14] twenty and stuff he's a designer slash developer, and he just like ships cool stuff like entirely on
[4088.14 → 4094.42] his own is a bit of a unicorn in that way uh you know i just I'm blown away that somebody can do
[4094.42 → 4100.62] that at such a high level um she's certainly not a JavaScript guy but uh that's always been like
[4100.62 → 4107.56] really impressive to me um you know people like TJ Holloway chuck who can just like
[4107.56 → 4114.50] the amount of volume of high quality code that he's generated is just mind-blowing to me
[4114.50 → 4121.86] um I would list people like farms who I mentioned earlier uh he's doing some really amazing stuff uh
[4121.86 → 4126.98] really pushing the web forward um, and even you know folks like Gilmer Ralph he created
[4126.98 → 4132.44] talk at AO but like he's also done a bunch of awesome stuff since then um anyway there's a few
[4132.44 → 4138.04] to start there you go we'll get uh those links in the show notes we always like to link up the
[4138.04 → 4141.90] heroes when we can sometimes it's a Wikipedia page sometimes it's a GitHub page because yeah
[4141.90 → 4149.18] some heroes are from like you know the 1800s or early 1900s you know yeah like you go back in the day
[4149.18 → 4155.00] the days of yore to some you know to somebody who inspired the web you know yeah you know with a
[4155.00 → 4162.10] quote like uh JFK or something like that just nice you know I'm saying yeah have we had JFK as a hero
[4162.10 → 4168.76] no we have not but uh Henry mentioned him in the talk and that's why I was I did you're right you're
[4168.76 → 4172.50] pulling in a bunch of references oh man I just dropped them in there you don't even know
[4172.50 → 4176.64] it's like four or five of the show you didn't even recognize so I didn't expect you to do research
[4176.64 → 4183.00] like this I'm caught off guard we're going to have to have a commentary track on this yeah that would be
[4183.00 → 4188.42] cool we uh we appreciate our guests when they come on the show so we have to we have to do
[4188.42 → 4193.88] that do our research man so since you're since you're such an edger a bleeding edger you've got
[4193.88 → 4200.12] to be looking at some unique technologies and or projects so when you have a free weekend or
[4200.12 → 4203.64] you know and yet isn't making you work on the weekend which I'm sure they probably don't but
[4203.64 → 4211.44] they do uh if you had a free weekend, and you can choose whatever what project or what repo or what
[4211.44 → 4215.76] thing out there is sitting out there for you like waiting to go play with it, you haven't that you uh
[4215.76 → 4220.64] that's open source you haven't done yet I keep meaning to get around to playing with React Native
[4220.64 → 4227.66] a little bit um just because it's kind of it's a kind of cool idea um uh i have to throw in a
[4227.66 → 4234.32] mention to for surge to surge.sh I just freaking love those guys they've they've done some uh
[4234.32 → 4241.24] they've made this like dead simple deployment platform for uh just deploying static sites uh
[4241.24 → 4245.96] and i just love that too so I've been using that for all kinds of little pet projects and stuff
[4245.96 → 4254.82] um nice tagline zero BS yeah exactly it's from uh so brock Witten who's one of the people behind
[4254.82 → 4261.52] that he kind of helped do the whole phone gap thing um so anyway they definitely cool group of people
[4261.52 → 4270.20] there um let's see I don't know like i I think it's fascinating to use like I want to see
[4270.20 → 4275.98] people do more like physics-based stuff in the Dom uh to get sort of these more interesting
[4275.98 → 4284.00] drag things around you know gravity and those kinds of effects used inside web applications so
[4284.00 → 4291.04] um I've seen people use things like d3 as kind of the math engine and then rendering things with
[4291.04 → 4298.14] react uh and kind of using that to I don't know to get some fascinating effects uh in
[4298.14 → 4305.04] terms of interaction effects uh okay I don't know there are a few things cool jerry you want to take
[4305.04 → 4310.98] a closing question anything you got uh for Henryk no man I'm over here on surge.sh just is that right
[4310.98 → 4316.28] you probably just deployed something right I may have I don't even know this looks pretty awesome
[4316.28 → 4322.66] it's kind of cool I really like it um and i also I mean that's something I reference as a trainer
[4322.66 → 4326.14] like that's been really nice to have something like that because one of the first things I do in
[4326.14 → 4331.18] my workshops and stuff is like I have people deploy stuff because you know for so long I think there's
[4331.18 → 4335.00] been this kind of barrier like oh I'm working on this thing and then how do I actually get this live
[4335.00 → 4341.42] oh you call your ops person and like I don't have an ops person okay uh you have hosting yeah exactly so
[4341.42 → 4348.28] it's like it's kind of nice to uh to be like hey just get this out of the way right, and so I mean a
[4348.28 → 4352.86] little plug here too i have like a set of videos that basically show people how to build apps
[4352.86 → 4360.10] using ampersand react and I use surge for that too so um that stuff is that learn.humanjavascript.com
[4360.10 → 4365.06] so there's some of that stuff in there too and a good hour of that is completely free so you can bind
[4365.06 → 4368.86] of poke around in there and see what you think and at least get your hands on this stuff
[4368.86 → 4375.38] good deal so well Henryk it's definitely been uh awesome to have you on the call today I know that
[4375.38 → 4381.12] uh you span so many chasms we be in the pre-call jarred, and we're planning for this call as you can
[4381.12 → 4385.80] tell we do plan um we were thinking can we get it all in one conversation should we have you back
[4385.80 → 4390.66] for another you know would you be an I should do fewer things it's kind of annoying actually I'm
[4390.66 → 4396.22] trying to figure out how to do less simplify man you have to simplify yeah totally I keep preaching
[4396.22 → 4400.78] that and I need to do it in my own life can you read that do you know it off offhand
[4400.78 → 4409.06] your uh what you say about that what i oh the uh complexity thing um yeah oh shoot I can read it
[4409.06 → 4413.06] for you if you don't what yeah why don't you read it if you haven't all right so to maximize simplicity
[4413.06 → 4418.44] this is on the ampersandjs.com website so if you don't actively fight for simplicity in software
[4418.44 → 4425.30] complexity will win, and it will suck exactly so that that was telling jarred earlier there's no
[4425.30 → 4430.48] maybe it will suck, or probably it will it will it will so complexity always
[4430.48 → 4435.94] we're always about keeping things simple around here man we try you know it's its it's
[4435.94 → 4440.90] hard it's something you really do have to resist the urge to overengineer everything yeah
[4440.90 → 4446.74] creeps in its something I struggle with still well to the listeners thank you for listening
[4446.74 → 4451.24] to Henrik thank you so much for taking some time to join us today to talk about everything you're
[4451.24 → 4455.76] interested in and for heroes thank you for having me I really appreciate if it's a pleasure it's been
[4455.76 → 4461.70] a pleasure to have you also thanks to our three awesome sponsors for this show code ship top tile
[4461.70 → 4467.46] and dreamhost has new VPS options they have us talking about so check that out if you uh
[4467.46 → 4474.08] if you don't mind dreamhost.com slash the changelog is the URL to go to and with that fellas let's say
[4474.08 → 4476.96] goodbye see ya all right see you later
[4476.96 → 4479.54] you
[4479.54 → 4483.54] you
[4483.54 → 4485.54] you
[4485.54 → 4487.54] you
[4487.54 → 4489.54] you
[4489.54 → 4491.54] you
[4491.54 → 4493.54] you
[4493.54 → 4495.54] you
[4495.54 → 4497.54] you
[4497.54 → 4499.54] you
[4499.54 → 4501.54] you
[4501.54 → 4503.54] you
[4503.54 → 4503.60] you
[4504.08 → 4533.54] you
[4533.54 → 4533.60] you
[4533.60 → 4533.64] you
[4533.64 → 4533.68] you
