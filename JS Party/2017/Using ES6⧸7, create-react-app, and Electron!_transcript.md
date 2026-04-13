[0.00 --> 5.92]  Bandwidth for JSParty is provided by Fastly. Learn more at Fastly.com.
[10.24 --> 14.40]  Welcome to JSParty, a weekly celebration of JavaScript and the web.
[14.76 --> 19.72]  Tune in live on Fridays at 3 p.m. U.S. Eastern at changelaw.com slash live.
[19.72 --> 24.12]  Join the community and Slack with us in real time. Head to changelaw.com slash community.
[24.42 --> 28.34]  Follow us on Twitter. We're at JSPartyFM. And now on to the show.
[28.34 --> 32.44]  Hey, everybody. Welcome to JSParty. It's a party every week with JavaScript.
[33.06 --> 34.86]  We're back. I'm Michael Rogers.
[35.38 --> 36.40]  I'm Rachel White.
[36.80 --> 38.24]  And I'm Alan Sampson.
[38.84 --> 44.08]  Yep. And Rachel and I are back from a nice little vacation in Europe.
[44.98 --> 51.06]  If you didn't, like, check out the episode where YayQuery took over.
[51.14 --> 52.76]  Definitely go back and listen to that one.
[52.82 --> 56.16]  That one was so good that Rachel and I were actually fired.
[56.16 --> 60.62]  I got a text from Adam Stachowiak while I was in Europe, but just said you're fired.
[61.54 --> 64.56]  And then it turned out that they can't do it.
[64.70 --> 67.94]  They can't schedule it for another nine months.
[68.20 --> 73.44]  So we're filling in now for them until they can come back around.
[74.10 --> 75.00]  All right. Let's jump into it.
[75.00 --> 84.30]  Okay. So we're going to talk about actually using ES6 and ES7 features, new language features,
[84.40 --> 87.34]  with and without compilers and some of the trade-offs and stuff like that.
[88.04 --> 89.34]  Don't look at my years now.
[89.74 --> 91.32]  Is it ES2015?
[91.32 --> 97.46]  I think that we should just talk about specific features rather than what bucket they land in,
[97.54 --> 99.90]  because they actually get implemented sort of out of order anyway.
[100.16 --> 100.28]  Right.
[100.62 --> 106.92]  So Rachel, what features are you using that you've been enjoying from the new language stuff?
[107.62 --> 108.18]  I'm not.
[109.54 --> 110.10]  You're not.
[110.10 --> 110.12]  You're not.
[110.12 --> 110.14]  You're not.
[110.14 --> 110.20]  You're not.
[110.20 --> 110.74]  You're not.
[110.74 --> 110.92]  You're sick.
[110.92 --> 116.90]  No. I mean, the only thing that I've used really, because since I don't write production code,
[116.96 --> 118.16]  nobody tells me what to do.
[118.28 --> 122.78]  So I kind of just do what I've always done.
[122.98 --> 129.60]  So I've worked with some things that have the new variable naming and stuff like that.
[129.62 --> 132.84]  But that's really all that I've dipped my toes in.
[132.94 --> 134.12]  And what is the other thing?
[134.12 --> 135.64]  Like let is in there?
[135.78 --> 136.26]  I don't know.
[136.68 --> 137.28]  Enlighten me.
[137.96 --> 138.76]  Let's been there forever.
[138.76 --> 145.78]  I think the big ones for me have been arrow functions and template literals.
[146.12 --> 147.78]  The arrow functions are super cool.
[147.96 --> 152.16]  And I totally get that it helps with readability so much.
[152.74 --> 156.98]  But I'm still stuck in that mindset of forgetting to use it.
[157.12 --> 160.74]  And I feel like if I'm going to incorporate all of the new type of things,
[160.74 --> 165.30]  I'm going to have to enforce it to strict in my code linting.
[165.30 --> 169.76]  But other than that, I'm not actively going out of my way to use it.
[169.82 --> 172.56]  Because nobody tells me what to do when I write code.
[174.62 --> 176.46]  So let me jump in.
[176.94 --> 182.74]  I think I disagree that it makes code more readable.
[183.08 --> 189.64]  I often am looking at typed and arrow function JavaScript.
[189.64 --> 192.98]  So there are types in there and then there are arrow functions.
[193.18 --> 195.08]  And people use implicit returns and stuff.
[195.50 --> 200.14]  And I look at it and it does not look recognizable to me.
[200.54 --> 202.88]  I'm smart enough to figure it out or whatever.
[203.00 --> 205.40]  But I can no longer scan it the same way.
[205.52 --> 205.88]  I don't know.
[205.94 --> 207.80]  It's just a skill that you can do.
[208.26 --> 211.56]  I'm lucky enough that a lot of the stuff that I work on is fairly small.
[211.78 --> 214.40]  So when it's much smaller scale, I think it's readable.
[214.40 --> 220.46]  But I could totally get if you're looking at larger systems where you would be scanning through a lot of lines,
[220.52 --> 222.92]  it would be kind of hard to pattern match.
[224.24 --> 229.44]  It certainly encourages unnamed functions for one thing.
[229.98 --> 231.44]  Yeah, that's true.
[231.80 --> 233.68]  I don't like anonymous functions.
[233.90 --> 235.92]  I like to try and name everything if I can.
[236.74 --> 237.18]  I don't know.
[237.18 --> 249.10]  I mean, they've gotten so small and so kind of easy to use that I'm able to use them in ways that you wouldn't use functions before because it would just be too verbose.
[249.44 --> 249.54]  Right.
[250.10 --> 260.96]  There's a couple libraries that I've written for like templatized HTML and using functions inside of a template literal and stuff like that.
[261.00 --> 263.10]  Like that would have just been too verbose beforehand.
[263.42 --> 263.56]  Right.
[264.14 --> 264.42]  Sure.
[264.42 --> 276.36]  And I think I mean, I was certainly one of those people like I mean, you can dig up me saying this, that like the problem with arrow functions is that it's just a bunch of extra semantics that you have to keep in your head, which is true.
[276.36 --> 277.42]  Like it is.
[277.88 --> 283.22]  And like to your point, Alex, it's certainly not as easily readable as the word function.
[283.38 --> 284.98]  It's pretty clear what that is.
[285.26 --> 287.14]  This arrow thing could be anything.
[287.14 --> 287.46]  Right.
[287.78 --> 292.34]  And so it is more semantics you have to keep in your head like like any other language rule.
[292.34 --> 295.96]  So, but the net of semantics, the semantics.
[296.16 --> 297.56]  So just sorry to interrupt.
[297.72 --> 304.40]  The semantics are are maybe easier because it's just like it's we talked about this a little bit where you're gone.
[304.40 --> 312.08]  It is kind of just literal scope of the variables.
[312.14 --> 312.88]  There's no bound.
[314.00 --> 316.34]  It's just lexical scope of variables.
[316.34 --> 326.98]  So you can reason about what a variable or what this is much more simply because it's impossible for it to be anything but lexical, lexically bound.
[326.98 --> 334.16]  So to some degree, like you can forget about some things that functions add.
[334.54 --> 340.44]  And then to another degree, like it's hard to scan maybe, especially with implicit returns.
[341.14 --> 341.24]  Yeah.
[341.34 --> 341.46]  Yeah.
[341.46 --> 348.78]  I was just going to say whatever sort of complexity they they take take out of the pool by by by not having this.
[348.78 --> 351.24]  Um, they probably add it with the implicit return stuff.
[351.34 --> 363.58]  But so I'm I don't know if you saw this or not, but there was a, uh, a post that somebody did where he was essentially saying that his his style guide now is that he no longer uses the function keyword ever.
[363.58 --> 365.64]  So he doesn't use old style functions anywhere.
[365.64 --> 373.72]  Um, everything is arrow functions, um, and classes, um, have like a different new function syntax for properties.
[373.72 --> 380.62]  And so he uses those when when you would have traditionally used, um, functions for any kind of prototypal stuff or or referencing this.
[380.62 --> 382.12]  Um, and I'm curious.
[382.78 --> 387.50]  Is this just for like personal projects or is this like in practice in his job?
[388.18 --> 389.26]  Or you do not know?
[389.50 --> 390.24]  I think both.
[390.40 --> 390.92]  I think both.
[390.92 --> 395.74]  I mean, he's certainly advocating it to other people, which I assume, you know, would also be for production use.
[395.90 --> 403.86]  But I think that the argument that this actually can reduce complexity if you stop using older syntax is one that comes up a lot.
[403.92 --> 404.70]  Like people talk about.
[405.14 --> 405.34]  Yeah.
[405.52 --> 409.82]  You know, like like eventually the language does get simpler if we can stop using some of these older forms.
[410.00 --> 413.28]  Um, and this is this is certainly, you know, somebody advocating for that.
[413.28 --> 423.44]  But so the, the primary rift I had with the person at my company who felt the same was that I was thinking of functions as the default and arrows as the sugar.
[423.44 --> 435.50]  And he was thinking of arrows as the default and functions as the sugar because arrows are other than in implicit returns are simpler in the sense that they can't be bound.
[435.70 --> 445.22]  And so he's like, well, why would we use the more complex one that can have all these weird binding situations instead of using the default arrow functions, which are lexically bound.
[445.22 --> 446.40]  And so you always know.
[446.94 --> 452.32]  And so like, for me, an unbound function keyword is fine.
[452.82 --> 456.96]  Like an unbound function is fine because like, I'm just not using this inside of it.
[457.02 --> 462.94]  But for him, it's like, why would you use the thing that could be bound when you could just use the thing that's always lexically bound.
[463.34 --> 473.88]  And so it's an interesting like perspective of once you kind of switch over, like seeing the arrows as the default and the function as like this thing that can be different.
[473.88 --> 490.28]  The problem is that, so even, I forgot who you said does this, but the class functions, if you just use the syntax inside classes where you do, you know, a class and then you just tab inside the blocks and you do function name.
[491.34 --> 492.92]  That is not an arrow function.
[493.12 --> 494.16]  It's not lexically bound.
[494.16 --> 504.88]  And you have to do function name equals open parens arrow function function in order to get a lexically bound function in there.
[504.94 --> 507.52]  So it's actually like you kind of have to modify some of that syntax.
[508.06 --> 514.58]  And then like if you decide, okay, I'm always going to use that syntax, like the constructor inside of there can't be listed like that.
[514.64 --> 516.00]  You have to do the constructor the old way.
[516.00 --> 524.12]  And so it could be bound, but you can't find constructors and then like a whole bunch of things like that start getting weird.
[524.80 --> 528.10]  Well, in the case of classes, though, you often do want to reference this, though.
[528.18 --> 529.24]  Like you have a use for that.
[529.36 --> 532.92]  I think that what he was saying was that we can take the function keyword out of it at least.
[533.08 --> 534.54]  And then we can not have this ambiguity.
[534.80 --> 535.32]  Yeah, no.
[535.42 --> 540.00]  So what I'm saying is that if you use arrow functions, the functions can't be rebound.
[540.00 --> 549.62]  It's guaranteed to be lexically bound, whereas if you use just the class syntax, it more mimics using the function keyword.
[549.98 --> 554.28]  And then using this will default to the right thing probably to what you want.
[554.28 --> 562.64]  But pulling it out, like if you just use an instance, kind of like a static function, like this can change very quickly to window.
[563.40 --> 565.52]  Like all those types of problems start to show up again.
[565.52 --> 571.76]  And it's just sugar for, you know, prototypal properties on an object.
[572.22 --> 574.90]  So there are still gotchas if you use the class syntax.
[575.12 --> 581.68]  Like you could still go further and say, I still want to use arrow syntax inside of my classes, if that makes sense.
[582.86 --> 583.60]  Yeah, yeah.
[583.66 --> 585.18]  I guess you could take it.
[585.18 --> 593.38]  And I think if you are going to say we require arrow functions everywhere they can be used, you should also require them in classes.
[593.38 --> 609.48]  So rather than saying like function name, open paren arguments, and then brackets with the function, you should say function name equals open paren fat arrow brackets, if that kind of makes sense.
[609.56 --> 609.90]  Yeah, yeah.
[609.96 --> 615.28]  I don't think that the point that any of these people are trying to make, though, is to be zealots about arrow functions.
[615.28 --> 621.58]  I think the point that they're making is that we can deprecate the use of the function keyword and just rely on these new rules.
[621.82 --> 622.28]  Yeah, I disagree.
[622.64 --> 629.76]  And then we get out of a lot of like ambiguity if we're just using the new rules around classes.
[630.32 --> 636.40]  I think I disagree on what those people, at least the people I've talked to who are doing this, aren't necessarily.
[636.40 --> 642.46]  They're not doing it just because they think it looks better or it's smaller or it's more streamlined or anything like that.
[642.50 --> 649.30]  They're explicitly doing it because of the lexically bound ambiguity like problems go away.
[649.78 --> 656.42]  And so you end up with a program that only has lexically bindable functions.
[656.42 --> 667.86]  And so it's important to do it everywhere, even if the syntax is old, like if there's some way to use the old function syntax and then just say, oh, this is a lexically bound function.
[668.18 --> 669.24]  Like they would still be cool with that.
[669.32 --> 670.40]  It's not about the fat arrow.
[670.52 --> 677.14]  It's about the semantics of how the function kind of exists and how it can change and what contexts it can run in.
[677.34 --> 683.76]  And it's taking away the foot gun of this changing out from under you, I think is the goal.
[683.76 --> 692.56]  So transitioning a little bit, like we're talking about all these features and I assume that we're talking about using them.
[693.00 --> 695.76]  Actually, my assumption is that we're talking about using them without a compiler.
[695.98 --> 698.10]  And I think that may not be your assumption.
[699.68 --> 705.62]  I'm wondering, like, so where can you where do you have to have a compiler down to ES5 to use this stuff right now?
[706.00 --> 711.56]  Like where like like are there IoT devices that have older VH that we have to worry about?
[711.56 --> 717.08]  Are there like which browsers like still don't support this kind of garbage?
[717.30 --> 719.54]  I mean, we're not supporting IE6 anymore, right?
[719.64 --> 720.54]  Like we're done with that.
[720.64 --> 721.56]  That conversation is over.
[721.56 --> 726.96]  So like IE9 doesn't, IE1011 get into some of the territory, but still are missing quite a bit.
[727.30 --> 732.92]  I think the problem is that, and Babbel's perfectly capable of doing this.
[732.92 --> 739.38]  It's just somewhat uninteresting to try to solve unless there's a performance problem.
[739.76 --> 747.36]  But if you think about your application, there's probably, let's say you're using 10 new ES star features.
[747.36 --> 758.48]  And one of them is like object spreads, which is like totally going to get in the language, but isn't in any browsers or node or anything like that.
[758.54 --> 760.82]  It's just like an obvious thing that we're going to do.
[760.92 --> 767.62]  And it's really useful to be able to, much like an argument spread or an array spread, you can do the same thing into an object.
[767.84 --> 772.86]  It kind of like finally solves the jQuery extend thing.
[772.86 --> 779.26]  So does object assign, but the problem is that you're already compiling with Babbel at that point.
[779.88 --> 782.70]  And so you're saying like, well, I want all these features in Babbel.
[783.04 --> 787.48]  And you could just say, well, I just want object spreads and I know the rest will.
[787.80 --> 791.64]  But at the point where you pull in a compiler, you're like, well, I might as well just go down to ES5.
[791.92 --> 793.28]  And I think that's the common way.
[793.34 --> 800.70]  It's just let me pull in all of everything that I know I need to compile to because I want to just work everywhere.
[800.70 --> 807.26]  And then people don't think about it too much past there because there isn't too much of a hit for many things.
[807.64 --> 809.68]  This isn't my thinking at all, though.
[809.98 --> 817.42]  And like, I don't know if Rachel feels similar to this, but like I don't use a compiler like ever for like down to a different language.
[817.62 --> 820.06]  And so like I only use browsers that support this.
[820.10 --> 823.82]  And like if it's a feature that isn't widely available, like I just don't use that feature.
[824.00 --> 824.36]  Same.
[824.64 --> 825.24]  I don't.
[825.32 --> 825.56]  Yeah.
[825.94 --> 827.68]  I think you guys are definitely in the minority.
[827.68 --> 831.34]  I don't think like that seems a little nuts to me.
[831.48 --> 837.22]  Like I really enjoy like line numbers and like just like a lot of the simplicity of not having it.
[837.96 --> 839.16]  Well, yes, yes, yes.
[839.68 --> 841.30]  Provided that you have all that tool properly.
[841.52 --> 843.00]  And it can be kind of a pain.
[843.14 --> 846.34]  I mean, like, look, if you're going to use Babel, then you're already in this boat.
[846.42 --> 848.66]  Or sorry, if you're going to use like React, you're already in this boat.
[848.98 --> 849.12]  Right.
[849.42 --> 855.70]  So there's enough people like using frameworks or other upper level tools where the compiler is just part of that tool chain already.
[855.70 --> 861.40]  But like I'm certainly not going to add Babel to my Node project in order to use object spread.
[861.56 --> 862.90]  Like that's not going to be that.
[863.06 --> 864.68]  That's just like I don't understand that thinking.
[864.82 --> 866.44]  And I don't think that a lot of people do that.
[866.72 --> 868.56]  I think a lot of people do that.
[868.74 --> 878.58]  I think it's pretty common these days to just start your project writing in the new thing, even if it's compatible with like the latest browsers or the latest whatever.
[878.98 --> 880.16]  Your pure Node module?
[880.34 --> 883.64]  Your pure Node module, you're going to like already have a compiler.
[883.64 --> 891.72]  I think Node is a little bit less this way because there are different norms there.
[892.38 --> 897.32]  But I think even in those cases, it's somewhat common to see.
[897.80 --> 898.18]  Yeah, sure.
[898.76 --> 903.20]  Like I wonder how many IoT projects Rachel has seen where they're compiling things with Babel.
[904.58 --> 906.76]  Not many, that's for sure.
[906.76 --> 917.92]  Yeah, I mean, I think IoT projects in the grand scheme of the amount of JavaScript that's being written are a small percentage.
[918.40 --> 920.92]  And that doesn't make them unimportant or anything like that.
[921.00 --> 927.56]  I'm just saying that I think the average JavaScript developer these days is working in a framework.
[927.56 --> 935.28]  And those frameworks somewhat already introduce enough compile steps to where it's just a non-issue to add this.
[935.36 --> 946.46]  So if you're working in Vue or you're working in React or you're working in Ember or you're working in Angular or you're working in any of these things, you have a Babel-like compiler already in your stack.
[946.46 --> 951.28]  And so adding object spreads is just like a decision you can make or not.
[952.10 --> 958.40]  So I feel like the most of the features that I have used and interacted with would have been like things that we touched on already.
[958.60 --> 965.52]  You know, cons, let, arrow functions, some of the way that they're doing class definitions and stuff like that.
[965.84 --> 969.24]  I guess this is about going to be the same thing that Michael was just about to ask.
[969.30 --> 971.94]  Are there any like features that you aren't using?
[971.94 --> 979.34]  Like which ones do you two think are the ones that people aren't really like, you know, fully embracing or trying out yet?
[980.00 --> 982.24]  I mean, I guess there's two buckets there.
[983.32 --> 993.36]  Ones that people aren't trying out yet because they're bad and ones that people aren't trying out yet because they aren't fully aware of them or they aren't fully powerful or things like that.
[993.52 --> 996.24]  I guess there's things that go in both buckets.
[996.24 --> 1005.40]  I mean, a lot of the stuff we use in Babel and the stuff that we're compiling down to is stuff that isn't even finished getting through ECMA and will change.
[1005.60 --> 1007.48]  Like modules is something that everyone uses.
[1007.66 --> 1014.46]  And like a lot of the semantics of how modules load like haven't been known for a really long time.
[1014.46 --> 1033.84]  And that's kind of the driving force behind the problem with getting proper modules into Node specifically because we've been doing it slightly wrong for so long because we kind of just wanted to compile ahead of time that now there's a clash in the semantics of how it should really work.
[1033.96 --> 1038.12]  And we're going to have to kind of work around that problem for a little while.
[1038.12 --> 1047.86]  Yeah, I mean, without getting the specifics there, there's actually a particular point where the spec sort of implies but does not define how things are supposed to work.
[1048.40 --> 1051.12]  And Babel made a decision about how they work at one point.
[1051.94 --> 1054.48]  And we're not going to be able to support that.
[1054.58 --> 1061.60]  And noted, in fact, the spec committee said that we should not do that and go that route because of some of the other tradeoffs that it would have to make.
[1061.60 --> 1068.52]  So, yeah, there's just there's stuff that until they're, you know, that one's even out like that one is actually in the spec.
[1068.64 --> 1073.98]  We just haven't had enough implementations to know what some of these like really, really nitty gritty details are.
[1075.44 --> 1076.50]  So, yeah, yeah.
[1076.56 --> 1082.94]  I mean, like you're you're you're by definition kind of on the bleeding edge if you're using features that aren't even actually in the browser yet.
[1084.20 --> 1085.52]  Modules are in the browser now, though.
[1086.68 --> 1087.70]  In one browser.
[1087.86 --> 1088.02]  Yeah.
[1090.22 --> 1090.86]  Pretty cool.
[1091.60 --> 1091.78]  Yeah.
[1092.00 --> 1094.22]  So what features are you staying away from, though?
[1094.32 --> 1095.50]  Like actually staying away from?
[1096.18 --> 1097.32]  The ones that I don't need.
[1099.56 --> 1102.40]  I think proxies are a terrible idea and that nobody should use them.
[1102.72 --> 1104.76]  They're just a performance bottleneck.
[1105.72 --> 1108.94]  Proxies were a really good idea for like a hot second.
[1108.94 --> 1114.32]  It seemed like a really solid solution to a thing that everyone was trying to solve at the time.
[1115.00 --> 1120.60]  And then, like, we found different ways to we found better ways to solve those user land problems.
[1120.60 --> 1125.22]  And then proxies became this thing that made a lot less sense.
[1126.04 --> 1129.50]  Namely, like the get set type problems.
[1129.72 --> 1133.80]  Like the way that Ember used to work where you have to do dot get and dot set.
[1133.80 --> 1145.24]  Like there was a world where proxies in the future could do more getter setter type stuff to where you could just say, you know, like my object dot foo equals five.
[1145.24 --> 1151.24]  And then that would be the same as saying my object set foo five or whatever.
[1151.24 --> 1157.28]  It would happen to do like it would need to do that because we need to run functions when things change in order to re-render.
[1157.28 --> 1169.96]  But now with like virtual doms and all that kind of stuff, like the community moved on to different techniques for solving that problem that are a little less magic.
[1170.72 --> 1172.52]  So I think proxies kind of fell.
[1172.96 --> 1177.14]  There are certainly like use cases, but I think they're pretty small.
[1177.14 --> 1183.22]  So generally, if you're using proxies, you're hacking the crap out of a closed library these days.
[1183.22 --> 1192.90]  Yeah, I remember similar features are in Python metaclasses and the guidance for metaclasses is don't use metaclasses.
[1195.68 --> 1197.52]  Other things I'm trying to think.
[1197.76 --> 1202.54]  There are definitely like proposals that I think it's less about.
[1202.74 --> 1204.60]  I'll use anything that's kind of in the language.
[1204.84 --> 1212.98]  Like they're pretty conservative, I think, about by the time it gets in the language, everyone's already been using it for so long that it's not even.
[1213.22 --> 1214.66]  That cool.
[1215.54 --> 1222.30]  But there are definitely things that are, you know, level two in the spec that I don't think are ever going to make it.
[1222.50 --> 1229.74]  Things like you could turn on stuff for like immutable types or even like one thing I don't use is decorators.
[1230.42 --> 1234.70]  I am skeptical that decorators are going to go the distance.
[1234.96 --> 1239.06]  And so I've been avoiding decorators.
[1239.30 --> 1240.60]  I don't have any data.
[1240.60 --> 1243.46]  I'm just waiting till they're like more of a sure thing, I guess.
[1244.02 --> 1246.86]  I used them when I was a Python programmer.
[1247.20 --> 1250.88]  And my general feeling is that they complicate more than they simplify.
[1251.66 --> 1258.48]  Yeah, there are some cases where they're like, I think the authentication case for decorators is so pretty all the time.
[1258.48 --> 1267.70]  It's just like this is an authenticated function and just like magically makes off something that makes sense like on a per function basis.
[1268.00 --> 1272.96]  And so like that's such a cool use case for decorators that it makes you want to use them a little bit more.
[1273.16 --> 1275.76]  But I think they have a place.
[1275.90 --> 1278.04]  And I know the Ember community uses them a little bit.
[1278.22 --> 1279.82]  Like there are also people in the React community.
[1280.82 --> 1285.76]  Ember concurrent uses decorators to do some of their stuff.
[1285.76 --> 1288.12]  And I think that it's a decent use case for it.
[1288.12 --> 1295.44]  But in general, I haven't seen a huge need for them, even though I'd probably use them once they made it into the language.
[1295.96 --> 1299.78]  Once they became more of a first class supported thing by the libraries I was using.
[1300.44 --> 1300.70]  I don't know.
[1300.90 --> 1303.70]  I'm more on the functional programming side of things.
[1303.88 --> 1307.32]  And so I just don't like encouraging people to write more classes.
[1307.32 --> 1307.96]  Sure.
[1308.40 --> 1311.56]  I think, I mean, that's a different conversation.
[1311.88 --> 1319.64]  But there are kind of two properties that I think the, I'm pretty happy with the React worlds.
[1320.42 --> 1324.60]  There are function components and some people are very big into that.
[1324.80 --> 1328.30]  But I actually don't mind the class components.
[1328.30 --> 1335.82]  But then all functions that are a part of it are like pure functions and like that kind of stuff.
[1335.92 --> 1344.20]  Kind of a mix of some of the better parts of each of the patterns to where you don't have crazy side effects and you don't have these different things.
[1345.56 --> 1354.54]  But then your kind of view layer is a little more readable than just, you know, a function that calls a function that sends half of its arguments to another function.
[1354.54 --> 1356.96]  So, I don't know.
[1357.04 --> 1358.20]  I think there's middle ground there.
[1358.32 --> 1358.88]  That's nice.
[1360.14 --> 1360.42]  Yeah.
[1360.64 --> 1363.24]  I think that we've hit a nice little spot here.
[1364.20 --> 1366.32]  I think we can take a short break.
[1366.92 --> 1370.04]  When we come back, we're going to get into Create React App.
[1371.74 --> 1377.62]  First sponsor of the show today is our friends at Sentry, helping you to find and fix your errors in your applications.
[1378.22 --> 1380.54]  You can start tracking your errors today totally free.
[1380.54 --> 1386.16]  They support React, Angular, Ember, Vue, Backbone, and no free marks like Express and Koa.
[1386.44 --> 1390.40]  You can view actual code and stack traces, including support for source maps.
[1390.86 --> 1393.66]  See the errors URL, parameters, and session information.
[1394.20 --> 1397.12]  And even prompt your users for feedback when you have front-end errors.
[1397.46 --> 1399.94]  Head to jsparty.fm slash Sentry.
[1400.14 --> 1401.78]  Start tracking your errors for free today.
[1402.14 --> 1403.06]  No credit card required.
[1403.32 --> 1404.62]  Get off the ground with their free plan.
[1404.94 --> 1407.48]  And when you're ready to expand your usage, simply pay as you go.
[1407.48 --> 1410.86]  So, once again, jsparty.fm slash Sentry.
[1411.04 --> 1412.08]  And now back to the show.
[1414.18 --> 1418.98]  We're going to get into some new features that just landed in Create React App.
[1419.40 --> 1421.60]  It actually seems like a pretty substantial change.
[1422.12 --> 1422.76]  We've talked about Create React.
[1422.76 --> 1423.24]  1.0.
[1423.58 --> 1424.12]  Yeah, yeah.
[1424.18 --> 1427.28]  We've talked about Create React App on the show before.
[1427.54 --> 1434.54]  But Alex, why don't you give us a little bit of that backstory and a little bit about this in less than 12 minutes.
[1434.84 --> 1435.28]  How about that?
[1435.28 --> 1436.40]  In less than 12 minutes.
[1436.40 --> 1437.14]  That's tough.
[1437.38 --> 1438.72]  That's an Alex problem.
[1439.42 --> 1439.64]  All right.
[1439.86 --> 1443.32]  Create React App is very similar to Ember CLI.
[1443.44 --> 1450.96]  If you've ever used Ember, I think Angular has its own CLI tool as well that I don't know the name of.
[1450.96 --> 1461.08]  But pretty much the goal of Create React App is to kind of manage all of the things that Michael's always complaining about for you.
[1461.26 --> 1462.56]  That way you don't have to care about them.
[1462.56 --> 1474.02]  So if you want to color completely in the lines of the suggested React world set of tools.
[1474.48 --> 1475.92]  And Webpack for that matter.
[1475.92 --> 1477.56]  Well, yeah.
[1477.56 --> 1482.32]  It's included in the suggested React world set of tools.
[1483.20 --> 1485.24]  Then you can use Create React App.
[1485.32 --> 1489.84]  And the idea is that you can say, create React App to do.
[1489.84 --> 1496.26]  And then you have a React app for to do's that automatically compiles your ES6.
[1496.26 --> 1509.46]  has a way to do CSS in JavaScript and does error handling and building and all sorts of the different things that you would normally have to set up manually one by one.
[1509.60 --> 1511.88]  All is this one big kind of package.
[1511.98 --> 1513.86]  It's kind of a template to get started with a project.
[1513.86 --> 1517.12]  But one thing that is important.
[1517.34 --> 1518.30]  And the history is interesting.
[1518.46 --> 1523.28]  It was like a hack weekend project because React was one of.
[1523.52 --> 1530.56]  A lot of the feedback React got was that there's no kind of baseline of guaranteed supported tools that work together.
[1530.96 --> 1534.34]  And this is kind of like an answer to say like, well, this stuff all works together.
[1536.24 --> 1539.34]  So it was kind of like a hackathon one day thing.
[1539.42 --> 1543.18]  And then it's grown up a lot since then.
[1543.18 --> 1545.18]  And this is the 1.0 release.
[1545.54 --> 1548.84]  So it's been in use by a lot of people already.
[1549.92 --> 1551.88]  But now it's gone 1.0.
[1552.18 --> 1556.24]  And so the idea is you have to stay within there.
[1558.40 --> 1560.44]  So even like it configures your ESLint.
[1560.52 --> 1561.46]  It configures your Webpack.
[1561.54 --> 1562.70]  It configures your CSS.
[1562.96 --> 1564.12]  It configures your Babel.
[1564.50 --> 1565.42]  All those different things.
[1565.86 --> 1571.94]  And that configuration is even hidden from you because if you change it, then it's hard for them to make the assumptions that they can make.
[1571.94 --> 1580.64]  And so you can either choose to use Create React app as this thing that you can constantly update because you're staying within the coloring lines.
[1580.64 --> 1584.54]  Or you can use Create React app to like generate a thing.
[1584.54 --> 1587.36]  And then you can do what they call ejecting.
[1587.56 --> 1590.84]  And so you can eject from Create React app as soon as you create your app.
[1591.00 --> 1595.98]  It'll pull all that configuration into kind of your core directory or where it would go if you wrote it yourself.
[1596.26 --> 1598.34]  And then you can just edit it and all that stuff.
[1598.34 --> 1605.56]  But you can no longer kind of pull updates from Create React app in order to like get automatic updates if that kind of makes sense.
[1607.58 --> 1609.96]  So does that make sense as kind of a background?
[1611.38 --> 1612.70]  Makes sense to me.
[1613.16 --> 1613.38]  Cool.
[1613.38 --> 1626.38]  So like in general, I found that like with the things at work that are difficult to like do, if I want to do a Create React app, I have to eject pretty fast.
[1627.84 --> 1632.44]  Because we need to change one ESLint thing in order to work with our build servers.
[1632.70 --> 1633.62]  And it's like, oh, that kind of stinks.
[1634.16 --> 1636.06]  And that's like part of the deal.
[1636.20 --> 1638.48]  It's like if you can't do it, then you just don't get the updates.
[1638.48 --> 1641.28]  And sometimes that is not a problem.
[1641.40 --> 1650.30]  In general, like I haven't kind of missed, I haven't like paid enough attention to Create React app to get mad when they have an update and my thing can update with them.
[1650.64 --> 1657.96]  But this release would be maybe a good example of something that's like, well, if you stayed in the coloring lines, this would be a really nifty change.
[1658.20 --> 1661.92]  So we can go through the changes in 1.0 if you all want.
[1662.46 --> 1663.00]  Sure, sure.
[1663.00 --> 1671.92]  My first question is that it says something on the order of like, okay, you can use import and export semantics now without actually compiling down to CommonJS.
[1672.14 --> 1673.68]  But it's compiling down to something, right?
[1673.80 --> 1674.68]  Just to get into the browser.
[1674.86 --> 1677.12]  It's not relying on the browser's support yet.
[1677.82 --> 1678.70]  So it could.
[1679.50 --> 1684.08]  So the idea is, this is, I think you skipped ahead.
[1684.56 --> 1689.34]  Webpack 2 is a part of Create React app now.
[1689.48 --> 1691.02]  So it used to be based on Webpack 1.
[1691.02 --> 1698.08]  When most people are on Webpack 1, Webpack 2 is pretty new and it's a pretty, it's a larger departure than a lot of 2.0s would be.
[1698.20 --> 1701.70]  And so it's going to take some work to get people moved over.
[1701.80 --> 1713.06]  But one of the features of Webpack 2 is that it supports imports and exports natively, like at all, as part of its parser.
[1713.06 --> 1723.24]  And so before, if you gave Webpack 2 imports and exports ES6 modules and you weren't using Babel, nothing would happen.
[1723.40 --> 1726.42]  Like it would break because it wouldn't understand that.
[1726.52 --> 1734.80]  So what the steps would be, it would be compile with Babel to, you know, require statements and then pass it to Webpack.
[1734.80 --> 1735.98]  Oh, okay.
[1735.98 --> 1738.08]  And then Webpack could understand the require statements.
[1738.48 --> 1747.82]  But there are some features in ES6 modules like static analysis and stuff like that that are more guaranteed in ES6 modules.
[1747.94 --> 1754.30]  So they were able to say like, all right, we no longer care if you pass this require or these things.
[1754.30 --> 1762.26]  And so you may skip the Babel step in order to pass imports and exports rather than first compiling down to Webpack.
[1762.38 --> 1774.34]  And then it can use like the proper static analysis that is guaranteed as part of ES6 modules in order to do better things with regards to bundle size and tree shaking and dynamic loading and all that kind of stuff.
[1774.34 --> 1788.40]  And so it's more of a what does Webpack understand rather than you still may or you still more than likely at the end will compile it down to require statements that like from whatever library in order to to bundle it all together.
[1788.48 --> 1789.98]  It's like part of what Webpack does.
[1790.18 --> 1792.92]  But it natively understands imports and exports now.
[1792.92 --> 1822.10]  And that is now included automatically in Create React App, which means that if you were coloring in the lines before, all you have to do is update your Create React App kind of instance, the version, and you were automatically upgraded from Webpack 1 to Webpack 2, which is kind of the amazing thing is that like, whoa, that was a pretty big upgrade from Webpack 1 to 2 that a lot of people are going to spend a lot of time rewriting their Webpack configurations.
[1822.10 --> 1824.74]  And it was free because you stay within the lines.
[1824.96 --> 1827.86]  Someone else like worked on the hard parts of that, which is cool.
[1828.06 --> 1828.42]  It's nifty.
[1828.74 --> 1829.22]  It's a good idea.
[1829.96 --> 1830.86]  Does that make sense, Michael?
[1831.44 --> 1837.28]  Yeah, it's just it's yeah, I'm just constantly sort of reframing how to think about Webpack.
[1837.42 --> 1843.02]  I think that the longest time I think everybody kind of thought of it as like this compile tool.
[1843.26 --> 1846.72]  And but in actuality, it's more like a platform onto itself.
[1846.72 --> 1855.12]  Like it has a lot of primitives like a like its own module system and with with more types and things like that than the node does.
[1856.20 --> 1859.40]  So, yeah, I'm just kind of reframing how to think about that.
[1859.94 --> 1861.24]  Yeah, it is an interesting tool.
[1861.54 --> 1865.96]  Like it kind of crosses over a few different boundaries of old tools that we've had.
[1866.28 --> 1871.28]  And so if you think about it as a grunt type thing, you'll think about it as a grunt type thing.
[1871.34 --> 1874.24]  If you think about it as a babble type thing, you'll think about it as a babble type thing.
[1874.24 --> 1879.10]  But like it kind of is more of a piece of glue.
[1879.68 --> 1886.58]  But then it still needs to understand things like ES6 modules natively in order to do tree shaking and things like that.
[1886.98 --> 1889.80]  So it's an interesting project.
[1890.46 --> 1896.44]  So I was going through and like reading the whole what's new in the React or create React app article.
[1897.10 --> 1898.40]  And a bunch of it made sense to me.
[1898.44 --> 1903.18]  But there's some things in here that I've like never heard of and I have no idea what they are.
[1903.18 --> 1906.18]  So one of those being just 20.
[1907.50 --> 1909.12]  Yeah, it's a React specific thing.
[1909.26 --> 1912.14]  Just is the test running framework for React.
[1912.86 --> 1919.52]  So it's just they've upgraded just, I guess, two versions that used to be just 18 or something like that.
[1919.88 --> 1921.52]  There are like testing.
[1921.52 --> 1926.48]  Testing is we should do a whole episode on testing sometime in the future.
[1926.48 --> 1936.76]  But one of the hardest parts about testing in the past, if you guys have done testing like at scale for a web app, which may not be the case.
[1936.76 --> 1949.74]  But like functional tests are so sad where you need to like pop open a browser with XVFB and then send web driver commands to it in order to try to click around.
[1950.14 --> 1951.22]  Like they're so slow.
[1951.36 --> 1956.36]  They have so many like false positives and timeouts and problems.
[1956.70 --> 1959.78]  And Chrome automatically updates and breaks all your tests.
[1959.78 --> 1962.62]  And web driver implementations are shady between the different.
[1963.04 --> 1973.68]  But like there's so many problems with that that there's this new world of writing like unit tests where you can kind of mount components directly into memory.
[1973.68 --> 1983.42]  And then like kind of write functional style tests as something that doesn't need a browser at all.
[1983.98 --> 1990.42]  And it's a little different than running like JSDOM, which is like essentially providing it a subset of a browser.
[1990.70 --> 2000.52]  And you can do a lot of the tests that you used to do very slowly, very non-deterministically with browsers as a unit test where you say like,
[2000.52 --> 2007.58]  well, if this function, like if a click is applied here and then this, the DOM should then reflect these different things.
[2007.80 --> 2013.48]  And you can test all that stuff like on a per component basis very quickly without spinning up a whole browser.
[2013.90 --> 2020.34]  So JEST is good at helping you manage those types of things.
[2020.90 --> 2029.24]  In general, if you're writing React code, there's a pretty, JEST would be your default choice, even if it's not.
[2029.24 --> 2034.76]  I doubt it has like more than 70% saturation, but that's pretty good.
[2034.84 --> 2039.48]  There's still quite a few other options that people use, Ava and a few different things.
[2039.90 --> 2047.06]  JEST is, I think, coming around and winning the default choice for testing because Facebook wrote it and supports it and stuff.
[2047.32 --> 2049.58]  So is this one just bundled with the new release?
[2050.12 --> 2052.18]  Yeah, so JEST used to be bundled.
[2052.36 --> 2053.38]  It's just a new version.
[2053.38 --> 2059.80]  And so there are new things that the highlights include immersive watch mode, better snapshot format.
[2059.92 --> 2065.62]  So snapshots are where you can say like, once this is rendered with this data, the HTML should look exactly like X.
[2066.12 --> 2067.26]  And then it can test.
[2067.36 --> 2071.94]  So it's kind of like whenever people do screenshots with like CSS frameworks and stuff like that.
[2071.94 --> 2072.72]  Yeah, yeah, yeah.
[2072.74 --> 2073.86]  It needs to be pixel perfect.
[2073.98 --> 2077.20]  You can do the same thing with the HTML output of your components.
[2077.20 --> 2082.64]  You can just say snapshot, like I don't need to write down what it should look like, but I know this is good snapshot.
[2082.84 --> 2085.34]  It shouldn't change unless I change that module.
[2085.76 --> 2090.54]  And so if some dependency accidentally starts changing your HTML, you'll get a test failure.
[2092.24 --> 2097.18]  And then just like the output and stuff, APIs for new stuff for React.
[2097.44 --> 2102.30]  So you also get automatic coverage reporting, which is good.
[2102.30 --> 2102.78]  Cool.
[2102.78 --> 2103.10]  Cool.
[2103.20 --> 2107.24]  So it's kind of just like enforcing good practices on you anyway.
[2107.72 --> 2107.96]  Yeah.
[2108.08 --> 2127.80]  And whenever you do a create React app, it'll start you up with a test directory with a test already written and imported and building and all that kind of stuff to where it's like really as soon as you write your thing, it's a very fast and easy example on how to start writing tests for your thing without needing to learn about how to configure JEST.
[2128.32 --> 2129.04]  That's awesome.
[2129.82 --> 2130.26]  Yeah.
[2130.26 --> 2150.82]  One tough thing for writing web apps is if you want to write tests in the same JavaScript that you write your components and stuff in, but if you're using Babel and Webpack and stuff in order to compile everything down, then you start needing to like watch and compile your test directory, which is cool.
[2150.82 --> 2161.00]  But then like while you're writing your app, you're spending an additional, you know, three seconds every time you do a save compiling your thousands of tests that you've written.
[2161.68 --> 2170.62]  And so like there needs to be good configuration on whether you're kind of in a mode where tests run or get compiled or whether it's important for them to get recompiled.
[2170.62 --> 2183.28]  And most of that's handled to where you're not doing unnecessary work as you're working and then your tests can still be in like new, cool, good ES6-y, babbly stuff that you write your other components in.
[2183.42 --> 2188.40]  You don't have to switch context to write like older school JavaScript for your tests.
[2189.10 --> 2189.30]  Great.
[2189.30 --> 2192.42]  So moving off of testing, because I think it's boring.
[2192.80 --> 2193.72]  No, I'm just kidding.
[2194.76 --> 2195.20]  Fair.
[2195.20 --> 2195.24]  Fair.
[2196.94 --> 2210.78]  So I see that one of the things that it also does is it just it adds a service worker like automatically and has an offline caching strategy, which like I think is great that service worker support and PWAs are like landing in frameworks like this.
[2211.02 --> 2217.26]  I'm terrified at the idea of the framework just like implementing a caching strategy that I don't understand.
[2218.48 --> 2218.96]  Sure.
[2218.96 --> 2221.52]  Because I've spent so much time fighting caches.
[2221.96 --> 2224.00]  Like, yeah, it's just kind of worrisome.
[2224.00 --> 2231.86]  So I put a service worker on TXJS early on the TXJS website in 2015, I think.
[2232.60 --> 2247.18]  And if someone had hit it between like 2 a.m. and 3 a.m. a week before the conference, then they would still have be being served that version of the website for the rest of their lives unless they like went in and cleared the service worker.
[2247.18 --> 2257.04]  So like there's definitely some danger to where like you can get yourself in a place where you accidentally cache everything and there's no way to break out.
[2257.18 --> 2258.26]  And that can be unfortunate.
[2258.26 --> 2262.26]  But I haven't dug deep into their service worker implementation.
[2263.32 --> 2267.66]  But my gut is that if you don't do anything weird, it should be fine.
[2267.70 --> 2269.82]  And if you do something weird, sorry.
[2269.82 --> 2279.16]  Yeah, my gut is that it's fine for normal stuff and you'll probably need to turn it off for crazier stuff.
[2279.30 --> 2290.50]  Or if you want like something like it's probably very baseline and very lazy in the sense that it isn't going to do too much because it can't assume as much.
[2290.50 --> 2294.58]  But if you think about just like a caching strategy of like have we seen this before?
[2295.16 --> 2302.30]  Like if you think about a caching strategy, if we've seen it before, return the old one and then always go grab the new one.
[2302.62 --> 2309.34]  And if there is a new one that's different than the old one, go ahead and also send up another event for new data.
[2309.34 --> 2321.32]  And if that's kind of built into the idea of how you render things, which a lot of the React stuff is like as things change, like it automatically updates, then it can kind of be a good default strategy.
[2322.12 --> 2322.74]  Oh, yeah.
[2322.80 --> 2323.88]  I hadn't really thought about that.
[2324.04 --> 2326.94]  Like React has a lot of understanding about the individual components.
[2326.94 --> 2329.98]  So it knows if re-renders need to happen when the backend updates.
[2330.10 --> 2331.04]  That's interesting.
[2331.90 --> 2338.66]  Yeah, there's some nice synchronicity in some of that stuff, I think.
[2338.66 --> 2342.30]  But yeah, it's not going to be a silver bullet, but I think it's pretty good.
[2342.62 --> 2352.94]  Something, Ember CLI doesn't have service worker, but they have, by default, they serve, like whenever you do Ember serve, a, what is it?
[2353.08 --> 2363.40]  A CSP, a content security policy, which I think is a really cool default to have just to like make that a more widely used thing.
[2363.40 --> 2370.40]  Just like beat by default, XSS is harder in Ember apps than it is in other apps because they do CSP.
[2371.16 --> 2387.98]  And so I really like these toolkit style CLI helper things, doing things like solid generic defaults that maybe aren't the best version of them, but maybe get people thinking about service workers or get people thinking about CSP.
[2387.98 --> 2390.44]  And we'll work in all the simple cases as well.
[2391.56 --> 2392.04]  Interesting.
[2392.46 --> 2393.32]  Very interesting.
[2394.46 --> 2396.74]  You sound skeptical, but I know.
[2396.86 --> 2397.14]  No, no, no.
[2397.22 --> 2404.28]  I think just in general, like on the surface, this looks like a boilerplate generator.
[2404.78 --> 2408.34]  It's actually very much not just a boilerplate generator.
[2408.72 --> 2408.84]  Yeah.
[2408.84 --> 2409.78]  I mean, it's like that too.
[2410.54 --> 2410.84]  Yeah.
[2411.06 --> 2411.58]  Yeah, yeah, yeah.
[2411.68 --> 2412.12]  I mean, obviously.
[2412.12 --> 2416.06]  Like a living boilerplate generator, kind of.
[2416.06 --> 2416.18]  Yeah.
[2416.98 --> 2417.42]  Yeah.
[2418.16 --> 2418.60]  Yeah.
[2418.68 --> 2419.84]  That's intense, though.
[2419.92 --> 2423.92]  Well, it's a boilerplate generator, but it keeps on helping.
[2424.22 --> 2427.32]  Like it just helps you continue on developing the app.
[2427.36 --> 2430.74]  It doesn't just like run once and then you like don't use it.
[2430.76 --> 2431.02]  Right.
[2431.08 --> 2433.90]  Because it helps you put together all of the tools that you need for it.
[2434.28 --> 2434.54]  Right.
[2435.20 --> 2435.60]  Yeah.
[2435.60 --> 2442.40]  I mean, it's like all of this stuff feels like it's a great grandchild of Rails where
[2442.40 --> 2446.68]  Rails would, there's a word for it.
[2447.22 --> 2448.20]  It would generate code.
[2449.16 --> 2451.80]  Like you would just say Rails new controller.
[2452.22 --> 2452.66]  Scaffolding.
[2452.84 --> 2453.56]  Yeah, scaffolding.
[2453.78 --> 2454.70]  That's the word.
[2455.14 --> 2457.26]  And it definitely feels kind of like scaffolding.
[2457.26 --> 2460.88]  And there's a bit of scaffolding like in the initial like create React app.
[2461.48 --> 2467.00]  But I think it focuses less on generating code for you and more about providing tools
[2467.00 --> 2470.48]  and examples and kind of a baseline for you to build on.
[2470.64 --> 2475.92]  And then allowing like the kind of one of the things of scaffolding is like once it generates
[2475.92 --> 2481.00]  that code, that code is is stuck there forever in that format.
[2481.00 --> 2487.36]  Whereas I think more of the strategy with create React app is that hopefully it scaffolds little
[2487.36 --> 2492.76]  enough to where it can update those things that it has generated like on the fly.
[2493.36 --> 2501.72]  I think the last thing that's interesting in the not Webpack, create React app 1.0 release
[2501.72 --> 2503.86]  is the code splitting stuff.
[2504.10 --> 2506.36]  And that's part of Webpack as well.
[2506.36 --> 2511.26]  But there's a standard that no one uses for dynamic imports.
[2511.50 --> 2515.10]  It mixes async await with import.
[2515.72 --> 2520.54]  And I hadn't looked into it much because there wasn't really a great place to use it.
[2520.58 --> 2522.28]  But it's like it's part of the standards track.
[2524.06 --> 2526.70]  And like I don't know where it is in that.
[2526.82 --> 2531.24]  But you can have an async function and then you can import something.
[2531.48 --> 2532.92]  You can do await import.
[2532.92 --> 2538.16]  And then that will automatically build into a separate like all the dependencies of the
[2538.16 --> 2544.12]  thing that you're asynchronously importing can be built into a separate bundle.
[2544.82 --> 2547.26]  Yeah, I think you're complicating it a little bit.
[2547.32 --> 2551.92]  Like it's a piece of syntax that allows you to with a function do the same thing you do
[2551.92 --> 2553.36]  with syntax for import.
[2553.56 --> 2553.72]  Right.
[2553.94 --> 2558.52]  So and the nice thing about that is that at some point in the future, which is like not
[2558.52 --> 2563.98]  part of the initial interpretation phase of the browser, you can say import this module.
[2564.88 --> 2568.04]  And then what you're saying is that like now we can actually use that for code splitting
[2568.04 --> 2571.78]  because you can say, oh, well, like these these little pieces that you don't necessarily
[2571.78 --> 2575.56]  need, we can now import dynamically using the same kind of module system.
[2575.68 --> 2575.74]  Right.
[2575.80 --> 2579.60]  I guess I was complicating it because it would be invalid syntax to just throw an import
[2579.60 --> 2580.86]  there.
[2580.86 --> 2582.90]  So it needs to be like supported syntax.
[2583.04 --> 2586.52]  It's not just like something you could do before, but people didn't know about it.
[2586.52 --> 2592.64]  I think is like awaiting an import is not like it needs to be statically analyzable or or
[2592.64 --> 2598.68]  at least be known to be a part of it that isn't statically analyzable because it doesn't
[2598.68 --> 2600.32]  need to be something, you know, something like that.
[2600.68 --> 2608.16]  And that's why I think it's part of the standards track to do asynchronous imports like like this.
[2608.16 --> 2614.36]  And so create react app supports this in order to do bundles, which is a huge part of like
[2614.36 --> 2616.88]  the PWA communities problem.
[2617.06 --> 2621.24]  Like if you follow Alex Russell or whatever, you'll you'll know that your JavaScript that
[2621.24 --> 2623.64]  you're serving by default is far too large.
[2624.64 --> 2630.38]  And so if you can do so, if you can turn on HTTP two and then do something like a handful
[2630.38 --> 2634.70]  of these asynchronous imports for large portions of your application.
[2634.70 --> 2640.86]  I think it could go a long way to like loading far less JavaScript on load, which is which
[2640.86 --> 2641.50]  is really nifty.
[2641.64 --> 2647.24]  I think this is such a good direction to like automatically for like give to people.
[2647.40 --> 2651.44]  I hope they use it in the baseline example that they generate, you know, that way people
[2651.44 --> 2651.86]  use it.
[2652.88 --> 2652.96]  Yeah.
[2653.06 --> 2657.42]  Sort of following on with your talk about scaffolding, it seems like the big difference between
[2657.42 --> 2661.76]  this and what Rails does is like you said, Rails will generate a lot of boilerplate code.
[2661.76 --> 2664.86]  This seems to generate a lot of configuration, right?
[2664.92 --> 2670.78]  Like we have like like the joke about Webpack is that like you you only write one Webpack
[2670.78 --> 2673.46]  configuration and then you copy paste it into every project.
[2673.68 --> 2675.48]  I mean, that's a make file joke, but yeah.
[2675.90 --> 2676.22]  Yeah.
[2676.32 --> 2676.46]  Yeah.
[2676.62 --> 2677.02]  Exactly.
[2677.72 --> 2677.92]  Right.
[2678.72 --> 2683.86]  But I think also like like you were saying, one of the things this does is really standardize,
[2683.96 --> 2689.02]  you know, what is the the proper path for writing a React app with all these different
[2689.02 --> 2689.56]  configurations.
[2689.56 --> 2695.06]  And so this allows you to sort of add features over time to that configuration without trying
[2695.06 --> 2699.20]  to get, you know, thousands and thousands of developers to update their, you know, this
[2699.20 --> 2700.88]  particular line in their Webpack config.
[2701.38 --> 2701.50]  Right.
[2701.98 --> 2703.34]  It's a noble cause.
[2703.50 --> 2707.76]  And other people are doing it like Ember CLI and stuff are doing this well as well.
[2707.84 --> 2716.36]  Like when you upgrade these like new world configuration CLI tools, you get instant improvements in
[2716.36 --> 2717.72]  your applications, which is cool.
[2717.72 --> 2722.74]  I really like like everything still works and now it's 20 percent faster.
[2723.00 --> 2729.94]  It's like whenever Ember did the Glimmer update, all you did was upgrade Ember CLI and suddenly
[2729.94 --> 2731.02]  everything was using Glimmer.
[2731.18 --> 2735.78]  It was all supported unless you're doing something weird, you know, and suddenly your website rendered
[2735.78 --> 2736.12]  faster.
[2736.22 --> 2738.04]  And I think that's a cool world.
[2738.04 --> 2745.88]  Like for I think that's a good goal for these well-used frameworks to to to go after.
[2746.50 --> 2747.26]  Yeah, definitely.
[2747.46 --> 2752.32]  One thing I can't wait to see is not compiling down to ES5 anymore, but compiling down to,
[2752.32 --> 2756.16]  you know, a set of features that are actually mostly supported because there's a lot of performance
[2756.16 --> 2760.10]  benefits to like arrow functions are faster than regular functions and in V8.
[2760.10 --> 2764.00]  And for the most part, you know, people that are working with compilers aren't getting those
[2764.00 --> 2765.20]  performance benefits right now.
[2765.28 --> 2765.34]  Yeah.
[2765.60 --> 2766.28]  You can choose.
[2766.40 --> 2771.46]  You can configure that not in create react app, but in a generic Babel config, you can
[2771.46 --> 2772.64]  say these are the things.
[2773.10 --> 2776.76]  This is the target set of features that I want to compile down to.
[2776.88 --> 2777.76]  So it's certainly possible.
[2777.76 --> 2780.00]  But I don't think many people go that far.
[2780.00 --> 2783.58]  Well, and also there's only one minifier that supports it as well.
[2783.74 --> 2787.76]  So and it's still under really active development.
[2788.00 --> 2790.18]  So that's one of the things that you kind of lose.
[2790.56 --> 2792.76]  Anyway, I think that we're about time for another break.
[2793.80 --> 2795.86]  I'm going to take a short little break here.
[2795.90 --> 2798.08]  And then when we come back, we're going to talk about the project of the week.
[2799.54 --> 2804.84]  If you're looking for trusted freelance talent, ready to join your team right now.
[2804.94 --> 2809.98]  I mean, like within the week, call up all my friends at TopTile, T-O-P-T-A-L.com.
[2810.42 --> 2815.12]  And as a listener of the show, you might actually be one of those developers or designers
[2815.12 --> 2820.40]  looking for awesome freelance, independent contractor type opportunities where you can
[2820.40 --> 2821.86]  still be a remote worker.
[2821.96 --> 2825.18]  You can still have the freedom you have right now, which means you can travel anywhere.
[2825.30 --> 2827.52]  You can be anywhere and do what you do.
[2827.96 --> 2828.80]  We love TopTile.
[2828.86 --> 2830.88]  They've been supporting this show for a very long time.
[2831.16 --> 2832.58]  They're really good friends of ours.
[2832.80 --> 2835.54]  If you want a personal introduction, I'd be glad to give that to you.
[2835.84 --> 2838.48]  Email me, Adam at changelaw.com.
[2838.48 --> 2840.58]  Otherwise, head to TopTile.com.
[2840.68 --> 2843.36]  That's T-O-P-T-A-L.com to learn more.
[2843.70 --> 2845.36]  Tell them Adam from changelaw sent you.
[2845.68 --> 2846.90]  And now back to the show.
[2846.90 --> 2852.10]  The project of the week this week is Electron.
[2852.92 --> 2854.88]  There's been so much stuff about Electron.
[2854.96 --> 2857.48]  I'm sure that we've talked about Electron apps on here.
[2858.22 --> 2861.00]  I know that the changelaw did like a whole episode as well.
[2861.00 --> 2870.80]  Just for some quick background, Electron is a way to build desktop applications for Mac, Windows, and Linux using Node.js and browser technologies.
[2871.24 --> 2875.84]  So if you can make a website and use Node.js, you can write an Electron app.
[2875.84 --> 2883.50]  And it was originally broken out of the Atom editor that GitHub was doing.
[2883.64 --> 2885.78]  It was initially called, I think, Atom Shell.
[2886.66 --> 2891.98]  And then Jessica Lord and some of the good people at GitHub moved it into its own project.
[2892.14 --> 2893.16]  And now it's really taken off.
[2893.16 --> 2904.02]  And some of the Electron apps that people might know of is like Hyper and Slack and something that we talked about recently, which is WebTorrent and stuff like that.
[2904.42 --> 2908.86]  Visual Studio Code, which is my current editor of choice as well.
[2910.34 --> 2919.64]  Yeah, it's one of the interesting things that I've seen about it is that I think a lot of people initially viewed it as like, oh, I can take my website and turn it into a desktop app.
[2919.74 --> 2921.42]  That's sort of what the Slack app does.
[2921.42 --> 2927.18]  Or, you know, I can write desktop apps, but it's a pain to do them cross-browser.
[2927.34 --> 2928.98]  So I will write them in this instead.
[2929.46 --> 2938.00]  But what I've seen lately are applications that I don't think would even exist if it wasn't for, you know, having unrestricted access to Node.js.
[2939.48 --> 2942.72]  And then just being able to put a browser front end on that.
[2942.90 --> 2945.10]  Like, just the size of the ecosystem is so amazing.
[2945.10 --> 2952.74]  You know, MongoDB has like a new DB admin thing that's like a desktop app with Electron.
[2953.16 --> 2958.28]  Voltra is like this new music app that is like way prettier and nicer than iTunes.
[2958.28 --> 2963.16]  And that is just, you know, because like they knew Node.js really well.
[2963.22 --> 2965.58]  They can really dig into the nitty-gritty there.
[2965.92 --> 2970.20]  And they need like a lot of the stuff that they're doing with data storage and syncing and stuff.
[2970.28 --> 2971.64]  They need that performance, that layer.
[2971.74 --> 2973.24]  They couldn't just do it as a pure web app.
[2974.52 --> 2975.94]  So it's awesome.
[2976.76 --> 2978.40]  Have you built anything with Electron?
[2978.40 --> 2981.02]  Yes, yes.
[2982.24 --> 2991.64]  I mean, I've gone through – I wrote a little kind of browser viewer on top of IPFS because I wanted to play around with IPFS.
[2991.82 --> 2994.06]  So I made like a little like drag and drop thing.
[2995.40 --> 3002.82]  I have – I'm about halfway done with like a desktop version of Roll Call that uses Electron as well.
[3003.24 --> 3006.32]  And then I pulled down and just worked with a couple projects.
[3006.32 --> 3011.84]  Like I dug into the Brave code at one time, which is also an Electron app.
[3013.16 --> 3015.22]  And – or it was back then.
[3015.28 --> 3016.84]  I think now they're on their fork of Electron.
[3018.12 --> 3021.96]  And there was another app that I can't remember that I sent a pull request to.
[3022.08 --> 3023.78]  And so I had to pull it down that way.
[3023.90 --> 3024.96]  And all of them have been great.
[3025.02 --> 3026.22]  I mean, I'm comfortable with Node.
[3027.64 --> 3031.44]  So it's a really kind of comfortable place to be to develop in.
[3031.88 --> 3032.44]  What about you?
[3032.50 --> 3035.36]  Yeah, I mean, I'm super comfortable with Node too.
[3035.36 --> 3041.78]  And Electron like has always been something that, you know, I have known existed as a thing.
[3042.44 --> 3051.66]  But like is there anything extra that people that already know how to build like web applications with Node would need to know in order to get up and running with Electron?
[3051.78 --> 3054.90]  Or does Electron kind of like just wrap around all that stuff?
[3054.90 --> 3057.32]  I mean, it wraps around all of it.
[3057.32 --> 3065.34]  But also, I think – like I don't think that we can underestimate like how much stuff there is in NPM right now.
[3065.42 --> 3066.40]  Like how many modules.
[3066.86 --> 3080.12]  And to make like a lot of web apps work, a ton of what you do is that you build these backend services that just, you know, talk to something that is like has less security around it and more of the Node ecosystem.
[3080.12 --> 3082.24]  And then you push that to the browser in some way.
[3083.24 --> 3095.54]  And I've seen a lot of people just get up and running so quickly on their ideas because they can just store directly on the file system and access every module in NPM and then put a web frontend on it and not have to spin up a backend service.
[3095.54 --> 3102.34]  Not have to deal with, you know, a frontend and a backend where they just like kind of have it all mashed together in this environment in Electron.
[3103.66 --> 3104.06]  Alex?
[3104.92 --> 3105.28]  Yeah?
[3105.28 --> 3106.94]  Have you made anything?
[3107.90 --> 3108.82]  In Atom?
[3108.90 --> 3109.10]  No.
[3110.44 --> 3130.34]  I – my experience with Atom or in Electron has been installing the Electron bin for like – actually, we used Electron in order to do screenshots for our CSS library visual diffs.
[3130.34 --> 3139.40]  Because it was easier to just run Electron cross-browser, render something, and then use the stuff to take a screenshot.
[3140.02 --> 3145.00]  And then not even reload pages, just inject the new components into the same page.
[3145.38 --> 3148.96]  And then you could take like a ton of screenshots all in a row and it ended up being really fast.
[3149.04 --> 3150.64]  I think there's an open source library that we have.
[3150.78 --> 3151.70]  I can find the leak.
[3151.70 --> 3155.00]  But yeah, so I used it for a pretty different thing.
[3155.28 --> 3160.46]  But yeah, like that may be an interesting use case of it.
[3160.56 --> 3167.62]  It's just like it's a cross-browser environment to run HTML in headlessly, which is kind of cool.
[3168.50 --> 3168.64]  Yeah.
[3169.00 --> 3178.86]  What was the thing that – this is going to be a horrible – it's going to showcase my horrible memory.
[3178.86 --> 3183.78]  What was the thing that Adobe had that was allowing you to make apps easier?
[3184.72 --> 3187.98]  It might have just been like in Macs or something.
[3188.10 --> 3189.94]  Does anyone know what I'm talking about?
[3190.46 --> 3196.22]  Yeah, they had an editor and then they had – yeah, the name of the stuff.
[3196.34 --> 3199.98]  But it was like kind of Dreamweaver 2000 or whatever.
[3200.56 --> 3201.00]  Well, no.
[3201.54 --> 3203.08]  Not Dreamweaver.
[3203.08 --> 3208.70]  It was one that actually let you get some kind of – obviously, I guess it's not as notable.
[3208.70 --> 3208.82]  Adobe Air?
[3209.50 --> 3210.88]  Yes, Adobe Air.
[3211.34 --> 3213.48]  Thank you, Corbin, you in the panel.
[3214.44 --> 3214.76]  Thanks.
[3215.92 --> 3216.84]  Okay, cool.
[3217.42 --> 3218.04]  Adobe Flex.
[3218.24 --> 3220.76]  And Flex, I think, is what it eventually became, right?
[3221.18 --> 3224.96]  Flex was the framework that you wrote in.
[3225.60 --> 3229.28]  And you wrote that Air was the container that it would run in.
[3229.82 --> 3230.60]  Okay, okay.
[3230.60 --> 3232.74]  Hold on, the cops are coming again.
[3234.86 --> 3236.26]  It was all Flash-based.
[3236.52 --> 3237.58]  Action script.
[3238.64 --> 3242.24]  The cops are coming to arrest Rachel for talking about Adobe Flash.
[3244.44 --> 3245.26]  Excuse me now.
[3245.28 --> 3246.10]  Oh, okay, cool.
[3246.26 --> 3249.88]  So, I mean, I remember when that came out and I was like, whoa, this is rad.
[3249.88 --> 3258.66]  And, I mean, Electron seems like – I know that people are talking about it a lot, but I feel like people should be talking about it more.
[3258.66 --> 3272.02]  I know that's just like a hand-wavy thing to say, but like, why aren't people that are making like pretty rad apps just not also like by default making them in Electron as well?
[3272.72 --> 3273.32]  Does anybody know?
[3273.88 --> 3278.40]  Because the web is important, an important distribution platform.
[3278.40 --> 3286.68]  And defaulting to native applications is maybe not the best strategy to reach the most people.
[3287.34 --> 3288.06]  Well, I mean –
[3288.06 --> 3289.68]  Go ahead.
[3290.54 --> 3292.40]  Well, like, there's –
[3293.58 --> 3306.26]  I think, like, if you talk to people that have apps that people use, like, in their – like, daily, like any app that you use for kind of business or anything that you open up daily, people prefer desktop applications.
[3306.26 --> 3306.66]  True.
[3307.30 --> 3307.88]  Like, yeah.
[3308.74 --> 3315.92]  Well, they don't have to, but if you talk to, like, Slack, for instance, right, like, they have ostensibly the exact same thing on their – on the website as they do on the desktop.
[3316.04 --> 3320.44]  And the desktop has a lot more engagement because – yeah.
[3320.56 --> 3329.46]  But getting to people initially, asking them to, you know, before they've seen any value, download this thing, it is a bit of a stretch for a lot of use cases.
[3329.46 --> 3329.90]  Right.
[3329.90 --> 3336.04]  But I think that once you have people's attention and you really want to up their engagement, that's where desktop applications are really useful.
[3337.26 --> 3337.88]  I agree.
[3338.48 --> 3338.80]  There we go.
[3338.86 --> 3341.56]  Well, we still value the desktop, it looks like.
[3342.72 --> 3345.96]  But, yeah, there's been some great articles lately.
[3346.62 --> 3351.80]  So, GitHub, actually, they have these GitHub desktop apps that they built a while back.
[3351.80 --> 3354.26]  And they had not actually moved them to Electron yet.
[3354.46 --> 3363.20]  And so, they wrote up their experience of, you know, some C Sharp and Objective-C developers that are used to writing, you know, native applications for Windows and Mac.
[3363.36 --> 3366.92]  What their experience was like, you know, moving to Electron and doing Electron stuff.
[3367.10 --> 3368.08]  It's pretty interesting.
[3368.28 --> 3369.64]  I recommend it.
[3371.94 --> 3372.38]  Yeah.
[3372.44 --> 3372.76]  All right.
[3373.30 --> 3374.16]  Let's move on to our picks.
[3374.90 --> 3375.50]  All right.
[3375.56 --> 3377.38]  Everybody got their picks locked and loaded?
[3378.34 --> 3379.70]  Yeah, but mine's a cop out.
[3379.70 --> 3380.14]  Okay.
[3381.14 --> 3382.94]  Well, we'll start with your cop app then.
[3383.04 --> 3384.26]  And then we'll go up from there.
[3384.26 --> 3385.56]  It's create React App 1.0, baby.
[3386.04 --> 3386.98]  Oh, shut up.
[3387.56 --> 3389.54]  You can't pick the project of the week.
[3389.64 --> 3390.32]  That's like cheating.
[3390.96 --> 3391.30]  Okay.
[3391.56 --> 3392.22]  Webpack 2.
[3396.32 --> 3397.60]  Tell us about Webpack 2.
[3397.66 --> 3398.14]  What's in it?
[3399.18 --> 3399.92]  Tree shaking.
[3402.48 --> 3408.18]  So, I'm going to go on a little bit of a tangent here.
[3408.18 --> 3409.72]  And you're going to get mad about it.
[3410.10 --> 3414.24]  But I think that if you need tree shaking, you're dependent on some anti-patterns.
[3414.40 --> 3419.98]  I don't think that we should have these grab bag modules with a bunch of other properties in them that you should be shaking out.
[3420.18 --> 3424.40]  I think that we should be using modules that do one thing and only export one thing.
[3424.44 --> 3425.84]  And then you don't need to tree shake.
[3428.02 --> 3428.76]  There you go.
[3429.40 --> 3429.62]  Maybe.
[3431.22 --> 3431.58]  Maybe.
[3431.58 --> 3434.22]  It's an amazing rebuttal.
[3436.30 --> 3436.74]  Maybe.
[3439.96 --> 3442.30]  Anyway, my pick of the week.
[3443.36 --> 3444.56]  Were you going to say something else?
[3444.64 --> 3445.16]  Go ahead, Ale.
[3445.16 --> 3458.42]  I was going to say that I agree to an extent that if you write something that is a little bit, does a few too many things, then tree shaking becomes a crutch.
[3458.96 --> 3462.48]  But I also think that, like, take a substack something.
[3462.78 --> 3470.20]  Take a set of tools that are only substack and you'll still get some benefit from tree shaking in the end.
[3470.20 --> 3472.68]  It won't be massive, but might as well do it.
[3473.80 --> 3483.48]  So I think tree shaking becomes even more cool when it can, the dead code removal, like, types plus.
[3484.64 --> 3488.56]  So I guess you guys are gone when we made this, the project of the week.
[3488.72 --> 3490.38]  It was, what was that thing?
[3490.84 --> 3493.96]  Code something came out recently.
[3494.16 --> 3494.48]  Facebook.
[3495.84 --> 3496.88]  It was the project.
[3496.88 --> 3508.30]  Anyways, it tries to, like, code unroll and, like, pre-compute things that are already, like, available to compute at runtime or at compiler time.
[3509.12 --> 3515.72]  And so things like that are also going to be massive, like, to where, like, there's an if statement inside of a substack module.
[3516.22 --> 3519.06]  And there's no way that's going to run based on the configuration.
[3519.62 --> 3521.46]  And therefore, it can be compiled out.
[3521.68 --> 3524.48]  And that's tree shaking, like, and it should be fine.
[3525.60 --> 3526.24]  Use it all.
[3526.24 --> 3527.24]  Use everything.
[3527.44 --> 3528.84]  Use every minifier at the same time.
[3532.98 --> 3533.90]  All right.
[3534.76 --> 3536.00]  Rachel, what's your pick?
[3536.96 --> 3544.94]  So my pick of the week is a talk from JS Confu that just happened that I unfortunately did not get to see in person.
[3545.30 --> 3547.78]  But it's from Anjana Vakil.
[3547.96 --> 3550.86]  And it's about immutable data structures for functional JS.
[3550.86 --> 3568.52]  And she just, like, explains it in such a really simplified, easy-to-understand way for people that don't really understand what, you know, immutability or mutability or functional, like, programming looks like.
[3568.52 --> 3569.52]  Like, AKA me.
[3569.52 --> 3579.52]  And so, like, she just gives visuals that explains, like, how nodes work and how, like, you can do different things with it.
[3579.52 --> 3586.78]  And how it, like, you can have the arrays structured in, well, I guess that's what mutability and immutability is.
[3586.78 --> 3589.06]  But she explains it in a way that makes sense.
[3589.46 --> 3606.70]  And she talks about it in context of David Nolan's Maury library and Facebook's immutable JS library and shows examples from both so that you're able to, like, one, understand the concept and see how different libraries are handling that kind of thing.
[3606.70 --> 3612.66]  So, yeah, if anybody else was wondering about that kind of thing, there's a link to it.
[3612.72 --> 3613.50]  And it's pretty great.
[3614.46 --> 3614.86]  Awesome.
[3615.40 --> 3619.06]  Earlier in the episode, we talked about features that we don't use.
[3619.32 --> 3626.58]  My wish is that there was a way to use immutable JS as, like, the default in the syntax.
[3627.00 --> 3631.94]  Like, there could be a Babel plugin for just, like, immutable versions of things.
[3631.94 --> 3642.82]  And there actually is a spec, I think, Seb Markage proposed immutable data structures to ECMA, but I think it's dead and it's not going to go.
[3643.40 --> 3644.82]  And it makes me sad.
[3644.96 --> 3650.38]  But I really want to use immutable JS, but I really hate changing the syntax for everything.
[3650.52 --> 3653.30]  I just want native immutable data structures.
[3653.54 --> 3656.70]  And so that's a good example of something that I don't use that I wish I could.
[3657.64 --> 3657.90]  Cool.
[3659.48 --> 3659.88]  Cool.
[3660.82 --> 3661.22]  Okay.
[3661.94 --> 3664.48]  My pick is a book.
[3665.04 --> 3666.84]  It's actually a really old book.
[3667.00 --> 3668.82]  It came out, like, in the 80s, I think.
[3669.38 --> 3669.86]  84.
[3670.64 --> 3671.04]  Crazy.
[3671.78 --> 3672.98]  But it's called Hackers.
[3673.48 --> 3674.60]  It is not...
[3674.60 --> 3675.22]  I've seen the movie.
[3675.30 --> 3676.16]  ...for the film Hackers.
[3676.26 --> 3676.68]  It is not.
[3677.32 --> 3678.66]  There's no rollerblading.
[3680.78 --> 3687.80]  No, Hackers is about the kind of origins of hacker culture, which eventually kind of became early technology and open source culture.
[3687.80 --> 3691.58]  So you can skip the third part.
[3691.68 --> 3692.70]  The book is in three parts.
[3692.70 --> 3694.94]  The third one does not hold up.
[3694.94 --> 3705.20]  But the first one is basically from the Tech Model Railroad Club at MIT in the late 50s and early 60s that started using computers in a very different way.
[3705.20 --> 3719.24]  And how their kind of culture evolved and became the AI lab at MIT, which spawned a bunch of other AI labs and was like all of the early kind of programming culture came out of what was going on there.
[3719.24 --> 3721.16]  What's the third chapter about?
[3721.68 --> 3722.30]  So hold on.
[3722.40 --> 3729.00]  The second chapter is about kind of the homebrew computer club and early Apple and early computing, like, in the Bay Area.
[3729.32 --> 3737.84]  And also how a bunch of, like, really kind of crazy counterculture political figures, like, also informed that culture and what they were doing.
[3738.02 --> 3738.96]  And that's super interesting.
[3738.96 --> 3748.32]  The third section is about the gaming industry in, like, this in Sierra and all those companies that were, like, in the early 80s.
[3748.54 --> 3752.98]  And it was more of, like, a – at the time it was like, oh, and then this is what people are doing right now.
[3753.10 --> 3756.18]  But it really doesn't connect very well to the other parts.
[3756.30 --> 3763.58]  And it really doesn't hold up as, like, this particular section of computing is not nearly as influential as these other ones, like, in hindsight, right?
[3763.58 --> 3769.06]  But also, I will – there's some appendices.
[3769.52 --> 3772.58]  One of the appendices is called The Last Hacker.
[3773.16 --> 3784.10]  And it's about the last person in the MIT media lab – or, sorry, the MIT AI lab – that is kind of the keeper of the flame for hacker culture.
[3784.90 --> 3792.82]  And it's about Richard Stallman before he started the GNU project and before there was even such thing as copyleft licenses or a GPL to argue about.
[3793.58 --> 3797.94]  And it is fascinating and explains so much.
[3799.02 --> 3799.38]  So, yeah.
[3799.88 --> 3806.46]  I've been reading – I've been trying to read a lot about kind of early hacker culture and how the counterculture movement kind of played into all this stuff.
[3806.72 --> 3810.70]  And this is, like, one of the best books to really dig into it.
[3811.08 --> 3812.00]  So it's by Steve Levy.
[3812.38 --> 3813.46]  It's called Hackers.
[3814.54 --> 3815.00]  There you go.
[3815.86 --> 3817.30]  My pick is the movie Sneakers.
[3818.30 --> 3819.64]  Oh, that's a good movie.
[3819.98 --> 3821.08]  Oh, my God.
[3821.08 --> 3823.94]  It's really the only tech movie that holds up.
[3824.36 --> 3825.38]  River Phoenix?
[3826.82 --> 3827.42]  Yeah.
[3827.84 --> 3828.18]  Yeah.
[3828.86 --> 3829.44]  Oh, man.
[3829.70 --> 3830.50]  That's a good one.
[3831.04 --> 3831.94]  That's a really good one.
[3832.38 --> 3833.66]  Some Robert Redford.
[3835.12 --> 3835.72]  Okay.
[3836.36 --> 3836.90]  Anyway.
[3837.64 --> 3838.08]  Anyway.
[3839.26 --> 3840.32]  Great talking with y'all.
[3840.46 --> 3841.96]  I think that we're just about done now.
[3842.66 --> 3843.68]  Rate us on iTunes.
[3844.24 --> 3847.38]  Check us out at changelog.com slash jsparty.
[3847.38 --> 3850.18]  You can get into our Slack.
[3850.28 --> 3859.58]  You can catch us live every Friday at noon Pacific time and something in other time zones.
[3859.94 --> 3861.00]  And thank you very much.
[3861.10 --> 3861.40]  Goodbye.
[3861.40 --> 3861.48]  Bye.
[3862.68 --> 3863.72]  All right.
[3863.76 --> 3866.14]  That wraps up this episode of JSParty.
[3866.20 --> 3867.06]  Hope you enjoyed it.
[3867.32 --> 3870.46]  We record this show live every Friday at 3 p.m.
[3870.48 --> 3870.74]  U.S.
[3870.82 --> 3871.16]  Eastern.
[3871.30 --> 3872.96]  So if you want to listen live, you can.
[3873.08 --> 3874.92]  Head to changelog.com slash community.
[3875.40 --> 3876.36]  Get in Slack.
[3876.74 --> 3878.34]  Hang out with us in real time.
[3878.68 --> 3881.86]  Special thanks to our sponsors, Century and TopTal.
[3882.22 --> 3884.20]  Also thanks to Fastly, our bandwidth partner.
[3884.74 --> 3886.30]  Head to fastly.com to learn more.
[3886.30 --> 3893.74]  This episode was edited by Jonathan Youngblood and the theme music for JSParty is produced by the mysterious Breakmaster Cylinder.
[3894.22 --> 3895.16]  We'll see you again next week.
[3895.50 --> 3896.18]  Thanks for listening.
