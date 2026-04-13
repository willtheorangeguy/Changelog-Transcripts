[0.00 → 3.28] One other thing that we have not mentioned so far is documentation.
[3.82 → 7.94] And that's like another important thing to make it so that you can actually hand off
[7.94 → 12.56] a project from one engineer to another or have multiple engineers working on it so that
[12.56 → 16.86] one doesn't have to kind of mind read for the previous person writing the code.
[16.98 → 21.12] Having like decision documents when an architectural decision is being made, all those types of
[21.12 → 24.36] things help to set context for the next person.
[24.52 → 28.64] So the next person isn't just like, let's rewrite this for the sake of rewriting this
[28.64 → 29.64] or whatever.
[29.64 → 45.92] This is JS Party, your weekly celebration of JavaScript and the web.
[45.92 → 49.04] If you're new to the pod, don't forget to subscribe.
[49.40 → 52.02] Head to jsparty.fm for all the ways.
[52.28 → 54.42] And if you're a longtime party animal, thank you.
[54.56 → 55.56] We appreciate you listening.
[55.56 → 59.94] Check out our membership program at changelog.com slash plus.
[60.08 → 64.24] Drop the ads, get bonuses like extended episodes and directly support the show.
[64.66 → 68.84] Thanks to our friends at Vastly for shipping JS Party all around the world to wherever you
[68.84 → 69.14] listen.
[69.30 → 70.98] Check them out at fastly.com.
[71.30 → 71.70] Okay.
[71.98 → 72.96] You know what time it is.
[73.38 → 74.40] It's party time, you all.
[74.40 → 81.42] Hello, JS Party people.
[81.64 → 83.18] Yes, the sound of those beats.
[83.28 → 86.42] And if you're watching on YouTube, those bopping heads going back and forth.
[86.42 → 89.46] That means we are ready for this week's JS Party.
[89.60 → 90.14] I'm K-Ball.
[90.22 → 91.26] I'm your host this week.
[91.56 → 93.46] I'm excited to do this episode.
[93.56 → 95.44] We're going to try some new stuff, which should be fun.
[95.50 → 99.16] But I am joined this week by two of my favourite co-panellists.
[99.50 → 100.42] First off, Allie Spittle.
[100.50 → 101.20] Allie, how are you going?
[101.54 → 102.20] Good, good.
[102.22 → 102.58] How about you?
[103.10 → 104.18] Life is good.
[104.30 → 105.24] I've got my coffee.
[105.36 → 106.88] I'm high energy and ready to go.
[107.18 → 108.38] Nick Needed.
[108.74 → 109.24] Hoi.
[109.60 → 110.06] How's it going?
[110.46 → 111.30] It's going well.
[111.38 → 116.96] Your consistency with hoi is amazing because we have a recording of that, and it sounds just
[116.96 → 117.40] the same.
[117.54 → 120.36] Like, can we, well, I'll try that, and you tell me which one is real.
[120.80 → 121.42] Hoi?
[121.94 → 122.70] Hoi?
[123.06 → 123.48] All right.
[123.72 → 126.02] Maybe not as consistent as I thought, but okay.
[126.02 → 133.76] So we are starting off this week with a new segment and if it works, maybe we'll do this
[133.76 → 134.56] again a few times.
[134.72 → 138.18] So if you're listening, let us know what you think of this segment and we'll try.
[138.30 → 144.82] But this segment is going to be about all the weird things that JavaScript as a language
[144.82 → 145.18] does.
[145.26 → 147.12] So this segment is called WTFJS.
[147.56 → 151.12] And introducing this segment, folks, we were talking about it and we wanted an intro.
[151.12 → 155.66] Now, we have a lot of intros where we got like Matt Refer from Go Time or something to
[155.66 → 155.86] do it.
[155.88 → 157.06] And like, he's really talented.
[157.24 → 161.24] So if you ask him to do an intro, like help play something in the guitar and sing it, folks
[161.24 → 162.96] had me do the intro and this is what you get.
[163.58 → 166.42] If you're WTFJS.
[167.74 → 173.74] So WTFJS about the weird things that is this language we spend so much of our time talking
[173.74 → 174.08] about.
[174.24 → 176.12] Allie, you have a really fun one to share.
[176.16 → 176.82] Do you want to go first?
[177.36 → 177.64] Yeah.
[177.84 → 178.08] Yeah.
[178.20 → 178.28] Yeah.
[178.28 → 178.46] Yeah.
[178.60 → 179.46] I have two.
[179.60 → 180.32] Should we rotate?
[180.32 → 181.70] Yeah, we could rotate.
[181.92 → 182.56] That sounds good.
[182.70 → 182.90] Okay.
[183.16 → 186.14] I should warn folks, we're going to import one of our panellists.
[186.34 → 190.32] He has some great takes on things, and we're just going to reference occasionally.
[190.54 → 194.64] So listen out for some bone skull sound effects as well as we go through here.
[195.86 → 196.26] Great.
[196.34 → 198.56] Because I'll be needing some bleeping for this one.
[198.56 → 207.02] So one of my favourite really weird JavaScript things is that you can actually write anything
[207.02 → 213.62] in JavaScript using only brackets, parentheses, a bang, and a plus sign.
[213.62 → 216.06] So you can write anything in JavaScript with these.
[216.28 → 216.38] What?
[216.38 → 221.60] So if you use combinations of them, you can do anything.
[221.60 → 226.62] So for example, a hello world doing this would be 4,325 characters.
[227.38 → 229.92] So it's definitely not the efficient way of doing things.
[229.92 → 234.64] And it's become kind of an esoteric subset of JavaScript.
[235.14 → 243.38] And it's named JS bleep, inspired by brain bleep, which probably a lot of listeners have
[243.38 → 244.64] heard of.
[244.76 → 248.22] It's esoteric programming language that's only using characters.
[248.92 → 252.08] And you can write the whole entire alphabet with this.
[252.08 → 257.44] So for example, if you wanted to get like an A for an alert, you wanted to do an alert.
[257.96 → 259.28] Aren't alerts like deprecated now?
[259.36 → 262.90] Anyway, if you wanted to write an alert, an array is truthy.
[263.42 → 268.48] So in order to get the word false, you could do bang and then an empty array.
[269.20 → 272.76] You get true by doing bang, bang, and then that empty array too.
[273.44 → 279.96] So you could get the letter A from the word false by getting the first index from the word
[279.96 → 280.56] false.
[281.12 → 287.16] And then you could use the zero index, which is plus and then an empty array.
[287.54 → 290.64] And so it's all really, really, really wild.
[290.86 → 291.48] It makes no sense.
[292.12 → 292.52] Yeah.
[292.72 → 294.38] So you use bang array.
[294.64 → 294.98] Yes.
[295.08 → 298.94] To generate a false because that's the opposite of truthy.
[299.10 → 299.44] Exactly.
[299.72 → 303.24] But then you map it, you make it a string, or you treat it as a string, and you index into
[303.24 → 303.44] it.
[303.48 → 304.36] You treat it as a string.
[304.66 → 308.84] And so you're going to index into it with one, but you don't want to use a number.
[308.84 → 315.18] So you're actually getting one from the array plus one or something.
[315.46 → 315.62] Yeah.
[316.34 → 316.74] Yeah.
[316.96 → 317.00] Yeah.
[317.00 → 317.08] Yeah.
[317.32 → 318.24] You just blew my mind.
[318.58 → 322.22] So you get the number one by doing, let me see.
[322.72 → 323.58] Oh, I see it.
[323.68 → 324.42] I was just playing with this.
[324.48 → 326.42] If you do plus array, you get zero.
[326.84 → 330.86] And if you do plus bang, bang array, you get one.
[331.24 → 332.02] There you go.
[332.14 → 333.80] And then you could add another one, right?
[333.82 → 336.76] So you could do like plus bang, bang array.
[336.76 → 337.16] Yeah.
[337.36 → 337.56] Yeah.
[337.66 → 340.28] So you do plus bang, bang array, plus bang, bang array, you get two.
[340.60 → 341.86] And so now you've got all your numbers.
[342.10 → 344.62] Then you're indexing into false or true.
[345.26 → 345.46] Yeah.
[345.62 → 350.24] Or false in order to get the A for like an alert, for example.
[350.76 → 355.44] And then you could do the same in order to get the L from false for an alert.
[355.86 → 357.48] I guess I have to call it to Chris on this.
[357.80 → 358.06] What?
[358.40 → 359.56] That's blowing my mind.
[359.62 → 361.22] So how would you experiment with this?
[361.28 → 361.78] Where would you go?
[361.78 → 365.66] Well, first you can just do it in your JavaScript console.
[366.12 → 370.22] So anywhere that you can run JavaScript, you can run JS Bleep.
[370.60 → 375.72] But you can also try out, there's this REPL at JSBleep.com.
[375.94 → 378.92] But you sub in the word for bleep, the F word there.
[379.28 → 381.66] And then you can put in any line of JavaScript.
[382.38 → 384.80] And it'll show you what it would be in JS Bleep.
[384.80 → 385.36] Okay.
[385.68 → 390.92] So if we were to do A and encode it in JS Bleep, it ends up.
[392.50 → 393.38] Oh, dear.
[393.98 → 395.06] It's totally unreadable.
[395.44 → 396.56] It's totally unreadable.
[397.00 → 397.54] All right.
[397.86 → 400.14] First entry dominating.
[400.44 → 401.80] Okay, Nick, what have you got?
[402.08 → 407.22] Well, I've been struggling with this because, I mean, just using JavaScript and not TypeScript
[407.22 → 408.88] is just a big WTF.
[409.38 → 411.66] So I'll throw that out there as my first one.
[411.76 → 412.68] But I do have another one.
[412.68 → 414.90] Do you remember array-like objects?
[415.48 → 416.30] They still exist.
[416.50 → 417.30] I mean, they're still there.
[417.94 → 419.80] But WTF, they're wild.
[420.10 → 421.44] They're not quite arrays.
[421.74 → 424.96] They're just objects that have a length property and index things by numbers.
[425.68 → 429.86] And real APIs, like DOM APIs, use them and return them.
[430.56 → 435.58] And facilitated the need for the arrayed up from method, for example.
[436.24 → 438.46] It's just a big WTF to me.
[438.56 → 438.88] I don't know.
[438.88 → 443.70] So can you take an object that is not an array-like object and make it an array-like object by just
[443.70 → 444.38] giving it a length?
[444.72 → 444.92] Yeah.
[445.20 → 449.88] But then it will, like if you give it a length of five, and then you try to iterate over that
[449.88 → 455.40] with a for loop or something like that, it would be trying to look at the indexes.
[455.50 → 457.38] Zero, one, two, three.
[457.54 → 460.40] Which could exist as properties on the object.
[460.58 → 461.46] Or could not.
[461.58 → 463.98] And could just be undefined and return undefined for everything.
[463.98 → 467.14] So it's just a weird way to get that.
[467.20 → 471.22] But then on top of that, with modern JavaScript, we also have, you can implement iterable on
[471.22 → 471.36] there.
[471.42 → 476.16] You can use symbol. Iterator to create your own custom iterator method on anything.
[476.96 → 478.84] And yeah, it's just wild.
[479.00 → 482.10] All these ways that we have to sort of be arrays.
[482.50 → 484.94] And then we also have sets, which is kind of like an array.
[485.28 → 487.48] Trying to figure out what the right reaction to that is.
[487.54 → 487.98] I think it might be...
[488.98 → 490.66] JavaScript should be destroyed.
[491.52 → 491.92] Appropriate.
[492.14 → 492.24] Yeah.
[492.24 → 492.76] Possibly.
[493.36 → 493.64] Okay.
[493.74 → 497.16] So I've got one, which is more of a cross-browser oddity.
[497.36 → 501.24] So JavaScript, I think one of the things that makes JavaScript, so weird is that we...
[502.26 → 504.50] There's no standard implementation environment, right?
[504.56 → 505.34] Like there's...
[505.34 → 509.62] JavaScript is being run in different browsers and also on the server.
[509.74 → 511.74] And these are all implementations of the language.
[511.90 → 516.30] And so any sort of spec edge case gets treated differently.
[516.40 → 520.48] So the first one I'm going to talk about is like dates and time zones.
[520.48 → 527.92] So if you do like a new date, let's say you do like new date 2022-01-01.
[528.10 → 532.72] If you do that in Firefox, you get back a date that is January 1st, 2022.
[533.14 → 540.04] If you do that in Chrome, at least if you're in the US, you get back Friday, December 31st, 2021.
[540.04 → 544.94] Because the new date does it in UTC.
[545.20 → 549.14] But if you're in a time zone such that that time UTC is actually the day before...
[549.14 → 552.78] Like Chrome actually returns the object in the user's time zone.
[552.88 → 556.16] And so you can ask for one date and actually get the date previous.
[556.84 → 561.38] Even more fun, if you ask for a date in February that does not exist...
[561.38 → 562.72] So February is a weird month, right?
[562.78 → 567.74] We've got only 28 days when most months, if you can go up to 30 or 31.
[567.94 → 572.82] If you ask for the 31st of February, Firefox will rightly tell you, hey, that's an invalid date.
[572.92 → 576.76] But Chrome will happily hand you a date that is for March 2nd.
[577.86 → 579.30] So yeah.
[579.30 → 585.86] I don't know if that's a JavaScript-ism or a browser-ism, but it's a hole in the spec, I think,
[585.94 → 588.60] that is implemented in kind of weird way.
[588.60 → 591.08] Dates are just so hard in general.
[591.38 → 592.72] Dates are hard.
[593.18 → 593.88] So hard.
[594.04 → 594.50] So hard.
[594.86 → 600.08] Although I kind of like the way that Chrome handles it, that it goes to like March 2nd or
[600.08 → 603.42] whatever, because it makes adding to dates much easier.
[603.92 → 604.28] Totally.
[604.54 → 607.10] Well, and I was wondering, like, does it let me do that for anything?
[607.20 → 610.58] Like, can I ask for the 64th of January?
[610.80 → 612.32] But there it will do invalid.
[612.56 → 613.22] Oh, interesting.
[613.30 → 616.26] Or if you even ask for like the 32nd of something, it will do invalid.
[616.26 → 621.28] But if you ask for the 31st of February, it will map it over into March.
[622.50 → 623.32] So interesting.
[623.46 → 624.50] I wonder what the cutoff is.
[624.70 → 625.26] I don't know.
[625.56 → 625.78] Yeah.
[625.94 → 630.76] I guess we'd have to like to dig into the source code or something or try it.
[631.60 → 631.80] Cool.
[632.16 → 634.06] Allie, you said you had another one as well.
[634.58 → 634.76] Yeah.
[634.84 → 637.74] And so this is more of a programming oddity.
[637.92 → 639.56] And it's not even really an oddity.
[639.70 → 641.22] It's how it's supposed to be.
[641.22 → 648.82] But if you've ever done like 0.1 plus 0.2 in JavaScript, you'll notice that you get like
[648.82 → 651.70] three point and then a bunch of zeros and then a four.
[652.22 → 653.58] You've probably done this before.
[653.66 → 659.34] You've done like float math and like seeing this really, really random number show up.
[659.46 → 665.48] I have it happen if I handle like a shopping cart or whatever with floats instead of strings
[665.48 → 668.32] or instead of doing the integer math or whatever.
[668.32 → 672.30] So this is a thing across most programming languages.
[673.02 → 679.26] It is the way that it has to be because binary is base two.
[679.84 → 685.24] And so it only handles like one half, one fourth, one eighth cleanly.
[685.66 → 689.74] And so something like one fifth or one tenth would be a repeating decimal.
[689.74 → 697.82] And so this is expected that it needs to have in order to be properly represented in binary
[697.82 → 701.86] is to have like this weird number at the end there.
[702.26 → 706.32] So that's my other favourite one is that there's actually a reason for this.
[706.36 → 710.46] And there's a website that handles that explains this really well.
[710.70 → 716.00] It's called the so the subdomain is zero, and then it's point three and then a bunch of zeros
[716.00 → 717.06] and then four dot com.
[717.06 → 721.20] So we'll leave that in the show notes, but I like these little like explainer sites
[721.20 → 723.62] that explain these really niche concepts.
[724.96 → 726.58] There are a lot of them for JavaScript.
[727.38 → 727.74] Yes.
[728.38 → 730.92] You need to get exactly the right number of zeros.
[731.14 → 736.90] So I just checked to see if they like reserved the other domains if you like type of it.
[736.98 → 738.10] So how many zeros is that?
[738.16 → 739.82] It's like one, two, three, four, five, six.
[740.14 → 741.06] It's like 15 zeros.
[741.06 → 744.86] So 0.3 followed by 15 zeros, I think.
[745.66 → 750.00] Yeah, I think it's 10 to the negative 14th is what it says down in the footnotes.
[750.10 → 752.08] So that would track.
[752.98 → 753.90] That's a fun one.
[754.20 → 758.00] Nick, do you have any other JavaScript acidities that you want to share?
[758.42 → 759.56] Yeah, I'll share one more.
[759.90 → 765.36] These are all things that you never really run into, hopefully in real life code.
[765.36 → 771.94] So the number in JavaScript, like the number object or number constructor has some constants
[771.94 → 772.24] on it.
[772.30 → 774.86] It has number dot min value and number dot max value.
[775.06 → 780.72] And those are some ridiculous numbers, ridiculously high numbers or ridiculously low numbers.
[780.96 → 788.00] If you take the min value, which is you just print it out, it's 5e to the negative 324th.
[788.00 → 794.56] But if you do a comparison on that and say number dot min value is greater than 0, it
[794.56 → 796.20] becomes true, even though it's a negative value.
[796.70 → 797.44] Just amazing.
[797.74 → 798.68] Is it a negative value?
[798.88 → 802.64] 5e negative, that's like 5 is positive, right?
[802.70 → 804.12] So it's going to...
[804.12 → 805.08] Wait, yeah, you're right.
[805.20 → 811.26] It's like 5 in the 324th decimal place past the or points past the decimal.
[811.52 → 815.12] Because you can do negative min value, number dot min value, and then it's false too.
[815.72 → 816.54] Yeah, you're right.
[816.54 → 821.80] But it's, you can still have negative values and you can have 0, right?
[822.02 → 826.26] And so it should be the minimum value that you can have, but it's not.
[827.30 → 831.76] It's like the smallest fraction, not the most negative.
[832.20 → 832.44] Yeah.
[832.76 → 837.86] And I think that it's just taking that float and converting it to an INT and then doing the
[837.86 → 841.40] comparison to 0, which is why it's coming out that way.
[842.32 → 845.90] There's always lots of fun, simple explanations as to why those things happen.
[845.90 → 847.22] But it's very fun.
[847.22 → 850.60] I see there's also a number dot max safe integer.
[851.06 → 855.66] I don't know if this will do it for you, but if I do in Chrome the max safe integer plus
[855.66 → 858.06] one, it shows me a number that is one more.
[858.12 → 862.42] But if I also do max safe integer plus two, it actually shows me the same number.
[862.42 → 869.50] So if I do number dot max safe integer plus one equal to number dot max safe integer plus
[869.50 → 870.46] two, it says true.
[870.68 → 873.38] But if I do plus three on one side, it says false.
[873.50 → 873.64] Yeah.
[873.64 → 877.66] So at least in Chrome, it's jumping in some weird way.
[878.08 → 878.28] Yeah.
[878.58 → 879.84] I'm trying in the node ripple too.
[879.90 → 884.86] And I was trying with the min safe integer and subtracting one and subtracting two.
[884.96 → 885.68] And those are identical.
[885.68 → 889.42] And then subtracting three is two more or two less, I guess.
[889.52 → 892.90] And then subtracting five is two less from that.
[892.90 → 899.34] I think that might be just a Chrome bug, but that sounds like JavaScript should be destroyed.
[900.38 → 902.32] It's just like physics, right?
[902.38 → 907.26] They just JavaScript is the black hole that physics falls apart around or that number
[907.26 → 909.80] number addition falls apart around arithmetic.
[910.24 → 910.64] Awesome.
[910.96 → 918.32] I have one last one that I will share, which is related to sort.
[918.32 → 924.76] And so if you have a set of strings, and you have them in an array, you can sort them.
[924.90 → 929.30] And if you sort them without passing a comparison function, it will do kind of what you expect.
[929.32 → 930.60] It'll sort them in alphabetical order.
[930.60 → 934.84] But if you pass a comparison function, which is something that in theory you should be able
[934.84 → 941.38] to do, you know, you pass A and B and you return B minus A, which is what works with
[941.38 → 942.58] numbers or things like that.
[942.58 → 948.58] It behaves differently once again in Chrome versus Firefox.
[948.92 → 957.74] And I think it has to do with string subtraction not being defined or returning not a number.
[958.34 → 960.40] But it's kind of weird.
[960.66 → 965.68] Like in theory, if you want to sort something backwards, you pass in the comparator and you
[965.68 → 967.42] do B minus A instead of A minus B, right?
[967.42 → 968.88] Like the default will be ascending order.
[968.98 → 969.62] You want to do it backwards.
[969.72 → 970.40] You pass this in.
[970.40 → 974.90] But for strings, it suddenly goes to indeterminate behaviour.
[975.10 → 977.68] And so I think you need like a reverse method instead.
[978.10 → 984.18] I think it's also fascinating that the algorithm that different browsers use for sort
[984.18 → 985.52] is different too.
[985.72 → 987.46] So like some of them use like Tim sort.
[987.84 → 992.68] Some of them use merge sort and then some are quick sort, which I think is also like fascinating.
[993.26 → 993.66] Totally.
[994.22 → 995.58] So there you have it.
[995.70 → 999.24] Our inaugural WTFJS.
[999.24 → 1001.50] Let us know what you all think.
[1001.88 → 1006.78] You want more of this, or it's worthless because this stuff is actually not things that you
[1006.78 → 1008.06] should be using in your day to day.
[1017.32 → 1020.24] Talking about maintainable code bases.
[1020.24 → 1025.26] Let's just have a little bit more of a conversation about what makes for a maintainable code base.
[1025.38 → 1028.78] I mean, I think not using JS bleep comes to mind.
[1029.44 → 1030.18] That's a big one.
[1030.72 → 1035.12] It's really hard to read a 4,000 letter long hello world.
[1035.52 → 1038.38] That is kind of an interesting like code obfuscation.
[1038.52 → 1041.98] And if you're trying to like to get something in that that people aren't going to understand,
[1042.16 → 1043.44] like you could do something there.
[1043.44 → 1047.22] Yeah, but for the most part, don't do it at home, folks.
[1047.62 → 1052.26] Is there a way to go backwards from a JS bleep to what it was trying to do?
[1052.70 → 1055.32] Oh, I don't know if there's an interpreter for it.
[1055.76 → 1060.70] I mean, you could just execute the code, run like a console log on it instead of a
[1061.16 → 1064.84] or like an evil and then to a string and then console log or something.
[1065.02 → 1067.60] But that'd probably be how you'd have to do it.
[1067.60 → 1072.74] So what else have you all seen that makes for making a code base maintainable?
[1072.82 → 1075.26] I feel like we all want a maintainable code base, right?
[1075.28 → 1079.26] We all want something that is, oh, this is going to be easy to maintain.
[1079.48 → 1081.96] And it's not going to keep blowing up on us.
[1082.00 → 1086.30] We're not going to have the team slowing down because the code base is hard to maintain.
[1086.42 → 1089.72] But like, what does that actually mean to you?
[1090.04 → 1093.92] Well, there are some basic things that really used to be much more of a problem,
[1093.92 → 1095.58] but aren't really in today's world.
[1095.70 → 1097.32] And that's like code style.
[1097.32 → 1101.32] We used to maintain a manual code style document that was like,
[1101.44 → 1104.32] you should have a space after an if statement,
[1104.32 → 1107.62] but before the parentheses and things like that.
[1107.68 → 1111.18] But we don't have that anymore in like a document style.
[1111.26 → 1116.32] We just have tools like Prettier or some other formatter that just formats it for you.
[1116.38 → 1118.12] And as long as everyone's on board with that,
[1118.22 → 1120.68] then all the code looks the same in a good way.
[1121.18 → 1123.28] And it makes it much more readable for everyone.
[1123.64 → 1127.30] Yeah, it saves you from having to like to have arguments within code reviews.
[1127.32 → 1129.96] Like, hey, I don't like this semicolon.
[1130.28 → 1132.34] Well, okay, well, automated.
[1132.62 → 1133.74] Doesn't matter anybody.
[1134.32 → 1134.80] Yes.
[1134.86 → 1135.74] Have a guide for this.
[1135.96 → 1136.06] Yeah.
[1136.10 → 1141.98] Some of the choices, Prettier or like Black or the Python formatter or like all these different formatters,
[1142.12 → 1143.46] some of their choices are really weird.
[1143.46 → 1146.44] But it does stop the arguments.
[1146.74 → 1147.14] Definitely.
[1147.54 → 1150.30] And you can really use that as a tool.
[1150.64 → 1156.04] Like I write the most concise code, like on a single line, I'll write things very quickly.
[1156.10 → 1158.94] And then I'll hit save and Prettier will format it for me.
[1159.22 → 1162.88] And so I can like use that as a shortcut to write code fast.
[1162.88 → 1166.12] And then it just gets prettified as I go.
[1166.60 → 1168.96] That's what I do for sure as well.
[1169.26 → 1173.16] It's too much work to worry about indentation myself.
[1173.56 → 1177.76] I'll just have my editor do that myself for me.
[1177.76 → 1183.88] I think another really, really important one for maintainable code bases is an appropriate level of abstraction.
[1184.34 → 1192.12] I think that sometimes you can go really, really heavy on abstraction, and it makes it so that the code base is impossible to navigate,
[1192.64 → 1194.94] especially for somebody joining that code base.
[1195.02 → 1197.34] They just can't figure out where to find things.
[1197.34 → 1203.46] So if there's like 18 levels of inheritance or something like that, that makes it very, very difficult to find,
[1203.66 → 1207.52] hey, this is where this attribute is coming from or this is where this method is.
[1207.98 → 1213.90] But then also on the inverse, if you are rewriting things over and over and over again,
[1213.90 → 1222.04] that also becomes impossible to maintain because then you have to update things in 18 different places every single time that you want to update something.
[1222.04 → 1226.72] So having like a very appropriate level of abstraction is difficult to do.
[1226.72 → 1231.82] But I think it's one of the most important things for making it so that more people can contribute to a code base
[1231.82 → 1234.76] and that that code base is able to live a long time.
[1235.46 → 1244.32] So how would you define or measure or like what are the smells or whatever that say this is the appropriate level of abstraction?
[1244.82 → 1246.14] That's a good question.
[1246.50 → 1250.42] I don't know if there's like a set of finite rules that I would have,
[1250.54 → 1256.14] but I think one of the biggest things, and I guess this is less relevant because object-oriented programming
[1256.14 → 1258.72] isn't as like hot in JavaScript right now.
[1258.96 → 1265.08] But that is something that I saw all the time when I was a software engineer working on the back end,
[1265.12 → 1271.82] is that there would be so many levels of inheritance that it would just be impossible to figure out where things were coming from.
[1271.82 → 1278.90] So having like a set rule on your code base, whether it's like three levels of inheritance or two or something like that,
[1279.44 → 1285.10] where you can have abstractions, but you make it so that they're at least possible to navigate.
[1285.26 → 1286.32] I think that that's important.
[1286.32 → 1293.88] I also think that when you're cleaning up duplication, thinking about, hey, like,
[1294.36 → 1299.88] is this something that's going to be duplicated twice or is this something that's going to be duplicated 50 times?
[1300.26 → 1306.46] And if it's something that's just going to be duplicated twice, maybe, just maybe, think about like,
[1306.68 → 1313.48] is this going to make the code base more complex to abstract this or is it going to make it more readable?
[1313.48 → 1316.20] So I think about those types of things is important.
[1316.68 → 1325.24] Another smaller thing, and I used to read a lot of Sandy Metz earlier in my career, like obsessed with her books.
[1325.30 → 1331.24] And I know that they're Ruby oriented, but I think that they really do apply to any programmer.
[1332.02 → 1336.76] I've never really been a full-time Ruby person myself, so I've learned a ton from there.
[1336.76 → 1343.66] And I think another thing that she mentions is having relatively short classes, methods, and functions.
[1344.42 → 1353.10] So having like 100 lines as your length for a class, which I think that those rules can be bent a little bit
[1353.10 → 1355.24] depending on your individual code base.
[1355.56 → 1360.72] But I do think that if you're going to a file of code, and it has like 4,000 lines of code in it,
[1360.78 → 1363.12] that becomes very hard to navigate as well.
[1363.12 → 1365.02] And I do see that like all the time still.
[1365.50 → 1369.12] Those really, really long files or these really, really long classes.
[1369.46 → 1372.62] And also like a function should do one thing and one thing well.
[1373.24 → 1379.14] And if it's doing like three different things, if the function should have an and in the name of it,
[1379.24 → 1383.52] that's another sign that it's going to be very difficult to figure out what that function is doing
[1383.52 → 1384.86] and to update it in the future.
[1385.28 → 1388.62] So her rule is like five lines of code for a method or function.
[1388.62 → 1393.06] And I think that in a lot of cases, that's a decent length as well.
[1393.46 → 1396.72] Maybe you could double that for your code base or something like that.
[1396.82 → 1402.48] But again, if you're getting to like 100 line functions, which again, I've seen in production code bases,
[1403.12 → 1405.90] it's sometimes like, maybe we should rethink that.
[1406.00 → 1407.24] It's going to be pretty hard to maintain that.
[1407.96 → 1408.02] Totally.
[1408.14 → 1410.02] Well, and you've alluded to something that I think is good,
[1410.02 → 1418.10] which is like most of these rules should be rules of thumb that occasionally you'll find a case where it's not appropriate.
[1418.50 → 1425.00] And you should not get in a fight over a six line function, you know, just because five is your line.
[1425.08 → 1431.10] Maybe sometimes you actually need six lines and especially like white space sensitive languages like Python
[1431.10 → 1435.56] or, you know, if you're prettier format and JavaScript extends, you know, how you're doing it.
[1435.60 → 1438.88] Like don't fight over that number, but it is a good rule of thumb.
[1438.88 → 1443.20] I think this question of like, what's the right level of dryness is fascinating.
[1443.66 → 1443.76] Yes.
[1443.98 → 1448.94] The industry was obsessed for a while about dry everything, dry everything, dry everything.
[1449.02 → 1454.94] And I remember having a conversation a long time ago with Michael Chan, Phantastic for the React podcast.
[1455.10 → 1457.52] And we actually, we recorded an episode with him.
[1457.98 → 1462.22] And we were talking about like dry code is dead code.
[1462.34 → 1463.68] It's code that's not changing.
[1464.40 → 1468.24] And that can be perfect for something that's well understood.
[1468.24 → 1473.82] But if it's an actively changing part of your code base, or it wasn't dead code, it was like brittle code.
[1473.96 → 1481.28] Dry code is brittle in the sense that it's hard to change it because lots of things depend on it behaving in a particular way.
[1481.70 → 1487.48] And so it can be good to dry things out when you've got something that has showed up as a pattern over and over again.
[1487.48 → 1491.18] And you know, okay, this, we're always wanting to do this in this particular way.
[1491.76 → 1499.24] But actively changing parts of your code base should probably not be dry because you're still trying to understand like, what are the abs tractable bits?
[1499.88 → 1502.00] What else makes for a maintainable code base?
[1502.02 → 1502.78] Or maybe turning it around.
[1502.86 → 1505.68] What makes for a terrible, hard to maintain code base?
[1505.68 → 1510.58] Probably the inverses of what we just talked about for the most part.
[1510.84 → 1513.64] I think another one that we haven't talked about yet is testing.
[1513.76 → 1526.64] And on both sides, that making sure that you have a system set up that you can catch errors and make sure that adding one feature isn't breaking a bunch of other features or even any features.
[1526.64 → 1529.46] That's really, really important to have.
[1529.74 → 1535.96] And also I think writing tests makes it so that you have to think about your code a little bit more as well.
[1536.04 → 1539.24] So I think that's another big value add there.
[1539.40 → 1542.04] So that's another point of conversation is testing.
[1542.42 → 1542.94] Yeah.
[1543.08 → 1545.12] And having the right, or testing the right things.
[1545.26 → 1548.64] Having a testing code base that you trust too.
[1548.64 → 1561.44] Like if there's any, like we have occasionally some tests that are like, I'm forgetting the word for them, but they intermittently like fail in areas, and it makes us really skeptical about the code.
[1561.54 → 1572.00] And it might just be like things that are just weird timeouts and things with the tests, but it causes distrust in the testing system, and it causes distrust when we go to change those things.
[1572.00 → 1578.56] I was going to go in a similar direction, but talking about like, yeah, testing at the right levels of abstraction.
[1578.88 → 1587.38] So like backend models, unit testing, like really fine-grained unit testing can be really useful for view components.
[1588.18 → 1599.72] Testing like the rendered state to me is usually like unit tests are not the right level of abstraction there because anytime you're changing your UI, you just end up with additional churn, and you're not actually checking very much.
[1599.72 → 1604.66] And I end up biasing much more for end-to-end tests to test my UI.
[1604.88 → 1609.08] And then if there's like logic that's happening in the front end, we can have unit tests for those.
[1609.22 → 1620.38] But like the HTML that's getting rendered in my experience, like having tests in that reduces the maintainability of that code because you just end up doubling the effort anytime you make a change.
[1620.60 → 1622.42] Let me ask you a question on that, K-Ball.
[1622.66 → 1626.10] When you say end-to-end, what's the end, and what's the other end?
[1626.10 → 1630.90] Is it like from this end of the component to that end of the component or from this end of?
[1631.06 → 1632.12] No, whole stack.
[1632.48 → 1642.60] So get a database booted up, render your application, use Selenium to drive through it as an actual browser, as a user would.
[1643.02 → 1647.08] Build yourself utilities for logging in and getting yourself all in the right state.
[1647.22 → 1651.34] But testing the UI as a user as it connects all the way back through your API.
[1651.98 → 1654.42] Now that's a complex setup.
[1654.42 → 1657.08] Does that lead to issues?
[1657.26 → 1659.46] Because it's harder to just spin up quickly.
[1659.54 → 1660.10] Maybe it is.
[1660.14 → 1660.50] I don't know.
[1660.76 → 1661.58] Yeah, that's a good question.
[1661.70 → 1665.08] So we run end-to-end primarily in our CI tools.
[1665.58 → 1666.82] So it takes a long time.
[1666.92 → 1668.68] The end-to-end tests are the slowest part of our testing.
[1669.10 → 1672.02] And this actually kind of gets to another area here.
[1672.08 → 1674.92] So not just tests, but tests that run automatically.
[1675.16 → 1681.28] Tests that don't require cognitive overhead, remembering to run them, doing something like that.
[1681.28 → 1688.44] But tests that run in any time you push a change, and you're submitting a pull request that all the tests pass, and they catch things.
[1688.44 → 1693.00] I think it's a huge part of what makes for a maintainable code base.
[1693.06 → 1696.74] And this actually, there's a whole realm we can talk about there in terms of practices, right?
[1696.80 → 1703.72] Like having a general team practice of always having a clean trunk or main branch that can be deployed.
[1703.72 → 1712.28] So that you reduce the cognitive overhead of, wait, if I'm doing this change, do I have to check with these people or check this thing before I can push it out and do things like that?
[1712.34 → 1715.52] Like that's not necessarily anything in the code itself.
[1715.82 → 1721.70] It's a practice for how you keep the code and how you approach the code and what qualifies as done.
[1722.06 → 1726.10] But makes a huge difference in your sort of sense of maintainability.
[1726.10 → 1732.62] Because now if an issue comes in, and I want to do a target, a point fix and deploy it, I know I can.
[1733.14 → 1733.22] Yeah.
[1733.40 → 1742.08] And kind of leading, well, not really leading from that, but another similar thing is like having tests run automatically is a perfect thing.
[1742.12 → 1748.76] So having like a whole CI pipeline, but also just thinking about like your review pipeline and how code reviews get done.
[1748.76 → 1759.38] We utilize a tool that GitHub provides called a code owners file that lets you specify files or globs of files that are owned by a particular team.
[1759.52 → 1770.36] And so anytime, you know, you can freely go change whatever files, but the code owners file will just automatically tag the appropriate people to be a reviewer on that pull request as it goes through.
[1770.36 → 1777.04] Just to make sure that you have kind of more domain level experts looking at things before they're getting merged.
[1777.42 → 1778.00] That's cool.
[1778.06 → 1779.14] I didn't know about that feature.
[1779.44 → 1781.92] I'll put a link in the show notes on that.
[1782.18 → 1783.00] I want to look into that.
[1783.58 → 1790.54] Anything else that comes to mind either on the absolutely you should be doing this or absolutely you should not be doing this?
[1790.54 → 1811.70] I think one thing that helps in terms of maintainability is in kind of going in that tooling direction, like typed code makes a big difference in terms of maintainability because it has a whole class of issues that you can catch now at compile time without additional requirements from the user to think about it.
[1811.70 → 1829.52] I think in, I spent a lot of my career in like loose typing, duct typing worlds, and there you have to be extremely thoughtful about how you write your unit tests to handle and catch classes of errors that the type checker will catch for you without you ever having to think about it.
[1829.52 → 1840.76] And so it makes both writing new code, but especially refactoring code, changing code, just so much easier that it dramatically increases the maintainability of your code base.
[1840.76 → 1844.08] And there are, you know, even for, you know, TypeScript is a great example.
[1844.22 → 1851.20] In Python, there's MYP, like even languages that don't have strong typing have abilities to add that level of protection at this point.
[1851.88 → 1855.80] I think one other thing that we have not mentioned so far is documentation.
[1856.26 → 1870.74] And that's like another important thing to make it so that you can actually hand off a project from one engineer to another or have multiple engineers working on it so that one doesn't have to kind of mind read for the previous person writing the code.
[1870.76 → 1872.26] Like, why were these decisions made?
[1872.26 → 1875.68] Having like decision documents when an architectural decision is being made.
[1876.00 → 1886.10] Like all those types of things help to set context for the next person, so the next person isn't just like, let's rewrite this for the sake of rewriting this or whatever.
[1886.30 → 1887.80] Like, what was the context there?
[1887.94 → 1889.58] Why did people make those decisions?
[1889.58 → 1901.60] So there are a lot of different layers of documentation from code comments to more like centralized true documentation for a project to like the decision and architectural documents from the beginning of the project.
[1901.60 → 1907.06] And I think keeping all of those and making sure to surface them is another really important part.
[1907.84 → 1908.40] Totally.
[1908.72 → 1914.82] I was going to say kind of towards the, you know, using types, which is another form of documentation really.
[1914.82 → 1926.12] But using code generation whenever possible, specifically for things like don't be manually typing out the responses that you get from, you know, your server or your database or whatever.
[1926.32 → 1928.12] Have those be automatically generated.
[1928.12 → 1936.04] And there are great tools that can do it from GraphQL or from REST schemas and just generate them automatically so that they're always 100% correct.
[1936.04 → 1941.98] And then you can, you don't have any ambiguity or incorrect types that you're working off of.
[1942.24 → 1942.40] Totally.
[1942.60 → 1945.94] Going in on the documentation a little bit, which I love that you brought that up, Ali.
[1945.94 → 1955.70] I think one of the things that I've seen be challenging, especially for newer developers, is to know the right level of documentation and commenting to put in.
[1955.70 → 1966.18] A rule of thumb that I've heard that I really like is that if you're commenting in a file, like within a function or something like that, comments should always be a different level of abstraction than the code.
[1966.40 → 1970.92] So either a higher level of abstraction, communicating why behind this.
[1971.04 → 1972.20] Why would you use this function?
[1972.34 → 1973.16] Why would you do this?
[1973.34 → 1979.94] Or a lower level of abstraction where it's like, okay, we're doing, here are the details of why this algorithm works.
[1979.94 → 1987.44] I think a lot of more novice developers or folks who haven't thought about it deeply will comment at the same level as their code.
[1987.56 → 1989.44] I'm going to change this thing to this thing.
[1989.70 → 1992.34] And the code should already do that.
[1992.54 → 1993.14] Should document itself.
[1993.36 → 1993.48] Yeah.
[1993.88 → 1994.22] Yeah.
[1994.36 → 1995.92] It should document itself there.
[1996.00 → 2002.26] Where the additional commenting is really helpful is that additional context that set a slightly different layer of abstraction.
[2002.90 → 2003.36] For sure.
[2003.48 → 2005.38] The comments should be the why, not the what.
[2005.38 → 2014.30] Have you encountered other good guidelines for like right level of abstraction to do in design decision documents or the other types of documentation that you brought up?
[2014.74 → 2020.84] I don't know if I have direct rules for them by any means, but I think that having this is important.
[2021.16 → 2026.68] I think I've worked at a lot of early stage startups and those things just do not exist whatsoever.
[2026.68 → 2039.40] And then working at a bigger company, having to do like reviews before any code is written of here are the plans, here's what we're going to do, here are the thoughts behind this, here's why these decisions were made.
[2039.68 → 2045.90] I think that that's like incredibly important because I've seen so many times when it's like, okay, we've got this Python code base.
[2045.90 → 2056.00] Let's now rewrite it in Ruby because that person who was writing Ruby before or the person who was writing Python left the team, and we don't understand why they decided to do it this way.
[2056.44 → 2057.92] And so like, let's just start from scratch.
[2058.04 → 2059.82] And it's just not productive.
[2059.82 → 2063.86] And so having to think through those things, justify them to other people.
[2063.98 → 2069.08] So if that appeal disagree, they can disagree then rather than after the code base is written.
[2069.28 → 2070.90] I think that that's so important.
[2071.12 → 2078.22] And also just having to justify your decisions is such an important part of being an engineer.
[2078.52 → 2087.06] But then the documentation point for maybe like an API or something like that, having it laid out, like here's how to use this.
[2087.06 → 2096.96] You don't just have to guess, you don't just have to dive into the code in order to figure out how to use your API or documentation to explain how the code base is organized.
[2097.30 → 2105.22] That's another huge one so that more people can jump into it, and they don't have to spend like a week trying to figure out where the class for this is.
[2105.40 → 2108.64] I think that all of those are things that really, really help out.
[2109.20 → 2109.44] Totally.
[2110.02 → 2114.76] Something you were saying reminded me, I was having a conversation like this on what belongs in a design doc.
[2114.76 → 2124.46] And a couple of things that I have been thinking about and trying to advocate to folks as well are like the things you considered that you chose not to do.
[2124.90 → 2129.88] Because I think a lot of times we bias towards the like we forget the negative space.
[2130.00 → 2134.88] We talk a lot about where we landed in our final thing, but we don't talk about what we ruled out and why.
[2134.88 → 2145.18] And then the other thing that I think is really helpful if you can do it, it's hard, but is if you can lay out what would make it worth reconsidering this decision?
[2145.40 → 2152.64] Like what types of changes, new information or new tools or new things would make it worth reconsidering this decision?
[2152.64 → 2157.76] Because I think some of the resistance to design docs is like the world is dynamic.
[2157.90 → 2158.50] Things are changing.
[2158.64 → 2164.76] It might actually be different, but you want the design doc so that you're not always relitigating this.
[2165.10 → 2167.70] You have, you know, if somebody is coming in and saying, did you think about this?
[2167.76 → 2168.50] Did you think about this?
[2168.50 → 2170.08] You can say, yes, look in the design doc.
[2170.16 → 2171.68] You can see all the things we thought about.
[2172.08 → 2175.50] But there is sometimes that question of here's something I didn't think of.
[2175.62 → 2176.12] Here's the thing.
[2176.12 → 2181.80] So if you can sort of flesh out, like these are the types of things that would cause this decision to not be right anymore.
[2181.98 → 2182.38] Yeah.
[2182.46 → 2183.50] That can be super helpful.
[2183.98 → 2184.38] Definitely.
[2184.94 → 2185.58] Super important.
[2185.70 → 2195.96] And having like a review meeting about that design doc, I think is so important too, so that people can poke holes in it before the decisions are actually fully made and can't be reversed.
[2206.12 → 2225.12] So we wanted to talk a little bit about the current moment in tech, because it feels like if you're on Twitter, or you're watching things, the zeitgeist has shifted within like weeks from this is the hottest market for engineers in history.
[2225.12 → 2235.58] You can never, you know, you have dozens of job offers and like if you're hiring, like you just can't find people to, oh no, everything is stopping in like weeks.
[2235.80 → 2236.86] It has gone there.
[2237.04 → 2242.84] And there's like Y Combinator put this memo out about like plan for the worst, you know, try to do all these things.
[2242.94 → 2246.40] And Sequoia has a deck and like all of these different things.
[2246.40 → 2253.64] So I thought it might be worth us just sort of talking about what's actually going on, like what's causing this.
[2254.02 → 2261.02] Is it as bad as people are saying, like, and what should people do about this?
[2261.06 → 2269.28] So I have lots of thoughts because it's been top front of my mind, but I'm very curious what you all have seen and heard and how you're thinking about this.
[2269.40 → 2274.00] I'd be lying if I said it didn't cause extra anxiety, just thinking about it a little bit.
[2274.00 → 2276.38] But it's been on my mind because you're right.
[2276.44 → 2285.06] It did just go from you can leave and get 30 to 50% just by, you know, hopping companies to maybe I won't have a job next week.
[2285.44 → 2287.96] And I don't think that's the case for me.
[2288.00 → 2292.08] But like it does seem like just the tides are shifting.
[2292.08 → 2303.84] But at the same time, like, is there a delineation that can be made between like some of the like more venture backed startup companies versus like more established companies?
[2304.00 → 2312.38] Because at the same time, we've seen articles about like Microsoft doubling their compensation budgets for the next year.
[2312.88 → 2316.04] Yeah, I think it's unreal how fast this has turned.
[2316.04 → 2323.66] And I think that I mean, the economy in general has clearly shifted with the response to inflation.
[2323.66 → 2330.28] And then also the shift in the markets as well.
[2330.54 → 2337.78] I think that even a lot of software engineers, a lot of our compensation is based on the company stock.
[2338.00 → 2344.04] And so that has dramatically decreased for a lot of people over the past few months as well.
[2344.04 → 2350.80] So even if you're at your current job, you're probably still affected, even if you haven't been laid off.
[2350.92 → 2360.30] And so I think it's a fascinating economic moment of will this be a recession, which is a very scary thought, I think, for a lot of us.
[2360.38 → 2362.36] Or is this just a momentary thing?
[2362.42 → 2373.48] Is it just that things are shifting, and we're kind of correcting for the fact that a lot of these companies boomed really, really fast due to the changes in our lives due to the pandemic?
[2373.48 → 2376.48] So I think that we'll have to see.
[2376.62 → 2377.80] I don't think anybody knows.
[2378.12 → 2383.14] Like people who work in finance have predictions, but I think it's a really, really hard thing to predict.
[2383.22 → 2385.68] And there's lots of conflicting predictions out there.
[2386.06 → 2387.56] But it's a tough time.
[2387.60 → 2391.78] And it's really, really wild how fast it shifted from like you got to leave your job.
[2391.84 → 2394.06] You got to get a new job while everything's hot.
[2394.16 → 2397.76] Like software engineers are getting paid a bazillion dollars a year now.
[2397.86 → 2400.02] Everybody needs to take advantage like these.
[2400.02 → 2408.76] I'm sure that everybody saw all the rumours on like social media about Web3 and how much people were making in that realm.
[2408.94 → 2411.44] And then, I mean, that crashed overnight as well.
[2411.66 → 2418.16] So it's a really, really crazy time both for us in tech, but also I think outside of it as well.
[2418.78 → 2418.86] Yeah.
[2418.96 → 2424.00] Well, and one of the interesting things is like there's a lot of companies that are doing layoffs, right?
[2424.00 → 2429.28] And there's this like layoffs.FYI site that is just tracking what layoffs are happening in tech.
[2429.32 → 2430.42] And there are quite a few.
[2430.72 → 2432.54] There are also a lot of companies that are still hiring.
[2432.84 → 2434.28] Like I saw this Twitter thread.
[2434.36 → 2434.52] Yeah.
[2434.64 → 2440.04] It was talking about how basically like somebody was at a CTO forum and half of the people were like, oh, I'm worried we're going to do layoffs.
[2440.08 → 2443.14] And half of the people were like, oh my gosh, I can finally hit my hiring goals.
[2443.14 → 2444.14] Like this will be great.
[2444.14 → 2453.04] So it definitely like seems like there's stuff going on, but there's also company – it's not like universal.
[2453.70 → 2458.42] It's not something where every tech company all of a sudden is laying people off or stopping hiring.
[2458.54 → 2459.70] I mean, my company, we're still hiring.
[2459.90 → 2469.88] We are looking at and potentially like shifting some of our later in the year hiring targets because we were planning to continue hiring very rapidly.
[2470.06 → 2472.62] But like short term, we're still hiring tons of folks.
[2472.62 → 2475.18] Because I have – we had a couple – we're small, right?
[2475.20 → 2476.92] But we had new engineers start this week.
[2476.98 → 2478.36] I have new engineers starting in two weeks.
[2478.46 → 2479.56] Like my team is growing.
[2480.12 → 2480.30] Yeah.
[2480.74 → 2484.72] At AWS, we're still hiring like crazy as well.
[2484.82 → 2486.78] Like can't find enough engineers still.
[2486.98 → 2488.62] So that's one side of it.
[2488.76 → 2489.16] Yeah.
[2489.28 → 2490.78] The sky is not falling everywhere.
[2491.20 → 2491.46] Yeah.
[2491.46 → 2495.92] So I was trying to think about what are the actual dynamics here, right?
[2495.94 → 2499.56] And I feel like there's a couple of things going on, and they're all kind of hitting at the same time.
[2499.56 → 2508.56] So like one is there were, as you highlighted, like there's a set of companies that grew really fast all of a sudden because of the pandemic.
[2509.44 → 2513.62] And perhaps grew based on the assumption that this was going to change things forever.
[2513.62 → 2517.14] And then it's looking like it's not going to change things forever.
[2517.14 → 2527.16] So things like food delivery companies and teleconferencing companies and e-commerce companies, like all of these had a massive change all of a sudden from the pandemic.
[2527.84 → 2529.74] And hired massively.
[2530.10 → 2535.34] And a lot of them are doing layoffs now because – I mean, the pandemic is still ongoing.
[2535.34 → 2543.56] There's a ton of COVID out there, but also a lot of people are kind of over it, and they're going back to work in person, and they're eating out and all these other things.
[2543.72 → 2547.76] So the demand has not stayed elevated in the same way.
[2548.38 → 2549.66] Travelling in conferences too.
[2550.22 → 2551.08] Travelling is starting.
[2551.24 → 2552.20] Conferences are starting.
[2552.66 → 2552.96] Yeah.
[2553.28 → 2555.38] So I think that's one dynamic.
[2555.88 → 2560.80] And I don't know, are there other categories of things that fit in there that people, if they're working in that space, should be worried about?
[2561.22 → 2562.52] I'm not sure.
[2562.52 → 2569.28] I think that one that we've seen already is like e-commerce get hit really bad and growth tech more generally.
[2569.86 → 2579.50] Just watching my portfolio of stocks, seeing that like, you know, Shopify going way down and other companies in that kind of same realm.
[2579.50 → 2581.28] I've seen a lot of that.
[2581.84 → 2584.44] And then I think the other huge one is crypto.
[2585.06 → 2588.42] That we've seen that that was like just soaring this winter.
[2588.42 → 2593.54] And everybody's like, you know, you got to get in, you got to work for it while you can.
[2593.66 → 2595.12] Like you got to get in on this.
[2595.16 → 2597.90] It's going to be worth 85 X in a year or whatever.
[2597.90 → 2600.14] And then it's really crashed.
[2600.26 → 2604.84] And I'm not sure what the job situation looks like in that realm right now.
[2604.84 → 2609.04] But I think that that's another industry that's probably really struggling right now.
[2609.04 → 2620.10] Yeah, I feel like crypto is kind of a particular case of a broader thing, which is like companies that were very dependent on how much capital was like sloshing around.
[2620.10 → 2623.32] Like I'm a very crypto skeptic on a lot of things.
[2623.32 → 2631.68] And whether you're a crypto skeptic or crypto positive, I think you'll probably agree that a huge amount of the money flowing into crypto was just capital trying to find returns.
[2631.68 → 2636.14] There's capital flowing around because we had very, very loose capital and that has started to end.
[2636.64 → 2639.32] There are all sorts of capital tightening that is happening.
[2639.96 → 2641.80] And I think that's hitting crypto.
[2642.12 → 2646.66] I think that's likely to hit real estate and real estate sales are already slowing.
[2646.80 → 2650.82] But I think companies that are serving the real estate market may end up getting hit there.
[2651.34 → 2656.94] And kind of anyone else who's depending on there being really, really cheap capital,
[2656.94 → 2662.28] because we've gone from an era of cheap capital to an era where capital is getting more expensive.
[2662.62 → 2669.08] That's also very like cyclic because every like VCs are you'd think VCs are risk tolerant,
[2669.08 → 2672.86] but VCs are like the most risk-averse people in so many ways.
[2673.02 → 2674.78] And so they're like, oh, things are tightening.
[2675.02 → 2676.04] I got to tighten too.
[2676.18 → 2679.46] And so all of these open spigots of money are shutting down.
[2679.64 → 2685.04] And so anyone who's dependent on that, like really cheap available capital, they're running into challenges.
[2685.04 → 2687.00] Who's not hit?
[2687.20 → 2690.02] You mentioned AWS is not hit too much.
[2690.38 → 2691.04] At least not yet.
[2691.10 → 2693.64] We're still hiring like crazy right now.
[2693.80 → 2697.18] So, I mean, if anybody is looking, feel free to reach out.
[2697.58 → 2699.12] I can definitely set you up there.
[2699.40 → 2700.48] But I don't know.
[2700.58 → 2707.02] So far, being at a bigger company, I've felt a little bit isolated from it personally.
[2707.50 → 2710.40] But that's just been my experience so far.
[2710.40 → 2715.64] It seems like the more established companies, meaning like they have like means of revenue,
[2715.92 → 2719.62] they're less affected by it, at least for right now.
[2719.90 → 2721.34] But who knows how that could change?
[2721.70 → 2721.84] Yeah.
[2721.94 → 2726.40] Companies that are profitable probably are a little bit safer as well because they're not
[2726.40 → 2728.24] reliant on just funding.
[2728.50 → 2730.98] They can actually make the money themselves as well.
[2731.90 → 2732.42] Yeah.
[2732.50 → 2737.64] We have heard things about like hiring freezes at some of the bigger tech companies.
[2737.94 → 2738.22] Yeah.
[2738.22 → 2738.30] Yeah.
[2738.80 → 2739.22] Let's see.
[2739.52 → 2741.54] I know Meta had one.
[2741.74 → 2743.38] I did Google as well.
[2743.62 → 2744.26] I'm not sure.
[2744.46 → 2746.26] I don't think Google, but I think Twitter.
[2746.64 → 2746.92] Twitter.
[2747.18 → 2749.08] Which I guess is less big, but.
[2749.26 → 2750.28] That makes sense though.
[2750.54 → 2751.64] Weird in the middle there.
[2752.12 → 2755.62] And Meta, like they're betting everything on something that's not going to be ready for
[2755.62 → 2755.96] years.
[2756.20 → 2756.40] So.
[2756.76 → 2757.04] Yeah.
[2757.20 → 2758.24] It makes sense there too.
[2758.48 → 2762.62] It seems like social media in general might be a little bit impacted, which I think goes
[2762.62 → 2766.86] along with what we've been saying is that social media grew a lot during the pandemic
[2766.86 → 2768.70] because people were stuck online.
[2768.80 → 2770.62] They couldn't see people in person.
[2770.62 → 2776.02] And so it makes sense that they might be declining or shrinking a little bit due to
[2776.02 → 2778.86] the change in people's lifestyles.
[2779.38 → 2779.56] Totally.
[2780.34 → 2782.08] They're also very ad focused.
[2782.08 → 2787.92] And so depending on where their advertising money is coming from, like, I don't know how
[2787.92 → 2792.30] many of our listeners remember back to like the 01 crash, but a huge amount of that crash
[2792.30 → 2797.26] was because all the ad focused tech companies, their revenue was being propped up by other
[2797.26 → 2797.80] tech companies.
[2797.80 → 2801.28] And so some of them started and then that cut everybody's revenue all at once.
[2801.86 → 2804.40] Tech has diversified massively since then.
[2804.40 → 2810.90] But I wouldn't be surprised if, for example, a lot of Facebook's ad revenue was from other
[2810.90 → 2814.64] companies that had grown massively during the pandemic and are cutting back.
[2814.80 → 2819.52] That may, you know, depending on who's advertising on your channel, anyone whose ad focused may
[2819.52 → 2821.00] get that kind of knock on effect.
[2821.78 → 2822.84] Yeah, we're hiring as well.
[2822.98 → 2824.64] We're much smaller than AWS.
[2825.10 → 2828.16] But, you know, if you're interested in working in a small company, you can hit me up.
[2828.20 → 2830.40] I know there are lots of folks out there still hiring.
[2830.40 → 2837.00] So I think coming back to what should an individual do if you're concerned about this, which, you
[2837.00 → 2838.80] know, it's fair to be concerned.
[2838.94 → 2842.20] I think there are going to be a lot of people impacted.
[2842.68 → 2847.46] So Nick and Allie, what would your recommendations be for people who are maybe feeling a little
[2847.46 → 2848.02] bit uncertain?
[2848.66 → 2853.04] I think my first piece of advice is that if you're already employed somewhere, it's probably
[2853.04 → 2858.30] a pretty good time to stay there and not to job hop for the most part.
[2858.30 → 2865.74] I think for the reason that at a lot of companies, like layoffs are first in, first out or last
[2865.74 → 2867.30] in, first out, I guess.
[2867.50 → 2873.64] So if you were recently hired, you probably have a better probability of being one of the
[2873.64 → 2874.70] first people laid off.
[2875.34 → 2881.98] And so I would suggest if you've been somewhere, it's probably a pretty good time to sit tight.
[2881.98 → 2888.78] But if you were laid off to definitely reach out to your network, a lot of more tech things
[2888.78 → 2890.60] are happening right now.
[2891.20 → 2893.80] And so make sure to solidify that.
[2893.96 → 2898.66] It's also a good time to learn new skills and make sure that you're keeping on top of
[2898.66 → 2899.56] the industry.
[2899.88 → 2902.06] So that would be my basic advice.
[2902.76 → 2902.86] Yeah.
[2902.94 → 2904.54] I was going to say kind of the same thing.
[2904.54 → 2907.76] Like don't assume too much of a safety net ever, really.
[2907.94 → 2912.80] You can pretty much be let go at any time for any reason in this country, at least.
[2913.58 → 2919.30] And it's always best to be a little selfish on that, like looking out for yourself and
[2919.30 → 2922.48] kind of preparing or having like a basic preparation.
[2922.62 → 2927.34] You don't have to like be ready to walk out the door to moment's notice, but keep your tech
[2927.34 → 2929.60] skills up, keep your interviewing skills up.
[2929.60 → 2934.52] And you can still be on the lookout for those opportunities because they usually stick around
[2934.52 → 2935.02] for a while.
[2935.12 → 2938.78] So, you know, like something happens, this is where I'm going to go immediately.
[2939.02 → 2941.46] And your network is a great first place to start.
[2941.78 → 2944.22] Well, and you can, you know, you talked about keeping your tech skills up.
[2944.28 → 2948.10] You can keep your network warm to reach out to folks, even though you're not looking and
[2948.10 → 2949.18] reopen conversations.
[2949.18 → 2950.16] How are you doing?
[2950.40 → 2951.64] How is it where you're working?
[2951.76 → 2952.70] Are you all still hiring?
[2952.88 → 2953.90] Oh, okay, cool.
[2953.90 → 2958.50] You know, and so then, you know, if something happens, and suddenly you need to find something,
[2958.74 → 2960.68] you have, they've already got you in mind.
[2961.18 → 2966.08] You've Sussex out where there are maybe opportunities, and it's really fast.
[2966.20 → 2968.64] Now, I'm very network driven, but I've been here.
[2968.98 → 2970.92] I've been in the industry for almost 20 years at this point.
[2971.02 → 2972.44] What about folks who are new to the industry?
[2972.56 → 2977.42] What can they do to kind of survive and hopefully even thrive at this moment?
[2977.66 → 2981.80] Well, I think the same is true that networking, even if that network is new, is so important.
[2981.80 → 2986.18] And if you can build that network when you don't need anything from them, that's how
[2986.18 → 2990.32] you're going to build the most authentic network that's going to be there when you do need
[2990.32 → 2996.08] something and make sure that the relationship is mutual as well, that you're giving in some
[2996.08 → 2997.84] way, not just taking.
[2998.18 → 3003.52] And so for a lot of people though, that like giving you a job at their company is like really
[3003.52 → 3004.72] great for them as well.
[3004.82 → 3008.54] So I'm not saying to, you know, not ask for that or anything like that, but if you're just
[3008.54 → 3012.54] like constantly asking people code questions or, Hey, can you do this for me?
[3012.56 → 3013.28] Can you do this for me?
[3013.32 → 3014.10] Can you do this for me?
[3014.70 → 3019.58] It makes it feel like it's a one directional, like par asocial type relationship.
[3019.58 → 3023.18] So make sure that it's mutual and that you have things that you're conversing about, that
[3023.18 → 3026.30] you're checking in on them, seeing how you can help them as well.
[3026.74 → 3027.58] That's one big thing.
[3027.84 → 3028.60] Events are happening.
[3029.00 → 3032.82] So if you're comfortable going to those, it's a great time to do that.
[3032.82 → 3035.30] But you can also network a ton online too.
[3035.80 → 3040.94] The best way I've found is to learn in public, like write blog posts about what you're learning.
[3041.08 → 3045.18] You don't have to be like a 10X expert in the industry for 50 years in order to write
[3045.18 → 3046.18] a good blog post.
[3046.50 → 3050.36] You can have learned something a couple of weeks ago and still be able to teach something
[3050.36 → 3051.30] pretty well to people.
[3051.80 → 3056.40] And I have found that that works really, really well for people trying to look for jobs is
[3056.40 → 3060.34] to just teach somebody else something and give back to the community because you're proving
[3060.34 → 3063.42] your skills, and you're also getting yourself out there.
[3063.74 → 3065.74] So that's my biggest piece of advice, I think.
[3066.32 → 3067.32] Nick, anything from you?
[3067.72 → 3070.32] I mean, Allie, you kind of nailed it along a number of dimensions.
[3071.02 → 3072.06] Yeah, I really like that.
[3072.10 → 3075.88] Just kind of like reiterating, like there's always people that know more than you and there's
[3075.88 → 3081.50] always people that know less than you and your insight into how you learn things or just
[3081.50 → 3083.54] sharing what you have learned is always valuable.
[3084.14 → 3085.52] So somebody will find it valuable.
[3085.92 → 3086.26] Definitely.
[3086.26 → 3091.20] And I think we don't talk about portfolios as much anymore, but I think that's still
[3091.20 → 3097.56] a really, really great way to display your skills, especially if you're a newbie, showing
[3097.56 → 3102.88] that you have built X app and then explain your process for building it and what technology
[3102.88 → 3105.70] you used, why you decided to do things X and Y way.
[3105.90 → 3111.08] That's going to go really far and also actually really prepare you for interviews too, because
[3111.08 → 3114.46] that's going to be a lot of the things that you're asked, like the trade-offs and all
[3114.46 → 3114.70] that.
[3114.88 → 3120.18] So that's another thing that you can do if you're unemployed and trying to become employed.
[3120.90 → 3127.48] One other thing that I'm going to put out there for folks is if you have time, getting
[3127.48 → 3134.26] involved with an open source project is another useful way to network and also build a track
[3134.26 → 3134.54] record.
[3134.62 → 3140.24] Because a lot of the challenge in hiring folks who are newer to the industry, I speak
[3140.24 → 3143.18] this now as a hiring manager is there's no track record.
[3143.46 → 3148.38] I have no idea looking at your resume if you are just out of school or just out of boot
[3148.38 → 3148.92] camp or whatever.
[3149.10 → 3154.34] I have no idea if you're one of the boot camp grads who's going to be amazing or one of the
[3154.34 → 3156.96] boot camp grads who still doesn't know anything about code.
[3157.46 → 3160.34] And we can try to figure that out.
[3160.38 → 3161.60] But a lot of companies won't bother.
[3162.16 → 3164.64] A lot of companies look, they'll say, eh, not worth our time.
[3164.64 → 3169.02] And I can tell you, we're right now, it's hard to filter through boot camp grads.
[3169.08 → 3171.66] We've got hundreds of boot camp grads applying.
[3172.18 → 3173.90] And it takes a lot of time and energy.
[3174.08 → 3174.98] And we care a lot.
[3175.12 → 3176.88] So we're figuring out how do we work through this.
[3176.94 → 3178.06] But it is really hard.
[3178.12 → 3180.04] And a lot of companies will just say, no, you know what?
[3180.16 → 3183.50] If you don't have any track record, I'm not even going to bother talking with you.
[3183.82 → 3186.92] And so looking for ways to manufacture that track record.
[3187.60 → 3190.00] And one way you can do that is getting involved with open source.
[3190.00 → 3195.12] And if you can show a history of contribution to a project, that is a track record.
[3195.28 → 3198.42] The people who are on that project are going to know of you.
[3198.52 → 3200.58] They become a proto network, a set of people.
[3200.78 → 3206.00] So I think I hesitate to point everyone there because it does take a time commitment.
[3206.38 → 3209.18] And not everyone has the ability to put that time in.
[3209.44 → 3213.36] But if you do, that can be a great way to kind of hack around that lack of track record.
[3213.90 → 3218.28] Another thing that's very related to that that helped me early on in my career is getting
[3218.28 → 3221.12] involved with the local community, the local dev community.
[3221.68 → 3222.24] I'm in Omaha.
[3222.50 → 3223.68] It's not a huge community.
[3224.06 → 3227.52] But there's some very niche people that I got to know.
[3227.82 → 3233.98] And I got several offers and accepted a few just from word of mouth or from we knew each
[3233.98 → 3237.36] other from going to the Pearl meetup or things like that.
[3237.54 → 3241.04] Like just getting involved early on really helped my career tremendously.
[3241.04 → 3246.56] It's harder now to give that advice, I think, in a pandemic slash post-pandemic world where
[3246.56 → 3248.80] those things exist or don't anymore.
[3249.42 → 3249.62] Yeah.
[3249.80 → 3251.46] I think a lot of them are coming back.
[3251.58 → 3254.72] But even the ones that aren't, they're still like virtual events.
[3254.76 → 3262.06] Or you can use social media in that same kind of way that we used in-person events back in
[3262.06 → 3262.40] the day.
[3262.74 → 3263.08] For sure.
[3263.34 → 3268.82] I will also say that as a fellow hiring manager that a lot of times if you can build some sort
[3268.82 → 3274.38] of relationship with those hiring managers, that tends to help out a little bit as well.
[3274.58 → 3278.46] So if you can, it just all goes back to networking, right?
[3278.58 → 3282.24] Building up that strong network and making relationships.
[3282.52 → 3283.76] Like I saw this so much.
[3283.80 → 3285.18] I used to teach at a coding boot camp.
[3285.44 → 3293.82] And I also used to hire a lot of juniors of this kind of like spray technique for applying
[3293.82 → 3299.86] applying to jobs of just submitting a resume every single place you could and applying
[3299.86 → 3301.34] for every single job on LinkedIn.
[3302.16 → 3306.14] And in a lot of cases, those types of jobs get like thousands of applicants.
[3306.34 → 3312.82] And so it's impossible to get to the top of that pile of resumes if you don't have some
[3312.82 → 3318.50] sort of like knowledge of somebody at the company or some sort of personal outreach or
[3318.50 → 3319.54] something along those lines.
[3319.54 → 3323.38] So if you can find, hey, this is like the hiring manager for the role, I'm going to
[3323.38 → 3327.08] write them an email about how I'm like qualified for it or whatever.
[3327.36 → 3331.46] I think that things like that can go a long way too, because you can get really, really
[3331.46 → 3333.32] lost in that like sea of applicants.
[3333.64 → 3337.56] Or if you've met them at a meetup or something along those lines, that goes a long way too.
[3338.22 → 3338.36] Totally.
[3338.64 → 3340.20] In the end, we are still human.
[3340.92 → 3343.98] And reaching out as a human makes a big difference.
[3344.70 → 3345.10] Awesome.
[3345.10 → 3350.92] Well, any last things you all want to leave folks with, or should we call this a wrap?
[3351.24 → 3352.56] I think we're probably pretty good.
[3353.86 → 3354.34] Amazing.
[3354.64 → 3354.94] All right.
[3355.06 → 3363.78] Well, thank you everyone for joining us for this JS party for the inaugural WTF JS for a
[3363.78 → 3367.50] discussion about maintainable code bases and a look at this moment in technology.
[3367.66 → 3368.78] We'll catch you all next week.
[3368.78 → 3374.50] If you're listening, and you want to join us live, you can always join us live at on Thursdays
[3374.50 → 3376.18] at 10 a.m.
[3376.28 → 3377.92] Pacific, one o'clock Eastern.
[3378.20 → 3381.34] And who knows what it is in Omaha, but we'll play with you all.
[3381.56 → 3381.86] All right.
[3382.08 → 3382.94] Take it easy, you all.
[3382.94 → 3398.90] All right.
[3398.96 → 3400.24] That is our show for this week.
[3400.38 → 3401.82] Now's a great time to subscribe.
[3402.08 → 3405.54] If you haven't yet, head to jsparty.fm for all the ways.
[3405.68 → 3410.06] And if you're a longtime listener of the pod, pay it forward and share JS party with a friend.
[3410.06 → 3413.70] We love when new folks join the party and tell us they were personally recommended.
[3414.06 → 3414.48] So cool.
[3415.06 → 3416.00] Oh, and here's something new.
[3416.32 → 3421.44] You can now buy a changelog sticker pack from our merch shop or just get one for free when
[3421.44 → 3422.82] you join changelog plus.
[3423.02 → 3423.32] Yep.
[3423.40 → 3427.36] We are adding stickers to the bag of goodies you receive for directly supporting our work.
[3427.60 → 3430.48] Learn more at changelog.com slash plus.
[3430.88 → 3435.32] Thanks again to Vastly for CD ending for us to Break master Cylinder for cranking out the
[3435.32 → 3436.88] beats and to you for listening.
[3436.88 → 3442.70] Next up on the pod, Josh Goldberg, the author of Learning TypeScript, will be our guest.
[3442.90 → 3445.88] We'll have that episode ready to put in your holes next week.
[3445.88 → 3475.26] Game on.
