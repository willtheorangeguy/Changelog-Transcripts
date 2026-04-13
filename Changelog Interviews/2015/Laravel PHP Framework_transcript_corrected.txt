[0.00 → 16.16] welcome back everyone this is the change log and I'm your host Adam stekowiak this is episode 142
[16.16 → 22.10] today jarred and I talked to Taylor Orwell the creator and maker of Laravel an awesome PHP
[22.10 → 27.78] framework built for artisans we've got some awesome sponsors for today's show code ship
[27.78 → 32.96] top towel and clear bit we'll tell you a bit more about top towel and clear bit later in the show
[32.96 → 38.90] but our friends at code ship are all about continuous delivery made simple in just a few
[38.90 → 43.82] steps you can automatically deploy all your code when you're tested passed with code ship they're
[43.82 → 49.06] based on usability, so everything is designed to be as easy as possible and in fact they recently took
[49.06 → 54.10] some feedback from their user base and redesigned their entire application to include new usability
[54.10 → 58.82] improvements that made it even easier to use they've got great support for lots of languages
[58.82 → 63.52] and test frameworks they integrate with GitHub and Bitbucket you can deploy to cloud services like
[63.52 → 69.18] Heroku and AWS and many more, and you can get started today by trying out their free plan which includes
[69.18 → 76.42] 100 builds a month and five private projects use our offer code the changelog podcast to get 20 discount
[76.42 → 82.76] on any plan you choose for three months that offer code again is the changelog podcast, and you'll get
[82.76 → 88.18] 20 off any plan you choose for three months head to code ship.com slash the changelog to get started
[88.18 → 89.80] and now on to the show
[89.80 → 98.46] all right we're back it is it's a good day it's Friday right jarred that's right it's Friday so that
[98.46 → 104.42] means we record this show, and we've got an awesome guest today long time in the making Taylor we had
[104.42 → 111.10] to uh reschedule once you had some you had a cold or something like that and then we wanted
[111.10 → 116.18] to get you back on this show back in November but Taylor Orwell's here we're talking about Laravel
[116.18 → 125.06] uh awesome PHP framework so Taylor welcome to the show thanks for having me and uh i I know that uh
[125.06 → 130.10] some news for those who probably are really close to you know this, but you've recently gone full-time
[130.10 → 137.54] into Laravel I have I recently went full-time um starting January 1st basically I work on Laravel
[137.54 → 142.56] full-time and then also you know Laravel forge which is kind of a counterpart product uh supporting
[142.56 → 147.76] product to Laravel so yeah it's been a blast it's been really cool and I guess for the listeners out
[147.76 → 152.66] there who may not know who you are give an intro to yourself and then uh from there we'll go into
[152.66 → 160.32] to kind of explain what Laravel is at the deeper parts okay so um I'm of course Taylor I'm I grew up
[160.32 → 163.66] in Arkansas and I still live in Arkansas in the central part of the United States
[163.66 → 170.42] and I've kind of always been into you know tech and computer since I was a kid and majored in um
[170.42 → 177.68] it at Arkansas tech university and then I actually worked in the dot net field for um I guess three or
[177.68 → 183.22] four years for a large trucking company here in Arkansas and that's where i kind of got my programming
[183.22 → 189.38] chops really and worked with some really bright programmers and learned a lot and then I got into PHP
[189.38 → 194.00] because i kind of had some side project ideas that I wanted to flesh out some businesses
[194.00 → 199.90] and PHP is of course super easy to host and throw up on a server, and it's really great for kind of
[199.90 → 205.62] uh rapidly hacking something like that out so uh that's kind of how I got into PHP just dabbling
[205.62 → 211.82] like that and then eventually brought um some of my ideas from dot net over and created Laravel this
[211.82 → 219.08] this PHP web framework Laravel is it so when I say Laravel should I enunciate the l at the end of
[219.08 → 224.90] that a bit better I say laravel just like that what about you jerry how do you say it I say
[224.90 → 231.32] laravel so I'm the only one whose wrong here jeez I just follow Taylor man all right he gets
[231.32 → 235.76] to he gets to have final say on that the audience is used to it though right I mean I'm always
[235.76 → 240.72] mispronouncing something like Olivier Lacan I just couldn't get that right during the show and
[240.72 → 246.86] it's just even now I can't enunciate it once later you would you just have to mispronounce
[246.86 → 252.26] that month later sometimes I go to tech conferences, and it's like I try to pronounce things in this
[252.26 → 256.56] weird general way so that I don't I don't sound stupid you know if I'm not pronouncing it right
[256.56 → 261.64] right I try to cover both bases so to speak and the pre-show we talked about Sarah Goldman uh being
[261.64 → 267.54] on the show recently talking about the PHP spec and HHV over there Facebook and whatnot but on that
[267.54 → 274.18] show we had a conversation about whether it was called Oscan or Oscan mm-hmm gotcha still don't
[274.18 → 279.62] know yeah we're still out we'll have to get Tim on the call to see we can get a official
[279.62 → 286.94] ruling here or something on Laravel's home page it says the PHP framework for web artisans
[286.94 → 294.46] can you explain to us what a web artisan is so web artisan is kind of just a fun little marketing
[294.46 → 300.56] word we use and I think of it a lot like um you know the software craftsmanship type of movement so
[300.56 → 306.70] it's really supposed to mean the same thing um it's Laravel is built for people it's built with
[306.70 → 312.10] a lot of care I guess you could say, and we really sweat the details in terms of how easy it is to use
[312.10 → 317.48] what the API looks like uh we try to make the documentation perfect try to put a lot of care
[317.48 → 324.18] kind of handcrafted ness into the product so it's not supposed to be like elitist, or it's only for
[324.18 → 330.02] perfect programmers or whatever it's more just saying hey we really care about good code if you
[330.02 → 334.74] care about that kind of thing too maybe you'll like Laravel so uh that's kind of the thought
[334.74 → 341.28] behind it kind of the software craftsman slash artisan feel you find that that has set you apart
[341.28 → 348.24] a little bit in the PHP community I think it's I think people um you know it kind of creates this
[348.24 → 353.24] this fun community and people like to be a part of something you know what I mean like to feel like
[353.24 → 359.94] they're a part of some kind of club or movement or fun thing and I think it has benefited to kind of
[359.94 → 364.98] have um this kind of marketing angles on the framework and it kind of does set it apart
[364.98 → 371.70] in people's minds at least from a marketing perspective of this cool inner circle you're a
[371.70 → 380.20] part of Laravel developers yeah I mean also you know PHP is one of those languages that has such
[380.20 → 386.74] broad use and has been around for such a long time that there's a lot of terrible PHP code on the
[386.74 → 391.06] internet you know it's kind of like JavaScript in that way every language there's bad code out there
[391.06 → 397.60] but you know some of them kind of come up to the top of just having a lot of code out there that
[397.60 → 404.20] because it's so easy to get into yeah um it's easy to publish your kind of newbie code that being
[404.20 → 409.32] said there are a lot of PHP developers like you like yourself who really care about code quality
[409.32 → 415.14] who consider themselves more craftsmen, and so I think it makes a lot of sense to have tooling
[415.14 → 423.18] specifically tailored at these people right no uh no pun intended huh yeah I've I've said you saw
[423.18 → 429.46] what I did there I saw that I like that it's good I've said in the past that I feel like PHP sort of
[429.46 → 434.68] has this copy and paste culture that we're we're trying to get out of where like you said there's a ton of
[434.68 → 440.48] um there's I mean there are whole websites devoted to basically copying and pasting bits of PHP into
[440.48 → 446.62] your application, and we're kind of got this uh we've been playing catch-up so to speak where we're
[446.62 → 453.34] trying to talk about things like good architecture good design and at the same time um I like to bring
[453.34 → 458.44] a lot of kinds of the rails flavour in of rapid application development and making things very
[458.44 → 463.78] practical and pragmatic um so yeah we've been playing catch-up quite a bit but I feel like PHP
[463.78 → 469.02] has really gained a lot of ground in the past few years how long have you been doing Laravel
[469.02 → 478.26] I wrote Laravel it released in june 2011 so coming up on four years now wow and how many
[478.26 → 484.36] uh major versions has that been we just released our fifth version, and they've been getting farther
[484.36 → 489.42] apart like the first couple versions were really close together because we was almost all early
[489.42 → 494.54] adopters you know kind of hacker types, and we didn't really care about stuff breaking somewhat
[494.54 → 499.16] frequently so we came out with version one two and three really close together and then version four
[499.16 → 503.96] and five have been um a little over a year and a half apart coming up on two years apart so they've
[503.96 → 513.86] been spreading out yeah over 14 000 stars uh 4 600 forks on GitHub so you've definitely um succeeded
[513.86 → 521.00] where many uh frameworks and communities fail to gain a large audience can you speak to
[521.00 → 527.24] why you think that is yeah I have a few um a few reasons I think that Laravel has kind of taken off
[527.24 → 531.74] that way and one is from the very beginning i kind of made this promise to myself that I would never
[531.74 → 536.54] release any version of Laravel without good documentation I just like wouldn't do it I don't
[536.54 → 542.00] even release betas if they don't have good documentation because you I mean you only have
[542.00 → 546.66] so long to really capture people's attention you know or and give them either like a good experience
[546.66 → 552.34] or a really frustrating experience and in terms of frameworks there are PHP frameworks out there that
[552.34 → 557.64] still to this day I'm not really sure like how do I log someone in like it's just not clear to do
[557.64 → 563.78] something that basic that almost every website needs to do so with Laravel I tried to have awesome
[563.78 → 569.52] documentation from day one and then also have a really great community so from the day we launched
[569.52 → 575.04] I personally was in the forums in the chat rooms and I'm still in the chat rooms a lot of talking with people
[575.04 → 582.44] and really engaging the community to make it feel um more inclusive and tight-knit, and it draws people
[582.44 → 586.00] in, and they feel like they're a part of something they're a part of something that they can
[586.00 → 591.48] learn from, and they can get help from others and even help others themselves so yeah the documentation
[591.48 → 596.52] the community have been huge and then that ties into things like Caracas and of course all the
[596.52 → 604.30] surrounding ecosystem of educational materials so I guess uh to rewind a tiny bit bring us
[604.30 → 613.14] up to speed on exactly what Laravel is than okay so Laravel is a lot of people probably think of it
[613.14 → 618.42] as the rails of PHP um that's probably the easiest way to think of it if you're not really a PHP developer
[618.42 → 625.00] it's its really rails in the sense that it has an active record ORM uh that's that feels very much
[625.00 → 632.20] like rails after active record it also has um it's also had features um that not many other frameworks
[632.20 → 637.50] have, or that rails just got like we've had queuing a queuing system for uh over a year now
[637.50 → 644.72] with several different backends for beanstalk and AWS and iron me it has a CLI much like rails where
[644.72 → 649.82] you can just do Laravel new blog and start a new project, and you can generate migrations just like
[649.82 → 655.30] rails and the migrations even look like rails so it's very uh very much rails inspired development
[655.30 → 662.04] framework for PHP and then also mixes in a lot of unique stuff the emulating engine is called blade and
[662.04 → 669.64] is more inspired by dot net than rails I would say so uh the whole goal of it is to let's build a
[669.64 → 675.08] really productive web framework for rapidly developing your ideas and getting them out to the
[675.08 → 681.66] world as quickly as possible and making them at the same time maintainable and testable, and you know a
[681.66 → 688.18] joy to develop for tell us about blade um I know it's hard to describe code a little bit just with words
[688.18 → 697.06] but if you can what what makes it unique from a typical embedded uh emulating system, so blade is
[697.06 → 702.56] unique because it's very, very minimal under the hood um there are other emulating systems for
[702.56 → 710.46] PHP like twig which actually convert your template into a fairly complicated PHP class that then renders
[710.46 → 718.16] the HTML blade is significantly different in that it's really just a handful of regular expressions
[718.16 → 724.40] that translate your template into raw PHP which is your know compiled and stored, and then it's
[724.40 → 732.38] processed as raw PHP the next time the view is needed, but it's very much um inspired by asp.net MVC
[732.38 → 737.02] razor and in fact that's where the blade name comes from so you're going to see very familiar syntax
[737.02 → 743.54] where you have liked you know at sign if or at sign for each instead of having to do you know bracket
[743.54 → 751.36] question mark PHP all that jazz and then of course it has a kind of template inheritance where you can
[751.36 → 756.98] define a master layout and then extend that layout for your child pages and such you know that old
[756.98 → 762.06] saying about regular expressions right yeah you ran I've got I've got two problems yeah you run
[762.06 → 769.70] into issues uh with that those internals what's the what's the what's the saying uh a programmer
[769.70 → 775.40] when tasked with a problem thought to himself I know I'll use regular expressions now he has two
[775.40 → 782.24] problems kind of the old joke yeah we haven't thankfully I mean blade is pretty simple so we
[782.24 → 788.58] haven't really had a lot of problems there uh hopefully we don't yeah I am familiar with that warning
[788.58 → 797.16] you give it the uh the rails nod there I suppose right so you're on version five you've been at this
[797.16 → 803.46] for what I think you said four years now is that right yeah four years so take us back to I guess
[803.46 → 810.14] the PHP framework landscape at that time what were some of the problems you're trying to solve
[810.14 → 816.30] and what were some of the early beginnings that made Laravel what it is I guess then and then now
[816.30 → 822.68] today okay yeah I'll just I'll just talk really honestly about the PHP framework landscape back then
[822.68 → 828.50] because it's changed quite a bit uh the big players back then in terms of frameworks um were
[828.50 → 836.60] code igniter Khan and symphony and I would say code igniter and Khan are basically becoming
[836.60 → 843.28] irrelevant now but the issue was um at PHP at the time there was really not a large framework
[843.28 → 851.24] that was simple and that embraced the newest PHP features so code igniter was simple as a framework
[851.24 → 856.36] it was easy to use it had great documentation, but it was like woefully out of date in terms of what
[856.36 → 862.26] PHP could do for instance PHP had um anonymous functions you know you could um you could pass
[862.26 → 866.64] functions around as first class citizens and that makes for a perfect routing system where you can
[866.64 → 872.22] just say route get slash home and then pass it a function that is called you know kind of like a
[872.22 → 880.30] Sinatra or something like that, and so we needed a really nice modern framework that embraced what PHP
[880.30 → 887.40] was and what modern PHP was and Laravel i I really think Laravel was at the right place at the right
[887.40 → 894.14] time in that sense in that I was able to come in right when PHP had these great features these other
[894.14 → 900.36] frameworks were kind of getting dated and old and the newcomers were ignoring things like documentation
[900.36 → 905.52] and community, and so I tried to come in and bring in a modern framework with modern PHP
[905.52 → 912.90] which in Laravel one was very much uh Sinatra inspired more than rails inspired and to and
[912.90 → 917.34] fill that gap of having a great modern framework with perfect documentation that's easy for
[917.34 → 926.16] people to use and rapidly build things you mentioned rails and um we had last week uh rob Aurelia
[926.16 → 933.74] rob Aurelia his project's called Aurelia uh rob Eisenberg on the show um yeah the Eisenberg effect
[933.74 → 940.86] and he was talking about one of the things that he believes that came out of the rails' mindset which
[940.86 → 948.24] is that um you know quality frameworks um maintain their quality and their usefulness when they're
[948.24 → 954.96] abstracted or extracted from production applications or built alongside production applications um you
[954.96 → 961.38] know rails famously pulled out of base camp Rob's last framework Durand had a production application i
[961.38 → 967.20] can't recall that he built it alongside did you have that with Laravel from the beginning do you have
[967.20 → 974.64] it now what's the situation with production apps yeah I had it very early on into Laravel um I didn't
[974.64 → 982.10] have it in the very beginning for Laravel one but from Laravel um two or three on I did have a major
[982.10 → 987.42] application that Laravel was kind of extracted from and modern Laravel really looks a lot different from
[987.42 → 993.90] Laravel one, but that app was a snappy when I worked for a company called user scape we built a help desk
[993.90 → 1001.12] application called snappy it's b snappy.com and that used Laravel and so many things were extracted
[1001.12 → 1006.78] into Laravel from what we needed with snappy the queue system was kind of geneticized and brought into
[1006.78 → 1013.46] Laravel all kinds of stuff even the migration system really was inspired by our needs as a team
[1013.46 → 1021.06] at user scape so and I've I've always been terrified of not having a real application I can develop Laravel
[1021.06 → 1028.08] out of just building Laravel in a vacuum is really terrifying to me because I have no I have no compass
[1028.08 → 1034.32] so to speak in terms of what's real and what's just imagined needs you know and with Laravel 5
[1034.32 → 1042.10] since I work full-time I'm on Laravel now I actually built like a whole new sass on Laravel 5 just
[1042.10 → 1048.26] so I could dog food it in that way and really see how the framework felt, and it identified a ton of
[1048.26 → 1053.74] like little you know it didn't bring out necessarily like big show-stopping bugs, but it identified like a
[1053.74 → 1058.32] lot of little paper cut bugs I like to call them where things that are just like annoying when you're
[1058.32 → 1064.08] building a real app, and you see the edges of the framework so it's its extremely helpful to have
[1064.08 → 1068.88] that kind of thing and I imagine going forward you know over the next few years or whatever the next
[1068.88 → 1074.32] version of Laravel is I'll build something entirely new just so I can dog food it if I have to
[1074.32 → 1081.12] on the bakes on the I'm looking over the docs too by the way love the docs that uh and I like your
[1081.12 → 1087.40] principle of uh not releasing without good docs, and you can tell that's a green didn't principle
[1087.40 → 1093.46] for you but um looking over some of the basics the foundations and services you have here where's a
[1093.46 → 1099.36] good starting place for kind of covering some of these pieces in terms of architecture the
[1099.36 → 1104.88] service providers are kind of foundational and how they tie into the IOC container um it's that's a
[1104.88 → 1109.18] little bit deep of a concept or a little bit you know in the guts of the framework, but that's pretty
[1109.18 → 1117.88] foundational I would say what's uh what's IOC uh so Laravel is driven by the IOC container which is
[1117.88 → 1124.36] inversion of control container dependency injection container, and it can automatically inject your class
[1124.36 → 1131.80] dependencies so that if you have a user controller, and maybe you have some kind of user repository class
[1131.80 → 1137.88] that abstracts your all your database functions or methods you need to call you can just type hint
[1137.88 → 1142.50] that user repository right on your controller's constructor and the container will inject it
[1142.50 → 1146.82] automatically for you so you don't really have to wire up a bunch of dependencies manually
[1146.82 → 1154.22] the um Laravel's container can do all that sort of magically for you where was the inspiration for
[1154.22 → 1161.42] dependency injection the dependency injection is Laravel is really modelled after um Microsoft's
[1161.42 → 1168.66] unity container and then n inject from the dot net ecosystem you know like i I feel like the
[1168.66 → 1174.50] architecture can go a little overboard i kind of agree with um with some of the things DHH said
[1174.50 → 1180.56] recently in terms of architecture and kind of over architecting things but uh, so the container tries
[1180.56 → 1185.84] to it doesn't kind of like to dominate your life in Laravel, but it's a really helpful tool if you need to
[1185.84 → 1191.46] abstract some pieces out of your application and kind of separate layers of your application for unit
[1191.46 → 1198.10] testing or whatever gotcha as a quick plug I think we got DHH coming up on an upcoming show is that right
[1198.10 → 1203.40] Adam I was wondering if we should mention that i kind of hesitated to do so but yeah um for those
[1203.40 → 1211.22] listening now we do have an awesome show planned with uh DHH uh also known as David heifer Hanson
[1211.22 → 1219.38] the show is going to be all about 10 plus years of rails we hope that's a pretty awesome conversation i
[1219.38 → 1223.56] know that I've got about a thousand things I want to ask him I'm sure you're you're the same jarred so
[1223.56 → 1227.68] but yeah he's always got something interesting to say doesn't he at tip to the future that's
[1227.68 → 1231.68] February 20th we're recording probably a week after that on the shipping and yeah he's always
[1231.68 → 1241.34] he's always uh full of good stuff so and now a word from our sponsor top towel is the best place to
[1241.34 → 1246.54] work as a freelance software developer if you're freelancing right now as a software developer and
[1246.54 → 1252.08] you're looking for a way to work with top clients on projects that are interesting challenging and using
[1252.08 → 1258.06] the technologies you want to use top towel might just be the place for you working as a freelance
[1258.06 → 1263.02] software developer with top towel your days of searching for high quality long-term work and
[1263.02 → 1267.82] getting paid with your worth will be over let's face it you're an awesome developer, and you deserve
[1267.82 → 1272.76] to be compensated like one joining top means that you'll have the opportunity to travel the world
[1272.76 → 1278.98] as an elite freelancer on top of that top talk and help provide the software hardware and support
[1278.98 → 1284.46] you need to work effectively no matter where you are head to top towel.com slash developers that's
[1284.46 → 1290.60] t-o-p-t-a-l.com slash developers to learn more and tell them the changelog sent you
[1290.60 → 1296.42] but Taylor any other specific features so you have an ORM you have routing dependency injection
[1296.42 → 1302.82] you have kind of a unique uh at least internally unique view layer um any other major features of
[1302.82 → 1308.88] Laravel you got command line uh generators that you that are you know big tent pole
[1308.88 → 1312.20] features that you definitely want people to know about before we move on to other topics
[1312.20 → 1319.14] uh the queuing system is huge uh in PHP frameworks nothing like that exists in any other framework and
[1319.14 → 1325.24] basically I really like it because it's super easy to use so i can go to my command line and say
[1325.24 → 1331.60] make command purchase podcast maybe some purchase podcast routine that I'm going to run and then on
[1331.60 → 1336.66] that class I can just say should be queued I can just mark it with an interface that reads very much
[1336.66 → 1341.60] like you know English just should be queued and then when I dispatch that command it's automatically
[1341.60 → 1348.26] sent out to the queue and my eloquent models are serialized and deserialized gracefully
[1348.26 → 1354.16] and everything is just super easy to use and I find that's you really need that in most web
[1354.16 → 1359.36] applications you build nowadays it feels like to me some kind of good queuing system and Laravel's
[1359.36 → 1368.02] unique in that regard in PHP yeah for sure uh what about deployment uh build process uh JavaScript
[1368.02 → 1374.68] integration stuff like that yeah so we actually have a tool called Laravel elixir which is sort of a
[1374.68 → 1381.68] it's kind of sort of fluent layer on top of gulp where um we abstract out quite a bit of the
[1381.68 → 1387.22] hairiness of writing your own gulp file and so you can just say elixir mix sass and give it your
[1387.22 → 1392.50] sass file or less or coffee script or whatever, and it's like super clean I mean even just like a
[1392.50 → 1398.68] 10 line file I can do my sass I can have it automatically run my tests when I change my
[1398.68 → 1404.84] test files and I can have it version my files so that the cache busts and all that so it's really
[1404.84 → 1409.58] slick, but that's a that's a new feature in Laravel 5 and kind of kind of add-on feature is that
[1409.58 → 1415.86] that gulp integration is there a reason why uh I guess is it just to maintain writing PHP versus
[1415.86 → 1423.94] go into JavaScript like why didn't we use a PHP compiler basically why didn't you just do it
[1423.94 → 1430.10] straight in gulp like a layer on top of it yeah it is built on top of gulp, and we found that
[1430.10 → 1438.56] PHP the PHP community is um gosh it's hard to say it nicely, but we're just behind in some ways
[1438.56 → 1445.34] and it's very hard to throw people right into gulp like for our a lot of our users and so this is kind
[1445.34 → 1450.14] of a nice way to get them into gulp and get them kind of believing in themselves like hey I can use
[1450.14 → 1455.64] JavaScript build tools cool, and then they start digging into it more, and they find out oh I can
[1455.64 → 1461.90] I can write my own gulp task in this file and drop into all the gulp goodies I want it's
[1461.90 → 1466.20] kind of good way to get their feet wet and get their feet in the door whereas they might not have
[1466.20 → 1470.42] they might have felt overwhelmed or might have been scared to try something like that um had they not
[1470.42 → 1476.16] had a softer easier introduction to the whole scene how easy is it to layer on like
[1476.16 → 1481.36] a front-end framework something and like things like bootstrap or just various things that are out
[1481.36 → 1489.40] there that uh you know integration with less or sass and those pieces how easy is it to put something
[1489.40 → 1496.90] I guess an interface on top of uh you know a level app uh it's fairly easy you know it's pretty
[1496.90 → 1502.06] straightforward a lot of people just use Bauer or whatever to install whatever they want you know
[1502.06 → 1507.56] we haven't tried to get too opinionated with that out of the box we don't really um ship any
[1507.56 → 1512.98] any particular front-end framework besides you know the gulp tooling but uh yeah it's pretty
[1512.98 → 1517.08] straightforward like you would expect for any other web app really do you have anything like
[1517.08 → 1523.78] the asset pipeline like there is in rails and whatnot there are community asset pipelines that
[1523.78 → 1528.98] have been built that kind of mimic that functionality for the Laravel core itself we stuck with
[1528.98 → 1536.32] just the gulp slash elixir um integration because it's a lot simpler to build um first
[1536.32 → 1542.64] and then the asset pipeline it was so opinionated and there were so many um you know some people loved
[1542.64 → 1547.06] it and some people just absolutely loathed it, and so we were very hesitant to bring that in after
[1547.06 → 1550.88] seeing kind of some of the reaction from the ruby community so we took kind of the more
[1550.88 → 1555.98] conservative approach with kind of simple gulp file to help you get started with
[1555.98 → 1562.10] asset compilation what about the mentioned a template language earlier for the views how does
[1562.10 → 1566.96] that work I know that in the rails world you tend to have camps there's somebody who keeps the era
[1566.96 → 1571.68] someone who goes with Tamil someone that goes with something else what else is out there now
[1571.68 → 1578.42] jarred besides era and Tamil uh slim maybe slim okay so what's it like when you come into
[1578.42 → 1585.04] Laravel so you can take your pick like that sort of most probably 99 of people are just
[1585.04 → 1590.16] sticking with blade the default engine, but other people have right written engines for um you know
[1590.16 → 1595.48] PHP has Tamil parsers as well and uh there's another parser called twig which I think is based
[1595.48 → 1602.62] off some kind of python uh emulating language Jena maybe so you can swap them out and there are
[1602.62 → 1606.80] packages to do that um I don't really do it I think most people probably stick with kind of the
[1606.80 → 1612.30] default stuff there's kind of not a really um emulating language in general are not very well
[1612.30 → 1617.14] received in PHP interesting uh it's kind of interesting in that way a lot of people just like
[1617.14 → 1621.92] to use plain PHP then we'll like fight over that like PHP is a emulating language why would I need
[1621.92 → 1627.60] any other emulating language um so but yeah kind of interesting argument in PHP
[1627.60 → 1631.92] so you kind of have two sides you got you know pulling in assets, and then you have
[1631.92 → 1637.16] the people who want to have a separate front end app all together with our JavaScript frameworks
[1637.16 → 1644.70] so in that case how does Laravel play if you just want to have uh an API back end Laravel is really
[1644.70 → 1650.76] awesome that's one of the best use cases for Laravel I feel like because it's so easy to convert the
[1650.76 → 1658.78] eloquent models into Jason that setting up a Jason back end is just it's really just pretty painless in
[1658.78 → 1664.24] Laravel and other frameworks and arms and PHP are not like that at all it's very difficult
[1664.24 → 1670.86] to convert um something like doctrine entities into Jason it's just not as straightforward so i I use
[1670.86 → 1675.32] Laravel for that a lot actually because I do quite a bit of angular in my own projects and forge is a
[1675.32 → 1681.28] heavy um angular project and most of the Laravel app I would say is just serving up Jason, and it's its
[1681.28 → 1685.78] really great for that because the ORM suits it really well and that was kind of that was intentional
[1685.78 → 1692.38] you know even a few years ago it was very obvious that these Jason backends were going to be extremely
[1692.38 → 1698.38] popular and maybe even more popular than you know your typical template back end emulating system
[1698.38 → 1704.94] so we always have tried to make the API building super easy right uh right about now it's probably a
[1704.94 → 1710.02] good time to mention I guess Caracas by way of talking about composer I was pretty excited to
[1710.02 → 1716.12] stumble upon the fundamentals for Laravel 5 being completely free so big shout out there to
[1716.12 → 1724.80] Caracas but uh composer is the dependency manager for PHP uh again jarred and I aren't PHP developers
[1724.80 → 1729.36] but kind of walk us through that we're norms to say bundler for example in the review world
[1729.36 → 1736.14] um how does this play into Laravel yeah composer feels um it's a lot like bundler it's a lot like NPM
[1736.14 → 1740.90] if you're familiar with that and node so you would just have like a requirement block just like
[1740.90 → 1745.52] you really do a NPM, and you list out your PHP packages that you wanted to pull in and instead
[1745.52 → 1750.44] of pulling into node modules it would pull it into a folder called vendor and all the PHP code would be
[1750.44 → 1756.10] in there and all that jazz so it works very similar to that, but that was huge for PHP that's
[1756.10 → 1760.74] probably one of the biggest PHP developments really over the last five or six years was getting
[1760.74 → 1766.42] something that would let us easily distribute code and package form because we did not have a very
[1766.42 → 1771.52] clean way to do that before that and that kind of churned the whole ecosystem and kind of
[1771.52 → 1777.58] revitalized people into writing and sharing open source PHP code all the packages are shared at package
[1777.58 → 1788.02] a gist.org um so that's you know if you go to get composer.org you got browser or sorry browse packages
[1788.02 → 1794.62] so since you mentioned NPM that sort of makes you and throwing no stones here of course but just
[1794.62 → 1799.54] like you said speaking plainly here in some cases but kind of makes you really have some respect for
[1799.54 → 1806.62] what NPM's done for the just dependency management of packages because the front end to NPM in comparison
[1806.62 → 1813.66] to this is sort of night and day yeah for sure well maybe we should talk about a little bit more
[1813.66 → 1817.64] about your community and more about how you're making a living man because you're you're full
[1817.64 → 1822.30] time now that's true yeah full-time you keep you do keep saying we which I like yes you obviously are
[1822.30 → 1827.44] not you're not you're not the only committer on this project i I hope um seems like it's you got a
[1827.44 → 1833.18] nice community going so tell us who all's involved besides just yourself and then follow up with that on
[1833.18 → 1840.64] how you're actually going to make a living ongoing okay so the Laravel in terms of the code base
[1840.64 → 1846.36] I make most of the commits on the code base however there is sort of an inner circle of Laravel
[1846.36 → 1853.64] community members like Jeffrey way uh people that I have worked with in the past a guy named dale
[1853.64 → 1859.80] Reese in England and all these people we kind of collaborate on Laravel ideas and then of course
[1859.80 → 1864.88] we have tons of community members on GitHub issues and pull requests commenting and giving their feedback
[1864.88 → 1870.54] and our IRC channels and so forth so even though I write the majority of the code a lot of the
[1870.54 → 1876.08] features are discussed and kind of ironed out beforehand by the community or um you know
[1876.26 → 1883.52] in IRC or whatever in terms of um you know making a living you know I didn't want to charge
[1883.52 → 1887.70] have some kind of premium Laravel right that would feel kind of weird and I don't think
[1887.70 → 1892.62] would be well received so what I did was come up with this idea called Laravel forge where
[1892.62 → 1898.48] it's sort of like a poor man's Heroku in a way where it links to your digital ocean or your
[1898.48 → 1904.88] Linde account, and it provisions the whole server with PHP and nginx and geocached and Regis and
[1904.88 → 1911.08] everything you would need really to build a nice PHP app, and then it has deployment tools where you
[1911.08 → 1917.08] get kind of the Heroku style push to deploy when you push your git repository you can add environment
[1917.08 → 1923.16] variables and even set up SSL and subdomains and all that jazz you can do through forge and that's
[1923.16 → 1928.56] that's ten dollars a month for the basic plan so it's its really affordable because digital oceans
[1928.56 → 1934.68] servers are of course pretty affordable it's like uh 20 bucks a month for a two gig ram instance and
[1934.68 → 1939.92] then 10 bucks a month for forge, and you're really got everything you need to get started so that's
[1939.92 → 1945.08] been really well received and PHP really didn't have anything like that because uh PHP support on
[1945.08 → 1950.98] Heroku is of course not as uh fleshed out I would say is the ruby support the default ruby support
[1950.98 → 1957.44] I like the idea of this though you also have uh one layer above that too so you have a 10 dollar plan
[1957.44 → 1963.80] and a plus plan if I recall correctly wasn't it yeah the plus plan lets you share servers with
[1963.80 → 1968.44] teammates so that you can, you know share across accounts that's more of like a business feature
[1968.44 → 1973.52] um yeah so it's a really nice setup, and then we also came out with this thing at the same time
[1973.52 → 1980.00] called Laravel homestead which is free and that's a vagrant virtual machine that basically mirrors
[1980.00 → 1985.90] the forge environment so that you can have um your local environment very much mirroring
[1985.90 → 1989.90] your production environment in terms of software and all that and that the goal behind that is
[1989.90 → 1995.42] really to make the whole development experience really great from beginning to end or what I say
[1995.42 → 1999.90] from download to deploy so we want your local development experience to be perfect with
[1999.90 → 2004.80] Laravel homestead, and you don't have to muck around with your uh you know your OS 10 or
[2004.80 → 2010.44] whatever installing crap uh through brew a good way to say all that installing crap yeah it's a mess
[2010.44 → 2016.16] all that stuff that way yeah, yeah so if your homestead gets all jacked up you just delete it and
[2016.16 → 2020.80] reprovision the whole thing it takes you know just a couple minutes and so then you know you've
[2020.80 → 2025.76] got the download part the homestead the local development all the during your development you've
[2025.76 → 2030.10] got all the documentation Caracas and then when you're ready to deploy you've got Laravel forged so
[2030.10 → 2034.96] kind of that whole story is fleshed out from beginning to end in terms of how you're going to
[2034.96 → 2042.88] build and launch your PHP application using Laravel so did you have this out, and we're making money
[2042.88 → 2048.84] uh prior to January or are you hoping this takes off uh is this gonna is this already supporting you
[2048.84 → 2055.76] yeah this is already supporting me so I launched forge I launched forge in May and i I worked um for
[2055.76 → 2062.72] user scape for the rest of uh 2014 basically and forge was out there and making money and really
[2062.72 → 2068.60] had um what could have supported me a lot earlier I just hadn't gone a full-time yet I actually went
[2068.60 → 2073.38] part-time at user scape in August, so a couple of months after forge came out I only worked every other week
[2073.38 → 2080.64] for user scape and then in between weeks I worked on Laravel nice, and you decided to make the full-time
[2080.64 → 2085.36] jump how have you how have you reacted to that decision here I guess you're only about a month in
[2085.36 → 2091.10] yeah i I love it so far I mean it's just insane how much more I can get done on the framework I mean
[2091.10 → 2096.22] even back when i before I was full-time even just like a full day to work on the framework because
[2096.22 → 2103.80] my boss uh gave me um every Friday to work on Laravel and that was huge back then just to have
[2103.80 → 2108.66] one full day to work on open source it was insane the amount of pull requests and issues you could go
[2108.66 → 2114.12] through so to have five days a week of that is you know pretty unbelievable I'm really thankful for it
[2114.12 → 2119.04] it's allowed you know it's going to ensure a bright future for the framework I think having someone
[2119.04 → 2127.22] that can devote this much time to it every week and now a word from our sponsor clear bit is a new
[2127.22 → 2133.24] company that builds business intelligence APIs friend of the show and past guest on the show
[2133.24 → 2139.16] Alex McCall if you want to go back and listen to that show its episode 71 by the way he runs clear bit
[2139.16 → 2144.16] and they offer a collection of powerful APIs designed to help your business grow specifically
[2144.16 → 2148.98] they have one API that takes an email address and returns related social information such as
[2148.98 → 2154.94] the person's name title social accounts like Twitter and Facebook they also provide an API that looks up
[2154.94 → 2161.44] company information via a domain name they return attributes like company name location category head
[2161.44 → 2165.54] count now there are lots of use cases for both these APIs, but they're especially awesome
[2165.54 → 2170.18] for finding out more information about your customers and their companies for example clear bit
[2170.18 → 2175.00] has an alert triggered whenever a high profile customer signs up and their metric for someone
[2175.00 → 2179.88] that might be high profile for them is a startup that has recently raised money if you want to learn
[2179.88 → 2184.72] more about the powerful APIs they offer head to clearbit.com and tell them the changelog sent you
[2184.72 → 2194.58] can you talk uh a bit about your choice of vagrant and homestead and I guess the I mean you already
[2194.58 → 2201.42] said the crap part of that, but you know some use a camp I guess can you talk about the idea of
[2201.42 → 2207.10] vagrant I guess in this scenario because it's not a norm for PHP developers to use this
[2207.10 → 2214.24] yeah it's uh yeah it's its yeah it hasn't been in the past I think it's starting to grow now that
[2214.24 → 2219.60] people are sort of seeing what it can do um of course, so there's there are multiple aspects um
[2219.60 → 2226.44] it's difficult to configure setup PHP and nginx and my sequel especially like on Windows I would
[2226.44 → 2231.38] say um it was more difficult to get all that set up and then including like teacake and Regis
[2231.38 → 2236.26] or like a queuing system on Windows would be even probably more challenging to set up
[2236.26 → 2242.22] and then of course on the mac side it was just for me, it was always like it made me nervous to install
[2242.22 → 2246.14] a bunch of that stuff because what if I mess it up will, I have a good way to reverse it or like
[2246.14 → 2251.22] is my system screwed and I just like throw my Mac away and get a whole new mac, or you know just all
[2251.22 → 2255.80] those fears you have of kind of mucking around in the internals of your system and installing that
[2255.80 → 2261.18] kind of software so once I tried out vagrant I hated it at first because I felt like it was kind of like
[2261.18 → 2266.50] slow and I had to provision the whole box every time and so like every time I destroyed the box I had
[2266.50 → 2271.84] to like reinstall wait for it to install PHP nginx my sequel, and it took quite a while like 10 minutes
[2271.84 → 2278.22] and so I hated it at first but then I saw that you could kind of you could kind of build your box
[2278.22 → 2283.02] and then store it off and people could use that as a starting point and so that's kind of what gave
[2283.02 → 2289.20] me the idea for homestead where when you when it comes down it's already got PHP and Postgres and
[2289.20 → 2292.72] Regis and all that, and then you can install anything else you want on top, but that makes the
[2292.72 → 2299.38] the provisioning process you know like 10 seconds instead of 10 minutes and so uh and then also you
[2299.38 → 2303.96] know like I said just the ability to totally destroy that box and play with it install whatever
[2303.96 → 2309.18] you want you know you install elastic search maybe, or you install all kinds of node stuff, and you can
[2309.18 → 2313.78] do whatever you want and if something gets totally screwed up who cares I can just delete the whole box
[2313.78 → 2319.88] and have a fresh one in 10 seconds so I don't have to worry about messing up my Mac I like the idea
[2319.88 → 2326.34] of vagrant here I know I've been using that for any WordPress sites I still maintain which the changelog is on
[2326.34 → 2333.88] on WordPress right now so we spin up I think it's a shout-out to vagrant press I believe is what I use
[2333.88 → 2339.82] it pretty much mirrors our digital ocean instance and we're good to go on that front and
[2339.82 → 2346.16] I like that a lot so it's an it's a good process whereas normally you know you're used to either
[2346.16 → 2351.60] using map or something that's you know gives you less ability to fine-tune like you've done with the
[2351.60 → 2359.96] box and having an actually named thing like homestead so um we did kind of get off track there with uh
[2359.96 → 2366.66] with that question there about the money topic there I guess and ford so maybe it makes sense uh
[2366.66 → 2373.14] to swing back there and talk about future plans for ford I know that prior to the call in the members
[2373.14 → 2378.20] only slack room so a shout-out to that as well a lot of shout-outs today you know we just launched
[2378.20 → 2383.56] the members only slack room so if you're a member of the changelog if you're a supporting member than
[2383.56 → 2387.40] check your inbox you got an invitation and if you don't then email us we'll get you in
[2387.40 → 2396.02] but before that Taylor I asked you about an unofficial forge uh CLI, and you hinted at some secrecy so is
[2396.02 → 2401.56] there anything you could share at all well I'd like to get a forge API out you know which would enable
[2401.56 → 2406.94] the community to do a lot more than they can in terms of building cool little tools like that I mean
[2406.94 → 2411.12] there are people that have expressed interest in writing you know desktop apps for forge where you
[2411.12 → 2415.76] can drag a folder onto your forge app, and it launches a server and deploys the app and all that
[2415.76 → 2421.70] if I had is I can get a good API out um of course that would enable a lot of that stuff and then
[2421.70 → 2426.74] um as I mentioned before you know when I wrote Lara 5 I've actually built a whole new sass which I've
[2426.74 → 2432.24] actually got you know sitting on my computer and in a private repo on GitHub that uh complements
[2432.24 → 2438.80] forge I would say in a way, and it's kind of an unrelated field in terms of application deployment
[2438.80 → 2443.80] and launching and all that so I'm going to polish that up in the next few months and
[2443.80 → 2448.34] hopefully get it out there soon I think that'll be another cool product that people can use with
[2448.34 → 2454.20] their Laravel apps and even just generally PHP apps while we're on the notion of forge how much
[2454.20 → 2461.32] of a linchpin is it to the developers using Laravel to use forge it's it saves you so much time it
[2461.32 → 2467.16] really does um you know a lot of people in the PHP world over the past few years have been really
[2467.16 → 2472.02] locked into shared hosting and that's because they don't feel comfortable configuring their own server
[2472.02 → 2478.74] and there was nothing like um a Heroku for so long uh for PHP that people just bought you know this
[2478.74 → 2483.20] five dollar a month shared hosting and that had a lot of downsides like sometimes you might
[2483.20 → 2488.74] not even have terminal access to that host, or sometimes they don't have uh Regis and you really
[2488.74 → 2493.38] want to use Regis for this app because you like some of its features and so people have been really
[2493.38 → 2499.48] stuck in terms of what they could do with their PHP apps so to have something that's basically just as
[2499.48 → 2505.20] easy as shared hosting and is you know minimally more expensive than shared hosting, but that gives
[2505.20 → 2510.06] you so much more that you can do in terms of even what kind of database systems you can use
[2510.06 → 2516.60] with Postgres and then geocached and beanstalk queues and all that uh it just you know I feel like it's
[2516.60 → 2520.18] opened the door for a lot of people to do things that they wouldn't have felt comfortable doing
[2520.18 → 2524.52] and that's kind of what we're all about um for Laravel at least is how can we help people turn
[2524.52 → 2530.48] their dreams into reality and how can we remove roadblocks from people's development experience so
[2530.48 → 2535.98] whether that's gulp with elixir or deployment with forge or server configuration or local development
[2535.98 → 2540.98] with homestead how can we get these roadblocks out of the way so that you have a great experience
[2540.98 → 2546.02] turning this app ID you have into reality, and you know making money and supporting your family and all
[2546.02 → 2553.52] that good stuff so that's kind of our overarching goal so you mentioned a future SAS product to sort
[2553.52 → 2560.96] of complement forge any anything else you could share think of like uh you know what's on the horizon
[2560.96 → 2565.68] what's super secret what's something you can share today that's enough but doesn't put you to timelines
[2565.68 → 2573.84] or you know we don't expose too much but whatever you can one issue with forge um is that I can't deploy
[2573.84 → 2580.70] something like forge with forge because forge has um very simple deployment facilities and that it's
[2580.70 → 2585.50] kind of locked to one server it's very limited in terms of what it can do you know when you push when
[2585.50 → 2589.64] you push to GitHub it can run a bash script on your one forge server, but that's pretty much it
[2589.64 → 2594.74] um so I'd like to see something where how can I deploy something like forge
[2594.74 → 2602.72] with a product that's as easy as forge to use so um I think there's a pretty good use case there and i
[2602.72 → 2607.18] think it's going to be I'm really interested to get it out there, but it's going to be yeah it's
[2607.18 → 2612.04] going to be interesting it's going to be a great way to deploy PHP I feel like just looking at your
[2612.04 → 2616.86] forge page here I've also been looking at your Laravel page and your CARICOM page and I'm just
[2616.86 → 2622.58] thinking these are all really nice designs just on top of it all and then I'm thinking, and you also run
[2622.58 → 2630.66] this you know this cloud I mean it's not your infrastructure but right you have says you have sysadmin
[2630.66 → 2637.34] skills it appears like do you do all your own designs as well I don't do the designs the
[2637.34 → 2641.32] know I have I've kind of developed a circle of friends you know I was going to get mad at you for a
[2641.32 → 2646.08] second I was like man this guy can do it all yeah I don't do the designs I did the forge um
[2646.08 → 2650.74] the internal app design of forge I did do, but that's not much more than basic uh bootstrap
[2650.74 → 2657.24] customization the front page of Laravel a guy named jack McKay did who actually makes a PHP cms
[2657.24 → 2663.28] called stat amic which is a flat file cms, and he helped me out with that how about Aragon because
[2663.28 → 2669.00] your Aragon site has a really cool uh SVG animation at least on desktop as you hit the
[2669.00 → 2676.66] Aragon us logo so the Lara the Aragon stuff is actually done by a group in Amsterdam i I partner
[2676.66 → 2683.66] with a guy named Sean McCook um to he does the Aragon EU chapter the European Aragon and i kind
[2683.66 → 2688.68] of manage the U.S. uh conference, and so we kind of went in together this year on the branding and
[2688.68 → 2693.20] the design and split the cost of that so that we could have kind of a unified appearance across both
[2693.20 → 2700.14] conferences and so yeah we used a firm in Amsterdam to do a lot of that branding I like it that it is
[2700.14 → 2708.04] very hot anytime I see a SVG animate I'm just like oh it's awesome anyway um so I guess getting
[2708.04 → 2712.80] back to some of these supporting things is this supporting you as well is this profitable I guess
[2712.80 → 2719.16] yeah Aragon does usually generate a little profit i I couldn't live just on Aragon like if forge
[2719.16 → 2724.76] collapsed I couldn't keep going just on Aragon but uh yeah it turns a little profit, and it's nice it is
[2724.76 → 2729.32] quite a bit of work of course to have a conference and get the speakers, and you know you
[2729.32 → 2733.12] really want to provide an um you know obviously you want to provide a great experience for people
[2733.12 → 2737.36] that come to these conferences and there are so many things that could go wrong at a conference so
[2737.36 → 2742.88] it is quite a bit of work and stress but yeah it really goes well and everyone seems to have a
[2742.88 → 2747.72] great time the past few years so I'm looking forward to it, you mentioned I guess jarred mentioned earlier
[2747.72 → 2752.36] that you keep saying we and this might be a good time to give a shout-out to some people that have
[2752.36 → 2757.68] helped you this past four years get to where you're at now so beyond you who else is in the
[2757.68 → 2762.84] Laravel community making sure you don't go crazy yeah I mean the first person that comes to mind
[2762.84 → 2767.18] would be Jeffrey way which I mean a lot of Laravel success I think has to be credited
[2767.18 → 2775.48] to him, and he runs Caracas of course and I mean this guy has hundreds of videos on how to
[2775.48 → 2779.78] do modern PHP and how to do Laravel and even really other stuff too like how to do gulp and
[2779.78 → 2786.56] some JavaScript stuff so I mean without that resource Laravel I think would not be as far
[2786.56 → 2791.54] along as it is so he's definitely the first person that comes to mind thinking um and then of course uh
[2791.54 → 2797.26] you know my overseas friends with Sean who have kind of maintained that community over there and
[2797.26 → 2801.84] been leaders in Europe in terms of organizing community events and conferences and there are
[2801.84 → 2807.90] just so many user groups all around the world um like I just saw um you know the London Laravel
[2807.90 → 2813.68] meetup has like 50 people every time they meet up and that's a really nice meetup really from
[2813.68 → 2819.50] you know kind of a young PHP framework so there's so many people in the community anyone that writes
[2819.50 → 2825.20] these blogs or organizes these meetups I feel like is contributing because they're they're building
[2825.20 → 2831.80] a more open and diverse and inclusive community all around the world this might be a good chance for
[2831.80 → 2841.50] us to give a shout-out to listener Justin page who is handle is klutz on GitHub he uh first pinged us
[2841.50 → 2847.20] for a Laravel show all the way back in April 23rd so Justin thanks for the idea thanks for your
[2847.20 → 2853.34] patience, and it's been a while since April but here it is uh at the time he had mentioned uh yourself
[2853.34 → 2858.04] Taylor as well as Jeffrey way he also mentioned perhaps a good guess would be a guy named dale
[2858.04 → 2866.68] Reese he appears to be at least an enthusiast has he been involved yeah dale was super um super
[2866.68 → 2872.24] popular with Laravel 4 because of his um his code bright book he wrote a really popular Laravel book
[2872.24 → 2879.06] it's actually the top grossing book on lean pub out of all books wow on lean pub so um it was a
[2879.06 → 2885.30] very popular book and he actually because of you know his work in Laravel got hired on to what i
[2885.30 → 2891.00] believe is the fastest growing startup in the UK which is um just park or park at my house
[2891.00 → 2897.00] which is kind of like Airbnb for parking where people that have an extra parking spot can
[2897.00 → 2903.50] basically rent out their parking spot for any period of time and that's I mean it's huge like uh
[2903.50 → 2909.92] I saw um I think it was many was even building like integration for this thing into their cars
[2909.92 → 2914.44] wow over there so yeah it's a pretty big deal that reminds me of something that used to happen around
[2914.44 → 2919.10] Omaha uh we have the college world series comes here every June which is kind of one of our bigger
[2919.10 → 2924.30] events and used to be in the ballpark that was down by these old small neighbourhoods with
[2924.30 → 2930.66] small houses with large kind of gravel driveways and no parking at all and uh there was a huge
[2930.66 → 2938.14] huge boon around temporarily selling your driveway out um for parking spots for the two weeks of the
[2938.14 → 2943.92] college world series and uh then they moved to a stadium kind of in downtown and that whole
[2943.92 → 2948.80] neighbourhood was very, very upset about that but cool idea I could see why it'd definitely take off in
[2948.80 → 2958.14] crowded areas just park like that yeah so he's the CTO of just park so he is not as um involved I think
[2958.14 → 2963.06] he would love to be more involved with Laravel 5's release, but you know he is you know he's pretty
[2963.06 → 2970.90] busy these days um managing the tech side of that startup awesome man well great stuff this sounds like
[2970.90 → 2975.52] a huge success and uh we're excited to see where you take it from here we do have a few closing
[2975.52 → 2980.58] questions that uh we generally ask, and so I guess we'll go to those now uh the first one is who is
[2980.58 → 2989.50] your programming hero uh lately it's been I would say DHH the rails guy um mainly because I think
[2989.50 → 2995.98] he's perfect at seeing through a lot of BS um from the programming community and kind of calling
[2995.98 → 3002.74] things how he sees it and keeping things very practical and easy to use because I mean i always I've laughed at
[3002.74 → 3008.94] um you know at one of his keynotes he said basically is the code cleaner easier to read
[3008.94 → 3014.74] if not then you know who gives a shit about anything else and uh you know that's something I keep in mind
[3014.74 → 3019.44] a lot with Laravel in terms of keeping things very nice and expressive and easy to get into
[3019.44 → 3027.66] awesome um next one what would be a call to arms or something that you would say directly to the
[3027.66 → 3031.98] open source community how they could get involved what they can do in regard to Laravel
[3031.98 → 3038.32] one of the most valuable things just anyone can do with Laravel is if you learn something cool with
[3038.32 → 3046.14] Laravel or learn something about the framework share it or blog it or make a post or share it at a user
[3046.14 → 3051.02] group or even start a user group if there's not one near you because the more of that kind of stuff
[3051.02 → 3055.56] that's in the community it makes it even easier for other people to get involved so the more we're all
[3055.56 → 3060.98] sharing our knowledge and sharing the way we do things with Laravel it just makes the ecosystem
[3060.98 → 3066.00] that much bigger and that much brighter and helps bring in even more people so definitely share what
[3066.00 → 3070.72] you've learned speak at conferences speak at user groups start user groups that kind of thing
[3070.72 → 3077.24] awesome last question this one's kind of more personal about you Taylor um if you were not doing
[3077.24 → 3082.38] what you're doing now which is your know coding Laravel and running forge making a living with your code
[3082.38 → 3089.84] what would you be doing instead hmm I've uh you know I've always kind of been interested in like
[3089.84 → 3095.10] being like a really high-end car detailer like detailing like Ferraris and stuff um and I was
[3095.10 → 3099.30] really into that in college um so I would probably do something like really basic like that with my
[3099.30 → 3104.46] hands because sometimes I feel like you know I'm in the code so much and in these abstract things like
[3104.46 → 3110.44] sometimes just like mowing grass yeah or like detailing a car seems really appealing so I'd probably do
[3110.44 → 3115.90] something uh simple like that some kind of simple work that is a first for us for sure I can that
[3115.90 → 3120.46] resonates that resonates with me though because i I've told my wife many times that when I retire
[3120.46 → 3125.00] or something I just want to be like a mailman I can just like to drive around and enjoy the weather
[3125.00 → 3130.04] and listen to podcasts all day or I said I'd even be a garbage man which that would suck at certain
[3130.04 → 3135.64] points but professional something simple you know when I was in college I had a job uh one summer
[3135.64 → 3140.20] mowing soccer fields, and it was honestly like one of the best jobs I've ever had it was amazing
[3140.20 → 3147.58] those are always fun right that's that's cool though I'd never um I mean i can relate
[3147.58 → 3153.96] obviously but just didn't expect you to say that uh detail cars but I guess if it's a Ferrari
[3153.96 → 3159.02] and it's a know a lot more elegant right yeah exactly would it be your Ferrari as a thing
[3159.02 → 3165.16] I hope so that would be awesome just I just clean my car all day I clean my Ferrari
[3165.16 → 3170.12] that's what I do that's what I do for work all right well Taylor you know it has been a while
[3170.12 → 3176.76] getting on the show definitely excited about what you're doing here I think yeah I don't code PHP
[3176.76 → 3182.88] but you know I knew that we needed to get you on here because we'd heard so much about what you're
[3182.88 → 3187.74] doing with Laravel, and then you mentioned Jeffrey and the rest of the community, and you know and
[3187.74 → 3193.44] obviously uh since April of last year we were getting uh mentioned to have you on the show and
[3193.44 → 3199.60] and get talking about this and I'm just glad we can finally do that um you mentioned digital ocean
[3199.60 → 3205.00] uh they are a sponsor of this show but on that note I do want to kind of tag some sponsors before
[3205.00 → 3211.92] we close out here we got code chip top towel and clear bit uh sponsoring this show today so with that
[3211.92 → 3216.02] fellas let's let's say goodbye all right thanks for having me yeah
[3216.02 → 3223.92] you
[3241.92 → 3253.92] you
[3253.92 → 3255.92] you
[3255.92 → 3257.92] you
[3257.92 → 3259.92] you
[3259.92 → 3261.92] you
