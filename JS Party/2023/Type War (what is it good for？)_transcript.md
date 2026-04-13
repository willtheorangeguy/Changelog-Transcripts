[0.00 --> 11.38]  This is JS Party, your weekly celebration of JavaScript and the web.
[11.80 --> 13.86]  Are you missing out on the ChangeLog newsletter?
[14.32 --> 20.76]  Every Monday, I curate, contextualize, package up, and email you the developer news worth your attention.
[21.26 --> 26.60]  It's a totally free way to keep up with the fast pace of the software world the easy way.
[26.60 --> 30.08]  Sign up today at changelog.com slash news.
[30.30 --> 35.88]  Big thanks to our partners, Fastly.com, Fly.io, and Typesense.org.
[36.00 --> 38.40]  Okay, hey, it's party time, y'all.
[43.30 --> 47.92]  What's up, friends? I'm here with James Cowling, co-founder and CTO at Convex.
[48.06 --> 52.48]  They're one of our new sponsors, and they're building a full-stack platform for the TypeScript era.
[52.48 --> 58.64]  So, James, in your main navigation, you link to a page called Convex versus Firebase.
[59.22 --> 60.94]  How similar is Convex to Firebase?
[61.50 --> 66.00]  And if someone is quickly trying to grok what Convex is, is that a good comparison?
[66.58 --> 68.28]  I think it's a good starting point for sure.
[68.44 --> 69.84]  I mean, Firebase has been very impactful.
[70.28 --> 73.60]  And the people we speak to who use Firebase often love it,
[73.74 --> 77.04]  and they often lament the time they have to move off of Firebase
[77.04 --> 80.48]  because it's kind of failed to meet their needs as a growing company.
[80.48 --> 82.94]  So, Firebase falls short in a few ways.
[83.44 --> 86.60]  One is in terms of like a fully relational document model.
[87.02 --> 90.40]  One is in terms of having strong type system.
[90.78 --> 94.78]  One is in terms of having this full end-to-end consistency story
[94.78 --> 99.94]  where you write functions that run on an API server on the data that you can subscribe to.
[100.28 --> 103.78]  And so, one thing I think we see in the Firebase-style development model
[103.78 --> 108.82]  is that you have web applications talking directly to a database in a cloud Firestore.
[108.82 --> 114.60]  With Convex, what is different is you have your code talking to actual fully-fledged TypeScript functions
[114.60 --> 117.20]  running on your data that you can subscribe to.
[117.46 --> 120.46]  But I think the Firebase's comparison is fairly apt.
[120.54 --> 124.36]  And if someone is a Firebase user, I think you will love Convex.
[124.66 --> 127.14]  And it's certainly designed to fill that niche in the market.
[127.28 --> 130.10]  It's people who want to build applications without having to mess with infrastructure.
[130.60 --> 134.10]  In what way has infrastructure failed specifically application developers?
[134.10 --> 140.44]  I think if one was to compare what it looked like to build an application 10 plus years ago to today,
[140.60 --> 143.30]  it's gotten more complex, not less complex.
[143.48 --> 145.06]  There's a bewildering amount of frameworks.
[145.46 --> 151.78]  I think Google, for all their amazing work they do, has had a bad influence on how people build systems.
[151.88 --> 154.06]  Because oftentimes when someone wants to build a web app these days,
[154.12 --> 157.70]  they're told to like learn Kubernetes or something ridiculous like that.
[157.70 --> 163.62]  You know, these infrastructure platforms really resemble the shape of the underlying implementation,
[164.20 --> 167.46]  not the shape of the problem that the application developers are facing.
[167.74 --> 171.14]  And so even when before we started Convex, we're talking to customers, people are like,
[171.58 --> 174.62]  well, I just want someone to like manage my Kafka cluster.
[175.02 --> 176.86]  And I'd say, well, why do you even have Kafka?
[177.24 --> 178.38]  And like, well, I don't really know.
[178.48 --> 181.84]  I think the database falls over if I don't put a queue in front of it.
[181.96 --> 184.76]  Or like I need to like buffer some data somewhere.
[184.76 --> 189.92]  And what became clear is that the tools just weren't serving the needs of the application developers.
[190.42 --> 195.46]  And I think application developers and framework, front-end framework engineers understand the problem space
[195.46 --> 197.28]  because they spend all day doing it.
[197.44 --> 201.22]  They sometimes don't have the power to fix the problem because they don't build the database themselves.
[201.74 --> 204.94]  And I think oftentimes infra folks, you know, including myself,
[205.26 --> 207.66]  don't have enough empathy for the application developer.
[207.82 --> 210.06]  At the end of the day, all that matters is the application.
[210.62 --> 210.90]  Okay.
[210.90 --> 217.28]  If you're looking for a better type of backend, Convex is the full stack TypeScript development platform you've been looking for.
[217.62 --> 220.38]  Replace your database, server functions, and glue code.
[220.78 --> 222.98]  Get started at Convex.dev.
[223.22 --> 226.00]  That's C-O-N-V-E-X.dev.
[226.18 --> 228.18]  Again, Convex.dev.
[228.18 --> 251.72]  Hello, JS Party listeners.
[252.32 --> 254.92]  We're back with an emergency podcast today.
[255.14 --> 255.28]  Emergency!
[255.78 --> 256.62]  This is an emergency.
[256.62 --> 263.22]  We've bumped up our regularly scheduled programming to have this very important conversation with you all today.
[263.32 --> 267.96]  Because I'm getting the sense that you all need to process, because I know I certainly need to process.
[268.18 --> 269.14]  You need to co-process.
[269.82 --> 271.96]  And who better than to co-process with?
[272.34 --> 274.30]  Today with me on the show is Jared.
[274.42 --> 275.00]  Hello, Jared.
[275.18 --> 275.54]  Hello.
[276.08 --> 278.54]  Excited to co-process with you all.
[278.76 --> 279.18]  Yes.
[279.34 --> 279.60]  Yes.
[279.60 --> 281.56]  We're all co-processing together.
[282.22 --> 286.16]  I'm going to light some sage, you know, put on some mood music, you know.
[286.60 --> 288.18]  Mood lighting, I should say, not mood.
[288.30 --> 289.72]  Is mood music a thing?
[289.82 --> 290.30]  I don't know.
[290.38 --> 291.14]  We don't have to answer that.
[291.36 --> 291.54]  I think so.
[291.74 --> 292.78]  I think it's a different kind of mood.
[293.22 --> 293.88]  But yes.
[294.36 --> 294.76]  Okay.
[294.76 --> 299.98]  So we have a very, very, very special guest with us here today to co-process this really
[299.98 --> 300.74]  important topic.
[300.74 --> 305.86]  So we're going to be talking today about the little TypeScript dramatic brouhaha that's
[305.86 --> 307.46]  been going on within the community.
[308.02 --> 311.10]  If you don't know what I'm talking about, you just stay tuned.
[311.28 --> 312.02]  You'll find out.
[312.16 --> 314.32]  If you know what I'm talking about, then yeah.
[314.46 --> 316.24]  Like, aren't you glad you're listening to this?
[316.56 --> 317.06]  I know.
[317.16 --> 317.90]  Because I know I am.
[318.32 --> 321.78]  And so Rich Harris is here to help us co-process today.
[321.86 --> 322.52]  Welcome, Rich Harris.
[322.80 --> 323.08]  Hello.
[323.34 --> 324.10]  Hey, how's it going?
[324.18 --> 324.90]  Thanks for having me back.
[325.20 --> 325.48]  Yeah.
[325.86 --> 329.54]  And please, you don't need an introduction, but would you mind just telling-
[329.54 --> 330.20]  No introduction necessary.
[330.20 --> 330.58]  Yeah, yeah.
[330.62 --> 330.86]  I know.
[331.00 --> 332.22]  He's like Jay-Z, right?
[332.26 --> 333.14]  Oh, please do it anyways.
[333.54 --> 333.62]  Yeah.
[334.00 --> 335.06]  He's like the tech Jay-Z.
[335.86 --> 336.48]  So-
[336.48 --> 338.24]  Do you like that, Rich?
[338.26 --> 339.54]  Do you like me calling the tech Jay-Z?
[339.54 --> 341.86]  Is that a compliment for you or not sure?
[342.08 --> 343.06]  Can't quite work that out.
[343.36 --> 344.16]  I'll take it.
[345.06 --> 346.12]  I'll take it.
[346.40 --> 346.68]  Okay.
[346.80 --> 347.58]  So tech Jay-Z.
[347.90 --> 350.94]  Can you tell us a little bit about yourself for people who may not know you?
[351.38 --> 351.66]  Yeah.
[351.76 --> 356.28]  I'm a dude who tweets a lot and has apparently too many opinions, some of which get me in
[356.28 --> 358.56]  trouble, which I expect we'll talk about.
[359.00 --> 363.38]  Prior to that, I did a lot of open source things.
[363.80 --> 368.26]  I made a JavaScript module bundler called Rollup, and I started a UI framework called Svelte.
[368.52 --> 371.10]  And Svelte is what I work on day-to-day at Vassell.
[371.94 --> 372.98]  That's me, I guess.
[373.28 --> 374.56]  And you have a really cool British accent.
[375.12 --> 376.34]  It's not fake, right?
[376.34 --> 377.92]  It's like you are from England.
[378.38 --> 379.94]  This is truly how I speak.
[380.16 --> 380.52]  Okay.
[380.96 --> 381.26]  Cool.
[381.62 --> 382.82]  Just like the real Jay-Z.
[383.24 --> 383.76]  Oh my God.
[383.80 --> 385.52]  Imagine Jay-Z with a British accent.
[385.66 --> 386.32]  That would be great.
[386.40 --> 387.58]  Oh, that could be a good deep fake.
[387.80 --> 388.50]  Someone should work on that.
[388.50 --> 388.80]  For sure.
[389.00 --> 389.44]  For sure.
[389.50 --> 390.40]  Don't tempt the internet.
[390.54 --> 391.02]  They'll do it.
[391.54 --> 394.50]  And so thank you so much for coming to talk with us today, Rich.
[394.50 --> 399.56]  This is a really important topic because I think for me, there's just so much to unpack here.
[399.56 --> 411.68]  So the community essentially has had like kind of crazy uproar reactions to several large, well-known projects removing TypeScript support within the library.
[412.20 --> 418.32]  Some libraries have completely removed TypeScript without any other support for types.
[418.72 --> 420.32]  Turbo being an example of that.
[420.32 --> 435.46]  But Rich's project several months ago, so this isn't even like, I feel like this isn't new news for you all in Svelte land, but you removed TypeScript support and put JS docs type annotations in place of that.
[435.64 --> 439.90]  So folks have some backwards compatibility and which I thought was great.
[439.90 --> 444.60]  And you dealt with your own level of community uproar when you did that several months ago.
[445.02 --> 451.50]  And so could you kind of talk us through a little bit about what that process was like for you and kind of how you came to that decision, Rich?
[452.12 --> 457.32]  I can, but I should say that the uproar very largely wasn't from the Svelte community.
[457.32 --> 466.94]  It was from, I guess, the TypeScript community or like the wider web development community who heard that we were removing TypeScript from the repo and immediately took the wrong conclusion.
[467.50 --> 468.32]  And they were up in arms.
[468.32 --> 481.20]  They thought that we were just doing this completely mad retrograde thing and took a long time to yell at us on Hacker News and on Reddit and on Twitter and elsewhere without taking the time to understand the nuance of what we'd actually done.
[481.20 --> 486.48]  So a couple of years ago, we're working on SvelteKit, which is the application framework that goes with Svelte.
[486.80 --> 492.24]  And we had taken the step of writing that code base in vanilla JavaScript.
[492.24 --> 501.80]  So when you install SvelteKit and that gets downloaded into your node modules, the code that you're running when you run SvelteKit is the code that we wrote.
[501.84 --> 502.84]  It's the exact code that we wrote.
[502.90 --> 504.18]  It's not going through a build step.
[504.28 --> 508.58]  It's not going through Babel or TypeScript or it's not even being bundled with RollerPort or ESBuild or anything like that.
[508.64 --> 511.08]  It is just the source code that was originally authored.
[511.62 --> 513.50]  And that's great for a whole bunch of reasons.
[513.62 --> 516.04]  Like we don't have all of the complexities of a build step.
[516.04 --> 520.66]  We don't have anything in between you and the code that's running.
[520.92 --> 526.04]  There's no sort of changes of behavior that are being introduced by some kind of transpilation artifact or anything like that.
[526.28 --> 534.06]  But also, if you're inside a SvelteKit project and you want to understand what a particular piece of code that you've imported from the framework is doing,
[534.44 --> 538.52]  you can, you know, in VS Code, you have this command click functionality, which is called go to definition.
[538.72 --> 544.30]  And it will take you to the exact piece of like the exact line within the source code where that function was implemented.
[544.30 --> 547.96]  And you can like start adding debugger statements and console log statements and whatever.
[548.16 --> 550.92]  And it will just work, which is kind of a magical thing.
[551.52 --> 557.50]  Svelte, on the other hand, was for a very long time written in TypeScript with .ts files.
[558.52 --> 565.86]  And because we'd had such a great success with authoring SvelteKit in JavaScript, we thought, well, why don't we do the same thing?
[566.40 --> 569.78]  And Svelte is going to give us a whole raft of benefits.
[569.78 --> 574.92]  In addition to the things that I talked about, the go to definition, the fact that there's no complex build artifacts, any of that,
[575.20 --> 577.42]  it means that the package itself gets way smaller.
[577.46 --> 583.66]  Because typically what happens when you have a code base that is authored in TypeScript and you have to turn it into JavaScript,
[584.34 --> 591.28]  then in addition to the compiled output, you have these chunky source maps and all of these other things.
[591.42 --> 593.28]  And the package itself is way, way bigger.
[593.28 --> 596.88]  And so we've managed to shrink the package down by a huge amount.
[597.14 --> 599.10]  The complexity is way reduced.
[599.72 --> 602.60]  And everything is wonderful.
[603.00 --> 606.56]  But everyone wants to know what's going to happen when I use this library.
[606.78 --> 611.04]  Am I sacrificing type safety by using a library that is authored in JavaScript?
[611.04 --> 618.98]  And this is where what we did and what DHH did, which I'm sure we're about to talk about, is very different.
[619.48 --> 625.66]  Because what we did is we're authoring in JavaScript, but we're annotating all of that code with JS doc annotations,
[625.78 --> 631.78]  which give the system the same type information that we would have if we were authoring in .ts files.
[631.78 --> 640.26]  And so we're still authoring .dts files, which get shipped alongside the package, and it's still being generated from the source.
[640.66 --> 645.94]  We're just not doing it by using this non-standard TypeScript syntax.
[646.56 --> 651.16]  So we get all of the benefits of type safety, auto-completion, IntelliSense, all of that stuff.
[651.32 --> 658.02]  But none of the drawbacks of complex build steps and coding your node modules that you can't edit and all the rest of it.
[658.02 --> 662.54]  Oh, yeah. Yeah. And you're leveraging the JS doc TypeScript integration.
[662.88 --> 665.56]  Like there's a plugin for like doing that, right?
[665.70 --> 669.24]  Like that they, because I think JS, JS doc added support for that.
[669.36 --> 670.14]  Like that's not.
[670.28 --> 672.58]  It's not even a plugin. It's not something that JS doc did.
[672.66 --> 677.64]  It's just something that TypeScript just supports since like a long time ago.
[677.70 --> 681.94]  I introduced it in version 3.7 or something like many moons ago.
[681.94 --> 686.88]  They added the ability to do type checking with JavaScript that has JS doc annotations.
[686.88 --> 693.82]  And it's a subtly different version of JS doc than people were using 10 years ago before TypeScript.
[694.38 --> 695.46]  But it's basically the same.
[695.60 --> 704.76]  Like above a function or an object, you have this block comment, which begins slash star star and closes with a star slash.
[704.94 --> 710.06]  And inside there, you have basically the same stuff that you would have had in your type annotations in the first place.
[710.06 --> 719.32]  It's a little bit of a different way of using TypeScript, but it's something that like once you learn it is pretty familiar and you can learn it in the space of a couple of hours.
[719.66 --> 722.38]  Yeah. Yeah. No, JS docs was like the savior back in the day.
[722.48 --> 730.68]  That was like how a lot of library in node publish their API docs kind of automagically, you know, with every release.
[730.68 --> 736.74]  And yeah. And so just kind of getting back to your point about all the improvements that came with the removal of TypeScript.
[737.52 --> 740.66]  I'm kind of team idiomatic JavaScript any day, right?
[740.78 --> 745.00]  Like idiomatic JavaScript, meaning, you know, this is JavaScript that you wrote.
[745.22 --> 747.80]  It's not something that got spit out by a transpiler.
[747.80 --> 756.36]  And, you know, if you look at like so many common things that we use in JavaScript, like a recent example that was brought up on the podcast was optional chaining.
[756.68 --> 762.06]  You know, you look at what happens when you transpile something that was, you know, that uses optional chaining.
[762.36 --> 764.22]  It's a lot more bytes than what you wrote.
[764.64 --> 771.92]  So, yeah, of course, for a library like Svelte that really prides itself on like, hey, we are giving you code that you don't have to compile.
[771.92 --> 778.80]  It just works, you know, like this is like you're running our source code essentially without any intermediaries.
[779.22 --> 793.38]  Like I can see how, yeah, transpiling and doing a bunch of intermediary steps really pollutes the intention of, you know, the library, but also the readability and your ability to even control the size of your bundles, right?
[793.46 --> 794.30]  Or your output.
[794.94 --> 796.42]  Yeah. And that's actually an interesting case.
[796.42 --> 798.82]  The optional chaining thing, like, is it getting transpiled or not?
[798.88 --> 800.60]  Because you don't need to transpile that.
[800.60 --> 806.82]  If you have that optional chaining syntax inside your TypeScript, then you can just strip out the type annotations and run that as JavaScript.
[807.08 --> 809.82]  But it depends on what's in your TS config file.
[810.16 --> 819.60]  It's very easy to have the target setting such that that will get turned into the JavaScript that you would have had to write before optional chaining was in the language.
[819.70 --> 822.74]  And that's when you get that really bloated, transpiled output.
[823.14 --> 827.10]  And the reality is most people don't know what's in their TS config.
[827.10 --> 831.32]  A lot of people just, like, don't want to learn what all of those different settings mean.
[831.82 --> 841.14]  And so when you start adding these tools, like, you really take on a responsibility for being very careful about what they're doing to your code.
[841.20 --> 842.52]  And most people just don't.
[843.08 --> 852.98]  So, Rich, would you agree that what you guys did is effectively equivalent to changing your internal tooling without changing any of your external artifacts?
[852.98 --> 854.12]  Is that fair to say?
[854.48 --> 855.36]  That's exactly right.
[855.44 --> 856.14]  Well, actually, no.
[856.46 --> 857.60]  I'll caveat that.
[857.94 --> 862.38]  It's correct insofar as people who are using the library still get the type safety.
[862.70 --> 864.40]  And that's what people care about at the end of the day.
[864.52 --> 872.20]  They want to know that if they start typing the name of something that's in your framework, that they'll get the auto import.
[872.62 --> 875.00]  And if they hover over it, they'll get the inline documentation.
[875.34 --> 878.80]  And if they pass the wrong arguments to it, they'll get red squigglers and all of that stuff.
[878.88 --> 881.32]  Like, that's what people want when they're using a library.
[881.32 --> 889.04]  But that's not to say that there are no user observable changes as a result of changing from .ts to .js with .js doc.
[889.38 --> 895.52]  Because, you know, as I say, the package gets way smaller because we're not shipping all of these source maps and, like, all of these other things get much simpler.
[896.12 --> 900.54]  So improvements to Svelte, the compiled bundled version.
[901.30 --> 906.92]  But you changed, let me say it this way, you changed your team's tooling without affecting your user's tooling.
[906.92 --> 911.94]  Your users still have all the tools they had previously with autocomplete and whatnot, correct?
[912.42 --> 913.24]  Exactly, yeah.
[913.64 --> 919.20]  If anything, we've taken on a bit of a burden ourselves because TypeScript is, we think, nicer to author.
[919.94 --> 925.08]  But we're very careful about making sure that our users get the best possible experience.
[925.44 --> 925.60]  Yeah.
[925.82 --> 927.54]  Yeah, and that's a good pivot.
[927.54 --> 935.00]  Because, you know, one thing that, like, I wanted to discuss today is that, like, you know, what are those user observable differences, right?
[935.08 --> 936.54]  Like, end user observable differences.
[937.20 --> 941.38]  Especially, you're still supporting type annotations with .js doc.
[941.48 --> 946.16]  So builds aren't going to break the next day for people if they upgrade.
[946.64 --> 947.14]  What else?
[947.22 --> 948.54]  I mean, is there anything besides...
[949.54 --> 950.26]  I don't know.
[950.28 --> 955.12]  Is there anything at all besides, like, oh, there's, like, my node modules are slightly smaller.
[955.12 --> 957.48]  And is there anything else?
[957.76 --> 965.42]  I mean, I think that the go-to-definition stuff is huge and something that we don't spend nearly enough time talking about.
[965.60 --> 978.36]  I'm old enough to remember the days before NPM when if you wanted to use some code off the internet, like, you would literally go find it on some page somewhere and then you would copy and paste it into your project folder.
[978.56 --> 982.88]  And the expectation was that you would adapt it to your requirements.
[982.88 --> 988.92]  Like, it wasn't something that you would get from somewhere and then it was just a black box that you would never touch.
[989.36 --> 997.40]  But then NPM came along and people started installing stuff from a registry and then people stopped checking their node modules into Git.
[997.50 --> 999.36]  They were like, well, we can do that when we publish.
[999.46 --> 1001.44]  We don't need to do it in version control.
[1001.44 --> 1005.72]  And then all of a sudden, like, the culture changed.
[1006.50 --> 1011.02]  And nowadays, node modules is kind of treated as this black box.
[1011.18 --> 1013.52]  Like, you don't venture inside there unless you really need to.
[1014.08 --> 1019.78]  And especially once we started using transpilers, people don't ship their source code.
[1019.88 --> 1023.60]  They ship the output of Babel or ESBuild or TypeScript or whatever it is.
[1024.20 --> 1027.66]  Like, it really becomes this no-go area.
[1027.66 --> 1035.80]  Like, you can go in there, you can have a poke around, but, like, good luck finding the bit of code that you're trying to debug or understand or whatever.
[1036.20 --> 1037.90]  And I think that's a real shame.
[1038.40 --> 1047.50]  And I really believe that if you install a library, you should be able to poke around its internals and see what it's doing inside there.
[1048.16 --> 1052.82]  And the only way that you can do that is by shipping your source code, ultimately.
[1052.82 --> 1062.16]  Like, a lot of libraries, even if they do have go-to-definition working, which almost none of them do, like, you're probably going to be looking at some transpiled output.
[1062.26 --> 1068.72]  And if you start adding your console.logs or your debugger statements inside this function that you're trying to, like, understand, like, why isn't this function working?
[1068.72 --> 1075.38]  That's not going to do anything because you need to, like, rebuild from source.
[1076.18 --> 1085.96]  And that's just a headache that, like, means cloning the repo from GitHub, understanding the very, like, idiosyncratic build processes that they have, all of that stuff.
[1086.18 --> 1087.02]  It's just too much work.
[1087.08 --> 1087.88]  And so no one does it.
[1087.88 --> 1100.80]  And so we've become this slightly helpless consumer culture of libraries when, you know, back in the day, the gap between library author and library consumer was a little bit more fluid and porous.
[1101.30 --> 1103.52]  And I'm trying to do my bit to bring that back.
[1104.14 --> 1111.18]  So, Rich, if you go back and psychoanalyze to a certain extent the reaction to your change, which has been a while now in internet years,
[1111.66 --> 1116.02]  you said that a lot of it was because people didn't understand the nuance of what you all had done.
[1116.02 --> 1118.46]  I think that's fair to say that's part of it.
[1118.54 --> 1122.12]  Do you think another part of it is simpler than that?
[1122.34 --> 1126.68]  Like, Rich Harris, who I respect, doesn't like TypeScript, which I love.
[1126.86 --> 1128.28]  Therefore, I'm mad at Rich Harris.
[1128.44 --> 1129.60]  Do you think some of it's that simple?
[1129.84 --> 1133.42]  Or do you think a lot of it was just not understanding exactly what had gone on?
[1133.46 --> 1139.62]  Because it seems like on the current kerfuffle, it's more like that level of dialogue that's going on
[1139.62 --> 1148.36]  and not so much about the difference between libraries and applications and JS doc versus not and autocomplete versus losing that.
[1148.48 --> 1150.00]  It seems like it's more basic now.
[1150.18 --> 1151.00]  Was any of that there?
[1151.60 --> 1152.90]  No, I think you're right.
[1153.00 --> 1157.18]  I think that a lot of it is TypeScript good, JavaScript bad.
[1157.18 --> 1167.48]  And so if someone tries to bring any nuance into that conversation, then they're saying something less than TypeScript good.
[1167.94 --> 1170.94]  They're saying like, TypeScript's mostly good under certain circumstances.
[1171.24 --> 1173.18]  Sounds like American voters, you know?
[1174.28 --> 1176.64]  Yeah, you can't have that level of dialogue.
[1176.64 --> 1186.60]  Even that is essentially an attack if you are someone who doesn't have a very nuanced understanding of what these technologies bring to the table.
[1187.30 --> 1191.36]  And unfortunately, I think there are a lot of people to whom that description applies.
[1192.04 --> 1195.78]  I'd say like majority of the internet, just in general.
[1195.78 --> 1207.76]  It's like we've all been reduced to like headlines and, you know, like tweets and, you know, it's like, you know, anything over like 500 characters is like too much information, you know?
[1207.92 --> 1208.48]  Sum it down.
[1208.60 --> 1210.72]  How do we sum this down?
[1211.28 --> 1220.32]  Yeah, honestly, like for me, I think what's just so strange about this whole thing is not just like the lack of nuance and curiosity, you know?
[1220.32 --> 1229.32]  Like I think I would expect developers who, by the way, especially web developers, like I will argue this with anyone any day, hands down the smartest people on earth.
[1229.62 --> 1242.90]  Like most creative people, you know, I'd expect from a bunch of really smart people to be more curious, to be asking why and not just kind of this weird like pitchfork reaction that we're seeing.
[1243.06 --> 1248.90]  And I know when that happened with Svelte many months ago, was that around May, I think, or April?
[1248.90 --> 1249.74]  I don't even.
[1250.18 --> 1251.26]  That sounds about right.
[1251.38 --> 1252.18]  Yeah, something like that.
[1252.30 --> 1254.08]  Yeah, your mentions kind of went crazy, right?
[1254.18 --> 1258.78]  Like there was a lot of at Rich Harris or there was just a lot.
[1258.94 --> 1259.10]  Yeah.
[1259.80 --> 1265.60]  And to be fair, it all began with an interview on a website that I had given.
[1265.72 --> 1268.74]  I had talked about the fact that we were switching from TypeScript to JavaScript.
[1268.92 --> 1270.92]  And I'd explained that this was going to yield certain benefits.
[1271.04 --> 1274.96]  And the way that it was written up didn't really explain what we were doing.
[1274.96 --> 1280.10]  And so some people saw that interview and they were like, oh my God, Svelte is moving from TypeScript to JavaScript.
[1280.46 --> 1283.64]  Surely that's just a typo or a mistake on the part of the reporter.
[1283.92 --> 1287.04]  And I did an even worse job of clarifying it at that point.
[1287.10 --> 1288.50]  I said, no, no, no, the article is correct.
[1288.62 --> 1289.82]  It's moving from TypeScript to JavaScript.
[1290.06 --> 1295.92]  And that's the point at which everyone was just said, well, you must clearly be a gibbering idiot because no one would do that.
[1295.92 --> 1302.78]  So what's kind of funny is that Nick Neesey, who couldn't be here today, of course, all of our listeners are like, where is Nick?
[1302.84 --> 1306.46]  Because he's our resident TypeScript evangelist.
[1306.72 --> 1312.38]  And I'm sorry, listener, news of this kerfuffle caused Nick to literally become ill.
[1312.92 --> 1314.18]  So he can't be here today.
[1314.18 --> 1316.10]  He's literally ill because of this.
[1316.20 --> 1317.16]  No, not because of this.
[1317.30 --> 1322.14]  Because of an unfortunate run-in with airborne viruses.
[1322.14 --> 1330.20]  But during this time, of course, you may not know this, Rich, but I've taken an anti-TypeScript stance on this podcast merely for the lulls.
[1330.30 --> 1334.06]  Like, I'm just in it to be Nick's dramatic foil because he's too positive.
[1334.20 --> 1335.22]  So I just go against it.
[1336.06 --> 1340.72]  And so when you did that, I explained it to him like, hey, dude, Rich Harris doesn't like TypeScript.
[1340.88 --> 1343.40]  So you, so TypeScript bad, right?
[1343.98 --> 1344.92]  And I was just joking.
[1345.26 --> 1347.58]  And through the course of this, this was on a show we did.
[1347.58 --> 1353.56]  Through the course of the conversation, we ironed out exactly what happened with Svelte and with the JS.comments and everything.
[1354.10 --> 1355.80]  And at the end of it, he was like, oh, that's not so bad.
[1355.96 --> 1356.74]  I'm fine with that.
[1357.04 --> 1361.58]  And I was like, it's just interesting how when you actually address the nuance and have the conversation,
[1362.08 --> 1367.02]  what was an immediate gut reaction of, oh, uh-oh, TypeScript's going down because Svelte's not using it,
[1367.36 --> 1370.36]  becomes like, oh, that's logical and reasonable.
[1370.36 --> 1371.86]  And I'm totally fine with it.
[1372.28 --> 1374.42]  And so we found common ground in the details.
[1374.60 --> 1378.84]  Yeah, I mean, look, let me just, just stay on the record once and for all.
[1378.98 --> 1380.12]  I f***ing love TypeScript.
[1380.32 --> 1382.06]  I think TypeScript is fantastic.
[1382.50 --> 1386.48]  He'll be happy to hear you preferred it to author it than you do JS.comments.
[1386.48 --> 1388.86]  Because he thought that was crazy that you guys would want to do,
[1389.80 --> 1392.06]  who wants to comment in their code is what he said at the time.
[1392.94 --> 1393.54]  Oh, really?
[1393.74 --> 1396.06]  No, it's, it's, it's all, it's all situational.
[1396.26 --> 1399.22]  If I'm, if I'm writing an application, then I will 100% use TypeScript.
[1399.22 --> 1405.06]  But if I'm writing a library that needs to be consumed by myself in another project or by someone else,
[1405.48 --> 1411.48]  then having the raw source code in your node modules just has so many benefits.
[1411.92 --> 1417.98]  And I think people are somewhat in denial about the costs that tool chains impose on them.
[1418.16 --> 1418.76]  Yeah.
[1418.98 --> 1424.10]  And so are you, are you all shipping ES5, ES7, ES6?
[1424.18 --> 1425.96]  Like, what are you all, you know,
[1425.96 --> 1429.36]  I'm curious since, since you are shipping just like vanilla JS.
[1430.00 --> 1434.16]  Are there any, any features that we're preventing ourselves from using?
[1434.60 --> 1441.90]  I think by and large browsers and server-side JavaScript runtimes are pretty current with syntax.
[1442.22 --> 1446.60]  Like I think like optional chaining is, that we mentioned is one of the newest syntactical features
[1446.60 --> 1448.82]  and that's supported everywhere that we care about.
[1449.42 --> 1452.96]  So I don't think that's something that we generally think about.
[1453.02 --> 1456.40]  Like we just author modern JavaScript and just assume that it's going to run.
[1456.58 --> 1458.54]  And if there's something that doesn't, then we'll remove it.
[1458.82 --> 1459.22]  Okay.
[1459.40 --> 1462.70]  So as long as it's basically gone through the full standards process
[1462.70 --> 1467.86]  and is like actual JavaScript, not just like in a proposed stage, then you'll write it.
[1467.94 --> 1468.06]  Right.
[1468.10 --> 1468.44]  Exactly.
[1468.44 --> 1468.84]  Yeah.
[1468.92 --> 1471.96]  Like we're not, we're not using records and tuples or anything like that.
[1472.08 --> 1476.54]  We're, but we're using, using everything that's available in evergreen browsers, essentially.
[1476.72 --> 1477.00]  Got it.
[1477.04 --> 1477.32]  Got it.
[1477.34 --> 1477.96]  That makes sense.
[1478.24 --> 1481.00]  And so, I mean, so I guess for me, like what's shocking is like,
[1481.30 --> 1486.52]  did people forget that before 2012, we were writing, you know, there was no TypeScript
[1486.52 --> 1490.76]  and there was, you know, large scale websites with like millions of lines of JavaScript
[1490.76 --> 1491.80]  and all of that jazz.
[1491.88 --> 1495.86]  Like, I'm just trying to understand, like, I know people love TypeScript,
[1495.86 --> 1498.28]  but, you know, why behave on JavaScript?
[1498.66 --> 1503.98]  Like as somebody who personally falls into the like pragmatic TypeScript camp, right?
[1504.08 --> 1508.42]  Like I definitely see the benefit of TypeScript, I think, especially for a large code basis
[1508.42 --> 1511.42]  with multiple people contributing, it makes sense.
[1511.66 --> 1513.60]  But it's still a superset of JavaScript.
[1513.76 --> 1519.04]  Like why, you know, why is, you know, vanilla JavaScript just so bad, so scary is even with
[1519.04 --> 1522.98]  types, like, you know, even with type annotations, apparently it's not good enough.
[1522.98 --> 1529.28]  So I just, I worry that we've gotten to, you know, just this weird place in the community
[1529.28 --> 1532.96]  where people don't really know why they have the opinions that they have.
[1533.04 --> 1538.36]  They just have them, like, because someone else, like, said it was cool or someone else
[1538.36 --> 1539.66]  that they respect also has that.
[1539.74 --> 1544.80]  Or, you know, it's just, it's just disappointing because I know how smart engineers are.
[1545.14 --> 1545.86]  So it's like.
[1546.40 --> 1547.60]  So I have a theory about this.
[1547.60 --> 1553.42]  Everyone who uses TypeScript was, or almost everyone, I mean, some people come into the
[1553.42 --> 1556.34]  industry and they, TypeScript is the first thing they learned, but almost everyone who
[1556.34 --> 1559.30]  uses TypeScript was at one point a JavaScript developer.
[1560.44 --> 1566.60]  And when you've experienced JavaScript without types, and then you've experienced development
[1566.60 --> 1569.58]  with types, like the difference is so stark.
[1569.66 --> 1573.04]  Like once it clicks, and it does take a while to click for a lot of people, myself included,
[1573.22 --> 1575.66]  took me a long time to get on board the TypeScript train.
[1575.66 --> 1579.16]  Once you get there, the idea of going back is just so painful.
[1579.36 --> 1585.02]  So everyone defends TypeScript with the zeal of the convert because everyone is a convert.
[1586.04 --> 1591.16]  And people who have not yet made that journey themselves, like it's so hard to explain to
[1591.16 --> 1598.00]  someone just how beneficial types are in a code base if they either haven't yet had that
[1598.00 --> 1603.60]  epiphany or they're actively resisting having the epiphany for ideological reasons or whatever
[1603.60 --> 1603.96]  it is.
[1603.96 --> 1604.94]  Yeah, I get that.
[1605.08 --> 1606.64]  But TypeScript isn't perfect, right?
[1606.74 --> 1608.86]  Like just to play kind of devil's advocate here.
[1608.94 --> 1614.42]  So I agree with everything you said, but types that, a lot of time, I mean, I wish actually
[1614.42 --> 1618.30]  as an experiment, maybe we could do this with our listeners or something.
[1618.38 --> 1623.62]  For the month of November, let's just start a tally for how many minutes and hours that
[1623.62 --> 1627.30]  you spend in that month fussing with the TypeScript compiler.
[1627.54 --> 1630.48]  But you can't measure the amount of time that it's saving you.
[1630.78 --> 1631.20]  Interesting.
[1631.20 --> 1632.56]  Yeah, that's a fair point.
[1632.90 --> 1639.32]  I know just from like observing myself that TypeScript saves me like literally hours a
[1639.32 --> 1640.28]  week, I would say.
[1640.42 --> 1643.00]  It costs me minutes a week, certainly.
[1643.26 --> 1648.06]  And those minutes are some of the most frustrating minutes that I spend programming.
[1648.46 --> 1653.36]  Like let's say that I spend an hour a week fighting TypeScript, which is, it's less than
[1653.36 --> 1653.54]  that.
[1653.60 --> 1655.86]  But like, let's say for the sake of argument that that's what it is.
[1655.86 --> 1661.66]  Like I'm going to be super conscious of that hour because at the time I'm like, oh, I don't
[1661.66 --> 1663.04]  understand what is going on here.
[1663.36 --> 1665.66]  And usually at the end of it, you're like, oh, right.
[1665.72 --> 1665.88]  Yeah.
[1665.94 --> 1666.22]  Okay.
[1666.58 --> 1667.68]  I understand now.
[1667.90 --> 1669.86]  TypeScript tricked me into writing better code.
[1670.02 --> 1672.92]  Turns out I'm not smarter than Anders Halberg.
[1673.08 --> 1673.86]  I don't know how you say his name.
[1674.20 --> 1674.70]  After all.
[1675.34 --> 1680.64]  But the time that TypeScript saved you over the same time period, which just like observation
[1680.64 --> 1683.40]  for myself is way, way, way more time.
[1683.70 --> 1684.48]  You're not aware of it.
[1684.56 --> 1685.76]  You're just like happily coding.
[1686.54 --> 1689.20]  But there are times that you do become aware of it.
[1689.76 --> 1693.72]  Recently, I did a fairly major refactor on a sizable code base.
[1694.22 --> 1699.92]  And if I hadn't had TypeScript to do that, where, you know, you just change some property
[1699.92 --> 1701.52]  of an interface somewhere.
[1701.68 --> 1705.84]  And then the type checker just tells you all of the places in your code base where the signature
[1705.84 --> 1706.40]  has changed.
[1706.50 --> 1710.12]  Or like you can even do, you know, rename or references and it'll just go through the entire
[1710.12 --> 1711.52]  code base and it'll just do it for you.
[1711.70 --> 1716.52]  The idea of doing that refactor without the benefit of TypeScript brings me out on a cold
[1716.52 --> 1716.80]  sweat.
[1717.32 --> 1722.06]  But, you know, you're so much more viscerally aware of the time that you spend fighting
[1722.06 --> 1723.36]  with TypeScript than the reverse.
[1723.60 --> 1724.48]  Yeah, no, that's fair.
[1724.68 --> 1730.76]  And that's a good reminder because, you know, I do like to be angry about how much time we
[1730.76 --> 1735.88]  spent on TypeScript, like specifically fighting with a compiler.
[1735.88 --> 1741.58]  And, you know, for me, I'm like, oh man, that's like time we are not spending like writing
[1741.58 --> 1746.06]  unit tests or doing other important things that are going to shore up the quality of this
[1746.06 --> 1750.94]  code or writing, you know, feature code, for example, even.
[1751.08 --> 1751.20]  Right.
[1751.28 --> 1755.38]  Like, so I think for me, that's just, that's my own personal bias.
[1755.78 --> 1757.26]  But you're right.
[1757.40 --> 1757.58]  Yeah.
[1757.68 --> 1760.44]  I mean, there's two places where I really agree with you.
[1760.50 --> 1761.54]  Doesn't ship in production.
[1761.54 --> 1764.02]  And that's what gets me angry.
[1764.12 --> 1766.84]  I'm like, our customers are never going to run this code, you know?
[1767.08 --> 1767.60]  Right, right.
[1768.02 --> 1771.62]  But if you're doing something very exploratory and you don't yet know what the shape of the
[1771.62 --> 1775.78]  system that you're building is, like you're kind of like uncovering the design as you
[1775.78 --> 1779.60]  write it, that's a really bad time to be thinking about type safety.
[1780.02 --> 1784.14]  And I've always resisted adding types at that very, very early stage of a project that I
[1784.14 --> 1785.66]  don't yet understand the shape of.
[1786.08 --> 1790.22]  But the other one is the build tooling complexity that I referred to earlier.
[1790.22 --> 1792.20]  I've got a great example just from a few days ago.
[1792.68 --> 1797.28]  Have this, have this code base that is written in TypeScript and the tests all passed.
[1797.44 --> 1797.74]  Fine.
[1797.86 --> 1798.24]  Locally.
[1798.42 --> 1798.86]  Type checking.
[1799.06 --> 1799.28]  Fine.
[1799.40 --> 1799.68]  Locally.
[1799.76 --> 1800.04]  Linting.
[1800.16 --> 1800.30]  Fine.
[1800.36 --> 1800.58]  Locally.
[1801.28 --> 1806.88]  Send it to GitHub and the CI is failing and it's failing with the most inscrutable error
[1806.88 --> 1807.70]  imaginable.
[1807.70 --> 1813.10]  And it turned out from like a very long time spent like digging through stack traces and
[1813.10 --> 1820.50]  something that somehow a module deep inside Babel was getting executed twice and it was
[1820.50 --> 1825.90]  trying to update something on the exports object that had already been updated and it was saying,
[1826.00 --> 1826.94]  well, this is, this is read only.
[1827.02 --> 1827.60]  You can't do this.
[1827.86 --> 1829.04]  And I couldn't reproduce it locally.
[1829.04 --> 1830.48]  There was nothing I could do.
[1830.48 --> 1835.42]  Like I made sure all of my versions of everything were perfectly in sync and I just couldn't
[1835.42 --> 1836.00]  figure it out.
[1836.04 --> 1841.08]  And I spent so long trying to sort this out and I never would have had to if we just hadn't
[1841.08 --> 1843.06]  been using .ts files in the first place.
[1843.06 --> 1847.62]  Because the only reason that it happened is because our rollup configuration mentioned
[1847.62 --> 1848.60]  Babel somewhere.
[1849.38 --> 1854.54]  And so in, without being able to actually solve the problem, the way that I worked around it
[1854.54 --> 1857.58]  in the end was just by not using rollup and using esbuild instead.
[1857.58 --> 1863.20]  And so now the build artifact is 10% larger because rollup is like generates more efficient
[1863.20 --> 1863.54]  output.
[1863.84 --> 1866.48]  Like that is the cost of having to deal with this bull.
[1867.06 --> 1871.10]  And the real solution is to just not be writing .ts files there in the first place, because
[1871.10 --> 1872.52]  then these things don't even arise.
[1872.66 --> 1877.70]  It's not the fault of TypeScript, but it is the fault of the enormous complex dependency
[1877.70 --> 1882.72]  chains that we've had to use in order to deal with all of this complexity.
[1883.30 --> 1883.38]  Yeah.
[1883.38 --> 1889.42]  And don't forget the beauty of being able to also just copy your code into a node context
[1889.42 --> 1893.64]  or just in a browser console and just being able to copy paste your module and just have
[1893.64 --> 1894.22]  it run.
[1894.46 --> 1896.58]  You know, like that's another thing, you know?
[1896.76 --> 1901.68]  Like you can't, for debugging purposes specifically, you know, and not have to worry about like,
[1901.76 --> 1906.30]  oh, is this like, oh, this is TypeScript and I need to like do a few things before I
[1906.30 --> 1906.84]  can do that.
[1906.90 --> 1909.98]  And it's, you know, it's just, it's quite, you know, quite nice in that sense.
[1909.98 --> 1914.68]  And so for me, that's why I'm tremendously excited about the solution of kind of adding
[1914.68 --> 1921.06]  type annotation to JavaScript and having that be in the standards, like as part of the language,
[1921.18 --> 1922.12]  you know, that's huge.
[1922.12 --> 1925.76]  And like so many wins can come from that, right?
[1925.86 --> 1930.66]  And part of it, I think, is also just reducing this tooling hell, like nightmare that we're
[1930.66 --> 1931.30]  in right now.
[1931.30 --> 1936.08]  We had Mark Erickson on the show a couple of weeks ago talking about, I'm sure you saw
[1936.08 --> 1941.56]  the blog post, you know, his whole like trying to modernize ESM, you know, and yeah, we're
[1941.56 --> 1945.40]  slightly different topic than the one we're talking about here, but similar pain points,
[1945.62 --> 1950.78]  you know, just around kind of tooling, tooling hell and interoperability and all that jazz.
[1950.78 --> 1953.00]  So future can't come soon enough.
[1961.30 --> 1980.82]  Okay, I'm here with Morris Gruber, CTO of KC.
[1980.94 --> 1986.40]  Morris, tell me about how KC gives developers a headless CMS that lets them build with endless
[1986.40 --> 1987.20]  possibilities.
[1987.30 --> 1988.06]  What do you mean by that?
[1988.06 --> 1993.54]  So usually when you start a new project, you pick the technology and then you're limited
[1993.54 --> 1996.26]  to whatever you choose in the first place.
[1996.44 --> 2002.62]  So if in the first place you go on WordPress or Redflow, you're like stuck to what they offer
[2002.62 --> 2003.10]  to you.
[2003.62 --> 2006.38]  With KC, you're building your own front end.
[2006.48 --> 2011.94]  You can choose whatever technology you like and you're not learning our system.
[2012.08 --> 2017.98]  You just have to use GraphQL and that knowledge is like very powerful because you can
[2017.98 --> 2023.46]  transfer it to every other tool and you have the flexibility to connect it to an app, to
[2023.46 --> 2025.48]  a website, an e-commerce store.
[2025.58 --> 2028.30]  You're not limited to whatever plugin is supported.
[2028.58 --> 2032.98]  You can use any e-commerce system and just connect it in your front end together.
[2033.20 --> 2035.42]  That's the power of using a headless CMS.
[2035.46 --> 2035.94]  Okay.
[2036.32 --> 2037.42]  Take me one layer deeper then.
[2037.58 --> 2040.90]  So you have framework compatible starter templates.
[2040.90 --> 2045.30]  You have an API that allows you to import and export data.
[2045.54 --> 2047.02]  You've got UI extensions.
[2047.58 --> 2049.10]  What tooling do you all have for developers?
[2049.82 --> 2050.26]  Yeah, of course.
[2050.36 --> 2055.04]  So the first thing probably when you start a project is you want to import what you already
[2055.04 --> 2055.36]  have.
[2055.44 --> 2060.66]  So we got you covered importing and exporting data and you can access all of that with the
[2060.66 --> 2062.30]  easy to use GraphQL API.
[2062.64 --> 2063.82]  We build an SDK on top.
[2063.92 --> 2066.40]  You can use in TypeScript that gets you started.
[2066.40 --> 2072.90]  And then we also got you covered if the project grows, like you have multiple layers deep of
[2072.90 --> 2073.32]  nesting.
[2073.72 --> 2078.74]  You have the really big GraphQL queries and we still run them really fast for you.
[2078.82 --> 2079.64]  That's our guarantee.
[2080.16 --> 2083.84]  And also we got you covered for every new technology that is coming up.
[2083.96 --> 2089.68]  There is like a ton of new frameworks like quick and fresh of Dino coming everything every
[2089.68 --> 2090.84]  couple of months.
[2090.84 --> 2097.64]  But we are there to help you choose whatever is the best solution for you.
[2097.80 --> 2101.04]  And you don't have to make compromises on the CMS.
[2101.50 --> 2101.96]  Very cool.
[2102.06 --> 2105.32]  OK, the next step is to go to Casey.io.
[2105.52 --> 2108.88]  That's C-A-I-S-Y.io.
[2109.46 --> 2112.24]  And one thing you could try is try it free.
[2112.40 --> 2120.02]  Up to three users, two locales, 50,000 entries, 100 gigs of traffic, tons of free forever in
[2120.02 --> 2121.28]  their free forever tier.
[2121.62 --> 2122.34]  Hell is fun.
[2122.50 --> 2123.38]  Zero cost.
[2123.76 --> 2124.38]  Check it out.
[2124.64 --> 2130.44]  And for those who want a lifetime 50% off discount code, you can use JS Party to get that.
[2130.66 --> 2132.66]  Redeem now, but the discount lasts forever.
[2133.14 --> 2134.50]  Casey.io.
[2134.60 --> 2138.54]  Again, C-A-I-S-Y.io.
[2138.92 --> 2140.76]  And make sure you tell them the changelog sent you.
[2140.76 --> 2162.36]  Can we get anthropological again?
[2162.36 --> 2169.94]  Because I liked Rich's theory about, let's just call it the level of discourse that we
[2169.94 --> 2171.68]  tend to have around these things.
[2171.86 --> 2174.30]  The, would you call it the conviction of the convert?
[2174.76 --> 2175.76]  The zeal of the convert.
[2176.02 --> 2176.32]  Yeah.
[2176.76 --> 2178.08]  And that's really interesting to me.
[2178.14 --> 2179.82]  I have another, I have a theory of my own.
[2179.96 --> 2186.24]  And I think it's actually dealing with the other subset of users, the non-converts.
[2186.24 --> 2186.88]  Okay.
[2187.02 --> 2189.90]  Because TypeScript's been around since 2012.
[2190.38 --> 2192.60]  You know, it's been popular since maybe 2015.
[2193.30 --> 2195.90]  It's been dominant in the last five years.
[2196.32 --> 2202.90]  The size of the programming community roughly doubles every five-ish years.
[2203.56 --> 2205.92]  That's a lot of people coming into the industry.
[2206.64 --> 2212.26]  And so we are, as Bob Martin explained it to us on the changelog, he said, this industry
[2212.26 --> 2216.68]  is perpetually in a state of infancy because we always have new people coming in just by
[2216.68 --> 2220.48]  the fact of every five years, twice as many people are here.
[2220.58 --> 2222.92]  That means almost everybody is getting started.
[2223.34 --> 2226.50]  And a lot of those people get started in TypeScript today.
[2226.66 --> 2228.84]  And I think that's all well and good.
[2229.16 --> 2231.54]  But I think they don't have the conviction of the convert.
[2231.66 --> 2234.96]  I think what they end up having then is an identity problem.
[2234.96 --> 2241.16]  I think we have an identity problem inside of programming, which I think is probably
[2241.16 --> 2247.70]  stronger in people who are new to programming because they have less experience with different
[2247.70 --> 2250.36]  things and a lot of experience with one thing.
[2250.56 --> 2253.44]  And they begin to identify with that one thing.
[2253.96 --> 2260.42]  And I think we have a lot of people who identify as TypeScript developers, just like people used
[2260.42 --> 2262.12]  to think of themselves as JavaScript developers.
[2262.12 --> 2266.22]  Hey, even JavaScript devs think of themselves as TypeScript devs and vice versa.
[2266.42 --> 2268.98]  It's like this superset kind of a thing.
[2268.98 --> 2277.32]  And that's problematic because if somebody then speaks against the thing you identify
[2277.32 --> 2278.78]  with, they're speaking against you.
[2279.72 --> 2285.36]  And so like you said earlier, Rich, JavaScript good, TypeScript bad, like that level of argumentation
[2285.36 --> 2289.36]  is usually because if you think TypeScript bad, I TypeScript, I bad.
[2289.60 --> 2290.24]  Like that's okay.
[2290.28 --> 2294.36]  I'm speaking like a caveman somewhat on purpose because it is kind of a basic reaction that's
[2294.36 --> 2296.18]  playing out is cave person, right?
[2296.18 --> 2297.72]  It is kind of at that level.
[2297.86 --> 2300.34]  It's like kind of the worst of who we are.
[2300.58 --> 2301.84]  And I think we can be better.
[2302.54 --> 2304.82]  And so I think that's a solvable problem.
[2304.90 --> 2308.56]  It's difficult because we have so many new people coming into the industry and you're
[2308.56 --> 2310.06]  always going to have people just getting started.
[2310.52 --> 2316.82]  But I think individually we can combat that by generalizing and not identifying with our
[2316.82 --> 2318.46]  tools so tightly.
[2318.46 --> 2322.36]  I know it's tough because when you're trying to get a job, they want to react dev.
[2322.46 --> 2323.86]  They want a svelte person.
[2323.96 --> 2325.26]  They want a TypeScript person.
[2325.42 --> 2329.74]  And so you have to say, I'm a TypeScript person because I want this job for a TypeScript
[2329.74 --> 2330.14]  person.
[2330.38 --> 2335.08]  But that's one little context in which you have to define yourself as a certain type of
[2335.08 --> 2335.38]  person.
[2335.38 --> 2339.66]  But in your life, in your work, don't be a svelte dev.
[2340.08 --> 2341.04]  No offense, Rich.
[2341.14 --> 2343.44]  Don't be, unless you're actually working on it.
[2343.44 --> 2345.00]  Unless you're Rich Harris, he can be a svelte dev.
[2345.00 --> 2346.92]  Don't be a React dev.
[2347.00 --> 2349.12]  Don't be a TypeScript person, a JavaScript person.
[2349.32 --> 2352.76]  Like be a software developer or an engineer, whatever you want to be called.
[2353.34 --> 2355.72]  And generalize as much as you can.
[2355.80 --> 2361.70]  And don't identify so closely with your tools because tools have trade-offs.
[2362.32 --> 2363.64]  Some are good, some are bad.
[2363.66 --> 2366.54]  And we should be able to discuss those trade-offs without attacking each other.
[2366.80 --> 2367.62]  And shelf life.
[2367.80 --> 2369.16]  They have shelf life too.
[2369.62 --> 2372.38]  I mean, like for real, you know?
[2372.54 --> 2373.44]  It's super hard though.
[2373.44 --> 2379.56]  Like if you're new to any domain, not just programming, you want to build up some credibility.
[2379.98 --> 2381.16]  You want to run with the big dogs.
[2381.30 --> 2384.26]  And like a very quick way to do that is to align yourself with a tribe.
[2384.88 --> 2391.22]  And like if you can identify the dominant tribe and that clearly is TypeScript nowadays, like
[2391.22 --> 2395.34]  TypeScript is in the ascendant and JavaScript without types is not.
[2395.34 --> 2398.68]  Then like it kind of makes sense to do so.
[2398.68 --> 2406.14]  Like people will project wisdom onto you by virtue of the fact that you have made the right choice of tribal affiliation.
[2406.14 --> 2412.74]  And so I don't know that it's as easy a problem to solve as just saying to people, be a software developer.
[2413.12 --> 2416.84]  Like people have been saying that for a long time and it doesn't seem to have stuck.
[2416.96 --> 2424.60]  So I don't know if there's like some way that we can, I don't know, maybe it takes the people who build the tools to say it themselves.
[2424.60 --> 2427.64]  Like maybe I should say, don't call yourself a Svelte developer.
[2427.86 --> 2428.50]  Yeah, yeah.
[2428.68 --> 2430.12]  You should do it in that voice.
[2430.40 --> 2431.28]  Rich Harris says so.
[2431.48 --> 2431.94]  Yeah, you should.
[2432.00 --> 2433.02]  That's a very convincing voice.
[2433.16 --> 2433.60]  I like that.
[2433.62 --> 2434.30]  Very convincing voice.
[2434.46 --> 2438.30]  It's like Barry White meets Jay-Z's tech nerd.
[2439.32 --> 2440.32]  Jay-Z, I'm true.
[2440.56 --> 2440.82]  Rich Harris.
[2441.34 --> 2442.24]  Yeah, that was good.
[2442.26 --> 2444.56]  If we could put that to a baseline, you know.
[2444.58 --> 2445.50]  Yeah, yeah, exactly.
[2445.70 --> 2447.96]  It's like, hey, y'all, you know.
[2448.00 --> 2449.26]  So he needs advertisements, you know.
[2449.30 --> 2451.10]  We need a public service announcement, you know.
[2451.60 --> 2453.60]  Rich Harris says, don't be a Svelte developer.
[2453.60 --> 2454.24]  Right, right.
[2454.32 --> 2458.10]  Yeah, I do agree that there are incentives in order to do what you're saying.
[2458.22 --> 2460.06]  And you have to start somewhere, right?
[2460.18 --> 2461.74]  You can't start on everything.
[2462.36 --> 2466.26]  It does make sense when you're getting started to pick a technology and dive deep into it.
[2466.60 --> 2473.06]  I hope as we advance in our careers and we start to see, like Amel said, that things have shelf lives.
[2473.72 --> 2477.84]  And Svelte won't be the best project forever.
[2478.42 --> 2480.86]  And TypeScript won't be the bees and bees forever.
[2480.86 --> 2482.50]  I mean, look, here comes Bun.
[2482.76 --> 2485.44]  Maybe Node is on its way out all of a sudden.
[2485.58 --> 2486.78]  Who knows what's going to happen?
[2487.10 --> 2488.12]  Maybe Dino is going to take.
[2488.48 --> 2490.60]  So, like, it's interesting.
[2490.88 --> 2491.92]  Technology is advanced.
[2492.30 --> 2496.42]  And we need to be able to hop, skip, and jump along the path in order to stay relevant.
[2496.80 --> 2498.10]  So I agree.
[2498.18 --> 2505.90]  It's tough because you want to start somewhere and you can have a shortcut to competency, perhaps, or at least perceived competency by picking the right popular thing.
[2505.90 --> 2509.62]  But in the long game, it doesn't pay off to stay there.
[2509.72 --> 2515.08]  And I feel like too much of us are just staying in one place and throwing Molotov cocktails everywhere else.
[2515.32 --> 2517.40]  Can I put my tinfoil hat on?
[2517.42 --> 2517.66]  Sure.
[2517.82 --> 2518.84]  Actually, it's not going to be a tinfoil.
[2519.10 --> 2523.22]  It's going to be my, like, $2 I'm going to pretend to be a psychologist hat on.
[2523.36 --> 2524.72]  Like, just bear with me for a second.
[2524.72 --> 2534.96]  So, you know, listening to you talk about this, Jared and Rich, like, it's very clear to me that there's some very kind of, like, deep primal things going on here.
[2535.18 --> 2539.66]  I do think community is very important, you know, in our industry, obviously.
[2540.18 --> 2546.54]  People identifying as a community means that they have a shared set of interests, tools, values, whatever, right?
[2546.78 --> 2550.24]  But people find comfort in those boundaries, right?
[2550.30 --> 2552.84]  Like, you got to know who's in your tribe.
[2552.84 --> 2566.98]  And so I feel like there's maybe an opportunity for the leaders of said tribes, you know, to kind of come together, like a little state of the union, you know, and do things maybe more often and put out, like, joint statements or whatever it is.
[2567.02 --> 2568.20]  I know that sounds kind of ridiculous.
[2568.20 --> 2573.94]  But really, like, I do think there's a need for more intermingling of thoughts and ideas.
[2573.94 --> 2583.94]  And people need to understand that, like, you might think that, like, oh, a React dev immediately is, like, hates every other type of developer or whatever, or, like, oh, this library is better than that library.
[2584.02 --> 2589.08]  But, like, really, like, if you know the maintainers of all these projects, they're talking to each other behind the scenes all the time.
[2589.32 --> 2591.04]  They're collaborating with each other all the time.
[2591.38 --> 2593.62]  They're using pieces of code from each other all the time.
[2593.76 --> 2597.38]  They're inspiring, you know, things in each other's libraries.
[2597.38 --> 2606.14]  I mean, you know, there's a lot of collaboration that I don't think gets surfaced in very binary environments like Twitter or X, I guess now.
[2606.56 --> 2607.82]  You know, it just sucks, right?
[2607.90 --> 2610.52]  Like, and I don't know how we can fix this problem.
[2610.76 --> 2617.72]  Like, people need to stop being so, like, unnecessarily, like, hostile, I think, when they meet people from other tribes.
[2617.90 --> 2619.34]  And it's okay to have different opinions.
[2619.34 --> 2623.02]  Like, it's okay to meet someone who hates TypeScript and you shouldn't have to poo-poo on them either.
[2623.34 --> 2624.62]  You know, like, it's fine.
[2624.62 --> 2629.28]  Like, you know, you might not agree, but we should agree to disagree.
[2629.50 --> 2634.56]  Like, that's just, like, sign of a civilized society, right, being able to agreeably disagree.
[2635.00 --> 2640.30]  The thing about Twitter, though, is a lot of people, like, switch over to that to escape their current work that they're doing.
[2640.44 --> 2647.28]  And so some people just like to troll and make stupid jokes and throw them all in tough cocktails and see where they land.
[2647.50 --> 2648.94]  And it's not really them.
[2649.00 --> 2650.60]  It's, like, the worst part of them.
[2650.60 --> 2658.98]  And I do agree that maybe leadership could help, but, I mean, at this point we have, you know, some leadership of certain projects actively throwing the cocktails into the mix.
[2659.10 --> 2664.44]  You know, like, there's incentive on the internet to draw attention to yourself.
[2664.44 --> 2668.80]  And we have well-known contrarians who are very good at drawing attention to themselves.
[2669.34 --> 2674.14]  And they're well-spoken and they write very well and they're very convincing.
[2674.14 --> 2680.68]  And they could be using that to bring people together and not to cause this basic level of discourse.
[2680.68 --> 2689.42]  But it's more beneficial to just draw the attention, get all the clicks, all the responses, and then write a follow-up post that does even more.
[2689.56 --> 2692.40]  Like, that's more at a very individualistic level.
[2692.52 --> 2694.14]  It's, like, better for them individually.
[2694.34 --> 2697.14]  So it's a really, maybe it's an untenable situation.
[2697.28 --> 2697.76]  I don't know, Rich.
[2697.76 --> 2698.92]  You have large audience.
[2699.06 --> 2702.76]  Do you feel pressure to lead in a positive manner?
[2702.76 --> 2704.64]  I know you're very funny on the internet.
[2704.76 --> 2709.42]  I know you also aren't immune to throwing in a Molotov cocktail every once in a while.
[2709.46 --> 2710.32]  What are your thoughts on the matter?
[2710.32 --> 2713.98]  I mean, Twitter is the Molotov cocktail throwing app, right?
[2714.08 --> 2714.54]  It is.
[2714.54 --> 2715.94]  That's why we go there.
[2717.06 --> 2722.54]  And if anything, like, because its current owner has made such a complete whore looks at everything over the last few months,
[2722.76 --> 2726.44]  I feel like all of the moderate, reasonable voices have left.
[2727.00 --> 2730.24]  And all the people who have left are, like, the addicts and the people who just, like,
[2730.24 --> 2730.44]  it's...
[2730.44 --> 2732.78]  God, can't help but stir up something.
[2732.78 --> 2732.98]  Yeah.
[2733.12 --> 2734.92]  Like, the expert trolls are still there.
[2734.92 --> 2737.38]  Thanks for explaining my reality, by the way, Rich.
[2737.44 --> 2738.50]  Because I feel like...
[2738.50 --> 2744.06]  I don't want to say I was a moderate, but I definitely, you know, I felt like I felt into, like, camp reasonable.
[2744.74 --> 2746.40]  You know, camp, can't we all get along?
[2746.66 --> 2747.98]  And, yeah.
[2748.20 --> 2752.28]  And I've definitely disengaged and have left that platform right now.
[2752.42 --> 2754.16]  I've been toying a comeback.
[2754.36 --> 2754.64]  I don't know.
[2754.68 --> 2755.68]  I've been thinking about it.
[2755.68 --> 2756.88]  But, like, I really...
[2756.88 --> 2757.26]  I look...
[2757.26 --> 2761.18]  Every time I look at Twitter, I'm like, oh, my God, all the people that are left are the people on the extremes.
[2761.94 --> 2762.92]  You know, like you said.
[2763.06 --> 2765.16]  And it's just, like, the pole tents.
[2765.32 --> 2767.50]  You know, you just see the top of the tents.
[2767.62 --> 2769.30]  But, like, everything in the middle is gone.
[2769.52 --> 2769.82]  You know?
[2769.90 --> 2770.66]  It's like...
[2770.66 --> 2771.70]  It's not just Twitter, though.
[2772.24 --> 2772.90]  It's Reddit.
[2773.34 --> 2774.06]  It's Hacker News.
[2774.14 --> 2777.22]  It's pretty much anywhere that developers hang out on the internet.
[2777.88 --> 2780.28]  I haven't seen quite as much on Mastodon.
[2780.46 --> 2781.52]  There's some talk...
[2781.52 --> 2785.14]  I'm just speaking of this current hooliganism thing going on.
[2785.74 --> 2787.84]  Like, pretty much anywhere on Twitter is the worst place.
[2787.90 --> 2792.40]  It's kind of like, you know, that neighborhood where you're definitely going to get a shiv in your back.
[2792.40 --> 2804.46]  But anywhere that we hang out and chat, it feels like, specifically on this topic, these, you know, X versus Y, is that this kind of activity is par for the course.
[2804.70 --> 2807.28]  I think that's just what the internet has done to all of us.
[2807.78 --> 2807.94]  Yeah.
[2807.94 --> 2813.00]  Twitter is an extreme example, but, you know, the incentives to...
[2813.00 --> 2815.24]  Everyone loves that little dopamine hit of engagement.
[2816.08 --> 2819.04]  And the best way to get engagement is to throw Molotov cocktails.
[2819.24 --> 2819.48]  Right.
[2819.64 --> 2819.88]  And rage.
[2819.90 --> 2820.16]  Yeah.
[2820.22 --> 2822.64]  And I am certainly not above this.
[2822.80 --> 2829.30]  I mean, I actually broke a longstanding rule last week with that whole thing with DHH.
[2829.30 --> 2829.48]  Oh, yeah.
[2829.54 --> 2830.46]  You gave a hard take.
[2830.62 --> 2831.88]  You gave a very hard take.
[2831.98 --> 2833.70]  So I thought I was late to the party.
[2833.70 --> 2837.42]  I saw everyone else talking about this and like everyone was dunking.
[2837.58 --> 2839.04]  But you have a loud microphone.
[2839.26 --> 2839.92]  So it doesn't matter.
[2840.04 --> 2842.44]  Even if you show up late, everybody knows when you show up.
[2842.44 --> 2843.36]  I always forget that.
[2843.50 --> 2843.76]  I always...
[2843.76 --> 2847.72]  In my head, I'm still like a guy with 5,000 followers.
[2848.04 --> 2852.08]  It's like really hard to like mentally adjust to the idea that, oh, there's like people who...
[2852.08 --> 2856.22]  If I tweet this, then like a lot of people are going to think it's like a big sort of pronouncement.
[2856.52 --> 2858.98]  No, it's just me like blowing off steam on a Tuesday afternoon.
[2858.98 --> 2861.04]  What's your rule and why did you finally break it?
[2861.04 --> 2864.50]  So the rule is only do positive quote tweets.
[2864.82 --> 2868.14]  The quote tweet dunk is the lowest form of tweet.
[2869.12 --> 2871.82]  And I've abided by that for a very long time.
[2871.94 --> 2877.20]  And when people quote tweet me to dunk on me, I won't quote tweet dunk on them back.
[2877.72 --> 2880.26]  I'm not going to like try and sick my followers on them or anything like that.
[2880.26 --> 2881.44]  I will reply to them.
[2881.54 --> 2882.92]  And that's usually enough.
[2882.92 --> 2890.24]  But the tweet last week about the Turbo 8 thing, it was just so unambiguously wrong.
[2890.66 --> 2895.46]  And everyone was basically in agreement about that, that I just forgot my rule.
[2895.52 --> 2896.18]  I couldn't help it.
[2896.22 --> 2901.42]  But now I have relinquished any moral high ground that I may have held from having that rule for so long.
[2901.48 --> 2904.80]  And so I do regret a little bit getting involved in that whole thing.
[2905.02 --> 2906.74]  But at the same time, it was kind of fun.
[2906.74 --> 2909.76]  So, I don't know, should we give context?
[2909.82 --> 2915.94]  Because I feel like maybe our listener might not know exactly the tweet that was quote tweeted and what you said about it.
[2915.94 --> 2922.94]  I was just going to say, we'll put a link in the show notes to this famous quote, like, you know, to Jay-Z not realizing that he was Jay-Z.
[2923.46 --> 2924.70]  Like, you know, tweet.
[2925.50 --> 2927.52]  It's like, oh, I forgot I'm Jay-Z.
[2927.64 --> 2931.46]  I guess I can't just go to McDonald's and order a cheeseburger, you know.
[2931.90 --> 2933.44]  It's like, sorry.
[2933.44 --> 2933.84]  Sorry.
[2934.24 --> 2936.22]  You know, it's like, but yeah.
[2936.26 --> 2936.68]  That's good.
[2936.68 --> 2937.34]  We'll definitely put a link.
[2937.46 --> 2939.88]  But yeah, maybe we can read it out loud or share some context.
[2940.14 --> 2942.12]  Like, because I do want to pivot to DHH.
[2942.32 --> 2948.24]  I really didn't want this show to be all about that because there's so much more important nuance to cover here.
[2948.30 --> 2949.96]  And I'm really glad we're having this discussion.
[2950.50 --> 2954.50]  But I think DHH's, his takes were also very specific.
[2954.50 --> 2965.40]  And he listed a slightly different list of reasons than you did, Rich, you know, which is really around like, hey, TypeScript kind of shackles me and shackles my code.
[2965.40 --> 2976.80]  And I'm not able to really write that beautiful, rich expressiveness that you get with just, you know, writing JavaScript and like doing all the fun things that you want to do when you're not restricted.
[2976.80 --> 2978.24]  So, yeah, I don't know.
[2978.28 --> 2980.68]  Should we like pull up that tweet and read it out loud, Jared?
[2980.80 --> 2985.74]  Like, I'm not logged on to Twitter on this machine and I'll have to pull it up on my phone.
[2986.62 --> 2986.64]  But.
[2986.90 --> 2988.22]  Well, I think I'm sure Rich has it.
[2988.36 --> 2988.70]  Yeah.
[2989.10 --> 2991.04]  Rich is like, it's embedded.
[2991.22 --> 2992.86]  It's a feed embedded in my brain.
[2993.66 --> 2995.78]  It's his biggest mistake of the last week.
[2995.92 --> 2996.36]  It's got to be right there.
[2996.36 --> 2998.32]  He's like, I'm recording this podcast through Twitter.
[2998.64 --> 3001.86]  Like, it's like, throw an iframe on next.com, you know.
[3001.86 --> 3003.74]  So a little bit of context around.
[3003.96 --> 3007.38]  So David Hennemeyer Hansen, he's a creator of Ruby on Rails.
[3007.62 --> 3012.64]  He's a very outspoken developer and business guy, quasi professional contrarian.
[3012.72 --> 3014.88]  He's very good at taking a contrarian view.
[3015.54 --> 3029.86]  And he has a library called Turbo, which is a JavaScript library that helps your website go faster by basically hijacking anchor clicks and replacing them with Ajax non-full page refreshes.
[3030.04 --> 3031.64]  It's a longstanding thing.
[3031.86 --> 3033.24]  That's on its eighth version.
[3033.36 --> 3034.26]  It's gone through a lot of iterations.
[3034.48 --> 3035.28]  Actually, we use it.
[3035.58 --> 3038.48]  The older, older Turbo 5, I think, on changelog.com.
[3038.54 --> 3039.56]  I've used it for many years.
[3039.74 --> 3041.26]  It's decent software.
[3041.88 --> 3048.26]  And it's an open source project that's pretty much controlled and managed by him and his company.
[3048.90 --> 3060.12]  And they took TypeScript out of Turbo, not the way that Svelte did it with type annotations or with JS.comments, but just by actually removing it wholesale.
[3060.12 --> 3063.90]  And DHH wrote a blog post about why they did this.
[3063.96 --> 3067.02]  And he had a tweet about it, which Rich has now found.
[3067.50 --> 3069.34]  And I'm clicking on, which says,
[3069.34 --> 3070.72]  So, farewell TypeScript.
[3070.72 --> 3082.90]  May you bring much rigor and satisfaction to your tribe while letting the rest of us enjoy JavaScript in the glorious spirit it was originally designed free of strong typing.
[3082.90 --> 3088.52]  So, that's, I think, probably a pull quote from the blog post as his typical fare is.
[3088.74 --> 3090.02]  So, that's the context.
[3090.24 --> 3093.72]  And then, Rich, you want to dunk on him again?
[3093.82 --> 3094.78]  You should read this in your Jay-Z voice.
[3095.22 --> 3096.94]  Or your Barry White voice.
[3097.02 --> 3097.56]  Either one.
[3097.56 --> 3099.90]  Hang on, I've got to find my own tweet now.
[3102.04 --> 3103.70]  Yeah, I like the Barry White voice.
[3104.20 --> 3105.18]  Okay, here we go.
[3105.42 --> 3106.48]  You want me to read out my own tweet?
[3106.78 --> 3108.08]  Oh, I can pretend guitar.
[3109.22 --> 3109.58]  Okay.
[3111.02 --> 3116.10]  So, just again, for context, a lot of people had already been attacking me.
[3116.52 --> 3118.22]  This sounds like I'm an absolute psycho.
[3118.38 --> 3119.02]  Okay, okay, okay.
[3119.08 --> 3123.42]  This is like being forced with your bad decisions, like, you know, like the morning after.
[3123.42 --> 3124.28]  I'm sorry.
[3124.40 --> 3128.52]  I'm sorry to make you read your naughty tweet on, like, a large podcast.
[3128.94 --> 3132.52]  If I had spent a little bit longer on this tweet and thought a bit more about the reaction,
[3132.78 --> 3134.30]  I probably did change some of the wording.
[3134.60 --> 3135.00]  Okay.
[3135.70 --> 3137.42]  Did you know that you were going to be reading it out loud?
[3137.52 --> 3137.96]  Just kidding.
[3139.76 --> 3140.16]  Anyways.
[3141.00 --> 3145.08]  Removing types from your own code is clownish, epically misguided behavior.
[3145.36 --> 3146.66]  But whatever, to each their own.
[3147.38 --> 3150.82]  Removing types from a library that other people have to use, however,
[3151.16 --> 3153.40]  is just user hostile, d***wattery.
[3153.42 --> 3159.40]  Is d***wattery, is that even a word that we can, we might, yeah, that might even be censored.
[3159.54 --> 3159.94]  I don't even know.
[3159.94 --> 3161.64]  We'll have to find out whether or not it gets leaked.
[3161.98 --> 3164.78]  But it's a great, it's a great turn of phrase, I think.
[3165.18 --> 3165.40]  All right.
[3165.42 --> 3166.76]  So, a little bit of nuance to this as well.
[3166.86 --> 3172.82]  So, the reason I was describing Turbo itself is because it's not exactly the kind of library.
[3173.00 --> 3175.02]  So, I'm kind of defending DHH to a certain extent here.
[3175.38 --> 3176.74]  It's not exactly the kind of library.
[3176.84 --> 3180.84]  You're not going to reference its API inside of your own code.
[3180.84 --> 3187.92]  It's the kind of thing that you link to, you, like, bundle it in, you tell it to go, like, turbo links dot whatever, start.
[3187.92 --> 3193.90]  And then everything else is just data attributes on your HTML, and it kind of does its thing.
[3194.50 --> 3197.26]  So, I understand your statement there.
[3197.42 --> 3203.30]  I think with that particular library, there is a nuance where it's like, no one's going to be doing autocomplete on its functions.
[3203.50 --> 3205.00]  Like, it's mostly just internal stuff.
[3205.00 --> 3210.92]  And you just write your HTML to conform to the way it works, and that's how you use it.
[3211.36 --> 3213.36]  It does expose a public API, though.
[3213.76 --> 3214.20]  Oh, it does.
[3214.56 --> 3214.68]  Yeah.
[3214.84 --> 3217.12]  But that would be an atypical use case for it.
[3217.18 --> 3220.94]  I mean, I'm a user of the version 5, so I know that part, at least back then.
[3221.28 --> 3222.52]  Maybe it's changed from 5 to 8.
[3222.52 --> 3229.48]  But giving him a little bit of credit, it's not like pulling our library and using our API is how you do it.
[3230.00 --> 3231.26]  Fair enough, it has a public API.
[3231.42 --> 3234.74]  So, he's still removing features from his users.
[3234.84 --> 3239.92]  So, I don't completely disagree with you, but it's a little bit better than I think people give it credit for.
[3239.92 --> 3240.28]  Yeah.
[3240.48 --> 3248.86]  Well, I mean, people, I mean, DHH could, like, tell everyone that he's opened up an orphanage, you know, in South America, and I think people would still dunk on him.
[3248.92 --> 3251.24]  I think at this point, I think he's just kind of like, first.
[3251.24 --> 3252.14]  Yeah, he's earned that level of dunkage.
[3252.14 --> 3254.68]  Yeah, he's just persona non grata for some people.
[3254.84 --> 3255.30]  And you know what?
[3256.08 --> 3256.58]  I don't know.
[3256.68 --> 3264.64]  You know, I mean, this is, again, like, this is just, I personally don't think it's healthy as a community to dunk on people that we disagree with philosophically.
[3264.64 --> 3273.00]  Like, I think, like, it's important to have diversity in thought, like, as long as somebody isn't, like, being hateful towards others, like, they're allowed to exist, right?
[3273.20 --> 3274.32]  Like, it's whatever.
[3274.80 --> 3275.74]  So, but anyway.
[3276.08 --> 3276.38]  So, yeah.
[3276.44 --> 3278.14]  So, did anybody read the blog post?
[3278.22 --> 3279.14]  Because I didn't.
[3279.52 --> 3281.18]  So, thoughts on the blog post?
[3281.76 --> 3289.02]  The reason that this is such perfect fodder for passionate nerd arguments is that there's just so much going on there.
[3289.02 --> 3294.98]  No matter what your bias is, what your priors, you can find something to strongly agree with or strongly disagree with.
[3295.42 --> 3299.34]  Even just the bit of the article that he quoted in the tweet that you just read out.
[3300.02 --> 3305.48]  Let the rest of us enjoy JavaScript in the glorious spirit it was originally designed free of strong typing.
[3306.06 --> 3307.98]  It wasn't designed at all.
[3308.04 --> 3311.90]  It was thrown together by Brendan Eich over, like, a weekend in 1980.
[3312.48 --> 3312.94]  It's a hack.
[3313.24 --> 3313.44]  Yeah.
[3313.56 --> 3313.84]  Okay.
[3313.88 --> 3314.44]  It wasn't 1980.
[3314.54 --> 3315.84]  It was a little bit more recent than that.
[3315.84 --> 3319.18]  But, you know, this is not something that-
[3319.18 --> 3319.40]  Fact check.
[3319.78 --> 3320.74]  I'm out with a fact check.
[3322.36 --> 3325.60]  Like, it's not like JavaScript was supposed to be this way.
[3326.34 --> 3328.14]  Like, this is just like what we-
[3328.14 --> 3329.02]  It's an afterthought, yeah.
[3329.04 --> 3332.82]  And before that, like, may you bring much rigor and satisfaction to your tribe?
[3333.04 --> 3341.64]  Well, Matt Pocock, who, like, to be fair, is a TypeScript educator and so has a little bit of a bias here, pointed out that, like, consistently in survey responses,
[3341.64 --> 3347.30]  TypeScript is a very large majority of, like, TypeScript slash JavaScript users.
[3347.52 --> 3349.62]  So, like, it's not a tribe anymore.
[3349.86 --> 3360.46]  And even looking beyond the people who self-identify as TypeScript users, every JavaScript user in 2023 is a TypeScript user, whether they're aware of it or not.
[3360.46 --> 3371.32]  Because the minute that you start typing some code in VS Code, the minute that you start referencing anything from an external library, it's pulling in the type definitions and it's giving you IntelliSense and autocomplete and all of that stuff.
[3371.56 --> 3373.24]  So everyone is a TypeScript user.
[3373.50 --> 3376.62]  It's just that a lot of people aren't, like, aware of it.
[3377.22 --> 3384.46]  And so just in that very small amount of space, like, just that tweet, there's, like, a lot of different things to engage with.
[3384.46 --> 3385.28]  Yeah, yeah, yeah.
[3385.34 --> 3391.46]  But in the piece itself, I mean, it begins with, like, we can't do a full read-through because there's just so much in here.
[3391.60 --> 3392.84]  But, like, it begins with...
[3392.84 --> 3393.86]  You know what, actually, I would totally be fine with this.
[3393.86 --> 3394.38]  If you do the voice.
[3394.60 --> 3396.12]  Yeah, that's exactly what I was going to say.
[3396.14 --> 3402.22]  I was like, if you read it like you're Barry White, but, you know, just joking.
[3402.22 --> 3402.66]  Well, let's begin.
[3403.00 --> 3406.18]  By all accounts, TypeScript has been a big success for Microsoft.
[3406.98 --> 3409.78]  Like, straight away, we're getting some digs in at Microsoft.
[3409.78 --> 3415.96]  It's like I'm, like, teenage me renaming the Internet Explorer icon to Internet Explorer.
[3416.18 --> 3416.54]  Right, right.
[3416.64 --> 3417.50]  Spelling Windows.
[3417.86 --> 3419.60]  W-R-M-D-O-Z-E.
[3419.74 --> 3420.86]  Take that, Bill Gates.
[3421.08 --> 3424.64]  It's like, no, it's like, yeah, okay, so Microsoft main...
[3424.64 --> 3427.98]  Or the MS-DOS, and you do it with the M dollar sign.
[3428.12 --> 3430.16]  You're like, yeah, M dollar sign, DOS.
[3430.58 --> 3433.54]  That was one that we used to do because, like, Microsoft's all about money.
[3433.66 --> 3434.10]  So true.
[3434.10 --> 3441.98]  Well, as I said before, he's very skilled at being contrarian and just drawing out people's ire.
[3442.52 --> 3444.12]  And so he brings a lot of it upon himself.
[3444.24 --> 3446.22]  I mean, I think he actually enjoys that.
[3446.50 --> 3453.10]  I actually have been around DHH long enough to know how much he despised JavaScript for many years
[3453.10 --> 3455.48]  and would do anything possible not to write it.
[3455.86 --> 3459.96]  And so that sentence from the quote tweet is particularly interesting for me
[3459.96 --> 3463.38]  because I know that he just despised JavaScript so much.
[3463.42 --> 3466.86]  And this is the way that it was designed to be, you know, like, it was so good.
[3466.96 --> 3469.72]  Well, in the blog post, he says, the fact is that I actually rather like JavaScript.
[3469.98 --> 3473.14]  I'd go so far as to say it's my second favorite language after Ruby.
[3473.70 --> 3476.08]  Yes, a distant second, but a second nonetheless.
[3476.08 --> 3476.56]  Oh, my gosh.
[3477.56 --> 3478.98]  Because Ruby's so perfect, right?
[3479.38 --> 3480.72]  Well, that's the thing.
[3480.84 --> 3484.78]  I mean, Ruby is, like, a pretty divisive language.
[3484.78 --> 3492.54]  Like, you know, I think that part of the reason that this created such a fuss was that,
[3492.88 --> 3497.84]  you know, to talk about tribes and communities again, the Rubyists are very much not our tribe.
[3498.32 --> 3504.36]  Like, the JavaScript and TypeScript big tent, like, the broader coalition of JavaScript and TypeScript developers,
[3504.78 --> 3510.86]  you know, is going to feel like an attack if a Rubyist comes along and says,
[3511.00 --> 3512.80]  you're doing it wrong, like, you don't know what you're doing.
[3512.86 --> 3513.66]  Right, right, right.
[3513.66 --> 3517.04]  No, that's very, you know what, thank you for pointing that out, Rich,
[3517.08 --> 3522.08]  because I feel like I didn't quite follow the reaction that you got when you first went public
[3522.08 --> 3527.94]  with this announcement for Spell to Spell to Guild, but, like, I think the HH being kind of in that,
[3528.12 --> 3533.36]  yeah, like a Rubyist and, like, from a different, you know, different tribe, you know,
[3533.48 --> 3536.08]  adjacent tribe where there's a Venn diagram, but definitely, like,
[3536.66 --> 3539.58]  a lot of people who are writing Ruby code are not writing JavaScript, right?
[3539.58 --> 3546.54]  Like, dunking on TypeScript and then dunking, you know, like, and calling JavaScript cooler than TypeScript.
[3546.70 --> 3552.20]  Yeah, like, I can see how that would really be, like, Molotov cocktail times a thousand, you know?
[3552.34 --> 3552.96]  Like, that's really...
[3552.96 --> 3557.10]  And I think you could make the case that TypeScript has made JavaScript less Ruby-like.
[3557.38 --> 3557.88]  A hundred percent.
[3557.88 --> 3564.16]  Like, the two languages used to have some kind of spiritual similarities in the, like, the dynamic nature,
[3564.32 --> 3569.22]  like, the way that you can just kind of get in there and monkey-patch globals and all of that stuff.
[3569.28 --> 3573.70]  Like, you don't really do that if you're writing TypeScript because the compiler's going to yell at you for a good reason.
[3573.92 --> 3575.64]  Like, you shouldn't do that because it's dumb.
[3575.88 --> 3584.68]  But, like, there's still this cultural shift that I think has been kind of encouraged, maybe, slash forced by the rise of TypeScript.
[3584.68 --> 3585.12]  Yeah.
[3585.44 --> 3586.14]  No, absolutely.
[3586.38 --> 3587.72]  I couldn't agree with you more.
[3588.16 --> 3591.34]  So, I want to make sure we have time for our listeners' questions, Rich.
[3591.42 --> 3595.24]  So, if you're not in our Slack channel, what are you waiting for?
[3595.44 --> 3601.98]  Join the Changelog Slack channel and then join the JS Party channel in particular.
[3602.66 --> 3606.80]  But, yeah, so I asked the listeners, like, for their hot takes and questions.
[3607.04 --> 3607.86]  And there was quite a few.
[3608.22 --> 3612.50]  Too many for me to, like, go through line by line here, but I'm just kind of paraphrasing.
[3612.50 --> 3613.70]  Kyle Beard was one of them.
[3614.20 --> 3619.26]  And, essentially, his whole thing was, like, I don't get how someone could do something this hostile, right?
[3619.42 --> 3622.40]  And, like, I mean, this seems, like, super, super hostile.
[3622.68 --> 3624.34]  And, like, how many – his question was, like –
[3624.34 --> 3625.72]  Are we talking about the PR or my tweet?
[3625.74 --> 3626.62]  No, no, no.
[3626.62 --> 3630.56]  We're talking about – we're talking about the DHH thing specifically.
[3630.58 --> 3632.28]  The Turbo 8 removal of TypeScript.
[3632.28 --> 3641.60]  Yeah, like, any project that would basically flat out remove TypeScript without, like, providing type support, like, you know, that feels very hostile.
[3641.60 --> 3646.76]  And so his thing was, like, how many CI runs are broken because of Turbo this morning, right?
[3646.96 --> 3647.96]  Which I think is a fair –
[3647.96 --> 3650.44]  Well, they haven't released it yet, so none so far.
[3650.44 --> 3650.88]  Okay, good to know.
[3650.98 --> 3653.30]  But it will be interesting to see if that happens.
[3653.82 --> 3656.28]  Yeah, which would make a fair point, you know?
[3656.72 --> 3657.36]  I don't know.
[3657.44 --> 3660.42]  I mean, given that you didn't do that, you can't answer that.
[3660.68 --> 3662.60]  But – so I guess the answer is really –
[3662.60 --> 3663.86]  I mean, I can stab a guess.
[3663.96 --> 3669.88]  I think the way that you would do – the reason that you would do that is if you literally don't understand what the purpose of the type declaration files is.
[3669.88 --> 3671.62]  Like, what benefit it brings to people.
[3671.92 --> 3679.94]  If you think of it as just, like, some box that I have to check, like, filling out a package.json correctly, then you'll be like, eh, I don't care about this.
[3680.00 --> 3680.92]  Like, I see no benefit.
[3681.50 --> 3685.64]  But if you use JavaScript libraries and you're part of, like, the JavaScript TypeScript ecosystem,
[3685.64 --> 3697.16]  and you've experienced the difference between a library that has good types and a library that just doesn't bother or, like, delegates it to definitely types or something like that, then you'll be a lot more sympathetic.
[3697.40 --> 3703.48]  And I think what was at the core of this whole thing was a lack of empathy for the people who are affected by this.
[3703.68 --> 3704.72]  Yeah, yeah, that makes sense.
[3704.72 --> 3715.36]  So, Daniel Buckmaster had a question – well, this is more of a comment, and they were like, well, you know, this is really interesting timing around this, like, removal of TypeScript,
[3715.70 --> 3721.44]  especially when projects like YesBuild and Denno and Bun are all trying to actually add support.
[3721.60 --> 3726.74]  So, like, I – and I think that's an interesting point, but I'm curious if you have any thoughts on that.
[3726.74 --> 3732.06]  Yeah, I mean, I'm – Denno and Bun are adding TypeScript, but Chrome isn't.
[3732.68 --> 3737.30]  So I would prefer that packages continue to ship JavaScript.
[3737.88 --> 3744.12]  Like, if I have to start transpiling stuff to run – stuff that I've installed from Node modules, then I'm going to be mad.
[3744.40 --> 3748.00]  Are you excited about the type annotations proposal? Is that something you've looked at and you're –
[3748.00 --> 3748.90]  Oh, yes, extremely.
[3749.18 --> 3751.74]  Yeah, so I don't know how many people are aware of this.
[3751.92 --> 3755.02]  I think it's absolutely huge, and I really hope it comes to pass.
[3755.02 --> 3760.82]  Essentially, the idea is that you can write TypeScript syntax or something very close to TypeScript syntax inside JavaScript,
[3761.24 --> 3765.00]  and the JavaScript engine essentially just treats it as an inline comment and ignores it.
[3765.42 --> 3769.54]  And the idea is that, in theory, you can express any type system in there.
[3769.62 --> 3771.10]  In practice, it will be TypeScript.
[3771.86 --> 3776.58]  And so you can have type-check JavaScript without any transpilation whatsoever.
[3777.38 --> 3783.02]  And it will just put this whole argument about should you use .ts or should you use .js with js.to bed once and for all.
[3783.02 --> 3785.60]  And I, for one, could not be more excited.
[3786.10 --> 3786.20]  Yeah.
[3786.32 --> 3790.18]  I mean, you're basically doing that already just with the help of a library.
[3790.70 --> 3795.24]  And, like, once it's supported in JavaScript engines, you won't need JSDoc.
[3795.32 --> 3800.78]  You can just do this, like, using the famous web platform that we keep hearing about, right?
[3800.90 --> 3802.76]  Like, just use the platform, right?
[3802.98 --> 3804.34]  That we keep hearing about.
[3804.48 --> 3804.80]  Yeah.
[3805.04 --> 3805.66]  One of these days.
[3805.66 --> 3807.08]  When's that web platform going to come out?
[3807.10 --> 3807.44]  Yeah.
[3807.44 --> 3808.04]  Like, yeah.
[3808.36 --> 3809.20]  This thing.
[3809.70 --> 3813.30]  And lastly, Shock Neatling says, quote, I am here for it.
[3813.58 --> 3822.68]  I have been saying that, especially on the front end, I lose a lot more time using TypeScript than any time it could possibly spare me from potential runtime bugs.
[3823.00 --> 3825.64]  On the API side, it makes a lot of sense, though.
[3825.98 --> 3827.16]  This is kind of how I feel.
[3827.16 --> 3834.46]  But, of course, like, it would be completely irresponsible for me, especially when working in a large-scale application or with other developers.
[3835.00 --> 3840.32]  I think in 2023, it would be responsible for me to not use TypeScript in application code.
[3840.44 --> 3841.58]  That's just my personal opinion.
[3841.70 --> 3845.00]  And it's fine for, you know, you can have a different opinion and that's fine.
[3845.06 --> 3847.28]  It doesn't make you a bad person, despite what the internet says.
[3847.84 --> 3848.46]  But, yeah.
[3848.58 --> 3849.88]  I mean, what are your thoughts on that, Richard?
[3849.88 --> 3852.56]  We kind of talked about that a little bit earlier, right?
[3852.56 --> 3861.74]  But I feel like maybe your expertise in TypeScript helps you have, like, minutes lost to TypeScript every week versus hours.
[3861.88 --> 3866.58]  Because I've seen some people just literally will spend hours struggling with TypeScript.
[3866.76 --> 3867.66]  And that's not uncommon.
[3868.46 --> 3872.04]  I have so much empathy for people in that position because I've definitely been there.
[3872.62 --> 3877.66]  When you first start using TypeScript, you really do feel like this is just busy work.
[3877.66 --> 3882.68]  I am just writing all of this extra junk to appease the compiler and it's not doing anything for me.
[3883.10 --> 3892.18]  And then at a certain point in my experience, and this has happened to me and it's happened to so many people that I've talked to and that I've, like, personally helped on the TypeScript journey.
[3892.66 --> 3894.14]  At some point, it kind of clicks.
[3894.56 --> 3899.08]  And then you realize that you're not fighting with the compiler anymore.
[3899.22 --> 3901.78]  You're just giving the compiler the means to help you.
[3901.78 --> 3909.70]  And I think what sometimes happens is people aren't aware of the degree that you can take advantage of inference, for example.
[3910.04 --> 3912.66]  Like, you feel like you need to annotate every variable declaration.
[3912.82 --> 3915.42]  When actually, like, by and large, you don't need to do that.
[3915.60 --> 3917.36]  Like, TypeScript has got your back.
[3917.92 --> 3922.86]  And it's this difference between fixing the types and doing type-driven development.
[3923.04 --> 3927.92]  And once you manage to flip from one into the other, it's super hard to go back.
[3927.92 --> 3929.48]  And so I get it.
[3929.54 --> 3931.84]  Like, I understand why someone would feel that way.
[3932.48 --> 3935.06]  All I can say is, keep at it.
[3935.26 --> 3935.96]  It gets better.
[3936.50 --> 3936.66]  Yeah.
[3936.80 --> 3937.46]  Yeah, it does.
[3937.54 --> 3938.02]  It does.
[3938.14 --> 3941.50]  And once you're over the hump, you know, it really does get better.
[3941.60 --> 3943.00]  You just have to keep plighting it, though.
[3943.58 --> 3945.94]  Just work towards getting over the hump, you know.
[3946.56 --> 3949.56]  And in the meantime, just slapping any on there.
[3949.76 --> 3950.06]  Yeah.
[3950.36 --> 3950.60]  Bam.
[3950.80 --> 3951.78]  Like, it's fine.
[3951.86 --> 3952.70]  It's there for a reason.
[3953.18 --> 3953.94]  That's right.
[3954.14 --> 3956.62]  Or even, like, a TS ignore comment.
[3956.62 --> 3962.38]  Like, if there's something that you just can't get to work, then, like, just ignore it for now and come back to it later.
[3962.50 --> 3963.76]  Or get someone else to do it for you.
[3963.90 --> 3964.00]  Yeah.
[3964.40 --> 3965.98]  I could not agree with you more.
[3966.58 --> 3969.66]  So, I mean, Rich, it's been an absolute pleasure having you on the show.
[3970.06 --> 3975.88]  I'm kind of, like, my last question is just, like, what's the magic wish for the future here?
[3976.06 --> 3979.40]  Like, where do you see this landing in, like, a year or two?
[3979.82 --> 3980.72]  This whole situation.
[3981.32 --> 3984.36]  Please let the type annotations proposal happen.
[3984.36 --> 3992.18]  The one thing that scares me a little bit is the fact that it is, like, it has to be language agnostic or type system agnostic.
[3992.18 --> 3995.92]  Because otherwise that really would represent, like, a capture of the language by Microsoft.
[3997.42 --> 4004.16]  And so there is clearly, like, still potential for tribalism and nerd fights and whatever.
[4004.16 --> 4017.38]  But just having the ability to write TypeScript syntax in JavaScript and have it strongly typed and type checked, but also have it just run everywhere without any need for all of these complex build chains.
[4017.52 --> 4022.04]  It's going to make so many people, especially me, really, really happy.
[4022.24 --> 4024.58]  And so I just pray that that happens.
[4024.98 --> 4025.08]  Yeah.
[4025.42 --> 4026.32]  Amen to that.
[4026.46 --> 4027.62]  Your lips to God's ears.
[4027.62 --> 4032.54]  So, Jay-Z, Barry White, Rich Harris, it's been so fun.
[4033.42 --> 4040.94]  I ask this to everyone, but where can folks connect with you online if they want to give you hot takes or give you high fives?
[4041.48 --> 4051.08]  Well, I am still a hostage to twitter.com slash rich underscore Harris, at least until they finally destroy that place.
[4051.08 --> 4056.56]  And, I don't know, GitHub, come and look at the Svelte and the SvelteKit projects.
[4056.68 --> 4057.88]  That's where I spend most of my time.
[4058.54 --> 4061.12]  Join the discords for those projects and come out.
[4061.48 --> 4062.76]  Yeah, that sounds great.
[4062.86 --> 4064.16]  Well, thank you again, Jared.
[4064.22 --> 4068.60]  It's been fun having you co-paneling or whatever the word is.
[4068.60 --> 4069.10]  Thanks for having me.
[4069.16 --> 4070.60]  And thanks for not having Nick here.
[4070.68 --> 4071.56]  That was really a good call.
[4071.86 --> 4073.06]  Oh, no, no, no.
[4073.28 --> 4074.24]  It's not my fault.
[4074.38 --> 4077.64]  His immune system, like, gave out in the wrong week.
[4077.64 --> 4079.64]  I'm glad you uninvited him at the last minute.
[4079.64 --> 4081.22]  Now you're going to start a controversy.
[4081.82 --> 4082.50]  Like, anyways.
[4082.94 --> 4083.42]  All right, guys.
[4083.48 --> 4086.12]  So, next week, back to our regularly scheduled programming.
[4086.56 --> 4088.84]  So, show on JavaScript security.
[4089.10 --> 4091.16]  Unless there's another emergency in the meantime.
[4092.08 --> 4093.20]  Unless there's another emergency.
[4093.70 --> 4097.26]  An awesome show on JS security with Ron Paris.
[4097.82 --> 4099.66]  He's an security engineer at Reddit.
[4099.78 --> 4101.34]  We worked together when we were at NPM.
[4101.46 --> 4101.96]  He's phenomenal.
[4102.24 --> 4103.88]  Just bring your notebook to that podcast.
[4104.24 --> 4105.94]  So, with that said, have a good one, y'all.
[4105.94 --> 4106.50]  Cheers.
[4109.64 --> 4116.78]  All right, party people.
[4117.14 --> 4119.96]  That concludes this emergency pod.
[4120.52 --> 4122.76]  We know it's not an actual emergency.
[4123.16 --> 4125.42]  But emergency pod is just fun to say.
[4125.80 --> 4127.46]  And it makes us feel important.
[4128.38 --> 4135.18]  Speaking of important, our Changelog++ members are super important when it comes to sustaining our continued efforts.
[4135.18 --> 4140.48]  So, we hook them up with bonuses at the end of an increasingly high percentage of our shows.
[4141.18 --> 4142.68]  This episode is no exception.
[4143.08 --> 4146.58]  So, stick around, Plus Plus people, for your Rich Harris bonus question.
[4147.08 --> 4156.78]  If you'd like to get in on these bonuses, ditch the ads, and directly support our work, sign up today at changelog.com slash plus plus.
[4157.12 --> 4157.70]  It's better.
[4157.70 --> 4164.18]  Thanks, once again, to our partners, Fastly.com, Flyto.io, and Typesense.org.
[4164.82 --> 4170.14]  And to our mysterious friend, Breakmaster Cylinder, for being our beat freak in residence.
[4170.62 --> 4175.00]  Next up on the pod, Amel and Chris are joined by Ron Paris.
[4175.54 --> 4182.58]  Ron is a security engineer at Reddit, and they'll be talking best practices and common pitfalls when securing your code.
[4183.44 --> 4184.56]  Stay tuned right here.
[4184.56 --> 4187.12]  We'll have that episode ready for you next week.
[4187.70 --> 4198.50]  Game on!
