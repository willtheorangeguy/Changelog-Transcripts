[0.00 --> 1.80]  Shall we talk about ints?
[2.16 --> 3.80]  Who uses ints?
[4.12 --> 6.30]  I only use Flow64.
[6.68 --> 7.96]  No matter what it is.
[8.38 --> 8.94]  Yeah.
[9.52 --> 11.14]  Because you're always on point.
[11.14 --> 14.84]  Oh, nice to be done.
[15.24 --> 17.28]  That's the first good joke you've made today, Matt.
[20.08 --> 21.16]  Just today.
[22.68 --> 25.42]  Bandwidth for Change Log is provided by Fastly.
[25.74 --> 27.62]  Learn more at Fastly.com.
[27.62 --> 30.16]  Our feature flags are powered by LaunchDarkly.
[30.42 --> 32.24]  Check them out at LaunchDarkly.com.
[32.46 --> 34.32]  And we're hosted on Leno cloud servers.
[34.72 --> 38.22]  Get $100 in hosting credit at Leno.com slash Change Log.
[38.94 --> 39.94]  What's up, Gophers?
[40.02 --> 46.28]  Our friends over Gravitational made a big transition at the end of 2020 to rebrand as Teleport
[46.28 --> 49.64]  and shared a new product announcement to showcase the direction they're taking.
[50.04 --> 54.84]  Teleport is operating from a vision of being able to run and access software anywhere
[54.84 --> 56.68]  in a secure and compliant manner.
[56.68 --> 59.10]  Something they call environment-free computing.
[59.48 --> 64.70]  With Teleport, engineering teams can quickly access any resource anywhere using a unified
[64.70 --> 70.88]  access plane that consolidates access controls and auditing across all environments, infrastructure,
[71.28 --> 72.84]  applications, as well as data.
[73.22 --> 79.14]  Teleport server access lets you SSH securely into Linux servers and smart devices with a complete
[79.14 --> 79.86]  audit trail.
[80.22 --> 84.56]  Teleport Kubernetes access lets you access Kubernetes clusters securely with complete visibility
[84.56 --> 86.18]  to access and behavior.
[86.52 --> 91.00]  And finally, Teleport application access lets you access web apps running behind NAT and
[91.00 --> 92.58]  firewalls with security and compliance.
[93.44 --> 96.98]  Try Teleport today in the cloud, self-hosted, or open source.
[97.32 --> 99.92]  Head to goteleport.com to learn more and get started.
[99.92 --> 102.30]  Again, goteleport.com.
[122.10 --> 123.10]  Let's do it.
[123.66 --> 124.72]  It's go time.
[124.72 --> 130.20]  Welcome to Go Time, your source for diverse discussions from around the Go community.
[130.78 --> 135.52]  If you're following Go Time FM on Twitter, then you already know that your chance to win
[135.52 --> 138.68]  Mark Bates' Raspberry Pi 400 is on and popping.
[139.20 --> 140.84]  There are three ways to enter.
[141.18 --> 143.78]  Check the link in your show notes to read all about it.
[144.42 --> 146.02]  Okay, let's do this.
[146.02 --> 147.90]  Here we go.
[147.90 --> 159.02]  Hello and welcome to Go Time.
[159.24 --> 163.42]  I'm Matt Ryer and today we're talking about Go language proposals.
[164.28 --> 169.12]  Go is open source, so you can open issues and make proposals.
[169.12 --> 173.74]  And sometimes people do that and then sometimes they end up in the language itself.
[173.74 --> 179.72]  So we're going to learn a bit about that process and take a look at some of our favorite proposals.
[180.38 --> 183.00]  Joining me today, Johnny Borsico is back.
[183.30 --> 183.78]  Hello, Johnny.
[184.32 --> 184.60]  Hello.
[185.24 --> 186.20]  Welcome back, sir.
[186.26 --> 187.00]  It's been a while.
[187.60 --> 188.40]  Yeah, it's been a while.
[188.50 --> 191.54]  Although I was in last week's episode, you weren't around.
[191.94 --> 194.04]  But for you, I'm back.
[194.26 --> 194.42]  Yes.
[194.78 --> 195.02]  I'm back.
[195.02 --> 195.24]  Yes.
[195.50 --> 196.40]  You're new to me.
[196.64 --> 197.32]  I'm new to you.
[197.74 --> 198.92]  The listener is probably sick of you.
[199.18 --> 200.38]  But to me, I'm not.
[200.86 --> 200.92]  Yeah.
[200.92 --> 201.40]  Yeah.
[201.58 --> 202.58]  Fixture on the wall, kind of.
[202.58 --> 204.20]  No, not really.
[204.26 --> 205.08]  It doesn't happen that quickly.
[205.56 --> 206.40]  Two or three episodes.
[207.06 --> 209.24]  We're also joined by Chris Brando.
[209.32 --> 209.90]  Hello, Chris.
[210.06 --> 210.62]  Welcome back.
[210.96 --> 211.16]  Hello.
[211.86 --> 212.60]  Glad to be back.
[212.86 --> 213.50]  How have you been?
[214.20 --> 214.78]  Been well.
[215.20 --> 216.92]  You know, getting the new year started.
[217.14 --> 218.16]  Almost done with January.
[219.00 --> 219.46]  Mm-hmm.
[220.76 --> 221.08]  Yeah.
[221.90 --> 223.14]  Same for us, actually.
[223.76 --> 226.92]  And same for Daniel, who's joined us also.
[227.22 --> 227.86]  Daniel Marty.
[228.02 --> 228.94]  Welcome back, sir.
[229.22 --> 229.48]  Hi.
[229.68 --> 230.30]  Happy to be back.
[230.30 --> 231.56]  Thanks for coming back.
[231.56 --> 233.40]  Thanks for accepting our invitation.
[233.88 --> 238.10]  Maybe you could just start off by telling us, what's the process behind a proposal?
[238.44 --> 239.72]  What's the usual sort of flow?
[239.84 --> 241.04]  How do they come about?
[241.18 --> 242.38]  And what happens to them?
[243.08 --> 246.58]  So it's been a process that has iterated quite a lot in the past few years.
[246.68 --> 250.56]  So initially, it was, as you can imagine, with any open source project, people would open
[250.56 --> 253.00]  issues and be like, hey, please do X or Y.
[253.00 --> 258.20]  With language features, it was kind of messy because sometimes you would get two lines of
[258.20 --> 260.62]  somebody saying, hey, add generics, that kind of thing.
[261.08 --> 263.50]  So over time, it became more formal.
[263.50 --> 269.60]  So for really fancy changes like generics or error checking, there's a formal process where
[269.60 --> 274.98]  you have to write a document and sort of write an experimental implementation of your language
[274.98 --> 275.42]  change.
[275.82 --> 278.54]  But most changes that get proposed are smaller.
[278.80 --> 280.98]  So instead, there's a small template that you have to fill.
[281.40 --> 283.04]  And I think that's what most people end up doing.
[283.04 --> 283.48]  Right.
[284.52 --> 287.26]  And then what happens once they're out?
[287.48 --> 288.72]  We're talking open source, aren't we?
[288.78 --> 291.28]  So this is available for everyone to look at.
[291.52 --> 291.68]  Right.
[292.00 --> 297.60]  So it's a bit tricky because it's hard for the team to prioritize because something they
[297.60 --> 299.86]  could do is, for example, go from oldest to newest.
[300.42 --> 305.48]  But there's such a large backlog and some proposals are much more complex and large than others.
[305.86 --> 310.74]  So if you do them exclusively by creation time, I don't think you would get very far.
[310.82 --> 311.78]  You would get stuck pretty quickly.
[311.78 --> 316.78]  So they do a mix of like easy ones and ones that they agree with, sort of.
[317.26 --> 319.72]  And then over time, they tend to get to most of them.
[320.30 --> 324.74]  And I think they meet about once a week and they sort of consider about a dozen proposals
[324.74 --> 325.68]  per week.
[326.38 --> 326.40]  Right.
[326.52 --> 326.70]  Yeah.
[326.78 --> 328.08]  So that's amazing, really.
[328.24 --> 333.90]  And to think of like all the different possible things you could change in Go, of course, there
[333.90 --> 338.68]  are going to be a lot of those proposals because, you know, sometimes it comes down to personal
[338.68 --> 339.10]  taste.
[339.10 --> 346.06]  Sometimes people think of things that perhaps in one specific case, it would be a great feature,
[346.20 --> 348.52]  but maybe it doesn't fit in other situations.
[349.04 --> 352.14]  So it is kind of a difficult thing to do, I think, isn't it?
[352.14 --> 353.26]  To balance that.
[353.52 --> 356.00]  And like you say, some easy ones as well.
[356.00 --> 362.02]  And so, of course, yeah, the difficulty of implementing and maintaining features as well becomes the
[362.02 --> 362.22]  thing.
[362.54 --> 364.60]  You must have to kind of consider all that stuff.
[365.46 --> 365.56]  Yeah.
[365.62 --> 369.22]  And I think the template is sort of the first filter nowadays, which I think is pretty well
[369.22 --> 369.60]  designed.
[369.96 --> 370.82]  It's pretty long.
[370.90 --> 372.02]  So I'm not going to read the whole thing.
[372.02 --> 373.60]  But some bits are pretty interesting.
[373.84 --> 376.78]  There's stuff like how long have you been using Go for?
[377.12 --> 379.10]  Or who would this change help?
[379.18 --> 382.78]  Such as only researchers or maybe people who do 3D games.
[383.44 --> 386.26]  And other questions like, has this been proposed before?
[386.38 --> 387.78]  And if so, how is this different?
[388.34 --> 391.48]  Or things like, is this backwards compatible with existing Go programs?
[391.48 --> 396.98]  Because sometimes if the answer to a lot of these questions is not what you're after,
[397.38 --> 399.60]  the change is most likely not a good idea.
[400.26 --> 404.74]  And you can sense that they're encoding in those questions a way to find, make sure you've
[404.74 --> 408.72]  checked to see if there's already a proposal that's been made for this.
[409.16 --> 413.32]  Because actually, GitHub issues isn't probably the best way to solve this problem.
[413.62 --> 416.16]  So I imagine there's a lot of duplication and things like that.
[416.42 --> 416.60]  Yeah.
[416.76 --> 418.78]  And I actually find GitHub search not very good.
[418.78 --> 421.28]  It's almost like a keyword substring search.
[421.48 --> 424.44]  So I actually use Google to search for Golang issues.
[424.62 --> 426.88]  Because there's like, what, 50,000 of them.
[427.02 --> 428.84]  So it's the only way, really.
[429.70 --> 430.70]  That's a good tip.
[430.98 --> 431.62]  How do you do it?
[431.68 --> 432.46]  Any special way?
[433.54 --> 435.06]  So you can filter by site.
[435.38 --> 439.76]  So I filter by github.com slash golang slash go slash issues.
[439.94 --> 441.36]  And then whatever keywords.
[441.70 --> 443.04]  And it mostly works.
[443.72 --> 447.50]  But it's especially better than GitHub search in terms of relevance.
[447.82 --> 450.52]  Because, you know, if you didn't get exactly the right keyword,
[450.52 --> 452.84]  GitHub might not even show the issue at all.
[453.02 --> 453.46]  That kind of thing.
[453.98 --> 454.00]  Okay.
[454.10 --> 457.98]  So maybe we could have a look at some of the proposals that are out there.
[458.22 --> 459.64]  Some really interesting ones.
[460.26 --> 464.62]  And we're not going to pick any that are currently underway.
[464.84 --> 466.04]  Is that what we said?
[466.12 --> 468.56]  Although I think we've added a few extras since then, haven't we?
[469.42 --> 469.72]  Maybe.
[469.72 --> 469.92]  Yeah.
[470.40 --> 470.60]  Yeah.
[470.70 --> 475.42]  At least what I try to do when picking these is avoid the big issues like generics and error handling.
[475.42 --> 477.50]  Because I feel like those are too controversial.
[478.00 --> 480.52]  And already, you know, there's a lot of material on them.
[481.06 --> 486.42]  And we also picked proposals that are still being considered, but that haven't been accepted yet.
[486.64 --> 488.68]  So it's still stuff that's a bit up in the air.
[488.68 --> 489.86]  Mm-hmm.
[490.18 --> 493.38]  By the way, though, Daniel, nothing's too controversial for this show.
[494.04 --> 495.26]  We'll go anywhere.
[495.98 --> 496.82]  That's a promise.
[497.14 --> 497.50]  Fair enough.
[498.00 --> 498.18]  Yeah.
[498.72 --> 502.32]  So one of the first ones on the list we have is this.
[502.50 --> 504.12]  This is a really interesting one.
[504.24 --> 512.06]  It's issue 21670, which makes me feel like I'm in Star Trek by saying that.
[512.06 --> 519.40]  But it is have functions auto-implement interfaces with only a single method of that same signature.
[519.70 --> 526.72]  So this is essentially how we have handle func, which is a function type that implements the handler interface.
[527.20 --> 530.66]  And you have to explicitly say that in the code at the moment.
[531.10 --> 536.82]  It's quite a short amount of code usually because all you're doing is creating a method that then calls itself.
[536.82 --> 542.70]  So it's not too difficult to do, but this proposal is about making it automatic.
[543.14 --> 549.90]  So given a handler interface that has a serve HTTP method, you wouldn't ever have to have a handler func type.
[550.02 --> 553.90]  You could always just make a func that matches that single method.
[554.18 --> 556.72]  It would only work for single method interfaces, of course.
[557.70 --> 558.96]  What do we think about it?
[559.38 --> 560.52]  Daniel, what do you think about that one?
[560.94 --> 564.24]  Somebody made a comment in this proposal, which I think was a good point,
[564.24 --> 568.46]  which is that in Go, you can go from a method to a function by using a method value.
[568.74 --> 572.70]  So we've got a variable of type bytes.buffer, and you name it buff.
[572.80 --> 575.64]  You can do buff.write, and that is a function.
[576.02 --> 579.52]  So you can go from the method to the function, but you cannot go back, if that makes sense.
[579.68 --> 583.28]  If you have a function, you cannot easily say, okay, now use it as a method.
[583.54 --> 586.66]  You have to statically define a new type to use that function.
[588.18 --> 590.66]  So in a way, this would make the language more consistent.
[591.24 --> 593.52]  But then the question is, how often does this come up?
[593.52 --> 598.30]  NetHttp is a good example, but I struggle to think of more than like four examples.
[599.12 --> 602.46]  Well, from the standard library, maybe, but I love that pattern from that.
[602.54 --> 603.86]  I copied it from the handler funk.
[604.12 --> 606.78]  So whenever I see opportunities to use that, I do.
[607.14 --> 608.90]  And there are often opportunities.
[609.56 --> 614.06]  You know, there are lots of times when, especially when you're building something new,
[614.56 --> 618.46]  there's like a, there is a new abstraction somewhere, but you're not sure about it,
[618.46 --> 621.06]  or all you really need is just one thing from it.
[621.06 --> 623.76]  So inevitably it ends up being a single method.
[623.94 --> 630.68]  So I do a lot of homegrown single method interfaces, if you like, and usually have a funk version of them.
[631.04 --> 634.00]  In fact, sometimes I only just have the funk thing too.
[634.00 --> 642.10]  I think maybe the main argument against this proposal is that you could argue that an interface is not defined only by the signature of its methods,
[642.28 --> 644.80]  or in this case, a single method, but also the name of the method.
[645.44 --> 650.18]  So for example, is any function that looks like a read really a read?
[650.22 --> 654.60]  It could do something entirely different, and it might match the reader interface by accident.
[654.60 --> 658.16]  And I'm not sure that this would be a problem that happens often in practice,
[658.16 --> 661.48]  but it does sort of break, go as explicitness a little bit.
[661.92 --> 662.76]  That's true, yeah.
[662.86 --> 668.60]  Because you're no longer dealing with that interface type or, so yeah, and it's not explicit.
[668.86 --> 669.50]  That's a good point.
[670.52 --> 671.36]  Chris, what are your thoughts?
[671.62 --> 672.84]  I guess I have a clarifying question here.
[672.84 --> 677.82]  So this is like when you pass a function into something that takes the interface,
[678.24 --> 680.90]  it would just be like, oh, this satisfies this interface.
[681.66 --> 684.98]  I think in that case, I generally like this,
[685.20 --> 687.48]  because I feel like when you do have a function, you just want to pass it in,
[687.82 --> 692.78]  it's kind of annoying to have to wrap it in that like, oh, hdb.handler funk, here's my function,
[692.78 --> 697.68]  just adds a bit of verbosity when it's already kind of obvious what it is.
[698.26 --> 700.68]  I'm sure there's other use cases where it would be used,
[700.68 --> 706.32]  but from that perspective, it feels like that is something good about the language
[706.32 --> 707.46]  that would cut down on verbosity.
[707.60 --> 711.78]  Because I feel like Go is often a lot about just cutting down on verbosity overall.
[713.24 --> 714.78]  Yeah, well, that's interesting.
[715.02 --> 718.30]  Because to Daniel's point, it makes quite an interesting point.
[718.64 --> 722.12]  If somebody made an interface that was just a simple, just returned a string,
[722.44 --> 726.82]  say that it was called identifier, and it had an id string method,
[726.82 --> 732.40]  you could easily have a function that returned a string,
[733.32 --> 735.38]  and passing that in, I was just wondering about that case,
[735.86 --> 738.14]  about accidentally implementing an interface.
[738.84 --> 741.34]  But you're passing a function into a thing,
[741.54 --> 745.56]  so you're really aware of what you're doing at that point, aren't you?
[745.74 --> 748.88]  In fact, you're probably making the function anonymously, aren't you?
[749.42 --> 751.92]  So that you're doing it in line, right there.
[752.78 --> 756.16]  So I feel like you probably can't imagine that becoming a problem.
[756.16 --> 757.32]  I think in some cases.
[757.44 --> 759.66]  But I think you could also just have package-level functions
[759.66 --> 762.18]  that you want to use as an interface.
[762.72 --> 765.50]  And I think as far as confusing interfaces,
[765.60 --> 766.74]  or accidentally implementing them,
[766.80 --> 770.06]  I think the only one that I've consistently accidentally implemented is stringer,
[770.48 --> 773.76]  which I just think is an issue with stringer overall
[773.76 --> 775.40]  that we're probably never going to get away from.
[775.52 --> 776.64]  It's just like, oh, yeah,
[776.80 --> 781.60]  this thing will always print out whatever this method puts out
[781.60 --> 784.64]  if you pass it into any of the thump functions,
[784.64 --> 786.32]  because it implements stringer.
[786.32 --> 790.46]  But I've never really had that issue with any other interface
[790.46 --> 792.62]  of just accidentally implementing it.
[793.06 --> 794.98]  Yeah, I think I'm probably the same.
[795.38 --> 796.18]  I think, yeah.
[796.98 --> 799.70]  Johnny Borsico, what do you think about this idea
[799.70 --> 805.24]  of having functions automatically kind of magically implement an expected interface?
[805.24 --> 808.56]  I have somewhat of an allergic reaction to magic,
[808.98 --> 810.24]  so I tend to prefer...
[810.92 --> 813.28]  It's all the glitter gets in your nose, doesn't it?
[813.56 --> 814.02]  I know, yeah.
[814.04 --> 814.80]  It just gets everywhere.
[815.02 --> 816.16]  I start sneezing and coughing.
[817.24 --> 818.44]  Beautiful sneezes, though.
[819.56 --> 820.44]  Like fireworks.
[820.86 --> 821.36]  Yeah, exactly.
[821.62 --> 821.94]  Yeah, exactly.
[821.94 --> 826.20]  I mean, I kind of see the intent behind it,
[826.38 --> 832.20]  and it's one of those things where it's sort of adding a layer
[832.20 --> 833.94]  that I'm not super...
[834.52 --> 836.76]  Like, well, I don't want to say I'm uncomfortable with it.
[836.82 --> 836.94]  I'm just...
[838.06 --> 840.60]  It solves a problem I don't find myself having very often.
[840.76 --> 842.94]  I don't mind sort of that explicitness.
[843.46 --> 844.16]  So I don't know.
[844.42 --> 844.86]  It's...
[844.86 --> 845.72]  This one's...
[845.72 --> 846.70]  I'm on the fence about this one.
[846.70 --> 850.56]  I don't think I'd be pushing for it very hard.
[850.86 --> 851.70]  That's just my...
[851.70 --> 854.42]  No thumbs up on the GitHub issue from you?
[854.86 --> 856.04]  No, no.
[856.30 --> 856.68]  Okay.
[857.36 --> 858.34]  Let's move on.
[858.44 --> 860.62]  See if any of these we can get some love for.
[861.56 --> 863.24]  Have you seen this one?
[863.44 --> 864.60]  It's number...
[864.60 --> 866.30]  It's issue 43557,
[866.94 --> 870.04]  and this is about function values as iterators.
[870.64 --> 873.98]  So this is a way to let you implement a type
[873.98 --> 876.44]  that will work with the range for loop,
[876.66 --> 879.62]  and it does it by having an inter method,
[879.74 --> 881.38]  which returns a function,
[881.38 --> 882.74]  which will get the next item.
[882.86 --> 887.16]  So you kind of relies on closures to keep the state,
[887.30 --> 888.36]  and then, you know, obviously,
[888.64 --> 889.74]  if it's a method,
[890.36 --> 892.28]  which it would be from a type,
[892.34 --> 894.56]  it can use data from that type
[894.56 --> 896.42]  when kind of it's called.
[896.54 --> 897.70]  So it can return, like,
[898.20 --> 899.72]  the next item in the list,
[899.72 --> 900.46]  or whatever it's doing.
[900.46 --> 902.44]  How do you feel about this one?
[903.14 --> 905.88]  I feel like it's a carryover from other languages.
[905.88 --> 909.26]  I've used this sort of pattern in Java and stuff like that.
[909.64 --> 910.62]  And it's fine.
[911.26 --> 913.48]  Again, it's...
[913.48 --> 915.02]  I tend to be at...
[915.02 --> 918.58]  My default stance with sort of improvements like this to the language
[918.58 --> 919.62]  tends to be sort of,
[919.62 --> 921.64]  what is it that the language does now
[921.64 --> 923.16]  that this could improve?
[923.28 --> 924.54]  So this adds another way,
[924.58 --> 927.20]  a different way of sort of doing your iteration.
[927.68 --> 929.98]  And I don't have a need for that.
[930.06 --> 931.20]  Again, I don't want to be the curmudgeon
[931.20 --> 933.28]  in the corner saying no to everything, right?
[933.32 --> 934.60]  But, like, to me,
[934.66 --> 936.58]  like, if you're going to improve the language in some way,
[936.66 --> 937.62]  like, I don't want, like,
[937.86 --> 939.70]  half a dozen ways to do the same thing, right?
[939.90 --> 940.36]  And Go.
[940.44 --> 942.28]  Like, the fact that Go only has four for looping,
[942.42 --> 943.94]  I mean, to me, that was like...
[943.94 --> 944.58]  At first, I was like,
[944.98 --> 945.80]  wow, really?
[945.96 --> 948.48]  Like, aren't you going to be missing some things
[948.48 --> 950.20]  in keywords, some constructs, whatever it is?
[950.44 --> 952.04]  And then you sit down and you start using it,
[952.06 --> 953.96]  like, oh, okay, I guess, yeah,
[953.98 --> 955.46]  I don't need much else.
[955.56 --> 957.42]  I can do all the things that I need.
[958.82 --> 960.38]  So to me, this is another one of those.
[960.96 --> 963.34]  Well, this doesn't add a new way to loop over.
[963.34 --> 965.32]  It just means you can write types
[965.32 --> 968.80]  that work with the current four range thing, right?
[968.80 --> 970.52]  I mean, the way you have to do it at the moment
[970.52 --> 973.54]  is either you build your own API,
[973.88 --> 975.00]  you write, you have your own methods,
[975.00 --> 976.62]  and you just implement your own iterator,
[976.84 --> 979.60]  or you do something, if it's small enough data,
[979.70 --> 981.98]  you'll just, like, maybe create a slice,
[982.04 --> 983.70]  have a method that creates a slice,
[983.72 --> 986.26]  and then that slice can be easily ranged over
[986.26 --> 989.52]  by the four block thing.
[990.10 --> 991.10]  That's right, isn't it, Daniel?
[991.52 --> 991.76]  Yeah.
[991.76 --> 994.16]  I thought I saw you shaking your head in my periphery.
[994.62 --> 996.32]  I was thinking that I've actually seen
[996.32 --> 998.62]  some people use channels for this use case,
[998.80 --> 1001.46]  and that is avoiding the boilerplate with next,
[1001.76 --> 1004.30]  done, and so on, that kind of method interface.
[1004.92 --> 1006.16]  And it kind of works,
[1006.28 --> 1007.44]  but channels are also, like,
[1007.50 --> 1010.14]  the biggest foot gun in the entire Go language.
[1010.40 --> 1012.78]  So I really don't like when people use channels for that.
[1013.04 --> 1015.60]  And they also have their own inherent overhead, right?
[1015.80 --> 1017.14]  So a channel is an allocation,
[1017.68 --> 1019.48]  and it also means that there has to be
[1019.48 --> 1020.82]  a different Go routine on the other side
[1020.82 --> 1021.54]  sending you stuff.
[1021.74 --> 1023.40]  And how do you signal that you're done
[1023.40 --> 1024.58]  and that kind of thing?
[1025.20 --> 1026.84]  So I'm kind of with Johnny on this,
[1026.90 --> 1028.66]  that I don't think this is a big enough problem
[1028.66 --> 1030.68]  to require a language feature.
[1031.02 --> 1032.16]  But at the same time,
[1032.26 --> 1034.30]  out of all the solutions that I've seen
[1034.30 --> 1036.26]  to, like, implement custom ranging,
[1036.80 --> 1038.86]  I feel like this is the simplest and nicest.
[1039.62 --> 1041.18]  I wouldn't oppose it, but...
[1041.18 --> 1043.22]  Yeah, so you wouldn't thumbs down on the GitHub repo,
[1043.56 --> 1044.82]  on the GitHub issue.
[1045.52 --> 1046.48]  You see, I'm with you on that.
[1046.82 --> 1049.54]  This, of these solutions,
[1049.74 --> 1050.74]  this is probably my favorite,
[1051.00 --> 1052.38]  because I like the fact,
[1052.42 --> 1053.68]  I mean, it's a little bit complicated,
[1053.68 --> 1056.20]  because it's a method that returns a function.
[1057.08 --> 1058.98]  And then you have to know about closures
[1058.98 --> 1060.72]  in order to make that work properly.
[1061.28 --> 1062.34]  But it is very neat
[1062.34 --> 1065.28]  to have all your iteration code in just one method.
[1065.28 --> 1068.50]  And then the fact that you're able to use it
[1068.50 --> 1071.42]  as a normal type is kind of quite nice.
[1072.04 --> 1072.98]  The only thing is,
[1073.00 --> 1074.58]  is that it hurts readability, potentially,
[1074.72 --> 1075.60]  because at the moment,
[1075.70 --> 1077.26]  when you see a range block,
[1077.40 --> 1079.78]  you know that that is a map,
[1079.90 --> 1081.72]  or a slice, or an array.
[1081.90 --> 1084.00]  You know that isn't anything more,
[1084.08 --> 1086.24]  and it's not doing much more work, is it?
[1086.60 --> 1089.22]  Whereas if you've got your own iterator implemented,
[1089.46 --> 1091.66]  that could be doing expensive things,
[1091.66 --> 1093.04]  and that wouldn't be very clear
[1093.04 --> 1095.92]  straight from just looking at that code.
[1096.48 --> 1097.48]  And you're also relying at that point
[1097.48 --> 1099.20]  on sort of the convention, right,
[1099.30 --> 1100.46]  of the naming.
[1100.82 --> 1102.06]  And basically, whenever you see that,
[1102.10 --> 1103.42]  you're like, oh yeah, the iterator pattern.
[1103.66 --> 1104.26]  You're like, okay.
[1104.64 --> 1106.24]  It's like, you have to kind of trust, right?
[1106.52 --> 1107.70]  Obviously, you can always go take a look
[1107.70 --> 1108.30]  at the code, hopefully.
[1108.88 --> 1110.26]  But to me, again,
[1110.26 --> 1113.22]  the explicitness of my iteration
[1113.22 --> 1114.76]  matters to me, I guess.
[1115.38 --> 1117.44]  But I mean, this is nice.
[1117.52 --> 1120.02]  I mean, as presented, it is a nice idea.
[1120.02 --> 1122.60]  I'm not going to beat down on it.
[1123.00 --> 1125.40]  Is it worth the tradeoff for me?
[1125.74 --> 1127.08]  This is another one where I'm like,
[1127.16 --> 1128.02]  no, I can't see it.
[1128.38 --> 1130.34]  I think I want to like this.
[1130.52 --> 1131.46]  I like the idea,
[1131.58 --> 1133.32]  but I think the big thing for me about it
[1133.32 --> 1135.44]  is that slices and maps
[1135.44 --> 1137.12]  are known quantities, right?
[1137.12 --> 1137.78]  We can get the length.
[1137.84 --> 1138.78]  We know how long they are.
[1138.92 --> 1140.48]  With most other types of iterators,
[1140.58 --> 1142.34]  you usually have some error
[1142.34 --> 1143.76]  that might happen, right?
[1143.76 --> 1144.98]  If you're getting something from a database,
[1145.16 --> 1146.96]  or you're getting something from somewhere else.
[1146.96 --> 1150.04]  And there's not really anything in here
[1150.04 --> 1152.62]  about how you would do error handling.
[1152.72 --> 1153.82]  That's one of the things I like
[1153.82 --> 1156.38]  about kind of the iterator pattern
[1156.38 --> 1157.62]  that I've fallen into a lot,
[1157.74 --> 1158.90]  which looks a lot like,
[1159.10 --> 1160.58]  I think like db.rows does this,
[1160.64 --> 1161.44]  where you just have like,
[1161.58 --> 1163.08]  oh, .next that returns a bool,
[1163.16 --> 1164.22]  and then inside of it,
[1164.50 --> 1165.72]  you can actually get the value,
[1165.92 --> 1167.34]  and then you have an error afterward
[1167.34 --> 1169.20]  if the bool returns false.
[1169.20 --> 1172.16]  And then it kind of has this neatly packaged way
[1172.16 --> 1173.54]  of handling iteration.
[1174.96 --> 1176.34]  Because yeah, I just think like,
[1176.76 --> 1178.16]  this would definitely, I think,
[1178.18 --> 1179.10]  get abused in some ways
[1179.10 --> 1181.18]  and lead to people just not recognizing
[1181.18 --> 1182.46]  that they need to handle errors,
[1183.02 --> 1184.98]  or like call another method
[1184.98 --> 1187.00]  to get the error when they get false back.
[1187.44 --> 1188.54]  So I think this is like,
[1188.60 --> 1190.34]  it adds a little bit of nicety,
[1190.54 --> 1192.48]  but I think it would become like a giant foot gun
[1192.48 --> 1194.42]  for API designers.
[1195.56 --> 1196.50]  Very interesting.
[1196.84 --> 1197.08]  Cool.
[1197.36 --> 1198.88]  One thing I want to come back to, Daniel,
[1198.88 --> 1201.94]  is that you said channels are a foot gun.
[1202.70 --> 1204.74]  I'm considering that in a popular opinion,
[1204.88 --> 1206.16]  but we'll swing back to that one later.
[1207.06 --> 1208.40]  Just making a mental note.
[1208.74 --> 1210.14]  A verbal mental note.
[1210.78 --> 1213.30]  It sounded like a verbal mental threat.
[1214.56 --> 1215.32]  Just a note.
[1216.30 --> 1218.26]  And I was about to also bring up something
[1218.26 --> 1220.74]  about ranges being simple nowadays,
[1220.74 --> 1222.24]  because they're not really,
[1222.38 --> 1223.70]  you can range over a channel
[1223.70 --> 1225.26]  and that could block forever, basically.
[1225.52 --> 1227.68]  Or you could range over, for example,
[1227.68 --> 1229.24]  a slice where each element
[1229.24 --> 1230.62]  takes a gigabyte in memory
[1230.62 --> 1231.60]  and then you have to copy that
[1231.60 --> 1232.42]  in every iteration
[1232.42 --> 1233.82]  and that could take a long time.
[1234.30 --> 1234.40]  Right.
[1234.70 --> 1237.02]  So I think ranges are already kind of confusing.
[1237.16 --> 1238.84]  This would maybe make them more confusing,
[1239.06 --> 1240.14]  but it's not binary.
[1240.34 --> 1241.52]  Like suddenly they become bad.
[1241.52 --> 1251.02]  Hey, Gophers, this episode is brought to you
[1251.02 --> 1252.56]  by our friends at LaunchDarkly,
[1252.90 --> 1255.08]  feature management for the modern enterprise,
[1255.34 --> 1257.26]  power experimentation and production.
[1257.66 --> 1258.38]  Here's how it works.
[1258.76 --> 1260.16]  LaunchDarkly enables development
[1260.16 --> 1263.60]  and operation teams to deploy code at any time.
[1263.78 --> 1266.08]  Even if a feature isn't ready to be released to users,
[1266.40 --> 1267.94]  wrapping code with feature flags
[1267.94 --> 1270.06]  gives you the safety to test new features
[1270.06 --> 1272.44]  and infrastructure in your production environments
[1272.44 --> 1274.82]  without impacting the wrong end users.
[1275.20 --> 1276.14]  When you're ready to release,
[1276.38 --> 1278.66]  more widely, simply update the feature flag
[1278.66 --> 1281.12]  and the changes are made instantaneously
[1281.12 --> 1282.84]  by the real-time streaming architecture.
[1283.22 --> 1284.90]  Eliminate risk, deliver value,
[1285.18 --> 1287.74]  get started for free today at LaunchDarkly.com.
[1287.94 --> 1289.50]  Again, LaunchDarkly.com.
[1289.50 --> 1291.50]  LaunchDarkly.com.
[1291.50 --> 1293.50]  LaunchDarkly.com.
[1293.50 --> 1295.50]  LaunchDarkly.com.
[1295.50 --> 1296.00]  LaunchDarkly.com.
[1296.00 --> 1296.50]  LaunchDarkly.com.
[1296.50 --> 1297.00]  LaunchDarkly.com.
[1297.00 --> 1298.00]  LaunchDarkly.com.
[1306.58 --> 1308.82]  It's time to move on to the next proposal.
[1309.40 --> 1311.06]  Daniel, do you want to tell us about this next one?
[1311.40 --> 1314.06]  Yeah, so this next one is pretty easy to understand, I think.
[1314.22 --> 1317.72]  It's essentially type inference for when you use make and new.
[1317.92 --> 1321.02]  So you can use make or new to, for example,
[1321.38 --> 1324.12]  make to create a new map with some capacity
[1324.12 --> 1326.84]  or new to allocate a pointer to an int.
[1327.00 --> 1329.12]  or a Boolean or whatever you want.
[1329.84 --> 1332.14]  And that is fine, but quite a lot of the times
[1332.14 --> 1333.22]  when you use make or new,
[1333.66 --> 1335.92]  you're assigning that to something that already has a type,
[1336.00 --> 1337.64]  like a field, like a struct field.
[1338.08 --> 1340.18]  So in those cases, you have to repeat the type,
[1340.26 --> 1342.72]  or even worse, you have to remember what the type was
[1342.72 --> 1345.00]  to then copy and paste it or write it again manually.
[1345.68 --> 1347.70]  So this is a small language change to say
[1347.70 --> 1350.66]  only within those two built-in functions,
[1350.66 --> 1352.12]  infer the type.
[1352.26 --> 1353.40]  If, for example, it's missing,
[1353.80 --> 1355.08]  that would be like NeoSyntax.
[1355.08 --> 1359.92]  And this is number 34515 in the GitHub issues
[1359.92 --> 1362.38]  in the Go repo if you want to follow along at home.
[1363.38 --> 1365.04]  Okay, what do we think about this one then?
[1365.70 --> 1366.88]  Chris, have we got any thoughts?
[1367.56 --> 1368.22]  I like it.
[1368.56 --> 1372.08]  I'm kind of thinking about like when I write like test code,
[1372.16 --> 1375.22]  I sometimes like to have like lots of anonymous structs
[1375.22 --> 1377.10]  and anonymous things,
[1377.54 --> 1379.94]  and it'd be a little bit easier to make a map
[1379.94 --> 1381.10]  if it already has the type there
[1381.10 --> 1382.46]  and it'd cut down on the code a little bit.
[1382.84 --> 1385.90]  I don't know how I feel about the kind of empty
[1385.90 --> 1387.84]  or whatever the syntax we come up with,
[1387.88 --> 1389.18]  like just having something be like make.
[1389.28 --> 1391.90]  I think it'd take a while for me to get used to that
[1391.90 --> 1394.72]  since I'm so used to like seeing a type in there.
[1395.02 --> 1395.98]  But I think overall,
[1396.12 --> 1397.82]  it could be a benefit to the language
[1397.82 --> 1400.16]  and make things a little bit less verbose
[1400.16 --> 1401.24]  in obvious situations.
[1401.86 --> 1404.46]  So overall, I think I'm like a general thumbs up,
[1404.46 --> 1405.28]  but cautious.
[1406.04 --> 1407.30]  Yeah, general thumbs up.
[1407.56 --> 1410.26]  Ian Lance Taylor actually recommended
[1410.26 --> 1413.04]  using the three dots again inside the make
[1413.04 --> 1414.90]  to indicate like infer the type
[1414.90 --> 1415.66]  because it's the same.
[1415.86 --> 1417.50]  That's what we mean in inside
[1417.50 --> 1419.82]  both like lengths of arrays
[1419.82 --> 1422.72]  and also if we're doing other times,
[1422.76 --> 1423.30]  I can't remember.
[1424.20 --> 1425.46]  So yeah, I'm with you actually.
[1425.54 --> 1426.64]  I quite like this one too.
[1426.72 --> 1429.84]  I feel like you don't get really any benefit
[1429.84 --> 1432.52]  from repeating it, I suppose.
[1432.72 --> 1435.16]  And so maybe that's the argument though.
[1435.44 --> 1436.64]  Would there be a benefit
[1436.64 --> 1439.24]  if they're separated those two types?
[1439.24 --> 1441.42]  Would you lose something?
[1441.50 --> 1443.00]  Would you have to then go back to the type?
[1443.64 --> 1444.28]  I like that one.
[1444.68 --> 1445.62]  Of the ones so far,
[1445.68 --> 1447.26]  this was probably my favorite one
[1447.26 --> 1448.22]  I could see using it.
[1448.80 --> 1450.80]  What we settled on in terms of
[1450.80 --> 1451.94]  how to indicate like,
[1452.04 --> 1453.80]  hey, we've already specified the type,
[1453.86 --> 1454.44]  go figure it out,
[1454.50 --> 1455.24]  whether it's a three dot
[1455.24 --> 1457.14]  or the original post was
[1457.14 --> 1459.78]  proposing a type of keyword,
[1459.98 --> 1461.80]  which would definitely get abused everywhere.
[1461.80 --> 1466.26]  But I could definitely see that
[1466.26 --> 1468.30]  because you've already specified the information.
[1468.52 --> 1470.44]  I mean, the language can infer the type.
[1471.00 --> 1473.26]  So it's like saving a few keystrokes.
[1474.48 --> 1476.10]  I mean, of the bunch we've seen so far,
[1476.18 --> 1478.36]  this is probably the one I could see using.
[1479.02 --> 1481.52]  You know, like to borrow Chris's opinion,
[1481.92 --> 1483.88]  they would take me a little bit of getting used to
[1483.88 --> 1484.98]  because I'm not used to,
[1485.06 --> 1486.66]  I'm always used to specify my types,
[1486.66 --> 1487.84]  but I don't know.
[1487.92 --> 1489.56]  I could see myself like,
[1489.62 --> 1490.62]  you know, getting used to it.
[1491.04 --> 1491.18]  Yeah.
[1491.46 --> 1493.02]  I think like it said in the proposal,
[1493.22 --> 1494.90]  making new are kind of weird functions anyway,
[1495.00 --> 1496.90]  since they take like a type name,
[1497.04 --> 1499.28]  whereas most other things in the language
[1499.28 --> 1500.40]  don't take type names.
[1500.50 --> 1502.32]  So they're already a bit like different and weird.
[1502.88 --> 1503.10]  Yeah.
[1503.12 --> 1504.00]  Why are they different?
[1504.26 --> 1506.10]  Why couldn't that be one keyword?
[1506.64 --> 1506.86]  Yeah.
[1507.44 --> 1509.22]  And I was actually going to go in that direction.
[1509.44 --> 1511.86]  I find making new to be too special
[1511.86 --> 1513.78]  and this would make them further special.
[1514.90 --> 1515.82]  Like for example,
[1515.82 --> 1518.80]  if people wouldn't currently have composite literals
[1518.80 --> 1520.38]  for like maps or something else,
[1520.82 --> 1522.60]  they might switch them over to use make
[1522.60 --> 1524.36]  just so that they could get type inference.
[1524.94 --> 1526.50]  And I find that kind of weird.
[1526.74 --> 1530.06]  So I would rather almost see make a new gone.
[1530.96 --> 1534.52]  And well, make wouldn't be gone for good
[1534.52 --> 1536.30]  because it can still be useful to, for example,
[1536.38 --> 1537.96]  specify the capacity and that kind of thing.
[1538.28 --> 1540.08]  But in most cases, you don't need to specify.
[1540.08 --> 1541.86]  You just want to create a new thing.
[1542.78 --> 1545.04]  So I would rather see composite literals
[1545.04 --> 1545.86]  become more powerful.
[1546.58 --> 1549.60]  Are auto kind of instantiating maps
[1549.60 --> 1550.86]  such a big problem?
[1551.10 --> 1555.96]  I mean, I love how the append key built-in function
[1555.96 --> 1560.40]  will make the slice if it's not already there.
[1560.50 --> 1562.18]  If it's nil or if it's, you know,
[1562.24 --> 1563.22]  you've just declared it,
[1563.42 --> 1565.76]  then it will make it when you put the first item in,
[1565.84 --> 1566.84]  it will set things up.
[1567.10 --> 1569.18]  Could we not also have maps that behave that way?
[1569.18 --> 1571.42]  Or is it just that way?
[1571.46 --> 1573.16]  Because it sort of would be magic,
[1573.72 --> 1574.50]  would be too magic.
[1574.50 --> 1575.56]  If you had that, though,
[1575.62 --> 1577.02]  anytime you want to assign to a map,
[1577.10 --> 1578.58]  you'd have to like call a built-in function
[1578.58 --> 1579.90]  and reassign to the map,
[1580.06 --> 1582.40]  which would be, I guess it would be worse.
[1582.56 --> 1582.92]  I don't know.
[1583.88 --> 1585.34]  Well, I mean, it could be, yes.
[1585.44 --> 1588.36]  But I was thinking the language would stay the same,
[1588.64 --> 1589.82]  but it would work.
[1589.96 --> 1591.40]  You'd be able to just like,
[1591.46 --> 1592.64]  I mean that as a core principle,
[1592.74 --> 1593.88]  not as a change, I suppose.
[1594.34 --> 1596.30]  So like the compiler would be like,
[1596.36 --> 1597.32]  oh, this is a nil map.
[1597.38 --> 1599.02]  I'm going to instantiate it for you
[1599.02 --> 1602.22]  and then add this value or whatever.
[1603.12 --> 1605.34]  Yeah, because that's really the experience
[1605.34 --> 1606.24]  we get with append.
[1607.96 --> 1610.20]  But that's not this proposal, by the way.
[1610.86 --> 1611.76]  But I was just saying,
[1611.92 --> 1614.18]  I always thought it would have been all right.
[1614.58 --> 1616.46]  I definitely agree with Daniel, though,
[1616.54 --> 1619.18]  on like how make and new are kind of weird,
[1619.72 --> 1621.64]  especially when you're first learning the language
[1621.64 --> 1623.52]  and you're like, oh, I want to make a map
[1623.52 --> 1625.50]  or I want to make a slice.
[1625.68 --> 1627.06]  And you think like, oh, I use new.
[1627.18 --> 1628.78]  I'm going to make new other things.
[1628.92 --> 1629.86]  So I should make new here.
[1629.90 --> 1632.92]  And it's like, no, new is not what you want at all
[1632.92 --> 1634.80]  when you make a map or a slice.
[1635.28 --> 1636.38]  And I think that's like something
[1636.38 --> 1637.42]  that trips people up a lot
[1637.42 --> 1639.34]  and you just like kind of got to get used to it.
[1639.42 --> 1641.98]  So yeah, I think like if there was a way
[1641.98 --> 1645.38]  to like reduce down what you used make and new for,
[1645.84 --> 1647.40]  I think that would be good.
[1647.80 --> 1647.90]  Yeah.
[1647.96 --> 1649.14]  Because a lot of the time it's just better
[1649.14 --> 1652.36]  to just like do the kind of instantiation
[1652.36 --> 1655.04]  without using the built-ins.
[1655.82 --> 1658.36]  Unless you really do want to have that capacity
[1658.36 --> 1660.66]  or you want to specify the length
[1660.66 --> 1663.46]  and don't want to type a bunch of empty values
[1663.46 --> 1664.74]  in a slice or something like that.
[1665.00 --> 1667.54]  It is awkward explaining you to a Go beginner
[1667.54 --> 1669.86]  when to use it, when not to use it.
[1670.28 --> 1672.32]  You know, it also like usually the conversation,
[1672.48 --> 1675.70]  well, is that like a constructor kind of thing?
[1675.70 --> 1679.00]  Like, can I use it to like initialize a new thing?
[1679.26 --> 1680.52]  And how does that work?
[1680.58 --> 1683.14]  And I can only use make in certain cases,
[1683.14 --> 1685.26]  like with channels and other places.
[1685.26 --> 1687.08]  It becomes very sort of confusing,
[1687.34 --> 1688.82]  but I don't think that's a bad thing, honestly.
[1688.90 --> 1690.46]  I think that's just Go.
[1691.26 --> 1693.48]  Once you learn how Go works,
[1693.72 --> 1696.84]  you kind of get over those minor issues.
[1696.96 --> 1698.46]  I call them minor, but again,
[1698.48 --> 1699.24]  I'm speaking for somebody
[1699.24 --> 1700.94]  who's been doing this for a little while.
[1700.96 --> 1702.18]  So my opinion is going to be very different
[1702.18 --> 1703.38]  from somebody who's approaching the language.
[1703.38 --> 1704.50]  And I'll admit that, you know,
[1704.54 --> 1706.88]  like it's the curse of those who are experienced, right?
[1706.94 --> 1708.94]  You no longer see the problems beginners have.
[1709.02 --> 1710.88]  And I totally, you know, own up to that.
[1712.78 --> 1714.10]  Yeah, I think that's fine.
[1714.10 --> 1717.38]  I like the curly brace to create new things
[1717.38 --> 1719.82]  because it's the same for maps and slices
[1719.82 --> 1721.26]  and structs and stuff.
[1721.34 --> 1722.18]  So you get to be,
[1722.44 --> 1725.18]  you can yourself choose to just do it one way.
[1725.62 --> 1728.06]  And so I would actually be happy with just that way.
[1728.16 --> 1729.84]  I think we should just only have that.
[1730.48 --> 1731.26]  Except basic types.
[1731.26 --> 1731.70]  Right.
[1733.46 --> 1733.80]  Yes.
[1733.94 --> 1735.76]  Well, also zero value types,
[1735.88 --> 1738.00]  I think are also quite nice.
[1738.22 --> 1739.32]  So the fact that that works,
[1739.36 --> 1741.46]  I think is, you know, it's kind of good.
[1741.66 --> 1745.00]  You can call methods on nil types
[1745.00 --> 1747.10]  and it isn't always a disaster.
[1747.60 --> 1748.70]  Anything else on this?
[1749.20 --> 1750.68]  Then we shall move forward.
[1751.46 --> 1752.36]  Sorry if that was too loud.
[1755.06 --> 1756.42]  Jarrah's going to have words with you.
[1756.82 --> 1757.04]  Yeah.
[1757.80 --> 1758.92]  Someone's got a mouse wheel
[1758.92 --> 1762.32]  because I've been listening and you've done about six miles so far.
[1762.68 --> 1763.36]  Calling anyone out.
[1763.58 --> 1764.72]  Someone's got a mouse wheel.
[1764.96 --> 1765.62]  That's all I'm saying.
[1766.46 --> 1767.62]  You know, a wheel and a mouse.
[1768.20 --> 1769.24]  It's a wheel and a mouse.
[1769.96 --> 1770.44]  This doesn't matter.
[1770.54 --> 1772.50]  I'm just saying I can hear a mouse wheel going.
[1772.74 --> 1773.64]  It's been about six miles.
[1773.72 --> 1775.04]  I've been keeping track of my Apple Watch.
[1776.92 --> 1777.90]  So, okay.
[1777.90 --> 1783.34]  The next proposal then is called lazy values.
[1784.06 --> 1784.62]  Dally nil.
[1785.88 --> 1786.78]  What's this one?
[1786.78 --> 1790.10]  So this is proposal number 37739,
[1790.80 --> 1792.06]  if anybody wants to check it out.
[1792.60 --> 1795.86]  And it's essentially trying to solve the problem that,
[1796.16 --> 1796.48]  for example,
[1796.54 --> 1799.22]  if you've got some verbose logging lines
[1799.22 --> 1802.28]  and you are logging some things
[1802.28 --> 1804.90]  that might be expensive to calculate,
[1804.90 --> 1806.46]  to evaluate such as, you know,
[1806.96 --> 1808.30]  give me the string of something
[1808.30 --> 1810.56]  or give me the length
[1810.56 --> 1813.24]  of some very large decentralized data structure
[1813.24 --> 1813.98]  or something like that.
[1814.42 --> 1815.24]  And the thing is,
[1815.54 --> 1819.00]  yes, the log verbose function can do nothing
[1819.00 --> 1821.90]  if the verbose logging is not enabled.
[1822.16 --> 1823.18]  But those parameters,
[1823.40 --> 1825.16]  those arguments have to be calculated anyway
[1825.16 --> 1826.42]  because it's still a function call.
[1827.24 --> 1829.40]  And you can wrap the whole function call
[1829.40 --> 1830.90]  in an if statement,
[1831.20 --> 1833.00]  but that's very verbose in itself.
[1833.00 --> 1835.74]  So what this proposal says is essentially,
[1835.94 --> 1838.48]  what if we have a sort of generic interface
[1838.48 --> 1840.70]  that has a method called eval
[1840.70 --> 1843.68]  to evaluate into some type T?
[1844.20 --> 1846.78]  And then when you pass that onto a function,
[1847.02 --> 1849.98]  which is designed to take lazy values,
[1850.36 --> 1853.10]  then it's going to evaluate that lazy value
[1853.10 --> 1854.84]  as it needs it, but not otherwise.
[1855.48 --> 1855.56]  Yeah.
[1855.72 --> 1857.70]  So essentially then you can pass functions
[1857.70 --> 1860.68]  into other functions and other types
[1860.68 --> 1863.10]  and it'll only be called when they're used
[1863.10 --> 1864.48]  inside that function body.
[1864.70 --> 1865.26]  Is that right?
[1865.98 --> 1866.66]  Yeah, pretty much.
[1866.78 --> 1867.86]  And you could do this today
[1867.86 --> 1870.10]  with like interface types or functions,
[1870.24 --> 1870.96]  passing functions.
[1871.68 --> 1873.64]  But I think this is more about
[1873.64 --> 1876.02]  making it more of a proper language feature
[1876.02 --> 1877.16]  that people should be using
[1877.16 --> 1878.20]  for this kind of thing.
[1878.74 --> 1879.00]  Hmm.
[1880.46 --> 1880.94]  Yes.
[1881.12 --> 1882.66]  Well, often lazy loading
[1882.66 --> 1885.58]  is a good thing to do in code
[1885.58 --> 1886.98]  for various reasons.
[1887.42 --> 1888.46]  Chris, how do you feel about it
[1888.46 --> 1890.22]  being an actual language feature?
[1890.22 --> 1892.06]  I guess I'm kind of on the fence with it.
[1892.14 --> 1895.06]  I can see where and how it would be useful.
[1895.64 --> 1896.70]  I think my only concern would be
[1896.70 --> 1898.52]  like getting the API right.
[1898.96 --> 1899.46]  And then also,
[1899.46 --> 1900.64]  I guess I have two concerns.
[1900.74 --> 1903.80]  I think also how it can be abused
[1903.80 --> 1905.54]  and helping to make sure
[1905.54 --> 1907.54]  that it's not abused
[1907.54 --> 1910.02]  to kind of make egregious Go code.
[1910.64 --> 1911.76]  I think like channels
[1911.76 --> 1912.66]  always come to my mind
[1912.66 --> 1913.38]  when I think about that,
[1913.42 --> 1914.52]  of how people just like
[1914.52 --> 1916.62]  really abuse channels in bad ways
[1916.62 --> 1917.64]  just because they're there
[1917.64 --> 1919.68]  and channels are a feature of the language.
[1920.22 --> 1921.98]  I could see people perhaps being like,
[1922.06 --> 1923.48]  oh, we have this like lazy evaluation.
[1923.70 --> 1925.12]  I know how lazy evaluation works
[1925.12 --> 1926.10]  in language X.
[1926.20 --> 1927.00]  So I'm just going to do
[1927.00 --> 1928.60]  what I do in language X,
[1928.70 --> 1929.38]  even if there's like
[1929.38 --> 1930.78]  a more idiomatic go way
[1930.78 --> 1932.28]  to do it that has
[1932.28 --> 1933.10]  either better performance
[1933.10 --> 1933.82]  or more clarity
[1933.82 --> 1934.84]  or whatnot.
[1935.34 --> 1936.14]  But I think if we can,
[1936.38 --> 1936.88]  as a community,
[1937.00 --> 1938.40]  figure out how to like convey
[1938.40 --> 1940.36]  this is the kind of things
[1940.36 --> 1941.78]  you should be using lazy for
[1941.78 --> 1943.66]  and lazy evaluation for,
[1943.74 --> 1944.70]  then I think it could be
[1944.70 --> 1945.94]  a very useful feature
[1945.94 --> 1947.94]  and a wide range of software.
[1947.94 --> 1949.28]  Yeah, you see,
[1949.38 --> 1951.82]  I've implemented almost this,
[1951.92 --> 1953.12]  but by using functions.
[1953.46 --> 1954.38]  So the idea is
[1954.38 --> 1955.92]  you've got some kind of loader
[1955.92 --> 1958.50]  and you just pass in the function
[1958.50 --> 1959.50]  and it works
[1959.50 --> 1960.94]  because it can also be
[1960.94 --> 1962.54]  the method of a type as well.
[1963.18 --> 1963.46]  You know,
[1963.48 --> 1964.48]  so you can even have it
[1964.48 --> 1965.64]  in this kind of services
[1965.64 --> 1967.22]  or other higher level
[1967.22 --> 1969.26]  kind of object design
[1969.26 --> 1971.32]  situations as well.
[1971.82 --> 1972.76]  And so it's nice.
[1972.84 --> 1973.90]  You pass the function in
[1973.90 --> 1975.42]  and internally,
[1975.78 --> 1977.00]  depending on when you call it,
[1977.02 --> 1977.80]  if you even do,
[1978.42 --> 1978.70]  you know,
[1978.74 --> 1979.46]  it only gets called
[1979.46 --> 1980.16]  at that point.
[1980.52 --> 1981.52]  The nice thing about
[1981.52 --> 1982.50]  doing it explicitly
[1982.50 --> 1984.52]  is you get to choose
[1984.52 --> 1985.94]  like arguments
[1985.94 --> 1986.88]  and things like this.
[1987.12 --> 1989.20]  Whereas this proposal,
[1989.62 --> 1990.88]  where it seems like
[1990.88 --> 1992.08]  almost it looks a bit like
[1992.08 --> 1993.58]  defer how you're calling
[1993.58 --> 1994.78]  that method immediately.
[1995.44 --> 1997.00]  But I guess, again,
[1997.04 --> 1997.98]  it's kind of trade-offs
[1997.98 --> 1998.50]  and things.
[1999.30 --> 2000.10]  Johnny, did you have a chance
[2000.10 --> 2000.90]  to look at this one?
[2000.90 --> 2003.74]  This is the functions,
[2004.26 --> 2005.10]  lazy values.
[2005.66 --> 2006.82]  Yeah, I didn't have enough time
[2006.82 --> 2008.08]  to sort of form an opinion
[2008.08 --> 2009.54]  of it on its face.
[2009.72 --> 2011.40]  It looks like an interesting idea.
[2011.62 --> 2012.16]  I just don't have
[2012.16 --> 2012.92]  an opinion on it.
[2013.26 --> 2013.62]  Fair enough.
[2014.08 --> 2014.98]  Somebody also left
[2014.98 --> 2016.26]  a counterproposal
[2016.26 --> 2017.42]  somewhere in the comments
[2017.42 --> 2018.78]  essentially saying
[2018.78 --> 2020.90]  if we made anonymous functions
[2020.90 --> 2022.52]  less verbose to write
[2022.52 --> 2023.08]  and use,
[2023.28 --> 2024.44]  then people would do
[2024.44 --> 2025.16]  what Matt said
[2025.16 --> 2027.08]  of using function parameters
[2027.08 --> 2027.52]  more often.
[2027.92 --> 2029.42]  And I think I agree with that.
[2029.96 --> 2030.42]  Hmm.
[2030.90 --> 2032.34]  Yeah, those function parameters
[2032.34 --> 2034.56]  are definitely worth a look,
[2034.90 --> 2035.50]  I would say.
[2035.76 --> 2037.04]  Okay, that's an interesting one.
[2037.50 --> 2038.18]  It's funny, you know,
[2038.22 --> 2040.02]  seeing these proposals,
[2040.22 --> 2040.76]  they're sort of,
[2041.48 --> 2042.26]  a lot of them so far
[2042.26 --> 2044.88]  are solving real code problems
[2044.88 --> 2046.02]  that we've lived with
[2046.02 --> 2046.56]  for a while.
[2047.06 --> 2048.00]  So it's interesting
[2048.00 --> 2048.98]  to see the different
[2048.98 --> 2050.00]  kind of points
[2050.00 --> 2051.40]  of the life in a language.
[2052.14 --> 2052.62]  Because, of course,
[2052.66 --> 2053.78]  there have been language proposals
[2053.78 --> 2054.66]  all along,
[2054.84 --> 2056.04]  but these are interesting
[2056.04 --> 2057.02]  to see some of the level
[2057.02 --> 2057.42]  of these.
[2058.74 --> 2060.74]  Shall we talk about ints?
[2060.90 --> 2061.52]  Does anyone,
[2062.06 --> 2063.84]  who uses ints
[2063.84 --> 2066.08]  in your programming?
[2066.44 --> 2067.34]  I only use
[2067.34 --> 2068.62]  Flow64.
[2069.02 --> 2069.52]  You only do.
[2069.56 --> 2070.32]  No matter what it is.
[2070.84 --> 2071.32]  Yeah.
[2072.00 --> 2072.88]  Because you're always
[2072.88 --> 2073.50]  on point.
[2074.34 --> 2074.78]  Oh,
[2074.78 --> 2077.20]  nice to be done.
[2078.26 --> 2078.82]  Something like that.
[2078.82 --> 2079.46]  First good joke
[2079.46 --> 2080.32]  you've made today, Matt.
[2083.58 --> 2084.38]  Just today.
[2086.06 --> 2087.02]  Yeah, that's a compliment.
[2087.58 --> 2088.38]  Ooh, it's a pile on.
[2088.44 --> 2089.14]  Daniel, it's your turn.
[2090.72 --> 2091.44]  Oh, no,
[2091.48 --> 2092.08]  I was going to say
[2092.08 --> 2093.22]  a joke about Batman
[2093.22 --> 2094.04]  and, you know,
[2094.12 --> 2094.68]  not a number.
[2095.42 --> 2095.80]  Oh, yeah.
[2097.10 --> 2097.68]  Thank you
[2097.68 --> 2099.24]  for taking the heat
[2099.24 --> 2099.72]  off me
[2099.72 --> 2101.54]  and placing it rightly
[2101.54 --> 2102.48]  onto Batman
[2102.48 --> 2104.22]  and that not a number
[2104.22 --> 2105.10]  thing in JavaScript.
[2105.40 --> 2106.20]  They both deserve our.
[2107.00 --> 2108.06]  They both deserve our.
[2108.56 --> 2109.00]  Arr.
[2109.80 --> 2110.14]  Okay,
[2110.32 --> 2111.66]  let's talk about ints.
[2112.32 --> 2113.24]  There's a proposal
[2113.24 --> 2114.76]  to change an int
[2114.76 --> 2116.64]  to be arbitrary precision,
[2117.08 --> 2117.50]  which when,
[2117.64 --> 2118.46]  when you think about that,
[2118.52 --> 2119.00]  this is number
[2119.00 --> 2119.32]  one,
[2119.38 --> 2119.60]  nine,
[2119.60 --> 2120.02]  six,
[2120.14 --> 2120.26]  two,
[2120.26 --> 2120.62]  three.
[2121.36 --> 2122.42]  That as a headline
[2122.42 --> 2123.82]  doesn't make much sense,
[2124.08 --> 2125.24]  but Daniel,
[2125.34 --> 2126.26]  perhaps you could explain
[2126.26 --> 2127.10]  this one to us.
[2127.52 --> 2127.62]  Yeah,
[2127.62 --> 2128.42]  so to recap,
[2128.88 --> 2129.60]  Go has,
[2129.70 --> 2130.02]  for example,
[2130.22 --> 2131.64]  int 32 and int 64,
[2131.94 --> 2133.10]  which are fixed size.
[2133.70 --> 2133.72]  So,
[2134.04 --> 2134.34]  for example,
[2134.46 --> 2135.10]  int 32,
[2135.18 --> 2136.06]  you've got 32 bits
[2136.06 --> 2137.64]  when you get to the maximum value,
[2137.72 --> 2138.22]  which is
[2138.22 --> 2139.68]  two to the power of
[2139.68 --> 2140.60]  31
[2140.60 --> 2142.14]  or whatever it is.
[2142.48 --> 2143.48]  If you go past that,
[2143.54 --> 2144.24]  then it overflows
[2144.24 --> 2144.92]  and it goes to the
[2144.92 --> 2146.34]  lowest negative value.
[2146.80 --> 2146.94]  Right,
[2146.96 --> 2147.74]  so it wraps around.
[2148.48 --> 2148.70]  Yeah.
[2149.34 --> 2149.56]  Yeah,
[2149.64 --> 2150.32]  like Pac-Man.
[2151.96 --> 2153.00]  I think it's called that.
[2153.32 --> 2153.72]  If not,
[2153.74 --> 2154.20]  it should be.
[2155.28 --> 2155.68]  Go on,
[2155.68 --> 2156.76]  I'm just trying to make it clear
[2156.76 --> 2157.48]  for all,
[2157.62 --> 2158.34]  all levels,
[2158.54 --> 2159.12]  all abilities.
[2160.08 --> 2160.30]  Yeah.
[2160.82 --> 2161.24]  So,
[2161.34 --> 2161.66]  essentially,
[2161.86 --> 2162.66]  you don't have protection
[2162.66 --> 2163.90]  against that kind of error
[2163.90 --> 2164.80]  where it essentially
[2164.80 --> 2165.46]  loops around
[2165.46 --> 2166.78]  and goes back to the bottom.
[2167.38 --> 2168.26]  And then there's int,
[2168.44 --> 2170.02]  which doesn't have a fixed size.
[2170.16 --> 2170.30]  So,
[2170.34 --> 2171.48]  on 64-bit computers,
[2171.64 --> 2172.64]  like most laptops
[2172.64 --> 2173.74]  and desktops these days,
[2174.12 --> 2175.14]  it's 64 bits,
[2175.68 --> 2176.00]  but on,
[2176.08 --> 2176.40]  for example,
[2176.50 --> 2177.22]  small routers,
[2177.28 --> 2178.74]  which might still be 32 bits,
[2179.20 --> 2180.28]  it's going to be 32 bits.
[2180.80 --> 2181.80]  And this causes
[2181.80 --> 2183.68]  some bugs in real programs
[2183.68 --> 2183.96]  because,
[2184.08 --> 2184.34]  for example,
[2184.46 --> 2185.52]  people might only test
[2185.52 --> 2186.68]  on 64-bit machines
[2186.68 --> 2187.82]  and then their code
[2187.82 --> 2188.88]  might actually break
[2188.88 --> 2189.82]  on 32-bit machines
[2189.82 --> 2190.14]  with,
[2190.18 --> 2190.42]  like,
[2190.46 --> 2191.26]  regular workloads.
[2191.86 --> 2192.08]  So,
[2192.14 --> 2192.60]  this proposal
[2192.60 --> 2193.48]  is essentially to say,
[2194.02 --> 2194.26]  no,
[2194.62 --> 2196.20]  the int type without a size
[2196.20 --> 2197.60]  never wraps around.
[2197.76 --> 2198.22]  It's essentially
[2198.22 --> 2199.28]  infinitely sized.
[2199.52 --> 2201.20]  And then it's up to the compiler
[2201.20 --> 2202.42]  to generate good code
[2202.42 --> 2203.50]  to implement that.
[2203.50 --> 2204.08]  So,
[2204.08 --> 2205.08]  would you be able to go
[2205.08 --> 2206.20]  beyond int 64
[2206.20 --> 2208.08]  with this proposal as well?
[2208.54 --> 2208.68]  Yeah.
[2209.20 --> 2209.68]  Hmm.
[2210.24 --> 2211.88]  That's getting more interesting.
[2212.82 --> 2213.92]  Although I've never needed
[2213.92 --> 2214.76]  numbers that big,
[2215.08 --> 2215.90]  but still,
[2216.04 --> 2216.72]  I want them.
[2216.96 --> 2218.08]  It would be kind of like,
[2218.62 --> 2219.96]  I'm not sure if many of you
[2219.96 --> 2220.64]  have seen the package
[2220.64 --> 2221.80]  math slash big,
[2221.92 --> 2223.14]  but it has a big dot int
[2223.14 --> 2223.56]  in there,
[2223.66 --> 2224.88]  and that is arbitrary size.
[2225.02 --> 2225.36]  So,
[2225.40 --> 2226.74]  you can store whatever number
[2226.74 --> 2227.28]  you want in there.
[2227.60 --> 2227.86]  So,
[2227.96 --> 2228.98]  this is kind of like that,
[2229.06 --> 2229.88]  but in the language.
[2230.18 --> 2230.96]  That is a big int.
[2230.96 --> 2233.06]  You can get some really big ints
[2233.06 --> 2233.70]  in that type.
[2235.80 --> 2237.54]  I keep trying to squeeze
[2237.54 --> 2238.22]  that one in.
[2239.40 --> 2240.26]  It's massive.
[2240.44 --> 2240.78]  You can't.
[2241.28 --> 2242.66]  It's a big int.
[2243.52 --> 2244.96]  What's the biggest int
[2244.96 --> 2246.16]  you've ever used,
[2246.32 --> 2246.56]  Chris?
[2246.82 --> 2247.34]  Be honest.
[2249.34 --> 2250.76]  Have you ever gone beyond
[2250.76 --> 2251.34]  int 32?
[2252.20 --> 2253.48]  I have written things
[2253.48 --> 2254.96]  that use int 64,
[2255.14 --> 2256.18]  need to use int 64
[2256.18 --> 2257.26]  for various reasons.
[2257.82 --> 2258.66]  I do really,
[2258.98 --> 2259.12]  like,
[2259.16 --> 2260.32]  I like this proposal.
[2260.32 --> 2260.56]  Like,
[2260.60 --> 2261.60]  I'd like it if we did have
[2261.60 --> 2263.50]  more arbitrary precision things
[2263.50 --> 2264.70]  in the language itself.
[2265.04 --> 2265.30]  Like,
[2265.40 --> 2266.98]  the math dot big package
[2266.98 --> 2268.92]  is a little difficult to use.
[2269.38 --> 2270.34]  And I think there's some
[2270.34 --> 2271.38]  interesting opportunities
[2271.38 --> 2272.68]  for having kind of
[2272.68 --> 2274.22]  good arbitrary arithmetic
[2274.22 --> 2275.38]  built into the language,
[2275.62 --> 2275.76]  right?
[2275.80 --> 2275.98]  Like,
[2276.06 --> 2277.84]  adding arbitrarily big
[2277.84 --> 2278.74]  integers together,
[2279.04 --> 2280.52]  which I assume that
[2280.52 --> 2282.02]  would come with this
[2282.02 --> 2282.92]  if this proposal
[2282.92 --> 2283.52]  was accepted.
[2284.10 --> 2284.72]  I think the only
[2284.72 --> 2286.40]  maybe strange thing
[2286.40 --> 2286.96]  about this
[2286.96 --> 2287.78]  is if you were doing
[2287.78 --> 2288.64]  any bit shifting
[2288.64 --> 2289.52]  or using,
[2289.52 --> 2289.74]  like,
[2289.76 --> 2291.18]  an int as a bit mask,
[2291.18 --> 2292.16]  but you probably
[2292.16 --> 2292.78]  shouldn't have been
[2292.78 --> 2293.34]  doing that.
[2293.84 --> 2295.16]  So that's probably
[2295.16 --> 2296.12]  not an issue.
[2296.62 --> 2297.08]  But in general,
[2297.24 --> 2298.42]  I like this.
[2298.62 --> 2300.14]  I feel like the int type
[2300.14 --> 2300.82]  right now
[2300.82 --> 2301.98]  is kind of in this,
[2301.98 --> 2302.26]  like,
[2302.90 --> 2304.02]  useless space
[2304.02 --> 2304.94]  because it's like
[2304.94 --> 2306.26]  you can't really guarantee
[2306.26 --> 2308.14]  how large it's going to be
[2308.14 --> 2309.42]  if you're writing code
[2309.42 --> 2310.84]  that is cross-platform.
[2310.84 --> 2312.38]  So I think that kind of
[2312.38 --> 2313.98]  forces you to default
[2313.98 --> 2314.68]  to using,
[2314.76 --> 2314.94]  like,
[2315.02 --> 2316.30]  an int 64 and int 32
[2316.30 --> 2317.76]  or a uint 64
[2317.76 --> 2318.62]  and a uint 32.
[2319.04 --> 2319.72]  But I also think that
[2319.72 --> 2321.38]  it's good for
[2321.38 --> 2321.98]  kind of,
[2322.06 --> 2322.14]  like,
[2322.18 --> 2322.78]  if you're trying to
[2322.78 --> 2323.58]  specify a length
[2323.58 --> 2323.98]  or, like,
[2324.00 --> 2325.44]  kind of what Rob lays out
[2325.44 --> 2326.30]  in this proposal,
[2326.54 --> 2327.46]  I think that's good
[2327.46 --> 2327.96]  to know that,
[2328.00 --> 2328.16]  like,
[2328.28 --> 2329.64]  you won't overflow
[2329.64 --> 2330.58]  or you won't have
[2330.58 --> 2331.84]  that type of issue
[2331.84 --> 2332.76]  when it comes to
[2332.76 --> 2333.82]  specifying something.
[2334.14 --> 2335.12]  Or you won't,
[2335.14 --> 2335.34]  you know,
[2335.36 --> 2336.04]  have the issue of it
[2336.04 --> 2337.22]  being only 32 bits
[2337.22 --> 2337.98]  and you have
[2337.98 --> 2339.78]  a really large thing
[2339.78 --> 2340.76]  and now you've run
[2340.76 --> 2341.26]  into this problem
[2341.26 --> 2341.66]  where your code
[2341.66 --> 2342.00]  just, like,
[2342.06 --> 2342.62]  isn't working
[2342.62 --> 2343.74]  and failing in a weird way.
[2344.10 --> 2344.34]  Yeah.
[2344.90 --> 2345.58]  But what about
[2345.58 --> 2346.32]  the implications
[2346.32 --> 2347.84]  at runtime of this?
[2348.02 --> 2348.72]  Does this mean
[2348.72 --> 2350.06]  ints would be slower?
[2350.46 --> 2351.40]  Because there surely
[2351.40 --> 2352.02]  has to be some
[2352.02 --> 2352.86]  runtime element
[2352.86 --> 2353.96]  checking to see the size
[2353.96 --> 2355.18]  before you cross
[2355.18 --> 2355.66]  a threshold
[2355.66 --> 2356.52]  into needing
[2356.52 --> 2358.52]  bigger and bigger ints.
[2358.96 --> 2359.14]  Yeah.
[2359.34 --> 2360.40]  And I think that's where
[2360.40 --> 2361.46]  people sort of
[2361.46 --> 2362.60]  wave their hands
[2362.60 --> 2363.08]  a little bit
[2363.08 --> 2363.76]  and say that
[2363.76 --> 2364.62]  modern computers
[2364.62 --> 2365.20]  are good enough
[2365.20 --> 2365.76]  at this stuff.
[2366.22 --> 2366.82]  On one hand,
[2366.86 --> 2367.32]  the compiler
[2367.32 --> 2368.52]  can be smart enough
[2368.52 --> 2368.86]  to,
[2369.10 --> 2369.76]  in some cases,
[2369.78 --> 2370.42]  realize that
[2370.42 --> 2370.98]  it doesn't need
[2370.98 --> 2371.82]  to check
[2371.82 --> 2372.20]  if something
[2372.20 --> 2373.04]  will overflow.
[2373.24 --> 2373.62]  For example,
[2373.62 --> 2374.10]  if you use
[2374.10 --> 2374.44]  an integer
[2374.44 --> 2375.32]  to range
[2375.32 --> 2376.68]  over a slice,
[2377.24 --> 2377.70]  a slice
[2377.70 --> 2378.14]  is never going
[2378.14 --> 2379.22]  to be too big
[2379.22 --> 2380.02]  to not fit in memory,
[2380.18 --> 2380.90]  so that's fine.
[2381.56 --> 2382.50]  And another case
[2382.50 --> 2384.56]  is if you cannot
[2384.56 --> 2385.60]  statically
[2385.60 --> 2386.70]  know that for sure,
[2387.40 --> 2388.12]  you can also say
[2388.12 --> 2388.96]  that modern CPUs
[2388.96 --> 2389.40]  are good enough
[2389.40 --> 2390.30]  at predicting branches
[2390.30 --> 2391.30]  and say,
[2391.50 --> 2391.98]  oh, you know,
[2392.08 --> 2392.60]  this is basically
[2392.60 --> 2393.12]  never going to happen
[2393.12 --> 2393.54]  in practice,
[2393.66 --> 2394.12]  so the CPU
[2394.12 --> 2394.92]  is essentially
[2394.92 --> 2395.44]  not going to be
[2395.44 --> 2395.84]  any slower
[2395.84 --> 2396.90]  executing this code.
[2397.52 --> 2398.28]  But those are
[2398.28 --> 2398.82]  the kind of things
[2398.82 --> 2399.46]  where you would have
[2399.46 --> 2401.06]  to actually experiment
[2401.06 --> 2401.76]  with this implementation
[2401.76 --> 2402.24]  and see.
[2402.78 --> 2402.82]  Yeah.
[2403.30 --> 2403.96]  Good points.
[2404.60 --> 2405.50]  Anyone else want to
[2405.50 --> 2406.22]  say anything else
[2406.22 --> 2407.04]  about this one?
[2407.56 --> 2408.28]  I like the idea
[2408.28 --> 2410.50]  of just massive ints.
[2411.78 --> 2412.22]  Generally?
[2412.78 --> 2413.70]  Yeah, like,
[2413.96 --> 2414.92]  you need it.
[2415.10 --> 2415.70]  I don't need it,
[2415.74 --> 2416.22]  but it's like,
[2416.36 --> 2417.70]  whenever I buy a laptop,
[2417.92 --> 2419.46]  I always get the most RAM
[2419.46 --> 2420.48]  I can get.
[2421.44 --> 2422.10]  And honestly,
[2422.32 --> 2422.82]  I just,
[2423.18 --> 2423.98]  I've tried to find
[2423.98 --> 2424.60]  reasons now
[2424.60 --> 2425.44]  to use up RAM.
[2426.00 --> 2426.26]  Like,
[2426.30 --> 2427.52]  if you've got any data
[2427.52 --> 2428.18]  you want me to store
[2428.18 --> 2428.54]  for you,
[2428.62 --> 2429.20]  just let me know.
[2429.44 --> 2429.90]  Send it over.
[2430.00 --> 2431.12]  I've got loads of RAM
[2431.12 --> 2432.02]  going to waste.
[2432.78 --> 2434.28]  I do wonder as well
[2434.28 --> 2435.06]  if there's like,
[2435.12 --> 2437.02]  maybe a corollary proposal
[2437.02 --> 2437.92]  and probably already exists
[2437.92 --> 2438.56]  to have like,
[2438.66 --> 2439.80]  a float type
[2439.80 --> 2440.38]  in a language
[2440.38 --> 2441.80]  that is arbitrary precision.
[2442.28 --> 2442.66]  So I feel like
[2442.66 --> 2443.48]  that could be useful
[2443.48 --> 2444.06]  for like,
[2444.32 --> 2445.48]  perhaps financial applications
[2445.48 --> 2447.02]  where you really need
[2447.02 --> 2448.16]  that arbitrary position,
[2448.32 --> 2448.52]  like you,
[2448.78 --> 2449.52]  or arbitrary precision,
[2449.64 --> 2450.12]  you can't like,
[2450.18 --> 2451.42]  use a float 64 for money.
[2451.50 --> 2451.66]  Like,
[2451.98 --> 2453.14]  please don't use a float 64
[2453.14 --> 2453.58]  for money.
[2453.58 --> 2454.36]  That's a bad idea.
[2456.68 --> 2457.24]  And it's,
[2457.24 --> 2457.86]  it's one of those things
[2457.86 --> 2458.42]  where I always like,
[2458.46 --> 2459.76]  when I go to use a float,
[2460.06 --> 2460.68]  I'm always like,
[2460.72 --> 2460.92]  oh yeah,
[2460.98 --> 2461.26]  float.
[2461.42 --> 2461.80]  And I'm like,
[2461.84 --> 2462.04]  oh no,
[2462.08 --> 2463.36]  it has to be float 32 or 64.
[2463.48 --> 2463.60]  Like,
[2463.60 --> 2464.98]  I have to specify it.
[2465.56 --> 2466.24]  So I feel like
[2466.24 --> 2467.54]  adding that type there
[2467.54 --> 2468.92]  could also be useful
[2468.92 --> 2470.24]  if we're already going to add,
[2470.82 --> 2470.98]  like,
[2471.04 --> 2472.26]  or change how int works
[2472.26 --> 2473.26]  and how uint works.
[2473.84 --> 2474.50]  Does anybody know
[2474.50 --> 2475.52]  why we don't have that?
[2475.60 --> 2475.74]  I mean,
[2475.76 --> 2476.68]  we have it for ints.
[2476.88 --> 2477.54]  Why don't we have
[2477.54 --> 2478.34]  just a float?
[2478.86 --> 2479.32]  I don't know.
[2479.94 --> 2480.82]  I think it's a
[2480.82 --> 2481.90]  carryover from C.
[2482.52 --> 2482.72]  Hmm.
[2482.88 --> 2483.10]  Okay.
[2483.58 --> 2484.72]  Because C does have
[2484.72 --> 2485.82]  an int type,
[2486.10 --> 2487.08]  which is essentially
[2487.08 --> 2488.84]  just the machine size int,
[2488.94 --> 2489.48]  but it doesn't have
[2489.48 --> 2490.18]  the same for float.
[2490.44 --> 2491.10]  It only has,
[2491.20 --> 2491.56]  you know,
[2491.66 --> 2492.76]  single and double precision
[2492.76 --> 2493.62]  let go.
[2493.82 --> 2493.92]  Yeah,
[2493.96 --> 2494.74]  because then it's just
[2494.74 --> 2495.90]  a bit of memory,
[2495.98 --> 2496.34]  isn't it?
[2496.40 --> 2497.46]  It's just like one bit of memory,
[2497.56 --> 2498.10]  not a bit.
[2500.30 --> 2501.88]  But the machine's 32 bit,
[2502.04 --> 2503.56]  so that's what it can move around
[2503.56 --> 2504.88]  fastest.
[2505.36 --> 2506.04]  For those who are going to,
[2506.18 --> 2507.46]  going to be listening to this show,
[2507.64 --> 2509.12]  we're all making a face at Matt,
[2509.18 --> 2509.66]  right now?
[2510.30 --> 2511.10]  Shaking our heads,
[2511.14 --> 2511.32]  you know?
[2511.32 --> 2511.72]  Yeah.
[2511.94 --> 2512.16]  Okay.
[2512.16 --> 2513.52]  But they've already paid
[2513.52 --> 2515.22]  for my computer science course,
[2515.54 --> 2516.38]  so shut up.
[2517.28 --> 2517.78]  But no,
[2517.82 --> 2518.58]  I'm just saying like,
[2518.64 --> 2518.78]  yeah,
[2518.84 --> 2519.36]  it's that reason,
[2519.46 --> 2520.06]  what Daniel said.
[2520.58 --> 2522.12]  And I feel like my overall stance
[2522.12 --> 2523.18]  on this is that I like
[2523.18 --> 2524.18]  the next proposal better,
[2524.36 --> 2525.70]  which kind of aims
[2525.70 --> 2526.46]  at the same problem.
[2526.72 --> 2527.30]  So maybe we should
[2527.30 --> 2527.92]  talk about that one.
[2527.92 --> 2539.40]  This episode is brought to you
[2539.40 --> 2540.04]  by our friends
[2540.04 --> 2541.16]  at Equinix Metal,
[2541.44 --> 2542.46]  globally interconnected,
[2542.68 --> 2544.18]  fully automated bare metal.
[2544.54 --> 2545.50]  Equinix Metal gives you
[2545.50 --> 2546.76]  hardware at your fingertips
[2546.76 --> 2547.92]  with physical infrastructure
[2547.92 --> 2549.20]  at software speed.
[2549.58 --> 2550.38]  Accelerate your workloads
[2550.38 --> 2552.00]  with fully automated bare metal
[2552.00 --> 2552.76]  that's secure,
[2553.08 --> 2553.48]  powerful,
[2553.66 --> 2554.60]  and cost-effective.
[2554.60 --> 2556.32]  This is the promise
[2556.32 --> 2557.32]  of the cloud delivered
[2557.32 --> 2558.24]  on bare metal.
[2558.62 --> 2559.94]  Equinix Metal makes it easier
[2559.94 --> 2561.34]  than ever to take advantage
[2561.34 --> 2563.14]  of the unmatched global reach
[2563.14 --> 2564.44]  and connectivity ecosystem
[2564.44 --> 2565.94]  made possible by Equinix,
[2566.08 --> 2566.90]  which includes more than
[2566.90 --> 2568.08]  220 data centers
[2568.08 --> 2569.54]  across 63 metros,
[2569.82 --> 2571.20]  making interconnection easy.
[2571.54 --> 2572.26]  And they're obsessed
[2572.26 --> 2573.48]  with making bare metal
[2573.48 --> 2574.46]  even more awesome.
[2574.84 --> 2575.14]  Seriously,
[2575.28 --> 2576.08]  check out these features.
[2576.48 --> 2577.72]  60-second deploys,
[2578.14 --> 2578.94]  hourly pricing,
[2579.34 --> 2580.40]  a customer success team
[2580.40 --> 2581.70]  that engages over Slack,
[2581.70 --> 2583.32]  x86 Intel,
[2583.50 --> 2584.38]  AMD and ARM,
[2584.70 --> 2585.40]  single tenant,
[2585.76 --> 2587.80]  NVMe and SSD storage,
[2588.16 --> 2589.08]  RESTful API,
[2589.60 --> 2591.30]  first-class DevOps integrations,
[2591.74 --> 2593.02]  Equinix fabric integration,
[2593.50 --> 2594.94]  support for enterprise OSes
[2594.94 --> 2596.88]  and open-source Linux OSes,
[2597.10 --> 2598.10]  air-gapped installs
[2598.10 --> 2598.88]  without a public IP,
[2599.32 --> 2601.16]  no installed agent or keys,
[2601.52 --> 2602.74]  extensive open-source
[2602.74 --> 2603.76]  love and support,
[2604.02 --> 2604.94]  plus so much more.
[2605.22 --> 2607.16]  Visit info.equinixmetal.com
[2607.16 --> 2607.92]  slash changelog,
[2607.96 --> 2609.54]  get $500 in free credit
[2609.54 --> 2610.06]  to play with,
[2610.30 --> 2611.58]  plus a rad t-shirt.
[2611.88 --> 2612.20]  Again,
[2612.38 --> 2613.98]  info.equinixmetal.com
[2613.98 --> 2614.92]  slash changelog.
[2614.92 --> 2639.76]  So the next one
[2639.76 --> 2641.78]  talks about having new types
[2641.78 --> 2642.74]  that are stricter,
[2643.20 --> 2643.44]  right?
[2643.52 --> 2644.14]  So that you have,
[2644.36 --> 2645.72]  as well as like an int,
[2645.86 --> 2646.70]  you'd have an oint,
[2647.20 --> 2648.90]  which is a kind of overflow int
[2648.90 --> 2650.68]  or overflow protected,
[2650.80 --> 2651.12]  I guess.
[2652.00 --> 2652.24]  Or,
[2652.40 --> 2653.20]  and it would panic
[2653.20 --> 2653.72]  if it over,
[2653.92 --> 2655.10]  if it was to overflow,
[2655.24 --> 2655.42]  right?
[2655.54 --> 2657.30]  So instead of just wrapping around
[2657.30 --> 2658.20]  like Pac-Man,
[2658.52 --> 2659.16]  it would be like
[2659.16 --> 2660.82]  if Pac-Man went off the screen
[2660.82 --> 2662.84]  and never came back,
[2663.02 --> 2663.24]  right?
[2664.10 --> 2664.76]  Pretty much.
[2665.12 --> 2667.18]  And this is issue 30613,
[2667.18 --> 2668.46]  if anybody wants to check it out.
[2668.86 --> 2669.12]  Yes.
[2669.34 --> 2671.22]  So are there people
[2671.22 --> 2673.20]  that struggle with numbers
[2673.20 --> 2675.02]  and them overflowing a lot?
[2675.40 --> 2676.72]  Are there particular people
[2676.72 --> 2677.62]  that kind of,
[2678.18 --> 2679.46]  programmers that struggle
[2679.46 --> 2679.94]  with this?
[2680.06 --> 2681.52]  Because I've never come across it.
[2681.52 --> 2683.36]  So I'm going to bring up
[2683.36 --> 2684.58]  one case that's quite common
[2684.58 --> 2685.42]  with this kind of issue,
[2685.66 --> 2686.76]  overflows and underflows,
[2686.86 --> 2687.16]  that is.
[2687.26 --> 2688.28]  And it's when you
[2688.28 --> 2689.78]  implement codecs
[2689.78 --> 2691.28]  or things that have to encode
[2691.28 --> 2692.26]  or decode images,
[2692.44 --> 2692.78]  video,
[2693.12 --> 2693.40]  audio,
[2693.48 --> 2694.04]  that kind of thing.
[2694.76 --> 2696.10]  Because you can quite easily,
[2696.48 --> 2697.56]  like if you just write the code
[2697.56 --> 2698.46]  and you're not thinking about
[2698.46 --> 2699.56]  overflows and underflows,
[2700.16 --> 2701.06]  you're thinking about,
[2701.06 --> 2701.44]  you know,
[2701.54 --> 2702.46]  inputs that might be like
[2702.46 --> 2703.48]  one kilobyte in size.
[2703.72 --> 2705.02]  But what if somebody feeds you
[2705.02 --> 2705.76]  like really,
[2705.76 --> 2706.82]  really large data
[2706.82 --> 2708.12]  or something that
[2708.12 --> 2709.08]  you didn't expect?
[2709.08 --> 2709.78]  And then suddenly
[2709.78 --> 2710.98]  one little loop
[2710.98 --> 2712.40]  that looked very honest
[2712.40 --> 2712.94]  and fine,
[2713.28 --> 2714.24]  it sort of loops forever
[2714.24 --> 2715.38]  because it's overflowing
[2715.38 --> 2716.28]  and it's just looping
[2716.28 --> 2717.02]  and looping forever.
[2717.20 --> 2717.70]  And then suddenly
[2717.70 --> 2718.58]  your CPU is stuck.
[2719.88 --> 2720.36]  Yeah.
[2721.02 --> 2721.90]  Why don't you just put it
[2721.90 --> 2723.36]  all into a big int?
[2724.94 --> 2725.42]  Okay.
[2725.84 --> 2726.98]  Don't do that int idea.
[2727.44 --> 2728.90]  I won't teach computer science.
[2728.96 --> 2729.24]  Don't worry.
[2730.60 --> 2732.04]  How do you feel about this then?
[2732.16 --> 2732.36]  I mean,
[2732.38 --> 2733.04]  I feel like,
[2733.36 --> 2733.96]  you know,
[2734.02 --> 2735.56]  adding a new type like this
[2735.56 --> 2736.88]  definitely makes sense
[2736.88 --> 2737.60]  because it's completely
[2737.60 --> 2738.76]  backwards compatible.
[2740.08 --> 2741.60]  Anyone else have any
[2741.60 --> 2743.20]  strong feelings either way?
[2743.70 --> 2745.04]  I feel like this is,
[2745.72 --> 2746.36]  like this would be
[2746.36 --> 2746.90]  a good addition,
[2746.98 --> 2747.48]  especially for like
[2747.48 --> 2748.38]  the smaller ones.
[2748.48 --> 2749.16]  Like I know I've
[2749.16 --> 2750.90]  sometimes written code
[2750.90 --> 2752.18]  that needs to check
[2752.18 --> 2753.34]  for overflows
[2753.34 --> 2755.70]  and it's a bit annoying
[2755.70 --> 2757.36]  and it's a bit of verbosity
[2757.36 --> 2758.06]  and it'd be nice
[2758.06 --> 2759.16]  to just kind of like
[2759.16 --> 2761.12]  catch a panic instead
[2761.12 --> 2762.80]  as kind of bad
[2762.80 --> 2763.64]  as that is.
[2763.86 --> 2765.24]  But I think it's like
[2765.24 --> 2765.94]  pretty tricky
[2765.94 --> 2767.24]  to like kind of detect
[2767.24 --> 2768.34]  when overflows
[2768.34 --> 2769.06]  are happening.
[2769.74 --> 2770.52]  Especially if you're like
[2770.52 --> 2771.50]  just adding things
[2771.50 --> 2772.06]  to numbers
[2772.06 --> 2773.08]  and just kind of like
[2773.08 --> 2774.12]  trying to be efficient
[2774.12 --> 2775.54]  and have like clean code.
[2775.74 --> 2776.96]  But I also don't like
[2776.96 --> 2778.12]  see a downside
[2778.12 --> 2779.64]  to adding these.
[2779.74 --> 2780.46]  Like I don't know
[2780.46 --> 2781.94]  how they would be
[2781.94 --> 2783.52]  abused in some way
[2783.52 --> 2783.94]  that's like,
[2784.00 --> 2784.24]  oh no,
[2784.32 --> 2784.76]  that's like
[2784.76 --> 2786.04]  going to be such a problem.
[2786.12 --> 2787.20]  And I think if it does make
[2787.20 --> 2788.40]  writing code
[2788.40 --> 2789.40]  in some of these,
[2789.48 --> 2789.76]  you know,
[2789.96 --> 2790.80]  for like encoders
[2790.80 --> 2791.40]  or decoders
[2791.40 --> 2792.74]  or whatever other
[2792.74 --> 2793.86]  circumstances people have,
[2793.86 --> 2794.50]  it makes it easier
[2794.50 --> 2795.30]  to write that code
[2795.30 --> 2796.28]  and write that code
[2796.28 --> 2796.70]  safer,
[2796.90 --> 2797.88]  which I think is important,
[2798.28 --> 2799.28]  then I think that's
[2799.28 --> 2800.44]  worth adding
[2800.44 --> 2801.42]  to the language for,
[2801.66 --> 2801.80]  right?
[2801.86 --> 2802.54]  I think like Go
[2802.54 --> 2803.24]  is one of those
[2803.24 --> 2803.72]  languages that's like,
[2803.80 --> 2803.90]  okay,
[2803.96 --> 2804.08]  well,
[2804.16 --> 2805.86]  we're safer than C
[2805.86 --> 2806.62]  and this could be
[2806.62 --> 2807.34]  one of those things
[2807.34 --> 2807.70]  that's like,
[2807.82 --> 2808.48]  this is a way
[2808.48 --> 2809.12]  in which we are
[2809.12 --> 2809.94]  safer than C.
[2810.52 --> 2810.60]  Right.
[2811.00 --> 2811.26]  Yeah,
[2811.28 --> 2812.50]  because when it overflows,
[2812.70 --> 2813.92]  it does so silently,
[2814.06 --> 2814.42]  doesn't it?
[2814.50 --> 2814.86]  I mean,
[2815.04 --> 2815.84]  it's essentially,
[2816.50 --> 2817.42]  if there's no error
[2817.42 --> 2818.76]  and it just wraps around,
[2818.86 --> 2819.48]  you wouldn't know
[2819.48 --> 2819.98]  it's happened.
[2820.70 --> 2821.08]  And of course,
[2821.16 --> 2822.44]  that is a problem.
[2822.80 --> 2823.40]  It is a problem,
[2823.40 --> 2823.64]  yeah.
[2824.24 --> 2824.60]  Yeah,
[2824.74 --> 2825.88]  I would even say that,
[2826.16 --> 2827.30]  so I like this idea,
[2827.96 --> 2829.30]  I like both of these proposals
[2829.30 --> 2830.30]  and that they handle
[2830.30 --> 2831.36]  overflows in some way
[2831.36 --> 2831.92]  because Go
[2831.92 --> 2832.94]  doesn't have a good way
[2832.94 --> 2833.66]  to deal with those.
[2833.90 --> 2834.64]  You can't have them both
[2834.64 --> 2834.84]  though,
[2834.84 --> 2835.16]  can you?
[2835.52 --> 2835.70]  Well,
[2835.76 --> 2835.94]  right,
[2836.06 --> 2836.18]  yeah.
[2836.22 --> 2836.90]  You have to pick one.
[2837.18 --> 2837.38]  Right.
[2837.86 --> 2839.16]  So what I'm thinking is,
[2839.78 --> 2840.18]  so for example,
[2840.24 --> 2840.80]  with this proposal,
[2840.92 --> 2841.78]  you would still have to
[2841.78 --> 2842.70]  check for overflows
[2842.70 --> 2843.44]  because if you don't,
[2843.52 --> 2844.32]  your code would panic
[2844.32 --> 2845.38]  and that might not be
[2845.38 --> 2846.10]  the best idea.
[2846.24 --> 2846.80]  But the thing is,
[2846.84 --> 2847.78]  it would be a safety net
[2847.78 --> 2848.40]  of sorts.
[2848.54 --> 2849.30]  It's kind of like
[2849.30 --> 2850.18]  in Go,
[2850.50 --> 2851.28]  there are no buffer
[2851.28 --> 2851.84]  overflows
[2851.84 --> 2852.76]  because yes,
[2852.76 --> 2853.76]  you can check against them
[2853.76 --> 2854.82]  but if you forget to check them,
[2854.86 --> 2855.34]  you're going to panic.
[2855.74 --> 2856.66]  It's not like you execute
[2856.66 --> 2857.36]  arbitrary code
[2857.36 --> 2858.42]  or you hang forever
[2858.42 --> 2859.16]  and that kind of thing.
[2859.74 --> 2860.48]  So to me,
[2861.08 --> 2862.28]  this proposal feels
[2862.28 --> 2863.04]  quite Go-like
[2863.04 --> 2864.18]  but at the same time,
[2864.24 --> 2864.84]  what I don't like
[2864.84 --> 2866.32]  is that they're separate types
[2866.32 --> 2868.18]  so the user has to choose
[2868.18 --> 2868.86]  every single time
[2868.86 --> 2869.64]  which one to use
[2869.64 --> 2870.86]  and I think the default
[2870.86 --> 2872.16]  should be the safe version.
[2872.46 --> 2873.40]  It shouldn't be the weird,
[2873.60 --> 2874.12]  funky version
[2874.12 --> 2875.40]  that wraps around.
[2875.84 --> 2876.68]  That would be a backwards
[2876.68 --> 2878.04]  incompatible change though,
[2878.08 --> 2878.40]  I suppose,
[2878.48 --> 2878.84]  wouldn't it?
[2879.48 --> 2879.70]  Maybe.
[2879.70 --> 2880.46]  Maybe not
[2880.46 --> 2881.82]  because is overflowing
[2881.82 --> 2884.48]  kind of unspecified behavior
[2884.48 --> 2886.26]  or would there be people
[2886.26 --> 2887.08]  that rely on it?
[2887.68 --> 2888.50]  It is specified
[2888.50 --> 2890.00]  to wrap around
[2890.00 --> 2891.02]  in the Go spec
[2891.02 --> 2892.06]  but the thing is,
[2892.72 --> 2893.66]  does much code
[2893.66 --> 2894.74]  actually depend on that?
[2894.90 --> 2895.58]  And if they do,
[2895.86 --> 2896.68]  this could be triggered
[2896.68 --> 2898.36]  by like a new Go language version.
[2898.54 --> 2899.88]  So if your Go mod says
[2899.88 --> 2901.56]  Go when 17 or later,
[2901.74 --> 2902.28]  then suddenly
[2902.28 --> 2903.32]  in some units,
[2903.62 --> 2904.16]  they're all,
[2904.22 --> 2904.48]  you know,
[2904.76 --> 2905.86]  safe against overflow.
[2906.20 --> 2907.42]  And then if you do that upgrade
[2907.42 --> 2908.40]  and you want the overflow,
[2908.56 --> 2909.46]  you use the other type
[2909.46 --> 2910.96]  that explicitly allows you
[2910.96 --> 2911.94]  to overflow without panicking.
[2913.40 --> 2913.80]  Okay,
[2913.90 --> 2915.86]  so you would have another type
[2915.86 --> 2916.94]  but you'd flip it
[2916.94 --> 2918.38]  so that the new type
[2918.38 --> 2919.28]  had the old behavior
[2919.28 --> 2920.62]  and the default behavior
[2920.62 --> 2922.58]  was panicking overflows.
[2923.22 --> 2923.86]  Because otherwise
[2923.86 --> 2924.98]  you have to like trust
[2924.98 --> 2925.92]  that people will use
[2925.92 --> 2926.96]  this safer type
[2926.96 --> 2927.68]  and I don't think
[2927.68 --> 2928.24]  that's a good idea,
[2928.34 --> 2929.12]  especially with the amount
[2929.12 --> 2929.84]  of existing code.
[2930.12 --> 2930.28]  Yeah.
[2930.62 --> 2931.42]  That was a fair point,
[2931.48 --> 2931.84]  wasn't it, Johnny?
[2931.98 --> 2933.14]  That last point Daniel made.
[2933.50 --> 2934.00]  What do you think?
[2934.50 --> 2935.10]  I think it's fair
[2935.10 --> 2935.78]  to say it was fair.
[2935.78 --> 2936.06]  Yeah.
[2936.06 --> 2936.36]  Yeah.
[2936.90 --> 2937.96]  Oh, so I've made
[2937.96 --> 2938.58]  a fair point too.
[2939.44 --> 2940.64]  I wondered because
[2940.64 --> 2942.08]  I'm trying to see
[2942.08 --> 2943.50]  if it's actually time
[2943.50 --> 2945.90]  for our regular slot
[2945.90 --> 2947.68]  Unpopular Opinions.
[2953.02 --> 2953.78]  What?
[2954.08 --> 2954.84]  I actually think
[2954.84 --> 2955.76]  should probably leave.
[2959.00 --> 2960.96]  Unpopular Opinions.
[2964.96 --> 2965.36]  Okay.
[2966.06 --> 2967.82]  Who's going to kick us off?
[2967.88 --> 2968.44]  Does anyone have
[2968.44 --> 2969.88]  an unpopular opinion?
[2970.86 --> 2972.06]  Well, now that you bring it up.
[2972.64 --> 2973.30]  Mm-hmm.
[2973.94 --> 2974.38]  Daniel.
[2975.16 --> 2975.90]  You don't like him?
[2976.12 --> 2976.42]  You see,
[2976.74 --> 2979.02]  like usually when we have you
[2979.02 --> 2979.48]  on the show,
[2979.62 --> 2980.76]  you have one of those faces,
[2980.88 --> 2981.48]  one of those voices
[2981.48 --> 2983.18]  that is soothing to me.
[2983.54 --> 2983.82]  Right?
[2984.24 --> 2984.66]  You know,
[2984.70 --> 2986.56]  like it's a good thing,
[2986.62 --> 2986.86]  right?
[2987.74 --> 2989.04]  But you said something earlier
[2989.04 --> 2990.52]  that I want you to explain
[2990.52 --> 2991.20]  a little bit more
[2991.20 --> 2993.70]  about why channels
[2993.70 --> 2994.56]  are a foot gun
[2994.56 --> 2995.90]  and go.
[2996.38 --> 2997.28]  What did he say?
[2997.80 --> 2998.52]  He said channels
[2998.52 --> 2999.18]  are a foot gun.
[2999.66 --> 2999.86]  Yeah.
[2999.96 --> 3001.06]  We're talking about ranging
[3001.06 --> 3002.16]  and I said that,
[3002.22 --> 3002.40]  you know,
[3002.44 --> 3003.48]  people use channels
[3003.48 --> 3004.58]  for ranges
[3004.58 --> 3005.50]  as a sort of iterator
[3005.50 --> 3006.02]  and I said,
[3006.02 --> 3007.02]  I think channels
[3007.02 --> 3007.94]  are probably the biggest
[3007.94 --> 3008.68]  foot gun and go.
[3009.08 --> 3010.06]  And I think that's what
[3010.06 --> 3010.94]  probably triggered
[3010.94 --> 3012.06]  every action.
[3012.06 --> 3014.22]  He certainly did that.
[3014.42 --> 3015.06]  He's livid.
[3016.06 --> 3016.78]  What's the phrase
[3016.78 --> 3017.28]  you're using?
[3017.74 --> 3018.86]  As my unpopular opinion,
[3019.10 --> 3019.42]  you mean?
[3019.92 --> 3020.42]  No, no.
[3020.60 --> 3021.24]  The food gun
[3021.24 --> 3021.68]  you're saying,
[3021.84 --> 3022.04]  right?
[3022.58 --> 3023.12]  Foot gun.
[3023.44 --> 3023.62]  Yeah.
[3024.12 --> 3024.70]  What's that?
[3024.82 --> 3025.42]  What's that about?
[3025.96 --> 3026.72]  Can someone explain that
[3026.72 --> 3027.38]  for anyone who's never
[3027.38 --> 3028.00]  heard it before?
[3028.42 --> 3028.76]  Oh.
[3029.24 --> 3030.06]  It's basically like
[3030.06 --> 3030.64]  if you have,
[3030.72 --> 3031.02]  you know,
[3031.06 --> 3031.72]  a gun,
[3032.22 --> 3032.52]  it's,
[3032.68 --> 3032.90]  you know,
[3033.00 --> 3033.68]  usually you're trying
[3033.68 --> 3034.66]  to shoot other things
[3034.66 --> 3035.08]  with it,
[3035.14 --> 3035.72]  but instead,
[3035.96 --> 3036.30]  you know,
[3036.34 --> 3037.04]  it's going to hit you
[3037.04 --> 3037.50]  in the foot
[3037.50 --> 3038.30]  and that's back.
[3038.80 --> 3039.00]  Oh,
[3039.16 --> 3040.16]  foot gun.
[3040.70 --> 3040.94]  Yeah.
[3040.94 --> 3041.88]  What did you think
[3041.88 --> 3042.44]  we were saying?
[3042.72 --> 3043.52]  Food gun?
[3043.54 --> 3044.00]  I thought you were
[3044.00 --> 3044.72]  saying food gun.
[3045.08 --> 3045.54]  Like I'm going to
[3045.54 --> 3047.02]  launch a burger
[3047.02 --> 3047.98]  straight at your mouth
[3047.98 --> 3048.26]  or something?
[3048.56 --> 3049.30]  I couldn't figure out
[3049.30 --> 3050.60]  if it shot food out
[3050.60 --> 3051.62]  or if you used it
[3051.62 --> 3052.64]  for shooting food.
[3054.40 --> 3055.48]  I'm going to
[3055.48 --> 3056.48]  shoot up some food
[3056.48 --> 3058.30]  in the range today?
[3059.04 --> 3059.56]  Oh, man.
[3060.86 --> 3061.34]  This is,
[3061.46 --> 3061.64]  yeah,
[3061.72 --> 3062.06]  I mean,
[3063.14 --> 3063.66]  do you want
[3063.66 --> 3064.60]  a language proposal?
[3064.86 --> 3065.86]  I propose that
[3065.86 --> 3067.84]  my American cousins
[3067.84 --> 3069.32]  pronounce their T's
[3069.32 --> 3069.94]  a little more
[3069.94 --> 3070.84]  and then
[3070.84 --> 3071.70]  wouldn't get in
[3071.70 --> 3072.30]  this mess?
[3072.86 --> 3073.56]  That's a language
[3073.56 --> 3074.58]  proposal for me.
[3075.48 --> 3076.00]  I'm going to
[3076.00 --> 3076.80]  actually open that.
[3077.88 --> 3078.86]  Can you open
[3078.86 --> 3079.86]  PRs for America?
[3082.72 --> 3083.50]  Oh, man.
[3083.60 --> 3083.80]  Okay,
[3083.94 --> 3084.22]  Daniel,
[3084.30 --> 3085.22]  do you have a real
[3085.22 --> 3086.22]  unpopular opinion?
[3086.94 --> 3087.32]  Yeah,
[3087.76 --> 3088.28]  I guess so.
[3088.40 --> 3089.18]  My unpopular opinion
[3089.18 --> 3090.18]  is that
[3090.18 --> 3091.48]  Go as a language
[3091.48 --> 3092.76]  should be frozen
[3092.76 --> 3093.70]  again at some point
[3093.70 --> 3094.68]  over the next few years.
[3095.10 --> 3095.24]  You know,
[3095.28 --> 3096.22]  we've had a couple
[3096.22 --> 3096.90]  of years where
[3096.90 --> 3097.92]  new features
[3097.92 --> 3099.34]  have been added in,
[3099.34 --> 3100.42]  especially big ones
[3100.42 --> 3101.14]  are being considered
[3101.14 --> 3101.74]  like generics.
[3102.14 --> 3103.28]  I want to see that
[3103.28 --> 3104.12]  slow down again
[3104.12 --> 3105.26]  like it was for like
[3105.26 --> 3106.52]  six or seven years
[3106.52 --> 3107.72]  after Go 1.0
[3107.72 --> 3108.10]  came out.
[3108.62 --> 3108.86]  You're like,
[3108.94 --> 3109.14]  yeah,
[3109.26 --> 3110.24]  you've had your fun.
[3110.96 --> 3112.34]  You've gone too far.
[3112.58 --> 3113.28]  It's time
[3113.28 --> 3114.56]  to take a step back.
[3115.12 --> 3115.46]  Why?
[3115.84 --> 3117.06]  It's a mix of reasons.
[3117.28 --> 3118.24]  On one hand,
[3118.36 --> 3119.26]  I feel like
[3119.26 --> 3120.40]  Go succeeded
[3120.40 --> 3120.88]  the most
[3120.88 --> 3121.68]  when it was stable.
[3122.18 --> 3122.34]  You know,
[3122.40 --> 3123.16]  a lot of the
[3123.16 --> 3124.20]  amazing software
[3124.20 --> 3125.00]  that came out in Go
[3125.00 --> 3126.24]  was conceived
[3126.24 --> 3127.06]  while Go was
[3127.06 --> 3128.02]  essentially frozen
[3128.02 --> 3128.62]  as a language.
[3129.28 --> 3130.10]  And I feel like
[3130.10 --> 3131.02]  if Go keeps growing
[3131.02 --> 3131.46]  and growing,
[3131.62 --> 3132.00]  it's not like
[3132.00 --> 3132.34]  it's growing
[3132.34 --> 3133.36]  very fast at the moment,
[3133.40 --> 3134.22]  but if it keeps
[3134.22 --> 3135.38]  the upward pace
[3135.38 --> 3136.20]  like that,
[3136.32 --> 3137.06]  I feel like
[3137.06 --> 3138.04]  it might lose
[3138.04 --> 3138.82]  this good quality
[3138.82 --> 3139.78]  of just,
[3140.04 --> 3140.28]  you know,
[3140.32 --> 3140.90]  being chill
[3140.90 --> 3141.60]  and letting other
[3141.60 --> 3142.52]  languages experiment
[3142.52 --> 3143.44]  and then just
[3143.44 --> 3144.50]  taking the good bits
[3144.50 --> 3146.44]  and being a small language.
[3147.76 --> 3148.16]  Interesting.
[3148.86 --> 3149.22]  Well,
[3149.50 --> 3150.20]  what do you think
[3150.20 --> 3150.74]  of that, Chris?
[3151.14 --> 3151.94]  I think that's popular.
[3152.08 --> 3152.60]  I think that's
[3152.60 --> 3154.26]  something I would
[3154.26 --> 3154.80]  like to see.
[3154.96 --> 3155.58]  I feel like,
[3155.74 --> 3156.22]  especially over the
[3156.22 --> 3156.82]  last couple years,
[3156.92 --> 3157.78]  we've had some,
[3158.32 --> 3158.68]  I don't think
[3158.68 --> 3159.48]  they're missteps,
[3159.70 --> 3160.26]  but I feel like
[3160.26 --> 3161.34]  we've been moving
[3161.34 --> 3163.16]  a little bit too fast
[3163.16 --> 3164.28]  with like the sense
[3164.28 --> 3164.74]  of urgency.
[3164.86 --> 3165.40]  I think modules
[3165.40 --> 3166.84]  is a pretty decent
[3166.84 --> 3167.56]  example of that.
[3167.68 --> 3168.48]  I feel like
[3168.48 --> 3169.36]  the end result
[3169.36 --> 3170.10]  has been good.
[3170.62 --> 3171.28]  I think there was
[3171.28 --> 3171.76]  a need,
[3171.92 --> 3172.50]  but I feel like
[3172.50 --> 3173.66]  there was a lot
[3173.66 --> 3174.26]  of stuff
[3174.26 --> 3175.04]  with modules
[3175.04 --> 3175.82]  that was like,
[3176.26 --> 3176.38]  oh,
[3176.46 --> 3177.18]  how are we
[3177.18 --> 3177.88]  actually going
[3177.88 --> 3178.60]  to make this work?
[3178.68 --> 3179.04]  How are we going
[3179.04 --> 3179.66]  to get the tooling
[3179.66 --> 3180.80]  to be there
[3180.80 --> 3181.74]  for modules?
[3181.98 --> 3182.14]  I mean,
[3182.24 --> 3183.46]  now I think
[3183.46 --> 3183.90]  the tooling's
[3183.90 --> 3184.30]  pretty solid,
[3184.30 --> 3184.82]  but there were
[3184.82 --> 3185.86]  a few really
[3185.86 --> 3186.50]  rough years
[3186.50 --> 3186.90]  of like,
[3187.58 --> 3188.62]  what does my editor
[3188.62 --> 3189.76]  install look like?
[3189.84 --> 3190.80]  How do I operate
[3190.80 --> 3191.92]  in both modules
[3191.92 --> 3193.14]  and with GoPath?
[3193.24 --> 3193.82]  How do I
[3193.82 --> 3194.48]  kind of
[3194.48 --> 3195.84]  make both of
[3195.84 --> 3196.78]  these two worlds
[3196.78 --> 3197.96]  that need to exist
[3197.96 --> 3198.88]  for various reasons
[3198.88 --> 3199.90]  actually work?
[3200.36 --> 3201.02]  I think that,
[3201.12 --> 3201.28]  yeah,
[3201.34 --> 3202.34]  slowing down some,
[3202.54 --> 3203.96]  letting other people
[3203.96 --> 3205.38]  experiment for a bit
[3205.38 --> 3206.92]  and really stabilizing
[3206.92 --> 3207.36]  the language
[3207.36 --> 3208.70]  would be a good idea.
[3208.70 --> 3210.26]  I think the main
[3210.26 --> 3211.10]  reason why this
[3211.10 --> 3211.98]  opinion might be
[3211.98 --> 3212.36]  unpopular
[3212.36 --> 3213.40]  is because it
[3213.40 --> 3214.10]  means that a lot
[3214.10 --> 3214.78]  of the proposals
[3214.78 --> 3215.52]  that people have
[3215.52 --> 3216.44]  filed for the language
[3216.44 --> 3218.00]  might not make it
[3218.00 --> 3219.72]  because if we stop
[3219.72 --> 3220.20]  at some point
[3220.20 --> 3221.12]  for another five
[3221.12 --> 3221.76]  years or so,
[3221.90 --> 3222.82]  that means the
[3222.82 --> 3223.44]  proposals are going
[3223.44 --> 3224.10]  to keep coming in,
[3224.20 --> 3225.20]  but they're either
[3225.20 --> 3225.88]  going to be rejected
[3225.88 --> 3226.46]  or,
[3226.56 --> 3226.92]  you know,
[3227.16 --> 3227.74]  put on hold,
[3227.96 --> 3229.06]  which might be
[3229.06 --> 3229.94]  frustrating for some.
[3230.70 --> 3230.92]  Right.
[3231.36 --> 3231.72]  Hmm.
[3232.44 --> 3232.78]  Well,
[3233.36 --> 3233.62]  good,
[3233.74 --> 3234.16]  strong point.
[3234.22 --> 3234.86]  Then we'll certainly
[3234.86 --> 3235.94]  be testing that
[3235.94 --> 3236.92]  unpopular opinion
[3236.92 --> 3238.44]  on our Twitter feed
[3238.44 --> 3239.76]  at GoTimeFM
[3239.76 --> 3240.84]  and we actually
[3240.84 --> 3241.36]  do a poll
[3241.36 --> 3242.20]  and find out
[3242.20 --> 3242.90]  if it is indeed
[3242.90 --> 3244.70]  unpopular or not.
[3245.42 --> 3246.46]  Does anybody else
[3246.46 --> 3247.20]  have an unpopular
[3247.20 --> 3247.66]  opinion?
[3248.42 --> 3248.72]  I have,
[3248.86 --> 3249.14]  I guess,
[3249.24 --> 3250.66]  a somewhat related
[3250.66 --> 3251.66]  one to what
[3251.66 --> 3252.18]  Daniel said.
[3252.46 --> 3253.14]  Is it unpopular?
[3253.32 --> 3253.76]  Because that's all
[3253.76 --> 3254.24]  I care about.
[3254.26 --> 3255.14]  I think so.
[3255.34 --> 3255.58]  Right.
[3255.68 --> 3256.02]  Well then,
[3256.12 --> 3256.42]  proceed.
[3257.84 --> 3259.00]  I don't think
[3259.00 --> 3260.38]  we're ever going
[3260.38 --> 3261.30]  to fix the
[3261.30 --> 3262.30]  V2 Plus
[3262.30 --> 3263.40]  module problem
[3263.40 --> 3264.44]  in the language.
[3264.78 --> 3264.88]  Like,
[3264.90 --> 3265.50]  I think we're stuck
[3265.50 --> 3265.90]  with that.
[3266.06 --> 3266.08]  Oh,
[3266.08 --> 3266.68]  get over it.
[3266.92 --> 3269.36]  Because I think
[3269.36 --> 3269.58]  like,
[3269.70 --> 3270.32]  you know,
[3270.52 --> 3271.06]  I think anyone
[3271.06 --> 3271.66]  that's experienced
[3271.66 --> 3272.56]  like a package
[3272.56 --> 3273.66]  or a module
[3273.66 --> 3274.18]  that has like
[3274.18 --> 3275.28]  a V5 version
[3275.28 --> 3275.92]  but also at one
[3275.92 --> 3276.72]  point had like,
[3276.82 --> 3277.62]  one point was
[3277.62 --> 3278.44]  like a GoPath
[3278.44 --> 3279.38]  or like
[3279.38 --> 3280.18]  incompatible
[3280.18 --> 3280.76]  and now they're
[3280.76 --> 3281.48]  like just trying
[3281.48 --> 3282.18]  to import it
[3282.18 --> 3282.96]  and like the
[3282.96 --> 3283.44]  tooling's just
[3283.44 --> 3283.60]  like,
[3283.70 --> 3283.80]  oh,
[3283.86 --> 3284.30]  of course you
[3284.30 --> 3285.24]  meant like V1,
[3285.42 --> 3286.62]  not V5,
[3286.72 --> 3287.04]  which is the
[3287.04 --> 3287.26]  latest.
[3287.64 --> 3288.20]  I think we
[3288.20 --> 3289.02]  might find ways
[3289.02 --> 3290.26]  to like make
[3290.26 --> 3291.10]  that a little
[3291.10 --> 3292.26]  bit less rough,
[3292.26 --> 3293.28]  but I think
[3293.28 --> 3294.28]  that's an inherent
[3294.28 --> 3295.18]  design flaw
[3295.18 --> 3296.92]  in how
[3296.92 --> 3297.54]  that whole
[3297.54 --> 3298.24]  semantic
[3298.24 --> 3299.24]  import versioning
[3299.24 --> 3299.92]  was constructed.
[3300.24 --> 3300.88]  And I think
[3300.88 --> 3301.18]  we're just
[3301.18 --> 3301.80]  more or less
[3301.80 --> 3302.46]  stuck with it
[3302.46 --> 3303.22]  at this point.
[3303.38 --> 3304.22]  I saw a very
[3304.22 --> 3305.42]  popular project
[3305.42 --> 3306.70]  or actually
[3306.70 --> 3307.42]  GORM.
[3307.62 --> 3308.36]  Their approach
[3308.36 --> 3309.00]  was to basically
[3309.00 --> 3309.20]  say,
[3309.28 --> 3309.60]  you know what,
[3310.12 --> 3311.06]  the old code base,
[3311.20 --> 3311.66]  the supposed
[3311.66 --> 3312.62]  version one
[3312.62 --> 3313.28]  of this thing,
[3313.38 --> 3313.80]  we're going to
[3313.80 --> 3314.14]  move that
[3314.14 --> 3314.80]  into a separate
[3314.80 --> 3316.20]  branch altogether.
[3316.20 --> 3317.54]  basically they
[3317.54 --> 3318.56]  just skirted
[3318.56 --> 3318.86]  the issue
[3318.86 --> 3319.44]  all together
[3319.44 --> 3319.82]  by basically
[3319.82 --> 3320.08]  saying,
[3320.22 --> 3320.34]  hey,
[3320.44 --> 3320.86]  when you
[3320.86 --> 3321.46]  pull,
[3321.62 --> 3321.90]  right,
[3322.02 --> 3322.62]  our V1
[3322.62 --> 3322.96]  now,
[3323.04 --> 3323.36]  so whatever
[3323.36 --> 3324.18]  our V2
[3324.18 --> 3325.44]  new features
[3325.44 --> 3325.82]  and everything
[3325.82 --> 3326.30]  else that was
[3326.30 --> 3326.68]  supposed to be
[3326.68 --> 3327.04]  V2,
[3327.12 --> 3327.38]  we're not going
[3327.38 --> 3327.62]  to put that
[3327.62 --> 3328.34]  behind a V2
[3328.34 --> 3330.36]  module path,
[3330.44 --> 3330.56]  right?
[3330.94 --> 3332.10]  Now when you
[3332.10 --> 3332.70]  pull it down,
[3332.80 --> 3333.10]  that's what
[3333.10 --> 3333.54]  you're getting,
[3333.66 --> 3333.82]  right?
[3333.86 --> 3334.48]  So they
[3334.48 --> 3335.08]  basically skirted
[3335.08 --> 3335.68]  the whole issue
[3335.68 --> 3336.12]  by basically
[3336.12 --> 3336.60]  saying the
[3336.60 --> 3337.16]  latest stuff
[3337.16 --> 3338.32]  is the V1
[3338.32 --> 3338.72]  now.
[3338.90 --> 3339.18]  And then they
[3339.18 --> 3339.48]  just say,
[3339.62 --> 3339.92]  if you want
[3339.92 --> 3340.44]  the other stuff,
[3340.50 --> 3341.08]  then lock to
[3341.08 --> 3342.28]  a commit hash
[3342.28 --> 3342.72]  or something,
[3343.10 --> 3343.66]  find another
[3343.66 --> 3344.36]  way to do it,
[3344.40 --> 3344.54]  right?
[3344.54 --> 3345.42]  So honestly,
[3345.62 --> 3346.80]  I think that's
[3346.80 --> 3348.32]  a nice way,
[3348.84 --> 3349.14]  right,
[3349.20 --> 3349.86]  to actually get
[3349.86 --> 3350.16]  around the
[3350.16 --> 3350.48]  problem.
[3351.16 --> 3351.78]  Although it
[3351.78 --> 3353.32]  may rob some
[3353.32 --> 3353.62]  people the
[3353.62 --> 3354.00]  wrong way,
[3354.08 --> 3354.36]  but I think
[3354.36 --> 3354.64]  that was a
[3354.64 --> 3355.08]  nice way of
[3355.08 --> 3355.52]  actually getting
[3355.52 --> 3355.84]  around the
[3355.84 --> 3356.34]  problem rather
[3356.34 --> 3356.88]  than introducing
[3356.88 --> 3357.42]  a V2
[3357.42 --> 3358.52]  in the path.
[3359.58 --> 3360.20]  It's a bit
[3360.20 --> 3360.88]  of work for
[3360.88 --> 3361.82]  maintainers because
[3361.82 --> 3362.30]  suddenly they
[3362.30 --> 3363.40]  might build
[3363.40 --> 3364.00]  their code one
[3364.00 --> 3364.34]  day and it
[3364.34 --> 3364.90]  doesn't build
[3364.90 --> 3365.98]  because they've
[3365.98 --> 3366.42]  made breaking
[3366.42 --> 3366.88]  changes,
[3367.14 --> 3368.46]  but with a
[3368.46 --> 3369.76]  relatively simple
[3369.76 --> 3370.20]  fix,
[3370.26 --> 3370.70]  which is just
[3370.70 --> 3371.20]  change your
[3371.20 --> 3372.60]  reports or fix
[3372.60 --> 3373.18]  your go mod
[3373.18 --> 3373.50]  or whatever.
[3374.54 --> 3375.80]  Interesting
[3375.80 --> 3376.28]  approach.
[3376.94 --> 3377.32]  Has anyone
[3377.32 --> 3377.74]  got any
[3377.74 --> 3378.16]  views on
[3378.16 --> 3378.42]  that?
[3378.42 --> 3378.96]  I think
[3378.96 --> 3379.38]  semantic
[3379.38 --> 3379.70]  import
[3379.70 --> 3380.32]  versioning
[3380.32 --> 3380.98]  had to
[3380.98 --> 3381.36]  happen
[3381.36 --> 3381.80]  because
[3381.80 --> 3382.16]  otherwise
[3382.16 --> 3383.10]  it wouldn't
[3383.10 --> 3383.70]  be impossible
[3383.70 --> 3384.34]  to have
[3384.34 --> 3384.76]  semantic
[3384.76 --> 3385.32]  versioning
[3385.32 --> 3386.64]  work at
[3386.64 --> 3387.22]  large scale
[3387.22 --> 3387.82]  because,
[3387.94 --> 3388.20]  for example,
[3388.30 --> 3388.60]  with the
[3388.60 --> 3389.60]  Gorham case,
[3390.06 --> 3390.68]  if I depend
[3390.68 --> 3391.02]  on one
[3391.02 --> 3391.52]  library that
[3391.52 --> 3391.92]  wants an
[3391.92 --> 3392.52]  old version
[3392.52 --> 3393.46]  and I depend
[3393.46 --> 3393.82]  on another
[3393.82 --> 3394.38]  library that
[3394.38 --> 3394.72]  wants a
[3394.72 --> 3395.32]  newer version,
[3395.94 --> 3396.60]  if both
[3396.60 --> 3397.12]  are the
[3397.12 --> 3398.04]  same version
[3398.04 --> 3398.64]  one module,
[3398.82 --> 3399.12]  there's a
[3399.12 --> 3399.42]  clash.
[3399.58 --> 3399.94]  There's like
[3399.94 --> 3400.54]  a diamond
[3400.54 --> 3401.32]  dependency
[3401.32 --> 3401.68]  problem.
[3401.68 --> 3402.62]  I can't
[3402.62 --> 3402.98]  build with
[3402.98 --> 3403.50]  both versions
[3403.50 --> 3403.80]  at the
[3403.80 --> 3404.14]  same time
[3404.14 --> 3404.50]  because they're
[3404.50 --> 3404.84]  the same
[3404.84 --> 3405.18]  module.
[3405.82 --> 3406.42]  That's what
[3406.42 --> 3407.34]  version 2 plus
[3407.34 --> 3407.86]  is meant to
[3407.86 --> 3408.10]  fix.
[3408.22 --> 3408.50]  You can
[3408.50 --> 3409.04]  build with
[3409.04 --> 3409.54]  version 1
[3409.54 --> 3410.04]  and 2 at
[3410.04 --> 3410.28]  the same
[3410.28 --> 3410.56]  time.
[3411.24 --> 3412.52]  I see Chris's
[3412.52 --> 3412.80]  point.
[3413.22 --> 3414.08]  We are stuck
[3414.08 --> 3414.64]  with this
[3414.64 --> 3415.90]  version 0 and 1
[3415.90 --> 3416.36]  are special
[3416.36 --> 3416.82]  problem,
[3417.46 --> 3418.02]  but I think
[3418.02 --> 3418.80]  it's mostly
[3418.80 --> 3419.12]  going to get
[3419.12 --> 3419.78]  better with
[3419.78 --> 3420.42]  better tooling
[3420.42 --> 3421.06]  like package
[3421.06 --> 3421.32]  site.
[3421.88 --> 3422.48]  Package site,
[3422.56 --> 3422.90]  for example,
[3423.04 --> 3424.04]  now, if you
[3424.04 --> 3424.82]  look at the
[3424.82 --> 3425.44]  docs for version
[3425.44 --> 3426.74]  1 and version
[3426.74 --> 3427.20]  3 is the
[3427.20 --> 3427.76]  latest table,
[3427.92 --> 3428.36]  it tells you,
[3428.48 --> 3429.38]  hey, did you
[3429.38 --> 3429.96]  notice that you're
[3429.96 --> 3430.34]  not on the
[3430.34 --> 3430.90]  latest version?
[3431.28 --> 3431.74]  And that's
[3431.74 --> 3432.40]  kind of a
[3432.40 --> 3433.50]  hint that users
[3433.50 --> 3434.06]  should be getting
[3434.06 --> 3434.76]  moving forward.
[3435.80 --> 3436.24]  Nice.
[3436.36 --> 3436.68]  And by the way,
[3436.72 --> 3437.08]  for anyone who
[3437.08 --> 3437.36]  doesn't know,
[3437.44 --> 3437.84]  a diamond
[3437.84 --> 3439.52]  dependency thing
[3439.52 --> 3440.42]  is not good.
[3440.68 --> 3441.30]  Sounds good,
[3441.36 --> 3441.78]  it's not.
[3442.98 --> 3443.62]  Shiny and
[3443.62 --> 3444.04]  expensive.
[3444.16 --> 3444.56]  Sounds like
[3444.56 --> 3445.22]  you've unlocked
[3445.22 --> 3445.82]  an achievement.
[3446.26 --> 3446.44]  Yeah.
[3447.14 --> 3447.54]  It's like,
[3447.66 --> 3448.80]  congratulations,
[3449.18 --> 3450.00]  achievement unlocked.
[3450.32 --> 3450.86]  You've got a
[3450.86 --> 3451.80]  diamond dependency
[3451.80 --> 3452.36]  problem.
[3452.68 --> 3453.40]  It'd be cool if
[3453.40 --> 3453.84]  it was like that.
[3453.84 --> 3455.04]  I also feel like
[3455.04 --> 3455.70]  for the next
[3455.70 --> 3456.46]  couple of years,
[3456.54 --> 3456.96]  it's going to be
[3456.96 --> 3457.92]  rough on people
[3457.92 --> 3458.82]  that were already
[3458.82 --> 3460.44]  on v2 when
[3460.44 --> 3460.94]  it was like
[3460.94 --> 3461.36]  kind of like
[3461.36 --> 3461.96]  using DAP
[3461.96 --> 3462.52]  or using some
[3462.52 --> 3463.10]  other system.
[3463.28 --> 3463.64]  And now they're
[3463.64 --> 3464.16]  like, I want to
[3464.16 --> 3464.78]  upgrade to modules
[3464.78 --> 3465.16]  and it's like,
[3465.88 --> 3466.44]  you have to go
[3466.44 --> 3467.14]  rewrite your entire,
[3467.48 --> 3468.48]  like, you can do
[3468.48 --> 3469.08]  it automatically,
[3469.18 --> 3469.50]  but you have to
[3469.50 --> 3470.52]  go to every
[3470.52 --> 3471.28]  single import
[3471.28 --> 3471.88]  path in your
[3471.88 --> 3473.00]  entire code base
[3473.00 --> 3474.42]  and update them.
[3475.00 --> 3475.94]  And that can be
[3475.94 --> 3476.98]  a lift for some
[3476.98 --> 3477.78]  people, for sure.
[3477.88 --> 3478.52]  That's like a big
[3478.52 --> 3479.04]  change, especially
[3479.04 --> 3479.78]  if you have like
[3479.78 --> 3480.96]  a monolith of
[3480.96 --> 3481.50]  some sort.
[3481.70 --> 3482.80]  Like, it can be
[3482.80 --> 3482.96]  difficult.
[3483.06 --> 3483.40]  I have a friend
[3483.40 --> 3484.04]  that has this
[3484.04 --> 3485.10]  like exact problem
[3485.10 --> 3485.72]  at work and he's
[3485.72 --> 3486.18]  just like, I'm
[3486.18 --> 3486.82]  just hanging on to
[3486.82 --> 3487.62]  go path for dear
[3487.62 --> 3489.18]  life until it is
[3489.18 --> 3490.90]  very, very dead
[3490.90 --> 3492.00]  and gone and we
[3492.00 --> 3493.70]  have to deal with
[3493.70 --> 3495.00]  modules and it's
[3495.00 --> 3496.54]  going to be a lift
[3496.54 --> 3496.96]  because they've,
[3497.02 --> 3498.28]  they've tried and
[3498.28 --> 3499.04]  they've tried to do
[3499.04 --> 3499.68]  the upgrade and it
[3499.68 --> 3500.52]  just like didn't work
[3500.52 --> 3501.32]  out well for them.
[3501.58 --> 3502.50]  So, and maybe
[3502.50 --> 3503.06]  there's something we
[3503.06 --> 3504.32]  can do to alleviate
[3504.32 --> 3505.54]  that, but I think
[3505.54 --> 3506.18]  that's also going to
[3506.18 --> 3507.08]  be like a struggle
[3507.08 --> 3507.80]  for some people.
[3508.46 --> 3508.68]  Brilliant.
[3509.60 --> 3510.52]  Anyone want to say
[3510.52 --> 3510.96]  anything else?
[3511.44 --> 3512.02]  So I'm just going to
[3512.02 --> 3513.04]  wind up.
[3513.36 --> 3513.66]  I don't know why I
[3513.66 --> 3513.92]  say that.
[3513.92 --> 3514.62]  Hopefully that gets
[3514.62 --> 3515.06]  cut out.
[3515.18 --> 3516.22]  It's a silly thing
[3516.22 --> 3516.92]  for me to announce
[3516.92 --> 3517.42]  on it.
[3517.58 --> 3518.40]  Plus this is live,
[3518.52 --> 3520.54]  so sometimes we go
[3520.54 --> 3521.74]  meta, don't we?
[3521.78 --> 3522.38]  And we talk about
[3522.38 --> 3522.96]  what we're talking
[3522.96 --> 3523.66]  about instead of
[3523.66 --> 3524.42]  just talking about
[3524.42 --> 3525.20]  the thing we're
[3525.20 --> 3525.74]  meant to be talking
[3525.74 --> 3526.00]  about.
[3526.18 --> 3526.78]  I do anyway.
[3527.44 --> 3528.14]  This is one of
[3528.14 --> 3528.60]  those times.
[3528.94 --> 3530.06]  It's time to say
[3530.06 --> 3530.90]  goodbye, I'm afraid.
[3531.06 --> 3532.14]  I really hope you
[3532.14 --> 3533.74]  enjoyed going through
[3533.74 --> 3534.88]  these proposals with
[3534.88 --> 3535.12]  us.
[3535.66 --> 3536.30]  And there's actually
[3536.30 --> 3538.14]  so many more.
[3538.36 --> 3539.10]  Daniel, you'll have
[3539.10 --> 3540.44]  to come back very
[3540.44 --> 3541.82]  soon and we'll do a
[3541.82 --> 3542.62]  part two of this
[3542.62 --> 3544.44]  episode and talk
[3544.44 --> 3545.24]  about some more
[3545.24 --> 3546.42]  proposals to the
[3546.42 --> 3546.98]  Go language.
[3547.46 --> 3548.72]  I'd also love if we
[3548.72 --> 3549.92]  could find some kind
[3549.92 --> 3550.78]  of bonkers ones.
[3550.88 --> 3551.32]  I don't want to be
[3551.32 --> 3552.14]  mean to anyone.
[3552.92 --> 3553.64]  Definitely not.
[3553.76 --> 3555.18]  But I'd love to see
[3555.18 --> 3555.80]  some that are like
[3555.80 --> 3557.32]  really out there as
[3557.32 --> 3557.52]  well.
[3557.58 --> 3558.20]  If we could find
[3558.20 --> 3559.22]  some of those, if
[3559.22 --> 3559.96]  anyone knows of any,
[3560.04 --> 3560.94]  please send them in
[3560.94 --> 3562.52]  on a stamped address
[3562.52 --> 3564.16]  envelope or postcard
[3564.16 --> 3565.06]  or whatever they used
[3565.06 --> 3565.68]  to do in the old
[3565.68 --> 3565.80]  days.
[3565.80 --> 3566.16]  Bonkers?
[3566.26 --> 3566.56]  You mean like
[3566.56 --> 3566.98]  generics?
[3567.92 --> 3569.76]  Oh, sorry.
[3571.26 --> 3571.92]  Sorry, I'm just
[3571.92 --> 3572.52]  yanking your chain.
[3572.86 --> 3573.50]  That was great.
[3573.80 --> 3574.58]  Now that's going in
[3574.58 --> 3574.84]  there.
[3575.24 --> 3576.02]  That one's definitely
[3576.02 --> 3576.54]  going to be made
[3576.54 --> 3578.22]  into a wrap or
[3578.22 --> 3580.82]  into put into some
[3580.82 --> 3581.58]  sample somewhere.
[3582.50 --> 3582.98]  Hopefully.
[3583.66 --> 3584.38]  Thank you so much
[3584.38 --> 3585.58]  to our guests.
[3586.26 --> 3587.12]  Johnny Borsico.
[3587.78 --> 3588.38]  Goodbye, Johnny.
[3588.58 --> 3589.56]  Have a lovely time.
[3590.32 --> 3590.76]  Live long and
[3590.76 --> 3591.02]  prosper.
[3591.54 --> 3592.02]  I can't do it.
[3593.28 --> 3593.44]  Yeah.
[3593.98 --> 3594.76]  Can't do it.
[3595.56 --> 3596.46]  Are there like
[3596.46 --> 3597.48]  Vulcan kids that
[3597.48 --> 3598.36]  can't do that?
[3598.44 --> 3598.84]  And they're like,
[3598.96 --> 3600.06]  oh, and it's like,
[3600.24 --> 3601.06]  there's like a stigma
[3601.06 --> 3601.90]  about it and stuff.
[3601.90 --> 3602.26]  And they're like,
[3602.40 --> 3603.48]  oh, live long and
[3603.48 --> 3603.88]  prosper.
[3605.34 --> 3605.70]  Do you know what I
[3605.70 --> 3605.88]  mean?
[3606.48 --> 3607.28]  Daniel, can you do
[3607.28 --> 3607.52]  that?
[3607.92 --> 3608.28]  Apparently.
[3609.62 --> 3610.54]  You never tried.
[3610.64 --> 3611.16]  You got on the first
[3611.16 --> 3611.38]  track.
[3611.64 --> 3612.24]  Man, that is.
[3613.26 --> 3613.62]  Skills.
[3613.86 --> 3614.28]  You've got two.
[3615.12 --> 3616.02]  I'm just not using my
[3616.02 --> 3616.38]  hands.
[3617.70 --> 3618.28]  I guess.
[3618.50 --> 3619.32]  Not using it for that
[3619.32 --> 3619.66]  enough.
[3621.74 --> 3621.86]  Yeah.
[3621.96 --> 3622.44]  Right there.
[3622.78 --> 3623.32]  To be fair, though,
[3623.32 --> 3624.54]  that isn't very useful
[3624.54 --> 3625.36]  in any other.
[3625.72 --> 3626.42]  Like, that's not,
[3626.50 --> 3627.32]  you can't even use it
[3627.32 --> 3627.80]  for digging.
[3628.46 --> 3628.82]  Do you know what I
[3628.82 --> 3628.96]  mean?
[3629.10 --> 3629.84]  There's nothing.
[3630.58 --> 3631.74]  So it's only for
[3631.74 --> 3634.78]  that, showing off that
[3634.78 --> 3635.76]  you like Star Trek or
[3635.76 --> 3637.22]  at least are aware of
[3637.22 --> 3637.44]  it.
[3638.00 --> 3639.08]  Chris, thanks so much
[3639.08 --> 3639.40]  again.
[3639.80 --> 3640.62]  It was lovely to have
[3640.62 --> 3641.12]  you as usual.
[3641.48 --> 3641.98]  Of course.
[3642.12 --> 3642.72]  See you soon.
[3643.42 --> 3644.50]  And Daniel Marty.
[3645.06 --> 3646.24]  Daniel, see you next
[3646.24 --> 3646.50]  time.
[3647.16 --> 3647.56]  Thank you.
[3647.66 --> 3648.02]  It was fun.
[3648.44 --> 3649.04]  Thanks, everyone.
[3649.46 --> 3650.24]  See you next time.
[3650.58 --> 3651.16]  Said it twice.
[3651.66 --> 3652.10]  Ridiculous.
[3652.10 --> 3653.06]  It's really hard to
[3653.06 --> 3654.04]  just basic things
[3654.04 --> 3654.58]  sometimes.
[3655.30 --> 3655.60]  What I'm going to do
[3655.60 --> 3656.36]  is just say goodbye
[3656.36 --> 3657.38]  in a way that I
[3657.38 --> 3658.20]  haven't just said
[3658.20 --> 3658.78]  those words.
[3659.24 --> 3660.42]  Now it's time to
[3660.42 --> 3661.26]  say goodbye.
[3661.72 --> 3662.32]  Goodbye, everyone.
[3662.46 --> 3663.18]  See you next time.
[3667.90 --> 3669.00]  You can support
[3669.00 --> 3670.28]  our work and help
[3670.28 --> 3671.52]  ensure that GoTime
[3671.52 --> 3672.78]  continues into the
[3672.78 --> 3673.72]  future with a
[3673.72 --> 3674.52]  Changelog++
[3674.52 --> 3675.08]  membership.
[3675.58 --> 3676.42]  Ditch the ads,
[3676.64 --> 3677.36]  get closer to the
[3677.36 --> 3678.48]  metal, and directly
[3678.48 --> 3679.34]  contribute to all
[3679.34 --> 3680.42]  Changelog podcasts
[3680.42 --> 3681.92]  at changelog.com
[3681.92 --> 3682.98]  slash plus plus.
[3683.28 --> 3684.20]  Once again, that's
[3684.20 --> 3685.80]  changelog.com slash
[3685.80 --> 3686.48]  plus plus.
[3686.68 --> 3687.16]  Check it out.
[3687.78 --> 3688.84]  This episode was
[3688.84 --> 3689.72]  hosted by Matt
[3689.72 --> 3690.08]  Reier.
[3690.28 --> 3691.00]  It was produced by
[3691.00 --> 3692.14]  Jared Santo with
[3692.14 --> 3693.06]  music by the Beat
[3693.06 --> 3693.88]  Freak, Breakmaster
[3693.88 --> 3694.32]  Cylinder.
[3694.74 --> 3695.40]  GoTime is brought
[3695.40 --> 3696.12]  to you by our
[3696.12 --> 3696.98]  awesome sponsors.
[3697.28 --> 3697.98]  Special thanks to
[3697.98 --> 3699.52]  Fastly, LaunchDarkly,
[3699.90 --> 3700.42]  and Linode.
[3700.96 --> 3702.52]  On the next episode,
[3702.82 --> 3703.96]  Johnny and Chris are
[3703.96 --> 3704.86]  joined by Ian
[3704.86 --> 3706.18]  Lopshire and yours
[3706.18 --> 3707.40]  truly to discuss
[3707.40 --> 3708.52]  reading the docs.
[3709.36 --> 3710.04]  Stay tuned for
[3710.04 --> 3710.48]  that one.
[3710.72 --> 3711.36]  It'll be hitting your
[3711.36 --> 3712.20]  podcast feed
[3712.20 --> 3713.24]  next week.
[3719.98 --> 3720.98]  Bye.
[3721.04 --> 3721.54]  Bye.
[3722.12 --> 3722.18]  Bye.
[3722.58 --> 3723.54]  Bye.
[3726.22 --> 3727.10]  Bye.
[3727.22 --> 3728.30]  Bye.
[3728.30 --> 3732.28]  Bye.
[3733.30 --> 3735.64]  Bye.
[3735.64 --> 3765.62]  Thank you.
[3765.64 --> 3795.62]  Thank you.
[3795.64 --> 3825.62]  Thank you.
