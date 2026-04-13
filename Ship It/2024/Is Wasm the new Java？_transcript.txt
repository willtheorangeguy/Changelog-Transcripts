[0.00 --> 13.86]  this is ship it with justin garrison and autumn nash a podcast about everything that happens
[13.86 --> 20.80]  after get push ship it is brought to you by fly.io the home of changelog.com
[20.80 --> 27.30]  launch your apps close to your users all around the world learn how at fly.io
[30.00 --> 56.28]  hello and welcome to ship it the podcast all about what happens after you get push i'm your host justin
[56.28 --> 60.92]  garrison and with me as always is autumn nash how's it going autumn good how are you how's your
[60.92 --> 68.44]  sunday going uh it's monday by the way it feels like a sunday we are recording on memorial day
[68.44 --> 73.44]  a day off for us in the united states but uh yeah it does feel like a sunday because tomorrow is back
[73.44 --> 80.48]  to work back to school so it's totally it's a mon sunday but that was a three-day weekend so fyi
[80.48 --> 86.68]  it's the only monday that doesn't feel like a monday yeah and it hasn't sucked oh but don't
[86.68 --> 90.98]  worry it sounds like a double tuesday it feels like a double tuesday tomorrow when you have double the
[90.98 --> 97.06]  email the people that were either out of the country don't have it off or just were deciding
[97.06 --> 104.08]  to catch up on a monday yeah you get to figure that one out so it'll be fun this is our 16th episode
[104.08 --> 108.16]  ever since the reboot of ship it's and we just wanted to talk to everyone let you know that we
[108.16 --> 112.10]  are adjusting the format a little bit thank you everyone for sending in feedback and for letting
[112.10 --> 116.18]  us know what you did and didn't like about the show and recommending topics all of those things
[116.18 --> 119.80]  have been awesome we've been reading all those emails but we are going to change up the format
[119.80 --> 124.88]  just a little bit to help the streamlining of episodes for us to record them um and also because
[124.88 --> 130.10]  we kept feeling like we were pushing people we are interviewing into smaller schedules either the uh
[130.10 --> 134.08]  the interview would go long and the episode was an hour and a half long or we were trying to tighten
[134.08 --> 138.04]  them up and say like oh we can't talk about that really cool thing that you do uh so let's just
[138.04 --> 142.32]  ignore it and then move on and so we don't want to do either of those things so we're actually
[142.32 --> 147.46]  going to cut out the beginning links of the week segment uh that we were doing and it's going to be
[147.46 --> 152.32]  part of our normal rotation for outro section so we're still going to have an outro uh which will be
[152.32 --> 158.12]  a variety of different things uh we've had lots of good feedback on uh those outros but we'll we'll
[158.12 --> 161.16]  mix in links of the week if there's something that autumn and i want to talk about or something
[161.16 --> 166.04]  that we found really interesting that will be our outro segment and and that's just what we're
[166.04 --> 171.44]  going to do also thanks for listening like we've been such cool listeners and like feedback on slack
[171.44 --> 177.38]  and twitter and all kind of blue sky yeah it's been awesome just seeing people really enjoying the show
[177.38 --> 181.68]  come back and listening to the topics and then just connecting with different technologies and what
[181.68 --> 185.74]  people are doing and that's just fun to see like we're kind of introducing people to stuff and i love
[185.74 --> 189.54]  doing that because we're getting introduced to it and then we get to share and then when people are
[189.54 --> 194.04]  so excited about things it's so much fun when like they're like i totally saw that video and you're just
[194.04 --> 201.38]  like exactly yeah so this week on the show we have danielle lancashire who is a principal engineer
[201.38 --> 209.06]  at fermion and fermion is a web assembly cloud hosting platform that you can run your web assembly code
[209.06 --> 215.90]  and they will run it for you and so we get to dive into how that works what is web assembly and how the
[215.90 --> 222.30]  back end of fermion works and how kind of you can run this stuff in in either the fermion environment
[222.30 --> 228.26]  or even uh what they ship as a like a kubernetes uh interface for it so um it has a lot of variety
[228.26 --> 232.98]  there but if you've never used web assembly before never tried it aren't familiar with it don't worry
[232.98 --> 238.90]  the outro we also have you covered we're going to go over the wta outro of what the acronym and explain
[238.90 --> 243.46]  some of the stuff because there's a lot of terms and stuff in the interview we try to explain those
[243.46 --> 247.26]  as well but we're going to do them a little bit more in the outro just as a review so we can make sure
[247.26 --> 251.80]  everyone's on the same page we want to be inclusive and help anyone even if you don't know the tech
[251.80 --> 256.98]  or you're familiar with it i had no idea before we were doing research for this episode i had no idea
[256.98 --> 263.30]  what web assembly was at all yeah it's pretty new i found out it has just as many awful acronyms as
[263.30 --> 268.44]  kubernetes and all of your crazy stuff yeah it's just web assembly's acronyms are usually in english
[268.44 --> 273.28]  and that is a benefit for web assembly not like let's do everything in greek and then take all the
[273.28 --> 280.78]  vowels yeah yeah trying to make uh abbreviations and acronyms out of greek words is a little bit
[280.78 --> 286.14]  more difficult uh to wrap your head around so in kubernetes defense all the names sound cool you're
[286.14 --> 293.40]  just like but what are we talking about though for sure what is an istio i don't know but it's like
[293.40 --> 299.82]  it sounds cool like it's just not giving you a lot of information but you know yeah uh one thing that
[299.82 --> 303.68]  is nice is like the terms kind of line like kubernetes as a helmsman you're like okay what
[303.68 --> 307.74]  does that mean like well docker is ships and there's containers like okay like you drive it
[307.74 --> 312.66]  all right i see it uh but yeah like that doesn't always line up there's always some gaps there it is
[312.66 --> 316.96]  nice that it's themed it's like one of those like pinterest birthday parties you throw your kids but
[316.96 --> 322.12]  like with technology like got a theme going you could stick to it it's cool to make stickers with
[322.12 --> 327.16]  so let's jump into the interview with danielle and then we will come back for the outro and
[327.16 --> 351.28]  explain some more acronyms all around web 7 what's up friends this episode is brought to you by our
[351.28 --> 357.40]  friends at neon on demand scalability bottomless storage and database branching and i'm here with
[357.40 --> 364.28]  nakita shamganov co-founder and ceo of neon so nakita imagine you are a tour guide give me a tour
[364.28 --> 371.08]  through the world of neon so let's look at a modern developer as people say never bet against javascript
[371.08 --> 377.08]  so more than 50 probability this person is writing javascript and typescript using react
[377.08 --> 386.10]  next js deploying their code on a platform like purcell and really care about design so working
[386.10 --> 392.92]  with figma working with a local designer or maybe starting to work with an ai designer and using
[392.92 --> 399.92]  technology like purcell just shipped called v0 and then like you got to store data somewhere so
[399.92 --> 405.96]  you go to neon or use purcell postgres which is powered by neon you push a button and now you're able
[405.96 --> 412.82]  to write and read from neon and then that kind of just works out of the box the majority of your time
[412.82 --> 419.20]  you spend crafting your application crafting the front end and then the database is just kind of like
[419.20 --> 424.08]  it's just kind of there and just kind of works and you don't think too much about it and when you run
[424.08 --> 431.64]  previews when you run next versions of your software you can send your collaborators your other engineers on
[431.64 --> 437.70]  your team or your product managers or designers a version of your app the version of the future that you want to
[437.70 --> 444.50]  debate if you want to comment on and it's fully sandboxed you know from your front end to back end to the database
[444.50 --> 450.64]  that's like a good part of this world the world is obviously much bigger than just building front end apps
[450.64 --> 458.64]  there's also back end apps there are python apps there are java apps and all of those things we're perfecting the world for the world that i just described
[458.64 --> 466.12]  and we think that the rest of the world will follow uh and the rest of the world is java apps rast apps back
[466.12 --> 474.64]  and that's queues scheduling aws lambda kubernetes containers again the tech world of the back end is just
[474.64 --> 481.78]  enormous but i think perfecting this first world that i described will create a standard in developer
[481.78 --> 487.10]  experience that the rest of the developer world will just follow so you have versell postgres powered by neon
[487.10 --> 493.18]  you've got neon as an integration to versell you've got neon out there at neon.tech as self-serve where
[493.18 --> 499.20]  anybody could just go and sign up and start up right now you're optimizing for this new standard but what's
[499.20 --> 503.82]  the response been like what's the community saying what's the community's response we are lately
[503.82 --> 510.76]  onboarding close to 2500 databases a day that's more than one database a minute of somebody in the world
[510.76 --> 516.94]  coming to neon either directly or through the help of our partners and they're able to experience
[516.94 --> 521.80]  what it feels like to program against database that looks like a url and the program against
[521.80 --> 527.00]  database that can support branching and be like a good buddy for you in the in the software development
[527.00 --> 533.32]  lifecycle so that's exciting and while that's that's exciting the urgency at me and is currently is
[533.32 --> 539.26]  unparalleled there you go if you want to experience the future go to neon.tech on demand scalability
[539.26 --> 544.94]  bottomless storage database branching everything you want for the postgres of the future once again
[544.94 --> 569.98]  neon.tech hello and welcome to the podcast danielle lancashire a principal engineer at fermion
[569.98 --> 574.80]  danielle welcome uh tell us about yourself hi uh you'd think i'd be prepared for these things
[574.80 --> 582.84]  ever but i never am i uh um by heart a photographer and then by trade uh software engineer at fermion
[582.84 --> 590.04]  where i work a lot on bringing web assembly to the cloud which is a sort of interesting concept if you
[590.04 --> 595.78]  think about it a lot of people think web assembly and hear browser but it turns out having a like
[595.78 --> 601.26]  portable binary format you can run anywhere is kind of awesome and i want to dive really deep onto
[601.26 --> 606.86]  to to web assembly and wasm in general uh because like portable binaries um we've kind of like an elf
[606.86 --> 612.08]  binary is pretty portable right like how is wasm different and what does it do i mean an elf binary
[612.08 --> 618.00]  is portable across like some number of like linux distributions but the second you want to talk
[618.00 --> 626.48]  about windows or mac os or like moving to you know arm or risk 5 or wherever else well not so portable
[626.48 --> 632.00]  anymore unless you you know do apple things and rosetta everything the struggle is real
[632.00 --> 641.96]  and so by building to a like portable intermediary format like web assembly uh you can then run those
[641.96 --> 649.36]  on literally anything uh so i have a demo cluster where i take the same web assembly application
[649.36 --> 658.38]  and i have a kubernetes cluster that's risk 5 um 64 and you know amd 64 and the same thing just runs
[658.38 --> 664.82]  across all of them with no changes and that is the point where a lot of people go oh wait i didn't have
[664.82 --> 669.60]  to spend like six months supporting different architectures and testing a bunch of like really
[669.60 --> 675.74]  cursed dependencies and that's pretty awesome and how does that actually get accomplished right because
[675.74 --> 680.34]  like you have uh containers which can be portable and you just build them twice for the architectures
[680.34 --> 688.50]  and then at the runtime layer says oh i need the arm or the risk or the amd whatever version i need as
[688.50 --> 692.60]  the executable give me that one but that's like build time you build them multiple times and wasm is
[692.60 --> 699.20]  different right yeah with web assembly you build once and then it's the job of the runtime to either
[699.20 --> 704.58]  build a specialized version for your platform or just interpret the web assembly the same way that you
[704.58 --> 710.30]  know node interprets javascript although i think it also does some pre-compilation and stuff whatever too
[710.30 --> 717.28]  because you know nothing is ever truly interpreted these days uh so you either uh like with wasm time
[717.28 --> 723.74]  which is what we use there's a thing called crane lift and what crane lift does is build optimized local
[723.74 --> 731.26]  native representations at instantiation time or lazily and jitter but after the first request everything is
[731.26 --> 736.34]  pretty fast and that sounds similar to what we had in the past was something like python right like python
[736.34 --> 741.92]  so an interpreted language it's like hey the runtime handles the architecture and my python code doesn't
[741.92 --> 748.46]  have to change to run on different architectures and then at at runtime it does some compilation for my
[748.46 --> 755.40]  architecture to run exactly with web assembly you end up being a little bit lower overhead if you compile c to
[755.40 --> 762.36]  web assembly i think the most recent set of benchmarks i saw was like a few percentage points slower than
[762.36 --> 769.08]  running a native binary but the other joy of that is you can do that for any programming language that can
[769.08 --> 778.94]  eventually support web assembly so like be that python ruby swift javascript rust go you can truly do this
[778.94 --> 786.24]  like polyglot thing and when you bring in things like the component model uh which is um one of the
[786.24 --> 793.48]  sort of more recent evolutions of uh wasi you can even have different components of your application be
[793.48 --> 799.40]  built in written in different languages for example if you have a tooling team that writes a bunch of
[799.40 --> 806.42]  stuff for doing observability or interacting with different apis or whatever you can call those from
[806.42 --> 812.10]  any language that your team is writing software in can you take a step back and just describe wasi for us to the
[812.10 --> 822.42]  interface oh yeah i should probably do that uh wasi is bringing io to web assembly basically uh so web assembly by
[822.42 --> 829.90]  itself can't really talk to the outside world it's just an executable format and you know you run in the browser so you
[829.90 --> 836.20]  might extend some like javascript browser apis into a web assembly binary but it's mostly like pure
[836.20 --> 842.32]  hot something and get something out not much else and the runtime is responsible for like moving that
[842.32 --> 849.98]  data between right yeah and wasi takes you know the web assembly format and brings a standard set of
[849.98 --> 857.88]  interfaces for doing a lot of the stuff that software needs to do sort of like you know posix apis are to
[857.88 --> 865.50]  everything else but it doesn't quite copy those because we bring in a capability-based security model
[865.50 --> 871.84]  and so you can say that like at runtime this wasi application can you know talk to these set of
[871.84 --> 878.04]  files and these set of files only or make outbound requests to these specific ip addresses is that
[878.04 --> 883.86]  enforced at the in the runtime yeah okay so the runtime knows hey you have this rule set that you're
[883.86 --> 888.14]  allowed to do and and i'm only going to allow you to do those things where it's like a again an elf
[888.14 --> 894.24]  binary or python scripts like you i basically have the whole machine uh unless i'm containerized some
[894.24 --> 899.92]  other way right where i have to isolate my space with a different mechanism yeah all web assembly
[899.92 --> 905.00]  stuff is pretty much default than i and you have to sort of incrementally give it the things you want
[905.00 --> 911.44]  it to do and that all happens through a standardized set of interfaces that is wasi that's a bunch of
[911.44 --> 917.12]  people coming together and figuring out sort of the right way to do things for both from a security
[917.12 --> 923.52]  perspective but also like efficiency and standardization of like what does it mean to talk to a database
[923.52 --> 929.80]  right wasi stands for the web assembly system interface right yeah that's that like spec that
[929.80 --> 933.72]  says hey these are the things you do if you need to open a socket to listen on a port or something
[933.72 --> 939.50]  you do that through the wasi interface yeah exactly that's interesting i never heard about the
[939.50 --> 944.38]  extensions to be able to write multiple like components of the app in different languages to
[944.38 --> 950.92]  kind of glue those together as as and at that point it compiles down to a single wasm binary
[950.92 --> 957.16]  it can compile down to a single wasm binary or you can have those multiple binaries sort of like
[957.16 --> 963.78]  composed together so they call each other and sort of expose interfaces that the other thing can talk to
[963.78 --> 970.92]  kind of like a library but while being language agnostic the language agnosticism of its uh limits what you
[970.92 --> 976.02]  could do right because it's like we have this runtime that's default deny we have javascript and
[976.02 --> 980.28]  python in the wild wild west of like what can compile into this but there has to be like some subset of
[980.28 --> 985.04]  like this just doesn't work in web assembly right because like those two things aren't the same
[985.04 --> 990.84]  there's definitely a lot of things that you can't just take as they are today and run within wasi
[990.84 --> 997.64]  like wasi doesn't yet have a standardized threading model it's something that's being actively worked on
[997.64 --> 1004.58]  this year uh was like a really big topic at wasmio a few months ago and there's sort of a lot of stuff
[1004.58 --> 1010.42]  that's like early but coming but there's not a lot of stuff that you couldn't theoretically do
[1010.42 --> 1016.34]  now what software are you responsible for you you work at fermion and and you have like this wasm cloud
[1016.34 --> 1022.62]  that you offer what do you what do you run or what's what software are you building there i've worked on
[1022.62 --> 1029.02]  a big mix of both our cloud and also the bringing web assembly to kubernetes stuff through spin cube a lot
[1029.02 --> 1036.72]  of that is sort of mine and people i work with domain which is a mix of um you know for kubernetes
[1036.72 --> 1044.30]  things we built out a container d shim uh so container d has pluggable runtime environments
[1044.30 --> 1052.66]  well like execution things called shims and there's a project called uh run wasi that exists to let you
[1052.66 --> 1058.58]  write shims that run web assembly code and so we have one of those for running spin applications which is
[1058.58 --> 1066.18]  fermion's like web assembly i guess framework is kind of the right word it's like kind of a runtime but
[1066.18 --> 1071.42]  also kind of a framework and like the community hasn't really standardized on language for that yet
[1071.42 --> 1079.70]  and then sort of an operate why would i want that why why do i want to run web assembly binaries inside
[1079.70 --> 1085.28]  of kubernetes cluster i have containers and i can i can put those languages in a container and run them
[1085.28 --> 1090.48]  and and the runtime can also handle architecture differences right because i could build it twice
[1090.48 --> 1095.78]  and then i can pull it down and run it on arm versus amd whatever what other benefits does
[1095.78 --> 1104.56]  a web assembly binary have in this case so one of the big ones is density so when a web assembly
[1104.56 --> 1112.20]  application is doing nothing it is actually doing nothing it's a bit of memory and effectively no cpu
[1112.20 --> 1119.92]  that's pretty different to a lot of other sort of serverless programming models uh where like you
[1119.92 --> 1125.40]  potentially need to be running fairly heavyweight software and potentially two applications to have
[1125.40 --> 1132.44]  that programming model in some cases that's like 10 plus x density improvements which if you're worrying
[1132.44 --> 1139.56]  about you know cloud cost or managing your like cloud infrastructure that can make really big
[1139.56 --> 1146.28]  differences especially at scale but beyond that the security model and being able to cleanly express
[1146.28 --> 1152.80]  what you want your applications to do gives you a lot of really nice benefits partially for things like
[1152.80 --> 1157.50]  multi-tenancy you know especially if you ever need to run like an untrusted application in your
[1157.50 --> 1164.70]  environment i've used in the past uh like clubflare workers uh is is web assembly based and they have
[1164.70 --> 1168.40]  some really good blog posts on like how they would speed that up and why that why they use it
[1168.40 --> 1173.30]  um and i know there's other uh web assembly companies that use uh more i don't say lighter
[1173.30 --> 1179.12]  weight but different scheduling engines like nomad to be able to speed up execution time for scheduling
[1179.12 --> 1183.66]  because that's like a built-in stack it's it's less flexible but also faster um than kubernetes in
[1183.66 --> 1189.44]  a lot of ways all those things like build layers of where do i want to control this thing right because
[1189.44 --> 1194.04]  i can control again at the container layer i can say you're not allowed to talk to this other thing or
[1194.04 --> 1199.68]  you're not allowed to run this kernel argument or permissions whatever and that the web assembly
[1199.68 --> 1204.26]  layer i can do it at the application and say hey the runtime will enforce i can't read this file
[1204.26 --> 1209.02]  and then at the cloud layer right if i'm running all this in an aws account like i have i am on top of
[1209.02 --> 1213.20]  that that says you know somewhere in there i have some linux permissions all this like it seems like we
[1213.20 --> 1218.10]  like security is good in layers but at some point you have to pick the layer that you want to operate
[1218.10 --> 1223.08]  in and i guess the more portable you need to be the closer you want that to be the application right
[1223.08 --> 1228.24]  yeah you know in our cloud we actually use nomad okay i'm a little bit biased i'm a former nomad
[1228.24 --> 1233.34]  maintainer i'm you know now also a kubernetes maintainer but like nomad has a special place in
[1233.34 --> 1240.14]  my heart yeah but the sort of security and layers and the application layer security is really nice when
[1240.14 --> 1247.56]  you're building a platform like fermion cloud or like something like lambda or whatever because we run
[1247.56 --> 1252.22]  thousands of applications on every node like looking at that from like the kubernetes world
[1252.22 --> 1259.32]  it's like what what are you doing like how and we can do that partially because of the guarantees we
[1259.32 --> 1266.76]  get from that execution layer because we can map you know you deployed this application as you know
[1266.76 --> 1273.04]  team foo and you only have access to these things and you've declared that this application should be
[1273.04 --> 1279.62]  able to access you know this database or this key value store whatever and then at a runtime layer we can
[1279.62 --> 1285.94]  guarantee that they are the only things you can talk to which is pretty revolutionary in a lot of ways
[1285.94 --> 1293.04]  like i worked at circle ci when we moved from doing a lot of stuff in like you know pre-configured lxc
[1293.04 --> 1301.12]  containers to docker and bring your own container and the amount of work we had to do to isolate
[1301.12 --> 1308.20]  anything sensibly was like monumental in comparison to what we had to do for fermion cloud and trying to like
[1308.20 --> 1313.76]  you know understand when anything needed was basically impossible and now it's your application self describes
[1313.76 --> 1320.22]  what it needs like it tells us that it needs this thing and we can go yes you can have this thing and we can
[1320.22 --> 1327.18]  guarantee it deploy time that your application has access to the things it needs to or doesn't and bring that
[1327.18 --> 1332.86]  conversation much earlier in the loop as opposed to doing you know like runtime profiling to understand
[1332.86 --> 1338.60]  what syscall something is making right and i think that's just that approach of starting with the default
[1338.60 --> 1345.68]  deny and building up is so much easier than i mean not easier but it's a different approach than what we
[1345.68 --> 1350.26]  have with containers where we're taking all of the kernel calls and we're dividing them and we have all these
[1350.26 --> 1355.34]  namespaces that we say hey we we take a big machine with a single kernel and then make it smaller
[1355.34 --> 1361.00]  into smaller chunks and then how do we how do we divvy all that up and if you at some point you want the
[1361.00 --> 1367.72]  more secure thing and so you're going to say hey i just need these 10 20 30 things versus i don't need
[1367.72 --> 1374.48]  these hundreds of things and how you approach those things are very different can you walk through if i
[1374.48 --> 1381.74]  create a wasm binary what is the process for me going from the spin command to an executable inside of
[1381.74 --> 1387.12]  fermion like i can call it and i get data back from it like what are all the layers and steps there
[1387.12 --> 1391.80]  spin cloud deploy but i mean like what's the what's the stack like i know like the experience is great
[1391.80 --> 1395.94]  like the experience is very much like hey you just hid like a hundred different things from me
[1395.94 --> 1405.10]  oh yeah it's an adventure so we have a front-end application that's written in c-sharp of all things
[1405.10 --> 1412.84]  which has been interesting to relearn interesting so that's all like what i call front-end monolith
[1412.84 --> 1419.48]  it's where it's the api service that anyone using fermion cloud interacts with and is also what serves
[1419.48 --> 1427.72]  our ui then there's uh what i lovingly call the back-end monolith and that's uh like relatively
[1427.72 --> 1433.70]  standard go service that mostly just talks gropc and that is basically the cloud control plane
[1433.70 --> 1439.32]  and that's what goes and you know when the front-end app receives the request to deploy
[1439.32 --> 1446.08]  the application uh make sure it's all stored in an oci registry and you know when all of that stuff is
[1446.08 --> 1452.78]  done it goes ahead and gives the sort of back-end monolith the manifest after you know sort of
[1452.78 --> 1459.74]  validating permissions and stuff is that manifest a like a nomad job or is that it's a custom thing
[1459.74 --> 1466.62]  that manifest is a rendered version of some tumble okay it's a data structure that kind of goes you
[1466.62 --> 1473.80]  want these key value stores and they're bound to these names for this application and you want like
[1473.80 --> 1480.28]  this database and you should respond to things that this address like that kind of stuff then the
[1480.28 --> 1486.72]  back-end monolith goes and runs a nomad job that will go and deploy your web assembly app on some
[1486.72 --> 1492.04]  subset of the nodes and that goes and does the you know sort of pre-compilation step getting everything
[1492.04 --> 1498.36]  set up and also goes and like make sure the databases that you wanted uh exist and make sure
[1498.36 --> 1503.80]  that your like applications token has access to them and that sort of all gets handled in the runtime
[1503.80 --> 1509.28]  layer so your application doesn't know that there's an authentication for example handle that outside
[1509.28 --> 1513.84]  the app so i don't have to deal with it as a developer yeah the idea is like you should focus on
[1513.84 --> 1519.82]  writing code and it shouldn't matter what is backing any of those things which is a programming model
[1519.82 --> 1525.20]  that a lot of people really love and we've had it repeatedly sort of happen over the years you know
[1525.20 --> 1531.96]  like especially when uh sort of heroku took the world by storm and did a lot of stuff for you but left you
[1531.96 --> 1538.02]  with a lot of sort of vendor lock-in the joys of web assembly and standardizing on a bunch of these
[1538.02 --> 1542.88]  interfaces is that you can get that programming model without necessarily being tied into a platform
[1542.88 --> 1548.36]  forever because you know the same thing you've run on your laptop when you type spin up and you know
[1548.36 --> 1555.36]  by default binds a lot of things to being in sqlite but will also let you talk to cosmos db or dynamo db or
[1555.36 --> 1564.76]  whatever it is works the same way in fermion cloud as it does in anywhere else that layer of of abstracting
[1564.76 --> 1570.42]  what i'm talking to happens at the runtime right so like the runtime shim is saying like oh you wanted a
[1570.42 --> 1576.80]  key value store i give you a key value store you don't care right exactly then uh the rest of the
[1576.80 --> 1583.88]  cloud rundown as it is uh we have a multi-tenant key value store that's uh actually backed by postgres
[1583.88 --> 1591.76]  postgres runs the world oh yeah postgres i love like postgres you can make it do anything if you're
[1591.76 --> 1597.30]  willing to be cursed enough the way that you held your chest with postgres like we're gonna be like
[1597.30 --> 1604.92]  just we're right here like it's the best it deals with all the pesky persistence things and all we
[1604.92 --> 1610.52]  have to do is give it a sensible api it's so underrated i think because it's not the cool hip
[1610.52 --> 1616.14]  thing but it's crazy how many things run on postgres or how other cool databases you don't want your
[1616.14 --> 1621.86]  database to be cool that should be the most boring piece of your stack but people always want the
[1621.86 --> 1627.34]  newest coolest thing in tech but it's funny because those newest coolest things usually are on postgres
[1627.34 --> 1635.16]  anyway my personal feeling about infrastructure is it should aim to be as boring as physically possible
[1635.16 --> 1642.00]  can all of tech adopt that because it would make their lives so much easier like simple boring
[1642.00 --> 1650.64]  tested things like and then please document it like our tech stack is you see two instances running in an
[1650.64 --> 1658.00]  auto scaling group nomad console vault and like the shiniest newest thing we have is traffic
[1658.00 --> 1664.40]  that fancy load balancer there you got a reverse proxy that's like hey we got and i guess that has a
[1664.40 --> 1669.68]  lot of integrations for like where it routes the traffic right it's just like oh this is multi-tenant
[1669.68 --> 1676.98]  routing for that right yeah traffic is basically there because uh it can talk to console it has like
[1676.98 --> 1683.04]  reasonably sensible routing rules that it can derive from console and it can generate tls certificates
[1683.04 --> 1688.90]  and then there's you know postgres and sqs because like sqs is the best service that amazon have ever
[1688.90 --> 1696.34]  released and nothing comes close to it someone recently described uh event bridge as sqs with a hat
[1696.34 --> 1703.86]  and and i was just i was like yeah that that sounds so accurate this is uh i love it you know it's funny
[1703.86 --> 1709.46]  though that's gonna sound weird but like in fashion right like even the most expensive things are
[1709.46 --> 1716.94]  usually simple right like they're either good quality simple or almost like weirdly like junky
[1716.94 --> 1721.88]  and simple and expensive you know kind of like what we were talking about earlier like when people buy
[1721.88 --> 1726.84]  like super expensive stuff in seattle to like go hiking you know and then they wear expensive hiking
[1726.84 --> 1733.18]  stuff everywhere so it's funny like i think sometimes the best stuff in tech and like fancy stuff in like
[1733.18 --> 1738.46]  fashion in a lot of places like you almost pay more for simplicity because it's it sticks around
[1738.46 --> 1745.06]  longer you know oh yeah like i also just love how stable this is like i've been focusing a lot on the
[1745.06 --> 1751.22]  kubernetes things rather than the cloud uh for a while and so the last time i meaningfully touched
[1751.22 --> 1759.40]  our cloud infrastructure was february and it just keeps working and now i've said that there's going
[1759.40 --> 1766.90]  to be an outage just because you said this podcast but like that's fine because if i only have to care
[1766.90 --> 1773.14]  once every few months i'm fine with it occasionally being a problem not just that but if you build it
[1773.14 --> 1777.62]  like with simplicity it's not hard well i mean i'm not going to say it's not hard but it's so much
[1777.62 --> 1783.32]  easier to debug when it's not a million fancy things that are not like if you're using something that's
[1783.32 --> 1788.12]  been around for a while and used a lot at least somebody else has come into that problem and someone on
[1788.12 --> 1795.04]  stack overflow is complaining about it and can give you a couple ideas how to fix it yeah like our um
[1795.04 --> 1801.00]  biggest single node scaling bottleneck in the cloud is that like because we health check applications
[1801.00 --> 1808.60]  relatively frequently uh console starts chewing a lot of cpu because if there's more than about 8 000
[1808.60 --> 1815.66]  applications on every node it starts consuming about four cpu cores just to do health checks it's like
[1815.66 --> 1821.58]  okay we know that's a problem we could eventually fix it how do you do health checks for 8 000
[1821.58 --> 1826.34]  applications on a single node uh from console like because they're all they're not long-running
[1826.34 --> 1830.82]  processes right like these are all essentially functions so you have to start them to help check
[1830.82 --> 1836.06]  them right yeah so you're just constantly like starting and stopping all of these workloads on a
[1836.06 --> 1842.98]  single node and saying like yep you're good still yep how do you do that efficiently though i mean
[1842.98 --> 1848.02]  partially because like running web assembly stuff is relatively efficient to begin with
[1848.02 --> 1854.08]  it takes less than a millisecond for a web assembly application to start it's essentially forking a
[1854.08 --> 1858.30]  process right because like the runtime's there it's always running and we have this binary that it's
[1858.30 --> 1863.12]  just going to like execute and so we're like oh fork the process you can kill it right i mean
[1863.12 --> 1869.90]  because a lot of this happens within tokyo which is a rust equivalent of like go routines you know
[1869.90 --> 1874.60]  it's a lot of green threads more than anything else we don't even need to fall you don't even yeah
[1874.60 --> 1881.98]  it's not even a four fork okay yeah it's kind of awesome the biggest bottleneck is um for that part
[1881.98 --> 1888.50]  in particular is just disk io because a bunch of stuff is kept and mapped uh if it actually got like
[1888.50 --> 1893.08]  pushed from memory then we have to reread it from disk yeah that takes a long time when
[1893.08 --> 1899.58]  when you're used to having something in memory yeah it takes like a few hundred nanoseconds no big
[1899.58 --> 1905.70]  deal what are you doing in the kubernetes side because you say you mainly deal with both and like your
[1905.70 --> 1912.94]  infrastructure for the cloud portion is is a known set of interactions with ec2 instances and some
[1912.94 --> 1917.92]  services but what are you building and doing on the kubernetes side i'm working on two things on the
[1917.92 --> 1925.84]  kubernetes side one is spin cube which is you know open source uh runs every uh application in a pod
[1925.84 --> 1930.64]  sort of gives you you know the things you're comfortable with but also a bit of something new
[1930.64 --> 1936.88]  but the other thing that i'm working on is basically what we call fermion platform for kubernetes
[1936.88 --> 1942.54]  which is taking a lot of the ways we run things in the cloud and moving them into kubernetes
[1942.54 --> 1948.40]  which has its like own set of trade-offs because rather than running every application in a pod
[1948.40 --> 1954.64]  we run one pod per node which changes a lot of the sort of kubernetes networking model
[1954.64 --> 1961.52]  i spent a lot of time this week uh having to very quickly like learn the endpoint slices api
[1961.52 --> 1965.78]  and how like all of that should work if you're running it yourself that was my first thought was
[1965.78 --> 1970.56]  like when you say you run thousands of applications per node and you know like the trade-offs there of
[1970.56 --> 1975.20]  architecture of like kubernetes typically requires one ip address per pod and i'm like you're gonna
[1975.20 --> 1979.30]  run out of ip addresses real quick like that's just not going to happen and so now you're taking that
[1979.30 --> 1984.44]  you're saying hey you know what like we can't do one application or one ip address per per web
[1984.44 --> 1990.72]  assembly application because it doesn't need an ip just the runtime needs the ip right uh yeah exactly
[1990.72 --> 1995.92]  and so at that point you take your runtime and shove it in a pod and then all of the applications
[1995.92 --> 2001.52]  that run under that are all under one ip address but it routes and does all the stuff to say like
[2001.52 --> 2006.72]  hey we're just going to fork or or run these threads running these executables inside of this
[2006.72 --> 2012.24]  one container and now if i'm debugging it from a kubernetes admin perspective i say hey i want to get
[2012.24 --> 2017.16]  my pod but that's just a runtime and i say i want to get my application i need to go a layer deeper than
[2017.16 --> 2026.48]  that exactly uh so like my prototype for this runs uh 3 000 apps on every node with basically zero
[2026.48 --> 2034.30]  noticeable overhead so at the networking layer that still means making a service for every application
[2034.30 --> 2040.08]  but an application might be multiple web assembly components because you know you might want like a
[2040.08 --> 2045.50]  different component per like set of roots or something in a http application depending on how you want to
[2045.50 --> 2053.12]  architect your application so we create a service per application and then we bind the runtimes that
[2053.12 --> 2057.54]  are running that application to the service when the application is ready and those are just pods
[2057.54 --> 2062.22]  behind a service in a kubernetes case this is like i have a service and that routes to pods and then the
[2062.22 --> 2068.48]  runtime itself says oh i was called on this path or this host name let me start that application for you
[2068.48 --> 2075.16]  exactly and it works surprisingly well it's one of those things where you know like you think something's
[2075.16 --> 2082.36]  gonna work but then you try it and it works better than you expected it to and you're surprised yeah
[2082.36 --> 2090.90]  i mean you know i i generally sometimes have some self-confidence issues so like when like this like
[2090.90 --> 2097.40]  idea that i thought was vaguely cursed which is can we put our cloud in a box turns out the answer is yes
[2097.40 --> 2103.08]  and why why put your cloud in a box in a kubernetes box when you're doing everything with ec2 and nomad
[2103.08 --> 2110.60]  now it turns out a lot of people really like the programming model of serverless but between sort
[2110.60 --> 2118.66]  of like potential vendor issues cost whatever else means that they're looking for something else
[2118.66 --> 2127.00]  and web assembly in my opinion is basically what serverless should be you completely separate away
[2127.00 --> 2132.64]  the runtime from the application and so like you don't need your application to bind to a socket
[2132.64 --> 2139.34]  which you still have in a lot of you know other serverless environments combine that with web
[2139.34 --> 2145.64]  assemblies you know security capabilities and the fact that it actually does scale to effectively zero
[2145.64 --> 2151.62]  you get this sort of perfect coupling of infrastructure that can support the programming model
[2151.62 --> 2156.58]  whereas before we had a programming model we were shoehorning into infrastructure that couldn't
[2156.58 --> 2161.68]  really handle it and that meant that you know we were paying huge startup costs if you wanted to run
[2161.68 --> 2169.06]  anything in lambda or other similar stuff because you've got to go fetch a container start a vm launch
[2169.06 --> 2175.78]  the thing and then set up all your network pathways and that's in response to a request like i never
[2175.78 --> 2181.24]  understood it i was like i like the idea of serverless but i could never get behind ever
[2181.24 --> 2186.76]  shipping something in a serverless way there's just too many drawbacks there's a lot of network
[2186.76 --> 2193.08]  and infrastructure overhead to take some data and send it back and and like you mentioned you know
[2193.08 --> 2198.60]  like a container or a zip or whatever how it's however we're packaged is probably larger than you need
[2198.60 --> 2204.92]  for your application piece of it the runtime being part of that as well if i have a python lambda versus
[2204.92 --> 2211.16]  java lambda like i have to have that runtime as part of it's versus compiling wasm into like
[2211.16 --> 2216.36]  a single binary format that can all be understood from the different languages but yeah and also
[2216.36 --> 2222.60]  like the vm side of it right you're like we have lambda has fargate that runs of creates a vm and then
[2222.60 --> 2228.52]  network and maybe a container on top of that and and how do you how you isolate all those things is
[2228.52 --> 2233.88]  is very slow when you actually look at all the components involved how would you describe and i i
[2233.88 --> 2237.72]  wanted to bring this conversation this way because we're almost out of time but i wanted to get autumn's
[2237.72 --> 2242.84]  like how how is web assembly different than java because i feel like some of the promises that i
[2242.84 --> 2250.12]  hear over and over again in the web assembly world have been what i heard 20 years ago in the java world
[2250.12 --> 2256.52]  and it was like hey write once run anywhere um we have this vm that will handle all of that like
[2256.52 --> 2263.32]  machine architectures and stuff under the hood and all of that stuff became either bloated or slow or
[2263.32 --> 2266.92]  people didn't like it went out of style but there's still like java and postgres still run the world
[2266.92 --> 2271.40]  and that's still like very much a thing i'd also like to just put it out there that java's got
[2271.40 --> 2276.52]  considerably faster just want to put that out there well if anyone can upgrade from java 12
[2276.52 --> 2282.60]  so like everyone's still it's eight and i mean i think like the world will like blow up before it
[2282.60 --> 2288.52]  fully dies but that's not the point justin i was like i remember running java i don't like four or
[2288.52 --> 2292.68]  five or something like that and like we had these tomcat absolutely like hey if but i mean java's also
[2292.68 --> 2297.64]  done a lot like they've like increased how you're going to release every six months so
[2297.64 --> 2303.64]  that problem does not continue happening you know smaller releases smaller jumps but honestly i've
[2303.64 --> 2308.52]  never used web assembly so i do not have the context to compare the two well that's why i was curious i
[2308.52 --> 2312.84]  wanted to know either autumn or danielle like if there's like if this promise keeps repeating itself
[2312.84 --> 2317.80]  like is is web assembly the new java it's not kind of just like tech in general everybody wants to do
[2317.80 --> 2321.56]  the new cool thing and then half the time they don't even use the old cool thing they just come
[2321.56 --> 2326.84]  up with a new cool thing because they're like i have the most brilliant idea ever and nobody's ever
[2326.84 --> 2335.16]  done it before and they have when i speak at like very enterprise conferences i uh describe web assembly
[2335.16 --> 2344.52]  as like fast cgi for the modern era uh partially just because you know that is basically what serverless
[2344.52 --> 2351.48]  is but also the execution model of web assembly is so close to that java is always interesting to me
[2351.48 --> 2360.92]  partially because like sun needed java to succeed like existentially and then well there's a reason why
[2360.92 --> 2368.52]  you can't go work at sun microsystems but java did a lot of really interesting things and i think part of
[2368.52 --> 2376.12]  of the reason the jvm could never really like be all it could be was because it was so tied to java
[2376.12 --> 2382.92]  the language a lot of stuff now exists that you know we'll run like python on the jvm and like whatever
[2383.88 --> 2391.40]  but a lot of that is sort of very new and java has its own like big set of like bloaty problems and
[2391.40 --> 2398.28]  people that need to understand how to tune and work on all of the bits that let the jvm be good
[2398.28 --> 2403.32]  but you don't see the jvm really scaling down effectively i mean like java card exists but
[2403.32 --> 2409.32]  like that's not the jvm i mean it is a full vm right like the java vm i have a question though
[2409.80 --> 2415.00]  when usually when you want things to be more secure right like there's always that balance between
[2415.00 --> 2421.40]  security and like unusability have you ever ran into like a any like of those type of issues because
[2421.40 --> 2426.52]  you're essentially putting a cloud in the box right so like what were like your main struggles
[2426.52 --> 2432.36]  i guess in putting it in the box like where did you have to make the choice of like secure
[2432.36 --> 2439.48]  versus usability in that process so the joys of having already thought through a lot of those problems
[2439.48 --> 2446.12]  is that like there's not a lot of new trade-offs really when you move from the cloud to putting
[2446.12 --> 2454.76]  it in a box because the way we think about building configuration and applications uh in the spin model
[2455.32 --> 2460.92]  where you're already defining the things you want and then at an infrastructure layer you're saying
[2460.92 --> 2465.80]  here are the things you can actually talk to and you're mapping those things together there's not
[2465.80 --> 2472.44]  really a whole lot of like serious security trade-offs in that bit specifically the thing
[2472.44 --> 2479.08]  i'm actually really struggling with is finding the right layer of like expressive infrastructure
[2479.08 --> 2483.96]  configuration and mapping that back to the developer programming model like it's a really
[2483.96 --> 2490.36]  big dx problem more than it is like a technical problem because when you're giving things people
[2490.36 --> 2494.92]  to run in their own infrastructure the like sort of combinatorial problem of like
[2495.56 --> 2503.32]  interfaces to back-end things is so much broader and trying to figure out like the right level of
[2503.88 --> 2508.20]  this is something your infra team should own versus this is something the developer should
[2508.20 --> 2515.00]  own the decision of is really nuanced like one of the things that i want to model in our kubernetes
[2515.00 --> 2522.76]  stuff eventually is um the concept of like a default data store so in fermion cloud every application
[2522.76 --> 2529.88]  gets access to at least a quote-unquote default key value store which is really nice to rely on because
[2529.88 --> 2535.80]  it means that every component can assume that it has access to some form of cache and like in building a
[2535.80 --> 2541.72]  lot of applications on top of that it's a really powerful assumption to be able to make and we want to be able to
[2541.72 --> 2551.24]  bring that kind of thing into kubernetes and so it's what i'm thinking about is how do you give that kind
[2551.24 --> 2559.48]  of magic to someone without making them write a ton of yaml because you know anything that is a
[2559.48 --> 2564.44]  configurable knob is something that will be off by default and then you can't rely on that assumption
[2564.44 --> 2569.72]  anymore and it's really hard to get right especially generally right right because like if you can get
[2569.72 --> 2575.40]  something right for a specific use case or for a certain type of uh developer application like
[2575.40 --> 2580.60]  yeah this is the right way to do this thing what's right for one person someone else absolutely hates
[2581.24 --> 2585.16]  and then once you're generic enough that you're like hey everyone should do this and i think that
[2585.16 --> 2590.68]  that's going back to like the kubernetes networking model right because one ip address per pod was right
[2590.68 --> 2598.20]  for a certain type of application and as long as it's it's one application instance for that network io
[2598.20 --> 2603.32]  yeah we're fine but once you're shoving a wasm runtime into that pod and then say now you are 5000
[2603.32 --> 2609.08]  applications um that model isn't the right defaults anymore hey for one person it's a feature another
[2609.08 --> 2614.92]  person's bug the load-bearing bugs are the hard part right like when someone's like i this needs to
[2614.92 --> 2625.72]  work this specific way otherwise i go down that's a problem a million dollar bug it's so hard like it's the
[2625.72 --> 2632.12]  like having run enough things in production to have like a lot of empathy for you know the tired
[2632.12 --> 2636.92]  operator who has been handed this thing by a dev team and been told to make it work that's why i think
[2636.92 --> 2640.52]  like when people are like you can't just say it depends and i'm like yes you can
[2642.60 --> 2648.44]  yes you can like if you have like when anyone speaks in total absolutes i'm always like
[2648.44 --> 2654.84]  like oh that is some confidence i don't know if i have
[2657.80 --> 2663.80]  maybe it's just like girl in tech like imposter syndrome but i'm just like absolutes are very hard
[2663.80 --> 2670.04]  for me like i'm like a majority of cases if you do x and y but like i don't know because i'm not
[2670.04 --> 2676.84]  surprised when something is like for me this was horrible i remember a long time ago being the excited
[2676.84 --> 2681.48]  person who would like read about something on the weekend and then want to do it and i'm now the
[2681.48 --> 2688.28]  person who like sees someone say that and goes not here as long as the pager goes to your phone
[2689.32 --> 2695.64]  i was that person for years and then now i'm just like can we just do it as simple and boring as
[2699.24 --> 2704.04]  i do still play with those things on the weekend and build something random that i won't get paged for
[2704.04 --> 2709.72]  but if i'm thinking of you know we want to hire someone and all of their resume is just ec2 and
[2709.72 --> 2716.84]  postgres like that is an instant hire because they know all the things right like like here's the 10
[2716.84 --> 2721.56]  things i built all of them with ec2 and postgres i'm like good this is the come on it's so funny
[2721.56 --> 2726.12]  because like i feel like everybody wants like to get a job with a new cool thing and i'm over here like
[2726.12 --> 2733.40]  what is the most boring legacy like hole i can fault like go hide in until this like ai thing is over
[2733.40 --> 2739.88]  no shade to ai like i want to use it but i just want to go crawl into like the most boring legacy
[2739.88 --> 2744.44]  like have you asked chat to bt to give you some recommendations i'm gonna go do that justin
[2746.76 --> 2749.00]  be like what do you not touch
[2752.28 --> 2758.28]  tell me the secrets i am like really enjoying the space i found myself in though where i get to like
[2758.28 --> 2764.76]  build the new cool shiny but with like the most boring choices possible those are the best new
[2764.76 --> 2770.28]  shiny things though like those are the shiny things i get excited about because it's like i hate the like
[2770.28 --> 2776.60]  you know sparkle points or like innovation points analogy but it works so well well and it also just
[2776.60 --> 2781.88]  sucks because like i do think some things are super interesting about it but now i'm scared to even touch
[2781.88 --> 2787.16]  those things because what happens when it bursts you know what i mean so it's not even like a shade
[2787.16 --> 2793.96]  to the new shiny thing oh i haven't even tried chat gpt what i'm like i'm too boring for this like my
[2793.96 --> 2799.56]  boyfriend hasn't tried it either and i'm like you work in tech and i'm just like how did how did you escape
[2801.96 --> 2809.40]  in firmy on cloud we have like an ai thing that like i help design and i'm like i i have no personal
[2809.40 --> 2817.08]  interest in using this see i love trying new things and new tools i just don't know like i very much
[2817.08 --> 2823.56]  believe in like use the tool that you need for the job like every database does not need to be a no
[2823.56 --> 2828.04]  sequel database as much as i love them you know job is not always right for stuff just because it's my
[2828.04 --> 2834.20]  favorite but like i think like people just don't know how to like in art we have this saying and it
[2834.20 --> 2838.36]  sounds horrible but it's called kill your ugly children and you have to accept when something doesn't
[2838.36 --> 2842.36]  work and it's bad and people don't want to do that they're like i used it once and i have to use
[2842.36 --> 2848.12]  it for everything you're like dude no you don't like like just put it down and it'll be okay
[2849.24 --> 2854.76]  i still remember the first time an art teacher told me to throw away a sculpture i've been working
[2854.76 --> 2860.84]  on and i was like that's why art kids do get great in tech because we know disappointment okay
[2860.84 --> 2870.68]  we know having your dreams killed so we're just like it's cool i may have spent like my life on this
[2870.68 --> 2878.28]  for two weeks but like i'm used to being disappointed yes like i just spent like 12 hours like shaping this
[2878.28 --> 2886.76]  eyebrow um you're telling me to throw it and start again yo art teachers are savage they'll be like it's
[2886.76 --> 2894.44]  horrible get rid of it start over and you're just like but i just put my whole life that's like my
[2894.44 --> 2901.64]  life's work and like i love it and it's like nope yeah it's like one of the fun parts of shooting film
[2901.64 --> 2907.24]  too is like you know it's this very like analog chemical process that sometimes just goes wrong
[2907.88 --> 2913.80]  for completely random reasons okay but is that not very related to building software though like i'd
[2913.80 --> 2918.60]  that's what like when people are like you have to have like this fancy degree from like this fancy
[2918.60 --> 2925.48]  school and i'm like but do you like sometimes having people with other backgrounds you know that have
[2925.48 --> 2931.48]  like sometimes i'm telling you some of the best developers i know have like the craziest like
[2931.48 --> 2936.76]  theater background and like all kind and i'm just like they are fire like they their brains work in
[2936.76 --> 2944.28]  ways that you're just like how did you get from point a to point b like i'm just amazed i'm a high
[2944.28 --> 2950.84]  school dropout and now like half the world runs my software it's cursed that is badass like sorry we're
[2950.84 --> 2959.48]  gonna bleep that out too but like i'm such a fan now like i love me a like beats adversity story like
[2960.36 --> 2965.32]  all for it danielle thanks so much for coming on the show today where can people find you online if they
[2965.32 --> 2971.72]  wanted to uh reach out and chat some more i moved to mastodon because that's where all the cool kids
[2971.72 --> 2979.32]  went but if you go to links.danielle.fyi you find me in all of the places come to blue sky
[2980.76 --> 2988.04]  i'm also technically on blue sky uh at danielle.fyi come back well we'll link that in the show notes for
[2988.04 --> 2993.32]  everyone so they can see it so thanks so much for coming on and explaining wasm and fermions cloud to us
[2993.32 --> 2999.96]  yeah i'm sorry that i am an unprepared mess it's uh no this is great i learned a lot we wanted a
[2999.96 --> 3007.96]  conversation to walk through it it was awesome oh wow this has been great thank you so much danielle
[3007.96 --> 3013.32]  for coming on the show and telling us all about the back end of fermion and web assembly in general
[3013.32 --> 3018.36]  and it's just such a different mindset when you think oh i'm going to shove a thousand applications
[3018.36 --> 3023.48]  on a single instance uh compared to you know back in the day when it was like one server one
[3023.48 --> 3028.36]  application containers kubernetes like oh i can get you know like maybe a hundred or so and they're
[3028.36 --> 3032.76]  just like let's just change how this works and get a thousand out of it that's just really cool
[3032.76 --> 3038.52]  we talked for so long that i think my computer died like even after you got off i was like had so
[3038.52 --> 3044.68]  much fun talking to her she was amazing so for this outro we're going to go into wta uh which stands for
[3044.68 --> 3049.96]  what the acronym and we just want to explain some of the acronyms that were either in the episode or
[3049.96 --> 3054.92]  just in general around web assembly because if it's a new space uh it is a very new space for a lot of
[3054.92 --> 3063.64]  people it wasn't even really announced until 2015 when it came out of mozilla it was a evolution of asm.js
[3063.64 --> 3068.92]  and asm stands for assembly uh it's like assembly code which is the machine code that you can write
[3068.92 --> 3074.60]  on which is usually like compiled to your processor and and you know higher level language is like oh
[3074.60 --> 3079.80]  i don't need to like compile to my 8086 anymore i can compile to like any processor and the you know
[3079.80 --> 3084.68]  the compiler figures that slide out of it was was amazing like that was a big step for development and
[3084.68 --> 3089.48]  how programming works and uh shout out to grace hopper for making cobalt you know back in the day
[3089.48 --> 3093.56]  to having these like higher level languages that you can just write once and compile them multiple times
[3093.56 --> 3099.40]  so asm stands for assembly and again like i don't actually don't know why like it's not
[3099.40 --> 3104.20]  there is an a and s and m in there but like why those three letters out of assembly i don't know i'm
[3104.20 --> 3112.60]  not sure but web assembly is is wasm or wasm and if you're reading it or writing it usually the
[3112.60 --> 3117.40]  acronym is all capitalized not all acronyms are fully capitalized and also when you're writing web
[3117.40 --> 3125.40]  assembly out long ways uh it's one word with the w and the a camel cased uh so just fyi to get those uh
[3125.40 --> 3129.80]  those things right sometimes it's just it looks better if you're correct in how you're spelling it
[3129.80 --> 3134.20]  it's really cool meeting different people and learning about products and then seeing where
[3134.20 --> 3138.36]  they come from like i wouldn't have like mozilla came up with that and just seeing the things that
[3138.36 --> 3141.72]  have come out of meta and all these different places and then they create something and then open
[3141.72 --> 3148.04]  source it's really cool yeah and really the beginning of asmjs was all about getting a smaller
[3148.04 --> 3153.72]  subset of javascript they wanted to minimize the amount of what you know javascript is a big language
[3153.72 --> 3158.68]  and how do we take just a small subset of javascript and then we can compile it and we can take it and we
[3158.68 --> 3163.40]  can actually just run it at more native speeds because javascript is an interpreted language and when
[3163.40 --> 3170.04]  you're moving text files around and then trying to interpret it and just in time compile it those are all
[3170.04 --> 3175.40]  things that just take time and it's something that machines like hey what if we compile this up ahead
[3175.40 --> 3179.40]  of time before we send it to a person we can make the file size smaller because it can be
[3180.12 --> 3185.56]  actually like in bytes not in text or ascii and and then we can also just the machine can read it
[3185.56 --> 3190.52]  and it can just start executing it and there's all these steps you can kind of avoid and then by
[3190.52 --> 3197.00]  minimizing all of the javascript from not everything but a smaller subset you can say like oh like you only
[3197.00 --> 3201.48]  write a small subset of javascript but then we can compile that and be really fast about it because
[3201.48 --> 3207.72]  we know how that's going to compile into what our runtime is going to execute not to like defend
[3207.72 --> 3214.20]  javascript i can't believe i'm defending javascript but i mean i think it's because it started off for one
[3214.20 --> 3218.92]  use and then people wanted to do so many different things and to be object-oriented programming and
[3218.92 --> 3225.24]  it just became so much to do so many things that it just got so big and web assembly has followed a very
[3225.24 --> 3229.96]  similar trajectory where javascript was first designed for the web browser web assembly ran
[3229.96 --> 3235.64]  in browsers and it was targeted for browser environments and how we make web apps faster
[3235.64 --> 3240.04]  and then it kind of shifted into this like what node.js did for javascript right where it's like oh we
[3240.04 --> 3244.44]  can run this on the server and we can say like oh we have a runtime that runs outside of the browser
[3244.44 --> 3249.56]  and how does that work and that's what a lot of the fermion and the web assembly like cloud environments
[3249.56 --> 3254.36]  do we're like hey we're running executing code that runs services and most of the time these are
[3254.36 --> 3258.76]  like functions these are more like lambda functions or function as a service where it's just executing
[3258.76 --> 3263.56]  one thing and then dying that's how like cloudflow workers and fermion works there are some that are
[3263.56 --> 3268.76]  starting to do these like long running processes more like a traditional web server like nginx
[3269.48 --> 3275.08]  but that gets into the next acronym of the web assembly system interface which we did mention in the
[3275.08 --> 3282.12]  interview the wasi w-a-s-i is is that interface of how it's kind of like the node.js of web assembly of
[3282.12 --> 3286.92]  like how does this thing that is intended to run inside of a basically an operating system
[3286.92 --> 3292.52]  right like a browser is an operating system to many many degrees it has isolation it has all this
[3292.52 --> 3297.56]  runtime stuff that's built into the browser but what if we don't have a browser what if we don't have
[3297.56 --> 3303.56]  chrome or firefox and so you need another runtime engine that can execute this code that's like when
[3303.56 --> 3308.04]  people try to argue if a hot dog's a sandwich or not and then people have these debates on twitter for
[3308.04 --> 3312.04]  like people like like debating things they really do
[3314.52 --> 3319.48]  sometimes you're like why do you care so much those people should just get kids is my hot take
[3319.48 --> 3323.16]  today it's just like if you have they can argue a tiny version of themselves
[3324.84 --> 3326.44]  i feel you i've been there all weekend
[3328.20 --> 3334.20]  if you like to argue go have a seven to 12 year old i don't know somewhere there i'm sure older and
[3334.20 --> 3337.88]  younger this it happens but like but i feel like there's like a sweet spot in there of like you
[3337.88 --> 3342.68]  know what they know enough that they know how to argue it but they don't know does your kid ever say
[3342.68 --> 3346.92]  something that feels so much like yourself that you feel like you're arguing with a smaller version
[3346.92 --> 3351.32]  of yourself and you're just like i can't believe i've made you and kept you alive just for you to
[3351.32 --> 3355.08]  argue with me and tell me how terrible i am and that's when i just say go to your room
[3355.08 --> 3360.12]  like i'm sorry i fed you
[3362.92 --> 3368.92]  a couple other acronyms here we are we did mention just in time compilation j-i-t jit uh is a common
[3368.92 --> 3374.28]  way to abbreviate that as well as at least their acronyms like kind of sound cool wasi sounds cool
[3374.28 --> 3377.72]  yeah it's hard when someone's saying it right because if someone says like oh it's it's jit
[3377.72 --> 3381.72]  compiled you're like well if you're not familiar with it you know like you're taking the the code
[3381.72 --> 3384.92]  and interpreting it and compiling it right there it's kind of what python does right like
[3385.08 --> 3391.64]  python's not running the text files it's compiling it's just in time ahead of time or aot compilation
[3391.64 --> 3396.20]  is what you do with like a rust or go or something that's like oh i'm gonna make this binary and then
[3396.20 --> 3402.44]  we're gonna ship the binary out wasi interfaces was tripping me up because wasi is web assembly
[3402.44 --> 3406.60]  system interface and then there's an interfaces on top of that like it's an interface interface
[3406.60 --> 3412.20]  yes that's a it's like atm machine uh you have an automated automated teller machine machine
[3412.20 --> 3418.36]  um is how that works and so it feels a little redundant but the wasi interfaces is just like
[3418.36 --> 3423.72]  general categorization of how your code is going to interact with a wider system and those are things
[3423.72 --> 3430.52]  like input outputs for you know like streams uh clocks random file systems sockets um there's a
[3430.52 --> 3436.12]  couple other ones what are those uh cli and http these are all different interfaces that your application
[3436.12 --> 3441.16]  says oh i need the file system and so i'm going to use that interface and those get declared in
[3441.16 --> 3446.60]  what's called a wit file w-i-t yeah these acronyms just keep going they're all w's and they just keep
[3446.60 --> 3452.12]  all kubernetes stuff is k's all web assembly is w's and a w-i-t a wit file is a web assembly interface
[3452.12 --> 3457.72]  type and so you define that as hey i need to use this interface and and then when the runtime is going
[3457.72 --> 3463.96]  to let you run it says oh you can or cannot access that thing which has good and bad parts of it
[3463.96 --> 3469.80]  because if i'm using the runtime and say hey i want to interface with the database then it doesn't
[3469.80 --> 3475.16]  matter what the database is on the back end i need a sql database the runtime can interface and say like
[3475.16 --> 3480.12]  oh well you you can get my sql you can get postgres you can get whatever i tell you is this generic
[3480.12 --> 3484.36]  database thing and and that could be really good from an application developer you're like i just need
[3484.36 --> 3489.72]  the generic thing but can also be bad when you need something specific exactly because you're like i need
[3489.72 --> 3495.88]  this specific feature from this it's always that caveat yep it's easy to write and deploy as long
[3495.88 --> 3499.72]  as you fit the mold of what they're providing you and as soon as something's different because the
[3499.72 --> 3507.40]  second you don't it's gonna get real yep then you have to control it yeah so for now the wasi interfaces
[3507.40 --> 3513.64]  are are categorized in these different types and your runtime can provide that into you as an
[3513.64 --> 3518.28]  application but those are all still pretty new those are all very like they're very new there's like
[3518.28 --> 3523.72]  point two specification of these interfaces so they're still evolving interface interface it
[3523.72 --> 3528.12]  just made me think about the fact that javascript has three equal signs and that just hurts my soul
[3528.12 --> 3534.04]  every time i see it like a little part of like me dies the last couple things i want to talk about was
[3535.16 --> 3543.16]  some runtimes there's wasmer which is w-a-s-m-e-r which is an acronym for how it sounds like i don't
[3543.16 --> 3548.36]  wasmer yeah like their acronyms are very cute i don't know if i'd like would guess any of these
[3548.36 --> 3553.16]  things from the acronym but you know and that's why we're here that's why we're explaining this stuff
[3554.28 --> 3561.48]  so wasmer is is a runtime so again you can execute your wasm bytecode and is created by the wasmer
[3561.48 --> 3566.44]  company i actually don't know i couldn't find like who's behind the wasmer company but they make a
[3566.44 --> 3573.96]  runtime named after themselves but they also make wapm w-a-p-m which is the web assembly package
[3573.96 --> 3579.72]  manager and this is kind of the like a registry of reusable bits for web assembly compiled code
[3580.28 --> 3584.20]  you can think of this as any sort of registry is something like similar to maybe a terraform
[3584.84 --> 3590.60]  modules or docker hub the downside is this is very very new and so when i looked at it there was only
[3590.60 --> 3596.04]  like a thousand packages out there and there was only like a dozen that looked reasonably useful
[3596.92 --> 3600.52]  a lot of them to me were just like oh i don't i have no idea what that does it seems like someone
[3600.52 --> 3606.04]  just uploaded a package just to see how uploading packages works um so looks a little bit promising
[3606.04 --> 3610.68]  but again another acronym that you might want to know because they have a command line tool
[3610.68 --> 3617.48]  wapm to install packages from their registry i feel like half of tech is algorithms you mean
[3617.48 --> 3623.40]  acronyms acronyms this is what happens when you've been at home with your kids for three days
[3625.80 --> 3632.68]  they suck all the think out of you oh my god my brain used to work well it has to work for tuesday
[3635.48 --> 3637.16]  put in the wall to sleep so early
[3639.48 --> 3640.44]  seven o'clock go to bed
[3640.44 --> 3648.60]  the last one i want to talk about the last runtime is wasm time and this one is created by the bytecode
[3648.60 --> 3656.04]  alliance and the bytecode alliance is a non-profit that is is trying to push the specs forward for
[3656.04 --> 3662.60]  what web assembly is what wasi is and they created wasm time as a runtime for web assembly and the
[3662.60 --> 3667.32]  bytecode alliance uh i couldn't tell if they were like a sub organization like a lot of them are part
[3667.32 --> 3671.24]  of the linux foundation yeah that's what i'm trying to understand like how what is the hierarchy or
[3671.24 --> 3677.64]  like the way this is all structured so anyone not familiar any sort of like non-profit or foundation
[3677.64 --> 3681.80]  that kind of does this stuff like cloud native computing foundation all of the companies that are
[3681.80 --> 3686.84]  part of it pay money they pay a lot of money to be part of it they get a seat on the board and they can
[3686.84 --> 3693.64]  set the direction for what that foundation does and so some companies on the bytecode alliance
[3693.64 --> 3699.80]  board or or part of the companies that pay into it are companies like amazon cisco microsoft intel
[3699.80 --> 3704.20]  docker arm there's a bunch of them there's a bunch of big names that you've heard of and a bunch of
[3704.20 --> 3708.76]  smaller companies that are really specific in this space and they pay money into it so they can have a
[3708.76 --> 3713.88]  seat at the table they can say hey this is a priority for us we have to make wasi the system
[3713.88 --> 3720.52]  interfaces really good or we need an interface that does this and they put the money in they control the
[3720.52 --> 3725.48]  the direction for it and then they also can help add developers and have ownership of some of the
[3725.48 --> 3729.96]  projects right they're maintainers they built wasm time which is actually a really interesting thing as
[3729.96 --> 3735.16]  a person working at a large company if you want to work in open source and you want to work as like hey
[3735.16 --> 3740.20]  i want to give back to the community this is one of those ways that usually it happens as i used to work
[3740.20 --> 3746.04]  on the eks team at amazon and a lot of what i did was open source because a lot of the community was
[3746.04 --> 3750.84]  was open source first and being in that environment makes it really easy to say like hey i don't
[3750.84 --> 3756.20]  actually contribute internally to the code i contribute externally in the community and then
[3756.20 --> 3761.72]  we pull that whatever i do externally we pull that back in so we can use it it seems like more and more
[3761.72 --> 3766.60]  that's where it's going and i hope that's where it continues to go yeah there's definitely some larger
[3766.60 --> 3771.40]  projects that need that kind of guidance and really that kind of funding because this stuff doesn't happen
[3771.40 --> 3776.52]  with no funding and actually that leads us right into the the very end of here where our next week
[3776.52 --> 3782.76]  episode is going to be with gina uh who runs octoprint and that is one of those completely self
[3782.76 --> 3789.48]  community funded no foundation uh donations uh provided to create great software that she's been
[3790.04 --> 3795.16]  creating and building and running for what was it 15 years something like that more than 15 years 10 i think
[3795.16 --> 3800.20]  she started doing it full-time 10 years that's right it was like a hobby for yeah it was something she
[3800.20 --> 3807.48]  started on a christmas break i think yeah gina's amazing she talks multiple languages she is the
[3807.48 --> 3815.00]  sole maintainer and not just python and yeah she's just amazing like she's just like and then i solved
[3815.00 --> 3819.88]  this problem and i found this problem and then i made this solution for it and i'm just like you
[3819.88 --> 3825.96]  are just a legit problem solver it's amazing yeah so thanks everyone for listening um if anyone is
[3825.96 --> 3833.32]  around any conferences in june just a heads up i'm going to be at a couple conferences on june 22nd a
[3833.32 --> 3840.76]  few weeks after this goes out at sre day in san francisco and the uh 26th and 27th i'll be in seattle at
[3841.64 --> 3847.40]  cloud native security con i have talks at both of them so if you're around and uh want to say hi i have
[3847.40 --> 3852.12]  some stickers that we can hand out and we just love to meet anyone and see what you're working on and what
[3852.12 --> 3858.52]  uh what software you're learning sneak me in to the security one in seattle so we can like record
[3858.52 --> 3863.08]  an episode it will be fun well we'll have to figure something out so for sure i'm going to be around um
[3863.08 --> 3868.04]  so definitely uh let me know if you're there and we will talk to you all next week bye guys
[3868.04 --> 3879.96]  thanks for listening to ship it with justin garrison and autumn nash subscribe now if you haven't
[3879.96 --> 3885.72]  already head to ship it.show for all the ways or just search for ship it wherever you get your
[3885.72 --> 3892.68]  podcasts you'll find us thanks once again to our partners at fly.io to the mysterious breakmaster
[3892.68 --> 3899.96]  cylinder for these dope beats and to sentry use code changelog when you sign up and save 100 bucks
[3899.96 --> 3905.08]  off their team plan that's all for now but come back next week when we continue discussing
[3905.08 --> 3911.64]  everything that happens after get push
[3922.68 --> 3951.16]  skew
