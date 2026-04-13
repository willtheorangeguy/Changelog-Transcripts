[0.00 → 2.56] Hello friends, Jared here, Go Times producer.
[2.96 → 5.16] This week we're doing another classic
[5.16 → 6.44] from the back catalogue.
[6.96 → 9.26] One common request we get from listeners
[9.26 → 12.18] is for more beginner level conversations.
[12.72 → 14.90] Well, that's exactly what this episode is.
[15.14 → 17.72] It was originally recorded on May 7th, 2019,
[18.12 → 21.26] back when John Calhoun was merely a guest panellist.
[21.56 → 23.40] We'll be back with some freshens next week.
[23.48 → 25.50] In the pipeline, we have a debugging episode,
[25.74 → 27.28] what's new in Go 1.19,
[27.28 → 30.98] Gophers Say, live from Gopher Con EU and more.
[31.50 → 32.70] Okay, go for beginners.
[33.16 → 33.58] Enjoy.
[38.08 → 40.84] This episode is brought to you by Source graph.
[40.94 → 42.92] With the launch of their Code Insights product,
[43.06 → 45.92] teams can now track what really matters in their code base.
[46.24 → 48.34] Code Insights instantly transforms your code base
[48.34 → 49.96] into a queryable database
[49.96 → 52.54] to create visual dashboards in seconds.
[52.92 → 53.94] And I'm here with Joel Chortler,
[54.16 → 55.98] the product manager of Code Insights for Source graph.
[55.98 → 58.82] Joel, the way teams can use Code Insights
[58.82 → 60.56] seems to pretty much be limitless,
[60.74 → 63.68] but a particular problem every engineering team has
[63.68 → 66.14] is tracking versions of languages or packages.
[66.64 → 69.34] How big of a deal is it actually to track versions for teams?
[69.80 → 71.54] Yeah, it's a big deal for a couple of reasons.
[71.72 → 73.54] The first is, of course, just compatibility.
[73.78 → 75.44] You don't want things to break when you're testing locally
[75.44 → 77.66] or to break on your CI systems or test systems.
[78.04 → 80.40] You need to have some sort of level of version unification
[80.40 → 81.40] and minimum version support,
[81.56 → 84.30] and all of that needs to be compatible forward.
[84.30 → 87.02] But the other thing we learned was that for a lot of customers,
[87.14 → 88.44] especially, you know, engineering organizations
[88.44 → 89.50] that are pretty established,
[89.94 → 91.40] they have older versions of things
[91.40 → 93.32] or even older versions of, like, SaaS tools
[93.32 → 94.08] they don't use anymore
[94.08 → 95.58] that they haven't fully removed
[95.58 → 96.96] because they're, like, not sure if it's still in use
[96.96 → 98.46] or they, you know, lost focus on that.
[98.76 → 100.58] And they're spinning up old virtual machines
[100.58 → 101.58] that they're still paying for.
[101.68 → 103.26] They're using, you know, old SaaS subscriptions
[103.26 → 104.08] they're afraid to cancel
[104.08 → 105.70] because they're not sure if anyone's actually using it.
[105.80 → 107.16] And so getting off of those versions
[107.16 → 108.78] not just, like, saves you the headaches
[108.78 → 109.94] and the risks and the vulnerabilities
[109.94 → 111.22] of being on old versions,
[111.22 → 113.36] but also literally the money of, you know,
[113.42 → 115.06] older systems running more slowly
[115.06 → 115.90] or the build times
[115.90 → 117.36] or, you know, virtual machines
[117.36 → 119.08] and SaaS tools that you're no longer using.
[119.40 → 120.56] Before you had this ability,
[120.66 → 121.28] we talked to teams
[121.28 → 122.96] there were basically three ways you could do this.
[123.24 → 124.50] You could slack a million people
[124.50 → 126.68] and ask for just, like, an update point in time.
[126.94 → 128.46] You could have sort of one human
[128.46 → 129.12] and one spreadsheet
[129.12 → 130.68] where, like, it's somebody's job
[130.68 → 132.02] every Friday or every two weeks
[132.02 → 133.64] to just, like, search all the code
[133.64 → 134.56] and find all the versions
[134.56 → 135.94] and write it down in a Google sheet.
[136.20 → 137.66] Or there were a couple of companies
[137.66 → 139.58] I came across with in-house systems
[139.58 → 140.48] that were sort of complicated.
[140.68 → 142.44] You had to know, you know, maybe Kotlin,
[142.62 → 143.60] but you didn't know Kotlin.
[143.66 → 144.54] But if you wanted to use this system,
[144.58 → 145.30] you had to learn Kotlin
[145.30 → 146.64] and you'd have to sort of build
[146.64 → 147.66] the whole world from scratch
[147.66 → 149.52] and run basically a tool like this
[149.52 → 150.88] with a pretty steep learning curve.
[151.18 → 152.52] And now for all three of those,
[152.56 → 153.26] you could replace it
[153.26 → 155.00] with a single line, Source graph Search,
[155.12 → 156.08] which is basically just
[156.08 → 156.82] the name of the thing
[156.82 → 157.34] you're trying to track
[157.34 → 158.04] and the version string
[158.04 → 158.80] in the right format.
[159.08 → 160.00] And then we have templates
[160.00 → 160.76] that'll help you get started
[160.76 → 161.60] if you're not sure
[161.60 → 162.32] what that format is.
[162.48 → 163.54] And then it'll automatically track
[163.54 → 164.68] all the different versions for you,
[164.86 → 165.58] both historically.
[165.76 → 166.74] So even if you start using it today,
[166.82 → 167.90] you can see your historical patterns.
[167.90 → 169.38] And then, of course, going forward.
[169.96 → 170.64] Very cool. Thank you, Joel.
[170.72 → 172.12] So right now there is
[172.12 → 174.42] a treasure trove of insights
[174.42 → 175.18] just waiting for you.
[175.42 → 178.04] Living inside your code base right now,
[178.32 → 180.10] teams are tracking migrations,
[180.44 → 182.02] adoption, deprecations.
[182.36 → 183.50] They're detecting and tracking
[183.50 → 185.20] versions of languages and packages.
[185.20 → 187.18] They're removing or ensuring
[187.18 → 189.18] the removal of security vulnerabilities.
[189.56 → 191.14] They understand their code by team.
[191.22 → 192.90] They can track their code smells and health
[192.90 → 193.90] and they can visualize configurations
[194.52 → 196.60] and services and so much more
[196.60 → 197.50] with code insights.
[197.90 → 200.18] A good next step is to go to
[200.18 → 202.18] about.sourcegraph.com
[202.18 → 204.10] slash code dash insights.
[204.38 → 205.88] See how other teams are using
[205.88 → 206.90] this awesome feature.
[207.22 → 209.84] Again, about.sourcegraph.com
[209.84 → 211.98] slash code dash insights.
[212.24 → 213.98] This link is in the show notes.
[213.98 → 230.04] Let's do it.
[230.26 → 231.70] It's go time.
[232.26 → 233.94] Welcome to go time,
[234.10 → 235.78] your source for diverse discussions
[235.78 → 237.26] from around the go community.
[237.26 → 240.20] We record live on Tuesdays at 3 p.m.
[240.20 → 240.62] U.S.
[240.68 → 241.08] Eastern.
[241.46 → 243.36] Subscribe at YouTube.com
[243.36 → 245.24] slash changelog to be notified
[245.24 → 247.14] so you can be part of the action.
[247.48 → 249.30] And don't forget to follow the show on Twitter.
[249.46 → 250.72] We're at go time FM.
[250.92 → 252.84] Special thanks to our partners at Vastly.
[253.04 → 255.24] Everything we ship here at Changelog is fast
[255.24 → 257.80] because Vastly serves it up superfast
[257.80 → 258.74] everywhere on Earth.
[258.98 → 261.04] Check them out at fastly.com.
[261.44 → 262.72] Okay, here we go.
[262.72 → 266.04] Welcome back, everyone, to go time.
[266.58 → 269.52] I am Carmen Onto and Matt is out this week,
[269.60 → 272.06] so I will be your host for the journey.
[272.94 → 275.36] Joining me today is our recurring panellist,
[275.54 → 276.58] Ashley McNamara.
[277.16 → 278.30] Say hello, Ashley.
[278.76 → 279.82] Hello, everyone.
[280.46 → 283.26] We have a returning guest, John Calhoun,
[283.26 → 288.40] who is the content founder for gophersizes.com,
[288.48 → 292.26] but also use goling.com, testwithgo.com,
[292.72 → 293.94] errorsandgo.com.
[294.64 → 296.40] And so I'm excited to have you on, John.
[296.50 → 296.98] Say hi.
[297.24 → 297.68] Hi, everybody.
[298.08 → 300.32] And now we have a new panel,
[300.44 → 301.04] or new guest,
[301.36 → 302.80] and it's Dave Valentine,
[303.28 → 305.52] and he's the instructor of Udemy's
[305.52 → 308.42] A Gentle Introduction to Golang for Beginners.
[309.12 → 310.20] Welcome to our show.
[310.60 → 311.54] Thank you so much.
[311.58 → 313.28] It's a pleasure to be here for the first time.
[313.68 → 314.58] Speaking of beginnings,
[314.80 → 318.40] when we asked Dave to show up on the show
[318.40 → 319.70] and give a profile pic,
[319.70 → 323.04] he submitted one of him as like a toddler
[323.04 → 327.20] with a TSR-80 Model 1 circa 1980.
[327.96 → 331.36] So I think that's probably like when you began.
[331.72 → 332.24] Absolutely.
[332.60 → 333.78] And Carmen, I have to say,
[333.88 → 335.02] I was chuckling when you're like,
[335.10 → 337.00] what computer is that?
[337.00 → 339.72] But yes, yes,
[339.72 → 343.02] I got a start in the microcomputer generation world.
[343.16 → 345.26] So I started with a TSR-80
[345.26 → 347.98] and then moved over to a PC junior
[347.98 → 353.26] and then continued on through microcomputers
[353.26 → 356.42] and programming way back at that time.
[356.52 → 358.10] So I've had an early start on things.
[358.54 → 359.10] Wow.
[359.66 → 360.50] That is hard.
[360.86 → 361.94] That is hardcore nerd.
[362.22 → 362.44] Yeah.
[362.82 → 364.74] Total nostalgia ahoy,
[364.74 → 366.00] I'm sure for many people.
[366.20 → 368.04] Certainly you can share what you started
[368.04 → 368.98] with your beginning,
[369.52 → 372.14] your first computer in the Go Time FM channel
[372.14 → 373.10] on Overslack.
[373.32 → 373.68] Okay.
[373.76 → 376.60] So let's talk a little bit about today's theme.
[377.16 → 379.30] This is Golang for beginners.
[380.14 → 382.72] I had originally envisioned this episode
[382.72 → 383.88] to engage,
[384.08 → 386.66] to be meant to engage for both non-Go users
[386.66 → 390.04] that listen to maybe sister podcasts on Change Lab
[390.04 → 393.28] or any Go curious programmers out there,
[394.00 → 396.14] and encourage those
[396.14 → 397.68] that have just started with Go
[397.68 → 400.20] and want to level up beyond the basics.
[400.62 → 403.04] So I'm hoping that maybe we can start
[403.04 → 405.72] and just kind of see where the conversation takes us.
[405.78 → 409.74] We have three wonderful experts online today
[409.74 → 411.80] and see what their perspectives
[411.80 → 412.86] and their experiences
[412.86 → 414.18] and how they've shared content
[414.18 → 415.80] to help Gophers worldwide.
[415.80 → 416.24] Okay.
[416.96 → 418.02] So I guess the first thing
[418.02 → 420.24] I wanted to start with is asked,
[420.78 → 422.04] what is a beginner?
[422.46 → 424.80] Like what types of beginners are there?
[425.22 → 425.52] Anyone?
[426.46 → 427.64] Good question.
[428.64 → 429.92] So there are beginners
[429.92 → 432.30] that know one programming language
[432.30 → 433.42] that want to learn another.
[433.76 → 436.24] There are people that are career transitioning
[436.24 → 438.98] that don't know any programming.
[439.36 → 441.08] There are all kinds of beginners.
[441.68 → 442.04] Yeah.
[442.16 → 442.48] I was going to say,
[442.54 → 444.04] there's even the curious kids
[444.04 → 445.50] who don't know what they're doing
[445.50 → 447.06] and like to break their parents' technology,
[447.42 → 449.40] which is probably some of us.
[449.62 → 449.90] Yeah.
[450.12 → 451.02] Those are my favourites.
[451.48 → 451.68] Yeah.
[452.12 → 452.52] Absolutely.
[452.68 → 453.54] I've experienced that
[453.54 → 454.92] with one of the courses
[454.92 → 456.32] that I've published
[456.32 → 457.92] that one of the kids was,
[458.38 → 458.90] what are we saying?
[458.98 → 460.60] I don't have system privilege
[460.60 → 462.64] to install Go on my computer.
[462.76 → 463.44] What do I do?
[463.62 → 463.86] Oh.
[464.12 → 464.48] You know,
[464.58 → 466.02] and how do I get around
[466.02 → 466.94] that kind of thing?
[467.14 → 467.34] So,
[467.68 → 469.18] because his dad had bought him
[469.18 → 469.98] the course.
[470.42 → 471.18] I've actually,
[471.58 → 472.24] in my program,
[472.24 → 473.60] originally created a course
[473.60 → 475.32] that was in advance
[475.32 → 476.28] of the one I currently have
[476.28 → 476.78] in the marketplace,
[476.94 → 477.80] which I've since retired,
[478.28 → 479.70] that was kind of trying to get
[479.70 → 481.00] the entire beginners
[481.00 → 481.78] in Go space,
[481.88 → 483.46] where it's for people
[483.46 → 484.12] that are experienced
[484.12 → 484.70] with programming
[484.70 → 485.76] and it's for people
[485.76 → 487.42] that are new to programming
[487.42 → 488.32] for the first time.
[488.46 → 489.90] But what I found was
[489.90 → 491.04] I was trying to appeal
[491.04 → 492.26] to too many different people
[492.26 → 494.04] and so the course content
[494.04 → 495.08] wasn't that effective.
[495.72 → 496.40] And since then,
[496.42 → 497.34] I've actually specialized
[497.34 → 500.00] in making something very clear.
[500.00 → 501.64] It is for absolute beginners
[501.64 → 503.48] because I actually walked them
[503.48 → 504.58] through some of the fundamentals
[504.58 → 505.70] of computer science
[505.70 → 507.60] in learning Go
[507.60 → 509.12] and giving them a foundation
[509.12 → 510.18] if they've never seen
[510.18 → 510.86] anything before.
[511.06 → 511.42] So,
[511.48 → 512.26] I've actually learned
[512.26 → 512.78] to specialize.
[513.38 → 514.68] And is this the course
[514.68 → 516.08] that I mentioned before
[516.08 → 517.30] or is this a different course?
[517.68 → 519.00] It is exactly the course
[519.00 → 519.78] you just mentioned.
[519.94 → 520.16] Yes,
[520.20 → 521.30] that one's been in the marketplace
[521.30 → 523.34] since January of this year
[523.34 → 524.84] and so it's a reboot
[524.84 → 526.28] specifically
[526.28 → 527.78] and I've taken the other one
[527.78 → 528.64] out of the marketplace.
[528.64 → 531.12] It is specifically intended
[531.12 → 532.48] for people that have never
[532.48 → 533.86] seen programming languages before
[533.86 → 535.44] and want to get started
[535.44 → 536.50] with the exciting
[536.50 → 537.62] computer language Go.
[538.24 → 538.76] That's great
[538.76 → 540.08] and just a reminder to everyone
[540.08 → 541.76] what Dave is referring to
[541.76 → 542.48] is Udemy
[542.48 → 543.60] Udemy.com
[543.60 → 544.68] and it's called
[544.68 → 546.08] A Gentle Introduction
[546.08 → 546.86] to Golang
[546.86 → 548.20] for Beginners.
[548.76 → 549.00] So,
[549.12 → 549.72] is that what you mean
[549.72 → 550.24] by gentle?
[550.50 → 550.68] So,
[550.86 → 551.68] the idea that you're
[551.68 → 552.52] a complete beginner
[552.52 → 554.02] not just a beginner
[554.02 → 554.70] to Go.
[555.38 → 556.48] Exactly right.
[556.56 → 557.38] That is just it
[557.38 → 558.18] because I did find
[558.18 → 558.98] that people were like,
[559.14 → 559.36] you know,
[559.88 → 560.80] what tends to happen
[560.80 → 561.40] with beginners
[561.40 → 562.30] is that
[562.30 → 564.28] they end up
[564.28 → 565.02] making assumptions
[565.02 → 565.90] about what the computer
[565.90 → 566.58] is doing underneath
[566.58 → 568.44] and they end up
[568.44 → 569.80] almost with a heuristic
[569.80 → 570.30] knowledge
[570.30 → 571.80] or almost some voodoo.
[571.92 → 572.74] Why is it like that?
[572.80 → 573.02] Well,
[573.42 → 574.66] I prefer to try
[574.66 → 576.30] to explain tip to tail
[576.30 → 577.32] everything that's happening.
[577.88 → 578.44] Maybe it's that
[578.44 → 579.54] deep computer background
[579.54 → 580.70] from that TSR-80
[580.70 → 581.34] time frame
[581.34 → 583.06] but I get into memory
[583.06 → 584.80] and what computer code
[584.80 → 585.70] actually looks like
[585.70 → 586.20] and the role
[586.20 → 586.88] of a compiler
[586.88 → 589.20] and try to expose
[589.20 → 590.08] all the pieces
[590.08 → 591.00] so at the end
[591.00 → 591.98] the light bulb
[591.98 → 592.70] goes on
[592.70 → 593.88] and somebody understands
[593.88 → 594.86] especially when it comes
[594.86 → 595.58] to understanding
[595.58 → 596.56] the concept
[596.56 → 597.68] of what's at
[597.68 → 598.42] a memory location
[598.42 → 599.34] versus what
[599.34 → 600.04] a memory location
[600.04 → 600.82] is itself.
[601.38 → 601.48] So,
[601.58 → 602.02] that is,
[602.08 → 602.60] you know,
[602.62 → 603.36] the type of thing
[603.36 → 603.92] journey
[603.92 → 604.52] that I bring
[604.52 → 605.26] with people through
[605.26 → 606.70] specifically though
[606.70 → 607.60] in relation
[607.60 → 608.64] to the Computer Language Go.
[608.64 → 610.20] that is the kind
[610.20 → 610.64] of course
[610.64 → 611.72] that I value
[611.72 → 612.38] specifically
[612.38 → 612.86] as somebody
[612.86 → 613.70] who does not
[613.70 → 614.90] have a CS degree
[614.90 → 616.46] I think I get
[616.46 → 617.46] into the weeds
[617.46 → 618.12] often
[618.12 → 619.18] because what happens
[619.18 → 620.52] I'm my own worst enemy
[620.52 → 622.06] what happens is
[622.06 → 623.16] I try to learn something
[623.16 → 623.46] and I'm like
[623.46 → 623.84] no,
[623.88 → 623.94] no,
[623.96 → 624.54] I need to know
[624.54 → 625.52] the thing before that
[625.52 → 626.16] and then the thing
[626.16 → 626.88] before that
[626.88 → 627.50] and then the thing
[627.50 → 628.26] before that
[628.26 → 629.34] until I'm like
[629.34 → 630.20] have I learned
[630.20 → 630.72] anything
[630.72 → 631.92] at all?
[632.06 → 632.40] So,
[632.50 → 633.34] I like to get
[633.34 → 634.08] into the weeds
[634.08 → 634.96] a little bit
[634.96 → 636.58] but if it's
[636.58 → 637.66] self-guided
[637.66 → 638.16] sometimes
[638.16 → 639.14] I'm too
[639.14 → 640.00] in the weeds.
[640.68 → 641.50] I think this is
[641.50 → 642.02] one of the reasons
[642.02 → 642.76] why at times
[642.76 → 643.20] I feel like
[643.20 → 643.86] the younger you are
[643.86 → 644.40] the easier it is
[644.40 → 645.04] to learn this stuff
[645.04 → 645.94] because you're
[645.94 → 647.00] less likely to
[647.00 → 647.36] try,
[647.44 → 648.18] like you're more
[648.18 → 648.62] willing to just
[648.62 → 649.38] take things for granted
[649.38 → 649.78] I think
[649.78 → 651.04] whereas like
[651.04 → 651.56] the older you get
[651.56 → 651.92] you're like
[651.92 → 652.98] I just think
[652.98 → 653.68] that it's easy
[653.68 → 653.98] to,
[654.34 → 654.44] you know,
[654.46 → 655.14] as an adult
[655.14 → 655.50] to like
[655.50 → 656.38] think I need
[656.38 → 656.96] to figure out
[656.96 → 657.34] what all these
[657.34 → 657.88] things are doing
[657.88 → 658.66] and understand it all
[658.66 → 659.14] and as a kid
[659.14 → 659.78] you're just like
[659.78 → 660.82] I'm willing to
[660.82 → 661.88] just trust you
[661.88 → 662.54] and just go with it
[662.54 → 663.44] and you know
[663.44 → 664.04] let it go.
[664.04 → 664.96] Interesting.
[665.30 → 665.74] So you think
[665.74 → 666.46] that's kind of
[666.46 → 667.30] maybe the key
[667.30 → 668.28] is just sort of
[668.28 → 669.38] trusting how
[669.38 → 670.72] whoever has shaped
[670.72 → 671.36] the content
[671.36 → 671.90] is going to
[671.90 → 672.76] structure the content
[672.76 → 673.76] that's how
[673.76 → 674.06] you're going to
[674.06 → 674.74] learn or?
[675.12 → 675.98] I sometimes think
[675.98 → 677.46] like one example
[677.46 → 678.00] I can give
[678.00 → 679.58] is I talked to
[679.58 → 680.36] somebody who
[680.36 → 681.38] had started a company
[681.38 → 682.36] and when they
[682.36 → 682.98] started the company
[682.98 → 683.74] they couldn't find
[683.74 → 684.48] a technical founder
[684.48 → 685.38] so they basically
[685.38 → 685.92] just went and
[685.92 → 686.36] learned programming
[686.36 → 686.82] on their own
[686.82 → 687.88] and I was talking
[687.88 → 688.40] to them about
[688.40 → 688.96] like how they
[688.96 → 689.66] learned to program
[689.66 → 691.04] and the one thing
[691.04 → 691.78] I found interesting
[691.78 → 692.80] was that they
[692.80 → 693.48] basically forced
[693.48 → 694.02] themselves to
[694.02 → 694.38] go through
[694.38 → 695.30] like three or four
[695.30 → 696.12] complete like web
[696.12 → 696.80] development courses
[696.80 → 697.70] and they said
[697.70 → 698.32] the first time
[698.32 → 698.76] there was a lot
[698.76 → 699.14] of things that
[699.14 → 699.48] were mentioned
[699.48 → 699.96] that they just
[699.96 → 700.90] didn't quite get
[700.90 → 701.92] but by the time
[701.92 → 702.32] they went through
[702.32 → 702.84] like their third
[702.84 → 704.04] course some of
[704.04 → 704.40] those things
[704.40 → 704.94] like they had
[704.94 → 705.78] enough understanding
[705.78 → 706.38] and foundation
[706.38 → 707.02] that those more
[707.02 → 707.72] intricate details
[707.72 → 708.34] started to make
[708.34 → 709.62] sense and I think
[709.62 → 710.12] if you get too
[710.12 → 710.76] focused on them
[710.76 → 711.74] early you just
[711.74 → 712.56] you know go down
[712.56 → 713.12] too many rabbit
[713.12 → 713.98] holes and you
[713.98 → 714.32] don't really
[714.32 → 714.84] you know get
[714.84 → 716.08] anywhere but if
[716.08 → 716.52] you're willing to
[716.52 → 717.18] just push yourself
[717.18 → 717.72] through it and
[717.72 → 718.46] realize that I'll
[718.46 → 719.04] come back to this
[719.04 → 719.56] later, or we'll
[719.56 → 719.96] go through the
[719.96 → 720.74] material again later
[720.74 → 721.36] then that can
[721.36 → 721.82] really help.
[721.82 → 723.60] That's a good
[723.60 → 723.98] point.
[724.14 → 724.88] Now you've
[724.88 → 725.50] mentioned a little
[725.50 → 726.08] bit about like
[726.08 → 726.86] kids and whatnot
[726.86 → 728.38] I also wanted to
[728.38 → 729.08] ask a little bit
[729.08 → 729.76] what everyone's
[729.76 → 730.42] thoughts were about
[730.42 → 731.08] like industry
[731.08 → 731.84] trends and
[731.84 → 732.90] educational backgrounds
[732.90 → 733.54] because I'm
[733.54 → 734.34] seeing that we
[734.34 → 735.72] are increasingly
[735.72 → 736.54] having people
[736.54 → 736.90] within our
[736.90 → 737.50] industry that are
[737.50 → 738.50] not formally
[738.50 → 739.18] trained with the
[739.18 → 739.98] university CS
[739.98 → 741.42] degree but maybe
[741.42 → 742.90] are self-taught or
[742.90 → 743.76] they went to a
[743.76 → 744.16] boot camp.
[744.28 → 744.96] I know Ashley that
[744.96 → 745.62] was your path
[745.62 → 745.92] right?
[745.92 → 746.92] So is there
[746.92 → 747.98] anything in terms
[747.98 → 749.08] of like difference
[749.08 → 750.08] between how we
[750.08 → 751.36] teach people that
[751.36 → 753.06] are not you know
[753.06 → 754.64] CS degree learners?
[755.34 → 756.74] So I what so
[756.74 → 757.50] boot camps are
[757.50 → 758.78] predatory sorry all
[758.78 → 760.62] boot camp grads I
[760.62 → 761.84] value you don't
[761.84 → 762.28] know they are
[762.28 → 762.72] predatory.
[763.58 → 764.98] I did all the
[764.98 → 766.38] open courseware for
[766.38 → 767.28] all the major
[767.28 → 768.04] universities.
[768.92 → 770.72] I that material was
[770.72 → 772.18] way more valuable but
[772.18 → 773.66] it's hard when you
[773.66 → 774.68] don't know where to
[774.68 → 775.08] start.
[775.08 → 776.06] You believe that you
[776.06 → 776.80] need a classroom
[776.80 → 777.24] setting.
[777.74 → 779.02] Some of us are not
[779.02 → 780.56] in a place where we
[780.56 → 782.40] can go get our CS
[782.40 → 782.94] degrees.
[783.10 → 784.16] That is a place of
[784.16 → 785.78] privilege and so
[785.78 → 786.60] some of us have to
[786.60 → 786.76] learn.
[786.88 → 787.50] So with all of
[787.50 → 789.14] these online courses
[789.14 → 791.00] out there are
[791.00 → 791.92] many more
[791.92 → 793.14] opportunities to
[793.14 → 794.20] self-pace and
[794.20 → 795.84] self-teach and not
[795.84 → 796.52] all of them are
[796.52 → 797.72] great so it takes
[797.72 → 799.04] some time to get
[799.04 → 800.38] through them but
[800.38 → 801.16] for me, I want to
[801.16 → 802.04] say that the most
[802.04 → 804.20] valuable learning that
[804.20 → 805.06] I did when I was
[805.06 → 805.74] learning to program
[805.74 → 806.64] was the open
[806.64 → 807.10] courseware.
[808.44 → 809.58] John and Dave can
[809.58 → 810.56] you tell us a little
[810.56 → 811.34] bit about your
[811.34 → 812.70] personal journeys as
[812.70 → 814.24] beginners both
[814.24 → 815.06] beginners but just
[815.06 → 816.56] beginners to go how
[816.56 → 817.42] you levelled up
[817.42 → 817.72] there.
[818.06 → 818.52] Absolutely.
[818.92 → 819.76] So I'll jump in
[819.76 → 820.28] there first.
[820.50 → 822.30] So go is gosh my
[822.30 → 823.40] eighth ninth tenth I'm
[823.40 → 824.36] not even sure anymore
[824.36 → 827.24] computer language and
[827.24 → 828.46] obviously having a
[828.46 → 829.28] background in computer
[829.28 → 830.06] science and having
[830.06 → 831.20] done a lot of
[831.20 → 832.54] things with it.
[832.54 → 834.12] Python is another
[834.12 → 834.42] one of the
[834.42 → 835.16] languages that I do
[835.16 → 835.92] a lot with because
[835.92 → 837.26] I also teach and
[837.26 → 838.06] introduce people to
[838.06 → 838.78] machine learning and
[838.78 → 839.66] artificial intelligence
[839.66 → 840.64] concepts and courses.
[841.36 → 843.22] With Go to be honest
[843.22 → 845.06] it sort of came about
[845.06 → 846.08] for me from market
[846.08 → 847.52] research because I
[847.52 → 848.54] became curious about
[848.54 → 849.58] what I should make my
[849.58 → 850.64] next great course on
[850.64 → 852.34] and then I found this
[852.34 → 853.56] amazing computer
[853.56 → 855.10] language that really
[855.10 → 856.06] is a next generation
[856.06 → 856.72] computer language
[856.72 → 857.38] because almost any
[857.38 → 858.12] other language that
[858.12 → 858.98] we may even consider
[858.98 → 860.32] new was really
[860.32 → 861.08] developed in the last
[861.08 → 861.46] century.
[861.46 → 861.88] Right.
[862.00 → 863.32] And I love the
[863.32 → 863.94] ghost story.
[864.26 → 865.82] The legend being that
[865.82 → 866.68] people are waiting for
[866.68 → 868.04] a C++ program to
[868.04 → 868.92] finish compiling and
[868.92 → 870.16] said hey if we were
[870.16 → 871.02] to develop a language
[871.02 → 873.34] now what could, should
[873.34 → 874.54] would that look like
[874.54 → 876.02] and you've got some
[876.02 → 876.92] brilliant engineers
[876.92 → 878.72] that that ended up
[878.72 → 879.66] putting it together
[879.66 → 880.76] and so I became
[880.76 → 882.40] absolutely fascinated by
[882.40 → 884.30] it and realized that
[884.30 → 885.24] here was a language
[885.24 → 886.32] that back in the day
[886.32 → 888.10] when I learned C for
[888.10 → 889.52] the first time very
[889.52 → 890.52] much smelled like
[890.52 → 891.64] tasted like acted
[891.64 → 893.30] like C exposed
[893.30 → 894.04] some of those
[894.04 → 894.88] fundamental computer
[894.88 → 896.54] bits but had grown
[896.54 → 897.78] into being so much
[897.78 → 898.46] more than a system
[898.46 → 900.12] based language and so
[900.12 → 901.52] I literally fell in
[901.52 → 902.30] love with it and
[902.30 → 903.78] then because I had
[903.78 → 904.86] intended to develop a
[904.86 → 906.34] course on it what I
[906.34 → 908.22] really try to do in
[908.22 → 909.16] all the courses that I
[909.16 → 911.06] teach is I try to
[911.06 → 912.60] develop a road map so
[912.60 → 914.10] that my students aren't
[914.10 → 915.26] sort of depending on
[915.26 → 915.42] me.
[915.52 → 917.06] My intent like with
[917.06 → 918.84] the internet there is
[918.84 → 920.74] this amazing amount
[920.74 → 921.74] of material that's
[921.74 → 922.50] out there, but it's
[922.50 → 923.66] not curated in a
[923.66 → 926.06] meaningful way and
[926.06 → 927.38] that is maybe the
[927.38 → 928.34] secret sauce that I
[928.34 → 929.06] try to bring to the
[929.06 → 931.12] table right it's you
[931.12 → 931.64] know because people
[931.64 → 932.48] have the itch they
[932.48 → 933.66] have that how do I
[933.66 → 935.60] get up to speed and
[935.60 → 937.40] make meaningful use of
[937.40 → 939.56] my time in order to
[939.56 → 940.58] achieve a learning
[940.58 → 941.90] understanding with go
[941.90 → 943.24] or whatever their
[943.24 → 945.12] thing is right and so
[945.12 → 946.52] in the course I have
[946.52 → 947.08] what I call an
[947.08 → 949.08] emergency Golang
[949.08 → 950.26] parachute which is
[950.26 → 951.24] learning resources
[951.24 → 953.48] right out of the gate
[953.48 → 954.72] right saying if you get
[954.72 → 956.50] stuck here's all the
[956.50 → 958.18] really other cool stuff
[958.18 → 959.90] that's out there that
[959.90 → 961.16] you should know about
[961.16 → 962.04] so that you can take
[962.04 → 963.10] advantage of that in
[963.10 → 963.82] order to supplement
[963.82 → 965.24] you're learning and then
[965.24 → 966.38] I finish off the course
[966.38 → 968.18] with here's where to go
[968.18 → 969.90] from here and to
[969.90 → 970.98] continue your learning
[970.98 → 973.00] journey and then take
[973.00 → 974.52] them through that piece
[974.52 → 975.02] where they can
[975.02 → 977.16] effectively then use
[977.16 → 978.26] those examples and
[978.26 → 979.68] resources and they
[979.68 → 980.64] have the know
[980.64 → 981.44] it's that very
[981.44 → 982.62] beginning that
[982.62 → 984.12] beginning is so hard
[984.12 → 985.68] for people that don't
[985.68 → 986.78] have any experience so
[986.78 → 987.56] giving them that
[987.56 → 989.06] ignition even that
[989.06 → 990.94] permission to break
[990.94 → 992.12] things and experiment
[992.12 → 993.10] with things and to
[993.10 → 995.34] think about things as
[995.34 → 996.18] they're coding and
[996.18 → 996.92] developing their
[996.92 → 998.24] exercises and so on
[998.24 → 1000.44] gets them that little
[1000.44 → 1001.60] bit of traction with
[1001.60 → 1002.88] their wheels and gets
[1002.88 → 1003.90] them started and the
[1003.90 → 1004.56] more students I can
[1004.56 → 1005.72] get started the
[1005.72 → 1007.02] happier I am that's
[1007.02 → 1008.24] great I think that's
[1008.24 → 1009.48] also a perfect
[1009.48 → 1010.96] what I say companion
[1010.96 → 1012.14] or complimentary to
[1012.14 → 1013.86] what John does which
[1013.86 → 1014.86] is okay you have an
[1014.86 → 1016.94] ignition you know the
[1016.94 → 1017.60] basics and the
[1017.60 → 1018.90] foundations the next
[1018.90 → 1019.52] thing you got to do
[1019.52 → 1022.50] is go for sizes right
[1022.50 → 1023.90] John tell us a little
[1023.90 → 1025.70] bit about that yeah so
[1025.70 → 1026.96] I mean basically
[1026.96 → 1028.14] whenever I learned what
[1028.14 → 1029.40] I generally found was
[1029.40 → 1030.86] that it didn't matter
[1030.86 → 1032.28] if I was coding the
[1032.28 → 1033.04] the prettiest code or
[1033.04 → 1034.10] anything it generally
[1034.10 → 1035.26] came down to if I
[1035.26 → 1036.22] coded a lot I learned
[1036.22 → 1037.48] a lot and if I didn't
[1037.48 → 1038.74] build things I you
[1038.74 → 1039.40] know I sort of just
[1039.40 → 1041.20] stopped learning and
[1041.20 → 1042.56] I think a lot of times
[1042.56 → 1043.56] I've talked to tons and
[1043.56 → 1044.34] tons of people who are
[1044.34 → 1044.84] like you know I'm
[1044.84 → 1045.66] trying to build things
[1045.66 → 1046.40] but I can't come up
[1046.40 → 1047.48] with a good project and
[1047.48 → 1048.48] what's even worse is if
[1048.48 → 1048.98] they come up with a
[1048.98 → 1049.98] project they like I
[1049.98 → 1050.52] had a friend who did
[1050.52 → 1051.74] this all the time he'd
[1051.74 → 1052.42] say I have this cool
[1052.42 → 1053.70] project, and he presented
[1053.70 → 1054.62] to me, and I'd be like
[1054.62 → 1055.92] well it's going to be
[1055.92 → 1056.90] really hard for you to do
[1056.90 → 1057.64] that project at your
[1057.64 → 1058.36] current skill level
[1058.36 → 1059.98] because there's like six
[1059.98 → 1060.80] other factors that you
[1060.80 → 1061.74] don't know much about
[1061.74 → 1063.44] and you know I know
[1063.44 → 1064.24] from experience that
[1064.24 → 1064.72] they're going to be
[1064.72 → 1065.68] very hard you know
[1065.68 → 1066.14] like they'll want to
[1066.14 → 1066.86] get data from it and
[1066.86 → 1067.36] they'll assume there's
[1067.36 → 1068.16] an API to get some
[1068.16 → 1069.50] data, and it's like no
[1069.50 → 1070.02] that doesn't really
[1070.02 → 1070.66] exist you're probably
[1070.66 → 1071.26] have to like scrape
[1071.26 → 1072.10] web pages and that's
[1072.10 → 1072.60] going to be terribly
[1072.60 → 1074.12] hard so go for sizes
[1074.12 → 1075.20] was kind of me saying
[1075.20 → 1076.08] you know if I was
[1076.08 → 1076.82] starting over and I
[1076.82 → 1077.42] just wanted some
[1077.42 → 1078.52] random exercises to
[1078.52 → 1079.28] build that weren't
[1079.28 → 1080.36] completely boring but
[1080.36 → 1081.48] would challenge me
[1081.48 → 1082.40] would teach me to
[1082.40 → 1084.02] read the docs to look
[1084.02 → 1085.06] at different APIs in the
[1085.06 → 1086.40] standard library to do
[1086.40 → 1087.74] stuff like that what
[1087.74 → 1088.44] would they look like
[1088.44 → 1089.74] and I basically just sat
[1089.74 → 1090.54] down and picked out
[1090.54 → 1092.22] 20 projects that I
[1092.22 → 1092.88] sort of picked them
[1092.88 → 1093.66] intentionally to try
[1093.66 → 1094.36] different stuff I
[1094.36 → 1094.86] didn't want to keep
[1094.86 → 1095.88] using the same thing so
[1095.88 → 1096.40] I didn't want to build
[1096.40 → 1097.46] like 20 web applications
[1097.46 → 1099.00] but the idea was like
[1099.00 → 1099.56] you know if you go
[1099.56 → 1100.26] through all of these
[1100.26 → 1101.12] and you code them all
[1101.12 → 1101.72] and you actually give
[1101.72 → 1102.48] it is an honest shot of
[1102.48 → 1103.18] trying to solve each
[1103.18 → 1104.14] problem on your own
[1104.14 → 1105.74] you will learn a ton in
[1105.74 → 1106.94] the process even if you
[1106.94 → 1107.68] don't complete them
[1107.68 → 1108.92] fully, or you don't
[1108.92 → 1110.16] understand everything or
[1110.16 → 1111.00] your code's pretty ugly
[1111.00 → 1111.76] it doesn't matter you
[1111.76 → 1112.48] will still learn a lot
[1112.48 → 1112.92] doing it.
[1113.44 → 1114.12] I think that that's so
[1114.12 → 1115.26] valuable as well because
[1115.26 → 1116.48] I tweeted about this
[1116.48 → 1117.56] recently when I was
[1117.56 → 1119.94] learning to code I was
[1119.94 → 1120.74] already pretty well
[1120.74 → 1122.20] established in tech on
[1122.20 → 1123.96] Twitter and so like how
[1123.96 → 1125.42] should I start just build
[1125.42 → 1126.78] something build what
[1126.78 → 1128.94] something what where
[1128.94 → 1130.28] where do I start how do
[1130.28 → 1131.86] I start what do I build
[1131.86 → 1133.78] I don't know well you
[1133.78 → 1134.62] know what figure it out
[1134.62 → 1135.72] that's how you learn just
[1135.72 → 1136.34] figure it out.
[1136.34 → 1137.38] and that's really
[1137.38 → 1137.90] frustrating.
[1138.18 → 1139.50] So frustrating because
[1139.50 → 1141.94] you just like to build a to-do
[1141.94 → 1144.62] app like tell me something
[1144.62 → 1145.86] tell me where to start
[1145.86 → 1148.04] right, and so I feel like
[1148.04 → 1149.24] really experienced
[1149.24 → 1151.14] programmers that's kind of
[1151.14 → 1152.46] their go-to advice we'll
[1152.46 → 1153.26] just go build
[1153.26 → 1153.58] something.
[1154.16 → 1155.60] Actually the other advice
[1155.60 → 1156.42] that I'd add to that
[1156.42 → 1157.28] though I mean if you've
[1157.28 → 1158.70] got a project right build
[1158.70 → 1160.24] it right but don't build
[1160.24 → 1161.34] it just once build it
[1161.34 → 1164.00] three times because the
[1164.00 → 1164.94] first time you build it
[1164.94 → 1165.46] right you're going to
[1165.46 → 1166.54] commit all the sins and
[1166.54 → 1167.12] you're going to build the
[1167.12 → 1168.44] wrong thing right it's not
[1168.44 → 1169.96] going to meet the needs
[1169.96 → 1170.68] that you're looking to
[1170.68 → 1172.16] address with it right it's
[1172.16 → 1172.94] not going to work well
[1172.94 → 1173.56] you're going to be like oh
[1173.56 → 1174.38] that was
[1174.38 → 1175.98] horrific right the second
[1175.98 → 1177.24] time it will probably
[1177.24 → 1178.86] function and achieve what
[1178.86 → 1180.66] you want it to achieve in
[1180.66 → 1181.62] terms of the end results
[1181.62 → 1182.38] of the thing that you're
[1182.38 → 1183.66] building, but you're going
[1183.66 → 1185.10] to think oh that is some
[1185.10 → 1187.50] ugly awful evil code
[1187.50 → 1189.42] there are monsters working
[1189.42 → 1191.14] inside that you hate
[1191.14 → 1193.22] and the third time then
[1193.22 → 1194.06] you're in a position where
[1194.06 → 1195.54] you can actually put
[1195.54 → 1196.78] together some really
[1196.78 → 1199.48] elegant approaches and to
[1199.48 → 1200.60] develop some beautiful
[1200.60 → 1202.72] code and so if I were to
[1202.72 → 1203.74] add any advice with that
[1203.74 → 1204.80] once you do find that
[1204.80 → 1205.86] something whatever that
[1205.86 → 1207.42] is if that's reproducing
[1207.42 → 1208.50] someone's example or
[1208.50 → 1210.52] finding anything that
[1210.52 → 1211.70] inspires you to build
[1211.70 → 1213.04] something build it three
[1213.04 → 1213.48] times.
[1214.34 → 1216.06] Wow I love that advice.
[1216.26 → 1217.94] Me too I heard once that
[1217.94 → 1219.98] if you want to become a
[1219.98 → 1222.46] great writer don't read a
[1222.46 → 1224.28] hundred books just read one
[1224.28 → 1226.58] book a hundred times and I
[1226.58 → 1227.64] think this is kind of in the
[1227.64 → 1229.30] same vein Dave in that this
[1229.30 → 1230.38] kind of gives you the chance
[1230.38 → 1231.42] to revisit a thing in
[1231.42 → 1232.72] different stages which is
[1232.72 → 1234.16] reality right in terms of
[1234.16 → 1236.00] maintaining a software a
[1236.00 → 1237.34] piece of software as it
[1237.34 → 1239.42] ages as you age and an
[1239.42 → 1240.60] increase in your skill set
[1240.60 → 1242.48] etc, etc so that's really
[1242.48 → 1244.12] great I love that I'm going
[1244.12 → 1244.72] to try that.
[1245.30 → 1246.16] Just to add something to
[1246.16 → 1247.28] that I know some people get
[1247.28 → 1249.04] bored doing that, or I should
[1249.04 → 1249.94] say some people seem like
[1249.94 → 1251.10] they do even if you don't
[1251.10 → 1252.34] build the exact same thing I
[1252.34 → 1253.68] think building similar things
[1253.68 → 1255.48] is probably would go in line
[1255.48 → 1256.58] with what Dave's saying
[1256.58 → 1258.36] because I'll see people take
[1258.36 → 1259.20] like a course, and they'll
[1259.20 → 1260.00] just build whatever's in the
[1260.00 → 1260.82] course then they'll be done
[1260.82 → 1262.58] and what I really like to
[1262.58 → 1264.44] encourage is to like to go back
[1264.44 → 1265.34] through the course and build
[1265.34 → 1266.50] something similar but not
[1266.50 → 1267.68] quite the same so it forces
[1267.68 → 1269.22] you to go out on your own and
[1269.22 → 1270.40] sort of you know do what he's
[1270.40 → 1271.42] saying to try different stuff
[1271.42 → 1272.34] to do a little bit different
[1272.34 → 1273.76] but you're still building you
[1273.76 → 1274.88] know the same basic building
[1274.88 → 1276.02] blocks you know like you're
[1276.02 → 1277.06] building a web application or
[1277.06 → 1278.72] you're building a CLI or
[1278.72 → 1279.88] whatever, but it might do
[1279.88 → 1280.92] something slightly different
[1280.92 → 1281.78] that forces you to really
[1281.78 → 1282.74] think about what you're doing
[1282.74 → 1283.60] and consider stuff.
[1284.10 → 1285.22] Yes John and I think that
[1285.22 → 1286.84] learning is repetition right
[1286.84 → 1288.48] if you learn anything right
[1288.48 → 1289.48] you're gonna you need to
[1289.48 → 1291.10] repeat it in order to sort of
[1291.10 → 1292.62] make it go to long-term
[1292.62 → 1293.92] memory, but I think that
[1293.92 → 1295.20] that's also a great approach.
[1308.72 → 1321.00] This episode is brought to you by
[1321.00 → 1322.76] our friends at Fire Hydrant.
[1322.96 → 1324.28] Fire Hydrant is the reliability
[1324.28 → 1325.82] platform for every developer.
[1326.22 → 1328.00] Incidents, they impact everyone
[1328.00 → 1330.00] not just Sees.
[1330.16 → 1331.50] They give teams the tools to
[1331.50 → 1332.98] maintain service catalogues,
[1333.18 → 1334.26] respond to incidents,
[1334.44 → 1335.74] communicate through status pages,
[1335.74 → 1337.90] and learn with retrospectives.
[1338.26 → 1339.62] What would normally be manual
[1339.62 → 1341.52] error-prone tasks across the
[1341.52 → 1343.08] entire spectrum are responding
[1343.08 → 1343.66] to an incident.
[1343.96 → 1345.50] They can all be automated in
[1345.50 → 1347.16] every way with Fire Hydrant.
[1347.36 → 1348.86] They have incident tooling to
[1348.86 → 1350.72] manage incidents of any type with
[1350.72 → 1352.50] any severity with consistency.
[1353.04 → 1354.64] Declare and mitigate incidents
[1354.64 → 1356.18] all from inside Slack.
[1356.58 → 1357.74] Service catalogues allow service
[1357.74 → 1359.12] owners to improve operational
[1359.12 → 1361.28] maturity and document all your
[1361.28 → 1362.90] deploys in your service catalogue.
[1363.50 → 1364.84] Incident analytics allow you to
[1364.84 → 1366.10] extract meaningful insights
[1366.10 → 1367.68] about your reliability over any
[1367.68 → 1369.66] facet of your incident or the
[1369.66 → 1370.86] people who respond to them.
[1371.24 → 1372.06] And at the heart of it all
[1372.06 → 1373.46] incident run books, they let you
[1373.46 → 1375.16] create custom automation rules,
[1375.40 → 1376.76] convert manual tasks into
[1376.76 → 1378.80] automated, reliable, repeatable
[1378.80 → 1380.64] sequences that run when you want.
[1381.00 → 1381.98] You can create Slack channels,
[1382.12 → 1383.30] Jira tickets, Zoom bridges
[1383.30 → 1384.74] instantly after declaring an
[1384.74 → 1385.02] incident.
[1385.50 → 1386.50] Now your processes can be
[1386.50 → 1388.08] consistent and automatic.
[1388.52 → 1390.22] The next step is to try it free.
[1390.36 → 1392.08] Small teams, up to 10 people,
[1392.22 → 1393.54] can get started for free with all
[1393.54 → 1394.74] Fire Hydrant features included.
[1395.08 → 1396.46] No credit card is required.
[1396.92 → 1398.98] Get started at FireHydrant.io.
[1399.36 → 1401.38] Again, FireHydrant.io.
[1401.38 → 1419.18] Well, I want to segue in to,
[1419.82 → 1421.82] instead of maybe talking more about
[1421.82 → 1424.60] how we learn and approaches to
[1424.60 → 1426.76] learning, let's talk about
[1426.76 → 1428.02] learning and go.
[1428.02 → 1430.36] And so we kind of touched on that
[1430.36 → 1432.08] about the starting point in
[1432.08 → 1433.80] foundations and computer science
[1433.80 → 1435.02] fundamentals in your course,
[1435.34 → 1436.46] your Udemy course, Dave.
[1436.88 → 1440.72] But how do you teach beginners go?
[1440.98 → 1442.42] And we can talk about this either
[1442.42 → 1445.18] from other languages in terms of
[1445.18 → 1447.84] their experience or from scratch.
[1448.18 → 1450.40] And what do you think is unique to
[1450.40 → 1452.08] learning and go versus just
[1452.08 → 1453.20] programming in general?
[1453.90 → 1455.70] Well, I specifically at this point
[1455.70 → 1457.46] specialize in starting from scratch.
[1457.46 → 1460.48] And so I have my course that is
[1460.48 → 1462.42] designed really to bring someone up
[1462.42 → 1463.00] from scratch.
[1463.44 → 1465.56] And one thing I did find is that
[1465.56 → 1466.86] originally some people were having
[1466.86 → 1468.20] some trouble with the technical
[1468.20 → 1468.98] aspects of it.
[1469.04 → 1470.00] They were having some trouble with
[1470.00 → 1471.84] GOPATH and Groot and some of those
[1471.84 → 1472.16] things.
[1473.00 → 1475.48] And originally I had created
[1475.48 → 1476.98] Windows installation videos and
[1476.98 → 1479.70] saying, hey, if you want, you can go
[1479.70 → 1481.88] ahead and, you know, do the same
[1481.88 → 1482.60] thing on Mac.
[1482.66 → 1483.84] You can do the same thing on Linux.
[1483.84 → 1486.26] And when I rebooted the course and
[1486.26 → 1487.94] specialized more in helping beginners,
[1487.94 → 1489.82] I said, the heck with that noise.
[1489.82 → 1493.24] And I literally have approached it to
[1493.24 → 1495.62] give them videos and follow through
[1495.62 → 1499.70] instructions on Windows 10, on macOS,
[1499.80 → 1502.18] as well as Ubuntu Linux, so that they
[1502.18 → 1503.62] at least have something that looks,
[1503.80 → 1506.12] tastes and smells similar to whatever
[1506.12 → 1507.08] platform they have.
[1507.10 → 1508.60] Because there were some people that
[1508.60 → 1509.66] were experiencing problems.
[1509.66 → 1512.16] And my intent with it is to reduce
[1512.16 → 1513.82] the amount of friction at all
[1513.82 → 1514.28] possible.
[1514.96 → 1517.32] Once they achieve that, though, what
[1517.32 → 1519.34] I find is that people are really
[1519.34 → 1520.42] functional within it.
[1520.50 → 1521.54] They get an understanding.
[1522.02 → 1523.62] One of the beautiful things that is,
[1523.70 → 1526.36] I think, unique about Go as well is
[1526.36 → 1528.06] that if people want, they can get into
[1528.06 → 1529.18] the Go code itself.
[1529.34 → 1529.96] It's there.
[1530.08 → 1531.08] It's in your workstation.
[1531.28 → 1533.18] If you're interested in how, you know,
[1533.26 → 1534.68] print line works and things of that
[1534.68 → 1536.40] nature, you can sort of dive into it
[1536.40 → 1538.66] and start to see these other elements
[1538.66 → 1540.76] and how they come together in the
[1540.76 → 1543.40] compiler and provide a, you know,
[1543.42 → 1545.36] the end user experience of the
[1545.36 → 1547.14] compilation and the code that gets
[1547.14 → 1547.66] executed.
[1548.08 → 1549.56] So really, I think, you know, it's
[1549.56 → 1550.92] similar to other programming languages
[1550.92 → 1553.58] in the sense that the fundamentals
[1553.58 → 1554.28] are the same.
[1554.68 → 1556.92] But it has, you know, great syntax.
[1557.30 → 1558.24] It's really thoughtful.
[1558.58 → 1560.52] It's really built for concurrency.
[1561.06 → 1563.28] And I think it's really an effective
[1563.28 → 1565.48] language for beginners because some of
[1565.48 → 1566.90] those obscure elements in earlier
[1566.90 → 1568.06] languages aren't there.
[1568.56 → 1570.06] It's very quick to compile.
[1570.66 → 1572.14] So I'm really an evangelist when it
[1572.14 → 1572.78] comes to it.
[1573.04 → 1574.50] But I did find that some of the
[1574.50 → 1575.84] students that I was experiencing had
[1575.84 → 1577.50] that little bit of friction at first.
[1577.88 → 1580.10] And now if I can get them over that,
[1580.22 → 1581.68] you know, then they're off to the
[1581.68 → 1581.90] races.
[1582.14 → 1584.46] It's usually a very early problem early
[1584.46 → 1586.72] on, or they're off to the races and
[1586.72 → 1589.08] then asking more advanced items out
[1589.08 → 1589.46] of the gate.
[1589.52 → 1591.70] So there's this pendulum that swings in
[1591.70 → 1593.72] their experience, I find, where they're
[1593.72 → 1594.74] like, oh, that was awesome.
[1594.82 → 1595.40] What's next?
[1595.40 → 1595.84] Right.
[1596.26 → 1596.92] In the beginning.
[1597.28 → 1597.50] Right.
[1597.58 → 1598.96] Well, you know, until recently.
[1599.28 → 1600.16] Thanks, Go team.
[1600.80 → 1603.22] Go path was a nightmare.
[1604.22 → 1606.82] So once you got through that hurdle,
[1607.20 → 1609.06] after you're like ready to throw your
[1609.06 → 1611.04] computer, and then you build something,
[1611.26 → 1612.34] you're feeling better.
[1612.50 → 1614.64] But I think that the hurdle of setting
[1614.64 → 1616.50] up your Go path was such a nightmare
[1616.50 → 1618.30] that people were just like, no, no.
[1618.36 → 1620.18] If this is just set up, how's it going
[1620.18 → 1620.48] to be?
[1620.84 → 1621.50] Oh, absolutely.
[1621.50 → 1623.44] And getting that to be set out of the
[1623.44 → 1625.06] default was the most brewing thing that
[1625.06 → 1625.44] could happen.
[1625.44 → 1627.06] So I think that's one of the reasons
[1627.06 → 1629.48] why, like, you see PHP being so popular
[1629.48 → 1630.40] still to this day.
[1630.64 → 1632.40] And I still think one of the big reasons
[1632.40 → 1634.56] it was because if you knew very
[1634.56 → 1636.92] little, you could find a free PHP server
[1636.92 → 1639.48] and just upload a file or your FTP in or
[1639.48 → 1640.64] something and connect to and change a
[1640.64 → 1642.02] file, and you would see results like you
[1642.02 → 1643.28] didn't have to understand or install
[1643.28 → 1644.64] anything, and you could get stuff working.
[1644.64 → 1646.54] And I think like every new language
[1646.54 → 1648.14] should strive for as much simplicity
[1648.14 → 1648.82] as possible.
[1649.22 → 1650.16] Like, that's one of the reasons why I
[1650.16 → 1652.66] love the Go Playground, because I'm
[1652.66 → 1654.02] glad they thought about like we need
[1654.02 → 1655.36] some way for somebody to quickly and
[1655.36 → 1657.42] easily just write some code and you
[1657.42 → 1658.58] like, yeah, it's limited to the standard
[1658.58 → 1659.84] library and some stuff like that.
[1659.90 → 1661.58] But it's still a great learning tool
[1661.58 → 1663.00] for somebody who, you know, like you
[1663.00 → 1664.24] said, couldn't install it for some
[1664.24 → 1666.12] reason, or they just want to see it
[1666.12 → 1667.58] before they actually spend that time.
[1667.74 → 1669.42] Because I think if we don't focus on
[1669.42 → 1671.22] that some there are languages like
[1671.22 → 1672.78] JavaScript where, you know, you can
[1672.78 → 1674.76] have interactive tutorials really,
[1674.90 → 1675.88] really easily in JavaScript.
[1676.62 → 1677.74] And, you know, somebody can just
[1677.74 → 1678.94] bring up Chrome and open up Chrome
[1678.94 → 1680.50] DevTools and write some JavaScript.
[1680.96 → 1682.48] So like, you know, the barrier to
[1682.48 → 1684.44] entry there is so small that I think
[1684.44 → 1685.54] it's important for other languages
[1685.54 → 1686.50] to keep that in mind.
[1687.16 → 1688.98] Yeah, this is a good thing that I
[1688.98 → 1690.50] kind of was wondering, like how much
[1690.50 → 1692.12] is set up a part of learning Go
[1692.12 → 1693.02] versus other languages?
[1693.02 → 1694.58] And you mentioned PHP and Java.
[1694.82 → 1697.38] And if it's different, what are some
[1697.38 → 1700.32] of the setup gotchas in addition or
[1700.32 → 1701.42] you think are going to be the setup
[1701.42 → 1703.72] gotchas or the learning gotchas?
[1704.16 → 1705.54] And maybe we can ask for audience
[1705.54 → 1707.84] participation on the Go Time FM
[1707.84 → 1708.50] Slack channel.
[1708.98 → 1710.26] Well, some of these show-offs are
[1710.26 → 1712.54] saying that GOPATH made perfect
[1712.54 → 1713.36] sense to them.
[1713.90 → 1715.78] So good job, guys.
[1715.98 → 1716.64] Good job.
[1717.06 → 1718.70] I think the problem with it was like
[1718.70 → 1720.16] it either made sense to you or it
[1720.16 → 1721.06] made no sense to you.
[1721.16 → 1722.12] There was no middle ground.
[1722.80 → 1723.24] Yes.
[1723.58 → 1725.04] And it was also very platform
[1725.04 → 1726.40] specific as well, right?
[1726.40 → 1727.28] Because at that point when you're
[1727.28 → 1728.54] hooking into environment variables
[1728.54 → 1730.50] or whatever your platform is,
[1730.52 → 1731.80] you can get stuck in the details
[1731.80 → 1733.00] of your particular platform.
[1733.66 → 1735.14] Yeah, especially because a lot of
[1735.14 → 1736.26] beginners are coming from Windows
[1736.26 → 1737.72] and like setting environment
[1737.72 → 1739.24] variables has always seemed easier
[1739.24 → 1739.58] to me.
[1739.68 → 1741.22] And, you know, in Mac or Linux,
[1741.40 → 1743.04] whereas on Windows, trying to get
[1743.04 → 1744.14] somebody to go set that stuff up
[1744.14 → 1745.72] correctly was sometimes a pain.
[1746.18 → 1746.50] Yeah.
[1746.66 → 1747.46] Super pain.
[1747.72 → 1750.38] We used to, me and Steve Francia,
[1750.74 → 1753.24] who, hi, Steve, used to teach
[1753.24 → 1754.04] workshops.
[1754.32 → 1755.72] And the first thing that we would do
[1755.72 → 1756.94] is raise your hand if you use
[1756.94 → 1757.72] a Windows machine.
[1758.08 → 1758.44] Great.
[1758.98 → 1760.42] You guys are now friends
[1760.42 → 1762.50] because you're going to need
[1762.50 → 1763.78] to help each other during setup
[1763.78 → 1764.96] because we cannot help you.
[1765.58 → 1765.90] Mm-hmm.
[1766.14 → 1767.86] Yeah, you taught, and I have that
[1767.86 → 1768.80] material, and I thought it was
[1768.80 → 1770.96] amazing in terms of CLI.
[1771.32 → 1772.70] So CLI workshop, and I think it
[1772.70 → 1774.28] was for OSCAN last year or the
[1774.28 → 1774.86] year before.
[1775.60 → 1777.20] And it has like, the slide deck
[1777.20 → 1778.80] is something like 300-some slides.
[1779.36 → 1781.14] And setup, Ashley, was like the
[1781.14 → 1782.96] first third of that, right?
[1782.96 → 1784.96] And so I just wonder, like, is that
[1784.96 → 1786.68] the hump that we just want to help
[1786.68 → 1787.96] beginners get over, and then they'll
[1787.96 → 1789.16] be able to get really productive
[1789.16 → 1790.08] soon after that?
[1790.52 → 1793.26] It really was the first half of
[1793.26 → 1794.16] the workshop.
[1794.76 → 1796.76] Setup was difficult for a lot of
[1796.76 → 1797.06] people.
[1797.20 → 1798.74] There was a lot of going around and
[1798.74 → 1800.20] helping people get their machines
[1800.20 → 1800.68] set up.
[1800.98 → 1804.50] Once we got into building the app,
[1804.78 → 1806.94] things seemed to flow much, much
[1806.94 → 1807.40] easier.
[1807.82 → 1810.32] So yeah, setup was definitely a big
[1810.32 → 1810.64] issue.
[1810.64 → 1812.42] I think setup's also like the
[1812.42 → 1813.50] biggest quitting point, too.
[1813.94 → 1814.12] Yeah.
[1814.32 → 1815.64] Like, at some point during setup, if
[1815.64 → 1816.76] it stops working, you quit.
[1816.92 → 1818.88] But like, if you're writing code and
[1818.88 → 1820.44] you've got most things running, I
[1820.44 → 1821.68] think you're less likely to quit at
[1821.68 → 1822.06] that point.
[1822.38 → 1824.18] And is this unique to Go, or are we
[1824.18 → 1826.62] just, I want to kind of give a nod to
[1826.62 → 1828.38] any beginner out there, whether it's
[1828.38 → 1829.48] somebody who's already learned
[1829.48 → 1830.92] something else in terms of the
[1830.92 → 1831.86] programming language, or someone
[1831.86 → 1834.48] who's a complete beginner, is set up
[1834.48 → 1836.34] a quitting point for all languages, or
[1836.34 → 1838.14] is it a little bit more painful in Go?
[1838.44 → 1839.02] I think it's all.
[1839.02 → 1840.72] I think every language has some, like,
[1840.78 → 1842.46] barrier to entry, and once you get it,
[1842.56 → 1842.92] you're good.
[1843.04 → 1844.62] But up until that point, it can be
[1844.62 → 1845.02] frustrating.
[1845.70 → 1846.94] I do think it also depends on whether
[1846.94 → 1848.04] you're talking about an interpreted
[1848.04 → 1849.92] language or a compiled language as
[1849.92 → 1850.50] well, right?
[1850.74 → 1852.44] Because it is a little, you know, hard
[1852.44 → 1853.98] to compare Go to an interpreted
[1853.98 → 1856.20] language, like the like of PHP,
[1856.40 → 1857.82] perhaps, in the way that it's
[1857.82 → 1859.20] structured and some of those elements
[1859.20 → 1860.46] that it actually achieves underneath.
[1860.90 → 1863.10] But one other element I think comes
[1863.10 → 1864.74] into play is, you know, what do you
[1864.74 → 1866.56] then, once you have Gone set up, what do
[1866.56 → 1868.60] you hook in after that, right?
[1868.68 → 1870.12] Is it an IDE?
[1870.44 → 1871.78] Do you have plans for an IDE?
[1872.18 → 1873.72] Because there's some really outstanding
[1873.72 → 1874.98] things you can do afterwards.
[1875.12 → 1877.18] And yeah, I show, just like everyone
[1877.18 → 1878.32] else does, how do you make a Hello
[1878.32 → 1879.98] Word program on the command line?
[1880.48 → 1882.62] But then if you can actually trace and
[1882.62 → 1884.48] set up breakpoints and have an IDE
[1884.48 → 1887.46] experience after that, that will help
[1887.46 → 1889.60] guide the student, then they can trace
[1889.60 → 1891.32] their way through the code, which again,
[1891.32 → 1892.72] will help them understand what's actually
[1892.72 → 1894.06] happening underneath the covers.
[1894.06 → 1896.08] So, you know, there's that initial setup,
[1896.22 → 1898.40] but then also, and that's the kind of
[1898.40 → 1900.48] thing where, ask anyone, they have
[1900.48 → 1902.22] their favourite, is it Atom, is it
[1902.22 → 1903.94] Sublime, is it Visual Studio Code?
[1904.44 → 1906.30] Everyone has their favourite sort of
[1906.30 → 1909.14] tools to then add to the language,
[1909.32 → 1910.94] whatever language they're programming
[1910.94 → 1911.98] on at that point, right?
[1912.30 → 1912.50] Yeah.
[1912.64 → 1914.34] And then what do you think about in
[1914.34 → 1917.26] terms of content or setup, in terms
[1917.26 → 1918.90] of audience competence?
[1919.44 → 1921.54] We have a comment here from Corey Land
[1921.54 → 1924.06] in the Go Time FM Slack, who said that
[1924.06 → 1925.64] Go Install was the easiest that he's
[1925.64 → 1928.14] ever used, but again, it was geared
[1928.14 → 1929.62] towards me as an audience.
[1930.04 → 1932.10] And so that we're saying somebody who's
[1932.10 → 1933.70] an experienced beginner.
[1934.18 → 1936.50] So is there content, do you feel like
[1936.50 → 1938.42] for the people who have sort of looked
[1938.42 → 1940.48] through content, created content in this
[1940.48 → 1942.76] panel, that there are audiences for whom
[1942.76 → 1944.66] there are content gaps for beginners?
[1945.04 → 1946.24] Yeah, I do think.
[1946.24 → 1948.70] So when people ask me what language they
[1948.70 → 1951.02] should start with, I usually say Python,
[1951.52 → 1953.68] because there's so much information out
[1953.68 → 1955.08] there, and I felt like setup was easier
[1955.08 → 1955.84] for some reason.
[1956.30 → 1959.22] For Go, I feel like there's a lot of highly
[1959.22 → 1961.26] technical things out there, which is great.
[1961.62 → 1964.02] And then there are some beginner courses
[1964.02 → 1966.26] that may or may not work.
[1966.40 → 1967.94] I'm excited to try your guys'
[1968.18 → 1971.94] So I just felt like beginner materials were
[1971.94 → 1973.20] super lacking.
[1973.20 → 1975.78] For me, when I learn a new programming
[1975.78 → 1978.08] language, I am not ashamed by this.
[1978.24 → 1979.12] I don't care if you laugh.
[1979.56 → 1980.78] I buy children's books.
[1981.06 → 1982.90] I love kids' programming books.
[1983.10 → 1984.10] They are the greatest.
[1984.58 → 1986.50] There needs to be one for Go yesterday.
[1987.42 → 1988.56] Oh my God, yes.
[1988.96 → 1991.88] Well, you know, there was this trend that
[1991.88 → 1993.08] was, I don't know, it's probably about
[1993.08 → 1993.82] eight years old now.
[1993.92 → 1995.36] Do you remember ELI 5?
[1995.50 → 1996.74] Explain It Like I'm 5?
[1996.90 → 1997.22] Yes.
[1997.34 → 1999.18] And it was like a popular, yeah, those
[1999.18 → 2001.70] were great because it was, you know, we
[2001.70 → 2004.06] had someone in the chat earlier said, well,
[2004.10 → 2006.16] I need to learn the thing to get to the thing
[2006.16 → 2008.04] and learn the thing before that thing.
[2008.50 → 2011.84] And it's just a recursive, but I don't know
[2011.84 → 2012.88] this all the way down.
[2012.98 → 2015.38] And so I'm hoping your gentle beginners course
[2015.38 → 2016.94] tackles exactly that.
[2017.16 → 2018.20] Well, I appreciate that.
[2018.24 → 2019.96] And I'll tell you, you know, you're almost
[2019.96 → 2021.26] throwing the gauntlet down because I have
[2021.26 → 2022.32] twin 11-year-olds.
[2022.86 → 2024.48] And while they have tasted a little bit of
[2024.48 → 2027.02] Python and a lot of scratch, I'm thinking
[2027.02 → 2029.04] I should be the, you know, maybe the first to
[2029.04 → 2031.76] write a Golang children's book at this rate.
[2031.96 → 2032.92] So we'll see.
[2033.00 → 2033.74] I'll give it some thought.
[2034.42 → 2035.66] Please do.
[2035.84 → 2036.14] Yes.
[2036.24 → 2037.58] I hope you have a good artist because I feel
[2037.58 → 2038.78] like that'd be my biggest limitation.
[2038.92 → 2040.12] If I was drawing it, it would look like a
[2040.12 → 2041.20] five-year-old drew the whole thing.
[2041.50 → 2044.54] Oh, I am a coder, you know, coder art scheme.
[2044.66 → 2046.68] I'd be, you know, full up on the red, green
[2046.68 → 2047.76] and blue colours.
[2047.88 → 2048.86] It would look horrific.
[2049.90 → 2053.70] So yeah, I need to, any artists shout it out
[2053.70 → 2056.20] and I could probably use some folks to
[2056.20 → 2056.84] collaborate with.
[2056.90 → 2057.44] There's no doubt.
[2057.44 → 2058.20] I'm here.
[2058.32 → 2059.20] I'm taking note.
[2059.94 → 2062.26] There may or may not be a preeminent artist
[2062.26 → 2064.50] for the Golang community speaking to us
[2064.50 → 2065.84] at this moment right now.
[2065.96 → 2066.20] Maybe.
[2066.40 → 2066.80] I don't know.
[2066.88 → 2067.48] What do you think?
[2068.78 → 2069.22] Yeah.
[2069.58 → 2071.72] Ashley's gophers are, there's how many?
[2071.90 → 2074.28] Like in your automated, you know, like
[2074.28 → 2075.60] billions in the gopher eyes.
[2075.66 → 2077.10] Oh, in gopher eyes me.
[2077.18 → 2078.12] Yeah, there are billions.
[2078.38 → 2081.32] I don't know how many combinations there
[2081.32 → 2081.98] are right now.
[2082.04 → 2083.98] I think I might have added some things, but
[2083.98 → 2084.56] billions.
[2084.56 → 2087.16] And I really like whoever did your artwork
[2087.16 → 2089.34] on your gopher sizes, John.
[2089.38 → 2091.38] I think it looks like Ashley-issue, but it could
[2091.38 → 2092.10] be someone else.
[2092.22 → 2092.74] Yeah, it's not me.
[2092.84 → 2096.34] I think that one was Marcus Olson is who I want
[2096.34 → 2096.60] to say.
[2096.76 → 2097.88] Yes, it was.
[2098.06 → 2098.36] Oh.
[2098.36 → 2098.84] Yes.
[2099.26 → 2100.50] I was going to say Ashley's who introduced me
[2100.50 → 2102.56] to him, but I've actually gotten into the habit
[2102.56 → 2104.64] of, so Ashley's usually really, really swamped.
[2105.04 → 2106.92] So I've gotten into the habit of trying to find
[2106.92 → 2109.68] different artists for all the courses because
[2109.68 → 2111.36] I like them to have a slightly unique feel.
[2111.86 → 2114.52] So like the testing course was Ego Aubrey, and I
[2114.52 → 2117.30] have an algorithms course that I'm working on that
[2117.30 → 2118.94] is another gopher in the community.
[2119.36 → 2120.38] I think it's Adrian.
[2120.62 → 2122.18] I'm drawing a blank on his last name though.
[2122.36 → 2124.18] And then I have another artist who's working on
[2124.18 → 2125.96] another course that's way down the pipeline.
[2125.96 → 2127.86] So like I'm trying to like to use different artists
[2127.86 → 2129.48] for all of them because I think it's cool to have
[2129.48 → 2130.78] different people drawing gophers.
[2131.34 → 2133.68] And I know that Ashley's just overwhelmed with
[2133.68 → 2133.88] stuff.
[2133.98 → 2135.82] So it's like, I don't want to like keep bugging
[2135.82 → 2136.06] her.
[2136.32 → 2138.96] But it just goes to show that I think when you are
[2138.96 → 2142.08] making content, whether that is for beginners or
[2142.08 → 2145.64] for anyone, you know, we are not a black and white
[2145.64 → 2146.68] or gray world, right?
[2146.70 → 2149.20] We are a world of colour, and we like visuals and we
[2149.20 → 2152.22] like fun, and we want, we learn better when we feel
[2152.22 → 2153.60] we're at play, right?
[2153.60 → 2156.30] So I remember Richard Feynman talking about how he
[2156.30 → 2159.28] bottled burnout and won a Nobel Prize for his
[2159.28 → 2160.16] Feynman techniques.
[2160.16 → 2161.96] We're kind of veering into physics, but still
[2161.96 → 2162.84] learning for beginners.
[2162.84 → 2164.98] And he always said, just keep a sense of play
[2164.98 → 2165.40] about you.
[2165.44 → 2168.08] And Ashley, that's what I love about the gophers
[2168.08 → 2170.14] that you bring to the table and to the community.
[2170.46 → 2172.96] And so anyway, Jared Santa, who's also part of the
[2172.96 → 2175.84] changelog crew said that they do an ELI five and
[2175.84 → 2178.66] explain it like you're five on the sister podcast
[2178.66 → 2179.30] JS party.
[2179.58 → 2181.54] That would be a great segment for go time.
[2181.54 → 2183.82] So if any of you are down to come back and do a
[2183.82 → 2186.72] repeat, but for four or five-year-olds by our inner
[2186.72 → 2189.08] five-year-olds, I'd love to do that episode.
[2189.32 → 2189.88] That'd be awesome.
[2190.14 → 2190.42] Yeah.
[2190.48 → 2190.70] Yeah.
[2190.70 → 2190.98] Same.
[2191.04 → 2191.80] I'm here for it.
[2197.50 → 2200.52] This episode is brought to you by our friends at
[2200.52 → 2203.60] Acuity, a new platform that brings fully managed Argo
[2203.60 → 2206.96] CD and enterprise services to the cloud or on premise.
[2206.96 → 2209.26] And I'm here with two of the co-founders from Acuity,
[2209.56 → 2212.14] Jesse Seen and Alexander Matrusenchev.
[2212.40 → 2214.96] So the Acuity platform is in beta right now.
[2215.18 → 2217.50] You guys have some big ideas you're executing on around
[2217.50 → 2220.68] Argo CD, managed Argo CD, Kubernetes native application
[2220.68 → 2222.58] delivery and the power of Git Ops.
[2222.64 → 2224.98] Help me understand the what and the why of what you're
[2224.98 → 2225.50] doing right now.
[2225.50 → 2230.10] So we started Acuity because we saw what was happening in the
[2230.10 → 2232.42] Kubernetes community, the challenges that people were
[2232.42 → 2234.86] facing about developer experience.
[2235.26 → 2238.98] And having run Argo CD for Intuit for a couple of years, we
[2238.98 → 2241.90] knew it took like a small team to build this and scale it and
[2241.90 → 2244.96] provide a performant solution for the developers.
[2245.46 → 2248.52] And so at Acuity and the Acuity platform, what we're trying to
[2248.52 → 2251.38] do is the first thing we're trying to do is actually provide
[2251.38 → 2255.18] Argo CD as a fully managed solution to our users.
[2255.18 → 2257.72] But that is just actually the start of things.
[2257.82 → 2262.70] And we actually want to take the next steps on improving the whole
[2262.70 → 2265.86] Git Ops and developer experience and providing new tools and
[2265.86 → 2268.66] ecosystems around Argo and the Argo project.
[2269.00 → 2269.80] Yeah, that's right, Jesse.
[2269.98 → 2273.96] So Argo CD is just the beginning, but every company eventually
[2273.96 → 2277.40] needs way more tools integrated into the DevOps platform.
[2277.78 → 2280.54] And that's what we're hoping to deliver with Acuity platform.
[2281.02 → 2284.26] So we're hoping to provide a great user interface that enable
[2284.26 → 2288.00] developers to achieve what they need in a matter of just a few clicks.
[2288.48 → 2291.34] But we also want to make Argo CD enterprise ready.
[2291.82 → 2296.80] What that means is our customers will get audits and insightful
[2296.80 → 2300.36] analytics out of the box without configuring anything.
[2300.86 → 2302.46] That's what we did at Intuit.
[2302.58 → 2304.40] And we learned that it was not so easy to do.
[2304.78 → 2307.60] And that's what we're hoping to solve for multiple organizations.
[2308.12 → 2308.38] Very cool.
[2308.46 → 2308.98] Thank you, Jesse.
[2309.14 → 2309.84] Thank you, Alex.
[2309.84 → 2313.02] Again, listeners, this is a closed beta.
[2313.30 → 2313.96] Check it out.
[2314.06 → 2316.76] Acuity.io slash changelog.
[2316.82 → 2319.72] Head there and see what this platform is all about.
[2320.04 → 2322.38] Again, Acuity.io slash changelog.
[2322.50 → 2324.10] Links are in the show notes.
[2324.56 → 2327.48] And by Honeycomb, find your most perplexing application issues.
[2327.78 → 2333.28] Honeycomb is a fast analysis tool that reveals the truth about every aspect of
[2333.28 → 2334.70] your application in production.
[2335.18 → 2339.16] Find out how users experience your code in complex and unpredictable environments.
[2339.16 → 2343.90] Find patterns and outliers across billions of rows of data and definitively solve your
[2343.90 → 2344.36] problems.
[2344.82 → 2346.28] And we use Honeycomb here at Change.
[2346.32 → 2350.14] Well, that's why we welcome the opportunity to add them as one of our infrastructure partners.
[2350.66 → 2354.84] In particular, we use Honeycomb to track down CDN issues recently, which we talked about
[2354.84 → 2357.96] at length on the Kaiden edition of the Ship It podcast.
[2358.20 → 2358.90] So check that out.
[2359.16 → 2359.62] Here's the thing.
[2359.88 → 2363.12] Teams who don't use Honeycomb are forced to find the needle in the haystack.
[2363.24 → 2366.40] They scroll through endless dashboards playing whack-a-mole.
[2366.40 → 2371.18] They deal with alert floods, trying to guess which one matters, and they go from tool to
[2371.18 → 2375.26] tool to tool playing sleuth, trying to figure out how all the puzzle pieces fit together.
[2375.62 → 2379.94] It's this context switching and tool sprawl that are slowly killing teams' effectiveness
[2379.94 → 2381.92] and ultimately hindering their business.
[2382.32 → 2388.36] With Honeycomb, you get a fast, unified, and clear understanding of the one thing driving
[2388.36 → 2389.08] your business.
[2389.32 → 2389.76] Production.
[2390.26 → 2392.76] With Honeycomb, you guess less and you know more.
[2392.76 → 2398.36] Join the swarm and try Honeycomb free today at honeycomb.io slash changelog.
[2398.48 → 2401.98] Again, honeycomb.io slash changelog.
[2401.98 → 2424.20] I kind of want to talk a little bit about learning mediums.
[2424.20 → 2429.34] So each of you has created or taught content in this new world of online.
[2429.34 → 2436.02] And so I would love to talk about your perspectives on pros and cons about each of these mediums.
[2436.08 → 2440.66] And so, John, we're talking about your gopher sizes with code accompanied by videos.
[2441.06 → 2442.70] Dave, this would be your online course.
[2443.22 → 2445.78] Workshops that you've given at events and conferences, Ashley.
[2445.96 → 2449.46] So what are some of the pros and cons about each of these mediums for beginners?
[2449.86 → 2451.46] I guess I can start with some of them.
[2451.76 → 2453.62] I like videos because you can show mistakes.
[2453.62 → 2459.26] I think it's important, especially for beginners, to see that even experienced developers make mistakes,
[2459.26 → 2462.80] but also to see how you get to derived code.
[2462.98 → 2465.94] Because I think there are a lot of times when we'll just show them the final code.
[2466.58 → 2470.42] And as developers, we know that there might be three refactors that got us there.
[2471.06 → 2475.50] And I think having a video makes it possible to do that versus if you're doing a book or
[2475.50 → 2478.94] something like that, it's much, much harder because to actually show them, well, I went to
[2478.94 → 2480.32] this line and changed this one thing.
[2480.32 → 2482.36] And then I went to this other file and changed this one thing.
[2482.46 → 2483.46] Like, it becomes a lot.
[2483.92 → 2487.28] So I think videos are perfect for that sort of interactive or not quite interactive,
[2487.42 → 2488.66] but, you know, something like that.
[2488.96 → 2494.12] But I've also started to find that books are probably more accessible, which is something
[2494.12 → 2498.94] that I hate about videos is that you almost need to find translators for a couple different
[2498.94 → 2503.22] languages, or you need to get somebody to come in and actually, like, write all the transcripts
[2503.22 → 2505.60] up because anything automated just doesn't do a good enough job.
[2505.60 → 2509.52] And so basically, that's something I've been struggling with lately is trying to figure
[2509.52 → 2513.36] out the right approach to that, because I think that making videos more accessible is
[2513.36 → 2515.34] something that needs to happen in the future.
[2515.88 → 2520.24] So one of the things that I think is important, because I recognize that my courses have reached
[2520.24 → 2525.00] 160 something different countries is having good closed captioning.
[2525.02 → 2527.62] And I have to admit right now, my Moline course doesn't have it yet.
[2527.62 → 2533.32] But to second John's thoughts around closed captioning, because some people, you know,
[2533.36 → 2537.50] they're coming off of, you know, where English may not be their native language.
[2537.62 → 2538.96] They speak several different languages.
[2538.96 → 2542.50] So having something there is extremely useful for them.
[2542.70 → 2546.32] But the challenge is, is that the automated closed captioning just doesn't work.
[2546.40 → 2551.90] I don't know how many times I've said Udemy, and it gets translated to you and me on the
[2551.90 → 2555.02] Udemy platform itself or something absolutely crazy.
[2555.02 → 2559.40] And I'm thinking if there's any word that Udemy would have right in their closed captioning,
[2559.44 → 2560.50] it would be Udemy, right?
[2560.76 → 2563.74] So that is a huge technical challenge and hurdle.
[2563.98 → 2568.84] But the other thing, you know, because I did have a background in teaching outside of this,
[2568.94 → 2574.28] where I've done some workshops in person in advance of this type of experience, as well
[2574.28 → 2581.30] as having tutored one on one, you lose that interaction when you have an online video.
[2581.30 → 2587.72] And it is extremely difficult to iterate and make changes and there are substitutes for it.
[2587.80 → 2590.20] But I like to see eyes, right?
[2590.26 → 2596.10] And even just hello and putting content out there into the world is a very different platform
[2596.10 → 2599.28] when you're doing a static video than when you're recording.
[2599.38 → 2604.12] I think ideally what I'd almost prefer to do as I grow and continue to make new courses
[2604.12 → 2607.38] is to teach in a live event, record those.
[2607.38 → 2610.02] So at least I've got somebody else I'm talking to.
[2610.16 → 2615.30] And if you see that deer in headlights look, you get that sense of, oh, okay, I've fallen
[2615.30 → 2616.02] off track here.
[2616.18 → 2620.52] I need some more explanation here because it was a very different approach.
[2621.02 → 2624.10] Mind you, you get unlimited redos when you're recording video, right?
[2624.14 → 2627.32] So it's, oh, that was, I needed more coffee or something, right?
[2627.32 → 2632.76] So there's pros and cons of each, but it's a very, everyone has its own flavour and piece
[2632.76 → 2633.24] to it, right?
[2633.24 → 2637.48] I feel like every way that we do this is valuable.
[2637.90 → 2640.02] We all have different learning styles.
[2640.20 → 2643.88] For me, it's hard for me to consume the content on video.
[2644.06 → 2648.16] I'm like, okay, now I have to pause the video and do this step, play the video again.
[2648.30 → 2649.22] And then I go back.
[2649.26 → 2650.56] I'm like, did I do that step right?
[2650.66 → 2653.10] So for me, I like step-by-step instructions.
[2653.74 → 2658.82] And so the workshops are really helpful, but the cons of a workshop is that a lot of people
[2658.82 → 2660.64] are afraid to ask questions.
[2660.74 → 2665.14] So they will sit there and act like they know what's going on when they don't know what's
[2665.14 → 2665.66] going on.
[2665.66 → 2668.94] So we have to constantly go around and be like, do you really understand?
[2669.26 → 2670.34] You can ask questions.
[2670.50 → 2671.18] It's fine.
[2672.00 → 2678.34] So video, written tutorials, workshops, they're all valuable in their own way.
[2678.40 → 2679.38] We all learn differently.
[2680.16 → 2684.26] Just to chime in one additional, like one of the reasons I have never focused on workshops,
[2684.38 → 2685.78] conferences, that sort of stuff as much.
[2685.78 → 2689.02] And I think it's easy to forget when you live in a city, but if there's a lot of people
[2689.02 → 2693.60] who live nowhere near a city, or they don't have the resources to pay for a workshop or
[2693.60 → 2697.82] something, like to give you an example, I live two hours away from the nearest city and that's
[2697.82 → 2699.76] Pittsburgh, which is not exactly a massive city.
[2700.26 → 2703.80] So, you know, just knowing that there's a lot of people out there who cannot go to that
[2703.80 → 2704.34] type of thing.
[2704.44 → 2708.04] I definitely think that there's a good, like you said, we need almost everything because
[2708.04 → 2711.60] some people are going to do better in the workshops and some people will meet more people
[2711.60 → 2713.16] and they'll actually collaborate with them afterwards.
[2713.16 → 2715.62] Other people will do online courses.
[2716.08 → 2719.76] I think one of the big things I've just noticed is that people find other people to collaborate
[2719.76 → 2720.76] with and to learn with.
[2720.84 → 2722.10] That's very, very huge.
[2722.98 → 2730.04] So like collaboration in person, looking or gauging for like deer in the headlights, course
[2730.04 → 2730.50] correcting.
[2731.08 → 2733.48] That's typically been the traditional way of learning, right?
[2733.52 → 2737.76] But it doesn't scale and doesn't scale the teacher, and it's not accessible to, you know,
[2737.82 → 2739.54] rural and suburban learners.
[2740.00 → 2740.96] I think it can scale.
[2740.96 → 2742.08] It just scales differently.
[2742.46 → 2746.18] Like one way I've seen it scale is I've seen people who do online courses, and they'll
[2746.18 → 2750.02] essentially have, they call them classes or whatever, but essentially a bunch of people
[2750.02 → 2755.50] sign up, and they say like, all right, we're going to start in maybe December and every
[2755.50 → 2758.58] week you're supposed to go through so much content, and then you're all like in a Slack
[2758.58 → 2761.74] channel or something, and you discuss that content, and you're sort of expected to keep
[2761.74 → 2763.44] up with the classroom on that content.
[2763.70 → 2767.86] It's less acceptable in the sense that you can't just start whenever you want.
[2767.86 → 2771.64] But I think there are ways to sort of get that simulated classroom environment.
[2772.16 → 2774.94] And I think that's, you know, as course creators, it's things we have to think about.
[2775.00 → 2777.02] Like, is there a way that we can make that possible?
[2777.32 → 2779.76] I think tools like Slack have made it much, much better too.
[2780.28 → 2783.92] Like I've gotten into this habit of like all the courses I have, I provide support for,
[2784.34 → 2786.40] but I've gotten into this habit of the paid courses.
[2786.40 → 2790.36] If you, you got access to a Slack and I basically say, ask your question there.
[2790.36 → 2794.16] Even if you email it to me and I can answer in five seconds, I say, ask there
[2794.16 → 2797.72] because this is the best way to foster this growth between different people taking the
[2797.72 → 2798.06] courses.
[2798.06 → 2800.64] Like you each try to answer the questions and help each other out.
[2800.76 → 2802.80] And that will, you know, establish that learning.
[2802.90 → 2804.68] It'll help you like get used to helping each other.
[2804.96 → 2808.92] And over time, it's gotten to this point where I can sometimes check the Slack and somebody
[2808.92 → 2811.52] will have asked a question and somebody will have answered it better than I could have before
[2811.52 → 2812.30] I even got to it.
[2812.66 → 2813.34] Oh, that's great.
[2813.34 → 2814.30] Yeah, that's always great.
[2814.38 → 2817.98] The feedback loops and in-person for me is where I can get unblocked.
[2818.02 → 2823.16] And I know that the other exercise site that I've tried is exorcism.io for not just Go,
[2823.22 → 2824.28] but a variety of languages.
[2824.84 → 2826.72] And I was a mentor for Go.
[2826.94 → 2832.22] And so when I signed on to be a mentor, they were like, listen, if you agree to sort of walk
[2832.22 → 2837.90] through the code exercise, we all kind of as a community try to get the next person in
[2837.90 → 2840.38] the queue so that their feedback is as quick as possible.
[2840.38 → 2845.62] So there was that like online mentorship and trying to scale that differently, as you said.
[2846.06 → 2847.94] So I love exorcism.io.
[2848.46 → 2850.22] Thanks, Katrina and team.
[2850.98 → 2855.84] Also, I feel like I need to mention it because it's great, and we haven't talked about it yet,
[2855.84 → 2857.82] but just for funk, I love it.
[2858.10 → 2858.30] Yeah.
[2858.76 → 2863.70] And I just wanted to ask John before I kind of talk about other possible resources for
[2863.70 → 2864.24] gophers.
[2864.24 → 2868.56] Can you tell us a little bit more about where learners could go for gopher sizes?
[2868.80 → 2873.88] Are they going to get that content for asking questions within the course as they sign on?
[2874.38 → 2877.48] So gopher sizes, there's a channel in the gopher Slack.
[2877.62 → 2877.80] Okay.
[2878.18 → 2879.12] Hashtag gopher sizes.
[2879.62 → 2880.64] And there's some people there.
[2880.70 → 2882.10] I don't know if that one's actually that active.
[2882.44 → 2885.12] That one's a little bit harder because it's not paid.
[2885.28 → 2887.06] So supporting, it's a little bit trickier.
[2887.32 → 2889.88] And people email me and I do try to answer where I can.
[2889.88 → 2893.70] You know, in the Slack, if they ask questions, I think I try to check there every so often
[2893.70 → 2894.24] and respond.
[2894.72 → 2898.82] So all those are options because I think that one right now has something like 20,000 students
[2898.82 → 2902.92] and it can be a little bit trickier sometimes whenever I've got a bunch of other things
[2902.92 → 2903.42] I have to do.
[2903.92 → 2906.74] But I do try to help, and I do try to answer email and that sort of stuff.
[2906.80 → 2908.18] So like those are all viable options.
[2908.66 → 2908.76] Great.
[2909.22 → 2910.96] Well, we're about 10 minutes out.
[2911.36 → 2915.24] Let's go beyond Hello World or go 101 and go 201.
[2915.94 → 2917.62] So we can start to name.
[2917.62 → 2921.26] So we have a great foundational course, and we have exercises.
[2921.66 → 2925.94] Where else can go beginners go next once they get there?
[2926.12 → 2927.10] I'll jump in there.
[2927.18 → 2930.82] So one of the, you know, once you've sort of got your head around some basic go, you've
[2930.82 → 2934.24] done lots of different examples, and you have the basic language across.
[2934.46 → 2939.88] I think at that point, you know, jumping into effective go in terms of learning how to write
[2939.88 → 2943.58] good, clean, idiomatic go code is your very next step.
[2943.68 → 2947.30] And then as Ashley was mentioning, you know, and we were talking about building examples,
[2947.30 → 2953.28] another item I think that is fantastic, which is similar to awesome Python is awesome go.
[2953.28 → 2959.10] And if you go to awesome hyphen go.com, you'll end up with a list of, you know, curated go
[2959.10 → 2960.74] frameworks, libraries and software.
[2961.30 → 2965.32] And, you know, anything that floats your boat, you know, whether you're interested in audio
[2965.32 → 2970.86] and music or bot building or, you know, any kind of different piece, there are some really
[2970.86 → 2973.70] outstanding resources available there.
[2974.30 → 2978.56] And then finally, I think, you know, the third thing I'd lead off with in that respect would be
[2978.56 → 2980.44] to go user groups, right?
[2980.52 → 2986.62] Because almost any geography that you're in, either there are online forums or in-person groups,
[2986.68 → 2990.66] especially the in-person groups, you'll find, you know, that there are go user groups.
[2990.66 → 2991.66] There's a go user group.
[2992.02 → 2998.00] I live in a fairly small city in Canada called Winnipeg, which is smack central in the prairies.
[2998.50 → 3001.00] And yet we have a thriving go user group locally.
[3001.78 → 3006.86] And so, you know, unless you're rural, you may be able to find, you know, where you can
[3006.86 → 3010.62] crash a go user group, even if you're travelling and to connect with go users in person, which
[3010.62 → 3011.48] I think is amazing.
[3012.12 → 3013.54] Plus one to go user groups.
[3013.98 → 3018.98] Yeah, we're actually trying to build that up and strengthen a unified go user group, if
[3018.98 → 3020.58] you will, called the Go Developer Network.
[3020.74 → 3024.44] So I joined Google a couple of months ago, and I have another colleague that joined the
[3024.44 → 3025.10] team recently.
[3025.24 → 3026.12] His name is Van Riper.
[3026.88 → 3032.82] And he wants to complement Go Bridge's efforts, as well as Women Who Gos efforts, into sort
[3032.82 → 3038.02] of getting this network of groups to be able to maybe give them content, help them maybe
[3038.02 → 3041.78] something like a live broadcast, give them a chance to go at their own pace.
[3041.88 → 3046.40] But I really like the idea of community and the importance of in-person learning and trying
[3046.40 → 3050.84] to balance that off with the people for whom maybe online courses are not working.
[3051.20 → 3054.26] I think it's a perfect thing that that's something you focus on.
[3054.70 → 3057.36] Because like we talked about all these things with learning languages, but we didn't really
[3057.36 → 3061.54] talk about the community or the fact that like some coding communities really weren't
[3061.54 → 3062.80] that inclusive or inviting.
[3063.40 → 3067.64] And I think the fact that Go has stressed that from the start is one of the huge things
[3067.64 → 3071.00] for learning it, at least as a, you know, especially if you happen to be in a minority group
[3071.00 → 3075.52] or something that can be very helpful that you can actually feel okay being yourself and
[3075.52 → 3077.42] not having to pretend you're somebody else's you're learning.
[3077.78 → 3078.16] Absolutely.
[3078.42 → 3081.72] That's why I moved from Python to Go.
[3082.30 → 3084.46] Python community is fine.
[3084.72 → 3090.54] But so I found that within the Go community, there is no such thing as a dumb question.
[3090.54 → 3093.58] And I am really, perfect at asking dumb questions.
[3094.22 → 3096.64] And people are just super, super helpful.
[3096.78 → 3098.62] They will go out of their way to help you.
[3098.62 → 3102.80] I have never been part of a community like this.
[3103.52 → 3103.76] Agreed.
[3104.10 → 3106.78] And it's the reason why I chose Go and stuck with Go.
[3106.96 → 3108.62] And I just really am happy for that.
[3108.76 → 3111.00] So yeah, thank you, John, for bringing that up.
[3111.02 → 3115.58] Because it is, I feel, of paramount importance in terms of learning the language, mastering
[3115.58 → 3119.42] the language, and then staying and keeping and communicating to the language.
[3119.70 → 3122.34] One thing you mentioned, Dave, was Awesome Go.
[3122.48 → 3126.30] There's also Go or Lib Hunt, which I think works for all languages.
[3126.30 → 3130.18] And then they have go.libhunt.com, which is a similar thing, right?
[3130.22 → 3135.62] You can go see third-party packages and kind of compare them to other packages depending
[3135.62 → 3136.58] on what you want to do.
[3137.08 → 3139.06] They sort of release the newest, greatest.
[3139.42 → 3142.36] And I kind of like that to keep up with my things.
[3142.52 → 3146.22] I know that Mark Bates, who is a panellist on the show, along with Corey Lanose, they made
[3146.22 → 3147.22] Go for Guides.
[3147.22 → 3152.42] And I think this is kind of along those same lines of trying to find a path or a curated
[3152.42 → 3156.96] path based on a certain thing that you want to learn, whether that's a data structure or
[3156.96 → 3158.20] a type or an algorithm.
[3158.64 → 3160.80] So I'm going to give a little shout-out to them for that.
[3161.44 → 3165.56] Any other resources for people to go or their go-to, pun intended?
[3165.72 → 3168.70] We've been very short on go puns this episode.
[3168.94 → 3169.58] Shame on us.
[3169.58 → 3173.66] I think one that everybody always says, and it's very hard, but if you can find an open
[3173.66 → 3177.96] source project you like, it can be daunting at first because you'll be like, how do I
[3177.96 → 3178.56] get started here?
[3178.62 → 3179.46] There's so much there.
[3179.70 → 3180.98] But you mentioned Mark Bates.
[3181.08 → 3185.36] I think one of the things that he's done a great job with Buffalo is that he can help
[3185.36 → 3188.40] people get started and be like, just help with documentation or help with something
[3188.40 → 3191.04] that's relatively easy as you get familiar with stuff.
[3191.54 → 3195.70] But that one comes to mind because there were one or two people that were very, very early
[3195.70 → 3197.68] students of one of the courses I made.
[3197.68 → 3201.66] And they later were telling me that they were actually contributing pretty like more heavily
[3201.66 → 3202.54] to those projects.
[3202.54 → 3206.88] And it was because they really helped them grow as a developer and learn more about them
[3206.88 → 3209.04] and get to the point where they could actually fix PRs.
[3209.48 → 3211.08] And it's not going to happen overnight.
[3211.32 → 3215.48] I don't think you can ever as a beginner jump into a project and make meaningful code changes
[3215.48 → 3217.00] or big code changes.
[3217.26 → 3221.98] And people who run open source projects have to resist this urge to fix a one line bug.
[3222.38 → 3224.88] They sort of have to set it aside for a beginner to tackle.
[3224.88 → 3230.00] But if you can find the right projects and maybe ask around in the Go community for suggestions,
[3230.00 → 3234.96] that's a great way to grow where you just gradually do small changes and work your way up to handling
[3234.96 → 3236.06] more and more of the code base.
[3236.52 → 3236.84] I agree.
[3236.96 → 3238.86] That is advice I give often.
[3239.66 → 3245.92] And what I would like to see in the future is people prioritizing PRs.
[3246.00 → 3248.00] Like, here's what's great for a beginner.
[3248.30 → 3250.32] Here's what's great for people that are more advanced.
[3250.46 → 3252.26] There's a site called Up4Grabs.
[3252.26 → 3253.62] It's not .com.
[3253.70 → 3255.06] I can't remember what it is.
[3255.10 → 3260.16] But it does just that, where it's like, these are great bug fixes that you can do as a beginner.
[3260.62 → 3261.98] And so it will rank things.
[3262.12 → 3264.98] I would love to see people do that within open source in general.
[3265.40 → 3265.64] Yeah.
[3265.84 → 3269.06] I love when GitHub tags, like, great first issue.
[3269.26 → 3271.34] And then you can just kind of sort by the tags.
[3271.34 → 3286.26] And then they've optimized their project, not for getting things done necessarily, but for, well, yes, that's certainly important, but also for being inclusive and trying to onboard new members into their project or their ecosystem and whatnot.
[3286.72 → 3293.30] Another one is first timers only, where basically they limit specific issues, and you have to be a first time contributor to that project to do it.
[3293.48 → 3294.28] Oh, that's nice.
[3294.46 → 3294.78] Love it.
[3294.78 → 3299.76] And we would be remiss if we didn't mention Golang-Newbies channel in the Gopher Slack.
[3299.94 → 3305.20] When I first began, I just loved being able to ask, as Ashley said, all the questions.
[3305.48 → 3310.66] And I was sort of fearless because I had people that I already had met in person that said, just ask the question.
[3310.78 → 3316.48] And when you do, if you do that, then it will make people more comfortable in asking what they are afraid of to ask questions.
[3316.78 → 3318.90] So, yes, Golang-Newbies and Gopher Slack.
[3318.90 → 3328.76] It's funny because that reminds me of before Go Time got rebooted, I was talking to Matt Refer, and he had said that one of his goals was to say, I don't know in the podcast at least once or twice.
[3329.30 → 3334.12] And his goal for that was basically just so beginners realize that it's okay to admit you don't know and to ask questions.
[3334.54 → 3342.00] And I think that's important, like you said, just to really reinforce that it's okay to ask questions and that nobody's going to think you're a bad developer or something because of it.
[3342.10 → 3342.38] Yes.
[3342.74 → 3345.12] No, and there's so much that Matt doesn't know.
[3345.12 → 3349.30] We had to throw Matt some shade.
[3349.50 → 3355.04] So, I think our issue, our episode is quasi-complete because we have thrown Matt some shade.
[3355.14 → 3356.30] We've given Steve a hello.
[3357.12 → 3359.94] We mentioned Mark and his Gopher guides.
[3361.12 → 3362.98] Anything else we're missing before we go?
[3363.22 → 3374.40] Well, just to add on the question piece, one thing I notice, you know, with the courses that I teach, so often someone asks a question and the next thing you know, there's a crowd of Me Too's.
[3374.40 → 3376.42] And I'm like, where were you a minute ago?
[3376.70 → 3381.32] You know, like, you know, why did, you know, so-and-so have to be the first one to ask?
[3381.46 → 3388.70] And then inevitably when the answer, you know, is made, you get a handful of a dozen or so thank yous.
[3388.74 → 3394.26] And you're like, you know, make it interactive, especially when you're trying to bring, you know, that about.
[3394.58 → 3399.70] I really find that people are unnecessarily shy for whatever reason.
[3400.32 → 3402.22] It's not even unnecessarily shy.
[3402.22 → 3408.26] I think that people's fear of embarrassment rules them, right?
[3408.40 → 3409.38] It's all psychological.
[3409.62 → 3414.72] So there has to be somebody in the room who just doesn't embarrass by not knowing something.
[3415.10 → 3415.18] Yeah.
[3415.28 → 3425.22] I think it's also how you answer can make a huge impact because if you make it sound like it was something obvious or another example is like if somebody says like, well, I'm not sure, but I want to try to help you.
[3425.22 → 3429.48] And if you just jump in and just disregard everything they said, then they're not going to try that in the future.
[3429.72 → 3439.42] So like I think there's a lot of thinking about how we answer questions and how we present stuff to people and just trying to be as, I don't know, gentle or friendly as possible is very important.
[3439.98 → 3440.42] Absolutely.
[3440.72 → 3441.18] Very good.
[3441.52 → 3448.10] Definitely encourage those people to ask more questions might open it up for other people to ask questions.
[3448.10 → 3448.54] Great.
[3449.58 → 3452.26] Well, we're kind of coming up on the top of the hour.
[3452.40 → 3454.88] There are a couple of things I wanted to mention.
[3455.34 → 3459.86] First, there's one last segment that I'm really interested in learning more about.
[3459.98 → 3465.10] And I made a survey because I'm just going to like I am not a survey designer, but I really am curious.
[3465.56 → 3470.94] How many of you here on this panel have had to learn a new programming language while on the job?
[3470.94 → 3471.68] I have.
[3471.96 → 3472.16] Yeah.
[3472.38 → 3482.68] And is learning while on the job, whether it's because you have to or you're exploring for, you know, new tooling or because it's, you know, a change in the technical stack?
[3482.78 → 3489.22] Like how does learning or beginning from that headspace any different from learning maybe on your own time?
[3489.86 → 3495.76] I feel like it's different because usually if it's for work, you know why you need to learn it.
[3495.96 → 3496.16] Okay.
[3496.68 → 3500.10] So you kind of have some base knowledge, right?
[3500.10 → 3506.06] So you're like, I have to learn it because I need to build this feature, or we're building this tool and that's why I have to learn it.
[3506.12 → 3508.14] So you can Google more specifically.
[3509.28 → 3509.64] Okay.
[3510.34 → 3511.20] John, Dave?
[3511.34 → 3512.48] I've had to learn on the job.
[3512.88 → 3520.02] And I think like Ashley said, it's specifics, but it's also like your focus is on being productive, not academic learning.
[3520.32 → 3525.66] So that forces you to not let yourself get distracted as much, I guess, is the best way to put it.
[3525.66 → 3535.00] You know, so like if you need to build a web server, whatever, a WebSocket server or something, you're going to focus more on, I just need to get this done, and I can come back and fine tune it later.
[3535.00 → 3537.48] Or I can come back and look at those things I'm not quite sure about later.
[3537.48 → 3543.70] Whereas when you're learning it just, you know, for leisure, it's, there's no really like time restrictions or anything.
[3543.70 → 3545.84] So you have a little bit more ability to get distracted.
[3546.14 → 3555.22] Well, I think that getting distracted is the enjoyment that you have when you decide to explore something in your own personal time for your own personal benefit.
[3555.32 → 3555.52] Right.
[3555.58 → 3556.64] You can go down those rabbit holes.
[3556.78 → 3557.46] You can explore.
[3557.72 → 3559.78] It's almost like a buffet of knowledge.
[3560.24 → 3562.24] And I love reading and learning.
[3562.36 → 3567.78] I listen to a lot of podcasts because I want to experience those tangential things that I may not otherwise have.
[3567.78 → 3580.36] But I mean, I will say, even though programming isn't a day-to-day part of my job, I think anyone in IT or anyone in the world in general can literally have what happened to me this recent Friday where the CIO called the boss.
[3580.36 → 3580.70] Right.
[3580.72 → 3583.12] And said, I want Dave full-time on this other project.
[3583.62 → 3586.08] Whatever he's doing right now goes away.
[3586.16 → 3586.48] Right.
[3586.52 → 3588.56] And the next thing you know, it's OK.
[3588.84 → 3596.60] So let's figure out, you know, how we're going to approach this and what I need to do there and what his objectives are and how do I fulfill those?
[3596.60 → 3600.68] So it's very pointed because you're trying to get to a particular objective.
[3600.68 → 3607.82] But the pleasure of just learning something for kicks and giggles sometimes can be there's a joy with that as well.
[3607.86 → 3608.18] Right.
[3608.22 → 3613.02] And it's different from when you're trying to fulfill, you know, what the CIO asked on a Friday morning.
[3613.18 → 3613.62] Yeah.
[3613.80 → 3614.14] Yes.
[3614.32 → 3617.80] I guess I should say those distractions, like you said, can be very good things.
[3617.80 → 3622.26] But I just think that's one of the big differences is that, like, sometimes they're good, sometimes they're bad.
[3622.26 → 3629.90] And I think that having them there, it's just being one of the big differences for me is I just felt like in the work environment, I never was.
[3630.30 → 3633.74] I never had that freedom to just really go look at the stuff, explore things.
[3634.08 → 3636.98] You know, you can't like go compare three different HTTP routers.
[3637.08 → 3638.42] It's like I just need to pick one and use it.
[3638.64 → 3639.08] Exactly.
[3639.24 → 3643.40] No, you definitely get less in the weeds when it's for work.
[3643.66 → 3644.22] Very cool.
[3644.36 → 3646.08] I want to hear more about this.
[3646.08 → 3649.40] I am going to put a link in the chat.
[3649.80 → 3653.00] It's bit.ly slash on job code survey.
[3654.00 → 3657.36] And I just I'm going to share it on my Twitter and maybe everyone else can share it.
[3657.42 → 3659.82] I just want to know because that's kind of my one.
[3660.24 → 3661.30] How is that different?
[3661.56 → 3669.96] And are there any gaps out there in the ocean of content that you think that need to be most filled at this point as we close out?
[3670.32 → 3670.88] Children's book.
[3671.16 → 3671.74] Dang it.
[3672.08 → 3672.50] All right.
[3672.60 → 3674.02] I think that's what is happening.
[3674.42 → 3675.14] Children's book.
[3675.14 → 3676.06] It is happening.
[3676.44 → 3677.60] Please do it.
[3677.76 → 3681.98] Brian Kettle son and I were supposed to do it, but we are just far too busy.
[3682.74 → 3684.88] I really need somebody to do this.
[3685.12 → 3686.78] Just selfishly, please do it.
[3687.40 → 3687.80] Amazing.
[3688.40 → 3693.60] I almost feel like there needs to be resources teaching people how to ignore all the bad advice they're going to get.
[3693.82 → 3700.60] Like Ashley had said, people keep telling you to build something or like if you get on the go Reddit, they're going to tell you never to use third party libraries or like there's just right.
[3700.88 → 3702.02] There are a lot of things like that.
[3702.02 → 3706.88] And I think when you're learning, especially as a beginner, it's really easy to get suckered into this.
[3707.02 → 3708.22] I need to use all these things.
[3708.86 → 3710.42] And I don't know.
[3710.50 → 3716.90] It's almost like they need a guide to like a practical guide to just ignoring all that other stuff that doesn't matter and just focusing on what does matter.
[3716.90 → 3717.26] Yes.
[3717.44 → 3717.74] Yes.
[3717.78 → 3718.82] Also, please write that.
[3719.50 → 3719.86] Yes.
[3719.96 → 3724.30] I have that as a survey question, which is like, what is this like letter to your past self?
[3724.42 → 3728.76] Like what do you wish that you didn't have to unnecessarily go through?
[3728.88 → 3729.58] So, yeah, totally.
[3730.08 → 3730.66] I think that's great.
[3730.72 → 3733.46] I wonder if we, I wish we had more time to discuss that.
[3733.52 → 3735.44] But that is just really some of the best.
[3735.50 → 3739.56] If we can sort of get rid of some of the headaches that we ourselves had to endure.
[3739.56 → 3741.88] Eh, maybe that's all part of the journey.
[3742.98 → 3744.94] So let's, I'm going to close out.
[3745.10 → 3751.26] Whatever kind of beginner you are, we hope this episode has given you a good starting point as you start to learn and improve your go.
[3751.68 → 3761.22] The learning gotchas, how learning go might be different from your current programming language, where to ask questions and get help from the community, and where to continue on your learning journey.
[3761.82 → 3765.12] Whatever you do, embrace failure and don't stop trying.
[3765.64 → 3766.54] Engage with others.
[3767.16 → 3768.78] Use your resources.
[3768.78 → 3770.22] Go for Slack.
[3770.54 → 3771.30] Go Lang Newbies.
[3771.80 → 3773.90] Attend meetups online or in person.
[3774.50 → 3778.58] Like the famous quote from Benjamin Franklin, tell me and I forget.
[3779.22 → 3780.60] Teach me and I may remember.
[3781.14 → 3782.36] Involve me and I learn.
[3782.72 → 3785.58] Thanks everyone for today's episode of Go Time FM.
[3786.12 → 3787.12] Thank you, Ashley.
[3787.38 → 3788.18] Thank you, John.
[3788.32 → 3789.92] Thank you, Dave, for joining me.
[3790.20 → 3791.18] We'll see you next week.
[3795.14 → 3797.70] Thank you for listening to this episode of Go Time.
[3797.70 → 3802.98] If you liked this oldie but goodie, it's from our list of recommended episodes.
[3803.38 → 3806.42] Find the rest at gotime.fm slash recommended.
[3806.98 → 3809.50] And of course, subscribe now if you haven't already.
[3809.80 → 3813.52] We are in all the podcast apps or on the web at gotime.fm.
[3813.52 → 3817.34] And if you enjoy the show, please tell a friend to give us a listen.
[3817.54 → 3820.60] It's the best way you can help Go Time grow and thrive.
[3821.00 → 3829.48] Thanks again to our partners at Vastly for Coming for us, to the mysterious Break master Cylinder for these fresh beats, and to you for listening.
[3829.84 → 3830.66] We appreciate you.
[3830.66 → 3836.16] Next time on Go Time, Natalie talks debugging Go with some new friends.
[3836.52 → 3839.50] We'll have that episode ready for your ear holes next week.
[3839.50 → 3854.28] Game on.
