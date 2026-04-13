[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.14] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to Linode.com slash Changelog.
[15.28 → 18.12] This episode is brought to you by Rollbar.
[18.42 → 24.36] Rollbar is real-time error monitoring, alerting, and analytics that helps you resolve production errors in minutes.
[24.68 → 28.60] And I talk with Paul Bigger, the founder of CircleCI, a trusted customer of Rollbar.
[28.60 → 32.94] And Paul says they don't deploy a service without installing Rollbar first.
[33.32 → 34.58] It's that crucial to them.
[34.78 → 36.60] We operate at serious scale.
[37.04 → 42.46] And literally the first thing we do when we create a new service is we install Rollbar in it.
[42.64 → 45.52] We need to have that visibility.
[45.94 → 50.44] And without that visibility, it would be impossible to run at the scale we do.
[50.58 → 52.54] And certainly with the number of people that we have.
[52.72 → 55.70] We're a relatively small team operating a major service.
[55.70 → 61.46] And without the visibility that Rollbar gives us into our exceptions, it just wouldn't be possible.
[61.84 → 62.00] All right.
[62.02 → 66.70] If you want to follow in Paul's footsteps and start deploying with confidence today, head to Rollbar.com slash Changelog.
[67.36 → 70.34] Once again, Rollbar.com slash Changelog.
[70.34 → 81.74] Welcome to JS Party, a weekly celebration of JavaScript and the web.
[81.90 → 88.38] Tune in live on Thursdays at 1 p.m. Eastern, 10 a.m. Pacific at changelog.com slash live.
[88.38 → 93.48] Join the community and Slack with us in real time during the show at changelog.com slash community.
[93.88 → 94.66] Follow us on Twitter.
[94.76 → 96.28] We're at JSPartyFM.
[96.52 → 97.76] And now on to the show.
[97.76 → 102.16] All right.
[102.28 → 102.80] Hello.
[102.96 → 106.22] This is K-Ball here reporting live from React Amsterdam.
[106.48 → 115.72] In Amsterdam, I am here with Florian Rival, who is a software engineer at Facebook and has developed an open source gaming engine using React and WebAssembly.
[115.90 → 116.24] Florian.
[116.58 → 116.78] Hi.
[116.88 → 117.38] Hi, everyone.
[117.72 → 118.74] Very nice to be there.
[119.06 → 119.26] Yeah.
[119.32 → 120.16] Thank you for joining me.
[120.24 → 122.56] So I'm really excited to hear more about the game engine.
[122.66 → 124.80] But first, so you're speaking a little later today.
[125.10 → 125.42] Yes.
[125.42 → 128.04] Can you give us a little bit about what your talk is going to be?
[128.24 → 128.58] Yeah, yeah.
[128.58 → 128.78] Sure.
[128.94 → 138.54] So the idea is that my talk is about using React and WebAssembly to create applications that are going a bit beyond what we used to do.
[138.54 → 145.34] So the idea is that I had this game engine that you just mentioned called Develop.
[145.84 → 153.04] And it was a whole C++ game engine, a desktop application that you can use on Windows, Microsoft, Linux.
[153.04 → 164.88] And I was like, okay, maybe I could port it to the browsers and have a kind of refreshed version because I've been using React for quite a bit of time.
[164.96 → 167.86] And I was like, React is really a good way of making interface.
[168.20 → 171.94] So is there a way I can remake the software in a better way using React?
[171.94 → 181.64] And that's how I happened to use WebAssembly to, in fact, port most of the software from C++ to WebAssembly.
[182.76 → 195.18] So my talk is basically about this and what were the challenges using WebAssembly and what are the things that we can use in the React ecosystem to make ambitious applications like a game editor.
[195.18 → 200.04] So is the core engine still written in C++, but you're now compiling it to WebAssembly?
[200.26 → 205.90] So yes, there are the core classes of the software that describe what a game is.
[206.04 → 210.60] So the objects that are in a game and the rules that define the game.
[211.02 → 219.14] So the interesting thing about the software is that people can create their own game without programming because they are able to create the rules of their game using visual events.
[219.52 → 221.34] It's a bit visual programming in a way.
[221.34 → 228.82] And all of this is still in C++ because there are kinds of lots of business logic that I didn't want to rewrite.
[229.18 → 235.34] All the tooling to convert your game from this structure in memory to a real game.
[235.68 → 237.72] At the end, games are running in JavaScript, actually.
[237.92 → 240.24] HTML5, WebGL, and JavaScript.
[241.06 → 247.12] And then, so the idea was, can I take all this logic in C++ and convert it to WebAssembly?
[247.12 → 255.12] And that's what I did using a project called scripted, which is a Mozilla-backed project.
[255.88 → 259.68] Well, at the beginning, it was powered by guys at Mozilla.
[260.56 → 261.50] I think it's still the case.
[261.96 → 263.24] Or maybe that has changed.
[263.66 → 269.22] Anyway, that's a really nice project that is basically a compiler, a C++ to JavaScript compiler.
[269.46 → 273.38] And now a compiler that is a C++ to WebAssembly.
[273.38 → 273.88] That's neat.
[274.36 → 275.06] That's neat.
[275.20 → 277.46] So, can you give me the spoiler?
[277.70 → 279.56] What did you have to change to get that to work?
[279.94 → 280.66] So, yeah.
[281.50 → 293.32] The interface that was the user interface of the software at the beginning was all done in C++ using a cross-platform toolkit called WE Widgets.
[294.20 → 299.14] So, there are also cross-platform toolkits like this in C++, for example, Out.
[299.14 → 305.42] My idea was, can I remove this interface, this user interface from the code base?
[305.72 → 312.30] So, I had to dig a bit in the C++ code to basically remove all the classes that were defining the interface,
[312.48 → 318.36] just to keep the core classes, the business logic describing what a game is and all the surrounding tooling.
[318.36 → 323.78] And once you have it, you are then able to run scripted, the compiler.
[324.20 → 332.78] But instead of, at the end, having an executable that you can run on your machine, you can run it as a WebAssembly module.
[333.46 → 334.62] That makes a lot of sense.
[334.78 → 340.00] So, essentially, you are taking that UI that you want to replace with a React application and saying,
[340.10 → 345.20] okay, let's get rid of that and let's bundle this thing up so now I just plug it into my JavaScript and go?
[345.20 → 348.44] Yes. That's the theory.
[348.90 → 351.88] In practice, there are a few things that you have to know, of course.
[352.30 → 356.64] So, once you have your world code base that is converted to WebAssembly, well, that's a very good start.
[356.92 → 361.34] You can actually see in the browser a few, for example, when you log things in the console,
[361.74 → 364.78] it's actually redirected to the console in Chrome.
[364.92 → 366.36] So, you can see that things are running.
[366.66 → 368.24] So, it's a very good first step.
[368.52 → 373.08] You can use scripted like I did, but if you want to write WebAssembly from scratch,
[373.08 → 379.64] you can use things like language like Rust or this interesting project called Assembly Script,
[380.08 → 384.26] which is basically a kind of type script that compiled to WebAssembly.
[384.70 → 388.84] So, it's very interesting and, I mean, there are multiple ways of writing WebAssembly.
[389.10 → 393.30] In my case, I had an already existing code base, so I wanted to reuse it.
[394.06 → 396.74] So, yeah, that's the first part.
[396.74 → 401.76] And then the other part is how to use it in JavaScript without creating too much memory leaks
[401.76 → 407.00] or this kind of things that we use to bother in the whole native language
[407.00 → 409.44] and that we kind of forget in JavaScript.
[409.86 → 410.50] That's cool.
[410.58 → 414.20] Yeah, I think this is actually a fascinating area for WebAssembly
[414.20 → 420.20] of taking these existing engines that are out there that have targeted other platforms
[420.20 → 424.62] and saying, guess what, now we can target them to the web and just plug into it
[424.62 → 427.32] the same way we would any sort of JavaScript module.
[428.02 → 431.60] Were there any major gotchas along the way?
[432.32 → 437.88] So, I would say that the first thing that you will see is that the bundle that is created,
[438.10 → 439.94] the WebAssembly module, is quite large.
[440.48 → 443.88] Depends on your code base, of course, but even for something that is quite small,
[444.14 → 446.46] if your code is, for example, coming from C++,
[446.46 → 448.94] you have the standard library that is coming along.
[449.24 → 450.68] So, it waits a lot.
[450.98 → 453.60] Well, for example, for Develop, it's three megabytes,
[454.12 → 456.60] the bundle containing all the WebAssembly code.
[457.28 → 460.56] Honestly, I don't care because I'm making an application,
[460.96 → 464.72] so I'm willing to have people wait a bit while they're downloading it.
[464.94 → 467.72] It would be better if it was linear, but it's okay.
[467.86 → 470.36] It's maybe something that will be improved,
[470.36 → 478.18] and it's already better because the first version of my port to browser of my app
[478.18 → 483.12] was using ASM.js, which is a kind of subset of JavaScript
[483.12 → 485.30] that Script used to compile to,
[485.82 → 488.20] and it was seven megabytes, maybe.
[488.76 → 490.26] So, things are progressing.
[490.70 → 490.80] Yeah.
[491.18 → 493.66] Well, and WebAssembly megabytes are cheaper in some ways.
[493.78 → 496.70] They're the same amount over the wire, but parsing cost goes way down.
[496.70 → 501.14] Yeah, yeah, and I think, again, it depends on what you're making.
[501.42 → 504.46] If you're making a complex game or app,
[504.90 → 508.22] it might be okay to ask the user to download this bundle.
[508.66 → 512.06] And also, as I'm packaging the application as an electronic application,
[512.58 → 515.26] three megabytes, more or less, that's okay.
[516.54 → 518.18] So, yeah, that's the first goal chart.
[518.30 → 520.84] The other will be more in using the classes,
[521.24 → 523.90] the bindings to your original classes in JavaScript,
[523.90 → 526.56] where there are a few things like memory leaks
[526.56 → 530.28] or passing the proper type of parameters that are really important.
[530.68 → 532.02] You raise a fascinating point.
[532.12 → 533.42] A lot of times we think about WebAssembly,
[533.58 → 535.66] oh, I'm going to run it on the browser, and it's going to be there,
[535.76 → 537.70] but part of this for you, it sounds like,
[537.76 → 540.00] was just you wanted to use React for your UI,
[540.20 → 541.80] even if you're shipping it in Electron.
[542.20 → 542.56] Yes.
[542.70 → 545.54] Being able to have that seamless integration.
[546.16 → 546.42] Yes.
[546.42 → 549.84] So, actually, my starting point wasn't really about,
[549.98 → 551.04] oh, I want to use WebAssembly.
[551.28 → 554.32] It was about, I have this existing application
[554.32 → 558.88] and I know that I can make a better new interface using React,
[559.34 → 563.32] but how can I interface React with my existing code base?
[563.48 → 565.64] I don't want to rewrite the whole application in JavaScript.
[566.04 → 569.36] It will be too long, and I will lose the backward compatibility.
[569.76 → 570.86] So, existing users will be like,
[570.94 → 574.06] oh, your new software has less feature
[574.06 → 576.08] and it's not working with our existing games.
[576.26 → 578.64] So, no, no, it would have been a foolish idea.
[579.06 → 581.08] But still, I was really interested in React
[581.08 → 583.28] because I've been using React Native for making applications
[583.28 → 588.34] and React for making websites or kind of applications on the web.
[588.68 → 593.32] And I was like, we can do things that are really, really impressive with React.
[593.42 → 597.02] So, let's try to port the whole interface to React and see how it goes.
[597.26 → 600.56] It's interesting to think about this because React Native,
[600.82 → 603.14] as you kind of bring up, is sort of trying to do a similar thing.
[603.14 → 607.48] Let's use the React abstractions and ideas for native programming.
[608.06 → 612.96] Here, we're taking something that wasn't originally planned for mobile
[612.96 → 615.76] or anything like that at all and saying, you know what?
[615.76 → 616.34] It doesn't matter.
[616.52 → 618.22] We don't have to build it from scratch with this.
[618.40 → 620.66] We can just take out the UI component.
[621.60 → 622.20] Yeah, yeah, yeah.
[622.38 → 626.88] I think that's React, the approach of React Native,
[627.88 → 631.52] with the approach of React but binding to native components.
[631.52 → 633.40] Here, I'm doing a bit the reverse.
[633.58 → 638.48] I'm staying with React.js because I'm primarily targeting desktop users.
[639.06 → 644.00] So, it's fine to run React.js and the performance is correct.
[644.40 → 647.10] But I'm still binding to existing native code
[647.10 → 650.48] that I don't want to rewrite, and I want to reuse.
[650.90 → 653.36] So, in my case, I'm reusing an existing code base that I did.
[653.62 → 655.14] But you could do the same with, for example,
[655.62 → 657.52] existing libraries that are doing computation,
[657.52 → 659.68] like, I don't know, physics engine.
[660.34 → 662.70] I know that some have been compiled to WebAssembly.
[663.34 → 665.30] Code base of game engine, of course,
[665.38 → 667.96] but also things like maybe physics simulation.
[668.52 → 671.24] I think that we'll see more and more people reusing
[671.24 → 674.32] or using WebAssembly module inside application
[674.32 → 676.72] without even seeing it.
[677.48 → 677.66] Yeah.
[677.86 → 679.58] Well, and the cool thing about your approach
[679.58 → 681.70] is it's not limited to React, right?
[681.70 → 683.98] If you're a Vue user, if you're an Angular user,
[684.14 → 685.16] if you're an Ember user,
[685.32 → 687.58] if you're using any of these JavaScript frameworks,
[687.96 → 690.06] but you still want to package up a bunch of native stuff,
[690.20 → 693.60] now you don't need to wait for Vue native or what have you.
[693.68 → 696.52] You just package WebAssembly and go.
[696.92 → 697.34] Yeah, yeah.
[698.80 → 702.14] Actually, in my talk, I'm speaking about WebAssembly
[702.14 → 706.62] for the first part and then moving to more React-related stuff.
[706.84 → 708.40] But actually, it could be another framework.
[708.40 → 712.08] The cool thing with React is that it has a really huge ecosystem.
[712.88 → 714.28] And the second part of my talk,
[714.36 → 717.34] I more or less explain all the packages
[717.34 → 720.88] and open source modules that I've been using in React
[720.88 → 723.92] to make an interface that looks like a native interface
[723.92 → 727.52] with, for example, a list of hundreds or thousands of elements
[727.52 → 728.64] that you can virtualize
[728.64 → 732.02] and things like if there are performance issues,
[732.14 → 733.10] how to deal with them
[733.10 → 736.28] and other things like displaying trees of nodes.
[736.28 → 739.44] For example, in my software, the events that are describing
[739.44 → 742.02] the rules of the game, it's basically a tree
[742.02 → 743.80] that is displayed on screen.
[744.00 → 747.78] So how to do it properly with the DOM elements and React.
[748.30 → 750.56] But all those things could be applied to another framework.
[751.10 → 752.64] Yeah, that makes a ton of sense.
[753.22 → 756.16] Were there any things that you found were missing
[756.16 → 757.90] coming into WebAssembly?
[758.02 → 761.54] Like I know, for example, the WebAssembly team is making a big push
[761.54 → 764.88] or the WebAssembly coalition, I guess, is making a big push towards
[764.88 → 768.90] being able to do multi-threading and scripting across that.
[768.98 → 772.64] Was that something that proved to be a problem, not having those features?
[773.12 → 775.16] So for me, it was okay because actually,
[775.58 → 779.18] I don't have any performance requirement on WebAssembly
[779.18 → 782.10] because all the WebAssembly code that is running is,
[782.38 → 785.54] as I said, some business logic that can,
[785.76 → 787.10] it's not running the games.
[787.22 → 789.90] Games are actually in JavaScript at the end.
[789.90 → 792.70] But yeah, I think that the most,
[793.18 → 796.54] the thing that I had the most problem with was debugging,
[796.78 → 800.78] especially when, imagine that you're calling a function in WebAssembly.
[801.26 → 804.78] So you have some bindings, meaning that you have a JavaScript object
[804.78 → 808.14] and when you call a function, then it's calling into the WebAssembly module.
[808.62 → 810.40] But if you pass the wrong type of parameter,
[810.66 → 812.92] let's say you pass a number instead of an object,
[813.50 → 816.82] then it won't be caught at the runtime.
[816.82 → 821.24] Then WebAssembly will think of the number as being a pointer to an object
[821.24 → 823.12] and then it will mess up the whole memory.
[823.76 → 826.80] So you end up, if you don't, if you're not careful,
[827.36 → 830.52] it's easy to break things, and it's not as forgiving as JavaScript.
[830.68 → 833.10] You don't have an error telling you,
[833.22 → 834.34] oh, this line there is an error.
[834.34 → 839.60] You have a strange error telling you that the module has to abort
[839.60 → 841.78] because of some memory issue.
[842.34 → 843.64] So how do you track those things down?
[843.74 → 848.16] What were the tooling that you had to apply in addition to just scripted to compile?
[848.54 → 854.04] So first thing is that I already had a set of tests in C++,
[854.50 → 856.68] but not enough, if you ask me.
[857.44 → 858.48] Yeah, that happened.
[858.80 → 860.84] The universal developer situation, right?
[860.92 → 861.96] Oh yeah, we have testing.
[862.42 → 862.96] Not enough.
[862.96 → 864.04] Well, maybe not.
[865.28 → 868.10] So yeah, what I still did was that when I,
[868.46 → 870.70] so when you have your WebAssembly module,
[871.00 → 875.84] you also have to create bindings that describe the classes existing in C++
[875.84 → 879.24] or in your language that you want to expose to the JavaScript world.
[879.92 → 884.02] And when writing this, I've also been writing tests
[884.02 → 886.94] to check that I can create a new object,
[887.28 → 888.72] like I call a method on it,
[888.80 → 891.02] and that it's returning the proper thing,
[891.02 → 894.62] just because I wanted to be confident about the fact that this was really working.
[894.78 → 895.48] The first time you're like,
[895.60 → 899.36] there should be a gotcha that it's going to crash at some point.
[899.50 → 900.74] So I started to write this,
[900.94 → 904.14] and basically what I've been doing without knowing
[904.14 → 908.96] is I created a set of tests on the interface of my library,
[909.24 → 910.66] because at the end what I have, it's a library.
[910.92 → 911.10] Right.
[911.10 → 915.76] And this thing is giving you great confidence into the fact that it's working.
[916.32 → 918.66] And also, if later something is crashing,
[918.96 → 920.48] you already have a test telling you that,
[920.62 → 922.64] okay, the base case is working,
[922.80 → 924.64] so maybe I've been misusing something,
[924.98 → 925.74] but it's working.
[925.86 → 928.02] So it's on me to fix it.
[928.08 → 928.96] It's not on WebAssembly.
[929.20 → 929.94] That makes sense.
[930.04 → 930.90] Yeah, you have to be,
[931.52 → 934.08] well, and now you're bridging from a compiled language
[934.08 → 936.50] where perhaps you have stronger types and things like that
[936.50 → 939.40] into a dynamic language like JavaScript.
[939.72 → 943.40] You have to do a lot more validation of your inputs and things like that.
[943.68 → 944.24] Yeah, exactly.
[944.54 → 949.40] And I've been looking at things to automate the creation of flow types
[949.40 → 952.64] or TypeScript types for the library that is generated.
[953.18 → 954.42] It's still not a thing.
[954.42 → 956.62] I've seen a project called End Bind
[956.62 → 962.36] that allows you to compile your C++ code base to ASM.js.
[962.52 → 963.50] So it's still not WebAssembly,
[963.50 → 967.60] but they are making automatic generation of typing.
[967.98 → 969.18] So I'm really missing this.
[969.36 → 973.28] I hope that we'll see more and more tooling creating these types.
[973.86 → 974.90] On the JavaScript side,
[975.04 → 977.76] I've been using Flow to type all my stuff.
[978.20 → 981.82] So at least I have not the safety as strong
[981.82 → 984.18] as a really strongly typed language,
[984.66 → 987.48] but still at first I started without,
[988.02 → 990.76] and now I cannot write any code without types
[990.76 → 992.48] because I'm getting more confident
[992.48 → 996.20] and this kind of things that are easy to debug in JavaScript,
[996.80 → 998.66] that they are there in WebAssembly.
[998.74 → 1000.36] So I want to be sure to pass the proper things.
[1000.36 → 1005.26] Yeah, it is an interesting example of how these things that are convenient
[1005.26 → 1006.96] but maybe not necessary in JavaScript,
[1007.18 → 1010.78] suddenly they become a requirement when you start bridging into other languages.
[1011.12 → 1012.60] Yes, and speaking of types,
[1013.24 → 1017.64] I'm a big fan of the typing system like TypeScript or Flow.
[1017.98 → 1020.84] It turns out that it's not really necessary when you're starting,
[1021.22 → 1022.62] but as the app is growing,
[1023.14 → 1025.92] it's really convenient to have typing that help you to refactor,
[1025.92 → 1028.28] will help you or someone else,
[1028.48 → 1030.66] like a contributor or another teammate.
[1031.52 → 1032.54] And in fact,
[1032.64 → 1035.54] when you're back to your code base after a few months without dealing with it,
[1035.66 → 1037.52] you're a stranger to your own code
[1037.52 → 1039.86] and types will save your life at least,
[1040.10 → 1040.74] or telling you,
[1040.82 → 1042.48] okay, you have removed a prop in this component,
[1042.90 → 1045.50] but you've not done it in the rest of the code base.
[1045.50 → 1050.24] So it's a really powerful tooling that, I guess,
[1050.44 → 1054.68] is really shining a few weeks or months after you're writing the code.
[1055.34 → 1058.88] Yeah, yeah, it's the type of thing that doesn't feel like you need it
[1058.88 → 1060.32] when you're getting started.
[1060.54 → 1063.08] And then as complexity grows, as contributors grow,
[1063.50 → 1065.80] you really wish you'd started it from the beginning.
[1066.08 → 1070.54] Yeah, sometimes I'm back on some components of the user interface
[1070.54 → 1071.66] that are not typed.
[1072.30 → 1074.04] Like, well, what I was thinking?
[1074.04 → 1074.70] No, no, no.
[1074.80 → 1076.18] I mean, it's okay.
[1076.32 → 1077.04] It's working well.
[1077.44 → 1079.60] But it's a good thing to add typing
[1079.60 → 1083.18] and to have the peace of mind that things will be all right.
[1083.18 → 1104.36] This episode is brought to you by DigitalOcean.
[1104.74 → 1108.62] DigitalOcean is the simplest cloud platform for developers and teams
[1108.62 → 1112.92] with products like droplets, spaces, Kubernetes, load balancers,
[1113.08 → 1115.42] block storage, and pre-built one-click apps.
[1115.72 → 1119.30] You can deploy, manage, and scale cloud applications faster
[1119.30 → 1121.34] and more efficiently on DigitalOcean.
[1121.68 → 1124.30] Whether you're running one virtual machine or 10,000,
[1124.62 → 1127.76] DigitalOcean makes managing your infrastructure way too easy.
[1128.12 → 1130.54] Head to do.co slash changelog.
[1130.54 → 1133.58] Again, do.co slash changelog.
[1133.58 → 1150.06] So it sounds like you have kind of a mixed background.
[1150.22 → 1153.22] You're coming from like a C++ and more traditional programming,
[1153.36 → 1156.02] and now you do a lot of web and React and things like that.
[1156.56 → 1159.66] I think our audience, we have also mixed background.
[1159.66 → 1163.18] I don't know, the listener here might have just JavaScript
[1163.18 → 1164.90] or they might be coming from all of those.
[1165.02 → 1169.12] But for someone who is just used to coding for the web and JavaScript,
[1169.28 → 1172.66] can you talk a little bit more about the things to wrap your head around?
[1172.74 → 1175.24] If, for example, you wanted to come and start using your game engine
[1175.24 → 1178.40] or you wanted to start working with some other native libraries,
[1178.56 → 1179.58] what feels different?
[1180.18 → 1185.38] Yeah, I mean, the thing that is really nice with JavaScript
[1185.38 → 1190.90] is that there is a simple mental model for how objects are living.
[1191.16 → 1192.72] Basically, you're creating a new object,
[1193.20 → 1195.00] and as long as it's not garbage collected,
[1195.16 → 1196.98] as long as you have a reference to it somewhere,
[1197.30 → 1198.80] then it's still there.
[1199.26 → 1201.96] I think the important thing to think about
[1201.96 → 1204.00] where you're using WebAssembly with,
[1204.24 → 1206.50] at least C++ might be better
[1206.50 → 1210.36] if WebAssembly is getting garbage collected at some point.
[1210.58 → 1211.50] For now, it's not the case.
[1211.50 → 1215.00] So I think the most important thing is to make sure
[1215.00 → 1216.82] that you understand the lifetime of your objects.
[1217.04 → 1218.82] I'm creating a new WebAssembly object,
[1219.22 → 1220.94] for example, when my component is mounted.
[1221.50 → 1225.24] Then I have to destroy this object when the component is mounted.
[1225.86 → 1228.64] Otherwise, the memory, well, the JavaScript object
[1228.64 → 1232.26] that is the shell around the WebAssembly object
[1232.26 → 1233.96] will be garbage collected,
[1234.30 → 1237.68] but the inner WebAssembly object in memory will stay there.
[1237.68 → 1240.66] So I think that's also something that I had issue with.
[1241.06 → 1242.18] At some point, for example,
[1242.50 → 1244.84] I created a new WebAssembly object,
[1244.98 → 1246.36] then I deleted it at some point,
[1246.88 → 1248.52] and without seeing it,
[1248.74 → 1250.30] I was reusing it at some other point.
[1250.54 → 1251.70] So it was a crash again.
[1252.36 → 1255.56] That's the thing that you want to look at when you're starting,
[1255.98 → 1258.46] especially if you're coming from a more web background.
[1259.02 → 1260.22] Yeah, that makes a lot of sense.
[1260.50 → 1262.34] And I do know that is another big area
[1262.34 → 1264.74] that the WebAssembly consortium is working on,
[1264.80 → 1265.58] is garbage collection,
[1265.58 → 1268.54] because that will smooth a lot of
[1268.54 → 1270.58] how do we interact with this via JavaScript
[1270.58 → 1273.54] and make sure that we're able to actually communicate objects
[1273.54 → 1275.68] back and forth rather than having a wrapper around it
[1275.68 → 1278.04] and serialization and all that mess.
[1278.44 → 1279.40] Yeah, it's true that,
[1280.18 → 1282.32] well, sometimes what I do in my component
[1282.32 → 1284.42] is that I get the WebAssembly object
[1284.42 → 1287.00] as a prop, or I create it.
[1287.04 → 1287.94] It depends on what I do.
[1288.74 → 1289.98] But then sometimes,
[1290.28 → 1293.34] I more or less convert it to a JavaScript object
[1293.34 → 1296.18] so that I can then pass it down to other components
[1296.18 → 1299.78] and I don't care about the lifetime and all those things.
[1300.34 → 1304.12] So I think that if WebAssembly is getting the garbage collection,
[1304.70 → 1307.42] yeah, it might ease the whole usage of it
[1307.42 → 1309.34] and bring additional safety.
[1310.22 → 1312.88] I'm pretty sure that I have some memory leaks in my application.
[1313.10 → 1313.88] I hope not too much.
[1314.34 → 1315.00] It should be okay.
[1315.54 → 1317.58] But still, it's manual memory management.
[1317.86 → 1319.40] Yeah, that's the downside for now.
[1319.40 → 1324.12] Is there any tooling available for debugging those memory leaks?
[1324.22 → 1325.32] So I know on the native side,
[1325.86 → 1328.70] there are lots of different tools that folks use.
[1328.84 → 1330.76] Have any of those things been ported to WebAssembly?
[1331.02 → 1331.80] I'm not sure.
[1332.26 → 1335.00] I've not seen any tooling like this.
[1335.58 → 1336.50] Hopefully that will appear.
[1336.84 → 1337.78] I've seen people,
[1338.34 → 1340.66] when you compile your WebAssembly module
[1340.66 → 1342.64] with some debugging flags,
[1343.20 → 1344.74] you're getting source maps.
[1344.74 → 1345.38] So for example,
[1345.48 → 1347.36] you can see in your Chrome debugger
[1347.36 → 1349.28] the source in C++
[1349.28 → 1352.06] and you can go from one line to the other.
[1352.48 → 1353.42] And that's really awesome.
[1353.84 → 1354.62] In my case,
[1354.80 → 1355.20] as I said,
[1355.24 → 1356.76] I have quite a lot of tests.
[1357.22 → 1360.00] So I'm actually confident in the fact that it's working.
[1360.22 → 1362.90] But if you're writing from scratch,
[1363.24 → 1365.14] it's a good idea to see if it's working.
[1365.36 → 1366.54] At least to see your Rust
[1366.54 → 1367.78] or Assembly Script
[1367.78 → 1369.80] or your C++ code base in Chrome.
[1369.90 → 1370.52] That's really fun.
[1370.98 → 1371.50] Yeah, no,
[1371.54 → 1372.26] that's really cool.
[1372.26 → 1374.94] But I feel like for the memory management stuff,
[1375.04 → 1375.46] that's tricky
[1375.46 → 1378.50] because it seems like a lot of the natural bugs
[1378.50 → 1380.28] are actually going to be in the interface.
[1380.72 → 1381.76] You can test one side,
[1381.86 → 1382.96] you can test the other side.
[1383.40 → 1384.96] But are you letting these things go?
[1385.64 → 1386.84] Well, that's an interesting question.
[1387.00 → 1389.52] So how would you write tests
[1389.52 → 1391.84] that bridge between your C++ code base
[1391.84 → 1392.36] and the JavaScript?
[1393.02 → 1394.64] Ideally, you won't
[1394.64 → 1396.56] and you would have an automatic generation
[1396.56 → 1397.88] of these bindings.
[1398.26 → 1399.68] At least the thing that...
[1399.68 → 1401.26] So in my case,
[1401.26 → 1402.64] as I'm using Scripted,
[1402.76 → 1405.08] I'm using some language called WebID.
[1405.52 → 1408.98] It's a Java-like way of describing classes.
[1409.94 → 1411.96] So this thing is used by Scripted
[1411.96 → 1413.14] to generate glue code.
[1413.76 → 1414.50] So that means that
[1414.50 → 1416.70] it's exposed on the JavaScript side,
[1417.08 → 1417.52] the classes
[1417.52 → 1419.42] and on the C++ side,
[1419.52 → 1420.76] it's calling the method.
[1421.28 → 1423.22] So at least if I'm making a mistake here,
[1423.62 → 1424.72] the C++ won't compile.
[1425.20 → 1425.84] But still,
[1426.02 → 1427.32] if I pass too much
[1427.32 → 1428.70] or too fewer arguments
[1428.70 → 1429.50] on JavaScript side,
[1429.72 → 1430.58] nothing will happen.
[1430.58 → 1431.30] So that's why I think
[1431.30 → 1432.20] that automatic generation
[1432.20 → 1433.82] of typings will help.
[1434.26 → 1434.96] Yeah, absolutely.
[1435.10 → 1435.86] I'm just thinking about
[1435.86 → 1437.88] if JavaScript is calling in
[1437.88 → 1438.32] to something
[1438.32 → 1440.40] that's going to allocate memory
[1440.40 → 1442.38] and then JavaScript owns that object
[1442.38 → 1443.10] and is required
[1443.10 → 1443.90] to then call in
[1443.90 → 1444.50] to reallocate,
[1444.80 → 1445.60] to write a test,
[1445.66 → 1446.18] we're going to kind of
[1446.18 → 1447.30] have to bridge across.
[1447.58 → 1448.20] Yeah, right.
[1448.38 → 1449.38] I think that there is
[1449.38 → 1450.50] no good solution for now
[1450.50 → 1451.18] except maybe
[1451.18 → 1452.60] automatic garbage collection.
[1452.86 → 1453.20] Basically,
[1453.46 → 1454.26] you can't really test
[1454.26 → 1456.18] for manual memory management.
[1456.52 → 1457.68] You just have to be careful.
[1457.68 → 1459.70] Yeah, absolutely.
[1460.40 → 1461.38] So you talked a little bit
[1461.38 → 1462.78] for the game engine,
[1462.86 → 1463.60] your target is
[1463.60 → 1464.46] kind of laptop,
[1464.64 → 1464.86] desktop,
[1465.08 → 1465.76] things like that.
[1465.84 → 1467.56] Is this also a methodology
[1467.56 → 1468.22] that will work
[1468.22 → 1468.84] for targeting
[1468.84 → 1469.98] mobile applications?
[1470.64 → 1472.06] I think that could be,
[1472.30 → 1473.20] so if you're running
[1473.20 → 1474.46] a native application
[1474.46 → 1475.50] and you want to reuse
[1475.50 → 1476.30] your native code base,
[1476.54 → 1477.46] well, if it's C++
[1477.46 → 1479.04] or even Rust maybe,
[1479.16 → 1479.70] I've not tried,
[1480.00 → 1480.58] you might as well
[1480.58 → 1482.74] compile to a native library
[1482.74 → 1483.54] and reuse it
[1483.54 → 1484.22] in your iOS
[1484.22 → 1485.46] or Android application.
[1485.92 → 1486.54] I would say a bit
[1486.54 → 1487.64] the same in React Native.
[1488.00 → 1489.06] If you want to reuse
[1489.06 → 1490.16] a native library,
[1490.42 → 1491.26] you can keep it
[1491.26 → 1492.78] as a native module.
[1493.34 → 1493.64] But I think
[1493.64 → 1495.56] this is getting interesting
[1495.56 → 1496.56] for mobiles,
[1496.74 → 1498.02] for progressive web apps,
[1498.10 → 1498.46] for example.
[1498.76 → 1499.56] There is an example
[1499.56 → 1500.88] made by some
[1500.88 → 1501.76] Google developers.
[1502.40 → 1502.66] It's called
[1502.66 → 1503.92] a squoosh.app.
[1505.08 → 1507.04] It's a PWA
[1507.04 → 1508.92] but running
[1508.92 → 1509.92] WebAssembly code
[1509.92 → 1511.64] to reduce
[1511.64 → 1512.80] the size of an image
[1512.80 → 1513.78] and to do transformation
[1513.78 → 1514.78] on an image.
[1515.34 → 1515.86] And it's a good,
[1515.98 → 1516.54] it's open source.
[1516.70 → 1518.00] So it's a good example
[1518.00 → 1518.38] for people
[1518.38 → 1519.80] that want to start.
[1520.26 → 1520.62] And I think
[1520.62 → 1521.10] that we'll see
[1521.10 → 1521.72] more and more
[1521.72 → 1522.84] application,
[1523.80 → 1524.66] well, web apps
[1524.66 → 1526.04] and even web apps
[1526.04 → 1526.62] for mobile
[1526.62 → 1527.90] that are running
[1527.90 → 1528.58] some kind of
[1528.58 → 1529.06] WebAssembly
[1529.06 → 1531.22] and that using this
[1531.22 → 1532.22] we might get something
[1532.22 → 1534.44] that is not as fast
[1534.44 → 1535.60] as a native app
[1535.60 → 1536.62] on mobile
[1536.62 → 1537.64] because native
[1537.64 → 1538.14] is still
[1538.14 → 1539.50] has a lot of
[1539.50 → 1540.38] compelling advantage
[1540.38 → 1541.24] when it comes to
[1541.24 → 1542.16] making user interface
[1542.16 → 1543.06] it's super smooth
[1543.06 → 1543.62] and so on.
[1544.26 → 1545.60] But you never know
[1545.60 → 1546.72] with WebAssembly
[1546.72 → 1547.78] running your business logic
[1547.78 → 1548.68] or maybe some part
[1548.68 → 1549.92] of your interface
[1549.92 → 1550.70] that might get
[1550.70 → 1551.36] really smooth
[1551.36 → 1552.16] and good enough
[1552.16 → 1553.02] to say
[1553.02 → 1554.54] that it's an app
[1554.54 → 1556.50] and it's not
[1556.50 → 1557.46] a progressive web app
[1557.46 → 1558.26] or web app
[1558.26 → 1559.24] it's just an app.
[1559.48 → 1559.78] Yeah, no,
[1559.84 → 1561.18] this is fascinating
[1561.18 → 1562.20] and I think
[1562.20 → 1562.92] one of the very
[1562.92 → 1563.72] nice things
[1563.72 → 1564.36] that WebAssembly
[1564.36 → 1565.18] gets you
[1565.18 → 1565.74] is it's got
[1565.74 → 1566.38] all these great
[1566.38 → 1567.78] sandboxing utilities
[1567.78 → 1568.44] and then
[1568.44 → 1569.46] you now
[1569.46 → 1570.08] if you're using
[1570.08 → 1570.62] WebAssembly
[1570.62 → 1571.12] and JavaScript
[1571.12 → 1571.84] you have access
[1571.84 → 1572.66] to NPM
[1572.66 → 1573.48] and all of this
[1573.48 → 1574.72] incredible ecosystem
[1574.72 → 1576.12] that is
[1576.12 → 1577.82] much more expansive
[1577.82 → 1579.04] than might exist
[1579.04 → 1580.08] and that's what
[1580.08 → 1581.08] I lacked really
[1581.08 → 1581.80] with JavaScript
[1581.80 → 1582.24] is that
[1582.24 → 1583.04] sometimes people
[1583.04 → 1583.46] are complaining
[1583.46 → 1584.00] about oh yeah
[1584.00 → 1585.42] I'm doing NPM install
[1585.42 → 1586.04] and getting
[1586.04 → 1587.66] tons of modules
[1587.66 → 1588.20] that I don't know
[1588.20 → 1588.80] what they're doing.
[1589.38 → 1590.12] Actually that's
[1590.12 → 1590.80] the weakness
[1590.80 → 1591.74] and the force
[1591.74 → 1593.04] of the whole ecosystem.
[1593.42 → 1594.02] When I'm back
[1594.02 → 1594.48] to working
[1594.48 → 1595.24] with C++
[1595.24 → 1596.82] I want an easy
[1596.82 → 1597.92] function to do something
[1597.92 → 1598.78] I can't find it
[1598.78 → 1599.68] I have to write it
[1599.68 → 1600.26] from scratch
[1600.26 → 1601.48] or I can find it
[1601.48 → 1602.56] maybe in a library
[1602.56 → 1603.30] but then
[1603.30 → 1604.28] it's a pain
[1604.28 → 1604.92] to install
[1604.92 → 1606.30] so I think
[1606.30 → 1606.74] that's really
[1606.74 → 1608.36] the huge strength
[1608.36 → 1609.14] of the JavaScript
[1609.14 → 1609.54] ecosystem
[1609.54 → 1610.16] that you can
[1610.16 → 1611.40] NPM install
[1611.40 → 1612.72] basically anything.
[1612.96 → 1613.20] Anything.
[1613.54 → 1613.70] Yep.
[1614.16 → 1614.98] The strength
[1614.98 → 1615.34] is you can
[1615.34 → 1615.92] NPM install
[1615.92 → 1616.24] anything
[1616.24 → 1616.72] the weakness
[1616.72 → 1617.24] is you can
[1617.24 → 1617.84] NPM install
[1617.84 → 1618.84] anything.
[1620.30 → 1620.84] Yeah exactly
[1620.84 → 1622.10] but I want to say
[1622.10 → 1622.74] that when people
[1622.74 → 1623.12] are sometimes
[1623.12 → 1623.72] like oh yeah
[1623.72 → 1624.28] there are tons
[1624.28 → 1624.82] of modules
[1624.82 → 1625.50] that are being
[1625.50 → 1626.00] imported
[1626.00 → 1627.04] I'm like yeah
[1627.04 → 1627.94] but you know
[1627.94 → 1628.74] the C++
[1628.74 → 1629.42] standard library
[1629.42 → 1630.24] it's huge too
[1630.24 → 1632.58] and we cannot
[1632.58 → 1633.86] iterate as fast
[1633.86 → 1635.26] because it has
[1635.26 → 1635.66] to go through
[1635.66 → 1636.46] a standardization
[1636.46 → 1636.92] process
[1636.92 → 1638.24] it has advantage
[1638.24 → 1638.90] and disadvantage
[1638.90 → 1642.94] but the reason
[1642.94 → 1644.16] I've written
[1644.16 → 1644.92] the whole interface
[1644.92 → 1645.34] in React
[1645.34 → 1646.00] is because I think
[1646.00 → 1646.54] that React
[1646.54 → 1647.12] and JavaScript
[1647.12 → 1647.52] ecosystem
[1647.52 → 1648.66] is better
[1648.66 → 1649.74] now and faster
[1649.74 → 1651.16] at developing
[1651.16 → 1652.68] good and advanced
[1652.68 → 1653.30] interface.
[1654.12 → 1654.24] Yeah.
[1654.72 → 1655.58] Yeah JavaScript
[1655.58 → 1656.82] just moves faster
[1656.82 → 1657.34] and the web
[1657.34 → 1658.16] moves faster
[1658.16 → 1658.88] and there's
[1658.88 → 1659.84] pros and cons
[1659.84 → 1660.14] to that
[1660.14 → 1660.34] you know
[1660.34 → 1661.06] it's a constant
[1661.06 → 1661.38] effort
[1661.38 → 1661.88] and I think
[1661.88 → 1663.02] one of the things
[1663.02 → 1663.84] that the
[1663.84 → 1664.50] you know
[1664.50 → 1665.24] the fact that
[1665.24 → 1665.82] every project
[1665.82 → 1666.44] then ends up
[1666.44 → 1667.06] having a thousand
[1667.06 → 1667.62] dependencies
[1667.62 → 1668.54] and sub-dependencies
[1668.54 → 1669.60] means is we need
[1669.60 → 1670.36] to improve the tooling
[1670.36 → 1670.90] around that.
[1670.98 → 1671.10] Yeah.
[1671.76 → 1672.78] Give more visibility
[1672.78 → 1673.40] on what you're
[1673.40 → 1673.80] importing
[1673.80 → 1674.86] maybe some
[1674.86 → 1675.94] more checking
[1675.94 → 1677.56] around what's
[1677.56 → 1678.34] really inside
[1678.34 → 1679.16] your bundles
[1679.16 → 1680.06] code splitting
[1680.06 → 1681.14] and conversely
[1681.14 → 1681.82] things that are
[1681.82 → 1682.50] native are not
[1682.50 → 1683.34] yet in JavaScript
[1683.34 → 1684.22] but things are
[1684.22 → 1684.68] improving.
[1685.18 → 1685.76] I like to
[1685.76 → 1686.80] look at even
[1686.80 → 1687.52] the language
[1687.52 → 1688.14] JavaScript
[1688.14 → 1689.64] it's used to
[1689.64 → 1690.26] be a scripting
[1690.26 → 1690.66] language
[1690.66 → 1691.22] and now
[1691.22 → 1691.94] with all
[1691.94 → 1693.06] the ES6
[1693.06 → 1693.96] and all
[1693.96 → 1695.32] the typing
[1695.32 → 1696.86] that we can
[1696.86 → 1697.18] add
[1697.18 → 1698.20] we are moving
[1698.20 → 1698.74] toward a
[1698.74 → 1699.66] really robust
[1699.66 → 1700.14] language
[1700.14 → 1701.82] and on
[1701.82 → 1702.58] the contrary
[1702.58 → 1703.30] things like
[1703.30 → 1704.20] language like
[1704.20 → 1704.92] C++ are now
[1704.92 → 1705.72] introducing things
[1705.72 → 1706.48] like lambdas
[1706.48 → 1708.34] and automatic
[1708.34 → 1708.88] typing
[1708.88 → 1710.08] so things are
[1710.08 → 1711.76] going in the
[1711.76 → 1712.30] same direction
[1712.30 → 1712.70] actually.
[1713.26 → 1713.40] Yeah.
[1713.62 → 1714.38] Yeah absolutely.
[1714.38 → 1715.38] When you were
[1715.38 → 1715.86] talking about
[1715.86 → 1716.56] the size of
[1716.56 → 1717.60] the WebAssembly
[1717.60 → 1717.88] bubble
[1717.88 → 1718.46] pulling in
[1718.46 → 1718.80] the standard
[1718.80 → 1719.10] library
[1719.10 → 1719.62] so is there
[1719.62 → 1720.28] any concept
[1720.28 → 1721.00] of tree shaking
[1721.00 → 1721.84] when you talk
[1721.84 → 1722.64] about compiling
[1722.64 → 1723.16] you know
[1723.16 → 1724.30] we've got this
[1724.30 → 1724.94] standard library
[1724.94 → 1725.58] but maybe I'm
[1725.58 → 1726.08] only using
[1726.08 → 1726.74] five functions
[1726.74 → 1727.20] and sure
[1727.20 → 1727.68] they use
[1727.68 → 1728.30] 20 more
[1728.30 → 1728.84] underneath the
[1728.84 → 1729.10] covers
[1729.10 → 1730.00] but you know
[1730.00 → 1730.92] 25 out of
[1730.92 → 1731.46] however many
[1731.46 → 1731.88] thousand
[1731.88 → 1733.38] Yeah yeah
[1733.38 → 1734.76] so there is
[1734.76 → 1736.42] no code splitting
[1736.42 → 1737.68] or tree shaking
[1737.68 → 1738.86] no way there is
[1738.86 → 1739.28] for example
[1739.28 → 1739.84] when you're
[1739.84 → 1741.14] what language
[1741.14 → 1741.70] like C++
[1741.70 → 1742.50] and compilers
[1742.50 → 1743.08] have been doing
[1743.08 → 1743.78] since a bit
[1743.78 → 1744.06] of time
[1744.06 → 1744.82] that when
[1744.82 → 1746.10] you're compiling
[1746.10 → 1747.18] your whole
[1747.18 → 1747.56] software
[1747.56 → 1748.50] and using
[1748.50 → 1748.94] a library
[1748.94 → 1749.56] only the
[1749.56 → 1750.10] functions
[1750.10 → 1751.14] that are
[1751.14 → 1751.86] actually used
[1751.86 → 1752.50] will be included
[1752.50 → 1753.38] in the binary
[1753.38 → 1754.04] at the end
[1754.04 → 1754.92] so it's
[1754.92 → 1755.82] basically tree shaking
[1755.82 → 1756.64] They're already
[1756.64 → 1757.70] doing dead code
[1757.70 → 1758.16] elimination
[1758.16 → 1758.62] or whatever
[1758.62 → 1759.08] it's called
[1759.08 → 1760.04] I think that
[1760.04 → 1760.58] dead code
[1760.58 → 1760.92] elimination
[1760.92 → 1761.60] might still
[1761.60 → 1762.04] not be
[1762.04 → 1763.18] 100% exact
[1763.18 → 1764.32] so you're
[1764.32 → 1764.66] still having
[1764.66 → 1766.66] more libraries
[1766.66 → 1767.34] that you
[1767.34 → 1768.30] want to have
[1768.30 → 1769.34] I think that
[1769.34 → 1770.02] I've seen
[1770.02 → 1770.62] things like
[1770.62 → 1771.60] how to have
[1771.60 → 1772.16] some kind of
[1772.16 → 1773.00] dynamic libraries
[1773.00 → 1773.72] in WebAssembly
[1773.72 → 1774.86] that mean
[1774.86 → 1775.70] that you
[1775.70 → 1776.28] could have
[1776.28 → 1777.08] your native
[1777.08 → 1777.44] code
[1777.44 → 1778.14] that is
[1778.14 → 1778.60] required
[1778.60 → 1779.14] only when
[1779.14 → 1779.68] it's really
[1779.68 → 1780.04] needed
[1780.04 → 1780.64] so I don't
[1780.64 → 1780.88] know for
[1780.88 → 1781.10] example
[1781.10 → 1781.78] if you have
[1781.78 → 1783.00] a physics
[1783.00 → 1783.38] engine
[1783.38 → 1783.68] that you
[1783.68 → 1783.94] want to
[1783.94 → 1784.38] reuse
[1784.38 → 1785.16] if it's
[1785.16 → 1785.54] a 2D
[1785.54 → 1786.00] or 3D
[1786.00 → 1786.44] there might
[1786.44 → 1787.40] be a way
[1787.40 → 1788.14] to exclude
[1788.14 → 1788.76] the 2D
[1788.76 → 1789.16] library
[1789.16 → 1789.82] or the 3D
[1789.82 → 1790.14] library
[1790.14 → 1790.54] according to
[1790.54 → 1790.82] what you're
[1790.82 → 1791.08] doing
[1791.08 → 1791.58] yeah
[1791.58 → 1791.60] yeah
[1791.60 → 1792.82] that's
[1792.82 → 1793.82] starts to
[1793.82 → 1794.18] get really
[1794.18 → 1794.58] interesting
[1794.58 → 1795.42] and
[1795.42 → 1796.18] you know
[1796.18 → 1797.14] there's
[1797.14 → 1797.50] some
[1797.50 → 1798.06] progress
[1798.06 → 1798.42] towards
[1798.42 → 1798.74] saying
[1798.74 → 1799.04] okay
[1799.04 → 1799.64] do we
[1799.64 → 1799.98] want to
[1799.98 → 1800.42] have
[1800.42 → 1801.22] a standard
[1801.22 → 1801.54] library
[1801.54 → 1801.92] for
[1801.92 → 1802.30] JavaScript
[1802.30 → 1802.84] or something
[1802.84 → 1803.22] like that
[1803.22 → 1803.50] so that
[1803.50 → 1803.94] the browser
[1803.94 → 1804.70] just already
[1804.70 → 1805.18] has all
[1805.18 → 1805.34] these
[1805.34 → 1805.84] functionality
[1805.84 → 1806.76] when we
[1806.76 → 1807.34] talk about
[1807.34 → 1808.32] WebAssembly
[1808.32 → 1808.72] and pulling
[1808.72 → 1809.48] in the C++
[1809.48 → 1810.32] standard library
[1810.32 → 1810.62] like
[1810.62 → 1811.76] that is a
[1811.76 → 1812.08] standard
[1812.08 → 1813.20] why not
[1813.20 → 1813.82] why not
[1813.82 → 1814.34] just have it
[1814.34 → 1814.82] bundled with
[1814.82 → 1815.16] the browser
[1815.16 → 1815.68] you have to
[1815.68 → 1816.06] get the good
[1816.06 → 1816.40] balance
[1816.40 → 1816.84] between
[1816.84 → 1817.68] innovation
[1817.68 → 1818.22] in your
[1818.22 → 1818.58] ecosystem
[1818.58 → 1819.10] and still
[1819.10 → 1819.32] something
[1819.32 → 1819.66] that is
[1819.66 → 1820.04] robust
[1820.04 → 1820.44] enough
[1820.44 → 1822.08] people like
[1822.08 → 1822.42] to say
[1822.42 → 1822.66] also
[1822.66 → 1823.04] that for
[1823.04 → 1823.26] example
[1823.26 → 1823.96] when the
[1823.96 → 1824.46] package
[1824.46 → 1824.72] was
[1824.72 → 1825.40] left pad
[1825.40 → 1825.94] was
[1825.94 → 1826.46] you know
[1826.46 → 1827.26] removed
[1827.26 → 1827.90] from NPM
[1827.90 → 1828.28] oh yeah
[1828.28 → 1828.66] that was
[1828.66 → 1829.42] the end
[1829.42 → 1829.68] of the
[1829.68 → 1829.94] world
[1829.94 → 1830.82] in a way
[1830.82 → 1831.40] it was
[1831.40 → 1831.88] but I
[1831.88 → 1832.04] think
[1832.04 → 1832.74] that still
[1832.74 → 1833.18] it's not
[1833.18 → 1833.60] a problem
[1833.60 → 1834.14] about
[1834.14 → 1834.92] the ecosystem
[1834.92 → 1835.28] it's a
[1835.28 → 1835.48] problem
[1835.48 → 1835.80] about
[1835.80 → 1836.10] the thing
[1836.10 → 1836.34] that
[1836.34 → 1836.82] package
[1836.82 → 1837.16] should be
[1837.16 → 1837.82] immutable
[1837.82 → 1838.82] and
[1838.82 → 1839.66] shouldn't
[1839.66 → 1840.00] be able
[1840.00 → 1840.36] to be
[1840.36 → 1840.68] removed
[1840.68 → 1841.00] maybe
[1841.00 → 1841.58] but I
[1841.58 → 1841.72] think
[1841.72 → 1842.04] that we
[1842.04 → 1842.66] can improve
[1842.66 → 1843.04] and that's
[1843.04 → 1843.38] great
[1843.38 → 1843.90] to see
[1845.16 → 1847.10] the
[1847.10 → 1847.66] thing
[1847.66 → 1848.26] is
[1848.26 → 1850.84] we are
[1850.84 → 1852.34] able to
[1852.34 → 1853.32] build
[1853.32 → 1854.60] on
[1854.60 → 1854.94] things
[1854.94 → 1855.56] that's
[1855.56 → 1855.70] maybe
[1855.70 → 1857.16] the dream
[1857.16 → 1857.52] of open
[1857.52 → 1857.84] source
[1857.84 → 1859.32] or using
[1859.32 → 1859.80] stuff
[1859.80 → 1860.40] as much
[1860.40 → 1860.86] as possible
[1860.86 → 1861.74] yeah
[1861.74 → 1862.26] the
[1862.26 → 1862.86] thousand
[1862.86 → 1863.36] module
[1863.36 → 1864.86] situation
[1864.86 → 1865.38] comes from
[1865.38 → 1865.72] the fact
[1865.72 → 1866.06] that
[1866.06 → 1866.64] module
[1866.64 → 1867.00] bundling
[1867.00 → 1867.42] used to
[1867.42 → 1867.62] be
[1867.62 → 1867.96] tricky
[1867.96 → 1868.60] it used
[1868.60 → 1869.08] to be
[1869.08 → 1869.66] expensive
[1869.66 → 1870.08] so you'd
[1870.08 → 1870.36] only do
[1870.36 → 1870.62] it for
[1870.62 → 1871.06] very big
[1871.06 → 1871.46] things
[1871.46 → 1871.80] but
[1871.80 → 1872.50] now
[1872.50 → 1872.82] it's so
[1872.82 → 1873.12] easy
[1873.12 → 1873.60] and simple
[1873.60 → 1873.96] at least
[1873.96 → 1874.28] in the
[1874.28 → 1874.56] JavaScript
[1874.56 → 1874.92] world
[1874.92 → 1875.16] then
[1875.16 → 1875.64] why not
[1875.64 → 1876.06] you can
[1876.06 → 1877.04] NPM
[1877.04 → 1877.60] publish
[1877.60 → 1878.04] something
[1878.04 → 1878.34] in a
[1878.34 → 1878.64] few
[1878.64 → 1879.44] minutes
[1879.44 → 1880.74] and
[1880.74 → 1881.40] it's
[1881.40 → 1881.72] something
[1881.72 → 1881.98] that I
[1881.98 → 1882.26] like
[1882.26 → 1882.80] for example
[1882.80 → 1883.20] React
[1883.20 → 1883.48] that
[1883.48 → 1884.16] when you
[1884.16 → 1884.42] have your
[1884.42 → 1884.80] tree of
[1884.80 → 1885.20] components
[1885.20 → 1885.64] you have
[1885.64 → 1885.94] a large
[1885.94 → 1886.26] component
[1886.26 → 1886.82] it's
[1886.82 → 1887.08] easy
[1887.08 → 1887.42] to take
[1887.42 → 1887.66] a bit
[1887.66 → 1888.28] of JSX
[1888.28 → 1888.72] somewhere
[1888.72 → 1889.66] extract it
[1889.66 → 1890.00] to a new
[1890.00 → 1890.32] component
[1890.32 → 1891.28] and reuse
[1891.28 → 1891.66] it really
[1891.66 → 1892.02] quickly
[1892.02 → 1892.80] and I
[1892.80 → 1892.92] think
[1892.92 → 1894.18] that this
[1894.18 → 1894.56] feedback
[1894.56 → 1895.06] loop
[1895.06 → 1895.46] that is
[1895.46 → 1895.68] really
[1895.68 → 1896.16] quick
[1896.16 → 1896.92] is important
[1896.92 → 1897.54] in all
[1897.54 → 1897.80] stages
[1897.80 → 1898.00] of the
[1898.00 → 1898.32] development
[1898.32 → 1898.92] including
[1898.92 → 1899.64] in libraries
[1899.64 → 1900.54] if you want
[1900.54 → 1900.76] to make
[1900.76 → 1901.08] a new
[1901.08 → 1901.60] C++
[1901.60 → 1902.14] library
[1902.14 → 1903.66] that takes
[1903.66 → 1903.86] a bit
[1903.86 → 1904.38] of time
[1904.38 → 1904.82] to get
[1904.82 → 1905.16] the whole
[1905.16 → 1905.90] tooling
[1905.90 → 1906.58] set up
[1906.58 → 1907.82] that would
[1907.82 → 1908.36] be a nightmare
[1908.36 → 1909.04] if you compare
[1909.04 → 1909.30] it to
[1909.30 → 1909.68] NPM
[1909.68 → 1910.60] I hope
[1910.60 → 1911.02] that things
[1911.02 → 1911.26] that are
[1911.26 → 1911.74] compiling to
[1911.74 → 1912.16] WebAssembly
[1912.16 → 1912.72] like Rust
[1912.72 → 1913.32] are improving
[1913.32 → 1913.62] this
[1913.62 → 1914.46] the ability
[1914.46 → 1914.88] to create
[1914.88 → 1915.32] libraries
[1915.32 → 1916.06] really quickly
[1916.06 → 1917.00] because that's
[1917.00 → 1917.46] how you
[1917.46 → 1918.60] create an
[1918.60 → 1918.94] ecosystem
[1918.94 → 1919.32] that is
[1919.32 → 1919.86] exploding
[1919.86 → 1920.86] instead of
[1920.86 → 1921.68] growing
[1921.68 → 1922.78] linearly
[1922.78 → 1923.60] yeah
[1923.60 → 1924.16] well and we
[1924.16 → 1924.72] seem to be
[1924.72 → 1925.42] figuring out
[1925.42 → 1926.00] some of the
[1926.00 → 1926.60] factors that
[1926.60 → 1927.06] make that
[1927.06 → 1927.78] possible
[1927.78 → 1929.30] I think
[1929.30 → 1930.10] an emphasis
[1930.10 → 1932.14] on refactorability
[1932.14 → 1933.10] and composability
[1933.10 → 1933.66] is huge
[1933.66 → 1934.14] that was one
[1934.14 → 1934.72] of the driving
[1934.72 → 1935.80] at least
[1935.80 → 1936.88] stated motivations
[1936.88 → 1937.42] for hooks
[1937.42 → 1938.00] is it makes
[1938.00 → 1938.44] it is easier
[1938.44 → 1939.02] to cut and
[1939.02 → 1939.58] paste code
[1939.58 → 1940.42] and refactor
[1940.42 → 1940.68] it into
[1940.68 → 1941.32] new locations
[1941.32 → 1942.58] and sort of
[1942.58 → 1943.54] move things
[1943.54 → 1943.94] around
[1943.94 → 1944.88] I was speaking
[1944.88 → 1945.50] about typing
[1945.50 → 1945.96] I think it's
[1945.96 → 1946.32] a bit the
[1946.32 → 1946.56] same
[1946.56 → 1947.42] that when
[1947.42 → 1948.72] you're investing
[1948.72 → 1949.66] a bit in
[1949.66 → 1951.02] some tooling
[1951.02 → 1951.50] like this
[1951.50 → 1952.48] for making
[1952.48 → 1953.44] things easier
[1953.44 → 1954.02] to refactor
[1954.02 → 1954.80] then it's
[1954.80 → 1955.38] a huge win
[1955.38 → 1956.58] because some
[1956.58 → 1957.50] people told me
[1957.50 → 1957.98] yeah but you
[1957.98 → 1958.40] know if you
[1958.40 → 1958.88] make small
[1958.88 → 1959.20] modules
[1959.20 → 1960.18] you will have
[1960.18 → 1960.68] things that
[1960.68 → 1962.12] have a simple
[1962.12 → 1962.68] interface
[1962.68 → 1963.26] so you don't
[1963.26 → 1963.78] need typing
[1963.78 → 1964.30] for example
[1964.30 → 1965.26] that might be
[1965.26 → 1965.80] true but
[1965.80 → 1966.16] on the other
[1966.16 → 1966.94] way you can't
[1966.94 → 1967.44] say that you
[1967.44 → 1967.98] will never
[1967.98 → 1968.76] refactor something
[1968.76 → 1969.58] even a small
[1969.58 → 1970.28] module you want
[1970.28 → 1970.66] to at some
[1970.66 → 1971.70] point add or
[1971.70 → 1972.38] remove something
[1972.38 → 1973.46] I mean even
[1973.46 → 1974.50] even components
[1974.50 → 1976.64] it's a strength
[1976.64 → 1977.50] of React is to
[1977.50 → 1978.22] be able to move
[1978.22 → 1979.44] components easily
[1979.44 → 1982.12] and I think
[1982.12 → 1982.52] that's something
[1982.52 → 1983.04] that you want
[1983.04 → 1983.84] to keep
[1983.84 → 1984.46] is your ability
[1984.46 → 1984.92] to refactor
[1984.92 → 1985.46] things without
[1985.46 → 1986.64] breaking things
[1986.64 → 1987.66] so that's why
[1987.66 → 1988.44] I think typing
[1988.44 → 1989.90] and having a
[1989.90 → 1990.38] library that
[1990.38 → 1990.82] allows you to
[1990.82 → 1991.10] create a
[1991.10 → 1992.08] component using
[1992.08 → 1992.84] only a function
[1992.84 → 1994.04] that's a really
[1994.04 → 1994.58] great thing
[1994.58 → 1995.80] yeah well and
[1995.80 → 1997.00] anytime you're
[1997.00 → 1997.98] exploring somebody
[1997.98 → 1998.56] else's module
[1998.56 → 1999.26] having those types
[1999.26 → 1999.92] is really useful
[1999.92 → 2000.80] because I don't
[2000.80 → 2001.20] know am I
[2001.20 → 2001.88] using this right
[2001.88 → 2002.72] oh it didn't
[2002.72 → 2003.52] compile the types
[2003.52 → 2003.76] are wrong
[2003.76 → 2004.82] okay now I
[2004.82 → 2005.16] know what I
[2005.16 → 2005.64] need to do
[2005.64 → 2006.20] yeah that's
[2006.20 → 2007.06] basically documentation
[2007.06 → 2008.00] and it's a
[2008.00 → 2008.72] safety net
[2008.72 → 2010.26] so it's
[2010.26 → 2011.14] particularly useful
[2011.14 → 2011.74] for library
[2011.74 → 2012.80] this being said
[2012.80 → 2013.70] it has to
[2013.70 → 2014.16] it depends on
[2014.16 → 2014.78] your use case
[2014.78 → 2015.54] I have the
[2015.54 → 2017.04] website of
[2017.04 → 2018.58] Develop the
[2018.58 → 2019.18] game engine
[2019.18 → 2020.20] which is done
[2020.20 → 2021.02] in React
[2021.02 → 2021.94] using Gatsby
[2021.94 → 2023.10] but I have
[2023.10 → 2023.46] no typing
[2023.46 → 2024.60] because there
[2024.60 → 2025.30] I don't really
[2025.30 → 2026.08] care the
[2026.08 → 2026.86] model of
[2026.86 → 2028.08] components that
[2028.08 → 2028.56] I have with
[2028.56 → 2029.44] React is enough
[2029.44 → 2030.18] to get something
[2030.18 → 2031.74] that is working
[2031.74 → 2032.02] well
[2032.02 → 2033.02] well this being
[2033.02 → 2033.48] said I'm the
[2033.48 → 2034.04] only one
[2034.04 → 2035.06] more or less
[2035.06 → 2035.52] the only one
[2035.52 → 2036.04] to be working
[2036.04 → 2037.00] on it, so I
[2037.00 → 2037.52] might change my
[2037.52 → 2038.30] opinion if I get
[2038.30 → 2038.90] more contributors
[2038.90 → 2040.86] yeah okay, so I
[2040.86 → 2041.30] want to explore
[2041.30 → 2041.82] that a little bit
[2041.82 → 2042.28] because we just
[2042.28 → 2044.04] talked with Jason
[2044.04 → 2044.76] from Gatsby
[2044.76 → 2046.28] and so we were
[2046.28 → 2046.74] hearing a lot
[2046.74 → 2047.46] about you know
[2047.46 → 2048.00] what they have
[2048.00 → 2048.96] working and sort
[2048.96 → 2049.60] of the inside
[2049.60 → 2050.60] view, but you're
[2050.60 → 2051.16] coming in you're
[2051.16 → 2051.76] using it as a
[2051.76 → 2052.58] user what's your
[2052.58 → 2053.38] impression of Gatsby
[2053.38 → 2055.58] I've been very
[2055.58 → 2056.74] happy with it, I'm
[2056.74 → 2057.92] a big fan of the
[2057.92 → 2059.06] React approach
[2059.06 → 2059.72] because when I was
[2059.72 → 2060.54] redesigning the
[2060.54 → 2061.78] website I was like
[2061.78 → 2063.46] I can identify
[2063.46 → 2065.46] components in the
[2065.46 → 2066.12] design that I
[2066.12 → 2066.74] want for my
[2066.74 → 2068.20] website, so I
[2068.20 → 2069.20] wanted to have
[2069.20 → 2070.04] an easy way to
[2070.04 → 2071.08] start a website
[2071.08 → 2071.82] so I started to
[2071.82 → 2072.58] look at Gatsby
[2072.58 → 2073.88] and all the
[2073.88 → 2075.38] performance that
[2075.38 → 2076.10] come with it
[2076.10 → 2077.36] I've been very
[2077.36 → 2078.02] happy with it
[2078.02 → 2079.48] the website is
[2079.48 → 2081.66] running really
[2081.66 → 2083.12] fast and the
[2083.12 → 2083.76] development experience
[2083.76 → 2084.42] is also really
[2084.42 → 2085.04] nice because there
[2085.04 → 2086.00] is hot reloading
[2086.00 → 2087.06] which is something
[2087.06 → 2088.78] that's a bit hard
[2088.78 → 2090.20] to set up but
[2090.20 → 2091.10] well it comes for
[2091.10 → 2091.90] free with Gatsby
[2091.90 → 2093.96] so I only have
[2093.96 → 2095.00] good things to
[2095.00 → 2097.74] say about Gatsby
[2097.74 → 2098.50] and the ecosystem
[2098.50 → 2099.22] around it
[2099.22 → 2101.06] it's funny thinking
[2101.06 → 2102.86] about these days
[2102.86 → 2103.80] with Webpack and
[2103.80 → 2104.40] various things we
[2104.40 → 2105.04] almost take for
[2105.04 → 2106.10] granted okay auto
[2106.10 → 2107.02] reloading I make a
[2107.02 → 2107.82] change it's just
[2107.82 → 2108.54] going to be there
[2108.54 → 2109.72] but that's a
[2109.72 → 2111.40] phenomenal upgrade in
[2111.40 → 2112.54] productivity because of
[2112.54 → 2113.46] that iteration speed
[2113.46 → 2115.02] yeah that's again the
[2115.02 → 2115.96] feedback loop in the
[2115.96 → 2116.62] development that is
[2116.62 → 2117.32] really important that
[2117.32 → 2118.52] is being improved by
[2118.52 → 2119.70] this that's the
[2119.70 → 2120.30] reason why I
[2120.30 → 2121.30] ported my software
[2121.30 → 2122.86] interface to react
[2122.86 → 2124.24] because I can use
[2124.24 → 2125.28] storybook auto
[2125.28 → 2126.12] reloading well I'm
[2126.12 → 2126.60] not using auto
[2126.60 → 2127.46] reloading but at
[2127.46 → 2128.02] the least things like
[2128.02 → 2129.28] storybook to develop
[2129.28 → 2130.06] your components in
[2130.06 → 2131.36] isolation that's a
[2131.36 → 2132.08] huge speed
[2132.08 → 2134.22] improvement and
[2134.22 → 2135.52] yeah to come back
[2135.52 → 2136.98] to Gatsby I think
[2136.98 → 2138.66] that it's making
[2138.66 → 2139.58] out of the box most
[2139.58 → 2140.42] of what I wanted for
[2140.42 → 2141.56] my website, so I
[2141.56 → 2142.98] went with it and
[2142.98 → 2144.24] the thing that I
[2144.24 → 2145.06] like is that if at
[2145.06 → 2145.94] some point I want to
[2145.94 → 2146.90] scale the website
[2146.90 → 2148.46] more I'm not a
[2148.46 → 2149.28] afraid because it's
[2149.28 → 2150.32] based on react I
[2150.32 → 2151.78] know that there is
[2151.78 → 2152.56] an ecosystem around
[2152.56 → 2154.06] it I know that if I
[2154.06 → 2155.58] want to add some I
[2155.58 → 2155.92] don't know for
[2155.92 → 2157.50] example a part of
[2157.50 → 2158.30] the website where
[2158.30 → 2159.12] you have to be
[2159.12 → 2161.38] sign up you can do
[2161.38 → 2162.50] it because at the
[2162.50 → 2163.32] end it's its all
[2163.32 → 2165.04] react and still it's
[2165.04 → 2165.78] server side rendered
[2165.78 → 2167.14] so I get something
[2167.14 → 2168.46] that is blazing
[2168.46 → 2170.50] fast yeah yeah it
[2170.50 → 2172.22] is amazing how fast
[2172.22 → 2173.18] Gatsby sites are and
[2173.18 → 2173.82] they're doing a lot
[2173.82 → 2174.52] more than just the
[2174.52 → 2175.28] server side rendering
[2175.28 → 2176.16] there they're doing a
[2176.16 → 2177.72] lot or sorry a lot
[2177.72 → 2179.16] of the pre rendering
[2179.16 → 2180.76] like they're really
[2180.76 → 2182.20] emphasizing how do we
[2182.20 → 2183.34] optimize this to make
[2183.34 → 2184.50] it superfast
[2184.50 → 2195.36] this episode is brought
[2195.36 → 2196.18] to you by Keen
[2196.18 → 2197.28] Keen makes customer
[2197.28 → 2198.34] facing metrics simple
[2198.34 → 2199.74] it's a platform that
[2199.74 → 2200.96] gives you powerful in
[2200.96 → 2202.44] product analytics fast
[2202.44 → 2203.42] with minimal development
[2203.42 → 2204.92] time for example a
[2204.92 → 2206.22] DIY solution to build
[2206.22 → 2206.98] out customer facing
[2206.98 → 2207.94] metrics in your product
[2207.94 → 2208.82] could take six months
[2208.82 → 2209.92] or more and with Keen
[2209.92 → 2210.52] you can be up and
[2210.52 → 2211.02] running in the same
[2211.02 → 2212.28] day the Keen platform
[2212.28 → 2213.30] lets you stream events
[2213.30 → 2214.56] to easily collect and
[2214.56 → 2215.40] enrich your data
[2215.40 → 2216.84] compute with embeddable
[2216.84 → 2218.32] answers insights and
[2218.32 → 2220.04] metrics access controls
[2220.04 → 2220.80] so you can design
[2220.80 → 2222.06] role-based access to
[2222.06 → 2223.44] your data and of
[2223.44 → 2224.74] course a visualization
[2224.74 → 2225.68] layer to create
[2225.68 → 2227.14] stunning charts and we
[2227.14 → 2228.22] have a special offer
[2228.22 → 2229.06] just for our JS
[2229.06 → 2230.58] party listeners go to
[2230.58 → 2232.14] Keen.io slash JS
[2232.14 → 2233.20] party and get your
[2233.20 → 2234.68] first 30 days of Keen
[2234.68 → 2236.10] for free and as a
[2236.10 → 2237.30] bonus for checking out
[2237.30 → 2238.72] a 15-minute demo of
[2238.72 → 2239.62] Keen's customer facing
[2239.62 → 2240.70] metrics they'll send you
[2240.70 → 2242.38] a free Keen t-shirt go
[2242.38 → 2244.02] to Keen.io slash JS
[2244.02 → 2245.88] party again Keen.io
[2245.88 → 2246.88] slash JS party
[2246.88 → 2261.12] want to swing back now
[2261.12 → 2261.80] so we're talking about
[2261.80 → 2262.50] the importance of
[2262.50 → 2263.64] auto reload and that
[2263.64 → 2264.48] kind of fast iteration
[2264.48 → 2265.64] when you're working in
[2265.64 → 2266.80] your C++ code base
[2266.80 → 2268.56] is there a way to
[2268.56 → 2269.42] hook it up so that you
[2269.42 → 2270.70] get automatic recompile
[2270.70 → 2272.12] and changing or like
[2272.12 → 2273.02] how does that end up
[2273.02 → 2273.34] working?
[2273.34 → 2274.12] At some point I'd
[2274.12 → 2275.56] like to have the
[2275.56 → 2277.62] compiler running after
[2277.62 → 2279.22] every change that would
[2279.22 → 2280.16] be possible basically
[2280.16 → 2283.14] the compilation is
[2283.14 → 2286.00] there is a package
[2286.00 → 2287.50] .Jason that is running
[2287.50 → 2288.96] scripted and compiling
[2288.96 → 2290.92] the C++ to the web
[2290.92 → 2292.20] assembly module, so I
[2292.20 → 2293.32] could more or less do
[2293.32 → 2294.76] my own watcher for files
[2294.76 → 2296.24] and rerun it every time
[2296.24 → 2297.56] I'm modifying something
[2297.56 → 2299.88] so right now my feedback
[2299.88 → 2301.36] loop is changing
[2301.36 → 2302.82] something in the C++
[2302.82 → 2304.28] code base I'm using
[2304.28 → 2305.70] VS Code that has a
[2305.70 → 2306.30] good integration
[2306.30 → 2307.20] actually with C++
[2307.20 → 2308.94] so I can even get
[2308.94 → 2310.50] errors directly in VS
[2310.50 → 2311.84] code so that's the
[2311.84 → 2313.04] first thing that is
[2313.04 → 2313.82] important to get the
[2313.82 → 2314.88] errors displayed in your
[2314.88 → 2316.48] editor so you're not
[2316.48 → 2317.58] getting you know C++
[2317.58 → 2319.12] you can get errors at
[2319.12 → 2320.28] compilation that takes
[2320.28 → 2322.14] your whole terminal so
[2322.14 → 2324.32] having a good idea to
[2324.32 → 2325.72] start is I guess the
[2325.72 → 2327.62] main thing and then I
[2327.62 → 2328.98] have a terminal I run
[2328.98 → 2330.96] the NPM run build
[2330.96 → 2333.06] then the test just after
[2333.06 → 2336.18] and then I can when the
[2336.18 → 2338.46] tests are passing its
[2338.46 → 2340.04] copied to the
[2340.04 → 2341.20] node modules of my
[2341.20 → 2343.10] react application and at
[2343.10 → 2344.28] this moment as there was a
[2344.28 → 2346.20] change the app is reloading
[2346.20 → 2348.86] so it's still longer that I
[2348.86 → 2350.38] would like to, but it's not
[2350.38 → 2352.32] that bad because I remember
[2352.32 → 2354.08] doing a change in C++
[2354.08 → 2356.46] then we're compiling the
[2356.46 → 2357.84] whole thing for a few
[2357.84 → 2359.24] seconds when you're lucky
[2359.24 → 2361.10] then running the native
[2361.10 → 2363.38] application going to the
[2363.38 → 2364.66] page well not the page
[2364.66 → 2366.00] the screen where you want
[2366.00 → 2367.24] to test and see that oh
[2367.24 → 2368.58] no that I made the silly
[2368.58 → 2369.74] mistake let's start again
[2369.74 → 2372.92] no I have less this because
[2372.92 → 2374.52] as my C++ code is more or
[2374.52 → 2376.00] less my business logic I can
[2376.00 → 2377.82] test it faster using test
[2377.82 → 2379.48] auto unit test and the
[2379.48 → 2380.68] interface is done in a
[2380.68 → 2381.56] react I can use something
[2381.56 → 2382.78] like storybook and I have
[2382.78 → 2383.52] my component display
[2383.52 → 2386.54] directly, so I'm I'm much
[2386.54 → 2388.80] faster at writing
[2388.80 → 2391.22] components interface and
[2391.22 → 2393.34] I'm equally fast as
[2393.34 → 2394.80] writing C++ for business
[2394.80 → 2396.38] logic yeah you kind of get
[2396.38 → 2397.26] the best of both worlds
[2397.26 → 2399.94] there yeah yeah I guess
[2399.94 → 2401.82] that once you are okay
[2401.82 → 2402.92] with the go chat that I
[2402.92 → 2405.14] told you get the best of
[2405.14 → 2406.60] both worlds that's what I
[2406.60 → 2407.86] want to show in my talk
[2407.86 → 2409.44] not saying that you will
[2409.44 → 2410.74] have a great experience all
[2410.74 → 2412.82] the time, but that's
[2412.82 → 2413.66] that's something that is
[2413.66 → 2414.68] working that's working
[2414.68 → 2416.38] yeah when I've seen you
[2416.38 → 2417.04] know talking about the
[2417.04 → 2417.88] build step so it sounds
[2417.88 → 2418.58] like you have a manual
[2418.58 → 2420.26] build still, but I've seen
[2420.26 → 2421.82] people do like webpack
[2421.82 → 2423.82] integration just essentially
[2423.82 → 2425.72] pulling in C++ or rust
[2425.72 → 2428.36] stuff as modules into
[2428.36 → 2429.86] directly into webpack I have
[2429.86 → 2430.78] to check that that's
[2430.78 → 2431.74] surely possible especially
[2431.74 → 2433.66] for a language like rust or
[2433.66 → 2434.68] any new language that
[2434.68 → 2435.74] compiled to web assembly
[2435.74 → 2437.78] they have a something to
[2437.78 → 2439.86] play on the side of
[2439.86 → 2440.94] integration with JavaScript
[2440.94 → 2443.76] yeah I'm using create react
[2443.76 → 2446.00] app for for the
[2446.00 → 2448.08] react application I highly
[2448.08 → 2449.60] recommend it I don't want
[2449.60 → 2451.84] to to to mess too much
[2451.84 → 2453.12] with the initial setup I
[2453.12 → 2454.08] want to be able to upgrade
[2454.08 → 2455.88] it easily that's why I'm
[2455.88 → 2457.72] okay with having a manual
[2457.72 → 2459.32] build step that I launch
[2459.32 → 2460.42] but even this I could
[2460.42 → 2461.90] improve I could do a watcher
[2461.90 → 2464.46] by myself or maybe
[2464.46 → 2465.72] later there will be some
[2465.72 → 2467.64] kind of integration with
[2467.64 → 2469.60] between a script and webpack
[2469.60 → 2471.06] you know we'll see I
[2471.06 → 2472.68] haven't looked at the
[2472.68 → 2473.78] newer versions of create
[2473.78 → 2474.82] react because I've been
[2474.82 → 2476.02] more in the view ecosystem
[2476.02 → 2477.24] recently do they still
[2477.24 → 2478.38] require you to eject to
[2478.38 → 2479.92] customize the webpack
[2479.92 → 2481.16] configure do they use the
[2481.16 → 2483.86] webpack compose, so I don't
[2483.86 → 2484.86] think they are using webpack
[2484.86 → 2485.90] compose I would have to
[2485.90 → 2487.46] check to be sure but then
[2487.46 → 2489.78] no you can use a label
[2489.78 → 2491.82] macros so for example I've
[2491.82 → 2493.28] been hiding internationally
[2493.28 → 2495.36] internationalization sorry to
[2495.36 → 2498.60] the to the app and
[2498.60 → 2501.04] I've been using JS
[2501.04 → 2503.36] lingua which is using some
[2503.36 → 2505.10] label macros to have you
[2505.10 → 2506.52] so that you are able to use
[2506.52 → 2507.90] a component inside your
[2507.90 → 2508.98] application to translate
[2508.98 → 2512.28] strings and basically they
[2512.28 → 2515.14] are changing the AST they're
[2515.14 → 2516.30] passing the JavaScript and
[2516.30 → 2517.74] changing the AST that's all
[2517.74 → 2519.04] done using macros and without
[2519.04 → 2520.64] ejecting that's cool yeah I
[2520.64 → 2522.36] love the way that essentially
[2522.36 → 2524.12] like meta programming in the
[2524.12 → 2525.28] JavaScript ecosystem is
[2525.28 → 2526.64] growing up because we're
[2526.64 → 2527.84] now addressing things that
[2527.84 → 2528.52] you know there's the
[2528.52 → 2529.46] application layer but then
[2529.46 → 2530.56] there's even this compilation
[2530.56 → 2532.14] layer we're using it to do
[2532.14 → 2534.34] things like JSX babble macros
[2534.34 → 2535.70] all this other fun stuff that
[2535.70 → 2537.50] is you know kind of compile
[2537.50 → 2540.34] time abstractions yeah there
[2540.34 → 2542.76] is I'm not sure if it's some
[2542.76 → 2544.24] new year language like maybe
[2544.24 → 2546.52] it's reason ML or other
[2546.52 → 2548.50] language that for sure they are
[2548.50 → 2551.62] allowing you to extend the
[2551.62 → 2554.52] syntax by manipulating the AST of
[2554.52 → 2556.10] the of the language so
[2556.10 → 2557.46] basically it's an it's a meta
[2557.46 → 2558.46] language that you can create
[2558.46 → 2559.22] you can create your own
[2559.22 → 2560.16] language in the language I
[2560.16 → 2562.18] think that's very powerful and
[2562.18 → 2563.48] something that we are starting
[2563.48 → 2564.58] to see in the JavaScript
[2564.58 → 2566.68] ecosystem at least it was very
[2566.68 → 2568.22] convenient because I didn't
[2568.22 → 2569.76] have to eject for using the
[2569.76 → 2573.02] translation component and so
[2573.02 → 2574.74] there is the result is very
[2574.74 → 2576.62] lightweight yeah no I love this I
[2577.42 → 2578.62] used to do a lot of creating
[2578.62 → 2580.00] creating these domain specific
[2580.00 → 2582.34] languages using Ruby but there
[2582.34 → 2584.40] it's all runtime, and it's Ruby
[2584.40 → 2587.06] which is slower here we can do
[2587.06 → 2589.06] it at compile time using Babel and
[2589.06 → 2590.48] it's lightning fast, and you get
[2590.48 → 2592.72] you know Rust has this idea of
[2592.72 → 2594.18] cost-free abstractions that's
[2594.18 → 2595.42] basically what this is it has a
[2595.42 → 2597.34] cost but only a compile time yeah
[2597.34 → 2600.22] that's great and yeah they have
[2600.22 → 2602.54] been the in a way that the
[2602.54 → 2604.36] template metabrogramming in C++
[2604.36 → 2608.08] was the same idea, but it's super I
[2608.08 → 2612.10] mean super easy to use, so I'd like
[2612.10 → 2614.10] to most of the time I'm avoiding to
[2614.10 → 2617.16] to do it in my own con base it's
[2617.16 → 2619.76] super, super convenient for libraries
[2619.76 → 2623.40] but also a pain to use yeah and the
[2623.40 → 2628.72] pain to debug yeah well, and I mean it
[2628.72 → 2630.16] sounds like pain to debug is kind of a
[2630.16 → 2631.82] theme as we go along when you start
[2631.82 → 2633.38] moving if you're starting from the web
[2633.38 → 2634.58] and you're used to the tooling that's
[2634.58 → 2635.70] available on the web it's funny
[2635.70 → 2637.52] because we used to say oh you know
[2637.52 → 2639.44] console log debugging became a thing
[2639.44 → 2641.10] because the tools was so bad now the
[2641.10 → 2642.42] tools on the web are so good that
[2642.42 → 2644.02] anytime you kind of go away from it
[2644.02 → 2646.54] you're like wow I miss my you mean I
[2646.54 → 2649.00] can't add the breakpoints without
[2649.00 → 2652.14] recompiling that's strange but this
[2652.14 → 2654.02] being said if you've never tried for
[2654.02 → 2655.66] example native development and mobile
[2655.66 → 2659.08] the experience is also pretty good if
[2659.08 → 2661.60] you start Xcode or Android Studio so
[2661.60 → 2663.80] things have to be good things have to be
[2663.80 → 2666.32] picked up from both worlds yeah
[2666.32 → 2669.82] absolutely awesome anything else come
[2669.82 → 2671.30] into mind you want to chat about before
[2671.30 → 2675.32] we wrap up nothing much just check out
[2675.32 → 2678.02] develop it's my game engine it's for
[2678.02 → 2680.90] people it's for anyone because of the
[2680.90 → 2683.06] visual programming system anyone can jump
[2683.06 → 2685.26] into software and start making games so
[2685.26 → 2687.64] make sure to check it out, and it's all
[2687.64 → 2689.18] open source it's all open source you want
[2689.18 → 2692.30] to see a practical example of compiling
[2692.30 → 2694.42] web assembly using that integrating it
[2694.42 → 2696.72] with JavaScript and application there you
[2696.72 → 2699.24] go develop exactly awesome thank you so
[2699.24 → 2702.80] much Florian thanks, thanks a lot all
[2702.80 → 2704.36] right thank you for tuning in to JS party
[2704.36 → 2707.88] this week tuning live on Thursdays at 1 p.m.
[2707.92 → 2710.64] us eastern at changelog.com slash live join
[2710.64 → 2713.20] the community and slack with us in real time
[2713.20 → 2715.38] during the shows head to changelog.com slash
[2715.38 → 2717.54] community and do us a favour share this
[2717.54 → 2719.18] show with a friend, or you don't have a
[2719.18 → 2721.66] podcast go into overcast and favourite it
[2721.66 → 2723.92] and thank you to fast our bandwidth
[2723.92 → 2726.26] partner head to fastly.com to learn more
[2726.26 → 2728.12] and we move fast to fix things around here
[2728.12 → 2729.98] at changelog because of Rollbar check them
[2729.98 → 2732.62] out at rollbar.com we're hosted on leno
[2732.62 → 2735.00] cloud servers head to leno.com slash
[2735.00 → 2736.66] changelog check them out and support this
[2736.66 → 2738.94] show our music is produced by break master
[2738.94 → 2741.08] cylinder, and you can find more shows just
[2741.08 → 2743.42] like this at changelog.com thanks for
[2743.42 → 2744.98] tuning in we'll see you next week
[2744.98 → 2750.70] by main Hornet
[2750.70 → 2754.38] let's see you next week
[2754.38 → 2755.32] in the CENTO
[2755.32 → 2757.72] is
[2757.72 → 2762.16] every
[2762.16 → 2763.54] number
[2763.54 → 2764.00] back
[2764.00 → 2766.80] out
[2767.02 → 2767.58] to
[2767.58 → 2769.68] our
