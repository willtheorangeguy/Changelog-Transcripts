[0.00 --> 3.66]  We have go.mod files, and now we have go.work files.
[3.98 --> 5.50]  So you create a go.work file.
[5.62 --> 8.00]  The syntax is very similar to go.mod.
[8.08 --> 9.96]  We want it to be easy for people to pick up.
[10.36 --> 13.22]  And the go.work has one new directive,
[13.78 --> 14.92]  is the use directive.
[15.32 --> 18.76]  So you tell it which directories you want it to use,
[18.90 --> 20.72]  and all the modules in those directories,
[20.76 --> 22.54]  if you're under the go.work files,
[22.66 --> 24.72]  and where you're under a go.mod file before,
[24.88 --> 25.56]  are in your workspace.
[25.56 --> 30.64]  Hey, Jared here.
[31.22 --> 35.44]  One of the things we can count on in the software industry is change.
[36.12 --> 38.74]  The state of the art changes so fast, in fact,
[38.90 --> 41.10]  that keeping up can feel like a whole other job
[41.10 --> 42.68]  on top of your actual job.
[43.50 --> 45.54]  That's why we created Change Log Weekly.
[46.14 --> 49.16]  It's our totally free newsletter that we drop in your inbox
[49.16 --> 50.44]  each and every Sunday.
[50.98 --> 53.82]  We link to the latest news, the best articles,
[53.82 --> 56.72]  and the most interesting projects that you should be aware of.
[57.36 --> 59.60]  We also add a little commentary from us
[59.60 --> 61.00]  saying why something's important,
[61.42 --> 63.16]  pointing you to other instances of a trend,
[63.26 --> 65.44]  or just making a dorky joke to keep it lively.
[66.02 --> 67.12]  So if you haven't yet,
[67.36 --> 69.08]  I recommend subscribing to Change Log Weekly
[69.08 --> 71.60]  and help us help you keep up with the latest.
[72.52 --> 75.78]  Head to changelog.com slash weekly and sign up today.
[76.00 --> 78.56]  Again, it's totally free and we never spam you.
[78.68 --> 79.02]  Yuck.
[79.90 --> 83.40]  One last time, that's changelog.com slash weekly.
[83.40 --> 97.18]  GoTime.fm
[97.18 --> 98.86]  Let's do it.
[99.42 --> 100.46]  It's GoTime.
[100.98 --> 102.20]  Welcome to GoTime,
[102.86 --> 106.02]  your source for diverse discussions about Go 118.
[106.54 --> 109.18]  Subscribe today at GoTime.fm
[109.18 --> 112.02]  and follow the show on Twitter at GoTimeFM.
[112.02 --> 114.36]  Special thanks to our friends at Fastly
[114.36 --> 117.00]  for shipping GoTime super fast all around the world.
[117.24 --> 119.16]  Check them out at Fastly.com.
[119.76 --> 121.36]  All right, let's get into it.
[121.42 --> 122.08]  This is a good one.
[122.38 --> 123.10]  I think you promise.
[123.76 --> 124.72]  Here we go.
[132.48 --> 135.36]  Hello and welcome to GoTime.
[135.36 --> 136.44]  I'm Matt Ryer.
[136.76 --> 141.32]  And today we're talking about the other features in Go 118.
[141.96 --> 143.98]  Now listen here, you come here, come here.
[144.20 --> 147.64]  Go 118 has got two great big features
[147.64 --> 149.80]  that everyone's talking about.
[150.32 --> 151.12]  I mean, everybody,
[151.22 --> 152.80]  all the popular people are talking about it.
[152.94 --> 153.26]  Everyone.
[153.82 --> 154.58]  Well, we're not popular.
[154.92 --> 157.96]  We're going to be talking about the other features,
[158.10 --> 158.86]  not those two.
[159.20 --> 160.44]  And just for anyone that doesn't know,
[160.50 --> 161.82]  it's fuzzing and generics.
[161.82 --> 164.70]  And that's the only time they're going to be mentioned on this episode.
[165.16 --> 166.42]  In fact, we've got a new rule.
[166.56 --> 168.94]  If they are mentioned by anyone, even accidentally,
[169.42 --> 173.50]  unfortunately, you will be immediately booted from the podcast.
[173.70 --> 175.34]  So please bear that in mind.
[175.42 --> 177.60]  No talk of those two subjects.
[177.78 --> 178.28]  Pinky promise.
[179.02 --> 180.34]  That's a pinky promise from me.
[180.66 --> 183.20]  And we'll find out if we're also going to get a pinky promise
[183.20 --> 185.90]  from our special guests today.
[186.06 --> 188.02]  It's joining me, Daniel Marty.
[188.34 --> 188.92]  Hello, Daniel.
[188.92 --> 190.34]  Hello. Nice to be back.
[190.60 --> 193.24]  And nice to bring my technical problems along with me.
[194.06 --> 197.78]  Your technical problems are, like you, always welcome, Daniel.
[198.24 --> 202.64]  Daniel's been using and contributing to Go for quite a few years now.
[202.72 --> 205.16]  And you've actually written a few tools as well,
[205.28 --> 207.78]  like the stricter GoFumped
[207.78 --> 210.50]  and what could be described as the opposite,
[211.08 --> 212.80]  a Go code obfuscator.
[213.28 --> 215.54]  So they're interesting tools, Daniel.
[215.66 --> 218.22]  How is the GoFumped more strict?
[218.92 --> 222.34]  It essentially restricts how you can write and format code
[222.34 --> 223.44]  in a few extra ways.
[223.54 --> 226.14]  Like, for example, no empty lines at the start of a function body.
[226.96 --> 228.22]  Things that I generally do.
[229.22 --> 229.98]  Cool. Okay.
[230.02 --> 231.60]  We'll put a link to that in the show notes,
[231.72 --> 233.02]  because if anyone likes...
[233.02 --> 235.30]  I like the fact we have GoFumped,
[235.46 --> 237.50]  and I like the idea of a more strict one.
[238.04 --> 239.00]  Oh, Daniel, did Pinky Promise
[239.00 --> 241.24]  not going to talk about those two other subjects today?
[241.60 --> 242.06]  Pinky Promise.
[242.30 --> 242.56]  Okay.
[242.80 --> 243.84]  But Daniel's Pinky Promise.
[244.04 --> 244.20]  Okay.
[244.66 --> 245.68]  This is really professional.
[245.68 --> 246.08]  Okay.
[246.18 --> 246.94]  We've also...
[246.94 --> 248.24]  You're not going to believe this, Daniel.
[248.44 --> 249.16]  You will believe it.
[249.22 --> 249.80]  You already know.
[250.02 --> 251.28]  But imagine if you didn't.
[251.60 --> 253.70]  We've also got Michael Matlub with us.
[253.90 --> 254.54]  Hello, Michael.
[254.66 --> 255.56]  Welcome to GoTime.
[255.88 --> 256.14]  Hi.
[256.38 --> 257.14]  Great to be here.
[257.32 --> 258.60]  Oh, it's a pleasure to have you.
[258.98 --> 261.18]  Michael's on the GoTools team at Google,
[261.44 --> 263.44]  living in, you know, New York City.
[263.52 --> 264.16]  No big deal.
[264.16 --> 267.72]  And he previously worked on Go slash packages,
[267.72 --> 272.48]  which is very useful if you're writing like code generation tools and things like that,
[272.48 --> 275.20]  and infrastructure for tooling.
[275.36 --> 278.26]  And now works on the Go command, right, Michael?
[278.80 --> 279.10]  Yes.
[279.42 --> 284.48]  And do Pinky Promise to not mention those two big subjects on this very episode?
[284.98 --> 286.44]  I won't mention them by name.
[287.14 --> 287.74]  Okay.
[287.98 --> 290.46]  That sounds like a pinky caveat.
[290.46 --> 291.58]  It is.
[291.72 --> 292.80]  It is a pinky caveat.
[293.50 --> 294.28]  Okay, fine.
[294.94 --> 296.08]  We won't mention them by name.
[296.22 --> 296.70]  Well, that's it.
[296.76 --> 297.40]  We'll see how we go.
[297.94 --> 298.30]  Well, yeah.
[298.38 --> 303.30]  So this episode, like, obviously, there's a lot of people blogging and talking about
[303.30 --> 305.44]  the big sort of headline features that we are.
[305.70 --> 307.70]  A lot of people are very excited.
[307.86 --> 310.40]  A lot of people are very dismayed about generics in particular.
[310.52 --> 311.00]  I've just said it.
[311.10 --> 311.62]  I can't believe it.
[311.64 --> 312.60]  I have to leave the podcast.
[313.46 --> 314.94]  But a raft of other things.
[314.94 --> 320.42]  And this release in particular seems very packed and dense with features.
[320.76 --> 322.30]  Why is that, do we think?
[322.80 --> 326.04]  I believe they've been saving a few large features for some time.
[326.24 --> 330.02]  Like, they've been building up to generics for, like, nearly two years now.
[330.10 --> 331.16]  And now it's shipping, right?
[331.56 --> 333.68]  And I did mention the taboo subject.
[333.84 --> 337.24]  But I think it's also happened with fuzzing, which has been in the works for, like, a year now.
[337.38 --> 338.08]  Yeah, I see.
[338.20 --> 341.68]  By the way, just mentioning another taboo subject doesn't cancel out the other one.
[342.62 --> 343.02]  Yeah.
[343.02 --> 345.10]  You're just compounding your crimes.
[345.10 --> 353.94]  I asked Daniel and Michael to find a list of the things that they're sort of excited about or interested in that we can go through and talk about.
[354.74 --> 358.82]  And obviously, Michael worked on module workspaces as well.
[358.82 --> 362.36]  So we'll carve some time out at the end to talk about that in particular.
[362.96 --> 366.04]  But, Daniel, maybe you could kick us off.
[366.12 --> 372.50]  There's a really interesting one that, to me, seemed like a silly, unnecessary helper.
[372.86 --> 375.52]  But turns out to be actually quite worthy.
[375.96 --> 378.12]  That was strings.cut.
[378.26 --> 379.16]  Could you tell us about that?
[379.16 --> 385.26]  Yeah, so I think anybody who's written any non-trivial amount of code knows that they have to deal with strings.
[385.42 --> 388.58]  They have to add strings, look at prefixes and suffixes and so on.
[388.98 --> 392.28]  And one quite common operation is wanting to cut a string in two.
[392.78 --> 396.52]  So, for example, maybe you've got a domain name and you want the actual name and the extension.
[397.16 --> 399.68]  Or maybe you've got a file name and you want the file name extension.
[400.04 --> 400.72]  That kind of thing.
[400.72 --> 408.22]  You can use Go APIs like strings.index or there's also strings.splitn and you can give it the number two.
[408.44 --> 412.18]  So, like, split this string in up to two pieces, right?
[412.52 --> 415.22]  But these APIs are not super easy to use.
[415.38 --> 417.80]  For example, if you use index, it may give you minus one.
[418.34 --> 420.38]  And if you don't check for that, that might panic.
[421.16 --> 422.78]  And split has the same issue, right?
[422.80 --> 424.68]  Because it gives you a slice.
[425.04 --> 430.18]  So cut is, it has, you could say cut has less sharp edges.
[430.18 --> 436.64]  So it only gives you two strings for the two sides and a boolean telling you whether or not it successfully cut.
[437.22 --> 437.98]  Yeah, so that's nice.
[438.04 --> 445.30]  So if, say, you were cutting on a colon and there wasn't a colon in there, it wouldn't be in any way like a panic or a problem.
[445.52 --> 448.28]  You'd just get a false as the second argument.
[448.52 --> 448.82]  Exactly.
[449.18 --> 449.36]  Yeah.
[449.82 --> 450.74]  What do you think about that, Michael?
[451.18 --> 454.04]  Have you written code that cuts things up like this?
[454.26 --> 454.78]  I have.
[454.94 --> 457.22]  Yeah, it would be a nice convenience.
[457.54 --> 458.40]  I like conveniences.
[458.40 --> 462.34]  Yeah, I thought this was like an unnecessary helper.
[462.52 --> 466.46]  Because whenever you can already do something, that's usually my preferred way.
[466.46 --> 469.56]  I looked at some of the commentary on this one.
[469.56 --> 476.42]  And the number of cases where people were basically doing this same operation over and over again, it's kind of everywhere.
[476.72 --> 484.58]  And including some places where we'd done it incorrectly or in a way that would panic if it got some bad input or something.
[484.58 --> 491.76]  If there was like some testing tool that helped you try to test out all these different possible ways of responding to input, that'd be great.
[491.88 --> 493.22]  But not on this episode, there isn't.
[493.88 --> 494.44]  But yeah, okay.
[494.58 --> 497.18]  So strings cut and that's coming in Go 118.
[497.82 --> 499.48]  Okay, Daniel, have you got another one for us?
[499.48 --> 503.66]  So I've got another one that's significantly more complex than strings.cut.
[503.78 --> 507.48]  And I believe it was developed by the people at Tailscale over a few years.
[507.48 --> 510.74]  And it's essentially a replacement for the net.ip type.
[511.32 --> 516.26]  So right now, IP addresses in Go, they represent it as a byte slice.
[516.26 --> 519.24]  So you can think of a byte slice, it can have many lengths.
[519.60 --> 523.56]  So an IPv4 is going to be shorter than an IP version 6, for example.
[524.22 --> 527.74]  And they designed a new IP package, which they called NetAdder.
[528.02 --> 530.58]  But now it's being merged as NetIP.
[531.18 --> 532.50]  So it's net slash NetIP.
[533.12 --> 537.26]  And it's got a bunch of advantages, mostly related around performance.
[537.70 --> 543.24]  But the two main properties that it has as part of its design, which do not use a slice, essentially.
[543.84 --> 544.86]  One, it's comparable.
[545.14 --> 546.38]  So you cannot compare slices.
[546.44 --> 547.56]  You can only compare them to nil.
[548.18 --> 550.54]  And the other one is that it doesn't allocate.
[550.54 --> 554.68]  So you can create a new IP without calling make or new or anything like that.
[554.68 --> 558.20]  Because I think it's backed by what is essentially a bunch of integers.
[559.18 --> 563.22]  So will the standard library bits of it be rewritten to use this new type?
[563.56 --> 567.78]  Or is this just going to be something that's available for calling code?
[568.06 --> 568.96]  I think that's a good question.
[568.96 --> 575.04]  And I think anything that exposes APIs with the old type will have to remain the same because of backwards compatibility.
[575.64 --> 590.20]  I seem to recall one of the reasons to add this to a standard library is so that, for example, HTTP 2 and 3, which I think it's only HTTP 3, which re-implements something like TCP, right, in user space.
[590.70 --> 593.08]  And that deals with a lot of IP addresses.
[593.08 --> 598.64]  So if you can remove a bunch of internal allocations that don't leak into the API, that can be a very large plus.
[599.10 --> 599.56]  Yeah, that's nice.
[599.84 --> 603.24]  And do you know if they're going to be helpers to kind of switch between the two?
[603.32 --> 606.38]  Do you think we're going to see code like that flying around for a bit?
[606.56 --> 610.32]  I believe the package comes with helpers, but my memory is failing me.
[610.88 --> 611.14]  Okay.
[611.42 --> 614.50]  I mean, if not, people will probably end up doing that, I imagine.
[614.70 --> 618.94]  But yeah, it's nice to know that there's a sort of improved data type there.
[618.94 --> 626.16]  And it's funny, like, you know, with the Go backwards compatibility promise, you can't just break things and break APIs and break everyone's code.
[626.68 --> 627.78]  You know, it's not Python.
[628.32 --> 631.70]  I shouldn't have a go at other languages, but Python does that a lot.
[632.32 --> 635.14]  But with that promise, of course, your hands get tied.
[635.32 --> 644.28]  So this is kind of a nice way of releasing almost like more modern implementations is to sort of release them alongside and then they kind of coexist.
[644.28 --> 646.70]  But does that create confusion?
[646.98 --> 648.78]  Like, how will people know which one to use?
[648.94 --> 649.78]  That's a good question.
[650.14 --> 655.72]  I think the Go standard library has a bunch of cases where there are packages and APIs that everybody knows not to use.
[655.82 --> 659.62]  Like there's container slash list that has like a linked list, for example.
[659.88 --> 662.46]  And I don't think everybody's used that outside of an example.
[662.66 --> 662.80]  Yeah.
[663.16 --> 670.92]  I don't think they can deprecate net IP simply because, as in the existing net.ip type, because it is used in existing APIs.
[670.92 --> 679.10]  But I think there is going to be a common understanding that if you want the extra nice features of the new type, you should just use it.
[679.38 --> 679.46]  Right.
[679.88 --> 680.14]  Great.
[680.46 --> 681.10]  Thank you.
[681.24 --> 681.68]  Nice one.
[682.22 --> 682.86]  Right, Michael.
[682.86 --> 685.84]  Maybe you could pick one to talk about next.
[685.84 --> 692.18]  I'll pick a couple of features that my colleagues, Jay and Brian, added to the Go command.
[692.18 --> 708.50]  So they are VCS build stamping and a debug build info function to get information about the versions of modules in a Go library as an Go binary as an API.
[708.50 --> 720.08]  So both of these have a similar core motivation, which is to improve visibility into binaries, to know which packages they were built on.
[720.28 --> 726.48]  So you can determine, say, if binaries were built with certain commits of code.
[726.68 --> 733.04]  In the case of VCS build stamping, because the main module may not have a version associated with it.
[733.64 --> 737.06]  And in the case of the build info of dependencies.
[737.06 --> 749.56]  And this is shaping up to be a big thing in these days to know whether your dependencies and the code that you're built with have bugs or bad features in them.
[749.62 --> 754.38]  And if the code that you're running with is safe and to audit everything properly.
[754.78 --> 758.54]  We've seen several cases of bad libraries in the wild.
[758.80 --> 763.56]  And people have to quickly audit if all their code is safe or not.
[763.70 --> 765.56]  All their code running in production is safe or not.
[765.56 --> 767.38]  Yeah, and it's a tricky thing.
[767.56 --> 768.86]  So I'm picking that a little bit then.
[768.98 --> 776.78]  So VCS, version control systems, like the Git hash, when you have a certain level that you've committed up to.
[777.28 --> 778.98]  And every time you commit, you get a new hash.
[779.50 --> 783.12]  And so now when we build, that will be incorporated.
[783.38 --> 788.00]  Is it like it supports all the major kind of VCS systems?
[788.00 --> 790.00]  So like it'll support Git and...
[790.00 --> 790.88]  Yeah, yeah.
[790.88 --> 792.46]  I mean, it definitely supports Git.
[792.58 --> 798.00]  I don't know what other VCSs we support if we do support other VCSs.
[798.10 --> 799.32]  Dan, do you know?
[799.36 --> 800.22]  But they'll be coming soon.
[800.42 --> 804.16]  I think there's Mercurial Bazaar subversion.
[804.50 --> 806.18]  And that might be it for these days.
[806.42 --> 807.40]  That's a good selection.
[808.04 --> 809.10]  Could you name five?
[810.38 --> 812.08]  Five VCS systems?
[812.28 --> 813.18]  Yeah, just five dead quick.
[813.18 --> 815.18]  Well, Dan named four, so...
[815.18 --> 815.56]  I know.
[815.92 --> 816.72]  So it should be easy.
[816.84 --> 823.10]  I think there was like, I've seen in the Go command, like a VCS named like Fossil that had support somewhere.
[823.46 --> 825.28]  So that'll round us out.
[825.42 --> 825.98]  There we go.
[826.06 --> 826.66]  Fossil, there we go.
[826.72 --> 826.96]  Five.
[827.06 --> 827.28]  Brilliant.
[827.44 --> 827.78]  There you go.
[828.34 --> 828.68]  Learning.
[829.16 --> 829.60]  So, okay.
[829.70 --> 835.74]  And then the other thing is that build info with all the dependencies, because that is a big thing.
[835.74 --> 849.54]  You know, sometimes, well, we're paying a lot more attention now to reporting vulnerabilities, capturing that data, and then being able to, in the tooling, use that to know whether we are dealing or running something that has some known vulnerability.
[850.10 --> 850.18]  Yeah.
[850.30 --> 852.14]  So that is a massive thing.
[852.26 --> 857.48]  And of course, having this put in there automatically saves us a lot of effort, right?
[857.48 --> 868.42]  My understanding is that build info is like a function that's like accessible to programs that was like just in the Go command before, like Go version dash M, right?
[868.78 --> 881.28]  So it makes it easier for other people to write these auditing programs that can help detect if there are bad versions in your dependencies and, you know, then flag it or fix it or whatever.
[881.28 --> 891.20]  And these automated things, I hope, can solve a lot of like manual human work that we've had to do when these issues have come up.
[891.42 --> 891.54]  Yeah.
[891.94 --> 902.36]  Well, it's very useful with like if you have Dependabot or whatever running in your continuous integration or just running in GitHub, like having those tools help, you know, it's all great.
[902.44 --> 904.60]  So anything in that effort, I think, is worth having.
[905.10 --> 905.76]  Very cool.
[905.76 --> 911.26]  And yeah, before we had to like use either build tags or do something else funky to get the version.
[911.66 --> 912.62]  I would always do that.
[912.68 --> 918.84]  I would have some script that would, I think I did it with Go Embed as well successfully recently.
[919.32 --> 920.84]  But we just don't have to do that now.
[921.00 --> 924.88]  And so we'll be able to access that version inside the build as well from somewhere.
[925.34 --> 926.92]  Sorry, access the...
[926.92 --> 929.50]  Access like the git hash inside the binary itself.
[929.80 --> 930.66]  Yeah, it's in the binary.
[930.92 --> 934.32]  So I don't know what the API is.
[934.32 --> 934.72]  Yeah.
[935.24 --> 937.92]  There's some either method or...
[937.92 --> 938.14]  Yeah.
[938.40 --> 946.86]  It's honestly a bit confusing because before there was an API to get the module information of yourself, like of your own running binary.
[947.14 --> 955.10]  But the new API they've added is you can give it a binary path so you can use it with any binary without having to shell out to go version dash and blah, blah, blah.
[955.56 --> 956.74]  It's essentially the same feature.
[957.22 --> 960.84]  Oh, so the build info includes that, the hash.
[961.22 --> 962.26]  Oh, well, there we go.
[962.38 --> 962.58]  Okay.
[962.58 --> 969.28]  And I think the VCS stamping is also a bit confusing to end users because you tell them Go 118 now stamps VCS build info.
[969.28 --> 977.56]  But they might say, if I go install a Go package, a Go main package, and I run Go version dash M with Go 117, I already see the module version, right?
[977.56 --> 990.38]  But where that doesn't work is instead of doing a global git install via a module path, if you git clone and then go build or go install locally from that git clone, Go doesn't know what module version that is.
[990.46 --> 991.32]  It just has a git clone.
[991.32 --> 997.32]  It's not resolving that module through the whole proxy system that tells it what version it is.
[997.72 --> 1000.04]  In Go 117, it tells you version devil.
[1000.34 --> 1001.22]  It has no idea.
[1001.66 --> 1010.16]  And in Go 118, it will add some extra separate metadata that will say, hey, this was built from git hash, blah, blah, blah, date, blah, blah, blah, and so on.
[1010.16 --> 1010.84]  All right.
[1011.32 --> 1011.72]  Okay.
[1011.88 --> 1014.78]  Daniel, your turn to pick one from the list.
[1014.96 --> 1016.92]  What else is cool coming in Go 118?
[1017.26 --> 1021.82]  By the way, do you say 118, 1 dot, 1 eight, 1 point 18?
[1022.40 --> 1023.28]  How do you say it?
[1023.64 --> 1026.38]  Now you're making me doubt myself about how I pronounce these things.
[1026.72 --> 1026.98]  Yeah.
[1027.18 --> 1028.08]  You just have to forget.
[1028.28 --> 1030.06]  Just clear your mind and then just say it.
[1030.32 --> 1030.94]  See what happens.
[1031.24 --> 1031.60]  118.
[1031.98 --> 1033.06]  Yeah, I say 118.
[1033.42 --> 1033.68]  Yeah.
[1033.84 --> 1034.10]  Okay.
[1034.40 --> 1034.88]  That's good.
[1035.04 --> 1036.34]  It is kind of 118, isn't it?
[1036.38 --> 1038.88]  It's not, because it's not a decimal number, is it?
[1039.30 --> 1039.78]  It's Semver.
[1040.04 --> 1041.88]  So that second number is 18.
[1041.96 --> 1042.58]  I think we're right.
[1042.84 --> 1046.78]  So does that mean that when we reach 120, we can go back to 1.2?
[1047.14 --> 1048.90]  I think for just that release.
[1049.34 --> 1050.32]  No, you can't, can you?
[1050.42 --> 1051.28]  No, because that's what I mean.
[1051.28 --> 1051.94]  It's not decibel.
[1052.46 --> 1052.90]  That's it.
[1053.00 --> 1053.14]  Yeah.
[1053.88 --> 1054.92]  Yeah, we've got that in the end.
[1054.92 --> 1059.50]  So another feature, I mean, it's maybe a bit cheeky that I bring this up because I worked on this,
[1059.50 --> 1064.30]  but GoFump without a space now formats files in parallel.
[1064.88 --> 1068.46]  So up until now, you have, well, you have two tools, which is also confusing.
[1068.64 --> 1072.80]  You have GoFump without a space, and then you have Go space Fump.
[1073.06 --> 1073.34]  Yeah.
[1073.38 --> 1078.18]  It's ironic that the GoFump tool, it can be called in different ways just by changing the formatting.
[1079.78 --> 1080.30]  Yeah.
[1080.94 --> 1081.70]  Oh God.
[1082.04 --> 1086.36]  The difference between the two tools, and I think it also confuses a bunch of users,
[1086.36 --> 1091.42]  is that without a space, it takes files and directories, but it doesn't know what packages
[1091.42 --> 1091.72]  are.
[1092.12 --> 1095.58]  And with a space, it takes a package pattern.
[1095.72 --> 1097.80]  So you can give it dot slash dot dot dot, for example.
[1098.44 --> 1103.80]  And the one that works on packages has always been relatively well parallelized, because what
[1103.80 --> 1108.30]  it does is, I believe it formats each package in parallel or something like that.
[1108.42 --> 1111.88]  But the one that takes directories and files, it would just do one at a time.
[1111.88 --> 1118.48]  And now we've essentially removed the parallelism from the one with the space, and just made
[1118.48 --> 1122.92]  both tools use the same kind of parallelism, which is GoFump without a space.
[1123.20 --> 1126.24]  When you give it a bunch of files to format, it's just going to figure out how to format
[1126.24 --> 1127.20]  them as fast as possible.
[1127.92 --> 1128.40]  So that's cool.
[1128.52 --> 1132.88]  Does GoFump work only within the context of a file at a time then?
[1133.10 --> 1136.76]  Like, it doesn't need to know anything else about types and things, does it?
[1136.76 --> 1138.84]  Because it's just doing kind of formatting tasks.
[1139.14 --> 1139.68]  Yeah, that's correct.
[1139.68 --> 1141.92]  So it makes sense, you just do all that at the same time.
[1142.16 --> 1147.66]  Yeah, even though there's a few tricky bits about that, because initially my naive implementation
[1147.66 --> 1152.60]  was just format each file as a separate GoRoutine as they come in.
[1153.16 --> 1154.90]  But some files are really, really tiny.
[1155.28 --> 1159.74]  I think like a doc.go file that only has like 10 lines with like a package documentation
[1159.74 --> 1160.60]  or something like that.
[1161.00 --> 1166.10]  And spawning a new GoRoutine, synchronizing with the parent, maybe allocating the new parser,
[1166.10 --> 1167.64]  the new printer, and stuff like that.
[1167.64 --> 1172.52]  It actually consumes quite a lot more CPU just because of the overhead of all those tiny
[1172.52 --> 1172.90]  files.
[1173.60 --> 1178.28]  So we ended up with something that's kind of like chunking groups of files in groups of
[1178.28 --> 1182.78]  similar sizes so that they're big enough that actually doing that as parallel units,
[1182.94 --> 1183.50]  it's fast.
[1183.82 --> 1184.94]  Oh, that's really cool.
[1185.06 --> 1185.78]  That's a surprise.
[1185.88 --> 1188.10]  I would not have expected it to be doing that.
[1188.28 --> 1191.80]  But that's nice to know that that's measured and done properly.
[1191.80 --> 1191.88]  Okay.
[1192.76 --> 1193.56]  That's very cool.
[1193.66 --> 1194.66]  Have you used this then?
[1194.82 --> 1197.86]  Have you really noticed this in practice?
[1198.34 --> 1199.10]  The speed importance?
[1199.34 --> 1201.08]  I think it depends on what people do.
[1201.40 --> 1205.68]  I think many people use the tool that works on packages, and then they just format their
[1205.68 --> 1206.04]  packages.
[1206.20 --> 1208.94]  But I like using the one with directories.
[1208.94 --> 1214.06]  So I go to the root of my repository, and I just tell it, format everything, including
[1214.06 --> 1215.44]  test files, including everything.
[1216.16 --> 1218.14]  And because I did that, it was really slow before.
[1218.46 --> 1222.14]  So now, depending on your machine, it's usually about three to four times as fast.
[1222.40 --> 1228.12]  So for me, for example, formatting a large repo might go from like five seconds to two
[1228.12 --> 1229.24]  seconds, which is nice.
[1230.10 --> 1232.08]  Matt Lube, do you format your code?
[1232.60 --> 1232.90]  Yes.
[1233.04 --> 1235.26]  I mean, we all format our code.
[1235.66 --> 1236.44]  It's not a trick question.
[1236.44 --> 1238.68]  No, is there anyone who doesn't format their code?
[1239.00 --> 1241.14]  Because I want to hear about it.
[1241.22 --> 1242.74]  It's like a problem we need to solve.
[1243.02 --> 1243.34]  Oh, yeah.
[1243.40 --> 1244.00]  No, I don't.
[1244.06 --> 1245.10]  I don't think so.
[1245.16 --> 1247.08]  Because you only have to do it a few times.
[1247.08 --> 1251.74]  And then when pull requests, although they improved it in GitHub, where whitespace was
[1251.74 --> 1252.70]  understood better.
[1253.02 --> 1257.30]  But it certainly used to be that what you'd get just pull requests that every line has
[1257.30 --> 1259.66]  changed because some whitespace thing.
[1259.82 --> 1265.12]  And that got so annoying that it's very high motivator, I think, to get people formatting.
[1265.12 --> 1266.10]  But I don't know.
[1266.10 --> 1268.44]  I assume everyone does format their code.
[1268.88 --> 1270.92]  Do you do it in the way Daniel described then?
[1271.10 --> 1274.96]  Or do you do it like me, where you just, every time you save a file, it does just that file?
[1275.62 --> 1278.60]  I don't think I've ever run either of the tools.
[1279.24 --> 1282.42]  Or I certainly haven't run either of the tools by hand in years.
[1282.80 --> 1286.36]  My editors are just set up to format files as I save them.
[1286.82 --> 1287.12]  Oh, yeah.
[1287.16 --> 1287.28]  Yeah.
[1287.28 --> 1291.40]  I thought you were saying that you just write it in perfect, go-thumped way first time.
[1291.40 --> 1293.56]  Oh, no, no, I don't.
[1293.62 --> 1294.02]  Nailed it.
[1294.08 --> 1298.06]  I write it in the wrong way and just let the format or take care of it.
[1298.22 --> 1300.74]  Like any good codeveloper.
[1301.00 --> 1301.52]  Yeah, exactly.
[1301.66 --> 1306.30]  To be honest, I'll deliberately make mistakes so that when I hit save, I get the visual clue
[1306.30 --> 1307.34]  that it has formatted.
[1307.74 --> 1311.16]  Because if I write it and I get it right and then I hit save and nothing happens, I'm like,
[1311.50 --> 1312.58]  computer's not working.
[1312.58 --> 1318.40]  So I genuinely sometimes like to see the little shift into place of things as a clue that it's
[1318.40 --> 1318.76]  working.
[1319.10 --> 1319.22]  Yeah.
[1319.28 --> 1323.04]  I mean, that's like a nice way to know that like, oh, the syntax is correct.
[1323.32 --> 1324.24]  Yeah, that's true.
[1324.46 --> 1325.30]  You know, it can parse.
[1325.60 --> 1328.22]  Yeah, because if it errors, it doesn't complete it.
[1328.34 --> 1330.56]  So it actually is a feedback loop thing.
[1330.88 --> 1331.22]  There you go.
[1331.44 --> 1332.46]  Tip there for everyone.
[1332.72 --> 1334.40]  I've actually done that with tests.
[1334.56 --> 1339.24]  Like if you write a ton of software and some tests and you run the tests and everything's
[1339.24 --> 1341.56]  green, I often go like, I don't believe that.
[1341.56 --> 1345.44]  Let me bring one of the tests to see if I'm doing something really dumb right now.
[1345.58 --> 1347.02]  Yeah, absolutely.
[1347.58 --> 1350.78]  In TDD, they do talk about that red-green testing for that reason.
[1350.88 --> 1352.44]  Like you have to see the test fail.
[1352.80 --> 1355.36]  So you know it's saying something useful.
[1355.84 --> 1357.94]  And then when you fix it, that's true.
[1358.04 --> 1362.02]  If I write some code and it just, even if I'm just running it and I'm going to run it
[1362.02 --> 1366.90]  myself and look at the results in the terminal, like without even any tests, if that works
[1366.90 --> 1370.20]  first time, I'm highly suspicious, really suspicious.
[1370.20 --> 1374.00]  So yeah, in a way, I'm not happy when it does.
[1374.92 --> 1375.24]  Okay.
[1375.38 --> 1379.50]  We've also got the Pacer redesign in the garbage collector.
[1379.86 --> 1380.26]  Right.
[1380.46 --> 1381.16]  That's interesting.
[1381.28 --> 1382.16]  What's going on there then?
[1382.38 --> 1386.36]  I brought this up because I think it's a very interesting topic, but I think we should also
[1386.36 --> 1389.58]  warn that none of us here are experts in this area.
[1389.58 --> 1393.60]  So we can talk about it at a high level, but I'm going to stop there.
[1393.70 --> 1397.94]  If anybody wants to read more about it, we can mention the issue number and then they
[1397.94 --> 1400.46]  can go and read the whole doc.
[1400.78 --> 1402.12]  And I think that's very reasonable.
[1402.70 --> 1402.82]  Yeah.
[1403.12 --> 1403.58]  Fair enough.
[1403.68 --> 1404.26]  Good disclaimer.
[1405.22 --> 1411.06]  To give a bit of an intro, the way I understood it, because again, I just read this, the GC Pacer,
[1411.06 --> 1415.20]  it's the part of the garbage collector that decides when a new collection should happen.
[1415.68 --> 1419.68]  So it's sort of the thing that times when the GC should be doing its work, because if
[1419.68 --> 1423.62]  it happens too often, then you're just burning too much CPU, you're wasting time.
[1423.76 --> 1428.36]  But if you run it too little, you might be holding onto too much memory, or you might be
[1428.36 --> 1432.60]  delaying some things happening in the runtime that you don't want to delay by very long.
[1432.60 --> 1436.84]  It seems like the GC Pacer was designed a while ago.
[1437.34 --> 1439.44]  For the purpose that it was designed, it was good.
[1439.68 --> 1443.78]  But over time, it's accumulated a bunch of debt and a bunch of quirks.
[1444.06 --> 1448.44]  And they've sort of sat down and said, okay, let's redesign it in a way that it does a lot
[1448.44 --> 1452.96]  better in these edge cases that we found in production workloads that the old one doesn't
[1452.96 --> 1453.64]  do very well in.
[1454.14 --> 1456.12]  And I think that's where I'm going to leave it.
[1456.92 --> 1456.96]  Hmm.
[1457.60 --> 1458.62]  That's very exciting.
[1458.62 --> 1463.32]  I'm really interested whenever there are these kind of really low level, because it's funny,
[1463.46 --> 1468.72]  like when you dig into these little subsystems, they're just like other types of programs.
[1468.72 --> 1472.60]  Like they are just doing the same things that we're doing in our programs.
[1472.82 --> 1478.74]  But they're just so kind of, it's such an interesting domain, I think, that it always makes it more
[1478.74 --> 1479.08]  interesting.
[1479.18 --> 1483.78]  And the fact that, I love the fact that as programmers, we get this for free.
[1483.96 --> 1487.72]  Like people are doing this work for us to make these improvements.
[1487.72 --> 1490.98]  Like I didn't even know about a pacer, to be honest.
[1491.16 --> 1493.74]  So it's very nice to know that that's happening.
[1494.16 --> 1495.50]  What do you think about that, Michael?
[1496.02 --> 1497.00]  Do you know anything about this?
[1497.46 --> 1504.38]  Not, I mean, I am not closely acquainted with it, but I think any runtime improvements are
[1504.38 --> 1505.66]  well appreciated.
[1506.50 --> 1507.76]  Good work, team.
[1508.22 --> 1508.44]  Yep.
[1508.64 --> 1512.44]  And it's Michael, there's another Michael who I think was the author of the redesign.
[1512.68 --> 1513.14]  Is that right?
[1513.76 --> 1514.16]  Yeah.
[1514.16 --> 1517.08]  Do you know all the other Michaels on the Go team?
[1517.32 --> 1520.06]  Or have you got together yet with all the rest of the Michael?
[1520.42 --> 1521.14]  Is there another?
[1521.94 --> 1522.72]  There's a Michael.
[1523.28 --> 1524.80]  I may just be a contributor, actually.
[1525.12 --> 1525.82]  There's two.
[1526.70 --> 1527.80]  Are there more than two?
[1528.58 --> 1530.52]  Or are there three, I guess, including myself?
[1530.90 --> 1531.18]  Okay.
[1531.38 --> 1532.70]  I don't want to be forgetting anyone.
[1532.84 --> 1533.74]  So if I forgot you.
[1533.80 --> 1535.50]  No, I think we should spend time on this.
[1536.66 --> 1537.58]  Don't forget anyone.
[1537.94 --> 1539.48]  We should not spend time on this.
[1539.66 --> 1540.86]  Mind you, you're just telling me a number.
[1540.86 --> 1545.54]  Even if you forgot a Michael, they don't know which one they've, they don't know that they've
[1545.54 --> 1546.06]  been forgotten.
[1546.28 --> 1547.12]  It's just, there you go.
[1547.20 --> 1547.82]  I think you're safe.
[1548.30 --> 1551.88]  So everyone can assume that I included them in the list of Michaels.
[1552.10 --> 1552.42]  Yeah.
[1552.56 --> 1554.22]  So calm down, Michaels.
[1554.34 --> 1554.94]  You were counted.
[1555.36 --> 1557.76]  All Michaels have been accounted for.
[1559.50 --> 1559.90]  Excellent.
[1559.90 --> 1564.38]  I was thinking before we go on to the next topic, if anybody wants to read about this,
[1564.56 --> 1567.08]  the issue number is 44167.
[1567.70 --> 1571.50]  And at the end of the issue, which is very short, there's a link to the full proposal
[1571.50 --> 1573.28]  design, which is very long.
[1573.54 --> 1576.34]  And you can read that carefully and get the full picture.
[1576.72 --> 1576.88]  Yeah.
[1577.00 --> 1578.54]  It looks very well written.
[1578.88 --> 1582.62]  And we'll post the link to all of these in the show notes.
[1582.68 --> 1585.58]  So you'll be able to go and actually look at the original issues.
[1585.58 --> 1590.96]  And honestly, like notice that some of these issues aren't created by members of the Go
[1590.96 --> 1596.24]  team or even popular contributors like Daniel who've contributed massively.
[1596.86 --> 1600.26]  Sometimes these come from just people in the community that have a problem that they want
[1600.26 --> 1601.54]  to solve or something they care about.
[1601.86 --> 1606.20]  So we do get stuck in basically, because you never know, you might get some improvements
[1606.20 --> 1607.94]  made and that'd be great for everyone.
[1615.58 --> 1624.16]  We are going to send three, two, one.
[1624.62 --> 1629.90]  I'm Karhara Zhu, host of Ship It, a show with weekly episodes about getting your best ideas
[1629.90 --> 1631.88]  into the world and seeing what happens.
[1632.22 --> 1637.28]  We talk about code, ops, infrastructure, and the people that make it happen like charity
[1637.28 --> 1638.36]  majors from Honeycomb.
[1638.70 --> 1641.64]  We act like great engineers make great teams.
[1641.84 --> 1643.28]  And it's exactly the opposite.
[1643.28 --> 1646.92]  In fact, it is great teams that make great engineers.
[1647.58 --> 1650.82]  And Dave Farley, one of the founders of Continuous Delivery.
[1651.18 --> 1653.98]  Start off assuming that we're wrong rather than assuming that we're right.
[1654.24 --> 1655.22]  Test our ideas.
[1655.36 --> 1656.86]  Try and falsify our ideas.
[1657.00 --> 1658.98]  Those are better ways of doing work.
[1659.04 --> 1661.28]  And it doesn't really matter what work it is that you're doing.
[1661.42 --> 1663.10]  That stuff just works better.
[1663.60 --> 1669.54]  We even experiment on our own open source podcasting platform so that you can see how we implement
[1669.54 --> 1672.60]  specific tools and services within changelog.com.
[1672.90 --> 1674.68]  What works and what fails.
[1675.08 --> 1678.92]  It's like there's a brand new hammer and we grab hold of it and everyone gathers around.
[1679.02 --> 1682.82]  We put our hand out and we strike it right on our thumb.
[1683.06 --> 1685.90]  And then everybody knows that hammer really hurts.
[1686.06 --> 1688.54]  When you strike it on your thumb, I'm glad those guys did it.
[1688.60 --> 1689.42]  I've learned something.
[1689.58 --> 1690.24]  Instead, yeah.
[1690.24 --> 1694.98]  I think that's a very interesting perspective, but I don't see that way.
[1695.16 --> 1695.38]  Okay.
[1695.50 --> 1698.60]  It's an amazing analogy, but I'm not sure that applies here.
[1698.96 --> 1701.24]  Listen to an episode that seems interesting or helpful.
[1701.40 --> 1703.04]  And if you like it, subscribe today.
[1703.16 --> 1704.30]  We'd love to have you with us.
[1708.98 --> 1711.06]  Does anyone have the M1 chip?
[1711.52 --> 1712.60]  Apple's M1.
[1713.04 --> 1715.30]  I have it on my personal laptop.
[1715.68 --> 1716.30]  Yeah, that counts.
[1716.80 --> 1717.62]  It's fast, isn't it?
[1717.82 --> 1718.78]  Oh yeah, it's great.
[1718.78 --> 1721.64]  I've been surprised with how fast it is.
[1721.96 --> 1722.28]  Me too.
[1722.48 --> 1726.02]  I got a new MacBook Pro recently and it's phenomenal.
[1726.24 --> 1726.64]  Absolutely.
[1727.32 --> 1730.96]  But Go had support for the M1 chip for quite a while, didn't it?
[1731.24 --> 1732.38]  What does that look like?
[1732.44 --> 1734.08]  How do we support another chip?
[1734.38 --> 1738.26]  Could someone just briefly, and I do mean briefly, like we don't have to get into the
[1738.26 --> 1740.24]  weeds of it, but what do we have to do?
[1740.30 --> 1745.38]  Is it literally, we have to add some kind of mapping file for all the instructions so
[1745.38 --> 1748.18]  that a compiler knows what to compile them into?
[1748.18 --> 1750.18]  And it's different if it's a different chip?
[1750.56 --> 1752.86]  Because there's also the Rosetta 2 stuff.
[1753.00 --> 1758.70]  So that even if a binary on these new architectures hasn't been built for that architecture, this
[1758.70 --> 1759.76]  is translation layer.
[1760.14 --> 1764.70]  And to be honest, they're still lightning fast, like as far as I can see when I run programs
[1764.70 --> 1765.24]  like that.
[1765.74 --> 1767.08]  But there are some improvements coming.
[1767.14 --> 1767.58]  Is that right?
[1767.58 --> 1773.42]  I do seem to recall that when the M1 first came out, Go did already support ARM64.
[1773.74 --> 1776.16]  So the 64 version of the ARM architecture.
[1776.50 --> 1782.58]  But binary's build for Go targeting the architecture didn't work out of the box for one reason,
[1782.66 --> 1787.16]  because there wasn't a Darwin slash ARM64 port yet.
[1787.16 --> 1791.92]  So Go did support Mac, and it supported ARM64, but not together yet.
[1792.04 --> 1797.26]  So they needed to add some glue code to essentially make those two work together.
[1797.60 --> 1802.20]  And I think the other major work they had to do was the whole thing about signing binaries,
[1802.68 --> 1805.94]  because I think the M1 was the first machine that required all binaries to be signed.
[1806.14 --> 1810.00]  So they had to teach the linker how to sign binaries locally, something like that.
[1810.00 --> 1810.72]  Yeah, yeah.
[1811.04 --> 1811.90]  Oh, that's very cool.
[1812.14 --> 1813.68]  Well, I just noticed it started working.
[1814.12 --> 1820.00]  There's also a lot of work that needs to be done when we're signing binaries for,
[1820.28 --> 1824.42]  when we're making releases, when Apple makes changes to their operating system,
[1824.88 --> 1832.38]  we often have to change the infrastructure we use to produce the Go distributions that people
[1832.38 --> 1832.94]  get.
[1833.08 --> 1834.46]  And that takes a lot of work.
[1834.46 --> 1839.62]  And I kind of just want to kind of mention all the work that the Go release team has
[1839.62 --> 1845.96]  done to make our releases smooth, because sometimes that goes, it's not explicitly talked
[1845.96 --> 1846.56]  about as much.
[1846.90 --> 1851.86]  So I imagine every time Apple says a new major version of macOS is coming, I imagine some
[1851.86 --> 1854.52]  people start sweating, thinking, oh no, what is coming?
[1855.62 --> 1860.60]  Yeah, I mean, sometimes there's like nothing, but sometimes they're disruptive.
[1860.60 --> 1866.90]  Was it Catalina that they like introduce like major signing requirements or something?
[1867.18 --> 1869.28]  It caused big problems.
[1869.92 --> 1872.50]  Well, again, we do appreciate all that work.
[1873.02 --> 1878.02]  Newer x86-64 machines are also getting improvements, aren't they, Daniel?
[1878.42 --> 1884.52]  Yeah, so that's a good segue because going from, for example, ARM-based machines, there's
[1884.52 --> 1885.18]  a lot of versions.
[1885.50 --> 1889.76]  If you have an old phone, I believe that's going to be like ARM version 6, but later phones
[1889.76 --> 1892.54]  are going to be ARM version 8 or 9, which is 64 bits.
[1893.20 --> 1897.98]  And if you compile a binary that's targeting like the lowest possible denominator, the
[1897.98 --> 1901.68]  older version, it's not going to run as fast as it could on a newer device.
[1902.12 --> 1907.98]  So Go has had a flag called, I think it's called Go ARM 64, and you tell it what version
[1907.98 --> 1911.42]  of the architecture your machine, your target machine supports.
[1911.70 --> 1917.24]  And then if you swap a 6 for a 9, it might run 10% faster, depending on what kind of code
[1917.24 --> 1917.66]  you're running.
[1918.32 --> 1920.52]  And x86-64, i.e.
[1920.76 --> 1927.40]  AMD 64 desktop CPUs, they don't suffer from as much of the same problem because they haven't
[1927.40 --> 1930.82]  had as many versions with as many changes in the last decade or two.
[1931.32 --> 1933.22]  But you have had some changes.
[1933.76 --> 1939.08]  And sort of mirroring the same environment variable for ARM 64, now we have Go AMD 64.
[1939.48 --> 1941.42]  And it targets one of four versions.
[1941.42 --> 1947.00]  And these are sort of standard versions between Intel and AMD, where roughly speaking, I believe
[1947.00 --> 1948.94]  version one is like the common denominator.
[1949.40 --> 1952.54]  It's basically every single machine that's valid AMD 64.
[1952.98 --> 1957.66]  And then you've got version two for things that are starting, I think, in like 2010 or
[1957.66 --> 1957.92]  so.
[1958.38 --> 1960.94]  Version three starting in like 2013, 2014.
[1961.42 --> 1967.30]  And then version four, which is, I think, AVX 512, which is mostly server computers or very
[1967.30 --> 1968.80]  new desktop computers.
[1968.80 --> 1974.32]  So if, for example, you know you're targeting a cloud machine and you know the cloud machine
[1974.32 --> 1978.76]  has all these new instructions, you can swap from the older version one to version three
[1978.76 --> 1979.16]  or four.
[1979.66 --> 1984.42]  And maybe you're going to save five, 10% CPU cost, depending on what kind of code you're
[1984.42 --> 1984.60]  running.
[1985.04 --> 1990.16]  And presumably if you choose a higher number and then the architecture is lower, then
[1990.16 --> 1990.78]  that's a problem.
[1991.04 --> 1993.32]  I believe it's just going to fail, refuse to run.
[1993.46 --> 1994.64]  It's going to say not supported.
[1994.98 --> 1995.18]  Yeah.
[1995.54 --> 1996.24]  Okay, cool.
[1996.40 --> 1997.08]  Yeah, makes sense.
[1997.08 --> 1997.88]  Huh?
[1998.24 --> 1998.88]  Yeah, there you go.
[1998.94 --> 1999.62]  That's good to know.
[1999.94 --> 2000.28]  Yeah.
[2000.42 --> 2006.38]  I mean, I often I'm so abstracted from the physical hardware in certain environments where
[2006.38 --> 2008.54]  that wouldn't be able to make use of that.
[2008.60 --> 2012.56]  But there's certainly some cases where I could probably use that today.
[2012.92 --> 2014.80]  I appreciate you telling me about that one.
[2015.14 --> 2018.16]  And even if you think, well, my workload is not that special.
[2018.16 --> 2024.50]  I believe in Go AMD 64 version three, there's an instruction that the runtime garbage collector
[2024.50 --> 2030.26]  can use to quickly scan memory for pointers or something like that in a way that essentially
[2030.26 --> 2031.94]  batches the work and makes it a lot faster.
[2032.42 --> 2037.64]  So you might get the runtime GCs being like a few percent faster, even if you don't care
[2037.64 --> 2038.66]  about new CPUs.
[2038.66 --> 2044.12]  So even if you're not going to make use of it, maybe the Go tooling and runtime and bits
[2044.12 --> 2045.52]  and pieces do.
[2045.72 --> 2046.50]  Very interesting.
[2047.08 --> 2051.32]  I do want to speak about one more subject before we get onto workspaces if we can.
[2051.46 --> 2053.18]  And this is something I use a lot.
[2053.26 --> 2055.32]  And these are the templates in Go.
[2055.32 --> 2059.30]  So we've got text template and HTML template.
[2059.80 --> 2064.62]  And these sometimes get criticized as being too rudimentary and too low level.
[2065.68 --> 2068.60]  But it sort of has enough of what you need.
[2068.70 --> 2073.40]  As long as you mix in Go code, usually in functions that you make available to the templates,
[2073.88 --> 2075.60]  you can kind of really do everything you need.
[2076.08 --> 2078.76]  But are we getting some new functionality in templates?
[2079.34 --> 2079.48]  Yeah.
[2079.72 --> 2083.42]  So I added a couple here, which are pretty simple to understand, I think.
[2083.42 --> 2088.08]  They both revolve around control flow or logic, if you want to think of it that way.
[2088.40 --> 2090.62]  So one is about adding break and continue.
[2090.94 --> 2096.32]  So it's the same feature that you have in regular Go loops, but for ranges within a template.
[2096.86 --> 2104.72]  And the other one is that the AND and OR operators in Boolean expressions now short circuit in a
[2104.72 --> 2110.62]  template like in Go, which means that if you do A or B and A is true, then B is not evaluated.
[2111.02 --> 2113.26]  Whereas right now it evaluates all the expressions.
[2113.42 --> 2115.98]  And then works out the Boolean expression.
[2116.46 --> 2116.56]  Yeah.
[2116.68 --> 2120.26]  And the result on the expression itself is the same, isn't it?
[2120.32 --> 2124.82]  But if you like you're calling functions within that, then you can save those functions.
[2124.92 --> 2126.02]  They won't need to get called.
[2126.46 --> 2128.82]  So that short circuiting sometimes is very important.
[2129.38 --> 2130.72]  That's very nice to know.
[2131.14 --> 2135.08]  So the break and continue, I guess they are quite simple then.
[2135.08 --> 2137.70]  So continue is going to loop back.
[2138.26 --> 2140.86]  And well, actually, I'm not sure that is that simple.
[2141.22 --> 2143.88]  Because the template is kind of declarative, isn't it?
[2144.34 --> 2145.88]  What does the continue do then?
[2146.26 --> 2150.68]  What happens if there was within the block, like content after the continue?
[2150.92 --> 2151.68]  Is that skipped?
[2151.68 --> 2155.20]  So you can think of templates as sort of scripts.
[2155.68 --> 2159.82]  I don't believe they let you run code forever, at least not that I can remember.
[2159.94 --> 2164.14]  But they do have a range statement where you can say range over, for example, a slice.
[2164.14 --> 2169.18]  And then within that body, you can set variables or you can template some.
[2169.48 --> 2172.52]  Like if you just type something without using the brackets, right?
[2172.54 --> 2174.52]  That's going to be output as part of the template.
[2174.98 --> 2175.06]  Yeah.
[2175.16 --> 2178.96]  If you have two blocks of code within a range and in between you say continue,
[2179.14 --> 2180.62]  then the second block is going to be omitted.
[2180.80 --> 2183.02]  And then you're going to go back to the top of the range, right?
[2183.36 --> 2183.52]  Yeah.
[2183.56 --> 2183.78]  Okay.
[2183.82 --> 2185.56]  So that is how it works and goes.
[2185.66 --> 2186.78]  So that should feel quite natural.
[2186.78 --> 2188.78]  But that is quite unusual for templating.
[2189.10 --> 2190.48]  I don't think I've seen that before.
[2190.58 --> 2191.38]  It is a bit unusual.
[2191.52 --> 2191.76]  Yes.
[2192.16 --> 2192.54]  Very cool.
[2192.54 --> 2197.58]  Well, we have somebody here, of course, Michael Matloub,
[2197.82 --> 2202.62]  who has done a fair bit of work recently on workspaces.
[2202.98 --> 2205.58]  And this is coming in Go 118.
[2205.96 --> 2208.98]  Michael, could you just tell us briefly what are Go workspaces?
[2209.08 --> 2210.22]  What problem do they solve?
[2211.00 --> 2216.28]  So just like at a simple level, the Go command in the module mode
[2216.28 --> 2220.34]  allows you to have a single main module that you're working on, right?
[2220.34 --> 2224.82]  Like that's the module that your current directory is in.
[2225.38 --> 2232.34]  And all the files in the module, all the packages in the module are like the modules that are the packages that Go builds by default.
[2232.34 --> 2241.02]  And if you have any other code on disk, previously you would have to like add replaces or other ways of kind of getting it in,
[2241.30 --> 2245.38]  which are kind of annoying if you want to make changes across modules.
[2245.48 --> 2248.34]  It was hard to work across two modules at the same time, basically.
[2249.04 --> 2252.40]  Now, workspaces allow you to have more than one main module.
[2252.40 --> 2260.04]  Those are modules where you are making edits and Go builds from rather than getting it from a specific version.
[2260.76 --> 2264.42]  And so Workspace is allowed you to say, these are the modules on this that I'm working on.
[2264.72 --> 2274.06]  And those are like the base that the minimal version selection uses when computing its dependency graph.
[2274.06 --> 2282.36]  So we think this is going to be useful because we've gotten a lot of feedback from people who work across multiple modules.
[2282.52 --> 2288.06]  In fact, that was like one of the number one complaints we saw in the Go user survey.
[2288.62 --> 2295.76]  People working with modules that they had problems when they were working on multiple modules, they found it cumbersome.
[2296.44 --> 2300.66]  And so we hope that multi-module workspaces make that workflow a lot easier for them.
[2301.06 --> 2303.08]  Yeah, this is definitely something I've encountered.
[2303.08 --> 2306.84]  Do you think people were like overusing modules?
[2307.44 --> 2311.18]  Do you think that there's like, you know, we were doing something wrong?
[2311.26 --> 2314.42]  It felt like that because we were kind of fighting with the tools a little bit.
[2314.80 --> 2317.18]  What do you mean overusing modules?
[2317.54 --> 2322.10]  Well, I mean, like sometimes in a project, you have like multiple packages.
[2322.78 --> 2328.40]  Sometimes people will, each one of those would be a module instead of just a package inside this bigger module.
[2328.58 --> 2329.36]  Things like that.
[2329.36 --> 2349.22]  Yeah, I feel like one thing that we learned after, you know, some experimentation with modules, like after some time using like Vgo and then modules in the Go command, we learned that multi-module repositories are, they should be rare.
[2349.22 --> 2353.22]  They have a lot of surprises when you're working with them.
[2353.22 --> 2371.84]  And so like now our general recommendation is for people to usually have like one module per repository unless there's a specific, very rare set of use cases where they wanted to have a sub module in their module.
[2371.84 --> 2378.92]  So in that sense, yeah, I guess people, we were overusing modules because we were learning how to use modules.
[2379.26 --> 2384.08]  And now those modules exist and we kind of have to work with them.
[2384.36 --> 2384.50]  Yeah.
[2384.70 --> 2391.52]  I think for like packages and things for if you're releasing a library that people are going to use, I think that's kind of great advice.
[2391.66 --> 2395.22]  Definitely a time I've seen where multiple modules exist is if you have a mono repo.
[2395.22 --> 2403.62]  And the way that you would do it at the moment, I use Visual Studio Code, you basically open the folder, the subfolder just as the root.
[2403.90 --> 2406.94]  And that's essentially like that becomes the context of that module.
[2407.16 --> 2408.80]  And that's a way to get around it.
[2408.86 --> 2415.42]  If you have multiple folders and they have modules in different ones, the workspaces, I think, is going to enable that now.
[2415.52 --> 2417.70]  So you'll be able to operate, right?
[2417.70 --> 2418.34]  Yeah.
[2418.58 --> 2435.72]  I mean, one of the driving forces behind us starting to work on modules was the user experience in not just Visual Studio Code, but like any editors that use Go, please, which kind of powers the Visual Studio Code Go experience.
[2435.72 --> 2443.82]  The team was thinking of different ways of representing multiple modules and providing that information to the Go command.
[2444.44 --> 2450.56]  But it had to like kind of introduce a new concept that like didn't exist in the Go command.
[2450.64 --> 2455.14]  Like the Go command had no concept of like people working in multiple modules at the same time.
[2455.20 --> 2458.64]  It just had, you know, replace directives or requirements.
[2458.64 --> 2465.24]  And so we decided like the best thing to do is to like make this a first class feature of the Go command.
[2465.54 --> 2476.42]  So not only could Go please use it, but users who introduce modules can then open up, you know, command line and the Go command understand that they're working in the same workspace and the same set of modules.
[2477.28 --> 2479.34]  So how does it actually work in practice then?
[2479.42 --> 2482.16]  Do you have to like set up a workspace?
[2482.38 --> 2484.72]  Is this a new concept of a thing you create?
[2485.06 --> 2485.62]  Yes.
[2485.62 --> 2490.10]  So we have Go.mod files and now we have Go.work files.
[2490.48 --> 2492.00]  So you create a Go.work file.
[2492.12 --> 2494.40]  The syntax is very similar to Go.mod.
[2494.58 --> 2496.48]  We want it to be easy for people to pick up.
[2497.10 --> 2502.02]  And the Go.work has one new directive is the use directive.
[2502.44 --> 2506.06]  So you tell it which directories you want it to use.
[2506.40 --> 2513.82]  And all the modules in those directories, if you're under the Go.work file, the same way you're under a Go.mod file before, are in your workspace.
[2513.82 --> 2518.46]  So you make your Go.work file and CD under it.
[2518.62 --> 2524.62]  And now you're using all those modules and any builds that you do or Go list or any such command like that.
[2525.08 --> 2529.62]  And it's going to be aware of those other modules and you're not going to be fighting the tools anymore.
[2530.00 --> 2530.18]  Yep.
[2530.18 --> 2532.68]  And can you do replaces as well in there?
[2532.90 --> 2533.50]  You can.
[2534.14 --> 2540.68]  We don't think people should need to add replaces except in like very specific circumstances.
[2540.82 --> 2547.54]  We actually added replace because if you have multiple modules in your workspaces, they might have conflicting replaces.
[2547.54 --> 2553.48]  And so the replacing the Go.work file can override the replaces that are fighting.
[2554.42 --> 2562.22]  But if you wanted to use a specific module, then usually the right thing to do is just use that module in your Go.work file.
[2562.70 --> 2562.84]  Yeah.
[2563.10 --> 2568.70]  So I feel like lots of tools probably got touched by adding this kind of support.
[2569.02 --> 2570.88]  Was it a difficult one to get in?
[2571.22 --> 2574.90]  Most of the work was in the Go command itself.
[2574.90 --> 2584.14]  I mean, there is definitely like an amount of complexity in the Go command because our module loading code does more than you'd think.
[2584.80 --> 2590.80]  But once we got it to work in the Go command, one of the nice things is most of our tools call into the Go command.
[2591.56 --> 2602.10]  And so, you know, as long as they're making a call into the, you know, Go packages or the Go command, they kind of get all that for free as long as the Go.work file exists on disk.
[2602.10 --> 2612.88]  You know, we've had to like make on the VS Code Go and Go please teams, they've made changes to understand Go.work files and pass them into the Go command.
[2613.20 --> 2618.24]  But, you know, once you pass it in, like all the hard work is done by the Go command itself.
[2618.72 --> 2620.62]  This is a really nice thing to have.
[2620.92 --> 2624.00]  In the way that I work, this is going to change a lot.
[2624.26 --> 2627.44]  There's an experiment for a while where you could try this out.
[2627.44 --> 2628.18]  Wasn't there?
[2628.40 --> 2629.52]  With an environment variable.
[2629.84 --> 2644.98]  Yeah, we, you know, I filed a proposal for this and I made it available and we had a link for people to easily download like a development version that included these changes using the Go tip command.
[2645.70 --> 2647.56]  And so people could try it and give feedback.
[2648.40 --> 2651.28]  And we got some feedback on it, which was super helpful.
[2651.28 --> 2656.60]  And we got a lot of feedback on the issue too, which was very helpful in developing the issue.
[2657.02 --> 2658.60]  So, or the proposal.
[2659.48 --> 2665.62]  So, yeah, I mean, hopefully we've addressed most of the important issues people have.
[2665.84 --> 2667.72]  For anything else, there's 119.
[2669.40 --> 2669.80]  Absolutely.
[2670.18 --> 2673.86]  Well, no, I mean, honestly, I think these kinds of things make such a difference.
[2674.06 --> 2675.26]  So we're so pleased.
[2675.26 --> 2679.50]  And honestly, I feel like there's a lot more to talk about with workspaces and modules.
[2679.62 --> 2684.80]  Maybe, Michael, you could come back one day and we'll do like a modules and workspaces special.
[2685.18 --> 2685.60]  Oh, sure.
[2685.72 --> 2686.44]  I'd love to.
[2686.72 --> 2687.00]  Yeah.
[2687.48 --> 2688.16]  Okay, cool.
[2688.24 --> 2689.74]  Well, we will hold you to that.
[2689.88 --> 2691.72]  I do consider this to be legally binding.
[2692.10 --> 2693.60]  Like the pinky promises?
[2694.08 --> 2696.94]  Pinky promises are of all the types of promise.
[2697.08 --> 2698.56]  I think they're up there, aren't they?
[2698.60 --> 2700.38]  With the most important, aren't they?
[2700.92 --> 2701.98]  Pinky, you know what I mean?
[2701.98 --> 2704.98]  You've got like local kind of laws.
[2705.20 --> 2707.50]  You've got like national laws.
[2707.88 --> 2712.48]  And then all the way at the top, after the Supreme Court, you've got the little pinky promise there.
[2712.84 --> 2714.46]  It's been pinky promise at the top.
[2714.56 --> 2715.04]  I got it.
[2715.44 --> 2716.32]  Yeah, I think that's how it works.
[2716.38 --> 2719.08]  I think that's the legal structure of the pinky promise.
[2719.46 --> 2721.42]  Well, here's another pinky promise.
[2721.58 --> 2724.36]  I promise you're about to hear some unpopular opinions.
[2728.36 --> 2730.08]  Unpopular opinions.
[2730.84 --> 2731.18]  What?
[2731.18 --> 2733.02]  I actually think should probably leave.
[2736.36 --> 2737.92]  Unpopular opinions.
[2741.86 --> 2742.34]  Okay.
[2743.74 --> 2745.80]  Who's going to go first with...
[2745.80 --> 2747.44]  I don't know why I'm speaking in the spooky voice.
[2747.60 --> 2749.54]  Who wants to say the first unpopular opinion?
[2750.00 --> 2751.48]  So maybe I can start with mine.
[2751.98 --> 2756.20]  Mine is that I think code generation should be avoided whenever possible.
[2756.20 --> 2761.14]  I think the main reason for that is because it adds developer friction.
[2761.54 --> 2764.64]  It often increases build size and build time.
[2765.18 --> 2769.60]  And oftentimes people overestimate how slow reflection is.
[2769.76 --> 2773.04]  If you use reflection well, the cost is actually very reasonable.
[2773.26 --> 2776.96]  And it's not like you're building your whole program around reflection.
[2776.96 --> 2779.92]  You're using it in very careful ways in small places.
[2780.80 --> 2782.14]  What do you think of that, Michael?
[2782.52 --> 2787.92]  I guess I don't have like a very strong opinion about this either way.
[2787.92 --> 2788.68]  I do.
[2788.98 --> 2789.38]  Yes?
[2790.02 --> 2791.04]  Let's hear your opinion.
[2791.14 --> 2793.96]  Is it the popular or unpopular variety?
[2794.22 --> 2800.02]  The thing is, I love CodeGen because it's like you're doing loads and loads of typing.
[2800.28 --> 2802.90]  You just do a bit of typing and you run a command.
[2803.70 --> 2806.64]  And it's like, oh, it's like you've done loads of typing.
[2806.64 --> 2807.68]  So that's the thing.
[2808.40 --> 2811.00]  Reflection's hard, so it's quite satisfying when you get it right.
[2811.36 --> 2817.36]  But editing a template and then running a thing and having 1,200 methods update,
[2817.94 --> 2820.64]  you've like fixed 1,200 bugs at the same time.
[2821.38 --> 2822.62]  What do you think of that, Michael?
[2822.98 --> 2823.86]  I will say this.
[2824.16 --> 2831.02]  I find that working with code generation when using the Go command is not very fun.
[2831.52 --> 2833.22]  I don't like using Go Generate.
[2833.22 --> 2836.30]  I don't think it has a good user experience.
[2836.30 --> 2841.88]  It happens separate from the build, so it's really easy to have stale files.
[2842.62 --> 2846.70]  You know, I feel like this ship has sailed, but if you're going to do a lot of code generation,
[2847.16 --> 2854.12]  Bazel is very nice for that, but it's not very heavily used in the Go community.
[2854.60 --> 2857.44]  I mean, I miss inside of Google, right?
[2857.68 --> 2861.80]  We use mostly generated protos, right?
[2861.80 --> 2868.48]  And it's seamless because the build just generates them automatically and you don't need to think about them.
[2868.80 --> 2874.96]  And the tools take care of all of the annoyances that are caused by code generation.
[2875.42 --> 2883.06]  But our tools don't really do that, so there's a lot of friction when using generated code outside of those build systems.
[2883.06 --> 2885.68]  So I get pretty annoyed.
[2885.86 --> 2890.50]  If I have to run a make before my Go build, I feel like there's a problem.
[2891.28 --> 2892.84]  That's kind of answering a different question.
[2893.20 --> 2893.48]  But, you know.
[2894.24 --> 2898.22]  I think generics, oh, I've said it, are going to get booted out here.
[2898.30 --> 2901.74]  But I think this rule obviously is very weakly enforced.
[2902.50 --> 2904.14]  So much for pinky promises, eh?
[2904.54 --> 2907.48]  After I was bigging them up and giving them all that legal weight.
[2907.62 --> 2908.26]  Look at it now.
[2908.74 --> 2911.00]  It's been reduced to a silly, childish thing.
[2911.00 --> 2911.88]  How sad.
[2912.80 --> 2919.14]  Well, what I was saying is I think generics are going to get rid of a lot of cases for code generation.
[2919.42 --> 2925.12]  But reflection is pretty difficult to write because there's no kind of feedback.
[2925.32 --> 2930.08]  Like you need unit tests really for your feedback to, I mean, you don't really need that.
[2930.32 --> 2931.42]  Let me rephrase that.
[2932.14 --> 2936.60]  I think reflection is quite hard to get right because it's that sort of metaprogramming.
[2936.60 --> 2944.10]  But then code generation templates are also metaprogramming and they are often quite difficult to look after and maintain.
[2944.66 --> 2945.70]  So maybe you've got some legs.
[2946.14 --> 2950.50]  I'll be interested to find, to test this one on Twitter at GoTimeFM.
[2950.60 --> 2954.36]  We will tweet out a poll and find out if this really isn't popular.
[2954.82 --> 2956.04]  It's a candidate for one though.
[2956.16 --> 2956.74]  It's a good one.
[2957.24 --> 2959.44]  Can you beat him, Michael, is the question.
[2959.44 --> 2963.24]  My unpopular opinion is we should bring back the TriProposal.
[2963.40 --> 2964.00]  Oh, really?
[2964.18 --> 2977.10]  And this is where I'm going to not mention the other features by name, but I'll say of all the features that people have proposed to the Go, as language changes to the Go language,
[2977.10 --> 2983.86]  I feel like none have been as potentially impactful as the TriProposal was.
[2983.98 --> 2994.84]  And I was sad to see it pulled back because I think error handling properly is really important to writing good code, good Go code.
[2995.50 --> 3002.50]  And I think the language ergonomics should encourage people to handle their errors properly.
[3002.50 --> 3013.04]  And so often people will just, if error does not equal nil, return error and just not think about what they're doing with their errors.
[3013.38 --> 3027.90]  And I feel like Tri gave an opportunity to think a little bit harder about wrapping errors properly and what to do with errors and kind of nudged people to do the right thing a little bit more.
[3027.90 --> 3035.18]  And certainly the proposal, as it was, needed more work before it should go in.
[3035.58 --> 3042.70]  But I really do think we should bring back the TriProposal and keep working on it and make it better.
[3043.10 --> 3047.62]  I don't know when we'll have the bandwidth for another big language change like that.
[3047.92 --> 3049.64]  I have to agree with Michael.
[3049.64 --> 3056.74]  I think the reason the TriProposal got so much bad feedback is sort of the, because Go is so opinionated,
[3056.92 --> 3061.40]  a lot of its users have gone into this mentality of Go doesn't need features.
[3061.92 --> 3071.56]  So sometimes the users can have this knee-jerk reaction of somebody proposes a change to the language and they go, well, but that wouldn't be Go, right?
[3072.02 --> 3074.06]  And I think I agree with Michael in the case of Tri.
[3074.14 --> 3076.82]  I think it would have been a very interesting change and I hope it comes back.
[3076.82 --> 3078.90]  So just refresh our memories.
[3079.00 --> 3079.74]  What did Tri do?
[3080.30 --> 3090.92]  Yeah, so basically it gave you a mechanism to try with an expression that returned an error as its final function,
[3091.12 --> 3092.82]  that returned an error as its final argument, right?
[3093.10 --> 3096.92]  And then it would allow you to handle that error elsewhere.
[3097.48 --> 3102.34]  So you could add like, I think in one of the variations of the proposal,
[3102.34 --> 3107.24]  there was like a handle for handling like a number of tries in a function.
[3107.98 --> 3113.40]  I think in another one, if I'm remembering correctly, recover was an option for handling the error,
[3113.84 --> 3119.14]  but you could kind of have the errors handled in like a single place.
[3119.72 --> 3126.44]  I mean, basically like people realize that error handling is awkward in Go and the awkwardness, I think,
[3126.50 --> 3128.10]  causes people to take shortcuts.
[3128.10 --> 3132.98]  And so addressing that awkwardness and nudging people towards doing the right thing,
[3133.04 --> 3136.84]  especially if, you know, try and handle came with helpers.
[3136.96 --> 3143.88]  And now we do have like functions like errors, is, and as that like help people with like wrapping errors.
[3144.12 --> 3151.02]  Like those together would like provide a better model for handling errors and for people to think about handling errors.
[3151.54 --> 3153.12]  Wow. Fascinating stuff there.
[3153.12 --> 3158.38]  Yeah. Yeah. I tell you what, that's, it's interesting because I think, see, when I handle errors,
[3158.74 --> 3164.02]  and I don't know if I do this different to other people, I think that there may be, I may be unusual in this,
[3164.10 --> 3169.82]  but I will wrap, when I return the error, I added quite a bit of context there.
[3170.26 --> 3171.60]  So each one is different.
[3171.72 --> 3175.48]  I'll add and I'll include the thing it's trying to do in that wrapped error.
[3175.48 --> 3181.68]  So it's not that I'll have a wrap where I just put the method name or whatever into the error.
[3182.00 --> 3183.60]  And it's the same every time.
[3184.02 --> 3190.66]  So if it was the same every time, like having it pulled out and have it deal with it in one place is kind of quite nice.
[3191.12 --> 3196.36]  But yeah, the other thing is, I mean, this doesn't hurt that, but I do like that error handling is at least explicit.
[3196.36 --> 3205.22]  Like, and I think the tried proposal didn't really interfere with that, but I like the fact that in Go, we see, we are kind of handling errors.
[3205.42 --> 3214.92]  Even if you are just returning it, it's like, as long as you're not forgetting about it, you know, it's kind of, it's nice that they are in the forefront of our minds when we're coding.
[3215.04 --> 3220.66]  I literally was writing something today and I literally had to write if error doesn't equal nil.
[3220.66 --> 3224.86]  And then I had to stop and think, oh, what do I do if this errors?
[3225.12 --> 3230.18]  Like that actually is a bit of a, not a trivial problem in this particular case.
[3230.36 --> 3232.40]  I wasn't able to just return an error.
[3232.82 --> 3234.22]  You know, I had to handle that.
[3234.46 --> 3239.14]  So I quite like that it's in the forefront, at least of the language, but yeah, interesting.
[3239.28 --> 3244.38]  We'll, we'll, we'll definitely find out what our other people think on Twitter when we post that one.
[3244.44 --> 3245.30]  It's going to be very interesting.
[3245.30 --> 3245.60]  Yeah.
[3245.90 --> 3246.32]  I think.
[3246.52 --> 3251.14]  I'm interested in seeing how unpopular that, that, that is.
[3251.60 --> 3256.12]  Could, do you think that could go for the most unpopular opinion expressed in one of these segments?
[3256.40 --> 3260.30]  It could do, or you might surprise us and maybe everyone's like, yeah, we loved that.
[3260.86 --> 3267.20]  And honestly, I think that, I think that point of like, we're now so familiar with Go, we, we have to be careful.
[3267.34 --> 3274.24]  We don't just become curmudgeons about it and resist any change, you know, because, you know, we do, it should change.
[3274.24 --> 3274.82]  It should evolve.
[3274.92 --> 3276.58]  It should get better, like all software.
[3276.88 --> 3280.40]  So I kind of like, yeah, interested to hear what people think of that.
[3280.58 --> 3286.98]  I think Michael also needs to think that if this opinion is going to be really unpopular, then Try is not going to come back.
[3287.22 --> 3288.66]  So you want it to be very popular.
[3289.12 --> 3291.56]  I hope it's, I mean, I would like for it to be popular.
[3292.16 --> 3292.32]  Yeah.
[3292.56 --> 3295.80]  That's not really in the spirit of the segment, but that's fine.
[3295.98 --> 3297.86]  I think it is unpopular, but.
[3298.16 --> 3298.96]  Well, we'll find out.
[3298.96 --> 3306.26]  If it's an opinion that I hold, I, I, you know, I would like it to be less unpopular, even though it is unpopular.
[3306.80 --> 3311.22]  Sometimes, you know, when the case is made, in fact, it's hard to get unpopular opinions.
[3311.36 --> 3315.14]  This is what we've found because people make the case so eloquently like you did.
[3315.40 --> 3320.12]  And then people on, on Twitter, you know, they're easily swayed.
[3320.36 --> 3321.46]  They'll believe that now.
[3321.46 --> 3332.54]  I mean, if I can make reference to the G word again, there was a time in the community where you brought up the G word and people are like, no, not in my go.
[3332.88 --> 3337.48]  And they, people were right to be worried about, you know, those things.
[3337.54 --> 3340.60]  But I, I think like the case was made.
[3340.60 --> 3355.30]  People worked really hard to present the case, why it would actually be an improvement and really convince people, like convince people who use Go that it was actually going to be a net positive.
[3355.56 --> 3364.92]  And I, I think the sentiment now towards the G word is a lot more positive than, than it was five or six years ago.
[3365.50 --> 3367.20]  Yeah, that is definitely true.
[3367.20 --> 3373.68]  And then the counter is, you know, we don't want it to be too easy to change things because of the backwards compatibility promise.
[3373.86 --> 3380.98]  I do quite like the fact that it's quite a rigorous process before we really get any big changes like this.
[3381.16 --> 3383.20]  I think that's, there's value in that too.
[3383.50 --> 3386.12]  So that really only the only good stuff is going to get through.
[3386.40 --> 3386.84]  Hopefully.
[3387.52 --> 3392.18]  Every new thing we add is something we have to maintain forever.
[3392.80 --> 3396.62]  We do have to be careful about adding new things for sure.
[3396.62 --> 3396.98]  Yeah.
[3396.98 --> 3398.46]  Because forever is ages, isn't it?
[3398.52 --> 3399.30]  It's a pretty long time.
[3399.80 --> 3400.10]  Yeah.
[3400.76 --> 3403.52]  I also remember somebody recently criticizing Go.
[3403.70 --> 3412.86]  I think it was on Hacker News saying something along the lines of, Go is a popular language that has ignored all the programming language development in the past 15 years.
[3413.44 --> 3415.78]  But that's kind of why it works, right?
[3415.82 --> 3420.04]  Because it, it, it only builds on top of what has been well tested.
[3420.04 --> 3425.90]  And I think the only major exception there is modules, which goes against everything else that has been done in package management.
[3426.40 --> 3426.42]  Yeah.
[3426.46 --> 3427.34]  That's quite interesting.
[3427.62 --> 3429.22]  It is a very stable thing.
[3429.22 --> 3434.26]  And yeah, that other thing of having lots of different ways to do the same thing.
[3434.26 --> 3441.28]  In JavaScript, like you almost have to learn a particular flavor of JavaScript now in order to contribute to a project.
[3441.72 --> 3448.28]  Some are using all the latest language features and like the little arrows for functions and things like this.
[3448.28 --> 3450.34]  And you sort of have to learn all that.
[3450.64 --> 3450.82]  Yeah.
[3451.02 --> 3472.14]  I mean, I find that sad from the other side, you know, JavaScript and all the other parts of the web ecosystem have become so big that it is impossible for anyone to make a new JavaScript interpreter engine without the resources of a huge multinational corporation.
[3472.56 --> 3473.60]  That sucks.
[3473.60 --> 3477.98]  Well, I'm afraid that's all the time we have on that somber note.
[3479.26 --> 3483.52]  You can forget about your dreams of writing your own JavaScript engine.
[3483.82 --> 3484.70]  It's not going to happen.
[3485.74 --> 3487.02]  So just wake up.
[3487.22 --> 3487.36]  Sorry.
[3487.72 --> 3488.72]  No, it's, it's harsh.
[3488.88 --> 3491.00]  It's a harsh wake up call, Michael, but we needed it.
[3491.12 --> 3491.86]  Thank you very much.
[3493.14 --> 3496.52]  Thank you so much to our guests today.
[3497.48 --> 3500.98]  Michael Matloub joined us, as did Daniel Marti.
[3501.32 --> 3502.80]  It was a pleasure as always.
[3502.80 --> 3503.76]  Thank you very much.
[3503.84 --> 3505.04]  Thanks for joining us on GoTime.
[3505.22 --> 3505.70]  Thanks to me.
[3505.90 --> 3506.72]  We'll see you next time.
[3507.46 --> 3512.48]  All right.
[3512.62 --> 3514.22]  That is GoTime for this week.
[3514.76 --> 3517.24]  What are you most excited about in Go 1.18?
[3517.62 --> 3518.26]  Is it fuzzing?
[3518.86 --> 3519.34]  Generics?
[3519.86 --> 3520.96]  Something we talked about today?
[3521.34 --> 3522.90]  Let us know in the comments.
[3523.40 --> 3524.76]  Just pop open your show notes.
[3525.04 --> 3528.48]  Click the discuss on changelog news link and let your voice be heard.
[3528.48 --> 3532.78]  And if you're a long time listener, do us a solid and tell a friend about the show.
[3532.98 --> 3534.90]  It is the best way for you to support GoTime.
[3535.22 --> 3539.34]  Of course, we have our changelog++ membership, which is awesome and gets you closer to the metal.
[3539.52 --> 3545.20]  But if you want to pitch in, we would love a tweet, a blog post, a Reddit thread, however it is that you like to socialize.
[3545.20 --> 3553.16]  Thanks again to Fastly for being our CDN partner for all these years, to Brakemaster Cylinder for keeping our beats fresh, and to you for listening.
[3553.38 --> 3554.24]  We appreciate you.
[3554.48 --> 3557.26]  An episode on GraphQL is in the pipeline.
[3557.60 --> 3560.34]  In fact, it's coming up next time on GoTime.
[3560.34 --> 3576.68]  Game on.
