[0.00 --> 18.12]  this week on the change law we're going back to the hallway track of all things open 2023
[18.12 --> 23.96]  in raleigh north carolina today's episode features matthew sanabria former engineer
[23.96 --> 31.04]  at hashi corp who worked on terraform enterprise nithya ruff chief open source officer and head
[31.04 --> 36.50]  of the open source program office at amazon and last up today is jordan hardband open source
[36.50 --> 42.84]  maintainer at large with dependencies in most javascript apps out there there has been many
[42.84 --> 49.16]  changes this year in open source and each of these perspectives lends insight into the challenging
[49.16 --> 55.58]  and changing waters happening right now in open source and we have to give a tremendous thank
[55.58 --> 61.70]  you to todd lewis the organizer behind all things open it is one of our favorite conferences and
[61.70 --> 68.28]  todd lewis and team does a tremendous job leading that conference of course a big thank you to our
[68.28 --> 74.90]  friends and our partners at fastly and fly this podcast got you fast because fastly they are super
[74.90 --> 81.10]  fast globally check them out at fastly.com and our good friends at fly will help you put your app
[81.10 --> 88.16]  and your database in 30 plus regions on six continents with no ops check them out at fly.io
[88.16 --> 104.78]  what's up friends i'm here with james cowling co-founder
[104.78 --> 110.56]  and cto at convex they're one of our new sponsors and they're building a full stack platform for the
[110.56 --> 118.20]  typescript era so james in your main navigation you link to a page called convex versus firebase how
[118.20 --> 124.22]  similar is convex to firebase and if someone is quickly trying to grok what convex is is that a
[124.22 --> 129.12]  good comparison i think it's a good starting point for sure i mean firebase has been very impactful and
[129.12 --> 135.08]  the people we speak to who use firebase often love it and they often lament the time they have to move
[135.08 --> 140.60]  off of firebase because it's kind of failed to meet their needs as a growing company so firebase falls
[140.60 --> 147.82]  short in a few ways one is in terms of like a fully relational document model one is in terms of having
[147.82 --> 154.20]  strong type system one is in terms of having this full end-to-end consistency story where you write
[154.20 --> 159.94]  functions that run on an api server on the data that you can subscribe to and so one thing i think
[159.94 --> 165.90]  we see in the the firebase style development model is that you have web applications talking directly to
[165.90 --> 171.42]  a database in a cloud fire store with convex what is different is you have your code talking to actual
[171.42 --> 176.96]  fully fledged typescript functions running on your data that you can subscribe to but i think that the
[176.96 --> 182.54]  the firebase's comparison is fairly apt and if someone is a firebase user i think you will love
[182.54 --> 186.90]  convex and it's certainly designed to fill that niche in the market it's people who want to build
[186.90 --> 190.54]  applications without having to mess with infrastructure in what way has infrastructure
[190.54 --> 196.42]  failed specifically application developers i think if one was to compare what it looked like to build an
[196.42 --> 203.08]  application 10 plus years ago to today it's gotten more complex not less complex there's a bewildering
[203.08 --> 209.34]  amount of frameworks i think google for all their amazing work they do has had a bad influence on how
[209.34 --> 213.32]  people build systems because oftentimes when someone's got a web app these days they're told to
[213.32 --> 218.18]  like learn kubernetes or something ridiculous like that you know these infrastructure platforms
[218.18 --> 224.40]  really resemble the shape of the underlying implementation not the shape of the problem
[224.40 --> 229.06]  that the application developers facing and so even when before we started comics we're talking to
[229.06 --> 234.78]  customers people like well i just want someone to like manage my kafka cluster and i say well why do you
[234.78 --> 240.00]  even have kafka and like well i don't really know i think the database falls over if i don't put a queue
[240.00 --> 245.76]  in front of it or like i need to like buffer some data somewhere and what became clear is is that the
[245.76 --> 250.28]  the tools just weren't serving the needs of the application developers and i think application
[250.28 --> 254.74]  developers and framework front-end framework engineers understand the problem space because
[254.74 --> 258.58]  they spend all day doing it they sometimes don't have the power to to fix the problem because they
[258.58 --> 264.00]  don't build the database themselves and i think oftentimes infra folks don't have enough empathy for the
[264.00 --> 267.12]  application developer that at the end of the day there's all that matters is the application
[267.12 --> 272.74]  okay if you're looking for a better type of back-end convex is the full stack typescript
[272.74 --> 277.44]  development platform you've been looking for replace your database server functions and glue code
[277.44 --> 285.24]  get started at convex.dev that's c-o-n-v-e-x.dev again convex.dev
[293.24 --> 293.94]  so
[294.00 --> 322.38]  let's talk about the last two weeks of your life
[322.38 --> 328.88]  yeah what's what's happened what's going on what do you how you feel i feel good i feel good so
[328.88 --> 334.78]  last two weeks i've left my job where did you work i worked at hashi corp i've heard of them
[334.78 --> 339.58]  yeah i was there for about five years so it's a long time it was a while four years ten months or
[339.58 --> 344.16]  whatever it was and what'd you do there uh i started in support engineering went to software
[344.16 --> 348.86]  engineering for terraform enterprise got promoted there went that route but when i left i was pretty
[348.86 --> 355.48]  much the terraform enterprise subject matter expert um working on terraform enterprise so yeah software
[355.48 --> 362.74]  engineering bunch of like docker go kubernetes things yeah pretty fun um it's funny what he said
[362.74 --> 367.20]  terraform there i'm not even kidding with you i legit thought he said tofu
[367.20 --> 374.64]  you're kidding me aren't you no i really am not kidding you they don't have any tofu there i thought
[374.64 --> 382.08]  he said i was on the tofu enterprise team i ate some tofu but i never used it yeah it was that was a fun
[382.08 --> 387.36]  that announcement the license change announcement was a very fun time at hashi corp i will say
[387.36 --> 392.84]  tell us about it from the inside i mean i wish i could come up here and say like the inside was
[392.84 --> 398.76]  different in the sense of like we were made aware and you know we we had all this notice and da da da
[398.76 --> 404.68]  it wasn't we found out the same time you all found out so from the inside yeah the same yeah the same
[404.68 --> 409.98]  day that you all found out the announcement that's how that's how we found out which doesn't really
[409.98 --> 414.32]  inspire a lot of like you know yeah it didn't make me happy i will say what we're not asking you to
[414.32 --> 419.70]  do just to be clear is to just talk smack yeah i think what these podcasts serve as in my opinion is
[419.70 --> 425.26]  like the facts of what really happened yeah the sentiment right it's less like oh they're bad and
[425.26 --> 430.06]  open source good it's more like what really happened so that one we just know as developers
[430.06 --> 435.34]  because there's an assumption from the outside oh people knew in advance and this was orchestrated
[435.34 --> 440.14]  well maybe it was at some level so i just talked to somebody else in dev advocacy today
[440.14 --> 446.24]  and she said they knew three days in advance yeah so dev advocacy knew maybe a couple days
[446.24 --> 451.18]  yeah but engineers senior engineers on the tofu i mean the terraform team
[451.18 --> 456.74]  well i didn't know like hash group's a an interesting company right because they're like a company of
[456.74 --> 462.28]  companies if you think about it right they have multiple projects right nomad vol terraform console
[462.28 --> 468.44]  all their projects they have a bunch of projects and each of those teams kind of operates by like you
[468.44 --> 472.56]  know in autonomy by themselves they contribute to each other's code base they have shared libraries
[472.56 --> 477.32]  and stuff but for the most part terraform's terraform vault's vault nomad's nomad so from the terraform
[477.32 --> 483.20]  side we were pretty shocked and mind you i was on terraform enterprise right so our licensure all that
[483.20 --> 488.14]  has never changed terraform open source changed so i wasn't on the terraform open source team maybe
[488.14 --> 492.36]  they knew in advance but for me on the terraform enterprise team we did not know in advance i guess
[492.36 --> 497.36]  it kind of makes sense to some degree that enterprise doesn't need to know right because you don't
[497.36 --> 502.58]  really not so much care but it's your underpinnings your customers that are buying right from the
[502.58 --> 505.98]  open source and the customers that are buying the enterprise product are paying for it right they're
[505.98 --> 511.24]  going through that that sales process anyway right i think though when you make a major shift like that
[511.24 --> 517.10]  the story arc quickly for hashicorp mitchell hashimoto created it years ago when he created vagrant
[517.10 --> 521.58]  actually a couple years after vagrant it was successful enough to create a company that created
[521.58 --> 525.88]  products yeah that lived in open core but also had paid models around it it was very successful
[525.88 --> 530.66]  so successful that they ipo'd you're part of that company i was very definitely happy for that
[530.66 --> 533.96]  right which is a great thing yeah and i think when you're at that level you probably should
[533.96 --> 538.20]  communicate to the people around you in your company to say is this a right is this a wise move
[538.20 --> 545.22]  like yeah we are so ingrained given that success in the dev culture and the dev community terraform
[545.22 --> 550.42]  is such a used software that they the community was like that's not cool we're gonna fork it
[550.42 --> 555.56]  yeah and make our own thing it's that it was that impactful when you make software tools and products
[555.56 --> 560.80]  that are that impactful you probably should ask for is this the right way to handle this agreed can we
[560.80 --> 567.16]  do is there a better way i mean looking at the open source repos there's definitely people that are
[567.16 --> 572.56]  happy to use hashicor products they love the products they are very active on the issues pull requests
[572.56 --> 577.80]  and all that and yeah there there there was a time where where terraform was short-staffed and there
[577.80 --> 583.04]  was a public read me update or an issue where they told the community hey we're a little short-staffed
[583.04 --> 590.04]  in the next couple months let's uh you know we're gonna slow down on reviewing yeah open prs but that
[590.04 --> 595.10]  was communicated and yeah the the community looks at that and says hey you know like hey what's going
[595.10 --> 599.22]  on with terraform but it was communicated to the community and they're aware right they're kept in the
[599.22 --> 604.22]  loop that's something that i would have probably expected to happen with the projects with the
[604.22 --> 608.30]  license change but that didn't happen so i was kind of a shock about that right like you would expect
[608.30 --> 612.82]  that to have been communicated to the community more in advance i guess what i'm trying to say
[612.82 --> 619.54]  you know so it's kind of a shock when it wasn't did you leave because of that or that was one of the
[619.54 --> 625.82]  the motivating factors of why why i left right it was just the shift in the engineering culture
[625.82 --> 632.26]  like move away towards that more product culture kind of did it for me right i mean when i joined
[632.26 --> 637.90]  hashi corp there was about 350 people when i left there was about 2 000 and obviously when i went to
[637.90 --> 643.60]  the ipo with them and whatnot um so that was one of the reasons too yeah you know it's like you're no
[643.60 --> 648.66]  longer working on open source you're working on source available if you think about it right yeah
[648.66 --> 652.74]  that's interesting though because you feel that way even though you're on the enterprise team yeah
[652.74 --> 658.78]  so just because you're in in a silo that isn't really benefited or involved in the creation of
[658.78 --> 662.90]  the open source you still care exactly right if you think about the enterprise the whole point of
[662.90 --> 667.52]  the enterprise product is to be able to use the open source product in a way that you control in
[667.52 --> 671.90]  your own data center in your own cloud or whatever right use it in a way that you get the r back you get
[671.90 --> 678.24]  the cicd kind of pipeline ish aspect to it you want to be able to use that but at the end of the day it
[678.24 --> 683.52]  it relies on the open source product to even be functional right so when you take up when you
[683.52 --> 689.40]  take that out i don't know do you destroy trust maybe i don't know right it's hard to say yeah
[689.40 --> 702.00]  how big is your team we were about 10 engineers in like june then hashcorp did a layoff in june
[702.00 --> 707.32]  then we dropped to eight engineers and then a few fewer engineers went on maternity leave and then i
[707.32 --> 713.62]  left so when i left we were five so seven if you count the staff but yeah i don't count the staff
[713.62 --> 721.84]  engineers like in that so were your colleagues equally as shocked were they also upset what was
[721.84 --> 727.68]  the general vibe on your team uh some of them were pretty frustrated with it some of them were like i
[727.68 --> 732.90]  don't care we're enterprise doesn't really matter yeah that was kind of the vibe me i was more so
[732.90 --> 739.26]  like affected by it because i was looking to like transfer teams a year before that to an open source
[739.26 --> 744.24]  team to specifically work on the open source product and not the enterprise product and that team also
[744.24 --> 749.60]  had their license changed so for me i was like that that sucks but the team sentiment was pretty good
[749.60 --> 754.32]  right like being close to the money is nice right tower from enterprise made a pretty good revenue chunk
[754.32 --> 759.12]  for for hashcorp and most people were like eh we're okay we're making we're still making money we're
[759.12 --> 764.04]  fine don't care with license that's fair this might be tmi but can you talk at all about your slack
[764.04 --> 770.20]  message yeah yeah overview of it yeah i can give an overview of it that's that was a good one so
[770.20 --> 777.34]  like every company hashcorp has channels in their slack where you can monitor where they like talk about
[777.34 --> 781.20]  the competition or they have a twitter feed channel all that stuff right where you talk about
[781.20 --> 786.62]  you know what's going on in the industry around us and there is one for competition and open tofu
[786.62 --> 791.30]  came up a lot in that channel obviously people were like oh they don't know what they're doing
[791.30 --> 795.46]  some people were like oh you know they're gonna they're gonna eat our lunch and the sentiment was
[795.46 --> 799.82]  spread out they had people that were like they're gonna take our business and other people were like
[799.82 --> 804.94]  nah they're they're nothing and it was interesting though but there was one message there was like
[804.94 --> 810.18]  when open tofu finally announced like that they went to what the linux foundation and they're trying to go
[810.18 --> 814.08]  to the cntf but then they announced their name change because they were open tf right and then
[814.08 --> 818.24]  they changed open tofu when they announced that someone posted that mess like you know that
[818.24 --> 825.48]  announcement yeah in the slack channel and i replied and verbatim what i said was like you know i wish
[825.48 --> 830.60]  i i wish them well overall right like i'm rooting for them overall but that name sucks that's what i said
[830.60 --> 835.54]  right verbatim that's what i said i don't like the name open tofu i've never been a fan of it that's fine
[835.54 --> 843.78]  but that's what i said to in the chat um and yeah like i i got pretty good uh backlash for that
[843.78 --> 851.06]  comment oh really yeah i was i was shocked and why this was like two two to three days before my last
[851.06 --> 856.88]  day at ashtacore so i had already put my like notice in and all that stuff but i was just engaging
[856.88 --> 862.58]  conversation i was like hey you know like i wish them well but i don't like the name whatever and i had
[862.58 --> 869.46]  backlash from that comment where i guess two days passed and someone went to leadership and said hey
[869.46 --> 876.24]  matthew's comment in slack they're not rooting for hashi corp they're rooting for open open tofu they
[876.24 --> 882.08]  want us to fail da da da and i was like what that's not even what i said so that made it back to me
[882.08 --> 887.96]  through my manager and i was legitimately just shocked i was like wait a minute what what are you
[887.96 --> 892.92]  even saying here right yeah so that that was kind of like a an eye-opener to me i was like
[892.92 --> 899.06]  that was a little weird in my respect but what are you gonna do right like things happen yeah so
[899.06 --> 904.84]  are you at cockroach labs now i start in like a couple weeks yeah you're actually representing them
[904.84 --> 910.64]  i do i have them on the badge despite not truly what if they rescind their offer they could they
[910.64 --> 916.52]  could they sure can it's business it's business what makes you excited about cockroach just uh the
[916.52 --> 920.96]  distributed systems problems that i'll be able to like get into and solve right like so comparing
[920.96 --> 925.70]  it and contrasting it to where i was and now hash core great company cool cool people right some of
[925.70 --> 932.04]  the nicest and smartest ic's i've ever worked with there and good products but they build the tools
[932.04 --> 938.32]  they don't necessarily like run the tools at the scale that the customers do right yeah uh whereas
[938.32 --> 942.24]  cockroach they create the database they run the database as a managed service so i'll get to
[942.24 --> 947.48]  in like interact with those distributed systems problems that's what draws me there um so yeah
[947.48 --> 951.96]  also some licensing issues there too wasn't there some licensing issues at cockroach yeah they so
[951.96 --> 955.64]  which i think it's fair to change and it's fair to protect but that's the thing right like
[955.64 --> 960.92]  people with my comment in the slack that we were talking about people were saying like oh you know
[960.92 --> 965.62]  the license is good you're just like you know you want hash core to fail it's like no i don't the
[965.62 --> 971.00]  license i'm not mad about the license what i'm mad about is the lack of transparency right right right and
[971.00 --> 976.38]  that's kind of what what got me and then the company i'm going to cockroach they have the
[976.38 --> 982.00]  same license right they're under the bsl license as well yeah yeah i thought it was sspl but i'm
[982.00 --> 986.32]  probably wrong i think it's bsl i gotta check too you're probably right and i'm probably wrong but
[986.32 --> 991.10]  there's a lot of licensing we cover over the years so much my licensing wires might get crossed
[991.10 --> 994.96]  and in the time that i left hash core and before i started cockroach i've been like
[994.96 --> 1000.28]  unplugged in a break mode i just gave myself a little time to i think they've always been just
[1000.28 --> 1003.82]  clear too cockroach has always been clear about where they're trying to what they're trying to do
[1003.82 --> 1010.26]  but it makes sense cockroach db is a service that you're going to run long-running service that's
[1010.26 --> 1016.12]  going to provide value to whatever applications you run if you notice the licensing conversations
[1016.12 --> 1021.88]  around hashicorp have primarily been focused on terraform but all of hashicorp's license changed
[1021.88 --> 1028.52]  yeah right vagrant nomad vault console right all of them all of them change so it's like when you think
[1028.52 --> 1032.54]  about when you step back and you say why are people upset about the terraform license change
[1032.54 --> 1038.72]  versus the other products like vault or whatever it kind of breaks down where vault and them are
[1038.72 --> 1045.02]  services and terraform's a tool right so then when you apply that to like you know cockroach or even
[1045.02 --> 1050.46]  elastic right there there's services that run yeah terraform's a tool i don't know if it made sense to
[1050.46 --> 1054.92]  change the license of a tool it does make sense to change the license of a service yeah because you
[1054.92 --> 1060.30]  don't want like other providers providing that service on your behalf and whatnot yeah and they
[1060.30 --> 1064.82]  fundamentally use it a different way right right like you're gonna plug into a service and have it
[1064.82 --> 1070.90]  operated or operated yourself yeah a tool you're gonna build things with on top of yeah right modify
[1070.90 --> 1077.54]  more etc and so they are approached very differently and so that's why why the reaction is quite a bit
[1077.54 --> 1081.96]  different agreed yeah it was it was interesting thing for sure i mean again we don't know what's
[1081.96 --> 1087.62]  gonna happen i just felt like i don't know i don't know if the communication was fully like
[1087.62 --> 1095.00]  thought through in that sense you probably saw the faq pages they kept adding faq like messages there
[1095.00 --> 1100.16]  and it's i don't know it's it's it's a weird one but what i thought was interesting is so i downloaded
[1100.16 --> 1106.36]  open tofu played with it used it despite the name despite the name yeah i just i just renamed the binary
[1106.36 --> 1111.54]  yeah it's fine it's okay alias the fact to what we had a conversation in our slack about the name
[1111.54 --> 1115.04]  as well i bet everybody in their slack had a conversation about the name of course i thought
[1115.04 --> 1121.10]  open tf was a totally fine name i thought so too but they wanted a cute mascot apparently
[1121.10 --> 1126.46]  and so they went with the tofu i think they probably wanted to get further away from the word terraform or
[1126.46 --> 1131.64]  tf in particular i mean it's obviously i think it's enforceable through some sort of i mean yeah
[1131.64 --> 1138.44]  it's probably had to yeah it's an obvious derivative correct of its predecessor right
[1138.44 --> 1144.42]  correct so i mean it's not like you could argue that it's just shortened to open tf yeah i also
[1144.42 --> 1149.98]  not a huge fan of the name but go ahead you were saying you ran it yeah i ran it used it like some of
[1149.98 --> 1154.56]  their first of all i think they made a really smart decision if i were in their position i'd do the same
[1154.56 --> 1159.38]  thing right if i was in their position of the companies that got together and and started that that
[1159.38 --> 1164.36]  foundation all that i would do the exact same thing they did right why wouldn't you right like
[1164.36 --> 1168.36]  you have an opportunity there you have people that are willing to throw engineering time and then there
[1168.36 --> 1172.64]  were a few like quick win features that you could have added like the encrypted save file and whatnot
[1172.64 --> 1178.58]  so it made sense for them to to do what they did so what do you think of their claim so one of the
[1178.58 --> 1185.20]  things that josh padnick said on the show was about the amount of effort dedicated to terraform
[1185.20 --> 1191.92]  versus open tofu and he stated like based on github public you know activity on the repos
[1191.92 --> 1197.28]  and who's actually working on a handful of people and he's saying we had 15 i think they said 15
[1197.28 --> 1202.58]  engineers at the time i don't know dedicated full-time resources do you think that's a accurate
[1202.58 --> 1205.74]  from your perspective and then b do you think that's going to really you know move the needle
[1205.74 --> 1212.38]  uh i think that's relatively accurate if you if you keep to if you just talk about terraform
[1212.38 --> 1217.12]  open source as itself right because terraform is kind of a beast of a of a tool right you have the
[1217.12 --> 1220.82]  open source binary that's responsible for like the graphing and whatnot and you have the providers
[1220.82 --> 1226.06]  that actually communicate with the apis if you look at the open source part of the product then yeah
[1226.06 --> 1229.26]  there's probably just a handful of engineers working there but then there's like various
[1229.26 --> 1236.40]  little ecosystem teams cli experience teams provider teams and then the the team i quotes i air
[1236.40 --> 1241.76]  quotes the team of terraform expands beyond that right but realistically speaking the major
[1241.76 --> 1247.52]  providers you're already partnering with like aws google azure all that for those providers so
[1247.52 --> 1251.36]  you're kind of already sharing that bandwidth but if you just focus on the core i think they're
[1251.36 --> 1257.02]  correct there's only about a handful of engineers that work on the core core so can open tofu pull
[1257.02 --> 1263.26]  it off with their 15 or so engineers i don't see why not yeah right i think my worry with them is
[1263.26 --> 1269.16]  a lot of companies are coming together to work on open tofu and maybe for now the companies have an
[1269.16 --> 1274.24]  alignment on where they're going but will that always remain hard to say right what happens when
[1274.24 --> 1278.56]  conflict arises and one company wants to go one way and one wants to go the other way what do they do
[1278.56 --> 1283.00]  yeah you know one thing i was trying to drill down with him which i don't think i ever quite got the
[1283.00 --> 1288.54]  question asked in a way that he understood it was it seems like they have a lot of logos
[1288.54 --> 1294.64]  but not a lot of like guaranteed support so it's like how much of this is support and name only
[1294.64 --> 1300.70]  like yeah we're behind you put our name on the website but are we actually gonna like because
[1300.70 --> 1304.96]  it takes a lot not just up front you get the energy and the excitement and everybody slapped
[1304.96 --> 1310.38]  their logo on in the beginning but like over the course of years to support a project like that's a
[1310.38 --> 1315.52]  that's an ongoing initiative that requires dedication and how many of these companies are
[1315.52 --> 1322.58]  actually dedicated obviously time will tell but he didn't seem too worried about it so yeah i listened to
[1322.58 --> 1327.02]  that episode i heard the question i was waiting for a concrete answer as well we didn't get like
[1327.02 --> 1332.18]  a super concrete answer which is fine yeah you know they're still early but i agree i i time will tell
[1332.18 --> 1337.10]  on that i hope they can maintain it because it's it's a beast of a of a tool to maintain the people
[1337.10 --> 1341.32]  that work on terraformer have been there for quite a few number of years built up the context around it
[1341.32 --> 1345.96]  right it's it's a pretty decent large code base and it's a complex problem domain right like the whole
[1345.96 --> 1350.38]  idea of terraformer is just you're graphing your infrastructure and you're making api requests so if you
[1350.38 --> 1354.88]  don't understand that whole idea of graphing and whatnot and dependency resolution it's gonna be
[1354.88 --> 1358.90]  a little bit of a difficult thing for you to contribute to the question is will you be a
[1358.90 --> 1364.50]  contributor uh i think so i've already contributed to some of the terraform providers so i probably
[1364.50 --> 1368.68]  keep contributing in that respect i haven't contributed i have i think i have contributed to
[1368.68 --> 1373.58]  core maybe like small little contributions but nothing major to the core code base does cockroach
[1373.58 --> 1377.56]  choose terraform yeah they have a terraform provider but they don't use it for their production
[1377.56 --> 1383.32]  infrastructure gotcha yeah they're on palumi i believe from what last i heard we'll see i guess
[1383.32 --> 1389.24]  right yeah yeah we'll see there's at the end of the day infrastructure is if you think about it it's
[1389.24 --> 1392.80]  a solved problem we know what we need to do with it we need to spin it up we need to manage it
[1392.80 --> 1397.80]  the tool that you use use the best one for your team right the one that's going to provide you the
[1397.80 --> 1402.96]  best benefit that's the one you should be using curious if you have takes on some of the
[1402.96 --> 1409.60]  more recent releases in the infra world system initiative the stuff that the dagger folks are
[1409.60 --> 1415.42]  doing so what's interesting to you yeah the dagger stuff's interesting i heard about it in the podcast
[1415.42 --> 1421.68]  saw like looked at the website whatnot haven't used it yet have not used it system initiative however
[1421.68 --> 1428.64]  i have used i've contributed to and i interviewed them okay yeah so excited about that yeah i'm very
[1428.64 --> 1432.74]  excited about the system initiative stuff yeah adam jacob great person i know i think you had him on
[1432.74 --> 1438.44]  the show right yeah we call him a friend there you go perfect yeah perfect yeah great great people
[1438.44 --> 1443.84]  there um a couple former hash core people that are there talked to a few of them they have a wonderful
[1443.84 --> 1448.30]  discord that if you are really interested in system initiative go join they're wonderful people
[1448.30 --> 1452.32]  they do everything out in the open as much as possible and that's how i got involved so i interviewed
[1452.32 --> 1456.38]  with them uh didn't get that that role they went with somebody else because you know startups
[1456.38 --> 1460.18]  there were only like 14 people yeah they're small right they're small so they got to be very very
[1460.18 --> 1465.44]  picky which is great but then i liked the product did the beta like went through the beta testing or
[1465.44 --> 1470.02]  whatnot gave them feedback and all that and then i contributed their podman driver to run system
[1470.02 --> 1476.80]  initiative on podman is it the future is it the future is a good question i don't i don't know i i like
[1476.80 --> 1482.14]  the ergonomics of it a lot honestly it's very fun because if some like when you're thinking about
[1482.14 --> 1487.16]  infrastructure the one thing that really like left a bad taste in my mouth with terraform is when
[1487.16 --> 1491.16]  you're trying to find out what risk like what other resources you can use with this resource it's
[1491.16 --> 1494.86]  very difficult you need to know the name of the resource that you want to use right like finding
[1494.86 --> 1499.12]  the dependencies and the connections between them is tough you have to look in their docs and the
[1499.12 --> 1505.40]  docs are there's a lot but with system initiative you drag an asset onto the pane and you know the
[1505.40 --> 1508.42]  dependencies that you can use with that resource you know what can plug into it you know what it can
[1508.42 --> 1513.52]  output to and that's great like i thought that was cool so from the visibility of how you can like
[1513.52 --> 1519.26]  build your graph of infrastructure i think system initiative is great in that regard uh outside of
[1519.26 --> 1524.12]  that like there's obviously they're still in very very early release phase so they have like a few ui
[1524.12 --> 1530.32]  things to smoothen out but i don't know is it the future again the future will tell what the future
[1530.32 --> 1535.52]  is right do you think it could be just a ui that others like could it be a ui on top of terraform
[1535.52 --> 1541.86]  for example like could it become the the interface that we begin to use to orchestrate services and
[1541.86 --> 1547.50]  infrastructure and stuff like that rather than just being its own silo it's possible they could
[1547.50 --> 1552.70]  open that up because they have like the capability technically under the hood all the assets are just
[1552.70 --> 1557.16]  typescript under the hood right so it's like a function or whatever you run as long as you write
[1557.16 --> 1561.20]  it in that interface way you're good i think so would they want to do that i'm not sure
[1561.20 --> 1567.72]  right that seems to be the most innovative thing really yeah and what it offers right is the
[1567.72 --> 1574.48]  visual interface to connect the nodes and see the dependencies rather than scouring through yaml or
[1574.48 --> 1579.62]  whatever else you might have for configuration exactly that's challenging right it's it is and
[1579.62 --> 1584.70]  the example they they run you through in the beta is basically spin up ec2 instance security group
[1584.70 --> 1590.42]  sh key right you just put all together and you see a graph in your aws region and whatnot and it's all
[1590.42 --> 1594.96]  graph really nice for you and you get to apply it and they you know similar to terraform they have
[1594.96 --> 1599.92]  their graph based way of applying so dependencies get created first and blah blah blah which is great
[1599.92 --> 1606.40]  um i like their extensibility though so for terraform if you want to extend terraform you need to
[1606.40 --> 1610.74]  contribute to the provider if there is one if there's not a provider you need to create a provider
[1610.74 --> 1618.44]  build that binary ship it in system initiative side you can just edit the typescript or you can go in
[1618.44 --> 1621.94]  their job typescript functions in and now you have a new asset to manage so like from the
[1621.94 --> 1627.10]  extensibility side i think they have a like a more extensible platform you know for the average
[1627.10 --> 1632.50]  developer right right right and you're an ops guy who likes typescript i don't actually use a lot of
[1632.50 --> 1636.78]  typescript i it's i use a lot of go i use a lot of go you don't seem to have a problem with that
[1636.78 --> 1642.06]  i don't it's it's typescript very readable right it's like it's not my favorite language but coming from
[1642.06 --> 1647.60]  another you know strongly typed language typescript works for me happy to hear that i just remember
[1647.60 --> 1652.76]  that one of the i think kelsey was on saying that one of the concerns is that it needs to be
[1652.76 --> 1657.94]  multilingual specifically you know back-end folk infrastructure folk aren't going to want to use
[1657.94 --> 1664.60]  typescript and so counterpoint yeah i think if you're like if you're a good engineer the tools
[1664.60 --> 1670.24]  matter less than knowing how to use them correctly amen right that that's what it is so if you if they're
[1670.24 --> 1675.38]  using typescript and i know how to use typescript and to do what i need to do why do i care so much
[1675.38 --> 1681.28]  right i'm using the thing it's okay right yeah i'm using the thing so for me it works out like
[1681.28 --> 1687.26]  do i maybe wish it was something like go or rust maybe but everybody knows typescript right like at
[1687.26 --> 1691.98]  this point it's it's it's a pretty ubiquitous language i think it's a good first choice for them
[1691.98 --> 1697.92]  if they want to expand later it's got a wide footprint of users it does it really does and then so not
[1697.92 --> 1702.74]  regard it smart yeah when you contrast it with something like palumi who like supports many
[1702.74 --> 1708.38]  languages i don't know if that's the right choice i think when you give people too many choices you
[1708.38 --> 1714.44]  fall into that like analysis paralysis situation right where you're like what choice what language
[1714.44 --> 1719.54]  do i use if team if this team is using python and that team's using go can they like contribute to
[1719.54 --> 1724.26]  each other's stuff or am i creating silos right so i don't know i don't know the right answer but
[1724.26 --> 1728.24]  yeah we'll see well it's a different thing so one thing that solomon said on the show about
[1728.24 --> 1733.28]  dagger is like they were qlang you know yes which is basically yaml on steroids if you don't know
[1733.28 --> 1739.54]  about it it's type it's strongly typed configuration language and that was a real hang-up for people
[1739.54 --> 1745.32]  because they wanted more power and so now they went the other direction right go sdk elixir sdk
[1745.32 --> 1753.60]  typescript sdk etc and i wonder if if like that distinction is significant from a declarative
[1753.60 --> 1759.76]  yaml-esque thing to a programming language but once you get to that point the language itself
[1759.76 --> 1766.54]  is less significant right yeah i think the win there is getting off of like the dsl yeah for them
[1766.54 --> 1770.48]  and then giving the opportunity to really just plug in whatever you need i don't know if it's
[1770.48 --> 1775.66]  right code right it's a right code proprietary versus whatever's out there exactly yeah exactly
[1775.66 --> 1779.82]  because there are there have been a lot of people that i've i work with so many customers over my time
[1779.82 --> 1785.96]  hashicorp that they asked for loops like proper like loops in programming languages and they had
[1785.96 --> 1793.56]  good use cases for them and you know the hashicorp hcl dsl wouldn't really enable that in that regard
[1793.56 --> 1797.72]  so yeah it's interesting to see what's out there though i'm i'm excited for all these new tools and
[1797.72 --> 1802.92]  i wish when i was doing more ops work earlier in my career a lot of these tools existed because it
[1802.92 --> 1807.68]  would have gave more choice i was kind of stuck with bash and ansible and in a sense right so
[1807.68 --> 1812.68]  well man appreciate you stopping by and telling the story thanks for having me it's a fun deep dive
[1812.68 --> 1817.50]  yeah yeah i'm happy to chat about these things it's more of a it's more like a shotgun dive
[1817.50 --> 1822.90]  you know we got a lot of stuff out there we splashed it we splashed it yeah sure splash
[1822.90 --> 1826.06]  no i appreciate y'all having me it's great to see you nice meeting y'all too
[1826.06 --> 1828.96]  you did it you're off the hot seat
[1828.96 --> 1830.16]  that's fun
[1830.16 --> 1831.96]  you
[1831.96 --> 1835.96]  you
[1835.96 --> 1837.96]  you
[1837.96 --> 1839.96]  you
[1839.96 --> 1841.96]  you
[1841.96 --> 1845.96]  you
[1845.96 --> 1847.96]  you
[1847.96 --> 1849.96]  you
[1849.96 --> 1858.96]  you
[1858.96 --> 1864.32]  what's up friends we're working closely with dot tech domains to feature startups that are
[1864.32 --> 1869.64]  participating in their startups dot tech program right here on the change log i've never seen
[1869.64 --> 1875.56]  something like this from one of our advertisers but it does make sense to me to show off not only
[1875.56 --> 1881.76]  what dot tech domains offer but also who is building on dot tech domains and i'm here with
[1881.76 --> 1890.00]  bastion co-founder of eyewear you can find them at eyewear dot tech e-y-e-w-a-r-e dot tech
[1890.00 --> 1897.26]  where they build a high-powered webcam eye tracking software used by amd microsoft and even intel
[1897.26 --> 1902.84]  bastion give me the backstory what what does eyewear do uh we're deep tech spinoff computer vision and ai
[1902.84 --> 1911.30]  spin-off from a swiss research lab we turn your webcam or 3d sensor into an eye tracker so you don't
[1911.30 --> 1919.18]  have to buy expensive hardware to get a reliable and robust eye tracking performance on your pc
[1919.18 --> 1928.38]  so we have two main products one is the gaze sense sdk which is an eye tracking sdk that companies like amd
[1928.38 --> 1933.92]  have used in collaboration with us to build for example the amd privacy view app that is now part
[1933.92 --> 1940.44]  of the radian software driver suite um there you can use eye tracking for certain features like
[1940.44 --> 1947.62]  privacy view it blurs out parts of the screen that you're not looking at um we also took that app and
[1947.62 --> 1953.42]  built our own solution called eyewear beam that is targeting gamers where you can turn your webcam
[1953.42 --> 1959.04]  into a gaming eye tracker for more immersive gameplay in for example simulator games over 200
[1959.04 --> 1964.34]  of them through the open track extension or you can use it for streaming or game recording to
[1964.34 --> 1971.26]  improve your own gameplay by re-watching your uh recordings with that overlay and seeing when you
[1971.26 --> 1977.34]  missed something uh during uh essential sections of your gameplay or just share it with the audience
[1977.34 --> 1984.14]  and engage better with them well this is definitely the next frontier are you only licensing focused or
[1984.14 --> 1990.66]  do you have any offerings that's ready for developers to consume and leverage in their projects so we with
[1990.66 --> 1995.12]  eyewear beam we are facing consumers directly with this app you can download it there's a free trial
[1995.12 --> 2002.94]  on our website and on steam so you can give it a go and and and and see how you like it um the the idea is
[2002.94 --> 2008.92]  still that we provide licensing solutions to big players to oems and and allow them to integrate
[2008.92 --> 2013.88]  eye tracking i think there's going to be a world where you're going to have headsets they're for sure
[2013.88 --> 2019.12]  going to come i'm going to be one of the users and eye tracking is an essential part of it but then
[2019.12 --> 2025.24]  you'll have a lot of just interfaces surfaces screens where where you will want to interact with
[2025.24 --> 2030.46]  them without a headset on and their eye tracking will also matter so there's for example these 3d screens
[2030.46 --> 2036.40]  3d stereoscopic displays where you would need eye tracking and similar situations so like it's going
[2036.40 --> 2041.46]  to be a hybrid setup and i think our technology is is an essential part of that talk to me about the
[2041.46 --> 2048.40]  choice of using a dot tech domain i think it's it was a logical decision to make from i think every
[2048.40 --> 2053.96]  startup will first take their name and then add a dot com behind it and try that out and then it's
[2053.96 --> 2059.70]  probably going to be too expensive or or taken already and then look for alternatives we are a deep tech
[2059.70 --> 2066.52]  company that has already part of it in the name so if if we put eyewear dot tech it makes it clear for
[2066.52 --> 2072.20]  third parties specifically for these potential clients that we want a license to that we are a
[2072.20 --> 2077.58]  tech provider we're a deep tech company we're spinoff and and i think that represents it pretty well
[2077.58 --> 2086.12]  okay make sure you check out eyewear dot tech that's e-y-e-w-a-r-e dot tech and of course go to
[2086.12 --> 2092.48]  startups dot tech slash changelog if you want to have your startup that's building on a dot tech domain
[2092.48 --> 2101.40]  featured on a show like this don't wait go to startups dot tech slash changelog again startups dot tech
[2101.40 --> 2103.22]  slash changelog
[2103.22 --> 2126.02]  all right so nitya rough director of the ospo at amazon is that right that's right open source program
[2126.02 --> 2134.80]  office for all of amazon aws and the uh stores devices other everything the whole nine yards
[2134.80 --> 2141.28]  so the ospo of ospos ospo of ospos my gosh that is that's got to be a big thing right on top of that
[2141.28 --> 2147.04]  you listen to the show i listen to the show that's an even bigger credential right you think so i don't
[2147.04 --> 2150.96]  think your credentials are your real credentials but i'm excited about your credentials i feel honored that you
[2150.96 --> 2159.82]  think that's an honor gosh i i'm a huge podcast fan i listen to podcasts uh on my walks and typically
[2159.82 --> 2165.74]  podcasts are about 24 minutes to 30 minutes right and my goal every day is to do at least a 30 minute
[2165.74 --> 2173.18]  walk so it really helps me kind of listen learn and walk every day 30 minutes i try let's talk about
[2173.18 --> 2178.30]  that for a second because that is a big deal yes too many people have health conditions and issues or
[2178.30 --> 2183.26]  whatever right and all they got to do is just walk yes for 20 minutes maybe 30 minutes every day
[2183.26 --> 2189.44]  just go enjoy the world right just go and see what's out there bam healthy there you go right
[2189.44 --> 2195.02]  i mean obviously a little bit of diet changes if you want to but like literally your heart and a lot
[2195.02 --> 2200.38]  your lungs all these things change if you just are a little active and they say you know small micro
[2200.38 --> 2206.30]  habits add up oh my gosh and what kind of books you read it's like compound interest so over the course
[2206.30 --> 2215.38]  of a year 30 multiplied by 365 yes all of a sudden you walk miles right day people are uh not that
[2215.38 --> 2222.08]  excited about one percent change until it compounds yes right yes if you have oh it's one percent no big
[2222.08 --> 2228.48]  deal right compound interest is fantastic yes today one percent tomorrow when i hear do the math
[2228.48 --> 2236.72]  me jared two percent hey chat gpt that's right where is chat gpt when you need it do this math
[2236.72 --> 2242.90]  for me that's a good thing okay cool love it so what does it take to be the ospo of ospos then what
[2242.90 --> 2248.06]  what do you what kind of things do you see what kind of stories can you tell us what led me to being
[2248.06 --> 2255.20]  here and sure that too but more so like what you're doing yeah as the ospo of ospos i mean amazon is a
[2255.20 --> 2259.00]  massive company yeah yeah i mean i probably have something on my front door right now from amazon
[2259.00 --> 2263.90]  yeah you know i do just sends me something every day does he really okay that's nice
[2263.90 --> 2268.98]  does he personalize it or no around my house i do say jeff a lot because
[2268.98 --> 2275.66]  do you it's we we all know it's jeff bezos but like i just say yeah i just referenced jeff i'm
[2275.66 --> 2279.22]  gonna talk to jeff about eggs if i want to change amazon i'm like i gotta call jeff
[2279.22 --> 2287.16]  it's funny you say that because every time i receive a package and i order things constantly
[2287.16 --> 2294.64]  on amazon i always say oh jeff sent me something today okay my husband said with jeff
[2294.64 --> 2301.76]  i said uh you know the jeff so we're of the same mind then so yes what does it take to
[2301.76 --> 2307.16]  run the ospo of ospos like we we know how big amazon is we know how influential it is as a brand and
[2307.16 --> 2313.50]  just of change aws has changed the way we compute i mean they were early on in the cloud essentially
[2313.50 --> 2318.64]  creating and inventing it but what is it like to be in that role what does open source play in that
[2318.64 --> 2324.58]  in that kind of position open source is really central to how we build our products how we build
[2324.58 --> 2331.76]  our infrastructure how we build our services it's a key component in everything we build so
[2331.76 --> 2338.52]  all of our builders all of our developers we call our developers builders because they're building
[2338.52 --> 2344.52]  something right software builders our job in the open source program office is to make it dead easy
[2344.52 --> 2350.72]  for our builders to work with open source so that from the time they consume to contribute to release
[2350.72 --> 2358.42]  to distribute to comply or to engage with open source we want to educate them on the easy way to do
[2358.42 --> 2365.24]  things the norms of open source build it into our workflows so that they don't have to open a ticket
[2365.24 --> 2372.40]  to ask us permission to use something or work with something so our job is to let them innovate
[2372.40 --> 2380.72]  with open source freely and openly and and we also play another role which is work with foundations
[2380.72 --> 2389.06]  open source communities projects people so that they know how to navigate amazon we help them
[2389.06 --> 2395.42]  navigate within amazon as to who to connect with who's doing what from an open source perspective
[2395.42 --> 2404.36]  and so we kind of are the bridge between open source community and amazon that's the role we play
[2404.36 --> 2412.46]  i would say historically amazon hasn't had the best reputation with regard to open source at least from
[2412.46 --> 2419.62]  the from my purview and i'm curious like what what your position is and maybe helping change that
[2419.62 --> 2425.66]  image or what you're doing to maybe change the way amazon approaches open source i mean you all do a lot
[2425.66 --> 2431.72]  in the world of open source i think that gets perhaps shrouded in other things like the hosting of you know
[2431.72 --> 2435.82]  open source projects and commercializing of that which is what we talk about more often i think
[2435.82 --> 2442.92]  what's your perspective on that um we want to do it through action we don't we want to do it through
[2442.92 --> 2450.52]  participating in communities by giving back by supporting maintainers and projects and foundations
[2450.52 --> 2460.10]  uh rather than just telling yeah and so i hope you've seen over the years that we are showing up more
[2460.10 --> 2470.48]  in open source forums uh we we donate a lot of aws credits for example that's true we do github sponsors
[2470.48 --> 2481.38]  uh we support foundations like the open ssf apache foundation uh linux foundation project cncf that sort
[2481.38 --> 2488.10]  of thing and we have lots of developers who are behind the scenes actually contributing to projects
[2488.10 --> 2494.56]  it's never enough because all of us consume a lot so we we have to keep working on that
[2494.56 --> 2502.08]  and most businesses not just amazon is challenged with business justification why should i dedicate
[2502.08 --> 2508.86]  you know five engineers to doing this work because there's so many competing needs right customer needs
[2508.86 --> 2515.62]  and product development needs and so on and so forth so we work hard as an ospo and open source marketing
[2515.62 --> 2521.98]  team who's downstairs at our booth to work with businesses to educate them on why they should be
[2521.98 --> 2528.80]  involved why they should contribute back what's the business case for setting aside people to do it so
[2528.80 --> 2536.02]  those are the ways we help the business do more with open source but we have to have a good business
[2536.02 --> 2544.30]  decision decision and argument uh because business is no business and they need the return on investment
[2544.30 --> 2550.48]  or justification for why they should be involved what are some of the things that your ospo does to
[2550.48 --> 2557.28]  enable these different business units to adopt open source to maintain open source to do more like what are the
[2557.28 --> 2565.74]  kind of things that helps them get there one of the easy things ospos can do is to create easier policies
[2565.74 --> 2576.86]  so in in a very restrictive regime uh you can make developers ask for permission go to lawyers and ask for
[2576.86 --> 2583.22]  permission for everything they use yeah which will deter them from using open source so we streamline
[2583.22 --> 2590.40]  and we make sure that a lot of open source licenses are already green lighted and that they automatically
[2590.40 --> 2596.84]  flow through the system without a ticket being cut or permission being asked so that's one easy way you
[2596.84 --> 2603.90]  make it easy for people to consume it we have relaxed some of the rules for contribution back if it's a
[2603.90 --> 2608.64]  simple contribution you don't even have to cut a ticket you can just go contribute okay even for
[2608.64 --> 2616.62]  releasing software uh we have something called simple releases so if it is a sample or a scientific work
[2616.62 --> 2623.62]  etc you don't even have to cut a ticket you can just release it and even the rules for reviewing
[2623.62 --> 2631.42]  bigger release of projects and stuff we really work with the business to help them see what the business
[2631.42 --> 2638.24]  reason is for contributing and how to run a successful project once you contribute it because you just
[2638.24 --> 2645.22]  don't want to dump it on github and run you want to be able to maintain it build a community a neutral
[2645.22 --> 2652.02]  governance all that stuff so we kind of make it easy in that fashion for business owners to know
[2652.02 --> 2661.20]  that we are here to support you and make it easier for you to do open source a lot of times teams don't want
[2661.20 --> 2666.82]  to do it because i'll say i don't want to go talk to our ip lawyer and i don't want to have to justify
[2666.82 --> 2674.28]  why i need to do this but if you take away all those excuses then it becomes easier for people to
[2674.28 --> 2681.66]  go do it how long has been the ospo been in place has it been in place for years half a decade eight
[2681.66 --> 2686.78]  years i mean they've become more popular in the last i would say five to eight years roughly but
[2686.78 --> 2691.36]  that's probably even farther fetching like more like in the last three to five how long has this ospo
[2691.36 --> 2697.90]  been in place the amazon ospo has been in place almost since 2007 2008 believe it or not really
[2697.90 --> 2704.60]  even further okay yeah one of my but it wasn't called an ospo 16 years yeah okay what was the
[2704.60 --> 2711.12]  version of it i think it was just called an open source office open source strategy office right or
[2711.12 --> 2720.86]  open source approvers my colleague henry yondel who is in my team he started it uh it was because
[2720.86 --> 2727.82]  you know the the gms and lawyers said please come someone who's knowledgeable cost a lot more
[2727.82 --> 2733.58]  money right lawyers cost a lot of money what attorneys yes right yes hour so i would much
[2733.58 --> 2739.14]  rather have policy in place that i can reference than a lawyer that has to spend an hour to charge
[2739.14 --> 2746.06]  you 700 bucks right any and maybe that's even cheap for an amazon type of attorney it's funny you
[2746.06 --> 2750.16]  mentioned that a lot of companies start their open source program office because they say
[2750.16 --> 2755.98]  we can't have everybody go to our lawyers and ask questions so if you have thousands of developers
[2755.98 --> 2760.62]  yeah all pinging them and say can i use this license can i use this license can i contribute this
[2760.62 --> 2769.10]  can i release this it is it it chews up a lot of valuable uh attorney time so often ospos kind of act as
[2769.10 --> 2776.54]  the front line and we we kind of act as the in between developers and legal and we handle a lot
[2776.54 --> 2781.50]  of the questions and the issues and the tickets that's funny it's called open source programs office
[2781.50 --> 2789.02]  when it's that yeah right like it's essentially the gateway to legal the cheaper not not just it's
[2789.02 --> 2794.54]  one role you described it just now i'm not saying that's only the way it is that's how a lot of ospos get started
[2794.54 --> 2801.18]  right because you have to do compliance when you consume open source right but then you know good
[2801.18 --> 2809.18]  ospos go beyond that and actually make it easy to work with community they go do uh they go work with
[2809.18 --> 2818.22]  foundations they publish they speak they share best practices you know they help the the company be a
[2818.22 --> 2824.22]  contributor and a leader in the community so you need to take it past compliance into
[2825.18 --> 2831.26]  really leaving something behind so yeah i mean general the generic ospo has been around for the
[2831.26 --> 2839.10]  last 10 15 years google facebook everyone had an open source program office there was a group called
[2839.10 --> 2845.50]  the to-do group which sits in the linux foundation which came along and created kind of a support system
[2845.50 --> 2852.78]  for open source program offices to share best practices across teams because we are all trying to do the same
[2852.78 --> 2859.82]  thing trying to make it easy for our developers to work in open source try to ease the legal burden try to
[2859.82 --> 2865.74]  engage more try to respect the norms of open source be a good citizen you know all of those kinds of things
[2865.74 --> 2872.54]  what are some of the challenges that you face now like today this week this month what are some
[2872.54 --> 2877.34]  challenges you're dealing with positive and negative like positive challenges in terms of like we gotta
[2877.34 --> 2881.66]  get this done this is a great thing and also ones like this sucks we gotta just deal with this and make it better
[2881.66 --> 2889.82]  i think scaling um what we do across the company is one of the challenges because especially in a large
[2889.82 --> 2896.86]  company when you have thousands of developers who you need to make aware of the policies and processes
[2896.86 --> 2903.90]  that we are here to help you it's hard to get the word across so we've been working on a program called
[2903.90 --> 2913.02]  champions where we have people in businesses become open source champions and enthusiasts and so you have a
[2913.02 --> 2920.70]  local person that you can talk to instead of coming to an ospo all the time because ospos typically tend to be small
[2920.70 --> 2928.30]  and they're serving thousands of developers so today we have 230 champions in the company that help local
[2928.30 --> 2934.62]  businesses across amazon have a local person who's an expert that they can reach out to right and they
[2934.62 --> 2941.66]  can then reach out to us if necessary so scaling is a challenge uh the second challenge is open source
[2941.66 --> 2948.70]  security and all the different places we need to get involved in from an open source security perspective
[2948.70 --> 2956.38]  working with open ssf working with upstream producers working with our security teams inside the company
[2956.94 --> 2964.54]  working with policy makers uh there's there's a lot going on in security so that's another big area of
[2964.54 --> 2973.50]  interest the third is ai um what's the role of open source in ai what are the different artifacts in ai
[2974.46 --> 2977.18]  how are they going to be licensed from an open source perspective
[2977.18 --> 2984.54]  working with osi and and trying to get our arms around making sure that we have a standard for
[2984.54 --> 2992.22]  open source artifacts is is important yeah and and you know with all of us using more and more models
[2992.22 --> 3001.18]  and more data sets helping our legal team again like we did for licenses helping them review and approve
[3001.18 --> 3008.54]  model use and data set use uh is something we're trying to do and finding good people to build your
[3008.54 --> 3013.90]  ospo is always hard yeah it probably is there's only a small group of people that would be people
[3013.90 --> 3021.42]  people that also like policy how did you land here how did i land at amazon well specifically in the ospo
[3021.42 --> 3027.18]  director of ospo like what brought you there yes i've been working in open source for 25 years now
[3027.18 --> 3034.54]  uh the my first job in open source was at silicon graphics uh working on open source strategy and
[3034.54 --> 3041.02]  support uh and i loved open source i fell in love and i said because it's such an intersectional
[3042.06 --> 3052.22]  role of strategy community technology law uh and it's just fabulous so i've been working in various
[3052.22 --> 3058.14]  companies companies in open source and it was about 10 years ago i was at sandisk and
[3058.14 --> 3065.74]  um my manager said to me i was the director of marketing there and he said you know every time
[3065.74 --> 3071.34]  you work with open source your eyes light up and maybe you should go do open source for the whole company
[3072.30 --> 3079.10]  and that kind of gave me the bug of yeah maybe i should run open source strategy for sandisk and i
[3079.10 --> 3086.06]  started i pitched the idea to our svp of marketing uh engineering and he said yes we need someone
[3086.06 --> 3093.42]  doing that so i became the first director of open source strategy at sandisk which then led to becoming
[3094.94 --> 3103.10]  the senior director of open source at comcast for five years so i started these ospo there and built it all
[3103.10 --> 3109.98]  the way and then so when amazon was looking for someone to lead their ospo they came to talk to me
[3110.86 --> 3118.46]  and i love the challenge of the scale of amazon and the width and breadth of things that they do
[3119.42 --> 3126.06]  and it's it's an open source geek's dream to kind of look at all of the different use cases and
[3126.06 --> 3133.90]  how we work in open source so here i am that's a good story yeah it's a fun journey what was that
[3133.90 --> 3139.02]  pitch like do you remember it when you pitched the svp of engineering back in the day like what you sold
[3139.02 --> 3149.10]  him yeah i i basically wrote a one and a half page document which said open source is so important even
[3149.10 --> 3155.74]  though we are a hardware company software is very important to flash and flash hardware that cannot
[3155.74 --> 3165.18]  function if stacks storage stacks and open source io does not know how to use the flash speed
[3165.18 --> 3170.70]  because most software stacks in those days were optimized for hard drives yeah and i said we need
[3170.70 --> 3177.90]  to change the software ecosystem around us if we need to get flash to be fully optimal working with
[3177.90 --> 3184.38]  software and i know the consumer group which works on usbs is is trying to do that i know
[3184.38 --> 3189.58]  our enterprise group is trying to do that this group is trying to do that we need to be involved
[3189.58 --> 3196.30]  in the linux foundation we need to work with the kernel we need so he said yes and we need to coordinate
[3196.30 --> 3202.62]  and leverage each other's work and we need to do it in a more intentional way rather than everybody going
[3202.62 --> 3209.98]  off and doing their own thing yeah and and with that we became members of the lf we started working more closely with
[3209.98 --> 3218.30]  uh all the storage subgroups and the kernel and uh started recruiting more open source friendly people we now
[3218.30 --> 3227.18]  started doing compliance better i started showing up at you know shows and huh it's a good sales pitch i would
[3227.18 --> 3239.18]  have bought it as well that was fun yeah that sounds like it was a very challenging coordination yeah it was because i still had to work with all these different divisions and
[3239.18 --> 3245.82]  understand their engagement with open source and understand their engagement with open source and where they were what their obstacles were
[3245.82 --> 3250.06]  how to what was the commonality across these teams
[3250.06 --> 3259.42]  etc i didn't own any resources i didn't have a team i was working with a cto and trying to help the company
[3259.42 --> 3269.18]  but now i have a team so it's it's so much nicer yeah to be able to scale and have really smart smart people
[3269.18 --> 3278.54]  at amazon uh who helped me uh get this work done yeah curious what your guidance is coming back to amazon
[3279.10 --> 3284.54]  i'm an engineer at amazon i have a library that i've written that facilitates something inside of our
[3284.54 --> 3291.50]  service it's generic i could open source it i come to whomever and say hey i like to open source this
[3292.22 --> 3296.38]  what is the guidance like you will do this you will license it that way it will be under this
[3297.26 --> 3303.58]  organization on github it will have this kind of a read me i mean do you guys yes step by step help
[3303.58 --> 3309.50]  people through this what does that guidance look like like what do you say they they typically have to
[3309.50 --> 3317.90]  write a document we we are big doc writers at amazon so they have to write a doc to get approval from
[3317.90 --> 3325.58]  their business their manager and their business owner that this is okay to open source and typically
[3325.58 --> 3331.98]  their business line lawyer may be involved in in approving that and then once it's approved they come to the
[3332.78 --> 3338.46]  open source program office we help them go through security review of the code we help them do
[3338.46 --> 3344.94]  something called uh it's an open source project called repo linter which looks through your code and
[3344.94 --> 3353.26]  make sure that you haven't got keys and uh proprietary information etc so it sanitizes it we help them
[3353.26 --> 3362.30]  attach an apache 2.0 license we make sure that they have a readme file code of conduct etc and then my i
[3362.30 --> 3370.62]  have a github team also who administers our external github they help them cut a ticket to open a repo put it
[3370.62 --> 3379.42]  in the right org we have a samples org we have a you know a lab org where all the lab papers are published
[3380.30 --> 3386.22]  and so they'll put it in the right org and they'll also monitor the org making sure it has a proper
[3386.22 --> 3393.10]  maintainer issues are not stale uh that we are you know being good citizens on on the project yeah
[3393.10 --> 3399.58]  cool that's a bit of a ceremony i would say right like it's yeah it's still somewhat imitating or
[3399.58 --> 3405.26]  intimidating to to have to go to your manager and be like hey this is cool because you kind of have to
[3405.26 --> 3409.50]  be vulnerable a little bit right i guess you are anyways when you're introducing code into the world
[3409.50 --> 3414.06]  you're being a little vulnerable with your your works but yeah yeah but like hey this thing is valuable
[3414.06 --> 3419.98]  enough then you said the business line attorney might have to approve it yes right and they still
[3419.98 --> 3425.34]  have to come to you for more stuff yeah it's a lot though still yet i think you have to be thoughtful
[3425.34 --> 3431.26]  if it's a a full library and a full project right you need to be thoughtful about what's the right
[3431.26 --> 3437.10]  thing to do and one of the right things to do is to resource it correctly if you're open sourcing it
[3437.10 --> 3443.26]  so that it can be maintained properly yeah very often teams will be very enthusiastic about
[3443.26 --> 3449.58]  open sourcing but not commit to maintaining it yeah and so we want to make sure that the business
[3449.58 --> 3456.30]  is fully behind it and that there is a good sound reason why it's the right thing to do
[3457.50 --> 3462.38]  it's like a liability in a way even too right and because liability in the fact that you have to
[3463.02 --> 3468.14]  show up it's one more thing to commit to it's one more yes that you don't that you can't say no to
[3468.14 --> 3473.34]  later on right it's a liability in that sense that from the business perspective as amazon you have to
[3473.34 --> 3479.02]  say yeah yeah this makes sense not just open source but for us to open source yes yes and and you know
[3479.02 --> 3487.26]  small little things that you want to release like a sample uh a sample code or something we really don't do
[3487.26 --> 3494.14]  that much due diligence yeah but if it's a full-blown project we've released bottle rocket and firecracker
[3494.14 --> 3501.26]  and finch and projects like that we really want to make sure we do it right we owe it to open source
[3501.26 --> 3506.94]  to do it right and not just throw it over the wall let's say there's a case where this library you
[3506.94 --> 3513.66]  written jared is generic it's not it's useful to some but y'all say well it makes sense to be open
[3513.66 --> 3519.10]  source but not from us do you allow that person to put it open source on their own if they've written
[3519.10 --> 3524.06]  it on company time or for company resources is there ever a time whenever it's like it's not
[3524.06 --> 3529.02]  right for us but it's okay for you i haven't seen a situation where we have said it's okay for you to
[3529.02 --> 3535.90]  go off and do it on your own because if it's done on company time it we need to make sure it's done right
[3536.70 --> 3542.06]  if it's if it's their pet project they've been working on in the weekend something to do with dairy
[3542.06 --> 3548.86]  farming or something different you'll never get into dairy farming but farming is getting into open source
[3548.86 --> 3556.86]  agriculture amazon might i mean you're becoming but there is uh a project in the linux foundation
[3556.86 --> 3562.38]  around farming is there yeah that's awesome yeah well i mean amazon is a i don't know if it's a
[3562.38 --> 3567.26]  conglomerate but you're definitely the organization expands into areas where you may have i mean whole
[3567.26 --> 3572.22]  foods is an example for sure where all of a sudden now you're a grocer and so maybe there are
[3572.22 --> 3577.50]  competitive things that you don't know about but you eventually will i don't know and and we need to
[3577.50 --> 3585.02]  do due diligence to make sure that it's not something that we need to care about uh what are
[3585.02 --> 3590.94]  some of the darlings of amazon open source like if you were to name like here's our biggest open
[3590.94 --> 3596.54]  source projects you you you listed a few there or like the ones that the ospo really loves like ah
[3596.54 --> 3603.18]  a shining example of amazon open source what are some examples i think if you go on uh aws open
[3603.18 --> 3610.54]  you'll see some of the projects listed there and blogs clearly bottle rocket firecracker finch
[3611.10 --> 3618.06]  uh real artos what else those are some of the ones that i can think of off the top of my head
[3618.06 --> 3625.50]  but we contribute to a lot of different projects yeah like openjdk we take what we do inside the
[3625.50 --> 3633.66]  company to harden it and to make it easy to use and we provide it as coreto which is an open free
[3633.66 --> 3641.02]  distribution for everybody to use so there's lots of really fun things like that that we contribute to
[3641.82 --> 3647.02]  well we appreciate you stopping by and chatting with us thank you
[3655.50 --> 3662.14]  what's up friends i'm here with vj raji ceo and founder of statsig where they help thousands of
[3662.14 --> 3667.98]  companies from startups to fortune 500s to ship faster and smarter with a unified platform for
[3667.98 --> 3675.02]  feature flags experimentation and analytics so vj what's the inception story of statsig why did you
[3675.02 --> 3680.14]  build this yeah so statsig started about two and a half years ago and before that i was at facebook
[3680.14 --> 3686.62]  for 10 years where i saw firsthand the set of tools that people or engineers inside facebook had access
[3686.62 --> 3693.18]  to and this breadth and depth of the tools that actually led to the formation of the canonical
[3693.18 --> 3698.22]  engineering culture that facebook is famous for and that also got me thinking about like you know
[3698.22 --> 3703.66]  how do you distill all of that and bring it out to everyone if every company wants to like build
[3703.66 --> 3708.62]  that kind of an engineering culture of building and shipping things really fast using data to make
[3708.62 --> 3714.54]  uh data informed decisions and then also informed like what do you need to go invest in next and all
[3714.54 --> 3720.62]  of that was like fascinating was really really powerful so so much so that i decided to quit facebook and start
[3720.62 --> 3726.38]  this company yeah so in the last two and a half years we've been building those tools that are helping
[3726.38 --> 3732.70]  engineers today to build and ship new features and then roll them out and as they're rolling it out also
[3732.70 --> 3738.54]  understand the impact of those features does it have bugs does it impact your customers in the way that you
[3738.54 --> 3744.14]  expected it or are there some side effects unintended side effects and knowing those things help you make
[3744.14 --> 3750.38]  your product better it's somewhat common now to hear this train of thought where an engineer developer
[3750.38 --> 3757.42]  was at one of the big companies facebook google airbnb you name it and they get used to certain tooling on the
[3757.42 --> 3763.66]  inside they get used to certain workflows certain developer culture certain ways of doing things tooling of
[3763.66 --> 3771.58]  course and then they leave and they miss everything they had while at that company and they go and
[3771.58 --> 3776.06]  they start their own company like you did what are your thoughts on that what are your thoughts on that
[3776.06 --> 3782.70]  kind of tech being on the inside of the big companies and those of us out here not in those companies without
[3782.70 --> 3788.78]  that tooling in order to get the same level of sophistication of tools that companies like facebook google airbnb
[3788.78 --> 3793.26]  and uber half you need to invest quite a bit you need to like take some of your best engineers and
[3793.26 --> 3799.66]  then go have them go build tools like this and not every company has the luxury to go do that right
[3799.66 --> 3804.78]  because it's a pretty large investment and so the fact that the sophistication of those tools inside
[3804.78 --> 3811.02]  these companies have advanced so much and that's like left behind most of the other companies and the
[3811.02 --> 3816.86]  tooling that they're they get access to is that's that's exactly the opportunity that i was like okay well we
[3816.86 --> 3823.26]  need to bring those sophistication um outside so everybody can be you know benefiting from these okay
[3823.26 --> 3830.78]  the next step is to go to statsig.com slash changelaw they're offering our fans free white glove
[3830.78 --> 3838.70]  onboarding including migration support in addition to five million free events per month that's massive
[3838.70 --> 3849.34]  test drive stat sig today at statsig.com slash changelaw that's s-t-a-t-s-i-g.com slash changelaw the link is in the show notes
[3849.34 --> 3870.30]  all right well we have uh jordan harband hey man welcome good good good thanks for having me
[3870.30 --> 3875.74]  you are an open source maintainer at large i know you mostly through the javascript side of things tell us about yourself
[3875.74 --> 3883.66]  yeah um let's see so i maintain 400 450 some npm packages as well as nvm um they account for like
[3883.66 --> 3889.98]  five to ten percent of npm's download traffic which is terrifyingly high i've been on tc39 which is the
[3889.98 --> 3896.38]  javascript standards committee right since 2014 i was an editor of the spec for three years um long time
[3896.38 --> 3903.50]  yeah when do you sleep then well i in between you know open source and taking care of my kids
[3903.50 --> 3910.62]  i squeeze in a few hours here and there wow yeah 450 repositories surely those all those don't all
[3910.62 --> 3915.90]  require active maintenance no i the vast majority of them are effectively done and only need occasional
[3915.90 --> 3921.82]  like dependency updates and things like that so it's um you know there's it's the that 80 20 thing
[3921.82 --> 3928.30]  right 20 of the packages take 80 of my time right you know the rest are pretty self self-sufficient okay
[3928.30 --> 3935.82]  from the tc39 lens when is temporal coming so when can we use this yeah so that that when can we use
[3935.82 --> 3941.74]  it is the right question so temporal's been stage three for two years now uh stage three usually is the
[3941.74 --> 3948.54]  time to signal hey browsers you can ship this users you can start using it um however temporal has had
[3948.54 --> 3954.86]  uh what we call normative changes like observable changes from javascript uh for almost every two months
[3954.86 --> 3960.62]  since it got stage three which to me tells me it's not ready like api changes or what do you mean
[3961.18 --> 3966.06]  some minor api changes some semantic changes it's it's because it's such a large and complex proposal
[3966.06 --> 3971.90]  that it was a largely impossible to thoroughly review it before it got to stage three everyone
[3971.90 --> 3976.62]  did what it is he doesn't know what it is yeah so uh school me have you ever written stuff with code
[3976.62 --> 3982.62]  with the date object in javascript yeah uh so you may understand you may realize that the date object sucks
[3982.62 --> 3986.70]  it is awful okay it's api is terrible it's like i haven't used enough to know that that's fine
[3986.70 --> 3991.50]  a lot of things yeah it it's like mutable so you can change it all the time which means it's hard to
[3991.50 --> 3997.18]  keep track of what things are it can't be trusted uh it has really poor support for localization and
[3997.18 --> 4002.46]  all the different time zones in the world and it's really hard to do date and time math that's reliable
[4002.46 --> 4007.66]  and so on so temporal is a proposal that was originally championed by the moment js maintainers
[4007.66 --> 4015.90]  that uh it basically provides like i think it's seven new globals that all uh that they're all
[4015.90 --> 4023.98]  under the the temporal object that allow you to do like reasonable date time operations uh and so it
[4023.98 --> 4030.38]  takes a lot of inspiration from uh actually a java library called joda time um and although i'm not a
[4030.38 --> 4035.26]  big fan of java or taking inspiration from java like this actually is is a java library that's done things
[4035.26 --> 4040.14]  really right and you know we've still of course made some tweaks to make it fit javascript idioms
[4040.14 --> 4046.06]  like java uh that's a that's a topic for another time okay all right fair enough but but either way
[4046.06 --> 4051.18]  the like you can do you'll be able to create a timestamp effectively as one object you'll be able
[4051.18 --> 4055.26]  to create like your birthday that doesn't have a time associated with it so be you'll be able to
[4055.26 --> 4061.34]  create just a day year and month and that's all it represents you'll be able to create a duration
[4061.34 --> 4066.62]  like an object that spans two timestamps and you'll be able to do reasonable things with that so it's
[4066.62 --> 4071.50]  going to make working with dates and times infinitely easier and less painful in javascript so i'm very
[4071.50 --> 4076.06]  excited as are a lot of other people about being able to use this as am i well hence i say when can
[4076.06 --> 4081.50]  i use exactly so okay so it's been in it's a third it's been working on it a while so the stages are zero
[4081.50 --> 4086.06]  through four okay four is when it lands in the spec three is usually when things start shipping it when you
[4086.06 --> 4091.02]  can use it um and it's been in stage three for two years but we just had a tc39 meeting two or three
[4091.02 --> 4095.90]  weeks ago and that was the first tc39 meeting since it got stage three that there were no normative
[4095.90 --> 4100.86]  changes to it okay so i'm settling down yes so it's settling down exactly and i'm i'm holding my
[4100.86 --> 4106.70]  breath because if at the next tc39 meeting it doesn't have any normative changes that's when like
[4106.70 --> 4112.78]  so i'm a polyfill maintainer i have like a hundred plus different polyfills uh for for language features
[4112.78 --> 4118.06]  so if in the next tc39 meeting it doesn't have any normative changes to me that tells me it's ready
[4118.06 --> 4122.14]  for me to start implementing it as a polyfill yeah which you know everybody can have their own
[4122.14 --> 4126.06]  signals you don't have to rely on just what i say but if i feel like it's worthy for a polyfill
[4126.06 --> 4129.82]  that's when i'm going to start recommending people use it in production because at that point it's
[4129.82 --> 4134.78]  stable enough uh and there is it available to use but just not stable so you shouldn't use it basically
[4134.78 --> 4139.82]  that's exactly right there are polyfills out there but they don't typically a polyfill tries to be as
[4139.82 --> 4145.18]  backwards compatible as possible so you can use the new feature in the oldest possible environments the
[4145.18 --> 4149.90]  polyfills that are currently available don't have that as a goal they're just trying to replicate
[4149.90 --> 4156.06]  the api in modern feature with modern features so um that's good enough if you happen to be
[4156.06 --> 4161.50]  supporting like just the latest chrome or something but most production web apps need to support farther
[4161.50 --> 4166.94]  back than that in every browser and so and in addition in addition to that there's those api changes
[4166.94 --> 4171.10]  i told you about so that's why you i would say you shouldn't have been using it in production yet
[4171.10 --> 4175.34]  yeah but now that the api is settling down i'm hoping that that will change and we'll all be
[4175.34 --> 4181.02]  able to start using it okay when your polyfill is done let us know we'll have a big js party absolutely
[4181.02 --> 4185.42]  we'll all celebrate so have the moment js folks actually obsoleted themselves or will you still
[4185.42 --> 4189.42]  need something like that they they will have once temporal is usable in production just completely
[4189.98 --> 4195.82]  unfortunately for in my opinion they announced that moment is done essentially like two years ago yeah
[4195.82 --> 4201.18]  um and i don't think they used the term deprecated but essentially they're saying you probably should
[4201.18 --> 4206.46]  stop using moment we're not going to change it anymore like go use temporal but because temporal
[4206.46 --> 4212.94]  wasn't quite stable yet like i wish they had saved that kind of uh impact for the moment when it's
[4212.94 --> 4217.42]  stable but nonetheless um all of those things will become aligned at the point where temporal is
[4217.42 --> 4222.46]  stable and ready to use you have closed doors and people waiting outside exactly long line of
[4222.46 --> 4228.06]  people give me the black friday temporal day exactly right and it is coming rush let's use it
[4228.06 --> 4231.98]  okay certainly there's a lot of people that are still using moment you know absolutely for sure yeah
[4232.78 --> 4237.98]  and i have a library that i i maintain as well that uses moment and as and i'm going to migrate it
[4237.98 --> 4242.22]  straight to temporal yeah people have been asking me to migrate it to date functions or the other
[4242.22 --> 4247.10]  alternatives out there and i just didn't want to do two migrations because the instant temporal is usable
[4247.10 --> 4251.50]  everything else is obsolete so i'm just going to wait until temporal is the thing i can migrate to so
[4251.50 --> 4256.86]  that'll be exciting that'll be an exciting day absolutely thinking about your open source and
[4256.86 --> 4263.26]  your life and your lack of sleep are you able to make money off of this have you been i mean because
[4263.26 --> 4268.54]  you you're kind of crucial at this point to the npm ecosystem as a as a human it seems yeah i mean
[4269.10 --> 4276.54]  i would say that the amount i make off of my projects is i'm very grateful for it and it's enough
[4276.54 --> 4282.46]  that if i were single and in my 20s i could do it full time but i am not single and i have kids and
[4282.46 --> 4291.42]  i'm not in my 20s and uh it just doesn't cover the bills so um i've done the math and if my most
[4291.42 --> 4297.66]  lucrative package like i look at my most lucrative package and then i look at the my most used package
[4297.66 --> 4302.30]  and if i extrapolated all that out for all my packages i would be able to do open source full time
[4302.30 --> 4308.06]  um but at the moment that's not the case so i i would definitely be very happy to see a world where
[4308.62 --> 4314.70]  all of the profitable corporations that are using you know people's open source packages mine included
[4314.70 --> 4318.78]  are able to contribute even a tiny fraction of their profit at that point i think it will become
[4318.78 --> 4325.02]  a much more viable world for open source maintainers what accounts for the diff between those two things
[4325.02 --> 4331.26]  um i just think it's uh because there's no like so this is capitalism the world we live in right
[4331.26 --> 4335.82]  sure which means that there's only two levers you can apply capital and regulation and there's no
[4335.82 --> 4343.34]  regulation that's forcing anyone to contribute to their you know tech infrastructure their open source
[4343.34 --> 4348.30]  tech infrastructure uh you could perhaps look at fiduciary duty and say that they do in fact have
[4348.30 --> 4353.66]  a requirement but it's not enforced in that way at least right um so without the regulation there needs
[4353.66 --> 4358.78]  to be a capital incentive for them to do it and there is one it's just a really hard one to
[4358.78 --> 4362.38]  it's invisible sometimes yeah it's invisible it's really hard to talk about it in a way that's
[4362.38 --> 4367.26]  quantifiable you can point to and be like you have risked this amount of money because you didn't invest
[4367.26 --> 4372.14]  in this thing it's it's like really hard to demonstrate an roi or impact to the bottom line
[4372.14 --> 4377.34]  right um but it absolutely i think ties like it couples to everyone's bottom line and that if you
[4377.34 --> 4381.58]  don't maintain your infrastructure it's going to crumble and fall apart and then there goes your company
[4381.58 --> 4389.42]  so when we go back to your packages and talk about the most supported yeah and then the most used
[4390.54 --> 4396.94]  those are different right yeah why is the most used not the most supported uh um i think part of
[4396.94 --> 4403.18]  that is because most of my packages are end up being people's transitive dependencies so like i'm
[4403.18 --> 4407.66]  most of my stuff isn't like babble or eslint or webpack where people are choosing it right most of my
[4407.66 --> 4413.02]  stuff is chosen by the maintainers of those packages or three or four levels deep right and so
[4413.02 --> 4417.82]  even though my code is in almost every application on the planet like the number of people that have
[4417.82 --> 4426.06]  chosen me is very small right and so i think that's a big part of it uh i think also that the the specific
[4426.06 --> 4431.18]  organizations that have chosen to give back are just going to always use some subset of what's out there
[4431.18 --> 4436.46]  and so it's i what i'm seeing i think is that the ones that are most supported just happen to be in
[4436.46 --> 4440.70]  that subset subset like i don't know if there's a good rationale for it yeah it might just be the way
[4440.70 --> 4447.18]  it is i kind of see if it is like a movie and you have your scarlett johansson and then you have your
[4447.18 --> 4451.90]  audio engineer yeah and it's like they're both crucial right and maybe she knows that this is the
[4451.90 --> 4457.10]  best audio engineer in the world and so he's coming with me or whatever yeah but the studio doesn't
[4457.10 --> 4461.66]  and i think that's exactly right like when everyone watches the you know the academy awards or whatever
[4462.06 --> 4466.30]  everyone pays real close attention to the best actor or actress but they don't pay as much attention to
[4466.30 --> 4471.18]  like the best sound guy or the best costume person or whatever even though the industry knows that
[4471.18 --> 4474.70]  those are the best people and really wants to hire them in fact even at the oscars i think they have
[4474.70 --> 4479.10]  like the engineering style oscars have their own separate banquet exactly the day before or whatever
[4479.10 --> 4483.18]  because they know that's not what people want to watch yeah right so it's kind of that same problem in a
[4483.18 --> 4487.02]  different in a different situation but the the crucial difference here though is that that's
[4487.02 --> 4493.50]  a business an industry and they the money that comes in from the actors the well-known faces
[4494.06 --> 4498.94]  does in fact filter back to all the people who support it but in open source no one's paying
[4498.94 --> 4503.34]  any money for the software so there's nothing to filter back to all those transitive authors which
[4503.34 --> 4509.02]  is in fact why i really like sites like tidelift and thanks.dev they are the ones like get up sponsors
[4509.02 --> 4515.42]  and open collective and so on are great but tidelift and thanks.dev really focus on kind of surfacing and
[4515.42 --> 4520.14]  filtering the money through to all the transitive dependencies so folks like me who are the
[4520.14 --> 4524.94]  backbone of all of these projects actually get see some of that support whereas with github sponsors
[4525.66 --> 4530.70]  you know people don't know who i am to go click on me and support myself right how can we get you more
[4530.70 --> 4536.54]  well known to the people that use you via transient dependencies like why why that's how can we get
[4536.54 --> 4542.30]  that that visibility i wish i knew the answer to that okay um that's the hard question here certainly
[4542.30 --> 4548.38]  i think part of it is is the kind of the skills that it takes to be a good engineer are very
[4548.38 --> 4551.42]  different than the skills it takes to be a good manager and they're very different from the skills
[4551.42 --> 4555.82]  that it takes to be a good influencer or promoter right these are all there's overlap but they're all
[4555.82 --> 4561.26]  distinct skill sets yeah and some people have the skill set to like go on make a twitch stream every
[4561.26 --> 4567.98]  day or write blogs you know periodically or like tweet the exact right hot takes you know and so on
[4567.98 --> 4573.34]  and and i i don't have zero of that skill but i just don't have enough of it i think to get the
[4573.34 --> 4579.50]  audience that i would need to get that visibility right um and i don't know if it's necessarily a
[4579.50 --> 4585.58]  good idea for me to assume that that's the only path i can follow um but i certainly haven't
[4585.58 --> 4591.50]  dived deep and tried to become an influencer in that right i don't know if this is our doing jared
[4591.50 --> 4597.58]  but we just had the maintainer and creator of askeenama on the podcast and one thing we kind of
[4597.58 --> 4602.46]  like did heavy-handedly at least i did and i think you agreed because i you didn't i agree that it was
[4602.46 --> 4609.42]  heavy-handed you didn't be like dude don't do that i was like hey change the audience let's make his
[4609.42 --> 4616.30]  dream to work on askeenama more full-time a reality yeah and he has a get up sponsors page we link to
[4616.30 --> 4620.78]  that that's the only conduit for which he's taking money from the community to say hey you support me
[4620.78 --> 4624.78]  in this effort to do this thing and you see see the big picture but it's going to take time to get
[4624.78 --> 4633.34]  there yeah we added two if if the number uptick is our doing yeah we added two from seven to nine
[4633.34 --> 4640.62]  that's great is that great well so it's it's great in relative terms because so it's sort of like
[4641.42 --> 4646.38]  if you have someone starving and you give them a tiny piece of bread it's great for them it's not
[4646.38 --> 4651.42]  enough it's not sufficient it shouldn't be great it's the right direction yes it's the right it didn't
[4651.42 --> 4656.94]  go from seven to five right exactly like and we're taking it back and seven to nine like that is that is
[4656.94 --> 4662.70]  great it's just nowhere near sufficient yeah exactly and so like every if i happen to get a new sponsor from
[4662.70 --> 4667.66]  from this you know conversation that's awesome it's just like it's not one new sponsor that's
[4667.66 --> 4674.70]  going to move the needle right you know if enough people do it it will matter i i think that the folks
[4674.70 --> 4680.30]  that should be paying you probably are profitable corporations that leverage the dependencies for
[4680.30 --> 4686.06]  which you are a transit dependency of yeah right like i agree it's not truly the listeners but the
[4686.06 --> 4691.02]  listeners for which they have influence at the place they they operate at and have you as a dependency
[4691.02 --> 4696.30]  in their graph when people ask me about that's what i think our request is is like examine that
[4696.30 --> 4702.30]  be aware of it because if not yeah what will happen to you if you if if this doesn't change in the next
[4702.30 --> 4707.18]  year or whatever time frame like how does that change how you operate in open source yeah i mean
[4707.90 --> 4711.50]  before i get to your question i was just like i think when somebody sponsors me or they they ask hey
[4711.50 --> 4715.82]  can i sponsor you i'm always appreciative i say yes of course thank you it really means a lot it's
[4715.82 --> 4721.10]  validation for me right even if it's a dollar it's still that somebody like cares enough right to vote
[4721.10 --> 4726.14]  with their wallet that matters however if you really want to help go tell your employer right
[4726.14 --> 4731.02]  right because once you get a company starting to put money into these sorts of things it the the
[4731.02 --> 4736.30]  incremental difference to putting more money in is so small but it's like that first getting through
[4736.30 --> 4740.78]  all the boilerplate of getting the finances approved and getting the money like pipeline hooked up
[4740.78 --> 4745.58]  like that's a pain in the butt but once you've got that hooked up you can add more money you can
[4745.58 --> 4749.98]  pay different people like it becomes a much more permanent thing yeah um and so that's what i'd like
[4749.98 --> 4754.70]  to see and then so your question is if this doesn't change fast enough what will happen well i'm going to
[4754.70 --> 4760.62]  have to keep getting jobs that aren't full-time open source and keep trying to squeeze it in and as a
[4760.62 --> 4767.90]  result like some of the things i really want to or need to work on are going to keep falling by the wayside
[4767.90 --> 4772.78]  i mean there are specific tasks large tasks that i have wanted to do for years and have not had the
[4772.78 --> 4779.18]  time to do it yeah um i'm the maintainer of enzyme and we don't support react 17 or 18 yet because i've
[4779.18 --> 4785.50]  been the only maintainer on it for seven years and i haven't had time to like set aside a whole month or
[4785.50 --> 4793.66]  two to do it and but i've had a hundred employees of companies post on the repo saying this is blocking us
[4793.66 --> 4798.86]  we're gonna have to spend a whole like developer month to like migrate our test suite to rtl or
[4798.86 --> 4805.18]  something it's like well have your developers help me fix it and like not one company has actually put
[4805.18 --> 4811.98]  money or time towards this problem it could have been solved four years ago and but it's still not
[4811.98 --> 4817.98]  solved because i'm not i can justify taking a few hours or a day to work on something i cannot set aside
[4817.98 --> 4823.26]  all income for a month yeah like that's just not real that's a non-starter that's uncalled for will
[4823.26 --> 4831.26]  you quit will you ever break i hope not i haven't yet how long you've been doing it um i i mean i have
[4831.26 --> 4838.06]  an unbroken github streak dating back to 2014 so what does that mean like i've done i've committed and or
[4838.06 --> 4847.10]  reviewed code uh and or merged code uh every day since 2014 yeah that's that's an amazing it's a long time
[4847.10 --> 4851.42]  yeah are you sure you're not a robot doing it for you i mean no it's i mean and it's it's it's a it's
[4851.42 --> 4855.74]  a system that's incredibly easy to game and cheat right yeah so it's for me it's more of more of like
[4855.74 --> 4861.50]  a it's a personal meditative thing yeah where it's like some days i do a lot but most days i'm just kind
[4861.50 --> 4867.82]  of checking in i do a few few updates i triage some things i move on right and it's it's the way i kind
[4867.82 --> 4874.86]  of yeah myself regular very regular 2014 man you're coming up on a decade that's a ways a couple years
[4874.86 --> 4879.66]  back github made these 3d prints of your contribution graph for a specific year and
[4879.66 --> 4885.02]  they mailed it out to select maintainers and i went ahead and went on the site that's like skyline.github.com
[4885.02 --> 4890.22]  or something and you can download them for any year and so i have a whole city now of my entire streak
[4890.78 --> 4896.22]  that's on my desk it looks really cool send us a picture that i want to see we'll include that in
[4896.22 --> 4901.50]  the show that's spectacular that is cool so thanks.dev is cool because they're actually
[4901.50 --> 4906.78]  general tell us what they do they generate where you send your money to based on your
[4906.78 --> 4911.50]  dependency yeah so both tide lift and thanks.dev right they um you give them your your lock file
[4911.50 --> 4916.86]  your manifest right and then they figure out your entire dependency graph and then you just put money
[4916.86 --> 4922.94]  in and then they distribute it out and thanks.dev gives you some granular control about like how deep
[4922.94 --> 4928.30]  you can go which probably appeals to some but like actually hurts me because i'm towards the bottom of
[4928.30 --> 4935.02]  that graph but like nonetheless the um it's good to have more competition out there more sites trying
[4935.02 --> 4941.34]  to get maintainers paid yeah what do you know about their algorithm if you're not much you said earlier
[4941.34 --> 4947.18]  yeah that you're in rephrase it for me it's not like you're in all software a large majority of
[4947.18 --> 4953.42]  software out there i am in most i think uh javascript applications even a little bit like if if you go and
[4953.42 --> 4958.94]  type npm fund in almost any javascript application my name will be in there not everyone and it's
[4958.94 --> 4963.90]  and it might be in there for one package it might be in there for 50 but it's in there somewhere um
[4963.90 --> 4968.30]  and it might be an inconsequential piece right like i'm not trying to claim that i am an
[4968.30 --> 4973.10]  irreplaceable part of sure most javascript of even any javascript applications right it's just that
[4973.10 --> 4978.78]  i happen to be in there yeah i've uh something i've done has made life easier for somebody along the way
[4978.78 --> 4983.66]  yeah have they spoken at all ty left about their the way they distribute those funds how they
[4983.66 --> 4987.50]  weighed it talked about the specific algorithm and how they weighed it but i'm sure they i mean
[4987.50 --> 4991.74]  they've been doing it for a long time yeah um and they have their upstream conference you know
[4991.74 --> 4997.02]  last couple years um i was part of their keynote this year actually um talking about how i took over
[4997.02 --> 5002.54]  packages when a former npm author prolific author decided to kind of delete his github and
[5003.42 --> 5008.70]  quit the ecosystem so i was able to take over like a dozen or so of his very highly dependent packages
[5008.70 --> 5013.42]  so like i think that um so the specifics i don't know and i think they tweak it right i've seen the
[5013.42 --> 5021.18]  amounts change over time um i think that the the the goal like tide lift has a more kind of enterprise
[5021.18 --> 5026.06]  focused goal which is like you depend on these things and you need them to you know have a certain
[5026.06 --> 5031.34]  amount of security and responsiveness and so on and so in in turn for maintainers doing those tasks they
[5031.34 --> 5037.66]  get a portion of the money thanks.dev i don't have to do anything to get it so that's more of a like uh
[5038.30 --> 5044.30]  patronage gratitude based model right um and so in that regard you can support more maintainers
[5044.30 --> 5047.98]  because they don't have to do anything to do it but you're not necessarily getting as much out of it
[5047.98 --> 5051.82]  as you would through tideless so there's it kind of depends on your preferred approach yeah and you
[5051.82 --> 5055.58]  know if i'm talking to a company who's in a generous state of mind i would encourage them to do both
[5055.58 --> 5062.14]  have you considered sponsorware i i mean i've thought about it every time i've seen authors try it
[5062.14 --> 5067.98]  i mean i remember like i grew up in the late 80s early 90s where shareware was a big thing where
[5067.98 --> 5071.82]  all you get all these games and you could use them for free but they'd kind of bug you and be like hey
[5071.82 --> 5077.42]  if you send us five bucks we can turn off this annoying warning and you know i i appreciated the
[5077.42 --> 5082.94]  spirit of it let me like try out the software and you know but i didn't have any money as a kid so i
[5082.94 --> 5088.78]  didn't i just ignored the warning the whole time right and very rarely did i end up when i had the money
[5088.78 --> 5093.26]  get to the point where i was like sure i'll pay for this yeah you know it just kind of didn't
[5093.26 --> 5099.66]  because i kind of think of it as free so i don't know if there is some solution out there hopefully
[5099.66 --> 5105.02]  to you know the nice thing about sponsorware specifically is that i'm thinking specifically
[5105.02 --> 5111.02]  your example of enzyme and all these engineers want this feature this upgrade or whatever you know
[5111.02 --> 5116.62]  call it what it is this bit of code to be written and they work for companies like you said who
[5116.62 --> 5121.58]  could definitely afford yeah right and so you develop that in a closed source environment but
[5121.58 --> 5126.78]  available all your sponsors right and so if they're a sponsor they're already in on it and then you set
[5126.78 --> 5131.10]  a threshold if i get to this many sponsors it goes out to everyone and so they can get their early access
[5131.10 --> 5135.74]  they can afford it it's not a kid who wants to play with a toy right it's a it's a well-funded company
[5135.74 --> 5139.98]  yeah they can get access now obviously this does require you to invest because you got to build it first
[5139.98 --> 5144.70]  i think that's it it's a chicken and egg there's a there is money at the end of the i mean if it's a
[5144.70 --> 5150.14]  desirable thing there's money at the end and because it's a sponsorship it raises your baseline
[5150.14 --> 5155.42]  right because now they're a monthly sponsor i think that that would work really well if i had the sort
[5155.42 --> 5161.90]  of direct software like babble eslint webpack um i don't think it would work as well for my transitive
[5161.90 --> 5167.26]  packages which is the majority of them right i so but i think also even if i had like even if something
[5167.26 --> 5173.98]  like enzyme i think that i in order to spend the time to make something that would be compelling
[5173.98 --> 5179.98]  enough to want people to pay for early access to i'd need to be able to pay for my time and so
[5179.98 --> 5184.70]  that's the chicken and egg thing where like if i had some companies show up and be like we will pay
[5184.70 --> 5189.42]  you money for this early adapter and as you know but you have to keep it exclusive for us for six months
[5189.42 --> 5194.94]  or something yeah then i would do it because it would get it done faster than no money but yeah if but
[5194.94 --> 5199.02]  i'm not going to just do it and then like dangle it like a carrot that feels like it violates the
[5199.02 --> 5204.86]  ethos of open source to me a bit um and like i can see that that's part of the challenge right
[5204.86 --> 5210.70]  because the philosophy of open source and the reality of capitalism are contradictory but somehow
[5210.70 --> 5217.42]  we have to mesh them right because the world we're in right now how um these issues i'm assuming with
[5218.14 --> 5223.58]  uh enzyme yeah people saying hey can't upgrade this and that have you reached out to
[5223.58 --> 5231.82]  that company not just those developers but like done some proactive outreach to criers the the squeaky
[5231.82 --> 5235.82]  wheels that i did actually but can't have because you don't you can't you haven't built it i've had
[5235.82 --> 5243.66]  conversations with three or four companies um i even had a conversation with you know one or two very
[5243.66 --> 5252.94]  large you know big big alphabet letter companies and like it's just never materialized um one you know i had
[5252.94 --> 5257.34]  a company who i i met with the manager and some of their engineers and we talked about what it would
[5257.34 --> 5263.90]  take and they decided that it would take about the same amount of time to migrate to rtl and so they
[5263.90 --> 5271.02]  just did that instead and i mean that's their decision to make but if it's the same amount of time
[5271.02 --> 5276.06]  they could have done it not had to change their test code and benefited everyone and i'm like sponsor
[5276.06 --> 5280.22]  where ask i guess i would have been happy to slap companies names on there like i'm happy to
[5280.22 --> 5285.90]  show appreciation and help market somebody that's helped me do something good um but it just never
[5285.90 --> 5289.82]  worked out yeah we may be thinking about sponsor we're slightly differently so this is a model
[5289.82 --> 5294.22]  wherein you're talking about like withholding a change yes yeah yeah it's so providing that only
[5294.22 --> 5299.18]  not to not for them to advertise but for them to gain it's like early access right but then when you
[5299.18 --> 5303.58]  reach a certain threshold of of sponsors overall you're just going to put it out to everybody no matter
[5303.58 --> 5308.54]  what yeah no it's kind of like a little bit of a middle ground totally and it works it works well at
[5308.54 --> 5314.38]  least for a few people but they tend to have more product oriented open source so definitely not for
[5314.38 --> 5318.30]  your transit dependencies i thought maybe with enzyme it would be a situation where if you have a hundred
[5318.30 --> 5322.38]  engineers like hey we want this it's like well that's worth money to somebody and i think it would
[5322.38 --> 5327.74]  be like i think enzyme would be a good fit for that model it's just that like unless i have the work
[5327.74 --> 5332.46]  complete no i get it you have to invest yeah which is not the easiest you can't always do that exactly
[5332.46 --> 5337.34]  yeah totally yeah but i appreciate the creativity i mean like you got to consider all an interesting idea
[5337.34 --> 5343.42]  yeah it's a way of going about it not all of your projects are going to be funded necessarily like
[5343.42 --> 5349.18]  right you know you look at an artist or a musician or a film you know certain you have one hit and that
[5349.18 --> 5353.50]  powers the rest of your things and so maybe you have one project that's letting you work on the other ones
[5353.50 --> 5361.66]  can you lay out your open source income streams like what they are sponsors open collective like
[5361.66 --> 5367.58]  how do you structure it how do you how does it come into your yeah so i have a sponsor for my personal
[5367.58 --> 5374.22]  account i have one for uh and then i have an open collective for two of the github orgs that i also
[5374.22 --> 5379.18]  have hooked up through open sponsor through github sponsors on uh through that open collective
[5379.74 --> 5387.42]  i'm on thanks.dev i'm on tidelift i'm on stackade.us um i think that's it but like i'm pretty much willing
[5387.42 --> 5393.42]  to sign up for anything that might bring money uh it's just you know the anything that requires a
[5393.42 --> 5399.26]  heavy marketing effort for me is something that has to pay out in turn and very few of the things
[5399.26 --> 5405.26]  have yeah um i would say tide lift and github sponsors and open collective and thanks.dev in
[5405.26 --> 5411.42]  that order have been the most like lucrative first huh yes by a large margin that's good good for you
[5411.42 --> 5417.50]  yeah i like their model of the dependencies of the dependencies because yeah all too often do you
[5417.50 --> 5424.22]  have a great as you mentioned influencer not saying that these people have been but like sean webpack
[5424.22 --> 5431.58]  etc like these things have been they've been great at um promoting the project and getting the you know
[5431.58 --> 5436.70]  getting the awareness but they're also sitting on top of the other shoulders of other folks that right
[5436.70 --> 5442.86]  it's not filtering too and there's there's there's not enough money even coming into webpack let's say
[5442.86 --> 5448.38]  for webpack to compensate its own developers and also to significantly compensate its entire debt
[5448.38 --> 5453.82]  graph if there was i would hope that they would do it but like there just isn't and i know that
[5453.82 --> 5457.82]  that's the case for babble that babble has barely to either i mean exactly i mean you're all sort of
[5457.82 --> 5462.94]  fighting for the same customer basically in a way exactly right yeah what a problem it's a hard problem
[5462.94 --> 5469.18]  to solve wow yeah well i'm happy to hear that you know 20 year old single jordan could at least do
[5469.18 --> 5473.50]  this so that means you're it's encouraging that's actually better than most people are doing right
[5473.50 --> 5477.10]  but a lot of us are out there getting our eight bucks a month from our sponsors and that's it exactly
[5477.10 --> 5483.18]  right but but it is worth noting that it takes such an outsized level of reach yes to get to that point
[5483.18 --> 5489.66]  right where like i could you know have a roommate in a studio apartment and like cover my food and my
[5489.66 --> 5495.82]  drinks for the week like you know it's it's better than most but it's and i'm grateful for it but it's
[5495.82 --> 5501.98]  still not anywhere close to sufficient like we need to be in a world where somebody providing public value
[5501.98 --> 5509.50]  like a public good is able to live their life without disruption and that's not where we are right now
[5509.50 --> 5515.66]  yeah what would you change about tie lift about get up sponsors what would you change about how
[5515.66 --> 5521.18]  because it's all about distribution and awareness and you're only one person right they have a company
[5521.18 --> 5527.34]  in both cases profit in both cases i assume tie lift profits um they have marketing they probably
[5527.34 --> 5532.62]  have marketing dollars they spend they do upstream they do a lot of outreach what would you change about
[5533.26 --> 5538.22]  i guess any of the things you use to make it better for you and for others honestly i think it's
[5538.22 --> 5542.94]  just a pipeline problem what i would change if i had a little regulatory magic wand is i would make the
[5542.94 --> 5550.14]  e the us and the eu uh require that profitable companies only profitable ones donate you know
[5550.14 --> 5555.98]  or contribute let's say one percent of their profit to their open source infrastructure period and you
[5555.98 --> 5561.18]  can do that with time or with money you know you can sponsor conferences and that counts like it'd be
[5561.18 --> 5566.30]  very liberally interpreted if something like that were to happen companies would just do it all over
[5566.30 --> 5570.86]  the world because it's simpler than you know trying to separate out the money and on top of that
[5570.86 --> 5576.06]  uh there would be so much money that companies like tide lift and thanks.dev and so on would
[5576.62 --> 5581.18]  would already be there to fill the gap and like provide that accountability you know the government
[5581.18 --> 5585.58]  would require a forum or something and like can help filter the money to the right folks i think that
[5585.58 --> 5590.62]  would be that would just solve this problem because like i said capitalism right we have capital and
[5590.62 --> 5596.62]  regulation and i think that and unless we can i can't come up with a big enough capital incentive
[5596.62 --> 5602.06]  that's convincing enough but regulation could do it profitable companies yeah so if your company
[5602.06 --> 5606.30]  doesn't make any money you're good as soon as you start making money every dollar you make a penny has
[5606.30 --> 5613.58]  to go towards open source there's a lot of very well known well used a lot of value even created by
[5613.58 --> 5618.14]  the company that doesn't make money they lose money absolutely and you could argue that that they
[5618.14 --> 5623.58]  might even make money off of that great one percent of that could also go sure right like it's
[5623.58 --> 5627.90]  i i'm not precluding them making money regulation challenging i see where you're going with that
[5627.90 --> 5632.94]  i think regulation magic wand yeah i know i know you did i'm hypothetical in this a little bit
[5633.66 --> 5637.50]  you might get into a world where it's like well we don't want to be profitable or we're not
[5637.50 --> 5641.82]  profitable you know and we're already in that world that's what companies do to try and ditch taxes
[5642.06 --> 5646.94]  and that's a yeah exactly that's why you know hbo shelves shows and and writes them off right oh i
[5646.94 --> 5653.42]  know isn't that the worst like completely finished yeah movies literally yeah just not released they could
[5653.42 --> 5658.46]  just release that on bit torrent for the world to have totally makes no sense they deep six it
[5659.18 --> 5664.46]  yeah and that's your only change regulation i think i mean obviously i would make many changes in the
[5664.46 --> 5668.70]  world if i had that kind of power but i think that as it relates specifically to the funding of open
[5668.70 --> 5674.38]  source i think that one change would be the most impactful could github or tidelift do more i guess
[5674.94 --> 5679.10]  always my sub question yeah always um and i think what could they do more well i think tide lifts
[5679.10 --> 5685.90]  the all they need to do is get more subscribers and that's a human problem a sales challenge right
[5685.90 --> 5691.90]  right um github is in a position where they can do a lot more but microsoft would have to be willing
[5691.90 --> 5697.18]  to pump a lot more money into it post acquisition than they seem to have been doing lately um
[5698.38 --> 5703.74]  you know yeah it's i i don't think for example i don't think github sponsors is really staffed right now
[5703.74 --> 5708.46]  inside github and i think that there's at least one person i think they might have one person but
[5708.46 --> 5712.70]  like i talked to her but there should be more than one there should be like looking for people
[5712.70 --> 5717.74]  20 people on that product right and i don't think there is so like a lot of things that github seem
[5717.74 --> 5723.42]  to be understaffed at the moment how does npm look in uh from my external view it seems wildly
[5723.42 --> 5728.22]  understaffed as well that's there's a lot of things they need to fix and the people working there
[5728.22 --> 5734.14]  who are doing great work are very overworked what a world man i know it stop talking i don't
[5734.14 --> 5739.10]  want to hear any more of this stuff you're starting to scare me all right well let's uh let's chill your
[5739.10 --> 5746.22]  your links now github sponsors how do they hit you up what do we do github.com slash what uh lj h a r b
[5746.22 --> 5752.86]  lj harb that's i'm that on everything lj harb if you use javascript i do probably use his code
[5752.86 --> 5760.14]  if you are in an organization that profits from that javascript maybe uh throw them a bone that's
[5760.14 --> 5767.26]  right type npm fund into your node code base join tide lift throw some money at thanks.dev i mean just
[5767.82 --> 5772.78]  pick one or more ways and try and get your company to contribute certainly do so yourself if you can but
[5772.78 --> 5777.26]  you know it's much more impactful to take your employer's money than yours so yeah yeah for sure
[5778.22 --> 5779.82]  thanks man yeah appreciate it thanks for having me
[5783.50 --> 5789.98]  okay so stick around if you are a plus plus subscriber if you are not a plus plus subscriber
[5789.98 --> 5797.98]  you can correct that by going to changelog.com slash plus plus it's better that's right it's better
[5797.98 --> 5804.78]  when you are a plus plus subscriber because you get bonuses you get no ads you get closer to that
[5804.78 --> 5812.70]  cool changelog medal but most of all more importantly you directly support us and we love that and we
[5812.70 --> 5819.66]  appreciate that so changelog.com slash plus plus there's a little bonus on here jared now we're in
[5819.66 --> 5825.82]  the hallway at our booth and we had some time where there's nobody else around so we're just like
[5825.82 --> 5831.74]  let's just uh let's just chat see what's going on and i think you can do it but again big thank you to
[5831.74 --> 5840.46]  todd lewis and team at all things open for working with us so closely every single year to make us a part of
[5840.46 --> 5848.78]  what they're doing and also for letting us host the panel on the impact of ai on developers you'll
[5848.78 --> 5854.54]  find that right here in this podcast feed so look for it if you want to listen to it big thanks to
[5854.54 --> 5861.42]  our friends at fastly our friends at fly our friends at typesense and also to breakmaster cylinder
[5861.42 --> 5869.10]  those beats are banging banging make sure you check out our albums on spotify search for
[5869.10 --> 5877.50]  changelog beats stream buy whatever we don't care just enjoy it okay until next time
[5877.50 --> 5882.14]  jackenc equal to jack the band on we have a lightning map we have boozer for esc Надеюсь
[5882.14 --> 5882.88]  grodare for your uwu
[5882.88 --> 5885.46]  Kurz Health focused for housing take care snowfall
[5885.46 --> 5887.98]  And that's how we know your boys with biolemica captain Mews
[5887.98 --> 5889.58]  in the valentine gill cock
[5889.58 --> 5893.28]  And the fishacAnuda Oriental
[5893.28 --> 5894.44]  The fishacAnuda keto
[5894.44 --> 5897.04]  And that's how we could naturally put our bears on here in the forging
[5897.04 --> 5898.46]  America in the the��대 selector
[5898.46 --> 5900.78]  The fishacAnuda the supermon passenger
[5900.78 --> 5901.02]  The fishacAnuda coars
[5901.02 --> 5902.12]  That's how they outcomes the bait
[5902.12 --> 5903.54]  The water and där
[5903.54 --> 5904.52]  The fishacAnuda
[5904.52 --> 5906.62]  The ti researching
[5906.62 --> 5916.84]  Game on.
