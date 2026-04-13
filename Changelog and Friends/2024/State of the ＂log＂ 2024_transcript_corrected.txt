[0.00 → 2.66] Okay, last episode of the year.
[2.92 → 5.02] I'll just drop in that Friends theme.
[8.54 → 10.32] No, something's off.
[10.62 → 12.30] This is State of the Log.
[12.64 → 13.50] We have to go Classic.
[14.02 → 15.34] But where did I put that?
[19.62 → 21.44] Ah, there it is.
[30.00 → 44.74] Oh yes, it's late December once again.
[45.10 → 48.74] That classic Change Log theme song is bumpin'.
[48.74 → 53.38] And it is time for our 7th annual State of the Log episode.
[53.92 → 57.26] If this is your first time with us, welcome to the Change Log.
[57.26 → 62.50] We are the software world's best weekly news brief, deep technical interviews,
[62.96 → 67.40] and weekend talk show that feels like hanging out in the hallway of your favourite conference,
[67.64 → 68.36] only on repeat.
[68.74 → 75.46] Big thanks to our partners at fly.io for helping us bring you awesome developer pods all year long.
[75.76 → 79.94] You know we love Fly, the public cloud built for developers who ship.
[80.36 → 83.24] Give it a try at fly.io.
[83.90 → 85.62] Okay, let's do it.
[85.62 → 87.26] What's up, nerds?
[87.32 → 90.60] I'm here with Kurt Mickey, co-founder and CEO of Fly.
[90.98 → 92.04] You know we love Fly.
[92.54 → 95.22] So, Kurt, I want to talk to you about the magic of the cloud.
[95.86 → 96.64] You have thoughts on this, right?
[97.00 → 97.20] Right.
[97.54 → 100.18] I think it's valuable to understand the magic-minded cloud
[100.18 → 104.26] because you can build better features for users, basically, if you understand that.
[104.32 → 108.00] You can do a lot of stuff, particularly now that people are doing LLM stuff,
[108.00 → 111.18] but you can do a lot of stuff if you get that and can be creative with it.
[111.18 → 116.46] So, when you say clouds aren't magic because you're building a public cloud for developers
[116.46 → 120.72] and you go on to explain exactly how it works, what does that mean to you?
[121.00 → 123.32] In some ways, it means these all came from somewhere.
[123.56 → 127.36] Like, there was a simpler time before clouds where we'd get a server at Rack shack
[127.36 → 132.18] and we'd SSH or Telnet into it, even, and put files somewhere
[132.18 → 135.64] and run the web servers ourselves to serve them up to users.
[136.04 → 137.88] Clouds are not magic on top of that.
[137.94 → 140.52] They're just more complicated ways of doing those same things
[140.52 → 143.78] in a way that meets the needs of a lot of people instead of just one.
[143.96 → 146.12] One of the things I think that people miss out on,
[146.12 → 149.36] and a lot of this is actually because AWS and GCP
[149.36 → 152.38] have created such big black box abstractions.
[152.68 → 154.44] Like, Lambda is really black boxy.
[154.44 → 156.80] You can't, like, pick apart Lambda and see how it works from the outside.
[156.96 → 158.70] You have to sort of just use what's there.
[158.86 → 161.22] But the reality is, like, Lambda is not all that complicated.
[161.40 → 163.52] It's just a modern way to launch little VMs
[163.52 → 165.88] and serve some requests from them
[165.88 → 168.52] and let them, like, kind of pause and resume
[168.52 → 170.92] and free up, like, physical compute time.
[171.34 → 173.38] The interesting thing about understanding how clouds work
[173.38 → 175.84] is it lets you build kind of features for your users
[175.84 → 176.78] you never would have expected.
[177.00 → 179.46] And our canonical version of this for us is that, like,
[179.46 → 181.86] when we looked at how we wanted to isolate user code,
[181.86 → 184.54] we decided to just expose this machines concept,
[184.86 → 186.62] which is a much lower level abstraction than Lambda
[186.62 → 188.78] that you could use to build Lambda on top of.
[188.96 → 190.94] And what machines are is just these VMs
[190.94 → 193.48] that are designed to start really fast
[193.48 → 195.68] or designed to stop and then restart really fast
[195.68 → 198.20] or designed to suspend sort of like your laptop does
[198.20 → 201.04] when it closes and resume really fast when you tell them to.
[201.30 → 203.60] And what we found is that giving people those primitives
[203.60 → 205.68] is actually, there's, like, new apps being built
[205.68 → 207.02] that couldn't be built before,
[207.34 → 209.48] specifically because we went so low level
[209.48 → 212.54] and made such a minimal abstraction
[212.54 → 215.42] on top of generally, like, Linux kernel features.
[215.76 → 217.70] A lot of our platform is actually just exposing
[217.70 → 220.08] a nice UX around Linux kernel features,
[220.30 → 221.74] which I think is kind of interesting.
[221.74 → 223.08] But, like, you still need to understand
[223.08 → 225.04] what they're doing to get the most use out of them.
[225.42 → 225.76] Very cool.
[225.88 → 229.02] Okay, so experience the magic of Fly
[229.02 → 231.52] and get told the secrets of Fly
[231.52 → 233.06] because that's what they want you to do.
[233.18 → 234.28] They want to share all the secrets
[234.28 → 236.18] behind the magic of the Fly cloud,
[236.50 → 237.94] the cloud for productive developers,
[238.20 → 240.08] the cloud for developers who ship.
[240.40 → 243.58] Learn more and get started for free at fly.io.
[243.86 → 245.92] Again, fly.io.
[250.74 → 252.04] All right, man, here we are.
[252.22 → 254.58] State of the log.
[255.20 → 256.10] Can you believe it?
[256.38 → 257.50] I can't believe it.
[257.76 → 260.90] You know, I listened to last year's in prep for this one.
[261.34 → 261.66] You did?
[262.00 → 263.54] Yeah, I went to sleep to that last night.
[263.54 → 265.08] You might be more prepared than I am then
[265.08 → 265.76] because I did not do that.
[265.76 → 266.92] I wouldn't call that prepared, really.
[267.32 → 271.46] I, at first glance, as a consumer of podcasts,
[271.82 → 273.22] I looked at the chapter list
[273.22 → 278.94] and it was like voicemail, reaction to voicemail,
[279.04 → 280.34] voicemail, reaction to voicemail.
[280.84 → 281.28] Right.
[281.28 → 283.76] The chapters weren't really indicative of the content.
[283.76 → 284.54] That was okay.
[284.94 → 286.58] So it was a different vibe,
[286.72 → 290.10] but then also audibly a very different vibe.
[290.16 → 291.86] We did some list different last year, you know,
[291.90 → 293.72] and we're going to carry it through this year too.
[293.92 → 294.04] So.
[294.72 → 294.80] Right.
[295.00 → 295.56] We appreciate that.
[295.62 → 296.60] Well, we did some things different.
[296.74 → 297.96] We did other things the same.
[298.04 → 298.92] Listener voicemails.
[299.16 → 299.32] Yeah.
[300.02 → 301.24] Reactions to listener voicemails.
[301.30 → 302.84] That's been a thing for a few years now.
[303.06 → 304.46] And then picking our favourites,
[304.94 → 305.86] as we've always done that,
[306.36 → 308.68] only we're going to hold off our favourites to the end.
[308.68 → 311.24] Now, I'm just going to foreshadow a little bit.
[311.30 → 311.98] I'm going to say this.
[312.06 → 312.94] I think you're going to like this.
[313.14 → 313.42] Okay.
[313.86 → 315.46] I'm going to do something unprecedented.
[315.88 → 316.46] Oh gosh.
[316.58 → 317.40] When we get to our picks.
[317.88 → 318.24] Okay.
[318.54 → 319.86] You're going to have a list,
[320.00 → 321.48] an actual list that's longer than mine.
[321.66 → 323.10] This has never happened before
[323.10 → 325.00] and it may never happen again.
[325.18 → 325.52] Okay.
[325.68 → 327.00] So there's a little bit of a teaser.
[327.76 → 328.90] One thing I thought would be cool.
[329.16 → 330.50] I'm not sure if I like that, honestly.
[331.04 → 331.88] A little mini-game.
[332.18 → 332.42] Oh.
[332.62 → 334.40] Because our listeners are all going to pick
[334.40 → 337.20] their favourite episodes on their voicemails.
[337.20 → 338.88] And the question,
[338.98 → 339.96] and of course you have some prepared.
[340.04 → 340.82] How many did you pick?
[341.00 → 342.04] Just give me a number.
[342.68 → 343.20] What'd you bring?
[344.40 → 345.62] Of favourite episodes?
[345.92 → 346.38] Yeah, yeah.
[347.06 → 347.42] 15.
[348.28 → 348.64] What?
[351.26 → 351.62] Okay.
[351.78 → 352.10] 15.
[352.30 → 354.16] I'm joking because last year I said 11
[354.16 → 354.68] and I actually,
[354.88 → 356.10] so because I just listened back,
[356.18 → 357.12] I laughed at myself
[357.12 → 358.48] because you said,
[358.58 → 359.46] how many do you have?
[359.56 → 360.22] And I was like,
[360.60 → 361.50] dramatic pause.
[361.68 → 361.98] Right.
[362.16 → 362.48] 11.
[363.04 → 364.24] And it was a lot.
[364.24 → 365.16] You know, 11's a lot.
[365.48 → 365.82] Yeah, yeah, yeah.
[365.84 → 366.10] So I was like,
[366.12 → 367.12] I got to trump that number.
[367.40 → 367.72] 15.
[367.94 → 368.44] So 15.
[368.64 → 368.86] All right.
[368.92 → 369.94] So in honesty,
[369.94 → 371.56] I have five favourites,
[371.88 → 373.02] four honourable mentions,
[373.60 → 375.94] and then I picked my favourite titles.
[376.30 → 377.92] I have of that list,
[378.78 → 380.14] six best titles.
[380.56 → 381.04] Oh, man.
[381.08 → 381.76] So here's the mini-game.
[382.48 → 384.36] How many of our favourites
[384.36 → 385.40] are going to cross over
[385.40 → 386.18] with listener favourites?
[386.28 → 386.52] Meaning,
[386.66 → 388.44] if we were to scratch out our favourites
[388.44 → 389.38] each time they were mentioned
[389.38 → 390.44] by somebody else first,
[390.84 → 392.36] how many do you think
[392.36 → 393.44] we'll have at the end?
[393.98 → 395.38] How many unique to you
[395.38 → 396.38] and or me?
[397.10 → 397.68] Do your own.
[397.80 → 398.60] I'll do my own.
[398.96 → 399.98] I have five favourites
[399.98 → 401.00] and four honourable mentions.
[401.26 → 402.40] This number that we choose
[402.40 → 403.18] is a secret too.
[403.32 → 404.16] We're going to reveal it later.
[404.34 → 405.26] No, we're going to reveal it right now.
[405.32 → 405.76] It's a mini-game.
[405.84 → 406.42] We're going to guess
[406.42 → 407.54] and then we'll see if we're right.
[407.82 → 408.14] Okay.
[408.46 → 409.44] I will say
[409.44 → 410.86] all of them.
[411.12 → 411.72] All of them.
[411.84 → 412.70] So you have how many?
[412.84 → 413.82] I'm going 100%.
[413.82 → 414.80] 100% crossover
[414.80 → 416.24] or 100% unique?
[416.84 → 417.56] Truth be told,
[417.62 → 418.58] I'm still making my list.
[419.38 → 419.74] Okay.
[420.44 → 421.26] Truth be told,
[421.56 → 422.64] I'm still making my list.
[422.74 → 424.32] So you're not repaired at all.
[424.40 → 424.66] Okay.
[424.74 → 425.80] So we can't play this game
[425.80 → 427.02] because your list changes
[427.02 → 427.78] throughout the show.
[427.88 → 428.32] Is that what's happening?
[428.32 → 428.70] That's true.
[428.78 → 429.38] I can cheat.
[429.54 → 429.82] Okay.
[429.88 → 430.40] I can cheat.
[430.92 → 431.20] You know,
[431.20 → 431.80] the problem is
[431.80 → 433.12] there's just so many good ones.
[433.52 → 434.88] So I started making a list
[434.88 → 435.24] and I was like,
[435.62 → 436.02] okay,
[436.04 → 436.68] that was a good one.
[436.88 → 437.10] Okay,
[437.12 → 437.80] that was a good one.
[437.80 → 438.20] Okay,
[438.22 → 438.90] that was a good one.
[439.28 → 439.44] Right.
[439.84 → 441.66] And I just had a really hard time
[441.66 → 443.02] making an actual list this year
[443.02 → 443.98] because like,
[444.06 → 445.16] there's a lot of good stuff.
[445.56 → 445.80] All right.
[445.84 → 446.00] Well,
[446.08 → 446.90] minigame cancelled
[446.90 → 447.96] because your list changes
[447.96 → 448.40] throughout the show.
[448.50 → 448.90] Fair enough.
[449.36 → 450.26] There were a lot.
[450.32 → 450.68] And in fact,
[450.70 → 452.02] I did a sequel query.
[452.64 → 454.04] I think we have 101 episodes
[454.04 → 454.70] to pick from
[454.70 → 456.48] between interviews and friends.
[456.74 → 457.14] Yes.
[457.34 → 457.70] So,
[457.82 → 458.20] I mean,
[458.92 → 460.06] it's tough to pick five
[460.06 → 460.78] out of 101
[460.78 → 462.78] or even 15.
[463.18 → 464.14] But let's get into it,
[464.16 → 464.44] shall we?
[464.86 → 465.42] Let's do it.
[465.90 → 466.34] All right.
[467.00 → 467.40] Listener,
[467.40 → 468.10] voicemails.
[468.18 → 468.90] Thank you so much
[468.90 → 470.14] to our listeners.
[470.30 → 471.78] We have the coolest community,
[471.90 → 472.66] even BMC
[472.66 → 474.08] just this morning
[474.08 → 474.62] was saying,
[474.86 → 477.08] let me see if I can quote BMC.
[478.34 → 479.28] Break massive cylinder.
[479.28 → 482.96] I was thanking BMC
[482.96 → 484.08] for making all these remixes
[484.08 → 485.76] and telling them
[485.76 → 486.92] it makes this episode
[486.92 → 487.94] extra special for us
[487.94 → 488.68] and our listeners.
[489.24 → 490.30] And BMC said,
[490.36 → 490.94] I really like it.
[491.00 → 492.06] You got a whole community
[492.06 → 492.94] thing going on,
[493.30 → 495.34] which is kind of how BMC types.
[495.70 → 496.44] And that's true.
[496.54 → 497.88] We have a cool community
[497.88 → 498.62] thing going on
[498.62 → 500.74] and we appreciate that.
[500.80 → 502.44] It makes not just this episode
[502.44 → 503.16] awesome,
[503.32 → 505.20] but really what we do awesome.
[505.42 → 505.64] So,
[505.72 → 506.34] thank you to everybody
[506.34 → 506.80] who called in.
[506.84 → 508.02] We have 12 voicemails,
[508.24 → 509.04] same as last year.
[509.94 → 511.88] And we have one person
[511.88 → 512.68] who sent theirs in
[512.68 → 513.54] at the last minute.
[513.64 → 514.76] And if you listen to last year's,
[515.58 → 516.26] you already know
[516.26 → 516.96] who that person is.
[517.02 → 517.90] We'll save them to the end
[517.90 → 518.20] because,
[518.30 → 518.52] you know,
[519.14 → 519.80] they deserve it.
[519.90 → 520.12] So,
[520.52 → 522.60] let's get straight into it.
[522.64 → 523.96] Our first caller
[523.96 → 524.84] in
[524.84 → 525.50] is
[525.50 → 527.04] AJ Kerrigan.
[527.18 → 527.36] Ooh.
[527.36 → 527.84] Hi,
[527.92 → 528.36] Adam.
[528.44 → 528.62] Hi,
[528.68 → 529.02] Jared.
[529.12 → 530.30] It's some other random
[530.30 → 531.48] named AJ Kerrigan.
[531.72 → 532.76] There was a bit of a theme
[532.76 → 533.50] to some of my favourite
[533.50 → 534.22] episodes this year.
[534.38 → 535.04] They talked about
[535.04 → 535.64] taking control
[535.64 → 536.32] of your own workspace,
[536.50 → 536.82] your tools,
[536.92 → 537.36] your environment,
[537.52 → 537.98] and thinking through
[537.98 → 538.88] what's important to you.
[539.02 → 539.64] And that could be
[539.64 → 540.78] starting at the hardware level,
[540.84 → 541.42] the lowest level.
[541.54 → 542.74] The interview with Kyle
[542.74 → 543.52] from fixity
[543.52 → 545.96] or with Perez from USA
[545.96 → 546.68] about customizable
[546.68 → 547.64] ergonomic keyboards.
[547.82 → 548.96] That's building a solid base.
[549.34 → 550.74] And then moving up
[550.74 → 552.20] the stack to the OS,
[552.70 → 553.82] the Linux Dischars episode
[553.82 → 554.82] with George Castro
[554.82 → 555.46] on Ship It
[555.46 → 557.00] was another fantastic one.
[557.00 → 558.36] And what a lot of
[558.36 → 559.22] my favourite episodes
[559.22 → 559.80] this year had
[559.80 → 561.14] was some great Zulip chat.
[561.34 → 562.34] Moving to Zulip,
[562.44 → 563.62] the episode about Zulip,
[563.76 → 564.86] and then also seeing
[564.86 → 566.00] the Change Law community
[566.00 → 566.72] move to Zulip
[566.72 → 568.78] was a great experience.
[568.94 → 569.52] As a listener,
[569.60 → 570.34] it's definitely much easier
[570.34 → 571.74] to keep track of chats now.
[571.96 → 572.72] And I love it.
[572.78 → 573.38] Seeing the engagement
[573.38 → 574.30] from the Zulip team,
[574.52 → 575.30] hearing that hard P
[575.30 → 575.78] from Adam
[575.78 → 576.80] that now I've started doing.
[576.98 → 577.32] Zulip.
[577.62 → 579.14] So thanks for another great year.
[579.64 → 580.88] I got a remix last year,
[580.96 → 582.50], so please do not bother
[582.50 → 583.44] including me this year.
[583.54 → 584.20] I just wanted to get
[584.20 → 585.30] some voice out to you all
[585.30 → 586.18] and say well done.
[586.18 → 587.36] I appreciate what you're doing.
[587.64 → 589.10] I like being a
[589.10 → 589.38] Change Law
[589.38 → 590.08] subscriber,
[590.54 → 591.48] and I don't see that changing.
[591.80 → 593.06] And I'll see you all
[593.06 → 594.44] in Zulip going forward.
[594.68 → 594.96] Thanks.
[595.32 → 595.64] Zulip.
[596.10 → 596.74] Good job, AJ.
[596.92 → 597.56] I like that.
[597.88 → 598.46] Oh, man.
[599.28 → 600.10] Zulip for the win.
[600.58 → 601.10] Mm-hmm.
[601.34 → 602.02] Zulip for the win.
[602.26 → 602.80] For the win.
[603.28 → 604.26] Remix is for the win,
[604.34 → 605.82] so we appreciate you saying
[605.82 → 606.72] don't remix this,
[606.84 → 607.44] but you know
[607.44 → 608.50] we don't take orders
[608.50 → 609.16] around here, AJ,
[609.26 → 609.86] and we do what we want.
[609.92 → 610.34] It's like saying
[610.34 → 611.24] when you edit that out,
[611.40 → 612.34] you're going to leave it in.
[612.34 → 613.06] Yeah, exactly.
[613.24 → 613.82] It's like Matt Refer
[613.82 → 614.66] saying edit that out.
[615.16 → 616.10] You're getting a remix.
[616.34 → 617.02] Gosh darn it.
[617.50 → 618.94] But yeah, okay,
[619.04 → 620.68] so you have a moving list
[620.68 → 621.96] of episodes,
[622.08 → 622.64] but I'm guessing
[622.64 → 623.56] I fix it,
[623.94 → 624.94] we have a right to repair.
[625.04 → 625.90] That had to be on your list,
[625.94 → 626.30] right, Adam?
[626.46 → 627.08] It was.
[627.22 → 628.38] Actually, both of those were.
[628.80 → 629.92] Open Source Thread Chat,
[630.46 → 631.70] Team Chat was on my list.
[631.78 → 632.96] Yeah, so far,
[633.38 → 635.42] 100% of AJ's picks
[635.42 → 636.74] are at least your pick.
[636.80 → 637.72] I also had one of those,
[637.72 → 640.60] so we may not have anything left
[640.60 → 641.48] at the end.
[642.12 → 643.06] And if you know the reference,
[643.22 → 643.38] Adam,
[643.92 → 644.64] some other random,
[644.78 → 645.64] AJ was referencing
[645.64 → 648.16] our secondary theme song,
[648.40 → 649.54] our alt theme song,
[649.88 → 650.62] which is called
[650.62 → 652.56] Your Favourite Ever Show.
[653.12 → 653.48] Yes.
[653.74 → 655.88] And BMC took that reference
[655.88 → 656.54] and ran with it.
[656.66 → 658.82] Here is AJ Kerrigan's
[658.82 → 659.48] BMC remix.
[660.76 → 661.96] Finally, it's time
[661.96 → 663.72] for change-logging friends
[663.72 → 665.26] with Adam and Jay.
[665.92 → 667.28] I don't like that theme,
[667.28 → 668.48] and I don't see that changing,
[668.82 → 670.24] so I have to fix it
[670.24 → 671.64] starting at the lowest level.
[673.34 → 674.66] That's building a solid bass.
[674.90 → 675.90] Adam and Jared
[675.90 → 677.22] it's a mother random,
[677.76 → 678.72] random, random,
[678.86 → 679.68] do, do, do, do, do.
[680.30 → 681.60] This is how we party.
[682.22 → 683.44] Another fantastic remix
[683.44 → 685.82] by AJ Kerrigan.
[686.76 → 687.22] So dope.
[688.98 → 690.80] Oh, and the late,
[690.82 → 691.82] is that a vuvuzela?
[692.06 → 692.86] The late siren.
[693.64 → 694.36] You know,
[695.10 → 696.84] having heard that remix,
[696.84 → 697.50] I have to say
[697.50 → 699.04] that I have purposefully
[699.04 → 700.58] behind the scenes
[700.58 → 701.80] not listened
[701.80 → 703.02] to any of these.
[703.90 → 705.22] So that I can have
[705.22 → 706.30] at the moment,
[706.40 → 707.08] I know you have,
[707.12 → 707.62] and I thank you
[707.62 → 708.80] for doing all the prep of this,
[708.90 → 709.02] you know,
[709.04 → 710.58] all that behind the scenes
[710.58 → 711.26] love,
[711.78 → 712.24] care,
[712.42 → 712.82] attention,
[712.82 → 714.68] so that I don't have to
[714.68 → 715.84] burst the bubble for myself.
[715.84 → 716.98] I can live at the moment
[716.98 → 717.86] in this podcast,
[718.00 → 718.72] so I appreciate that.
[718.72 → 719.20] That's right.
[719.28 → 719.98] You sit back,
[720.12 → 720.56] relax,
[720.66 → 721.30] and enjoy.
[721.68 → 722.04] Yes.
[722.04 → 722.98] As Break master,
[723.06 → 723.36] cylinder,
[723.62 → 725.34] and I toiled over these,
[725.60 → 727.30] although I did very little work,
[727.58 → 729.64] just criticism as we went,
[730.26 → 731.44] and handing off of files
[731.44 → 732.04] and stuff like that.
[732.06 → 732.62] Well, you had to create
[732.62 → 733.34] a type form,
[733.44 → 734.96] you had to promote it
[734.96 → 735.74] here and there,
[735.80 → 736.82] you had to talk to people
[736.82 → 737.48] and Zulip.
[737.62 → 738.38] Oh, that's true.
[738.62 → 738.88] You know,
[738.94 → 741.20] that's so much extra work involved.
[741.38 → 741.42] Okay.
[741.42 → 742.22] I mean, it is work, though.
[742.38 → 745.22] It's the nurturing process
[745.22 → 746.06] of the things.
[746.20 → 746.56] Yes.
[747.08 → 747.46] All right.
[747.52 → 747.94] Thanks, AJ.
[748.26 → 749.20] That is awesome.
[749.42 → 750.74] Next listener,
[751.26 → 752.08] somebody new,
[752.38 → 754.88] lots of familiar voices and names,
[755.08 → 758.14] but we have a new listener here
[758.14 → 759.40] calling in.
[760.04 → 760.32] Arno,
[760.42 → 760.62] now,
[760.74 → 761.58] you mentioned the type form.
[761.68 → 764.34] I do ask for pronunciation help,
[765.20 → 767.44] and this fellow's name is,
[767.44 → 768.08] I believe,
[768.38 → 768.82] Arno,
[769.06 → 771.60] but his last name is
[771.60 → 775.00] V-O-U-T-I-L-A-I-N-E-N.
[776.06 → 776.42] Utilizing?
[777.44 → 777.80] Utility?
[778.20 → 778.48] Vutilinian?
[778.76 → 779.38] I don't know.
[779.64 → 780.64] I don't know how to say it.
[781.64 → 783.28] And under the pronunciation help,
[783.38 → 783.80] he wrote
[783.80 → 785.12] E,
[785.26 → 786.06] as in enter,
[786.56 → 788.06] but I'm fine with any pronunciation.
[788.34 → 789.80] So he gave us help on the first name,
[790.22 → 790.58] Arno.
[791.22 → 791.90] Well, come on, man.
[792.00 → 792.72] I can't pronounce
[792.72 → 794.22] Vutilinian.
[795.46 → 796.52] Let's hear from Arno.
[796.94 → 798.18] Dear Adam and Jared,
[798.86 → 799.58] greetings from
[799.58 → 800.98] all the way from Finland,
[801.52 → 803.76] the land of the happiest people on planet,
[803.84 → 804.56] as you might know.
[804.78 → 806.42] Just to clearly meet up front,
[806.42 → 808.22] I think the reason for our happiness
[808.22 → 809.50] is just the fact that
[809.50 → 812.28] everyone must be listening to the changelog,
[812.50 → 812.90] obviously.
[813.50 → 815.18] Or maybe it's just me, and I'm weird,
[815.30 → 816.82] but honestly and sincerely,
[816.82 → 817.76] I love what you do.
[817.84 → 819.90] I've been listening for a few years already,
[820.02 → 821.72] so I decided it's about time
[821.72 → 823.04] to give you a personal hello
[823.04 → 824.20] and some cheers.
[824.20 → 826.74] And what was the kicker for me to reach out
[826.74 → 829.02] was the very first episode of the year
[829.02 → 831.22] where you dropped in the new beats.
[831.82 → 832.20] Honestly,
[832.30 → 833.62] I was shocked
[833.62 → 834.74] and I almost had to cry.
[834.92 → 836.30] They were so good,
[836.62 → 838.10] as Adam likes to put it.
[838.40 → 838.80] So gold.
[839.34 → 840.24] So back then in January,
[840.24 → 841.70] I also decided to see
[841.70 → 843.30] if the famous regency bias
[843.30 → 843.96] is a thing
[843.96 → 844.94] what Jared wondered
[844.94 → 846.28] on the last state of the log.
[846.28 → 848.22] And my conclusion for the year
[848.22 → 850.38] is that if it is regency bias,
[850.58 → 852.62] I'm also susceptible to it.
[852.90 → 853.84] Or you by chance
[853.84 → 855.42] happen to put out the best content
[855.42 → 856.44] towards the end of the year.
[856.74 → 857.50] So who knows?
[858.14 → 859.78] So a few highlights for me this year,
[859.88 → 861.14] in addition to the beats,
[861.36 → 863.26] were the reappearance of Cameron Say
[863.26 → 864.34] and changelog and friends,
[864.50 → 865.66] episode 36.
[866.16 → 866.56] By the way,
[866.60 → 868.44] I love the changelog and friends format.
[868.78 → 869.50] Please keep on coming.
[869.88 → 871.00] Then we got Matt Refer
[871.00 → 872.10] sing it if you know it.
[872.10 → 874.20] A modern classic.
[874.80 → 876.38] Almost choked on my coffee
[876.38 → 877.14] while listening to that
[877.14 → 877.90] for the first time.
[878.42 → 879.36] And finally,
[879.54 → 880.78] two tickets for departure.
[881.02 → 883.24] Changelog interviews 618.
[883.72 → 884.32] So thanks to you,
[884.36 → 886.12] I'm now a happy departure mono user
[886.12 → 887.30] on my terminal
[887.30 → 888.80] and I'm loving it.
[889.24 → 890.40] And I could, of course,
[890.48 → 892.14] include all the Kaiden episodes,
[892.40 → 893.96] the never-ending typescript
[893.96 → 896.26] arm wrestles between Jared and Nick,
[896.82 → 898.92] all of Adam's home-loving goodness,
[899.54 → 900.56] the Dan Tans
[900.56 → 901.08] and the
[901.08 → 902.28] well, you get the point.
[902.54 → 903.44] So thank you so much
[903.44 → 904.10] for what you do.
[904.28 → 906.26] You have indeed befriended me
[906.26 → 907.86] and I'm here to stay.
[908.20 → 909.56] Happy holiday season to you all
[909.56 → 910.60] and all the success
[910.60 → 911.88] on those pipe dreams
[911.88 → 913.10] for 2025.
[914.10 → 914.80] Thank you, Arno.
[914.92 → 915.28] That's a
[915.46 → 915.60] wow.
[916.30 → 916.86] Dan Tan.
[917.00 → 917.92] That's like a deep cut now.
[918.04 → 918.90] I was going to say that.
[918.96 → 919.60] My gosh.
[919.74 → 920.42] I was being quiet.
[920.50 → 921.98] I was going to come in right away
[921.98 → 923.28] and just say there was
[923.28 → 924.32] so many deep cuts there.
[924.36 → 924.68] Yeah.
[924.80 → 925.10] You know,
[925.30 → 926.00] really there were.
[926.34 → 927.44] From Dan Tan
[927.44 → 928.54] to the home-lab stuff
[928.54 → 930.68] to just all the details, man.
[930.68 → 930.88] Yeah.
[931.48 → 932.12] That's cool.
[932.68 → 933.68] And some good picks as well.
[933.80 → 936.12] Cameron says return to the pod.
[936.26 → 937.20] So many good picks.
[937.64 → 939.20] Two tickets for departure.
[939.84 → 941.96] We have a departure mono convert.
[942.22 → 944.58] I'm not using mono in my terminal.
[944.76 → 945.42] I tried it
[945.42 → 946.68] and I've determined,
[946.84 → 947.60] maybe I shared this already,
[947.70 → 949.74] I determined that I don't like pixel fonts
[949.74 → 951.96] at the terminal level.
[951.96 → 952.58] Mm-hmm.
[952.58 → 953.50] I like it in the editor more
[953.50 → 954.52] but for something about it in the terminal
[954.52 → 956.46] it just looks a little too pixelated.
[956.60 → 957.36] Mm-hmm.
[957.54 → 958.98] I'm over here on JetBrains Mono
[958.98 → 959.54] at this point
[959.54 → 961.62] but that conversation
[961.62 → 963.74] actually got me to re-evaluate
[963.74 → 966.92] my mono space font of choices
[966.92 → 968.92] and codingfont.com
[968.92 → 970.72] which I put in news
[970.72 → 971.94] and we were all playing with it.
[972.02 → 973.26] A lot of people chatting in Zulip
[973.26 → 975.14] were playing with that website.
[975.24 → 975.70] Very cool.
[975.82 → 976.40] It's like a
[976.98 → 977.82] not a hot or not
[977.82 → 978.54] but what's the
[978.54 → 980.08] hot or not
[980.08 → 981.56] like a royal rumble of fonts
[981.56 → 982.28] you know where you
[982.28 → 982.64] sure
[982.64 → 984.10] you put two fonts against each other
[984.10 → 985.70] and then it swaps in another one
[985.70 → 986.48] and you just keep picking,
[986.60 → 987.58] picking the Pepsi challenge
[987.58 → 988.42] so to speak.
[988.56 → 988.78] Yeah.
[988.90 → 989.70] And you can determine
[989.70 → 991.34] without knowing the names of the fonts
[991.34 → 992.74] and the stories
[992.74 → 994.24] which one you actually like the best
[994.24 → 995.08] and that one landed me
[995.08 → 996.02] on JetBrains Mono
[996.02 → 997.80] but I don't think,
[997.88 → 998.56] it's not comprehensive
[998.56 → 999.46] like Departure Mono
[999.46 → 1000.62] is not on there for instance
[1000.62 → 1002.10] or at least it didn't come up in mine.
[1002.30 → 1002.68] Anyway,
[1003.70 → 1004.46] should we hear
[1004.46 → 1005.34] Arno's remix?
[1006.10 → 1007.32] I would like to.
[1008.54 → 1012.38] Dear Adam and Jared,
[1013.02 → 1014.24] Greetings from Finland,
[1015.56 → 1017.84] the land of the happiest people on planet.
[1019.84 → 1020.72] Thus you might know
[1020.72 → 1022.12] the reason for our happiness
[1022.12 → 1023.34] is just the fact that
[1023.34 → 1025.94] everyone must listen to the new beats,
[1026.24 → 1026.62] obviously.
[1028.38 → 1029.56] They were so good.
[1030.66 → 1031.32] So good.
[1033.44 → 1034.78] Sing it if you know it.
[1038.54 → 1039.80] Finland, Finland, Finland.
[1040.82 → 1042.98] Finland, Finland, Finland.
[1042.98 → 1043.48] Finland, Finland, Finland.
[1043.88 → 1045.74] Finland, Finland, Finland.
[1046.38 → 1047.88] Finland, Finland, Finland.
[1048.00 → 1049.34] Finland, Finland, Finland.
[1049.82 → 1051.58] Finland, Finland, Finland.
[1052.24 → 1053.34] Finland, Finland.
[1053.34 → 1054.66] Nations, Finland, Finland.
[1054.66 → 1060.60] It almost sounds like you're saying for Linda.
[1060.98 → 1063.12] For Linda, for Linda, for Linda, for Linda.
[1063.52 → 1066.02] That could be like a new Finland anthem, you know,
[1066.06 → 1067.88] like maybe if they need a new national anthem,
[1068.00 → 1069.54] we could submit that one, perhaps.
[1070.04 → 1072.58] I think a theme will hit this year with the remixes,
[1072.68 → 1074.18] at least that I know that you don't know
[1074.18 → 1075.74] because I've been listening to them as we go.
[1076.20 → 1077.86] I think BMC has some new toys.
[1078.22 → 1078.76] You think so?
[1079.14 → 1079.52] Yes.
[1079.66 → 1080.82] Like AI?
[1080.82 → 1081.02] AI?
[1081.42 → 1083.82] Like some, there are more noises
[1084.38 → 1088.06] that don't come from the words of our actual listeners this year.
[1088.22 → 1090.08] I think BMC is playing, like the Finland,
[1090.16 → 1091.82] like that was not Arno.
[1092.56 → 1093.38] Or was it?
[1093.52 → 1094.62] You know, it might be actually.
[1094.76 → 1095.04] I don't know.
[1095.04 → 1095.72] I don't think so.
[1095.80 → 1097.06] I mean, you could really push the voice.
[1097.50 → 1097.76] Yeah.
[1098.18 → 1101.90] Maybe just taking Arno's voice and then just like really.
[1102.28 → 1103.04] Stretching it.
[1103.24 → 1103.80] And then.
[1104.66 → 1105.78] Harmonics, timing.
[1106.00 → 1107.14] Yeah, maybe, maybe, maybe.
[1107.32 → 1107.86] It's possible.
[1108.06 → 1108.60] We'll have to see.
[1108.60 → 1111.90] We'll have to get Break master Cylinder on the pod in the new year.
[1112.38 → 1112.74] That's easy.
[1112.88 → 1114.64] And discuss some stuff because that's what we did last year.
[1114.82 → 1116.54] Well, we'll probably have a new album next year.
[1116.60 → 1117.38] So that is breaking news.
[1117.46 → 1118.86] We have been working on our fourth.
[1119.32 → 1125.02] You call it a studio album when the studio is Break master Cylinder's studio by himself.
[1125.26 → 1125.72] I don't know.
[1125.84 → 1126.90] It's a new studio album.
[1127.48 → 1129.46] Our fourth, Changelog Beats.
[1129.84 → 1131.86] And it'll be coming out next year.
[1132.52 → 1133.58] So, teaser.
[1134.24 → 1136.90] And we'll certainly get BMC on after that one drops, right?
[1137.30 → 1137.66] Mm-hmm.
[1137.66 → 1138.58] All right.
[1138.66 → 1140.68] Listener voicemail number three.
[1141.34 → 1144.00] This is Don McKinnon.
[1144.58 → 1146.72] Hey, Jared, Adam, and everyone at Changelog.
[1147.16 → 1154.42] My favourite episode of 2024 was the Changelog and Friends episode from Chef to System Initiative.
[1154.76 → 1158.62] I've been following Adam Jacob on social media for a while, and he's always a great guest.
[1158.76 → 1163.94] So it was interesting to hear more about his career journey that led him to where he is now with his new company.
[1163.94 → 1168.48] And I did have to go back and watch any given Sunday after hearing that episode.
[1168.80 → 1169.64] I'd never seen it before.
[1169.90 → 1173.86] I also got a kick out of the Rails is having a moment again episode.
[1174.08 → 1179.40] A lot of times I disagree with DHH, but regardless, he is always entertaining to listen to.
[1179.72 → 1181.80] Thank you for all the work you guys do on the podcast.
[1181.94 → 1182.80] It's one of my favourites.
[1182.80 → 1183.80] See?
[1184.40 → 1185.64] These are all on my list, Jared.
[1186.64 → 1187.00] Okay.
[1187.38 → 1187.84] So you're bad.
[1187.94 → 1188.40] So you are.
[1188.54 → 1189.12] Maybe you're right.
[1189.18 → 1189.82] A hundred percent.
[1190.08 → 1192.16] We can just skip your section altogether at the end.
[1192.26 → 1192.46] Yeah.
[1192.50 → 1193.18] Maybe we could.
[1193.26 → 1194.88] I'd just be like, just listen to the show.
[1195.14 → 1195.46] That kind of thing.
[1195.46 → 1195.54] Right.
[1195.54 → 1196.70] But that was a good show.
[1196.80 → 1199.72] Like, I really wanted to do that show for a very long time.
[1199.92 → 1200.64] The Adam Jacobs show.
[1200.84 → 1201.16] Yes.
[1201.40 → 1201.64] Yes.
[1201.70 → 1201.98] Yes.
[1202.10 → 1208.32] Every time we had Adam on the podcast, I found myself biting my tongue to go into those depths,
[1208.50 → 1208.80] you know?
[1209.12 → 1209.34] Yeah.
[1209.40 → 1212.24] Because it wasn't the point of the show, but I had curiosities.
[1212.70 → 1216.46] And I figured, well, I'll just be patient because eventually we'll get that time.
[1216.54 → 1220.24] I guess the only sad thing is that it ended up on Change Login and Friends.
[1220.36 → 1220.58] Right.
[1220.58 → 1221.78] It was more of an interview.
[1222.16 → 1223.64] So I kind of broke the system.
[1223.64 → 1224.04] Yeah.
[1224.10 → 1227.44] You even called it a different kind of Friends episode at the opener.
[1227.58 → 1230.28] I'm like, the kind of Friends' episode that's actually an interview?
[1230.78 → 1230.94] Yeah.
[1230.98 → 1231.70] Well, you know.
[1231.78 → 1233.06] Sometimes you got to blur your lines, you know?
[1233.18 → 1234.00] You have to.
[1234.16 → 1240.74] And I think that what I've learned from talking to listeners over the years is that their lines
[1240.74 → 1244.82] are very blurred for them, so much so that they don't know the difference half the time.
[1245.18 → 1249.42] So it's probably more on us, although Don sure noticed where it landed.
[1249.94 → 1251.16] I liked that episode a lot, too.
[1251.16 → 1254.30] Obviously, I wasn't there, so I got to listen to it as a listener would.
[1254.40 → 1258.12] And I just loved some of the stories that came out, especially around the high school
[1258.12 → 1260.78] dropout move, you know, the loophole.
[1261.62 → 1266.76] And some of the stuff early on in his career were fascinating to me.
[1266.90 → 1268.36] So good choice.
[1268.42 → 1270.30] And of course, DHH always delivers.
[1270.30 → 1273.90] And so that was a good episode as well.
[1274.36 → 1278.28] I don't want to call this out necessarily to try to embarrass Adam.
[1278.78 → 1282.96] But did you, do you recall the part in the show where he almost cried?
[1283.54 → 1283.84] No.
[1284.16 → 1288.80] It was the first time I ever interview history or career, whatever you want to call it,
[1289.24 → 1291.26] where I've actually gotten somebody.
[1291.96 → 1293.38] I don't even want to say it like that.
[1293.44 → 1294.02] It's not cool.
[1294.38 → 1294.60] Right.
[1294.60 → 1296.24] You're not getting them to it like you're trying.
[1296.34 → 1297.42] Yeah, I'm not trying to do that.
[1297.50 → 1299.74] It's just I don't necessarily want to make him cry.
[1299.94 → 1300.48] Let's just say.
[1301.06 → 1304.00] But I do want to hear the good stuff.
[1304.50 → 1310.60] And he was sharing this really raw, emotional part of the chef history when he had to go
[1310.60 → 1317.38] out and in quotes or a version of quotes, paraphrase, command the troops, get them excited.
[1317.38 → 1323.30] And he just shared how he went back afterwards into his office and wept.
[1323.84 → 1329.10] And in the moment of sharing that story with me, he's like, I'm like getting emotional, he says, you know,
[1329.40 → 1333.62] and I'm there visually, which is why I'm desperately wanting this video version of our show,
[1333.66 → 1335.02] because there's there are things you miss.
[1335.52 → 1335.56] Sure.
[1335.70 → 1340.50] And as a listener of that show, you only hear the audio as a person who's there at the moment.
[1340.92 → 1345.82] We had to take a quick pause because he was getting he's getting emotional.
[1345.82 → 1354.10] And the reason why I share that isn't it's not to expose that necessarily, but to point it out because I got to see that.
[1354.44 → 1361.84] And I felt like that was a raw, real moment with Adam in a conversation that was quite lengthy.
[1362.26 → 1369.06] It's like two and a half hours, I think, real time, maybe two hours, you know, produced.
[1369.06 → 1382.32] And that's why I like doing podcasting, because you get that truly real, truly authentic, truly deep when you can go there kind of conversation that can only really happen in a podcast like that.
[1382.70 → 1385.06] You are the Barbara Walters of our...
[1385.06 → 1385.96] Baba Walters.
[1387.52 → 1388.98] You like my impersonation?
[1389.44 → 1390.04] That was good.
[1390.20 → 1391.04] Baba Walters.
[1391.68 → 1392.40] All right.
[1392.52 → 1394.12] Don, BMC.
[1394.26 → 1394.72] Hook him up.
[1394.72 → 1399.86] My favourite episode was from Chef to System Initiative.
[1400.56 → 1403.16] I've been following Adam Jacob on social media for a while.
[1403.68 → 1406.16] I've been also following Adam Jacob to work.
[1406.82 → 1408.62] And I got kicked out of his company.
[1409.22 → 1414.12] So it was interesting to hear more about his career journey that led him to kick me out of his company.
[1414.94 → 1420.40] And I disagree with him, but regardless, he is always entertaining, and he is always kicking me out.
[1420.40 → 1436.46] The goodness that Break Messing land brings is just so good.
[1437.26 → 1437.62] Right?
[1437.92 → 1440.78] I love the little, is that like a cop cherry sound?
[1440.90 → 1441.80] Like the cops are there?
[1441.98 → 1442.62] Like, who!
[1442.68 → 1445.14] You know, that's what I figured when he gets kicked out of his company.
[1445.28 → 1447.00] Like, he calls the police on him, you know?
[1447.40 → 1447.90] Oh, yeah.
[1448.00 → 1448.80] It's, uh...
[1448.80 → 1449.76] I don't think it's that.
[1449.76 → 1454.08] I think it's that, uh, that whistle when you pull it out, it elongates the sound.
[1454.12 → 1457.06] And when you push it in, it might be the same thing that we're talking about, but...
[1457.06 → 1457.48] Right, right, right.
[1457.50 → 1458.96] I wasn't saying it's actually that sound.
[1459.02 → 1460.46] I was saying, like, that's what it's reminiscent of.
[1460.50 → 1467.00] I'm wondering if BMC was trying to imply that Don McKinnon actually had to be arrested at System Initiative Headquarters.
[1467.16 → 1468.80] It's quite possible, honestly.
[1471.42 → 1472.36] That'll make you cry.
[1472.48 → 1472.80] All right.
[1472.82 → 1473.40] It's quite possible.
[1473.40 → 1483.64] Moving on to long-time listener, I believe new Changelog++ member, if this is indeed the same, Andrew O'Brien.
[1484.16 → 1484.90] Hey, Jared and Adam.
[1485.08 → 1486.60] Thanks for another year of great pod.
[1486.76 → 1491.04] Big thanks to Adam for giving me the push I needed to finally rewatch and finish Silicon Valley.
[1491.50 → 1492.70] Also, an apology.
[1492.70 → 1498.02] I'm sorry for ruining the whole Antarctic data centre joke in one of your fly.io ads.
[1498.46 → 1501.92] I asked follow-up questions, and then it went away, so I feel responsible.
[1502.30 → 1507.14] Anyway, here's my message to anyone listening who has a professional development stipend to spend before year-end.
[1507.36 → 1515.78] Everyone knows that Changelog++ is better, but what my theory presupposes is that it's a membership that gets you more educational material, so work should pay for it.
[1515.78 → 1520.26] Fill out that reimbursement form and get that warm, fuzzy feeling for supporting independent tech media.
[1520.48 → 1521.28] Thanks again, guys.
[1521.28 → 1525.52] Now, there has to be an inside story on this Antarctic code vault.
[1525.66 → 1528.16] Do you know Andrew, and you were interviewing him for something?
[1528.50 → 1530.06] No, this is disconnected.
[1530.48 → 1530.60] Okay.
[1530.76 → 1536.42] So for a bit there, on the fly homepage, it said, I can't recall how many continents there are.
[1536.48 → 1537.16] Is there seven continents?
[1537.58 → 1538.20] I always forget.
[1538.62 → 1539.88] I'm too old to remember this stuff.
[1539.90 → 1541.24] There are seven continents, aren't there?
[1541.32 → 1541.62] Right.
[1541.68 → 1545.52] I believe there's seven, and they mention Antarctica coming soon.
[1545.78 → 1546.18] Right.
[1546.18 → 1553.40] I thought it's a joke, and I started seeing that as part of the big thanks to our friends at Fly and partners at Fly.
[1553.62 → 1554.06] All right.
[1554.26 → 1555.88] Antarctica coming soon, you know?
[1556.44 → 1557.54] And I think that's what he's referencing.
[1558.02 → 1561.92] And I didn't take it away from that because he said something in Slack.
[1561.92 → 1563.02] I think it was Slack at the time.
[1563.02 → 1563.98] Oh, okay.
[1564.26 → 1566.06] So he brought up in Slack and ruined the joke.
[1566.26 → 1566.48] Yeah.
[1566.90 → 1574.54] But he did ask if, I think it was him, and Slack is a challenge because it's hard to find the right people, I suppose, over the years.
[1574.62 → 1578.78] But I think Zulip's a bit easier to catch with people because you see the thread longer.
[1578.90 → 1579.66] It doesn't go away.
[1579.72 → 1580.58] It's not really ephemeral.
[1580.58 → 1592.92] So I don't really recall the conversation in Slack necessarily, but I do recall the conversation around speculation of if it truly was going to be in Antarctica coming soon.
[1593.30 → 1601.56] We speculated whether there was, you know, servers down there because there are bases down there, et cetera, if there truly is a down there, flat partners.
[1603.28 → 1604.34] So that's what it is.
[1604.34 → 1605.26] Oh, I thought you were going to keep talking.
[1605.46 → 1606.26] You just ended it.
[1606.34 → 1607.74] You just mic dropped on the flat partners.
[1607.74 → 1609.12] I dropped it on the flat partners, man.
[1609.20 → 1609.32] Yeah.
[1609.32 → 1610.72] So a couple of things.
[1610.80 → 1613.04] First, great idea.
[1613.48 → 1620.08] Thanks for promoting, Andrew, the concept of having your employer pay for your Changelog++ membership.
[1620.28 → 1621.40] I mean, come on.
[1621.56 → 1624.28] This is continuing education at its core, is it not?
[1624.66 → 1626.44] I mean, I think that's awesome.
[1626.72 → 1627.24] Do more of it.
[1627.26 → 1627.80] Great idea.
[1628.04 → 1629.86] Everybody who thinks of it thinks, why not?
[1630.02 → 1631.92] If you haven't thought of it, hopefully now you've thought of it.
[1632.48 → 1633.54] It's a win-win-win.
[1633.54 → 1641.56] I will shout out to Andrew for what I think is a Royal Tenenbaum's deep cut in the middle of one of his sentences.
[1641.86 → 1650.38] He says, my theory presupposes, which to me sounded very much like Owen Wilson on Royal Tenenbaum's talking about Custer dying.
[1650.38 → 1651.22] I'm going from memory.
[1651.52 → 1655.96] It's like everybody knows that Custer died at the Battle of Little Bighorn, something like that.
[1656.34 → 1660.06] But what my book presupposes is maybe he didn't, something like that.
[1660.30 → 1662.44] Well, everyone knows Custer died at Little Bighorn.
[1662.66 → 1666.06] What this book presupposes is maybe he didn't.
[1666.06 → 1674.36] So, Andrew, if that's indeed your reference, reference acknowledged, friend, and you have a Royal Tenenbaum's fan here,
[1674.42 → 1677.54] if not, then I just completely ran into something that didn't exist.
[1677.68 → 1679.44] And either way, go check out Royal Tenenbaum's.
[1679.50 → 1679.82] Good movie.
[1680.18 → 1681.46] I've never watched that movie.
[1681.64 → 1682.50] I have to confess.
[1682.70 → 1683.38] Do you like Wes Anderson?
[1683.84 → 1684.30] Maybe.
[1684.98 → 1685.24] Okay.
[1685.72 → 1687.36] What kind of movies has he directed?
[1688.22 → 1689.20] Royal Tenenbaum's.
[1689.42 → 1689.82] Okay.
[1689.98 → 1690.56] That's a good one.
[1690.92 → 1692.28] Well, I guess we'll find out.
[1692.28 → 1696.92] Bottle Rocket, Fantastic Mr. Fox, The Life Aquatic with Steve Sis.
[1697.30 → 1698.06] This is all from memory?
[1698.28 → 1698.76] Yeah, I'm a fan.
[1698.98 → 1699.70] I'm a Wes Anderson fan.
[1699.76 → 1700.48] Wow, I'm proud of you.
[1700.56 → 1701.08] You're welcome.
[1701.16 → 1703.18] I bet you quickly LLM'd yourself or something.
[1703.60 → 1704.52] No, I'm just going from memory.
[1704.78 → 1705.90] Wes Anderson.
[1706.26 → 1716.60] He has a very specific style, a very specific taste, and all the same characters as Owen Wilson, Luke Wilson, Bill Murray, Angelica Houston,
[1716.60 → 1718.88] like these people, Jason Schwartzman.
[1719.10 → 1722.02] He has all the same actors in his movie, George Clooney.
[1722.28 → 1723.64] In his movies all the time.
[1724.42 → 1730.34] And I just watched Fantastic Mr. Fox with my family a few weeks back, and that movie completely holds up.
[1730.72 → 1732.08] I just utterly enjoyed it.
[1732.64 → 1735.26] I'm going to have to circle back.
[1735.36 → 1738.48] I resisted the royal Tenenbaum's.
[1739.66 → 1743.52] I thought it looked maybe strange.
[1743.64 → 1745.92] Also, 2001 wasn't a year I was watching a lot of movies.
[1746.34 → 1747.28] It is strange.
[1747.48 → 1748.88] It takes a specific taste.
[1748.88 → 1754.28] I think you either love Wes Anderson movies or you hate them because they're shot in a specific way.
[1754.36 → 1764.28] In fact, Adam Lessor, here's another foreshadow, and I were talking about how I felt like his commercials, like a lot of the sandwich films, were borrowing prompts.
[1764.28 → 1766.30] Not prompts, but homages to Wes Anderson.
[1766.44 → 1767.20] He's like, yeah, totally.
[1767.74 → 1767.86] Wow.
[1768.04 → 1770.06] He shoots in a very, he has his choreography.
[1770.78 → 1771.52] It's amazing.
[1771.70 → 1774.80] But it's also like very opinionated and specific.
[1775.02 → 1780.24] And so if you don't like that style, and the humour is very subdued and somewhat intellectual.
[1780.92 → 1786.44] And so it's not like a Tommy boy, you know, it's like, it gets funnier the more you think about it.
[1786.46 → 1788.72] When the first time you hear it, like, this is ridiculous.
[1788.94 → 1789.72] Like, it's just so stupid.
[1789.96 → 1794.56] So I'm not saying that you'll necessarily love Royal Tenenbaum's, but if you watch it, it's well-made.
[1794.62 → 1796.46] So you at least appreciate the craft.
[1796.56 → 1799.84] And if you enjoy it, there's a bunch of movies waiting for you.
[1799.84 → 1800.42] Just like it.
[1800.64 → 1800.84] Yeah.
[1800.90 → 1801.66] Or versions of it.
[1801.94 → 1805.78] I do recall the Grand Budapest Hotel being promoted.
[1806.36 → 1806.46] Yeah.
[1806.76 → 1807.40] Was that a good one?
[1807.58 → 1808.22] That's a good one.
[1808.80 → 1809.44] It's not my favourite.
[1809.44 → 1812.88] I think Tenenbaum's is a more approachable movie to start with.
[1813.00 → 1813.26] Okay.
[1813.38 → 1816.24] Fantastic Mr. Fox because it is animated.
[1816.72 → 1817.04] Okay.
[1817.26 → 1818.40] Great music, by the way.
[1818.70 → 1819.66] It's very approachable.
[1820.04 → 1820.44] Kid friendly?
[1820.92 → 1821.20] Yes.
[1821.44 → 1822.44] We watched it with our whole family.
[1822.98 → 1828.16] There are a few things that are like adult things, but they just fly over the kid's head.
[1828.24 → 1830.76] It's not like the whole movie's like that, but there are moments where you're like,
[1830.94 → 1833.32] hmm, this is kind of mature, but the kids just don't notice it.
[1833.84 → 1837.20] This isn't the best place to go for this, but it's one of the places I go to it.
[1837.20 → 1847.34] But if I want to know if I can trust this for my kid, I do use IMDB's section where it talks about parental spots.
[1847.44 → 1856.88] It's like as you scroll the profile page for a movie title, there's a section that talks about the different things that appear in the movie,
[1856.88 → 1862.38] specifically for parents to gauge whether they should or should not.
[1863.04 → 1864.96] Like nudity, violence, et cetera.
[1865.48 → 1865.56] Yeah.
[1865.58 → 1868.50] There's also like specific websites that are watching.
[1868.66 → 1872.30] One that I don't know if it's good anymore, but used to be good was called Kids in Mind.
[1872.76 → 1875.88] And they actually watch and review movies with kids in mind.
[1875.88 → 1884.34] And they will tell you almost to an extreme level where they're like every single thing that happens that might be something you might want to know about prior to the kids watching it.
[1884.70 → 1886.86] And so in the past, I have used that.
[1887.08 → 1888.22] I know there are other ones.
[1888.60 → 1894.12] Do you recall a female in the movie being called the town tart in her youth?
[1894.48 → 1894.80] Yeah.
[1895.08 → 1895.38] Okay.
[1896.44 → 1898.82] They highlighted that as sex and nudity.
[1899.14 → 1899.54] Right.
[1899.72 → 1900.16] Which is cool.
[1900.20 → 1902.12] It's called the parental guide.
[1902.36 → 1903.34] She's the town tart.
[1903.46 → 1904.30] She's the town tart.
[1904.30 → 1905.88] That goes over their head, doesn't it?
[1905.92 → 1906.70] They're like, what's a tart?
[1906.88 → 1907.20] Why is it?
[1907.58 → 1908.56] Why would the town have a tart?
[1908.68 → 1909.32] Like pop tarts?
[1909.42 → 1909.88] What are they talking about?
[1910.08 → 1910.64] Yeah, sure.
[1911.10 → 1911.78] Pop tarts are sweet.
[1912.28 → 1912.60] All right.
[1912.64 → 1916.88] So anyway, we could have just created an entire tangent around something Andrew wasn't referring to.
[1916.98 → 1921.36] But if you were indeed referring to a quote from Royal Tenenbaum's, reference acknowledged.
[1921.72 → 1921.98] All right.
[1922.36 → 1925.24] Here is Andrew's Break master Cylinder remix.
[1926.00 → 1926.74] Hey, Jared and Adam.
[1926.90 → 1928.90] Thanks for another year ruining Silicon Valley.
[1929.38 → 1932.96] Big thanks to Adam for giving me the push I needed to also ruin Silicon Valley.
[1932.96 → 1933.62] Oh my gosh.
[1933.62 → 1936.08] Anyway, here's my message to everyone listening.
[1937.40 → 1938.12] Silicon Valley.
[1939.04 → 1940.14] Also, an apology.
[1940.46 → 1942.58] I'm sorry for my message to everyone listening.
[1945.02 → 1946.26] I feel responsible.
[1946.86 → 1947.74] And you should.
[1948.18 → 1949.78] So many, so many dings.
[1950.30 → 1953.02] Well, I told BMC you literally can't have enough dings.
[1953.58 → 1954.08] Literally cannot.
[1954.08 → 1961.04] So yeah, I mean, in a sense, maybe we have ruined Silicon Valley, but also maybe.
[1961.04 → 1961.46] I don't think so.
[1961.52 → 1963.08] In a sense, we brought it back.
[1963.40 → 1968.08] Yeah, I think we've been responsible for a lot of HBO subscriptions.
[1968.08 → 1969.08] I think so.
[1969.48 → 1972.26] We should get an HBO Max affiliate code or something.
[1972.58 → 1973.10] We really should.
[1973.14 → 1975.04] Like every time you stream that, there should be a royalty.
[1975.44 → 1976.72] Like an Adam and Jared royalty.
[1976.72 → 1981.72] I would just take a 4K version of the entire series.
[1982.68 → 1983.36] You don't have that?
[1983.48 → 1984.36] They didn't shoot in 4K?
[1984.36 → 1990.76] Well, if you recall, Christina Warren, if you recall, she and I, or at least she was,
[1990.80 → 1992.80] and we were both lamenting, at least I was lamenting this.
[1993.48 → 1999.12] These studios purposefully withhold the higher resolution versions on disc.
[1999.76 → 2003.68] They make you subscribe to the service to get the higher resolution.
[2003.96 → 2007.52] So there's lots of Seinfeld even, I believe, in like DVD quality.
[2007.70 → 2008.58] Like, come on, for real?
[2008.78 → 2008.90] Yes.
[2009.12 → 2011.10] Not even Blu-ray quality, DVD quality.
[2011.44 → 2012.86] You're about to get Rage Monster out.
[2013.08 → 2014.00] Let's not do this.
[2014.36 → 2014.78] Let's go on.
[2014.82 → 2015.40] Tone it down.
[2015.52 → 2015.98] Hold still.
[2016.26 → 2016.58] Yes.
[2016.84 → 2018.06] This is supposed to be a happy time, you know?
[2018.14 → 2018.64] Stay out of the log.
[2018.70 → 2019.64] It is supposed to be a happy time.
[2020.16 → 2024.04] But I don't believe that we've break-matched the cylinder.
[2024.12 → 2026.28] We did not ruin Silicon Valley.
[2026.44 → 2027.30] Thank you for all the dings.
[2027.46 → 2028.74] No, Andrew O'Brien ruined it.
[2028.76 → 2029.78] He feels responsible.
[2030.10 → 2031.82] Did he actually say that in his actual voicemail, though?
[2031.82 → 2032.58] I don't think he did, did he?
[2032.70 → 2035.26] No, he said that you caused him to go watch Silicon Valley.
[2035.36 → 2035.64] Right.
[2035.64 → 2038.00] And then BMC remixed his words.
[2038.64 → 2038.98] That's right.
[2039.28 → 2039.50] Yeah.
[2039.70 → 2040.30] That's what I was thinking.
[2040.40 → 2041.52] I mean, that's what you sign up for around here.
[2041.60 → 2042.36] It's a remix, you know?
[2042.36 → 2044.94] No, we're going to hijack what you say and make you say something different.
[2045.32 → 2046.10] I mean, pretty much.
[2046.20 → 2050.24] Don McKinnon just told a story about how he got arrested at System Initiative Headquarters,
[2050.38 → 2050.70] you know?
[2050.88 → 2052.02] And he doesn't agree with Adam.
[2052.12 → 2053.22] I don't think that really happened.
[2053.50 → 2054.70] No, I don't believe that happened at all.
[2054.84 → 2055.70] Let's hope not.
[2056.26 → 2056.96] We'll have to confirm.
[2057.68 → 2058.26] Silicon Valley.
[2058.26 → 2068.52] Well, friends, this is the last chance you have to get the 8sleep Pod 4 Ultra in your
[2068.52 → 2071.10] hands in your bedroom before Christmas.
[2071.64 → 2078.56] Go to 8sleep.com slash changelog and use the code changelog if you need to get $350 off
[2078.56 → 2081.08] your very own Pod 4 Ultra.
[2081.32 → 2082.42] I've never had better sleep.
[2082.56 → 2083.34] I love this thing.
[2083.44 → 2085.02] I sleep on it every single night.
[2085.02 → 2088.20] My wife and I, we absolutely love what it does for our sleep.
[2088.56 → 2090.88] So what exactly is the Pod?
[2091.16 → 2095.80] Imagine a high-tech mattress cover that you can easily add to any bed.
[2096.22 → 2097.46] And this isn't just any cover, though.
[2097.50 → 2099.96] It's packed with sensors, heating and cooling elements.
[2100.18 → 2103.20] It's all controlled by sophisticated AI algorithms.
[2103.66 → 2106.04] And it's all designed to give you better sleep.
[2106.04 → 2111.96] It's like having a sleep lab, a smart thermostat, and a personal sleep coach all rolled into
[2111.96 → 2115.82] a single device and no wearables required.
[2115.82 → 2121.88] It uses a network of sensors to track a wide variety of biometrics while you sleep, sleep
[2121.88 → 2123.56] stages, heart rate variability.
[2123.88 → 2124.58] That's so important.
[2125.02 → 2127.64] Respiratory rate, temperature, and so much more.
[2128.02 → 2128.62] The best part?
[2129.00 → 2131.46] It does all this without you having to wear any devices.
[2131.46 → 2133.06] Again, no wearables.
[2133.68 → 2138.00] And the accuracy rivals what you would get in a professional sleep lab.
[2138.46 → 2142.68] The Pod uses precision temperature control to regulate your body's sleep cycles.
[2143.08 → 2148.68] It can cool you down to a chilly 55 degrees Fahrenheit or warm you up to 110 Fahrenheit.
[2149.12 → 2151.32] And it does this separately for each side of the bed.
[2151.62 → 2155.68] This means that you and your partner can each have your own ideal sleep temperature going on.
[2155.68 → 2162.28] And the really, really cool part is the Pod uses AI and machine learning to learn how you
[2162.28 → 2164.06] sleep, to learn your sleep patterns over time.
[2164.28 → 2168.86] And it uses this data to automatically adjust the temperature of your bed throughout the
[2168.86 → 2173.30] night to fine tune how you sleep, to give you more REM sleep, to give you deeper sleep.
[2173.62 → 2174.88] And that's the part I love most.
[2175.04 → 2178.96] And all this functionality is accessible through their awesome mobile app.
[2179.04 → 2184.80] You get detailed sleep analytics, trends over time, and even a daily sleep fitness score.
[2184.80 → 2187.80] Again, go to 8sleep.com slash changelog.
[2187.88 → 2188.80] Use our code changelog.
[2189.42 → 2192.40] Get $350 off your very own Pod 4 Ultra.
[2192.86 → 2193.40] Do it now.
[2193.76 → 2194.54] Sleep up for Christmas.
[2195.10 → 2197.94] Again, 8sleep.com slash changelog.
[2198.24 → 2203.28] And also by our friends over at Wix, I've got just 30 seconds to tell you about Wix Studio,
[2203.78 → 2208.18] the web platform for freelancers, agencies, and enterprises.
[2208.90 → 2213.76] So here are a few things you can do in 30 seconds or less on Studio.
[2213.76 → 2219.56] Number one, integrate, extend, and write custom scripts in a VS Code-based IDE.
[2220.16 → 2224.04] Two, leverage zero setup dev, test, and production environments.
[2224.74 → 2227.36] Three, ship faster with an AI code assistant.
[2227.94 → 2231.80] And four, work with Wix headless APIs on any tech stack.
[2232.14 → 2236.88] Wix Studio is for devs who build websites, sell apps, go headless, or manage clients.
[2236.88 → 2239.74] Well, my time is up, but the list keeps going on.
[2240.08 → 2242.20] Step into Wix Studio and see for yourself.
[2242.66 → 2244.66] Go to wix.com slash studio.
[2244.96 → 2247.48] Once again, wix.com slash studio.
[2247.48 → 2255.40] All right, next up, an old voice, Jarvis Yang.
[2255.50 → 2261.28] I think Jarvis calls in every year and gives us shoutouts, but also gives other people shoutouts.
[2261.56 → 2263.08] And this is no different here.
[2263.66 → 2267.00] Jarvis is going to shoutout us as well as somebody else.
[2267.08 → 2267.50] Here he is.
[2267.50 → 2269.30] NIA Hong Changelog.
[2269.58 → 2270.76] That's hello and long.
[2271.34 → 2278.34] As the year comes to a close, I wanted to give a big shoutout to both the Ship It Podcast and Prime Digital Academy.
[2278.74 → 2282.80] When I started diving into DevOps, Ship It became my go-to resource.
[2283.18 → 2287.68] Gerhard, Adam, and Jared, you've all taught me so much, and it had a huge impact on my journey.
[2288.16 → 2289.04] Thank you for everything.
[2289.04 → 2295.54] I also want to recognize Prime Digital Academy, which, after 10 incredible years, is closing its doors.
[2295.98 → 2301.90] Prime was where my second career in software development began and helped me through some of the toughest times in my life.
[2302.14 → 2305.46] Gave me an amazing supportive community and lifelong connections.
[2305.84 → 2308.46] A special shoutout to my abash cohort.
[2308.86 → 2309.56] Ooh, ha, ha.
[2309.84 → 2311.92] And of course, to Mary and Christy.
[2312.28 → 2314.40] Thank you for being such inspiring mentors.
[2314.86 → 2318.38] It's bittersweet to say goodbye to both Prime and the Ship It Podcast,
[2318.38 → 2322.50] but the impact you've made will stay with me and so many others.
[2322.80 → 2325.02] Thank you for being such a big part of my journey.
[2325.46 → 2326.82] There's an obvious thing here, right?
[2326.90 → 2328.04] I mean, are you going to say that?
[2328.44 → 2328.92] Go ahead.
[2329.38 → 2331.52] What is Prime Digital Academy?
[2334.50 → 2336.86] First time hearing about this, did I miss something?
[2337.20 → 2339.46] No, this was a boot camp that Jarvis went to.
[2339.74 → 2339.98] Okay.
[2340.12 → 2344.72] And just like last year, Jarvis shouted out, I think it was like Minnesota Gophers or something.
[2344.80 → 2346.04] Like he likes to give shoutouts.
[2346.04 → 2350.60] And so he gives Ship It a shoutout, and then he gives Prime Digital Academy,
[2350.76 → 2354.36] which is a software engineering boot camp that helped Jarvis launch his career.
[2354.82 → 2356.68] And it's closing down after 10 years.
[2356.84 → 2360.84] And so there's some alignment there with Ship It being retired now.
[2361.24 → 2361.52] I see.
[2362.02 → 2362.26] There.
[2362.38 → 2363.04] There's your connection.
[2363.48 → 2364.04] Oh, okay.
[2364.16 → 2364.94] That makes more sense.
[2365.06 → 2365.64] I was like, gosh.
[2366.64 → 2369.84] I thought we were getting credit where credit was not due or conflation.
[2370.02 → 2371.42] I was like, what is going on here?
[2371.42 → 2372.30] I'm down.
[2372.44 → 2376.08] I'm on the webpage, primeacademy.io, by the way.
[2376.64 → 2379.18] They're in the mix of the IOS that may get repurposed.
[2379.26 → 2379.60] We'll see.
[2380.36 → 2382.72] And I'm on the about page, and I'm like, meet our team.
[2382.80 → 2384.12] I'm like, I don't know any of these people.
[2384.98 → 2385.98] Where is the connection?
[2386.12 → 2386.68] Please help me.
[2386.84 → 2387.72] So anyway, that's it.
[2387.72 → 2391.74] So Jarvis then sent me this note in addition to the audio submission.
[2392.50 → 2398.38] Glad to hear that Ship It is getting its spinoff and looking forward to more of the dynamic duo, Justin and Autumn.
[2398.52 → 2401.76] So yes, Ship It will have a continuity.
[2402.24 → 2408.70] It will have a continuation as a different pod called FAO, Fork Around and Find Out.
[2409.12 → 2412.92] And then he says, for context, Ooh aha, which you heard him say Ooh aha.
[2413.14 → 2413.70] Yeah, I did say it.
[2413.78 → 2416.70] Was his cohort's call-out on campus.
[2416.70 → 2418.12] So they would say that to each other.
[2418.26 → 2419.62] And so he's giving him a call-out.
[2419.98 → 2420.24] Okay.
[2420.64 → 2421.10] All right.
[2421.32 → 2423.92] Can I share a call-out that I used to do back in the day?
[2424.24 → 2424.60] Brouhaha?
[2424.88 → 2426.10] No, this is going to be epic.
[2427.04 → 2427.88] Okay, I like it.
[2427.92 → 2428.62] This is going to be epic.
[2428.72 → 2429.22] This should be clipped.
[2430.24 → 2433.20] V-I-C-T-O-R, Victor.
[2433.58 → 2436.66] V-I-C-T-O-R, Victor.
[2436.78 → 2438.38] You mess with the best you'd like the rest.
[2438.54 → 2439.18] Victor what?
[2439.32 → 2440.08] Victor what?
[2440.92 → 2441.28] Wow.
[2442.36 → 2444.70] That's not my best rendition, but it's a pretty good one.
[2445.28 → 2445.84] Say more.
[2445.84 → 2446.58] The context.
[2447.00 → 2448.52] I was in the military, of course.
[2449.46 → 2452.50] And the military has an alphabet, A thorough Z, just like anybody else.
[2452.66 → 2455.18] But V is Victor.
[2455.34 → 2458.94] So when you do the phonetic alphabet, at least the military version of it.
[2459.02 → 2460.38] Alpha, Bravo.
[2460.42 → 2465.00] Alpha, Bravo, Charlie, Delta, Echo, all the things.
[2465.16 → 2468.08] You know, Foxtrot all through V, which is Victor.
[2468.32 → 2469.52] And so I was in Victor company.
[2470.24 → 2470.48] Oh.
[2470.48 → 2475.58] And so every company is charged with creating their own thing to kind of get the hype.
[2475.86 → 2477.58] Kind of like this ooh-ha-ha thing.
[2477.86 → 2479.46] Except for that one's shorter, right?
[2479.86 → 2480.08] Yeah.
[2480.08 → 2483.54] And so it was Victor company.
[2483.72 → 2484.68] V-I-C-T-O-R.
[2484.86 → 2485.30] Love it.
[2485.66 → 2485.80] Yeah.
[2486.00 → 2489.84] You should send that to your old Victor company colleagues.
[2489.90 → 2490.40] What do you call them?
[2491.14 → 2491.56] Colleagues.
[2491.98 → 2492.72] Troops, I guess.
[2492.94 → 2493.34] Soldiers.
[2493.80 → 2493.98] Yeah.
[2493.98 → 2494.72] Your fellow soldiers.
[2494.86 → 2494.98] Yeah.
[2495.02 → 2495.56] Fellow soldiers.
[2496.40 → 2497.94] But you mess with the best.
[2498.32 → 2499.08] You down like the rest.
[2499.28 → 2499.82] Victor what?
[2500.10 → 2500.72] Victor what?
[2500.88 → 2502.30] Is the clincher.
[2502.98 → 2503.46] Love it.
[2503.46 → 2504.76] All right.
[2504.98 → 2505.50] Jarvis.
[2506.16 → 2506.76] Remixed.
[2507.70 → 2508.24] Ooh-ha-ha.
[2513.24 → 2515.30] The year comes to a close.
[2518.10 → 2520.60] It had a huge impact on my journey.
[2522.24 → 2524.04] The toughest times in my life.
[2525.00 → 2526.58] Me and me since we're in the new.
[2527.70 → 2529.04] My long connection.
[2530.44 → 2532.50] And such inspiring interest.
[2532.50 → 2533.50] It's been very sweet.
[2534.06 → 2535.30] Bittersweet to say goodbye.
[2537.14 → 2539.02] And I give me a mistake with me.
[2539.68 → 2540.88] And so many others.
[2559.06 → 2559.86] There you go.
[2560.06 → 2562.28] I don't know about you, but I've got my scalp massager out.
[2562.50 → 2566.92] And I'm thoroughly, just thoroughly just relaxed.
[2567.18 → 2570.88] I was going to say, it reminds me of like, you're about to get hypnotized.
[2571.16 → 2573.44] And they're like, you are floating off into sleep.
[2573.78 → 2574.06] Yes.
[2574.20 → 2576.58] There are no problems in your life.
[2577.06 → 2580.54] You are weightless as you float on a cloud.
[2581.24 → 2581.40] Yeah.
[2582.10 → 2584.40] Well, you know, even BMC has a softer side.
[2585.12 → 2585.44] Yeah.
[2585.80 → 2586.24] I dig it.
[2586.38 → 2586.60] And so does Jarvis.
[2586.92 → 2587.12] Yeah.
[2587.12 → 2588.16] I dig it.
[2588.50 → 2589.06] All right.
[2589.18 → 2590.88] We move onward and upward.
[2592.18 → 2593.08] Here's Brett Cannon.
[2593.82 → 2594.78] Hi, Adam and Jared.
[2595.04 → 2595.80] Congratulations again.
[2595.94 → 2598.58] Another banger of a year for the changelog.
[2598.96 → 2602.56] For my highlights of 2024, the Cannon breakdown into themes.
[2602.56 → 2604.58] Probably the first thing was hardware.
[2604.98 → 2611.22] Episode 608 for interviews with building customizable ergonomic keyboards with Evers Zuckerman of USA.
[2611.38 → 2617.70] I thought that was really cool to hear their ethos and approach to making keyboards that last and can last for a long time.
[2618.24 → 2623.58] Interviews episode number 592 from Sun to Oxide with Brian Mandrel was great just for the stories alone.
[2623.58 → 2625.92] Also with what Oxide is trying to do with hardware.
[2626.24 → 2629.58] And then finally for hardware was interviews episode number 582.
[2630.42 → 2632.88] We have a right to repair with Kyle Wayne's.
[2633.24 → 2638.44] I also say that's the most expensive episode for me personally because it led to me buying an fixity repair kit.
[2638.68 → 2640.32] And it has actually been very helpful.
[2640.66 → 2642.46] So thank you, Adam, for that recommendation.
[2642.72 → 2643.72] The next theme is languages.
[2644.20 → 2645.30] No shock coming from me.
[2645.52 → 2650.58] Interviews episode number 611, Free Threaded Python with my friends Pablo and Lukas from the Core.py podcast.
[2650.58 → 2653.74] It was obviously a lot of fun to hear someone else interview them for a change.
[2654.14 → 2658.30] And then also Changelog and Fred's episode number 28, gradually typing Elixir.
[2658.38 → 2664.50] It was kind of cool to hear Jose talk about how Elixir is trying to bring in typing after having seen how Python tried to pull it off.
[2664.88 → 2666.84] The third theme was operating systems.
[2667.06 → 2670.90] Actually, in Ship It, episode number 122 with Linux distros with Jorge Castro,
[2670.90 → 2677.50] it was kind of cool to hear how Universal Blue is trying to use containers to make operating systems a bit easier to work with from a Linux perspective.
[2677.50 → 2683.70] And then it was great to hear, let's talk FreeBSD finally from Changelog interviews number 574 with Alan Jude,
[2683.86 → 2686.18] because FreeBSD, I don't think it's enough play in the world.
[2686.44 → 2690.60] Theme number four was apps with Changelog and friends episode 35 with the Obama Pros.
[2690.70 → 2694.64] It was cool to hear Shannon Parker-Stolberg talk about how they make Obama Pro work as a business.
[2694.84 → 2701.42] And also personally, it was kind of a fun episode because it was the first time I was out with an extended walk with my son by myself
[2701.42 → 2704.46] and trying to keep him calm with mom not around.
[2704.46 → 2711.24] And then there was also Why We Need Lady Bird, Changelog interviews number 604 with Andreas King and Chris Winston
[2711.24 → 2713.70] and how trying to make browsers extremely hard.
[2713.94 → 2715.84] And then finally, the fifth theme is people.
[2716.34 → 2723.60] And that was from Changelog interviews, episode number 595 with Kelsey Hightower talking about retired but not tired
[2723.60 → 2729.62] and just hearing Kelsey seemingly having a great time, no longer being constrained by the corporate world
[2729.62 → 2731.58] and getting to do what he truly wants to do.
[2731.58 → 2736.02] Once again, congrats again for a wonderful 2024 and look forward to 2025.
[2736.72 → 2736.92] Bye.
[2737.36 → 2740.06] I'm thinking Brett just knocked out the rest of your list.
[2740.50 → 2746.02] Well, I was pumping my fist on several of them, but I have to say that I'm not batting a thousand now.
[2746.08 → 2746.56] It's a shame.
[2746.88 → 2750.48] There was two or several that were not on my list.
[2751.16 → 2752.00] And I'm sad now.
[2752.00 → 2756.34] Well, he did pick 10 episodes, so I mean, he's rivalling you in quantity.
[2756.80 → 2757.70] Yes, true.
[2758.24 → 2760.86] Can we talk about BSD or at least free BSD?
[2761.12 → 2762.00] Can we or did we?
[2762.22 → 2763.38] Can we briefly?
[2763.84 → 2764.28] Sure.
[2764.28 → 2766.22] So I got excited about that afterwards.
[2766.60 → 2768.40] And I share Brett's excitement too.
[2768.50 → 2776.50] But then I got sad because it seems like free BSD is just not getting the love because it's not the way I suppose Linux is.
[2777.26 → 2780.78] And there's the lack of support for certain things.
[2780.78 → 2782.34] And it's just hard.
[2782.48 → 2783.74] It's just hard to use.
[2784.52 → 2790.42] And so I think it gets – it has such good pure intentions, but it doesn't get the same love that Linux proper gets.
[2790.86 → 2792.24] Gets the same love in what way?
[2792.30 → 2792.86] What do you mean love?
[2793.50 → 2798.08] Well, obviously Linux is, you know, one over it is what I mean by that.
[2798.16 → 2798.70] But I think –
[2798.70 → 2799.06] Corporate love.
[2799.46 → 2801.48] I think developer love, you know, really.
[2801.62 → 2801.92] Investment.
[2802.48 → 2803.34] Investment potentially.
[2803.64 → 2806.10] But I believe – I can't recall at this moment.
[2806.20 → 2807.88] I'll have to go back in my links and find it.
[2807.88 → 2815.80] But I believe earlier this year there was talk about how FreeBSD wasn't supporting certain things, and they were falling by the wayside.
[2815.94 → 2826.52] And essentially, like, it seemed to me like if I was reading the tea leaves, like, pay less attention to it because it's just eventually going to always be this super minority.
[2827.04 → 2827.52] It's a niche.
[2827.94 → 2828.16] Yeah.
[2828.54 → 2828.76] Yeah.
[2829.24 → 2831.36] I mean, you really got to want to feel the pain, I suppose.
[2832.12 → 2832.40] Right.
[2832.72 → 2834.34] Or have already overcome the pain.
[2834.34 → 2839.52] And that's why the reputation – and I brought that up, I think, on that episode –
[2839.52 → 2839.66] Yeah.
[2839.94 → 2844.32] Is that FreeBSD people are generally more expert because they have to be.
[2844.68 → 2846.36] And it's harder to use than Linux.
[2847.04 → 2850.74] Not necessarily because it's more complicated or wrong or anything, but just different.
[2850.74 → 2851.32] Mm-hmm.
[2851.70 → 2854.00] And a smaller community.
[2855.32 → 2861.28] So fewer helps, less investment, less support, et cetera.
[2861.28 → 2868.04] So sorry to hear that, but there's certainly people who love and use it and build cool things with it.
[2868.40 → 2870.66] That being said, you should check it out.
[2870.90 → 2875.48] I'm actually, like, on hackaday.com on a post from this year.
[2875.62 → 2880.02] And at the very end, just scanning it, it says FreeBSD is here to stay.
[2880.80 → 2882.08] So don't take it from me.
[2882.16 → 2883.78] I am not steeped in all the things.
[2884.16 → 2884.84] I'm not in great –
[2884.84 → 2885.56] You just tried it.
[2885.60 → 2887.24] You hit some bumps.
[2887.48 → 2887.84] Yeah.
[2888.06 → 2892.28] You saw some people saying it was not going to be supported for whatever you're up to.
[2892.42 → 2892.98] And it's like –
[2892.98 → 2893.48] Precisely.
[2893.68 → 2900.54] It's kind of just the harder path in some cases than the straight – not the straight and narrow – than the mainstream path.
[2900.54 → 2902.50] I mean, that being said, I did spin up ZFS.
[2902.96 → 2905.00] I did get a file server running.
[2905.30 → 2907.14] I did do all the things I intended to do.
[2907.26 → 2908.50] Do you remember where you got stuck?
[2908.98 → 2909.78] I didn't get stuck.
[2910.06 → 2912.00] I didn't actually have any issues with it personally.
[2912.00 → 2919.32] But it was just this tension of what FreeBSD was supporting and what it wasn't supporting and how it was being supported.
[2919.44 → 2925.44] And then you got True NAS, who moved away from FreeBSD to basically a Debian version.
[2925.72 → 2927.16] And they're deprecating.
[2927.28 → 2929.14] They're sort of maintaining the FreeBSD flavour.
[2929.98 → 2932.58] But True NAS scale is the future of True NAS.
[2932.98 → 2937.18] Not that they're the litmus test of FreeBSD dying or not.
[2937.18 → 2945.18] It's just like, well, if the people making a file system and a server can't build their future on FreeBSD, then who can?
[2945.30 → 2946.24] Where does it really fit?
[2947.04 → 2949.46] And so that's what was making me think, well, maybe it's just not worth my –
[2949.46 → 2950.06] It's not that they can.
[2950.16 → 2951.36] It's that they chose a different way.
[2951.62 → 2951.94] Sure.
[2952.24 → 2952.44] Yeah.
[2952.92 → 2953.50] Fair enough.
[2953.98 → 2954.88] I had no problem with it.
[2954.88 → 2955.24] I loved it.
[2955.28 → 2956.08] It was actually kind of fun.
[2956.46 → 2960.76] Except it was limiting, you know, to me at some point.
[2960.96 → 2963.64] Now, do you recall Brett's voicemail last year?
[2963.94 → 2965.78] You probably just listened to it last night while you were going to sleep.
[2965.78 → 2966.20] Oh, yeah.
[2966.48 → 2966.80] Andrea.
[2966.90 → 2967.48] My wife, Andrea.
[2968.08 → 2968.40] All right.
[2968.46 → 2968.68] Good.
[2968.98 → 2969.24] All right.
[2969.24 → 2969.62] Here we go.
[2969.68 → 2970.98] Here's Brett's remix from this year.
[2971.68 → 2972.38] Hi, Adam and Sure.
[2972.82 → 2973.18] Congratulations.
[2973.34 → 2976.24] This is another singer of the year for Changelog.
[2976.42 → 2979.66] For my highlights of 2024, break down the themes.
[2979.88 → 2981.26] Probably the first thing was hardware.
[2981.78 → 2986.20] Episode 6 or 8 for interviews with customizable ergonomic keyboards.
[2986.38 → 2990.28] With Evan Zuckerman of CSA, I thought that was really cool to hear their ethos.
[2990.28 → 2993.72] An approach to making keyboards that last and can last for a long time.
[2993.72 → 2997.74] Interviews episode number 5592.
[2998.04 → 3000.26] From Sun to Oxide with Brian Vendrell was great.
[3000.34 → 3001.60] Just for the stories alone.
[3001.74 → 3004.26] Also with what Oxide is trying to do with hardware.
[3004.72 → 3007.20] I'll also say I really enjoyed episode 558.
[3007.46 → 3009.08] It was my wife, Andrea.
[3009.08 → 3013.26] I want to give a shout-out to my wife, Andrea.
[3014.08 → 3014.48] Andrea.
[3015.58 → 3018.22] Gotta give a shout-out to my wife, Andrea.
[3019.06 → 3020.60] Oh, man.
[3021.54 → 3022.16] So good.
[3022.78 → 3024.70] Where else would you get that kind of goodness in life?
[3025.20 → 3025.78] I'm telling you.
[3026.08 → 3030.82] I mean, you put your spoon in to that cup, and you're coming out with goodness, okay?
[3031.52 → 3032.32] Yum, yum, yum.
[3032.32 → 3037.82] Okay, so I'm digging what Break master's doing on the voices stuff.
[3038.00 → 3038.76] That's pretty cool.
[3039.12 → 3040.40] I want more of that in our life.
[3040.66 → 3040.82] Right.
[3041.20 → 3043.70] I feel like these are proving grounds for future coolness.
[3044.18 → 3047.90] I was also thinking not this voicemail remix, but the one prior.
[3048.90 → 3053.40] It'd be kind of cool to also release a companion podcast that's just the voicemails.
[3053.86 → 3055.44] Just like we did with the album.
[3055.84 → 3058.40] I don't know if that would fit or not, but I'm just thinking like as a condensed version,
[3058.48 → 3059.58] just listen to them all in continuity.
[3059.78 → 3060.34] It's like, there you go.
[3060.38 → 3060.48] Boom.
[3060.48 → 3062.56] Yeah, especially if we can't sleep at night.
[3062.66 → 3064.62] You and I could just listen to people call us and leave us.
[3064.74 → 3064.92] That's right.
[3065.04 → 3066.06] Say nice things about us.
[3066.18 → 3066.24] I mean.
[3066.32 → 3067.28] I feel bad about my life.
[3067.36 → 3068.08] Let me listen to this show.
[3069.28 → 3070.12] They love us.
[3070.42 → 3071.16] People like us.
[3071.22 → 3072.16] They really like us.
[3072.50 → 3073.18] That was a good one, Brett.
[3073.32 → 3074.38] I liked that one a lot.
[3074.54 → 3077.26] Brett, thanks for liking so many of our episodes.
[3077.44 → 3079.12] I mean, I gave it a hard time because you picked 10.
[3079.34 → 3080.50] At least they were from this year.
[3080.68 → 3081.40] That's also a callback.
[3082.60 → 3086.00] And the fact that you like so many of our shows is kind of amazing, isn't it?
[3086.02 → 3088.12] I mean, I appreciate that.
[3088.12 → 3090.00] One in particular, if you don't mind.
[3090.00 → 3090.68] Go ahead.
[3090.74 → 3091.16] Pick one.
[3091.36 → 3091.94] Get into it.
[3092.26 → 3093.20] Change log interviews.
[3093.98 → 3095.04] Episode 592.
[3095.98 → 3097.04] From sun to oxide.
[3098.14 → 3098.54] Epic.
[3099.18 → 3101.82] I thought he would pee himself.
[3102.70 → 3103.52] During the podcast.
[3104.64 → 3106.62] You thought Brian Cantwell was going to pee himself.
[3106.84 → 3108.24] I thought Brian would.
[3108.80 → 3111.50] Well, he drank like three Diet Cokes or something like that.
[3111.56 → 3112.54] Like during the podcast.
[3112.90 → 3115.02] When you say epic, you mean it literally in terms of length.
[3115.26 → 3115.52] Oh, yeah.
[3115.52 → 3116.02] It was long.
[3116.02 → 3119.18] I think it was as long as I could maybe have ever gone.
[3119.66 → 3120.70] Probably our longest episode.
[3120.88 → 3121.42] I think so.
[3121.62 → 3121.84] Honestly.
[3122.00 → 3124.70] That wasn't a sometimes when we do anthologies, they get long.
[3124.84 → 3126.14] But single conversation.
[3126.54 → 3126.72] Yeah.
[3126.84 → 3128.96] Let me just for.
[3129.30 → 3130.76] Oh, I can sort by duration pretty easily.
[3130.88 → 3131.50] I do have a.
[3132.22 → 3133.00] 153 minutes.
[3134.04 → 3135.14] That's two hours.
[3136.00 → 3136.76] 33 minutes.
[3136.76 → 3140.18] I do happen to have our database available to me.
[3140.64 → 3140.94] Okay.
[3141.68 → 3142.36] And I can.
[3142.62 → 3143.30] Sort by length.
[3143.48 → 3144.84] Query it for.
[3145.14 → 3145.50] Exactly.
[3145.94 → 3147.72] We have audio duration as a field.
[3148.10 → 3148.44] Mm-hmm.
[3148.68 → 3152.64] And I will say order by audio duration.
[3153.62 → 3153.94] Okay.
[3154.04 → 3160.00] So in terms of audio duration, if we take out the anthologies, which was Adam's brilliant idea.
[3160.06 → 3160.82] I hadn't thought of it.
[3160.82 → 3166.82] And limited to this year, the longest episode was from Sun to Oxide with Brian Cantwell.
[3167.54 → 3174.36] So yes, the longest episode of the year, except for Microsoft is all in on AI part two, which had three interviews on it.
[3174.44 → 3175.18] Now that's this year.
[3175.26 → 3178.16] Should I pull out this year and just see of all time?
[3178.26 → 3179.26] Let's see of all time now.
[3180.04 → 3180.52] Boom.
[3181.76 → 3182.64] 708 rows.
[3182.82 → 3185.48] This is from interviews and friends all time.
[3185.48 → 3189.48] And the longest episode of all time is from Sun to Oxide with Brian Cantwell.
[3189.96 → 3190.12] Mm-hmm.
[3190.16 → 3190.64] So there you go.
[3191.24 → 3191.64] Confirmed.
[3191.94 → 3192.10] Yeah.
[3192.22 → 3194.08] I mean, I thought he was going to burst.
[3194.30 → 3199.00] And the second longest that's not an anthology is from Chef to System Initiative, which we already covered.
[3199.34 → 3199.36] So.
[3199.58 → 3199.92] Right.
[3200.52 → 3204.64] These deep dives expect more like this, I think, next year.
[3204.96 → 3206.30] Adam going deep one-on-one.
[3206.70 → 3207.20] So deep.
[3207.38 → 3211.26] It's like founder's talk on the changelog.
[3211.90 → 3212.66] It's beautiful.
[3212.98 → 3213.64] It is beautiful.
[3214.26 → 3215.10] Some would say it's better.
[3215.38 → 3216.74] Especially when the ads are removed.
[3217.94 → 3219.26] Because it's even shorter.
[3219.62 → 3220.62] Because it's long enough.
[3220.82 → 3221.18] Okay.
[3221.24 → 3221.54] Yes.
[3221.54 → 3222.06] Truth.
[3222.28 → 3224.82] Moving on to our next voicemail.
[3225.32 → 3228.56] This is Nail Suleiman.
[3229.00 → 3230.00] Hello, Adam and Jared.
[3230.28 → 3231.84] Congratulations on another great year.
[3231.84 → 3236.16] really so many of the episodes on the changelog are amazing.
[3236.16 → 3242.28] But really ones that have stuck out to me, especially just looking through the list of episodes this year.
[3242.48 → 3249.54] Really anything with Kelsey Hightower or the Oxide folks have just been, you know, great episodes and I've really enjoyed them.
[3249.54 → 3252.72] I also really liked the Moneyball episode.
[3252.72 → 3259.54] It was just a nice exploration of entrepreneurship and software that doesn't necessarily have to be like a rocket ship startup.
[3259.80 → 3263.58] Other episodes, the Obverse books, you know, and the talk about that.
[3263.68 → 3266.44] I listened to those books this year and really enjoyed them all.
[3266.44 → 3270.22] I'm kind of sad I listened to them a little too fast and finished them all in about a week.
[3270.54 → 3273.00] The ergonomic keyboards episode was great.
[3273.26 → 3275.14] The right to repair episode was really great.
[3275.46 → 3278.26] And I think there were several episodes on home lab things.
[3278.42 → 3279.60] And I really liked those too.
[3279.60 → 3287.02] For me, the changelog is a big source of discovery for new types of software and things like that I had never heard of before.
[3287.26 → 3289.24] This year, it was Zulip, I think, in particular.
[3289.46 → 3296.00] I was, and it was great timing because I was getting tired of Slack and the other mainstream chat platforms.
[3297.00 → 3299.42] And yeah, Zulip was just a nice breath of fresh air.
[3299.52 → 3301.08] And yeah, I've really, really liked using it.
[3301.08 → 3309.28] From other years, especially Doppler and Nat's were two pieces of software that are still a very big part of my software systems now.
[3309.28 → 3314.02] And I really appreciate being introduced to these pieces of software through your podcast.
[3314.40 → 3316.16] Anyway, thanks again for a great year.
[3316.26 → 3317.54] And I'm looking forward to the next.
[3318.52 → 3325.74] I dig it because Nail was, he started the WordPress drama thread, by the way, and has been consistently posting in there.
[3326.20 → 3330.34] And that's been going on for a while, so much so that I'm scrolling back.
[3330.46 → 3337.42] So September 21st, Nail posted odd drama going on in the WordPress land thoughts and linked out to like two X posts.
[3337.42 → 3337.54] Yes.
[3338.42 → 3340.78] And then, yes, Don McKinnon just after that.
[3340.84 → 3343.46] So maybe that was where you're connecting it a little behind the scenes there.
[3343.54 → 3345.04] But yeah, dig those.
[3345.18 → 3346.40] I mean, thanks for listening.
[3346.58 → 3347.06] So awesome.
[3347.56 → 3347.64] Yeah.
[3348.00 → 3349.38] And being in Zulip.
[3349.60 → 3350.06] That's right.
[3350.16 → 3353.28] And joining us there and threading up the threads.
[3354.06 → 3359.92] I like to hear stories like this one where it's like, I found cool technology because of the show.
[3359.92 → 3362.08] So I adopted cool technology.
[3362.58 → 3364.90] Now my life is better because of cool technology.
[3365.04 → 3371.64] Like for me, that's kind of what we are all about is like finding cool stuff, showing it to people, talking about it.
[3372.10 → 3372.90] That's a win.
[3373.42 → 3374.04] It's a big win.
[3374.16 → 3374.36] Yeah.
[3374.40 → 3377.48] It's always been this spotlight kind of nature behind the scenes.
[3377.56 → 3377.92] This exposure.
[3378.96 → 3383.08] This where is the light less shined and shine it there and see what's over there.
[3383.08 → 3388.08] And sometimes it's not so much duds, but like just cool stuff, but not so interesting.
[3389.12 → 3393.70] And then sometimes it's like, wow, there was a diamond in the rough over there and we found that thing.
[3393.74 → 3399.22] And now it's like, boom, it's, you know, all the places doing all the things like Zulip.
[3399.24 → 3400.54] Clean it off, shine it up.
[3400.98 → 3402.30] You know, hanging out in Zulip.
[3402.70 → 3403.42] And Baba verse.
[3404.02 → 3404.48] Oh, yeah.
[3404.48 → 3405.58] It's got to be exposed there.
[3405.68 → 3407.64] It's not software, but it is book.
[3408.42 → 3408.82] Books.
[3409.12 → 3410.20] Certainly on your list.
[3410.28 → 3411.56] Then is he Taylor episode.
[3412.12 → 3412.32] Yeah.
[3412.32 → 3413.20] It is on my list.
[3413.58 → 3415.88] How does it feel that your list is almost entirely predictable?
[3416.52 → 3418.02] Well, do you got any surprises in there?
[3418.46 → 3418.86] I don't know.
[3418.92 → 3420.28] I mean, is that a good thing or a bad thing?
[3420.64 → 3421.88] Well, that's why I asked you how you feel.
[3421.98 → 3422.92] I don't know if it's good or bad.
[3423.62 → 3427.20] I feel like that means that I'm probably in alignment with our audience.
[3427.64 → 3429.42] No, I mean not predictable by them, by me.
[3429.50 → 3430.74] Like I know which ones you're going to pick.
[3431.14 → 3432.28] It's just because I know you so well.
[3432.88 → 3435.74] Well, I'm cool with that.
[3435.94 → 3436.36] There you go.
[3436.60 → 3437.28] That's what I mean.
[3437.36 → 3437.76] I dig it.
[3438.16 → 3438.60] Okay, good.
[3438.96 → 3439.38] So do I.
[3439.38 → 3440.60] Here's Nail's remix.
[3440.60 → 3443.24] This year, kind of sad.
[3443.34 → 3445.08] I think there were no episodes on rocket ships.
[3445.30 → 3446.12] I really like those.
[3446.52 → 3449.14] I think there were several episodes on software things.
[3449.96 → 3450.70] Never rocket ships.
[3451.84 → 3452.32] Entrepreneurships.
[3452.62 → 3452.80] Great.
[3453.10 → 3453.98] Anything with ships.
[3454.36 → 3459.18] But really, so many of the episodes are about software, things like that I had never
[3459.18 → 3464.22] heard of before that doesn't necessarily have to be like a, you know, podcast.
[3466.22 → 3467.70] I really like rocket ships.
[3467.70 → 3479.86] It's got some Donkey Kong vibes.
[3480.02 → 3481.40] I was just going to say that.
[3481.66 → 3481.96] Yeah.
[3482.32 → 3482.94] Donkey Kong.
[3483.06 → 3483.26] Yep.
[3483.88 → 3485.22] The other vibe I get is Rain Man.
[3485.34 → 3486.72] Didn't that kind of have like Rain Man vibes?
[3486.82 → 3488.06] I just really like rocket ships.
[3488.28 → 3489.36] Just the way he remixed it.
[3489.80 → 3490.14] Yes.
[3490.40 → 3492.00] The obsession with a specific thing.
[3492.34 → 3493.00] Tropical freeze.
[3493.00 → 3495.38] We need a new version of Tropical freeze.
[3496.04 → 3496.62] I am down.
[3497.04 → 3497.40] I mean.
[3497.48 → 3497.86] I am down.
[3498.64 → 3499.56] DK for life.
[3499.80 → 3500.80] I am 100% down.
[3501.16 → 3501.42] Yeah.
[3501.92 → 3502.74] For some more DK.
[3502.92 → 3503.26] All day.
[3503.44 → 3503.86] All day.
[3504.12 → 3505.18] DK all day, man.
[3505.28 → 3506.00] That's what I always say.
[3506.16 → 3512.96] So I've been listening to some synth wave remixes of, I guess, game soundtracks remixed, like
[3512.96 → 3513.68] synth wave style.
[3514.60 → 3518.44] And Donkey Kong Country, et cetera, translates very well.
[3519.60 → 3520.92] Retro Kid on YouTube.
[3521.44 → 3521.98] Check them out.
[3521.98 → 3522.66] Amazing.
[3523.00 → 3523.32] Yeah.
[3523.74 → 3524.74] Code to those beats.
[3525.22 → 3525.42] Nice.
[3525.62 → 3528.14] And I've archived them to my Plex, by the way.
[3528.42 → 3530.52] Did you try out Archive Box?
[3531.04 → 3531.96] No, I have a Plex.
[3532.26 → 3534.26] So I've just been Flexing it.
[3534.62 → 3539.06] But the principles of Archive Box have crept into my life.
[3539.18 → 3539.52] Right.
[3539.60 → 3542.46] Well, you had mentioned that maybe you were working too hard and this might be easier,
[3542.58 → 3543.58] but you already have it solved.
[3543.80 → 3544.32] So it just.
[3544.58 → 3544.94] Yeah.
[3544.94 → 3549.62] I already have the software and already have an uptime guarantee on it and et cetera.
[3549.88 → 3550.12] So.
[3550.50 → 3550.70] Yeah.
[3550.70 → 3552.04] I'm just Flexing it essentially.
[3552.04 → 3557.28] So I'm just moving it into my music category in Plex and I go to Retro Kid and I push play
[3557.28 → 3560.26] and all the albums just queue up and I work.
[3560.96 → 3561.34] Sweet.
[3561.34 → 3563.62] And there's a good Zelda track in there.
[3563.62 → 3564.70] So you would be.
[3565.12 → 3565.56] Bring it.
[3565.80 → 3566.00] Yeah.
[3566.16 → 3567.00] You'd love it.
[3567.16 → 3573.54] I'm currently playing the new Zelda Echoes of Wisdom where you get to play as Zelda herself.
[3573.74 → 3575.28] My little daughters love it.
[3575.62 → 3576.74] And we are playing it right now.
[3576.74 → 3579.84] It's a classic Zelda.
[3580.64 → 3581.78] Exactly what you'd expect.
[3581.90 → 3584.12] So far we're about 45 minutes in.
[3584.24 → 3586.80] So I can't review it entirely, but so far so good.
[3587.14 → 3587.72] Who's this?
[3587.84 → 3589.62] It's our old friend, Lars Wickman.
[3590.52 → 3594.00] Hi, this is Lars Wickman, a long time listener, occasional guest.
[3594.00 → 3602.68] I recently did my Pocket Casts wrapped type of deal and three of my top four most frequently
[3602.68 → 3610.58] listened podcasts had the same theme as in visual theme, as in dark with neon green colours.
[3610.58 → 3614.38] And to most people, maybe the changelog does not have that.
[3614.62 → 3616.78] For changelog++ members, it does.
[3617.08 → 3618.66] And of course, it's better.
[3619.22 → 3623.22] But yeah, the other ones are acquired and oxide inference.
[3623.34 → 3626.46] And you've done the oxide inference crossover when I appreciate it greatly.
[3627.16 → 3629.42] So acquired crossover next?
[3629.76 → 3630.16] Maybe.
[3630.64 → 3631.18] That'd be cool.
[3631.56 → 3638.32] And aside from that, I really appreciated the episodes with the Beat master Break master cylinder.
[3638.62 → 3639.16] I'm sorry.
[3639.16 → 3646.56] And since went to Bandcamp and picked up his back catalogue for not that much money.
[3646.92 → 3653.20] And now I have a bunch of his hits, among others, Change Log Dance Party, burned out on
[3653.20 → 3655.24] Minidisc, and I play them in my office.
[3655.70 → 3656.98] So that's what I'm up to.
[3657.34 → 3658.92] What do you think about that, Adam?
[3658.94 → 3662.76] Maybe getting acquired in 25 on the show?
[3663.02 → 3663.56] I'm down.
[3663.86 → 3667.36] I'm on the .fm right now, acquired.fm, checking it out.
[3667.36 → 3668.32] I've heard of the show.
[3668.32 → 3669.82] I haven't listened to too many of them.
[3669.92 → 3670.48] It's very popular.
[3670.58 → 3672.10] I haven't listened to it either, but people love it.
[3672.14 → 3672.96] I think they do a good job.
[3673.28 → 3673.86] I'm down.
[3674.42 → 3675.08] Crossover away.
[3675.26 → 3675.64] Let's do it.
[3675.72 → 3676.38] We'll see if they're down.
[3676.92 → 3680.52] You know, I'm seeing their about page, and it seems like they're maybe on a stage.
[3680.62 → 3685.18] Like, I think this next year, I don't want to call it a conference, but it'll be cool
[3685.18 → 3686.46] to do a live podcast.
[3687.36 → 3689.26] Like, sell tickets, do a live podcast.
[3689.50 → 3690.16] That'd be kind of cool.
[3690.16 → 3691.70] Have you seen this?
[3691.76 → 3693.70] Where there's like the thing that podcasters are doing?
[3693.80 → 3697.02] I'm wondering, could we sell 50 tickets, maybe?
[3697.52 → 3698.50] I think we'd sell 50.
[3698.76 → 3699.48] In a city?
[3699.60 → 3702.82] I think if we went to like New York or San Francisco or...
[3702.82 → 3703.44] Yeah, or Austin.
[3703.94 → 3704.60] Austin even.
[3704.76 → 3705.32] Maybe Austin.
[3705.86 → 3706.88] Austin's kind of small, though.
[3707.32 → 3708.04] It's big, small.
[3708.60 → 3710.90] Yeah, but it's tech big to a certain extent.
[3711.14 → 3711.46] Yeah.
[3711.94 → 3713.36] I suppose Elon's doing something.
[3713.36 → 3714.54] And it's centrally located.
[3714.66 → 3715.64] Like, people will fly, maybe?
[3716.06 → 3716.36] True.
[3716.92 → 3717.32] Or drive?
[3717.34 → 3718.86] I mean, it is my backyard, so I'm down.
[3718.92 → 3720.42] I mean, SF would be much easier, though.
[3720.80 → 3722.98] I just have less hope that we have a ton of listeners here.
[3723.28 → 3725.64] I think we have more based on our stats.
[3725.88 → 3731.56] I've shipped out some shirts and some other merch lately, and I'm telling you, Texas listens.
[3731.86 → 3732.18] Okay.
[3732.86 → 3733.26] All right.
[3733.44 → 3734.12] I'm wrong, man.
[3734.38 → 3734.86] I love it.
[3735.06 → 3736.12] Not necessarily wrong.
[3736.22 → 3737.20] I'm just saying there are some people there.
[3738.08 → 3738.78] Anywho, yeah.
[3738.92 → 3739.62] That would be cool.
[3739.62 → 3748.36] I also think it's super rad that Los his creating mini-discs of BMC beats and stuff and listening to them on mini-disc.
[3748.52 → 3750.28] I mean, analog.
[3750.64 → 3753.78] I mean, not literally analog, but like real life for the win.
[3753.94 → 3754.90] Real life for the win.
[3755.66 → 3756.08] Hardware.
[3756.42 → 3758.68] Physical media for the win, is what I meant to say.
[3758.94 → 3760.10] Yeah, physical media is cool.
[3760.44 → 3763.12] I don't know if I like physical media personally.
[3763.18 → 3765.56] I think it's cool, but like, maybe not.
[3766.82 → 3767.30] Good take.
[3767.30 → 3767.34] Good take.
[3767.34 → 3767.98] Good take.
[3767.98 → 3768.26] Good take.
[3769.20 → 3770.46] That's cool, but maybe not.
[3770.48 → 3771.34] You all didn't see his face.
[3771.42 → 3773.78] He was struggling to figure out what to say, and he came up with a good take.
[3774.02 → 3776.70] Well, I was about to opine, then I'm like, I'm just going to leave it.
[3776.80 → 3777.12] Good take.
[3777.18 → 3777.72] Oh, gosh.
[3777.74 → 3778.44] You should opine.
[3778.68 → 3779.42] At least a sentence.
[3779.98 → 3782.18] I like physical things.
[3782.66 → 3786.90] I, of course, also lived through a time period where I was digitizing all my things.
[3787.00 → 3789.88] I don't like to print, but I also kind of think printing's cool now.
[3789.96 → 3792.20] So it's like, what's old is new again.
[3792.20 → 3797.58] And I think that physical media has a tangibility to it that we desire.
[3798.04 → 3799.16] And so in that way, it is cool.
[3799.36 → 3800.48] Obviously, there are lots of drawbacks.
[3800.66 → 3803.34] Like, you know, your dog eats it or something.
[3803.94 → 3805.58] My vehicle can't play it.
[3806.00 → 3809.28] It's useless to me in like the places I consume content.
[3809.54 → 3811.60] Well, how about a record player like in your house?
[3811.78 → 3812.50] Do you think that would be cool?
[3812.60 → 3813.50] I would love a record player.
[3813.66 → 3814.24] So that's cool.
[3814.32 → 3815.22] I would go there.
[3815.32 → 3815.48] Yeah.
[3815.74 → 3815.96] Yeah.
[3815.96 → 3816.84] That's kind of what he's doing.
[3816.90 → 3818.30] It sounds like with mini discs, you know?
[3818.36 → 3818.66] Okay.
[3818.78 → 3819.54] That's cool then.
[3819.70 → 3819.96] Okay.
[3820.06 → 3820.90] I'll take it back then.
[3821.08 → 3821.90] I need more context.
[3821.92 → 3822.80] I'm glad I opined.
[3822.96 → 3824.88] I'm down for that kind of thing.
[3824.98 → 3826.54] Like, I want a listening room, Jared.
[3826.68 → 3829.18] This is like intentional listening, I feel like, is what he's doing.
[3829.22 → 3829.36] Yeah.
[3829.36 → 3830.78] Which is very much what a record player is like.
[3830.80 → 3832.14] It's like, I'm going to listen to this now.
[3832.40 → 3832.58] Yeah.
[3832.58 → 3835.32] It's not like, oh, let's just queue up artists.
[3835.50 → 3835.72] Right.
[3835.80 → 3839.10] Let me just download this off YouTube and just throw out of my play and get to work.
[3839.26 → 3842.80] Now, this is like, let's sit down and enjoy some Break master Cylinder beats.
[3843.40 → 3844.04] All right, Lost.
[3844.30 → 3844.84] Remix him.
[3845.66 → 3846.02] Hi.
[3846.16 → 3847.12] This is Lost Weidman.
[3847.12 → 3849.26] Longtime listener, occasional guest.
[3849.82 → 3854.56] I really appreciated the episodes with Break master Cylinder.
[3856.44 → 3860.52] And went to Bandcamp and picked up his back catalogue.
[3861.16 → 3866.84] And now I have a bunch of his hits for not that much money.
[3866.84 → 3870.88] I have, among others.
[3872.78 → 3873.22] And.
[3875.70 → 3876.14] And.
[3878.38 → 3878.82] Gosh.
[3879.22 → 3881.16] I had a dance party in my office.
[3882.30 → 3883.26] That's what I'm up to.
[3883.68 → 3885.62] I have a dance party in my office.
[3886.62 → 3887.58] That's what I'm up to.
[3887.58 → 3893.16] So I can say that the I don't know if this is how your household went, Jared, but the moment
[3893.16 → 3900.52] that dance party was on the actual, I guess, proverbial air waves, like on Spotify, I was like,
[3900.58 → 3901.84] okay, that's when it's real.
[3902.28 → 3902.56] Yeah.
[3902.56 → 3904.22] And, you know, obviously we QA'd it.
[3904.30 → 3910.22] We kind of like previewed some things, but I didn't listen to it with intention and enjoyment
[3910.22 → 3915.64] and motion, like body motion, until it was on Spotify.
[3916.10 → 3922.28] And the moment it was, I queued it up and legit me and the kids just danced.
[3922.38 → 3923.58] They mainly danced a lot.
[3923.70 → 3925.50] I just like moved a little, you know.
[3925.50 → 3929.38] So they were really having a lot of fun for the whole thing.
[3929.74 → 3932.34] Like we just listened end to end the entire album.
[3933.04 → 3933.84] It was awesome.
[3934.38 → 3934.52] Yeah.
[3934.52 → 3937.32] It's just a cool thing to have that be real.
[3937.46 → 3943.20] I definitely got cooler in my kid's eyes when we had some actual beats like on Apple
[3943.20 → 3946.34] Music and Spotify, even though we were not the artist.
[3946.54 → 3949.62] We were just the curators of this music.
[3949.72 → 3950.44] Just a vessel.
[3950.44 → 3952.18] We're a vessel for which these things came.
[3952.30 → 3955.44] We were part of the creative process, you know, but BMC does all.
[3955.92 → 3956.56] All the creation.
[3956.70 → 3957.20] The true creation.
[3957.50 → 3957.64] Yeah.
[3957.68 → 3962.60] And I will say that like that, that Dracula's purse, you know, like that sound just immediately
[3962.60 → 3964.14] triggers in a good way.
[3964.80 → 3966.08] Me and my kids.
[3966.16 → 3967.98] And it's just like, yeah, here we go.
[3968.20 → 3968.56] Yes.
[3968.94 → 3973.42] Which I think Dracula's purse is, which is the first real track off of Next Level, the
[3973.42 → 3974.46] video game inspired one.
[3974.76 → 3980.04] I think that's our most listened to track on the proverbial air waves.
[3980.04 → 3981.16] It's the most popular one now.
[3981.68 → 3984.76] It makes sense because the Castlemaine soundtrack was just phenomenal.
[3985.22 → 3985.36] Yeah.
[3986.06 → 3993.26] And Dracula's purse is obviously an homage to Dracula's curse, which was the true music
[3993.26 → 3998.20] that came from the video game that literally everybody loves way more than Zelda.
[3998.94 → 3999.24] Ha.
[3999.24 → 4000.92] Just saying.
[4001.72 → 4002.32] Just saying.
[4003.60 → 4004.70] We could take a poll.
[4004.92 → 4006.04] I think you might lose that one.
[4006.50 → 4008.48] It would probably lose.
[4008.56 → 4008.94] It would.
[4009.38 → 4009.90] No offence.
[4010.62 → 4011.86] It's just not as popular.
[4012.44 → 4013.86] It's more of a cult classic.
[4013.92 → 4014.84] It's a dang shame.
[4014.94 → 4016.48] Hey man, I love Castlemaine.
[4017.18 → 4018.78] So you're not going to get me to disagree.
[4019.00 → 4020.90] Although the fact that you don't like Zelda.
[4021.34 → 4022.18] I do like Zelda.
[4022.18 → 4023.84] I just never got into it as much.
[4024.64 → 4025.10] That's all.
[4025.24 → 4025.72] Fair enough.
[4025.86 → 4027.50] I identified more so with Castlemaine.
[4028.26 → 4030.60] You know, it just had different touchpoints, I suppose.
[4030.76 → 4036.08] It might have been the first NEW game I'd maybe bought.
[4036.08 → 4040.54] Or like there was some connection to it where it was up there more than Zelda.
[4041.24 → 4044.90] And I also grew up poor, so I don't think I was able to afford Zelda for many years.
[4044.96 → 4046.00] I think I had to play my friends.
[4046.12 → 4047.22] It was gold, so it was cool.
[4047.36 → 4047.70] You know, like that.
[4047.86 → 4051.04] It had the gold cartridge, but you know, it didn't cost any more than the other games.
[4051.22 → 4051.48] Yeah.
[4051.68 → 4052.74] It was super cool.
[4052.98 → 4053.32] You know?
[4053.86 → 4055.76] I didn't have the bling to get the thing, you know?
[4055.82 → 4056.22] I'm sorry.
[4057.22 → 4059.04] You had to settle for Castlemaine.
[4059.52 → 4059.78] Yeah.
[4059.78 → 4061.26] All right, moving on.
[4061.42 → 4063.68] Here comes Nick Needed.
[4063.84 → 4067.92] My favourite episodes of the changelog are the ones where Adam and Jared just let loose
[4067.92 → 4070.94] and just get so excited about the topics that they're discussing.
[4071.22 → 4073.02] That's things like Home lab for Adam.
[4073.24 → 4074.62] His face just lights up.
[4074.68 → 4075.74] You can hear it in his voice.
[4075.82 → 4077.22] He gets very excited about that.
[4077.38 → 4079.82] And the same thing goes for Jared when it comes to TypeScript.
[4080.24 → 4084.16] He just can't control how excited he is about Type Safe JavaScript.
[4084.54 → 4086.74] And it really shows in the podcasts.
[4086.74 → 4090.74] Aside from that, I really enjoyed hanging with you guys at that conference in January,
[4091.28 → 4096.04] seeing you work the hallway and get amazing interviews from attendees and speakers,
[4096.42 → 4100.20] and playing a really fun game of JS Danger.
[4100.34 → 4101.22] That was so fun.
[4101.58 → 4102.96] Thank you for all that you do.
[4103.20 → 4109.20] And I am very much looking forward to what this new changelog podcast universe is all about.
[4110.16 → 4111.74] So much emotion, Nick.
[4111.76 → 4112.78] I appreciate that.
[4113.26 → 4114.24] Nick brings it.
[4114.52 → 4115.16] He does bring it.
[4115.16 → 4118.34] So then I'm thinking like, okay, he was joking about you, obviously, because you hate TypeScript.
[4118.64 → 4119.60] So was he joking about you?
[4119.64 → 4120.58] Or at least you do on a podcast.
[4120.80 → 4125.68] And I'm thinking like, maybe he thinks I don't like Home lab, and he's not telling the truth about me.
[4125.70 → 4128.02] I think he was being sincere with yours and joking with mine.
[4128.32 → 4128.62] Gotcha.
[4129.14 → 4130.22] It's part of the shtick, right?
[4130.24 → 4130.80] It's a setup.
[4131.02 → 4131.90] See, he set it up.
[4132.60 → 4132.88] Yes.
[4133.28 → 4133.56] Right.
[4134.48 → 4135.64] Nick's a showman, you know?
[4135.78 → 4136.34] Good one, Nick.
[4136.36 → 4137.62] He knows how to set it up and knock it down.
[4137.62 → 4141.38] I really, you know, I think that was the first time I met Nick.
[4141.94 → 4142.30] Yeah.
[4142.52 → 4147.70] Well, no, I met Nick back at the JS conference back in like Nebraska times.
[4147.94 → 4149.62] The very first Nebraska JS cone.
[4149.72 → 4149.92] Yeah.
[4150.08 → 4150.40] Yeah.
[4150.72 → 4153.06] And we've obviously digitally hung out.
[4153.34 → 4153.76] Right.
[4153.76 → 4156.64] Zooms and Riversides and podcasts.
[4156.98 → 4158.52] I don't think you guys hung out back in that.
[4158.58 → 4159.38] We were very busy.
[4160.12 → 4166.66] There were so many balls in the air between organizing the conference and trying to do Beyond Code, the video thing we're up to.
[4166.76 → 4166.94] Yes.
[4166.94 → 4168.58] It was a whirlwind.
[4169.10 → 4176.04] We should bring that back just for fun to see what people who never saw that just to get a glimpse of like the experiments, you know?
[4176.46 → 4177.54] The trials and tribulations.
[4177.78 → 4178.12] Right.
[4178.30 → 4178.96] It's out there.
[4179.50 → 4180.70] There's a playlist on our YouTube.
[4180.70 → 4182.90] I'm not going to link to it directly, but it's there.
[4182.90 → 4184.26] I'm not going to link to it directly.
[4185.46 → 4187.00] You will not get a link from me.
[4187.16 → 4189.44] It was the very first Changelog Films effort, I think.
[4189.70 → 4190.02] Yes.
[4190.58 → 4190.96] It was.
[4191.78 → 4193.32] I do want to say, though, about Nick.
[4193.74 → 4194.90] He's actually pretty cool.
[4195.50 → 4197.06] He's actually pretty cool.
[4197.34 → 4197.70] Surprise.
[4198.20 → 4198.40] Surprise.
[4198.64 → 4198.84] Yeah.
[4198.96 → 4200.32] Except for the whole TypeScript thing.
[4200.34 → 4201.16] I just don't understand.
[4201.48 → 4201.88] Why?
[4202.88 → 4203.60] Why the love?
[4203.78 → 4205.08] Why the fanaticism?
[4205.88 → 4208.38] You know, there are some things you just can't know.
[4208.94 → 4212.24] It's like, you know, TypeScript is kind of the Java of JavaScript.
[4212.90 → 4213.76] Nick would agree.
[4214.52 → 4216.78] And no one gets excited about Java.
[4216.96 → 4217.60] I mean, it's fine.
[4217.74 → 4218.38] It does its job.
[4218.42 → 4223.70] But like, what is there to get excited about and love and fanboy over TypeScript?
[4223.96 → 4224.50] Like types.
[4225.12 → 4225.74] Static types.
[4226.40 → 4227.12] It's not exciting.
[4227.38 → 4228.42] Maybe you think it's better.
[4229.38 → 4230.98] But I don't know.
[4231.04 → 4232.60] Let's just listen to Nick's remix.
[4232.80 → 4234.30] Let me just say, it is not better.
[4234.62 → 4234.94] TypeScript.
[4235.14 → 4235.82] It's not better.
[4236.04 → 4236.24] Yeah.
[4236.84 → 4237.52] It's worse.
[4237.80 → 4238.14] Here we go.
[4238.14 → 4242.68] My favourite episodes of the changelog are the ones where Adam and Jared just let loose
[4242.68 → 4244.94] and just get so excited about TypeScript.
[4245.14 → 4245.58] TypeScript.
[4245.72 → 4246.16] TypeScript.
[4246.48 → 4246.78] Yeah.
[4247.32 → 4250.50] Just get so excited about the TypeScript.
[4250.76 → 4252.32] Jared's face just lights up.
[4252.38 → 4253.44] You can hear it in his voice.
[4253.54 → 4255.16] He gets very excited about the TypeScript.
[4255.24 → 4258.32] S-E-R-I-P-T.
[4258.74 → 4259.34] All right.
[4259.38 → 4259.92] All right.
[4259.96 → 4260.50] All right.
[4260.52 → 4261.02] All right.
[4261.06 → 4262.46] I want to say thank you.
[4262.68 → 4264.76] It really shows in the podcasts.
[4264.76 → 4268.70] Aside from that, I really enjoyed hanging with you guys at that conference all about
[4268.70 → 4269.80] Type Safe JavaScript.
[4270.30 → 4271.36] And it really shows.
[4287.36 → 4290.04] TypeScript saves another day.
[4290.24 → 4290.58] Another day.
[4291.00 → 4291.88] Maybe that's why, Jared.
[4292.28 → 4292.72] Maybe.
[4292.84 → 4293.98] I mean, I'm almost converted.
[4293.98 → 4294.50] You're right.
[4294.76 → 4295.20] Ah.
[4295.90 → 4296.16] Yeah.
[4296.30 → 4297.90] That was a good preacher right there.
[4298.10 → 4298.40] Good preacher.
[4299.32 → 4299.66] All right.
[4299.72 → 4301.40] Next up, Rusty Nail.
[4302.36 → 4303.38] Hello there, listeners.
[4304.30 → 4310.56] My favourite moments of the year are, number one, big thanks for remastering 10,000 hours
[4310.56 → 4311.66] of deliberate programming.
[4312.04 → 4316.50] That was my overall favourite episode for two plus years that I've listened to the podcast.
[4316.94 → 4318.92] And I've been meaning to come back to that episode.
[4319.32 → 4323.90] However, I don't have to do that now that I re-listened it again in the main feed.
[4323.90 → 4324.44] Number two.
[4324.44 → 4324.86] Number two.
[4324.86 → 4324.92] Number two.
[4325.44 → 4331.74] In the go time 3.3.2, the discussion of the founder mode led me to a conclusion that I've
[4331.74 → 4333.34] always had it on myself.
[4333.34 → 4334.34] But I didn't know how it was called.
[4334.34 → 4335.48] But I didn't know how it was called.
[4335.48 → 4343.98] And during this summer, on one of the interviews, I was asked what made me an outlier among my
[4343.98 → 4345.28] peers and coworkers.
[4345.28 → 4350.20] And now I know what should have been the answer, which at the moment I did not.
[4350.60 → 4352.48] Now I am prepared for the next one.
[4352.82 → 4361.80] In the episode of 6.11 of Changelog, I was really excited to hear the voices of the core
[4361.80 → 4363.08] Python developer team.
[4363.08 → 4369.60] I've programmed in Python all my career and I have never interacted with these people in
[4369.60 → 4370.10] any way.
[4370.50 → 4375.12] Hearing the voices, I was generally excited about it.
[4375.54 → 4382.40] In the Practical AI 257, it was mentioned how the role of corporate culture and non-tech
[4382.40 → 4387.26] people impact the AI adoption in big corporations and organizations.
[4387.26 → 4390.10] And that was an eye-opening moment for me.
[4390.60 → 4393.22] So I was really excited to hear that.
[4393.44 → 4394.22] Number five.
[4395.20 → 4401.20] My absolute favourite episode of the year is when the Secret Service or police knocking on
[4401.20 → 4401.72] the door.
[4402.12 → 4410.72] I think it was episode 609 for not even hacking, but vulnerability reporting.
[4411.36 → 4414.86] And with a few of the jokes that went along with the story.
[4414.86 → 4419.52] Next, we share a fun fact in our morning stand-ups.
[4420.28 → 4425.34] And the day I learned about the boss factor from the Changelog conference number 70.
[4425.56 → 4432.56] I had to share the fun fact and I shared with the team what boss factor was.
[4432.74 → 4437.36] But it was actually called Morbid by our CEO.
[4437.78 → 4443.26] And finally, I think we're missing an insane hiring market episode this year.
[4443.26 → 4445.74] And this was the year that I shifted my job.
[4445.96 → 4447.66] First time over the last five years.
[4448.04 → 4451.80] And if you are going to do it, I do have a question to ask.
[4452.20 → 4453.60] It's more like a paradox.
[4454.16 → 4461.78] If everyone complains about not having enough talent and people to hire when you apply for
[4461.78 → 4464.34] a job at some company, you never hear anything back.
[4464.40 → 4468.24] If you don't have any connections there, how does this paradox happen?
[4468.24 → 4470.06] Good question.
[4470.56 → 4475.84] We did not do an insane hiring market with Gergay Arose this fall.
[4475.92 → 4477.14] We normally did it every fall.
[4477.38 → 4477.98] What's up with that?
[4478.06 → 4481.22] And I can't speak for you, Adam, but I just forgot about it this time.
[4481.62 → 4482.24] Oh, gosh.
[4482.42 → 4483.38] Did you forget about it?
[4483.46 → 4483.64] Or?
[4484.18 → 4488.70] I would like to say that maybe the well has dried up on, maybe, I don't know, on the
[4488.94 → 4490.72] should we dip back into that hiring market?
[4490.80 → 4491.48] It seems like we should.
[4491.54 → 4492.10] It was enjoyed.
[4492.78 → 4493.56] I love Gergay.
[4493.66 → 4494.52] I love talking to him.
[4494.70 → 4495.64] Yeah, people like that.
[4495.64 → 4497.56] I think we should definitely get Gergay on the show.
[4497.62 → 4500.68] He does have his own podcast now, so that's a thing.
[4500.78 → 4502.56] But maybe, you know, it could be a January thing.
[4502.58 → 4503.70] It doesn't have to be in the fall.
[4503.78 → 4505.02] It can be whenever we want it to be.
[4505.20 → 4507.46] So we could queue that up for Rusty.
[4507.62 → 4508.12] Let's do it.
[4508.58 → 4510.04] And ask that question.
[4510.70 → 4511.00] Yeah.
[4511.14 → 4512.00] I like doing it in the fall.
[4512.08 → 4517.38] It's a good end cap to the year because it's almost like, how do we get here and where
[4517.38 → 4517.84] are we going?
[4518.06 → 4519.66] Well, we dropped the ball in the fall, though.
[4520.70 → 4520.98] Yeah.
[4521.40 → 4524.00] So maybe we'll just wait till next fall.
[4524.54 → 4524.86] Maybe.
[4524.86 → 4526.98] Sometimes two years is the right amount of years.
[4527.38 → 4527.64] Sometimes.
[4528.54 → 4532.12] But I was pumping my fist on the best worst code base.
[4532.56 → 4532.88] Yes.
[4533.10 → 4533.76] That was a good one.
[4534.24 → 4535.36] I love that story.
[4535.54 → 4535.68] Yeah.
[4535.76 → 4536.30] Great story.
[4537.04 → 4538.78] 10,000 hours remastered.
[4539.20 → 4541.00] That was actually, I like how that worked out, actually.
[4541.20 → 4545.08] We had a gap, and we were thinking about what to do.
[4545.52 → 4548.54] And I was like, let's remaster an oldie, but a goodie.
[4549.22 → 4551.48] So I'm glad at least one person really enjoyed it.
[4551.48 → 4552.22] Mm-hmm.
[4552.34 → 4558.50] I think that it got re-listened to another 25-ish thousand times, maybe 21,000 times, at
[4558.50 → 4560.36] least based on the site stats.
[4560.86 → 4563.72] And the remastered version actually has some cool stuff.
[4564.02 → 4564.50] Chapters.
[4564.50 → 4564.70] Chapters.
[4565.18 → 4565.66] Mm-hmm.
[4565.66 → 4568.62] So the first time we did it was pre-chapters, and now it has chapters.
[4568.88 → 4573.30] So, you know, this listening experience might actually be slightly more enjoyable because
[4573.30 → 4574.68] you can jump around.
[4575.50 → 4576.40] Cue the music.
[4576.40 → 4582.00] My favourite numbers are the number five.
[4582.72 → 4584.18] Generally excited about it.
[4584.76 → 4585.48] The number two.
[4586.50 → 4589.88] Next is seven.
[4590.82 → 4593.60] But I think five plus two is actually seven.
[4593.88 → 4595.88] And that was an eye-opening moment for me.
[4596.08 → 4597.10] Now you know the answer.
[4597.10 → 4613.18] And finally, we're missing my absolute favourite number is 3.141-526-5979-3238-466-4338-3279-5278-419-419-7169-399-325.
[4613.18 → 4614.10] Oh my gosh.
[4615.16 → 4620.16] I don't know if this was it or not.
[4620.68 → 4625.66] I was thinking maybe those numbers at the end might have been like 4, 8, 15, 16, 23, 42,
[4625.66 → 4628.88] which is from the TV show Lost.
[4629.62 → 4630.54] That would have been cool.
[4630.80 → 4631.98] That would have been a good tie-in.
[4633.04 → 4633.90] Still good though.
[4634.08 → 4634.40] Still good.
[4634.50 → 4634.96] Yeah, that was fun.
[4635.00 → 4636.06] He would have had to say the numbers
[4636.06 → 4637.48] to get that to do that.
[4637.72 → 4638.54] Yeah, that'd be hard.
[4638.66 → 4639.66] You have to have specific numbers
[4639.66 → 4641.50] that maybe Rusty didn't say.
[4641.90 → 4642.14] Yeah.
[4642.60 → 4643.58] When I said cue the music
[4643.58 → 4647.04] I was thinking the song Jump Around though.
[4652.92 → 4654.20] I came to get down.
[4654.32 → 4655.06] I came to get down.
[4655.06 → 4656.44] So get off your feet and jump around.
[4656.58 → 4657.16] I can't get down.
[4657.36 → 4658.44] Get off your feet and jump around.
[4658.72 → 4658.98] That's right.
[4659.54 → 4659.94] There you go.
[4660.00 → 4661.14] Cypress Hill, kids.
[4661.60 → 4662.00] No.
[4662.40 → 4663.44] That's Cypress Hill, isn't it?
[4663.72 → 4667.06] No, that's the leprechauns.
[4668.58 → 4669.02] What?
[4669.46 → 4670.06] Not the leprechauns.
[4671.40 → 4672.12] House of Pain.
[4672.46 → 4672.62] Yeah.
[4672.86 → 4673.32] I told you.
[4673.38 → 4673.98] House of Pain.
[4674.40 → 4675.52] You said Cypress Hill.
[4675.56 → 4676.26] Listen to this.
[4676.54 → 4678.86] It's produced by DJ Mugs of Cypress Hill
[4678.86 → 4680.20] who also covered the song.
[4681.22 → 4681.56] All right?
[4681.84 → 4683.50] So take that.
[4683.78 → 4684.08] What?
[4684.08 → 4684.90] That's right.
[4685.20 → 4685.74] Jump Around.
[4685.74 → 4685.78] Jump Around.
[4685.92 → 4687.66] I don't know about this history.
[4688.00 → 4688.66] School me quickly.
[4689.24 → 4689.50] Okay.
[4690.00 → 4692.20] Jump Around is a song by the American hip-hop group
[4692.20 → 4692.86] House of Pain
[4692.86 → 4695.18] produced by DJ Mugs of Cypress Hill
[4695.18 → 4697.60] who has also covered the song
[4697.60 → 4699.56] and was released in May 1992
[4699.56 → 4701.00] by Tommy Boy and XL
[4701.00 → 4703.14] as the first single from the debut album
[4703.14 → 4704.20] House of Pain.
[4704.20 → 4707.62] So I wasn't wrong.
[4707.74 → 4708.72] I just had it wrong.
[4709.52 → 4709.80] Sort of.
[4710.74 → 4711.52] There's a tie-in.
[4712.48 → 4713.88] There's a reason why I thought Cypress Hill
[4713.88 → 4715.36] but yeah, it's House of Pain.
[4715.58 → 4716.06] That's cool.
[4716.26 → 4716.98] I didn't know that.
[4717.24 → 4717.42] Yeah.
[4718.26 → 4721.34] Glad you messed up but didn't.
[4721.82 → 4722.20] Same.
[4722.54 → 4723.88] I'm always glad when I mess up
[4723.88 → 4725.02] and it's not actually a mess-up.
[4725.78 → 4726.34] All right.
[4726.42 → 4726.96] Who's this?
[4727.08 → 4729.08] Oh, it's only Matt Refer.
[4729.08 → 4730.46] Hello everybody.
[4730.62 → 4731.32] Matt Refer here.
[4731.60 → 4733.08] Just want to say a big thank you
[4733.08 → 4734.78] to everybody that supported us
[4734.78 → 4736.62] with the Go Time podcast
[4736.62 → 4738.84] and everything that I do on Changelog
[4738.84 → 4740.14] and France.
[4740.80 → 4742.26] It's a platform, you know,
[4742.38 → 4744.24] they just make great podcasts
[4744.24 → 4745.70] and I can't wait to see
[4745.70 → 4747.48] what the future of Changelog
[4747.48 → 4748.58] is going to look like.
[4748.80 → 4749.06] Oh, sorry.
[4749.14 → 4749.58] I'm just...
[4749.58 → 4749.90] Oh, what?
[4751.18 → 4752.00] Oh, change...
[4752.00 → 4752.46] Oh, yeah.
[4753.68 → 4754.12] Changelog.
[4754.46 → 4754.94] No, no, no.
[4754.96 → 4755.60] Now you've said it.
[4755.64 → 4756.36] That is really...
[4756.36 → 4757.18] Yeah, it's obvious now
[4757.18 → 4759.06] but I've only seen it written down.
[4759.70 → 4760.30] You're right, change.
[4760.40 → 4760.80] Yeah, okay.
[4761.10 → 4761.92] That's really clever.
[4762.60 → 4763.90] Well, Happy New Year, everyone
[4763.90 → 4765.94] and I hope you let me
[4765.94 → 4766.90] come and be an idiot
[4766.90 → 4769.22] a bit on future podcasts.
[4770.12 → 4771.26] Love you all.
[4771.50 → 4771.86] Bye.
[4772.78 → 4773.18] Wow.
[4773.88 → 4774.46] Changelog.
[4774.94 → 4775.56] Oh, Matt.
[4775.72 → 4776.42] I don't have to say that.
[4776.60 → 4777.76] I don't have to say about that, you know.
[4778.28 → 4778.90] Matt's a character.
[4779.14 → 4779.90] I'll say this.
[4780.08 → 4780.28] Yeah.
[4780.60 → 4782.02] Stay tuned because
[4782.02 → 4783.92] Matt Refer will be
[4783.92 → 4785.26] our very first friend
[4785.26 → 4786.80] of 2025.
[4787.10 → 4788.06] It's already booked, so...
[4788.06 → 4788.70] As it should be.
[4788.70 → 4789.62] It's the way it should be.
[4789.82 → 4790.60] Get with your friends.
[4790.78 → 4792.64] It was the pilot for friends.
[4792.86 → 4793.46] It was.
[4793.84 → 4795.38] It was the inspiration,
[4795.74 → 4796.46] the proving ground,
[4796.82 → 4797.24] so to speak.
[4797.50 → 4798.10] Proving ground, yeah.
[4798.90 → 4800.84] Oh, and Matt's always up to something
[4800.84 → 4801.42] and he is,
[4801.50 → 4802.38] I will tell you this also,
[4802.58 → 4803.46] he is up to something
[4803.46 → 4804.50] for this next episode
[4804.50 → 4805.30] of Changelog and Friends.
[4805.52 → 4805.84] Oh, really?
[4806.10 → 4806.78] He's up to something.
[4807.14 → 4808.42] Do you know what the something is?
[4808.56 → 4809.70] I know a little bit about it
[4809.70 → 4811.18] but I'm not going to say
[4811.18 → 4811.88] any more than that.
[4812.18 → 4813.00] What might it involve?
[4813.00 → 4813.74] Just give him us
[4813.74 → 4815.84] like one hint.
[4816.52 → 4817.64] Off colour if you have to.
[4817.72 → 4817.92] Whatever.
[4818.06 → 4818.48] Not direct.
[4818.72 → 4819.18] Yes and.
[4819.60 → 4819.76] Oh.
[4820.50 → 4821.46] That's so revealing.
[4821.96 → 4822.84] That's so revealing.
[4824.96 → 4825.96] You said it so quickly
[4825.96 → 4827.24] like as if you had it queued up.
[4827.34 → 4827.88] No, I didn't.
[4827.92 → 4828.66] You put me on the spot.
[4828.78 → 4829.04] I thought,
[4829.20 → 4829.84] this is a good hint.
[4830.00 → 4830.64] Is that too much?
[4830.94 → 4831.20] Okay.
[4831.48 → 4831.76] Okay.
[4832.16 → 4832.80] Here's Matt Refer
[4832.80 → 4833.74] remixed.
[4834.24 → 4834.74] Let's do it.
[4834.74 → 4835.90] Hello everybody.
[4836.06 → 4836.76] Matt Refer here.
[4837.10 → 4837.68] Just want to say
[4837.68 → 4838.52] a big thank you
[4838.52 → 4838.98] to everybody
[4838.98 → 4839.74] that's supported
[4839.74 → 4841.10] Changelog and Friends.
[4842.24 → 4842.82] You know,
[4842.96 → 4844.82] they just make great podcasts.
[4844.94 → 4845.32] Tu said,
[4845.66 → 4846.32] ILS font just
[4846.32 → 4847.34] d'excellence podcasts.
[4847.70 → 4848.52] And I can't wait
[4848.52 → 4850.02] to see what the future
[4850.02 → 4850.92] of Changelog
[4850.92 → 4851.84] is going to look like.
[4851.88 → 4852.62] J'ai hate devoir
[4852.62 → 4853.54] à quoit resemble
[4853.54 → 4854.70] l'avenge Du Changelog.
[4854.80 → 4855.66] Happy New Year everyone
[4855.66 → 4857.72] and I hope you let me
[4857.72 → 4858.68] come and be an idiot
[4858.68 → 4860.94] a bit on the future podcasts.
[4861.16 → 4862.02] Bone Anne à thus
[4862.02 → 4863.70] et j'Esper Que vows me lasered
[4863.70 → 4864.26] un EU idiot
[4864.26 → 4865.44] SUR l's future podcasts.
[4865.66 → 4866.62] Love you all.
[4866.88 → 4867.24] Bye.
[4867.60 → 4868.52] JE vows AIME thus.
[4869.94 → 4870.46] Au Renoir.
[4879.14 → 4880.36] I told you BMC
[4880.36 → 4881.04] has some new toys.
[4881.36 → 4882.26] I'm just not sure
[4882.26 → 4883.14] what this show has become.
[4883.44 → 4884.88] I think it might be
[4884.88 → 4885.84] like a show-off centre
[4885.84 → 4886.92] for Break master Cylinder
[4886.92 → 4889.00] and then obviously
[4889.00 → 4889.66] a show-off centre
[4889.66 → 4890.54] for our listeners.
[4891.42 → 4892.84] Very much not about us at all.
[4892.96 → 4893.78] At the very, yeah.
[4893.78 → 4895.14] At least a playground, yeah.
[4895.20 → 4896.12] I keep trying to talk
[4896.12 → 4897.10] and I keep being cut off
[4897.10 → 4897.78] by these voicemails.
[4901.78 → 4902.58] Well, there's something
[4902.58 → 4903.54] poetic about that.
[4903.98 → 4904.32] Matt.
[4904.60 → 4905.74] Oh, I'm looking forward to it.
[4906.02 → 4906.96] I'm looking forward to it.
[4907.04 → 4907.52] I should say
[4907.52 → 4908.60] we might have to bleep that
[4908.60 → 4909.30] but I wouldn't know.
[4909.40 → 4909.96] I have no idea
[4909.96 → 4910.58] what she was saying.
[4910.68 → 4911.20] I assume
[4911.20 → 4912.82] it was what Matt was saying
[4912.82 → 4913.90] in French.
[4914.24 → 4914.98] It's possible.
[4915.34 → 4916.14] I have no idea.
[4916.24 → 4916.98] So if you knew,
[4917.06 → 4918.10] if you can hear that
[4918.10 → 4919.80] and translate it for us.
[4919.98 → 4920.64] I'll have my daughter
[4920.64 → 4921.12] listen to it.
[4921.12 → 4921.76] She speaks French.
[4921.76 → 4922.12] Okay.
[4922.50 → 4922.76] Yeah.
[4923.18 → 4924.64] We've reached our final caller.
[4925.26 → 4926.54] Any guesses, Adam,
[4926.58 → 4927.26] on who it might be?
[4927.32 → 4928.14] The person that might
[4928.14 → 4929.06] leave a voicemail
[4929.06 → 4930.52] at the very last moment.
[4930.76 → 4931.72] Give me a second.
[4932.50 → 4933.02] Need a hint?
[4933.42 → 4933.74] Sure.
[4934.12 → 4935.06] It's the same as
[4935.06 → 4936.26] the last caller last year.
[4937.14 → 4937.98] It's a big hint.
[4938.52 → 4939.28] Unless you didn't make it
[4939.28 → 4940.02] to the end of the show
[4940.02 → 4940.64] before you fell asleep.
[4940.66 → 4941.22] I fell asleep.
[4941.76 → 4942.92] I fell asleep.
[4943.88 → 4944.96] Jamie Tana.
[4945.04 → 4946.14] Oh gosh, yes.
[4946.14 → 4946.70] Jamie Tana.
[4947.00 → 4947.78] Just in time Jamie.
[4947.88 → 4948.52] That's what we call him.
[4948.52 → 4948.96] Really?
[4950.96 → 4952.08] I just made that up
[4952.08 → 4952.54] on the spot.
[4953.14 → 4953.70] I love it.
[4954.10 → 4954.68] Yeah, that's nice.
[4954.86 → 4955.26] It's so,
[4956.36 → 4956.76] yeah,
[4956.88 → 4957.58] I was going to make
[4957.58 → 4958.20] a timing joke,
[4958.26 → 4959.48] but I can't find my words.
[4959.90 → 4960.08] Yeah.
[4960.34 → 4960.64] All right.
[4960.66 → 4961.74] Well, let's hear from Jamie then.
[4962.16 → 4962.80] Hey, Adam and Jared.
[4963.04 → 4963.96] It's Jamie Tana here.
[4964.26 → 4964.96] Thanks for another
[4964.96 → 4966.00] awesome year
[4966.00 → 4967.40] of Changelog.
[4968.06 → 4968.72] Plus, plus,
[4968.88 → 4969.28] it is
[4969.28 → 4970.88] so much better.
[4971.32 → 4971.84] So much better.
[4972.50 → 4972.92] I think
[4972.92 → 4974.02] I'm making this
[4974.02 → 4974.54] a tradition
[4974.54 → 4975.46] of me
[4975.46 → 4976.46] submitting late,
[4976.66 → 4977.38] so I'm
[4977.38 → 4978.22] sorry again.
[4978.98 → 4979.66] But hopefully
[4979.66 → 4980.36] I managed to make it
[4980.36 → 4980.78] in time.
[4981.10 → 4981.86] I probably didn't,
[4982.04 → 4983.08] but we'll find out
[4983.08 → 4983.60] this week.
[4984.36 → 4985.30] I think that's probably
[4985.30 → 4985.76] a good segue
[4985.76 → 4987.26] into what my favourite
[4987.26 → 4988.00] episode of the year
[4988.00 → 4988.36] has been,
[4988.76 → 4989.40] which I'm probably
[4989.40 → 4990.36] a little bit biased
[4990.36 → 4991.30] because it was me.
[4991.92 → 4992.60] In February,
[4992.70 → 4993.32] I joined you
[4993.32 → 4994.96] on Friends 31
[4994.96 → 4996.22] to talk about
[4996.22 → 4996.88] being public,
[4997.30 → 4998.52] how ADHD affects me,
[4998.62 → 4999.82] including being late
[4999.82 → 5000.86] to submitting things
[5000.86 → 5001.24] like this,
[5002.02 → 5003.00] dependency management data,
[5003.56 → 5004.52] and also kick-started
[5004.52 → 5005.40] my podcast career
[5005.40 → 5006.58] where I
[5006.58 → 5007.62] followed up
[5007.62 → 5008.18] with a conversation
[5008.18 → 5009.08] on Go Time
[5009.08 → 5010.74] in episode 328
[5010.74 → 5011.76] about OpenAI.
[5012.12 → 5012.82] But enough about me.
[5013.18 → 5014.10] This year has been
[5014.10 → 5015.32] an epic year
[5015.32 → 5016.00] for Changelog,
[5016.16 → 5016.66] in particular
[5016.66 → 5017.50] the first year
[5017.50 → 5018.08] of Friends
[5018.08 → 5019.60] in full,
[5019.80 → 5020.32] which I've been
[5020.32 → 5021.36] incredibly,
[5021.62 → 5022.38] thoroughly enjoying.
[5022.86 → 5023.42] Which you may be able
[5023.42 → 5023.70] to guess
[5023.70 → 5024.34] from me listening
[5024.34 → 5024.92] to a whopping
[5024.92 → 5026.70] 45 episodes
[5026.70 → 5027.20] this year,
[5027.42 → 5028.08] including one
[5028.08 → 5028.76] that I finished
[5028.76 → 5029.74] listening to this morning.
[5029.74 → 5030.56] Some of my favourite
[5030.56 → 5031.66] episodes this year,
[5032.20 → 5033.22] especially in Friends,
[5033.36 → 5034.50] have been the new
[5034.50 → 5036.42] Hashtag Prime episodes,
[5037.08 → 5038.36] Friends 47 and 59,
[5038.72 → 5039.00] which have been
[5039.00 → 5040.04] really fun listening
[5040.04 → 5041.44] on my own,
[5041.46 → 5042.30] but also with my partner.
[5042.64 → 5043.34] It's a fun,
[5043.42 → 5043.76] different thing
[5043.76 → 5044.62] to listen to.
[5044.86 → 5045.90] As well as meeting
[5045.90 → 5046.92] some really awesome
[5046.92 → 5047.72] and interesting people
[5047.72 → 5048.32] at the different
[5048.32 → 5049.12] hallway tracks
[5049.12 → 5049.88] at conferences
[5049.88 → 5050.46] you've been at.
[5050.62 → 5051.66] I also really enjoyed
[5051.66 → 5052.72] listening to
[5052.72 → 5053.44] Adam and Jared
[5053.44 → 5054.28] solo,
[5054.70 → 5055.76] either in Friends 70
[5055.76 → 5056.48] or the Plus
[5056.48 → 5057.28] special episode
[5057.28 → 5058.64] at Build 2024.
[5058.64 → 5060.48] And hearing a bit
[5060.48 → 5061.54] more from the two
[5061.54 → 5061.86] of you,
[5062.24 → 5062.84] because we always
[5062.84 → 5064.28] hear from your
[5064.28 → 5064.74] point of view
[5064.74 → 5065.72] from behind the mic.
[5066.58 → 5067.26] Data-wise,
[5067.42 → 5069.16] I've been split
[5069.16 → 5070.32] on Go Time
[5070.32 → 5070.86] and interviews,
[5071.04 → 5072.10] listening to 38
[5072.10 → 5072.98] podcasts apiece
[5072.98 → 5073.48] this year,
[5074.08 → 5074.70] and then ship it
[5074.70 → 5075.18] just behind
[5075.18 → 5076.30] on 35 lessons.
[5077.10 → 5077.72] In total,
[5077.90 → 5078.38] according to my
[5078.38 → 5079.00] podcast app,
[5079.10 → 5079.74] in 2024,
[5080.04 → 5080.62] I've listened to
[5080.62 → 5081.32] eight days'
[5081.42 → 5082.02] worth of podcasts
[5082.02 → 5082.44] with you all.
[5082.96 → 5083.68] It's been great,
[5084.08 → 5086.24] but it's bittersweet
[5086.24 → 5087.26] with the news
[5087.26 → 5087.64] of the change
[5087.64 → 5088.42] of podcasting.
[5088.64 → 5089.08] universe.
[5090.02 → 5090.60] I'm cautiously
[5090.60 → 5091.40] optimistic for the
[5091.40 → 5091.70] future,
[5091.94 → 5092.34] and I hope
[5092.34 → 5093.32] that in the
[5093.32 → 5093.78] coming year,
[5094.46 → 5095.00] I'll be having
[5095.00 → 5095.76] some similar
[5095.76 → 5096.42] numbers across
[5096.42 → 5097.20] the whole podcast
[5097.20 → 5097.68] universe.
[5098.40 → 5099.34] Just quickly to go
[5099.34 → 5100.80] back to interviews,
[5101.18 → 5102.10] there's been some
[5102.10 → 5103.16] really incredible
[5103.16 → 5103.96] interviews this
[5103.96 → 5104.48] last year,
[5105.14 → 5105.90] but to give
[5105.90 → 5107.02] just three of
[5107.02 → 5107.94] my top ones,
[5108.66 → 5109.38] Brian Cantwell
[5109.38 → 5111.06] in interviews
[5111.06 → 5112.08] 592,
[5113.14 → 5113.64] Akin from
[5113.64 → 5114.14] Hack Club
[5114.14 → 5114.96] in interviews
[5114.96 → 5115.52] 620,
[5115.52 → 5117.14] Danny Thompson
[5117.14 → 5118.20] in interviews
[5118.20 → 5118.82] 617.
[5119.56 → 5120.38] A bunch of
[5120.38 → 5121.44] fascinating
[5121.44 → 5122.14] and diverse
[5122.14 → 5122.84] thoughts,
[5123.30 → 5124.04] and yeah,
[5124.18 → 5125.72] I've loved the
[5125.72 → 5126.12] way that you
[5126.12 → 5127.10] have just some
[5127.10 → 5127.78] really incredible
[5127.78 → 5128.84] people from
[5128.84 → 5129.62] different walks of
[5129.62 → 5129.84] life,
[5130.08 → 5130.78] different stages of
[5130.78 → 5131.10] career,
[5131.94 → 5133.48] different viewpoints.
[5133.48 → 5134.56] I'm going to
[5134.56 → 5134.98] stop rambling
[5134.98 → 5135.34] now,
[5135.78 → 5136.06] but I want to
[5136.06 → 5136.98] say thanks again
[5136.98 → 5138.02] to all the
[5138.02 → 5138.76] many,
[5138.86 → 5139.24] many folk
[5139.24 → 5140.58] who have
[5140.58 → 5141.78] contributed to
[5141.78 → 5142.74] another really
[5142.74 → 5144.08] great year of
[5144.08 → 5144.28] Change.
[5144.44 → 5144.84] Plus,
[5145.46 → 5146.18] it is better,
[5146.62 → 5147.60] but it's so much
[5147.60 → 5147.84] better,
[5148.04 → 5148.42] it's been better
[5148.42 → 5148.94] for years,
[5149.68 → 5150.16] getting on it.
[5150.58 → 5151.50] I love how
[5151.50 → 5152.64] it's better
[5152.64 → 5153.56] has become a
[5153.56 → 5153.82] thing,
[5154.22 → 5155.18] like an
[5155.18 → 5155.56] unstoppable
[5155.56 → 5156.10] freight train.
[5156.66 → 5157.46] I love that
[5157.46 → 5158.58] it's so recycled
[5158.58 → 5159.10] throughout,
[5159.38 → 5160.88] it's a dumb
[5160.88 → 5161.46] thing I said
[5161.46 → 5161.90] one time,
[5161.96 → 5162.56] just like messing
[5162.56 → 5162.98] around,
[5163.20 → 5163.50] you know,
[5163.82 → 5165.56] and it stuck,
[5165.98 → 5167.10] and my kids
[5167.10 → 5168.84] mimic it as well,
[5169.12 → 5169.72] my youngest,
[5169.84 → 5170.52] my five-year-old,
[5171.26 → 5171.42] they,
[5171.66 → 5171.80] you know,
[5171.82 → 5172.26] in their kid
[5172.26 → 5172.64] voice,
[5173.08 → 5173.40] Change.
[5173.40 → 5173.74] Plus,
[5173.84 → 5173.86] plus,
[5173.86 → 5174.10] plus,
[5174.14 → 5174.60] it's better,
[5174.76 → 5174.94] you know,
[5174.94 → 5175.38] they hold their
[5175.38 → 5175.82] nose,
[5175.96 → 5176.20] because they
[5176.20 → 5176.78] make it sound
[5176.78 → 5177.40] nasally for some
[5177.40 → 5177.62] reason,
[5177.82 → 5178.82] I'm not sure to
[5178.82 → 5179.02] be,
[5179.28 → 5179.70] if I should be
[5179.70 → 5180.40] offended or not,
[5180.50 → 5181.38] but the Danny
[5181.38 → 5182.00] Thompson one,
[5182.46 → 5183.12] I like that,
[5183.24 → 5184.38] I'm glad that
[5184.38 → 5185.22] got out there.
[5185.58 → 5185.80] Yeah,
[5185.90 → 5186.34] that one almost
[5186.34 → 5186.78] didn't make it
[5186.78 → 5187.08] out.
[5187.38 → 5187.58] Yeah,
[5187.90 → 5188.28] it's,
[5188.72 → 5189.40] it was,
[5189.90 → 5190.36] can you talk
[5190.36 → 5191.02] about the
[5191.02 → 5192.28] the travels,
[5192.42 → 5192.52] the
[5192.56 → 5193.30] data had to go
[5193.30 → 5193.92] through to get
[5193.92 → 5195.04] to us to become
[5195.04 → 5196.04] an MP3 on the
[5196.04 → 5196.50] air waves?
[5196.96 → 5197.82] I'm holding it in
[5197.82 → 5198.38] my hand,
[5198.88 → 5199.36] which you would
[5199.36 → 5199.96] see if we had
[5199.96 → 5200.54] video first
[5200.54 → 5200.94] production,
[5202.04 → 5203.34] a Nick Geese
[5203.34 → 5204.20] hard drive,
[5204.66 → 5205.60] which holds
[5205.60 → 5206.22] something like
[5206.22 → 5207.80] 35 gigabytes
[5207.80 → 5210.16] of film,
[5210.94 → 5211.58] the proverbial
[5211.58 → 5211.82] film,
[5211.92 → 5212.40] not actual film,
[5213.24 → 5214.06] from our,
[5214.20 → 5215.24] of stuff at
[5215.24 → 5215.98] that conference,
[5216.76 → 5217.92] and this had to
[5217.92 → 5218.64] come by way,
[5218.84 → 5219.56] we were at that
[5219.56 → 5220.00] conference in
[5220.00 → 5220.32] Austin,
[5220.48 → 5221.02] Texas,
[5221.02 → 5221.68] our Danny
[5221.68 → 5221.90] Thompson
[5221.90 → 5222.44] interview is
[5222.44 → 5223.06] on here,
[5223.26 → 5225.32] and it took
[5225.32 → 5225.72] a long time
[5225.72 → 5226.06] to get it
[5226.06 → 5226.52] gathered together,
[5226.58 → 5226.86] I'm not sure
[5226.86 → 5227.12] of the whole
[5227.12 → 5227.44] story,
[5227.68 → 5228.10] but Clark
[5228.10 → 5229.12] Sell diligently
[5229.12 → 5230.34] gathered,
[5230.74 → 5231.08] it was just
[5231.08 → 5231.48] too much to
[5231.48 → 5232.02] just send us,
[5232.06 → 5232.28] I mean,
[5232.34 → 5232.82] that's a lot
[5232.82 → 5233.90] of data,
[5234.80 → 5235.28] and so the
[5235.28 → 5235.96] idea was like
[5235.96 → 5236.70] sneaker net,
[5236.76 → 5237.08] I guess,
[5237.12 → 5237.52] for the win,
[5237.60 → 5238.86] and so Clark
[5238.86 → 5240.34] saw Nick at
[5240.34 → 5240.98] the Summers
[5240.98 → 5241.60] that conference
[5241.60 → 5242.16] in Wisconsin,
[5242.30 → 5242.72] so there's two
[5242.72 → 5243.44] that conferences,
[5244.36 → 5244.58] Austin,
[5244.68 → 5244.92] Texas,
[5245.08 → 5245.72] and Wisconsin
[5245.72 → 5246.36] Dells,
[5246.36 → 5248.52] and Nick
[5248.52 → 5248.88] happened to
[5248.88 → 5249.08] have his
[5249.08 → 5249.36] hard drive
[5249.36 → 5249.66] on him,
[5249.98 → 5250.58] so Clark
[5250.58 → 5251.06] gave him
[5251.06 → 5251.60] the 35
[5251.60 → 5252.00] gigs or
[5252.00 → 5252.36] whatever it
[5252.36 → 5252.64] is,
[5253.08 → 5253.58] and put it
[5253.58 → 5253.70] on the
[5253.70 → 5254.20] hard drive,
[5254.36 → 5254.64] I actually
[5254.64 → 5254.94] think it's
[5254.94 → 5255.30] more than
[5255.30 → 5255.52] that,
[5255.58 → 5255.86] now that I'm
[5255.86 → 5256.24] saying it,
[5256.28 → 5256.52] it's something
[5256.52 → 5257.02] ridiculous,
[5257.12 → 5257.66] like 500
[5257.66 → 5258.04] gigabytes,
[5259.04 → 5259.56] it was just
[5259.56 → 5260.08] too much to
[5260.08 → 5260.74] just put on
[5260.74 → 5261.30] the Dropbox
[5261.30 → 5261.62] or something,
[5261.70 → 5261.94] I guess,
[5262.60 → 5263.78] and Nick
[5263.78 → 5264.66] sneaker netted it
[5264.66 → 5265.34] via an airplane
[5265.34 → 5266.12] back to his
[5266.12 → 5266.42] house,
[5266.68 → 5267.16] and then I
[5267.16 → 5267.48] had lunch
[5267.48 → 5267.82] with him,
[5267.90 → 5268.14] because you
[5268.14 → 5268.24] know,
[5268.28 → 5269.02] Nick and
[5269.02 → 5269.38] I both
[5269.38 → 5270.12] live in
[5270.12 → 5270.56] the Omaha,
[5270.72 → 5271.02] Nebraska
[5271.02 → 5271.46] area,
[5271.58 → 5271.92] I'm in
[5271.92 → 5272.34] Bennington,
[5272.90 → 5273.24] which is
[5273.24 → 5273.90] northwest of
[5273.90 → 5274.12] Omaha,
[5274.26 → 5274.48] and he's
[5274.48 → 5274.98] in Bellevue,
[5275.24 → 5275.76] which is
[5275.76 → 5275.98] kind of
[5275.98 → 5276.44] southeast
[5276.44 → 5276.78] Omaha,
[5276.96 → 5277.36] so we
[5277.36 → 5277.64] aren't
[5277.64 → 5278.32] super close
[5278.32 → 5278.60] together,
[5278.68 → 5279.20] probably a
[5279.20 → 5279.66] 40 minute
[5279.66 → 5280.28] drive if
[5280.28 → 5280.42] he was
[5280.42 → 5280.54] going to
[5280.54 → 5280.80] come to
[5280.80 → 5281.30] my house,
[5281.50 → 5282.00] but we
[5282.00 → 5282.20] meet in
[5282.20 → 5282.40] the middle
[5282.40 → 5282.58] and have
[5282.58 → 5282.76] lunch
[5282.76 → 5283.12] sometimes,
[5283.42 → 5283.76] and so he
[5283.76 → 5284.02] brought me
[5284.02 → 5284.58] this to
[5284.58 → 5284.90] lunch,
[5284.98 → 5285.30] and I
[5285.30 → 5285.64] went through
[5285.64 → 5285.84] it,
[5285.90 → 5286.10] and I
[5286.10 → 5286.56] extracted
[5286.56 → 5286.82] it,
[5286.90 → 5287.16] and I
[5287.16 → 5287.42] gave it
[5287.42 → 5287.86] to Jason,
[5288.64 → 5289.30] our editor,
[5289.90 → 5290.52] and Jason
[5290.52 → 5291.04] did his best
[5291.04 → 5291.38] with it,
[5291.42 → 5291.62] and he
[5291.62 → 5291.96] handed it
[5291.96 → 5292.38] to you,
[5292.46 → 5292.72] and we
[5292.72 → 5292.92] said,
[5293.00 → 5293.26] can we
[5293.26 → 5293.66] ship this
[5293.66 → 5294.02] interview,
[5294.36 → 5294.60] and you
[5294.60 → 5294.76] know,
[5294.90 → 5295.38] the audio
[5295.38 → 5295.94] wasn't
[5295.94 → 5296.76] our
[5296.76 → 5297.18] standard
[5297.18 → 5297.60] quality,
[5297.72 → 5297.92] and so
[5297.92 → 5298.14] there were
[5298.14 → 5298.26] some
[5298.26 → 5298.76] questions,
[5299.20 → 5299.66] and it
[5299.66 → 5299.98] wasn't that
[5299.98 → 5300.28] long,
[5300.36 → 5300.62] honestly,
[5300.68 → 5300.86] it was
[5300.86 → 5301.06] kind of
[5301.06 → 5301.34] a shorter
[5301.34 → 5301.76] episode,
[5302.22 → 5302.68] and so
[5302.68 → 5303.04] we actually
[5303.04 → 5303.58] almost
[5303.58 → 5305.02] deposited
[5305.02 → 5305.10] it,
[5305.16 → 5305.38] didn't we,
[5305.48 → 5305.56] Adam?
[5306.78 → 5307.38] We came
[5307.38 → 5307.90] close,
[5308.42 → 5309.64] we almost
[5309.64 → 5310.18] deposited it
[5310.18 → 5310.52] because we
[5310.52 → 5311.16] thought about,
[5311.54 → 5313.04] what was it
[5313.04 → 5313.56] about it?
[5313.78 → 5313.96] Well,
[5313.98 → 5314.30] it didn't
[5314.30 → 5315.50] sound amazing,
[5315.50 → 5316.34] and it was a
[5316.34 → 5316.60] little bit
[5316.60 → 5317.50] shorter than
[5317.50 → 5317.98] we normally
[5317.98 → 5318.20] do,
[5318.40 → 5319.06] and we
[5319.06 → 5319.24] thought,
[5319.36 → 5319.54] well,
[5319.66 → 5320.00] wouldn't we
[5320.00 → 5320.42] just get
[5320.42 → 5321.02] Danny back
[5321.02 → 5321.58] on the pod
[5321.58 → 5321.90] and just
[5321.90 → 5322.38] do it
[5322.38 → 5323.02] fresh,
[5323.32 → 5323.64] like a
[5323.64 → 5324.18] real episode,
[5324.34 → 5325.28] which was
[5325.38 → 5325.78] another route
[5325.78 → 5326.04] we could
[5326.04 → 5326.36] have gone,
[5326.50 → 5326.76] but you
[5326.76 → 5326.90] know,
[5327.08 → 5327.54] this is a
[5327.54 → 5327.84] business,
[5327.98 → 5328.42] we do put
[5328.42 → 5328.88] shows out
[5328.88 → 5329.18] on the
[5329.18 → 5329.46] weekly,
[5329.60 → 5329.76] and we
[5329.76 → 5330.06] needed a
[5330.06 → 5330.36] show that
[5330.36 → 5330.62] week,
[5330.88 → 5331.18] so it's
[5331.18 → 5331.40] like,
[5331.52 → 5332.08] that was
[5332.08 → 5332.34] definitely
[5332.34 → 5332.92] part of
[5332.92 → 5333.34] the decision
[5333.34 → 5333.94] making process,
[5334.04 → 5334.32] we can't
[5334.32 → 5334.72] act like it
[5334.72 → 5335.02] wasn't,
[5335.36 → 5335.84] we have
[5335.84 → 5336.86] sponsors who
[5336.86 → 5337.42] count on us
[5337.42 → 5337.72] to put
[5337.72 → 5338.16] shows out,
[5338.28 → 5338.68] and so it's
[5338.68 → 5338.92] like,
[5339.12 → 5339.70] can this be
[5339.70 → 5340.14] a standalone
[5340.14 → 5340.58] episode,
[5341.18 → 5341.48] and I'm
[5341.48 → 5341.98] glad that at
[5341.98 → 5342.44] least for
[5342.44 → 5342.84] Jamie,
[5343.02 → 5343.64] it was one
[5343.64 → 5343.98] of the best
[5343.98 → 5344.56] of the year,
[5345.36 → 5345.82] hopefully other
[5345.82 → 5346.14] people liked
[5346.14 → 5346.44] it too.
[5346.82 → 5347.20] Danny was
[5347.20 → 5348.20] over the moon
[5348.20 → 5348.90] because I saw
[5348.90 → 5349.62] Danny at
[5349.62 → 5350.52] All Things
[5350.52 → 5350.78] open,
[5350.86 → 5351.22] I told him,
[5351.26 → 5351.62] I don't think
[5351.62 → 5351.92] we're going to
[5351.92 → 5352.24] get that
[5352.24 → 5352.86] episode out,
[5353.34 → 5353.84] and thankfully
[5353.84 → 5354.54] it was about
[5354.54 → 5355.26] his life story
[5355.26 → 5355.74] more than it
[5355.74 → 5356.24] was about
[5356.24 → 5357.16] current events
[5357.16 → 5357.54] or anything
[5357.54 → 5357.96] because it
[5357.96 → 5358.36] was last
[5358.36 → 5358.98] January that
[5358.98 → 5359.38] we recorded
[5359.38 → 5359.62] it,
[5359.82 → 5360.98] so it was
[5360.98 → 5362.02] pretty much
[5362.02 → 5362.56] evergreen.
[5362.98 → 5363.00] Well,
[5363.10 → 5363.66] this January,
[5363.90 → 5364.30] last January,
[5364.48 → 5364.76] if you're
[5364.76 → 5365.04] listening to
[5365.04 → 5365.16] this in
[5365.16 → 5365.50] 2025,
[5365.78 → 5366.24] last January.
[5366.62 → 5367.32] January of
[5367.32 → 5367.86] 24.
[5368.36 → 5368.68] Yes.
[5369.84 → 5370.48] Gotta give
[5370.48 → 5371.04] to get back.
[5371.68 → 5371.84] Yeah,
[5371.90 → 5372.40] gotta give.
[5372.42 → 5372.78] Gotta give to
[5372.78 → 5373.24] get back.
[5373.46 → 5374.12] To get back.
[5374.20 → 5374.58] I'm glad we
[5374.58 → 5374.92] got it out
[5374.92 → 5375.28] there because
[5375.28 → 5376.12] I think that
[5376.12 → 5377.06] I don't know
[5377.06 → 5377.80] Danny's full
[5377.80 → 5378.48] story aside from
[5378.48 → 5379.12] what we had
[5379.12 → 5379.54] shared there,
[5379.60 → 5380.14] but I think
[5380.14 → 5381.62] he had been
[5381.62 → 5382.86] newer or
[5382.86 → 5383.48] newish to
[5383.48 → 5384.02] sharing his
[5384.02 → 5384.28] story,
[5384.38 → 5384.92] especially on
[5384.92 → 5385.42] stage.
[5386.50 → 5387.36] I think since
[5387.36 → 5387.90] then he's had
[5387.90 → 5388.44] more reps,
[5389.32 → 5390.10] and so we
[5390.10 → 5390.70] actually may be
[5390.70 → 5391.10] late to the
[5391.10 → 5391.70] party in terms
[5391.70 → 5392.32] of sharing
[5392.32 → 5392.86] that story.
[5393.34 → 5393.66] Sure.
[5393.96 → 5394.42] But obviously
[5394.42 → 5395.18] sharing it on
[5395.18 → 5396.88] the conference
[5396.88 → 5397.30] stage,
[5397.36 → 5397.90] so to set
[5397.90 → 5398.26] the stage a
[5398.26 → 5398.62] bit more
[5398.62 → 5400.22] elongated but
[5400.22 → 5400.54] shortened,
[5401.30 → 5402.04] is that even
[5402.04 → 5402.42] a thing?
[5402.64 → 5403.02] I don't know.
[5403.02 → 5404.10] Is we were
[5404.10 → 5404.64] on stage with
[5404.64 → 5404.90] Danny.
[5405.80 → 5406.66] Did we pass
[5406.66 → 5407.20] the mic back
[5407.20 → 5407.66] and forth?
[5407.96 → 5408.56] I don't think
[5408.56 → 5408.84] so.
[5409.12 → 5409.26] Yeah,
[5409.30 → 5409.44] okay.
[5409.50 → 5409.78] I think we
[5409.78 → 5410.20] each had our
[5410.20 → 5410.80] own mics,
[5410.90 → 5411.10] but they were
[5411.10 → 5411.82] handheld mics.
[5411.92 → 5412.16] They weren't
[5412.16 → 5412.88] like stationary
[5412.88 → 5413.24] mics.
[5413.34 → 5413.66] We had them
[5413.66 → 5414.76] handheld so we
[5414.76 → 5415.60] can pull them
[5415.60 → 5416.00] away from our
[5416.00 → 5416.22] face.
[5416.30 → 5416.58] There's no
[5416.58 → 5417.08] breath going
[5417.08 → 5417.42] on.
[5417.84 → 5418.08] And then we
[5418.08 → 5418.36] had some
[5418.36 → 5419.84] Q&A afterwards,
[5420.10 → 5420.40] and so the
[5420.40 → 5420.90] Q&A didn't
[5420.90 → 5421.88] fit, and so
[5421.88 → 5422.18] if you're at
[5422.18 → 5422.64] the conference,
[5422.72 → 5423.02] it was a
[5423.02 → 5423.32] lengthy
[5423.32 → 5424.04] conversation
[5424.04 → 5424.90] with more
[5424.90 → 5425.42] context.
[5425.78 → 5426.72] As a podcast,
[5426.82 → 5427.28] the Q&A just
[5427.28 → 5428.34] didn't fit because
[5428.34 → 5429.14] it was so
[5429.14 → 5430.80] contextual to the
[5430.80 → 5431.66] conference and
[5431.66 → 5432.60] the screens in
[5432.60 → 5433.08] front of us,
[5433.10 → 5433.38] and so it
[5433.38 → 5434.02] just made sense
[5434.02 → 5435.38] to trim that.
[5436.34 → 5436.92] But I'm glad
[5436.92 → 5437.46] we got it out.
[5437.46 → 5438.46] I'm glad that
[5438.46 → 5439.56] the sneaker
[5439.56 → 5440.28] net worked out.
[5440.54 → 5441.64] I'm glad Nick
[5441.64 → 5442.62] had his hard
[5442.62 → 5442.90] drive.
[5443.02 → 5443.78] I'm glad Clark
[5443.78 → 5444.36] Sell came
[5444.36 → 5444.68] through and
[5444.68 → 5445.22] got us the
[5445.22 → 5446.26] data.
[5446.96 → 5447.72] And even if
[5447.72 → 5448.10] it was
[5448.10 → 5448.64] published,
[5449.54 → 5449.68] you know,
[5449.70 → 5450.24] recorded January
[5450.24 → 5450.96] 30th and
[5450.96 → 5451.54] published November
[5451.54 → 5452.58] 14th, that's
[5452.58 → 5452.82] cool.
[5453.12 → 5453.62] At least we
[5453.62 → 5454.04] still shipped
[5454.04 → 5454.42] it, you know.
[5455.34 → 5457.58] And it was
[5457.58 → 5457.86] awesome.
[5458.18 → 5458.78] I dug it.
[5459.38 → 5459.66] All right,
[5459.72 → 5460.30] Jamie, thank
[5460.30 → 5461.06] you as always
[5461.06 → 5463.36] for calling in
[5463.36 → 5464.20] just in time.
[5464.60 → 5465.24] Just in time.
[5465.38 → 5466.24] Here is your
[5466.24 → 5467.14] Break master,
[5467.14 → 5467.66] Cylinder
[5467.66 → 5468.26] Remix.
[5469.46 → 5470.46] This year has
[5470.46 → 5471.68] been an epic
[5471.68 → 5472.04] year.
[5472.30 → 5473.10] Awesome year.
[5473.58 → 5474.04] Awesome and
[5474.04 → 5474.34] interesting.
[5474.76 → 5475.32] Pretty fun.
[5475.74 → 5476.42] It's been great.
[5477.00 → 5477.60] A bunch of
[5477.60 → 5478.68] fascinating
[5478.68 → 5479.20] and diverse
[5479.20 → 5479.92] thoughts.
[5480.70 → 5481.34] Really incredible.
[5482.60 → 5483.56] So much better.
[5483.94 → 5484.52] So much better.
[5484.70 → 5485.28] So much better.
[5485.56 → 5486.04] Been better for
[5486.04 → 5486.38] years.
[5486.82 → 5487.30] Getting on it.
[5488.88 → 5489.54] But enough
[5489.54 → 5489.98] about me.
[5489.98 → 5498.38] That one smacks.
[5498.50 → 5498.92] So much better
[5498.92 → 5499.54] for years.
[5499.82 → 5500.34] That beats a
[5500.34 → 5500.60] banger.
[5501.28 → 5501.56] Check the
[5501.56 → 5502.06] scoreboard.
[5502.44 → 5502.70] The numbers
[5502.70 → 5503.14] don't lie.
[5504.10 → 5504.80] I reversed it.
[5505.08 → 5505.36] What'd you
[5505.36 → 5505.74] reverse?
[5506.24 → 5506.80] Well, it's
[5506.80 → 5508.22] actually the
[5508.22 → 5508.58] numbers don't
[5508.58 → 5508.78] lie.
[5508.88 → 5509.10] Check the
[5509.10 → 5509.50] scoreboard.
[5509.88 → 5510.24] Oh, I don't
[5510.24 → 5510.46] know the
[5510.46 → 5510.70] saying.
[5511.26 → 5511.50] Dude.
[5512.16 → 5512.60] Shabby!
[5512.60 → 5512.90] Shabby!
[5513.38 → 5513.96] Excuse me?
[5514.54 → 5514.88] Can't do
[5514.88 → 5515.14] night.
[5517.30 → 5518.14] It's Jay-Z.
[5518.68 → 5519.50] That's a Jay-Z
[5519.50 → 5519.80] line?
[5519.98 → 5520.54] Yeah, man.
[5520.70 → 5521.10] Here's my
[5521.10 → 5521.58] concern with
[5521.58 → 5521.96] Jay-Z.
[5522.22 → 5523.46] I like the
[5523.46 → 5524.20] man's music and
[5524.20 → 5525.36] everything and
[5525.36 → 5526.02] Shabby certainly
[5526.02 → 5526.72] comes from it, but
[5526.72 → 5527.46] it turns out he
[5527.46 → 5528.40] might be a really
[5528.40 → 5529.08] awful person.
[5529.44 → 5530.10] Turns out.
[5530.26 → 5530.82] Yeah, well, you
[5530.82 → 5531.34] know, the Pete
[5531.34 → 5532.06] Daddy tapes are
[5532.06 → 5533.84] dropping and Jay-Z
[5533.84 → 5534.58] maybe implicated
[5534.58 → 5535.60] some seriously
[5535.60 → 5536.96] wicked stuff.
[5537.34 → 5538.16] And not wicked in
[5538.16 → 5538.82] the Boston accent
[5538.82 → 5539.36] kind of way.
[5539.76 → 5540.48] Wicked smart.
[5540.90 → 5541.38] Wicked bad.
[5541.38 → 5541.96] Wicked smart.
[5542.30 → 5542.82] Wicked bad.
[5543.18 → 5543.42] Yeah.
[5543.42 → 5544.08] So anyway,
[5544.34 → 5545.40] distancing myself
[5545.40 → 5545.82] perhaps.
[5545.94 → 5546.34] I'm not going to
[5546.34 → 5546.98] drop the Shabby,
[5547.16 → 5547.92] but most people
[5547.92 → 5548.30] don't even know
[5548.30 → 5548.84] what it is.
[5549.20 → 5549.60] Well, I thought
[5549.60 → 5550.12] because of the
[5550.12 → 5550.80] Shabby, you
[5550.80 → 5551.30] would know.
[5551.46 → 5551.82] I don't know
[5551.82 → 5552.24] that verse.
[5552.70 → 5553.08] Check the
[5553.32 → 5553.86] what is it?
[5553.94 → 5554.56] It's, uh,
[5554.66 → 5555.34] numbers don't lie.
[5555.40 → 5556.06] Check the scoreboard.
[5556.42 → 5556.74] Okay.
[5557.18 → 5557.78] I know I've
[5557.78 → 5558.54] pointed at a
[5558.54 → 5559.18] scoreboard before,
[5559.40 → 5559.94] especially in high
[5559.94 → 5560.48] school basketball,
[5560.72 → 5561.52] and said scoreboard.
[5561.80 → 5562.28] Well, that's a
[5562.28 → 5562.46] thing.
[5562.52 → 5562.98] I mean, I think
[5562.98 → 5563.52] it's a thing,
[5563.54 → 5564.10] and he made it
[5564.10 → 5564.62] a lyric.
[5564.94 → 5565.60] He didn't create
[5565.60 → 5565.82] it.
[5566.02 → 5566.50] He didn't coin
[5566.50 → 5566.74] it.
[5566.94 → 5567.16] Yeah, I was
[5567.16 → 5567.56] going to say he
[5567.56 → 5567.94] stole it from
[5573.42 → 5574.14] copyright.
[5575.16 → 5575.90] Okay, so,
[5576.48 → 5577.28] uh, good
[5577.28 → 5577.66] attempt.
[5577.82 → 5578.24] You know, we
[5578.24 → 5578.76] missed the layup
[5578.76 → 5579.30] on that one.
[5579.52 → 5580.26] It was my fault.
[5580.86 → 5581.60] But that's it.
[5581.64 → 5582.48] That's our 12
[5582.48 → 5583.58] voicemails and
[5583.58 → 5584.02] remixes.
[5584.30 → 5585.02] Thank you, BMC.
[5585.12 → 5585.64] Thank you to all
[5585.64 → 5586.20] of our listeners.
[5586.70 → 5587.68] But now it's our
[5587.68 → 5588.36] turn to talk.
[5588.46 → 5589.24] Ooh, yes.
[5589.90 → 5590.72] It's a whole new
[5590.72 → 5591.30] show now.
[5591.50 → 5592.26] Chapter Marker,
[5592.44 → 5592.96] Drop It.
[5593.00 → 5593.76] Part two.
[5593.90 → 5594.78] Another hour of
[5594.78 → 5595.56] show coming up.
[5595.76 → 5596.32] Get ready.
[5596.58 → 5597.16] We're going for a
[5597.16 → 5597.84] bathroom break.
[5597.92 → 5598.42] We're shaking our
[5598.42 → 5598.80] legs.
[5599.56 → 5600.26] I'm just kidding.
[5603.42 → 5604.16] What's up, friends?
[5604.40 → 5604.90] I'm here in the
[5604.90 → 5605.56] breaks with David
[5605.56 → 5606.76] Hsu, founder and
[5606.76 → 5608.18] CEO at Retool.
[5608.50 → 5608.90] If you didn't
[5608.90 → 5609.96] know, Retool is
[5609.96 → 5611.28] the fastest way to
[5611.28 → 5612.18] build internal
[5612.18 → 5612.74] software.
[5613.24 → 5613.68] So, David, we're
[5613.68 → 5614.22] here to talk about
[5614.22 → 5614.68] Retool.
[5614.86 → 5615.52] I love Retool.
[5615.58 → 5616.10] You know that.
[5616.38 → 5616.94] I've been a fan of
[5616.94 → 5617.80] yours for years.
[5618.28 → 5618.74] But I'm on the
[5618.74 → 5619.76] outside, and you're
[5619.76 → 5620.88] clearly on the
[5620.88 → 5621.44] inside, right?
[5621.50 → 5621.90] You're on the
[5621.90 → 5622.34] inside, right?
[5622.50 → 5623.06] I think so.
[5623.20 → 5624.00] Yeah, I'd say so.
[5624.16 → 5624.70] Okay, cool.
[5625.18 → 5625.84] So, given that
[5625.84 → 5626.26] you're on the
[5626.26 → 5627.30] inside, and I'm
[5627.30 → 5628.36] not on the
[5628.36 → 5629.32] inside, who is
[5629.32 → 5630.56] using Retool and
[5630.56 → 5632.00] why are they
[5632.00 → 5632.60] using Retool?
[5632.84 → 5633.14] Yeah.
[5633.42 → 5634.16] So, the primary
[5634.16 → 5634.96] reason someone
[5634.96 → 5635.88] uses Retool is
[5635.88 → 5637.02] typically they are
[5637.02 → 5637.62] a backend
[5637.62 → 5638.80] engineer who's
[5638.80 → 5639.78] looking to build
[5639.78 → 5640.26] some sort of
[5640.26 → 5641.52] internal tool and
[5641.52 → 5642.08] it involves the
[5642.08 → 5642.44] frontend.
[5642.80 → 5643.52] And backend
[5643.52 → 5644.20] engineers typically
[5644.20 → 5644.80] don't care too
[5644.80 → 5645.16] much for the
[5645.16 → 5645.54] frontend.
[5645.74 → 5646.28] They might not
[5646.28 → 5646.86] know React,
[5646.98 → 5647.76] Redux, all that
[5647.76 → 5648.50] well, and they
[5648.50 → 5649.40] say, hey, I just
[5649.40 → 5650.00] want a simple
[5650.00 → 5650.52] button, simple
[5650.52 → 5651.26] form on top of
[5651.26 → 5651.82] my database or
[5651.82 → 5652.16] API.
[5652.70 → 5653.16] Why is it so
[5653.16 → 5653.42] hard?
[5653.66 → 5654.00] And so that's
[5654.00 → 5654.52] kind of the core
[5654.52 → 5655.48] concept behind
[5655.48 → 5656.82] Retool is frontend
[5656.82 → 5657.62] web development has
[5657.62 → 5658.88] gotten so difficult
[5658.88 → 5660.68] in the past 5,
[5660.78 → 5662.02] 10, 20 years.
[5662.02 → 5663.22] It's so complicated
[5663.22 → 5663.66] today.
[5663.88 → 5664.44] Put together a
[5664.44 → 5665.48] simple form with
[5665.48 → 5666.22] a submit button,
[5666.50 → 5667.06] have to submit to
[5667.06 → 5667.46] an API.
[5667.82 → 5668.32] You have to worry,
[5668.44 → 5669.24] for example, about
[5669.24 → 5669.90] oh, you know, when
[5669.90 → 5670.42] you press to submit
[5670.42 → 5670.96] button, you got to
[5670.96 → 5671.88] bounce it or you
[5671.88 → 5672.76] got to disable it
[5672.76 → 5673.38] when it's, you
[5673.38 → 5673.98] know, is fetching
[5673.98 → 5674.56] is true.
[5674.86 → 5675.44] And then when it
[5675.44 → 5676.20] comes back, you got
[5676.20 → 5676.86] to enable the
[5676.86 → 5677.48] button again.
[5677.58 → 5677.92] When there's an
[5677.92 → 5678.56] error, you got to
[5678.56 → 5679.22] display the error
[5679.22 → 5679.48] message.
[5679.64 → 5680.54] There's so much
[5680.54 → 5681.70] crap now with
[5681.70 → 5682.28] building a simple
[5682.28 → 5683.10] form like that.
[5683.36 → 5683.76] And Retool takes
[5683.76 → 5684.30] that all away.
[5684.42 → 5685.36] And so really, I
[5685.36 → 5686.16] think the core
[5686.16 → 5686.84] reason why someone
[5686.84 → 5687.78] would use Retool is
[5687.78 → 5688.36] they just don't want
[5688.36 → 5688.84] to build any more
[5688.84 → 5689.48] internal tools.
[5689.74 → 5690.08] I want to save
[5690.08 → 5690.44] some time.
[5690.94 → 5691.56] Yeah, clearly the
[5691.56 → 5692.66] front end has gotten
[5692.66 → 5693.20] complex.
[5693.30 → 5694.12] No doubt about that.
[5694.34 → 5695.08] I think even front
[5695.08 → 5695.68] Enders would agree
[5695.68 → 5696.20] with that sentiment.
[5696.64 → 5697.22] And then you have
[5697.22 → 5698.16] back end folks that
[5698.16 → 5698.80] already have access
[5698.80 → 5700.22] to everything, API
[5700.22 → 5701.56] keys, production
[5701.56 → 5703.20] database, servers,
[5703.46 → 5703.76] whatever.
[5704.00 → 5704.96] But then to just
[5704.96 → 5706.22] stand up Retool, to
[5706.22 → 5707.40] me, seems like the
[5707.40 → 5708.40] next real easy
[5708.40 → 5709.62] button because you
[5709.62 → 5710.50] can just remove the
[5710.50 → 5711.80] entire front end
[5711.80 → 5712.98] layer complexity.
[5713.50 → 5714.08] You're not trying to
[5714.08 → 5714.78] take it away.
[5714.90 → 5715.60] You're just trying to
[5715.60 → 5716.28] augment it.
[5716.66 → 5717.60] You're trying to give
[5717.60 → 5719.50] developers a given
[5719.50 → 5720.50] interface, that's
[5720.50 → 5721.90] Retool, build out
[5721.90 → 5723.38] your own admin, your
[5723.38 → 5724.80] own view to a Google
[5724.80 → 5726.14] sheet or to the
[5726.14 → 5727.38] production database,
[5727.64 → 5728.64] all inside Retool.
[5728.96 → 5729.86] Let Retool be the
[5729.86 → 5730.80] front end to the
[5730.80 → 5731.84] already existing
[5731.84 → 5732.52] back end.
[5732.76 → 5733.70] Is that about right?
[5734.22 → 5735.32] Yeah, that is
[5735.32 → 5736.50] exactly right.
[5736.60 → 5737.48] The way we think
[5737.48 → 5739.22] about it is we want
[5739.22 → 5740.52] to abstract away
[5740.52 → 5741.68] things that a
[5741.68 → 5742.78] developer should not
[5742.78 → 5743.98] need to focus on,
[5744.12 → 5744.72] such that a
[5744.72 → 5745.54] developer can focus
[5745.54 → 5746.24] on what is truly
[5746.24 → 5747.44] specific or unique to
[5747.44 → 5748.10] their business.
[5748.44 → 5749.22] And so the vision
[5749.22 → 5750.10] of what we want to
[5750.10 → 5751.32] build is something
[5751.32 → 5752.22] like an AWS,
[5752.52 → 5753.86] actually, where I
[5753.86 → 5754.78] think AWS really
[5754.78 → 5756.02] fundamentally transformed
[5756.02 → 5756.62] the infrastructure
[5756.62 → 5756.94] layer.
[5757.24 → 5757.78] Back in the day,
[5758.02 → 5759.06] developers spent all
[5759.06 → 5759.86] their time thinking
[5759.86 → 5761.08] about how do I go
[5761.08 → 5761.78] rack servers?
[5762.28 → 5763.66] How do I go manage
[5763.66 → 5764.76] cooling, manage power
[5764.76 → 5765.26] supplies?
[5765.34 → 5766.08] How do I upgrade my
[5766.08 → 5767.50] database without it
[5767.50 → 5768.16] going down?
[5768.30 → 5769.56] How do I change out
[5769.56 → 5771.06] the hard drive while
[5771.06 → 5771.82] still being online?
[5772.08 → 5772.94] All these problems.
[5773.26 → 5773.76] And they're not
[5773.76 → 5774.60] problems anymore because
[5774.60 → 5775.30] nowadays when you want
[5775.30 → 5776.06] to upgrade your database,
[5776.22 → 5776.82] just go to RDS,
[5776.82 → 5777.58] press a few buttons.
[5777.90 → 5779.16] And so what AWS did to
[5779.16 → 5780.26] the infrastructure layer
[5780.26 → 5781.44] is what we want to do
[5781.44 → 5782.54] to the application layer
[5782.54 → 5783.74] specifically on the
[5783.74 → 5784.36] front end today.
[5784.76 → 5785.88] And for me, that's
[5785.88 → 5787.02] pretty exciting because
[5787.02 → 5788.58] as a developer myself,
[5788.84 → 5790.32] I'm not really honestly
[5790.32 → 5791.28] that interested, for
[5791.28 → 5792.48] example, in managing
[5792.48 → 5793.94] infrastructure in a
[5793.94 → 5794.70] nuts and bolts way.
[5794.86 → 5795.38] Now, I would much
[5795.38 → 5796.14] rather be like, hey,
[5796.16 → 5796.72] you know, I want S3
[5796.72 → 5797.52] bucket, boom, there's
[5797.52 → 5798.06] an S3 bucket.
[5798.14 → 5799.02] I want a database, boom,
[5799.08 → 5799.54] there's a database.
[5799.54 → 5800.82] And similarly, on the
[5800.82 → 5801.92] front end or in the
[5801.92 → 5803.34] application layer, there is
[5803.34 → 5805.10] so much crap people have
[5805.10 → 5806.34] to do today when it
[5806.34 → 5806.98] comes to building a
[5806.98 → 5807.94] simple CRUD application.
[5808.14 → 5808.94] It's like, you know,
[5808.94 → 5809.54] you probably have to
[5809.54 → 5810.86] install 10, 15, maybe
[5810.86 → 5811.54] even 20 different
[5811.54 → 5812.08] libraries.
[5812.36 → 5813.02] You probably don't know
[5813.02 → 5814.04] what most libraries do.
[5814.18 → 5815.36] It's really complicated
[5815.36 → 5816.96] to load a simple form.
[5817.12 → 5817.80] You know, you're probably
[5817.80 → 5818.80] downloading almost like a
[5818.80 → 5819.54] megabyte or two of
[5819.54 → 5819.88] JavaScript.
[5820.10 → 5822.26] It's so much crap to
[5822.26 → 5823.10] build a simple form.
[5823.30 → 5824.00] And so that's kind of the
[5824.00 → 5825.16] idea behind Retool is
[5825.16 → 5826.00] could it be a lot
[5826.00 → 5826.44] simpler?
[5826.82 → 5827.66] Could we just make it so
[5827.66 → 5828.28] much faster?
[5828.52 → 5829.18] Could you go from
[5829.18 → 5830.58] nothing to a form on top
[5830.58 → 5831.50] of your database or API
[5831.50 → 5832.50] in two minutes?
[5832.86 → 5833.44] We think so.
[5833.44 → 5834.56] Yeah, I think so, too.
[5834.88 → 5837.18] So listeners, Retool is
[5837.18 → 5838.02] built for scale.
[5838.42 → 5839.42] It's built for enterprise.
[5839.72 → 5840.80] It's built for everyone.
[5841.16 → 5842.62] And Retool is built for
[5842.62 → 5843.12] developers.
[5843.24 → 5843.64] That's you.
[5843.96 → 5844.86] You can self-host it.
[5844.92 → 5845.36] You can run into the
[5845.36 → 5845.76] cloud.
[5846.08 → 5847.80] Custom SSO, audit log,
[5847.94 → 5849.44] SOC 2, type 2, professional
[5849.44 → 5850.22] services.
[5850.60 → 5851.60] Starting with Retool is
[5851.60 → 5853.42] simple, fast, and of
[5853.42 → 5854.32] course, it's free if you
[5854.32 → 5855.16] want to try it right now.
[5855.48 → 5857.68] So go to retool.com
[5857.68 → 5859.28] slash changelog.
[5859.28 → 5862.66] That's R-E-T-O-O-L dot com
[5862.66 → 5864.20] slash changelog.
[5871.48 → 5874.30] Favourite episodes of ours.
[5874.56 → 5875.82] How many of yours are left
[5875.82 → 5876.16] standing?
[5876.60 → 5878.10] Let me just say one thing
[5878.10 → 5879.68] before we truly break over.
[5880.04 → 5880.36] Okay.
[5880.48 → 5882.88] Because I recall the podcast
[5882.88 → 5883.36] with Jamie.
[5883.86 → 5884.14] Yes.
[5884.40 → 5885.68] I recall being there,
[5885.80 → 5886.14] obviously.
[5886.56 → 5887.52] I recall this show was
[5887.52 → 5887.88] awesome.
[5888.08 → 5888.36] Good.
[5888.50 → 5890.08] I do not recall titling
[5890.08 → 5891.86] that show Meeting Stuff
[5891.86 → 5892.54] Into Public.
[5893.14 → 5893.92] Did you title that
[5893.92 → 5894.90] Sans Me?
[5895.12 → 5896.52] Was I on vacation or
[5896.52 → 5896.76] something?
[5896.94 → 5897.44] It was like a Friday
[5897.44 → 5897.82] afternoon.
[5897.96 → 5899.14] I just slapped a title on
[5899.14 → 5899.60] it and went.
[5899.88 → 5900.22] Okay.
[5900.48 → 5901.40] Well, he said that.
[5901.60 → 5901.88] Did he?
[5902.02 → 5902.26] Okay.
[5902.56 → 5903.64] And it was all about him
[5903.64 → 5904.98] doing like public, you
[5904.98 → 5905.88] know, his whole public
[5905.88 → 5907.44] salary and writing and
[5907.44 → 5907.74] everything.
[5907.98 → 5908.18] And so.
[5908.40 → 5909.44] Meeting is a term?
[5909.64 → 5910.18] What is a meeting?
[5910.46 → 5910.82] Meeting?
[5911.12 → 5911.44] Meeting.
[5911.48 → 5911.66] Yeah.
[5911.88 → 5913.08] To yeet something is to
[5913.08 → 5913.80] throw it.
[5914.38 → 5914.60] Whew.
[5915.44 → 5915.94] T-I-L.
[5916.18 → 5916.42] Yeah.
[5916.74 → 5917.46] It's what the kids are
[5917.46 → 5917.66] saying.
[5917.76 → 5918.22] At least they were
[5918.22 → 5919.24] saying it about 10 years
[5919.24 → 5919.46] ago.
[5919.52 → 5920.38] I think it's kind of old.
[5920.84 → 5921.04] Yeah.
[5921.18 → 5921.54] Meeting.
[5922.06 → 5922.28] Hmm.
[5922.58 → 5922.90] Yeet.
[5923.18 → 5923.98] See, I mean.
[5924.04 → 5924.58] You say that when you
[5924.58 → 5925.40] just toss somebody.
[5925.54 → 5925.80] Yeet.
[5926.30 → 5927.26] I didn't toss anybody
[5927.26 → 5927.72] for one.
[5928.90 → 5929.76] No, it's not you.
[5929.90 → 5930.96] Jamie was meeting stuff
[5930.96 → 5931.28] in the public.
[5931.30 → 5931.84] He's just been throwing
[5931.84 → 5932.78] stuff into public, you
[5932.78 → 5932.90] know?
[5932.98 → 5933.48] I got it.
[5933.68 → 5934.54] I'm getting it, but.
[5934.68 → 5935.02] Okay.
[5935.20 → 5935.40] Yeah.
[5935.40 → 5936.22] I titled that one without
[5936.22 → 5936.46] you.
[5936.52 → 5937.46] You know, sometimes we just
[5937.46 → 5937.78] roll.
[5937.90 → 5938.50] I have an idea.
[5938.64 → 5939.22] I like it.
[5939.32 → 5940.06] I'm just going to publish
[5940.06 → 5940.56] that sucker.
[5940.90 → 5941.08] You know?
[5941.28 → 5942.04] It's so obvious.
[5942.20 → 5942.80] Why check?
[5942.92 → 5943.28] Exactly.
[5943.98 → 5944.62] Especially when it's
[5944.62 → 5945.28] something that they say
[5945.28 → 5945.76] on the show.
[5945.84 → 5946.70] It's like too easy.
[5947.20 → 5948.00] I have a long list.
[5948.04 → 5948.34] Okay.
[5948.62 → 5950.04] I mean, I'm not even sure
[5950.04 → 5951.52] that I can express this
[5951.52 → 5951.82] list.
[5951.94 → 5952.46] It's lengthy.
[5952.76 → 5953.18] Well, we are.
[5953.36 → 5954.38] While we're bike shedding
[5954.38 → 5955.26] titles, should we just get
[5955.26 → 5956.06] the titles out of the way?
[5956.20 → 5957.02] Favourite titles.
[5957.36 → 5957.98] Did you write some down?
[5958.28 → 5958.56] Oh, yeah.
[5958.88 → 5959.02] Yeah.
[5959.02 → 5959.22] Okay.
[5959.34 → 5960.16] Let's just do that one quick
[5960.16 → 5961.54] because it's less emotional.
[5962.10 → 5962.98] Can we do it quick?
[5963.44 → 5963.96] Let's do it.
[5964.26 → 5964.44] Yeah.
[5964.44 → 5965.40] You, me, or you?
[5965.90 → 5966.78] Let's just go back and
[5966.78 → 5967.08] forth.
[5967.52 → 5968.36] You, me, or you?
[5968.68 → 5968.92] Okay.
[5968.96 → 5969.48] Me first.
[5969.70 → 5969.94] Okay.
[5970.28 → 5971.06] Great title.
[5971.46 → 5972.68] It's not always DNS.
[5973.34 → 5975.44] Oh, that's in, I won't say
[5975.44 → 5975.58] it.
[5975.78 → 5975.96] Yeah.
[5976.10 → 5976.60] Oh, that's in your
[5976.60 → 5976.96] favourite list.
[5977.38 → 5977.58] Yeah.
[5977.68 → 5979.04] I like that one because we
[5979.04 → 5980.10] wanted to call it, it's always
[5980.10 → 5982.10] DNS, but we realized on the
[5982.10 → 5983.32] show that Paul Dixie actually
[5983.32 → 5984.52] didn't like that statement.
[5984.74 → 5987.80] And so we inverted it similar
[5987.80 → 5989.02] to the not insane tech hiring
[5989.02 → 5989.36] market.
[5989.50 → 5990.90] And we said, it's not always
[5990.90 → 5991.20] DNS.
[5991.70 → 5992.92] So that's why I like that
[5992.92 → 5993.12] one.
[5993.32 → 5993.68] Your turn.
[5993.68 → 5995.52] You'll rent chips and be
[5995.52 → 5995.84] happy.
[5996.16 → 5996.92] Oh yeah.
[5997.34 → 5999.86] This was a recent friend
[5999.86 → 6000.58] episode, wasn't it?
[6000.92 → 6001.30] Yeah.
[6001.66 → 6002.28] And what were we talking
[6002.28 → 6002.82] about again?
[6003.44 → 6005.92] Zach Smith, Equinix, metal
[6005.92 → 6006.34] fame.
[6006.54 → 6006.86] Right.
[6006.96 → 6007.56] Previous to that was
[6007.56 → 6007.92] packet.
[6008.38 → 6008.72] Right.
[6008.92 → 6010.38] But they go back to the
[6010.38 → 6011.18] um, we talk about
[6011.18 → 6012.48] subscriptions inside of data
[6012.48 → 6013.18] centres and stuff.
[6013.40 → 6013.88] Right.
[6014.48 → 6015.76] Because of like recycling
[6015.76 → 6018.30] hardware and getting kind of
[6018.30 → 6019.22] having the best tech.
[6019.36 → 6019.50] Right.
[6019.58 → 6020.94] And his big idea is like to
[6020.94 → 6021.94] recycle the hardware and
[6021.94 → 6022.60] subscribe to it.
[6022.68 → 6023.56] And people were not,
[6023.68 → 6024.84] down with his idea, by
[6024.84 → 6025.52] the way, we had lots of
[6025.52 → 6026.68] people writing in like,
[6026.76 → 6027.64] this isn't a good idea.
[6027.74 → 6029.32] I was, I don't know,
[6029.38 → 6029.86] data centres.
[6029.94 → 6031.44] I don't know big data
[6031.44 → 6031.92] business.
[6031.92 → 6032.54] Who wrote this in?
[6032.58 → 6033.06] Where did they write this
[6033.06 → 6033.36] in at?
[6033.58 → 6033.98] In Zulip?
[6034.88 → 6035.64] Did I miss the chat?
[6035.96 → 6036.70] There was some chat.
[6037.10 → 6037.56] I don't remember.
[6037.94 → 6038.22] Oh dang.
[6038.28 → 6039.26] Probably Zulip, probably
[6039.26 → 6039.78] Internets.
[6040.30 → 6040.56] Okay.
[6040.84 → 6042.00] Um, but interesting
[6042.00 → 6043.30] conversation brought out a
[6043.30 → 6044.80] lot of people's thoughts and
[6044.80 → 6046.66] great title because we were
[6046.66 → 6048.34] talking about the whole world
[6048.34 → 6050.44] economic forum, and you'll
[6050.44 → 6051.44] own nothing and be happy.
[6051.44 → 6052.34] And this is you will rent
[6052.34 → 6052.66] chips.
[6052.72 → 6054.28] These are GPUs and be
[6054.28 → 6054.50] happy.
[6054.60 → 6054.90] Good one.
[6054.96 → 6055.38] My turn.
[6055.56 → 6056.76] Retirement is for suckers.
[6058.72 → 6059.62] That is a good one.
[6059.92 → 6061.48] Oh, talk about a quote.
[6061.60 → 6062.56] I mean, he literally said
[6062.56 → 6062.72] that.
[6063.40 → 6065.40] Cameron say came out right at
[6065.40 → 6065.78] the beginning.
[6065.78 → 6067.04] It's just like retirements for
[6067.04 → 6067.54] suckers.
[6067.66 → 6068.44] And that was the show title.
[6068.66 → 6069.20] Show title.
[6069.94 → 6070.78] You will like this one.
[6070.90 → 6071.98] I think it's the best one of
[6071.98 → 6072.28] the year.
[6072.78 → 6074.00] If there was an award for the
[6074.00 → 6074.90] the best title of the year, this
[6074.90 → 6075.28] is it.
[6075.58 → 6075.80] Okay.
[6075.92 → 6077.14] The wrong place to slap a
[6077.14 → 6077.44] person.
[6078.26 → 6079.60] I believe it's the best of the
[6079.60 → 6079.72] year.
[6079.72 → 6081.66] That one is in my list as well.
[6082.06 → 6083.14] I think it stands still yet.
[6083.22 → 6084.14] That's the wrong place to slap
[6084.14 → 6084.48] a person.
[6084.60 → 6085.32] I mean, it's great.
[6085.44 → 6087.62] It's created some major waves, a
[6087.62 → 6088.12] lot of drama.
[6088.30 → 6090.00] I mean, would it be different if
[6090.00 → 6090.72] it was done differently?
[6091.00 → 6091.34] Maybe.
[6091.90 → 6092.78] I don't think so.
[6093.22 → 6094.48] Of course, referring to the Matt
[6094.48 → 6096.98] Mullen call out of WB
[6096.98 → 6098.70] Engine at Word Camp.
[6099.16 → 6100.22] That's the wrong place to
[6100.22 → 6100.68] slap a person.
[6100.82 → 6101.86] We recorded this Friends
[6101.86 → 6102.36] episode.
[6102.44 → 6102.72] Yes.
[6102.82 → 6103.84] I think with Nick Needed as
[6103.84 → 6105.62] well, right after that event.
[6105.72 → 6106.62] And so that's what this thing
[6106.62 → 6107.32] is referring to.
[6107.78 → 6109.06] And Adam said that on the
[6109.06 → 6109.22] show.
[6109.30 → 6110.80] I do like to have show titles
[6110.80 → 6112.72] that are something that was
[6112.72 → 6113.34] said on the show.
[6113.42 → 6114.38] I think it's a nice, easy way
[6114.38 → 6115.76] of having a tie in, especially
[6115.76 → 6116.64] when you don't know what it
[6116.64 → 6117.94] means at first and then you
[6117.94 → 6119.06] hear it later on the show.
[6119.14 → 6119.98] I've always enjoyed that.
[6120.12 → 6120.82] It does make it sweeter.
[6121.22 → 6121.54] I agree.
[6121.62 → 6122.46] That was in my list of best
[6122.46 → 6122.80] titles.
[6123.08 → 6123.70] How about this one?
[6123.70 → 6125.06] The Old Hot and Juicy.
[6125.26 → 6126.32] That's in my list too.
[6127.38 → 6128.24] Adam's the best.
[6128.72 → 6129.64] The Old Hot and Juicy.
[6130.00 → 6131.08] Gosh, what was the context?
[6131.88 → 6133.02] Why did he say that?
[6133.14 → 6133.60] Do you recall?
[6134.28 → 6137.10] It was similar to a horse
[6137.10 → 6138.00] head in your bed.
[6138.66 → 6140.72] You know, it's the offer you
[6140.72 → 6141.28] can't refuse.
[6141.38 → 6142.56] The Old Hot and Juicy is like
[6142.56 → 6144.36] this thing that's like he was
[6144.36 → 6147.48] referring to the article written
[6147.48 → 6150.94] by Matt Essay about open tofu,
[6150.94 → 6153.46] potentially copyright infringing
[6153.46 → 6153.98] terraform.
[6154.36 → 6154.68] Yes.
[6155.08 → 6155.92] And it's like this.
[6156.20 → 6157.48] The Old Hot and Juicy is like.
[6157.58 → 6158.96] Can I quote him from the
[6158.96 → 6159.28] transcript?
[6159.58 → 6160.12] Yeah, go ahead.
[6160.44 → 6161.64] Adam Jacobs says, yeah.
[6161.90 → 6163.16] And the reputation dragon was
[6163.16 → 6164.04] the reason to do it.
[6164.18 → 6165.20] Somebody replied to me on
[6165.20 → 6165.96] Twitter and called the
[6165.96 → 6167.38] cease and desist letter the
[6167.38 → 6168.08] Old Hot and Juicy.
[6168.50 → 6168.80] Right.
[6169.12 → 6170.24] So the letter was the Old
[6170.24 → 6170.68] Hot and Juicy.
[6170.78 → 6171.70] OK, not the article.
[6172.00 → 6172.50] Not the article.
[6172.50 → 6173.76] But he said Old Hot and Juicy
[6173.76 → 6175.08] like three, four more times
[6175.08 → 6175.64] on that show.
[6175.90 → 6176.58] I think so.
[6176.68 → 6177.92] And it became the show title.
[6178.66 → 6179.26] You got another one?
[6179.74 → 6181.38] The B.S.O.D.
[6181.98 → 6182.96] Crowd Strikes Back.
[6183.16 → 6184.14] That's my other one.
[6184.62 → 6185.42] This was, of course, our
[6185.42 → 6186.56] Crowd Strike episode with
[6186.56 → 6187.12] Robert Ross.
[6187.44 → 6188.04] Probably should have said it
[6188.04 → 6188.20] differently.
[6188.34 → 6189.04] The B.S.O.D.
[6189.18 → 6190.02] The Blue Screen of Death.
[6190.04 → 6191.22] To drag it out doesn't like
[6191.22 → 6191.82] let it land.
[6192.38 → 6193.14] The B.S.O.D.
[6193.40 → 6194.08] Crowd Strikes Back.
[6194.20 → 6194.46] Right.
[6194.54 → 6195.30] Well, of course, we are
[6195.30 → 6197.40] referring to the Empire Strikes Back,
[6198.08 → 6200.14] but it's the Blue Screen of Death
[6200.14 → 6202.10] that's Crowd Striking back.
[6202.66 → 6202.78] Yes.
[6202.78 → 6203.34] Because it did, man.
[6203.36 → 6204.38] All of a sudden, here comes the
[6204.38 → 6205.00] B.S.O.D.
[6206.16 → 6208.22] Striking a PC near you around
[6208.22 → 6210.76] the Crowd Strike debacle.
[6210.96 → 6211.26] Incident.
[6211.58 → 6212.26] Yeah, debacle.
[6212.46 → 6213.34] It's probably a debacle.
[6213.56 → 6214.58] Well, that's an incident for sure.
[6214.96 → 6215.52] Oh, for sure.
[6215.86 → 6217.80] A scalable incident at that.
[6217.88 → 6218.80] Bigger than an incident.
[6219.28 → 6220.46] Incident doesn't do it justice.
[6221.22 → 6222.30] Debacle was a great word.
[6222.70 → 6223.68] Having caught up with the
[6223.68 → 6225.90] ripples, though, like what's
[6225.90 → 6227.52] changed as a result of this
[6227.52 → 6227.90] happening?
[6228.50 → 6229.04] That'd be good.
[6229.32 → 6229.98] Yeah, I don't know.
[6230.16 → 6230.90] I mean, that can be kind of
[6230.90 → 6231.36] boring, maybe.
[6231.36 → 6232.70] Well, if it's interesting, then
[6232.70 → 6233.30] it's interesting.
[6233.44 → 6234.12] But if it's boring.
[6234.26 → 6234.60] That's true.
[6234.78 → 6236.02] Let's change very little.
[6236.22 → 6237.08] There's like a few more
[6237.08 → 6238.86] processes inside CrowdStrike now.
[6239.50 → 6239.70] All right.
[6239.74 → 6240.90] Last one for me.
[6241.00 → 6242.48] Best title of the year.
[6242.74 → 6244.84] This one saved us from a
[6244.84 → 6246.04] bunch of other bad titles.
[6246.24 → 6247.80] So from a bunch of bad titles
[6247.80 → 6249.00] that we had come up before it.
[6249.06 → 6249.92] And the title is
[6249.92 → 6252.40] Major. Semver. Patch.
[6253.42 → 6254.40] That was a good title.
[6254.64 → 6255.10] All caps.
[6255.14 → 6255.48] Of course.
[6255.48 → 6257.30] We had a hard time naming
[6257.30 → 6258.58] that episode we did about
[6258.58 → 6258.94] SemVer.
[6259.84 → 6262.06] But why not use SemVer to name
[6262.06 → 6263.30] SemVer and call it a patch?
[6263.34 → 6264.10] Because the whole thing was
[6264.10 → 6265.00] about how we can change
[6265.00 → 6265.88] SemVer to make it better.
[6266.08 → 6266.30] Yeah.
[6266.44 → 6267.44] Can we have a major patch
[6267.44 → 6267.86] to SemVer?
[6268.32 → 6268.78] Solid title.
[6269.24 → 6269.46] Yeah.
[6270.46 → 6270.86] 1999.
[6271.46 → 6272.62] A film odyssey.
[6272.90 → 6273.34] Hmm.
[6273.52 → 6274.88] That's a changelog plus
[6274.88 → 6275.30] only.
[6275.40 → 6276.78] It's a bonus show for those
[6276.78 → 6278.34] who are the cool people.
[6278.46 → 6279.42] You know, it's better.
[6280.32 → 6281.08] Just saying.
[6282.06 → 6283.44] That was actually almost
[6283.44 → 6284.38] made my list of favourite
[6284.38 → 6285.48] episodes, but I didn't want
[6285.48 → 6286.34] to put it on because I feel
[6286.34 → 6287.38] like that's just rude.
[6288.66 → 6289.94] Well, I did it for you.
[6290.40 → 6290.62] Oh.
[6291.04 → 6291.52] And I'm rude.
[6292.08 → 6293.18] And the last one was
[6293.18 → 6294.88] The Wu-Tang Way.
[6295.10 → 6296.00] Yeah, that's a good one.
[6296.14 → 6296.28] Yeah.
[6296.82 → 6297.34] Good show.
[6297.48 → 6297.88] Good title.
[6298.78 → 6299.20] Fun title.
[6299.46 → 6299.72] All right.
[6299.78 → 6300.30] Here we go.
[6300.60 → 6301.32] Favourite episodes.
[6301.52 → 6302.54] How many years are left
[6302.54 → 6303.10] standing?
[6303.70 → 6304.06] Standing?
[6304.32 → 6305.26] Like have not been
[6305.26 → 6305.52] mentioned?
[6305.64 → 6306.30] Like they haven't been
[6306.30 → 6307.54] referenced by anybody else.
[6307.70 → 6308.58] Let's see here.
[6308.58 → 6313.44] Oh, one, two, three, four.
[6314.74 → 6315.52] Technically five.
[6315.94 → 6318.04] So of my nine, I have five
[6318.04 → 6319.08] favourites and four
[6319.08 → 6319.74] honourable mentions.
[6320.38 → 6322.96] Of my nine, I have almost
[6322.96 → 6323.62] all of them.
[6324.38 → 6325.32] I have seven of nine.
[6325.56 → 6325.90] Okay.
[6326.06 → 6327.12] Maybe six, depending on
[6327.12 → 6327.94] how you count this one.
[6328.06 → 6328.82] You just want to go through
[6328.82 → 6329.78] the list real fast?
[6330.14 → 6330.94] You want to do all yours
[6330.94 → 6332.04] and then all mine, all mine
[6332.04 → 6332.44] and then all yours.
[6332.48 → 6333.32] I think everyone's waiting
[6333.32 → 6334.36] for me to reveal my
[6334.36 → 6334.94] unprecedented.
[6335.40 → 6335.72] Yeah.
[6335.86 → 6336.64] Because I mean, it's been
[6336.64 → 6337.34] like an hour and a half.
[6337.34 → 6338.34] I'm not, but I think they
[6338.34 → 6338.78] might be.
[6338.94 → 6339.66] They've forgotten about
[6339.66 → 6340.12] it by now.
[6340.30 → 6341.32] I've forgotten about it,
[6341.32 → 6342.84] but I'm down for it.
[6342.96 → 6343.54] I'm just kidding with you.
[6343.68 → 6343.98] All right.
[6344.00 → 6344.90] So here's what I'm going to
[6344.90 → 6345.20] say.
[6345.30 → 6346.66] And I think you're going
[6346.66 → 6347.24] to like this.
[6347.34 → 6347.60] Okay.
[6348.26 → 6349.42] One of my favourite episodes,
[6349.52 → 6350.34] these are in no particular
[6350.34 → 6350.78] order.
[6350.92 → 6351.18] Okay.
[6351.18 → 6352.06] So they're not like one
[6352.06 → 6352.48] through five.
[6352.54 → 6353.56] This is not my number one
[6353.56 → 6354.90] favourite episode, but right.
[6355.08 → 6356.22] One of my five favourite
[6356.22 → 6357.44] episodes, unprecedented,
[6357.58 → 6358.24] never happened before.
[6358.24 → 6360.72] hasn't come out yet because
[6360.72 → 6363.38] it's coming out today as
[6363.38 → 6364.72] or tomorrow as we record
[6364.72 → 6366.04] and it will be out in the
[6366.04 → 6367.94] feed on Friday, but I'm not
[6367.94 → 6369.04] sure if it's my favourite
[6369.04 → 6370.30] because it hasn't been
[6370.30 → 6371.30] produced, but I'm pretty
[6371.30 → 6372.64] sure it's going to be one of
[6372.64 → 6373.78] my favourites because it is
[6373.78 → 6375.50] forty with Mitchell
[6375.50 → 6376.88] Hashimoto.
[6377.40 → 6377.78] Really?
[6378.30 → 6378.66] Really.
[6379.22 → 6380.20] Please tell me why it's your
[6380.20 → 6381.48] favourite, given that you
[6381.48 → 6382.26] haven't listened to it.
[6382.26 → 6383.66] It's the most recency bias
[6383.66 → 6384.90] I could possibly have.
[6387.36 → 6388.58] We just talked to him the
[6388.58 → 6389.22] other day, man.
[6389.90 → 6391.02] Recency bias is real.
[6391.42 → 6391.54] No.
[6391.80 → 6392.36] Good show though.
[6392.48 → 6392.88] I like that.
[6392.88 → 6393.50] Great show.
[6393.66 → 6394.22] Deep dive.
[6394.46 → 6395.18] He's so thoughtful.
[6395.70 → 6396.50] You know, you don't hear
[6396.50 → 6397.42] from him very much.
[6397.54 → 6398.70] So I hadn't heard from him
[6398.70 → 6400.68] besides his blog in a long
[6400.68 → 6401.04] time.
[6401.44 → 6402.32] I think forty is
[6402.32 → 6403.40] legitimately really cool.
[6404.06 → 6405.00] You know, it's not every
[6405.00 → 6406.52] year that I changed both my
[6406.52 → 6408.56] main text editor, which is
[6408.56 → 6410.70] now Zed, and my terminal,
[6410.70 → 6413.00] which as of last week, and
[6413.00 → 6413.52] I think it's going to
[6413.52 → 6414.74] continue, why wouldn't it
[6414.74 → 6415.64] is forty.
[6415.96 → 6416.20] Really?
[6416.48 → 6416.70] Yeah.
[6416.72 → 6417.80] I'm off terminal.app, man.
[6417.86 → 6419.04] I pulled it out of my
[6419.04 → 6419.34] doc.
[6419.64 → 6420.00] Oof.
[6420.14 → 6420.92] I haven't launched it
[6420.92 → 6421.22] since.
[6421.36 → 6422.20] He convinced me out of
[6422.20 → 6424.02] terminal.app, and I'm on
[6424.02 → 6425.62] forty and I just feel like
[6425.62 → 6426.78] I'm excited because I think
[6426.78 → 6427.80] forty is going to get way
[6427.80 → 6429.30] better over the next year
[6429.30 → 6430.32] and Mitchell got me
[6430.32 → 6430.66] excited.
[6430.82 → 6431.64] So I don't know.
[6431.84 → 6432.82] Call it recency bias.
[6433.20 → 6434.32] Call it haven't heard the
[6434.32 → 6435.22] episode yet bias.
[6435.78 → 6436.86] I just got a feeling that's
[6436.86 → 6438.46] going to be a top for not
[6438.46 → 6438.90] just me.
[6438.90 → 6441.06] And so what was your
[6441.06 → 6442.12] remind me what your hint
[6442.12 → 6443.28] was to me and what I did
[6443.28 → 6443.74] not get.
[6444.42 → 6445.26] Did you give me a hint?
[6445.64 → 6446.28] No, I didn't give you a
[6446.28 → 6446.56] hint.
[6446.58 → 6447.18] I just told you I was
[6447.18 → 6447.60] going to do something
[6447.60 → 6448.02] unprecedented.
[6448.20 → 6448.96] No one's ever picked a
[6448.96 → 6449.70] show that hasn't shipped
[6449.70 → 6449.96] yet.
[6450.26 → 6450.72] Oh, okay.
[6451.14 → 6451.66] That's true.
[6452.26 → 6453.36] And it is in this year.
[6453.48 → 6453.84] That's right.
[6453.96 → 6454.66] And that is unprecedented.
[6454.96 → 6456.08] It follows all the rules.
[6456.34 → 6457.02] Congratulations, Jerry.
[6457.06 → 6457.46] Thank you.
[6457.64 → 6458.02] Thank you.
[6458.28 → 6459.14] Probably the best pick of
[6459.14 → 6459.40] the year.
[6460.44 → 6461.20] What do you get going?
[6461.88 → 6462.60] Should I share my whole
[6462.60 → 6462.86] list?
[6462.92 → 6463.36] What should I do?
[6463.44 → 6464.10] Well, I might as well just
[6464.10 → 6464.94] keep going down mine.
[6465.12 → 6465.80] Yeah, sure.
[6465.90 → 6466.12] Why not?
[6466.14 → 6466.76] I'm going to break a few
[6466.76 → 6467.32] rules, though.
[6467.54 → 6468.70] The other thing I picked,
[6468.86 → 6470.02] number two, is all the
[6470.02 → 6470.36] Maidens.
[6470.84 → 6471.06] Oh.
[6471.36 → 6472.18] Can I just pick the Maidens
[6472.18 → 6473.26] as a totality?
[6473.26 → 6474.38] Yeah, it's too hard to do.
[6474.76 → 6475.66] I mean, they're a thread.
[6475.82 → 6476.62] I feel like they're chapters
[6476.62 → 6477.74] in a major podcast.
[6477.86 → 6478.68] They almost are.
[6479.00 → 6479.66] They're like nested
[6479.66 → 6480.02] chapters.
[6480.40 → 6480.52] Yeah.
[6480.52 → 6481.78] So we did five this year,
[6481.92 → 6482.62] five Maidens with
[6482.62 → 6483.04] Gerhard.
[6483.38 → 6484.92] If I had to pick just one,
[6485.32 → 6486.22] it would be the Not a
[6486.22 → 6487.22] Pipe Dream one, the one
[6487.22 → 6488.00] where he took us on that
[6488.00 → 6489.78] journey, and he revealed to
[6489.78 → 6490.98] us over time what was
[6490.98 → 6491.52] going on.
[6491.76 → 6492.12] Yes.
[6492.34 → 6494.10] That was just spectacular.
[6494.62 → 6494.76] But.
[6495.02 → 6495.16] Epic.
[6495.16 → 6496.64] They are all kind of one
[6496.64 → 6498.48] long, windy road.
[6498.60 → 6499.82] And so I'm just going to
[6499.82 → 6500.70] pick all the Maidens.
[6500.94 → 6501.94] I just feel like I'm loving
[6501.94 → 6502.68] what we're doing with
[6502.68 → 6502.98] Kaiden.
[6503.10 → 6505.34] What's happening there is
[6505.34 → 6505.86] interesting.
[6506.06 → 6506.78] I feel like that's probably
[6506.78 → 6507.62] one of the best things we
[6507.62 → 6508.14] did this year.
[6508.68 → 6509.60] So that's breaking the
[6509.60 → 6510.28] rules because I picked
[6510.28 → 6511.34] five episodes as one.
[6511.58 → 6511.80] Yeah.
[6511.90 → 6512.78] It just counts as one.
[6513.26 → 6513.86] I'm going to break the
[6513.86 → 6514.62] rules one more time.
[6514.68 → 6515.16] Oh, gosh.
[6515.54 → 6517.16] And I'm going to pick the
[6517.16 → 6518.26] episodes from that
[6518.26 → 6518.72] conference.
[6519.40 → 6519.60] Oh.
[6519.92 → 6520.76] So this is two for the
[6520.76 → 6521.36] price of one.
[6521.68 → 6522.02] Nice.
[6522.02 → 6523.22] You have how many open
[6523.22 → 6523.68] tabs?
[6523.68 → 6524.28] Yes.
[6524.96 → 6526.70] That was with Nick
[6526.70 → 6529.56] Needed, Amy Dutton, and
[6529.56 → 6531.52] Andres Pineda.
[6531.74 → 6532.26] Andres.
[6532.56 → 6532.86] Yeah.
[6532.94 → 6533.60] And the second one was
[6533.60 → 6535.30] Future of Energy,
[6535.58 → 6536.78] Content, Food.
[6537.42 → 6538.22] And that was with a bunch
[6538.22 → 6539.02] of people as well.
[6539.32 → 6540.88] We had Samuel Goff,
[6541.14 → 6541.78] Future of Energy.
[6542.14 → 6543.80] We talked with YouTuber
[6543.80 → 6545.56] Jess Chan from the
[6545.56 → 6546.96] Coder channel.
[6547.12 → 6547.84] And then you did one
[6547.84 → 6548.54] without me because I had
[6548.54 → 6549.18] to leave earlier than
[6549.18 → 6549.36] you.
[6549.54 → 6549.90] Mm-hmm.
[6549.90 → 6551.74] With Vanessa Via and
[6551.74 → 6552.78] Noah Jenkins all about
[6552.78 → 6553.96] AG tech and the future
[6553.96 → 6554.44] of food.
[6555.12 → 6556.52] I thought both of those
[6556.52 → 6558.16] episodes turned out
[6558.16 → 6558.74] awesome.
[6558.92 → 6559.06] Yeah.
[6559.06 → 6559.54] And all those
[6559.54 → 6560.50] conversations were good.
[6560.90 → 6562.40] There wasn't a dud in
[6562.40 → 6562.80] the mix.
[6563.12 → 6564.16] And so I'm picking those
[6564.16 → 6565.70] two as a bundle as one
[6565.70 → 6567.24] of my top five of the
[6567.24 → 6567.46] year.
[6567.68 → 6567.92] Mm-hmm.
[6567.92 → 6568.12] Okay.
[6568.40 → 6568.94] I dig it.
[6569.10 → 6569.34] Okay.
[6569.80 → 6570.20] Nice.
[6570.54 → 6572.56] Number four, The Man
[6572.56 → 6574.28] Behind the Sandwich with
[6574.28 → 6575.06] Adam Lessor.
[6575.06 → 6577.16] I just really enjoyed
[6577.16 → 6577.84] that conversation.
[6578.34 → 6578.52] Mm-hmm.
[6578.58 → 6580.72] Adam is so smart and
[6580.72 → 6582.44] experienced and deep.
[6583.10 → 6583.64] I feel like we went
[6583.64 → 6584.76] really deep places there.
[6585.44 → 6586.18] And I remember making
[6586.18 → 6586.88] clips, and I'm like,
[6586.94 → 6588.12] I got like seven clips
[6588.12 → 6588.36] here.
[6588.90 → 6589.92] I just, I have to stop
[6589.92 → 6590.66] clipping this because
[6590.66 → 6591.46] there's so many good
[6591.46 → 6591.86] parts.
[6592.36 → 6594.04] Fun talk about Apple
[6594.04 → 6595.08] Vision Pro and what
[6595.08 → 6595.90] they're doing there with
[6595.90 → 6596.62] Sandwich Theatre.
[6597.40 → 6598.30] I love that one.
[6598.80 → 6599.80] I've been a fan of his
[6599.80 → 6601.94] for a long time and was
[6601.94 → 6602.66] excited to meet him.
[6603.42 → 6604.20] And he delivered.
[6604.20 → 6606.26] And my last one, top
[6606.26 → 6606.88] five favourite.
[6607.74 → 6608.48] This is Change Dog and
[6608.48 → 6608.82] Friends.
[6609.26 → 6610.96] Starbucks DVD Peddlers
[6610.96 → 6613.02] with Emily Freeman and
[6613.02 → 6613.74] Justin Garrison.
[6614.16 → 6615.30] That conversation went
[6615.30 → 6616.40] off the rails in every
[6616.40 → 6617.66] great way possible.
[6617.96 → 6619.38] I remember thinking I
[6619.38 → 6620.78] was excited to have a
[6620.78 → 6621.64] conversation with them,
[6621.80 → 6623.18] but coming into it, the
[6623.18 → 6624.16] topic that we were
[6624.16 → 6624.90] supposed to be talking
[6624.90 → 6626.18] about just wasn't
[6626.18 → 6627.04] hidden for me at the
[6627.04 → 6627.20] moment.
[6627.26 → 6627.98] It was like Derrel
[6627.98 → 6629.14] stuff, which we had
[6629.14 → 6629.90] already just done a
[6629.90 → 6630.64] Derrel episode with
[6630.64 → 6632.02] SIX maybe a month
[6632.02 → 6632.48] prior.
[6632.48 → 6634.82] And maybe that's why,
[6634.90 → 6635.66] but like it just never
[6635.66 → 6636.12] got to that.
[6636.22 → 6637.48] The Derrel part is like
[6637.48 → 6638.36] the last 20 minutes
[6638.36 → 6638.64] maybe.
[6638.82 → 6639.62] And the conversation
[6639.62 → 6641.06] just went wild about
[6641.06 → 6643.36] DVDs and nostalgia,
[6643.64 → 6645.88] the 90s and so many
[6645.88 → 6646.52] good laughs.
[6646.94 → 6647.74] Selling things and
[6647.74 → 6648.46] meeting people at,
[6648.92 → 6650.04] no, selling DVDs and
[6650.04 → 6650.40] meeting them at
[6650.40 → 6650.60] Starbucks.
[6650.92 → 6652.30] Yeah, buying DVDs from
[6652.30 → 6653.26] people at Starbucks.
[6653.52 → 6655.08] And then like even
[6655.08 → 6655.94] listening back to it,
[6655.98 → 6656.84] I was laughing because
[6656.84 → 6657.90] like me and Emily are
[6657.90 → 6659.40] just awestruck by
[6659.40 → 6660.32] Justin doing this.
[6660.32 → 6661.00] And he's like, why,
[6661.10 → 6661.56] why wouldn't I?
[6661.64 → 6662.22] I'm like, because you
[6662.22 → 6663.12] might be murdered, you
[6663.12 → 6663.24] know?
[6663.30 → 6664.72] I mean, she goes,
[6664.78 → 6665.90] that's wild.
[6666.14 → 6666.88] We're just having so
[6666.88 → 6667.40] much fun.
[6667.64 → 6668.20] I like to meet people
[6668.20 → 6669.36] at police stations.
[6669.74 → 6670.48] By choice or because
[6670.48 → 6671.24] they make you go there?
[6672.68 → 6673.84] Well, like I once
[6673.84 → 6674.98] sold a bicycle.
[6675.40 → 6675.92] Do you ride in the
[6675.92 → 6676.50] back of the car?
[6677.46 → 6677.90] No, no, no.
[6678.04 → 6678.26] Okay.
[6679.00 → 6679.94] Well, no, I literally
[6679.94 → 6680.66] will say, hey, if you
[6680.66 → 6681.22] want to buy this thing
[6681.22 → 6682.00] for me, meet me at the
[6682.00 → 6682.24] police station.
[6682.24 → 6682.98] That's a great place to
[6682.98 → 6683.40] meet somebody.
[6683.50 → 6683.66] Yeah.
[6683.88 → 6684.30] A hundred percent
[6684.30 → 6685.06] not getting murdered
[6685.06 → 6685.40] there.
[6685.74 → 6686.02] Exactly.
[6686.46 → 6687.00] It's a maybe.
[6687.00 → 6688.68] Actually, it might be.
[6689.24 → 6691.40] It's so obviously safe
[6691.40 → 6692.80] that it's not safe.
[6693.28 → 6693.66] Right.
[6693.84 → 6695.08] So good by fire.
[6695.34 → 6696.44] So just a real quick
[6696.44 → 6696.98] recap.
[6697.62 → 6698.70] My top five forty
[6698.70 → 6700.70] Kaiden's that
[6700.70 → 6702.16] conference, the man
[6702.16 → 6702.78] behind the sandwich
[6702.78 → 6704.06] and Starbucks DVD
[6704.06 → 6704.70] peddlers.
[6704.86 → 6705.16] Your turn.
[6705.82 → 6707.44] Now, were these
[6707.44 → 6708.54] episodes you mentioned
[6708.54 → 6709.80] ones that were
[6709.80 → 6711.06] delimited from the
[6711.06 → 6712.28] list of ones already
[6712.28 → 6712.78] mentioned?
[6713.78 → 6714.96] So nobody mentioned,
[6715.10 → 6716.18] I think any of those,
[6716.18 → 6716.96] I think that I think
[6716.96 → 6717.90] our conference hallway
[6717.90 → 6718.76] tracks were kind of
[6718.76 → 6719.38] mentioned by a few
[6719.38 → 6719.68] people.
[6719.88 → 6720.16] Yes.
[6720.38 → 6721.04] But I do have some
[6721.04 → 6721.58] honourable mentions,
[6721.74 → 6722.38] which I'll let you go
[6722.38 → 6723.16] first, and then I'll see
[6723.16 → 6723.80] because some of those
[6723.80 → 6724.50] have been picked
[6724.50 → 6724.78] already.
[6724.94 → 6725.58] But yeah, these are all
[6725.58 → 6726.88] pretty much standalones.
[6727.24 → 6728.08] Should I share my
[6728.08 → 6729.06] entire list or should I
[6729.06 → 6729.86] share the list that
[6729.86 → 6730.60] hasn't been shared
[6730.60 → 6730.92] already?
[6731.40 → 6732.18] Share your list that
[6732.18 → 6732.86] hasn't been shared.
[6733.68 → 6734.56] Number one,
[6735.46 → 6736.46] Change Log Interviews
[6736.46 → 6737.36] 615.
[6737.84 → 6738.90] Rails is having a
[6738.90 → 6739.82] moment again.
[6740.10 → 6740.60] Good one.
[6740.84 → 6741.24] Good one.
[6741.38 → 6741.68] Yes.
[6742.30 → 6743.24] Into the Baba verse
[6743.24 → 6744.64] episode 603.
[6745.06 → 6746.02] Because why not?
[6746.60 → 6747.58] I'm concurring with you
[6747.58 → 6747.94] on this one,
[6747.98 → 6748.50] The Man Behind the
[6748.50 → 6749.64] Sandwich, 601.
[6749.80 → 6750.10] Nice.
[6750.54 → 6751.58] In the beginning of
[6751.58 → 6752.62] Generative AI,
[6753.02 → 6755.08] episode 576.
[6755.24 → 6755.66] Joe Reese.
[6756.46 → 6757.02] You know, that was so
[6757.02 → 6757.90] long, I kind of forget
[6757.90 → 6758.78] it was this year.
[6758.96 → 6759.60] It does feel like a
[6759.60 → 6760.20] long time ago.
[6760.40 → 6761.04] Well, we did 100
[6761.04 → 6763.06] episodes, so they add
[6763.06 → 6763.64] up, and you think,
[6763.72 → 6764.40] that feels like a lot
[6764.40 → 6765.20] of episodes ago.
[6765.40 → 6766.08] But it was only like,
[6766.26 → 6767.08] was that March,
[6767.18 → 6768.28] April, February?
[6768.58 → 6768.96] I don't know.
[6769.32 → 6769.96] Big fan of Joe
[6769.96 → 6771.72] Reese, data engineering
[6771.72 → 6773.06] guy and happy.
[6773.06 → 6773.94] We actually went on
[6773.94 → 6775.08] his pod after that.
[6775.88 → 6777.28] And I'm glad to have
[6777.28 → 6777.66] him back on.
[6777.70 → 6777.98] He's a great
[6777.98 → 6778.66] conversationalist,
[6778.70 → 6779.20] has lots of cool
[6779.20 → 6779.56] stories.
[6779.98 → 6780.64] That was fun too,
[6780.72 → 6781.46] going on his podcast.
[6781.66 → 6782.28] I feel like we went
[6782.28 → 6782.98] there and had no
[6782.98 → 6783.48] topics.
[6784.02 → 6784.34] Yes.
[6784.54 → 6784.80] Right?
[6785.26 → 6785.74] Pretty much.
[6785.86 → 6786.50] Where can we go,
[6786.62 → 6787.50] basically, was the
[6787.50 → 6788.04] conversation.
[6788.40 → 6788.76] That was cool.
[6788.90 → 6789.16] Right.
[6789.16 → 6790.12] I appreciate that
[6790.12 → 6791.04] about Joe that he
[6791.04 → 6792.16] did that because,
[6792.28 → 6793.26] I mean, one, you
[6793.26 → 6793.78] can say he didn't
[6793.78 → 6794.78] plan or two, you
[6794.78 → 6796.00] can say he didn't
[6796.00 → 6796.62] plan on purpose.
[6797.26 → 6797.82] There you go.
[6799.50 → 6800.58] I know which one he
[6800.58 → 6801.10] might say.
[6801.38 → 6802.06] This one here was
[6802.06 → 6804.12] also early last year.
[6804.20 → 6804.74] It's actually one
[6804.74 → 6805.84] episode before that,
[6806.44 → 6808.36] episode 5, 7, 5,
[6808.70 → 6809.16] Shift Left.
[6809.64 → 6809.96] Seriously.
[6810.42 → 6810.74] Ah.
[6810.98 → 6811.58] I feel like that was
[6811.58 → 6812.32] a perfect show on
[6812.32 → 6813.14] the Shift Left idea.
[6813.24 → 6813.80] I mean, Shift Left
[6813.80 → 6814.62] has been said a lot,
[6815.16 → 6815.96] but I think the thing
[6815.96 → 6817.02] I took away mainly
[6817.02 → 6819.00] from that was it's
[6819.00 → 6819.74] always been said,
[6819.92 → 6820.64] like, who shifts
[6820.64 → 6820.98] left?
[6821.28 → 6821.96] Developers, obviously.
[6822.04 → 6822.52] It's going to shift
[6822.52 → 6823.12] left into the
[6823.12 → 6823.74] development cycle.
[6824.06 → 6824.40] Right.
[6824.56 → 6825.74] But for me, I think
[6825.74 → 6826.80] I even said it, and
[6826.80 → 6827.40] it was me saying it,
[6827.44 → 6828.10] like, my aha moment
[6828.10 → 6829.58] was that it doesn't
[6829.58 → 6830.94] have to be developers
[6830.94 → 6831.86] shifting left, that
[6831.86 → 6832.66] it's in development.
[6833.10 → 6834.00] So it could be those
[6834.00 → 6835.60] around the, you know,
[6835.66 → 6836.50] the dev cycles.
[6836.68 → 6836.94] It doesn't have to
[6836.94 → 6837.64] just be the developer
[6837.64 → 6838.20] writing the code.
[6838.28 → 6839.38] It could be the team
[6839.38 → 6840.18] playing the software
[6840.18 → 6841.46] and the product team.
[6841.54 → 6842.34] It could be that
[6842.34 → 6843.32] Shift Left isn't just
[6843.32 → 6844.74] simply a developer
[6844.74 → 6846.30] task to pick up.
[6846.46 → 6847.10] It's not the who,
[6847.20 → 6847.66] it's the when.
[6847.88 → 6848.06] Yeah.
[6848.38 → 6848.72] It's not the who,
[6848.72 → 6849.00] this will win.
[6849.08 → 6849.38] Thank you.
[6849.42 → 6849.56] Yeah.
[6849.68 → 6850.18] That's what I said.
[6850.54 → 6850.94] I know you did.
[6851.00 → 6851.30] I remember you
[6851.30 → 6851.78] saying it.
[6853.32 → 6854.00] That's my list.
[6854.10 → 6854.76] That's my list of
[6854.76 → 6855.24] ones that haven't
[6855.24 → 6855.62] been mentioned.
[6855.74 → 6856.18] Oh, those are,
[6856.48 → 6857.08] those are not
[6857.08 → 6857.76] mentioned because all
[6857.76 → 6858.20] the rest of them
[6858.20 → 6858.78] have been hit on
[6858.78 → 6859.08] the head.
[6859.24 → 6859.60] Like, Right to
[6859.60 → 6860.90] Repair, Sun to
[6860.90 → 6862.28] Oxide, Adam
[6862.28 → 6863.22] Jacob, System
[6863.22 → 6863.66] Initiative.
[6864.20 → 6864.66] Retired Not
[6864.66 → 6865.12] Tired.
[6865.60 → 6866.00] USA.
[6866.60 → 6866.92] Yes.
[6867.12 → 6867.96] USA was.
[6868.34 → 6868.74] Is it on there?
[6868.92 → 6869.66] I mean, I had a
[6869.66 → 6870.10] long list.
[6870.16 → 6870.70] It didn't make my
[6870.70 → 6871.26] list because it's
[6871.26 → 6872.00] such a long list.
[6872.58 → 6873.10] The Moneyball
[6873.10 → 6873.96] Approach, Best
[6873.96 → 6874.84] Worst Codebase,
[6875.32 → 6875.80] Open Source
[6875.80 → 6876.28] Threaded Team
[6876.28 → 6876.72] Chats.
[6876.96 → 6877.78] Best Worst Codebase
[6877.78 → 6878.48] is in my honourable
[6878.48 → 6878.80] mentions.
[6879.16 → 6879.60] Open Source
[6879.60 → 6880.02] Threaded Team
[6880.02 → 6880.64] Chat is in my
[6880.64 → 6881.88] honourable mentions.
[6882.28 → 6882.42] Yeah.
[6882.52 → 6883.12] The Wu-Tang Wei
[6883.12 → 6883.96] with Ron Evans is
[6883.96 → 6884.82] in my honourable
[6884.82 → 6885.92] mentions as well as,
[6885.96 → 6886.40] this one hasn't
[6886.40 → 6886.90] been said yet,
[6887.26 → 6888.14] The Winamp Era
[6888.14 → 6889.40] with Jordan Eldridge.
[6890.40 → 6891.12] Yeah, that was a
[6891.12 → 6892.08] fun one even to
[6892.08 → 6892.90] come up with because
[6892.90 → 6894.46] when I saw what he
[6894.46 → 6895.86] was spelunking into
[6895.86 → 6896.46] when it came to
[6896.46 → 6897.06] those Winamp
[6897.06 → 6897.72] themes, I'm like,
[6897.80 → 6898.52] wow, that is some
[6898.52 → 6899.32] cool stuff there.
[6900.22 → 6900.88] And I think I
[6900.88 → 6901.30] shared that with you
[6901.30 → 6901.56] and you're like,
[6901.60 → 6902.02] yeah, that's dope.
[6902.08 → 6902.48] Let's do it.
[6902.48 → 6903.72] And so we did it.
[6904.36 → 6904.76] Paraphrasing.
[6904.88 → 6905.20] Of course, I don't
[6905.20 → 6905.64] think you ever said
[6905.64 → 6906.12] the word dope.
[6906.18 → 6906.98] I say the word dope.
[6907.72 → 6907.94] Dope.
[6908.04 → 6909.06] I call people dopes.
[6909.28 → 6909.96] Well, that's not nice.
[6910.48 → 6911.34] Yeah, just my kids.
[6911.78 → 6912.10] Yeah.
[6912.36 → 6913.04] Well, you know,
[6913.10 → 6914.26] it's been a fun year.
[6914.50 → 6915.06] It's been,
[6915.54 → 6916.48] is this the first year
[6916.48 → 6916.98] where we've,
[6917.48 → 6918.22] was Friends around
[6918.22 → 6919.02] all last year?
[6919.46 → 6920.32] Like end to end
[6920.32 → 6920.96] all last year?
[6921.14 → 6921.80] I don't think so.
[6921.84 → 6922.58] I think we started
[6922.58 → 6923.58] Friends last year.
[6924.18 → 6924.48] Yeah.
[6924.74 → 6925.28] And this was probably
[6925.28 → 6926.02] the first year
[6926.02 → 6927.14] we've done Friends
[6927.14 → 6928.28] through and through.
[6928.84 → 6930.16] This will be episode
[6930.16 → 6932.04] 74 of Friends.
[6932.04 → 6932.84] So there you go.
[6932.92 → 6933.56] You have a 52
[6933.56 → 6935.12] plus a 20 something.
[6935.84 → 6936.06] Yeah.
[6936.32 → 6936.68] So yeah,
[6936.76 → 6937.92] first full year of Friends.
[6938.24 → 6938.86] What I was trying to make
[6938.86 → 6939.40] was I think it was
[6939.40 → 6939.92] the first year
[6939.92 → 6940.44] where we had
[6940.44 → 6941.88] two shows a week
[6941.88 → 6942.76] all year long
[6942.76 → 6943.86] January to December.
[6944.22 → 6944.54] Right.
[6944.82 → 6945.38] And that's why
[6945.38 → 6946.14] it feels like a lot.
[6946.24 → 6946.94] That's like a
[6947.44 → 6947.66] I don't know,
[6947.72 → 6948.06] episodes.
[6948.46 → 6948.64] Yeah.
[6948.70 → 6948.86] It's like,
[6949.02 → 6950.00] it's a lot of shows.
[6950.16 → 6950.90] 101 technically.
[6951.08 → 6951.42] Somehow we,
[6951.88 → 6952.46] and by the end of the year
[6952.46 → 6953.32] we'll have 103
[6953.32 → 6954.16] because we have
[6954.16 → 6955.22] Ghost and this one.
[6955.50 → 6956.56] How do we bonus some shows?
[6956.60 → 6957.10] That's crazy.
[6957.36 → 6958.08] Well, we did some bonuses.
[6958.28 → 6958.44] Yeah.
[6958.84 → 6959.32] What do you think
[6959.32 → 6960.70] was the through line
[6960.70 → 6961.42] to the year
[6961.42 → 6962.64] in terms of,
[6963.26 → 6963.84] there wasn't like
[6963.84 → 6964.62] a consistent,
[6965.24 → 6966.60] this is the change
[6966.60 → 6967.24] or the trend line.
[6967.36 → 6967.82] I feel like.
[6967.94 → 6969.58] Like the year of this
[6969.58 → 6970.98] where this is something.
[6971.28 → 6971.56] Yeah.
[6971.56 → 6973.18] like AI didn't get
[6973.18 → 6974.48] touched on a lot this year
[6974.48 → 6975.48] even though I think it did.
[6975.64 → 6976.02] I mean,
[6976.66 → 6978.06] we talked about AI loosely
[6978.06 → 6978.60] I believe in
[6978.60 → 6979.64] The Man Behind the Sandwich.
[6980.06 → 6980.44] Mm-hmm.
[6980.78 → 6981.24] You know,
[6981.54 → 6982.74] obviously in the beginning
[6982.74 → 6983.62] of Generative AI
[6983.62 → 6984.72] with Joe Reese.
[6985.16 → 6986.24] That was right in the title
[6986.24 → 6986.90] there itself.
[6987.40 → 6988.24] I feel like AI
[6988.24 → 6989.12] didn't play a major
[6989.12 → 6990.66] conversational role
[6990.66 → 6991.60] in all these.
[6992.32 → 6992.82] We didn't talk about
[6992.82 → 6994.30] with DHH at all.
[6994.48 → 6994.76] No.
[6994.84 → 6995.88] Or the Moneyball approach.
[6996.08 → 6996.36] No.
[6996.50 → 6997.20] With John Una maker.
[6997.84 → 6998.98] Or the Best Worst Codebase.
[6999.48 → 6999.74] No.
[6999.74 → 7000.94] So I think we kind of kept it
[7000.94 → 7001.94] somewhat AI-free.
[7002.32 → 7002.86] I think so.
[7003.20 → 7004.20] Mostly AI-free.
[7004.50 → 7005.28] Like mostly local.
[7005.54 → 7006.70] Mostly AI-free.
[7006.88 → 7007.06] Dude,
[7007.14 → 7008.10] mostly local is a way to go.
[7008.32 → 7008.50] Yeah,
[7008.52 → 7008.84] I don't know if there was
[7008.84 → 7010.14] any major theme for the year.
[7010.30 → 7011.08] As some of our listeners
[7011.08 → 7011.64] pointed out,
[7011.84 → 7012.92] we obviously camped out
[7012.92 → 7013.74] in certain areas.
[7013.90 → 7014.92] There's the home lab area.
[7015.62 → 7016.54] There's the programming
[7016.54 → 7017.50] languages area.
[7018.38 → 7020.86] There's the culture area.
[7020.96 → 7022.20] There's the open source area.
[7023.10 → 7024.40] And I don't know
[7024.40 → 7024.90] if I had to like
[7024.90 → 7025.48] pick one thing.
[7025.56 → 7025.84] It's like,
[7025.90 → 7026.50] how about like
[7026.50 → 7028.58] realistic and healthy
[7028.58 → 7029.20] relationships
[7029.20 → 7030.64] with technology
[7030.64 → 7031.70] and the industry?
[7032.24 → 7032.50] Mm-hmm.
[7032.54 → 7033.12] Something like that.
[7033.50 → 7033.74] Yeah.
[7033.74 → 7035.14] I think a lot of the patina
[7035.14 → 7036.42] of tech
[7036.42 → 7037.44] is showing.
[7038.30 → 7039.34] And we're having,
[7039.62 → 7039.78] I think,
[7039.84 → 7040.66] more of a
[7040.66 → 7042.34] appropriate view
[7042.34 → 7043.64] of both
[7043.64 → 7045.04] technology itself
[7045.04 → 7046.32] and the companies
[7046.32 → 7047.22] that we work for
[7047.22 → 7048.86] than in the past.
[7049.08 → 7049.74] And I think it's been realized
[7050.30 → 7051.74] and shown this year.
[7052.14 → 7052.50] Mm-hmm.
[7052.60 → 7053.58] Amongst other trends,
[7053.62 → 7054.08] of course.
[7054.08 → 7056.14] the open source
[7056.14 → 7057.00] deal,
[7057.92 → 7058.18] you know,
[7058.26 → 7059.96] going non-open source
[7059.96 → 7060.96] and then back again
[7060.96 → 7061.62] for Elastic,
[7061.80 → 7062.64] but then a lot of
[7062.64 → 7064.24] companies choosing
[7064.24 → 7065.54] to go non-open source
[7065.54 → 7066.74] and go fair source,
[7067.04 → 7068.00] business source,
[7068.70 → 7069.42] that whole deal.
[7070.14 → 7070.50] I don't know.
[7070.70 → 7070.86] Mm-hmm.
[7070.86 → 7071.58] I'm just rambling.
[7072.24 → 7073.04] You asked a hard question.
[7073.18 → 7073.72] I don't have answers.
[7074.20 → 7074.80] Slight ramble.
[7075.20 → 7075.90] Somebody mentioned,
[7075.98 → 7076.78] I forget whom,
[7076.96 → 7077.52] with their voicemail,
[7077.52 → 7079.26] mentioned episode 70,
[7079.98 → 7080.66] bus factors
[7080.66 → 7082.18] and conspiracy theories.
[7082.18 → 7082.92] I think that,
[7083.06 → 7083.48] Yeah.
[7083.64 → 7085.60] I enjoy solo shows
[7085.60 → 7086.54] with you just as much
[7086.54 → 7087.60] as a guest
[7087.60 → 7088.66] and I'm glad people
[7088.66 → 7089.18] like those
[7089.18 → 7089.66] because I think we,
[7089.78 → 7091.26] we do have some,
[7091.54 → 7091.82] you know,
[7091.88 → 7092.40] some good,
[7092.84 → 7093.54] some good stuff,
[7093.60 → 7094.08] let's just say,
[7094.50 → 7095.38] in this kind of shows.
[7095.64 → 7096.62] We are good at talking sometimes.
[7096.88 → 7098.00] We are good at talking.
[7098.64 → 7099.44] I will say,
[7099.52 → 7099.92] now that I'm looking
[7099.92 → 7100.70] at this list,
[7100.88 → 7102.14] there is an honourable mention
[7102.14 → 7103.02] I want to bring up.
[7103.26 → 7103.48] Okay.
[7103.48 → 7104.38] And I really,
[7104.64 → 7104.84] really,
[7104.96 → 7105.84] really enjoyed
[7105.84 → 7106.56] the listen back.
[7106.68 → 7106.80] So,
[7106.90 → 7107.12] I mean,
[7107.26 → 7108.24] I don't always listen
[7108.24 → 7108.62] to our shows
[7108.62 → 7108.98] because obviously
[7108.98 → 7109.62] I'm like there.
[7110.44 → 7111.58] But I do listen to
[7111.58 → 7112.44] parts.
[7112.56 → 7113.10] That's why I appreciate
[7113.10 → 7113.52] our chapters.
[7113.64 → 7113.80] I'm like,
[7113.84 → 7114.36] I was there.
[7114.48 → 7115.04] I'm in a chapter.
[7115.12 → 7115.78] I'm going to jump around.
[7115.96 → 7116.32] I'm not going to,
[7116.34 → 7117.16] You're going to Cypress Hill
[7117.16 → 7117.60] that thing.
[7117.72 → 7117.90] You know,
[7117.94 → 7119.04] go all in and listen to it
[7119.04 → 7119.44] end to end.
[7119.54 → 7119.68] Yeah.
[7121.10 → 7122.26] Shop talking friends.
[7122.96 → 7123.16] Yeah.
[7123.28 → 7123.34] Yeah.
[7123.66 → 7124.24] I mean,
[7124.52 → 7125.18] I thoroughly,
[7125.68 → 7126.04] truly,
[7126.04 → 7127.54] really enjoyed
[7127.54 → 7129.28] having Chris and Dave on.
[7129.38 → 7130.44] I feel like we literally
[7130.44 → 7131.18] were sitting down
[7131.18 → 7131.80] with friends.
[7132.84 → 7133.80] And we were obviously,
[7134.34 → 7135.44] but I think that's,
[7135.76 → 7136.56] that to me was just
[7136.56 → 7136.84] like a
[7136.92 → 7137.52] such a fun,
[7138.18 → 7139.22] even the way it opened up
[7139.22 → 7140.82] with like me telling Dave
[7140.82 → 7142.46] that he wasn't on brand
[7142.46 → 7143.00] with his,
[7143.06 → 7143.40] you know,
[7144.20 → 7146.12] his all caps or camel cases.
[7146.24 → 7147.04] And he let me fix that.
[7147.08 → 7147.96] And then it turned into like,
[7148.44 → 7149.28] was that a web socket
[7149.28 → 7150.02] behind the scenes?
[7150.06 → 7150.62] That just opened up
[7150.62 → 7151.16] the conversation
[7151.16 → 7151.90] just naturally.
[7152.00 → 7152.96] There was no real true,
[7153.04 → 7154.42] true beginning to the show.
[7155.06 → 7156.84] We just opened up there.
[7157.28 → 7158.64] And I think just the conversation
[7158.64 → 7159.04] was,
[7159.28 → 7161.10] there was no true plan
[7161.10 → 7162.48] because that's what
[7162.48 → 7162.96] you're doing anyway,
[7163.02 → 7163.10] right?
[7163.12 → 7163.70] You're just going to sit down
[7163.70 → 7164.26] and talk to people.
[7164.26 → 7164.56] So,
[7164.56 → 7164.94] right.
[7165.14 → 7166.22] I like when that works out
[7166.22 → 7167.10] to our betterment,
[7167.16 → 7167.38] when,
[7167.68 → 7168.62] when we actually come
[7168.62 → 7170.24] without a true plan,
[7170.54 → 7171.96] there's a version of an idea.
[7172.18 → 7173.40] There's a concept of a plan.
[7173.54 → 7173.74] Yeah,
[7173.74 → 7174.48] there's a concept.
[7174.60 → 7174.70] No,
[7174.74 → 7175.00] I agree.
[7175.04 → 7175.76] That's why I think that
[7175.76 → 7176.96] that conversation
[7176.96 → 7177.96] with Emily and Justin
[7177.96 → 7179.58] just tickled me so much
[7179.58 → 7180.56] because afterwards
[7180.56 → 7181.12] I was like,
[7181.18 → 7182.08] that was just four friends
[7182.08 → 7182.56] hanging out.
[7182.90 → 7184.52] And maybe the through line
[7184.52 → 7185.20] there is like,
[7185.54 → 7186.62] four is better than three.
[7186.84 → 7187.36] Oh yeah.
[7187.56 → 7187.84] Maybe.
[7187.98 → 7188.86] Because it's both those
[7188.86 → 7189.68] produce good,
[7189.72 → 7190.22] like friend,
[7190.28 → 7191.34] like almost party atmosphere
[7191.34 → 7192.00] conversations.
[7192.00 → 7193.94] But that could just be
[7193.94 → 7195.12] a coincidence as well.
[7195.36 → 7195.92] I can probably think
[7195.92 → 7196.50] of some times
[7196.50 → 7197.82] where we've had three
[7197.82 → 7198.90] and it's felt like that as well.
[7199.24 → 7200.44] Like with Matt or Nick,
[7200.56 → 7201.52] but that's like the whole,
[7201.66 → 7202.54] like that is friends
[7202.54 → 7203.12] in a nutshell.
[7203.32 → 7204.52] Like that's so frenzy
[7204.52 → 7205.00] is like,
[7205.66 → 7207.36] let's just get people together
[7207.36 → 7208.86] who are friends
[7208.86 → 7209.62] or want to be friends
[7209.62 → 7210.14] or friendly.
[7210.36 → 7211.34] In the case of Jamie Tana,
[7211.46 → 7212.00] I started off with
[7212.00 → 7213.34] change dog and friendlies
[7213.34 → 7214.70] and becomes a friend
[7214.70 → 7216.28] and let's just talk
[7216.28 → 7217.60] and enjoy each other
[7217.60 → 7219.20] and laugh
[7219.20 → 7221.34] and come up with ideas
[7221.34 → 7223.76] and my question for you is,
[7223.78 → 7224.46] maybe we should end
[7224.46 → 7225.08] after this
[7225.08 → 7225.48] because we're getting
[7225.48 → 7226.02] long in the tooth,
[7226.72 → 7228.82] is change dog plus
[7228.82 → 7229.42] is well known
[7229.42 → 7230.22] for being better.
[7230.48 → 7231.34] But here's a question.
[7231.84 → 7232.96] Is change dog and friends
[7232.96 → 7234.96] better than change dog interview?
[7235.06 → 7235.86] Like then our thing,
[7235.92 → 7236.62] then our show,
[7236.70 → 7237.72] then the thing that we created
[7237.72 → 7238.26] all these years,
[7238.30 → 7239.04] like maybe friends
[7239.04 → 7241.04] is actually the better show.
[7241.58 → 7242.14] I'm going to leave that
[7242.14 → 7243.04] as an open question
[7243.04 → 7244.12] and not as an answered question.
[7245.48 → 7246.54] Something to think about.
[7246.54 → 7247.30] Well,
[7247.54 → 7249.46] I don't know
[7249.46 → 7250.36] if this is a
[7250.36 → 7252.06] indicative or not,
[7252.18 → 7253.44] but I would probably say
[7253.44 → 7254.72] based on my list,
[7254.80 → 7255.00] no.
[7255.46 → 7255.70] Yeah.
[7256.18 → 7256.90] All of my favourites
[7256.90 → 7258.32] were on interviews.
[7259.08 → 7259.86] That's not to say
[7259.86 → 7260.94] that I didn't enjoy friends.
[7261.00 → 7262.04] It's just to say that,
[7262.18 → 7262.42] you know,
[7262.46 → 7263.64] I think that my list
[7263.64 → 7264.74] sort of gravitated there.
[7265.16 → 7265.84] But my favourite titles
[7265.84 → 7266.58] were on friends.
[7266.88 → 7267.78] Of my top five,
[7267.92 → 7268.80] Ghost was an interview.
[7269.62 → 7270.80] The Maidens are friends.
[7271.10 → 7271.32] That,
[7271.80 → 7272.06] Cone,
[7272.14 → 7272.36] those,
[7272.50 → 7272.84] one was,
[7273.30 → 7274.28] I think we did one of each.
[7274.66 → 7275.58] Maybe they're both friends.
[7276.06 → 7276.82] Man Behind the Sandwich
[7276.82 → 7277.30] was an interview.
[7277.54 → 7278.20] And then Starbucks
[7278.20 → 7279.36] DVD Peddlers was friends.
[7279.80 → 7280.72] Wu-Tang Wei was friends.
[7281.02 → 7282.00] Winamp Barrow was friends.
[7282.72 → 7283.52] Open Source Thread,
[7283.62 → 7283.94] Team Chat,
[7284.00 → 7284.58] that was an interview.
[7285.10 → 7285.94] Best Works Codebase,
[7286.02 → 7286.64] that was an interview.
[7286.96 → 7287.38] But it probably
[7287.38 → 7288.16] could have been a friend.
[7288.36 → 7289.22] We broke the rules
[7289.22 → 7290.00] a couple of times too.
[7290.12 → 7290.24] Like,
[7290.26 → 7290.94] I think you may be on
[7290.94 → 7291.42] something with this
[7291.42 → 7292.32] whole three people
[7292.32 → 7293.02] because when it's three,
[7293.10 → 7293.64] it feels like an interview.
[7294.26 → 7294.44] Like,
[7294.50 → 7295.42] 10 years of free code camp
[7295.42 → 7296.20] was on friends.
[7296.52 → 7296.68] Yeah,
[7296.70 → 7297.76] but he's an old friend.
[7297.86 → 7298.42] He's been on the show
[7298.42 → 7299.00] tons of times.
[7299.22 → 7300.04] We weren't interviewing him.
[7300.06 → 7300.44] I know that.
[7300.58 → 7302.38] That's where it's a bendy.
[7302.56 → 7302.64] You know,
[7302.64 → 7303.14] that's a bendy.
[7303.20 → 7304.18] We're trying not to interview him.
[7304.24 → 7305.06] The problem with Quincy,
[7305.62 → 7306.60] there are no problems with him,
[7306.66 → 7307.34] but the challenge,
[7307.76 → 7308.56] the problem,
[7308.80 → 7309.82] here's why Quincy sucks.
[7309.92 → 7310.02] No,
[7310.32 → 7311.80] the challenge with Quincy is
[7311.80 → 7313.26] he answers questions
[7313.26 → 7314.04] like they're interviews.
[7314.24 → 7314.30] Like,
[7314.42 → 7315.26] he's going to give you
[7315.26 → 7315.66] an interview.
[7316.06 → 7316.88] And so it's hard
[7316.88 → 7318.86] to just like riff with him.
[7318.98 → 7319.78] It's not that hard,
[7319.86 → 7320.40] but it feels like
[7320.40 → 7320.94] you're interviewing him
[7320.94 → 7321.60] because he's going to give you
[7321.60 → 7323.24] a two or three-minute response.
[7323.76 → 7324.12] Yes.
[7324.34 → 7325.06] And he's not going to give
[7325.06 → 7325.74] Adam or Jared
[7325.74 → 7326.60] much time to chat.
[7326.92 → 7327.12] No,
[7327.26 → 7328.16] he's a talker,
[7328.22 → 7328.38] man.
[7328.48 → 7328.72] Oof.
[7329.24 → 7329.96] I have one more.
[7330.08 → 7330.60] This is the
[7330.70 → 7331.84] this is the one that broke the rule.
[7331.88 → 7333.28] I think the most potentially
[7333.28 → 7334.26] on friends,
[7334.94 → 7336.26] developer unhappiness.
[7336.46 → 7337.34] With Abby Nova,
[7337.46 → 7338.24] we're talking about,
[7338.68 → 7339.90] I think that one is a show
[7339.90 → 7341.32] that like to set up for a friend.
[7341.56 → 7341.86] Yeah.
[7342.06 → 7343.40] But ended up feeling
[7343.40 → 7344.18] more like an interview.
[7344.58 → 7344.86] Yeah.
[7345.50 → 7346.02] I'm down.
[7346.42 → 7347.16] I'm just saying like,
[7347.22 → 7347.92] it is what it is.
[7348.00 → 7348.92] I think I like them all,
[7349.00 → 7349.24] honestly.
[7349.46 → 7349.84] I mean,
[7349.84 → 7351.14] I do agree that there's,
[7351.28 → 7352.12] there's some,
[7352.24 → 7353.58] there's some good stuff
[7353.58 → 7354.90] on both sides of the fence.
[7355.28 → 7355.90] I didn't need,
[7356.00 → 7356.68] you didn't need to answer.
[7356.68 → 7358.12] I was just leaving it there open.
[7358.24 → 7358.42] Oh,
[7358.64 → 7359.14] oh man.
[7359.56 → 7360.36] But I appreciate you
[7360.36 → 7361.42] taking a crack at it.
[7362.28 → 7363.94] How do we end this year?
[7364.14 → 7364.90] What do we say?
[7365.08 → 7365.96] What do we do
[7365.96 → 7367.28] before we hit stop?
[7367.28 → 7367.42] Well,
[7367.42 → 7368.84] we did drop some major news
[7368.84 → 7370.72] and the only time we talked about it
[7370.72 → 7372.10] was with Gerhard loosely.
[7372.54 → 7372.88] Right.
[7373.60 → 7375.18] Should we talk about that at all?
[7375.60 → 7377.12] Or is there more to say about that?
[7377.76 → 7378.08] Well,
[7378.58 → 7379.84] there'll be a link in the show notes.
[7380.56 → 7381.40] A new era
[7381.40 → 7382.38] coming
[7382.38 → 7383.56] 2025.
[7384.20 → 7384.64] That's right.
[7384.88 → 7385.68] Still percolating.
[7385.68 → 7386.56] You know,
[7386.68 → 7387.48] it's a
[7388.00 → 7389.08] this is a dry brine.
[7389.26 → 7390.00] A drive-by?
[7390.36 → 7391.56] It's a dry brine.
[7391.64 → 7391.76] Oh,
[7391.82 → 7392.98] I thought you called this a drive-by.
[7393.40 → 7393.66] It's like,
[7393.70 → 7394.46] that's not good.
[7394.64 → 7395.10] Dry brine.
[7395.28 → 7396.12] Dry brines are what?
[7396.16 → 7396.94] They're a work in progress?
[7397.16 → 7397.36] Well,
[7397.40 → 7398.12] they take some time.
[7398.14 → 7398.50] It's a whip.
[7398.60 → 7399.34] Let's call this a whip.
[7400.02 → 7400.30] Sure.
[7400.84 → 7402.18] We have some change.
[7402.40 → 7402.76] It's,
[7402.84 → 7404.28] it's clear.
[7404.66 → 7405.62] It's clearly unclear.
[7406.16 → 7407.08] But I would say this,
[7407.12 → 7407.58] this is what I said
[7407.58 → 7408.32] at the end of this one show.
[7408.50 → 7409.04] And I said,
[7409.06 → 7409.28] just,
[7409.36 → 7409.70] just said,
[7409.74 → 7410.46] just trust us.
[7411.06 → 7413.08] Trust us to have
[7413.08 → 7414.16] the best interests
[7414.16 → 7415.48] of all the reasons
[7415.48 → 7417.26] you've shared your voicemails,
[7417.38 → 7418.02] all the reasons
[7418.02 → 7419.54] you've hung out in Zulip,
[7419.62 → 7420.16] all the reasons
[7420.16 → 7420.70] you've listened
[7420.70 → 7422.90] for a few years,
[7423.10 → 7423.82] for many,
[7423.92 → 7424.68] many years,
[7425.44 → 7425.88] et cetera.
[7426.36 → 7427.16] Have some patience
[7427.16 → 7428.26] with the process
[7428.26 → 7429.02] of what we're trying to do.
[7429.12 → 7430.52] We're making some change.
[7430.64 → 7431.38] It's not going to be
[7431.38 → 7432.46] exactly precise,
[7432.80 → 7434.76] but it's mostly precise,
[7435.52 → 7436.12] intentionally
[7436.12 → 7438.08] precise if we can.
[7438.08 → 7439.28] And we're trying our best
[7439.28 → 7439.78] to,
[7439.78 → 7441.36] to move the direction
[7441.36 → 7442.62] that we want to go,
[7442.98 → 7443.92] that it needs to go.
[7444.52 → 7445.52] And that's really it.
[7446.28 → 7446.72] Patience.
[7447.28 → 7447.74] Patience,
[7447.84 → 7448.28] Grasshopper.
[7448.52 → 7448.92] Patience.
[7449.42 → 7451.30] Thank you all for calling in.
[7451.40 → 7452.22] Thank you all for
[7452.22 → 7453.80] listening to us
[7453.80 → 7455.46] and being part of our community.
[7455.46 → 7456.90] If you're not in Zulip yet,
[7457.64 → 7458.64] let's fix that bug.
[7458.94 → 7459.32] Fix it.
[7459.72 → 7460.72] Head to changelog.com
[7460.72 → 7461.38] slash community.
[7462.06 → 7463.42] Sign up for free.
[7464.06 → 7465.02] Throw in your email address.
[7465.12 → 7466.14] Get yourself a Zulip invite.
[7466.14 → 7467.04] Hop into Zulip.
[7467.04 → 7469.38] And hang out with us.
[7469.86 → 7470.54] But other than that,
[7470.56 → 7470.88] we're going to take
[7470.88 → 7471.76] the next couple of weeks off.
[7472.26 → 7472.94] We're going to be
[7472.94 → 7473.50] with our families.
[7473.68 → 7474.52] We're going to be
[7474.52 → 7475.38] chillaxing.
[7475.80 → 7476.68] And we are going to be
[7476.68 → 7477.10] preparing
[7477.10 → 7478.84] for 2025.
[7479.38 → 7480.40] What will it hold?
[7481.10 → 7481.90] We don't know exactly,
[7482.00 → 7482.84] but trust us,
[7483.38 → 7484.22] young Grasshopper.
[7484.84 → 7485.54] Anything else?
[7486.08 → 7486.62] The remixes.
[7486.84 → 7487.44] Thank you, BMC,
[7487.52 → 7488.14] for the
[7488.14 → 7489.78] the extra attention.
[7489.94 → 7490.36] So good.
[7490.52 → 7491.16] So gold.
[7491.42 → 7491.88] So gold.
[7492.84 → 7493.00] Yeah,
[7493.00 → 7494.02] that should be the better
[7494.02 → 7494.68] so good.
[7495.08 → 7496.36] The new so good
[7496.36 → 7497.08] is so gold.
[7497.20 → 7497.70] So gold.
[7497.94 → 7498.38] So gold.
[7498.50 → 7499.88] Like that Zelda cartridge.
[7501.14 → 7501.62] Preach.
[7501.72 → 7502.26] So gold.
[7502.52 → 7502.98] So gold.
[7503.12 → 7503.34] Yeah.
[7503.60 → 7504.22] Thank you, BMC,
[7504.32 → 7505.08] for those beats
[7505.08 → 7507.04] and for just the remixes
[7507.04 → 7508.72] and making this show
[7508.72 → 7510.10] a little more special.
[7510.48 → 7511.38] A little more special.
[7511.54 → 7511.90] Thank you.
[7512.16 → 7512.60] There you go.
[7512.92 → 7513.38] Bye, friends.
[7513.74 → 7514.32] Bye, friends.
[7514.36 → 7514.96] We'll see you
[7514.96 → 7515.84] in the new year.
[7521.26 → 7521.94] All right.
[7522.02 → 7522.74] That is it.
[7522.74 → 7524.82] 2024 is in the bag.
[7524.82 → 7525.96] Can you believe it?
[7526.46 → 7527.72] If you have ideas,
[7528.06 → 7528.68] requests,
[7528.94 → 7530.18] or anything at all
[7530.18 → 7531.12] you'd like to say,
[7531.32 → 7532.40] hop in our Zulip
[7532.40 → 7533.26] and sound off
[7533.26 → 7534.40] on the discussion thread
[7534.40 → 7535.26] for this episode.
[7535.62 → 7536.94] We absolutely love
[7536.94 → 7537.64] hearing from you.
[7538.22 → 7539.20] Thanks one last time
[7539.20 → 7540.12] for listening to our shows
[7540.12 → 7540.56] this year.
[7540.82 → 7542.00] We literally wouldn't be able
[7542.00 → 7543.32] to keep putting out new stuff
[7543.32 → 7544.46] if you all weren't listening.
[7544.72 → 7545.20] So thanks.
[7545.74 → 7546.66] And a huge thanks
[7546.66 → 7548.12] to everyone on our team
[7548.12 → 7549.76] and in the Changelog community
[7549.76 → 7551.02] for everything you do.
[7551.22 → 7552.08] You know who you are.
[7552.08 → 7552.76] But still,
[7552.88 → 7553.72] I'll name a few names.
[7553.92 → 7554.88] BMC, of course.
[7555.14 → 7555.70] Our editors,
[7555.90 → 7556.68] Brian and Jason.
[7557.20 → 7558.62] Alexandru on transcripts.
[7558.74 → 7559.58] Gear heart, of course.
[7559.88 → 7561.08] Our friends and panellists
[7561.08 → 7562.06] on JS Party.
[7562.58 → 7563.02] Go Time,
[7563.14 → 7563.80] Practical AI,
[7564.20 → 7564.58] Ship It,
[7564.68 → 7565.44] all of our pods.
[7565.70 → 7566.38] You all are awesome.
[7566.90 → 7567.80] To our wives,
[7568.20 → 7569.04] Rachel and Heather,
[7569.46 → 7570.32] thank you so much.
[7570.54 → 7571.34] And to our sponsors,
[7571.86 → 7572.54] Fly.io,
[7572.94 → 7573.34] Sentry,
[7573.50 → 7573.84] Wix,
[7573.98 → 7574.28] Shopify,
[7574.62 → 7575.02] Works,
[7575.32 → 7575.78] Retool,
[7576.02 → 7576.48] Neon,
[7576.66 → 7577.10] 8sleep,
[7577.20 → 7578.74] and many more awesome companies
[7578.74 → 7579.68] who support us.
[7580.00 → 7580.48] Thank you.
[7580.76 → 7581.02] Truly.
[7581.02 → 7581.78] Thank you.
[7582.28 → 7582.92] All right.
[7583.06 → 7584.46] That's all for now.
[7584.62 → 7586.38] But let's get together
[7586.38 → 7587.52] and talk a lot more
[7587.52 → 7588.50] next year.
[7611.02 → 7611.66] Finally,
[7611.66 → 7612.72] the end of
[7612.72 → 7614.22] Changelog and Friends
[7614.22 → 7616.04] with Adam and Jared
[7616.04 → 7617.82] and some of the random
[7617.82 → 7619.50] We love that you love
[7619.50 → 7621.34] didn't stay until the end
[7621.34 → 7623.20] But now it's over,
[7623.32 → 7624.82] it's time to go
[7624.82 → 7626.28] We know your problem
[7626.28 → 7627.62] should be coding
[7627.62 → 7629.38] And your deadline
[7629.38 → 7631.26] is pretty foreboding
[7631.26 → 7633.46] Your ticket backlog
[7633.46 → 7635.58] Is an actual problem
[7635.58 → 7638.52] So why don't you go inside
[7638.52 → 7639.80] No more listening
[7639.80 → 7641.90] to Changelog and Friends
[7641.90 → 7643.60] The Batman Chair
[7643.60 → 7645.52] In Silicon Valley
[7645.52 → 7647.24] If no one gave the gag
[7647.24 → 7648.88] We'll come to an end
[7648.88 → 7650.04] But honestly,
[7650.24 → 7652.38] that will probably be our finale
[7652.38 → 7661.80] You best be slinging
[7661.80 → 7663.26] Ones and zeros
[7663.26 → 7665.22] And that makes you
[7665.22 → 7666.86] one of our heroes
[7666.86 → 7669.16] Your list of to-dos
[7669.16 → 7670.96] is waiting for you
[7670.96 → 7673.66] So why don't you go inside
[7673.66 → 7675.32] No more listening
[7675.32 → 7677.48] to Changelog and Friends
[7677.48 → 7679.12] The Batman Chair
[7679.12 → 7680.92] In people you know
[7680.92 → 7682.70] Changelog and Friends
[7682.70 → 7684.20] Time to get back
[7684.20 → 7685.40] into the flow
[7685.40 → 7687.36] Changelog and Friends
[7687.36 → 7689.04] Changelog and Friends
[7689.04 → 7691.08] It's your favourite ever show
[7691.08 → 7693.96] Favourite ever show
