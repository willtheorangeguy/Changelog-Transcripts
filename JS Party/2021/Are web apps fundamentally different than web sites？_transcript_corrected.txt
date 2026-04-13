[0.00 → 6.50] Maybe if we can quantify the level of over-engineering that's going into something, we can distinguish it on a scale between website and web app.
[7.06 → 8.40] Maybe we could do it on page size.
[8.52 → 12.10] Like if it's three megabytes of JavaScript bundle, then it's a web app.
[13.48 → 16.18] But if it's 10 megabytes of images, then it's a website.
[16.18 → 17.04] There you go.
[17.72 → 19.56] That's a totally fair argument.
[21.14 → 23.82] BAM with 4ChangeLog is provided by Vastly.
[24.14 → 26.02] Learn more at Fastly.com.
[26.26 → 28.54] Our feature flags are powered by Launch Darkly.
[28.54 → 30.62] Check them out at LaunchDarkly.com.
[30.86 → 32.86] And we're hosted on Leno Cloud Servers.
[33.06 → 36.64] Get $100 in hosting credit at Leno.com slash Changelog.
[37.30 → 38.36] What's up, party people?
[38.46 → 41.04] This episode is brought to you by Strap.
[41.26 → 45.18] Strap is an open source, headless CMS that contenders love.
[45.44 → 49.26] It's 100% JavaScript, fully customizable, and developer-first.
[49.64 → 53.12] Strap is more than a node framework and more than a headless CMS.
[53.56 → 57.66] It saves API development time through a beautiful admin panel anyone can use.
[57.66 → 58.90] It's open source.
[59.22 → 60.08] It's agnostic.
[60.52 → 64.08] Choose your preferred database and API options using GraphQL or REST.
[64.30 → 66.30] It's self-hosted and GDPR-compliant.
[66.62 → 69.34] Control your data, privacy, and cost at all time.
[69.58 → 70.44] It's customizable.
[70.84 → 73.12] Create content structures that flex to fit your needs.
[73.34 → 75.24] Customize the admin panel as well as the API.
[75.72 → 77.96] And extend your content management with custom plugins.
[77.96 → 81.16] To get started, head to the homepage using our special URL,
[81.36 → 83.24] strappy.io slash js party.
[83.48 → 87.28] That's S-T-R-A-P-I dot I-O slash js party.
[87.40 → 91.46] And click the Get Started button for a step-by-step guide to create a sample app using CreateStrapi app.
[91.76 → 93.62] Strap is also enterprise-ready.
[94.00 → 96.28] For those who need to unlock enterprise features and services,
[96.74 → 99.02] email js party at strappy.io
[99.02 → 104.24] and connect with Maxime, the resident expert, on guidance and a special offer for JS Party listeners.
[104.24 → 107.20] Again, that's strappy.io slash js party.
[111.28 → 121.06] This is JS Party, your weekly celebration of JavaScript and the web.
[121.66 → 127.14] We record live on Thursdays at 1 p.m. U.S. Eastern and you can be part of the show.
[127.74 → 129.94] Come hang with us in our community Slack.
[130.06 → 131.06] It's totally free.
[131.06 → 134.24] Head to changelog.com slash community and sign up today.
[134.62 → 135.88] Okay, let's get into it.
[135.92 → 137.60] Hey, it's party time, you all.
[151.10 → 152.22] Hello, friends.
[152.30 → 154.98] It's time once again for a JS Party.
[155.16 → 155.96] I'm Jared.
[156.38 → 158.32] I'm here to host a debate.
[158.32 → 162.94] This is our yep, nope format wherein we come up with a premise,
[163.20 → 166.78] we team up, and we debate either side of that premise.
[166.92 → 172.60] Whether we actually believe in the side that we're assigned, we'll find out later.
[173.12 → 174.58] I'm joined by four friends.
[174.94 → 176.00] Let's just get through it real quick.
[176.10 → 179.36] We got Nick, Abel, Divya, and Fears with us.
[179.40 → 179.94] What's up, everybody?
[181.10 → 181.48] HOI, HOI.
[182.02 → 182.66] Hey, everybody.
[182.68 → 183.16] What's going on?
[183.46 → 183.86] Hello.
[183.86 → 192.62] And our teams will be Divya and Fears versus Abel and Nick.
[193.24 → 194.08] Are you all ready?
[195.04 → 196.40] Let's do it.
[196.42 → 200.92] Do you want to do any smack talk to get started or like announce how you're about to dominate
[200.92 → 201.66] or anything like that?
[202.06 → 203.28] Like in WWE?
[204.04 → 204.34] Yeah.
[204.58 → 205.60] Take you down.
[205.60 → 207.80] I don't know what they say.
[208.06 → 210.28] Well, I used to watch it actually a lot, strangely.
[211.38 → 214.58] Or we just do a stare-down like at a weigh in for MMA or something.
[214.70 → 215.56] You just stare at each other.
[215.72 → 217.78] But that doesn't make for, oh, Nick's staring us down.
[218.06 → 219.80] Doesn't make for very good podcasting.
[220.30 → 221.08] So I'll move on.
[221.20 → 228.54] The premise for today's debate is one that is debated online and in the industry sometimes,
[228.54 → 233.60] which is that web apps are fundamentally different from websites.
[233.60 → 238.90] So we will have one team representing the yep, which is agreeing that web apps are fundamentally
[238.90 → 239.72] different from websites.
[240.08 → 242.72] And that will be team Abel.
[242.98 → 248.42] And then we'll have team Divya representing the nope side of the debate, which argues that
[248.42 → 252.22] web apps are not fundamentally different from websites.
[252.42 → 254.06] So two minutes on the board.
[254.20 → 255.90] We do this semiformal.
[256.30 → 257.54] We don't get totally dressed up.
[257.60 → 258.54] We get dressed up a little bit.
[258.54 → 263.50] That was a failed attempt at a semiformal dance joke.
[263.92 → 266.94] I'm not sure if nobody got it or if it just wasn't very funny.
[267.54 → 267.84] Oh, well.
[268.52 → 270.36] And we set some timers.
[270.52 → 274.74] So there'll be a two-minute timer for you to make your case.
[274.98 → 277.12] If you run out of time, you'll hear this sound.
[278.74 → 279.94] And your time will be up.
[280.18 → 282.08] If you run short, that's totally cool as well.
[282.14 → 284.66] Just go ahead and concede the rest of your time.
[284.66 → 285.80] And we'll go back and forth.
[286.02 → 288.04] So we have the yeps first.
[288.40 → 288.86] Team Abel.
[289.54 → 290.88] Two minutes on the board.
[291.68 → 293.50] And who's going first for Team Abel?
[293.62 → 294.36] Is it Abel or Nick?
[294.90 → 296.16] I say gentlemen first.
[296.94 → 296.96] So.
[297.18 → 297.56] Okay.
[298.00 → 298.96] Reverse chivalry.
[299.22 → 299.74] Appreciate it.
[299.86 → 299.90] Wow.
[299.90 → 300.34] Reverse.
[300.58 → 301.22] Yeah, I know.
[302.12 → 302.94] All right, Nick.
[303.00 → 304.70] You are on the board for two minutes.
[304.92 → 309.80] I was going to make a terrible joke about how, you know, men actually run the world anyway.
[310.06 → 310.82] So, oh, well.
[312.20 → 312.90] Just kidding.
[313.06 → 313.46] No, I was.
[313.46 → 315.06] Abel dropping truth bombs.
[316.02 → 319.70] I like how Abel introduces her jokes by saying she was going to make the joke and then she
[319.70 → 320.50] makes it anyway.
[320.66 → 321.42] Kind of in a reverse.
[321.60 → 322.86] Kind of sneaky joke there.
[322.98 → 323.30] All right.
[323.30 → 324.90] Nick, you're running the world.
[325.08 → 325.98] I'm running the clock.
[326.08 → 326.92] Two minutes on the board.
[327.22 → 328.10] Here you go, Nick.
[328.66 → 329.02] All right.
[329.34 → 332.08] Web apps are fundamentally different from websites.
[332.68 → 337.50] Now, my opponents here are probably going to say that to an end user, it probably is no
[337.50 → 340.34] different because you're just hitting them from a browser.
[340.68 → 343.76] You're going to a URL, and you're using whatever is there.
[344.52 → 347.76] And I'm going to say that I disagree with that because they are fundamentally different.
[347.88 → 351.98] And when you look at it from the perspective of actually building them, they're really fundamentally
[351.98 → 354.32] different, or they can be really fundamentally different.
[354.90 → 357.82] But first, I'll start by kind of trying to define what each one is.
[357.84 → 361.46] And I'll just say quickly that a website is informational.
[361.88 → 364.14] It's defined by its content.
[364.14 → 368.58] And it can be minimal on scripting, although that doesn't necessarily have to be the case.
[369.30 → 370.52] The content is typically static.
[370.88 → 374.22] And then a web app is defined by its interaction with the user.
[374.46 → 377.14] So it's more, what can the user do with this?
[377.76 → 382.56] And it definitely expects interaction, which means it probably has scripting on the heavier
[382.56 → 383.00] side.
[383.16 → 387.84] So a lot of JavaScript, a lot of other scripting languages in there potentially doing things.
[387.84 → 395.56] So I think that they are fundamentally different just in that definition, because a web app
[395.56 → 397.08] is something that you're going to interact with.
[397.40 → 401.72] And a website is going to be something that you're just going to look at and consume the
[401.72 → 401.92] data.
[402.38 → 406.94] And some examples of that is I think that GitHub is a perfect website to look at my code
[406.94 → 410.22] and to see what's going on there and to do a little bit of minimal interaction.
[410.22 → 415.98] I can press a button to do a pull request as long as everything is green, and I can't really
[415.98 → 422.32] change things like resolve conflicts or anything because it's just a website that's giving me
[422.32 → 425.76] a lot of information and letting me interact with it in a minimal way.
[426.10 → 430.38] But if I want to actually go in and change my code, I'm going to load the Code spaces web
[430.38 → 432.80] app and use that to change my code.
[433.48 → 436.36] Or Vim if I want to actually be productive.
[436.36 → 440.84] Another example would be like, I want to look at pretty web design.
[441.02 → 441.66] Oh, all right.
[442.02 → 442.46] Sorry, Nick.
[442.50 → 444.28] You wasted all your time doing Vim drops.
[446.38 → 447.96] Which is the time well spent, I will say.
[448.38 → 449.72] Great job, teammate, though.
[450.22 → 450.54] Okay.
[450.94 → 454.04] So Team Divya, you now have two minutes to respond.
[454.22 → 456.82] You can also just ignore everything Nick said and just state your case.
[457.10 → 457.84] However you want to do it.
[457.88 → 459.12] Who's going to go first for Team Divya?
[459.46 → 460.30] I can go.
[460.72 → 461.12] All right.
[461.20 → 462.60] Divya, you got two minutes on the board.
[463.04 → 463.46] It's all yours.
[463.52 → 463.76] Go ahead.
[464.28 → 464.62] All right.
[464.62 → 468.62] So websites and web applications are not fundamentally different.
[468.62 → 475.34] But I will make the argument that at one point in time, the reason why there seems to be
[475.34 → 479.36] this artificial difference is because in the beginning, websites or the way we see websites
[479.36 → 483.46] and web properties were static in the sense that you had to SSH into your server.
[483.58 → 484.90] You had to FTP your content.
[485.14 → 487.22] Everything was static, mostly HTML.
[487.62 → 493.80] But then in the early 2000s, we saw full stack frameworks coming to the fore, mainly LAMP stack
[493.80 → 494.44] and so on.
[494.82 → 497.56] And these were web applications in the sense that they were not static.
[497.72 → 499.88] They were not just plain HTML files.
[500.00 → 501.92] They were actual PHP running on a server.
[502.36 → 503.72] You needed Apache and so on.
[504.22 → 510.72] But as time moved on and as web development developed, we saw this shift where now we have
[510.72 → 515.16] software as a service where there's hosted platforms that allow you to do things that
[515.16 → 516.48] were not possible before.
[516.48 → 523.10] And what I mean by that is that the traditional sense of the website and the traditional sense
[523.10 → 525.12] of web app no longer exists.
[525.36 → 529.32] Like the difference between them is fairly, well, non-existent in this point.
[529.32 → 535.92] Because now whatever you can do in regard to this static versus dynamic is not really
[535.92 → 537.66] a dichotomy that you can talk about.
[537.82 → 542.68] So for example, Nick brought up this idea that you can't do this minimal user interaction
[542.68 → 543.56] on a static site.
[543.80 → 549.84] Well, there actually is a lot of user interaction that you can include because you have things
[549.84 → 552.40] like hosted databases that you can make calls to.
[552.90 → 554.10] Sites can start static.
[554.10 → 558.12] And then you can build up APIs using this like so many microservices.
[558.30 → 560.86] There's a whole API economy that allows you to do things.
[560.86 → 566.54] So you could have something super dynamic, like a Shopify site that is completely full
[566.54 → 567.26] end to end.
[567.38 → 571.70] And therefore, websites and web applications are not very different for us.
[571.76 → 572.72] Did you want to add?
[573.40 → 573.68] 10 seconds.
[574.46 → 574.70] Okay.
[574.80 → 575.30] 10 seconds.
[576.48 → 577.72] I'll just give back the time.
[577.80 → 579.74] I'll take the 10 seconds in the second part.
[580.90 → 581.48] All right.
[581.56 → 581.82] Fair enough.
[581.82 → 584.26] Yeah, we'll get you an extra 10 on the next time.
[584.62 → 584.96] All right.
[585.32 → 585.72] All right.
[586.32 → 588.54] That was Divya's turn.
[588.86 → 592.32] And of course, as your moderator, I'm here to provide real time fact checking.
[592.96 → 597.56] Nick asserted that you cannot perform merge conflicts on, or you cannot fix merge conflicts
[597.56 → 598.36] on GitHub.com.
[598.50 → 599.28] Fact check false.
[599.68 → 600.66] You can't actually do that.
[600.80 → 600.94] Okay.
[601.64 → 601.94] We can.
[602.60 → 602.98] Limited.
[602.98 → 605.80] You can do limit merge conflict fixes now.
[606.16 → 606.32] Can't you?
[606.42 → 608.10] Like some things they still make you check out.
[609.16 → 609.38] Do they?
[609.74 → 610.36] You can do.
[610.76 → 611.00] Really?
[611.00 → 613.06] Well, I don't know how fancy they're going to get.
[613.08 → 614.04] Yeah, I think it's limited.
[614.38 → 615.12] But anyway.
[616.18 → 616.90] If there's conflict.
[617.10 → 618.00] But Nick did not say it.
[618.04 → 619.96] So your fact-checking my fact check or what's going on?
[619.98 → 621.00] I've never seen that UI.
[621.70 → 622.16] Oh yeah.
[622.22 → 625.04] There's definitely a merge conflict resolution UI.
[625.38 → 625.64] There is.
[625.64 → 630.76] I don't know how limited it is because apparently my merge conflicts are all relatively simple
[630.76 → 632.28] because I'm so basic.
[632.96 → 634.30] When did GitHub become a web app?
[634.30 → 637.02] All right.
[637.10 → 638.28] Let's get back onto the board.
[638.28 → 641.26] We're going now back to team Abel and to Abel herself.
[641.96 → 643.00] The chivalrous one.
[643.60 → 648.66] Abel, you get one minute to respond because that's less time than the other people got.
[648.90 → 649.14] I don't know.
[649.20 → 650.04] It doesn't explain why.
[650.12 → 650.38] But go ahead.
[650.40 → 650.82] You got one minute.
[651.18 → 651.28] Sure.
[651.28 → 655.72] So I'd like to say that I'm going to take a different approach with my one minute, which
[655.72 → 663.64] is just like fundamentally assert that the web has evolved and that websites and web
[663.64 → 670.08] apps are terms used to, I think, distinguish level of complexity and expected interaction
[670.08 → 671.02] for users.
[671.64 → 678.02] And so, you know, if I'm interacting in a website, I'm really expecting a more static experience,
[678.02 → 680.42] something that's typically a read.
[681.06 → 685.44] And when I'm interacting with web apps, I'm really, you know, like there's a context shift
[685.44 → 685.78] there.
[686.04 → 687.76] There's a lot of read-write behaviour.
[688.36 → 694.32] And I think it's really important for us as web developers to push the term of web app
[694.32 → 698.92] because, you know, users have native apps on their phone, and we have progressive web
[698.92 → 707.58] apps that essentially are allowing web apps to compete with native apps in their domain.
[708.02 → 713.58] And so, you know, users essentially can't distinguish sometimes between, you know, is this button
[713.58 → 717.54] launching a browser that's full screen or is this launching a native app?
[718.02 → 720.80] And I think it's, you know, yes, that's it.
[721.22 → 721.54] Okay.
[721.98 → 724.02] I'll continue the rest of my arguments later.
[724.48 → 724.92] Okay.
[725.44 → 726.34] Good job, Mel.
[726.38 → 727.44] We go now to Fears.
[727.56 → 729.66] One minute and 10 seconds to respond.
[730.16 → 730.32] Yeah.
[730.40 → 734.50] So we're talking about whether websites and web apps are different from each other.
[734.50 → 738.62] And, you know, I'll concede right away that obviously there are different types of websites.
[739.04 → 742.94] There are static blogs on one end, you know, static sites that are basic HTML.
[743.58 → 746.84] And then on the other end, there are things like full graphic editors like Figma and there's
[746.84 → 747.96] 3D multiplayer games.
[748.54 → 751.44] So there's obviously a huge range of different types of websites.
[751.84 → 755.24] So, you know, the other side is arguing that there are differences in the types of websites
[755.24 → 755.96] that you can build.
[756.04 → 757.18] And that obviously makes sense.
[757.34 → 759.60] So, you know, our side will totally concede that.
[759.98 → 761.70] But at the end of the day, these are all just websites.
[762.22 → 763.96] You know, the web is extremely capable and amazing.
[764.10 → 766.32] It can do all kinds of types of experiences.
[766.88 → 769.32] But fundamentally, we're dealing with the same web technology.
[769.84 → 771.06] You know, a user visits a URL.
[771.28 → 772.50] The server sends some HTML.
[773.08 → 773.92] The browser displays it.
[774.06 → 774.90] It runs some scripts.
[775.40 → 777.70] And all this stuff is running inside the same thing.
[777.76 → 778.84] It's running inside a web browser.
[779.20 → 780.76] All the same browser features work.
[780.76 → 784.30] The back button, the forward button, the refresh button, the bookmarks, the history,
[784.70 → 785.48] your browser extensions.
[785.84 → 788.88] You know, you can copy and paste URLs and share websites to other people.
[788.88 → 792.40] So, you know, if we were debating whether native apps and web apps are different,
[792.74 → 793.28] I would agree.
[793.52 → 794.02] But come on.
[794.08 → 795.98] We're talking about websites here.
[796.08 → 797.48] All these different types of things are websites.
[797.80 → 800.70] Just ask the W3C or what WG or TC39.
[801.14 → 803.72] You know, they're all working on one set of standards for websites.
[803.92 → 806.36] They're not making a separate set of standards for other websites.
[806.88 → 812.78] So by this appeal to authority, you should see that we're talking about the same thing here.
[813.22 → 816.38] Not to mention, the other side has already been fact-checked and proven wrong.
[816.66 → 818.10] So take that into account.
[818.88 → 820.68] All right.
[820.76 → 822.00] Real-time fact-check here.
[822.22 → 824.50] Fears stated that the back button always works.
[825.04 → 825.58] Fact-check false.
[825.58 → 826.42] Oh my God.
[826.64 → 829.74] No, it usually works unless it's been tampered with.
[829.82 → 831.08] I think that's a fair point.
[831.44 → 833.78] I was going to argue that that's a key feature of a web app.
[834.06 → 837.30] You don't have all of that built-in functionality working.
[837.30 → 843.64] With that fact, we will take a break, and we'll begin round two right after this.
[843.64 → 861.74] This episode is brought to you by Source graph.
[862.10 → 864.64] Source graph is code search for every developer and team.
[864.88 → 868.14] Easily search across all the code that matters to you and your organization.
[868.58 → 869.54] Find example code.
[869.54 → 870.86] Explore and read code.
[871.08 → 871.96] Debug issues.
[872.34 → 873.16] And so much more.
[873.46 → 876.28] And I talked with Bung Liu, CTO and co-founder of Source graph.
[876.60 → 881.34] And asked him to share what code search is, what developers and teams are missing out on,
[881.46 → 884.50] and how Source graph provides code search to every developer in the world.
[884.50 → 891.96] If you've worked inside a Google or a Facebook or any one of these huge, well-respected technology companies,
[892.08 → 897.26] chances are you've used something like code search before, and you know the value that it provides to your team.
[897.34 → 902.80] You know that almost every single engineer inside these organizations uses it on a daily basis.
[903.18 → 907.72] If you've never had that experience, chances are you may not know what you're missing out on.
[907.72 → 912.74] You know, the term code search sounds a lot like, you know, grew or the search inside your editor.
[913.12 → 915.10] And that's what a lot of people think when they first hear it.
[915.16 → 916.86] But it's really about much more than that.
[916.96 → 923.02] It's really about connecting you as a developer to the broader universe of code and code-related data
[923.02 → 928.78] that's relevant to you, that you need at hand in order to enter that, you know, magical flow state of, you know,
[928.78 → 934.66] being in your editor, writing code quickly, making rapid progress towards that feature bug fix that you're working on.
[934.78 → 938.90] It's really about making all that contextual information accessible at your fingertips.
[939.36 → 944.70] And what that means is, think about every single repository, every single file, and every single language,
[945.04 → 948.94] every single diff, and every single open source dependency,
[949.12 → 952.04] or maybe closed source dependency that's shared across your organization.
[952.04 → 954.86] All that is searchable through a single text box.
[954.86 → 960.96] And that's really powerful because it means all this friction is eliminated between you and understanding that broader world of code.
[961.04 → 962.70] You don't have to clone stuff down to your local machine.
[962.82 → 964.54] You don't have to mess around with editor config.
[964.98 → 969.96] You don't have to be constantly bugging people on other teams who may not even know who you are
[969.96 → 973.40] in order to teach yourself how all that code works.
[973.80 → 978.00] What Source graph is, is really a way for the rest of us,
[978.00 → 981.06] the people who don't work inside the Googles, the Facebook's,
[981.06 → 987.38] to get a tool that gives us access to that sort of information readily and at our fingertips.
[987.38 → 992.62] It's really about bringing this type of tool that a lot of the larger technology companies have developed,
[992.74 → 997.36] invested hundreds of millions of dollars into making for the productivity of their own engineers,
[997.64 → 1000.66] and making that accessible to every single developer in the world.
[1000.66 → 1004.60] All right, if code search powered by Source graph sounds like something you and your team could use,
[1004.82 → 1009.60] head to info.sourcegraph.com slash changelog and click the button that says try Source graph now.
[1009.84 → 1012.94] You can install it locally, deploy it to a server, or to a cluster.
[1013.34 → 1016.56] They have a quick start guide that takes less than five minutes to install Source graph using Docker,
[1016.74 → 1018.40] so it's too easy to give it a try.
[1018.66 → 1022.04] Again, head to info.sourcegraph.com slash changelog.
[1022.04 → 1052.02] We'll be right back.
[1052.02 → 1053.94] of yep, nope, we are debating.
[1054.24 → 1056.76] Are web apps and websites fundamentally different?
[1057.20 → 1058.22] Yep, nope.
[1058.64 → 1059.50] We're here to find out.
[1059.68 → 1061.00] Divya, it is now your turn.
[1061.08 → 1062.86] You have two minutes to state a case
[1062.86 → 1065.44] or refute something that your opponent said.
[1065.96 → 1066.28] Go ahead.
[1066.66 → 1067.76] Thank you for the floor.
[1068.00 → 1071.28] As Fears mentioned, I'd like to just build upon his case,
[1071.36 → 1073.10] which is a lot of the times when we talk about
[1073.10 → 1075.62] this artificial difference between websites
[1075.62 → 1078.36] and web applications, we actually mean the same thing
[1078.36 → 1079.92] because we're talking about browsers
[1079.92 → 1082.28] and browser technology and how exactly
[1082.28 → 1085.10] these assets are viewed by users.
[1085.28 → 1086.86] And I know Amal had mentioned
[1086.86 → 1089.38] that the end user experience doesn't matter so much
[1089.38 → 1091.92] and we should focus on the building of it as a whole,
[1092.04 → 1093.88] but I think it should account as a whole
[1093.88 → 1095.88] because ultimately when you look at websites
[1095.88 → 1098.32] and maybe if you want to call it web applications,
[1098.40 → 1099.50] which is basically a website,
[1099.96 → 1101.54] ultimately it's about how you build it
[1101.54 → 1102.96] as well as how it is perceived
[1102.96 → 1104.22] from an end user's perspective.
[1104.84 → 1108.36] What I've focused on so far is the building of a website
[1108.36 → 1110.56] and a web app, same thing again.
[1110.98 → 1115.82] The idea that you can build a fully functional dynamic website
[1115.82 → 1117.46] using a lot of technologies
[1117.46 → 1120.22] without you having to artificially call it an application.
[1120.80 → 1122.70] So this difference between static and dynamic
[1122.70 → 1124.06] is kind of artificial.
[1124.34 → 1126.48] If anything, it's a range, as Fears had mentioned,
[1126.90 → 1128.94] websites can range from something incredibly static
[1128.94 → 1130.38] to something incredibly dynamic,
[1130.38 → 1132.72] like doing merge conflicts on GitHub, which is possible.
[1133.32 → 1135.46] And that is something that we should take into consideration.
[1135.46 → 1139.16] And from a user's perspective, they also don't see that difference as a whole
[1139.16 → 1142.84] because in addition to being able to see content directly,
[1142.84 → 1145.82] they can also interact directly with a website.
[1146.40 → 1148.46] And to them, it's perceivable, the difference.
[1148.54 → 1150.38] And of course, they would not know the terminology
[1150.38 → 1151.66] and the differences between them,
[1151.70 → 1155.74] but I think it matters to talk about and to focus on as well.
[1156.00 → 1157.46] I think the other thing to talk about also
[1157.46 → 1159.42] is just how websites are served.
[1159.42 → 1162.36] We often talk about websites as static,
[1162.60 → 1163.68] where it's on a CDN,
[1163.82 → 1166.86] and web apps as something that are on servers.
[1167.28 → 1169.50] And the thing is that artificial difference makes sense
[1169.50 → 1171.38] when we think of static sites
[1171.38 → 1173.80] and CDNs as hosting static properties.
[1173.96 → 1176.50] However, with the movement of edge computing,
[1176.98 → 1178.80] CDNs are getting more powerful.
[1179.04 → 1181.26] You can run a lot of logic at the CDN level.
[1181.70 → 1184.16] And so websites and web apps,
[1184.56 → 1187.36] that artificial difference is sort of removed completely
[1187.36 → 1189.92] because you can make something incredibly static
[1189.92 → 1192.44] have logic like redirects, for instance,
[1192.56 → 1195.34] where you can route a user from one asset to another.
[1196.00 → 1196.38] Very good.
[1196.58 → 1197.04] That is.
[1197.92 → 1200.44] Okay, Abel, we pitched to you two minutes to respond.
[1201.00 → 1202.70] Well, the only thing about that argument
[1202.70 → 1205.22] that was made that made sense to me
[1205.22 → 1208.82] was when she said the lines that something,
[1209.98 → 1211.60] that web apps and websites,
[1211.74 → 1213.86] it makes sense for them to be distinguished as differently.
[1214.02 → 1214.82] So I just wanted to say,
[1214.98 → 1216.72] thanks for agreeing with our argument.
[1217.36 → 1218.42] In one line, Divya?
[1219.70 → 1221.50] I think that was taken out of context.
[1221.86 → 1222.44] Yeah, whatever.
[1222.80 → 1225.22] Anyway, so case of point.
[1225.44 → 1226.30] Quick, what's the fallacy?
[1227.18 → 1227.58] Okay.
[1228.34 → 1229.00] It's the whatever.
[1229.72 → 1231.84] So I think it's really important for us
[1231.84 → 1235.12] to start educating users around the scale of the web,
[1235.36 → 1237.92] especially as users are accessing the web
[1237.92 → 1239.00] through mobile devices,
[1239.54 → 1240.92] understanding that a site,
[1241.36 → 1244.44] a simple kind of bulletin board for the web
[1244.44 → 1246.24] is really different from,
[1246.34 → 1246.62] you know,
[1246.90 → 1249.36] building complex interactive experience,
[1249.36 → 1249.92] which, you know,
[1249.96 → 1251.40] with a lot of read-write,
[1251.64 → 1252.94] a lot of data usage,
[1253.24 → 1253.46] you know,
[1253.56 → 1256.08] just potentially just more assets
[1256.08 → 1258.06] to download up front, right?
[1258.06 → 1259.96] And so I think it's important for us
[1259.96 → 1261.90] to start making the web more accessible
[1261.90 → 1264.76] in terms of its ability to kind of,
[1264.80 → 1265.16] I think,
[1265.30 → 1266.96] have its scales and tiers.
[1267.34 → 1269.12] And I think we all fundamentally agree that,
[1269.12 → 1269.68] you know,
[1269.98 → 1272.10] a web app is certainly an evolution of,
[1272.20 → 1272.46] you know,
[1272.88 → 1273.98] good old-fashioned websites,
[1273.98 → 1276.22] but they are absolutely not the same
[1276.22 → 1278.38] and nor do they take the same level of skill
[1278.38 → 1279.04] to build,
[1279.42 → 1279.66] you know,
[1279.70 → 1281.10] or create or maintain.
[1281.54 → 1281.66] You know,
[1281.70 → 1283.46] I think tossing something up on,
[1283.98 → 1284.22] you know,
[1284.30 → 1285.58] WordPress as a static site
[1285.58 → 1287.68] is not the same level of effort
[1287.68 → 1287.92] as,
[1288.04 → 1288.16] you know,
[1288.56 → 1289.26] building a
[1289.26 → 1289.82] you know,
[1289.88 → 1291.24] a Wasm game engine,
[1291.24 → 1291.76] like,
[1291.88 → 1292.36] in the browser.
[1292.90 → 1294.64] And so you have fundamentally different,
[1294.64 → 1295.30] like,
[1295.42 → 1297.80] skills needed to perform the work
[1297.80 → 1298.54] and therefore,
[1298.88 → 1299.20] you know,
[1299.26 → 1299.90] that alone,
[1300.28 → 1300.84] for me,
[1300.84 → 1304.20] it just speaks to why they are fundamentally different things.
[1304.54 → 1304.94] Yep,
[1305.04 → 1305.46] very good.
[1305.66 → 1306.60] Time's pretty much up.
[1306.66 → 1307.88] So we'll pass it now to FIRAS
[1307.88 → 1308.64] and give you,
[1308.76 → 1308.88] FIRAS,
[1309.04 → 1310.04] one minute to respond.
[1310.54 → 1310.92] Go ahead.
[1311.22 → 1312.58] So I'd like to remind everyone,
[1313.02 → 1314.80] the premise that we're debating here
[1314.80 → 1317.38] is that web apps are fundamentally different from websites.
[1317.92 → 1319.88] And I'll just focus on the word there,
[1320.04 → 1320.56] fundamental.
[1321.28 → 1323.18] The web apps are fundamentally different from websites.
[1323.84 → 1325.46] What we've heard from the other side
[1325.46 → 1328.76] is an argument that web apps and websites
[1328.76 → 1330.08] are kind of different.
[1330.08 → 1332.74] They've argued that web apps and websites
[1332.74 → 1334.00] are built a bit differently,
[1334.64 → 1336.00] that they're an evolution,
[1336.66 → 1340.86] and that users may perceive a bit of difference
[1340.86 → 1345.30] in the degree to which a website versus a web app is dynamic
[1345.30 → 1346.78] and, you know,
[1346.84 → 1348.72] the degree to which the back button may or may not work.
[1349.50 → 1351.52] But fundamentally here,
[1351.78 → 1354.20] the argument is about whether web apps
[1354.20 → 1356.68] are fundamentally different from websites.
[1356.68 → 1359.68] And I think if we were debating the difference
[1359.68 → 1361.34] between websites and native apps,
[1361.50 → 1363.64] there would be a very fundamental difference there.
[1364.02 → 1368.04] But since we're talking about an issue of degree here,
[1368.64 → 1368.78] you know,
[1368.80 → 1370.54] a website can be a little bit more apply
[1370.54 → 1371.78] or a little bit less apply.
[1372.32 → 1374.56] I argue that really,
[1374.82 → 1376.68] the difference between websites and web apps
[1376.68 → 1377.90] is really not that great.
[1377.90 → 1379.96] And it's certainly not great enough
[1379.96 → 1381.76] to rise to the level of describing it
[1381.76 → 1382.98] as fundamentally different.
[1383.50 → 1384.56] And so for that reason,
[1385.02 → 1386.84] I urge you to support our side.
[1387.68 → 1388.60] Okay, very good.
[1388.70 → 1391.66] Nick, the final word of this segment.
[1391.90 → 1392.48] You got one minute.
[1393.16 → 1393.50] All right.
[1393.50 → 1396.82] So I'll just respond to both of my opponents real quick.
[1397.10 → 1398.82] And I'll say that in Divya's argument,
[1399.40 → 1402.66] she talked about being able to do more
[1402.66 → 1403.78] at the CDN level,
[1404.28 → 1405.92] which stands for content delivery network.
[1406.10 → 1408.06] Content being the key word there.
[1408.14 → 1410.36] So you're delivering content to consume.
[1411.24 → 1412.06] And so,
[1412.56 → 1414.00] you're thinking more of websites.
[1414.68 → 1418.34] Whereas web apps would be more,
[1419.34 → 1419.80] I don't know.
[1419.80 → 1423.68] I lost where I was going with that thread.
[1423.88 → 1424.66] So I'll just go for us.
[1424.68 → 1426.00] To compute would happen somewhere else,
[1426.08 → 1426.40] typically.
[1426.94 → 1427.40] A server.
[1428.28 → 1428.78] Phone a friend.
[1429.14 → 1429.80] Thanks for that.
[1431.40 → 1432.68] And for us,
[1432.70 → 1433.62] you were talking about,
[1433.70 → 1435.72] maybe if we were comparing web apps
[1435.72 → 1437.86] to native apps, for example.
[1438.20 → 1438.90] And I would say that
[1438.90 → 1441.50] with the underlying APIs
[1441.50 → 1442.56] that you get natively,
[1442.70 → 1444.58] like battery and geolocation
[1444.58 → 1446.30] and compass and all of these,
[1446.78 → 1448.58] and with things like service workers,
[1448.58 → 1450.14] where can you draw the line
[1450.14 → 1451.06] between what's a native app
[1451.06 → 1452.40] and a web app?
[1452.46 → 1453.34] You can install them
[1453.34 → 1454.92] just like you would a regular app.
[1454.96 → 1456.24] It's just the underlying technology
[1456.24 → 1457.12] that they're built in.
[1457.60 → 1458.46] But it's,
[1458.94 → 1460.72] they are applications.
[1462.02 → 1462.42] And,
[1463.16 → 1463.58] um,
[1463.98 → 1465.74] All right.
[1465.74 → 1466.24] Saved by the bell.
[1466.58 → 1467.68] Saved by the bell there.
[1469.16 → 1470.78] We've now reached the conclusion
[1470.78 → 1471.90] of our formal,
[1472.08 → 1473.50] semiformal debate.
[1473.50 → 1474.78] I've been keeping score
[1474.78 → 1475.60] the entire time.
[1476.24 → 1477.44] And I'm now ready to claim
[1477.44 → 1478.34] the victor.
[1478.66 → 1479.72] How does this algorithm work?
[1479.96 → 1480.60] Tell us.
[1481.44 → 1482.60] He has a web application
[1482.60 → 1483.24] to do that.
[1483.24 → 1483.54] Oh yeah,
[1483.62 → 1484.30] that makes sense.
[1484.98 → 1486.08] And the winner of this debate
[1486.08 → 1486.88] is me.
[1487.34 → 1487.74] Because
[1487.74 → 1488.90] the only way to win
[1488.90 → 1489.90] is by not participating.
[1490.14 → 1491.00] And I'm the only one here
[1491.00 → 1492.10] who did not actually play.
[1492.40 → 1492.64] So,
[1493.18 → 1494.02] I win.
[1494.30 → 1495.40] Congratulations to me.
[1495.92 → 1496.78] After this break,
[1496.82 → 1497.48] we're going to come back.
[1497.52 → 1498.88] We're going to peel back the veil.
[1499.48 → 1500.22] We're going to talk about
[1500.22 → 1500.92] what our participants
[1500.92 → 1501.96] actually believe.
[1501.96 → 1502.66] Maybe get into
[1502.66 → 1503.66] a real world debate
[1503.66 → 1505.64] around the nuances here.
[1505.64 → 1506.72] because there's no nuance
[1506.72 → 1507.38] in that premise.
[1507.58 → 1508.54] But there's a lot of nuance
[1508.54 → 1509.30] in this discussion.
[1509.44 → 1509.54] So,
[1509.60 → 1510.06] we'll return
[1510.06 → 1510.82] and we will see
[1510.82 → 1512.20] what everybody really thinks
[1512.20 → 1512.76] right after this.
[1525.76 → 1526.26] What's up,
[1526.32 → 1527.00] JS Party people?
[1527.10 → 1528.04] Have you ever wondered
[1528.04 → 1529.02] if you could be offering
[1529.02 → 1529.92] a faster,
[1529.92 → 1531.28] less buggy experience
[1531.28 → 1531.88] for your customers?
[1531.88 → 1532.56] Well,
[1532.80 → 1533.72] with Ray gun Error
[1533.72 → 1534.74] and Performance Monitoring,
[1534.92 → 1536.22] you have all the information
[1536.22 → 1537.60] you need at your fingertips
[1537.60 → 1538.78] to quickly find
[1538.78 → 1539.70] and fix errors
[1539.70 → 1540.86] and performance issues
[1540.86 → 1542.04] across your tech stack
[1542.04 → 1543.10] down to the line of code.
[1543.42 → 1544.34] Ray gun makes it easy
[1544.34 → 1545.18] to monitor the impact
[1545.18 → 1546.28] of your performance improvements,
[1546.50 → 1547.58] quickly identify issues
[1547.58 → 1548.92] across web and mobile apps,
[1549.10 → 1550.80] and see how your code performs
[1550.80 → 1551.90] in the hands of your customers.
[1552.32 → 1553.58] This saves you time,
[1553.76 → 1554.54] this saves you money,
[1554.54 → 1555.98] and this saves your sanity.
[1556.36 → 1557.32] Head to raygun.com
[1557.32 → 1557.94] to join thousands
[1557.94 → 1559.30] of customer-centric software teams
[1559.30 → 1559.98] who use Ray gun
[1559.98 → 1560.94] every single day.
[1560.94 → 1562.48] Again, raygun.com
[1562.48 → 1563.22] to give them a try
[1563.22 → 1565.12] with a free 14-day trial.
[1590.94 → 1592.98] Okay, so let's talk about
[1592.98 → 1594.06] what we really think
[1594.06 → 1594.86] about this.
[1595.18 → 1596.02] The premise was
[1596.02 → 1597.20] web apps and websites
[1597.20 → 1599.34] are fundamentally different,
[1599.84 → 1600.66] and that's worded
[1600.66 → 1601.22] in such a way
[1601.22 → 1602.08] that it is defensible
[1602.08 → 1602.82] from either side.
[1602.92 → 1603.52] I think for Ross,
[1604.02 → 1605.22] keyed in on the word fundamental,
[1605.38 → 1605.62] which I thought
[1605.62 → 1606.84] was a strong argument myself,
[1606.90 → 1607.90] even though he's still lost
[1607.90 → 1608.54] at the end of the day.
[1611.08 → 1611.44] Remember,
[1611.52 → 1612.34] I was the only one that won,
[1612.48 → 1614.10] so sorry,
[1614.32 → 1615.40] but you participated,
[1615.62 → 1616.28] which was foolish.
[1616.28 → 1618.58] But what do you all really think?
[1618.72 → 1619.48] So do you make
[1619.48 → 1620.22] distinguishes?
[1620.52 → 1621.72] Are they different
[1621.72 → 1622.74] but not fundamentally different?
[1622.88 → 1624.30] Like, we can just relax
[1624.30 → 1625.20] and chat.
[1625.58 → 1626.10] What do you all
[1626.10 → 1626.94] really think about this?
[1627.16 → 1628.34] I felt like there was
[1628.34 → 1630.16] the PWA argument
[1630.16 → 1630.94] was a good one
[1630.94 → 1632.24] because it is
[1632.24 → 1634.00] the weird divide.
[1634.24 → 1635.46] Like, in a way,
[1635.58 → 1636.22] I think there's like,
[1636.36 → 1637.70] there were two sets
[1637.70 → 1638.88] of arguments in a way.
[1639.00 → 1639.66] It was like the
[1639.66 → 1641.12] websites, web apps.
[1641.26 → 1641.78] Actually, the part
[1641.78 → 1642.24] that was like
[1642.24 → 1643.40] hardly talked about
[1643.40 → 1643.82] was the
[1644.30 → 1645.70] well, we talked about it a lot,
[1645.70 → 1646.50] was like websites
[1646.50 → 1647.18] and web apps,
[1647.34 → 1648.58] like the full stack
[1648.58 → 1650.80] versus like Jam stack,
[1650.88 → 1651.98] maybe is the term.
[1652.70 → 1653.46] And then there was
[1653.46 → 1654.08] the other argument,
[1654.16 → 1655.14] which was like mobile
[1655.14 → 1656.94] and web merging,
[1657.58 → 1658.12] which I thought
[1658.12 → 1659.70] that one was more nuanced
[1659.70 → 1661.24] because the first argument
[1661.24 → 1661.66] was like,
[1661.72 → 1662.42] it's very clear
[1662.42 → 1663.36] that we're moving away
[1663.36 → 1664.16] from this website,
[1664.26 → 1664.84] web app thing.
[1665.00 → 1666.46] But I felt like with mobile
[1666.46 → 1668.40] and this idea
[1668.40 → 1669.58] of like cross-platform
[1669.58 → 1670.78] where it's like React Native,
[1671.20 → 1672.26] there's, I guess,
[1672.34 → 1673.26] Native Script still a thing,
[1673.40 → 1673.68] Ionic,
[1674.28 → 1675.44] and I guess Flutter
[1675.44 → 1676.56] is also really exciting
[1676.56 → 1677.62] for a lot of developers
[1677.62 → 1679.02] and that's just like using,
[1679.22 → 1680.54] well, Flutter is unique
[1680.54 → 1681.96] and actually everything else
[1681.96 → 1682.32] is unique
[1682.32 → 1683.26] except for React Native
[1683.26 → 1684.38] because React Native
[1684.38 → 1685.34] is like building on
[1685.34 → 1686.08] a framework
[1686.08 → 1687.84] that developers already know.
[1687.96 → 1688.52] So if you're building
[1688.52 → 1689.26] like websites,
[1689.52 → 1690.62] well, React apps,
[1691.10 → 1691.98] you would be able
[1691.98 → 1693.16] to build like something hybrid
[1693.16 → 1694.52] and there's a lot
[1694.52 → 1695.32] of other frameworks
[1695.32 → 1697.02] like Next and Next
[1697.02 → 1698.04] and they do like
[1698.04 → 1698.98] kind of this idea
[1698.98 → 1700.60] of like universal apps.
[1701.36 → 1702.08] But yeah,
[1702.08 → 1702.64] I thought that was
[1702.64 → 1703.24] a good argument,
[1703.60 → 1703.96] honestly.
[1704.60 → 1705.56] Just saying.
[1706.22 → 1707.48] Even though I still disagree.
[1709.08 → 1710.02] I think the focus
[1710.02 → 1711.02] on how the technologies
[1711.02 → 1711.70] are, you know,
[1711.76 → 1712.76] involved in building
[1712.76 → 1714.26] websites versus web apps
[1714.26 → 1715.14] is that's one way
[1715.14 → 1716.88] of looking at the argument.
[1717.42 → 1718.22] I was looking at it
[1718.22 → 1718.70] more from like
[1718.70 → 1719.76] what is the user experience
[1719.76 → 1721.16] like for the end user?
[1721.58 → 1722.64] And I think that
[1722.64 → 1723.94] when you tell people
[1723.94 → 1724.90] about a website,
[1725.14 → 1725.26] you know,
[1725.28 → 1725.50] you say,
[1725.58 → 1726.72] hey, have you seen this app
[1726.72 → 1727.60] or have you seen this site?
[1727.60 → 1729.26] The main like differentiating line
[1729.26 → 1730.06] that they think about
[1730.06 → 1730.50] in their mind
[1730.50 → 1731.64] is like whether it's a website
[1731.64 → 1732.46] or it's an app
[1732.46 → 1734.12] and an app meaning
[1734.12 → 1734.80] like a native app
[1734.80 → 1735.54] that they'll search for
[1735.54 → 1736.74] in like their app store.
[1737.64 → 1738.40] And so like
[1738.40 → 1739.72] I've built sites before
[1739.72 → 1740.74] where people are like
[1740.74 → 1741.86] searching for it
[1741.86 → 1742.54] in the app store
[1742.54 → 1742.92] and they're like,
[1742.96 → 1743.98] I can't find your app.
[1744.08 → 1744.52] And it's like,
[1744.56 → 1745.12] well, it's because
[1745.12 → 1745.80] it's a website.
[1746.00 → 1747.80] It's not an app yet.
[1748.16 → 1749.38] So, you know,
[1749.38 → 1749.90] go to Safari
[1749.90 → 1751.24] and search for it there
[1751.24 → 1751.96] and you'll find it.
[1752.32 → 1754.06] But like from a user perspective,
[1754.06 → 1755.10] I actually agree
[1755.10 → 1755.84] with the argument
[1755.84 → 1756.30] I was made
[1756.30 → 1757.28] that I was assigned to,
[1757.38 → 1757.44] you know,
[1757.46 → 1758.36] the side that I was assigned to
[1758.36 → 1760.56] because like I don't think
[1760.56 → 1761.68] users are really thinking about
[1761.68 → 1762.76] when they go to Safari
[1762.76 → 1763.72] or whatever browser
[1763.72 → 1764.28] on their phone
[1764.28 → 1765.48] and they're going to
[1765.48 → 1766.70] some kind of website,
[1766.88 → 1767.84] they're not really thinking about
[1767.84 → 1768.58] whether it's an app
[1768.58 → 1769.18] or it's a website.
[1769.70 → 1770.32] It's just that
[1770.32 → 1771.04] they're in the web browser.
[1771.92 → 1772.62] And, you know,
[1772.68 → 1773.50] like I don't know,
[1773.54 → 1774.50] I don't know how you distinguish
[1774.50 → 1776.38] there for the user
[1776.38 → 1777.20] because, you know,
[1777.26 → 1778.16] before we even had
[1778.16 → 1779.32] like the concept of a web app,
[1779.42 → 1779.92] there were like,
[1780.04 → 1780.40] for example,
[1780.50 → 1781.24] e-commerce sites
[1781.24 → 1782.28] that implemented things
[1782.28 → 1783.10] like shopping carts
[1783.10 → 1783.86] where there was like
[1783.86 → 1784.66] state on the server
[1784.66 → 1785.60] and, you know,
[1785.66 → 1786.36] you're adding things
[1786.36 → 1786.88] to your card
[1786.88 → 1787.46] and you're adjusting
[1787.46 → 1787.94] the quantity
[1787.94 → 1789.06] and you're checking out
[1789.06 → 1789.38] and you're doing
[1789.38 → 1790.50] all this very stateful stuff.
[1791.08 → 1791.50] And nowadays,
[1791.68 → 1792.84] a site or an app like that
[1792.84 → 1793.38] would be built
[1793.38 → 1794.84] with like more of the
[1794.84 → 1796.24] sort of web app-y technologies,
[1796.46 → 1796.60] you know,
[1796.62 → 1797.60] like React or something
[1797.60 → 1799.34] and you would very clearly argue,
[1799.46 → 1800.56] oh, that's obviously an app
[1800.56 → 1801.36] because it's using
[1801.36 → 1802.58] all this client-side stuff
[1802.58 → 1803.54] and all this fancy routing
[1803.54 → 1805.34] and all this really complicated
[1805.34 → 1806.96] machinery to do it.
[1807.26 → 1807.60] But, you know,
[1807.62 → 1808.78] we had that kind of stuff
[1808.78 → 1809.62] in the 90s too.
[1810.14 → 1810.74] And that was definitely,
[1810.92 → 1811.56] back in the 90s,
[1811.60 → 1812.22] I think that would have been
[1812.22 → 1813.44] called a website for sure
[1813.44 → 1814.84] because it was just a website
[1814.84 → 1815.64] with like a server,
[1815.64 → 1816.80] like a PHP server
[1816.80 → 1817.72] on the back end
[1817.72 → 1818.84] doing some stateful things.
[1819.48 → 1820.82] So this is all very,
[1820.86 → 1821.84] it's all very mixed up.
[1822.04 → 1823.36] I don't think users really
[1823.36 → 1824.70] think about the difference.
[1824.90 → 1825.44] So if we're looking at it
[1825.44 → 1826.26] from the user perspective,
[1826.48 → 1827.86] then I think it's really the same.
[1828.48 → 1829.66] To add to that,
[1829.80 → 1830.86] so when I think about
[1830.86 → 1832.76] a quintessential web app,
[1832.98 → 1833.96] maybe like the first,
[1834.32 → 1835.06] at least for me,
[1835.20 → 1836.50] major web app was Gmail
[1836.50 → 1837.92] where it was like,
[1838.42 → 1840.04] as an informed user,
[1840.20 → 1840.62] I was like,
[1840.78 → 1842.46] this seems fundamentally different
[1842.46 → 1843.78] than other things.
[1844.42 → 1846.28] But it was still in my browser.
[1847.12 → 1849.28] And as less informed users,
[1849.40 → 1851.04] as maybe more mainstream users,
[1851.18 → 1851.94] I know that,
[1852.42 → 1852.90] for instance,
[1853.12 → 1853.28] you know,
[1853.64 → 1854.98] my parents are on Gmail.
[1855.40 → 1856.52] And when I talk to them
[1856.52 → 1857.46] about, you know,
[1857.54 → 1858.52] their email,
[1858.74 → 1859.18] it's like,
[1859.26 → 1859.52] do I,
[1859.92 → 1861.04] I'll tell them
[1861.04 → 1862.26] certain configurations
[1862.26 → 1862.88] or I don't know
[1862.88 → 1863.90] if it's like blacklist
[1863.90 → 1864.66] or whatever you're going to do,
[1865.08 → 1866.08] those can only be done
[1866.08 → 1867.12] via the web
[1867.12 → 1869.34] versus inside their mail app
[1869.34 → 1870.90] that's connected to Gmail.
[1871.12 → 1872.20] Their differentiation is,
[1872.56 → 1873.78] is it in my mail app
[1873.78 → 1875.56] or is it on the web?
[1876.10 → 1876.38] You know,
[1876.46 → 1877.00] and I'll tell them,
[1877.08 → 1877.18] like,
[1877.22 → 1878.14] go to the web interface
[1878.14 → 1878.64] to do that.
[1878.70 → 1879.04] And to them,
[1879.08 → 1879.98] there's no differentiation.
[1880.24 → 1880.32] Like,
[1880.34 → 1880.90] if it's on the web,
[1880.98 → 1882.52] it's a website thing.
[1882.86 → 1883.78] And if it's in an app,
[1883.82 → 1884.42] it's an app thing.
[1884.48 → 1885.02] So I think that
[1885.02 → 1886.58] is an anecdotal
[1886.58 → 1887.62] piece of evidence
[1887.62 → 1888.80] around the concept
[1888.80 → 1889.86] that end users are like,
[1889.94 → 1890.76] is it in a website?
[1891.24 → 1892.50] Is it in a web browser or not?
[1892.58 → 1893.26] And that's probably
[1893.26 → 1894.96] where they think about it.
[1895.42 → 1895.84] Or is it,
[1895.92 → 1896.82] maybe even the other way around,
[1896.86 → 1898.02] is it in an app or not?
[1898.20 → 1899.10] Which I think PWAs
[1899.10 → 1899.70] do kind of start
[1899.70 → 1900.50] to change that calculus
[1900.50 → 1900.92] a little bit,
[1900.96 → 1901.10] you know,
[1901.12 → 1901.76] because if you find it
[1901.76 → 1902.40] in the app store
[1902.40 → 1903.48] and you install it
[1903.48 → 1904.20] onto your phone
[1904.20 → 1905.58] and it is a website
[1905.58 → 1906.58] that's being wrapped
[1906.58 → 1908.06] and doing fancy things,
[1908.06 → 1909.74] now is it different
[1909.74 → 1910.32] than a website?
[1910.78 → 1910.88] Yeah,
[1910.92 → 1911.36] it's interesting
[1911.36 → 1912.42] to think about it that way
[1912.42 → 1912.80] because,
[1913.30 → 1913.52] like,
[1913.62 → 1914.92] a lot of native apps,
[1915.00 → 1915.10] like,
[1915.14 → 1915.68] I know Facebook
[1915.68 → 1915.92] has,
[1916.02 → 1916.06] like,
[1916.08 → 1917.36] their own browser thing
[1917.36 → 1918.40] that they're working on
[1918.40 → 1919.30] and it's just like,
[1919.58 → 1920.22] it's an app,
[1920.38 → 1920.84] kind of,
[1920.92 → 1922.24] but it's an in-app browser
[1922.24 → 1923.32] window
[1923.32 → 1924.32] and so users
[1924.32 → 1925.26] are still interacting
[1925.26 → 1926.20] with the website,
[1926.66 → 1927.20] so to speak,
[1927.24 → 1928.02] but they see it
[1928.02 → 1928.96] in the app shell
[1928.96 → 1930.08] and so,
[1930.36 → 1931.18] from that perspective,
[1931.18 → 1932.14] it seems different.
[1932.46 → 1933.34] I feel like maybe
[1933.34 → 1934.34] instead of developing
[1934.34 → 1935.56] their own browser
[1935.56 → 1936.92] or browser extension
[1936.92 → 1937.42] or whatever,
[1937.56 → 1938.06] maybe Facebook
[1938.06 → 1938.70] should just give
[1938.70 → 1939.64] all of their users,
[1939.64 → 1939.98] like,
[1940.14 → 1941.00] cameras to put
[1941.00 → 1941.62] in their house
[1941.62 → 1942.68] so it'll just be easier
[1942.68 → 1944.04] to keep track of users,
[1944.20 → 1944.42] you know?
[1944.48 → 1944.92] It's called a portal.
[1946.92 → 1947.68] A portal,
[1947.78 → 1947.90] yeah,
[1947.94 → 1949.00] they already did that.
[1949.78 → 1950.18] Sorry,
[1950.24 → 1950.56] anyway.
[1950.56 → 1952.62] All right,
[1952.68 → 1953.84] I'll stop the Facebook show.
[1953.84 → 1954.02] A mouse on fire.
[1954.44 → 1954.62] No,
[1954.74 → 1955.16] it's fine,
[1955.22 → 1955.72] it's fine.
[1955.86 → 1956.58] I'll just,
[1956.76 → 1956.98] you know,
[1957.32 → 1957.64] whatever.
[1957.88 → 1958.18] It's fine.
[1958.68 → 1960.00] User privacy is important
[1960.00 → 1961.56] but not to social media companies,
[1961.72 → 1961.92] so.
[1962.06 → 1962.78] That was actually going to be
[1962.78 → 1963.48] one of my arguments
[1963.48 → 1964.58] for the distinction
[1964.58 → 1965.32] between the two
[1965.32 → 1966.50] was a web app
[1966.50 → 1966.84] is something
[1966.84 → 1967.68] that you're going to use
[1967.68 → 1968.84] to do something for you
[1968.84 → 1969.62] and a website
[1969.62 → 1970.66] is going to be something
[1970.66 → 1972.02] that is spying on you
[1972.02 → 1972.82] for their benefit.
[1974.12 → 1975.30] It's a bad argument.
[1975.70 → 1976.36] That's a really,
[1976.54 → 1976.78] yeah.
[1976.78 → 1977.42] Yeah,
[1978.16 → 1978.42] I mean,
[1978.48 → 1978.98] so for me,
[1979.02 → 1980.38] this is like super nuanced
[1980.38 → 1981.16] because,
[1981.72 → 1981.98] you know,
[1982.04 → 1983.10] I think it's very important
[1983.10 → 1984.58] that we continue
[1984.58 → 1985.78] to blur the lines
[1985.78 → 1986.44] between,
[1986.44 → 1986.90] you know,
[1986.98 → 1988.40] native desktop apps
[1988.40 → 1989.50] or native mobile apps
[1989.50 → 1989.92] and,
[1990.16 → 1990.32] you know,
[1990.56 → 1991.22] web apps,
[1991.58 → 1992.38] mainly because,
[1992.56 → 1992.76] you know,
[1993.10 → 1994.00] the web is definitely
[1994.00 → 1995.18] the better platform
[1995.18 → 1996.10] for users
[1996.10 → 1997.02] because it's open
[1997.02 → 1998.12] but it's also,
[1998.74 → 1999.62] it's got to get better.
[1999.80 → 2000.40] It's got to get better
[2000.40 → 2001.60] for like small screens.
[2001.82 → 2002.48] It's got to get better
[2002.48 → 2003.56] for other,
[2003.80 → 2004.32] you know,
[2004.56 → 2006.18] ephemeral interactions.
[2006.18 → 2006.80] I think it definitely
[2006.80 → 2008.12] does have to get better
[2008.12 → 2009.68] and I think when we think
[2009.68 → 2010.40] about the difference
[2010.40 → 2011.02] between the two,
[2011.10 → 2011.76] I think developers
[2011.76 → 2012.46] obviously talk
[2012.46 → 2013.12] and think about these things
[2013.12 → 2013.78] more often.
[2014.70 → 2015.10] Fundamentally,
[2015.94 → 2016.50] are they different?
[2016.62 → 2017.26] I don't think they're different
[2017.26 → 2018.14] because for us,
[2018.18 → 2019.02] his argument's strong.
[2019.20 → 2020.04] Like the technical ways
[2020.04 → 2020.60] that they're delivered
[2020.60 → 2021.80] and executed,
[2021.92 → 2022.92] like it's all the same technology,
[2023.06 → 2023.98] it's all the same platform
[2023.98 → 2025.58] so they aren't fundamentally different
[2025.58 → 2027.50] but what if we change that
[2027.50 → 2029.24] to its useful to distinguish
[2029.24 → 2030.38] because I think
[2030.38 → 2031.66] when we get to the side
[2031.66 → 2032.52] of somebody who's building
[2032.52 → 2033.36] one of these things,
[2033.82 → 2034.50] I think that's where
[2034.50 → 2037.62] we start to consider them different.
[2038.24 → 2039.40] Like what am I building
[2039.40 → 2040.66] and how am I trying to build it?
[2040.70 → 2041.66] What's it going to be?
[2042.00 → 2043.28] Does that change the technologies
[2043.28 → 2044.00] that I select?
[2044.06 → 2044.80] Does that change the decisions
[2044.80 → 2045.36] that I make?
[2045.72 → 2046.70] And I think at that point,
[2046.78 → 2047.68] maybe you can say fundamentally
[2047.68 → 2049.06] but at least there is
[2049.06 → 2050.10] a distinguished that says
[2050.10 → 2051.98] I'm building a rich
[2051.98 → 2054.40] in-browser experience
[2054.40 → 2056.98] which is going to be app-like
[2056.98 → 2058.68] and I can probably enumerate
[2058.68 → 2059.66] what app-like means
[2059.66 → 2061.60] and therefore I'm going to pick
[2061.60 → 2063.06] this technology stack
[2063.06 → 2064.24] or these particular ways
[2064.24 → 2064.84] of building it
[2064.84 → 2065.88] or this architecture
[2065.88 → 2067.68] in order to make that
[2067.68 → 2068.68] the best thing it can be
[2068.68 → 2071.04] versus what I'm really making
[2071.04 → 2072.12] over here is
[2072.12 → 2076.40] a content-first publishing website
[2076.40 → 2078.58] and so I might reach
[2078.58 → 2079.42] for different technologies.
[2079.56 → 2080.28] I think that's where
[2080.28 → 2080.82] it starts to become
[2080.82 → 2081.94] more of a useful way
[2081.94 → 2082.72] of thinking about things
[2082.72 → 2083.32] or do you guys think
[2083.32 → 2083.84] that even that
[2083.84 → 2084.80] is not worth distinguishing?
[2085.32 → 2086.08] I mean, everybody's
[2086.08 → 2086.92] building their websites
[2086.92 → 2088.36] like web apps these days.
[2088.58 → 2089.82] You know, even a lot of people
[2089.82 → 2091.04] are just using the same tools
[2091.04 → 2091.56] for everything.
[2092.00 → 2092.78] But I agree.
[2092.92 → 2094.90] I think that is a more useful place
[2094.90 → 2096.10] to distinguish between the two
[2096.10 → 2096.70] when you're thinking
[2096.70 → 2098.22] from a developer's perspective
[2098.22 → 2099.98] like how should I build this?
[2100.38 → 2101.56] There's definitely different decisions
[2101.56 → 2103.06] that you can make there.
[2103.42 → 2103.86] I think GitHub's
[2103.86 → 2104.90] such a fascinating case
[2104.90 → 2106.18] because it really was a thing
[2106.18 → 2107.30] that moved from
[2107.30 → 2109.00] kind of website-looking things
[2109.00 → 2109.62] to like actually
[2109.62 → 2111.46] there's some pretty rich interactions now
[2111.46 → 2112.20] although they've kept
[2112.20 → 2114.50] they're not a single-page app.
[2114.50 → 2115.66] You know, like they didn't come out
[2115.66 → 2117.34] and say we are an app, right?
[2117.38 → 2118.92] It was a place to host your code
[2118.92 → 2120.50] and of course there are tons of stuff
[2120.50 → 2121.66] that makes that possible
[2121.66 → 2122.70] which is very app-like.
[2123.24 → 2123.80] But the interface
[2123.80 → 2124.66] was very much like
[2124.66 → 2126.38] you know, search for a thing
[2126.38 → 2127.40] read a thing
[2127.40 → 2128.16] find a thing
[2128.16 → 2128.84] write a thing
[2128.84 → 2128.98] comment
[2128.98 → 2131.00] these are very basic interactions
[2131.00 → 2131.66] but over time
[2131.66 → 2132.88] it's gotten more and more rich
[2132.88 → 2134.60] and they really have blurred the lines
[2134.60 → 2135.28] between the two.
[2136.04 → 2137.08] Web 2.0
[2137.08 → 2140.04] The rise of user interactivity.
[2140.66 → 2140.76] Yep.
[2140.94 → 2142.00] Honestly, I mean it's the same
[2142.00 → 2143.18] with like if you look at websites
[2143.18 → 2146.10] that were just like purely one way
[2146.10 → 2147.42] where it's like a user
[2147.42 → 2148.28] didn't really interact
[2148.28 → 2149.64] they kind of hyperlinked
[2149.64 → 2150.70] it was just like hyperlinks
[2150.70 → 2151.38] to different things
[2151.38 → 2152.30] and everything was static
[2152.30 → 2154.56] and now a lot of sites
[2154.56 → 2155.64] are very interactive
[2155.64 → 2157.30] and in, you know
[2157.30 → 2158.00] like you have things
[2158.00 → 2159.26] like sockets and WebRTC
[2159.26 → 2160.16] that allows people
[2160.16 → 2161.06] to like communicate
[2161.06 → 2162.90] with each other
[2162.90 → 2165.08] on a single browser tab
[2165.08 → 2165.92] like session
[2165.92 → 2167.90] which I think is really cool
[2167.90 → 2168.44] and powerful
[2168.44 → 2170.08] and so the line is blurred
[2170.08 → 2170.68] definitely
[2170.68 → 2171.32] but yeah
[2171.32 → 2171.86] I think
[2171.86 → 2173.40] there's
[2173.40 → 2174.86] something to be said
[2174.86 → 2176.00] about from a user's perspective
[2176.00 → 2177.40] they might see the difference
[2177.40 → 2178.16] actually
[2178.16 → 2179.52] I think a fascinating
[2179.52 → 2180.70] argument
[2180.70 → 2181.58] that we can have
[2181.58 → 2182.18] later
[2182.18 → 2183.44] like another yup nope
[2183.44 → 2184.52] is websites
[2184.52 → 2185.06] are dead
[2185.06 → 2186.36] long live web apps
[2186.36 → 2187.44] just to like
[2187.44 → 2188.70] troll
[2188.70 → 2190.68] this argument
[2190.68 → 2191.28] further
[2191.28 → 2192.12] there you go
[2192.12 → 2192.96] write it down
[2192.96 → 2193.98] write it down
[2193.98 → 2195.00] future premise
[2195.00 → 2196.40] by the way
[2196.40 → 2196.92] out there
[2196.92 → 2197.56] listening
[2197.56 → 2198.98] we do take episode requests
[2198.98 → 2200.22] so if there's a specific
[2200.22 → 2200.86] yup nope
[2200.86 → 2202.40] premise that you want debated
[2202.40 → 2204.14] we are happy to take that up
[2204.14 → 2205.40] we're happy to invite on guests
[2205.40 → 2206.24] and other people
[2206.24 → 2207.28] to debate these topics
[2207.28 → 2207.86] not just
[2207.86 → 2209.68] us regular panellists
[2209.68 → 2211.40] so to do that
[2211.40 → 2212.16] all you have to do
[2212.16 → 2212.72] is head to
[2212.72 → 2213.50] changelog.com
[2213.50 → 2214.78] slash request
[2214.78 → 2216.38] select JS Party
[2216.38 → 2217.22] in the drop-down
[2217.22 → 2218.40] drop a topic
[2218.40 → 2219.26] drop a guest
[2219.26 → 2220.92] you can pick your panellists
[2220.92 → 2222.10] we know we've had
[2222.10 → 2223.16] specific panellists
[2223.16 → 2224.22] requested for specific topics
[2224.22 → 2224.88] we're cool with that too
[2224.88 → 2226.38] so just a shout-out
[2226.38 → 2226.70] out there
[2226.70 → 2227.22] if you're listening
[2227.22 → 2228.42] and you want to hear more
[2228.42 → 2229.56] debates like this
[2229.56 → 2230.10] with premises
[2230.10 → 2230.90] that you come up with
[2230.90 → 2232.96] please do drop us a note
[2232.96 → 2234.18] we would love to hear from you
[2234.18 → 2236.00] okay final thoughts
[2236.00 → 2237.74] before we call it a day
[2237.74 → 2238.70] this was a lot of fun
[2238.70 → 2239.88] I always enjoy
[2239.88 → 2240.74] the argumentation
[2240.74 → 2241.60] whether I
[2241.60 → 2242.88] agree or disagree
[2242.88 → 2244.76] and I always enjoy
[2244.76 → 2245.72] declaring myself the winner
[2245.72 → 2246.58] Nick you've been quiet
[2246.58 → 2247.00] recently
[2247.00 → 2247.60] do you have any thoughts
[2247.60 → 2248.52] on the distinguishes
[2248.52 → 2249.90] the usefulness
[2249.90 → 2251.10] and what you really believe
[2251.10 → 2251.80] in this context
[2251.80 → 2252.86] yeah I think
[2252.86 → 2253.88] just I think
[2253.88 → 2254.36] going back to
[2254.36 → 2255.24] maybe what Frost
[2255.24 → 2255.74] was saying
[2255.74 → 2256.60] about how
[2256.60 → 2257.74] like everything
[2257.74 → 2258.52] is kind of being built
[2258.52 → 2259.72] as a web app
[2259.72 → 2260.24] nowadays
[2260.24 → 2261.36] like that's
[2261.36 → 2262.14] that's totally true
[2262.14 → 2263.30] my blog that I haven't
[2263.30 → 2264.00] really posted on
[2264.00 → 2264.56] since 2015
[2264.56 → 2266.52] I just redid with 11d
[2266.52 → 2267.22] and it's all
[2267.22 → 2267.62] JavaScript
[2267.62 → 2268.72] but at the end of the day
[2268.72 → 2269.76] it's no JavaScript
[2269.76 → 2271.08] at all running on the page
[2271.08 → 2273.14] so it feels like an app
[2273.14 → 2274.04] that I'm working on
[2274.04 → 2275.68] but it's served
[2275.68 → 2276.26] like a site
[2276.26 → 2278.30] and to an end user
[2278.30 → 2278.96] I don't think
[2278.96 → 2280.06] that there's any difference
[2280.06 → 2281.06] so I think that's the
[2281.06 → 2282.06] the most important takeaway
[2282.06 → 2283.96] I have to say
[2283.96 → 2285.52] like to that point
[2285.52 → 2286.02] Nick
[2286.02 → 2287.08] people who can write
[2287.08 → 2288.00] or build web apps
[2288.00 → 2289.24] we tend to kind of
[2289.24 → 2290.28] over-engineer everything
[2290.28 → 2291.62] so you know
[2291.62 → 2292.42] you don't need
[2292.42 → 2294.00] React running your blog
[2294.00 → 2294.62] for example
[2294.62 → 2295.14] right
[2295.14 → 2296.48] or even an NPM
[2296.48 → 2297.90] dependency tool chain
[2297.90 → 2298.48] for example
[2298.48 → 2299.26] right
[2299.26 → 2300.18] obviously like
[2300.18 → 2301.28] you can do whatever you want
[2301.28 → 2301.88] you're an engineer
[2301.88 → 2302.74] you can do it
[2302.74 → 2304.20] but I think it's important
[2304.20 → 2305.16] for us to really think
[2305.16 → 2306.36] about the future of the web
[2306.36 → 2307.04] and for me
[2307.04 → 2307.90] the future of the web
[2307.90 → 2308.76] needs to include
[2308.76 → 2310.08] like more web authors
[2310.08 → 2311.54] and content creators
[2311.54 → 2313.14] and like what does that world
[2313.14 → 2313.86] look like
[2313.86 → 2314.52] and so
[2314.52 → 2316.34] and not just like folks
[2316.34 → 2317.54] posting content
[2317.54 → 2319.28] through social media platforms
[2319.28 → 2319.80] like TikTok
[2319.80 → 2320.34] right
[2320.34 → 2321.76] like you see the engagement
[2321.76 → 2322.48] level there
[2322.48 → 2323.94] for people who are
[2323.94 → 2324.86] interested in
[2324.86 → 2326.32] in putting things out there
[2326.32 → 2327.20] onto the web
[2327.20 → 2327.94] but you know
[2327.94 → 2329.14] I think it would be nice
[2329.14 → 2330.24] for people to be able to
[2330.24 → 2332.36] put content onto the open web
[2332.36 → 2333.74] without that intermediary
[2333.74 → 2335.18] and so you know
[2335.18 → 2336.34] and for that
[2336.34 → 2337.20] we're going to need to
[2337.20 → 2337.78] kind of I think
[2337.78 → 2339.14] have a more distinct
[2339.14 → 2339.74] simpler
[2339.74 → 2340.38] more accessible
[2340.38 → 2341.26] class of tools
[2341.26 → 2342.10] and you know
[2342.10 → 2343.38] we really want to get there
[2343.38 → 2344.42] that's actually really why
[2344.42 → 2345.54] I think the distinguished
[2345.54 → 2347.00] between sites and apps
[2347.00 → 2348.02] can help
[2348.02 → 2348.50] I think
[2348.50 → 2349.36] define those boundaries
[2349.36 → 2350.00] for people
[2350.00 → 2350.54] you know
[2350.54 → 2351.28] on the other side
[2351.28 → 2351.76] of the spectrum
[2351.76 → 2352.46] you know
[2352.46 → 2352.72] so
[2352.72 → 2353.22] maybe
[2353.22 → 2354.32] maybe if we can quantify
[2354.32 → 2355.92] the level of over engineering
[2355.92 → 2356.82] that's going into something
[2356.82 → 2357.70] we can distinguish it
[2357.70 → 2358.26] on a scale
[2358.26 → 2359.34] between website
[2359.34 → 2359.92] and web app
[2359.92 → 2360.56] right
[2360.56 → 2361.08] maybe we could do it
[2361.08 → 2361.76] on page size
[2361.76 → 2363.16] like if it's three megabytes
[2363.16 → 2364.74] of JavaScript bundle
[2364.74 → 2365.52] then it's a web app
[2365.52 → 2365.92] right
[2365.92 → 2368.24] but if it's 10 megabytes
[2368.24 → 2368.68] of images
[2368.68 → 2369.66] then it's a website
[2369.66 → 2370.54] there you go
[2370.54 → 2373.04] totally fair argument
[2373.04 → 2374.32] I also think
[2374.32 → 2374.70] there's something
[2374.70 → 2375.18] to be said
[2375.18 → 2375.78] about like
[2375.78 → 2376.96] the terminology
[2376.96 → 2377.64] so
[2377.64 → 2378.58] you know how
[2378.58 → 2379.98] web developer
[2379.98 → 2381.16] and software engineer
[2381.16 → 2381.94] like people
[2381.94 → 2383.12] choose whichever
[2383.12 → 2384.02] to use
[2384.02 → 2385.06] depending on how
[2385.06 → 2386.60] they want to be perceived
[2386.60 → 2388.22] so for example
[2388.22 → 2389.44] I'll just give you
[2389.44 → 2390.42] my biased opinion
[2390.42 → 2391.42] which is
[2391.42 → 2392.42] whenever I tell people
[2392.42 → 2393.22] I'm a web developer
[2393.22 → 2394.74] it's not as cool
[2394.74 → 2395.34] as saying
[2395.34 → 2396.46] I'm a software engineer
[2396.46 → 2397.20] because I'm just like
[2397.20 → 2398.06] I'm a software engineer
[2398.06 → 2399.32] holds a lot of gravity
[2399.32 → 2400.50] and also
[2400.50 → 2401.68] in certain countries
[2401.68 → 2402.30] you're not allowed
[2402.30 → 2403.38] to say you're a software engineer
[2403.38 → 2404.56] without an actual degree
[2404.56 → 2406.00] so there's like
[2406.00 → 2406.64] this distinction
[2406.64 → 2407.92] which I imagine
[2407.92 → 2408.56] is the same
[2408.56 → 2409.16] with websites
[2409.16 → 2409.72] and web apps
[2409.72 → 2410.60] to some extent
[2410.60 → 2412.48] where it's not as cool
[2412.48 → 2413.00] when I say
[2413.00 → 2414.32] I'm working on a website
[2414.32 → 2415.64] but when I say
[2415.64 → 2416.72] I'm working on a web app
[2416.72 → 2417.32] people are like
[2417.32 → 2418.36] that's awesome
[2418.36 → 2419.54] what are you
[2419.54 → 2420.98] like what are you using
[2420.98 → 2422.60] but when it's website
[2422.60 → 2423.00] it's like
[2423.00 → 2423.40] oh it's just
[2423.40 → 2424.20] HTML and CSS
[2424.20 → 2424.70] whatever
[2424.70 → 2425.08] right
[2425.08 → 2427.22] let me go on record
[2427.22 → 2427.86] and say websites
[2427.86 → 2428.62] are cool
[2428.62 → 2429.58] websites are cool
[2429.58 → 2430.66] come on people
[2430.66 → 2431.00] yeah
[2431.00 → 2432.02] what about the term
[2432.02 → 2432.50] programmer
[2432.50 → 2433.22] do any of you
[2433.22 → 2433.64] call yourselves
[2433.64 → 2434.06] programmers
[2434.06 → 2434.96] I call myself
[2434.96 → 2435.60] a programmer
[2435.60 → 2436.52] a programmer
[2436.52 → 2440.44] that's appropriation
[2440.44 → 2444.06] taking it back
[2444.06 → 2444.46] yeah
[2444.46 → 2445.20] you can't steal
[2445.20 → 2446.42] my culture
[2446.42 → 2446.84] yeah
[2446.84 → 2447.94] that is total
[2447.94 → 2448.68] appropriation
[2448.68 → 2450.78] so it's funny
[2450.78 → 2451.26] I've heard that
[2451.26 → 2451.74] I've been around
[2451.74 → 2452.10] long enough
[2452.10 → 2453.16] to see the transition
[2453.16 → 2454.42] and I know
[2454.42 → 2454.98] a lot of people
[2454.98 → 2456.08] actually take offence
[2456.08 → 2456.56] to certain
[2456.56 → 2458.54] like I've seen blog posts
[2458.54 → 2460.08] like do not call me a coder
[2460.08 → 2461.28] because they think coder
[2461.28 → 2462.34] is belittling
[2462.34 → 2462.92] but then like
[2462.92 → 2463.92] don't call me a programmer
[2463.92 → 2464.82] like don't call me a coder
[2464.82 → 2465.70] call me a programmer
[2465.70 → 2466.72] don't call me a programmer
[2466.72 → 2467.60] call me a developer
[2467.60 → 2468.34] don't call me a developer
[2468.34 → 2469.26] call me an engineer
[2469.26 → 2470.42] actually I'm an architect
[2470.42 → 2471.04] I feel like
[2471.04 → 2472.18] we kind of get caught up
[2472.18 → 2472.58] on these things
[2472.58 → 2473.08] and because
[2473.08 → 2474.84] each of us does
[2474.84 → 2475.84] view the world
[2475.84 → 2476.86] through a different lens
[2476.86 → 2478.00] these words have
[2478.00 → 2479.36] different connotations
[2479.36 → 2480.58] or like to me
[2480.58 → 2481.58] I don't think
[2481.58 → 2482.58] I'm a smaller
[2482.58 → 2483.34] or I don't take it
[2483.34 → 2484.40] as speaking down to me
[2484.40 → 2485.14] to call me a developer
[2485.14 → 2486.02] versus an engineer
[2486.02 → 2487.34] I couldn't care less
[2487.34 → 2488.10] but I can see
[2488.10 → 2488.84] where to for Divya
[2488.84 → 2489.72] especially if it has to do
[2489.72 → 2490.92] with like certain
[2490.92 → 2491.98] you know job opportunities
[2491.98 → 2492.38] or whatever
[2492.38 → 2493.38] her context is
[2493.38 → 2494.34] like engineer
[2494.34 → 2496.44] is more uplifting
[2496.44 → 2498.14] or she'd rather be called that
[2498.14 → 2499.18] so it's weird
[2499.18 → 2500.00] because we all kind of
[2500.00 → 2501.48] just have our own
[2501.48 → 2503.30] ways of defining
[2503.30 → 2503.82] in our heads
[2503.82 → 2504.76] what the words mean
[2504.76 → 2505.08] you know
[2505.08 → 2505.68] yeah
[2505.68 → 2506.90] I think that's a really
[2506.90 → 2507.62] interesting topic
[2507.62 → 2508.42] for a debate though
[2508.42 → 2510.14] like these words
[2510.14 → 2512.10] I remember Silicon Valley
[2512.10 → 2513.22] that show on HBO
[2513.22 → 2514.32] I remember
[2514.32 → 2516.28] getting so distinctly annoyed
[2516.28 → 2517.08] every time I heard
[2517.08 → 2518.00] the word coder
[2518.00 → 2519.56] because I was like
[2519.56 → 2520.00] you know
[2520.00 → 2521.58] I do personally feel like
[2521.58 → 2522.36] coder just
[2522.36 → 2523.46] it belittles
[2523.46 → 2524.92] like the craft
[2524.92 → 2526.20] a little
[2526.20 → 2527.26] what if coding
[2527.26 → 2528.22] was the craft
[2528.22 → 2529.30] yeah but like
[2529.30 → 2529.80] it's
[2529.80 → 2531.02] this is completely
[2531.02 → 2531.90] like subjective
[2531.90 → 2532.32] right
[2532.32 → 2533.16] that's why it's interesting
[2533.16 → 2533.74] because we all bring
[2533.74 → 2535.86] our own contextual baggage
[2535.86 → 2536.54] to the words
[2536.54 → 2536.92] you know
[2536.92 → 2537.92] and then we interpret them
[2537.92 → 2538.80] according to us
[2538.80 → 2539.46] and I've
[2539.46 → 2540.72] I used to write for a blog
[2540.72 → 2541.78] called fuel your coding
[2541.78 → 2542.34] and I thought it was
[2542.34 → 2543.06] totally cool
[2543.06 → 2544.36] and then I read somebody else
[2544.36 → 2544.80] saying that
[2544.80 → 2545.68] like you that says
[2545.68 → 2546.78] coding is not cool
[2546.78 → 2547.16] and I'm like
[2547.16 → 2547.94] well I thought it was cool
[2547.94 → 2548.44] when I wrote
[2548.44 → 2548.72] you know
[2548.72 → 2550.12] but I think
[2550.12 → 2551.72] maybe coding attaches
[2551.72 → 2553.98] to the code monkey term
[2553.98 → 2555.06] which is incredibly
[2555.06 → 2556.20] belittling
[2556.20 → 2556.58] right
[2556.58 → 2557.34] and that whole like
[2557.34 → 2558.24] hey just go grab a ticket
[2558.24 → 2558.94] and write the code
[2558.94 → 2560.08] or like that makes us seem
[2560.08 → 2560.80] like we are not
[2560.80 → 2561.72] all that we are
[2561.72 → 2562.48] and so I understand that
[2562.48 → 2563.54] maybe there's an attachment there
[2563.54 → 2564.94] but it's a fascinating
[2564.94 → 2566.00] linguistics problem
[2566.00 → 2566.88] yeah
[2566.88 → 2567.52] yeah
[2567.52 → 2568.46] I think for some reason
[2568.46 → 2569.02] I just feel like
[2569.02 → 2571.10] programmer is the purest term
[2571.10 → 2572.68] like a person who makes programs
[2572.68 → 2574.08] it doesn't have the baggage
[2574.08 → 2574.66] of coder
[2574.66 → 2576.48] and it doesn't have the
[2576.48 → 2577.30] like software engineer
[2577.30 → 2578.24] feels a little bit
[2578.24 → 2579.74] grasping to me
[2579.74 → 2580.14] like
[2580.14 → 2581.62] like
[2581.62 → 2582.22] in the same way
[2582.22 → 2583.44] that the term computer science
[2583.44 → 2584.34] is also grasping
[2584.34 → 2584.82] it's like
[2584.82 → 2586.32] oh we got to add the word science
[2586.32 → 2587.40] to make it seem like
[2587.40 → 2587.82] we're legit
[2587.82 → 2588.40] you know
[2588.40 → 2590.16] please respect us
[2590.16 → 2590.94] yeah
[2590.94 → 2591.36] yeah
[2591.36 → 2591.78] oh wait
[2591.78 → 2593.10] oh computer science
[2593.10 → 2593.42] science
[2593.42 → 2593.72] yeah
[2593.72 → 2594.44] because you're adding
[2594.44 → 2595.04] the word science
[2595.04 → 2595.40] on the end
[2595.40 → 2595.64] it's like
[2595.64 → 2596.16] oh the science
[2596.16 → 2596.78] of computers
[2596.78 → 2597.24] when really
[2597.24 → 2598.52] it could just be called
[2598.52 → 2599.12] computation
[2599.12 → 2599.94] or
[2599.94 → 2602.02] computation
[2602.02 → 2603.38] also like
[2603.38 → 2604.90] I teach computation
[2604.90 → 2606.56] I like that
[2606.56 → 2607.30] it's not about
[2607.30 → 2607.44] the
[2607.44 → 2608.10] it's not about
[2608.10 → 2609.04] like the physical
[2609.04 → 2610.12] computer hardware
[2610.12 → 2610.62] that like
[2610.62 → 2610.90] we're not
[2610.90 → 2611.94] like you wouldn't call
[2611.94 → 2613.24] I'm trying to think
[2613.24 → 2613.82] of a good example
[2613.82 → 2615.08] you wouldn't call
[2615.08 → 2615.24] it
[2615.24 → 2615.92] it's weird to call
[2615.92 → 2616.74] an entire field
[2616.74 → 2617.62] like
[2617.62 → 2618.78] to name it
[2618.78 → 2619.34] based on
[2619.34 → 2620.38] the tool
[2620.38 → 2621.08] that you use
[2621.08 → 2622.14] like the physical tool
[2622.14 → 2622.48] that you use
[2622.48 → 2623.02] oh I see
[2623.02 → 2623.92] really what we're doing
[2623.92 → 2624.26] is like
[2624.26 → 2624.92] it's more abstract
[2624.92 → 2625.62] yeah
[2625.62 → 2626.26] biology
[2626.26 → 2627.40] like assays
[2627.40 → 2627.88] you know
[2627.88 → 2628.50] or whatever
[2628.50 → 2629.68] like spectrums
[2629.68 → 2630.10] or yeah
[2630.10 → 2630.86] it's not like
[2630.86 → 2631.84] microscope science
[2631.84 → 2632.78] I think it's
[2632.78 → 2633.52] it's the same with
[2633.52 → 2634.34] like when you see
[2634.34 → 2635.40] people having degrees
[2635.40 → 2636.50] and there are some
[2636.50 → 2637.12] countries where
[2637.12 → 2638.24] they call computer science
[2638.24 → 2639.22] like informatics
[2639.22 → 2640.74] and then when you see
[2640.74 → 2641.24] that you're like
[2641.24 → 2642.08] oh they're not really
[2642.08 → 2642.84] a computer scientist
[2642.84 → 2643.32] and you're like
[2643.32 → 2643.76] they're studying
[2643.76 → 2644.40] the same thing
[2644.40 → 2645.46] informatics is a study
[2645.46 → 2646.86] of computational systems
[2646.86 → 2647.58] that's literally
[2647.58 → 2648.80] what computer science is
[2648.80 → 2649.46] yeah yeah
[2649.46 → 2649.94] literally
[2649.94 → 2651.68] yeah I have to say
[2651.68 → 2652.38] that there is a
[2652.38 → 2653.86] science-y part
[2653.86 → 2654.72] to comp sci
[2654.72 → 2656.08] and I think it starts
[2656.08 → 2657.36] at the graduate level
[2657.36 → 2658.96] like, but there's
[2658.96 → 2660.54] there's a ton of theory
[2660.54 → 2662.32] and I don't know
[2662.32 → 2663.82] if that really for me
[2663.82 → 2664.58] falls under the
[2664.58 → 2665.22] computation
[2665.22 → 2666.36] description
[2666.36 → 2667.18] you know
[2667.18 → 2668.18] ah interesting
[2668.18 → 2669.46] so it's like
[2669.46 → 2670.44] research versus
[2670.44 → 2671.76] computational theory
[2671.76 → 2672.58] could work
[2672.58 → 2674.06] instead of computer science
[2674.06 → 2674.90] but you know
[2674.90 → 2675.64] it's definitely
[2675.64 → 2676.50] there's a lot of
[2676.50 → 2676.82] theory
[2676.82 → 2678.96] actually that's so cool
[2678.96 → 2679.52] because I
[2679.52 → 2680.76] I have used that
[2680.76 → 2681.28] before
[2681.28 → 2682.84] when I talk about
[2682.84 → 2683.10] myself
[2683.10 → 2683.84] I never talk about
[2683.84 → 2684.68] myself as a computer
[2684.68 → 2685.08] scientist
[2685.08 → 2686.82] because I am not
[2686.82 → 2687.86] very theory driven
[2687.86 → 2688.90] I tend to be very
[2688.90 → 2690.60] like vocation
[2690.60 → 2691.78] like how does it work
[2691.78 → 2692.58] how do you implement
[2692.58 → 2693.08] it has driven
[2693.08 → 2694.38] and I think I've
[2694.38 → 2695.40] used this distinction
[2695.40 → 2696.16] with certain
[2696.16 → 2697.20] when I have certain
[2697.20 → 2698.24] conversations with people
[2698.24 → 2699.02] when they talk about
[2699.02 → 2700.00] like programming languages
[2700.00 → 2700.72] and I talk about
[2700.72 → 2701.64] like the syntax
[2701.64 → 2702.78] and how exactly it works
[2702.78 → 2703.82] when you're building a thing
[2703.82 → 2704.80] and the ergonomics
[2704.80 → 2705.58] and then they're coming
[2705.58 → 2705.98] from it
[2705.98 → 2707.20] isn't it beautiful
[2707.20 → 2708.48] from a research perspective
[2708.48 → 2709.72] in terms of how the language
[2709.72 → 2710.22] is organized
[2710.22 → 2710.78] and I'm like
[2710.78 → 2711.56] no, but it sucks
[2711.56 → 2712.32] to work with
[2712.32 → 2712.72] though
[2712.72 → 2714.64] well I think we have
[2714.64 → 2715.48] stumbled upon a couple
[2715.48 → 2716.10] of future
[2716.10 → 2717.04] yep nope debates
[2717.04 → 2718.56] around terminology
[2718.56 → 2719.64] and usefulness
[2719.64 → 2721.24] but quite a ways
[2721.24 → 2722.14] upstream from where
[2722.14 → 2723.00] we started today
[2723.00 → 2723.90] web apps and websites
[2723.90 → 2724.88] that being said
[2724.88 → 2725.98] a fun debate
[2725.98 → 2727.86] a fun post conversation
[2727.86 → 2730.54] and gotta give a shout-out
[2730.54 → 2731.40] to Thomas Expert
[2731.40 → 2732.30] in the chat
[2732.30 → 2733.14] for the best joke
[2733.14 → 2733.56] of the day
[2733.56 → 2734.50] which I missed on
[2734.50 → 2736.36] when Abel
[2736.36 → 2738.00] called herself a programmer
[2738.00 → 2738.62] it was
[2738.62 → 2739.80] a procreation
[2739.80 → 2741.58] a procreation
[2741.58 → 2743.80] that's so awesome
[2743.80 → 2744.66] oh my god
[2744.66 → 2745.18] our listeners
[2745.18 → 2745.96] are so smart
[2745.96 → 2746.38] yes
[2746.38 → 2747.40] so you win Thomas
[2747.40 → 2749.70] so thanks everybody
[2749.70 → 2750.20] for listening
[2750.20 → 2751.24] this is our show
[2751.24 → 2751.96] for this week
[2751.96 → 2752.74] and we'll talk to you
[2752.74 → 2753.08] next time
[2753.08 → 2758.14] support our work
[2758.14 → 2759.20] and help ensure
[2759.20 → 2760.54] JS Party continues
[2760.54 → 2761.58] into the future
[2761.58 → 2762.32] with a
[2762.32 → 2763.74] Changelog++ membership
[2763.74 → 2765.60] ditch the ads
[2765.60 → 2766.76] get closer to the metal
[2766.76 → 2768.16] and directly contribute
[2768.16 → 2769.04] to all of
[2769.04 → 2770.08] Changelog's podcasts
[2770.08 → 2770.52] at
[2770.52 → 2771.50] changelog.com
[2771.50 → 2772.62] slash plus
[2772.62 → 2773.48] once again
[2773.48 → 2773.82] that's
[2773.82 → 2774.76] changelog.com
[2774.76 → 2776.04] slash plus
[2776.04 → 2777.96] music for JS Party
[2777.96 → 2778.82] is provided by
[2778.82 → 2779.34] the mysterious
[2779.34 → 2780.44] Break master Cylinder
[2780.44 → 2781.60] and we're brought to you
[2781.60 → 2783.00] by our awesome sponsors
[2783.00 → 2784.62] thanks again to Vastly
[2784.62 → 2785.38] Linde
[2785.38 → 2786.64] and Launch Darkly
[2786.64 → 2787.98] for their continued support
[2787.98 → 2789.20] on the next episode
[2789.20 → 2790.04] I'm joined by
[2790.04 → 2791.60] Ball and special guest
[2791.60 → 2792.56] Eric Normand
[2792.56 → 2793.36] to talk about
[2793.36 → 2794.30] functional programming
[2794.30 → 2794.94] with JavaScript
[2794.94 → 2796.76] stay tuned for that
[2796.76 → 2797.64] it's coming at you
[2797.64 → 2798.72] next week
[2813.00 → 2817.54] clap your hands everybody
[2817.54 → 2818.52] if you got
[2818.52 → 2819.66] what it takes
[2819.66 → 2820.98] because I'm Curtis Blow
[2820.98 → 2822.22] and I want you to know
[2822.22 → 2823.40] that these are
[2823.40 → 2824.10] the boys
[2824.10 → 2825.54] I had to fact-check you
[2825.54 → 2826.26] cause you just stated
[2826.26 → 2827.28] that one of your arguments
[2827.28 → 2828.22] is the other team
[2828.22 → 2829.16] got fact checked
[2829.16 → 2832.18] which shows how bad
[2832.18 → 2832.44] they are
[2832.44 → 2832.80] and I was like
[2832.80 → 2833.56] well hold on
[2833.56 → 2834.58] I was about to fact-check you
[2834.58 → 2835.82] I was trying to use
[2835.82 → 2836.56] as many appeals
[2836.56 → 2836.92] to
[2836.92 → 2837.78] to like
[2837.78 → 2838.26] different
[2838.26 → 2838.46] you know
[2838.46 → 2839.04] different fallacies
[2839.04 → 2840.10] oh like different fallacies
[2840.10 → 2840.46] yeah
[2840.46 → 2841.62] so I used appeal to authority
[2841.62 → 2842.16] at the end
[2842.16 → 2843.00] and then I was gonna
[2843.00 → 2843.76] the one about them
[2843.76 → 2844.36] being fact checked
[2844.36 → 2844.78] was like
[2844.78 → 2845.22] whatever the
[2845.22 → 2846.18] one is
[2846.18 → 2846.42] where you
[2846.42 → 2848.82] disparage the other side's
[2848.82 → 2850.02] credibility
[2850.02 → 2851.10] right
[2851.10 → 2852.70] like an ad hominem
[2852.70 → 2853.16] kind of thing
[2853.16 → 2853.38] yeah
[2853.38 → 2853.80] and then
[2853.80 → 2854.56] well yeah kind of
[2854.56 → 2855.68] and then I tried to do
[2855.68 → 2857.18] I redefined
[2857.18 → 2858.62] I don't know if that is one too
[2858.62 → 2859.12] but I like
[2859.12 → 2860.38] changed the goal posts
[2860.38 → 2861.22] oh
[2861.22 → 2862.46] redefined the premise
[2862.46 → 2864.10] I also did the thing
[2864.10 → 2864.64] that Biden does
[2864.64 → 2865.06] where he's like
[2865.06 → 2865.64] come on
[2865.64 → 2868.78] or what does he say
[2868.78 → 2869.46] does he say like
[2869.46 → 2870.68] yeah come on man
[2870.68 → 2871.18] yeah he's like
[2871.18 → 2871.70] come on man
[2871.70 → 2872.04] yeah yeah
[2872.04 → 2872.50] you should have said
[2872.50 → 2873.50] that's a bunch of malarkey
[2873.50 → 2874.32] that's what you should have said
[2874.32 → 2876.16] he's like
[2876.16 → 2877.30] we're going to end up
[2877.30 → 2878.48] with so many adorable
[2878.48 → 2879.58] isms from him
[2879.58 → 2880.46] over the next four years
[2880.46 → 2881.70] come on man
[2881.70 → 2882.34] yeah
[2882.34 → 2883.60] that's funny dude
[2883.60 → 2884.02] alright
[2884.02 → 2884.86] should we hop back in
[2884.86 → 2885.90] so now we'll flip the script
[2885.90 → 2887.60] and we'll go Divya
[2887.60 → 2888.38] and Fears
[2888.38 → 2889.40] first
[2889.40 → 2890.14] is that right
[2890.14 → 2890.88] yes
[2890.88 → 2892.60] because Nick was first
[2892.60 → 2893.86] Fears did you want to go first
[2893.86 → 2894.76] or what do you
[2894.76 → 2895.64] how do you feel
[2895.64 → 2896.38] you can go
[2896.38 → 2897.04] no you can do that
[2897.04 → 2897.28] okay
[2897.28 → 2899.24] I've already dropped the mic
[2899.24 → 2899.58] so
[2899.58 → 2902.70] pick it back up
[2902.70 → 2903.52] pick it back up
[2903.52 → 2905.08] the show's not over
[2905.08 → 2911.58] I love how Nick just said
[2911.58 → 2913.50] websites have content
[2913.50 → 2914.42] and web apps
[2914.42 → 2919.34] I realized that I was making
[2919.34 → 2919.84] that argument
[2919.84 → 2921.22] I just tried to step away
[2921.22 → 2924.56] that was awesome
[2924.56 → 2925.08] yeah
[2925.08 → 2925.50] wait
[2925.50 → 2926.54] Jared you need to share
[2926.54 → 2927.26] this algorithm
[2927.26 → 2927.90] dude
[2927.90 → 2928.40] you know
[2928.40 → 2928.98] here's the algorithm
[2928.98 → 2929.92] I listen to all you guys
[2929.92 → 2930.80] and then I declare myself
[2930.80 → 2931.16] the winner
[2931.16 → 2931.94] that's the algorithm
[2931.94 → 2935.90] it's the simple algorithm
[2935.90 → 2936.44] it's just like
[2936.44 → 2937.06] while true
[2937.06 → 2937.72] Jared wins
[2937.72 → 2938.18] you know
[2938.18 → 2938.56] yeah
[2938.56 → 2938.90] yeah
[2938.90 → 2939.06] yeah
[2939.06 → 2939.62] makes sense
[2939.62 → 2939.86] so
[2939.86 → 2940.76] oh, thank you
[2940.76 → 2941.64] I'm getting congratulated
[2941.64 → 2942.54] in our chat room
[2942.54 → 2943.38] thanks Aaron
[2943.38 → 2944.46] cheers
[2944.46 → 2945.24] you know
[2945.24 → 2946.26] hey Aaron
[2946.26 → 2947.42] technically you also won
[2947.42 → 2948.40] because the only way you win
[2948.40 → 2949.26] is by not participating
[2949.26 → 2950.54] and you and I both just
[2950.54 → 2950.90] sit around
[2950.90 → 2951.44] is that how like
[2951.44 → 2952.64] kid soccer looks dude
[2952.64 → 2953.56] oh no
[2953.56 → 2954.28] it's kind of different
[2954.28 → 2955.04] everybody wins
[2955.04 → 2955.92] here nobody wins
[2955.92 → 2956.58] except for me
[2956.58 → 2957.20] and Aaron
[2957.20 → 2958.12] Yo shitake
[2958.12 → 2959.70] this is the downside
[2959.70 → 2960.70] of being an adult
[2960.70 → 2963.58] one of many
[2963.58 → 2964.34] the one thing
[2964.34 → 2965.08] that is stuck
[2965.08 → 2965.80] about being an adult
[2965.80 → 2966.98] is we don't all get to win
[2966.98 → 2968.48] our little
[2968.48 → 2970.38] participation trophies
[2970.38 → 2971.02] I mean I'll send you
[2971.02 → 2972.16] a trophy if you want it
[2972.16 → 2973.02] I don't want a trophy
[2973.02 → 2974.22] I just want orange slices
[2974.22 → 2977.44] that's the other downside
[2977.44 → 2977.92] of being an adult
[2977.92 → 2978.62] you have to buy your own
[2978.62 → 2979.34] orange slices
[2979.34 → 2980.66] you have to cut them yourself
[2980.66 → 2981.86] you want them sliced
[2981.86 → 2982.78] you have to slice them
[2982.78 → 2983.42] I know
[2983.42 → 2984.44] listen around
[2984.44 → 2985.14] fight you
[2985.14 → 2986.16] fight you
[2986.16 → 2987.52] to the guy in blue
[2987.52 → 2988.78] what you going to do
[2988.78 → 2989.36] fight you
[2989.36 → 2990.46] fight you
[2990.46 → 2991.18] and do the girl
[2991.18 → 2993.28] GAME GONE
[2993.28 → 2995.28] GAME GONE
