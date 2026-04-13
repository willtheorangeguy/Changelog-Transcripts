[0.00 → 3.00] So for anyone not familiar, Go does have GOTO.
[3.24 → 5.46] If you want to listen back to Johnny's pun earlier,
[5.56 → 9.36] it's actually a double pun because he had the word Go in it and GOTO.
[9.92 → 13.26] They were responsible for spaghetti code, essentially,
[13.62 → 16.04] because that's how you used to write code in basic.
[16.04 → 20.00] You'd have line IDs, every ID like 10, 20, 30,
[20.18 → 22.00] and then the code was on those lines.
[22.50 → 23.80] They went up in tens, by the way,
[23.84 → 27.24] so that you could insert other instructions between.
[27.24 → 28.16] Later on, yeah.
[28.16 → 31.04] Yeah, because you've already put your number in, so it's too late.
[31.84 → 34.54] I don't know when they came up with dynamic line numbers,
[34.76 → 38.00] but that changed the world, let me tell you.
[40.32 → 42.92] Bandwidth for Changelog is provided by Vastly.
[42.92 → 45.10] Learn more at Fastly.com.
[45.34 → 47.64] Our feature flags are powered by Launch Darkly.
[47.90 → 49.72] Check them out at LaunchDarkly.com.
[49.98 → 51.80] And we're hosted on Leno cloud servers.
[52.20 → 55.74] Get $100 in hosting credit at Leno.com slash Changelog.
[58.16 → 62.06] Whether you're working on a personal project or managing enterprise infrastructure,
[62.38 → 66.36] you deserve simple, affordable, and accessible cloud computing solutions
[66.36 → 68.92] so you can take your project to the next level.
[69.38 → 72.94] Simplify your life with Leno's Linux VMs to develop, deploy,
[73.12 → 75.78] and scale your applications faster and easier.
[76.34 → 80.32] Get started on Leno today with $100 in free credit for our listeners.
[80.32 → 84.12] You can find all the details at Leno.com slash Changelog.
[84.22 → 88.58] Or if you're not at your desk, just text Changelog to 474747
[88.58 → 90.44] and get instant access to that $100.
[90.98 → 96.68] Linde has 11 global data centres and provides 24-7, 365 human support
[96.68 → 100.08] with no tiers or handoffs, regardless of your plan size.
[100.32 → 102.78] In addition to shared and dedicated compute instances,
[103.08 → 106.50] you can use that $100 credit on S3-compatible object storage,
[106.72 → 108.26] managed Kubernetes, and more.
[108.26 → 114.00] Visit Leno.com slash Changelog and click on the Create Free Account button to get started.
[114.28 → 116.76] Or just text Changelog to 474747.
[117.28 → 118.90] Get started today on Linde.
[129.50 → 130.50] Let's do it.
[131.06 → 132.12] It's go time.
[132.80 → 137.60] Welcome to Go Time, your source for diverse discussions from around the Go community.
[137.60 → 142.56] If this is your first time listening, subscribe now at go time.fm.
[143.04 → 146.58] Stay tuned for all three of our Gopher Con episodes.
[146.82 → 148.58] What to expect when you're not expecting?
[148.94 → 150.22] The secret life of gophers.
[150.54 → 153.82] And we don't call it Jeopardy, but we do call it Go Panic.
[154.06 → 154.94] All right, let's do this.
[155.46 → 156.48] Here we go.
[156.48 → 156.98] Hello.
[164.98 → 166.12] Welcome to Go Time.
[166.40 → 167.10] I'm Matt Riot.
[167.22 → 170.80] Today we're talking about what you would remove from Go.
[171.42 → 171.74] Hmm.
[172.06 → 173.62] Curious subject, you may think.
[173.84 → 176.72] Well, unpicking it with me, John Calhoun.
[177.00 → 177.48] Hello, John.
[177.86 → 178.22] Hey, Matt.
[178.62 → 179.12] How's it going?
[179.66 → 180.70] It is going pretty well.
[181.36 → 182.20] Glad to hear that.
[182.52 → 184.14] We've also got Johnny Portico here.
[184.24 → 185.42] Johnny, how's it going for you?
[185.42 → 186.28] Pretty well also.
[187.24 → 188.44] Yeah, I have my milk.
[188.78 → 193.42] And I've come to the show about where everything is going to be an unpopular opinion from what
[193.42 → 193.68] I hear.
[193.74 → 194.18] So I'm ready.
[195.28 → 196.02] Okay, yeah.
[196.52 → 198.30] Yeah, this is going to be an interesting one.
[198.62 → 202.24] We also have Daniel Marty who is also joining us.
[202.44 → 202.90] Hello, Daniel.
[203.36 → 203.54] Hi.
[203.72 → 204.34] Happy to be back.
[205.16 → 206.34] Yeah, you're more than welcome.
[206.70 → 207.92] Thanks for joining us.
[207.92 → 214.76] I wonder if it's worth, very first, just let's talk about why this subject turns out to be
[214.76 → 216.18] quite an interesting subject.
[217.00 → 222.50] You know, we do tend to kind of, as developers, we're very focused on what's new and new features.
[222.64 → 225.98] You know, it's very exciting when there are new features in Go.
[226.12 → 230.40] And, you know, we think about generics and changes to the errors and things.
[230.40 → 232.16] It's very exciting.
[232.94 → 235.90] What's the value in taking things out of Go?
[235.98 → 238.22] Why would that be a worthwhile endeavour?
[238.74 → 243.32] Well, I think a small language is on one side easier to learn, but on the other, it's
[243.32 → 244.50] easier to read and maintain.
[245.06 → 249.52] So it happened a lot of years ago before I did Go that I would do C++ or Python.
[250.12 → 253.72] And a couple of years down the line, I would write C++ or Python differently because
[253.72 → 255.24] the language is so fast.
[255.90 → 257.70] And I would just not be able to read my own code.
[257.94 → 261.70] And with Go, that doesn't happen nearly as often because the Go code you write today is
[261.70 → 266.16] very similar to how you write Go, like in five years or five years ago, for the most part.
[266.72 → 266.82] Yeah.
[267.24 → 272.26] I'd say another part to that is that any friction you can remove from teammates is useful.
[272.60 → 276.86] So not having people bicker about the correct way to instantiate a variable or anything like
[276.86 → 279.42] that that just gets them back to work is a useful thing.
[279.94 → 280.18] Right.
[280.18 → 285.42] So the Go Fund stuff, the fact that all the code is formatted automatically by the tooling
[285.42 → 289.04] means it's kind of takes that conversation off the table, doesn't it?
[289.30 → 289.52] Yeah.
[289.72 → 294.12] And I think anybody who's used a language with more features understands that when you have
[294.12 → 297.52] seven ways to do something, you're going to have seven different people who all think
[297.52 → 298.22] the different ways better.
[299.34 → 300.76] So that is interesting then.
[300.86 → 301.04] Yeah.
[301.36 → 306.10] A smaller language tends to only have then one way to do something.
[306.10 → 309.94] And that is quite a good goal for readability and for maintainability purposes.
[310.26 → 311.30] And also for learning.
[311.48 → 316.22] Like if you want to know how to do something, and you want to figure that out, it's easier
[316.22 → 317.90] if there's only one way you can do it.
[318.12 → 323.38] You should see like the number of ways you can add arrays together in JavaScript and stuff
[323.38 → 323.68] like that.
[323.74 → 328.48] There are some amazing and wonderful and scary things.
[328.68 → 330.50] And you don't really get that in Go.
[330.50 → 336.00] And I think sometimes people's opinion from the outside when they first see it is that
[336.00 → 338.70] it's a drawback of the language that it's so simple.
[338.90 → 341.86] But it turns out to be one of its greatest strengths, doesn't it?
[342.30 → 347.38] And I think it's multiplicative because, for example, back when I used to do Java, at least
[347.38 → 350.90] in the context of Android, you would look at the Android APIs and you would wonder like,
[351.10 → 355.46] oh, exactly what does this API do if it's not very well documented to go see the code?
[355.46 → 360.14] But then you would find a class that extends another class that extends an abstract class.
[360.42 → 363.10] And then, you know, you end up with like five layers of abstraction.
[363.94 → 366.82] And at least to me, that made it very difficult to actually see what was going on.
[366.94 → 370.44] Whereas in Go, you know, you click on the Go doc and you almost always just reach the
[370.44 → 371.14] code directly.
[372.00 → 372.04] Right.
[372.46 → 373.56] Yeah, that's very true.
[373.80 → 381.36] The class hierarchies, when that's used in the exact perfect situation, they're so powerful.
[381.86 → 383.92] But I was also guilty of this.
[383.92 → 385.34] I got addicted to that.
[385.34 → 393.66] I've built some amazing structures in types, in type hierarchies, abstract classes and generics.
[394.08 → 399.22] And in C Sharp that I was doing, you could have like generics could have also constraints
[399.22 → 399.90] on them too.
[400.02 → 401.46] So it's not just any type.
[401.64 → 404.36] The type has to be, have certain properties and things.
[404.98 → 405.90] It's amazing.
[406.08 → 410.04] And it feels very good when you can figure that out and get the code working.
[410.04 → 415.94] But when you have to then come back later, and it doesn't have to be very much time pass
[415.94 → 419.48] for my code to look like a stranger's code sometimes.
[420.18 → 421.62] And yeah, I couldn't figure it out.
[421.72 → 426.78] And so I learned the hard way to, I would just use those features in those languages very
[426.78 → 427.46] sparingly.
[427.46 → 431.88] Yeah, and I actually think this goes back to something that John said earlier, which is,
[432.02 → 435.08] you know, it's perfect for working as part of a team, because it removes a lot of
[435.08 → 435.38] friction.
[435.72 → 440.04] But at least for myself, it removes friction with myself in the past and future.
[440.62 → 444.48] Because again, you know, what I coded two years ago, I probably don't remember most of
[444.48 → 444.92] the details.
[445.60 → 450.06] So having the language be simple forces me to, I'm not going to say keep things simple,
[450.18 → 453.28] but at least it does constrain what magic I can do for sure.
[453.28 → 460.36] So simple is a very sort of subjective kind of sort of quality we sort of apply to something,
[460.46 → 460.58] right?
[460.66 → 465.34] So what's simple for me may not be simple for someone else.
[465.86 → 470.44] Even the term that we like to throw around, like readability, right?
[471.02 → 475.58] Within, you know, within the Go community, that too is quite subjective, right?
[475.58 → 483.20] So I'm wondering if any of us here in the panel know of perhaps studies or research done
[483.20 → 484.64] around sort of code readability.
[484.90 → 491.04] I'm sure I've come across one or two out there, not specifically on Go per se, but I'd be interested
[491.04 → 498.12] in sort of getting some more sort of data around the readability, right?
[498.14 → 502.18] Or the simplicity, all this sort of qualitative sort of things we're assigned to Go.
[502.18 → 507.24] I'd be interested in sort of seeing if we can prove it, right, out there.
[507.52 → 509.88] Benchmark readability somehow in code.
[510.16 → 510.40] Right.
[510.46 → 514.22] It's fascinating because, like you say, it's in some ways quite subjective.
[514.62 → 519.48] Certainly, like if you were to measure how long it took for a developer to be able to
[519.48 → 523.34] go and fix something in a certain code base, you know, something like that, and then tested
[523.34 → 523.96] that out.
[523.96 → 530.92] I could imagine some interesting kind of results, but they'd be so dependent on that individual
[530.92 → 531.44] developer.
[531.82 → 539.48] But as far as API design goes, we probably can say that, you know, less is better, less
[539.48 → 543.20] is simpler in the API surface.
[543.86 → 548.08] I mean, maybe not, because in some cases I could even imagine now saying that.
[548.08 → 553.68] I could imagine a case where adding a type really helps explain something, even though
[553.68 → 555.00] you may not have needed that type.
[555.36 → 557.42] So, yeah, it is an interesting one.
[557.78 → 557.88] Yeah.
[557.92 → 564.74] In some ways, some languages sort of embrace the notion of having like very expressive ways
[564.74 → 571.08] of sort of articulating your intent within a file or within your project, right?
[571.32 → 577.22] Having different ways of basically contextual ways of basically saying the same thing, right?
[577.22 → 582.82] But, you know, in this context, using these keywords makes the code more readable by some
[582.82 → 583.28] definition.
[583.28 → 587.66] And in that context, something that does the exact same thing, but, you know, using different
[587.66 → 590.62] keywords, you know, means more in that context, right?
[590.64 → 595.10] And I think Ruby, for example, a language I'm familiar with, it has that sort of, those sets
[595.10 → 596.84] of attributes going forward, right?
[597.02 → 601.08] You know, you might have different things that the same thing could be expressed in different
[601.08 → 601.50] ways.
[601.98 → 605.10] And Ruby has sort of valued that expressiveness of the language, right?
[605.10 → 614.20] So, in Go, what is, do we, I don't hear us talk about expressiveness of the Go language.
[614.48 → 621.22] Like we don't really, our go-to tends to be, and forgive the pun here, our go-to tends to
[621.22 → 624.12] be sort of a simplicity, right?
[624.14 → 625.00] It's simple to read.
[625.16 → 632.66] There are fewer keywords, you know, basically the whole notion that less is more, but is less
[632.66 → 637.04] really more, if I'm playing devil's advocate here, right, could having more expressive
[637.04 → 641.06] ways by some definition using, say, Ruby's definition of expressiveness, right?
[641.46 → 646.80] Would having that be, sort of allow us to write more readable code, right?
[647.46 → 651.16] Than the lack of, right, certain ways of expressing certain things.
[651.94 → 653.54] Yeah, I think that is a good point.
[654.26 → 654.42] Yeah.
[654.42 → 661.02] It's almost a subject for what we would do to kind of evolve and add to Go.
[661.40 → 664.28] But it's a fascinating one when you start to think about that.
[664.36 → 667.40] I don't know if anyone else has anything to add to that.
[667.42 → 671.64] I think there was a recent example in the direction that Johnny says, which is people
[671.64 → 675.64] wanted an idiom to remove all the elements from a map in a very fast way.
[675.64 → 680.18] And some people were arguing for some sort of built-in for that, sort of like delete,
[680.48 → 681.96] like delete all, you could imagine.
[682.28 → 686.52] But in the end, what they did was they taught the compiler to see the pattern for a simple
[686.52 → 691.38] loop to delete all the elements one by one and convert that into an efficient delete
[691.38 → 691.64] all.
[692.62 → 695.70] So it's kind of, because it's sort of a trade-off, right?
[695.74 → 699.22] Because if you add another method to delete all the elements, then suddenly people have
[699.22 → 701.72] two options and the language gets a little bit more complex.
[701.72 → 706.28] So I think it's a trade-off between, do you let people do higher level things, but then
[706.28 → 709.14] they have to choose between doing the higher level or lower level thing.
[709.68 → 714.16] I think those trade-offs also, like we talk about context a lot, but where you work and
[714.16 → 717.76] the goals of your company and the size of your company all play a big role in that.
[718.38 → 723.54] So if you were ever doing a readability study, I would almost imagine you'd have to compare
[723.54 → 728.94] like small teams using more expressive languages might be just as efficient at jumping in
[728.94 → 734.58] and, you know, to some code that's maybe new to them, but existent within the team versus
[734.58 → 738.92] like one of the things that I think makes when we say about readable for Go, one of the things
[738.92 → 742.96] for me at least is that you can jump into code that doesn't even have to come from your
[742.96 → 743.44] organization.
[743.44 → 747.70] It can come from pretty much anybody in the Go community, and you can jump in and read
[747.70 → 749.88] the code and usually, you know, help with it.
[749.88 → 755.64] But in some of these more expressive languages, because everybody sort of has opinions within
[755.64 → 759.32] your small group, you can have readable code and be very efficient with it.
[759.60 → 762.86] But once you get outside that small group, and you start working with other people who
[762.86 → 767.34] have differing opinions, then I think that's where things slow down and new developers jumping
[767.34 → 770.10] into projects probably think things are less readable.
[770.10 → 775.84] But it would be definitely interesting to see a study that, you know, evaluates that and
[775.84 → 780.56] sees like when new developers come in, especially like new grads, how quickly are they picking
[780.56 → 782.00] this up versus other languages here?
[782.84 → 783.32] Yeah.
[784.30 → 785.22] Well, okay.
[785.38 → 790.60] So, Johnny, next time, don't ruin the episode by saying, give me some evidence.
[791.08 → 792.88] Do some science, please.
[793.94 → 796.34] It makes it way too much more work.
[796.34 → 797.28] Just tell them to drink more milk.
[798.26 → 798.70] Yeah.
[798.70 → 801.96] But, but no, obviously the very, very good points there.
[802.28 → 808.02] What I was thinking then is, so are there examples within the language or within the standard library
[808.02 → 814.60] of things that we feel like if we were to remove them, we would be better off, you know?
[814.66 → 819.60] And so some of the things we've talked about, like of having just one way to do something
[819.60 → 826.66] or optimizing for, you know, being able to express ideas or, you know, whether that does
[826.66 → 829.14] impact readability positively or negatively.
[829.88 → 832.34] Are there any things, maybe we could get into that.
[832.40 → 838.96] And I also think if any of us disagree on this, we could, like, you could just press a buzzer,
[839.10 → 842.00] make a buzzer sound with your mouth and the editor will change it later.
[842.00 → 844.20] So it'll be a proper sound, right?
[844.20 → 846.30] I promise.
[847.26 → 852.44] And then you can pick up the gauntlet that was thrown down if you have a different opinion,
[852.44 → 855.20] because there may be some things here that we don't agree on.
[855.22 → 859.68] And I think, you know, there's a lot of personal taste in this, but who wants to go first with
[859.68 → 863.30] an example of something that you would happily take out?
[863.46 → 865.28] Daniel, what would you take out of Go?
[865.28 → 867.58] So I'm going to start with the language feature.
[868.00 → 870.50] I think.import should be removed entirely.
[871.24 → 875.36] And.import is, you know, an import statement that begins with a dot saying that everything,
[876.26 → 880.30] all the exported names in that package are immediately in this package scope.
[880.46 → 882.28] I don't have to do like foo dot something.
[882.90 → 883.10] Yeah.
[883.52 → 886.96] All the DSL loving people are looking at you sideways.
[886.96 → 894.72] I feel like the DSL use case can be valid, but it's so extremely rare that I don't think
[894.72 → 897.50] Go needs to have a feature just for that, if that makes sense.
[897.60 → 900.96] Like pretty much every single time I've seen a.import, I've been like,
[901.22 → 906.44] ah, do you really have to, like, for example, in tests, it just makes tests so much less readable
[906.44 → 909.96] because you see like a function call, and you're like, wait, where's this function?
[910.12 → 911.62] Oh, wait, there's a.import somewhere.
[911.62 → 912.26] Hmm.
[912.66 → 917.52] It's interesting to me that this one came up only because I didn't think about this at all
[917.52 → 921.36] because I don't think I've seen a.import and code in like months.
[922.02 → 923.70] So I didn't even think about it.
[924.04 → 927.62] So it's one of those things where I can't disagree with you that like,
[927.68 → 929.92] I haven't seen a good, perfect use case for it,
[930.08 → 933.74] but I guess it just wasn't high on my priority list because I'm like,
[933.84 → 935.80] it doesn't seem like something that's being abused.
[936.04 → 937.64] So, eh, whatever.
[938.10 → 939.18] That's brutal, mate.
[939.18 → 942.02] I'm like, he's asking him to come on and tell us what he would remove.
[942.10 → 945.14] And you're like, no, that is not a priority for me.
[945.52 → 947.26] I'm just saying it wouldn't be one of my priorities.
[947.40 → 948.50] It's fine if it's one of his.
[948.68 → 949.96] Because you don't see it anyway.
[950.18 → 951.96] Like if he removed it, I wouldn't know the difference.
[952.22 → 955.66] So I guess that's an argument in his favour is that I would never know.
[956.16 → 957.02] Well, hang on, hang on.
[957.08 → 958.14] We've made a grave error.
[958.40 → 961.38] We're assuming that everybody listening to the show knows exactly what we're talking about.
[961.52 → 961.72] All right.
[961.72 → 964.16] So let's take a quick step back here.
[964.62 → 966.38] So the.import, right?
[966.38 → 967.86] Actually, Dan, you brought it up.
[967.90 → 971.34] Why don't you explain what the.import does and what does it enable?
[972.34 → 972.54] Sure.
[972.82 → 976.98] So if you import a package named foo to use anything from that package,
[977.20 → 981.84] you would then do foo. Bar, for example, for an exported function called bar.
[982.28 → 984.86] So if you import that package foo with a dot at the beginning,
[985.06 → 988.42] so dot and then the package path in quotes in your import statement,
[988.66 → 992.56] then you can use bar directly without adding foo. As a prefix.
[992.56 → 999.92] So it essentially allows you to use the names directly as if they were defined in this very package that you're working on.
[1000.30 → 1008.48] But of course, you lose something in the readability there because you don't at a glance know whether it probably would look like a local method
[1008.48 → 1010.58] or something that's in the current package space.
[1011.32 → 1015.82] And so, yeah, having package names on everything, you know, all the types,
[1015.82 → 1019.46] that's a very nice readability gain.
[1020.36 → 1022.52] So, yeah, I'm with you for that one.
[1022.84 → 1023.88] What are the pros?
[1024.06 → 1027.62] Why is it just so that you can people can save key presses?
[1028.06 → 1032.22] I think there's well, as a pro, I don't know because I'm arguing that it should be removed.
[1034.16 → 1036.04] That's just not a priority for us, though.
[1037.78 → 1041.40] I'm going to bring up another con and I know that's going to be pretty niche, but it's tools,
[1041.40 → 1043.66] tools that analyze code and so on.
[1043.72 → 1047.74] Because right now, if you see a name, you can figure out what it is by just, you know,
[1047.76 → 1051.42] looking at your scope and the parent scope and so on and just work your way up.
[1051.94 → 1056.64] But if there's a.import, that kind of goes out the window because you have to look at all the.imported packages
[1056.64 → 1057.96] and look at their scopes as well.
[1058.44 → 1059.52] And that's a linear search.
[1059.60 → 1062.40] It's not like just going up the parent in any way.
[1063.32 → 1065.02] Yeah, I'm so convinced.
[1065.08 → 1066.84] Does anyone like.import on here?
[1066.84 → 1076.44] I like them for the very specific use case that they enable, despite the fact that I actually do not make use of the patterns that they enable.
[1076.78 → 1078.40] So I mentioned DSLs before.
[1078.66 → 1085.58] Like if you want a great example of a DSL that sort of leverages the.import capability, look at go.design.
[1085.90 → 1088.92] It's a Go library for writing APIs and things like that.
[1088.92 → 1096.12] And it's a beautiful DSL that basically, you know, that allows you sort of be that whole express in this thing we were talking about before,
[1096.56 → 1100.48] sort of, you know, almost like you're writing pros, right, to basically to build your APIs.
[1100.78 → 1103.08] And it generates code for you and all that stuff.
[1103.46 → 1106.00] So it's a very good implementation, right?
[1106.22 → 1109.42] It's something that leverages that.import capability quite well.
[1109.64 → 1113.06] It just so happens that I don't use DSLs to write my APIs, right?
[1113.10 → 1115.82] So that's, I'm not knocking it for that, right?
[1115.82 → 1117.82] So it exists.
[1118.02 → 1122.04] It's a feature of the language, like other things I'm sure we're going to come up with here.
[1122.32 → 1125.02] It's part of the language and enables certain use cases.
[1125.14 → 1126.74] It's just not a very common one.
[1127.04 → 1131.92] And if I see it, and personally, if I see a.import, not in this particular Goa use case,
[1131.96 → 1135.60] but if I see a.import in production code during a pull request,
[1136.16 → 1140.74] that developer and I are going to sit down and talk about, you know, some stuff, like some life choices, right?
[1140.74 → 1146.16] Because it's not something that, you know, you typically will see in sort of the everyday Goa code.
[1146.22 → 1148.14] And you must have a very good reason why, right?
[1148.32 → 1152.62] Precisely because it is so unexpected, not because it's a bad thing, right?
[1152.62 → 1156.44] It's just not something you're going to see very often within a production code base.
[1156.44 → 1162.76] I think Ginkgo is another example of something that most developers will probably relate to.
[1163.04 → 1168.60] Like if you've ever come from any BDD testing framework, so behaviour-driven development type testing stuff,
[1169.26 → 1170.70] I think Spec is one of them.
[1170.96 → 1174.14] If you're from like the Rails community, Ginkgo is very similar.
[1174.46 → 1180.48] And to make it sort of read like an Spec test, they commonly use.imports, like in the test file.
[1180.48 → 1186.24] So that in your test code, you can just like say it and then pass a string into that method and then a function
[1186.24 → 1190.76] and then just describe things without using the package space all the time.
[1191.10 → 1197.64] Yeah, so you can say like it should be a book or something and go test this code, and it reads kind of like a story then.
[1198.48 → 1202.58] Well, I also think underscore, I think underscore imports.
[1202.82 → 1204.76] Oh, well, on.imports, one question.
[1205.10 → 1207.18] Whose decision is it that it's a.import?
[1207.32 → 1208.78] It's the person importing it, right?
[1208.78 → 1209.26] Yeah.
[1209.94 → 1215.24] So even if it's a package that has a DSL in it, you still can use it in the other way.
[1215.36 → 1217.62] You just have to keep repeating the package name.
[1218.80 → 1219.20] Yeah.
[1219.40 → 1221.64] You could also rename it to something short like two letters.
[1221.90 → 1224.52] I personally think that's fine for tests, for example.
[1224.98 → 1229.42] And if you really truly want a DSL, I honestly think you need something that's higher level than Go,
[1229.62 → 1231.60] like something that generates Go code, for example.
[1232.50 → 1237.92] Yeah, and then I was going to say the underscore imports is another one that I feel like could go on this list
[1237.92 → 1241.98] because this is the one where you basically import the package,
[1242.12 → 1246.78] but you don't bring it into the package space so that you can use it.
[1246.88 → 1249.86] You can't refer to the package name and access it or anything.
[1250.08 → 1253.78] It's done only, I think, to access the side effect of unit,
[1254.60 → 1258.92] which on Twitter was a very popular option of something to remove
[1258.92 → 1261.78] and definitely gets another one of my votes in it,
[1261.78 → 1263.40] which we're going to talk about in a minute.
[1263.60 → 1266.96] But so yeah, these underscore imports, dead weird.
[1267.30 → 1270.40] And there are a few places in the standard library that does this.
[1270.46 → 1274.04] Like if you're doing image processing, you import the image package
[1274.04 → 1278.56] and then to support JPEG and PNG and GIFs, you import different packages,
[1278.56 → 1280.44] but you don't do anything.
[1280.78 → 1282.12] You don't use those packages.
[1282.12 → 1285.56] They just register themselves in their own little unit.
[1286.02 → 1287.72] So that's why we don't like it.
[1287.78 → 1291.16] It's because it's sort of magical side effect that you're just not expecting.
[1291.78 → 1292.56] So how would you implement?
[1292.90 → 1294.58] Another reason I don't like that pattern
[1294.58 → 1298.54] is just because I feel like it's easy to not know
[1298.54 → 1301.26] if something's been imported or where it needs to be imported.
[1301.44 → 1304.24] Like take the SQL package or the image packages, for example.
[1304.46 → 1306.70] People are like, well, do I import this in my main package?
[1306.76 → 1309.80] Do I import this like in the actual package that uses it?
[1309.86 → 1312.06] What happens if somebody is importing another one in their code?
[1312.34 → 1313.74] Is that going to cause conflicts?
[1314.12 → 1317.24] Like there's all this weird, you know, confusion in your head
[1317.24 → 1318.34] as to like what's going on.
[1318.34 → 1322.88] Whereas like if you actually were to say like a PNG.driver or something,
[1322.96 → 1325.12] you know, along those lines and call that in your code,
[1325.18 → 1327.08] it's very clear where it needs to be all of a sudden.
[1327.86 → 1327.94] Yeah.
[1328.00 → 1330.18] So Daniel, you were asking how would you implement it otherwise?
[1330.18 → 1334.78] And I think you would just import the package and then call a method.
[1335.36 → 1339.52] You know, in fact, if you get rid of all the global state altogether,
[1339.52 → 1345.58] then you'd have something to register the PNG or register the different types with.
[1345.58 → 1350.16] You don't have that because you're sort of registering them in a global way with that in it.
[1350.54 → 1351.48] So that's the other thing.
[1351.56 → 1355.04] It's that whole in it global state underscore imports world.
[1355.20 → 1360.00] I think we're better off clearing, steering clear of that.
[1360.74 → 1364.06] Even like if you look at something like the SQL package,
[1364.20 → 1367.62] in my opinion, it would be easier to call like SQL.open
[1367.62 → 1369.60] and just pass in the drivers the first argument
[1369.60 → 1372.18] than to pass in a string naming the driver.
[1372.18 → 1376.40] Like it's not really any clear seeing the name of it versus just the actual imported driver.
[1376.74 → 1378.98] Does anyone like underscore imports?
[1379.86 → 1380.18] Nope.
[1380.84 → 1381.28] Okay.
[1383.90 → 1384.30] Yeah.
[1384.38 → 1388.66] And by proxy, since we touched on it, I don't tend to,
[1389.42 → 1392.28] I'm not an unit basher, but I don't tend to like in it, right?
[1392.32 → 1395.32] Because, you know, typically where it is in it, there's a global.
[1395.58 → 1399.24] And because I don't like global, and I'm not liking in it as a result.
[1399.24 → 1399.68] Yeah.
[1400.06 → 1403.70] If you're not against them, then you're for them, Johnny.
[1405.68 → 1406.04] Okay.
[1406.10 → 1406.84] That's just the way it is.
[1406.86 → 1407.32] It's like that.
[1407.40 → 1407.56] Okay.
[1408.00 → 1408.66] I'm sorry.
[1408.78 → 1408.98] Yeah.
[1409.18 → 1410.84] Because we've got to sort these in it's out.
[1411.72 → 1413.50] For anyone that doesn't know what they are,
[1413.94 → 1415.28] they're little special functions.
[1415.60 → 1419.24] And you can have multiple of them in the same package in different files.
[1419.38 → 1422.42] In fact, I think even in the same file, you can have multiple in it.
[1422.82 → 1425.28] So already it doesn't feel right, does it?
[1425.34 → 1426.78] Something feels a bit wrong with it.
[1426.78 → 1435.10] And then that code is run when the package is first imported or immediately when the main program is run.
[1435.84 → 1440.78] So it's useful for, and I think the original thinking was around more complex initializations.
[1442.12 → 1449.22] You can just use the var keyword in package space and create a variable and assign it to a simple value,
[1449.32 → 1452.82] like a number or a string or something, or even structs and stuff,
[1453.02 → 1454.76] even slightly more complicated structures.
[1454.76 → 1461.46] But if you need to do anything slightly more computational to prepare, you know,
[1461.62 → 1465.94] or maybe decompress some compressed data or something in order to prepare it,
[1466.14 → 1468.28] then you'd have to do some work first.
[1468.46 → 1471.54] And so the units were kind of, weren't they?
[1471.58 → 1477.02] They were there for initialization time things where you couldn't use vars.
[1477.02 → 1480.02] I think they end up just being a bit too magic.
[1480.56 → 1488.56] And again, it sort of relies on global state, package space state, which is, I think, something worth avoiding.
[1488.90 → 1490.30] Can I make an argument for them?
[1490.80 → 1492.42] Yes, but you have to do your buzzer sound.
[1492.74 → 1493.86] And then when in post...
[1493.86 → 1494.32] Put it in there.
[1494.68 → 1495.24] No, come on, mate.
[1495.30 → 1495.68] Do it properly.
[1495.72 → 1496.90] I don't have a good buzzer.
[1497.36 → 1498.10] Is that better?
[1498.54 → 1498.88] Nope.
[1498.88 → 1499.68] All right.
[1499.96 → 1506.64] So this isn't really a serious argument for, but if you took the reflection package and then in the unit,
[1506.80 → 1510.04] put a time. Sleep for like one minute, punishing anybody who used it,
[1510.30 → 1513.44] then you'd have a good reason for it.
[1514.00 → 1514.24] Right.
[1515.42 → 1515.82] Yeah.
[1515.86 → 1516.62] What would that do?
[1516.68 → 1518.74] Stop the process from starting up?
[1518.92 → 1519.90] For like a minute, I think.
[1519.90 → 1521.24] What happens if you sleep in an unit?
[1521.68 → 1524.68] Because all the units have to complete then before...
[1524.68 → 1525.50] I believe so.
[1525.80 → 1527.48] I've never tried it, but I assume so.
[1527.88 → 1531.02] In which case, people get a real penalty for using reflect.
[1531.86 → 1533.56] You get a penalty for using it anyway.
[1533.86 → 1534.84] Well, they get a bigger one.
[1535.00 → 1535.78] That's not safe.
[1536.58 → 1537.06] That's harsh.
[1537.54 → 1538.10] That's harsh.
[1538.64 → 1540.98] There are some legitimate uses for reflect, you know.
[1541.68 → 1542.56] I know there are.
[1543.84 → 1545.84] But they still got to earn it.
[1546.96 → 1547.64] By waiting.
[1549.40 → 1550.96] Yeah, we've got to earn it.
[1552.00 → 1552.42] Oh, yeah.
[1552.52 → 1553.92] I like John when he's brutal.
[1554.28 → 1554.78] I know, right?
[1554.78 → 1555.98] You're absolutely brutal today.
[1569.98 → 1574.28] How much time does your team spend building and maintaining internal tooling?
[1574.56 → 1576.54] I'm talking about those behind-the-scenes apps.
[1576.54 → 1578.58] The ones no one else sees.
[1578.58 → 1581.34] The S3 uploader you built last year for the marketing team.
[1581.64 → 1585.06] That quick Firebase admin panel that lets you monitor key KPIs.
[1585.38 → 1590.34] Maybe even the tool your data science team hacked together so they can provide custom ad spend analytics.
[1590.92 → 1592.86] Now, these are tools you need so you build them.
[1593.12 → 1594.00] And that makes sense.
[1594.54 → 1601.06] But the question is, could you have built them in less time, with less effort, and less overhead and maintenance required?
[1601.48 → 1603.56] And the answer to that question is, yes.
[1603.56 → 1603.68] Yes.
[1604.06 → 1605.32] That's where Retool comes in.
[1605.68 → 1609.16] Rohan Copra, engineering director at DoorDash, has this to say about Retool.
[1609.54 → 1609.78] Quote,
[1609.78 → 1618.00] The tools we've been able to quickly build with Retool have allowed us to empower and scale our local operators, all while reducing the dependency on engineering.
[1618.44 → 1618.82] End quote.
[1619.28 → 1625.54] Now, the internal tooling process at DoorDash was bogged down with manual data entry, missed handoffs, and long turnaround times.
[1625.54 → 1635.06] And after integrating Retool, DoorDash was able to cut the engineering time required to build tools by a factor of 10x and eliminate the error-prone manual processes that plague their workflows.
[1635.48 → 1639.58] They were able to empower backend engineers who wouldn't otherwise be able to build frontends from scratch.
[1639.98 → 1644.96] And these engineers were able to build fully functional apps in Retool in hours, not days or weeks.
[1645.38 → 1648.54] Your next step is to try it free at retool.com slash changelog.
[1649.28 → 1651.72] Again, retool.com slash changelog.
[1655.54 → 1679.90] Okay, so what about some others?
[1680.12 → 1682.32] Anything else you feel like you would remove?
[1682.32 → 1691.68] I can give one that's a little maybe more controversial because I feel like a lot of the ones we've had are we've all pretty much agreed with.
[1692.64 → 1695.74] So one of the ones that I would get rid of is one-line if statements.
[1696.06 → 1703.38] So when you have something like if x comma error colon equals some function, then you have a semicolon, then you'd like to check the error.
[1703.38 → 1711.82] So my reasoning for this is that I've found over time that there are a few good cases for one-line if statements.
[1712.00 → 1717.64] Most notably, if you're just trying to see if something's in like a map or something like that, it can be useful.
[1717.94 → 1727.24] But why I generally dislike them is that most code that I find more readable sticks to the left, like all the happy path is left aligned.
[1727.24 → 1731.78] And when you're using one-line if statements, it pretty much forces you to break that.
[1732.56 → 1734.22] Yeah, unless you're doing it for error.
[1734.56 → 1739.50] If the error is the type returned, and you're going to then only handle it in that little block.
[1739.88 → 1748.52] Yeah, but I guess what I mean is if there's a second variable ever to access that second variable that's not the error, you either have to put an else statement or you have to like to make your happy path indent.
[1748.52 → 1749.24] Right.
[1749.40 → 1751.38] And in those cases, I'm just not a fan of it.
[1751.58 → 1756.86] And even like the error case you're talking about, you end up shadowing at that point, if I recall correctly.
[1757.32 → 1759.70] So that can potentially be another issue.
[1760.12 → 1764.08] So I just, it's not that there aren't a couple valid use cases for one-line if statements.
[1764.24 → 1768.92] It's just that generally speaking, I feel like people would write better code if it wasn't available to them.
[1770.00 → 1770.40] Okay.
[1770.64 → 1771.38] I'm going to disagree.
[1771.82 → 1772.06] Right.
[1772.46 → 1773.48] Do the buzzer then.
[1773.58 → 1773.86] Yeah.
[1774.54 → 1775.28] Gauntlets throne.
[1775.84 → 1776.92] Oh, nice.
[1776.92 → 1777.54] That's a good buzzer.
[1777.54 → 1781.12] Daniel, that's the sample we're going to use for the rest of our buzzers.
[1781.54 → 1783.24] That's how good that was.
[1784.52 → 1791.20] So I'm going to say that you should prefer not to quote unquote pollute the scope of your parent.
[1791.20 → 1794.22] If you just want to do something that's like just for a few lines.
[1795.12 → 1806.94] And so, for example, if you do, you know, if instead of doing if x comma error colon equals something, for example, that error variable is only scoped to the if or the else.
[1806.94 → 1811.82] So it's not leaking to the if statement has finished.
[1811.82 → 1817.26] So I feel like if you put it in the parent scope, there's more chance that you might make a mistake.
[1817.66 → 1817.78] Yeah.
[1817.78 → 1823.96] But as John said, if there is another value that you want to get out, that is also only scoped to that block.
[1824.16 → 1824.34] Right.
[1824.44 → 1830.04] So then you end up copying it out or something else, which is fine.
[1830.22 → 1830.90] But yeah.
[1830.90 → 1837.88] The alternative then is just to flatten the if or to pull the expression out and have that happen first.
[1837.96 → 1840.22] And then you test with the if after.
[1840.96 → 1841.26] So you do.
[1841.40 → 1841.66] Yeah.
[1841.74 → 1843.48] It's a line you save with that little format.
[1844.46 → 1845.32] Johnny Portico.
[1845.62 → 1847.88] What do you think of those one line if statements?
[1848.50 → 1850.64] They don't bother me as much as they bother John.
[1851.56 → 1851.70] Yeah.
[1851.74 → 1853.32] They don't actually bother me that much.
[1853.32 → 1860.52] It's just something I've noticed where maybe it's just people who are new to the language are looking for a quicker way to write something.
[1860.88 → 1864.10] And I feel like they get overused in some ways.
[1864.30 → 1872.16] And then eventually they realize, oh, this code would be easier if I'd pull that out, you know, pull the actual function call to a line and then check the error statement afterwards.
[1872.16 → 1881.06] And after seeing enough code and like refactoring enough code that had it, I just feel like my life would have been easier if I never used them in the first place.
[1881.66 → 1881.76] Right.
[1881.86 → 1882.02] Yeah.
[1882.08 → 1884.86] So you're just treating this episode basically like therapy for you.
[1886.48 → 1886.88] Yeah.
[1886.92 → 1887.48] No, fair enough.
[1887.54 → 1888.48] But actually, that's a good point.
[1888.54 → 1890.88] I mean, that's why we're here to talk about these kinds of experiences.
[1891.10 → 1901.88] One thing this has against it is it fights against, rubs against a little bit that philosophy of having just one way to do something, you know, that you can do the exact same thing.
[1902.16 → 1904.08] In a slightly different way.
[1904.46 → 1912.06] But at the same time, the similar way of doing this would be an explicit block that indents the whole thing, which is kind of ugly and uses two extra lines.
[1912.68 → 1912.80] Right.
[1913.12 → 1914.76] I guess I just wouldn't do either of those.
[1914.88 → 1919.28] I would just use the same error variable throughout my code is what I tend to do.
[1919.94 → 1924.62] If I ever have a case where like that stuff needs to be isolated, I feel like it's better suited to be in another function.
[1925.06 → 1926.74] But that's, I guess, just my opinion.
[1927.56 → 1928.44] Well, there you go.
[1928.66 → 1929.80] It's not a priority for Daniel.
[1929.80 → 1930.26] That one.
[1930.26 → 1933.10] I got one.
[1933.20 → 1933.72] I got another one.
[1934.04 → 1934.14] Yeah.
[1934.18 → 1935.80] Johnny, what would you take out of the language?
[1936.04 → 1939.04] Sounds like Daniel was going to add a little bit of spice to the wound.
[1939.74 → 1939.94] Oh, no.
[1939.96 → 1943.96] So I don't have another one, but Bill has been bringing up one for the past 15 minutes.
[1944.36 → 1945.68] Bill's like, damn it.
[1945.98 → 1946.82] Naked returns.
[1949.46 → 1950.86] So maybe we should talk about that.
[1951.42 → 1951.62] Yeah.
[1952.16 → 1953.02] What did he say?
[1953.64 → 1955.22] So actually, I think I agree.
[1955.22 → 1958.80] So I think in most cases, naked returns don't make sense.
[1959.16 → 1961.38] I think there's only one case where they do make sense.
[1961.56 → 1966.86] And it's if you want to recover a panic and then alter the return values.
[1967.06 → 1968.86] And then the naked return allows you to do that.
[1969.56 → 1971.48] We're going to have to explain what they are.
[1971.48 → 1973.38] I just see the chat message.
[1973.46 → 1977.72] By the way, you can join in the Go Time chat on the Slack channel, GoTimeFM.
[1978.04 → 1979.68] I just see Bill say naked returns.
[1979.68 → 1981.54] I thought he was asking for nudes.
[1981.78 → 1983.36] He just keeps saying naked returns.
[1983.76 → 1987.22] It's like a really like a Victorian way of that.
[1987.22 → 1987.92] It's a code of conduct.
[1988.08 → 1988.76] It really went out the door.
[1989.60 → 1989.82] Yeah.
[1990.44 → 1991.42] Naked returns.
[1992.62 → 1993.50] But what are they?
[1993.74 → 1994.12] What are they?
[1995.28 → 1996.48] Can someone explain them?
[1996.68 → 1997.38] Oh, sure.
[1997.38 → 2001.56] When you're declaring a function, at the end, you declare the types that you're returning.
[2002.50 → 2004.80] And when you're declaring those, you can also give them names.
[2004.90 → 2011.68] So each variable can have a name, which can be useful whenever you want to make it more clear what each one stands for, what it is.
[2012.04 → 2012.14] Right.
[2012.48 → 2014.46] A naked return is when you name those.
[2014.76 → 2017.38] And then inside your function, you don't have to declare those variables.
[2017.52 → 2019.88] They're already declared because of the way you define the function.
[2020.28 → 2021.96] And you can just write the word return.
[2022.16 → 2024.68] And those variables will be the ones returned for those values.
[2024.68 → 2033.18] So rather than saying like return nil, errors. New or something, you could just say error equals some value.
[2033.30 → 2034.40] And then at the end, just write return.
[2034.60 → 2035.78] And it would return that error.
[2036.36 → 2036.42] Right.
[2037.60 → 2038.04] Yes.
[2038.16 → 2043.24] So naming returns, naming the return arguments, I just don't do that.
[2043.68 → 2045.56] I've seen some code that does it.
[2045.68 → 2046.78] And I can see why.
[2046.86 → 2052.96] And in some cases, they've even saved an allocation by doing it because they need to type anyway to pass into something else.
[2052.96 → 2054.32] So it gets clever.
[2054.56 → 2056.68] But yeah, I like to just be explicit.
[2057.08 → 2063.10] If you've got a couple of strings you're going to return, and you want to be clear about what it is, I'd probably pop that in a struct.
[2063.38 → 2070.92] I think we might be getting two things confused because there are naked returns as in return with nothing else, but you're actually returning something.
[2071.82 → 2075.38] And then there's naming the result parameters in your function declaration.
[2075.38 → 2077.48] I think those two are different things.
[2078.06 → 2080.34] But naming is required for naked returns, I think is how.
[2080.80 → 2081.16] Right.
[2081.60 → 2084.76] Yeah, but you could name your results without using naked returns.
[2084.92 → 2085.84] That's what I'm trying to say.
[2086.12 → 2086.34] Yeah.
[2086.76 → 2087.52] Right, right, right.
[2087.52 → 2093.04] Like I use named return values all the time just to make it clear what something is.
[2093.16 → 2102.12] But then if you read my code, you would probably not really even tell that I'm using the named returns because I don't tend to use those variables the way that that would be.
[2102.12 → 2111.74] Honestly, I would almost prefer it didn't initialize variables for me some days just because in my code I'll go to initialize it and not realize it's like, oh, it's already initialized because it's a named return.
[2112.12 → 2119.20] But yeah, I still, while I do see uses for the named return variables, I really don't like the empty return.
[2120.22 → 2127.24] Does anyone want to make a case for keeping naked returns or named arguments, return arguments?
[2127.24 → 2139.68] Is it possible to do, like when you're recovering from a panic, I know you use name returns, but once you're inside the deferred block, do you have to use a naked return there?
[2139.76 → 2142.88] Or can you, like, I don't actually know what that looks like.
[2143.00 → 2149.28] I know you can say like return, you know, nil comma error, and that should work, but I think you still have to assign the error.
[2149.40 → 2150.18] I'm not positive though.
[2150.76 → 2152.62] Well, the deferred function returns nothing.
[2152.62 → 2158.62] So the whole reason you need the named return parameters is so that you can assign back to them in the parent, right?
[2158.76 → 2160.50] But you don't ever have to have a naked return in it, do you?
[2161.18 → 2165.54] No, when I said that earlier, I was getting confused between the two features, I think.
[2165.84 → 2172.26] Okay, like I was going to say that that's the hard part is I think the naked returns probably show up because the name variables are already there.
[2172.78 → 2176.92] But I do kind of agree that getting rid of the naked return would make code clearer.
[2176.92 → 2177.40] Yeah.
[2177.40 → 2177.72] Yeah.
[2177.92 → 2189.80] I think one feature that people would want if naked return was to go away was to be able to, for example, if you want to return a zero value of a struct, you have to like to name the struct in a composite literal, right?
[2189.90 → 2196.24] You have to do like some very long type name, open curly brace, close curly brace, because that's a zero value.
[2196.24 → 2201.92] It would be nice if instead you could use something like underscore to say the zero value of whatever this is.
[2201.98 → 2207.10] I don't care because the naked return does give you that brevity that you would lose if you didn't have it.
[2207.80 → 2214.04] So wouldn't it be possible to write a lint tool that just finds all naked returns and puts the variables in there?
[2214.92 → 2217.18] Because you have to have named like return variables.
[2217.56 → 2217.96] Sure.
[2218.48 → 2220.16] So I feel like that should be Bill's next project.
[2220.38 → 2221.78] So who wants to die in that hill?
[2222.86 → 2224.16] When would you use that?
[2224.16 → 2226.30] If you want them, type them in.
[2226.56 → 2231.68] Well, I mean, like you could just set it up in your tool chain so that like if you have the empty return, it just automatically replaces them.
[2232.08 → 2232.48] Right.
[2232.66 → 2235.44] And then if Bill gets everybody to use it, he'll never see them again.
[2235.90 → 2240.96] Why don't you just have Bill in the PR, everyone's PR process, and then Bill can just do it himself?
[2241.90 → 2243.08] Bill's already pretty busy.
[2243.22 → 2244.78] I'm not so sure if he would manage that.
[2245.68 → 2247.34] Somebody's going to write a lint or just call Bill.
[2251.42 → 2252.42] Fix your returns.
[2252.42 → 2255.30] Maybe it gives you a pin if everything is green.
[2255.48 → 2255.72] A pin?
[2256.22 → 2257.40] Oh yeah, like a badge.
[2258.04 → 2258.40] Yeah.
[2258.68 → 2259.60] For your hat or something.
[2261.16 → 2264.76] So I think Johnny was going to say another feature that he would remove earlier.
[2265.00 → 2266.20] Johnny, do you have one?
[2266.76 → 2270.32] Something you would remove from the language, mate, or from the standard library?
[2271.00 → 2276.02] I have one, but my stance against it has softened.
[2276.20 → 2276.86] Since when?
[2276.86 → 2281.44] I was looking for a reason to use it, to like it, and I was like squinting.
[2281.70 → 2282.20] You found one.
[2282.78 → 2289.94] Yeah, I probably still wouldn't use it, but I understand for those that do, like, you know, I'm trying to understand where they're coming from.
[2290.58 → 2291.86] Labels in Go.
[2291.86 → 2296.22] And the associated use of the go-to, all right?
[2296.48 → 2296.58] Yeah.
[2296.88 → 2301.36] Very rarely do I find myself wanting to do that.
[2301.44 → 2307.20] Like, if I even sense the need for something like that, I just rewrite the code to not have them.
[2307.20 → 2307.52] Yeah.
[2308.32 → 2311.74] So for anyone not familiar, Go does have go-to.
[2312.68 → 2316.12] If you want to listen back to Johnny's pun earlier, it was actually a double pun.
[2316.24 → 2319.00] Because he had the word go in it and go-to.
[2319.68 → 2324.02] Yeah, they were responsible for spaghetti code, essentially.
[2324.36 → 2326.80] Because that's how you used to write code in basic.
[2327.04 → 2333.28] You'd have line IDs, every ID, like 10, 20, 30, and then the code was on those lines.
[2333.28 → 2338.52] They went up in tens, by the way, so that you could insert other instructions between.
[2338.78 → 2339.02] Later on.
[2339.34 → 2339.44] Yeah.
[2339.52 → 2342.50] Yeah, because you've already put your number in, so it's too late.
[2343.80 → 2349.92] I don't know when they came up with dynamic line numbers, but that changed the world, let me tell you.
[2350.52 → 2354.40] And then they would use go-to to jump around the flow.
[2354.62 → 2359.98] And in some languages, they didn't have functions and subroutines and things, which do that, basically.
[2359.98 → 2360.90] That's what they're doing.
[2361.04 → 2362.96] But they do it for you in a kind of safe way.
[2363.28 → 2365.52] And you declare the ins and outs to that.
[2366.64 → 2369.28] So yeah, go-to was kind of famous for creating.
[2369.42 → 2371.84] It's very difficult to follow code.
[2371.96 → 2379.14] And it's a bit like one of those write-your-own-adventure books, where you'd go to a certain page and jump around.
[2379.30 → 2379.68] You couldn't.
[2380.08 → 2381.66] It's very difficult to reason about that.
[2381.72 → 2382.94] It was hard to hack those games.
[2383.00 → 2384.24] You had to really just play them.
[2385.38 → 2388.22] There's another use case for labels, though, isn't there?
[2388.22 → 2391.60] Which is when you use break out of loops.
[2391.60 → 2404.94] If you have a few nested loops, even just two, in some deep situation inside the inner loop, you may want to exit either just this one, which you can do easily enough with break.
[2404.94 → 2407.36] But you might want to also exit the outer loop.
[2408.44 → 2412.56] And you could set a flag and then check the flag and things and then break.
[2412.96 → 2418.46] But labels allow you to break a particular loop, which is kind of strange.
[2418.46 → 2424.30] But again, as you were saying, Johnny, I've seen examples where that seems perfectly reasonable.
[2424.70 → 2433.80] And usually when the code is very small and succinct, not in great big long multipage functions.
[2434.70 → 2439.56] So just to make sure I remember correctly, with labels, there's what?
[2439.64 → 2441.28] Go to, break, and continue?
[2441.72 → 2441.98] Mm-hmm.
[2442.16 → 2442.88] Are there any others?
[2443.60 → 2444.16] I think that's it.
[2444.44 → 2444.90] No, that's it.
[2445.20 → 2447.90] I don't know if like fall through or any of those other keywords had something with them.
[2447.90 → 2449.08] No, that's your switch.
[2449.08 → 2452.98] Also, you mean continue, you can say continue this particular loop.
[2452.98 → 2454.12] Yeah, you can continue to a label.
[2454.26 → 2458.72] So like if you're nested loops, you can say continue, and it'll like jump to the outer loop and continue.
[2459.02 → 2461.56] You're really labelling the four block, aren't you?
[2461.74 → 2461.90] Yeah.
[2461.90 → 2462.96] When you label those things.
[2463.12 → 2464.64] And you're saying continue this one.
[2465.00 → 2465.34] Yes.
[2465.96 → 2468.14] So you're like jumping to the outer one that you want to go to.
[2468.46 → 2468.80] Right.
[2469.80 → 2470.70] It's magic, isn't it?
[2470.70 → 2471.30] It's dark magic.
[2471.40 → 2477.52] I'll say I agree with Johnny that I've seen some people make not awful arguments.
[2477.90 → 2478.46] For them.
[2479.30 → 2481.94] But I've never wanted to use them myself.
[2482.56 → 2495.84] It's always felt like, I don't know, easier, cleaner or something to just, if I have to use like a nested function or something else, like something has always felt better to me than doing that.
[2496.64 → 2498.54] And maybe just a personal preference.
[2499.02 → 2500.26] I can't really say.
[2501.36 → 2503.24] But I mean, they're there.
[2503.32 → 2507.14] So I don't know if like the people who created the language saw a perfect reason that I didn't.
[2507.14 → 2510.96] So it's hard for me to like really say don't use them or get rid of them.
[2510.96 → 2511.24] Yeah.
[2511.92 → 2514.32] I think the listeners should take this show with a pinch of salt.
[2514.42 → 2516.92] We're just discussing the things that we would remove.
[2517.14 → 2518.90] I mean, please feel free to use these.
[2518.98 → 2520.02] They are part of the language.
[2521.02 → 2523.50] But obviously, if you've got any sense, listen to what we're saying.
[2524.18 → 2525.38] We've made all the mistakes.
[2525.38 → 2531.60] I guess a better way to put it would be if I was reviewing code, and it had a label, I'd probably suggest a change.
[2532.36 → 2532.80] Yeah.
[2533.00 → 2533.54] Do you know what?
[2533.60 → 2546.20] I've definitely used it, but only in very specific cases where it's the clearest thing to do, which is literally you're saying in this case, we're just going to stop, break the whole thing.
[2546.52 → 2548.82] But, you know, you're in some other flow.
[2549.28 → 2553.46] But yeah, I mean, you can always re-architect it to avoid these problems.
[2553.46 → 2555.44] I'm actually going to use my buzzer again.
[2555.78 → 2556.20] So, psst.
[2557.12 → 2557.50] Oh, yeah.
[2557.92 → 2558.98] But what I'm going to say is...
[2558.98 → 2561.82] Could you do a few takes of it so we can choose the editor, please?
[2561.82 → 2562.34] No, I'm okay.
[2562.44 → 2562.70] Thanks.
[2564.34 → 2564.90] Fair enough.
[2565.24 → 2567.84] What I'm going to say is I think it's a bit of both.
[2568.02 → 2573.14] I do agree that I don't use labels all that often, maybe like once or twice per package at most.
[2573.48 → 2580.24] But when I do use them, having to split a function into two, for example, if it was a 60 line function with two levels of indentation,
[2580.24 → 2584.14] I think being forced to split it up would not be good.
[2585.02 → 2590.08] And I'm actually going to make a case for go-to's as well, or rather two cases.
[2590.22 → 2592.58] One of them is sort of like the retry idiom.
[2593.00 → 2597.14] So being able to go to retry a function is pretty useful.
[2597.28 → 2598.58] And you can use a for loop for that.
[2599.02 → 2603.52] But the for loop, if you're going from the top, reads like an endless loop.
[2603.92 → 2606.48] And it's only at the end that you go like, oh, wait, do I want to break?
[2606.94 → 2608.92] Which honestly, I don't feel like it's better.
[2609.82 → 2611.74] And the other use case is code generation.
[2612.08 → 2618.88] For example, if you want to generate an automaton or some sort of bot that jumps between states, having go-to's is pretty useful then.
[2619.60 → 2624.48] It's hard because you almost have to see the case to really determine if it's better to use a label or something else.
[2624.48 → 2632.94] Like when you say breaking into a function, part of me wonders if you could just like to write an anonymous function or a closure or something and slap it in there.
[2633.00 → 2634.90] And if that would work or not, I don't know, though.
[2634.96 → 2635.46] It would depend.
[2636.98 → 2644.74] I will say one of my other arguments against labels is that they're so rare that I think somebody jumping into the language is going to be like, wait, what is this?
[2644.74 → 2652.66] And while the other one might not be as clear what it's doing, the fact that it's going to be all stuff they're accustomed to might make it easier to read.
[2653.20 → 2653.56] Yeah.
[2653.68 → 2657.92] You just have to battle it out in the pull request comments for that one, I think.
[2657.92 → 2665.56] You see, that's the thing again, you know, that whole notion of what's easy for me to read is not necessarily what's easy for you to read, right?
[2665.60 → 2671.38] So for somebody seeing a go-to to a label makes perfect readable sense, right?
[2671.64 → 2674.16] It's just like, oh, yeah, I can definitely follow what's going on here.
[2674.22 → 2677.18] You get to this point, you need to break out these loops and, you know, use the go-to.
[2677.28 → 2678.34] Yep, that makes perfect sense.
[2678.34 → 2681.54] And then for someone like me who doesn't use them very often, right?
[2681.84 → 2684.44] And just because I don't use them very often doesn't mean it's bad, right?
[2684.44 → 2686.14] It just means I don't typically use them.
[2686.14 → 2690.22] So when I see that the first time, I'll scratch my head and be like, why are you doing that, right?
[2690.24 → 2695.38] Then I take John's posture and I bring you into a pull request, a battle, and force you to take it out.
[2697.26 → 2708.54] Like one example I can give there is if you had like three nested for loops and the innermost one would continue to like a label that's like below where the first one starts.
[2708.54 → 2709.94] So it's like technically in the second one.
[2710.12 → 2713.36] I think at that point only the second for loop would be the one that gets continued.
[2714.02 → 2715.60] But I honestly don't know.
[2715.60 → 2721.30] So I'd be like, I need to run this code to actually figure out what it's doing at this point, which would kind of frustrate me.
[2721.96 → 2723.42] You mean you don't run the code for every PR?
[2724.10 → 2725.74] I don't like to sit there and run the for loops.
[2726.14 → 2728.88] Although I don't run into like triple nested for loops very often.
[2729.66 → 2731.02] They run them in your head.
[2731.36 → 2732.72] You could just run them in your head, you know.
[2733.72 → 2735.02] I mean, that's what CI is for, right?
[2735.72 → 2735.94] Yeah.
[2736.76 → 2737.78] Actually, I kind of agree.
[2737.94 → 2739.52] I feel like continue and break.
[2739.52 → 2743.22] I would only ever do it just to jump over one parent, not more than one.
[2743.34 → 2745.90] Because the moment you jump over more than one, it gets confusing.
[2745.90 → 2753.34] So maybe you could replace labels for like break, actually not this one, the parent, but only the direct parent.
[2753.84 → 2754.20] Yeah.
[2754.90 → 2755.26] Okay.
[2755.42 → 2755.88] We'll do that.
[2757.50 → 2757.86] Yeah.
[2757.98 → 2758.62] Good one, that.
[2759.02 → 2759.86] And by the way, thank you, Daniel.
[2760.04 → 2762.82] When you were defending go to, you actually made three puns.
[2763.10 → 2764.60] Go in there, go to itself.
[2764.60 → 2765.44] It's Elf.
[2766.10 → 2768.38] And because you have two reasons.
[2769.20 → 2770.44] The two was the third pun.
[2772.04 → 2773.46] Yeah, I've got it in my pun book.
[2774.94 → 2777.26] Let me go to my go-to puns.
[2777.82 → 2778.58] There you go, see.
[2779.44 → 2785.24] I did a talk at Gotham Go called Things in Go I Never Use, which was actually about this very subject.
[2786.10 → 2788.68] Really talking about the same kinds of things, really.
[2788.68 → 2791.60] And another one that I talked about was Elf.
[2791.60 → 2798.46] And it gets quite a funny reaction because it sounds like, of course, you need Elf.
[2798.66 → 2801.92] You know, you're talking about, you know, doing something if this.
[2802.02 → 2804.02] And then if not, you need to do something else.
[2804.72 → 2817.80] But really, it was a point about the kind of line of sight thing, the guard and check, where you check errors early and handle the edge cases in the indentation and leave, as John mentioned earlier, that happy path down the left.
[2818.68 → 2820.34] So, but Elf is an interesting one.
[2820.34 → 2828.86] And if you find yourself with a big else block and big if-else blocks, one trick is you can flip, if you flip the logic in the if.
[2829.04 → 2831.12] So, if you're saying like, if you do something.
[2831.50 → 2840.48] If you flip the if you do something into if not do something and then handle the else case in there, then you can get back out into the main path.
[2840.54 → 2841.70] It's essentially the same thing.
[2841.70 → 2843.86] It's just kind of a writing style.
[2844.34 → 2846.88] Do you use else a lot?
[2847.30 → 2847.68] You three?
[2848.04 → 2852.44] Johnny, how many times have you used else this week in the last seven days?
[2852.68 → 2852.96] Zero.
[2853.34 → 2853.68] Zero.
[2854.12 → 2854.38] Right.
[2854.38 → 2860.44] I can probably, well, I've been using Go for a while.
[2860.52 → 2865.14] I was going to say, I can probably count the number of times I've used it in my entire time of using the Go language.
[2865.26 → 2866.80] But that's probably an overkill.
[2867.42 → 2867.54] Yeah.
[2867.58 → 2869.48] It's just something that I don't tend to.
[2869.68 → 2872.76] Like the moment I have to use an else, I have to think really hard.
[2872.84 → 2875.38] Is there a way I could return early?
[2875.38 → 2881.90] Or, like, you know, like you said, basically reason about what I'm doing differently so that I don't have to use an else.
[2882.00 → 2884.66] Like the moment I see it, like immediately I start scratching my head.
[2884.72 → 2886.42] I'm like, hmm, that doesn't look quite right.
[2886.62 → 2886.74] Right.
[2886.98 → 2888.56] Again, it's a part of the language.
[2888.94 → 2891.42] That doesn't mean you should avoid using it.
[2891.46 → 2893.48] And there are some cases that you really do need to use it.
[2893.58 → 2893.74] Right.
[2894.10 → 2902.08] But it's just like I typically like even before if I know I'm going to have some conditionals in a function or something like that, I'm already thinking ahead of time.
[2902.08 → 2903.44] How am I going to avoid an else here?
[2903.44 → 2905.52] It's second nature at this point.
[2906.14 → 2906.60] That's interesting.
[2906.72 → 2906.86] Yeah.
[2907.06 → 2908.24] For that reason, is it?
[2908.30 → 2910.26] For the readability line of sight thing.
[2910.54 → 2910.76] Mm-hmm.
[2911.14 → 2911.38] Yeah.
[2922.90 → 2923.70] What's up, friends?
[2923.76 → 2926.28] Have you ever seen a problem and thought to yourself, I bet I could do that better?
[2926.58 → 2927.88] Our friends at Equinix agree.
[2928.30 → 2930.72] Equinix is the world's digital infrastructure company.
[2930.72 → 2934.22] And they've been connecting and powering the digital world for over 20 years now.
[2934.46 → 2936.88] They just launched a new product called Equinix Metal.
[2937.16 → 2941.74] It's built from the ground up to empower developers with low latency, high performance infrastructure anywhere.
[2942.14 → 2943.82] We'd love for you to try it out and give them your feedback.
[2944.28 → 2950.10] Visit info.equinixmetal.com slash changelog to get $500 in free credit to play with plus a rad t-shirt.
[2950.58 → 2953.44] Again, info.equinixmetal.com slash changelog.
[2953.50 → 2954.76] Get $500 in free credit.
[2955.18 → 2955.78] Equinix Metal.
[2956.08 → 2956.54] Build freely.
[2956.54 → 2985.78] So this is quite a simple thing for if you're new to writing Go.
[2985.78 → 2989.02] That is a little cognitive check just to do.
[2989.24 → 2993.86] There are definitely cases where the clearest thing is just a kind of five or six line.
[2994.16 → 2996.80] If this, then set something else.
[2997.08 → 2997.92] Set something else.
[2998.04 → 3001.04] You know, sometimes that logically is exactly what you need.
[3001.60 → 3009.46] But yeah, what happens if you don't protect against that, of course, is once you have two or three of these in a function,
[3009.46 → 3011.82] you really are nesting quite deep.
[3012.68 → 3015.76] And, you know, you're wasting a lot of tabs there.
[3016.54 → 3017.26] You know what I mean?
[3017.32 → 3019.78] Like, you don't need that many tabs in your code.
[3020.98 → 3021.76] It's a waste.
[3022.50 → 3022.92] It's a save your tabs.
[3022.92 → 3023.58] That's too many bytes.
[3023.58 → 3025.48] But what if you replace them with spaces?
[3026.98 → 3029.92] Well, they take up more, don't they?
[3030.60 → 3031.44] Tabs versus spaces.
[3031.88 → 3032.08] Fight.
[3033.08 → 3034.84] Well, tabs wins in Go, doesn't it?
[3034.96 → 3036.58] Because Go Fund uses tabs.
[3038.58 → 3039.58] But, yeah.
[3040.24 → 3043.28] You just send all that white space to GitHub.
[3043.44 → 3043.98] It's a waste.
[3044.78 → 3046.38] Do you know how much white space is in GitHub?
[3046.38 → 3049.90] I've never thought to figure that out.
[3049.98 → 3050.92] You should just count it all.
[3051.22 → 3051.76] But there are loads.
[3052.52 → 3053.58] And it's just all empty.
[3053.76 → 3054.34] It's waste.
[3054.68 → 3056.58] You need like a website that just updates every day.
[3057.60 → 3057.78] Yeah.
[3058.42 → 3059.12] They've got them.
[3059.32 → 3060.90] They've got those websites that update every day.
[3061.50 → 3062.30] They're called the news.
[3064.22 → 3065.72] With the count of white space.
[3066.14 → 3066.38] Right.
[3066.46 → 3067.02] With the count of.
[3067.16 → 3067.34] Yeah.
[3067.46 → 3068.22] That's the hard thing.
[3068.76 → 3071.90] Did you know they have this language where they waste a ton of white space?
[3071.96 → 3072.68] I think it's called Python.
[3073.40 → 3075.10] So much wasted white space.
[3076.38 → 3079.10] Oh, boy.
[3080.46 → 3082.40] Well, it's only white space to us.
[3082.50 → 3086.18] Or if you're looking at it on a white page, there's still characters there.
[3086.26 → 3087.04] There's still data.
[3087.36 → 3089.08] It's travesty.
[3089.16 → 3091.68] We need to trim down that white space.
[3092.86 → 3093.52] Never mind.
[3093.66 → 3095.12] I mean, we can do climate change later.
[3095.62 → 3098.04] We need to probably sort this one out first.
[3098.30 → 3100.86] I feel like Bill is outside our window picketing.
[3101.56 → 3102.28] Right now.
[3103.48 → 3105.64] Like, he's kind of mastered that within Slack.
[3105.84 → 3105.92] Right.
[3105.92 → 3108.28] He's shouting in looking for naked returns.
[3110.28 → 3114.88] Well, now he wants us to talk about removing the ability to return an interface.
[3115.62 → 3116.62] Oh, good Lord.
[3117.42 → 3118.60] Except for the empty interface.
[3119.90 → 3120.68] I disagree.
[3121.74 → 3123.74] I mean, I think I see the intention.
[3123.96 → 3127.36] Like, if you have a constructor, it needs to return a specific type, not an interface.
[3127.52 → 3130.50] And in most cases, you don't want to return an unempty interface.
[3130.50 → 3131.96] But in some cases you do.
[3132.04 → 3132.88] And that's fine.
[3133.02 → 3134.66] As long as you know what you're doing, I think.
[3135.14 → 3135.50] Hmm.
[3135.50 → 3141.86] Part of the reason I like returning the interface occasionally is I feel like it's just clear as to what your intent was.
[3141.86 → 3151.00] Like, if I have a function that sets up, I don't know, like a small little server and all I want to return is a handler.
[3151.00 → 3157.60] I don't really, like, I want the ability sometimes to change how I implemented all that and just to return a handler.
[3157.60 → 3163.42] And sometimes, in my opinion, that's easier is just to say, look, all you really care is that I'm giving you an HTTP handler.
[3163.94 → 3167.08] Like, the actual details are, you know, shouldn't matter to you right now.
[3167.84 → 3171.14] But I do think it's few and far between as to when that makes sense.
[3171.54 → 3175.24] It also lets you hide your internals a little bit as well.
[3175.44 → 3180.56] Sometimes you might not want to export those concrete types for whatever reason.
[3180.68 → 3184.38] And again, maybe that's, maybe you just can return those types.
[3184.38 → 3193.34] But yeah, having an interface return, I think also has this, in a way, comes from kind of factory thinking a little bit, potentially.
[3193.76 → 3199.16] Because it's possible that it returns a different type depending on something else.
[3199.50 → 3199.88] You know what I mean?
[3199.98 → 3202.62] So in that case, you would want the interface to be returned.
[3202.76 → 3207.66] Or you'd have to just have a couple of methods and move that logic elsewhere.
[3207.76 → 3211.08] But that logic of which type to use sometimes is part of it.
[3211.50 → 3214.30] I think what's the argument against doing it?
[3214.38 → 3219.70] It's just that it's better to return the concrete type and the caller can still use the interface if they want to.
[3220.16 → 3222.72] I think one is that the caller can decide if they need an interface.
[3223.06 → 3226.98] Another that Bill's mentioning is that in 1.16, there was an optimization.
[3227.90 → 3232.90] I think it was something with escape analysis and basically extra allocations or something.
[3232.94 → 3233.78] I don't remember what it was.
[3233.88 → 3238.00] But basically, it was like not as efficient memory-wise, if I recall correctly.
[3238.00 → 3242.30] And they made a couple optimizations in the compiler specifically for it.
[3242.78 → 3244.46] And it helped speed up some code.
[3245.08 → 3247.62] But I still think, like, it kind of depends on the context.
[3247.78 → 3255.84] If I'm writing all the code, so I control both the function that's returning something and the functions that are using it, I think it's fine.
[3255.84 → 3259.70] Because I can change one and go change the other spots and not really have an issue.
[3260.12 → 3265.56] But, like, if I'm writing a library that I'm publishing on the internet and lots of developers are going to grab and use,
[3266.02 → 3271.38] sometimes returning an interface means that I can make what would otherwise be a breaking change without bumping major versions.
[3271.98 → 3275.28] And to me, that's worth a slight performance loss.
[3275.28 → 3277.22] That's a good one.
[3277.62 → 3279.64] So what about the standard library?
[3279.92 → 3284.16] Is there anything in particular that you would take out of the standard library?
[3284.56 → 3285.46] Daniel's all over that.
[3286.36 → 3291.34] So I've got one that I think might be very controversial or non-controversial whatsoever.
[3291.70 → 3292.96] I don't know which way it's going to go.
[3293.58 → 3295.10] And that is the plugin package.
[3295.84 → 3297.94] Because I think the plugin package is a very good idea.
[3298.50 → 3300.18] But it's sort of half-baked.
[3300.56 → 3301.88] You know, it has no Windows support.
[3302.12 → 3303.52] It's very easy to misuse.
[3303.52 → 3309.18] If somebody else builds a plugin and tries to run it with your binary, it's almost certainly not going to work.
[3309.94 → 3311.48] So I think it's a great idea.
[3311.66 → 3314.40] But it should never have hit the standard library until it was finished.
[3315.00 → 3315.10] Yeah.
[3315.24 → 3322.64] So this is a kind of runtime way of loading other, like, almost dynamically loading other Go code.
[3323.16 → 3327.26] And you do that through this quite strange plugin interface.
[3328.58 → 3331.80] Has anyone ever seen this used or used it?
[3332.00 → 3333.18] I don't think I have.
[3333.18 → 3333.74] I would say I have.
[3334.16 → 3334.40] No.
[3335.20 → 3335.98] I've seen people try.
[3336.36 → 3337.28] That kind of speaks for Linux.
[3337.82 → 3338.10] Yeah.
[3339.72 → 3340.06] Yeah.
[3340.14 → 3341.46] I think that probably speaks for Linux.
[3341.90 → 3342.12] Yeah.
[3342.36 → 3346.50] I think if your target platform is only like Linux or Linux and Mac, I think it's fine.
[3346.50 → 3354.56] But if it has to be portable or easy to use for essentially any Go user or any user in general, I think it's just not an option at all.
[3355.80 → 3356.20] Yeah.
[3356.30 → 3357.60] I think I'm on the same boat here.
[3357.66 → 3360.42] The idea of it was it had a lot of promise.
[3360.90 → 3368.18] The fact that you can't swap plugins at runtime, for example, that seems like a big missed opportunity.
[3368.84 → 3369.06] Yeah.
[3369.06 → 3372.88] I think it's just an unfinished sort of capability.
[3373.72 → 3380.12] But if it's unfinished, right, that also means that it could be finished and made to be more robust.
[3380.12 → 3383.06] Lots of honking.
[3383.06 → 3386.40] It could be made more robust.
[3386.88 → 3390.52] I think the fact that not a lot of people are using it.
[3390.66 → 3397.32] I'm wondering if it's because it's not good enough yet or is it the chicken on the egg problem, right?
[3397.42 → 3399.28] Is it're not using it because it's not good enough?
[3399.48 → 3405.44] Or is that if it was finished, would they start using it and thereby would plugins become popular?
[3405.72 → 3405.86] Right.
[3405.86 → 3406.60] It's kind of hard to tell.
[3407.26 → 3414.42] I think if it was finished, as in proper Windows support and some sort of wrapper to allow for nice error messages,
[3414.70 → 3419.20] if something doesn't align when you load a plugin, I think with those constraints,
[3419.38 → 3424.72] for some use cases where you load something, but you never want to unload it, I think plugin would be fine.
[3425.50 → 3432.00] But the thing is, it hasn't been finished in the I think, for three or four years that it's been in the standard library.
[3432.00 → 3434.64] So I don't have high hopes for it being finished anytime soon.
[3434.64 → 3437.36] And right now you can't really remove it, right?
[3437.42 → 3440.82] Because once it's in Go 1, you can't remove it from there.
[3441.40 → 3443.92] We can in Go 2, whenever that is.
[3444.38 → 3445.88] Pun overload, sorry.
[3446.72 → 3450.90] When you're creating a new library or language in this case,
[3451.80 → 3455.50] I feel like some things are going to sneak in that you wish weren't there.
[3456.00 → 3460.00] And this definitely sounds like one of those where it got in there and now if you asked anyone in the Go team,
[3460.00 → 3462.72] they'd probably be like, yeah, that really shouldn't be there just yet.
[3464.12 → 3464.52] Yeah.
[3465.24 → 3473.14] Sometimes there are specific problems that had to be solved and there are some examples of that in the standard library.
[3473.80 → 3476.46] Well, tell me about, John, the container packages.
[3476.82 → 3477.94] Do you ever use those?
[3478.42 → 3480.82] So there are a couple container packages in the standard library.
[3480.98 → 3484.22] There's list, heap, and ring, I think is the other one.
[3484.22 → 3493.86] I've tried to use them before and every single time I've used them, I've just felt it's easier to just write my own link list or my own heap or whatever.
[3493.86 → 3501.24] I feel like because they're stuck using interfaces and there aren't generics, and they aren't set up to generate code,
[3501.86 → 3505.34] it's almost just more confusing than writing something on your own,
[3505.34 → 3508.14] which was just, I get why they're there.
[3508.34 → 3514.06] You know, it seems like a type you'd need in the standard library of some sort, but it just kind of feels subpar.
[3514.06 → 3519.80] And I feel like if that's the first impression somebody gets of the language, it really makes the language look worse than it is.
[3519.80 → 3526.22] So if I could go back and redo things, I think I would suggest like, let's not put this in the standard library.
[3526.32 → 3534.26] Let's instead like make a tool that generates list, and you give it a type and like make maybe a standard tool for that.
[3534.34 → 3534.82] That'd be cool.
[3535.26 → 3539.04] But don't actually like put that specific package in the standard library.
[3540.08 → 3540.44] Fair enough.
[3540.92 → 3541.22] Yeah.
[3541.80 → 3548.04] Do you think generics will, do you think we'll get a range of packages that are common sort of data structure types?
[3548.04 → 3550.74] When generics, if generics lands in Go?
[3551.20 → 3552.50] I think somebody will write them.
[3552.64 → 3555.82] Whether it's the Go team or not is probably the biggest question.
[3556.24 → 3561.88] Well, I think it should be the Go team because if not, we're going to have lots of like competing.
[3562.56 → 3563.64] Well, maybe that's okay.
[3564.14 → 3564.94] And incompatible.
[3565.46 → 3565.72] Yeah.
[3565.78 → 3571.84] But it'd be nice if there was a at least for the more common ones, that there were proper ways to do it.
[3571.86 → 3573.20] A bit like how we have maps.
[3573.44 → 3573.72] Yeah.
[3575.00 → 3576.10] It probably depends.
[3576.10 → 3579.54] Like the harder part there is like, how do you decide which ones are the more common ones?
[3579.66 → 3581.72] Like which ones deserve to be in the standard library?
[3582.58 → 3587.12] And I mean, you could make the argument that like list heap and ring are all in the standard library now.
[3587.22 → 3591.70] So like those are important enough, but still it's, I don't know.
[3591.70 → 3600.52] Well, you could put them in the X package and just as a hint to everybody that, hey, you know, this is experimental, but this is something that we've, we're, we're thinking about it.
[3600.52 → 3601.38] Have thought about, right?
[3601.80 → 3603.92] No need to reinvent the wheel 200 times.
[3603.92 → 3607.32] You know if you have improvements, you know, suggest them, that kind of thing.
[3607.64 → 3613.88] It'll be good as well as part of the development of the Go generics proposal because, you know, it's a good test.
[3613.98 → 3622.06] I mean, really that's where generics, almost there's no debate that that's a good use case for generics for those kinds of problems.
[3622.06 → 3627.22] But yeah, I think that's a fair, fair candidate, John.
[3627.32 → 3631.74] I hope it's on some people's priority lists to have that taken off, deleted.
[3632.52 → 3633.96] Okay, it's that time.
[3634.04 → 3640.68] We're running a little late, but if you'll bear with us a few more minutes, dear listener, it's time for Unpopular Opinions.
[3644.68 → 3645.92] Unpopular Opinions
[3645.92 → 3646.64] What?
[3646.92 → 3648.62] I actually think you should probably leave.
[3648.62 → 3653.96] Unpopular Opinions
[3653.96 → 3662.62] So, any, I mean, I feel like this has been a kind of episode of Unpopular Opinions,
[3662.84 → 3667.24] but are there any particular unpopular opinions you'd like to get off your chest?
[3667.56 → 3672.22] So, I've got one, and I'm not sure how I feel about it.
[3672.22 → 3676.72] I think Go as a language is making a mistake by investing so much into generics
[3676.72 → 3682.18] because they're putting a bunch of very smart people for years and years into generics,
[3682.26 → 3683.94] how to design them and how to implement them.
[3684.56 → 3689.70] And if instead you invested those resources in improving the compiler's support of interfaces
[3689.70 → 3692.14] with changes like the one we discussed for 1.16.
[3692.14 → 3697.32] I think if you covered the common use cases of interfaces and made them faster,
[3697.56 → 3701.56] I think a lot of use cases for generics would go away.
[3704.02 → 3705.04] That's an interesting one.
[3705.76 → 3707.62] Is that popular or unpopular?
[3708.04 → 3709.00] Johnny, what do you think?
[3709.18 → 3710.36] What's your immediate reaction?
[3710.48 → 3714.96] If you had to give an immediate reaction to that, which you do, what would it be?
[3714.96 → 3718.60] So, well, I don't do immediate reactions.
[3718.82 → 3720.32] I think about things.
[3720.34 → 3721.56] Do it in your style, for sure.
[3722.04 → 3722.74] Yeah, yeah.
[3722.92 → 3724.94] So, yeah, I think about these things, right?
[3725.30 → 3726.16] So, here's the thing.
[3726.26 → 3732.16] Perhaps that is indicative of perhaps the way I approach these things.
[3732.20 → 3735.62] In the beginning, right, when I first was getting comfortable with Go,
[3736.34 → 3740.12] and I was like, oh, the lack of generics, that is a miss.
[3740.12 → 3744.46] That is, oh, like how could they, yeah, that is just a big no-no.
[3744.60 → 3746.02] Why do they not have that in the language, right?
[3746.54 → 3748.48] And then I learned to work around them.
[3748.94 → 3754.18] Some would say code, which might have been sort of confusing to write in generics,
[3754.24 → 3756.68] you know, because you had to do it the quote-unquote long way, right?
[3756.84 → 3760.58] I sort of took pride and pleasure in that, and it's actually basically,
[3760.72 → 3762.24] hey, am I going to be more explicit here?
[3762.88 → 3767.28] Yes, it might not be as elegant as it could have been using generics, but it's okay, right?
[3767.28 → 3768.66] So, over the years, I've gotten used to it,
[3768.66 → 3771.90] and then I got into, you know, the camp of,
[3772.28 → 3774.26] ah, we need no stinking generics, right?
[3774.74 → 3777.74] And then I see the proposal, and it's, you know,
[3777.80 → 3781.44] I've seen some documented use cases where it could be better and things like that.
[3781.48 → 3784.22] And it's one of those places, it's one of those things, again,
[3784.32 → 3788.46] where my experience, my use of the language, right,
[3788.56 → 3790.56] is I'm not the only one using the language.
[3790.62 → 3792.78] So, there are some things that I'm naturally not going to see
[3792.78 → 3795.54] that other people are going to have different experiences
[3795.54 → 3797.76] and different needs and things.
[3797.76 → 3803.00] So, I've sort of broadened my tent for these competing ideas, so to speak.
[3803.34 → 3807.66] So, if we don't get generics for another year or two, I'm fine with that.
[3807.74 → 3810.88] If we get them within the next year or two, yeah, I'll use them.
[3811.08 → 3818.20] I'll probably be very sort of conservative in sort of how often and how much I use them, right?
[3818.20 → 3822.64] But, you know, again, like GOTO and labels and all these things, they have their place.
[3822.90 → 3824.42] And when I see them, I'm like, oh, you know what?
[3825.10 → 3829.68] This would make an excellent use case for, you know, having a generic type here or something like that, right?
[3829.76 → 3834.76] And again, and that's the I think for me personally, that's sort of been my evolution, right,
[3834.78 → 3839.82] as an engineer is basically knowing that, sort of living that, well, it depends, right?
[3839.82 → 3844.98] I used to hate that when people said that, but I've learned over the years that, yes, it does depend, right?
[3845.08 → 3847.50] And your use case is going to drive which way you go.
[3847.96 → 3850.52] So, I have a question related to that, I guess.
[3851.12 → 3855.72] Are you more, is your unpopular opinion that not as much time should have been put into it
[3855.72 → 3858.38] and they should have just picked something and went with it?
[3858.38 → 3863.00] Or is it that generics are coming to Go itself or a combination of both?
[3864.18 → 3867.82] So, I'm not going to say that generics are a bad idea, or they're not needed
[3867.82 → 3873.12] because I think generics as part of types are good in many cases, such as maps or slices, right?
[3873.98 → 3876.88] What I'm trying to say is that it's a trade-off.
[3877.42 → 3880.82] And the compiler right now is very basic in some ways, like inclining.
[3881.50 → 3884.28] And if that effort had been spent in those parts of the compiler,
[3884.28 → 3890.26] a lot of the function kind of generics could probably be mostly solved
[3890.26 → 3893.18] by just a better compiler with just plain interfaces.
[3894.20 → 3894.30] Yeah.
[3894.48 → 3898.00] But if your argument is that they're smart, these really smart people
[3898.00 → 3900.60] and they're spending all their time on generics, they could be doing better things.
[3901.06 → 3902.34] Why stop at compiler things?
[3902.42 → 3903.40] Why not like hoverboards?
[3903.84 → 3908.00] And maybe someone could invent a pill that makes all your hair grow back.
[3908.00 → 3908.84] Or the plug-in package.
[3909.52 → 3910.66] Or fix the plug-in package.
[3911.44 → 3912.78] Yeah, or plug-in hair.
[3912.78 → 3915.66] Yeah, and gnash those two ideas together.
[3916.46 → 3917.86] New startup idea.
[3918.60 → 3919.56] Top of my head.
[3919.96 → 3920.98] That's what it could be called.
[3921.58 → 3924.26] And it just sends you random wigs.
[3926.54 → 3927.92] Sorry, I've just derated it.
[3927.94 → 3929.54] You make a compelling point.
[3930.00 → 3930.40] Very good.
[3931.18 → 3933.34] Any other unpopular opinions today?
[3934.00 → 3935.64] I'm still thinking about Daniel's.
[3935.64 → 3941.80] It's more just, in some ways, I understand what Daniel's saying.
[3942.46 → 3950.90] But I also kind of, I think that as the language grows and matures, that it's probably going to have to slow down in some ways
[3950.90 → 3956.76] and take more time and thought into what it adds to the language and how it changes the language over time.
[3956.76 → 3961.82] I imagine, you know, before 1.0 was released especially, you could get away with a lot.
[3961.82 → 3970.50] But now that 1.0 is out and now that, you know, this is a major change, I'm, in some ways, it's promising to me that they're spending this much time on it
[3970.50 → 3973.08] because it means that they're not just throwing something in there.
[3973.08 → 3980.98] And, like, even when we saw the proposals for the error handling stuff, that they spent a lot of time on that, it seemed like, and that all got thrown out.
[3981.24 → 3990.12] So you could say that was all wasted effort, but at the very least, they're taking community feedback into account and trying to decide, like, is this something we can improve on?
[3990.78 → 3992.06] And I think that's a positive thing.
[3992.76 → 3998.00] So it would be nice to see some compiler, like, you know, performance improvements and stuff like that.
[3998.26 → 4000.80] For me personally, those aren't actually a priority at all.
[4000.80 → 4005.52] I would have more use for generics than, like, compiler optimizations.
[4006.16 → 4017.84] I'd rather they spend the time and the money basically doing an investigation and either going forward something or throwing out whatever it is that they deem not good enough
[4017.84 → 4021.18] rather than sort of dismissing it out of hand, right?
[4021.22 → 4023.56] Because a lot of people have been asking for generics for a long time.
[4023.94 → 4029.90] And the fact that there's somebody footing the bill for all that work, all that research, I welcome that.
[4029.90 → 4041.58] The one thing I'll mention here is that when Robert and Ian came on the show a few episodes ago, I think the episode title is The Latest on Generics.
[4042.10 → 4050.88] One of Ian's sort of mic drop moments basically was that the community keeps asking for all this sort of language features basically to add things, right?
[4050.88 → 4053.18] So we've done a whole show on things we would remove, right?
[4053.22 → 4057.72] But generally speaking, most of the time people are asking for things to be added to the language, right?
[4058.30 → 4067.14] But the advice that he gave, which I thought was, you know, very apt, was that before you ask for these additional things,
[4067.14 → 4072.40] sort of in terms of, you know, features and things that you want the language to support and do and these things like that,
[4073.06 → 4079.08] don't consider only the things you would add for your use cases, but also consider the things that it would make harder,
[4079.28 → 4083.68] the things that it would make sort of a harder, sort of the reason about, you know, for readability.
[4083.86 → 4091.32] Basically asking everybody sort of make a concerted effort to truly weigh the pros and cons of anything you add to the language, right?
[4091.32 → 4097.80] Because, you know, it's like I can give you an example, so many examples we can probably all think of,
[4098.16 → 4105.44] of a new language, a new piece of software, a new framework, something comes in, and we relish the simplicity of that V1, right?
[4105.46 → 4106.86] We're like, oh, thank goodness, right?
[4106.88 → 4110.78] I've been dealing with this thing with all these features, all these bells and all these whistles.
[4111.10 → 4112.18] It gets complicated.
[4112.32 → 4113.84] I don't know the right way to do things.
[4113.84 → 4119.04] And, you know, I spend all my time reading blog posts so I can figure out which knob and button to flip and things.
[4119.04 → 4126.36] And then when something simpler comes along, we immediately gravitate towards that thing because the simplicity of it is the attractiveness, right?
[4126.40 → 4128.70] That's what we like about it, right?
[4129.14 → 4136.98] But over time, if we're not careful, Go could find itself being one of those languages that we just keep throwing everything in there.
[4137.08 → 4139.90] And it becomes more and more complicated over time, right?
[4139.90 → 4146.20] So let's not forget why we all, most of us anyway, love Go, right?
[4146.20 → 4149.74] It is that simplicity, that word we keep throwing around, that simplicity, right?
[4149.74 → 4152.76] The fact that it doesn't have all these extra features, bells and whistles.
[4153.20 → 4154.10] That's why we love Go.
[4154.14 → 4159.18] I know personally for me, that's why I love Go because it doesn't try to beat everything to everybody.
[4160.00 → 4160.34] Well said.
[4160.42 → 4163.10] I don't think we can beat that.
[4163.86 → 4165.10] Great ending there, Johnny.
[4165.22 → 4166.22] Thank you very much.
[4166.22 → 4168.66] And thanks to everyone for listening.
[4169.36 → 4171.70] We were joined today, don't forget, by Daniel Marty.
[4172.24 → 4173.30] Daniel, thanks for coming.
[4173.60 → 4174.14] Happy to be here.
[4174.14 → 4175.36] You're welcome back.
[4175.52 → 4178.06] Johnny, there's a cool episode next week.
[4178.28 → 4181.02] Why don't you tell everyone about that?
[4181.10 → 4181.76] Do you know which one I mean?
[4182.10 → 4183.38] Yeah, I know which one you mean.
[4183.54 → 4187.00] Next week, we'll have Kelsey back on the show, Kelsey Hightower.
[4187.42 → 4194.56] And we're going to be talking about how distributed systems go bad and what you can do about it.
[4194.70 → 4195.76] It's going to be an exciting show.
[4196.14 → 4197.26] So do join us.
[4197.84 → 4198.54] Sounds great.
[4198.96 → 4199.70] We'll be there.
[4200.60 → 4202.90] John Calhoun was also on this episode.
[4204.14 → 4206.26] Okay.
[4206.46 → 4207.28] Well, thanks very much.
[4207.34 → 4207.94] Thanks for listening.
[4208.28 → 4209.14] I'll see you next time.
[4209.14 → 4220.84] If you enjoyed this episode, subscribe now in your favourite podcast app or peruse the entire catalogue at gotime.fm.
[4220.84 → 4226.26] There you'll find lists of recommended and popular episodes, transcripts for each, and a lot more.
[4226.82 → 4230.16] We put our unpopular opinions to the test on Twitter.
[4230.48 → 4232.52] It's like Hot or Not, but for ideas.
[4233.04 → 4237.36] Follow at Go time FM to vote for or against and let your voice be heard.
[4237.36 → 4242.36] Our music is provided by the Beat Freak, Break master Cylinder, and we are brought to you by some awesome sponsors.
[4242.76 → 4246.34] Shout out to Vastly, Linde, and our brand-new partner, Launch Darkly.
[4246.64 → 4247.30] Welcome aboard.
[4248.08 → 4249.10] That's all for now.
[4249.30 → 4252.12] Distributed systems go wrong next week.
[4252.12 → 4252.86] We'll be right back.
[4252.86 → 4256.80] We'll be right back.
[4257.00 → 4258.10] We'll be right back.
[4259.06 → 4259.40] Get ready to talk.
[4259.40 → 4261.16] See you next week.
[4261.16 → 4291.14] Thank you.
[4291.16 → 4321.14] Thank you.
