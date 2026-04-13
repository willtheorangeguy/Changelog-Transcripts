[0.00 → 16.48] let's do if it's go time welcome to go time your source for wide-ranging discussions from all
[16.48 → 24.18] around the go community find us on the web at gotime.fm on the Fediverse at go time at changelog. Social
[24.18 → 31.12] and on x at gotime.fm thanks to our partners at fly.io the home of changelog.com launch your app
[31.12 → 37.46] as close to your users as possible find out how at fly.io okay here we go
[37.46 → 47.82] what's up friends I'm here with two new friends of mine from speakeasy sugar batch co-founder and CEO
[47.82 → 54.00] and George Hadar founding engineer so for the uninitiated speakeasy takes care of the entire
[54.00 → 60.42] SDK workflow to save you and your team significant time delivering enterprise-grade SDKs to your
[60.42 → 70.10] customers in minutes you can generate best in class SDKs in typescript python go java c sharp and even
[70.10 → 78.08] PHP so sugar what's your excitement level for APIs and this API world we're living in I'm super excited
[78.08 → 85.56] about APIs I think we went to gen zero of the API first revolution and I think we're actually going
[85.56 → 91.06] to a second one now with the tailwinds of the AI ecosystem kind of causing that to be invigorated
[91.06 → 95.68] so yeah super, super psyched to be working in this space right now I think it's everyone's at a point
[95.68 → 101.76] now where everyone knows about rest APIs and GraphQL APIs and GPC APIs and now I think we're actually
[101.76 → 107.50] getting into the second phase of that which is how do people ship great developer experience in
[107.50 → 113.22] addition to the APIs and how do we build like truly best in class APIs that turn into they know long
[113.22 → 118.62] with infrastructure right this is kind of the vision I think that stripe helped manifest for
[118.62 → 123.88] everyone in the fintech space which is the API that really sets the bar for developer experience
[123.88 → 129.50] but also like it's something you can truly rely on right it's its a true if you make stripe a
[129.50 → 134.30] dependency of your company you can feel confident doing that and I think that's that's the part of
[134.30 → 139.82] API developer that really excites me I agree that is exciting so George teams who leverage speakeasy
[139.82 → 146.70] are those who have leaned all the way in on documenting a solid open API spec and mostly
[146.70 → 152.82] want to be hands-off of their SDKs is that right precisely so you're coming to us because you want
[152.82 → 158.88] to be hands-off from that process you want to put all of your effort into documenting your API and then
[158.88 → 164.98] you're trusting and relying on great quality tooling to turn that into code and documentation which is
[164.98 → 170.70] what we're doing for you, you're not meant to change or edit the code because it will be regenerated the
[170.70 → 176.66] next time you change your open API so you ultimately put it in our hands once you've committed the changes
[176.66 → 181.70] to your open API it's its off to the races, and you get a new release of your SDK you'll get a pull
[181.70 → 187.42] request to review you will have the opportunity to look at the contents of the code but quite often
[187.42 → 193.04] you can let it hum along creating SDKs for you or new releases of your SDK every time you change your
[193.04 → 198.18] API very cool well the thing that got me with speakeasy that really helped me understand it was
[198.18 → 204.82] that as George said it is hands-off you can just focus on documenting your API via the open API spec
[204.82 → 210.26] and you still have pull requests you still have visibility and in fact they will even hop into pull
[210.26 → 217.00] requests with you to triage any sort of anomalies or issues that come from the SDK generation and
[217.00 → 223.68] improve the back end of speakeasy to make future releases better for you, I think this is so cool
[223.68 → 229.72] for teams who want to just be hands-off of their SDKs and focus on their product focus on the core
[229.72 → 236.48] documentation around the open API spec but still have all that awesome visibility okay so the next
[236.48 → 244.72] step is to go to speakeasyapi.dev you can start off with one free SDK that's so cool because you can go
[244.72 → 252.22] there right now and try it out completely free one free SDK let them know the changelog sent you
[252.22 → 256.86] let them know JS party sent you once again speakeasyapi.dev
[256.86 → 259.86] you
[259.86 → 261.86] you
[261.86 → 263.86] you
[263.86 → 265.86] you
[265.86 → 267.86] you
[267.86 → 269.86] you
[269.86 → 271.86] you
[271.86 → 280.56] hello everyone and welcome to another episode of go time my name is Natalie and I'm here with Jesus
[280.56 → 287.88] Jesus Jesus Jesus Jesus Jesus okay Jesus spin joining us from Mattermost, and he's here to you
[287.88 → 293.36] are here to talk about the aha moments you got from reading the source code have you been doing go
[293.36 → 300.84] for long yeah I've been doing go for around seven years already so yeah quite long not a lot how
[300.84 → 307.18] how did you start why well I started because I start getting interested in the language itself
[307.18 → 312.96] yeah there's I had a friend that she was learning go, and she was very excited about the language and
[312.96 → 317.80] she said with the cool things that you can find and go and I start getting interested I start
[317.80 → 323.62] practicing and actually I start contributing to open source projects one of them was Mattermost
[323.62 → 329.94] and like six months later I start working for Mattermost actually so it was a very, very good
[329.94 → 337.20] timing nice what language were you switching from i I come from python I was using python for
[337.20 → 344.70] around 10 years before that so do you still use python or completely all go time to time i I use it is
[344.70 → 351.58] it's its a nice language also it's I like go more, but python is a great language and for very specific
[351.58 → 358.54] use case I still use python like writing AI models yeah playing with AI is one of them
[358.54 → 368.16] probably some small scripting things or maybe even some small rest API very, very small rest API with bottle
[368.16 → 375.48] or flask or things like that so very small things nothing, nothing big but yeah I still use it
[375.48 → 382.02] nice um let's start talking about the 10 aha moments that you got from reading the go source code
[382.02 → 391.28] how did that even come to be yeah well this is um i I really like to know deeply my tools the
[391.28 → 398.64] things I use the things that i I work with every day and things like that in the past in my python
[398.64 → 406.72] background I like to give talks and things like that and get into the details and back then i
[406.72 → 413.94] investigated around how the python objects works under the hood and things like that how they
[413.94 → 420.90] the different python objects that were built in in the language were working on and all that
[420.90 → 426.58] kind of stuff I prepared a talk I did a talk actually in some conference about that but then when i
[426.58 → 433.88] switched to go I start fresh I didn't know anything at that level I start to learn the language I start
[433.88 → 442.44] learning the language and start getting confidence with it and there was a point in 2020 21 or something
[442.44 → 450.42] like that I felt confident enough to start investigating for preparing a talk and one of the things
[450.42 → 458.92] that I investigated was exactly the same how certain built-in objects works in go and where that
[458.92 → 467.48] objects were the slices maps and channels because we're like the bread and butter of go so I started
[467.48 → 472.96] investigating probably half the pop quizzes I'm seeing are usually around slices arrays and such yeah
[472.96 → 479.40] yeah that's a that's a fun one yeah tricky and understanding how they work in the hood is interesting
[479.40 → 487.48] and that's where that's where that was my first um my first attempt to start reading the ghost search
[487.48 → 495.14] code in here and there was relatively targeted so it was kind of simpler at that time I prepared a talk
[495.14 → 501.90] I give that talk in the foster them for first time so uh what's really great give me a lot of
[501.90 → 511.32] insights about how how how channels actually work and how slices and maps work and even some small
[511.32 → 519.44] sneak peek on how go routines works so it's what was a interesting experiment and that is how I started
[519.44 → 528.64] then I just keep going i I use conferences and public speaking as an excuse to learn things that I want
[528.64 → 536.20] to learn so I prepare a talk and then i I have to learn something to the degree that I can give a talk
[536.20 → 543.48] and I can answer the questions that sometimes it's really hard so yeah it's how we get into that so
[543.48 → 550.90] the 10 a half moment comes from the exploration that keeps going preparing other talks that if you
[550.90 → 558.64] want we can't keep talking about it yes and also uh I already hear episode number two part number two
[558.64 → 563.20] of this one do you want to start with the first biggest aha moment how would you go we
[563.20 → 568.22] would go about that the biggest the most impressive ones or the most uh chronologically like the
[568.22 → 574.26] order of that yeah I think I like the chronological approach because it's kind of easier for understanding
[574.26 → 581.92] my head and probably sometimes explain why it's an aha moment and the first one for me is exactly
[581.92 → 588.06] about the slices maps and channels and specifically about the slices that was how slices are implemented
[588.06 → 596.84] in the day hood because when I started writing you I was said that you have slices and the slices are
[596.84 → 604.14] immutable, and then you just append things to that slices, and then you get an appended version
[604.14 → 611.96] of the slice um the thing is that sounds really, really inefficient it's looks like it has to be
[611.96 → 617.70] inefficient how in the hell are you doing that to make it that efficient then you realize what when you
[617.70 → 623.64] start investigating the code you start realizing how they are doing it, and it's really smart you are
[623.64 → 630.50] slices are not slices just a sort of pointers and counters the real data is a sword under the hood
[630.50 → 639.42] in an array and that array is changing in size, and it's automatically managed for you and the growing
[639.42 → 646.44] of the slice or the growing of the underneath array is not something like I going to add one add
[646.44 → 654.44] one it's normally doubling the size of the previous array to store more data and then you because of that
[654.44 → 663.42] you understand why you should be pre-allocating the array size all that kind of stuff was one of my
[663.42 → 669.98] first aha moment was like oh so that's the reason why it's efficient it's really a smart approach
[669.98 → 676.24] actually then you have some pitfalls that you know because you know how it's implemented under
[676.24 → 683.08] the hood, but there are some pitfalls around that approach that is using multiple slices that point
[683.08 → 689.42] to the same array and some of them and one of them get resized were connected before because we're
[689.42 → 696.14] accessing the same underneath array, but suddenly they are not connected anymore so it's kind of a weird
[696.14 → 703.14] behaviour that it is unexpected I guess if you don't understand the implementation details but yeah
[703.14 → 710.52] that was my first one the the first aha moment was like oh then that is how they make this efficient
[710.52 → 717.30] and make this work smoothly so were you comparing it to what you know from other languages or was it
[717.30 → 723.18] more like this is the first time on that okay for arrays I'm focusing on how's it done under the hood
[723.18 → 734.66] yeah i think from python was a very similar it's not the same because in python I'm not 100% sure
[734.66 → 741.28] in python they are not appending things you are saying hey I have a list of elements and I'm adding
[741.28 → 747.14] things to that list so you semantically you are understanding that you are adding things to the
[747.14 → 753.80] list under the hoodie if I recall correctly it's pretty similar the behaviour is just an array of memory
[753.80 → 759.68] that keeps doubling and the, and you have this pointer and these counters that give you the lens and the
[759.68 → 766.32] capacity all that is almost exactly the same if I recall correctly i I don't have the python
[766.32 → 772.80] implementation very fresh yeah of course it's been a yeah we're not talking about the focus of a
[772.80 → 779.92] of go of python source code I'm I'm just curious if you generally in uh were focusing on the same
[779.92 → 787.38] topic for other languages or was go kind of where you started really diving into this no i i I start in
[787.38 → 794.58] python before and then I started with go because I was using go every day so they the whole point
[794.58 → 801.14] was it's a tool that I use every day I want to understand it better that's the reason why I did
[801.14 → 808.02] that in python before I want to do that with all the tools that i I use I did that with git in the past i
[808.02 → 815.12] want to do that with Postgres in the future but yeah it's something that I want to do I don't know if
[815.12 → 820.96] it's going I going to do it's a matter of time, and sometimes it's hard to find the time for that
[820.96 → 827.60] but yeah yeah it's like an advent of uh diving into code can be a fun project instead of solving
[827.60 → 833.52] challenges like in advance of code actually reading somebody else's code and learning those things
[834.32 → 842.00] yeah new year's list yeah yeah it's its challenging I have to say that go helps a lot there go is a great
[842.00 → 850.00] language to read because it's feels like home everywhere of course the algorithms and the
[850.00 → 857.44] the complexity of the different projects it's its different and reading a compiler a source code it's
[858.32 → 864.64] it's a tough thing because it's a compiler the complexity of a compiler is already big enough to be
[864.64 → 873.92] challenging but at the same time you see the same kind of styling everywhere the code is it's its kind
[873.92 → 882.56] of familiar okay this is an error if error whatever than nil whatever all that things are kind of the
[882.56 → 890.64] same so you feel it feels less weird than other languages where every project has its own styling
[890.64 → 898.40] yeah yeah very much goes to our human need for pattern recognition for sure yeah exactly I agree okay
[898.40 → 905.52] so you say that the arrays' implementation was making sense and was a little bit familiar also
[905.52 → 912.24] speaking to your pattern recognition as well yeah so no I was interested in that at the end of the day
[912.24 → 919.12] most of the implementations for example slices and maps is not like super weird implementation you can
[919.12 → 925.36] find very similar implementations other languages it's its just a relatively standard implementation of
[925.36 → 931.28] certain things there are details on for example maps that can be different from other languages
[931.28 → 939.92] for example in go maps keys are unsorted and are unsorted on purpose actually they are unsorted
[939.92 → 947.76] on purpose up to the level that every single map have a random seed for the keys so it's two
[947.76 → 953.92] different maps with the same keys and the same values are going to be ordered differently so it's its
[953.92 → 959.04] kind of it's on purpose it's by design but at the end of the day most of the languages have its own
[959.04 → 965.28] implementation of this kind of things, and they are all most of them are kind of similar around hash
[965.28 → 974.56] maps and slices and all that stuff okay how about uh the second aha moment okay next step one of the
[974.56 → 982.48] things that I was intrigued about go because it's one of the key things is um go routines is something
[982.48 → 989.28] that everybody wants in go everybody loves in go and I did want to understand better what a go routine
[989.28 → 996.72] is and how it works and I started digging into the source code and I started investigating how
[996.72 → 1002.16] the go routines works under the hood from the perspective of the go routine how of the life cycle of the
[1002.16 → 1009.68] go routine and actually for that I prepared another talk that is called the sacred life of a go routine
[1010.32 → 1019.52] and that in that talk what i I try to do is follow the process of when a go routine is created how it's
[1019.52 → 1026.32] created and what are the steps that the go routine goes through and how it changed from one
[1026.32 → 1032.56] state to another and what are the reasoning around that changes and one of the things that I discovered
[1032.56 → 1038.96] while I was doing that was it's something that I already have the kind of the intuition around that
[1038.96 → 1047.60] or the understanding about that that is go routines are cooperative but whenever I start seeing the code
[1047.60 → 1053.92] was more obvious and evident that it's a cooperative approach in threats in operating system threats you
[1053.92 → 1060.00] have the operating system deciding when to cut something and assign another threat to the processor
[1060.72 → 1069.36] in go the go routine itself is the responsible for saying hey I have to stop just I going to call the scheduler to i
[1069.36 → 1075.92] going to stop myself call the scheduler to select another task or another go routine and the go routine is going to start running
[1075.92 → 1105.76] not only that the go routine I stop myself because I waiting for something and the one that is going to wake me up is another go routine for example whenever to just send something to a channel, and it's some another go routine waiting it's a are going to wake the go routine that is sending to that channel is going to wake up the other go routine so they are collaborating together to do all the processing there's some special go routines like the system monitor go routine that is a
[1105.92 → 1135.90] is doing certain thing or the net pool that also it's kind of monitoring certain things for getting back that go routines whenever they finished but in general the go routines are waking up each other or are sleeping by themselves and calling the scheduler to select another go routine so that cooperative nature of the go routines is something that I found very interesting and was an aha moment for me also yeah so you said the previous one the arrays one made a lot of
[1135.90 → 1164.66] sense does this one make a lot of sense would you have done it somehow differently I think it's kind of a natural way of doing that whenever you are doing coroutines that it is not exactly the same a coroutine that what ghosts have, but it's this kind of cooperative approach where you have one single thread, and you have to decide when to change to one or another, and it's its just easier if you let the go routines collaborate
[1164.66 → 1192.66] than if you have to put another process on top of that orchestrating all of that go routines because actually the scheduler the go scheduler is not another process it's not another go routine it's nothing like that the go scheduler is a chunk of code that the go routine that is going to sleep or the go routine that finished his work, and it's going to go to that it's going to call the scheduler code and the scheduler code it's going to transfer
[1192.66 → 1206.30] transfer somehow transfer the execution to the scheduler the scheduler executes and select another go routine and transfer to that go routine the execution so it's just a chunk of code that transition from one
[1206.30 → 1211.84] go routine to another it's its it's pretty cool actually it's its fascinating code
[1211.84 → 1239.84] I don't know if I answer your question actually yeah yeah another philosophical question a little bit um as a background for the question have you watched rick and Morty do you know the concept of the Mr me six oh no I don't sorry so there is a concept of a little blue creatures that is called Mr me six, and it's very I found it super helpful to understand this concept and also of like spinning up a task that has to do exactly one thing, and then it dies
[1239.84 → 1257.40] I think it's I think it's probably there are some developers and the creators of the show because I found lots of similarity and then when AI came and the concept of agents autonomous agents in the world of AI not the world of software it's also a little bit similar in the sense that AI agent gets a task, and then it spins off
[1257.40 → 1268.76] subtasks, and then it finishes the task and kind of buckles up to report so i kind of see similarity between the three of them and I hope that in those two and a half sentences I explained
[1268.76 → 1275.48] enough of this logic to you but uh this will be my guiding question kind of throughout our conversation
[1275.48 → 1283.02] on the aha moment because I like finding lots of equivalents between our current day software and what i
[1283.02 → 1290.48] try to imagine AI based software will be so this is kind of I don't know you're not familiar with rick and
[1290.48 → 1293.34] Morty I get that that's uh probably better
[1293.34 → 1301.04] have you played at all with AI agents what do you have enough experience to say an opinion about this or
[1301.04 → 1307.84] not yet actually i I haven't played I don't know what you mean with an AI agent so
[1307.84 → 1315.16] that autonomous agent is a better name yeah I guess it's something like you ask to realize a task and
[1315.16 → 1323.20] it's going to use external resources or external actions to fulfill the task something like that I guess
[1323.20 → 1329.20] it uh basically the AI goes and decides what is the sub tab like you give it a goal it breaks it
[1329.20 → 1336.14] down to sub-tasks, and then it spins off mini AIs to execute those tasks let's say which is very
[1336.14 → 1348.02] similar to that concept yeah yeah could be yeah no i I don't I it's hard for me because i I like AI I have
[1348.02 → 1355.64] I have used it but I'm not very into very deep into that but yeah i I think there are similarities at
[1355.64 → 1362.42] the end of the day what go routines are is just processes that are kind of independent as up to
[1362.42 → 1368.72] certain degree they have a task they have to realize that task and they are kind of independent of
[1368.72 → 1374.38] the rest of the go routines there is an actually what is something like for some people's
[1374.38 → 1380.04] weird is go routines doesn't have a parent if I recall correctly so go routines are go routines there's
[1380.04 → 1384.56] no relationship with three go routines you can execute thousands of go routines, and they are not
[1384.56 → 1389.52] related to each other not even with the parent or the execute or the one that's pawned so
[1389.52 → 1397.04] I don't know I think I'm a bit lost with your questions to me yeah yeah yeah well just to it's even
[1397.04 → 1403.40] more like an opinion than a question but just to confuse a bit more, and then we move on to number three
[1403.40 → 1409.82] another similarity that I see there is also to the concept of threads in um in processors
[1409.82 → 1417.20] I know how much you got a chance to dive into like a like operating system breaking down things into
[1417.20 → 1421.56] telling the different processors how they run around their tasks and so on, but there's also like
[1421.56 → 1428.06] now you have a threat and so on so it's also I see some similarity in those concepts and i personally
[1428.06 → 1433.62] find it really cool that it kind of goes between the different fields that have something
[1433.62 → 1437.92] to do with each other but not fully yeah just an observation it's not a question if you have
[1437.92 → 1443.52] experience there I'm happy to hear your thoughts if not tell us about numbers in in in threads and
[1443.52 → 1447.94] the difference between threads and go routines or something like that or yeah if you want to chat
[1447.94 → 1453.24] about that yeah well now it's interesting how it's solved in in the go runtime it's its
[1453.24 → 1459.72] basically they abstract you from the operating system trends and call them CPUs actually processors
[1459.72 → 1465.44] actually and then that processors gets assigned to different go routines but the go routines and the
[1465.44 → 1471.88] processors are not highly coupled so they can, they normally have certain the certain
[1471.88 → 1479.16] tendency to execute in the same processor on the same operating system thread, but it's not necessarily
[1479.16 → 1485.60] it's not mandatory at all for the go routines so the go routines can execute in different operating
[1485.60 → 1491.90] system threads so it's a very smart approach that decouple the CPU and them and the go routines or the
[1491.90 → 1499.88] operating system thread and the go routines and allows you to execute at full capacity of your processors
[1499.88 → 1508.16] using that architecture because yeah because if a CPU is overloaded you can take the go routines from
[1508.16 → 1514.60] other CPU and start executing in the one that is more free things like that so it's its an it's very
[1514.60 → 1522.76] cool how go abstract you from CPUs operating system threads and the go routines so it's its pretty
[1522.76 → 1529.86] cool yep and efficient so what is your number three aha moment okay number three oh well
[1529.86 → 1537.02] this this this was a kind of silly one I was investigating around the I was investigating
[1537.02 → 1543.64] the compiler and one of the things that i I started investigating was the process for
[1543.64 → 1551.88] tokenizing and parsing and whenever I start reading the parser I just realized that it was obvious in any
[1551.88 → 1562.04] way but I realized that whatever is in the parser in the ast3 is what you can have in a go file there's
[1562.04 → 1570.46] nothing else so if you start seeing how the ast3 the abstract syntax tree for go is generated you are going
[1570.46 → 1579.98] going to see that is one abstract syntax tree per file, and it's going to have an import a set of declarations
[1579.98 → 1589.02] and a set of imports and a declaration can be a constant a variable a function and a type and that's it
[1589.02 → 1596.46] there's nothing else that can be in a file so what's kind of a sensation of complete understanding of
[1596.46 → 1603.48] something I say okay now I know where is the boundaries so everything it's inside these
[1603.48 → 1609.06] boundaries there's nothing else that can go in a file, so there's nothing that I am I'm missing
[1609.06 → 1616.80] constants variables functions and types and the import and the package name that's everything
[1616.80 → 1623.98] and what probably is kind of silly but for me was like an aha moment so it was like oh that's it
[1623.98 → 1629.56] of course then you have the body of the functions and all that stuff and there's a lot of stuff that
[1629.56 → 1637.22] goes there but yeah inside a file you only have that the things this makes me think of how in c
[1637.22 → 1641.78] there is the I think it's in c that you have the header file, and you have the code file
[1641.78 → 1648.22] right it's kind of similar let's scope our little universe, but this is scoping it for
[1648.22 → 1652.96] that file, but it's its kind of like knowing that this is everything that's included there
[1652.96 → 1660.42] yeah it's kind of like that exactly is you have a clear definition of what can go there it's not
[1660.42 → 1666.78] exactly the same because in the h file you are saying hey these are the functions that I declare it's
[1666.78 → 1674.12] kind of publishing this is a public interface but at the same time is like okay yeah if I understand
[1674.12 → 1681.34] the h file in theory I should be able to use it and I should be able to understand all the
[1681.34 → 1687.96] boundaries so yeah, and you say that what you liked more than that this is like defining scoping
[1687.96 → 1693.48] it for this file it's kind of scoping it for go in general that this is your entire toolbox and there
[1693.48 → 1701.26] be no surprises it's like not keywords but tool toolbox really yeah there 's's nothing else
[1701.26 → 1712.48] if is you think oh could I execute a chunk of code inside the main file but outside the function no you
[1712.48 → 1719.68] can't that's it that it is a variable declaration then you can, it's a constant then you can, but it's
[1719.68 → 1727.78] not that it's not a type definition or a function you can't there's no representation for that you
[1727.78 → 1734.94] can't represent that in the AST now there are the dramas and this kind of, but they are comments
[1734.94 → 1743.28] that are handled in a smart way but at the end of the day the AST is just that there's nothing else
[1743.28 → 1749.04] that you can represent with that sounds like it is has not been a talk yet this aha moment not
[1749.04 → 1755.46] really it's there's a talk the aha moment comes from a from another talk that I was preparing actually
[1755.46 → 1763.24] that was the at the time I was preparing the understanding the go compiler actually was called
[1763.24 → 1768.50] hello world from the code to the screen I prepared that talk I did that talk in the go for con us
[1768.50 → 1777.60] but then I made uh update of an updated version to the last version of the go compiler for a go for
[1777.60 → 1783.24] con UK and I renamed that to understanding the go compiler because it was more clear the title and I don't
[1783.24 → 1789.16] want to mislead people around what I'm going to talk but yeah it was on that understanding the
[1789.16 → 1794.20] compiler and I go through the all the whole compiler and there there are a lot of aha moments that
[1794.20 → 1802.02] comes from that talk because I went through the whole process of compiling and the idea was I have
[1802.02 → 1810.28] a hello world and that hello world is going to be the main character of my talk is going to go
[1810.28 → 1817.72] through the whole process of transformation until getting to a binary and I want in the talk i I guide
[1817.72 → 1824.40] you through the whole process and that's a that's the idea and this aha moment comes from that
[1824.40 → 1831.68] and there's some of them some that come from that too so if you want we can jump to the next one actually
[1831.68 → 1838.48] yeah yeah let's do that so aha moment number four yeah I think so when I was investigating that
[1838.48 → 1845.50] one of the things that I investigate during the process were two characteristics that were escape analysis
[1845.50 → 1851.92] and inclining and the escape analysis for that people that doesn't know that escape analysis is a
[1851.92 → 1860.84] process inside the compiler that is going to decide if a variable it needs to be a store in the heap or
[1860.84 → 1867.80] can be a store in the stack so that's that decision is made through escape analysis that basically decides
[1867.80 → 1875.22] hey if it's possible for me to use the function stack to restore this data or because
[1875.22 → 1884.10] the scope of this variable escapes from the function I need to store some somewhere else that means
[1884.10 → 1891.46] basically the main memory the heap so that um that is what escape analysis does on the other hand
[1891.46 → 1899.18] you have inlining it's a process that analyzes a function in the co-compiler it's a process that
[1899.18 → 1907.60] analyze the function and decide if the function is simple enough to be embedded to be inclined in the
[1907.60 → 1914.64] other side in the call side instead of calling the function you are going to take the whole code of the
[1914.64 → 1921.40] function and replace the function code with the code itself that is inclining, and it depends on the
[1921.40 → 1927.54] complexity of the function that it not necessarily means the size of the function it means the size of the
[1927.54 → 1934.16] function but actually means the operations that you use inside the function so the cool thing that i
[1934.16 → 1941.42] learned was if you have escape analysis that the size of function it needs to go into the stack or the heap
[1941.42 → 1947.96] and you have inclining that allows you to take a function and put the function in place of the caller
[1947.96 → 1955.20] what is going to happen is they are going to collaborate together so if your function is simple enough
[1955.20 → 1962.88] it's going to be inline and suddenly the scope of your variables is bigger so it's more probable
[1962.88 → 1969.44] that you can use the stack instead of the heap so that was very cool that was very interesting its
[1969.44 → 1976.28] yeah it's its something that I found fascinating yeah and then what did you have any
[1976.28 → 1982.64] any chance of implementing this function like writing code that is kind of corresponding to this
[1982.64 → 1988.20] functionality that was extra efficient or interesting or not or is there a use case you can imagine for
[1988.20 → 1994.08] this to be interesting or because as you were describing this i i I had nothing come to mind
[1994.08 → 2001.02] there are use cases i think you have it's its a tool that you have there and sometimes
[2001.02 → 2007.92] you have you can say okay I have a very tight function here that is generating a lot of allocations
[2007.92 → 2017.44] then I can try to tweak that to reach the point where this gets in line so that's one option but also
[2017.44 → 2025.82] I think the cool part is knowing that you can make decisions that are just smarter around creating your
[2025.82 → 2033.10] your structs for example if you have a new function for creating a new struct, and you have initialization
[2033.10 → 2040.32] process in that inside that that function that new function that new function almost for sure is not going
[2040.32 → 2048.02] to be in line because the initialization process it's going to get complex enough to not get embedded to not
[2048.02 → 2055.70] get in line, so the scope of that variables is always going to be whenever you execute new is going to
[2055.70 → 2062.72] return a pointer to that variable and because of that is going to always go into the heap but if the function is
[2062.72 → 2069.40] small enough if you say hey the new function is going to create the object and return the pointer
[2069.40 → 2076.68] suddenly the new function is always embedded it's always in line, and it's always a store in the stack
[2076.68 → 2083.90] in the stack of the parent unless there's other reason for escaping, but you are storing that in the stack of
[2083.90 → 2091.52] the parent and then if you call for example initialization function that initialization function is already
[2091.52 → 2099.68] working in the stack so keeping your constructors small enough to get them embedded
[2099.68 → 2107.80] than in line if it's going to be a good practice in general so for example that is a good
[2107.80 → 2116.94] thing because it's not going to give you a huge boost in performance, but it can get you tiny improvement
[2116.94 → 2125.72] in performance here and there and suddenly you are gaining well that adds up at the end so yeah it's
[2125.72 → 2130.68] yeah that that makes a lot of sense that that would be actually fascinating to also run tracing on
[2130.68 → 2136.26] that for example and to compare yeah if depending on the size of your application you can have
[2136.26 → 2141.70] thousands a thousand of creation of certain objects and if they go to the heap instead of the
[2141.70 → 2147.74] stack it's going to be a lot of allocation a lot of garbage collectors pressure a lot of other stuff that maybe
[2147.74 → 2150.48] is not that important so
[2150.48 → 2156.18] or actually we'll find a like big differences I would be I would be very curious we do have a
[2156.18 → 2164.22] tracing episode in planning part two of that so that will be I will remember to do a cross and to bring this up there as well
[2164.22 → 2171.94] yeah it's a cool observation yeah actually I think the inline now it's been rewriting I don't know if it's already
[2171.94 → 2178.02] finished the work I think in 23 it will be released in the updated yeah with the profiler right with a
[2178.02 → 2184.98] with a profile guide optimization so yeah that's that that can be very, very cool to see if that is going to
[2184.98 → 2191.06] have a huge impact because probably it's going to have certain impact there yeah anything else to say about point
[2191.06 → 2198.30] number four I don't think so okay we have to we have a lot of field to cover still so all right
[2198.30 → 2206.70] jumping back, and we are continuing now with aha moment number five and six yes the other thing that i
[2206.70 → 2213.60] was doing well i I keep investigating the go compiler and go through different steps in the process and i
[2213.60 → 2220.52] reached a point that was fascinating for me that was another aha moment that was when the go compiler
[2220.52 → 2230.38] gets machine specific so all the process related to tokenizing parsing um there's an intermediate
[2230.38 → 2237.04] representation uh in the middle then it's converted to something that is called SSA that is single
[2237.04 → 2244.80] a single static assignment, and then it's applied a lot of optimizations and there's a point in the process of
[2244.80 → 2252.94] converting SSA or processing SSA where it's applying optimizations and accepting point there's one of the
[2252.94 → 2262.26] passes of the optimizations that is called lower that is the exact point where the compiler start doing
[2262.26 → 2270.16] things that are machine specific everything before that point it's machine agnostic is if you have an
[2270.16 → 2280.88] IRM or if you have a MD AMD 64 doesn't matter it's all the same code base and then gets into this lower
[2280.88 → 2290.44] phase of the SSA transformation or SSA passes and gets converted into a machine specific SSA and then
[2290.44 → 2297.56] apply other optimizations and finally with that optimization supply start generating the binary the
[2297.56 → 2303.42] linking and generate the final binary that is an executable, but it's its pretty cool that very far
[2303.42 → 2311.04] in the process it's when you get the machine specific part that by itself was an aha moment and was very
[2311.04 → 2316.94] interesting for me but I'm also a big fan of tiny go I love microcontrollers I love playing around I'm not
[2316.94 → 2323.34] good at it but I love playing around with them and for me, it was kind of interesting how tiny go was
[2323.34 → 2330.46] doing that, and it's very interesting that tiny go it's follow a very smart approach it's basically
[2330.46 → 2338.84] taking everything up to that point everything up to SSA it's up to that point is the same compiler
[2338.84 → 2346.98] it's the same code base mainly and in that point it takes that SSA and instead of converting that SSA
[2346.98 → 2355.76] into machine code it's going to convert that into a SLBM intermediate representation or SLBM
[2355.76 → 2363.46] kind of self-assembly and then SLBM is the one responsible for compiling that to the microcontroller
[2363.46 → 2370.78] specific architecture so apart from that you have to have a runtime that is compatible with microcontrollers
[2370.78 → 2376.06] because in microcontrollers you don't have the same kind of access to things you don't have an
[2376.06 → 2381.66] operating system and things like that but at the end of the day the compilation part is exactly the
[2381.66 → 2387.96] same so that is the reason why tiny go it is exactly the same language you can have differences in the
[2387.96 → 2393.86] runtime, but you don't have differences in the language because it's the same one, and it's leveraging that
[2393.86 → 2400.66] point so for me that was like oh wow these people is really smart so I really love that aha moment
[2400.66 → 2403.72] and actually I'm a big fan of tiny go
[2403.72 → 2413.78] shouting out to the cool things that tiny go does and uh together with the Ron and Ron Evans and uh
[2413.78 → 2419.88] Daniel Esteban and the team who is working on the cool projects around that oh yeah yeah that is uh
[2419.88 → 2426.52] that is interesting i how would you say that this so if this maps easily to across the different
[2426.52 → 2435.50] processors, and it maps also to little tiny embedded tech would that be how would that be working on GPUs for example
[2435.50 → 2442.04] yeah that's that's interesting I think the GPUs have a different set of instructions
[2442.04 → 2449.50] so I don't think it's it fits really well with that the things I'm not an expert to be honest
[2449.50 → 2456.72] but my sensation here is what you have is a cell assembly that is oriented to a general purpose CPUs
[2456.72 → 2465.36] and that general purpose CPUs gets a general purpose CPU cell assembly gets converted into real
[2465.36 → 2474.30] general purpose CPU like IRM or amd64 or things like that so applying that to CPU you can apply
[2474.30 → 2482.40] the same set of ideas probably you can write you can do what rod pike did here that is or what the
[2482.40 → 2492.74] go team did here that is taking the generating a cell assembly that is going to be for GPU code and
[2492.74 → 2500.90] build that up to the level that you have this intermediate language and whenever you reach that
[2500.90 → 2508.10] point you convert that into the specifics of different GPUs assembly code or instructions
[2508.10 → 2516.54] but I don't think it's applicable to execute the go binary for example or go binary directly into a GPU
[2516.54 → 2523.06] because I think half different set of instructions is not the same kind of machine that
[2523.06 → 2530.12] you are managing there yeah that's fair again I'm not an expert maybe I'm yeah I'm wrong here so it's its a
[2530.12 → 2536.30] guess it's a guess it's a surprise question yeah yeah yeah but that definitely is interesting and i
[2536.30 → 2542.88] will go and uh look about that a little bit I'm also now curious you said embedded tiny go and
[2542.88 → 2547.30] although this connection has been around in forever I'm kind of only now starting to think will it be
[2547.30 → 2552.20] how different will it be for FGAS for example and like all the other hardware out there in
[2552.20 → 2558.34] the world um when maybe one day we'll do an episode about go and different um different processing units
[2558.34 → 2568.46] yeah uh well we only covered five six of the ten, but we're slowly approaching uh our time which
[2568.46 → 2573.20] means we will have to do a part two because you're you're just bringing up two interesting points and i
[2573.20 → 2577.80] have too many questions slash comments about them my last question to you would be done you have an
[2577.80 → 2604.72] unpopular opinion okay i think I'm going to get some hate for this uh so well that's what
[2604.72 → 2615.78] unpopular opinion is about yeah I think mechanical keyboards are just glorified nostalgia so it's a
[2615.78 → 2624.82] loudly glorified yeah very loud glorified nostalgia so that's that's the thing i I have used them
[2624.82 → 2631.14] I don't think are more comfortable I don't think are more are better for sure I'm not going to make
[2631.14 → 2637.00] you a better programmer or improve your performance or something like that there's no way i
[2637.00 → 2642.00] understand for some cases pretty cool whenever you are building your own keyboard or this kind of
[2642.00 → 2648.12] split keyboards or programmable keyboards that you have your microcontroller and things like that for
[2648.12 → 2654.34] that kind of cases I found that cool because you can have your switches and all that stuff and there's
[2654.34 → 2661.28] a lot of pieces out there for doing that kind of things but I don't know paying 10x it's its all the
[2661.28 → 2667.92] 10x that you are going to get for a keyboard is 10x in the price and the sound the noise oh yeah exactly
[2667.92 → 2675.42] and the decibels yeah getting that 10x in the price for something that is I don't know
[2675.42 → 2682.12] probably it's an unpopular opinion i get that people the people that is going to consider this
[2682.12 → 2688.76] unpopular is going to consider this very unpopular so let's see well I cannot say I don't agree with
[2688.76 → 2695.00] you at least with me, you're you are popular my opinion is on the unpopular opinion is on a similar
[2695.00 → 2703.90] topic and trackpads are better than mice I use a mouse but yeah i I think so
[2703.90 → 2712.10] well I guess we both agree then with this consensus I will say thank you so much for
[2712.10 → 2717.60] joining and sharing your interesting insights and I am looking forward to episode two and thanks
[2717.60 → 2720.08] everybody who joined yeah thank you for having me
[2720.08 → 2729.84] that is go time for this week thanks for listening along subscribe now if you haven't already headed to
[2729.84 → 2737.50] gotime.fm for all the ways or simply search for go time wherever you get your podcasts you'll find us
[2737.50 → 2744.24] hey do you receive our changelog newsletter each Monday if not let's fix that bug one reader calls
[2744.24 → 2751.64] it is so good he considers it a competitive advantage sign up for zero dollars at changelog.com
[2751.64 → 2758.68] slash news thanks once again to our partners at fly.io to our mysterious beat freak break master
[2758.68 → 2764.60] cylinder and to our friends at sentry we love sentry you might too use code changelog when you're
[2764.60 → 2771.34] signing up for a team plan and save 100 bucks why not right that is all for now, but we'll talk to you
[2771.34 → 2773.68] again next time on go time
[2773.68 → 2776.32] you
[2776.32 → 2778.34] you
[2778.34 → 2780.34] you
[2780.34 → 2790.34] you
[2790.34 → 2792.34] you
[2792.34 → 2794.34] you
[2794.34 → 2796.34] you
[2796.34 → 2798.34] you
