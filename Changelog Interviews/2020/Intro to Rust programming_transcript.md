[0.00 --> 7.40]  what is up everyone adam stuchowiak here editor-in-chief of changelove we teamed up with
[7.40 --> 12.28]  some friends of ours over heroku to promote their podcast called codish you can check it out at
[12.28 --> 17.80]  heroku.com slash podcasts slash codish check the show notes for links to that show and how to
[17.80 --> 22.76]  subscribe and today we're dropping a full-length episode of codish into the changelove's feed
[22.76 --> 28.66]  this episode features chris castle and special guests carol nichols and jake goulding and they're
[28.66 --> 31.78]  talking about the strengths of the rust programming language here we go
[31.78 --> 45.14]  hello and welcome to codish an exploration of the lives of modern developers join us as we dive
[45.14 --> 50.54]  into topics like languages and frameworks data and event-driven architectures and individual and
[50.54 --> 55.94]  team productivity all tailored to developers and engineering leaders this episode is part of our
[55.94 --> 64.64]  deeply technical series hello welcome to codish i'm chris castle heroku developer advocate and this
[64.64 --> 70.56]  episode is all about the rust programming language rust is often categorized as a systems programming
[70.56 --> 76.16]  language but it's really much more capable than that and you can see rust is being used to build
[76.16 --> 82.98]  web applications command line interfaces re-implement javascript libraries in web assembly when performance
[82.98 --> 89.06]  more performance is needed and even for programming memory constrained embedded devices and because of
[89.06 --> 94.66]  this flexibility and a host of other reasons rust is gaining in popularity quickly i did a quick review of
[94.66 --> 102.10]  the results of various developer surveys out there like red monk and tayobe t-i-o-b-e and they showed rust as
[102.10 --> 108.86]  one of the fastest growing languages by number of developers and even stack overflow's developer survey has listed rust
[108.86 --> 115.48]  as the most loved programming language for four years running but personally i found rust interesting
[115.48 --> 121.76]  because it has made low-level programming more accessible to me i never learned c or c plus plus
[121.76 --> 127.76]  when i learned to program 20 years ago started in java and went to ruby and node and python and rust has kind of
[127.76 --> 134.02]  shown me that i can write lower level code but still kind of have this like human friendly developer
[134.02 --> 139.88]  experience or user experience for sure rust has a steeper learning curve than ruby or node or python
[139.88 --> 145.04]  but it's tooling it's documentation it's community and learning resources out there have made learning and
[145.04 --> 154.02]  learning it a delightful experience and that brings me to today's guests joining me are carol nichols and jake golding
[154.02 --> 160.74]  who've contributed much to the rust community thanks for for joining me carol and jake welcome can you uh
[160.74 --> 167.38]  let's start with carol can you give us a little intro about yourself i'm carol nichols i am the co-author
[167.38 --> 175.14]  on the rust programming language book i got interested in rust i used to do ruby and i got interested in
[175.14 --> 181.68]  rust because i was working a lot on improving ruby performance and there's a point you get to
[181.68 --> 189.44]  when you really have to to make ruby go faster you have to drop in to c but i'm terrified of c
[189.44 --> 199.86]  and yeah same yeah around that time uh steve klabnick who was and is still a uh luminary in the ruby world
[199.86 --> 205.30]  he just kept talking about this brand new language called rust and how awesome it was so and he actually
[205.30 --> 211.52]  wrote a book called rust for rubius and i was like oh cool i can do this and i started checking out and
[211.52 --> 220.74]  it was a way to write faster low resource usage code without the seg faults and the memory problems
[220.74 --> 227.90]  and uh use after free and and all the problems that come with c and i was like oh this is this is just
[227.90 --> 235.72]  what i need and i started sending steve a lot of pull requests for his book and that actually
[235.72 --> 242.68]  eventually led into me co-authoring the rust programming language book with steve which is
[242.68 --> 248.82]  kind of like the canonical rust learning resource is that correct yeah we're trying to be yeah it's
[248.82 --> 254.56]  it comes with every rust installation the book is on your computer with installed with rust uh you can
[254.56 --> 260.14]  also buy a dead tree version uh from no starch press it's not it's not completely comprehensive
[260.14 --> 265.62]  because rust is a really big language but it's aiming to get you productive in rust uh and give
[265.62 --> 271.48]  you what you need to be writing most rust code so what about you jake what is your your background and
[271.48 --> 276.44]  kind of entrance into the rust world so i kind of came at it from the other direction from carol uh
[276.44 --> 285.66]  my first big job was a lot and a lot of c code and a little bit of uh java a little bit of ruby as
[285.66 --> 290.34]  well and when i was introduced to ruby i was amazed like this language is so nice to write
[290.34 --> 296.18]  compared to c but i always had that thing in the back of my head where oh but what am i giving up
[296.18 --> 304.80]  by switching to ruby and i was introduced to rust through carol and i kind of just took to it immediately
[304.80 --> 311.08]  i was like this is great this is a wonderful high level language that it's it allows you to express ideas
[311.08 --> 319.28]  concisely but you still get a lot of performance you have that ability of writing that hardcore c
[319.28 --> 325.56]  programmer code but you don't have to give up the things that you normally have to give up when you
[325.56 --> 333.56]  choose to write c or c plus plus code so that really just kind of rang true for me and because of my
[333.56 --> 339.84]  background i see a lot of similarities of kind of a fusion of c and ruby and obviously there's a lot of
[339.84 --> 346.90]  other influences and in rust but to me those two things are kind of like a beautiful marriage and
[346.90 --> 354.10]  rust is kind of the offspring there yeah that's cool so and and carol mentioned um she and and steve
[354.10 --> 358.92]  are kind of the co-authors of the rust book um but you also have some kind of pretty pretty major
[358.92 --> 366.12]  contributions to the rust community um what are some of those yeah so whatever it is about my brain
[366.12 --> 373.84]  i really enjoy answering questions and so um when we started with rust it was about rust 0.13 i think
[373.84 --> 380.42]  and at that point in time there was not a lot of content for it on stack overflow and i kind of saw
[380.42 --> 384.88]  my chance i said you know i can get in at the ground floor i can learn a bunch of things by answering
[384.88 --> 392.32]  questions and i might be slightly addicted to answering questions definitely addicted um it has
[392.32 --> 397.92]  i saw your little your little pink kirby character at the top of the list yeah uh so i'm the number one
[397.92 --> 404.86]  answerer on uh stack overflow for all things rust related and it's really been great for me because
[404.86 --> 411.64]  i've learned a lot but hopefully i've also helped a lot of other people learn things and uh through that
[411.64 --> 417.88]  one of the tools that i end up using the most there is taking people's code and testing it and so i
[417.88 --> 423.18]  would copy and paste a lot of that into the rust playground at the time and over time i kind of
[423.18 --> 427.64]  how carol started contributing pull requests to the book i started saying oh well this part of the
[427.64 --> 431.26]  playground needs to be better and this part needs to be better and i actually ended up re-implementing
[431.26 --> 436.42]  it and then now i'm the maintainer of the rust playground but yeah to back up a little bit the
[436.42 --> 444.44]  playground is uh play.rust-lang.org and it's a website where you can just type in some rust code and then
[444.44 --> 448.18]  send it off to a server that runs it and then spits the output back so you don't have to have
[448.18 --> 452.80]  rust installed to be able to try yeah and you can like share links to programs and things like that
[452.80 --> 458.62]  yeah big goal of it is to make it so that people who are interested in rust can very easily see what
[458.62 --> 464.94]  rust is kind of see how the compiler interacts with you and be able to try some things out it's
[464.94 --> 470.64]  obviously a great resource for people trying to report bugs or just communicate ideas but in my mind
[470.64 --> 476.10]  one of its biggest goals is to make rust really accessible to people who want to try it and don't
[476.10 --> 481.26]  want to spend the 10 minutes to install it or whatever it takes so that's great uh interesting
[481.26 --> 487.68]  stuff that you used to work on in the rust world what is uh kind of the the current big rust project
[487.68 --> 493.34]  that you're working on in rust land so we've got two things that we've been working on currently one is
[493.34 --> 500.38]  the rust belt rust conference this will be our fourth year it's going to be in dayton ohio on
[500.38 --> 507.74]  october 18th and 19th uh tickets are on sale now so we live in the rust belt in pittsburgh and we like
[507.74 --> 514.84]  showing off that there is technology stuff going on in the rust belt we're no silicon valley or new york
[514.84 --> 520.80]  city or anything like that but there are a number of us here and there are benefits to being in the
[520.80 --> 528.84]  rust belt so we've we've had a conference in pittsburgh columbus ann arbor and this year is dayton so we'd love
[528.84 --> 534.34]  to have any of your listeners join is for any levels of rust knowledge jake is actually giving
[534.34 --> 540.40]  an intro to rust workshop on the first day yeah we've done a few conferences over the years and
[540.40 --> 546.56]  that's always been a strong component of them is an attempt to make them very accessible to first-time
[546.56 --> 551.74]  conference goers as well as people who don't even necessarily know the language i think you had one
[551.74 --> 556.54]  more thing that that you guys are working on right now right a pretty kind of a kind of a big project
[556.54 --> 563.42]  that that you've been working on to uh for for rust and rust education yeah so the second thing we've been
[563.42 --> 573.40]  working on is the rust in motion video series for manning it's a video learning course that we're aiming
[573.40 --> 580.60]  to uh get you up to speed on the parts that make rust the most different from most other programming
[580.60 --> 586.90]  languages so the topics we cover in the course that we think make rust the most different we do a unit
[586.90 --> 595.58]  on kind of syntax and basic things things like variables are immutable by default in rust and the
[595.58 --> 603.66]  way you call functions and have structs and the second unit is on ownership and borrowing which is a huge
[603.66 --> 613.52]  difference with rust that very few languages make an explicit first class idea and what this is is
[613.52 --> 620.50]  that in rust there's one owner of every piece of data and when that owner goes out of scope
[620.50 --> 627.86]  then the data gets automatically cleaned up so this this is the part of rust that lets you
[627.86 --> 633.56]  not have to have a garbage collector running while your code is running and cleaning up after you
[633.56 --> 640.32]  and also not have to manually think about where you should call free like you have to see which
[640.32 --> 647.88]  everyone gets wrong and leads to problems like psych vaults and use after freeze and things like that
[647.88 --> 655.68]  and borrowing is how you can the owner can let other parts of code use that data without
[655.68 --> 662.40]  taking over the responsibility of cleaning it up most languages don't have that there are some that do
[662.40 --> 669.74]  c and c plus plus have concepts of ownership and borrowing and then the thing that rust adds on top
[669.74 --> 676.42]  of that that is basically unique to rust there's a few research languages is this concept of lifetimes
[676.42 --> 684.10]  where the compiler checks and make sure that the way that you're using this borrowed data is always
[684.10 --> 691.08]  valid you're never going to get into a case of memory on safety where you've borrowed something and
[691.08 --> 697.34]  then it's been cleaned up like the the compiler make sure that you aren't doing that so all borrows must
[697.34 --> 703.36]  be shorter than the lifetime of the actual data you're borrowing so i've i'm mostly most of the
[703.36 --> 708.60]  way through the rust book i'm actually on is it lifetime annotations is that the correct name
[708.60 --> 715.08]  yeah yeah so chapter 10 yeah yeah that sounds about right i'm at the point where my i feel like my brain is
[715.08 --> 721.74]  full or needs like more exercises or things like that so i'm kind of uh excited to check out rust in
[721.74 --> 727.82]  motion and maybe a few other things to kind of like layer on top of the the my work through the rust book
[727.82 --> 734.88]  so far one of the goals with rust in motion was to cover this different stuff because we've watched a
[734.88 --> 741.86]  lot of people who are good at picking up new programming languages are used to just being able to pick a
[741.86 --> 747.80]  programming language pick up the docs and kind of start typing and get into rewriting their favorite
[747.80 --> 754.72]  problem and be off and running with rust they try and do that same thing and they hit this brick wall
[754.72 --> 759.72]  and they kind of freak out because you really have to stop and think and understand what the borrow
[759.72 --> 764.60]  checker is doing and what it's protecting you from and what it's telling you with the error messages
[764.60 --> 769.34]  there's been a lot of work put into the error messages and so i think sometimes people are
[769.34 --> 774.00]  don't read the error messages because they're used to error messages not being helpful but
[774.00 --> 779.20]  when rust they're actually really great right i think that even those super helpful messages like
[779.20 --> 783.16]  even if you don't know or if you don't know the terms in that super in that error message it still is
[783.16 --> 787.58]  you're still going to struggle a bit if you don't know what lifetimes mean or ownership means yeah
[787.58 --> 792.14]  carol used the phrase and it's a common one i'm in among the community of fighting the
[792.14 --> 797.02]  borrow checker i understand it i'm always a little disappointed by that choice of words because like
[797.02 --> 801.50]  the truth is it is the compiler is attempting to help you it's trying to say hey this thing that
[801.50 --> 806.90]  you are attempting to do could introduce security vulnerabilities to your code hey this thing you're
[806.90 --> 813.64]  trying to do might you know crash in production you don't want to do that and it's really it is like
[813.64 --> 819.60]  you're having a nice well-reasoned discussion uh with the compiler with your pair your pair
[819.60 --> 825.14]  programmer right and it just they're they're always right they're right 99 of the time but the vast
[825.14 --> 828.84]  majority of the time they're right which can get a little annoying yeah they're really trying to
[828.84 --> 837.24]  help yeah um jake you mentioned the rust community um and there's a fun word or name that's used to
[837.24 --> 841.52]  describe the rust community um do you know is there do either of you know if there's like a story
[841.52 --> 846.46]  behind that or so what is the word first of all and is there a story behind where the um the name
[846.46 --> 852.48]  came from uh the word is rustation and it's a kind of like crustation without the c
[852.48 --> 861.14]  our fun mascot is ferris the crab who is a rustation um i'm not really sure of the origins of
[861.14 --> 867.12]  it i think we were just looking for a fun name and someone suggested it and then someone drew a cute
[867.12 --> 873.24]  crab and there we are so speaking of the the community and and kind of other users what are
[873.24 --> 881.62]  some examples of kind of interesting uses of rust or like rust in production in maybe big deployments
[881.62 --> 888.86]  or maybe like innovative or or unique or interesting ways so the most obvious example of rust in
[888.86 --> 894.28]  production is through mozilla it's in the firefox browser and it's the most obvious because mozilla is
[894.28 --> 901.28]  a huge sponsor of rust rust came out of mozilla research yeah and if you remember two years ago when
[901.28 --> 909.56]  firefox released firefox quantum and that was the first public release that had rust as part of the
[909.56 --> 916.50]  browser that everyone was running at that point in time and you know they integrated rust into the
[916.50 --> 922.50]  it's called stylo it's the part that parses the style sheets and deals with styles inside the browser
[922.50 --> 929.18]  and they were able to be very free about using references and especially using references in
[929.18 --> 936.40]  multi-threaded context and because of that they were able to get pretty sizable speedups in that portion
[936.40 --> 941.44]  of firefox now firefox still has quite a lot of c and c plus plus code so it's not by any means all rust
[941.44 --> 948.26]  but the pieces that they have been able to port to rust have gotten really sizable and noticeable gains
[948.26 --> 955.46]  as you spend many years as a software developer speed is great and like delivering that thing the first time
[955.46 --> 962.16]  is great but then maintainability is always a concern a question and can be a big problem if it's not kind of
[962.16 --> 970.20]  planned or thought about what is or how do people talk about kind of the maintainability story with with rust
[970.20 --> 978.40]  i compare to c plus plus it's way better um a big part of that i think is cargo which is uh the build
[978.40 --> 985.98]  management and package manager of rust which lets you add dependencies really easily way more easily than
[985.98 --> 994.14]  in c plus plus so that lets you break your program into lots of little components which can be easier
[994.14 --> 1002.52]  to maintain than one big monolith and i think the compiler being a constant kind of pair to everyone
[1002.52 --> 1007.58]  who works on the code base i've heard this anecdote from a lot of companies is that more junior developers
[1007.58 --> 1012.62]  are you can trust them to write rust because the compiler is always checking that you don't have to
[1012.62 --> 1019.26]  review their code quite and frankly with more senior developers too like you don't have to review
[1019.26 --> 1026.12]  the code quite so carefully you can review it for like logic problems which is still very possible in
[1026.12 --> 1032.84]  rust but as far as like the memory things and security vulnerabilities and and seg faults and crashes
[1032.84 --> 1039.44]  that sort of thing the compiler so if it compiles then you know the compiler has checked all of those things
[1039.44 --> 1048.24]  so it it makes it a lot easier to bring more people in and more people over time because the compiler is that
[1048.24 --> 1054.16]  constant in and it really helps out and to add on what carol was saying about crates there like rust
[1054.16 --> 1060.98]  definitely is on that side of let's push a lot of stuff into the ecosystem and there are some people that are
[1060.98 --> 1067.10]  not big fans of this concept uh my go-to example for this that always kind of surprises people is rust
[1067.10 --> 1072.30]  the standard library does not have any mechanisms for generating random numbers random numbers is
[1072.30 --> 1078.54]  actually offloaded to a i'll say third-party crate it's a crate that's maintained by people that are
[1078.54 --> 1084.30]  close to the core ecosystem of rust but still it's just a crate that is distributed on crates.io
[1084.30 --> 1090.20]  there's been a lot of work recently in futures for example with rust and all of that work
[1090.20 --> 1098.34]  has mostly been in the third-party ecosystem so there's a lot of do lots of little things uh some
[1098.34 --> 1105.22]  of the work from firefox like there's a url crate and i'm pretty sure that that came out of the firefox
[1105.22 --> 1110.38]  work because they're like you know what everybody needs urls and we are really good at urls because we
[1110.38 --> 1116.06]  do web browsers so they're like let's make that public and that's part of that community there is
[1116.06 --> 1123.12]  trying to share and trying to have good quality and that's helped i think with maintenance as well
[1123.12 --> 1128.30]  just because people are cognizant that this is something that we do we try to make good quality
[1128.30 --> 1133.64]  crates that people can use yeah so that's cool i do actually i want to talk more about crates.io but i
[1133.64 --> 1140.36]  but before that i want to hear some more examples of other companies or other kind of interesting uses
[1140.36 --> 1147.44]  of of rust um because i think we like me in the in the intro in the beginning and and um you and i
[1147.44 --> 1154.48]  have chatted uh about clis and like embedded devices and all these other different different uses for rust
[1154.48 --> 1159.84]  and i'm curious to uh hear hear about some other examples of how those things are being built or who
[1159.84 --> 1167.28]  is building those things yeah so a lot of the the big and tech companies are using rust in some
[1167.28 --> 1172.48]  projects uh amazon recently announced their firecracker micro vm which is written in rust
[1172.48 --> 1179.28]  google is using rust for their fuchsia operating system which they're still kind of secretive about
[1179.28 --> 1186.34]  what they're doing with it but it's open source so you can like go see it semi-stealth yeah so you can
[1186.34 --> 1190.94]  see that it's written in rust but we're still not sure what they're doing with it um facebook is using
[1190.94 --> 1196.32]  rust for a number of projects they've written a mercurial server in rust that can handle their
[1196.32 --> 1203.26]  humongous monorepos they recently announced libra their their blockchain uh cryptocurrency
[1203.26 --> 1211.32]  is written in rust and actually a a fun trivia fact there was recently a congressional hearing
[1211.32 --> 1218.16]  where a representative asked an executive from facebook about why they were using the nightly rust
[1218.16 --> 1223.94]  compiler and what features they needed the nightly compiler for and which is this is like a very
[1223.94 --> 1230.80]  technical detail and so this came up in congressional testimony because that because they are related
[1230.80 --> 1238.84]  to using rust on libra which is aiming to be like a global currency uh rust has proven to be a pretty
[1238.84 --> 1247.00]  strong case for blockchain in general there's quite a few projects that are fairly large and fairly
[1247.00 --> 1253.88]  mature with regards to blockchain technology so i think that's a very interesting thing about rust
[1253.88 --> 1258.14]  actually i thought you were going to say um i thought you were going to mention something
[1258.14 --> 1265.40]  about like web assembly because is visual studio code still an electron app um which is written in
[1265.40 --> 1270.74]  javascript to my knowledge it is yeah i thought you were going to say they they re-implemented the search
[1270.74 --> 1276.46]  in rust to to make it speedy can you speak a little bit more do you know of any examples of um
[1276.46 --> 1283.68]  uh like useful and real examples of rust and web assembly and javascript being used
[1283.68 --> 1289.06]  the most real one that i'm aware of and i don't know exactly where they are in the the process
[1289.06 --> 1297.64]  is um the frame ember framework has at its core it's called the glimmer engine i believe
[1297.64 --> 1305.24]  and it's kind of a diffing algorithm and that that is a piece of that library that is a hundred percent
[1305.24 --> 1311.78]  like needs to be performant it's at the core it doesn't touch like any dom really it's all
[1311.78 --> 1319.18]  pure data structurey um i know that there was a lot of effort to get that in rust and then
[1319.18 --> 1326.18]  compiled the web assembly i don't know exactly how far they are on that um obviously with with a
[1326.18 --> 1330.92]  library like that you're going to have the issue of web assembly is a newer technology and so if you
[1330.92 --> 1336.72]  start making that decision then you have to have some amount of fallback capability for
[1336.72 --> 1343.04]  uh all the people who may not have a web assembly enabled browser for whatever reason yeah i haven't
[1343.04 --> 1349.98]  done too much web assembly myself but um rust is one of the few languages that can target web assembly
[1349.98 --> 1357.68]  if you have a choice of what to write your web assembly and i i would highly suggest considering rust
[1357.68 --> 1364.48]  but in general web assembly is a really exciting technology if people out there had have seen uh gary
[1364.48 --> 1371.02]  bernhardt's javascript talk i'm not sure if you're familiar that's not that's different from the
[1371.02 --> 1378.60]  wat talk right yes yes it's a it's a different talk where he predicts that uh the browser will become
[1378.60 --> 1384.84]  the operating system and you kind of run everything within the browser and that's kind of what web
[1384.84 --> 1391.68]  assembly is doing so he kind of predicted web assembly in this like joke talk where he mispronounces
[1391.68 --> 1398.32]  javascript it's incredible one other thing is that um even though it's called web assembly the actual
[1398.32 --> 1404.94]  virtual machine there is uh cross-platform and conceptually can be used for lots of different
[1404.94 --> 1411.12]  things so i've actually also heard of uh there's a linux kernel i believe a module that allows you to
[1411.12 --> 1416.72]  write web assembly that then gets run inside of the kernel um i think some of the blockchain
[1416.72 --> 1425.54]  technologies as well actually use web assembly as kind of their base layer for when you're writing
[1425.54 --> 1432.16]  blockchain based applications they actually get compiled down to web assembly so it's not necessarily
[1432.16 --> 1438.16]  web assembly is not only the browser it obviously has web in the name but it is an assembly language
[1438.16 --> 1441.90]  and can be used in lots of different contexts is it the new jvm
[1441.90 --> 1449.56]  that is i've heard something like that because the idea is you know you've got a set of assembly
[1449.56 --> 1456.44]  mnemonics that fit and there are interpreters that you can run it this time this time we'll really make
[1456.44 --> 1463.90]  something cross-platform well let's jump back to rust and the cargo utility and crates um and specifically
[1463.90 --> 1469.62]  like crates.io which is a project that you're one of the maintainers of carol is that right
[1469.62 --> 1478.14]  yeah yeah so crates.io is kind of like the npm js or the rubygems.org of the rust world it's the package
[1478.14 --> 1485.00]  registry website for open source packages um the back end is written in rust the front end is ember
[1485.00 --> 1492.80]  um and it runs on heroku nice that's cool uh so many people probably don't know that you can run
[1492.80 --> 1499.14]  rust on heroku um rust is i guess it's not one of heroku's officially supported languages
[1499.14 --> 1506.40]  no it's not we have to use an unofficial build pack so maybe maybe heroku can get on that soon
[1506.40 --> 1512.64]  since so many other cool people are using it maybe you can join us join heroku and help be the dedicated
[1512.64 --> 1519.80]  language engineer that makes deploying rust on heroku a smooth process it's pretty smooth even with the
[1519.80 --> 1526.28]  unofficial build pack because the build pack like installs rust gets the right version then calls cargo
[1526.28 --> 1531.78]  which downloads all your pack actually this part is really meta because when we build a new version
[1531.78 --> 1540.82]  of crates.io it downloads the packages from crates.io uh and then builds them and then uh into into a
[1540.82 --> 1546.14]  single executable or actually we have multiple executables but the main server is one executable
[1546.14 --> 1551.38]  and then we have a bunch of utilities and then you just kind of run that executable and then your
[1551.38 --> 1558.70]  server is running is that using any uh popular rust web framework and if so like what is well i guess
[1558.70 --> 1564.08]  in general what are some of the advantages of using uh rust for an application like this versus using
[1564.08 --> 1572.00]  say python or node or ruby or go because rust is so young there isn't like a rails for rust yet there
[1572.00 --> 1579.16]  isn't like one good web framework yet there's lots of like pieces of web frameworks being worked on and
[1579.16 --> 1585.60]  different ideas being experimented with crates.io is probably one of the first uh web applications
[1585.60 --> 1592.18]  written in rust so it doesn't it uses this framework that i don't think anyone else uses and no one else
[1592.18 --> 1600.50]  should use because it was pretty much written for crates.io and it's not even i wouldn't even call it a
[1600.50 --> 1608.84]  framework it's like barely a small layer over uh the network code stuff so but there are
[1608.84 --> 1614.14]  a bunch of different web frameworks that are kind of yeah different stages of maturity and different
[1614.14 --> 1622.44]  levels of use one of the the most popular ones is called rocket um it has a pretty amazing
[1622.44 --> 1628.40]  developer experience when you're using it its biggest downside right now is because the maintainer
[1628.40 --> 1635.92]  really wants to have such a wonderful developer experience that they require usage of rust's nightly
[1635.92 --> 1640.98]  builds because there are features that they want to use that are not yet stabilized there's a couple other
[1640.98 --> 1648.74]  big ones so the rust playground uses uh the iron framework there's another one uh if you've heard of the
[1648.74 --> 1655.72]  tech empower benchmarks rust tends to place pretty highly in those and one of the ones that does really well
[1655.72 --> 1663.52]  there is called actics web which is an actor-based framework built on top of another library called actics
[1663.52 --> 1671.84]  with the recent stabilization and continuing stabilization of futures and async await i think
[1671.84 --> 1679.30]  there's going to be a big renaissance in web frameworks and people are looking for things to try
[1679.30 --> 1685.26]  trying these new ideas like carol mentioned experimenting to figure out exactly you know what style works best
[1685.26 --> 1691.46]  with rust code a lot of the existing frameworks have copied ideas from other languages which is a great
[1691.46 --> 1697.72]  place to start but then you need to explore within how idiomatic rust code works and how does it work
[1697.72 --> 1702.58]  in a strongly typed language versus a dynamically typed language and what is just the right way of putting
[1702.58 --> 1708.08]  together these types of apps so i think there's a lot of that experimentation still going on yeah so if
[1708.08 --> 1717.56]  you're looking for like a a real easy smooth kind of rails experience i would wait for writing a web app in rust
[1717.56 --> 1726.40]  today if you are excited by experimentation and trying new things and maybe you want to try writing your own and
[1726.40 --> 1735.04]  maybe you want to try writing a piece of like rails is made up of so many gems so there's a opportunity for
[1735.04 --> 1744.82]  writing a piece of what might become the rust web framework so that sort of thing excites you this is a great time to
[1744.82 --> 1753.16]  get in and try and experiment what is i think in the rust book the first like bigger maybe like non-trivial
[1753.16 --> 1761.62]  thing that you have the readers create is a cli is that correct yeah the uh mini grep project yes yeah
[1761.62 --> 1770.62]  it seems like clis are a good fit for rust um not just in general but kind of in in the state that rust is
[1770.62 --> 1775.80]  is at right now also are there any clis that we would like i would or others would recognize
[1775.80 --> 1784.24]  that are built in rust so rip grip is one right yep zola is a static site generator that's written
[1784.24 --> 1790.92]  in rust oh yeah yep i think i saw that okay there's like a lot of little ones the reason that rust is a
[1790.92 --> 1797.24]  great fit for this is it's uh cross-compiling capabilities whereas if you wrote a command line
[1797.24 --> 1802.36]  tool in ruby because it's interpreted you would have to make sure that the person you're sending
[1802.36 --> 1810.02]  the tool to has a compatible ruby version installed whereas with rust you can cross-compile and then just
[1810.02 --> 1817.28]  hand off the binaries yeah which we kind of alluded to earlier with deploying of crates io but rust is a
[1817.28 --> 1823.58]  everything gets statically linked at build time and so when you have this thing it is just a single
[1823.58 --> 1828.12]  executable that you're very likely to be able to pass around and uh i've heard some from people
[1828.12 --> 1834.46]  who were writing kind of some smaller tools for like their own companies and they were like i actually
[1834.46 --> 1838.88]  just checked it out on windows and it built the first time and i didn't ever think about it until
[1838.88 --> 1846.54]  somebody asked if there was one to download so like that's a really powerful ability now i mean you can
[1846.54 --> 1853.00]  opt into platform specific things and say well i want to make use of something linux specific or mac os
[1853.00 --> 1857.40]  specific or windows specific and then obviously you have to deal with that at some point but
[1857.40 --> 1865.94]  rust right the standard library is fairly cross-platform and most libraries except for ones that are specific
[1865.94 --> 1871.50]  to a platform tend to be pretty good at being cross-platform as well speaking of cross-platform
[1871.50 --> 1879.28]  and cross-compiling yeah rust is also good for uh writing code for embedded devices oh right yeah jake's
[1879.28 --> 1885.80]  actually done way more of that i mean so i've played with like arduino and uh these this little
[1885.80 --> 1894.00]  device called the esp8266 and uh esp32 that has wi-fi stuff um are any of those devices compile
[1894.00 --> 1899.72]  targets i guess or the processor on those compile targets for rust so the biggest one right now
[1899.72 --> 1906.60]  generally when people kind of say embedded in rust they're talking about the cortex m3 arm processor
[1906.60 --> 1914.86]  that's pretty much the best target right now for rust um to me like that chip ends up being a little
[1914.86 --> 1922.52]  bit more than embedded it's got all this space it's got all this you know abilities um i'm interested in
[1922.52 --> 1929.68]  arduino like you mentioned using the avr processor yeah unfortunately right now uh so rust is built on top
[1929.68 --> 1937.06]  of llvm and llvm doesn't actually have great support for those chips and so i'm actually part of a project
[1937.06 --> 1944.88]  that when i in my copious free time i try to help where they are um supporting that inside of llvm with
[1944.88 --> 1952.76]  the intent of getting it into rust and so you know every few months we update the compiler and try things
[1952.76 --> 1958.22]  and figure out where new bugs are but that's that's my end goal as well i think the same thing is kind of
[1958.22 --> 1963.18]  true for the esp that you mentioned i think llvm support for it is not super great and i think
[1963.18 --> 1969.24]  there's another parallel group of people who are working on getting that support as well as getting
[1969.24 --> 1976.96]  support in rust for it uh it's funny because most of the the work is all in llvm like basically the
[1976.96 --> 1981.70]  amount of work inside of rust to support in your platform at least for the ones that i've seen has
[1981.70 --> 1988.12]  been very minimal it's basically tell it what llvm settings to use and you're 90 of the way
[1988.12 --> 1994.18]  there i mean one thing that seems interesting too is like i sometimes think of of uh raspberry pi
[1994.18 --> 2000.78]  is like not embedded kind of cheating embedded um because you get this whole linux environment or os
[2000.78 --> 2006.94]  to work in but it seems like a 35 raspberry pi um still has constrained memory like you're still
[2006.94 --> 2011.34]  limited to a gig or or actually i guess two or four gigs now with the new raspberry pi of fours
[2011.34 --> 2017.40]  but you know they have gpio pins and people do very often use them in projects that are are kind
[2017.40 --> 2023.50]  of more associated with embedded work but it seems like that's that thing still has constrained resources
[2023.50 --> 2030.72]  and so using rust on for those types of projects would still still be valuable and useful um in using
[2030.72 --> 2038.00]  constrained memory but also efficiently using that cpu that's on the raspberry pi yeah and when when you
[2038.00 --> 2043.36]  start to get into the beefier hardware like you're talking about there are some operating system
[2043.36 --> 2051.52]  projects in rust the most well known is called redox but uh there's actually a really great uh tutorial
[2051.52 --> 2058.28]  about creating your own operating system in rust the person producing is called fill up and i forget if
[2058.28 --> 2063.20]  that's their online name or their actual name but you know you could do something like that with the
[2063.20 --> 2068.54]  raspberry pi where you basically you are the entire operating system you know that's the best way of
[2068.54 --> 2073.18]  getting as much memory as you can right is you don't let anything else run whatsoever but yeah
[2073.18 --> 2079.46]  like uh one of the other benefits of using rust for a web service there's some of the white papers on
[2079.46 --> 2085.26]  the rust website talk about this but there's web services that were written in java using eight
[2085.26 --> 2089.66]  gigabytes of memory or something like that and it was rewritten in rust and now they take on the order
[2089.66 --> 2096.52]  of like 50 or a couple hundred megabytes of ram just through the you know ability that you get and
[2096.52 --> 2102.46]  so like that kind of thing would also apply on something like the pi just you'll be able to make
[2102.46 --> 2108.48]  much more efficient use of your memory and those resources and even on even on heroku like i used to
[2108.48 --> 2114.44]  work for a company that ran a rails app on heroku and like there was just a base amount of memory that
[2114.44 --> 2120.96]  rails always needed and we would hit memory limits and we'd have to bump up to bigger dinos and
[2120.96 --> 2126.18]  and with crates.io like i just i sometimes just look at our graphs of memory usage and i laugh
[2126.18 --> 2132.90]  because it's just so tiny compared to what a rails app uses the the stat there is that you actually pay
[2132.90 --> 2141.08]  more for logs for paper trail for for storing our logs than we do for dinos wow yeah so you can
[2141.08 --> 2147.88]  save learn rust save money so we've talked about some things that rust is is good for what are what
[2147.88 --> 2154.98]  are some examples that rust is not a good fit for so i i think rust isn't great for prototyping
[2154.98 --> 2161.56]  and just writing something real quick that you just want to run once or twice or you know you're doing a
[2161.56 --> 2170.26]  demo or you're trying out an idea and then you're going to rewrite it real for production later like maybe
[2170.26 --> 2176.56]  ruby or python yeah excel in that area if you're going for pure development speed and if you want
[2176.56 --> 2183.16]  to ignore the things that the compiler is trying to help you remember um then then rust will get in
[2183.16 --> 2189.80]  your way a little bit i think it's it's good and i i do use rust to prototype because often prototypes
[2189.80 --> 2196.96]  end up in production um but it can get in your way i think rust also has kind of that chicken egg
[2196.96 --> 2203.56]  thing going on right now like you know if you want to do some machine learning right like hands down
[2203.56 --> 2208.86]  basically people are going to use something based on top of python and a bunch of under the hood tools
[2208.86 --> 2215.66]  and so if you want to do that in rust right now it may not be pragmatic yeah the ecosystem is
[2215.66 --> 2221.22]  definitely still growing in a lot of areas so it there might not be like in ruby and javascript and
[2221.22 --> 2226.14]  python like there's probably a library out there that will do what you want to do there's probably 10 of
[2226.14 --> 2232.42]  them in rust there might be half of one we'll get there right it's still early it's always driven by
[2232.42 --> 2237.34]  somebody who says you know it's almost there if i just put in that little bit of work to get the
[2237.34 --> 2242.72]  next thing or wow if i wrote this in rust then i'd get all this other benefits let's go ahead and bite
[2242.72 --> 2249.76]  the bullet you know there's genomics companies out there who are like you know we can process that
[2249.76 --> 2256.36]  much more data if we do rust more pervasively than what we're currently doing let's go ahead and try
[2256.36 --> 2261.66]  and get some of that ecosystem out there let's go ahead and you know encourage some of these create
[2261.66 --> 2268.92]  authors to expand on this or that yeah and and like if you if your code is working if it's if you have
[2268.92 --> 2272.28]  code written in some other language it's working it's doing what you need to do it's making you money
[2272.28 --> 2278.20]  absolutely do not rewrite it in rust i want to be very clear about that there are people who go around
[2278.20 --> 2285.70]  saying everything should be rewritten in rust we disagree with that um when when rust benefits
[2285.70 --> 2292.64]  would be useful to you we encourage you to look at rust and and there are uh foreign function
[2292.64 --> 2298.24]  interfaces that can help you incrementally rewrite in rust because wholesale rewrites are always risky
[2298.24 --> 2303.62]  don't use it just for the sake of using it have a have a reason to use it we talked about a few
[2303.62 --> 2309.74]  learning resources um but what are some other resources or kind of what's a what's a good path
[2309.74 --> 2313.64]  you would you would share with someone who's interested in learning more about rust um and
[2313.64 --> 2319.16]  potentially learning to be proficient in the language yes so we talked about uh the rust program
[2319.16 --> 2325.38]  language book uh there's also programming rust is the o'reilly book and i've heard there are uh good
[2325.38 --> 2329.60]  compliments to each other so if one doesn't quite resonate with you the other one might
[2329.60 --> 2336.80]  rust in motion video course if you like video learning more than that if you like trying out
[2336.80 --> 2343.88]  code and and learning while you code there's rust by example uh is an official resource there's also
[2343.88 --> 2349.16]  exorcism which gives you little programming problems to try and that you submit for review
[2349.16 --> 2354.76]  which is good for lots of languages but there's also a rust track i started a project a long time ago
[2354.76 --> 2360.96]  that i've since kind of passed on to the community called rustlings and it's lots of little pieces of
[2360.96 --> 2367.22]  rust code that intentionally don't compile to give you that practice of reading compiler messages and
[2367.22 --> 2372.90]  trying to fix them so so you're given this code that's broken and your job is to figure out a way to fix it
[2372.90 --> 2377.70]  i like that it's easier it's always easier to like jump into yeah solving problems than to starting with
[2377.70 --> 2383.36]  that like blank page that you have to start writing from there's also um the rust cookbook is kind of
[2383.36 --> 2391.12]  trying to be like i want to parse the url in rust how do i do that and so it gives you kind of a little
[2391.12 --> 2398.44]  recipe of how to do common tasks like that for the different areas like uh the embedded and web assembly
[2398.44 --> 2407.30]  there are books just for those areas um so documentation has always been something really important to the
[2407.30 --> 2412.82]  rest community um we're really proud of the work that's gone into documentation and that we see
[2412.82 --> 2419.78]  documentation as a first class citizen as an artifact that we need to produce or else like the the
[2419.78 --> 2424.76]  technical if you can't explain how to use something it doesn't matter how technically great it is so
[2424.76 --> 2431.40]  um we take documentation very seriously and touching on that like yeah we talked a little bit about cargo
[2431.40 --> 2437.22]  and that's actually part of cargo you know it's a build tool it's a dependency management tool it's also
[2437.22 --> 2443.36]  a test runner and it's a documentation build tool and that's all been there since rust 1.0 like these are
[2443.36 --> 2449.60]  all things that we take seriously and we say there needs to be documentation there's actually a lint that
[2449.60 --> 2457.46]  you can add in the compiler that will fail your builds if your public api is not documented and that's
[2457.46 --> 2465.34]  something you opt into but it is not unusual to see that in well-regarded crates one thing that i
[2465.34 --> 2471.70]  remember looking for is um idiomatic rust like i knew it had i wanted to solve some little problem
[2471.70 --> 2477.78]  but i kind of just wanted like a little bit of a nudge or guidance as to like what is the rust way
[2477.78 --> 2483.36]  to do this um and then not only do i know it for that thing but i can also kind of then repeat that
[2483.36 --> 2489.80]  pattern in other places that are similar do you know of any good resources of things like that or
[2489.80 --> 2495.94]  maybe rustlings is a good resource for that rustlings i feel like i mostly wrote those to be broken so i
[2495.94 --> 2502.80]  don't know if i'd look to that for okay don't follow those um but there is the clippy tool uh which is
[2502.80 --> 2510.12]  named after microsoft's clippy it's a set of of lints that are not appropriate for the compiler for a
[2510.12 --> 2517.14]  variety of reasons um but it will do things like encourage idiomatic code it does fun things like
[2517.14 --> 2522.58]  if it notices you've written a floating point number that's awfully close to pi it'll be like
[2522.58 --> 2529.36]  hey the standard library has this constant for pi you might want to use that instead so it has a lot
[2529.36 --> 2537.68]  of hints and nudges and uh checks for things like that and and it can often teach you about uh rust
[2537.68 --> 2544.82]  patterns that you don't know about in the realm of idiomatic style there's also um a rust format
[2544.82 --> 2553.74]  tool there's a community agreed upon general style for rust and rust format enforces that by default
[2553.74 --> 2559.78]  it is one of the configurable tools so if you are strongly opinionated that it needs to be two spaces
[2559.78 --> 2564.44]  instead of four spaces or tabs instead of four spaces like it's the kind of thing you can change but
[2564.44 --> 2571.04]  i've been pleased to see that most people who use it tend to stick basically to the defaults
[2571.58 --> 2575.28]  um which gives a really nice ability to read a random piece of rust code and
[2575.28 --> 2579.60]  not have to jump all over with your eyes and that's something that i understand is
[2579.60 --> 2584.46]  a touchy subject to a lot of people you know that's my code style don't touch it but
[2584.46 --> 2587.64]  i'm i'm appreciative that there's mostly a standard
[2587.64 --> 2594.10]  cool well uh thanks for thanks for joining us for the codish podcast um i just wanted to i'll
[2594.10 --> 2600.30]  mention rust in motion uh your video series video learning series again and we'll have more details
[2600.30 --> 2606.40]  about that in the show notes are you guys still working working on that rust in motion um it looked
[2606.40 --> 2612.40]  like it's like it's ready to be to be used and consumed by people but it's also still like changing
[2612.40 --> 2617.66]  and expanding over time is that correct we've finished the the first draft of the content um
[2617.66 --> 2623.80]  it's still in manning's early access program so it still might change a little bit but all the all
[2623.80 --> 2631.14]  the content is now there cool well thanks for very much for joining us on codish carol and jake and uh
[2631.14 --> 2637.10]  also if you want to check out carol and jake's video series the rust in motion video series to learn
[2637.10 --> 2646.98]  rust uh we've got a 40 off coupon code here it's podish 19 p-o-d-i-s-h 19 all one word all lowercase
[2646.98 --> 2652.86]  uh so yeah check that out it'll actually get you 40 off on anything from manning publications who
[2652.86 --> 2660.06]  they partnered with for the video series thanks for joining us for this episode of the codish podcast
[2660.06 --> 2666.30]  codish is produced by heroku the easiest way to deploy manage and scale your applications in the cloud
[2666.30 --> 2673.82]  if you'd like to learn more about codish or any of heroku's podcasts please visit heroku.com slash podcasts
