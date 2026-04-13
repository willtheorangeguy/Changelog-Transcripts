[0.00 → 10.02] Welcome to Practical AI.
[10.44 → 17.50] If you work with artificial intelligence, aspire to, or are curious how AI-related technologies
[17.50 → 20.78] are changing the world, this is the show for you.
[21.46 → 26.34] Thank you to our partners for helping us bring you practical AI each and every week.
[26.34 → 31.32] Fastly.com, fly.io, and typesense.org.
[56.34 → 61.86] On October 26th, at this free online conference, developers and data scientists from around
[61.86 → 66.08] the world will share how they use graph technology for everything from building intelligent apps
[66.08 → 70.44] and APIs to enhancing machine learning and improving data visualizations.
[70.80 → 75.24] There are 90 inspiring talks over 24 hours, so no matter where you're at in the world,
[75.30 → 76.78] you can attend live sessions.
[76.78 → 81.20] To register for this free conference, visit neo4j.com slash nodes.
[81.34 → 86.84] That's N-E-O, the number 4, J.com slash nodes.
[86.84 → 106.46] Welcome to another episode of Practical AI.
[106.80 → 108.40] This is Daniel Whiten ack.
[108.52 → 113.86] I am the founder at Prediction Guard, and I'm joined as always by my co-host, Chris Benson,
[113.86 → 116.70] who is a tech strategist at Lockheed Martin.
[116.84 → 117.94] How are you doing, Chris?
[118.26 → 119.94] I am doing very well today, Daniel.
[120.66 → 123.68] It is fall weather out, and I'm enjoying getting outside.
[124.16 → 124.80] It's fall.
[125.00 → 126.36] It's raining here today.
[126.60 → 128.28] Yeah, it's a little cloudy out, but I'm enjoying.
[128.40 → 129.00] It's nice weather.
[129.58 → 134.24] And so, you know, it's like part of me wants to stay inside and do the fun things, like
[134.24 → 135.96] especially about what we're going to be talking about today.
[136.12 → 136.34] Right.
[136.44 → 138.64] And part of me wants to get outside and enjoy the weather.
[138.82 → 145.58] Well, it's that time of year when you just want to curl up next to a fireplace and burn
[145.58 → 146.38] some firewood.
[146.38 → 147.78] Oh, my gosh.
[147.88 → 149.24] You took us right there.
[149.66 → 150.50] I'll tell you what.
[150.60 → 156.24] Before you say that, I'll just say this is an exciting episode coming up because I think
[156.24 → 160.30] this is a little moment where we're going to talk about our industry maturing a little
[160.30 → 161.76] bit through one effort.
[162.10 → 164.48] And with that said, I'll let you go ahead and do the intro.
[164.48 → 172.54] Well, the connection to burn is because burn is a deep learning framework that's built in
[172.54 → 173.08] Rust.
[173.72 → 178.64] And today we have with us the creator of burn, Nathaniel Samar.
[178.76 → 179.58] Welcome, Nathaniel.
[180.08 → 180.34] Hi.
[180.76 → 181.48] Thanks for having me.
[181.48 → 182.12] Yeah.
[182.12 → 190.72] Well, I admitted to you before the episode that I am basically uninitiated in terms of
[190.72 → 191.60] Rust goes.
[191.98 → 195.90] I've looked at various articles.
[195.90 → 203.02] I think that I've run Rust programs just in a sort of hello world sort of way.
[203.18 → 211.60] Probably my biggest use of Rust has been using Rust in the Python linter called Ruff, which
[211.60 → 212.58] is really great.
[212.58 → 215.12] So that's kind of a circular thing.
[215.34 → 222.36] But for those others out there in our audience that might not be as familiar with Rust as a
[222.36 → 227.68] programming language, could you just tell us a little bit about this sort of like, what
[227.68 → 229.68] is Rust and why Rust?
[230.10 → 236.36] Yeah, Rust is, I think it's falsely being categorized as a low level programming language, probably
[236.36 → 237.88] because of historical reason.
[237.88 → 242.26] But it's very general programming language that can be used for high level stuff.
[242.58 → 243.90] As well as low level stuff.
[244.28 → 249.70] So the main reason to use Rust is maybe when you need to go through multiple abstraction
[249.70 → 253.08] boundaries without having to pay for performance.
[253.64 → 256.00] So yeah, this is how I defined it.
[256.88 → 264.14] And I could be wrong about this, but I think one of the great features, along with Go having
[264.14 → 267.60] a really great mascot, we've got, isn't it a crab?
[267.98 → 271.52] If you see crabs or something for Rust, isn't that a thing?
[271.52 → 274.28] Yeah, I think it's a cute crab.
[274.48 → 275.54] It's a cute crab.
[275.64 → 276.34] That's the mascot.
[276.60 → 276.78] Yeah.
[278.08 → 280.86] I think it's important for programming language to have that.
[281.14 → 281.56] Yes.
[281.90 → 286.30] You have Python or the snake with this programming language.
[286.48 → 288.10] We've got, I don't know what it is for Go.
[288.38 → 289.64] It's the gopher.
[289.82 → 290.70] The go gopher.
[290.96 → 292.18] Yeah, it's quite nice.
[292.40 → 293.04] Yeah, the gopher.
[293.20 → 293.84] It's funny.
[293.98 → 295.02] And you mentioned that.
[295.18 → 298.68] Go is actually how Daniel and I got to know each other.
[298.68 → 301.22] We met in the Go programming language community.
[301.38 → 304.54] And we were kind of the two data-oriented people at the time.
[304.60 → 305.32] This is going way back.
[305.38 → 307.80] There are many, many data-oriented people these days.
[308.00 → 309.64] But got to know each other.
[310.16 → 313.50] After that, I had been hearing about Rust for a while.
[313.50 → 321.08] And I got very interested in it, not only because, as you pointed out, it's a fantastic general-purpose programming language all around.
[321.46 → 329.00] But it also does have a lot of really amazing low-level features and performance capability that attracted me to it.
[329.06 → 333.58] So I'm not nearly as accomplished in the language as you are, Nathaniel.
[333.74 → 338.64] I still love Go, but Rust is now another programming language that I have fallen in love with.
[338.92 → 341.74] Yeah, I think Go is really well-suited for web services.
[341.74 → 344.00] So we've got a lot of tooling around that.
[344.10 → 345.98] It's really pragmatic to use it for that stuff.
[346.50 → 351.28] So yeah, Rust is getting there, but we've got the whole async stories behind that.
[351.82 → 351.90] Yep.
[352.26 → 359.74] And for Rust itself, you mentioned kind of people have this stereotype of Rust as a low-level programming language.
[359.74 → 373.54] But could you give maybe some examples of the types of things either you've built in Rust over time or that are possibilities, just to kind of give people a sense of what people are doing with the language?
[373.68 → 380.28] Obviously, we're going to be talking about deep learning, which is, thanks to you, something that can be done with the language.
[380.28 → 384.96] But what are some of the other things that are out there that people are doing right now with Rust?
[385.42 → 390.46] Well, I think it was first created as a replacement for C++ to write browser engines.
[390.90 → 394.90] So this is maybe why it was known as a low-level programming language.
[395.14 → 397.86] But now I think it's used in game engines.
[398.26 → 400.24] It's also used to do web frontend.
[400.24 → 406.30] So you've got like Letts and Deoxys, which are frontend libraries like React and Vue.
[406.44 → 407.68] So this is pretty high-level.
[408.20 → 418.04] We've got also command-line libraries that you can use, like meta-programming, so that it's very easy to do your command-line arguments, all of that kind of stuff.
[418.38 → 422.28] So yeah, there are tons of things that are built with Rust, high-level and low-level.
[422.56 → 425.08] So you can mix and match by your own applications.
[425.08 → 433.22] Of course, there is like the web services with Tokyo, the Async Front Time, Action, a lot of, if you want to do web services.
[433.66 → 435.70] There is also libraries for that.
[436.30 → 437.98] Yeah, this is a project on top of my mind.
[438.50 → 442.90] It was one of the first languages that really embraced WebAssembly and got it out there.
[443.10 → 449.78] It's interesting, coming, speaking as kind of a novice in the language and coming from most recently Go,
[450.04 → 454.48] there's always this debate on Go versus Rust that you tend to see in articles out there.
[454.48 → 459.66] And I really found room for both of them, and I go back and forth at this point.
[460.08 → 468.50] I will point out, whereas Go is one of those languages that has runtimes, that kind of manages memory, Rust has a really cool feature to it.
[468.56 → 475.78] It's not specific to what we're talking about today, but the compiler ensures that you don't have memory faults, SEG faults,
[476.30 → 480.34] which is something like 70% of all the bugs in software, according to Microsoft.
[480.34 → 486.92] And so it has a fascinating way of approaching ensuring that you can produce bug-free software,
[487.14 → 490.40] or at least much fewer bugs in it, far fewer bugs in it.
[490.76 → 492.00] So it's a pretty cool language.
[492.16 → 496.64] I'm just curious, as we're talking about the language in general, what's your favourite feature?
[496.78 → 501.36] What are some of the things that made you turn to Rust versus some of the other languages you may have worked in?
[501.82 → 504.22] Oh, this is hard to just choose one feature.
[504.64 → 506.24] I think this is the whole package.
[506.24 → 508.72] Said like a real Rust aficionado there.
[508.98 → 514.36] Yeah, but like my favourite feature is not the reason why I started writing in Rust.
[514.70 → 520.70] But now I think my favourite feature is just associated types, because it can abstract data types,
[520.94 → 523.30] like something that is really hard to do with other languages.
[524.08 → 525.00] So, yeah.
[525.36 → 529.56] And could you explain a little bit of like, when might that be useful,
[529.56 → 534.48] or how is that useful in terms of like, when that might come up in your programming?
[534.48 → 539.06] Well, it's when you need to abstract the type you're going to use,
[539.42 → 542.48] but you let the implementation decide the types.
[542.84 → 544.78] Normally, like you have the generics.
[545.08 → 548.48] The generics, you have to, maybe you have a list, and you have to say,
[548.60 → 549.74] okay, I want a list of string.
[550.18 → 552.44] But it's when you use the list that you decide the type.
[552.98 → 558.10] Where associative type is, okay, I've got maybe a list, but I don't know of what.
[558.22 → 561.70] It's the implementation that decides of what's going to be the list.
[561.70 → 563.26] So, sometimes it makes sense.
[563.56 → 566.70] For instance, in Burn, we've got a backend, a backend trait,
[566.96 → 570.20] which we can have multiple implementations, like CPU, GPU.
[570.64 → 574.52] And we have associative types for the memory, for the tensile endpoints,
[574.60 → 577.94] for all of those things that you can manipulate at a high level,
[578.16 → 581.04] but you don't have to know which type it is.
[581.08 → 582.68] It's to the implementation to decide.
[582.68 → 586.90] I'm just going to ask maybe an ignorant question,
[587.16 → 591.26] but I think maybe some people out there might be wondering it.
[591.48 → 600.12] If I'm working in Python, this is a language where I don't have to compile my Python code.
[600.54 → 603.78] Some of the things that we're talking about here with the compiler and other things,
[604.20 → 608.40] a lot of people don't think about, although there's some intersection with that.
[608.40 → 612.58] Could you describe when you're writing a Rust program,
[613.26 → 617.52] what does that look like in terms of, is it a statically typed language?
[617.60 → 619.38] You were talking a little bit about type there.
[619.82 → 621.62] It sounds like you talked about a compiler.
[622.08 → 624.76] So, am I right in that it's a compiled program,
[624.76 → 628.46] and then you can run the binary on some architecture?
[629.00 → 635.26] What is it like to work in Rust as compared to something that people might be very familiar with,
[635.26 → 639.48] like Python, where a lot of people that are probably listening to our episode
[639.48 → 644.36] or have their Google Cola notebook pulled up right next to them, right?
[644.44 → 647.62] And they're doing all sorts of things with a Python interpreter.
[648.18 → 652.26] What is the workflow and programming like in Rust
[652.26 → 655.92] as far as how the language is set up and how you work with it?
[656.30 → 659.20] Obviously, it's a bit different from working in a notebook.
[659.20 → 663.18] Like you said, it's a strongly typed static programming language,
[663.60 → 667.96] similar to like C++, Java, all of this older language.
[668.58 → 670.28] So, for people that comes from Python,
[670.44 → 674.50] maybe you're aware of the Python type INT that you can use.
[674.84 → 677.76] It's a bit like that, but you have to use it everywhere
[677.76 → 679.88] in all of your functions and definitions.
[680.46 → 684.78] And the workflow, something that I like is that in Rust,
[684.92 → 688.08] I think it's one of the few programming language that does that,
[688.08 → 691.66] is that when you write a function, you can just write the test below it.
[691.98 → 695.18] So, that's kind of the way where you can get some feedback
[695.18 → 697.00] on what you're actually writing.
[697.42 → 699.20] And it encourages good practice
[699.20 → 702.34] because you're writing a test that can be reused all the time.
[702.70 → 705.62] It's not a script that you're trying to just run on the side.
[705.72 → 706.84] You can actually commit that.
[707.30 → 709.16] And it describes how the code should run.
[709.40 → 712.46] And that's how you get interactivity with this.
[712.46 → 715.60] And since you have a packet manager, which is Cargo,
[715.86 → 718.94] it's pretty easy to just execute the code you're writing.
[719.26 → 722.30] To follow up on that, Cargo, the package manager,
[722.54 → 725.74] is based on a lot of the best practices we see
[725.74 → 727.28] in some of the other programming languages.
[727.82 → 731.28] For instance, in JavaScript and the Node community,
[731.66 → 732.60] you have NPM.
[733.34 → 734.40] And there are several others.
[734.64 → 738.64] And the Rust community really drew from kind of best practices on that.
[738.64 → 741.70] Another thing to kind of follow up on the compiler notes
[741.70 → 745.60] that Nathaniel was mentioning was a lot of Rust developers
[745.60 → 750.12] kind of see the compiler almost as a pair programming partner,
[750.28 → 752.70] in a sense, to where instead of just hitting compile
[752.70 → 756.16] from time to time like you would in Java or something like that,
[756.50 → 759.74] the compiler is so comprehensive that it kind of helps you.
[759.86 → 761.86] And you kind of use it to write the right code.
[762.00 → 763.52] And you get to the end of the process
[763.52 → 766.68] and know that your code will actually work without runtime errors.
[766.68 → 770.28] So it's a different way of thinking about being a developer.
[770.44 → 773.80] It takes a little bit of a mind shift to adjust over to it.
[774.18 → 775.10] This is very different.
[775.26 → 779.16] Like in Python, an important skill is just to be able to read the stack trace
[779.16 → 781.00] because you're going to have a lot of exceptions
[781.00 → 783.10] when you run your programs
[783.10 → 785.76] and you have to learn how to develop your program.
[785.88 → 789.18] This is kind of a hard skill you have to do when you learn Python.
[789.68 → 793.66] In Rust, it's you have to learn how to write the compiler errors.
[793.66 → 797.70] But they made, at least they tried to make it as easy as possible.
[797.88 → 800.58] Even sometimes you've got links to the documentation.
[801.10 → 802.00] It opens a browser.
[802.20 → 803.60] It can read why you have that error.
[803.96 → 805.16] It explains the reasons why.
[805.56 → 807.80] So this is a different set of skills.
[808.12 → 812.66] And yeah, this is quite different from the workflow you use with Python.
[813.34 → 817.72] Maybe just one more question about Rust in general
[817.72 → 820.10] before we dive into some other things.
[820.10 → 825.76] What is the Rust community like in terms of whether it be,
[826.22 → 830.88] is there active channels where the Rust community communicates with one another,
[831.30 → 832.84] conferences, meetups?
[833.14 → 835.38] What is the Rust community like?
[835.58 → 837.00] And is it growing?
[837.52 → 843.20] How is it changing over time as you've been with the language for some time?
[843.32 → 846.80] How has it developed in the time that you've been part of the community?
[846.80 → 851.44] I'm not sure about all the community, obviously, but I think it's pretty friendly.
[851.96 → 857.06] Like there are some Discord channels where you can just go and ask your questions if you want to.
[857.28 → 859.02] There is an active GitHub issue.
[859.18 → 860.42] So the language is open source.
[860.84 → 864.80] If you have a problem, just open an issue and people maybe are going to help.
[865.16 → 867.40] So this is a pretty inviting community, I think.
[867.58 → 871.40] This is part of the reason why it succeeds, I think.
[871.40 → 877.24] Because if you don't answer questions, you don't help people use your technology, it doesn't really work out.
[877.60 → 881.64] I never went to a conference for Rust yet, but I know there are many.
[881.92 → 884.38] So maybe I'm going to go to some later.
[884.38 → 892.26] You know, one of the topics that has been kind of a recurring topic between Daniel and me over a number of episodes,
[892.26 → 903.76] we've been tracking kind of the maturity process of the AI community and kind of what it takes to kind of level up and to take it to the next level.
[903.76 → 912.18] And on a number of different occasions, we've talked about the fact that if you look at other communities that have arisen before this one,
[912.30 → 914.66] often it takes kind of broad support.
[914.82 → 921.82] Whereas in the kind of the early days, you know, that we're really still in, in my view, of modern AI,
[922.36 → 928.70] it has been largely dominated by a single programming language, which most of our listeners are very aware of, which is Python,
[929.24 → 932.70] which has really been kind of the focus of where all the work is.
[932.70 → 935.76] That's where all the APIs have been focused on and everything.
[936.32 → 944.04] And we've discussed quite a bit about how for AI to mature, it needs to become more broadly available to other languages.
[944.04 → 950.94] And so that as you have different types of use cases addressing, you know, different business needs,
[950.94 → 958.10] and that requires languages other than just Python all the time, how do you get to AI and what kind of bridging do you need to do?
[958.10 → 967.88] It leads me, Nathaniel, as I wanted to ask you is, it's clearly a need that the community has had to be able to start getting Rust and other languages in there.
[968.04 → 970.88] I'm curious, how did you approach this?
[970.98 → 977.78] What was it about trying to get Rust working as a framework that could work with AI tools of the day?
[977.94 → 979.30] How did you get into that?
[979.38 → 980.26] What was your motivation?
[980.86 → 983.08] What did you see as the need at a personal level?
[983.08 → 994.60] Well, I started working on Bird because I was experimenting with asynchronous neural network, and I wanted to make something a bit not standard, let's say that.
[994.84 → 998.48] And I needed like multi-trading, concurrency and stuff like that.
[999.00 → 1001.54] And it was really hard to do with Python.
[1002.08 → 1003.88] And I have a software engineering background.
[1003.88 → 1010.30] So I said to myself, well, if it's hard for me to do that, then maybe it's too hard for any researcher to do that.
[1010.38 → 1013.82] So that's why maybe we don't have yet an architecture for that kind of stuff.
[1014.02 → 1022.60] So I say, well, let me try and make a framework in a language that has support for high-level programming and concurrency and all those things.
[1023.16 → 1025.86] And yeah, it's pretty much the description of Rust.
[1026.10 → 1029.22] So that's why I started writing a framework in this language.
[1029.22 → 1032.60] And then it's just was a personal project for a long time.
[1032.70 → 1034.34] I just was experimenting with it.
[1034.50 → 1037.14] And yeah, it grew with time.
[1037.78 → 1058.60] When you first started thinking about Burn and these problems that you were looking at, what was the current support for doing, whether it be kind of, quote unquote, traditional machine learning, like, you know, random forests, SVM, whatever that is, in all the way up to kind of deep learning.
[1058.60 → 1061.46] In Rust, what was kind of the state of things?
[1061.88 → 1068.98] I'm looking at your burn repo, and I see you've at least been submitting pull requests since July 2022.
[1069.70 → 1072.84] Maybe I'm sure some of it goes back further than that.
[1072.98 → 1078.56] So back to those days, what did the ecosystem look like in terms of its support for these things?
[1079.14 → 1082.34] Well, I don't think there was a lot of deep learning framework in Rust.
[1082.74 → 1088.24] So there were some experiments, but nothing really pragmatic that you can use.
[1088.60 → 1095.50] So I think there was a library for normal, like, SVM random forest in Rust.
[1095.80 → 1096.66] I never used it.
[1097.06 → 1102.74] But yeah, I don't think it's comparable yet to Scikit-learn and PyTorch, which is very complete.
[1102.74 → 1109.38] It's interesting because some of the sort of early stuff that we were doing in Go was similar there.
[1109.46 → 1122.20] There were certain packages like for whether it be kinds of regression or hypothesis testing, statistical things, but not really a robust deep learning framework.
[1122.20 → 1126.16] One of my questions would be in Go.
[1126.36 → 1140.30] I know one of the struggles with trying to support really robust deep learning is not necessarily the fact that you can't create a nice package with a good API.
[1140.30 → 1153.22] But a lot of this sort of specialized libraries and toolkits like CUBA and GPU support make things a little bit more difficult.
[1153.22 → 1165.38] So it might not be that, but what did you see at the time you started working on burn as the big challenges on the Rust side?
[1165.88 → 1173.40] And has that been the case as you develop the package or have other things become the kind of dominant challenges over time?
[1173.40 → 1183.02] Yeah, all of those things are hard to work with, like CUBA, having your own GPU kernels, all the drivers, not necessarily easy to install on other platforms.
[1183.48 → 1188.06] There is a GPU library in Rust that has written kernels.
[1188.38 → 1190.90] This is like GPU, so it's targeting the web.
[1190.90 → 1205.92] But when I started working on burn, I acknowledged that it was pretty important to be generic over the backend so that we can write the best backend for the specific hardware you're actually targeting.
[1205.92 → 1221.58] Because it's probably always going to be faster to write CUBA for NVIDIA, to write like low-level C or Rust maybe with SCMD support for CPU or to write with the metal graphics driver for Mac.
[1221.68 → 1225.64] So I was aware that one backend cannot be written for all of them.
[1226.14 → 1234.90] And I just defined the API and I just used Lip Torch as a backend because there was already bindings to Lip Torch and Rust.
[1234.90 → 1251.20] So this allowed myself to iterate over the abstraction over the user space API and not necessarily worry about speed and writing all the kernels, just getting the abstractions in place and the software architecture in place.
[1251.98 → 1253.64] And it's more pragmatics.
[1253.76 → 1257.32] It's probably like as fast as Lip Torch by default.
[1257.48 → 1262.98] And then I can just go and write more kernels afterwards, which is what we're doing right now.
[1262.98 → 1272.66] I'm curious, do you feel, given the low-level capabilities that Rust brings to bear that so many other languages don't have,
[1273.02 → 1279.38] and that when you're looking at whether it be GPUs over time, and I know you're talking about using Lip Torch in this case,
[1279.38 → 1294.72] but do you think that as you move forward that that low-level capability that you have in this language that other languages don't bring to bear will be a helpful part of kind of developing it and maturing burn over the years ahead?
[1294.90 → 1300.04] Does that low-level give you an advantage that you might not have with other languages that we're trying to integrate in?
[1300.04 → 1304.54] I think so. Mostly in the part where we need to handle memory.
[1305.12 → 1307.46] So that's an important part of deep learning frameworks.
[1307.56 → 1308.76] You don't have to waste memory.
[1309.16 → 1318.40] We can leverage all the type system of Rust to actually do graph optimizations and all of that kind of stuff that we're going to work on soon.
[1318.94 → 1328.10] And I think it's going to be easier to work with Rust to do that with good performance than it will be with maybe another programming language with the garbage collection,
[1328.10 → 1330.52] because it has fine control over the memory.
[1331.14 → 1333.70] So not necessarily to write GPU kernels.
[1333.86 → 1340.78] When you do that, you're actually writing compute shaders, so it's not relevant to Python or C++ or even Rust.
[1340.88 → 1347.18] But if you want to handle memory and write the optimization pipeline, then I think Rust can be really useful.
[1347.18 → 1359.18] And just to get a sense of kind of the current state of burn, what is possible in terms of support and what you can do right now?
[1359.30 → 1367.76] And what are some of the highest requested things that you would like to work on but kind of aren't there yet?
[1368.12 → 1371.34] I don't know. There are so many things that I want to work on.
[1372.24 → 1375.82] Time is just limited, so it's quite hard.
[1375.82 → 1384.26] What I'm really excited to work on is kernel fusion and really optimize the compute pipeline with lazy evaluation.
[1384.58 → 1387.52] So that's something I'm really excited to work on.
[1387.96 → 1393.88] Could you dive into that a little bit and kind of what that might mean for a user specifically?
[1394.38 → 1397.28] Yeah, in terms of user, it's just going to be faster.
[1397.50 → 1402.36] So this is really like optimization techniques that the deep learning framework can use.
[1402.36 → 1411.18] So yeah, there aren't a lot of impacts in terms of user API and usability, but it's just going to be faster.
[1411.18 → 1431.94] Gotcha. And would you say that right now, in terms of what people are doing with the package, now you mentioned that part of what got you into it was building kind of experimental models or architectures that maybe you were experimenting with on the research side.
[1431.94 → 1438.88] So I'm wondering, what are you seeing as the people that are using it?
[1439.38 → 1442.72] What are they most doing with the package?
[1442.84 → 1446.94] Is it that sort of experimental research implementation side?
[1447.18 → 1456.10] Is it taking models that aren't maybe experimental and embedding them in, you know, Rust applications where they wouldn't have been able to before?
[1456.18 → 1457.06] Is it something else?
[1457.18 → 1460.32] What are you seeing in terms of what people are doing over and over again?
[1460.32 → 1467.02] I think a lot of people are using it because it's easy to deploy on any platform because we have different backends.
[1467.14 → 1472.98] So you can deploy on WebAssembly, you can deploy on even a device without operating systems.
[1473.24 → 1476.94] So this is pretty great in terms of deployment flexibility.
[1477.70 → 1486.68] But even though I started the framework because I had like a research idea I wanted to do, the goal of Burn isn't necessarily to be only for research.
[1486.68 → 1493.46] I wanted to go with kind of blank sheet and thinking about all the constraints and who is going to use the framework.
[1493.78 → 1501.52] So I'm always thinking about the machine learning engineer perspective, the researcher's perspective, and then the back-end engineer's perspective.
[1501.52 → 1507.70] So the one that is going to write the actual low-level kernel code and CUBA kernels and stuff.
[1507.70 → 1513.28] So there are kind of different user profiles or use cases that you can assign to the framework.
[1513.52 → 1513.66] Yeah.
[1513.78 → 1519.40] Kind of as a follow-up to that, as you were looking, and I noticed that you had quite a few people that were making contributions.
[1519.80 → 1526.28] For being a relatively young project overall, you have a lot of people involved in it.
[1526.34 → 1528.48] So, I mean, it looks like it's really getting a lot of traction.
[1528.48 → 1537.58] How do you kind of organize the workaround it and kind of satisfy the interests of each of those personas along the way?
[1537.80 → 1543.38] You know, is there one that tends to lead or do you tend to try to have certain people that do different ones?
[1543.50 → 1544.50] How do you approach that?
[1545.24 → 1546.32] To be honest, I'm not sure.
[1546.54 → 1548.76] I think the key is just to be reactive.
[1549.16 → 1551.70] So if there is an issue, just go and comment it.
[1551.80 → 1553.70] If there is a bug, try and go fix it.
[1553.70 → 1560.66] And I think the most important work I can do is in terms of architecture, like setting the stones in place.
[1560.78 → 1570.16] But then if I want to extend, maybe add more tensor operations or if I want to add more neural network modules, then I can open issues.
[1570.58 → 1575.78] And people that are interested can just assign themselves and actually do a pull request.
[1576.22 → 1579.10] And I just have to be really conscious about that.
[1579.50 → 1580.72] Do code review correctly.
[1581.24 → 1581.86] Be kind.
[1581.86 → 1584.02] And I think that's pretty much it.
[1584.08 → 1585.46] I don't have any other secret.
[1586.70 → 1591.62] So Nathaniel, I've deployed a lot of models as part of my day job.
[1591.62 → 1608.62] Let's say that I am interested in Rust, and I am interested to maybe take some model that I might have experimented a little bit with in a collab notebook or something like that.
[1608.62 → 1617.12] And I want to make it like you said, have the support for multiple backends implemented in a maybe more efficient application.
[1618.08 → 1630.88] What would be the process that someone would have to do to, let's say, get one of the kind of popular quote unquote models these days up and running in Rust using Burn?
[1630.88 → 1633.14] Is that something that's possible right now?
[1633.34 → 1636.06] How are people kind of pushing the edges with respect to that?
[1636.06 → 1638.38] Well, I think there are two different strategies.
[1638.68 → 1643.92] So we're actually working on being able to import Onyx model.
[1644.16 → 1650.72] So if you have maybe an image classification models, then maybe our import is going to work.
[1650.82 → 1651.56] It's still in WIP.
[1651.56 → 1654.20] But if there is no crash, it's going to work.
[1654.28 → 1655.56] Not all operations are supported.
[1656.18 → 1667.04] But maybe for other models, you maybe need to write the model from scratch using our framework and then translate the weights, and you would be fine to deploy it.
[1667.38 → 1668.38] So it's a bit of work.
[1668.52 → 1671.50] But working it with Burn is quite intuitive.
[1671.50 → 1676.24] So the API is similar to PyTorch, the modelling API at least.
[1676.66 → 1682.66] So it's not that hard depending on obviously the size of the model and the complexity of the model.
[1683.18 → 1683.30] Yeah.
[1683.44 → 1689.12] And I think I saw a few on the repo that people have already sort of done this.
[1689.26 → 1693.72] What are some examples of some of these that people have brought over into Burn?
[1694.14 → 1700.00] Yeah, I think there are community models for LAMA, for Stable Diffusion, for Whisper.
[1700.00 → 1702.18] This is thanks to the community.
[1702.34 → 1704.04] I didn't actually port those models.
[1704.62 → 1712.18] But yeah, since it's open source, I think if you actually do the work to port maybe a model, I think it's great to share it with the community.
[1712.42 → 1713.62] People can start using it.
[1714.12 → 1716.84] So yeah, we have a few, but we would like more.
[1717.44 → 1717.90] Yeah.
[1718.02 → 1722.34] So call out to the listeners out there that are Rust people in the audience.
[1722.60 → 1726.46] Check it out and submit some of your own model implementations.
[1726.96 → 1729.50] That's a great way to contribute, I'm sure.
[1730.00 → 1735.14] You mentioned it having a similar API to PyTorch.
[1735.64 → 1738.92] And I'm kind of looking through some of the documentation here.
[1739.02 → 1748.66] I'm wondering if you could just comment on a few of the things that you call out as far as features of Burn and kind of explain what you mean by some of those things.
[1748.66 → 1754.72] I think we already talked a little bit about the customizable, intuitive, user-friendly neural network modules.
[1754.88 → 1758.08] So this kind of familiarity with maybe a PyTorch API.
[1758.26 → 1759.38] Maybe there's more to that.
[1759.84 → 1766.52] But you also mentioned this comprehensive training tools, including metrics, logging, check pointing.
[1766.52 → 1781.88] Could you describe that a little bit in terms of what the thought process is in the framework around these things, which are definitely important practically, as you said, for the machine learning engineer, for the actual practical person who's trying to build models?
[1781.88 → 1783.46] Yeah, and even the researchers.
[1783.68 → 1786.52] Sometimes they don't want to actually write all the training loops.
[1786.76 → 1789.04] That's not the core of their research.
[1789.60 → 1797.62] Yeah, there is a library, which is called Burn Train, which tries to bring a training loop to the user so they don't have to write it.
[1797.62 → 1803.40] So you've got like a basic CLI dashboard where you can follow all your metrics.
[1803.98 → 1804.98] You have your logging.
[1805.40 → 1811.74] So if you want to maybe synchronize the drive to maybe a Google account, you can probably do that.
[1811.90 → 1814.20] So it's similar really to PyTorch Lightning.
[1814.60 → 1820.38] So for the PyTorch users that are familiar with the projects, but we also have that for Burn, and we just have that.
[1820.90 → 1823.32] It's just easier to get started with the framework.
[1823.32 → 1827.36] I think it's essential for now, if you're starting a new framework, to provide that.
[1827.88 → 1831.96] We already talked a little bit about the versatile backends.
[1832.24 → 1835.56] I don't know if you want to say any more about the other options for that.
[1835.64 → 1840.38] You mentioned Torch and WebGPU, but I see a couple others here mentioned.
[1840.54 → 1848.36] Are there any callouts that you'd like to make there, both in terms of other options, but when also those other options might be useful?
[1848.36 → 1855.64] People might not realize in the audience when you would want to use a Torch backend versus something else.
[1855.64 → 1860.26] Yeah, I think the Torch backend is probably the fastest if you have an NVIDIA GPU.
[1860.52 → 1866.64] For the CPU, I'm not sure if it depends on the model, but we also have an NDA ray backend.
[1866.92 → 1870.68] So NDA ray is similar to NumPy or Rust.
[1871.18 → 1875.02] This is maybe the fastest backend, but this is extremely portable.
[1875.02 → 1877.16] So you can deploy the backend everywhere.
[1877.16 → 1883.62] So if you've got the small model, it can be very handy to have that or to write unit tests and stuff like that.
[1883.62 → 1885.84] We also have a Kindle backend.
[1886.12 → 1890.98] So Kindle, it's also a new framework built by Hugging face in Rust.
[1891.46 → 1895.18] So they're trying to make it easier to deploy model with that.
[1895.50 → 1900.76] So we actually have their framework as a backend for burn so we can benefit from their work.
[1901.30 → 1904.04] And yeah, we have the WebGPU backend as well.
[1904.18 → 1906.58] So we can target any GPU.
[1906.88 → 1908.82] So if you don't have NVIDIA, don't be sorry.
[1908.96 → 1910.06] We have you covered.
[1910.06 → 1910.74] Awesome.
[1911.36 → 1919.52] So I also noticed on your GitHub repo, in addition to kind of the familiarizing us with kind of the capabilities and features,
[1919.76 → 1926.76] you also have the burn book, which I assume was maybe inspired by the Rust book.
[1926.84 → 1928.46] That seems to be a common thing.
[1928.90 → 1931.66] What is the burn book, and how can we best use it?
[1931.72 → 1932.74] What's it for in your mind?
[1933.22 → 1936.84] Yeah, the burn book is to help people getting started with the framework.
[1936.84 → 1943.52] So it's like a big tutorial slash reference that you can use to actually start using burn.
[1943.80 → 1948.06] At the beginning, it tells how to install Rust, how to get started with the language,
[1948.44 → 1954.02] how to make a basic models, the training loop, the data, the data pipeline, all of that.
[1954.12 → 1957.22] So it's just with all the explanations and stuff like that.
[1957.34 → 1961.92] So it's really to help people getting started with the framework easily.
[1961.92 → 1968.08] Of the people that are coming through and learning from the burn book, interacting with you on the repo,
[1968.82 → 1979.16] do you see a lot of people coming from the non-Rust community in because they have either performance-related things
[1979.16 → 1985.00] or maybe their company is exploring deploying things in Rust or other people, that sort of thing.
[1985.00 → 1995.48] So people coming from maybe the Python community, or do you see more people kind of Rust engineers who are already building things in Rust?
[1995.62 → 2003.24] And so now that everybody wants to integrate AI into their applications, you sort of have the influx from that way.
[2003.32 → 2004.62] Are you seeing both?
[2004.78 → 2007.82] Which side is kind of coming your direction more?
[2007.82 → 2018.88] I'm not sure necessarily about the backend of users of Bird, but I think the main pain point is that they want to deploy their model reliably,
[2019.10 → 2021.42] and they're coming to Bird to do that.
[2021.76 → 2027.80] And some of them, once they get familiar with the framework, they actually port also the training part.
[2027.92 → 2031.70] So they can have all of their machine learning workflow working with Bird.
[2031.70 → 2040.08] So it can be people with Python background or Rust engineer, I'm not sure, but I think this is the main traction point.
[2040.70 → 2044.58] I will offer kind of a burn newbie perspective on that myself.
[2044.78 → 2054.64] When I ran across burn and reached out to you, I was really excited about it, in part because as this industry is maturing and affecting,
[2054.64 → 2066.38] as many other vertical industries out there, we are seeing AI capability being pushed out from only being in data centres and stuff out onto the edge.
[2066.86 → 2069.38] And you can define the edge in many, many ways, obviously.
[2069.92 → 2076.08] But the place where processing is happening and even training is happening is evolving over time.
[2076.08 → 2086.04] And if you look at businesses and their other use cases, the fact that they need AI in all these other industry things that they're doing,
[2086.12 → 2092.98] all these other businesses, they may be platforms that are mobile, such as we have autonomous cars out these days,
[2093.14 → 2097.68] and you name it, all sorts of stuff that are increasingly relying on AI.
[2097.68 → 2105.88] And they're turning, because those are autonomous things, they need the performance, in many cases, the safety and low-level performance capability that Rust offers.
[2106.34 → 2111.76] I know that I got super excited when I came across burn because I'm in this AI world,
[2111.84 → 2117.88] but I'm also in this high-performance, things-moving-around-time-and-space world as well.
[2118.00 → 2124.36] And being able to combine those into one, have one language that is able to do both at the same time
[2124.36 → 2129.98] and deploy out to the edge in a very safe way and highly performant way was hugely exciting.
[2130.12 → 2133.90] And it's been a point of conversation that I've had with colleagues for quite some time.
[2134.22 → 2141.14] So I think you've hit a sweet spot with burn that is going to get, probably as people become aware of it,
[2141.22 → 2148.98] you'll get a lot more uptake because it solves what would otherwise be a big problem that they're going to be faced with in the years ahead.
[2148.98 → 2156.94] Yeah, and I think it's not just about, like, there is a good amount of solutions to just deploy inference model,
[2157.08 → 2162.40] like with Onyx and stuff like that, but it's not going to cover the training part.
[2162.82 → 2165.94] And I think it's valuable to be able to do training everywhere.
[2166.42 → 2170.36] Like, maybe the next generation of model, you're going to call backward during inference.
[2170.56 → 2171.26] We don't know that.
[2171.64 → 2175.26] It's cool to have, like, one tool that you can do both on any platform.
[2175.26 → 2186.30] As you kind of look to the future of the project itself, I maybe have kind of two elements to this question.
[2186.80 → 2198.82] What are some of your hopes for what burn becomes into the future as a framework in terms of, like, the sweet spot and what it does really well, what people turn to it for?
[2198.96 → 2202.40] So what is your kind of hope and vision for the project, I guess?
[2202.40 → 2211.86] And then for yourself, in terms of your own work and how you're using the project or other things, what is your hope for the future?
[2212.26 → 2217.46] You have your own interests, obviously, in terms of developing AI-related applications.
[2217.46 → 2220.76] So I'd love to hear both of those things if you have a comment on them.
[2221.26 → 2226.40] I think I would like burn to be widely used for maybe complex model.
[2226.66 → 2229.58] I think rust really shines when you've got complexity.
[2229.58 → 2239.54] So if you've got a convolutional neural network with just a few layers, maybe the benefits of using rust isn't as massive, maybe for deployment.
[2240.14 → 2247.88] But if you've got, like, big models and a lot of complexity in the building blocks, then I think burn will shine in that place.
[2247.88 → 2264.16] So I would like to see, like, innovative new deep learning application being built with it, as well as maybe just normal deep learning models that we're familiar with, like Reset, Transformers, all of those, but deploy on any hardware.
[2264.16 → 2270.92] So that everybody can run maybe locally some models, maybe not the big ones, but at least the smaller ones.
[2271.56 → 2283.48] And what I would like to do with it is maybe more research, like I said previously, on maybe bigger models, maybe asynchronous neural network, like try to leverage the culture and nature of the framework.
[2283.48 → 2283.80] Yeah.
[2283.80 → 2297.72] And as we kind of get close to an end here, just for those, because it is a podcast, people are listening in their car and maybe taking mental notes of some things or on their run.
[2298.12 → 2301.96] Where do people go to find out more about burn?
[2302.22 → 2306.76] And what would you suggest, let's say it's a newbie to burn.
[2306.98 → 2311.40] What should they do to get familiar with it and try things out?
[2311.40 → 2314.64] So where do they go, and what would you suggest they start with?
[2315.20 → 2318.22] I think the best place to start is to go to the website.
[2318.52 → 2320.98] So it's just burned.dev, pretty simple.
[2321.58 → 2326.78] And from there, you can just go in the book that we spoke about and just follow along.
[2327.10 → 2333.20] If you are not familiar with Rust, we're going to provide links so that you can get familiar with the language.
[2333.58 → 2337.60] And then you can come back afterwards, follow the rest of the book.
[2337.60 → 2343.22] And if you're interested, you can also go to the GitHub, try the examples.
[2343.60 → 2345.50] You can run them with one command line.
[2345.64 → 2351.48] So you can try to do end friends or to even launch a training on your own laptop.
[2351.48 → 2352.64] So that can be great.
[2353.10 → 2355.76] So yeah, that would be the place I would go to start.
[2356.28 → 2356.76] Awesome.
[2357.04 → 2362.32] Well, thank you so much for taking time to join us and not burn us.
[2362.40 → 2363.22] You are very kind.
[2363.22 → 2365.22] So thank you.
[2365.26 → 2366.80] Thank you for your time.
[2366.96 → 2377.84] We're really excited about what you're doing and hope to have you on the show maybe next year or sometime to see all the exciting things that are happening in deep learning and Rust and Burn.
[2378.00 → 2379.26] So thanks much, Nathaniel.
[2379.42 → 2380.12] Thanks a lot, man.
[2380.32 → 2381.28] Thanks to you for having me.
[2381.28 → 2394.10] If you enjoy the music you hear on Practical AI, you'll be happy to know we've released two full-length albums for purchase or streaming.
[2394.46 → 2398.60] Just search for Changelog Beats in your music app of choice and check them out.
[2399.08 → 2404.48] Volume zero is called Theme Songs, and it includes special remixes in addition to the classics.
[2404.48 → 2411.98] And our first volume is called Next Level, featuring many of the video game-inspired tracks you've heard on Changelog Podcasts over the years.
[2412.38 → 2413.84] Check us out, Changelog Beats.
[2414.30 → 2419.72] Thanks once again to our partners, Fastly.com, Fly.io, and Typesense.org.
[2420.10 → 2425.00] That's all for now, but we'll be back with more Practical AI Goodness next week.
[2425.00 → 2425.62] Brilliant.
[2425.62 → 2455.60] Thank you.
