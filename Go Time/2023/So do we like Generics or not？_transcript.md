[0.00 --> 17.68]  welcome to go time your source for diverse discussions from all around the go community
[17.68 --> 24.20]  thanks to our partners for helping us bring you awesome pods each and every week check them out
[24.20 --> 31.82]  at fastly.com fly.io and typesense.org okay here we go
[31.82 --> 53.32]  hello there welcome to go time i'm matt riah and i have a cold so i'm sorry about that don't worry
[53.32 --> 58.76]  we've got good editors you probably won't notice anything but i just wanted to let you know i'm not
[58.76 --> 64.94]  a hero i'm just uh you know doing my bit for the go community um so please feel free to celebrate
[64.94 --> 71.12]  that on twitter today we're talking about generics we're asking so do we like generics or not some
[71.12 --> 76.28]  people feared that they'd be the end of the language you know that people would abuse it and use them in
[76.28 --> 82.24]  all the wrong places others were a bit more hopeful they had clear use cases and were kind of thrilled
[82.24 --> 86.80]  that they were getting this feature but it was also often touted as the reason a lot of people
[86.80 --> 93.84]  didn't adopt go so we have it now we have generics our flavor of generics what do we think of it
[93.84 --> 99.78]  joining me to discuss this it's my co-host chris brando hello chris hello matt how are you doing
[99.78 --> 104.02]  i'm not too bad you know i've got a bit of a cold but getting through it being just being
[104.02 --> 109.88]  soldering on really just being brilliant how about you doing great so it's a beautiful morning good
[109.88 --> 114.30]  yes and i appreciate this is quite early for you we're doing this at a different time yeah so
[114.30 --> 119.52]  thanks for getting up so early no problem we're also joined by roger pepe roger's been a go enthusiast
[119.52 --> 124.54]  since the day it was released and has been contributing loads of things to the standard
[124.54 --> 130.46]  library and the ecosystem currently working on implementing modules in the q language qlang.org
[130.46 --> 135.74]  welcome back roger hi how's it good good not bad pleasure to have you back of course
[135.74 --> 141.16]  like your hoodie for those that don't know he's wearing a q hoodie it's my favorite hoodie yeah
[141.16 --> 146.36]  we're also joined by brian boren brian's a distinguished engineer at grafana labs working
[146.36 --> 152.64]  on highly scalable storage for metrics logs and traces brian's used go since 2014 so again a long time
[152.64 --> 157.34]  there and contributes to many open source projects including you may have heard of prometheus perhaps
[157.34 --> 164.50]  you've used grpc and i know a lot of you have used go itself welcome brian welcome back hi thanks for
[164.50 --> 170.56]  having me pleasure cool so i'm very excited about this episode because i was one of those people
[170.56 --> 176.94]  that was i'd used generics in previous languages and i kind of was excited that we were getting it
[176.94 --> 181.48]  how do we feel like maybe we could just give someone a quick overview of what generics are
[181.48 --> 189.54]  and when they came to go just so everyone's caught up any volunteers roger you you go okay uh
[189.54 --> 196.72]  yeah i mean generics they're um they basically mean you can pass types to functions and uh methods and
[196.72 --> 201.94]  you can have types that are themselves associated with types so you can it's all it's all a compile
[201.94 --> 208.92]  time in a sense you don't need generics but it means that you can you can have these things which
[208.92 --> 215.06]  where before you might pass a dynamic interface value and maybe do a type coercion like the classic
[215.06 --> 222.04]  case of course is with containers so i you know i've made this nice advanced data structure that
[222.04 --> 227.62]  holds holds all my values and i put a value in like and i know that i'm only going to help put
[227.62 --> 232.48]  integers in there and i get this thing out and ah it's not in literature anymore it's the empty interface
[232.48 --> 237.16]  and i you know so i have to assert that it's an interface that it's an int but maybe i didn't
[237.16 --> 243.20]  actually put an int in there and and so my program panics at runtime and also there are a bunch of
[243.20 --> 249.74]  performance improvements associated with that because you know in that example hold it putting
[249.74 --> 255.72]  an integer in a interface if it's you know greater than 256 or something like that then it's actually
[255.72 --> 259.80]  going to have an allocation to put that in an interface so you're actually paying the price
[259.80 --> 266.40]  of storing that data where in fact you just you actually only need to one little integer sized slot
[266.40 --> 272.94]  for it and that can really mount up in terms particularly when you have larger data structures
[272.94 --> 279.06]  which incorporate uh which incorporate types you know the safety and the performance aspects both
[279.06 --> 286.38]  both can add up a lot in larger systems i think i think i might want to note that we had some generic
[286.38 --> 292.04]  types before since since the beginning pretty much like a map for instance where whenever you used a map
[292.04 --> 297.56]  you had to put in in square brackets what the key type was and then right after that what the value
[297.56 --> 306.04]  type was so map string of string map int of string whatever and so what changed uh was it go 1.18 they put
[306.04 --> 311.04]  them in what changed is is the kind of available availability of the programmer to define their own
[311.04 --> 316.70]  things their own types and functions which still had those those little square brackets bit with a type in
[316.70 --> 323.98]  the middle so the power was kind of reserved to the gold compiler beforehand and uh and now now we have
[323.98 --> 332.24]  the power yeah and have we been wielding that power responsibly yeah well i i was a c++ programmer for
[332.24 --> 340.36]  a long time 20 years and actually oh during the from the time before c++ had generics oh wow and i think a lot
[340.36 --> 346.64]  of people feared that go would suffer the way c++ did because people started writing programs that frankly
[346.64 --> 354.16]  no one could understand yeah using uh templates in you know which is the same thing basically in in c++
[354.16 --> 362.10]  i feel go has largely escaped that i i personally have not really come across people overusing generics
[362.10 --> 368.48]  i think it's kind of too early to say honestly i think you know we're we're just past the point where
[368.48 --> 375.26]  people are generally using it where people can assume go 1.18 and everyone all their users are using go 1.18
[375.26 --> 380.28]  and i think you know give it give it a couple of years two or three years and we'll see i think
[380.28 --> 387.02]  whether things are moving in a dubious direction or not yeah what do you think about the choice of
[387.02 --> 394.54]  square brackets uh somebody that was quite new to the language was kind of surprised that it was it was
[394.54 --> 398.72]  just using square brackets and not something different because it was such a different concept
[398.72 --> 405.52]  brian you make a good point about maps and slices being kind of maps well yeah slices the the type
[405.52 --> 410.96]  was before outside the square brackets it's it's not a great pattern well and that's too right well
[410.96 --> 415.68]  yeah maps you have one type inside the square brackets and one outside it it's i don't know if we
[415.68 --> 420.72]  can read too much into that c++ it's uh it's angle brackets less than greater than so i guess they
[420.72 --> 427.42]  wanted to distinguish themselves from that well angle brackets are problematic right deeply problematic
[427.42 --> 431.54]  because you can't because you're syntactically ambiguous because you can't tell if you got a
[431.54 --> 437.70]  less than b then you know you can't well is that the start of a of a type parameter or is it not and i
[437.70 --> 442.90]  think there's lots of good reasons not to use angle brackets for that reason i think that's the same
[442.90 --> 449.12]  reason we didn't use parentheses as well because there was some syntactic ambiguity actually the the first
[449.12 --> 454.16]  generics proposal in go or the first serious generics proposal ago did use parentheses so you you
[454.16 --> 459.84]  really you really can use parentheses but i think i think in that case they were considered not
[459.84 --> 466.08]  sufficiently distinguished you know the square brackets it's somewhat distinguished right but not
[466.08 --> 470.96]  yeah there's still some ambiguity there right so i guess that would be semantic ambiguity on the
[470.96 --> 476.24]  human side of like what is this thing saying if you use you know regular parentheses instead of
[476.24 --> 479.04]  brackets yeah i think that would look quite weird just trying to imagine
[479.04 --> 483.98]  what it would look like with parentheses like yeah that would be yeah it did it was there were
[483.98 --> 490.70]  just loads of parentheses and it's like are we listening yeah take me back to the 50s so have you used
[490.70 --> 496.14]  generics yourself like roger you mentioned that you you're currently working on implementing modules
[496.14 --> 505.22]  in the queue language does that work call for the use of generics much uh not so i do use generics and i use
[505.22 --> 511.76]  them quite often use them in a kind of in a in a in a local way that isn't part of the api you know
[511.76 --> 518.08]  often you want to like there was there was a nice example i came across recently where i had like an
[518.08 --> 524.10]  interface type and an implementation that basically joined two of those together and you want to do that
[524.10 --> 530.88]  in parallel right so for every method call there were quite like maybe 10 12 15 method calls you wanted to
[530.88 --> 538.00]  make a parallel call to both the underlying values and gather the results together and without generics
[538.00 --> 543.84]  he would have written a load of boilerplate code right and with generics i could write a little wrapper
[543.84 --> 548.14]  and and it's just the code was really super clean and you could just do it in a couple of lines
[548.14 --> 553.60]  same thing for every function regardless of the signature of the function and that was worked out
[553.60 --> 558.26]  really nicely actually and and not only that you could oh well okay we've got the boilerplate well maybe
[558.26 --> 563.18]  we don't want to make that maybe want to be sequential and configurable and that's that
[563.18 --> 567.86]  yeah super easy right so how would you have solved that problem if you hadn't had generics
[567.86 --> 573.70]  i'd have probably just written out all the code would you just by hand probably yeah but i might might
[573.70 --> 579.30]  maybe code generation but it wouldn't be too bad i'd or maybe some dynamic type conversion
[579.30 --> 585.62]  that that also but you'd have had to i'd have had to implement a bunch of um a bunch of helper types
[585.62 --> 590.80]  probably yeah so that's it and i think like there are those use cases where it's just perfect
[590.80 --> 595.88]  and that's why i think that i was quite pleased that they came to the language we'll talk a bit
[595.88 --> 604.14]  more about what's in changes in go 121 but i do really like the the slices package yeah so for
[604.14 --> 609.30]  anyone that doesn't know this is like just you know there's common things you do a lot with slices
[609.30 --> 615.54]  and of course i've had the case where i wanted to search through a slice and find something based
[615.54 --> 621.08]  on some function something like this and had to just write that manually for the particular type
[621.08 --> 625.68]  that i was supporting i tried doing things with interfaces and things before but you end up adding
[625.68 --> 630.68]  a lot of complexity in order to just solve that problem so i feel like the slices package is going
[630.68 --> 634.72]  to help us there um are there any other good use cases we've seen when i feel on the slices
[634.72 --> 640.36]  package this thing too maybe i won't have to google the slice tricks document as much because
[640.36 --> 644.90]  there's some things that it covers which i'm very happy about because it was always annoying finding
[644.90 --> 649.08]  that thing even though it was like pretty easy to find i was like okay i gotta google this thing
[649.08 --> 653.92]  it's not in like dash or anything so yeah but they also those slice you almost when you're reading the
[653.92 --> 659.32]  code it's not always obvious what's happening yeah so it's almost like you need the slice look at the
[659.32 --> 663.52]  slices thing when you're reading the code as well whereas if it's just like i don't know one of the
[663.52 --> 668.62]  examples it's much easier to read isn't it so i i was still in the slices package i was really
[668.62 --> 674.56]  pleased that the sorting function there was faster i i always want to make programs faster
[674.56 --> 682.92]  and uh we should say so that slices will become part of the standard library in go 1.21 but it's
[682.92 --> 689.20]  it's available right now as part of the the experimental directory from google so you can you and i have been
[689.20 --> 695.96]  using it for like a year so that change went into prometheus using so where you would previously use
[695.96 --> 701.74]  sort.slice uh you can change that to slices.sort that's much better isn't it but much more of an
[701.74 --> 706.98]  improvement now i much prefer that it is you could easily see what's going on the other it really you
[706.98 --> 713.86]  you don't see it unless you look at a profile the um sort one works in terms of interfaces so every
[713.86 --> 718.98]  single time it needs to compare two elements or to move things around or whatever it's going through
[718.98 --> 724.42]  a dynamic dispatch through through the interface mechanism so it's doing extra lookups so like oh
[724.42 --> 730.60]  what is this thing and and in particular when you're sorting like integers which which happens a couple of
[730.60 --> 738.66]  times in prometheus for instance the generic one just compiles all the way down to like the machine
[738.66 --> 745.70]  instructions for less than so there's no no dynamic lookup no function call overhead no nothing and
[745.70 --> 754.00]  it's like way way faster and narrow you know niche case but it it was um night and day that's pretty
[754.00 --> 758.94]  cool so is that does that actually happen when you're passing like a a function that does the comparison
[758.94 --> 764.82]  of two integers so it kind of devirtualizes the whole thing yeah so there's two variants uh slices.sort
[764.82 --> 770.82]  works for things like ints and strings that you can compare with less than and then there's a variant
[770.82 --> 776.60]  which is called slices.sort func where you supply a less function and that one that one's pretty good
[776.60 --> 783.08]  as well i mean it's not as much faster but as you just said it devirtualizes it's calling through
[783.08 --> 791.10]  uh reference to a function which is much faster than doing dynamic dispatch on the uh on the elements of
[791.10 --> 796.58]  the slice yeah i mean one of the things that i was interested in like is a kind of a bit of a
[796.58 --> 802.42]  conflict for performance optimization because in many languages like well c++ particularly but also
[802.42 --> 808.02]  languages like rust uh you know when you have a generic type it's all devirtualized it's all in
[808.02 --> 813.82]  lined it's all you know like everything everything is basically expanded out so what i one thing i worry
[813.82 --> 821.18]  about in go in the future is that people make think something generic because of that performance
[821.18 --> 829.38]  specifically when actually it would be kind of uh like a nicer easier to understand and and simpler to
[829.38 --> 835.88]  use if it was using interfaces because if you're at the moment you're using generics you have to pass
[835.88 --> 840.36]  around the type parameter you know although the actual type isn't hidden under the hood as it were
[840.36 --> 846.46]  and things become i think are quite often harder to use so there's a kind of tension there because
[846.46 --> 853.42]  if people make generics truly efficient like they can be then you have this pressure to use generic types
[853.42 --> 859.76]  and then you start going down the the route of oh things become harder to use and go maybe starts to
[859.76 --> 864.62]  get that reputation so i i'm interested what you think about that brian actually yeah it's definitely
[864.62 --> 871.76]  complicated right now and and there's basically two cases the the case where you have some kind of method
[871.76 --> 877.34]  in your generic basically if your generic type parameter has an interface which has some methods on it
[877.34 --> 883.12]  that's one case and then the the case where it doesn't have any methods but you do want to use things
[883.12 --> 889.02]  like less than and greater than and it basically has to be one of the underlying types that the compiler
[889.02 --> 895.58]  handles so right now the the first case when it's it basically boils down to an interface and it's it's
[895.58 --> 900.68]  slightly worse than interface because the compiler is passing a little bit of extra information for the
[900.68 --> 910.44]  generic mechanism so generic functions with parameters which are interface type are not that fast
[910.44 --> 918.04]  little bit slower than than interfaces pre-generic whereas generic functions taking things which don't have
[918.04 --> 924.70]  methods can be blindingly fast certainly don't have any dynamic dispatch might enable you to inline
[924.70 --> 930.64]  things you couldn't do before so i mean i think that's already too complicated for you know your
[930.64 --> 936.94]  typical goal programmer to really grasp that's really down in the weeds that's um sorry i don't want to
[936.94 --> 943.88]  insult anyone i just mean there's too much to grok to get your head around to read through the details of
[943.88 --> 949.74]  how this is implemented and that's just where we are today where it's what they call monomorphization
[949.74 --> 956.32]  it's everything is kind of coerced to look like an interface i think in the future if they do start
[956.32 --> 961.88]  stamping out multiple copies of the code for different types for performance reasons then it'll just it'll
[961.88 --> 969.68]  get much harder to understand the trade-offs and yeah i i certainly worry a little bit about that i guess
[969.68 --> 974.60]  where we are there's an uncomfortable thing that happens where where you you get advised to pass
[974.60 --> 980.56]  around a function parameter and that's exactly why sort func slices.sort func has this extra parameter
[980.56 --> 986.42]  that we kind of don't want to exist and it's a value parameter not a type parameter and that's c plus in c
[986.42 --> 991.20]  plus plus that would be a type parameter that would be a parametrization on the type of the function
[991.20 --> 996.36]  rather than a value that you pass into the function so yeah we've got something that's a little bit ugly
[996.36 --> 1002.72]  i would say and i guess what most people are just you know perfectly happy to to get the power or the
[1002.72 --> 1009.00]  expressive power you know we we should be we should be trying to express programs nicely elegantly that
[1009.00 --> 1014.58]  should be our first concern and and then make it work make it right make it fast only the last thing
[1014.58 --> 1020.98]  you do is performance yeah i think my my ideal scenario would be where you could use either approach
[1020.98 --> 1025.90]  so you could use you could pass an interface in or you could pass function parameter in the compiler
[1025.90 --> 1031.26]  is clever enough to know that that's static to know that that's you're always passing the same
[1031.26 --> 1037.34]  function and do the same thing regardless of whether you're using generics or not right and it probably i
[1037.34 --> 1042.92]  think does de-virtualization in a bunch of cases apparently the profile guided optimization is clever
[1042.92 --> 1049.10]  enough to do that sort of thing now in certain cases which is interesting so you know that's that's
[1049.10 --> 1054.72]  pretty cool yeah but i like that message this thing of focus on making the code easy to read easy to
[1054.72 --> 1060.40]  maintain there are times i think when and if you're lucky you'll reach the point where it really
[1060.40 --> 1065.30]  performance really matters you know we've got either massive scale or just you've got things that are
[1065.30 --> 1071.88]  being used depends on the problem really and then it's worth that kind of digging in to the details and
[1071.88 --> 1078.46]  and maybe even worth a bit of complexity and a little bit of sort of ugliness just to for that purpose
[1078.46 --> 1083.36]  then then you're making a trade-off for quite a good reason but i guess brian you'd recommend
[1083.36 --> 1090.26]  you you profile first you gather data you wait until you have one of those situations yeah i mean
[1090.26 --> 1096.58]  you're almost always fine that your performance problems are in a few small places and and so maybe
[1096.58 --> 1103.14]  it's okay to make something that was was five lines of code into 30 lines because that's the bulk of
[1103.14 --> 1108.40]  your performance problem but don't do that all over the place yeah that is tempting i remember
[1108.40 --> 1114.22]  i just wanted to just have the fastest possible thing like it was almost like gamified it for
[1114.22 --> 1119.42]  myself of just like i want the best performance of course i do and i would i would sometimes trade
[1119.42 --> 1125.64]  off the you know i felt like i'm being clever here i'm doing this and yeah it might be complicated you
[1125.64 --> 1130.18]  takes a bit you have to be smart to understand it i wouldn't go as far as insulting half the community
[1130.18 --> 1136.42]  like you did brian yeah but but and then and then maintaining that code over time and where i would
[1136.42 --> 1142.54]  forget i'd be like what on earth is this and then i was like do you know what i'll just rather it was
[1142.54 --> 1149.02]  dead simple thanks yeah was there someone like brian kernogan said um you need to be smarter to debug a
[1149.02 --> 1154.26]  piece of code than you do to write it and therefore if if you write the code to the limit of your ability
[1154.26 --> 1160.76]  then you're actually not able to debug it right i like that that sock that slices dot sort does that
[1160.76 --> 1166.76]  work with anything can you pass any type into that function only ones that support less than so so
[1166.76 --> 1172.46]  ints and floats and strings but that's what there's a sort funk the where you you supply a function that
[1172.46 --> 1178.42]  implements less if you have a more interesting type yeah so this is where constraints comes in
[1178.42 --> 1185.12]  and this is the sort of part of our generics is we have these quite interesting looking ways of
[1185.12 --> 1189.78]  expressing like these are this is a constraint of the types that you can pass into this thing
[1189.78 --> 1194.60]  and there are a few built-in ones aren't there no in fact they've gone the other way they've
[1194.60 --> 1200.26]  in 1.21 there's a new package called comp and i think the main purpose of that is to define
[1200.26 --> 1206.20]  an ordered type which is these things that that support less than so it's it's in the library it's not in
[1206.20 --> 1210.88]  the language i think there's a difference so there's kind of two kinds of you can constrain
[1210.88 --> 1216.04]  something in various ways you can constrain it say it looks like an interface type but constraint
[1216.04 --> 1221.74]  is actually an interface type and it can have methods like any interface type so that means that
[1221.74 --> 1226.70]  you're constrained that that type is constrained to have those methods but also you can name a number
[1226.70 --> 1231.52]  of other types and say this interface must be one of these and you just say that like int
[1231.52 --> 1238.50]  or like as in the bar symbol pipe symbol or string or and that that basically means that
[1238.50 --> 1245.04]  that value must be any one of those and because and if some operation is supported by all of those
[1245.04 --> 1252.20]  then you're able to use it in your generic function and that's how for example that sort function
[1252.20 --> 1258.18]  can work with less than because it's got a constraint that says that mentions all the possible underlying
[1258.18 --> 1263.04]  types in the language of which there aren't that many like 10 or 15 or something you know like we've
[1263.04 --> 1268.26]  got all the uint types all the int types a few others and because we've mentioned all of those
[1268.26 --> 1274.72]  we means we can use less than and we can pass any of our existing types that we can compare less than
[1274.72 --> 1280.94]  which is you know that's pretty cool i gave a talk at go4con last year go4con uk last year
[1280.94 --> 1286.82]  where i talked about using unconstrained types and and how they were kind of strictly more powerful
[1286.82 --> 1292.36]  i didn't talk about performance at all there and yes they're definitely less powerful but i thought
[1292.36 --> 1297.82]  the sort versus sort funk example is an interesting example of that because you can you can write
[1297.82 --> 1304.06]  one in terms of the other so you can write sort in terms of sort funk but you can't do the other way
[1304.06 --> 1310.04]  around right which is kind of interesting to me well particularly as sort is more performant as well
[1310.04 --> 1315.18]  which is like a bit of a shame right because we'd like to be able to write the the more generic the more
[1315.18 --> 1320.78]  powerful version and rather than the other one if i ideally i think but that that actually made me
[1320.78 --> 1325.16]  think of so there's one thing we haven't talked about here which i think is like it just kind of
[1325.16 --> 1330.94]  fell out from the design and i think it's amazingly powerful and quite interesting is that of generic
[1330.94 --> 1338.26]  interface types right which people don't i'm not sure people are unaware of quite how useful powerful
[1338.26 --> 1343.86]  they are so you can have an like an interface type that actually itself has a type parameter so for
[1343.86 --> 1348.50]  example you could imagine i don't know a sorter you know compare interface type that has a method
[1349.30 --> 1355.30]  that takes two parameters both of type t for any type and returns bool so that's kind of equivalent to
[1355.30 --> 1360.98]  a function that takes two type t but you can have multiple methods right so and it's actually a really
[1360.98 --> 1366.42]  powerful really powerful paradigm essentially you can counter you can define a kind of algebra between your
[1366.42 --> 1372.02]  methods in terms of this abstract type in terms of this type that we haven't defined yet which is
[1372.02 --> 1376.74]  quite cool and because it's an interface you've actually got an underlying value you're passing this
[1376.74 --> 1382.18]  thing of type t into this interface but you've actually got a value under there too so for example
[1382.18 --> 1388.18]  it could know how to sort right or it could know and i've used that a few times and i've found it yes
[1388.18 --> 1393.46]  quite interesting but i don't know the performance implications of it i have no idea what you know
[1393.46 --> 1398.90]  brian you might know what is it efficient to call a method on a generic interface or is it about the
[1398.90 --> 1404.98]  same as a as calling it on a normal interface or methods are slightly worse uh with generics than they
[1404.98 --> 1412.18]  were before methods on interfaces so it's a little bit disappointing so i i guess an example which is a
[1412.18 --> 1416.82]  little bit like what you're talking about is is the heap not the heap that you allocate memory on but the
[1416.82 --> 1422.42]  the one which sort of keeps the smallest element at the front so that's expressed in the go standard
[1422.42 --> 1429.94]  library as as an interface that has a less method but also has a swap method and and a pop or push
[1429.94 --> 1435.86]  i forget exactly what it has anyway i noticed that there wasn't one of those in the slices package and i
[1436.50 --> 1440.50]  around about christmas time i was off work i thought oh you know i should i'll be able to fix that in
[1441.14 --> 1447.78]  a couple of hours and this ballooned into something that that took weeks because it's just not that nice
[1447.78 --> 1454.10]  to try and express a thing which is a container and has operations on the objects being contained
[1454.82 --> 1462.50]  in terms of go generics and um i've got a talk at gopher con in san diego coming up where i sort of
[1462.50 --> 1467.46]  explain where all this landed uh which is with a with a completely different data structure called a loser
[1467.46 --> 1473.62]  tree so i won't i won't go into the whole explanation of that right now but anyways uh short version is that
[1473.62 --> 1480.42]  that it's kind of yeah leaves a lot to be desired right now trying to express a a kind of a generic
[1480.42 --> 1486.02]  thing which operates as a container on other things interesting so do you think that's a fundamental
[1486.66 --> 1490.34]  limitation of the current generics design or something that could be addressed with a language
[1490.34 --> 1495.46]  change or maybe it's just because it's performant not performant no well it's a little bit of everything
[1495.46 --> 1499.94]  i i mean the the um kind of borrowing from something we thought we were going to talk about later that
[1499.94 --> 1505.30]  there's there's a function a couple of functions max and min have been put into go 1.21 and i think
[1505.30 --> 1512.02]  they they form a sort of similar example so you can write a generic in go you can write a function
[1512.02 --> 1520.98]  using generics which takes a type t and just basically says if if a less than b then the minimum is is a
[1520.98 --> 1527.38]  otherwise it's b you can write that but it's not the function that you want in the case of floating
[1527.38 --> 1532.58]  point numbers because in the case of floating point numbers they have this exception which is a nan
[1532.58 --> 1538.90]  not a number and nans are never less than or greater than and you know this is sort of annoying anomaly
[1539.62 --> 1545.86]  and where that story ended in 1.21 is these things became built-ins in the language so they sort of
[1545.86 --> 1553.46]  cheated the kobayashi maru the feature development well it's ironic because max and men were one of
[1553.46 --> 1558.74]  he and lach taylor's kind of red lines like if we can't express the maximum made with generics
[1558.74 --> 1564.74]  then you know then the generics design isn't good enough right but now oh damn it we still can't
[1564.74 --> 1570.74]  express maximum with generic so we're putting over the language yeah yeah so i'm harping back to c plus
[1570.74 --> 1575.62]  plus in that language you can you can write what i call partial template specializations you you can
[1575.62 --> 1581.14]  basically say well if it's a float you say this to the compiler i want you to use this version of the code
[1581.14 --> 1586.26]  and then if i don't say anything just use this other version and that technique that language
[1586.26 --> 1593.30]  feature would i think get us out of this problem so basically i do think that's the thing that would
[1593.30 --> 1600.42]  help the ability to put special cases into my generics and say you know if it's this kind of a
[1600.42 --> 1604.58]  thing i want you to use this kind of code and if it's this other kind of thing then do it totally
[1604.58 --> 1610.74]  differently do you think uh so this is a proposal that i made a little while ago for type switching
[1610.74 --> 1617.22]  on generic types type switching on it's issue four five three eight oh oh how could i forget
[1618.34 --> 1623.70]  but with that with that would that give you what you want i have to confess i haven't read it but it's
[1623.70 --> 1630.42]  i mean maybe yeah it sounds so basically what you what you don't want is is for the uh runtime to be
[1630.42 --> 1634.98]  executing these type you don't you don't want to be executing these these types at checks at runtime
[1635.62 --> 1640.58]  which is kind of where you you might try and do it today it would work but it would just be horrible
[1640.58 --> 1647.70]  in performance for for anything low level like a sort or something like that uh yes if if the compiler
[1647.70 --> 1653.06]  is doing a compile time that would be better i guess a type switch i mean is it literally a switch
[1653.06 --> 1657.94]  like with case statements is that what you proposed yeah pretty much except there's target of the switch
[1657.94 --> 1662.74]  is the type itself rather than a value yeah be interesting to try it out i mean all the other
[1662.74 --> 1666.82]  things that i'm familiar with in that space tend to do more of a pattern matching approach
[1667.54 --> 1674.18]  i guess rust does that doesn't it i'm not a i'm not a big rust user but um i think it it borrowed the
[1674.18 --> 1680.26]  idea from haskell which sort of borrowed it from ml which i did learn yeah so so i i think conceptually
[1680.26 --> 1684.26]  it's a little bit nicer to sort of write out the the patterns of things that you're trying to match
[1684.26 --> 1690.10]  and and the code that goes with those yeah i mean this wouldn't allow you to do something like oh
[1690.10 --> 1697.14]  the slice of anything right you'd have to type switch on specific types because otherwise i think it
[1697.14 --> 1703.38]  might be otherwise basically you're in reflection territory right it's not great yeah performance
[1703.38 --> 1708.18]  interesting future anyway yeah that definitely seems doable i was just scanning that proposal
[1708.74 --> 1714.02]  roger and i feel like that could be done at compile time right i mean yeah it could
[1714.02 --> 1717.94]  definitely be done at compile time yes that's because you know the types that one of the things
[1717.94 --> 1724.02]  about generics is it's fundamentally it's all expo logically it's all expanded out at compile time
[1724.02 --> 1729.46]  even though it might not actually be fully expanded out at combine time you you have all the information
[1729.46 --> 1737.14]  you need you can't dynamically generate dynamic generic types although theoretically you can like except
[1737.14 --> 1742.18]  the compiler finds it finds it out and said no no you can't do that we've got over because you can have a
[1742.18 --> 1748.10]  recursive type you could have a recursive type that has a type definition there in there which you know
[1748.10 --> 1754.18]  involves two of the original and then calls itself and then you get this blow up of an infinite number of
[1754.18 --> 1762.18]  generic types it's like the compiler's no no not today how would people show support for that proposal
[1762.18 --> 1766.98]  how does it work like i noticed that there's like thumbs up and things do people pay attention to that
[1766.98 --> 1773.94]  i believe so i mean no one's come up i haven't seen any anyone no one's come up with a good
[1773.94 --> 1779.46]  counter pros i think i think they just need to have the energy the go team need to sort of say yeah this
[1779.46 --> 1784.50]  is this is worth working on now you know this is because i think last i heard russ was like
[1785.06 --> 1792.18]  yeah for later you know it's a proposal hold here's what it what it is too much for now and you can kind
[1792.18 --> 1796.50]  of do it at the moment with a dynamic type switch i'm surprised you yourself haven't been put on
[1796.50 --> 1802.90]  proposal hold roger i am pretty much on hold together sorry yeah because roger i don't yeah
[1802.90 --> 1808.90]  aren't you responsible for the error interface i did i did suggest the error interface and they saw
[1808.90 --> 1813.06]  they saw it and said ah yes this is what we're looking for because they were about to propose like
[1813.06 --> 1817.70]  uh you know that the error thing that just be a package that you imported everywhere everywhere
[1817.70 --> 1824.42]  we'd have to import errors and and say errors dot error and it's like no come on this is well then
[1824.42 --> 1829.70]  it'd be more popular than testify at least until then oh by the way i found out at go for con we did
[1829.70 --> 1836.98]  a we did a panel with the go team i found out that testify my package is banned in google so it's like
[1836.98 --> 1842.90]  good that's going on my uh that's going on my resume what do you mean good brian don't you don't you
[1842.90 --> 1849.38]  don't you use it well i like uh you know i think conflict is good for um a bit of tension a bit of
[1849.38 --> 1856.42]  drama cdd well i could use that i could use that as a moment to shout out uh qt oh yeah which is my
[1856.42 --> 1863.94]  generics based uh testing testing package which i quite like it was kind of has fake heritage from uh
[1863.94 --> 1872.26]  gustavo's uh check package originally was but anyway yes it used generic so i quite like it because it's small
[1872.26 --> 1878.34]  which i don't think you can accuse test five being small no i also had the same feeling and and i
[1878.34 --> 1884.66]  actually have another package which is on github matt riah slash is and that is like i call it testify
[1884.66 --> 1891.46]  off steroids it's like the minimalist version for the same kind of reason uh but it's not generic so
[1891.46 --> 1895.46]  that's quite interesting i wonder how yeah so this is quite nice because because if you want to compare
[1895.46 --> 1900.74]  two things you know for equality or particularly for not equality you want to make sure that they're
[1900.74 --> 1906.34]  actually the same type and generics can do that quite nicely and i quite like so the other thing
[1906.34 --> 1911.06]  the other nice thing i think like that is it's composable so you can you know you can put these
[1911.06 --> 1916.66]  things together and you can make new checkers which all fit into the same framework so i i've been using
[1916.66 --> 1922.34]  it recently and i've been quite i've been quite happy with it i shall post a link to it yeah let's put
[1922.34 --> 1929.30]  we'll put a link into the show notes for that very cool i was going to ask i was literally qt the
[1929.30 --> 1936.66]  letters it's it it says importing dot it's a qt dot is a fairly small small prefix cool good thing
[1936.66 --> 1942.18]  we have a link because i think people googling qt are going to find not that yeah this is true this
[1942.18 --> 1948.02]  is true actually i should shout out francesco banconi who who wrote the original quick test for me this is
[1948.02 --> 1955.54]  pretty much he was a previous colleague of mine so we uh we wrote it together basically nice so when it
[1955.54 --> 1962.42]  comes to like people choosing to pick up generics or not is this sort of advice like we sometimes say
[1962.42 --> 1967.54]  if you're going to do an abstraction like solve the problem a couple of times before and that really
[1967.54 --> 1972.90]  helps figure out what the right kind of abstraction is or if indeed there is one that's suitable do we
[1972.90 --> 1978.02]  have the same kind of advice for generics is this a case where you think there's a clear case for
[1978.02 --> 1982.90]  generics so just use it or should you just implement solve your problems with the specific type if you
[1982.90 --> 1988.90]  only need to solve it for one type first and add make them generic later what would be your thoughts
[1988.90 --> 1996.02]  on that yeah i i think i would agree with that i mean i thought you liked conflict brian well yeah i i
[1996.02 --> 2001.46]  just like uh you know writing programs like keep it simple most of the time so if you just implemented
[2001.46 --> 2007.22]  one thing then then yeah don't muck around making it generic it's only if you find yourself implementing
[2007.22 --> 2013.78]  it two or three times or you want to reuse the same thing in somebody else's program and it and it it
[2013.78 --> 2019.38]  really benefits from being made generic in that way one of the things that i really like actually in
[2019.38 --> 2024.66]  terms for using that pattern in go and it applies to both interfaces and generics actually is that you
[2024.66 --> 2029.70]  can do that you can do it for one type and actually the changes to make it generic the changes to make it
[2029.70 --> 2034.42]  use an interface tend to be pretty small right you can take that generic code and just like do a global
[2034.42 --> 2041.38]  substitution of the type by the type parameter and oh done you know just add a few square brackets here
[2041.38 --> 2048.58]  and there that's you know just just works so i i would say that's a good approach and and helped by
[2048.58 --> 2054.34]  go's uh syntax and semantics i found it sometimes takes a bit of thought to figure out what is the
[2054.34 --> 2059.62]  thing that i should be parameter you know if i've sort of fundamentally got a slice of thing do i
[2059.62 --> 2064.34]  parameterize on the thing that it is the slice or do i parameterize on the thing inside the slice
[2065.06 --> 2071.06]  i'm not sure yet what if there's a rule there but those those kind of questions take a bit of time
[2071.06 --> 2076.02]  sometimes you've got you know maybe try it two different ways and see what happens or find you
[2076.02 --> 2081.30]  know start out and see where you get blocked yeah i actually found an interesting case for that
[2081.30 --> 2086.66]  recently where it was changing an api and i wanted to change it in a backwardly compatible way
[2087.22 --> 2093.70]  and there were basically two types both of which were kind of one was type x y you know so it was
[2093.70 --> 2100.10]  like a new type but had the same underlying type and i wanted the old one was deprecated the new one
[2100.10 --> 2105.46]  was you know was new but we had this function that took the old type so of course oh well you know we
[2105.46 --> 2110.98]  want to make it change the new type and it was taking a pointer type so i said you know the type parameter
[2110.98 --> 2116.42]  is foo and it's taking star foo and then we'll we'll actually do a type conversion inside the function to the new
[2116.42 --> 2121.06]  type which technically should have worked with saying we're allowing just this old type and
[2121.06 --> 2127.06]  just this new type we could type convert between them but doesn't now you can't do that but you can
[2127.06 --> 2133.46]  do that if you type if you move the pointer out so you're like your type parameter is it's either star
[2133.46 --> 2139.30]  old type or star new type then you can do the type conversion so this little little yeah little
[2139.30 --> 2143.94]  niggles like that which is like oh that's interesting where that kind of decision can make a difference
[2143.94 --> 2150.42]  so generally brian then would you say that you are unhappy with the performance of generics or do
[2150.42 --> 2156.98]  you feel like in most cases i think i would go as far as disappointed because i personally with my
[2156.98 --> 2164.26]  background in c++ i i sort of expected there would be more stamping out of different versions of the code
[2164.26 --> 2169.78]  specialized to each type and more opportunities for inlining and and so on and so forth and and
[2169.78 --> 2177.46]  basically the opposite is true and unless your type is a built-in like an inter or a float performance
[2177.46 --> 2184.18]  gets a little bit worse when when using generics and methods on generics so i was i was disappointed
[2184.18 --> 2190.90]  by that i mean you know like first world problem right it's uh having generics at all is vastly better
[2190.90 --> 2196.74]  than where we were before but there there are still these well it's kind of corner cases that i tend to
[2196.74 --> 2202.42]  inhabit where you still reaching for other techniques but and like this we talked about
[2202.42 --> 2208.42]  this a bit before but is this like that's forever because of the design or is this sort of like over
[2208.42 --> 2214.02]  time these things will improve under the hood and we can just wait yeah i expect it to improve over
[2214.02 --> 2219.94]  time and particularly profile guided optimization i think so with trying to not get too deep into the
[2219.94 --> 2227.62]  weeds the current implementation says that anything where the layout and memory looks the same i.e you know
[2227.62 --> 2236.42]  this is this is always uh eight byte fundamental type or this is always a 48 byte struct with four things
[2236.42 --> 2241.54]  in it or something like that and anything that looks like that will run the same code and anything
[2241.54 --> 2246.90]  that looks the same in memory will run the same code as is the current implementation and so they could
[2246.90 --> 2252.02]  generalize that a little bit to say well we ran the profile the profile guided optimizer says there are
[2252.02 --> 2258.66]  these two cases that we should kind of flatten out into the most performant code and then every other
[2258.66 --> 2264.90]  case is going to still run the same code i think that's eminently doable it's you know i'm hand waving
[2264.90 --> 2271.62]  a lot of work onto whoever actually has to implement it but um i expect something like that will happen
[2271.62 --> 2278.34]  it kind of reminds me i've got to get uh profile guided optimization plumbed into our ci pipelines
[2278.34 --> 2284.82]  because it's it's been available since uh 1.20 and i think it's turned on by default in 1.21 so
[2284.82 --> 2290.42]  really should get going on that what will that do for people oh good question well so first of all the
[2290.42 --> 2297.78]  mechanism is basically that you supply the compiler with a a profile like uh in the pprof format the
[2297.78 --> 2304.98]  that is a record of what the program was doing when you ran it doing its normal thing so the compiler
[2304.98 --> 2311.46]  can then look at that and say well i see that 80 of the time in this program was in this one function
[2311.46 --> 2316.34]  so i'm going to change the rules that i apply so there are certain rules inside the compiler like like
[2316.34 --> 2322.90]  for instance how when am i going to inline other functions and it normally only inlines really small
[2322.90 --> 2331.22]  functions but if it sees that uh this one thing is 80 of the whole program and at runtime then it can
[2331.22 --> 2336.58]  say i'm going to inline a bunch more things i'm going to really change the rules on this one i'm going
[2336.58 --> 2344.82]  to go all out for performance just in this one place so the the go team themselves said that the
[2344.82 --> 2350.26]  pgo profile guided optimization gave them a six percent performance improvement on the compiler
[2350.26 --> 2357.38]  in their benchmarks on the go compiler so you know it's it's obviously case by case but uh
[2358.26 --> 2362.26]  it's a little bit more work because you have to come up with some kind of representative profile
[2362.82 --> 2367.62]  you know maybe maybe that's if you only work in one environment that's pulled from your production
[2367.62 --> 2374.34]  environment if you if you have a wide range of use cases you maybe use benchmarks and profile that so
[2374.34 --> 2379.86]  can you combine different profiles a bunch of different profiles uh that's a good question i i i mean in in
[2379.86 --> 2386.18]  general there are tools that do that you know like fleet-wide continuous profiling is a is a very general
[2386.18 --> 2392.26]  case of what you just said and there's several companies sell that kind of a product so i don't know
[2392.26 --> 2398.58]  whether you can just sort of give six files to the compiler and it figures out what to do but i mean a profile
[2398.58 --> 2404.74]  is essentially a list of of stack traces in the code and count sampling counts of those the number of times that
[2404.74 --> 2411.46]  stack trace showed up so you you can essentially aggregate different profiles just just by finding
[2411.46 --> 2416.66]  the common stack traces and adding all the counts up i mean to be clear this is applying to one main
[2416.66 --> 2422.74]  program right one binary so you can't sort of say oh we've got profiles of a bunch of things for this
[2422.74 --> 2428.90]  particular library you know that that doesn't apply or is it just that's a good question i i think it's it's
[2428.90 --> 2435.78]  matching on the um the kind of module name function name how often that shows up so it ought to be
[2435.78 --> 2442.90]  applicable to libraries and it ought to be fairly generally generally applicable i guess the the thing
[2442.90 --> 2447.86]  maybe that you don't want to do is supply a profile that's kind of wildly unrepresentative because then
[2447.86 --> 2453.54]  the compiler will do the wrong thing make your program at least bigger which might make it a little bit slower
[2453.54 --> 2460.26]  so if i'm providing if i'm if i'm supplying a module that other people are using i'll still be
[2460.26 --> 2464.90]  it would still be worth doing some pgo on on that that's oh well that's a good question because
[2464.90 --> 2472.98]  generally people don't use pre-compiled code in go generally they're they're compiling it all on their
[2472.98 --> 2479.22]  target so it wouldn't see that if you import a module for example yeah so it is something in that
[2479.22 --> 2484.42]  sense it applies more to the main program and would you keep updating the profile so that you
[2484.42 --> 2488.98]  sort of as things change you keep right yeah that that would be a good idea i don't think that's vital
[2488.98 --> 2494.10]  i think like i say the the worst thing that can happen is the compiler kind of optimizes the wrong
[2494.10 --> 2499.86]  thing that has the potential to be interesting because the profile guarded program itself will have
[2499.86 --> 2504.98]  different profile right so you kind of need to iterate that's a good point yeah i i think that it's
[2504.98 --> 2509.30]  it's it's at the margins it's things like certainly right now inlining i think is the main thing that
[2509.30 --> 2517.06]  gets affected but it might in future do loop unrolling for instance based on uh on how intensive
[2517.06 --> 2521.78]  this function is used yeah until we have an ai that's just doing this all for us and then we can
[2522.34 --> 2527.46]  stop worrying about it and we don't have to talk to brian anymore uh on the performance point i know
[2527.46 --> 2532.74]  like it wasn't planned this way but i kind of feel like having generics have slightly worse performance
[2532.74 --> 2537.86]  for that kind of interface case might actually be good for us in the long term so i feel like it will
[2537.86 --> 2543.70]  make it so people don't right now jump into just using genetics like oh well this is so much faster
[2543.70 --> 2548.34]  than interfaces so i'm going to use this thing instead of what's been there before so i feel like maybe
[2548.34 --> 2553.94]  that in the long term will help us escape the kind of just using this thing because it's faster just
[2553.94 --> 2559.54]  using this thing since it's shiny and will like keep us solidly rooted in using interfaces where
[2559.54 --> 2563.94]  interfaces are appropriate and then oh well i really do have this use case for generics so i will
[2563.94 --> 2568.90]  use it in this in this place even though i know i'm paying a performance penalty now even if it might
[2568.90 --> 2573.14]  not be true in the future like i assume we're going to get better with generics and then they might be
[2573.14 --> 2578.66]  faster than interfaces in the future or maybe we'll also make interfaces faster in some way yeah that
[2578.66 --> 2584.58]  that was precisely yeah what i was trying to get at before actually like i do think that there's this
[2584.58 --> 2590.34]  pressure if it's much faster to use generics where it might not be appropriate you know and that's i
[2590.34 --> 2596.82]  think that's the worry about everyone has or you know many people had about generics just polluting code
[2596.82 --> 2602.74]  because you know oh generics are faster therefore everything must use generics you know you change
[2602.74 --> 2609.54]  io.copy so instead of taking a reader and a writer value yeah you make it parameterized on the types which
[2609.54 --> 2614.42]  could be faster right and probably would be faster so you know why why wouldn't you do that but that
[2614.42 --> 2620.02]  means you have to you've got it's actually more complex to use i'm hoping that the years of people
[2620.02 --> 2625.22]  using far too many good routines and far too many channels has like taught us as a community to like
[2625.22 --> 2631.06]  not overdo the nice things we do kind of ruin them yeah we do talk we do hear that a lot we do say it a
[2631.06 --> 2636.90]  lot and we talk about that a lot and i do think that's important so yeah that's great well before we move
[2636.90 --> 2642.90]  on to unpopular opinions are there any other things coming in go 1 21 that we're excited about
[2642.90 --> 2650.82]  it gets released next month in august 2023 min and max they're cool that clear functions a bit weird
[2650.82 --> 2655.06]  isn't it like yeah i was gonna bring that up i think the clear i'm happy with clear function
[2655.06 --> 2660.02]  it's like i know it only saves like a little bit of code but having to write those loops or for map to
[2660.02 --> 2664.26]  clear everything out was always kind of annoying like i just want this to be empty now yeah it's
[2664.26 --> 2668.10]  it's weird how it does it with slices yeah it does it does something that you sometimes want
[2668.10 --> 2673.46]  to do with a slice it fills it full of the zero value but it's so different to what it does with
[2673.46 --> 2678.98]  maps so if you have a slice that has 100 elements in it and you call clear on it then you still have
[2678.98 --> 2684.42]  a slice with 100 elements in it but they're all zero which i think is a very very niche case like what
[2684.42 --> 2689.46]  most people would expect is they they have a zero length slice when they finish so i don't i don't
[2689.46 --> 2693.94]  really know that i didn't read through all the thinking that arrived at that i guess it's a
[2693.94 --> 2699.78]  cool look to mem zero in c right so yeah it's very efficient because you can use essentially an
[2699.78 --> 2705.54]  underlying machine instruction probably one to just zero it out just like in one thing really
[2705.54 --> 2710.66]  efficiently and that might not be easy if you're using a loop i feel like if you have a slice of
[2710.66 --> 2714.66]  pointers as well you just want to be like i'd like all of these things to be garbage collected but
[2714.66 --> 2720.02]  i still want to use this slice again it could be useful for that just clearing them all out
[2720.02 --> 2725.86]  yeah it's it's very occasionally useful it's just that the same name does something so different with
[2725.86 --> 2731.38]  maps and slices i guess it's the same with most of those right like make and and new and all of that
[2731.38 --> 2736.42]  they i guess new doesn't but make definitely does like different things with maps and slices sort of
[2736.42 --> 2743.86]  sort of yeah one thing that i i'm looking forward to in go 121 is some improvements to generic type
[2743.86 --> 2750.58]  inference actually in that so there's one particular you know in go you know standard idiom
[2750.58 --> 2757.78]  is to like return concrete types but use interfaces right so you know you have you're returning concrete
[2757.78 --> 2763.70]  type but you're actually going to be uh maybe using your you're accepting an interface but this didn't
[2763.70 --> 2768.82]  work for generic interfaces so you could have like an implementation a concrete implementation and you pass it
[2768.82 --> 2773.70]  to this generic interface and it's like uh-uh no you can't do that you have to explicitly mention
[2773.70 --> 2777.78]  your type this type parameter even though you can clearly see that one implements the other and
[2777.78 --> 2782.90]  now you don't anymore so that's that's pretty cool actually yeah that's the interesting point
[2782.90 --> 2789.06]  though about you can clearly see because there's more type inference that can happen where you actually
[2789.06 --> 2794.02]  would lose when you're reading it you'd kind of lose information and that's probably a line that
[2794.02 --> 2798.42]  you wouldn't want to cross it's a tricky line to choose and they said they were conservative
[2798.42 --> 2802.10]  initially and now they're a little bit less conservative i think i think that's that's
[2802.10 --> 2806.18]  really and also you can if you've got a generic function you don't necessarily you can it will
[2806.18 --> 2811.30]  infer the type of that generic function from where you're assigning it to so if you've got a function
[2812.02 --> 2817.94]  a generic less function that automatically knows how to compare two comparable types for example and
[2817.94 --> 2823.06]  you pass that to something that expects another generic function then you don't have to mention you
[2823.06 --> 2829.14]  don't have to instantiate it it's it'll infer from where you're assigning it to the type parameter for
[2829.14 --> 2834.42]  the function which is also quite cool actually particularly in the context of things like
[2834.42 --> 2840.98]  slices.sort func and that sort of thing so we've talked about the slices package quite a lot there's
[2840.98 --> 2846.82]  there's also a maps package that sort of matches it has two or three functions like keys gets you all
[2846.82 --> 2851.38]  the keys out of map values gets you all the values out of a map those were things you could do before
[2851.38 --> 2856.74]  you just write the loop but those are a little generic functions now that are going into the
[2856.74 --> 2865.22]  standard library and go 1.21 i want sorted keys or you can do slice slices.sort of maps.keys
[2865.78 --> 2867.94]  doesn't quite work because it doesn't return the slice
[2870.66 --> 2874.98]  i it's the it's probably the generic function i've copied and pasted the most because it's quite often you
[2874.98 --> 2880.50]  want to you know like as a test result or you're printing something in a deterministic way i just want
[2880.50 --> 2886.02]  all this all the keys sorted please like oh damn so you just copy and paste sorted keys
[2886.02 --> 2891.54]  and usually they're strings right but not always i'm pretty happy about the equal function because
[2891.54 --> 2895.78]  that's another thing that was kind of annoying to do with the loop right yeah well you did have to sort
[2895.78 --> 2902.02]  them then uh given two maps you had to get all the keys out and then sort them and then check if things
[2902.02 --> 2908.18]  were equal yeah i mean that the sorted keys if if someone's you know perhaps they haven't contributed to
[2908.18 --> 2912.50]  go maybe they could start a proposal the problem they may already be a proposal that roger's written
[2912.50 --> 2917.54]  but if not you could write one get involved and see what that process is like it's quite a nice opportunity
[2917.54 --> 2924.10]  there's also clear as well for like a in that maps package there's a clear function what's the difference
[2924.10 --> 2930.02]  between those two maybe it was there before the clear built-in looking at the the pack of the
[2930.02 --> 2934.34]  docs package it doesn't look like or the docs for the package doesn't look like there's a clear
[2934.34 --> 2939.14]  funk in here oh it doesn't well there was there was in the experimental one and it it suffered i
[2939.14 --> 2944.18]  mean it's it the whole reason why map the clear built-in for in maps was justified was was that you
[2944.18 --> 2953.22]  can't uh again float nan not a number of values break the obvious implementation of of clearing things
[2953.22 --> 2960.02]  from a map because a nan is never equal to anything not even itself yeah it must be right
[2960.02 --> 2965.62]  no it's not it's not equal to itself yeah so if you try and delete the nan value from a map it's
[2965.62 --> 2970.98]  like nope you can't delete that because it doesn't exist in the map yeah wow who's putting their nans in
[2970.98 --> 2988.02]  the map who put nans in the latin in in floats right well speaking of that it's time for our unpopular opinions
[2988.02 --> 3007.06]  okay i'll go first somebody told me that jingle is too long apparently this has been said a few
[3007.06 --> 3012.90]  times like people are like no that's way too long that little jingle it's nothing the singing is great
[3012.90 --> 3019.30]  thanks brian that's really sweet you've accidentally been nice to me actually it was a very well put
[3019.30 --> 3025.62]  together by the the mysterious brake master cylinder who um edited that and made it sound good it's 25
[3025.62 --> 3031.46]  seconds long a little jingle is that too long i feel like it's the exact amount yeah what's going on i
[3031.46 --> 3037.06]  like it i like that you should probably leave but yeah yeah thank you yeah i actually think you should
[3037.06 --> 3043.94]  probably leave you've you've gone it's gone too far just wait uh does anyone else have an unpopular
[3043.94 --> 3050.90]  opinion i have an unpopular opinion it's definitely non-techie i uh my unpopular opinion is that a
[3050.90 --> 3056.18]  shower is no good unless it goes properly cold what do you mean you turn it cold or you just stay in
[3056.18 --> 3061.54]  there until all the water's gone yeah i always finish i always finish by alternating on hot and cold and it
[3061.54 --> 3067.06]  has to finish on cold and if it doesn't it's deeply disappointing i think i was it was recommended by
[3067.06 --> 3071.30]  a physiotherapist once to like you know stop inflammation and things and i started doing it
[3071.30 --> 3077.14]  and now i go you know i go to someone's house and it turned it down to cold and it's like still lukewarm
[3077.14 --> 3084.26]  it's like oh no no i just feel bad i feel right i feel unfinished it's just not it's just not right do you
[3084.26 --> 3090.34]  gradually make it go cold like sort of the opposite of boiling a frog or do you just blast it straight
[3090.34 --> 3096.88]  immediately cold no no absolute blast cold blast hot blast cold yeah absolutely i heard that's good
[3096.88 --> 3104.16]  for your immune system as well like you it's good for all things and lack of it is bad for you know
[3104.16 --> 3110.88]  bad for all things that's like by start of the day so there you go wow i do like the ice pool thing
[3110.88 --> 3115.34]  brian have you ever had a freezing cold shower well yeah when when things are broken
[3115.34 --> 3121.18]  yeah when or it's it's a good example of a bad bad user interface right where you
[3121.18 --> 3127.82]  you it's a little bit too hot and you turn it sort of a tiny tiny amount and it's freezing cold
[3127.82 --> 3133.32]  that's my experience i do it by accident i think i have if i had the choice between a
[3133.32 --> 3139.38]  hot shower that couldn't go cold or just a shower that was cold i'd probably go for the cold one i'm
[3139.38 --> 3145.28]  tempted to get into cold showers because i hear a lot about it and i used to love the plunge pools you
[3145.28 --> 3150.18]  get sometimes in places where there's just ice cold water you just throw you just basically throw
[3150.18 --> 3157.04]  your body in it and uh i find that to be really refreshing um people do all sorts of ice swimming
[3157.04 --> 3162.70]  and things like that maybe my opinion will become popular with matt in the future i'm gonna give it a
[3162.70 --> 3169.34]  go that's for sure chris what do you reckon i feel like when it's hot outside i i kind of want to do
[3169.34 --> 3174.24]  more of a cold shower like if i get back from around when it's been like 90 something degrees outside
[3174.24 --> 3179.66]  i'm like i just really would like to be a lot cooler than i am right now so i feel like that
[3179.66 --> 3183.80]  can sometimes be good i know i feel like i alternate sometimes i'm like okay like doing a
[3183.80 --> 3188.56]  little bit of cold at the end sounds good but most of the time i'm like i just i just want to do a
[3188.56 --> 3193.76]  nice hot shower also i keep my apartment very cold so i think sometimes i get that cold by like
[3193.76 --> 3198.70]  stepping out of the shower and it's like oh okay now it's just like very cold all at once i find it
[3198.70 --> 3203.40]  weird if i've had the cold at the end i actually feel warmer when i come out of the shower if i've had a
[3203.40 --> 3208.40]  hot shower i feel colder it's this i think there's something about my body saying oh it's cold i'm
[3208.40 --> 3212.62]  i want to you know i want to keep warm and then you turn it off it's like oh hang on but you yeah
[3212.62 --> 3216.92]  because you feel different right you feel the difference your skin temperature is warmer is
[3216.92 --> 3222.16]  colder i guess but you feel warmer yeah because the outside air is warmer that's cool do you do any
[3222.16 --> 3225.34]  weird other weird stuff in the shower if that's such a personal question
[3225.34 --> 3235.24]  one i had an idea and this doesn't exist i don't think but this should exist and the idea was a
[3235.24 --> 3240.96]  little device you could put on your tap and it has a blue and a red led and then depending on the
[3240.96 --> 3247.44]  temperature of the water it changes and sort of like shines down so the water glows it's glowing red
[3247.44 --> 3253.96]  if it's hot and cold if it's blue i don't know if in every country that they're the two colors that
[3253.96 --> 3260.68]  people use for hot and cold should be i feel like like it feels like quite universal but i wouldn't
[3260.68 --> 3266.42]  be surprised what do you think of that idea are you in do you want to invest what's halfway what's
[3266.42 --> 3273.02]  lukewarm it puts both it's a kind of purple yeah purple it would have to be it literally like would
[3273.02 --> 3278.12]  just be a very simple i could get ron evans to build this probably with tiny go and probably
[3278.12 --> 3283.72]  wouldn't even need that tricky uh electricity and water is i disagree they go they love each other
[3283.72 --> 3290.54]  they get very excited they're too friendly i think if anything your product liability people might have
[3290.54 --> 3295.36]  something to say about this well that's why i don't hire those people i mean i do i do feel like
[3295.36 --> 3300.68]  there's sometimes electricity in that because you know you have those obnoxious like hands-free faucets
[3300.68 --> 3304.94]  that have to have some amount of electricity for the sensor or whatever so it's kind of like that
[3304.94 --> 3310.48]  it's just adding some leds instead of some sensors yeah i've got one of those taps that does immediate
[3310.48 --> 3315.60]  boiling water which turns out eventually good because you're not you're not boiling a full kettle
[3315.60 --> 3321.40]  if you want a cup of tea you can just do it straight from the tap but then i think i want that tap in my
[3321.40 --> 3329.78]  bath as well so i can just scold yourself yeah well yeah product liability
[3329.78 --> 3335.78]  so you don't want to invest brian that's what i'm hearing yeah fair enough hopefully it does really
[3335.78 --> 3342.30]  well then and you'll be like ah i was the guy that missed out on the led taps well i've i have
[3342.30 --> 3348.12]  often thought that a hedge fund which the investment strategy was just exactly what whatever the
[3348.12 --> 3354.74]  opposite is whatever i invested in that would that would be a great product yeah there's another idea
[3354.74 --> 3360.54]  i had when we we readed our kitchen and i wanted to instead of cupboards just have dishwashers
[3360.54 --> 3366.46]  just every cupboard was a dishwasher and you just put your dishes away it just cleans them they stay
[3366.46 --> 3372.12]  there they're already you don't have to pack them away imagine how much time it's and i pitched it to
[3372.12 --> 3377.64]  the guy that was designing the kitchen like i pitched it as a as though i was dead serious and uh
[3377.64 --> 3382.70]  he was sort of thinking of contemplating it and then he just said like it'd be really expensive and
[3382.70 --> 3388.50]  wasteful to run you know and you probably don't want to wash your cereal boxes right oh yeah that's
[3388.50 --> 3393.68]  true you want other there's other things where you could just not turn it on yeah that's a good
[3393.68 --> 3399.88]  point you couldn't uh you can cook salmon that is that what you do just don't put the soap tablet
[3399.88 --> 3405.28]  don't put detergent yeah well put like a dressing in instead wrap it in foil two layers have you
[3405.28 --> 3411.32]  ever done have you ever done it brian i've heard this too i'm not gonna try either
[3411.32 --> 3417.92]  i get if you've got a huge salmon it's quite difficult to you know it's not gonna it's not
[3417.92 --> 3422.04]  gonna fit in your oven right it's not i could i could see why people might want to do this
[3422.04 --> 3427.62]  you could take the drawers out i bet you could cook loads of stuff like that what are we doing
[3427.62 --> 3428.96]  we're wasting our time
[3428.96 --> 3431.82]  no
[3431.82 --> 3439.64]  not having that chris how do you cook how do you cook salmon chris i don't i don't actually i don't
[3439.64 --> 3443.70]  eat seafood so i don't cook salmon at all that's what i mean i'm sure you could cook other stuff
[3443.70 --> 3448.56]  here's the answer yeah also i don't know if my dishwasher is that much bigger than my
[3448.56 --> 3453.18]  oven oh really like have you got a small dishwasher or a big oven
[3453.18 --> 3460.18]  they do tend to be smaller don't they and you might not necessarily be able to pull all of the
[3460.18 --> 3464.50]  racks out of a dishwasher depending on what type of dishwasher it is i get a little mad at you
[3464.50 --> 3470.60]  they're very intricate machines very magical yeah they're clever they're good i've got one which at
[3470.60 --> 3476.80]  the end of its cycle it opens the door i just does that too yes it's weird when you're in the room
[3476.80 --> 3483.08]  and you've forgotten that it's on you hit that yeah what's going on over there yeah hello i love
[3483.08 --> 3489.56]  that if anybody wants a good watch there's a guy on youtube that has not one but two whole videos
[3489.56 --> 3494.98]  on dishwashers and how they work that's not just like a five minute video these are two like hour
[3494.98 --> 3501.16]  long videos on how dishwashers work and the channel's called technology connections and it's
[3501.16 --> 3504.08]  one of those things where you're like there's no way i'm gonna watch this whole thing and yet
[3504.08 --> 3509.38]  you will watch the whole thing does he cover cooking of salmon and other fish or no but he
[3509.38 --> 3515.60]  does scold people for pre-washing their dishes yeah we need that in the we need that in the show
[3515.60 --> 3520.50]  links please yeah let's do that we'll put that in the show notes yeah it's good it's a good you
[3520.50 --> 3525.54]  learn to not pre-wash your dishes and not use pods you should just use like the cheapest detergent you
[3525.54 --> 3531.10]  can get because just soap it's all the same oh this is good the pods are actually worse unless you
[3531.10 --> 3535.20]  use multiple of them because there's a nice little pre-wash cycle and yeah it's it's a good
[3535.20 --> 3538.94]  video just go watch what about rinse aid and by the way when he scolds people does he use one of
[3538.94 --> 3545.60]  those taps that does the water boiling water quickly no he just looks at you as if he's a
[3545.60 --> 3551.20]  disapproving father just kind of like yeah which which might be the same it might it might burn you
[3551.20 --> 3555.24]  in various ways that's how brian looks at me brian did you think of an unpopular opinion
[3555.24 --> 3560.00]  even beyond cooking salmon in a dishwasher you express no opinion on that though
[3560.00 --> 3570.98]  i um i did i wanted to uh rant about just a little short rant about people who who seem to
[3570.98 --> 3577.30]  want to put the entire program in one line of code like they want to like they get they get the data
[3577.30 --> 3582.32]  and then they filter it and then they decorate it and then they map it into something else and then they
[3582.32 --> 3588.32]  maybe a little bit more in the uh javascript world or the python world it's a little bit more
[3588.32 --> 3593.44]  popular but i see it trying people trying to get that into go you just write the write the loop
[3593.44 --> 3599.30]  please just write the thing that does the thing don't try and put it inside of it doesn't make it
[3599.30 --> 3603.60]  any better if it's in a function in a different file i just have to go read this another reason why
[3603.60 --> 3611.54]  slices.sort should not return the slice that's sorted oh because that enables you to kind of wrap you
[3611.54 --> 3616.32]  know you've got i've got this thing or it turns a slice and i can have them all in the same
[3616.32 --> 3622.66]  expression deeply nested sort filter blah blah blah yeah well so i i guess the implication would be
[3622.66 --> 3628.52]  that it should return a different slice whereas the the one where it doesn't return the implication
[3628.52 --> 3632.96]  is it mutates the one you gave it i'd say don't be scared of vertical white space right
[3632.96 --> 3638.56]  people people i want to put it all on one line because you know it's it looks looks simpler because
[3638.56 --> 3643.82]  it's all in one line but actually just have a few different lines you can have a comment yeah you
[3643.82 --> 3649.88]  see that that pattern you see happening with i've seen it now in i did a bit of svelte js which is the
[3649.88 --> 3656.24]  javascript front-end frameworky thing and the way that they are now the way that they recommend you
[3656.24 --> 3664.02]  format your code attribute having attributes inside an html tag on different lines and it really when you
[3664.02 --> 3668.42]  first see you think that's really unexpected you you know it's very common to just have them
[3668.42 --> 3675.32]  going horizontally but it's so much more readable so yeah it's like that's what i now do and actually
[3675.32 --> 3680.40]  a lot of the formatters do that as well i do that with uh go function parameters actually a lot actually
[3680.40 --> 3684.12]  if it's just starting to get a bit longer just put every parameter on its own line
[3684.12 --> 3689.42]  open brackets on its own line each parameter separately close brackets right at the end
[3689.42 --> 3695.56]  on its own line too and it works quite nicely much more readable uh it's also nice because they
[3695.56 --> 3701.14]  line up all the the all the variable names align in a little stack which is great and again yeah
[3701.14 --> 3708.30]  it's great all right this is not popular opinions this section i feel like with a code golf community
[3708.30 --> 3713.76]  it will be unpopular you know they're trying to minimize on lines and characters and all that yeah
[3713.76 --> 3720.70]  i'm i'm yeah i'm relying on there being a lot of people who like the idea that they can write the
[3720.70 --> 3725.26]  whole thing in one line i guess that the the sort of idiom that you're ranting against really is
[3725.26 --> 3732.76]  maybe epitomized by the sort of fluid programming style or fluent sorry fluent yeah fluid where you
[3732.76 --> 3738.04]  you know one thing returns the same thing returns the same thing and you're just kind of operating on that
[3738.04 --> 3744.32]  thing flowing through so you don't yeah yeah people do that to create little dsls and things
[3744.32 --> 3751.46]  and i understand the appeal of it but it's almost in every case i find it to be i would rather it was
[3751.46 --> 3757.10]  just just spelled out in the boring way that's just very easy to it's much easier to debug things like
[3757.10 --> 3763.06]  you can put log statements in between and things like this as well rather than it being yeah and i think
[3763.06 --> 3768.66]  sometimes sometimes package developers they want to really help the people that are going to consume
[3768.66 --> 3773.12]  the package so they do a lot of things like a lot of extra help and a lot of work for them
[3773.12 --> 3779.08]  when actually you aren't necessarily helping you might as well just let them you know they they're not
[3779.08 --> 3785.28]  idiots let them do do their thing you don't have to solve every problem yeah hard to argue against
[3785.28 --> 3789.62]  though when you're in the design phase and they're like oh but this will make it easy for them for
[3789.62 --> 3796.50]  people are like i don't think so but yeah it's a tricky conversation to have i think sometimes yeah
[3796.50 --> 3803.82]  yeah i think so i have an unpopular opinion oh i feel like it might actually be maybe this time i'll
[3803.82 --> 3809.20]  actually get an unpopular one humble brag humble humble brag i do have i think the second most
[3809.20 --> 3813.42]  unpopular opinion ever what was that one i think i'm like i don't know i think it might have been the
[3813.42 --> 3821.38]  one where i said uh calling go going is like uh dead naming somebody oh right uh that one was very
[3821.38 --> 3826.88]  unpopular people were very mad at me uh about that one i think that's i was popular with me
[3826.88 --> 3833.52]  i think it's popular with a certain subset of people but i'm with you so yeah my my unpopular opinion
[3833.52 --> 3840.72]  it's about analogies i think that the tech debt analogy we should get rid of it because i don't think
[3840.72 --> 3844.98]  the thing that we're talking about we're talking about tech debt is debt i think it's more akin to
[3844.98 --> 3850.64]  malpractice and people are being irresponsible because i think most of the time when tech debt
[3850.64 --> 3854.76]  gets brought up it's like oh we're just going to skip writing the test or skip writing documentation
[3854.76 --> 3858.44]  so that we can get this thing out the door faster or we're just like going to code this in like a
[3858.44 --> 3863.14]  really messy way so it gets out the door faster and i'm like that's not that's not debt that's you
[3863.14 --> 3867.82]  not doing your job properly like please just just write the comments and the docs and the tests it's like
[3867.82 --> 3873.74]  it's it's part of the job like you can't cut out vital things or if you do then you're committing
[3873.74 --> 3877.70]  malpractice and like we should we should call it that and that's why i think it's going to be
[3877.70 --> 3883.88]  unpopular so it's not tech debt it's malpractice do you ever though make like technical decisions
[3883.88 --> 3890.02]  that are pragmatic like there are ways that not i don't mean skipping tests i mean i do tdd so i
[3890.02 --> 3896.00]  rarely skip tests and docs i think that's all very important but do you not sometimes think well
[3896.00 --> 3901.52]  this thing could be better but we're gonna just it's good enough for now and we're gonna ship it
[3901.52 --> 3907.02]  but then maybe there's at some point we know we have to come back and and fix this up i think if
[3907.02 --> 3912.20]  you you have a good understanding of the trade-offs and it's not like a like i guess it's about like
[3912.20 --> 3917.54]  how much future harm are you going to do in this and how and also like how much is it of a best
[3917.54 --> 3922.50]  practice thing like if you're skipping best practices then obviously you shouldn't be doing
[3922.50 --> 3927.46]  that so it's not really debt but i think like the thing that might be akin to technical debt is like
[3927.46 --> 3933.02]  choosing to use a library framework instead of building yourself right so it's like oh i've
[3933.02 --> 3938.26]  assessed how long it would take us for us to build it i've assessed the risk of taking on this
[3938.26 --> 3943.76]  dependency and actually using this framework and all of the knowledge that's needed for both options
[3943.76 --> 3947.94]  and we've decided that taking on this framework makes more sense even though it's more risky right
[3947.94 --> 3952.80]  like i think that's closer to like especially businesses use debt right businesses aren't just
[3952.80 --> 3956.74]  going out being like i'm gonna go get a big old loan just for that you know for the hell of it it's
[3956.74 --> 3960.48]  like no you're gonna you're gonna sit down and assess what are you actually going to use the money for
[3960.48 --> 3964.52]  how are you going to use it how are you going to repay it all of this stuff so if you're doing all of
[3964.52 --> 3970.96]  that math and risk assessment then i think then what you are doing is likely a debt focused thing but
[3970.96 --> 3977.16]  that's rarely if ever at least in my experience what people are doing they're just kind of not doing the
[3977.16 --> 3982.10]  things they should be doing and then being like oh we'll just fix it later and then later literally
[3982.10 --> 3985.66]  never comes and then they just throw out the whole thing and they're like okay we're gonna do it right
[3985.66 --> 3990.84]  this time and they do the same thing again and it's like it's i guess the thing i think it's more akin
[3990.84 --> 3997.12]  to is like using single entry accounting for your like multi-million dollar company and then having no
[3997.12 --> 4002.72]  notes in your single entry account it's just like money is going places where is it going we don't know
[4002.72 --> 4007.66]  like it's like it's it's that level of thing and it's like how do you clean up a single entry
[4007.66 --> 4011.12]  accounting system and turn it into a double accounting system double entry accounting system
[4011.12 --> 4016.80]  down the road it's like that's going to be awful for you like you should never do that like if you
[4016.80 --> 4019.58]  know you're going to build a big enough business where you're going to need double entry accounting
[4019.58 --> 4023.38]  just start with it and it's the same thing with this like if you're not building something you're
[4023.38 --> 4031.12]  going to throw away in six months then just write the docs just write the test code think about what
[4031.12 --> 4034.98]  you're doing it's going to make you go faster in the long run you're not going to get that much
[4034.98 --> 4038.48]  speed if you're like oh i'm going to do this because it's going to save me like a few hours
[4038.48 --> 4042.40]  here it's like it's going to save you a few hours here it's going to make you spend four weeks trying
[4042.40 --> 4050.44]  to unwind it in like six months or less how do you feel about that i agree no i i for me a lot of
[4050.44 --> 4055.18]  the tech debt it's the biggest tech debt things that i've seen in the past have usually it's often been
[4055.18 --> 4060.56]  because you've upgraded you've made a new api for example right you've made the new api you can't
[4060.56 --> 4065.28]  remove the old api because people are using it so you end up with two versions of the api
[4065.28 --> 4069.84]  and at some point in the future you realize that no one is using the old api anymore
[4069.84 --> 4075.10]  and but removing it maybe maybe you've written in such a way that it's really hard to remove the
[4075.10 --> 4080.06]  old one but you kind of want to because it's holding you back because it's using loads of stuff
[4080.06 --> 4085.14]  that you want to be able to get rid of so that's tech debt to me i you know you're in this situation
[4085.14 --> 4091.06]  of being indebted to this thing in the past which you kind of had to take on this debt and you kind
[4091.06 --> 4097.54]  of have to pay it sometime you know that that's often the case like not not just skipping tests
[4097.54 --> 4103.62]  you know that's an easy like which yeah we're taking on this we're committing malpractice by by
[4103.62 --> 4108.58]  taking on deliberately taking on this debt i suppose but there's loads of other cases i think where
[4108.58 --> 4114.50]  you just it just arises because for out of yes matt says pragmatism because you have to
[4114.50 --> 4119.52]  do this of this way otherwise you won't make progress yeah and i think once again if you've
[4119.52 --> 4124.08]  like done a lot of measured analysis of things when you go into it you're like okay this is why we've
[4124.08 --> 4129.54]  taken this on i think it can be described as as a debt but i think a lot of the times when people
[4129.54 --> 4134.46]  are doing it they're not they're not winding up in those situations because of i feel like a lot of
[4134.46 --> 4138.18]  times at least when i've walked into places it's like we've wound up at those places not because
[4138.18 --> 4142.98]  people have like thought things through but because they just rushed to do something so it's like oh
[4142.98 --> 4148.46]  well this thing is hard to maintain so we're just going to greenfield it and it's like okay but what's
[4148.46 --> 4154.14]  your plan to actually deprecate and dismantle the old thing and it's like well we didn't think about
[4154.14 --> 4158.92]  that i'm like well okay well that's not once again we're back in the realm of like just because you
[4158.92 --> 4162.62]  have it like you have it now and you don't like that you have it well you have it because you didn't
[4162.62 --> 4168.12]  plan to actually get rid of the thing but you knew you had to get rid of the thing that doesn't feel
[4168.12 --> 4173.52]  as much like responsible debt usage to me that once again feels like no you should have planned
[4173.52 --> 4177.10]  for how you're going to get rid of it if you knew you were going to get rid of it obviously if like
[4177.10 --> 4180.48]  you need to build this new api for some reason and you're like we don't know how we're going to
[4180.48 --> 4183.70]  get rid of the old one and we're marking that down as a debt and we know we're going to deal with
[4183.70 --> 4188.68]  it was no going to be painful different situation right but we know how to get rid of it it's just
[4188.68 --> 4194.32]  going to take two man lots of work and we don't have that time you know that's usually yeah we
[4194.32 --> 4199.76]  know we know how to do it we know exactly what what we want to do but we just yeah have to pay that
[4199.76 --> 4209.74]  debt chris i bet your finances are in great shape aren't they yes i yeah i'm the person that was like
[4209.74 --> 4213.94]  you know to my friends i'm like yes you know i like balance my checkbook every month and my friends
[4213.94 --> 4218.40]  are like what do you mean balance your checkbook i'm like i reconcile my finances like what do you mean
[4218.40 --> 4223.66]  what do you what do i mean i was also the person who was 21 at the bar just like keeping diligent
[4223.66 --> 4229.48]  track of my drinks and how much i had spent so i would know how much money i had spent oh wow even
[4229.48 --> 4234.30]  while very drunk i would do this i'd be like okay i'm just documenting i'll wake up the next morning
[4234.30 --> 4239.06]  be like okay well like i guess that's exactly how much i drink okay and you look at the credit it's
[4239.06 --> 4244.36]  like oh yeah yeah so yes i keep very good track of my finances yes i mean you actually count the change
[4244.36 --> 4250.18]  i mean i don't spend cash anymore so not not really or i rarely spend cash i don't even look
[4250.18 --> 4255.94]  in my bank account i'm the i'm basically the opposite of that it's all gone matt yeah yeah
[4255.94 --> 4263.88]  basically um well yeah okay i have another i have an unpopular opinion another one quick quick one
[4263.88 --> 4271.90]  i get this we obviously want to be nice and kind to everyone but actually in the right places
[4271.90 --> 4279.36]  banter being mean poking fun is the way i've built the my strongest friendships with people
[4279.36 --> 4284.64]  so i actually think it's not as simple as just always be kind and nice to everyone
[4284.64 --> 4292.04]  i think it's an intellectual exercise sometimes to especially if you do it in a way that's funny
[4292.04 --> 4299.04]  um and somewhat uplifting it can be so i just don't think my unpopular opinion is don't always be
[4299.04 --> 4305.80]  nice to everyone because you miss out be mean to your friends is that what you're saying
[4305.80 --> 4314.34]  i mean i basically am kind of i would hate i hate the idea of upsetting anyone like if it and i do do
[4314.34 --> 4319.86]  that because that's a risky take like sometimes one time this is quite embarrassing but i'll tell this
[4319.86 --> 4326.06]  quick story i was introduced to this guy and he's he had a very cool like the way he was dressed was
[4326.06 --> 4332.48]  very cool but it was like deliberately almost like dystopian like he looked dystopian in his whole vibe
[4332.48 --> 4338.02]  which i really appreciated i thought he looked great so he had like low really sort of tatty clothes
[4338.02 --> 4343.66]  and and like scruffy hair and stuff looked great and then someone introduced him and said oh this is
[4343.66 --> 4349.68]  this is john and i just said uh didn't i give you a pound earlier right outside i was just like
[4349.68 --> 4355.38]  obviously and and i and i don't think he liked it and so it's that that that's one of those things
[4355.38 --> 4360.94]  where i'm drifting off to sleep and i'm like suddenly woken again where i've said this horrible
[4360.94 --> 4368.92]  thing to somebody take a risk sometimes it doesn't pay off but but in it to the right person like if
[4368.92 --> 4374.16]  someone said something like that to me i'd be thrilled and i get i do get it i because of like
[4374.16 --> 4380.24]  at the conferences i was at go for con eu recently and people someone said to me last year someone
[4380.24 --> 4385.12]  said oh because i talk about my hairline a lot they said your hair doesn't look that bad from a
[4385.12 --> 4392.42]  distance from a distance it's like you you're quite good looking in low res i'd be gorgeous if i was a
[4392.42 --> 4398.46]  minecraft character and then this year this year someone said uh because they're joking they feel
[4398.46 --> 4403.86]  like they know me it's a complete stranger but they just said is that a wig why would i choose
[4403.86 --> 4413.96]  this it's like imagine going to a wig shop and saying oh yeah how much is that one very affordable
[4413.96 --> 4418.66]  very affordable i thought it would be because it's tiny they clearly think your hair looks they
[4418.66 --> 4424.36]  thought your hair looks good i cannot think why yeah yeah exactly it doesn't look it's not great
[4424.36 --> 4429.82]  it's not great but so yeah banter and you know what do you think the thing you said about the low
[4429.82 --> 4436.84]  res reminds me of that uh cute from far but far from cute line right which is always like fun but
[4436.84 --> 4441.78]  i i don't think i i don't know how much i disagree with you because i think in some spaces there is
[4441.78 --> 4446.22]  this like very large sense i think especially within 10 companies now there's a very large sense of like
[4446.22 --> 4453.22]  yes be nice to everybody be kind be civil all of that and then i think of like the like black or
[4453.22 --> 4458.02]  queer spaces that i'm in i like people are not like that's not how things work there right now it's
[4458.02 --> 4463.98]  like we're we're mean to each other all of the time um this isn't like all people in this community
[4463.98 --> 4467.80]  but a lot of people you know it's what a whole like throwing shade comes from reading people all
[4467.80 --> 4472.62]  of that it's just like this yeah you know you kind of you know read people for filth sometimes you're
[4472.62 --> 4476.88]  just like yeah there's my friend but like no what you did i just gotta i gotta rip you apart for that
[4476.88 --> 4482.48]  and i think there's also this like slight level for me where i like i don't particularly like when
[4482.48 --> 4487.26]  environments try to be like be kind to everybody be nice everybody we're welcoming to everybody
[4487.26 --> 4491.88]  because that's like a little bit of a dog whistle for me that it's like i'm probably not in a safe
[4491.88 --> 4497.80]  space like this is like i guess to be blunt it's like this is some white people nonsense when i when
[4497.80 --> 4501.84]  that happens i'm just like that we have to recognize that sometimes people are gonna not be
[4501.84 --> 4505.52]  nice and what are you gonna do then you're just gonna tell them to be nice like that's not that's not
[4505.52 --> 4510.14]  how this works like who determines what is nice is it you that determines what's nice because what
[4510.14 --> 4515.20]  might be nice for you might not be nice for me so i think it's there's a lot of complexity in there but i think
[4515.20 --> 4521.20]  overall matt i agree with you slightly yeah i mean those roasts when they do like the comedy roasts
[4521.20 --> 4525.42]  of people you know i'd love to be doing that like maybe we could have that as a regular segment like
[4525.42 --> 4532.98]  today's the roast of brian borum just like go through the whole episode yeah yeah it'd be a new
[4532.98 --> 4538.76]  series that one but i i was listening back to one of the episodes i think it was a go for a says
[4538.76 --> 4544.12]  episode where you were hosting matt and like all of us were just roasting you for like the entire
[4544.12 --> 4550.46]  episode and that was that was fun yeah exactly yeah it's fun but i think you miss like if you
[4550.46 --> 4557.18]  have this very sterile environment and i understand why this happens in in tech companies of course we
[4557.18 --> 4562.82]  want to make sure that people aren't like you don't want to upset people but you miss there's a missed
[4562.82 --> 4569.68]  opportunity there to to build some stronger it's a little bit like a cut will where you get scar tissue
[4569.68 --> 4575.38]  on a cut and it's stronger that scar tissue is stronger than the tissue was before so these
[4575.38 --> 4581.36]  little cuts these little jibes this seems i think it's i think we need it the more you the more you
[4581.36 --> 4584.72]  explain this the more i'm like i maybe i think i think i think we're going through because i think
[4584.72 --> 4588.62]  too like part of the part of the issue i have with the like just be nice to everybody is it's like
[4588.62 --> 4592.54]  is that really the biggest problem you think we need to solve right now it's just like
[4592.54 --> 4598.14]  people are saying mean things and i'm like that's not the biggest problem that i have certainly had
[4598.14 --> 4602.92]  and all these tech spaces i'm just like hey i just i would just really like it if people weren't
[4602.92 --> 4607.02]  doing racist things all the time can we like solve that and it's not them saying things it's like other
[4607.02 --> 4612.54]  things so i think sometimes we focus a little bit too much on the like oh just just say kind things to
[4612.54 --> 4618.82]  each other please right yeah it's almost worse by just now at least we've solved this problem because
[4618.82 --> 4624.12]  we're all saying these right things it reminds me a bit of like a few years ago when there was a
[4624.12 --> 4630.30]  really big push to like get rid of certain words that we use in tech like whitelist and blacklist
[4630.30 --> 4636.16]  and master and all of this and people are like well it's really painful for like people of color to
[4636.16 --> 4640.62]  have to see these words and all of this and i'm like you know the color like black people were just
[4640.62 --> 4646.12]  like what do you mean like i seeing the word slave is not having like throwing me into an existential
[4646.12 --> 4652.06]  existential crisis or anything it's a thing that happened but also like this usage of master is not
[4652.06 --> 4657.58]  different whitelists and blacklists have different like words can mean multiple things so it's like
[4657.58 --> 4661.88]  this feels really weird as a thing for us to be focusing on right now especially when it's like
[4661.88 --> 4666.76]  there are much bigger problems that we should probably be looking at and there was like a non
[4666.76 --> 4671.70]  insignificant amount of effort that went into like let's get let's go through all the code bases and
[4671.70 --> 4677.10]  remove master let's go through all the code bases and remove blacklist and whitelist and all of this and
[4677.10 --> 4681.88]  i feel like after that people were kind of like kind of like after the election of barack obama like oh no
[4681.88 --> 4686.52]  more racism like we got we got rid of all the stuff but it was like that that's not the stuff that's
[4686.52 --> 4690.44]  not the that's not the thing i think it's kind of the same with this like oh everybody's being nice
[4690.44 --> 4695.16]  and civil and kind to each other right now so there's there's clearly no problems with with other
[4695.16 --> 4701.98]  stuff that's not that's not how that works tokenism right yeah on a level yeah but roger you're you're
[4701.98 --> 4705.76]  quite a nice guy are you you ever mean to people never
[4705.76 --> 4713.64]  only my friends exactly your best like yeah your closest friend we definitely have some good banter
[4713.64 --> 4719.48]  yeah yeah but as you mentioned this chris like sometimes i mean i think it's really valuable
[4719.48 --> 4726.96]  a joke that's a jibe can be a really kind of good way of actually people like getting some feedback
[4726.96 --> 4733.68]  like i've actually like you know that's how we do it like if if someone if they're like being big
[4733.68 --> 4741.16]  headed or something you the way that the punishment the social kind of reaction to that is uh is often
[4741.16 --> 4746.92]  a joke or you poke fun at it or something like that and it's a kind of a nicest way or a very nice way
[4746.92 --> 4753.54]  some ways to deliver that bit of feedback and it's kind of light-hearted and it's non-serious and
[4753.54 --> 4760.28]  many true words is spent said in jest right yeah yeah so you say you mean you're just yeah you it
[4760.28 --> 4767.10]  might sound like banter but actually actually being mean well i think it's sometimes a good
[4767.10 --> 4772.30]  it's a good signal it's a it's a signal and it gets you thinking but it's a safe way to do it like
[4772.30 --> 4780.06]  humor is often a it's a safe a safer way brian you called a lot of people idiots today on this podcast
[4780.06 --> 4787.16]  so i assume you're i assume you're on board with this by individually by now yeah yeah we'll cut it out
[4787.16 --> 4795.08]  we'll cut out all the names that's brutal i uh i'm just thinking sitting here thinking that there
[4795.08 --> 4802.56]  are a lot of cultural differences and that really in in a bigger company tends to be a thing that you
[4802.56 --> 4808.50]  need to watch out for and and and in a broadcast medium you have to to go to the lowest common
[4808.50 --> 4815.46]  denominator that that's makes it harder right they but i do i do love you know the sort of well for me
[4815.46 --> 4819.48]  and i'm going to insult more people so so like the sort of american thing of everything that's
[4819.48 --> 4825.94]  awesome right the uh all of the time fantastic right if it's not fantastic then you you you must
[4825.94 --> 4833.10]  hate it right you know hey i fixed that bug fantastic right and um and the the british thing
[4833.10 --> 4839.04]  is more yeah it's all right could do better yeah it's fair fair yeah and i i really love
[4839.04 --> 4846.16]  many of our eastern european colleagues who just say this code is they're just absolutely straight
[4846.16 --> 4853.36]  out with um for the same code yeah to be clear in each case yeah i feel like eastern europeans the
[4853.36 --> 4859.88]  highest compliment they can give is like good it's good and you're like oh that's once every five
[4859.88 --> 4867.04]  years yeah it's ours this is but the other thing of going around the conferences and stuff i've noticed
[4867.04 --> 4873.78]  is that because in a way we are we're all selected around this language so we're all kind of in
[4873.78 --> 4880.16]  software a lot of us like building things like so i think there's a certain level of i don't know what
[4880.16 --> 4886.46]  it is there's a certain level of intelligence you can kind of assume with technical people or it's
[4886.46 --> 4893.64]  whatever the go community does that attracts people to it i don't know but i find that wherever i go
[4893.64 --> 4900.44]  there's just some some jokes just work everywhere and that that was a big surprise to me because i was
[4900.44 --> 4906.96]  very conscious of different kind of cultures and different approaches to things but um i do find
[4906.96 --> 4913.60]  that you can kind of have we just have a lot of fun with people anytime i've interacted with groups
[4913.60 --> 4919.88]  in the go community and tech communities is tends to be like really high level of kind of really good
[4919.88 --> 4925.98]  quality sort of interacting only sometimes well like i said like the people make fun of my hair
[4925.98 --> 4932.22]  because i make fun of it on stage and stuff but it's it's it's fun it's like it's nice so what kind
[4932.22 --> 4939.54]  of jokes do go down well universally i'm interested given i'm giving a talk at some point in italy yeah
[4939.54 --> 4947.28]  well i find because a lot of in the conference audiences a lot of them listen to go time so that's
[4947.28 --> 4953.16]  different because they sort of expect it now one of the big things i noticed is you have to let
[4953.16 --> 4959.08]  people know that it's a joke you can't just say something that's hilarious that we might we might
[4959.08 --> 4964.34]  think it's hilarious arguably hilarious yeah that's but if they don't know it's a joke they're probably
[4964.34 --> 4968.30]  not going to just sit and laugh at you because that they might consider that to be quite rude
[4968.30 --> 4975.12]  so conference like standard office humor works at conferences i don't do it but things like
[4975.12 --> 4981.16]  oh forgive this code i wrote it on a monday you know that will that'll get a laugh or if you say
[4981.16 --> 4987.44]  oh i probably did this before i'd had any coffee like these sort of things work because they're safe
[4987.44 --> 4993.08]  they're a bit like we have these christmas crackers in the uk and they always come with a little joke
[4993.08 --> 5000.34]  that is just terrible like they're terrible jokes and almost it's almost like you're united in the
[5000.34 --> 5007.38]  eye rolling against these jokes you know but it's safe they know it's a joke i told i said once at
[5007.38 --> 5012.28]  a conference that my dad had said oh well yeah he'd said something i can't remember what it was
[5012.28 --> 5018.02]  and i just said get out dad right that was my thing which to me that was really funny and it was just
[5018.02 --> 5023.28]  silent everyone just thought i was telling my dad to get out so it's like sometimes it doesn't work
[5023.28 --> 5028.32]  yeah i feel i feel like the broader thing is like it's just you got to have a lot of nuance with this
[5028.32 --> 5033.06]  right i think sometimes in these types of spaces or in communities i guess in the world in general
[5033.06 --> 5037.78]  it's like people want to have like one easy way that's like universally true objectively like
[5037.78 --> 5042.36]  everybody should be nice to each other or like everybody should be you know once again like
[5042.36 --> 5046.08]  everybody should be nice or kind or these other like very positive words and it's like well
[5046.08 --> 5051.58]  i mean that's not possible like there's going to be some people who are like going to be like not
[5051.58 --> 5056.90]  nice but it's also just like infeasible since like what is nice from one person's perspective is not
[5056.90 --> 5061.06]  nice from another person's perspective like you know there's the whole thing about like with
[5061.06 --> 5065.58]  southern people where if they say like oh bless your heart it's like is that are you saying that
[5065.58 --> 5071.28]  in a nice way or are you saying that in like the quote nice way right so it's like the very same words
[5071.28 --> 5076.38]  said in the very same way could mean two completely different things so i think it's more like we got
[5076.38 --> 5083.06]  to be like let's navigate these situations better and let's like have ways of like you know if there is
[5083.06 --> 5087.62]  harm that's done repairing that harm and focus on that and making sure that's like okay that's a
[5087.62 --> 5091.70]  that's a line we've crossed let's make sure we don't cross that line again but i think when people
[5091.70 --> 5096.00]  start getting into the dogmatic like universality of like don't tell jokes about things or don't do
[5096.00 --> 5100.98]  this or don't do that it's kind of like yeah oh no like that's that's a little too much on the
[5100.98 --> 5106.36]  and this pendulum has swung a bill much to the other side yeah and so we have to we should forgive
[5106.36 --> 5111.38]  people as well if they do cross those lines because usually especially if it's a joke like usually
[5111.38 --> 5117.54]  it depends but if it's coming from a good place and it's too far or whatever i do think we need
[5117.54 --> 5123.92]  to be a bit more forgiving rather than i sometimes get dms then it just it'll just say matt no it just
[5123.92 --> 5131.12]  says like a dog like you might say to a dog yeah so i get that and i'm just like oh come on i don't
[5131.12 --> 5136.78]  like the concept of like throwing away humans or like being like you did something bad you're gone
[5136.78 --> 5142.66]  forever like i just oh it's always irked me a bit even with things where i'm just like i don't like
[5142.66 --> 5147.58]  you as a person at all but like still like we should yeah you still do a podcast with me i'm not
[5147.58 --> 5153.52]  saying you specifically you in the general this time yeah yeah i mean i find ways to poke fun at you
[5153.52 --> 5158.66]  right i made a whole whole little tiktok about you that maybe one day we'll get posted because i think
[5158.66 --> 5170.12]  it's hilarious tomorrow show notes i'll still tiktok for that oh a plug we do actually have a tiktok
[5170.12 --> 5174.14]  i found out i'm on the tiktok i didn't know i thought i was just like never had anything posted
[5174.14 --> 5178.56]  about me on tiktok that's a lie there's lots of videos on the internet tiktok's about oh wow i didn't
[5178.56 --> 5184.14]  know that either go check out changelog.com it's like at changelog.com on tiktok a nice little tiktok
[5184.14 --> 5192.60]  oh wow nice okay well on that bombshell it's time for us to wrap this up we've gone way over
[5192.60 --> 5197.94]  but this is great i hope they keep they'll keep this in thank you so much for joining us to talk
[5197.94 --> 5203.84]  about generics roger pepe always a pleasure hopefully you'll come back again soon brian
[5203.84 --> 5209.38]  borum again we should maybe do some more performance specific episodes it would be really great to
[5209.38 --> 5212.48]  talk to you pick your brains on that a little bit more as well
[5212.48 --> 5217.92]  and of course chris brando thank you very much see you next time on go time
[5217.92 --> 5229.26]  all right that is go time for this week thanks for hanging with us if you're a first-time listener
[5229.26 --> 5236.22]  subscribe now at go time.fm there you'll also find our recommended episodes listener favorites
[5236.22 --> 5241.90]  and a request form so you can let us know what you want to hear about on the pod check it out once
[5241.90 --> 5247.40]  again that's go time.fm and if you're a long-time listener help us help more people on their gopher
[5247.40 --> 5252.28]  path by sharing go time with your friends and colleagues word of mouth is the number one way
[5252.28 --> 5260.06]  people find us thanks once again to our partners fastly.com fly.io and typesense.org and thank you
[5260.06 --> 5266.22]  also to breakmaster cylinder for keeping our beast supply all topped up that's all for now but we'll talk
[5266.22 --> 5268.02]  to you again next time on go time
[5268.02 --> 5271.72]  you
[5271.72 --> 5277.22]  you
[5277.22 --> 5281.22]  you
[5281.22 --> 5295.22]  you
