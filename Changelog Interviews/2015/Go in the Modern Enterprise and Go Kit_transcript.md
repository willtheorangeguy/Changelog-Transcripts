[0.00 --> 16.06]  welcome back everyone this is the change log and i'm your host adam stankowiak this is episode 163
[16.06 --> 21.54]  and on today's show we got peter begon joining us to talk about go in the modern enterprise
[21.54 --> 28.42]  and today we're talking about go kit a go toolkit for microservices great call today with peter
[28.42 --> 35.74]  and uh speaking of peter he's going to be at gopher con along with us uh and so many other people 1500
[35.74 --> 41.36]  people are going to be at gopher con 2015 so we're going to be there with cameras in hand
[41.36 --> 48.82]  covering everything we possibly can with gopher con so say hello if you're there hit us up on twitter
[48.82 --> 56.74]  whatever it takes we got three awesome sponsors for this show code ship digital ocean and top towel
[56.74 --> 63.58]  our first sponsor is code ship a hosted continuous delivery service focusing on speed security
[63.58 --> 70.22]  and customizability you can set up continuous integration in your application today in a
[70.22 --> 75.52]  matter of seconds and automatically deploy your code when your tests have passed code ship supports your
[75.52 --> 80.84]  good hub and your bid bucket projects and you can get started today totally and absolutely for free
[80.84 --> 86.62]  should you decide to go with a premium plan you can save 20 off any plan you choose for three months
[86.62 --> 94.28]  by using our special code it's the changelog podcast use that code and save 20 off any plan you
[94.28 --> 101.82]  choose for three months head to codeship.com slash the changelog to get started and now on to the show
[101.82 --> 113.78]  all right everybody we're back we got peter be gone with us he's a software engineer living in
[113.78 --> 120.24]  berlin germany it's 10 at night over there by the way it's 3 p.m on my time uh across this pond but
[120.24 --> 125.18]  he focuses on large-scale distributed systems peter welcome to the show thank you very much thanks for
[125.18 --> 132.08]  having me so peter the the conversation we're gonna have is based around go kit but there's lots of
[132.08 --> 138.60]  other separate conversations that happen sort of to describe why and what go kit is and why you're
[138.60 --> 144.40]  doing it before we do all that um for those who may not know who you are can you describe what you
[144.40 --> 149.78]  what you do and what you work on sort of maybe some of your background oh sure um so i got my start
[149.78 --> 157.14]  actually in the telecom industry i was doing embedded software like c and c++ on i guess it was
[157.14 --> 166.62]  uh like routers and switches that you would normally stick into um telecom uh switching centers
[166.62 --> 172.90]  at sort of the national level so i kind of grew up as an embedded networking guy uh and then over
[172.90 --> 179.68]  some time moved into more distributed systems at a sort of higher application level i worked at
[179.68 --> 185.84]  bloomberg for a while i did a search product there as sort of a federated search and i worked for some
[185.84 --> 192.46]  ngos for a little while i worked at another telecom company doing a monitoring product uh sort of global
[192.46 --> 199.08]  scale monitoring product and wound up at soundcloud here in berlin and at soundcloud i worked on quite
[199.08 --> 206.98]  a few things uh the search product there i rebuilt that i moved into the stream uh activities feed
[206.98 --> 212.98]  kind of area which i guess is something that a lot of web companies are doing in one way or another
[212.98 --> 219.82]  i got into distributed systems theory there and i did a couple of projects related to that i guess the
[219.82 --> 227.36]  one that got the most uh attention in the world is a distributed sort of quasi time series uh database
[227.36 --> 234.12]  system called roshi which is based on crdts which is a fun distributed systems data type
[234.12 --> 239.38]  conflict free replicated data types it's all the rage it's the hipster data type and distribution
[239.38 --> 246.50]  systems theory um and then after that i and currently i'm i'm working for weaveworks which is a
[246.50 --> 252.86]  company that does software defined networking for the container space so for docker containers so we
[252.86 --> 261.10]  uh currently are giving away this product that can uh network's docker containers up together
[261.10 --> 266.46]  in you know the easiest way possible and then we're building out uh stuff around that basically
[266.46 --> 274.46]  very interesting yeah i mean uh speaking of docker and whatnot docker con just happened they just had a
[274.46 --> 282.40]  huge announcement about the app container spec becoming uh i guess federated is maybe a way to
[282.40 --> 288.00]  say it uh yeah the two houses combined yeah i mean that's that's good news for the users so that must
[288.00 --> 293.94]  be some good news for weave as well yeah definitely where is it weave works uh weave works is a company
[293.94 --> 298.10]  weave is the product okay one of the products yeah i was looking at the page i'm like i just said weave
[298.10 --> 302.80]  and i don't want to mispronounce it i'm like okay is that right or wrong yeah this this seems really
[302.80 --> 308.84]  interesting so you've you've definitely had you know the full gamut of of interesting software
[308.84 --> 313.94]  development experience embedded i mean doing something on just the device itself how how
[313.94 --> 318.86]  different is that than what you're used to now which is distributed and you know multi-layered services
[318.86 --> 325.38]  how much different is it to to just sort of embed software onto a network you know network hardware
[325.38 --> 329.84]  or something like that yeah i mean there's similarities and differences a lot of the theory applies pretty
[329.84 --> 335.26]  directly actually um no matter what scale you're working at i would say the major differences are
[335.26 --> 341.30]  the sorts of things you have to care about when you're focused on something so small you uh your
[341.30 --> 346.28]  your scope is narrowed i would say so you spend a lot of time counting all the bytes and counting
[346.28 --> 352.06]  all the ops and when you're working at a at a broader level that stuff sort of fades into the background
[352.06 --> 357.80]  and you're more concerned with correctness uh especially in the face of failure i think probably
[357.80 --> 363.64]  the biggest uh shift for me in my career is that i've become more and more concerned with
[363.64 --> 371.52]  building correct things quickly or uh rather than sort of eking out the last little bit of performance
[371.52 --> 378.76]  because uh that seems to be what's important or perhaps where the industry is going like we can
[378.76 --> 385.90]  buy servers to scale horizontally but if the systems are fundamentally broken no amount of servers is going
[385.90 --> 391.46]  to fix that so that's kind of been my experience that's very true so i guess the meat of this
[391.46 --> 399.54]  conversation um as we'd mentioned a little earlier was was really routed around go kit and this was
[399.54 --> 404.92]  originally a talk that you gave at fosdam at the google campus there in london at a meetup
[404.92 --> 411.40]  earlier this year so back in february so this is relatively a new idea or at least publicly a new idea
[411.40 --> 418.42]  yeah yes and no um what happened there was uh andrew durand who i know through uh the go community
[418.42 --> 423.48]  uh reached out to me and asked me if i might have anything to say at fosdam since i'm not too far away
[423.48 --> 430.06]  and i've spoken at at go events in the past and he kind of left it up to me what i should say uh or what
[430.06 --> 436.00]  i wanted to talk about and i kind of did a survey of my mind and the state of the sort of go community
[436.00 --> 442.42]  at the time and uh at the time i was working at soundcloud and we had just sort of or we were maybe
[442.42 --> 449.16]  in the middle of this period of change um maybe the story will resonate with a lot of people working
[449.16 --> 455.86]  in in organizations where when we were kind of young and and excited and and full of optimism and
[455.86 --> 462.04]  opportunity we uh we had a lot of languages that different teams at the at the uh at the company
[462.04 --> 469.00]  were free to to implement things in and that was great it was like a cambrian explosion and we were
[469.00 --> 476.84]  very productive and and very happy uh but we were small also uh we were maybe 20 50 up to 75 engineers
[476.84 --> 482.60]  or something when that was still going on and so obviously uh that carries a cost as you get bigger
[482.60 --> 491.78]  um support costs go up and and there's a natural tendency to kind of uh isolate to or like
[491.78 --> 497.08]  pare down to just a few sort of core supported languages for example at google i believe the
[497.08 --> 504.12]  supported core languages are c++ java python and now go but that was you know the most recent addition
[504.12 --> 509.58]  um so that's the choices that you have when you want to write something there and so similarly at
[509.58 --> 515.48]  soundcloud we started saying you know we can't really be putting haskell uh services into production
[515.48 --> 521.68]  forever um let's think about uh where our strengths lie let's think about the sorts of things
[521.68 --> 529.78]  we want to be supporting long term and um it came down to a few final candidates uh we had a lot of
[529.78 --> 536.62]  people who were into scala which was great a lot of services in scala we had a lot of people into go
[536.62 --> 542.28]  we had built a lot of stuff and go and it was running you know really quite well uh there was a
[542.28 --> 547.08]  little bit of closure there was a little bit of java there was quite a lot of ruby uh as these things go
[547.08 --> 553.20]  and um those were kind of the languages that we settled on um but that process continued
[553.20 --> 560.68]  and uh what i found was that the scala camp was kind of winning and more and more new things were
[560.68 --> 565.54]  being written in scala or scala was being chosen for more and more new projects where in my opinion
[565.54 --> 571.92]  go would have been an equally good or perhaps even better choice um so i started reflecting on why this
[571.92 --> 578.54]  was and what i kind of came up with was that product managers and owners people who aren't
[578.54 --> 585.12]  invested in like the long-term success of projects and and teams uh they wanted some sort of sense of
[585.12 --> 592.88]  security or support from a language from a framework from the technology decisions that they were investing
[592.88 --> 598.96]  in uh for a long time right like a year two years maybe indefinite sort of time horizon
[598.96 --> 606.26]  and while go was like proving itself technically uh it wasn't mature enough and it didn't quite have
[606.26 --> 613.80]  the library support that we needed in our architecture um so it was an easier or maybe safer choice to pick
[613.80 --> 619.86]  scala even though it might have performance characteristics that weren't uh as good as they
[619.86 --> 627.76]  could have been or might have a cost of complexity that was higher than it needed to be um so that got me
[627.76 --> 634.14]  thinking and it made me realize maybe something that go is missing is this uh collection of like
[634.14 --> 641.34]  higher order uh idioms and and tools and i hesitate to use the word framework but maybe something like
[641.34 --> 647.70]  a framework that can be used in these sort of uh uh well i call it a modern enterprise these sort of
[647.70 --> 653.56]  organizations like soundcloud is um to give these middle managers and and technical leaders
[653.56 --> 659.08]  uh confidence in choosing go is sort of a long-term language for their for their application layer
[659.08 --> 663.52]  for their business logic and so i sort of rolled that idea around in my head a little bit and
[663.52 --> 671.42]  decided that would probably make a pretty good talk and um yeah go kit was born so kit certainly makes a
[671.42 --> 677.44]  lot more sense when you reflect back on the idea of going framework or not framework and kit certainly
[677.44 --> 681.12]  makes a lot more sense too especially as you start to break it down into all these different
[681.12 --> 686.22]  components that may or may not fit into this blessed framework that somebody might use sort of
[686.22 --> 691.86]  piecemeal right it's sort of choose your own choose your own things you need for your infrastructure
[691.86 --> 699.66]  your architecture exactly the one of the fundamental ideas behind the go kit is that uh we're coming in
[699.66 --> 705.78]  we expect to be coming into an organization that already is a little bit big successful they have some
[705.78 --> 710.32]  inertia they have some momentum they have some existing infrastructure that they're not going to just throw away
[710.32 --> 716.52]  overnight um we want to kind of slide in where go makes sense and we want to work with the stuff
[716.52 --> 722.50]  that's already there so yeah we're not a framework that you have to buy into 100 and you can only talk
[722.50 --> 727.44]  to other go kit services or something like that we really want to be good neighbors and we want to be
[727.44 --> 734.38]  able to have a story that you can tell to your boss or to your uh engineering director that's like
[734.38 --> 739.44]  look we're just going to use a little bit uh right now if it makes sense we're going to there's a
[739.44 --> 744.54]  there's a future there and i just want to make that future kind of look bright exactly this also
[744.54 --> 753.18]  seems like a you know not so much a fist fight but definitely a uh an attempt a try a fight to
[753.18 --> 761.10]  for go to win over java or scala or other options in the enterprise you mentioned closure ruby uh and
[761.10 --> 768.16]  yeah java so it seems like this is your your attempt to because you're you seem like a go champion
[768.16 --> 776.00]  and you want to to use go where you can use it and not let scala or others win when uh when i guess
[776.00 --> 783.28]  win the win the battle for the next project the battle for mindshare yeah yeah um i'm definitely a go
[783.28 --> 788.68]  advocate um and that's a personal thing that uh was immediately apparent to me when the initial
[788.68 --> 793.52]  release happened and um the more energy i've put into go the more i've gotten out of it it really
[793.52 --> 800.68]  just aligns with my personal philosophies and my um preferences when it comes to programming but i want
[800.68 --> 805.42]  to be and of course this is going to sound a little political but i but i'm really being honest when i
[805.42 --> 811.86]  say it's it's not for me a fight at all i don't want to see go beat java or scala or any of these things
[811.86 --> 820.54]  all i want to do is make go a viable option for people who want to use it and uh if if there are
[820.54 --> 825.20]  go champions at your organization who think that they can be productive and go who think that there
[825.20 --> 831.46]  are a set of services that would work really well with go i want to lower barriers to adoption from
[831.46 --> 837.94]  people who maybe don't know a lot about the language or would tend to stick with safer uh safer
[837.94 --> 843.64]  choices like like java or the jvm um so yeah it's really not about winning so much as just
[843.64 --> 851.14]  getting uh go to the same playing field i would say so for those you mentioned middle managers
[851.14 --> 857.12]  product managers that wanted security and support from the language and you mentioned that go hadn't
[857.12 --> 862.66]  been quite as mature as it could be to win some of those over since february and since you've gotten
[862.66 --> 867.80]  more of an advocate for go what what have you learned about go in terms of security and support
[867.80 --> 873.34]  from the language that's changed that would change those people's minds so a lot of it i think is
[873.34 --> 879.46]  purely a matter of time i mean go has only been in the wild for i think five years i think we're
[879.46 --> 885.92]  coming up on a five-year anniversary if i'm not mistaken maybe six years now yeah 2009 i just had
[885.92 --> 889.60]  andrew duran on the show not long ago and i think we're talking about the five years then because
[889.60 --> 895.38]  you know to rewind way back i think episode if i'm correct i keep missing the number but episode
[895.38 --> 903.00]  three i believe of the changelog we had rob pike on to talk about go and that was november 27 2009
[903.00 --> 910.10]  yeah exactly before that that go was born exactly that that um that sounds true to me so yeah five
[910.10 --> 916.22]  and a half years or something which uh to someone who's been in the language like uh 100 basically
[916.22 --> 921.40]  from the beginning that seems like a long time but of course to somebody who is responsible for
[921.40 --> 927.50]  you know the the the engineering department of a business that's almost no time at all uh so i
[927.50 --> 935.68]  totally understand that they are a bit uh perhaps cautious about uh investing in something so young on a
[935.68 --> 941.18]  on a broad time scale and i think that's actually totally totally rational um i think it's just a matter
[941.18 --> 947.10]  of time for a lot of people and they need to see not just one or two successful projects that you know
[947.10 --> 952.86]  super techie companies but you know a series of successful projects and companies that are
[952.86 --> 960.16]  not so techie that are consumer oriented that are maybe b2b uh companies who can tell a good like
[960.16 --> 966.36]  business success story from choosing go rather than just a technical success story and so i want to help
[966.36 --> 975.56]  the people who are capable of um becoming those good stories becoming go advocates from a uh perhaps less
[975.56 --> 982.38]  technical and more business oriented kind of domain um so that's that's like my my impetus here
[982.38 --> 989.34]  well let's dive deep into go kit then let's figure out what it is why you built it and i guess what
[989.34 --> 997.38]  what problems it aims to solve for the in quotes modern enterprise yeah exactly um so the most important
[997.38 --> 1004.56]  piece of context to kind of make transparent is that i'm designing this uh explicitly for companies who
[1004.56 --> 1009.60]  have chosen to go with the so-called microservice architecture or service oriented architecture
[1009.60 --> 1017.48]  and in my experience and i think correctly that is something that a company or an organization should
[1017.48 --> 1023.20]  do only once they reach a certain size so we were talking about containers a little bit earlier
[1023.20 --> 1029.06]  and often i think containers and microservices end up in the same bag of tricks they end up on the same
[1029.06 --> 1035.24]  like hacker news homepage and they are related but i think and i i i feel they they serve orthogonal
[1035.24 --> 1041.98]  kind of ends they they do they do different things containers are a solution for a technical problem
[1041.98 --> 1048.04]  of uh continuous integration of continuous deployment of like getting your actual code
[1048.04 --> 1053.00]  onto machines and running it in a predictable and reproducible way and they're great for that right
[1053.00 --> 1059.64]  whether it's whether it's apse open container format docker like they solve this very technical problem
[1059.64 --> 1066.74]  um microservices on the other hand they can help with technical things but fundamentally they're not
[1066.74 --> 1071.44]  solving a technical problem they're solving an organizational problem they're solving the problem of
[1071.44 --> 1077.76]  too many cooks in the kitchen too many engineers wanting to touch the same uh fundamentally the same
[1077.76 --> 1084.94]  software project and what they allow you to do is decouple workflows and component life cycles in a way that
[1084.94 --> 1091.58]  increases the uh forgive the like agile speak for a moment but increases the velocity of your organization
[1091.58 --> 1100.82]  right so uh in my opinion companies that are adopting microservice architectures are uh of a minimum size
[1100.82 --> 1105.92]  and i sort of point this out on the go kit website they're probably at least 100 engineers
[1105.92 --> 1112.24]  uh maybe you can bring that down to 50 but probably not fewer than that go kit isn't really targeting
[1112.24 --> 1118.00]  organizations that are fewer than 50 engineers uh not to say you can't use it but that's just not
[1118.00 --> 1124.20]  where we're kind of uh focusing our energy um and it's at that scale in my opinion that microservices
[1124.20 --> 1129.48]  really begin to make sense when you can decouple teams from each other's life cycles when you don't
[1129.48 --> 1135.42]  have to have these deployment dependencies when you can sort of treat other teams and other services
[1135.42 --> 1143.06]  within your organization as uh in some sense a black box with an api that you can talk to and interact
[1143.06 --> 1149.08]  with to accomplish your own specific business goals uh this is the context where go kit is kind of
[1149.08 --> 1155.40]  designed to shine so that's sort of microservice architecture so let's pause there for just a second
[1155.40 --> 1161.34]  then so you mentioned microservices or service oriented architecture some other options you have
[1161.34 --> 1168.48]  monolith soa can does it make sense to break down i guess the different options to developers and
[1168.48 --> 1173.40]  different options to those who are architecting services inside of organizations that are 50 to 100
[1173.40 --> 1181.04]  or more developers yeah sure um obviously like the buzzword is monolith versus microservice right
[1181.04 --> 1187.56]  it just leans out to a really awesome article i uh not chad fowler martin fowler i think monolith
[1187.56 --> 1193.78]  first it was his uh the title of it so it's it's catchy yeah yeah and i think he's on to something
[1193.78 --> 1200.24]  um kind of glossing over the details in general i would agree that if you're a small team trying to
[1200.24 --> 1205.96]  find market fit or whatever you're doing with your venture capital money um it makes a lot of sense to
[1205.96 --> 1213.96]  start with a monolith because the uh uh the velocity you can get in a but with four people crammed
[1213.96 --> 1220.26]  around a table is like super high and uh microservices carry like real frictional costs
[1220.26 --> 1227.20]  that only make sense to pay when the benefits you get are bigger than the costs and that only happens
[1227.20 --> 1234.28]  when your team is quite large i think um yeah so the question is like uh sort of the evolution right i
[1234.28 --> 1240.68]  think when when teams start on a product or an idea monolith makes a lot of sense and to be clear
[1240.68 --> 1247.04]  monolith is the idea that all of your code is deployed in effectively a single binary um as a
[1247.04 --> 1253.94]  single application to one or more application servers and any change you make means you rebuild
[1253.94 --> 1258.44]  and redeploy the whole thing even if you just change you know the search function you're going to
[1258.44 --> 1264.94]  rebuild and redeploy the entire application um and that's fine for a long time actually i think
[1264.94 --> 1271.32]  a lot of companies can stay in that mode for years until they grow to a certain size
[1271.32 --> 1277.80]  what ends up happening is when you get to a certain size uh changes that you want to apply
[1277.80 --> 1282.76]  and i feel like i'm just kind of reciting a history now that everybody has already heard a thousand times
[1282.76 --> 1287.64]  uh but just for the sake of completeness uh the changes that you want to make uh start conflicting
[1287.64 --> 1292.50]  with the changes that other people want to make and uh you start having this sort of friction
[1292.50 --> 1298.46]  deployment related friction um and at this point you start thinking wouldn't it be nice if i could
[1298.46 --> 1304.76]  deploy the search function totally independently of the uh the user graph function or whatever the
[1304.76 --> 1310.40]  the front end or whatever it may be and um when you start having these conversations around the
[1310.40 --> 1314.36]  water cooler then microservices begin to make sense there's a whole lot of costs that come
[1314.36 --> 1320.68]  with decoupling uh into independent processes that communicate over the network uh the complexity is
[1320.68 --> 1326.28]  actually really uh in my opinion undervalued by people who are microservice champions but despite
[1326.28 --> 1331.36]  all that i think they still do make sense once you get past a certain scale and um yeah so that's the
[1331.36 --> 1340.96]  evolution as i see it so that's that's that and then you got the i guess the focus here you said is 50
[1340.96 --> 1345.68]  is as far down as 50 you've actually bent your own rules you said 100 at first and now you say 50
[1345.68 --> 1352.08]  but that that's that's okay because we're trying to get go to a an even playing field and it's really
[1352.08 --> 1357.12]  focused towards the modern enterprise and you mentioned uh if those out there listening to this
[1357.12 --> 1362.58]  have heard your talk you mentioned that it's not companies like apple ibm bank of america goldman
[1362.58 --> 1366.16]  sacks things like that it's it's not your large corporations that typically you might think of when
[1366.16 --> 1372.20]  you think modern enterprise it's more like google amazon twitter netflix facebook spotify or even your
[1372.20 --> 1376.98]  previous all-modern which is soundcloud and they sort of set the tone for the industry in terms of
[1376.98 --> 1384.98]  the way they build software that is consumer focused and user experience focused and now you're growing
[1384.98 --> 1391.16]  your team so when when you had this idea for gokit and it was back at fosdum you're thinking well what
[1391.16 --> 1399.44]  can i talk about gokit is what was born um what exactly is gokit when you break it down yeah so gokit
[1399.44 --> 1405.74]  fundamentally is a collection of pieces um that you that play well together but that you can kind
[1405.74 --> 1413.16]  of opt into one by one and the idea is um you are in an organization that's pretty big and you're in a
[1413.16 --> 1419.66]  team that is deploying a bunch of services or microservices to accomplish specific business goals
[1419.66 --> 1424.54]  so maybe you have a search service maybe you have a user service maybe you have a authentication service
[1424.54 --> 1429.70]  or something like this uh these services as they exist today may be written in a number of languages
[1429.70 --> 1435.72]  maybe ruby maybe scala whatever and um you have some idea that you'd like to use go and i think
[1435.72 --> 1442.04]  that idea makes a lot of sense because go is in many in my opinion and in many ways sort of the perfect
[1442.04 --> 1448.08]  language for microservices um so what gokit is is a collection of things you can kind of compose in
[1448.08 --> 1455.18]  and produce what i call a well-behaved microservice and well-behaved means a lot of things it means
[1455.18 --> 1462.30]  well-behaved sort of inside of itself that means proper logging proper telemetry and instrumentation
[1462.30 --> 1469.30]  um proper life cycle management of components stuff that keeps your process on your on your linux system
[1469.30 --> 1476.46]  happy uh and keeps your uh telemetry and your metrics and sort of the business layer up to date and
[1476.46 --> 1483.06]  correct and that sort of thing um but playing nice also means talking playing nice with other services
[1483.06 --> 1490.26]  in your in your infrastructure and so here there's a whole suite of things that are very subtle very
[1490.26 --> 1497.34]  complex and can fail in a lot of terrible ways and this is the field of distributed programming or
[1497.34 --> 1506.16]  distributed systems theory and gokit really simplifies a lot of it down um we choose as our messaging
[1506.16 --> 1511.72]  pattern so-called messaging pattern we're doing rpc right now so if you know anything about distributed
[1511.72 --> 1517.88]  uh systems you know that there's a lot of ways that processes can talk to other processes right
[1517.88 --> 1524.68]  pub sub request response um async message bus blah blah blah there's a whole litany of these like
[1524.68 --> 1530.56]  zero mq actually implements a lot of these and nano message the spiritual successor implements sort of a
[1530.56 --> 1536.88]  difference that uh we've chosen to isolate down and focus purely on rpc for the time being uh
[1536.88 --> 1543.52]  emphasis on the time being that's just um sort of a optimization so that uh we can iterate quickly
[1543.52 --> 1550.02]  and get a product to market so to speak very quickly so your service is going to play nicely
[1550.02 --> 1555.46]  on the system it's in it's going to uh be an rpc service it's going to call other services
[1555.46 --> 1561.90]  using the rpc messaging pattern and uh it's going to play nicely with them and so that means
[1561.90 --> 1568.12]  gokit is going to give you idioms like circuit breakers on the client side uh rate limiters on
[1568.12 --> 1574.20]  both client and service uh client and server side it's going to give you integration with uh service
[1574.20 --> 1583.06]  discovery components whether you're using uh dns records dns srv records console etcd however you or just
[1583.06 --> 1587.34]  manual configuration however you get services to find out about each other and talk to each other
[1587.34 --> 1592.54]  we're going to have integrations for that um we're going to have integrations with uh distributed
[1592.54 --> 1597.16]  tracing systems in fact we already have an integration with zipkin which is the twitter
[1597.16 --> 1603.80]  sort of distributed tracing infrastructure we have several more sort of planned um and so it's things
[1603.80 --> 1607.92]  like this things that are making services be well-behaved neighbors and these sort of infrastructures
[1607.92 --> 1615.84]  that uh i hope and and i hope other people will agree is something that uh product owners and
[1615.84 --> 1621.14]  and engineering directors want and need to see before they can kind of sign off on go as an
[1621.14 --> 1626.04]  implementation language this stuff exists in scala uh in a number of different ways for example
[1626.04 --> 1633.60]  twitter has something called finagle which is kind of what i'm driving towards it's a similar
[1633.60 --> 1641.72]  collection of components um load balancers and and so forth that make services play nicely in these
[1641.72 --> 1648.38]  kind of environments netflix has a whole suite of tools um i guess the most important one to search
[1648.38 --> 1652.76]  would be something called ribbon but there's all sorts of other like correlated things that can
[1652.76 --> 1657.90]  compose together in the same way and kind of accomplish the same thing although i think most people believe
[1657.90 --> 1662.88]  that uh the netflix stack is a little bit more tailor-made to the netflix architecture twitter stack is a bit
[1662.88 --> 1668.46]  more generic and in that sense gokit is aiming to be a bit more generic even than than finagle uh there's
[1668.46 --> 1673.06]  a couple other ones that do this sort of thing piecemeal airbnb has something called smart stack
[1673.06 --> 1678.72]  which is mostly concerned with service discovery and load balancing and that sort of thing but that's a
[1678.72 --> 1683.96]  bit more infrastructural a bit less libraries that you put in your service um so that's what gokit is
[1683.96 --> 1688.60]  it's a collection of these things that you can take in one by one uh but that play nicely together and
[1688.60 --> 1694.32]  kind of give a positive story uh and a bright future to organizations that are buying into go
[1694.32 --> 1701.12]  perhaps for the first time or perhaps just uh more than they were before very interesting so i guess
[1701.12 --> 1706.64]  the question i think i come up with after this is uh you mentioned a lot of big companies there with a
[1706.64 --> 1714.34]  lot of firepower and i'm not saying you're one little guy but um i'm wondering um you know what part
[1714.34 --> 1725.24]  weave work plays into this um and i guess just your ability to to uh to build what needs to be built to
[1725.24 --> 1730.84]  compete yeah even on a light scale to other organizations building similar things in the
[1730.84 --> 1736.94]  languages like why why will you win why will this not so much win but how will you succeed yeah exactly
[1736.94 --> 1742.50]  one person how are you doing it well um this really gets to the core of what i wanted to talk about
[1742.50 --> 1748.60]  today actually um and what i'm really happy to be on the changelog for which is uh the open source
[1748.60 --> 1754.66]  community right um it's one of my favorite things about the go community and one of the things that
[1754.66 --> 1762.42]  probably has kept me around for longer than i've been part of anything uh in sort of the technology
[1762.42 --> 1771.56]  sphere is that uh the the quality and the intelligence and the friendliness and um just the
[1771.56 --> 1777.74]  the the the level of people involved in in the in the go open source community has been um one of the
[1777.74 --> 1784.16]  nicest things for me and and nothing i've seen in any other uh sort of sphere that i've been in and so
[1784.16 --> 1791.16]  you ask me um i'm just one guy that's definitely true uh this is absolutely a passion project it's
[1791.16 --> 1797.04]  something that i want to see happen it's not something that i'm being funded for um weaveworks is not
[1797.04 --> 1802.98]  not directly uh sponsoring any of this work it's really a nice and weekends sort of gig for me
[1802.98 --> 1808.66]  and i'm motivated purely out of sort of this uh hold on i want to make sure i say the right word
[1808.66 --> 1814.32]  benevolence that's the good one right malevolence is a bad one yeah okay oh is it i didn't know there
[1814.32 --> 1820.12]  was a bad or good educate me well whichever one is good that's that's the one that i have in my heart
[1820.12 --> 1827.22]  um yeah and so um in combination so i i feel like my job is kind of to carry the banner and say hey
[1827.22 --> 1832.24]  uh if if go is going to get to the next level of its success which i i'm sure it will and i and i and
[1832.24 --> 1837.20]  i hope it will uh we're going to need stories like go kit we're going to need things like go kit to get
[1837.20 --> 1843.66]  it there we're going to need buy-in in sort of like the next uh tier of developers which are the
[1843.66 --> 1848.18]  developers that are working at these somewhat larger companies that maybe aren't refreshing hacker
[1848.18 --> 1854.86]  news eight times a day and that still like deserve the benefits that go can provide so i'm kind of
[1854.86 --> 1861.04]  viewing myself as um at the moment definitely the primary developer but more of a sort of community
[1861.04 --> 1866.14]  leader and and i'm hoping uh with the help of the changelog with the help of the talk that i'm going to
[1866.14 --> 1872.48]  do at gopher con in about a week and um with the sort of publicity for lack of a better word that i'm
[1872.48 --> 1877.32]  going to be doing throughout the year to attract people who have similar ideas and i definitely got some of
[1877.32 --> 1883.30]  this uh when i gave the two talks in brussels and in london i was approached by several people in
[1883.30 --> 1888.96]  those communities and saying you know i've been saying the same thing to my guys at my organization
[1888.96 --> 1896.30]  my girls at at my university and um and we really feel that the time is right for this and we're
[1896.30 --> 1901.64]  excited to contribute and indeed we've had a couple of really great uh powerful contributors so far
[1901.64 --> 1909.24]  uh top of my mind is chris hines who's been really uh incredible in helping me with the log package
[1909.24 --> 1914.82]  we've iterated on a few api designs we're continuing to iterate i think we're going to produce definitely
[1914.82 --> 1921.82]  even if you use nothing else in gokit the gokit log package is going to be the premier uh value
[1921.82 --> 1927.64]  add log package in the in the go universe and there's already that's a very crowded field so it's a big
[1927.64 --> 1933.14]  statement but i think it's going to get there absolutely um my uh friend uh here in berlin
[1933.14 --> 1940.14]  thomas sanart has helped me a lot with um uh iterating on the endpoint uh api design and like
[1940.14 --> 1946.20]  the core kind of components there uh canonical friend of mine roger pepe i hope i'm saying his
[1946.20 --> 1952.02]  name correctly uh he's helped me a lot with the rate limiter um and we have like a core stable of
[1952.02 --> 1956.58]  contributors a couple of people from digital ocean are very interested as well and and have helped me out
[1956.58 --> 1961.52]  so i hope this grows and you're absolutely right to say just one guy isn't going to be able to
[1961.52 --> 1968.88]  you know uh produce code to the same level that twitter is able to do but i hope that uh my instinct
[1968.88 --> 1973.82]  is correct and that this is something that people want and with a little bit of uh help i'll be able
[1973.82 --> 1979.16]  to attract the kind of people that can make patches and uh push it forward with me absolutely
[1979.16 --> 1982.66]  that's what we're here for and i'm glad you mentioned digital ocean because it is time for a
[1982.66 --> 1986.50]  sponsor break and i'm going to change the order of it top top was supposed to be the first
[1986.50 --> 1991.12]  sponsor of the show but uh well technically the slot number two but i'm going to move digital
[1991.12 --> 1995.64]  ocean up just because you mentioned them uh so we're gonna take a break and hear from our friends
[1995.64 --> 2001.44]  at digital ocean who love this show and obviously love what peter's doing with with go kit and is
[2001.44 --> 2009.00]  supporting it so take a listen we'll be right back i have yet to meet a single person who doesn't love
[2009.00 --> 2014.18]  digital ocean if you've tried digital ocean you know how awesome it is and here at the change log
[2014.18 --> 2021.18]  everything we have runs on blazing fast ssd cloud servers from digital ocean and i want you to use
[2021.18 --> 2028.06]  the code change log when you sign up today to get a free month run a server with one gig of ram and 30
[2028.06 --> 2035.32]  gigs of ssd drive space totally for free on digital ocean use the code change log again that code is
[2035.32 --> 2040.58]  change log use that when you sign up for a new account head to digital ocean.com to sign up
[2040.58 --> 2047.98]  and tell them the change log sent you all right we're back and i guess peter since you
[2047.98 --> 2055.16]  mentioned digital ocean we just had that super awesome sponsor spot for digital ocean uh and you
[2055.16 --> 2062.96]  also mentioned your upcoming talk which is uh we're recording this uh let's see what's today today is
[2062.96 --> 2072.04]  june 30th yeah and we'll publish this on july 3rd and on july 8th or 9th i'm not sure which day you
[2072.04 --> 2077.56]  speak you'll be at gopher con you'll be talking about go kit so on one of those days you'll be
[2077.56 --> 2082.58]  giving a talk going even more in depth so if you're a change load listener and you're not going to gopher
[2082.58 --> 2087.64]  con it's there's still probably about a half a second to buy a ticket um maybe they're all gone i don't
[2087.64 --> 2092.86]  know but we'd love to see you there and if you see us say hello um but we're work with gopher con
[2092.86 --> 2098.26]  we're doing video work with them this year where if uh if you see us running around we got cameras in
[2098.26 --> 2105.12]  our hands say hello it's me myself um which is me and myself right uh we got jared and we also have
[2105.12 --> 2111.44]  donald i call him dk but if you if you see us around say hello we'll every day we have plenty of
[2111.44 --> 2115.00]  them but every day we'll be wearing a change log t-shirt because what other uniform would we wear
[2115.00 --> 2123.76]  um but you'll be there uh gopher con is awesome uh 1500 people how excited are you to to come back
[2123.76 --> 2128.32]  over to the u.s you were just what in in california recently right yeah that's right i was just there
[2128.32 --> 2134.80]  for um docker con yeah and i think that was i don't know how many people that was but it was on the same
[2134.80 --> 2141.40]  order of magnitude and docker con was huge it was really a gigantic gigantic conference i'm looking
[2141.40 --> 2146.22]  forward to i've never been to well i guess i have i've been a rails conference stuff like that
[2146.22 --> 2153.38]  and i think that might have borderline on like 800 900 ish at the time now it's much more um
[2153.38 --> 2158.02]  but it's been a while since i've been to such a large conference and then to be
[2158.02 --> 2164.20]  in the role of documenting what's happening it kind of blows my mind that we'll have to like catch up
[2164.20 --> 2169.74]  with 1500 people somehow yeah it's gonna be some way but but anyway it's enough to say gopher con's
[2169.74 --> 2174.02]  awesome you'll be there you'll be speaking there that's right and that's uh yet another plug but
[2174.02 --> 2179.24]  let's dive deep uh now that we're back from that break let's dive deep into gokit and its components
[2179.24 --> 2186.26]  and their statuses and and kind of what what makes up gokit itself not just this idea of it
[2186.26 --> 2191.02]  yeah um where should we begin there so probably conceptually the place that makes sense to start
[2191.02 --> 2197.34]  is um package endpoint which is kind of uh there's not much there i think there's like three things
[2197.34 --> 2205.12]  there but the idea is to define a common interface or a common uh function signature that everything
[2205.12 --> 2211.22]  else can be built around and this gets back to what i said uh that are are the way we're starting
[2211.22 --> 2217.80]  is by assuming rpc the rpc messaging pattern so in package endpoint we have uh what i was able to
[2217.80 --> 2226.36]  figure out as the lowest common denominator rpc method signature and it's kind of what you'd expect
[2226.36 --> 2232.44]  func uh takes a request returns a response but because it's in go it returns a response and an
[2232.44 --> 2240.00]  error and because we need to thread a lot of things through this uh it also takes a context and a
[2240.00 --> 2244.40]  context is a thing that was released not too long ago maybe a year maybe a little bit more
[2244.40 --> 2252.42]  from google it's this value add package and it is a little bit uh awkward when you first see it
[2252.42 --> 2258.66]  but it's a parameter that you can thread through or rather you should thread through all of the
[2258.66 --> 2267.98]  functions or all of the uh points in your request path and it allows you to do a lot of really handy
[2267.98 --> 2274.60]  stuff uh at a basic level it allows you to thread information sort of across um stack boundaries
[2274.60 --> 2281.32]  across thread boundaries across contact basically across bounded contexts within not only a single process
[2281.32 --> 2291.36]  but from uh one service to another and uh it also lets you set up nice um i forget exactly what the term is
[2291.36 --> 2299.12]  sort of like a hierarchy of uh uh component ownership process ownership life cycle ownership so
[2299.12 --> 2305.68]  uh if you're a component and you want to scatter gather 10 requests to 10 other components you sort of
[2305.68 --> 2312.34]  can set a sort of timer send those requests off and then the first one that comes back can for example
[2312.34 --> 2318.14]  cancel all the other ones and they'll terminate and clean up nicely so the context is something that
[2318.14 --> 2324.40]  gives these these sort of nice semantics and um it's been around out in the wild for i guess about a
[2324.40 --> 2331.32]  year uh a lot of things have have made good use of it and so gokit has chosen that as its mechanism of
[2331.32 --> 2337.36]  yeah taking information across across context boundaries so that's a good place to start and
[2337.36 --> 2342.82]  once you get your head around that everything else kind of opens up like a flower so you got uh
[2342.82 --> 2347.20]  package endpoint in no particular order but i'm going to read them down from from the readme package log
[2347.20 --> 2353.00]  package metrics patrick package endpoint which we just talked about i'll not say package anymore
[2353.00 --> 2357.46]  because it prefaces all them but transport circuit breaker which we sort of talked about a little
[2357.46 --> 2363.32]  bit in theory earlier yep load balancer rate limiting or rate limit those are all implemented
[2363.32 --> 2369.54]  um and then in prototyping you've got tracing you've also got client patterns which seems to be
[2369.54 --> 2373.90]  i'm not really sure what that makes up but and then you got service discovery which is impending
[2373.90 --> 2379.28]  and then you got some other i'm sure some other ideas ad services is uh is implemented as well
[2379.28 --> 2387.36]  yep so let's start at the top i guess um login metrics are maybe the simplest ones uh in the sense that
[2387.36 --> 2393.36]  they just do a very specific thing package log is like many other log packages kind of floating out
[2393.36 --> 2401.78]  there in the wild uh it encodes some opinions about how microservices should do logging and uh i really
[2401.78 --> 2407.82]  have chris heinz to think thank for pretty much all of this but something that we both agree on and that
[2407.82 --> 2415.60]  was in the initial rfc uh which was contributed by a digital ocean guy by the way um was that microservices
[2415.60 --> 2423.36]  or rather package log in gokit uh enforces strictly the idea of structured logging so if you're familiar
[2423.36 --> 2430.52]  with the standard go logging package you can write log dot printf and then just sort of an arbitrary
[2430.52 --> 2437.68]  string and it's gokit's uh opinion that that's kind of bad practice and what all of your logs should
[2437.68 --> 2445.02]  look like is key value pairs so if you wanted to log for example starting a thrift server
[2445.02 --> 2453.42]  on this uh host and port with uh this particular piece of debug information you wouldn't write that
[2453.42 --> 2459.56]  sentence out in a in a printf string and drop your variables in rather you would log the structured
[2459.56 --> 2468.90]  data transport equals thrift address equals whatever it is debug equals blah blah blah and then log that
[2468.90 --> 2476.14]  sort of collection of pairs and you do pay a cost in sort of human readability but it's gokit's opinion
[2476.14 --> 2483.34]  that that cost is more than made up for in the ability to programmatically uh read those logs parse
[2483.34 --> 2490.70]  those logs and hopefully at 2am god forbid uh make sense of those logs uh so that's sort of the the one
[2490.70 --> 2496.36]  core opinion about log and then we have a lot of stuff that kind of wraps that core opinion and gives
[2496.36 --> 2503.24]  nice value add stuff like leveled logging is in the pipeline uh contextual logging different output
[2503.24 --> 2508.68]  formats another important thing about package log is that it's not only for application logging it's also
[2508.68 --> 2515.32]  equally usable for so-called structured log log format data this is the kind of stuff that you might push
[2515.32 --> 2522.58]  into a kafka instance this is uh click tracking this is general analytics it's anything that needs to have
[2522.58 --> 2529.42]  a stronger sort of qos than simple application logging that might end up in uh an elk stack an elastic
[2529.42 --> 2537.92]  search log stash kibana stack so log is good for all these things and a natural sister or brother would
[2537.92 --> 2544.12]  be metrics precisely and metrics is also simple uh in the sense that it does sort of one thing that's
[2544.12 --> 2548.96]  independent from other things uh it lives in your process and actually maybe we should take a step back
[2548.96 --> 2554.48]  and ask like what is metrics what is instrumentation uh lots of people have i love your question do it
[2554.48 --> 2561.78]  yeah yeah there are there are different ideas um there are services like airbreak right where you
[2561.78 --> 2568.14]  sort of trap all the exceptions or errors in your code and then whenever you see one you emit a piece of
[2568.14 --> 2573.88]  information to a third-party server that collects them and tells you uh what parts of your system are crashing
[2573.88 --> 2581.82]  or whatever that's kind of a type of instrumentation i guess but it's not what metrics is uh something a
[2581.82 --> 2590.36]  bit closer would be uh a system like graphite or statsd where uh rather than trapping errors what you're
[2590.36 --> 2595.88]  doing is going through your code and you're instrumenting all of the important bits and what is an important
[2595.88 --> 2603.82]  bit one thing might be uh the number of requests that hit you on uh on an http service
[2603.82 --> 2612.20]  the duration of those requests so average mean uh mean median max min this sort of thing uh not only
[2612.20 --> 2620.58]  the the basic sort of statistics but also bucketed over quantiles so mean uh 50th percentile latency
[2620.58 --> 2626.84]  99th percentile latency this sort of thing um so that's kind of more what i'm getting at here and
[2626.84 --> 2633.78]  metrics package metrics in gokit represent sort of a distilled uh boiled down
[2633.78 --> 2642.70]  version of what i and many of my contributors have found is important we expose three core concepts
[2642.70 --> 2650.28]  that is the counter the histogram and the gauge and we provide different backends that implement each of
[2650.28 --> 2655.94]  these counters you can or each of these metrics you can hook them all up together in a single sort of
[2655.94 --> 2662.98]  api you can use one or as many as you want and so the idea is you should aggressively instrument your
[2662.98 --> 2669.26]  code using the package metric sort of interfaces and then once a program startup in your funk main
[2669.26 --> 2675.94]  you uh wire up the interface to the back end of your choice and this is in keeping with our
[2675.94 --> 2681.10]  sort of philosophy gokit philosophy of working with the infrastructure that you have you almost
[2681.10 --> 2687.62]  certainly as an organization are going to have a statsd server or graphite server or whatever it is
[2687.62 --> 2693.56]  existing and receiving metrics uh if you're if you're a team of 50 engineers so we want to work
[2693.56 --> 2698.68]  with that and we have adapters for many of the common ones uh the one i'll plug is prometheus that
[2698.68 --> 2704.92]  was also developed at soundcloud and um yeah we think that's probably the best model for this kind of
[2704.92 --> 2709.40]  thing yeah we've heard good things about prometheus as well around here we've been meaning to to to do a
[2709.40 --> 2713.94]  bit more coverage on it too so definitely if you need an intro let me know i i know the developers quite
[2713.94 --> 2717.78]  well and they're also going to be a gopher con well that would be awesome let's make it happen
[2717.78 --> 2722.16]  yeah definitely no it's a really cool piece of software and uh it does its job quite well
[2722.16 --> 2730.42]  so adapters into some of the most common uh metric packages uh ex is it exp var is how you pronounce it
[2730.42 --> 2736.44]  yeah well xvar is one of the xvar okay uh standard library packages in go and it's really like bare bones
[2736.44 --> 2743.04]  simple stuff but pretty cool um you can export kind of instantaneous view of of certain certain types of
[2743.04 --> 2749.52]  metrics and um just kind of dump them by hitting a specific http endpoint so it's a good like entry
[2749.52 --> 2754.70]  level bare bones type of exposition and development or something like that yeah sure sure gotcha okay
[2754.70 --> 2761.58]  well very cool that makes sense so counters gauges histograms those all dump data into these known
[2761.58 --> 2767.56]  metrics packages precisely that that help you sort of dive deeper into them as as you need to
[2767.56 --> 2774.54]  um what's next so if we walk down the stack we can kind of start looking at uh the value add
[2774.54 --> 2781.72]  components uh and this is stuff that uh benefits from the common endpoint uh api or the common endpoint
[2781.72 --> 2787.36]  interface this is things like circuit breaker load balancer rate limiting and these are things that
[2787.36 --> 2795.46]  you probably can intuitively guess that a microservice needs but it actually turns out it it takes some
[2795.46 --> 2801.00]  thinking to get it right and this is part of the value proposition of go kit uh we have contributors
[2801.00 --> 2806.86]  who have thought about it and have made mistakes implementing circuit breakers and load balancers and
[2806.86 --> 2813.24]  uh prevent you from making those same mistakes hopefully so each of them is something that you want to wire
[2813.24 --> 2819.50]  into your microservice either at the client side when you're connecting to other services or on the server
[2819.50 --> 2825.12]  side when you're receiving connections from other services and they prevent you from behaving badly
[2825.12 --> 2829.56]  so let's start with circuit breaker uh this is something that you would typically put in the
[2829.56 --> 2838.52]  client side uh and what it does is if it detects that requests to a specific back end to a specific other
[2838.52 --> 2847.56]  service are failing regularly above some threshold let's say it will prevent other requests from going
[2847.56 --> 2853.66]  out until it detects sort of a healthy state and the idea here the reason it's called circuit breaker is
[2853.66 --> 2860.50]  it's kind of like a fuse right if you put too many uh uh amps through a fuse it's going to explode and
[2860.50 --> 2865.72]  prevent you from starting a fire in your house right great naming i like the naming yeah yeah it's a it's a
[2865.72 --> 2871.62]  cool name it's a pretty common pattern but until you've had this sort of thundering herd where a failure
[2871.62 --> 2875.94]  in one service brings down your entire company and it takes like hours to get everything restarted and
[2875.94 --> 2881.56]  back online uh you don't really understand how important it is to have these things and it is important
[2881.56 --> 2886.28]  and go get chips with one actually several you can kind of pick your favorite type of implementation
[2886.28 --> 2893.96]  and um wire it into hopefully every request that you make and it's important to note that circuit
[2893.96 --> 2899.84]  breakers aren't really a mechanism of solving load problems so if you're under provisioned in your
[2899.84 --> 2905.12]  infrastructure circuit breakers aren't going to fix that what they do is prevent bad problems from
[2905.12 --> 2910.92]  becoming terrible problems and for that reason uh they're very important does this tie into load
[2910.92 --> 2915.52]  balancer then yeah in a way um you would you would certainly wire circuit breakers and load balancers
[2915.52 --> 2920.34]  together uh where circuit breaker is kind of something that only comes into play when things go
[2920.34 --> 2924.44]  wrong uh load balancer is something that's in play all the time when things are going right
[2924.44 --> 2931.50]  the idea is that if you have uh a set of services that are horizontally scaled multiple instances of the
[2931.50 --> 2936.90]  same thing to to support the amount that the millions of requests per second that i'm sure your
[2936.90 --> 2943.32]  startup is getting um load balancer is something you're going to install in your client side to
[2943.32 --> 2948.28]  distribute the load across all of those instances and there's a lot of ways you can do that um
[2948.28 --> 2953.96]  you can do very simple things like picking a random instance every time you can do well-known
[2953.96 --> 2961.08]  algorithms like round robin you can use an algorithm that sort of weights each instance based on
[2961.08 --> 2967.22]  uh criteria like average response times you send more requests to the to the healthier instances
[2967.22 --> 2974.14]  you can weight them based on locality based on data center um so package load balancer is something
[2974.14 --> 2979.84]  that allows you to implement those types of algorithms across sets of otherwise identical
[2979.84 --> 2989.10]  instances of services and we provide a lot of hooks for uh getting sets of instances and so this is
[2989.10 --> 2993.62]  sort of the service discovery component given you know you want to talk to the user service
[2993.62 --> 3000.88]  and how do you translate the string user service to a set of instances well this is a whole uh probably a
[3000.88 --> 3008.12]  multi-hour changelog podcast in itself but we provide hooks for a number of common solutions to that problem
[3008.12 --> 3014.66]  and so that's all sort of wrapped up into the load balancer package how is that uh different from rate
[3014.66 --> 3020.50]  limiting uh so rate limiting is something that you can stick either on the client side or the server
[3020.50 --> 3027.12]  side and of of your service and it's something that maybe is a little bit less useful or at least
[3027.12 --> 3032.74]  less generally applicable but if you know that for example you're calling out to the facebook api
[3032.74 --> 3039.26]  and you know that you don't want to do more than 10 requests a minute or 100 requests a second or
[3039.26 --> 3044.20]  whatever it happens to be you can declare that up front you can stick a rate limiter on that client
[3044.20 --> 3049.80]  connection and you can say i only want to do 100 requests a second max and then you can determine
[3049.80 --> 3055.56]  what to do with any requests that happen to go above that limit uh you can kill them immediately
[3055.56 --> 3060.84]  with an error you can tell them to wait a while whatever whatever is right for you uh that package
[3060.84 --> 3067.42]  is pretty uh bare bones at the moment but there's hooks for doing things like hooking into a central lock
[3067.42 --> 3072.68]  store so that you can enforce for example a consistent rate limit across multiple instances
[3072.68 --> 3078.96]  um yeah the sky's the limit there but that's what that does so just to summarize here we got log
[3078.96 --> 3085.20]  metrics endpoint transport circuit breaker load balancer and rate limit and those are all implemented
[3085.20 --> 3091.34]  and ready to use today that's right and tracing is in prototyping stage along with client patterns
[3091.34 --> 3096.72]  can we talk through uh those two pieces there sure so tracing is something that um maybe a lot of people
[3096.72 --> 3102.34]  some people some people know about some people don't the idea is when you have a uh microservice
[3102.34 --> 3106.96]  architecture and you have a bunch of things talking to each other typically what happens is a request is
[3106.96 --> 3111.42]  going to hit your website for example it's going to go to some service that service is going to need
[3111.42 --> 3117.38]  information from a bunch of other services each of them in turn may need information from more services
[3117.38 --> 3121.74]  and so what happens is you create this sort of tree this sort of hierarchy of requests
[3121.74 --> 3128.88]  that was all spawned by a single incoming request and once you get past a certain size or a certain
[3128.88 --> 3136.20]  level of complexity it's really important to be able to look at that call graph and see how long each
[3136.20 --> 3143.44]  individual thing takes uh where your hot spots are um this sort of thing and the way to do that is with a
[3143.44 --> 3149.58]  so-called distributed tracing framework uh the canonical one in the open source world is uh well i should
[3149.58 --> 3155.02]  take a step back this all became sort of public knowledge uh quite a long time ago i think maybe
[3155.02 --> 3161.92]  10 years ago at this point when google released a a paper called dapper dapper is the name of the google
[3161.92 --> 3166.16]  internal system that does this and not to say it was the first system that does this but that's sort of
[3166.16 --> 3171.12]  when it became en vogue and so in google fashion they released the paper but not the implementation
[3171.12 --> 3177.50]  uh the apache folks i think maybe it was twitter initially i don't have my history right on this
[3177.50 --> 3184.38]  somebody uh said about creating an open source implementation of the dapper paper which uh when
[3184.38 --> 3189.70]  complete they called zipkin and zipkin is what you can kind of download and use today if you're running
[3189.70 --> 3195.84]  on the jvm um there's a number i guess that was three or four years ago that that became public
[3195.84 --> 3200.38]  knowledge there's a number of similar systems now in other languages there's a number of zipkin
[3200.38 --> 3208.56]  implementations in other languages um and so gokit provides a package tracing that does this sort of
[3208.56 --> 3214.10]  thing we have a zipkin implementation at the moment so if you have a zipkin infrastructure in your
[3214.10 --> 3220.84]  organization we can uh we can interact with that uh we have planned support for a similar system from
[3220.84 --> 3226.34]  a company called source graph which is also another prominent member of the go community uh they have a
[3226.34 --> 3231.42]  system called app dash which does basically the same thing as far as i understand i plan on tackling
[3231.42 --> 3237.02]  that at some point in the near future and um there's actually a couple of other ones uh there's another
[3237.02 --> 3243.70]  i think apache project called h trace there's something uh from netflix with a funny name that begins with s
[3243.70 --> 3250.56]  that i can't remember um actually during gopher con there's a distributed tracing working group that's
[3250.56 --> 3254.76]  going on in budapest that unfortunately i'm not going to be able to be a part of uh but they're
[3254.76 --> 3259.82]  sort of having a symposium and talking about the future of this sort of thing so keep an eye out in
[3259.82 --> 3266.16]  the next month or two i'm sure we'll see some interesting news there very interesting so a lot
[3266.16 --> 3270.02]  of stuff happening around that i mean especially the support with a lot of new things i've heard
[3270.02 --> 3277.96]  there too uh zipkin app dash uh dapper and like you mentioned it is uh similar to how kubernetes
[3277.96 --> 3283.90]  came out recently it came out as a paper first and well sort of what was the kubernetes is its own
[3283.90 --> 3289.76]  thing but then the other thing they recently announced similar borg yeah borg yeah that's
[3289.76 --> 3293.26]  what i was thinking i think you've helped me there it's like they release this paper but then you also
[3293.26 --> 3298.72]  have kubernetes which is similar to what what's happened with borg exactly i think they would
[3298.72 --> 3305.74]  say that kubernetes is like the the if they were able to to redo borg and and fix all of the problems
[3305.74 --> 3310.84]  that they discovered that that would be what kubernetes is and kind of made a bit uh more
[3310.84 --> 3316.66]  straightforward for the open source kind of public world at large yeah exactly you got zipkin
[3316.66 --> 3322.22]  app dash and what was the other one h trace h trace and then there was there was another one
[3322.22 --> 3326.24]  that you mentioned but i didn't get a chance to jot that one down yeah uh i didn't get a chance to
[3326.24 --> 3329.88]  remember the name of it either uh all right we'll go back and list till we get in the show notes i was
[3329.88 --> 3335.74]  just thinking for the show notes sakes to to make sure we get it all go in there yeah um let's see
[3335.74 --> 3342.02]  where are we at on the list here i guess i closed that i closed that list let me get back to the
[3342.02 --> 3351.28]  readme so i can get back there next is uh so client patterns exactly this has no link there is no
[3351.28 --> 3358.28]  description help me out here so yeah the idea is uh you write a service and your service has an
[3358.28 --> 3362.96]  implementation and people can call it and this is something i haven't mentioned yet actually but it's
[3362.96 --> 3367.80]  actually also pretty core to the go kit idea uh you're going to have a service and it's going to
[3367.80 --> 3373.90]  be implemented in go and um you're going to do your implementation once but you probably want to be
[3373.90 --> 3380.12]  able to expose that service on any number of different transports maybe your company is using thrift
[3380.12 --> 3386.60]  exclusively behind the scenes maybe it's using just standard http json semantics maybe it's using
[3386.60 --> 3392.14]  uh bleeding edge g rpc which is actually very similar to kubernetes it's like the
[3392.14 --> 3399.02]  open source the google open source version of an internal project called stubby an internal rpc framework
[3399.02 --> 3406.12]  so i don't know we have a bunch of uh so-called transports that allow you to expose your service
[3406.12 --> 3413.10]  in different ways and a core idea of go kit is that you should write your implementation once using
[3413.10 --> 3419.26]  sort of the rpc pattern but then you should be able to expose it on an arbitrary number of transports
[3419.26 --> 3424.96]  simultaneously in the same process and so um yeah that's an important thing that i sort of forgot
[3424.96 --> 3432.72]  to mention um so in support of that um you have the service running on some transport and you can
[3432.72 --> 3440.10]  hand write the code to talk to that if it's http json it's probably pretty straightforward but if it's a
[3440.10 --> 3445.96]  thrift server for example it's a little bit more laborious and so client patterns is just my way of
[3445.96 --> 3452.04]  saying given you're exposing a service on any one of our supported transports we want to be able to
[3452.04 --> 3459.56]  show you an example client you can build that gives you the same semantics the same uh go language level
[3459.56 --> 3465.94]  rpc semantics to talk to that service uh over the chosen transport so if you have some service that
[3465.94 --> 3472.14]  adds two numbers together and you expose it on thrift g rpc and http then we want to be able to say
[3472.14 --> 3479.60]  you can create a thrift g rpc or http uh client that can talk to that service and you just get the
[3479.60 --> 3485.16]  really like straightforward basic call response semantics on it so uh client patterns is just
[3485.16 --> 3491.00]  building those things up basically and making uh good examples it sounds like service discovery might
[3491.00 --> 3497.60]  play a little bit into that in terms of discovering different uh services exactly exactly so yeah it's a
[3497.60 --> 3503.60]  bit of a tautology but yeah uh precisely you're you're gonna as part of a client package you're going
[3503.60 --> 3510.82]  to figure out how to get to the services you want to talk to and that's a question that's answered uh
[3510.82 --> 3516.40]  differently in different infrastructures but yeah absolutely you're going to wire in uh service
[3516.40 --> 3521.60]  discovery into your load balancer all on the client side and then use that in combination with
[3521.60 --> 3525.68]  circuit breaker or whatever else to talk to those remote services
[3525.68 --> 3532.18]  that's interesting i mean this um i mean as we walk down this entire component status list
[3532.18 --> 3538.00]  and everything you're doing with it i mean it starts to really make a lot more sense in terms of
[3538.00 --> 3544.30]  what gokit is trying to accomplish and uh reminding all the listeners too that you know quite a bit of
[3544.30 --> 3549.72]  this is implemented we didn't even talk about the api stability document and that that piece yet there but
[3549.72 --> 3557.28]  uh if um if you want to talk about ad service real quick and then just sort of go through the api stability
[3557.28 --> 3565.70]  um which also talking about these statuses you got adopted implemented prototyping pending uh
[3565.70 --> 3570.38]  yeah so there's several different statuses that it's sort of tricky to to navigate around as a as an
[3570.38 --> 3575.84]  outsider yeah yeah um and that's totally my bad this is all sort of in a pre-alpha state and the words
[3575.84 --> 3579.26]  don't really mean a lot well you are one person and we're trying to we're giving you some slack
[3579.26 --> 3585.40]  here so we're not holding your feet to the fire peter yeah much appreciated um yeah it's it's just
[3585.40 --> 3591.14]  a sort of a signal to the to the anyone who might stumble by as to where we are sort of uh in in a
[3591.14 --> 3598.34]  percentage wise in in in accomplishing the goals we set out for ourself um so yeah pretty much
[3598.34 --> 3604.24]  everything is implemented with a with a basic api uh we're not personally gokit like gokit itself is
[3604.24 --> 3610.36]  not in an api stable state um if someone came along filed an issue and said hey here's a much better
[3610.36 --> 3616.62]  api for uh the metrics package take a look uh if indeed they're right then that's going to change
[3616.62 --> 3621.72]  and um yeah we're going to be that way for a little while so this is definitely like alpha quality stuff
[3621.72 --> 3627.84]  right now alpha stage stuff uh but that said the uh the example ad service is sort of the proving
[3627.84 --> 3635.02]  ground for a lot of this it's it's just a directory uh of a of a fake microservice that implements all of
[3635.02 --> 3642.54]  the transports it implements all of the little value add composed in uh features just as a way to feel
[3642.54 --> 3649.60]  get a sense of how all these things play together and um it's it's really an opportunity for me to see if
[3649.60 --> 3655.42]  i'm accomplishing my goals with this thing if if i design my apis correctly this stuff should sort of
[3655.42 --> 3661.04]  fall out naturally and feel very good to to write on the page and if that's not the case i'm going
[3661.04 --> 3667.04]  to see it in ad service and i'm going to need to change things that's interesting so the ad service
[3667.04 --> 3670.90]  essentially is a is a good example for anyone following in our footsteps of this conversation
[3670.90 --> 3676.98]  uh to to look at how it should be implemented how it should work exactly and and as you're working
[3676.98 --> 3682.44]  sort of test privy rounds yeah exactly and i think the thing i'm most proud of that is that when
[3682.44 --> 3688.58]  you look at the the main function and ad service there's no magic at all it's very uh comparatively
[3688.58 --> 3695.10]  long but it's all straightforward nothing nothing like there's no package globals that get sort of
[3695.10 --> 3702.22]  magically pulled in everything is composed uh in this very declarative bump bump bump step-by-step way
[3702.22 --> 3709.80]  that uh is really like for me a joy to read um it's so easy to figure out what's being wired together
[3709.80 --> 3715.10]  how the the information is flowing through the through the object graph this is like really
[3715.10 --> 3721.66]  nice for me and something i'm really seeking to preserve on the notion of the api stability you'd
[3721.66 --> 3727.38]  mentioned that the api is stable but it's not like in quotes stable to the point where you couldn't come
[3727.38 --> 3732.80]  by and change it if someone wanted to listen to this podcast or pick up on what you're doing and step
[3732.80 --> 3739.16]  in and help out in some way yep um does it make sense to uh talk about that uh api stable quote
[3739.16 --> 3743.08]  you have on the the docs there that yeah that you wrote there do you know by heart let me read it for
[3743.08 --> 3748.28]  you no no i've got it in front of me too um and this is actually sort of a conversation that touches
[3748.28 --> 3756.58]  in the broader go ecosystem um one of the most long-standing sort of trouble spots or maybe concerns
[3756.58 --> 3763.34]  in the go world is uh this idea of how do you manage dependencies and how do you make reproducible
[3763.34 --> 3768.82]  builds and how do you enforce things like api stability policies and there's been a number of
[3768.82 --> 3774.16]  solutions to that that have been more or less successful luckily in go 1.5 which is due for
[3774.16 --> 3782.06]  release i think in about a month um we have sort of a canonized blessed uh approach to to this uh
[3782.06 --> 3788.64]  process of so-called vendoring that's going to be baked into the go tool but uh for a go kit really
[3788.64 --> 3793.80]  the api stability policy comes in two parts uh it says first of all if we're going to bring in a
[3793.80 --> 3801.50]  dependency uh we'd prefer to have one that has a stable api so that users of our software don't
[3802.10 --> 3809.38]  get unexpected breakage whenever they import us and we in turn import something else so we prefer to
[3809.38 --> 3815.36]  do that uh given a choice between two packages we'll pick the one with the stable api uh the other
[3815.36 --> 3822.06]  side of the coin is the api of go kit itself is not currently stable so if you want to use go kit
[3822.06 --> 3830.68]  what you should do is vendor it in and this is uh sort of a a process by which in your service you
[3830.68 --> 3836.82]  shouldn't import uh github go kit kit sort of directly you should use some sort of vendoring tool
[3836.82 --> 3843.52]  or some sort of vendoring process to uh vendor that code into your repo directly and uh use it
[3843.52 --> 3850.78]  from that place so that you control the life cycle i guess let's uh let's take a pause there we'll have
[3850.78 --> 3856.16]  one last sponsor break when we come back we'll talk a bit uh i guess about the closing pieces of it i
[3856.16 --> 3861.28]  want to talk to you about the the potential working group and what's going on at uh go for con to see
[3861.28 --> 3867.02]  if there's any sort of get together for go kit enthusiasts or those who want to step up and help
[3867.02 --> 3874.12]  out so let's break we'll come back we'll talk about that top towel is by far the best place to work
[3874.12 --> 3879.74]  as a freelance software developer i had a chance to sit down and talk with brendan banishad the co-founder
[3879.74 --> 3886.10]  and coo of top towel and i asked brendan to share some details about the foundation of top top what
[3886.10 --> 3891.58]  makes top towel different and what makes their network of the elite engineers so strong take a
[3891.58 --> 3898.34]  listen i mean i'm one of the co-founders and i'm an engineer um i studied chemical engineering and to
[3898.34 --> 3903.12]  pay for this super expensive degree i was freelancing as a software developer then by the time i finished
[3903.12 --> 3907.70]  realized that being a software developer was pretty awesome and so i kept doing that
[3907.70 --> 3915.40]  and my co-founder is in a similar situation as well and so we wanted to solve a problem as engineers
[3915.40 --> 3922.26]  and do it from as a network of engineers kind of for engineers by engineers and having that
[3922.26 --> 3928.96]  perspective and and consistently bringing on new team members who also share this really makes top
[3928.96 --> 3934.76]  towel different and that it's a network of engineers not kind of like you have top towel and then the
[3934.76 --> 3940.52]  developers it's never about us and them it's it's always us like everybody at top towel for the most
[3940.52 --> 3944.90]  part refers to top towel as their company and they feel like it's their company and everybody acts like a
[3944.90 --> 3949.46]  core team member even though they're freelancers within the top towel network and all of these
[3949.46 --> 3954.16]  things are extremely important to us all right if you're interested in learning more about what top
[3954.16 --> 3962.86]  towel is all about head to top towel.com slash developers that's t-o-p-t-a-l.com slash developers to
[3962.86 --> 3970.32]  learn more and make sure you tell them the changelog sent you all right we're back uh i guess peter this
[3970.32 --> 3979.22]  has been quite an enlightening trip down go kit slash go slash microservices lane good to hear um i know
[3979.22 --> 3984.88]  i've certainly learned quite a bit and i'm thinking for the listeners sake you know how can they get
[3984.88 --> 3989.46]  involved i know that's one of our coin questions at the tail end of this podcast which we'll get to
[3989.46 --> 3995.02]  here in just a minute or so but um i'm thinking is there a working group at fosdem you got a lot of
[3995.02 --> 4000.22]  enthusiasm around go kit and i'm wondering what's happened since then that that was february this is
[4000.22 --> 4008.42]  obviously june now so not too much time but enough to have some things change and get more uh you got
[4008.42 --> 4012.74]  chris and you got some others so who else is sort of stepping up and what's happening in terms of
[4012.74 --> 4020.46]  a working group yeah so um yeah there was a lot of uh ideas that came into the into the into the sphere
[4020.46 --> 4027.26]  right away um we set up a mailing list and so that would be a good place to start you can see that
[4027.26 --> 4031.76]  sort of i think at the top of the readme or at the top of the website uh you can subscribe to that
[4031.76 --> 4038.28]  it's just a typical uh google group mailing list and um so that's that's good for a sort of longer form
[4038.28 --> 4045.26]  discussion there's also a slack channel uh which we set up recently uh on the gophers.slack.com
[4045.26 --> 4050.92]  um slack group is that how it's called slack organization i have no idea what to call them
[4050.92 --> 4055.46]  these days i just they're just they're just out there there's so many slack rooms there's so many
[4055.46 --> 4062.16]  things so many um but yeah that's actually uh a well-managed and moderated uh slack group and there's
[4062.16 --> 4066.80]  a channel in there go kit uh you have to get an invite for that but invites are freely available and
[4066.80 --> 4071.48]  i provide a link for invites on the go kit website as well what's the oral for that right now real quick
[4071.48 --> 4081.16]  so i can write it down gophers.slack.com okay and if you want an invite that is bit.ly slash go
[4081.16 --> 4088.22]  dash slack dash signup and that'll get you one in an email right away as far as i'm aware awesome
[4088.22 --> 4094.70]  um yeah so those are the online forums i'm pretty active on the slack thing so if you have ideas
[4094.70 --> 4101.02]  that's probably the easiest way to reach me um and there's also several contributors that hang out there
[4101.48 --> 4108.00]  uh in terms of gopher con uh we're definitely going to do a go kit sort of hack day on the hack day i
[4108.00 --> 4113.98]  think that's going to be yeah wednesday is that right thursday tuesday is tuesday is the um is the
[4113.98 --> 4118.68]  training i feel i think they're calling them workshops to uh so that's tuesday wednesday thursday is the
[4118.68 --> 4124.04]  conference days and friday is hack day yeah so um i was at the hack day last year and that was actually
[4124.04 --> 4129.72]  the the probably the coolest part of the conference uh because it was an opportunity to meet people you
[4129.72 --> 4134.80]  kind of only knew by their twitter or github handles or whatever and uh the level of stuff
[4134.80 --> 4139.30]  that was produced there was actually really cool i'm not really much of a hackathon guy myself
[4139.30 --> 4145.58]  but uh the hack day was a much different experience than that it was a bit more heads down a bit more
[4145.58 --> 4151.58]  focused and uh really like a good a good sort of atmosphere and a really productive space so i'm
[4151.58 --> 4156.16]  really looking forward to that we're gonna have a table we had eric and brown on the show recently
[4156.16 --> 4162.76]  and they on that note they said that you know you mentioned hackathon that it's not hackathon at
[4162.76 --> 4168.78]  all it's more like for those 1500 people come to the conference you got all these speakers and people
[4168.78 --> 4173.76]  there that are building and contributing into the go ecosystem this is a chance to sit down with
[4173.76 --> 4180.36]  you know your like you had mentioned the avatar you only know or your hero so to speak and sit down
[4180.36 --> 4186.04]  and hack with them on your favorite library or ask them questions and and sort of fiddle with code
[4186.04 --> 4190.90]  together and that's more or less what the is that what you got out of as well yeah definitely i met
[4190.90 --> 4195.32]  some really cool people who there for the first time who i'm still talking to on a on a weekly basis
[4195.32 --> 4200.66]  today and i'm looking forward to meeting them again this year very cool so yeah chris hines
[4200.66 --> 4206.14]  mentioned in the mailing list room that uh or your mailing list that a go kit birds of a feather
[4206.14 --> 4211.48]  might happen so is that around the same hack day kind of thing yeah as far as i understand i don't
[4211.48 --> 4215.62]  know if there's a formal process if there is i'll look into it and i'll be sure to to set something
[4215.62 --> 4220.40]  up but i think it's pretty informal uh maybe day of i'll set something up and and i'll make myself
[4220.40 --> 4224.60]  visible so yeah if anybody's at all interested this show up show up in the right room and you'll
[4224.60 --> 4228.82]  be able to find me i'll make sure that's possible and while we're talking about gopher con if you're
[4228.82 --> 4233.18]  listening to this and you're not at gopher con but you know somebody who is and they listen to this show
[4233.18 --> 4238.36]  and they want to get on camera they want to say hello we'll be at the first after party the second
[4238.36 --> 4243.38]  after party the hack day pretty much everything you see there will be there cameras in hand the
[4243.38 --> 4249.00]  changelog uh has a new division called changelog films we're going to conferences and helping
[4249.00 --> 4253.76]  conferences like gopher con document what's going on in the community and it's a huge part of what
[4253.76 --> 4257.96]  we're moving towards so if you're listening to this and you're not there uh hopefully we'll see you
[4257.96 --> 4262.96]  next year but if uh if you got friends that are there hit them up let them know we're there if they
[4262.96 --> 4266.84]  don't already know and tell them come check us out because we want to uh we'll want to see
[4266.84 --> 4271.60]  everybody and we'll have you on camera as well at some point peter so you can't uh you can't hide
[4271.60 --> 4279.06]  you can't hide and i guess uh in true fashion at the ending of this show let's let's wrap with two uh
[4279.06 --> 4285.02]  two awesome questions the first question is if we haven't already said it obviously we've talked quite
[4285.02 --> 4289.72]  a bit about several things instead of go and go kit but for those out there that are thinking man this
[4289.72 --> 4295.56]  is super cool how can i get involved what is the where are the places you need help to make go kit
[4295.56 --> 4302.36]  a real thing and keep moving forward and get better adoption yeah so this is a great question um if
[4302.36 --> 4307.10]  you're an accomplished go developer and everything i've been saying is really like struck a chord with
[4307.10 --> 4313.56]  you then uh dive right into the issues list i've making i've been making a an effort and i'll continue
[4313.56 --> 4321.16]  to do uh to make an effort to um sort of keep my roadmap up to date in there and um have a list
[4321.16 --> 4325.68]  of things that need to be implemented that i'll try to make as straightforward as possible if you want
[4325.68 --> 4331.08]  to claim ownership of them please feel free uh a lot of them is is pretty straightforward a lot of them
[4331.08 --> 4335.08]  are going to be a little bit subtle but you know it's nothing we we can't like talk through
[4335.08 --> 4339.32]  so if you're a gopher already and you want to contribute that would be amazing
[4339.32 --> 4344.48]  um but that's not even really necessary the the thing that i think would help quite a lot and
[4344.48 --> 4351.16]  especially at this early stage is if you're somebody in an organization and you want to use go but you're
[4351.16 --> 4356.96]  feeling some friction or you're you're you're missing something in the ecosystem something that go kit might
[4356.96 --> 4363.88]  be able to provide or even help provide um file an issue with that let me know somehow and let me sort
[4363.88 --> 4370.84]  of fold it into my like idea of what this thing is that i'm building um use cases like that user
[4370.84 --> 4376.00]  stories uh sorry again for the agile terminology i've been working in startups for too long i guess
[4376.00 --> 4381.96]  um but information like that is super super helpful to me then also don't forget the
[4381.96 --> 4387.52]  gophers.slack.com too so you said you're there all the time and so i guess issues would be a good
[4387.52 --> 4393.64]  place to go and kind of uh find things off yourself but at the same time get an invite
[4393.64 --> 4401.02]  yeah enjoying that slack room precisely awesome well cool and i guess our our final question which
[4401.02 --> 4405.44]  to some i don't know peter you might like it as well but some absolutely hate this question some
[4405.44 --> 4412.30]  love it we'll see what line you fall upon but uh we're curious who your programming hero or heroes
[4412.30 --> 4420.98]  are yeah that's interesting it's sort of a like with me it's it's it's like a favorites like i try not to
[4420.98 --> 4428.00]  have favorites i try not to do things like that but i will say that there's been several people in my
[4428.00 --> 4433.54]  like career that have been very heroic to me and it's not specific people or specific personalities
[4433.54 --> 4440.96]  rather it's been people who have been mentors to me uh not only when i was in school or fresh out of
[4440.96 --> 4446.98]  school although those people have played like a really important role in in in growing me and and
[4446.98 --> 4453.56]  making me a better person and a better programmer and all these fun things but even like on a day-to-day
[4453.56 --> 4460.46]  basis today people who take time out of their day to contribute to me and to like lend a little wisdom
[4460.46 --> 4467.86]  to me if if you can get into a mentor mentee is that right apprentice master sort of thing this kind
[4467.86 --> 4472.98]  of relationship with somebody in a professional context i think this is really the way that information
[4472.98 --> 4479.00]  flows this is really the way people get better and to everyone who's ever been a mentor to me that's
[4479.00 --> 4486.02]  people like uh gary sumar back at bloomberg uh sean treadway at soundcloud uh more people than i could
[4486.02 --> 4491.16]  possibly name actually but uh these are the people that are like heroes to me and the people that have
[4491.16 --> 4499.22]  uh really allowed me to level up and and get to where i am today speaking of mentoring and menteeing if
[4499.22 --> 4503.28]  that's i'm not sure that's the thing or not maybe not i'm gonna follow your lead on that one are you
[4503.28 --> 4508.42]  mentoring anybody uh not sort of officially right now and that's a great sort of call out of me i
[4508.42 --> 4513.26]  should really find a way to do that um yeah i'm gonna i'm gonna look into the community here because
[4513.26 --> 4518.24]  berlin is a great place for this lots of junior devs lots of people looking to get into the industry so
[4518.24 --> 4524.18]  yeah it's definitely something i could look into yeah uh i'm trying to remember the the ad spot i did for
[4524.18 --> 4530.14]  digital ocean but uh in that ad spot i talked about the huge community for um startups there
[4530.14 --> 4535.88]  because they just opened up uh fra1 yeah frankfurt yeah so yeah and it's on that
[4535.88 --> 4540.20]  trying to remember the words for but some some exchange some internet exchange that's huge that
[4540.20 --> 4544.60]  feeds basically all of europe and it makes it super fast that's where the digital ocean servers are at
[4544.60 --> 4549.78]  yeah um not to plug them much more but you made me think about how that spot talked about the
[4549.78 --> 4554.16]  thriving startup community there and ecosystem there so yeah definitely and when they came
[4554.16 --> 4558.52]  and did their press tour i was actually like helping them coordinate that there's a lot of fun stuff
[4558.52 --> 4564.18]  happening in germany and berlin especially so yeah definitely and you said there's some folks at
[4564.18 --> 4568.86]  digital ocean helping with gokit um yeah there's a couple of infrastructure engineers who have
[4568.86 --> 4576.62]  contributed to the log package a bit to the uh to the server side stuff um with luck uh they've already
[4576.62 --> 4582.52]  contributed a sort of a staging testing uh server for me to help me test the zipkin stuff it turns out if
[4582.52 --> 4589.54]  you want to start a zipkin server you need a pretty beefy machine uh zipkin is written in on the jvm and
[4589.54 --> 4596.12]  it uses a lot of memory more than my little dinky uh vps's can handle so thanks to them for that
[4596.12 --> 4601.60]  um with luck that'll continue uh yeah so digital ocean has been a great partner for gokit so far
[4601.60 --> 4607.34]  i guess the one question that eluded my mind to even think about but mentioning digital ocean there and
[4607.34 --> 4614.76]  asking about their uh work into the into the software itself is who is there anybody out there
[4614.76 --> 4622.34]  who's adopted gokit so far and using gokit in the wild or even in like a test phase yeah um there's a
[4622.34 --> 4627.84]  couple of organizations that i can't uh really name by name for a variety of reasons that are using pieces
[4627.84 --> 4634.58]  of gokit um the the log package is attracting a lot of attention metrics is attracting a lot of attention
[4634.58 --> 4639.12]  because these are sort of the most feature complete kind of self-contained uh packages at the moment
[4639.12 --> 4646.68]  um but yeah a couple of others are starting to play around with um structuring microservices using
[4646.68 --> 4651.16]  gokit components and then hopefully the goal is their feedback is going to drive further
[4651.16 --> 4657.94]  gokit development so that's the idea fantastic well peter it's been such an honor to have you on the show
[4657.94 --> 4663.62]  man i know we've been what playing twitter dm tag for a little bit and then email a little bit and then
[4663.62 --> 4668.16]  you were traveling and then it was a good time for us so we finally got you on and we wanted to get
[4668.16 --> 4673.76]  you on the show after we had that conversation with andrew yeah uh because that sort of set the
[4673.76 --> 4681.38]  the new tone for go on the show go into large yeah exactly we sort of stepped back into go on a year-to-year
[4681.38 --> 4688.16]  basis and you know we started with rob pike by himself way back when go very first started and then
[4688.16 --> 4693.54]  about two years back had andrew and rob back on and then we had andrew back on and i knew that
[4693.54 --> 4699.66]  it was time to to to talk to you because he was like hey when i'm done on this show you got to get
[4699.66 --> 4703.62]  peter on the line because he's got something very cool happening that everyone in the go community has
[4703.62 --> 4709.26]  to know about nice so so there you go so you got a good old uh slap on the back and blessing from
[4709.26 --> 4713.78]  andrew nice that one as well good to hear and i and i hope to hear even more go people uh on the
[4713.78 --> 4717.70]  changelog in the future i'm definitely going to tune in if that happens we definitely want to talk
[4717.70 --> 4722.38]  about prometheus at some point so when uh we get off here we'll have to get some get something
[4722.38 --> 4727.80]  happening oh yeah definitely in the near future but peter it's it's been awesome any links you want
[4727.80 --> 4733.36]  to mention as we close here to follow you on then you got your github.com slash peter and your last
[4733.36 --> 4739.74]  name anywhere else it's best to kind of catch up with you at uh yeah i mean uh i'm probably easiest to
[4739.74 --> 4747.46]  reach on twitter that's just uh my full name peter bergon no spaces um github uh sorry gokit.io
[4747.46 --> 4754.04]  takes you to the github repo and um yeah i guess that's that's about it i'm pretty pretty simple guy
[4754.04 --> 4761.36]  and for the listener's sake we'll have all those in the show notes so this is episode 163 of the
[4761.36 --> 4769.70]  changelog go to changelog.com slash 163 and you'll find all the show notes and all the details about
[4769.70 --> 4772.34]  everything we talked here so don't feel like you got to wreck your car if you're listening in the
[4772.34 --> 4777.98]  car or jumping out of that airplane to get to i don't know just making funny jokes but don't go
[4777.98 --> 4782.76]  crazy just go to the show notes everything's there for you we make it easy but uh peter thanks so much
[4782.76 --> 4787.40]  for joining us today on the show and uh let's let's say goodbye all right yeah no thank you very much
[4787.40 --> 4789.94]  the pleasure's all mine and i had a lot of fun
[4799.70 --> 4829.36]  i had a good time
[4829.70 --> 4859.68]  Thank you.
