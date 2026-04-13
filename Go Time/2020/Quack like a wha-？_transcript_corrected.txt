[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.76] Head to linode.com slash Changelog.
[17.38 → 22.28] Do not underestimate the power of the independent open cloud for developers.
[22.50 → 24.58] Yes, I'm talking about Linde.
[24.86 → 29.38] Linde is our cloud of choice, and it's the home of Changelog.com.
[29.38 → 34.32] What we love most about Linde is their independence and their commitment to open cloud.
[34.74 → 39.92] Open cloud means being unencumbered by outside investment and maximizing value for the community,
[40.28 → 41.12] not shareholders.
[41.54 → 43.16] And that's exactly what Linde represents.
[43.54 → 44.56] No vendor lock-in.
[44.92 → 46.32] Open at every layer.
[46.74 → 49.24] If you want to learn more, head to linode.com slash open.
[49.50 → 51.86] Again, linode.com slash open.
[59.38 → 65.96] Let's do it.
[66.60 → 67.58] It's Go Time.
[67.58 → 73.82] Welcome to Go Time, your weekly podcast discussing everything inside Go's expanding reach.
[73.98 → 77.88] We've got clouds, containers, system architecture, CLI's, you name it.
[77.96 → 80.62] And of course, the people and language that make it all go.
[80.82 → 82.36] We record live on Tuesdays.
[82.38 → 83.06] It's a lot of fun.
[83.20 → 87.10] Join us in the Go Time FM channel of Go for Slack at 3 p.m. Eastern.
[87.32 → 90.18] We also take requests at Changelog.com slash request.
[90.32 → 93.68] Select Go Time in the dropdown and let us know what you'd like to hear about on the show.
[93.96 → 95.34] Okay, here's Matt and the team.
[95.62 → 96.20] Go Time, baby.
[96.20 → 102.66] Hello and welcome to Go Time.
[102.76 → 103.48] I'm Matt Ryder.
[103.64 → 106.98] Today, we're talking about abstractions and interfaces.
[107.84 → 112.50] And we're obviously going to deep dive on Go interfaces and look at some patterns and things there.
[113.02 → 115.34] Joining me today, it's Mark Bates.
[115.46 → 116.02] Hello, Mark.
[116.36 → 117.22] Hello, Matthew.
[117.32 → 118.04] How are you doing today?
[118.42 → 119.06] Good, thank you.
[119.08 → 119.52] And yourself?
[119.98 → 120.62] Not bad.
[120.62 → 125.98] It says here in my show notes that I'm supposed to mention Bit Bar and compliment you accordingly.
[126.64 → 128.98] Well, that's very kind of you to say, Mark.
[129.12 → 131.12] So this is my mention of Bit Bar?
[131.24 → 131.84] Yeah, yeah.
[132.00 → 132.94] Thank you very much.
[133.38 → 134.32] Complimenting you accordingly.
[134.64 → 135.74] No, you've surprised me there.
[135.82 → 138.38] Yeah, but I'll talk more about that later because...
[138.38 → 140.32] Oh, is that not the sponsorship portion of the show?
[140.38 → 141.12] Is that not where I...
[141.12 → 141.88] No, that's the...
[141.88 → 142.96] Oh, sorry.
[143.34 → 143.60] Sorry.
[143.60 → 144.28] That's Vastly.
[146.78 → 149.22] We're also joined by Johnny Portico.
[149.42 → 149.88] Hello, Johnny.
[150.52 → 151.16] Hello, Matthew.
[151.30 → 153.14] Wait, your full name, first name is Matthew?
[153.60 → 153.84] Yeah.
[153.92 → 154.44] How many knew that?
[154.86 → 155.10] Yeah.
[155.36 → 155.52] Yeah.
[155.52 → 155.72] Really?
[156.42 → 159.76] Yeah, Matt's a shorter version of it, but it's just one T.
[160.12 → 160.54] Whoa, whoa.
[160.66 → 162.04] Matt is short for Matthew?
[162.56 → 163.00] Yeah.
[163.42 → 164.34] I've just been...
[164.34 → 164.60] Huh.
[164.98 → 165.66] Oh, interesting.
[166.12 → 166.50] Mine.
[166.50 → 167.02] Mine totally...
[167.02 → 168.12] I did not see that coming.
[168.12 → 173.58] And John is short for Jonathan, and speaking of which, Jonathan, it's John Calhoun.
[174.04 → 174.64] Hello, John.
[175.02 → 175.62] Hi, Matt.
[176.12 → 176.60] How's it going?
[177.04 → 177.34] Good.
[178.04 → 178.46] Good.
[178.88 → 183.04] We're going to talk about interfaces and abstractions today, and I thought, since you've
[183.04 → 186.04] done a lot of kinds of training material and stuff, it might be cool if you could kick
[186.04 → 191.36] us off and just start with sort of tell us what is an interface, and what are they for?
[191.68 → 192.00] Yeah.
[192.44 → 196.60] I mean, at its very core, they're just a way of defining behaviour that you want.
[196.60 → 200.14] And so, you know, when we talk about code, a lot of times you look at structs, and you'll
[200.14 → 203.96] see very concrete things that say, like, what a user is or all these different things.
[204.24 → 207.10] But whenever you're actually writing code, a lot of times you don't care specifically
[207.10 → 208.56] about the type that you're getting.
[208.64 → 212.46] You don't care if it's a user or if it's an admin or if it's something else.
[212.94 → 215.72] You just care about some specific behaviour that it might have.
[215.92 → 218.76] And in Go, this is typically represented with methods of some sort.
[219.22 → 219.32] Yeah.
[219.32 → 222.60] So an interface is a type that just lists out methods.
[222.60 → 228.20] And then any other type that happens to have those same methods can be used wherever that
[228.20 → 229.80] interface is requested.
[230.02 → 230.24] Is that?
[231.38 → 231.66] Yep.
[232.30 → 232.58] Yeah.
[232.78 → 237.66] The example I always use when I'm doing training is like an entertainer interface.
[237.86 → 242.04] So if I'm starting a club, some sort of entertainment venue, right?
[242.32 → 247.14] If I use a concrete type, if I say, you know, I want to use this concrete type, the concrete
[247.14 → 247.94] type is beetle.
[247.94 → 250.62] Well, anybody who's a beetle can play at my club.
[250.68 → 253.38] Well, there's only two people in the whole world who can play.
[253.88 → 257.46] Admittedly, if I got one of those two, I could easily pack the house.
[258.32 → 259.98] The other one would be tending bar.
[261.02 → 263.36] But, you know, that's concrete behaviour.
[263.48 → 266.40] I can only fill it two nights of the year, possibly.
[267.04 → 267.26] Right.
[267.38 → 267.58] Right?
[267.62 → 272.08] If I accept an interface, if I say anybody who's an entertainer, anybody who can play
[272.08 → 278.00] something, whether it be a guitar or a flute or can read poetry or an improve troupe, they
[278.00 → 278.68] can all entertain.
[278.92 → 282.40] They all have this play method on them, just like a beetle would.
[282.94 → 285.32] Now I can have Paul McCartney come play.
[285.46 → 287.76] I can have the flutist come play.
[287.82 → 291.82] I can have that dance group come and perform because they all implement that.
[291.82 → 293.16] They're not concrete anymore.
[293.56 → 296.44] To me, that's always a clear analogy, but maybe not.
[296.44 → 301.06] See, I like that because it's a good way of sort of showing that you can also do interfaces
[301.06 → 304.46] that are like a long-running process, like anything that can play and that might block
[304.46 → 305.16] for a half hour.
[305.72 → 307.66] You know, everybody sits down and listens to an entertainer play.
[308.02 → 312.52] Or you can have behaviours like if you're dealing with like packages, and you're like the post
[312.52 → 314.82] office, all you really care about is like, give me the dimensions.
[315.02 → 317.32] You don't typically care what's specifically in the box.
[317.32 → 319.20] Like you might have something like, is this hazardous?
[319.92 → 321.12] You know, a couple of things like that.
[321.16 → 324.98] But once you've checked those things off and those are sort of more behaviours that just give
[324.98 → 326.92] you some quick data back, and they don't necessarily block.
[327.04 → 331.26] But interfaces can cover everything on that broad spectrum of, you know, start a server
[331.26 → 335.16] that can start up any type of server, or it could be, you know, just give me some information.
[336.14 → 336.20] Yeah.
[336.24 → 341.42] And I love in Go that you don't have to explicitly say that you're implementing an interface.
[341.80 → 347.54] So in a lot of languages, when you create your type, you actually list out all the interfaces
[347.54 → 348.76] that you're going to implement.
[349.40 → 353.56] And then the IDE usually helps you enforce that and make sure that you put all the right methods
[353.56 → 355.22] in so that you satisfy the list.
[355.44 → 357.16] It doesn't work like that in Go.
[357.68 → 359.88] In Go, it's called structural typing.
[360.22 → 365.14] So it's kind of like duck typing, but because it happens at compile time, it's called structural
[365.14 → 365.84] typing apparently.
[366.18 → 370.36] But the duck typing idea is if it looks like a duck, and it sounds like a duck, it's a duck.
[370.78 → 374.76] And it's kind of like saying, yeah, so here's the interface with a few methods.
[374.76 → 381.38] And even if you didn't know about this interface, you can still implement it, or you can write
[381.38 → 385.48] interfaces to things that already exist, or that other people have written.
[385.74 → 389.02] So that turns out to be really quite powerful as well.
[389.28 → 389.38] Yeah.
[389.46 → 394.82] The implicit over explicit is really where it shines in terms of the interfaces.
[395.20 → 399.50] And I know a lot of new people coming to Go, I've seen from class, really struggle
[399.50 → 405.56] with that bit, understanding that just because they've written a method, they are now implicitly
[405.56 → 409.84] implementing an interface, and they get hung up on, well, how do I know that I'm implementing
[409.84 → 410.58] that interface?
[410.68 → 414.40] And I'm like, well, it's not important until you need to use it as an interface.
[414.70 → 416.42] Like that's the beauty of it.
[416.44 → 417.26] You say, well, how do I know?
[417.32 → 418.14] You just look at the docs.
[418.24 → 419.16] What is this thing taking?
[419.22 → 419.98] It's taking a writer.
[420.10 → 420.74] What's a writer?
[420.90 → 424.56] A writer is anything that implements the right function, takes a slice of bytes, turns it
[424.56 → 425.20] into an error, right?
[425.96 → 427.22] That's the beauty of it.
[427.24 → 428.04] You just kind of do it.
[428.04 → 430.70] You don't have to worry about tying into all these other things.
[430.78 → 435.54] It also means, and we can definitely talk on this later, that you can break a lot of
[435.54 → 437.16] dependencies too.
[437.44 → 442.50] Just you can keep dependencies out of the mix by using interfaces in ways too as well,
[442.54 → 443.22] which is quite nice.
[443.22 → 450.12] So yeah, along those lines, my favourite use of interfaces is to leverage its ability to
[450.12 → 456.74] provide that sort of independent means of sort of decoupling packages, dependency between
[456.74 → 457.48] packages, right?
[457.48 → 460.78] So for example, I do a lot of work with AWS SDKs.
[461.22 → 466.82] And for example, when writing a lot of data to say Dynamo DB, I don't necessarily have to
[466.82 → 473.90] bring in the AWS SDK, the Dynamo DB interface or implementation anywhere near my code.
[473.90 → 484.08] I can simply create an interface that I expect my code to use and basically have that interface be local to my code, not even export it to the rest of the application at all.
[484.28 → 486.18] Have that be local to my code.
[486.18 → 496.94] And maybe in my main package, when I'm initializing my application, I can then basically, you know, initialize a value that represents a client to my Dynamo DB server and then pass that in.
[497.02 → 502.02] And as long as it satisfies the interface I've defined for my code locally, everything is good, right?
[502.02 → 506.88] My code didn't have to know anything about the fact that it's even a Dynamo DB implementation at all, right?
[506.90 → 508.68] It can be anything that actually implements that interface.
[508.96 → 514.54] So that allows you to create that separation, that decoupling, you know, because of that implicit satisfaction of those methods.
[514.54 → 519.84] It really allows you to keep your code separate and not depend on any sort of externalities at all.
[520.16 → 522.06] That's my favourite part of using interfaces.
[522.48 → 529.80] I'm glad you brought that up because like Mark was saying, a lot of people get hung up on this fact that how do I know if I'm implementing an interface?
[530.36 → 536.70] And I think that it's a weird paradigm to get used to is like your kind of lift that responsibility off your shoulders.
[536.70 → 541.68] And it's the person who's using the type that actually has to care about is this going to be implementing an interface?
[541.68 → 543.26] And then they define the interface.
[543.52 → 551.84] Like you were saying, Johnny, your code that, you know, needs something that interacts with a database of some sort, it defines the interface, and it doesn't even necessarily have to export it to the rest of the code.
[552.52 → 559.34] And it's weird to get used to that when you come from another language like Java or something where you're explicitly saying like, here are all the interfaces I'm implementing.
[560.02 → 562.12] And that's very different from the way it is in Go.
[562.12 → 563.18] In Go, you just write your code.
[563.26 → 569.56] And then if somebody wants it to be an interface, it's their job to define the interface and, you know, sort of make sure that it's the right one.
[569.56 → 582.10] Yeah, a lot of, especially again, new developers don't realize is that you can create non-exported interfaces inside a function or a method and to use to check right there.
[582.30 → 583.64] Like you don't have to export them.
[583.98 → 585.96] You don't have to have tons of interfaces.
[586.36 → 590.70] You can say, I'm looking for one very specific thing, create an interface in line right there.
[591.10 → 592.80] And it's amazing.
[592.90 → 599.44] It's so wonderful that you can do stuff like that, you know, because you can even then turn around and create your own like default implementation.
[599.44 → 603.30] Of that interface using functions and types, right?
[603.44 → 607.76] You know, to have a backup in case the thing you're looking for doesn't exist or is nil or whatever.
[607.90 → 613.88] It's such a wonderful way of working and asking for and getting more and more enhanced functionality.
[614.12 → 622.24] Like along those lines, I've seen way too many times whereas I'm writing my code, if I happen to, I used to create public interfaces all the time.
[622.24 → 624.58] And then I realized, okay, first, I don't need to.
[625.12 → 630.14] And the reason, and I came to a point where I'm like, every time I create a public interface, right?
[630.34 → 637.72] I'm kind of implicitly saying to whoever is going to use this package, this code that, hey, you can actually depend on this because I've exported it.
[638.04 → 638.12] Right.
[638.16 → 643.54] You can depend thereby making it hard for me to actually change that later on if I wanted to.
[643.66 → 643.80] Right.
[643.80 → 648.22] So like every other type, if you don't need to export something, don't.
[648.40 → 648.46] Right.
[648.54 → 656.54] So by keeping it local and private to the package, I'm basically saying, hey, I'm just going to, in my README, I'm saying, hey, this is what you should expect to send in.
[656.62 → 661.60] Or you can actually read the code, the implementation, and then see what is expected, what interface you expect it to satisfy.
[661.98 → 664.32] And then that enforces that separation.
[664.48 → 664.60] Right.
[664.66 → 665.96] So it removes the temptation.
[666.12 → 672.12] When I don't export it, it removes the temptation to actually sort of have that my interface be in your code.
[672.12 → 672.28] Yeah.
[672.96 → 683.06] So that's interesting you bring that up, Johnny, because Eric Fugger on the Slack channel in GoTimeFM was actually talking just about that thing.
[683.28 → 692.18] And he says that he likes the idea of providing the interface with the implementation because you get this sort of explicit storytelling, I guess.
[692.52 → 697.92] And he's apparently challenged this before and people have said you don't need to do it, or it's unnecessary or something.
[697.92 → 700.88] But he asks for a more concrete reason.
[701.10 → 706.40] Why is it bad to ship the interface and a struct, say, if you've got a package?
[706.56 → 707.54] What are the pros and cons?
[707.76 → 708.90] I don't think it's wrong.
[708.94 → 710.86] And I don't think that's what Johnny was saying.
[710.86 → 720.08] And I think what he was saying, like most code, is start with the least amount exported and export what you need as you go.
[720.08 → 732.66] And I can tell you from very much so firsthand experience, and I'm feeling a lot of pain around a lot of this, is exposing too much of your API too early and exporting too much of it does cause problems.
[732.66 → 740.84] It causes a lot of problems down the line in terms of migrating things, just dependencies, things get stuck, and it becomes difficult to work with.
[740.84 → 748.30] If you start by exposing nothing and then expose the things you need as you go, that's really very, very useful.
[748.54 → 752.76] And so, yes, there are very much so reasons you should expose interfaces.
[753.14 → 755.18] I don't think anybody would ever say don't.
[755.68 → 757.04] Standard libraries littered with them.
[757.10 → 758.08] They are very useful.
[758.26 → 768.84] I think what Johnny's saying and what most people are advocating are don't expose the ones that people don't need to know about, the ones that are just useful for you inside your package.
[768.84 → 772.88] Only expose the ones that people need to fulfill to work with your package.
[773.88 → 778.12] Maybe I'm misunderstanding the question, but that's kind of the way I was kind of viewing it.
[778.56 → 779.36] Yeah, I think that's right.
[779.42 → 791.96] And I think I have a special place in my heart as well for single method interfaces for a kind of similar reason, like about the whole sort of minimalist mindset of keeping everything as tiny as possible.
[791.96 → 800.88] And doing that even down to the interface level, there are some surprising things that can happen which only work with single method interfaces.
[801.58 → 808.08] One example is just being able to use like a function type, like the handler fun is the great example of that.
[808.58 → 814.92] If anyone that hasn't seen that code, go and look up the handler fun and handler types in the HTTP package.
[814.92 → 824.98] It's not very much code, but it's very cool how there's a function type which happens to match the signature of the serve HTTP method in the handler interface.
[825.64 → 830.68] And it too implements the serve HTTP method and then just calls itself.
[830.80 → 832.28] So it's this kind of weird inception.
[832.66 → 836.92] It's the weirdest little thing that I think you encounter in Go often.
[836.92 → 838.22] It is.
[838.28 → 839.22] It's a beautiful little code.
[839.58 → 843.32] You know, I know that if you ask, you know, it was very much so a fallout.
[843.38 → 844.78] That wasn't an intended thing.
[844.86 → 847.80] That was just a fallout from the way the type system is designed.
[848.42 → 852.70] You know, for those of you who don't know in Go, you can declare your own types.
[852.80 → 858.98] Like we type, you know, we do type foo struct and that's declaring a new type based off of struct or based off of interface.
[859.18 → 860.56] We can do it off of into.
[860.80 → 862.08] We can do it off of slices.
[862.08 → 865.28] We can create new types off of anything, including functions.
[865.28 → 869.00] And when you do that, then you can put methods on that new type.
[869.44 → 874.88] And that method can implement, in this case, HTTP handler and then just call itself.
[875.04 → 876.14] I use it all the time.
[876.20 → 880.36] It's a wonderful little thing, especially for those single method interface.
[880.44 → 884.46] And even double, you know, depending on what the other methods are, you can easily mock those out too.
[885.16 → 885.50] Yes.
[887.28 → 887.72] Yes.
[888.18 → 888.78] Thank you, Matt.
[889.00 → 892.58] That was some, that was deep insight into what I just said there.
[892.70 → 893.38] I appreciate that.
[893.38 → 897.02] I was contemplating challenging it, but I was just going to let it go.
[897.10 → 900.14] But actually it only works with a single method interface.
[900.38 → 907.46] The, you know, that trick of doing the function thing, because, you know, there's only one function it can call.
[907.54 → 907.98] Right.
[908.34 → 910.58] Unless it's like a, like a close.
[910.72 → 914.52] Sometimes you get like a no op close, and then you can, you can implement those, actually.
[914.92 → 915.92] And it just doesn't do anything.
[916.42 → 916.58] Yeah.
[916.58 → 918.74] But on the testing side, it's incredibly useful.
[919.64 → 924.60] That's where I, that's where I use it all the time is to implement testing versions of these interfaces.
[925.22 → 925.32] Yeah.
[925.36 → 926.66] So that's another use.
[926.66 → 933.92] If you do have some kind of concrete dependency, like you're going to send an email, and you're using a package from SendGrid.
[933.92 → 936.54] Let's say that they didn't export an interface.
[936.78 → 938.90] So you only have a struct to work with.
[939.20 → 946.74] If you want to stub that out and test the code that you're writing, make sure it calls that, uses that SendGrid API in the way you expect.
[947.08 → 949.30] If that's indeed the kind of test you want to do.
[949.48 → 951.06] Then that can be quite tricky.
[951.06 → 954.22] If you forget that you can write the interface after.
[954.50 → 961.32] You can write an interface that just essentially describes the same methods that you're going to call in the original SendGrid API.
[962.06 → 964.24] You use that type instead in your real code.
[964.34 → 968.92] And then you've got an opportunity to build your own stubbed version of that you can use for testing.
[969.18 → 975.88] So that, if it, sometimes you can't avoid the situation of having to test those types of dependencies if you want to unit test something.
[976.26 → 979.66] And for those cases, it's, that's incredibly useful.
[979.66 → 984.20] So it's really worth remembering that you can write your own interface about something else.
[984.44 → 986.02] It doesn't always have to be the other way around.
[986.64 → 994.74] Another one that's come up with some of that weird stuff is any type that chains, like does method chaining, can be really hard to use an interface for.
[994.84 → 999.86] So you almost have to wrap the whole thing in something else that returns interfaces and sort of define your own interface there.
[999.92 → 1004.26] And it can get frustrating, I guess, at times, but it's just kind of the way it is.
[1004.84 → 1008.02] Yeah, method chaining is a real drag in that respect.
[1008.02 → 1011.16] Yeah, it's not very Go, actually, I think.
[1011.50 → 1012.16] No, it's not.
[1012.16 → 1019.88] These fluent, what we're talking about is these fluent APIs where every method call returns the object itself so that you can add.
[1020.24 → 1023.08] Or a clone or a modified or a new version of it.
[1023.26 → 1024.18] Yeah, right, right.
[1024.36 → 1024.56] Whatever.
[1024.76 → 1025.36] The same type.
[1025.70 → 1026.00] Yes.
[1026.50 → 1026.70] Yeah.
[1026.70 → 1028.24] Depending on what it's doing.
[1028.38 → 1028.52] Yeah.
[1028.66 → 1029.42] And I get it.
[1029.46 → 1031.40] And in some languages, they really work well.
[1031.78 → 1032.36] But they do.
[1033.00 → 1035.40] In Go, Go is very strict about types.
[1035.72 → 1043.00] And in this situation, it's very difficult for you to not replace wholesale some of these concepts with, you know, regardless.
[1043.48 → 1043.78] It's funny.
[1043.78 → 1050.18] So I ran into, I think, the very first time I've ever really wanted generics in Go the other day.
[1050.74 → 1052.30] It was all about interfaces.
[1052.74 → 1057.84] And the problem I had was I have two identical interfaces.
[1058.24 → 1061.90] And all they had was one method on them that returns a string.
[1062.34 → 1062.74] That's it.
[1062.86 → 1065.18] Just plain method.
[1065.36 → 1067.68] Just called name returns a string.
[1068.14 → 1068.98] Both the same.
[1069.40 → 1069.92] Both the same.
[1069.92 → 1071.42] Like, they're both called plugin.
[1071.54 → 1073.08] They both have a method called name.
[1073.30 → 1074.80] They both return a string.
[1075.02 → 1077.26] They're identical, just in different packages.
[1078.44 → 1082.14] But because they're in different packages, they are now different types.
[1082.54 → 1086.78] And you cannot use one as the other in, say, a return.
[1086.96 → 1089.66] Even though they implement the exact same interface.
[1089.94 → 1090.18] Yeah.
[1090.60 → 1092.06] They're not the same type.
[1092.16 → 1093.30] So, they don't work.
[1093.30 → 1098.02] That was the first time when it's like, well, the compiler could tell that.
[1098.02 → 1100.32] That information is there.
[1100.40 → 1101.10] They are identical.
[1101.32 → 1102.96] So they do implement each other.
[1103.06 → 1105.42] They are interchangeable interfaces.
[1106.34 → 1109.36] So, their types really shouldn't matter.
[1109.74 → 1109.84] Yeah.
[1109.96 → 1113.32] And that's a case where I think generics would have solved that problem.
[1114.18 → 1114.60] Yeah.
[1114.66 → 1118.02] So this was Russ Cox when they did the alias.
[1118.16 → 1119.54] Do you remember that type alias?
[1119.54 → 1119.90] Oh, yes.
[1120.04 → 1121.42] This was to kind of solve.
[1121.48 → 1122.16] It's still there.
[1122.26 → 1122.90] You know, it's here.
[1123.06 → 1123.54] It's in our code.
[1124.80 → 1125.02] Yeah.
[1125.02 → 1126.56] I mean, I've used it before.
[1126.78 → 1130.86] It's just, I feel like you're using something you're not supposed to be using when you use that alias.
[1131.54 → 1131.66] Yeah.
[1131.84 → 1132.98] That's the hard part with it.
[1133.02 → 1135.74] It's like, I've used it occasionally to experiment with some stuff.
[1136.24 → 1140.08] And it just feels like I'm doing something naughty that I'm not supposed to be doing.
[1140.22 → 1143.54] And I'm like, eh, I probably don't want to advertise this code now.
[1143.58 → 1143.86] Yeah.
[1143.92 → 1146.84] It doesn't quite do feel right when I use it too.
[1146.96 → 1147.30] I'm with you.
[1147.34 → 1148.94] It was a fix, I think.
[1149.18 → 1151.58] And yeah, it didn't quite do its thing.
[1151.58 → 1156.06] Now, what's interesting, we're hearing breaking news from the Slack channel.
[1156.62 → 1161.20] Marian is actually saying that in 1.14, there could be some changes.
[1161.78 → 1162.04] Oh, no.
[1162.12 → 1162.78] I think the changes.
[1162.96 → 1163.14] Okay.
[1163.40 → 1165.70] I'm reading it live as we speak for some reason.
[1166.44 → 1169.30] It's like proper live journalism, this, isn't it?
[1169.70 → 1171.48] No, it's just me reading out of Slack.
[1172.12 → 1174.62] I'm distracted by Slack even now.
[1174.76 → 1176.44] The overlapping interfaces.
[1176.44 → 1179.60] That's the overlapping in one struct.
[1179.84 → 1182.66] I don't think that's the same.
[1183.00 → 1185.18] Yeah, because you can just do that with structs, can't you?
[1185.20 → 1190.16] If you've got two structs that have exactly the same fields, you can just cast one to the other.
[1190.28 → 1192.04] And it's a very cheap operation.
[1192.36 → 1192.88] Is that right?
[1193.32 → 1193.98] I think that's right.
[1194.50 → 1197.24] No, you can cast the type that's based on the other type.
[1197.74 → 1198.76] What do you mean based on?
[1198.76 → 1200.06] I'm pretty sure what Matt's saying is right.
[1200.20 → 1203.34] It's just, it's one of those things that every time you happen to do it, you're like,
[1203.42 → 1205.78] let me go ahead and write this real quick and make sure it works.
[1205.78 → 1206.70] Yeah, make sure this works.
[1207.18 → 1210.56] Well, it's like if you have a type that's, you know, type my INT based on INT,
[1210.60 → 1212.92] you can cast it back and forth between my INT and INT.
[1213.00 → 1215.10] So I guess you could do that with a struct too, yeah.
[1215.34 → 1220.02] You can do that with, exactly, with structs if the same fields and same structure, essentially.
[1220.16 → 1224.00] You can do the same, just the name of it and then brackets and then pass the other type in.
[1224.12 → 1226.26] Yeah, that's not at all weird Go code.
[1226.64 → 1226.98] Exactly.
[1226.98 → 1229.96] And the fact that, I mean, it just feels like so brittle.
[1230.08 → 1233.70] But I guess if one of the structures changes, you get then a compile error.
[1233.70 → 1236.70] It's a compiled the time error because the types are no longer compatible.
[1237.28 → 1238.94] So maybe it's quite reliable, really.
[1239.50 → 1243.42] But it's surprising to see because it looks like you're calling a method, actually.
[1243.52 → 1245.60] It looks like you're calling a method and that is quite strange.
[1245.60 → 1253.90] The 114 feature that's coming in regard to the overlapping interfaces is that you can now,
[1254.12 → 1259.92] if you actually have two interfaces that have the same method before 114, you couldn't do that.
[1260.10 → 1262.90] Now, as long as they match, obviously, then you can do that, right?
[1262.96 → 1264.80] And obviously your implementation can only have one.
[1265.20 → 1267.36] Say you have an open method or something or whatever.
[1267.54 → 1269.02] Your implementation can only have one anyway.
[1269.02 → 1274.84] So it makes the fact that you have two, the fact that the embedded and the embedded have the same thing kind of makes it moot.
[1275.14 → 1276.12] So now you're allowed to do that.
[1276.20 → 1277.10] The compiler won't yell at you.
[1277.26 → 1278.20] So that's the new thing.
[1278.28 → 1280.50] I didn't know you weren't allowed to do that before, actually.
[1281.20 → 1281.78] Funnily enough.
[1282.10 → 1282.28] Yeah.
[1282.74 → 1283.96] Yeah, I think I never tried to do that.
[1284.44 → 1286.26] Yeah, certainly.
[1286.62 → 1288.40] I didn't know you couldn't do that.
[1288.48 → 1289.40] I thought they'd be all right.
[1290.98 → 1291.78] Anyway, now it is.
[1291.94 → 1293.24] Doesn't solve the problem I had.
[1293.24 → 1296.20] But yeah, it is useful that that fixes there.
[1302.06 → 1304.44] This episode is brought to you by Brave.
[1304.84 → 1306.66] We deserve a better internet.
[1306.98 → 1310.32] That's why the team behind Brave reimagined what a browser could be.
[1310.90 → 1312.76] Brave is like Chrome, the good parts.
[1313.08 → 1314.68] Even your extensions will just work.
[1314.92 → 1316.58] It has built-in ad and tracker blocking.
[1316.90 → 1318.68] Easy anonymization with the Tor network.
[1318.94 → 1322.18] Earn tokens while you browse and use them to tip your favourite creators.
[1322.18 → 1324.18] And did I mention it's lightning fast?
[1324.50 → 1327.12] Turns out the web is superfast when you remove all the cruft.
[1327.44 → 1332.14] Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[1341.18 → 1345.10] So I know this is like really delayed, but earlier we were talking about single method interfaces.
[1345.10 → 1353.78] I think the one thing that I want to point out is that one of the aspects of them that I really, really like is just that it makes writing closures and turning them into an interface much, much easier.
[1354.26 → 1354.36] Yeah.
[1354.46 → 1358.26] Because otherwise, like using a closure for an interface would be like a nightmare.
[1358.78 → 1359.12] Yeah.
[1359.22 → 1362.46] So I do this a lot with handler funk again, actually.
[1362.46 → 1369.68] So my handlers, which are usually methods on some server type, they, when called, return a function.
[1369.96 → 1372.14] So they return a handler funk, essentially.
[1372.50 → 1377.94] And in that case, the compiler will cast the type for you if it matches, actually, for that function case.
[1378.42 → 1382.94] And so essentially you get that little closure environment that you were talking about, John, where you can do some setup.
[1383.18 → 1387.52] You can prepare some resources if it's a web request, which it is in this case.
[1387.52 → 1393.00] And then in the body of the function you return, that's the hand, that's the real handler that gets called every time.
[1393.24 → 1395.26] So it's a tiny bit of indirection.
[1395.44 → 1400.28] But what you get from that is you can have per handler dependencies just passed in as arguments.
[1400.56 → 1408.72] You can have the little setup code all in one place near to, you know, where your actual handler is being done, the work of it.
[1409.14 → 1413.22] And similarly, you can have like request and response types also in that space as well.
[1413.30 → 1416.10] And it keeps them all in one place out of the way.
[1416.10 → 1423.82] And so for some projects, I think that's quite a nice little neat package, a nice little neat way of designing out these services.
[1424.68 → 1426.94] This is a good time for a commercial break.
[1427.10 → 1428.54] Please purchase.
[1429.40 → 1431.74] This dead air brought to you by Bit bar.
[1435.02 → 1435.54] Bit bar.
[1436.02 → 1438.34] For all your stroking of Matt's ego needs.
[1438.34 → 1442.74] We're going to like to find out after this that it's like Bit bar's not been working with the latest update or something.
[1445.44 → 1445.88] Yeah.
[1446.10 → 1447.16] Well, no, it works.
[1447.34 → 1449.50] It doesn't really need many updates, frankly.
[1449.68 → 1450.86] It's kind of like done.
[1451.10 → 1458.80] For anyone that doesn't know, it's the little project which puts the script, the output of any script or program into your Matt menu bar.
[1459.04 → 1462.12] And the contents of your password manager into Matt's email.
[1465.04 → 1465.44] No.
[1465.44 → 1468.94] I did, but it still comes through as little black dots.
[1468.94 → 1470.40] So I still can't read it.
[1470.48 → 1471.60] It was a mistake on my part.
[1472.08 → 1473.48] Open developer tools.
[1473.86 → 1474.06] Yeah.
[1474.06 → 1484.16] But so actually, it's a nice example, really, if we're talking about abstractions, because the key point is like this, the little tool doesn't really do anything.
[1484.16 → 1485.56] It just calls another program.
[1485.56 → 1491.32] And then the output of that program is what basically builds the menu bar and the menu that you get when you click it.
[1491.32 → 1502.36] So it's a kind of perfect example of an abstraction that really worked because there are hundreds now of plugins for this, and they all do kind of wildly different things.
[1502.36 → 1508.42] None of them that I could have imagined when I just made Bit Bar for the one case that I had it for.
[1508.72 → 1509.62] So it's nice.
[1509.72 → 1513.06] It's that that's the side of interfaces that enables other people.
[1513.06 → 1522.82] So if you do provide an interface or a very simple way for people to integrate and extend what you're doing, if that's easy, then more people are going to do it.
[1523.06 → 1527.06] And, you know, the point of having that there surely is for people to use it.
[1527.10 → 1531.48] It's what, you know, it's enabling other people to also build on top of what you're doing.
[1531.48 → 1534.58] So that's a great, even for its own sake, it's great.
[1534.70 → 1538.16] But obviously in business, there's massive value as we've seen as well.
[1538.88 → 1543.52] So we've talked about all the benefits of using interfaces.
[1543.70 → 1547.88] Can you think of reasons when you should not use an interface?
[1548.58 → 1549.66] That's a perfect one.
[1549.76 → 1552.16] I've definitely in the past overdone it.
[1552.46 → 1560.64] I've definitely done cases where I've overused interfaces when a simple struct, it turns out to be much simpler.
[1560.64 → 1569.88] I tend not to do that anymore because I tend to start with the structs first, and then I let the interfaces kind of find themselves or reveal themselves over time.
[1570.26 → 1572.82] So you don't design your code.
[1573.06 → 1577.74] You don't try to abstract too early by saying, oh, yeah, this thing's going to receive an interface.
[1578.16 → 1582.78] So, Matt, can you go on record right now as saying you don't design your code?
[1583.58 → 1585.38] Well, come on.
[1585.60 → 1586.84] Johnny just asked you a question.
[1587.02 → 1589.28] Do you or do you not, sir, design your code?
[1589.28 → 1591.40] I feel like it designs me.
[1592.44 → 1593.84] I don't even know what that means.
[1595.30 → 1597.62] Well, yes, I mean, obviously you do.
[1597.92 → 1601.84] And interfaces are a great way to do that as well, especially if you're collaborating with people.
[1602.08 → 1606.54] Like you could say, well, you know, we know that our two things have to communicate.
[1606.90 → 1610.76] So let's agree on the interface between them, and we can both build towards that.
[1610.96 → 1612.68] So in those contexts, it's great.
[1612.92 → 1617.48] But yeah, of course, like it is useful if you're just sketching out concepts, actually.
[1617.48 → 1625.00] Sometimes in my notebook, I'll actually write out Go interfaces to try and think about what these things are going to be doing and stuff.
[1625.62 → 1627.14] But yeah, I do tend to wait.
[1627.34 → 1631.16] You know if I'm doing a package, I want that to be the smallest possible footprint.
[1631.16 → 1638.40] So I am definitely in that camp of I wouldn't have an interface unless it was an extremely important part of this package.
[1638.68 → 1642.96] Like the reader, IO reader, IO writer, those kinds of types.
[1642.96 → 1658.80] I think like sort of building on what Matt said, one of the downsides to jumping straight to an interface is that it causes you to think, oh, I'm going to have like three implementations of this and starting to like focus on breaking things into like multiple versions when sometimes that's just never the case.
[1659.40 → 1661.58] The classic example is typically like your database.
[1661.72 → 1663.42] You're like, well, what if we switch out for another database?
[1663.42 → 1666.30] But in reality, most people never do that.
[1666.92 → 1678.72] So, you know, it's one of those like it's not that you can't do some of that stuff to sort of make it easier for you, but it doesn't make sense to bend over backwards to make this possible later when in reality, you're probably not going to do it.
[1678.72 → 1690.46] Yes. And often, whenever you think like that, the detail actually doesn't allow it anyway, like two different data stores often behave very differently.
[1690.78 → 1692.20] You wouldn't treat them the same.
[1692.38 → 1696.72] So it's more likely to encourage bigger changes anyway, isn't it?
[1696.82 → 1698.10] So I completely agree.
[1698.10 → 1703.52] Yeah, I've found every interface, like when I design interfaces up front, they're almost never correct.
[1703.52 → 1713.32] You know, it's just because you're guessing, you're taking a wild stab at what you think the interface, you know, is.
[1713.46 → 1731.54] And especially if you go ahead and publish that now, you know, I've been doing a lot of work with interfaces and whatever, but, you know, and recently, and I can tell you that, you know, a lot of what I've been doing now is working with stuff with problems that I do understand and problems that I do know what these interfaces need to look like now and how people are using them.
[1731.54 → 1740.18] But even then, I'm still saying, well, what's the simplest I can get away with and see how far I can push that before it starts breaking, right?
[1740.24 → 1745.80] And before I need a second month method or a concrete type or something further down the line.
[1746.06 → 1751.20] Yeah. So in Buffalo, in the Buffalo project, you're quite flexible.
[1751.40 → 1753.36] It's kind of like a framework, and it's flexible.
[1753.52 → 1756.30] It lets people plug different things in and out, doesn't it?
[1756.84 → 1757.26] Wait a minute.
[1757.46 → 1759.94] I feel like you jumped about 10 steps.
[1761.54 → 1761.84] Oh, really?
[1762.30 → 1762.64] Yeah.
[1762.90 → 1770.94] Oh, no. I mean, like generally though, Buffalo, well, the reason why interfaces are important and these kinds of concepts, abstractions are important.
[1771.04 → 1776.80] They're especially important in the Buffalo project because of the nature of it, the fact that you can use different technologies.
[1777.24 → 1783.52] Well, yeah. The reason I jumped ahead was I think Buffalo actually does a terrible job today of doing that.
[1784.28 → 1785.48] How does it work today?
[1785.48 → 1791.42] Well, today we have a lot of hard concrete types all over the place, lots of dependencies.
[1791.76 → 1800.56] You know, we've got a plugin system that goes and searches your path for executable binaries named a certain thing and asks them for information.
[1800.92 → 1801.74] It's very slow.
[1801.74 → 1807.76] So, generally, as a whole, the Buffalo project was very much so like a lot of projects, right?
[1807.80 → 1816.16] I started it when I first came to Go and, you know, I started writing Ruby for Go, basically.
[1816.58 → 1818.98] And we all bring our baggage with us, right?
[1818.98 → 1831.06] And so, a lot of this has grown over time with just, you know, me making choices that at the time seemed logical or at the time were what I just knew how to do because I didn't know go well enough to make those choices.
[1831.42 → 1841.10] And things kind of, you know, and then as projects grow, right, you know, things evolve and people come in and changes are made, and new requirements are added on, whatever.
[1841.10 → 1851.46] So, today, you know, what we have with Buffalo isn't as pluggable as I want it to be, and it doesn't achieve the goals I want it to in terms of, you know, saying I don't want to use pop.
[1851.54 → 1852.32] I want to use form.
[1852.58 → 1854.60] I want to make that as seamless as possible.
[1854.68 → 1855.54] I don't want to use form.
[1855.66 → 1856.70] I want to use nothing.
[1856.86 → 1863.68] I want to use, you know, ego templates or Raymond templates or whatever emulating you want, right?
[1863.72 → 1867.28] Or whatever it is you want to do, right now you can't do that in Buffalo.
[1867.28 → 1880.82] So, we, I, definitely had to go back to the drawing board, and we're currently rewriting it all now using a completely different system but all interface driven.
[1881.02 → 1883.68] Using pretty much all of what we've just been talking about.
[1883.86 → 1884.66] I have to ask though.
[1884.84 → 1885.10] Yeah.
[1885.76 → 1889.76] If I'm going to use a framework, I want it to make some decisions for me.
[1889.86 → 1890.92] I want it to be opinionated.
[1891.18 → 1895.94] I mean, personally, I think that's the reason why I use a framework and not kind of one of the reasons you use a framework, right?
[1896.04 → 1896.78] I'm with you.
[1897.28 → 1905.12] So, if you're now telling me, hey, you're going to provide this whole new pluggable system that can basically take any ORM tooling you want.
[1905.28 → 1909.12] It can use any, you know, UI interface you want.
[1909.22 → 1910.94] Whatever, whatever, all the bits and pieces.
[1911.04 → 1914.82] If you make everything pluggable, then I think, do you not create another problem now?
[1914.88 → 1916.70] Now you have to sort of document patterns.
[1916.88 → 1920.16] Hey, you could use, you know, this set of things.
[1920.30 → 1921.18] This for ORM.
[1921.42 → 1922.90] This for, you know, template generation.
[1923.12 → 1923.60] This for that.
[1923.60 → 1931.18] It's almost like you're pushing the decision to the user of the framework as opposed to being opinionated about it.
[1931.18 → 1933.46] Absolutely doing that.
[1933.68 → 1936.78] I think a little bit cleaner than you might be imagining it.
[1936.78 → 1946.88] You know, I mean, like Buffalo today, right now you can say, you know, generate a new app, and you get this whole web stack, and it's got Node, and it's got Pop, and it's got Plush and all that sort of stuff, right?
[1946.90 → 1949.28] And that's that very opinionated thing you're talking about.
[1949.30 → 1953.68] And there's also a flag you can generate a JSON one, which is slightly different, right?
[1953.68 → 1955.42] And that won't ever go away.
[1955.54 → 1962.78] That is just, you know, we will still have what, you know, this kind of, I don't know, Rails calls them like templates, but I'm not quite sure exactly.
[1963.52 → 1966.52] Like kind of default presets, if preset's a good word, right?
[1966.90 → 1970.64] Or you could say like, give me the web preset, you know, and Buffalo will ship with a few of them.
[1970.64 → 1978.02] And you're going to get a file, you know, you're going to get a Go file that has all those plugins in them, and you can just pull them out or add your own whatever.
[1978.40 → 1984.48] Or you could come up with a different preset that your company has of all these plugins and just use that instead.
[1984.96 → 1993.56] So yeah, there's always going to be opinions, and it's just like, you know, Rails basically generates a base camp for you whenever you do Rails new, right?
[1993.66 → 1998.70] I mean, Buffalo new will always generate the base camp for me, I would assume, right?
[1998.72 → 1999.50] Or something like that.
[1999.50 → 2001.80] But we need to make it easier for other people.
[2002.12 → 2003.52] You know, not everybody wants pop.
[2003.64 → 2004.96] Not everybody wants these things.
[2005.16 → 2011.86] And I know myself, I have hit points where I'm like, I need to do X, Y, and Z and I can't.
[2012.28 → 2014.60] Because I don't have the hooks in the tooling.
[2014.78 → 2019.64] I don't have the hooks in the library itself, right?
[2019.68 → 2024.98] I mean, we talk about tooling and CLI's and you start talking about how do you get versioning and stuff like that.
[2025.02 → 2027.38] But that's getting way off this track.
[2027.38 → 2040.28] Do you think if you had the opportunity to sit and design for much longer before you started Buffalo, that you would have come to these realizations just by exploring in your mind?
[2040.34 → 2042.88] Or do you think the process was important?
[2042.88 → 2043.98] Oh, God, no.
[2044.42 → 2046.60] I think everybody else would probably agree with it.
[2046.64 → 2049.06] You can't design stuff like this in a vacuum.
[2049.50 → 2067.06] If you've never written a web framework and managed a web framework and all that goes along with something like Buffalo, for example, or if you're writing Docker or whatever tool it is you're talking about, project you were talking about, you can't just start one of those in a vacuum and say, I know how to solve this problem.
[2067.06 → 2071.26] The problems are always infinitely more complex than you know.
[2072.42 → 2072.82] Always.
[2073.04 → 2074.34] It doesn't matter the domain.
[2074.56 → 2080.58] So, no, I could not have come up with a better design than I did when I first started writing Buffalo, when I first started writing Buffalo.
[2080.58 → 2099.64] What I can do is spend the last six months going on a kind of Constance, a vision quest, if you will, for code, trying to figure out what that needs to be, what it needs to be truly idiomatic and pluggable and easy and dependable and trusted.
[2099.96 → 2103.18] You can only do that sort of thing with time and experience.
[2103.18 → 2104.50] Yeah, absolutely.
[2104.68 → 2111.24] So, in the way this next API has emerged, in some ways, out of what you had before.
[2111.52 → 2114.34] But also, of course, it's not to say you shouldn't do any design.
[2114.46 → 2120.64] I mean, that's what you're doing now is when you're thinking about this, you're taking everything you know before and putting it into a new design.
[2120.78 → 2120.86] Yeah.
[2120.96 → 2122.74] So, of course, there's value in that.
[2122.74 → 2134.86] Yeah, I mean, we're currently rewriting the entire CLI project to a V2 using Pure Go and kind of interface-based plugins to really drive us in.
[2134.98 → 2145.22] And we're about, I would say, about 70% done, including some major pieces like generate, generate subcommand, generate resource, and build and test.
[2145.22 → 2148.38] And so far, it's holding up beautifully.
[2148.52 → 2152.52] And we've got very small interfaces, not a ton of them.
[2152.78 → 2154.18] They're all standard libraries.
[2154.42 → 2155.76] There's no, like, Buffalo types.
[2155.96 → 2157.10] Everything is a plugin.
[2157.34 → 2159.82] Even the subcommands are plugins.
[2160.12 → 2162.46] And it's all managed with just a slice of plugins.
[2162.70 → 2167.44] It's ridiculously simple in its concepts, but really powerful.
[2167.54 → 2172.22] You can build really amazing things with just a few interfaces if you line them up correctly.
[2172.22 → 2175.10] And think about what it is you're doing.
[2175.24 → 2178.12] And you set yourself a space to work in, you know?
[2178.24 → 2181.22] For me, it's been understanding that everything is a plugin.
[2181.90 → 2187.64] And, you know, so if you take something like Buffalo generate, that generate command is just another plugin.
[2187.84 → 2197.98] And it implements the one interface you need to be a subcommand of Buffalo, which is a main function that takes a context root string for where you are in the slice of arguments returns an error.
[2198.34 → 2198.56] Right?
[2198.60 → 2199.00] That's it.
[2199.08 → 2200.46] Now it's a subcommand of Buffalo.
[2200.46 → 2213.78] And that generate command, that generate plugin issues, you know, three or four interfaces maybe that say, hey, if you implement these, you're going to get these different lifestyle hooks when you run Buffalo generate.
[2214.02 → 2216.80] One of them being, say, a subcommand of Buffalo generate, like resource.
[2217.44 → 2218.00] And that's it.
[2218.12 → 2221.90] And so you can write your own implementation to generate.
[2222.28 → 2227.10] If you speak those couple interfaces, you can write your own drop-in replacement for it, right?
[2227.12 → 2228.64] Or any of the other things.
[2228.64 → 2231.52] So it's not about a lot of interfaces.
[2231.52 → 2233.34] It's about targeted interfaces.
[2233.54 → 2237.16] It's about defining the scope of where your interfaces are.
[2237.66 → 2242.08] Yeah, I like that idea, which I think everyone could actually use, potentially.
[2242.48 → 2245.48] You don't have to be building a kind of Buffalo for it to apply.
[2245.48 → 2248.62] But the idea of having hooks into something.
[2248.62 → 2256.20] So if you do have some process that's kind of a closed box process, but you may want some hooks into that.
[2256.72 → 2262.10] Having different interfaces for each hook, essentially, each method gets its own interface.
[2262.44 → 2266.62] And then they get to just implement the methods that they care about.
[2267.18 → 2271.68] You can, of course, check if a type implements an interface and go very easily.
[2272.10 → 2276.98] And if you use the two argument format, then, you know, you're not going to panic when they don't implement that.
[2276.98 → 2277.86] So that's pretty safe.
[2278.22 → 2282.60] So you could use that pattern to allow other people then to hook into your own code.
[2282.68 → 2284.62] And a bit like how you've done it for Buffalo.
[2285.08 → 2285.92] Yeah, exactly.
[2286.10 → 2297.24] One of the examples I like to use is the Buffalo Dev subcommand, which currently, you know, watches your Go files, compiles them, restarts your app every time you're working.
[2297.44 → 2300.54] Which is, you know, when you're working with a compiled language, it's great.
[2300.54 → 2303.30] So every time you go back to your browser, it's the fresh app again, right?
[2303.64 → 2304.98] And same thing with Webpack.
[2305.06 → 2309.04] But the problem is you can't add your own build scripts, right?
[2309.06 → 2313.62] You can't say, I want something else that's watching my files and running my tests.
[2313.86 → 2318.00] You can't have something else that maybe is starting up a Docker service, right?
[2318.06 → 2322.66] And, you know, there's no way of hooking into that build lifecycle, right?
[2322.66 → 2335.18] But you can easily add a couple plugins, and this is exactly what the develop plugin for Buffalo does now, or will do in V2, is it's like, okay, well, we've got a before develop and after develop.
[2335.28 → 2343.22] So if you want to set up some stuff, you need to launch Docker or whatever, write some files, you know, run migrations before everything starts up, do that.
[2343.50 → 2345.20] There's the teardown you can hook into.
[2345.58 → 2348.38] And then there's a develop that you can be.
[2348.38 → 2355.72] You can implement that, the developer interface, and get spawn off in a Go routine with everybody else, you know, to run your things you need to.
[2355.80 → 2361.36] And again, that's still, that's context, string, slice of strings, and error.
[2361.56 → 2365.04] And you get context gives you all that cancellation, right?
[2365.10 → 2369.92] You can easily test async code if you're taking a context as your first argument.
[2370.10 → 2376.22] So in this case, testing this plugin that runs all these things in a Go routine was super easy.
[2376.22 → 2381.58] I just wrote another plugin that implemented that one function, and then I just cancelled the context when it ran.
[2382.06 → 2383.98] That was all I needed to do.
[2384.40 → 2394.20] So they're easily testable, and you can hook in with so much ease that they're really powerful if you start thinking about interfaces in the right way.
[2394.66 → 2398.34] And yeah, you can do some pretty amazing stuff.
[2398.34 → 2404.54] Yeah, you reminded me of another one that's great, and John and I were talking about this the week as well.
[2405.34 → 2410.18] And it's this, it's that idea of being able to wrap things with interfaces.
[2410.82 → 2417.20] So a bit like how the middleware things work in the HTTP, where you have a function that takes in a handler and returns a handler.
[2417.20 → 2425.14] And then what you can essentially do is create a new handler that does extra things before and after passing the execution on to the other handler.
[2425.58 → 2428.28] And so that thing of wrapping is actually quite useful.
[2428.68 → 2437.06] And one trick that you can use as well, if you've got like a long-running IO copy operation, and you want to cancel that with context,
[2437.06 → 2447.02] you can create a kind of reader with context yourself, which essentially wraps another reader and intercepts the read method.
[2447.10 → 2448.84] And that's obviously the first one that gets called.
[2449.04 → 2454.02] Checks to see if the context has been cancelled by checking the err method.
[2454.24 → 2457.56] If that returns an error, it can then, the read method can return the error.
[2457.64 → 2460.52] If not, it passes it on to the inner reader.
[2461.02 → 2464.22] That's a way that you can actually get cancellable IO copy.
[2464.22 → 2469.02] You know, it's really cool to think that just because of these basic interfaces,
[2469.18 → 2474.46] you can add actually quite a lot of power just by thinking about it in the right way.
[2475.40 → 2477.92] Yeah, the reader's a really fun one to experiment with.
[2478.04 → 2482.96] Like I would definitely encourage anybody trying to get like to wrap their head around this idea to spend some time with that.
[2483.10 → 2486.38] Because like when I was messing around with the context, like Matt and I were talking about,
[2486.48 → 2488.06] is it possible to cancel a reader?
[2488.72 → 2492.98] And we, for whatever reason, we hadn't read the whole thread on the GitHub issue,
[2492.98 → 2496.02] where somebody actually proposed, you know, just wrapping it like we said.
[2496.34 → 2500.92] But in the process of looking at it, I was like, all right, well, let me go ahead and just throw this context in there
[2500.92 → 2502.92] and just check to see if it's cancelled and just stop it.
[2503.34 → 2506.16] Well, one of the issues you run into is if you're doing tiny files to test it,
[2506.56 → 2509.46] your one read will just read the entire file in one method call.
[2509.54 → 2510.54] So it's like, well, that doesn't work.
[2510.54 → 2517.80] But then you can quickly be like, okay, can I make like another, you know, another reader that limits it to reading five bytes at a time?
[2518.36 → 2524.36] And like now you have an easy way of saying like, you know, I can chunk this and make it a little bit easier to see when it cancels.
[2524.48 → 2529.26] And I can actually have another one that's set that after it reads maybe eight bytes, it actually cancels the context.
[2529.26 → 2535.82] So you can do these things to sort of like sequentially exactly see what's happening and make sure your code's doing what you think it's doing.
[2535.90 → 2539.28] And you get this, it ends up just, it's really weird, I guess, at first.
[2539.54 → 2544.74] But it's also really cool seeing like how much control you have over these things by just chaining these interfaces together.
[2545.34 → 2549.36] And this all stems from a single method interface, which is the crazy part.
[2549.50 → 2552.46] You know, it's not like we went ahead and had some really complicated types.
[2552.54 → 2553.56] It was just a read method.
[2554.02 → 2557.08] The single method interfaces are really key for stuff like that.
[2557.08 → 2564.18] Because like we've been talking about, you know, you can just create those types right there in your test and have them do whatever you need them to do.
[2564.98 → 2566.42] Whatever you need them to do.
[2566.54 → 2575.34] And then just an interface, whether it's read five bytes and cancel, whether it's, you know, capture the arguments and whatever that came into this function.
[2575.50 → 2580.06] So you can check them later and then cancel a context or return some error you want it to return.
[2580.06 → 2588.70] And you can just implement those types right there, implementations of them using simple functions or slices or whatever you need to do.
[2588.70 → 2595.62] And it'll never get as complicated as abstract classes and big class hierarchies used to in C Sharp.
[2595.76 → 2599.72] Because this technique really only works well with tiny little interfaces.
[2600.50 → 2600.54] Right.
[2600.58 → 2603.06] So I think we kind of go protects us a little bit there.
[2603.14 → 2605.98] There's another trick you reminded me of when we talked about wrapping.
[2605.98 → 2612.76] If you're doing an HTTP response, or you're writing to a file, and you're copying, or you're writing to that file.
[2613.04 → 2623.44] If you want to see what's been written out, you can actually just replace the writer with a multi-writer and pass in OS.standard out as one of the writers.
[2624.18 → 2625.82] OS.standard out is a file.
[2626.04 → 2628.18] So it actually implements cowriter.
[2628.78 → 2630.66] And you pass in also the original writer.
[2630.66 → 2633.10] So it still carries on doing what it was doing before.
[2633.34 → 2637.46] But because of that multi-writer, you also see it printed out into standard out.
[2638.02 → 2640.66] So again, tiny little, not many keystrokes.
[2641.54 → 2645.78] And suddenly you can peer inside your code without having to open up a debugger and things.
[2645.92 → 2649.72] And they're difficult to use, especially when you're dealing with byte streams and things.
[2650.40 → 2652.44] There are a lot of really cool ones like that in the IO package.
[2652.64 → 2656.16] Like treader is another one that it does kind of like what Matt was saying, I believe.
[2656.16 → 2661.20] Except whenever you're reading, you can actually pass in something that will write everything that it reads to that output.
[2661.80 → 2664.96] So you can actually have it write to standard out everything that it's reading from a file.
[2665.02 → 2669.70] So you can actually see like, what am I actually reading from this HTTP request body?
[2670.18 → 2671.26] And what does it look like?
[2671.28 → 2672.60] And you don't interfere with the rest of your code.
[2672.64 → 2677.10] You just wrap it real quick, test it, and make sure you look at it and visually see like, what am I getting?
[2677.50 → 2678.84] And then you can remove it as soon as you're done.
[2679.68 → 2681.50] Yeah, the multi-writer is awesome.
[2681.50 → 2687.56] I use that one all the time, just for that purpose, just for debugging what I'm expected to see.
[2687.62 → 2692.00] If I'm generating files or whatever, it's like, why am I not seeing that?
[2693.22 → 2695.26] Yeah, it's important, isn't it, in some cases.
[2695.58 → 2698.80] And sometimes you don't want to interfere with what it's doing.
[2699.24 → 2701.10] You don't want to invoke the Heisenberg principle.
[2701.28 → 2704.52] You want to be able to observe it and for it not to change behaviour.
[2705.26 → 2707.22] I mean, nothing's worse than like you're trying to debug.
[2707.22 → 2712.68] And in the process of like interfering with it, you break it yourself, and you're like, it was never going to work after I did that.
[2712.72 → 2713.26] Yeah, right.
[2713.54 → 2717.24] Yeah, I saw a great example which involved putting a log line.
[2717.36 → 2720.64] The log line slowed the program down enough that the behaviour changed.
[2721.78 → 2725.92] Yeah, and it was obviously the kind of thing you do when you're debugging something.
[2726.02 → 2727.28] You go and put some log statements in.
[2727.54 → 2729.46] Even that can interfere in some cases.
[2729.46 → 2739.52] Yeah, I used to have weird ones in Ruby where just the act of printing it would cause something in the function or the type.
[2739.56 → 2748.44] Whatever it was I was trying to debug would get kicked off, and it would actually produce different results when you printed it versus when you like just executed it.
[2748.62 → 2751.02] I think that's one that catches beginners off guard.
[2751.16 → 2755.54] Like if they're dealing with a linked list, they'll like iterate through it to actually print it out.
[2755.54 → 2758.58] And then they won't realize that their list is pointing to the end of the list, which is nothing.
[2759.16 → 2762.26] And then they'll be like, why is this like, why is it not working anymore?
[2762.76 → 2765.16] I've seen so many beginners get messed up by that.
[2765.40 → 2767.50] It's like, no, you need to reset back to the front of your list.
[2767.52 → 2770.60] And like if you don't have a pointer to that anymore, like you're done.
[2770.76 → 2773.12] Like, you know, so printing out really screws you up.
[2773.82 → 2774.14] Hmm.
[2774.54 → 2774.80] Yeah.
[2775.34 → 2776.08] That's a great one.
[2776.18 → 2778.58] Well, in Ruby, of course, you could just do anything.
[2778.58 → 2779.76] There weren't any rules.
[2780.10 → 2786.78] So someone probably that took the 2S method and just wrote their own and did some something crazy in there.
[2786.86 → 2787.38] And that's it.
[2787.68 → 2793.32] Well, it's usually was never even anything that like, you know, mean or intentional.
[2793.32 → 2802.14] It's usually like the 2S was probably calling some other method that, you know, that printed it gave you a default value.
[2802.14 → 2804.94] And it was maybe calculating a default value or something.
[2805.22 → 2805.30] Right.
[2805.30 → 2807.60] Or they maybe had some caching logic or something.
[2807.60 → 2808.48] Or exactly.
[2808.98 → 2809.18] Yeah.
[2809.44 → 2810.78] And so it was never necessary.
[2810.86 → 2811.72] It's not, it wasn't, I mean.
[2812.22 → 2813.24] I'm not sure if it wasn't.
[2813.30 → 2817.66] I wasn't suggesting Ruby people go around casting spells on each other or anything.
[2818.18 → 2818.64] No, no, no.
[2818.68 → 2826.14] And I've certainly had never modified the plus sign on Numeric and Ruby to do division to my coworkers ever.
[2828.30 → 2828.74] Yeah.
[2828.80 → 2832.56] Because why wouldn't you want a language that lets you change what the plus symbol does?
[2833.58 → 2834.44] Hey, you know what?
[2834.46 → 2835.68] It made debugging fun.
[2836.06 → 2837.08] You know, it was an adventure.
[2837.08 → 2838.04] Every time.
[2839.80 → 2841.88] I don't know if I want an adventure when I'm coding.
[2843.58 → 2844.88] I mean, when I was young, I did.
[2844.90 → 2847.18] You didn't like gripping for source code that didn't exist?
[2847.96 → 2849.80] That wasn't a fun time for you, Johnny?
[2850.38 → 2852.16] No, I don't miss method missing.
[2852.60 → 2854.26] You could implement every interface that way.
[2854.26 → 2855.26] You couldn't find it.
[2855.26 → 2855.28] You couldn't find it.
[2855.34 → 2856.22] So it's hard to find.
[2856.30 → 2857.26] It's hard to say it was missing.
[2858.40 → 2860.70] Method missing itself isn't defined anywhere.
[2861.12 → 2861.44] Right.
[2863.18 → 2863.96] Some noise.
[2864.40 → 2865.74] I do miss Ruby sometimes.
[2865.92 → 2866.74] It was fun to do.
[2866.82 → 2869.84] You could do some really fun stuff with things like method missing.
[2869.84 → 2874.38] You could, of course, do some very appropriate use as well.
[2874.52 → 2875.26] Oh, absolutely.
[2875.26 → 2875.80] Great examples.
[2875.80 → 2881.84] I mean, no, but honestly, you look at Rails and I mean, Rails was one of the things that
[2881.84 → 2883.60] made Rails was method missing.
[2884.10 → 2888.88] And like a lot of Rails is based entirely from method missing.
[2888.98 → 2894.38] All that magic that everybody loves in Rails is essentially using method missing.
[2894.50 → 2897.56] Sometimes well and sometimes, you know, not so.
[2897.56 → 2902.10] Yeah, so for anyone not familiar, basically, if you call the method on an object and if
[2902.10 → 2905.38] you do that in Go, if you call a method, and it's not there, that's a compile time error.
[2905.78 → 2907.46] In Ruby, it would just let you do that.
[2907.60 → 2911.90] But then it would just call like a catcall inside called method missing.
[2912.10 → 2916.04] And so you could then say, then it gave you a kind of second chance of seeing if you could
[2916.04 → 2916.90] do something with it.
[2917.00 → 2922.00] And yeah, a lot of the Rails things, you could write things like find by name and age.
[2922.44 → 2925.06] And then that becomes a new method that you just invented.
[2925.06 → 2930.66] Yeah, you basically would then, you'd parse out, you could parse the name of the method
[2930.66 → 2933.58] and generate, in that case, it was generating queries for SQL.
[2934.72 → 2940.38] And you could also, in Ruby, you could also, if a type didn't exist, a module or a type,
[2940.48 → 2944.82] you could also capture that and define types on the fly.
[2945.02 → 2951.70] So I had a library that distributed Ruby, and it would actually, if you just ask for any type
[2951.70 → 2957.80] inside a module, it would just create the module, it would create the type and connect
[2957.80 → 2961.94] it to a remote data source somewhere for the DRB stuff.
[2962.06 → 2967.76] And it just did all that by capturing those error hooks where things don't exist in Ruby.
[2968.16 → 2970.30] That's, I know, isn't it terrific?
[2970.30 → 2971.72] Oh my God.
[2971.84 → 2972.30] Oh yeah.
[2972.30 → 2972.38] Okay.
[2985.70 → 2986.36] Hi there.
[2986.54 → 2989.04] This is John Calhoun, one of your Go Time panellists.
[2989.58 → 2993.84] When I'm not working on Go Time, I create programming courses that help developers level up their
[2993.84 → 2994.34] Go skills.
[2994.34 → 2999.04] And one of my more recent courses, Algorithms with Go, is live, and I wanted to invite you
[2999.04 → 2999.64] to check it out.
[3000.10 → 3004.52] So it's completely free and in it, we explore how algorithms and data structures work as
[3004.52 → 3006.58] well as how to actually implement them in Go code.
[3006.96 → 3011.22] So if you've ever had an interest in learning about algorithms or data structures, or if you
[3011.22 → 3015.00] felt like you understand them conceptually but just couldn't nail down that coding part,
[3015.34 → 3016.54] this course is going to be great for you.
[3016.70 → 3020.76] We actually dive into coding everything, we work on practice problems, and it's a lot of fun.
[3020.76 → 3025.22] You can sign up completely free at algorithmswithgo.com slash Go Time.
[3025.72 → 3028.72] Again, that's algorithmswithgo.com slash Go Time.
[3028.92 → 3030.78] And don't forget that last slash Go Time bit.
[3031.14 → 3034.48] It helps me keep track of how you found out about the course so that Go Time gets credit
[3034.48 → 3035.20] for referring you.
[3035.60 → 3036.22] Thanks for listening.
[3050.76 → 3056.44] So getting back to Go.
[3056.70 → 3057.28] Yes, please.
[3057.50 → 3059.22] I feel like we've talked about interfaces a bit.
[3059.72 → 3061.42] How have we not talked about errors?
[3061.76 → 3063.88] Like, I feel like that's something we should talk about.
[3064.04 → 3067.62] Probably error is probably the most important interface we have in Go, actually.
[3068.16 → 3069.80] The best part of Go, you'd say, Matt?
[3069.98 → 3070.30] Matthew?
[3070.88 → 3072.80] The best interface in Go.
[3072.80 → 3074.80] I thought Bit Bar is the best thing.
[3075.30 → 3076.20] Bit Bar is good.
[3077.48 → 3078.42] There are no bones.
[3078.54 → 3079.66] No one's ever said it's not.
[3079.66 → 3082.90] Yes, Mark, you have said it's not.
[3083.94 → 3086.34] Yeah, but you shouldn't phone me at 3 a.m. to tell me.
[3086.84 → 3089.36] Well, when should I phone you to tell you?
[3089.36 → 3089.86] Like everyone else.
[3091.78 → 3093.10] Office hours, please.
[3093.28 → 3094.64] Your answer phone's full by midnight.
[3094.74 → 3095.64] I have no choice.
[3098.42 → 3098.78] Yes.
[3098.96 → 3099.92] Well, John.
[3101.16 → 3103.80] I mean, so I guess it depends on what we want to talk about.
[3103.94 → 3108.98] So the first, the obvious thing is, for anybody who's unaware, errors in Go are just an interface.
[3108.98 → 3112.82] It's an interface that just has the single error method, and it returns a string.
[3113.64 → 3118.66] And it's weird how powerful that ends up becoming because it allows you to return nil.
[3118.76 → 3121.56] It allows you to just return any specific error type you want.
[3122.10 → 3128.42] You know, I find that really useful because you'll see all this code where people get to return specific errors, and you can actually check them and see what they're doing.
[3128.42 → 3135.24] It's probably led to some bad patterns too, but it does let you, you know, do a lot more with the code than you otherwise could have.
[3135.72 → 3138.56] So I guess I'd like to explore that more, but I don't really know where to start.
[3138.64 → 3139.24] Any suggestions?
[3141.58 → 3143.42] I mean, there are a couple of things I'd like to look at.
[3143.48 → 3147.64] Like the first one is, for you guys, if you're writing code, do you return specific error types?
[3147.64 → 3153.70] Or do you just return an error that has a method and just tell them, like, look for this method with an interface?
[3154.92 → 3157.66] My first pass is with the simple error types.
[3157.80 → 3158.02] Yeah.
[3158.80 → 3171.66] And then if the program gets complicated enough where I care, where basically the call site needs to do different things depending on the kind of error it is, then I'll start using typed errors.
[3171.66 → 3178.08] I'm assuming, John, just real quick, just to clarify, you're not advocating that we don't return the error interface.
[3178.66 → 3179.16] No, no.
[3179.16 → 3183.80] You're just asking whether we use simple, like, thump.error for errors. New or custom errors.
[3184.14 → 3189.34] Like, to give you examples, like, IO has, like, specific errors like end-of-file and different things like that.
[3189.34 → 3189.78] Sentinel errors, yeah.
[3190.28 → 3196.68] So there are some like that, but then you, by using that, you then make anybody who's using your package have a dependency on your package,
[3196.68 → 3201.12] which a lot of times when you're using interfaces, your goal is to get rid of that neodependence.
[3201.12 → 3201.78] Right, yeah.
[3202.34 → 3206.48] But then the other side of it is you could return an error that, you know, just looks like the error,
[3206.68 → 3211.28] but then they have to actually check, does it implement this interface where maybe it has another method of some sort?
[3211.76 → 3211.98] Right.
[3212.02 → 3217.86] And then more recently, one of the things that makes that even more confusing is with all the wrapping of errors,
[3218.12 → 3222.48] when you start wrapping interfaces, you lose access to some of the embedded methods that are there,
[3222.54 → 3227.84] which is something we didn't really get into, but it is a more challenging thing to tackle.
[3228.38 → 3229.50] Oh, are we out of time?
[3229.50 → 3230.30] We got to go?
[3230.44 → 3231.68] We can't talk about this anymore?
[3231.80 → 3232.08] Oh, no.
[3232.98 → 3235.62] We could always do another episode on the more advanced stuff.
[3236.16 → 3237.86] As Mark tries to skirt out of the issue.
[3238.44 → 3240.26] I've used the error interface.
[3240.54 → 3242.82] I use errors. New by default for sure.
[3243.24 → 3245.84] Oh, see, I use full.error by default.
[3245.84 → 3245.86] Yeah.
[3246.16 → 3247.58] Well, I tend to use that.
[3247.66 → 3248.50] There's an errors package.
[3248.66 → 3251.52] Dave Cheney, by the way, was the one that coined sentinel errors,
[3251.82 → 3254.66] and they're the special variable error types that you return.
[3254.66 → 3259.70] When context package does this, it has cancelled and deadline exceeded to errors,
[3259.78 → 3262.00] that you can then see why the context has stopped.
[3262.76 → 3264.60] So, yes, that's nice.
[3264.72 → 3268.12] But as John said, it becomes part of the API, doesn't it?
[3268.12 → 3271.06] It becomes part of the public surface of it.
[3271.12 → 3272.76] So you then can't change that.
[3272.82 → 3273.36] You live with that.
[3273.42 → 3274.80] That's then a design decision.
[3275.16 → 3280.46] Sentinel errors also offer a problem in that they can be changed at runtime.
[3281.22 → 3281.90] Oh, right, right.
[3281.92 → 3282.66] Oh, that's fun.
[3283.14 → 3283.90] Because they're just variables.
[3283.90 → 3286.14] They're variables, package-level variables.
[3286.36 → 3290.10] So you can redeclare IOOF at any time.
[3290.60 → 3295.82] Julie Q does a good talk on finding dependable dependencies, Mark,
[3295.86 → 3298.26] which I really recommend you watch again.
[3298.88 → 3299.92] Oh, I've seen that talk.
[3300.28 → 3302.78] Dave Cheney has a good write-up on making constant errors,
[3303.08 → 3304.64] but I don't think everybody does it.
[3305.52 → 3306.58] But it is possible.
[3307.22 → 3308.94] Yeah, but it depends on what you're going to do with it.
[3309.02 → 3309.54] That's the thing.
[3309.54 → 3312.22] So it's nice to think, oh, we'll build this system,
[3312.30 → 3314.22] and all these errors will be strongly typed,
[3314.28 → 3315.36] and everything will be brilliant.
[3315.80 → 3317.10] But what's the real use?
[3317.18 → 3319.64] I mean, are you going to end up just sticking these errors in a log,
[3319.70 → 3323.46] or is it going to be a notification at some point if it's mission-critical?
[3323.82 → 3328.48] So what I've found myself doing is I sometimes find for myself,
[3328.66 → 3332.60] internally, Sentinel errors can be very useful in a few different places.
[3332.90 → 3336.08] So if I need one of those, and sometimes, sorry, not even a Sentinel error.
[3336.24 → 3337.08] Let me take that back.
[3337.08 → 3341.72] I just often might need to return the same error in multiple places.
[3341.72 → 3341.98] Right.
[3342.08 → 3346.12] You know, file not found, whatever the stupid error is, right?
[3346.30 → 3347.24] Resource not found.
[3347.40 → 3352.02] And so I might declare that as a non-exported variable, you know, error at the top
[3352.02 → 3355.06] that I can just return, but it's not for anybody else to use.
[3355.12 → 3356.12] It's not a Sentinel error.
[3356.26 → 3357.02] It's not exported.
[3357.32 → 3357.92] It's documentation.
[3357.92 → 3362.18] Yeah, well, it's no, it's just more so I can say return file not found error,
[3362.34 → 3365.40] as opposed to jump. Error f file not found.
[3365.50 → 3368.14] I can, you know, I can just kind of declare the error once and return it.
[3368.32 → 3370.04] But I'm not telling you to check for it.
[3370.08 → 3371.84] I'm not making you aware of it.
[3371.90 → 3374.38] It's just so that I don't have to change.
[3374.38 → 3374.64] Shorthand.
[3374.86 → 3375.74] Yeah, it's just shorthand.
[3375.84 → 3376.22] Exactly.
[3376.40 → 3377.54] Well, it does let you change it.
[3377.84 → 3379.42] It does let you change it in one place.
[3379.46 → 3379.70] Exactly.
[3380.22 → 3382.92] And so your methods would just return the error interface.
[3383.12 → 3384.84] So externally, it just looks like a normal error.
[3385.00 → 3385.18] Right.
[3385.28 → 3385.42] Yeah.
[3385.42 → 3389.08] Of course, it is a normal error because you have, you either use errors new to make
[3389.08 → 3392.12] it, or it has somehow that error method on it.
[3392.12 → 3392.44] Yeah.
[3392.58 → 3396.16] And I've been leaning towards the behaviour driven errors.
[3396.74 → 3397.14] Right.
[3397.38 → 3400.86] Again, as you know, the last few months, as I've been working more and more towards,
[3400.96 → 3405.72] you know, using interfaces a lot more, that always, that makes more sense to
[3405.72 → 3407.88] me in terms of, you know, asking for information.
[3407.88 → 3410.96] But I don't return a ton of errors that are customized like that anyway.
[3411.68 → 3417.20] But we do have that losing the embedded history thing becomes a problem.
[3417.20 → 3421.82] It's kind of like, it's tricky because one of the cases that I'll use like errors with
[3421.82 → 3425.36] extra methods on them for is like if I'm building a web server, I sometimes like to
[3425.36 → 3428.46] differentiate between an error where I can actually expose some information to the
[3428.46 → 3432.30] end user in an error where like the end user just needs a generic something went
[3432.30 → 3432.72] wrong error.
[3432.88 → 3433.22] That's it.
[3433.22 → 3436.84] Because I've seen many applications that will just expose the error every time.
[3436.96 → 3438.66] And I'm like, that's probably a bad idea.
[3439.44 → 3441.68] You know, you shouldn't just be printing out strings when you don't really know what's
[3441.68 → 3443.70] in that string when it gets to the end user.
[3444.16 → 3448.70] And then the other like area I've seen it useful is if you have like users submitting
[3448.70 → 3453.28] forms, or they're doing something on the back end of your code, you might have the same
[3453.28 → 3455.22] code handling an API and handling forms.
[3456.06 → 3460.00] So it might want to return something that says like this field is wrong, or it's invalid or
[3460.00 → 3463.88] whatever. And then on the front end, you kind of render that differently. You know, if it's an HTML
[3463.88 → 3468.74] page, you're going to render like an input box with a red line around it. If you're dealing with
[3468.74 → 3472.92] JSON, you might have something that says like, this is the field that's wrong to try to help out the
[3472.92 → 3478.90] developer. So there are some errors that that's useful. But when you start wrapping them, it becomes a
[3478.90 → 3483.46] little bit trickier. And it's not impossible. Like with wrapping, it's not impossible, luckily, but that's like the one
[3483.46 → 3489.58] case of interface sort of embedding that it doesn't cause you to lose it. And that's because of the what the
[3489.58 → 3492.30] wrapper type? Is that what it is? That has the unwrap method?
[3492.40 → 3492.48] Wrap error.
[3492.62 → 3493.34] Yeah, wrap error.
[3493.66 → 3499.78] Yeah, that's like the only interface where like the name of it is not what the method is. So like it always
[3499.78 → 3506.14] throws you off. But because of that, you can actually write like errors dot as or is, I forget which
[3506.14 → 3507.72] one it is, but use one of those two.
[3507.82 → 3508.30] As is, yeah.
[3508.30 → 3512.40] You end up like having to find a bunch of variables ahead of time. And it's kind of like,
[3512.66 → 3519.02] it's not pretty looking, but you can do it. So like it not being pretty kind of makes you only
[3519.02 → 3522.50] do it when it's important. So that there is one upside to that is you just don't throw it in there
[3522.50 → 3525.96] for everything. It's like it has to be important enough for this code to look kind of ugly.
[3526.58 → 3526.76] Yeah.
[3527.04 → 3529.26] But it is like tricky sometimes.
[3529.46 → 3534.42] On that too, whenever you have APIs that return errors, or if you're going to show them in the UI
[3534.42 → 3540.92] somewhere, I personally think that should be its own explicit mechanism in your code. I don't think
[3540.92 → 3547.54] we should use error for that. I think error in Go code means something's gone wrong. Like it not,
[3547.66 → 3553.90] not that like you, this, this field doesn't exist or this, you know, you don't have permission to
[3553.90 → 3559.56] access this resource. Those kinds of things should be, I think, done explicitly because for these
[3559.56 → 3564.72] reasons it's too complicated, and you expect these different things to know too much about each
[3564.72 → 3569.58] other. But yeah, that was just a sort of extension on that. Otherwise, I completely agree. I have to
[3569.58 → 3579.18] say we are approaching that special time when we launch our new regular slot. It's time for your
[3579.18 → 3580.62] unpopular opinions.
[3599.02 → 3605.40] So let's go. We actually have, for the first time, we have a an unpopular opinion from our Slack channel.
[3605.40 → 3613.64] Dylan writes that interface names should be adjectives rather than ER verbs. So he prefers
[3613.64 → 3619.38] closable to closer. What do you think about that? Is that unpopular?
[3620.04 → 3626.78] All I'll say is sometimes it is hard to twist a name into following that convention. I mean,
[3626.92 → 3630.92] I'm with Dylan on that one. You know, you don't have to be dogmatic about it. Sometimes, you know,
[3630.92 → 3635.48] it just, for readability's sake, just makes more sense to go at what makes sense, right?
[3635.72 → 3641.58] I use a combination of both because some are abbots and some are errs. I mean,
[3641.68 → 3646.70] some are more describing and some are more doing. Some are more verbs and some are more
[3646.70 → 3652.12] adjectives, you know, or adverbs. And I think that's fine. I don't think you have to be dogmatic
[3652.12 → 3652.56] about it.
[3652.92 → 3655.88] Yeah, I think it's nice to have a general guideline to get everybody on the same page,
[3655.88 → 3661.10] but it's not, it's kind of like the what it was mentioned in the Slack channel as well,
[3661.18 → 3666.78] to accept interfaces return structs. It's not a rule. It's a it's a guideline to sort of get you
[3666.78 → 3669.92] moving in the right direction, but there's always exceptions to that.
[3670.20 → 3670.30] Yeah.
[3672.18 → 3679.86] Rococo Powwow on Slack says that they use a prefix for their interface names. And I know that in C-sharp,
[3679.86 → 3685.70] it was tradition to use like, I-closable so that you know it's an interface. Does anyone use,
[3685.70 → 3687.94] prefixes or suffixes or anything like that?
[3688.30 → 3692.76] If I see I in front of any interface, like that developer and I are going to have a little chat.
[3693.30 → 3699.02] You refuse to implement it. I'm not going to implement that ever. I'm not going to implement
[3699.02 → 3700.62] that interface, which takes a lot of work.
[3701.14 → 3705.60] That's just, well, you know, I mean, again, other languages do it, and it's idiomatic in other
[3705.60 → 3710.90] languages. So I think that's fine for those languages. In Go, it's not idiomatic. And so,
[3710.90 → 3716.94] you know, if, if a PR came across, I would, that had that for me, I would probably ask them to,
[3717.00 → 3723.18] to change it just because it doesn't conform with kind of idiomatic, oh, not for reasons I,
[3723.50 → 3726.94] I may or may not agree with. It's just, that's kind of what it is. But yeah.
[3727.64 → 3731.98] Like all of these are interesting too, because like the classic example of a like,
[3732.50 → 3737.80] so an example of a company, like going completely against like style guides for a language is like,
[3737.80 → 3742.84] Google was pretty notorious for going against the Python style guide slightly internally.
[3743.76 → 3747.78] And like, even when the creator of Python started working at Google, he had to suddenly
[3747.78 → 3750.98] not use his own style guide, which would have been frustrating, I'm sure.
[3751.46 → 3755.26] But I think if you have an organization where your entire org is like using the prefix,
[3755.82 → 3759.52] then by all means, you know, keep it consistent there. That's probably more valuable than,
[3759.62 → 3763.50] than being idiomatic. But if you're working on open source, then you need to like to conform to
[3763.50 → 3765.62] whatever the, you know, the norm is there.
[3765.62 → 3768.04] Like, I say find out during the interview.
[3769.46 → 3772.78] I mean, because I would seriously have a problem with that.
[3773.30 → 3775.96] So Johnny, the interview's over. Do you have any questions for us?
[3776.62 → 3779.86] Do you use any prefixes when naming your interfaces?
[3780.12 → 3780.78] Well, yes we do.
[3780.78 → 3784.94] I just need to see some code. I need some like legit production code with interfaces in it.
[3785.46 → 3789.16] I need either a 10% bump or I'm out.
[3791.30 → 3793.08] I like that there's still a price though.
[3793.08 → 3800.32] I mean, I am willing to overlook this, you know, but you have to make it worth my watch.
[3801.62 → 3805.34] They like to have an intern just write plugins for your, everything you use that just moves it.
[3806.26 → 3808.00] It just hides it, puts a Mac entry and commit.
[3808.14 → 3808.70] Yeah, exactly.
[3809.48 → 3811.26] Just rewrites you on save, right?
[3812.00 → 3815.08] Your own version of Grump just puts I in front of every interface.
[3817.56 → 3818.32] Go troll.
[3818.80 → 3819.54] That could be a tool.
[3820.04 → 3820.78] We could make that.
[3820.78 → 3821.82] Nice.
[3822.48 → 3822.92] Nice.
[3823.26 → 3824.70] Popular opinions, I guess.
[3825.24 → 3825.54] Yeah.
[3826.36 → 3827.48] What about you, Bates?
[3827.84 → 3829.42] Have you got an unpopular opinion, mate?
[3829.50 → 3829.86] Yeah.
[3830.76 → 3832.36] No, I don't have any popular ones.
[3833.56 → 3834.60] Everybody knows that.
[3835.66 → 3839.16] It was difficult choosing an unpopular.
[3839.80 → 3840.10] Yeah.
[3840.20 → 3841.64] That's the bit that you struggled with, wasn't it?
[3841.64 → 3843.24] That was the bit I struggled with.
[3843.24 → 3843.64] Yeah.
[3843.98 → 3849.70] And I think I'm going to come up with, I don't like the way that the main package and the
[3849.70 → 3850.88] main function is designed.
[3851.38 → 3851.86] I see.
[3852.24 → 3852.72] Explain.
[3853.16 → 3853.46] Explain.
[3853.84 → 3854.10] Explain.
[3854.62 → 3855.10] Yeah.
[3855.10 → 3859.80] I think it promotes global scope, for example.
[3860.16 → 3862.82] OS.arms comes to mind, right?
[3862.96 → 3866.54] We were just talking about you can redefine IO.EOF, right?
[3867.32 → 3873.12] And the problem with CLI's is if you're not immediately taking that OS.arms and handing
[3873.12 → 3876.24] it off to something else, it's hard to write tests around.
[3876.36 → 3877.76] Everything's kind of globally scoped.
[3877.98 → 3883.98] Present working directory, while it's technically being global, again, it makes it hard to test
[3883.98 → 3885.46] if you're talking about those things, right?
[3885.46 → 3890.36] So I feel like that and a context, we have no context when we're in there, right?
[3890.52 → 3894.34] And admittedly, that was all after context came out later.
[3894.34 → 3901.44] But if the main package was exportable, if we could call it, if the main function was
[3901.44 → 3908.14] exportable and, say, took a context, a current working directory, the arguments and returned
[3908.14 → 3911.46] even a basic error, still let us do OS.exit, whatever.
[3911.78 → 3916.86] But if we return an error, just do a default exit of some kind.
[3917.24 → 3923.98] And I think that allows for better tested CLI's, nicer looking code that Go can give us
[3923.98 → 3925.56] that information at runtime.
[3925.88 → 3927.94] That's not difficult information to give us.
[3928.38 → 3933.20] And I think it promotes a better kind of generally a better way of writing our CLI's.
[3933.28 → 3938.72] Right now, I feel a lot of CLI's get written in the main function by accident just because
[3938.72 → 3941.10] people are hacking away trying to get something to write.
[3941.18 → 3946.36] And then they've got a big, long main.go file that's not very well tested or broken out.
[3946.50 → 3952.36] And other people can't make use of that CLI without compiling and shelling out.
[3952.36 → 3954.18] I completely agree with that, actually.
[3954.34 → 3959.94] And what I solve that problem, though, by I have a little run function and that takes
[3959.94 → 3964.82] in the arms, and it takes in an IO reader and a writer, if there's standard in, standard out,
[3965.22 → 3966.18] and returns an error.
[3966.32 → 3968.14] And then I just have a standard little main.
[3968.72 → 3973.54] I do create a context in that main, which is cancelled when command C is hit the first
[3973.54 → 3973.82] time.
[3974.18 → 3975.08] That cancels the context.
[3975.22 → 3977.74] Then the second command C exits the program.
[3977.88 → 3981.52] So, you know, you don't want to be annoying people if it's hanging for too long or something.
[3981.52 → 3981.96] Right.
[3982.44 → 3982.96] And then, yeah.
[3983.10 → 3987.06] And then you can write test code and just call run and pass in a different slice of
[3987.06 → 3988.02] string for your arguments.
[3988.14 → 3989.68] You could pass in different writer.
[3989.96 → 3993.34] You could use a buffer so you can read then what was written by your tool.
[3993.46 → 3997.80] My biggest problem with that, which, you know, again, is definitely just having another,
[3998.22 → 4000.10] giving it to another function is a good thing.
[4000.18 → 4004.34] My biggest problem there is I still can't, as a third party, I still can't use your code
[4004.34 → 4005.76] programmatically from Go.
[4005.96 → 4007.10] Yeah, they're different, aren't they?
[4007.22 → 4009.74] Packages and programs are fundamentally different.
[4009.74 → 4015.34] So the way I'm trying to solve it in my code now is my main is very, very simple.
[4015.62 → 4020.28] It, you know, context background, get the slice of arms, get the working directory, and
[4020.28 → 4026.50] then hand all of that off to an exported main function that takes those things in a package
[4026.50 → 4028.16] that I can then work with.
[4028.32 → 4031.40] And I basically don't have to look at the main.go file ever again.
[4032.08 → 4032.52] Right?
[4032.52 → 4036.96] Now I'm just kind of off in Golan, and then you can come along and import it, and you can
[4036.96 → 4043.82] pass it a context, a working directory, and some arms and start using my CLI in your program.
[4044.44 → 4047.34] And it's really nice and clean and kind of top level.
[4047.56 → 4051.42] And I don't know, I've been finding as a pattern, it's been working really, really well for me
[4051.42 → 4051.84] recently.
[4051.84 → 4054.44] Do you shell out or do you call them directly?
[4055.02 → 4055.52] What do you mean?
[4055.74 → 4059.46] Do you create a command exec and run an actual sub process?
[4059.62 → 4061.92] Is that how you run things or do you just call?
[4062.92 → 4066.66] I think he just has a method, like he just calls a method or a function on another package.
[4067.08 → 4068.12] Yeah, exactly.
[4068.32 → 4071.52] Like he might name the other package mark, and it might have a main exported function
[4071.52 → 4075.26] and he calls mark. Main inside his actual main that doesn't do much.
[4075.72 → 4077.38] I bet he does have a program called that.
[4078.12 → 4078.72] I know, right?
[4078.72 → 4080.04] I was thinking the same thing.
[4081.40 → 4086.42] I've been leaning towards a CLI package and then like I said, having a type, not even
[4086.42 → 4090.72] a top level function, but a top level type, you know, a type there, you know, whatever
[4090.72 → 4091.28] it is.
[4091.54 → 4093.66] And that has the main function on it.
[4094.12 → 4096.08] Again, it just no scope, right?
[4096.10 → 4097.40] I don't want top level.
[4097.56 → 4099.04] I don't want any global scope here.
[4099.72 → 4104.86] A zero value struct should be able to handle that CLI.
[4105.22 → 4108.00] And like I said, it's a pattern I found has been working really well for me because then
[4108.00 → 4113.54] I can kind of manipulate whatever I need to just with those three kind of pieces of function
[4113.54 → 4114.76] at those three pieces.
[4115.26 → 4115.64] It is nice.
[4115.70 → 4117.50] So the go makes it easy enough to do that.
[4117.56 → 4120.70] Like you found a pattern that works for you, and you can sort of build around that.
[4120.70 → 4125.18] And it's so like, I get what you're saying, but I also feel like because it's so easy to
[4125.18 → 4128.86] sort of just build around it, that it's kind of a not that much of a limitation.
[4129.66 → 4131.00] No, it's not necessarily limited.
[4131.08 → 4132.90] It's just an unpopular opinion, by the way.
[4132.90 → 4139.96] I'm just saying it would, you know, like if they were to rethink it for V2, those would
[4139.96 → 4141.32] be my suggestions for.
[4142.30 → 4145.08] Well, I'm those bombshells of suggestions.
[4145.08 → 4145.22] Whoa, whoa, whoa.
[4145.22 → 4145.96] Where's Johnny's?
[4145.98 → 4147.44] Isn't Johnny supposed to come up with one today?
[4147.72 → 4148.14] Nah, man.
[4148.16 → 4148.78] That's next week.
[4148.96 → 4149.70] Oh, that's not cool.
[4149.82 → 4150.18] I need time.
[4150.18 → 4151.34] I need time to think about this.
[4151.34 → 4151.66] Oh, yeah.
[4151.82 → 4152.10] Fine.
[4152.52 → 4153.22] He's too nice.
[4153.28 → 4153.64] That's right.
[4153.68 → 4154.22] He's too nice.
[4154.32 → 4155.56] I remember now.
[4155.80 → 4155.98] Yeah.
[4156.04 → 4156.36] That's right.
[4156.36 → 4159.56] He broke into a cold sweat when we said we managed to upset somebody.
[4162.02 → 4164.22] Well, that just makes him a nice guy, doesn't it?
[4165.40 → 4166.78] I like how these two offset each other.
[4167.08 → 4168.68] Mark's nowhere near too nice.
[4169.44 → 4170.52] Oh, yeah, absolutely.
[4171.24 → 4171.34] Yeah.
[4171.60 → 4173.82] And Mark trolls him for being nice.
[4174.00 → 4175.96] That's how we've got to.
[4176.18 → 4177.82] That's how evil I am.
[4178.42 → 4180.04] Well, welcome to the internet.
[4180.46 → 4183.04] And I'll say our goodbyes.
[4183.10 → 4184.10] We've reached the end of the show.
[4184.22 → 4185.10] Thank you very much.
[4185.10 → 4186.60] Mark, Johnny, and John.
[4187.40 → 4191.68] Hopefully, everyone's learned a little bit about interfaces and abstractions and grappled
[4191.68 → 4195.40] with them as you go into your future endeavours.
[4195.90 → 4196.98] We wish you all the best.
[4197.06 → 4198.00] We'll see you next time.
[4202.70 → 4204.04] That's our show for this week.
[4204.20 → 4207.18] Thanks to Dylan and the Gopher Slack for sharing that unpopular opinion.
[4207.54 → 4209.12] We love hearing from all the Gophers out there.
[4209.42 → 4210.06] Hit us up on Twitter.
[4210.16 → 4211.46] We are at GotimeFM.
[4211.68 → 4213.70] Or comment directly on changelog.com.
[4213.70 → 4216.28] Just click the discuss on changelog news link in your show notes.
[4216.50 → 4220.56] This episode was hosted by Matt Refer with panellists Johnny Portico, John Calhoun, and
[4220.56 → 4221.06] Mark Bates.
[4221.34 → 4225.46] It was produced by me, Jared Santo, with music by the oh-so-mysterious BMC.
[4225.66 → 4227.18] We're brought to you by awesome sponsors.
[4227.34 → 4227.86] Support them.
[4228.00 → 4228.68] They support us.
[4228.84 → 4232.14] We've got Vastly on Bandwidth, Linde on Hosting, and Rollbar on Bugs.
[4232.38 → 4235.64] The changelog master feed is your one-stop shop for all of our podcasts.
[4235.64 → 4241.86] You can find it by searching changelog master in Apple Podcasts, Overcast, Spotify, or wherever
[4241.86 → 4242.78] you get your podcasts.
[4243.04 → 4244.46] All for the price of a free bit bar.
[4244.88 → 4245.70] Thanks again for listening.
[4246.10 → 4246.92] We'll talk to you next week.
[4246.92 → 4276.90] We'll be right back.
[4276.92 → 4306.90] We'll be right back.
[4306.92 → 4336.90] We'll be right back.
[4336.92 → 4337.22] Yeah.
[4337.62 → 4338.34] So let people in.
[4339.00 → 4339.20] Okay.
[4339.48 → 4340.40] Two minutes.
[4340.72 → 4342.90] Let's all sit in uncomfortable silence then.
[4342.96 → 4344.46] Well, I don't think it has to be silent.
[4345.46 → 4348.06] You can still be uncomfortable, and we'll be talking.
[4349.20 → 4349.96] No need to be.
[4350.28 → 4353.38] Otherwise, if we do that now, then what are we going to do for the next 60 minutes?
[4354.04 → 4354.28] Yeah.
[4355.56 → 4357.40] Not talk and make things uncomfortable.
[4358.90 → 4359.30] Yes.
[4359.30 → 4359.92] Wait.
[4359.92 → 4359.96] Yeah.
[4361.64 → 4362.12] Wait.
[4362.38 → 4363.42] You all weren't kidding about that?
[4364.22 → 4364.58] What?
[4365.88 → 4368.52] Then we just genuinely ran out of things to say.
[4369.60 → 4370.48] That's it, folks.
[4370.56 → 4371.50] We're numb with the episode.
[4372.84 → 4373.94] Come back next week.
[4373.94 → 4374.68] Is that it?
[4374.68 → 4375.60] That was amazing.
[4375.90 → 4377.10] That hour flew by.
[4377.36 → 4378.42] Thank you for having me.
[4378.56 → 4380.38] It's the best hour I've ever spent with you, Mark.
[4381.68 → 4382.12] Definitely.
[4383.12 → 4383.40] Wow.
[4384.14 → 4384.58] Absolutely.
[4385.42 → 4385.90] Yeah.
[4385.90 → 4387.90] This isn't the show yet.
[4388.14 → 4388.92] I hope not.
[4389.22 → 4389.50] No.
[4389.68 → 4389.92] Mm.
[4390.82 → 4391.00] Thank you.
[4391.00 → 4391.26] Thank you.
