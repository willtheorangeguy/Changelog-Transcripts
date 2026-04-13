[0.00 → 2.12] This is John Resign. You're listening to The Change Log.
[17.30 → 22.46] Welcome to The Change Log, episode 0.2.9. I'm Adam Stachowiak.
[22.82 → 26.72] And I'm Wynne Edelman. This is The Change Log. We cover what's fresh and new in the world of open source.
[26.72 → 31.62] If you found us on iTunes, we're also on the web at thechangelog.com. And we're also up in GitHub.
[32.18 → 39.10] Yep. Head to GitHub.com forward slash explore. You'll find some training repos, some feature repos from our blog, as well as the audio podcast.
[39.38 → 46.64] And if you're on Twitter, go to twitter.com forward slash changelog show and hit the follow button. And also follow Adam Stack.
[47.46 → 54.20] And I'm Penguin, P-E-N-G-W-Y-N-N. Fun interview this week with a guest host, Michael Smith from Australia.
[54.20 → 55.32] Mm-hmm.
[55.56 → 59.70] We sat down with Jeremy Ash kenos from Document Cloud. You may remember from episode five.
[59.96 → 63.82] Yeah, episode five. Yeah, that was a lot of fun. Talked about, what did we talk about in that episode?
[64.20 → 67.34] Underscore.js. You don't have the episodes memorized?
[67.70 → 70.44] Oh, my bad. I'm sorry. There's, what, 29 of them now, so.
[70.52 → 73.46] There you go. Talking about CoffeeScript this time. So back to JavaScript.
[73.46 → 79.20] You know, we're big fans of Tamil and Mass, and those are preprocessors to write HTML and CSS.
[80.18 → 96.54] CoffeeScript's kind of the same thing for JavaScript. It allows you to write JavaScript in another way, provide some additional syntax, time savers, and enhancements to output JavaScript to either use in the browser and server side with something like maybe, I don't know, Node.js.
[96.54 → 98.36] Cool. Are you using this anywhere?
[99.24 → 105.16] I'm using it in Titanium, personally, which we've talked about, I believe, seventh, episode seventh or something.
[105.42 → 107.16] Yeah? You don't know the episodes when?
[107.32 → 113.66] I don't. I don't have them re-memorized. So, yeah, I'm using it to do some iPhone and iPad stuff lately.
[114.00 → 122.44] Very cool. Well, you're a very out-there kind of guy, always mixing a bunch of products into the mix of your work, so this is kind of fun. So is it fun to work with?
[122.44 → 128.88] It is. You know, I'm a mash-up of design and development, and my projects are a mash-up of every fun toy that I want to play with.
[129.10 → 131.46] Cool. And so Jeremy gives us a lot of good nuggets in this interview?
[132.08 → 145.54] He does. Some insight into the design of the language and kind of the inspiration behind it and some of the languages that he ripped off from to provide us this cool new syntax.
[145.84 → 148.36] Ripped off. All right, cool. So it's a good interview, then, I suppose.
[148.68 → 149.38] Let's get to it.
[149.54 → 150.00] All right, man.
[152.44 → 163.98] All right, we're joined this afternoon by Jeremy Ashkenazi from Document Cloud.
[164.12 → 165.36] I'm going to talk about CoffeeScript.
[165.52 → 169.46] I also should mention we've got a guest host today, Michael Smith from Way Down Under.
[169.66 → 170.20] Say hello, Michael.
[170.88 → 171.04] Hi.
[172.14 → 180.22] So, Jeremy, I want you to introduce yourself to the folks that maybe didn't catch episode 0.5
[180.22 → 182.94] that was Document Cloud and Underscore JS.
[183.76 → 190.30] Right. So it's been, I guess it's been a little over six months since I talked to you guys the first time about the stuff that we were doing with Document Cloud.
[190.30 → 204.04] But so basically, I'm working on this project that is to make an online repository of primary source documents that news organizations contribute, and the journalists get to use to do their document-based research.
[204.16 → 209.12] And when they're done writing their story, they put the documents online alongside the story for extra context.
[209.12 → 217.62] And so that's a large JavaScript application, and we're doing a ton of client-side JavaScript to show the entities that are present in the documents and to show the dates that are present on the timeline.
[218.60 → 229.66] And I've been using JavaScript heavily on the client-side for a long time, and I'm very excited about what's going to happen when we can start using the same language on both the server-side and the client-side.
[229.66 → 235.24] And not only is it going to be the same language, but it's also going to be a very nice language, and it's going to be a very fast language.
[235.90 → 243.82] And so I've had this kind of idea kicking around in the back of my head for a long time about what would JavaScript look like if it could look like anything you wanted it to look like.
[244.06 → 253.04] If it hadn't been basically stuck in a place where you had all the browsers having to agree on what JavaScript would be in order to make any progress,
[253.28 → 256.86] if it had been a language that had evolved, what could it look like?
[256.86 → 260.70] So that's kind of what CoffeeScript was, and it was just for fun sort of – and it still is.
[261.00 → 265.10] It's for fun. I'm not trying to sell it or to build a business out of it or to persuade you to use it.
[265.40 → 268.90] It's a thought experiment about what JavaScript could look like potentially.
[269.76 → 271.20] And so, yeah, that's what we're going to talk about today.
[271.50 → 276.50] Let's talk about what it looks like. So what is the syntax influence of CoffeeScript?
[277.44 → 279.48] There's actually been a bunch. It's been kind of fun.
[279.48 → 283.92] So my own background is mostly doing Ruby and JavaScript stuff with a little bit of Java.
[283.92 → 289.46] But CoffeeScript, I guess people think that it looks a lot more like Python than it does like Ruby these days.
[289.94 → 295.66] So it's got basically simple – the regular simple scripting language syntax that you're used to,
[295.84 → 297.94] but it uses significant white space to delimit blocks.
[298.38 → 302.90] So if you have a function, or you have a class, or you have an array or switch statement or an if else,
[302.98 → 307.06] you use white space and indentation to delimit the start and the end of that.
[307.06 → 310.52] And, of course, you can wrap it in parentheses if it's not totally clear what you're up to.
[310.52 → 318.48] But there's also been a strong bunch of contributions from the functional programming community and from Haskell in particular.
[318.70 → 321.72] So there's been a bunch of Sellers who have come on and have added features
[321.72 → 324.66] and have contributed both syntax and implementation.
[325.02 → 327.78] So I'd say there's a big strain of that in there as well.
[328.78 → 331.44] Okay. So since it compiles down to JavaScript,
[331.44 → 338.54] is there anything that you support in CoffeeScript that you don't actually support in JavaScript
[338.54 → 344.04] or things that you can't sort of get access to because you're cross-compiling?
[344.92 → 352.28] Right. So an important thing to mention here is that CoffeeScript is a very limited language.
[352.42 → 354.02] It's not like you have complete freedom.
[354.18 → 355.84] You're not working with C. You're not working with assembly.
[355.84 → 357.24] You can't do anything you want to.
[357.34 → 364.64] You can't implement new constructs or new semantics very easily because it's a source-to-source language.
[364.84 → 369.68] And not only is it source-to-source, but we're trying to keep the compiled JavaScript very clean and very readable.
[370.22 → 373.78] And in a perfect world, if we had everything worked out correctly,
[373.94 → 379.92] then the JavaScript that gets generated by the CoffeeScript compiler would be the code that you would have written anyway
[379.92 → 382.22] if you had done it by hand or something very close to that.
[382.22 → 382.88] So that's our goal.
[384.18 → 386.90] And so because of that, there are a lot of things that we can't implement.
[387.00 → 391.74] A very simple one that has actually come up several times before has been indexing into an array.
[392.02 → 398.04] It would be great in JavaScript if you could index into an array with a negative number and get the value off the end.
[398.10 → 402.48] So instead of having to do array, array.length minus one to get the last element,
[402.60 → 405.56] you could just say array negative one and get back to the final one.
[405.66 → 410.34] But that's something that we could support naively in CoffeeScript, you know,
[410.34 → 414.30] if you actually use a literal number, but because you could pass a variable in as the index or a function in,
[414.62 → 421.00] there's absolutely no way for us to reliably do negative array indexing without actually changing the runtime,
[421.32 → 421.98] which we can't do.
[422.20 → 426.70] So that's just a very simple example of a tiny, tiny feature that would take two seconds if we had access to the runtime,
[426.84 → 428.30] but we don't, so we can't implement it.
[429.00 → 431.70] Do you actually need to learn JavaScript to write CoffeeScript,
[431.94 → 435.56] or can you just learn CoffeeScript and forget about the JavaScript?
[435.56 → 442.26] Right, I mean, so that's more of a documentation question, I think, than an actual code question.
[442.46 → 446.24] So you definitely could learn just the CoffeeScript semantics,
[446.32 → 448.22] which are slightly different from JavaScript,
[448.38 → 449.88] and I can get into what those differences are in a second.
[450.60 → 455.26] But right now, the documentation is basically a list of the ways in which it differs from JavaScript.
[455.48 → 459.40] You know, you're using the JavaScript runtime, JavaScript functions behave the same way,
[459.58 → 461.18] you know, numbers behave the same way,
[461.18 → 465.22] and basically all the semantics are JavaScript semantics.
[466.46 → 468.82] So, yeah, so right now it's basically, you know JavaScript,
[469.08 → 471.48] here's a cleaner way to write it, is the idea.
[472.10 → 473.30] You know, I'm a big fan.
[473.38 → 475.18] I'm using it in a couple of projects now,
[475.28 → 478.32] and when I explain it to folks that haven't seen it,
[478.88 → 481.04] the example that I give is it's, you know,
[481.08 → 483.66] Hamill is to HTML and SAS is to CSS,
[484.28 → 485.42] CoffeeScript is to JavaScript.
[485.54 → 486.58] Is that a fair statement?
[486.58 → 486.62] Yeah.
[487.48 → 489.44] I'm not sure, actually, how fair that is,
[489.50 → 491.30] because I think the interesting thing about that comparison,
[491.44 → 493.38] which, of course, has been what it's been since the beginning,
[494.04 → 497.24] is that, you know, with CSS and with HTML,
[497.46 → 499.20] you have basically static languages,
[499.20 → 502.56] and you're writing abbreviations that expand into larger formats.
[503.02 → 504.14] And I think with something like CoffeeScript,
[504.20 → 505.96] you're actually compiling into a programming language,
[506.36 → 507.64] it goes a little bit beyond that,
[507.70 → 511.08] because you can actually start to change, you know,
[511.08 → 513.32] the semantics of the code and change the way you would have written things.
[513.44 → 514.98] It's not just a one-to-one expansion.
[514.98 → 517.74] You can actually start to write things in a little bit of a different way.
[518.84 → 520.54] So to get into that a little bit,
[520.96 → 525.58] there's kind of, I think, three core aspects to CoffeeScript.
[525.78 → 527.20] There's the syntax changes.
[527.64 → 531.56] So at the basic level, it's a cleaner, a short, you know,
[531.56 → 532.22] you have to type less.
[532.30 → 533.52] You don't have to type as many parentheses.
[533.78 → 535.62] You don't have to type as many semicolons or brackets
[535.62 → 538.38] just to write what you would have written in JavaScript.
[539.02 → 541.84] The second aspect of it is that there are semantic cleanups.
[541.84 → 546.78] So the core thing there is that everything is an expression in CoffeeScript.
[547.00 → 550.64] And we try to make every function returns a meaningful value.
[551.20 → 555.44] Every if statement or switch or try catch is an expression that can be used
[555.44 → 556.64] as part of a larger computation.
[556.78 → 558.62] There's no difference, for the most part,
[558.72 → 561.64] between statements and expressions.
[561.64 → 565.24] So a lot of work has been done there, basically,
[565.60 → 570.94] as you sort of, as you go, as the nodes compile,
[571.18 → 572.96] as you have the compiler that's turning, you know,
[573.00 → 576.06] turning your code into tokens, into nodes, into JavaScript,
[576.32 → 579.60] to say if you're using the result of a particular statement,
[579.72 → 582.52] then that statement gets converted into an expression in JavaScript.
[582.98 → 584.26] And so you can use it.
[584.64 → 586.06] So there's been a lot of effort there.
[586.12 → 587.64] And that's an example of a semantic cleanup.
[587.64 → 590.08] There are a couple other ones, like switch statements,
[590.28 → 592.88] which don't work very well in JavaScript unless you're using strings
[592.88 → 595.34] to compare on work on any object in CoffeeScript
[595.34 → 598.06] because you compile them into if-else chains instead of switch statements.
[599.08 → 601.58] And things like that where the statements don't actually work the same
[601.58 → 602.28] as they would in JavaScript.
[603.08 → 604.70] So that's the second aspect is semantic cleanups.
[604.78 → 606.34] And then the third aspect is bonus features.
[606.68 → 610.42] So, you know, I thought it was really cute in the last presidential campaign
[610.42 → 614.92] when John McCain started talking about goodies in legislation.
[615.24 → 619.08] So I think of the bonus features as the goodies that you get alongside with CoffeeScript.
[619.24 → 622.18] And so things like that are the array comprehension.
[622.38 → 624.22] So instead of having to write out your explicit for loop,
[624.28 → 628.60] you can do a comprehension over an array and get back the list of values.
[628.60 → 633.38] And so that takes care of mapping and filtering and reducing, actually.
[633.38 → 638.80] And you also get range comprehensions and object comprehensions, too.
[638.90 → 642.96] So things like that are bonus features and the existential operator and splats
[642.96 → 645.18] and all these goodies we can talk about.
[645.60 → 649.70] So those are the three parts, the syntax, the semantic cleanups, and then the goodies.
[650.64 → 650.80] Okay.
[650.90 → 656.38] So with these goodies, you're obviously adding on things like different for loops
[656.94 → 657.96] and things like that.
[657.96 → 664.74] Are you following the ECMAScript 5 specifications when designing those?
[664.94 → 667.76] Or do you follow some other sort of standard?
[668.34 → 674.28] So in terms of extra features, so there's ECMAScript 5, which we now have since this fall.
[675.76 → 679.34] And all the code that – and yes, we've been influenced by ECMAScript 5,
[679.46 → 681.18] but even to a large extent ECMAScript Harmony.
[681.18 → 685.50] So there's this great wiki with all the suggestions that were in ECMAScript 4
[685.50 → 690.34] and didn't quite make it out when ECMAScript 5 came over and took –
[690.34 → 693.42] and made it a much more minimal language than the next version of JavaScript was going to be.
[693.80 → 695.78] There are a lot of great suggestions for things that they wanted to do
[695.78 → 698.08] that aren't implemented yet in this ECMAScript Harmony wiki.
[698.66 → 701.60] And so we've taken a lot of things directly from there where we can
[701.60 → 703.36] and where we think that it makes sense.
[704.34 → 708.00] So, I mean, for example, the syntax for – I'm not sure if this is on the wiki,
[708.00 → 710.54] but the syntax for splats, for doing triadic arguments,
[710.80 → 713.98] where you can have a couple positional arguments
[713.98 → 717.32] and then a splat that soaps up the rest of the arguments to a function.
[717.78 → 720.62] Or you could pass in a variable number of functions into a –
[720.62 → 723.48] sorry, a variable number of arguments into a function without having to use apply.
[724.94 → 727.94] The syntax for that with the triple dots was suggested by Douglas Crockford.
[728.92 → 733.82] And another piece of syntax that we took from ECMAScript 5 is the –
[733.82 → 737.48] a string interpolation is you can look at the proposal they have on the wiki right now,
[737.48 → 739.94] and that's very similar to what was proposed for ECMAScript Harmony,
[739.94 → 744.24] where you can interpolate naked variables just using a dollar sign into a string,
[744.34 → 747.26] or you can use a dollar sign with brackets and have arbitrary expressions
[747.26 → 748.74] interpolated into a string.
[750.12 → 750.64] So, yes.
[751.54 → 757.48] Going off the usage and implementation of splats in JavaScript,
[758.02 → 759.12] or in CoffeeScript,
[759.36 → 762.70] now that you've got these extra language features,
[763.34 → 767.04] it's doing a lot of behind-the-scenes work to make them actually work in JavaScript.
[767.04 → 772.24] So, one thing that I noticed when I first saw some CoffeeScript
[772.24 → 776.02] was actually that the developer sent me the compiled JavaScript
[776.02 → 780.62] when I was trying to help them out and try and figure out what their problem was with it.
[780.86 → 786.66] Now, of course, I couldn't actually read the JavaScript that I had compiled a fair bit
[786.66 → 790.22] because there were so many things that were being done behind the scenes,
[790.30 → 792.50] and I couldn't say, change these couple of lines,
[792.82 → 795.36] because he wasn't actually writing those few lines.
[795.36 → 801.72] Is cross-compiling from CoffeeScript to JavaScript adding a barrier in the debugging process?
[802.84 → 803.26] Yes.
[803.36 → 803.92] So, absolutely.
[804.04 → 805.72] Anytime you have a source-to-source translation,
[806.50 → 808.68] there's going to be a barrier in the debugging process.
[808.96 → 811.68] And so, the way it's worked out in practice is, you know,
[811.76 → 815.88] our tactic instead of building a special, you know, CoffeeScript-only debugger
[815.88 → 819.42] has been to make the generated JavaScript as readable as we possibly can
[819.42 → 821.94] and use whatever tricks we can to make it as readable as possible.
[822.70 → 825.78] And so, if you do, for example, if you do compile a CoffeeScript file to JavaScript,
[825.96 → 829.06] you load it in the browser, and you get an exception in the browser,
[829.06 → 830.68] it's going to give you the line number of the JavaScript
[830.68 → 832.08] and not the line number of the CoffeeScript.
[832.20 → 835.50] And that is the single biggest problem with figuring out and debugging right now.
[835.56 → 839.52] You have to keep your JavaScript files handy and go look up what's happening
[839.52 → 841.68] and then see where that occurs in the CoffeeScript and fix it.
[841.68 → 845.86] And I thought it was going to be a larger problem personally than it has been for me.
[846.00 → 851.46] I haven't had too much trouble with tracing back and figuring out where things are going wrong.
[852.00 → 855.46] But from a beginner's perspective, if you're just getting started with it,
[855.48 → 857.06] it certainly would be more daunting.
[858.00 → 861.66] So, I think what you might have been referring to are our use of temporary variables.
[861.82 → 867.20] So, we do have to put in some temporary variables to do things like convert a comprehension,
[867.20 → 871.86] a one-line array comprehension in CoffeeScript into the equivalent JavaScript.
[872.02 → 875.38] You have to use a temporary variable for the memorized array
[875.38 → 879.82] where you're caching all the result values before you turn the computed result
[879.82 → 881.72] of passing the function through the array.
[882.68 → 885.18] So, you'll get things like that where you'll have a variable with a name,
[885.26 → 887.36] usually underscore A, underscore B, underscore C,
[887.70 → 890.88] a temporary variable that has no equivalent on the CoffeeScript side.
[892.00 → 894.32] And so, before you're familiar with what that is doing,
[894.66 → 895.72] then, yeah, it wouldn't make any sense.
[895.72 → 900.66] With those temporary variables, would it make more sense to assign them
[900.66 → 904.20] as an actual meaningful value?
[905.22 → 906.48] As a meaningful name?
[907.24 → 907.62] Yeah, yeah.
[908.00 → 911.56] So, rather than underscore A, actually have it, so it's say...
[912.30 → 913.14] Underscore results?
[913.98 → 915.66] ...arguments length or something like that.
[916.06 → 917.22] Sure, we could do that.
[917.30 → 920.84] The problem is then you have name clashes with anything that's in external scope
[920.84 → 921.90] that might already be defined,
[921.90 → 925.84] unless you happen to have a function wrapper around that.
[926.24 → 928.88] And we don't necessarily know what's in external scope
[928.88 → 932.94] because you could be including other scripts onto the page
[932.94 → 935.00] that could be having things at the global level.
[935.28 → 937.28] So, that gets a little bit tricky.
[937.46 → 940.28] It might actually be a worthwhile change
[940.28 → 942.44] to start doing underscore meaningful name
[942.44 → 944.60] and then if something's already declared that we can detect
[944.60 → 949.44] to make it a double underscore or add a one after or something like that.
[950.08 → 952.68] Because right now we do have a way of seeing...
[952.68 → 954.12] In the particular file you're compiling,
[954.30 → 955.24] of seeing what's in scope,
[955.32 → 958.26] which is how CoffeeScript scoping is handled for you.
[958.30 → 961.08] You don't have to use var to declare a keyword in CoffeeScript.
[961.18 → 962.66] So, we could take advantage of that probably
[962.66 → 965.46] to do better with meaningful names for those variables.
[965.46 → 967.40] Getting back to the goodies for a moment,
[967.68 → 972.00] two that drew me in were your approach to classes, inheritance,
[972.36 → 974.36] and also for function binding.
[974.48 → 976.14] Could you talk about those two features for a moment?
[976.90 → 977.30] Sure.
[977.70 → 981.74] So, with classes, the idea is that...
[981.74 → 983.28] This has actually been very controversial
[983.28 → 984.46] because people...
[985.12 → 986.70] You know, when you talk about classes in JavaScript
[986.70 → 989.52] and of course a lot of people who do significant work
[989.52 → 991.92] with prototypes and with inheritance in JavaScript
[991.92 → 995.30] will yell at you if you have something called a class.
[995.30 → 997.18] So, there's a big argument about whether we should call it class
[997.18 → 999.26] or whether we should call it proto or something else.
[1000.68 → 1002.84] To which my answer has always been that
[1002.84 → 1005.92] if you look at any amount of JavaScript code
[1005.92 → 1009.16] that uses prototypes to do inheritance,
[1009.50 → 1011.82] then they always work in classical patterns
[1011.82 → 1013.36] regardless of whether you call it a class or not.
[1013.44 → 1017.20] You always have a base object with a prototype
[1017.20 → 1020.04] and you always make many new instances of it with different data.
[1020.32 → 1021.10] And so, calling it...
[1021.10 → 1021.84] You can call it whatever you want,
[1021.94 → 1024.38] but I'd say call it a class just because that's what it is.
[1024.38 → 1027.40] And so, what we're trying to do here
[1027.40 → 1029.28] is to make it easier to work with prototype chain
[1029.28 → 1033.48] because it's not very easy to correctly set up a prototype chain
[1033.48 → 1035.26] so that you can have more than one level of inheritance
[1035.26 → 1035.94] without it breaking
[1035.94 → 1039.66] and with having the instance of operator working correctly
[1039.66 → 1043.14] and being able to call super efficiently
[1043.14 → 1045.54] is one of the most difficult things.
[1045.54 → 1048.20] And so, usually if you override a function,
[1048.32 → 1050.54] you want some way to reference the base implementation
[1050.54 → 1053.86] so that you can run that and then subclass it
[1053.86 → 1056.66] and then do your specialized overrides on that function.
[1056.78 → 1059.14] And it's very, very difficult with regular prototypes
[1059.14 → 1060.18] to call super in JavaScript.
[1060.34 → 1062.02] You have to know the name of your parent
[1062.02 → 1063.28] and you have to go look at their method
[1063.28 → 1065.92] and you have to apply it on your current object.
[1066.52 → 1069.12] And so, CoffeeScript's trying to make that easier for you.
[1069.12 → 1074.88] So, we use a variant of the Google Closure libraries.
[1075.34 → 1078.24] I think it's called good. Inherits function
[1078.24 → 1080.32] to do the subclassing.
[1080.42 → 1081.24] So, it's about, let's see,
[1081.30 → 1083.60] it's about five lines of JavaScript
[1083.60 → 1085.76] that actually makes the child class.
[1086.28 → 1088.08] And then anytime you call super within a method
[1088.08 → 1089.62] inside the subclass,
[1089.78 → 1092.88] it makes a direct reference to the parent class for you.
[1092.90 → 1093.90] So, you don't have to write it out by hand
[1093.90 → 1096.08] and performs very well for that reason.
[1096.08 → 1098.62] So, function binding is another problem
[1098.62 → 1099.84] that tends to be a brain bender
[1099.84 → 1102.76] for new JavaScript developers.
[1103.26 → 1103.58] Right.
[1103.94 → 1105.52] So, talking about function binding,
[1105.68 → 1107.38] we actually used to have more support
[1107.38 → 1108.90] for function binding in the language,
[1109.04 → 1110.58] but it was decided that instead of having
[1110.58 → 1111.66] kind of cryptic operator
[1111.66 → 1112.92] for binding functions directly,
[1113.04 → 1115.24] we would make that more of a standard library thing,
[1115.62 → 1116.76] you know, because you should really be able,
[1116.96 → 1118.32] it is really binding should be,
[1118.84 → 1121.40] and I guess maybe in some future version
[1121.40 → 1122.62] of ECMAScript it will be,
[1122.92 → 1125.12] but it should be a method on a function object.
[1125.12 → 1126.60] You should be able to call function. Bind
[1126.60 → 1128.34] and pass in the context you want to bind it.
[1129.00 → 1131.14] So, what we have right now is basically
[1131.14 → 1133.74] the syntax for defining a function in copy script
[1133.74 → 1135.22] looks like this.
[1135.34 → 1136.00] You have your arguments,
[1136.16 → 1136.72] you have an arrow,
[1136.90 → 1138.12] and then you have your function body
[1138.12 → 1139.02] on the right-hand side.
[1139.54 → 1140.96] And the function body can be many lines,
[1141.04 → 1141.62] it can be indented.
[1142.36 → 1146.06] So, arguments goes to, you know, computation.
[1146.90 → 1149.94] And it's a regular little sort of ASCII arrow
[1149.94 → 1151.80] as the function syntax,
[1151.80 → 1153.40] but if you use a fat arrow
[1153.40 → 1155.74] with, like, the hash-style arrow,
[1155.84 → 1156.68] if you're familiar with Ruby,
[1156.78 → 1158.82] with the equals sign and the arrow.
[1159.02 → 1160.56] The hash rocket, as we would call it in Ruby.
[1160.62 → 1161.42] Exactly, hash rocket.
[1161.48 → 1161.76] There you go.
[1161.96 → 1164.04] If you use a hash rocket instead of a skinny arrow,
[1164.16 → 1165.34] you get a function that's bound
[1165.34 → 1166.42] to the current object.
[1167.06 → 1168.22] So, basically,
[1168.32 → 1169.82] anytime you're doing something fancy
[1169.82 → 1171.44] with, you know, with jQuery
[1171.44 → 1172.80] where you have an AJAX callback
[1172.80 → 1175.02] and you need to have your function stay bound
[1175.02 → 1175.78] to the current objects
[1175.78 → 1177.60] that you can reference, you know, everything else,
[1177.60 → 1179.12] you can use a fat arrow
[1179.12 → 1180.48] to make sure that it stays bound.
[1181.02 → 1182.20] And it works the same way in classes.
[1182.36 → 1183.40] If you have a method on a class,
[1183.48 → 1184.78] you know, you're going to pass that to a callback
[1184.78 → 1186.10] or pass that to something async.
[1186.46 → 1187.74] You can define that with a fat arrow
[1187.74 → 1189.08] and that means you'll always stay bound
[1189.08 → 1191.70] to the instance of the class that you're creating.
[1191.80 → 1193.00] So, you don't have to worry about
[1193.00 → 1194.60] creating a special wrapper function
[1194.60 → 1196.40] when you're ready to go do that callback.
[1197.08 → 1198.06] So, that's a little convenience.
[1199.06 → 1202.64] What about when ECMAScript 5's bind
[1202.64 → 1205.20] is natively supported on functions?
[1205.20 → 1207.96] That's going to be a wonderful day.
[1208.24 → 1211.60] So, there's been a lot of requests
[1211.60 → 1213.34] and talk about, you know,
[1213.38 → 1214.62] adding things like getters and setters
[1214.62 → 1216.02] which are starting to get better supported
[1216.02 → 1217.82] to the CoffeeScript syntax.
[1218.70 → 1220.28] And that would be fantastic.
[1220.84 → 1221.66] And, you know, if...
[1221.66 → 1223.18] So, taking the function binding example,
[1223.72 → 1225.88] when the day comes that bind is supported
[1225.88 → 1226.80] across all the browsers
[1226.80 → 1228.14] and you can rely on it,
[1228.22 → 1229.42] then we could switch our implementation
[1229.42 → 1231.16] to actually use bind
[1231.16 → 1233.18] and, you know, all your code would still work
[1233.18 → 1235.62] across all browsers like it had before
[1235.62 → 1238.74] and would now just work in a better way.
[1239.74 → 1240.50] And I think, in general,
[1240.82 → 1241.86] we would hope to do that
[1241.86 → 1243.40] with ECMAScript features
[1243.40 → 1244.40] that start being supported.
[1245.04 → 1246.80] So, Jeremy, are you using CoffeeScript
[1246.80 → 1248.68] on the client side or the server side?
[1249.44 → 1250.58] So, I've been using it
[1250.58 → 1252.10] for a couple little fun projects
[1252.10 → 1253.28] and for some art projects.
[1253.38 → 1255.22] I've been using it with Canvas a lot
[1255.22 → 1256.58] because that's been a ton of fun
[1256.58 → 1258.68] to take, you know, old processing sketches
[1258.68 → 1260.84] and to do them in CoffeeScript
[1260.84 → 1261.90] and Canvas
[1261.90 → 1264.34] and do things like the Buddha Brat fractal
[1264.34 → 1268.06] where you have this great sort of
[1268.06 → 1269.46] inverted Mandelbrot fractal.
[1269.56 → 1270.80] And it's actually amazing
[1270.80 → 1271.38] because, you know,
[1271.40 → 1272.30] if you do it in processing
[1272.30 → 1272.80] and you have it,
[1272.86 → 1274.24] you're using Java and you think...
[1275.68 → 1276.18] And actually,
[1276.34 → 1277.28] so some of my background
[1277.28 → 1278.54] is in working on Ruby processing,
[1278.74 → 1280.86] which is doing processing through Ruby.
[1281.68 → 1283.90] And so comparing the Ruby version
[1283.90 → 1285.38] of a Buddha Brat fractal
[1285.38 → 1287.08] to the CoffeeScript and Canvas version,
[1287.08 → 1288.82] like the speed is just unreal.
[1289.20 → 1290.62] You can have, you know,
[1290.66 → 1292.30] these great mathematically intensive
[1292.30 → 1294.04] computations running in the browser
[1294.04 → 1295.20] and going so much
[1295.20 → 1297.14] and being comparable to the speed
[1297.14 → 1298.64] at which processing would do them,
[1298.70 → 1299.56] you know, in the JVM.
[1300.30 → 1301.12] So, yeah,
[1301.18 → 1302.36] so I've been playing a lot with that.
[1302.46 → 1303.84] And then also been using it
[1303.84 → 1304.82] a little bit on the server side
[1304.82 → 1307.24] for some Node.js applications.
[1307.36 → 1308.46] I've been using it with Express,
[1309.18 → 1310.34] which has been a lot of fun too
[1310.34 → 1311.76] because it makes Express
[1311.76 → 1312.80] really fun to work with.
[1313.68 → 1316.32] And then also just raw Node.js.
[1316.32 → 1318.80] We have a piece of document cloud,
[1318.90 → 1319.74] which is a pixel tracker
[1319.74 → 1322.86] because people embed the documents
[1322.86 → 1323.96] that they upload
[1323.96 → 1325.72] on the different websites.
[1325.90 → 1327.34] So you'll have the Chicago Tribune.
[1327.52 → 1328.04] Right now,
[1328.08 → 1328.58] the Chicago Tribune
[1328.58 → 1329.66] has a bunch of great documents
[1329.66 → 1331.68] regarding the Blagojevich trial.
[1332.20 → 1333.38] And I think they've got hundreds
[1333.38 → 1334.32] and hundreds of them in there.
[1334.84 → 1336.68] And so we have a little pixel tracker
[1336.68 → 1337.66] so that we can keep track
[1337.66 → 1339.30] of the remote URL
[1339.30 → 1340.14] that people are embedding
[1340.14 → 1340.86] these documents at.
[1340.92 → 1342.20] And we can start sending traffic to them
[1342.20 → 1343.72] when we have a public search.
[1343.72 → 1344.68] And that's written in Node.js
[1344.68 → 1345.48] and CoffeeScript.
[1346.24 → 1347.02] And yep,
[1347.30 → 1348.06] it's about 100 lines.
[1348.20 → 1348.56] It's pretty short.
[1349.60 → 1349.80] Okay.
[1349.94 → 1351.92] So with Node.js,
[1352.80 → 1354.84] I noticed that it's actually
[1354.84 → 1355.98] one of the requirements
[1355.98 → 1356.70] for CoffeeScript.
[1357.78 → 1359.80] And the compiler actually runs
[1359.80 → 1360.82] on top of CoffeeScript,
[1361.02 → 1361.98] Node.js rather?
[1363.08 → 1363.98] Yep, that's correct.
[1364.44 → 1366.32] So CoffeeScript is written
[1366.32 → 1367.50] in CoffeeScript itself.
[1367.84 → 1368.76] When it started out,
[1368.82 → 1370.04] it was a Ruby program
[1370.04 → 1371.66] because we didn't have anything
[1371.66 → 1372.24] to write it with.
[1372.74 → 1373.76] So I actually started with Ruby
[1373.76 → 1374.40] and with Rack.
[1375.52 → 1377.16] And then it built and built
[1377.16 → 1378.42] and eventually it became
[1378.42 → 1379.78] a viable language
[1379.78 → 1382.90] that worked in the browser
[1382.90 → 1384.60] and worked in Node.js.
[1385.04 → 1386.00] And then there was a big,
[1386.04 → 1387.62] I think it was around 0.3.0,
[1387.76 → 1390.24] but a really sort of big switch.
[1390.42 → 1391.06] So I rewrote,
[1391.20 → 1392.04] I basically ported
[1392.04 → 1394.00] the entire Ruby compiler
[1394.00 → 1395.74] over to CoffeeScript itself.
[1396.06 → 1398.50] And then I ran it on itself.
[1399.16 → 1400.58] And then I ran that parser
[1400.58 → 1401.08] on itself.
[1401.20 → 1402.20] And then we had a completely
[1402.20 → 1404.28] bootstrapped compiler
[1404.28 → 1404.82] that basically,
[1404.94 → 1405.88] so now it compiles itself
[1405.88 → 1406.86] and the source code
[1406.86 → 1407.78] is written in CoffeeScript.
[1409.04 → 1409.54] And so, yeah,
[1409.62 → 1411.54] so I played around a little bit
[1411.54 → 1412.66] with doing it on Narwhal
[1412.66 → 1414.16] and Rhino as opposed to Node.
[1414.26 → 1415.70] But then just the speed of Node
[1415.70 → 1416.62] in terms of me,
[1416.74 → 1417.84] because compiling can take
[1417.84 → 1418.22] a little while
[1418.22 → 1419.12] to generate the parser,
[1419.96 → 1420.60] the speed of Node
[1420.60 → 1421.20] has been great.
[1422.24 → 1423.70] And so now the basic,
[1423.94 → 1425.12] the server-side version of it
[1425.12 → 1426.44] that you would install
[1426.44 → 1427.56] into user local bin
[1427.56 → 1428.14] and you would use
[1428.14 → 1428.84] from the command line
[1428.84 → 1430.20] is based on Node.
[1430.70 → 1432.02] But the compiler also
[1432.02 → 1432.96] runs in the browser too,
[1433.08 → 1433.66] so the JavaScript
[1433.66 → 1434.90] is pretty Node-agnostic
[1434.90 → 1435.70] at the core.
[1435.92 → 1436.94] You can run it in Firefox
[1436.94 → 1438.10] or Internet Explorer or whatever.
[1438.38 → 1439.32] So more than just Node,
[1439.42 → 1440.60] it also has a dependency,
[1440.96 → 1443.30] or I guess it can be aided
[1443.30 → 1444.38] in the installation process
[1444.38 → 1445.66] with Node Package Manager.
[1445.82 → 1446.28] Have we found
[1446.28 → 1448.32] our default package manager
[1448.32 → 1448.92] for Node now?
[1450.10 → 1450.80] As NPM?
[1450.90 → 1451.54] Yeah, I think NPM
[1451.54 → 1452.34] has won the battle
[1452.34 → 1452.80] at this point.
[1454.14 → 1455.70] Well, development node.
[1455.70 → 1457.92] TJ Holloway Chuck's
[1457.92 → 1459.80] Kiwi Package Manager
[1459.80 → 1461.28] seems to have halted now,
[1461.42 → 1463.28] so NPM seems to be
[1463.28 → 1463.76] the default.
[1464.06 → 1466.12] So why the dependency
[1466.12 → 1468.96] on Node
[1468.96 → 1471.18] from a parsing standpoint?
[1471.18 → 1474.12] It's just a JavaScript runtime.
[1474.60 → 1475.94] Because it also does run
[1475.94 → 1476.30] in the browser,
[1476.38 → 1476.86] and people have gotten
[1476.86 → 1478.10] it to run on Rhino also.
[1478.26 → 1478.94] It doesn't really matter
[1478.94 → 1479.42] where you run it.
[1479.46 → 1481.26] It's just our default runtime.
[1481.86 → 1482.36] But you can take,
[1482.46 → 1483.70] so there's a compiled,
[1484.36 → 1485.62] if you go into the
[1485.62 → 1486.34] extras slash
[1486.34 → 1488.28] coffeescript.js directory,
[1488.64 → 1489.80] that's a compressed,
[1490.04 → 1491.60] minified, compiled version
[1491.60 → 1492.50] of the entire compiler,
[1492.60 → 1493.12] and you can drop that
[1493.12 → 1493.76] onto a web page.
[1493.82 → 1494.62] You can load that
[1494.62 → 1495.02] into Rhino
[1495.02 → 1496.94] and work with that.
[1497.34 → 1498.34] Although you do have
[1498.34 → 1499.12] some hooks to use
[1499.12 → 1499.70] Coffee directly
[1499.70 → 1500.18] in the server.
[1502.60 → 1503.22] Some hooks?
[1503.32 → 1504.58] You mean the Node hooks?
[1504.84 → 1505.76] Yeah, you could use Coffee.
[1506.04 → 1506.90] You've got some examples
[1506.90 → 1507.32] on the website
[1507.32 → 1508.30] of using Coffee
[1508.30 → 1510.02] as your CoffeeScript
[1510.02 → 1511.04] in Node, right?
[1511.50 → 1511.82] Yeah.
[1512.64 → 1513.08] Right.
[1513.20 → 1514.44] So that was a special hook
[1514.44 → 1515.36] that was actually,
[1515.44 → 1516.24] that was added to Node,
[1516.30 → 1517.60] I think, by Tim Smart,
[1518.36 → 1519.66] so that if you have
[1519.66 → 1520.46] a different file extension
[1520.46 → 1521.18] that's not JS,
[1521.36 → 1522.00] Node can run
[1522.00 → 1522.70] a preprocessor
[1522.70 → 1523.76] like CoffeeScript on it
[1523.76 → 1524.58] and then run it directly.
[1525.10 → 1525.72] I still don't,
[1525.80 → 1526.54] because of the debugging
[1526.54 → 1527.22] reason that we talked
[1527.22 → 1527.70] about before,
[1527.80 → 1528.64] I still don't recommend
[1528.64 → 1529.46] running it directly
[1529.46 → 1530.20] because effectively
[1530.20 → 1530.80] what you're doing
[1530.80 → 1531.48] is you're reading
[1531.48 → 1532.32] in a file
[1532.32 → 1533.14] and then you're
[1533.14 → 1534.20] generating JavaScript
[1534.20 → 1534.76] in memory
[1534.76 → 1535.16] and then you're
[1535.16 → 1535.76] calling evil
[1535.76 → 1536.48] to run it,
[1536.60 → 1537.50] which will work fine,
[1537.58 → 1537.98] but as soon as
[1537.98 → 1538.70] you have to debug that,
[1539.06 → 1539.52] you're debugging
[1539.52 → 1540.28] a huge evil
[1540.28 → 1541.42] and that's not very fun.
[1541.80 → 1542.68] So I still recommend
[1542.68 → 1543.62] compiling it to JavaScript
[1543.62 → 1544.42] before you actually
[1544.42 → 1545.02] launch Node
[1545.02 → 1546.46] in both cases
[1546.46 → 1547.42] for both the server
[1547.42 → 1550.12] and for Node work,
[1550.22 → 1551.14] but it's certainly possible.
[1551.52 → 1552.38] Let's talk about
[1552.38 → 1553.36] compilation for a second
[1553.36 → 1553.96] because you've got
[1553.96 → 1555.40] several different options.
[1555.40 → 1556.84] I guess the default
[1556.84 → 1557.30] that I'm using
[1557.30 → 1558.40] is just a Coffee Watch
[1558.40 → 1560.12] command line interface,
[1560.24 → 1560.88] but there's also
[1560.88 → 1562.30] a lot of community
[1562.30 → 1563.58] contributed scripts
[1563.58 → 1564.62] for Rack
[1564.62 → 1567.48] and for Rails plugins
[1567.48 → 1568.36] and others.
[1568.36 → 1569.90] Yeah, there's a great
[1569.90 → 1571.06] resources section on,
[1571.14 → 1572.00] so coffeescript.org
[1572.00 → 1572.44] is the webpage
[1572.44 → 1573.20] and there are a resources
[1573.20 → 1573.98] section down at the bottom
[1573.98 → 1574.62] with a bunch
[1574.62 → 1575.42] of different syntax
[1575.42 → 1576.46] highlighters and integration
[1576.46 → 1578.58] into different Rails
[1578.58 → 1579.48] and Rack
[1579.48 → 1580.32] and I think there might be
[1580.32 → 1581.04] a Python 1 too,
[1581.30 → 1583.38] ways to compile it
[1583.38 → 1584.38] and to preprocess it
[1584.38 → 1584.84] if you have it
[1584.84 → 1585.68] as part of a website.
[1586.50 → 1587.22] So those just make it
[1587.22 → 1587.68] more convenient.
[1588.32 → 1588.84] But the basic,
[1588.92 → 1589.48] you can also use
[1589.48 → 1590.58] the basic Coffee command
[1590.58 → 1591.42] pretty easily
[1591.42 → 1592.32] because it can watch,
[1592.58 → 1594.02] if you do Coffee Watch
[1594.02 → 1595.12] and then a directory
[1595.12 → 1596.48] and give it
[1596.48 → 1597.26] an output directory,
[1597.52 → 1598.24] it will compile
[1598.24 → 1599.20] every CoffeeScript file
[1599.20 → 1599.64] that's found,
[1599.72 → 1599.92] you know,
[1599.96 → 1600.98] recursively in the directory
[1600.98 → 1602.36] anytime it changes
[1602.36 → 1603.24] using Node's
[1603.24 → 1604.46] great watch file support
[1604.46 → 1604.98] which works,
[1605.74 → 1606.30] uses, you know,
[1606.38 → 1607.06] the file system
[1607.06 → 1607.98] to do perfect
[1607.98 → 1608.70] watching of files
[1608.70 → 1609.38] for when they change.
[1609.78 → 1610.82] It'll compile that over
[1610.82 → 1611.44] into the parallel
[1611.44 → 1612.24] directory structure
[1612.24 → 1612.92] in JavaScript.
[1613.56 → 1614.12] So that makes it
[1614.12 → 1614.48] pretty easy
[1614.48 → 1615.70] to have it running
[1615.70 → 1616.08] in the background
[1616.08 → 1616.56] and development
[1616.56 → 1617.18] and not have to worry
[1617.18 → 1617.48] about it.
[1617.54 → 1618.06] When you refresh
[1618.06 → 1618.76] your page,
[1618.82 → 1619.82] you'll get your new code.
[1620.12 → 1621.02] Yeah, that's exactly
[1621.02 → 1621.78] how I'm using it
[1621.78 → 1623.00] in a Titanium,
[1623.22 → 1624.12] Accelerator Titanium
[1624.12 → 1624.82] mobile application
[1624.82 → 1625.28] right now.
[1625.48 → 1626.38] It's written in JavaScript
[1626.38 → 1627.46] and just watching
[1627.46 → 1627.88] that folder
[1627.88 → 1628.60] and it spits out
[1628.60 → 1630.30] the whole tree
[1630.30 → 1631.42] into the output folder.
[1632.04 → 1632.60] As far as,
[1632.64 → 1632.80] you know,
[1632.82 → 1633.66] the debugging
[1633.66 → 1634.70] in Stack trace,
[1634.80 → 1635.46] Titanium currently
[1635.46 → 1636.24] doesn't support
[1636.24 → 1636.86] that in JavaScript
[1636.86 → 1637.60] anyway,
[1637.76 → 1638.72] but so one of the
[1638.72 → 1639.84] pluses that I get
[1639.84 → 1640.50] from CoffeeScript
[1640.50 → 1642.96] is that nice
[1642.96 → 1643.72] JS Lint
[1643.72 → 1646.04] evaluated script.
[1646.16 → 1646.26] You know,
[1646.28 → 1646.76] there's no more
[1646.76 → 1647.58] warnings in the
[1647.58 → 1648.60] Titanium compiler
[1648.60 → 1649.04] telling me
[1649.04 → 1649.34] that I missed
[1649.34 → 1650.28] a semicolon or something.
[1651.12 → 1651.32] Right.
[1651.52 → 1651.94] Yeah, I guess
[1651.94 → 1652.66] the Titanium compiler
[1652.66 → 1653.28] is very strict
[1653.28 → 1653.94] about the JavaScript
[1653.94 → 1654.64] that it accepts
[1654.64 → 1655.04] I've heard
[1655.04 → 1656.78] because I don't
[1656.78 → 1657.06] even know how
[1657.06 → 1657.46] it works.
[1657.72 → 1658.56] Does it turn it
[1658.56 → 1659.60] into Objective-C
[1659.60 → 1660.08] or do you know
[1660.08 → 1661.50] how that works?
[1661.72 → 1663.10] It creates native
[1663.10 → 1664.62] objects on the fly
[1664.62 → 1665.32] but it goes through
[1665.32 → 1666.00] even at runtime
[1666.00 → 1666.74] it goes through
[1666.74 → 1667.66] it uses WebKit
[1667.66 → 1669.54] to interpret
[1669.54 → 1670.06] the JavaScript
[1670.06 → 1670.54] and then they have
[1670.54 → 1671.48] these proxy objects
[1671.48 → 1672.74] that proxy between
[1672.74 → 1673.22] the JavaScript
[1673.22 → 1674.80] and the Cocoa object
[1674.80 → 1675.96] so it creates
[1675.96 → 1676.74] Cocoa objects
[1676.74 → 1677.16] at runtime.
[1678.30 → 1678.56] Great.
[1678.66 → 1678.92] So I guess
[1678.92 → 1679.18] you're actually
[1679.18 → 1680.16] using JavaScript core
[1680.16 → 1681.02] as an interpreter
[1681.02 → 1682.98] inside the app.
[1682.98 → 1683.38] Right.
[1683.44 → 1683.84] I'm not sure
[1683.84 → 1684.48] if it's
[1684.48 → 1686.98] the Vanilla
[1686.98 → 1687.58] WebKit
[1687.58 → 1688.56] JavaScript interpreter
[1688.56 → 1689.20] or if they've
[1689.20 → 1690.14] forked that as well.
[1691.32 → 1692.06] That's cool stuff.
[1692.86 → 1693.90] So it's a nice fit
[1693.90 → 1694.48] until they
[1694.48 → 1696.44] introduce a debugger
[1696.44 → 1697.10] for the JavaScript
[1697.10 → 1697.86] and this is like
[1697.86 → 1698.54] all upside
[1698.54 → 1699.12] no downside.
[1701.20 → 1701.68] Okay.
[1701.76 → 1702.16] So also
[1702.16 → 1702.96] on the debugging
[1702.96 → 1703.78] you mentioned
[1703.78 → 1704.54] before that
[1704.54 → 1706.74] if you're using
[1706.74 → 1707.42] it in the browser
[1707.42 → 1708.48] and there's an example
[1708.48 → 1709.48] on the website
[1709.48 → 1710.52] or there has been
[1710.52 → 1711.00] an example
[1711.00 → 1711.48] I've seen
[1711.48 → 1712.54] where you've used
[1712.54 → 1714.00] a text slash
[1714.00 → 1714.76] copy script
[1714.76 → 1716.22] script tag
[1716.22 → 1718.78] when you're using
[1718.78 → 1719.60] one of those
[1719.60 → 1721.26] rather
[1721.26 → 1722.88] when you
[1722.88 → 1724.52] use a script
[1724.52 → 1725.44] tag with
[1725.44 → 1726.48] text slash
[1726.48 → 1727.38] copy script
[1727.38 → 1728.16] as the
[1728.16 → 1729.20] content type
[1729.20 → 1730.54] do you get
[1730.54 → 1732.18] any enhanced
[1732.18 → 1732.64] debugging
[1732.64 → 1733.72] in the browser?
[1733.98 → 1734.54] For instance
[1734.54 → 1737.16] TJ Holloway
[1737.16 → 1737.64] Chuck's
[1737.64 → 1738.16] recent
[1738.16 → 1738.68] emulating
[1738.68 → 1739.12] engine
[1739.12 → 1739.80] Jade
[1739.80 → 1741.38] when you're
[1741.38 → 1741.68] using it
[1741.68 → 1742.16] in the browser
[1742.16 → 1742.78] it'll actually
[1742.78 → 1743.46] give you
[1743.46 → 1744.66] a complete
[1744.66 → 1745.44] stack trace
[1745.44 → 1746.24] of where the
[1746.24 → 1746.98] error occurred
[1746.98 → 1747.38] in your
[1747.38 → 1747.86] template?
[1748.48 → 1748.88] Is there anything
[1748.88 → 1749.52] like that
[1749.52 → 1750.02] you can do
[1750.02 → 1750.78] in CoffeeScript?
[1751.30 → 1752.52] So again
[1752.52 → 1753.00] it's not
[1753.00 → 1753.74] a completely
[1753.74 → 1754.50] static language
[1754.50 → 1755.66] like HTML is
[1755.66 → 1756.54] so yes
[1756.54 → 1757.98] if you do it
[1757.98 → 1758.46] in the browser
[1758.46 → 1759.38] and if you
[1759.38 → 1760.44] go to
[1760.44 → 1761.10] coffeeScript.org
[1761.10 → 1761.38] and you do
[1761.38 → 1761.72] the try
[1761.72 → 1762.32] CoffeeScript
[1762.32 → 1763.98] page
[1763.98 → 1765.52] then yes
[1765.52 → 1765.80] you will
[1765.80 → 1766.16] absolutely
[1766.16 → 1766.56] get the
[1766.56 → 1767.12] syntax error
[1767.12 → 1767.44] it'll tell
[1767.44 → 1767.68] you what
[1767.68 → 1768.02] line it
[1768.02 → 1768.46] occurred on
[1768.46 → 1768.68] and it'll
[1768.68 → 1769.04] show you
[1769.04 → 1769.54] what went
[1769.54 → 1769.80] wrong
[1769.80 → 1770.22] which is
[1770.22 → 1770.52] basically
[1770.52 → 1770.84] just a
[1770.84 → 1771.08] feature
[1771.08 → 1771.70] that our
[1771.70 → 1772.10] parser
[1772.10 → 1772.50] generator
[1772.50 → 1774.12] we use
[1774.12 → 1774.74] JSON
[1774.74 → 1775.78] which is
[1775.78 → 1778.70] a great
[1778.70 → 1779.10] parser
[1779.10 → 1779.34] generator
[1779.34 → 1779.50] for
[1779.50 → 1779.78] JavaScript
[1779.78 → 1780.24] so yes
[1780.24 → 1780.48] if you
[1780.48 → 1780.66] have a
[1780.66 → 1781.02] syntax error
[1781.02 → 1781.18] in your
[1781.18 → 1781.36] code
[1781.36 → 1782.58] that'll
[1782.58 → 1782.70] be
[1782.70 → 1782.96] pointed
[1782.96 → 1783.16] out
[1783.16 → 1783.26] to
[1783.26 → 1783.34] you
[1783.34 → 1783.48] but
[1783.48 → 1783.68] because
[1783.68 → 1783.80] it's
[1783.80 → 1783.94] not
[1783.94 → 1784.04] a
[1784.04 → 1784.24] static
[1784.24 → 1784.50] language
[1784.50 → 1784.68] you're
[1784.68 → 1784.86] actually
[1784.86 → 1785.16] running
[1785.16 → 1785.50] the code
[1785.50 → 1786.24] then you
[1786.24 → 1786.36] have
[1786.36 → 1786.50] your
[1786.50 → 1786.66] real
[1786.66 → 1786.96] problem
[1786.96 → 1787.16] which
[1787.16 → 1787.28] is
[1787.28 → 1787.50] not
[1787.50 → 1787.66] a
[1787.66 → 1787.96] syntax
[1787.96 → 1788.12] error
[1788.12 → 1788.30] your
[1788.30 → 1788.74] problem
[1788.74 → 1789.04] is
[1789.04 → 1789.42] you have
[1789.42 → 1789.70] a bug
[1789.70 → 1789.92] in your
[1789.92 → 1790.14] code
[1790.14 → 1790.90] and
[1790.90 → 1791.30] then
[1791.30 → 1791.66] you're
[1791.66 → 1791.92] basically
[1791.92 → 1792.18] doing
[1792.18 → 1792.30] an
[1792.30 → 1792.58] evil
[1792.58 → 1792.72] and
[1792.72 → 1792.92] that's
[1792.92 → 1793.02] the
[1793.02 → 1793.26] difficult
[1793.26 → 1793.52] part
[1793.52 → 1793.68] so
[1793.68 → 1793.80] the
[1793.80 → 1794.04] syntax
[1794.04 → 1794.28] errors
[1794.28 → 1794.52] aren't
[1794.52 → 1795.02] so much
[1795.02 → 1795.38] the issue
[1795.38 → 1795.94] for running
[1795.94 → 1796.24] it directly
[1796.24 → 1796.44] in the
[1796.44 → 1796.66] browser
[1796.66 → 1797.60] but
[1797.60 → 1798.90] calling an
[1798.90 → 1799.20] evil
[1799.20 → 1799.66] on code
[1799.66 → 1800.08] instead of
[1800.08 → 1800.54] loading it
[1800.54 → 1801.00] as a
[1801.00 → 1801.34] regular
[1801.34 → 1801.76] JavaScript
[1801.76 → 1802.30] is
[1802.30 → 1803.04] which is
[1803.04 → 1803.32] why
[1803.32 → 1803.58] it's
[1803.58 → 1804.02] recommended
[1804.02 → 1804.56] to compile
[1804.56 → 1805.00] the JavaScript
[1805.00 → 1805.38] first
[1805.38 → 1805.72] and then
[1805.72 → 1806.04] you don't
[1806.04 → 1806.32] have
[1806.32 → 1806.54] this
[1806.54 → 1806.88] problem
[1806.88 → 1807.60] at all
[1807.60 → 1808.20] but if
[1808.20 → 1808.32] you're
[1808.32 → 1808.46] just
[1808.46 → 1808.66] doing
[1808.66 → 1808.90] some
[1808.90 → 1809.20] fun
[1809.20 → 1809.60] scripting
[1809.60 → 1809.92] around
[1809.92 → 1810.30] and you're
[1810.30 → 1810.68] not too
[1810.68 → 1810.92] worried
[1810.92 → 1811.22] about
[1811.22 → 1811.76] having
[1811.76 → 1811.90] to
[1811.90 → 1812.08] debug
[1812.08 → 1812.22] a
[1812.22 → 1812.38] major
[1812.38 → 1812.92] application
[1812.92 → 1813.64] then
[1813.64 → 1813.86] the
[1813.86 → 1814.12] text
[1814.12 → 1814.40] slash
[1814.40 → 1814.78] CoffeeScript
[1814.78 → 1814.96] thing
[1814.96 → 1815.06] is
[1815.06 → 1815.22] pretty
[1815.22 → 1815.48] fun
[1815.48 → 1815.78] and so
[1815.78 → 1816.02] that's
[1816.02 → 1816.32] what
[1816.32 → 1817.16] CoffeeScript
[1817.16 → 1817.72] uses
[1817.72 → 1818.86] to hook
[1818.86 → 1819.38] into jQuery
[1819.38 → 1820.00] and set up
[1820.00 → 1820.22] the
[1820.22 → 1820.86] try CoffeeScript
[1820.86 → 1821.20] box
[1821.20 → 1821.46] that's
[1821.46 → 1821.78] all done
[1821.78 → 1822.08] with the
[1822.08 → 1822.30] little
[1822.30 → 1822.62] text
[1822.62 → 1823.42] tag down
[1823.42 → 1823.60] at the
[1823.60 → 1823.78] bottom
[1823.78 → 1824.68] and I think
[1824.68 → 1824.98] the best
[1824.98 → 1825.28] example
[1825.28 → 1825.54] of it
[1825.54 → 1825.92] is this
[1825.92 → 1826.44] website
[1826.44 → 1826.94] the
[1826.94 → 1827.48] Lincolnshire
[1827.48 → 1828.86] poacher
[1828.86 → 1830.02] by Chris
[1830.02 → 1830.28] Lloyd
[1830.28 → 1830.84] which has
[1830.84 → 1831.10] a whole
[1831.10 → 1831.32] bunch
[1831.32 → 1831.54] of
[1831.54 → 1831.98] Raphael
[1831.98 → 1832.32] sketches
[1832.32 → 1832.80] that are
[1832.80 → 1833.00] written
[1833.00 → 1833.24] in
[1833.24 → 1833.66] CoffeeScript
[1833.66 → 1833.88] down
[1833.88 → 1834.08] at the
[1834.08 → 1834.24] bottom
[1834.24 → 1834.44] of the
[1834.44 → 1834.70] page
[1834.70 → 1835.26] and you
[1835.26 → 1835.52] can click
[1835.52 → 1835.80] on the
[1835.80 → 1836.12] refresh
[1836.12 → 1836.56] button
[1836.56 → 1837.34] to redraw
[1837.34 → 1837.92] the
[1837.92 → 1838.34] Raphael
[1838.34 → 1838.68] sketches
[1838.68 → 1839.14] and so
[1839.14 → 1839.52] those are
[1839.52 → 1840.34] a good
[1840.34 → 1840.66] example
[1840.66 → 1841.34] of a
[1841.34 → 1841.50] nice
[1841.50 → 1841.72] place
[1841.72 → 1841.96] to use
[1841.96 → 1842.20] it
[1842.20 → 1843.50] okay
[1843.50 → 1843.72] so
[1843.72 → 1844.02] a quick
[1844.02 → 1844.42] question
[1844.42 → 1844.90] on
[1844.90 → 1845.84] a couple
[1845.84 → 1846.08] of your
[1846.08 → 1846.24] other
[1846.24 → 1846.70] projects
[1846.70 → 1847.30] you've
[1847.30 → 1847.96] also
[1847.96 → 1848.36] written
[1848.36 → 1849.38] underscore
[1849.38 → 1849.82] JS
[1849.82 → 1850.36] and
[1850.36 → 1850.90] Docker
[1850.90 → 1852.50] with
[1852.50 → 1853.24] underscore
[1853.24 → 1853.74] JS
[1853.74 → 1854.32] was that
[1854.32 → 1854.62] actually
[1854.62 → 1855.02] originally
[1855.02 → 1855.28] written
[1855.28 → 1855.54] in
[1855.54 → 1856.12] CoffeeScript
[1856.12 → 1856.62] or was
[1856.62 → 1856.72] it
[1856.72 → 1856.94] written
[1856.94 → 1857.42] originally
[1857.42 → 1857.62] in
[1857.62 → 1857.96] JavaScript
[1857.96 → 1859.34] so
[1859.34 → 1859.92] that was
[1859.92 → 1860.04] written
[1860.04 → 1860.16] in
[1860.16 → 1860.40] JavaScript
[1860.40 → 1860.74] first
[1860.74 → 1860.96] that's
[1860.96 → 1861.10] from
[1861.10 → 1861.28] the
[1861.28 → 1861.62] fall
[1861.62 → 1862.08] actually
[1862.08 → 1862.30] so
[1862.30 → 1862.78] that's
[1862.78 → 1863.06] from
[1863.06 → 1863.76] when I
[1863.76 → 1864.02] first
[1864.02 → 1864.24] started
[1864.24 → 1864.38] the
[1864.38 → 1864.64] Document
[1864.64 → 1864.84] Cloud
[1864.84 → 1865.32] project
[1865.32 → 1866.12] so
[1866.12 → 1866.78] at
[1866.78 → 1867.06] Document
[1867.06 → 1867.34] Cloud
[1867.34 → 1868.22] everything
[1868.22 → 1868.54] that we
[1868.54 → 1868.80] do
[1868.80 → 1869.36] has to
[1869.36 → 1869.46] be
[1869.46 → 1869.72] released
[1869.72 → 1869.96] open
[1869.96 → 1870.24] source
[1870.24 → 1870.56] it's
[1870.56 → 1870.74] funded
[1870.74 → 1871.00] by the
[1871.00 → 1871.12] Knight
[1871.12 → 1871.48] Foundation
[1871.48 → 1871.94] the idea
[1871.94 → 1872.38] is that
[1872.38 → 1873.00] we both
[1873.00 → 1873.58] make this
[1873.58 → 1873.90] service
[1873.90 → 1874.44] and also
[1874.44 → 1875.24] every single
[1875.24 → 1875.82] bit of code
[1875.82 → 1876.00] that we
[1876.00 → 1876.50] write will be
[1876.50 → 1877.08] made open
[1877.08 → 1877.48] source sooner
[1877.48 → 1877.78] or later
[1877.78 → 1878.58] so it was
[1878.58 → 1879.00] extracted
[1879.00 → 1879.92] directly from
[1879.92 → 1880.98] the application
[1880.98 → 1881.60] there and it
[1881.60 → 1882.04] was basically
[1882.04 → 1882.70] just a collection
[1882.70 → 1883.14] of all the
[1883.14 → 1883.76] little functional
[1883.76 → 1884.30] helpers that
[1884.30 → 1884.66] you might
[1884.66 → 1885.66] want to use
[1885.66 → 1885.98] when you're
[1885.98 → 1886.14] writing
[1886.14 → 1886.48] JavaScript
[1886.48 → 1886.94] and trying
[1886.94 → 1887.24] to do
[1887.24 → 1887.66] sophisticated
[1887.66 → 1888.14] stuff on
[1888.14 → 1888.44] the client
[1888.44 → 1888.70] side
[1888.70 → 1889.54] being able
[1889.54 → 1890.14] to select
[1890.14 → 1890.52] and filter
[1890.52 → 1891.10] and reduce
[1891.10 → 1891.64] a lot of
[1891.64 → 1891.94] things that are
[1891.94 → 1892.20] now in
[1892.20 → 1892.88] ECMAScript 5
[1892.88 → 1893.58] that underscore
[1893.58 → 1894.34] uses if they're
[1894.34 → 1894.66] available
[1894.66 → 1896.12] so that was
[1896.12 → 1896.44] not written
[1896.44 → 1896.88] in CoffeeScript
[1896.88 → 1897.26] first
[1897.26 → 1898.70] but it was
[1898.70 → 1899.08] kind of
[1899.08 → 1899.40] test
[1899.40 → 1901.62] so besides
[1901.62 → 1902.40] having the
[1902.40 → 1903.18] compiler of
[1903.18 → 1903.60] CoffeeScript
[1903.60 → 1904.30] itself be
[1904.30 → 1904.62] written in
[1904.62 → 1905.04] CoffeeScript
[1905.04 → 1906.02] doing the
[1906.02 → 1906.34] underscore
[1906.34 → 1907.02] port was
[1907.02 → 1907.38] kind of
[1907.38 → 1907.78] test of
[1907.78 → 1908.50] alright I've
[1908.50 → 1908.78] got this
[1908.78 → 1909.18] real world
[1909.18 → 1909.52] library
[1909.52 → 1909.90] I've got a
[1909.90 → 1910.30] bunch of
[1910.30 → 1910.74] performance
[1910.74 → 1911.30] benchmarks
[1911.30 → 1911.74] so I can
[1911.74 → 1912.12] know if
[1912.12 → 1912.46] it slows
[1912.46 → 1912.82] down
[1912.82 → 1914.22] I've got
[1914.22 → 1915.12] a big test
[1915.12 → 1915.66] suite, so I
[1915.66 → 1916.00] can make
[1916.00 → 1916.36] sure that it
[1916.36 → 1916.60] behaves
[1916.60 → 1917.10] correctly and
[1917.10 → 1917.32] is it
[1917.32 → 1918.48] possible to
[1918.48 → 1919.04] write it in
[1919.04 → 1919.38] CoffeeScript
[1919.38 → 1919.78] and have it
[1919.78 → 1920.74] work and so
[1920.74 → 1921.16] the answer
[1921.16 → 1922.04] was yes it
[1922.04 → 1922.56] is possible
[1922.56 → 1923.42] and we've
[1923.42 → 1923.92] got that as
[1923.92 → 1924.18] one of the
[1924.18 → 1925.02] examples in
[1925.02 → 1925.72] the CoffeeScript
[1925.72 → 1926.66] checkout and
[1926.66 → 1927.22] also that it's
[1927.22 → 1927.66] actually a little
[1927.66 → 1928.48] bit faster than
[1928.48 → 1928.88] the JavaScript
[1928.88 → 1929.58] version because
[1929.58 → 1930.14] of things like
[1930.14 → 1931.02] comprehensions where
[1931.02 → 1932.82] in JavaScript you
[1932.82 → 1933.32] would have had to
[1933.32 → 1934.04] write out the
[1934.04 → 1934.56] for loops by
[1934.56 → 1935.16] hand every time
[1935.16 → 1935.74] instead of using
[1935.74 → 1936.28] an or
[1936.28 → 1937.16] for each but
[1937.16 → 1938.08] you don't have to
[1938.08 → 1938.72] worry about that as
[1938.72 → 1939.34] much in CoffeeScript
[1939.34 → 1939.66] because it will
[1939.66 → 1940.32] generate the
[1940.32 → 1940.92] efficient for
[1940.92 → 1941.56] loops for you
[1941.56 → 1942.42] where possible
[1942.42 → 1943.30] so it ended
[1943.30 → 1943.96] up beating the
[1943.96 → 1944.90] original underscore
[1944.90 → 1945.72] and a couple of
[1945.72 → 1946.46] little benchmarks
[1946.46 → 1946.96] by a bit
[1946.96 → 1948.68] speaking of those
[1948.68 → 1949.22] for loops real
[1949.22 → 1950.42] quick the one
[1950.42 → 1950.82] that we didn't
[1950.82 → 1951.30] talk about was
[1951.30 → 1952.08] the for of
[1952.08 → 1952.92] that I fell in
[1952.92 → 1953.46] love with
[1953.46 → 1955.06] the for of
[1955.06 → 1955.86] right the
[1955.86 → 1956.72] yeah you
[1956.72 → 1958.14] had basically
[1958.14 → 1958.52] we'll give you
[1958.52 → 1959.26] the key back
[1959.26 → 1961.54] and evaluate
[1961.54 → 1962.62] the object on
[1962.62 → 1962.94] the fly
[1962.94 → 1964.34] similar to what
[1964.34 → 1965.00] Ruby does where
[1965.00 → 1965.30] you can do
[1965.30 → 1965.86] multiple keys
[1965.86 → 1966.66] into a loop
[1966.66 → 1969.06] right so the
[1969.06 → 1970.26] comprehensions in
[1970.26 → 1970.98] CoffeeScript you
[1970.98 → 1971.70] have I guess you
[1971.70 → 1971.98] have sort of
[1971.98 → 1972.42] three basic
[1972.42 → 1972.92] types you
[1972.92 → 1973.44] have you can
[1973.44 → 1974.36] comprehend over
[1974.36 → 1975.68] an array or
[1975.68 → 1976.46] over an object
[1976.46 → 1976.98] or over a
[1976.98 → 1977.96] range so the
[1977.96 → 1978.46] range is the
[1978.46 → 1978.94] simple one the
[1978.94 → 1979.66] range is basically
[1979.66 → 1980.48] a for loop with
[1980.48 → 1981.46] a fixed start and
[1981.46 → 1982.16] end you know from
[1982.16 → 1983.10] one up to ten do
[1983.10 → 1985.48] this so you say
[1985.48 → 1987.24] you know for I
[1987.24 → 1988.68] in range and you
[1988.68 → 1989.24] give it a start and
[1989.24 → 1991.44] end point and
[1991.44 → 1993.16] and then you have
[1993.16 → 1993.50] the array
[1993.50 → 1994.30] comprehensions where
[1994.30 → 1995.40] you can say for
[1995.40 → 1998.12] value comma index
[1998.12 → 1999.90] in array and then
[1999.90 → 2000.66] you also have objected
[2000.66 → 2001.34] comprehensions where
[2001.34 → 2002.24] you can say for
[2002.24 → 2003.72] key comma value of
[2003.72 → 2005.00] object and we
[2005.00 → 2005.60] actually just added
[2005.60 → 2006.94] a new one a new
[2006.94 → 2007.64] variant of it where
[2007.64 → 2009.30] you can say for
[2009.30 → 2010.58] all key comma value
[2010.58 → 2011.38] of object which
[2011.38 → 2012.66] which will so the
[2012.66 → 2013.18] difference between
[2013.18 → 2013.90] there is a
[2013.90 → 2014.74] subtle JavaScript thing
[2014.74 → 2015.80] where usually a for
[2015.80 → 2017.48] in JavaScript will
[2017.48 → 2018.14] look up the entire
[2018.14 → 2019.26] prototype chain and
[2019.26 → 2020.06] if you've added
[2020.06 → 2021.72] methods like say
[2021.72 → 2023.22] prototype JS does to
[2023.22 → 2024.16] the array prototype
[2024.16 → 2025.56] you're going to get
[2025.56 → 2027.24] methods that you don't
[2027.24 → 2027.88] care about that you're
[2027.88 → 2029.08] not interested in so
[2029.08 → 2030.02] by default coffee
[2030.02 → 2030.90] script is safe and
[2030.90 → 2032.18] only looks in and
[2032.18 → 2033.02] uses a has own
[2033.02 → 2033.78] property check to
[2033.78 → 2034.74] only look in the
[2034.74 → 2036.28] the closest object but if
[2036.28 → 2036.82] you want to speed that
[2036.82 → 2037.34] up a little bit you
[2037.34 → 2038.52] can say for all key
[2038.52 → 2039.60] comma value of object
[2039.60 → 2040.14] and then that'll give
[2040.14 → 2041.14] you everything with a
[2041.14 → 2043.54] with a vanilla JavaScript
[2043.54 → 2044.74] for in with no
[2044.74 → 2046.50] special checks and so
[2046.50 → 2047.54] this gives you a
[2047.54 → 2048.50] unified interface these
[2048.50 → 2049.26] three different kinds of
[2049.26 → 2050.04] comprehensions because
[2050.04 → 2051.00] you can use all of
[2051.00 → 2052.54] them are expressions you
[2052.54 → 2053.42] can use them directly you
[2053.42 → 2054.06] know you can't usually
[2054.06 → 2055.12] just return for loop and
[2055.12 → 2055.86] have that mean anything
[2055.86 → 2056.64] but if you return a
[2056.64 → 2057.44] comprehension that'll
[2057.44 → 2059.44] give you back all the
[2059.44 → 2060.66] values the
[2060.66 → 2061.76] computed results of all
[2061.76 → 2062.54] of the values being
[2062.54 → 2063.78] passed through the
[2063.78 → 2064.60] block of code that
[2064.60 → 2065.78] you've given and they
[2065.78 → 2067.30] all work in identical
[2067.30 → 2068.86] ways with that so
[2068.86 → 2071.20] well this is the part of
[2071.20 → 2071.78] the interview where we
[2071.78 → 2072.66] turn it upside down
[2072.66 → 2073.60] the folks that we speak
[2073.60 → 2075.16] to usually who's on our
[2075.16 → 2076.34] open source radar so
[2076.34 → 2077.50] we get to turn it right
[2077.50 → 2078.88] back at you and ask what
[2078.88 → 2079.80] kind of projects are on
[2079.80 → 2080.80] your open source radar
[2080.80 → 2082.98] I'm getting pretty excited
[2082.98 → 2083.50] about it, so I think we
[2083.50 → 2084.70] talked in the fall you
[2084.70 → 2085.22] asked me the same
[2085.22 → 2086.32] question you know and
[2086.32 → 2087.62] I talked about node.js
[2087.62 → 2089.54] and you said that
[2089.54 → 2090.88] you know everyone's
[2090.88 → 2091.40] been saying that
[2091.40 → 2092.06] recently, and I think
[2092.06 → 2092.78] that's that's still
[2092.78 → 2093.64] definitely the case and
[2093.64 → 2094.68] still going strong and
[2094.68 → 2095.30] has a lot of
[2095.30 → 2096.24] steam and a bunch
[2096.24 → 2098.30] of great patches that
[2098.30 → 2099.56] that come out constantly
[2099.56 → 2100.76] and you have to keep up
[2100.76 → 2103.30] with, and I'm still
[2103.30 → 2104.60] waiting for the first
[2104.60 → 2106.94] sort of end to end you
[2106.94 → 2107.88] know or at least the
[2107.88 → 2108.94] first the first person
[2108.94 → 2109.72] who glues it together
[2109.72 → 2110.60] end to end where you
[2110.60 → 2111.82] actually have you know
[2111.82 → 2112.66] rich models in the
[2112.66 → 2114.42] browser with a good
[2114.42 → 2115.98] standard library of
[2115.98 → 2117.20] of common functions
[2117.20 → 2118.60] that then you know
[2118.60 → 2119.46] that then work
[2119.46 → 2120.30] seamlessly with the
[2120.30 → 2121.34] server side and you
[2121.34 → 2121.98] know maybe it
[2121.98 → 2122.92] integrates comments you
[2122.92 → 2124.06] get live updates across
[2124.06 → 2124.76] you know all of your
[2124.76 → 2125.98] models because this is
[2125.98 → 2126.68] something that any
[2126.68 → 2127.88] client side app that
[2127.88 → 2128.82] that does a lot of work
[2128.82 → 2129.66] in the browser ends up
[2129.66 → 2131.00] doing so in our case
[2131.00 → 2132.08] we're dealing with
[2132.08 → 2133.16] with journalists in the
[2133.16 → 2133.94] newsroom working with
[2133.94 → 2134.92] documents and writing
[2134.92 → 2135.90] stories and annotating
[2135.90 → 2137.54] the documents and you
[2137.54 → 2138.74] can share those between
[2138.74 → 2139.50] different newsrooms you
[2139.50 → 2140.16] could have someone you
[2140.16 → 2140.70] know in Chicago and
[2140.70 → 2141.50] someone in Miami working
[2141.50 → 2142.96] on the same project and
[2142.96 → 2143.68] annotating the same
[2143.68 → 2145.32] document and now you
[2145.32 → 2146.20] have to you know what
[2146.20 → 2146.74] you want to do is you
[2146.74 → 2147.44] want to be able to live
[2147.44 → 2148.32] update the changes back
[2148.32 → 2149.06] and forth when someone
[2149.06 → 2150.32] you know kind of like a
[2150.32 → 2151.40] Google wave style or an
[2151.40 → 2153.62] ether pad style thing where
[2153.62 → 2154.80] as soon as someone starts
[2154.80 → 2155.46] finishes typing
[2155.46 → 2156.24] orientation it appears
[2156.24 → 2157.74] instantly and you can
[2157.74 → 2158.60] really work together and
[2158.60 → 2159.38] collaborate in that way
[2159.38 → 2160.52] and that's something that
[2160.52 → 2161.66] JavaScript is a great
[2161.66 → 2163.14] language for enabling
[2163.14 → 2164.08] instead of like a rich
[2164.08 → 2164.88] flash app and that's
[2164.88 → 2165.56] something that is very
[2165.56 → 2166.32] complicated right now
[2166.32 → 2166.92] because you have to use
[2166.92 → 2168.82] comment you have to you
[2168.82 → 2169.58] know it's very
[2169.58 → 2170.60] difficult to get the
[2170.60 → 2171.38] changes pushed across
[2171.38 → 2172.06] correctly in a
[2172.06 → 2173.42] performant way and so
[2173.42 → 2174.36] node provides the
[2174.36 → 2175.42] performance that's needed
[2175.42 → 2176.96] for doing that well and
[2176.96 → 2178.16] web sockets coming of
[2178.16 → 2179.70] age are going to provide
[2179.70 → 2182.24] the comment replacement
[2182.24 → 2183.60] that's a little bit nicer
[2183.60 → 2185.68] to work with, and I think
[2185.68 → 2186.48] that someone's going to
[2186.48 → 2188.42] come out with an end-to-end
[2188.42 → 2189.56] solution you know that
[2189.56 → 2191.02] that knows how to talk to
[2191.02 → 2191.92] databases in the background
[2191.92 → 2193.42] for persisting data that
[2193.42 → 2194.68] has good ways of routing
[2194.68 → 2196.00] URLs to actions in the
[2196.00 → 2198.02] server that has client-side
[2198.02 → 2198.86] models that can be shared
[2198.86 → 2199.58] with the server and can
[2199.58 → 2200.54] do validations on both
[2200.54 → 2201.80] end and can transparently
[2201.80 → 2203.52] sync changes so all you
[2203.52 → 2204.18] have to worry about is
[2204.18 → 2205.04] basically your client-side
[2205.04 → 2205.68] app, and you can call
[2205.68 → 2207.02] save in the browser and
[2207.02 → 2207.96] it'll safely save it to
[2207.96 → 2209.18] the server with validations
[2209.18 → 2211.34] and has that all hooked
[2211.34 → 2212.60] together I think that'll be
[2212.60 → 2213.30] that's that's what I'm
[2213.30 → 2214.36] waiting for that's that's
[2214.36 → 2214.96] what I'm hoping to see in
[2214.96 → 2215.98] the next year that's quite
[2215.98 → 2216.78] the dream who'd have
[2216.78 → 2217.66] thought that five years
[2217.66 → 2218.82] ago you know and going
[2218.82 → 2219.74] into the next decade we'd
[2219.74 → 2220.42] be so excited about
[2220.42 → 2222.24] JavaScript yeah who
[2222.24 → 2224.28] would have thunk so
[2224.28 → 2225.22] where can folks catch up
[2225.22 → 2226.28] with you online the
[2226.28 → 2227.10] coffee script Twitter
[2227.10 → 2228.18] handle is that you or a
[2228.18 → 2229.24] fan that's actually not
[2229.24 → 2230.20] me that's that's an
[2230.20 → 2231.30] unofficial one but he
[2231.30 → 2232.06] answers questions pretty
[2232.06 → 2232.74] good too so you can ask
[2232.74 → 2233.86] him but if you want to
[2233.86 → 2235.08] so right now coffee script
[2235.08 → 2236.62] if you have an idea for
[2236.62 → 2237.68] an enhancement or a
[2237.68 → 2238.96] question or an issue you
[2238.96 → 2239.94] should use the GitHub
[2239.94 → 2241.60] issues page and if you
[2241.60 → 2242.38] want to just chat about
[2242.38 → 2243.36] it comes into the coffee
[2243.36 → 2244.74] script room all one word
[2244.74 → 2245.62] coffee script on free
[2245.62 → 2246.94] node that's the IRC room
[2246.94 → 2247.34] and there's usually
[2247.34 → 2248.30] someone who can answer
[2248.30 → 2248.92] your question there
[2248.92 → 2250.84] cool thanks for joining
[2250.84 → 2252.42] us today Jeremy all
[2252.42 → 2253.20] right thanks a lot it's
[2253.20 → 2253.56] been fun
[2253.56 → 2274.68] so how could I forget
[2274.68 → 2277.96] that's when I found
[2277.96 → 2281.40] myself for the first time
[2281.40 → 2285.90] safe in your arms and the
[2285.90 → 2287.22] dark passion
[2287.22 → 2287.74] you
[2287.74 → 2288.74] you
[2288.74 → 2289.74] you
[2289.74 → 2291.74] you
[2291.74 → 2293.74] you
[2293.74 → 2295.74] you
[2295.74 → 2297.74] you
[2297.74 → 2299.74] you
