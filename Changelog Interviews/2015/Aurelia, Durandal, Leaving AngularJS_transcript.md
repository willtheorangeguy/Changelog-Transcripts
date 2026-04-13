[0.00 --> 15.02]  welcome back everybody this is the change log and i'm your host adam stekowiak this is episode 140
[15.02 --> 21.68]  today jared and i talked to rob eisenberg about durandal js is joining and leaving the angular
[21.68 --> 27.68]  js team so lots of details there for you and we also talked about aurelia really great conversation
[27.68 --> 33.86]  today with rob today's sponsors are rackspace top towel and code ship we'll tell you a bit more
[33.86 --> 39.50]  about top towel and code ship later in the show but our friends at rackspace are giving away 50 bucks
[39.50 --> 44.98]  a month to anyone who wants it in credit for 12 months to explore their open cloud all you have
[44.98 --> 49.92]  to do is create a free developer plus account to get started dev to dev support so if you've got
[49.92 --> 54.76]  complex questions you can talk directly to their developers who are writing and maintaining their
[54.76 --> 61.94]  sdks and apis all services are included monitoring dns auto scaling orchestration private networking
[61.94 --> 67.64]  message queues and more all for free there's no usage limit so you can use as much as you want your
[67.64 --> 74.44]  only build above and beyond 50 bucks a month free 50 bucks a month in credit 12 months explore the
[74.44 --> 79.82]  open cloud go to the change law.com slash rackspace to get started and now on to the show
[79.82 --> 88.56]  what's up everybody we are back jared here adam there adam say hi to the people hey people and
[88.56 --> 94.68]  we're joined today by rob eisenberg you may know him as the eisenberg effect on twitter you may know him
[94.68 --> 103.54]  as the keeper of durandal js perhaps you know him as the guy who left angular or as the creator of the
[103.54 --> 109.12]  brand new shiny aurelia javascript framework rob thanks for joining us you're welcome glad to be here
[109.12 --> 115.18]  what an introduction i liked it it's good you got you got an effect he's got a lot going on
[115.18 --> 123.84]  right love that handle by the way it's so awesome it really is cool um rob we got lots to talk about
[123.84 --> 129.70]  lots on the plate here but i thought we'd uh start off with a little bit about you who you are and your
[129.70 --> 136.78]  history in the web dev game sure yeah um you know it's it's it's funny actually i started programming
[136.78 --> 143.72]  when i was a kid on my commodore 64 uh which i have many fond memories of and uh in high school
[143.72 --> 151.60]  was sort of when the web started to emerge and i kind of sloughed it off um i was doing like c plus
[151.60 --> 158.60]  plus coding at the time and i just thought that the desktop was the bomb uh and uh it wasn't some
[158.60 --> 163.02]  years later i actually went to college to study music and then uh that turned out to not be the most
[163.02 --> 168.96]  stable of careers and i uh got myself back into to doing software development my first gig was
[168.96 --> 176.18]  writing uh you know web apps in the early 2000s and it was a different different uh mid 2000s
[176.18 --> 181.54]  it was a different world so that's my introduction and i floated back and forth between web development
[181.54 --> 189.08]  and and desktop development on a bunch of different platforms and i did open source uh in the desktop
[189.08 --> 196.04]  world actually um i don't know how familiar your listeners are with uh different microsoft technologies
[196.04 --> 204.92]  but back in 2006 microsoft released something called wpf which was a vector-based declarative ui framework
[204.92 --> 210.10]  and it had data binding and all this kind of stuff and i started building a framework on top of that
[210.10 --> 217.24]  called caliber and that was basically it was brought the rails programming model to windows desktop
[217.24 --> 224.48]  development was kind of the idea uh and a couple years later i presented uh at a big microsoft
[224.48 --> 230.10]  conference called mix about how to build a framework like that for yourself and just a few hundred lines
[230.10 --> 236.26]  of code and that there was so much interest in that that that's been off other open source projects
[236.26 --> 243.10]  one caliber micro which was sort of like a smaller version of my of my caliber and library and in the
[243.10 --> 246.92]  you know events after that someone had just walked up to me and said man that was cool
[246.92 --> 253.38]  wouldn't it be awesome if you could do this kind of thing in html and that was 2010 and so i thought
[253.38 --> 259.24]  that would be cool and so i started playing around with it and i don't know a year or two later um
[259.24 --> 265.66]  i released durandal which was uh you know it's in the same lineage you know i'd sort of started
[265.66 --> 272.12]  in desktop development with these ideas but influenced by rails imagining them for stateful rich client
[272.12 --> 278.52]  development and it evolved through several different open source frameworks in the windows realm and then i tried
[278.52 --> 285.16]  to reimagine it for the web with durandal and then aurelia is really sort of the evolution of all those ideas
[285.16 --> 292.64]  with modern you know kind of the the latest and the greatest if you will of what is available or to be available
[292.64 --> 298.26]  via web tech so that's a that's kind of the story of how i got to this week
[298.26 --> 306.84]  there you go interesting well um i must confess i had not actually even heard of durandal until your
[306.84 --> 312.56]  leaving angular post which i read and and and enjoyed and then we have to give a thanks out to
[312.56 --> 319.62]  listener kevin mcgee who uh hopped into ping and actually suggested this show which we're grateful for
[319.62 --> 325.60]  that kevin in fact he even helped frame up some of the topics and it was uh real useful in that very
[325.60 --> 331.52]  in that in that conversation so thanks kevin a shout out to you um and it seems like durandal which
[331.52 --> 335.74]  you know it's a large ecosystem out there we try to keep our thumb on the pulse but
[335.74 --> 344.34]  stuff slips by you had or have to this day perhaps a loyal kind of a large user base or following
[344.34 --> 351.84]  around durandal um can you tell us what durandal is yeah and you've given them the back history but
[351.84 --> 356.82]  just what does it do for you yeah so durandal like i said kind of came out of this progression of ideas
[356.82 --> 362.48]  that was being inspired by a lot of you know a lot of what happened in the rails community in terms of
[362.48 --> 369.94]  convention over configuration but reimagined for sort of rich apps desktop like apps and things like
[369.94 --> 376.18]  this and so durandal was for really building those kind of apps in the browser um but at the time
[376.18 --> 382.58]  you know i decided not to build the entire framework from scratch so durandal what it what it does that
[382.58 --> 389.24]  was a little bit different was it kind of looked out across the web open source projects at the time
[389.24 --> 397.56]  and said okay what are some of the highly successful stable projects that people are using and can we bring
[397.56 --> 403.76]  them together in an opinionated way and sort of put an application layer on top of it that that makes
[403.76 --> 411.32]  it easy to build this kind of app so what durandal did is actually it took jquery um which was quite
[411.32 --> 417.06]  useful at the time for for you know a variety of things and it took that and combined it with require
[417.06 --> 423.14]  js which provided kind of modularity and module loading and then knockout which we use for data binding and
[423.14 --> 428.74]  we stitch these two these three things together and we put kind of an application life cycle over
[428.74 --> 436.84]  the top of it we put routing on top of it we put ui composition so you could do complex uis that were
[436.84 --> 443.16]  componentized and basically put a thin layer on top of all these libraries and brought them together so
[443.16 --> 449.16]  that if you are coming from using one of these libraries you could feel comfortable but also you are
[449.16 --> 452.52]  going to be building something that was maybe a little bit more complex than what you had previously
[452.52 --> 457.60]  we would bring all the pieces together and and then kind of wrap them up and and put this
[457.60 --> 463.36]  icing on the top to make it really easy for you to build you know single page apps and so durandal was
[463.36 --> 471.32]  in that um it was kind of took that approach to the spa use cases if you will and that actually worked
[471.32 --> 477.50]  very well um and i built a bunch of apps i actually built my own product on top of it which the product
[477.50 --> 482.96]  failed but the framework lived on um you know people we have people that have written or companies
[482.96 --> 488.34]  that have written apps that are a hundred thousand lines you know of javascript code built on durandal
[488.34 --> 493.22]  and they love it and so it was it was very modular you could write very large apps very componentized
[493.22 --> 498.00]  apps you could have large teams working on it so it succeeded very well on a lot of those things
[498.00 --> 504.40]  and people like the developer workflow but it's it's it's shortcoming is was also it's strength
[504.40 --> 510.70]  was also its shortcoming so it was highly dependent on these other libraries and that was great in the
[510.70 --> 515.42]  beginning it proved to be a bit of an issue as things moved over time because we had to we had to
[515.42 --> 522.96]  synchronize with them and we had to uh we hit barriers in terms of what we could do how well we could
[522.96 --> 527.96]  present this application building experience when we had to kind of work with the idiosyncrasse
[527.96 --> 534.70]  of the various libraries underneath them but yeah but uh so durandal probably you know it's not as
[534.70 --> 540.36]  well known as something like angular or ember but as a substantial community and people have built some
[540.36 --> 546.92]  really amazing apps with it and big companies uh and small companies and uh you know just the whole
[546.92 --> 553.14]  breadth i've built with that and it's still still going quite strong um uh something you said in there
[553.14 --> 557.82]  which kind of struck me off a little bit was sort of a tangential as jared says but uh
[557.82 --> 562.92]  important to note is that you said the product failed but the framework lived on yeah imagine if
[562.92 --> 567.78]  that was the same case for rails and base camp like would we still would you still be influenced by
[567.78 --> 575.52]  rails had base camp failed you know uh i would have i would have because the the simplicity of the
[575.52 --> 582.30]  developer experience was what well me personally you know um was what enticed me it just it it made
[582.30 --> 588.02]  sense it was so easy and i'm not a rails developer um funny enough because i because i was in the dot
[588.02 --> 594.18]  net camp but uh we were working at the time with something called monorail which was sort of a dot net
[594.18 --> 598.62]  open source it was an open source project in the dot net land that was inspired by rails and so i
[598.62 --> 604.02]  actually came to rails through that and started looking at all these ideas and at the time i was doing
[604.02 --> 610.50]  desktop development and i wanted that type of a development workflow and experience and simplicity
[610.50 --> 618.38]  for for desktop type apps and that's where kind of all that was the seed of it you know sort of in my
[618.38 --> 623.74]  mind and then it just kind of flowed through each of these different platforms that i i would build on
[623.74 --> 627.78]  you know i would i wanted to bring those ideas to it you know when i came to the web i said you know
[627.78 --> 635.24]  i i want it to be that easy to build these these rich interactive experiences it should be it should
[635.24 --> 640.96]  be that easy it shouldn't it shouldn't be it shouldn't be super super complicated you know um
[640.96 --> 647.66]  so to give a little bit of a of a backstory with regards to angular you said i don't know honestly
[647.66 --> 654.68]  you sideline durandall but you kind of left focus on it about a year ago to focus on angular
[654.68 --> 661.96]  to work with the angular team on angular 2.0 um i'm just curious what durandall's relationship was
[661.96 --> 667.82]  with is with angular from a technical aspect and then how did that whole thing come into fruition did
[667.82 --> 673.46]  you catch their attention did did they reach out to you or vice versa so what happened was um to start
[673.46 --> 678.16]  there um there was crossover between the communities i had some people that had been successful with
[678.16 --> 684.08]  durandall and that were also successful with angular um there are consultants that you know work with a
[684.08 --> 689.86]  variety of technologies but there were things that they really liked about durandall um things about
[689.86 --> 694.38]  life cycle of components and and navigation and different things like that which they felt it
[694.38 --> 701.02]  did much better than angular and uh early last year angular had their first um i think their first
[701.02 --> 707.64]  conference and several of these people with with were at that conference and ended up you know
[707.64 --> 711.54]  sitting down and talking with brad green who runs the angular project and said hey you should
[711.54 --> 716.84]  you should really talk to rob because he's got some good ideas over here and they knew that i was
[716.84 --> 722.32]  working on a next gen stuff and and at that time angular had announced that they were working on some
[722.32 --> 729.76]  next gen stuff so they kind of planted a seed in brad's uh mind there and he contacted me and said hey
[729.76 --> 736.50]  i heard this let's talk and so i sent him a few links at the time i i had i actually had a prototype
[736.50 --> 742.20]  demo video out on vimeo at the time so i sent him a couple couple of videos i sent him links to
[742.20 --> 750.30]  and i said oh and here's durandall js and uh so he checked it all out and you know we we got on google
[750.30 --> 754.58]  hangout and talked for about 15 minutes and then he said you should come work with us so
[754.58 --> 761.60]  uh that's like as an employee of google well you know the offer was made but um that's not really my
[761.60 --> 768.04]  thing so um i so i told him that and he said well we you know we have members on the team that are
[768.04 --> 773.84]  consultants as well they're basically full-time consultants that work on angular so we talked
[773.84 --> 777.68]  and i said well let me think about it and you know i came back a little bit later and said all right
[777.68 --> 782.62]  let's do this and we worked out kind of a you know what we called a probationary period basically
[782.62 --> 788.24]  for both of us uh you know basically to make sure on both sides that it was a good fit and it looked
[788.24 --> 793.54]  like things were working out and so uh we did that and it did look like it was working out and so then
[793.54 --> 799.12]  i kind of announced to the community hey this is what's happening and the idea was basically to
[799.12 --> 804.24]  you know there were some ways in which angular 2.0 looked like it was going to be more similar to
[804.24 --> 811.08]  durandall actually and um and so the idea was to bring over the durandall community into angular 2.0
[811.08 --> 817.72]  and to take as many of my ideas from durandall as possible and bring them into the angular 2.0 codebase
[817.72 --> 826.20]  and and and use that as um you know a catalyst for uh certain changes and and improvements there
[826.20 --> 832.18]  and so that's what that's kind of how it happened and it's and it looked great for a number of months
[832.18 --> 836.40]  and then there was kind of there was kind of a point in time where things started to shift a little
[836.40 --> 844.60]  bit and and i began to doubt um that that it was in the best interests of my community or even my own
[844.60 --> 851.66]  personal you know endeavors in terms of development long term and different things like that and so
[851.66 --> 859.32]  that resulted in my then of course leaving the project which so before we go before you dive into
[859.32 --> 864.68]  that the details around that how was the original community response when you announced that you're
[864.68 --> 870.74]  you know joining the angular team to work on angular 2.0 you had these loyal durandall users
[870.74 --> 875.06]  did they felt were they excited did they feel betrayed was there a mixture of emotions you know
[875.06 --> 880.96]  for the most part it was very very positive um i can only remember maybe one or two you know from
[880.96 --> 885.32]  what i from what i know based off of comments you know on the blog or twitter or whatever there
[885.32 --> 889.98]  were maybe only one or two people that were very upset about this but i think most people thought
[889.98 --> 898.30]  well that's that's great um which is funny because when i when i came back from angular back to durandall
[898.30 --> 907.38]  or and ultimately aurelia i had the same response so so uh so i i don't know but uh but it was
[907.38 --> 914.00]  um it was affirmed by the community at the time so yeah i was reading through some of the comments
[914.00 --> 919.12]  on your leaving angular post and i was surprised to see certain people said they're excited that you're
[919.12 --> 924.54]  leaving angular because they were gonna switch from durandall to angular 2 just because of you right
[924.54 --> 928.76]  but now that you're not involved now they feel relieved that they don't have to do that well
[928.76 --> 934.14]  you know it's funny i told that that kind of that story some people that are working with durandall and
[934.14 --> 939.44]  now looking at aurelia have sort of been with me if you way if you will for the ride since back on
[939.44 --> 946.32]  the windows stuff and uh so they've used by various frameworks over the years because they like the
[946.32 --> 952.52]  kind of the the ideas behind them and they've some of them were had never done web programming at all
[952.52 --> 956.32]  but when durandall appeared it made sense to them because of their past experiences
[956.32 --> 962.54]  with with libraries that i'd written so they they made the leap so to speak um into into the web
[962.54 --> 968.82]  programming world and so a number of people have just kind of been with me if you will uh for this
[968.82 --> 975.26]  whole time so it's just it's pretty cool it's it's fun it's um it's encouraging to me um yeah it's got
[975.26 --> 982.38]  to feel good 122 comments on that on that uh post too so you got some passion behind you whether it's
[982.38 --> 987.74]  positive or negative in terms of you know what's the next course of action whether it's durandall
[987.74 --> 994.76]  back to durandall arelia angular i think this post also came at like a kind of a timely moment
[994.76 --> 1000.36]  for angular because of some of the controversy around 2.0 um this announcement you made was
[1000.36 --> 1007.52]  november 17th 2014 i think it was the previous summer where at ng conf europe where some of the
[1007.52 --> 1013.48]  announcements around 2.0 the back the lack of backwards compatibility um the far you know the
[1013.48 --> 1022.14]  far future uh launch date for for 2.0 caused quite a stir right um what what was some of the stuff you
[1022.14 --> 1026.60]  said like your principles and their principles started to diverge what were some of the things
[1026.60 --> 1034.56]  that were warning signs for you um you know one thing about the way i build frameworks i mean i i guess
[1034.56 --> 1040.64]  i am sort of a framework builder i've done a lot of it but i never ever do it in isolation from a real
[1040.64 --> 1049.46]  world app because i i think that you can make a lot of uh decisions in your you know on your whiteboard
[1049.46 --> 1057.46]  and in your cubicle or whatever that that that look good and that don't really pan out when you try and
[1057.46 --> 1065.38]  build real apps with it so uh and one of those things is that frameworks need to be flexible
[1065.38 --> 1073.32]  because as a consultant over the years every company that i've worked with every product i've
[1073.32 --> 1078.48]  ever worked on there's something different about it you know it may be 80 percent like everything i've
[1078.48 --> 1085.00]  built before but then there's that 20 percent that's completely unique uh obviously their their
[1085.00 --> 1090.48]  business exists for a reason but but usually there's some technical aspect of it that's unique
[1090.48 --> 1097.62]  in some way and what you really hate is when you have chosen a framework to build something
[1097.62 --> 1107.16]  and you do get maybe 50 60 70 80 percent through building it and then you hit some barrier in the
[1107.16 --> 1112.62]  framework that is kind of preventing you from really building what you need to build for the business or
[1112.62 --> 1120.02]  whatnot and so because of my experience um you know doing a lot of consulting and building frameworks
[1120.02 --> 1125.42]  in the midst of that i always try to build frameworks that are extensible or pluggable you know where
[1125.42 --> 1132.08]  pieces can be swapped in and out or where there's specific um what i would call seams maybe in the
[1132.08 --> 1138.96]  framework so that you know the framework matches maybe what your normal development is like in that
[1138.96 --> 1143.70]  sense that 80 percent of the time when you work with the framework you're kind of going with the
[1143.70 --> 1149.12]  flow of the framework and everything works and it makes sense but that 20 percent where there's just
[1149.12 --> 1154.26]  something different you have to do you need to be able to you need to be able to do it and the
[1154.26 --> 1160.60]  framework can't prevent you from doing that and that manifests itself uh based off how the framework
[1160.60 --> 1167.82]  is designed and the overarching thing with angular 2.0 under which all the specifics i don't want to get
[1167.82 --> 1172.34]  into all the specifics because it's it's some small things and some larger things and it could all
[1172.34 --> 1178.58]  change it could all change but at the time the overarching theme in my mind um that sort of
[1178.58 --> 1183.90]  aggregated all those things together was that it felt like angular 2.0 was becoming much more
[1183.90 --> 1189.58]  restrictive in nature and there are good reasons to do that because there is a lot of confusion in the
[1189.58 --> 1193.48]  angular community about what is the right way to do that maybe there's like 10 ways to do something
[1193.48 --> 1201.36]  you know and and so there's definitely a benefit to having a framework where there's only one way to
[1201.36 --> 1207.48]  do anything but in the midst of sort of of trying to do that and to maybe solve some of the performance
[1207.48 --> 1212.86]  issues that they had and address some of the different concerns of the community the way that it was being
[1212.86 --> 1218.98]  handled was producing what in my opinion felt like something that was a bit too restrictive
[1218.98 --> 1225.64]  for my own scenarios even and i was worried that it would be too restrictive for my existing
[1225.64 --> 1230.52]  durandal community that i hope to kind of bring over i wasn't sure that they would be able to bring
[1230.52 --> 1238.24]  over their apps port their apps um and i was just kind of you know going over my year you know
[1238.24 --> 1242.52]  number of several years of experience of building js apps with durandal about the types of things that i
[1242.52 --> 1248.50]  built and the kinds of things i had to do uniquely at each client and i worried that you know this
[1248.50 --> 1254.02]  certain scenarios would just be i want to say that i don't want to say that they would be impossible
[1254.02 --> 1262.76]  because you know javascript is amazingly malleable right so you you can find ways almost one way or
[1262.76 --> 1270.20]  another but it it i was starting to feel like it would be very very hard in some scenarios to accomplish
[1270.20 --> 1276.20]  certain types of things that my community and i was used to doing uh and the types of apps that we were
[1276.20 --> 1283.02]  building and uh so that's a blanket kind of a statement there that kind of encapsulates a bunch of
[1283.02 --> 1289.68]  specific things that were happening uh and eventually that just kind of hit a critical mass and i felt like
[1289.68 --> 1297.18]  you know my own feedback into the process was not necessarily changing minds um or directing anything
[1297.18 --> 1303.38]  uh towards a direction i you know that i really felt strongly about so it just it uh it seemed like
[1303.38 --> 1312.28]  it was time to to leave and it was something i was very you know hesitant to do because my whole
[1312.28 --> 1318.46]  because i really want to i want to bring the community together i mean one of the reasons that i
[1318.46 --> 1323.36]  you know i felt strong about durandal but one of the reasons i wanted to join angulars because i wanted to
[1323.36 --> 1329.16]  try and bring some unification you know there's so many different libraries out there and there's
[1329.16 --> 1334.84]  all this stuff so i i felt pretty strongly about that that was that was a good choice but in the end i
[1334.84 --> 1342.00]  ultimately felt like i no longer believed in the thing i was working on you know um and so that
[1342.00 --> 1348.42]  sort of necessitated i want to say in a moral sense you know but it's sort of for me uh necessitated
[1348.42 --> 1355.24]  returning to my original project and my original community and and picking up where i left off
[1355.24 --> 1359.10]  basically with with some of the prototyping i had been doing and basically saying well
[1359.10 --> 1365.22]  there were some really good ideas back there a year ago when i did this you know these prototypes and
[1365.22 --> 1372.54]  let me uh you know see what happens if i don't sleep for the next few months and just flesh this out
[1372.54 --> 1380.82]  you know and now a word from our sponsor top towel is the best place to work as a freelance software
[1380.82 --> 1385.52]  developer if you're freelancing right now as a software developer and you're looking for a way
[1385.52 --> 1390.84]  to work with top clients on projects that are interesting challenging and using the technologies
[1390.84 --> 1396.72]  you want to use top towel might just be the place for you working as a freelance software developer
[1396.72 --> 1401.76]  with top towel your days of searching for high quality long-term work and getting paid with your
[1401.76 --> 1406.82]  worth will be over let's face it you're an awesome developer and you deserve to be compensated like
[1406.82 --> 1411.76]  one joining top top means that you have the opportunity to travel the world as an elite
[1411.76 --> 1417.74]  freelancer on top of that top talk can help provide the software hardware and support you need to work
[1417.74 --> 1425.30]  effectively no matter where you are head to top towel.com slash developers that's t-o-p-t-a-l.com
[1425.30 --> 1428.70]  slash developers to learn more and tell them the changelog sent you
[1428.70 --> 1436.98]  you also move from a position with Durandal of complete control and ownership to a position of
[1436.98 --> 1441.34]  consultant yes and that was actually something i didn't take into account when i considered that
[1441.34 --> 1445.76]  this was a you know sort of a life lesson for me because even actually as a consultant when i consult
[1445.76 --> 1451.64]  with most companies they bring me on as kind of like the ui expert guy and so i have a lot of authority
[1451.64 --> 1458.36]  uh and decisions and when i joined the angular team i had pretty much no authority you know so it was
[1458.36 --> 1464.66]  something i hadn't accounted for and it was uh you know kind of added to that mix of of going oh
[1464.66 --> 1469.44]  you know i don't own this thing anymore i don't i don't have decision making power or anything like
[1469.44 --> 1477.60]  that and so here i am kind of with a different set of opinions and nothing can really be done you know
[1477.60 --> 1481.92]  is that what you meant by when you said probably naive of me to think that this would work out not
[1481.92 --> 1487.60]  so much contrasting against angular but so much like your own passion for your own work and the
[1487.60 --> 1494.40]  direction of that yes that's more of a criticism of my own um yeah it was like i said it was a life
[1494.40 --> 1498.94]  lesson it was an important lesson i wish it i wish it hadn't happened in the public like that but uh
[1498.94 --> 1505.24]  you know it was it was an important life lesson for me i i hadn't fully considered all aspects
[1505.24 --> 1510.70]  and i hadn't really considered this aspect in terms of ownership and authority and these sorts
[1510.70 --> 1516.50]  of things that that that do play a role some other word you used too is uh was sacrificing you said
[1516.50 --> 1523.06]  you'd sacrificed randos independence as a framework in lieu of the work you would put into angular and
[1523.06 --> 1529.58]  you thought it was a good choice so it's it's kind of nice to see your willingness to try something
[1529.58 --> 1534.80]  especially for the good of the community but it's also i guess to a degree good to see that
[1534.80 --> 1539.78]  you're smart enough to know when to quit so if anybody's read seth godin's the dip even though
[1539.78 --> 1544.56]  you may be a developer that's a phenomenal book to read no matter who you are sometimes the dip is
[1544.56 --> 1549.96]  not worth getting through and i hear you are uh rob that you're smart enough to to say it's time to
[1549.96 --> 1554.64]  quit i don't maybe i don't know we'll see if i made the right choice in the long run right but
[1554.64 --> 1560.58]  it's a hard choice to make i mean it's especially i you know i consult with friends and and people about
[1560.58 --> 1564.44]  this too because when you're in the middle of a situation like that there's a lot of things that
[1564.44 --> 1571.44]  are happening in your mind um you know your own emotions your own connectedness to the various
[1571.44 --> 1576.08]  projects and your own ideas and and hopes and all these kinds of things and then your own career
[1576.08 --> 1582.92]  um you know i've got a wife and kids and all that kind of stuff uh got to pay the bills and all these
[1582.92 --> 1589.08]  things are factoring in and you're going okay um did i make the right choice is it am i too far here am i
[1589.08 --> 1594.64]  or you know is it time to kill it you know i stated to ask was uh was about google though because
[1594.64 --> 1600.48]  i mean angular google is there any sort of a lure to that position was that part of your naivete as
[1600.48 --> 1607.72]  you said i mean to to sort of sacrifice your work on the altar of progressing the community in
[1607.72 --> 1613.62]  angular was there any lure to just the wider community google might help bring what do you
[1613.62 --> 1618.38]  mean by lure in this sense well you know an attraction something that was like a lure kind of
[1618.38 --> 1624.66]  yeah okay yeah the lure your attraction to it not a lure but a lure oh okay i was hearing it i was
[1624.66 --> 1631.54]  thinking lore as in like uh you know fantasy lore oh no but anyways i was trying to make that connection
[1631.54 --> 1639.30]  yes um yeah certainly certainly google has lots of resources i mean um and that's that's very
[1639.30 --> 1645.76]  enticing uh you know it was i'd never been paid to work full-time on open source before
[1645.76 --> 1651.70]  so there was certainly an attraction there there was the attraction for my community of having
[1651.70 --> 1658.52]  a full-time paid development team that would be working on what they were building and all this
[1658.52 --> 1663.88]  all this kinds of stuff so there was definitely that i think that that um sort of overshadowed me
[1663.88 --> 1670.24]  considering the sort of the negative sides which is also that you know google is it's is a business and
[1670.24 --> 1676.86]  has their own concerns independent of you know my ideas of a framework you know they have their own
[1676.86 --> 1681.12]  needs they have their own path and they're going to do their own thing also to a certain degree so
[1681.12 --> 1687.82]  you know there's internal politics and all these kind of things that uh that come into play as well and
[1687.82 --> 1692.74]  so i didn't really consider all that kind of stuff i just kind of looked at uh you know as you say the
[1692.74 --> 1699.04]  alluring things and in leaving i had to i had to weigh those same things on both sides again
[1699.04 --> 1704.34]  and it's part of the reason why i'm actually taking a slightly different approach with the
[1704.34 --> 1710.08]  new framework than i have with previous open sources uh so well i'm glad we timed this uh show
[1710.08 --> 1717.06]  how we did because if we hadn't we could only talk about you know the sadness the bummer of you
[1717.06 --> 1723.98]  leaving angular and we just focus on that but uh we can look ahead just at the end of january
[1723.98 --> 1731.40]  you released your brand new shiny which is aurelia um to pretty good reception it seems people were
[1731.40 --> 1736.54]  quite excited about it um can you tell us about aurelia what's what's new about it what's different
[1736.54 --> 1742.00]  what gets you excited about it yeah so it it follows in the same tradition really of the previous
[1742.00 --> 1749.00]  libraries i've written so a lot of the same concepts concepts uh the approaches development
[1749.00 --> 1757.18]  are very similar but unlike durandal it actually doesn't have any third-party uh dependencies it's
[1757.18 --> 1763.24]  completely uh you know self-contained if you will uh it's only dependencies are really on polyfills which
[1763.24 --> 1770.70]  we you know hope over time will drop away so uh and it's and it's highly modular i think probably more
[1770.70 --> 1777.06]  than any of the other uh comparable apps today it's actually broken into i think about 22 separate
[1777.06 --> 1782.32]  libraries and they're each independent in their own repos are each independently versioned and released
[1782.32 --> 1789.48]  and so we're able to do this because we're built with ecma script 6 which is you know a new kind of a
[1789.48 --> 1795.08]  very important part of aurelia as well and we leverage es6 modules and then we have dependency injection
[1795.08 --> 1800.26]  which we leverage as well so we can have certain kinds of abstractions and you know by leveraging
[1800.26 --> 1806.22]  modern package managers and and here at december and and you know having all these things which are
[1806.22 --> 1811.54]  kind of a part of part of our world now that have actually some of which have emerged only in the last
[1811.54 --> 1818.32]  few years it actually makes it possible to build much much more easy to build if you will a highly
[1818.32 --> 1824.26]  modular library like this so it's a collection of libraries that work together as a unified framework
[1824.26 --> 1828.84]  but a number of them can be used independently you can use some of them on the server
[1828.84 --> 1833.28]  so the dependency injection you can totally just use in an express app or something like that
[1833.28 --> 1838.52]  if you want di but there's other libraries too that you can just use in the browser outside of aurelia
[1838.52 --> 1845.28]  for example it's got a it's got a brand new data binding engine that's i think different than
[1845.28 --> 1851.20]  pretty much all the other binding engines out there because it's it's adaptive in nature so it will
[1851.20 --> 1856.18]  look at a property on an object that you want to observe and it will it'll find the best way to
[1856.18 --> 1861.46]  observe it and if object observe is present and it can use that it will use it you know if it's
[1861.46 --> 1866.98]  simple properties it will use getters and setters if there's no object observed it will and it has a
[1866.98 --> 1871.32]  dirty checking you know implementation that will fall back to if it can't do anything else and it's
[1871.32 --> 1876.60]  pluggable so you can bring other libraries in and and basically teach it how to observe different
[1876.60 --> 1884.34]  types of objects so if you have something like you know backbone models or breeze js or some of the
[1884.34 --> 1888.26]  different data libraries that are out there that kind of have their own way of storing properties
[1888.26 --> 1894.10]  and and raising change notifications you can teach the binding layer about that and it doesn't need
[1894.10 --> 1900.92]  to use dirty checking to observe them it can it can uh you can use the same data binding mechanism to
[1900.92 --> 1905.14]  observe all kinds of different things so that's a really big important new piece and what's nice
[1905.14 --> 1911.06]  about it is because like i said this is a very modular framework the the binding piece is actually
[1911.06 --> 1918.00]  completely decoupled from the templating engine and even the the syntax the the syntax for data binding
[1918.00 --> 1924.18]  is completely decoupled from both of those pieces so we don't expect people will swap those out a lot in
[1924.18 --> 1931.78]  the framework itself but you can imagine somebody that might have a need for data binding and wants to
[1931.78 --> 1937.14]  just take that piece rather than build it and connect it into something else entirely and in a sense
[1937.14 --> 1942.98]  aurelia while we're making it easily packaged as a full framework there is a sense in which it's
[1942.98 --> 1948.10]  actually a set of building blocks to create your own framework as well because like i said you could
[1948.10 --> 1954.42]  take binding and you could write your own templating engine on top of that uh you know write a you know
[1954.42 --> 1960.34]  writing a templating engine is not trivial to to have one like we have but if you had a smaller simpler app
[1960.34 --> 1967.06]  and you just want to use data binding and you had very simple templating needs you could totally build
[1967.06 --> 1974.26]  something that you know queried the dom with for data dash attributes and use simple parsing to connect
[1974.26 --> 1979.22]  up the binding expressions and you wouldn't have to write the really hard part you know you could write
[1979.22 --> 1984.50]  the really easy part and just leverage this other library so it's it's highly modular i think in a way that
[1984.50 --> 1990.90]  that that a lot of other libraries aren't it's written with es6 and it tries to push you towards
[1990.90 --> 1996.18]  writing your stuff with es6 it works with anything but tries to kind of motivate you in that direction
[1996.90 --> 2003.54]  it's got some unique capabilities like the way it implements data binding um you know it works with
[2003.54 --> 2008.74]  it leverages stuff that's that's not fully available yet like object observe which is in chrome
[2009.46 --> 2015.46]  but isn't anywhere else so we have we have fallbacks for that that use the same sort of timing model
[2016.02 --> 2021.62]  and the same semantics you know as object observe and so there's unique things like that it's a really
[2021.62 --> 2029.46]  powerful router you know it works with web components out of the box the syntax for working with templates
[2029.46 --> 2035.30]  is kind of designed to be very extensible you know i talked at the beginning about the importance of an
[2035.30 --> 2040.90]  extensible framework and so that drives the modularity of the framework and the abstractions
[2040.90 --> 2047.14]  but also the way that certain apis are designed so you can extend the data binding language you can
[2047.14 --> 2054.58]  create extensions to html you can extend not only in kind of our out-of-the-box ways html which we have
[2054.58 --> 2059.78]  you know like behaviors you can attach and custom elements and we call template controllers which are
[2059.78 --> 2064.42]  like your repeaters and your ifs but but those are actually built over a core abstraction that the
[2064.42 --> 2070.26]  compiler understands so you can actually extend the compiler with completely new ideas so it's built
[2070.26 --> 2076.26]  around this extensibility thing you know from end to end from the way that it's broken up into modules
[2076.26 --> 2085.30]  and released and deployed to the api design and everything really is focused on on developer experience
[2085.30 --> 2091.70]  so again i was really influenced even though i never was a rails developer actually i was very influenced
[2091.70 --> 2098.02]  by the ideas there over the years and so you know when you build an app in my opinion you ought to just
[2098.02 --> 2103.30]  write a class and i have to have methods and you know properties simple stuff right and your view ought to be
[2104.18 --> 2109.86]  you know mostly basic html with with just some bindings that connect it with the class but there shouldn't be a
[2109.86 --> 2117.46]  whole lot of um i shouldn't have to call lots of special apis and do all kinds of registrations and
[2117.46 --> 2124.50]  i shouldn't have to use funky services to you know me i don't want to see the framework in my application
[2124.50 --> 2130.42]  code at all um now there's places where you you just you it's almost impossible not to do that right
[2130.42 --> 2134.58]  and in a rally app you will have these things if you create a custom element or one of these attached
[2134.58 --> 2140.18]  behaviors but your actual your more kind of core application code you know where your your
[2140.18 --> 2144.02]  interesting business logic if you will the things that are unique to the product that you're building
[2144.90 --> 2150.66]  um that's just going to be plain es6 classes and that's kind of the goal you don't want to see
[2150.66 --> 2157.06]  the framework you don't want the framework uh to intrude upon the interesting parts of your app if you
[2157.06 --> 2163.54]  can do that and so aurelia really tries hard to make that a reality so that's kind of a unique
[2163.54 --> 2168.02]  thing as well and that just plays out like i said the fact that you don't have to register with apis
[2168.02 --> 2174.66]  you don't have to attribute anything really um you don't have to inherit from special base classes
[2175.54 --> 2180.26]  none of that none of the kind of traditional things it's all based off of kind of simple
[2180.26 --> 2185.78]  conventions and you can override it with you know bringing the framework in to override things but
[2186.50 --> 2192.58]  you know the idea is if we can get it to like that 80 percent where you just write plain javascript
[2192.58 --> 2197.30]  and it just works and that's kind of the goal and that's where our focus have been so i think
[2197.30 --> 2201.22]  that's kind of a unique thing as well so there's a lot of different angles kind of coming together i
[2201.22 --> 2206.66]  think if you look at aurelia as a whole for me it's you know i wanted to build something that was
[2206.66 --> 2213.78]  compelling for me and those are a lot of factors extensibility modularity es6 powerful and extensible
[2213.78 --> 2221.54]  binding an extensible system as a as a whole a system that is favorable for you know pojos or you know i
[2221.54 --> 2228.98]  don't know if your community use that term or not but uh what's that what's the plane so they used
[2228.98 --> 2234.10]  to be called plain old java objects and then they were pocos which were plain old clr objects so this
[2234.10 --> 2238.34]  comes from like some of the statically typed languages but i would say a plain old javascript
[2238.34 --> 2244.90]  object you know nothing special about it no special base classes or annotations or anything
[2244.90 --> 2252.74]  uh you know just vanilla it looks you you write vanilla code it's not vanilla js because there's a
[2252.74 --> 2258.90]  framework there but your code is very vanilla you know and that's kind of the goal and now a word from
[2258.90 --> 2265.86]  our sponsor code ship is all about continuous delivery made simple you can set up continuous
[2265.86 --> 2270.90]  integration for your application in just a few steps and automatically deploy your code when all
[2270.90 --> 2277.30]  your tests have passed code ship is based on usability so everything is designed to be as easy to use
[2277.30 --> 2282.82]  as possible in fact code ship listened to feedback from their users and recently redesigned their app
[2282.82 --> 2287.38]  to include new usability improvements and made it even easier to use they've got great support for
[2287.38 --> 2292.10]  lots of languages and test frameworks they integrate with github and bitbucket you can deploy to cloud
[2292.10 --> 2298.26]  services like roku and aws and many more and you can get started today by trying out their free plan
[2298.26 --> 2305.62]  which includes 100 builds a month and five private projects use the offer code the changelog podcast
[2305.62 --> 2312.82]  to get a 20 discount on any plan you choose for three months again that code is the changelog podcast
[2312.82 --> 2318.58]  and you're going to get a 20 discount on any plan you choose for three months head to codeship.com
[2318.58 --> 2324.90]  slash the changelog to get started and now back to the show seems like the timing is really nice
[2324.90 --> 2331.78]  especially around es6 um i watched your your video on aurelia.io which anybody interested go check out
[2331.78 --> 2336.98]  that video he builds a uh pretty nice little app in about 20 30 minutes and you get a good idea of how
[2336.98 --> 2342.82]  everything kind of gets wired together but um in that the whole time i'm thinking is this this framework
[2342.82 --> 2350.10]  was built specifically with the assumption that es6 is available which it was one wasn't for polyfills and
[2350.10 --> 2356.10]  for you know modern browser um getting better and better a lot of the older frameworks could not
[2356.10 --> 2360.82]  make that that fundamental assumption which i think is a nice advantage at least for the time being
[2361.78 --> 2366.50]  edis or six to five is the polyfill project is that the one that you're using a six to five is a
[2366.50 --> 2372.66]  uh is a compiler yeah it uh right there are some polyfills that kind of go with it too but it uh yeah
[2372.66 --> 2380.02]  yeah it'll take uh your es6 code and turn it into es5 code and it's uh it's very uh it's a it's highly
[2380.02 --> 2387.22]  standards compliant output very clean uh generated code and it's um it doesn't have a required runtime
[2387.22 --> 2393.22]  that you have to include that goes with it so it's i mean and their team is just killer i mean they are
[2393.22 --> 2400.98]  really working hard they're releasing every day um so it's a super active project very high quality and i've
[2400.98 --> 2405.94]  been really impressed with it and it's been really easy it was really easy to also uh make it work
[2405.94 --> 2412.02]  with other tools you know so there was no problem we you know getting it to work with uh karma for testing
[2412.02 --> 2419.70]  or uh we have protractor happening now too for e2e tests and there was no problem uh getting jspm to work
[2419.70 --> 2426.50]  with it which is uh the package manager that we're kind of preferring because it's es6 oriented and uh so
[2426.50 --> 2431.46]  there was really no problems to get it to play well with anything else too uh so it was it's a
[2431.46 --> 2438.58]  fantastic uh open source project really and yeah yeah i was gonna say i i agree absolutely with that
[2438.58 --> 2445.62]  and um they're even now starting to do some es7 uh features which is shows how forward-looking they are
[2445.62 --> 2451.46]  bringing those back into um you know current browsers and it's kind of funny because you know the name six
[2451.46 --> 2457.94]  to five uh they kind of they pigeonhole themselves a little bit in fact there's a a github there's a
[2457.94 --> 2463.38]  github issue out there on their project about a rename where they're calling for new names and it's
[2463.38 --> 2468.26]  just as long as you could read it all i've heard of it i haven't read i read it but i oh man i read a
[2468.26 --> 2473.06]  little bit of it it's hilarious you know naming things is so hard it is um they're struggling they
[2473.06 --> 2478.58]  had a name they thought was great which i think it was rosetta yeah and turns out like that means
[2478.58 --> 2483.14]  something in german something not cool in german yeah something offensive in german it's like oh
[2483.14 --> 2486.98]  we can't do that yeah well you know like the big organizations like google and microsoft i mean
[2486.98 --> 2493.54]  whenever they name something it's like they have this huge process you know because you don't know
[2493.54 --> 2499.78]  they've got to check every language you know slang terms common use uh all this kind of stuff and
[2499.78 --> 2505.14]  i mean i had a few names for this framework too that were that ended up being problematic for
[2505.14 --> 2509.70]  similar kinds of reasons and i was gonna say while we're on the name why don't you mention how
[2509.70 --> 2515.54]  it got its name ah gosh it's kind of hard to trace to be honest because of the process i was just
[2515.54 --> 2522.66]  talking about uh i you know all my frameworks so far uh prior to this have been named after mythical
[2522.66 --> 2530.42]  swords so calaburn is is excalibur is another name for excalibur and durandal is a is a mythical sword
[2530.42 --> 2537.86]  and so i wanted to try and follow that theme but you know it it was there's a lot of mythical or
[2537.86 --> 2546.74]  fantasy-based sword names out there but not all of them are easy to spell or pronounce or um uh even
[2546.74 --> 2554.18]  sound like they would be even remotely usable in this scenario and i wanted to kind of have draw some
[2554.18 --> 2560.90]  connection to durandal if i could and so at some point i just started coming up with random words
[2560.90 --> 2566.90]  you know and um i think aurelia came out of it except it was uh it turned out to be a real word
[2566.90 --> 2572.82]  but it's an interesting word because there's a bunch of different meanings uh for it you know it means
[2572.82 --> 2580.74]  golden uh but it also refers to jellyfish in a particular context and it also has um
[2580.74 --> 2587.86]  um it's a term for a um uh i don't know a snarky female or something like that i can't i can't
[2587.86 --> 2594.10]  remember exactly the literal there's a bunch of different meanings for it but uh ultimately i like
[2594.10 --> 2602.18]  the way it sounded that's kind of cool so the latin family name of yes yeah so there's some historical
[2602.18 --> 2609.06]  things behind it and i kind of just liked a bunch of the different things and and the logo is inspired by
[2609.06 --> 2615.62]  you know a little like you can see the inspiration from the jellyfish idea and the color coloration so
[2615.62 --> 2619.14]  we didn't actually take the golden idea and the logo because that didn't that didn't turn out to
[2619.14 --> 2627.30]  look as nice but the jellyfish kind of idea filtered into the colors but the overlapping bars are slightly
[2627.30 --> 2635.54]  inspired by the sword ish logo from previous right so there's that and um i don't know it's kind of a
[2635.54 --> 2641.14]  hodgepodge in a way but it it turned out looking pretty elegant i think and um that's the long and
[2641.14 --> 2649.14]  short of it it's it's kind of it's not really a coherent story though well let's get back to the
[2649.14 --> 2655.14]  tech for a little bit um one thing i noticed in your video is you're using something called jspm
[2655.14 --> 2661.30]  which appears to be your own package manager no it's not my own actually uh okay it is uh a project
[2661.30 --> 2668.50]  run by guy bedford and it is uh who is also highly involved with the es6 module loader spec and the
[2668.50 --> 2674.02]  polyfill for that so so there's two parts to this one is jspm which is the package manager and the
[2674.02 --> 2681.78]  other part is system js and system js sits on top of the standards compliant module loader polyfill and
[2681.78 --> 2686.42]  adds a bunch of features to it that are needed for more advanced applications so these are things if you
[2686.42 --> 2692.34]  use require js that sometimes you need like like shimming libraries that weren't built in a modular
[2692.34 --> 2697.78]  way um doing different path configs and things like that because libraries are living in different
[2697.78 --> 2705.62]  folder structures um it makes amd common js umd es6 all the module formats it makes them work together
[2706.58 --> 2713.62]  and so i think i have system js open in a tab right now yes so system i'm gonna link that up on on
[2713.62 --> 2720.50]  the website here probably definitely system js is is really cool it's the module loader itself and
[2720.50 --> 2726.74]  jspm is the package manager and all this is sort of focused around es6 modules and one thing that's
[2726.74 --> 2736.66]  nice about it is that um the thing that's different about jspm is that it understands module formats and it
[2736.66 --> 2745.78]  understands the loader so when you install a package with jspm the identifier that you use to install
[2745.78 --> 2751.46]  it by is the same identifier you use to import it in your javascript and under the covers it just
[2751.46 --> 2758.18]  makes things work and you can jspm install directly from libraries on github or from libraries on npm
[2758.18 --> 2763.62]  and when it imports them into your project it does some fancy things that basically configures each
[2763.62 --> 2770.10]  library independently so that you can in a very clean fashion write an es6 import statement and
[2770.10 --> 2776.50]  bring in that library and work with it so it's it's the idea of the integration between the package
[2776.50 --> 2783.14]  manager and the loader that will ultimately load that code and it it makes it a very nice process
[2783.14 --> 2790.18]  in fact if you go to jspm i think it's jspm.io uh guy bedford has a video from jsconf i think
[2790.18 --> 2798.02]  it was maybe it was early 2014 it's a 20 30 minute video definitely worth watching where he starts to
[2798.02 --> 2802.58]  demonstrate the kind of the workflow that this enables and i'm going to hopefully demonstrate
[2802.58 --> 2808.10]  this with the relia too and in some future videos because i didn't really get into it too much in the
[2808.10 --> 2814.82]  in that first kind of quick intro but the idea is that somebody could publish a custom web component
[2814.82 --> 2820.18]  or a relia component or a plug into a relia straight on github and then on your command line
[2820.18 --> 2825.62]  you say jsbm install github and you you give it the project name it brings it down into your project
[2825.62 --> 2831.30]  and then you just import it in code and use it you know um and it's that i think it's that kind of
[2831.30 --> 2836.26]  workflow that that we all want it's the kind of workflow that is typically available on on native
[2836.26 --> 2842.66]  platforms for a while now you know if you if you work in a in a ruby or a java or a dot net kind of a
[2842.66 --> 2848.58]  an area you there's some package resource that you go to and when you install the package you just
[2848.58 --> 2855.06]  kind of like you import it and use it right and it just works and there hasn't really been that
[2855.06 --> 2860.82]  clean of an experience yet in javascript and jspm and system js is looking to kind of solve that
[2860.82 --> 2865.46]  problem and it does a bunch of smart things like i said it handles multiple module formats and
[2865.46 --> 2873.54]  globals but it also understands semver very very well and so you can actually have it'll actually
[2873.54 --> 2879.62]  fork dependencies in your in your project if you have you know two different libraries that are
[2879.62 --> 2886.74]  dependent on two different non-compatible versions of the same library it will make it work you know
[2887.38 --> 2891.86]  and it understands contextually what requires what and what versions and it works out all the stuff
[2891.86 --> 2898.02]  very very well and it's it's it's very it's very nicely done i think it's still you know like a
[2898.02 --> 2903.54]  really i think it's still early days for that project as well but it's probably the best thing i've seen so
[2903.54 --> 2911.06]  far for uh this concept of the integration of package manager and loader and it's very forward
[2911.06 --> 2918.50]  thinking too it's all it's all kind of es6 based and in that mindset and so it gels very nicely with what
[2918.50 --> 2923.38]  we want to do with aurelia so people are less familiar with it but i think if you watch that
[2923.38 --> 2928.66]  video and you kind of see some of the stuff we're going to put out soon i think you'll see okay you
[2928.66 --> 2935.70]  know now i understand why this is kind of our default that said though you can use bower if you want we
[2935.70 --> 2940.42]  don't require any particular package manager we don't actually require any particular loader so the
[2940.42 --> 2946.50]  loader is abstracted you can we work with system js or any require based loader but the loader is also
[2946.50 --> 2951.62]  abstracted so you can write your own loader you know if you want to write a loader that loads from
[2951.62 --> 2957.14]  stuff that's already all in the page or whatever because you've got a special build process or or
[2957.14 --> 2962.18]  something like that then you can totally write that and drop it in it's it's completely abstracted
[2962.18 --> 2967.78]  and so we just out of the box we say we think that this is probably looking out at the future and
[2967.78 --> 2973.38]  looking at modules and this kind of stuff we think that this is the most forward-looking path aligned
[2973.38 --> 2981.14]  with what we want to do but you can use other things interesting what else so you got two-way
[2981.14 --> 2987.38]  data binding going on is it always two-way or is there sometimes one way no it's not always two-way
[2987.38 --> 2992.74]  it's it's one way by default the only thing that's two-way is if you bind like a form input control to
[2992.74 --> 2997.78]  a property then that that turns two-way and you can actually turn the knob so to speak and control
[2997.78 --> 3004.18]  everything but we try and provide again the idea of convention over configuration if you say dot bind
[3004.18 --> 3009.38]  on something then we pick what we think is the sensible default which basically means one way
[3009.38 --> 3015.46]  unless it's a form control now when you write custom elements and custom behaviors with aurelia
[3016.02 --> 3021.78]  when you define your properties on that that are bindable you can specify the mode that is the
[3021.78 --> 3027.06]  default mode so if you have a custom element that has a property that's designed to be two-way data
[3027.06 --> 3033.62]  bindable bindable you can say that and it will just and it will work that way but you know binding is one
[3033.62 --> 3039.06]  of those things i worked with it for a long time before it really happened in the web space
[3040.10 --> 3044.50]  so i'm very comfortable with it and i also kind of know the pitfalls of it so we wanted to
[3045.30 --> 3049.54]  be one way by default with two-way in the places that it made sense by default
[3049.54 --> 3057.22]  but we also want to encourage people to use data binding and uh in a responsible way and uh
[3057.22 --> 3061.94]  right and that means basically that the purpose of data binding is to connect your view and your
[3061.94 --> 3068.26]  view model together it's not to do anything else it's not to be used to pipe events or to do uh people
[3068.26 --> 3074.34]  have done some crazy things so that's that's not what it's intended to be used for we actually provide
[3074.34 --> 3078.58]  other mechanisms for solving that problems like event we have a pub sub mechanism
[3078.58 --> 3085.14]  that's specifically designed if you need to do sort of cross-component highly decoupled messaging
[3085.78 --> 3092.98]  we give you a way to do that you know um but we are one way by default we as much as i can
[3092.98 --> 3097.94]  discourage people from doing crazy things like that i will because that creates a maintainable
[3098.82 --> 3104.42]  uh maintainability disaster to be honest and it can i suppose it could probably cause uh performance
[3104.42 --> 3110.10]  problems too we're not we're not a dirty check system primarily like angular is so angular has
[3110.10 --> 3114.34]  a bigger issue if you do that kind of things because it has to digest over and over and over again
[3115.38 --> 3120.02]  aurelia doesn't need doesn't have that problem but the real issue with that is in the understandability
[3120.02 --> 3128.66]  of the system when you start using data bindings as a way to create events or um you know that's not
[3128.66 --> 3134.10]  what it's for it's meant to basically synchronize your immediate view with your immediate view model
[3135.14 --> 3139.94]  and it's not meant to do anything more than that so we try and make that easy because it does make
[3139.94 --> 3145.14]  for a very nice developer experience but we try and provide other mechanisms for handling the other
[3145.14 --> 3152.18]  types of scenarios nice so it just watching the video i haven't used the the framework yet but as
[3152.18 --> 3157.46]  somebody who's used ember i've used angular uh used backbone i would say if you if you're coming from
[3157.46 --> 3163.54]  an angular style um you'll feel kind of at home i would call it kind of a simplified version i just
[3163.54 --> 3169.14]  i mean that in the best way possible where you have your custom elements um you have your data binding
[3169.14 --> 3174.98]  you have your interpolated strings what angular would have as directives you have these custom elements
[3174.98 --> 3182.02]  like i said that are a little bit easier to define you consider it a model view or view model
[3182.18 --> 3187.70]  uh what kind of yeah is it mvvm it is yeah that's what i would consider it and then technically a lot
[3187.70 --> 3192.98]  of angular apps are mvvm as well it's just yeah people don't aren't as familiar with that pattern but
[3193.54 --> 3200.98]  you know the idea is that you have a special type of model called a view model that is literally designed
[3200.98 --> 3208.90]  to be a model of the view so the idea is that you can strip off the visual component and have this model
[3208.90 --> 3213.78]  that represents everything the the view does its behavior and its state and that's what the view
[3213.78 --> 3218.74]  model is and so this works really really well in data binding scenarios because then the view just
[3218.74 --> 3224.10]  becomes like i said this thin layer over top of the view model that just is a rendering of that view
[3224.10 --> 3229.86]  model and this is great for testability because effectively what you want to have in the end is the
[3229.86 --> 3238.02]  ability to instantiate your entire app with no views right and that's the idea of of view models and a
[3238.02 --> 3242.74]  lot of apps you'll have sort of this this tree structure of view models or this hierarchy of
[3242.74 --> 3247.86]  view models that represents you know a view model for the application shell a view model for the
[3247.86 --> 3252.98]  current you know page that you're navigated to view models for the components inside of those pages
[3253.78 --> 3260.10]  and the whole the entire behavior of the app is represented in plain javascript models it just so
[3260.10 --> 3267.06]  happens that it's being rendered by html because it's that html is synchronizing its state to the view model
[3267.06 --> 3274.82]  right so this is a twisting of you know mvc mvc is much more um sort of you know controllers were
[3274.82 --> 3282.50]  more kind of event uh centric i tend to think of it like a spectrum with mvc is on one end entirely
[3282.50 --> 3287.94]  stateless and mvvm is on the other end which it's actually very stateful and then you have something
[3287.94 --> 3294.42]  like model view presenter which is sort of in the middle um right a little bit of data binding a little
[3294.42 --> 3300.90]  bit of more event centric programming um so you know you could do any of it really with aurelia
[3301.62 --> 3307.30]  but it makes mvvm really really easy and that's just something that is natural in a in a world where
[3307.30 --> 3312.50]  you have a rich data binding okay two more things i want to talk about testing i want to talk about
[3312.50 --> 3317.86]  the data model let's start on the data side so a lot of these frameworks seem to punt when it comes to
[3317.86 --> 3325.78]  the data i mean they or maybe just plug in so ember has ember data angular has rest angular and some
[3325.78 --> 3332.58]  other things does aurelia have stuff for you know persisting and retrieving data from servers
[3333.62 --> 3336.98]  uh not at this point actually we're planning we're kind of planning to punt too because
[3338.82 --> 3344.18]  you know it it's a complex space in its own right and there's a lot of good solutions out there's a lot
[3344.18 --> 3351.14]  of good solutions out there and what we would love to do is be able to say like hey do you like ember
[3351.14 --> 3357.54]  data plug it into aurelia you know because one of the key aspects of our data binding i'm saying that
[3357.54 --> 3361.86]  you can do that you know i haven't tried it but that's the kind of idea because one of the key
[3361.86 --> 3368.18]  aspects of the data binding system is that it's it's this uh adaptive uh model if you will so you can
[3368.18 --> 3373.94]  plug in an adapter that understands particular way of building models and it will know how to observe
[3373.94 --> 3379.22]  them that's kind of the idea so um we've got some people doing integration with different stuff
[3379.22 --> 3384.98]  breeze js is a library that's out there that i'm familiar with it's just a model library that does
[3385.62 --> 3392.58]  restful updates and it does a client-side caching and it does a whole you know it tracks relationships
[3392.58 --> 3398.58]  and all kinds of stuff and so we've got someone that's actually already built an adapter for aurelia
[3398.58 --> 3407.14]  so that you can build your breeze models and you plug this into aurelia and uh it basically tells
[3407.14 --> 3411.70]  aurelia how to observe it because that library has its own way of notifying when changes happen
[3412.42 --> 3416.82]  so we don't have to do any kind of dirty checking against it because we don't you know because we
[3416.82 --> 3422.18]  don't know how it works or when things change with it we plug the adapter in and whenever it changes
[3422.18 --> 3426.98]  something it tells the binding system and it it looks to the rest of the binding system in the
[3426.98 --> 3433.30]  templating world so to speak like anything else so our focus is can we make the data binding engine
[3433.30 --> 3439.78]  pluggable and can we work um together with the community to try and build adapters for popular
[3439.78 --> 3444.66]  data libraries so then you can just bring whatever you like you know or whatever your company has
[3444.66 --> 3450.26]  standardized on or you know whatever the case whatever the constraints are you know so i don't have
[3450.26 --> 3456.74]  in the plans to build a data library um i do know how complicated it is because i actually build an
[3456.74 --> 3461.78]  object relational mapper and dot net i've built three of them actually and i never open sourced any of
[3461.78 --> 3467.38]  them and i'm really glad because it is so complicated to build stuff like that um and to make it work
[3467.38 --> 3474.90]  right for everybody so i'm trying to avoid that and we would rather just let people write adapters and
[3474.90 --> 3480.42]  let them bring their own favorite way of dealing with data and or even their project specific way
[3480.42 --> 3485.86]  you know because some of these libraries are better with um you know with different types of apis
[3486.58 --> 3491.54]  yeah yeah it's even harder than doing a an orm where you have to spit out you know sql at the end of
[3491.54 --> 3498.74]  the day because each of these apis has a different right um interface and so a generic solution is is
[3498.74 --> 3503.94]  very difficult i think um when yahuda and tom dale were on they spoke to that about
[3504.90 --> 3509.62]  ember data and how it's been the slowest part to come into production use of their system just
[3509.62 --> 3514.18]  because it's such a hard problem and they didn't realize how much work it is to build a generic
[3514.18 --> 3520.98]  adapter for all these backends when they got started um last thing and then i'll pass it back to adam is
[3520.98 --> 3526.82]  testability so you say it's testable on the home page i think uh if you call back to the rails
[3526.82 --> 3532.02]  influence i think one of the things rails did for the rupee community was not just make things
[3532.02 --> 3537.22]  testable but it actually brought along all the test harness for you and even generated tests and
[3537.22 --> 3541.86]  stuff so it was just like it was just there to be done and i think that influenced rubius to really
[3541.86 --> 3548.90]  become uh excited about testing how is aurelia testable right so we've you know just first off
[3548.90 --> 3554.10]  just in the core when you move to a world with es6 where your javascript is kind of being forced to
[3554.10 --> 3560.26]  be modular that tends to help a little bit anyways and everything in in aurelia itself
[3560.90 --> 3565.62]  is built that way and all of our things are kind of pieced together with dependency injection so the
[3565.62 --> 3571.30]  framework itself is is very decoupled and it encourages you to build your own apps in the
[3571.30 --> 3579.62]  same way so it helps to push you down that road but what we uh have done actually is in our skeleton
[3579.62 --> 3584.10]  starter kit and i didn't i didn't get to show this in the video there's just only some you know
[3584.10 --> 3589.78]  trying to keep a video short there's only so much you can show we have basically set up the skeleton
[3589.78 --> 3594.02]  so that if you kind of use that as your starting point for your new app you've already got karma set
[3594.02 --> 3599.30]  up for unit tests and protractor set up for end-to-end tests so these aren't tools we built there were
[3599.30 --> 3604.18]  tools actually built i think uh primarily for angular but they're just out there in the community now
[3604.18 --> 3609.54]  and used in a variety of contexts and they work pretty well so we've gone and actually pre-configured
[3609.54 --> 3616.18]  everything for you in that skeleton uh gulp is set up and and all the configuration is set up for all
[3616.18 --> 3623.86]  that stuff uh so that you can basically and there's some there's some starter tests in there ed and unit
[3623.86 --> 3631.06]  tests so you can basically just you just start filling in your own tests you know nice um and we'll
[3631.06 --> 3637.06]  do more work there too i think i've got some some nice ideas uh you know like doing auto mocking
[3637.06 --> 3642.98]  because we use dependency injection we can we can we can create some tooling around tests that make
[3642.98 --> 3647.14]  it easier to you know create jasmine spies automatically when the dependency injection
[3647.14 --> 3653.94]  container you know knows that there's a dependency that needs to be a spy or whatever and so we can do
[3653.94 --> 3660.82]  some more work there but the core pieces are all there in terms of uh like if you download actually i think
[3660.82 --> 3664.66]  i need to make a release of the skeleton actually the new release that has the protractor in it
[3664.66 --> 3670.02]  uh because we didn't have that originally but but if you get the latest release basically everything
[3670.02 --> 3675.22]  is just good to go you know you follow the getting started guide and you just start changing things
[3675.22 --> 3682.50]  is kind of the idea start adding your own tests and everything is just like i said the the concept
[3682.50 --> 3688.90]  and the kind of the the path we try to push you down is to write very modular code so we want you to
[3688.90 --> 3694.58]  leverage dependency injection and to leverage es6 modules in the right small focus classes you know
[3694.58 --> 3700.02]  know single responsibility principle yada yada yada we want you to do that our framework is built
[3700.02 --> 3706.02]  that way and we give you the infrastructure to do that and then we set you up with this
[3706.02 --> 3712.74]  pre-configured set of uh tools so you can just start writing tests you know in that in that fashion
[3713.86 --> 3717.30]  well last question i think i've got for you then we can probably go to our closing questions
[3717.30 --> 3723.38]  is i guess the framework not framework maybe the framework's not good a way to frame the tail end
[3723.38 --> 3728.26]  of this conversation which is more or less you know when someone's trying to choose which framework
[3728.26 --> 3734.66]  to use as a matter of fact coming on to this call here with you in preparation i've seen some people say
[3734.66 --> 3740.90]  about a really is announcement that like oh one more just another uh framework out there to use
[3740.90 --> 3746.02]  more like in a bad way like one more to choose from right so obviously there's some sort of
[3746.02 --> 3751.62]  anxiety or some sort of friction on the choice of which to use you got durando which is sort of you
[3751.62 --> 3755.30]  know we know where that came from which we already talked about that but supports legacy browsers all
[3755.30 --> 3760.58]  that are really focused on the future and es6 es7 all the things we talked about
[3761.54 --> 3766.10]  you got backbone you've got angular which we already heard about from you as well and then you
[3766.10 --> 3770.58]  got ember js and there's probably several other out there that that maybe not on my radar quite
[3770.58 --> 3776.50]  yet but when someone chooses a really uh i guess keep it somewhat short because we're close to time
[3776.50 --> 3781.46]  on this but like you know what is it that they're choosing what to what makes them choose a really over
[3781.46 --> 3787.38]  others and how did that how does someone make a choice on these frameworks to use well with a really
[3788.10 --> 3792.90]  you know the thing that we've been focusing on which is i think what what entices a lot of people
[3792.90 --> 3799.94]  so far is that we really focus on this developer experience you know it's very modern and we try
[3799.94 --> 3805.70]  and keep it very very simple and again it's simple but it's not simplistic you can do some crazy crazy
[3805.70 --> 3812.66]  things but we want it to be a very simple set of patterns that you follow and simple conventions so
[3812.66 --> 3818.18]  i think you choose irelia if that appeals to you i mean um i think frameworks are interesting because
[3818.18 --> 3823.94]  they're built to solve technical problems but every framework really you can't be divorced from
[3823.94 --> 3830.02]  the human component people pick frameworks for very subjective reasons you know or sometimes for
[3830.02 --> 3838.50]  political reasons company culture or team culture reasons so i think that irelia though the idea is that
[3838.50 --> 3845.06]  it should make you happy actually i mean uh yeah um when you look at the code you should feel good about
[3845.06 --> 3850.34]  that code it's it's your code most of it is your code without framework around it it should be simple
[3850.34 --> 3855.22]  and straightforward the process you follow for creating things should be simple straightforward
[3855.22 --> 3862.74]  consistent and i think that that is probably what will draw people uh to irelia and i understand the
[3862.74 --> 3869.94]  framework uh anxiety um you know but i want a couple of things to that point which are
[3869.94 --> 3876.34]  you know first off things are always evolving and so we have to try and create new things we have to
[3876.34 --> 3884.10]  learn from each other we it's it's very incremental sometimes and if we kind of have to be in a state of um
[3884.10 --> 3890.42]  of of kind of working with what we have but not quite being content all the time or else we won't really
[3890.42 --> 3898.90]  progress it at all um so i think that it's not a bad thing to have one more framework and i frankly welcome
[3898.90 --> 3903.46]  anyone else that wants to build one too because i i learn i study i've studied pretty much everything
[3903.46 --> 3907.94]  that i know about that's out there i i look at the code bases i look at the videos i do some training
[3907.94 --> 3914.10]  on it and and try and understand and um i think that helps to move us better and the reason that i
[3914.10 --> 3918.98]  build stuff like this and others keep building stuff like this is because you know we're not happy with
[3918.98 --> 3924.34]  the way things are we we feel that it could be better whether it's performance or whether it's usability or
[3924.34 --> 3930.66]  you know whatever the the kind of the angle that you're coming at it is people recognize that we're
[3930.66 --> 3934.90]  making it happen but we're not really happy we're not really there yet so to speak so we keep kind of
[3935.46 --> 3941.30]  trying to evolve that and i would just say also that you know if you're working in this industry
[3941.94 --> 3947.14]  um you know don't feel like you're you know you have to be an aurelia expert to get a job or something
[3947.14 --> 3952.82]  like that i mean um i i would even tell you you you should not be going to production with aurelia right now
[3952.82 --> 3956.50]  i don't know if you're working in this industry or something like that i don't know if you're
[3956.50 --> 3960.90]  working in this industry or something like that but but but really if you work in our field hopefully
[3960.90 --> 3964.90]  you find it interesting and like to learn new things so i would just say when you see something
[3964.90 --> 3969.86]  like aurelia or anything else take it as an opportunity to see how other people are trying
[3969.86 --> 3975.06]  to solve these problems and to learn something and not not be stressed out about now i have to
[3975.06 --> 3981.62]  be an expert in x you know x to to keep my job because the way i tend to approach all of this is
[3981.62 --> 3986.34]  i'm fascinated by what people are building and i learn just enough about it usually to know what it
[3986.34 --> 3992.34]  is and then i catalog it for when i need it for when i need to make a decision for which this might
[3992.34 --> 3999.38]  be the you know the answer and having options is good because every scenario is different you know and
[3999.38 --> 4004.18]  you want to be able to make an informed decision if you're in a place of authority where you're going to
[4004.18 --> 4010.82]  choose a framework you want to know what your options are you want to have options and you want to
[4010.82 --> 4017.38]  know how you can pick the best solution for your particular project you know your team company etc
[4020.10 --> 4025.22]  awesome man well uh this has been great we have our closing questions and we'll probably limit it to
[4025.22 --> 4030.90]  just one or two since we're low on time so rob um let's go with who is your programming hero
[4031.94 --> 4038.90]  uh so i wouldn't say i have heroes in the programming world uh i definitely have some strong influences and
[4038.90 --> 4045.22]  uh one of the biggest influences is eric evans who wrote a book called domain driven design which is
[4046.02 --> 4054.18]  very almost like a poetical sort of work on software design bob martin uncle bob he is a big influence
[4054.18 --> 4066.18]  uh rebecca worse brock also uh a big influence on me her um just discussions about object design roles and
[4066.18 --> 4070.98]  responsibilities and these kinds of things so those are i would say i don't know if i call them heroes
[4070.98 --> 4077.78]  but they're influencers they shape the way i think and approach problems a lot perfect perfect uh all
[4077.78 --> 4082.66]  right last one uh you know that can spread the love around the podcasting scene a lot of great podcasts
[4082.66 --> 4087.38]  out there uh what are some podcasts that you listen to or that you could suggest that our listeners might
[4087.38 --> 4094.02]  enjoy so my two you know the two biggest technologies i've worked with in the last decade are dot net and
[4094.02 --> 4099.54]  then javascript and so on the dot net side of things uh there's a fantastic podcast that's been around
[4099.54 --> 4105.70]  forever it's very entertaining and it's dot net rocks so definitely check out dot net rocks and i'm actually
[4105.70 --> 4110.58]  checking their page out right now and they had they had uncle bob on like their most recent episodes so
[4110.58 --> 4115.38]  that's probably that's probably interesting we'll link up to that another one is uh is herding code
[4116.50 --> 4122.90]  uh and there's a group of guys that host that and they're all kind of uh of different uh perspectives
[4122.90 --> 4128.58]  i would say and uh it's it's really interesting and then i also like to check out javascript jabber
[4128.58 --> 4135.30]  on the javascript side of things that's a great great uh podcast too herding code that's on soundcloud right
[4135.30 --> 4140.42]  i recall subscribing on soundcloud maybe maybe maybe i follow all the guys
[4140.42 --> 4146.02]  so on twitter so whenever something happens that's interesting i i grab it from the site but
[4146.90 --> 4154.82]  cooliello.com we'll link up the uncle bob uh podcast for sure and uh is it eric evans was
[4154.82 --> 4159.62]  that right the main language yeah domain driven design eric evans that's his book yeah it's it's uh
[4160.26 --> 4165.86]  fantastic ddd not bdd ddd yes but they they go together i guess yeah
[4165.86 --> 4172.18]  well cool rob it was a it was awesome to have you on the show i know that so for the listeners
[4172.18 --> 4177.38]  obviously if you're listening to now you know that this is a slightly longer show than normal we gave
[4177.38 --> 4183.86]  uh rob about 10 maybe 12 extra minutes this time just because we knew we had you know like jared said
[4183.86 --> 4188.82]  earlier we thought we were coming to this call with uh durando and angular and that was enough and then we
[4188.82 --> 4193.54]  added a really to it so yes six yes seven all these things he was talking about so we had to
[4194.18 --> 4199.86]  reallocate some some more time to to this one before we close out i do want to mention our ping
[4199.86 --> 4205.62]  repo jared you mentioned that that's where this guest idea came from yep um you know super awesome
[4205.62 --> 4212.18]  there so github.com slash the changelog slash ping uh post an issue share code you're working on show
[4212.18 --> 4218.18]  code share code that's influencing you we have a recent issue we've opened up talking about conferences we're
[4218.18 --> 4222.10]  going to this year we'd like to go to so if you have a conference you're a conference organizer
[4222.10 --> 4226.34]  you're listening to this and you'd like to have us come there um there is a post there so go ahead
[4226.34 --> 4232.58]  and throw a comment in there just keep in touch it's sort of our open inbox uh so to speak so ping
[4232.58 --> 4239.22]  on github is awesome for us uh we also have a couple sponsors we want to mention rack space top
[4239.22 --> 4244.26]  tile and code ship um as we know right now rob's going afterwards as soon as he's done here he's
[4244.26 --> 4249.62]  going to figure out who code ship is because he's he's he's not a ruby hacker so javascript and uh
[4249.62 --> 4254.42]  and dot net so i think uh coach has some stuff with javascript if i remember correctly on on
[4254.42 --> 4260.18]  testing deployments for that but rack space top tile coach that makes the show possible and of
[4260.18 --> 4264.26]  course you the listeners we thank you jared rob anything else you want to cover before we
[4264.26 --> 4269.46]  say goodbye to this fantastic audience we're talking to i'm good it's been a great conversation i
[4269.46 --> 4274.26]  really appreciate uh you all having me on you're a friend of the show now man you're welcome back
[4274.26 --> 4279.94]  anytime awesome thanks all right let's say goodbye everybody bye guys bye
[4299.46 --> 4318.52]  you
