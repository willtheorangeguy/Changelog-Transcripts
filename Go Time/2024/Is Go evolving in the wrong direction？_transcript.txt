[0.00 --> 16.60]  let's do it it's go time welcome to go time your source for wide-ranging discussions from all
[16.60 --> 24.32]  around the go community find us on the web at gotime.fm on the fediverse at gotime at changelog.social
[24.32 --> 31.24]  and on x at gotime.fm thanks to our partners at fly.io the home of changelog.com launch your app
[31.24 --> 37.62]  as close to your users as possible find out how at fly.io okay here we go
[37.62 --> 48.54]  what's up friends do you remember when chat gpt launched i do it felt like the llm was this
[48.54 --> 54.02]  magical tool out of the box however the more you use it the more you realize that's just not the
[54.02 --> 59.46]  case the technology is brilliant don't get me wrong but it's prone to issues like hallucination
[59.46 --> 66.10]  on its own but there's hope there is still hope feed the llm reliable current data ground it in
[66.10 --> 71.88]  the right data in context then and only then can it make the right connections and give the right
[71.88 --> 78.42]  answers the team at neo4j has been exploring how to get results by pairing llms with knowledge graphs
[78.42 --> 83.98]  and vector search check out their podcast episode about llms and knowledge graphs throughout 2023
[83.98 --> 90.70]  at graphstuff.fm they share tips on retrieval methods prompt engineering and so much more
[90.70 --> 97.80]  don't miss it find a link in our show notes yes check it out graphstuff.fm episode 23
[97.80 --> 122.46]  welcome to go time i'm your host my name is chris and today we're going to be talking about
[122.46 --> 126.98]  some of the news some of the news surrounding go just some fun collection of articles
[126.98 --> 131.52]  uh the last time we did this we got some really good feedback from you wonderful listeners and
[131.52 --> 136.78]  you seem to enjoy that episode a lot i'm not sure if there will be as much laughing in this episode
[136.78 --> 144.42]  but uh we we can try we can see joining me today as co-host is ian how are you doing today ian
[144.42 --> 150.28]  i'm doing well i do think we might uh miss some johnny's laughter but we'll we'll do the best we can
[150.28 --> 155.92]  yeah we'll still we'll still try to keep it fun and uh and interesting and hilarious as best we can
[155.92 --> 163.80]  so yeah first up from our our nice list of articles here there's an article titled go evolves in the
[163.80 --> 170.08]  wrong direction and i guess the summary of this article is that the the author feels that go
[170.08 --> 178.76]  is getting more complex and dislikes this added complexity and the most notable thing that he
[178.76 --> 182.80]  points out or i guess a couple notable things he points out is the addition of generics in 118
[182.80 --> 190.62]  and then the upcoming edition of iterators in 123 so ian what are your what are your thoughts on this
[190.62 --> 196.46]  yeah i don't know um i guess i do know i think i kind of disagree i do think it's getting more
[196.46 --> 202.06]  complicated i don't think that's something we can say isn't happening but generics i i think was a
[202.06 --> 207.00]  needed feature and i think it's worth the added complexity especially since i think in a lot of
[207.00 --> 213.42]  everyday go you don't even notice it and then the range over function iterators i'm kind of skeptical
[213.42 --> 219.02]  about this but i'm also really excited i've played with it some and it is like the function signatures
[219.02 --> 225.62]  are hard and it kind of is confusing but having a standard way to iterate is something that i've
[225.62 --> 232.00]  wanted in go for ever so yeah i don't know what do you think i mean generics it did add a lot of
[232.00 --> 237.34]  complexity to the language itself from like a specification perspective but yeah i haven't
[237.34 --> 243.12]  really seen them like abused i haven't seen them make things worse in any way so i think it's it's
[243.12 --> 247.56]  it's like a for the everyday go user i don't think it added much complexity i think it just added
[247.56 --> 252.44]  complexity on like the if you want to implement go or if you want to maintain go and there's all
[252.44 --> 257.18]  sorts of very complex things about that so i don't know if that complexity argument applies as much
[257.18 --> 262.62]  and i think there have been some useful productivity gains for some things like i use the slices package
[262.62 --> 266.56]  like all the time now because it's just there i'm like oh i can just do this instead of having to
[266.56 --> 271.30]  remember that wonky syntax that i'd always have to look up because i can never quite remember it
[271.30 --> 275.44]  unless i've been typing it a whole bunch lately so it's just nice to break out the slices package
[275.44 --> 281.02]  and be like oh slices not this or slices not whatever especially slices.clone that is one that i always
[281.02 --> 286.14]  like was like this is terrible i don't want to have to do this three lines of nonsense to get a clone slice
[286.14 --> 291.40]  so i think on that aspect i don't really agree with with him that like generics have made the
[291.40 --> 296.70]  language considerably more complex as far as iterators i'm not really sure how i feel about
[296.70 --> 305.86]  this because it's on the one hand i i really like this idea i see his argument around not liking
[305.86 --> 311.28]  the potential complexity that can come from looking at a line that says like for range and have it
[311.28 --> 316.00]  previously been like okay well that's like a static thing that's not gonna like
[316.00 --> 322.04]  block for a long period of time trying to get the next iteration of something and now that could be
[322.04 --> 325.78]  a thing that happens because you might be making a network request in there or something like that
[325.78 --> 331.42]  but i think that's just like a thing we have to get used to over time because then it's just it's more
[331.42 --> 335.84]  just like a regular for loop with a function in it except sometimes that function might be like a
[335.84 --> 341.78]  little hidden but i do think like the tooling we have now will make it blatantly clear that this is a
[341.78 --> 348.02]  function this is an iterator powered by a function and you got to dig into that somewhat to see if
[348.02 --> 352.44]  there's something i'm going to dig into that to see you know what might be the issue at hand but
[352.44 --> 358.72]  having designed things that have iterators in them before i think this will be much better overall
[358.72 --> 364.08]  because i think that is a very inconsistent pattern across not just the standard library but across go
[364.08 --> 370.64]  packages in general of like oh do you have a next function that just returns okay if there's
[370.64 --> 375.48]  something you can get next or does it return like we have a thing that just returns like an object
[375.48 --> 380.32]  in an error or an object in okay and like there's just like so many different patterns and it's hard
[380.32 --> 386.50]  to know like which one you should use in a given circumstance and i think this at least helps out with
[386.50 --> 391.90]  some of them where you just want to use the kind of like object okay pattern and then you probably
[391.90 --> 396.06]  have like a separate like error function and then you have that kind of standard sort of like what the
[396.06 --> 401.76]  database sql package does where it's like oh you do the check the error afterward if you get kicked out
[401.76 --> 408.62]  of the loop so i think it will be a useful addition it adds a little bit of complexity yes but i don't feel
[408.62 --> 414.94]  like it adds such a tremendous amount of complexity that it's going to be like difficult for new people
[414.94 --> 419.18]  to learn this i think it's going to be more difficult for people that have been writing go for a long
[419.18 --> 424.86]  time to adjust to this yeah i think it might be a lot like generics where you don't see it a lot in
[424.86 --> 429.74]  every day but when you're implementing libraries you're going to be using it right so i think it
[429.74 --> 437.80]  could end up being like that yeah i do think like the push pull semantics are a little wonky like i
[437.80 --> 441.34]  don't i don't i don't know how i feel about them as far as like trying to implement it and trying to
[441.34 --> 446.20]  get all of that right we have to see i guess how it all shakes out i haven't looked at this in a while
[446.20 --> 451.42]  either since it kind of first came onto the scene so i'm not sure how much it's shifted from
[451.42 --> 458.20]  how it was before but i mean in general i just i don't see how this like necessarily makes the
[458.20 --> 466.50]  language worse or makes it immeasurably more complex compared to how things were before outside
[466.50 --> 472.78]  of that one instance of now you look at a four range statement and it could do something arbitrary
[472.78 --> 478.34]  in there it could cause side effects it could like pause for a long time outside of that it's like
[478.34 --> 485.08]  i don't i don't know there was just like kind of debugging argument that he was making that i was
[485.08 --> 489.10]  sort of following but i'm not really sure how that's going to shake out in the actual implementation
[489.10 --> 493.38]  as far as like when you look at it if it's going to look i don't think it's going to look this weird
[493.38 --> 498.84]  when you look at it the iterators but yeah i think that's also something that can be worked out in the
[498.84 --> 503.46]  error messaging and the stack traces right i don't know there's also an argument here that it
[503.46 --> 510.70]  implicitly transforms returns continue breaks defers all of those and i understand that that does add
[510.70 --> 515.16]  complexity and like when you're thinking but as far as writing code i think that makes it a lot more
[515.16 --> 521.66]  simple i don't have to learn how to do these things outside of the actual keywords right like trying to
[521.66 --> 528.04]  continue inside a not like a custom iterator now is kind of a nightmare yeah right and there's been so
[528.04 --> 533.38]  many times i'm like i would like to continue here please so i i honestly do think it's going to be
[533.38 --> 539.26]  simpler overall just being able to use your normal semantics and yeah keywords yeah because that's
[539.26 --> 546.00]  like i was uh using the gold mark package the other day and it has like this ast walking thing and you
[546.00 --> 552.06]  have to like return special things to be like oh continue or like exit or whatever and i was like this
[552.06 --> 557.04]  this is this is kind of wonky i don't know if i like this as much and then also like error handling
[557.04 --> 564.54]  sucked a whole lot and i think it's kind of easier to apply your own error handling if you can just do
[564.54 --> 571.98]  a regular for loop here or for range loop because you can just have the captured error variable that
[571.98 --> 577.58]  should still work is i think it should work let's see why it wouldn't work i know there's also the
[577.58 --> 582.00]  argument that this is one more way to iterate right but i think that argument kind of falls
[582.00 --> 586.50]  flat because it's not like there were standard ways to iterate before right so we're not
[586.50 --> 593.14]  introducing a new standard it's just we're agreeing on a a pattern um yeah making an attempt to
[593.14 --> 600.28]  consolidate or at least give people a a predefined path to go on and not just like what packages have
[600.28 --> 605.66]  you been using and deciding how you want to design your iterator based on what packages you've seen
[605.66 --> 609.32]  how you have an actual like well this is how you can canonically do it in the language and
[609.32 --> 614.06]  you can still go do it by under the way if you wish but this is how the way people are probably
[614.06 --> 621.50]  going to be most familiar with yeah so to sum it up i'm not sure it's going in the wrong direction um
[621.50 --> 626.30]  yeah it's kind of a it's a it's a very bold and broad statement
[626.30 --> 633.02]  maybe like it's evolving in the wrong direction i think it it's i think the only direction that languages
[633.02 --> 639.08]  can evolve especially if you want backwards compatibility guarantees is to become more complex over time
[639.08 --> 645.90]  like i think through that complexity too you can gain simplicity right so i think there's a weird
[645.90 --> 652.66]  argument in here about like yes we have to keep all of these old iterator styles but perhaps you know
[652.66 --> 658.74]  not forever like we have ways of deprecating things even in the standard library now so it's like it gives
[658.74 --> 664.36]  us a path toward all of the iterators eventually looking the same or being able to like convert one
[664.36 --> 668.04]  iterator to like this style of iterator in the future with some like glue code or something
[668.04 --> 675.16]  so it seems like it feels like it will have the eventual effect of making things more simple in the same
[675.16 --> 681.08]  way that generics had the effect of making things more simple for example from the slices package right
[681.08 --> 684.84]  now you don't have to implement your own slices package or implement all these functions all of the time
[684.84 --> 690.26]  or you don't have to you know write those same lines of code that are kind of confusing if you don't
[690.26 --> 695.48]  understand that pattern already i think most people if you see the word slices.clone you're like i bet this
[695.48 --> 699.88]  clone's a slice right it's very it's very straightforward what that means so i think like
[699.88 --> 706.30]  yes on the i think on the small scale it might add complexity to language but i think on the large scale
[706.30 --> 713.56]  it's making the language go in a good direction toward more of the the simplicity that we want
[713.56 --> 718.40]  because yeah if you don't want to have any added complexity then you just can't add anything to the
[718.40 --> 724.86]  language and that is also a bad thing for the language yeah i like that that small scale versus big scale
[724.86 --> 731.40]  like it's making the ecosystem simpler not the language simpler right and there is a kind of
[731.40 --> 737.98]  somewhat strange argument at the end here too where he talks about like oh like we should have more simd
[737.98 --> 744.32]  instructions and things like that because go is losing in the performance space to to rust and i mean
[744.32 --> 749.68]  we can talk about this with the next article but i i don't i don't really know if like go is that
[749.68 --> 755.18]  great of a language for performance critical things it's not terrible for performance critical
[755.18 --> 761.58]  things but i don't think that's like the target that go is usually going for most of the time it's
[761.58 --> 766.48]  not like that when i think of go i don't think of like oh i need like low level raw performance i think
[766.48 --> 773.42]  like oh i i want a language that allows me to maintain you know large code bases that do you know a
[773.42 --> 776.92]  whole bunch of different things and i want to be able to actually maintain it with you know somewhat
[776.92 --> 783.42]  large team of people yeah i do think that's a good transition to the next article yeah so this one
[783.42 --> 790.94]  isn't so much of an article as it is a post on reddit and someone asking are an argolang uh what
[790.94 --> 801.04]  software shouldn't you write and go and i interestingly i i feel like the people that commented like some of
[801.04 --> 807.22]  the top comments i just i'm just like you're all oddly wrong like most of it is about like oh garbage
[807.22 --> 812.96]  collection is is a barrier like one of the comments literally says garbage questions a barrier for some
[812.96 --> 821.64]  hard real-time processes and there was an interesting other reddit thread i found it was about same sort of
[821.64 --> 830.58]  thing of like well why do we keep saying that go is bad at real time and the argument and people people
[830.58 --> 837.18]  were uh people basically said like what do you mean by real time like what type of real-time constraints
[837.18 --> 842.30]  are you talking about and this is very insightful just like you know real time doesn't necessarily
[842.30 --> 848.00]  have to mean like as fast as possible it could also just mean like at a fixed interval but also like
[848.00 --> 855.10]  you know we're not in the go certainly not in the pre-go 1.5 era or in the even 1.5 1.6 era where
[855.10 --> 860.84]  garbage collection pauses were you know 10 milliseconds out of every 50 milliseconds now it's
[860.84 --> 867.88]  sub millisecond max garbage collection pauses i think it's like 100 microseconds is where they've
[867.88 --> 873.56]  gotten it down to for the like the the longest like worst case garbage collection pause which for most
[873.56 --> 880.20]  real-time systems seems to like that shouldn't that does not feel like it makes a large difference
[880.20 --> 885.72]  for most people as far as gc is concerned so i don't i don't really buy that whole argument of
[885.72 --> 893.66]  it's bad at doing things that need to be real time but uh what do you think i mean i get what they're
[893.66 --> 900.90]  saying right like i'm not gonna write some invest embedded like firmware and go that needs to
[900.90 --> 906.46]  recalculate something at 100 hertz right like that it just doesn't make sense anyways but yeah i think
[906.46 --> 911.88]  i think people are still kind of confused about the stop the world gc stuff yeah i don't think people
[911.88 --> 916.78]  like that also goes to like my thing i always remember of like you don't have a garbage collection
[916.78 --> 922.68]  problem you have a garbage problem like if if the garbage collector is getting in your way it
[922.68 --> 928.52]  probably means that you have done something pretty awful with your memory management you need to go
[928.52 --> 932.86]  fix up your memory management like garbage collection does not mean you don't do memory
[932.86 --> 938.38]  management it means you don't have to write as much of the the code to management as intricately but
[938.38 --> 942.78]  you still have to do memory management yeah i also saw a lot of arguments on here you shouldn't write
[942.78 --> 948.02]  like guis with go and i i think i would tend to agree with that like that's just not what i would
[948.02 --> 955.00]  reach for i think there are some like decent libraries now but yeah i don't know yeah i think guis is
[955.00 --> 963.30]  especially when like the native platform like languages and apis are like just so strong i think
[963.30 --> 967.40]  it's kind of weird i guess it depends on like what you're trying to do if you're like trying to do like
[967.40 --> 972.54]  an open source project and you don't want to write three at least different platforms worth of guis
[972.54 --> 979.14]  maybe you can do it and go but there's also like other tooling that can do that for you things like
[979.14 --> 984.80]  react native or like even just using web views to do most of what you want and then writing in
[984.80 --> 991.44]  javascript and html and css so yeah i would say yeah guis guis are a little of a weird thing i probably
[991.44 --> 997.64]  would try and learn the languages of the platforms i want to use over just like trying to use go and
[997.64 --> 1003.22]  shoehorn it for all the different types of uh platforms i might be using another interesting one
[1003.22 --> 1009.90]  here too was like the deeply nested json argument of like trying to parse that out and i think that
[1009.90 --> 1015.78]  comes down to like we don't have a culture right now people implementing their own json decoders people
[1015.78 --> 1021.80]  usually just want to throw a struct at the decoder and be like please place all of the things into
[1021.80 --> 1027.64]  this nicely thank you so yeah i think without having better like custom json decoder building tools
[1027.64 --> 1033.70]  those deeply nested really just deeply nested any type any type of like that you know configuration
[1033.70 --> 1040.90]  style language whether that's eml or json or maybe even toml it gets pretty hairy and annoying when
[1040.90 --> 1045.26]  you're trying to you know do some things and go if you don't haven't built up that custom
[1045.26 --> 1050.84]  encoder or decoder yeah i think i agree with that on the same line of decoding encoding stuff
[1050.84 --> 1056.02]  it's not in the article but i would not use go to write anything that interacts with like
[1056.02 --> 1063.52]  canonical xml saml anything like that um yeah i've gone down that path and it is you end up like
[1063.52 --> 1070.02]  calling into a c library to make your xml canonical and oh yeah yeah if you need to do canonicalization
[1070.02 --> 1076.64]  that's that's tough i think xml in general is is fine like i worked in an xmpp server for a few years
[1076.64 --> 1085.06]  and like it was not like go was not the the issue at hand that we had and or go parsing xml and it's
[1085.06 --> 1091.40]  pretty simple yeah i haven't had as much issue parsing xml with go as writing xml yeah go just
[1091.40 --> 1096.12]  doesn't handle like namespace as well it doesn't handle other xml features well yeah i feel like
[1096.12 --> 1101.20]  that's probably also part of just like we haven't we don't really have good libraries for doing that
[1101.20 --> 1105.72]  so it's like good libraries for doing that then it's kind of rough to do it i guess that's the same
[1105.72 --> 1110.40]  argument for like the deeply nested json or really like any of these encoding decoding things it's like
[1110.40 --> 1115.76]  if we don't write tools that make it easier to do those things then it's just going to wind up being
[1115.76 --> 1123.54]  not great yeah i don't know if you've had to use soap with go before i would say avoid it i mean i
[1123.54 --> 1128.76]  try to avoid soap as a in general as a whole i don't sometimes you don't have a choice you don't
[1128.76 --> 1138.30]  have a choice yeah it's true but yeah oh god so i think my favorite comment on this whole thread
[1138.30 --> 1143.32]  though is excel macro should not be written in go ah yes and then someone disagreed and they're like
[1143.32 --> 1150.90]  i'd rather write it in go than visual basic as like or vba like uh i okay yeah i mean true but no
[1150.90 --> 1157.66]  sure i mean really no one should be writing excel macros those things are dangerous but
[1157.66 --> 1163.80]  yeah i don't know the the custom function and google sheets are real nice sometimes but that's
[1163.80 --> 1170.32]  just javascript i don't even know what excel macros are written in is it vba only i think so
[1170.32 --> 1175.64]  i don't know i think you can write a whole bunch of different like microsoft languages but it's just
[1175.64 --> 1179.46]  yeah i guess it's mostly vba especially if you want it to be cross-platform but you only care
[1179.46 --> 1184.52]  about windows i imagine you can write it in like c sharp or something maybe i have no idea i don't know
[1184.52 --> 1190.50]  how excel macros work i don't write them because i like spreadsheets i don't like spreadsheets job title
[1190.50 --> 1197.20]  excel macro engineer that could be i mean well the world runs on spreadsheets so i'm sure there's
[1197.20 --> 1204.52]  many a people who have many a custom macros to make everything work yeah anything else on this uh
[1204.52 --> 1210.62]  this list of uh responses oh someone said they write everything and go
[1210.62 --> 1218.76]  oh god i'm actually like trying to answer this like is there a class of software you should not
[1218.76 --> 1224.46]  write and go i don't think there is yeah i mean i don't i don't think there is i think i think like
[1224.46 --> 1230.44]  there's software that might be slightly better to write in another language but and this is kind of
[1230.44 --> 1235.34]  like a thing i've been thinking about a lot lately it's probably like another another podcast idea
[1235.34 --> 1241.00]  or another podcast episode idea but we can also talk about if we have time where i've been reading
[1241.00 --> 1246.42]  a bunch of leslie lamport's work mostly because i haven't read the paxos paper in a long time the
[1246.42 --> 1252.28]  part-time parliament and i was like i think looking for something else that he had written
[1252.28 --> 1258.02]  and i came across like uh basically leslie lamport has this very long list of all his written works
[1258.02 --> 1264.86]  i think currently 193 works long so he's written a lot of stuff over his career and in the kind of
[1264.86 --> 1270.32]  blurb he writes about paxos in the part-time parliament parliament he's like oh this is this is a
[1270.32 --> 1274.48]  simple algorithm and he doesn't really he's like i don't understand why people don't understand
[1274.48 --> 1278.80]  this algorithm so i said something i read that paper and then after reading that paper i was like
[1278.80 --> 1284.04]  oh this is kind of simple and so i went through and like got a whole bunch of other papers so i'm
[1284.04 --> 1289.82]  gonna read all of these and there's one of his papers where he's talking about teaching concurrency
[1289.82 --> 1295.96]  and kind of like his suggestions for how we should teach concurrency to students specific computer
[1295.96 --> 1302.14]  science students and computer engineering students and there's this really great line in that paper
[1302.14 --> 1307.58]  and actually let me like pull it up so i can read it correctly and he's talking about like
[1307.58 --> 1312.44]  computation here so he says how should we describe computations most computer scientists would probably
[1312.44 --> 1317.20]  interpret this question to mean what language should we use which i think is kind of the question we're
[1317.20 --> 1322.32]  asking here of like i don't know what things shouldn't you write and go what things shouldn't you use
[1322.32 --> 1327.90]  this language for and then he says imagine an art historian answering how would you describe
[1327.90 --> 1334.70]  impressionist painting by saying in french which is just a hilarious line and just it's one of those
[1334.70 --> 1341.28]  like deep and subtle cuts at us as an industry because it's true it's like we talk about like oh
[1341.28 --> 1346.16]  you shouldn't use that language to build that thing it's like saying you shouldn't write that novel in
[1346.16 --> 1349.74]  french because it's not a good like you should write all novels in english because english is a good
[1349.74 --> 1355.64]  language for writing novels and it's like we should we should not be thinking about things in that way
[1355.64 --> 1360.50]  kind of his point it's like we should be talking about this stuff in form of concepts and i think
[1360.50 --> 1368.02]  that's you know true of this discussion as well of like i don't think that there are things that you
[1368.02 --> 1372.42]  there certainly aren't things you can't write and go if you can write them in any language go is a
[1372.42 --> 1376.62]  turning complete language which means it's equivalent to all of the other languages there might be like
[1376.62 --> 1382.24]  missing apis you might have to like go do some ffi stuff and to see to like make it work or do other
[1382.24 --> 1387.46]  weird assembly stuff but there's not like a fundamental thing that you can't do with that
[1387.46 --> 1390.74]  you can do with go and can't do with another language or you can do with another language
[1390.74 --> 1396.26]  you can't do and go so i think it's like more about the concepts that matter and can you express
[1396.26 --> 1402.24]  those concepts well and go but also there's like the whole other other argument as well of just like
[1402.24 --> 1407.52]  i don't know if you're doing a startup or something like that or creating a project you know is go your
[1407.52 --> 1412.22]  strongest language that's probably the language you should write that thing in right so if you're like
[1412.24 --> 1415.68]  for example when you're talking about early about guis it's like okay if you need to build a whole
[1415.68 --> 1421.12]  bunch of guis and go is your strongest language perhaps it's just better to make a slightly uglier
[1421.12 --> 1428.04]  gui and learn something like fine so you can just implement a gui with that and then have the
[1428.04 --> 1433.22]  application you want and then move on instead of having to like learn a whole new language just to
[1433.22 --> 1441.42]  build a gui right it's like oh i gotta learn swift and c sharp and i guess c plus plus for linux i don't
[1441.42 --> 1446.54]  know what linux guis are made in but you know go learn three other languages to go express this
[1446.54 --> 1453.96]  same concept seems kind of silly it's like yes go oh you you want to like write this same story but
[1453.96 --> 1458.10]  you need to write it in like four different languages now like that feels a little weird if
[1458.10 --> 1462.84]  you could just write it in the one it can still be accessible to everybody we're right back to the
[1462.84 --> 1469.52]  ask a question in software engineering and the answer is it depends um yeah yeah i mean i guess the
[1469.52 --> 1473.92]  answer to this is like what software shouldn't you write and go is it's mostly just like i don't
[1473.92 --> 1480.24]  know just just write and go like if you know go go to strong language write and go like and if that
[1480.24 --> 1483.98]  doesn't work for some reason or other reason then i'm gonna write in something else but i think it's
[1483.98 --> 1491.14]  yeah yeah i don't think there's any broad answers that that work for this kind of certainly you know
[1491.14 --> 1495.68]  there's no broad answers that'll fit into like a reddit response that is reasonable to read right
[1495.68 --> 1501.50]  when people say like can't build real-time systems in it it's like no like nuance is required there
[1501.50 --> 1507.90]  like if i'm writing like spark jobs i'm not gonna write them and go though because it's python or scala
[1507.90 --> 1513.02]  right like that's the supported languages like i think there's an argument for tooling here right
[1513.02 --> 1519.48]  like don't shoehorn go into things where there is no tooling yeah just because you want to i mean it
[1519.48 --> 1524.76]  also depends on your goal though right because it's like if you have that argument then there will
[1524.76 --> 1529.40]  never be tooling for that thing in that space right if no one does it then there's never gonna
[1529.40 --> 1534.66]  it's not it's not gonna be in that space right that creates like those artificial barriers and i think
[1534.66 --> 1540.82]  like even even thinking in this way is indicative of i think of the problem that like leslie lamport was
[1540.82 --> 1547.14]  bringing up in that conversation which is like or in that paper which is like if we think in the
[1547.14 --> 1552.80]  framing of like certain languages are good for certain things then we're not really thinking about the
[1552.80 --> 1558.32]  problem itself right we're thinking about this other colored version of the problem of like okay
[1558.32 --> 1563.22]  this problem in go and then it's like oh well now if we go to another language you have to solve that
[1563.22 --> 1570.56]  problem in a different way in that language which is i don't know not not not the not the best of
[1570.56 --> 1577.70]  situations but that's like a larger industry level thing we gotta solve for yeah i agree with you there
[1577.70 --> 1582.60]  but i think there's some leeway on both sides like at the end of the day you gotta make money you gotta
[1582.60 --> 1588.92]  get stuff done yeah you gotta get stuff done i don't know yeah i guess it's like once again like
[1588.92 --> 1595.28]  the big view versus the little view from a individual person standpoint uh or a small company standpoint
[1595.28 --> 1599.74]  yeah there's probably some things you shouldn't write and go and you gotta make that trade-off but
[1599.74 --> 1605.64]  it's also like a different type of question because the difference you post a question to a company
[1605.64 --> 1612.60]  versus toward an individual i would say so yeah you're right it's a you know it it depends it
[1612.60 --> 1621.68]  depends it depends uh yeah that's lord the answer to all the questions it depends yeah you know there's
[1621.68 --> 1628.92]  a whole whole series over on uh on changelog i think it's a changelog and friends series it depends
[1628.92 --> 1633.66]  i did an episode it was fun there's many more episodes you should i have not listened to that yet i'll
[1633.66 --> 1638.08]  have to check it out so i'll go listen they're good episodes they're fun all right do we have
[1638.08 --> 1643.04]  anything else to say on what software shouldn't you write and go it's a choose your own adventure
[1643.04 --> 1649.76]  i do think that leads interestingly into the make files written and go alternatives to make written
[1649.76 --> 1656.84]  and go um should you write an alternative to make and go i think probably yes yeah yeah i mean make
[1656.84 --> 1664.94]  also make is for a number of reasons pretty awful it's like standard which is nice but like that
[1664.94 --> 1673.08]  whole only using like tabs thing and so many other weird syntactical things about make and make files
[1673.08 --> 1681.40]  is just exhausting and like i i you know for well-established projects or i think ecosystems like
[1681.40 --> 1687.90]  see and you know that that have this more baked into them it makes sense but for go it's always
[1687.90 --> 1696.34]  like make files always feel so awkward weird in go so i think i've always like reach for some other
[1696.34 --> 1702.74]  alternative have you used any of the alternatives mentioned in the article i think i've used mage a few
[1702.74 --> 1707.90]  times i don't think i've ever used task file um also i hate yaml so i don't think i want to use task
[1707.90 --> 1713.94]  well yeah we use mage pretty extensively where i work and i think like the one of the great parts
[1713.94 --> 1720.36]  about it is like i don't have to learn all the weird extrinsicities how do you say that oh
[1720.36 --> 1729.82]  extrinsicities yeah of the aws cli for doing stuff like go has a great aws sdk right so we can do all of
[1729.82 --> 1735.50]  our like automated s like aws stuff in a mage file and it just works it's oh it's amazing i would
[1735.50 --> 1741.92]  definitely recommend that's nice yeah and just being able to keep everything in go sounds nice
[1741.92 --> 1748.22]  i mean having the full power of like a full actual turning complete language is is nice and not having
[1748.22 --> 1752.66]  to do kind of as the author points out all of this kind of bending over backwards to make stuff work
[1752.66 --> 1759.50]  with the shell and the weird version of the shell that make has yeah being able to do real for loops
[1759.50 --> 1765.36]  is real nice yeah not that the shell can't do for loops but it's i i mess it up every single time i try
[1765.36 --> 1773.64]  real for loops and logging and you know execution of parallel commands and a whole bunch of other
[1773.64 --> 1780.34]  stuff that's just like this is like easier to do in go than it is to do in in other things so yeah i
[1780.34 --> 1785.58]  mean i'm fully on board with things like mage um once again i don't when it comes to task file i don't
[1785.58 --> 1794.20]  really see i guess if you don't want to learn make like the syntax of make and you're happy with yaml
[1794.20 --> 1800.66]  then it's good but i just really do not like yaml there's just so many so many oddities like i was
[1800.66 --> 1805.78]  writing yaml inside of markdown the other day and it was like i was getting some weird error from it
[1805.78 --> 1811.54]  because oh because i was writing it and it was like converting my tabs to spaces spaces tabs i don't
[1811.54 --> 1815.90]  know which but the yaml parser didn't like the fact that it was not using the correct spacing type
[1815.90 --> 1820.40]  and it and it blew up with some weird error and i was like this is this is obnoxious i don't like
[1820.40 --> 1830.62]  this like white space important syntax is not what i enjoy in life so i would probably just sit down
[1830.62 --> 1835.76]  and use make or really just use mage or something like that instead of task file but i'm sure plenty
[1835.76 --> 1840.92]  of people like this well if we want to diss toml or yaml some more i think one of my most frustrating
[1840.92 --> 1847.14]  days ever was because yaml was not considering something a string i thought was a string
[1847.14 --> 1852.68]  where so you don't have to quote things right but every once in a while that'll bite you so yeah
[1852.68 --> 1862.18]  yeah no that's it's like it's a messy messy markup language for sure i get why why it was created but
[1862.18 --> 1866.94]  you know there's a lot of things we create that sometimes are bad ideas a lot of things in this
[1866.94 --> 1872.94]  industry we create our bad ideas but but yeah no i think like mage mage is cool i think i've used it
[1872.94 --> 1877.16]  a few times in the past if you haven't checked it out you should definitely listen and go check go
[1877.16 --> 1881.40]  check it out um i especially would recommend yeah especially like the fact you can have like a
[1881.40 --> 1887.54]  directory of files so you can kind of like properly manage the structure of it and have your own little
[1887.54 --> 1893.14]  like build system within your code base but i think it's helpful yeah we've actually used mage inside
[1893.14 --> 1900.86]  of github actions too to help manage some of the like build and test scripts and it works real well
[1900.86 --> 1905.26]  yeah it's like it's like you're building your own little build system which if you're only reading go
[1905.26 --> 1910.64]  that's a it's a nice little thing to have yeah yeah i don't know is there much else we want to say
[1910.64 --> 1918.08]  on uh good old mage or good old what are these alternatives to make files that's all i got
[1918.08 --> 1928.34]  do recommend check it out if it works for you it works really well yeah what's up friends i'm here
[1928.34 --> 1935.64]  with two new friends of mine from speakeasy sagar batchu co-founder and ceo and george hadar founding
[1935.64 --> 1942.14]  engineer so for the uninitiated speakeasy takes care of the entire sdk workflow to save you and your
[1942.14 --> 1947.94]  team significant time delivering enterprise grade sdks to your customers in minutes you can
[1947.94 --> 1957.78]  generate best in class sdks in typescript python go java c sharp and even php so sagar what's your
[1957.78 --> 1965.92]  excitement level for apis and this api world we're living in i'm super excited about apis i think we
[1965.92 --> 1972.34]  went to gen zero of the api first revolution and i think we're actually going to a second one now
[1972.34 --> 1978.10]  with the tailwinds of the ai ecosystem kind of causing that to be invigorated so yeah super super
[1978.10 --> 1982.08]  psyched to be working in this space right now i think it's everyone's at a point now where everyone
[1982.08 --> 1988.22]  knows about rest apis and graphql apis and gpc apis and now i think we're actually getting into
[1988.22 --> 1993.70]  the second phase of that which is how do people ship great developer experience in addition to the
[1993.70 --> 1999.14]  apis and how do we build like truly best in class apis that turn into they know long bit of
[1999.14 --> 2004.34]  infrastructure right this is kind of the the vision i think that stripe helped manifest for
[2004.34 --> 2009.62]  everyone in the fintech space which is the an api that really sets the bar for developer experience
[2009.62 --> 2015.22]  but also like it's something you can truly rely on right it's it's a true if you make stripe a
[2015.22 --> 2020.02]  dependency of your company you can feel confident doing that and i think that's that's the part of
[2020.02 --> 2024.82]  api development that really excites me i agree that is exciting so george teams who leverage
[2024.82 --> 2032.42]  speakeasy are those who have leaned all the way in on documenting a solid open api spec and mostly
[2032.42 --> 2038.50]  want to be hands-off of their sdks is that right precisely so you're coming to us because you want
[2038.50 --> 2044.66]  to be hands-off from that process you want to put all of your effort into documenting your api and then
[2044.66 --> 2050.84]  you're trusting and relying on great quality tooling to turn that into code and documentation which is what
[2050.84 --> 2056.36]  we're doing for you you're not meant to change or edit the code because it will be regenerated the
[2056.36 --> 2061.96]  next time you change your open api so you ultimately put it in our hands once you've committed the
[2061.96 --> 2066.92]  changes to your open api it's it's off to the races and you get a new release of your sdk you'll
[2066.92 --> 2072.20]  get a pull request to review you will you will have the opportunity to look at the contents of the code
[2072.20 --> 2078.44]  but quite often you can let it hum along creating sdks for you or new releases of your sdk every time you change
[2078.44 --> 2083.88]  your api very cool well the thing that got me with speakeasy that really helped me understand it was
[2083.88 --> 2090.84]  that as george said it is hands-off you can just focus on documenting your api via the open api spec
[2090.84 --> 2095.72]  and you still have pull requests you still have visibility and in fact they will even hop into
[2095.72 --> 2102.68]  pull requests with you to triage any sort of anomalies or issues that come from the sdk generation and
[2102.68 --> 2109.32]  improve the back end of speakeasy to make future releases better for you i think this is so cool
[2109.32 --> 2115.48]  for teams who want to just be hands-off of their sdks and focus on their product focus on the core
[2115.48 --> 2122.12]  documentation around the open api spec but still have all that awesome visibility okay so the next
[2122.12 --> 2130.04]  step is to go to speakeasy api.dev you can start off with one free sdk that's so cool because you
[2130.04 --> 2137.64]  can go there right now and try it out completely free one free sdk let them know the changelog sent
[2137.64 --> 2142.44]  you let them know js party sent you once again speakeasy api.dev
[2142.44 --> 2157.80]  so the next article we have is uh titled the long overdue problem coming for some people in go 123
[2157.80 --> 2165.64]  this is kind of like an in the weeds article this is talking about a specific compiler directive
[2165.64 --> 2173.56]  called go link name that the go team is starting to really lock down yeah should we explain what it
[2173.56 --> 2179.72]  does yeah yeah so i was about to explain what it does so uh go link name effectively allows you to uh
[2180.44 --> 2187.24]  reference an object or a symbol or something like that that you would usually not be allowed to access
[2187.24 --> 2195.00]  so for example you can use it to access a unexported you know variable or function in a
[2195.72 --> 2201.48]  in another package so you can have some package that has some type or some you know function foo that
[2201.48 --> 2205.96]  would only usually be able to be called from within that package and you have another package you can use
[2205.96 --> 2212.44]  this go link name directive to be like actually i want to be able to call foo from inside my package
[2212.44 --> 2221.80]  which obviously it's necessary for the go team and for go to have this for a number of reasons but it also is
[2221.80 --> 2228.60]  you know kind of not great because it means that now all of your the things you meant to be private
[2228.60 --> 2234.28]  are not really private anymore you just kind of reach in and grab them and take them out and use them
[2234.28 --> 2240.60]  yeah a couple notes on that you do have to import unsafe to use this right so you are the go team is
[2240.60 --> 2246.52]  telling you like hey this is gonna break yeah um so the the changes that they're making is that you can
[2246.52 --> 2253.08]  no longer just go in and grab something out of any package and the next version of go in 123
[2253.80 --> 2260.84]  only things that are explicitly marked as you being allowed to do this will allow you to do it which i
[2260.84 --> 2265.64]  just find to be kind of a funny thing because then this is just like another way of exporting things
[2266.36 --> 2271.24]  because it's like yeah it is a little bit weird yeah it's like i i get i get why we're doing this kind of
[2271.24 --> 2277.48]  gymnastics to make this happen but it's just kind of hilarious yeah you see it a lot in the standard
[2277.48 --> 2285.08]  library library pulling in stuff from the runtime right like if they're gonna lock this down i wonder
[2285.08 --> 2291.00]  why there isn't just a runtime package that is used to pull those things in like there's probably a good
[2291.00 --> 2297.08]  reason but i don't know why yeah and i think this directive also was probably intended to be used for
[2297.08 --> 2300.92]  something else and people found they could use it for this thing and are like oh we'll just you know
[2300.92 --> 2308.60]  use it for this other thing it's also interesting like the particular situation of why the author kind
[2308.60 --> 2314.52]  of stumbled upon this was because of the quick go package that needed to get the default cipher
[2314.52 --> 2321.00]  suites for tls 1.3 and uh and go there was explicit choice made that those cipher suites are not
[2321.00 --> 2327.00]  configurable but also because of you know does your hardware support aes does your
[2327.00 --> 2334.12]  client want to use aes and a whole bunch of other things it's not like a the default cipher suites
[2334.12 --> 2340.20]  might not even be like an actual like stable thing that you can reference which is it's like an
[2340.20 --> 2346.04]  interesting little quirk of this quirk is that you know the reason why it's not an exposed variable is
[2346.04 --> 2351.16]  because it's an extremely complex thing that like can't really be determined until runtime and still
[2351.16 --> 2357.56]  might shift at runtime so it winds up being like this this kind of odd odd space and that's why it's
[2357.56 --> 2363.72]  not an exported thing but yeah just a little bit of a weirdness this whole situation is just weird
[2363.72 --> 2369.24]  overall but yeah it's like a little thing that's going to start breaking random things i'm sure there's
[2369.24 --> 2374.68]  tons of just people that have used this as some sort of pack to get around something and now stuff is
[2374.68 --> 2379.64]  just going to start breaking and people have to figure out how to fix that yeah and the proposal to do
[2379.64 --> 2384.52]  this i think is really interesting because in it ruscox literally says hey this is going to break
[2384.52 --> 2390.44]  stuff but it puts us on a good path forward so it's worth breaking those things which i think i agree
[2390.44 --> 2396.52]  with yeah i mean once again you probably shouldn't be able to just reach into other packages and tinker
[2396.52 --> 2405.00]  with their unexported things like that's that's not generally what we want to happen in the language
[2405.00 --> 2410.36]  yeah i don't i don't know if i have uh have much else to say about this article you got anything
[2410.36 --> 2416.04]  else not really i just think it's interesting that it exists and that it works outside the standard
[2416.04 --> 2421.88]  library yeah i mean a lot of these directives are like interesting little tidbits of like yeah it's
[2421.88 --> 2427.24]  like i like once again i see why these things are are necessary i think like go link name is also
[2427.88 --> 2434.12]  used a lot when you want to refer to something in assembly so you have like a function that's
[2434.12 --> 2439.32]  implemented in assembly use this directive and then it goes and grabs the assembly code and when
[2439.32 --> 2445.00]  the linker is doing its thing it connects them together even though there's no go version of that
[2445.00 --> 2454.20]  assembly so i imagine that usage of it will be left alone but yeah no it is it's it's interesting that
[2454.20 --> 2460.44]  this that this ever worked and that this continues to work i think an interesting thing also for this
[2460.44 --> 2467.56]  proposal to lock it down the 1.23 iterators introduced uh coroutine functionality for
[2467.56 --> 2474.20]  iterators right so you don't have to call out to a separate go routine and and sync back up um and they
[2474.20 --> 2479.80]  say this will not be able these new coroutine functionalities will not be able to be linked names
[2480.36 --> 2488.60]  link named now or ever so they've they've shut that down with this change too so fascinating yeah like
[2488.60 --> 2493.16]  little little little things that probably affect a small very small percentage of the of the go
[2493.16 --> 2500.12]  community as a whole but might have profound impacts moving forward okay and i think the last last
[2500.12 --> 2509.00]  last article we have in our list is called uh go don't name packages common nouns which i don't i
[2509.00 --> 2515.48]  don't know if i agree with this one this one's basically the author is saying like find a a different name a
[2515.48 --> 2524.76]  longer name a multiple noun name for things uh and they give the example of the time rate package
[2525.48 --> 2533.40]  which is in goline.org x and they basically argue like hey like rate is a really good variable name so
[2533.40 --> 2539.96]  it shouldn't be a package name and you should call the package like rate limiter instead and i think i
[2539.96 --> 2547.24]  i think i don't agree with it i think like just because something might be a good variable name
[2547.24 --> 2551.56]  doesn't necessarily mean you shouldn't use it as a package name because at the end of the day packages
[2551.56 --> 2560.68]  are effectively variables yeah i mean i agree with that but the number of times i've accidentally
[2560.68 --> 2566.44]  called a variable url with the url package imported and been like wait why isn't this working yeah but
[2566.44 --> 2571.80]  like what else would you call the url package like i don't have an answer to that either but what do you
[2571.80 --> 2579.96]  call the url that you're building you right like yeah yeah i guess you're right i don't know uh the the
[2579.96 --> 2585.48]  latter part of this section he says in all of his internal packages he generally prefixes them with like
[2586.12 --> 2593.88]  a letter like with p in this case for crunchy platform right i don't hate this i mean i hate the name of
[2593.88 --> 2606.68]  these packages in general like i don't like naming a package server or db or client just feels lazy like
[2606.68 --> 2613.56]  it feels like your your code base isn't structured well if you don't have like a delineation for the
[2613.56 --> 2618.76]  name like i like what if i look at a package client then what is this i guess if you're using the rest of
[2618.76 --> 2625.16]  the import path to say like what type of client this is that works but i guess it's just an outcrop
[2625.16 --> 2630.76]  too of me not liking having lots of small packages and would rather just have one big package and have
[2630.76 --> 2637.72]  it like oh you have like the you know maybe it's the platform or the c platform packet that has a client
[2637.72 --> 2644.68]  in it instead of being like p clients i guess there's times when this will crop up of like you you have to have a
[2644.68 --> 2649.16]  package with this name for some reason or other but i just think it's a bad bad pattern yeah like
[2649.16 --> 2655.80]  this shows up for me like in air packages right like a lot of our services like have a like an in
[2655.80 --> 2662.36]  errors package where we define a bunch of our standard error behavior that's shared between different like
[2662.36 --> 2666.92]  subservices and you don't want to call it errors because then you have to if you're going to call
[2666.92 --> 2673.16]  errors i think you have to implement all of the general error functions from errors right so yeah we end up
[2673.16 --> 2679.64]  calling it like in errors um i don't know maybe that's just a foot gun i'm building right now that
[2680.44 --> 2686.92]  will come back to bite me but i think there's some merit to it yeah like i do think if you're going to
[2686.92 --> 2693.48]  have a package called the same thing as like a commonly used like standard package you should at
[2693.48 --> 2699.16]  least implement all of the like methods and stuff inside that package yeah yeah it does really this is
[2699.16 --> 2705.64]  just another outcrop of like the naming is hard problem in computer science like it's it's really
[2705.64 --> 2711.40]  challenging to name things well all right i guess in general saying like i think i think don't name
[2711.40 --> 2717.80]  things with a noun is like too too blankety it's like too much of a wide purview i think it needs to be
[2717.80 --> 2724.60]  scoped down to to something else what else i don't know but i like using nouns for package i mean if there
[2724.60 --> 2731.08]  was any any hard and fast rules for naming it wouldn't be hard right like if we could create
[2731.08 --> 2738.44]  a rule set that made naming easy i just don't think there is one yeah but i also i hate long package
[2738.44 --> 2748.60]  names though oh yeah yeah so i would rather have it be short and maybe not as obvious than have a package
[2748.60 --> 2757.24]  called like this is my server yeah i don't think it's but that's the thing of like why do you have
[2757.24 --> 2764.68]  a server package like why isn't it just server is a type in another package it's like it's not like
[2764.68 --> 2773.56]  the hdb server package it's http dot server and http dot client because it's the http package so i feel like
[2773.56 --> 2777.96]  that's the sort that's why i don't really like you know the suggestion of like we should call it rate
[2777.96 --> 2783.88]  limiter instead of you know the rate package but then there's other great things you could have in
[2783.88 --> 2791.24]  there besides a rate limiter so it's yeah i guess it's just not like if it's a very general type of
[2791.96 --> 2797.00]  noun that you would use perhaps you need to come up with a more specific thing you want to call it
[2797.00 --> 2803.16]  or make up a name right take a name from another language of what that thing is and then use that i've
[2803.16 --> 2807.88]  done that too many times in the past i will say what not to do is just give it a random name that
[2807.88 --> 2814.36]  means nothing like we have a lot of like things where it's like cat dog you know named after an old
[2814.36 --> 2822.60]  tv show yeah and you have no idea what it does don't do that yeah if you want to go with like the the fun
[2822.60 --> 2828.36]  theme names yeah you got to really dig into the lore whatever it has to all be related like yeah that's
[2828.36 --> 2834.52]  what you like like at a previous job we were building something and for some reason we called
[2834.52 --> 2841.64]  it the matrix so i used matrix characters for all of the different services but it fit with what those
[2841.64 --> 2847.48]  characters were in the franchise so like made sense compared it was a whole thing but like you got it
[2847.48 --> 2852.44]  you got to go all in if you want to use some sort of reference like that and throughout your code yeah we
[2852.44 --> 2861.08]  had one called api card like apicard like picard the star trek captain and that one like worked
[2861.08 --> 2867.40]  because it started with api oh yeah apicard yeah no that works i mean that's i think that's how like
[2867.40 --> 2872.52]  they kind of stumbled into go please because they had go lsp and they're like oh we can just
[2873.64 --> 2878.52]  rearrange some of these letters so sometimes stuff like that falls out yeah go please like clear what it
[2878.52 --> 2884.12]  does well i guess kind of i guess i knew it as go lsp before go please yeah but it's not like so it
[2884.12 --> 2890.12]  might be confusing yeah it has all the right letters yeah but it's easy to like once you look at you're
[2890.12 --> 2895.96]  like oh that's what this is okay but yeah i'm not i'm not completely sold on the don't use common nouns
[2895.96 --> 2904.12]  for package names i don't it doesn't have enough nuance for me that's not subtle enough for me but once
[2904.12 --> 2909.48]  again it works for you works in your code base if you like the letter prefixing uh i'd say go for it
[2909.48 --> 2914.60]  as long as like everybody on our team is on board with that as well yeah it's like any other pattern
[2914.60 --> 2920.92]  like don't just start using it like if you're gonna use it use it and document it and tell everyone to
[2920.92 --> 2928.44]  use it yeah we have anything else to say about not using package names that are common nouns not really
[2928.44 --> 2935.32]  how do you feel about underscores and package names oh no i don't i don't want to i don't want
[2935.32 --> 2939.80]  to be typing an underscore when i'm typing package that's just no what about underscores and file names
[2939.80 --> 2945.64]  that aren't test that's fine you think that's fine yeah yeah so you want to be able to like read the
[2945.64 --> 2949.64]  file like i only have to type the file like once and the file doesn't have like i'm not writing the
[2949.64 --> 2954.44]  file name in my code all the time can you even put an underscore in a package name i don't even know
[2954.44 --> 2960.52]  yeah you can't put a hyphen but you can't put an underscore at least i'm reasonably sure you can
[2960.52 --> 2965.88]  put an underscore but yeah i know i i'm yeah you can't put a you can't put a hyphen but you can't
[2965.88 --> 2971.96]  put an underscore but yeah i like if your package name is getting too long i'm like there is something
[2971.96 --> 2977.56]  wrong like you gotta rethink all of this so because yeah once again you're gonna be typing that thing
[2977.56 --> 2981.48]  out all the time and typing underscores sucks i don't like typing underscores that's why i don't want
[2981.48 --> 2985.88]  another package name once again it also means that your package name is long which means that
[2985.88 --> 2989.80]  your line length is going to get long so you're using a long function names there too it's like
[2990.84 --> 2995.64]  yeah yeah i do i do think your your idea that if your package name is getting too long you're
[2995.64 --> 3001.16]  probably doing something wrong and you should figure out what that is that you're doing wrong but yeah
[3001.16 --> 3005.64]  yeah that's all i got
[3005.64 --> 3010.52]  i actually think you should probably leave
[3010.52 --> 3019.88]  unpopular opinions
[3019.88 --> 3026.84]  huzzah unpopular opinions all right ian what's your unpopular opinion can you go first i'm still thinking
[3026.84 --> 3037.48]  i'll make this complicated okay um yes i i think i i think i do want to turn this into uh an episode
[3037.48 --> 3046.28]  idea but i have so i have finally i think figured out why i'm i don't want to say i don't like i think
[3046.28 --> 3054.92]  it's better to phrase it as like i'm meh on rust like i figured out why i'm meh on rust and the reason
[3054.92 --> 3062.60]  i'm like kind of meh on rust which is like not like a strong dislike but like a slight dislike of rust
[3062.60 --> 3067.40]  or like not not even a dislike of rust it's mostly a criticism of the way that rust is sold
[3067.40 --> 3075.48]  um is because of this other paper i was reading by leslie lamport and let me just like once again
[3075.48 --> 3081.56]  pull up this quote because it's i i want to get it right because it's just once again a deep and
[3081.56 --> 3087.24]  subtle cut and i like it a lot okay and then this paper it's a the paper is titled if you want to read
[3087.24 --> 3091.88]  it computation and state machines and i'll just read this this paragraph in the preface and then i'll
[3091.88 --> 3099.72]  talk about why this is the reason why i don't why i'm meh on rust so he says for quite a while i've
[3099.72 --> 3105.24]  been disturbed by the emphasis on language in computer science one result of that emphasis is
[3105.24 --> 3109.96]  programmers who are c++ experts but can't write programs that do what they're supposed to the
[3109.96 --> 3115.16]  typical computer science response is that programmers need to use the right programming specification or
[3115.16 --> 3121.64]  development language instead of or in addition to c++ the typical industrial response is to
[3121.64 --> 3127.72]  provide the programmer with better debugging tools this is the this is the crux of the crux of it here
[3127.72 --> 3133.16]  so uh the the typical industrial response is to provide the programmer with better debugging tools
[3133.16 --> 3138.76]  on the theory that we can obtain good programs by putting a monkey at a keyboard and automatically
[3138.76 --> 3146.28]  finding the errors in its code and for one i find that paragraph that last sentence to be hilarious but i
[3146.28 --> 3154.04]  think that also like gets at why i've kind of disliked this whole aura of like type safety and memory
[3154.04 --> 3159.88]  safety and all of these other type of safeties will like fix the problems that we have with our with our
[3159.88 --> 3165.80]  code and with our software and with our programs it's like the it's a theory based in like i think a
[3165.80 --> 3173.64]  misunderstanding of where the problems with modern day software are and with where software development is and i think
[3173.64 --> 3181.24]  that rust and the kind of ethos around it not saying that the language itself is not good and useful i
[3181.24 --> 3187.96]  think it is good if useful but i think that argument of like we need rust because c is not safe enough
[3187.96 --> 3194.60]  so if we just had a memory safe version of c then our problems would be fixed and i know there's there's
[3194.60 --> 3198.04]  nuance like lots of people have much more nuanced argument of that like it will solve some of those memory
[3198.04 --> 3201.64]  safety problems and then there's other problems we have to solve as well but the big selling point
[3201.64 --> 3207.80]  seems to be feels like it is the way to fix the problem with so much of our software is to add this
[3207.80 --> 3213.40]  memory safety thing to have this this borrow checker that exists in rust and by having this
[3213.40 --> 3219.88]  we will solve some large class of problems and issues that we have and i think what that does is it it
[3219.88 --> 3224.60]  masks that problem that leslie lamport points out of like but we're not getting the programs right we're
[3224.60 --> 3229.64]  not writing the kind of we're not starting from the correct point and if you don't start from the correct
[3229.64 --> 3235.16]  point then you're just trying to like iterate your way toward a good solution at the end of the day
[3235.16 --> 3240.44]  which is like the kind of you know the whole monkey typing code thing is a i think a reference to the
[3240.44 --> 3245.00]  you know you know if you give an infinite number of monkeys typewriters they'll eventually write
[3245.00 --> 3251.64]  shakespeare and i think that's a lot of how we do treat software is like well if you just keep banging at
[3251.64 --> 3258.84]  it eventually you'll shove out the right thing and we can bang on things faster if we have these tools
[3258.84 --> 3265.80]  that tell us when we're clearly wrong and i think what what we should be trying to do is teach software
[3265.80 --> 3271.32]  engineers specifically and i think computer engineers as a whole to actually think like i think that's the
[3271.32 --> 3275.56]  problem we have no one wants to sit down and think deeply about the problems we're trying to solve
[3275.56 --> 3281.08]  and we lack some of the training and the languages that we would likely use to do this thinking and
[3281.08 --> 3286.04]  then this documenting of things mostly like math like you can represent a lot of what we want to
[3286.04 --> 3291.96]  represent with simple math and we kind of run to a language instead which also harkens back to that
[3291.96 --> 3296.92]  thing of like how would you describe impressionist painting like oh in french right like we we run to
[3296.92 --> 3301.88]  programming languages to solve the problems when the problems actually have to deal with the fact that
[3301.88 --> 3306.84]  we're just not writing correct software we're not writing correct programs and we we don't even have
[3306.84 --> 3312.76]  the the frame of reference to know what correct would mean in that case either like we never sat down
[3312.76 --> 3320.04]  and said this is what we're actually trying to do and so i think like when we when we try and run away
[3320.04 --> 3324.36]  from languages like c which is what it feels like we're trying to do so the times people like no one
[3324.36 --> 3328.52]  should ever write c no one should ever do this it's like saying like you know english is a messed up
[3328.52 --> 3333.64]  language and there's a lot of weird oddities with it so we should be moving everybody to esperanto and
[3333.64 --> 3338.84]  nobody should write or speak in english anymore because english is so bad and it's like that's
[3338.84 --> 3343.80]  that's a silly argument right that's not it's not just impractical it's it's rather silly because like
[3343.80 --> 3348.44]  the problems with english don't usually have to do with like the structural language itself has to do with
[3348.44 --> 3354.36]  like the concepts like are we talking about you know concepts incorrectly in english and i think that's
[3354.36 --> 3358.60]  the thing with programming and with software it's like do we have the concepts right are we talking
[3358.60 --> 3364.12]  about the concepts right and it's like this is one of the reasons why i like go is because if you do
[3364.12 --> 3370.12]  sit down and you do really think about what you're building and how you're building it and then you you
[3370.12 --> 3375.24]  document that and you go through this rigorous process of developing it go is a really nice language
[3375.24 --> 3381.08]  to just express that simply and easily it's a language that just doesn't really get in your way and
[3381.08 --> 3386.20]  that when you need some help there's some tooling there for you but you don't have to use the tooling
[3386.20 --> 3392.20]  necessarily um and it also makes it easier to do it on a communal level it has all of those things
[3392.20 --> 3398.28]  right go popularized go thumped which is not like a you know correcting somebody's code but it's making
[3398.28 --> 3404.28]  it easier for all of us to read everybody else's code so we can work collaborative collaboratively together
[3404.28 --> 3409.08]  and so that we can see you know the obvious mistakes here and there between like this is what you were
[3409.08 --> 3413.40]  supposed to do and this is what it's actually doing so once again it's not that i don't think
[3413.40 --> 3417.40]  rust exists i think it's cool that rust exists i think all of these features that it has are very
[3417.40 --> 3423.32]  nifty but i think that that selling point of it really just soured the language for me because it's
[3423.32 --> 3429.48]  so much of that it will replace c or we have to rewrite everything in rust because of blah blah blah
[3430.36 --> 3435.96]  i think it's like much more advantageous for us as an industry to focus on how do we actually get
[3435.96 --> 3442.36]  people to write software correctly and then also how do we bring down the cost of software which i
[3442.36 --> 3448.28]  think are are two of the same thing because right now i think we do have you know too many software
[3448.28 --> 3453.00]  engineers for this amount of software that we're producing because for the most part a lot of us are
[3453.00 --> 3457.40]  just monkeys banging on keyboards being like oh yeah i'm trying to write this thing and oh the compiler
[3457.40 --> 3462.28]  got mad at me oh i guess i can't do it that way oh i can't and you just kind of inflate the number of
[3462.28 --> 3467.56]  of of people you have doing software and even though you're not really doing the thinking part
[3467.56 --> 3473.40]  of it i think this is also what leads to people believing that you can replace software engineers
[3473.40 --> 3480.04]  with ai with kind of like a more advanced version of the current ai we have which makes sense if if you
[3480.04 --> 3485.64]  under if you believe that the whole we're just monkeys banging on keyboards thing is a reality and like
[3485.64 --> 3490.84]  yes as long as we can correct the output of the ai it will be a much faster monkey banging on the
[3490.84 --> 3495.88]  keyboard than a human could ever be but if you recognize that like no we actually need to have
[3495.88 --> 3502.20]  more thought in there than just blindly typing blindly smashing the keys then it's clear that ai is not
[3502.20 --> 3507.16]  going to be able to do those things because ai can't think but yeah that's my very long-winded
[3507.16 --> 3514.52]  reasoning for why i'm kind of meh on rust still think it's a cool language but like the the the way that
[3514.52 --> 3520.44]  it's been propositioned i think is what just sours me on it i think i agree with a lot of you said but i
[3520.44 --> 3525.88]  definitely have a bit of a different perspective on it like maybe rust is saying that you know this
[3525.88 --> 3531.96]  borrow checker this memory safety is gonna save us all and it's what has to happen but in my
[3531.96 --> 3537.24]  perspective like we're all human we're all gonna we're all gonna mess up and we're all gonna design
[3537.24 --> 3543.48]  things poorly or write poor code at some points and what what these memory safety features and what
[3543.48 --> 3550.28]  rust is trying to do is just minimize the impact of that mistake right like if i'm just writing c and
[3550.28 --> 3558.36]  i let up an index overflow and read arbitrary memory like that has big consequences but if i just can't do
[3558.36 --> 3563.64]  that you know i don't know i mean i guess like there's there's kind of two sides to that too where
[3563.64 --> 3569.64]  it's like how much like how many of those types of problems are the problems we're having i think it's
[3569.64 --> 3574.68]  relatively little that like the kind of memory like corruption problems we have are like the big
[3574.68 --> 3577.88]  things i think a lot of the time even when there are memory corruption problems from when there's
[3577.88 --> 3583.80]  like you know buffer overruns and that a lot of that gets patched and the problem is that people
[3583.80 --> 3587.24]  don't update the version of the software they're using so they're using some unpatched version that
[3587.24 --> 3592.44]  has the exploit internet which is part of the the larger thing but i also think there's we like to
[3592.44 --> 3601.72]  think about things as if we have infinite resources and we can do things infinitely fast but there there's
[3601.72 --> 3609.00]  a reality that we can't really be spending all like huge amounts of industry effort on developing these
[3609.00 --> 3617.40]  things but also be spending huge amounts of industry effort on really rethinking and redoing how we teach
[3617.40 --> 3622.52]  software engineers and then retraining the entire industry right like we're not doing that right
[3622.52 --> 3628.12]  we're not we're not shifting toward that type of thing where we actually push software engineers to be
[3628.68 --> 3634.52]  deep thinkers because that is a very hard very resource intensive problem like you know it takes a
[3634.52 --> 3641.16]  lot of energy to teach someone how to think critically it's not a simple thing to do and we just aren't
[3641.16 --> 3647.16]  doing it because i think we can get along well enough since we have these tools that make it so
[3647.16 --> 3653.64]  we can kind of produce software at least somewhat decently because we have all these tools and all
[3653.64 --> 3657.56]  these protections where it's like no like you have to you see and we actually have to find a way to teach
[3657.56 --> 3663.64]  everybody to you see well that's not i don't think that's an impossible thing to do right i don't think
[3663.64 --> 3667.56]  that's an impossibility that most software engineers should be able to learn under tnc i don't think it's
[3667.56 --> 3673.48]  an impossible thing that most people couldn't learn and understand c i think that we have an industry
[3673.48 --> 3678.68]  have just given up on that being a possibility because we well we have these little languages
[3678.68 --> 3683.40]  that are easier and because we think that we can solve the problem through things like oh we just add
[3683.40 --> 3688.12]  this one more type of safety if we add type safety you add memory safety we add you know what have you
[3688.12 --> 3694.68]  that it will be we will get to the point where everybody will be able to write software so i think it's the
[3694.68 --> 3699.16]  these things might actually be a little bit at odds with each other but i definitely think like
[3699.56 --> 3703.56]  we won't fix this as an industry if we keep diluting ourselves into thinking that like
[3703.56 --> 3709.32]  the solution to c is rust or the solution to the problems we have with c is rust because we just
[3709.32 --> 3713.72]  won't we don't fix the problems at the end of the day i mean it harkens back to like a thing that i've
[3713.72 --> 3719.64]  also been thinking about a lot lately with like a few years ago we as an industry went through this whole
[3719.64 --> 3724.60]  thing of saying like oh we need to get rid of these harmful quote unquote harmful words that are
[3724.60 --> 3729.16]  code bases so master and master and slave and blacklist and whitelist and all these things and
[3729.16 --> 3735.72]  there's a huge hubbub and people filed a bunch of prs and we eliminated a bunch of these words and like
[3735.72 --> 3740.44]  you know get we we changed it it's no longer master's default it's main right we went through all of this
[3740.44 --> 3745.48]  effort to change all of these things and this in this idea that like oh these words using these words
[3745.48 --> 3750.20]  are harmful to you know people of color especially black people and they shouldn't have to see them every
[3750.20 --> 3755.88]  day and all of this and i pushed back a lot on that at the time i was like this is not this is
[3755.88 --> 3759.00]  not where we need to be spending our time if people said well we got to do something we should be doing
[3759.00 --> 3764.12]  some things and like we can do this and we can do those other things and then you look at the same
[3764.12 --> 3771.24]  industry as the same people and we're just like you know full-on embracing ai right now and if you go
[3771.24 --> 3778.12]  look at the underpinnings of how all this data is cleaned how these things get trained there's a lot of like
[3778.12 --> 3783.48]  subjugation of like especially people of color going on a lot of destroying of people's mental
[3783.48 --> 3789.08]  health and oppression and like where is that energy from our industry to push back on those things right
[3789.08 --> 3793.00]  we said well we'll get rid of these things this is the first step toward fixing larger problem
[3793.64 --> 3798.04]  but then the follow-through isn't there i think that's the same thing that sort of happens
[3798.04 --> 3801.72]  in obviously a different context for these other things where they oh we got to make software better
[3801.72 --> 3806.76]  so the way we make software better is by fixing the languages but the languages aren't the problem
[3806.76 --> 3811.80]  it's the concepts and understanding that's the problem and that's where the rust isn't helping
[3811.80 --> 3816.52]  but it's not just rust it's like any of these languages that are like we will by making this
[3816.52 --> 3821.48]  language better we will make it so you can write better software and like that's addressing the wrong
[3821.48 --> 3825.88]  problem so i guess at the end of the day you're saying it's not the languages that's the problem it's
[3825.88 --> 3830.92]  us that's the problem yeah that's the engineer once again i think rust is a cool i think i would agree
[3830.92 --> 3835.32]  with yeah and it's like i think rust is a cool language i think people should use rust i think we should
[3835.32 --> 3839.16]  have memory safety and i think the borrow checker is a really cool thing and i think we should have
[3839.16 --> 3844.28]  type safety i think we should have all these tools that help us write software better but we shouldn't
[3844.28 --> 3850.44]  forget that the primary problem with software today is not that we don't have memory safety like we've
[3850.44 --> 3855.88]  been able to write many a systems with really good without having memory safety we've been able to write
[3855.88 --> 3860.20]  many a system without having type safety right and at the end of the day your computer also like you
[3860.20 --> 3863.64]  know assembly doesn't have any of these things that's what's running everything with the
[3863.64 --> 3868.60]  instructions at the end of the day don't have these protections on them so it's like not having
[3868.60 --> 3873.32]  these things doesn't preclude us from writing good software so we should focus on what are the things
[3873.32 --> 3878.60]  that will help us write good software which i i think that this could be a part of it once we actually
[3878.60 --> 3882.68]  teach people how to think about code and how to think about their programs because i think if you
[3882.68 --> 3887.32]  actually do sit down you spend time a lot of time thinking you wind up with massively simpler solutions to
[3887.32 --> 3893.48]  problems and if you kind of aggregate those things together you wind up with massively simpler larger
[3893.48 --> 3897.48]  code bases at the end of the day because if you don't the problem just snowballs like once you're
[3897.48 --> 3904.04]  already in a mess it's so much harder to get out of that mess yeah so we'll see how unpopular that is
[3904.04 --> 3907.56]  i mean they're probably pretty popular with go people because i just said you know go is the is
[3907.56 --> 3911.48]  the ideal language for writing good software well not ideal it's one of the good ones i would say like
[3911.48 --> 3917.56]  lisp is probably one of the more you know ideal languages for the translation at least from the
[3918.20 --> 3924.52]  view of computation if you want to do it rigorously into actual code you can run i think i do have an
[3924.52 --> 3931.00]  unpopular opinion okay go for it and this is something i want to do an episode on i guess the premise is
[3931.00 --> 3937.16]  learning go isn't easy i know we say that a lot like oh go is easy you can you can get it down in an
[3937.16 --> 3943.64]  afternoon and i would go on to expand that learning any new language isn't easy and it's not when we say
[3943.64 --> 3949.00]  learning a language i think a lot of people think learning the syntax of a language right like how
[3949.00 --> 3954.12]  to do a for loop how to assign a variable and i think that's the not even the tip of the iceberg
[3954.12 --> 3958.84]  it's just the pointy part on top and nothing else right learning a language is learning its paradigms
[3958.84 --> 3965.56]  learning like how its normal libraries work it's learning how to write idiomatic code in that language
[3966.28 --> 3970.52]  and that's not like you're never going to get that overnight like that's all going to come with
[3970.52 --> 3976.44]  experience so pretending that any language is easy to learn i think does the whole community a
[3976.44 --> 3981.88]  disservice right acting like you can jump into a language and immediately write good code is
[3982.68 --> 3987.48]  is i don't think realistic at least it's not realistic for me you just don't know enough
[3987.48 --> 3991.80]  to know if you're writing good code when you first jump in so learning any programming language is not
[3991.80 --> 3998.28]  easy learning the syntax is easy the rest is hard yeah i think i i agree with that because i think like
[3998.28 --> 4003.16]  the way i was just kind of translating that in my mind was like if you think about it in terms of
[4003.16 --> 4007.96]  like language as a whole it's like yeah you can you can learn like the syntax and the grammar of like
[4007.96 --> 4014.36]  a particular natural language but also deeply embedded into language is the culture of the the
[4014.36 --> 4020.44]  community that developed that language and it takes a lot of effort to learn that culture and to
[4020.44 --> 4026.20]  understand that culture especially if that's a culture that is somewhat at odds or juxtaposed with your
[4026.20 --> 4031.00]  own or it's like okay like i think this is like the thing between like i have some friends who are
[4031.00 --> 4034.76]  like eastern europeans and the way that they express things in the way that americans tend to express
[4034.76 --> 4039.72]  things is like vastly different especially when it comes to levels of excitement i think that same
[4039.72 --> 4043.64]  sort of thing exists within programming languages where it's like yeah i know the way that you express
[4043.64 --> 4047.24]  something and i mean go and rust are good examples the way you do something and go and the way you do
[4047.24 --> 4052.52]  something in rust are going to be very different because the cultures of those communities are very
[4052.52 --> 4057.32]  different so you might be able to learn in syntax but actually understanding all of that cultural
[4057.32 --> 4064.28]  stuff is is real tough i think that's the perfect analogy for it yeah yeah i know so i think yeah it's uh
[4065.56 --> 4070.28]  i think our our unpopular opinions are like somewhat somewhat tensionally related because it's like
[4070.92 --> 4076.20]  the tough part of of all of this is like figuring out like how do you express what you want to express
[4077.16 --> 4082.20]  in the language in the way it should be expressed in the language i think that's how you wind up with these
[4082.20 --> 4087.72]  these languages that get or these concepts that get siloed into our particular language
[4088.36 --> 4092.92]  is because be like oh well that language is easy enough to learn like i think python and data science
[4092.92 --> 4097.00]  is a good example of this like oh python is easy enough to learn so you can do data science and data
[4097.00 --> 4103.48]  engineering in it and that whole world just kind of gets everything built for it but it's like do the
[4103.48 --> 4108.60]  people doing those things understand conceptually what it is that they're doing and they're simply mapping
[4108.60 --> 4115.32]  those concepts into that language or can they only express those ideas in that language itself and
[4115.32 --> 4119.56]  they can't pull it out to another language i think that's a that's an actual more concise way of saying
[4119.56 --> 4125.24]  my own unpopular opinion is like no we need to need to focus more on having the conceptual understanding
[4125.24 --> 4131.08]  and mapping it into the language as opposed to having the language be our only vehicle for for
[4131.08 --> 4135.56]  expressing that conceptual thing yeah it's almost like we're learning things the wrong in the wrong
[4135.56 --> 4141.56]  direction like inside out yeah instead of outside in we're hyper focused on language which again was
[4141.56 --> 4146.20]  is leslie lamport's point like i haven't finished reading the computation and state machines paper
[4146.92 --> 4154.12]  but in that paper he basically talks about his interesting thing in the beginning of it where he talks about
[4154.12 --> 4163.64]  like oh imagine if we didn't use equations in say physics so you have two different parts of physics that had their own
[4163.64 --> 4169.72]  special notation then it might not be obvious that like e equals mc squared is like the same thing in
[4169.72 --> 4174.68]  these two in two different parts of physics right or you know for for anything right if you don't if
[4174.68 --> 4181.72]  you use dissimilar syntax then it's not going to be easy to recognize similarities and patterns between two
[4181.72 --> 4187.32]  different places or that you have the exact same thing in two different places and so his kind of point
[4187.32 --> 4192.12]  there was like oh well you might you have equations and just because like you have two equations that
[4192.76 --> 4197.72]  say the same thing doesn't mean they do the same thing inside of the you know branch of physics that
[4197.72 --> 4203.40]  you're you're operating within in the same way like you can you know if you put this into natural language
[4203.40 --> 4210.60]  you can say the same english phrase it to two different communities of people and it could mean two vastly different things
[4211.08 --> 4216.84]  even though the words are still equivalent but you have the ability to kind of like understand and translate those things because you have the
[4216.84 --> 4244.04]  similar base of words that you're using and all of that yeah i have that issue talking to non-software people like all a regular software term will slip into everyday language and they're like what are you talking about yeah that that's like that's the you know the beginner to master like you know you've mastered something when you can explain it to someone that doesn't have any context for what it is because like you understand what the concept of the thing is so you can better bring that over to what people want to understand
[4244.04 --> 4251.48]  so yeah i think i think these would be two two good episodes now to get some people that will probably disagree with me and get johnny on
[4251.48 --> 4258.60]  get some uh who else would disagree with me oh maybe i can get sam to come back and disagree with what i'm saying
[4258.60 --> 4263.88]  and another you know gotta gotta gotta if i'm gonna have this as an episode of like yeah
[4263.88 --> 4267.68]  meh on rust for all these reasons gotta have people that are gonna disagree with me
[4267.68 --> 4271.48]  this is assuming that they're gonna disagree with me they might agree with me and then it wouldn't be as fun
[4271.48 --> 4277.56]  or it might be you know sam's stance on rust i i don't i think he's now i won't speak for that i
[4277.56 --> 4282.84]  think he's fine with it but now i don't know that'll be a good thing to learn right yeah yeah i'm interested
[4282.84 --> 4291.00]  to know i'm still undecided on rust so once again i don't i'm probably gonna learn rust like i like me
[4291.00 --> 4295.64]  being met on rust has little to do with like the language or its usefulness or utility like i understand in
[4295.64 --> 4301.16]  the current context it is it's a more macro thing right it's learn concepts people
[4301.16 --> 4304.76]  learn how to think that's the big thing we all need to learn how to think and
[4305.32 --> 4310.68]  and i hope i hope people don't think it's an insult i'm not insulting us as an industry by saying that
[4310.68 --> 4315.64]  we don't think about things like thinking is very difficult to do and it's a very difficult thing to
[4315.64 --> 4322.12]  learn how to do to think critically and intensively about things like so it's not an insult to anybody
[4322.12 --> 4328.12]  to say like we're not thinking it's just a thing that we should fix if we want to build better software
[4328.12 --> 4333.40]  it's like yeah i think it's hard it's hard work we get paid a lot of money we can do the hard work
[4333.40 --> 4341.72]  but yeah that that the that feels like a good place to wrap it up uh any last uh any last words ian i
[4341.72 --> 4348.28]  think we've said it all i think so thanks for joining me and uh thank you listeners for uh listening to
[4348.28 --> 4353.08]  this kind of all over the place episode i hope i hope you enjoyed it as much as the last one we did
[4353.08 --> 4362.52]  that is go time for this week thanks for listening along subscribe now if you haven't already head to
[4362.52 --> 4370.20]  go time.fm for all the ways or simply search for go time wherever you get your podcasts you'll find us
[4370.20 --> 4377.16]  hey do you receive our changelog newsletter each monday if not let's fix that bug one reader calls it
[4377.16 --> 4384.36]  so good he considers it a competitive advantage sign up for zero dollars at changelog.com
[4384.36 --> 4391.40]  slash news thanks once again to our partners at fly.io to our mysterious beat freak breakmaster
[4391.40 --> 4397.30]  cylinder and to our friends at sentry we love sentry you might too use code changelog when you're
[4397.30 --> 4404.06]  signing up for a team plan and save 100 bucks why not right that is all for now but we'll talk to you
[4404.06 --> 4406.38]  again next time on go time
[4406.38 --> 4420.86]  you
