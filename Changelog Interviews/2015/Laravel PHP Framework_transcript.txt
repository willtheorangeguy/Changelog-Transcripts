[0.00 --> 16.16]  welcome back everyone this is the change log and i'm your host adam stekowiak this is episode 142
[16.16 --> 22.10]  today jared and i talked to taylor otwell the creator and maker of laravel an awesome php
[22.10 --> 27.78]  framework built for artisans we've got some awesome sponsors for today's show code ship
[27.78 --> 32.96]  top towel and clearbit we'll tell you a bit more about top towel and clearbit later in the show
[32.96 --> 38.90]  but our friends at code ship are all about continuous delivery made simple in just a few
[38.90 --> 43.82]  steps you can automatically deploy all your code when you're tested passed with code ship they're
[43.82 --> 49.06]  based on usability so everything is designed to be as easy as possible and in fact they recently took
[49.06 --> 54.10]  some feedback from their user base and redesigned their entire application to include new usability
[54.10 --> 58.82]  improvements that made it even easier to use they've got great support for lots of languages
[58.82 --> 63.52]  and test frameworks they integrate with github and bitbucket you can deploy to cloud services like
[63.52 --> 69.18]  heroku and aws and many more and you can get started today by trying out their free plan which includes
[69.18 --> 76.42]  100 builds a month and five private projects use our offer code the changelog podcast to get 20 discount
[76.42 --> 82.76]  on any plan you choose for three months that offer code again is the changelog podcast and you'll get
[82.76 --> 88.18]  20 off any plan you choose for three months head to code ship.com slash the changelog to get started
[88.18 --> 89.80]  and now on to the show
[89.80 --> 98.46]  all right we're back it is it's a good day it's friday right jared that's right it's friday so that
[98.46 --> 104.42]  means we record this show and we've got an awesome guest today long time in the making taylor we we had
[104.42 --> 111.10]  to uh reschedule once you had you had some you had a cold or something like that and then then we wanted
[111.10 --> 116.18]  to get you back on this show back in november but taylor otwell's here we're talking about laravel
[116.18 --> 125.06]  uh awesome php framework so taylor welcome to the show thanks for having me and uh i i know that uh
[125.06 --> 130.10]  some news for those who probably are really close to you know this but you've recently gone full-time
[130.10 --> 137.54]  into laravel i have i recently went full-time um starting january 1st basically i work on laravel
[137.54 --> 142.56]  full-time and then also you know laravel forge which is kind of a counterpart product uh supporting
[142.56 --> 147.76]  product to laravel so yeah it's been a blast it's been really cool and i guess for the listeners out
[147.76 --> 152.66]  there who may not know who you are give an intro to yourself and then uh from there we'll go into
[152.66 --> 160.32]  to kind of explain what laravel is at the deeper parts okay so um i'm of course taylor i'm i grew up
[160.32 --> 163.66]  in arkansas and i still live in arkansas in the central part of the united states
[163.66 --> 170.42]  and i've kind of always been into you know tech and computer since i was a kid and majored in um
[170.42 --> 177.68]  it at arkansas tech university and then i actually worked in the dot net field for um i guess three or
[177.68 --> 183.22]  four years for a large trucking company here in arkansas and that's where i kind of got my programming
[183.22 --> 189.38]  chops really and worked with some some really bright programmers and learned a lot and then i got into php
[189.38 --> 194.00]  because i kind of had some side project ideas that i wanted to flesh out some businesses
[194.00 --> 199.90]  and php is of course super easy to host and throw up on a server and it's really great for kind of
[199.90 --> 205.62]  uh rapidly hacking something like that out so uh that's kind of how i got into php just dabbling
[205.62 --> 211.82]  like that and then eventually brought um some of my ideas from dot net over and created laravel this
[211.82 --> 219.08]  this php web framework laravel is it so when i say laravel should i enunciate the l at the at the end of
[219.08 --> 224.90]  that a bit better i say laravel laravel just like that what about you jerry how do you say it i say
[224.90 --> 231.32]  laravel laravel so i'm the only one who's wrong here jeez i just follow taylor man all right he gets
[231.32 --> 235.76]  to he gets to have final say on that the audience is used to it though right i mean i'm always
[235.76 --> 240.72]  mispronouncing something like olivier lacan i just couldn't get that right during the show and
[240.72 --> 246.86]  it's just even now i can't enunciate it once later you would you you just have to mispronounce
[246.86 --> 252.26]  that month later sometimes i go to tech conferences and it's like i try to pronounce things in this
[252.26 --> 256.56]  weird general way so that i don't i don't sound stupid you know if i'm not pronouncing it right
[256.56 --> 261.64]  right i try to cover both bases so to speak and the pre-show we talked about sarah goldman uh being
[261.64 --> 267.54]  on the show recently talking about the php spec and hhvm over there facebook and whatnot but on that
[267.54 --> 274.18]  show we had a conversation about whether or not it was called oscon or oscon mm-hmm gotcha still don't
[274.18 --> 279.62]  know yeah we're still out we'll have to get tim on the on the call to see we can get a an official
[279.62 --> 286.94]  ruling here or something on laravel's home page it says the php framework for web artisans
[286.94 --> 294.46]  can you explain to us what a web artisan is so web artisan is kind of just a fun little marketing
[294.46 --> 300.56]  word we use and i think of it a lot like um you know the software craftsmanship type of movement so
[300.56 --> 306.70]  it's really supposed to mean the same thing um it's laravel is built for people it's built with
[306.70 --> 312.10]  a lot of care i guess you could say and we really sweat the details in terms of how easy it is to use
[312.10 --> 317.48]  what the api looks like uh we try to make the documentation really good try to put a lot of care
[317.48 --> 324.18]  kind of handcraftedness into the product so it's not supposed to be like elitist or it's only for
[324.18 --> 330.02]  really good programmers or whatever it's more just saying hey we really care about good code if you
[330.02 --> 334.74]  care about that kind of thing too maybe you'll like laravel so uh that's kind of the thought
[334.74 --> 341.28]  behind it kind of the software craftsman slash artisan feel you find that that has set you apart
[341.28 --> 348.24]  a little bit in the php community i think it's i think people um you know it kind of creates this
[348.24 --> 353.24]  this fun community and people like to be a part of something you know what i mean like to feel like
[353.24 --> 359.94]  they're a part of some kind of club or movement or fun thing and i think it has benefited to kind of
[359.94 --> 364.98]  have um those kind of marketing angles on the framework and it kind of does set it apart
[364.98 --> 371.70]  in people's minds at least from a marketing perspective of this cool inner circle you're a
[371.70 --> 380.20]  part of of laravel developers yeah i mean also you know php is one of those languages that has such
[380.20 --> 386.74]  broad use and has been around for such a long time that there's a lot of really bad php code on the
[386.74 --> 391.06]  internet you know it's kind of like javascript in that way every language there's bad code out there
[391.06 --> 397.60]  but you know some of them kind of come up to the top of just having a lot of code out there that
[397.60 --> 404.20]  because it's so easy to get into yeah um it's easy to to publish your kind of newbie code that being
[404.20 --> 409.32]  said there's a lot of php developers like you like yourself who really care about code quality
[409.32 --> 415.14]  who consider themselves more craftsmen and so i think it makes a lot of sense to have tooling
[415.14 --> 423.18]  specifically tailored at these people right no uh no pun intended huh yeah i've i've said you saw
[423.18 --> 429.46]  what i did there i saw that i like that it's good i've said in the past that i feel like php sort of
[429.46 --> 434.68]  has this copy paste culture that we're we're trying to get out of where like you said there's a ton of
[434.68 --> 440.48]  um there's i mean there's whole websites devoted to basically copying and pasting bits of php into
[440.48 --> 446.62]  your application and we're kind of got this uh we've been playing catch-up so to speak where we're
[446.62 --> 453.34]  trying to talk about things like good architecture good design and at the same time um i like to bring
[453.34 --> 458.44]  a lot of kind of the rails flavor in of rapid application development and making things very
[458.44 --> 463.78]  practical and pragmatic um so yeah we've been playing catch-up quite a bit but i feel like php
[463.78 --> 469.02]  has really gained a lot of ground in the past few years how long have you been doing laravel
[469.02 --> 478.26]  i wrote laravel it released in june of 2011 so coming up on four years now wow and how many
[478.26 --> 484.36]  uh major versions has that been we just released our fifth version and they've been getting farther
[484.36 --> 489.42]  apart like the first couple versions were really close together because we it was almost all early
[489.42 --> 494.54]  adopters you know kind of hacker types and we didn't really care about stuff breaking somewhat
[494.54 --> 499.16]  frequently so we came out with version one two and three really close together and then version four
[499.16 --> 503.96]  and five have been um a little over a year and a half apart coming up on two years apart so they've
[503.96 --> 513.86]  been spreading out yeah over 14 000 stars uh 4 600 forks on github so you've definitely um succeeded
[513.86 --> 521.00]  where many uh frameworks and communities fail to to gain a large audience can you can you speak to
[521.00 --> 527.24]  why you think that is yeah i have a few um a few reasons i think that laravel has kind of taken off
[527.24 --> 531.74]  that way and one is from the very beginning i kind of made this promise to myself that i would never
[531.74 --> 536.54]  release any version of laravel without good documentation i just like wouldn't do it i don't
[536.54 --> 542.00]  even release betas if they don't have good documentation because you i mean you only have
[542.00 --> 546.66]  so long to really capture people's attention you know or and give them either like a good experience
[546.66 --> 552.34]  or a really frustrating experience and in terms of frameworks there are php frameworks out there that
[552.34 --> 557.64]  still to this day i'm not really sure like how do i log someone in like it's just not clear to do
[557.64 --> 563.78]  something that basic that almost every website needs to do so with laravel i tried to have awesome
[563.78 --> 569.52]  documentation from day one and then also have a really great community so from the day we launched
[569.52 --> 575.04]  i personally was in the forums in the chat rooms and i'm still in the chat rooms a lot talking with people
[575.04 --> 582.44]  and really engaging the community to make it feel um more inclusive and tight-knit and it draws people
[582.44 --> 586.00]  in and they feel like they're a part of something they're a part of something that they can
[586.00 --> 591.48]  learn from and they can get help from others and even help others themselves so yeah the documentation
[591.48 --> 596.52]  the community have been huge and then that ties into things like laracast and of course all the
[596.52 --> 604.30]  surrounding ecosystem of educational materials so i guess uh to rewind a tiny tiny bit bring us
[604.30 --> 613.14]  up to speed on exactly what laravel is then okay so laravel is a lot of people probably think of it
[613.14 --> 618.42]  as the rails of php um that's probably the easiest way to think of it if you're not really a php developer
[618.42 --> 625.00]  it's it's really railsy in the sense that it has an active record orm uh that's that feels very much
[625.00 --> 632.20]  like rails after active record it also has um it's also had features um that not many other frameworks
[632.20 --> 637.50]  have or that rails just got like we've had queuing a queuing system for uh over a year now
[637.50 --> 644.72]  with several different backends for beanstalk and aws and iron mq it has a cli much like rails where
[644.72 --> 649.82]  you can just do laravel new blog and start a new project and you can generate migrations just like
[649.82 --> 655.30]  rails and the migrations even look like rails so it's very uh very much rails inspired development
[655.30 --> 662.04]  framework for php and then also mixes in a lot of unique stuff the templating engine is called blade and
[662.04 --> 669.64]  is more inspired by dot net than than rails i would say so uh the whole goal of it is to let's build a
[669.64 --> 675.08]  really productive web framework for for rapidly developing your ideas and getting them out to the
[675.08 --> 681.66]  world as quickly as possible and making them at the same time maintainable and testable and you know a
[681.66 --> 688.18]  joy to develop for tell us about blade um i know it's hard to describe code a little bit just with words
[688.18 --> 697.06]  but if you can what what makes it unique from a typical embedded uh templating system so blade is
[697.06 --> 702.56]  really unique because it's very very minimal under the hood um there are other templating systems for
[702.56 --> 710.46]  php like twig which actually convert your template into a fairly complicated php class that then renders
[710.46 --> 718.16]  the html blade is significantly different in that it's really just a handful of regular expressions
[718.16 --> 724.40]  that translate your template into raw php which is you know compiled and stored and then it's
[724.40 --> 732.38]  processed as raw php the next time the view is needed but it's very much um inspired by asp.net mvc
[732.38 --> 737.02]  razor and in fact that's where the blade name comes from so you're going to see very familiar syntax
[737.02 --> 743.54]  where you have like you know at sign if or at sign for each instead of having to do you know bracket
[743.54 --> 751.36]  question mark php all that jazz and then of course it has a kind of template inheritance where you can
[751.36 --> 756.98]  define a master layout and then extend that layout for your child pages and such you know that old
[756.98 --> 762.06]  saying about regular expressions right right yeah you ran i've got i've got two problems yeah you run
[762.06 --> 769.70]  into issues uh with that that those internals what's the what's the what's the saying uh a programmer
[769.70 --> 775.40]  when tasked with a problem thought to himself i know i'll use regular expressions now he has two
[775.40 --> 782.24]  problems kind of the old joke yeah we haven't thankfully i mean blade is pretty simple so we
[782.24 --> 788.58]  haven't really had a lot of problems there uh hopefully we don't yeah i am familiar with that warning
[788.58 --> 797.16]  you give it the uh the rails nod there i suppose right so you're on version five you've been at this
[797.16 --> 803.46]  for what i think you said four years now is that right yeah four years so take us back to i guess
[803.46 --> 810.14]  the php framework landscape at that time what were some of the problems you're trying to solve
[810.14 --> 816.30]  and what were some of the early beginnings that made laravel what it is i guess then and then now
[816.30 --> 822.68]  today okay yeah i'll just i'll just talk really honestly about the php framework landscape back then
[822.68 --> 828.50]  because it's changed quite a bit uh the big players back then in terms of frameworks um were
[828.50 --> 836.60]  code igniter kohana and symphony and i would say code igniter and kohana are basically becoming
[836.60 --> 843.28]  irrelevant now but the the issue was um at php at the time there was really not a large framework
[843.28 --> 851.24]  that was simple and that embraced the newest php features so code igniter was simple as a framework
[851.24 --> 856.36]  it was easy to use it had great documentation but it was like woefully out of date in terms of what
[856.36 --> 862.26]  php could do for instance php had um anonymous functions you know you could um you could pass
[862.26 --> 866.64]  functions around as first class citizens and that makes for a really good routing system where you can
[866.64 --> 872.22]  just say route get slash home and then pass it a function that is called you know kind of like a
[872.22 --> 880.30]  sinatra or something like that and so we needed a really nice modern framework that embraced what php
[880.30 --> 887.40]  was and what modern php was and laravel i i really think laravel was at the right place at the right
[887.40 --> 894.14]  time in that sense in that i was able to come in right when php had these great features these other
[894.14 --> 900.36]  frameworks were kind of getting dated and old and the newcomers were ignoring things like documentation
[900.36 --> 905.52]  and community and so i tried to come in and bring in a modern framework with modern php
[905.52 --> 912.90]  which in laravel one was very much uh sinatra inspired more than rails inspired and to and
[912.90 --> 917.34]  fill that gap of having a great modern framework with really good documentation that's easy for
[917.34 --> 926.16]  people to use and rapidly build things you mentioned rails and um we had last week uh rob aurelia
[926.16 --> 933.74]  rob aurelia his project's called aurelia uh rob eisenberg on the show um yeah the eisenberg effect
[933.74 --> 940.86]  and he was talking about one of the things that he believes that came out of the rails mindset which
[940.86 --> 948.24]  is that um you know quality frameworks um maintain their quality and their usefulness when they're
[948.24 --> 954.96]  abstracted or extracted from production applications or built alongside production applications um you
[954.96 --> 961.38]  know rails famously pulled out of base camp rob's last framework durandal had a production application i
[961.38 --> 967.20]  can't recall that he built it alongside did you have that with laravel from the beginning do you have
[967.20 --> 974.64]  it now what's the situation with production apps yeah i had it very early on into laravel um i didn't
[974.64 --> 982.10]  have it in the the very beginning for laravel one but from laravel um two or three on i did have a major
[982.10 --> 987.42]  application that laravel was kind of extracted from and modern laravel really looks a lot different than
[987.42 --> 993.90]  laravel one but that app was a snappy when i worked for a company called userscape we built a help desk
[993.90 --> 1001.12]  application called snappy it's b snappy.com and that used laravel and so many things were extracted
[1001.12 --> 1006.78]  into laravel from what we needed with snappy the queue system was kind of genericized and brought into
[1006.78 --> 1013.46]  laravel all kinds of stuff even the migration system really was was inspired by our needs as a team
[1013.46 --> 1021.06]  at userscape so and i've i've always been terrified of not having a real application i can develop laravel
[1021.06 --> 1028.08]  out of just building laravel in a vacuum is really terrifying to me because i have no i have no compass
[1028.08 --> 1034.32]  so to speak in terms of what what's real and what's just imagined needs you know and with laravel 5
[1034.32 --> 1042.10]  since i work full-time i'm on laravel now i actually built like a whole new sass on laravel 5 just
[1042.10 --> 1048.26]  so i could dog food it in that way and really see how the framework felt and it identified a ton of
[1048.26 --> 1053.74]  like little you know it didn't bring out necessarily like big show-stopping bugs but it identified like a
[1053.74 --> 1058.32]  lot of little paper cut bugs i like to call them where things that are just like annoying when you're
[1058.32 --> 1064.08]  building a real app and you see the edges of the framework so it's it's extremely helpful to have
[1064.08 --> 1068.88]  that kind of thing and i imagine going forward you know over the next few years or whatever the next
[1068.88 --> 1074.32]  version of laravel is i'll build something entirely new just so i can dog food it if i have to
[1074.32 --> 1081.12]  on the bakes on the i'm looking over the docs too by the way love the docs that uh and i like your
[1081.12 --> 1087.40]  principle of of uh not releasing without good docs and you can tell that's a a green didn't principle
[1087.40 --> 1093.46]  for you but um looking over some of the basics the foundations and services you have here where's a
[1093.46 --> 1099.36]  good starting place for kind of covering some of these pieces in terms of architecture the the
[1099.36 --> 1104.88]  service providers are kind of foundational and how they tie into the ioc container um it's that's a
[1104.88 --> 1109.18]  little bit deep of a concept or a little bit you know in the guts of the framework but that's pretty
[1109.18 --> 1117.88]  foundational i would say what's uh what's ioc uh so laravel is driven by the ioc container which is
[1117.88 --> 1124.36]  inversion of control container dependency injection container and it can automatically inject your class
[1124.36 --> 1131.80]  dependencies so that if you have a user controller and maybe you have some kind of user repository class
[1131.80 --> 1137.88]  that abstracts your all your database functions or or methods you need to call you can just type hint
[1137.88 --> 1142.50]  that user repository right on your controller's constructor and the the container will inject it
[1142.50 --> 1146.82]  automatically for you so you don't really have to wire up a bunch of dependencies manually
[1146.82 --> 1154.22]  the um laravel's container can do all that sort of magically for you where was the inspiration for
[1154.22 --> 1161.42]  dependency injection the dependency injection is laravel is really modeled after um microsoft's
[1161.42 --> 1168.66]  unity container and then n inject from the dot net ecosystem you know like i i feel like the
[1168.66 --> 1174.50]  architecture can go a little overboard i kind of agree with um with some of the things dhh said
[1174.50 --> 1180.56]  recently in terms of architecture and kind of over architecting things but uh so the container tries
[1180.56 --> 1185.84]  to it doesn't kind of like dominate your life in laravel but it's a really helpful tool if you need to
[1185.84 --> 1191.46]  abstract some pieces out of your application and kind of separate layers of your application for unit
[1191.46 --> 1198.10]  testing or whatever gotcha as a quick plug i think we got dhh coming up on an upcoming show is that right
[1198.10 --> 1203.40]  adam i was wondering if we should mention that i i kind of hesitated to do so but yeah um for those
[1203.40 --> 1211.22]  listening now we do have an awesome show planned with uh dhh uh also known as david heimer Hanson
[1211.22 --> 1219.38]  the show is going to be all about 10 plus years of rails we hope that's a pretty awesome conversation i
[1219.38 --> 1223.56]  know that i've got about a thousand things i want to ask him i'm sure you're you're the same jared so
[1223.56 --> 1227.68]  but yeah he's always got something interesting to say doesn't he at tip to the future that's
[1227.68 --> 1231.68]  february 20th we're recording probably a week after that on the shipping and yeah he's always
[1231.68 --> 1241.34]  he's always uh full of good stuff so and now a word from our sponsor top towel is the best place to
[1241.34 --> 1246.54]  work as a freelance software developer if you're freelancing right now as a software developer and
[1246.54 --> 1252.08]  you're looking for a way to work with top clients on projects that are interesting challenging and using
[1252.08 --> 1258.06]  the technologies you want to use top towel might just be the place for you working as a freelance
[1258.06 --> 1263.02]  software developer with top towel your days of searching for high quality long-term work and
[1263.02 --> 1267.82]  getting paid with your worth will be over let's face it you're an awesome developer and you deserve
[1267.82 --> 1272.76]  to be compensated like one joining top top means that you'll have the opportunity to travel the world
[1272.76 --> 1278.98]  as an elite freelancer on top of that top talk and help provide the software hardware and support
[1278.98 --> 1284.46]  you need to work effectively no matter where you are head to top towel.com slash developers that's
[1284.46 --> 1290.60]  t-o-p-t-a-l.com slash developers to learn more and tell them the changelog sent you
[1290.60 --> 1296.42]  but taylor any other specific features so you have an orm you have routing dependency injection
[1296.42 --> 1302.82]  you have kind of a unique uh at least internally unique view layer um any other major features of
[1302.82 --> 1308.88]  laravel you got command line uh generators that you that are you know big tentpole
[1308.88 --> 1312.20]  features that you definitely want people to know about before we move on to other topics
[1312.20 --> 1319.14]  uh the queuing system is huge uh in php frameworks nothing like that exists in any other framework and
[1319.14 --> 1325.24]  basically i really like it because it's super easy to use so i can i can go to my command line and say
[1325.24 --> 1331.60]  make command purchase podcast maybe some purchase podcast routine that i'm going to run and then on
[1331.60 --> 1336.66]  that class i can just say should be queued i can just mark it with an interface that reads very much
[1336.66 --> 1341.60]  like you know english just should be queued and then when i dispatch that command it's automatically
[1341.60 --> 1348.26]  sent out to the queue and my eloquent models are serialized and deserialized gracefully
[1348.26 --> 1354.16]  and everything is just super easy to use and i find that's you really need that in most web
[1354.16 --> 1359.36]  applications you build nowadays it feels like to me some kind of good queuing system and laravel's
[1359.36 --> 1368.02]  unique in that regard in php yeah for sure uh what about deployment uh build process uh javascript
[1368.02 --> 1374.68]  integration stuff like that yeah so we actually have a tool called laravel elixir which is sort of a
[1374.68 --> 1381.68]  it's kind of sort of a fluent layer on top of gulp where um we abstract out quite a bit of the
[1381.68 --> 1387.22]  hairiness of writing your own gulp file and so you can just say elixir mix sass and give it your
[1387.22 --> 1392.50]  sass file or less or coffee script or whatever and it's like super clean i mean even just like a
[1392.50 --> 1398.68]  10 line file i can do my sass i can have it automatically run my tests when i change my
[1398.68 --> 1404.84]  test files and i can have it version my files so that the cache busts and all that so it's really
[1404.84 --> 1409.58]  slick but that's a that's a new feature in laravel 5 and kind of a kind of an add-on feature is that
[1409.58 --> 1415.86]  that gulp integration is there a reason why uh i guess is it just to maintain writing php versus
[1415.86 --> 1423.94]  go into davascript like why didn't we use a php compiler basically why didn't you just do it
[1423.94 --> 1430.10]  straight in gulp like a layer on top of it yeah it is built on top of gulp and we found that
[1430.10 --> 1438.56]  php the php community is um gosh it's hard to say it nicely but we're just behind in some ways
[1438.56 --> 1445.34]  and it's very hard to throw people right into gulp like for our a lot of our users and so this is kind
[1445.34 --> 1450.14]  of a nice way to get them into gulp and get them kind of believing in themselves like hey i can use
[1450.14 --> 1455.64]  javascript build tools cool and then they start digging into it more and they find out oh i can
[1455.64 --> 1461.90]  i can write my own gulp task in this file and drop down into all the all the gulp goodies i want it's
[1461.90 --> 1466.20]  kind of a good way to get their feet wet and get their feet in the door whereas they might not have
[1466.20 --> 1470.42]  they might have felt overwhelmed or might have been scared to try something like that um had they not
[1470.42 --> 1476.16]  had a softer easier introduction to the whole the whole scene how easy is it to layer on like
[1476.16 --> 1481.36]  a front-end framework something and like things like bootstrap or just various things that are out
[1481.36 --> 1489.40]  there that uh you know integration with less or sass and those pieces how easy is it to put something
[1489.40 --> 1496.90]  i guess an interface on top of uh you know a level app uh it's fairly easy you know it's pretty
[1496.90 --> 1502.06]  straightforward a lot of people just use bauer or whatever to install whatever they want you know
[1502.06 --> 1507.56]  we we haven't tried to get too opinionated with that out of the box we don't really um ship any
[1507.56 --> 1512.98]  any particular front-end framework besides you know the gulp tooling but uh yeah it's pretty
[1512.98 --> 1517.08]  straightforward like you would expect for any other any other web app really do you have anything like
[1517.08 --> 1523.78]  the asset pipeline like there is in rails and and whatnot there are community asset pipelines that
[1523.78 --> 1528.98]  have been built that kind of mimic that functionality for the for the laravel core itself we stuck with
[1528.98 --> 1536.32]  just the the gulp slash elixir um integration because it's a lot simpler to build um first of all
[1536.32 --> 1542.64]  and then the asset pipeline it was so opinionated and there were so many um you know some people loved
[1542.64 --> 1547.06]  it and some people just absolutely loathed it and so we were very hesitant to bring that in after
[1547.06 --> 1550.88]  seeing kind of some of the reaction from the ruby community so we took kind of the more
[1550.88 --> 1555.98]  conservative conservative approach with kind of a simple gulp file to help you get started with
[1555.98 --> 1562.10]  asset compilation what about the you mentioned a template language earlier for the views how does
[1562.10 --> 1566.96]  that work i know that in the rails world you tend to have camps there's somebody who keeps the erb
[1566.96 --> 1571.68]  someone who goes with hamil someone that goes with something else what what else is out there now
[1571.68 --> 1578.42]  jared besides erb and hamil uh slim maybe slim okay so what's it like when when you come into
[1578.42 --> 1585.04]  laravel so you can you can take your pick like that sort of most probably 99 of people are just
[1585.04 --> 1590.16]  sticking with blade the default engine but other people have right wrote engines for um you know
[1590.16 --> 1595.48]  php has hamil parsers as well and uh there's another parser called twig which i think is based
[1595.48 --> 1602.62]  off some kind of python uh templating language jenga maybe so you can swap them out and there are
[1602.62 --> 1606.80]  packages to do that um i don't really do it i think most people probably stick with kind of the
[1606.80 --> 1612.30]  default stuff there's kind of not a really um templating language in general are not very well
[1612.30 --> 1617.14]  received in php interesting uh it's kind of interesting in that way a lot of people just like
[1617.14 --> 1621.92]  to use plain php then we'll like fight over that like php is a templating language why would i need
[1621.92 --> 1627.60]  any other templating language um so but yeah kind of an interesting argument in php
[1627.60 --> 1631.92]  so you kind of have two sides you got you know pulling in assets and then you have
[1631.92 --> 1637.16]  the the people who want to have a separate front end app all together with our javascript frameworks
[1637.16 --> 1644.70]  so in that case how does laravel play if you just want to have uh an api back end laravel is really
[1644.70 --> 1650.76]  awesome that's one of the best use cases for laravel i feel like because it's so easy to convert the
[1650.76 --> 1658.78]  eloquent models into json that setting up a json back end is just it's really just pretty painless in
[1658.78 --> 1664.24]  laravel and other other frameworks and orms and php are not like that at all it's very difficult
[1664.24 --> 1670.86]  to convert um something like doctrine entities into json it's just not as straightforward so i i use
[1670.86 --> 1675.32]  laravel for that a lot actually because i do quite a bit of angular in my own projects and forge is a
[1675.32 --> 1681.28]  heavy um angular project and most of the laravel app i would say is just serving up json and it's it's
[1681.28 --> 1685.78]  really great for that because the orm suits it really well and that was kind of that was intentional
[1685.78 --> 1692.38]  you know even a few years ago it was very obvious that these json backends were going to be extremely
[1692.38 --> 1698.38]  popular and maybe even more popular than you know your typical template back end templating system
[1698.38 --> 1704.94]  so we always have tried to make the api building super easy right uh right about now it's probably a
[1704.94 --> 1710.02]  good time to mention i guess laracast by by way of talking about composer i was pretty excited to
[1710.02 --> 1716.12]  stumble upon the fundamentals for laravel 5 being completely free so big shout out there to
[1716.12 --> 1724.80]  laracast but uh composer is the dependency manager for php uh again jared and i aren't php developers
[1724.80 --> 1729.36]  but kind of walk us through that we're norms to say bundler for example in the review world
[1729.36 --> 1736.14]  um how does this play into laravel yeah composer feels um it's a lot like bundler it's a lot like npm
[1736.14 --> 1740.90]  if you're familiar with that and node so you you would just have like a require block just like
[1740.90 --> 1745.52]  you really do an npm and you list out your php packages that you wanted to pull in and instead
[1745.52 --> 1750.44]  of pulling into node modules it would pull it into a folder called vendor and all the php code would be
[1750.44 --> 1756.10]  in there and and all that jazz so it works very similar to that but that was huge for php that's
[1756.10 --> 1760.74]  probably one of the biggest php developments really over the last five or six years was getting
[1760.74 --> 1766.42]  something that would let us easily distribute code and package form because we we did not have a very
[1766.42 --> 1771.52]  clean way to do that before before that and that kind of churned the whole ecosystem and kind of
[1771.52 --> 1777.58]  revitalized people into writing and sharing open source php code all the packages are shared at package
[1777.58 --> 1788.02]  a gist.org um so that's you know if you go to get composer.org you got browser or sorry browse packages
[1788.02 --> 1794.62]  so since you mentioned npm that sort of makes you and throwing no stones here of course but just
[1794.62 --> 1799.54]  like you said speaking plainly here in some cases but kind of makes you really have some respect for
[1799.54 --> 1806.62]  what npm's done for the just dependency management of packages because the front end to npm in comparison
[1806.62 --> 1813.66]  to this is sort of night and day yeah for sure well maybe we should talk about a little bit more
[1813.66 --> 1817.64]  about your community and more about how you're making a living man because you're you're full
[1817.64 --> 1822.30]  time now that's true yeah full time you keep you do keep saying we which i like yes you obviously are
[1822.30 --> 1827.44]  not you're not you're not the only committer on this project i i hope um seems like it's you got a
[1827.44 --> 1833.18]  nice community going so tell us who all's involved besides just yourself and then follow up with that on
[1833.18 --> 1840.64]  how you're actually going to make a living ongoing okay so the laravel in terms of the code base
[1840.64 --> 1846.36]  i make most of the commits on the code base however there is sort of an inner circle of laravel
[1846.36 --> 1853.64]  community members like jeffrey way uh people that i have worked with in the past a guy named dale
[1853.64 --> 1859.80]  reese in england and all these people we kind of collaborate on laravel ideas and then of course
[1859.80 --> 1864.88]  we have tons of community members on github issues and pull requests commenting and giving their feedback
[1864.88 --> 1870.54]  and our irc channels and so forth so even though i write the majority of the code a lot of the
[1870.54 --> 1876.08]  features are discussed and kind of ironed out beforehand by the community or um you know
[1876.26 --> 1883.52]  in irc or whatever in terms of um you know making a living you know i didn't want to charge
[1883.52 --> 1887.70]  have some kind of premium laravel right that would that would feel kind of weird and i don't think
[1887.70 --> 1892.62]  would be well received so what i did was come up with this idea called laravel forge where
[1892.62 --> 1898.48]  it's sort of like a poor man's heroku in a way where it links to your digital ocean or your
[1898.48 --> 1904.88]  linode account and it provisions the whole server with php and nginx and memcached and redis and
[1904.88 --> 1911.08]  everything you would need really to build a nice php app and then it has deployment tools where you
[1911.08 --> 1917.08]  get kind of the heroku style push to deploy when you push your git repository you can add environment
[1917.08 --> 1923.16]  variables and even set up ssl and subdomains and all that jazz you can do through forge and that's
[1923.16 --> 1928.56]  that's ten dollars a month for the basic plan so it's it's really affordable because digital oceans
[1928.56 --> 1934.68]  servers are of course pretty affordable it's like uh 20 bucks a month for a two gig ram instance and
[1934.68 --> 1939.92]  then 10 bucks a month for forge and you're really got everything you need to get started so that's
[1939.92 --> 1945.08]  been really well received and php really didn't have anything like that because uh php support on
[1945.08 --> 1950.98]  heroku is of course not as uh fleshed out i would say is the ruby support the default ruby support
[1950.98 --> 1957.44]  i like the idea of this though you also have uh one layer above that too so you have a 10 dollar plan
[1957.44 --> 1963.80]  and a plus plan if i recall correctly wasn't it yeah the plus plan lets you share servers with
[1963.80 --> 1968.44]  teammates so that you can you know share across accounts that's more of like a a business feature
[1968.44 --> 1973.52]  um yeah so it's a really nice setup and then we also came out with this thing at the same time
[1973.52 --> 1980.00]  called laravel homestead which is free and that's a vagrant virtual machine that that basically mirrors
[1980.00 --> 1985.90]  the forge environment so that you can have um your your local environment very much mirroring
[1985.90 --> 1989.90]  your production environment in terms of software and all that and that the goal behind that is
[1989.90 --> 1995.42]  really to make the whole development experience really great from beginning to end or what i say
[1995.42 --> 1999.90]  from download to deploy so we want your local development experience to be really good with
[1999.90 --> 2004.80]  laravel homestead and you don't have to muck around with your your uh you know your os 10 or
[2004.80 --> 2010.44]  whatever installing crap uh through brew a good way to say all that installing crap yeah it's a mess
[2010.44 --> 2016.16]  all that stuff that way yeah yeah so if your homestead gets all jacked up you just delete it and
[2016.16 --> 2020.80]  reprovision the whole thing it takes you know just a couple a couple minutes and so then you know you've
[2020.80 --> 2025.76]  got the download part the homestead the local development all the during your development you've
[2025.76 --> 2030.10]  got all the documentation laracast and then when you're ready to deploy you've got laravel forged so
[2030.10 --> 2034.96]  kind of that whole story is fleshed out from beginning to end in terms of how you're going to
[2034.96 --> 2042.88]  build and launch your php application using laravel so did you have this out and we're making money
[2042.88 --> 2048.84]  uh prior to january or are you hoping this takes off uh is this gonna is this already supporting you
[2048.84 --> 2055.76]  yeah this is already supporting me so i launched forge i launched forge in may and i i worked um for
[2055.76 --> 2062.72]  userscape for the rest of uh 2014 basically and forge was out there and making money and and really
[2062.72 --> 2068.60]  had um what could have supported me a lot earlier i just hadn't gone a full-time yet i actually went
[2068.60 --> 2073.38]  part-time at userscape in august so a couple months after forge came out i only worked every other week
[2073.38 --> 2080.64]  for userscape and then in between weeks i worked on laravel nice and you decided to make the the full-time
[2080.64 --> 2085.36]  jump how have you how have you reacted to that decision here i guess you're only about a month in
[2085.36 --> 2091.10]  yeah i i love it so far i mean it's just insane how much more i can get done on the framework i mean
[2091.10 --> 2096.22]  even back when i before i was full-time even just like a full day to work on the framework because
[2096.22 --> 2103.80]  my boss uh gave me um every friday to work on laravel and that was huge back then just to have
[2103.80 --> 2108.66]  one full day to work on open source it was insane the amount of pull requests and issues you could go
[2108.66 --> 2114.12]  through so to have five days a week of that is you know pretty unbelievable i'm really thankful for it
[2114.12 --> 2119.04]  it's allowed you know it's going to ensure a bright future for the framework i think having someone
[2119.04 --> 2127.22]  that can devote this much time to it every week and now a word from our sponsor clearbit is a new
[2127.22 --> 2133.24]  company that builds business intelligence apis friend of the show and past guest on the show
[2133.24 --> 2139.16]  alex mccall if you want to go back and listen to that show it's episode 71 by the way he runs clearbit
[2139.16 --> 2144.16]  and they offer a collection of powerful apis designed to help your business grow specifically
[2144.16 --> 2148.98]  they have one api that takes an email address and returns related social information such as
[2148.98 --> 2154.94]  the person's name title social accounts like twitter and facebook they also provide an api that looks up
[2154.94 --> 2161.44]  company information via a domain name they return attributes like company name location category head
[2161.44 --> 2165.54]  count now there's lots of use cases for both these apis but they're especially awesome
[2165.54 --> 2170.18]  for finding out more information about your customers and their companies for example clearbit
[2170.18 --> 2175.00]  has an alert triggered whenever a high profile customer signs up and their metric for someone
[2175.00 --> 2179.88]  that might be high profile for them is a startup that has recently raised money if you want to learn
[2179.88 --> 2184.72]  more about the powerful apis they offer head to clearbit.com and tell them the changelog sent you
[2184.72 --> 2194.58]  can you talk uh a bit about your choice of vagrant and homestead and i guess the i mean you already
[2194.58 --> 2201.42]  said the crap part of that but you know some use a mamp i guess can you talk about the the idea of
[2201.42 --> 2207.10]  vagrant i guess in this scenario because it's not a norm for php developers to use this
[2207.10 --> 2214.24]  yeah it's uh yeah it's it's yeah it hasn't been in the past i think it's starting to grow now that
[2214.24 --> 2219.60]  people are sort of seeing what it can do um of course so there's there's multiple aspects um
[2219.60 --> 2226.44]  it's difficult to configure setup php and nginx and my sequel especially like on windows i would
[2226.44 --> 2231.38]  say um it was more difficult to get all that set up and then including like memcache and redis
[2231.38 --> 2236.26]  or like a queuing system on windows would be even probably more challenging to set up
[2236.26 --> 2242.22]  and then of course on the mac side it was just for me it was always like it made me nervous to install
[2242.22 --> 2246.14]  a bunch of that stuff because what if i mess it up will i have a good way to reverse it or like
[2246.14 --> 2251.22]  is my system screwed and i just like throw my mac away and get a whole new mac or you know just all
[2251.22 --> 2255.80]  those fears you have of kind of mucking around in the the internals of your system and installing that
[2255.80 --> 2261.18]  kind of software so once i tried out vagrant i hated it at first because i felt like it was kind of like
[2261.18 --> 2266.50]  slow and i had to provision the whole box every time and so like every time i destroyed the box i had
[2266.50 --> 2271.84]  to like reinstall wait for it to install php nginx my sequel and it took quite a while like 10 minutes
[2271.84 --> 2278.22]  and so i hated it at first but then i saw that you could kind of you could kind of build your box
[2278.22 --> 2283.02]  and then store it off and people could use that as a starting point and so that's kind of what gave
[2283.02 --> 2289.20]  me the idea for homestead where when you when it comes down it's already got php and postgres and
[2289.20 --> 2292.72]  redis and all that and then you can install anything else you want on top but that makes the
[2292.72 --> 2299.38]  the provisioning process you know like 10 seconds instead of 10 minutes and so uh and then also you
[2299.38 --> 2303.96]  know like i said just the ability to totally destroy that box and play with it install whatever
[2303.96 --> 2309.18]  you want you know you install elastic search maybe or you install all kinds of node stuff and you can
[2309.18 --> 2313.78]  do whatever you want and if something gets totally screwed up who cares i can just delete the whole box
[2313.78 --> 2319.88]  and have a fresh one in 10 seconds so i don't have to worry about messing up my my mac i like the idea
[2319.88 --> 2326.34]  of vagrant here i know i've been using that for any wordpress sites i still maintain which the changelog is on
[2326.34 --> 2333.88]  on wordpress right now so we spin up i think it's a shout out to vagrant press i believe is what i use
[2333.88 --> 2339.82]  it pretty much mirrors our digital ocean instance and and we're good to go on that on that front and
[2339.82 --> 2346.16]  i like that a lot so it's a it's a good process whereas normally you know you're used to to either
[2346.16 --> 2351.60]  using map or something that's you know gives you less ability to fine-tune like you've done with the
[2351.60 --> 2359.96]  box and having an actually named thing like homestead so um we did kind of get off track there with uh
[2359.96 --> 2366.66]  with that question there about the the money topic there i guess and ford so maybe it makes sense uh
[2366.66 --> 2373.14]  to swing back there and talk about future plans for ford i know that prior to the call in the members
[2373.14 --> 2378.20]  only slack room so a shout out to that as well a lot of shout outs today you know we we just launched
[2378.20 --> 2383.56]  the members only slack room so if you're a member of the changelog if you're a supporting member then
[2383.56 --> 2387.40]  check your inbox you got an invite and if you don't then email us we'll get you in
[2387.40 --> 2396.02]  but before that taylor i asked you about an unofficial forge uh cli and you hinted at some secrecy so is
[2396.02 --> 2401.56]  there anything you could share at all well i'd like to get a forge api out you know which would enable
[2401.56 --> 2406.94]  the community to do a lot more than they can in terms of building cool little tools like that i mean
[2406.94 --> 2411.12]  there are people that have expressed interest in writing you know desktop apps for forge where you
[2411.12 --> 2415.76]  can drag a folder onto your forge app and it launches a server and deploys the app and all that
[2415.76 --> 2421.70]  if i had if i can get a good api out um of course that would enable a lot of that stuff and then
[2421.70 --> 2426.74]  um as i mentioned before you know when i wrote lara 5 i've actually built a whole new sass which i've
[2426.74 --> 2432.24]  actually got you know sitting on my computer and in a private repo on github that uh complements
[2432.24 --> 2438.80]  forge i would say in a way and it's kind of an unrelated field in terms of application deployment
[2438.80 --> 2443.80]  and and launching and all that so i'm going to polish that up in the next few months and
[2443.80 --> 2448.34]  hopefully get it out there soon i think that'll be another cool product that people can use with
[2448.34 --> 2454.20]  their laravel apps and even just generally php apps while we're on the notion of forge how much
[2454.20 --> 2461.32]  of a linchpin is it to the developers using laravel to use forge it's it saves you so much time it
[2461.32 --> 2467.16]  really does um you know a lot of people in the php world over the past few years have been really
[2467.16 --> 2472.02]  locked into shared hosting and that's because they don't feel comfortable configuring their own server
[2472.02 --> 2478.74]  and there was nothing like um a heroku for so long uh for php that people just bought you know this
[2478.74 --> 2483.20]  five dollar a month shared hosting and that had that had a lot of downsides like sometimes you might
[2483.20 --> 2488.74]  not even have terminal access to that host or sometimes they don't have uh redis and you really
[2488.74 --> 2493.38]  want to use redis for this app because you like some of its features and so people have been really
[2493.38 --> 2499.48]  stuck in terms of what they could do with their php apps so to have something that's basically just as
[2499.48 --> 2505.20]  easy as shared hosting and is you know minimally more expensive than shared hosting but that gives
[2505.20 --> 2510.06]  you so much more that you can do in terms of even what kind of database systems you can use
[2510.06 --> 2516.60]  with postgres and and then memcached and beanstalk queues and all that uh it just you know i feel like it's
[2516.60 --> 2520.18]  opened the door for a lot of people to do things that they they wouldn't have felt comfortable doing
[2520.18 --> 2524.52]  and that's kind of what we're all about um for laravel at least is how can we help people turn
[2524.52 --> 2530.48]  their dreams into reality and how can we remove roadblocks from people's development experience so
[2530.48 --> 2535.98]  whether that's gulp with elixir or deployment with forge or server configuration or local development
[2535.98 --> 2540.98]  with homestead how can we get these roadblocks out of the way so that you have a great experience
[2540.98 --> 2546.02]  turning this app id you have into reality and you know making money and supporting your family and all
[2546.02 --> 2553.52]  that good stuff so that's kind of our our overarching goal so you mentioned a future sas product to sort
[2553.52 --> 2560.96]  of complement forge any anything else you could share think of like uh you know what's on the horizon
[2560.96 --> 2565.68]  what's super secret what's something you can share today that's enough but doesn't put you to timelines
[2565.68 --> 2573.84]  or you know we don't expose too much but whatever you can one issue with forge um is that i can't deploy
[2573.84 --> 2580.70]  something like forge with forge because forge has um very simple deployment facilities and that it's
[2580.70 --> 2585.50]  kind of locked to one server it's very limited in terms of what it can do you know when you push when
[2585.50 --> 2589.64]  you push to github it can run a bash script on your one forge server but that's pretty much it
[2589.64 --> 2594.74]  um so i'd like to see something where how can i deploy something like forge
[2594.74 --> 2602.72]  with a product that's as easy as forge to use so um i think there's a pretty good use case there and i
[2602.72 --> 2607.18]  think it's going to be i'm really interested to get it out there but it's going to be yeah it's
[2607.18 --> 2612.04]  going to be interesting it's going to be a great way to deploy php i feel like just looking at your
[2612.04 --> 2616.86]  forge page here i've also been looking at your laravel page and your laracom page and i'm just
[2616.86 --> 2622.58]  thinking these are all really nice designs just on top of it all and then i'm thinking and you also run
[2622.58 --> 2630.66]  this you know this cloud i mean it's not your infrastructure but right you have sys you have sysadmin
[2630.66 --> 2637.34]  skills it appears like do you do all your own designs as well i don't do the designs the you
[2637.34 --> 2641.32]  know i have i've kind of developed a circle of friends you know i was gonna get mad at you for a
[2641.32 --> 2646.08]  second i was like man this guy can do it all yeah i don't do the designs i did the forge um
[2646.08 --> 2650.74]  the internal app design of forge i did do but that's not much more than basic uh bootstrap
[2650.74 --> 2657.24]  customization the front page of laravel a guy named jack mcday did who actually makes a php cms
[2657.24 --> 2663.28]  called statamic which is a flat file cms and he helped me out with that how about laracon because
[2663.28 --> 2669.00]  your laracon site has a really cool uh svg animation at least on desktop as you hit the
[2669.00 --> 2676.66]  laracon us logo so the lara the laracon stuff is actually done by a group in amsterdam i i partner
[2676.66 --> 2683.66]  with a guy named sean mccool um to he does the laracon eu chapter the european laracon and i kind
[2683.66 --> 2688.68]  of manage the u.s uh conference and so we kind of went in together this year on the branding and
[2688.68 --> 2693.20]  the design and split the cost of that so that we could have kind of a unified appearance across both
[2693.20 --> 2700.14]  conferences and so yeah we used a firm in amsterdam to do a lot of that branding i like it that's it's
[2700.14 --> 2708.04]  very hot anytime i see an svg animate i'm just like oh it's awesome anyways um so i guess getting
[2708.04 --> 2712.80]  back to some of these supporting things is this supporting you as well is this profitable i guess
[2712.80 --> 2719.16]  yeah laracon does usually generate a little profit i i couldn't live just on laracon like if forge
[2719.16 --> 2724.76]  collapsed i couldn't keep going just on laracon but uh yeah it turns a little profit and it's nice it is
[2724.76 --> 2729.32]  quite a bit of work of course to to have a conference and get the speakers and you know you
[2729.32 --> 2733.12]  really want to provide a um you know obviously you want to provide a great experience for people
[2733.12 --> 2737.36]  that come to these conferences and there's so many things that could go wrong at a conference so
[2737.36 --> 2742.88]  it is quite a bit of work and and stress but yeah it really goes well and everyone seems to have a
[2742.88 --> 2747.72]  great time the past few years so i'm looking forward to it you mentioned i guess jared mentioned earlier
[2747.72 --> 2752.36]  that you keep saying we and this might be a good time to give a shout out to some people that have
[2752.36 --> 2757.68]  helped you this past four years get to where you're at now so beyond you who else is in the
[2757.68 --> 2762.84]  laravel community making sure you don't go crazy yeah i mean the first person that comes to mind
[2762.84 --> 2767.18]  would be jeffrey way which i mean a lot of laravel success i think has to be credited
[2767.18 --> 2775.48]  to him and he runs laracast of course and i mean this guy has hundreds of videos on how to how to
[2775.48 --> 2779.78]  do modern php and how to do laravel and even really other stuff too like how to do gulp and
[2779.78 --> 2786.56]  some javascript stuff so i mean without that resource laravel i think would not be as far
[2786.56 --> 2791.54]  along as it is so he's definitely the first person that comes to mind to think um and then of course uh
[2791.54 --> 2797.26]  you know my overseas friends with sean who have kind of maintained that community over there and
[2797.26 --> 2801.84]  been leaders in europe in terms of organizing community events and conferences and there are
[2801.84 --> 2807.90]  just so many user groups all around the world um like i just saw um you know the london laravel
[2807.90 --> 2813.68]  meetup has like 50 people every time they meet up and that's a really nice meetup really from
[2813.68 --> 2819.50]  you know kind of a young php framework so there's so many people in the community anyone that writes
[2819.50 --> 2825.20]  these blogs or organizes these meetups i feel like is contributing because they're they're building
[2825.20 --> 2831.80]  a more open and diverse and inclusive community all around the world this might be a good chance for
[2831.80 --> 2841.50]  us to give a shout out to listener justin page who is handle is klvtz on github he uh first pinged us
[2841.50 --> 2847.20]  for a laravel show all the way back in april 23rd so justin thanks for the idea thanks for your
[2847.20 --> 2853.34]  patience and it's been a while since april but here it is uh at the time he had mentioned uh yourself
[2853.34 --> 2858.04]  taylor as well as jeffrey way he also mentioned perhaps a good guess would be a guy named dale
[2858.04 --> 2866.68]  reese he appears to be at least an enthusiast has he been involved yeah dale was super um super
[2866.68 --> 2872.24]  popular with laravel 4 because of his um his code bright book he wrote a really popular laravel book
[2872.24 --> 2879.06]  it's actually the top grossing book on lean pub out of all books wow on lean pub so um it was a
[2879.06 --> 2885.30]  very popular book and he actually because of you know his work in laravel got hired on to what i
[2885.30 --> 2891.00]  believe is the fastest growing startup in the in the uk which is um just park or park at my house
[2891.00 --> 2897.00]  which is kind of like airbnb for parking where people that have an extra parking spot can can
[2897.00 --> 2903.50]  basically rent out their parking spot for for any period of time and that's i mean it's huge like uh
[2903.50 --> 2909.92]  i saw um i think it was many was even building like integration for this thing into their cars
[2909.92 --> 2914.44]  wow over there so yeah it's a pretty big deal that reminds me of something that used to happen around
[2914.44 --> 2919.10]  omaha uh we have the college world series comes here every june which is kind of one of our bigger
[2919.10 --> 2924.30]  events and used to be in the this ballpark that was down by these old small neighborhoods with
[2924.30 --> 2930.66]  small houses with large kind of gravel driveways and no parking at all and uh there was a huge
[2930.66 --> 2938.14]  huge boon around temporarily selling your driveway out um for parking spots for the two weeks of the
[2938.14 --> 2943.92]  college world series and uh then they moved to a stadium kind of in downtown and that whole
[2943.92 --> 2948.80]  neighborhood was very very upset about that but cool idea i could see why it'd definitely take off in
[2948.80 --> 2958.14]  crowded areas just park like that yeah so he's the cto of just park so he is not as um involved i think
[2958.14 --> 2963.06]  he would love to be more involved with laravel 5's release but you know he is you know he's pretty
[2963.06 --> 2970.90]  busy these days um managing the tech side of that startup awesome man well great stuff this sounds like
[2970.90 --> 2975.52]  a huge success and uh we're excited to see where you take it from here we do have a few closing
[2975.52 --> 2980.58]  questions that uh we generally ask and so i guess we'll go to those now uh the first one is who is
[2980.58 --> 2989.50]  your programming hero uh lately it's been i would say dhh the the rails guy um mainly because i think
[2989.50 --> 2995.98]  he's really good at seeing through a lot of bs um from the programming community and kind of calling
[2995.98 --> 3002.74]  things how he sees it and keeping things very practical and easy to use because i mean i always i've laughed at
[3002.74 --> 3008.94]  um you know at one of his keynotes he said basically is the code cleaner easier to read
[3008.94 --> 3014.74]  if not then you know who gives a shit about anything else and uh you know that's something i keep in mind
[3014.74 --> 3019.44]  a lot with laravel in terms of keeping things very nice and expressive and easy to get into
[3019.44 --> 3027.66]  awesome um next one what would be a call to arms or something that you would say directly to the
[3027.66 --> 3031.98]  open source community how they could get involved what they can do with regards to laravel
[3031.98 --> 3038.32]  one of the most valuable things just anyone can do with laravel is if you learn something cool with
[3038.32 --> 3046.14]  laravel or learn something about the framework share it or blog it or make a post or share it at a user
[3046.14 --> 3051.02]  group or even start a user group if there's not one near you because the more of that kind of stuff
[3051.02 --> 3055.56]  that's in the community it makes it even easier for other people to get involved so the more we're all
[3055.56 --> 3060.98]  sharing our knowledge and sharing the way we do things with laravel it just makes the ecosystem
[3060.98 --> 3066.00]  that much bigger and that much brighter and helps bring in even more people so definitely share what
[3066.00 --> 3070.72]  you've learned speak at conferences speak at user groups start user groups that kind of thing
[3070.72 --> 3077.24]  awesome last question this one's kind of more personal about you taylor um if you were not doing
[3077.24 --> 3082.38]  what you're doing now which is you know coding laravel and running forge making a living with your code
[3082.38 --> 3089.84]  what would you be doing instead hmm i've uh you know i've always kind of been interested in like
[3089.84 --> 3095.10]  being like a really high-end car detailer like detailing like ferraris and stuff um and i was
[3095.10 --> 3099.30]  really into that in college um so i would probably do something like really basic like that with my
[3099.30 --> 3104.46]  hands because sometimes i feel like you know i'm in the code so much and in these abstract things like
[3104.46 --> 3110.44]  sometimes just like mowing grass yeah or like detailing a car seems really appealing so i'd probably do
[3110.44 --> 3115.90]  something uh simple like that some kind of simple work that is a first for us for sure i can that
[3115.90 --> 3120.46]  resonates that resonates with me though because i i've told my wife many times that when i retire
[3120.46 --> 3125.00]  or something i just want to be like a mailman i can just like drive around and enjoy the weather
[3125.00 --> 3130.04]  and listen to podcasts all day or i said i'd even be a garbage man which that would suck at certain
[3130.04 --> 3135.64]  points but professional something simple you know when i was in college i had a job uh one summer
[3135.64 --> 3140.20]  mowing soccer fields and it was honestly like one of the best jobs i've ever had it was amazing
[3140.20 --> 3147.58]  those are always fun right that's that's cool though i'd never um i mean i can i can relate
[3147.58 --> 3153.96]  obviously but just didn't expect you to say that uh detail cars but i guess if it's a ferrari
[3153.96 --> 3159.02]  and it's a you know a lot more elegant right yeah exactly would it be your ferrari as a thing
[3159.02 --> 3165.16]  i hope so that would be awesome just i just clean my car all day i clean my ferrari
[3165.16 --> 3170.12]  that's what i do that's what i do for work all right well taylor you know it has been a while
[3170.12 --> 3176.76]  getting on the show definitely excited about what you're doing here i think yeah i don't code php
[3176.76 --> 3182.88]  but you know i knew that we needed to get you on here because we'd heard so much about what you're
[3182.88 --> 3187.74]  doing with laravel and then you mentioned jeffrey and the rest of the community and you know and
[3187.74 --> 3193.44]  obviously uh since april of last year we were getting uh mentioned to to have you on the show and
[3193.44 --> 3199.60]  and get talking about this and i'm just glad we can finally do that um you mentioned digital ocean
[3199.60 --> 3205.00]  uh they are a sponsor of this show but on that note i do want to kind of tag some sponsors before
[3205.00 --> 3211.92]  we close out here we got code chip top towel and clearbit uh sponsoring this show today so with that
[3211.92 --> 3216.02]  fellas let's let's say goodbye all right thanks for having me yeah
[3216.02 --> 3223.92]  you
[3241.92 --> 3253.92]  you
[3253.92 --> 3255.92]  you
[3255.92 --> 3257.92]  you
[3257.92 --> 3259.92]  you
[3259.92 --> 3261.92]  you
