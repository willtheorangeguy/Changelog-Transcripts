[0.00 → 11.30] Now, Nick, Ball pointed out what was one of his strongest points was the hypocrisy of your argumentation, which is why I assigned you on that team is that you almost entirely only build single page apps, right?
[11.36 → 11.78] Day to day.
[12.18 → 12.32] Yep.
[12.58 → 15.56] So you don't actually think they're a big mistake or you just.
[15.70 → 16.22] Oh, no, I do.
[16.48 → 16.86] Oh, you do.
[18.36 → 18.98] Oh, OK.
[19.36 → 21.36] So you're just making a big mistake every day.
[21.42 → 22.04] No, no, no, no.
[22.04 → 28.34] I think that in a lot of ways we do overcomplicate everything, and we do have to re-architect a lot of stuff.
[28.34 → 35.10] And it's just a lot more that's put on my plate to maintain and make sure it's working when I could be off solving more important problems.
[35.26 → 37.48] But I do think that they have their place for sure.
[37.72 → 39.28] I do like working with them.
[39.40 → 45.90] Take right now, we're recording this podcast in a web app, and it's on a single page and it works fantastically.
[50.48 → 53.84] This episode is brought to you by our friends at Ray gun.
[53.84 → 59.06] They give software teams instant visibility into the quality and the performance of their software.
[59.54 → 62.94] And I'm here with John Daniel Track, co-founder and CEO of Ray gun.
[63.26 → 68.56] JD, talk to me about the joy a team feels when they're able to find and resolve an issue,
[68.72 → 74.32] even before a customer has a chance to get upset or reach out to support about the issue.
[74.66 → 75.30] Talk to me about that.
[75.58 → 78.56] Well, I find it pretty exciting to be able to hit it off early.
[78.56 → 84.10] So, and being able to tell people that you resolved something, so maybe they come through, you know, and they do report an issue.
[84.36 → 87.20] And you can say, cool, we don't need to ask you for any more context.
[87.44 → 89.66] We've got all the details, and can have this fixed tomorrow.
[89.94 → 92.94] It turns an at-risk customer into an absolute raving advocate.
[93.20 → 94.26] So that's a huge win.
[94.40 → 98.60] And then the other thing that was a little bit embarrassing, we launched Ray gun, but we had these other products.
[98.76 → 99.86] And we instrumented them.
[99.86 → 104.62] And that's when we realized this less than 1% of our users would ever actually report a problem.
[105.04 → 107.74] And so you're sitting there thinking your software is actually not bad.
[107.80 → 110.58] And actually, it's really, terrible.
[110.66 → 113.74] And that's hurting all of your conversion rates, business performance.
[113.90 → 115.04] These aren't really dev tools.
[115.12 → 116.34] They're actually business tools.
[116.90 → 117.02] All right.
[117.02 → 121.80] If you want to see how this dev tool impacts the entire business, head to raygun.com to learn more.
[122.08 → 124.02] And start your 14-day free trial.
[124.12 → 125.48] No credit card required.
[125.48 → 133.04] Join thousands of customer-centric software teams who use Ray gun every single day to deliver flawless experiences to their customers.
[133.20 → 134.98] Again, raygun.com.
[145.12 → 151.10] This is JS Party, your weekly celebration of JavaScript and the web.
[151.10 → 155.38] We have another extended episode for Changelog++ members.
[155.68 → 158.52] This time, we're putting the pre-show into the post-show.
[158.76 → 160.18] That'll get you a little closer to the metal.
[160.40 → 161.52] And of course, no ads.
[161.90 → 165.20] Join today at changelog.com slash plus.
[165.72 → 171.10] Special thanks to our longtime partners at Vastly for shipping JS Party superfast to wherever you listen.
[171.34 → 173.04] Check them out at fastly.com.
[173.20 → 174.56] Okay, let's do this.
[174.88 → 175.86] It's debate time, you all.
[175.86 → 184.74] Hello, hello.
[185.22 → 186.62] Jared here, your internet friend.
[186.92 → 189.72] We are back for another awesome JS Party.
[189.80 → 191.84] We've lined up a debate episode.
[192.06 → 197.02] Now, we've been doing debates off and on over the years, but we haven't done one for a very long time.
[197.02 → 212.58] And that's because we didn't have a great premise to debate until recurring guest Chris Ferdinand provided one on his blog when he wrote back in February that Spas, that single page apps, were a mistake.
[212.58 → 218.18] So, I hopped on that real quick and decided, ooh, that sounds like a premise that we could debate.
[218.66 → 222.04] And I wanted to be more bombastic, and so I added the word big.
[222.72 → 227.72] And so the debate, the premise is, were Spas a big mistake?
[228.52 → 233.10] And I'm sure Divya will hop on that jargon and decide exactly what big means.
[233.16 → 235.14] Speaking of Divya, she's joining us today.
[235.18 → 235.62] What's up, Divya?
[236.12 → 237.08] Hey, how's it going?
[237.56 → 238.70] Got your debate shoes on?
[239.02 → 239.80] I'm wearing socks.
[239.80 → 241.36] I got my debate socks on.
[241.54 → 242.54] Okay, right on.
[242.84 → 244.16] No shoes in the house.
[244.32 → 246.26] I hope those work just as well.
[246.84 → 250.24] And Divya's teammate today will be Nick Nisi.
[250.46 → 250.96] What's up, Nick?
[251.24 → 251.86] HOI, HOI.
[252.26 → 258.08] I'm very excited, but I was ready to debate spas, like, as in a place where you go for a day.
[258.10 → 258.56] A day spa?
[259.08 → 259.36] Yeah.
[259.60 → 261.44] There's no way a spa could be a mistake, though.
[261.64 → 262.62] Never a mistake.
[262.70 → 263.12] I don't know.
[263.14 → 263.96] It's always the right choice.
[264.14 → 265.74] How would you argue that they're a mistake?
[266.68 → 268.04] They're germ-ridden.
[268.26 → 268.50] Okay.
[268.50 → 269.40] Oh, fair, fair.
[269.44 → 269.76] I don't know.
[270.72 → 271.46] Fair, fair.
[272.08 → 272.40] Expensive?
[273.16 → 273.82] Expensive, yeah.
[274.26 → 275.82] Strangers touching your body in places?
[276.10 → 276.46] I don't know.
[276.50 → 277.06] It could be a mistake.
[277.16 → 278.90] You can get there and think, why did I do this?
[279.08 → 282.94] Now all of my arguments are just going to be, like, double entendres.
[283.96 → 284.32] Okay.
[284.50 → 285.38] We'll hold you to that.
[286.08 → 293.04] Well, Team Divya and Nick will be facing off against Team K-Ball and Abel, only without
[293.04 → 295.70] Abel, because construction problems at Mel's house.
[296.04 → 297.92] K-Ball, you're representing all by yourself.
[297.96 → 298.48] How are you going to do?
[298.48 → 302.74] Well, you know what I was thinking I would do is not just channel Abel, but I'm going
[302.74 → 308.94] to channel the ghosts of all the JS Party participants who aren't here today.
[308.94 → 316.10] We have some folks who have done amazing jobs in previous Yep, Nope episodes, and I'm going
[316.10 → 324.06] to see if I can dig up some callbacks and represent all of our panellists as Yep, Nope.
[324.28 → 324.56] Okay.
[324.56 → 328.22] And especially because we're on Nope, and we got a lot of cynics on JS Party.
[328.42 → 331.58] Like, Nope is definitely a place to pull from the past.
[331.58 → 332.34] That's right.
[332.34 → 337.44] So to explain a little bit how we do this, we call these episodes Yep, Nope, which is a
[337.44 → 343.94] nod to former JS Party panellist Alex Sexton's Yep, Nope.js, which was a cool library back
[343.94 → 347.40] in the day for determining whether the browser had certain features.
[347.46 → 349.38] I think it was a feature detection aid.
[349.80 → 352.98] And we use that to debate whether a premise is true.
[352.98 → 360.32] So the question today, as I said, is where Spas, not Spas, let's call them Spas for simplicity's
[360.32 → 362.96] sake today, were Spas a big mistake?
[363.34 → 367.94] And so one team is Team Yep, agreeing with that, answering in the affirmative, I should say,
[368.28 → 370.58] and the other team is Team Nope.
[371.18 → 379.16] And so Nick and Divya will be arguing that Spas indeed were a big mistake, and Ball plus
[379.16 → 381.00] the ghosts of JS Party passed.
[381.00 → 383.66] Ball's trying to make this real hard on himself today.
[383.80 → 387.12] We'll be arguing that Spas were not a big mistake.
[387.20 → 390.28] Now we do this kind of formal debate style.
[390.48 → 391.50] So we will have a timer.
[391.68 → 392.34] I'm your moderator.
[392.76 → 394.40] I will be watching the time.
[394.92 → 398.28] I will be enforcing time constraints.
[398.66 → 402.34] And when your time is up, we will channel Chris Miller, and he will say,
[403.08 → 403.28] What?
[404.16 → 406.68] Because we couldn't find a buzzer in our soundboard.
[406.82 → 407.52] So when you hear,
[407.96 → 408.18] What?
[408.18 → 411.42] Your time is officially over, and you must cede the floor.
[411.50 → 413.50] Any questions from the panellists?
[414.38 → 415.22] Old pros.
[415.72 → 416.12] Okay.
[416.90 → 421.22] Well, ladies first, we will start with Divya, and I will get my timer out here.
[421.28 → 421.74] Give me a moment.
[422.72 → 423.16] Cool.
[423.44 → 424.48] You will have two minutes.
[425.10 → 429.80] Ooh, actually, I could just leave my old car horn as well, which would be a good one,
[429.88 → 431.76] but we'll see what happens with that.
[432.28 → 437.38] You'll have two minutes to make your case, and you can start right now.
[437.38 → 443.82] Well, first, if we were to talk about single-page applications, it's worth talking about the
[443.82 → 450.16] definition of what they are, which is single-page apps are generally single HTML pages.
[450.60 → 455.70] They allow full interactions without any page refreshes, because the idea is that you're
[455.70 → 462.38] loading the entire app onto a user device, and the user is just going to work within that
[462.38 → 465.30] frame or within that particular HTML page.
[465.52 → 470.46] And then, I guess, all the data is already fetched, more or less, and then new data is
[470.46 → 473.58] just fetched additionally as needed.
[473.82 → 478.04] But the idea is that everything is loaded, so it allows for a single experience.
[478.74 → 481.82] The problem and the downsides, of course, you can guess is...
[481.82 → 486.04] Well, actually, first, I'll kind of talk about the corollary to that.
[486.12 → 488.14] So there's single-page apps, which is a single HTML page.
[488.36 → 491.94] The opposite of that is multipage apps, where you have multiple pages.
[492.08 → 496.40] So every time you do a page, you try to go back or forward.
[496.70 → 500.52] It's really a full-page refresh, because you're going back to the server, requesting something,
[500.62 → 502.54] and then it loads data and so on.
[503.10 → 507.92] And so those are the two differences that you work with, single-page apps versus multipage
[507.92 → 508.18] apps.
[508.18 → 514.30] You can kind of guess the obvious problem to this, which is that single-page apps are
[514.30 → 521.26] incredibly not performant in that sense, because you're loading an entire web page or web app.
[521.40 → 523.10] I think we've had this discussion before.
[523.42 → 528.34] You're loading this entire application, and sometimes a user won't even access all pages.
[528.54 → 531.14] They're not going to use the entirety of that particular app.
[531.54 → 533.22] And so you're wasting a lot of space.
[533.36 → 537.12] And the initial load time is so huge, because you're loading assets.
[537.12 → 540.40] There's a lot of whatever, pages, data.
[540.96 → 543.64] And so the initial load is a problem.
[544.26 → 548.78] And that can already impede user experience, because the argument oftentimes is that, yeah,
[548.82 → 551.84] you can make user experiences really nice on single-page apps.
[552.50 → 552.98] Performance.
[554.56 → 556.84] Sorry, your time is up.
[556.96 → 557.70] Good job, Divya.
[557.86 → 558.22] Thank you.
[558.22 → 564.28] You actually referenced one of our previous Yep nopes, which was episode 162, are web apps
[564.28 → 566.56] fundamentally different from websites?
[566.78 → 567.58] So you want to go back?
[567.62 → 571.38] I needed to one-up K-Ball, because I knew he was going to start bringing in other things.
[573.76 → 576.30] I was like, if he's going to bring in other things.
[576.42 → 577.30] Ah, preempting.
[577.40 → 582.12] See, what K-Ball made the classic mistake, which is he giving his plan out before the thing
[582.12 → 582.52] started.
[582.52 → 583.84] You got to keep it to yourself.
[584.12 → 588.10] It's just like, every evil genius ruins it when he gives the monologue at the end.
[588.14 → 589.04] Anyway, I'm stalling.
[589.16 → 590.28] K-Ball, you are up.
[590.36 → 594.32] Or I could be just giving enough rope for you all to hang yourselves, trying to struggle
[594.32 → 595.24] to pull things in.
[596.52 → 597.48] We're going to start.
[597.62 → 598.58] We will, shall see.
[598.86 → 599.26] Are you ready?
[599.58 → 599.80] Go.
[600.12 → 600.36] All right.
[600.36 → 604.82] I'm going to start as myself and just highlight to you all that single-page apps, and I'm going
[604.82 → 611.36] to call them spas, because they are as lovely and luxurious as a spa that you might go to.
[612.14 → 616.66] Spas are what make it possible to create rich browser-based applications that feel like native
[616.66 → 617.22] application.
[617.54 → 620.78] So once the application is rendered, it feels much more responsive.
[621.00 → 622.88] Navigation no longer has to go back to the server.
[623.00 → 625.62] You don't get these long pauses as you're clicking through things.
[625.62 → 630.32] If the new page doesn't require any new data to be loaded, the client can essentially render
[630.32 → 631.00] it instantly.
[631.00 → 636.36] And even if more data is required, it's just an API call, much less data flowing over the
[636.36 → 637.54] network, so much faster.
[638.10 → 642.72] Spas also make it much easier on developers to create those intricate user experiences and
[642.72 → 643.14] interactions.
[643.44 → 649.00] The whole application is living within JavaScript, so manipulating it in fine detail based on user
[649.00 → 651.34] interaction is just so much easier to implement.
[651.56 → 657.02] So if you create a complex UI, creating it with a client-side framework like React, Angular,
[657.02 → 661.76] Angular, View, knowing that you can control the whole entire experience, it's just an order
[661.76 → 666.28] of magnitude easier than trying to create the same level of interactivity on top of some
[666.28 → 668.74] sort of server-rendered page, passing things back and forth.
[669.20 → 674.46] So you can use all these straw men that you want, throw things out, like there's no need
[674.46 → 677.30] to make a blog, a spa, all this other stuff.
[677.58 → 682.42] But the question is not, is there ever a case against a spa for a particular use case?
[682.44 → 684.10] Of course there are some cases, right?
[684.10 → 687.76] If I'm just throwing words on a page and I don't care, don't use a spa.
[687.94 → 688.50] Sure, fine.
[688.60 → 691.72] But the question is, were spas a big mistake?
[691.86 → 697.26] Spas are what are taking the web browser as a platform and turning it from just a document
[697.26 → 703.36] reading engine to something where you can have genuine interactive applications on par
[703.36 → 704.32] with a native application.
[705.04 → 706.54] I rest my opening statement.
[706.84 → 707.38] Very good.
[707.82 → 709.98] You have 10 more seconds, but we'll just give you a complimentary.
[710.54 → 710.80] What?
[710.80 → 713.78] Okay, K-Ball coming in with the words per minute.
[714.14 → 714.94] Very nice.
[715.34 → 719.26] Nick, you don't talk quite that fast, but yet you still have the exact amount of minutes
[719.26 → 720.12] that K-Ball has.
[720.40 → 721.16] You ended early.
[721.68 → 722.74] Let's see how you do.
[722.96 → 723.86] It's your turn, Nick.
[723.92 → 724.44] Take it away.
[724.80 → 725.12] All right.
[725.22 → 728.88] Well, first off, let's start in the way that Divya started, with some definitions.
[729.06 → 732.82] If we look at the words that make up single page app, the first one is single.
[732.92 → 735.82] And as we all know, two is one and one is none.
[735.82 → 738.58] So you're already off at a disadvantage there.
[738.74 → 740.52] So then you just have page apps.
[740.90 → 742.16] And you know what that is?
[742.20 → 743.50] That's multipage apps.
[743.50 → 745.48] So we can just continue on going from there.
[745.60 → 749.66] We all know as a JS party, JS is where you party.
[749.84 → 751.60] It's not what you build apps with.
[752.26 → 755.42] And, you know, to get a little more serious, JS breaks.
[755.80 → 758.98] When you start building a single page app, you're building everything from scratch.
[759.10 → 761.02] You're breaking the back button by default.
[761.40 → 763.78] You're breaking the URL by default.
[763.78 → 765.06] Those things don't work.
[765.40 → 771.32] And to get those to consistently work is entirely up to every single development team that's doing it themselves.
[771.56 → 774.06] So it's just you're just starting off at a disadvantage.
[774.20 → 775.86] Your Lighthouse scores are immediately terrible.
[776.28 → 784.98] And you don't have a good experience for your users because they're expecting a standard level of accessibility, a standard way to interact with things.
[784.98 → 791.10] And it's up to every single development team to pick the right implementation or to do it themselves to get it done in that way.
[791.36 → 793.70] And so if you think about it, look at your phone.
[794.20 → 794.76] Take out your phone.
[794.82 → 796.26] How many apps do you have on that phone?
[796.54 → 798.58] I bet you don't have a lot of bookmarks to apps.
[798.68 → 800.94] You have a lot of apps because native apps are right.
[801.02 → 802.42] Maybe Apple was right about that.
[802.96 → 804.96] And single page is not the way to go.
[805.14 → 807.90] It doesn't matter that Apple is the one intentionally crippling those.
[808.26 → 811.10] Like it is just a bad experience.
[811.10 → 812.08] And maybe they're right.
[812.60 → 815.28] And that is all I have.
[815.28 → 816.90] Oh, wait.
[816.96 → 817.28] No, no, no.
[817.32 → 817.90] I have one more.
[817.98 → 818.30] I have one more.
[818.46 → 818.92] 15 seconds.
[819.10 → 820.86] We all know that Jared wins every debate.
[821.34 → 821.96] What would Jared do?
[822.08 → 823.38] Jared wouldn't build a single page app.
[823.52 → 826.60] So, I rest my case that that is the wrong way to do it.
[827.04 → 827.22] What?
[827.48 → 829.42] Well, I will say that your last point was spectacular.
[829.96 → 834.22] And I want to go back real quick and recover your first point, which was also spectacular.
[834.22 → 835.48] But you said it so fast.
[835.52 → 836.34] I'm not sure if I tracked.
[836.44 → 839.00] I think you said something like two is one and one is none.
[839.10 → 839.62] What was this?
[839.88 → 840.24] Exactly.
[841.10 → 842.10] You never heard that saying?
[842.10 → 842.36] That's the point?
[842.48 → 842.70] Okay.
[843.08 → 843.98] That was amazing.
[844.64 → 845.14] That was awesome.
[845.50 → 846.66] I just want to make sure I heard you correctly.
[847.46 → 847.82] Okay.
[848.22 → 850.24] Well, I generally do win these debates.
[850.34 → 851.50] But right now, I'm not going to lie.
[851.62 → 852.20] Nick is winning.
[852.98 → 854.08] But we'll see what happens.
[854.46 → 859.00] K-Ball, we now turn to you plus JS Party panellists past or whatever stick you have going
[859.00 → 859.54] on next.
[859.70 → 862.02] You have two minutes to do whatever it is that you're about to do.
[862.48 → 862.84] All right.
[862.84 → 866.64] Well, Nick, you're trying to steal thunder as well by referencing Christopher Randi and
[866.64 → 869.48] his whole thing about having to reinvent browser capabilities.
[869.64 → 874.00] But I'm going to call out to a different JS Party guest, Lori Voss, who highlighted that
[874.00 → 876.46] the history of change, the browser moves slowly.
[876.64 → 877.80] It has so many different things.
[877.96 → 883.86] But what happens to create progress is there will be user land changes where libraries implement
[883.86 → 884.64] new capabilities.
[884.82 → 891.02] And those that work really well end up transcending their user land area and are rising up to the
[891.02 → 891.60] browser level.
[891.80 → 895.64] Now, the first version that was highlighted in that conversation was jQuery, which doesn't
[895.64 → 896.08] stand here.
[896.08 → 901.30] But the next one that he was proposing would stand out was React and this approach to the
[901.30 → 904.46] world that is what enabled spas to occur.
[904.66 → 907.94] So I think you're referencing the wrong JS Party guests.
[908.34 → 911.92] But I also want to call out, you all are trying to make yourself seem so official by starting
[911.92 → 915.08] from definitions and playing with these like logical puzzles.
[915.08 → 917.94] But I'm going to call out to Fears and appeal to authority.
[918.20 → 919.68] I'm going to read some quotes.
[919.68 → 928.62] So quotes from the first result to the Google search, why single page apps are amazing.
[929.42 → 930.48] I'm going to read you these quotes.
[930.90 → 932.06] Spa is fast.
[932.42 → 938.60] As most resources, HTML, CSS scripts are only loaded once throughout the lifespan of application.
[939.22 → 941.82] We don't use the or anything here in this quote.
[942.14 → 943.16] Spa is fast.
[943.84 → 944.12] Next.
[944.58 → 945.18] Oh, there's a the.
[945.34 → 946.74] Is simplified and streamlined.
[946.74 → 950.04] There is no need to write code to render pages on the server.
[950.22 → 954.08] It's much easier to get started because you can usually kick off development from a file
[954.08 → 955.98] without using any server at all.
[956.46 → 958.54] Spas are easy to debug with Chrome.
[959.32 → 959.80] Okay.
[959.96 → 960.96] I'm just reading quotes here.
[961.06 → 962.24] This is the authority involved.
[962.42 → 962.98] I can tell.
[963.32 → 963.92] Top of Google.
[964.44 → 965.04] As you can monitor.
[965.48 → 965.98] Question authority.
[966.16 → 967.18] Network operations.
[967.86 → 970.36] Investigate page elements and data associated with it.
[970.44 → 975.22] And finally, it's easier to make a mobile application because the developer can reuse the same
[975.22 → 978.40] backend code for web application and native mobile application.
[978.96 → 978.98] What?
[979.50 → 979.74] What?
[980.26 → 980.50] What?
[980.64 → 983.34] Is that a comment on my quotes or am I out of time?
[984.18 → 987.26] That was both a buzzer and a commentary on what are you talking about?
[987.38 → 987.60] Okay.
[987.76 → 991.80] It sure sounds like your partner is Horses where you're just taking snippets out of context.
[992.66 → 994.58] Oh, I forgot Horses.
[994.66 → 994.82] Okay.
[994.86 → 996.46] I got to go find Horses Spa.
[996.66 → 997.86] You can't forget Horses.
[998.02 → 999.20] Oh my God.
[999.70 → 1003.54] If you need some Horses sounds, I can actually bring them in because I've been making them for
[1003.54 → 1003.72] years.
[1003.72 → 1004.00] Okay.
[1004.60 → 1005.78] This ends round one.
[1006.32 → 1007.58] So far, it's a no-brainer.
[1007.70 → 1008.48] I'm currently in first.
[1008.58 → 1009.12] Nick in second.
[1009.74 → 1011.42] K-Ball in fourth.
[1011.82 → 1015.46] And the ghost of JS Party panellists past is in last.
[1015.78 → 1016.38] What about Tiffin?
[1016.76 → 1017.54] Well, she's with Nick.
[1018.46 → 1019.24] Or third.
[1019.40 → 1019.80] I don't know.
[1019.88 → 1020.68] Same team.
[1020.80 → 1021.48] Yeah, same team.
[1022.00 → 1023.26] So we'll see what happens in round two.
[1023.32 → 1024.42] It's going to be the rapid fire round.
[1024.48 → 1028.70] We'll have half as much time and hopefully 100% less reading quotes.
[1029.00 → 1031.50] We'll find out what happens right after this break.
[1031.50 → 1033.68] We'll find out what happens right after this break.
[1033.72 → 1047.68] This episode is brought to you by Tercel, the platform that enables front-end teams
[1047.68 → 1048.98] to do their best work.
[1049.36 → 1054.32] Tercel combines the best developer experience with an obsessive focus on end-user performance.
[1054.96 → 1058.42] And I'm here with founder and CEO of Tercel, Fisher Rank.
[1058.78 → 1062.00] So, Fisher, I had you on Founders Talk recently talking about making the web faster
[1062.00 → 1066.36] and how Tercel is built on three pillars, develop, preview, ship.
[1066.72 → 1069.30] But talk about why it's so important to make the web faster.
[1069.30 → 1074.16] I think, first, the web is the most open and exciting platform to build on.
[1074.68 → 1079.22] And listeners are going to be enthusiastic about JavaScript, which is one of our areas
[1079.22 → 1079.70] of focus.
[1079.84 → 1085.68] We think that by creating amazing tools and open sourcing them, developers will go on
[1085.68 → 1088.32] to create amazing experiences for the end users.
[1088.52 → 1092.86] And I think that's where the concept of making the web faster to build and faster to end users.
[1092.86 → 1095.22] That's the crucial mission of Tercel.
[1095.48 → 1101.38] This is what's led to us investing all across the board to build this end-to-end platform.
[1101.66 → 1107.18] It started with the framework that you develop with, the workflow of pushing up a change and
[1107.18 → 1110.82] seeing it instantly and being able to share that change with your collaborators.
[1111.34 → 1115.90] All the way to shipping to the edge network of Tercel that makes your site or application
[1115.90 → 1118.50] globally fast, globally available.
[1118.50 → 1124.26] So it's this very comprehensive mission of making the web end-to-end faster and more open.
[1124.54 → 1125.16] I love it.
[1125.20 → 1128.28] Globally fast, globally available on a more open web.
[1128.40 → 1130.18] Learn more at Vercel.com.
[1130.38 → 1132.08] Again, Vercel.com.
[1148.50 → 1151.64] We're back.
[1152.06 → 1153.36] Round two of Yep, Nope.
[1153.46 → 1154.46] So far, the scoring.
[1155.04 → 1157.64] Team Yep, that's Nick and Divya with 10 points.
[1158.06 → 1159.38] Team Nope with zero.
[1159.72 → 1160.92] Where are the points coming from?
[1161.86 → 1163.76] You got to tell me the rules of the game here.
[1163.84 → 1165.10] How do I score points?
[1166.96 → 1169.68] I suggest a different strategy than the one you're currently taking.
[1169.82 → 1170.84] No, I'm just giving you a hard time.
[1170.92 → 1171.54] There are no points.
[1171.60 → 1172.26] I'm just messing with you.
[1172.82 → 1173.98] We're going to let you go first.
[1174.08 → 1175.62] So hopefully you can score some points in this round.
[1175.62 → 1181.90] But it's a rapid fire, one minute, and we encourage in this round more crosstalk between
[1181.90 → 1185.44] debaters versus the previous round where you must remain silent.
[1185.62 → 1189.04] So feel free to interact a little bit, but you're also stuck in your one minute.
[1189.62 → 1189.98] K-ball go.
[1189.98 → 1190.60] All right.
[1190.72 → 1196.62] So I am going to highlight that my counterparts here are clearly hypocritical because Nick just
[1196.62 → 1203.30] did an entire episode on the application he wrote for our JS Party game show that is
[1203.30 → 1204.42] writing a spa.
[1204.42 → 1210.44] In fact, he wrote a spa, and then he rewrote a spa and has implemented it in such a way
[1210.44 → 1212.34] that it's only writeable as a spa.
[1212.34 → 1213.02] He's court points.
[1213.14 → 1219.26] So I think we have a little bit of hypocrisy going on Team Yep over there.
[1219.60 → 1220.50] Your response, Nick?
[1220.76 → 1225.68] You know, the next rewrite will be into multiple pages, a single page per question.
[1226.26 → 1229.92] I think there's a quote, you have to know your enemies better than your friends.
[1229.92 → 1233.04] And so I think that's what's happening here.
[1233.22 → 1239.02] Clearly, Nick dislikes single page apps, but decided to build a single page app because
[1239.02 → 1240.56] of how terrible it is.
[1240.84 → 1243.38] He needed to prove how terrible it is.
[1243.94 → 1247.56] It sounds to me like you are highlighting that I know my enemies better than my friends
[1247.56 → 1252.36] here because my attack was so effective there relative to when I tried to bring in the ghosts
[1252.36 → 1253.30] who are my allies.
[1253.30 → 1254.30] Okay, good response.
[1254.42 → 1255.58] Divya, the floor is yours.
[1255.64 → 1256.08] You have one minute.
[1256.60 → 1261.12] So one of the arguments that were brought up was the idea of building single page apps
[1261.12 → 1262.88] so that you have a native-like experience.
[1263.30 → 1268.36] And I call issue to that mainly because the issue that single page apps brings is that
[1268.36 → 1272.76] they try to make the web native, which causes the chasm between native and web.
[1273.10 → 1274.40] They are not the same platform.
[1274.40 → 1278.22] And the argument should hold that you build for the platform.
[1278.40 → 1282.22] You're building based on the functionality and the expectations of that platform.
[1282.70 → 1287.78] And so when you're building an application for the web, you should not build it for native-like
[1287.78 → 1290.52] functionality because we want to use the platform.
[1290.68 → 1293.28] The platform is built for a specific purpose.
[1293.88 → 1299.02] They have certain user expectations on how things work, like the back button, like links,
[1299.44 → 1301.58] like sharing browser history and so on.
[1301.58 → 1306.62] And a lot of single page apps break that because there's no good way of link sharing.
[1306.92 → 1311.30] There's no good way of like going, like the back button is essentially custom.
[1311.92 → 1318.22] And so the problem here is that now you have this need for people to redo how browsers do
[1318.22 → 1322.46] things, which then leads to a lot of fracturing of how applications work.
[1322.88 → 1328.60] User experience are not always the same across different applications, which causes issues over
[1328.60 → 1329.92] what people expect.
[1330.04 → 1331.06] Okay, well, your response.
[1331.06 → 1331.70] Is that the end?
[1331.94 → 1332.16] Yes.
[1332.56 → 1332.86] All right.
[1332.94 → 1334.64] I'm going to call out to Abel here.
[1334.88 → 1339.68] So she stated that she believes that engineers are really into zombies and intent impending
[1339.68 → 1340.64] death by zombies.
[1340.78 → 1343.88] And I will say that that sounds to me like a zombie argument.
[1344.18 → 1346.86] You're really just saying, get off my lawn here.
[1347.04 → 1351.94] Let me use the tools I have, not focus on the user problems and how I solve them.
[1352.34 → 1354.96] Spas are broken because my spa is broken.
[1354.96 → 1361.14] I don't know how to implement and tie into router functionality and the APIs, the browser
[1361.14 → 1364.94] supplies to allow JavaScript to hook into history and do other things.
[1365.08 → 1368.58] Like you can't tell me that spas are broken because your spa is broken.
[1368.58 → 1370.64] I can build you a broken multipage app.
[1370.72 → 1371.48] That ain't hard.
[1371.88 → 1372.18] We know.
[1374.54 → 1375.94] Isn't that what you do at your day job?
[1376.62 → 1376.94] Nick.
[1380.14 → 1380.62] All right.
[1380.62 → 1384.80] One of your arguments, K-Ball, did that browsers give you all of this stuff for free.
[1385.10 → 1385.62] Well, guess what?
[1385.70 → 1389.44] When you have multi-pages, you just get more of it for free because you get it on each page.
[1390.06 → 1392.44] And did you hear that pause there?
[1392.52 → 1394.10] That was my argument reloading.
[1394.60 → 1395.60] Just like my pages.
[1395.78 → 1396.22] Hold on a second.
[1396.38 → 1398.02] The interjection, moderator interjection.
[1398.18 → 1399.56] Nick, where is your argument stored?
[1400.16 → 1401.00] It's stored on the server.
[1401.46 → 1402.32] It's stored in the cloud.
[1402.68 → 1403.82] What kind of application is this?
[1404.20 → 1404.68] It's an...
[1404.68 → 1405.20] I don't know.
[1405.50 → 1405.82] I don't know.
[1405.82 → 1410.34] That stuttering, that sense that it's hard to load the next thing.
[1410.46 → 1412.42] That's what happens when it's stored on multiple pages.
[1412.54 → 1414.60] You got to get it all together so you can load it.
[1414.70 → 1415.20] It was one.
[1415.60 → 1417.10] Centralized state management, man.
[1417.56 → 1417.84] Okay.
[1417.98 → 1418.70] Nick, continue.
[1418.92 → 1419.20] All right.
[1419.44 → 1422.56] So let's think about how we implement these single page apps.
[1422.56 → 1426.98] If we were to do such a thing, it starts with this thing called asynchronous JavaScript
[1426.98 → 1427.62] and XML.
[1427.86 → 1428.80] Who uses XML?
[1428.90 → 1429.90] It's right in the name.
[1430.02 → 1431.98] Like this is old news, old tech.
[1432.18 → 1433.46] We don't do that anymore.
[1433.46 → 1438.06] We have a cloud, and we deliver everything directly from the cloud every time.
[1438.62 → 1442.72] And the browser updates, and it's fast enough to update each time and have everything all
[1442.72 → 1443.14] right there.
[1443.72 → 1448.02] In the chat, Robert Hall posted a hacker news comment, which is never wrong.
[1448.30 → 1449.86] Sorry, you have to hold that for your next turn.
[1450.78 → 1453.62] K-Ball, would you like to respond to Nick, or would you like to start something fresh?
[1454.12 → 1455.80] You know, I'm going to keep going with his quote.
[1455.88 → 1458.20] The hacker news comment was, the web is a mistake.
[1458.32 → 1461.94] You all are trying to tell me that, oh, the original design of the web is perfect and we
[1461.94 → 1463.10] should never build beyond it.
[1463.10 → 1464.52] We never said it was perfect.
[1465.20 → 1469.02] There was no indication of saying that it was perfect.
[1469.36 → 1470.84] We said build for the platform.
[1471.02 → 1472.30] Build for the platform.
[1472.56 → 1475.84] Don't build things that the platform doesn't natively give you.
[1475.98 → 1478.84] Don't ever go beyond that box.
[1479.54 → 1480.92] Who are we building for?
[1481.04 → 1484.56] You can build for the platform and still push for its development.
[1484.96 → 1486.02] Who are we building for here?
[1486.38 → 1488.62] You're building for the users of the platform.
[1488.62 → 1491.62] So the users who have user problems.
[1491.82 → 1497.24] They have user problems because single page apps have reused how the browser works and
[1497.24 → 1500.26] therefore people have disjointed experiences.
[1500.68 → 1503.00] We started with building an application for them.
[1503.10 → 1506.96] Before we have a single page app or a multiple page app, they have some problem we're trying
[1506.96 → 1507.76] to solve, right?
[1508.30 → 1512.86] So shouldn't we build the solution that best solves that problem regardless of whether or
[1512.86 → 1512.92] not...
[1512.92 → 1513.82] What is that problem?
[1514.32 → 1515.70] Please define that problem.
[1515.70 → 1517.28] Well, I think it varies a lot.
[1517.44 → 1520.10] So a problem I'm typically doing.
[1520.24 → 1520.68] Let's see.
[1520.82 → 1524.12] How about collaboration on a design in Figma?
[1524.48 → 1526.42] Oh, single page application.
[1526.60 → 1529.68] How about I'm searching for something on Google?
[1529.86 → 1532.44] Oh, that's now a single page application too.
[1532.84 → 1537.40] Oh, how about I'm trying to understand what's going on with my friends on Facebook?
[1537.64 → 1540.20] Oh, single page application too.
[1540.70 → 1540.94] What?
[1541.08 → 1542.00] You're out of time, sir.
[1542.70 → 1543.86] I will have order.
[1545.14 → 1545.62] Divya.
[1545.70 → 1546.16] Divya.
[1547.58 → 1548.90] Please respond to this man.
[1550.08 → 1550.40] Respond?
[1550.64 → 1552.34] Wait, I thought we were like all responding.
[1553.74 → 1554.18] I know.
[1554.20 → 1554.88] I just wanted to order.
[1555.10 → 1556.74] And now I want to keep going.
[1558.56 → 1559.98] I just hadn't said anything for a while.
[1560.04 → 1561.30] So I felt like I had to say something.
[1561.60 → 1562.14] That's fair.
[1562.42 → 1565.14] Apparently I have to argue for Java and Flash now.
[1566.40 → 1567.18] Bring it back.
[1567.68 → 1567.86] Yeah.
[1567.86 → 1569.54] You backed yourself in a little bit of a corner there.
[1569.54 → 1574.62] I mean, there are ways that you can use the platform.
[1574.74 → 1578.32] The platform has been moving in like a very solid direction in general.
[1578.32 → 1580.96] Like now we have a lot of different tools.
[1580.96 → 1585.16] Like you have Houdini where you can change a lot of how CSS works.
[1585.16 → 1586.94] You can add selectors of your own.
[1587.04 → 1588.06] You can add styles.
[1588.06 → 1590.30] It adds a lot of powerful features.
[1590.30 → 1597.56] And so when you build for the web, you're really wanting the web to be pushed forward and to champion that effort.
[1598.08 → 1609.60] I think the argument that you build a separate thing in the interest of the web moving and catching up is sort of like not investing in what you on the infrastructure of the web.
[1609.60 → 1617.70] You're sort of going off in a corner and building a suburb, hoping the city would build up and be better so that you can move away from the suburb.
[1617.84 → 1625.66] Even though you've tried to build this idyllic little town outside a space where the infrastructure is very good to hold people.
[1626.08 → 1630.30] I'm going to jump in here real quick because I have a different example that this strikes me as.
[1630.30 → 1638.08] So if you all ever work with designers who are a little overloaded, you may have discovered that if you're asking for a design for a new feature, it may never happen.
[1638.74 → 1648.76] The best way to get a designer to give you a beautiful design for a new feature is you build an ugly version of that feature and threaten to ship it or even do ship it.
[1648.86 → 1651.42] Once it's in production, the designer looks at that and says, hey, that's ugly.
[1651.48 → 1652.28] I'm going to fix that.
[1652.32 → 1652.98] I'm going to clean that up.
[1653.04 → 1654.86] That's exactly what spas are doing here, right?
[1654.86 → 1665.96] The browser is progressing because the people who are responsible for building the browser said, holy smokes, what we're providing here is clearly not sufficient because people are building all this stuff around it.
[1665.96 → 1671.88] If spas weren't being built, would they have bothered to build all those APIs to enable them to be built well?
[1672.70 → 1673.12] No.
[1673.74 → 1676.04] The argument is very interesting.
[1676.68 → 1679.42] And I take a lot of issue with it.
[1679.52 → 1685.46] Partially because you're creating problems in order, like you're creating extra problems.
[1685.80 → 1686.84] Sounds passive-aggressive, right?
[1686.84 → 1691.24] As a way of saying like, oh, these problems help make the solution make sense.
[1691.24 → 1697.12] It's sort of like the argument people have whenever they decide to drive more cars.
[1697.28 → 1701.74] And they're like, we should subsidize cars and gas because then you do that more.
[1701.94 → 1706.70] And then it causes like people not to have infrastructure for public transit.
[1706.70 → 1710.32] And then you're like, well, we're doing this because public transit sucks.
[1710.46 → 1716.30] And hopefully because there are more traffic jams, the city will decide to put more money in public transit.
[1716.50 → 1718.54] You're not investing in the infrastructure.
[1718.54 → 1723.08] So how would you want people to be incentivized to make it better?
[1723.20 → 1724.10] It doesn't work.
[1724.48 → 1728.00] I wouldn't say that you should only do spas and never invest in the infrastructure.
[1728.22 → 1729.04] You should do both.
[1729.14 → 1733.00] However, I will highlight that change never happens when the people in power are comfortable.
[1733.50 → 1735.74] The browsers would love to stop feature development.
[1736.18 → 1741.26] If everybody would use their stuff, and they don't have to do more features, like why keep investing?
[1741.44 → 1744.64] Why maintain these expensive browser engineers and all of this?
[1744.64 → 1748.84] They keep investing in improving things because we keep pushing the bar for them.
[1749.08 → 1759.86] They keep investing to handle all the edge cases of all the spa applications and frameworks that are being built around them instead of just using the tools that are given to you by the browser.
[1760.28 → 1760.76] Precisely.
[1760.86 → 1761.64] You've made my point.
[1761.82 → 1766.92] If those didn't work, if we weren't pushing the boundaries, they wouldn't invest, and we'd be back in browser stagnation.
[1766.92 → 1780.82] I could argue that the web could have been fascinating had spas not existed because then we'd be building experiences that push the web forward and makes experiences within that sort of linear and make sense.
[1780.98 → 1791.88] But now with single page apps, because they've brought in a lot of design changes and certain expectations, browsers have had to follow suit to sort of like meet those expectations.
[1791.88 → 1799.68] And so they've had to sort of derail their own plans in order to build for what people have been used to because of single page apps.
[1799.88 → 1802.64] So can you imagine what the web could have been like?
[1802.98 → 1805.12] We could have had better forms by now.
[1807.00 → 1810.58] We could have had so much more if we didn't have to support all of this JavaScript.
[1810.74 → 1811.42] But that's the thing.
[1811.62 → 1816.58] Spas just proliferate more JavaScript, which makes them have to support more backwards compatible JavaScript.
[1817.02 → 1818.18] What the heck is flat?
[1818.40 → 1819.48] What is a flat map?
[1819.48 → 1822.22] We could have, I don't even remember what they're originally called.
[1822.72 → 1823.90] Is it splosh?
[1824.10 → 1824.60] I don't know.
[1825.06 → 1825.42] Smooth.
[1825.54 → 1826.16] Smooth, right?
[1826.54 → 1827.14] Smooth, yeah.
[1827.18 → 1828.16] Perfect point, Nick.
[1832.10 → 1833.44] Oh, dear.
[1833.44 → 1847.04] If we weren't always trying to play catch up to everything that is re-implemented every month and then has a million blog posts about it and how you can redo with, you know, this router in this version, like just use a router.
[1847.16 → 1847.98] Just use a server.
[1847.98 → 1849.40] It's called a client server.
[1850.10 → 1851.22] How much time do I have left?
[1852.00 → 1854.76] I stopped running the timer because you guys just didn't even care.
[1854.88 → 1855.88] So I'm just listening now.
[1857.66 → 1859.00] Nick's just like trying to fill time.
[1859.08 → 1860.54] I'm not even keeping track right now.
[1861.32 → 1863.52] So I guess you can just stop right there.
[1863.52 → 1866.50] Cable, I'll allow one response, and then we'll call at the end of this segment.
[1866.50 → 1881.46] My response is you all may be willing to wait for the bureaucratic process that is involved in updating standards and creating browsers, browser change and all of this to happen before you solve your user problems.
[1881.46 → 1884.52] But I got users, and they need their problem solved.
[1884.60 → 1886.76] And I'll use the tools available to me today.
[1886.98 → 1889.20] And oftentimes that involves a spa.
[1889.34 → 1890.52] I just hope they don't hit the back button.
[1890.52 → 1897.50] You keep using that zombie, that straw man argument as if there are no spas where back button functionality works.
[1897.82 → 1898.42] Oh, you should point.
[1898.48 → 1899.68] You should point to us to some.
[1900.04 → 1902.44] Yeah, please show us an example.
[1902.80 → 1903.00] All right.
[1903.04 → 1905.60] Thus ends our official debate.
[1905.60 → 1912.72] We'll come back on the other side of the break, and we can talk freely about what we actually believe about these things versus what we've been assigned to argue.
[1912.86 → 1916.48] So stay tuned, and we'll hear what actually people think.
[1916.48 → 1921.14] I think in terms of winning, of course, the only way to win is to not participate.
[1921.36 → 1922.28] I'm the only one who did that.
[1922.38 → 1923.14] So I do win.
[1923.68 → 1926.38] But coming in a close second with the form reform.
[1926.72 → 1929.50] Thank you, Robert Hall and the chat room for giving it a name.
[1930.14 → 1933.72] Divya's argument about forms is the winning argument of the day.
[1933.72 → 1935.92] And so Divya takes a close second place.
[1936.48 → 1937.94] Everybody else, thank you for participating.
[1938.08 → 1938.54] We'll be right back.
[1959.90 → 1962.98] This episode is brought to you by Source graph.
[1962.98 → 1967.72] Source graph is universal code search to let you move fast, even in big code bases.
[1968.22 → 1974.98] Here's CTO and co-founder, Bung Liu, explaining how Source graph helps you to get into that ideal state of flow in coding.
[1975.12 → 1980.12] The ideal state of software development is really being in that state of flow.
[1980.30 → 1990.44] It's that state where all the relevant context and information that you need to build whatever feature or bug that you're focused on building or fixing at the moment, that's all readily available.
[1990.44 → 1996.00] Now, the question is, how do you get into that state where, you know, you don't know anything about the code necessarily that you're going to modify?
[1996.00 → 1998.68] That's where Source graph comes in.
[1998.88 → 2002.04] And so what you do with Source graph is you jump into Source graph.
[2002.12 → 2005.46] It provides a single portal into that universe of code.
[2005.60 → 2009.10] You search for the string literal, the pattern, whatever it is you're looking for.
[2009.18 → 2012.30] You dive right into the specific part of code that you want to understand.
[2012.30 → 2025.42] And then you have all these code navigation capabilities, jump to definition, find references that work across repository boundaries that work without having to clone the code to your local machine and set up and mess around with editor config and all that.
[2025.54 → 2030.88] Everything is just designed to be seamless and to aid in that task of, you know, code spelunking or source diving.
[2030.88 → 2039.06] And once you've acquired that understanding, then you can hop back in your editor, dive right back into that flow state of, hey, all information I need is readily accessible.
[2039.28 → 2043.76] Let me just focus on writing the code that influenced the feature or fixes the bug that I'm working on.
[2044.12 → 2044.36] All right.
[2044.40 → 2046.24] Learn more at Sourcegraph.com.
[2046.36 → 2054.36] And also check out their bi-monthly virtual series called DevToolTime covering all things DevTools at Sourcegraph.com slash DevToolTime.
[2060.88 → 2081.66] All right.
[2081.74 → 2083.16] Great debate, you all.
[2083.32 → 2085.38] K-Ball, you made some interesting points.
[2085.48 → 2087.74] Did you believe anything you were talking about or are you just talking?
[2087.74 → 2091.78] Mostly just talking, but I mean, so here's the thing.
[2092.16 → 2098.04] Spas can make sense for particular types of applications, right?
[2098.06 → 2104.02] Like if you're doing like a Slack web application, or you're trying to do Figma, which I used, right?
[2104.06 → 2107.00] Like a spa makes a ton of sense for that type of situation.
[2107.48 → 2113.10] The real issue is that they became the hammer that we threw at every single nail.
[2113.10 → 2117.62] There are very, very large numbers of applications for which they don't make sense.
[2118.10 → 2133.46] And I actually, I really like some of the new progress and Remix is doing some of this and other things where folks are actually trying to maintain that ease of programming interactivity while getting back some of the nicer features that you get with server rendered applications.
[2133.46 → 2134.54] Mm-hmm.
[2134.80 → 2146.32] Now, Nick, K-Ball pointed out what was one of his strongest points was the hypocrisy of your argumentation, which is why I assigned you on that team is that you almost entirely only build single page apps, right?
[2146.38 → 2147.16] I mean, day to day.
[2147.48 → 2147.68] Yep.
[2147.68 → 2151.04] So you don't actually think they're a big mistake or are you just...
[2151.04 → 2151.56] Oh, no, I do.
[2151.82 → 2152.22] Oh, you do.
[2153.72 → 2154.36] Oh, okay.
[2154.72 → 2156.70] So you're just making a big mistake every day.
[2156.78 → 2157.36] No, no, no, no.
[2157.36 → 2164.16] I think that in a lot of ways we do overcomplicate everything, and we do have to re-architect a lot of stuff.
[2164.28 → 2171.38] And it's just a lot more that's put on my plate to maintain and make sure it's working when I could be off solving more important problems.
[2171.38 → 2174.12] But I do think that they have their place for sure.
[2174.42 → 2175.90] I do like working with them.
[2176.04 → 2179.34] And I do think that in general, like there's...
[2179.34 → 2187.16] Like, take right now, we're recording this podcast in a web app, and it's on a single page and it works fantastically.
[2187.48 → 2190.56] And if we wanted to bring in another guest, guess what they don't have to do?
[2190.60 → 2192.76] They don't have to download a single thing or set anything up.
[2192.98 → 2199.34] They just have to do a complicated process of using a Chromium browser and giving it a lot of permissions for things.
[2199.34 → 2202.58] But it does still work, which is really quite impressive.
[2202.90 → 2207.10] And, you know, it's been practically flawless, which is really a good testament.
[2207.72 → 2214.18] So for the listener, we use riverside.fm to record, which provides us all video, streaming, recording, etc.
[2214.80 → 2217.68] Participation in this chat room, the soundboard, it's all in one spot.
[2218.08 → 2226.62] That being said, this is a bit of a hybrid application because we are in the studio and the studio are this web application that's all right here on one page.
[2226.62 → 2229.74] But then when you go to the recordings, it's just its own separate page.
[2229.80 → 2233.20] When you go back to the list of your different studios, it's its own separate page.
[2233.56 → 2236.98] And so it's not like all riverside.fm is one single page.
[2237.26 → 2243.06] It's like we have this rich web app in here that has its own tabs and stuff that don't reload the page.
[2243.36 → 2246.50] But when you go beyond that, it is multiple pages.
[2246.58 → 2247.36] So it's a bit of a hybrid.
[2247.48 → 2250.06] And I think a lot of times that makes a lot of sense.
[2250.78 → 2254.06] Divya, you argued that single page apps were a big mistake.
[2254.14 → 2254.86] Do you believe that?
[2254.86 → 2257.94] I mean, I think in general, it's just been misused.
[2258.14 → 2262.38] It's sort of like the argument that was made around we gave people this.
[2262.44 → 2266.38] It kind of became the de facto way that people started versus like actually making the decision up front.
[2266.60 → 2267.24] Yeah, exactly.
[2267.48 → 2275.02] It's just a matter of like everyone was given this crazy jackhammer and then everyone started using it for tiny things.
[2275.20 → 2278.02] They're like, oh, I need to remove my backslash.
[2278.16 → 2281.70] Let me just use this jackhammer to remove the tiling.
[2282.26 → 2283.94] I think that's how jackhammers work.
[2283.94 → 2284.42] I don't know.
[2284.84 → 2285.78] I've never used one.
[2286.00 → 2287.26] I've just used tiny hammers.
[2287.72 → 2290.72] And so the problem is that we gave people a tool.
[2290.92 → 2295.76] And I think when single page apps were created, they weren't even like this fixes everything.
[2295.90 → 2296.34] It was not.
[2296.64 → 2304.84] But everyone used it like to fix everything or to build everything, which I think became a problem because now apps became really bloated.
[2304.84 → 2311.08] People were re-implementing parts of the web that did things already, like back buttons, browser history.
[2311.22 → 2313.14] We were just like redoing it over and over again.
[2313.46 → 2314.92] And that became a huge problem.
[2315.26 → 2316.70] And I think there are certain use cases.
[2316.86 → 2317.24] I agree.
[2317.78 → 2322.54] Like if you wanted Figma, I think VS Code has like a web thing now.
[2322.54 → 2324.26] And that's a single page app as well.
[2324.40 → 2326.68] Like you can't build that as a multipage app.
[2326.74 → 2329.00] That would be, I think it would be horrible.
[2329.72 → 2331.96] But those are very specific instances.
[2331.96 → 2340.06] And I think like Dustin in the chat talked about, or he was like, the comment was, is it valuable to distinguish local first software versus spas?
[2340.06 → 2346.00] And in a way, I kind of feel like, and the discussion so far has just been around the development type.
[2346.28 → 2352.42] So I kind of feel like Figma and VS Code and all of these things are very specific kinds of development.
[2352.54 → 2357.56] And they are very specific use cases because they require like heavy user interaction.
[2357.94 → 2365.10] And you have to sometimes allow multiple sessions, like people working on, like Google Docs, for example, has like CRDT.
[2365.24 → 2367.38] There are a lot of things that you're dealing with.
[2367.38 → 2376.12] And those, there are reasons to use a single page app for them because the problem area is so vast and the interaction is very specific.
[2376.74 → 2387.18] But if you're building like a blog or something much smaller than a single page app, it's like way too much and not really what you should be building, in my opinion.
[2387.44 → 2390.42] So yeah, it's like very specific to the use case, I would say.
[2390.76 → 2394.16] I feel like every time we do a yup note, we just end up here.
[2394.78 → 2394.90] Yeah.
[2395.10 → 2396.58] Well, I mean, that's engineering, right?
[2396.58 → 2398.44] Engineering is all about trade-offs.
[2398.60 → 2400.76] There are no absolutes in engineering.
[2401.12 → 2403.04] Your point about local is an interesting one, right?
[2403.10 → 2407.30] So Figma, they have local applications using Electron.
[2407.54 → 2407.74] Yeah.
[2408.08 → 2408.30] Right?
[2408.36 → 2410.88] They're actually embedding their single page app.
[2411.06 → 2415.00] And that's a multipage app doesn't really work in that kind of embedding.
[2415.08 → 2424.60] Like one of the fascinating things that the single page approach kind of enables is you can take the same application and package it up in this sort of native wrappers.
[2424.60 → 2433.82] And is that as good as creating individual distinct native implementations using whatever those native packages prefer?
[2434.02 → 2434.56] I don't know.
[2434.78 → 2436.32] But for many cases, it's good enough.
[2436.38 → 2442.36] And it facilitates giving these capabilities while lowering your development burden quite a bit.
[2442.36 → 2450.02] I think the cross-platform argument is interesting because tools like Electron, and then I think there are newer ones too.
[2450.14 → 2451.20] Like there's a Rust one.
[2451.38 → 2451.90] I forget what it's called.
[2452.04 → 2453.26] It's like Tori or something.
[2453.26 → 2462.26] But it's just like a way in which you can not have to change your development environment, and you build a cross for like a desktop app, mobile and web.
[2462.44 → 2469.58] Which I think is honestly from a development cost perspective better because then you don't have to have separate teams.
[2469.78 → 2474.94] But again, not every app needs to be cross-platform, right?
[2474.94 → 2477.54] Like Figma, for example, is a great use case.
[2477.68 → 2478.76] VS Code is a good use case.
[2478.76 → 2483.06] Like these are things in which people want them across platforms.
[2483.32 → 2492.14] But again, like I don't know if you're building just like a small blog or if you're building like a podcast app thing, do you really need it to be cross-platform?
[2492.34 → 2493.68] Can you just use it on one platform?
[2493.88 → 2497.18] So you could argue there are a lot of different avenues for that.
[2497.44 → 2498.64] So cross-platform is interesting.
[2498.64 → 2505.36] The other thing that's interesting that I thought would have gotten brought up for on Ball's pro side is that multi-client.
[2505.94 → 2510.96] So this was actually one of the things that Tom Preston Warner really made an emphasis on last time he was on the show.
[2511.02 → 2513.80] By the way, he's coming up here soon to talk about Redwood 1.0.
[2514.30 → 2521.94] Was that division with a single page application and client-side rendering, you have the division between the API and the client.
[2521.94 → 2528.82] And that architecture sets you up and forces you as a team or an organization to set you up for multiple clients.
[2529.24 → 2544.38] Whereas when you go down the road on a multipage app with server-side rendering, or sometimes you're doing static, whatever, whichever way you're doing it, you're more likely to mix those concerns and not have that firm contract of here's my JSON API and here's my SPA.
[2544.38 → 2548.70] And that can back you into a corner when it's like, all of a sudden, hey, we want a command line app.
[2548.82 → 2550.44] Hey, we want an iOS app.
[2550.52 → 2551.94] Hey, we want a public API.
[2552.62 → 2561.74] And so teams that are trying to be economical, actually, sometimes the argument is we should do an SPA because it's more economical over the long term, even though it's less so getting started.
[2562.26 → 2565.02] That did come up in one of the quotes that I...
[2565.02 → 2566.76] Oh, they were rapid fire.
[2566.86 → 2567.44] I must have missed it.
[2567.46 → 2569.98] It was lost in the general ridicule around the quotes.
[2569.98 → 2578.24] I've always loved that original Fears take of, I'm going to appeal to authority and read some quotes.
[2578.66 → 2579.86] And read some quotes.
[2580.26 → 2581.72] I remember that, yeah.
[2581.84 → 2587.72] It's funny because I just recently read it in our trailer just because it's been a couple of years and people have come and gone, and I wanted to be fresh.
[2588.04 → 2594.54] But that old quote from Fears, I just, it was on the old trailer and I brought it into the new trailer too because it's just such a funny moment.
[2594.82 → 2595.80] It's so good.
[2595.80 → 2611.92] One of the things that we're starting to see, I think, is even if you're separating your front end, like having some amount of server rendering and server side logic there, and it gets you some of that capability that you're talking about without necessarily having to go all the way to an SPA.
[2611.92 → 2618.34] And, you know, even frameworks like Remix, which I'm going to bring up again, because they're doing kind of interesting stuff here, right?
[2618.38 → 2622.74] Like they're doing all of their rendering on the server, but their architecture is set up.
[2622.82 → 2624.08] It's still a separated front end.
[2624.14 → 2627.28] It expects there to be a backend API that lives separately.
[2627.82 → 2631.04] And from a developer's perspective, you don't really have to think about that too much, right?
[2631.06 → 2634.82] You just provide the data in the way that you need or the way that it defines.
[2634.82 → 2639.46] I haven't used Remix yet, but, and then it can, you can reload the page there and it'll be fine.
[2639.46 → 2643.02] Or you can navigate in a single page way, and it'll also be fine.
[2643.50 → 2643.64] Yeah.
[2643.76 → 2648.84] It hides that away and gives you like a nice little, what they call a bridge over the network chasm.
[2649.34 → 2649.56] Yeah.
[2649.72 → 2650.70] I think it's cool too.
[2650.70 → 2661.74] Like, I think I might've mentioned this in a previous episode, but just the architecture around what is possible on the web and like platforms and how we deploy things has also changed a lot.
[2662.38 → 2668.46] And so you no longer like single page apps where you want it to prevent that round trip constantly.
[2668.46 → 2672.72] Because you're just like loaded quickly because you didn't have access to a lot of servers.
[2672.94 → 2675.18] It was like servers were in certain locations.
[2675.18 → 2678.86] It was like US East Asia had one, like it was in certain parts.
[2678.86 → 2685.44] And so when someone loaded, yeah, the initial load time was long, but then subsequent loads were fast because everything's already there.
[2685.70 → 2695.08] Now you have a lot of really cool technology and platforms that give you access to multi-region deployments, and it makes it much faster and much easier to work with.
[2695.08 → 2706.30] And so you can do a lot of like kind of hybrid type approaches, and you can do some server side rendering if you wanted to without having to incur again, like that crazy round trip times.
[2706.30 → 2714.82] Cause it like, you'll still need a server round trip, but in terms of where the server is located, it's probably going to be closer to you now than it was like 10 or 20 years ago.
[2714.94 → 2715.44] For sure.
[2715.78 → 2716.12] Totally.
[2716.32 → 2722.90] Edge compute and having like edge, like server side rendering just completely changes all the trade-offs you have there.
[2722.90 → 2731.52] And even if you're going back to a centralized database, though, some of the edge compute platforms, like I feel like I was reading like fly.io will like to propagate your data out too.
[2731.70 → 2734.28] Like there are all sorts of fun stuff.
[2734.44 → 2735.84] Disclaimer, Divya works with fly.
[2736.08 → 2736.58] I do.
[2737.00 → 2738.46] Oh, oh, oh, oh, oh, oh.
[2738.72 → 2740.80] Well, she'll tell you all about it now.
[2741.56 → 2746.02] I try not to bring up where I sometimes work because I feel like I'm super biased, but yeah.
[2746.38 → 2749.52] So is that correct that it's propagating the data out to the edge as well?
[2749.62 → 2751.18] We do propagate some of the data, yeah.
[2751.60 → 2752.50] There are parts of that.
[2752.50 → 2758.42] But that creates like a totally different world in terms of the trade-offs that you need to make about the network then.
[2759.12 → 2759.22] Yeah.
[2759.46 → 2761.72] So here is a question around the premise.
[2761.98 → 2762.58] One more question.
[2762.76 → 2764.74] So Spas were a big mistake.
[2764.82 → 2766.72] It seems like sometimes they might be a mistake.
[2766.72 → 2771.34] If we think about like an individual team or person making a choice, like sometimes it might be a mistake to choose that.
[2771.74 → 2774.66] Sometimes it might be the right choice.
[2774.66 → 2780.32] I think we can all name certain applications where we're like, yes, SPA made a lot of sense for Gmail.
[2780.56 → 2782.38] It made a lot of sense for Trello, etc.
[2783.36 → 2793.56] But as an industry as a whole, like this pendulum swing, which we tend to go back and forth between different things, was that direction that we went on, which may have been a five or 10 year direction.
[2793.92 → 2799.12] And I think, Divya, you kind of touched on this with your argument around, I think, how good forms could be.
[2799.12 → 2809.70] Do you think as a whole, like the browser facilitating features for the needs of Spas and like this pendulum swing towards, and now we're kind of starting to swing back the other direction?
[2810.22 → 2812.28] Do you think that whole thing was a waste of time?
[2812.32 → 2815.72] Or do you think that we had profit or there are benefits from going that direction?
[2815.72 → 2819.84] It's really hard to say, but there are parts of it that feel like a waste of time.
[2819.98 → 2823.38] Like we are reinventing things, or we are creating interactions that people expected.
[2823.88 → 2828.34] But at the same time, I sort of, the industry is constantly in flux.
[2828.48 → 2832.58] Like there's always things that come up and then go like full stack apps.
[2832.76 → 2837.60] The whole like Rails and build everything in Rails was like a whole thing in like the early 2000s.
[2837.74 → 2841.16] And Node.js, you can still build things in Node pretty well.
[2841.16 → 2842.94] But anyway, aside from that.
[2843.02 → 2844.92] You can still build things in Rails pretty well, yeah.
[2845.44 → 2846.56] I don't really want to go there.
[2847.20 → 2847.96] I disagree.
[2848.22 → 2849.12] There's our next debate.
[2850.52 → 2851.42] I don't know.
[2852.40 → 2855.24] Bring on DHH to like to argue for Rails.
[2855.88 → 2857.40] We think we know which side he's on.
[2857.76 → 2867.48] Well, so I feel like DHH being the sort of disaster that he is hides a lot of the real value that still is there in the framework and the community beyond him.
[2867.86 → 2870.46] Yeah, I think there's definitely, I mean, I can see that.
[2870.46 → 2877.58] But I think I'm, again, like very biased because I'm working on a Rails app, and it's really clunky, and the experience is horrible.
[2878.40 → 2880.24] And I dislike it.
[2880.52 → 2882.36] Modern Rails or legacy Rails?
[2882.52 → 2883.44] It's not legacy.
[2883.74 → 2884.22] It's not legacy.
[2884.54 → 2891.78] The reason why I ask is that I actually haven't done a modern Rails, but I have fond recollections of Rails 6, like 4 through 6.
[2892.00 → 2892.22] Okay.
[2892.36 → 2896.54] And so I'm not sure what it looks like today, but it was very productive for a very long time.
[2896.54 → 2899.08] And I expect it to stay that way, but maybe it's gotten clunky.
[2899.20 → 2899.60] I don't know.
[2899.60 → 2906.42] Yeah, we're not using super legacy stuff, but I'm working with like GraphQL things in Rails, and it's just painful overall.
[2906.94 → 2909.66] Because it's just, yeah, it's just clunky for what it is.
[2909.82 → 2912.40] I would have rather written in TypeScript or something better.
[2912.88 → 2914.42] You just say that because you're on Nick's team.
[2914.70 → 2915.52] The debate's over, Divya.
[2915.60 → 2917.08] You don't have to kiss up to Nick.
[2917.14 → 2918.74] No, it's just that I don't like writing Ruby.
[2919.10 → 2922.44] Every time I have to write a new query or mutation, I have to write Ruby.
[2922.98 → 2923.74] I don't like that.
[2924.06 → 2925.82] You'd rather write TypeScript than Ruby?
[2925.82 → 2925.90] Ruby?
[2926.38 → 2927.54] Yes, of course.
[2928.04 → 2929.76] I'm personally offended at this point.
[2930.08 → 2930.24] Okay.
[2930.34 → 2931.78] So we found your bias there.
[2934.80 → 2937.88] Other than performance, I feel like Ruby is such a great language.
[2938.00 → 2938.58] I concur.
[2939.02 → 2941.48] Like it just, in terms of just the joy of using it.
[2941.96 → 2944.34] But maybe that's because I've used it for a long time.
[2944.34 → 2948.40] I do want to actually dig in a little bit more on your question there, Jared, about the direction.
[2948.82 → 2951.96] Like, I went a little over the top in the debate on this.
[2952.06 → 2959.78] But I actually do believe that the user space innovation as a push towards direction for platforms is really important.
[2960.16 → 2965.46] And it's something that we have seen in OS land and things like that as well, right?
[2965.46 → 2973.96] Like things that go into the platform or the kernel of necessity must move slower because they must maintain backwards compatibility.
[2974.32 → 2976.48] There are all sorts of stability needs and things like that.
[2976.54 → 2981.16] And so the place for really fertile innovation and exploration is in user space.
[2981.16 → 2989.98] And then that then is a very good indicator to the browser or the platform vendor of where the important areas are.
[2990.14 → 2994.40] And so I think this approach of lots of stuff gets tried in user space.
[2994.52 → 2996.78] And some of it will be a disaster and some of it will not.
[2997.26 → 3005.16] But the things that become very successful are then those things that start to get absorbed into the platform.
[3005.36 → 3006.80] And the platform makes those easier.
[3006.80 → 3016.16] And so I think there are things from the spa period that were probably mistakes and probably misdirections.
[3016.16 → 3020.16] But there's also an awful lot of valuable innovation and exploration that happened there.
[3020.24 → 3035.88] And I don't think we would be nearly in the place that we are in terms of things like Houdini, in terms of things like Canvas, in terms of all these things that are enabling these massively interesting and powerful applications to live in browsers if the spa period had not happened.
[3035.88 → 3039.90] Yeah, I wonder if Wasm wouldn't have moved forward without that too.
[3040.28 → 3042.54] Because now you can do crazy stuff with Wasm.
[3042.96 → 3043.10] Yeah.
[3043.24 → 3045.06] And that's like what Figma is doing, right?
[3045.18 → 3045.42] Yeah.
[3045.72 → 3049.04] Yeah, I was digging into their job postings.
[3049.10 → 3050.20] They're writing their stuff in C++.
[3050.66 → 3050.86] Yeah.
[3051.60 → 3052.62] Super low level.
[3052.88 → 3055.28] For these wild browser apps.
[3055.34 → 3055.94] That's awesome.
[3056.32 → 3056.84] Is it though?
[3056.84 → 3056.88] No.
[3057.68 → 3062.88] It's also like, I mean, you can have the application piece that's just there living on a single page.
[3063.00 → 3067.44] But then when you go to the gallery view or whatever, that's another page.
[3067.70 → 3068.06] Totally.
[3068.22 → 3069.16] You can mix and match.
[3069.48 → 3070.04] Yeah, you can.
[3070.70 → 3072.52] Yeah, that's one of the cool things is there's so much choice.
[3072.62 → 3074.38] But one of the hard parts is there's so much choice.
[3074.38 → 3081.44] And so often we are lazy or strapped on time or don't have all the information.
[3081.44 → 3083.38] And we're like, just tell me what's best.
[3083.58 → 3084.28] Just tell me what to do.
[3084.32 → 3085.38] Which is why these debate episodes are fun.
[3086.02 → 3090.60] Because, of course, they have a harsh premise that can either be a yes or a no.
[3091.14 → 3094.82] But at the end of the debate, you know that there's a lot of it depends.
[3095.20 → 3097.46] And the actual conversation around it is the interesting part.
[3097.46 → 3098.20] The debates are fun.
[3098.66 → 3104.30] But I always like the third segment best because we can discuss all of those in-between spots.
[3104.38 → 3106.70] If you enjoyed this debate episode, we've done this.
[3106.90 → 3107.78] It's our fifth one.
[3108.30 → 3109.26] So go back into the feed.
[3109.36 → 3111.22] You'll find different arguments.
[3111.50 → 3113.52] Are web apps fundamentally different from websites?
[3114.10 → 3115.88] Should websites work without JavaScript?
[3116.54 → 3118.98] Is modern JavaScript tooling too complicated?
[3119.60 → 3121.78] And should we rebrand JavaScript?
[3122.08 → 3124.56] Which was a fun one for sure.
[3124.56 → 3127.12] K-Ball mentioned Remix a couple of times on this show.
[3127.46 → 3130.66] Reminds me, it is time for our new segment, Holly.
[3131.04 → 3131.40] Can I Holly?
[3131.46 → 3131.98] Can I Holly at you?
[3132.02 → 3132.40] Can I Holly at you?
[3132.68 → 3135.66] Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly, Holly.
[3135.78 → 3137.52] Holly at Remixing.
[3137.60 → 3144.10] Remixing right around the corner, May 24th and 25th in Salt Lake City.
[3144.50 → 3149.54] And we do not have a for sure plan, but we believe JS Party will be involved at Remixing.
[3149.54 → 3155.48] So if you are thinking of going, and you want to come see us, hang out with us, we will most likely be there.
[3155.64 → 3157.02] I'm hedging, but it'll probably happen.
[3157.72 → 3159.34] And so do that.
[3159.54 → 3162.10] Come to Remixing and come see us.
[3162.16 → 3163.36] It's May 24th, 25th.
[3163.48 → 3165.16] Again, Salt Lake City.
[3165.52 → 3166.50] So check it out.
[3166.56 → 3169.76] Remix. Run slash cone.
[3170.24 → 3170.76] All right, you all.
[3170.86 → 3171.90] This is our episode.
[3172.36 → 3172.82] K-Ball.
[3172.96 → 3175.02] Nick, Divya, any final words before we call today?
[3175.46 → 3175.82] We win.
[3175.82 → 3178.54] It's been too long since I went to the other kind of spa.
[3179.52 → 3180.98] You made me miss it.
[3181.34 → 3184.28] The winner of this debate episode gets a free spa on us.
[3184.44 → 3185.14] Congrats, Jared.
[3185.14 → 3186.86] You have to go to the Korean spas.
[3186.96 → 3188.00] Those are the good ones.
[3188.26 → 3188.54] Oh.
[3188.78 → 3190.10] Some of them are all-inclusive.
[3190.28 → 3191.36] You get a massage.
[3191.64 → 3192.94] You can go to the hot tub.
[3193.22 → 3194.70] And then there's usually a restaurant.
[3194.70 → 3196.76] And then if you don't want to go home, they have a hotel.
[3196.88 → 3197.16] Seriously?
[3197.30 → 3198.08] It's like all-inclusive.
[3198.50 → 3198.68] Yeah.
[3199.10 → 3200.22] That really is all-inclusive.
[3200.22 → 3201.16] That's like a spa and breakfast.
[3201.16 → 3204.80] It's like an adult amusement park, I guess.
[3205.34 → 3208.44] I just, I don't know what to call it.
[3208.44 → 3209.16] That's good branding.
[3209.96 → 3213.06] Should we rebrand Korean spas to adult amusement parks?
[3213.40 → 3215.54] I don't know if you want that branding.
[3217.84 → 3218.64] I don't know.
[3218.70 → 3219.16] It was your idea.
[3219.30 → 3221.80] I didn't say special services were included.
[3222.50 → 3223.64] That was not.
[3223.64 → 3225.64] You said all-inclusive.
[3225.86 → 3226.76] So I assume.
[3227.46 → 3228.46] Hey, listen up.
[3228.46 → 3233.62] If you have a cool premise for another Yep Nope episode, let us know.
[3233.70 → 3240.28] We would love to compile more groups of debaters and find out who is the master debater.
[3240.46 → 3240.60] Okay.
[3240.64 → 3243.12] I have to end this episode now before I get myself in trouble.
[3243.12 → 3246.46] On behalf of K-Ball, Nick and Divya, I'm Jared.
[3246.62 → 3247.80] And this has been JS Party.
[3247.98 → 3249.28] And we'll talk to you next time.
[3253.14 → 3255.72] So who do you think had the most compelling arguments?
[3256.26 → 3258.62] Or maybe there are factors we completely failed to mention.
[3258.84 → 3260.18] Let us know in the comments.
[3260.52 → 3264.00] There's a link to the discussion thread for this episode in your show notes.
[3264.52 → 3265.50] We'd love to hear from you.
[3265.92 → 3268.54] Thanks again to Vastly for CD-ending for us,
[3268.80 → 3270.74] to Break master Cylinder for the Fresh Beats,
[3270.74 → 3271.92] and to you for listening.
[3271.92 → 3273.80] We appreciate you spending time with us.
[3274.24 → 3275.18] Next up on the pod,
[3275.46 → 3277.64] K-Ball goes one-on-one with Tom Press and Warner
[3277.64 → 3280.06] to discuss Redwood's big 1.0 release.
[3280.32 → 3282.12] There's a lot going on in that community.
[3282.46 → 3283.00] Stay tuned.
[3283.18 → 3285.20] We'll have that conversation ready for you next week.
[3285.76 → 3287.42] Okay, changelog++ friends,
[3287.62 → 3289.66] here comes your bonus five-minute pre-show.
[3289.94 → 3291.74] Thank you for directly supporting our work.
[3292.02 → 3292.74] It means a lot.
[3301.92 → 3314.58] We'll see you next week.
[3314.58 → 3315.40] Game on!
