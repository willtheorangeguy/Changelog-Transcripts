[0.00 --> 14.90]  welcome back everyone this is the changelog where a member supported blog podcast and weekly email
[14.90 --> 20.74]  covering what's fresh and what's new in open source check out the blog at the changelog.com
[20.74 --> 27.76]  our past shows at five by five dot tv slash changelog and you're listening to episode 121
[27.76 --> 34.18]  we're joined today by lars bach and seth ladd just two of the awesome team members behind dart
[34.18 --> 41.96]  a new language and platform started by google for scalable web app engineering today's show is
[41.96 --> 48.18]  sponsored by our partner digital ocean fresh books and new relic we'll tell you a bit more about
[48.18 --> 54.06]  fresh books and new relic later in the show but digital ocean we owe our uptime to digital ocean
[54.06 --> 58.46]  we're hosted on digital ocean we are partnered with digital ocean we think that you should
[58.46 --> 65.04]  use digital ocean i mean that's that's that should be the spot right there right but it goes on uh
[65.04 --> 71.68]  it's super easy to use digital ocean literally in 55 seconds you got a server full root access ssh keys
[71.68 --> 77.60]  on the machine your choice of os at your fingertips it just doesn't get any easier than that it's
[77.60 --> 83.68]  affordable pricing plans start at five bucks a month you get half a gram 20 gigs of ssd drive space
[83.68 --> 91.64]  one cpu one terabyte transfer and it's blazing fast ssds and it's super easy to use use the promo
[91.64 --> 98.92]  code changelog may that's right changelog may to get a ten dollar credit when you sign up head to
[98.92 --> 103.04]  digital ocean.com to get started and now on to the show
[103.04 --> 113.02]  welcome back everybody we are joined today by lars bach and seth ladd lars is the co-founder a co-founder
[113.02 --> 119.88]  of dart and v8 and seth is a developer advocate for dart we're here today to talk about dart and
[119.88 --> 125.90]  what it is and all those good things so lars why don't you give us an introduction to who you are and
[125.90 --> 132.70]  where you come from i don't want to spend too much time but the sad story is i've been doing virtual
[132.70 --> 139.84]  machines for object oriented languages since 88 so there's been a few and you probably can remember
[139.84 --> 148.20]  some of them like hotspot i was a tech leader on hotspot i've done strong talk what else v8 is one
[148.20 --> 157.44]  and so lots of different virtual machines and and my game is making the the languages run fast and
[157.44 --> 163.96]  lately last three years i've been focusing on the new programming language start and it's basically sort
[163.96 --> 171.12]  of uh written is from the experience of implementing the ioscript so we can talk about the later yeah
[171.12 --> 175.14]  for sure so i i forgot to mention when i introduced you that you both are at google so i just wanted to
[175.14 --> 181.28]  make sure we make that clear that is true okay all right and seth why don't you give us an introduction
[181.28 --> 187.20]  about who you are and where you come from sure so i'm a developer advocate with the google developer
[187.20 --> 193.36]  team and for the past couple years i've been focused on dart and helping external and internal
[193.36 --> 200.36]  developers get online with our tools our language our libraries and help get the community excited
[200.36 --> 207.62]  and participating in this new project awesome so can can one of you give me a introduction to what
[207.62 --> 211.46]  dart is i think that you know a lot a lot of people have heard about it because it's not exactly
[211.46 --> 216.28]  you know brand new um but but but maybe there are some people out there that aren't really familiar
[216.28 --> 221.42]  with it and would like to know what it is oh i can take a stab at that we started the dart project
[221.42 --> 227.04]  three years ago and it's a platform so and it includes a new programming language for the web
[227.04 --> 234.06]  but it also has a libraries a consistent set of libraries and programming tools on top of that
[234.06 --> 240.94]  if you talk about the the language it's a a clean simple class-based object oriented languages
[240.94 --> 247.94]  language and it's more structured than javascript and we want really want to capture people that are
[247.94 --> 253.76]  interesting uh having structure in the programming language so they can easily do refactoring and
[253.76 --> 262.86]  build last a lot web applications awesome so one of the things about dart i think that um i've i've
[262.86 --> 267.38]  heard just kind of talking to people and and and actually like doing some of my own research is
[267.38 --> 273.12]  right now it seems like and this is kind of the main one of the main questions i want to kind of
[273.12 --> 278.30]  get to but right now it seems like one of the big goals of dart is to be able to compile it down to
[278.30 --> 284.70]  javascript but that doesn't feel like the end goal for dart so would you say that javascript or sorry
[284.70 --> 290.30]  that dart is is is going to be an evolution in in uh you know writing program programming for the web or
[290.30 --> 294.26]  is it going to be an option you know a la coffee script or something like that to compile down to
[294.26 --> 301.08]  javascript well first of all i have to say for us uh being compatible with the web is really important so
[301.08 --> 307.80]  one of our most important components is the dart to js compiler it translates the dart source code
[307.80 --> 314.00]  into javascript and ensures that you get the same semantic semantics as if you ran on top of the
[314.00 --> 319.72]  virtual machine of course we have a virtual machine as well and we have a special build of chromium
[319.72 --> 328.64]  we call dartium and it has that dart virtual machine built in and so we can run raw dart in that
[328.64 --> 336.16]  browser but yeah the compatibility with the web is super important for us so so do you think that's
[336.16 --> 341.86]  something if i guess the question is if you had to kind of pick like would compatibility with javascript
[341.86 --> 346.08]  be what you would rather would you rather every browser have the dart vm installed
[346.08 --> 353.72]  well first of all it's always great if people take all our code and include in the browser but
[353.72 --> 358.68]  i think the the point is what we're trying to do is we are we're trying to make sure that
[358.68 --> 367.16]  that if you only have a javascript engine in your browser you'll still run a dart fine but there's
[367.16 --> 373.92]  certainly advantages or we're running the dart vm inside the browser two of them is that it runs faster
[373.92 --> 380.10]  and secondly you have a fantastic startup experience because the application startup super fast
[380.10 --> 386.16]  i do want to draw a distinction though between dart and some of the other languages like coffee script so
[386.16 --> 392.34]  coffee script is designed to provide a new syntax on top of javascript but it still retains
[392.34 --> 398.42]  javascript semantics whereas dart is its own language so yes compiling a javascript is really
[398.42 --> 403.18]  important for the project in the web but we're as large was saying we're we're able to bring over the
[403.18 --> 408.42]  semantics from the dart language and libraries back down to javascript so it's not just syntactic like
[408.42 --> 414.60]  code of paint so yeah that's something that you know you'll see with like typescript and asm
[414.60 --> 421.24]  that that are more like you know just you know subsets or supersets of javascript but this is a new
[421.24 --> 426.32]  language but i i have a i mean maybe just in layman's like if you could explain to me the difference
[426.32 --> 434.50]  because uh if it compiles down to javascript then it seems like it while you know in the future i could
[434.50 --> 440.08]  envision a world where using dartium or any other browser with the dart vm uh has major advantages
[440.08 --> 444.00]  because you can write dart and run dart in the browser but as long as it's being used to compile
[444.00 --> 449.10]  down to javascript it i don't really necessarily see the the huge increases that you can get with the
[449.10 --> 456.58]  dart vm so well well um let me just uh stop you a little bit it's uh you get fast execution i guess
[456.58 --> 463.56]  that's a good thing but think about the development process when you change the line of code you can
[463.56 --> 468.56]  be up running right away instead of first translating to to javascript and run in a
[468.56 --> 476.74]  java engine if you have the dart vm inside the browser right you can do a debugging at the source level
[476.74 --> 483.38]  and you can do very interesting things that are based on the language that's hard to do when you
[483.38 --> 489.54]  first translate to javascript and want to provide the same kind of programming experience yeah so so i
[489.54 --> 494.06]  guess that's what i'm saying is that it seems like the major the major benefits of dart other than just
[494.06 --> 498.38]  you know the the language itself being a very clean language is like when you actually use it in its
[498.38 --> 503.50]  in the dart vm itself rather than compiling it to javascript i think one of the huge benefits of dart
[503.50 --> 508.58]  is the productivity which is sort of what lars is alluding to here and that as a developer and i'm
[508.58 --> 515.14]  being asked to deliver engaging wonderful experiences to my users on mobile devices that need to run 60
[515.14 --> 521.04]  frames a second take advantage of all the html5 features and really take advantage of these new
[521.04 --> 527.50]  mobile devices i'm being asked to develop and deliver much more complex applications and when i have a
[527.50 --> 533.10]  much more complex world i need languages libraries and tools to help me compensate for that and do things
[533.10 --> 539.38]  like static analysis warnings refactoring all the great stuff that we've had for other platforms for
[539.38 --> 544.70]  years and years and years and to get i'm i'm basically being asked to do this on the web now today just
[544.70 --> 548.98]  because my users are asking for this and so the huge advantage of dart is i get that productive
[548.98 --> 553.56]  development experience yet still get the really fast iteration times of the web
[553.56 --> 559.62]  so so one thing i would like to mention about the language we haven't talked about what's in the
[559.62 --> 567.82]  language but one thing i find that's really great is the optional typing an optional static typing
[567.82 --> 575.12]  gives you that you can start programming without any types so when you do experimentation you can get up
[575.12 --> 581.70]  run very fast but as you write a library and you want to harden it you put in the types maybe on the
[581.70 --> 587.44]  interface to the library and you can make sure that if people want to use the library they can
[587.44 --> 594.20]  validate that you pass in the right kinds of objects to that interface and i think that that allows the
[594.20 --> 599.94]  programmer to to trust the library more instead of that if you don't have any types and you call a
[599.94 --> 604.12]  library and you get an error you basically have to debug a third-party code which is not easy
[604.12 --> 610.06]  yeah i think there are some really cool things about dart uh that the language itself which will
[610.06 --> 616.78]  we'll get into in in a in a little bit but uh the one thing that i think so okay so we we've talked a
[616.78 --> 623.54]  little bit about you know what's the the the major benefit of dart uh in its current form but what
[623.54 --> 629.14]  would you say where do you see dart in five years or in 10 years or in 15 years like where where do you
[629.14 --> 636.70]  want to see this project headed clearly we want to make sure that a lot of programmers will use it
[636.70 --> 646.06]  right now it's clear that web applications are becoming larger and larger and to control these big
[646.06 --> 652.82]  piles of source code i believe strongly that you need a better structure in the programming language
[652.82 --> 659.26]  and the way we handle libraries in dart will certainly help you the projects we have been
[659.26 --> 666.76]  supporting in dart they have all been saying that as soon as they uh get used to the new language which
[666.76 --> 672.84]  doesn't take very long they really really like uh the the typing and the tools so they can you can do
[672.84 --> 678.34]  refactoring that really counts when you build big applications and you have to maintain them over time
[678.34 --> 685.00]  yeah one of the the and this is kind of an aside here the fact that dart doesn't hoist variables i think
[685.00 --> 690.68]  makes it uh a lot easier to read like you know top to bottom than javascript just in general i mean
[690.68 --> 696.32]  that's like a a one little teeny feature of dart but like a major impact in readability when i've
[696.32 --> 703.42]  since i've noticed it so you asked uh what do we want to see in 5 10 15 years i'm extremely motivated
[703.42 --> 712.00]  to help the web continue to develop and deliver amazing experiences on mobile devices and so if anything
[712.00 --> 716.90]  we can do to help developers just naturally and organically continue to pick the web to deliver
[716.90 --> 723.16]  these really great experiences then i'm very happy i feel like at this point we need to give developers
[723.16 --> 727.56]  who are used to building on native platforms and who have very high expectations and tools and
[727.56 --> 731.84]  productivity i need to deliver that to developers when they want to target the web
[731.84 --> 740.14]  yeah so i think that that that's definitely a uh uh uh what's the what's the word a pretty broad
[740.14 --> 744.40]  goal right and i think that that's that there's nothing wrong with that i think that's a that's a
[744.40 --> 751.64]  that's a great goal but uh how do you how do you do that i mean i guess my question is i'm i'm trying to
[751.64 --> 757.38]  figure out a good way to word this but so in the 90s like you know javascript comes about and then all
[757.38 --> 761.64]  of a sudden today it's ubiquitous and it's everywhere and you can you know use it in any environment that
[761.64 --> 766.48]  basically a browser exists and and and now with node in cases of not the browser existing so
[766.48 --> 771.92]  like how does dart go from where it is now to becoming like a ubiquitous where you can use it
[771.92 --> 778.80]  anywhere well in the the first phase here it was very important to focus on the the web client and
[778.80 --> 784.86]  making sure that we can do web applications really well the next step is of course of course uh uh running
[784.86 --> 790.04]  on the uh the front end of the server so you can use the same programming language the same libraries
[790.04 --> 797.62]  in the client but also on the server side and with our last released uh release we we send out some
[797.62 --> 803.44]  more io code so you can actually run uh the the dart system on the server side so it's clear that
[803.44 --> 809.10]  if you can span from the client to the server it gives huge advantages to to the programmers
[809.10 --> 819.96]  yeah but again the uh what i would like to say that uh what's important to us is to make sure that
[819.96 --> 827.86]  we provide a very efficient uh programming platform and uh of course it's great to get more users but
[827.86 --> 837.48]  making sure that people can innovate faster uh is is a clear goal for us um i think um that is a
[837.48 --> 841.46]  different language and it's certainly not everybody that likes a new language for the web
[841.46 --> 846.76]  but deep down i think that innovation is what's going to make the web even better
[846.76 --> 852.94]  so it may be worth it to just talk about what is dart for a second because we we've talked a lot
[852.94 --> 857.84]  about the language a lot and i'm not sure many people know the full breadth or scope of the platform
[857.84 --> 863.70]  so real briefly it is its own language um and i'd love to hear lars talk a little bit about some of
[863.70 --> 868.92]  the influences to that but there's also a core set of libraries which i think is really missing from
[868.92 --> 873.54]  the web platform right now it's very hard to say like what kind of collection facilities do i have
[873.54 --> 879.72]  what do i have for dates and times what do i have for stopwatches debugging uh you name it uh so dart
[879.72 --> 884.56]  ships with a very rich core set of libraries it also has a package manager and inside the package
[884.56 --> 893.36]  manager you can go get libraries for crypto game uh game drivers um image processors you name it
[893.36 --> 899.74]  there's i think over 880 packages in our package repo right now we also ship uh an editor and
[899.74 --> 905.94]  plugins for other editors like sublime and webstorm and eclipse uh and then we have of course a dart to
[905.94 --> 912.80]  js compiler and we also have a great static analyzer which is speaks to that uh productivity aspect of dart
[912.80 --> 921.12]  where because dart is static and toolable i can run programs that tell me where i have warnings and errors
[921.12 --> 926.66]  before i run the program and that's such a huge productivity win so it's i really think of dart as a
[926.66 --> 933.30]  as a platform on which i can build so it's interesting because we actually had uh rob pike and andrew geron on
[933.30 --> 940.44]  the show to talk about goo or goo that's funny talk about go a while back but uh it feels kind of like
[940.44 --> 946.94]  you are taking the same like approach to dart as you as they are with go and that you know tooling and
[946.94 --> 952.62]  like productivity is a is a major major part of it it's not just a language that's you know that
[952.62 --> 957.14]  that's it's right it's not just the syntax that compiles the javascript it's its own language with
[957.14 --> 963.54]  its improved semantics uh better developer productivity and very toolable but i think the
[963.54 --> 969.50]  there are certainly big differences between uh go and dart yeah one thing i would like to highlight
[969.50 --> 974.08]  is that we have been very conservative when designing the language so if you have a background
[974.08 --> 982.48]  in java or c sharp or javascript it should be very easy to start being productive in dart i would say
[982.48 --> 988.60]  in a few hours you can probably understand most of the semantics of dart and that has been a goal
[988.60 --> 995.24]  from the beginning so that we can easily get programmers to be productive in our system yeah
[995.24 --> 1003.72]  so talking about uh a little bit about the community of dart here the is it similar as go
[1003.72 --> 1008.42]  where like it's an open language and that the kind of the whole world can see the changes that are made
[1008.42 --> 1012.74]  but you're you're hesitant to accept changes from the outside world as of right now anyway
[1012.74 --> 1020.74]  or on the contrary we want all the changes we can get so the so everything that relates to dart
[1020.74 --> 1028.34]  is out in the open uh even from day one uh all our chains let's go directly to the outside and and
[1028.34 --> 1036.58]  we are getting patches in from uh from external developers and we encourage that a lot it's of
[1036.58 --> 1044.82]  course clear it's clear that for some uh corner cases of the the advanced compiler not many people
[1044.82 --> 1050.60]  contribute uh but uh in in more light areas uh we get a lot of contribution uh especially when it
[1050.60 --> 1057.28]  comes to packages and and so on but on that note the language itself is now in the ecma
[1057.28 --> 1064.48]  spec uh process in fact there was some really good news there with the ecma group tc52 has been
[1064.48 --> 1070.40]  meeting to discuss the dart language spec itself and it looks great and it looks on track so what does
[1070.40 --> 1073.98]  that mean for dart when when if dart becomes standardized what does that what does that
[1073.98 --> 1078.40]  mean how does that change the game it basically means that there's an official process how the
[1078.40 --> 1085.44]  language is going to change in the future so we inside google cannot just decide um to change it
[1085.44 --> 1091.08]  and i think that's really important if we want to have other companies or organizations implement
[1091.08 --> 1097.32]  another version of the vm because then they can join the committee and make sure they have an
[1097.32 --> 1103.80]  influence in how the language is going to change in the future do you think that there's it's double
[1103.80 --> 1108.96]  yeah it's double important too when you're talking about building web languages and things that need
[1108.96 --> 1115.10]  to live in the open like the web ecosystem does so i think a lot of developers are just look for that
[1115.10 --> 1121.22]  to make sure that they can trust this is something that has legs and longevity let's pause the show
[1121.22 --> 1125.66]  for just a minute give a shout out to our sponsors fresh books you know we use fresh books here at
[1125.66 --> 1131.42]  the change login i gotta i gotta say i'm probably logged into fresh books five ten times or more a
[1131.42 --> 1139.64]  day um either sending invoices reviewing invoices estimates uh receipts expenses all these different
[1139.64 --> 1145.82]  things we're doing and honestly it makes our life a breeze it it makes my life so much easier and it
[1145.82 --> 1150.70]  makes people that work with us their life so much easier because it's so easy to pay us it's so easy to
[1150.70 --> 1157.72]  to like collaborate on what's going on um around these parts of our business and it's just just
[1157.72 --> 1162.22]  love fresh books and i want you to love fresh books too if you're if you're out there and you're not
[1162.22 --> 1169.70]  using fresh books go try it out 60 day free trial we're giving away um to our listeners uh if you go
[1169.70 --> 1175.96]  to getfreshbooks.com and enter the change log in how did you hear about us uh when you sign up you'll get
[1175.96 --> 1181.46]  access to that 60 day free trial uh because they support five by five and the change law but
[1181.46 --> 1186.30]  tell me if this sounds like you we just came to this tax season and your life is probably a bit of
[1186.30 --> 1189.94]  a mess if you weren't using fresh books you're digging through invoices you're going through
[1189.94 --> 1196.34]  all your records one by one it's the worst no one wants to do that and that's why there's fresh books
[1196.34 --> 1202.74]  okay it's simple it's easy it's a cloud accounting solution that makes not only your taxes easy but
[1202.74 --> 1209.20]  your day-to-day business a breeze uh create professional invoices capture and track expenses
[1209.20 --> 1215.38]  get real-time business reports in just a few clicks all too easy the sooner you start using fresh books
[1215.38 --> 1222.42]  the sooner you can start focusing on the work you love focus on your work not your paperwork again go to
[1222.42 --> 1230.18]  uh go to this url getfreshbooks.com and enter the change log in the how did you hear about us section
[1230.18 --> 1239.22]  and you'll get access to that 60 day free trial from fresh books do it now do you think that uh
[1239.22 --> 1244.46]  the lack of standardization right now has prevented anyone from considering building a vm for dart other
[1244.46 --> 1253.12]  than google um we're still early in the process i would say um but the you cannot make a standard
[1253.12 --> 1258.98]  out of something that's moving uh fast so it's important that you have a basic design of the language
[1258.98 --> 1266.28]  and it's fairly stable before you standardize it so you need to be at a certain uh stage before you
[1266.28 --> 1270.36]  can start standardizing i think we are there now we haven't changed the language very much since we
[1270.36 --> 1277.02]  came out with one o in november uh so this is the right time to do it and uh we expect that the
[1277.02 --> 1283.68]  the current spec is will be ratified in in the ecma tc 52 here uh this summer
[1283.68 --> 1289.24]  that's pretty quick actually i feel like that just a few months to to have the spec ratified
[1289.24 --> 1299.58]  well we started the process um uh late last year so okay it's half a year so yeah so it's funny when
[1299.58 --> 1303.84]  we talked about i i felt like i had heard about dart much longer you said the project's only about three
[1303.84 --> 1312.80]  years old yeah a good three years yeah so when you say yeah i mean just i i just remember hearing
[1312.80 --> 1316.96]  about dart and i guess maybe i've made so many life changes in the last couple years that it seems
[1316.96 --> 1322.14]  like it's been a lot longer but but that's a pretty quick process in general to to start the language and
[1322.14 --> 1327.34]  get to a point now where we're talking about you know like like when you started dart three years ago
[1327.34 --> 1332.28]  was it something that it was an experiment or or did you did you kind of envision it being this
[1332.28 --> 1341.84]  here only three years in the future um well i hoped it would be at this point uh so but when you
[1341.84 --> 1349.60]  started it was not an experiment uh um like five years ago um i did an experiment with casper that
[1349.60 --> 1356.50]  where we spent one quarter do a dart like dart like language we did a vm and an implementation just
[1356.50 --> 1362.74]  to see how it would work on the web um and that looked pretty good so uh three years ago we got
[1362.74 --> 1369.26]  the the go ahead uh to do it but it was not an experiment we really wanted to change how you did
[1369.26 --> 1375.94]  uh web applications or you could there was an alternative to do web applications so uh i think
[1375.94 --> 1381.10]  we are on good track three years is not long for a new programming language and we're getting good
[1381.10 --> 1386.48]  traction the the interesting part is that people that actually have tried uh dart and developed
[1386.48 --> 1393.18]  some real code with it they are fairly happy and that's what makes me proud yeah i mean i would
[1393.18 --> 1397.46]  encourage anyone to just go to the website and and you can tell very quickly that this is not
[1397.46 --> 1402.38]  it's very different from javascript in a lot of senses but it's very easy to pick up and you can
[1402.38 --> 1406.32]  just kind of you can tell that that there's a lot of emphasis put in like you know if you're a web
[1406.32 --> 1410.44]  developer if you've built things for the web right now it's not a huge hurdle to be able to write
[1410.44 --> 1416.80]  dart and i think that's a major win uh for you guys for sure and uh just to to talk about the
[1416.80 --> 1423.68]  seriousness of the project we are working we really hard to have a very clear semantics that's documented
[1423.68 --> 1428.48]  with a language specification and making sure the implementations we have are conformant so
[1428.48 --> 1436.54]  um that's what we spend a lot of time on and also making sure that when we generate a javascript
[1436.54 --> 1442.76]  from dart we validate the resulting code it runs in the various modern browsers like internet explorer
[1442.76 --> 1452.28]  firefox safari and obron so i want to move on a little bit to the language itself and some of the
[1452.28 --> 1455.66]  design and the thought behind the language do you do you have anything else you want to say about
[1455.66 --> 1457.86]  just the motivation and the theory behind dart
[1457.86 --> 1466.80]  i'm just super happy being able to write in dart so i think it's really cool that i get to come to
[1466.80 --> 1471.98]  work and work on something that actually makes me happier to build for the web so that i feel like
[1471.98 --> 1477.72]  that's a win yeah for sure so let's talk a little bit about the language itself um can you kind of give
[1477.72 --> 1483.86]  me some i don't know like obviously there this is hard to summarize in a few you know sentences because
[1483.86 --> 1487.86]  i'm sure a lot of thought went behind this but but can you give me some some of the insight into
[1487.86 --> 1491.50]  like the thought behind the language and and what the process looked like to figure out you know the
[1491.50 --> 1499.10]  syntax of the language and all that well first of all we have to um to say that the only way to get
[1499.10 --> 1504.64]  a successful language is to to include curly braces so that was the first thing oh and semicolons
[1504.64 --> 1512.30]  and semicolons yes of course of course um and then secondly we uh we knew from the beginning that
[1512.30 --> 1518.30]  it had to be translated to javascript and that uh uh sort of was a challenge because some of the
[1518.30 --> 1522.86]  language feature we wanted to have into the language we could not put in because they would not translate
[1522.86 --> 1528.86]  to efficient javascript so the design process was uh sort of very iterative in in coming up with a
[1528.86 --> 1534.22]  feature that matched the language and then implement and see how it would look in in javascript one thing
[1534.22 --> 1541.10]  uh or a feature we didn't put in we wanted to have but we could not make efficient on top of javascript
[1541.10 --> 1547.18]  was non-local returns as you probably know from small talk it's a way to bail out from a recursive
[1547.18 --> 1552.30]  algorithm very quickly but in javascript you could only implement that by throwing exception
[1552.30 --> 1557.66]  and that was really slow on most implementations yeah yeah one thing that i found really fascinating
[1557.66 --> 1563.18]  when i talked to the co-founders and some of the other vm uh developers for dart is the difference in
[1563.18 --> 1570.86]  how how vm design impacted the language design so maybe lars like when you you helped build v8 and you
[1570.86 --> 1575.98]  you took the javascript language which is very flexible uh and but you but you ultimately made
[1575.98 --> 1582.06]  it very fast how did that experience help us design the dart language so that the implementations can be
[1582.06 --> 1590.62]  fast well javascript is very flexible uh if you try to access a property that's not there you return
[1590.94 --> 1596.78]  an undefined if you if you set a property that's not there you will expand the object with a new
[1596.78 --> 1604.94]  property and so in order to make a v8 fast we had to design for a sweet spot kind of application
[1605.90 --> 1611.58]  and the problem with that is that if you from the side create a new library and you poke at a few
[1611.58 --> 1617.10]  objects suddenly the application would be slow so one of the design goals of dart was also to make sure
[1617.10 --> 1623.18]  that we had an execution model that would be robust when it came to performance right so you can actually
[1623.18 --> 1628.46]  trust that if you had a performance library it will continue to be robust no matter how you used it
[1629.90 --> 1636.46]  so one of the impacts of that is dart has classes and the dart program is declared and then when the
[1637.18 --> 1641.98]  virtual machine you know scans it and then parses it and then compiles it that's the structure of the
[1641.98 --> 1647.18]  program and you can know that that is the structure so the vm can more quickly more easily and more
[1647.18 --> 1653.42]  efficiently optimize that program we basically borrowed the the the optic model from small talk
[1654.70 --> 1661.02]  so a very simple optic model where in a class you define the the fields you want to have for the
[1661.02 --> 1669.34]  instances and but you cannot expand it at one time so fields have to be declared and the same way if you
[1669.34 --> 1678.30]  have a non-global array and you access a fear an element outside the range you get an exception instead of
[1678.30 --> 1684.94]  expanding the array so it's more rigid than than small talk in some sense on the other hand you also
[1684.94 --> 1691.18]  you get notified if you do something wrong like in javascript if you do if you if you have a spelling error
[1691.18 --> 1697.66]  what happens is the program continues to run but it doesn't behave the right way in dart you'll be notified
[1697.66 --> 1704.38]  you try to access something that's not there so we talked a little bit about how flexible javascript
[1704.38 --> 1709.98]  is and that's a kind of a double-edged sword right like it's it's neat and it's nice because it allows
[1709.98 --> 1715.34]  me to do a lot but it also makes it very easy for like developers to make mistakes and in a lot of ways
[1715.34 --> 1720.70]  because well for a few reasons i would imagine right the first is obviously that uh in order to compile
[1720.70 --> 1726.06]  dart down to javascript like it's it's a lot easier when dart is more restrictive than javascript to be able
[1726.06 --> 1731.02]  to compile to javascript and the other way is it's a lot harder it seems like to make mistakes in dart
[1731.02 --> 1735.34]  in the classical way that that you can make mistakes in javascript can is it was that was that part of
[1735.34 --> 1742.30]  the thought process behind some of the restrictions in dart uh clearly because uh if we want to support
[1742.30 --> 1748.54]  programming in the lot right it's very important for a programmer that he can write a piece of code and be
[1748.54 --> 1754.94]  fairly certain that it will work against the other libraries in the project so certainly having having a
[1754.94 --> 1761.98]  tool chain that will check that the way you use the system is valid is important for big programs so
[1761.98 --> 1769.58]  that was part of the design criteria and also in javascript not only properties for normal
[1771.02 --> 1777.10]  fields can be added but you can also change the functionality as you go along at one time so for
[1777.10 --> 1782.38]  instance if you want to swap two functions in the library of javascript you can do that without
[1783.18 --> 1788.46]  getting notified but the program doesn't behave the right way in dart we have decided that the
[1789.34 --> 1793.50]  libraries are declared and class are declared that means that when you first stop running
[1793.50 --> 1798.70]  they will stay the same functional from the beginning of the program execution to the end and that also
[1798.70 --> 1807.42]  means that you'll not get a problem with conflicts in javascript you can have monkey patching and if two
[1807.42 --> 1813.58]  libraries that are monkey patching a core object you can get into a sort of interesting behavior
[1815.82 --> 1821.42]  so uh one thing i want to bring up just kind of as another little aside here you've you've mentioned
[1821.42 --> 1825.18]  what the first thing you mentioned was that uh obviously it had to have curly braces because you
[1825.18 --> 1829.98]  know it's impossible to have a successful language without them and you've talked a lot about the influence
[1829.98 --> 1835.34]  small talk the small talk had on dart uh one of my co-workers said he thinks it's reasonable
[1835.34 --> 1839.26]  to describe dart as small talk with curly braces totally before this show in the same way that
[1839.26 --> 1844.70]  javascript is you know scheme with curly braces uh how how do you feel about that statement that's a
[1845.50 --> 1849.82]  i'm honored if if that's a statement because small talk is one of these languages that are
[1850.86 --> 1855.98]  very minimal and elegant uh so if he thinks we are close to that i'm very happy
[1857.50 --> 1864.14]  we try to have a very simple execution model we think that if you have a simple execution model it's much
[1864.14 --> 1869.10]  easier for the programmer to understand what's going on when he runs the program for instance if you go
[1869.10 --> 1874.14]  into a debugger and do a single step we want the people to be fully aware of what's going on
[1875.50 --> 1881.82]  and by having simple semantics like you mentioned before that that variables are staying in the scopes
[1881.82 --> 1888.46]  that are cleared in like we have a clean lexical scoping it's much easier to understand what's going on in
[1888.46 --> 1898.38]  in these cases and we think this is a the more comfortable the programmer is with the execution of
[1898.38 --> 1903.66]  a program the more experimentation he does and the more innovation and i think that makes him a better
[1903.66 --> 1908.94]  programmer or her a better programmer yeah it's almost like the flexibility of javascript in some
[1908.94 --> 1916.38]  ways can prevent you from from being too um uh too experimental because you're afraid of what of the
[1916.38 --> 1920.86]  unknown consequences right like with dart you know exactly what you're going to get uh it's very
[1920.86 --> 1924.86]  predictable and so it's it's a little bit easier to like try and experiment without worrying about
[1924.86 --> 1929.26]  you know impacting the rest of the large project you're working on so the other flip side oh go
[1929.26 --> 1935.90]  ahead lars i just one short comment before seth um so um i've used a many different programming
[1935.90 --> 1942.14]  languages but one thing that's interesting with dart is that i get the same feeling as when i program in
[1942.14 --> 1948.46]  small talk in the old days you want to make the program better so often you you write your class
[1948.46 --> 1954.06]  and you start experimenting with it making it smaller and denser and better that feeling as a programmer
[1954.06 --> 1959.42]  is very powerful it makes you make the program look good and it also makes it more robust going forward
[1961.26 --> 1966.30]  so you mentioned experimenting and maybe like features of language make it easier or harder this is
[1966.30 --> 1971.58]  something i think dart's done pretty well at least at least for me and i think it's really critical for a
[1971.58 --> 1976.38]  language of the web that is when you start a web project you might have a very small little script
[1976.38 --> 1981.02]  you know no type annotations probably just some functions and then you hit reload in your browser
[1981.02 --> 1984.30]  and then you see it you see it pop up right there you're like wow that was really cool and then you
[1984.30 --> 1988.86]  might add another couple functions and you hit reload you wow and before you know it you're actually
[1988.86 --> 1994.30]  experimenting and trying out the platform you're building up a mini little app and dart allows you to
[1994.30 --> 2000.22]  start way at that beginning where you just have some functions and reload but it helps you grow over time
[2000.22 --> 2005.34]  and scale up to when you're actually ready to add some classes and then you're ready to add maybe a
[2005.34 --> 2010.62]  library and then you maybe you're ready to add type annotations and so from an experimenting point of
[2010.62 --> 2017.10]  view i actually find dart easier because i can start as early as i want in that kind of scope or scale but i
[2017.10 --> 2021.98]  can keep going and keep going and keep going and i don't sort of collapse under my own weight and also due to
[2021.98 --> 2029.58]  that structure of things like classes and libraries and ultimately packages and interfaces and that you
[2029.58 --> 2036.54]  know all that great stuff um the experimenting of becomes even easier in the ecosystem because i can
[2036.54 --> 2041.50]  build on top of the structure other people build and so i don't need to put something out into the
[2041.50 --> 2046.06]  community and hope it doesn't monkey patch and sort of step over somebody else's stuff for so for
[2046.06 --> 2053.66]  experimenting i actually think dart is really really productive awesome yeah true let me ask you a
[2053.66 --> 2058.62]  question here i'm just reading through one of your faqs which by the way if you are listening to this
[2058.62 --> 2063.74]  show and you have any interest in dart whatsoever go to the website and just like read through the faqs
[2063.74 --> 2067.74]  and the and the different things about the language it's a it's a this is one of the best things i think
[2067.74 --> 2074.62]  dart has done so this is our bullet plate for the show i think i mean this this uh faqs list yeah i mean
[2074.62 --> 2080.14]  it's incredible reading through this and just being able to uh to easily see kind of the evolution of
[2080.14 --> 2085.10]  the language as well as like the the the differences but one of the things that i'm looking for and i
[2085.10 --> 2088.70]  haven't really been able to find because these have to exist right there there has to be some sort
[2088.70 --> 2093.18]  of gotchas for for javascript developers that are coming to dart it can't just be all you know like
[2093.18 --> 2099.02]  butterflies and flowers like there has to be something here that's like if you typically do uh this in
[2099.02 --> 2103.50]  javascript this will catch you up here do you know of any kind of common pitfalls or gotchas that that
[2103.50 --> 2109.42]  javascript developers might experience coming to dart well it's clear that we don't we don't we don't
[2109.42 --> 2116.22]  have eval so if if you are big on uh getting text strings converted into code and execute on the fly
[2116.70 --> 2122.22]  i think it's a problem in dart because we have decided to make it much more structured for various
[2122.22 --> 2130.14]  reasons and so that's certainly something you have to get used to but other than that yeah there
[2130.14 --> 2135.26]  doesn't seem to be a bunch which seems like uh like a pretty awesome thing but it you wonder if
[2135.26 --> 2140.06]  there is there a catch you know what i mean well we've run numerous hackathons internally to the
[2140.06 --> 2146.86]  company externally the company we had a recent global dart flight school program which we ran and uh so i've
[2146.86 --> 2152.14]  seen it numerous times people are up and running in dart in about an hour and they come from all different
[2152.14 --> 2158.46]  backgrounds and this is one of the reasons i really uh really like this project is because it it is so
[2158.46 --> 2163.26]  approachable i've seen high school students um some of their first programming experience in these
[2163.26 --> 2168.38]  hackathons have a web page built and i've seen people with years and years of java years and years
[2168.38 --> 2174.30]  of action script years and years of javascript all all get up and running so uh at least in my experience
[2174.30 --> 2179.42]  it's it's very approachable and familiar and there's not really a lot of those gotchas based on your
[2179.42 --> 2185.42]  other language because job um because dart says okay we've learned a lot of great lessons we're making this a
[2185.42 --> 2191.26]  a familiar approachable experience so let me let me ask you that one of the what i believe is
[2191.26 --> 2196.38]  probably the best lesson that uh dart learned and and i mean wow looking at the kind of the
[2196.38 --> 2202.62]  implementation here is like querying the dom and you know anyone anyone who was around before jquery
[2202.62 --> 2207.42]  knows like querying the dom in javascript was an absolute nightmare and then when jquery came along
[2207.42 --> 2211.26]  you're like oh wow i can query it based on these selectors and it's like so much easier and everything
[2211.26 --> 2216.78]  makes sense and i look at the dart you know how dart queries it on there's there's two succinct
[2216.78 --> 2221.82]  methods to query the dom and that's all you have to worry about oh it gets even better uh what is
[2221.82 --> 2228.06]  returned to you are actual iterables uh and so you no longer have like array like things or arrays
[2228.86 --> 2234.62]  because of that rich core library that we have that you get out of the box with dart you've got lists
[2234.62 --> 2240.38]  and arrays and sets and maps and iterables and once you have that core library then the other
[2240.38 --> 2244.94]  libraries like the html library get to use those as well so if you know dart programming
[2244.94 --> 2250.38]  then you know web programming so i don't even know if people are going to be able to function
[2250.38 --> 2255.82]  knowing that i mean when i start building something for the web like step one is get all your javascript
[2255.82 --> 2259.50]  requirements and one of those is jquery like how are people going to even know how to get started
[2259.50 --> 2262.70]  without having to go out and download the latest production build of jquery
[2262.70 --> 2272.14]  i guess we could yeah i guess skip that step yeah i'm not embarrassed that it's too easy
[2274.70 --> 2283.58]  so i think we should we should mention again that that dart has a very comprehensive basic library
[2284.06 --> 2291.26]  that's very cool we have for asynchronous programming you have futures and streams and that's a very
[2291.26 --> 2298.06]  consistent way of doing asynchronous programming and we have all these collection types that really fit
[2298.06 --> 2305.74]  well together so i think if people are used to a programming language where you have a a good self
[2305.74 --> 2312.70]  libraries like if you come from java or c sharp that is actually very interesting to look at for web
[2312.70 --> 2318.70]  programming and and because of the fact that yeah these futures which are sort of like promises in a sense
[2318.70 --> 2325.34]  and javascript are baked into the core platform all the other packages out in the dart ecosystem use
[2325.34 --> 2331.42]  all these same core primitives so there's no more like which one of these do i use just everyone uses
[2331.42 --> 2336.46]  futures for the one-shot callbacks and streams for the repeating callbacks and it just propagates the
[2336.46 --> 2341.58]  ecosystem and it's just another one of those decision points that the community doesn't have to debate and
[2341.58 --> 2346.62]  developers don't need to reinvent so everyone can kind of take a step up in terms of what they get to work
[2346.62 --> 2350.46]  on and contribute back and it's just it's helped everyone be so much more productive
[2352.38 --> 2357.42]  let's pause the show for just a minute give a shout out to our sponsors new relic if you've got a web
[2357.42 --> 2363.90]  or mobile application you need to know about new relic it's your new best friend basically it's your easy to use
[2364.30 --> 2371.58]  analytics dashboard that basically gives you powerful code level visibility into the real-time performance of your application so
[2371.58 --> 2378.70]  this means that you can spot bugs see bottlenecks and fix problems fast hopefully before they even affect your users
[2379.18 --> 2384.38]  and thanks new relic you no longer have to ship your app to production and then helplessly wait around
[2384.38 --> 2390.54]  hoping for the best until negative app reviews and tweets start to roll in new relic empowers you to
[2391.10 --> 2397.26]  to see what's going on and what's what is working and what isn't working all around time and the way it works is really straightforward
[2397.26 --> 2403.74]  they give you a lightweight agent that you unpackage into your production level apps that agent sits around
[2403.74 --> 2409.50]  quietly and securely in the background kind of gathering real-time metrics across geographies devices
[2409.50 --> 2416.22]  platforms all the way down to the end user level and then displays all that data in real-time graphs
[2416.22 --> 2422.06]  so coders can have the visibility they need into the performance of their web applications and make everything awesome
[2422.06 --> 2427.74]  awesome so go and check out new relic today by visiting new relic.com slash the changelog to learn more
[2427.74 --> 2435.02]  and use the offer code the changelog and take advantage of this special 30-day extended free pro trial
[2436.06 --> 2440.86]  available exclusively to our listeners new relic.com slash the changelog
[2442.62 --> 2447.34]  so i think there are like some obvious questions that people will probably have one of them is is um
[2447.98 --> 2451.90]  what does google use dart on right now that that you can kind of share with us
[2454.14 --> 2461.10]  sure uh we have an internal sales tool that uh this this is a great story um it's sort of sort of like
[2461.10 --> 2465.66]  the widow maker project in a sense that they've tried to re rebuild this system a bunch of times and you
[2465.66 --> 2470.70]  know legacy software right there's a bunch of decisions made and um and they try to rebuild rebuild it and then
[2470.70 --> 2479.82]  uh recently uh they they did a full rewrite in dart and angular dart and delivered the project on time
[2479.82 --> 2486.38]  and blew away everyone's expectations and now that's a successful deployment we also have other apps like
[2486.38 --> 2491.98]  google elections has a really neat app to help track elections around the world and numerous other
[2491.98 --> 2498.22]  internal tools that we're not quite ready to to share yet but there's a page on our site called who uses dart
[2498.22 --> 2504.86]  that references some internal and a bunch external as well awesome so there are so there are some
[2504.86 --> 2509.42]  external uh can you kind of kind of allude to some of those that that without having to go to the site
[2509.42 --> 2514.70]  here oh sure so uh one of my favorite is this company called soundtrap and what i really like
[2514.70 --> 2519.58]  about them is not only do they use dart but they also use some of the really cool new html5 features
[2519.58 --> 2526.94]  like web rtc which is real-time collaborative communication and some of the media stuff like get user media
[2526.94 --> 2534.22]  and audio and video so they built a collaborative music authoring uh app with dart and web rtc so it's
[2534.22 --> 2541.66]  such a cool thing another great story is a startup called blossom and i like i like their story because
[2541.66 --> 2549.66]  they were originally on javascript and uh let's see backbone and they over time gradually their users
[2549.66 --> 2554.46]  didn't even know it started swapping out some of their components for dart components and so that that
[2554.46 --> 2558.38]  was really cool to show that yes you can take an existing javascript app and if you like what dart
[2558.38 --> 2565.66]  has to offer you don't need to rewrite the whole thing you can do it piecemeal awesome so yeah i mean
[2566.86 --> 2571.10]  yeah i don't have much to say to that other than the fact that this is obviously something that is
[2571.10 --> 2576.94]  going to continue going in that direction and i think that that's a that's a good thing so just to
[2576.94 --> 2583.18]  even though we are from google and our only objective with this project here is to make people more
[2583.18 --> 2590.30]  efficient at doing web applications so everything is open and we are very receptive to to feedback so
[2590.30 --> 2596.38]  we can make it better so if people are trying it out and they have problems in an area we would like
[2596.38 --> 2602.06]  to hear the feedback so we can make the system solve that problem one thing i notice here is that
[2602.86 --> 2609.10]  similar to go uh you don't actually see any google brands on the dart website that's obviously a uh
[2609.10 --> 2616.30]  uh on purpose correct that's right it's an open source project it's for the web the spec itself
[2616.30 --> 2622.94]  is in the ecma process now um it's it's no secret that googlers work on the project but like a lot of
[2622.94 --> 2630.78]  other successful projects for the web it really is for and of the community so the the million dollar
[2630.78 --> 2636.30]  question and and we kind of talked about this a little bit before um but but how do you know that you've
[2636.30 --> 2641.74]  for lack of a better term how do you know that you've won with dart like when do you feel like
[2641.74 --> 2648.86]  okay you've gotten to a point where dart is is here to stay when every developer is building for the
[2648.86 --> 2655.02]  modern web on mobile devices and uh i don't think we can get there without something toolable and
[2655.02 --> 2665.18]  productive like dart yeah so um yeah that's a good answer but this the um so it bottoms out to that
[2665.18 --> 2672.30]  uh we will continue to innovate to make sure the web uh the web platform gets better and better over
[2672.30 --> 2677.58]  time uh getting success with the programming language is is hard because people have to like
[2677.58 --> 2683.34]  it they have to like the feel of it when they type in the code at this point it looks really good the
[2683.34 --> 2689.34]  projects we've seen working working with dart they like it and it's growing right now the community both
[2689.34 --> 2696.30]  inside our company and also outside so we have been around we've been working on this for three years
[2696.30 --> 2704.54]  success uh is coming i think it looks pretty good if we have the same uh growth over the next two years
[2705.10 --> 2712.14]  i would be really really happy because just having the competition going means that even other web
[2712.14 --> 2717.18]  programming language they will might learn something from what we did in dart and that will lift the whole
[2717.18 --> 2723.34]  industry hopefully so it's certainly an idea that we can we can make everything better not only the
[2723.34 --> 2729.58]  dart system yeah you get the feeling that that one of the goals of dart is not just to like catch up
[2729.58 --> 2734.14]  and be where web programming is now but but one of the goals of dart is to move web development forward
[2734.14 --> 2738.54]  and i think that's that's a pretty good and you know ambitious but but also one that's necessary
[2738.54 --> 2744.06]  here i don't know if we should go back and talk about v8 but that's sort of the same with the v8 project
[2744.06 --> 2750.14]  uh when we started out uh there was not a lot of javascript code being executed because it was very
[2750.14 --> 2757.42]  slow and and you basically have to have look into the future and figure out what do people want in the
[2757.42 --> 2764.62]  future when it comes to executing javascript and we decided that the more speed you have the more
[2764.62 --> 2771.18]  innovation the application developers would go for and that's also what happened and in the process
[2771.18 --> 2779.42]  all the other browsers got fast javascript engines as well and i think that's great yeah
[2780.30 --> 2785.98]  that's that's one of the things about um i don't know about javascript about the current state of
[2785.98 --> 2790.06]  browsers right now is you'll see these ships of browsers and it'll be like you know some javascript
[2790.06 --> 2796.06]  uh efficiency some some performance increase but but that kind of almost feels like it's plateauing to
[2796.06 --> 2800.94]  a to a degree where like the the major like you said the the the benefits you got when like v8 started
[2800.94 --> 2805.50]  coming and things like that were like were much bigger gains than the ones you're seeing right now
[2805.50 --> 2811.42]  um does dart follow that same trend or or you know obviously dart is young so there's a lot of
[2811.42 --> 2816.46]  performance increase to come in the future but but you're not plateauing now or there are from ship
[2816.46 --> 2822.54]  to ship are they are they major efficiency increases that you're seeing that is getting faster and faster with
[2822.54 --> 2830.38]  each release uh we're doing and we are focusing on it and uh because start is more structured than
[2830.38 --> 2836.94]  uh then as we mentioned with javascript uh you would see that over time that uh dart will get the same
[2836.94 --> 2847.42]  kind of performance as uh as java basically except for if you're doing a hardcore um double computation
[2847.42 --> 2853.66]  uh yeah but that's not our goal but for ordinary uh object-oriented programs we should approach that
[2853.66 --> 2860.46]  kind of speed so we're aiming high uh but you'll see performance improvements over at least the next few
[2860.46 --> 2869.50]  years uh yeah no no plateauing in sight yeah you heard it here first we're going to have a web development
[2869.50 --> 2877.10]  that is as fast as system programming that's a good thing so speaking about performance the the last
[2877.10 --> 2881.98]  release we had 1.3 really focused on server-side performance one of the questions we get all the
[2881.98 --> 2887.18]  time is is there a node for dart i think developers like what they see but they know they have to write
[2887.18 --> 2891.34]  some server code and client code and so they want to know can they do dart on the server and so the
[2891.34 --> 2897.98]  answer is a resounding definitely uh we the virtual machine runs on the command line uh just like you
[2897.98 --> 2904.38]  know ruby or python or or v8 and you can get access to files and directories sockets there's a built-in
[2904.38 --> 2909.82]  web server built-in web sockets ssl and we've recently turned our performance attention over
[2909.82 --> 2915.74]  to the server side story as well so the story is looking really good awesome oh yeah we since it's
[2915.74 --> 2921.18]  a language project we also have to say that our internal tools are mostly written in dart so the
[2921.18 --> 2929.50]  dart to js compiler is of course written in dart and also the analyzer nice so for people that are just
[2929.50 --> 2934.46]  getting started what's the what's the recommended way to to to do just that to get started with dart
[2935.34 --> 2943.74]  on the website uh there is a one hour code lab uh called try dart and uh you build up your pirate name
[2944.62 --> 2948.78]  but it's really great it walks you through the features of the the language it walks you through
[2948.78 --> 2952.86]  some web programming and yeah just about an hour you're gonna have a working dart app
[2952.86 --> 2962.78]  so the website is dartlang.org okay awesome i think obviously i mean it's an entire ecosystem
[2962.78 --> 2967.50]  it's not just a language we can sit here and talk about it for for a long time and and i would love to
[2967.50 --> 2972.22]  uh to do just that but we try and keep the show down to about an hour so i i have a feeling that this
[2972.22 --> 2976.54]  is going to be one that we're going to want to to have another show on in the future to see where it goes
[2976.54 --> 2981.34]  um but but for now i want to give you guys an opportunity anything else that you want to kind of
[2981.34 --> 2984.46]  to mention about dart for for the people to hear before we move on
[2987.98 --> 2994.70]  well the uh we hope that people try it out and give us their opinion and and hopefully it's a good
[2994.70 --> 3003.10]  one um that's pretty much it we'll continue to work hard on making it better over time um so that's
[3003.10 --> 3009.18]  pretty much it i think it's it's very hard to convince people to use another language over the radio
[3009.18 --> 3014.22]  uh people have to try it out and have to feel the program is to figure out if something they can be
[3014.22 --> 3020.94]  productive in so it's a very personal uh kind of decision what's the recommended way to to give
[3020.94 --> 3029.02]  feedback is it through the uh the mailing list or you can file a file an issue uh on the issue tracker or
[3029.02 --> 3036.46]  you can send an email to to the mailing list that'll be answered i'd love to ask all developers who are
[3036.46 --> 3043.26]  interested in dart to go check out pub.dartlang.org that's our hosting site for packages and you'll
[3043.26 --> 3048.38]  find a tons of great stuff in there from the community um and when when you're building for the
[3048.38 --> 3053.82]  web don't forget that uh the trends are very clear that everyone's moving to mobile i know i sound like a
[3053.82 --> 3060.14]  broken record here but if uh if i have to tell anyone anything it's um develop and test on mobile
[3060.14 --> 3064.38]  phones and tablets for your great web stuff because that's where your users are and and we think dark
[3064.38 --> 3071.02]  can help you do that awesome so okay great so we we ask our uh our guests the same uh set of questions
[3071.02 --> 3075.10]  at the end of every show and i want to go ahead and ask you all these questions so i'll ask lars first
[3075.10 --> 3079.18]  and and you kind of both answered this first one already but and just in case there's anything else
[3079.18 --> 3086.54]  uh do you have like a call to arms for the community um yes my call to arms is that innovation
[3086.54 --> 3091.34]  is important and programmers have to be flexible and try out new stuff to see if they're more
[3091.34 --> 3096.78]  efficient using a different platform there than they used in the past so try out that and and
[3097.66 --> 3103.50]  see if it's more efficient and set anything from you other than uh building mobile stuff i'll be
[3103.50 --> 3109.10]  really specific about it in dev tools you can turn on mobile emulation so my call to arms is
[3109.10 --> 3113.74]  when you develop on your desktop and you're you're in chrome or dev tools turn on mobile emulation
[3113.74 --> 3118.38]  and just always live with that uh that little window there gotcha
[3120.46 --> 3125.98]  the second question here is um if you weren't doing this what would you be doing and i'll ask you first
[3125.98 --> 3133.18]  seth uh probably doing something around education or teaching i'm really inspired by the uh the mooc the
[3133.18 --> 3137.42]  the online classes and courseware stuff and so i don't know i think i think that'd be pretty interesting
[3137.42 --> 3145.26]  gotcha and for you lars oh i need more spare time i am i would travel the world uh on a bike
[3146.22 --> 3148.62]  um well you can only travel part of the world on a bike
[3150.70 --> 3150.78]  yeah
[3150.78 --> 3159.02]  but i think i get on a plane at some point or a boat that that is true but uh half a year on the bike
[3159.02 --> 3164.86]  would be great for me uh but i always have so i've tried it before and it never works so
[3164.86 --> 3170.94]  um i would say if i don't do that i would probably do another language or vm project nice
[3172.94 --> 3178.06]  and lars um for a programmer hero or just somebody that's been hugely influential in your life
[3179.26 --> 3185.90]  oh i have to mention my old professor ole lehmann masson uh he was the uh co-designer of the beta
[3185.90 --> 3193.50]  programming language a successor to similar 67 if you remember that uh he's been very inspirational in
[3193.50 --> 3197.90]  pushing me to do languages and and virtual machine implementation all the way back in the
[3198.78 --> 3205.82]  mid 80s so that's he's probably the main reason why i'm um doing it still that's awesome and seth
[3206.70 --> 3212.46]  i gotta say uh neil degrasse tyson the scientist and educator is just really inspiring to me because
[3212.46 --> 3218.46]  that's someone who clearly knows what he's doing and talking about but is so passionate and inspirational
[3218.46 --> 3224.06]  with how he delivers that stuff to to the world so i really enjoy watching him i've actually been
[3224.06 --> 3228.86]  waiting for the day for somebody to mention him as their hero because he's he's uh he's been a
[3228.86 --> 3233.58]  personal hero for many that i've known and he's with the new show recently obviously it's really good
[3233.58 --> 3238.30]  so people are really enjoying his method of teaching kind of comes from his own predecessor too
[3238.30 --> 3250.06]  yeah nobody said anything to that no no love for adam no love for adam i've been listening to this
[3250.06 --> 3253.66]  show i mean this is one of those shows where i wanted to kind of jump in but i feel like i don't
[3253.66 --> 3258.70]  add a ton i wanted to kind of dig in a bit more about the pub package manager but uh we can save that
[3258.70 --> 3265.18]  for a different show i'm sure yeah yeah so anything else you guys want to mention here before we go ahead
[3265.18 --> 3273.02]  and close out the show uh just thanks for inviting us um we need to to get everybody to listen in on
[3273.02 --> 3278.70]  what that is all about so um we are just happy to be here yeah i really appreciate the opportunity i
[3278.70 --> 3284.38]  remember uh the changelog is always one of those podcasts that is on the top of my queue and for a
[3284.38 --> 3289.74]  long time now so it's it's kind of an honor to be on the show so thanks well it's an honor to have
[3289.74 --> 3294.78]  you guys so what so i just wanted to absolutely yeah so i wanted to once again just say thanks to
[3294.78 --> 3300.38]  lars and seth for joining us on today's show like like we kind of kind of alluded to uh dart is a
[3300.38 --> 3307.18]  is a big project and um it's hard to to do any project the size of dart you know justice in a 45
[3307.18 --> 3312.46]  minute to an hour radio show uh so i just want to encourage just like they were saying to encourage
[3312.46 --> 3316.78]  anyone if you're interested in this whatsoever just head over to the website it's it speaks for
[3316.78 --> 3321.26]  itself and it's something that uh you can just start hacking on in your own time and and really i mean
[3321.26 --> 3326.46]  just with the small amount of time i've spent on it just to kind of learn it and stuff it's been a uh
[3326.46 --> 3331.18]  it's been a pleasant experience something worth checking out worth hacking on i think it's uh
[3331.18 --> 3336.54]  definitely something we will want to consider uh talking about more on this show in the future but
[3336.54 --> 3341.58]  uh once again i just wanted to say thanks a bunch for joining us and and that's it for this week uh
[3342.22 --> 3347.26]  just for the listeners if you have not subscribed to the changelog weekly it is our weekly email where we
[3347.26 --> 3353.02]  share everything that hits our open source radar you can subscribe at the changelog.com weekly
[3353.98 --> 3360.70]  and um we will be back next week i don't think we know the uh guest yet adam so we will save that as
[3360.70 --> 3366.46]  a super the guest is still pending yes you're right yeah yeah so until next week though let's say goodbye
[3367.02 --> 3368.54]  all right bye-bye thank you
[3377.26 --> 3383.58]  you
