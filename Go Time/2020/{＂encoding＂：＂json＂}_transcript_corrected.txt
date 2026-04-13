[0.00 → 0.96] There are some bugs.
[1.24 → 5.40] For example, there's one that I would say affects most code bases out there,
[5.50 → 8.90] which is the standard, you know, you have an HTTP endpoint
[8.90 → 11.36] and the body is JSON, so you want to decode it.
[11.72 → 14.30] So what you do is you take the r.body
[14.30 → 17.90] and you do Jason.new decoder.decode with the body
[17.90 → 19.48] and then into some structure.
[20.04 → 22.24] And if you do that, it's buggy if you just do that.
[22.64 → 23.62] I've just got to go.
[24.64 → 25.92] What do you mean it's buggy?
[26.10 → 27.14] Tell me why, please.
[27.14 → 31.94] Bandwidth for Changelog is provided by Vastly.
[32.30 → 34.22] Learn more at Fastly.com.
[34.44 → 37.52] We move fast and fix things here at Changelog because of Rollbar.
[37.64 → 39.34] Check them out at Rollbar.com.
[39.58 → 41.76] And we're hosted on Linde Cloud Servers.
[42.06 → 44.10] Head to linode.com slash changelog.
[46.76 → 49.80] Linde makes cloud computing simple, affordable, and accessible.
[50.22 → 51.78] Whether you're working on a personal project
[51.78 → 53.76] or managing your enterprise's infrastructure,
[53.76 → 56.92] Linde has the pricing, support, and skill you need
[56.92 → 58.32] to take your ideas to the next level.
[58.68 → 60.34] We trust Linde because they keep it fast
[60.34 → 61.44] and they keep it simple.
[61.76 → 64.24] Check them out at linode.com slash changelog.
[74.54 → 75.40] Let's do it.
[76.10 → 77.04] It's go time.
[77.04 → 79.16] Welcome to Go Time,
[79.38 → 81.24] your source for diverse discussions
[81.24 → 82.48] from around the Go community.
[83.10 → 86.14] This episode is like a two for the price of one.
[86.44 → 88.22] You get a fascinating conversation
[88.22 → 90.28] about Go's encoding JSON package
[90.28 → 91.90] plus a murder mystery
[91.90 → 94.08] as a sneaky little bug was determined
[94.08 → 95.32] to kill Daniel's laptop.
[95.66 → 96.62] Don't miss the post show
[96.62 → 98.32] because Daniel put on his sleuthing hat
[98.32 → 100.70] and cracked the case just in the nick of time.
[101.26 → 103.54] Okay, here we go.
[103.54 → 111.76] Hello and welcome to Go Time.
[111.94 → 112.58] I'm Matt Raya.
[112.70 → 114.68] Today we're talking about JSON.
[115.38 → 116.60] You'd be forgiven for thinking
[116.60 → 118.70] this is going to be the most boring episode,
[118.96 → 121.80] but I guarantee you it will not be.
[122.28 → 124.56] Joining me today, Johnny Portico.
[124.92 → 125.46] Hello, Johnny.
[126.12 → 126.64] Hello, Matt.
[127.00 → 128.44] Have you had a good week so far?
[128.98 → 130.70] Yes, we're about to talk about JSON,
[130.88 → 131.34] so I don't know.
[131.84 → 132.44] We'll see.
[132.88 → 133.44] Let's see.
[134.50 → 135.36] Don't worry, though.
[135.52 → 137.62] We do have a great guest today,
[137.74 → 139.86] a very prolific contributor to Go.
[140.20 → 141.76] You've probably seen his name around.
[142.20 → 142.98] Daniel Marty.
[143.30 → 143.98] Hello, Daniel.
[144.48 → 145.46] Hi, happy to be here.
[145.86 → 146.72] Welcome to the show.
[146.82 → 147.56] Great to have you.
[148.06 → 149.52] Have you had a good week so far?
[149.92 → 151.96] Yeah, we almost got to 20 degrees in the UK,
[152.10 → 152.74] so that was nice.
[152.96 → 154.58] But summer was over a few weeks ago.
[154.72 → 155.66] It only lasted for a weekend.
[156.54 → 158.42] Yes, we do have some more heat coming
[158.42 → 159.70] later this week,
[159.70 → 161.16] so stay tuned for that.
[161.66 → 163.54] I don't know why I sound like a news anchor.
[164.60 → 166.72] I'm just trying to be a normal human,
[166.86 → 168.22] but I find that difficult sometimes.
[168.62 → 170.04] Okay, so let's start then.
[170.16 → 171.54] Just quickly for beginners,
[171.70 → 174.52] in case there's somebody that's really brand new,
[174.80 → 176.44] what is JSON?
[176.76 → 177.94] Do you say it like that?
[178.02 → 178.86] Do you say JSON,
[179.04 → 180.74] or do you pronounce it some other way?
[181.10 → 182.22] So I just say JSON,
[182.70 → 185.80] and I think if I had to explain this to a little kid,
[185.80 → 190.32] I would say it's kind of like a way to represent data,
[190.70 → 193.20] and I've already gone up the window,
[193.30 → 194.66] the plan to explain this to a little kid.
[194.98 → 195.78] No, kids get that.
[196.04 → 198.32] Let's assume it's a really smart kid.
[199.28 → 199.76] Yeah.
[200.32 → 203.16] So it's like a very generic way to represent data,
[203.46 → 206.02] so it doesn't matter who the other reader is,
[206.14 → 207.12] who's on the other side.
[207.60 → 209.76] They most likely will be able to read that data.
[210.22 → 212.70] Yeah, and it's JavaScript object notation,
[212.70 → 214.94] so it comes out of JavaScript,
[215.82 → 219.38] but it turns out to be really kind of useful across a lot.
[219.56 → 222.64] Every language really has now some kind of JSON support.
[223.26 → 224.94] It's practically everywhere.
[225.52 → 227.82] Practically every language out there that's modern today
[227.82 → 229.88] has to have JSON support because you just do,
[230.16 → 231.74] and your computer, you might not see it,
[231.76 → 234.06] but it definitely is running JSON at some level.
[234.94 → 236.52] Yeah, and so there's like,
[236.80 → 238.76] it's an object, and it has fields,
[238.90 → 240.84] and those fields have some types,
[240.84 → 243.14] and it's the types that we're used to as well in Go,
[243.26 → 246.42] like strings and numbers and Booleans,
[246.96 → 249.02] any others, other objects, arrays,
[249.30 → 250.04] those kinds of things.
[250.12 → 251.64] I think that might be the whole list.
[252.06 → 255.50] And why did it get such popular use on the web?
[255.78 → 258.00] I mean, it kind of is kind of perfect,
[258.10 → 259.82] isn't it, for web technologies?
[260.36 → 262.06] I would say it came from the
[262.46 → 264.04] from all the success that browsers had,
[264.24 → 265.40] you know, the modern web had,
[265.40 → 268.00] and, you know, suddenly HTTP, HTML,
[268.74 → 270.94] CSS, and JavaScript, and JSON,
[271.16 → 273.54] all these technologies kind of took everybody by surprise.
[274.02 → 275.64] Initially, everybody thought they were just toys,
[276.18 → 278.60] but now suddenly people are building real companies
[278.60 → 279.20] on top of them.
[279.86 → 281.78] And JSON is just, you know,
[282.18 → 283.02] has too much momentum.
[283.62 → 285.76] I don't think anything is ever going to replace it
[285.76 → 286.64] at this point, honestly.
[287.94 → 289.26] That's fascinating.
[289.58 → 290.40] Well, hang on.
[290.58 → 292.66] I'd like to add something here.
[292.66 → 294.78] I like what you said, Daniel.
[295.46 → 297.20] There's another reason, I think,
[297.34 → 298.56] my personal reasons as well,
[298.90 → 300.40] why I think JSON sort of took off.
[301.04 → 303.02] Because primarily, for me,
[303.20 → 305.52] it was because it was not XML,
[306.18 → 307.80] which is prior to that.
[308.56 → 310.48] Prior to JSON taking over.
[311.26 → 313.40] If you want to sort of interchangeable format
[313.40 → 315.26] with other systems and things like that,
[315.40 → 316.28] you know, sort of JSON,
[317.00 → 317.82] or rather XML,
[318.20 → 321.12] was the sort of the default go-to, right?
[321.12 → 323.40] And then we created a whole, like,
[323.70 → 325.22] ecosystem around XML,
[325.64 → 326.34] like parsing,
[326.44 → 327.14] XSLT,
[327.42 → 328.18] and templates,
[328.36 → 328.68] style sheets,
[328.74 → 329.50] and all kinds of,
[330.08 → 330.38] really,
[330.64 → 331.96] looking back,
[332.22 → 334.30] kind of brilliant technology for the times,
[334.42 → 335.08] but just really,
[335.24 → 336.72] really hard to sort of work with.
[337.16 → 338.86] You really had to depend on
[338.86 → 340.60] sort of machine-generated XML.
[340.72 → 342.06] Because sitting down and sort of
[342.06 → 344.16] editing XML by hand,
[344.50 → 345.62] especially like huge,
[345.72 → 347.06] large documents,
[347.24 → 347.80] like dealing with that,
[347.86 → 348.00] I mean,
[348.02 → 349.22] that was just maddening.
[349.22 → 351.08] So here comes JSON
[351.08 → 352.74] making it very simple,
[352.90 → 354.08] very human-readable,
[354.32 → 354.54] right?
[354.90 → 356.52] And it was like a breath of fresh air.
[356.70 → 357.46] So absolutely,
[358.06 → 359.08] to corroborate sort of
[359.08 → 359.92] the idea that
[359.92 → 361.52] basically it sort of became
[361.52 → 362.50] very, very popular
[362.50 → 364.34] with the rise of
[364.34 → 364.70] HTML,
[364.88 → 365.10] JavaScript,
[365.24 → 365.46] CSS,
[365.64 → 366.68] like building applications,
[366.86 → 367.06] right,
[367.48 → 368.08] on the web,
[368.84 → 370.80] from a systems and data interchange
[370.80 → 371.24] standpoint,
[371.44 → 372.32] it was revolutionary
[372.32 → 373.20] just as much.
[373.72 → 373.86] Yeah,
[373.90 → 375.16] and it's simpler also
[375.16 → 376.58] than XML too,
[376.58 → 377.90] because in XML,
[378.06 → 379.12] you can do weird things
[379.12 → 379.84] with the structure,
[379.96 → 381.40] like you can just have siblings
[381.40 → 382.82] next to each other.
[383.24 → 384.52] That gets very complicated
[384.52 → 385.54] to work with.
[385.88 → 387.02] You can't do that
[387.02 → 387.58] with JSON,
[388.10 → 388.44] can you?
[388.62 → 388.86] You know,
[388.94 → 390.78] there is a tighter structure
[390.78 → 391.20] to it,
[391.22 → 392.04] and I think that kind of
[392.04 → 392.70] helps as well.
[393.24 → 394.68] What about any gotchas
[394.68 → 396.10] with working with JSON?
[396.26 → 397.20] Is there anything that
[397.20 → 398.16] beginners ought to
[398.16 → 399.18] watch out for?
[399.32 → 400.62] One thing that occurred
[400.62 → 401.52] to me is
[401.52 → 402.56] in Go,
[403.20 → 404.02] if you have a
[404.02 → 406.18] time. Time type,
[406.68 → 407.18] so you're going to
[407.18 → 408.48] represent a time as JSON,
[408.74 → 410.36] it turns that into a string,
[410.44 → 410.72] doesn't it?
[410.94 → 411.08] Yeah,
[411.42 → 412.56] I'm actually not sure
[412.56 → 413.42] exactly what happens
[413.42 → 414.20] because I usually just
[414.20 → 415.30] write custom code
[415.30 → 416.66] to handle times in JSON.
[417.24 → 417.46] Really?
[417.52 → 417.70] Why?
[418.44 → 419.36] Most of the time,
[419.46 → 421.08] people will want times,
[421.44 → 422.54] or rather timestamps
[422.54 → 423.68] in a very specific format,
[424.24 → 425.82] so they will write the code
[425.82 → 426.56] to handle that.
[426.98 → 428.10] So I actually don't remember
[428.10 → 429.36] what the default behaviour is,
[429.36 → 430.82] but yes,
[431.06 → 431.88] JSON doesn't have
[431.88 → 432.68] a timestamp type,
[432.80 → 434.08] so it will just end up
[434.08 → 434.48] as a string.
[435.24 → 435.38] Yeah.
[435.88 → 436.50] It's fine,
[436.56 → 437.88] as long as the thing
[437.88 → 439.22] that's interpreting it
[439.22 → 440.98] also understands that format
[440.98 → 442.48] and can then work with it.
[442.52 → 443.38] But that's quite an interesting
[443.38 → 443.96] point,
[444.06 → 444.48] is that
[444.48 → 446.24] there are some rudimentary
[446.24 → 447.56] types in JSON,
[447.84 → 449.20] and sometimes you have to
[449.20 → 450.48] do a bit of magic
[450.48 → 452.16] to turn your particular data
[452.16 → 453.46] into something that's going to work
[453.46 → 455.02] in that text-based
[455.02 → 455.72] kind of format.
[456.04 → 456.66] And another thing
[456.66 → 457.38] that's quite weird
[457.38 → 458.00] is that
[458.00 → 459.04] by default,
[459.04 → 459.96] I think the
[459.96 → 461.38] numbers are all
[461.38 → 463.06] float64 type.
[463.26 → 463.82] If you're working
[463.82 → 465.70] with generic data,
[465.92 → 466.74] you can use the
[466.74 → 468.08] map string interface type
[468.08 → 468.60] in Go
[468.60 → 470.80] to Marshall JSON into,
[470.90 → 472.24] and it will work.
[472.42 → 472.64] You know,
[472.66 → 474.16] it will fill that map up
[474.16 → 475.52] as like it's the object.
[475.74 → 476.38] But of course,
[476.50 → 477.50] if there are the numbers
[477.50 → 478.02] in there,
[478.10 → 478.96] it's not sure
[478.96 → 479.86] whether it's a
[479.86 → 480.74] floating point number
[480.74 → 481.68] or an integer or whatever,
[481.78 → 482.62] and so it just uses
[482.62 → 484.14] the most kind of
[484.14 → 485.56] useful type
[485.56 → 487.38] or the most versatile type,
[487.50 → 488.22] the float64.
[488.22 → 489.54] I found that to be
[489.54 → 490.56] quite strange
[490.56 → 491.50] when I first started
[491.50 → 493.54] working with JSON in Go.
[494.00 → 494.64] And I actually think
[494.64 → 495.66] numbers are a really
[495.66 → 496.68] interesting point
[496.68 → 498.70] because I think
[498.70 → 499.46] JSON could have gone
[499.46 → 500.30] one of two ways.
[500.48 → 501.42] One of them would have been,
[501.64 → 501.78] you know,
[501.78 → 502.46] you've got integers
[502.46 → 503.22] on one side
[503.22 → 504.20] and you've got floats
[504.20 → 504.56] on the other,
[504.80 → 505.40] and then you define
[505.40 → 506.28] what the sizes and bits
[506.28 → 506.74] of those are.
[507.00 → 507.42] So for example,
[507.50 → 507.96] if this was Go,
[508.02 → 508.60] we could have said
[508.60 → 510.72] n64 and float64.
[510.72 → 512.42] and that has
[512.42 → 513.08] some advantages.
[513.36 → 514.00] It's stricter.
[514.32 → 515.06] So if you want to use
[515.06 → 515.72] one or the other,
[516.28 → 517.10] it's guaranteed
[517.10 → 518.42] that it's going to
[518.42 → 519.10] stay that way
[519.10 → 519.70] and you're not going
[519.70 → 520.34] to lose any precision
[520.34 → 521.14] or anything like that.
[521.66 → 522.54] But on the other hand,
[522.58 → 523.04] if you just say
[523.04 → 523.76] it's going to be a number,
[524.04 → 525.50] then that opens
[525.50 → 526.44] the door to,
[526.50 → 526.92] for example,
[527.10 → 528.80] supporting arbitrary
[528.80 → 529.74] precision numbers,
[530.38 → 532.08] aka big numbers,
[532.34 → 533.42] which Go also supports
[533.42 → 534.84] with a different package.
[534.84 → 538.08] So the encoding JSON package,
[538.48 → 539.36] which, by the way,
[539.60 → 539.94] Daniel,
[540.06 → 541.56] you actually co-maintain
[541.56 → 543.06] the encoding JSON package
[543.06 → 543.84] in the standard library,
[543.90 → 544.08] right?
[544.48 → 545.06] Yeah, that's right.
[545.28 → 546.50] And I should mention,
[546.58 → 547.30] before we go on,
[547.52 → 548.62] I've noticed something weird
[548.62 → 549.18] in my laptop,
[549.34 → 549.90] which is that
[549.90 → 550.80] my memory usage
[550.80 → 552.90] has been rising steadily
[552.90 → 554.36] for the past 15 minutes.
[554.82 → 555.40] I don't know
[555.40 → 556.44] if that's a bug in Zoom
[556.44 → 558.62] or in my recording program,
[558.72 → 559.54] but I think my laptop
[559.54 → 560.14] is going to crash
[560.14 → 560.98] in about 10 minutes.
[561.90 → 563.24] So if that happens,
[563.34 → 564.14] just FYI.
[564.14 → 566.78] Well, it's exciting, though.
[566.82 → 568.32] It's like there's a bomb
[568.32 → 569.26] that's going to go off
[569.26 → 570.30] and, you know,
[570.68 → 571.70] we're just sort of waiting.
[571.78 → 572.74] It started at 30%.
[572.74 → 574.22] I'm currently at 92%.
[574.22 → 574.84] So, yeah,
[575.04 → 576.18] about five minutes left, maybe.
[576.56 → 577.52] I don't know what's going on.
[578.28 → 578.68] Okay.
[578.86 → 580.48] Well, if you just disappear,
[580.62 → 581.70] we'll assume it's that.
[582.54 → 583.64] I just hope it doesn't happen
[583.64 → 584.44] after, like,
[584.52 → 585.44] Johnny says something
[585.44 → 586.74] and then you just cut off
[586.74 → 587.36] because he's definitely
[587.36 → 588.32] going to take that personally.
[588.90 → 589.26] Apologies.
[589.46 → 590.24] You asked about
[590.24 → 591.32] co-maintaining
[591.32 → 592.04] and coding JSON
[592.04 → 593.82] and yes, that is correct.
[594.14 → 595.38] I've been helping for,
[595.70 → 595.90] I guess,
[596.04 → 597.26] about three or four years now
[597.26 → 599.16] and JSON does have
[599.16 → 600.24] active maintainers.
[600.36 → 601.16] I believe they are
[601.16 → 602.12] Ross,
[602.40 → 602.84] Joe,
[603.10 → 604.24] and Brad.
[604.60 → 605.88] So I started helping
[605.88 → 607.18] mainly with just little bugs
[607.18 → 608.56] and little optimizations.
[608.88 → 609.84] But over time,
[609.98 → 610.98] these are all busy people.
[611.32 → 612.32] So it's gotten to a point
[612.32 → 612.94] that I do
[612.94 → 614.16] almost as much work
[614.16 → 615.36] as they do.
[615.36 → 617.38] And on one hand,
[617.40 → 618.10] it's a very rewarding
[618.10 → 619.42] work because
[619.42 → 621.18] it's a very useful package
[621.18 → 622.24] used by tons of people.
[622.66 → 623.84] But on the other hand,
[623.88 → 624.60] it's kind of stressful.
[625.18 → 625.52] Is it?
[625.58 → 625.80] Why?
[626.04 → 626.74] Well, on one hand,
[626.80 → 628.20] because I'm nearly at 100%.
[628.20 → 630.34] And his memory's run out.
[630.34 → 630.82] There we go.
[631.26 → 631.44] Yeah.
[632.58 → 633.66] Quite literally, yeah.
[633.74 → 634.10] Linux.
[634.10 → 641.22] How much time does your team
[641.22 → 641.94] spend building
[641.94 → 642.56] and maintaining
[642.56 → 643.48] internal tooling?
[643.74 → 644.46] I'm talking about
[644.46 → 645.74] those behind-the-scenes apps,
[645.98 → 647.78] the ones no one else sees,
[648.02 → 648.96] the S3 uploader
[648.96 → 649.70] you built last year
[649.70 → 650.54] for the marketing team,
[650.80 → 651.56] that quick Firebase
[651.56 → 652.32] admin panel
[652.32 → 653.18] that lets you monitor
[653.18 → 654.24] key KPIs,
[654.48 → 655.74] maybe even the tool
[655.74 → 656.76] your data science team
[656.76 → 657.36] hacked together
[657.36 → 658.12] so they can provide
[658.12 → 659.54] custom ad spend analytics.
[660.12 → 660.70] Now, these are tools
[660.70 → 661.26] you need
[661.26 → 662.06] so you build them.
[662.32 → 663.20] And that makes sense.
[663.20 → 665.42] But the question is,
[665.70 → 666.36] could you have built them
[666.36 → 667.06] in less time,
[667.36 → 668.18] with less effort,
[668.46 → 669.26] and less overhead
[669.26 → 670.26] and maintenance required?
[670.58 → 671.22] And the answer
[671.22 → 672.06] to that question is,
[672.34 → 672.76] yes.
[673.18 → 674.50] That's where Retool comes in.
[674.86 → 675.56] Rohan Copra,
[675.64 → 676.30] engineering director
[676.30 → 677.10] at DoorDash,
[677.16 → 677.80] has this to say
[677.80 → 678.36] about Retool.
[678.74 → 678.98] Quote,
[679.24 → 680.22] the tools we've been able
[680.22 → 680.86] to quickly build
[680.86 → 681.38] with Retool
[681.38 → 682.68] have allowed us to empower
[682.68 → 684.64] and scale our local operators,
[685.04 → 685.86] all while reducing
[685.86 → 686.40] the dependency
[686.40 → 687.20] on engineering.
[687.62 → 688.00] End quote.
[688.48 → 688.68] Now,
[688.80 → 690.08] the internal tooling process
[690.08 → 690.58] at DoorDash
[690.58 → 691.24] was bogged down
[691.24 → 692.26] with manual data entry,
[692.26 → 693.42] missed handoffs,
[693.58 → 694.74] and long turnaround times.
[695.04 → 696.24] And after integrating Retool,
[696.52 → 697.22] DoorDash was able
[697.22 → 697.96] to cut the engineering
[697.96 → 698.74] time required
[698.74 → 699.58] to build tools
[699.58 → 700.84] by a factor of 10x
[700.84 → 701.78] and eliminate
[701.78 → 702.48] the error-prone
[702.48 → 703.34] manual processes
[703.34 → 704.26] that plagued their workflows.
[704.68 → 705.08] They were able
[705.08 → 706.38] to empower back-end engineers
[706.38 → 707.28] who wouldn't otherwise
[707.28 → 707.84] be able to build
[707.84 → 708.78] front-ends from scratch.
[709.16 → 709.82] And these engineers
[709.82 → 710.56] were able to build
[710.56 → 711.58] fully functional apps
[711.58 → 712.98] in Retool in hours,
[713.20 → 714.16] not days or weeks.
[714.58 → 715.18] Your next step
[715.18 → 716.22] is to try it free
[716.22 → 717.42] at retool.com
[717.42 → 718.32] slash changelog.
[718.54 → 718.92] Again,
[719.04 → 720.06] retool.com
[720.06 → 720.92] slash changelog.
[720.92 → 724.82] Daniel,
[742.86 → 743.60] what other challenge,
[743.68 → 744.54] why is it stressful
[744.54 → 745.58] maintaining the
[745.58 → 746.82] encoding JSON package?
[746.82 → 747.30] So,
[747.46 → 748.64] I think it's very rewarding
[748.64 → 749.42] because the moment
[749.42 → 750.24] you fix any bug,
[750.48 → 751.36] suddenly there are tons
[751.36 → 751.62] of people
[751.62 → 752.48] that are happy about it.
[752.80 → 753.36] And clearly,
[754.04 → 754.86] there are tons
[754.86 → 755.18] of people
[755.18 → 756.72] that care deeply
[756.72 → 757.54] about how fast
[757.54 → 758.98] the JSON package goes.
[759.42 → 760.50] But on the flip side,
[760.62 → 761.10] because it has
[761.10 → 761.98] so many users,
[762.32 → 763.40] if you mess anything up,
[763.86 → 764.60] you're in big trouble
[764.60 → 765.48] because, you know,
[765.52 → 765.90] people are going
[765.90 → 766.56] to be very angry.
[767.26 → 768.64] And, you know,
[768.66 → 769.28] there's also something
[769.28 → 770.30] called the Go 1
[770.30 → 771.48] compatibility guarantee.
[771.48 → 773.00] And that essentially says
[773.00 → 774.16] if your program works
[774.16 → 775.18] with Go 1.0,
[775.70 → 776.50] it should also work
[776.50 → 777.86] with Go 1.2
[777.86 → 778.62] and Go 1.3
[778.62 → 779.08] and so on.
[779.66 → 780.02] Interesting.
[780.66 → 782.96] Does that include mistakes
[782.96 → 784.26] in if there was like
[784.26 → 785.02] a bug or something
[785.02 → 787.06] in that original JSON version?
[787.26 → 788.40] Does that still have
[788.40 → 789.04] to be supported?
[789.84 → 790.70] That is a very good question.
[791.42 → 791.66] So,
[791.80 → 792.52] I think there's multiple
[792.52 → 793.54] ways to interpret that
[793.54 → 794.62] because I think
[794.62 → 795.50] the most aggressive way
[795.50 → 796.16] to interpret it
[796.16 → 796.66] would be,
[797.32 → 797.50] you know,
[797.72 → 798.28] all the things
[798.28 → 798.90] that are documented
[798.90 → 799.50] to work
[799.50 → 800.62] will remain
[800.62 → 801.48] to work that way.
[801.94 → 803.10] So, if you write
[803.10 → 803.72] some code
[803.72 → 804.52] that just happens
[804.52 → 805.34] to depend on
[805.34 → 806.86] some implementation detail,
[807.38 → 808.30] that is allowed
[808.30 → 809.22] to break at some point
[809.22 → 809.66] in the future.
[810.46 → 811.22] And that is generally
[811.22 → 812.16] how I read it.
[812.50 → 813.38] But the more conservative
[813.38 → 814.24] way to read it
[814.24 → 815.14] and understand it
[815.14 → 815.52] is,
[816.18 → 816.40] no,
[816.72 → 817.02] like,
[817.46 → 818.50] pretty much anything you do,
[818.58 → 819.24] if it's reasonable,
[819.48 → 820.50] even if it's not documented,
[821.04 → 822.18] it should keep working
[822.18 → 822.88] because we don't want
[822.88 → 823.54] to break the users.
[823.92 → 824.44] And in between
[824.44 → 825.50] those two ends,
[825.66 → 827.04] there's some middle ground
[827.04 → 828.12] that the team
[828.12 → 828.88] has to choose.
[829.50 → 829.78] Hmm,
[829.94 → 830.16] well,
[830.30 → 831.12] it's a fine line
[831.12 → 831.62] to walk,
[831.68 → 831.92] isn't it?
[831.94 → 833.08] But it's so important
[833.08 → 834.08] that V1 promise
[834.08 → 835.24] because that's really
[835.24 → 835.94] how we're able
[835.94 → 837.20] to rely on the fact
[837.20 → 839.36] that we can build systems
[839.36 → 839.88] and we know
[839.88 → 840.28] that they're going
[840.28 → 841.14] to keep working
[841.14 → 842.00] with future versions
[842.00 → 842.32] of Go.
[842.42 → 843.12] That turns out
[843.12 → 844.34] to be one of the
[844.34 → 845.12] big selling points
[845.12 → 846.80] for me of Go itself.
[847.02 → 847.12] So,
[847.20 → 847.94] I really do appreciate
[847.94 → 848.92] the effort
[848.92 → 849.36] because I know
[849.36 → 850.12] that isn't an easy
[850.12 → 850.68] thing to do.
[851.30 → 852.32] I would have thought
[852.32 → 854.12] that the JSON package,
[854.24 → 855.68] after it was first written,
[855.84 → 856.94] it's kind of done.
[857.06 → 858.04] It's sort of working.
[858.04 → 859.04] So,
[859.20 → 860.08] what maintenance
[860.08 → 861.16] is there to do on it?
[861.72 → 862.14] That is also
[862.14 → 862.70] a good question.
[863.04 → 863.82] And I think it kind of
[863.82 → 864.60] goes back to
[864.60 → 866.78] how flexible JSON is
[866.78 → 867.76] because JSON
[867.76 → 868.88] doesn't have a schema.
[869.20 → 870.54] It's just data
[870.54 → 871.48] in some structure.
[871.90 → 872.64] You can do
[872.64 → 873.76] lots of things with it
[873.76 → 874.60] and people do
[874.60 → 875.78] do lots of weird
[875.78 → 876.48] things with it.
[876.96 → 877.10] So,
[877.18 → 878.20] then they come
[878.20 → 879.08] to the encoding JSON
[879.08 → 879.70] package in the
[879.70 → 880.94] standard library
[880.94 → 882.16] and they expect
[882.16 → 882.88] all those things
[882.88 → 884.52] to fit their workflow
[884.52 → 885.46] with this library,
[885.46 → 885.72] right?
[886.12 → 886.34] So,
[886.42 → 887.26] they might want
[887.26 → 888.74] to decode
[888.74 → 889.44] some fields
[889.44 → 889.98] depending on
[889.98 → 890.96] what this field is
[890.96 → 892.14] or they might say
[892.14 → 893.00] I want to stream
[893.00 → 893.66] a really,
[893.80 → 894.48] huge object
[894.48 → 895.34] even if it doesn't
[895.34 → 895.90] fit in memory
[895.90 → 897.10] and all those
[897.10 → 897.96] sort of
[897.96 → 898.76] use cases
[898.76 → 899.30] that you might
[899.30 → 900.04] not think
[900.04 → 901.24] to use JSON
[901.24 → 901.84] with initially
[901.84 → 902.70] but people do
[902.70 → 903.42] use JSON with.
[904.00 → 904.12] So,
[904.24 → 904.86] there's a constant
[904.86 → 905.68] stream of feature
[905.68 → 906.22] requests
[906.22 → 907.42] but there's also
[907.42 → 908.20] a constant stream
[908.20 → 909.82] of optimizations
[909.82 → 910.86] and bug fixes
[910.86 → 911.80] caused by previous
[911.80 → 912.20] changes
[912.20 → 913.06] if that makes sense.
[913.66 → 913.86] Yeah,
[913.98 → 914.36] I see.
[914.50 → 914.58] So,
[914.70 → 915.20] just sort of
[915.20 → 916.40] I suppose like
[916.40 → 917.16] any other bit
[917.16 → 917.64] of software
[917.64 → 918.14] it's,
[918.72 → 918.94] you know,
[919.04 → 920.74] you can improve it
[920.74 → 921.54] you can work on it
[921.54 → 922.34] and as you do that
[922.34 → 923.26] you create some
[923.26 → 924.08] other problems
[924.08 → 924.52] you know
[924.52 → 925.56] but it's well tested
[925.56 → 926.00] isn't it?
[926.18 → 926.80] The tests are
[926.80 → 928.34] decent in the
[928.34 → 929.90] encoding JSON package.
[930.16 → 930.24] Yeah,
[930.32 → 930.86] for the most part
[930.86 → 931.26] I would agree.
[931.50 → 931.58] Yeah.
[932.36 → 932.76] Yeah,
[932.96 → 933.96] which is important
[933.96 → 934.54] that's sort of
[934.54 → 935.32] what allows you
[935.32 → 936.98] to act with confidence.
[937.28 → 937.42] You know,
[937.44 → 937.88] you talk about
[937.88 → 938.30] you don't want to
[938.30 → 939.12] break the backwards
[939.12 → 940.90] compatibility promise.
[941.38 → 942.04] Unit tests
[942.04 → 943.32] are really the way
[943.32 → 944.20] to ensure that
[944.20 → 944.64] aren't they?
[945.42 → 946.20] Actually checking
[946.20 → 946.76] that your package
[946.76 → 947.32] is well tested
[947.32 → 948.32] is kind of an art
[948.32 → 949.08] I would say
[949.08 → 950.08] because you can
[950.08 → 950.64] obviously look at
[950.64 → 951.32] the code coverage
[951.32 → 952.14] from the Go tool
[952.14 → 953.82] but that doesn't
[953.82 → 954.72] cover everything
[954.72 → 956.40] because you might
[956.40 → 957.22] be covering a line
[957.22 → 958.00] but you might not
[958.00 → 958.58] be covering all
[958.58 → 959.56] the logic that's
[959.56 → 960.28] encoded within
[960.28 → 961.06] that line of code.
[961.64 → 961.74] Right.
[961.80 → 962.70] Or you might not
[962.70 → 963.22] be hitting one
[963.22 → 963.84] of the edge cases
[963.84 → 964.54] that might panic
[964.54 → 965.40] or something like that.
[965.94 → 966.16] Yeah,
[966.22 → 966.90] see I always tell
[966.90 → 968.02] people not to
[968.02 → 968.72] shoot for like
[968.72 → 970.64] 100% code coverage
[970.64 → 971.96] in their application
[971.96 → 973.24] code just because
[973.24 → 975.08] you kind of
[975.08 → 976.26] can tightly couple
[976.26 → 977.22] really your tests
[977.22 → 978.28] to your implementation.
[978.92 → 980.24] Is this an exception
[980.24 → 980.74] to that?
[981.24 → 982.08] Does it make sense
[982.08 → 982.76] in this package
[982.76 → 984.00] to have 100%
[984.00 → 984.68] code coverage?
[985.10 → 985.96] I would say
[985.96 → 987.04] for the most part
[987.04 → 988.18] it does make sense
[988.18 → 988.80] to try to go
[988.80 → 989.62] as high as possible
[989.62 → 991.08] because for the most part
[991.08 → 991.76] the package
[991.76 → 992.98] is just if-else
[992.98 → 994.44] with logic
[994.44 → 995.80] but there are also
[995.80 → 996.48] some places
[996.48 → 997.44] with like panics
[997.44 → 997.84] of things
[997.84 → 998.38] that should never
[998.38 → 998.72] happen
[998.72 → 1000.04] or also
[1000.04 → 1001.20] things like
[1001.20 → 1002.06] I'm trying to think
[1002.06 → 1002.98] of another edge case
[1002.98 → 1003.74] well there are
[1003.74 → 1004.46] certain edge cases
[1004.46 → 1005.58] that you say
[1005.58 → 1006.76] this really should
[1006.76 → 1007.20] never happen
[1007.20 → 1007.56] and it's going to
[1007.56 → 1007.76] panic
[1007.76 → 1008.70] so you could
[1008.70 → 1009.28] write tests
[1009.28 → 1010.10] that catch those
[1010.10 → 1010.54] and recover
[1010.54 → 1011.38] and I guess
[1011.38 → 1012.10] you could say
[1012.10 → 1012.56] even that you
[1012.56 → 1012.84] should
[1012.84 → 1013.44] but I don't
[1013.44 → 1013.90] think they do
[1013.90 → 1014.30] at the moment.
[1015.38 → 1015.48] Interesting,
[1015.72 → 1015.90] yeah.
[1016.38 → 1016.60] Yeah,
[1016.60 → 1016.86] because there's
[1016.86 → 1017.56] some weirdness
[1017.56 → 1017.98] around
[1017.98 → 1019.30] it's quite unusual
[1019.30 → 1021.46] actually as an API
[1021.46 → 1022.46] because you pass
[1022.46 → 1023.14] in a pointer
[1023.14 → 1023.88] when you want
[1023.88 → 1024.80] to Marshal it
[1024.80 → 1026.46] you pass in a pointer
[1026.46 → 1027.50] to the destination
[1027.50 → 1027.98] essentially
[1027.98 → 1028.80] where you want
[1028.80 → 1029.82] that JSON
[1029.82 → 1031.10] to be unmarshalled into
[1031.10 → 1032.18] and there's some
[1032.18 → 1033.44] kind of interesting
[1033.44 → 1035.30] tricky rules
[1035.30 → 1036.18] around what you
[1036.18 → 1036.86] can pass into
[1036.86 → 1037.44] that thing
[1037.44 → 1038.00] aren't there?
[1038.34 → 1038.50] Yep,
[1038.76 → 1039.66] so you can
[1039.66 → 1041.02] essentially pass
[1041.02 → 1041.42] the pointer
[1041.42 → 1043.22] to any valid data
[1043.22 → 1044.68] so it can't be
[1044.68 → 1045.48] a pointer pointing
[1045.48 → 1046.74] to nil
[1046.74 → 1047.22] to zero
[1047.22 → 1047.90] because then
[1047.90 → 1048.42] you know
[1048.42 → 1049.14] it can't actually
[1049.14 → 1050.32] store any data there
[1050.32 → 1052.12] so essentially
[1052.12 → 1052.96] it just expects
[1052.96 → 1053.44] the pointer
[1053.44 → 1054.88] to a structure
[1054.88 → 1055.28] that it can
[1055.28 → 1056.16] actually store
[1056.16 → 1056.92] decode
[1056.92 → 1058.08] the incoming
[1058.08 → 1058.72] JSON into
[1058.72 → 1059.90] and there are
[1059.90 → 1060.62] various rules
[1060.62 → 1061.04] around there
[1061.04 → 1061.68] for example
[1061.68 → 1063.02] if you pass it
[1063.02 → 1064.14] an empty interface
[1064.14 → 1065.08] it's going to
[1065.08 → 1065.88] sort of make a guess
[1065.88 → 1067.12] as to what it should do
[1067.12 → 1068.08] so if it sees a number
[1068.08 → 1068.82] it's going to assume
[1068.82 → 1069.58] float 64
[1069.58 → 1071.32] and if it sees an object
[1071.32 → 1072.40] it's going to use a map
[1072.40 → 1073.72] but if you give it
[1073.72 → 1074.24] for example
[1074.24 → 1074.68] a struct
[1074.68 → 1075.70] with very specific
[1075.70 → 1076.82] field types
[1076.82 → 1077.48] then it is going to
[1077.48 → 1078.12] follow your lead
[1078.12 → 1079.26] and if any of the types
[1079.26 → 1079.66] don't match
[1079.66 → 1080.46] it's just going to error
[1080.46 → 1081.82] but some intelligence
[1081.82 → 1082.80] that's sort of built
[1082.80 → 1083.38] into the package
[1083.38 → 1083.66] as well
[1083.66 → 1084.34] which I usually
[1084.34 → 1084.96] appreciate
[1084.96 → 1085.80] very recently
[1085.80 → 1086.36] I was sort of
[1086.36 → 1087.48] doing a PR review
[1087.48 → 1089.40] and we had a developer
[1089.40 → 1090.06] who was sort of
[1090.06 → 1090.74] creating a struct
[1090.74 → 1091.12] right
[1091.12 → 1092.20] and providing
[1092.20 → 1093.16] the annotation
[1093.16 → 1094.00] JSON annotation
[1094.00 → 1094.78] next to the fields
[1094.78 → 1095.82] but the data
[1095.82 → 1096.28] wasn't really
[1096.28 → 1096.56] sort of
[1096.56 → 1097.36] there was no inbound
[1097.36 → 1097.82] incoming
[1097.82 → 1099.32] sort of data
[1099.32 → 1099.60] right
[1099.60 → 1101.06] to unmartial into
[1101.06 → 1102.02] so in that case
[1102.02 → 1102.28] I'm like
[1102.28 → 1102.56] well
[1102.56 → 1103.86] unless you really
[1103.86 → 1104.68] anticipate that
[1104.68 → 1105.20] sort of
[1105.20 → 1105.76] the data
[1105.76 → 1106.62] that you're pushing out
[1106.62 → 1107.50] that basically
[1107.50 → 1108.68] the field names
[1108.68 → 1109.18] are going to be
[1109.18 → 1109.78] different from what
[1109.78 → 1110.82] they are named
[1110.82 → 1111.70] in the struct itself
[1111.70 → 1112.46] you don't really
[1112.46 → 1113.20] need to annotate
[1113.20 → 1114.52] your fields
[1114.52 → 1115.28] for your structs
[1115.28 → 1115.48] right
[1115.48 → 1117.12] so the JSON package
[1117.12 → 1117.80] is going to
[1117.80 → 1118.16] sort of
[1118.16 → 1119.20] follow your lead
[1119.20 → 1119.64] as you say
[1119.64 → 1120.06] Daniel
[1120.06 → 1120.44] it's going to
[1120.44 → 1120.94] basically look at
[1120.94 → 1121.48] the name
[1121.48 → 1121.90] you've given
[1121.90 → 1122.60] your fields
[1122.60 → 1123.14] and actually
[1123.14 → 1124.24] use those names
[1124.24 → 1125.20] in the JSON output
[1125.20 → 1125.46] right
[1125.46 → 1126.44] so you don't have
[1126.44 → 1127.06] to add that
[1127.06 → 1127.76] annotation there
[1127.76 → 1128.92] so there's a lot
[1128.92 → 1129.60] of smarts like that
[1129.60 → 1130.28] that I can certainly
[1130.28 → 1130.76] appreciate
[1130.76 → 1131.76] that's built
[1131.76 → 1133.70] into the package
[1133.70 → 1134.52] and this is something
[1134.52 → 1134.92] that we're going to
[1134.92 → 1135.52] get more
[1135.52 → 1136.86] into as well
[1136.86 → 1138.52] I like the standard
[1138.52 → 1138.88] library
[1138.88 → 1139.40] I like using
[1139.40 → 1140.10] the standard library
[1140.10 → 1141.12] because maybe
[1141.12 → 1141.42] it's the nature
[1141.42 → 1141.86] of my work
[1141.86 → 1142.78] but I tend to
[1142.78 → 1143.70] not sort of
[1143.70 → 1144.82] look for
[1144.82 → 1145.70] third party packages
[1145.70 → 1146.50] right
[1146.50 → 1148.04] to do certain things
[1148.04 → 1148.64] if I can
[1148.64 → 1149.48] find something
[1149.48 → 1150.12] in the standard library
[1150.12 → 1151.18] even if it's a little
[1151.18 → 1152.62] harder to deal with
[1152.62 → 1153.32] or a little less
[1153.32 → 1153.94] performant
[1153.94 → 1154.58] or whatever the case
[1154.58 → 1155.10] may be
[1155.10 → 1156.32] we're seeing
[1156.32 → 1156.88] sort of
[1156.88 → 1158.68] if you've been
[1158.68 → 1159.22] in that community
[1159.22 → 1160.44] for any length of time
[1160.44 → 1160.96] you've probably
[1160.96 → 1161.60] come across
[1161.60 → 1163.10] other third party
[1163.10 → 1164.04] packages
[1164.04 → 1164.80] can be built
[1164.80 → 1165.84] third party packages
[1165.84 → 1166.80] that have made
[1166.80 → 1167.66] their own trade-offs
[1167.66 → 1168.14] right
[1168.14 → 1169.50] in regard to
[1169.50 → 1170.06] implementation
[1170.06 → 1171.54] for JSON parsing
[1171.54 → 1172.24] and marshalling
[1172.24 → 1172.72] and marshalling
[1172.72 → 1173.20] and all that stuff
[1173.20 → 1174.04] and a lot of them
[1174.04 → 1174.60] seem to be focused
[1174.60 → 1176.12] around speed
[1176.12 → 1176.70] and performance
[1176.70 → 1177.12] right
[1177.12 → 1178.40] again Dave Cheney's
[1178.40 → 1179.04] own sort of
[1179.04 → 1179.92] experimentation
[1179.92 → 1181.14] which is published
[1181.14 → 1182.06] and hopefully
[1182.06 → 1182.48] you know
[1182.48 → 1183.52] we wish he was here
[1183.52 → 1184.08] to discuss it
[1184.08 → 1184.80] but there's that
[1184.80 → 1185.16] sort of
[1185.16 → 1186.18] I'm curious
[1186.18 → 1186.84] to understand
[1186.84 → 1187.62] sort of
[1187.62 → 1189.56] when is a good reason
[1189.56 → 1191.56] to deviate
[1191.56 → 1192.04] from
[1192.04 → 1192.70] say the standard
[1192.70 → 1193.60] library's approach
[1193.60 → 1194.06] right
[1194.06 → 1194.86] to
[1194.86 → 1196.12] everybody wants
[1196.12 → 1196.54] fast
[1196.54 → 1196.78] right
[1196.78 → 1197.38] it's fast
[1197.38 → 1198.12] oh it's faster
[1198.12 → 1199.14] I should use that
[1199.14 → 1199.36] right
[1199.36 → 1200.44] well
[1200.44 → 1201.48] there are trade-offs
[1201.48 → 1201.82] there too
[1201.82 → 1202.04] right
[1202.04 → 1202.36] you don't
[1202.36 → 1202.90] you don't pick it
[1202.90 → 1203.48] just because it's
[1203.48 → 1203.76] faster
[1203.76 → 1203.98] right
[1203.98 → 1204.66] but I'm curious
[1204.66 → 1205.16] to sort of
[1205.16 → 1205.86] your take
[1205.86 → 1206.14] right
[1206.14 → 1207.10] as to
[1207.10 → 1207.86] why
[1207.86 → 1208.44] pick one over
[1208.44 → 1208.80] the other
[1208.80 → 1209.18] what sort of
[1209.18 → 1209.54] trade-offs
[1209.54 → 1210.02] you're making
[1210.02 → 1211.06] along those lines
[1211.06 → 1212.12] I think that topic
[1212.12 → 1212.64] is at the heart
[1212.64 → 1213.82] of this whole discussion
[1213.82 → 1214.48] because
[1214.48 → 1215.64] it is true
[1215.64 → 1216.12] that a lot of people
[1216.12 → 1216.94] want the fastest
[1216.94 → 1217.78] JSON decoder
[1217.78 → 1218.14] out there
[1218.14 → 1219.06] and some of them
[1219.06 → 1219.66] might not realize
[1219.66 → 1220.08] the trade-offs
[1220.08 → 1220.40] at play
[1220.40 → 1221.96] and I have
[1221.96 → 1222.68] mixed opinions
[1222.68 → 1223.68] and feelings
[1223.68 → 1224.82] about all the
[1224.82 → 1225.54] third-party
[1225.54 → 1225.92] JSON
[1225.92 → 1226.70] re-implementations
[1226.70 → 1227.08] out there
[1227.08 → 1228.52] I think some of them
[1228.52 → 1229.10] do make sense
[1229.10 → 1229.78] for example
[1229.78 → 1230.54] one use case
[1230.54 → 1231.04] is
[1231.04 → 1232.58] you do absolutely
[1232.58 → 1233.78] want the most
[1233.78 → 1234.68] performance you can get
[1234.68 → 1236.10] because maybe this is
[1236.10 → 1237.46] a bottleneck for you
[1237.46 → 1238.68] and you don't mind
[1238.68 → 1240.10] go generating
[1240.10 → 1240.74] some code
[1240.74 → 1241.64] to then
[1241.64 → 1242.44] you know
[1242.44 → 1243.06] write
[1243.06 → 1244.32] generate
[1244.32 → 1244.90] automatically
[1244.90 → 1245.62] a decoder
[1245.62 → 1245.98] for you
[1245.98 → 1246.40] for JSON
[1246.40 → 1247.42] so you can use
[1247.42 → 1247.96] packages like
[1247.96 → 1248.78] easy JSON for that
[1248.78 → 1249.58] which is pretty popular
[1249.58 → 1250.96] and the trade-off there
[1250.96 → 1251.90] is you have to run
[1251.90 → 1252.52] code generate
[1252.52 → 1253.24] and your binary
[1253.24 → 1253.72] is going to weigh
[1253.72 → 1254.54] quite a little bit more
[1254.54 → 1254.98] because it has
[1254.98 → 1255.98] quite a lot of extra code
[1255.98 → 1257.40] but that extra code
[1257.40 → 1258.50] it just encodes
[1258.50 → 1259.64] all the logic directly
[1259.64 → 1260.78] in binary code
[1260.78 → 1261.58] in machine code
[1261.58 → 1262.76] so there's no reflect
[1262.76 → 1263.66] there's no
[1263.66 → 1264.58] dereferences
[1264.58 → 1265.82] there's no extra work
[1265.82 → 1266.64] involved
[1266.64 → 1268.30] so I think that's
[1268.30 → 1269.18] clearly one of the cases
[1269.18 → 1270.42] where it might make sense
[1270.42 → 1271.06] for your use case
[1271.06 → 1272.52] I like how you framed that
[1272.52 → 1272.78] as well
[1272.78 → 1273.26] you're saying
[1273.26 → 1274.60] maybe it's a bottleneck
[1274.60 → 1275.34] in your case
[1275.34 → 1276.28] and that's the thing
[1276.28 → 1276.72] it's like
[1276.72 → 1277.84] once you've seen
[1277.84 → 1278.98] that this is a place
[1278.98 → 1279.88] where an improvement
[1279.88 → 1280.76] is going to make
[1280.76 → 1281.58] a difference for you
[1281.58 → 1282.88] then it's worth
[1282.88 → 1284.38] taking on the extra pain
[1284.38 → 1285.56] whether it's complexity
[1285.56 → 1286.92] or learning a new API
[1286.92 → 1287.82] or whatever it is
[1287.82 → 1289.34] I like that approach
[1289.34 → 1289.82] because
[1289.82 → 1291.04] well I think it's what
[1291.04 → 1292.64] we should always be doing
[1292.64 → 1292.92] you know
[1292.92 → 1294.12] as you alluded to
[1294.12 → 1294.36] Johnny
[1294.36 → 1295.12] we kind of
[1295.12 → 1296.48] can get a bit obsessed
[1296.48 → 1297.46] with why wouldn't
[1297.46 → 1298.26] we want the fastest
[1298.26 → 1299.22] possible thing
[1299.22 → 1300.00] and the answer is
[1300.00 → 1301.36] it might be good enough
[1301.36 → 1303.14] just using the standard library
[1303.14 → 1305.14] what are some of the packages
[1305.14 → 1306.20] and how are they different?
[1306.20 → 1307.76] so another package
[1307.76 → 1308.36] that I saw
[1308.36 → 1309.26] fairly recently
[1309.26 → 1309.96] which is interesting
[1309.96 → 1311.08] I forget what it's called
[1311.08 → 1312.38] it was named after a company
[1312.38 → 1313.44] but essentially
[1313.44 → 1314.30] what they did was
[1314.30 → 1315.16] they tried to keep
[1315.16 → 1316.26] the same API
[1316.26 → 1317.80] as the standard library
[1317.80 → 1318.92] so they said
[1318.92 → 1319.86] there's a drop-in replacement
[1319.86 → 1321.72] but under the hood
[1321.72 → 1322.50] they did something
[1322.50 → 1323.66] which was interesting
[1323.66 → 1324.30] which is
[1324.30 → 1325.30] instead of using
[1325.30 → 1326.16] the reflection package
[1326.16 → 1327.00] and reflect
[1327.00 → 1328.28] is one of the major contributors
[1328.28 → 1329.12] to why
[1329.12 → 1330.26] encoding JSON is slow
[1330.26 → 1331.92] they used unsafe
[1331.92 → 1332.36] directly
[1332.36 → 1334.22] and the trade-off there
[1334.22 → 1334.60] is
[1334.60 → 1335.40] if you use unsafe
[1335.40 → 1337.04] you can do a lot of magic
[1337.04 → 1338.50] and it's very fast
[1338.50 → 1339.88] but it's also unsafe
[1339.88 → 1341.86] so I kind of
[1341.86 → 1342.72] have mixed feelings
[1342.72 → 1343.50] about telling people
[1343.50 → 1344.52] that it's a drop-in replacement
[1344.52 → 1345.72] because that sort of
[1345.72 → 1346.18] just tells them
[1346.18 → 1347.38] oh I just changed the import
[1347.38 → 1348.66] and suddenly it's twice as fast
[1348.66 → 1350.42] but they're not realizing
[1350.42 → 1352.04] what a big security hole
[1352.04 → 1353.10] they've just opened
[1353.10 → 1355.04] because it is true
[1355.04 → 1356.16] that reflect itself
[1356.16 → 1358.22] does use unsafe underneath
[1358.22 → 1360.62] but reflect is very well
[1360.62 → 1362.22] scrutinized and reviewed
[1362.22 → 1364.12] and it follows the go rules
[1364.12 → 1366.32] for what fields you can set
[1366.32 → 1366.84] and so on
[1366.84 → 1368.30] and if you use unsafe directly
[1368.30 → 1369.58] you just skip all of that
[1369.58 → 1370.38] and you're on your own
[1370.38 → 1372.08] and the standard library
[1372.08 → 1372.94] uses reflect
[1372.94 → 1374.76] because in a sense
[1374.76 → 1375.80] there's some kind of
[1375.80 → 1376.94] it's dynamic isn't it
[1376.94 → 1377.28] in a way
[1377.28 → 1378.16] it's dynamic data
[1378.16 → 1379.80] you don't necessarily know
[1379.80 → 1381.72] especially if you're
[1381.72 → 1383.28] unearthing into a map
[1383.28 → 1383.98] string interface
[1383.98 → 1385.30] you don't know
[1385.30 → 1386.56] necessarily the structure
[1386.56 → 1387.90] of that JSON
[1387.90 → 1389.04] and that by the way
[1389.04 → 1389.62] is
[1389.62 → 1390.60] can be
[1390.60 → 1391.34] an extremely
[1391.34 → 1393.06] powerful thing
[1393.06 → 1393.84] but can also be
[1393.84 → 1395.12] quite easy to abuse
[1395.12 → 1396.06] yeah
[1396.06 → 1397.20] that is an interesting point
[1397.20 → 1397.68] you make about
[1397.68 → 1398.84] using unsafe
[1398.84 → 1399.72] in that way
[1399.72 → 1400.82] I can see why
[1400.82 → 1401.54] they did that
[1401.54 → 1402.40] but yeah
[1402.40 → 1402.92] that's funny
[1402.92 → 1404.12] one use case
[1404.12 → 1404.80] that I've used
[1404.80 → 1405.76] JSON for before
[1405.76 → 1406.72] in quite a
[1406.72 → 1407.46] strange
[1407.46 → 1408.46] or maybe not
[1408.46 → 1409.02] way
[1409.02 → 1409.90] was just a
[1409.90 → 1411.24] command line tools
[1411.24 → 1412.04] which
[1412.04 → 1413.12] returned
[1413.12 → 1414.00] they took in
[1414.00 → 1415.04] through standard input
[1415.04 → 1416.36] lines of JSON
[1416.36 → 1417.66] and then their output
[1417.66 → 1419.12] were lines of JSON
[1419.12 → 1421.16] and just that
[1421.16 → 1422.16] we had a series
[1422.16 → 1423.24] of different tools
[1423.24 → 1423.92] that we could chain
[1423.92 → 1425.08] together in different ways
[1425.08 → 1425.84] just kind of
[1425.84 → 1427.08] passing around
[1427.08 → 1427.86] you know
[1427.86 → 1428.82] different objects
[1428.82 → 1430.26] just different JSON objects
[1430.26 → 1431.56] each one on its own line
[1431.56 → 1432.90] and the JSON
[1432.90 → 1434.70] when you create
[1434.70 → 1435.86] the marshaller
[1435.86 → 1437.38] you create the decoder
[1437.38 → 1438.46] or the encoder
[1438.46 → 1439.88] those types
[1439.88 → 1440.98] take a reader
[1440.98 → 1441.76] an IO reader
[1441.76 → 1442.56] don't they
[1442.56 → 1443.42] so that they can
[1443.42 → 1445.36] Marshal an object
[1445.36 → 1446.46] they break it
[1446.46 → 1447.62] at the line feed
[1447.62 → 1449.66] and then you can reuse it
[1449.66 → 1451.14] and keep marshalling objects
[1451.14 → 1451.72] in that way
[1451.72 → 1452.54] so that
[1452.54 → 1453.38] as a design
[1453.38 → 1453.98] was perfect
[1453.98 → 1454.92] for this situation
[1454.92 → 1455.36] because
[1455.36 → 1456.60] these tools
[1456.60 → 1457.76] basically didn't do anything
[1457.76 → 1459.20] until a line of JSON
[1459.20 → 1460.48] came in through standard in
[1460.48 → 1461.72] they'd then process it
[1461.72 → 1462.82] and then you get the line
[1462.82 → 1463.50] printed out
[1463.50 → 1464.54] but there's also the
[1464.54 → 1466.58] directly using the marshal
[1466.58 → 1467.54] and Marshal
[1467.54 → 1468.82] functions too
[1468.82 → 1469.96] what's the key difference
[1469.96 → 1470.82] between those?
[1471.46 → 1472.62] So I think most people
[1472.62 → 1473.90] would say that the difference
[1473.90 → 1474.74] is the streaming
[1474.74 → 1475.96] so if you use marshal
[1475.96 → 1476.84] or Marshal
[1476.84 → 1478.02] you can look at the
[1478.02 → 1478.88] function types
[1478.88 → 1479.54] and you can see that
[1479.54 → 1480.82] they take and give
[1480.82 → 1482.04] a slice of byte
[1482.04 → 1483.44] so it's pretty easy
[1483.44 → 1484.10] to tell that
[1484.10 → 1484.88] you know if you're
[1484.88 → 1486.04] marshalling a chunk of JSON
[1486.04 → 1486.88] you have to have
[1486.88 → 1487.58] that chunk of JSON
[1487.58 → 1488.00] in memory
[1488.00 → 1489.66] and if you look at
[1489.66 → 1490.40] the decoder
[1490.40 → 1491.22] it takes a reader
[1491.22 → 1492.54] you might then
[1492.54 → 1493.64] suspect that
[1493.64 → 1494.44] oh this is going to
[1494.44 → 1495.74] stream the JSON in
[1495.74 → 1496.64] so I don't have to
[1496.64 → 1497.40] load it all into memory
[1497.40 → 1498.38] but that's actually
[1498.38 → 1499.00] not the case
[1499.00 → 1500.14] and I think it's
[1500.14 → 1501.40] one of my main gripes
[1501.40 → 1502.16] with the current API
[1502.16 → 1503.42] I'm not going to say
[1503.42 → 1503.90] it's wrong
[1503.90 → 1504.98] but it's misleading
[1504.98 → 1505.98] to a certain degree
[1505.98 → 1507.46] because what it will do
[1507.46 → 1509.06] is it will buffer
[1509.06 → 1511.06] an entire JSON value
[1511.06 → 1511.82] such as an object
[1511.82 → 1513.36] and then once it's
[1513.36 → 1514.14] buffered the whole thing
[1514.14 → 1515.42] then it's going to decode it
[1515.42 → 1517.02] and there's a good reason
[1517.02 → 1517.42] for that
[1517.42 → 1518.48] and the reason is
[1518.48 → 1519.76] because the
[1519.76 → 1521.34] encoding JSON package
[1521.34 → 1523.24] essentially prefers
[1523.24 → 1524.24] correctness over
[1524.24 → 1525.02] everything else
[1525.02 → 1526.32] and it has some
[1526.32 → 1527.18] semantics for
[1527.18 → 1528.30] when you decode
[1528.30 → 1528.90] into a value
[1528.90 → 1529.94] it's going to merge
[1529.94 → 1531.36] the decoded data
[1531.36 → 1532.26] into that value
[1532.26 → 1533.14] so for example
[1533.14 → 1533.80] if you decode
[1533.80 → 1534.34] into a map
[1534.34 → 1535.42] and that map
[1535.42 → 1536.18] had the key foo
[1536.18 → 1537.52] and then you decode
[1537.52 → 1538.38] a new key bar
[1538.38 → 1539.18] you end up with
[1539.18 → 1540.22] both keys foo and bar
[1540.22 → 1541.50] it doesn't just replace
[1541.50 → 1542.36] the previous map
[1542.36 → 1542.92] with a new map
[1542.92 → 1544.08] and that is useful
[1544.08 → 1544.84] for some things
[1544.84 → 1546.52] but most people
[1546.52 → 1547.40] they just decode
[1547.40 → 1549.28] into an empty value
[1549.28 → 1550.40] they don't care about
[1550.40 → 1551.20] what was there before
[1551.20 → 1552.78] so for most people
[1552.78 → 1553.48] this is surprising
[1553.48 → 1554.52] because they don't care
[1554.52 → 1555.12] about this property
[1555.12 → 1556.14] and the way
[1556.14 → 1557.32] the encoding JSON package
[1557.32 → 1558.60] implements this property
[1558.60 → 1560.24] is tokenizing
[1560.24 → 1561.88] all the input
[1561.88 → 1563.06] so if there's any
[1563.06 → 1564.46] syntax mistake
[1564.46 → 1565.36] in the input
[1565.36 → 1566.46] or if it's invalid JSON
[1566.46 → 1567.58] then it's not going
[1567.58 → 1568.34] to decode anything
[1568.34 → 1569.54] because it's going
[1569.54 → 1570.36] to do a second pass
[1570.36 → 1571.34] and in that second pass
[1571.34 → 1572.42] it is actually going
[1572.42 → 1573.52] to write to the destination
[1573.52 → 1575.86] yeah that makes sense
[1575.86 → 1577.14] I saw another
[1577.14 → 1578.74] JSON implementation
[1578.74 → 1580.34] which essentially
[1580.34 → 1581.66] it didn't Marshal
[1581.66 → 1582.60] it didn't try and
[1582.60 → 1583.80] turn the JSON
[1583.80 → 1585.34] into structured data
[1585.34 → 1586.64] but you could use it
[1586.64 → 1588.14] to just find specific
[1588.14 → 1588.90] key paths
[1588.90 → 1590.44] so you might say
[1590.44 → 1591.84] here's the JSON stream
[1591.84 → 1593.04] or the JSON string
[1593.04 → 1594.62] and I'm looking for
[1594.62 → 1595.56] like you know
[1595.56 → 1597.78] author dot first name
[1597.78 → 1598.72] and so
[1598.72 → 1599.90] just by sort of
[1599.90 → 1600.62] reading it
[1600.62 → 1601.58] skimming it really
[1601.58 → 1602.82] not trying to understand
[1602.82 → 1604.18] and extract all the fields
[1604.18 → 1605.28] and figure out data types
[1605.28 → 1605.80] and all that
[1605.80 → 1607.40] but just looking
[1607.40 → 1608.52] for that particular
[1608.52 → 1609.16] key path
[1609.16 → 1610.56] and that's a kind of
[1610.56 → 1611.70] that's another approach
[1611.70 → 1613.38] if in a particular case
[1613.38 → 1614.32] all you care about
[1614.32 → 1615.42] is a single field
[1615.42 → 1616.90] that's a very fast way
[1616.90 → 1619.02] to get that field
[1619.02 → 1619.62] I'm having
[1619.62 → 1621.34] XPath flashbacks
[1621.34 → 1622.86] yeah kind of
[1622.86 → 1624.40] yeah
[1624.40 → 1625.32] and yeah
[1625.32 → 1625.90] that's actually
[1625.90 → 1626.42] a very good point
[1626.42 → 1627.18] I forgot about
[1627.18 → 1628.34] that extra use case
[1628.34 → 1628.98] and I think
[1628.98 → 1629.94] I think that library
[1629.94 → 1630.48] is called
[1630.48 → 1631.88] at least the most famous one
[1631.88 → 1632.96] JSON iterator
[1632.96 → 1633.90] or something like that
[1633.90 → 1634.58] or JSON inter
[1634.58 → 1635.00] right
[1635.00 → 1636.54] and I think it's useful
[1636.54 → 1637.46] for two use cases
[1637.46 → 1637.92] one of them
[1637.92 → 1638.42] you mentioned
[1638.42 → 1639.90] it's getting just one field
[1639.90 → 1640.68] or one value
[1640.68 → 1642.24] and if the JSON is very big
[1642.24 → 1643.56] you can save a lot of work
[1643.56 → 1644.74] by just skipping to that
[1644.74 → 1645.22] a little bit
[1645.22 → 1646.98] and I think the other one is
[1646.98 → 1647.72] what if you don't know
[1647.72 → 1648.68] what the data looks like
[1648.68 → 1650.24] because JSON
[1650.24 → 1651.56] at least the encoding
[1651.56 → 1652.26], JSON package
[1652.26 → 1653.56] forces you to know
[1653.56 → 1654.00] up front
[1654.00 → 1655.44] what all the data
[1655.44 → 1656.18] is going to look like
[1656.18 → 1657.38] and you can use
[1657.38 → 1658.04] something called
[1658.04 → 1659.34] Jason.raw message
[1659.34 → 1660.48] to sort of delay
[1660.48 → 1662.02] parsing chunks
[1662.02 → 1662.64] of the JSON
[1662.64 → 1663.88] decoding chunks
[1663.88 → 1664.34] of the JSON
[1664.34 → 1666.08] but that's kind of like
[1666.08 → 1666.84] just forcing you
[1666.84 → 1668.14] to do multiple decodes
[1668.14 → 1668.66] to do it
[1668.66 → 1669.58] in multiple stages
[1669.58 → 1671.16] if you want to quickly
[1671.16 → 1672.24] look at this
[1672.24 → 1673.18] and then if it's X
[1673.18 → 1673.98] then do that
[1673.98 → 1675.38] otherwise do something else
[1675.38 → 1676.66] if you want to encode
[1676.66 → 1677.86] that logic into your code
[1677.86 → 1679.28] using something like
[1679.28 → 1680.46] that package
[1680.46 → 1681.42] might be a little bit easier
[1681.42 → 1681.86] for you
[1681.86 → 1682.92] but I would say
[1682.92 → 1683.70] that for most people
[1683.70 → 1684.22] they do know
[1684.22 → 1684.78] what their JSON
[1684.78 → 1685.58] is going to look like
[1685.58 → 1686.38] yeah
[1686.38 → 1687.54] in my experience
[1687.54 → 1688.46] it's better
[1688.46 → 1689.34] if you do know
[1689.34 → 1689.90] what the JSON
[1689.90 → 1690.60] is going to look like
[1690.60 → 1691.52] don't be tempted
[1691.52 → 1692.44] by this idea
[1692.44 → 1693.18] that your app
[1693.18 → 1693.96] can just support
[1693.96 → 1695.16] any data structure
[1695.16 → 1695.92] because
[1695.92 → 1698.54] that will come back
[1698.54 → 1699.08] to bite you
[1699.08 → 1700.10] is my experience
[1700.10 → 1701.52] what does that raw message
[1701.52 → 1702.50] actually do then
[1702.50 → 1703.08] is it just like
[1703.08 → 1703.88] a string type
[1703.88 → 1705.38] or a slice of bytes
[1705.38 → 1706.16] or something
[1706.16 → 1706.72] what is it?
[1707.28 → 1707.84] it is exactly
[1707.84 → 1709.34] a named slice of byte
[1709.34 → 1710.42] and it implements
[1710.42 → 1711.46] on Marshall JSON
[1711.46 → 1712.32] and all it does
[1712.32 → 1713.28] is it just takes the JSON
[1713.28 → 1713.90] and stores it
[1713.90 → 1714.92] that's it
[1714.92 → 1716.14] it's really powerful
[1716.14 → 1718.20] because it essentially
[1718.20 → 1718.60] lets you do
[1718.60 → 1719.12] whatever you want
[1719.12 → 1721.48] and I was going to
[1721.48 → 1722.22] say before we go on
[1722.22 → 1723.62] I'm close to getting full
[1723.62 → 1724.16] so I'm going to
[1724.16 → 1724.74] stop the recording
[1724.74 → 1725.26] save it
[1725.26 → 1725.92] and then start over
[1725.92 → 1726.82] so give me two minutes
[1726.82 → 1727.52] sounds good
[1727.52 → 1728.18] let's do it
[1728.18 → 1729.06] take a break
[1729.06 → 1729.68] yeah
[1729.68 → 1730.38] stop the world
[1730.38 → 1742.84] what up gophers
[1742.84 → 1744.16] Jared Santo here
[1744.16 → 1745.16] your humble producer
[1745.16 → 1746.54] I'd like to tell you
[1746.54 → 1747.56] about something new
[1747.56 → 1748.72] we are beta testing
[1748.72 → 1749.66] around Go Time
[1749.66 → 1751.36] it's a membership program
[1751.36 → 1752.04] which we think
[1752.04 → 1753.14] could be really valuable
[1753.14 → 1754.00] for the whole community
[1754.00 → 1755.54] we call it
[1755.54 → 1756.32] Changelog++
[1756.32 → 1757.84] and it's the best way
[1757.84 → 1758.86] to directly support
[1758.86 → 1759.40] Go Time
[1759.40 → 1760.92] and all the podcasts
[1760.92 → 1761.40] videos
[1761.40 → 1762.34] and other stuff
[1762.34 → 1762.84] we create
[1762.84 → 1763.58] here at Changelog
[1763.58 → 1765.02] we have big plans
[1765.02 → 1766.18] and ambitions for this
[1766.18 → 1767.26] but we are experimenting
[1767.26 → 1767.84] for now
[1767.84 → 1768.46] to make sure
[1768.46 → 1769.16] there's interest
[1769.16 → 1770.80] so when you sign up today
[1770.80 → 1772.46] you make the ads disappear
[1772.46 → 1773.62] you get Go Time
[1773.62 → 1774.88] and all the shows you love
[1774.88 → 1775.76] just no ads
[1775.76 → 1776.94] I guess that means
[1776.94 → 1777.76] this part you're listening
[1777.76 → 1778.44] to right now
[1778.44 → 1779.44] it'll be gone
[1779.44 → 1781.20] we also have some
[1781.20 → 1782.48] extended episodes planned
[1782.48 → 1783.50] bonus content
[1783.50 → 1784.56] merch store discounts
[1784.56 → 1785.56] and a lot of ideas
[1785.56 → 1786.58] but since it's such
[1786.58 → 1787.20] early days
[1787.20 → 1787.90] we are offering
[1787.90 → 1788.44] memberships
[1788.44 → 1789.62] at a 40% discount
[1789.62 → 1790.84] for early adopters
[1790.84 → 1792.40] that deal's going on
[1792.40 → 1793.36] for the month of August
[1793.36 → 1793.94] so head to
[1793.94 → 1794.84] changelog.com
[1794.84 → 1795.84] slash plus
[1795.84 → 1796.72] to join today
[1796.72 → 1798.22] lock in that discount
[1798.22 → 1799.48] get closer to the metal
[1799.48 → 1801.04] and make the ad disappear
[1801.04 → 1802.14] once again
[1802.14 → 1803.48] that's changelog.com
[1803.48 → 1804.64] slash plus
[1804.64 → 1805.62] we'd love to have you
[1805.62 → 1806.22] supporting us
[1806.22 → 1807.06] as a member
[1807.06 → 1821.86] so that's an interesting
[1821.86 → 1822.48] bug that I have
[1822.48 → 1823.20] with this program
[1823.20 → 1824.26] so it seems to just
[1824.26 → 1825.38] keep using more
[1825.38 → 1825.88] and more memory
[1825.88 → 1826.88] as long as I record
[1826.88 → 1827.84] and then I have to
[1827.84 → 1828.60] close it completely
[1828.60 → 1830.24] after saving the file
[1830.24 → 1831.16] and then just start
[1831.16 → 1831.72] a new
[1831.72 → 1832.60] yeah
[1832.60 → 1834.22] it is just as though
[1834.22 → 1835.46] it's putting that audio
[1835.46 → 1836.54] into the RAM
[1836.54 → 1837.38] isn't it
[1837.38 → 1837.90] I guess so
[1837.90 → 1838.56] but I don't have time
[1838.56 → 1839.38] to fix that right now
[1839.38 → 1839.88] obviously
[1839.88 → 1841.34] is the amount of RAM
[1841.34 → 1842.46] it uses the same
[1842.46 → 1843.52] as the file
[1843.52 → 1844.52] when you save it
[1844.52 → 1845.20] same size
[1845.20 → 1846.68] I stored the WAV
[1846.68 → 1848.54] it was like 160 legs
[1848.54 → 1850.76] but it used all of my
[1850.76 → 1852.54] 15 gigabytes of RAM
[1852.54 → 1853.36] so I don't know
[1853.36 → 1853.84] what it's doing
[1853.84 → 1854.52] yeah
[1854.52 → 1855.64] well, so I'm ready again
[1855.64 → 1856.00] apologies
[1856.00 → 1856.86] yeah so
[1856.86 → 1857.66] one question
[1857.66 → 1858.34] that we're picking up
[1858.34 → 1858.78] from the channel
[1858.78 → 1859.70] this one coming
[1859.70 → 1860.36] from my very own
[1860.36 → 1860.96] John Calhoun
[1860.96 → 1861.88] you mentioned
[1861.88 → 1863.18] the Go 1.0
[1863.18 → 1864.24] compatibility promise
[1864.24 → 1865.42] which I think
[1865.42 → 1866.02] we all
[1866.02 → 1866.86] Go developers
[1866.86 → 1867.40] who have anything
[1867.40 → 1867.86] in production
[1867.86 → 1869.24] really value
[1869.24 → 1870.80] vis-à-vis
[1870.80 → 1872.34] the JSON
[1872.34 → 1873.72] package
[1873.72 → 1874.60] of the centre library
[1874.60 → 1875.40] are there things
[1875.40 → 1876.18] that you wish
[1876.18 → 1876.98] you could put in there
[1876.98 → 1877.40] right now
[1877.40 → 1878.20] but that you're
[1878.20 → 1878.58] sort of
[1878.58 → 1879.98] prevented from doing
[1879.98 → 1880.40] that
[1880.40 → 1881.24] because of that
[1881.24 → 1882.16] compatibility promise
[1882.16 → 1883.12] and perhaps
[1883.12 → 1883.88] maybe could find
[1883.88 → 1884.16] their way
[1884.16 → 1885.08] into a subsequent
[1885.08 → 1885.80] version of Go
[1885.80 → 1886.42] that is allowed
[1886.42 → 1886.88] to break
[1886.88 → 1887.90] that backwards
[1887.90 → 1888.32] compatibility
[1888.32 → 1889.64] yeah
[1889.64 → 1890.08] that is
[1890.08 → 1890.52] that is a good
[1890.52 → 1890.84] question
[1890.84 → 1891.96] I think there's
[1891.96 → 1892.74] two kinds of things
[1892.74 → 1893.40] that I would fix
[1893.40 → 1894.34] one of them
[1894.34 → 1894.96] are sort of
[1894.96 → 1895.80] high-level API
[1895.80 → 1896.28] changes
[1896.28 → 1897.38] so what we talked
[1897.38 → 1897.88] about earlier
[1897.88 → 1898.90] about the readers
[1898.90 → 1899.50] and writers
[1899.50 → 1900.78] making it seem
[1900.78 → 1901.44] like it's streaming
[1901.44 → 1902.02] but it's not
[1902.02 → 1902.66] actually streaming
[1902.66 → 1903.24] it's buffering
[1903.24 → 1904.82] but changing
[1904.82 → 1905.50] those would break
[1905.50 → 1906.40] practically every
[1906.40 → 1907.10] program using
[1907.10 → 1907.38] JSON
[1907.38 → 1908.52] so it's not
[1908.52 → 1909.02] something that I
[1909.02 → 1909.66] would ever change
[1909.66 → 1910.12] in v1
[1910.12 → 1910.62] it's just
[1910.62 → 1911.00] you know
[1911.00 → 1911.36] out of the
[1911.36 → 1911.66] question
[1911.66 → 1913.00] the other
[1913.00 → 1913.56] kind
[1913.56 → 1914.78] is subtle
[1914.78 → 1915.34] bugs
[1915.34 → 1915.98] and historical
[1915.98 → 1916.58] problems
[1916.58 → 1917.60] that have
[1917.60 → 1918.52] kind of
[1918.52 → 1919.02] become
[1919.02 → 1919.72] the de facto
[1919.72 → 1920.70] behaviour
[1920.70 → 1921.48] that everybody
[1921.48 → 1922.28] has ended up
[1922.28 → 1923.12] some people
[1923.12 → 1923.74] have ended up
[1923.74 → 1924.70] depending upon
[1924.70 → 1926.08] and one example
[1926.08 → 1926.58] was
[1926.58 → 1927.72] there's a type
[1927.72 → 1928.04] called
[1928.04 → 1928.84] JSON.number
[1928.84 → 1930.84] and JSON.number
[1930.84 → 1932.10] it essentially
[1932.10 → 1932.84] lets you easily
[1932.84 → 1933.82] support big numbers
[1933.82 → 1934.50] and it's just
[1934.50 → 1935.36] a string type
[1935.36 → 1936.46] so when you use
[1936.46 → 1937.02] it to decode
[1937.02 → 1937.38] a number
[1937.38 → 1938.40] such as
[1938.40 → 1938.68] you know
[1938.68 → 1939.82] like a 50-digit
[1939.82 → 1940.10] number
[1940.10 → 1940.90] it doesn't
[1940.90 → 1941.30] matter if
[1941.30 → 1941.76] that wouldn't
[1941.76 → 1942.54] fit in an
[1942.54 → 1943.62] int32 or
[1943.62 → 1944.24] int64
[1944.24 → 1945.22] because it's
[1945.22 → 1945.64] going to keep
[1945.64 → 1946.10] the string
[1946.10 → 1947.30] exactly as is
[1947.30 → 1948.64] so that would
[1948.64 → 1949.10] be like the
[1949.10 → 1949.94] the simplest way to
[1949.94 → 1950.74] implement big
[1950.74 → 1951.28] numbers right
[1951.28 → 1953.62] and the way
[1953.62 → 1954.76] JSON.number
[1954.76 → 1955.40] is implemented
[1955.40 → 1957.24] if the input
[1957.24 → 1958.30] JSON is actually
[1958.30 → 1958.76] a string
[1958.76 → 1959.40] containing the
[1959.40 → 1959.74] digits
[1959.74 → 1960.64] it's going to
[1960.64 → 1961.12] accept that
[1961.12 → 1961.72] even though
[1961.72 → 1962.10] it's not a
[1962.10 → 1962.62] JSON.number
[1962.62 → 1963.82] that is not
[1963.82 → 1964.64] documented behaviour
[1964.64 → 1965.94] the documented
[1965.94 → 1966.88] behaviour it says
[1966.88 → 1968.14] this decodes
[1968.14 → 1968.52] a number
[1968.52 → 1968.96] it doesn't
[1968.96 → 1969.26] say anything
[1969.26 → 1969.72] about strings
[1969.72 → 1971.36] so I tried
[1971.36 → 1972.00] to fix that
[1972.00 → 1972.62] or I think it
[1972.62 → 1973.16] was somebody else
[1973.16 → 1973.44] and then I
[1973.44 → 1974.12] reviewed I can't
[1974.12 → 1975.12] remember and
[1975.12 → 1976.20] then as you
[1976.20 → 1976.74] would expect a
[1976.74 → 1977.14] bunch of people
[1977.14 → 1977.76] said this broke
[1977.76 → 1979.26] my code and I
[1979.26 → 1980.26] showed look with
[1980.26 → 1981.00] three lines of
[1981.00 → 1981.66] code you can fix
[1981.66 → 1982.40] if it's really
[1982.40 → 1983.08] simple, and I'm
[1983.08 → 1983.50] giving them to
[1983.50 → 1984.46] you and here's a
[1984.46 → 1985.86] playground link but
[1985.86 → 1986.50] they said no, no
[1986.50 → 1987.48] no, no like this
[1987.48 → 1987.80] is breaking
[1987.80 → 1988.90] production this is
[1988.90 → 1989.50] breaking the
[1989.50 → 1990.66] guarantee so
[1990.66 → 1992.44] oh yeah that
[1992.44 → 1993.20] does fall into
[1993.20 → 1993.96] that gray area
[1993.96 → 1994.64] doesn't it because
[1994.64 → 1995.84] you shouldn't use
[1995.84 → 1996.82] it is like that but
[1996.82 → 1997.42] because it
[1997.42 → 1998.28] worked then
[1998.28 → 1998.62] what do you
[1998.62 → 1999.18] do it is a
[1999.18 → 1999.64] tough one
[1999.64 → 2000.84] and it is
[2000.84 → 2001.54] difficult because
[2001.54 → 2002.34] you have to
[2002.34 → 2003.60] gauge am I
[2003.60 → 2004.14] breaking too
[2004.14 → 2005.30] many users like
[2005.30 → 2005.76] what is too
[2005.76 → 2006.42] many users right
[2006.42 → 2007.20] I don't know how
[2007.20 → 2007.72] people use the
[2007.72 → 2009.02] JSON package I
[2009.02 → 2009.96] could maybe look
[2009.96 → 2011.10] at the open
[2011.10 → 2011.80] source out there
[2011.80 → 2012.62] and see what the
[2012.62 → 2013.22] code looks like
[2013.22 → 2013.60] with static
[2013.60 → 2015.04] analysis but that
[2015.04 → 2015.70] would only scratch
[2015.70 → 2016.68] the surface I
[2016.68 → 2017.52] would say you
[2017.52 → 2018.50] know the go
[2018.50 → 2019.08] code out there
[2019.08 → 2019.82] that handles the
[2019.82 → 2020.74] most JSON is not
[2020.74 → 2021.76] open source most
[2021.76 → 2024.16] likely so it's
[2024.16 → 2025.04] very, very hard to
[2025.04 → 2025.64] tell if something
[2025.64 → 2026.72] could fly or not
[2026.72 → 2028.24] yeah so you
[2028.24 → 2029.52] have a version
[2029.52 → 2031.02] 2 draft don't
[2031.02 → 2032.36] you of encoding
[2032.36 → 2034.74] JSON what's that
[2034.74 → 2035.78] for is this just
[2035.78 → 2036.46] sort of your
[2036.46 → 2038.44] perfect design of
[2038.44 → 2039.26] this is what you
[2039.26 → 2040.26] would have if you
[2040.26 → 2041.78] could so for the
[2041.78 → 2042.72] time being this has
[2042.72 → 2043.44] just been a document
[2043.44 → 2044.20] for me to collect
[2044.20 → 2044.84] my own thoughts
[2044.84 → 2046.18] because I've been
[2046.18 → 2047.06] co-maintaining JSON
[2047.06 → 2048.28] for a few years and
[2048.28 → 2048.92] I've been collecting
[2048.92 → 2050.08] these little nuggets
[2050.08 → 2051.52] of stress such as
[2051.52 → 2052.12] you know I can't
[2052.12 → 2053.26] fix this and if I
[2053.26 → 2053.90] try to fix that
[2053.90 → 2054.40] people are going to
[2054.40 → 2055.68] get upset and I
[2055.68 → 2056.34] can't touch this
[2056.34 → 2057.12] because it's you
[2057.12 → 2058.10] know it's restricted
[2058.10 → 2060.04] by the API, so I've
[2060.04 → 2060.94] collected all of my
[2060.94 → 2061.82] thoughts or at least
[2061.82 → 2062.30] the ones I can
[2062.30 → 2064.12] remember and I
[2064.12 → 2065.02] haven't gotten to
[2065.02 → 2065.86] the point where I
[2065.86 → 2066.90] I've designed a new
[2066.90 → 2069.82] API because to a
[2069.82 → 2070.42] certain level that
[2070.42 → 2071.48] feels futile at this
[2071.48 → 2072.58] point because if I
[2072.58 → 2073.52] design a new JSON
[2073.52 → 2074.94] API it's not going
[2074.94 → 2075.46] to replace the
[2075.46 → 2077.10] existing API and as
[2077.10 → 2077.62] far as I know
[2077.62 → 2078.84] there's no current
[2078.84 → 2080.28] plan to do a
[2080.28 → 2081.02] version 2 of
[2081.02 → 2081.54] standard library
[2081.54 → 2082.96] packages and I
[2082.96 → 2084.26] could potentially
[2084.26 → 2085.34] write something
[2085.34 → 2087.16] externally but in
[2087.16 → 2087.92] a way I don't want
[2087.92 → 2088.96] to add to all the
[2088.96 → 2089.96] complexity that
[2089.96 → 2091.10] is you know 50
[2091.10 → 2091.92] packages that do
[2091.92 → 2092.58] JSON and go
[2092.58 → 2095.12] I wonder what a
[2095.12 → 2096.04] sensible approach
[2096.04 → 2097.20] would be whether you
[2097.20 → 2098.34] could just add some
[2098.34 → 2099.66] new methods to the
[2099.66 → 2100.82] to the JSON
[2100.82 → 2102.40] package yeah and
[2102.40 → 2102.88] that is a good
[2102.88 → 2105.10] point and there
[2105.10 → 2106.32] are some bugs for
[2106.32 → 2108.12] example there's one
[2108.12 → 2109.44] that I would say
[2109.44 → 2110.64] affects most code
[2110.64 → 2111.32] bases out there
[2111.32 → 2112.58] which is the
[2112.58 → 2113.62] standard you know
[2113.62 → 2114.62] you have an HTTP
[2114.62 → 2115.88] endpoint and the
[2115.88 → 2116.74] body is JSON so
[2116.74 → 2117.38] you want to decode
[2117.38 → 2118.68] it so what you do
[2118.68 → 2119.70] is you take the
[2119.70 → 2121.26] r.body and you do
[2121.26 → 2123.74] Jason. New decoder
[2123.74 → 2125.10] .decode with the
[2125.10 → 2126.36] body and then into
[2126.36 → 2127.88] some structure and
[2127.88 → 2128.54] if you do that it's
[2128.54 → 2129.80] buggy if you just
[2129.80 → 2130.78] do that I've just
[2130.78 → 2133.14] got to go what do
[2133.14 → 2133.54] you mean it's
[2133.54 → 2134.62] buggy tell me why
[2134.62 → 2135.98] please so this was
[2135.98 → 2138.00] found by Joe one of
[2138.00 → 2139.02] the maintainers I
[2139.02 → 2139.80] want to say about
[2139.80 → 2140.72] a year ago and
[2140.72 → 2142.16] the bug is the
[2142.16 → 2143.32] decoder is meant
[2143.32 → 2145.90] to be useful for
[2145.90 → 2147.00] streams of JSON
[2147.00 → 2148.72] values and that is
[2148.72 → 2149.34] for example when you
[2149.34 → 2150.78] do go test with the
[2150.78 → 2151.82] JSON flag it's going
[2151.82 → 2152.98] to give you a new
[2152.98 → 2154.72] line separated stream
[2154.72 → 2155.98] of JSON
[2155.98 → 2156.76] values of JSON
[2156.76 → 2157.72] objects yeah that's
[2157.72 → 2158.42] kind of how I was
[2158.42 → 2159.38] using in those tools
[2159.38 → 2160.28] I was talking about
[2160.28 → 2161.44] yeah exactly in a
[2161.44 → 2162.86] way it is kind of
[2162.86 → 2164.18] streaming in a way
[2164.18 → 2165.02] like it takes the
[2165.02 → 2166.34] reader for each
[2166.34 → 2168.02] object it buffers
[2168.02 → 2169.36] it I guess but it
[2169.36 → 2170.38] discards that previous
[2170.38 → 2171.36] object doesn't it
[2171.36 → 2172.56] yeah, yeah next time
[2172.56 → 2174.06] right so in a sense
[2174.06 → 2175.16] it's streaming it
[2175.16 → 2176.40] appears to you as of
[2176.40 → 2177.02] a streaming but
[2177.02 → 2177.70] internally that's
[2177.70 → 2178.20] not what it's doing
[2178.20 → 2179.46] well it's still doing
[2179.46 → 2180.78] it only one object at
[2180.78 → 2181.66] a time which you
[2181.66 → 2182.36] could say is a
[2182.36 → 2183.18] stream it's just if
[2183.18 → 2184.28] it's a great big fat
[2184.28 → 2185.12] object then
[2185.12 → 2186.90] exactly in trouble
[2186.90 → 2187.92] yeah you might
[2187.92 → 2188.96] maybe yeah so I
[2188.96 → 2189.64] would say just
[2189.64 → 2190.32] assumes that your
[2190.32 → 2190.88] values are going to
[2190.88 → 2192.52] be small right so
[2192.52 → 2193.84] it doesn't imagine
[2193.84 → 2194.44] that you would ever
[2194.44 → 2195.26] have a JSON object
[2195.26 → 2196.12] weighing 200
[2196.12 → 2197.40] megabytes and if
[2197.40 → 2198.12] you do that it just
[2198.12 → 2198.96] goes like whoops I'm
[2198.96 → 2199.72] just going to buffer that
[2199.72 → 2200.28] essentially
[2200.28 → 2202.64] you couldn't do that
[2202.64 → 2203.72] on your machine
[2203.72 → 2204.92] today for example
[2204.92 → 2205.52] you don't have the
[2205.52 → 2205.74] RAM
[2205.74 → 2207.74] if you want me to
[2207.74 → 2208.24] leave you can just
[2208.24 → 2208.84] say that
[2208.84 → 2212.14] please don't
[2212.14 → 2213.46] you'll have to in
[2213.46 → 2214.08] about eight minutes
[2214.08 → 2214.52] anyway
[2214.52 → 2217.48] yeah I'm currently at
[2217.48 → 2218.76] 30% I've still got
[2218.76 → 2219.46] yeah like seven or
[2219.46 → 2219.90] eight minutes
[2219.90 → 2221.04] I wonder if it's
[2221.04 → 2221.70] based on how much
[2221.70 → 2222.46] you say as well
[2222.46 → 2223.08] surely when you
[2223.08 → 2224.14] when you talk it
[2224.14 → 2225.18] must use more RAM
[2225.18 → 2226.62] okay let me yell
[2226.62 → 2227.24] into the microphone
[2227.24 → 2228.04] and then just watch
[2228.04 → 2228.88] the RAM go up
[2228.88 → 2229.72] I don't know how
[2229.72 → 2230.28] it yeah I don't
[2230.28 → 2230.64] know how it
[2230.64 → 2231.30] structures it
[2231.30 → 2233.40] maybe I know
[2233.40 → 2233.86] what it's doing
[2233.86 → 2234.80] it's storing it in
[2234.80 → 2236.06] JSON isn't it
[2236.06 → 2237.14] yeah yeah
[2237.14 → 2237.88] maybe yeah
[2237.88 → 2239.30] maybe every wave
[2239.30 → 2240.62] is a JSON object
[2240.62 → 2241.52] yeah exactly
[2241.52 → 2242.14] being streamed
[2242.14 → 2242.40] somewhere
[2242.40 → 2243.56] it's not perfect
[2243.56 → 2244.68] JSON for every
[2244.68 → 2245.98] type of data
[2245.98 → 2246.76] is it sometimes
[2246.76 → 2247.80] binary data
[2247.80 → 2248.88] is better
[2248.88 → 2250.10] which actually leads
[2250.10 → 2250.76] us to a good
[2250.76 → 2251.90] segue here because
[2251.90 → 2253.32] yes JSON is
[2253.32 → 2253.92] is awesome
[2253.92 → 2254.84] it's human-readable
[2254.84 → 2255.70] you know but
[2255.70 → 2256.42] most of the time
[2256.42 → 2257.10] you know we have
[2257.10 → 2258.16] machines talking to
[2258.16 → 2258.54] each other
[2258.54 → 2260.30] so are there
[2260.30 → 2261.30] cases where
[2261.30 → 2262.16] for efficiency
[2262.16 → 2263.52] right of transport
[2263.52 → 2265.04] and storage
[2265.04 → 2265.46] perhaps
[2265.46 → 2266.46] it just makes
[2266.46 → 2267.20] more sense
[2267.20 → 2268.12] to just
[2268.12 → 2269.32] pick a binary
[2269.32 → 2269.82] format
[2269.82 → 2270.80] instead of the
[2270.80 → 2271.56] text base
[2271.56 → 2272.60] JSON passing
[2272.60 → 2273.74] back and forth
[2273.74 → 2274.16] especially
[2274.16 → 2275.50] if it's a stream
[2275.50 → 2276.08] of data
[2276.08 → 2277.30] or you know
[2277.30 → 2277.90] if you're ingesting
[2277.90 → 2278.76] a ton of information
[2278.76 → 2279.88] unless you're debugging
[2279.88 → 2280.84] really as a developer
[2280.84 → 2282.46] perhaps locally
[2282.46 → 2282.88] I mean
[2282.88 → 2283.70] there's no way
[2283.70 → 2284.02] you're going to be
[2284.02 → 2284.86] wading through
[2284.86 → 2286.20] vast amounts of
[2286.20 → 2286.48] JSON
[2286.48 → 2287.08] trying to
[2287.08 → 2287.94] read that
[2287.94 → 2288.44] and take advantage
[2288.44 → 2288.84] of the human
[2288.84 → 2289.72] readability aspect
[2289.72 → 2289.96] of it
[2289.96 → 2290.08] right
[2290.08 → 2290.84] so when
[2290.84 → 2291.68] should you give
[2291.68 → 2292.50] yourself a pass
[2292.50 → 2292.74] right
[2292.74 → 2293.32] and sort of
[2293.32 → 2294.10] not necessarily
[2294.10 → 2295.30] use JSON
[2295.30 → 2295.84] for the sake
[2295.84 → 2296.38] of using JSON
[2296.38 → 2296.86] because everybody
[2296.86 → 2297.70] else is using JSON
[2297.70 → 2297.96] right
[2297.96 → 2298.78] like what is a good
[2298.78 → 2299.34] sort of
[2299.34 → 2300.04] set of a
[2300.04 → 2301.12] criteria for making
[2301.12 → 2301.52] the decision
[2301.52 → 2302.54] against using JSON
[2302.54 → 2303.44] that's a good
[2303.44 → 2303.74] question
[2303.74 → 2304.48] before I answer
[2304.48 → 2304.76] that
[2304.76 → 2305.72] I just want to
[2305.72 → 2306.84] briefly mention
[2306.84 → 2307.42] what the
[2307.42 → 2308.16] bug was
[2308.16 → 2308.64] in the previous
[2308.64 → 2309.08] point
[2309.08 → 2311.48] sorry that's
[2311.48 → 2311.86] my fault
[2311.86 → 2312.58] of being stupid
[2312.58 → 2313.60] don't worry
[2313.60 → 2314.22] it's just more
[2314.22 → 2314.74] work for the
[2314.74 → 2315.10] editors
[2315.10 → 2315.56] clap
[2315.56 → 2316.18] okay
[2316.18 → 2317.32] you just clap
[2317.32 → 2318.26] and it fixes it
[2318.26 → 2319.84] has this ever
[2319.84 → 2320.62] happened to you
[2320.62 → 2321.24] presenting
[2321.24 → 2322.08] the clapper
[2322.08 → 2323.26] clap on the music
[2323.26 → 2326.44] it's easy
[2326.44 → 2327.82] clap on
[2327.82 → 2328.76] clap off
[2328.76 → 2330.62] the clapper
[2330.62 → 2332.34] so Daniel
[2332.34 → 2332.86] tell us
[2332.86 → 2333.52] what's the bug
[2333.52 → 2334.64] with r.body
[2334.64 → 2335.92] and reading it
[2335.92 → 2336.92] through the
[2336.92 → 2337.44] decoder
[2337.44 → 2338.58] so the bug
[2338.58 → 2339.12] is that you're
[2339.12 → 2339.70] only decoding
[2339.70 → 2340.34] one object
[2340.34 → 2341.16] but what if
[2341.16 → 2341.48] the body
[2341.48 → 2342.54] contained multiple
[2342.54 → 2343.48] values
[2343.48 → 2344.38] in multiple
[2344.38 → 2344.86] you know
[2344.86 → 2345.32] separated by
[2345.32 → 2345.68] new lines
[2345.68 → 2346.04] or something
[2346.04 → 2346.38] you're not
[2346.38 → 2346.54] going to
[2346.54 → 2346.80] notice
[2346.80 → 2347.14] you're just
[2347.14 → 2347.30] going to
[2347.30 → 2347.64] close the
[2347.64 → 2347.84] body
[2347.84 → 2348.08] straight
[2348.08 → 2348.34] after
[2348.34 → 2349.28] so if
[2349.28 → 2349.74] the client
[2349.74 → 2350.44] even if
[2350.44 → 2350.70] you don't
[2350.70 → 2351.26] support that
[2351.26 → 2351.88] if the client
[2351.88 → 2352.28] was trying
[2352.28 → 2352.86] to send
[2352.86 → 2353.98] you three
[2353.98 → 2354.46] objects
[2354.46 → 2355.20] separated by
[2355.20 → 2355.66] new lines
[2355.66 → 2356.20] you're going
[2356.20 → 2356.90] to use the
[2356.90 → 2357.38] first one
[2357.38 → 2357.78] and ignore
[2357.78 → 2358.06] the other
[2358.06 → 2358.32] two
[2358.32 → 2359.28] which is
[2359.28 → 2359.78] most likely
[2359.78 → 2360.14] not what
[2360.14 → 2360.38] you want
[2360.38 → 2360.64] to do
[2360.64 → 2361.48] you would
[2361.48 → 2361.88] either want
[2361.88 → 2362.36] to error
[2362.36 → 2363.06] or use all
[2363.06 → 2363.40] the data
[2363.40 → 2364.68] yeah that's
[2364.68 → 2365.18] quite interesting
[2365.18 → 2366.20] if you reach
[2366.20 → 2366.58] the end of
[2366.58 → 2367.18] the stream
[2367.18 → 2368.36] what happens
[2368.36 → 2368.92] when you try
[2368.92 → 2369.66] and decode
[2369.66 → 2370.84] using the
[2370.84 → 2371.42] decoder
[2371.42 → 2372.48] well I imagine
[2372.48 → 2373.10] it's going to
[2373.10 → 2374.20] wrap EOF
[2374.20 → 2374.80] and give you
[2374.80 → 2375.22] that error
[2375.22 → 2375.72] or something
[2375.72 → 2375.96] like that
[2375.96 → 2376.98] yeah
[2376.98 → 2378.26] so you could
[2378.26 → 2378.84] support it
[2378.84 → 2379.42] by having a
[2379.42 → 2379.70] loop
[2379.70 → 2380.12] and just
[2380.12 → 2380.82] keep looping
[2380.82 → 2381.30] and keep
[2381.30 → 2381.82] decoding
[2381.82 → 2383.44] but yeah
[2383.44 → 2383.82] but again
[2383.82 → 2384.42] that's kind
[2384.42 → 2385.24] of yeah
[2385.24 → 2385.52] I don't know
[2385.52 → 2385.88] it's quite
[2385.88 → 2386.34] strange I
[2386.34 → 2387.04] think when
[2387.04 → 2387.32] you think
[2387.32 → 2387.78] about an
[2387.78 → 2388.46] array in
[2388.46 → 2388.84] JSON
[2388.84 → 2389.62] an array
[2389.62 → 2390.38] can be
[2390.38 → 2391.02] well is
[2391.02 → 2392.06] often
[2392.06 → 2393.38] many objects
[2393.38 → 2394.38] inside
[2394.38 → 2394.90] an array
[2394.90 → 2395.94] that could
[2395.94 → 2396.24] be the
[2396.24 → 2396.56] payload
[2396.56 → 2396.90] and that
[2396.90 → 2397.26] would actually
[2397.26 → 2397.92] still work
[2397.92 → 2398.36] wouldn't it
[2398.36 → 2399.46] wouldn't hit
[2399.46 → 2399.96] that bug
[2399.96 → 2400.58] it's just
[2400.58 → 2401.48] if you're
[2401.48 → 2402.02] using new
[2402.02 → 2402.84] line separated
[2402.84 → 2403.80] JSON objects
[2403.80 → 2404.26] yeah
[2404.26 → 2405.26] and in that
[2405.26 → 2405.72] case you can
[2405.72 → 2406.52] fix the code
[2406.52 → 2407.14] pretty easily
[2407.14 → 2407.74] you can just
[2407.74 → 2408.92] add a check
[2408.92 → 2409.26] at the end
[2409.26 → 2409.74] that says
[2409.74 → 2410.78] if the decoder
[2410.78 → 2411.50] has more
[2411.50 → 2412.76] tokens
[2412.76 → 2413.74] to be decoded
[2413.74 → 2414.84] then give some
[2414.84 → 2415.10] error
[2415.10 → 2415.70] you can do
[2415.70 → 2415.92] that
[2415.92 → 2416.54] but the thing
[2416.54 → 2416.88] is that
[2416.88 → 2417.40] obviously
[2417.40 → 2418.00] people have
[2418.00 → 2418.30] to remember
[2418.30 → 2419.02] to do that
[2419.02 → 2420.32] and to begin
[2420.32 → 2420.74] with nobody
[2420.74 → 2421.32] knew to do
[2421.32 → 2421.56] that
[2421.56 → 2422.00] so
[2422.00 → 2423.08] it's just
[2423.08 → 2424.04] I would say
[2424.04 → 2424.98] it's
[2424.98 → 2425.76] complicated
[2425.76 → 2426.66] API design
[2426.66 → 2427.02] because it's
[2427.02 → 2427.40] very easy
[2427.40 → 2427.96] to misuse
[2427.96 → 2428.74] yeah but
[2428.74 → 2429.24] to be honest
[2429.24 → 2429.50] mate
[2429.50 → 2430.52] I don't know
[2430.52 → 2431.16] of any API
[2431.16 → 2431.68] where you
[2431.68 → 2432.74] send multiple
[2432.74 → 2433.68] lines of
[2433.68 → 2434.26] JSON like
[2434.26 → 2434.52] that
[2434.52 → 2435.32] I could be
[2435.32 → 2435.56] wrong
[2435.56 → 2436.56] but I don't
[2436.56 → 2436.90] think I've
[2436.90 → 2437.34] seen that
[2437.34 → 2438.06] yeah
[2438.06 → 2438.80] if an API
[2438.80 → 2439.40] was like
[2439.40 → 2439.62] that
[2439.62 → 2440.06] you would
[2440.06 → 2440.36] probably
[2440.36 → 2440.72] implement
[2440.72 → 2441.20] it properly
[2441.20 → 2442.12] and I
[2442.12 → 2442.76] agree
[2442.76 → 2443.14] this is
[2443.14 → 2443.36] probably
[2443.36 → 2444.16] not a
[2444.16 → 2444.44] problem
[2444.44 → 2445.00] in real
[2445.00 → 2445.38] life
[2445.38 → 2446.14] but it's
[2446.14 → 2446.40] still an
[2446.40 → 2446.78] edge case
[2446.78 → 2447.84] that exists
[2447.84 → 2449.16] and kind
[2449.16 → 2449.30] of
[2449.30 → 2449.96] very few
[2449.96 → 2450.32] people have
[2450.32 → 2450.78] thought about
[2450.78 → 2451.26] and is
[2451.26 → 2451.76] technically
[2451.76 → 2452.16] a bug
[2452.16 → 2453.08] this is
[2453.08 → 2453.30] what I
[2453.30 → 2453.78] love about
[2453.78 → 2454.46] people that
[2454.46 → 2455.32] maintain these
[2455.32 → 2456.06] packages for
[2456.06 → 2456.26] us
[2456.26 → 2456.70] you know
[2456.70 → 2457.76] it's really
[2457.76 → 2458.16] hard
[2458.16 → 2458.66] and you
[2458.66 → 2459.16] have to
[2459.16 → 2459.60] kind of
[2459.60 → 2460.28] care about
[2460.28 → 2460.94] everything
[2460.94 → 2461.64] but that's
[2461.64 → 2462.34] nice because
[2462.34 → 2462.70] it means
[2462.70 → 2463.10] the rest of
[2463.10 → 2463.70] us don't
[2463.70 → 2464.10] have to
[2464.10 → 2466.16] and going
[2466.16 → 2466.66] to Johnny's
[2466.66 → 2466.98] question
[2466.98 → 2467.42] he was
[2467.42 → 2468.14] asking about
[2468.14 → 2469.18] when do you
[2469.18 → 2469.74] choose between
[2469.74 → 2470.64] JSON or
[2470.64 → 2471.20] something that's
[2471.20 → 2471.76] plain text
[2471.76 → 2472.38] some format
[2472.38 → 2473.06] that's plain text
[2473.06 → 2473.94] versus something
[2473.94 → 2474.52] that's binary
[2474.52 → 2475.80] and I think
[2475.80 → 2476.12] there are
[2476.12 → 2476.54] multiple
[2476.54 → 2477.58] schools of
[2477.58 → 2478.08] thought there
[2478.08 → 2478.92] but I
[2478.92 → 2479.44] think the
[2479.44 → 2480.10] consensus
[2480.10 → 2480.96] between most
[2480.96 → 2481.40] programmers
[2481.40 → 2482.22] is that
[2482.22 → 2483.28] if it's
[2483.28 → 2483.68] something that
[2483.68 → 2484.02] a human
[2484.02 → 2484.32] is going
[2484.32 → 2484.70] to deal
[2484.70 → 2484.98] with
[2484.98 → 2485.44] such as
[2485.44 → 2485.72] a human
[2485.72 → 2485.92] is going
[2485.92 → 2486.24] to debug
[2486.24 → 2486.50] it
[2486.50 → 2486.96] or a human
[2486.96 → 2487.20] is going
[2487.20 → 2487.44] to look
[2487.44 → 2487.74] at it
[2487.74 → 2488.48] or a human
[2488.48 → 2488.74] is going
[2488.74 → 2488.98] to use
[2488.98 → 2489.22] it or
[2489.22 → 2489.58] write it
[2489.58 → 2490.44] you most
[2490.44 → 2490.92] likely want
[2490.92 → 2491.34] it to be
[2491.34 → 2492.10] plain text
[2492.10 → 2492.44] if you can
[2492.44 → 2492.88] afford it
[2492.88 → 2493.42] something like
[2493.42 → 2494.66] JSON or
[2494.66 → 2495.12] YAML and
[2495.12 → 2495.42] so on
[2495.42 → 2496.38] but if it's
[2496.38 → 2496.78] something that
[2496.78 → 2497.18] has to be
[2497.18 → 2497.56] efficient
[2497.56 → 2498.24] maybe because
[2498.24 → 2498.44] you have
[2498.44 → 2498.84] tons of
[2498.84 → 2499.18] it or
[2499.18 → 2499.66] maybe because
[2499.66 → 2499.96] it's only
[2499.96 → 2500.32] machines
[2500.32 → 2500.82] talking to
[2500.82 → 2501.14] each other
[2501.14 → 2502.54] then it
[2502.54 → 2502.90] might be
[2502.90 → 2503.26] of interest
[2503.26 → 2503.54] to you
[2503.54 → 2503.98] to consider
[2503.98 → 2504.40] a binary
[2504.40 → 2504.78] format
[2504.78 → 2505.20] that's
[2505.20 → 2505.36] more
[2505.36 → 2505.66] efficient
[2505.66 → 2506.34] that uses
[2506.34 → 2506.98] less space
[2506.98 → 2507.66] and so on
[2507.66 → 2508.78] yeah and I
[2508.78 → 2509.38] think that
[2509.38 → 2510.50] argument also
[2510.50 → 2511.16] applies to
[2511.16 → 2511.66] the whole
[2511.66 → 2512.68] debate around
[2512.68 → 2514.00] gRPC versus
[2514.00 → 2515.36] JSON APIs
[2515.36 → 2516.36] it's kind of
[2516.36 → 2516.70] the same
[2516.70 → 2517.26] thing you know
[2517.26 → 2517.94] there might be
[2517.94 → 2518.48] good reasons
[2518.48 → 2519.12] why you need
[2519.12 → 2519.70] this really
[2519.70 → 2520.22] low level
[2520.22 → 2520.74] binary
[2520.74 → 2521.34] you want
[2521.34 → 2522.04] it to be
[2522.04 → 2522.86] most efficient
[2522.86 → 2523.38] it possibly
[2523.38 → 2523.94] can be
[2523.94 → 2524.60] but yeah
[2524.60 → 2525.26] you hurt
[2525.26 → 2526.06] developer
[2526.06 → 2526.64] friendliness
[2526.64 → 2527.30] for sure
[2527.30 → 2528.10] it's nice
[2528.10 → 2528.88] when you
[2528.88 → 2530.38] use a
[2530.38 → 2531.20] or even
[2531.20 → 2531.54] when you're
[2531.54 → 2532.00] building it
[2532.00 → 2532.36] but even
[2532.36 → 2532.90] using it
[2532.90 → 2533.34] if you want
[2533.34 → 2534.02] to explore
[2534.02 → 2534.66] what's
[2534.66 → 2535.02] happening
[2535.02 → 2535.72] you can
[2535.72 → 2536.04] sometimes
[2536.04 → 2536.72] poke around
[2536.72 → 2537.04] in the
[2537.04 → 2537.38] browser
[2537.38 → 2538.06] inside the
[2538.06 → 2538.64] little network
[2538.64 → 2539.10] tab and
[2539.10 → 2539.68] see the
[2539.68 → 2540.40] see the
[2540.40 → 2541.26] HTTP requests
[2541.26 → 2541.78] and have a
[2541.78 → 2542.20] look at the
[2542.20 → 2542.92] JSON bodies
[2542.92 → 2543.80] and I find
[2543.80 → 2544.18] that to be
[2544.18 → 2544.78] very useful
[2544.78 → 2545.26] particularly
[2545.26 → 2545.94] if I'm
[2545.94 → 2546.60] developing
[2546.60 → 2547.80] so yeah
[2547.80 → 2548.18] which of
[2548.18 → 2548.48] course I
[2548.48 → 2548.98] think you'd
[2548.98 → 2549.54] need extra
[2549.54 → 2550.12] tooling in
[2550.12 → 2550.46] order to
[2550.46 → 2550.78] do that
[2550.78 → 2551.42] if you were
[2551.42 → 2551.62] going to
[2551.62 → 2552.06] use some
[2552.06 → 2552.34] kind of
[2552.34 → 2552.80] gRPC
[2552.80 → 2553.26] thing I
[2553.26 → 2553.50] think
[2553.50 → 2554.30] I definitely
[2554.30 → 2554.60] agree
[2554.60 → 2555.18] I would
[2555.18 → 2555.60] say by
[2555.60 → 2556.00] default
[2556.00 → 2556.52] choose plain
[2556.52 → 2557.26] text and
[2557.26 → 2558.02] only carefully
[2558.02 → 2558.80] consider binary
[2558.80 → 2559.92] or even
[2559.92 → 2560.56] better support
[2560.56 → 2560.92] both
[2560.92 → 2561.90] many people
[2561.90 → 2562.54] that build
[2562.54 → 2563.46] gRPC services
[2563.46 → 2564.56] they add
[2564.56 → 2565.00] something on
[2565.00 → 2565.52] top like a
[2565.52 → 2566.20] REST gateway
[2566.20 → 2567.28] and then you
[2567.28 → 2567.80] can the
[2567.80 → 2568.54] client can
[2568.54 → 2569.12] choose which
[2569.12 → 2569.66] one to use
[2569.66 → 2570.46] maybe they
[2570.46 → 2571.02] use gRPC
[2571.02 → 2572.00] for a machine
[2572.00 → 2572.60] but maybe a
[2572.60 → 2573.04] human that's
[2573.04 → 2573.58] debugging is
[2573.58 → 2573.92] going to use
[2573.92 → 2574.28] REST
[2574.28 → 2575.32] with JSON
[2575.32 → 2576.76] yeah absolutely
[2576.76 → 2577.38] I think that's a
[2577.38 → 2578.00] sound approach
[2578.00 → 2578.56] but I would
[2578.56 → 2579.34] agree start
[2579.34 → 2579.78] with the
[2579.78 → 2580.36] JSON one
[2580.36 → 2581.10] because in
[2581.10 → 2581.52] the beginning
[2581.52 → 2582.30] that's the
[2582.30 → 2583.18] most easy
[2583.18 → 2583.98] to work with
[2583.98 → 2584.86] and maybe
[2584.86 → 2585.24] it's all
[2585.24 → 2585.54] you're ever
[2585.54 → 2585.78] going to
[2585.78 → 2586.08] need
[2586.08 → 2586.66] are you
[2586.66 → 2587.22] saying it's
[2587.22 → 2587.96] a YAGNI
[2587.96 → 2588.72] situation
[2588.72 → 2590.10] YAGNI
[2590.10 → 2591.08] what is
[2591.08 → 2591.38] YAGNI
[2591.38 → 2593.22] oh you
[2593.22 → 2593.62] haven't been
[2593.62 → 2594.46] indoctrinated
[2594.46 → 2595.10] into the
[2595.10 → 2596.24] Ruby ecosystem
[2596.24 → 2596.88] YAGNI is
[2596.88 → 2597.28] something that
[2597.28 → 2598.02] was popularized
[2598.02 → 2599.32] by a very
[2599.32 → 2600.36] popular framework
[2600.36 → 2601.10] author in the
[2601.10 → 2601.82] Ruby ecosystem
[2601.82 → 2602.80] YAGNI stands
[2602.80 → 2603.46] for you ain't
[2603.46 → 2604.24] going to need it
[2604.24 → 2607.04] so I'm
[2607.04 → 2607.66] copying that
[2607.66 → 2608.78] yeah it's
[2608.78 → 2610.26] good isn't
[2610.26 → 2611.48] it yes
[2611.48 → 2612.08] indeed
[2612.08 → 2612.90] I still pull
[2612.90 → 2613.24] that out
[2613.24 → 2613.96] every once
[2613.96 → 2614.30] in a while
[2614.30 → 2615.46] but I do
[2615.46 → 2615.84] think there's
[2615.84 → 2616.34] one point
[2616.34 → 2616.64] that we
[2616.64 → 2616.96] might have
[2616.96 → 2617.44] missed here
[2617.44 → 2618.04] which is
[2618.04 → 2619.28] defining your
[2619.28 → 2619.94] data model
[2619.94 → 2620.80] and I think
[2620.80 → 2621.64] that's probably
[2621.64 → 2622.06] the place
[2622.06 → 2622.52] where JSON
[2622.52 → 2623.12] falls short
[2623.12 → 2623.56] the most
[2623.56 → 2624.04] and where
[2624.04 → 2624.50] it bites
[2624.50 → 2624.90] people the
[2624.90 → 2625.16] most
[2625.16 → 2626.48] and that's
[2626.48 → 2626.82] where things
[2626.82 → 2627.28] like JSON
[2627.28 → 2627.92] schema come
[2627.92 → 2628.90] in but
[2628.90 → 2629.68] I wouldn't
[2629.68 → 2630.04] say they're
[2630.04 → 2630.62] very good
[2630.62 → 2631.08] solutions
[2631.08 → 2631.86] they mostly
[2631.86 → 2632.78] tried to
[2632.78 → 2633.22] port the
[2633.22 → 2634.10] XML solutions
[2634.10 → 2635.18] 20 years
[2635.18 → 2636.08] ago to
[2636.08 → 2636.44] JSON
[2636.44 → 2637.44] I don't
[2637.44 → 2637.76] think they're
[2637.76 → 2638.12] a very good
[2638.12 → 2638.48] approach
[2638.48 → 2639.18] I think
[2639.18 → 2640.08] a proper
[2640.08 → 2640.88] schema language
[2640.88 → 2641.82] like
[2641.82 → 2642.48] proof
[2642.48 → 2643.46] and gRPC
[2643.46 → 2644.26] are better
[2644.26 → 2645.78] so you
[2645.78 → 2646.02] have to
[2646.02 → 2646.40] choose
[2646.40 → 2647.12] sort of
[2647.12 → 2647.42] the trade
[2647.42 → 2647.86] off between
[2647.86 → 2648.38] you know
[2648.38 → 2649.06] do I
[2649.06 → 2649.58] use something
[2649.58 → 2650.04] simple
[2650.04 → 2650.86] like JSON
[2650.86 → 2651.30] and then
[2651.30 → 2651.56] just get
[2651.56 → 2651.92] going
[2651.92 → 2652.86] or do I
[2652.86 → 2653.18] choose a
[2653.18 → 2653.74] schema language
[2653.74 → 2654.10] that's going
[2654.10 → 2654.70] to let me
[2654.70 → 2655.42] define my
[2655.42 → 2656.12] types properly
[2656.12 → 2656.68] and so on
[2656.68 → 2657.82] yeah and that's
[2657.82 → 2658.32] probably use
[2658.32 → 2658.82] case driven
[2658.82 → 2659.18] as well
[2659.18 → 2659.54] isn't it
[2659.54 → 2660.20] it's in
[2660.20 → 2660.96] some situations
[2660.96 → 2661.60] if you are
[2661.60 → 2662.50] working with
[2662.50 → 2663.94] generic data
[2663.94 → 2665.14] and you don't
[2665.14 → 2665.76] know the shape
[2665.76 → 2666.42] of that data
[2666.42 → 2667.52] and that does
[2667.52 → 2668.32] sometimes happen
[2668.32 → 2668.90] I've worked
[2668.90 → 2669.48] on projects
[2669.48 → 2670.06] for sure
[2670.06 → 2671.30] where it's
[2671.30 → 2671.78] it's a kind
[2671.78 → 2672.30] of platform
[2672.30 → 2673.12] and you don't
[2673.12 → 2673.62] know what
[2673.62 → 2674.12] the data
[2674.12 → 2675.60] is ahead
[2675.60 → 2676.06] of time
[2676.06 → 2678.24] then that
[2678.24 → 2679.08] does kind
[2679.08 → 2679.90] of lead
[2679.90 → 2680.42] you one way
[2680.42 → 2680.84] or the other
[2680.84 → 2681.76] the nice thing
[2681.76 → 2682.36] about JSON
[2682.36 → 2683.10] though is that
[2683.10 → 2683.78] you can always
[2683.78 → 2684.60] add fields
[2684.60 → 2685.04] to it
[2685.04 → 2685.46] can't you
[2685.46 → 2686.08] you can always
[2686.08 → 2687.24] add fields
[2687.24 → 2688.08] and previous
[2688.08 → 2689.00] code will just
[2689.00 → 2690.06] continue to work
[2690.06 → 2691.06] because in a
[2691.06 → 2692.34] struct in Go
[2692.34 → 2693.54] if there's a
[2693.54 → 2694.16] field missing
[2694.16 → 2694.74] in the struct
[2694.74 → 2695.38] but it's present
[2695.38 → 2696.02] in the JSON
[2696.02 → 2696.88] by default
[2696.88 → 2697.56] it just gets
[2697.56 → 2697.98] ignored
[2697.98 → 2698.62] doesn't it
[2698.62 → 2699.64] yep that's a
[2699.64 → 2700.08] very good point
[2700.08 → 2701.10] JSON does
[2701.10 → 2702.74] allow backwards
[2702.74 → 2703.14] compatibility
[2703.14 → 2704.12] pretty easily
[2704.12 → 2705.06] if you are
[2705.06 → 2705.48] okay with
[2705.48 → 2706.04] maintaining the
[2706.04 → 2706.60] previous fields
[2706.60 → 2707.04] and so on
[2707.04 → 2708.02] and I think
[2708.02 → 2708.98] most formats
[2708.98 → 2709.60] are like that
[2709.60 → 2710.18] for example
[2710.18 → 2711.36] proof if you
[2711.36 → 2711.84] just add things
[2711.84 → 2712.32] at the end
[2712.32 → 2713.46] with new IDs
[2713.46 → 2714.58] that's also
[2714.58 → 2715.92] fine but
[2715.92 → 2716.94] it is less
[2716.94 → 2717.26] intuitive
[2717.26 → 2718.48] it is a little
[2718.48 → 2718.94] bit of extra
[2718.94 → 2719.60] complexity to
[2719.60 → 2720.20] think about that
[2720.20 → 2721.42] I agree
[2721.42 → 2723.00] but it keeps
[2723.00 → 2723.62] my old stuff
[2723.62 → 2724.66] working so
[2724.66 → 2725.30] I don't know
[2725.30 → 2726.56] it's a trade
[2726.56 → 2726.94] I'm willing
[2726.94 → 2727.36] to make
[2727.36 → 2728.72] and are
[2728.72 → 2729.36] there other
[2729.36 → 2730.08] kinds of
[2730.08 → 2731.56] efficiencies to
[2731.56 → 2732.16] be had in the
[2732.16 → 2732.86] current implementation
[2732.86 → 2733.66] then would it
[2733.66 → 2734.28] be possible to
[2734.28 → 2735.18] make changes
[2735.18 → 2736.66] and say reduce
[2736.66 → 2737.76] allocations in
[2737.76 → 2738.56] the process of
[2738.56 → 2739.52] decoding JSON
[2739.52 → 2741.00] yep and that
[2741.00 → 2742.04] is kind of
[2742.04 → 2742.62] where most of
[2742.62 → 2743.24] my work has
[2743.24 → 2744.44] gone because
[2744.44 → 2745.26] I didn't like I
[2745.26 → 2745.72] said before I
[2745.72 → 2746.54] didn't want to
[2746.54 → 2747.30] just write a
[2747.30 → 2748.10] new package and
[2748.10 → 2748.70] just add to
[2748.70 → 2749.58] the fire that
[2749.58 → 2751.14] is making new
[2751.14 → 2751.84] code developers
[2751.84 → 2752.46] choose between
[2752.46 → 2753.10] 20 packages
[2753.10 → 2755.32] so I did do
[2755.32 → 2756.04] some changes to
[2756.04 → 2756.46] the internal
[2756.46 → 2757.44] such as
[2757.44 → 2758.34] don't do
[2758.34 → 2759.08] work twice
[2759.08 → 2759.70] or cache
[2759.70 → 2760.28] some stuff
[2760.28 → 2761.54] or remove
[2761.54 → 2762.40] a bounce check
[2762.40 → 2763.08] here and there
[2763.08 → 2763.56] and stuff like
[2763.56 → 2764.42] that and I
[2764.42 → 2764.84] think it was
[2764.84 → 2765.44] between go
[2765.44 → 2766.44] 110 and
[2766.44 → 2767.14] go 113
[2767.14 → 2768.12] that the
[2768.12 → 2769.16] decoder if
[2769.16 → 2769.62] you mostly
[2769.62 → 2770.76] use structs
[2770.76 → 2771.46] so no maps
[2771.46 → 2773.26] it got about
[2773.26 → 2774.34] 30 to 50%
[2774.34 → 2775.48] faster which
[2775.48 → 2776.26] was pretty nice
[2776.26 → 2777.54] but you have
[2777.54 → 2777.94] to understand
[2777.94 → 2778.18] that the
[2778.18 → 2778.68] base point
[2778.68 → 2779.78] was pretty
[2779.78 → 2780.12] low
[2780.12 → 2781.62] so initially
[2781.62 → 2782.66] you don't have
[2782.66 → 2783.20] to say that
[2783.20 → 2784.02] just focus on
[2784.02 → 2784.52] the improvement
[2784.52 → 2785.34] yeah exactly
[2785.34 → 2787.16] 30%
[2787.16 → 2787.70] faster
[2787.70 → 2788.78] but I will
[2788.78 → 2789.28] also say
[2789.28 → 2789.82] that the
[2789.82 → 2790.48] packages that
[2790.48 → 2791.20] claim to
[2791.20 → 2791.82] be 10
[2791.82 → 2792.54] times faster
[2792.54 → 2793.08] than encoding
[2793.08 → 2793.40] JSON
[2793.40 → 2794.62] they probably
[2794.62 → 2795.12] ran their
[2795.12 → 2795.80] benchmarks a
[2795.80 → 2796.30] long time
[2796.30 → 2797.00] ago and that
[2797.00 → 2797.34] is probably
[2797.34 → 2797.72] more like
[2797.72 → 2798.24] four times
[2798.24 → 2798.76] faster by
[2798.76 → 2799.02] now
[2799.02 → 2800.06] interesting
[2800.06 → 2800.74] yeah
[2800.74 → 2802.04] and I
[2802.04 → 2802.46] definitely
[2802.46 → 2802.98] think that
[2802.98 → 2803.48] there's more
[2803.48 → 2803.96] work to be
[2803.96 → 2804.60] done but
[2804.60 → 2805.42] all the
[2805.42 → 2806.04] low-hanging fruit
[2806.04 → 2806.34] has been
[2806.34 → 2807.48] picked mostly
[2807.48 → 2808.14] by me and
[2808.14 → 2808.72] some others
[2808.72 → 2810.22] but there
[2810.22 → 2810.56] are some
[2810.56 → 2810.88] things that
[2810.88 → 2811.40] can still be
[2811.40 → 2812.28] done without
[2812.28 → 2813.10] changing the
[2813.10 → 2813.78] API or
[2813.78 → 2814.18] breaking the
[2814.18 → 2814.76] users and
[2814.76 → 2815.12] I think the
[2815.12 → 2815.74] the biggest one
[2815.74 → 2816.84] and that
[2816.84 → 2817.82] ties into
[2817.82 → 2818.84] the work that
[2818.84 → 2819.32] Dave has been
[2819.32 → 2820.66] doing is
[2820.66 → 2821.48] essentially
[2821.48 → 2822.30] rewriting the
[2822.30 → 2822.80] tokenizer
[2822.80 → 2824.38] so what takes
[2824.38 → 2824.90] in the bytes
[2824.90 → 2825.78] and says oh
[2825.78 → 2826.22] this is a
[2826.22 → 2826.92] string and
[2826.92 → 2827.40] then this is
[2827.40 → 2827.72] an open
[2827.72 → 2828.38] brace and
[2828.38 → 2828.74] then there's
[2828.74 → 2829.24] a comma and
[2829.24 → 2829.58] so on
[2829.58 → 2830.80] yeah and
[2830.80 → 2831.66] so that
[2831.66 → 2832.62] process than
[2832.62 → 2834.14] I mean does
[2834.14 → 2835.02] it builds the
[2835.02 → 2835.88] data structures
[2835.88 → 2837.04] as it goes
[2837.04 → 2837.56] when it's
[2837.56 → 2838.58] parsing or
[2838.58 → 2839.10] does it
[2839.10 → 2840.10] describe somehow
[2840.10 → 2840.84] that structure
[2840.84 → 2841.32] in some
[2841.32 → 2841.58] other
[2841.58 → 2842.36] intermediate
[2842.36 → 2843.86] data structure
[2843.86 → 2844.60] if that makes
[2844.60 → 2844.92] sense
[2844.92 → 2846.24] so one way
[2846.24 → 2846.72] to go about
[2846.72 → 2847.30] it would be
[2847.30 → 2847.92] indeed to
[2847.92 → 2848.30] build some
[2848.30 → 2848.60] sort of
[2848.60 → 2849.42] tree such
[2849.42 → 2849.74] as like
[2849.74 → 2850.02] when you
[2850.02 → 2850.54] parse a
[2850.54 → 2850.98] go file
[2850.98 → 2851.34] and you
[2851.34 → 2851.64] get a
[2851.64 → 2852.18] syntax tree
[2852.18 → 2852.60] of the
[2852.60 → 2853.32] go code
[2853.32 → 2853.94] yeah
[2853.94 → 2855.06] it doesn't
[2855.06 → 2855.40] do that
[2855.40 → 2855.70] what it
[2855.70 → 2856.46] does is
[2856.46 → 2856.96] it
[2856.96 → 2857.96] tokenizes
[2857.96 → 2859.10] a value
[2859.10 → 2859.88] for example
[2859.88 → 2860.22] a JSON
[2860.22 → 2860.48] object
[2860.48 → 2860.96] once
[2860.96 → 2861.86] so you
[2861.86 → 2862.22] know it
[2862.22 → 2863.12] starts going
[2863.12 → 2863.46] through the
[2863.46 → 2863.94] reader through
[2863.94 → 2864.36] the bytes
[2864.36 → 2865.16] and goes
[2865.16 → 2865.76] token
[2865.76 → 2866.22] token but
[2866.22 → 2866.72] it forgets
[2866.72 → 2867.56] them because
[2867.56 → 2867.94] there's the
[2867.94 → 2868.44] first pass
[2868.44 → 2869.22] it just wants
[2869.22 → 2869.66] to check if
[2869.66 → 2870.14] the JSON is
[2870.14 → 2870.38] valid
[2870.38 → 2871.54] and once
[2871.54 → 2871.88] it reaches
[2871.88 → 2872.30] the end
[2872.30 → 2872.78] for example
[2872.78 → 2873.46] the closing
[2873.46 → 2874.22] brace for
[2874.22 → 2874.64] the initial
[2874.64 → 2875.00] brace
[2875.00 → 2876.38] then it
[2876.38 → 2876.78] goes all
[2876.78 → 2876.96] the way
[2876.96 → 2877.26] back to
[2877.26 → 2877.56] the beginning
[2877.56 → 2877.86] of the
[2877.86 → 2878.52] buffer
[2878.52 → 2879.68] and then
[2879.68 → 2880.88] it tokenizes
[2880.88 → 2881.22] again
[2881.22 → 2882.14] but this
[2882.14 → 2882.58] time
[2882.58 → 2883.64] when it
[2883.64 → 2884.08] encounters
[2884.08 → 2884.66] for example
[2884.66 → 2885.48] open object
[2885.48 → 2886.06] then it
[2886.06 → 2886.42] actually
[2886.42 → 2888.02] goes and
[2888.02 → 2889.92] starts an
[2889.92 → 2890.34] object in
[2890.34 → 2890.86] the destination
[2890.86 → 2892.26] value
[2892.26 → 2892.98] and if it
[2892.98 → 2893.26] sees a
[2893.26 → 2893.76] string then
[2893.76 → 2894.42] it tries to
[2894.42 → 2894.96] decode that
[2894.96 → 2895.38] into whatever
[2895.38 → 2896.66] the current
[2896.66 → 2897.44] destination is
[2897.44 → 2898.22] and so
[2898.22 → 2898.44] on
[2898.44 → 2899.12] that's
[2899.12 → 2899.52] interesting
[2899.52 → 2900.14] I'm surprised
[2900.14 → 2900.48] it does
[2900.48 → 2900.78] that
[2900.78 → 2902.12] because you
[2902.12 → 2902.78] think it
[2902.78 → 2903.24] would just
[2903.24 → 2903.74] do it
[2903.74 → 2904.22] once
[2904.22 → 2906.00] why does
[2906.00 → 2906.54] it does it
[2906.54 → 2907.08] like that
[2907.08 → 2907.86] so the
[2907.86 → 2908.18] reason it
[2908.18 → 2908.44] does it
[2908.44 → 2909.22] twice is
[2909.22 → 2910.50] to prevent
[2910.50 → 2911.66] partial decodes
[2911.66 → 2912.48] so if I
[2912.48 → 2912.94] give you for
[2912.94 → 2913.84] example an
[2913.84 → 2914.58] array of
[2914.58 → 2915.44] 9000 elements
[2915.44 → 2916.22] and there's no
[2916.22 → 2916.90] closing token
[2916.90 → 2917.96] that is invalid
[2917.96 → 2918.26] JSON
[2918.26 → 2919.20] so what are
[2919.20 → 2919.46] you going to
[2919.46 → 2919.90] do are you
[2919.90 → 2920.44] going to spend
[2920.44 → 2921.14] all the time
[2921.14 → 2923.00] to decode all
[2923.00 → 2923.58] those 9000
[2923.58 → 2924.56] elements into
[2924.56 → 2925.32] your destination
[2925.32 → 2926.34] and probably
[2926.34 → 2926.92] mess with your
[2926.92 → 2927.76] destination data
[2927.76 → 2928.16] if you had
[2928.16 → 2928.58] anything there
[2928.58 → 2929.88] before which
[2929.88 → 2930.56] for an array
[2930.56 → 2930.98] doesn't make
[2930.98 → 2931.40] sense but
[2931.40 → 2932.06] imagine a map
[2932.06 → 2932.48] for example
[2932.48 → 2934.22] so you don't
[2934.22 → 2934.64] want to do
[2934.64 → 2935.32] that at least
[2935.32 → 2935.76] not in the
[2935.76 → 2936.36] JSON package
[2936.36 → 2937.34] it values
[2937.34 → 2938.04] correctness so
[2938.04 → 2938.94] it says no
[2938.94 → 2939.42] I'm first going
[2939.42 → 2939.76] to make sure
[2939.76 → 2940.42] that the JSON
[2940.42 → 2941.42] is valid and
[2941.42 → 2942.32] only after I'm
[2942.32 → 2943.88] going to decode
[2943.88 → 2945.62] very interesting
[2945.62 → 2947.62] and I think you
[2947.62 → 2948.22] could say it
[2948.22 → 2948.68] should keep a
[2948.68 → 2949.32] tree instead
[2949.32 → 2949.88] of keeping the
[2949.88 → 2951.06] bytes that might
[2951.06 → 2951.60] be a little bit
[2951.60 → 2952.30] more efficient in
[2952.30 → 2952.92] terms of not
[2952.92 → 2953.66] redoing work
[2953.66 → 2955.04] but I would
[2955.04 → 2955.38] say you
[2955.38 → 2956.10] probably are
[2956.10 → 2956.42] going to end
[2956.42 → 2957.40] up costing
[2957.40 → 2958.10] more in
[2958.10 → 2958.74] terms of
[2958.74 → 2959.38] allocating
[2959.38 → 2960.20] objects and
[2960.20 → 2960.58] so on
[2960.58 → 2961.78] I mean I
[2961.78 → 2962.60] just go
[2962.60 → 2963.06] through it
[2963.06 → 2963.70] once don't
[2963.70 → 2964.10] worry about
[2964.10 → 2965.02] correctness and
[2965.02 → 2965.84] yes do all
[2965.84 → 2966.50] the work and
[2966.50 → 2967.22] then if at the
[2967.22 → 2968.02] end it's wrong
[2968.02 → 2968.62] then you get
[2968.62 → 2969.50] the error but
[2969.50 → 2969.76] you have to
[2969.76 → 2970.38] wait for it
[2970.38 → 2971.02] maybe I
[2971.02 → 2971.46] feel like
[2971.46 → 2972.78] that's more of
[2972.78 → 2973.32] an optimistic
[2973.32 → 2974.26] thing is done
[2974.26 → 2974.60] you think that
[2974.60 → 2975.46] would be a bad
[2975.46 → 2976.60] design I'm
[2976.60 → 2977.74] not sure if I'm
[2977.74 → 2978.78] about 50-50 I
[2978.78 → 2979.66] think both use
[2979.66 → 2981.08] cases are valid I
[2981.08 → 2981.56] think the current
[2981.56 → 2982.68] API tries to be
[2982.68 → 2983.20] as simple as
[2983.20 → 2983.54] possible
[2983.66 → 2984.42] it essentially
[2984.42 → 2985.16] only has one
[2985.16 → 2986.74] entry point which
[2986.74 → 2987.34] is you know
[2987.34 → 2988.84] decoder. Decode and
[2988.84 → 2989.80] Marshall is just
[2989.80 → 2990.60] a wrapper for it
[2990.60 → 2991.46] because if you look
[2991.46 → 2992.32] at Marshall it just
[2992.32 → 2993.02] does the thing for
[2993.02 → 2994.04] you underneath
[2994.04 → 2995.10] oh it's not the
[2995.10 → 2995.92] other way around I
[2995.92 → 2997.20] thought the decoder
[2997.20 → 2997.74] would use
[2997.74 → 2998.48] you thought decoder
[2998.48 → 2999.26] used Marshall
[2999.26 → 3000.52] yeah or Marshall
[3000.52 → 3001.78] yeah so the nice
[3001.78 → 3002.16] thing about the
[3002.16 → 3003.00] decoder is that it
[3003.00 → 3004.26] keeps stuff to be
[3004.26 → 3005.86] reused later if it
[3005.86 → 3006.44] was the decoder
[3006.44 → 3007.84] using Marshall then
[3007.84 → 3008.82] Marshall doesn't have
[3008.82 → 3010.00] the decoder object to
[3010.00 → 3010.88] then reuse all that
[3010.88 → 3012.66] stuff right yeah I
[3012.66 → 3014.68] see huh oh yeah
[3014.68 → 3015.90] that's okay very
[3015.90 → 3016.82] cool very cool and
[3016.82 → 3017.60] of course this is all
[3017.60 → 3018.72] open source so if we
[3018.72 → 3019.88] want to really see how
[3019.88 → 3020.82] this works we can go
[3020.82 → 3021.96] and read the code
[3021.96 → 3023.34] yeah, but I would say
[3023.34 → 3024.88] probably don't look at
[3024.88 → 3025.52] that code and that
[3025.52 → 3026.34] API and assume that
[3026.34 → 3027.22] it's idiomatic to go
[3027.22 → 3028.38] because a lot of this
[3028.38 → 3029.42] was written you know
[3029.42 → 3030.42] over a decade ago
[3030.42 → 3032.58] and it's been you know
[3032.58 → 3034.12] my dirty fingers have
[3034.12 → 3035.08] been on it as well as
[3035.08 → 3035.80] many other people's
[3035.80 → 3036.68] fingers so it's its
[3036.68 → 3037.38] kind of like a zombie
[3037.38 → 3038.00] at this point
[3038.00 → 3039.24] that's actually a very
[3039.24 → 3040.18] good point you raise
[3040.18 → 3041.48] because a lot of
[3041.48 → 3042.54] times you know I
[3042.54 → 3043.38] think many of us in
[3043.38 → 3044.68] the community who
[3044.68 → 3045.36] have been around for
[3045.36 → 3046.34] a while basically tell
[3046.34 → 3047.28] tell new folks hey
[3047.28 → 3048.08] just go read the
[3048.08 → 3048.78] standard library and
[3048.78 → 3049.26] that's that's an
[3049.26 → 3050.76] excellent example you
[3050.76 → 3051.38] know of how to write
[3051.38 → 3052.96] go code right but
[3052.96 → 3054.34] that is not always
[3054.34 → 3055.96] true you know we've
[3055.96 → 3056.72] learned a lot since
[3056.72 → 3057.48] then you know some
[3057.48 → 3058.22] dos and don'ts and
[3058.22 → 3058.92] some best practices
[3058.92 → 3059.88] and you know as you
[3059.88 → 3060.62] as we say some
[3060.62 → 3061.42] idiomatic ways of
[3061.42 → 3062.88] doing things and
[3062.88 → 3064.12] yeah encoding JSON
[3064.12 → 3065.02] package is perhaps not
[3065.02 → 3067.08] the best representation of
[3067.08 → 3067.74] how far we've come
[3067.74 → 3068.76] yeah the other thing
[3068.76 → 3070.54] is it contains lots of
[3070.54 → 3071.82] optimizations and it
[3071.82 → 3073.52] should and that can
[3073.52 → 3074.32] that can come at a
[3074.32 → 3076.08] cost of code complexity
[3076.08 → 3077.44] and kind of ugliness
[3077.44 → 3079.10] but you don't mind
[3079.10 → 3080.02] it because it's such an
[3080.02 → 3081.62] important place to have
[3081.62 → 3083.40] that but yes a junior
[3083.40 → 3084.40] developer could go and
[3084.40 → 3085.26] look and see some
[3085.26 → 3085.88] things in there and
[3085.88 → 3086.98] think well this is how
[3086.98 → 3087.80] you do this and
[3087.80 → 3089.12] probably you wouldn't
[3089.12 → 3089.84] want to do it like
[3089.84 → 3091.30] that yeah I
[3091.30 → 3092.74] completely agree we
[3092.74 → 3094.58] definitely should not run
[3094.58 → 3096.08] out of time to
[3096.08 → 3097.28] present some unpopular
[3097.28 → 3097.98] opinions
[3097.98 → 3117.84] so my unpopular
[3117.84 → 3119.54] opinion is that
[3119.54 → 3121.74] encoding JSON is fast
[3121.74 → 3124.94] enough oh come on
[3124.94 → 3126.68] wow this is the guy
[3126.68 → 3127.72] responsible for making
[3127.72 → 3128.34] it faster
[3128.34 → 3132.16] well I'm going to say
[3132.16 → 3133.50] generally where it
[3133.50 → 3134.90] generally means it most
[3134.90 → 3136.22] most likely applies to
[3136.22 → 3137.54] you, but it might not
[3137.54 → 3138.46] apply to the one person
[3138.46 → 3139.26] that's doing something
[3139.26 → 3140.96] completely esoteric such
[3140.96 → 3142.86] as handling 20 gigabytes
[3142.86 → 3144.54] of JSON but most people
[3144.54 → 3147.00] don't do that and kind of
[3147.00 → 3148.12] my point goes back to the
[3148.12 → 3149.58] trade-offs right yes if you
[3149.58 → 3151.40] pick another package you
[3151.40 → 3153.28] can get maybe a 2x 3x
[3153.28 → 3154.74] maybe even 4x improvement
[3154.74 → 3157.04] but is it really worth
[3157.04 → 3158.28] sticking with JSON at that
[3158.28 → 3159.76] point the overlap between
[3159.76 → 3161.06] the people that are stuck
[3161.06 → 3162.58] with JSON because they are
[3162.58 → 3163.86] and the people that have to
[3163.86 → 3165.46] deal with a lot of data is
[3165.46 → 3166.60] very small because the
[3166.60 → 3167.48] people that have to deal
[3167.48 → 3169.00] with a lot of data they
[3169.00 → 3169.82] generally pick better
[3169.82 → 3171.00] formats that are
[3171.00 → 3172.86] faster to decode I think
[3172.86 → 3174.24] that is a pretty solid
[3174.24 → 3176.08] argument actually yeah
[3176.08 → 3177.10] that's not unpopular with
[3177.10 → 3178.20] me that one I think
[3178.20 → 3179.82] you've nailed that yeah
[3179.82 → 3181.22] yeah you would think
[3181.22 → 3181.76] that the amount of
[3181.76 → 3182.80] people yelling about
[3182.80 → 3183.92] encoding JSON being too
[3183.92 → 3184.74] slow would disagree
[3184.74 → 3187.92] sure well, but that's
[3187.92 → 3188.78] because we gave them the
[3188.78 → 3190.02] tools to benchmark things
[3190.02 → 3190.64] I don't know what you
[3190.64 → 3192.24] expect of course
[3192.24 → 3194.14] should take them back
[3194.14 → 3198.04] well Daniel thank you so
[3198.04 → 3200.04] much for coming on the
[3200.04 → 3201.00] show and spending some
[3201.00 → 3201.82] time with us, it's been
[3201.82 → 3202.86] great you must come back
[3202.86 → 3204.22] at some point it was a
[3204.22 → 3206.26] pleasure yeah, thank you
[3206.26 → 3206.98] very much thanks to
[3206.98 → 3207.62] everyone for listening
[3207.62 → 3209.26] and we'll see you next
[3209.26 → 3209.58] time
[3209.58 → 3215.16] hey have you followed us
[3215.16 → 3216.32] on Twitter yet you
[3216.32 → 3218.36] should we post live
[3218.36 → 3219.26] recording notifications
[3219.26 → 3221.08] clips and highlights from
[3221.08 → 3223.00] past episodes links and
[3223.00 → 3224.22] repos from around the go
[3224.22 → 3226.44] community and more follow
[3226.44 → 3227.56] along and join the
[3227.56 → 3228.94] conversation we are at
[3228.94 → 3231.96] go time FM this episode
[3231.96 → 3232.92] was hosted by Matt
[3232.92 → 3234.08] Refer with help from
[3234.08 → 3235.88] Johnny Portico it was
[3235.88 → 3236.64] produced by Jared
[3236.64 → 3238.56] Santo that's me and the
[3238.56 → 3239.90] music as always was
[3239.90 → 3240.52] provided by the
[3240.52 → 3241.60] mysterious Break master
[3241.60 → 3243.58] Cylinder we are brought
[3243.58 → 3244.42] to you by the amazing
[3244.42 → 3246.78] folks at Vastly Linde and
[3246.78 → 3249.08] Rollbar that's our show
[3249.08 → 3250.62] come back next week we're
[3250.62 → 3251.48] talking infrastructure
[3251.48 → 3266.14] here
[3266.14 → 3271.14] Changelog Plus
[3279.14 → 3281.14] Changelog Plus
[3290.14 → 3291.14] Change love Plus
[3296.14 → 3301.14] Change love Plus
[3310.14 → 3311.14] Change love Plus
[3323.14 → 3325.14] By the way, I found what the bug was.
[3325.14 → 3326.14] Oh, you did?
[3326.14 → 3331.14] Yeah. So if I look at my recording program, it keeps using more memory.
[3331.14 → 3334.14] But if I switch to a different window, it doesn't.
[3334.14 → 3335.14] It's like quantum.
[3335.14 → 3336.14] It stops climbing.
[3336.14 → 3337.14] Yeah.
[3337.14 → 3340.14] I think it's the UI. So the UI keeps showing the wavelength of my voice.
[3340.14 → 3341.14] Ah.
[3341.14 → 3344.14] And it's probably like keeping the entire UI in memory.
[3344.14 → 3346.14] And then if I look away, it stops rendering it.
[3346.14 → 3348.14] And then it stops using more memory.
[3348.14 → 3350.14] So only does it when you're looking at it.
[3350.14 → 3351.14] So don't look at it.
[3351.14 → 3355.14] I'm looking at it now, and it's climbing to 31, 32.
[3355.14 → 3357.14] And then I stop looking at it and it stops.
[3357.14 → 3358.14] The Heisenberg principle.
[3358.14 → 3360.14] It's like Schrödinger's cat.
[3360.14 → 3365.14] Yeah, Schrödinger's cat files.
[3365.14 → 3366.14] Oh man.
[3366.14 → 3372.14] It is. It's like once it's observed, it changes its behaviour.
[3372.14 → 3374.14] Oh, that's so weird.
[3374.14 → 3376.14] You'd never think to check that, would you?
[3376.14 → 3379.14] That's such a classic computer bug.
[3379.14 → 3381.14] That is exactly what happened.
[3381.14 → 3387.14] Obviously, when I did the five-second recording, I didn't, you know, it wasn't enough time to notice if the memory was coming.
[3387.14 → 3388.14] Mm-hmm.
[3388.14 → 3396.14] So you literally, if you minimize the window or have it on a different screen or something when it's not doing it, does the RAM jump back to where it was?
[3396.14 → 3397.14] No, it just stays.
[3397.14 → 3402.14] So, so in this, in this second section, I, it claimed all the way up to 30%.
[3402.14 → 3404.14] So I just minimize the window, and then it's just stayed there.
[3404.14 → 3405.14] Right.
[3405.14 → 3407.14] And you just thought, I just don't want to stress about this.
[3407.14 → 3408.14] I don't want to look at it.
[3408.14 → 3410.14] And then it works.
[3410.14 → 3411.14] And you found it.
[3411.14 → 3416.14] If you, if you saw me looking up, this was me checking the memory usage and praying that it wasn't about to crash.
[3416.14 → 3419.14] But again, I apologize for that.
[3419.14 → 3420.14] Oh, you found it.
[3420.14 → 3421.14] Wow.
[3421.14 → 3422.14] Excellent.
[3422.14 → 3425.14] Daniel, you, you must come back and debug more of our tech gremlins, please.
[3425.14 → 3426.14] Oh my God.
[3426.14 → 3427.14] Oh my God.
[3427.14 → 3428.14] Oh my God.
[3428.14 → 3429.14] No, no, please.
[3429.14 → 3431.14] This was very stressful.
[3431.14 → 3432.14] Thank you.
