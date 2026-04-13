[0.00 → 3.10] 3, 2, 1
[3.10 → 9.56] This is Ship It
[9.56 → 12.18] with Justin Garrison and Autumn Nash.
[12.56 → 13.76] If you like this show,
[13.96 → 15.38] you will love The Change Log.
[15.86 → 17.40] It's software news on Mondays,
[17.76 → 19.94] deep technical interviews on Wednesdays,
[19.98 → 20.72] and on Fridays,
[21.16 → 22.34] an awesome talk show
[22.34 → 23.98] for your weekend enjoyment.
[24.52 → 26.52] Find it by searching for The Change Log
[26.52 → 28.08] wherever you get your podcasts.
[28.08 → 30.74] Ship It is brought to you by Fly.io.
[31.24 → 33.56] Launch your app in 5 minutes or less.
[33.92 → 35.98] Learn how at Fly.io.
[52.92 → 53.82] What's up, friends?
[53.86 → 54.90] I'm here with Dave Rosenthal,
[55.04 → 56.28] CTO of Century.
[56.78 → 57.74] So Dave, when I look at Century,
[57.74 → 59.16] I see you driving towards
[59.16 → 61.18] full application health.
[61.46 → 62.90] Error monitoring, where things began.
[63.30 → 64.04] Session replay,
[64.26 → 66.50] being able to replay a view of the interface
[66.50 → 68.22] a user had going on
[68.22 → 69.78] when they experienced an issue
[69.78 → 71.34] with full tracing, full data.
[71.68 → 73.28] The advancements you're making with tracing
[73.28 → 74.56] and profiling,
[74.92 → 75.60] Chrome monitoring,
[75.80 → 76.50] co-coverage,
[76.90 → 77.54] user feedback,
[78.10 → 79.94] and just tons of integrations.
[80.36 → 83.04] Give me a glimpse into the inevitable future.
[83.32 → 84.14] What are you driving towards?
[84.14 → 86.06] Yeah, one of the things that we're seeing
[86.06 → 87.74] is that in the past,
[88.06 → 89.36] people had separate systems
[89.36 → 91.10] where they had like logs on servers,
[91.22 → 91.90] written files.
[92.50 → 94.10] They were maybe sending some metrics
[94.10 → 95.88] to Datadog or something like that
[95.88 → 96.84] or some other system.
[97.20 → 98.38] They were monitoring for errors
[98.38 → 99.06] with some product,
[99.16 → 99.78] maybe it was Century.
[100.18 → 101.18] But more and more,
[101.24 → 102.36] what we see is people want
[102.36 → 104.32] all of these sources of telemetry
[104.32 → 106.28] logically tied together somehow.
[106.82 → 108.94] And that's really what we're pursuing
[108.94 → 110.10] at Century now.
[110.10 → 111.88] We have this concept of a trace ID,
[112.20 → 113.26] which is kind of a key
[113.26 → 114.52] that ties together
[114.52 → 116.26] all the pieces of data
[116.26 → 118.00] that are associated with the user action.
[118.42 → 119.70] So if user loads a web page,
[119.96 → 121.10] we want to tie together
[121.10 → 122.88] all the server requests that happened,
[123.06 → 124.42] any errors that happened,
[124.86 → 126.18] any metrics that were collected.
[126.70 → 128.58] And what that allows on the backend,
[129.08 → 130.26] you don't just have to look at
[130.26 → 131.50] like three different graphs
[131.50 → 133.08] and sort of line them up in time
[133.08 → 135.04] and try to draw your own conclusions.
[135.32 → 136.62] You can actually like analyze
[136.62 → 138.24] and slice and dice the data
[138.24 → 140.42] and say, hey, what did this metric look like
[140.42 → 142.06] for people with this operating system
[142.06 → 143.22] versus this metric look like
[143.22 → 144.70] for people with this operating system
[144.70 → 146.60] and actually get into those details.
[146.94 → 148.26] So this kind of idea
[148.26 → 151.64] of tying all the telemetry data together
[151.64 → 153.94] using this concept of a trace ID
[153.94 → 155.30] or basically some key,
[155.52 → 157.46] I think is a big win
[157.46 → 159.38] for developers trying to diagnose
[159.38 → 161.28] and debug real world systems
[161.28 → 162.54] and something that is,
[162.88 → 164.26] we're kind of charged the path
[164.26 → 165.08] for that for everybody.
[165.48 → 165.72] Okay.
[166.08 → 166.96] Let's see you get there.
[167.14 → 168.14] Let's see you get there tomorrow.
[168.48 → 168.58] Yeah.
[168.70 → 169.02] Perfectly.
[169.28 → 170.50] How will systems be different?
[170.74 → 172.80] How will teams be different as a result?
[173.14 → 173.40] Yeah.
[173.50 → 174.66] I mean, I guess, again,
[174.92 → 176.12] I just keep saying it maybe,
[176.26 → 177.60] but I think it kind of goes back
[177.60 → 179.10] to this debuggability experience.
[179.26 → 180.92] When you are digging into an issue,
[181.30 → 182.56] you know, having a sort of
[182.56 → 184.16] a richer data model that's,
[184.28 → 185.80] you know, your logs are structured.
[185.92 → 187.42] They're sort of this hierarchical structure
[187.42 → 188.12] with spans.
[188.12 → 189.80] And not only is it just the spans
[189.80 → 190.42] that are structured,
[190.56 → 191.60] they're tied to errors,
[191.72 → 192.78] they're tied to other things.
[193.06 → 194.48] So when you have the data model
[194.48 → 195.66] that's kind of interconnected,
[195.66 → 198.18] it opens up all different kinds
[198.18 → 200.66] of analysis that were just kind of
[200.66 → 202.42] either very manual before,
[202.66 → 204.74] kind of guessing that maybe this log
[204.74 → 205.42] was, you know,
[205.46 → 206.56] happened at the same time
[206.56 → 207.34] as this other thing,
[207.54 → 208.50] or we're just impossible.
[208.72 → 210.24] We get excited not only about
[210.24 → 211.46] the new kinds of issues
[211.46 → 212.28] that we can detect
[212.28 → 213.70] with that interconnected data model,
[213.70 → 215.12] but also just for every issue
[215.12 → 215.92] that we do detect,
[216.00 → 217.00] how easy it is to get
[217.00 → 217.74] to the bottom of it.
[217.74 → 218.54] I love it.
[218.62 → 219.86] Okay, so they mean it
[219.86 → 220.96] when they say code breaks,
[221.20 → 222.50] fix it faster with Sentry.
[222.74 → 224.72] More than 100,000 growing teams
[224.72 → 226.32] use Sentry to find problems fast,
[226.50 → 227.46] and you can too.
[227.92 → 230.40] Learn more at Sentry.io.
[230.54 → 234.30] That's S-E-N-T-R-Y.io.
[234.90 → 235.92] And use our code,
[236.18 → 236.70] changelog,
[236.80 → 238.94] get $100 off the team plan.
[239.24 → 240.56] That's almost four months free
[240.56 → 241.90] for you to try out Sentry.
[242.20 → 242.82] Once again,
[243.24 → 244.72] Sentry.io.
[244.72 → 244.96] Sentry.io.
[256.98 → 258.70] Hello, and welcome to Ship It,
[258.88 → 260.20] the podcast all about everything
[260.20 → 261.42] after Get Pushed.
[261.50 → 262.62] I'm your host, Justin Garrison,
[262.84 → 264.78] and with me as always is Autumn Nash.
[264.86 → 265.40] How's it going, Autumn?
[266.06 → 267.72] I'm very happy to be here.
[267.96 → 268.84] Slightly caffeinated,
[269.08 → 270.12] like almost there.
[271.14 → 271.64] Getting there.
[271.78 → 272.40] Getting there.
[272.40 → 273.04] A little more coffee.
[273.04 → 275.66] Are we telling people
[275.66 → 276.30] about your new job?
[276.92 → 278.06] Yeah, we're good to go now.
[278.36 → 279.48] I mean, the world knows
[279.48 → 279.96] at this point.
[281.20 → 282.02] That's right, you announced
[282.02 → 282.36] it is on LinkedIn.
[282.46 → 282.82] We're good.
[283.00 → 284.22] So what's your new job?
[284.66 → 287.02] So I am the product manager
[287.02 → 289.68] for Azure Linux.
[290.18 → 292.34] So the Azure Linux distribution
[292.34 → 294.20] at Microsoft.
[294.38 → 295.10] Just started this week.
[295.18 → 295.58] Congratulations.
[295.90 → 296.40] Well, actually,
[296.64 → 298.60] the security product manager.
[298.60 → 300.12] I'm sure there's a lot of PMs
[300.12 → 301.34] on Azure Linux.
[301.34 → 302.78] So I am the one that like
[302.78 → 305.60] works on the security vision
[305.60 → 307.86] for Azure Linux.
[308.06 → 309.38] So anyone listening to the podcast,
[309.48 → 310.06] if you have problems
[310.06 → 311.34] with security on Azure,
[311.46 → 312.00] you know what.
[312.34 → 313.02] Rude, Justin.
[313.44 → 313.90] Rude.
[314.10 → 314.66] Don't lie.
[314.80 → 315.80] The DMs are going to be
[315.80 → 317.44] from you making different accounts.
[317.96 → 317.98] Like,
[319.06 → 319.98] on my bot army.
[321.30 → 321.98] Because what?
[322.50 → 323.12] It's going to be
[323.12 → 324.76] Justin's bot army being like,
[324.92 → 326.50] can you fix this for me?
[326.50 → 328.26] I found a bug.
[329.12 → 330.96] For any long-time listeners
[330.96 → 331.46] of the show,
[331.60 → 332.50] you'll know our guest.
[332.72 → 333.58] How's it going, Gerhard?
[334.22 → 335.14] It's going really well.
[335.48 → 337.16] I'm very happy to be back.
[337.50 → 338.48] This feels very cozy.
[338.86 → 340.12] I'm so excited to meet you.
[340.30 → 341.30] I feel like I'm geeking out.
[341.64 → 341.96] Likewise.
[342.54 → 343.38] I was a long-time listener
[343.38 → 343.76] of the show.
[343.86 → 344.56] I thought it was great.
[344.82 → 345.48] Can you bring us back?
[345.54 → 347.10] Like, why did you start Ship It?
[347.52 → 349.26] It started with all the work
[349.26 → 349.92] that we were doing
[349.92 → 351.26] on Changelog
[351.26 → 352.38] with Adam and Jared.
[352.38 → 353.02] I mean,
[353.06 → 354.04] there was a lot of
[354.04 → 355.80] infra work
[355.80 → 357.64] and setting everything up
[357.64 → 358.90] and going through
[358.90 → 359.60] all the motions
[359.60 → 360.84] that you normally do
[360.84 → 361.80] when you take an application
[361.80 → 362.46] to production.
[362.78 → 363.78] And we've been doing that
[363.78 → 364.28] for,
[364.64 → 365.66] I don't know how many years
[365.66 → 366.70] before Ship It started,
[366.76 → 367.48] but it's been years
[367.48 → 367.96] in the making.
[368.58 → 369.48] And there were blog posts
[369.48 → 370.26] before that.
[370.96 → 372.52] And one day,
[372.82 → 373.56] we realized,
[373.74 → 374.12] actually,
[374.42 → 375.84] there's so much here
[375.84 → 377.02] that we could
[377.02 → 378.06] start a podcast,
[378.42 → 379.30] start a new show
[379.30 → 380.66] if you'd be up for it.
[381.24 → 382.26] And the rest is
[382.26 → 382.58] history.
[383.16 → 384.14] And you carried that on
[384.14 → 385.46] for, I think it was 90 episodes,
[385.62 → 386.22] which was awesome.
[386.86 → 387.56] And then also,
[387.68 → 388.04] we have,
[388.28 → 388.46] like,
[388.54 → 389.44] going full circle
[389.44 → 390.44] from you stopping
[390.44 → 391.18] at the 90th episode,
[391.26 → 391.78] we have some news
[391.78 → 392.64] to share everyone else
[392.64 → 393.66] that Ship It,
[393.74 → 394.56] as this podcast
[394.56 → 395.40] on the Changelog,
[395.80 → 396.66] is going to stop
[396.66 → 397.36] at the end of the year.
[397.44 → 399.02] So at the end of December 2024,
[399.88 → 400.40] don't know when you're
[400.40 → 401.10] listening to this now,
[401.22 → 402.76] but we're stopping
[402.76 → 403.46] the podcast.
[403.82 → 404.18] Again,
[404.26 → 404.56] for you,
[404.56 → 405.60] first time for me
[405.60 → 406.48] and Adam to stop it.
[407.08 → 407.10] Well,
[407.34 → 408.46] that was all news
[408.46 → 409.14] to me as well
[409.14 → 410.64] when we scheduled
[410.64 → 412.76] this conversation.
[413.40 → 413.86] We didn't know
[413.86 → 414.42] about that.
[414.92 → 416.36] And I'm glad
[416.36 → 417.16] that I was able
[417.16 → 418.10] to come back
[418.10 → 418.86] one more time
[418.86 → 420.72] before the original
[420.72 → 421.32] Ship It,
[421.42 → 422.12] in this form,
[422.62 → 424.36] will be put on pause.
[424.46 → 425.26] I always like to say
[425.26 → 425.86] it's on pause.
[426.28 → 427.06] Maybe indefinitely,
[427.84 → 428.74] most likely indefinitely,
[429.14 → 430.12] but you're right.
[430.28 → 431.18] It's like history
[431.18 → 431.92] repeating itself.
[432.38 → 432.54] Yeah.
[432.70 → 432.90] So,
[432.90 → 433.92] and for anyone,
[434.06 → 434.28] you know,
[434.32 → 434.56] listening,
[435.06 → 435.82] sorry about the news
[435.82 → 436.44] breaking it to you.
[436.66 → 437.46] This is a decision
[437.46 → 438.66] for Changelog
[438.66 → 439.58] as the network.
[439.72 → 441.22] They're stripping down,
[441.70 → 442.04] not stripping,
[442.12 → 443.30] they're not going to do
[443.30 → 444.14] a lot of the extra
[444.14 → 445.02] podcasts they were doing.
[445.12 → 446.60] I think Go Time
[446.60 → 447.94] and JS Party,
[448.40 → 449.14] they want to focus
[449.14 → 449.58] on the main
[449.58 → 450.40] Changelog podcast.
[450.78 → 451.40] And that makes
[451.40 → 452.00] total sense to me.
[452.06 → 452.58] I think we have,
[452.58 → 453.26] they're up to seven
[453.26 → 453.80] right now.
[454.04 → 455.08] I came in,
[455.26 → 455.36] and,
[455.46 → 455.62] you know,
[455.70 → 456.48] when we restarted
[456.48 → 456.68] Ship It,
[456.72 → 456.98] we were just like,
[457.04 → 457.64] let's just see
[457.64 → 458.56] what happens.
[459.14 → 459.84] And Autumn and I
[459.84 → 460.98] have been doing this
[460.98 → 461.96] for almost a full year.
[462.50 → 463.36] And they wanted
[463.36 → 464.06] to trim it back.
[464.10 → 464.46] And that makes
[464.46 → 464.80] total sense.
[464.94 → 465.34] Autumn and I
[465.34 → 466.38] are planning on
[466.38 → 467.46] continuing on
[467.46 → 469.50] with some form
[469.50 → 470.26] of this podcast,
[470.46 → 471.28] at least for a little while.
[471.34 → 472.04] We still have
[472.04 → 473.30] a bunch of amazing
[473.30 → 474.16] people to interview
[474.16 → 475.80] about all these
[475.80 → 476.32] different topics
[476.32 → 476.82] that we're just like,
[476.86 → 477.30] you know what?
[477.40 → 477.54] Like,
[477.60 → 478.34] this already has
[478.34 → 478.86] some momentum.
[479.22 → 479.62] We already
[479.62 → 481.04] appreciate everyone
[481.04 → 481.60] that's listening
[481.60 → 483.58] and talking to us
[483.58 → 484.30] and telling us,
[484.64 → 485.20] giving us feedback
[485.20 → 485.62] and telling us
[485.62 → 486.12] what they like
[486.12 → 486.74] about the show.
[487.00 → 487.68] So we want to
[487.68 → 488.16] continue that.
[488.24 → 488.54] We want to,
[488.66 → 489.12] we think there is
[489.12 → 489.96] space for this
[489.96 → 491.86] in the podcast
[491.86 → 492.26] universe.
[492.80 → 493.58] And it's a passion
[493.58 → 494.10] that,
[494.10 → 494.56] you know,
[494.62 → 495.12] Autumn and I
[495.12 → 495.80] and a lot of people
[495.80 → 496.94] share just about
[496.94 → 498.32] infrastructure and technology
[498.32 → 498.96] and just running,
[499.12 → 499.38] you know,
[499.40 → 500.42] responsibility of running
[500.42 → 502.08] software in general.
[502.58 → 503.00] And it's awesome
[503.00 → 503.96] meeting all the people
[503.96 → 504.58] that run,
[504.74 → 505.64] like that maintain
[505.64 → 506.46] and run software
[506.46 → 507.12] and infrastructure.
[507.60 → 508.34] And the variety.
[508.86 → 509.68] Like the variety
[509.68 → 510.16] of people that we,
[510.24 → 511.22] everything from 3D
[511.22 → 511.92] printer software,
[512.04 → 512.64] like the Octobrist
[512.64 → 513.68] stuff to stuff
[513.68 → 514.32] in space.
[514.32 → 515.78] And it's been awesome
[515.78 → 516.56] just learning all
[516.56 → 517.62] of the things
[517.62 → 518.24] that are different
[518.24 → 519.06] and the challenges
[519.06 → 519.92] in each space,
[519.94 → 520.88] but also all the things
[520.88 → 521.46] that are the same.
[521.82 → 521.88] Yeah,
[521.92 → 522.76] that are very much
[522.76 → 523.16] the same
[523.16 → 523.98] in the most
[523.98 → 524.94] hilarious of ways.
[525.52 → 526.34] We should also
[526.34 → 527.30] see if listeners
[527.30 → 528.08] want to send us
[528.08 → 528.66] some ideas
[528.66 → 529.24] for the name
[529.24 → 530.16] of our new podcast
[530.16 → 530.70] because that would
[530.70 → 531.10] be neat.
[531.30 → 531.68] That's going to be
[531.68 → 532.36] unhinged.
[532.54 → 532.76] Yeah,
[532.86 → 534.82] but that's
[534.82 → 535.26] when you get
[535.26 → 536.04] the best stuff.
[538.04 → 538.62] So yeah,
[538.64 → 539.22] so this episode,
[539.32 → 540.04] I think we have
[540.04 → 541.06] three more episodes
[541.06 → 542.02] after this one
[542.02 → 543.08] to finish out
[543.08 → 543.54] the year.
[544.02 → 544.92] And hopefully
[544.92 → 545.98] on that last episode,
[545.98 → 546.76] we will have
[546.76 → 548.58] some more formal
[548.58 → 549.22] announcement about
[549.22 → 550.26] where you can find us,
[550.78 → 551.66] where this is going forward.
[552.28 → 552.88] Jared and Adam
[552.88 → 553.54] have been great
[553.54 → 554.36] and they are
[554.36 → 555.40] encouraging us
[555.40 → 555.92] to continue
[555.92 → 556.94] and allowing us
[556.94 → 558.18] to keep doing this
[558.18 → 558.76] so they might keep
[558.76 → 559.46] some sort of redirect
[559.46 → 560.40] up for people
[560.40 → 560.92] that are listening
[560.92 → 561.52] to this later
[561.52 → 562.66] than the end
[562.66 → 563.26] of 2024.
[564.20 → 564.40] But yeah,
[564.42 → 564.92] we want to be able
[564.92 → 565.90] to keep that going
[565.90 → 566.38] for some people
[566.38 → 566.82] and make it as
[566.82 → 567.66] seamless as possible,
[567.80 → 568.38] but also like
[568.38 → 568.68] you're probably
[568.68 → 569.04] going to have to
[569.04 → 569.72] add a new feed
[569.72 → 571.30] in your podcast listener.
[571.92 → 572.52] I'm really excited
[572.52 → 572.76] though.
[572.86 → 573.20] I feel like
[573.20 → 575.00] this just allows
[575.00 → 576.00] for like a new
[576.00 → 577.16] evolution of Ship It.
[577.52 → 577.80] Yeah.
[578.22 → 578.52] I mean,
[578.52 → 579.56] you had 40 episodes,
[579.72 → 579.84] right?
[579.94 → 580.44] Nine months.
[580.96 → 582.00] More than 40 actually
[582.00 → 582.54] at this point,
[582.64 → 583.30] close to 50.
[583.94 → 584.60] How would you
[584.60 → 585.24] summarize that
[585.24 → 585.92] in a few words?
[586.60 → 587.56] All the episodes
[587.56 → 588.56] that you've done
[588.56 → 589.24] so far
[589.24 → 591.52] in this format?
[591.88 → 592.46] I think kind of
[592.46 → 593.10] going back to what
[593.10 → 593.50] Justin said,
[593.54 → 594.62] it's amazing to see
[594.62 → 595.76] like you can be
[595.76 → 596.58] running a satellite
[596.58 → 597.26] in space
[597.26 → 597.94] or you can be
[597.94 → 599.70] running pipelines
[599.70 → 601.80] and platform teams
[601.80 → 603.04] and it's so much
[603.04 → 603.78] that is different
[603.78 → 604.42] but so much
[604.42 → 605.12] of it is the same.
[605.26 → 605.86] So much of the
[605.86 → 606.46] new technology
[606.46 → 607.22] that we've built
[607.22 → 608.32] to make infrastructure
[608.32 → 609.72] easier is also
[609.72 → 610.84] just reminiscent
[610.84 → 612.66] of like the past,
[612.82 → 613.04] you know,
[613.10 → 614.22] and it just makes it,
[614.98 → 615.22] I don't know,
[615.30 → 616.44] it's like all the
[616.44 → 616.98] different ways
[616.98 → 617.66] that you can solve
[617.66 → 618.90] this awesome big puzzle
[618.90 → 619.60] in it.
[619.98 → 621.74] I sometimes think
[621.74 → 622.76] tech gets really weird,
[622.98 → 623.28] you know,
[623.34 → 624.44] and this podcast
[624.44 → 625.34] has made me
[625.34 → 626.80] remember why
[626.80 → 627.92] I love what we do
[627.92 → 630.24] and kept me loving it
[630.24 → 632.08] even in like the last year,
[632.32 → 632.64] you know?
[633.30 → 633.98] I think like for me
[633.98 → 634.36] some of the
[634.82 → 635.52] my favourite episodes
[635.52 → 636.36] were the throwbacks,
[636.48 → 636.62] right?
[636.64 → 637.46] Like talking to Rich
[637.46 → 637.96] and Mandy
[637.96 → 638.72] and people that were like,
[638.98 → 640.08] this is what it was like
[640.08 → 641.52] to run the AOL chat rooms.
[641.60 → 641.76] I'm like,
[641.78 → 642.34] that was awesome,
[642.40 → 642.56] right?
[642.58 → 643.20] It was just like,
[643.50 → 644.54] it was basically
[644.54 → 645.08] the same thing
[645.08 → 645.60] we're doing now
[645.60 → 646.64] just with tools
[646.64 → 647.04] that everyone's like,
[647.08 → 647.16] oh,
[647.18 → 647.68] you shouldn't use
[647.68 → 648.00] those anymore.
[648.02 → 648.20] I'm like,
[648.24 → 649.32] that ran the internet
[649.32 → 650.28] for years and years
[650.28 → 650.62] and years.
[650.62 → 651.66] Like we can't just
[651.66 → 652.66] throw out all the old
[652.66 → 653.40] stuff that was,
[653.40 → 654.54] was super functional
[654.54 → 656.04] because we don't like
[656.04 → 656.52] it anymore.
[656.86 → 657.54] And so those were
[657.54 → 658.28] really cool to me.
[659.00 → 659.04] Also,
[660.24 → 661.04] it's wild.
[661.22 → 662.54] Like the amount
[662.54 → 663.44] of people like
[663.44 → 664.38] that we've met
[664.38 → 665.06] and they were just like,
[665.10 → 665.64] we were doing
[665.64 → 666.68] this cool thing
[666.68 → 667.42] and I found it
[667.42 → 668.34] and I start doing it
[668.34 → 668.88] and then it leads
[668.88 → 669.64] to this job
[669.64 → 670.76] and this whole career.
[670.90 → 672.20] Like learning
[672.20 → 673.46] how you run Linux
[673.46 → 674.32] and different things
[674.32 → 674.86] in space
[674.86 → 675.98] is just wild to me
[675.98 → 676.54] and how you have
[676.54 → 677.14] to make sure
[677.14 → 679.16] that it can be updated
[679.16 → 680.64] and just all the
[680.64 → 682.00] thought that goes into it.
[682.14 → 683.28] But the people
[683.28 → 684.76] that we've met
[684.76 → 685.86] are almost cooler
[685.86 → 686.78] than the technology.
[687.60 → 687.78] Absolutely.
[688.22 → 688.40] I mean,
[688.42 → 688.56] yeah,
[688.60 → 690.18] the people in their journey
[690.18 → 690.68] into it
[690.68 → 691.84] have been really fun
[691.84 → 692.18] to learn from.
[692.24 → 693.02] In almost every case,
[693.06 → 693.90] it was like someone just,
[694.06 → 694.20] well,
[694.20 → 694.80] I just stepped up
[694.80 → 695.54] and learned a thing.
[695.66 → 696.40] That's what I'm saying.
[696.54 → 698.30] But how many jobs
[698.30 → 699.04] can you make
[699.04 → 700.80] this type of impact
[700.80 → 701.50] on the world,
[701.96 → 702.96] this type of money
[702.96 → 704.28] and this type of
[704.28 → 705.30] community
[705.30 → 706.78] and just because
[706.78 → 707.66] you thought something
[707.66 → 708.12] was cool
[708.12 → 708.78] and you needed out
[708.78 → 709.12] about it,
[709.20 → 711.16] that is the essence
[711.16 → 711.88] of what makes
[711.88 → 713.38] us still want to do this
[713.38 → 714.20] at the end of the day.
[714.52 → 714.66] You know?
[715.16 → 715.46] Yeah.
[715.46 → 716.80] I think my favourite
[716.80 → 718.00] ideas start with
[718.00 → 719.14] this can't be done.
[719.64 → 719.84] Yeah.
[720.24 → 721.10] This is too crazy.
[721.36 → 722.08] This is like no way.
[722.12 → 723.24] This is never going to work.
[723.94 → 725.24] And going through the cycles
[725.24 → 727.20] to either realize,
[727.44 → 727.68] indeed,
[727.80 → 728.64] this will never work
[728.64 → 729.66] the way I thought it would.
[730.42 → 731.70] But the learnings
[731.70 → 732.98] and the relationships
[732.98 → 733.56] that you make
[733.56 → 734.10] along the way,
[734.30 → 735.14] those are the ones
[735.14 → 735.98] that will take you
[735.98 → 737.22] wherever you're going next.
[737.90 → 738.22] So,
[738.94 → 739.48] it's all
[739.48 → 740.46] little steps,
[740.68 → 741.26] some is steps,
[741.26 → 742.52] and usually the missteps
[742.52 → 743.00] are the ones
[743.00 → 743.74] that teach you the most.
[744.12 → 744.86] That would be one
[744.86 → 746.96] of my takeaways,
[747.44 → 747.74] I think,
[747.88 → 749.10] from Ship It
[749.10 → 750.34] and from all the work
[750.34 → 750.94] that you do
[750.94 → 752.18] in this industry.
[752.78 → 753.82] Learning from mistakes.
[754.36 → 755.14] So powerful.
[755.68 → 756.42] So true.
[756.56 → 757.44] Because I think it's,
[757.70 → 757.84] like,
[757.88 → 758.74] I used to be, like,
[758.76 → 760.16] really scared of making mistakes
[760.16 → 761.02] and wanted it to be, like,
[761.08 → 761.94] perfect at everything,
[762.06 → 762.80] which was my toxic
[762.80 → 763.60] engineer trait.
[764.40 → 765.08] And, like,
[765.16 → 766.30] I think at, like,
[766.34 → 767.00] a certain point
[767.00 → 767.68] when you've done
[767.68 → 768.48] so much stuff
[768.48 → 769.18] in, like, production
[769.18 → 770.06] and just, like,
[770.12 → 771.14] worked in this industry
[771.14 → 771.80] for so long,
[771.88 → 772.60] like, you're no longer
[772.60 → 773.40] scared of, like,
[773.90 → 774.58] making mistakes.
[774.58 → 775.38] Like, you just kind of
[775.38 → 776.30] almost have to, like,
[776.82 → 778.94] get joy in the ambiguity,
[779.28 → 779.58] you know,
[779.64 → 781.24] and the doing hard things
[781.24 → 781.92] because you have
[781.92 → 782.66] no other choice.
[782.96 → 783.48] Well, you have to be
[783.48 → 784.04] given the freedom
[784.04 → 784.62] to do that, right?
[784.66 → 785.76] Like, the number one
[785.76 → 786.52] contributing factor
[786.52 → 788.24] to, like,
[788.32 → 789.26] good performance teams
[789.26 → 790.46] is psychological safety.
[790.94 → 791.04] Right?
[791.06 → 791.96] Like, being able to say,
[792.04 → 793.30] like, I don't know
[793.30 → 794.60] or I made a mistake
[794.60 → 795.12] and everyone's like,
[795.44 → 795.70] great,
[795.84 → 796.88] what do we learn from that?
[796.94 → 797.76] Where are we going forward?
[798.20 → 799.18] And that's okay
[799.18 → 800.68] to be able, you know,
[800.68 → 801.60] to have that freedom
[801.60 → 802.48] to make the mistakes
[802.48 → 804.46] and there's a lot of privilege
[804.46 → 806.04] in that for some of us.
[806.04 → 806.62] I guess, like,
[806.64 → 807.60] a white dude in tech.
[807.76 → 808.24] Like, I've been given
[808.24 → 809.00] the benefit of the doubt
[809.00 → 810.30] more than I should have been
[810.30 → 811.32] throughout my career
[811.32 → 812.08] to be able to say,
[812.16 → 813.04] actually, I don't know that
[813.04 → 813.80] or I messed up.
[813.92 → 815.50] Sorry, I'll fix it next time,
[815.62 → 816.56] which I know a lot of people
[816.56 → 817.08] don't give that,
[817.14 → 818.34] but also a lot of companies
[818.34 → 819.02] don't give that
[819.02 → 819.76] because they're just like,
[820.14 → 821.42] we hire senior people
[821.42 → 822.52] and senior people
[822.52 → 823.42] know what they're doing, right?
[823.46 → 823.90] Like, no.
[824.12 → 824.72] Like, senior people
[824.72 → 825.88] don't know what they're doing either.
[826.22 → 826.92] They've just taken down
[826.92 → 828.14] production before, right?
[828.14 → 830.12] It's just like the only real difference
[830.12 → 831.08] of, like, the junior people
[831.08 → 831.86] are, like, terrified
[831.86 → 832.66] to take down production
[832.66 → 833.72] and the senior people
[833.72 → 834.02] are like,
[834.08 → 834.90] oh, no, this is going to be all right.
[835.06 → 835.96] But that's why I think
[835.96 → 837.36] this podcast is important
[837.36 → 839.82] and that's why I'm proud
[839.82 → 841.28] of the last 50 episodes
[841.28 → 841.82] that we did
[841.82 → 843.70] because I feel like
[843.70 → 844.82] there are a lot of podcasts
[844.82 → 845.38] that are, like,
[845.42 → 846.42] big on, like, tech
[846.42 → 846.76] and, like,
[846.78 → 848.26] they're very technically deep depth,
[848.38 → 848.94] but, like,
[849.66 → 850.80] I appreciate the way
[850.80 → 851.52] that we talk about
[851.52 → 852.30] making mistakes
[852.30 → 853.48] and the way that we talk about,
[853.48 → 854.68] like, the people aspect
[854.68 → 855.88] and how you have to have
[855.88 → 856.66] that safe environment
[856.66 → 858.42] and we can talk about diversity
[858.42 → 859.76] and all these different things
[859.76 → 861.14] because, like,
[861.20 → 862.42] I think people really think
[862.42 → 862.92] that, like,
[863.06 → 864.74] diversity or safe places
[864.74 → 865.20] or, like,
[865.22 → 865.94] all these things
[865.94 → 866.44] are, like,
[866.52 → 867.58] an added bonus
[867.58 → 868.50] to technology,
[868.50 → 870.22] but you can't make good tech
[870.22 → 871.50] without thinking
[871.50 → 872.22] about the people,
[872.32 → 873.26] without thinking about
[873.26 → 874.66] how to make a better environment.
[874.66 → 875.30] So, like,
[875.96 → 876.92] whatever we can do
[876.92 → 878.22] to use whatever privilege
[878.22 → 878.80] we have
[878.80 → 879.82] to influence
[879.82 → 881.10] and to make things better
[881.10 → 881.84] and to, like,
[881.88 → 883.00] help people know
[883.00 → 883.40] that, like,
[883.58 → 884.34] they can get started
[884.34 → 885.28] and also just to talk
[885.28 → 886.00] to people that are
[886.00 → 887.86] perfect technically
[887.86 → 889.04] but are come from
[889.04 → 890.08] all these different backgrounds.
[890.20 → 891.00] Like, look at all the people
[891.00 → 891.96] that we've had on the show,
[892.22 → 892.52] you know?
[892.76 → 892.96] Like,
[893.38 → 894.40] so I just think it's cool
[894.40 → 895.46] to be able to use
[895.46 → 896.86] the privilege that we have
[896.86 → 899.06] to try to make it better
[899.06 → 900.08] and make other people,
[900.08 → 900.36] like,
[900.46 → 900.72] seen
[900.72 → 901.84] and to also, like,
[901.92 → 902.62] show that, like,
[902.82 → 903.58] you can be different
[903.58 → 905.12] and still very technically deep,
[905.36 → 905.66] you know?
[906.14 → 906.96] Well, I guess we'll just
[906.96 → 907.88] transition right into,
[908.12 → 908.32] Gerhard,
[908.36 → 909.10] what have you been doing
[909.10 → 911.28] since your kind of left Ship It,
[911.38 → 912.54] since you left Changelog,
[912.54 → 913.66] what have you been working on?
[913.76 → 914.98] What software
[914.98 → 916.10] have you been responsible for?
[916.86 → 917.26] So,
[917.42 → 918.86] it feels like
[918.86 → 920.26] I never really left Changelog
[920.26 → 921.04] because,
[921.20 → 921.94] first,
[921.98 → 922.96] the Kaiden episodes
[922.96 → 924.72] and of all the
[924.72 → 925.84] infrastructure improvements
[925.84 → 927.02] that we are still driving
[927.02 → 928.50] and they're still
[928.50 → 929.38] very much present.
[930.08 → 931.20] Trying all the things
[931.20 → 931.70] that we did
[931.70 → 932.74] over the years
[932.74 → 933.92] and taking it
[933.92 → 935.00] to a place where it is now
[935.00 → 935.92] and continuing the journey,
[936.04 → 936.78] that has been
[936.78 → 938.88] a long-term,
[939.40 → 940.58] very satisfying journey.
[940.98 → 941.52] That's the way
[941.52 → 942.08] I would put it.
[942.50 → 943.16] And I'm very happy
[943.16 → 944.06] that that is continuing
[944.06 → 945.44] and we figured out
[945.44 → 947.08] a way to make that work
[947.08 → 948.02] with Adam and Gerard.
[948.26 → 948.28] So,
[948.88 → 949.80] that is
[949.80 → 952.22] personally a very satisfying thing
[952.22 → 953.04] and also professionally
[953.04 → 954.10] a very satisfying thing.
[954.76 → 955.56] After Ship It,
[956.06 → 957.08] and the reason why
[957.08 → 957.42] for me,
[957.52 → 958.30] even like back then
[958.30 → 958.96] when I was
[958.96 → 959.88] the last episode,
[960.02 → 960.30] 19,
[960.42 → 961.16] Bracing Change,
[961.76 → 962.88] it was a
[962.88 → 963.52] priorities,
[964.52 → 965.56] like,
[965.68 → 966.52] I had to reshuffle
[966.52 → 967.28] a bunch of priorities,
[967.40 → 967.70] basically,
[967.70 → 968.46] and I had to give
[968.46 → 969.28] more time
[969.28 → 970.72] to my main job,
[970.96 → 971.62] which at the time
[971.62 → 972.14] was Dagger,
[972.48 → 972.84] a Dagger,
[972.96 → 973.96] and it still is a Dagger
[973.96 → 974.82] even to this day.
[975.82 → 977.66] And I think that was
[977.66 → 978.64] one of the big changes
[978.64 → 979.38] that happened
[979.38 → 981.10] between me starting Ship It
[981.10 → 981.42] and then,
[981.44 → 981.60] you know,
[981.64 → 982.38] having to
[982.38 → 984.06] part ways
[984.06 → 985.50] at that point.
[986.68 → 987.12] 2021
[987.12 → 988.78] was a very interesting year
[988.78 → 989.62] and it was not
[989.62 → 990.22] because of COVID,
[990.56 → 991.26] but that obviously,
[991.36 → 991.84] that did,
[991.96 → 992.72] that did make it
[992.72 → 993.84] interesting for everybody.
[994.32 → 995.16] But for me personally,
[995.16 → 996.08] I was transitioning
[996.08 → 998.00] into a startup again.
[998.38 → 998.82] I went from
[998.82 → 999.72] a large enterprise
[999.72 → 1000.62] at the time
[1000.62 → 1001.30] that was VMware
[1001.30 → 1003.16] and at VMware
[1003.16 → 1004.14] I have been working
[1004.14 → 1005.26] on RabbitMQ
[1005.26 → 1006.42] for,
[1006.62 → 1006.84] I think,
[1006.94 → 1007.90] six or seven years
[1007.90 → 1008.76] and I went through
[1008.76 → 1009.58] like different
[1009.58 → 1011.00] types of teams
[1011.00 → 1011.80] until eventually
[1011.80 → 1012.54] end up on the
[1012.54 → 1014.06] core RabbitMQ team.
[1014.42 → 1015.22] So you get all
[1015.22 → 1015.94] the Erlang,
[1016.56 → 1017.62] you get all the Make
[1017.62 → 1018.90] and there's a story
[1018.90 → 1019.64] there because it
[1019.64 → 1020.58] connects to Dagger
[1020.58 → 1022.32] and you just get
[1022.32 → 1023.70] to see a lot of
[1023.84 → 1025.10] really important systems,
[1025.76 → 1026.98] distributed systems,
[1027.14 → 1028.30] distributed systems problems
[1028.30 → 1029.92] and you realize
[1029.92 → 1030.60] how important
[1030.60 → 1031.48] the kernel is
[1031.48 → 1032.52] even when you're
[1032.52 → 1033.52] not using containers.
[1034.14 → 1035.10] So little differences
[1035.10 → 1036.38] between the different kernels
[1036.38 → 1037.56] can have a huge impact
[1037.56 → 1038.66] on how something
[1038.66 → 1039.48] like the Erlang VM
[1039.48 → 1040.00] behaves
[1040.00 → 1041.06] and these are
[1041.06 → 1041.68] really important
[1041.68 → 1042.22] applications
[1042.22 → 1043.34] like think for banks,
[1043.50 → 1044.54] financial institutions,
[1045.32 → 1046.50] GPS trackers
[1046.50 → 1048.50] and you may be thinking
[1048.50 → 1049.20] food deliveries
[1049.20 → 1049.98] but there's also
[1049.98 → 1051.22] some other GPS trackers
[1051.22 → 1052.08] which are really important
[1052.08 → 1053.32] they work correctly.
[1053.84 → 1054.60] Tills,
[1054.92 → 1055.94] payment systems,
[1056.10 → 1057.16] it's all over the place.
[1057.66 → 1058.36] At some point,
[1058.46 → 1059.58] we didn't realize this,
[1060.22 → 1061.22] some cars,
[1061.62 → 1062.60] the doors wouldn't open
[1062.60 → 1064.00] and RabbitMQ
[1064.00 → 1064.90] was in that stack.
[1065.30 → 1065.98] Like I was not
[1065.98 → 1066.76] expecting that.
[1067.00 → 1067.36] Like you know,
[1067.72 → 1068.40] you would honestly
[1068.40 → 1069.24] not expect that.
[1069.40 → 1069.84] It is wild
[1069.84 → 1070.46] like to see
[1070.46 → 1071.56] where tech ends up
[1071.56 → 1072.24] and how it ends up
[1072.24 → 1072.74] being used.
[1073.30 → 1074.14] A lot of the time
[1074.14 → 1074.98] it gets used wrong
[1074.98 → 1076.10] so having those
[1076.10 → 1076.64] conversations
[1076.64 → 1077.46] and going through
[1077.46 → 1078.00] those cycles
[1078.00 → 1078.58] when you have
[1078.58 → 1079.34] big teams
[1079.34 → 1080.62] and big budgets
[1080.62 → 1081.46] and big enterprises
[1081.46 → 1082.04] is fun
[1082.04 → 1083.08] but also
[1083.08 → 1084.12] it's a certain
[1084.12 → 1084.78] type of game.
[1085.38 → 1085.92] So after playing
[1085.92 → 1086.34] that game
[1086.34 → 1087.10] for like six,
[1087.24 → 1087.76] seven years
[1087.76 → 1088.84] something like that
[1088.84 → 1089.82] I said,
[1089.94 → 1090.26] you know what,
[1090.28 → 1091.02] it's time to go back
[1091.02 → 1091.94] to the startup world
[1091.94 → 1093.44] because I did start
[1093.44 → 1094.22] like on that journey
[1094.22 → 1095.52] before getting to VMware.
[1095.98 → 1096.88] We were a small startup.
[1097.16 → 1098.10] We were Cloud Credo.
[1098.44 → 1099.66] We were consultants
[1099.66 → 1101.34] for Cloud Foundry
[1101.34 → 1102.04] at the time
[1102.04 → 1102.62] and Bosch
[1102.62 → 1103.76] for those that
[1103.76 → 1105.42] remember Bosch
[1105.42 → 1106.56] maybe a few listeners
[1106.56 → 1106.92] will
[1106.92 → 1109.62] and Chef
[1109.62 → 1110.22] wasn't working
[1110.22 → 1111.16] for those systems
[1111.16 → 1112.32] so a team
[1112.32 → 1113.52] of 20 something people
[1113.52 → 1114.40] then we became
[1114.40 → 1114.82] Pivotal
[1114.82 → 1116.02] as in we were
[1116.02 → 1117.00] acquired by Pivotal
[1117.00 → 1117.82] but in my mind
[1117.82 → 1118.90] we took over Pivotal
[1118.90 → 1119.46] in some way
[1119.46 → 1120.88] because of that
[1120.88 → 1121.72] craziness
[1121.72 → 1122.50] the crazy spirit
[1122.50 → 1123.08] that we had
[1123.08 → 1124.04] and that worked
[1124.04 → 1124.48] really well
[1124.48 → 1125.42] so being part of
[1125.42 → 1126.20] Pivotal was great
[1126.20 → 1127.16] and pair programming
[1127.16 → 1128.14] and extreme programming
[1128.14 → 1129.46] that was at the core
[1129.46 → 1129.76] of it
[1129.76 → 1130.88] and then Pivotal
[1130.88 → 1131.72] eventually got acquired
[1131.72 → 1132.22] by VMware
[1132.22 → 1133.12] so those transitions
[1133.12 → 1134.68] from 20 to 2000
[1134.68 → 1135.78] to 40,000
[1135.78 → 1136.70] were huge jumps
[1136.70 → 1138.40] and huge changes
[1138.40 → 1140.02] so I wrote all of that
[1140.02 → 1140.36] and I said
[1140.36 → 1140.72] you know what
[1140.72 → 1141.54] it's time to go back
[1141.54 → 1142.34] to the startup world
[1142.34 → 1143.48] and that's where
[1143.48 → 1144.18] Dagger enters
[1144.18 → 1145.98] so Dagger was interesting
[1145.98 → 1147.26] because I was fascinated
[1147.26 → 1147.82] by Docker
[1147.82 → 1149.50] and I was working
[1149.50 → 1150.42] with Docker
[1150.42 → 1151.20] and using Docker
[1151.20 → 1152.58] but I haven't helped
[1152.58 → 1153.60] build Docker
[1153.60 → 1154.70] so Dagger
[1154.70 → 1155.66] was at the moment
[1155.66 → 1156.88] where I could try that
[1156.88 → 1158.20] and I took it
[1158.20 → 1159.70] and three years later
[1159.70 → 1160.48] here I am
[1160.48 → 1161.30] for anyone
[1161.30 → 1161.80] that doesn't know
[1161.80 → 1162.42] what Dagger is
[1162.42 → 1162.86] describe
[1162.86 → 1164.16] like what
[1164.16 → 1164.92] what are you doing
[1164.92 → 1165.54] or what does Dagger
[1165.54 → 1166.06] actually make
[1166.06 → 1166.52] as a product
[1166.52 → 1167.00] as a startup
[1167.00 → 1167.40] that's like
[1167.40 → 1168.26] hey we're going
[1168.26 → 1168.96] to change the world
[1168.96 → 1169.78] for this thing
[1169.78 → 1170.36] what is that
[1170.36 → 1171.96] so Dagger
[1171.96 → 1174.28] is what happens
[1174.28 → 1175.16] when you get tired
[1175.16 → 1175.88] of all the YAML
[1175.88 → 1177.34] when you get tired
[1177.34 → 1177.96] of all the YAML
[1177.96 → 1178.84] in your pipelines
[1178.84 → 1181.04] especially your CCD pipelines
[1181.04 → 1182.28] or when you get tired
[1182.28 → 1183.34] of your Jenkins file
[1183.34 → 1184.76] or when you get tired
[1184.76 → 1185.50] of your scripts
[1185.50 → 1187.36] you want something
[1187.36 → 1189.34] that scales
[1189.34 → 1190.52] with teams
[1190.52 → 1191.70] and with ideas
[1191.70 → 1192.76] that can
[1192.76 → 1194.14] it's really hard
[1194.14 → 1194.66] to capture them
[1194.66 → 1195.04] in YAML
[1195.04 → 1196.78] if you are finding
[1196.78 → 1197.48] yourself starting
[1197.48 → 1198.60] to template YAML
[1198.60 → 1200.16] for GitHub Actions
[1200.16 → 1201.02] or CircleCI
[1201.02 → 1202.56] or any CCD system
[1202.56 → 1204.20] you know you need Dagger
[1204.20 → 1205.64] the other option
[1205.64 → 1206.70] is to go towards
[1206.70 → 1207.22] Basel
[1207.22 → 1208.06] and to go into
[1208.06 → 1208.62] that world
[1208.62 → 1209.64] but for anyone
[1209.64 → 1210.40] that knows
[1210.40 → 1210.86] that world
[1210.86 → 1211.32] and experiences
[1211.32 → 1211.84] that world
[1211.84 → 1212.52] knows that is
[1212.52 → 1213.52] a very heavyweight
[1213.52 → 1214.92] enterprise world
[1214.92 → 1217.20] so Dagger
[1217.20 → 1218.84] takes all the scripts
[1218.84 → 1220.06] and all the YAML
[1220.06 → 1221.76] and it allows you
[1221.76 → 1222.98] to capture that in code
[1222.98 → 1224.56] so what that means
[1224.56 → 1225.36] is that imagine
[1225.36 → 1226.76] writing your automation
[1226.76 → 1228.92] it can be a make file
[1228.92 → 1230.36] it can be your
[1230.36 → 1231.28] GitHub Actions YAML
[1231.28 → 1232.40] it can be your
[1232.40 → 1233.24] CircleCI config
[1233.24 → 1234.20] your Jenkins file
[1234.20 → 1235.12] all those things
[1235.12 → 1235.68] you can take
[1235.68 → 1237.44] and you can put them
[1237.44 → 1238.10] in the code
[1238.10 → 1239.84] that you are familiar with
[1239.84 → 1241.22] whether it's Python
[1241.22 → 1242.38] whether it's Go
[1242.38 → 1243.48] whether it's TypeScript
[1243.48 → 1245.92] and some more
[1245.92 → 1247.16] legacy languages
[1247.16 → 1247.96] which are still
[1247.96 → 1248.64] very much present
[1248.64 → 1249.34] like PHP
[1249.34 → 1251.04] or Elixir for example
[1251.04 → 1251.72] Rust
[1251.72 → 1252.42] some newer ones
[1252.42 → 1253.78] any of these languages
[1253.78 → 1254.50] you can use
[1254.50 → 1256.20] to write your automation
[1256.20 → 1258.24] and you can package it
[1258.24 → 1259.36] in something called modules
[1259.36 → 1260.72] you can distribute
[1260.72 → 1261.54] these modules
[1261.54 → 1262.20] as you would
[1262.20 → 1262.90] any package
[1262.90 → 1264.76] and you can assemble them
[1264.76 → 1266.02] just in time
[1266.02 → 1267.20] and you can combine them
[1267.20 → 1268.00] with other modules
[1268.00 → 1269.54] so what that means
[1269.54 → 1270.40] is that now
[1270.40 → 1271.86] you writing automation
[1271.86 → 1273.16] you integrating with CI CD
[1273.16 → 1274.52] is just a matter of
[1274.52 → 1276.10] calling the right function
[1276.10 → 1277.06] from the right module
[1277.06 → 1278.44] and making sure
[1278.44 → 1279.18] that that function
[1279.18 → 1280.38] gets wired
[1280.38 → 1281.22] with everything else
[1281.22 → 1282.10] that it needs
[1282.10 → 1284.38] so for example
[1284.38 → 1285.70] you have your tests
[1285.70 → 1285.98] right
[1285.98 → 1286.72] and build
[1286.72 → 1287.16] and you say
[1287.16 → 1287.68] okay but
[1287.68 → 1288.94] you could do this
[1288.94 → 1289.62] with make files
[1289.62 → 1290.74] or you could use
[1290.74 → 1291.72] a just file
[1291.72 → 1292.46] or you could use
[1292.46 → 1293.42] anything like that
[1293.42 → 1294.48] and that is true
[1294.48 → 1295.46] you can
[1295.46 → 1297.04] but what ends up
[1297.04 → 1297.74] happening with that
[1297.74 → 1298.52] is that
[1298.52 → 1299.94] there will be
[1299.94 → 1300.68] assumptions
[1300.68 → 1302.24] about the context
[1302.24 → 1303.82] in which that automation
[1303.82 → 1304.26] runs
[1304.26 → 1305.58] Dagger
[1305.58 → 1306.80] the only assumption
[1306.80 → 1307.38] which it makes
[1307.38 → 1307.96] is that there will be
[1307.96 → 1308.40] an engine
[1308.40 → 1309.40] which is a container
[1309.40 → 1309.80] runtime
[1309.80 → 1311.76] and in that container
[1311.76 → 1312.08] runtime
[1312.08 → 1313.22] you always have to specify
[1313.22 → 1314.18] hey which container
[1314.18 → 1315.22] image do you want to run
[1315.22 → 1316.42] which one do you want
[1316.42 → 1317.14] to start with
[1317.14 → 1319.04] so all these functions
[1319.04 → 1320.34] they always have a context
[1320.34 → 1321.90] and the context
[1321.90 → 1322.66] is the same
[1322.66 → 1323.84] regardless where you run
[1323.84 → 1325.38] which means
[1325.38 → 1326.12] that if you want
[1326.12 → 1326.98] to run this locally
[1326.98 → 1327.94] it will run
[1327.94 → 1329.08] exactly the same
[1329.08 → 1330.02] as it runs
[1330.02 → 1331.26] on any CI platform
[1331.26 → 1332.48] anywhere in the world
[1332.48 → 1334.28] you can run Dagger
[1334.28 → 1334.68] in Jenkins
[1334.68 → 1335.26] if you want
[1335.26 → 1336.44] it is an option
[1336.44 → 1337.64] I've been doing
[1337.64 → 1338.50] containers and make files
[1338.50 → 1339.40] for a long time
[1339.40 → 1339.96] right like that
[1339.96 → 1340.82] that assumption
[1340.82 → 1341.78] that I can
[1341.78 → 1343.18] I can run make
[1343.18 → 1344.48] in Jenkins
[1344.48 → 1345.66] or my local machine
[1345.66 → 1346.44] and it runs the same
[1346.44 → 1347.18] I don't need Dagger
[1347.18 → 1347.82] for that right
[1347.82 → 1348.68] correct
[1348.68 → 1349.82] it's like I can do
[1349.82 → 1350.84] I've been doing it
[1350.84 → 1351.06] right like
[1351.06 → 1351.98] all of
[1351.98 → 1352.96] yeah a lot of stuff
[1352.96 → 1353.42] just works like
[1353.42 → 1354.12] oh just execute
[1354.12 → 1354.62] the container
[1354.62 → 1355.52] here are some arguments
[1355.52 → 1356.06] for it like
[1356.06 → 1356.90] you know variables
[1356.90 → 1357.56] to the make file
[1357.56 → 1358.00] that's fine
[1358.00 → 1358.76] so that side of it
[1358.76 → 1359.58] doesn't really
[1359.58 → 1361.18] change how I've
[1361.18 → 1361.66] been doing things
[1361.66 → 1362.02] at least I know
[1362.02 → 1362.40] it does change
[1362.40 → 1362.92] how a lot of people
[1362.92 → 1363.24] are doing it
[1363.24 → 1364.56] because bash is prevalent
[1364.56 → 1366.00] the second thing here
[1366.00 → 1366.38] though I think
[1366.38 → 1367.22] that is interesting
[1367.22 → 1368.72] to me Dagger
[1368.72 → 1369.58] has always
[1369.58 → 1371.14] been almost
[1371.14 → 1372.64] the dagger
[1372.64 → 1373.32] if you will
[1373.32 → 1374.84] the blade
[1374.84 → 1375.44] for like
[1375.44 → 1376.22] the DevOps team
[1376.22 → 1377.74] the fact that
[1377.74 → 1378.46] how DevOps
[1378.46 → 1379.50] used to work
[1379.50 → 1379.88] for me
[1379.88 → 1380.74] at large enterprises
[1380.74 → 1381.78] was
[1381.78 → 1383.40] application teams
[1383.40 → 1383.76] would go write
[1383.76 → 1384.38] a bunch of code
[1384.38 → 1385.18] and the DevOps team
[1385.18 → 1385.48] would come in
[1385.48 → 1386.04] and like drop
[1386.04 → 1387.20] a Jenkins file
[1387.20 → 1387.64] in right
[1387.64 → 1388.28] here's your PR
[1388.28 → 1389.20] for your Jenkins file
[1389.20 → 1390.54] now this is all
[1390.54 → 1390.88] going to work
[1390.88 → 1391.26] magically
[1392.02 → 1392.46] team
[1392.46 → 1393.46] at Disney Plus
[1393.46 → 1393.84] that was like
[1393.84 → 1395.02] a Lib Jenkins team
[1395.02 → 1395.74] like we wrote
[1395.74 → 1396.32] libraries
[1396.32 → 1397.28] I didn't do it
[1397.28 → 1397.96] I hate Jenkins file
[1397.96 → 1398.66] but they wrote
[1398.66 → 1399.36] they wrote libraries
[1399.36 → 1401.80] for this groovy script
[1401.80 → 1402.60] so that everyone
[1402.60 → 1403.34] in their Jenkins file
[1403.34 → 1404.02] would import
[1404.02 → 1405.52] that team's Lib Jenkins
[1405.52 → 1406.40] and then it would do
[1406.40 → 1406.88] a bunch of stuff
[1406.88 → 1407.24] for them
[1407.24 → 1407.88] by default
[1407.88 → 1409.22] but that's so required
[1409.22 → 1410.20] there was some
[1410.20 → 1410.98] other team
[1410.98 → 1412.16] doing some other
[1412.16 → 1412.62] thing
[1412.62 → 1414.02] in some other language
[1414.02 → 1415.10] that was external
[1415.10 → 1416.12] to the application team
[1416.12 → 1417.90] and my sense
[1417.90 → 1418.34] with Dagger
[1418.34 → 1419.18] is the fact that
[1419.18 → 1420.36] Dagger requires
[1420.36 → 1421.38] that the application team
[1421.38 → 1423.12] now owns CCD
[1423.12 → 1424.70] as like they are the ones
[1424.70 → 1425.46] because like the
[1425.46 → 1426.84] familiarity of code
[1426.84 → 1428.12] doesn't matter
[1428.12 → 1429.04] if you're not the one
[1429.04 → 1429.80] writing the code
[1429.80 → 1430.28] right like if you're
[1430.28 → 1431.16] some external person
[1431.16 → 1431.58] you're going to have
[1431.58 → 1432.14] your own
[1432.14 → 1433.64] pep formatting
[1433.64 → 1434.26] for Python
[1434.26 → 1435.06] and your own
[1435.06 → 1435.76] you know modules
[1435.76 → 1436.28] and formatting
[1436.28 → 1436.76] so that's like
[1436.76 → 1437.30] it's not going to
[1437.30 → 1437.86] jive well
[1437.86 → 1438.76] with the application team
[1438.76 → 1439.42] so in this case
[1439.42 → 1441.74] Dagger makes the most sense
[1441.74 → 1442.56] when the team
[1442.56 → 1443.36] writing the code
[1443.36 → 1444.98] is also the one
[1444.98 → 1446.02] doing the CCD
[1446.02 → 1446.54] is that right?
[1446.54 → 1447.36] yes
[1447.36 → 1448.78] that is a valid take
[1448.78 → 1449.48] for sure
[1449.48 → 1450.98] we see
[1450.98 → 1452.50] different teams
[1452.50 → 1454.26] and different companies
[1454.26 → 1454.82] use Dagger
[1454.82 → 1455.56] in different ways
[1455.56 → 1457.04] at this point
[1457.04 → 1457.42] we've seen
[1457.42 → 1458.32] every which way
[1458.32 → 1459.54] and they're all valid
[1459.54 → 1460.84] the point is
[1460.84 → 1461.60] that it forces
[1461.60 → 1463.48] the different perspectives
[1463.48 → 1464.88] to come together
[1464.88 → 1465.78] as code
[1465.78 → 1467.26] so forget like
[1467.26 → 1467.94] a make file
[1467.94 → 1469.06] or Jenkins file
[1469.06 → 1469.76] or a script
[1469.76 → 1470.28] or anything
[1470.28 → 1470.58] just
[1470.58 → 1471.44] we will be writing
[1471.44 → 1472.02] the code
[1472.02 → 1473.30] that our company
[1473.30 → 1474.72] is most familiar with
[1474.72 → 1476.52] whether you're a DevOps person
[1476.52 → 1478.34] whether you're someone
[1478.34 → 1478.92] in the community
[1478.92 → 1479.76] that wrote a module
[1479.76 → 1480.64] it doesn't really matter
[1480.64 → 1481.68] the point is
[1481.68 → 1482.70] we will all be looking
[1482.70 → 1483.42] at the same code
[1483.42 → 1485.04] we understand the same code
[1485.04 → 1486.70] we can contribute
[1486.70 → 1487.44] to the same code
[1487.44 → 1488.52] and all the automation
[1488.52 → 1489.82] ends up being code
[1489.82 → 1490.90] that we can run locally
[1490.90 → 1493.14] from wherever it is
[1493.14 → 1494.36] so just to give you
[1494.36 → 1494.80] an example
[1494.80 → 1496.30] of how powerful this is
[1496.30 → 1497.66] let's say that
[1497.66 → 1498.40] you will take
[1498.40 → 1499.60] the Dagger repository
[1499.60 → 1500.60] as is today
[1500.60 → 1502.26] the Dagger repository
[1502.26 → 1503.26] has a module
[1503.26 → 1504.58] for the entire repository
[1504.58 → 1507.08] which encapsulates
[1507.08 → 1507.92] all the things
[1507.92 → 1508.68] that can happen
[1508.68 → 1509.54] in that repository
[1509.54 → 1511.48] so without you knowing
[1511.48 → 1512.08] anything
[1512.08 → 1513.18] about
[1513.18 → 1514.32] how it runs
[1514.32 → 1515.08] or what's needed
[1515.08 → 1516.38] you can
[1516.38 → 1517.50] start discovering
[1517.50 → 1518.48] what is possible
[1518.48 → 1519.08] in this module
[1519.08 → 1520.18] for example
[1520.18 → 1521.52] build me the docs
[1521.52 → 1522.88] but also
[1522.88 → 1523.70] serve the docs
[1523.70 → 1524.58] you have one command
[1524.58 → 1525.44] that will build
[1525.44 → 1526.42] lint
[1526.42 → 1527.46] serve the docs
[1527.46 → 1528.74] on your local machine
[1528.74 → 1529.62] the Dagger docs
[1529.62 → 1530.46] without you knowing
[1530.46 → 1531.18] anything
[1531.18 → 1532.68] or having to install
[1532.68 → 1533.16] anything
[1533.16 → 1534.42] apart from the Dagger CLI
[1534.42 → 1536.10] in the same way
[1536.10 → 1537.26] you could build yourself
[1537.26 → 1538.12] a Dagger CLI
[1538.12 → 1539.02] if you wanted to
[1539.02 → 1539.94] once you discover
[1539.94 → 1540.90] what the command is
[1540.90 → 1542.42] and it's all self-documenting
[1542.42 → 1543.02] it's all there
[1543.02 → 1543.90] so it provides
[1543.90 → 1545.22] a very nice way
[1545.22 → 1546.20] of consuming things
[1546.20 → 1547.34] without you knowing
[1547.34 → 1548.02] much about
[1548.02 → 1549.04] what this piece
[1549.04 → 1549.86] of software is
[1549.86 → 1550.72] it's almost like
[1550.72 → 1551.86] an API to code
[1551.86 → 1553.50] but an API
[1553.50 → 1554.74] to consuming code
[1554.74 → 1555.84] to consuming resources
[1555.84 → 1557.02] I don't care
[1557.02 → 1557.62] whether it's Python
[1557.62 → 1558.36] whether it's PHP
[1558.36 → 1559.50] what I want
[1559.50 → 1560.22] is the artifact
[1560.22 → 1561.02] or what I want
[1561.02 → 1561.64] is the docs
[1561.64 → 1562.26] or what I want
[1562.26 → 1563.64] is the auto-completion
[1563.64 → 1564.64] whatever the case may be
[1564.64 → 1565.98] so how do you
[1565.98 → 1566.56] encapsulate that
[1566.56 → 1567.10] in a way
[1567.10 → 1568.70] that others can understand
[1568.70 → 1569.36] and consume it
[1569.36 → 1569.96] easily
[1569.96 → 1571.40] well, but there's
[1571.40 → 1572.50] a separation there
[1572.50 → 1572.92] of like
[1572.92 → 1574.36] understanding something
[1574.36 → 1575.20] and using something
[1575.20 → 1575.76] without needing
[1575.76 → 1576.46] to understand it
[1576.46 → 1576.58] right
[1576.58 → 1577.00] because again
[1577.00 → 1577.30] the
[1577.30 → 1578.64] I can
[1578.64 → 1579.64] I've written
[1579.64 → 1580.24] plenty of
[1580.24 → 1581.44] things that were
[1581.44 → 1581.72] just like
[1581.72 → 1582.14] you just run
[1582.14 → 1582.82] make docs
[1582.82 → 1583.66] and docs are there
[1583.66 → 1583.98] for you
[1583.98 → 1584.10] right
[1584.10 → 1584.84] like make docs
[1584.84 → 1585.22] dev
[1585.22 → 1585.64] and they're like
[1585.64 → 1585.96] it's like
[1585.96 → 1586.78] they don't need to know
[1586.78 → 1587.32] what's behind
[1587.32 → 1588.26] the make file
[1588.26 → 1588.98] and it's running
[1588.98 → 1589.56] containers still
[1589.56 → 1590.34] it's doing that stuff
[1590.34 → 1591.34] the thing that I think
[1591.34 → 1592.06] is fascinating
[1592.06 → 1592.96] here is the fact
[1592.96 → 1593.38] that like
[1593.38 → 1594.22] those modules
[1594.22 → 1594.98] are shareable
[1594.98 → 1596.14] and the modules
[1596.14 → 1598.10] are something
[1598.10 → 1598.80] really powerful
[1598.80 → 1599.60] that Terraform
[1599.60 → 1600.06] did for us
[1600.06 → 1600.16] right
[1600.16 → 1600.60] like Terraform
[1600.60 → 1601.20] modules were
[1601.20 → 1601.56] powerful
[1601.56 → 1602.06] because you're
[1602.06 → 1602.32] just like
[1602.32 → 1603.18] you don't have
[1603.18 → 1603.64] to know
[1603.64 → 1604.66] behind the scenes
[1604.66 → 1605.70] and granted
[1605.70 → 1606.24] at some point
[1606.24 → 1606.66] you might need
[1606.66 → 1607.60] to escape the module
[1607.60 → 1608.04] you might need
[1608.04 → 1608.84] to override the module
[1608.84 → 1609.18] you might need
[1609.18 → 1609.84] to go build
[1609.84 → 1610.50] your own module
[1610.50 → 1611.28] but you can get
[1611.28 → 1612.28] started with
[1612.28 → 1612.72] something that
[1612.72 → 1613.62] has some opinions
[1613.62 → 1616.06] on how we think
[1616.06 → 1616.46] you should be
[1616.46 → 1617.12] doing this
[1617.12 → 1618.40] and in the dagger
[1618.40 → 1618.78] sense
[1618.78 → 1619.82] and in the Terraform
[1619.82 → 1620.08] sense
[1620.08 → 1621.16] most of the time
[1621.16 → 1621.88] those things
[1621.88 → 1622.38] are just going
[1622.38 → 1623.12] to work for you
[1623.12 → 1623.82] without needing
[1623.82 → 1624.24] to care
[1624.24 → 1624.56] right
[1624.56 → 1625.02] so it's like
[1625.02 → 1625.38] I can
[1625.38 → 1626.44] dagger
[1626.44 → 1626.94] and it
[1626.94 → 1627.30] or whatever
[1627.30 → 1628.08] I can start
[1628.08 → 1628.66] off with the module
[1628.66 → 1629.02] like oh
[1629.02 → 1629.96] this is the thing
[1629.96 → 1630.40] I wanted
[1630.40 → 1631.38] this looks right
[1631.38 → 1632.20] I'm going to go
[1632.20 → 1633.42] with the defaults
[1633.42 → 1633.84] and if I need
[1633.84 → 1634.28] to change it
[1634.28 → 1634.86] I can
[1634.86 → 1636.42] so essentially
[1636.42 → 1637.28] can you get rid
[1637.28 → 1638.18] of the make file
[1638.18 → 1638.94] and all of that
[1638.94 → 1640.10] with dagger
[1640.10 → 1641.20] and just have
[1641.20 → 1642.78] like say
[1642.78 → 1643.60] you were
[1643.60 → 1645.08] building a startup
[1645.08 → 1645.86] or application
[1645.86 → 1646.80] and
[1646.80 → 1648.32] you didn't
[1648.32 → 1648.70] have
[1648.70 → 1649.16] the
[1649.16 → 1650.66] experience
[1650.66 → 1651.34] that Justin
[1651.34 → 1651.74] has
[1651.74 → 1652.52] right
[1652.52 → 1653.14] and you
[1653.14 → 1653.52] just needed
[1653.52 → 1654.10] to figure out
[1654.10 → 1654.56] how to make
[1654.56 → 1655.40] your CI,
[1655.48 → 1655.64] CD
[1655.64 → 1656.12] and like
[1656.12 → 1656.70] your DevOps
[1656.70 → 1657.94] like just
[1657.94 → 1658.74] whole realm
[1658.74 → 1659.30] work
[1659.30 → 1659.96] and you don't
[1659.96 → 1660.74] have that experience
[1660.74 → 1661.32] does this now
[1661.32 → 1661.86] enable you
[1661.86 → 1662.36] to skip
[1662.36 → 1663.60] all of those
[1663.60 → 1664.38] extra files
[1664.38 → 1665.28] in different ways
[1665.28 → 1665.88] and just have
[1665.88 → 1666.46] your whole team
[1666.46 → 1667.24] learn how to
[1667.24 → 1668.18] do your infrastructure
[1668.18 → 1668.92] in that way
[1668.92 → 1669.64] using dagger
[1669.64 → 1670.80] yes
[1670.80 → 1671.92] if you would
[1671.92 → 1672.80] go to the modules
[1672.80 → 1673.36] that Justin
[1673.36 → 1674.24] if so first
[1674.24 → 1674.76] it would require
[1674.76 → 1675.84] Justin to take time
[1675.84 → 1677.32] to write the modules
[1677.32 → 1678.40] and to share them
[1678.40 → 1679.02] so that others
[1679.02 → 1679.94] can discover them
[1679.94 → 1681.24] it's just a matter
[1681.24 → 1681.66] of basically
[1681.66 → 1682.24] putting him
[1682.24 → 1683.02] on his
[1683.02 → 1683.78] GitHub repository
[1683.78 → 1685.36] the convention
[1685.36 → 1686.08] is Dagger verse
[1686.08 → 1687.90] so many people
[1687.90 → 1688.84] have the Dagger verse
[1688.84 → 1689.12] repo
[1689.12 → 1690.24] which is a
[1690.24 → 1691.04] collection
[1691.04 → 1691.60] of the different
[1691.60 → 1692.08] modules
[1692.08 → 1692.84] that people
[1692.84 → 1693.52] use and wrote
[1693.52 → 1694.92] so at this point
[1694.92 → 1696.58] there's I think
[1696.58 → 1697.36] five or six
[1697.36 → 1698.30] implementations
[1698.30 → 1699.32] of the Go
[1699.32 → 1700.08] module
[1700.08 → 1701.40] which does all
[1701.40 → 1701.94] things around
[1701.94 → 1702.68] Go applications
[1702.68 → 1703.38] testing
[1703.38 → 1704.14] building
[1704.14 → 1704.74] linting
[1704.74 → 1705.42] all those things
[1705.42 → 1706.50] so you're right
[1706.50 → 1706.88] in the sense
[1706.88 → 1707.28] that you would
[1707.28 → 1708.30] need to figure out
[1708.30 → 1709.26] how to write
[1709.26 → 1709.86] that automation
[1709.86 → 1710.66] just a matter
[1710.66 → 1711.70] of using it
[1711.70 → 1712.66] you have a Go app
[1712.66 → 1713.20] great
[1713.20 → 1714.04] this is how
[1714.04 → 1714.42] you provide
[1714.42 → 1714.92] the source
[1714.92 → 1716.02] and this is
[1716.02 → 1716.76] what options
[1716.76 → 1717.20] are available
[1717.20 → 1717.62] to you
[1717.62 → 1718.80] and you can
[1718.80 → 1719.22] try running
[1719.22 → 1719.62] it locally
[1719.62 → 1720.82] it works
[1720.82 → 1721.30] great
[1721.30 → 1721.92] so how do I
[1721.92 → 1722.50] run this in CI
[1722.50 → 1723.80] the same commands
[1723.80 → 1724.86] the same commands
[1724.86 → 1725.28] that you'd run
[1725.28 → 1725.62] locally
[1725.62 → 1726.42] you'd put in CI
[1726.42 → 1726.92] and it would
[1726.92 → 1727.48] work exactly
[1727.48 → 1727.90] the same
[1727.90 → 1729.24] no more figuring
[1729.24 → 1729.88] of YAML
[1729.88 → 1730.56] no more figuring
[1730.56 → 1731.22] of a lot of
[1731.22 → 1731.52] things like
[1731.52 → 1731.88] caching
[1731.88 → 1732.56] for example
[1732.56 → 1733.20] I mean
[1733.20 → 1734.00] we haven't even
[1734.00 → 1734.68] like unpacked
[1734.68 → 1736.18] this aspect
[1736.18 → 1736.60] of Dagger
[1736.60 → 1737.60] how it caches
[1737.60 → 1739.12] how it for example
[1739.12 → 1740.32] sends open
[1740.32 → 1741.12] telemetry traces
[1741.12 → 1742.28] for every single
[1742.28 → 1742.96] operation which
[1742.96 → 1743.84] happens inside
[1743.84 → 1744.10] of it
[1744.10 → 1744.46] there's like
[1744.46 → 1745.10] so much
[1745.10 → 1745.38] here
[1745.38 → 1746.60] at a surface
[1746.60 → 1747.46] it looks like
[1747.46 → 1748.34] it's a replacement
[1748.34 → 1749.10] for your scripts
[1749.10 → 1750.92] a way of
[1750.92 → 1751.86] embedding this
[1751.86 → 1752.30] knowledge and
[1752.30 → 1752.86] sharing it with
[1752.86 → 1753.20] others
[1753.20 → 1754.44] but other tools
[1754.44 → 1754.94] have done this
[1754.94 → 1755.34] before
[1755.34 → 1756.60] so how is this
[1756.60 → 1756.92] special
[1756.92 → 1757.86] it's all the
[1757.86 → 1758.68] other things
[1758.68 → 1759.74] which we haven't
[1759.74 → 1760.34] gotten into
[1760.34 → 1761.18] which makes it
[1761.18 → 1763.18] a very
[1763.18 → 1764.84] comprehensive way
[1764.84 → 1766.32] of putting
[1766.32 → 1767.26] automation in
[1767.26 → 1767.52] code
[1767.52 → 1768.34] sharing it with
[1768.34 → 1768.64] others
[1768.64 → 1769.44] and letting
[1769.44 → 1770.46] others reuse it
[1770.46 → 1771.00] rather than
[1771.00 → 1771.88] everyone having to
[1771.88 → 1773.08] write the same
[1773.08 → 1773.56] thing in their
[1773.56 → 1774.62] own specific way
[1774.62 → 1775.36] I think the
[1775.36 → 1775.82] code piece for
[1775.82 → 1776.24] me is always
[1776.24 → 1776.72] kind of that
[1776.72 → 1777.64] barrier for a
[1777.64 → 1778.08] lot of people
[1778.08 → 1779.94] because saying
[1779.94 → 1780.48] you get to
[1780.48 → 1781.04] write all your
[1781.04 → 1781.76] automation in
[1781.76 → 1782.20] the code you're
[1782.20 → 1782.80] familiar with
[1782.80 → 1784.38] is a lockout
[1784.38 → 1784.84] for a lot of
[1784.84 → 1785.22] people because
[1785.22 → 1785.42] a lot of
[1785.42 → 1785.80] people don't
[1785.80 → 1786.04] they're not
[1786.04 → 1786.50] comfortable with
[1786.50 → 1786.74] code
[1786.74 → 1787.26] they're not
[1787.26 → 1787.92] all the people
[1787.92 → 1788.58] writing YAML
[1788.58 → 1789.30] are expert
[1789.30 → 1790.38] YAML engineers
[1790.38 → 1792.46] they know how
[1792.46 → 1793.62] the GitLab
[1793.62 → 1794.26] YAML is going
[1794.26 → 1794.92] to do something
[1794.92 → 1795.66] different on
[1795.66 → 1796.58] something that
[1796.58 → 1798.08] has a list
[1798.08 → 1798.72] versus an array
[1798.72 → 1799.48] whatever it is
[1799.48 → 1799.76] right like
[1799.76 → 1800.12] they're like
[1800.12 → 1800.92] I know this
[1800.92 → 1801.88] thing but once
[1801.88 → 1802.46] you ask me to
[1802.46 → 1802.92] like go write
[1802.92 → 1803.68] some go code
[1803.68 → 1805.00] I'm not as
[1805.00 → 1805.60] familiar with
[1805.60 → 1806.02] that and I
[1806.02 → 1806.58] feel a little
[1806.58 → 1807.72] bit out of
[1807.72 → 1808.90] place if I'm
[1808.90 → 1809.44] the one that
[1809.44 → 1809.98] is like an
[1809.98 → 1810.84] external person
[1810.84 → 1812.04] going into do
[1812.04 → 1812.64] and maintain
[1812.64 → 1813.54] and do this
[1813.54 → 1814.16] thing for another
[1814.16 → 1815.12] team that's an
[1815.12 → 1815.64] application team
[1815.64 → 1815.88] right because
[1815.88 → 1817.02] like a lot of
[1817.02 → 1817.36] companies I've
[1817.36 → 1817.70] worked at the
[1817.70 → 1818.32] app teams were
[1818.32 → 1818.90] always this like
[1818.90 → 1819.74] high level like
[1819.74 → 1820.24] you don't mess
[1820.24 → 1820.86] with them like
[1820.86 → 1821.24] they're the ones
[1821.24 → 1821.94] making the money
[1821.94 → 1823.14] and all you other
[1823.14 → 1823.62] people are just
[1823.62 → 1824.82] overhead and
[1824.82 → 1825.30] you're just like
[1825.30 → 1825.84] oh you write the
[1825.84 → 1826.30] YAML everyone
[1826.30 → 1827.02] else writes code
[1827.02 → 1827.80] right and like that
[1827.80 → 1828.34] I think is a
[1828.34 → 1829.06] barrier for a lot
[1829.06 → 1829.48] of people
[1829.48 → 1830.60] I think it's also
[1830.60 → 1831.46] perspective though
[1831.46 → 1832.06] because think about
[1832.06 → 1832.64] it when you go to
[1832.64 → 1833.46] school for computer
[1833.46 → 1834.36] science or you
[1834.36 → 1835.30] first get into
[1835.30 → 1836.48] like computers
[1836.48 → 1837.64] you're writing
[1837.64 → 1838.92] Python or Java
[1838.92 → 1840.00] right and nobody
[1840.00 → 1840.64] tells you about
[1840.64 → 1841.36] DevOps nobody
[1841.36 → 1841.96] tells you about
[1841.96 → 1842.94] scripting unless
[1842.94 → 1844.54] you somehow just
[1844.54 → 1845.36] stumble on that so
[1845.36 → 1846.78] I think for people
[1846.78 → 1847.76] that maybe started
[1847.76 → 1848.94] in systems or
[1848.94 → 1849.62] started with
[1849.62 → 1851.00] scripting yeah but
[1851.00 → 1852.40] it's a huge barrier
[1852.40 → 1853.38] for people who just
[1853.38 → 1854.36] started writing the
[1854.36 → 1855.62] high level code and
[1855.62 → 1856.28] then all of a sudden
[1856.28 → 1856.96] they're thrown into
[1856.96 → 1857.46] a production
[1857.46 → 1858.28] environment well now
[1858.28 → 1858.96] they have to manage
[1858.96 → 1860.56] infrastructure like I
[1860.56 → 1861.24] think you have more
[1861.24 → 1862.18] people coming from
[1862.18 → 1863.38] the like writing
[1863.38 → 1864.34] code because like
[1864.34 → 1864.92] when you think about
[1864.92 → 1865.56] it when you hear
[1865.56 → 1867.62] boot camps or school
[1867.62 → 1868.98] or you go to these
[1868.98 → 1870.32] different like ways
[1870.32 → 1871.06] that people are being
[1871.06 → 1872.16] educated to like get
[1872.16 → 1873.14] into the tech industry
[1873.14 → 1874.42] everybody tells you
[1874.42 → 1875.12] about the code and
[1875.12 → 1875.92] nobody tells you about
[1875.92 → 1877.06] the scripting and the
[1877.06 → 1878.98] version control and
[1878.98 → 1881.50] the DevOps and CCD
[1881.50 → 1883.10] right so like I think
[1883.10 → 1884.94] this is a great tool
[1884.94 → 1886.10] for those people and
[1886.10 → 1886.74] making it more
[1886.74 → 1887.94] accessible to get into
[1887.94 → 1889.22] DevOps and CCD and
[1889.22 → 1890.30] to be able to maintain
[1890.30 → 1891.02] your infrastructure
[1891.02 → 1892.38] because everybody
[1892.38 → 1893.18] talks about making
[1893.18 → 1894.22] this really cool app
[1894.22 → 1894.96] and nobody talks about
[1894.96 → 1895.90] maintaining that really
[1895.90 → 1896.78] cool app and releasing
[1896.78 → 1898.04] it you know that's why
[1898.04 → 1898.56] we're here that's what
[1898.56 → 1899.30] this podcast goes for
[1899.30 → 1900.96] yeah exactly but
[1900.96 → 1901.64] I think that's a great
[1901.64 → 1902.30] point where it's like
[1902.30 → 1903.34] it's an it's a barrier
[1903.34 → 1904.78] both ways there's the
[1904.78 → 1905.66] person that's only ever
[1905.66 → 1906.90] written web apps with
[1906.90 → 1907.82] spring boots like
[1907.82 → 1908.74] they're like I don't I
[1908.74 → 1909.12] don't know what this
[1909.12 → 1910.08] Docker thing is like
[1910.08 → 1911.80] don't like you
[1911.80 → 1912.24] know I'm not going to
[1912.24 → 1913.50] go into the weeds of
[1913.50 → 1914.34] something that's not my
[1914.34 → 1915.26] thing it's like actually
[1915.26 → 1916.76] it's all your thing and
[1916.76 → 1917.34] same thing for the
[1917.34 → 1918.14] system people like I
[1918.14 → 1919.70] don't know how the JVM
[1919.70 → 1920.38] is going to do that
[1920.38 → 1920.94] thing like well you
[1920.94 → 1921.74] better learn because
[1921.74 → 1922.84] that's also your thing
[1922.84 → 1923.68] because I feel like
[1923.68 → 1924.34] when they like they'll
[1924.34 → 1925.10] be like okay you have
[1925.10 → 1926.02] to learn front end but
[1926.02 → 1926.66] then you have to learn
[1926.66 → 1927.56] the back end and then
[1927.56 → 1928.08] you have to learn how
[1928.08 → 1929.34] to fix how to make that
[1929.34 → 1930.12] connect to a database
[1930.12 → 1931.20] but nobody's ever
[1931.20 → 1932.24] talking about how to
[1932.24 → 1934.32] like keep all of this
[1934.32 → 1935.56] working together and
[1935.56 → 1936.74] maintaining it and
[1936.74 → 1938.24] yeah you know so it's
[1938.24 → 1940.30] like I felt like all the
[1940.30 → 1941.30] whole time during school
[1941.30 → 1941.98] and going through
[1941.98 → 1943.22] training at AWS and
[1943.22 → 1943.84] going through different
[1943.84 → 1944.82] boot camps and everything
[1944.82 → 1945.94] like I was like why are
[1945.94 → 1947.52] we always like we
[1947.52 → 1948.54] talk about the main
[1948.54 → 1950.00] like the big main
[1950.00 → 1950.96] products but nobody
[1950.96 → 1951.76] talks about all the
[1951.76 → 1952.56] secrets you need to
[1952.56 → 1953.36] make all of it work
[1953.36 → 1954.34] together you know
[1954.34 → 1956.10] one analogy that I
[1956.10 → 1956.68] think works really
[1956.68 → 1958.12] well when you're
[1958.12 → 1958.90] trying to approach
[1958.90 → 1959.44] dagger, and you're
[1959.44 → 1960.06] trying just like to
[1960.06 → 1960.74] figure out like where
[1960.74 → 1961.74] does this thing fit in
[1961.74 → 1963.82] imagine that what
[1963.82 → 1964.78] you're building is a
[1964.78 → 1966.46] software factory right
[1966.46 → 1967.68] your startup your
[1967.68 → 1968.84] company your team
[1968.84 → 1969.60] whatever it is you
[1969.60 → 1970.54] are a software factory
[1970.54 → 1972.44] you are delivering value
[1972.44 → 1973.56] to your users in the
[1973.56 → 1974.40] form of software or
[1974.40 → 1975.84] through software great
[1975.84 → 1977.24] where's the thing
[1977.24 → 1978.82] that helps you
[1978.82 → 1979.82] maintain your factory
[1979.82 → 1980.88] where's the thing
[1980.88 → 1981.80] that helps you do all
[1981.80 → 1982.70] the things that you
[1982.70 → 1984.58] normally I mean there's
[1984.58 → 1985.60] not that much value in
[1985.60 → 1986.24] figuring out for
[1986.24 → 1987.16] example how to run your
[1987.16 → 1988.36] tests right or how to
[1988.36 → 1989.82] cache them properly or
[1989.82 → 1993.12] how to maybe lint
[1993.12 → 1994.26] that's another one how
[1994.26 → 1995.90] to package I mean how
[1995.90 → 1997.00] many hours do you want
[1997.00 → 1997.92] to spend figuring out
[1997.92 → 1999.66] how to package a JVM
[1999.66 → 2000.50] container or Java
[2000.50 → 2002.82] container seriously I
[2002.82 → 2004.16] mean sure there's like
[2004.16 → 2005.02] recipes that you can
[2005.02 → 2006.08] copy and AI is very
[2006.08 → 2007.98] helpful but what if
[2007.98 → 2009.22] some people that were
[2009.22 → 2010.10] really passionate about
[2010.10 → 2010.98] this and had the time
[2010.98 → 2012.86] they encoded this in
[2012.86 → 2013.86] Java let's say using
[2013.86 → 2015.14] Java and then just get
[2015.14 → 2016.60] to use it wouldn't that
[2016.60 → 2018.20] be nice but not just
[2018.20 → 2019.12] that when you have AI
[2019.12 → 2020.22] do if it's very hard to
[2020.22 → 2021.40] get the context but if
[2021.40 → 2022.40] somebody else on your
[2022.40 → 2023.64] team and that or
[2023.64 → 2024.62] somebody else that works
[2024.62 → 2025.52] at the same company as
[2025.52 → 2026.40] you that you can ping
[2026.40 → 2027.34] and be like hey I want
[2027.34 → 2028.34] to reuse this but I
[2028.34 → 2029.08] don't understand this
[2029.08 → 2030.58] part you know yeah and
[2030.58 → 2031.40] if you give people make
[2031.40 → 2032.88] files or Jenkins files or
[2032.88 → 2034.34] YAML what do they say
[2034.34 → 2035.16] mean when was the last
[2035.16 → 2035.90] time you received like
[2035.90 → 2036.66] a YAML package and
[2036.66 → 2037.36] you said wow this is
[2037.36 → 2038.20] cool I'm going to use
[2038.20 → 2039.68] this is amazing
[2039.68 → 2040.66] when did someone get
[2040.66 → 2041.46] excited about Jenkins
[2041.46 → 2043.46] file rarely not just
[2043.46 → 2044.50] that, but it never works
[2044.50 → 2045.52] the same for everybody
[2045.52 → 2048.64] exactly like everyone's
[2048.64 → 2049.58] like use this, and it's
[2049.58 → 2050.48] so easy, and you're like
[2050.48 → 2053.26] is it though I mean
[2053.26 → 2054.02] same thing can be said
[2054.02 → 2056.08] for a lot of like code
[2056.08 → 2056.80] though right like
[2056.80 → 2058.90] so many NPM modules and
[2058.90 → 2059.92] Python things I've tried
[2059.92 → 2060.70] to solve like this is
[2060.70 → 2061.80] broken right like what
[2061.80 → 2062.76] what is the expectations
[2062.76 → 2063.60] of this thing to work
[2063.60 → 2064.20] and I think that
[2064.20 → 2066.02] encapsulating that in a
[2066.02 → 2068.66] holistic container that
[2068.66 → 2069.48] can do some of that has
[2069.48 → 2070.76] has been to solve for a
[2070.76 → 2071.54] lot of those things but
[2071.54 → 2072.34] once I'm like I need to
[2072.34 → 2073.64] go write some software
[2073.64 → 2075.26] around this thing but I
[2075.26 → 2076.56] can't even run this thing
[2076.56 → 2078.96] is a problem yeah and
[2078.96 → 2079.44] when it comes to
[2079.44 → 2080.42] introspecting it's okay
[2080.42 → 2081.44] so great, so I have this
[2081.44 → 2083.02] command which I run great
[2083.02 → 2083.88] I'll figure out how to
[2083.88 → 2084.64] run it let's see it's in
[2084.64 → 2086.10] the make file so what is
[2086.10 → 2086.94] actually happening in
[2086.94 → 2087.60] this thing when it
[2087.60 → 2089.30] executes how can I
[2089.30 → 2090.92] visualize the execution
[2090.92 → 2092.64] of the different steps
[2092.64 → 2094.50] how do I know when a
[2094.50 → 2095.32] step runs or doesn't
[2095.32 → 2096.20] run I mean I used to
[2096.20 → 2097.64] love make I still have
[2097.64 → 2098.66] make files around which
[2098.66 → 2099.82] I still use to this day
[2099.82 → 2102.04] and they're great just
[2102.04 → 2103.30] files same thing only
[2103.30 → 2104.50] recently on the Kaiden we
[2104.50 → 2105.64] talked about just files
[2105.64 → 2107.76] and how just makes more
[2107.76 → 2108.94] sense in the context of
[2108.94 → 2110.42] changelog that's great
[2110.42 → 2111.76] you know if you're happy
[2111.76 → 2112.50] with your make file if
[2112.50 → 2113.00] you're happy with your
[2113.00 → 2114.06] just file any automation
[2114.06 → 2114.92] that you have that works
[2114.92 → 2116.92] for you keep if it's a
[2116.92 → 2117.78] good thing it's an asset
[2117.78 → 2119.58] it's not a liability but
[2119.58 → 2120.68] when that thing stops
[2120.68 → 2122.32] working when you get
[2122.32 → 2124.04] frustrated when you get
[2124.04 → 2124.92] all the issues with
[2124.92 → 2126.56] YAML and all the things
[2126.56 → 2127.54] that you know you've been
[2127.54 → 2128.56] maybe toiling away for
[2128.56 → 2130.30] years and years when you
[2130.30 → 2131.44] will consider something
[2131.44 → 2132.90] better have a look and
[2132.90 → 2133.80] see if that makes sense
[2133.80 → 2135.88] and then discover the web
[2135.88 → 2138.28] UI discover the traces
[2138.28 → 2140.08] discover all the things
[2140.08 → 2141.16] which are available and
[2141.16 → 2141.80] which are getting better
[2141.80 → 2143.04] discover the shell I
[2143.04 → 2143.74] haven't even talked about
[2143.74 → 2144.46] the shell that's by the
[2144.46 → 2145.20] way that's like a hidden
[2145.20 → 2147.22] experimental feature that
[2147.22 → 2148.16] is coming in a future
[2148.16 → 2149.70] dagger release that's
[2149.70 → 2150.74] been shipped silently
[2150.74 → 2152.30] for a while but if
[2152.30 → 2153.26] you are interested you
[2153.26 → 2154.00] can join the community
[2154.00 → 2155.00] calls, and you can find
[2155.00 → 2156.40] out more but enough
[2156.40 → 2157.58] about dagger we can
[2157.58 → 2158.46] talk about infrastructure
[2158.46 → 2159.78] if you want I want to
[2159.78 → 2160.48] lean into like all the
[2160.48 → 2161.00] other things you're
[2161.00 → 2161.42] talking about right
[2161.42 → 2162.12] because like I have a
[2162.12 → 2163.32] plenty of make files I've
[2163.32 → 2164.28] never loved make I've
[2164.28 → 2164.82] always thought it was
[2164.82 → 2166.12] arcane and hard to learn
[2166.12 → 2167.34] in a kind of in a
[2167.34 → 2168.98] very gatekeeper way right
[2168.98 → 2169.72] I was like this is like
[2169.72 → 2171.36] someone learned it once
[2171.36 → 2172.58] 18 years ago, and they're
[2172.58 → 2173.22] like yeah I wrote that
[2173.22 → 2174.40] make file I have no idea
[2174.40 → 2175.52] what it does, and it's
[2175.52 → 2176.44] always been really hard to
[2176.44 → 2177.50] get back into it, you're
[2177.50 → 2178.82] like this is all obscure
[2178.82 → 2180.22] old docs that aren't
[2180.22 → 2181.90] relevant anymore and
[2181.90 → 2182.76] it works right like if
[2182.76 → 2183.46] it's the thing if it
[2183.46 → 2184.90] keeps working cool it's
[2184.90 → 2185.66] probably you a
[2185.66 → 2186.56] problem if it doesn't
[2186.56 → 2188.00] work it works somewhere
[2188.00 → 2189.72] but you talk about like
[2189.72 → 2190.64] dagger is a drop-in
[2190.64 → 2191.44] replacement for some of
[2191.44 → 2192.24] those things but what
[2192.24 → 2193.86] are the other things like
[2193.86 → 2195.56] on the edges there we're
[2195.56 → 2196.52] like actually what are we
[2196.52 → 2197.86] missing out on by not
[2197.86 → 2199.28] doing this by not having
[2199.28 → 2201.54] a newer tool to be able
[2201.54 → 2202.02] to do that you've
[2202.02 → 2202.50] mentioned open
[2202.50 → 2203.56] telemetry you've
[2203.56 → 2204.26] mentioned the shell you
[2204.26 → 2206.12] mentioned modules like
[2206.12 → 2207.72] those are all pieces but
[2207.72 → 2209.34] it's hard to understand
[2209.34 → 2210.84] like why do I need those
[2210.84 → 2212.00] things or what what what
[2212.00 → 2212.94] can't I do today
[2212.94 → 2216.54] okay so modules as a
[2216.54 → 2218.00] category it's a way to
[2218.00 → 2219.38] package the code that you
[2219.38 → 2220.58] wrote and share it with
[2220.58 → 2222.50] others think about it like
[2222.50 → 2223.62] an atomic piece of code
[2223.62 → 2224.66] that go well together for
[2224.66 → 2226.66] example the go module
[2226.66 → 2228.50] would encapsulate all the
[2228.50 → 2229.68] code for writing with go
[2229.68 → 2231.22] apps there's something for
[2231.22 → 2232.30] node.js there's something
[2232.30 → 2233.86] for helm there's something
[2233.86 → 2235.94] for even Kubernetes if
[2235.94 → 2236.82] you want to figure out
[2236.82 → 2238.36] how to run k3s inside
[2238.36 → 2239.36] dagger that is possible
[2239.36 → 2241.94] many things like this are
[2241.94 → 2242.94] in the dagger verse
[2242.94 → 2244.42] dagger verse.dev is the
[2244.42 → 2246.36] place to go to check what
[2246.36 → 2247.46] modules are available what
[2247.46 → 2249.00] can I pick and choose so
[2249.00 → 2250.02] those are the
[2250.02 → 2251.60] modules the open
[2251.60 → 2254.74] telemetry is how we
[2254.74 → 2256.62] capture what happens
[2256.62 → 2258.12] inside a dagger call
[2258.12 → 2259.84] when basically dagger runs
[2259.84 → 2262.64] and we are sending all that
[2262.64 → 2264.42] information to dagger cloud
[2264.42 → 2266.64] using these traces so that
[2266.64 → 2268.68] we can visualize what
[2268.68 → 2271.96] happens in your run and
[2271.96 → 2272.98] think of like the network
[2272.98 → 2275.32] graph so in the browser if
[2275.32 → 2275.90] you were to open the
[2275.90 → 2276.84] network graph, and you would
[2276.84 → 2278.54] see how long resources take
[2278.54 → 2280.50] to load the spans the
[2280.50 → 2281.92] traces it's exactly the same
[2281.92 → 2285.10] concept so that gives you a
[2285.10 → 2287.42] very deep insight into what
[2287.42 → 2288.48] happens in your automation
[2288.48 → 2290.64] and you can see which are the
[2290.64 → 2291.90] steps which take a long time
[2291.90 → 2294.06] or which are the steps which
[2294.06 → 2295.48] for example don't cash well
[2295.48 → 2297.92] all that information would be
[2297.92 → 2299.02] conveyed in this case in
[2299.02 → 2302.36] dagger cloud so the way to do
[2302.36 → 2303.46] that you just basically connect
[2303.46 → 2305.32] your CLI to your dagger cloud
[2305.32 → 2306.50] account you have to create one
[2306.50 → 2309.14] for it's basically free for
[2309.14 → 2311.50] individuals for teams it is a
[2311.50 → 2313.56] paid plan but as an individual
[2313.56 → 2315.28] you can try to see what this
[2315.28 → 2317.54] looks like, and you know you can
[2317.54 → 2319.16] maybe bring your team members
[2319.16 → 2320.42] over your shoulder to look or
[2320.42 → 2321.50] share your screen to see what
[2321.50 → 2322.62] it looks like everyone can do
[2322.62 → 2324.70] this so that gives you an
[2324.70 → 2326.16] insight and appreciation of all
[2326.16 → 2327.16] the things that happen in your
[2327.16 → 2329.18] automation and then the shell
[2329.18 → 2332.10] the third thing is a way to
[2332.10 → 2335.26] put yourself in a context where
[2335.26 → 2337.30] you're trying to discover what
[2337.30 → 2339.78] automation is available and how
[2339.78 → 2341.52] to stitch the different functions
[2341.52 → 2343.42] together it's exactly how it
[2343.42 → 2346.44] use pipes how you basically get
[2346.44 → 2348.70] functionality from different parts
[2348.70 → 2351.00] and try experimenting with it to
[2351.00 → 2353.58] see what makes sense so what is
[2353.58 → 2355.86] the right arrangement for this for
[2355.86 → 2359.88] example pipeline that caches well
[2359.88 → 2362.20] that works well that the expensive
[2362.20 → 2363.80] steps happen first, and you can do
[2363.80 → 2365.64] that in the dagger shell so it's a
[2365.64 → 2368.50] way to interactively discover and work
[2368.50 → 2370.72] with your automation and the
[2370.72 → 2373.46] perspective is the functions that are
[2373.46 → 2376.56] declared in dagger so that is the
[2376.56 → 2378.76] starting point I think that's really
[2378.76 → 2380.16] important because we don't have
[2380.16 → 2382.36] enough ops availability and like
[2382.36 → 2385.08] actual like insight into our
[2385.08 → 2386.90] automation like automation is a great
[2386.90 → 2388.70] tool, and it makes it where you can
[2388.70 → 2391.46] scale and take a lot of the human
[2391.46 → 2393.32] area out but if you don't have a deep
[2393.32 → 2394.94] understanding of your automation it
[2394.94 → 2397.52] makes it really hard to maintain and to
[2397.52 → 2400.00] scale it and just to use it in general
[2400.00 → 2401.84] when it breaks you're kind of out of
[2401.84 → 2403.74] luck all these things put together
[2403.74 → 2406.62] it's about an experience which is a
[2406.62 → 2408.70] bit more visual it's an experience
[2408.70 → 2409.98] which is a little bit more curated
[2409.98 → 2412.82] right it's almost like what would you
[2412.82 → 2416.40] do if you had to do automation
[2416.40 → 2418.70] properly what would you do if you had
[2418.70 → 2423.82] to not reinvent but I would say rethink
[2423.82 → 2426.06] how make files and how your Jenkins
[2426.06 → 2429.92] files and how your scripts should work in
[2429.92 → 2432.42] a container first world and containers
[2432.42 → 2433.46] are important because it's that
[2433.46 → 2436.72] immutable thing right because those
[2436.72 → 2438.58] are like having something immutable
[2438.58 → 2440.22] having something that caches having an
[2440.22 → 2443.08] actual layer is able to speed things up
[2443.08 → 2445.44] in a way that's difficult to do
[2445.44 → 2448.42] otherwise make file is local right how
[2448.42 → 2450.92] do you distribute in make file
[2450.92 → 2453.30] resolution it has a dag but how do you
[2453.30 → 2455.54] distribute the dag and that's something
[2455.54 → 2457.32] which today for example in dagger
[2457.32 → 2459.34] getting very close to that being
[2459.34 → 2459.82] possible
[2459.82 → 2461.26] what do you mean by close like what's
[2461.26 → 2461.72] missing there
[2461.72 → 2465.52] so how do you have a cache like we
[2465.52 → 2467.08] tried a couple of iterations and we
[2467.08 → 2468.76] know how this fails how do you have a
[2468.76 → 2473.26] remote cache that you can safely store
[2473.26 → 2475.82] operations in at scale so imagine every
[2475.82 → 2477.60] single step that runs right it has some
[2477.60 → 2480.46] inputs it does a function and then it
[2480.46 → 2482.86] has some outputs if you're able to cache
[2482.86 → 2485.66] those outputs put them somewhere like a
[2485.66 → 2488.08] CDN or an object storage by the way the
[2488.08 → 2489.62] object storage is what we have
[2489.62 → 2492.36] and we had and then when a pipeline
[2492.36 → 2493.92] runs again or the same call runs again
[2493.92 → 2496.12] doesn't matter where you call it from as
[2496.12 → 2498.44] long as the engine is connected to this
[2498.44 → 2501.42] object store it can retrieve the steps
[2501.42 → 2502.94] right it can retrieve the layers doesn't
[2502.94 → 2505.44] have to recompute them sometimes it's a
[2505.44 → 2507.36] lot more efficient to pull down these
[2507.36 → 2508.62] layers rather than recompute the
[2508.62 → 2511.28] operation how do you do that safely at
[2511.28 → 2516.22] scale in a way that is easy to use and
[2516.22 → 2517.92] it's easy to operate that is the hard
[2517.92 → 2519.58] part caches should always be invisible
[2519.58 → 2521.44] right like you just like the easiest
[2521.44 → 2522.74] cache is the one you don't know you're
[2522.74 → 2525.20] using that's a local one locally it
[2525.20 → 2527.04] works well when you go distributed that's
[2527.04 → 2528.20] when problems start that's when you have
[2528.20 → 2529.98] race conditions that's when you have
[2529.98 → 2531.58] pruning for example that's when you have
[2531.58 → 2532.72] all sorts of things that you have to
[2532.72 → 2535.54] deal with when you're dealing with many
[2535.54 → 2537.62] terabytes like hundreds of terabytes of
[2537.62 → 2540.22] this data it becomes a hard problem and
[2540.22 → 2542.88] sometimes depending on network I wouldn't
[2542.88 → 2546.24] say even like a network conditions it
[2546.24 → 2548.28] can be cheaper to recompute it locally
[2548.28 → 2550.84] yeah how much of that can you rely on
[2550.84 → 2552.56] like what docker does for caching right
[2552.56 → 2554.48] because I can have my build x cache
[2554.48 → 2556.36] somewhere which is basically the same
[2556.36 → 2558.28] thing of I get this layer that has a
[2558.28 → 2560.54] shah and I can say oh I'm going to get
[2560.54 → 2561.84] the same shah just give me the data
[2561.84 → 2564.82] right like how much of that is using
[2564.82 → 2566.56] what's under the hood by relying on
[2566.56 → 2568.98] containers versus building something that
[2568.98 → 2572.50] do so that makes sense when the inputs
[2572.50 → 2575.02] don't change that frequently in this
[2575.02 → 2577.56] case an input is source code and source
[2577.56 → 2580.46] code churns a lot so how can you still
[2580.46 → 2583.62] have a good cache hit ratio when your
[2583.62 → 2585.96] input is something that changes like on a
[2585.96 → 2588.64] like with every commit so how do you
[2588.64 → 2591.02] sequence right your source code how do
[2591.02 → 2593.02] you compare compartmentalize it so that you
[2593.02 → 2595.74] know which functions depend on which
[2595.74 → 2598.64] source code so that you get like
[2598.64 → 2601.42] invalidations working properly and you
[2601.42 → 2603.14] don't bust the cache too often and that
[2603.14 → 2603.84] is a hard problem
[2603.84 → 2612.78] what's up nerds I'm here with Kurt Mackie
[2612.78 → 2616.02] co-founder and CEO of fly you know we
[2616.02 → 2617.90] love to fly so Kurt I want to talk to you
[2617.90 → 2620.56] about the magic of the cloud you have
[2620.56 → 2622.86] thoughts on this right I think it's
[2622.86 → 2624.46] valuable to understand the magic line of
[2624.46 → 2626.08] cloud because you can build better
[2626.08 → 2628.14] features for users basically if you
[2628.14 → 2629.64] understand that you can do a lot of
[2629.64 → 2631.62] stuff particularly now that people are
[2631.62 → 2633.44] doing LLM stuff, but you can do a lot of
[2633.44 → 2635.32] stuff if you get that and can be creative
[2635.32 → 2637.56] with it so when you say clouds aren't
[2637.56 → 2639.80] magic because you're building a public
[2639.80 → 2641.94] cloud for developers, and you go on to
[2641.94 → 2644.70] explain exactly how it works what does
[2644.70 → 2646.40] that mean to you in some ways it means
[2646.40 → 2648.32] these all came from somewhere like there
[2648.32 → 2650.38] was a simpler time before clouds where
[2650.38 → 2652.22] we'd get a server at rack shack, and we'd
[2652.22 → 2656.30] ssh or telnet into it even and put files
[2656.30 → 2658.26] somewhere and run the web servers
[2658.26 → 2660.18] ourselves to serve them up to users
[2660.18 → 2662.38] clouds are not magic on top of that
[2662.38 → 2663.84] they're just more complicated ways of
[2663.84 → 2665.84] doing those same things in a way that
[2665.84 → 2667.44] meets the needs of a lot of people
[2667.44 → 2669.16] instead of just one of the things i
[2669.16 → 2671.22] think that people miss out on and a lot
[2671.22 → 2674.00] of this is actually because AWS and GCP
[2674.00 → 2676.12] have created such big black box
[2676.12 → 2678.02] abstractions like lambda is really
[2678.02 → 2679.92] black boxy you can't like pick apart
[2679.92 → 2681.04] lambda and see how it works from the
[2681.04 → 2682.72] outside you have to sort of just use
[2682.72 → 2684.08] what's there, but the reality is like
[2684.08 → 2686.02] lambda is not all that complicated it's
[2686.02 → 2687.90] just a modern way to launch little VMS
[2687.90 → 2690.64] and serve some requests from them and
[2690.64 → 2693.02] let them like kind of pause and resume
[2693.02 → 2695.46] and free up like physical compute time
[2695.46 → 2697.10] the interesting thing about understanding
[2697.10 → 2698.78] how clouds work is it lets you build
[2698.78 → 2700.50] kind of features for your users you
[2700.50 → 2702.10] would never expect it and our canonical
[2702.10 → 2703.96] version of this for us is that like
[2703.96 → 2705.38] when we looked at how we wanted to
[2705.38 → 2707.22] isolate user code we decided to just
[2707.22 → 2709.62] expose this machines concept which is a
[2709.62 → 2711.10] much lower level abstraction lambda
[2711.10 → 2712.84] that you could use to build lambda on
[2712.84 → 2714.54] top of and what machines are is just
[2714.54 → 2717.32] these VMS that are designed to start
[2717.32 → 2719.14] really fast or designed to stop and
[2719.14 → 2720.80] restart really fast or designed to
[2720.80 → 2722.70] suspend sort of like your laptop does
[2722.70 → 2724.58] when it closes and resume really fast
[2724.58 → 2726.16] when you tell them to and what we
[2726.16 → 2727.70] found is that giving people as
[2727.70 → 2729.50] primitive is actually there's like new
[2729.50 → 2731.06] apps being built that couldn't be built
[2731.06 → 2733.48] before specifically because we went so
[2733.48 → 2736.34] low level and made such a minimal
[2736.34 → 2738.82] abstraction on top of generally like
[2738.82 → 2740.62] Linux kernel features a lot of our
[2740.62 → 2742.52] platform is actually just exposing a
[2742.52 → 2744.58] nice UX around Linux kernel features
[2744.58 → 2746.22] which I think is kind of interesting
[2746.22 → 2747.56] but like you still need to understand
[2747.56 → 2749.14] what they're doing to get the most use
[2749.14 → 2751.68] out of them very cool okay so experience
[2751.68 → 2754.82] the magic of fly and get told the
[2754.82 → 2756.96] secrets of fly because that's what they
[2756.96 → 2758.38] want you to do they want to share all
[2758.38 → 2760.22] the secrets behind the magic of the fly
[2760.22 → 2761.94] cloud the cloud for productive
[2761.94 → 2764.22] developers the cloud for developers who
[2764.22 → 2765.78] ship learn more and get started for
[2765.78 → 2770.48] free at fly.io again fly.io
[2770.48 → 2783.20] I was digging around in dagger verse while
[2783.20 → 2784.46] you were talking about things
[2784.46 → 2787.40] and I didn't you have a shell SDK is
[2787.40 → 2789.86] that like a thing like is that yeah so
[2789.86 → 2792.04] the dagger shell which I'm talking
[2792.04 → 2794.90] about yes so the shell SDK used to be
[2794.90 → 2797.20] a thing I mean okay so let me just like
[2797.20 → 2799.74] unpack a little bit the power of
[2799.74 → 2803.34] dagger one of the qualities of dagger
[2803.34 → 2807.24] is that it puts a GraphQL API it exposes
[2807.24 → 2811.06] a GraphQL API that all SDKs talk to so
[2811.06 → 2812.56] the engine itself which is where the work
[2812.56 → 2814.30] happens and I can think of it like the
[2814.30 → 2816.70] server and the way to interact with it
[2816.70 → 2820.54] is via this GraphQL API the SDKs all they
[2820.54 → 2824.44] do they are GraphQL clients that expose
[2824.44 → 2826.80] all the operations and all the
[2826.80 → 2830.88] resources from the GraphQL API in a
[2830.88 → 2833.34] language specific way with java by the
[2833.34 → 2835.30] way there's a java SDK with its shell
[2835.30 → 2838.46] in this case so if you're able to model
[2838.46 → 2841.26] the interactions with the GraphQL API
[2841.26 → 2843.54] through shell functions it would work
[2843.54 → 2846.12] one of the things that that dagger
[2846.12 → 2848.14] shipped a while ago was the ability to
[2848.14 → 2851.08] mix and match the SDKs right so I can
[2851.08 → 2854.40] use a module that's written in go but my
[2854.40 → 2856.88] apps in python and I can write my
[2856.88 → 2859.54] function on top of it in python and that
[2859.54 → 2863.04] seems like a outcome of everything
[2863.04 → 2865.10] talks to the GraphQL API right like
[2865.10 → 2866.72] everything's just like okay it's like we
[2866.72 → 2868.24] all just talked to an API I don't care how
[2868.24 → 2869.94] you got here if you're doing curl commands
[2869.94 → 2872.80] you can get to this GraphQL do something
[2872.80 → 2875.70] and then the next step is on you to write
[2875.70 → 2877.62] that in whatever language you want that's
[2877.62 → 2878.98] also awesome because it makes it
[2878.98 → 2881.38] accessible for multiple teams working at
[2881.38 → 2883.96] the same startup or enterprise that are
[2883.96 → 2886.44] writing in multiple languages because it
[2886.44 → 2888.10] gets to the point where enterprises want
[2888.10 → 2890.82] to just start making everybody use two
[2890.82 → 2892.40] languages, and you're like dude this
[2892.40 → 2894.50] language does not work for the things
[2894.50 → 2896.40] that you want it to do like I mean it
[2896.40 → 2898.18] can, but it's not the right you know like it
[2898.18 → 2899.12] just gets to the point where you're
[2899.12 → 2901.42] using a hammer for every project and
[2901.42 → 2902.46] when they want to optimize
[2902.46 → 2904.16] shareability right, and they're just like
[2904.16 → 2907.10] hey by making everyone write Kotlin
[2907.10 → 2909.32] then everything's going to go smoother
[2909.32 → 2910.84] don't lie it's usually a typescript we
[2910.84 → 2912.96] all know like it is typescript yeah but
[2912.96 → 2914.32] it's its you know it goes to the two
[2914.32 → 2915.58] languages right like everything front
[2915.58 → 2917.08] and you know that and maybe some back
[2917.08 → 2918.18] in Scotland or something like that it's
[2918.18 → 2919.54] just like okay everyone writes these
[2919.54 → 2920.72] languages now because we have to be
[2920.72 → 2921.94] able to share this stuff, and we have
[2921.94 → 2923.90] this DevOps team over in the corner and
[2923.90 → 2925.52] they're out there writing YAML and
[2925.52 → 2926.50] they're like well I'm just going to plug in
[2926.50 → 2927.72] this YAML thing it's like the team's
[2927.72 → 2930.16] like no I don't want that but the if is
[2930.16 → 2932.44] the Kotlin team is writing a dagger
[2932.44 → 2934.80] module and the typescript team wants
[2934.80 → 2937.86] to also use that module they can because
[2937.86 → 2940.14] you just said our lowest common denominator
[2940.14 → 2943.08] is the API if you can call the API i
[2943.08 → 2944.52] really don't care what language you call
[2944.52 → 2946.62] it in we're going to give you the same
[2946.62 → 2949.20] functions, and you can every language has
[2949.20 → 2952.26] a way to call a web socket or some
[2952.26 → 2954.00] way to like to call an API somewhere that's
[2954.00 → 2955.98] external and say like here's data give me
[2955.98 → 2958.58] back something you're enabling the dev team
[2958.58 → 2960.70] to do it in the language they're more
[2960.70 → 2962.70] comfortable with right, and you're allowing
[2962.70 → 2966.24] them to fit it into whatever they've already
[2966.24 → 2968.54] built which means that you're not trying to
[2968.54 → 2971.42] completely um this is what I'm looking for
[2971.42 → 2973.24] like there's so many times when they're just
[2973.24 → 2975.70] like go restructure all this code to fit this
[2975.70 → 2978.20] one API, and then you break six things it
[2978.20 → 2980.74] doesn't work right like you know like it any
[2980.74 → 2982.78] way that you can make your life easier without
[2982.78 → 2986.38] having to do like a huge restructure is enabling
[2986.38 → 2988.28] enforcing are kind of the same thing right
[2988.28 → 2990.14] because not all dev teams want this they're
[2990.14 → 2991.70] like actually I just liked it when the external
[2991.70 → 2993.52] team was responsible for the thing and when
[2993.52 → 2995.22] it broke I just emailed them and I went
[2995.22 → 2997.56] to lunch right like that was how a
[2997.56 → 2999.92] lot of devs liked it, and it's true but in this
[2999.92 → 3002.16] time when we're having we have less resources
[3002.16 → 3003.58] and we're trying to do less with more
[3003.58 → 3006.52] I don't know if people are going to always have a
[3006.52 → 3008.04] whole nother team you know what I mean like
[3008.04 → 3009.94] think about the restructuring of enterprises
[3009.94 → 3011.98] and just the fact of what you have to work lean
[3011.98 → 3015.12] with a startup you may not have the option to
[3015.12 → 3016.78] have that whole other team like there's a reason
[3016.78 → 3021.50] why cloud services and managed products and SAS
[3021.50 → 3023.72] products people pay so much money for it because
[3023.72 → 3026.68] it got rid of your DBA it got rid of parts of
[3026.68 → 3028.62] your ops teams, and you could have a smaller op
[3028.62 → 3030.78] team because at the end of the day people want
[3030.78 → 3033.00] us to do all the things with the least amount of
[3033.00 → 3035.92] resources, and you know I mean and I would also
[3035.92 → 3037.92] say like if you went to RDS and got rid of your
[3037.92 → 3040.48] DBA you made a mistake right like that's not
[3040.48 → 3043.22] it's not necessarily the thing you thought it was
[3043.22 → 3045.58] going to be I also think that these things evolve
[3045.58 → 3048.48] right so like instead of needing a DBA now a lot
[3048.48 → 3052.28] of people need data architects right so like maybe
[3052.28 → 3054.32] you don't need somebody running around a data centre
[3054.32 → 3057.78] like in doing the DBA in the traditional sense but
[3057.78 → 3060.62] just because you got rid of a DBA you need a data
[3060.62 → 3062.94] architect to now tell you how to like to do your access
[3062.94 → 3065.52] patterns and how to optimize your database but
[3065.52 → 3068.44] one is easier to contract and one you need every day
[3068.44 → 3071.10] like so it's just it's their all trade-offs
[3071.10 → 3074.88] right like they're it's all like what works for your
[3074.88 → 3076.96] business and what works for your use case
[3076.96 → 3079.88] but I think the problem that we have is that people
[3079.88 → 3082.76] don't know enough about the differences and we just
[3082.76 → 3085.04] tell them like it's this new shiny thing so they don't
[3085.04 → 3087.36] they're not enabled with the right information to make
[3087.36 → 3090.58] those decisions they both have value but what has the
[3090.58 → 3092.14] most value for what you're trying to do
[3092.14 → 3095.72] you know a lot of that also to me at least in my experience has been all
[3095.72 → 3102.08] people that were going after promotions, and you see bigger you know you like hey
[3102.08 → 3104.58] guess what I'm going to rewrite all of our make files and dagger
[3104.58 → 3108.92] and it's going to have impact on the business and someone else over here like but why
[3108.92 → 3111.32] didn't you learn why we had the make files in the first place like why
[3111.32 → 3114.20] didn't you learn he's like that's hard right like that that side of the
[3114.20 → 3117.60] business is a lot harder and also never get you a promotion I guess we're like i
[3117.60 → 3122.50] understand make now has never been on the promo doc for like any engineer yeah
[3122.50 → 3128.24] I would not recommend that by the way if you have a make file what I would
[3128.24 → 3133.18] say don't rewrite it in dagger try running it in dagger first that would be a much
[3133.18 → 3139.86] smarter first step and always focus on documentation first ship it episode 44
[3139.86 → 3145.14] can you say that louder like because I think people think that automation means we
[3145.14 → 3149.48] no longer have to document things, and it hurts my entire soul so badly
[3149.48 → 3156.18] automation is not documentation I'm going to emphasize this in a couple of ways
[3156.18 → 3161.52] first uh ship it episode 44 was a very important moment in my career
[3161.52 → 3168.06] when um we sat down with Kelsey, and we went through all the things that are
[3168.06 → 3170.76] important for understanding how complex systems work
[3170.76 → 3176.46] and documentation is the first step that you should do before you touch before
[3176.46 → 3181.62] you even think about automation because when you document you realize about all
[3181.62 → 3187.50] the inefficiencies, and you realize that if you were to change your automation at
[3187.50 → 3193.06] any point as back to your um what you're mentioning Justin make file rewriting that
[3193.06 → 3197.96] in dagger what you really want is the blueprint for the make file and the
[3197.96 → 3203.62] blueprint is the document that you don't have I was one of those people I remember
[3203.62 → 3209.48] Daniel editor I will not forget him we were on the rabbit me together, and he was
[3209.48 → 3213.52] asking me for the documentation I said hey Daniel you don't need documentation i
[3213.52 → 3218.48] wrote this beautiful make file it does everything for you, it's self-documenting it
[3218.48 → 3222.94] tells you what the targets are what do you mean where's the documentation this is the
[3222.94 → 3229.42] documentation and um it took me many years to understand how wrong I was in that
[3229.42 → 3236.50] moment and I did it right so when I joined dagger one of the first things which I did
[3236.50 → 3243.12] I made sure that the releasing process is documented so how we released dagger we
[3243.12 → 3249.14] started with a document that document has been updated almost every other week for the
[3249.14 → 3255.68] last three years and that is the blueprint which we use for all the automation at dagger
[3255.68 → 3262.00] that makes my heart so happy releasing MD so I've learned my lesson and I hope that you will too
[3262.00 → 3269.80] dear listener write the documentation first keep it up to date it keeps refining it keep working on it
[3269.80 → 3276.74] keep sharing it's not done it's never done and then add your automation did you guys hear him like
[3276.74 → 3284.70] just replay I just yes because like it blows my mind like and then people like so you know how you
[3284.70 → 3290.30] were saying like well people want to do that for promotion where they rewrite everything or people
[3290.30 → 3294.60] are like we've been doing it in bash the same way for 20 years, and we're never going to change
[3294.60 → 3300.50] anything and there are so many new ways to do it but let's just do it this way forever, and you're like
[3300.50 → 3307.22] not that like I do sometimes think if it's really simple bash sometimes is just the way to go right
[3307.22 → 3313.08] but like never thinking about how you can onboard new people and share knowledge and make it easier
[3313.08 → 3320.02] for everybody like you're just doing the same thing forever and the comments aren't docs too right like
[3320.02 → 3322.90] that's the thing that a lot of developers like well it has a bunch of comments we know no, no no
[3322.90 → 3328.46] you pull those out somewhere else you make it searchable for someone else that isn't in the code to be
[3328.46 → 3333.18] able to find I've had people tell me not to put comments though because it is the script is self
[3333.18 → 3338.90] explanatory no they'll be like it the automation is explanatory if you write it clean enough and I'm
[3338.90 → 3345.84] like no, no it's not years ago yeah yeah i know now I'm just like when you're new, and you've
[3345.84 → 3352.34] never seen this before it's not self-explanatory like every job I've worked at the docs I've written
[3352.34 → 3357.32] have lasted longer than the code I've written and like if you want to like to do the lasting impact like
[3357.32 → 3361.84] the docs are the thing that's, but we don't incentivize docs we incentivize yeah that's what
[3361.84 → 3366.88] I'm saying so like, and it's just it doesn't make sense because like what is the number one rule
[3366.88 → 3372.22] in school or wherever when they when you learn to code what do they always say write it down plan it
[3372.22 → 3376.36] out, and then you start coding but I don't know where we missed that with automation we were just
[3376.36 → 3381.08] like oh but like that's only for code not for scripting or anything else that's important or release
[3381.08 → 3386.64] processes when dude release processes and scripting and like doing the infrastructure usually takes
[3386.64 → 3390.84] longer than writing the code that you want to release so like why would you not do your due
[3390.84 → 3395.70] diligence to make sure well I mean let's be honest the meetings about writing the code take oh god
[3395.70 → 3400.66] yes like you know, but that's what just like kills me when they're just like engineers just need to be
[3400.66 → 3405.18] able to write perfect code and be technical and I'm like that is such a small part of being a good
[3405.18 → 3410.62] engineer a lot of people that are afraid of AI being able to write code is like you're just looking at
[3410.62 → 3416.38] just a small part of what the engineers are doing those are the parts that we incentivize and
[3416.38 → 3423.32] reward to be this 10x developer who can write and build things superfast but like who else who
[3423.32 → 3427.58] like but think about those are the people that job hop every two years and somebody else has to go fix
[3427.58 → 3434.02] the like 10x developer stuff that you put together and duct taped it nobody knows what it does nobody's
[3434.02 → 3439.04] documented, and you're ruining someone else's on-call life Adam you could just drop names if you want this is
[3439.04 → 3446.54] I was a little triggered for a minute there like I'm so tired of tech bros
[3446.54 → 3455.46] so where do you think this goes Gerhard like what is the end goal here for something like
[3455.46 → 3462.40] dagger something that is making this an i I feel like dagger is the productized make right
[3462.40 → 3468.58] if i erased everything and said what if this was a perfect product, and we put it in here and
[3468.58 → 3474.54] we gave them good experience and good tools and good UI around this thing that is kind of opaque and
[3474.54 → 3479.76] always been weird that one or two people on the team understand even remotely like let's just make it so
[3479.76 → 3484.02] it's easier for everyone to understand let's make it so it's a thing that's maintainable is shareable
[3484.02 → 3489.50] is scalable what's the end goal there what's the thing that you're at the end of it like oh if we get
[3489.50 → 3495.14] here we've made it you just made me think of like the difference between VMS and the cloud dagger is
[3495.14 → 3506.38] like the make file for like well remember what containers did for applications that is the moment
[3506.38 → 3513.44] that I envisage for all the scripts that we write that moment for all the automation that you write
[3513.44 → 3521.66] the container moment for all those things where we agree to put this these things in containers first
[3521.66 → 3529.30] in a way that's immutable in a way that's content addressable and if we do that if this grows to a
[3529.30 → 3537.00] certain point we are no longer writing automation the automation knows how to consume the resources
[3537.00 → 3543.04] that others have built without us having to go and figure out how to plug them together for example
[3543.04 → 3551.76] how many times have you gone to download the package checked or like a tarball unzipped it check the
[3551.76 → 3560.46] SHA 256 make sure it's okay make sure read at the change log read what changed figure out how like what
[3560.46 → 3567.16] things have deprecated all of that times a thousand in your career you will have done this a thousand
[3567.16 → 3576.20] times at least you're giving me PTSD of like flashbacks like is there a better way that I can
[3576.20 → 3581.42] consume these things I can run it I can validate that my software works whatever I'm trying to do
[3581.42 → 3589.50] it combines well with all these things in a way that is just friendlier you have got like a whole
[3589.50 → 3595.94] new experience of consuming software of building of distributing of doing anything that
[3595.94 → 3602.04] you have to do with your source code before it gets out in front of people encapsulating all that
[3602.04 → 3606.94] knowledge encapsulating all that knowledge in a way that is also documented right because coming back to
[3606.94 → 3613.04] documentation you don't document things, but maybe you're willing to document your argument maybe you're
[3613.04 → 3617.36] willing to document your function and explain how this function should be used and how it can be
[3617.36 → 3623.16] interacted and your function is a very small piece the world now gets to use because you're
[3623.16 → 3628.58] passionate about java, and you know how to build java apps and to package containers well can you just
[3628.58 → 3634.48] go on a speaking tour about documentation and automation because like I feel like you could fix the world
[3634.48 → 3641.32] one doc at a time one doc at a time yes, yes do you feel like there are any mistakes we're going to make
[3641.32 → 3646.30] again I feel like there's uh as much as containers have done well there are a lot of things that
[3646.30 → 3651.20] containers haven't done well for application packaging and sharing do you feel like there's
[3651.20 → 3656.78] something in there that's like this maybe this is in general like not dagger specifically but maybe
[3656.78 → 3662.02] this like process of like this writing code doing a bunch of stuff to it and then like spitting it out
[3662.02 → 3667.18] packaging it sending it somewhere else maybe that's the problem I think the problem is that the ambition
[3667.18 → 3674.20] is too big, and we don't get to capture it in practice well enough so if we disconnect it too much
[3674.20 → 3679.78] from reality if we talk about these hypotheticals without you know having something real to back
[3679.78 → 3687.60] them up everything will just not go where it needs to go because there's too much air in the balloon, and it will
[3687.60 → 3693.72] pop and the balloon is just, just air that's it that is my fear I think with every technology
[3693.72 → 3701.76] you tend to get that also you start getting um competition you know players that maybe they
[3701.76 → 3707.62] dominate the market, but maybe they're not the right solution for the problem, but they're the
[3707.62 → 3714.96] they're the know the big gorilla the 800 pound gorilla in the ring and everyone gravitates towards
[3714.96 → 3719.64] them because they have a monopoly on the market and everyone talks about that, and then you get like
[3719.64 → 3728.60] some huge acquisitions and everything goes sideways so i think there is a real risk of not
[3728.60 → 3738.54] keeping it rooted in reality going too far out in hypotheticals and maybe not dealing enough with
[3738.54 → 3744.30] like the little paper cuts because there are a lot of paper cuts, and we try addressing them so many paper cuts
[3744.30 → 3750.02] yeah and now I'm talking about dagger specifically, but you're right even in general like in the
[3750.02 → 3755.50] software industry there's like so much stuff which is broken and I think you need some of that because
[3755.50 → 3759.60] it is a form of technical debt right you need to innovate at the same time but if it's too broken
[3759.60 → 3766.84] that's a problem so one of the challenges that we have or that something which I've taken upon myself
[3766.84 → 3772.66] and if you want to read more about it, you can go to dagger issue 8184 and guess how I know it off the top
[3772.66 → 3781.08] of my head because I've been on it for months now is how dagger uses dagger at scale what does that mean
[3781.08 → 3791.54] the scale that I'm talking about when our pipeline runs we are spinning up maybe up to 10 15 large
[3791.54 → 3800.76] instances on ec2 that sum up about 500 CPUs to run the pipelines all the pipelines for dagger if you have
[3800.76 → 3806.08] five or six pull requests happening at the same time you have thousands of CPUs being spun up
[3806.08 → 3813.86] to test various things dagger that costs real money that is a hard problem the less reliable your
[3813.86 → 3820.14] pipeline is and the longer it takes to run the higher the pain the higher the waste and that is a
[3820.14 → 3826.16] hard problem every single team will have this at some point if they're successful we are getting there
[3826.16 → 3832.92] we are looking at our AWS bill, and we're thinking wow this is expensive really, really expensive what
[3832.92 → 3839.46] can we do and there are certain ways in which we use dagger which we need to bust the cache we need to
[3839.46 → 3847.46] do certain things at which point are containers the right way of doing this that comes up what are what
[3847.46 → 3854.28] is the overhead of using overlay FS what is the overhead on the disks what is the overhead on the
[3854.28 → 3860.04] networks of pulling all these bits down what is the overhead of having to recompute the same thing
[3860.04 → 3865.66] when you don't have a distributed cache, so there are some hard problems there they're fun to solve
[3865.66 → 3873.26] and this can either be a great success or the biggest lesson of my life and I will accept them both
[3873.26 → 3880.76] with equal joy to my heart I think you make a point there too like i I did a calculation for my
[3880.76 → 3886.80] local developer desktop which is like an AMD thread ripper versus something comparable at Amazon
[3886.80 → 3894.36] and when I look at the machine that I built out of parts basically uh cost around 600
[3894.36 → 3900.16] something dollars and like to get something to AWS it was 101 times more expensive like not 10 times
[3900.16 → 3904.60] like for a is consumer grade not ECC ram it's not all that stuff like I don't need that
[3904.60 → 3908.38] for some of these things right like I'm doing local like development and testing like I don't need
[3908.38 → 3912.08] ECC I don't need all this stuff and when you have something as portable as dagger it makes a lot more
[3912.08 → 3917.44] sense to like hey maybe actually just a couple of these pcs that don't have all the benefits that
[3917.44 → 3922.30] we don't actually need could save us a lot of money and even if they're not used because if people
[3922.30 → 3925.38] say like oh it's wasted right you're not using it all the time like doesn't actually matter
[3925.38 → 3930.50] when it's a hundred times cheaper I could use it one hundredth of the time and still save money
[3930.50 → 3936.86] out of it right like that that math works out so just be like oh maybe a pile of build machines just
[3936.86 → 3941.68] sometimes does make sense I think that's fascinating how sometimes it does make sense but sometimes you
[3941.68 → 3946.60] also have to remember that if you're using it, and you're not just playing around with it, and you need
[3946.60 → 3951.62] it to be reliable you have to replace it you have to maintain it, and you have to have people that have
[3951.62 → 3956.48] the knowledge to do it so I mean people build you know see like the I have terraformed code and all
[3956.48 → 3960.46] other stuff in the cloud too like all that stuff needs to be maintained and done and so it's not
[3960.46 → 3966.48] free either way like they're not free either way but like I think that we went so hard on the cloud
[3966.48 → 3972.40] we went so all in, and it was the answer for everything but now our attitude is automatically that
[3972.40 → 3977.06] we don't need the cloud and everything can be done on-prem and neither of those are correct like
[3977.06 → 3981.82] there 's is a use case and there is a time for both, and you have to figure out what works best
[3981.82 → 3986.06] and what is most cost-efficient and sometimes one works for a while, and then you grow too fast and
[3986.06 → 3992.18] you need to do the other but I do think that it's a disservice to pretend like one size fits all and
[3992.18 → 3997.26] we can do everything on-prem we can like no yeah absolutely if that was the case we'd still be
[3997.26 → 4003.92] running servers in our grandma's basement you know I mean I still am it's your basement now but you
[4003.92 → 4009.30] know what I mean what you use for fun and what you use to maintain I don't know a huge enterprise
[4009.30 → 4014.48] are two completely different things and like it's funny because like there's so many companies talking
[4014.48 → 4019.48] about how they run on-prem right now, but they're essentially building their own cloud that someone
[4019.48 → 4024.08] else is maintaining it's a little bit cheaper, but they're not really truly running on-prem like
[4024.08 → 4030.32] they're sending their hardware to someone else to run so it's like another iteration of the cloud
[4030.32 → 4035.90] almost you know what I mean it's not all AWS in all computers in my garage there's like this mix
[4035.90 → 4039.94] of like oh there's solos I can rent some things temporarily I can get bare metal places like
[4039.94 → 4045.56] that's what I'm saying so it's still a's almost an iteration of like the cloud and hardware and on-prem
[4045.56 → 4051.26] and we're in this weird place that I think because everybody is trying to save money and figure out how
[4051.26 → 4056.52] we do things differently that like people are almost scrambling, and it's going to be interesting to see
[4056.52 → 4061.90] what actually saves people money and time and is good for their use case or if they end up down a
[4061.90 → 4067.72] whole nother rabbit hole but I think we just like it's a disservice to pretend like they are all the
[4067.72 → 4071.86] same thing and that you are not essentially using a different type of cloud you're just using a
[4071.86 → 4077.62] private cloud if we remove the word cloud like in gear it's like it's just VMS that's what I'm saying
[4077.62 → 4083.32] they're all VMS and so my point was the fact that dagger is a new tool because the downside of having
[4083.32 → 4089.14] on-prem build machines which I've had in plenty of jobs is always the maintenance cost of like oh
[4089.14 → 4093.58] someone tweaked something and now I don't know what broke right but the dagger encapsulation
[4093.58 → 4099.68] of these jobs of saying hey actually this should run anywhere as long as this engine exists and
[4099.68 → 4105.72] now we can encapsulate that holistically and not rely on the base OS as much or the version of it and
[4105.72 → 4109.72] you even we started the conversation you were saying how like the kernel matters in a lot of these
[4109.72 → 4115.26] cases too and so there are some things that aren't generically possible across the board there is
[4115.26 → 4121.42] still some maintenance cost there but for the most part like dagger should run more portably than my
[4121.42 → 4125.74] make file that is doing bash scripts right like that side of it is like oh now I have that flexibility
[4125.74 → 4131.84] to make the decision of where do I want to run this how should I run this where is cheap compute
[4131.84 → 4137.26] available right like I could do spot instances to lower that price or if I have some extra computers in
[4137.26 → 4141.40] the closet I could just plug them in and do that too like there are options there because
[4141.40 → 4147.88] of the portability that you're building into the tool and I don't lose out on the benefits that i
[4147.88 → 4152.92] might get for something that's like hey I'm doing a VM in AWS I need logs from it oh cool those are just
[4152.92 → 4157.24] in cloud watch logs and in this case like no we're all talking to an API where you get the tracing
[4157.24 → 4162.98] by default uh by using this dagger cloud or by using you get the logs you get the stuff out of it like
[4162.98 → 4167.06] that's why I think there's so much gravity around get have actions because get have actions is just
[4167.06 → 4170.92] like we give you a bunch of these defaults, but it's not portable it's not something that is easy
[4170.92 → 4174.84] to move around and decide I don't want to run this here anymore I think that's going to be the
[4174.84 → 4180.34] startups that really like that become the next big tech companies that are going to really benefit from
[4180.34 → 4185.38] this weird sunken place of tech that we're in where everyone's trying to like to make as much money with
[4185.38 → 4191.32] the least amount of what they have is like the startups that allow you to lift and shift and to be
[4191.32 → 4198.32] portable and to be is kind of like into monitor and uh like to monitor all your different clouds
[4198.32 → 4202.86] all your different instances and all what you're running like whatever gives you that portability
[4202.86 → 4207.94] and that observability and monitoring into all the different things because everybody wants to do hybrid
[4207.94 → 4213.48] cloud all the different regulations coming or the fact that now one cloud or one way to do it or
[4213.48 → 4216.98] on-prem is cheaper, and they want to lift off of this thing and go to this thing like all the things
[4216.98 → 4222.44] that are going to make software more portable and easier to switch are going to be what really
[4222.44 → 4229.40] expands and like just hits right now and that's where I think dagger fits perfectly of we could
[4229.40 → 4234.64] say we could run this anywhere the portability of I can, I can't write code anywhere or like I need a
[4234.64 → 4240.40] developer machine like I need something that has some tooling locally in all the web-based
[4240.40 → 4245.52] development tools and whatnot like I've tried all of them I've never stuck with any of them because
[4245.52 → 4249.84] they always had some limitation for me, or they ended up being really expensive and I'm like actually
[4249.84 → 4253.94] I already paid for this computer I could use the computer and pay myself the maintenance cost of
[4253.94 → 4258.12] making sure this thing runs and on the other end is like well we have these containers we can package
[4258.12 → 4261.22] them we have this cooper and anything which can run everywhere we're like we have all these things
[4261.22 → 4265.28] that like at the other end we can have the portability but in the middle there between writing
[4265.28 → 4271.24] the code and deploying the code somewhere in that build pipeline the CCD stuff was always super sticky
[4271.24 → 4276.00] and it was super hard to say like I can shift this somewhere I can't lift and shift Jenkins I can
[4276.00 → 4280.18] but like it's a lot of work it's not actually just an endpoint like and you have to just reproduce
[4280.18 → 4285.20] the same thing in a different environments and I think that's really cool about how like you mentioned
[4285.20 → 4289.88] at the beginning right like this is what containers did for applications dagger could do for that CCD
[4289.88 → 4295.58] middle pipeline of this is portable, and we have some options here also when you're scaling like
[4295.58 → 4301.20] release infrastructure what used to work can definitely get to the point where you have too
[4301.20 → 4305.88] many pipelines, and you've grown too much and then having to lift and shift that is the most painful
[4305.88 → 4311.88] in the whole world I mean and that's that's a unique problem to a lot of like not all companies
[4311.88 → 4316.20] have that problem like Amazon had that problem that was a that was definitely an Amazon there's a lot
[4316.20 → 4321.40] of pipelines here um to make things safe and roll out and all that stuff but not everyone requires
[4321.40 → 4326.76] that amount but also when you're building stuff for different architectures too being able to lift
[4326.76 → 4331.76] and shift them to different things because what might work on Mac might not work on Windows and what
[4331.76 → 4337.64] you know what I mean so just being able to see if this really does work in that architecture natively
[4337.64 → 4343.66] is really important yeah one thing that we talked about previously I thought that was a really important
[4343.66 → 4350.16] point was around what makes a good developer what would say go further what makes a good
[4350.16 → 4355.92] engineer a good software engineer, and it is not the documentation even though that plays a very
[4355.92 → 4361.92] important role it is not the code that they write even though that has to be present it is not how they
[4361.92 → 4367.12] present and how they talk, but again that has to be present how they share ideas you know how they
[4367.12 → 4374.14] show into the world and do whatever they have to do those are well-rounded individuals and that
[4374.14 → 4381.28] well-roundedness I can see how it translates to whether it's the cloud whether it's the on-prem whatever
[4381.28 → 4387.00] the next thing is you need to be well-rounded in all these things and you should be using all of them
[4387.00 → 4394.78] because if you don't use it you lose it right very simple very true it will never change so you should be
[4394.78 → 4400.78] using the cloud but you should be using the cloud the way the cloud was meant to be used and you Justin
[4400.78 → 4406.72] made a very good point at Disney how you were using the cloud possibly the best example of using the
[4406.72 → 4415.94] cloud correctly right span out stand up all these instances and then tear them down that's how it's
[4415.94 → 4420.56] supposed to be used right its capacity on demand massive capacity you would not want to buy that
[4420.56 → 4426.36] but when you need it, it's there and it's a great commodity it is a hundred times more expensive
[4426.36 → 4431.74] because that's what this commodity costs you where else can you turn up and say hey spin up a hundred
[4431.74 → 4436.90] beef instances that wouldn't take months would take maybe years to source all of those things
[4436.90 → 4442.68] and by the way no, no I don't want that AMD CPU I want that intel CPU oh arm I think I'm going to
[4442.68 → 4448.74] have some arm and by the way I'm going to have I know 10 000 arm CPUs where can you get that is the
[4448.74 → 4454.78] convenience of that now if you know what you need right as a business that is successful as a
[4454.78 → 4459.82] startup that's successful well for the things that you know that you definitely need and that's like
[4459.82 → 4466.48] your baseline operating budget in terms of infrastructure have that in a place that makes
[4466.48 → 4473.26] sense have that cheap has that you know cheap I say cost-efficient do what makes sense hybrid cloud
[4473.26 → 4480.40] what about Wasm what about the was runtimes how do they change how we see containers and how we work
[4480.40 → 4487.62] with containers is that coming well I can tell you that react did not work for dagger cloud
[4487.62 → 4492.58] react the Dom to generate all the things that we had to generate was just breaking down
[4492.58 → 4500.02] the tech was not up to scratch so what did we do we looked at Wasm v3 that's the v3 cloud we went
[4500.02 → 4506.34] through three rewrites to get it to a point where it's as performant as it should be and there's so
[4506.34 → 4511.06] many dragons there like don't think that this is like the holy place where you pick it up and
[4511.06 → 4516.72] everything is awesome oh no the cycle starts again but that's it that's the beauty of it start those
[4516.72 → 4522.98] cycles keep going through them keep learning keep iterating eventually you will be able to consider
[4522.98 → 4528.54] yourself well-rounded and others will look at you and say wow I wish he responded to my pull requests
[4528.54 → 4534.72] I wish he left some comments and did some reviews because I like his reviews I wish he blogged more
[4534.72 → 4542.46] or I wish she went and gave some talks because she's an excellent presenter so look for well-rounded
[4542.46 → 4548.84] not for 10x I think that's a great place to end the uh end the episode and uh Gerard again thank you
[4548.84 → 4554.04] so much for starting this podcast for putting it out there as a place that people can learn
[4554.04 → 4559.22] and just get access to someone that they may not be able to approach and have a conversation with
[4559.22 → 4564.34] and then learn from their insights on all the cycles and failures that they've had from the past and
[4564.34 → 4568.16] the things they've learned and then the things they want to share about that um that's what we
[4568.16 → 4572.70] are trying to continue that's the things that we're like not just having cool people on with
[4572.70 → 4576.70] exciting conversations which we do like but really just being able to help people be a little more
[4576.70 → 4581.70] well-rounded about actually that database is important and actually the CCD is important and
[4581.70 → 4588.30] all the things that go around the code and uh the businesses responsible for matters and how do we
[4588.30 → 4593.78] help them be more responsible and help the people that run them understand them so thank you so much
[4593.78 → 4598.54] and I truly think people don't talk about that part enough like that's the information that people
[4598.54 → 4603.50] need because we don't reward it right but like it's so true though like you can't have any of
[4603.50 → 4607.78] these cool things without the database or without the infrastructure without all of these things so i
[4607.78 → 4613.32] just think that like it brings me like nerdy joy to expose people to things that they may not
[4613.32 → 4619.26] have been exposed to and to have people who do that every day tell them like the caveats or what they
[4619.26 → 4623.62] tried and what they hated and where they failed and what they succeeded at you know where should
[4623.62 → 4629.14] people find you online if they want to reach out continue the conversation gerhardt.io that's a good
[4629.14 → 4639.06] place there's this new space which now it has a domain make it work.fm and make it work.tv
[4639.06 → 4647.30] the way I think of it is movies for nerds. Come to blue sky so we can like to bug you. I am I have to
[4647.30 → 4653.58] start using it I am there but I have to start using it because I there are too many social places
[4653.58 → 4659.10] and there are so many things to do that's I think the one area in which I'm not as well-rounded as i
[4659.10 → 4664.84] could be more present on the social media. I think blue sky is becoming where everybody seems
[4664.84 → 4669.24] to be going I'm really hoping that it sticks because I can't manage all these social media
[4669.24 → 4674.26] platforms. yeah, I mean there's a lot i I'm hoping blue sky succeeds only for the fact that
[4674.26 → 4679.78] it will encourage people to hopefully make their own websites like I think that's the true mission
[4679.78 → 4684.56] and purpose of blue sky is to make the internet be more democratized and people just understand
[4684.56 → 4690.60] I should be able to own and run this data wherever I want and then publish my own content and own a
[4690.60 → 4696.10] domain like that stuff is super important to me and it's not just another centralization of
[4696.10 → 4700.88] hey we're the new search engine we're the new social media thing it's like everyone come here
[4700.88 → 4706.30] it's like no actually how everyone interacts together and builds on top of what other people
[4706.30 → 4711.72] are doing in a democratized way I think is very critical for the internet to succeed long term.
[4712.56 → 4717.94] I like that it has the ease of other social mediae, but it does like you said force you to like
[4717.94 → 4723.54] but not just force you, but you get to keep what you're investing in you know the data your
[4723.54 → 4728.22] content. You can't see it I'm running a PDS on my Raspberry Pi back here behind me, and so I have a
[4728.22 → 4732.28] user that's on blue sky that's literally reporting back here I already made a video about it is'll be
[4732.28 → 4738.62] posted soon I'm waiting for blue sky to cool down. Come get your nephews and teach them how to run
[4738.62 → 4743.72] stuff on Raspberry Pi because I've there are too many things to do and I don't have time to figure this
[4743.72 → 4747.20] out, and they keep bugging me come get them. We will have someone from blue sky infrastructure
[4747.20 → 4752.18] on the podcast soon they're dealing with all sorts of scaling a million people every day for the past
[4752.18 → 4756.90] few days so I'm I'm waiting to post my video because I was talking to them, I'm like hey would
[4756.90 → 4761.36] this be a problem for you if everyone started doing this like yeah actually please wait just wait a week
[4761.36 → 4765.48] and we'll be fine but yeah we're going to have them on the show soon because I'm fascinated to learn
[4765.48 → 4769.96] about their scaling journey for the last couple of weeks and months. They've done a great job and also
[4769.96 → 4775.52] they've done a great job on print. yeah, question for you Justin would it work in Kubernetes PDS?
[4776.24 → 4780.82] yeah I mean it's just it's an it's a web server with a SQLite database. Amazing. That's all it is.
[4781.06 → 4784.92] amazing. It's just you know it's like a git tree in SQLite and that's all it is, and it's just like
[4784.92 → 4789.78] yeah if you can publish that somewhere it's that's that's one of the things I think is really cool about
[4789.78 → 4795.52] blue sky's self-owned sort of federation versus mastodon where the mastodon scale-up story was a lot
[4795.52 → 4799.12] more difficult where like you need Postgres you have a Ruby on Rails app you need cash.
[4799.12 → 4804.78] I just can't commit to that type of like it's not that I hate mastodon I just can't commit to that
[4804.78 → 4810.10] type of overhead for social media like I have so many things to do. And the PDS is just a's
[4810.10 → 4813.56] it actually they deploy it in a container it's like if you have a Debian thing it's already packaged in
[4813.56 → 4819.14] a container you just want some way to have some uh you know reliable storage underneath so
[4819.14 → 4823.80] that your SQLite database is always available and backed up but otherwise yeah it's fascinating I've
[4823.80 → 4828.22] already run a few of them um I did a live stream a little while ago but yeah I'm still toying with it
[4828.22 → 4831.94] and figuring out like how does this thing work how would someone want to own this going forward
[4831.94 → 4838.10] because more things are being built on this sort of protocol and personal storage versus app tier
[4838.10 → 4843.20] scraper sort of thing, or it's like app tier is the search engine and I have a website and how does that
[4843.20 → 4847.56] interact speaking of that I need to go fix my website why can't you just fix my GitHub pages because you
[4847.56 → 4855.82] obviously like enjoy messing with DNS more than I do and like I love DNS I hate it so much I hate it
[4855.82 → 4863.02] so much like uh thank you everyone for listening um please reach out uh online to us if you have
[4863.02 → 4869.08] uh suggestions for a show title that we can continue going forward um and we will hopefully have
[4869.08 → 4873.92] something for you in a couple of weeks on where you can find us going forward for next year for 2025
[4873.92 → 4878.86] and we will talk to you all again soon I feel like gear heart has to come back for like our new
[4878.86 → 4885.26] podcast oh yeah I would be happy to good luck it was so nice meeting you too I think you've done
[4885.26 → 4891.10] an excellent job with these episodes I think it was a very nice transition, and it's great that you're
[4891.10 → 4897.38] able to carry the torch the spirit continue the spirit of ship it I think people appreciated that
[4897.38 → 4902.14] and I'm looking forward to what you'll do next I'm really excited I feel like this can be the
[4902.14 → 4908.30] new iteration of ship if it's a little scary though thank you see you next time
[4908.88 → 4920.02] thanks for listening to ship it with Justin garrison and autumn Nash if you haven't checked
[4920.02 → 4927.10] out our changelog newsletter do yourself a favour and head to changelog.com slash news there you'll find
[4927.10 → 4934.30] 29 reasons yes 29 reasons why you should subscribe I'll tell you reason number 17 you might actually
[4934.30 → 4940.08] start looking forward to Mondays sounds like somebody's got a case of the Mondays 28 more
[4940.08 → 4947.34] reasons are waiting for you at changelog.com slash news thanks again to our partners at fly.io over
[4947.34 → 4953.84] 3 million apps have launched on fly, and you can too in five minutes or less learn more at fly.io
[4953.84 → 4959.50] and thanks of course to our beat freak in residence we couldn't bump the best beats in the biz without
[4959.50 → 4964.64] break master cylinder that's all for now but come back next week when we continue discussing
[4964.64 → 4967.14] everything that happens after get push
[4967.14 → 4975.86] everything So
[4975.86 → 4978.22] I love you
[4978.22 → 4982.78] you
