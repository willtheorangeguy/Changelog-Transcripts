[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.74 --> 14.74]  Head to linode.com slash Changelog.
[15.52 --> 18.24]  This episode is brought to you by DigitalOcean.
[18.52 --> 23.08]  DigitalOcean makes it super simple to launch a Kubernetes cluster in minutes.
[23.08 --> 27.28]  The DigitalOcean Kubernetes platform empowers developers to launch their containerized
[27.28 --> 33.06]  applications into a managed production-ready cluster without having to maintain or configure
[33.06 --> 34.38]  the underlying infrastructure.
[34.80 --> 38.98]  They seamlessly integrate everything with the rest of the DigitalOcean stack, including
[38.98 --> 43.90]  load balancers, firewalls, object storage spaces, and block storage volumes.
[44.42 --> 49.10]  They even have built-in support for public and private image registries like Docker Hub
[49.10 --> 50.16]  and Quay.io.
[50.50 --> 55.20]  Developers can now run and scale container-based workloads with ease with the DigitalOcean platform.
[55.20 --> 59.68]  Learn more and get started for free with a $50 credit at do.co slash Changelog.
[59.80 --> 62.98]  Again, do.co slash Changelog.
[77.98 --> 83.36]  Welcome to GoTime, a podcast featuring a diverse panel and special guests discussing cloud
[83.36 --> 87.72]  infrastructure, distributed systems, microservices, Kubernetes, Docker.
[88.16 --> 89.24]  Oh, and also Go.
[89.46 --> 93.04]  We record live every Tuesday at 3 p.m. Eastern, noon Pacific.
[93.46 --> 97.54]  Join the community of Slack with us in real time during the show in the GoTime FM channel
[97.54 --> 98.42]  and go for Slack.
[98.64 --> 99.30]  Follow us on Twitter.
[99.40 --> 100.68]  We're at GoTimeFM.
[100.96 --> 106.20]  Listen live at changelog.com slash live or subscribe at changelog.com slash GoTime.
[106.46 --> 107.64]  And now on to the show.
[107.64 --> 116.24]  Hello and welcome to another exciting episode of GoTime.
[116.44 --> 118.04]  I'm your friendly neighborhood, Matt Ryer.
[118.30 --> 121.20]  And today we're talking about functional programming.
[121.68 --> 125.32]  Yes, a Go podcast talking about functional programming.
[125.56 --> 126.26]  That's right.
[126.62 --> 127.86]  I think it's going to be a great show.
[128.06 --> 131.76]  There's only one way to find out and that's to do it and then listen to it and see if it
[131.76 --> 132.32]  was good or not.
[132.32 --> 138.20]  And joining me to make it good is I'm joined by two of my favorite gophers.
[138.68 --> 141.64]  It's Johnny Borsico and Aaron Schleslinger.
[141.84 --> 143.38]  And welcome, gentlemen.
[143.48 --> 143.86]  How are you?
[144.08 --> 144.54]  Very well.
[144.70 --> 145.76]  Hey, very good.
[145.98 --> 149.42]  Johnny, it's been a while since we hung out on GoTime.
[149.56 --> 150.24]  What have you been up to?
[150.56 --> 151.06]  Yeah, yeah.
[151.08 --> 153.10]  It's been a couple of weeks at least.
[153.60 --> 156.80]  Yeah, I've been doing some teaching, some Go training.
[156.80 --> 163.68]  But what I really enjoyed since I've been off air, so to speak, was a Go Bridge workshop
[163.68 --> 166.54]  that I taught in New York last weekend.
[167.06 --> 170.28]  It was co-organized by some folks at the Go Bridge community.
[170.94 --> 175.70]  But really, the headlifting was done by the Women Who Go chapter in NYC.
[176.34 --> 178.32]  So shout out to the organizers there.
[179.16 --> 180.62]  Jonas is definitely one of them.
[180.76 --> 182.60]  Will can definitely help with that as well.
[182.68 --> 184.48]  So shout out to those folks and its TAs.
[184.48 --> 187.06]  This was really, really well put together.
[187.32 --> 188.16]  The spot was great.
[188.60 --> 189.44]  Everything was well organized.
[189.80 --> 193.30]  And the only thing I did was to show up and teach, which I think was basically just half
[193.30 --> 195.14]  really the battle there.
[195.74 --> 197.42]  But yeah, it went really well.
[197.56 --> 198.42]  Folks learned a ton.
[198.70 --> 200.34]  And I had a blast teaching it.
[200.66 --> 200.82]  Brilliant.
[201.40 --> 202.86]  Who is Go Bridge for?
[203.70 --> 208.24]  And so if any listeners are interested in getting involved, how can they either contribute
[208.24 --> 209.48]  or just take part in it?
[209.48 --> 214.52]  Its core mission is diversity and inclusion within the Go community specifically.
[215.04 --> 219.44]  So basically, we're open to all underrepresented groups within the community.
[219.70 --> 224.76]  So one of the ways we do that is by basically having those free workshops basically that target
[224.76 --> 225.28]  those individuals.
[225.68 --> 227.52]  And basically, they come in for the day.
[227.60 --> 230.76]  Or if it's a two-day workshop, they come in for Saturday and Sunday typically.
[230.76 --> 235.72]  And we usually have TAs, community members that give up some time.
[236.20 --> 237.12]  And we have people teaching.
[237.72 --> 244.02]  And really, it's a community effort to sort of help address the lack of diversity and
[244.02 --> 245.04]  inclusion in the community.
[245.20 --> 248.90]  I think either organize a workshop yourself or teach or TA.
[249.12 --> 251.92]  You can always donate money to the Bridge Foundry organization.
[252.10 --> 253.50]  And that money will find its way to us.
[253.98 --> 258.60]  And yeah, it helps us with offering diversity scholarships to some of the conferences that you
[258.60 --> 260.34]  know and love, Go4Con included.
[261.14 --> 262.56]  And yeah, there's lots of ways to help.
[262.80 --> 265.90]  Really, if you have any questions about it at all, feel free to reach out to me directly
[265.90 --> 270.06]  on Twitter or reach out on support.gobridge.org.
[270.66 --> 270.90]  Brilliant.
[271.00 --> 271.80]  What's your Twitter name?
[272.54 --> 274.22]  My Twitter handle is jborsico.
[274.40 --> 277.62]  So J-B-O-U-R-S-I-Q-U-O-T.
[278.18 --> 278.54]  Awesome.
[279.10 --> 279.66]  Yeah, that's great.
[279.66 --> 286.38]  What I love about this, of course, is diversity on teams makes the teams better, in my experience.
[286.38 --> 291.14]  So whatever that diversity looks like, and actually the more diverse, the better, because
[291.14 --> 296.54]  you just never know what different experiences are going to influence things.
[296.90 --> 298.78]  And so a nice broad range.
[298.88 --> 303.94]  That's why I think GoBridge is doing such an important thing for the community and for
[303.94 --> 304.54]  our teams.
[305.04 --> 305.70]  Yeah, I totally agree.
[305.78 --> 311.36]  And I think there's been tons of sort of articles and research and things that have come out
[311.36 --> 314.98]  that basically have shown, have proven that it makes business sense, right?
[314.98 --> 318.94]  To have diverse teams within your organization, within your company, and within the community
[318.94 --> 319.42]  overall.
[319.68 --> 321.12]  So I think it's a win-win for everybody.
[321.70 --> 322.26]  Yeah, it's brilliant.
[322.96 --> 326.90]  Also joining us today, joining us again from last week, Aaron.
[327.06 --> 330.00]  Aaron, is it Aaron or Aaron when I pronounce your name?
[330.46 --> 331.56]  Or is there no difference to you?
[331.82 --> 333.06]  No, no difference to me.
[333.24 --> 333.72]  Not really.
[334.10 --> 335.18]  The last name, though.
[335.26 --> 336.04]  But Schleslinger.
[336.04 --> 337.72]  Yeah, let's talk about the last name, though.
[337.72 --> 338.26]  Let's talk about it.
[338.36 --> 341.38]  You put another L in there again.
[342.00 --> 342.96]  Oh, Schleslinger.
[342.96 --> 343.24]  Schleslinger.
[343.44 --> 344.56]  Yeah, there you go.
[345.14 --> 345.66]  Schleslinger.
[346.16 --> 346.32]  Yeah.
[346.42 --> 347.88]  Oh, that's okay.
[348.38 --> 349.04]  Sorry, mate.
[349.10 --> 349.64]  You said it.
[349.72 --> 350.32]  No worries.
[350.44 --> 352.12]  You said it just fine the first time.
[352.38 --> 353.18]  I'm used to it.
[353.32 --> 357.24]  We'll edit it out so that in the podcast I sound like I got it correct.
[357.62 --> 358.48]  No worries.
[360.24 --> 362.16]  So what have you been up to since last week?
[362.62 --> 366.30]  So yeah, I've been doing a bunch of Athens stuff.
[366.30 --> 370.24]  I've been teaching a bit, too, the topic of Athens.
[371.02 --> 376.90]  And yeah, I've been writing some TypeScript stuff, too, which has been kind of a refreshing
[376.90 --> 380.64]  pause from Go because it's totally different.
[380.64 --> 389.24]  It has classes and objects and generics and all the things that Go doesn't.
[389.50 --> 392.98]  And it takes a completely different approach from Go.
[393.12 --> 397.54]  So it's been kind of cool to compare it in my mind interactively.
[398.38 --> 398.68]  Hmm.
[399.16 --> 399.88]  Very interesting.
[400.04 --> 404.80]  And maybe we'll get to talk a bit more about TypeScript as we discuss functional programming.
[404.80 --> 410.64]  So just a complete disclaimer, I don't know much about functional programming at all.
[410.70 --> 414.58]  It's not something that I've really had the time to properly dig into.
[414.72 --> 417.62]  I've got a sort of general enough idea about it.
[417.78 --> 423.64]  But I'm going to act like the noob, the audience member who doesn't really know what it's for.
[424.00 --> 427.44]  And there's a lot of tech wars all the time on Twitter.
[427.58 --> 431.72]  It's very common, you're right, to say, oh, you know, which do you prefer, Go or Rust?
[431.96 --> 433.54]  It's a very common thing you hear a lot.
[433.54 --> 441.00]  And really, the question's kind of flawed because it's more about, well, there's lots of other things that I think would lead you to choose a language.
[442.00 --> 444.62]  What the sort of problem space you're dealing with is one of them.
[444.70 --> 447.42]  But actually, even just sort of developer happiness.
[447.42 --> 455.06]  I think if a developer is going to work on something, they should pick the language that they're going to be most productive in, you know, the development team.
[455.42 --> 457.28]  I think that's also an important thing.
[457.28 --> 460.88]  But so functional programming is going to be somewhat new to me.
[461.04 --> 464.10]  And I'm keen to learn as much as I can about it.
[464.60 --> 466.94]  And so, yeah, why don't we kick off then, Aaron?
[467.04 --> 469.00]  You could perhaps give us a little bit of an intro.
[469.50 --> 474.86]  So for somebody who's never even heard of functional programming, how would you describe what it is?
[474.86 --> 475.78]  Yeah.
[476.20 --> 484.30]  Usually there's like a really simple, frustrating answer to that and then a crazy complicated, also frustrating answer.
[484.72 --> 490.64]  So I'll try to kind of hit the middle ground there so that it's not frustrating.
[490.64 --> 496.52]  So, yeah, I mean, first and foremost, functional programming can be anywhere.
[496.84 --> 499.52]  It doesn't just have to be in some of those hardcore languages.
[500.56 --> 504.54]  And it's as the name kind of implies, it's all about functions.
[505.26 --> 510.38]  You know, obviously you write functions, but also you use functions in new ways.
[510.58 --> 514.32]  You can pass functions into other functions.
[515.22 --> 518.88]  You can nest functions inside of other functions.
[518.88 --> 522.44]  You can do this thing called composing functions.
[522.96 --> 524.86]  You can return functions.
[526.12 --> 531.74]  And this is all kind of familiar to Go because functions are first class citizens there.
[532.50 --> 543.10]  So really, in the Go context, functional programming is just another kind of strategy to pick up and use it appropriately.
[543.10 --> 551.56]  It's really interesting to hear you say that the first point you made was that you can do functional programming anywhere, even in Go.
[551.96 --> 552.32]  Yeah.
[552.44 --> 559.32]  I mean, I won't say everywhere, but, you know, 99% of the places you write code, you could do it.
[559.42 --> 559.66]  Yeah.
[559.68 --> 560.40]  Including Go.
[560.78 --> 562.06]  Don't let anyone tell you otherwise.
[562.94 --> 563.22]  Right.
[563.22 --> 565.10]  Is it more like a set of rules then?
[565.82 --> 566.06]  Yeah.
[566.06 --> 573.32]  It's kind of half set of rules and strategies and maybe the other half you could say design pattern.
[573.72 --> 577.12]  I know that's a loaded word, but sort of design pattern.
[577.70 --> 578.76]  So what are some of the rules then?
[578.96 --> 586.22]  Because I know that, for example, I know that if you should get the same output when you put the same input in.
[586.22 --> 592.90]  Yeah, that's a rule you can take and sort of apply to some parts of your code in Go.
[593.60 --> 595.46]  That's called pure purity.
[595.78 --> 603.10]  So a pure function would be a function that always returns, like you said, the same thing for the same input.
[604.00 --> 608.76]  And that means usually that, you know, it can't do IO.
[609.20 --> 611.62]  So that's super, super limiting, obviously.
[611.62 --> 620.24]  But it's also really powerful if you put it into parts of your code, because you can kind of reason about it super easily.
[620.50 --> 622.74]  And you can write tests super easily for it, too.
[623.62 --> 630.52]  It sounds like, from what we're saying, it's a set of principles and strategies that you employ.
[630.98 --> 639.58]  But also, one could argue that basically the underlying technology, right, the programming language does a lot to sort of help or facilitate that, right?
[639.58 --> 650.74]  So I would imagine that writing functional in something like Scala or Haskell is going to feel vastly different than basically doing it in Go, which wasn't really designed for that.
[650.88 --> 651.88]  Would you agree is there?
[652.00 --> 653.06]  What don't we know there?
[653.68 --> 654.30]  I would agree.
[654.64 --> 658.94]  There are languages, like you said, you know, Haskell is probably the prime example.
[658.94 --> 671.50]  Those languages are designed for functional programming, and they just don't let you do the so-called imperative programming, the opposite of functional programming.
[672.40 --> 677.76]  So learning something like that, you just have to completely relearn programming almost.
[678.38 --> 683.06]  But then on the other side of the coin, you know, if you're going into Go, there are limitations there.
[683.06 --> 687.84]  And in Go's case, one of the big limitations is lack of generics.
[688.58 --> 693.86]  There are some things you can't do in the functional programming world with Go.
[694.14 --> 699.74]  So there's a middle ground to strike kind of everywhere because Go has its strengths.
[700.10 --> 711.64]  And if you were to take like 100% of the functional concepts and build them into Go, you would lose a lot of the sort of Go strengths that we all know and love.
[711.64 --> 712.12]  Hmm.
[712.60 --> 722.34]  So you're definitely not advocating that if the things that you can do in Go that are functional, that they should sort of replace the way you do Go, right?
[722.38 --> 726.44]  The idiomatic Go, the imperative style, right, of doing Go.
[726.52 --> 729.04]  You're not going to get the most bang for the buck there.
[729.22 --> 733.32]  So if you really want functional, you should use a functional language, right?
[733.62 --> 738.02]  Yeah, I'm certainly not advocating in the Go case to just dump everything you know.
[738.48 --> 740.78]  In some cases, that would be impossible anyway.
[740.78 --> 747.98]  But for the Go world, it's all about kind of just identifying when a functional pattern would help.
[748.48 --> 753.28]  And in most cases, would like reduce the amount of code you have to write and then doing it.
[753.56 --> 761.70]  And if you do, like you said, if you want to go hardcore, then, you know, go pick up Haskell or Scala or even Rust.
[761.70 --> 772.10]  Those are the kind of languages where you really can dive in and go like super, super hardcore and like, you know, rack your brain and relearn everything.
[772.58 --> 773.70]  And that's cool.
[773.70 --> 781.56]  But if you're a gopher and you want to stick with Go, that's really what it's about is just identifying when the pattern would help.
[781.56 --> 787.48]  And then going forward and implementing it just in that one part of the code.
[787.86 --> 788.26]  That's brilliant.
[788.38 --> 792.66]  Oh, now, remember, people listening live can join in on gopher Slack.
[792.84 --> 795.28]  We're in the hash GoTimeFM channel.
[796.00 --> 798.48]  And there's some gophers in there already asking some questions.
[799.16 --> 805.04]  And what are some domains or problems where functional programming, where programming is a good choice and a good strategy?
[805.78 --> 811.04]  And Barnaby Salter asks, is it only for mathematical or scientific disciplines?
[811.58 --> 818.26]  So, Aaron, could you tell us a bit about what sorts of problems functional programming is good at and perfectly targeted for?
[818.62 --> 822.70]  Yeah, I mean, in the Go space, it's definitely not just for math and science.
[823.16 --> 832.94]  You know, that being said, if you go on Wikipedia and you look up some mathematical strategy, a lot of times, you know, you can literally translate one of the proofs into Go and it'll look functional.
[832.94 --> 842.42]  But domain problem wise, you know, in addition to math and science, if you look at something like config parsing, let's take that as an example.
[843.24 --> 851.06]  It'll almost all the time, like you're going to get back out the same thing if you give it the same exact config file.
[851.52 --> 853.84]  And I know, like before, I said you shouldn't do IO.
[853.84 --> 861.94]  But if you think about config parsing, you can give it a string that represents, you know, YAML or TOML or whatever it might be.
[862.22 --> 864.56]  And it'll give you back the exact same struct.
[864.92 --> 867.08]  And that's really powerful, right?
[867.08 --> 873.70]  Because you can always rely on your config parsing code to give you back the same config.
[873.70 --> 879.60]  And right there, that's super simple in terms of like what we already know and go.
[880.14 --> 882.48]  But that actually is a functional principle.
[883.00 --> 886.04]  And that's, you know, that's starting simple, but goes on from there.
[886.70 --> 892.28]  It would be weird if it wasn't the case where you put the same input in, you know what I mean?
[892.28 --> 896.94]  Like if you've got different output with the same input, you'd probably consider that a bug.
[896.94 --> 904.94]  But what about things like if the config was, if there was a time in there and it was setting a default value to the current time?
[905.46 --> 907.24]  Or actually the current time at all.
[907.34 --> 910.68]  How is the current time even thought about in functional programming?
[911.08 --> 911.22]  Yep.
[911.36 --> 913.58]  And that's, of course, yeah, that's an exception.
[914.30 --> 918.12]  And that sort of touches on, you know, when do you depart from functional?
[918.26 --> 925.88]  When do you know, like, this is too hardcore and we shouldn't deal with the purity example.
[925.88 --> 928.82]  But there is a way to get around that.
[929.28 --> 941.02]  And there is a way to parse a config file so that it instead of returning or setting the current time in one of the struct fields, it puts a function instead in that struct field.
[941.34 --> 948.02]  So you always get back a function and then you can decide when to go ahead and call that function later on.
[948.02 --> 955.30]  And then that specific function becomes an impure function, of course, because it always gives back something different.
[955.88 --> 964.04]  But overall, when you're managing that config struct, you always have the same thing that you're looking at and dealing with when you pass it all around your code.
[964.04 --> 981.36]  So sort of one of the major benefits that, like, I immediately picked up when I started looking at sort of functional programming in Go was the judicious use of basically passing around and receiving or returning functions.
[981.36 --> 988.44]  You could tell right away that basically there's a heavy emphasis, right, on obviously it's functional for a reason, right?
[988.46 --> 993.12]  So basically passing functions, just like you're saying, like basically being able to return functions that you can then call on.
[993.12 --> 1000.74]  So the Go's treatment of functions as sort of first class citizens absolutely makes that possible.
[1001.28 --> 1010.74]  But I actually watched a talk by you actually at Gotham Go, it might have been this year, last year, probably last year, on sort of functional programming in Go.
[1010.84 --> 1019.90]  And one of the things that you talked about was basically the use of how higher order functions make that whole sort of notion possible.
[1019.90 --> 1037.64]  So if there's one thing a Gopher could take away from thinking about functional programming, would you say sort of using higher order functions, basically the taking in or returning of functions to do things, would that be sort of a major takeaway?
[1037.64 --> 1052.68]  Because I'll be honest, that's something I don't see a ton of, usually in the more sort of complex cases where, you know, people who really know Go, who really know what they're doing, you can see a bit more of that.
[1052.76 --> 1054.74]  But I don't see that in everyday Go code.
[1055.28 --> 1061.56]  But when I saw your talk, I was like, wow, this is a natural way of thinking.
[1061.56 --> 1062.64]  You can do more of that.
[1062.78 --> 1067.64]  So is that a good way of thinking about it if you're a Go programmer who's not used to doing that?
[1067.76 --> 1069.66]  Is that the first big takeaway you could have?
[1070.68 --> 1071.12]  100%.
[1071.12 --> 1071.64]  Yeah.
[1072.36 --> 1075.74]  And I'll even give like a super, super common example.
[1076.32 --> 1087.62]  If you're writing an HTTP server and you've got a global database variable, that's super, I mean, that's fine because that database variable is going to be sitting there probably for the whole life of your program.
[1087.62 --> 1097.32]  But on the other hand, you could pass a database variable as a parameter to a function that then returns an HTTP handler.
[1098.38 --> 1109.22]  And then testability gets a little bit simpler because you can test each handler with a different database driver or an in-memory driver or something along those lines.
[1109.22 --> 1120.88]  So you're passing in something to a function, receiving a function, and that function itself is the HTTP handler that you can then plug into whatever router you're interested in using.
[1121.88 --> 1126.56]  And that right there is, you know, you're passing in a thing, you're getting back a function.
[1127.30 --> 1132.24]  And right there, that's a functional pattern because, you know, it's like you said, it's a higher order function.
[1132.24 --> 1137.36]  And it talks a bit about not having side effects as well to calling a function.
[1138.10 --> 1139.68]  And Johnny, you touched on this a little bit.
[1139.84 --> 1146.14]  And there's some principles there that I think we already have started to talk about in Go.
[1146.34 --> 1152.72]  For example, when you, I like the idea of no unexpected side effects because it's magic.
[1152.72 --> 1164.02]  So, for example, currently in the images package in the standard library, if you import the JPEG package and you just do like an underscore import, you're not going to use them.
[1164.38 --> 1172.12]  But just by importing them, they then register themselves and you then can add support for JPEGs or PNGs or whatever you import.
[1172.60 --> 1180.38]  Now, I assume that was a early in the standard library's kind of history that they were playing around with ideas like that.
[1180.38 --> 1185.18]  Generally speaking, I personally don't think that's great because it's too magic.
[1185.40 --> 1189.38]  When you import something, I want to import it and then use it explicitly.
[1189.62 --> 1190.88]  I don't want it to be implicit.
[1191.66 --> 1198.18]  So there's probably some of the thinking as well that you could apply in parts outside even just the functions within Go.
[1198.82 --> 1200.70]  Yeah, you hit it on the head.
[1200.92 --> 1205.10]  I think the data, a lot of the standard library database stuff does that too.
[1205.26 --> 1207.92]  Kind of just like you got to remember to do it.
[1207.92 --> 1210.58]  And if you don't, you'll crash at runtime.
[1211.62 --> 1215.50]  You'll panic that the MySQL driver isn't registered.
[1216.18 --> 1218.62]  And, you know, that's like you said, it's shared state.
[1219.22 --> 1226.40]  And another option then to go and replace that is I think we all kind of know and love the builder pattern.
[1226.40 --> 1239.88]  And that is also a functional concept because if you were to go and say like db.withdriver MySQL, maybe you pass in a string MySQL or something like that.
[1240.20 --> 1246.34]  And db.withdriver returned itself a database driver that implemented MySQL.
[1246.34 --> 1250.72]  Right there, that's also a pure side effect free function.
[1251.10 --> 1255.34]  And it returns kind of itself so that you can chain those things together.
[1255.72 --> 1258.78]  And you can say, you know, .withdriver, .connect.
[1259.36 --> 1261.08]  Maybe you pass in the host string.
[1261.08 --> 1267.20]  And then .query or .query builder or whatever that might be.
[1267.72 --> 1276.52]  When you start seeing sort of those registration patterns happen explicitly in a function, then you start seeing those functions chaining together.
[1276.52 --> 1282.06]  Basically, you're doing the builder pattern, but you're taking advantage of those pure functions.
[1282.86 --> 1289.46]  And you start to do things that start to look like some other functional patterns that we kind of haven't gotten to.
[1290.04 --> 1298.20]  But they're like maybe functional programming 102 style patterns, which start to get you some really, really powerful code.
[1298.20 --> 1309.66]  Yeah, append springs to mind as one that you might consider pure in the sense of like, you know, we always assign back to the slice or to a new slice.
[1309.80 --> 1311.82]  Essentially, it returns a new slice.
[1312.66 --> 1316.22]  Although, of course, it can affect the underlying array.
[1316.48 --> 1318.54]  So I guess there are some times when it's not pure.
[1318.64 --> 1319.06]  Is that right?
[1319.46 --> 1319.68]  Yeah.
[1320.06 --> 1320.28]  Yeah.
[1320.28 --> 1326.58]  So there's kind of this concept of observable purity and interface purity.
[1326.58 --> 1338.62]  And when you talk about a language like Go, you probably want to be pure in that you don't modify the underlying slice, the underlying array, because there might be another Go routine touching it.
[1338.62 --> 1355.54]  But append is always interface pure because it'll always return the new array instead of from your perspective in your Go routine, you know, just modifying the underlying thing and then, you know, making you just start using that same variable.
[1355.54 --> 1355.58]  Cool.
[1356.02 --> 1366.16]  It's a really cool pattern in terms of you using append because you always know that the thing that append returns is the new one that you have the new value on.
[1366.16 --> 1366.44]  Yeah.
[1366.44 --> 1367.00]  Yeah.
[1367.00 --> 1375.18]  I quite like it because also it makes it very easy to branch things off to sort of set up some commonality.
[1375.52 --> 1390.80]  And then, right, you'd be able to then, whether it's literally branching it or at least logically, you'd be able to think of you could pass that thing, whatever the new thing is, into some other place and keep a reference to one of the ancestors almost in order to sort of keep it.
[1390.80 --> 1391.92]  I've not explained that very well.
[1392.42 --> 1393.54]  But don't worry.
[1393.92 --> 1395.20]  They'll fix it in post.
[1395.70 --> 1398.98]  I'll just say loads of words and then they can put them together in the right order.
[1399.30 --> 1399.56]  Yeah.
[1399.82 --> 1404.40]  That was, you know, 95% the right order, I think.
[1404.84 --> 1405.64]  Yeah, 95%.
[1405.64 --> 1406.22]  I'll take it.
[1406.70 --> 1406.96]  Yeah.
[1407.38 --> 1409.74]  Well, an interesting word that you said there is branch.
[1409.74 --> 1418.62]  And you can actually make trees, binary trees, that are almost purely functional based on append.
[1419.10 --> 1427.26]  So if you're really into something like that, you know, you can basically create a new tree, a copy of the old tree using append.
[1427.76 --> 1435.82]  So, you know, you can have tree one and you can add a new child node or a new leaf node or I forgot almost everything about trees.
[1435.82 --> 1438.52]  But I know there's a way to represent them in slices.
[1438.86 --> 1446.20]  And if you do an append, you can just create a copy of your tree number one and get a tree number two out of it.
[1446.52 --> 1456.58]  And it's kind of like the non-pure part of the append function actually helps there because it's a really fast operation then to create a new tree.
[1465.82 --> 1468.96]  This episode is brought to you by StrongDM.
[1469.28 --> 1477.56]  StrongDM makes it easy for DevOps to enforce the controls InfoSec teams require, manage access to any database, server, and any environment.
[1478.04 --> 1481.56]  And in this segment, we're talking to Jim Mortco, VP of Engineering at Hearst.
[1481.72 --> 1486.18]  He's sharing how they're using StrongDM within their team of 90 plus engineers.
[1486.46 --> 1491.46]  It now takes them just 60 seconds to off-board a team member from a data source.
[1491.46 --> 1495.28]  We have an engineering team of somewhere in the area of 80 or 90 engineers.
[1495.76 --> 1502.42]  Because we've got so many services and many databases and so many developers, we need a reasonable way to manage access to them.
[1502.86 --> 1506.44]  It was a somewhat painful and, you know, labor-intensive process.
[1507.12 --> 1512.84]  Our DevOps team would literally have to manage every one of the permissions for everybody who wanted access.
[1513.64 --> 1516.48]  So StrongDM has been a real godsend in that area for us.
[1516.84 --> 1520.32]  Requests for access to specific databases were pretty much manual.
[1520.32 --> 1521.92]  Now we've adopted StrongDM.
[1522.12 --> 1524.14]  It's something that you don't even know is there.
[1524.28 --> 1525.70]  Once it's installed, it just works.
[1525.80 --> 1526.40]  It's very simple.
[1526.70 --> 1532.68]  We've set up a multitude of data sources so that when somebody's onboarded, we just give them access to StrongDM.
[1532.96 --> 1533.78]  It's pretty simple.
[1534.18 --> 1540.44]  Our DevOps team, they have a very minimal effort required to enable each data source to be connected to StrongDM.
[1540.74 --> 1544.30]  And then installing the client software is very, very simple and straightforward.
[1544.54 --> 1546.86]  You can use whatever client you want to to talk to the database.
[1547.02 --> 1548.46]  So there's really no training necessary.
[1548.46 --> 1549.28]  All right.
[1549.32 --> 1558.84]  If your team can benefit from nearly instant onboarding and offboarding that's fully SOC 2 compliant, head to StrongDM.com to learn more and request a free demo.
[1559.20 --> 1561.24]  Again, StrongDM.com.
[1561.24 --> 1568.78]  StrongDM.com.
[1570.78 --> 1584.96]  I had this impression of functional, like my, like in my early years, you know, as an engineer, like I'd always hear of functional programming and always had this air of sort of superiority around it.
[1584.96 --> 1597.54]  Like, you know, like only those who had mastered, you know, the unknowns went to the mountaintop and came back with a tablet, you know, kind of thing, like had sort of could understand even approach functional.
[1597.72 --> 1600.50]  It's almost like you had to be sort of a it was like the next level.
[1600.56 --> 1602.94]  It was the evolution of the coder.
[1603.02 --> 1603.22]  Right.
[1603.32 --> 1609.62]  You know, once you once you've evolved beyond the mere mortal imperative style, then you could do functional.
[1609.82 --> 1610.00]  Right.
[1610.00 --> 1619.24]  So like my functional experience is limited to a little bit of Elixir that I started learning because I used to do Ruby and that became very popular in that community.
[1619.24 --> 1639.06]  But to me, like I'm always wondering, like, OK, it always feels like we're always trying to sort of sort of bring functional concepts into the imperative style, basically saying, hey, you can make your imperative programming sort of more stable, more resilient, you know, by sort of adopting some of the principles of functional programming.
[1639.06 --> 1648.34]  But I'm curious, given your background, have you come across situations in the functional community where you're kind of doing the reverse?
[1648.50 --> 1650.96]  Right. You're bringing some of the good ideas.
[1650.96 --> 1652.80]  Right. That exists in the imperative world.
[1652.88 --> 1654.64]  You bring those to the functional world.
[1654.82 --> 1657.30]  And then I'm asking because I really have no idea what those would be.
[1658.00 --> 1658.78]  Oh, yeah, totally.
[1659.12 --> 1664.50]  I mean, like to address the first thing you said, there is totally a religious war.
[1664.50 --> 1667.18]  I think, Matt, you said it kind of at the beginning, too.
[1667.60 --> 1672.06]  And the functional purists are, you know, kind of at the mountaintop.
[1672.24 --> 1675.20]  And a lot of times it's tough to break in.
[1675.58 --> 1678.00]  Even if you go on Wikipedia, there's all this math.
[1678.68 --> 1680.12]  And it's crazy.
[1680.28 --> 1684.06]  Like if you're looking at a math proof and you're like, how does this relate to programming?
[1684.56 --> 1690.94]  But some of the stuff like, for example, there's this concept of mapping over an array.
[1690.94 --> 1698.58]  And mapping over an array, I think someone even said in here, yeah, Barnaby said just remove four in the channel.
[1699.26 --> 1705.88]  Mapping over an array actually just lets you do a for loop without having to write all the for stuff.
[1706.46 --> 1710.28]  You know, you don't have to write for I in range or anything like that.
[1710.28 --> 1722.36]  Instead, you can just do my array dot map and then pass in basically a callback function that the map function will just run for you on every element of the array.
[1722.92 --> 1724.10]  I was thinking, is that a funk door?
[1724.60 --> 1725.08]  Oh, yeah.
[1725.16 --> 1728.66]  But but when you use that word, people start walking away.
[1728.88 --> 1729.86]  In my experience.
[1730.52 --> 1730.82]  No, no.
[1730.88 --> 1733.42]  The only reason I can say that is that because I watch your talk.
[1733.54 --> 1734.32]  Oh, yeah.
[1734.68 --> 1737.48]  I'll mention that word and I'll make me sound like I know what I'm talking about.
[1737.54 --> 1738.42]  Yes, that was that was my.
[1738.42 --> 1739.06]  Oh, yeah.
[1739.06 --> 1742.20]  So you're at the mountaintop then already.
[1742.56 --> 1745.90]  Yeah, I gleaned and it was shining way too bright for me.
[1745.98 --> 1747.10]  It almost burned my eyes out.
[1747.14 --> 1747.98]  So I had to come back down.
[1748.46 --> 1757.36]  I was just going to say, I mean, I learned that world from the Scala days and there were like a bunch of functional, crazy functional libraries in there.
[1757.60 --> 1760.48]  And I like racked my brain trying to figure those out.
[1760.72 --> 1764.30]  And I picked up like functor and like two other words.
[1764.30 --> 1771.66]  And then when I came over to go, I kind of realized like, hey, like this isn't really crazy.
[1772.14 --> 1774.34]  Like you don't have to call it something crazy.
[1774.68 --> 1776.42]  You just see it in the wild.
[1776.70 --> 1779.62]  And people just say, you know, this is a callback and that's it.
[1779.62 --> 1782.78]  Well, we like to use big words for simple things.
[1783.26 --> 1783.82]  Functor.
[1783.98 --> 1788.58]  Functor sounds to me like a kind of go supervillain would be called functor.
[1790.62 --> 1792.02]  It's like super funk.
[1792.12 --> 1792.44]  Yeah.
[1792.58 --> 1793.26]  And functor.
[1793.26 --> 1793.42]  Functor.
[1795.02 --> 1797.54]  Can we get some action figures for those too?
[1799.54 --> 1800.18]  Yes.
[1800.50 --> 1802.86]  I'm sure Ashley can design some for us.
[1803.10 --> 1804.10]  Ashley, if you're listening.
[1805.44 --> 1806.00]  Functor.
[1806.58 --> 1807.18]  Go.
[1808.14 --> 1808.48]  Yeah.
[1808.62 --> 1820.44]  So whenever I hear anyone, whenever there's this kind of snobbery around something, usually it ends up being, it's either inaccessible for some reason.
[1820.44 --> 1824.90]  And I don't usually believe that the reasons are usually that valid.
[1825.38 --> 1829.50]  But one question this leads me to is, how about readability?
[1829.84 --> 1834.18]  Is one of the reasons why functional programming has this elevated status?
[1834.18 --> 1838.02]  Is it because when you read it, it's difficult to read?
[1838.32 --> 1845.34]  Because I've read some functional code and it certainly doesn't spring out to me like GoCode does.
[1845.34 --> 1852.00]  GoCode has a very good glanceability because, you know, it doesn't have much magic in there.
[1852.32 --> 1855.70]  Technically, functional programming should be even less magic, I would assume.
[1856.26 --> 1864.82]  But when I've seen some bits put together, it's a little bit like, you know, you used to get these programmers that were very happy when they could cram all this program onto a single line.
[1865.50 --> 1866.70]  They get very proud of that.
[1866.70 --> 1875.10]  Whereas I always tell people in Go, just be more verbose, break it out onto many lines because it's just so much easier to read.
[1875.48 --> 1878.12]  How's the readability of functional programming code?
[1878.80 --> 1881.26]  Yeah, I mean, it really depends on the language.
[1881.26 --> 1896.74]  And in Go, Go has this kind of asset that it really is so simple that if you wanted to make some crazy functional concept or construct, you really would be forced to break it out onto separate lines.
[1897.38 --> 1900.92]  And even like naming the variables makes a difference there too.
[1900.92 --> 1912.66]  So if you, I would bet that the chances of you creating meaningful variable names would go up if you're going to end up having to break stuff out onto new lines.
[1913.08 --> 1916.04]  And even that makes a difference, right?
[1916.10 --> 1927.04]  It's just like now I can tell what's going on because instead of I, it's like, you know, my new array with added integers or whatever it might be.
[1927.04 --> 1927.64]  Hmm.
[1928.18 --> 1931.22]  But you can kind of go on the other side of that coin.
[1931.76 --> 1942.14]  And like even in Go, if you've got a query builder for SQL queries, like I said before, I mean, that technically is a functional concept.
[1942.46 --> 1948.68]  But you can build up some super crazy queries and have like 10 function calls chained together in a row.
[1949.32 --> 1956.58]  And that can get kind of confusing because you can go and say, you know, okay, I'm doing, I'm starting off with this select.
[1957.04 --> 1960.36]  And then like somehow I'm doing a join and a filter.
[1960.36 --> 1970.88]  And like after a couple of function calls, at least to me, like I can't really imagine what the actual query is going to be that runs against the database.
[1971.10 --> 1979.30]  It's like there's an inflection point where at some point you're going to be calling like five or six chain functions.
[1980.18 --> 1981.78]  And at that point you're like, wait, what?
[1981.98 --> 1983.68]  Like what, what am I trying to do again?
[1983.68 --> 1987.12]  And that's probably where, you know, you start breaking it out.
[1987.32 --> 1999.88]  Those variable names and maybe some docs are going to start making like your, your future self and all your, all the people on your team making their lives easier.
[1999.88 --> 2005.64]  And, you know, making them not want to come hunt you down and, you know, do something to you.
[2005.64 --> 2009.74]  That's how Funk tore actually, that's his origin story.
[2009.86 --> 2010.64]  Yep, exactly.
[2011.10 --> 2016.34]  Did some bad code and the rest of the team hunted him down and I don't, I don't spoil it.
[2016.60 --> 2019.28]  I don't know how far we can take this one.
[2019.88 --> 2020.08]  Yeah.
[2020.22 --> 2021.76]  Well, I think all the way to Netflix.
[2022.70 --> 2023.00]  Yeah.
[2023.38 --> 2023.62]  Yeah.
[2023.86 --> 2024.56]  Netflix original.
[2024.88 --> 2025.06]  Yeah.
[2025.16 --> 2025.84]  Let's make it happen.
[2026.00 --> 2026.58]  Let's do it.
[2026.58 --> 2027.14]  Yeah.
[2028.14 --> 2030.20]  So what about testing then?
[2030.36 --> 2039.06]  So I imagine if, if, if you have these pure functions where the input, whatever the input is, the output is always the same as one of the rules.
[2039.42 --> 2042.32]  I imagine writing tests does get easier.
[2042.32 --> 2046.22]  And can you do a lot more table driven tests and things like that?
[2046.30 --> 2049.66]  Does that just completely make sense now in that, in that world?
[2050.28 --> 2051.00]  Yeah, for sure.
[2051.00 --> 2058.62]  Take, for example, the, the whole pass in the database param and get back a HTTP handler example.
[2059.34 --> 2066.12]  You know, let's say you did a table driven test that had, you know, a bunch of tests against a specific route.
[2066.40 --> 2073.46]  You could, in theory, take out the HTTP server, like, you know, HTTP test dot test server.
[2073.84 --> 2075.10]  I think that's what it's called.
[2075.10 --> 2086.52]  You could save that for kind of an integration test and you could actually go and start passing in in-memory databases and then just calling the handler directly.
[2087.06 --> 2097.94]  And you get these super, super fast and efficient unit tests out of that, that really, really target your every single HTTP handler that you write.
[2097.94 --> 2106.18]  And then, like, you can even build on top of that and start writing your table driven tests against different types of databases, too.
[2106.72 --> 2113.94]  So, you know, an example there that I've seen a bunch is you've got your quick tests that run against memory databases.
[2114.28 --> 2119.34]  And then you've got a little bit slower tests that run against SQLite.
[2119.52 --> 2123.54]  And they will actually literally test your SQL queries out.
[2123.54 --> 2128.18]  Then you can start testing, like, query injection and all that crazy awesome stuff, too.
[2128.88 --> 2142.40]  So the imperative gopher in me, I guess, is basically saying what would be the advantage of using functional here instead of basically like a good using interfaces, right, to mock out some of this behavior.
[2142.94 --> 2150.78]  Does one offer a much greater advantage over the other or it really is you can pick whichever one makes you more productive kind of thing?
[2150.78 --> 2153.00]  Like, what's the decision?
[2153.22 --> 2157.96]  Where's the threshold to making that decision to go to functional style versus basically just using your interface?
[2158.72 --> 2160.30]  Yeah, I think that's a good question.
[2160.46 --> 2163.10]  I think it comes down to that sort of inflection point.
[2163.54 --> 2177.28]  If you're finding, like, you're going to write some crazy dot map function that's going to abstract away your loops and you and or your team are just, like, really struggling with it, it's probably when you just go back and you write your interface and you write your for loop.
[2177.28 --> 2182.04]  And that's totally, I mean, we know that's idiomatic awesome go code.
[2182.04 --> 2210.42]  But I think really where it matters is if you find yourself writing, like, a bunch of for loops and your interfaces start getting bigger and bigger, that is probably a good place to start prototyping something in a PR and figuring out, like, hey, could I break apart this interface and replacing, like, a couple of those methods with maybe a couple functions outside of the interface that modify some stuff inside of one of the implementations.
[2210.42 --> 2219.92]  And I think a lot of folks will find, like, just doing that, assuming you write some decent docs on that function, just doing that can really simplify things a lot.
[2220.54 --> 2229.44]  And I would call it writing in the functional style because that specific function you're writing can start getting pretty interesting.
[2229.44 --> 2237.78]  But really, like, when it comes down to it, you're just taking a method out of a struct or out of an interface and just breaking it out into a function.
[2238.44 --> 2244.26]  And really, a lot of times, just that can really simplify stuff in your implementations for the interface.
[2244.82 --> 2245.08]  Okay.
[2245.24 --> 2250.64]  Some of the questions in the channel are sort of hovering around sort of performance impact.
[2251.08 --> 2255.44]  What kind of impact does that have on your code being able to run in parallel, if any at all?
[2255.44 --> 2265.62]  Along those lines, is there a performance penalty, right, or gain to actually having all these functions, calling these other functions?
[2265.96 --> 2273.80]  Although one could argue you're kind of doing the same thing in the imperative style, although in a more readily apparent way versus the functional style.
[2273.96 --> 2281.76]  But I guess, yeah, those questions are kind of digging into, okay, what is the performance penalty, if any, right, for using the functional style over the imperative?
[2281.76 --> 2282.24]  Yeah.
[2282.24 --> 2282.56]  Yeah.
[2282.92 --> 2289.10]  I mean, if you go crazy, there's going to be a penalty for sure because you're going to start copying memory all over the place in the heap.
[2289.88 --> 2293.74]  But if we're talking about, like, let's take the map in that functor.
[2294.62 --> 2298.20]  A map is basically an abstraction over a for loop.
[2298.42 --> 2300.70]  So you're going to have your same array.
[2301.32 --> 2302.70]  You'll wrap it in a struct.
[2302.80 --> 2304.98]  So there is some memory penalty there.
[2305.32 --> 2308.16]  You'll wrap it in a struct, and then you'll call your dot map.
[2308.16 --> 2311.14]  And the dot map is going to take in a function.
[2311.72 --> 2313.16]  So there's some memory penalty there.
[2313.52 --> 2319.12]  But inside of that dot map function, you implement that, again, with just a for loop.
[2319.42 --> 2330.00]  So you don't get the actual runtime performance penalty there because you're really just building a convenience function on top of a for loop in that case.
[2330.70 --> 2335.88]  In this example, the map is like the in JavaScript for each, isn't it?
[2335.94 --> 2336.42]  Exactly.
[2336.72 --> 2336.92]  Yeah.
[2336.92 --> 2346.90]  There is one difference in that the for each doesn't return anything, but the map will return the new thing, basically.
[2347.08 --> 2351.96]  The new thing that you've transformed using that function you passed in to map.
[2352.38 --> 2352.70]  Right.
[2352.88 --> 2359.78]  If you have an array or a slice of ints and you just want to increase them all by one, you could call map and have a function.
[2360.14 --> 2364.60]  And that function will just take in an int, add one, and return the int with that.
[2364.86 --> 2365.14]  Okay.
[2365.34 --> 2365.74]  Exactly.
[2365.74 --> 2366.26]  Yeah.
[2366.26 --> 2366.30]  Yeah.
[2366.52 --> 2372.56]  And that doesn't necessarily need to return a completely new copy of the slice.
[2372.56 --> 2380.34]  So the function won't be strictly pure, but it'll be, it'll have all the conveniences of functional maps.
[2380.34 --> 2386.42]  And it'll also be like I was saying before, you know, there's the observable pure and the interface pure.
[2387.16 --> 2392.08]  Interface pure basically means, hey, I can write this in the style of a functional programming.
[2392.08 --> 2393.08]  And that's what you're saying.
[2393.08 --> 2394.08]  And that's what you're saying.
[2394.08 --> 2394.84]  And that's what you get with maps.
[2394.84 --> 2398.24]  And then the tradeoff is you still have the same performance.
[2398.24 --> 2402.00]  So you mentioned earlier the HTTP handler funk.
[2402.00 --> 2414.60]  And I wonder, does the way that we talk about middleware, because in middleware, it's quite easy in Go to have a function and you pass in an existing handler and you can pass in additional arguments too.
[2414.60 --> 2420.42]  And it returns a new handler, but in some way modified by whatever the middleware is going to do.
[2420.54 --> 2425.02]  You know, you could imagine it's very easy to run code before then calling the original handler and things.
[2425.38 --> 2427.60]  Does that kind of thing happen in functional programming too?
[2427.60 --> 2429.10]  Yeah, absolutely.
[2429.64 --> 2430.08]  Middleware.
[2430.82 --> 2432.20]  Someone just said it in.
[2432.76 --> 2435.18]  Yeah, Barnaby just said middleware is just a builder pattern.
[2435.62 --> 2436.18]  Pretty much.
[2436.50 --> 2442.24]  I mean, you take in this next function basically and you wrap it all around a new handler.
[2443.04 --> 2444.76]  And that is called functional composition.
[2445.56 --> 2451.38]  So you're basically when you return, so you take in a function and then you return a new function.
[2451.38 --> 2457.28]  And then inside of that new function you return, you're calling the next function.
[2457.90 --> 2465.26]  And then as you build up middlewares, you keep composing those functions deeper and deeper and deeper inside of each other.
[2465.68 --> 2474.38]  So eventually, let's say you add five middlewares, you've got a top level function that nests five other functions beneath it.
[2474.60 --> 2478.96]  And then all the way at the bottom of that, you've got your next function that's being called.
[2478.96 --> 2488.12]  And assuming the middlewares do stuff, then there's a bunch of modifying the request and the response and checking stuff and all that good stuff too.
[2488.96 --> 2489.46]  It's very cool.
[2489.54 --> 2491.54]  I think I've written this kind of thing.
[2491.64 --> 2496.46]  Well, I've definitely written it like this before without realizing it was functional programming, I think.
[2496.80 --> 2497.28]  Yeah.
[2497.38 --> 2498.12]  That's always fun.
[2498.72 --> 2505.30]  A for loop would be a way of flattening all that out because you basically have a tree of functions.
[2505.54 --> 2506.94]  It goes down the chain.
[2506.94 --> 2520.30]  And then if you were to take a for loop, you would basically go through and execute a bunch of different functions one after the other to check the request and the response and all the cool stuff that middleware does.
[2520.78 --> 2524.24]  And then at the very end of the for loop, then you would actually call the route.
[2525.06 --> 2528.64]  Are there any examples of this from the standard library that we could point to?
[2528.64 --> 2529.36]  Yeah.
[2529.36 --> 2529.46]  Yeah.
[2529.82 --> 2533.06]  So if you look at sorts, sorts do this.
[2533.60 --> 2543.82]  You can pass in a callback to sorts and you don't really know what two elements of the list you're going to get.
[2544.46 --> 2552.64]  But you take a function that just takes two elements and returns whether or not the first one, I think, is bigger than the second or vice versa.
[2552.64 --> 2557.30]  Actually, someone mentioned parallel programming.
[2558.22 --> 2560.44]  Yeah, Barnaby, you're on fire in the channel.
[2561.16 --> 2562.78]  You mentioned parallel programming.
[2563.48 --> 2568.36]  I swear I didn't pay him to ask that question, but it's a really awesome question.
[2568.36 --> 2578.34]  Because if you think about that, if you wanted to, you could go and write a sorting library or a map function or, for that matter, a ton of other functionality.
[2579.10 --> 2592.86]  And if you're talking about passing in a callback to a function, you get this great abstraction that the function can then go ahead and start doing cool parallel stuff just by calling that function in different Go routines.
[2592.86 --> 2594.36]  No, it's interesting.
[2594.58 --> 2598.12]  So is that because it doesn't matter which order these things happen in?
[2598.26 --> 2600.76]  Because it's all deterministic in theory.
[2600.90 --> 2607.40]  So that iterate over a slice, but run them all at the same time, if you like, the end result should be the same.
[2608.12 --> 2608.34]  Yeah.
[2608.58 --> 2611.50]  This is one of the benefits of a pure function.
[2611.76 --> 2612.00]  Right.
[2612.00 --> 2625.58]  If your callback is pure and you're running internally, you're running all those same callbacks parallel, then it's all good because the callback isn't going to rely on some global state that's going to be race condition-y.
[2626.16 --> 2631.34]  And it's not going to be calling some outside network service and all that cool stuff.
[2631.34 --> 2639.66]  And you can just like spin up a ton of Go routines and pipe the values back in after each of those functions is done running.
[2639.66 --> 2647.90]  Yeah, it reminds me, and it's not quite the same, but it reminds me in kind of microservice architecture world and message queues and things.
[2648.00 --> 2659.52]  It reminds me of kind of idempotent or idempotent messages where if the inputs are the same, then it doesn't matter really how many times you do it, the end result's the same.
[2659.58 --> 2662.78]  I guess in that sense, we're trying to get the component to be pure in some way.
[2662.78 --> 2671.52]  It's not quite the same, but the principle, actually, I've definitely seen that benefit pay dividends, that design pattern in the past.
[2672.16 --> 2680.86]  Yeah, really, the idempotency is a subset of purity in the, you know, hardcore functional theory world.
[2680.86 --> 2686.18]  And really, yeah, idempotency is usually enough for these sort of fan-out patterns.
[2686.76 --> 2692.52]  And I actually read about another pattern in the microservices world that applies here.
[2692.92 --> 2705.28]  Basically, when, if you're building a search engine and you've got, like, you know, a news feed and a weather feed and, of course, the search results and, you know, whatever, images and all that stuff,
[2705.28 --> 2714.30]  you can actually do a fan-out and do multiple requests to each of those image service and search service and weather and all that.
[2714.72 --> 2718.56]  And you can just take the one that comes back the fastest and dump the other ones on the ground.
[2718.90 --> 2725.28]  That works because it's a get request and it's idempotent and it's not going to make any sort of side effects.
[2725.48 --> 2727.60]  Or in other words, it's just all reads.
[2727.60 --> 2735.42]  And when you're operating a scale, that can really give you some good speed-ups and sort of that long tail of request latencies.
[2736.10 --> 2744.32]  Yeah, I remember this pattern was actually one of the examples that I believe Rob Pike gave in one of his earlier talks,
[2745.04 --> 2750.34]  where, yeah, he was basically talking about sort of the exact same example you gave,
[2750.46 --> 2755.88]  whereby you could have multiple Go routines go perform that same exact operation, right?
[2755.88 --> 2759.96]  So, you know, because it's idempotent, it doesn't matter which one comes back first.
[2760.00 --> 2764.38]  It would have been the same result, right, in theory for all the Go routines.
[2764.64 --> 2767.94]  So whichever one comes back first, that's the one you go with.
[2768.06 --> 2772.48]  So, yeah, that's something I actually wish I saw more often.
[2772.60 --> 2778.86]  Maybe I don't work on things that work at that scale, but that is a very interesting and very useful pattern, actually.
[2778.86 --> 2779.76]  Mm-hmm.
[2780.12 --> 2782.92]  I think I may have stolen this from him.
[2783.06 --> 2786.62]  I saw a talk on this a while ago, too, in the Erlang world.
[2787.02 --> 2788.90]  This is sort of a pattern there, too.
[2789.38 --> 2795.52]  But to implement it, I think the code Rob showed was, it was, you know, a good amount of lines of code.
[2795.52 --> 2806.68]  And a functional pattern would be to wrap that code in something like a map function or something like a, you know, do n or something along those lines,
[2806.68 --> 2810.84]  where you just pass a bunch of functions to another function.
[2810.84 --> 2820.46]  And then under the covers, that thing is going to take care of, you know, spinning up all the Go routines and running multiple of the same function over and over.
[2820.76 --> 2825.24]  And, you know, all the cool stuff about getting the result back that returns the fastest.
[2825.74 --> 2832.64]  But to the caller, really, you're just writing one function per major functionality you want.
[2832.64 --> 2843.08]  And then the underlying thing does all this awesome magic to do the cool background, fast, whatever awesome other stuff that you want your library to do.
[2850.08 --> 2853.06]  This episode is brought to you by our friends at Rollbar.
[2853.18 --> 2856.14]  Move fast and fix things like we do here at Changelog.
[2856.24 --> 2858.90]  Check them out at rollbar.com slash changelog.
[2859.20 --> 2861.46]  Resolve your errors and minutes and deploy with confidence.
[2861.46 --> 2864.66]  Catch your errors in your software before your users do.
[2865.02 --> 2871.28]  And if you're not using Rollbar yet or you haven't tried it yet, they want to give you $100 to donate to open source via Open Collective.
[2871.38 --> 2876.34]  And all you got to do is go to rollbar.com slash changelog, sign up, integrate Rollbar into your app.
[2876.42 --> 2880.52]  And once you do that, they'll give you $100 to donate to open source.
[2880.82 --> 2883.64]  Once again, rollbar.com slash changelog.
[2891.46 --> 2903.14]  So I'm kind of wondering what the impact for testing is, right?
[2903.14 --> 2917.42]  So on one layer of my mind, I'm thinking, okay, well, if it's just a function, you can write, you know, basically at the unit level, you can write a test to, you know, maybe test every nested function you could possibly call for a given operation.
[2917.42 --> 2922.50]  But at the same point, I'm thinking, well, is it enough to just test at the API level?
[2922.68 --> 2930.38]  And because the calls you're going to make, you know, is going to sort of go through every single layer of functions that you're calling, right?
[2930.38 --> 2931.54]  Every nested function anyway.
[2931.98 --> 2938.56]  Like how do you approach sort of testing differently, if at all, right, in the functional style?
[2938.56 --> 2945.28]  Yeah, I mean, this is kind of where the whole test the interface, not the implementation thing comes in.
[2945.72 --> 2951.84]  I've heard that said a bunch in the Go community, and I've heard it implemented a lot too, or seen it implemented.
[2952.16 --> 2959.80]  And it's awesome because in Go, we can pull in all these insanely cool libraries that just make our life simpler.
[2960.48 --> 2963.12]  And those are obviously tested.
[2963.30 --> 2966.10]  If it's a solid library, it's going to be tested really well.
[2966.10 --> 2969.24]  And in the functional world, you can kind of do the same thing.
[2969.66 --> 2974.78]  Because if you're going to take, you know, five functions that each does a slightly different thing,
[2975.32 --> 2983.08]  and you're going to pass them into a package or library that's going to take care of making them all concurrent and cool and stuff,
[2983.72 --> 2989.70]  really you just have to test each of those functions to make sure that it does the right thing, obviously,
[2990.00 --> 2994.88]  and also to make sure that it doesn't have those side effects and it's idempotent.
[2994.88 --> 3003.62]  And then beyond that, you're going to just lean on that library or another person that may have written the parallel stuff,
[3003.82 --> 3008.98]  or maybe even yourself in a different mindset that wrote that parallel stuff.
[3009.42 --> 3011.44]  And you can split up the testing then.
[3011.56 --> 3013.54]  And you can test your business logic.
[3013.54 --> 3021.76]  And then in a whole different package, in a whole different test suite, you can test the awesome parallel stuff completely separately.
[3022.36 --> 3027.74]  And it really makes it a lot easier then because you can just focus on your one thing in each different context.
[3028.58 --> 3029.42]  Makes sense.
[3029.42 --> 3033.90]  That's a piece that I really love about, you know, generally functional programming.
[3034.18 --> 3037.60]  Since you've got these new higher level abstractions in general,
[3038.10 --> 3043.72]  the testing just becomes that much easier because you can think about stuff separately a lot more.
[3044.38 --> 3048.82]  Would it be strange if you hadn't had much experience with functional programming,
[3048.88 --> 3054.46]  you're just a Go programmer, and you've stumbled upon a repo that was written in the functional style?
[3054.46 --> 3056.74]  Would it make sense at a glance?
[3057.14 --> 3059.48]  And would the code that you end up writing with it make sense?
[3059.72 --> 3063.70]  Or would it be different and would it feel different to the programmer as well?
[3064.16 --> 3071.46]  So a lot of times when I first started in Go, I would see code that would take callbacks.
[3072.20 --> 3076.96]  And I would say to myself, you know what, that's not really the Go style.
[3076.96 --> 3081.08]  Like I didn't really think callbacks were a thing that you did in Go.
[3081.64 --> 3087.80]  And I imagine that might be the same feeling that someone new to the functional style would say.
[3088.30 --> 3090.84]  You know, why should I pass a function in?
[3090.96 --> 3093.22]  What is this library going to do with my function?
[3094.00 --> 3101.34]  I think, yes, it would probably be kind of confusing because it's this new thing that's not really idiomatic to Go necessarily.
[3102.08 --> 3103.98]  So I think docs are huge.
[3103.98 --> 3113.04]  If someone is writing a library in the functional style, you know, if you've got an exported function that takes a callback and does some insane cool stuff with it,
[3113.32 --> 3121.22]  you know, writing those docs that are going to be visible in godoc.org and really explicitly saying,
[3121.44 --> 3122.84]  this is how we're going to use your function.
[3123.48 --> 3125.88]  This is what you need to make sure your function does.
[3126.64 --> 3130.56]  You know, if you don't do it this way, we're going to return an error or, you know,
[3130.56 --> 3133.86]  your database is going to blow up or whatever it might be.
[3134.40 --> 3136.86]  Like that is massive.
[3137.24 --> 3143.38]  Like that's going to be the most important thing that you can do in your new functional style library for sure.
[3143.90 --> 3153.20]  So file path walk is an example where it takes a function and it calls that function for every file and directory that it finds as it's walking.
[3153.20 --> 3157.52]  That's a real kind of the real standard library example of it.
[3158.06 --> 3163.72]  And what they do is, even though you actually don't have to do this, they create a type for that function.
[3164.18 --> 3167.60]  And I think that's there for documentation purposes.
[3167.86 --> 3171.52]  There's like a walk funk, it's called, and it has its own type.
[3171.98 --> 3176.44]  You could just describe the function in the signature, although that could get ugly.
[3176.44 --> 3181.64]  But I suspect it's really there for, as to your point, it's more of a documentation thing.
[3182.18 --> 3185.80]  But at the end of the day, they're just calling functions and methods and things.
[3185.94 --> 3190.88]  So at least the Go code will be able to understand it, won't we, if we read it.
[3191.08 --> 3195.44]  We'd at least know that this is calling a function and, you know, we have to sort of...
[3195.44 --> 3199.32]  Or does it get to the point where it really starts to look weird,
[3199.56 --> 3202.72]  where you do lots of nesting on one line and things like that?
[3202.72 --> 3210.66]  Yeah, it's like you said, you know, if you were to just copy that function signature into the file path.walk,
[3211.16 --> 3212.62]  that would be crazy.
[3213.04 --> 3215.34]  You know, if you start looking at that function signature,
[3215.96 --> 3220.28]  it would end with like 10 closed parentheses or something.
[3221.26 --> 3225.08]  And at least for me, when I see that, my eyes just start glazing over.
[3225.54 --> 3229.72]  Because, you know, I've got to like start counting them and it's crazy, crazy business.
[3229.72 --> 3236.10]  One thing that I love that they did in that case is they created that file walker,
[3236.34 --> 3239.54]  but they also documented that type super well.
[3239.62 --> 3243.82]  And they said, you might get an error in this case passed into the function.
[3244.22 --> 3249.66]  And if you don't get an error, you're going to get the path if it's a file
[3249.66 --> 3252.44]  and you're going to get the directory name if it's not a file.
[3252.44 --> 3259.88]  And there's like tons of stuff in there that I can look up without having to look up the documentation
[3259.88 --> 3263.22]  for the actual file path.walk function.
[3263.48 --> 3267.44]  And that lets me do that separation of context really well.
[3267.90 --> 3271.14]  Because I don't have to think about how file path.walk is working.
[3271.62 --> 3276.14]  I can just go look at that type and figure out how does my function need to work?
[3276.14 --> 3281.16]  And how do I need to like take into account all the possible errors that it might get
[3281.16 --> 3282.32]  and all that cool stuff?
[3282.82 --> 3288.26]  So that might actually be a good example of if you are going to create a library,
[3288.26 --> 3292.60]  a package in the functional style, the walk funk sort of documentation
[3292.60 --> 3295.32]  might be a good example to sort of emulate, right?
[3295.36 --> 3301.04]  So that folks who are actually using your package know exactly how the function will be called
[3301.04 --> 3305.12]  and what to expect with sort of with every call of the function,
[3305.28 --> 3308.76]  the different edge cases you need to sort of be prepared to receive, right?
[3309.12 --> 3309.92]  Yeah, for sure.
[3310.56 --> 3318.04]  And another example that's front and center is the HTTP.handler and HTTP.handler func.
[3318.76 --> 3324.16]  Because those don't really deal with errors, but those are a great way to say,
[3324.30 --> 3330.06]  this is the function that's going to basically be the callback when your server gets hit at this path.
[3330.06 --> 3334.08]  And this is what you need to do in order to write this function properly.
[3334.64 --> 3336.76]  And that's another way, just like the walk funk.
[3337.12 --> 3341.84]  It's another way for you to focus on your business logic and not have to think about,
[3341.92 --> 3344.74]  you know, how does this HTTP server work?
[3345.36 --> 3349.98]  And for me, that's been huge, like many, many times when I've been writing servers.
[3350.72 --> 3354.16]  So speaking of errors, do errors work the same way, do you think?
[3354.44 --> 3355.78]  Or do you think of them as different?
[3355.78 --> 3362.64]  How does the fact that GoCode actually returns an error value, and that's how it kind of does errors,
[3362.90 --> 3364.26]  how does that fit into this?
[3364.30 --> 3366.52]  It actually feels like it might fit quite well.
[3367.02 --> 3368.16]  Yeah, yeah, it does.
[3368.98 --> 3374.46]  So the pattern that we have now of doing if error not equal to nil and then returning,
[3374.46 --> 3381.80]  that is actually kind of the most basic, rawest form of this construct in functional programming,
[3382.56 --> 3385.64]  usually called a maybe or sometimes called option.
[3386.26 --> 3391.18]  And I will try to explain this super quickly and as clearly as possible.
[3391.70 --> 3398.08]  An option is basically just the success value or an error, but never both.
[3398.08 --> 3404.18]  And the option then you can check it to see, hey, did this thing error out?
[3404.26 --> 3406.78]  And if it errored out, then deal with the error.
[3407.54 --> 3410.52]  And in the other case, you know, did this thing succeed?
[3410.90 --> 3412.60]  Then get the success value.
[3413.06 --> 3417.60]  But the key thing about option and the annoying thing to a lot of people about option
[3417.60 --> 3421.36]  is that you can't just get the success value.
[3421.82 --> 3425.26]  It literally, the type just prevents you from getting the success value.
[3425.26 --> 3431.94]  So it's kind of similar to Go where, you know, you get back that error and you've got to deal
[3431.94 --> 3433.34]  with it first class.
[3433.88 --> 3442.06]  Option is a slightly more annoying and in-your-face way of telling you, hey, this thing might error
[3442.06 --> 3448.00]  out and you've got to deal with that error before we're going to give you access to that
[3448.00 --> 3449.86]  success value in your code.
[3450.32 --> 3452.40]  Wow, more annoying and in-your-face.
[3452.40 --> 3454.50]  So take that, any critics of Go.
[3455.26 --> 3459.48]  We might start to hit the inflection point there because now that you've got this thing,
[3459.76 --> 3464.60]  now you're talking about how do I get access to that success?
[3465.34 --> 3471.16]  And then you start talking about like, okay, maybe I need to write a callback to get access
[3471.16 --> 3471.78]  to it.
[3471.90 --> 3479.02]  Or maybe I need to do like, do some kind of dot get function that might panic or something
[3479.02 --> 3479.62]  like that.
[3479.62 --> 3483.52]  So this one is a really good one to know about.
[3483.84 --> 3490.16]  And I think it's more useful to know that the if error not equal to nil is kind of a
[3490.16 --> 3493.86]  raw form of this type called option.
[3493.86 --> 3498.46]  And also to know that it could be worse, basically.
[3498.84 --> 3502.38]  If you've got this option type, you got to deal with this thing a little bit more.
[3502.88 --> 3503.24]  Yes.
[3503.66 --> 3506.88]  You've written about the functional programming in Go, haven't you?
[3507.04 --> 3507.62]  On your blog.
[3507.70 --> 3508.52]  I remember reading it.
[3508.70 --> 3508.90]  Yeah.
[3509.30 --> 3510.14]  Where's your blog?
[3510.14 --> 3511.92]  How can our listeners find that?
[3512.60 --> 3515.68]  My blog is arschles.com.
[3516.30 --> 3518.22]  I think slash blog.
[3518.58 --> 3519.78]  I want to say slash blog.
[3520.40 --> 3521.32]  A.R. Schles.
[3521.92 --> 3523.92]  And that's A.R.
[3524.00 --> 3525.16]  S.C.H.
[3525.20 --> 3525.86]  L.E.S.
[3526.30 --> 3527.82]  dot com slash blog.
[3528.20 --> 3528.66]  Okay, good.
[3528.88 --> 3532.22]  And yeah, there's one on there about a decode, which was a package.
[3532.36 --> 3536.12]  Is it like a JSON parser decoder package?
[3536.76 --> 3537.10]  Yeah.
[3537.10 --> 3544.30]  This one was like an idea that I took from another functional language called Elm, E-L-M.
[3544.92 --> 3551.00]  And Elm is a front end language that aims to like basically just cut out JavaScript completely.
[3551.52 --> 3551.72]  Why?
[3553.00 --> 3559.26]  Well, I guess the creator didn't like JavaScript for some reason.
[3559.66 --> 3560.66]  Who knows why?
[3560.78 --> 3562.08]  They say it's good to have an enemy.
[3562.54 --> 3565.02]  If you're doing something, it's good to have an enemy sometimes.
[3565.36 --> 3565.84]  But fair enough.
[3565.84 --> 3570.78]  Yeah, it's like that necessity is the mother of invention type of thing.
[3571.02 --> 3578.90]  So the creator of Elm and a lot of the hardcore followers, they really love that it's a purely
[3578.90 --> 3580.06]  functional language.
[3580.76 --> 3584.88]  Technically not quite fair, but for the most part, it's completely pure.
[3584.88 --> 3595.50]  And you just write all of your front end code in this way that it forces you to deal with all the possible errors that can happen.
[3596.34 --> 3602.00]  And then the Elm compiler compiles it down to this crazy looking compressed JavaScript at the end of the day.
[3602.00 --> 3608.50]  But one of the cool things about Elm is their JSON support, especially their decoding support.
[3609.28 --> 3614.00]  So their decoding basically looks like a builder pattern.
[3614.00 --> 3621.04]  So you would say something like, when I get back this bucket of bytes, I expect an array.
[3621.68 --> 3632.28]  And then inside of that array, I expect the first element to be a number, an int32, the second element to be a string, and maybe the third element to be an object.
[3632.28 --> 3637.46]  But you also have to define the shape, exactly what that object should look like.
[3637.86 --> 3642.66]  And this is kind of starting to sound like the built-in encoding.json.
[3643.14 --> 3648.54]  But the only difference is that you get to define exactly what should come in.
[3649.06 --> 3652.60]  You can't do things like optional or non-optional.
[3652.98 --> 3657.34]  You actually have to call those out in the decoder functionally.
[3657.90 --> 3659.32]  So it's a crazy idea.
[3659.32 --> 3662.38]  It's sort of a little bit hard to explain.
[3662.76 --> 3664.82]  I tried to write some decent docs in there.
[3665.40 --> 3668.60]  But it's sort of a different take on JSON decoding.
[3669.20 --> 3673.02]  And it doesn't have performance that's too horrible.
[3673.72 --> 3677.18]  It's definitely not faster than encoding slash JSON.
[3678.02 --> 3685.02]  But it's sort of another take where you could actually use this thing and not expect your REST API to blow up.
[3685.54 --> 3685.72]  Awesome.
[3685.72 --> 3690.34]  And are there any other projects that you've seen that use this kind of builder pattern?
[3690.72 --> 3691.16]  I think the...
[3691.88 --> 3692.58]  Do you remember the Mongo?
[3692.78 --> 3693.54]  There's a MongoDB.
[3694.04 --> 3694.78]  It's called Mango.
[3695.00 --> 3695.84]  It's M-G-O.
[3695.98 --> 3697.58]  That's the name of the package.
[3697.68 --> 3699.42]  That was the driver for MongoDB.
[3699.60 --> 3704.40]  And that used to have this kind of fluent API, which feels a bit like that, this builder pattern.
[3705.38 --> 3709.26]  Didn't you also mention that Buffalo has this style too?
[3709.80 --> 3710.10]  Yeah.
[3710.10 --> 3713.68]  A lot of the query builders out there do.
[3714.08 --> 3715.46]  And Buffalo has POP.
[3715.74 --> 3718.58]  POP is their SQL query builder.
[3719.38 --> 3726.38]  And that's got the whole thing where you would do new query, dot select, dot filter.
[3726.58 --> 3729.00]  I think they have one called filter, dot order.
[3729.00 --> 3734.02]  And it's kind of like SQL sort of translated into a Go API.
[3734.90 --> 3744.76]  And each time you do one of those dot filter, dot select, all that stuff, you get a new struct back, a new query struct back.
[3744.76 --> 3749.30]  And then you can call the next function on that struct.
[3749.74 --> 3752.66]  So that's the builder pattern, but it's also pure.
[3752.86 --> 3768.50]  Because each time when you pass in select, you know, star from dogs, from your dog database, you're going to get back a new struct that has inside of it the information that you're about to select everything from the dogs database.
[3768.66 --> 3769.42]  It's super useful.
[3769.90 --> 3771.40]  That's where you could do the branching thing, right?
[3771.40 --> 3775.00]  You could have a function then that's going to go and get the latest dogs.
[3775.72 --> 3779.00]  And you could have a function that goes and gets the hairiest dogs.
[3779.84 --> 3782.02]  But you could base them off that original thing.
[3782.18 --> 3785.46]  My improvising use cases is not great, by the way.
[3786.18 --> 3789.00]  I started with dogs.
[3789.24 --> 3791.30]  So you're just going off of my thing.
[3791.44 --> 3791.58]  Yeah.
[3792.52 --> 3793.92]  No one would blame you.
[3793.92 --> 3808.34]  Given sort of your experience in Go and functional, like what would you say like a gopher who is sort of interesting, interested rather, and sort of knowing how to.
[3808.34 --> 3812.20]  I'm asking this really for myself is like, OK, it all sounds interesting.
[3812.30 --> 3824.42]  There's some benefits to be gained there, but I don't necessarily want to sort of dive in headfirst into the functional world to try and basically claw my way back out to figure out what of that I can actually use.
[3824.50 --> 3824.94]  Right.
[3824.94 --> 3838.88]  So what would you say is a good resource other than your blog where you have some articles in the Go functional GitHub repository where you have some examples there as well?
[3839.10 --> 3848.54]  What would you say is a good sort of a primer, right, that is just approachable enough for a gopher to sort of glean some things and sort of bring back to their Go?
[3848.54 --> 3862.28]  Yeah, so there's not a ton about functional programming specifically with Go, but there is a ton of functional programming resources out there that are in non-Go languages.
[3863.28 --> 3876.40]  So if it's with Go, I would say look in your own code and see if you've got global variables and open up a new branch and see if you can start passing global variables into your functions instead.
[3876.40 --> 3886.98]  And that might push you down this path of starting to return functions instead of returning values, other values and that kind of thing.
[3887.16 --> 3888.46]  And it's it's kind of simple.
[3888.62 --> 3890.98]  It might feel like, you know, why am I doing this?
[3891.46 --> 3893.50]  But it'll push you down the path a little bit.
[3893.98 --> 3898.40]  But then if you step outside of Go, there's tons of stuff.
[3898.50 --> 3902.38]  There's one that I love called Learn You in Erlang for Great Good.
[3902.38 --> 3905.80]  It's in Erlang, the Erlang language.
[3906.18 --> 3909.62]  We'll mix those words up as well to form a correct sentence.
[3910.22 --> 3910.72]  Yeah.
[3911.18 --> 3912.48]  Learn You in Erlang.
[3914.44 --> 3917.56]  There's the same the same thing for Haskell.
[3917.96 --> 3918.26]  Hang on.
[3918.30 --> 3918.44]  Sorry.
[3918.50 --> 3919.76]  Could you say that sentence again?
[3920.20 --> 3921.86]  I just really didn't pause it.
[3922.06 --> 3922.96]  One more time, please.
[3923.56 --> 3926.16]  Learn You in Erlang for Great Good.
[3926.56 --> 3927.90]  It sounds like you've had a stroke.
[3928.32 --> 3928.66]  Yeah.
[3928.84 --> 3929.16]  Yeah.
[3929.16 --> 3930.84]  I promise I haven't.
[3931.00 --> 3931.42]  Okay, good.
[3931.42 --> 3938.42]  But, you know, these resources are, you know, I guess they're probably 90% about functional
[3938.42 --> 3944.22]  programming and they don't really assume any familiarity with the language itself.
[3944.48 --> 3953.84]  But they do try to really dive into these sort of functional programming 102 concepts, which
[3953.84 --> 3959.16]  would be things like that dot map function and some stuff about parallel programming.
[3959.16 --> 3964.70]  And then, you know, when you go to page two, it's like you're going to read page two like
[3964.70 --> 3970.22]  10 times because then you start doing these like higher level things that take in functions
[3970.22 --> 3973.58]  that take in functions and your head will explode.
[3973.58 --> 3981.44]  But page one, even page one alone will bring you back to go with some really interesting
[3981.44 --> 3983.26]  sort of frame of mind.
[3984.14 --> 3989.56]  I actually, I promise that you can go into your code base and you can start at least seeing
[3989.56 --> 3995.22]  like, hey, this might be an interesting place to do a map instead of a for loop.
[3995.22 --> 3997.86]  And here's the reasons why and that kind of stuff.
[3997.86 --> 3997.90]  Yeah.
[3998.32 --> 3998.90]  That's great.
[3998.98 --> 4004.12]  Actually, Aaron, I'd love to see a talk on that very subject, which is just functional
[4004.12 --> 4010.20]  programming patterns and philosophies applied in Go in very useful ways.
[4010.30 --> 4014.46]  That would be a great talk because we've talked about a few of them on this show, but it would
[4014.46 --> 4020.50]  be cool to actually look at some real world examples of where these principles, if not exactly
[4020.50 --> 4026.54]  functional programming, but some of the principles, some of the shared principles, which might
[4026.54 --> 4029.22]  also help and make our code better to be a great talk.
[4029.32 --> 4029.96]  Was that a hint?
[4030.42 --> 4030.76]  Yeah.
[4032.60 --> 4038.92]  The thing that is sort of missing is like, at least for me, like if I was going to give
[4038.92 --> 4044.98]  that talk, I would go through like the Kubernetes code base, let's say.
[4045.52 --> 4047.24]  That's an extreme code base.
[4047.38 --> 4048.26]  It's massive, right?
[4048.26 --> 4054.12]  And there's tons of opportunity in there to like, you know, refactor a little bit.
[4054.34 --> 4058.74]  There's not, this isn't like go and replace 10,000 lines of code.
[4059.16 --> 4066.14]  It's like, I know like the client builder library in Kubernetes, the code that sets up the Kubernetes
[4066.14 --> 4067.96]  client and does all the cool stuff.
[4068.54 --> 4074.20]  There's a few places where you could replace like 20 lines of code with six or something
[4074.20 --> 4074.72]  like that.
[4074.72 --> 4079.76]  And, and that's the kind of thing that like I would go for.
[4080.58 --> 4086.38]  Not only would I talk about it, but if I was, you know, maintaining the client creation code
[4086.38 --> 4092.48]  in the Kubernetes code base, that's the kind of stuff I would go for is to even just in
[4092.48 --> 4094.82]  the implementation and not in the interface.
[4095.34 --> 4101.40]  Just go in and, you know, replace a couple lines with a few fewer lines and start there.
[4101.50 --> 4106.00]  And you can kind of build up from there as you gain steam in the functional world.
[4106.64 --> 4107.00]  Amazing.
[4107.30 --> 4111.76]  Aaron, thank you so much for joining us today and educating us on functional programming.
[4111.98 --> 4112.56]  Who knew?
[4113.22 --> 4114.48]  Well, thank you for having me.
[4114.74 --> 4115.46]  No, it's been great.
[4115.46 --> 4120.40]  Well, this channel is, some of the comments in here are really awesome.
[4121.24 --> 4123.06]  And Barnaby did it again.
[4123.70 --> 4127.46]  He said, what's missing from Go to make Go a real competitor in the space?
[4127.78 --> 4133.86]  I think without adding any new features like cough, cough, generics.
[4133.96 --> 4134.32]  Bless you.
[4134.48 --> 4134.94]  Thank you.
[4134.94 --> 4140.82]  I really think that what is missing are some more like real production code base examples
[4140.82 --> 4143.54]  of some functional concepts.
[4144.04 --> 4151.60]  So, you know, I would say, you know, if generics came, it would be a Cambrian explosion of functional
[4151.60 --> 4157.26]  concepts and really good functional libraries, general purpose libraries in Go.
[4157.80 --> 4163.44]  But that's not to say that there's a ton of opportunity even right now to build functional,
[4163.44 --> 4166.68]  really awesome stuff in the standard library.
[4167.28 --> 4168.56]  Sorry, in libraries.
[4169.54 --> 4174.32]  And like, I'll shamelessly plug this decode library, but not because I want people to
[4174.32 --> 4174.72]  use it.
[4174.88 --> 4176.02]  You're welcome to if you do.
[4176.46 --> 4180.70]  But it's really more that like, I would love to just have this start a conversation.
[4181.42 --> 4186.78]  You know, people go in, try it out, submit an issue, tell me I'm dumb, whatever it may
[4186.78 --> 4187.08]  be.
[4187.54 --> 4192.74]  It would just be really cool to expand sort of mindsets in the Go community using sort of
[4192.74 --> 4193.44]  functional programming.
[4193.98 --> 4194.16]  Brilliant.
[4194.78 --> 4195.24]  I agree.
[4195.72 --> 4196.36]  So check it out.
[4196.44 --> 4200.88]  That one is github.com slash go hyphen functional slash decode.
[4201.36 --> 4202.14]  And it's Go functional.
[4202.84 --> 4204.64]  Are there other repos in that organization?
[4205.34 --> 4206.24]  There are.
[4207.24 --> 4213.62]  Most of them are just like, I put a repo up and wrote a main.go and then said, be cool
[4213.62 --> 4214.30]  if I did this.
[4214.38 --> 4215.64]  And that's been completely.
[4215.64 --> 4219.64]  So that's really the only one with some meat in it.
[4219.92 --> 4222.62]  The rest are just defunct.
[4222.92 --> 4223.18]  Okay.
[4223.26 --> 4227.98]  But you seem to be the person to get in touch with if anyone's interested in contributing.
[4228.66 --> 4228.88]  Yeah.
[4229.04 --> 4233.10]  DM me on Slack or submit an issue or whatever it may be.
[4233.50 --> 4233.74]  Okay.
[4233.80 --> 4234.06]  Brilliant.
[4234.98 --> 4236.96]  Well, thank you so much.
[4237.22 --> 4241.54]  We have come to the end of our podcast today.
[4241.54 --> 4245.22]  It's been emotional, not emotional, but functional, if anything.
[4246.66 --> 4250.80]  Thank you to Aaron again for educating us here.
[4250.90 --> 4252.62]  We've learned a lot for sure about this.
[4253.22 --> 4259.04]  The most surprising thing for me is actually that there's a lot of these ideas can be applied
[4259.04 --> 4263.06]  today to your Go code and you can start to see the benefits.
[4263.18 --> 4268.64]  And I think learning about the advantages and the reasons why these other things exist,
[4268.64 --> 4274.20]  wherever you can do that, you might find there's always little bits and pieces that you can
[4274.20 --> 4277.02]  apply in Go to your own projects as well.
[4277.14 --> 4278.92]  So absolutely check it out.
[4279.06 --> 4280.10]  What can you build with it?
[4280.18 --> 4280.84]  Let us know.
[4281.04 --> 4281.88]  And that's it.
[4282.00 --> 4283.36]  That's our show for this week.
[4283.48 --> 4285.30]  We'll see you next week.
[4289.38 --> 4290.02]  All right.
[4290.10 --> 4291.48]  Go time is back.
[4291.48 --> 4294.76]  It's been so much work behind the scenes, but it's definitely paying off now.
[4295.00 --> 4296.72]  And it's so much fun producing this show.
[4296.72 --> 4298.94]  We have so many people listening live.
[4299.06 --> 4300.04]  Thank you so much for that.
[4300.10 --> 4300.68]  We love you.
[4300.94 --> 4303.28]  And if you're not yet, hang with us and go for slack.
[4303.36 --> 4304.60]  We have a channel called Go Time FM.
[4304.80 --> 4305.14]  Look it up.
[4305.20 --> 4305.94]  You'll find us.
[4306.22 --> 4309.58]  Chat with the community, share stories, share coffee recipes, whatever.
[4309.74 --> 4310.36]  It's a lot of fun.
[4310.72 --> 4315.00]  Also, we have discussions on every single episode at changelaw.com.
[4315.10 --> 4317.26]  So head to changelaw.com slash Go Time.
[4317.42 --> 4319.56]  Find this episode and discuss it with the community.
[4319.56 --> 4324.94]  And of course, thank you to our sponsors, Digital Ocean, Strong DM, and also GoCD.
[4324.94 --> 4327.96]  Huge thanks to Fastly for being our bandwidth partner.
[4328.08 --> 4329.42]  Head to fastly.com to learn more.
[4329.78 --> 4332.64]  And we move fast and fix things around here at changelaw because of Rollbar.
[4332.74 --> 4335.02]  Check them out at rollbar.com slash changelaw.
[4335.24 --> 4339.16]  And we're hosted on Leno cloud servers at leno.com slash changelaw.
[4339.22 --> 4342.32]  Our music is by the one and only Brake Master Cylinder.
[4342.72 --> 4348.20]  And if you want to hear more episodes like this, subscribe to our master feed at changelaw.com slash master.
[4348.32 --> 4351.12]  Or go to your podcast app and search for changelaw master.
[4351.18 --> 4351.76]  You'll find it.
[4351.76 --> 4357.64]  Subscribe, get all of our shows in one single feed, as well as some extras that only hit the master feed.
[4357.94 --> 4358.56]  Thanks for listening.
[4358.90 --> 4359.52]  We'll see you soon.
[4381.76 --> 4386.94]  Have a great day.
[4386.94 --> 4388.76]  Okay.
[4388.76 --> 4388.92]  Bye.
[4391.08 --> 4392.76]  Bye.
[4392.76 --> 4393.08]  Bye.
[4394.14 --> 4394.58]  Bye.
[4394.64 --> 4395.06]  Bye.
[4395.20 --> 4396.14]  Bye.
[4396.54 --> 4396.56]  Bye.
[4396.58 --> 4396.72]  Bye.
[4396.72 --> 4396.88]  Bye.
[4397.76 --> 4398.68]  Bye.
[4399.20 --> 4400.16]  Bye.
[4400.26 --> 4400.86]  Bye.
[4400.98 --> 4401.32]  Bye.
[4401.42 --> 4401.84]  Bye.
[4401.92 --> 4402.92]  Bye.
