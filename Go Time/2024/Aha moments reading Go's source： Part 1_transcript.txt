[0.00 --> 16.48]  let's do it it's go time welcome to go time your source for wide-ranging discussions from all
[16.48 --> 24.18]  around the go community find us on the web at gotime.fm on the fediverse at gotime at changelog.social
[24.18 --> 31.12]  and on x at gotime.fm thanks to our partners at fly.io the home of changelog.com launch your app
[31.12 --> 37.46]  as close to your users as possible find out how at fly.io okay here we go
[37.46 --> 47.82]  what's up friends i'm here with two new friends of mine from speakeasy sagar batchu co-founder and ceo
[47.82 --> 54.00]  and george hadar founding engineer so for the uninitiated speakeasy takes care of the entire
[54.00 --> 60.42]  sdk workflow to save you and your team significant time delivering enterprise-grade sdks to your
[60.42 --> 70.10]  customers in minutes you can generate best in class sdks in typescript python go java c sharp and even
[70.10 --> 78.08]  php so sagar what's your excitement level for apis and this api world we're living in i'm super excited
[78.08 --> 85.56]  about apis i think we went to gen zero of the api first revolution and i think we're actually going
[85.56 --> 91.06]  to a second one now with the tailwinds of the ai ecosystem kind of causing that to be invigorated
[91.06 --> 95.68]  so yeah super super psyched to be working in this space right now i think it's everyone's at a point
[95.68 --> 101.76]  now where everyone knows about rest apis and graphql apis and gpc apis and now i think we're actually
[101.76 --> 107.50]  getting into the second phase of that which is how do people ship great developer experience in
[107.50 --> 113.22]  addition to the apis and how do we build like truly best in class apis that turn into they know long
[113.22 --> 118.62]  with infrastructure right this is kind of the the vision i think that stripe helped manifest for
[118.62 --> 123.88]  everyone in the fintech space which is the an api that really sets the bar for developer experience
[123.88 --> 129.50]  but also like it's something you can truly rely on right it's it's a true if you make stripe a
[129.50 --> 134.30]  dependency of your company you can feel confident doing that and i think that's that's the part of
[134.30 --> 139.82]  api developer that really excites me i agree that is exciting so george teams who leverage speakeasy
[139.82 --> 146.70]  are those who have leaned all the way in on documenting a solid open api spec and mostly
[146.70 --> 152.82]  want to be hands-off of their sdks is that right precisely so you're coming to us because you want
[152.82 --> 158.88]  to be hands-off from that process you want to put all of your effort into documenting your api and then
[158.88 --> 164.98]  you're trusting and relying on great quality tooling to turn that into code and documentation which is
[164.98 --> 170.70]  what we're doing for you you're not meant to change or edit the code because it will be regenerated the
[170.70 --> 176.66]  next time you change your open api so you ultimately put it in our hands once you've committed the changes
[176.66 --> 181.70]  to your open api it's it's off to the races and you get a new release of your sdk you'll get a pull
[181.70 --> 187.42]  request to review you will you will have the opportunity to look at the contents of the code but quite often
[187.42 --> 193.04]  you can let it hum along creating sdks for you or new releases of your sdk every time you change your
[193.04 --> 198.18]  api very cool well the thing that got me with speakeasy that really helped me understand it was
[198.18 --> 204.82]  that as george said it is hands-off you can just focus on documenting your api via the open api spec
[204.82 --> 210.26]  and you still have pull requests you still have visibility and in fact they will even hop into pull
[210.26 --> 217.00]  requests with you to triage any sort of anomalies or issues that come from the sdk generation and
[217.00 --> 223.68]  improve the back end of speakeasy to make future releases better for you i think this is so cool
[223.68 --> 229.72]  for teams who want to just be hands-off of their sdks and focus on their product focus on the core
[229.72 --> 236.48]  documentation around the open api spec but still have all that awesome visibility okay so the next
[236.48 --> 244.72]  step is to go to speakeasyapi.dev you can start off with one free sdk that's so cool because you can go
[244.72 --> 252.22]  there right now and try it out completely free one free sdk let them know the changelog sent you
[252.22 --> 256.86]  let them know js party sent you once again speakeasyapi.dev
[256.86 --> 259.86]  you
[259.86 --> 261.86]  you
[261.86 --> 263.86]  you
[263.86 --> 265.86]  you
[265.86 --> 267.86]  you
[267.86 --> 269.86]  you
[269.86 --> 271.86]  you
[271.86 --> 280.56]  hello everyone and welcome to another episode of go time my name is natalie and i'm here with jesus
[280.56 --> 287.88]  jesus jesus jesus jesus jesus okay jesus espino joining us from mattermost and he's here to you
[287.88 --> 293.36]  are here to talk about the aha moments you got from reading the source code have you been doing go
[293.36 --> 300.84]  for long yeah i've been doing go for around seven years already so yeah quite long not not a lot how
[300.84 --> 307.18]  how did you start why well i started because i start getting interested in in the language itself
[307.18 --> 312.96]  yeah there's i had a friend that she was learning go and she was very excited about the language and
[312.96 --> 317.80]  she said with the cool things that you can find and go and i start getting interested i start
[317.80 --> 323.62]  practicing and actually i start contributing to open source projects one of them was mattermost
[323.62 --> 329.94]  and like six months later i start working for mattermost actually so it was a very very good
[329.94 --> 337.20]  timing nice what language were you switching from i i come from python i was using python for
[337.20 --> 344.70]  around 10 years before that so do you still use python or completely all go time to time i i use it is
[344.70 --> 351.58]  it's it's a nice language also it's i like go more but python is a great language and for very specific
[351.58 --> 358.54]  use case i still use python like writing ai models yeah playing with playing with ai is one of them
[358.54 --> 368.16]  probably some small scripting things or maybe even some small rest api very very small rest api with bottle
[368.16 --> 375.48]  or or flask or things like that so very small things nothing nothing big but yeah i still use it
[375.48 --> 382.02]  nice um let's start talking about the the 10 aha moments that you got from reading the go source code
[382.02 --> 391.28]  how did that even come to be yeah well this is um i i really like to to know deeply my my tools the
[391.28 --> 398.64]  things i use the things that i i work with every day and things like that in the past in in my python
[398.64 --> 406.72]  background i like to to give talks and things like that and get into the details and back then i
[406.72 --> 413.94]  investigated around how the python objects works under the hood and things like that how they
[413.94 --> 420.90]  the different python objects that were built in in the in the language were working on and all that
[420.90 --> 426.58]  kind of stuff i prepared a talk i did a talk actually in in some conference about that but then when i
[426.58 --> 433.88]  switched to go i start fresh i didn't know anything at that level i start to learn the language i start
[433.88 --> 442.44]  learning the language and start getting confidence with it and there was a point in 2020 21 or something
[442.44 --> 450.42]  like that that i felt confident enough to start investigating for preparing a talk and one of the things
[450.42 --> 458.92]  that i investigated was exactly the same how certain built-in objects works in in go and where that
[458.92 --> 467.48]  objects were the slices maps and channels because we're like the bread and butter of go so i started
[467.48 --> 472.96]  investigating probably half the pop quizzes i'm seeing are usually around slices arrays and such yeah
[472.96 --> 479.40]  yeah that's a that's a fun one yeah tricky and understanding how they work in the hood is is interesting
[479.40 --> 487.48]  and that's where that's where that was my first um my first attempt to start reading the ghost search
[487.48 --> 495.14]  code in here and there was relatively targeted so it was kind of simpler at that time i prepared a talk
[495.14 --> 501.90]  i give that talk in the in the foster them for first time so uh what's really great give me a lot of
[501.90 --> 511.32]  insights about about how how how channels actually work and how slices and maps work and even some small
[511.32 --> 519.44]  sneak peek on how goroutines works so it's what was a an interesting experiment and that is how i started
[519.44 --> 528.64]  then i just keep going i i use conferences and and public speaking as an excuse to learn things that i want
[528.64 --> 536.20]  to learn so i prepare a talk and then i i have to learn something to the degree that i can give a talk
[536.20 --> 543.48]  and i can answer the questions that sometimes it's really hard so yeah it's how how we get into that so
[543.48 --> 550.90]  the 10 a half moments comes from the exploration that keeps going preparing other talks that if you
[550.90 --> 558.64]  want we can't keep talking about it yes and also uh i already hear episode number two part number two
[558.64 --> 563.20]  of this one do you want to start with the first biggest aha moment how would you would you go we
[563.20 --> 568.22]  would go about that the biggest the most impressive ones or the most uh chronologically like the the
[568.22 --> 574.26]  order of that yeah i think i like the chronological approach because it's kind of easier for understanding
[574.26 --> 581.92]  my head and probably explain sometimes why it's an aha moment and the first one for me is is exactly
[581.92 --> 588.06]  about the slices maps and channels and specifically about the slices that was how slices are implemented
[588.06 --> 596.84]  in the dayhood because when i started writing you i was said that you have slices and the slices are
[596.84 --> 604.14]  immutable and then you just append things to that slices and then you get a appended version
[604.14 --> 611.96]  of the slice um the thing is that sounds really really inefficient it's looks like it has to be
[611.96 --> 617.70]  inefficient how in the hell are you doing that to make it that efficient then you realize what when you
[617.70 --> 623.64]  start investigating the code you start realizing how they are doing it and it's really smart you are
[623.64 --> 630.50]  slices are not slices just a sort of pointers and counters the real data is a sword under the hood
[630.50 --> 639.42]  in an array and that array is changing in size and it's automatically managed for you and the growing
[639.42 --> 646.44]  of the slice or the growing of the underneath array is not something like i going to add one add one add
[646.44 --> 654.44]  one it's normally doubling the size of the previous array to store more data and then you because of that
[654.44 --> 663.42]  you understand why you should be pre-allocating the array size all that kind of stuff was one of my
[663.42 --> 669.98]  first aha moment was like oh so that's the reason why it's efficient it's really a smart approach
[669.98 --> 676.24]  actually then you have some pitfalls that you you know because you know how it's implemented under
[676.24 --> 683.08]  the hood but there are some pitfalls around that approach that is using multiple slices that points
[683.08 --> 689.42]  to the same array and some of them and one of them get resized were connected before because we're
[689.42 --> 696.14]  accessing the same underneath array but suddenly they are not connected anymore so it's kind of a weird
[696.14 --> 703.14]  behavior that is it's unexpected i guess if you don't understand the implementation details but yeah
[703.14 --> 710.52]  that was my first one the the my first aha moment was like oh then that is how they make this efficient
[710.52 --> 717.30]  and make this work smoothly so were you comparing it to what you know from other languages or was it
[717.30 --> 723.18]  more like this is the first time on that okay for arrays i'm focusing on how's it done under the hood
[723.18 --> 734.66]  yeah i think i think from python was a very similar it's not the same because in python i'm not 100% sure
[734.66 --> 741.28]  in python they are not appending things you are saying hey i have a a list of elements and i'm adding
[741.28 --> 747.14]  things to that list so you semantically you are understanding that you are adding things to the
[747.14 --> 753.80]  list under the hoodie if i recall correctly it's pretty similar the behavior is just an array of memory
[753.80 --> 759.68]  that keeps doubling and the and you have this pointer and these counters that give you the lens and the
[759.68 --> 766.32]  capacity all that is almost exactly the same if i recall correctly i i don't have the python
[766.32 --> 772.80]  implementation very fresh yeah of course it's been a yeah we're not talking about the the focus of a
[772.80 --> 779.92]  of go of python source code i'm i'm just curious if you generally in uh were focusing on on the same
[779.92 --> 787.38]  topic for other languages or was go kind of where you started really diving into this no i i i start in
[787.38 --> 794.58]  python before and then i started with go because i was using go every day so they the the whole point
[794.58 --> 801.14]  was it's a tool that i use every day i want to understand it better that's the reason why i did
[801.14 --> 808.02]  that in python before i want to do that with all the tools that i i use i did that with git in the past i
[808.02 --> 815.12]  want to do that with postgres in the future but yeah it's something that i want to do i don't know if
[815.12 --> 820.96]  it's going i going to do it's a matter of time and sometimes it's hard to find the time for that
[820.96 --> 827.60]  but yeah yeah it's like a advent of uh diving into code can be a fun project instead of solving
[827.60 --> 833.52]  challenges like in advance of code actually reading somebody else's code and learning those things
[834.32 --> 842.00]  yeah new year's list yeah yeah it's it's challenging i have to say that go helps a lot there go is a great
[842.00 --> 850.00]  language to to read because it's feels like home everywhere of course the algorithms and the
[850.00 --> 857.44]  the complexity of the different projects it's it's different and reading a compiler a source code it's
[858.32 --> 864.64]  it's a tough thing because it's a compiler the complexity of a compiler is already big enough to to be
[864.64 --> 873.92]  challenging but at the same time you see the same kind of styling everywhere the code is it's it's kind
[873.92 --> 882.56]  of familiar okay this is an error if error whatever then nil whatever all that things are kind of the
[882.56 --> 890.64]  same so you feel it feels less weird than other languages where every project has its own styling
[890.64 --> 898.40]  yeah yeah very much goes to our human need for pattern recognition for sure yeah exactly i agree okay
[898.40 --> 905.52]  so you say that the arrays implementation was was making sense and was a little bit familiar also
[905.52 --> 912.24]  speaking to your pattern recognition as well yeah so no i was interested in that at the end of the day
[912.24 --> 919.12]  most of the implementations for example slices and maps is not like super weird implementation you can
[919.12 --> 925.36]  find very similar implementations other languages it's it's just a relatively standard implementation of
[925.36 --> 931.28]  certain things there's details on on for example maps that can be different than other languages
[931.28 --> 939.92]  for example in in go maps keys are unsorted and are unsorted on purpose actually they are unsorted
[939.92 --> 947.76]  on purpose up to the level that every single map have a random seed for the for the keys so it's two
[947.76 --> 953.92]  different maps with the same keys and the same values are going to be ordered differently so it's it's
[953.92 --> 959.04]  kind of it's on purpose it's by design but at the end of the day most of the languages have its own
[959.04 --> 965.28]  implementation of these kind of things and they are all most of them are kind of similar around hash
[965.28 --> 974.56]  maps and slices and all that stuff okay how about uh the second aha moment okay next next step one of the
[974.56 --> 982.48]  things that i was intrigued about go because it's one of the key things is um go routines is something
[982.48 --> 989.28]  that everybody wants in go everybody loves in go and i did want to understand better what a go routine
[989.28 --> 996.72]  is and how it works and i started digging into the into the source code and i started investigating how
[996.72 --> 1002.16]  the go routines works under the hood from the perspective of the go routine how of the life cycle of the
[1002.16 --> 1009.68]  go routine and actually for that i prepared another talk that is called the sacred life of a go routine
[1010.32 --> 1019.52]  and that in that talk what i i try to do is follow the process of when a go routine is created how it's
[1019.52 --> 1026.32]  created and what are the steps that the go routine goes through and how it changed from one from one
[1026.32 --> 1032.56]  state to another and what are the reasoning around that changes and one of the things that i discovered
[1032.56 --> 1038.96]  while i was doing that was it's something that i already have the kind of the intuition around that
[1038.96 --> 1047.60]  or the understanding about that that is go routines are cooperative but whenever i start seeing the code
[1047.60 --> 1053.92]  was more obvious and evident that it's a cooperative approach in threats in operating system threats you
[1053.92 --> 1060.00]  have the operating system deciding when to cut something and and assign another threat to the to the processor
[1060.72 --> 1069.36]  in go the go routine itself is the responsible of saying hey i have to stop just i going to call the scheduler to i
[1069.36 --> 1075.92]  going to stop myself call the scheduler to select another task or another go routine and the go routine is going to start running
[1075.92 --> 1105.76]  not only that the go routine i stop myself because i waiting for something and the one that is going to wake me up is another go routine for example whenever to just send something to a channel and it's some another go routine waiting it's a you are going to wake the go routine that is sending to that channel is going to wake up the other go routine so they are collaborating together to do all the processing there's some special go routines like the system monitor go routine that is a
[1105.92 --> 1135.90]  is doing certain thing or the net pool that also it's kind of monitoring certain things for for getting back that go routines whenever they finished but in general the go routines are waking up each other or are sleeping by themselves and calling the scheduler to select another go routine so that cooperative nature of the go routines is something that i found very interesting and was an aha moment for me also yeah so you said the previous one the arrays one made a lot of
[1135.90 --> 1164.66]  sense does this one makes a lot of sense would you have done it somehow differently i think it's kind of a natural way of doing that whenever you are doing coroutines that is it's not exactly the same a coroutine that what ghosts have but it's this kind of cooperative approach where you have you have one single thread and you have to decide when to change to one or another and it's it's just easier if you let the the go routines collaborate
[1164.66 --> 1192.66]  than if you have to put another process on top of that orchestrating all of that go routines because actually the scheduler the go scheduler is not another process it's not another go routine it's nothing like that the go scheduler is a chunk of code that the go routine that is going to sleep or the go routine that finished his work and it's going to go to that it's going to call the scheduler code and the scheduler code it's going to transfer
[1192.66 --> 1206.30]  transfer somehow transfer the execution to the to the scheduler the scheduler executes and select another go routine and transfer to that go routine the execution so it's just a chunk of code that transition from one
[1206.30 --> 1211.84]  go routine to another it's it's it's pretty cool actually it's it's super interesting code
[1211.84 --> 1239.84]  i don't know if i answer your question actually yeah yeah yeah yeah another philosophical question a little bit um as a background for the question have you watched rick and morty do you know the concept of the mr me six oh no i don't sorry so there there is a concept of a little blue creatures that is called mr me six and it's very i found it super helpful to understand this concept and also of like spinning up a task that has to do exactly one thing and then it dies
[1239.84 --> 1257.40]  i think it's i think it's probably there's some developers and the creators of the show because i found lots of similarity and then when ai came and the concept of agents autonomous agents in the world of ai not the world of software it's also a little bit similar in the sense that ai agent gets a task and then it spins off
[1257.40 --> 1268.76]  subtasks and then it finishes the task and kind of buckles up to report so i kind of see similarity between the three of them and i hope that in those two and a half sentences i explained
[1268.76 --> 1275.48]  enough of this logic to you but uh this will be my guiding question kind of throughout our conversation
[1275.48 --> 1283.02]  on the aha moment because i like finding lots of equivalents between our current day software and what i
[1283.02 --> 1290.48]  try to imagine ai based software will be so this is kind of i don't know you're not familiar with rick and
[1290.48 --> 1293.34]  morty i get that that's uh probably better
[1293.34 --> 1301.04]  have you played at all with ai agents what do you have enough experience to say an opinion about this or
[1301.04 --> 1307.84]  not yet not yet actually i i haven't played i don't know what you mean with an ai agent so
[1307.84 --> 1315.16]  that autonomous agent is a better name yeah i guess it's something like you ask to realize a task and
[1315.16 --> 1323.20]  it's going to use external resources or external actions to fulfill the task something like that i guess
[1323.20 --> 1329.20]  it uh basically the ai goes and and decides what is the sub tab like you give it a goal it breaks it
[1329.20 --> 1336.14]  down to sub tasks and then it spins off mini ais to execute those tasks let's say which is very very
[1336.14 --> 1348.02]  similar to that concept yeah yeah could be yeah no i i don't i it's hard for me because i i like ai i have
[1348.02 --> 1355.64]  i have used it but i'm not very into very deep into that but yeah i i think there are similarities at
[1355.64 --> 1362.42]  the end of the day what goroutines are is is just processes that are are kind of independent as up to
[1362.42 --> 1368.72]  certain degree they have a task they have to realize that task and they they are kind of independent from
[1368.72 --> 1374.38]  the rest of the of the goroutines there is a actually what is something like for some people's
[1374.38 --> 1380.04]  weird is goroutines doesn't have a parent if i recall correctly so goroutines are goroutines there's
[1380.04 --> 1384.56]  no relationship with three goroutines you can execute thousands of goroutines and they are not
[1384.56 --> 1389.52]  related to each other not even with the parent or the execute or the the one that's pawned so
[1389.52 --> 1397.04]  i don't know i think i'm a bit lost with your questions to me yeah yeah yeah well just to it's even
[1397.04 --> 1403.40]  more like a opinion than a question but just to confuse a bit more and then we move on to number three
[1403.40 --> 1409.82]  another similarity that i see there is also to the concept of threads in um in processors
[1409.82 --> 1417.20]  i know how much you got a chance to dive into like a like operating system breaking down things into
[1417.20 --> 1421.56]  telling the different processors how they run around their tasks and so on but there's also like
[1421.56 --> 1428.06]  now you have a threat and so on so it's also i see some similarity in those concepts and i i personally
[1428.06 --> 1433.62]  find it really cool that it kind of goes between the different different fields that have something
[1433.62 --> 1437.92]  to do with each other but not fully yeah just an observation it's not a question if you have
[1437.92 --> 1443.52]  experience there i'm happy to hear your thoughts if not tell us about numbers in in in threads and
[1443.52 --> 1447.94]  the difference between threads and goroutines or something like that or yeah if you want to chat
[1447.94 --> 1453.24]  about that yeah well now it's interesting how it's solved in in the in the go runtime it's it's
[1453.24 --> 1459.72]  basically they abstract you from the operating system trends and call them cpus actually processors
[1459.72 --> 1465.44]  actually and then that processors gets assigned to different goroutines but the goroutines and the
[1465.44 --> 1471.88]  processors are not highly coupled so they can they normally have certain the certain
[1471.88 --> 1479.16]  tendency to execute in the same processor on the same operating system thread but it's not necessarily
[1479.16 --> 1485.60]  it's not mandatory at all for the goroutines so the goroutines can execute in different operating
[1485.60 --> 1491.90]  system threads so it's a very smart approach that decouple the the cpu and them and the goroutines or the
[1491.90 --> 1499.88]  operating system thread and the goroutines and allows you to execute at full capacity of your processors
[1499.88 --> 1508.16]  using that architecture because yeah because if a cpu is overloaded you can take the goroutines from
[1508.16 --> 1514.60]  other cpu and start executing in the one that is more free things like that so it's it's a it's very
[1514.60 --> 1522.76]  cool how go abstract you from cpus operating system threads and and the goroutines so it's it's pretty
[1522.76 --> 1529.86]  cool yep yep and efficient so what is your number three aha moment okay number three oh well
[1529.86 --> 1537.02]  this this this was a kind of silly one i was investigating around the i was investigating
[1537.02 --> 1543.64]  the compiler and one of the things that i i started investigating was the the process for
[1543.64 --> 1551.88]  tokenizing and parsing and whenever i start reading the parser i just realized that it was obvious in any
[1551.88 --> 1562.04]  way but i realized that whatever is in the parser in the ast3 is what you can have in a go file there's
[1562.04 --> 1570.46]  nothing else so if you start seeing how the ast3 the abstract syntax tree for go is generated you are going
[1570.46 --> 1579.98]  going to see that is one abstract syntax tree per file and it's going to have an import a set of declarations
[1579.98 --> 1589.02]  and a set of imports and a declaration can be a constant a variable a function and a type and that's it
[1589.02 --> 1596.46]  there's nothing else that can be in a file so what's kind of a sensation of complete understanding of
[1596.46 --> 1603.48]  something i say okay now i know where is the boundaries so everything it's inside these
[1603.48 --> 1609.06]  boundaries there's nothing else that can go in a file so there's nothing that i am i'm missing
[1609.06 --> 1616.80]  constants variables functions and types and the import and the package name that's everything
[1616.80 --> 1623.98]  and what probably is kind of silly but for me was was like an aha moment so it was like oh that's it
[1623.98 --> 1629.56]  of course then you have the body of the functions and all that stuff and there's a lot of stuff that
[1629.56 --> 1637.22]  goes there but but yeah inside a file you only have that the things this makes me think of how in c
[1637.22 --> 1641.78]  there is the i think it's in c that you have the header file and you have the code file
[1641.78 --> 1648.22]  right it's kind of similar let's scope our little universe but this is scoping it for
[1648.22 --> 1652.96]  that file but it's it's kind of like knowing that this is everything that's included there
[1652.96 --> 1660.42]  yeah it's kind of like that exactly is you have a clear definition of what can go there it's not
[1660.42 --> 1666.78]  exactly the same because in the h file you are saying hey these are the functions that i declare it's
[1666.78 --> 1674.12]  kind of publishing this is a public interface but at the same time is is like okay yeah if i understand
[1674.12 --> 1681.34]  the h file in theory i should be able to use it and i should be able to understand all the all the
[1681.34 --> 1687.96]  boundaries so yeah and you say that what you liked more more than that this is like defining scoping
[1687.96 --> 1693.48]  it for this file it's kind of scoping it for go in general that this is your entire toolbox and there
[1693.48 --> 1701.26]  be no surprises it's like not keywords but tool toolbox really yeah there's there's nothing else
[1701.26 --> 1712.48]  if if you think oh could i execute a chunk of code inside the main file but outside the function no you
[1712.48 --> 1719.68]  can't that's it that's it's a variable declaration then you can it's a constant then you can but it's
[1719.68 --> 1727.78]  not that it's not a type definition or a function you can't there's no representation for that you
[1727.78 --> 1734.94]  can't represent that in the ast now there are the pragmas and this kind of but they are comments
[1734.94 --> 1743.28]  that are handled in a smart way but at the end of the day the ast is just that there's nothing else
[1743.28 --> 1749.04]  that you can represent with that sounds like it it has not been a talk yet this aha moment not
[1749.04 --> 1755.46]  really it's there's a talk the aha moment comes from a from another talk that i was preparing actually
[1755.46 --> 1763.24]  that was the at the time i was preparing the understanding the go compiler actually was called
[1763.24 --> 1768.50]  hello world from the code to the screen i prepared that talk i did that talk in the go for con us
[1768.50 --> 1777.60]  but then i made uh update of an updated version to the last version of the go compiler for a go for
[1777.60 --> 1783.24]  con uk and i renamed that to understanding the go compiler because was more clear the title and i don't
[1783.24 --> 1789.16]  want to mislead people around what i'm going to talk but yeah it was on that understanding the
[1789.16 --> 1794.20]  compiler and i go through the all the whole compiler and there there's a lot of aha moments that
[1794.20 --> 1802.02]  comes from that talk because i went through the whole process of compiling and the idea was i have
[1802.02 --> 1810.28]  a hello world and that hello world is going to be the main character of my of my talk is going to go
[1810.28 --> 1817.72]  through the whole process of transformation until getting to a binary and i want in the talk i i guide
[1817.72 --> 1824.40]  you through through the whole process and that's a that's the idea and this aha moment comes from that
[1824.40 --> 1831.68]  and there's some of them some that come from that too so if you want we can jump to the next one actually
[1831.68 --> 1838.48]  yeah yeah let's do that so aha moment number four yeah i think so when i was investigating that
[1838.48 --> 1845.50]  one of the things that i investigate during the process were two characteristics that were escape analysis
[1845.50 --> 1851.92]  and inlining and the escape analysis for that people that doesn't know that escape analysis is a
[1851.92 --> 1860.84]  process inside the compiler that is going to decide if a variable it needs to be a store in the heap or
[1860.84 --> 1867.80]  can be a store in the stack so that's that decision is made through escape analysis that basically decides
[1867.80 --> 1875.22]  hey if it's possible for me to use the the function stack to restore this data or because
[1875.22 --> 1884.10]  the scope of this variable escapes from the function i need to store some somewhere else that means
[1884.10 --> 1891.46]  basically the main memory the the heap so that um that is what escape analysis does on the other hand
[1891.46 --> 1899.18]  you have inlining inlining it's a process that analyzes a function in in the co-compiler it's a process that
[1899.18 --> 1907.60]  analyze the function and decide if the function is simple enough to be embedded to be inlined in the
[1907.60 --> 1914.64]  other side in the call side instead of calling the function you are going to take the whole code of the
[1914.64 --> 1921.40]  function and replace the function code with the code itself that is inlining and it depends on the
[1921.40 --> 1927.54]  complexity of the function that it not necessarily means the size of the function it means the size of the
[1927.54 --> 1934.16]  function but actually means the operations that you use inside the function so the cool thing that i
[1934.16 --> 1941.42]  learned was if you have escape analysis that the size of function it needs to go into the stack or the heap
[1941.42 --> 1947.96]  and you have inlining that allows you to take a function and put the function in place of the caller
[1947.96 --> 1955.20]  what is going to happen is they are going to collaborate together so if your function is simple enough
[1955.20 --> 1962.88]  it's going to be inline and suddenly the scope of your variables is bigger so it's more probable
[1962.88 --> 1969.44]  that you can use the stack instead of the heap so that was very cool that was very interesting it's
[1969.44 --> 1976.28]  yeah it's it's something that i found super interesting yeah and then what did you have any
[1976.28 --> 1982.64]  any chance of implementing this function like writing code that is kind of corresponding to this
[1982.64 --> 1988.20]  functionality that was extra efficient or interesting or not or is there a use case you can imagine for
[1988.20 --> 1994.08]  this this to be interesting or because as you were describing this i i i had nothing come to mind
[1994.08 --> 2001.02]  there are use cases i think i think you you have it's it's a tool that you have there and sometimes
[2001.02 --> 2007.92]  you have you can say okay i have a very tight function here that is generating a lot of allocations
[2007.92 --> 2017.44]  then i can try to tweak that to reach the point where this gets in line so that's one option but also
[2017.44 --> 2025.82]  i think the cool part is knowing that you can make decisions that are just smarter around creating your
[2025.82 --> 2033.10]  your structs for example if you have a new function for creating a new struct and you have initialization
[2033.10 --> 2040.32]  process in that inside that that function that new function that new function almost for sure is not going
[2040.32 --> 2048.02]  to be in line because the initialization process it's going to get complex enough to not get embedded to not
[2048.02 --> 2055.70]  get in line so the scope of that variables is always going to be whenever you execute new is going to
[2055.70 --> 2062.72]  return a pointer to that variable and because of that is going to always go into the heap but if the function is
[2062.72 --> 2069.40]  small enough if you say hey the new function is going to create the the object and return the the pointer
[2069.40 --> 2076.68]  suddenly the new function is always embedded it's always in line and it's always a store in the stack
[2076.68 --> 2083.90]  in the stack of the parent unless there's other reason for escaping but you are storing that in the stack of
[2083.90 --> 2091.52]  the parent and then if you call for example initialization function that initialization function is already
[2091.52 --> 2099.68]  working in the in the stack so keeping your constructors small enough to get them embedded
[2099.68 --> 2107.80]  then in line it it's going to be a good practice in general so for example that is that is a good
[2107.80 --> 2116.94]  thing because it's not going to give you a huge boost in performance but it can get you tiny improvement
[2116.94 --> 2125.72]  in performance here and there and suddenly you are gaining well that adds up at the end so yeah it's
[2125.72 --> 2130.68]  yeah that that makes a lot of sense that that would be actually super interesting to also run tracing on
[2130.68 --> 2136.26]  that for example and to compare yeah if depending on the size of your application you can have
[2136.26 --> 2141.70]  thousands a thousand a thousand of creation of certain objects and if they go to the heap instead of the
[2141.70 --> 2147.74]  stack it's going to be a lot of allocation a lot of garbage collector pressure a lot of other stuff that maybe
[2147.74 --> 2150.48]  is not that important so
[2150.48 --> 2156.18]  or actually we'll find a like big big differences i would be i would be very curious we do have a
[2156.18 --> 2164.22]  tracing episode in planning part two of that so that will be i will remember to do a cross and to bring this up there as well
[2164.22 --> 2171.94]  yeah it's a cool observation yeah actually i think the inliner now it's been rewriting i don't know if it's already
[2171.94 --> 2178.02]  finished the work i think in 23 it will be released in the updated yeah with the profiler right with a
[2178.02 --> 2184.98]  with a profile guide optimization so yeah that's that that can be very very cool to see if that is going to
[2184.98 --> 2191.06]  have a huge impact because probably it's going to have certain impact there yeah anything else to say about point
[2191.06 --> 2198.30]  number four i don't think so okay we have to we we have a lot of field to cover still so all right
[2198.30 --> 2206.70]  jumping back and we are continuing now with aha moment number five and six yes the other thing that i
[2206.70 --> 2213.60]  was doing well i i keep investigating the go compiler and go through different steps in the process and i
[2213.60 --> 2220.52]  reached a point that was super interesting for me that was another aha moment that was when the go compiler
[2220.52 --> 2230.38]  gets machine specific so all the process related to tokenizing parsing um there's an intermediate
[2230.38 --> 2237.04]  representation uh in in the middle then it's converted to something that is called ssa that is single
[2237.04 --> 2244.80]  a single static assignment and then it's applied a lot of optimizations and there's a point in the process of
[2244.80 --> 2252.94]  converting ssa or processing ssa where it's applying optimizations and accepting point there's one of the
[2252.94 --> 2262.26]  passes of the optimizations that is called lower that is the exact point where the compiler start doing
[2262.26 --> 2270.16]  things that are machine specific everything before that point it's machine agnostic is if you have an
[2270.16 --> 2280.88]  irm or if you have a md amd 64 doesn't matter it's all the same code base and then gets into this lower
[2280.88 --> 2290.44]  phase of the ssa transformation or ssa passes and gets converted into a machine specific ssa and then
[2290.44 --> 2297.56]  apply other optimizations and finally with that optimization supply start generating the binary the
[2297.56 --> 2303.42]  linking and generate the final binary that is an executable but it's it's pretty cool that very far
[2303.42 --> 2311.04]  in the process it's when you get the machine specific part that by itself was an aha moment and was very
[2311.04 --> 2316.94]  interesting for me but i'm also a big fan of tinygo i love microcontrollers i love playing around i'm not
[2316.94 --> 2323.34]  good at it but i love playing around with them and for me it was kind of interesting how tinygo was
[2323.34 --> 2330.46]  doing that and it's very interesting that tinygo it's follow a very smart approach it's basically
[2330.46 --> 2338.84]  taking everything up to that point everything up to ssa it's up to that point is is the same compiler
[2338.84 --> 2346.98]  it's the same code base mainly and in that point it takes that ssa and instead of converting that ssa
[2346.98 --> 2355.76]  into machine code it's going to convert that into a llbm intermediate representation or llbm
[2355.76 --> 2363.46]  kind of self-assembly and then llbm is the one responsible for compiling that to the microcontroller
[2363.46 --> 2370.78]  specific architecture so apart from that you have to have a runtime that is compatible with microcontrollers
[2370.78 --> 2376.06]  because in microcontrollers you don't have the same kind of access to to things you don't have an
[2376.06 --> 2381.66]  operating system and things like that but at the end of the day the compilation part is exactly the
[2381.66 --> 2387.96]  same so that is the reason why tinygo it is exactly the same language you can have differences in the
[2387.96 --> 2393.86]  runtime but you don't have differences in the language because it's the same one and it's leveraging that
[2393.86 --> 2400.66]  point so for me that was like oh wow these people is really smart so i really love that aha moment
[2400.66 --> 2403.72]  and actually i'm a big fan of tinygo
[2403.72 --> 2413.78]  shouting out to the cool things that tinygo does and uh together with the ron and ron evans and uh
[2413.78 --> 2419.88]  daniel estaban and the team who is working on the cool projects around that oh yeah yeah that is uh
[2419.88 --> 2426.52]  that is interesting i how how would you say that this so if this maps easily to across the different
[2426.52 --> 2435.50]  processors and it maps also to little tiny embedded tech would that be how would that be working on gpus for example
[2435.50 --> 2442.04]  yeah that's that's interesting i think the gpus have a different set of instructions
[2442.04 --> 2449.50]  so i don't think it's it fits really well with that the things i'm not an expert to be honest
[2449.50 --> 2456.72]  but my sensation here is what you have is a cell assembly that is oriented to a general purpose cpus
[2456.72 --> 2465.36]  and that general purpose cpus gets a general purpose cpu cell assembly gets converted into real
[2465.36 --> 2474.30]  general purpose cpu like irm or amd64 or things like that so applying that to cpu you can you can apply
[2474.30 --> 2482.40]  the same set of ideas probably you can write you can do what what rod pike did here that is or what the
[2482.40 --> 2492.74]  go team did here that is taking the generating a cell assembly that is going to be for gpu code and
[2492.74 --> 2500.90]  build that up to the level that you have this intermediate language and whenever you reach that
[2500.90 --> 2508.10]  point you convert that into the specifics of different gpus assembly code or or instructions
[2508.10 --> 2516.54]  but but i don't think it's applicable to execute the go binary for example or go binary directly into a gpu
[2516.54 --> 2523.06]  because i think half different different set of instructions is not the same kind of machine that
[2523.06 --> 2530.12]  you are managing there yeah that's fair again i'm not an expert maybe i'm yeah i'm wrong here so it's it's a
[2530.12 --> 2536.30]  guess it's a guess it's a surprise question yeah yeah yeah but that definitely is interesting and i
[2536.30 --> 2542.88]  will go and uh look about that a little bit i'm also now curious you said embedded tiny go and
[2542.88 --> 2547.30]  although this connection has been around in forever i'm kind of only now starting to think will it be
[2547.30 --> 2552.20]  how different will it be for fbgas for example and like all the all the other hardware out there in
[2552.20 --> 2558.34]  the world um when maybe one day we'll do an episode about go and different um different processing units
[2558.34 --> 2568.46]  yeah uh well we only covered five six six of the ten but we're slowly approaching uh our time which
[2568.46 --> 2573.20]  means we will have to do a part two because you're you're just bringing up two interesting points and i
[2573.20 --> 2577.80]  have too many questions slash comments about them my last question to you would be do you have an
[2577.80 --> 2604.72]  unpopular opinion okay i think i think i'm going to get some hate for this uh so well that's what
[2604.72 --> 2615.78]  unpopular opinion is about yeah i think mechanical keyboards are just glorified nostalgia so it's a
[2615.78 --> 2624.82]  loudly glorified yeah very loud glorified nostalgia so that's that's the thing i i have used them
[2624.82 --> 2631.14]  i don't think are more comfortable i don't think are more are better for sure i'm not going to make
[2631.14 --> 2637.00]  you a better programmer or improve your performance or something like that that there's no way i
[2637.00 --> 2642.00]  understand for some cases pretty cool whenever you are building your own keyboard or this kind of
[2642.00 --> 2648.12]  split keyboards or programmable keyboards that you have your microcontroller and things like that for
[2648.12 --> 2654.34]  that kind of cases i found that cool because you can have your switches and all that stuff and there's
[2654.34 --> 2661.28]  a lot of pieces out there for doing that kind of things but i don't know paying 10x it's it's all the
[2661.28 --> 2667.92]  10x that you are going to get for a keyboard is 10x in the price and the sound the noise oh yeah exactly
[2667.92 --> 2675.42]  and the decibels yeah getting getting that 10x in the price for something that is i don't know
[2675.42 --> 2682.12]  probably it's an unpopular opinion i get i get that people the people that is going to consider this
[2682.12 --> 2688.76]  unpopular is going to consider this very unpopular so let's see well i cannot say i don't agree with
[2688.76 --> 2695.00]  you at least with me you're you are popular my opinion is on the unpopular opinion is on a similar
[2695.00 --> 2703.90]  topic and trackpads are better than mice i use a mouse but yeah i i think so
[2703.90 --> 2712.10]  well i guess we both agree then with this consensus i will say thank you so much for
[2712.10 --> 2717.60]  joining and sharing your interesting insights and i am looking forward to episode two and thanks
[2717.60 --> 2720.08]  everybody who joined yeah thank you for having me
[2720.08 --> 2729.84]  that is go time for this week thanks for listening along subscribe now if you haven't already head to
[2729.84 --> 2737.50]  gotime.fm for all the ways or simply search for gotime wherever you get your podcasts you'll find us
[2737.50 --> 2744.24]  hey do you receive our changelog newsletter each monday if not let's fix that bug one reader calls
[2744.24 --> 2751.64]  it so good he considers it a competitive advantage sign up for zero dollars at changelog.com
[2751.64 --> 2758.68]  slash news thanks once again to our partners at fly.io to our mysterious beat freak breakmaster
[2758.68 --> 2764.60]  cylinder and to our friends at sentry we love sentry you might too use code changelog when you're
[2764.60 --> 2771.34]  signing up for a team plan and save 100 bucks why not right that is all for now but we'll talk to you
[2771.34 --> 2773.68]  again next time on go time
[2773.68 --> 2776.32]  you
[2776.32 --> 2778.34]  you
[2778.34 --> 2780.34]  you
[2780.34 --> 2790.34]  you
[2790.34 --> 2792.34]  you
[2792.34 --> 2794.34]  you
[2794.34 --> 2796.34]  you
[2796.34 --> 2798.34]  you
