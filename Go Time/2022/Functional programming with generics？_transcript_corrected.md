[0.00 → 15.26] As someone who has written a library to do a bunch of FP things, not only did it make the implementation easier in the form of less code and more guarantees at compile time about types, it extends those guarantees to the caller.
[15.26 → 36.52] So I no longer have to take in an interface or a list of any types and return a list of any types from map. And since now I can return the type parameter T and then a new type parameter for the return type of the list, well now those guarantees are extended to the user of the library.
[36.52 → 54.36] And now they can also say, oh, well, my program compiles, therefore my types are right too. So this is like a domino effect of benefits that if a user is using someone's FP library or even rolled their own, now they know that, well, my types are right.
[54.36 → 66.40] This episode is brought to you by Source graph. Source graph is universal code search to let you move fast, even in big code bases.
[66.90 → 73.66] Here's CTO and co-founder, Bung Lu, explaining how Source graph helps you to get into that ideal state of flow in coding.
[73.66 → 89.14] The ideal state of software development is really being in that state of flow. It's that state where all the relevant context and information that you need to build whatever feature or bug that you're focused on building or fixing at the moment, that's all readily available.
[89.30 → 94.68] Now the question is, how do you get into that state where, you know, you don't know anything about the code necessarily that you're going to modify?
[94.68 → 104.14] That's where Source graph comes in. And so what you do with Source graph is you jump into Source graph. It provides a single portal into that universe of code.
[104.30 → 110.98] You search for the string literal, the pattern, whatever it is you're looking for. You dive right into the specific part of code that you want to understand.
[111.26 → 124.10] And then you have all these code navigation capabilities, jump to definition, find references that work across repository boundaries that work without having to clone the code to your local machine and set up and mess around with editor config and all that.
[124.10 → 129.56] Everything is just designed to be seamless and to aid in that task of, you know, code spelunking or source diving.
[129.88 → 137.74] And once you've acquired that understanding, then you can hop back in your editor, dive right back into that flow state of, hey, all the information I need is readily accessible.
[137.96 → 142.44] Let me just focus on writing the code that influenced the feature or fixes the bug that I'm working on.
[142.44 → 152.44] All right, learn more at Sourcegraph.com and also check out their bi-monthly virtual series called DevToolTime covering all things DevTools at Sourcegraph.com slash DevToolTime.
[154.10 → 169.42] Let's do it.
[169.98 → 171.04] It's Go Time.
[171.62 → 176.42] Welcome to Go Time, your source for diverse discussions from all around the Go community.
[176.90 → 179.54] Check out our back catalogue at GoTime.fm.
[179.54 → 186.74] There you'll find the most popular episodes, our favourites, and a request form so you can let us know what you want to hear about on the pod.
[187.10 → 191.88] Special thanks to our partners at Vastly for shipping our shows superfast to wherever you listen.
[192.12 → 193.62] Check them out at Fastly.com.
[194.02 → 195.70] And to our friends at Fly.io.
[196.06 → 198.04] Host your app servers close to your users.
[198.30 → 199.16] No ops required.
[199.50 → 201.26] Learn more at Fly.io.
[201.52 → 202.28] Okay, here we go.
[203.56 → 206.22] Welcome, welcome, friends.
[206.22 → 209.16] And those who want to be friends.
[209.78 → 211.02] You want to be friends with me, right, Aaron?
[211.46 → 211.90] Of course.
[212.20 → 213.10] Why do you think I'm here?
[213.60 → 214.48] Awesome, awesome.
[215.08 → 220.44] So today we're going to talk about functional programming with generics.
[220.90 → 222.88] So I am your host, Johnny Portico.
[223.60 → 230.42] If you haven't heard from me for a while, that's because I've been heads down trying to ship some stuff that's coming out later this year.
[231.10 → 233.66] And I'm pretty excited about it, but I can't spill the beans on that yet.
[233.66 → 235.18] You're just going to have to stay tuned.
[235.76 → 238.54] And if you want, you can go to GolangJohnny.com.
[240.38 → 247.92] Since I own that, I made sure to snap that up the last time John Calhoun mentioned it on our show.
[248.38 → 252.12] So joining me today is, you know him, he's been on the show before.
[252.52 → 253.92] And you see his name everywhere.
[254.12 → 259.60] And especially as it relates to things like Gopher Con and getting us ready for the big show coming up next month, actually.
[259.82 → 260.26] Coming up.
[260.26 → 260.98] Yeah, yeah.
[261.10 → 264.14] Please join me in welcoming Aaron Schlesinger.
[264.70 → 265.30] Hi, everybody.
[265.56 → 266.56] Thanks for having me, Johnny.
[266.76 → 268.08] It's wonderful to be here again.
[268.46 → 269.06] Yes, yes.
[269.08 → 270.40] And it's great to have you.
[270.64 → 276.06] So we did a show on functional programming a little while back.
[276.34 → 278.72] This was episode 87, right?
[279.24 → 279.90] This was a while back.
[279.94 → 284.82] This was like May something of, let me see, let me double-check.
[285.40 → 287.14] 2019, back in 2019.
[287.54 → 288.34] Four days.
[288.34 → 291.66] So a lot's happened in the Go world since then, right?
[291.98 → 295.80] Most notably, the introduction of generics in 118, right?
[296.42 → 307.32] So it was suggested, actually, that there was a listener who basically went back and listened to the old show and basically said, hey, I found an episode on functional programming from back in 2019.
[307.60 → 310.12] However, it was a time before generics appeared in Go.
[310.48 → 314.88] It'd be nice to hear what can be done with functional programming and Go with generics.
[314.88 → 316.20] So this one's from Steve Nicholson.
[316.26 → 317.36] So, Steve, shout out to you.
[317.72 → 320.60] We indeed got this show put together on your suggestion.
[320.82 → 327.46] So the others you can follow in Steve's footsteps if you want to ask for certain shows.
[327.64 → 328.92] And you can basically suggest them.
[329.24 → 331.72] And we often look through the list and see what's interesting.
[331.72 → 333.28] And you tell us what you want to hear.
[333.46 → 335.70] And we put on shows like this as a result of that.
[335.98 → 340.60] So you and I, along with Matt, were basically, we did that episode.
[340.94 → 342.72] And we learned a lot during that time.
[342.82 → 349.88] We learned how to use what we had back then, mainly things like the empty interface and things like even generators, right?
[349.88 → 352.86] And things like that and even sort of using reflection, right?
[353.06 → 363.84] Because those were some of the things that really sort of enabled or facilitated the creation of functional programming and sort of style libraries and things like that or approaches to Go.
[364.22 → 369.38] But those were also some of the gripes, right, with trying to do functional programming in Go, right?
[369.48 → 371.02] Too much use of the empty interface.
[371.56 → 375.04] Too much use of, you know, sort of reflection on and on, right?
[375.04 → 380.66] And even the thinking that, well, Go is really for imperative programming, right?
[380.78 → 382.04] The verbose style, right?
[382.06 → 383.72] Not really suitable for functional programming.
[383.84 → 386.36] But I think we made a pretty good case for it, right?
[386.44 → 387.84] And listening back to the show.
[388.14 → 395.58] But now that we have generics, right, I wanted to bring you back so we can talk about what's easier now to do with Go.
[395.68 → 398.34] Like what was hard to do then that is easier to do now?
[398.72 → 398.92] Yeah.
[398.92 → 404.56] I think maybe we can do like a little bit of a recap of what FP is.
[404.56 → 415.80] That's actually a perfect introduction into, or I should maybe say segue into why generics can help and kind of answer your question too.
[416.30 → 423.24] Where did generics unlock new areas of functional programming awesomeness in Go, if you will?
[424.24 → 427.48] That's a technical term, awesomeness, just for all the listeners.
[428.22 → 433.54] So I'll give it a crack to start off, you know, the recap of functional programming.
[433.54 → 440.46] Really, you can go from a math perspective and say, you know, everything in FP is based on the function.
[441.06 → 446.32] And from a theoretical perspective, a function takes inputs and returns outputs.
[446.58 → 454.28] From a math perspective, right, you can chart a graph from a function, for example, just to map the inputs to the outputs.
[454.62 → 455.22] That's what it is.
[455.24 → 455.76] It's a mapping.
[455.76 → 460.14] In real life, of course, our functions don't just spit something back out.
[460.28 → 467.58] They also do some I.O. or maybe talk to a file or use a timer or send on a channel or whatever else.
[468.16 → 477.84] And so that's really important, actually, to remember that all of this stuff that we're going to talk about in functional programming comes from the theoretical.
[477.84 → 482.28] But when we apply it, it looks like a design pattern.
[482.52 → 487.58] It's not like adopting a framework or if you're in school, like doing an assignment.
[487.76 → 494.10] There's not just a right answer and a bunch of wrong answers or a right answer that everything else is just wrong.
[494.70 → 496.18] There are some gradients here.
[496.18 → 504.12] And we kind of saw that with the there have been talks on FP before, including one that I did way back in 2017.
[505.02 → 507.40] There's been talks at Gopher Con UK.
[507.72 → 510.58] There's another talk from Gopher Con in 2020.
[511.38 → 515.40] And obviously, like you said, Johnny, there 's's been previous go times.
[515.44 → 516.52] There's been blog posts.
[516.88 → 521.90] They all attack FP from a different perspective.
[521.90 → 522.58] Right.
[523.16 → 527.98] And it was all possible to do some FP things before generics.
[528.32 → 528.46] Right.
[528.52 → 532.24] So we were able to take some of the theory and apply it even before generics.
[532.62 → 537.16] Obviously, now generics has unlocked more stuff, and now we can unlock more things.
[538.14 → 541.76] So FP, the theory is things are based on the function.
[541.96 → 545.30] We can transform functions by putting two together.
[545.58 → 545.74] Right.
[545.74 → 556.16] So if the output of one gets passed into the input of a second one, now you essentially have a transitive property where you can input to the first one and get an output from the second one.
[556.16 → 558.10] And it all looks like one function.
[558.74 → 559.26] Composition.
[559.56 → 559.66] Right.
[559.98 → 561.28] You can curry functions.
[561.28 → 570.76] So you can think of it as partially applying a function, meaning if a function takes in three parameters, pass one of the parameters.
[570.76 → 573.82] And now you have a function that takes two parameters.
[574.14 → 578.28] And that first parameter that you already passed in is already baked into it.
[578.94 → 579.08] Right.
[579.68 → 585.84] Then you can take those tools and go to what I kind of think of as the next higher level.
[585.84 → 586.64] Right.
[586.72 → 594.42] So moving into the programming world, not just the math world, because all that stuff I just mentioned is basically just the math world.
[594.70 → 601.08] In the programming world, you can have sequences of things like a list or an array or in go a slice.
[601.78 → 609.02] So what if you could apply a function on every item in the slice without having to write a for loop?
[609.66 → 612.50] That's called in go and a lot of other languages.
[612.74 → 613.48] It's called a map.
[613.88 → 613.96] Right.
[613.96 → 618.10] You just apply the function on each element in the list.
[618.16 → 626.06] And then you get a new list out the other end that has the outputs of that function in the same indices as the respective inputs.
[626.46 → 630.14] So now starting to bend the mind a little bit.
[630.70 → 635.98] What if you had a function that took in an element of a list, but then output a list itself?
[636.80 → 636.96] Right.
[637.02 → 641.30] Now you can do something called a flat map where you take in an element.
[641.30 → 644.02] So you apply the function on each element.
[644.46 → 645.60] The output is a list.
[645.60 → 645.88] Right.
[645.88 → 651.22] So now you're taking a bunch of lists and combining them together to make a much bigger list.
[651.94 → 652.06] Right.
[652.10 → 656.14] So whereas before you were just dealing with input one element, output another element.
[656.52 → 663.48] Now you're inputting one element, outputting n elements for each element in the original list, and you end up with a much bigger list.
[663.48 → 669.34] Now you can go even further here, and you can start doing things like filtering.
[669.34 → 677.10] So if you have a function that takes in an element in the list and returns a Boolean, you can use that to decide, can I make a new list?
[677.24 → 681.46] And can I decide which elements from the original list are going to end up in the new list?
[681.82 → 693.66] You can also do things like zipping, which is using a function to determine the ordering of a final list given two or three or four or five or six or ten initial lists.
[693.66 → 694.26] Right.
[694.30 → 696.60] So you can determine how they're interspersed together.
[697.48 → 706.84] And I'm going to stop there, but there are a lot of other ways that we can sort of apply this very basic but powerful concept of a pure function.
[707.16 → 709.04] Just takes in an input and returns an output.
[709.42 → 711.26] Doesn't do IO or anything else.
[711.74 → 722.46] So this concept of a pure function and applying that into the programming world of maps and lists and other things, other data structures like trees and so forth.
[722.46 → 728.98] So forgive the overloading of the term list, but this list of things we can do, you know, it goes on.
[729.22 → 729.34] Right.
[729.40 → 731.80] And I could spend another hour and a half talking about it.
[731.84 → 733.42] Of course, I'm not going to do that.
[733.82 → 744.30] But the reason that I went into all that is to kind of start to talk about what could we do before and what can we do now with generics, with the addition of generics.
[744.60 → 748.90] And really, thinking about generics, this is another branch of math, right?
[748.90 → 752.10] We're talking about types here, statically defined types.
[752.30 → 761.24] And not only that, but now we're able to vary the type of the input of a function or the output of a function.
[761.68 → 764.58] We're able to vary that type based on a parameter.
[765.10 → 766.52] It's called type parameterization.
[766.52 → 777.60] So if we can do that, now we can write one function in Go, but we can have an infinite number of actual implementations of it because the type can change.
[777.60 → 784.26] So if you've got a function that takes in a type parameter or a parameter of type T, where T is a type parameter.
[784.96 → 788.94] Well, I can invent infinity types, right?
[789.38 → 799.66] So if I can invent infinity types, then that function can take in infinity different types of parameters, which means there are infinity different implementations of that function.
[800.36 → 806.10] And, you know, the Go compiler is going to figure out how to define actual implementations that take in those actual types.
[806.10 → 810.82] I don't have to worry about that anymore, which means I don't have to generate code or anything like that.
[811.24 → 815.06] But now that we have this power and this is immense amount of power.
[815.88 → 821.62] Now we can start to have things like, say, take the map example.
[822.24 → 829.78] We can start to have things like a single function called map that can operate on a list of any type.
[829.78 → 836.62] Instead of before, we had to have a function called map that only could operate on a list of one type.
[837.08 → 842.48] And we had to repeat the implementation of map over and over and over again for all our different lists.
[843.02 → 845.50] Now the compiler just does that for us like magic.
[845.78 → 846.66] Thank you, Go team.
[846.88 → 850.82] You all gave us this opportunity to save tons of generated code.
[850.92 → 851.58] And that's amazing.
[852.24 → 853.84] So that's kind of where we're at now.
[853.84 → 856.16] The implications of this go beyond map.
[856.86 → 874.78] But fundamentally, now we're at a point where instead of using interface, raw interfaces, or, you know, any type now, instead of doing reflection, now we can add compile time proof that certain functions will work for some definition of work.
[875.10 → 875.20] Right.
[875.62 → 880.20] We can prove via the type system that certain types of functions will work.
[880.70 → 881.98] Like map, for example.
[881.98 → 893.88] We don't have to wonder whether our reflection code or our type assertion on an empty interface does the right thing and figures out the right type of the list and then applies that to the function.
[894.28 → 908.12] Now we know that if our code compiles, that you've passed in the right function that takes in the right type for the type of elements in the list, and you will get back another list with the output type of that function.
[908.12 → 916.44] So if I'm hearing you correctly, it seems like now, so we're no longer arguing about the benefits of FP, right?
[916.52 → 923.98] So we've done a pretty good recap of why you'd want to introduce FP or at least know of its usefulness, right?
[924.10 → 925.32] In certain contexts.
[925.76 → 931.04] It's about now how easy is it to actually implement elegantly and go.
[931.04 → 932.70] And that's what generic gives us, right?
[932.74 → 937.72] Because like you said, there were FP libraries and talks and blog posts and everything.
[937.94 → 939.38] It was possible before.
[940.00 → 951.38] We just either had to write a lot of boilerplate ourselves or use, you know, go generate to produce, you know, a pile, a variance of a particular function to support the different types as many types as we wanted to support.
[951.88 → 952.12] Right.
[952.12 → 957.12] Or we had to do, you know, some voodoo with reflection to get to some type information.
[957.30 → 957.42] Right.
[957.74 → 965.16] So now it's about sort of the elegance, right, that we get to leverage, right, with type parameterization.
[965.46 → 966.66] Let's say that three times last.
[967.26 → 967.50] Yeah.
[968.90 → 969.30] Okay.
[969.40 → 981.62] So if I'm understanding correctly, then some of the libraries pre-generics, is it fair to say that you were going to see a lot of, at least for those who practice FP and are interested in practicing FP and doing FP in Go,
[981.62 → 985.58] which is something we'll touch on as a separate sort of thread, right, in our conversation.
[986.18 → 993.18] So we can expect that a lot of those FP libraries are going to start adopting generics because it just makes the implementation that much easier.
[993.60 → 993.88] Yeah.
[993.88 → 1009.22] I think as someone who has written a library to do a bunch of FP things, yeah, I saw not only did it make the implementation easier in the form of less code and more guarantees at compile time about types,
[1009.22 → 1015.86] but also it extends those guarantees to the caller, so the user of the library too.
[1016.46 → 1028.16] So, you know, like I said, I no longer have to take in an interface or any type and return an any type from, or a list of any types and return a list of any types from map.
[1028.16 → 1042.82] And since now I can return the type parameter T and then a new type parameter for the return type of the list, well, now those guarantees are extended to my user, the user of the library.
[1043.42 → 1048.82] And now they can also say, oh, well, my program compiles, therefore my types are right too.
[1048.82 → 1061.84] So this is like a domino effect of benefits that if a user is using someone's FP library or even rolled their own, now they know that, well, my types are right.
[1062.18 → 1065.84] They don't have to remember it's one less thing they have to keep in their head, right?
[1065.98 → 1072.16] That, oh, well, the input should be a slice of into and return should be a slice of strings.
[1072.16 → 1081.14] But all a compiler knew about in the past was it's just an empty interface or maybe a little better, a slice of empty interfaces or something like that.
[1081.56 → 1083.70] It is simplicity, but it is benefit too.
[1084.28 → 1093.18] So I was looking at sort of the how Go sort of provides this, or how Go talks about sort of this instantiation, right, of a generic function.
[1093.18 → 1104.14] So for those who haven't sort of gotten into generic setting Go, pretty much when you create a generic function, what you're basically saying is that you're going to support a number of types, right, based on the typeset information you provide.
[1104.60 → 1113.06] And basically what happens behind the scenes when you compile your code is that Go is going to generate an instance, right, of your function for each of the types you say you support, right?
[1113.18 → 1121.96] So it's kind of like an actual code generation that basically that we have that provides a type safety, the type checks, right, that the compiler is able to provide.
[1121.96 → 1128.14] But now the language itself is actually producing that for you behind the scenes, and you don't have to actually write your own generators, right?
[1128.34 → 1133.58] So effectively you're doing the exact same thing you were doing before, except now it's basically baked and supported to the language, right?
[1133.80 → 1142.54] So this is an efficiency game, right, in terms of you, the programmer, being able to write these libraries, being able to support multiple types of given functions and things.
[1142.72 → 1147.80] This is an efficiency game, really, not really a game changer for functional programming and Go per se.
[1147.80 → 1152.38] I think just a more efficient way of writing the functions, basically.
[1152.80 → 1162.06] Yeah, that is a really great point is that everything we can do now, technically you could do before because we had the empty interface, right?
[1162.38 → 1167.50] The empty interface is the set of all types, all possible types in this context.
[1167.50 → 1174.36] So you could have a function that take in an empty interface and that is a function that can take in anything you can come up with, right?
[1174.50 → 1179.98] Same thing, it can return if you have the empty interface return, and it can be the set of anything.
[1179.98 → 1188.28] So your task before was written the code to define a subset of all things that your function wants to deal with.
[1188.70 → 1191.84] Now there is a massive efficiency gain, right?
[1191.94 → 1203.58] Because now you can constrain a type parameter and have the compiler compute for you whether a given type for a type parameter that has constraints on it is legal.
[1203.58 → 1213.58] So do you want it to be integral or do you want it to be comparable or do you want it to be stringable or anything else under the sun that we can come up with?
[1214.08 → 1217.26] You write less than a line of code, right?
[1217.42 → 1222.26] And maybe you write a new constraint somewhere, and then you apply it on your type parameter.
[1222.94 → 1232.02] And the compiler does what I consider a very advanced and very useful computation for you across your entire code base.
[1232.02 → 1237.84] And if you're writing a library, across everyone's entire code base that uses it, which is pretty amazing.
[1238.00 → 1238.38] It's awful.
[1238.76 → 1239.00] Yeah.
[1239.20 → 1239.92] That is amazing.
[1258.62 → 1261.40] This episode is brought to you by Honeycomb.
[1261.40 → 1263.88] Find your most perplexing application issues.
[1264.18 → 1271.10] Honeycomb is a fast analysis tool that reveals the truth about every aspect of your application in production.
[1271.58 → 1275.56] Find out how users experience your code in complex and unpredictable environments.
[1275.86 → 1280.76] Find patterns and outliers across billions of rows of data and definitively solve your problems.
[1281.20 → 1282.68] And we use Honeycomb here at Change.
[1282.72 → 1286.52] Well, that's why we welcome the opportunity to add them as one of our infrastructure partners.
[1286.52 → 1294.36] In particular, we use Honeycomb to track down CDN issues recently, which we talked about at length on the Kaiden edition of the Ship It podcast.
[1294.62 → 1295.30] So check that out.
[1295.52 → 1296.02] Here's the thing.
[1296.26 → 1299.52] Teams who don't use Honeycomb are forced to find the needle in the haystack.
[1299.52 → 1302.80] They scroll through endless dashboards playing whack-a-mole.
[1303.00 → 1306.06] They deal with alert floods, trying to guess which one matters.
[1306.44 → 1311.64] And they go from tool to tool playing sleuth, trying to figure out how all the puzzle pieces fit together.
[1312.00 → 1318.32] It's this context switching and tool sprawl that are slowly killing teams' effectiveness and ultimately hindering their business.
[1318.32 → 1325.48] With Honeycomb, you get a fast, unified, and clear understanding of the one thing driving your business.
[1325.74 → 1326.16] Production.
[1326.66 → 1329.16] With Honeycomb, you guess less and you know more.
[1329.56 → 1334.74] Join the swarm and try Honeycomb free today at honeycomb.io slash changelog.
[1334.90 → 1338.36] Again, honeycomb.io slash changelog.
[1348.32 → 1358.32] How do you think you're going to be able to do this?
[1358.32 → 1368.64] So the Go team has been very vocal and deliberate about advising pretty much everybody to not go gang busters, which is on other things.
[1369.30 → 1372.02] Not use it as a hammer with everything being a nail.
[1372.24 → 1373.68] Just don't spread it everywhere.
[1373.68 → 1377.20] Where it's a very sort of cautious approach, right?
[1377.24 → 1383.82] Until some of the best practices start to emerge and still can see the sort of best use cases for generics in Go.
[1384.14 → 1390.34] Do you think that applies even more so for those who want to practice functional programming in Go?
[1390.46 → 1394.80] Or do you think, actually, it makes our lives a lot easier.
[1394.92 → 1395.78] Let's just go full level.
[1396.54 → 1399.34] Well, that is good advice for all software.
[1399.84 → 1402.24] So yes, the answer to your question is yes.
[1402.72 → 1402.84] Right.
[1402.84 → 1411.54] There is no telling right now whether map is enough, right?
[1411.72 → 1413.20] Or no one wants to use it.
[1413.56 → 1423.02] And if people do want to use map, there's no telling whether the parallel version of that is better or complementary to the regular serial version of map, for example.
[1423.02 → 1423.52] Right.
[1423.52 → 1438.68] So the parallel version for listeners would be instead of applying the function on every element of the list one after the other, it's applying them in parallel with X number of Go routines or at least concurrently with X number of Go routines and then returning the result.
[1439.18 → 1439.32] Right.
[1439.32 → 1442.86] There's no telling right now.
[1443.06 → 1445.14] You can say this is correct.
[1445.14 → 1446.74] You can say this is possible.
[1447.10 → 1454.00] You can guess this might be useful for this case or this case or this type of software or that type of software.
[1454.00 → 1459.30] But there's no substitute for usage in the wild in the community, if you will.
[1459.72 → 1461.60] There's just no substitute.
[1461.60 → 1463.74] So these things should be tried.
[1464.32 → 1473.14] Maybe, you know, we should go a little crazy, as they say, as the Go team has said, a little overboard to see what is possible.
[1473.14 → 1478.08] But we should not say that this is the result.
[1478.32 → 1481.00] This is the solution to all problems in FP.
[1481.48 → 1492.64] We should get these things out there, play around with them, experiment with them, see what works at a larger scale, and then say that is the solution to problems X, Y, and Z.
[1493.12 → 1496.02] You know, this is why we all say we test in production, right?
[1496.24 → 1501.04] Because there's no substitute for real world use cases.
[1501.04 → 1501.40] Yeah.
[1501.40 → 1503.46] In that case, it's data.
[1503.72 → 1510.52] And in our case, it's programmers experimenting with things and seeing what actually works in real world code bases.
[1510.72 → 1511.68] But it's the same effect.
[1512.62 → 1517.38] So picking back off of that, the thread that we paused, and now I want us to resume.
[1517.92 → 1518.68] You see what I did there?
[1519.36 → 1519.96] I do.
[1520.20 → 1520.70] I do.
[1520.88 → 1521.44] I love it.
[1522.66 → 1528.32] The idea of basically when to use generics, right?
[1528.32 → 1531.24] And in our case here, when to use functional programming.
[1531.24 → 1534.96] I think that's a fair question to ask whether, you know, regardless of generics, right?
[1535.02 → 1545.62] So one of the sort of the strong gripes that I found out there, right, that I've heard even in talking to some folks is that, look, Go is imperative, right?
[1545.62 → 1546.58] Through and through, right?
[1546.70 → 1553.68] We're kind of side bending and kind of pushing it in a direction it wasn't meant to, right?
[1553.68 → 1558.62] Even though some of its features and its capabilities are well suited, right, for functional programming.
[1558.80 → 1562.52] You know, functions being first class citizens and et cetera, et cetera.
[1562.68 → 1566.46] A lot of the sort of the things you look for in functional programming, you can do and go.
[1566.46 → 1569.04] But just because you can don't mean you should, right?
[1569.08 → 1570.00] That whole adage, right?
[1570.24 → 1583.20] So is functional programming still in the realm of sort of experimentation and just people who are curious, and they can play around with it, but really like at work or whatever, right?
[1583.26 → 1585.52] You know, you don't they don't really use it, right?
[1585.52 → 1589.40] Like, where are we in terms of really, I guess it's an adoption question, right?
[1589.48 → 1597.46] Like, are people interested or increasingly more so interested in using FP now, even with the bells and whistles that are enabled right through generics?
[1598.04 → 1605.04] Is FP attractive enough for people who are traditionally doing this imperative style, especially in the world of Go?
[1605.68 → 1610.54] Should they be looking, or really should we try to bring FP into our production code?
[1611.00 → 1611.86] Well, it's already here.
[1611.86 → 1618.40] Anyone who uses context is using a part of FP, right?
[1618.48 → 1622.64] Because context has a with cancel and with timeout.
[1622.76 → 1625.34] Those return a function, right?
[1625.50 → 1627.80] This is how pervasive FP is.
[1627.92 → 1632.96] That is technically a higher order function because it's a function returning.
[1633.16 → 1639.32] With cancel is a function and that's returning a function that you call to close to free the resources.
[1639.32 → 1644.82] There's an internal Go routine running, right, with a timer and, you know, and freeze that resource, right?
[1645.26 → 1645.94] That is FP.
[1646.08 → 1659.52] And I think like all technologies that are used by more than a trivial number of people in the world, a corner of this technology is used a lot, right?
[1660.10 → 1662.08] SQL is another good example here.
[1662.36 → 1664.20] You can do many, many things with SQL.
[1664.20 → 1669.64] You can turn Postgres SQL or PostgreSQL, is that how you say it, right?
[1670.04 → 1670.56] Yeah, yeah.
[1670.60 → 1671.12] I'll allow it.
[1671.74 → 1672.14] Okay.
[1672.48 → 1672.76] Yeah.
[1672.84 → 1673.10] Okay.
[1673.14 → 1674.72] It's got the Johnny stamp of approval.
[1675.38 → 1680.46] You can turn PostgreSQL into a time series database if you want to, for example, right?
[1680.46 → 1683.48] By using very advanced features of SQL.
[1683.76 → 1689.50] But not many people do that because obviously it's not the a lot of times it's not the best tool for the job.
[1689.62 → 1700.04] But also most people prefer, including myself, to stick with a smaller set of foundational features of the technology.
[1700.64 → 1703.16] And same thing with FP, right?
[1703.16 → 1706.86] There is a smaller set than even all the stuff that I said today.
[1707.40 → 1712.54] There's a smaller set of functionality that most people prefer to use.
[1712.64 → 1721.42] And my hypothesis for why that is, is because it makes more sense, and it fits into more workloads, right?
[1721.42 → 1734.60] And so if you need to capture some state of a function and expose one operation on that state to the caller, using a higher order function makes a lot of sense.
[1734.94 → 1741.88] It's a lot easier than doing a bunch of boilerplate and building a whole struct and storing the state in the struct and having a bunch of methods on it.
[1741.88 → 1750.92] And that, it just fits right into that use case, and it applies, that use case is applicable and exists on a ton of workloads.
[1751.08 → 1752.90] And so we use it, right?
[1752.98 → 1756.28] So FP, strictly speaking, is, is everywhere.
[1756.76 → 1760.46] Now I'm going to modify your second question a little bit accordingly.
[1760.90 → 1764.44] You said, should we be trying to get FP into more workloads?
[1764.44 → 1773.68] Well, given that it's already a lot of places, I'm going to modify it and say, should we get more features of FP into more workloads?
[1774.30 → 1775.42] Will you allow that?
[1776.86 → 1777.98] Yeah, yeah, let's do it.
[1778.50 → 1779.58] Yeah, tell me more.
[1779.92 → 1781.70] All right, so now we've got the seal on that.
[1781.94 → 1782.18] All right.
[1782.92 → 1789.16] And so the way that I think about it is tried to model it as the imperative declarative difference, I guess.
[1789.38 → 1791.84] There's a fundamental difference between imperative and declarative.
[1791.84 → 1795.72] You can see it with SQL versus Go, right?
[1795.82 → 1801.22] Because SQL, you say, dear database, this is the result that I want.
[1801.30 → 1813.38] And then the database has a ton of usually very clever implementation to figure out how to get whatever the way that it represents the data on disk into the result that you want.
[1813.78 → 1814.00] Right?
[1814.06 → 1818.28] So you can filter, you can join, you can group, you can order, et cetera, et cetera, et cetera.
[1818.28 → 1824.36] Now, in the FP world, let's just take this map example I keep using.
[1825.10 → 1825.20] Right?
[1825.30 → 1835.72] So with map, the intention is to take a function, apply it onto every element of the list, the slice, and then return a new slice with the results.
[1836.18 → 1839.28] You might return the same slice with the new results.
[1839.42 → 1841.74] That's also sometimes legal as well.
[1841.74 → 1846.76] But let's just say for sake of logic, we're returning a new slice with new results.
[1847.26 → 1849.52] Well, we're iterating through a list.
[1849.58 → 1850.50] So that's a for loop.
[1850.86 → 1852.00] That's just what it is.
[1852.14 → 1852.26] Right?
[1852.64 → 1853.86] We can write a for loop.
[1854.08 → 1855.22] And that's the imperative way.
[1855.28 → 1862.48] It's telling the machine to go through the list one by one, call this function every time, put the result into a new list.
[1862.48 → 1868.10] Or the other way is someone else did that for you, and you just call map.
[1868.62 → 1870.52] And that's the kind of declarative way.
[1870.98 → 1877.06] Because when you call map, you're effectively saying, like with SQL, you're saying this is the data that I want back.
[1877.52 → 1884.66] With map, you're saying I want a new list back with the results of the old list applied at the function that I gave to map.
[1885.14 → 1885.38] Right?
[1885.44 → 1886.48] And that's pretty much it.
[1886.48 → 1887.38] Right?
[1887.48 → 1907.98] So when we think about this question of should we get more features of FP into language, into code bases that are mainly go code bases, the way that I think about it is would this code base or this part of a code base, would it benefit in some way from more declaratively?
[1908.52 → 1911.42] I think I may have made up that word declaratively.
[1913.50 → 1914.28] But it works.
[1914.28 → 1915.92] I think people know what I mean.
[1915.92 → 1916.10] Right.
[1916.28 → 1917.82] Would it benefit in some way?
[1918.50 → 1922.44] And there are a lot of possible ways that declaratively can help.
[1923.00 → 1925.00] It can reduce lines of code.
[1925.66 → 1927.18] It can add structure.
[1927.92 → 1929.30] It can add readability.
[1929.74 → 1932.26] It can also reduce readability if you're not careful.
[1932.46 → 1933.48] So that's a tradeoff.
[1933.86 → 1935.42] It can fix bugs.
[1935.42 → 1938.60] Like if you have an error in one of your for loops.
[1938.60 → 1942.80] This happens a lot with parallel and concurrent code.
[1943.12 → 1947.96] And thus also code that deals with channel sends a lot too.
[1948.06 → 1949.06] I've seen that a lot as well.
[1949.34 → 1954.30] So it can reduce bugs because you're just getting someone else's code that did it the right way.
[1954.30 → 1955.12] Right.
[1955.12 → 1960.86] So if you think about it in this way, and this is where I start with any code base.
[1960.86 → 1970.22] I always start, okay, well, is there code in here that we can reduce by using the declarative features of FP?
[1970.22 → 1974.72] Whether it's maps or reduces or filters or zips and so on and so forth.
[1975.40 → 1988.56] And as a quick anecdote to close that thought out, I have seen filter as one of the most valuable tools to next tools to take and put into code bases.
[1988.56 → 1997.70] Because tons and tons of code has for loops that reduce down into selectively taking things out of a list and putting them somewhere else.
[1997.90 → 1997.94] Right.
[1998.10 → 1998.68] And that's filter.
[1999.14 → 1999.26] Right.
[1999.88 → 2000.26] Awesome.
[2000.48 → 2000.74] Awesome.
[2001.32 → 2002.28] Yeah, I can definitely see that.
[2002.36 → 2005.52] I think at least for me, it's a mindset shift.
[2005.66 → 2005.80] Right.
[2005.86 → 2009.58] So like I don't have a reason not to use FP.
[2009.72 → 2009.86] Right.
[2009.90 → 2015.72] Or not to bring some of the ideas or not really, or I should say not to think FP first.
[2015.72 → 2016.02] Right.
[2016.04 → 2018.64] In terms of how do I approach, how do I solve this problem?
[2018.82 → 2019.02] Right.
[2019.04 → 2023.60] Like I'm so used to the way I'm used to doing it.
[2023.62 → 2023.78] Right.
[2023.78 → 2031.76] So it's more of a sort of, I think maybe education and maybe sort of seeing more people talk about it, present about it.
[2031.96 → 2036.88] And having, you know, shows like this where people knowledgeable like yourself come on and sort of advocate for it.
[2037.08 → 2043.10] I think it's more of a sort of education issue more than the merits of it.
[2043.10 → 2046.74] Because all these things you're talking about here, these are things that make my program safer.
[2047.02 → 2050.12] They make, you know, my programs easier to understand.
[2050.44 → 2050.84] Right.
[2050.88 → 2056.48] And obviously, like as with everything in programming, we sprinkle things where they make sense.
[2056.48 → 2057.34] Yeah.
[2057.34 → 2066.70] And if your team at work is not using sort of FP style for things, and perhaps they want to or don't want to, so don't force it kind of thing.
[2066.82 → 2074.46] But I think every once in a while, even using your example, like Filter, for example, that I see the use case for it, not that you mentioned it.
[2074.48 → 2075.52] I see that everywhere.
[2075.96 → 2079.24] It could definitely be used in a lot more places.
[2079.90 → 2082.92] And maybe, who knows, maybe that sort of triggers somebody to say, hey, what's that?
[2082.92 → 2084.94] Like, I've never seen this particular approach, right?
[2084.98 → 2087.14] And then, boom, that's a brown bag launch right there.
[2087.14 → 2090.48] You can educate some coworkers around the merits of FP.
[2090.64 → 2098.20] So for me, I think it's an education thing more so than capabilities or features, which kind of leads me to my next question.
[2098.30 → 2110.50] Is there anything missing in Go to nudge us even more towards sort of the I don't want to say traditional FP, because I don't think we want to make an FP language per se.
[2110.68 → 2116.62] But is there missing features in Go that would allow us to even take more advantage of FP concepts?
[2117.14 → 2120.26] Well, it's so generics are young.
[2120.48 → 2123.88] And FP using generics is even younger.
[2124.40 → 2134.36] So really, the best I can do to answer that is hypothesize based on very, very unscientific things like gut feel and things I've seen and anecdotal evidence, right?
[2134.36 → 2146.22] I think the biggest thing that could unlock just making the building these things a little easier would be type parameters on methods of a struct, right?
[2146.22 → 2148.30] Or a type, right?
[2148.64 → 2149.98] So you can't do that now.
[2150.10 → 2156.52] So you can't have, let's say you have a custom list type that's a list of type T.
[2156.52 → 2165.58] You can't have a method called map on that list that takes a type parameter U and then returns a new list of type U.
[2166.28 → 2168.04] You can still build map.
[2168.14 → 2169.94] I have done it and I know others who have done it.
[2169.98 → 2171.10] I've seen it all over the place.
[2171.30 → 2172.26] You can still build it.
[2172.54 → 2173.56] It has the same effect.
[2173.56 → 2175.56] And it works the same.
[2176.26 → 2194.66] The reason that I'm hypothesizing that type parameters on methods would make things easier is because for many folks who are trained using Java or C++ or other pure, what I'll call pure object-oriented languages, although whether they're pure or not is another podcast.
[2195.04 → 2198.24] Pure in air quotes for those not watching.
[2198.62 → 2199.14] Air quotes.
[2199.30 → 2199.54] Yeah.
[2199.70 → 2200.60] Thank you for that call.
[2201.10 → 2202.32] Definitely in air quotes.
[2202.32 → 2217.62] Folks who are trained with the classical OOP type of programming, the OOP design patterns and methodology, having a method on a struct feels a lot like a method on a class in Java.
[2217.92 → 2219.92] It's not strictly the same.
[2219.92 → 2247.62] But for folks who are used to thinking of methods, if you have a method, quote unquote, again, air quotes, if you have a method, air quotes on your list struct in Go, well, it makes more sense to do it that way rather than to do it the more kind of pure, again, air quotes, pure FP way, which would be a totally separate function that takes in a certain type and returns a new type.
[2247.62 → 2277.60] Again, for some of the more advanced thing.
[2277.60 → 2279.02] It's not two hours ago.
[2279.02 → 2286.10] You know, higher kind of types add a ton of complexity to a compiler and a type checker inside the compiler.
[2286.72 → 2294.42] But, you know, they do offer basically something called a type constructor, which is a type that depends on another type.
[2294.62 → 2294.80] Right.
[2294.80 → 2300.08] And if you can do that, I'll leave it as an exercise to the reader or listener or watcher.
[2300.78 → 2302.94] What kinds of things could you do with that?
[2303.22 → 2304.52] Take me a while to get into it.
[2304.68 → 2306.04] So I'm not going to go there now.
[2306.04 → 2316.22] But if you had that right now, assuming it was correct in the compiler, you can start to do some very advanced things.
[2317.08 → 2330.50] But the only thing that I'll say is whenever I've seen that feature in a language or not in the language and then introduced into the language, at that point, it starts to become what you called sort of a functional language.
[2330.50 → 2331.10] Right.
[2331.10 → 2331.20] Right.
[2331.70 → 2342.08] Because getting to that level of sophistication in the type system often means that there are a bunch of people already there who have been demanding it.
[2342.44 → 2344.84] And those people are the majority.
[2345.16 → 2349.00] And those people write very heavily function oriented code.
[2349.00 → 2354.44] So really, I'm going to just limit it to the type parameters on methods' thing because that thing is not very controversial.
[2355.26 → 2367.12] But higher minded types or high order types are a very interesting and cool thing that I really do wish was in Go because it would enable some very slick FP things.
[2367.56 → 2368.98] Yeah, that is not controversial to me.
[2369.10 → 2369.88] I could see that.
[2370.12 → 2370.28] Okay.
[2370.56 → 2371.04] Some might.
[2371.14 → 2372.32] Maybe some people will think of it.
[2372.32 → 2372.64] Okay.
[2379.00 → 2384.56] We are going to ship it.
[2384.56 → 2387.08] Three, two, one.
[2387.54 → 2394.80] I'm Barbara Zhu, host of Ship It, a show with weekly episodes about getting your best ideas into the world and seeing what happens.
[2394.80 → 2401.30] We talk about code, ops, infrastructure, and the people that make it happen like charity majors from Honeycomb.
[2401.72 → 2404.56] We act like great engineers make great teams.
[2404.78 → 2406.22] And it's exactly the opposite.
[2406.22 → 2409.84] In fact, it is great teams that make great engineers.
[2410.42 → 2413.74] And they finally win the founders of continuous delivery.
[2414.12 → 2416.90] Start off assuming that we're wrong rather than assuming that we're right.
[2417.16 → 2418.16] Test our ideas.
[2418.28 → 2419.78] Try and falsify our ideas.
[2419.92 → 2421.92] Those are better ways of doing work.
[2421.98 → 2424.20] And it doesn't really matter what work it is that you're doing.
[2424.34 → 2426.00] That stuff just works better.
[2426.00 → 2437.62] We even experiment on our own open source podcasting platform so that you can see how we implement specific tools and services within changelog.com, what works and what fails.
[2437.62 → 2441.86] It's like there's a brand-new hammer, and we grab hold of it and everyone gathers around.
[2441.94 → 2445.74] We put our hand out, and we strike it right on our thumb.
[2445.96 → 2450.10] And then everybody knows that hammer really hurts when you strike it on your thumb.
[2450.18 → 2451.46] I'm glad those guys did it.
[2451.54 → 2452.90] I've learned something instead.
[2453.04 → 2453.16] Yeah.
[2453.32 → 2457.92] I think that's a very interesting perspective, but I don't see that way.
[2458.06 → 2458.32] Okay.
[2458.42 → 2461.52] It's an amazing analogy, but I'm not sure if that applies here.
[2461.52 → 2464.16] Listen to an episode that seems interesting or helpful.
[2464.32 → 2465.98] And if you like it, subscribe today.
[2466.08 → 2467.22] We'd love to have you with us.
[2471.70 → 2472.10] Okay.
[2472.20 → 2476.72] So before we transition into unpopular opinions, maybe I want one of those controversial ideas.
[2478.48 → 2478.88] Okay.
[2479.64 → 2480.12] All right.
[2480.46 → 2481.14] Let's get it going.
[2481.72 → 2490.88] I'm not going to give one that talks about higher kind of types because it's been a while, first, so I don't think I would do it justice or maybe even get some parts incorrect.
[2490.88 → 2493.50] But also it would take me a while.
[2493.94 → 2499.38] But I want to mention one pattern from FP that I think is really great.
[2499.92 → 2503.16] And it's not that hard to do yourself in your code.
[2503.52 → 2507.44] I also don't think it's too hard to imagine how it would work in a code base.
[2507.96 → 2509.12] It's called the lens.
[2509.84 → 2513.48] So it maybe sounds like an intimidating thing to some people.
[2513.64 → 2514.72] It certainly did to me.
[2515.38 → 2518.14] The lens is essentially a tuple of two functions.
[2518.14 → 2520.92] One function is a getter for some data.
[2521.44 → 2526.22] And then the other function is the setter for some probably the same type of data.
[2526.72 → 2528.26] But you can have separate things too.
[2528.34 → 2533.24] You can have a getter for one piece of data and a setter for another piece of data in the same tuple.
[2533.80 → 2537.82] So usually it's the getter first in the tuple and then the setter second in the tuple.
[2537.82 → 2543.12] Now the first function takes no parameters and returns the result, the data.
[2543.70 → 2550.48] It might take one parameter if the data is multidimensional like a map, and you want it to specify a key.
[2551.14 → 2551.82] And that's up to you.
[2551.90 → 2553.10] That's part of the design pattern.
[2554.04 → 2559.00] And then the setter potentially takes in the dimension of the data, again like the key of the map.
[2559.00 → 2563.80] And then it also takes in the data that you want to set into that place.
[2564.72 → 2570.86] So it might be the value of a map if we're going to use the map, like the example of a map.
[2571.50 → 2573.00] And then it returns nothing.
[2573.46 → 2579.74] These things can alternatively return an error if this is like doing something over the network or something that might fail.
[2580.14 → 2581.24] But traditionally they're not.
[2581.24 → 2590.00] All right, so if you could kind of imagine how these functions would be created, they would probably be closures.
[2590.58 → 2592.40] They would close over your data.
[2593.04 → 2595.18] They would take some parameter in the get.
[2595.34 → 2596.78] Let's take the get case, for example.
[2597.28 → 2601.90] They would take the parameter for the thing to get, and then they would return the value of it.
[2602.26 → 2603.16] Same thing with the set.
[2603.24 → 2605.34] It would close over the data and then do its thing.
[2605.34 → 2613.00] It's a fancy term called a lens, but it's a fairly basic foundational thing.
[2613.80 → 2618.30] And that is a common theme in FP, actually.
[2618.98 → 2623.70] So I called this the lens, and it is on Wikipedia, and it's in the textbook and everything.
[2624.14 → 2628.12] But it just boils down to functions like most things in FP do.
[2628.66 → 2633.32] They just boil down to one or more functions, maybe combined in some creative way.
[2633.32 → 2637.88] Or maybe one function applied across the data structure in some other way.
[2638.24 → 2643.52] So I would challenge everyone listening to just give it some thought.
[2643.80 → 2647.48] Can that reduce code somewhere in your code base?
[2648.12 → 2656.10] If you have a bunch of getters, can you get rid of those getters and just replace them with a closure of the lens?
[2656.52 → 2661.66] That's a very interesting one to me because it is exceptionally simple.
[2661.66 → 2663.10] I'll put it a different way.
[2663.26 → 2665.72] The return on investment is very high.
[2666.28 → 2671.02] It's very simple, but it tends to be applicable and useful in a lot of places in the code base.
[2671.48 → 2671.84] Very cool.
[2672.34 → 2675.18] I'd love to see that in action, like in practical use.
[2675.52 → 2677.20] The way you explain it, it sounds great.
[2677.54 → 2679.68] I'm like, yeah, that sounds like something I'd be up for.
[2679.98 → 2680.36] There you go.
[2680.54 → 2680.66] Yeah.
[2680.96 → 2681.16] Yeah.
[2681.16 → 2685.16] Perhaps we need sort of a blog post from you when you're done with school or something.
[2685.94 → 2686.34] Yeah.
[2686.34 → 2686.74] Yeah.
[2687.94 → 2690.56] So if you remember me asking, what did you go back to school for?
[2690.96 → 2693.22] Well, I went back to school for computer science.
[2693.44 → 2697.56] I got an undergraduate computer science degree in 2008.
[2698.16 → 2701.24] You know, I'm not that old, but I feel older than I am, I guess.
[2701.52 → 2705.26] You can do the math at home, see and figure out how old I'm likely to be.
[2705.94 → 2710.98] And so then I've been in industry ever since, focused on industry things, right?
[2710.98 → 2713.06] And they all tend to be very practical.
[2713.76 → 2717.06] They all tend to be, you know, single goal oriented.
[2717.98 → 2724.02] And all the learning that I've done has been very focused on a goal rather than broader.
[2724.28 → 2731.04] So I went back to get a master's to get that breadth again, because I've kind of missed that.
[2731.64 → 2737.18] Right now, I kept using the SQL and the database examples, because right now I'm taking a course in databases.
[2737.18 → 2741.28] So that's an easy extension there.
[2741.96 → 2750.86] But the thing that I'm planning to specialize in now is formal methods, because I love this stuff, like programming language theory and things like that.
[2751.12 → 2753.16] I really do enjoy it a lot.
[2753.96 → 2760.20] And the formal method specialization happens to have quite a bit of language theory stuff in it.
[2760.48 → 2762.06] So look forward to that.
[2762.06 → 2765.20] Yeah, it sounds like you're in your bread and butter kind of space right now.
[2765.38 → 2767.32] That's nice, nice, nice.
[2767.58 → 2767.74] Yeah.
[2767.98 → 2768.20] Yeah.
[2768.30 → 2776.18] And now that you mention it, interestingly enough, I think we tend to go to school to get a specialization, to narrow it down on a very particular set of skills.
[2776.66 → 2781.90] Even though when we go in, we might not know that's what we're doing, but we're going to learn how to do X, right?
[2781.90 → 2784.78] And then we come out, and we get a job to do X, right?
[2784.78 → 2789.20] It's very rarely do you go back just for the sake of breath, right?
[2789.26 → 2793.16] Just to get, basically to go find out what you don't know about, right?
[2793.24 → 2799.02] And then you sort of see how you can sort of apply it to your already existing set of knowledge that you require in the industry.
[2799.36 → 2800.30] So yeah, I commend you for that.
[2800.44 → 2801.28] That's very cool.
[2801.56 → 2806.44] Well, I'm very, very lucky and privileged to be able to do that at this point, right?
[2806.44 → 2815.28] Because I think probably all of us remember in undergrad, we probably just went so we could get to whatever our next step was.
[2815.70 → 2817.46] Most of us probably was a job, right?
[2817.58 → 2820.96] Maybe some of us was grad school, but most of us was a job.
[2821.04 → 2822.56] It certainly was me, right?
[2822.56 → 2826.72] I was laser focused on getting done so I could get paid.
[2827.98 → 2829.66] But these days it's different, right?
[2829.66 → 2836.32] I have a job and, you know, I'm able to continue working in this job while I do this part-time program.
[2837.06 → 2849.36] And so I fully acknowledge, and I try to remind myself daily that I'm very lucky to be able to do something like this just because I want to rather than having to do something.
[2849.66 → 2850.02] Pretty cool.
[2850.16 → 2850.46] Pretty cool.
[2850.96 → 2858.28] Well, Aaron, unless you have another like more like popular opinion for me, although I don't think anything you said here is unpopular, right?
[2858.28 → 2862.88] I think maybe it's just the way you talk and put it, but I don't think any of it was unpopular.
[2863.54 → 2864.32] Diplomacy, yeah.
[2864.94 → 2865.52] Yeah, yeah.
[2865.52 → 2867.40] Well, I do have an unpopular opinion.
[2867.66 → 2867.92] Okay.
[2868.24 → 2869.68] This one will be unpopular.
[2870.02 → 2870.52] Okay, wait.
[2870.64 → 2872.18] Then I got to play the song if that's the case.
[2872.44 → 2873.12] Okay, okay.
[2873.14 → 2873.76] Let's do it.
[2878.14 → 2878.78] Unpopular opinion.
[2878.98 → 2879.96] You want to.
[2879.96 → 2881.64] I actually think you should probably leave.
[2882.14 → 2886.58] Unpopular opinion.
[2887.14 → 2887.22] Unpopular opinion.
[2887.90 → 2888.42] Boom.
[2892.76 → 2893.46] Lay is on us.
[2893.46 → 2894.18] All right.
[2894.18 → 2894.20] All right.
[2894.58 → 2896.88] Well, I've been doing a bunch of Rust lately.
[2897.04 → 2900.96] Some like very low level stuff dealing with virtual machines.
[2901.82 → 2917.60] And I believe now that I've used Rust long enough, I believe the type system in Rust is more complete and leads to more concise and easier to write and read programs than Go.
[2917.60 → 2918.84] Okay, then.
[2919.32 → 2919.62] Yeah.
[2919.62 → 2923.46] So the Go type system has some work to do.
[2923.88 → 2924.26] Okay.
[2924.64 → 2925.06] Okay.
[2925.32 → 2925.60] Yeah.
[2925.98 → 2930.34] I don't mean to fan the flames of the Go Rust thing, but I'm sure I just have.
[2930.56 → 2931.90] Oh, too late, buddy.
[2931.90 → 2932.70] I'm just done it.
[2932.70 → 2932.74] I'm just done it.
[2933.78 → 2934.62] The flame war.
[2935.58 → 2938.56] It's been zero days now since the flame wars.
[2939.96 → 2941.30] I know, I know.
[2941.30 → 2946.56] I talked a lot about type system things today, right?
[2946.72 → 2949.70] And it's not that Rust lets you do all those things.
[2949.88 → 2950.84] It certainly doesn't.
[2951.40 → 2958.96] But the type system in Rust has more features than the type system in Go.
[2959.40 → 2963.70] It certainly allows for some programs that take forever to compile and are hard to read.
[2963.70 → 2966.14] So that's the pro and con thing here.
[2966.48 → 2976.22] But from my experiences so far, it lets you write more expressive code with fewer lines than the Go equivalent.
[2976.84 → 2977.14] Okay.
[2977.68 → 2979.98] Well, we shall put that to the test.
[2980.30 → 2980.56] Yeah.
[2980.82 → 2981.68] The audience.
[2982.20 → 2986.74] They will tell us whether they agree with you or disagree with you and come find you in the night or something.
[2987.06 → 2987.32] Yeah.
[2987.46 → 2987.66] Yeah.
[2987.72 → 2989.70] You all know my Twitter.
[2990.00 → 2991.92] So you can send me hate mail.
[2991.92 → 2993.98] I still love Go.
[2994.22 → 2995.10] Don't get me wrong.
[2995.30 → 2998.70] I've been writing Go for something like 10 years or something.
[2999.48 → 3003.58] And there's no language I can build something more quickly in.
[3004.10 → 3005.46] I'm just getting started with Rust.
[3005.56 → 3006.92] So that's my initial opinion, though.
[3007.88 → 3009.42] Hey, you can love more than one language.
[3009.62 → 3009.98] That's cool.
[3010.18 → 3010.50] Oh, yeah.
[3010.62 → 3011.60] As long as it's Go and Go.
[3011.74 → 3012.04] That's cool.
[3014.54 → 3016.46] Love anything you want as long as its Go.
[3018.30 → 3019.28] I love that.
[3020.08 → 3020.48] Awesome.
[3020.66 → 3020.98] Awesome.
[3020.98 → 3025.68] So thank you so much, Aaron, for coming back on the show and talking about functional programming.
[3026.38 → 3037.00] Hopefully we hit a few nails on the head for folks that have been curious about functional programming and how it's done, how it's been done, and what Generics enabled for us moving forward.
[3037.56 → 3038.80] This was a fun discussion.
[3039.04 → 3040.36] Thanks again, Aaron, for coming on the show.
[3040.68 → 3042.18] Thank you so much for having me, Jimmy.
[3042.18 → 3047.80] All right.
[3047.80 → 3049.40] That is Go time for this week.
[3049.64 → 3050.36] Thanks for listening.
[3050.36 → 3056.42] If you're FP curious and want some more like this, we had Eric Normand on JS Party While back talking about it.
[3056.58 → 3061.84] Eric is one of the best people I've heard explain FP principles and why they are worth putting to use in your code base.
[3061.98 → 3062.48] Take a listen.
[3062.88 → 3065.82] Have you ever seen the original show, the Get Smart?
[3065.82 → 3069.88] Like the intro where he has like 30 different doors he walks through.
[3070.10 → 3070.44] Yeah.
[3070.66 → 3073.98] And then he holds up his shoe to his ear and talks into it.
[3074.00 → 3074.02] Yeah.
[3074.20 → 3075.22] And he has a phone.
[3075.38 → 3076.72] He has a cell phone in his shoe.
[3077.42 → 3077.58] Yeah.
[3077.68 → 3080.36] But you go through all these doors, right?
[3080.42 → 3080.58] Right.
[3080.58 → 3084.00] And you get deeper and deeper into the sanctum of functional programming.
[3084.00 → 3091.86] Well, that first door is just recognizing the difference between what I call actions, calculations and data.
[3092.14 → 3092.50] Okay.
[3093.20 → 3096.48] Calculations are often known as pure functions.
[3096.68 → 3104.72] They're the stuff you can do in your language that always gives you the same answer no matter how many times you run them or when you run them.
[3105.38 → 3105.66] Okay.
[3105.70 → 3108.08] So this is like addition, right?
[3108.12 → 3110.10] Addition is always going to two plus two.
[3110.18 → 3110.84] It's always four.
[3111.28 → 3113.00] It doesn't matter how many times you run that.
[3113.00 → 3118.04] But then there are actions that do depend on when you run them or how many times you run them.
[3118.48 → 3131.70] So reading from a mutable variable, if you read after someone has written to it, you're going to get a different answer than reading before the other, you know, other part of the code writes to it.
[3131.94 → 3135.60] Likewise, sending an email or writing something to disk.
[3135.60 → 3143.02] These are all actions because, you know, sending the email zero times is different from sending it one time or 10 times.
[3143.24 → 3157.58] And so making this distinction between actions that depend on time because they're hard to deal with and calculations is like the first gateway into functional programming.
[3157.58 → 3159.12] Oh, and data is easy.
[3159.12 → 3162.72] Data is just, you know, the stuff that doesn't do anything.
[3162.84 → 3163.52] It's just inert.
[3163.80 → 3169.34] You know, the strings and numbers and hash maps and lists and stuff like that.
[3169.34 → 3172.30] That's episode 163 of JS Party.
[3172.30 → 3178.60] If you want to hear more, find it at jsparty.fm slash 163 or search for it in your podcast app.
[3178.72 → 3182.46] The title of the episode is JS is an Occasionally Functional Language.
[3182.96 → 3185.86] Thanks once again to Vastly and Fly for partnering with us.
[3186.10 → 3187.40] Please check out what they're up to.
[3187.56 → 3188.74] They support everything we do.
[3189.00 → 3191.10] And of course, thank you to our Beat Freakin' residents.
[3191.36 → 3195.32] Break master Cylinder, our beats are dope because BMC makes dope beats.
[3195.64 → 3196.52] It's as simple as that.
[3196.52 → 3200.22] That's all I have for you, but we'll talk to you next time on Go Time.
