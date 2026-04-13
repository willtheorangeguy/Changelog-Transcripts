[0.00 → 2.04] I've thought of one, just top of my head.
[2.38 → 3.32] Just see what you think of this.
[3.46 → 6.86] Switch true and false round to really separate the wheat from the chaff.
[6.86 → 8.86] Matt, Matt, Matt, Matt, Matt.
[9.94 → 10.18] No?
[11.64 → 11.96] Mm-mm.
[12.20 → 15.48] Shall I open it, though, and see what happens?
[17.64 → 18.86] You could.
[20.42 → 23.12] BAM with 4Change Log is provided by Vastly.
[23.42 → 25.32] Learn more at Fastly.com.
[25.56 → 27.86] Our feature flags are powered by Launch Darkly.
[28.12 → 29.92] Check them out at LaunchDarkly.com.
[30.16 → 32.10] And we're hosted on Leno Cloud Servers.
[32.10 → 35.94] Get $100 in hosting credit at Leno.com slash changelog.
[36.70 → 37.52] What's up, Gophers?
[37.58 → 41.68] This episode is brought to you by Modish, a podcast from the team at Heroku,
[42.14 → 45.20] exploring code, technology, tools, tips, and developer life.
[45.38 → 47.46] There's a ton of great episodes on the Modish podcast,
[47.74 → 49.50] so I'd encourage you to check it out and subscribe.
[49.62 → 52.66] But in particular, I want to bring to your attention the recent episode
[52.66 → 55.10] featuring Cornelia Davis, the CTO of WeWork's,
[55.16 → 57.12] talking about cloud native, cloud native patterns,
[57.12 → 60.16] and what it really means to be a cloud native application.
[60.56 → 61.16] Here's a sneak peek.
[61.16 → 63.26] Can you define Git Ops?
[63.48 → 66.84] Maybe give a formal definition and talk about what some of the implications are?
[67.22 → 73.16] I think that the simplest formal definition actually doesn't involve the word Git at all.
[73.16 → 76.74] It is cloud native operations is the way that I think of it.
[77.30 → 82.48] Now, let me draw an analog there in that one of the things I didn't mention in my intros,
[82.58 → 85.56] that I'm also the author of a book called Cloud Native Patterns.
[85.56 → 90.26] And that book is targeted at developers, software developers and architects
[90.26 → 94.64] who are building these, you know, highly distributed applications,
[94.84 → 96.50] these microservice-based applications,
[96.50 → 100.48] and helping them understand all the patterns that you have to put in place
[100.48 → 104.30] to be able to make these microservices-based apps work
[104.30 → 107.60] in this ever-changing environment that they run in.
[107.98 → 109.52] All right, links are in the show notes,
[109.60 → 112.46] or head to heroku.com slash podcast to listen and subscribe.
[112.46 → 117.16] Again, check the show notes for links or heroku.com slash podcasts.
[135.66 → 136.70] Let's do it.
[137.26 → 138.32] It's go time.
[138.98 → 140.28] Welcome to Go Time,
[140.28 → 143.74] your source for diverse discussions from around the Go community.
[144.38 → 146.82] We have some awesome episodes in the queue.
[147.28 → 149.20] Brian Kettle son on code generation,
[149.62 → 151.38] Bill Kennedy on design philosophy,
[151.70 → 155.22] and an episode on the new Go Embed coming in 1.16.
[155.68 → 157.68] Subscribe now if you haven't yet.
[157.86 → 159.28] Go to gotime.fm
[159.28 → 162.00] or just search for Go Time in your favourite podcast app.
[162.20 → 162.90] You'll find us.
[163.36 → 164.32] Okay, let's do this.
[164.52 → 165.36] Here we go.
[165.36 → 165.40] Here we go.
[165.40 → 166.36] Here we go.
[166.36 → 167.40] Here we go.
[167.40 → 168.40] Here we go.
[168.40 → 170.26] Here we go.
[170.28 → 173.44] Hello, and welcome to Go Time.
[173.90 → 177.34] I'm Matt Ryder, and I close my browser tabs.
[177.60 → 182.56] I'm not like these people that just have millions of tabs open for weeks and weeks,
[182.66 → 184.08] and then they can't find anything.
[184.30 → 188.46] And when you pair with them, you know, they can't even find anything.
[188.62 → 190.08] So it's like, close your tabs.
[190.66 → 191.12] That's it.
[191.48 → 192.62] I close my tabs.
[192.62 → 198.42] Welcome to part two of our deep dive on Go Language proposals.
[199.06 → 205.16] You don't have to have seen part one or heard part one, but you, you know, we're not that
[205.16 → 210.12] organized, but you can go back and listen to it afterwards for different language proposals
[210.12 → 212.56] that we all just discuss and chat about.
[212.56 → 216.48] So, let's meet the panel today.
[216.70 → 219.96] Joining me, it's your friend and mine, Johnny Portico.
[220.32 → 220.86] Hello, Johnny.
[221.56 → 222.58] Hello, everyone.
[222.94 → 225.08] And I do keep my tabs open.
[225.34 → 225.74] How many?
[226.14 → 229.22] Oh, I get to the point where I can only see the little favicons.
[229.22 → 234.68] I have to sort of guess which one of the multiple tabs are the same type of icon I have.
[235.14 → 240.52] Like, it's really hard when you have like a sort of GitHub icons on like more than
[240.52 → 241.52] half the tabs you have.
[241.54 → 243.28] And I have like 50, 60 of them.
[243.92 → 246.66] And then I wonder why my fan's like going off, right?
[246.68 → 248.46] So it's like self-inflicted wound almost.
[249.44 → 253.76] But yeah, I did find a neat little tool the other day called One Tab.
[254.22 → 258.22] It'll like close all the tabs and create links for you and put them on One Tab.
[258.22 → 259.54] One Tab as the name implies.
[260.22 → 262.86] So yeah, so now it's like I choose that.
[262.96 → 266.74] I use that as a sort of excuse to just open all kinds of things, right?
[266.78 → 269.70] Because I can always One Tab it and just have a list of things.
[270.10 → 272.34] By the way, am I the only one who doesn't use bookmarks anymore?
[272.78 → 274.78] Anyway, let's move on to the other folks.
[275.24 → 275.96] That's a good question.
[276.26 → 278.76] I've honestly never really used bookmarks.
[279.34 → 283.24] Like, I think I really should because there are loads of stuff on the internet in there.
[283.42 → 284.56] There are loads of stuff.
[285.26 → 286.88] But yeah, I don't.
[286.88 → 289.66] I just duck, duck, go everything fresh every time.
[290.16 → 293.22] Let's also meet our other guests.
[293.52 → 294.22] He's back.
[294.68 → 295.74] It's Roberto Claps.
[295.92 → 296.54] Hello, Roberto.
[297.24 → 298.30] Hello, hello.
[298.70 → 299.02] Welcome.
[299.54 → 303.58] And I would like to say that I pin some of my tabs and I close the others.
[304.42 → 306.66] So here's yet another approach.
[307.14 → 307.66] Nice.
[308.06 → 308.58] Professional.
[308.98 → 310.98] How many pinned tabs do you have?
[311.24 → 311.54] Nine.
[311.98 → 312.34] Okay.
[312.70 → 313.14] Okay.
[313.14 → 313.58] What are they?
[313.84 → 316.18] Is that because that's the maximum number you're allowed to have?
[316.42 → 318.28] Or is that where you really?
[318.48 → 321.18] No, it's just because that's the amount of charts that I use.
[321.66 → 325.92] And each one of them has to run in a separate tab because the web.
[326.56 → 326.96] Yeah.
[327.36 → 327.68] Okay.
[327.68 → 331.50] What are all the tabs or the URLs for them all?
[331.54 → 332.56] Can you just read them out quickly?
[333.22 → 333.60] No.
[334.24 → 334.92] No, it's fine.
[335.10 → 335.36] It's fine.
[335.42 → 336.64] I don't want to advertise any chat.
[336.66 → 337.18] I just thought I'd ask.
[337.92 → 338.90] Yeah, no, there are no props.
[339.46 → 342.64] We've also very lucky to welcome back Daniel Marty.
[343.00 → 344.18] Daniel, welcome back.
[344.42 → 345.12] Happy to be back.
[345.12 → 349.18] And I feel like I'm back from the past because I just realized that tab pinning is a thing.
[350.88 → 353.02] As of 10 seconds ago.
[353.40 → 354.46] It's like back to the future.
[354.98 → 357.02] I do close my tabs religiously.
[357.12 → 363.86] In fact, on my phone on Firefox, I even enable the setting to automatically close tabs after 24 hours because I'm too lazy to do it myself.
[364.04 → 365.20] So they just automatically die.
[366.06 → 366.36] Wow.
[366.36 → 367.88] That is very neat.
[368.30 → 369.08] That's next level.
[369.40 → 374.10] Your life must be clean and simple and just minimalist, you know?
[374.10 → 375.22] But so on the edge.
[375.24 → 377.04] Yeah, just ignore my background and yes.
[378.24 → 378.68] Okay.
[381.48 → 381.96] Great.
[382.24 → 385.28] Well, maybe we should just jump straight in.
[385.46 → 387.26] Although actually, I was just thinking about this.
[387.78 → 392.76] There may be new, there are in fact new watchers slash listeners.
[393.22 → 399.10] So maybe we could just quickly go around and tell us a little bit like where you work and that and what you do.
[399.54 → 399.72] Why?
[400.04 → 401.60] Like, do you do computers and stuff?
[402.20 → 402.42] Anyone?
[402.42 → 404.20] Johnny, do you do computers?
[404.68 → 404.90] Yeah.
[405.14 → 405.92] Yeah, usually.
[406.32 → 406.44] Yeah.
[406.66 → 411.02] My job involves finding out why they're not online anymore.
[411.70 → 411.94] Oh, yeah.
[412.04 → 412.92] I'm an SRE.
[413.54 → 413.78] Yeah.
[413.78 → 417.96] So usually I'm chasing down why they stop working those computers.
[418.60 → 418.68] Yeah.
[418.92 → 419.18] Oh.
[419.38 → 419.54] Yeah.
[419.62 → 420.62] What would we do without you?
[421.18 → 423.18] You know, not have any internet, I guess.
[423.32 → 423.78] No web.
[423.88 → 424.56] No web for you.
[424.64 → 425.44] No tabs for you.
[425.84 → 426.04] You know?
[426.04 → 426.44] Yeah.
[426.84 → 427.04] Yeah.
[427.36 → 427.72] Exactly.
[427.92 → 429.34] Solve the tabs' problem, though.
[429.58 → 431.92] So difficult one there.
[432.36 → 434.52] Roberto, what are you doing with your days?
[434.90 → 435.18] Yeah.
[435.18 → 437.40] I also work with computers, also the web.
[437.54 → 440.90] And I make sure that if it works, it doesn't work too much.
[440.90 → 444.14] Like, it starts giving data to people that are not supposed to get it.
[444.50 → 447.34] So kind of the other side of the spectrum.
[448.10 → 448.44] Right.
[448.92 → 449.12] Yeah.
[449.16 → 451.26] So you two are kind of fighting in some ways.
[451.42 → 453.44] You're trying to get things online and out there.
[453.58 → 454.14] And you're sort of like, no.
[454.14 → 457.90] If I could shut everything down, it would be perfect.
[458.16 → 459.70] Everything is secure if you can't access it.
[460.46 → 460.74] Yeah.
[460.90 → 461.72] That is true.
[462.04 → 462.56] Great point.
[463.50 → 464.82] Daniel, what about you, mate?
[464.88 → 465.78] Do you do computers?
[466.34 → 467.20] I do computers.
[467.20 → 471.96] I've also been contributing to Go for a while, especially some packages like JSON.
[472.30 → 476.44] So whenever any of our listeners complain about JSON, I'm usually on the receiving end.
[477.40 → 477.50] Right.
[478.30 → 478.62] Yeah.
[478.88 → 480.70] And I see Roberto laughing at that.
[482.56 → 483.04] Yeah.
[483.14 → 489.90] We'll have to do a proper episode one time when you can just show us all the complaints that you get about JSON.
[490.28 → 490.78] I'd love that.
[490.78 → 497.76] I worked with somebody once who complained about JSON because he thought it had too many brackets.
[498.18 → 502.20] And he wanted me to not use that many brackets because it's waste.
[503.50 → 503.94] So...
[503.94 → 504.42] That's YAML.
[504.80 → 505.04] Yeah.
[505.84 → 507.20] He invented YAML.
[510.12 → 510.76] Okay.
[510.92 → 511.90] So let's jump in.
[512.30 → 517.96] Why don't we go straight to our first language proposal that we're going to discuss today.
[517.96 → 521.40] Anybody following along, you can find these on GitHub.
[521.84 → 525.10] GitHub.com slash Golang slash go.
[525.64 → 529.12] And then we'll read out the issue number so you can follow along.
[529.54 → 535.14] The first issue number is issue number 20733.
[536.40 → 541.66] And it's a proposal to redefine range loop variables in each iteration.
[542.20 → 546.32] This is a common gotcha for a lot of people in Go.
[546.32 → 551.46] So, Johnny, have you seen this in the wild, bugs that relate to this?
[552.10 → 553.16] Yeah, I've seen it.
[553.30 → 557.44] And I have committed the defile myself.
[558.46 → 559.74] Not just as a newbie.
[559.92 → 564.02] Every once in a while, still to this day, it'll still catch me.
[564.48 → 566.16] So, yeah, it's a pesky little...
[566.16 → 570.34] Usually, the best example that's usually given is where you have some shadowing going on.
[570.34 → 575.02] Maybe you have a Go routine that you're launching, and you're closing kind of over your iterator or something like that.
[575.16 → 577.18] And you realize that you're not quite...
[577.18 → 579.26] The value you're expecting, you're not quite sort of...
[579.26 → 582.60] That's not quite coming out with each sort of iteration and whatnot.
[582.88 → 586.10] So it's a very easy sort of trap to fall into.
[586.10 → 588.10] And this proposal is...
[588.72 → 591.08] I looked at it, and I'm like, yeah, that kind of makes sense.
[591.14 → 593.94] Why doesn't it do that by default kind of thing?
[594.40 → 600.92] But yeah, as we dive a little deeper into it, I think there are some reasons why it wasn't adopted.
[601.06 → 602.62] But I'd be in favour of it, actually.
[603.32 → 603.78] Okay.
[603.88 → 609.56] So the problem is then, when you range over something, it reuses the variables, doesn't it?
[609.56 → 610.16] Mm-hmm.
[610.16 → 611.32] In each iteration.
[611.66 → 616.02] So if you do kick off Go routines and things, you feel like it should...
[616.02 → 620.76] You'd kick off that Go routine, and it's going to use the value that was there in that iteration.
[620.98 → 624.76] But actually, as that's updating, it'll update for all the Go routines.
[625.22 → 626.58] And that's where you then think...
[626.58 → 630.48] Usually you end up with like the last number and everything, and it's the same.
[630.56 → 632.38] And it's such a strange bug.
[633.00 → 634.32] It's like the last plus one.
[634.32 → 638.56] So if you're iterating over a slice, you actually go out of bound, which is even worse.
[638.56 → 638.96] And...
[638.96 → 639.34] Right.
[639.44 → 640.08] Yeah, of course.
[640.12 → 643.30] If you're ranging using it over like numbers, right?
[643.42 → 643.56] Yeah.
[644.04 → 644.44] Yeah.
[645.24 → 646.18] That's a good point, actually.
[646.18 → 646.94] I've never had that one.
[647.52 → 654.26] I just fixed one last week for a framework I'm working on that wasn't working because of this issue.
[655.88 → 657.16] So it's a fresh thing.
[657.22 → 658.10] It's a real thing.
[659.02 → 664.62] And I also think a pretty common case of this is when you have table-driven tests, and then you suddenly say,
[664.62 → 668.16] oh, I'm going to make them parallel so that they all can run in parallel with each other.
[668.56 → 669.36] Test cases, that is.
[669.86 → 673.84] And then, like days later, realize that one test should be failing, but it's not.
[674.20 → 678.98] And it's because you're testing the last test case a hundred times instead of testing each of the test cases separately.
[679.48 → 682.78] And it's because you forgot to make a copy of the variable, right?
[682.82 → 685.90] So you're just reusing the same variable and then the parallel test is a go-routine.
[686.26 → 688.16] So your tests are a lie then.
[689.00 → 689.22] Yeah.
[689.22 → 692.08] But that last case definitely works.
[692.08 → 693.08] It really works.
[693.38 → 694.38] It really works.
[695.34 → 695.52] Yeah.
[697.00 → 698.74] And there are workarounds, aren't they?
[698.80 → 703.72] But I genuinely find the workarounds to be really strange.
[704.18 → 710.94] Like you end up just essentially, yes, it looks like you're just assigning or creating a new variable and assigning it with the same name.
[710.94 → 713.54] That's weird, isn't it?
[713.56 → 716.58] Are there any other workarounds that are better than that?
[716.74 → 721.10] In one of my first talks, I was actually talking about this because it was a talk on Go pitfalls.
[721.62 → 724.54] And I proposed to pass it as a parameter.
[724.84 → 731.94] So if you're closing over the variable, instead of using a closure, you just accept that as a parameter, and you pass it to the function.
[731.94 → 737.64] But it's so intuitive because you see the variable appearing at the end of your code.
[738.34 → 751.02] And when I was talking about this, Roger Pepe was in the audience and just raised his hand saying, just shaking his head and saying, nope, shouldn't be doing that because it's unreadable.
[751.78 → 756.44] So I guess redeclaring the variable is the only readable way to do this.
[756.44 → 765.20] I feel like redeclaring a variable is also kind of silly because if somebody's, especially somebody that's new to Go, they look at that code, and they go like, that's kind of like a no-op.
[765.30 → 766.40] It's not doing anything, right?
[766.70 → 769.56] And then you kind of need a comment to say, hey, this is actually doing something.
[769.66 → 770.28] Don't delete it.
[770.52 → 773.20] Because if you delete it, the code might not actually break at all either.
[773.66 → 775.42] So it's extra confusing, I think.
[776.20 → 776.60] Yes.
[776.94 → 781.30] Sometimes if you're kicking off Go routines, you can pass arguments in.
[781.38 → 784.96] That's another way that it's actually quite a nice workaround, isn't it?
[784.96 → 790.24] If you're actually in the anonymous function, you actually take an argument and then when you call it, you pass in that value.
[790.36 → 794.92] At that point, then it'll be copied into that scope so that that's then safe.
[795.06 → 796.30] That's not too bad.
[796.92 → 799.04] But even that's quite strange.
[799.46 → 801.70] So Daniel, what is the proposal suggesting?
[801.70 → 808.20] So the proposal is essentially suggesting to change the default behaviour to redeclare the variable at each iteration.
[808.38 → 812.58] So essentially have a variable scoped within each iteration instead of sharing one.
[812.58 → 819.48] And then essentially, I can't think of a single program that would break that was doing something sane.
[819.74 → 828.82] If somebody was depending on this reuse of variables, and then I only use the last one for closures, I would argue that that was wrong to begin with.
[828.98 → 831.82] And it wasn't something that would always work anyway.
[831.82 → 834.10] So I think it's a good change.
[834.42 → 836.04] There is one extra data point about that.
[836.20 → 844.70] I found out that in the JavaScript specification, this is like if you use let in a for loop, it is redeclared on every iteration.
[845.16 → 856.00] So there is a specific entry in the JavaScript spec saying if you have a for loop and use let, the scope of let us inside the body of the for loop, not the one that is for var, for example.
[856.00 → 856.78] That makes sense.
[857.00 → 857.18] Really?
[857.30 → 857.46] Yeah.
[857.62 → 862.22] And everyone that uses JavaScript has never had any troubles with that.
[862.54 → 865.40] This is something that no one knows because it just works.
[865.52 → 868.70] It doesn't surprise anyone that this is behaving this way.
[868.86 → 869.08] Yeah.
[869.16 → 879.96] And I think to Daniel's point, this is probably completely backwards compatible because even code that has the weird quirky workarounds, they'll still work, you know, and they could be tidied up later.
[879.96 → 887.84] This has 91 thumbs up on GitHub emojis there and six thumbs downs.
[888.24 → 891.60] It's got 11 of these weird party emojis and nine love hearts.
[891.72 → 896.00] I think emojis are essentially how we should make decisions these days in the modern world.
[896.36 → 899.90] Someone's just done it deliberately, partied it, turned it to 12.
[901.60 → 904.50] So, yeah, I feel like this is actually quite a good one.
[904.68 → 908.42] Are there like, is there a difficulty in implementation?
[908.42 → 911.28] I mean, was this a design decision, do we know?
[911.64 → 918.18] Or is this just what happened and we sort of found out later this was a side effect of how it was built?
[918.80 → 924.60] In my reading of the commentary going back and forth, most folks seem to be in favour of it.
[925.30 → 928.82] People that are on the Go team, obviously, chiming in.
[929.10 → 931.70] People that are or were are chiming in.
[931.70 → 938.36] And for the most part, I mean, this seems like a change that wouldn't get a lot of pushbacks.
[938.92 → 948.82] Again, because, you know, with the sort of implicit implementation or support for this, you can't think of many situations where it would actually break someone's logic.
[949.36 → 954.50] If your stuff is sort of behaves as expected, not to say that there aren't any edge cases.
[954.50 → 959.12] But for the most part, it seems overwhelmingly supported.
[959.84 → 968.10] So, and there's a comment in there from Brad Fitzpatrick around sort of giving it more consideration for Go 2.
[968.36 → 968.98] So who knows?
[969.06 → 969.84] Maybe we'll see this.
[971.44 → 971.54] Yeah.
[971.54 → 978.84] But also, if you look at the way this is compiled, it's clear that the way it is because there is no exception there.
[979.20 → 980.06] It just works.
[980.18 → 983.54] This is the way the for loops are compiled because the first statement is run only once.
[984.32 → 985.60] And that's the declaration.
[986.24 → 992.22] And some people complain that this could introduce some performance issues because then you get a lot of variables.
[992.22 → 1002.62] But if you look at it, if you are really that concerned about performance, well, it's weird because why are you optimizing that kind of thing?
[1002.76 → 1008.40] But if you are, you can just declare it on the line before the for loop and just don't use the first.
[1008.48 → 1011.20] You can just do for semicolon and go on with your life.
[1011.20 → 1012.20] Yeah.
[1013.42 → 1022.48] So if you were ranging over some big chunks of data, you know, and then they're suddenly now being copied, could you ever notice that?
[1022.80 → 1025.02] Would that ever make a marked kind of difference?
[1025.44 → 1032.08] If you don't close over it and if you don't keep a reference, no, because the variable will be inclined by the inline.
[1032.22 → 1033.60] It will disappear in the next loop.
[1034.04 → 1036.74] I don't think these will survive iterations.
[1036.74 → 1037.18] Yeah.
[1039.34 → 1048.48] And I don't think copies are going to be a worry because if you have large structures as the element value that you're ranging over, they're getting copied today anyway.
[1048.92 → 1050.50] So it's just a different kind of copy.
[1050.76 → 1052.14] But I think it's still just going to be one copy.
[1052.58 → 1053.00] Yeah.
[1053.76 → 1062.62] Well, I know that junior devs often, and actually people sometimes from other languages and even just normal Go people.
[1062.62 → 1065.78] I'm really not trying to single any people out here.
[1065.78 → 1082.24] But there are some people that really do get a bit too worried about that kind of thing where, you know, they'll kind of use pointers unnecessarily sometimes because the idea of just passing pointers around is kind of much easier and lighter.
[1082.64 → 1084.58] But in practice, that's the thing.
[1084.66 → 1087.38] In practice, what difference does it really make?
[1087.42 → 1090.96] And I think that kind of good point generally to make there.
[1090.96 → 1091.00] Yeah.
[1092.14 → 1092.70] So, yeah.
[1093.10 → 1093.46] Okay.
[1093.62 → 1094.32] We'll do that one.
[1094.62 → 1095.48] We should do that one then.
[1095.62 → 1096.30] That's our decision.
[1096.44 → 1097.50] Is this what this is?
[1097.54 → 1098.62] We're just deciding now?
[1099.52 → 1101.16] Well, I've added a thumbs up.
[1101.50 → 1103.50] Maybe that'll kick it over the edge.
[1103.60 → 1103.90] What do you think?
[1104.04 → 1104.20] Yeah.
[1104.38 → 1108.94] They'll be like in the Go Team HQ, they'll be like, we've got a thumbs up from Johnny B.
[1110.02 → 1110.88] Let's get on it.
[1110.88 → 1114.34] I would actually bet on this one getting accepted soon.
[1114.84 → 1116.62] Of all the ones that we've talked about, at least.
[1117.72 → 1119.88] It's funny because it's been there for...
[1120.92 → 1122.80] I'm going to just check the date on it.
[1123.78 → 1125.04] June 19, 27.
[1125.58 → 1125.94] Yeah.
[1126.26 → 1126.62] 2017.
[1127.54 → 1128.46] So, yeah.
[1128.56 → 1129.34] It's a few years.
[1130.26 → 1130.60] But yeah.
[1130.70 → 1131.46] It'd be great to have that one.
[1132.78 → 1133.78] Okay, Daniel.
[1133.90 → 1135.60] Do you want to pick another one then?
[1136.42 → 1138.56] Unless anyone has anything more to say on this?
[1139.00 → 1139.30] Yeah.
[1139.46 → 1140.62] We can go on to the next one then.
[1140.76 → 1145.54] I'm actually going to go out of order because I'm avoiding a complex one and leaving it for
[1145.54 → 1148.14] later so that we can get to smaller ones first.
[1148.58 → 1151.76] So, I want to talk about issue 29036.
[1152.70 → 1155.04] And it's to make important symbols predictable.
[1155.04 → 1158.66] And this is sort of a double proposal.
[1159.12 → 1163.98] And that is, right now when you look at a Go file, and you see a name like foo, and you're
[1163.98 → 1165.36] thinking, where does this come from?
[1166.36 → 1168.24] You would think that the rules are pretty simple.
[1168.46 → 1169.98] Like, is foo in my current scope?
[1170.10 → 1172.28] Like, in my current function declaration as a variable?
[1172.54 → 1173.54] Or is it a parameter?
[1173.74 → 1174.38] Or is it a global?
[1174.80 → 1176.30] Or is it something that I imported?
[1177.50 → 1181.54] And that's usually true, but it's actually not always true in Go.
[1181.54 → 1187.68] Because if you use a.import, a.import means import all the names from this other package.
[1188.26 → 1191.90] And if you just look at the Go file alone, you don't know what all those names are.
[1192.12 → 1193.96] So, it's sort of implicit instead of explicit.
[1194.84 → 1197.64] And the other case is when you import a package.
[1198.38 → 1204.02] And the last element of its package path does not match its package name.
[1204.02 → 1205.94] And Go allows that.
[1206.12 → 1210.20] It allows you to then use the package name instead of the last element of the package path.
[1210.88 → 1215.34] And many people then use the name explicitly in the import, but you don't have to.
[1215.48 → 1220.12] And if you don't, then you've got to get back into this edge case where the name is implicit.
[1220.26 → 1220.78] It's not explicit.
[1221.18 → 1223.66] So, this proposal is essentially forbid those two modes.
[1224.26 → 1228.10] And then when you look at a name in a Go file, without loading all the dependencies,
[1228.30 → 1232.22] without loading all the type information, you can always easily know where it comes from.
[1232.22 → 1241.12] Yeah, this is one where it's kind of one of those best practices is to name the folder of the package the same as the package.
[1241.48 → 1244.10] Because it just helps with lots of things.
[1244.26 → 1251.00] And then this proposal is talking about, I suppose, you always require that symbol to be explicit, maybe.
[1251.32 → 1259.34] Or it would be harder to make it not allow you to put a different package name inside a folder, wouldn't it?
[1259.34 → 1260.84] That would be quite strange.
[1260.84 → 1267.10] But is that the proposal then, is to always, it will define, and you do it before the import.
[1267.22 → 1272.18] So, you do import the name that you're going to use locally, and then the package as a string.
[1272.68 → 1274.08] And that's how you can do that.
[1274.48 → 1278.98] You can also, Daniel, though, you could make up any symbol name, couldn't you?
[1279.10 → 1280.74] But that's probably okay, isn't it?
[1281.48 → 1283.70] Because it's local and that's up to you.
[1283.70 → 1286.04] And in fact, it's kind of a feature too, isn't it?
[1286.38 → 1291.02] Especially if you've got clashing packages, or even you just don't like the package name.
[1291.02 → 1291.54] Right.
[1291.66 → 1299.24] So, I think what's being forbidden here is that if I declare a package path called go-foo, but the package name is foo.
[1299.78 → 1306.40] Right now, I can import that as literally just some paths slash go-foo, but then use it as foo.
[1306.82 → 1308.48] Because the package name is implicit.
[1309.04 → 1310.02] So, there's a saying, no, no.
[1310.02 → 1313.98] If you want to use it, you have to explicitly import it as foo.
[1314.44 → 1317.46] Because then the syntax alone will tell you where foo is being defined.
[1318.16 → 1319.30] And I think that's a good change.
[1319.70 → 1324.90] I agree also because we can have tools like go-import automatically at that named import.
[1325.30 → 1329.96] And people will not touch it, but when you read the file from GitHub or wherever,
[1330.58 → 1337.54] you can just infer everything from the file without having to look around and hope that you find the right name.
[1338.04 → 1339.86] This is one of the features that I love about go.
[1340.10 → 1342.00] Every file is self-contained.
[1342.68 → 1345.60] You can understand a lot by just looking at a file.
[1345.84 → 1348.94] And if you can see every file of a certain package, you understand the whole thing.
[1348.94 → 1356.32] The one thing I'll say I'm not in love in regard to this proposal is the elimination of the.import.
[1357.24 → 1358.80] There are some legitimate use cases.
[1359.00 → 1364.24] I mean, although I'll caveat that by saying that I don't use.import very often.
[1365.04 → 1368.14] Honestly, I can't remember the last time I used that in production code, to be honest.
[1368.14 → 1373.76] I do know of some use cases where it does make for more elegant code, more readable code.
[1373.76 → 1387.96] The code generator, I think Goa, for example, I think does a very good job of that, of using the.import to allow you to leverage a very nice DSL-like mechanism.
[1387.96 → 1398.70] For those that don't know what the.import does, basically, whatever package you're importing with a.import, it just kind of pretends that whatever you've just imported is in the same package where we're actually using it.
[1398.70 → 1407.30] So rather than saying Goa.API, you can just say, if you import the Goa package, you can just say API.whatever, right?
[1407.30 → 1409.32] Without having to say Goa.API.whatever.
[1409.82 → 1416.78] So it makes for, if you're writing DSLs, it can be a nice tool to have on your tool belt.
[1416.78 → 1421.96] But those are very specific circumstances, I think.
[1422.52 → 1427.12] But even then, something like this would probably break a lot of things.
[1427.34 → 1430.34] So because of that, I can see the value of it.
[1430.60 → 1438.66] But because of that, we probably have to sort of have some tools to do some rewriting and things like that to sort of prevent a widespread breakage of things.
[1439.14 → 1441.74] But yeah, I think I'm not too hot on this one.
[1441.74 → 1448.64] I think that the first part of having explicit naming will probably work.
[1448.74 → 1451.08] Like, I don't see why this wouldn't be accepted.
[1451.44 → 1461.48] When I said the.import, I see this as a harder one, especially because in tests, I've seen a lot of packages that offer sort of a DSL for tests.
[1461.86 → 1465.36] And you just.import, and you can just write assert or do stuff.
[1465.52 → 1467.16] I personally don't like it.
[1467.16 → 1472.88] I advise against it, but I can see why people would like to do this.
[1473.28 → 1477.98] But these aren't mutually exclusive, or rather they don't have to go together, do they?
[1478.20 → 1478.36] Yeah.
[1478.36 → 1484.76] You could still have.import, but then also force the symbol, explicit symbol import.
[1485.26 → 1486.92] Yeah, this is kind of a two-in-one kind of.
[1487.98 → 1488.18] Yeah.
[1488.72 → 1492.38] Well, this one has 63 thumbs up and one thumb down.
[1492.60 → 1495.76] Just a single, solitary thumb down.
[1495.76 → 1499.14] So it does have some love there.
[1499.16 → 1499.48] Some support.
[1499.98 → 1500.26] Yeah.
[1500.44 → 1507.42] And I think also, like, there's a wider kind of point here, which comes up a lot when we talk about Go.
[1507.72 → 1510.52] And Daniel, you actually make this point in that issue.
[1510.78 → 1511.66] You made it years ago.
[1512.32 → 1515.26] Like, some kind of time traveller or something.
[1515.80 → 1520.92] You said, you know, Go, it's really like, it's read much more often than it's written.
[1520.92 → 1525.86] So we ought to optimize for it being read, right?
[1526.30 → 1526.62] Yeah.
[1526.80 → 1534.94] And I actually think there's also, like, we've talked a lot about the human element here, but I also think we should remember the tooling element, the machine element.
[1535.56 → 1538.04] Go is pretty well optimized to being fast to compile.
[1538.04 → 1544.44] But I feel like in these two cases, tools get slower because they can take shortcuts.
[1545.30 → 1549.44] If names are predictable, you can predict where they're going to be.
[1549.82 → 1553.28] Something like GoToDefinition could be a very simple Go program.
[1553.56 → 1555.60] You would just read a Go file, look at a name.
[1555.74 → 1556.54] Where is this name defined?
[1556.64 → 1559.72] You just look at your function, your imports, and that's pretty much it.
[1559.82 → 1560.98] And then you just follow the graph.
[1560.98 → 1564.94] But the moment you add.imports, you know, that kind of goes out the window.
[1565.04 → 1567.52] You have to put, like, a linear search across your dependencies.
[1568.08 → 1572.74] I think in practice, this might not affect most people because most people don't use.imports and such.
[1573.00 → 1579.38] But I feel like the mantra of Go being simple and being fast to use and compile would fit this.
[1580.20 → 1580.32] Yeah.
[1580.94 → 1581.20] Hmm.
[1582.22 → 1582.70] Cool.
[1582.78 → 1584.30] That's a fascinating one.
[1584.70 → 1585.98] Tell us what you think.
[1586.64 → 1590.16] Tweet us at gotimefm and let us know your thoughts.
[1590.16 → 1592.62] I've thought of one, just top of my head.
[1592.96 → 1593.92] Just see what you think of this.
[1594.46 → 1597.94] Switch true and false round to really separate the wheat from the chaff.
[1598.24 → 1599.96] Matt, Matt, Matt, Matt, Matt.
[1601.04 → 1601.30] Mm-mm.
[1601.84 → 1602.10] No?
[1602.74 → 1603.06] Mm-mm.
[1603.30 → 1606.56] Shall I open it, though, and see what happens?
[1608.84 → 1609.46] You could.
[1609.46 → 1609.98] You could.
[1620.16 → 1622.44] What's up, Gophers?
[1622.52 → 1624.60] Are you trying to take your infrastructure further, faster?
[1625.06 → 1625.88] Of course you are.
[1626.18 → 1630.22] On March 3rd, join Equinix Metal for their first technical user conference called Proximity.
[1630.54 → 1637.40] Proximity is a follow-the-sun day of live-streamed technical demonstrations showcasing Equinix Metal's partners and their ecosystem.
[1637.86 → 1643.28] Visit metal.equinix.com slash proximity to view the schedule for this event and get closer to your digital advantage.
[1643.28 → 1646.50] Again, metal.equinix.com slash proximity.
[1665.30 → 1668.34] Right, Daniel, what's the next one we should have a look at?
[1668.34 → 1676.98] So I was thinking we could open the Pandora's box, that is, type inferred composite literals, and this is issue number 12854.
[1678.12 → 1687.76] And this is a pretty large change to the language, and it's essentially saying whenever a composite literal is essentially an expression with the curly braces.
[1687.76 → 1691.54] So you can think of struck literals, slice literals, and such.
[1691.54 → 1705.10] And the proposal is essentially if the compiler can statically know what type that expression would be, for example, because you're assigning it to a struct variable, or you're assigning it, or you're passing it as a parameter that's a map,
[1705.60 → 1708.60] then it can statically know what the type of that composite literal is.
[1708.96 → 1710.32] Then you don't have to spell it out.
[1710.54 → 1711.76] You don't have to spell out the type.
[1711.76 → 1719.22] And I think a lot of people support this idea because Go can be quite verbose when you use a lot of these types.
[1719.84 → 1724.96] And oftentimes the type is repeated multiple times in the same function or in the same local code.
[1725.56 → 1734.80] But at the same time, I feel like it might hurt readability, especially in terms of what we talked about earlier, about Go being easy to read at a local level.
[1734.80 → 1736.58] Yes, that's interesting.
[1736.74 → 1742.96] There are examples of type inference in the language, and they do work quite nicely.
[1743.38 → 1748.68] Do you find that they affect readability much, the current examples that we have?
[1749.24 → 1754.58] I don't think so, because the current examples we have, the type is always spelled somewhere local.
[1754.98 → 1755.24] Yeah.
[1755.24 → 1762.30] You cannot create a new composite literal without having the name of that type somewhere in your local scope.
[1762.82 → 1763.96] I think it's impossible.
[1763.96 → 1766.80] With this new proposal, it would be possible.
[1766.98 → 1774.26] You might call an API that returns a type, and then you assign a new literal to that type, but you're not spelling out what that type is.
[1775.52 → 1778.22] Nowadays, this mostly happens for collections.
[1778.62 → 1788.00] Like, you can say a slice of this type, and of course, you can just use the literal without the type again, because, I mean, you just said what this is.
[1788.00 → 1799.94] If this were to change, I would be in favour of this proposal with a little twist to it, which are you can type that code without the type, and then Go Fund can just add the type for you.
[1799.94 → 1806.42] So you write fast, and then Go Fund kicks in and makes everyone able to read it fast.
[1806.78 → 1809.50] So you don't compromise.
[1809.70 → 1811.30] You get readability and writeability.
[1811.30 → 1813.62] That is very interesting, Roberto.
[1813.62 → 1820.42] Some are rather to speak up for those that think omitting the type makes for more readable code.
[1820.86 → 1822.10] I like the proposal.
[1822.64 → 1823.92] I'll start by saying that.
[1824.00 → 1832.20] I think it would make for less verbosity, but there are those who value that verbosity as part of what makes Goode readable.
[1832.20 → 1839.56] So it's really one of those things where you have some folks that are on either side, and they both make valid arguments.
[1840.14 → 1845.48] I like the Go Fund sort of compromise, if you will, that you can type it quickly.
[1846.06 → 1850.96] But if your sensibilities are offended by seeing it and reading it, that's not going to help.
[1851.94 → 1858.56] Well, perhaps the best judge of readability might be the beginners to the language.
[1858.56 → 1861.82] How much sense does that make sense when you read that?
[1862.20 → 1863.68] Do you understand what's going on?
[1864.22 → 1869.26] And the second best, I'd say, maintainers of code that's been around for a while.
[1869.54 → 1883.20] If you haven't looked at this code for a bit, and you pull it up, and you open it, does having that type definition explicit, does that make the code more readable, more glanceable to you than not having it?
[1883.46 → 1892.10] So I think this is one of those where I think we'd have to sort of do a little bit of research and really figure out where everybody kind of leans.
[1892.20 → 1894.64] Yeah, Bill Kennedy makes a good point.
[1894.72 → 1897.60] He talks about this a lot in Now I Go for Slack.
[1897.74 → 1902.40] He says, this is about making things easy to do and not easy to understand.
[1902.76 → 1906.68] And actually, making them easy to understand ought to be the priority.
[1906.68 → 1909.50] So, yeah, very interesting.
[1910.10 → 1911.64] I don't know how I feel about this one.
[1911.82 → 1919.08] There are some cases where I feel like it would still be clear enough without specifying the types.
[1919.54 → 1925.32] But I could see for sure other cases where that gets complicated too.
[1925.32 → 1933.62] I'm actually thinking that I agree with Johnny saying that readability and maintainability is also a factor here and not just typing.
[1934.28 → 1938.78] And I think Roberto's point is mostly solved by editors and go please these days.
[1938.96 → 1944.04] So completion, if you're too lazy to type it out, just rely on your editor to do it for you.
[1944.04 → 1953.24] But I think my stance on all this is that I like the overall idea to repeat types less if it's obvious enough from the local context.
[1953.48 → 1956.44] But I also think this proposal as is too broad.
[1956.44 → 1964.22] If we have, you know, catch all type inference for composite literals, it's going to be abused, and it is going to hurt maintainability.
[1964.60 → 1971.44] So I would like to see proposals which are more narrowly scoped to cases where people, pretty much everybody agrees the code is better.
[1972.30 → 1978.36] And I actually have a couple of follow-up proposals, which are, I think, newer, which are a little bit narrowly scoped.
[1979.02 → 1979.12] Yeah.
[1979.32 → 1979.60] Yeah.
[1979.64 → 1981.40] OK, let's dig into those then.
[1981.40 → 1986.12] So the next one is so this first one that we talked about is from 2015.
[1986.36 → 1990.64] The next one is proposal number 35304.
[1991.26 → 1994.56] And it's from Roger Pepe again from 2019.
[1995.06 → 1998.48] And it's essentially anonymous struct literals.
[1998.66 → 2000.98] So it's not about all composite literals.
[2001.06 → 2002.38] It's only about structs.
[2002.80 → 2008.00] And the basic idea is that you can use an expression which is a struct, but you don't say what type.
[2008.00 → 2012.66] And then the compiler essentially figures out what struct that fits into.
[2012.82 → 2014.22] But it's only for structs.
[2015.06 → 2015.74] Yes.
[2015.94 → 2028.20] So this one definitely looks strange in the examples because in the proposal, Roger's written an underscore in place of where the struct definition would previously have been.
[2029.16 → 2033.56] And underscores in go to me mean like ignore this or dismiss this.
[2033.56 → 2037.44] So that to me didn't stand out.
[2037.58 → 2040.74] I didn't quite understand that just by glancing at it.
[2041.22 → 2048.16] But the principle is an interesting one because, yeah, often you are just repeating yourself.
[2048.28 → 2055.24] I do it quite a lot in test code, but in other code too, where I'll just in line have a struct that I declare, basically.
[2055.24 → 2061.50] And then immediately I will instantiate that, create one of them and set the fields.
[2061.56 → 2062.92] And I do it all in one go.
[2063.28 → 2064.84] And it's very repetitive.
[2065.20 → 2070.50] It's essentially a list of the fields with the types and then a list of the field names with their values.
[2071.04 → 2073.22] Would it help with that situation?
[2073.74 → 2074.44] Probably wouldn't, would it?
[2074.46 → 2076.80] Because you have to declare the struct still somewhere, don't you?
[2077.04 → 2083.44] Part of me feels like grabbing a chunk of the previous proposal and sort of merging it with this one.
[2083.44 → 2088.06] What I don't like about this one is the blank identifier, the use of the blank identifier.
[2088.24 → 2090.20] That's kind of rubbing me the wrong way a little bit.
[2090.72 → 2095.96] Like I associate that with what you said, Matt, with whatever it is that I'm assigning to this thing.
[2096.04 → 2097.12] I don't care about it, right?
[2097.12 → 2099.36] So discard it, GC it, whatever.
[2099.36 → 2115.76] So here I think we could get a mix of this in a previous proposal by omitting the blank identifier and basically relying on the tap inference basically to determine that, okay, I'm assigning this literal value, right?
[2115.76 → 2120.08] You already know what the type is based on my var declaration or something like that.
[2120.14 → 2122.64] Obviously, it wouldn't work for the bucktooth operator, right?
[2122.70 → 2130.12] But, you know, you could use it for if, you know, if you do var something of a given type, then you provide the literal value.
[2130.20 → 2132.92] Then I could see that, you know, without the blank identifier, I could see that working.
[2132.92 → 2138.74] I would like to clarify one thing, which is that this proposal is not strictly a subset of the previous proposal.
[2138.96 → 2140.54] So I lied a little bit, my bad.
[2141.02 → 2151.80] So there's one case that the previous proposal does not cover, which is what if you just want to create a struct expression, but it's not a named type that's been defined before.
[2151.96 → 2157.20] So you're, you know, you're creating an anonymous struct, a variable of anonymous struct type.
[2157.20 → 2163.06] So you could do var something, some name, and then struct, define the struct inline.
[2163.24 → 2165.08] It's an anonymous struct type and then the value.
[2165.62 → 2177.98] So with the previous proposal, because it's inferring what the type will be, there's nothing to infer to if you use, you know, foo colon equals and then underscore with this new syntax because there's nothing to infer to.
[2178.56 → 2178.74] Right.
[2178.74 → 2183.28] But with this new proposal, it would essentially be like it's not, it's an anonymous struct type.
[2183.28 → 2185.40] I'm not trying to fit it into any other type.
[2185.48 → 2187.48] So it's just an anonymous type, and would just work.
[2188.42 → 2194.20] So it figures out what the struct shape and structure should be from the values that you set.
[2194.64 → 2195.12] Is that right?
[2195.38 → 2195.54] Yeah.
[2195.60 → 2205.12] So if you're using that expression in the context where you're assigning it to something that has an explicit value, then the compiler would figure out is the shape the same.
[2205.64 → 2206.92] And if so, it would just work.
[2207.24 → 2208.82] If the shape is different, it would fail.
[2208.82 → 2217.54] And if there's nothing, no specific type that you're assigning to, it would just use an anonymous struct type, just as if you had spelled it out, duplicating all the field names and so on.
[2217.92 → 2223.92] Ah, so that I quite like because, yeah, there's no other way.
[2224.30 → 2231.92] I mean, apart from we're going to get into the world of like number types, like is this a float or an INT and things like this, which you have with constants anyway.
[2231.92 → 2234.22] You have to sometimes be explicit.
[2234.50 → 2240.96] If you want it to be a floating point, you have to put a decimal point in it, even if it's 0.0, at least you're just giving a clue that that's the type.
[2241.78 → 2243.08] I quite like that.
[2243.88 → 2244.08] Yeah.
[2244.44 → 2258.60] I've yet to sort of dive deeper into the comments, but is there a performance penalty there with trying to, because the compiler would have to figure out, like, do you have a match with whatever it is that you're trying to sort of assign the value to, right?
[2258.60 → 2260.32] Doesn't it already do this?
[2260.92 → 2270.40] Like, if you are assigning, like, you currently, as of today, you can take any struct type and assign it any other struct type, just with a cast.
[2270.98 → 2271.38] Yeah.
[2271.48 → 2275.80] And it needs to be able to figure out if the field is a subset of the other field.
[2276.26 → 2276.58] Mm-hmm.
[2277.20 → 2279.44] So I think this is already there.
[2280.08 → 2282.92] Yeah, this would all be statically, so it's not at runtime.
[2283.14 → 2283.34] Right.
[2283.34 → 2283.78] Yeah.
[2284.14 → 2296.68] Yeah, I wonder if you could just drop that underscore and just use, like, the curly braces and say, it's almost like JavaScript has just JSON object notation in the language, but it's a struct.
[2296.82 → 2298.02] It's an anonymous struct.
[2298.12 → 2302.18] It doesn't have a type, almost, or its type is created magically.
[2303.16 → 2304.00] Would that work?
[2304.40 → 2305.12] Is that reserved?
[2305.24 → 2306.84] That's not reserved for anything else, is it?
[2307.06 → 2308.06] A block, I guess?
[2308.50 → 2309.44] It's not reserved.
[2309.94 → 2312.16] But what I love about Go is that it's consistent.
[2312.16 → 2319.00] If you have var token equals, there must be two tokens afterwards.
[2319.28 → 2320.90] And it's, like, a type and a literal.
[2321.02 → 2322.30] If you're doing a literal expression.
[2322.56 → 2327.66] And I like when I read code, I can just glance over it, and I know the order in which things come in.
[2327.98 → 2333.72] If you drop one token, it starts feeling, like, unbalanced or clunky, so it would require more attention.
[2333.90 → 2339.00] Especially if you do, like, open brace, and you go on a new line, which this proposal is using already.
[2339.00 → 2348.16] And that would feel, if you glance over the code, like an if or a statement or something, because it doesn't have the extra token.
[2348.66 → 2352.00] And I like to be able to glance over the code and tokenize it.
[2352.38 → 2355.18] It's like an inline, like, scope block or something.
[2355.42 → 2355.56] Yeah.
[2355.80 → 2356.04] Yeah.
[2356.04 → 2360.20] Yeah, something came to mind, but quickly left, so I'll defer it.
[2361.46 → 2362.50] It wasn't flattering.
[2362.50 → 2371.98] I was actually going to follow up with what Roberto said, which is that if we drop the underscore, we change the Go syntax.
[2372.34 → 2379.64] Because right now, when you parse a composite literal, you parse type, open curly brace, the elements, close curly brace.
[2379.64 → 2390.56] And if you drop the type, if you drop the type expression, be it the underscore, be it some name, be it whatever you want, then every single program out there that needs to parse Go code has to be updated.
[2390.84 → 2392.44] And that has a pretty high cost.
[2392.74 → 2395.28] Maybe you can use a Robert's fix, right?
[2395.34 → 2396.80] Just throw some Go Fund at it.
[2397.76 → 2398.24] You could.
[2398.46 → 2399.66] Have Go Fund put it in there.
[2401.82 → 2405.58] While we're at it, why don't we just have Go Fund write all the code for us?
[2405.58 → 2407.84] I mean, yeah, yeah.
[2407.92 → 2409.32] I mean, soon it should.
[2409.84 → 2410.88] Are we working on that?
[2411.38 → 2412.36] Yeah, someone must be.
[2412.90 → 2413.52] Someone must be.
[2414.70 → 2415.66] Sorry, Daniel.
[2415.90 → 2426.70] There is this joke that I've seen a lot in other communities that is in Go, what the language can't do, the editors are supposed to replace.
[2426.70 → 2435.86] Like, I've seen a lot of people saying that Go uses generating code when generics are not there, or like using other tools to fill in where the language misses something.
[2436.46 → 2437.96] And that is always for writing.
[2438.46 → 2442.46] Like, all the things that I've seen was always about writing, never about reading.
[2443.02 → 2449.60] So, honestly, I mean, I wouldn't go as far as like something like, okay, Go Fund, write my code.
[2450.04 → 2452.78] Because that would be, you know, writing my job away.
[2453.02 → 2453.48] Matt would.
[2453.48 → 2458.42] You're telling me you wouldn't pay for that if I could build it?
[2458.42 → 2458.82] I don't know.
[2458.88 → 2459.54] I like coding.
[2459.82 → 2460.70] Oh, I never said that.
[2463.96 → 2464.98] That's what I'm doing tomorrow.
[2465.30 → 2466.98] That's the rest of my week.
[2467.34 → 2467.66] Out.
[2468.24 → 2468.68] Right.
[2469.06 → 2474.92] But, yeah, so I like to be able to quickly read code rather than quickly write.
[2475.00 → 2480.90] And if tools have to kick in every other line, I mean, Java is successful, and it's exactly the same, so why not?
[2480.90 → 2485.72] So, we have one more proposal in this little group of alighting types.
[2486.08 → 2488.68] Maybe we can quickly mention that one.
[2489.08 → 2492.36] It's proposal number 21496.
[2492.76 → 2497.94] And it's called Permit Alighting the Type of Struct Fields in Nested Composite Literals.
[2498.32 → 2502.66] So, it's sort of a mix of the previous two because it's only for struct fields.
[2503.06 → 2507.00] And it's only within nested composite literals.
[2507.00 → 2508.78] But it's still a lesion.
[2509.00 → 2510.28] It's not about anonymous types.
[2510.70 → 2510.88] Yeah.
[2511.32 → 2511.58] Right.
[2512.08 → 2517.96] I like those where the compiler can figure out, you know, like put in the type for me.
[2518.04 → 2520.04] You already know what it is, what it's supposed to be.
[2520.12 → 2521.46] Just put it in for me kind of thing.
[2522.04 → 2525.74] But, again, on the other side of that, you pay that readability cost.
[2525.74 → 2530.18] So, I think this proposal might be the smallest in terms of effect.
[2530.52 → 2535.36] I would even argue that this proposal is not going to affect readability because it's only within nested types.
[2535.72 → 2540.24] So, if you're in a nested type, then further up the chain, you must have mentioned that type already.
[2540.74 → 2540.98] Yeah.
[2541.24 → 2542.16] Yeah, I like this.
[2542.36 → 2542.50] Yeah.
[2542.96 → 2544.24] Yeah, I was just reading it.
[2544.50 → 2548.76] At the same time, I'm looking at the examples, and they don't quite look like go to me.
[2548.86 → 2550.42] So, I'm not sure how to feel about it.
[2550.42 → 2553.42] Yeah, that's an interesting instinct.
[2554.22 → 2555.96] I think it's actually quite important.
[2556.18 → 2560.74] I was just sat here reading this, which I realized doesn't make for great podcast content.
[2562.02 → 2563.06] But, yeah.
[2563.30 → 2564.04] I don't know.
[2564.22 → 2566.18] Roberto, what do you think about this one?
[2567.00 → 2570.98] This one, out of all of them, is probably the one that I like the least.
[2571.28 → 2573.42] Because it's such an uncommon instance.
[2574.34 → 2578.68] Like, I would have used this, like, probably five times in the past five years.
[2578.68 → 2582.92] So, I mean, changing a language is a long process.
[2583.04 → 2585.80] It requires a lot of work and a lot of discussion.
[2586.16 → 2592.24] And this small change would address part of the issue, not all of it.
[2592.44 → 2597.40] And if you use an IDE, a modern IDE, well, I use Team, so not even a modern one.
[2597.66 → 2601.98] And you are inside a struct, and you're about to type a field, and you just tap complete it.
[2602.26 → 2603.32] It's going to be there.
[2603.80 → 2607.66] So, this one would save me two keystrokes every five years.
[2607.66 → 2609.92] So, not a big fan.
[2612.50 → 2612.98] Yeah.
[2613.42 → 2617.64] I think the reason I like this proposal is that it's a very small step we could take
[2617.64 → 2619.94] in the direction of more type illusion.
[2620.34 → 2621.74] And we could experiment with that.
[2621.96 → 2624.42] And if people like it, we could take other small steps.
[2624.80 → 2626.50] Like, maybe we'd also do it for maps.
[2626.58 → 2632.28] Or maybe we also do it for other very specific edge cases where we're sure that readability is not harmed.
[2632.28 → 2636.58] Yeah, we did talk about this in part one of this, which is still available.
[2636.58 → 2643.44] If you want to go into your little podcast app, find the part one of this, and you can hear about that.
[2643.50 → 2646.62] We talked about doing this kind of thing for maps.
[2647.04 → 2655.06] I think the general point of what does it do to readability, I think, has to be kind of like the main consideration, really.
[2655.06 → 2658.58] It's not naturally, I think, what you immediately go to.
[2658.76 → 2662.26] Because when we're doing the work, we're typing it.
[2662.32 → 2664.74] And that's kind of where all our conscious thought goes.
[2665.06 → 2671.96] But, yeah, for sure, the glanceability, the readability, these properties, they are being considered.
[2672.14 → 2675.76] I think which is great, really, to see that people do think about this.
[2675.76 → 2685.92] Right. And if this proposal is like Daniel said, which are we start, you know, taking this off, and then we look around, and we see what else we can address.
[2686.02 → 2688.52] And maybe we can start alighting some types here and there.
[2688.72 → 2689.88] I would be in favour of that.
[2690.10 → 2695.92] But this proposal, as it is, like just this is for me not enough.
[2695.92 → 2705.94] But if we start looking around and see, again, maybe in this other context is very clear for the reader what the type is, we can just remove it there too.
[2706.42 → 2706.80] Why not?
[2707.84 → 2710.70] I mean, this is how we started to change the language.
[2710.88 → 2717.54] Like I think one of the first changes to the language in a long time was numeric literals allowed underscores or something like that.
[2717.60 → 2719.14] It was a small change, but it was a change.
[2719.14 → 2722.70] So this was the first step towards moving forward.
[2722.90 → 2724.36] That was a great change, by the way.
[2724.36 → 2725.54] I found myself using that.
[2725.54 → 2726.42] Yeah, I agree.
[2726.74 → 2727.90] Very quickly, yeah.
[2728.62 → 2730.10] What is it for people unfamiliar?
[2730.54 → 2737.96] Basically, if you have very long numeric constants that have too many digits, you can just add underscores in between digits at any point.
[2738.22 → 2740.76] That is ignored during compilation.
[2741.06 → 2748.70] But like if you have a billion, it just looks nice because it's a one followed by three triplets of zeros separated by underscore.
[2749.20 → 2749.40] Yeah.
[2749.84 → 2752.56] Yeah, it's sort of an improvement of readability, isn't it?
[2752.56 → 2755.96] I've had another thought that I'd like to float.
[2756.28 → 2757.94] This is a serious one now.
[2758.12 → 2759.24] It's not going to be silly.
[2760.02 → 2766.72] You know how Ruby, in Ruby, when you're accessing arrays, you can use negative numbers to come at it from the other side.
[2766.72 → 2770.16] So minus one essentially is the last item.
[2770.16 → 2772.72] And then minus two is the penultimate item.
[2773.28 → 2776.02] Minus three is, you know, third from the end.
[2776.78 → 2778.48] That is sometimes very useful.
[2778.64 → 2780.76] Often you do want to get the last item.
[2780.82 → 2783.36] And at the moment you have to take the length of it.
[2783.44 → 2784.90] You have to explicitly do that.
[2784.90 → 2792.18] How do you feel about having those Rubenesque negative numbers in index accesses?
[2792.62 → 2793.62] I don't like it.
[2793.82 → 2795.22] Why not, Roberto?
[2795.40 → 2800.64] Because most of the time that I got an off by one, I noticed because it panicked.
[2801.50 → 2808.08] Like most of the bugs that I saw in logs or stuff like that was because of crashes, because of off by ones.
[2808.08 → 2811.88] And I found out that the logic was flawed in other ways thanks to this.
[2812.04 → 2823.74] I would be in favour of having a built-in function called last that takes a slice or array and returns the last item and the last index if you read two values, for example.
[2824.06 → 2829.62] Because I've never needed the penultimate element, but the last one is frequent, as you say.
[2829.98 → 2836.22] So I would prefer something like that rather than having just weird minus one access.
[2836.22 → 2842.28] Unless maybe if it is a literal, like a numeric literal that you write in the source code, which is a minus one.
[2842.34 → 2843.18] In that case, it's clear.
[2843.36 → 2845.46] You're not iterating or having an off by one.
[2845.54 → 2846.28] You mean that.
[2847.14 → 2847.32] Right.
[2847.44 → 2850.42] So you couldn't use it as a variable and count backwards through them.
[2850.52 → 2854.22] Because that's the other thing in Ruby you could do is you could loop backwards.
[2854.60 → 2855.60] That's silly, really.
[2856.06 → 2857.74] So yeah, actually a literal.
[2858.24 → 2860.72] So it has to be spelled out.
[2860.98 → 2861.40] Right.
[2861.64 → 2864.48] I'll take that compromise if it would convince you.
[2864.48 → 2868.02] But it's an interesting point, this wraparound.
[2868.14 → 2869.18] Johnny, we're not doing this one.
[2869.30 → 2869.92] What's the matter?
[2871.14 → 2871.48] What's the matter?
[2871.62 → 2875.24] Next thing you're going to, you probably will have loaded up.
[2875.50 → 2877.04] It's like, you know, you want method missing.
[2877.34 → 2878.02] Method missing.
[2878.26 → 2878.64] Method missing.
[2878.64 → 2879.28] From Ruby.
[2882.04 → 2883.38] Oh, method missing.
[2883.94 → 2885.40] Don't you miss method missing?
[2886.60 → 2888.22] I've built some magic things.
[2888.28 → 2890.46] Natural things happen with method missing.
[2891.24 → 2893.40] Oh, but yeah, I don't think.
[2893.40 → 2903.10] Yeah, for those who don't know, in Ruby you can define something that runs in case someone is trying to use something that doesn't exist.
[2903.70 → 2910.28] And basically it allows you to build a very simple shell, interactive shell in Ruby by just defining that method missing.
[2910.74 → 2915.70] And that is one of the best and worst features of Ruby, I would say.
[2915.86 → 2916.04] Yeah.
[2916.04 → 2916.44] Yeah.
[2917.44 → 2919.64] It's kind of amazing.
[2919.88 → 2928.64] I mean, literally, it's like having a struct with methods and another method called method missing that gets called if you call anything on that.
[2928.78 → 2932.44] So obviously that, by the way, that was not what I was advocating for.
[2932.54 → 2935.34] Johnny, as a joke, said that that's what I was advocating for.
[2936.24 → 2937.86] It's that for sure is too magic.
[2938.06 → 2942.40] Imagine, and this happened to me, you just do a typo, and it's just not an error.
[2942.40 → 2945.20] It's just like, sure, keep going.
[2945.56 → 2946.54] No probs.
[2946.74 → 2947.60] No problem here.
[2947.96 → 2948.36] Probs.
[2948.52 → 2949.80] I want it to say probs.
[2950.28 → 2950.92] Like, yeah.
[2952.42 → 2954.90] That's not quite the same as the minus one thing.
[2955.18 → 2959.42] But I don't know, Daniel, you might have to, it's not a casting vote.
[2959.58 → 2961.22] I've been well-intrigued defeated.
[2961.78 → 2962.06] Yeah, break the tie.
[2962.06 → 2962.34] There's no tie.
[2962.52 → 2963.56] I'm absolutely defeated.
[2963.66 → 2965.10] Daniel's like, what is wrong with these people?
[2965.10 → 2967.14] What do you reckon?
[2967.82 → 2972.06] I was actually reading an old proposal again because this idea has been proposed before.
[2973.36 → 2974.08] The method missing?
[2974.30 → 2974.98] That's a great idea.
[2975.28 → 2975.56] No.
[2976.40 → 2976.84] What?
[2977.10 → 2978.28] What is the method missing?
[2979.34 → 2981.12] The negative index thing.
[2981.46 → 2983.06] Yes, the negative index one.
[2983.24 → 2987.22] So it's issue number 3, 3, 3, 5, 9, if anybody wants to look into it.
[2987.30 → 2990.22] It's rejected, which is why we didn't consider it.
[2990.40 → 2992.32] But there were some good points in that thread.
[2992.32 → 2996.52] But essentially, the main argument against a proposal was what Roberto said, which is,
[2996.92 → 2999.24] what if you've got an index variable, and it happens to go negative?
[2999.84 → 3001.30] And then you wouldn't panic.
[3001.60 → 3002.70] You would do something weird.
[3003.22 → 3010.12] And then people said, what about doing Len minus something instead of having to do Len of the slice minus something?
[3010.88 → 3017.50] And that seemed to be like the most reasonable option, but I don't think it gained enough traction to keep the proposal open.
[3019.06 → 3019.78] I see.
[3019.78 → 3023.44] So inside the square brackets, you'd say like Len minus one.
[3023.88 → 3027.14] And you don't have to say Len brackets, then the variable again.
[3027.98 → 3030.68] It's kind of like inferring what you mean.
[3031.00 → 3034.74] Although sometimes you might mean a different length of a thing, I guess.
[3035.46 → 3040.82] And we're just back to being explicit is better than magic, as usual.
[3041.78 → 3045.82] Can't have nice things in Go because they're too magic.
[3046.50 → 3047.46] All right.
[3047.58 → 3048.92] Is that a definite no then, everyone?
[3048.92 → 3053.14] In that discussion, I saw that people rejected the literal thing.
[3053.78 → 3056.98] Someone proposed the same idea I had, which is, if it is a literal, it's fine.
[3057.22 → 3059.30] If it is not, it's not.
[3059.30 → 3061.14] And what was the rejection of that based on?
[3061.18 → 3062.20] It doesn't click with me.
[3064.14 → 3065.58] I'm literally reading out of it.
[3065.58 → 3066.10] That's subjective.
[3066.64 → 3068.54] People say, it doesn't click with me.
[3068.62 → 3069.26] Okay, fine.
[3069.44 → 3069.84] Okay.
[3070.98 → 3071.48] Fair enough.
[3071.48 → 3088.02] This episode is brought to you by our friends at Source graph.
[3088.42 → 3091.28] Source graph is code search for every developer and team.
[3091.28 → 3095.20] And in this segment, I'm talking with Bing Liu, co-founder and CTO of Source graph.
[3095.56 → 3098.72] And he's sharing exactly how code search works and how it will work for you and your team.
[3099.08 → 3103.34] So, Bing, I want you to share exactly what code search is and how teams can use it.
[3103.34 → 3113.44] So, Adam, I think the best way to describe Source graph is that it's this single search and exploration tool that encompasses the entire universe of code that you might care about.
[3113.64 → 3120.34] And that includes all the code inside your organization, code written by other teams, as well as code that might be external to your organization.
[3120.66 → 3122.76] For example, open source dependencies that you're pulling in.
[3122.76 → 3136.98] So, it's this single portal, this single search box that lets you type in a string literal or a regex pattern and instantly search across all that code and jump to the specific points in that code that you're interested in learning about.
[3136.98 → 3145.10] And then it becomes this interface that allows you to easily navigate and build up a mental model of how that part of code works.
[3145.10 → 3155.00] So, whether it's trying to find a needle in a haystack that you're concerned about or trying to find examples of how to use a particular unfamiliar library or package.
[3155.40 → 3160.70] Or maybe you just want to jump to a bunch of places in code that you can then link to and discuss with teammates.
[3161.08 → 3170.08] And this is all in the service of eventually getting back into your editor so that you have all the context, all the information that you need to know about the area of code that you're modifying.
[3170.08 → 3178.28] And get back into that flow state where you're just coding at the speed of light, and you feel like you're making rapid progress towards that bug fix or that feature that you're currently building.
[3178.78 → 3179.02] All right.
[3179.04 → 3187.28] If code search powered by Source graph sounds like something you and your team can use, head to info.sourcegraph.com slash changelog and click the button that says try Source graph now.
[3187.52 → 3190.60] You can install it locally, deploy it to a server or to a cluster.
[3191.00 → 3194.24] They have a quick start guide that takes less than five minutes to install Source graph using Docker.
[3194.42 → 3196.08] So, it's too easy to give it a try.
[3196.08 → 3199.74] Again, head to info.sourcegraph.com slash changelog.
[3200.08 → 3220.94] That's the thing with all these proposals, right?
[3221.08 → 3222.64] We don't have an objective.
[3222.78 → 3224.00] We have measuring readability.
[3224.00 → 3226.38] We all have hunches, right?
[3226.82 → 3232.70] And ideally, the more experienced you are as a developer, the better those hunches get.
[3233.14 → 3234.28] But it's hard.
[3234.80 → 3240.24] Like when I sit down to pair with a more junior developer, every time I feel like I have to rely on, well, because it's more readable.
[3240.98 → 3243.28] Then in the back of my head, I'm thinking, is there a better way?
[3243.64 → 3246.12] Like, how do I explain this, right?
[3246.14 → 3249.54] Like, how do I transfer this bit of intuition or wisdom?
[3249.54 → 3253.80] You know, like, is there a better way to actually explain this, right?
[3253.86 → 3256.24] So, simply saying it's more readable, less readable.
[3256.56 → 3258.20] Those are all what we think.
[3258.46 → 3259.20] Those are ideas.
[3259.28 → 3260.50] We don't have a way of measuring that.
[3260.74 → 3261.80] So, yeah.
[3262.10 → 3262.26] Yeah.
[3262.40 → 3264.50] And it also depends on where it comes from.
[3264.66 → 3267.48] The other day I was doing a readability review on some code that was submitted.
[3267.48 → 3273.62] And the person, which was completely new to go, called every receiver for every method this.
[3274.26 → 3276.60] So, basically, every receiver was called this.
[3276.96 → 3283.30] And I said, well, you should give it a more meaningful name, like S, because the type started with S.
[3283.50 → 3285.32] And he was like, how is that more readable?
[3285.56 → 3289.00] Like, please explain to me what are you trying to convey here?
[3289.26 → 3293.16] I was like, so, okay, where do I start?
[3293.16 → 3299.04] It's not that easy, because for me, calling that type, which was called something like sorted something,
[3299.50 → 3305.40] calling it S, R, which was that something, would have been more meaningful than calling it just these,
[3305.48 → 3309.06] because this requires me to go back to the function definition and see what it is,
[3309.30 → 3310.62] because maybe I lost context.
[3310.94 → 3312.46] But it was a long discussion.
[3312.92 → 3313.86] Let's put it this way.
[3314.24 → 3317.68] So, readability really changes depending on your background and your expectations.
[3318.28 → 3320.28] Yeah, I think there's a good lesson in that,
[3320.28 → 3324.70] because we can get a little bit dogmatic about things in Go.
[3324.78 → 3327.82] And we can be like, this is the way to do it.
[3327.88 → 3329.64] And we feel very strongly about that.
[3330.26 → 3332.18] And I'm a little bit guilty of this,
[3332.20 → 3335.02] because I've done talks at conferences that are available on YouTube,
[3336.10 → 3344.44] where I'll show idiomatic things and different idioms and patterns that are good and things.
[3344.44 → 3348.14] Although I always try and make the point that, you know,
[3348.48 → 3350.46] it should be taken in the right kind of spirit.
[3350.78 → 3355.72] And I think we should be a little bit more open when we kind of consider these things.
[3355.90 → 3359.80] We can sometimes be a little bit closed off, like these are, you know,
[3359.82 → 3361.26] this is the way to do it and that's it.
[3361.32 → 3367.56] And we should watch that, because that can be very exclusive if we go down that road, can't it?
[3367.80 → 3368.12] Mm-hmm.
[3370.46 → 3371.40] One last one.
[3371.40 → 3374.98] Oh, look at that.
[3375.06 → 3375.54] We're at the time.
[3375.84 → 3378.18] Yeah, this has been a cracking show.
[3378.58 → 3382.48] Remember, you have to let Jared know that he has to come back on it.
[3382.48 → 3384.20] Yeah, and he's either going to do it or he's not.
[3384.34 → 3387.06] If he doesn't do it, I'll just play it live.
[3387.66 → 3388.22] We'll do it live.
[3388.50 → 3390.38] You just grab the guitar and start going out.
[3391.84 → 3392.88] Shall we clap again?
[3395.22 → 3395.98] What's it get, Jared?
[3396.52 → 3398.58] It's not like a dog or a horse.
[3398.58 → 3400.40] It just responds to claps.
[3400.40 → 3403.02] He doesn't respond to them.
[3403.14 → 3404.06] That's the annoying thing.
[3404.36 → 3407.06] I wish he was more like a horse in a lot of ways.
[3407.22 → 3407.48] Yeah.
[3407.64 → 3407.94] Okay.
[3408.16 → 3411.88] Well, as I was saying before I was rudely interrupted, it's that time again.
[3412.26 → 3414.94] It's time for Unpopular Opinions.
[3419.06 → 3420.66] Unpopular Opinions.
[3420.72 → 3421.56] You what?
[3421.66 → 3423.36] I actually think she'd probably leave.
[3423.36 → 3428.36] Unpopular Opinions.
[3428.36 → 3428.80] Yeah.
[3434.62 → 3435.10] Okay.
[3435.60 → 3437.50] I'm going to go first this time.
[3437.84 → 3439.68] This is my unpopular opinion.
[3439.90 → 3445.84] And this one hurts me to say because people have done, like, lovely things for me.
[3446.10 → 3448.76] And this is now going to throw it back in their faces.
[3448.94 → 3449.30] Are you ready?
[3449.30 → 3453.22] I think we should stop doing conference swag.
[3453.76 → 3454.50] It's landfill.
[3455.76 → 3460.42] I mean, give people more tickets or something or licenses for software or something.
[3461.70 → 3463.32] No more conference swag.
[3463.70 → 3464.50] What about t-shirts?
[3465.50 → 3466.86] T-shirts are okay because they're useful.
[3467.40 → 3467.48] Yeah.
[3467.48 → 3468.52] I'm actually wearing one now.
[3468.52 → 3469.08] Yeah, exactly.
[3469.46 → 3470.48] I was about to go there.
[3471.32 → 3471.90] T-shirts.
[3471.90 → 3472.24] T-shirts.
[3472.56 → 3473.36] Except t-shirts.
[3473.74 → 3473.94] Yeah.
[3474.00 → 3474.86] T-shirts are great.
[3474.98 → 3475.30] That's true.
[3475.46 → 3479.24] I mean, you know, the other stuff that, like, it's lovely.
[3479.58 → 3484.08] And people go to such great lengths and a lot of effort goes into it.
[3484.26 → 3486.82] And this is why I was really reluctant to say this.
[3486.82 → 3489.82] But, yeah, it's a lot of garbage.
[3490.70 → 3493.66] What about, like, the little plushy gophers and stuff?
[3494.48 → 3502.02] I mean, those little things, we don't know if they're going to, at some point, come to life and try and get us.
[3502.38 → 3502.90] Do you see this?
[3502.98 → 3504.30] He's like, he's looking at us.
[3504.38 → 3504.74] Exactly.
[3505.00 → 3505.44] Right.
[3506.12 → 3508.86] And also, Daniel was holding up one.
[3509.04 → 3510.94] Daniel was creeping up the screen.
[3511.30 → 3511.82] Yeah, there you go.
[3512.42 → 3515.02] But, yeah, it's like, I have this block from Gopher Con UK.
[3515.02 → 3517.24] And I love this.
[3517.42 → 3518.94] Like, this kind of stuff is fine.
[3519.00 → 3521.90] But stuff like a squeeze bowl, I'm never going to use that.
[3522.60 → 3524.20] Or, like, fridge magnets.
[3525.36 → 3528.40] My fridge is in a wooden thing.
[3528.64 → 3529.70] I can't use this.
[3529.78 → 3530.90] You've got a wooden fridge?
[3531.30 → 3534.06] No, it's inside something to make it look like a cardboard.
[3534.06 → 3536.52] Oh, I thought it was a wooden fridge, like, from the olden days.
[3536.52 → 3537.54] You know, I put wood in it.
[3537.54 → 3538.66] These magnets are not good.
[3538.74 → 3539.60] You have to hammer them in.
[3539.96 → 3542.08] No, it's like, I have to put wood in it.
[3542.26 → 3544.34] It has to burn, you know, to produce it.
[3545.02 → 3546.58] Come bust in me.
[3546.82 → 3547.46] Oh, that's classic.
[3547.60 → 3548.90] So retro of you, Roberto.
[3549.08 → 3549.24] Right.
[3549.42 → 3549.78] Steampunk.
[3550.64 → 3551.30] Yeah, very.
[3552.74 → 3553.10] Yeah.
[3553.28 → 3553.80] I don't know.
[3553.82 → 3554.26] What do you think?
[3554.28 → 3555.00] Is it too harsh?
[3555.20 → 3557.58] What you're saying is you want more useful swag.
[3558.14 → 3558.46] Okay.
[3558.78 → 3558.98] Yeah.
[3559.08 → 3559.88] Actually, good point.
[3560.66 → 3560.96] Yeah.
[3561.16 → 3561.88] Actually, yeah.
[3562.40 → 3562.92] I don't know.
[3563.16 → 3564.58] People love it as well, don't they?
[3564.64 → 3567.52] So it's like, I really do feel like a spoiled sport a little bit.
[3568.52 → 3569.24] Daniel, what do you reckon?
[3569.56 → 3570.92] Do you like conference swag, mate?
[3570.92 → 3575.98] I used to be big into free t-shirts and swag t-shirts and t-shirts that would say like
[3575.98 → 3576.88] go or whatever.
[3577.28 → 3579.14] These days, not really anymore.
[3579.36 → 3582.00] So I tend to agree that there's too much swag.
[3582.26 → 3584.12] I feel like a little bit of swag would be fine.
[3584.74 → 3585.58] But yeah.
[3585.62 → 3587.30] Too cool now, aren't you, to wear go t-shirts?
[3588.30 → 3590.80] You know, I just wear like literally white t-shirts.
[3591.08 → 3591.16] Yeah.
[3591.32 → 3592.02] So minimalist.
[3593.94 → 3594.38] Yeah.
[3594.38 → 3597.04] You are an undercover minimalist, my friend.
[3597.96 → 3599.66] Current background notwithstanding.
[3602.44 → 3602.92] Yeah.
[3603.56 → 3606.04] No, I like to be able to see all Daniel's clothes.
[3606.60 → 3609.04] It's a bonus for anyone watching live on YouTube.
[3609.96 → 3613.68] You don't get to see those clothes if you're listening on the podcast.
[3613.84 → 3614.16] That's true.
[3614.56 → 3617.64] You need more colour though in your wardrobe, I'd say, Daniel.
[3617.96 → 3619.36] Oh, brutal.
[3619.36 → 3624.60] You can do some more go t-shirts, Daniel, actually.
[3626.98 → 3629.88] Yeah, Daniel, have some more variety in your t-shirts.
[3630.64 → 3632.90] I'll wear a hideous free t-shirt next time.
[3633.12 → 3633.50] I promise.
[3635.32 → 3635.76] Yeah.
[3636.90 → 3639.02] What's the best swag you've ever had?
[3639.44 → 3642.56] One time I was at a conference, and they gave out hand sanitizer.
[3643.26 → 3644.40] Now you're talking.
[3645.48 → 3647.54] Was this like immediately before COVID?
[3647.74 → 3648.74] No, it wasn't, actually.
[3648.74 → 3650.64] Especially now, it'd be great, wouldn't it?
[3650.76 → 3652.38] They were very forward-looking.
[3653.30 → 3655.32] Like that was almost an oracle.
[3656.00 → 3658.08] Germs have been around for ages, Roberto.
[3658.46 → 3661.16] No, I don't know of any germs before 2020.
[3661.66 → 3661.82] Sorry.
[3662.26 → 3662.40] Yeah.
[3664.14 → 3669.52] Once at a conference, they were giving out rechargeable batteries to charge your phone with.
[3669.78 → 3671.96] Because supposedly you're going around all day with your phone.
[3672.32 → 3677.24] So I was thinking, wait, now I need to remember to charge my second battery so I can charge my first battery.
[3677.24 → 3678.24] That's kind of...
[3679.24 → 3681.98] Can you charge it from your phone?
[3682.32 → 3683.06] Can you do it that way?
[3683.20 → 3685.40] If it runs out, you can just charge it with your phone?
[3686.14 → 3688.16] No, this was before the USB-C days.
[3688.30 → 3690.92] So it was like micro USB that would only go one way.
[3691.22 → 3691.24] No.
[3692.56 → 3693.62] I don't know, Pablo opinion.
[3694.02 → 3694.70] What is it, Johnny?
[3695.70 → 3696.44] You want to know what it is?
[3696.74 → 3697.60] Yes, please.
[3697.84 → 3698.56] You may not like it.
[3698.72 → 3700.18] Do you really want to know what it is?
[3700.18 → 3701.64] Is it about British people?
[3703.64 → 3704.60] Now it is.
[3704.86 → 3705.46] Now it is.
[3706.14 → 3707.26] It's like...
[3707.26 → 3707.74] Yeah.
[3710.06 → 3710.50] Yeah.
[3710.82 → 3711.74] But no, seriously.
[3711.96 → 3717.30] I do think that we in the Go community can suffer from a little bit of groupthink.
[3718.30 → 3722.72] The whole thing about idiomatic Go, what does it mean to write idiomatic Go?
[3723.08 → 3728.86] Again, to go back to the stuff that I touched on earlier when I'm pairing with somebody, the
[3728.86 → 3730.78] stuff that Roberta mentioned earlier.
[3731.32 → 3735.14] Like some things you can't really put a number or be specific about it.
[3735.18 → 3739.60] You kind of have to get, well, do it this way because that's kind of the way we do it.
[3739.60 → 3747.70] Now, there's some wisdom that can be gotten from the crowd when a bunch of people try something
[3747.70 → 3753.70] and they all discuss and exchange ideas and realize, okay, doing it this way more often
[3753.70 → 3755.28] than not will yield some benefits.
[3755.42 → 3759.12] Doing it that way more often than not will yield some troublesome things.
[3759.52 → 3760.70] There is value in that.
[3760.70 → 3768.72] But I think sometimes we can sort of like try so hard to sort of go with the pack that
[3768.72 → 3771.30] we stop thinking for ourselves, right?
[3771.52 → 3776.42] I've come across folks that are trying to learn Go that are beating themselves up.
[3776.52 → 3780.16] They have a working solution, but they're beating themselves up because their code doesn't
[3780.16 → 3784.00] quite look like what a Go developer's code is supposed to look like, right?
[3784.16 → 3787.04] They're like, oh, I have a working solution.
[3787.36 → 3788.66] Yeah, it might be a little bit of Booby.
[3788.66 → 3793.22] It might be a little bit of a GABA, GABA, you know, a little bit of GASTON.
[3793.62 → 3796.50] Yeah, we all go through those phases.
[3797.92 → 3798.70] GABA script.
[3801.18 → 3802.00] Objective-C.
[3802.48 → 3803.12] Oh, no.
[3805.66 → 3806.74] All that, right?
[3806.90 → 3810.58] So we kind of have to go sometimes, you know.
[3810.94 → 3812.74] You know, Johnny, I agree.
[3813.04 → 3816.62] And actually, my unpopular opinion was somewhat related to this.
[3816.62 → 3819.78] So I don't know how unpopular this is now.
[3821.36 → 3826.10] So basically, my opinion is the standard library defines a lot of interfaces.
[3826.94 → 3831.20] And every time someone comes up with an improvement, people say, yeah, but we don't know who implements
[3831.20 → 3831.56] them.
[3831.68 → 3832.92] So we cannot change them.
[3833.08 → 3835.44] Like we are kind of stuck with some of those interfaces.
[3835.44 → 3840.86] For example, the HTTP handler interface allows you to write a slice of bytes.
[3842.20 → 3844.58] And that is, I work in security.
[3844.74 → 3845.38] That is a nightmare.
[3845.78 → 3847.66] Like I've tried to secure that.
[3847.74 → 3849.16] There is no way to secure that.
[3849.16 → 3856.40] And when I try to propose to write something that would change the interface to something
[3856.40 → 3858.48] more secure, that would look the same.
[3858.58 → 3860.84] Like you still write something to it.
[3861.04 → 3863.72] And it looks as close as possible to the standard library.
[3863.84 → 3869.56] But in a secure way, I got so much resistance and friction and rejections.
[3869.56 → 3875.80] Like I think if there is a good reason to wrap or hide the standard interface with something
[3875.80 → 3877.98] of a higher level, why not?
[3878.18 → 3881.88] There are so many frameworks out there that are not used because people say, yeah, but
[3881.88 → 3885.58] I don't want to use this because it's not using the standard interface.
[3885.92 → 3888.12] Maybe it makes your code much easier to read.
[3888.64 → 3889.80] Why not go for that?
[3890.28 → 3892.38] So that is my unpopular opinion.
[3892.38 → 3898.38] Well, remember, we test these by tweeting them out from GoTimeFM.
[3898.98 → 3899.34] All right.
[3899.44 → 3901.30] We put a poll on it, and we ask people.
[3901.42 → 3902.28] So we find out.
[3902.44 → 3903.64] We do that science.
[3903.82 → 3905.24] And that is science.
[3905.80 → 3906.00] Okay.
[3907.00 → 3909.30] And we find out if they're unpopular or not.
[3909.52 → 3911.28] So we'll test these.
[3911.94 → 3915.20] Yeah, Johnny, on your unpopular opinion, I completely agree.
[3915.40 → 3921.36] We do always have to be more understanding and accepting and flexible for sure.
[3921.36 → 3926.80] But, you know, like some patterns, even if they're just, they're just memes, really, they're
[3926.80 → 3931.36] just around because there were ideas that enough people liked and enough people now say
[3931.36 → 3932.46] that that's how we do it.
[3932.80 → 3938.52] There is an advantage in having code that all kind of looks very similar.
[3938.76 → 3943.94] When you jump into a repo that you didn't write, and you read the code, and it feels like
[3943.94 → 3950.58] you could have written that, that is a massive kind of shortcut to getting stuck in or understanding
[3950.58 → 3952.92] and working with that code.
[3953.54 → 3958.88] And the other thing is there is such thing as good taste, which you can't really measure.
[3959.08 → 3963.24] It is subjective, but it exists, doesn't it?
[3963.64 → 3965.06] Doesn't good taste exist?
[3965.92 → 3968.58] So, yeah, I don't know if, does it?
[3970.02 → 3970.48] Does it?
[3970.48 → 3973.76] You were looking at Daniel when you said that.
[3974.06 → 3975.66] Are you like throwing some shade?
[3975.92 → 3976.66] I like his clothes.
[3977.56 → 3979.00] No, I like Daniel's clothes.
[3979.60 → 3982.20] Actually, to be fair to him, look at those clothes.
[3982.54 → 3984.74] They are, they are very...
[3984.74 → 3986.90] So much judgment on this podcast.
[3987.44 → 3987.94] From you.
[3987.94 → 3988.28] Goodness.
[3988.68 → 3990.34] How did we end up here?
[3990.42 → 3991.38] Like, what happened?
[3991.38 → 3994.42] It's the internet, isn't it?
[3994.80 → 3995.34] It's the internet.
[3995.58 → 3998.08] Eventually, everything, everything turns back.
[3998.08 → 3998.56] Evolves.
[3999.06 → 3999.38] Yeah.
[4000.70 → 4004.32] Johnny, you said something earlier and forgot and said you're going to defer it.
[4004.48 → 4005.78] We're about to close the show.
[4005.90 → 4007.72] So now's the time all the defers have to happen.
[4007.72 → 4009.42] So do you want to do it?
[4010.78 → 4013.56] No, probably something like, you know, go thump all the things.
[4014.18 → 4016.38] Like Roberto says, go thump things.
[4016.60 → 4017.98] I love that on a Swank t-shirt.
[4018.48 → 4019.56] Go thump all the things.
[4019.56 → 4019.88] Yeah.
[4020.34 → 4021.92] Well, we are over time.
[4022.24 → 4024.32] That is all the time we have for today.
[4024.70 → 4026.14] Thank you so much for joining us.
[4026.36 → 4030.92] It's early Johnny Portico, Roberto Claps and Daniel Marti.
[4031.20 → 4032.36] Thank you very much.
[4032.72 → 4033.88] And we'll see you next time.
[4034.18 → 4034.64] Bye.
[4039.98 → 4047.28] You can support our work and help ensure that Go Time continues into the future with a Changelog++ membership.
[4047.28 → 4055.12] Ditch the ads, get closer to the metal, and directly contribute to all Changelog podcasts at changelog.com slash plus.
[4055.44 → 4058.62] Once again, that's changelog.com slash plus.
[4058.82 → 4059.30] Check it out.
[4059.30 → 4065.58] This episode was hosted by Matt Refer, produced by Jared Santo, with music by Break master Cylinder.
[4066.20 → 4068.44] Go Time is brought to you by our awesome sponsors.
[4068.76 → 4071.86] Special thanks to Vastly, Launch Darkly, and Linde.
[4072.18 → 4080.12] Next time on Go Time, John Calhoun is joined by the team at Clever to hear all about how they started using Go at the education-focused startup.
[4080.52 → 4082.84] That won't be hitting your podcast feed next week.
[4082.84 → 4112.82] GoTime.com
[4112.84 → 4124.54] Wait, so did we skip Daniel's unpopular opinion?
[4124.76 → 4125.94] Something tells me we skipped that.
[4126.20 → 4126.66] Did we, Daniel?
[4126.76 → 4127.64] Yeah, but it's fine.
[4127.94 → 4128.90] I can just say it for next time.
[4129.84 → 4130.74] You'll have to come back, mate.
[4130.78 → 4131.66] We just ran out of time.
[4132.16 → 4132.72] We're way over.
[4133.06 → 4133.76] You'll have to come back.
[4133.78 → 4136.36] Yeah, come back just to deliver your unpopular opinion.
[4136.48 → 4137.28] It better be a good one.
[4138.24 → 4139.96] We're going to have a whole show just for that.
[4141.02 → 4141.38] Yeah.
[4142.44 → 4143.02] Could do that.
[4143.14 → 4145.86] I think we should address why Matt would prefer to replace me with a horse.
[4146.76 → 4147.86] Oh, you were listening.
[4149.12 → 4150.76] Not replace you with one, mate.
[4150.88 → 4151.74] Oh, augment?
[4153.30 → 4154.36] Yeah, like a centaur.
[4154.74 → 4155.66] It's not like a centaur.
[4155.78 → 4156.82] It's like a centaur. You can still do your programming.
[4157.30 → 4158.48] But you've got a horse's back.
[4159.18 → 4160.18] It's like you're here faster.
[4160.18 → 4162.96] I hope you're not attached to your legs.
[4163.20 → 4164.20] Someone is writing in the chat.
[4164.50 → 4168.26] Actually, Bill is writing in the chat that Daniel doesn't have any unpopular opinions.
[4168.64 → 4169.46] Want to prove them wrong?
[4170.10 → 4171.80] Dan, if you want to share, I'll splice it.
[4172.00 → 4172.54] I'll splice it.
[4172.56 → 4173.46] Yeah, he'll splice it.
[4173.66 → 4173.92] Do it.
[4174.10 → 4174.34] Do it.
[4174.36 → 4175.54] Or I'll put it in after the outro.
[4175.72 → 4176.56] Either way, it'll get in.
[4176.62 → 4176.86] Hang on.
[4176.90 → 4178.52] If we're splicing, if we're splicing.
[4178.54 → 4179.28] No, not for you.
[4180.06 → 4181.42] We have the centaur first.
[4182.74 → 4184.12] I'd love you as a centaur.
[4184.64 → 4186.08] I don't splice anything for you, Matt.
[4188.64 → 4189.08] Slice.
[4189.08 → 4191.18] I'll slice things out, but I won't splice things in.
[4191.24 → 4191.86] Go ahead, Daniel.
[4193.06 → 4198.14] So my unpopular opinion is going to be the vast majority of projects, including open source,
[4198.32 → 4201.14] should use monorepos, for example, on GitHub.
[4201.48 → 4206.94] I see far too many projects that have a sprinkling of 30 repos on GitHub.
[4207.88 → 4209.74] And oftentimes it's unnecessary.
[4210.22 → 4215.18] I feel like everybody should begin with a single repo and think very, very hard before splitting
[4215.18 → 4215.58] that up.
[4215.96 → 4218.12] Especially because it does have some advantages.
[4218.12 → 4222.78] Like if you have some component that you think many other people are going to want, you might
[4222.78 → 4224.96] want to consider living with the downsides.
[4225.26 → 4227.68] But do you really think that many people are going to use it?
[4228.08 → 4230.90] I don't think so, at least in general, or at least by default.
[4230.90 → 4231.94] I agree.
[4231.94 → 4233.88] That one is not unpopular with me.
[4234.18 → 4234.48] No.
[4234.96 → 4239.06] I'm doing a reboot of a project of mine called Bit bar.
[4239.98 → 4241.48] And it's got a website.
[4241.94 → 4242.76] It's an app.
[4242.94 → 4245.16] It has a front end in the app.
[4245.22 → 4245.98] It has a back end.
[4246.04 → 4246.88] It has Go packages.
[4247.12 → 4250.20] It has generation code.
[4250.20 → 4253.02] That is all going to be in a monorepo.
[4253.84 → 4254.80] I completely agree.
[4254.86 → 4256.96] How did you manage to turn this into an advertisement for Bit bar?
[4258.34 → 4259.30] Well, it's just an accident.
[4259.48 → 4260.88] It's just a happy accident for everyone.
[4260.98 → 4261.82] Bit bar is still available.
[4262.92 → 4264.70] Yeah, you can put anything in your macOS menu bar.
[4264.70 → 4266.16] You don't like to list any more of its features.
[4267.06 → 4267.46] Yeah.
[4267.92 → 4268.60] In defence.
[4268.76 → 4269.68] I don't know what happened.
[4269.74 → 4274.14] I was just saying you can put the output of any script or executable in your macOS menu bar.
[4275.08 → 4277.12] And, you know, that's all I'm saying.
[4277.38 → 4277.62] I don't know.
[4277.78 → 4278.22] That's all I'm saying.
[4278.22 → 4279.76] It just ran away from there.
[4280.86 → 4288.16] No, but the thing is, like, when you have a pull request, often you're changing things across the entire stack.
[4288.40 → 4289.00] Very often.
[4289.24 → 4295.18] To have that all go in one go is great, including documentation.
[4295.66 → 4301.22] You know, it could be front end JavaScript changes and server side changes at the same time.
[4301.34 → 4303.32] All in one logical unit.
[4303.32 → 4303.68] Yeah.
[4303.80 → 4308.82] I mean, monorepos for the win is my motto.
[4309.30 → 4311.66] It's not even just about Git or repos.
[4311.76 → 4312.78] It's also about modules.
[4313.40 → 4319.02] Oftentimes you find projects that produce, like, 30 modules, and you think this could all be a single module.
[4319.16 → 4321.06] It might be big, but does that really matter?
[4321.46 → 4323.96] It's not like I have to link in every single package from the module.
[4325.58 → 4325.98] Yeah.
[4326.26 → 4327.90] And also, I'm in favour of monorepo.
[4327.90 → 4331.26] I mean, at work, I only use one repo for everything.
[4331.70 → 4333.70] And that works fine so far.
[4334.76 → 4336.28] How long does it take to check out?
[4336.96 → 4337.54] Tooling, though.
[4337.62 → 4340.04] You need tooling for that to work well.
[4340.04 → 4341.20] You don't check it out.
[4341.50 → 4342.66] Not the entire thing.
[4343.62 → 4346.38] I mean, I don't know how many billion lines of code.
[4347.30 → 4349.40] I think I don't check it out.
[4350.80 → 4351.82] Well, why stop there?
[4351.90 → 4356.84] Why don't you just put, you know, GitHub.com slash the repo, and we'll just all put our code in one.
[4357.44 → 4357.84] Monorepo.
[4358.40 → 4359.20] I mean, if it's better.
[4359.92 → 4365.40] Git doesn't, I mean, Git is not very well-fitted for that, I would say.
[4366.16 → 4374.28] Well, it's funny because there's no such thing as pull requests across multiple repos in GitHub, for example.
[4374.72 → 4375.02] Right.
[4375.12 → 4376.02] It's not a thing, right?
[4376.88 → 4377.44] That could be.
[4377.44 → 4377.72] So you cannot.
[4377.92 → 4378.22] Right.
[4378.22 → 4384.34] If you want to change your API without breaking users, one solution is to fix your users when you change the API.
[4384.34 → 4391.64] But you can't because you cannot, your users are not able to sync on a single commit with you.
[4392.20 → 4393.62] So that's a pity.
[4395.36 → 4396.50] Fix your users.
[4396.76 → 4398.00] There's something there you can do with that.
[4398.00 → 4398.78] You're holding it wrong.
[4398.94 → 4399.06] Yeah.
[4399.28 → 4400.40] Fix your users.
[4400.92 → 4401.06] Yeah.
[4401.24 → 4403.72] It's not Roberto's code that's broken.
[4404.18 → 4406.06] It's the humans trying to use it that are broken.
[4406.06 → 4408.16] No, it's different.
[4408.54 → 4414.08] Let's say that if you change an API, you should be responsible to fixing all the code that you broke for that change.
[4414.08 → 4416.02] So you'll think twice before doing that.
[4416.68 → 4417.64] That's the approach.
[4418.66 → 4418.86] Yeah.
[4420.12 → 4421.20] Yeah, I could see that.
[4421.82 → 4423.44] It's a good, good and popular opinion.
[4423.62 → 4424.44] Again, we'll test it.
[4424.70 → 4426.14] I don't think it's going to be very unpopular.
[4426.34 → 4427.22] Well, it is, isn't it, actually?
[4427.88 → 4430.92] Especially like there's a lot of projects that.
[4430.98 → 4434.44] You don't see it much in practice, but I think people will agree with it.
[4434.44 → 4438.50] I think if anybody agrees with it, then they have to fix their splattering.
[4439.50 → 4439.78] Ooh.
[4440.30 → 4441.98] So that would have been a more unpopular opinion.
[4442.10 → 4444.86] You should have said, I think all these people need to fix their repost.
[4444.98 → 4446.08] Upping your stakes.
[4446.80 → 4447.10] Yeah.
[4447.92 → 4449.02] Now you're getting unpopular.
[4449.32 → 4450.94] Put your effort where your mouth is.
[4455.72 → 4456.70] Can you imagine?
[4457.10 → 4459.12] We all had to deliver on the things we promise.
[4460.50 → 4460.86] Anyway.
[4461.50 → 4462.64] That's why I don't make promises.
[4463.88 → 4465.80] Too much of a failure to promise things.
[4465.80 → 4467.54] Game on.
[4467.54 → 4467.60] Game on.
