[0.00 → 16.48] let's do if it's go time welcome to go time your source for wide-ranging discussions from all
[16.48 → 24.18] around the go community find us on the web at gotime.fm on the Fediverse at go time at changelog. Social
[24.18 → 31.42] and on x at gotime.fm thanks to our partners at fly.io the home of changelog.com launch your app as
[31.42 → 37.46] close to your users as possible find out how at fly.io okay here we go
[37.46 → 48.24] what's up gophers I'm here with kyle barberry CTO at coder.com so kyle I've known coder as the IDE in
[48.24 → 54.44] the cloud and over time you've iterated to become a fully open source cloud development environment
[54.44 → 60.60] a CDE how do you explain what coder is and what it does coder is a platform to provision you a
[60.60 → 65.60] development environment on any cloud infrastructure that might be in a VM that might be inside a
[65.60 → 70.28] container, but coder is kind of a developer's route to provision infrastructure for them to write
[70.28 → 75.20] software inside we started with the IDE which is kind of like putting VS Code in the browser
[75.20 → 79.78] which is what most people are certainly familiar with us for and we kind of funnelled that into
[79.78 → 83.68] more of a platform where people provision the infrastructure and a lot of people do use a web
[83.68 → 88.74] IDE with coder a lot of people use a local IDE and just connect in okay so what are teams coming to you
[88.74 → 93.84] for who's coming to you what people really come to us for particularly this problem is really
[93.84 → 98.62] exacerbated if you're a large enterprise is when you have like 500 engineers that are trying to
[98.62 → 103.90] update like a version of python, and instead we allow one engineer to go through that tedious work of
[103.90 → 107.98] updating some scripts or some docker container, and then you can actually just deploy that in one
[107.98 → 115.36] click to say like 500 engineers and make it really, really simple let's laser focus in on the platform
[115.36 → 121.76] engineer it is that team's job to provide the best infrastructure the best platform for their given
[121.76 → 129.08] applications for their teams what are some signs or signals for platform engineers to think about when
[129.08 → 133.56] it might be time to consider a cloud development environment like coder.com so as a platform
[133.56 → 138.92] engineer developers might constantly be opening like it tickets that their computer isn't working
[138.92 → 144.26] properly they might constantly want to update dependencies, but that's a big mess you constantly
[144.26 → 150.22] have to email people across your team to say hey Adam could we update from java 17 to java 18
[150.22 → 154.92] those are the kinds of problems that people typically have that's the status quo you ship people more
[154.92 → 159.82] powerful laptops to improve the build times of your projects you try to reduce the complexity of
[159.82 → 165.16] your products instead of simply you know leveraging better hardware we believe that the future is
[165.16 → 170.56] leveraging the cloud for a lot of these things you can get more powerful instances in GCP or AWS that
[170.56 → 175.12] can make the build times faster instantly you can let one developer create a standardized environment
[175.12 → 180.48] and then distribute it to a thousand so that when you're updating from java 17 to 18 it's just a simple
[180.48 → 185.58] pull request you can co-locate your servers right next to something like s3 or a database they're
[185.58 → 190.62] using in development so that you get immediate data transfers, and it's not slow many of our customers
[190.62 → 195.58] which is a crazy thing to say, but they use absolutely massive monorepos, and they get clones that go from
[195.58 → 201.22] like 10 minutes or 20 minutes or an hour to simply like a minute or 30 seconds it's just a lot simpler
[201.22 → 207.52] when all of your engineers are standardized on one centralized piece of infrastructure and then one person can
[207.52 → 211.88] can impact the lives of hundreds of engineers and with that we don't believe that everything belongs
[211.88 → 216.58] in the cloud we think that some workloads are really amazing for it and some are absolutely terrible
[216.58 → 221.64] coder should be a self-serve offering to your engineers it should not be prescriptive where you migrate
[221.64 → 226.78] all pieces of software development into the cloud only the things that really get a lot better by running
[226.78 → 233.44] them in this cloud native way do we really promote moving well it might be time to consider a cloud
[233.44 → 240.76] development environment and open source is awesome and coder is fully open source you can go to coder.com
[240.76 → 248.96] get a demo or try it right now or even start a 30-day trial of coder enterprise once again coder.com
[248.96 → 252.94] that's c-o-d-e-r.com coder.com
[252.94 → 276.88] all right my name is Natalie and I'm here again with Jesus, and we are for recording now the second
[276.88 → 286.10] part of our topic of the 10 aha moments that this was had when reading the go code phase and we
[286.10 → 293.64] stopped at six, and we would, you like to do a quick recap before we jump into seven yes uh great well
[293.64 → 297.94] hello everybody yes welcome it's nice of you to join again I'm just jumping straight back in but yeah
[297.94 → 306.24] yeah that's fine uh lets uh let me recap the last episode we were talking about the
[306.24 → 313.42] some aha moments that come from some explorations in the ghost source code that comes from a couple of
[313.42 → 320.30] talks that I did one was around the different parts of the different building objects like
[320.30 → 327.38] slices maps and channels and the other ones will come from the compiler itself another talk
[327.38 → 332.64] that I did around the understanding the go compiler and we explore these different
[332.64 → 339.98] moments one of them was how slices work under the hood that was surprising for me another one was about
[339.98 → 347.16] the syntax and how the syntax of the of go have a representation inside the compiler that is the
[347.16 → 354.18] abstract syntax tree and having that knowledge about how the abstract syntax tree is represented was
[354.18 → 362.68] an aha moment for me because give me the understanding of what can have a file in go what are the
[362.68 → 370.14] boundaries of what exists in a goal file and what can't exist what are the building blocks exactly what
[370.14 → 375.42] are the building blocks and the fact that there's no more building blocks there's nothing else that
[375.42 → 383.04] I'm not seeing because I haven't read about it so that was another cool aha moment also another one was
[383.04 → 389.58] the cooperative nature of the go routines and how they wake up each other and how they stop
[389.58 → 395.28] themselves and things like that that was pretty cool also was another very interesting thing
[395.28 → 402.86] another one was when I was investigating around the compiler I started seeing this escape analysis
[402.86 → 409.04] concept the idea of how the compiler decide what goes to the heap and what goes to the stack
[409.04 → 416.88] and also the inclining that the compiler decides when to inline or not a function code how they work
[416.88 → 424.58] together to give you way better usage of the memory because sometimes the inclining process makes
[424.58 → 431.60] something that before went to the heap now because the inclining process now goes to the stack
[431.60 → 440.48] and that is faster so that was an another one the other one that i I also was super cool for me was
[440.48 → 448.22] understanding when in the compiler start the code that is machine dependent where in the process of
[448.22 → 455.10] compiling your program your code gets in a state that is machine dependent this is pretty late in the
[455.10 → 463.98] process is one of the passes of the static single assignment representation and that was um was really cool because
[463.98 → 472.44] than you realize that almost a huge percentage of the compiler is an architecture agnostic and that's that's
[472.44 → 480.22] pretty amazing the other thing and that is related to that is the fact that tiny go leveraged that idea and
[480.22 → 491.44] leverage the SSA representation to build the tiny go compiler basically you use the SSA representation of go to get that SSA
[491.44 → 500.06] use the whole compiler machinery already there to generate the SSA and instead of compile that SSA to a binary
[500.06 → 508.06] for your architecture it's going to intercept that point convert that SSA into a LLM intermediate representation
[508.06 → 517.60] and that SLBM sorry SLBM intermediate representation yeah SLBM is low level virtual machine not the large
[517.60 → 524.26] language model exactly the SLBM intermediate representation and that SLBM intermediate representation
[524.26 → 532.60] converts your that code into your microcontroller specific architecture so I found that pretty amazing
[532.60 → 538.84] and pretty smart and that were the six a half moment that we explored yesterday which was just the
[538.84 → 544.78] the previous it's okay it's okay it's okay to say what happened behind the scenes all good it became a
[544.78 → 550.78] became a long episode longer than expected so we broke that down into two okay that I think that's it
[550.78 → 557.32] that was what we were talking yesterday all right I'm ready to jump to number seven okay the number seven
[557.32 → 563.80] that comes from its kind of the interception between the talk around understanding the go
[563.80 → 571.14] compiler and my talk around understanding the go runtime that is the next obvious step well actually
[571.14 → 578.82] the next obvious step on whenever you are exploring this kind of things is stopping it's not this make no
[578.82 → 586.58] sense to keep going and keep going but well I'm I'm I'm a reckless person so I still keep investigating
[586.58 → 594.92] and start investigating the runtime and as part of that there was some interesting thing that i I saw
[594.92 → 602.46] and was kind of surprising not necessarily surprising was kind of if you think about it makes sense
[602.46 → 609.46] but I haven't thought about it before and now and then when I saw that I was surprised, and it's the fact
[609.46 → 616.34] that the compiler compiles to binary code in general so if you have an assignation of a variable it's going
[616.34 → 624.36] to be compiled into some binary code that is going to do some register change and some memory access and
[624.36 → 634.24] things like that but not everything ends up being compiled to that binary code per se some of the syntax
[634.24 → 643.64] that you see in the go source code is compiled to calls to the runtime instead of executing
[643.64 → 653.04] some assembly code some CPU instruction is going to delegate that logic to a chunk of code that is going to be always there
[653.04 → 660.94] that is the runtime for example some very common syntax that we use is inserting things in a channel
[660.94 → 669.38] or reading from a channel that syntax it's going to end up converting to an instruction in the assembly
[669.38 → 677.40] that is a call function to the runtime module to the specific function that sends messages to a chance and
[677.40 → 685.50] data to a channel or receive data from a channel so that was very cool because is this you see how smart
[685.50 → 692.60] is the design there because you always have this runtime the runtime is kind of easy to follow code
[692.60 → 700.62] and converting all that into assembly to represent the concept of a channel in the final assembly probably is going
[700.62 → 708.86] to get your binaries probably more bloated but not only that it's kind of simpler to design that you have a package
[708.86 → 716.94] that is always there and your syntax can compile to that based on the existence of that package so that was
[716.94 → 725.40] that was really cool, and you can easily see that if you use the go build flags if you pass the
[725.40 → 735.64] dash s in GC flags you get the assembly generated when drew build your program, and you can see in the
[735.64 → 742.92] assembly there all that calls to the runtime package so it's kind of easy to see that and it's for me
[742.92 → 749.18] it's pretty cool why do you think this was done this way or what would be another way kind of doing
[749.18 → 756.66] that that would be maybe better for another setup I think for example there is a constant in rush that
[756.66 → 763.90] is zero cost abstractions that is something that you have the syntax there, but the compiler is going to
[763.90 → 771.60] take care of all that, and it's going to generate the final binary for that abstraction without any runtime
[771.60 → 778.70] cost that is another way of doing that that is going to put more pressure in the compiler most
[778.70 → 785.20] it's going to take more time into the compiler to compile all that code, so probably that's one of the
[785.20 → 792.10] reasons if you have a runtime that is always there, and it's always ready to just be linked to your
[792.10 → 801.50] binary or be embedded in your binary probably is more is faster to compile and also I think the
[801.50 → 806.86] code is going to be simpler because at the end of the day with all this transformation all these
[806.86 → 813.30] generate this AST that suddenly represents something an intermediate representation and that intermediate
[813.30 → 819.40] representation convert that into instructions all that it's its kind of more heavy lifting than saying
[819.40 → 829.18] yeah whenever you see a channel sent just add a call to a function and that it is simpler I think that's the
[829.18 → 839.12] idea behind that I don't know for sure, but that's my guess it's faster for compiling or I guess it's
[839.12 → 845.72] faster for compiling, and it's simpler for the mental model perspective does it have something to do with a
[845.72 → 853.32] cross compilation flags that to kind of support that from your guesstimate I know it's a yeah it's a cross of
[853.32 → 860.78] too many topics yeah no i think it doesn't need to be related to that because the cross compiling
[860.78 → 867.30] part it's going to be well have some relationship because if you are already you find your runtime
[867.30 → 873.98] already cross compiled for another architecture you don't need to recompile that part over and over and
[873.98 → 879.70] over again so that it could cross compile one time and the rest of your code needs to be cross compiled
[879.70 → 885.82] that's the one that needs to be cross compiled but at the end of the day the runtime is just a go
[885.82 → 892.64] package like any other go package so at the end of the day probably the cross compiling wouldn't be
[892.64 → 897.94] that different because at the end of the day what you will do is something like okay to send
[897.94 → 905.86] message to a channel it's going to be a set of instructions that goes together and that's it
[905.86 → 914.12] so i wouldn't expect that to be affecting the cross compiling or again it's a guest as you
[914.12 → 921.98] said it's a guest is there any like recommendation for when writing your code you can have this in mind
[921.98 → 929.56] or is this too many layers and this is more of like a general bonus there yeah for me, i think
[929.56 → 938.40] part of this is about whenever you want to know more about how certain things works you can check
[938.40 → 944.72] out that and say okay it's calling the runtime directly so whenever i for example whenever i
[944.72 → 951.70] happen something to a slice it's just calling the runtime, so there are some things that are happening
[951.70 → 959.44] in the runtime that you can say okay if this is the runtime responsibility I can easily go to the
[959.44 → 966.32] runtime code and understand what is going on understand what means a happed to a slice or what
[966.32 → 974.86] it means to go to an add something into a mob or send something to a channel so you can easily explore
[974.86 → 982.16] that based on that that's the only thing that I see some value there in general my talks are
[982.16 → 989.24] completely useless so they are interesting knowledge I found that knowledge interesting but
[989.24 → 996.46] in general they are useless there's not much thing that you can apply directly because it's about how
[996.46 → 1003.96] things works and to be fair the go compiler works really well so you don't need to know how they work
[1003.96 → 1011.74] how the compiler and the runtime work so it's just for about being curious and understanding better
[1011.74 → 1019.98] certain things and yes time to time you find that knowledge useful but in general it's more about
[1019.98 → 1025.96] the pleasure of understanding what is going on under the hood yeah get that I guess that one time when
[1025.96 → 1031.10] where suddenly memories are eating in the wild way nobody understands why that one person knows that
[1031.10 → 1039.92] one very esoteric one fun fact this is where it comes in useful yeah it's like well I went to a talk
[1039.92 → 1045.54] from Nikki Teresa in African UK that was about brain-teasers he has a book about that
[1045.54 → 1053.92] also but about brain-teasers and was like oh I was able to guess like 50 of them the other
[1053.92 → 1063.36] 50 i I goes I got caught but that easily actually was like okay this is not something that
[1063.36 → 1070.64] that I will expect but there some of them I was like oh okay I know that it's going to behave
[1070.64 → 1078.64] really because I know how it works under the hood but yeah it's pretty cool so, but it's not especially
[1078.64 → 1085.02] useful in general as he said keep it in the back of their mind basically is what you say yeah exactly
[1085.02 → 1091.28] it's that one time when compilation is being weird yeah and yeah yeah exactly understanding some
[1091.28 → 1095.12] some small things here and there that can be interesting
[1095.12 → 1109.70] what's up friends I'm here with two new friends of mine from speakeasy sugar batch co-founder and CEO
[1109.70 → 1115.92] and George Hadar founding engineer so for the uninitiated speakeasy takes care of the entire
[1115.92 → 1122.30] SDK workflow to save you and your team significant time delivering enterprise grade SDKs to your
[1122.30 → 1132.64] customers in minutes you can generate best in class SDKs in typescript python go java c sharp and even PHP
[1132.64 → 1139.96] so sugar what's your excitement level for APIs and this API world we're living in I'm super excited
[1139.96 → 1147.44] about APIs I think we went to gen zero of the API first revolution and I think we're actually going
[1147.44 → 1152.94] to a second one now with the tailwinds of the AI ecosystem kind of causing that to be invigorated
[1152.94 → 1157.56] so yeah super, super psyched to be working in this space right now I think it's everyone's at a point
[1157.56 → 1163.64] now where everyone knows about rest APIs and GraphQL APIs and GPC APIs and now I think we're actually
[1163.64 → 1168.80] getting into the second phase of that which is how do people ship great developer experience
[1168.80 → 1174.22] in addition to the APIs and how do we build like truly best in class APIs that turn into
[1174.22 → 1179.64] they know longer infrastructure right this is kind of the vision I think that stripe helped
[1179.64 → 1185.22] manifest for everyone in the fintech space which is an API that really sets the bar for developer
[1185.22 → 1190.94] experience but also like it's something you can truly rely on right it's its a true if you make
[1190.94 → 1195.70] stripe a dependency of your company you can feel confident doing that and I think that's that's
[1195.70 → 1200.52] the part of API development that really excites me I agree that is exciting so George teams who
[1200.52 → 1208.18] leverage speakeasy are those who have leaned all the way in on documenting a solid open API spec and
[1208.18 → 1214.40] mostly want to be hands-off of their SDKs is that right precisely so you're coming to us because you
[1214.40 → 1220.62] want to be hands-off from that process you want to put all of your effort into documenting your API and
[1220.62 → 1226.24] then you're trusting and relying on great quality tooling to turn that into code and documentation
[1226.24 → 1231.74] which is what we're doing for you, you're not meant to change or edit the code because it will be
[1231.74 → 1237.66] regenerated the next time you change your open API so you ultimately put it in our hands once you've
[1237.66 → 1242.30] committed the changes to your open API it's its off to the races, and you get a new release of your
[1242.30 → 1247.94] SDK you'll get a pull request to review you will have the opportunity to look at the contents of
[1247.94 → 1253.80] the code but quite often you can let it hum along creating SDKs for you or new releases of your SDK
[1253.80 → 1259.38] every time you change your API very cool well the thing that got me with speakeasy that really helped
[1259.38 → 1264.76] me understand it was that as George said it is hands-off you can just focus on documenting your
[1264.76 → 1270.56] API via the open API spec, and you still have pull requests you still have visibility and in fact
[1270.56 → 1276.66] they will even hop into pull requests with you to triage any sort of anomalies or issues that come
[1276.66 → 1284.38] from the SDK generation and improve the back end of speakeasy to make future releases better for you
[1284.38 → 1290.08] I think this is so cool for teams who want to just be hands-off of their SDKs and focus on their product
[1290.08 → 1296.94] focus on the core documentation around the open API spec but still have all that awesome visibility
[1296.94 → 1305.74] okay, so the next step is to go to speakeasy api.dev you can start off with one free SDK that's so cool
[1305.74 → 1313.08] because you can go there right now and try it out completely free one free SDK let them know the
[1313.08 → 1318.74] changelog sent you let them know JS party sent you once again speakeasy api.dev
[1318.74 → 1327.36] okay let's jump to number eight yeah this is another one that is it has to do with
[1327.36 → 1335.02] this understanding on the knowledge that is good to have, and sometimes you don't really understand
[1335.02 → 1341.18] what's going on, and it's about the binary entry point whenever you execute a go binary whenever
[1341.18 → 1347.76] you learn go the first thing that everybody said is oh the entry point of your program is this
[1347.76 → 1353.64] main function that you define and then your program start executing there of course that's
[1353.64 → 1362.74] not true because we have a runtime so the very first thing that is executed in your binary it's a
[1362.74 → 1369.08] function that is dependent on your it's an assembly function a go assembly function that is dependent on
[1369.08 → 1376.08] your operating system and your architecture, and then it's a start initializing things I start
[1376.08 → 1385.32] setting up a lot of stuff the memory allocator the garbage collector the different CPU flags
[1385.32 → 1395.42] security related stuff a lot of stuff is done before even your main function is called so that was
[1395.42 → 1402.72] very interesting because you see the amount of things that are done before your main function is
[1402.72 → 1410.66] executed, and it's its pretty amazing also doing that process one of the things that happens is that
[1410.66 → 1419.40] your function your main function it's its executed through a go routine also it's not the main process
[1419.40 → 1425.14] and the go routines is something that happens after it's the go the first go routine is created and
[1425.14 → 1431.98] start executing your main function, so your main function is not executed outside any go routine and then you
[1431.98 → 1438.16] spawn go routines your main function is a go routine and actually after before your main function is
[1438.16 → 1444.10] executed there are other go routines already executing that the system monitor and things like that so there
[1444.10 → 1453.44] is a huge um not huge but a very interesting process there before your main function is executed and
[1453.44 → 1459.48] yeah i I found that pretty cool I mean on the one hand it's very it's a lot happening but on the other
[1459.48 → 1465.52] hand it's so fast, and it makes me think of that xkcd comic of uh where it's compiling right that they
[1465.52 → 1471.02] play swords, and it's kind of how it stopped happening and go because the same thing happens but just faster
[1471.02 → 1478.08] basically yeah it's it is goes really fast if it is actually the if you start digging into that
[1478.08 → 1484.70] initialization process most of them are very small tasks for example the memory allocator is just
[1484.70 → 1492.70] initializing some struts that are there, but it's not like it's not heavy lifting there then something
[1492.70 → 1497.94] like the garbage collector is just setting some flags here and there and the garbage collector is set up
[1497.94 → 1504.74] it's all small things a small set of struts that you define and a small initialization that you do
[1504.74 → 1510.52] and then when the program starts running it starts using that thing so for example whenever you need memory
[1510.52 → 1517.10] is going to start using the memory allocator whenever you need to recollect the garbage collector
[1517.10 → 1522.94] is going to kick off and all that stuff so it's there are a lot of steps there's a lot of a lot of
[1522.94 → 1530.94] things that happen between when you start your binary and your main function is called, but they are very
[1530.94 → 1538.16] small things very targeted things so yeah if you would is one went to go about looking into that how would
[1538.16 → 1547.58] you do that well how did you do this yeah I will recommend going and check out my talk so that will be
[1547.58 → 1556.04] a kind of easy path but if you want to do it by yourself that is perfectly reasonable what I did
[1556.04 → 1565.06] was gone to the well I went to the GDB debugger and find the entry point that in my case was in the
[1565.06 → 1576.36] slash run src slash runtime slash rt0 Linux amd64.s that is uh the entry point that's an assembly code
[1576.36 → 1584.66] there and then I start tracing that and going to the different calls that is doing and see what are
[1584.66 → 1593.30] that calls doing what are the initializing and all that stuff so basically i manually trace all that
[1593.30 → 1602.72] execution and that was my process was relatively hard it's not super easy because that you have
[1602.72 → 1607.76] some assembly code there that you have to can understand a bit it's not something that you
[1607.76 → 1613.18] need to understand a lot of assembly, but you have to understand a bit, and then you can just start
[1613.18 → 1620.24] tracing all these small steps here and there and then you have the scheduler initialization but the
[1620.24 → 1625.68] scheduler initialization includes the memory allocator initialization the garbage collector
[1625.68 → 1632.42] initialization, so there is a big chunk that is the scheduler initialization, but it's initializing a lot
[1632.42 → 1642.66] of stuff inside so tracing all that took me time, but it's not especially hard it's more time-consuming
[1642.66 → 1649.12] that hard that is what I perceived all the links will be in the show notes oh yeah yeah i can
[1649.12 → 1658.66] share some links there and actually if you see i I usually do that in my talks whenever I do i
[1658.66 → 1664.76] explain this kind of things I usually have um in the bottom right corner of my slides I have links to
[1664.76 → 1671.02] the source code that is kind of homework for the people if they want to go there and check the
[1671.02 → 1676.94] where the in the source code is happening whatever and yeah if you go to the slides of my talk
[1676.94 → 1682.14] and you start uh looking the different steps you are going to see that in the bottom right corner
[1682.14 → 1689.66] the link to the source file and the specific version of the go um runtime or compiler
[1689.66 → 1696.36] and yeah you can go there and check it it's its interesting i I don't know how many people do that
[1696.36 → 1702.84] and to be honest but I put that there yeah that's fair it's um it's nice to have sources for sure
[1702.84 → 1712.70] references yeah um okay number nine okay it's kind of related with what we have been talking its uh
[1712.70 → 1721.16] was the memory allocator i probably that that was more my fault than anybody anything else but I didn't
[1721.16 → 1727.04] know I didn't even know I didn't even think about the concept of the memory allocator inside go
[1727.04 → 1733.58] whenever you talk about memory management in go normally you talk about the garbage collector
[1733.58 → 1740.40] but I never thought about the memory allocator and the memory allocator was an interesting piece of
[1740.40 → 1746.72] software that I didn't know, and the memory allocator is the responsible for talking with the operating
[1746.72 → 1755.24] system and reclaim pages and free pages so it's very interesting part of the how memory is
[1755.24 → 1766.78] managing in go and actually what it does it is organizes the data in a way that it take pages
[1766.78 → 1776.04] set of pages what is called spams memory spams and that memory spams have a variable of the same size
[1776.04 → 1784.76] always so a spam can have 30 pages but doesn't matter the amount of pages that it has it always
[1784.76 → 1793.20] going to store variables of the same size that means if you have a spam of eight bytes all the variables
[1793.20 → 1801.00] of eight bytes is going to go there if you have a spam of 32 bytes variables of 32 bytes goes there
[1801.00 → 1808.92] and that is there is a set of spam size that are defined and are the bigger is the spam the
[1808.92 → 1818.12] bigger is the space between them for example you have an 8 16 24 32 and then I think it jumps to 48
[1818.12 → 1825.12] or something like that and then to 60 and then to 96 or something like that so it's jumping and there's
[1825.12 → 1830.40] more and more space between them, I don't remember the exact numbers, but there's more space between
[1830.40 → 1838.10] them that is important to know because if for example you store a variable that is 30 bytes for
[1838.10 → 1846.50] example it's going to be a store in the spam of 32 so it's going to take 32 bytes of a space no matter
[1846.50 → 1854.42] the size of the of this track so every single variable that is between 24 and 32 it's going to
[1854.42 → 1861.48] be a store in the 32 span, and it's going to take 32 bytes so that's the idea that way you have less
[1861.48 → 1869.28] fragmentation you have a very efficient way of storing and retrieving that variables also you have
[1869.28 → 1877.38] an easy way of reclaiming and freeing that pages in memory so it's its an interesting approach
[1877.38 → 1884.04] and that's the memory locator apart from that you have all these spans then you have for each CPU
[1884.04 → 1889.98] you have a one span, and then you have a centralized version of all the spans of all the CPUs
[1889.98 → 1899.82] and then you have a ship that is managing everything and the other thing is the biggest span is 32
[1899.82 → 1907.04] kilobytes I think so everything that goes over 32 kilobytes is going to be handled directly from the ship
[1907.04 → 1915.86] and it's going to get its own memory pages so huge data chunks are going to be handled
[1915.86 → 1922.82] independently outside spans, and it's going to use pages directly in memory and everything under that
[1922.82 → 1928.74] is going to go in the spans that is going to handle that in pages of memory so then memory allocator
[1928.74 → 1939.44] asks for more pages and free pages from the operating system, so the memory management is done by the
[1939.44 → 1947.14] memory allocator the garbage collector decides what is its use and what is not but the memory itself
[1947.14 → 1952.38] the memory they're asking for memory and free the memory from the operating system is done by the
[1952.38 → 1959.32] memory allocator and I didn't even know that that exists before because I'm a web developer basically so
[1959.32 → 1967.34] so my my my focus has been always in other place yeah i I would like to watch a talk about that I feel
[1967.34 → 1975.48] like I need to hear this one more time yeah i think in the last euro python uh Diana uh
[1975.48 → 1983.00] swinchikko well Diana give a talk yeah from data doc give a talk about that about how they
[1983.00 → 1991.16] knowing how the memory allocator works they were able to squeeze a lot of performance and reduce the
[1991.16 → 1996.44] memory usage and the garbage collector pressure and all that stuff so that it is interesting and
[1996.44 → 2002.72] actually about knowing how the garbage collector works and knowing how a structure packing
[2002.72 → 2011.56] works how how changing the order of the fields of a struct can end up giving you a less
[2011.56 → 2021.38] memory usage for that struct and if that falls into the right spot between spans you can end up saving
[2021.38 → 2027.22] big amounts of memory actually and yeah probably whenever the recording is there check out the
[2027.22 → 2035.36] the talk from Diana is there any action item that or like recommended practice that somebody can take
[2035.36 → 2043.06] from this aha moment yeah I will say that knowing that span size and all that stuff and knowing
[2043.06 → 2049.14] the structure packing can lead you to safe memory and that that is something that I think I would recommend
[2049.14 → 2056.32] to check it out especially if you have a huge amount of instances of something for example in data
[2056.32 → 2063.64] or give obvious that they have a huge amount of events so they have some structure that is repeating
[2063.64 → 2069.90] millions and millions of times so that millions and millions of times if you have is you save I don't
[2069.90 → 2078.42] know 30 bytes on each structure there 30 bytes multiplied by millions of times you are saving memory there
[2078.42 → 2084.52] and you are saving yeah back and forth with a with operating system reclaiming pages and all that stuff so
[2084.52 → 2093.68] i think is something to check out if you have probably in the order of millions of instances of
[2093.68 → 2104.08] of any objects okay still, still trying to think what like I have no it always helps me to kind of
[2104.08 → 2107.90] link this in my mind to something, and it's still like hanging there but okay
[2107.90 → 2116.82] moving on to number 10 and the last one yeah the number 10 it's its kind of related one of the things
[2116.82 → 2123.72] that I always say I always have this oh when the garbage collector runs oh it runs whenever you have
[2123.72 → 2131.00] this memory threshold but can run time to time and without the memory threshold and you can run
[2131.00 → 2138.82] manually but when that runs there can be different places right and what's kind of interesting when
[2138.82 → 2146.76] I just realized that there are three cases only three specific cases where the garbage collector runs
[2146.76 → 2154.90] one it's whenever you call GC well whenever you explicitly call the garbage collector to do a cycle
[2154.90 → 2164.50] so that is um the GC trigger cycle so it's manual calling the garbage collector w's one in this case
[2164.50 → 2172.90] then you have another one that is related to time there is a coroutine that is running under the hood
[2172.90 → 2180.40] every 10 milliseconds in go that is called the system monitor and that system monitor checks if the garbage
[2180.40 → 2186.96] collector hasn't been called for too much time and if that's the case it's going to call the garbage
[2186.96 → 2194.44] collector from there it's what is a GC trigger time that is based on time it's the system monitor
[2194.44 → 2203.94] detects that and sends um and calls a GC garbage collector then you have the one that was more
[2203.94 → 2211.08] interesting for me that is the GC trigger heap that is this one that is related to the go GC environment
[2211.08 → 2218.06] variable that defines when the garbage collector has to pass based on the size of the heap in the
[2218.06 → 2224.38] previous pass so by default is 100 so what it means is whenever you do a garbage collection
[2224.38 → 2231.06] pass you end up with certain amount of memory let's say 16 megabytes for example the next pass is going
[2231.06 → 2238.96] to be whenever you double that whenever you reach 32 megabytes of run is going to trigger a garbage
[2238.96 → 2245.16] collection phase and for example after the garbage collection you get into 20 megabytes so the next
[2245.16 → 2253.18] pass is in 40 that reduce the amount to x and then whenever you reach 2x it's going to call
[2253.18 → 2260.66] again and all that stuff so that is how the GC panel works to do that check of whenever you double the
[2260.66 → 2268.78] memory but when that happened exactly in the code because you are asking for new variables new
[2268.78 → 2275.94] structs and things like that all the time so when are you checking if the is I surpass that memory
[2275.94 → 2283.32] and it's kind of simpler when you understand that the memory allocator is there the trigger heap the
[2283.32 → 2291.42] garbage collection heap check is done whenever you ask for a new page of memory whenever you need a
[2291.42 → 2298.10] new page of memory whenever you request for new memory new block new chunk of memory to store variables in
[2298.10 → 2306.18] any of the spans you are going to check if that is surpassing the threshold and then if it's
[2306.18 → 2312.06] surpassing the threshold it's going to call the garbage collector so that is exactly the exact point
[2312.06 → 2319.20] where he's checking that, so there's a tree these three cases is whenever you reclaim a page from the
[2319.20 → 2327.50] operating system it's when the garbage collector could run if the threshold is surpassed based on time from the
[2327.50 → 2335.32] system monitor and whenever you call it manually so and that's it there's no any other place where
[2335.32 → 2340.26] you are calling the garbage collector what's uh what's a practical takeaway here
[2340.26 → 2351.16] well understanding and there's I think understanding especially the heap one it's going to understand
[2351.16 → 2357.34] better when do you generate pressure in the garbage collector if you for example start
[2357.34 → 2361.52] creating variables and freeing them and creating them and creating them and creating them and creating them
[2361.52 → 2370.16] inside the same kind of size of variables probably you are not going to need to reclaim more pages because
[2370.16 → 2378.84] you probably are reusing the same spam and the same pages that you have in memory so I'm not 100% sure if that is
[2378.84 → 2395.66] 100% accurate so but yeah sounds like if I would want to like not hack but if I want to poke around somebody's code somehow I'm trying to think in an if this is an if you are playing some capture the
[2395.66 → 2403.96] fact, and you got this uh this piece of program, and you try to like to poke it to see where will it break maybe this is something to try there
[2403.96 → 2411.82] not the most everyday practical use case but yeah still trying to link that also into somewhere
[2411.82 → 2420.90] yeah yeah it's kind of its kind of hard for me because as I said i I don't find a lot of practical usage for most of the
[2420.90 → 2428.78] things that i I see here for me, it's about knowledge and about understanding how it works and
[2428.78 → 2436.86] having better understanding on on on things like this it's useful to know when the garbage collector is going to run
[2436.86 → 2445.50] probably in very specific real-time applications you need to know that but probably if you are doing
[2445.50 → 2453.54] real-time applications almost for sure you are not using garbage collected language uh so it's its um
[2453.54 → 2459.44] anyway for that kind of cases whenever you need to know that hey the garbage collector is not going to run
[2459.44 → 2466.76] in this space you can say okay I can run the garbage collector first so I reduce the chance of
[2466.76 → 2476.32] the timer one to running by itself and then I can control the size of the heap to be sure that during that time I'm not
[2476.32 → 2484.56] doubling the heap so I don't know if that is something that I will do or I will want probably I will try to
[2484.56 → 2490.56] disable the garbage collector and enable it again later I don't know if even possible in go
[2490.56 → 2493.12] anyway
[2493.12 → 2499.60] yeah it's its it's tricky and yeah trying to
[2499.60 → 2504.10] poke around with these I don't know how you can
[2504.10 → 2511.64] poke around with this uh it's its um I don't know its lots of arrays until something happens
[2511.64 → 2519.18] yeah no you can for sure you can generate a lot of data and start generating the
[2519.18 → 2525.34] garbage collector to spin and a lot actually you can do things like playing around with
[2525.34 → 2529.82] the concept of hey whenever you double memory I'm going to generate the garbage collector pass
[2529.82 → 2537.04] I can easily double the memory reduce the memory because I free that that thing and double the memory
[2537.04 → 2541.24] again and free that and double the memory again and free that and double the memory again and that
[2541.24 → 2549.48] will be that will generate a lot of garbage collector cycles but you need to play with that and
[2549.48 → 2557.00] yeah you can play with that and screw a bit the performance of the of this thing because
[2557.00 → 2564.36] you are doing a lot of garbage collection work instead of real work okay cool, and probably you can do
[2564.36 → 2570.60] even better just reducing the amount of memory needed for the garbage collector phase you can
[2571.16 → 2579.72] tune the GC the go GC to instead of 100 you put that in 10 and every time the 10 percent is it's
[2579.72 → 2586.20] rich or one percent is rich to run a garbage collection phase and that's going to be crazy spinning the
[2586.20 → 2590.52] garbage collector all the time so not something that I would recommend but
[2590.52 → 2598.12] yeah very nice segue you gave me here for an unpopular opinion, but before we jump there could
[2598.12 → 2603.88] I ask you to recap the two episodes on this and then just quickly go over all the 10 again as a
[2604.60 → 2609.88] it's a very quick summary it's it is really it was fascinating to hear them all yeah I can
[2609.88 → 2615.88] recap of them is a one of them was the slices internals the other one was the go routine cooperation
[2615.88 → 2622.68] the nature the cooperative natures of go routines the other one was the concept of the syntax the
[2622.68 → 2629.48] abstract syntax tree and how that sets the boundaries of all the things that can be there in a
[2629.48 → 2637.64] in a go file the other one was escape analysis plus inclining and how they collaborate to get a better
[2638.44 → 2646.52] memory usage the SSA lowering process that is the process that converts your program representation at
[2646.52 → 2655.32] that point the SSA program representation from machine independent to machine dependent and how tiny go
[2655.32 → 2666.92] leverage that SSA to use the LLVM technology to generate microcontroller binaries using the exact same go
[2666.92 → 2676.84] language and how the compiler and the runtime collaborate together to provide a lot of the syntax that you see in go
[2676.84 → 2684.36] like sending things to channel or appending things to a map the entry point of your binary and how that is not
[2684.36 → 2692.84] the main function it's a more complex than that and the memory allocator and how the memory allocator manage your
[2692.84 → 2698.36] memory and reclaim pages and all that stuff from the operating system and the final one when the garbage
[2698.36 → 2709.16] collector the GC runs and what are the three places where the garbage collector can run and why and I think
[2709.16 → 2718.84] that's it okay I would love to hear from people who listened to the episodes on this topic either on Slack channel of the go time
[2718.84 → 2727.00] podcast or on Twitter what was your mind-blowing one or what was uh or was useful or what was the biggest aha
[2727.00 → 2734.04] for you, it is really cool to go watch all the talks from Jesus they all will be linked in the show notes
[2734.76 → 2742.44] and uh thank you so much for joining do you have an unpopular opinion for today oh that's that's hard
[2742.44 → 2750.68] it took me some time to realize that I had one so no I don't have one for today i I'm going to stick to my
[2751.24 → 2759.08] mechanical keyboards and then dislike many unpopular opinions is that two episodes recorded in the two
[2759.08 → 2769.00] consecutive days are can share one unpopular opinion yeah great then thank you so much for sharing your
[2769.00 → 2774.76] insights and uh good luck in all the cool talks that are coming up for you yeah, thank you for
[2774.76 → 2782.60] having me and yeah it was uh i I had a great time here so thank you and i and I hope i really
[2782.60 → 2789.80] want to know more about people getting this knowledge and finding ways of doing that of using that because
[2789.80 → 2798.36] to be honest as I said I'm a web developer my main focus is on API development, so there are a lot of fields out
[2798.36 → 2807.00] there that are more system level that probably can take advantage of this kind of knowledge but for
[2807.00 → 2814.44] building APIs everything works so smoothly in go that you don't really need to go deeper so it's a
[2815.72 → 2822.84] do share thoughts everybody who listens yep yeah let's see let's see what what people say
[2822.84 → 2828.20] so all right thanks everyone for joining thanks Jesus bye-bye thank you bye
[2828.36 → 2837.08] that is go time for this week thanks for listening along subscribe now if you haven't already headed to
[2837.08 → 2845.08] go time.fm for all the ways or simply search for go time wherever you get your podcasts you'll find us
[2845.08 → 2852.04] hey do you receive our changelog newsletter each Monday if not let's fix that bug one reader calls it so
[2852.04 → 2858.84] good he considers it a competitive advantage sign up for zero dollars at changelog.com
[2858.84 → 2865.96] slash news thanks once again to our partners at fly.io to our mysterious beat freak break master
[2865.96 → 2871.72] cylinder and to our friends at sentry we love sentry you might too use code changelog when you're
[2871.72 → 2878.52] signing up for a team plan and save 100 bucks why not right that is all for now, but we'll talk to you
[2878.52 → 2887.24] again next time on go time
[2887.24 → 2893.24] so
