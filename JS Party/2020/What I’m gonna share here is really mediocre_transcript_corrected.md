[0.00 → 3.86] This is also probably unpopular because I've disagreed with it myself in the past.
[3.92 → 6.60] And I might disagree with it by the time we're done talking here.
[6.60 → 17.90] But I do believe it right now, which is that I think most of the time that you spend tweaking, customizing, optimizing your terminal, your editor.
[18.14 → 18.68] Oh, no.
[19.76 → 21.02] Your tools.
[21.82 → 24.10] Most of that is time not well spent.
[26.20 → 26.76] Amazing.
[28.60 → 29.86] How can you do this?
[30.00 → 31.76] I think most of that stuff is YAGNI.
[31.76 → 34.60] I think we spend six hours to save 60 seconds.
[34.92 → 37.46] And I think we yak shave far too much.
[37.76 → 39.90] You never know if you're going to do that 60 seconds again.
[44.04 → 46.84] Bandwidth for Changelog is provided by Vastly.
[47.22 → 49.10] Learn more at Fastly.com.
[49.34 → 52.40] We move fast and fix things here at Changelog because of Rollbar.
[52.56 → 54.24] Check them out at Rollbar.com.
[54.44 → 56.66] And we're hosted on Linde cloud servers.
[57.00 → 59.00] Head to Linode.com slash Changelog.
[59.00 → 63.02] This episode is brought to you by Rollbar.
[63.42 → 65.10] Move fast and fix things.
[65.46 → 67.46] Resolve errors and minutes and deploy with confidence.
[67.46 → 70.32] Head to Rollbar.com slash Changelog.
[70.38 → 71.22] Request a demo.
[71.36 → 72.24] Get started today.
[72.66 → 73.76] It's loved by developers.
[73.92 → 74.88] Trusted by enterprises.
[74.88 → 77.88] And most of all, we use it here at Changelog.
[78.26 → 80.92] Move fast and fix things with Rollbar.
[80.92 → 84.18] Once again, Rollbar.com slash Changelog.
[84.18 → 99.94] Welcome to JS Party, your weekly celebration of JavaScript and the web.
[99.94 → 106.38] Next week on the pod, we're celebrating Dino's big 1.0 release with Kit Kelly from the Dino Core team.
[106.64 → 109.04] Divya and Nick had an awesome conversation with Kit.
[109.22 → 112.60] Subscribe so you don't miss it at Changelog.com slash JS Party.
[112.74 → 116.46] Or search JS Party in Spotify, Apple Podcasts, etc.
[116.46 → 117.18] Dore, you know the drill.
[117.66 → 119.86] We have a great show for you starting right now.
[120.14 → 120.78] Party time, you all.
[132.30 → 133.62] Welcome back, everyone.
[133.78 → 134.48] Maybe you're out there.
[134.56 → 135.42] You're doing some dishes.
[135.98 → 138.22] Maybe you're taking a socially distanced walk.
[138.22 → 140.02] Maybe you're doing some push-ups.
[140.12 → 140.74] Come on, 10 more.
[140.80 → 141.46] You can do this.
[142.34 → 143.54] Maybe you're listening live.
[143.64 → 144.34] That means you're awesome.
[145.40 → 147.14] Whatever it is, we are here for you.
[147.28 → 148.28] We are here for a party.
[149.14 → 152.16] I'm Jared, and I'm joined by an awesome cast of characters.
[152.92 → 153.44] Divya's here.
[153.50 → 154.02] What's up, Divya?
[154.66 → 155.22] Hey, hey.
[155.98 → 157.34] And we've got Nick Needed in the house.
[157.38 → 157.84] What's up, Nick?
[158.24 → 158.78] Ahoy, hoy.
[159.54 → 160.04] Oh, hold on.
[160.06 → 160.74] I'm supposed to do this.
[160.94 → 161.50] Ahoy, hoy.
[163.30 → 165.06] Still a noob at the soundboard.
[165.40 → 166.98] And Bone Skull's here.
[166.98 → 167.58] What's up, Chris?
[168.22 → 168.62] Hello.
[168.82 → 169.26] How are you doing?
[170.12 → 170.86] Welcome back, Chris.
[170.90 → 171.38] It's been a minute.
[172.12 → 172.52] Yeah.
[172.80 → 173.10] Yeah.
[173.22 → 176.90] I've been busy with some children.
[178.70 → 179.68] Can't imagine why.
[180.84 → 181.84] Sounds rough.
[181.92 → 183.02] Maybe we should skip it.
[183.70 → 184.80] Get right into the news.
[185.02 → 187.62] So we have a three-segment show for you all today.
[187.76 → 194.80] We're going to do Story of the Week, which is all about news, links, things that have been going on in and around the JavaScript and web community.
[195.48 → 199.66] Then we're going to follow that up with some work from home tips and some unpopular opinions.
[200.58 → 205.24] And finally, we are going to give shout-outs to projects and people and things that we love.
[205.24 → 207.60] So let's hop right into the news.
[207.68 → 212.12] And it seems like Node 14, possibly the biggest news that's happened as of late.
[212.92 → 215.60] Chris, you want to give us the skinny on what's going on with Node?
[216.80 → 222.52] So Node 14 was released, I don't even know how long ago, not very long ago at all.
[222.52 → 227.44] And so there are a few things that you might want to check out.
[227.70 → 231.22] So ECMAScript module support has been in Node.
[231.88 → 233.30] It's in Node 12.
[233.54 → 234.82] It's behind a flag.
[235.80 → 240.42] But also now in Node 14, it's not behind a flag.
[240.70 → 246.76] However, it's important to know that the ECMAScript module support is still considered experimental.
[246.76 → 251.10] So that means it might break.
[251.26 → 252.50] The API might break.
[252.60 → 254.40] It doesn't mean you can't use it.
[254.68 → 256.54] It doesn't mean you shouldn't try it out.
[256.94 → 260.22] It doesn't mean that we expect it to be full of bugs.
[260.44 → 262.90] It just means the API might change.
[263.10 → 266.08] And it might change before the next major.
[266.26 → 270.38] So I don't have any visibility into, I'm not on the modules team.
[270.38 → 276.82] I don't know how they feel about it, but they were confident enough to drop the requirement for the flag.
[277.04 → 280.84] And I think actually you don't get a warning anymore either.
[281.18 → 282.42] I'm not sure exactly.
[282.72 → 283.58] I can't recall.
[283.84 → 285.98] But you might not even get a warning when you use it.
[286.24 → 290.28] But it's important to realize it's still considered an experimental API.
[290.68 → 292.60] And so, yeah, that is cool.
[292.68 → 297.80] And I think they want to push people to try it out a little bit more and give it a go.
[297.80 → 307.44] And there's still time to collect feedback and implement feedback from the community who's trying these things out and say, oh, well, this isn't working very well for whatever.
[307.70 → 310.14] And maybe it was a thing they didn't see.
[310.34 → 312.36] And so that's what this time is for.
[312.70 → 313.82] It's still experimental.
[314.16 → 316.16] And it can be changed if it needs to.
[316.68 → 319.86] The other thing, let's see, diagnostic reports.
[320.28 → 324.70] So in Node.js, diagnostic reports are also an experimental API.
[324.88 → 326.78] But now in 14, they're no longer experimental.
[326.78 → 329.68] So you can use diagnostic reports in Node 14.
[330.38 → 332.12] And you don't have to provide a flag.
[332.22 → 333.22] You're not going to get a warning.
[334.50 → 337.10] And so what these are, you can configure Node to do this.
[337.18 → 337.78] There's an API.
[338.12 → 339.46] There's command line options.
[340.34 → 345.42] And in certain situations, say, maybe there's an uncaught exception and the process crashes.
[345.62 → 350.40] Well, what you can do is configure Node to output a diagnostic report file.
[350.40 → 353.24] And so that's like a JSON blob full of information.
[353.68 → 360.58] And it's perfect for postmortem debugging especially because, you know, if your process is already dead, how are you going to debug it, right?
[360.82 → 363.80] But if you use diagnostic reports, well, there you go.
[363.90 → 368.68] There's how you can debug it because it gives you this great snapshot of the state of the system when it died.
[368.68 → 371.58] And so, yeah, diagnostic reports are now stable.
[372.44 → 375.48] I don't know too much about – I haven't worked with internationalization.
[375.64 → 380.04] But I do know that Node now in 14 ships with full ICU support.
[380.04 → 389.26] I don't know what that means except I think it just means if you need like maybe – does anybody know?
[389.44 → 391.58] Before I try to answer this, does anybody know?
[392.54 → 392.94] ICU?
[393.22 → 394.44] Anyway, so I think it's –
[394.44 → 395.68] I think that's an intensive care unit.
[396.66 → 402.54] It's – maybe there's like a set of languages or something that it did not support out of the box.
[402.62 → 405.34] And if you wanted support for those, you would have to compile them yourself.
[405.34 → 411.72] But as of 14, I believe the deal is you don't have to do that anymore because it comes with all of them.
[411.78 → 415.60] And yes, that increases the package size a little bit if you're worried about that.
[415.70 → 418.72] So that increases the size of the binary or what have you.
[419.86 → 424.28] Another cool thing – okay, so – and I actually didn't know about this before it landed.
[424.44 → 425.96] It's called async local storage.
[425.96 → 432.80] And so this is like a thing that many, many, many people have tried to do.
[433.76 → 435.96] And it's like none of these have really stuck.
[436.12 → 439.34] So if you've worked in Angular, there's – Angular 2.
[439.54 → 440.90] There's this thing called zones.
[441.38 → 447.02] And I don't really know how zones work, but it's kind of like attaching metadata to async,
[447.32 → 451.52] like an item in an async queue or an item in the event loop.
[451.52 → 453.66] And there's like a context.
[453.66 → 462.80] And you can actually do things like inspect, like, hey, when an async task is launched, then do this thing.
[462.92 → 464.82] That's kind of considered like an event or something.
[465.06 → 466.40] I don't know how zones work.
[466.70 → 469.10] As I said, there are lots of different implementations.
[469.72 → 475.96] The original one in Node was domain, which allows you to kind of like trap things at a certain level.
[475.96 → 479.04] But domain had a lot of problems and so was deprecated.
[479.38 → 485.66] And so some years later, async hooks was added to Node, which is another kind of attempt at this sort of thing.
[485.72 → 487.82] But it's very low level and difficult to use.
[488.36 → 491.82] And so now a couple more years later, async local storage was added.
[491.96 → 498.38] And this is more of a high-level API into doing really cool stuff with async tasks
[498.38 → 503.68] and being able to essentially instrument them or respond in different ways.
[504.08 → 508.70] I think like people working for APM companies or something who are like instrumenting Node
[508.70 → 510.44] might be interested in async local storage.
[510.64 → 513.28] It's an experimental API, but it looks cool.
[513.38 → 518.04] And I'm actually wanted to go check it out because I've wanted something like this for a long time
[518.04 → 522.96] to be able to detect, hey, did this code start an async process?
[522.96 → 528.84] Is it possible that this code that I just ran could throw an uncaught exception somewhere else
[528.84 → 530.08] that I might not know about?
[530.22 → 533.38] And so async local storage, you can learn about that.
[533.76 → 535.42] I assume that's how this has worked.
[535.48 → 536.58] You could do that with async code.
[536.78 → 537.82] So Node 14 is out.
[537.94 → 539.14] It's the current release.
[539.30 → 540.74] It's not LTS yet.
[541.42 → 543.54] So LTS is still 12.
[543.64 → 547.64] 14 will enter LTS, which is long-term support in October 2020.
[547.92 → 549.70] What exactly does LTS mean?
[550.02 → 552.26] It means long-term support, but how long is that long-term?
[552.26 → 553.12] What does that mean?
[554.04 → 555.28] That is a good question.
[555.48 → 556.42] I think it's two years.
[556.70 → 557.50] Yeah, two years.
[557.80 → 561.54] So a long-term support, it's going to be an active LTS for a year.
[561.68 → 566.20] So that means that 14 will get all the new features, all the new bug fixes, updates, and stuff.
[566.76 → 570.40] There's a period of maintenance after that, which is, I think, the next year,
[570.64 → 573.78] which the version will get critical bug fixes and security updates.
[573.98 → 581.10] So in October, when 14 becomes active LTS, Node 12 will be in maintenance LTS,
[581.10 → 584.60] which means it will still get these critical fixes and security fixes.
[585.16 → 590.20] But it's not going to get new features backported that 14 gets.
[590.26 → 590.50] Gotcha.
[592.00 → 592.44] Awesome.
[592.60 → 593.42] Lots of good stuff.
[593.52 → 594.10] Quick question.
[594.52 → 598.90] If you were in Node-version right now on your computer, where does everybody stand?
[599.00 → 600.32] Are we immediate updaters?
[600.76 → 607.38] Are we like, you're going to have to peel my dead, rotting corpse off of this Node version from seven years ago?
[607.38 → 608.50] What do you guys usually do?
[608.54 → 609.14] Do you upgrade right away?
[609.74 → 610.12] I do.
[610.44 → 611.18] I do as well.
[611.30 → 614.04] I always use the latest one that I can.
[615.36 → 616.80] You know, I don't know.
[617.08 → 618.60] It's just my development box.
[618.70 → 620.56] It's not like I have to worry about.
[621.06 → 623.02] I test that in CI or whatever.
[623.54 → 629.48] But, you know, I don't need to worry about deploying the bleeding edge Node or anything.
[629.96 → 631.20] Can I further make this controversial?
[631.42 → 632.58] How do you get your Node?
[633.54 → 633.94] Whoa.
[634.94 → 635.50] Good question.
[635.50 → 636.92] I use NVM.
[637.70 → 637.94] Yeah.
[638.42 → 640.68] It slows down my terminal so much.
[641.10 → 641.32] Really?
[641.94 → 644.34] Like on every command or just when using Node or what?
[644.60 → 645.56] Like startup of it.
[645.68 → 647.66] Like startup goes to seven seconds plus.
[647.96 → 648.08] Yeah.
[648.28 → 648.92] Why is that?
[648.96 → 650.68] It's like adding a bunch of stuff to the path or?
[651.32 → 651.68] Yeah.
[651.76 → 655.66] It's because I want it to be able to detect NVMRCs and automatically switch Node versions
[655.66 → 657.08] like when I CD into a directory.
[657.36 → 658.42] So that adds a lot.
[658.42 → 663.30] I think that there are commands that you can use to, or flags, sorry, that you can use to
[663.30 → 667.80] tell it not to do that and like only load NVM when you try and use Node somewhere.
[668.64 → 668.78] Gotcha.
[669.52 → 669.92] Yeah.
[669.92 → 670.94] It's slow.
[670.94 → 671.34] Yeah.
[671.74 → 674.32] I'm a brew install Node kind of guy.
[674.80 → 679.06] I've heard that that's not officially supported and there are problems with that.
[680.00 → 682.14] Well, I'm a problematic kind of guy, apparently.
[682.36 → 684.20] So if I ran it right now, I think I'm on 13.
[684.96 → 685.96] It is on their website.
[686.50 → 686.86] Oh, does it?
[687.26 → 687.66] Is it?
[687.66 → 690.06] Can you just go there and just download Node?
[691.00 → 691.44] I think so.
[691.46 → 691.76] Oh, yeah.
[692.16 → 692.38] Yeah.
[692.44 → 695.04] But then you got to go and re-download it for updated versions.
[695.12 → 695.60] Yeah, exactly.
[695.74 → 697.16] You just have to do it for every update.
[697.62 → 698.42] I'm so lazy.
[699.26 → 702.90] I can only have one version in my machine at one time and that's just okay with me.
[702.98 → 704.68] I don't use it for heavy development.
[704.80 → 709.36] I use it for the tooling and when things that I like rely on it, I don't do like active
[709.36 → 710.36] Node backend development.
[710.50 → 712.98] So I don't really need to be swishing versions very often.
[712.98 → 717.64] So I use one, a NVM, something similar to NVM.
[717.90 → 721.48] I won't say a clone, but it's called FNM, and it's written in Reason.
[721.66 → 724.88] It's written in Reason ML, and it's quite fast.
[725.28 → 726.02] Why do they do that?
[726.18 → 726.76] What was their reasoning?
[727.62 → 728.42] Good question.
[730.52 → 731.64] To use Reason.
[732.08 → 733.00] So that was the reason.
[733.76 → 734.48] That's the reason.
[735.24 → 738.32] I mean, I'm often asking myself why people use Reason.
[738.46 → 739.66] I guess that's one reason.
[739.86 → 740.54] It is.
[740.54 → 742.78] And I installed that from Homebrew.
[742.92 → 745.34] So I guess in a roundabout way, I use Homebrew too.
[746.16 → 746.58] Nice.
[747.46 → 748.10] All right.
[748.16 → 753.72] So Node 14 NVM upgrade or brew install or just go to the website and click download.
[753.92 → 755.08] We think you'll be happy.
[755.24 → 757.92] And thanks to everybody who puts all their hard work into Node.
[758.48 → 763.10] Definitely a huge ecosystem and a huge group of open source people getting involved.
[763.16 → 764.62] And we all appreciate the updates.
[765.44 → 769.14] Let's head over to Divya for some news from the Vue community.
[769.14 → 770.72] What's going on in Vue, Divya?
[771.74 → 772.02] Yeah.
[772.22 → 778.12] So recently, Evan has been doing a bunch of work on, well, Vue 3 is upcoming and there's
[778.12 → 782.50] a lot of work that's happening there, I think, alongside working on Vue 3, Evan.
[783.06 → 783.56] Vue 3?
[783.64 → 784.04] Wait a second.
[784.16 → 787.48] Remember when you wanted Vue 3 to come out before the new year?
[787.48 → 788.36] I didn't.
[788.44 → 789.44] It was K-Ball.
[789.74 → 790.68] K-Ball wanted it.
[790.70 → 794.62] We thought it might happen that it would ruin our New Year show because they might release
[794.62 → 797.16] it in the meantime between recording and shipping.
[797.84 → 798.14] Yes.
[798.28 → 799.12] It still hasn't happened.
[799.22 → 799.90] It still hasn't happened.
[800.32 → 800.54] No.
[800.74 → 802.28] So maybe end of Q2?
[802.50 → 802.94] I don't know.
[803.44 → 803.78] We'll see.
[804.00 → 804.72] We're getting close.
[804.88 → 805.06] Okay.
[805.22 → 805.48] Sorry.
[805.58 → 805.98] Cut you off.
[806.02 → 806.34] Keep going.
[806.68 → 810.38] So alongside them working on that, I think Evan has been itching to work on something different
[810.38 → 810.88] as well.
[811.02 → 811.42] Probably.
[811.64 → 811.88] Maybe.
[811.96 → 812.40] I don't know.
[812.40 → 816.64] So he came up with this new project called Site that he released.
[817.74 → 821.34] I almost think it's like a side project that he was doing because he talked about working
[821.34 → 825.10] on it all night, like two weeks ago or something like that.
[825.22 → 830.96] And the whole point of Site is that it's a no-bundler dev server for Vue single file components.
[831.68 → 835.62] So generally, whenever you deal with any single page application, you often have a bundling
[835.62 → 839.78] step, which takes up, you know, it can take time because you have to compile everything.
[839.78 → 844.24] And then the larger your application is and the larger your files are, part module reloads
[844.24 → 847.52] can take a while because it's essentially doing full reload, full page reload.
[848.24 → 852.00] And so what this does is it takes advantage of ES import syntax.
[852.50 → 856.86] So it's serving all your modules directly from the browser, and it does the resolution
[856.86 → 859.24] with like the script module syntax.
[859.80 → 861.06] So that's pretty cool.
[861.34 → 864.18] The downside is that it doesn't support legacy browsers at all.
[864.18 → 871.22] Like the whole point of Site is purely for just like working with like ESM modules and
[871.22 → 877.16] like things that are very much, I think, edge technology still, like they're not fully embraced
[877.16 → 877.90] by the community.
[878.12 → 881.82] And there's no, I think the whole point of this is just purely for development purposes.
[881.82 → 884.42] So like you would just use this for development.
[884.56 → 891.68] I think there's probably, if this becomes popular, there will be work done to make it shippable
[891.68 → 896.40] as production code, but that is not recommended at the moment, just because there's a lot of
[896.40 → 897.88] things that need to be thought through.
[898.48 → 904.34] But the upside is that because you are doing module resolution for files
[904.34 → 910.18] that are requested, only for files requested, the HMR is much faster because you're not bundling
[910.18 → 912.56] the entire thing, the entire application and rerunning it.
[912.80 → 913.90] So it's a bit faster that way.
[914.40 → 917.60] And then of course, there's just like, it's a cool thing to be working on.
[917.60 → 918.96] And I think it's fascinating.
[919.74 → 923.58] It uses native ES imports, which I think not a lot of people do at the moment.
[924.08 → 926.14] There are some things that they added.
[926.48 → 926.82] So like-
[926.82 → 927.44] It's a growing trend, right?
[927.46 → 928.54] It's a growing trend for sure.
[928.54 → 931.36] So it's really cool to see people actually using it in their applications.
[931.86 → 935.14] Well, Evan to be pushing people to be like using it.
[935.48 → 940.62] And I think this will help like grow adoption overall because not a lot of people are aware
[940.62 → 944.20] of the possibilities of ESM and ES imports and stuff like that.
[944.20 → 948.72] Like you might use it because of the syntax if you use like various node packages and
[948.72 → 949.02] so on.
[949.06 → 955.68] But I think this is really cool and interesting to see, especially as a like kind of a first
[955.68 → 957.28] prototype of what is possible.
[957.62 → 958.96] And yeah, we'll see where it goes from there.
[959.00 → 963.52] I'm not sure like in terms of future of where this is going, but I think the whole point of
[963.52 → 969.96] how this was built was purely as a proof of concept to see if it was possible and to optimize
[969.96 → 971.14] for development purposes.
[971.14 → 974.86] Lots of interesting technology.
[975.44 → 980.26] And I think it's also like, I mean, I don't want to speak for anyone, but it's also kind
[980.26 → 986.40] of a stopgap for anyone who's just like really excited for Vue 3 and kind of tired because
[986.40 → 989.86] the release date is not anywhere near.
[990.44 → 991.50] It's like, here you go.
[991.62 → 994.92] Here's a really quick thing for you to work on while you continue.
[994.92 → 999.88] I mean, Vue 3 is like pretty much in beta, so you can actually work on it now.
[1000.00 → 1002.42] It's not like behind a flag or anything like that.
[1002.52 → 1004.50] So if you really want to use it in production, you can.
[1004.62 → 1006.30] It's just not officially released.
[1006.88 → 1007.56] Very cool.
[1007.74 → 1014.44] Well, sort of back to Node land as we go to Nick and you've got a story that you promised
[1014.44 → 1015.60] would be pretty interesting.
[1016.26 → 1017.20] Why don't you tell us about that?
[1017.20 → 1023.46] Well, yes, for a total of three hours last Saturday, which would be the 25th of April,
[1023.88 → 1030.10] there were several broken projects in Node, including Create React App, because they relied
[1030.10 → 1034.62] on a very small one line function called is Promise.
[1034.80 → 1036.06] Like déjà vu all over again.
[1036.32 → 1036.84] Right.
[1036.84 → 1039.48] And so that's pretty interesting.
[1039.90 → 1045.52] The interesting takeaways from this are in 2020, which is the year we are in now, even
[1045.52 → 1047.00] though time has no meaning anymore.
[1047.32 → 1048.00] Last year on Earth.
[1050.12 → 1051.42] Potentially our last year.
[1052.12 → 1052.64] Yes.
[1053.60 → 1059.46] That we're still reliant on a single line function to find out if something is a promise, which
[1059.46 → 1062.24] promises have been built into the language since 2015 now.
[1062.24 → 1066.52] So it seems crazy that there are still projects, including Create React App, which was created
[1066.52 → 1070.70] three years and nine months ago, according to the repo I just cloned.
[1072.08 → 1072.94] Why it's necessary.
[1073.00 → 1076.90] And I haven't looked into Create React App, and maybe it's being pulled in by some dependency
[1076.90 → 1079.12] of a dependency several layers down the chain.
[1079.22 → 1079.58] Right.
[1080.00 → 1081.92] But it is interesting.
[1082.20 → 1084.72] It's not really like it's just a single line function.
[1084.72 → 1086.86] So there's not really much that can break.
[1086.96 → 1091.62] But the big takeaway here from this for me was I kind of have no idea what's going on in
[1091.62 → 1092.14] Node anymore.
[1092.74 → 1095.34] Because it wasn't the code that broke.
[1095.40 → 1097.32] It was the metadata about the code.
[1097.52 → 1098.82] I was going to ask, why did it break?
[1099.36 → 1099.58] Yeah.
[1099.66 → 1105.48] Parts of the package.Jason and the author of it updated the code so that it could be natively
[1105.48 → 1107.40] pulled in with ES modules.
[1107.76 → 1114.78] So you could just say import is promise without having to have the whole transpire, or I can't
[1114.78 → 1115.88] remember the term for it.
[1115.88 → 1122.56] But being able to pull the CJS module and use it as if it were an ES module.
[1122.96 → 1123.96] So he updated that.
[1123.96 → 1130.98] And there are just a lot of metadata issues that went wrong with that just because the project
[1130.98 → 1131.94] had an NPM ignore.
[1132.12 → 1135.24] So he assumed that it wouldn't have a files array in package.Jason.
[1135.24 → 1137.18] I won't go through all the changes.
[1137.60 → 1138.96] You can read the postmortem for that.
[1138.96 → 1143.74] But there's just a lot of metadata that I don't know about since the last time I published
[1143.74 → 1144.40] something on NPM.
[1144.90 → 1147.78] So it's something to look out for if you're going to be doing that soon.
[1149.16 → 1150.56] So, hey, Nick, I wanted to...
[1150.56 → 1154.72] People might not understand why is promise even a thing.
[1154.72 → 1157.14] So why doing a thing is promise?
[1157.40 → 1160.74] So as you said, promises have been in the language since 2015, right?
[1161.10 → 1161.46] Right.
[1161.92 → 1167.46] So, but promise implementations have been in the language since in the ecosystem since
[1167.46 → 1168.56] long before that.
[1168.76 → 1174.18] Like Google and before that Q, if you ever used Q and others.
[1174.46 → 1175.36] jQuery deferred.
[1175.46 → 1180.78] So if everybody was using native promises, you could say, okay, is this object, you could
[1180.78 → 1183.12] use the instance of keyword or something, right?
[1183.12 → 1185.74] And you could say instance of promise and it would check.
[1186.18 → 1190.70] But if you're using it, and a lot of packages still do because, you know, Bluebird for one
[1190.70 → 1192.90] has a lot of features, native promises don't.
[1193.48 → 1196.90] And so if you're using a Bluebird promise, it's not a native promise.
[1197.18 → 1202.22] And so you can't use instance of promise because that won't work.
[1202.32 → 1203.90] But what you do have, it is a promise.
[1204.04 → 1205.10] It works like a promise.
[1205.30 → 1207.02] It, you know, it's a duck type promise.
[1207.46 → 1212.12] And so that's why you need something like is promise because you need to be able to look
[1212.12 → 1215.82] at an object and say, well, you know, is this a promise like object?
[1216.18 → 1220.58] And the way if you look at is promise, the way they do that, they check for a then function.
[1220.78 → 1221.14] That's it.
[1221.24 → 1221.40] Yeah.
[1222.38 → 1224.88] If somebody has a then function, it's a promise.
[1225.56 → 1229.30] And that's about as best we can do in JavaScript, unfortunately.
[1229.96 → 1230.28] Wow.
[1230.28 → 1237.86] So I would submit that a better solution than a package called is promise is a piece of
[1237.86 → 1243.84] documentation or a blog post that's the number one hit on your favourite search engine of choice
[1243.84 → 1245.84] that says, how do I find out if it's a promise?
[1246.10 → 1248.88] And then it says, check for a then function.
[1249.10 → 1251.56] Wouldn't that route around issues like these?
[1251.66 → 1253.28] And we could all just check for a then function.
[1253.28 → 1257.56] So the thing with these one line packages, and I haven't looked at this one, but I've
[1257.56 → 1259.32] used plenty of one line packages before.
[1259.42 → 1263.18] And the thing is that one line is going to have like 200 lines of tests.
[1264.08 → 1266.34] They will test the hell out of that one line.
[1266.42 → 1270.58] And if you write that one line in your code, I can guarantee you're not going to do that.
[1271.04 → 1272.60] And so that's like, that's the benefit.
[1272.70 → 1275.78] It's, it's a trade-off, of course, because something like this can happen.
[1276.36 → 1276.44] Right.
[1276.50 → 1279.40] But what if the blog post author also wrote the test suite?
[1279.98 → 1281.36] This is actually correct.
[1281.36 → 1282.66] Like this is the way you do it.
[1283.80 → 1284.18] Yes.
[1284.22 → 1289.58] You could post the code, and you could post all the tests in a blog post, and you could
[1289.58 → 1291.08] go around copying and pasting that.
[1291.98 → 1295.92] Or you could download that package from, from NPN if it was published.
[1296.60 → 1299.44] For a while until, until something goes wrong with that package.
[1299.54 → 1300.54] So it's a trade off.
[1300.84 → 1301.14] Right.
[1301.72 → 1306.18] The problem with my solution is when the best practices change, my code doesn't change.
[1306.26 → 1306.46] Right.
[1306.60 → 1309.62] So if it becomes a better way of testing it or that way breaks.
[1309.62 → 1314.02] And once I go find that blog post and update my little snippet, I still have my old copy
[1314.02 → 1314.72] pasted version.
[1315.12 → 1315.52] Right.
[1315.52 → 1316.74] And so maybe it breaks down the road.
[1316.90 → 1317.04] So.
[1317.56 → 1317.80] Yeah.
[1318.18 → 1318.44] Yeah.
[1319.08 → 1323.94] Part of like the social contract with these one-liners is if there becomes a better way
[1323.94 → 1325.64] to do it, they'll, they'll update.
[1325.98 → 1326.36] Right.
[1327.74 → 1329.36] Or they'll take your site down.
[1329.62 → 1330.68] Your build at least.
[1331.50 → 1333.04] We'll break or whatever happens.
[1333.20 → 1334.32] So that was just a few hours.
[1334.40 → 1335.84] So that they just, what happened, Nick?
[1335.84 → 1337.64] Yeah, it was a total of three hours.
[1337.86 → 1342.84] It was pretty quickly resolved through removing versions from NPM that were published that
[1342.84 → 1345.54] were bad and replacing them with, with newer versions.
[1345.74 → 1350.66] And I think it fully incremented to a new major version because of it as it probably should
[1350.66 → 1350.94] have been.
[1351.30 → 1353.32] So yeah, it was only three hours on a Saturday.
[1353.48 → 1358.50] So probably not a huge disruption anywhere, but still something to think about.
[1358.50 → 1364.60] And now I will just ask for your support as I go pitch my first TC39 proposal of a promise.is
[1364.60 → 1365.80] promise implementation.
[1367.34 → 1368.76] Just like array.disarray.
[1369.00 → 1369.12] No.
[1369.68 → 1371.10] I mean, it would be nice, but.
[1371.52 → 1371.66] Yeah.
[1372.00 → 1373.24] You have my full support, Nick.
[1373.56 → 1373.78] Yeah.
[1374.24 → 1380.58] You probably can't account for it to, to match bluebird promises or, or like jQuery deferred
[1380.58 → 1381.30] or anything like that.
[1381.68 → 1385.30] But can't you just draw a line in the sand and say backwards compatible to this point and
[1385.30 → 1388.02] then we don't care about those anymore.
[1388.38 → 1390.48] If you care about those, here's the is promise package.
[1391.30 → 1392.18] The answer is yes.
[1393.40 → 1394.68] Silence means yes.
[1394.86 → 1395.24] I win.
[1396.20 → 1397.24] All right, let's take a break.
[1397.24 → 1399.32] We'll be back with some unpopular opinions.
[1406.14 → 1407.70] Big news, nerds.
[1407.88 → 1411.00] Gatsby's highly anticipated incremental builds are here.
[1411.66 → 1415.20] If you're already deploying with a Gatsby cloud, you've been enjoying builds up to 20
[1415.20 → 1416.88] times faster than other solutions.
[1417.36 → 1420.44] With incremental builds, that number moves two orders of magnitude.
[1421.20 → 1422.84] We're not talking 50 times faster.
[1423.10 → 1424.74] We're not talking a hundred times faster.
[1424.88 → 1427.62] Not even 500 times faster.
[1428.06 → 1432.40] After years of invested engineering and months of testing, the Gatsby team has been able to
[1432.40 → 1433.04] perform builds.
[1433.10 → 1433.74] Are you ready for it?
[1434.14 → 1436.60] Up to 1000 times faster.
[1437.00 → 1439.94] That is an average build time of less than 10 seconds.
[1439.94 → 1444.24] This is the feature we've all been waiting for and there's never been a better time to
[1444.24 → 1445.16] try Gatsby cloud.
[1445.60 → 1448.52] The best part is it's 100% free to get started.
[1448.68 → 1449.86] So you can put away your credit card.
[1449.96 → 1450.74] You're not going to need it.
[1450.96 → 1454.16] Go to Gatsbyjs.com slash changelog to get started.
[1454.50 → 1458.14] Once again, that's Gatsbyjs.com slash changelog.
[1458.14 → 1467.36] So we've got some work from home tips.
[1467.46 → 1468.92] We've got some unpopular opinions.
[1469.02 → 1474.38] We're going to start on the wholesome, happy isolation side, which is working from home.
[1475.16 → 1478.20] And this is going to be Chris and Nick sharing a couple of tips on working from home.
[1478.24 → 1482.86] And then we're going to get into the squared circle, the octagon, and share some unpopular
[1482.86 → 1484.18] opinions from Divya and me.
[1484.34 → 1486.00] Let's start with Nick.
[1486.08 → 1486.76] What you got, Nick?
[1486.76 → 1488.14] Working from home, what should we be doing?
[1488.74 → 1493.02] Yeah, I've been working from home for a long time, but something that's new is children
[1493.02 → 1494.26] at home all the time.
[1494.56 → 1499.60] And so I've been really trying to block out those children when I'm trying to get done,
[1499.64 → 1503.92] not negatively, just I don't want to hear them for a while, especially when they're
[1503.92 → 1507.04] getting up for breakfast and crying about everything.
[1507.66 → 1509.18] My kids are very young, one in three.
[1509.58 → 1510.52] So that makes sense.
[1510.96 → 1515.52] So I've been trying to find some good music that helps me get in the flow.
[1515.52 → 1519.82] I've used services like Brain.fm and just listen to Apple Music and such.
[1520.28 → 1525.52] But I found some soundtracks on Apple Music that I really like, and that's the West world
[1525.52 → 1528.08] soundtracks from the hit HBO show.
[1528.50 → 1530.48] Seasons one and two soundtracks are both great.
[1530.56 → 1531.48] There are no words in them.
[1531.98 → 1536.78] And they're like string quartet versions of popular songs like Black Hole Sun from Sun
[1536.78 → 1540.32] Garden, Paint It Black from the Rolling Stones, and several others.
[1540.90 → 1547.04] So yeah, definitely fun, easy to listen to, easy to zone out to music is perfect for
[1547.04 → 1547.70] working from home.
[1548.38 → 1548.78] Awesome.
[1548.86 → 1551.60] And you don't have to be a watcher of the show to get it.
[1552.04 → 1552.62] Not at all.
[1553.06 → 1553.26] Yeah.
[1553.62 → 1556.02] If you like Black Hole Sun, you're going to like this.
[1556.52 → 1556.74] Yeah.
[1557.98 → 1558.70] That's great.
[1559.18 → 1560.10] Definitely going to check that out.
[1560.24 → 1563.68] Chris, you've been working from home under adverse circumstances.
[1564.10 → 1564.48] Yes.
[1564.48 → 1566.40] You also share a lot of tips in the past.
[1566.46 → 1567.80] We have a great blog post from you.
[1568.42 → 1570.08] Pro tips for dads working from home.
[1570.38 → 1570.74] Yeah.
[1570.76 → 1573.00] Anything new for us or maybe old?
[1573.82 → 1575.78] All my good tips are in that blog post.
[1575.88 → 1577.92] So what I'm going to share here is really mediocre.
[1578.58 → 1578.86] Okay.
[1579.22 → 1584.16] So my situation is kind of like Nick's with two children.
[1584.34 → 1587.42] They're not as small, but one of them is.
[1587.42 → 1593.54] At any rate, it's important to be able to tune out somehow.
[1593.54 → 1598.78] So I love my active noise-cancelling headphones.
[1599.20 → 1599.36] Okay.
[1599.52 → 1601.58] I also use Brain FM a lot.
[1601.98 → 1608.94] They added like low-fi, chill, hip-hop beats or whatever to their offering.
[1609.30 → 1612.04] And I've been listening to a lot of that one.
[1612.62 → 1614.08] And Brain FM, I don't know.
[1614.16 → 1615.04] It works for me.
[1615.04 → 1620.54] So yeah, the thing is like I was trying to share an office with my wife.
[1620.60 → 1624.72] And my wife's job, for her job, she's in meetings literally all day.
[1624.72 → 1636.04] And so it is incredibly hard to come into the same tiny room and get anything done when there's somebody like right next to you yakking.
[1636.26 → 1642.84] What we ended up doing was like setting up a temporary desk for her elsewhere in the house.
[1643.22 → 1646.56] And that's been much better.
[1646.70 → 1648.74] I mean, it's better for her.
[1648.86 → 1649.80] It's better for me.
[1649.80 → 1654.24] When you're stuck in a house with a bunch of other people, and this is what's different, right?
[1654.70 → 1657.38] I'm used to working from home, but I'm here by myself.
[1657.56 → 1659.38] But now that's not how it works anymore.
[1659.94 → 1660.98] It's everybody's here.
[1661.10 → 1664.22] And so you've got to have like a space to yourself.
[1664.42 → 1668.30] You've got to have like a quiet space, a space where there's nobody else.
[1668.54 → 1677.48] Unless you and your spouse, or what have you been working at the same company on the same team on the same project, like you probably don't want to be sharing a space, right?
[1677.48 → 1685.80] So it's like if you're finding yourself in a situation where you're in close quarters, and you need to get work done, somebody's got to go somewhere else.
[1686.28 → 1687.14] Like, I don't know.
[1687.18 → 1689.26] I was about to move into the garage, for example.
[1689.64 → 1690.86] Like, I don't know.
[1691.04 → 1694.08] So it's just like, yeah, you really need that.
[1694.14 → 1695.80] And this is better for your mental health.
[1696.66 → 1699.66] And this goes for like, it's not just an introvert thing.
[1699.66 → 1708.76] It's just like, I don't know how people in open office plans do it because it seems like it's kind of like that, except it's not like a din, right?
[1708.84 → 1713.02] It's not like this like a million voices all at once.
[1713.14 → 1716.20] It's like one loud voice next to you.
[1716.30 → 1718.18] And it's impossible to tune that out.
[1718.38 → 1720.44] So you need your own space.
[1720.54 → 1721.20] That's my tip.
[1721.20 → 1722.50] Very good.
[1722.62 → 1724.00] Now we're going to get to unpopular opinions.
[1724.12 → 1734.50] And I should say that this segment idea, shamelessly stolen by our rival gang over at Go Time, they actually do unpopular opinions each and every episode.
[1735.14 → 1736.80] And I thought, hey, we could do that.
[1737.10 → 1738.22] We can do that, but better.
[1738.44 → 1743.10] We can do that, but more unpopular, more interesting, fiery or even.
[1743.10 → 1746.80] They do it so often they've written a theme song for the segment.
[1747.30 → 1750.34] And while I was stealing ideas, I was like, well, let's just steal a theme song.
[1750.68 → 1751.14] Why don't we?
[1769.66 → 1770.18] Amazing.
[1770.50 → 1771.82] That's jazzier than our intro.
[1772.18 → 1772.86] Pretty good, right?
[1773.10 → 1777.84] So Divya, please hit us up with an unpopular opinion.
[1778.62 → 1778.92] Okay.
[1779.18 → 1784.04] So I managed to distill my unpopular opinion into one sentence.
[1784.04 → 1784.80] Thanks to Jared.
[1785.42 → 1794.06] And that is, in my opinion, open source is remaining incredibly unwelcoming to folks from underrepresented minorities.
[1795.74 → 1797.02] That is my opinion.
[1798.00 → 1798.22] Yes.
[1798.32 → 1798.92] Please expand.
[1800.18 → 1800.74] Hey.
[1800.74 → 1804.92] It's like, it's pretty clear, but I will expand.
[1805.06 → 1805.22] Yes.
[1805.22 → 1808.40] Well, it's clearly stated, but maybe why do you think that?
[1808.56 → 1809.46] I can give examples.
[1809.46 → 1825.28] So I think a lot of, obviously, when I say things, it's fairly anecdotal, but you can see it across a lot of open source projects that when you see core contributors, they remain of a certain, like, gender and race and ethnicity generally.
[1825.28 → 1827.02] And you can fill in the gap there.
[1827.02 → 1837.22] But I think that is indicative of just the fact that a lot of the times open source is not as inclusive as it likes to be.
[1837.22 → 1840.48] So I'd like to preface it with that.
[1840.90 → 1843.40] I love the concept of open source.
[1843.54 → 1854.68] And I think there's an ideal of what open source is, which is this concept of meritocracy and the ability for you to showcase the work you're working on and have the community support you.
[1854.68 → 1855.92] That is the ideal.
[1856.38 → 1866.84] Unfortunately, we live in a reality where there is your success and the ability, basically your exposure is very much determined by your background.
[1867.24 → 1877.44] So if you come from a wealthy background, if you are privileged, if you don't have to worry about money, whatever that may be, that determines how much success you can get and how much work you can put into a community as well.
[1877.44 → 1886.54] And so I think that's something it's almost the elephant in the room when it comes to open source that no one really wants to talk about.
[1886.86 → 1889.44] And sure, you can even say this is true for life in general.
[1889.44 → 1890.92] So it's not like just tech.
[1891.02 → 1901.12] But the reason why I bring it up in regard to open source is because I think in tech and in open source specifically, we tend to talk about it like it is a meritocracy when that is not the case.
[1901.44 → 1906.30] And I think that's why I have this criticism, because I think we don't bring light to that.
[1906.30 → 1910.64] And what this leads to is because people don't talk about that as a problem.
[1911.18 → 1914.62] There's not a lot of focus on building the community.
[1914.80 → 1917.04] So we talk about open source being a community.
[1917.26 → 1935.98] But oftentimes when people want to put in place measures like code of conduct or contributing guidelines, there's a lot of backlash that happens because there's this strange hypocrisy that happens where people are like, open source is about the community, but the code is more important than the community, which kind of hits up against.
[1936.30 → 1948.14] They're antithetical, almost like you have to if you want a good community code is important, but the community is way more important, I would argue, because if you build people up, I think it overall leads to a better outcome.
[1948.64 → 1950.50] Right. Because more people are contributing.
[1950.72 → 1951.46] There are more voices.
[1951.64 → 1954.90] Obviously, you need like a core team of people who make decisions.
[1954.90 → 1961.90] But I think having like RFCs and a way for people to be involved and feel like their voices are heard is very important.
[1962.58 → 1968.18] And I can give you examples if you like, because I've spoken quite broadly, but I'll bring this back to JavaScript.
[1968.18 → 1970.22] And this happened in like 2015.
[1970.54 → 1978.44] And I mean, there are obviously many, again, it's anecdotal, but this is one example just to solidify this concept, which is that around 2015.
[1978.80 → 1981.02] So Ashley Williams is huge in the Node community.
[1981.02 → 1985.52] She's done so much in terms of building a community and making people feel inclusive.
[1985.52 → 1991.30] She started the Node inclusivity working group in like 2014 and 2015.
[1991.30 → 1994.52] And she got so much backlash from that.
[1994.52 → 2000.32] And there were so many people who opened issues with like, there was like this eggplant thing that people just kept sending her.
[2000.50 → 2009.64] And it was just horrible because people didn't see the value that she was bringing or what the point she was making, which is that in order for Node to succeed,
[2009.64 → 2017.58] the community needs to rally behind Node and you need to be more inclusive of the people who are in Node and contributing to Node.
[2017.82 → 2019.98] And it's really frustrating because I see this happen.
[2019.98 → 2023.84] It pops up always where it's like someone is like, hey, this is really important.
[2024.00 → 2029.02] And then it's oftentimes, unfortunately, a woman who does it where they're like community is really important.
[2029.02 → 2030.80] And then they end up having to firefight.
[2031.32 → 2036.42] I would say it's almost self-fulfilling sometimes because people are like, women don't contribute code.
[2036.42 → 2040.02] And like, the thing is, women do contribute code.
[2040.34 → 2049.12] The problem is when they do contribute code, they end up having to spend so much time communicating and like firefighting because no one else wants to do that.
[2049.26 → 2056.20] So it just ends up looking like they're not doing anything because they don't have the time to do anything but to like to fix the community.
[2056.44 → 2058.92] So they don't end up contributing the code.
[2059.00 → 2060.94] So it's self-fulfilling because they're not writing code.
[2061.02 → 2062.44] They're like kind of fixing the community.
[2062.62 → 2064.00] And it's really frustrating.
[2064.40 → 2065.70] And I do this too.
[2065.70 → 2067.60] Like I've contributed code before.
[2067.94 → 2071.68] I've gotten really frustrated and even burned because I'll contribute code.
[2071.80 → 2076.36] And then someone will like thumbs down a PR that I provide with no feedback.
[2076.88 → 2083.92] And then I would have to find a way to like to communicate without putting them on the spot because I know I'm a new contributor.
[2083.92 → 2086.12] And like there's so much work I have to do.
[2086.22 → 2092.18] And by the end of it, even though the issue gets resolved, or my PR gets submitted, I'm like, I don't really want to do that anymore.
[2092.60 → 2093.86] And that's really frustrating.
[2093.86 → 2098.66] And I think it is something that I want the community to improve.
[2098.76 → 2100.80] It's almost like I'm willing to do the work.
[2100.92 → 2106.16] But I think as a whole there needs to be buy-in for this to improve.
[2106.66 → 2106.80] Yeah.
[2107.46 → 2108.34] It's my hot take.
[2108.34 → 2112.40] So, yeah, I mean, there's a lot said there.
[2112.50 → 2114.68] I have some thoughts and some questions.
[2115.30 → 2131.44] So anecdotally as well, I guess I would encourage you to maybe persist or push through because even as a person who's in the privileged demographic, the unmentioned one, I've also had like the straight thumbs down closed, like not welcome here PR closed.
[2131.44 → 2134.98] And it's kind of like, well, this is not a community that I can be a part of.
[2135.46 → 2138.36] But open source is a very large thing.
[2138.50 → 2140.06] In fact, it's hard to define it.
[2140.38 → 2146.46] Like, so JavaScript is a large community, but then you go open source and there's like every kind of community, like group.
[2146.56 → 2148.14] People believe this, that or the other thing.
[2148.14 → 2151.98] And so there are some places where I think it's more welcoming than others.
[2152.18 → 2154.92] So like maybe as an optimist, I'd say, well, I see what you're saying.
[2155.02 → 2155.72] It's not all bad.
[2155.82 → 2156.60] Like it's not all that.
[2156.86 → 2156.94] Yeah.
[2157.04 → 2158.80] But that's a lot of it.
[2158.86 → 2159.52] I'm sure is.
[2160.10 → 2160.30] Yeah.
[2160.78 → 2161.58] That's just a thought.
[2161.86 → 2163.92] My question would be like, what would you love to see change?
[2164.00 → 2167.92] Like demonstrable steps towards a better world in this space?
[2168.70 → 2173.70] I think the first step, and I know like the moment this is mentioned, like people get really defensive.
[2174.10 → 2174.38] Yeah.
[2174.38 → 2180.40] Like just as a baseline, having a code of conduct is just like one way of just setting precedent.
[2181.22 → 2185.52] And it's not saying like, oh, you're pandering to whatever, like people's feelings or whatever.
[2185.60 → 2191.22] It's just more than setting a baseline for like, this is how we interact on this particular project.
[2191.52 → 2197.18] And then anytime people contribute to it, you're like, I have read the code of conduct and I agree to abide by this.
[2197.50 → 2201.60] That's like just a way of like, I'm agreeing to be a decent human being.
[2201.60 → 2205.04] And this is like how I want to act and how I will interact.
[2205.20 → 2216.88] And so when you set that baseline, then you have something to come back to as a sense of like, hey, you agreed to this code of conduct, and you reacted in this way that is counter to this code of conduct.
[2216.88 → 2224.96] So it becomes more of a you didn't abide by this contract that we all signed rather than I have this feeling, and you hurt my feeling.
[2225.12 → 2233.84] Because the moment you talk about feelings and people tend to question it, they're like, I think that's just you and your emotions, and you're too emotional and whatever.
[2233.84 → 2244.76] And I think this happens a lot, especially like, I hate doing the gender thing, but oftentimes women get shafted because they're like, I have these emotions and people are like, you're always emotional.
[2245.06 → 2246.82] And it's very not useful.
[2246.94 → 2247.92] It's not useful discussion.
[2248.08 → 2252.32] And so when you automatically have that baseline of this is the code of conduct, this is how we want to interact.
[2252.32 → 2263.56] It also sets its ground rules, and it also helps overall like new contributors understand that the owners and the core team of that particular project care about that.
[2263.94 → 2266.90] Because in general, a lot of projects need new contributors.
[2267.08 → 2274.46] They want people to like, one, be active in the community, use the product that the project that they are pushing and like also make it better.
[2274.46 → 2286.26] And so if that's the kind of thing, if you're trying to grow a community, you need to almost like as leadership of a project, be able to set the baseline of like, this is what we expect.
[2286.64 → 2287.66] Everyone is welcome here.
[2287.72 → 2290.80] And if you don't want to do that, like whatever, write that in your code of conduct.
[2291.04 → 2295.10] Like as a this is kind of like, we do this and this is how we act and whatever.
[2295.28 → 2298.92] So like, if I read it and I disagree with something, I can just choose not to commit to it.
[2298.92 → 2307.60] The other thing also, like if code of conducts are like too much for some people think it's a bit too much or whatever, too loose.
[2308.62 → 2312.60] There's also the other thing, which is just having a clear contributing guideline.
[2312.86 → 2317.26] Just like what is expected from a basic PR?
[2318.00 → 2323.48] Because oftentimes there are so many issues to work on and there's various people working on it with different backgrounds.
[2323.48 → 2326.62] But what's the expectation if you are to contribute?
[2327.06 → 2328.60] What does your PR have to look like?
[2328.60 → 2329.86] How does your code have to look like?
[2329.90 → 2330.64] How do you lint it?
[2330.68 → 2331.42] How do you test it?
[2331.56 → 2333.60] And even like with docs, how do you want it written?
[2333.84 → 2336.52] Do you want this particular thing covered or this or that?
[2336.88 → 2343.04] And so this gives you, just like if you don't want to talk about code of conducts, like whatever, like that's a separate issue.
[2343.58 → 2348.62] But a contributing guideline gives you a sense of, if you insist that code is very important,
[2349.00 → 2353.70] then maybe set ground rules as to what exactly the code expectation is.
[2353.70 → 2356.86] And also not just, I think it's a two-way street, right?
[2356.86 → 2360.30] Because when you do open source, we always ask people for contributions.
[2360.64 → 2365.28] But I think the people who own the project also have to be like, this is what you can expect of us.
[2365.94 → 2368.96] So if you're busy, you can say that.
[2368.96 → 2371.84] Like it'll take a couple of weeks for us to get to a PR.
[2372.08 → 2376.70] Because then as a contributor, I can be like, okay, my PR hasn't been looked at in the last week.
[2376.70 → 2379.58] But the timeline was two to three weeks.
[2379.58 → 2380.88] So it's fine.
[2381.34 → 2387.20] But if I don't even know what that is, I might ping them in like Discord or whatever channel they may use.
[2387.30 → 2389.70] And then they might get frustrated because they're like, we're busy.
[2389.96 → 2391.42] We have family things.
[2391.42 → 2392.76] And like we're all in lockdown.
[2392.76 → 2394.46] And we're whatever, whatever that may be.
[2394.56 → 2395.42] And so it's really hot.
[2395.48 → 2397.32] There's like this lack of communication that happens.
[2397.32 → 2405.12] And so off the bat, if you have like a good set of contributing guidelines, you set precedent and expectations between both parties.
[2405.38 → 2408.22] So you know what to expect automatically off the bat.
[2408.74 → 2408.80] Yeah.
[2408.90 → 2409.02] Yeah.
[2409.02 → 2412.16] And that's, it seems like common sense that everyone should want that.
[2412.26 → 2413.50] Some kind of guidelines to follow.
[2413.66 → 2413.82] Yeah.
[2414.18 → 2417.38] And that's definitely something that anyone can champion.
[2417.48 → 2421.50] You don't have to be from an underrepresented group to push for that on projects that you love.
[2421.74 → 2423.56] It seems so basic, like house rules.
[2423.56 → 2427.78] Like everybody has the right or whatever to like to make the rules of their own house.
[2428.02 → 2429.36] You know, maybe you come to my house.
[2429.58 → 2432.08] You got to take your shoes off when you enter the house.
[2432.26 → 2433.20] Maybe that's my rule.
[2433.46 → 2435.44] But if you go to Nick's house, maybe he doesn't care so much.
[2435.48 → 2436.08] Hey, where are your shoes?
[2436.12 → 2437.94] I want it to be a more relaxed place.
[2438.56 → 2442.16] Well, in social places, like we have to navigate those rules.
[2442.16 → 2445.22] Like we have to somehow say like, this is okay here.
[2445.28 → 2446.30] That's not okay here.
[2446.42 → 2447.60] We eat at 630.
[2447.66 → 2449.60] We eat at 9 p.m.
[2449.96 → 2450.94] This kind of things.
[2450.94 → 2455.62] And I think it just sets expectations and ground rules of like, this is the kind of
[2455.62 → 2456.38] community this is.
[2456.46 → 2457.96] You can still define it how you want to.
[2458.32 → 2460.42] You can still be closed off and like, I'm in charge.
[2460.52 → 2463.76] But just like put that on the read me, put that on the code of conduct so that people
[2463.76 → 2465.64] walk up, and we don't waste our time.
[2465.74 → 2468.34] Like, oh, this is a person who doesn't want any contributors.
[2469.22 → 2470.38] I'm going to go somewhere else.
[2470.54 → 2473.76] You know, so I think setting expectations, I think, is a huge part of it.
[2473.82 → 2478.18] And I think not enough people are doing it, which is why I'm, maybe this is an
[2478.18 → 2478.60] popular opinion.
[2478.66 → 2483.06] I'm not a huge fan of just copying and pasting other people's codes of conduct because it
[2483.06 → 2486.36] seems like it's checking the box, which I think it should be there.
[2487.26 → 2488.44] And I'm guilty as well.
[2488.50 → 2489.96] I've definitely copied and pasted a code of conduct.
[2490.04 → 2490.86] I read it at least.
[2491.42 → 2495.04] But it seems like, well, did I put any thought into this?
[2495.08 → 2497.70] Am I just calculating because I know I should have one?
[2497.82 → 2499.08] I think there's a lot of that going on too.
[2499.48 → 2500.72] Sorry, Chris, you were going to say something.
[2500.72 → 2501.16] Right.
[2502.58 → 2510.32] I know there are people listening to this program like me or like Jared or like Nick.
[2510.66 → 2516.08] Personally, some years ago, I was like, why do I need a code of conduct?
[2516.26 → 2517.28] I don't want this thing.
[2517.88 → 2519.88] Like, can't people just be nice?
[2520.52 → 2522.68] Like, I didn't understand.
[2523.24 → 2523.44] Right.
[2523.80 → 2525.18] I didn't think it was helpful.
[2525.40 → 2525.86] I didn't want.
[2526.28 → 2527.52] So what happened?
[2527.52 → 2537.14] So what I did is, number one, I kept that to myself because starting fights with other
[2537.14 → 2538.42] people is not going to be productive.
[2538.86 → 2548.74] But what I did was I listened to the people I disagreed with, and I got to know them and
[2548.74 → 2549.96] I befriended them.
[2550.56 → 2557.02] And over time, I began to have more empathy and I began to understand what is important
[2557.02 → 2557.74] about it.
[2558.20 → 2564.74] Even though, like, the first time that I heard about a code of conduct, I reflexively
[2564.74 → 2566.36] said, well, no, we don't need that.
[2566.60 → 2567.40] I don't want that.
[2567.98 → 2575.44] And the very same arguments that were made to me then are the very same, like, arguments
[2575.44 → 2579.42] and reasons for doing so that people are repeating today.
[2579.42 → 2586.04] But it's just that back then I didn't understand, and I didn't have empathy for the people that
[2586.04 → 2586.56] it affects.
[2587.34 → 2592.88] And so, you know, by listening and by getting to know people and being part of a community
[2592.88 → 2599.10] and that's how, like, I came to understand that, you know, this is really something that
[2599.10 → 2599.72] is necessary.
[2599.88 → 2605.62] This is something that's going to help this project's community or, you know, the greater
[2605.62 → 2607.98] JavaScript community or the greater open source community.
[2608.38 → 2612.46] And, you know, just listening to different viewpoints and people I disagreed with.
[2612.68 → 2614.52] And that's, yeah.
[2614.80 → 2620.54] So maybe if somebody is looking for, well, thinking, I don't understand why we need this
[2620.54 → 2620.76] thing.
[2620.80 → 2621.68] And no, I don't want it.
[2621.76 → 2625.94] Well, I would suggest to you to listen to the people that you disagree with.
[2626.60 → 2627.30] Good advice.
[2627.86 → 2628.18] All right.
[2628.18 → 2630.48] Let's switch gears, but not switch popularity.
[2630.48 → 2635.66] This is also, I think, probably unpopular because I've disagreed with it myself in the
[2635.66 → 2638.68] past and I may disagree with it by the time we're done talking here.
[2638.76 → 2646.86] But I do believe it right now, which is that I think most of the time that you spend tweaking,
[2647.90 → 2654.50] customizing, optimizing your terminal, your editor.
[2654.50 → 2655.30] Oh, no.
[2656.52 → 2657.64] Your tools.
[2659.44 → 2661.56] Most of that is time not well spent.
[2664.48 → 2667.96] How can you do this?
[2668.42 → 2670.22] I think most of that stuff is YAGNI.
[2670.40 → 2673.22] I think we spend six hours to save 60 seconds.
[2673.88 → 2676.98] And I think we yak shave far too much.
[2678.02 → 2680.90] You never know if you're going to do that 60 seconds again sometime.
[2680.90 → 2687.52] I think I've hit on a popular chord here because everyone just kind of sat there and laughed
[2687.52 → 2688.34] and shocked.
[2688.70 → 2689.50] What do you guys think?
[2689.50 → 2690.08] I agree with you.
[2690.20 → 2690.80] I agree with you.
[2690.90 → 2696.74] I feel like it's going to be faster to learn what you have in front of you than to spend
[2696.74 → 2698.32] time tweaking it.
[2698.60 → 2702.76] It is going to be faster to learn how to use these tools instead of making your own.
[2703.40 → 2703.76] Right.
[2704.56 → 2708.44] And like, I'm fine with a little bit of like ergonomics, you know, like I'd rather do it
[2708.44 → 2709.62] this way, rather do it that way.
[2709.62 → 2711.34] And that's not what I'm talking about.
[2711.46 → 2717.16] I'm talking about like the extreme customization that I myself has passed me very guilty of.
[2717.30 → 2719.24] I used to be like, pimp my ride.
[2719.74 → 2720.74] My ride is a terminal.
[2721.46 → 2725.00] And I know there's a lot of out there because I see a lot with screenshots and people sharing.
[2725.08 → 2727.38] And I think Nick is probably like, he's smiling real big over there.
[2727.48 → 2728.82] I know he likes to do this.
[2729.30 → 2732.78] I will say like, if this gives you joy and this is something you enjoy, like what?
[2732.90 → 2735.32] Go do it because it's not a waste of time if it's like a joy thing.
[2735.68 → 2737.44] But you think this is a productivity thing.
[2737.44 → 2739.60] I think you're probably fooling yourself most of the time.
[2739.78 → 2741.44] We're not going to need that level of customization.
[2742.56 → 2746.22] In fact, we may slow down our terminals so bad that we can't, you know, we have to switch
[2746.22 → 2751.42] tools because it takes my Vim RC got too thick and I Vim slowed down to the point that I don't
[2751.42 → 2752.46] use Vim very much anymore.
[2752.46 → 2755.34] It's just like, why did I do that to myself?
[2755.46 → 2758.60] But a very thin customization, a few keyboard shortcuts.
[2759.04 → 2764.14] I can be very productive in Vim in many different scenarios and servers and stuff that I never
[2764.14 → 2765.12] need all that other stuff.
[2765.56 → 2769.06] And so I'd rather just, like Chris said, kind of learn the tools that are in front of me
[2769.06 → 2771.20] and don't customize the heck out of it.
[2771.20 → 2772.04] Oh, man.
[2772.40 → 2778.98] I will agree with you that doing it for productivity is probably not beneficial.
[2779.64 → 2785.28] Although I will say, I don't know, I feel way more productive in my environment that I moulded
[2785.28 → 2788.56] to me rather than me trying to mould myself to some environment.
[2789.12 → 2794.60] And some background, the last three months I have spent working entirely on a Windows machine
[2794.60 → 2801.10] in the cloud running Visual Studio Code that's several versions behind and doing all of that
[2801.10 → 2806.06] with just a slight enough key lag, like on everything that I type because it's a machine
[2806.06 → 2808.96] in the cloud that I'm driving myself insane.
[2809.10 → 2810.12] Are you a glutton for punishment?
[2810.26 → 2811.00] Why are you doing this?
[2811.24 → 2812.12] I have no choice.
[2812.98 → 2813.22] Okay.
[2813.22 → 2821.62] And my bespoke environment with 51 Vim plugins and 15 COC plugins, which is a language server
[2821.62 → 2826.04] for Vim, bringing a total of what, 66 plugins.
[2826.74 → 2828.04] My Vim is fast.
[2828.48 → 2828.96] It's great.
[2830.66 → 2833.06] I'm sure I got one plugin that's just killing my Vim.
[2833.14 → 2834.34] I just don't know which one it is.
[2834.38 → 2834.60] Probably.
[2835.00 → 2835.60] I don't care.
[2835.86 → 2837.40] I'd rather use VS Code most of the time.
[2838.22 → 2838.46] Yeah.
[2838.68 → 2843.30] I can't defend the productivity part of it because while I have shaved off several minutes doing
[2843.30 → 2849.24] things over the last 10 years of using Vim, it's been, you know, 950 commits to my
[2849.24 → 2852.82] .files and lots of time debugging them.
[2853.02 → 2857.94] And I'm completely useless when I go to another editor like VS Code.
[2858.60 → 2864.22] And I can't justify the productivity cost of that, but I need it to fit me.
[2864.36 → 2865.48] I'm not going to fit it.
[2867.42 → 2868.84] I feel like this has been a good one.
[2868.94 → 2870.26] I've turned this into a confessional.
[2870.40 → 2871.24] Night's confessing.
[2871.24 → 2875.30] In the chat room, Rebecca brings up a good point.
[2875.60 → 2879.66] She says she stopped doing the extreme customization because it made it so much harder to help
[2879.66 → 2882.54] other people because their setup was so different.
[2883.40 → 2889.08] Just like Nick said, if I have to switch over to VS Code or whatever, I, you know, I'm stuck.
[2889.08 → 2895.70] I actually wrote a custom script once that, that would let someone, like I would, it would
[2895.70 → 2900.40] grab their, I would type the script out, put their username in, and it would go to GitHub,
[2900.80 → 2906.34] pull down their public key, add it to my authorized keys on my machine and set it up so that they
[2906.34 → 2910.70] could SSH in pass wordlessly into my machine directly into the Tmux session I was in.
[2910.82 → 2912.86] And then we could work together in there.
[2912.86 → 2920.24] And I tried it exactly once, and it was just completely useless because whoever is Ashing
[2920.24 → 2923.96] in and trying to work with me has no idea about any of the key bindings that I have.
[2924.32 → 2924.38] Right.
[2924.70 → 2926.24] So it just, it wasn't practical.
[2926.46 → 2931.20] Whereas something like Visual Studio Code's live share feature is amazing.
[2931.98 → 2932.14] Yeah.
[2932.64 → 2934.32] I agree with the customization thing.
[2934.38 → 2935.46] I used to do the same.
[2936.00 → 2940.94] It's interesting because I did it when I was like a very like newer programmer, just because
[2940.94 → 2947.42] I felt like that was being a lead programmer was just like doing these crazy customizations.
[2947.74 → 2955.48] And I think at the time I was using like Sublime and I felt I had this wrong opinion,
[2955.68 → 2961.78] obviously, that anyone using Sublime wasn't as lead and cool and like hacker-like as someone
[2961.78 → 2962.48] who used Vim.
[2962.48 → 2967.58] I think at the time the agency I worked at people were also using Emacs because it was cool.
[2967.58 → 2973.68] And it was just this set, this like complete sense of like you have to customize to the
[2973.68 → 2979.82] point of just like nobody knowing any of your bindings or what you're doing just to prove
[2979.82 → 2980.48] a point.
[2980.84 → 2983.82] So you would do a demo and everyone would be like, what is that?
[2983.86 → 2989.18] And it just feels like I've since learned that that is not, it's not indicative.
[2989.38 → 2993.28] Like how many customizations you have is not indicative of like how good you are as a
[2993.28 → 2994.92] programmer at all.
[2994.92 → 2999.36] Like I have seen phenomenal programmers program with Sublime code.
[2999.48 → 3004.20] Even today with VS Code, like they still use Sublime, and they're like leagues ahead.
[3004.66 → 3006.10] Coming down to it, it doesn't matter.
[3006.34 → 3010.68] Like if you find a tool that works for you, and you don't need to customize a lot, like
[3010.68 → 3012.50] it's just whatever gives you productivity.
[3012.74 → 3015.02] And I think sometimes customization can get in the way of that.
[3016.04 → 3018.44] And so, yeah, whatever works.
[3018.44 → 3020.88] Like if you enjoy customization and that brings you joy, sure.
[3020.88 → 3025.40] But I think I agree with Jared that like if you convince yourself, it gives you productivity.
[3025.88 → 3033.92] I actually know people who have convinced themselves that writing like even three letters in their
[3033.92 → 3037.20] terminal is too much that they have to write one.
[3037.50 → 3038.68] And I'm just like, it doesn't matter.
[3039.04 → 3039.52] It doesn't.
[3039.68 → 3044.16] And I almost feel judged when I'm like, I actually don't mind writing the entire thing.
[3044.16 → 3046.66] I have alias got to G.
[3047.40 → 3047.60] Yeah.
[3047.64 → 3048.38] I mean, yeah.
[3049.06 → 3050.68] I guess you're an example.
[3051.32 → 3056.20] I mean, I feel like the so that everybody has to pick where that point is for them.
[3056.20 → 3060.26] And I think that what my, my opinion is, is that we far easily go into like the extreme
[3060.26 → 3062.02] yak shave side of it.
[3062.22 → 3064.72] But I'm not against learning your tools.
[3064.72 → 3066.90] I'm not against solving pain points.
[3066.90 → 3071.88] Like if I'm feeling pain, there's an argument that says, okay, most of my time spent thinking,
[3072.04 → 3077.52] but when it comes time to actually type, whatever gets between me and my idea into the system
[3077.52 → 3079.64] is like a problem that I want to solve.
[3079.74 → 3080.78] I understand that completely.
[3081.32 → 3083.74] But for me, I'm like, I wait till I'm feeling pain.
[3083.84 → 3086.48] I mean, feeling like, gosh, this is the 17th time I've done this.
[3086.68 → 3087.74] There has to be a better way.
[3087.78 → 3088.06] Right.
[3088.42 → 3091.16] Or you see somebody else do something that you routinely do slowly.
[3091.24 → 3092.22] They do it really fast.
[3092.70 → 3093.50] Go learn that thing.
[3093.50 → 3097.44] But there's a law of diminishing returns and there's ROI on your time.
[3097.98 → 3104.04] And I think we often throw that out in pursuit of the extreme productivity and not say, is
[3104.04 → 3105.38] this worth my time right now?
[3105.62 → 3108.10] Or, I mean, like Emmett's a great example, by the way.
[3108.18 → 3112.38] I think this is an unpopular opinion because we've lit up the chat room with all sorts of
[3112.38 → 3112.94] statements.
[3113.72 → 3119.62] And Roos by is talking about using Emmett, which is the, you know, text expansion tool where
[3119.62 → 3123.02] you can type H and a carrot and L3 or whatever.
[3123.18 → 3125.88] And it'll expand a bunch of HTML for you.
[3126.48 → 3130.06] Like, that's an easy thing to learn and a huge win over time.
[3130.18 → 3133.08] So, like, that's not problematic in my opinion.
[3133.66 → 3139.48] It's like writing in your own stuff and the like, it's just picking where that pain point
[3139.48 → 3140.82] is and solving it fine.
[3141.00 → 3145.58] But extreme, like, pimp my ride style customization, which I've done tons of.
[3145.58 → 3149.36] I think it's kind of a young person's game that's maybe an old person talking because
[3149.36 → 3151.12] I used to think it was worth it.
[3151.22 → 3152.86] And now I'm like, ain't nobody got time for that.
[3153.28 → 3155.10] So maybe that's ageist or something.
[3155.20 → 3157.96] But I feel like it's kind of a person.
[3158.06 → 3159.24] I shouldn't say a young person's game.
[3159.56 → 3164.04] It's something that I think people who have the time and enjoy it do more of it because
[3164.04 → 3165.02] it is incredibly enjoyable.
[3165.38 → 3166.70] I'm not trying to take that away from everybody.
[3166.88 → 3170.38] But yeah, you got to feel the pain before you fix the pain.
[3170.50 → 3174.86] And you have to also judge how much work is it going to be for me to fix this pain or should
[3174.86 → 3175.58] I just live with it.
[3175.84 → 3177.44] I think oftentimes live with it's the right answer.
[3177.96 → 3178.88] Yeah, most of the time.
[3179.14 → 3183.78] But the 55th time that you come across the man, I could just write a macro to do this
[3183.78 → 3184.90] if I only knew macros.
[3185.08 → 3186.14] Like, I know that they're a thing.
[3186.66 → 3189.38] But in whatever, whatever editor you're using.
[3189.54 → 3189.68] Yeah.
[3190.16 → 3194.36] Eventually, like, you have to take a little bit of time to, to sharpen your axe.
[3195.08 → 3195.62] I'm with you.
[3195.66 → 3197.50] I've been writing Apple scripts for the last few days.
[3197.50 → 3199.82] So I'll share that in our shout-outs, why that is.
[3200.12 → 3201.20] There's a time and a place.
[3201.38 → 3203.24] I just think we misjudge it oftentimes.
[3204.86 → 3215.70] This episode is brought to you by DigitalOcean.
[3216.04 → 3220.48] DigitalOcean's developer cloud makes it simple to launch in the cloud and scale up as you
[3220.48 → 3220.78] grow.
[3220.78 → 3225.96] They have an intuitive control panel, predictable pricing, team accounts, worldwide availability
[3225.96 → 3232.46] with a 99.99 uptime SLA and 24-7, 365 world-class support to back that up.
[3232.46 → 3238.18] DigitalOcean makes it easy to deploy, scale, store, secure, and monitor your cloud environments.
[3238.56 → 3242.00] Head to do.co slash changelog to get started with a $100 credit.
[3242.38 → 3244.48] Again, do.co slash changelog.
[3244.48 → 3251.78] All right.
[3251.82 → 3255.84] We are back for one of my favourite segments because it's a chance for us to say thanks
[3255.84 → 3258.20] to folks or to point to cool things.
[3258.40 → 3263.54] Really give shout-outs to people and projects or whatever it happens to be that we think
[3263.54 → 3265.64] deserves a shout-out.
[3266.26 → 3268.30] So let's get right to it.
[3268.38 → 3269.80] Divya, you are up, my friend.
[3269.80 → 3270.40] Awesome.
[3270.70 → 3276.50] This is less code related, but I just noticed that today that Keynote has new templates,
[3276.76 → 3277.68] which are really cool.
[3277.82 → 3283.10] Not that I use a lot of their templates because I generally use a blank one, but they have
[3283.10 → 3285.08] a colour gradient one, which is really cool.
[3285.34 → 3287.28] So it automatically colour gradients things.
[3287.72 → 3288.86] Also, their templates look nicer.
[3289.20 → 3289.66] I don't know.
[3289.78 → 3293.96] Like they added new ones and just like the template layout itself is really nice.
[3293.96 → 3298.56] I use Keynote for a lot of my presentations and for like any slide decks I need to create
[3298.56 → 3299.44] for work or whatever.
[3299.76 → 3300.66] So that's cool.
[3300.90 → 3302.88] I just noticed that, and I thought that was really cool.
[3303.28 → 3307.88] So not that, I mean, I have other issues with Keynote, but that's a shout-out.
[3308.02 → 3312.00] Like its worthy shout out since I complain about Keynote a lot.
[3312.16 → 3313.50] I can't believe you're shouting out Keynote.
[3313.60 → 3315.18] Did you read my one?
[3315.82 → 3316.66] Wait, what was yours?
[3316.76 → 3317.30] Scroll down.
[3319.32 → 3320.48] Okay, Nick, you're up.
[3320.82 → 3321.26] It's different.
[3321.40 → 3322.24] You said yours is different.
[3322.80 → 3323.50] No, it totally is.
[3323.96 → 3324.50] It's just funny.
[3324.70 → 3325.04] Go ahead, Nick.
[3325.38 → 3326.78] I would also like to shout out Keynote.
[3326.88 → 3327.38] No, I'm kidding.
[3329.44 → 3335.34] So this one I'm a little bit biased on, but I really want to shout out to the Dojo team
[3335.34 → 3340.16] for the release of Dojo 7, which will be out by the time this episode actually airs.
[3340.20 → 3343.58] It's not out yet, but we're actively working on getting that out right now.
[3344.06 → 3349.54] And so I want to shout out the team, Matt Gad, Ant Ruler, and Tom Dye, and all the others
[3349.54 → 3351.54] who contributed to the project.
[3351.54 → 3354.08] This one really focuses on our widget library.
[3354.62 → 3358.76] I've written a number of widgets and converted a number of widgets to use the more modern
[3358.76 → 3359.06] Dojo.
[3359.56 → 3362.20] So it's really cool, really awesome.
[3362.28 → 3368.22] It has a whole new theming section, including a custom Dojo theme and also a material theme
[3368.22 → 3368.96] that ships with it.
[3369.78 → 3371.68] And yeah, it's really great.
[3371.82 → 3373.92] If you like React, I think you'll like Dojo better.
[3374.12 → 3375.48] So you should give it a shot.
[3375.48 → 3377.66] You should have any unpopular opinions.
[3377.74 → 3378.54] That would have been a great one.
[3379.26 → 3381.32] If you like React, you'll like Dojo better.
[3381.86 → 3383.80] All right, Chris, you're up.
[3384.26 → 3386.72] I want to shout out to Was Todd.
[3386.86 → 3388.50] So Was works at Netflix.
[3388.76 → 3390.86] He's a maintainer of Express.
[3391.48 → 3396.44] And he's been doing perfect work in the Express community.
[3396.56 → 3399.64] He's been working with the package maintenance group in Node.
[3399.64 → 3404.38] And he's been working with the Node tooling group and probably other stuff.
[3404.50 → 3406.50] But he's doing a lot right now.
[3406.68 → 3409.00] And I really appreciate what he's doing.
[3409.36 → 3410.32] So thanks, Was.
[3411.30 → 3412.38] Shout out to Was.
[3412.48 → 3414.76] Well, it's time to shout out Keynote once again.
[3415.26 → 3418.20] This time from a slightly different angle.
[3418.28 → 3422.24] I did not know about the new gradient background themes.
[3422.36 → 3423.68] So is that just you update Keynote?
[3423.76 → 3425.16] It just has new themes that weren't there before?
[3425.48 → 3426.62] Yeah, pretty much.
[3427.44 → 3427.98] Super cool.
[3427.98 → 3434.86] I like to shout out Keynote because I think it's underrated as a general purpose creation tool.
[3435.24 → 3440.56] I've been able to wield it in a way that I didn't realize it could be wielded before recently.
[3440.74 → 3450.10] And it's actually how we create all of our audio grams that come out of our shows that turn into videos that get posted onto Twitter and YouTube and what have you.
[3450.44 → 3456.62] It's been an incredibly valuable tool for that where other tools have failed in massive ways.
[3456.62 → 3461.82] And I'm going to end up writing this up and sharing with folks so they can also benefit from this workflow.
[3461.92 → 3465.60] But basically, we're using Keynote not to create presentations, but to create videos.
[3466.56 → 3469.62] And it's super smooth, super easy to work with.
[3469.72 → 3475.52] It's just like a general purpose canvas where you can drag objects around, and you can do amazing things.
[3475.62 → 3477.92] People generally use it for slide decks.
[3477.92 → 3480.92] I remember back when I was helping Groove Shark rebuild.
[3481.76 → 3490.10] That was an old music streaming service that was super cool back in the day before the RIAA and other entities took them down.
[3490.44 → 3496.10] One of their designers, I think their lead designer, actually built their entire UI.
[3496.54 → 3498.22] He did all his design work in Keynote.
[3498.22 → 3500.54] And I remember having my mind blown.
[3500.92 → 3507.02] And he loved it because it's basically like a free-form canvas for drawing shapes and dragging them around.
[3507.22 → 3508.74] And duplicating is really easy.
[3509.00 → 3510.54] And gridding is really easy.
[3510.66 → 3514.40] And it was just ergonomically something that he liked to do.
[3514.48 → 3515.90] He just preferred it to all the tools then.
[3515.98 → 3518.34] Now I know there's better tooling now than there was back then.
[3518.80 → 3521.56] This is probably the 2009 time frame.
[3521.56 → 3533.78] But if you haven't used Keynote for anything besides presentations, and you have some design needs or some video needs, there's a cool way you can use it to record it as a video.
[3534.06 → 3535.62] You can add soundtracks.
[3537.06 → 3539.00] It is a really cool tool.
[3539.06 → 3543.16] It's almost like Excel insofar as you can just kind of use it to make stuff.
[3543.46 → 3548.78] I think Excel is one of the most amazing pieces of software in human history for what it's unlocked for folks.
[3548.78 → 3554.80] I think Keynote is along those lines if more people knew that they could wield it in different ways.
[3555.10 → 3557.80] So shout out to Keynote for the second time.
[3558.78 → 3562.02] Grab a gradient background theme and use it for something it's not designed for.
[3562.16 → 3564.50] It's a pretty awesome piece of software.
[3565.10 → 3565.18] Yeah.
[3565.40 → 3570.04] Jared, do you have any examples of using Keynote for videos?
[3570.30 → 3571.78] Like a video that you've made with it?
[3572.14 → 3572.72] Yeah, absolutely.
[3572.86 → 3573.84] I can link one up in the show notes.
[3573.90 → 3576.82] If you follow on JSPartyFM on Twitter, you've seen some of those videos.
[3576.82 → 3587.40] All the videos that we do where we take the audio clips from the show, and we have the text and the people's, you know, like who's talking, face lights up.
[3587.60 → 3592.44] And it's basically like quotes out of our podcasts are all created in Keynote.
[3593.08 → 3594.70] I've never watched any of those.
[3594.92 → 3595.80] Come on, Chris.
[3596.26 → 3597.40] You've probably been in them.
[3597.72 → 3599.12] You've never retweeted them?
[3599.42 → 3600.16] Come on, man.
[3600.56 → 3601.30] Give us a retweet.
[3601.30 → 3604.70] I mechanically retweet everything that I see.
[3605.06 → 3605.88] You are your own bot.
[3606.42 → 3607.88] You are your own bot.
[3608.12 → 3610.90] So I'll link one of those up so that people can see what we're talking about.
[3611.38 → 3614.98] I love Keynote and I use it as much as I can.
[3615.26 → 3619.96] The only thing I wish was easier, and this is going back to slides, I guess, like using it for actual slides.
[3620.40 → 3623.72] So I just wish adding syntax highlighted code was easier.
[3623.74 → 3624.32] Oh, yes.
[3624.76 → 3625.70] Oh, my gosh.
[3625.96 → 3627.14] It's so annoying.
[3627.62 → 3629.08] You just take a picture and slide it in there.
[3629.16 → 3629.42] Perfect.
[3629.42 → 3634.34] I usually just copy from VS Code because it copies the syntax highlighting.
[3635.00 → 3635.34] Really?
[3635.62 → 3635.86] Yeah.
[3636.26 → 3642.78] So I copy it, and then I PB paste and pipe that to pigments, and then PB copy that.
[3643.98 → 3644.72] Oh, no.
[3644.84 → 3648.28] If you just copy straight from VS Code, it copies all the syntax highlighting.
[3648.34 → 3649.44] But then I'd have to open VS Code.
[3649.96 → 3650.48] That's fair.
[3651.28 → 3657.48] Can you do it remoted into a Windows machine and SSH through his authorized keys on somebody else's machine?
[3657.48 → 3660.50] If not, Nick doesn't want to have anything to do with that.
[3661.10 → 3668.36] I think you can also use, like, if you copy code in Code Sandbox, because sometimes I'm not, like, I want to do something really quick, and I'm doing a demo.
[3668.76 → 3673.40] If you copy from Code Sandbox, it also does the same syntax highlighting.
[3673.84 → 3674.68] So you don't have to open.
[3674.98 → 3678.10] You can just, like, open a tab of Code Sandbox, and it works.
[3678.10 → 3678.54] Awesome.
[3679.84 → 3681.84] Well, that's our show for this week.
[3682.36 → 3684.44] If you're listening live, we appreciate you.
[3684.52 → 3688.52] If you're listening in the produced version, I guess we appreciate you as well, but just slightly less.
[3688.60 → 3689.10] No, I'm just kidding.
[3689.54 → 3690.60] We love all of our listeners.
[3691.12 → 3694.08] We do appreciate shoutouts for JS Party.
[3694.16 → 3698.90] If you have friends in the JavaScript space, and they don't know about the show, tell everybody.
[3699.06 → 3699.56] Tell them all.
[3700.00 → 3700.86] JS Party is a thing.
[3701.34 → 3705.16] We record live each and every Thursday at 1 p.m. Eastern.
[3705.16 → 3706.88] We would love for you to participate.
[3707.02 → 3710.76] For those listening live and in the chat, we appreciate all the chatter.
[3711.36 → 3712.52] And that's it.
[3712.64 → 3713.54] We'll talk to you next time.
[3716.20 → 3719.78] We have some exciting JS Danger news for you.
[3720.14 → 3726.96] Our next recording of everyone's favourite Don't Call It Jeopardy game show is happening at Half Stack Online on May 22nd.
[3727.34 → 3728.08] What's Half Stack?
[3728.18 → 3732.86] It's a creative JS and web celebration slash COVID-19 charity fundraiser.
[3732.86 → 3734.60] They've got speakers from around the world.
[3734.72 → 3738.06] And yes, we're playing JS Danger with video over the lunch hour.
[3738.56 → 3740.02] Once again, that's May 22nd.
[3740.06 → 3741.52] Tickets are 19 bucks cheap.
[3741.72 → 3744.34] Get them at halfstackconf.com slash online.
[3744.52 → 3746.90] And I'll put a link in the show notes for easy click ins.
[3746.96 → 3747.66] Hope to see you there.
[3748.14 → 3749.14] That's all for now.
[3749.78 → 3750.56] Dino next week.
[3750.56 → 3777.42] Are we going to start with on popular opinions first?
[3777.42 → 3780.78] I thought we were going to start on a happy note.
[3781.10 → 3781.30] Okay.
[3781.44 → 3782.64] Like, woke from home.
[3783.12 → 3783.24] Yay.
[3783.24 → 3788.20] We'll also say that this specific example of a one-liner only has 35 lines of tests.
[3788.62 → 3790.70] And five of them are comments.
[3791.32 → 3792.74] And one of them is a console log.
[3792.88 → 3794.16] How many actual tests are there?
[3794.34 → 3797.24] Like, if you ran it, how many passing dots would you get?
[3798.02 → 3798.46] 14.
[3798.86 → 3799.26] 14?
[3799.64 → 3799.96] 16.
[3800.48 → 3800.88] 16.
[3801.24 → 3801.64] 16.
[3801.64 → 3805.00] Multiply that by the size of the build matrix.
[3805.74 → 3807.02] So where is it tested?
[3807.40 → 3809.80] What versions of Node is it tested in?
[3809.90 → 3810.48] Which browsers?
[3810.74 → 3810.92] Etc.
[3811.58 → 3813.20] Stop trying to make this make sense.
[3814.80 → 3816.22] No, I agree with you.
[3816.30 → 3818.24] There are a lot of benefits to that, for sure.
[3819.04 → 3823.64] I added an unpopular opinion, but I don't feel like defending myself.
[3826.02 → 3827.02] That's not how this works.
[3827.04 → 3827.84] That is unpopular.
[3827.84 → 3832.64] Yeah, if you all want to look at that, and if you all decide you're going to challenge
[3832.64 → 3835.32] me about it, I'm going to skip it, because I don't want to defend myself.
[3848.58 → 3852.98] I don't know.
[3852.98 → 3855.08] I don't know.
[3855.08 → 3855.74] I don't know.
[3855.78 → 3857.80] I don't know.
