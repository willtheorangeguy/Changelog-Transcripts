[0.00 --> 16.24]  welcome back everyone this is the changelog and i'm your host adam's dakowiak this is episode 171
[16.24 --> 22.92]  and on today's show we're joined by karen meyer the author of living closure she's also known
[22.92 --> 28.54]  as gigasquid on twitter github and pretty much everywhere else on the interwebs she's speaking
[28.54 --> 33.70]  soon if you're gonna be at strange loop talking about chemical computing a very interesting
[33.70 --> 39.32]  conversation we had on this show today she's also the author of babar a little language for machines
[39.32 --> 46.40]  with speech acts we have three awesome sponsors for the show today code ship imagix and digital
[46.40 --> 51.70]  ocean our first sponsor for the show today is code ship launching a brand new feature called
[51.70 --> 56.96]  organizations you've heard me mention it before now you can create teams set permissions for your
[56.96 --> 62.96]  teams and improve collaboration in your delivery workflows maintain centralized control over your
[62.96 --> 68.60]  organization's projects as well as your teams with this brand new feature and we want you to save 20
[68.60 --> 75.66]  that's huge off any premium plan for three months by using this code the changelog podcast again that
[75.66 --> 82.56]  code is the changelog podcast head to code ship.com slash the changelog to get started and now on to the show
[82.56 --> 95.26]  all right everybody we're back today we got karen meyer uh jerry we set up this call through twitter
[95.26 --> 101.72]  how crazy right it's crazy world out there crazy world so what was going on to invite karen onto the
[101.72 --> 110.08]  show probably just my interest in closure and um i came across karen i guess i came across her on the
[110.08 --> 115.22]  top pod podcast over the summer at some point nice shout out to them and then somebody retweeted her or
[115.22 --> 120.86]  something like that and i said oh that face is familiar and then i checked her bio i was like oh
[120.86 --> 126.30]  she should come on and talk to talk to us about closure and that was kind of the genesis of it well i'm
[126.30 --> 130.64]  happy to be here very gracious of you to respond so quickly and be so willing to come on we appreciate
[130.64 --> 136.40]  it yeah absolutely so karen i guess maybe an easy way to start would be i think your bio says a bit
[136.40 --> 142.40]  about you being starting in ballet and then physics and then ultimately in software development but
[142.40 --> 148.72]  when someone asks you kind of who you are what's your response yeah well i i usually just say i'm a
[148.72 --> 158.12]  i'm a closure developer um because that's what i i do every day and i quite enjoy it and um yeah i guess
[158.12 --> 165.56]  that pretty much just sums it up i got to it from a very windy path uh like many people uh so i started
[165.56 --> 171.06]  um i was professional ballet dancer for a couple years right out of high school
[171.06 --> 179.36]  and that was really cool and i really uh enjoyed it except for uh the starving artist bit which got
[179.36 --> 185.28]  a little bit old like sleeping on floors with mattresses and cockroaches and things like that
[185.28 --> 193.54]  so i decided maybe going going to college would be a good idea very pragmatic choice exactly so when i was
[193.54 --> 202.78]  in um high school i i really i liked physics and math and in particular i had a really nice role model
[202.78 --> 208.30]  um for my physics instructor she was an awesome woman and so i was super impressed with her and
[208.30 --> 213.60]  there was this one moment that i always remember in physics that kind of i always went back to i don't
[213.60 --> 222.16]  know if you did this sort of experiment in in school where you kind of line up ramps that marbles can run on
[222.16 --> 228.90]  and then you kind of measure everything all out and you predict where the marble will land in in a cup
[228.90 --> 236.24]  and like i did all the math and everything and release the marble and it landed perfectly in the cup
[236.24 --> 244.16]  what i was like wow this math physics stuff is awesome yeah i had a similar experience recently at the
[244.16 --> 248.98]  science center where they had this ramp where you can roll balls down it and if you put it at certain
[248.98 --> 255.12]  intervals with you know with you know basic multiplication you could determine what um what
[255.12 --> 260.00]  key it would hit which would make a certain tone and each key down the line got bigger and it was like
[260.00 --> 264.84]  two four six eight and you know you did the square root of things and that would determine where you would
[264.84 --> 272.16]  put it at on the ramp and that i mean similar that kind of blew my mind yeah yeah i never had such a
[272.16 --> 276.06]  great experience maybe that's why i didn't like physics because i didn't have this awesome moment in life
[276.06 --> 281.36]  why was it amazing that you can do the math and be like we'll put this here and you're gonna hit that
[281.36 --> 287.00]  key there and you know it's amazing there's a great video of a college professor i think it's a physics
[287.00 --> 292.68]  professor who i think he sets up like a bowling ball on the end of a chain or something i may have the
[292.68 --> 298.40]  objects incorrect but he does all the math like you just described karen and he actually swings it from
[298.40 --> 304.90]  a location at his own face and like he's gonna die or be like seriously injured if the math is wrong
[304.90 --> 310.52]  and it's great learning moment you know for the class and that's a i saw that on the internet but
[310.52 --> 316.36]  yeah i never had such a a great moment in physics so that that that that told you that you love math
[316.36 --> 321.42]  basically yeah yeah so that kind of was a catalyst of where i wanted to stay to went back to um
[321.42 --> 326.56]  college i i studied physics and really really liked it and then i kind of fell into um
[326.56 --> 332.54]  computer science after that but i have to ask you if you ever i don't know if i'm completely weird
[332.54 --> 337.72]  but like whenever i am taking off on planes you know like right at that moment where you just the
[337.72 --> 345.86]  plane's going really fast and you just start taking off i always say to myself yay math yay math i do
[345.86 --> 351.30]  because it's so incredible i'm like yay math well yeah because they got to get to a certain speed by a
[351.30 --> 358.26]  certain distance to actually lift off and some somebody did the math right i know hopefully
[358.26 --> 364.86]  yeah sometimes it doesn't work that's cool so do you really like do you kind of whisper it a little
[364.86 --> 369.40]  bit or is it just kind of like an inner voice i'd say it like an inner voice because otherwise people
[369.40 --> 374.18]  start thinking that you don't say it to the person sitting next to you what well that's a good
[374.18 --> 380.48]  conversation starter yay math and then you kind of go into who you are what you do yeah i guess it could be
[380.48 --> 386.44]  oh uh have you uh read this book the martian i'm like the halfway through it right now have you
[386.44 --> 392.42]  heard about this no so they're making it into a movie um with matt damon yeah yeah yeah and like
[392.42 --> 401.36]  september october and it's fabulous i mean if you like uh like space stuff math stuff engineer
[401.36 --> 408.92]  it's just fabulous so it's it's a retelling basically of robinson crusoe on mars like this engineer
[408.92 --> 415.52]  he gets straight or astronaut he gets stranded there and um strange circumstances of events
[415.52 --> 420.94]  you know his crew thinks he's dead but he's really not so he has to use all his engineering skills and
[420.94 --> 427.30]  everything else to like survive on mars and it's a total math and geek fest and it's fabulous so is it
[427.30 --> 433.08]  really he's really on mars then yeah yeah he's really on mars wow yeah so i totally recommend that
[433.08 --> 441.82]  i'm sorry so it's you're it's not a true story is that what you're saying jared it's it's i just i
[441.82 --> 445.34]  had to point that out right i just needed to bring us back to reality there for a second
[445.34 --> 452.26]  well that's why clarified is he really on mars right but i like it i'm mad even fan i'll check
[452.26 --> 458.30]  scott movie too oh see night see we just talked about really scott two shows ago with prometheus
[458.30 --> 462.92]  and see he's falling from grace a little bit with me although adam liked prometheus a lot i liked the
[462.92 --> 469.32]  name prometheus what about you karen do you like prometheus uh i did not see that so let's have to
[469.32 --> 475.08]  put that on my list yeah put on your list it's definitely just one of the two home theater if you
[475.08 --> 480.38]  have home theater do it on home theater don't just watch it on anything just home theater it if you can
[480.38 --> 488.90]  okay anyways well cool so we got to learn a bit about ballet into physics and some of the
[488.90 --> 494.50]  appreciation you have for math and whatnot so at what point did you start getting into software
[494.50 --> 499.58]  development and what was that like for you yeah so i i kind of got into software development doing
[499.58 --> 507.80]  physics um i started programming in mathematica uh doing computer simulations of um some like
[507.80 --> 515.22]  simulated annealing and that was like super interesting um so after i graduated uh there
[515.22 --> 520.48]  was a lot of opportunities for software developers and they were looking for people in just general
[520.48 --> 527.20]  science fields yeah um so i just kind of fell into it that way and i discovered i really liked
[527.20 --> 534.14]  um especially the feedback of programming i mean if you think of um a lot of the science experiments
[534.14 --> 540.06]  you don't have the fast feedback a lot of times but in software development you definitely do and
[540.06 --> 547.26]  it's a bit artistic too which i really like uh so yeah i did java programming uh ruby programming and
[547.26 --> 553.38]  then i met closure and i just kind of fell in love with closure and um i've been lucky enough to
[553.38 --> 562.38]  work in it every day for the past um almost two years so i'm extremely uh happy i still like it
[562.38 --> 568.54]  so well we definitely want to ask you about closure that's kind of the the thrust of this call but
[568.54 --> 572.42]  before that i also want to ask you about your internet handle because it's quite unique giga squid
[572.42 --> 576.92]  yes it's like one of these things that you see it and you can't you can never forget it but i
[576.92 --> 583.92]  what can you tell us the genesis of that okay so this is like way back in the day um i don't know
[583.92 --> 592.22]  if you remember this when there was a thing called aol yes aol chat oh yes so uh i was working at a
[592.22 --> 600.02]  company and during lunch we would all like play half-life together um and so my half-life avatar was
[600.02 --> 609.42]  um player name was squid so we signed up for um like aol instant messenger and i put in squid as my name
[609.42 --> 618.18]  and like it was taken i was like darn that's the worst so then i put in mega squid and mega squid
[618.18 --> 627.50]  was also taken oh man so then finally giga squid was not taken and that's who i was giga squid was born
[627.50 --> 632.46]  well that's much better alternatives usually people just throw like the year they're born at the end
[632.46 --> 637.52]  and it's like that's always kind of dorky so i think you did a good job with the prefixes
[637.52 --> 642.52]  thank you and you've held that handle for a while then too because i mean aol
[642.52 --> 649.40]  aol days forever ago yeah yeah 20 years maybe i haven't actually yeah i haven't actually been on
[649.40 --> 654.70]  there for a really long time but it was born it was born there so gotcha
[654.70 --> 660.82]  awesome well let's get back on the closure here a little bit you fell in love um you've been working
[660.82 --> 666.80]  with it for two years it sounds like what was it about the language um in your experience that you
[666.80 --> 674.64]  know turned you on so much yeah i uh i guess i've been asked that before and i never got to a chance
[674.64 --> 683.22]  to study uh lisp in uh college so i don't know whether it was kind of lisp that i fell in love with
[683.22 --> 694.14]  or closure but i mean closure gives you access to jvm and java interop and concurrency and all that
[694.14 --> 701.40]  so i mean right it's pretty sweet um but the simplicity of the language um really really appeals
[701.40 --> 707.46]  to me so i guess maybe i put the cart before the horse a little bit maybe back up a split second
[707.46 --> 712.98]  and give the summary of closure we've already known as programming language and like you said it's
[712.98 --> 718.48]  kind of a lisp can you just kind of give that overall summary sure sure so uh yeah closure is a
[718.48 --> 724.96]  is a lisp uh so that means it has all these prems and the prems sometimes scare people away
[724.96 --> 732.94]  but um it really you've just got to like not panic about the prems and they kind of go away
[732.94 --> 737.08]  after you work in it a while especially with an editor that does matching and automatically
[737.08 --> 748.22]  inserts it for you they just um you know it it's fine uh so it's a lisp on the jvm uh that's the main
[748.22 --> 758.22]  language it's a dynamic language it's got uh java interop and it has immutable data structures uh that is
[758.22 --> 766.12]  really nice for concurrency and also with an area that's really hot in closure land right now is closure
[766.12 --> 774.90]  which uh closure script is a dialect of closure but it compiles down to javascript and javascript
[774.90 --> 782.66]  as you know just goes about anywhere nowadays so um there's some really exciting advances uh in that
[782.66 --> 789.28]  i mean it's hard to keep up with they just uh more stuff's happening every day yeah so i mean just uh
[789.28 --> 793.54]  just to generalize a little bit and feel free to correct these generalizations but you know you kind
[793.54 --> 798.98]  of have this divide in uh programming languages between object oriented and functional the lisp
[798.98 --> 806.30]  language you know the lisp kind of tree of languages um have always been maybe not maybe always is a as a
[806.30 --> 813.56]  bad word but have kind of had the reputation of being more academic niche um there's always people
[813.56 --> 819.14]  that love lisps and will always hop into online conversations and tell you how much easier it would
[819.14 --> 827.24]  be to do in lisp um but overall object oriented has been kind of the dominant paradigm uh the last
[827.24 --> 835.20]  you know 20 years in programming and yet closure seems to be like super popular so speak to that maybe
[835.20 --> 840.86]  yeah so i think that's a combination of things um and i think that's because closure has a really
[840.86 --> 847.94]  practical side as well you know it's it's really concerned about getting the job done and being able
[847.94 --> 855.18]  to interop um is an important part of that um and being able to run the jvm is is like huge right
[855.18 --> 863.68]  uh and also there's just really a lot of energy a lot of innovation in the community and it's a really
[863.68 --> 871.62]  kind community um just a lot of great people so i think that that really has helped its success and
[871.62 --> 881.44]  also you know rich hickey is is pretty brilliant so that having having him guide our um language
[881.44 --> 889.94]  uh is is really it's really great um was i was on a project that upgraded from you know one version
[889.94 --> 893.58]  of closure to the other and all i had to do was change change the version number there was
[893.58 --> 900.30]  it was totally stable everything was compatible and that's nice that's really unusual that almost
[900.30 --> 908.00]  never happens right yeah so um so yeah they're really focused on stability and making sure that
[908.00 --> 913.66]  there's backwards compatibility and the language is moving in the right direction speaking of rich
[913.66 --> 919.72]  hickey i think adam we have to do a little bit of a shout out yes walters yeah so um devon
[919.72 --> 929.44]  walters was or is a closure guy who contributed to the changelog back in like 2013 and um he wrote
[929.44 --> 933.04]  one post for us and it wasn't even a guest post it was like he was going to come on and be you know
[933.04 --> 936.88]  kind of a more regular writer and you know life happens and whatnot but he wrote a post called rich
[936.88 --> 944.44]  hickey's greatest hits back in looking at september 16 2013 which is really just a list of like five or
[944.44 --> 951.96]  six awesome rich hickey talks and that one post was probably the most popular post of the year for
[951.96 --> 957.72]  us or at least i would almost say all time i would almost say like all time it is i'm i'm guessing here
[957.72 --> 964.88]  but i might be i see so many shares it's always on twitter like it gets recirculated and people find us
[964.88 --> 969.88]  because of this yeah years later even i wouldn't i would probably say it's probably the top all time
[969.88 --> 975.94]  post of the changelog devon's a great guy actually i worked with him um did you about yeah a little
[975.94 --> 982.14]  bit ago too so he's he's a great guy yeah we're after that post we're like devon you gotta write
[982.14 --> 987.40]  some more stuff yeah yeah you should he's a smart guy yeah we'll link that one up in the show notes
[987.40 --> 994.60]  it's kind of become a classic and um yeah rich hickey gives great talks great presenter obviously a very
[994.60 --> 999.84]  smart man and and uh seemed like he kind of invented closure almost in a vacuum do you know
[999.84 --> 1007.28]  any of the history of the creation of the language i don't know um his personal um like how he came
[1007.28 --> 1014.12]  to it all i know that he did work on it uh just solo for quite a bit yeah um before it was presented
[1014.12 --> 1021.06]  to i think a mailing list and then everybody was like wow this is really cool you know can i help um
[1021.06 --> 1030.46]  you know make it better so then he had um you know a few uh people just really help put a shine
[1030.46 --> 1040.98]  on it and bring it to the first version real version so very cool well let's get back to the
[1040.98 --> 1045.30]  to the language a little bit and one thing that you mentioned was that you said it runs on a jvm and
[1045.30 --> 1053.96]  that's huge i think is what you said why is that such a big deal just because um the uh the jvm
[1053.96 --> 1063.70]  is so production hardened and it's so efficient in what it does now after years and years
[1063.70 --> 1072.88]  that uh it it's just great to be able to run on that sort of platform um and you can see that with
[1072.88 --> 1080.88]  the explosion of languages that are running within that ecosystem right now like scala and um you
[1080.88 --> 1089.62]  know jruby and groovy and all the other ones so right yeah and i think that because there are so
[1089.62 --> 1094.28]  many java developers so many people that are familiar with the jvm um not only is it like
[1094.28 --> 1099.44]  production ready and hardened and has all these years of you know mind put or thought put into it
[1099.44 --> 1106.22]  it's just also kind of a comfortable you know uh kind of a not relaxing but just a
[1106.22 --> 1111.82]  non-confrontational what's the word i'm looking for here adam it's uh it's just an environment
[1111.82 --> 1116.90]  people are used to where if they're going to be switching you know the way they think about
[1116.90 --> 1121.30]  programming from an object-oriented mindset to a functional mindset which closure asks you to do
[1121.30 --> 1124.88]  if you're coming from the other side it's nice to have at least something that's familiar
[1124.88 --> 1130.00]  i think you're thinking expectations the expectations of working on the jvm are as such
[1130.00 --> 1136.96]  and because of that you can operate in more of a comfortable calm and uh manner than maybe chaotic
[1136.96 --> 1142.34]  that you see in the craziness that is open source these days which is the next newest hottest thing
[1142.34 --> 1148.68]  disrupting the newest hottest thing from yesterday yeah plus right don't you have access to all of the
[1148.68 --> 1156.66]  the libraries java library yeah yeah there's um there's full java interop um that's for the most
[1156.66 --> 1164.54]  part wrapper free so it's it's very comfortable to work with um other java classes and libraries
[1164.54 --> 1173.16]  um so yeah i mean if you're looking for um kind of a low risk kind of try it out you can either you
[1173.16 --> 1180.50]  carve off a little section and just add a jar and try it there or even in your tests you know you
[1180.50 --> 1187.16]  could just write some tests and closure and see how it goes um so there's lots of ways to introduce
[1187.16 --> 1191.36]  it to your team and get used to it when you can just say oh well let's just add this jar
[1191.36 --> 1197.92]  yeah i mean it sounds like a nice way to to bring up ramp up adoption as well as allowing people to
[1197.92 --> 1202.34]  dip their toes in the water as opposed to you know completely jumping off or into the pool so to speak
[1202.34 --> 1209.62]  right right awesome well i think we do want to ask about uh popular use cases like when closure
[1209.62 --> 1215.78]  makes sense when it doesn't make sense like what is being used for the types of software that you can
[1215.78 --> 1221.28]  build with closure um we do need to take a sponsor break so let's take a minute here from one of our
[1221.28 --> 1226.26]  awesome sponsors and when we get back we'll talk about what are the best times to actually use closure
[1226.26 --> 1234.48]  we'll be right back imagex is a real-time image processing proxy and cdn and let me tell you this
[1234.48 --> 1240.72]  is way more than image magic running on ec2 this is way better it's everything your friend and
[1240.72 --> 1249.50]  developers have dreamt of output to png jpeg jif jpeg 2000 and several other formats and if you're like me
[1249.50 --> 1255.64]  you've ever argued with your boss or a teammate about serving retina images to non-retina devices
[1255.64 --> 1261.56]  you'll appreciate their open source dependency free javascript library that allows you to easily
[1261.56 --> 1269.04]  use the imagex api to make your images responsive to any device now all this takes a platform and the
[1269.04 --> 1276.22]  imagex platform is built on three core values flexibility and quality performance and affordability
[1276.22 --> 1283.06]  when it comes to flexibility and quality imagex has over 90 url parameters that you can mix
[1283.06 --> 1288.58]  and match to provide an unlimited amount of transformations that you need for your images
[1288.58 --> 1294.94]  and they take quality very seriously and because of their commitment to quality several top 1000
[1294.94 --> 1302.54]  websites in the world trust them to serve their images now when it comes to performance imagex operates
[1302.54 --> 1308.02]  out of data centers filled with top of the line mac pros and mac minis and they're set up for a
[1308.02 --> 1314.70]  completely streaming solution this means your images never hit the disc images are served by the best
[1314.70 --> 1321.56]  ssd-based cdn for delivery around the world anywhere extremely fast and while we're talking about speed
[1321.56 --> 1328.50]  almost all the image processing happens on gpus this means transformations are super fast when compared
[1328.50 --> 1334.58]  to competing virtualized environments and lastly it's all about affordability everyone wants to save
[1334.58 --> 1341.38]  a buck that's how the world works because imagex processes close to a billion with a b images per day
[1341.38 --> 1349.10]  they're able to make certain optimizations at scale and pass those savings on to you to learn more about
[1349.10 --> 1358.88]  imagex and what they're all about head to imgix.com once again imgix.com and tell them adam from the
[1358.88 --> 1365.56]  changelog sent you all right we're back talking about closure with karen meyer and we're interested
[1365.56 --> 1372.40]  in closure for a few reasons first of all i'm an object-oriented person at least i have been i'm very
[1372.40 --> 1378.54]  interested in functional i tend to write more and more these days functional style inside of my object
[1378.54 --> 1384.88]  orientation probably a lot thanks to gary bernhardt and some of his influence on me but also because
[1384.88 --> 1390.56]  it seems like it's very useful in production applications and so i'm curious like what are
[1390.56 --> 1395.48]  some awesome use cases for closure how's it being used out there in the wild and maybe even on the
[1395.48 --> 1400.46]  flip side of that like when is it not a great idea to reach for the language sure well i mean closure
[1400.46 --> 1410.74]  is a general purpose language so it's good for lots of things um where it really shines is when you
[1410.74 --> 1420.46]  have to deal with concurrency because uh you have a very composable um simple language it's functional
[1420.46 --> 1427.42]  and you have mutable data structures and that really just uh lets you handle concurrency very nicely
[1427.42 --> 1441.56]  um so as a result uh you can see a lot of big companies like banks and financial and retailers i had a lot of
[1441.56 --> 1449.42]  adoption lately if you if you go to walmart and you get a receipt from walmart your uh receipts are all
[1449.42 --> 1457.40]  going through a closure program what and that goal that's so crazy yeah so it's it's it's it's it's
[1457.40 --> 1465.08]  out there and people are using it um in lots of places a big company startups um just everywhere
[1465.08 --> 1468.60]  it's in the places you may not expect it then
[1468.60 --> 1475.46]  well yeah like i said it's general purpose so um you could just really use it anywhere
[1475.46 --> 1480.42]  i just love the idea of this invisible infrastructure that so many people don't have to care about
[1480.42 --> 1485.92]  and even though we have so many problems with software and security and you know there's tons
[1485.92 --> 1491.00]  of leaky abstractions out there there's a lot of stuff that's powering you know businesses and
[1491.00 --> 1495.84]  communities around the world and most people don't even have to have any clue that their receipts from
[1495.84 --> 1501.42]  walmart are coming through closure but yeah exactly it's pretty cool yeah the kind of nice thing too is
[1501.42 --> 1507.74]  um now with closure script you can have closure on the front end and on the back end too so you just
[1507.74 --> 1512.78]  really have a single language that you're working with which um it's kind of nice for me you know
[1512.78 --> 1518.76]  when i'm developing i don't have to go and switch to javascript or you know copy script or or anything
[1518.76 --> 1525.12]  for the front end um i can stay within the the same ecosystem so closure script does that work
[1525.12 --> 1531.92]  pretty much just like any other transpiler would work yeah yeah it uses the um google's and this is
[1531.92 --> 1540.12]  the unfortunate name uses google's closure compiler but it's like cl right then su but it's you know
[1540.12 --> 1548.78]  closure and closure which is unfortunate naming namespace collisions cool yeah but yeah yeah it's i think
[1548.78 --> 1554.94]  it's good for uh just about anything where you wouldn't want to use it uh i could only think maybe
[1554.94 --> 1561.70]  embedded you know we have really a small uh footprint uh because uh you know the jvm is pretty large
[1561.70 --> 1566.86]  although that's changing now you know with um with closure script and javascript so if you can get
[1566.86 --> 1571.48]  small enough to put javascript on there you can probably get small enough to put closure script
[1571.48 --> 1578.20]  on there as well what about the receipt application that you can think of as an outsider why do you
[1578.20 --> 1584.36]  think they chose closure over say another way to do reseating for walmart is it because walmart
[1584.36 --> 1590.02]  is a closure company or is it because that was you know one of the main languages their programmers use
[1590.02 --> 1596.58]  or is there a reason why that was the best fit for it i i can't talk to their reasons for maybe not
[1596.58 --> 1601.56]  their reasons but like something in that scenario like that kind of scenario why does closure really
[1601.56 --> 1607.40]  fit that kind of scenario yeah well i mean it's a jvm right so you're running a lot on the jvm and
[1607.40 --> 1616.02]  then again current currency that um you're you're doing things um effectively and um then it's less code
[1616.02 --> 1625.28]  right i mean uh with closure it's really concise uh so you have less code to maintain um and you can
[1625.28 --> 1632.02]  compose things and break them up very nicely so it's just a nice place to be i think how about
[1632.02 --> 1637.54]  readability um aside from the parentheses let's just assume we can get over the parentheses which
[1637.54 --> 1646.72]  i i think i probably can get over that um but at the same time maybe just because it's foreign but
[1646.72 --> 1652.64]  uh you know you have the order of the arguments is flipped i believe yeah um isn't it pretty strange
[1652.64 --> 1659.00]  to read at least at first well maybe at first but i think once you get used to it then it's like really
[1659.00 --> 1667.18]  a really simple syntax right i mean what comes first it's always uh you know the function
[1667.18 --> 1672.64]  or the operator and then all the other stuff is afterwards so it's it's very beautiful and it's
[1672.64 --> 1676.94]  um like this is the thing that comes first all the time i don't really need to think about it
[1676.94 --> 1682.48]  so yeah i think that actually improves its readability it reminds me of adam when we were
[1682.48 --> 1686.30]  at space city js last spring i don't know if you remember this but there was a talk about
[1686.30 --> 1692.16]  how they built tetris enclosure script do you remember that talk i do yeah yeah pretty interesting
[1692.16 --> 1698.02]  and we were sitting way in the back um so we couldn't see the slides very well but it was cool
[1698.02 --> 1701.80]  because he showed how like after they had kind of built this foundation of these functions and closure
[1701.80 --> 1707.58]  script a lot of the features that they needed kind of fell out of the fact that the language is
[1707.58 --> 1711.58]  designed in such a way that adding additional features later on was very easy and they almost got
[1711.58 --> 1716.46]  certain things for free um and he was showing different code blocks and he showed the changes
[1716.46 --> 1722.68]  from one slide to the next to add the next feature and you know the the feature would be like when the
[1722.68 --> 1729.28]  row gets complete like wipe out the for the blocks of that row and i was so far back that i could only
[1729.28 --> 1734.48]  really see the shape of it i couldn't i couldn't read any of the code but it had this very i don't know
[1734.48 --> 1738.18]  it was like an attractive shape you know sometimes you can just look at a program from far away
[1738.18 --> 1743.80]  kind of do the squint test yeah and you can tell if it's like poorly factored or not exactly and this
[1743.80 --> 1749.10]  even though i couldn't i couldn't understand it from from latin or from hebrew it looked really
[1749.10 --> 1755.30]  nice and uh i wonder if that's appealing to you or if it was just because i was so far away no i'm
[1755.30 --> 1760.44]  sure that's a part of it i mean it's just um you know you get the joy factor of working in language
[1760.44 --> 1767.14]  too that you find pleasing right and um oh we haven't talked about the REPL yet like the REPL is like a huge
[1767.14 --> 1773.74]  part of it uh so the the REPL stands for read about print loop but it really it allows
[1773.74 --> 1780.30]  you to just interactively i like to think about it as like sculpting your code like you can just get
[1780.30 --> 1785.90]  in there and get your data structures and just manipulate it in and get like super fast feedback
[1785.90 --> 1793.76]  um and you can even poke it running code and explore it that way too um so the REPL is an incredibly
[1793.76 --> 1799.42]  powerful feature that just kind of really aids your development i think it speeds it up
[1799.42 --> 1804.10]  uh so yeah that's a really important part of it too
[1804.10 --> 1811.02]  very cool uh one thing i was going to ask is when you you mentioned kind of sculpting your data in
[1811.02 --> 1816.30]  the REPL one thing about functional programming and some of this could be my lack of understanding so
[1816.30 --> 1820.64]  feel free to like educate as well here um i will not be embarrassed if you educate me here
[1820.64 --> 1829.16]  um it's like you're just kind of passing around this bag of data um through these functions and i'm i'm down with
[1829.16 --> 1836.88]  transformation and like chaining and all that but it seems like it seems like you you could benefit from
[1836.88 --> 1841.68]  structure around that data you know some from some object orientation do you miss that ever inside of
[1841.68 --> 1847.06]  closure or is it just kind of like once you get used to it you're just used to passing bags of data and
[1847.06 --> 1851.24]  is even that even correct that you do that kind of just pass what i consider a hash or like a key
[1851.24 --> 1856.08]  value yeah yeah i mean it's all it's all based on those data structures and like a map uh data
[1856.08 --> 1862.32]  structure and like a vector data structure those are core uh you do organize your functions um and you
[1862.32 --> 1868.92]  organize them usually by namespaces okay uh so you can almost think about the way that you'd maybe
[1868.92 --> 1876.84]  organize um objects you'd use kind of namespaces for too you keep groups of related uh functions
[1876.84 --> 1883.38]  in a separate file or namespace and um then include them in whatever you're working on
[1883.38 --> 1887.50]  so yeah you can definitely organize your code um so it's not just
[1887.50 --> 1896.10]  um you know just plain functions everywhere okay you mentioned the community you said it kind of has a
[1896.10 --> 1902.18]  great community can you uh dive into that at all and give us some more detail yeah it has a very vibrant
[1902.18 --> 1908.82]  um community in fact there's a slack channel now that just started up it used to just be irc
[1908.82 --> 1915.90]  but somebody opened up a slack channel i think it's called closureians.slack.com but i think it's got
[1915.90 --> 1923.12]  almost pretty much 2 000 people from like around the world or just like all this yeah yeah and it's
[1923.12 --> 1927.08]  fabulous you know there's all sorts of different channels for different people's interests you know
[1927.08 --> 1934.24]  if they're in um you know england or russia or wherever sometimes by geography sometimes by
[1934.24 --> 1940.14]  interest if they're into a closure script or totomic um but you know it just brings everybody together
[1940.14 --> 1949.24]  and um talking and sharing hints um there's all sorts of interesting libraries that are being
[1949.24 --> 1956.88]  created every day um let me see there was a there's one that just came out the other day that was
[1956.88 --> 1962.94]  really cool um somebody put out a couple screencasts uh called parens of the dead
[1962.94 --> 1970.56]  wow so it was creating a closure script game he'd only done a couple um screencasts yet but i watched
[1970.56 --> 1977.96]  them and they're fabulous so he kind of codes it all as you're watching uh through emacs and uh the
[1977.96 --> 1985.12]  repl and closure script and everything so i think it was the first video is probably about 15 minutes
[1985.12 --> 1988.78]  and the second one was 12 and he pretty much had like this working closure script game
[1988.78 --> 1995.18]  it was awesome we gotta find that one adam and link that thing up yeah friends of the dead what do you
[1995.18 --> 2000.80]  know about the meetup communities and and conferences out there for closure oh well there's a lot of good
[2000.80 --> 2010.02]  ones um so closure conge is coming up in november so that was actually the first uh closure conference
[2010.02 --> 2013.98]  and after that there have been all sorts of other ones that have sprung up there's closure west
[2013.98 --> 2021.92]  for the west coast and now there's your closure for um people in europe and um i think there's some
[2021.92 --> 2027.90]  other ones i'm forgetting their names but um some more and more are are coming up with popularity
[2027.90 --> 2035.24]  and um so that's great there's local community groups everywhere i help run one in our local
[2035.24 --> 2041.60]  city um cincinnati ohio i help run the cincinnati functional programmers group and that's a great
[2041.60 --> 2048.52]  group of people too oh and there's one coming up too um strange loop uh that's not just closure
[2048.52 --> 2054.56]  but it's a lot of different languages um but closure has a strong contingent there as well but it's a
[2054.56 --> 2061.02]  fabulous conference i guess while we're on the note of strange loop muzzle mention your awesome
[2061.02 --> 2067.80]  talk chemical computing yeah yeah so that's the one i am going to be talking about when coming to
[2067.80 --> 2075.96]  strange loop so uh yeah chemical computing kind of a strange thing so i'm actually really excited that
[2075.96 --> 2084.26]  the talk had accepted because it's it's um the idea of it came from papers that i found in a book
[2084.26 --> 2093.20]  that was entitled unconventional programming paradigms so right off that really appealed to me
[2093.20 --> 2097.30]  uh just i like that would that would just scare me so you can tell we're different people
[2097.30 --> 2103.08]  i'd be like oh scary put it away yeah so i really like to be able to step back
[2103.08 --> 2109.38]  and kind of approach problems that we take every day and just think about it in a completely
[2109.38 --> 2117.90]  different way um i find that really interesting so what chemical programming is is it's not actually
[2117.90 --> 2124.74]  programming with real chemicals which i mean that would be super cool too but that's not what it's
[2124.74 --> 2131.88]  about it's about abstract um so you're using the kind of the metaphor of a chemical reaction
[2131.88 --> 2142.32]  to do your programming with so uh it would be you kind of think so if you can take the example of
[2142.32 --> 2152.16]  um like calculating a max like you know a max of some numbers right right you can think of um we'll say
[2152.16 --> 2157.32]  two numbers like five and three you can think of as molecules
[2157.32 --> 2168.38]  and when these molecules react they react according to a certain rule and the to find the max the rule
[2168.38 --> 2175.96]  is um if you have a five and a three um two molecules you're going to return two new molecules
[2175.96 --> 2183.18]  that are the same number as the biggest molecule that you had in so a five and a three would react and
[2183.18 --> 2193.00]  return a five and a five uh and basically you just do this with a big you can just imagine like a big
[2193.00 --> 2201.96]  list of molecule numbers from one to a hundred okay and then you mix them all up
[2201.96 --> 2206.86]  and you divide them into pairs
[2206.86 --> 2215.16]  and then each of those pairs reacts with one another so it becomes two more numbers
[2215.16 --> 2221.34]  wow and then you mix them up again until you just have one number and then you do the same thing
[2221.34 --> 2229.92]  right and then as they react with one another um you will eventually and this is the tricky part
[2229.92 --> 2238.42]  because you don't really know when yeah you will eventually get them all to be the same number
[2238.42 --> 2244.86]  which is the maximum so you can take a quote measurement which would be take a look at all these number
[2244.86 --> 2253.52]  molecules and say do a distinct on it and you should have you know the number 99 or you know 100
[2253.52 --> 2260.76]  wherever you ended up um calculating the max from and you'll have your result but yeah so that's a
[2260.76 --> 2268.42]  tricky bit trying to figure out where to end but the kind of awesome thing about um that i found kind
[2268.42 --> 2277.10]  of experimenting with it and doing things that way is that this model really allows you to just turn
[2277.10 --> 2285.30]  concurrency up to the max because there's no sequences and there's no no sequentially sequentiality
[2285.30 --> 2291.26]  can't talk there's no prerequisites for these yeah anything yeah and if you think about it like we
[2291.26 --> 2299.32]  as programmers like we iterate over loops and do so much stuff in sequences like all the time
[2299.32 --> 2305.16]  if you would just think about how you normally calculate a max that you just realize wow there's
[2305.16 --> 2311.96]  other ways to do it i don't really even need to have do stuff in order like that so it's it's kind
[2311.96 --> 2316.22]  of an interesting way to think about it and that's kind of what nature does right nature doesn't line
[2316.22 --> 2323.96]  everything up and put it in a loop and process it all well maybe if you think about time you have a 24
[2323.96 --> 2329.08]  hour loop and just kind of keep going every day it's a brand new day no i like that it seems like a
[2329.08 --> 2334.20]  whole different way of of thinking about things and is the purpose of these types of
[2334.20 --> 2341.84]  exercises is to just basically kind of get us out of our rut of thinking about solving problems in
[2341.84 --> 2348.30]  the same way is that what you're trying to do with this talk yeah and and also um just spreading the
[2348.30 --> 2359.16]  knowledge around of um another way of thinking uh i think when you have cross fertilization
[2359.16 --> 2368.46]  of two different fields uh like computer science and um you know biology or nature inspired solutions
[2368.46 --> 2376.80]  that's an area where you have a lot of new ideas and research and innovation and all the papers that
[2376.80 --> 2383.74]  i got all this information from right now all the ideas are just in research right now so there's
[2383.74 --> 2391.56]  nothing in the wild that has um been used but there could be right so this is kind of putting
[2391.56 --> 2396.72]  the knowledge out there and the seeds in people's minds and what might inspire them like to think
[2396.72 --> 2401.88]  about this in a different way you know maybe that'll help them solve some sort of concurrency
[2401.88 --> 2408.96]  problem that they're having um you know who knows what it might what it might spark so that's the
[2408.96 --> 2416.48]  exciting part to me sounds like there's a little bit of a of a pattern here because not only do you
[2416.48 --> 2421.62]  have this upcoming chemical computing uh talk which by the way you have a nice rundown on your website
[2421.62 --> 2425.04]  we'll link that one up in the show notes to those who can't make it to strange loop this year
[2425.04 --> 2431.88]  um but you also have a programming language of your own uh you also say that you're into ai and you're
[2431.88 --> 2437.20]  into robots you have this thing called uh babar i don't know if that's how you say it but
[2437.20 --> 2441.14]  that's how i always said it in my head i don't know how to say it either babar i don't know it's
[2441.14 --> 2446.70]  the elephant from the cartoons right i don't know well see there was a there was a car or a
[2446.70 --> 2452.82]  a cartoon called right babar yeah yeah was that what it was called and i would have so i was gonna
[2452.82 --> 2458.14]  say it babar but is it babar okay yeah i could be wrong i remember the elephant cartoon yeah i don't
[2458.14 --> 2462.76]  remember how they pronounce it and that's what it's named after yeah i don't i'm unsure about the
[2462.76 --> 2466.58]  pronunciation your language so you can pick how you pronounce it yeah all right we'll go with babar
[2466.58 --> 2472.72]  okay i'm almost certain it is babar i'm almost certain okay i was a fan of the show so i i like
[2472.72 --> 2480.40]  that show too tell us about uh your language yeah so um i i kind of have this habit uh that i like to
[2480.40 --> 2489.10]  try to dig into papers and um kind of understand them and one of the papers that i was looking at
[2489.10 --> 2498.14]  was by john mccarthy and it was entitled elephant 2000 and this was had a lot of his
[2498.14 --> 2507.70]  they weren't entirely flushed out but his ideas of what um a programming language of the future should
[2507.70 --> 2516.14]  be and i think it was entitled for the year 2000 right okay um so he had some very interesting ideas
[2516.14 --> 2524.52]  here and one that really aspect that really appealed to me was uh the idea and we talk about cross
[2524.52 --> 2535.86]  federalization that um from philosophy of humans all speak in a language right and if you look at the
[2535.86 --> 2544.32]  things that we do with our language you can abstract that to kind of higher a higher level like what
[2544.32 --> 2552.52]  what what do we try to communicate with each other with our speech for example if you say pass the salt
[2552.52 --> 2562.72]  in english and then you say pass the salt in japanese you know you're you're meaning the same thing even
[2562.72 --> 2569.22]  though you're speaking different languages you're meaning you are want to um you want to request
[2569.22 --> 2578.44]  someone to do an action for you so that kind of boils it down um to a different a different level
[2578.44 --> 2586.54]  and he thought that and philosophers he got this from philosophers that this would be
[2586.54 --> 2593.74]  the same sort of principles would hold true if you wanted to communicate with somebody from mars
[2593.74 --> 2601.84]  right you would still need to have requests you would still need to have um assertions asserting
[2601.84 --> 2609.44]  something like a fact you would still have to have something like queries you know asking a question
[2609.44 --> 2617.46]  um and those are and not only that is the way that we would communicate with machines
[2617.46 --> 2624.48]  right machines would have to and computers would have to communicate with us on this level and we can
[2624.48 --> 2631.70]  see the ones that i mentioned are pretty easy right we we tell computers facts um you know basically x is
[2631.70 --> 2643.12]  seven and um we do queries you know what what is the value of x uh we do requests quite a bit a lot of times
[2643.12 --> 2653.20]  but some things that he mentioned in the speech acts were aspects that our computers don't regularly have
[2653.20 --> 2664.42]  and these are um you could have beliefs and you could have um you could try to convince someone
[2664.42 --> 2671.74]  of something that might change your belief uh so it might affect your future actions
[2671.74 --> 2679.88]  uh so that was kind of an interesting one to explore with um what a computer might make of that
[2679.88 --> 2691.66]  another is um when you when somebody asks you to pass the salt and you agree you have made a kind of
[2691.66 --> 2700.14]  obligation to fulfill that request by kind of accepting it so there's all sorts of these interesting kind of
[2700.14 --> 2709.58]  philosophical um higher level how do we interact with each other and how would that drive interacting
[2709.58 --> 2713.94]  with computer so that was kind of a roundabout
[2713.94 --> 2720.78]  exploration so i created this language to kind of explore some of this so i made um
[2720.78 --> 2727.18]  uh the language through closure i used instaparse which is a great parsing language
[2727.18 --> 2735.70]  uh made my own language to uh give be able to have beliefs and speech acts um in my repl or in my
[2735.70 --> 2741.74]  computer program and then i used this to control um like my ar drone
[2741.74 --> 2750.24]  wow yes so now it got interesting yeah yeah so you know the whole you could maybe give it goals and
[2750.24 --> 2754.70]  beliefs and communicate it with speech acts this is kind of interesting so that was kind of fun i had one
[2754.70 --> 2763.36]  point where um you you know it would it would um fly up until it believed that it was high enough
[2763.36 --> 2771.44]  and that was you know at three meters or however it was and it was kind of fun debugging that so instead
[2771.44 --> 2775.28]  of saying stop when you're three meters high say you believe that three meters is high enough
[2775.28 --> 2780.98]  yeah yeah i i yeah i have i have the belief so when when it flew off and i got stuck on the ceiling
[2780.98 --> 2788.16]  i'm like oh you have a faulty belief right yeah i believe there's a ceiling there yeah so it's kind
[2788.16 --> 2793.08]  of a different way of thinking about and and debugging programs a different way of interacting with them
[2793.08 --> 2798.30]  very cool the syntax is pretty interesting too when you read through some of your examples on the on
[2798.30 --> 2804.30]  the readme just the way that you restructure uh jared almost counter to what you said earlier about
[2804.30 --> 2810.62]  closure like it's is it kind of hard to read but in this case the way that you're asking the program
[2810.62 --> 2817.68]  it's it's sort of like similar to english you know it's very english like yeah there was on purpose
[2817.68 --> 2822.62]  so i used to close your program to create a new language that had no friends
[2822.62 --> 2830.88]  it also is kind of funny because you know when you start to use things like convincing and
[2830.88 --> 2836.02]  requesting you're you're kind of humanizing the machine at this point right because you are
[2836.02 --> 2841.88]  trying to convince it to to power off you know exactly so i start to have sky net thoughts so how
[2841.88 --> 2847.08]  yeah how long have you been doing this like how old is this project don't kill us oh this one's a
[2847.08 --> 2853.94]  a few years old i think i did it in like 2013 so is it stable is it where it's at are you playing
[2853.94 --> 2859.58]  with it anymore it was it was mainly just kind of an exploratory thing for me um so i haven't been
[2859.58 --> 2866.34]  adding to it but um you know it's out there and i've had i've had all sorts of interesting people
[2866.34 --> 2874.12]  comment on it and in fact i found that uh there was another real programming language not just my
[2874.12 --> 2880.30]  toy programming language that actually had speech acts in it um this is called the star programming
[2880.30 --> 2885.16]  language uh so this is a language i think it's used privately right now although i think that he
[2885.16 --> 2892.98]  just open sourced it um starlang but a full featured language that has a notion of speech acts in it
[2892.98 --> 2895.78]  i mean they're not the requests and that's not the beliefs and the
[2895.78 --> 2904.64]  but there's some other some other um acts but very awesome that's all things that i've never even
[2904.64 --> 2911.28]  heard of so very cool things to to be exposed to uh even the term speech acts when i first hit your
[2911.28 --> 2916.70]  home page of the bar or bad bar i was like what the heck's a speech act you know that is exactly right
[2916.70 --> 2921.98]  this is why i love like looking at these papers yeah as i read elf in 2000 i had the same thing it
[2921.98 --> 2926.52]  came to speech acts and i was like what the heck what is that so it's kind of like just a thread
[2926.52 --> 2932.90]  that you can pull on and then you can say oh speech acts is from this philosophy john searles and
[2932.90 --> 2939.12]  and just follow the thread and through trying to just understand just like a couple paragraphs
[2939.12 --> 2945.26]  in this paper it takes you off in different wonderful directions um that you never knew existed
[2945.26 --> 2948.80]  yeah when you talk when you start talking about reading these papers it reminded me i think
[2948.80 --> 2955.46]  um it's the the independent there's independent mac developer i think it's super mega ultra groovy
[2955.46 --> 2962.56]  um which is smug is this company name which i thought was hilarious but he does like audio
[2962.56 --> 2970.62]  synthesizing type of software and i i saw a talk of his years ago where uh he says that he he reads
[2970.62 --> 2977.70]  research papers as a competitive edge in like the indie dev scene to like give himself a level above
[2977.70 --> 2983.12]  everybody else and so he'll like go read an academic paper about signal processing or about some sort of
[2983.12 --> 2988.76]  audio intricacies and he'll work that into his software into his product because nobody else is doing
[2988.76 --> 2994.28]  that you know and he's bringing these ideas from academia which you know oftentimes they just kind
[2994.28 --> 2999.30]  of stop there and they just sit on a shelf so to speak and bringing them into you know kind of a
[2999.30 --> 3003.64]  capitalist economy i thought was very interesting but yeah your take on it's just as interesting where
[3003.64 --> 3008.96]  it's like we can actually you know reach into these other areas and bring thoughts out that
[3008.96 --> 3015.10]  otherwise we never would have been exposed to and they can actually make us better developers
[3015.10 --> 3018.90]  uh they can affect the community in like kind of foundational ways so it's pretty cool
[3018.90 --> 3024.24]  sure yeah and this is actually i think one of the strong suits of uh that i see in the closure
[3024.24 --> 3033.14]  community too that there is a real um friendly give and take with the academic community and the industry
[3033.14 --> 3040.44]  uh that you'll see at the closure conferences there'll be uh speakers from the academic world
[3040.44 --> 3045.74]  and so they we learn from them and then they turn around and then they learn from us too and that
[3045.74 --> 3052.82]  cross-fertilization is just valuable everywhere well let's uh let's break there we do have some
[3052.82 --> 3057.46]  closing thoughts so let's break we'll hear from a sponsor and we'll be right back
[3057.46 --> 3064.64]  i have yet to meet a single person who doesn't love digital ocean if you've tried digital ocean
[3064.64 --> 3070.82]  you know how awesome it is and here at the changelog everything we have runs on blazing fast
[3070.82 --> 3077.02]  ssd cloud servers from digital ocean and i want you to use the code changelog when you sign up today
[3077.02 --> 3083.96]  to get a free month run a server with one gig of ram and 30 gigs of ssd drive space totally for free
[3083.96 --> 3091.12]  on digital ocean use the code changelog again that code is changelog use that when you sign up for a new
[3091.12 --> 3095.66]  account head to digitalocean.com to sign up and tell them the changelog sent you
[3095.66 --> 3103.24]  all right we're back we got karen here we're talking now about her book i didn't say that before
[3103.24 --> 3110.56]  the break my bad but uh we've been waiting to talk about this book because this this whole call has sort
[3110.56 --> 3118.02]  of been uh an introductory guide maybe even a preface to your book potentially but your book is a guide for
[3118.02 --> 3125.54]  those wanting to get in closure it's a as described by your um by your about here on uh on amazon the
[3125.54 --> 3131.72]  guide this is the guide that's perfect it's perfectly thorough but gentle uh in terms of an introduction
[3131.72 --> 3139.86]  for closure so what is this book why did you write it uh where did it come from right so um i think one
[3139.86 --> 3148.74]  of the unique things about this book is that it's a combo it is two parts and it's part uh an introduction
[3148.74 --> 3156.98]  in the first half and then in the second half it's a training plan and i structured it that way um
[3156.98 --> 3159.68]  from trying to run
[3159.68 --> 3166.48]  so i had been one of these people like everyone you know would run and i was like oh i wish i could run
[3166.48 --> 3170.60]  oh you mean actually running with your feet yeah like jogging with your feet like jogging and i was
[3170.60 --> 3176.78]  like and i would try it and i'd be like i just can't i can't do it you know i would try running for 15
[3176.78 --> 3182.98]  minutes and i would just feel like i was gonna die so i was just like this is just too hard for me i just
[3182.98 --> 3191.88]  i can't do it and then i um ran into one of these kind of like teach yourself to run programs that was
[3191.88 --> 3199.62]  like he's into 5k that had this thing like you just run for maybe a minute and then you walk for
[3199.62 --> 3205.76]  five minutes and then you run for another minute and then you gradually build up over the course of
[3205.76 --> 3213.28]  you know seven eight weeks till you can finally actually run and this was like i mean i guess i
[3213.28 --> 3218.02]  should have figured this out earlier but it just was mind opening for me that i just didn't have to do it
[3218.02 --> 3223.90]  all at once and the reason why i was having such trouble was i was trying to do too much at once
[3223.90 --> 3233.00]  and i thought you know this can apply to so many other areas and in fact i had i was at a user group
[3233.00 --> 3239.84]  and i was talking to a um a fellow that wanted to learn closure he said yeah i picked up a closure
[3239.84 --> 3245.44]  book and i read it over the weekend and i tried it all and i just i just don't get it it's just too hard
[3245.44 --> 3253.18]  and i was like that's the same thing like when i was running yeah that it if you're changing i mean
[3253.18 --> 3260.38]  the way that you think object oriented is kind of just a drastic difference from functional it's
[3260.38 --> 3266.02]  a different way of approaching problems and that it's it's just kind of like learning to think and do
[3266.02 --> 3271.14]  something in a new way that you just really can't do it all at once i mean maybe some people can
[3271.14 --> 3278.38]  but i certainly couldn't and it took me a long while to kind of mold my brain to think in a
[3278.38 --> 3285.12]  different way and approach problems that way so this book was um all about kind of approaching it
[3285.12 --> 3293.12]  um and giving people the the the path that says yeah it's okay let's ease into it let's start simple
[3293.12 --> 3298.28]  this is not going to happen you're not going to pick up this book and all of a sudden be
[3298.28 --> 3305.28]  totally knowing how to code closure in like two days right it's going to take seven weeks
[3305.28 --> 3311.96]  and i at least for me and i hope other people out there that just that knowledge of okay it's just
[3311.96 --> 3317.30]  not going to happen right away and that's okay it's just a very valuable thing so it provides a
[3317.30 --> 3324.10]  structured training plan um between week one and week seven it starts off using some open source
[3324.10 --> 3333.26]  um website called foreclosure where you can solve problems with the community in a um kind of a
[3333.26 --> 3340.66]  almost a test driven way which is nice and then it moves into doing some katas i've made a github
[3340.66 --> 3348.24]  repo and it's totally open sourcing you there it's called um wonderland katas um so you're doing
[3348.24 --> 3354.68]  katas for closure and developing your skills and little bigger chunks and then the final week is
[3354.68 --> 3361.74]  actually developing your own web app so and by the time you're done with that you've had your brain a
[3361.74 --> 3369.26]  chance to kind of think a different way and it it's it it becomes a lot easier and you can run a 5k
[3369.26 --> 3375.76]  and you can run a 5k i think this is a great example to to pause on the tech side of things
[3375.76 --> 3380.70]  from this conversation and just say that this is to me it seems like a really great example of
[3380.70 --> 3388.24]  living your real life not just in front of a computer and having profound uh new thoughts that
[3388.24 --> 3395.80]  totally impact what you do in your day job in programming uh i think it's amazing how learning to
[3395.80 --> 3400.60]  run and influence you to write this book and then ultimately hopefully potentially influence so
[3400.60 --> 3409.34]  many people out there to uh take their time learning closure through your book yes that's really cool
[3409.34 --> 3416.28]  i mean it's it's amazing to see that yeah i think it's a great conceit for an intro book i loved when i
[3416.28 --> 3421.54]  just saw that it was an intro slash training plan for closure and i almost feel like i need a training
[3421.54 --> 3426.06]  plan more than an introduction because you know i've talked to people about it and i've seen the
[3426.06 --> 3430.62]  syntax and you know i've i've got a little bit of an intro already but a training plan that's something
[3430.62 --> 3436.24]  that i feel like i can really execute on you know uh sometimes you have a book that just intros you to
[3436.24 --> 3444.00]  language it's like well now what do i do yeah i just like yeah write a blog yeah make a web app um but
[3444.00 --> 3450.64]  one that actually takes baby steps with it with you through it is is a great idea yeah yeah i mean it
[3450.64 --> 3456.10]  totally depends on your learning style but hopefully this will key into um the people that that appreciate
[3456.10 --> 3463.00]  that as their learning style i have a question about uh the wonderland closure katas and the
[3463.00 --> 3468.94]  question i guess is why you chose katas over cohen's since cohen's are so popular and they're very similar
[3468.94 --> 3477.94]  to katas right so yeah so what i guess a lot of people are what's the what's the difference so i'll give
[3477.94 --> 3483.52]  you my definition of it maybe it's it's not your definition of the difference of them i would think
[3483.52 --> 3491.34]  of katas being a little bit bigger um chunk problems than cohen's um so that's just my
[3491.34 --> 3496.76]  interpretation of it um but is that is that yours or do you have a different interpretation of it
[3496.76 --> 3502.72]  i my interpretation was just more or less learning something through iterative practicing not so much
[3502.72 --> 3507.84]  the the variant that you went to i think isn't cohen's the purpose is like it's test driven that's
[3507.84 --> 3512.98]  like the whole thing with cohen's but with katas it's you do the same thing over and over and over
[3512.98 --> 3519.44]  again is that right or am i off do i not understand that that that could be it's like i've heard i've
[3519.44 --> 3523.68]  heard various definitions but i'll tell you i'll tell you what it is and then you can tell me
[3523.68 --> 3532.48]  what camp it falls into okay so um the wonderland um code examples they're they're independent little um
[3532.48 --> 3539.88]  closure projects and they do have tests so they come with tests uh failing tests and you need to
[3539.88 --> 3546.70]  provide the code to make those tests pass um and then once you have a solution you're welcome to
[3546.70 --> 3554.22]  share that as a link in the readme too so people can learn from each other as well um so i don't know
[3554.22 --> 3560.58]  exactly what camp that falls into that's what it is well you can probably ask five people and get six
[3560.58 --> 3566.18]  opinions that's true i was gonna say that because i was just curious because they you know by definition
[3566.18 --> 3571.88]  they seem pretty similar and and i was just thinking like with so many coens out there you know sometimes
[3571.88 --> 3578.00]  you might ride the coat till the popularity of other coens to popularize yours for example oh okay yeah
[3578.00 --> 3583.50]  no i i got inspired just because the book um follows a lot of examples of alice in wonderland
[3583.50 --> 3594.06]  so the the repo um the exercises the wonderland exercises um take their inspiration from lewis carroll
[3594.06 --> 3602.86]  and he actually was a really big puzzlest so he he he really enjoyed doing puzzles there's um
[3602.86 --> 3613.06]  there's an alphabet cipher that he had published um there was um i don't think he originated this but
[3613.06 --> 3618.98]  he would is documented that he used it with children a lot it's the it's a river crossing puzzle i don't
[3618.98 --> 3626.86]  know if you've ever heard that where you've got like a a fox and a goose and a bag of corn and then
[3626.86 --> 3633.58]  you've got to get them across the river and you can only carry you know whatever across at one time
[3633.58 --> 3641.80]  and they gotta not eat each other so um that sort of thing i i do love your appreciation i'm not sure if
[3641.80 --> 3647.66]  it's uh that way or not but for just the some of the the art that comes with this so when you're
[3647.66 --> 3651.66]  reading me you've got alice kind of peeking i'm not sure what she's peeking into i think she's
[3651.66 --> 3657.60]  finding a door that's super small and she's gonna go into it but you know with each of these um i'm
[3657.60 --> 3662.36]  not sure do you call them are they called katas then each individual one is a kata yeah that's what
[3662.36 --> 3669.14]  i call them but like you said the terminology is up for grabs i guess so in that case you got but
[3669.14 --> 3674.94]  you have this art and this playfulness and i love so since i asked you about cohen's i i do appreciate
[3674.94 --> 3681.68]  your appreciation for alice in wonderland and how you've played each of these katas off of uh probably
[3681.68 --> 3688.66]  some of your appreciation for that book yeah yeah that's um thanks i i yeah it's just alice in wonderland's
[3688.66 --> 3695.36]  a fabulous a book um that speaks to people on so many levels so it's one of those books that uh
[3695.36 --> 3701.90]  are stories that you can read you know several times and still never get all the nuances that are in
[3701.90 --> 3707.86]  involved you know from everything from the plot to the characters to the yeah you know the ways they
[3707.86 --> 3712.18]  speak things like that you just there's always this constant onion effect that you can keep going
[3712.18 --> 3718.92]  layer by layer deeper deeper uh no pun intended back to alice of course yeah it's it's timeless
[3718.92 --> 3726.40]  well speaking of inspiration i guess we should go into our closing questions now and our closing
[3726.40 --> 3732.22]  question that we ask pretty much every guest is one about inspiration so if you had to pick somebody
[3732.22 --> 3736.84]  out there who would be your hero when it comes to programming somebody who inspires you a mentor
[3736.84 --> 3744.14]  or a role model uh who would you name as your programming hero i would name um jim wyrick he
[3744.14 --> 3750.10]  actually passed away last year but i had the privilege of working um with him and getting to know him
[3750.10 --> 3758.40]  personally and not only was he a brilliant man but he was one of the kindest and most inspiring men
[3758.40 --> 3765.72]  um that i ever got a chance to know so um for i'm sure you've heard of him like he's he was the creator
[3765.72 --> 3772.16]  of the rake library yeah yeah so uh just a beautiful man um he was kind to everybody uh
[3772.16 --> 3777.80]  you know it didn't matter whether you were a programmer or not a lot of times during lunch breaks
[3777.80 --> 3783.70]  and we'd find our drones together you know the the janer would be coming down the hall and he'd say oh
[3783.70 --> 3787.34]  come over here i'm going to show you something and like show him how to fly the drone and show him
[3787.34 --> 3794.14]  the code behind it all and everything and he was just a a naturally just beautiful person and a
[3794.14 --> 3802.28]  wonderful teacher uh so yeah very inspiring yeah amen to that one i think uh we hear jim as a hero
[3802.28 --> 3808.78]  often and well deserved he uh i think we had justin searles on um man it's been a while now but i
[3808.78 --> 3815.86]  definitely remember him having similar kind affectionate words for jim and uh we had adam and i are both
[3815.86 --> 3822.26]  you know have ruby in our roots so we were affected and still use rake to this day yeah by jim not
[3822.26 --> 3828.62]  only his software lives on but you know just the kind of man he was uh still affects and still like
[3828.62 --> 3833.66]  close in the hearts of many people to this day so absolutely definitely adam you want to take the
[3833.66 --> 3838.40]  next one well the the next one is always a fun one because it allows you to be a little introspective
[3838.40 --> 3845.60]  and and more shout outs to popular open source that may or may not be popular yet um but in terms
[3845.60 --> 3850.46]  of your radar what is out there either in just in programming or open source what's out there that's
[3850.46 --> 3854.28]  interesting to you that if you had a free weekend i'm not sure how often that happens for you
[3854.28 --> 3860.38]  but if you had a free weekend what would it be that you hack on well there's like new stuff all the
[3860.38 --> 3865.78]  time right at least for me there's like shiny stuff i'm like oh i'm gonna look at that i don't want to
[3865.78 --> 3872.36]  look at that all right but um right now i'm just um i'm really just entranced with the chemical
[3872.36 --> 3877.58]  programming and the chemical computing and just kind of looking into that a little bit more
[3877.58 --> 3884.42]  and there's some more papers about that and maybe practical applications um or practical
[3884.42 --> 3890.06]  potential applications because there's not in the wild in distributed computing um self-organizing
[3890.06 --> 3898.36]  systems and self-healing systems uh so i i would probably like to explore um a little bit more in that
[3898.36 --> 3907.34]  area as far as other kind of cool um libraries and languages um one that i've contributed to
[3907.34 --> 3918.98]  um quite a bit in uh the past months is pixie lang um and that's a new language by um timothy baldridge
[3918.98 --> 3929.36]  and he's a really smart guy but it's um it's a lisp again but it's it's uh made in r python
[3929.36 --> 3939.16]  um using the py py tool chain so um it compiles down natively it's super fast and um can access
[3939.16 --> 3944.80]  native libraries so it's kind of exciting and different it's closure inspired um but it doesn't
[3944.80 --> 3952.92]  necessarily um stick to um be compatible with closure says it has magical powers do you know what
[3952.92 --> 3960.06]  those magical powers are i think that it's it's supposed to be fast and light um but it it's you
[3960.06 --> 3964.76]  know it's a great language if you especially if you if you want to use fairy gifts
[3964.76 --> 3973.38]  i think the package manager is is named dust which is pretty cool right so you can have pixie dust
[3973.38 --> 3977.98]  yes love it yeah always a play on words love that
[3977.98 --> 3985.72]  but that's a fun it's a fun um project and um they're very open in uh contributions
[3985.72 --> 3992.02]  and friendly there's a nice chat room so if you're looking to get involved in kind of a cool language
[3992.02 --> 3997.58]  with nice people that's a nice side project very cool we'll link that up in the show notes so for
[3997.58 --> 4002.52]  those listening uh if you if you've listened to the show before you know that we take pretty thorough
[4002.52 --> 4009.70]  show notes um so we do a pretty good job on that this is episode 171 so you can find everything
[4009.70 --> 4017.50]  that we've talked about today show notes included at changelog.com 171 um any closing thoughts karen
[4017.50 --> 4026.26]  before we take it home no i think i've said it all but it's been fun well i do want to mention that
[4026.26 --> 4031.76]  your book living closure is available for order now so it's not like it's a pre-order she's written it
[4031.76 --> 4036.16]  it's out there now so if you wanted to go check it out there'll be a show note for that i'll link in
[4036.16 --> 4041.74]  the show notes for that but uh check out the book uh have fun learning closure if you pick up the book
[4041.74 --> 4046.52]  um as you know we release the show every friday so come back here next friday if you're not
[4046.52 --> 4050.76]  subscribing yet go into itunes and subscribe and while you're in the nozzle go ahead and rate the
[4050.76 --> 4055.60]  show if you've listened to it before we also ship a weekly email on saturdays called change all
[4055.60 --> 4062.06]  weekly you can find that at changelog.com slash weekly and because we love those kinds of words
[4062.06 --> 4068.10]  we also have a nightly which is essentially uh github trending on crack it's got lots more stuff
[4068.10 --> 4075.04]  in there maybe cracks a bad word to use on steroids on steroids yeah on steroids worse okay it was on
[4075.04 --> 4078.94]  steroids thank you for the correction jared read it and then you decide if it's on crack or if it's on
[4078.94 --> 4083.48]  steroids and we have a an open repo for that if you want to give us some feedback it's
[4083.48 --> 4089.94]  ping on uh on github so find us on there uh but change all nightly is pretty cool change
[4089.94 --> 4094.16]  all the com slash nightly subscribe to that we had uh some pretty awesome sponsors for this show
[4094.16 --> 4100.72]  that help us make it possible code chip love those guys imagex a brand new sponsor and a very cool
[4100.72 --> 4107.78]  platform for serving images uh very unique and then also digital ocean who doesn't love digital ocean so
[4107.78 --> 4111.68]  those are our sponsors thank you so much for listening and karen thank you so much for
[4111.68 --> 4116.50]  coming on the show and just schooling us in the world of closure and everything that you're about
[4116.50 --> 4121.56]  so cool having this conversation with you so thank you for joining us and uh let's all say goodbye
[4121.56 --> 4125.14]  thanks bye goodbye thank you
[4125.14 --> 4128.08]  you
[4128.08 --> 4130.64]  you
[4139.28 --> 4143.40]  you
[4143.40 --> 4144.30]  you
[4144.30 --> 4149.08]  you
