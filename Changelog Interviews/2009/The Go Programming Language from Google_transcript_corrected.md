[0.00 → 19.86] This is Changelog Spotlight 0.0.3.
[20.84 → 22.84] We spoke with Rob Pike of Google.
[22.98 → 26.80] He's one of the principal engineers of Google and also one of the leads behind their open
[26.80 → 27.94] source language called Go.
[27.94 → 30.16] I'm Adam Stachowiak.
[30.76 → 31.54] And I'm Wynne Netherlands.
[32.70 → 38.00] And yeah, so we had a really awesome interview with Rob Pike, a very candid guy.
[38.10 → 39.42] It was a super awesome interview.
[40.54 → 42.38] Very passionate about this new language.
[42.58 → 44.44] Yeah, had a lot of good things to say about it.
[44.82 → 47.80] Which I'm not sure yet if it's revolutionary or evolutionary.
[48.22 → 51.54] I think it's attacking some problems on a couple of fronts.
[52.02 → 54.10] Developer productivity being one of them.
[54.10 → 57.94] He mentioned being able to do builds faster internally at Google.
[58.70 → 65.28] And if you watch the video on golang.org, the build times for this language are incredibly fast.
[66.36 → 74.26] The concurrency also looks to be eating into some of Erlang's promise as well.
[74.26 → 82.52] Although, Rob, in the interview, as you'll hear, kind of downplayed any plans that they have for Go to attack any language.
[82.80 → 86.88] But you can't say concurrency without thinking Erlang.
[87.32 → 87.52] Right.
[87.86 → 100.08] And he talked about Google and infrastructure and how they want to use Go to gain productivity with building out their infrastructure, pieces of software, and stuff like that.
[100.08 → 101.94] So that's kind of awesome.
[102.26 → 106.84] And for a new language or a new software project, for me, that's the proof.
[107.74 → 113.02] That's where you eat your own dog food, so to speak, as someone at Microsoft once coined.
[113.56 → 124.26] You know, as a .NET developer back in the day, that was one of the things that I always found interesting is how very little Microsoft used their .NET platform and C Sharp in building their apps.
[124.26 → 133.10] I think if Go is going to make a go of it, no pun intended, they're going to have to get some inroads at Google and start building out some of these projects internally.
[134.42 → 135.04] Yeah, absolutely.
[135.14 → 142.38] I liked how he was talking about writing server software, too, with the concurrency in mind to make them faster, too.
[142.46 → 143.86] That's a very good play.
[143.94 → 147.52] And also piggybacking off another product of theirs, which is Google App Engine.
[148.14 → 152.74] So eating their own dog food is something that Google does a lot, and it's nice to see them do that with Go.
[152.74 → 153.74] So, absolutely.
[155.10 → 155.68] Cool, man.
[156.12 → 156.78] Anything else?
[157.26 → 158.14] No, it's a great interview.
[158.24 → 158.78] Let's get to it.
[158.88 → 159.12] All right.
[166.66 → 167.42] All right.
[167.48 → 169.20] So we're here with Rob Pike.
[169.30 → 171.14] He's a principal engineer at Google Inc.
[171.76 → 177.06] Everybody knows Google, and they've come up with this awesome new programming language that is getting lots of buzz.
[177.16 → 177.68] It's called Go.
[178.04 → 181.04] And Rob, why don't you introduce yourself and tell us a bit about who you are?
[181.04 → 183.64] I'm Rob Pike.
[183.64 → 189.12] I worked at Bell Labs for many years with the original guys who did Unix.
[189.64 → 194.24] I worked with Dennis Ritchie, Brian Kernighan, Ken Thompson, people like that.
[194.24 → 199.42] And then we did a number of interesting things over the years, including the Plan 9 operating system.
[200.20 → 205.46] Ken and I did what is now known as UTF-8 for international character support.
[206.18 → 219.02] And about seven years ago, I came to Google and been working here in the infrastructure department, building new pieces of the stuff you don't see at Google.
[219.02 → 221.28] Although I did do a little work on the math project early on.
[221.74 → 229.08] Can you give us kind of brief history of Go, kind of where it came from, sort of the inspiration from it?
[229.08 → 241.02] A couple of years ago, Ken and Robert and I were doing a lot of work in C++, which is the main systems programming language here at Google still.
[241.02 → 245.98] And became frustrated at the scale at which Google operates.
[246.16 → 253.52] There's a tremendous amount of overhead in building software because of the dependencies, the libraries, the speed of the compilers.
[254.10 → 258.76] And it seemed like the language was holding us back in terms of productivity.
[258.76 → 267.50] And so just sort of for purpose of discussion, we started talking about what we would do if we were trying to solve those problems linguistically.
[268.08 → 279.04] And it occurred to us there are a lot of things that have changed since C++ and Java and so on were designed in the areas of hardware, networking, multicore processing, things like that.
[279.04 → 295.66] And so before long, we decided that there was not only sort of something to talk about, but there's actually an opportunity to design a language that would be much more nimble for software development and also be more up to date in regard to some of the changes in the computing landscape.
[295.66 → 300.56] But at the same time, there were obviously things that we wanted to think about differently.
[300.68 → 304.94] We didn't want to just be another version of C++ or C or any other language.
[305.06 → 312.20] So we started from the ground up and just wrote down what we wanted the goals to be and then tried to construct a language that met those goals.
[313.30 → 314.82] And then that was two years ago.
[314.90 → 322.62] And by the middle of last year, 2008, we were the original three of us, Robert Gruesomer, Ken Thompson, and I were working on it full-time.
[322.62 → 327.32] And then Ian Taylor came in with the GCC front end for Go.
[327.54 → 334.02] And then Russ Cox, who's a relative newcomer to Google, joined our team towards the end of last year.
[334.14 → 337.82] And that was the sort of core team that rolled it out, although we've had a lot of other help from a lot of other people.
[338.16 → 351.74] I was going to ask you what the team size was because one of the quotes that I liked most, actually, Wynn and I both liked most about what you said when releasing Go was that we understand that a significant fraction of computers, and I like that significant fraction of computers in the world, run Windows.
[351.74 → 355.92] And then you talk about your team size, that you have a small team, and you don't have a lot of resources.
[356.04 → 357.04] What is the team size now?
[358.28 → 360.74] It kind of depends on how you count, but pixyish.
[361.30 → 364.18] Some people, a couple of people aren't full-time, so call it six or seven.
[365.50 → 366.64] But it's a pretty small group.
[367.90 → 371.90] And can you maybe just enlighten us on why you said a significant fraction of computers?
[372.16 → 373.04] Is that something you said?
[373.94 → 377.26] I don't remember that quote, but, I mean, let's be clear.
[377.36 → 379.02] You know, a majority of computers run Windows.
[379.02 → 381.72] So there's actually a Windows port of Go running now.
[381.72 → 385.78] Some on the outside, the open source community has got one up and running.
[385.86 → 390.04] We hope to kind of have it officially installed in our release branch sometime very soon.
[390.40 → 394.20] It's one of the great things with open source software, things that we aren't good at doing.
[394.30 → 398.00] Other people out there are, and they can come in and contribute and really make a big difference.
[399.00 → 399.36] Absolutely.
[399.96 → 400.40] Hi, Rob.
[400.44 → 400.98] This is Wynn.
[401.82 → 405.42] Question around some of the goals that you mentioned going into the project.
[405.42 → 413.60] How much of the actual syntax of the language was designed up front, or did you really know what you wanted when you started?
[414.80 → 421.20] We actually put syntax pretty low down at the beginning, but, of course, it rapidly becomes a point of discussion.
[422.08 → 430.88] So early on, Ken suggested that one of us just own syntax for the beginning, and we'll not worry about that, just so we have something to talk about.
[430.88 → 441.28] And so Robert sort of owned the syntax for a while, but then, you know, Ken and I came in with things we wanted different, and so it became more collaborative later on.
[441.36 → 446.96] But the thing about it is that it wasn't – it was designed from the beginning, like everything else.
[447.12 → 454.34] We obviously borrowed a lot of stuff, but, you know, there was nothing sacrosanct in existing syntax that we thought we had to keep.
[454.34 → 458.92] It's important when you're doing something like this that you want to think of as a replacement.
[459.58 → 469.02] You have to thread this interesting line between making something that is really familiar to people so that they want to use it, but different enough to be interesting.
[469.62 → 475.32] If you make it look just like the other languages, then it's sort of harder to see that it's different.
[475.44 → 477.40] You were not reminded that you were in a different world.
[477.78 → 481.06] But if you make it too different, then people don't want to try it because it looks too weird.
[481.06 → 488.64] And I think we did a reasonable job there of making it feel like it belongs in the C family but not actually be just like C.
[488.76 → 491.92] So when you're writing Go code, you're aware that you're writing Go code, right?
[492.16 → 497.16] Whereas in the middle of a Java, JavaScript, or C++ program, it's kind of hard to tell which language you're in.
[497.66 → 502.04] I think we did a nice job there of getting some of the details different but for good reason.
[502.72 → 504.08] You know, that's an interesting point.
[504.08 → 513.52] I remember when C Sharp came out, Microsoft's language, the comparisons to Java were pretty rampant, I think, for good cause.
[513.80 → 516.24] What other languages influenced Go?
[516.24 → 525.80] I don't know that any languages exactly influenced it so much as the languages that we've worked in inspired how we think about programming.
[526.56 → 537.50] So some of the languages that the group of us have worked on before, obviously Ken was involved in actually D, the language that predated C, but he also had a big hand in helping shape C.
[537.50 → 544.46] I've done work in several languages before, mostly around concurrency, languages called New squeak and Limbo.
[545.88 → 552.88] And Robert has worked a lot in small talk, and he did a big part of the hotspot code generator for Java.
[553.68 → 563.68] And so he also did a lot of his training, you know, university work in the languages out of the Etihad and Zurich, languages like Oberon.
[563.68 → 573.38] So it was a pretty interesting mix of stuff, and you can see bits of those languages inside Go, but it would be wrong to say that they were exactly inspirations.
[573.56 → 578.16] They more sort of informed us how things would work if we used them a certain way.
[578.82 → 583.40] What types of software projects do you see being the sweet spot for a language like this?
[584.46 → 585.68] That's a tricky question.
[585.68 → 594.14] We definitely started the project because we wanted to write Google infrastructure in a language that was more productive.
[595.30 → 601.16] And so we definitely have in mind things like web servers and web front ends and storage systems and things like that.
[601.66 → 607.50] But in developing the language and bringing some of the details of the type system and stuff like that in,
[607.92 → 611.12] we found that it's actually pretty nice for a lot of other things too.
[611.12 → 617.72] And, you know, text processing, it's kind of, it's almost a nice scripting language.
[617.82 → 619.38] You can see it doing some things Python does.
[620.52 → 623.74] And I really don't know what the sweet spot is going to be.
[623.94 → 627.54] I think people will find that as they use it more and more.
[627.96 → 632.82] At this point, I think there's not enough people have really played with it in depth to know where it really belongs.
[633.72 → 636.24] We're certainly going to try to use it internally to build some infrastructure,
[636.24 → 642.72] but a lot of other pieces of stuff look like they're perfect fits for Google using Go.
[642.88 → 651.32] An example is that the concurrency model in the language makes it really easy to use what we call Go routines to do client handling.
[651.92 → 657.14] And that makes it possible to write servers in a much easier to understand and flexible way
[657.14 → 661.16] than the kind of event-driven or callback-driven mechanism that tends to get used.
[661.16 → 666.34] So people are already discovering there are things they want to write where Go is actually a perfect candidate language,
[666.42 → 668.78] even though it's not as mature as we hope it will be.
[669.32 → 673.70] Do you see that being a play for Erlang-type applications?
[675.58 → 680.42] I think it's, well, I don't like the word play.
[680.48 → 683.62] It sounds like we're trying to sort of, you know, supplant something.
[683.76 → 684.30] We're really not.
[684.38 → 685.74] We're just offering an alternative.
[685.74 → 692.34] But, yes, I think the kind of things that Erlang gets used for now, Go, is an interesting option.
[693.16 → 697.48] I don't think it's mature enough yet, but it will get there, and we're certainly trying to make it mature.
[698.16 → 702.52] Are there any tools right now that you guys are building, that Google's building using Go?
[703.52 → 707.16] We've got a few things internally, but nothing that's facing user traffic yet,
[707.20 → 712.96] with one notable exception, which is the golang.org website is entirely a Go program.
[712.96 → 718.30] There's actually, it runs on App Engine with a Python front end that acts as a cache,
[718.38 → 720.14] just because that's the easiest way to roll it out.
[720.34 → 724.48] But all the content comes directly out of a web server running on our internal infrastructure.
[725.32 → 726.14] All written in Go.
[726.60 → 731.04] Would you see the App Engine as a natural place to host Go applications one day?
[731.52 → 731.92] Absolutely.
[732.08 → 733.08] We want to see that happen.
[733.26 → 734.38] We're trying to make it happen.
[734.60 → 736.98] But there are a couple of steps we still have to get through first.
[736.98 → 741.54] But I think it would be a fascinating alternative language for App Engine stuff.
[742.82 → 743.46] We'll see.
[743.96 → 747.48] Yeah, I found the notion of Go routines fascinating.
[748.00 → 753.38] Is there any plans for a package manager, or how would that work, something like a Ruby Gems for Go?
[754.78 → 755.52] I'm sorry.
[755.64 → 758.20] I'm not really an expert on that stuff.
[758.44 → 760.74] So I just don't know.
[760.88 → 763.06] I'd be lying to you if I understood it.
[763.06 → 769.70] But as far as distributing things at the moment, we're trying to keep everything in a Mercurial repository,
[769.70 → 777.98] which we maintain, because we don't really want to deal with packages and so on until things are a little more mature and stable.
[778.60 → 786.60] But I suspect sometime next year there'll be sensible binary downloadable packages about exactly what they're going to look like.
[786.64 → 787.38] Who knows at this point?
[789.04 → 789.98] Is that a reasonable answer?
[790.42 → 791.14] Sure, sure.
[791.14 → 793.22] And I understand it's early in the lifecycle here.
[794.94 → 800.60] It was a natural fit, I would think, to start sharing code with other Go programmers
[800.60 → 803.98] and want to know what kind of plans you had on the roadmap for that.
[805.20 → 806.12] We don't have any plans.
[807.24 → 809.46] We'll evolve them as we need them.
[811.76 → 817.00] You mentioned in there, you mentioned Mercurial as the source code manager.
[817.94 → 819.58] Any reason why Mercurial will ever get?
[819.58 → 822.14] Yeah, a very simple reason.
[822.58 → 824.34] Code.google.com doesn't support Git.
[825.00 → 827.76] So we had a choice of Subversion or Mercurial.
[828.14 → 834.08] The advantage of Mercurial is that it was easy to write a plug-in to implement our code review process,
[834.18 → 836.54] which we wanted to take now.
[837.34 → 841.16] Gillan Possum designed a really nice code review system we use internally,
[841.16 → 847.10] and he's got this sort of rewrite of it for external use on code.google.com called Reader.
[847.60 → 851.22] And all the Go source code that goes into the repository goes through that process.
[851.40 → 852.34] It's a really nice tool.
[852.88 → 854.38] And that was the reason we went to Mercurial.
[854.46 → 856.76] We could make that work with Mercurial.
[856.76 → 857.76] Awesome.
[861.76 → 864.02] So what are the next steps?
[864.10 → 865.52] What's on the immediate roadmap for Go?
[865.52 → 870.80] We have two things we want to do in a big scale.
[870.80 → 874.92] We have to build up the libraries and the implementation both.
[875.86 → 880.06] The libraries are spotty in places just because we haven't written everything we need,
[880.12 → 881.24] and there's lots of stuff to do.
[882.10 → 885.18] And then internally, there's a lot of runtime stuff,
[885.32 → 888.02] particularly around things like memory management, garbage collection, and so on,
[888.52 → 890.58] that really needs a redo.
[890.80 → 894.74] Now that we have the language designed and not that it's all locked down,
[894.82 → 896.28] things are still going to change,
[896.64 → 898.98] but we have a pretty deep idea about how a lot of it works.
[899.34 → 902.90] It's time to go back and revisit some of the concurrency primitives
[902.90 → 905.42] and the garbage collection, things like that,
[905.46 → 908.82] and reimplement them with more performance in mind now that we understand the semantics.
[908.82 → 914.00] Because until we do that, it won't really be competitive as a systems' language.
[914.48 → 917.72] But we think the language is intrinsically capable of being pretty efficient.
[917.96 → 921.08] Some of the benchmarks we have that rely on just raw computation
[921.08 → 925.06] seem to bring it to the sort of C regime for regular C
[925.06 → 928.36] as opposed to hyper-optimized pragmatism C.
[929.34 → 932.12] And then if we get the runtime up another couple of notches,
[932.20 → 938.42] it should be almost as nice to use as, say, Python or Ruby or something like that.
[938.42 → 941.38] But with performance, it's much closer to C or C++,
[941.72 → 943.24] and that's really where we want to get to.
[943.80 → 947.34] As far as language design goes, there are a lot of things we've talked about.
[947.64 → 951.24] We're very careful about features because one of the things about Go
[951.24 → 953.54] that really makes it work, I think,
[953.62 → 957.58] is that language was designed as a set of orthogonal features
[957.58 → 961.08] so that when you put two things together, you know what's going to happen.
[961.08 → 966.26] And it's very important that as we add new features,
[966.42 → 968.88] things like we're talking about union types and things like that,
[969.30 → 972.28] that they work with the existing pieces perfectly
[972.28 → 974.66] so that there are no surprises in how things interact.
[975.24 → 976.98] That's a lesson we've learned from some of the other languages
[976.98 → 977.94] that have grown organically.
[978.10 → 981.94] We tend to have features that don't quite intersect at right angles,
[981.98 → 983.58] and you get weird interactions with things.
[983.68 → 984.90] It's hard to explain what's going on.
[984.94 → 986.10] We want to avoid that very much.
[986.10 → 992.10] One of the things I found amusing from the FAQ was the reason for the name Go,
[992.40 → 994.58] that Ogle would be a good name for a Go debugger.
[995.32 → 996.56] Yeah, that's just a little joke.
[996.70 → 998.76] But there is, in fact, the beginnings of a debugger,
[998.84 → 999.78] and it is called Ogle.
[1000.04 → 1000.66] So there you go.
[1001.48 → 1001.88] Awesome.
[1002.32 → 1002.68] Debugger.
[1003.10 → 1004.00] Can't wait to see that.
[1004.52 → 1007.66] Do we anticipate Microsoft coming out with another language called Logo
[1007.66 → 1009.54] or No or something like that?
[1010.00 → 1011.54] Who knows what Microsoft wants to do?
[1011.54 → 1013.76] I don't think we're on their radar, actually.
[1013.76 → 1016.02] I think they're happy with their common language runtime.
[1016.18 → 1020.44] I would like to see someone try to build a Go backend for the CLR.
[1020.58 → 1025.32] I don't know how some of the type stuff is kind of slippery.
[1025.46 → 1030.68] For instance, it's quite difficult to implement Go's interface model using a JVM.
[1030.92 → 1034.10] You might have to add a byte code to deal with some of the type stuff.
[1035.04 → 1036.68] So for some of these existing systems,
[1036.88 → 1039.44] it's not that obvious how Go would run with them,
[1039.50 → 1042.56] but that doesn't matter for us directly because Go is a compiled language.
[1042.56 → 1044.58] We go right down to the raw metal.
[1045.32 → 1049.30] But for some environments, maybe you want to have something a little more VM-like.
[1050.32 → 1053.48] So for developers looking to kind of join the Go community
[1053.48 → 1055.98] after they go out to golang.org and get up to speed,
[1056.56 → 1057.94] where's the best place to get involved?
[1059.20 → 1060.14] That's the place to do it.
[1060.18 → 1062.96] There's a mailing list called Donuts.
[1063.04 → 1066.16] I think it's called Golang-nuts is the full name on Google Groups.
[1066.16 → 1069.08] There are links at golang.org to that.
[1069.38 → 1070.18] Join the discussion.
[1070.36 → 1070.90] Try it out.
[1072.78 → 1074.68] My experience has been in the last couple of weeks,
[1074.72 → 1076.50] it's been a little bit crazy watching a response,
[1076.64 → 1079.74] which I've got to tell you was much bigger than we expected,
[1079.90 → 1080.68] but that's gratifying.
[1081.10 → 1084.48] The people who've actually tried to use it to write programs seem to like it a lot.
[1085.22 → 1086.66] There are a lot of complainers out there.
[1086.78 → 1087.32] There always are.
[1087.38 → 1089.84] But they seem to be the people who haven't really sat down and tried it.
[1089.84 → 1094.78] And I think that comes back to the point I was making about how the thing is designed.
[1095.86 → 1099.66] It doesn't look very radical, but when you use it,
[1099.72 → 1102.36] you see it actually has a very different take on how things behave.
[1102.70 → 1105.76] And you can't really see that until you've really tried the language out.
[1106.14 → 1108.12] And some of the bloggers I've noticed have picked up on it.
[1108.18 → 1110.66] They sat down to use it, and they think, oh, this is kind of weird.
[1110.68 → 1111.30] Why are they doing that?
[1111.32 → 1113.14] And then they use it for a while, and they say, hey, that's kind of neat.
[1113.58 → 1115.62] So I think people who use it will like it.
[1115.62 → 1119.80] I think there's a lot of room to grow performance-wise.
[1119.98 → 1122.56] Get the libraries up to date.
[1122.82 → 1125.52] And it's still very early, and it's essentially an experiment.
[1125.68 → 1128.60] We want to make sure that that experiment succeeds.
[1128.86 → 1133.62] But we've got a long way to go before it's something you would want to commit your company to or anything like that.
[1134.12 → 1137.46] It's a Skunk Works project, and it's not even an official Google-branded product.
[1137.74 → 1140.88] We're releasing it as a pure open-source thing.
[1140.88 → 1146.60] And I'm actually kind of proud that it went out on day one as an open-source project, completely ready to go.
[1146.80 → 1150.18] And I think that's a really nice way to give something back to the community.
[1150.68 → 1150.86] Right.
[1150.92 → 1153.94] We see Google Chrome OS come out.
[1154.02 → 1155.22] Now we see Chromium OS.
[1155.36 → 1156.68] That started out as a closed-source.
[1156.76 → 1157.44] Now it's open-source.
[1157.56 → 1159.24] Is that what you mean by coming out the gate?
[1159.70 → 1169.72] Yeah, I like to think that because it is really an experiment for everybody to play with, there's really no reason to keep it behind closed doors any longer than you want to.
[1169.72 → 1175.96] I mean, we could have kept it inside for another couple of years and worked on it even more, but it's way more interesting for everybody to get it out there and make it a good idea.
[1175.96 → 1176.28] Absolutely.
[1176.76 → 1176.98] Yeah.
[1177.46 → 1187.60] Well, once you get the community involved, you start to see all brand-new ways of it being used, and you start to see a lot more growth and innovation happening once you start getting the collective involved.
[1187.60 → 1198.56] We see that with collective buying, everything from social networks, the way they work, to collective buying, to crowdsourcing design or crowdsourcing code development.
[1199.26 → 1200.36] Lots of stuff happening.
[1200.54 → 1206.30] And I said there are a couple of ports that have been done to FreeBSD and to Windows and some library work coming in.
[1206.34 → 1207.68] We're getting a lot of interesting contributions.
[1207.94 → 1209.28] So I think it's starting to take off.
[1209.32 → 1209.88] It's pretty exciting.
[1209.88 → 1210.32] Awesome.
[1211.04 → 1221.80] Well, I think the only last question I wanted to probably ping it to real quick is like besides Go and some of the things going on with Google and open source projects involving Google, what's on your radar in terms of open source?
[1222.78 → 1225.48] At the moment, I'm just so overwhelmed by this.
[1225.60 → 1227.58] I don't have anything else on my radar screen at all.
[1228.60 → 1238.40] One of the things I want to do in the next few months is got more Google internal development on Go, and that's going to be an interesting project, but that's not really open source.
[1238.40 → 1246.64] On the outside, I want to see more people use it, get more real production stuff running in the net.
[1246.84 → 1249.26] There are already a few websites that are based on it, which is kind of fun.
[1249.98 → 1253.70] And I think the community will let us know where it's going, and that's really what we want to see.
[1254.30 → 1254.64] Very cool.
[1255.28 → 1257.86] Well, Rob, thanks a lot for coming on the show.
[1257.94 → 1258.58] Really appreciate it.
[1258.60 → 1261.38] We had fun talking to you and can't wait to see what happens with Go.
[1261.92 → 1262.24] Great.
[1262.32 → 1263.26] Thank you very much for having me.
[1263.32 → 1263.60] I enjoyed it.
[1263.62 → 1263.90] Thank you.
[1263.90 → 1263.92] Thank you.
[1268.40 → 1271.46] Thank you for listening to this edition of The Change Log.
[1272.22 → 1276.22] Be sure to tune in weekly for what's fresh and new in open source.
[1277.38 → 1282.28] Also, visit thechangelog.com to follow along, subscribe to the feed, and more.
[1282.48 → 1283.52] Thank you for listening.
[1283.52 → 1284.52] Bye.
[1291.58 → 1292.10] Bye.
[1296.10 → 1296.58] Bye.
[1297.92 → 1298.30] Bye.
[1300.00 → 1302.18] Bye.
[1302.18 → 1304.60] Bye.
[1304.82 → 1305.24] Bye.
[1305.24 → 1307.28] Bye.
[1307.50 → 1309.32] Bye.
[1309.32 → 1309.46] Bye.
[1309.46 → 1309.60] Bye.
[1309.88 → 1310.16] Bye.
[1310.18 → 1310.50] Bye.
[1310.82 → 1311.28] Bye.
[1311.38 → 1313.40] Bye.
