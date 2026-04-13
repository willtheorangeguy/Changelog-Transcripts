[0.56 → 4.86] What's up, welcome back, I'm Adam Stachowiak and you are listening to The Change Log.
[5.12 → 10.28] On this show, Jared and I talk with the hackers, leaders, and innovators from all areas of the software world.
[10.58 → 13.18] We face our imposter syndrome, so you don't have to.
[13.52 → 17.16] Today on The Change Log, Jared is joined by a special co-host, Nick Needed from JS Party.
[17.46 → 21.00] For a follow-up on our Vim episode, talking to TJ Decries about Neovim.
[21.92 → 25.82] TJ is a core maintainer of Neovim, and he tells us why it was created in the first place,
[25.82 → 29.96] how it differs from Vim, why Lua is awesome for configuration and plugins,
[30.38 → 33.58] what LSPs are all about, the cool tech inside Tree Sitter,
[33.88 → 37.72] and how he's writing his own fuzzy file finder for Neovim called Telescope.
[38.04 → 41.44] Of course, big thanks to our partners Linde, Vastly, and Launch Darkly.
[41.74 → 43.96] We love Linde, they keep it fast and simple.
[44.22 → 47.00] Get $100 in credit at linode.com slash changelog.
[47.24 → 50.96] Our bandwidth is provided by Vastly. Learn more at fastly.com.
[50.96 → 55.12] And get your feature flags, powered by Launch Darkly. Get a demo at launchdarkly.com.
[55.82 → 61.18] This episode is brought to you by Gitpod.
[61.28 → 65.48] Gitpod lets you spin up fresh, ephemeral, automated dev environments in the cloud in seconds.
[66.00 → 68.42] And I'm here with Johannes Landgrave, co-founder of Gitpod.
[68.78 → 71.42] Johannes, GitHub made a big announcement recently with Code spaces,
[71.76 → 76.36] validating that it is now time for dev teams to consider what automated dev environments can do for them.
[76.52 → 77.30] What do you have to say to that?
[77.50 → 80.28] I'd say, welcome to the party, GitHub and Microsoft.
[80.28 → 87.64] No, honestly, we were very excited because it validated to the developer community what we have been pioneering over the last years.
[87.80 → 90.96] That developer environments need to be automated and ephemeral.
[91.24 → 96.04] We are now at the right place and the right time to move software development to the cloud for everybody.
[96.30 → 102.34] Not just for developers working for the Googles, Facebook's, or Shopify's who left local development already for several years.
[102.72 → 109.00] Gitpod is open source and provisions for every development team on GitHub, GitLab, and Bitbucket cloud-powered dev environments.
[109.00 → 116.48] You can access your developer environments via upstream VS Code, running on your desktop or in the browser, and soon also all JetBrains IDs.
[117.00 → 120.86] Very cool. If this gets you excited, learn more and get started for free at gitpod.io.
[121.16 → 127.94] Gitpod is free for individual developers for 50 hours a month, can be self-hosted, and is available for every developer today.
[128.30 → 129.58] Again, gitpod.io.
[139.00 → 155.04] We are back for a follow-up episode to episode 450 on VIM.
[155.04 → 161.04] First, I want to say that I appreciate all the positive feedback around our VIM episode.
[161.34 → 164.06] We put a lot of work into that, and it sounds like everybody enjoyed it.
[164.12 → 165.00] We're happy to hear that.
[165.58 → 169.20] And one of the things that we heard over and over and over and again was,
[169.64 → 170.36] When Neovim?
[170.70 → 173.58] So similar to the crypto kitties say,
[173.64 → 176.46] When Moon, the Neovim kitties were saying,
[176.88 → 178.02] Hey, you've done VIM.
[178.02 → 181.24] Now give us the Neovim treatment.
[181.50 → 187.50] So by popular demand, we have TJ Decries here to talk Neovim with us.
[187.54 → 188.78] TJ, thanks for coming on the show.
[189.24 → 189.90] Yeah, it's my pleasure.
[190.04 → 193.66] Really excited to chat and just explore some fun topics together.
[194.06 → 195.00] We are excited too.
[195.16 → 201.92] And I have with me, not Adam Stack, it is Nick Needed, my co-patriot at JS Party.
[202.06 → 203.36] Nick, welcome to the changelog.
[203.80 → 204.22] Hoi.
[204.36 → 205.30] I'm happy to be here.
[205.38 → 206.86] Excited to talk about Neovim.
[206.86 → 211.08] And just for the record, it wasn't just me hounding Jared to get a Neovim episode.
[211.48 → 214.18] That wasn't your bot just telling me over and over again.
[214.86 → 218.56] I can't confirm or deny that, but it wasn't me specifically.
[219.20 → 223.84] Well, if you know JS Party, you know Nick is often trying to turn it into VIM Party.
[224.54 → 227.12] And he brings up VIM whenever he has opportunity.
[227.36 → 229.86] And he has been for a little while a Neovim user.
[229.96 → 231.32] How long have you been on Neovim, Nick?
[231.78 → 232.92] It's been a couple of years.
[232.92 → 238.76] But I'm a recent convert to the Neovim 0.5 slash Lua lifestyle that I'm excited to talk
[238.76 → 239.30] about today.
[239.30 → 246.34] I will also confess that after our VIM episode and our modern Unix tooling episode, I've been
[246.34 → 249.24] reinvigorated, and I installed Neovim.
[249.44 → 250.94] And I threw away my VIM config.
[250.94 → 257.74] And I'm doing survivor style, which configs make it into the new config game, line by line.
[257.90 → 259.28] And I'm having lots of fun.
[259.78 → 265.38] I feel like a kid again, just tweaking and changing and kind of relearning how to use VIM.
[265.44 → 270.34] Because I've been using it for a very long time in a dual capacity with a full-time GUI.
[270.44 → 271.90] So I was on Sublime Text for years.
[272.10 → 273.32] I switched to VS Code.
[273.32 → 275.92] And I always had VIM open in a shell.
[276.14 → 277.30] And I would use it on servers.
[277.30 → 278.88] And I would use it kind of casually.
[279.12 → 281.80] As you know from that episode, I always use VIM mode whenever available.
[281.98 → 287.60] But I was not using it full-time as my programming editor until a few weeks ago.
[287.70 → 288.30] So I'm back.
[288.60 → 289.72] And I'm giving Neovim a try.
[290.20 → 291.44] And I'm having a lot of fun.
[291.52 → 293.30] But TJ, give us some of the backstory here.
[293.72 → 295.54] Because Neovim has been around for a while.
[295.62 → 298.36] And we've never done a show on it, despite multiple cries to do so.
[298.84 → 300.04] Who created Neovim?
[300.20 → 301.14] When did they start it?
[301.40 → 301.76] Why?
[301.76 → 303.40] Why did this have to exist?
[303.56 → 303.92] Et cetera.
[304.02 → 304.68] Give us the backstory.
[305.18 → 305.32] Yeah.
[305.42 → 310.56] So I think the main person who first started it was Tiago Garuda on GitHub.
[311.46 → 314.08] And it was probably about 10 years ago.
[314.14 → 315.60] I don't remember the exact date.
[315.98 → 320.28] The main thing that happened was Garuda was really interested in getting
[320.28 → 328.50] sort of some of the ability to run external jobs asynchronously from within VIM.
[328.90 → 329.12] Right?
[329.12 → 331.16] And that was the first main push.
[331.16 → 337.06] And Garuda submitted some patches to VIM Dev, which is the mailing list for VIM.
[337.56 → 342.50] But unfortunately, at the time, Garuda, the patches didn't work for Windows.
[342.50 → 346.68] And there were some other problems that would have broken compatibility with like a lot of
[346.68 → 349.08] the places that VIM expects to build.
[349.72 → 354.46] And so due to that, it was sort of like this struggle of, I don't know if struggle is the
[354.46 → 358.66] right word, but just sort of difficulty trying to figure out how these features could work
[358.66 → 363.62] within VIM and all the places that VIM needs to build and the size requirements and all these
[363.62 → 364.06] other things.
[364.06 → 364.30] Right.
[364.56 → 370.42] Which are like super valid concerns to have if you're on all the places that VIM can build.
[370.58 → 370.78] Right.
[370.84 → 372.84] Like, do you want to still be able to do that?
[372.90 → 377.14] That's one of the selling points is sort of the universalism of where VIM is.
[377.24 → 379.48] He didn't have an old Polaris machine to test it on?
[380.04 → 380.44] Right.
[380.44 → 383.16] He did not make any patches that work there.
[383.62 → 388.56] So basically, at that point, Garuda was kind of like, well, I don't want to necessarily
[388.56 → 389.70] have to support those.
[389.80 → 392.98] Like, I want to do different things that can work differently.
[393.08 → 398.16] And I want to like push forward in some of these areas that might make us end up in a
[398.16 → 400.18] place that's not the same place that VIM is.
[400.30 → 400.46] Right.
[400.98 → 404.28] And so Garuda basically started Neovim.
[404.28 → 409.28] And then from there, Garuda also had several other sorts of like large ideas in combination
[409.28 → 414.06] with people like Justin MK, who's still part of the project, as well as Six, who is one
[414.06 → 417.56] of the largest early contributors to Neovim.
[417.72 → 422.34] And they added other things like remote plugin support and started doing LUA scripting and
[422.34 → 423.06] things like that.
[423.70 → 430.18] But that was sort of the main branching point that started to allow Neovim to go down a separate
[430.18 → 431.00] path from VIM.
[431.50 → 433.66] Exactly how different is it?
[433.66 → 439.48] Yeah, so this is, I think, a pretty common misconception that VIM and Neovim are like
[439.48 → 441.02] very, very, very different.
[441.68 → 445.62] VIM and Neovim still share much of the same code base.
[446.14 → 450.26] Neovim still ports patches from VIM, like all the time.
[450.56 → 456.78] We have some contributors, especially like Jan Lao, who in the last 0.5 release helped
[456.78 → 461.56] to get us to over a thousand VIM patches ported from VIM into Neovim.
[461.56 → 467.82] So there's still sort of like an insane amount of similarity between the two.
[468.08 → 468.22] Right.
[468.32 → 475.32] And if you open them up, like you won't really see in effect, like any differences from like
[475.32 → 479.92] lightly configured and it dot VIM or VI MRC, whatever you want.
[480.04 → 484.12] You know, that's an important sort of like backwards combatting that we're interested in
[484.12 → 485.92] trying to work hard on.
[485.92 → 489.96] There are some things that are removed from Neovim that are in VIM.
[490.12 → 494.52] Like, for example, Neovim doesn't ship with a GUI by default, like GRIM.
[495.12 → 502.00] Neovim sort of removed all the code that tightly coupled it to a GUI application and
[502.00 → 504.16] instead implements GUIs over RPC.
[504.38 → 508.46] So that's like an example of if you were expecting to be able to just open up GRIM.
[508.68 → 512.50] But with Neovim, that doesn't happen because those two things have been sort of decoupled,
[512.50 → 514.52] as well as various other things.
[514.52 → 519.72] Like if you installed Neovim, it wouldn't install like Vue, the command Vue, which is like opening
[519.72 → 526.02] VIM and read-only mode, because you can instead do like vim dash R or something.
[526.14 → 527.88] I don't remember what it is off the top of my head.
[527.94 → 528.50] Sorry, everybody.
[528.60 → 533.02] But you could just alias that to be the same, and then it would retain the same behaviour.
[533.16 → 537.34] So of course, there are some, you know, similarities that are obvious at the start and some things
[537.34 → 539.84] that are a bit different when you're first encountering them.
[539.96 → 544.60] But in general, there's an incredible amount of overlap still between the two projects,
[544.60 → 545.12] I would say.
[545.66 → 551.44] That would be my experience so far is that I haven't noticed a difference in just like
[551.44 → 552.60] regular text editing.
[552.94 → 554.84] Like I could just alias it and never notice.
[554.94 → 558.78] Now, once I started configuring it and trying to do some more advanced things, you start
[558.78 → 560.68] to see where the seams are, the differences are.
[560.74 → 561.22] Go ahead, Nick.
[561.24 → 561.64] What were you going to say?
[561.64 → 565.90] Oh, I was going to say something similar in that when I started using it, I actually
[565.90 → 569.10] started using it, I think for the same reason that it might have been created now that I'm
[569.10 → 569.62] hearing that.
[570.00 → 573.78] And that's because I heard about this async job support and I had just gotten into like,
[574.02 → 575.94] you know, configuring linting and things like that.
[576.02 → 578.68] But every time it would glint, it would like completely freeze VIM.
[579.06 → 580.26] And that was just super annoying.
[580.42 → 584.10] So then I heard about Neovim and how it could do that asynchronously.
[584.24 → 586.98] And so I set it up, but I was like, this is just temporary.
[587.42 → 589.98] I'm sure VIM is going to catch up, and I'm just going to switch back to it.
[589.98 → 593.96] So I installed it and I did that alias, alias VIM equals VIM.
[594.38 → 595.66] And I still have that.
[595.70 → 596.94] And that's still how I invoke it.
[597.00 → 600.48] But that alias is like five years old at this point or five or six years old.
[601.14 → 607.16] And now I, yeah, it's just interesting that I really can't tell the difference or couldn't
[607.16 → 611.76] tell the difference in the beginning, aside from like where your config lies and that.
[611.86 → 615.60] But otherwise, when you start up, it said instead of VIM, it said VIM.
[615.78 → 617.22] That was pretty much the big difference.
[617.22 → 617.94] Yeah.
[618.08 → 622.88] And like just to mention as well, like VIM does have those capabilities now, right?
[622.92 → 625.00] Like it does have asynchronous jobs and other things.
[625.06 → 628.18] I just figure I want to throw that out there in case people are interested in adding some
[628.18 → 630.52] of those things to their own VIM config.
[630.94 → 633.20] But it does exist in both now.
[633.42 → 635.00] Yeah, that's one of the cool things that I've noticed.
[635.00 → 640.60] I wonder if NEOVIM is directly to blame or to accredit for this.
[640.68 → 645.98] But it seems like VIM's development picked up with regard to performance, synchronization
[645.98 → 649.32] and certain things that maybe weren't being advanced.
[649.32 → 653.52] And maybe there was a little bit of, you know, competition spurs innovation thing going on.
[653.60 → 655.42] That was just my casual observation.
[655.70 → 658.04] Is that your thoughts as well?
[658.04 → 662.22] Or if we ask Bram about it, would he say, yeah, I saw NEOVIM coming, and I was like,
[662.26 → 663.58] holy cow, I need to start doing more.
[663.72 → 665.14] Or what's the story there?
[665.68 → 669.04] I actually think that this is probably like a common misconception.
[669.42 → 673.98] I think Bram likes implementing things that he thinks people are going to use.
[673.98 → 679.90] And like, it wasn't really clear, like from the community that this was an important thing
[679.90 → 682.94] for them to like have previous to this.
[683.12 → 685.92] My personal opinion, obviously, I'm not inside Bram's head.
[686.12 → 690.46] And we've only spoken just casually a few times, you know, on GitHub issues or email.
[690.96 → 695.92] Is that Bram just was like, oh, there's people requesting this now in VIM dev.
[695.98 → 697.66] And they're like thinking about it a lot.
[697.74 → 699.54] Like, oh, we can implement that.
[699.62 → 701.72] And so then he implements it and it works well.
[701.72 → 704.18] And then he's happy with like the solution.
[704.48 → 710.64] I'm not 100% confident that like the NEOVIM like spurred him on to do that.
[710.74 → 712.66] I don't necessarily think that that's exactly the case.
[712.72 → 717.74] I think it's much more that Bram saw that people in VIM dev were like, this is cool.
[717.82 → 718.50] We should have this.
[718.52 → 721.14] And he was like, OK, I'll make one that works well for inside of him.
[721.22 → 722.38] And then that's what he did.
[722.68 → 722.82] Yeah.
[723.30 → 727.50] And to that point, both of them have like async and other similar features.
[727.60 → 729.92] But have they arrived there in different ways?
[729.92 → 733.92] Like, is it different APIs or ways to like invoke async, for example?
[734.46 → 734.72] Yes.
[734.82 → 739.82] So to like to start external jobs, the jobs APIs aren't compatible.
[740.06 → 744.28] There are like plugins that sort of wrap them to make them very similar.
[744.58 → 750.94] So you could like have one that's shared, and you call my shared lib dot start job or whatever.
[751.14 → 751.36] Right.
[751.40 → 755.18] And you could be doing that and sort of experiencing working them in both.
[755.18 → 757.60] But their implementations are different.
[757.90 → 767.10] Like Neovim is really focused a lot on building around like lib UV, which is the stuff that like I think Node, if I remember correctly, is built on top of.
[767.30 → 769.72] Probably know about that in JS Party Land.
[770.34 → 770.44] Right.
[770.48 → 773.52] So like Neovim's event loop and stuff is built around like that.
[773.52 → 782.66] And so we use lib UV bindings to do like the async jobs and many of our other event loop type things that we're interested in doing.
[782.88 → 786.62] And I haven't looked in depth at what then how it actually implements it.
[786.78 → 789.20] If I recall correctly, they're not using lib UV.
[789.44 → 792.66] So like the underlying implementation is not the same.
[793.26 → 793.78] Right.
[793.86 → 795.78] But their APIs are like pretty similar.
[795.78 → 798.20] And it's possible to write code that works in both.
[798.36 → 800.40] It's sometimes a bit annoying, but that's OK.
[800.40 → 808.54] And with the help of those like community plugins, is the burden on like plugin developers kind of lessened or almost nonexistent by that?
[808.60 → 810.90] Or does that kind of cause some issues?
[811.44 → 818.54] If all you want to do is run a job asynchronously, then it is not like incredibly difficult.
[818.54 → 831.86] There are other things that are much more like difficult to maintain shims between or some things that are very specific to Vim or very specific to Neovim that either haven't been like unified or never will be.
[832.32 → 835.60] For example, right now in Vim, there are APIs.
[836.06 → 837.80] They're all prefixed with pop-up underscores.
[837.94 → 841.36] There's like pop-up underscore create or pop-up underscore menu or things like this.
[841.36 → 841.54] Right.
[841.54 → 843.82] And they allow you to make little floaty windows.
[844.64 → 846.70] Neovim currently doesn't have those APIs.
[847.16 → 851.68] And we have not a shared floating window implementation underneath the hood.
[851.74 → 855.98] So it's not necessarily simple to just like to port the patches over and get the results.
[855.98 → 865.32] But I'm working on a project and other people are contributing as well to create like Lua API that we can create windows with.
[865.32 → 877.80] And then we could expose a thin wrapper over that back in Vim L that's the same or looks the same to the user so that you could write plugins in Vim script.
[877.98 → 882.74] And they would work in Vim or Neovim, even though the underlying implementations aren't the same.
[882.74 → 889.22] So it's not that we've completely abandoned any hope of like still making some things the same.
[889.34 → 895.72] But like right now, if you wanted to have floating windows in one versus the other, you'll have to write very different code.
[895.84 → 904.44] But if it's literally just like I just want to spin up a job and have it run externally, you could probably have that working for your plugin in like five or ten minutes for simple cases, I would say.
[905.06 → 910.78] So it sounds like the longer it goes, the less underpinnings they share.
[910.78 → 920.88] You mentioned that there was a thousand patches or so in the 0.5 that were like direct ports from Vim into Neovim.
[921.66 → 926.84] Do you expect over the course of Neovim's life that that number would decline over time?
[927.00 → 936.14] Or do you think there's enough foundation that's shared that there's always going to be massive amounts of shared porting the solutions that come with over there onto the Neovim side?
[936.14 → 941.50] In general, I try not to predict the future too much because it's a difficult game to play.
[941.74 → 942.88] But what trend are you watching?
[943.06 → 943.70] Give us the trend.
[943.82 → 943.98] Yeah.
[944.54 → 949.28] In certain areas of the code, I would see us still porting patches for a long time.
[949.38 → 952.40] And port is in some cases like very loose.
[952.48 → 961.78] It might be literally just applying style differences and putting them in and then porting like tests written in Vim into Lua because we write most of our tests in Lua.
[961.78 → 967.02] So some of those patches are like very simple, and they like are almost direct applications.
[967.34 → 976.96] So there are some areas that I would expect that to like to happen for a long, long time, like a bunch of things in like evil.c, which is where, you know, Vim script things get done.
[977.02 → 978.34] Like it's like, okay, it was simple.
[978.42 → 982.08] We just added this new argument to a Vim script function.
[982.38 → 983.02] Okay, cool.
[983.14 → 986.10] We can try and port that over, and then we can have that the same in both.
[986.10 → 990.16] But in other areas, there already exists no way to port patches.
[990.44 → 995.10] For example, like for floating Windows code, we have two separate implementations.
[995.92 → 998.64] So it makes no sense to port any of those patches.
[998.78 → 1001.10] They get marked as not applicable for Neovim.
[1001.74 → 1010.40] But it may be that we in effect port some of those patches over in attempts to keep the community as like close as we can.
[1010.40 → 1023.52] Right, like with the example I gave of the pop-up APIs where Neovim would still like to implement those so that people don't have to worry about which one they're writing for, and they can continue serving both communities easily.
[1023.52 → 1044.28] More and more startups are using Retool to focus their time on their core product.
[1044.60 → 1046.94] And that's exactly why they launched Retool for Startups.
[1046.94 → 1053.06] This is a program that gives early stage founders free access to a lot of the software needed for great internal tooling.
[1053.48 → 1055.02] And Retool has worked with thousands of startups.
[1055.38 → 1060.24] And the trend line they noticed was technical founders spending tons of time building internal tools.
[1060.62 → 1065.14] That means at this critical stage, these founders were distracted from their core product.
[1065.50 → 1066.36] The goal is simple.
[1066.62 → 1072.54] Make it 10 times faster to build the admin panels, CRUD apps, and the dashboards most early stage teams need.
[1072.54 → 1085.78] And Retool has bundled together a year of free access to Retool with over $160,000 in partner discounts to save you money while building Retool apps with common integrations like AWS, MongoDB, Bred, and Segment.
[1086.14 → 1087.64] There is so much you can do with Retool.
[1087.92 → 1096.48] You can use these free credits to build tools that join product and billing data into a single customer view, tools that convert manual workflows into fully featured apps for your team,
[1096.48 → 1102.42] or tools that help non-technical teammates get access to your database to read and write data, analyze, and query.
[1102.54 → 1104.20] These are just a few examples.
[1104.64 → 1108.92] Learn more, apply, and join Lightning Demos at retool.com slash startups.
[1109.18 → 1111.18] Again, retool.com slash startups.
[1124.64 → 1125.82] So let's talk Lua.
[1126.16 → 1127.14] Yeah, that sounds good.
[1127.14 → 1133.74] On our Vim episode, I asked everybody what frustrations they have with the editor, and Gary Bernhardt said, Vim Script.
[1133.74 → 1139.90] I'm pretty good at complaining, so I'll limit myself to just one thing, Vim Script.
[1140.02 → 1144.52] To understand Vim's relationship to its scripting language, let me contrast with Emacs.
[1144.70 → 1148.86] Emacs is more, is almost like an operating system that happens to ship with an editor.
[1149.66 → 1157.84] And long-term Emacs users will effectively end up rewriting parts of that editor sometimes, but it's still Emacs because the layers underneath are still Emacs.
[1157.84 → 1160.18] So Emacs Lisp is a whole programming language.
[1160.40 → 1162.18] It was designed to be a programming language.
[1162.44 → 1164.28] Vim is not like this at all.
[1164.44 → 1165.76] Vim was designed to be a text editor.
[1166.12 → 1167.28] It had a configuration language.
[1167.38 → 1172.88] That configuration language grew over time to acquire normal programming constructs, and that is what we call Vim Script.
[1173.04 → 1178.70] So it's a hodgepodge, and it wasn't sort of designed all at once, and I don't think it's controversial to say its kind of a mess.
[1178.70 → 1186.50] So that is the most frustrating part of Vim for me, and it also is one of the reasons that I avoid configuration when I can.
[1187.00 → 1193.34] I have a very sort of mostly stock Vim configuration, despite 15 years, and Vim Script is why.
[1194.14 → 1196.46] So this is something Neovim's taking head-on, isn't it?
[1196.66 → 1205.70] Yeah, I think Neovim's choice of choosing Lua as what I would consider sort of like the de facto future of configuring Neovim.
[1205.70 → 1211.56] Not that it won't be possible to write Vim Script or that we will like to remove the engine or anything like that.
[1211.94 → 1212.92] That is not happening.
[1213.26 → 1216.82] We will continue to support that and allow that to happen.
[1217.40 → 1227.52] I think Lua has invigorated a lot of people to be interested in both contributing and sort of being able to explore making Neovim more their own.
[1227.52 → 1239.76] Not only is like Lua like a programming language that has lots of external libraries that you could install with like Baroques and things like that, and there are a lot of other external resources for learning Lua.
[1240.02 → 1245.00] But there's also really cool things like Last, which allows for crazy performance.
[1245.30 → 1247.92] That's just like sort of insane.
[1247.92 → 1262.60] We'll talk probably a little bit about Telescope later, but like Telescope can find and fuzzy sort literally like tens of thousands of items as you're typing in one main thread attached to the UI.
[1263.02 → 1267.66] We currently have some stuff in progress to do a few things in a little bit smarter way so it doesn't block.
[1267.66 → 1278.46] But regardless, it's doing an incredible amount of work like as you're typing and that sort of like performance is just not possible with old Vim Script.
[1278.76 → 1283.26] It's true that Bram's working on Vim9Script and there will be performance improvements there.
[1283.86 → 1290.98] There's a lot of people I know that I've talked to personally that are excited to use Lua because there are applications outside Neovim, right?
[1290.98 → 1298.94] They're like, oh, I used this for scripting before in a video game, or I've used this in, you know, whatever C application or, oh, I've embedded this here.
[1299.04 → 1308.86] So they have sort of like previous experience or future experience that they'd like to have with the language that maybe makes it more accessible and exciting for them, as well as being fast.
[1309.82 → 1315.20] Given Neovim's architecture on top of Lib UV, was JavaScript considered as a potential language?
[1315.60 → 1318.62] It was, I think, considered but discarded.
[1318.62 → 1330.60] I mean, JavaScript's ability to be embedded easily inside a C application is not, I think, considered one of its strong suits, as well as sort of its minimalism, right?
[1330.68 → 1334.94] I mean, Lua can be run and is run inside some like Linux kernels.
[1335.30 → 1346.68] So the portability and the size and all of these other things are really great features, as well as like Neovim, I guess, like pinned in a way to Lua 5.1,
[1346.68 → 1349.34] which is the language is complete.
[1349.60 → 1350.28] There are no changes.
[1350.56 → 1352.50] There's no new things being added to the language.
[1352.70 → 1363.02] There are no things being removed, which is really nice for writing a plugin now and having it work in 15 years as opposed to not throwing shade at anything in JavaScript.
[1363.02 → 1372.96] But I feel like it is a common problem that I see people talk about on the internet that yesterday my NPM build worked and tomorrow it does not.
[1373.42 → 1375.84] Not to mention, you know, changes within the language itself.
[1375.84 → 1382.02] So there are a lot of things about Lua that provide sort of an incredible match with Neovim.
[1382.34 → 1393.40] Like I said, expendability, size, portability, and the fact that it's sort of static are really great things for us in terms of shipping a small binary that can work in a lot of places.
[1393.94 → 1397.68] Yeah, it almost seems like Lua was purpose built for use cases like this one.
[1397.68 → 1401.90] Yes, that is exactly what the design principles of Lua are.
[1402.20 → 1404.82] One of the primary design principles is expendability.
[1405.42 → 1409.24] So, yes, this is exactly the case where you would want to use Lua.
[1409.42 → 1413.94] You do not want to use Lua to write your 10 million line monolith.
[1413.94 → 1416.48] That is not the purpose of the language.
[1416.66 → 1427.14] The purpose of the language is to be embedded inside other languages to provide relatively safe and easy ways to script and extend something, right?
[1427.16 → 1435.78] Like you're not going to have a memory like leak in the same way or a memory problem with like writing C to script your editor or something like that.
[1435.88 → 1441.38] That's not exactly the same kind of fun experience, at least for me.
[1442.02 → 1442.46] Right.
[1442.46 → 1454.76] Now, Nick, I know that you've been porting your Vim config over to Lua in the last couple of weeks because, as TJ mentioned, Neovim, you can configure it in Vim script, and you can also configure it in Lua.
[1455.28 → 1457.98] You can have an unit. Vim or an unit.Lua.
[1458.06 → 1458.98] Is that the same file name?
[1459.32 → 1460.28] Yeah, you can have either one.
[1460.56 → 1461.40] You should not have both.
[1461.88 → 1464.94] But, Nick, you've had both here for a while, or I don't know how you've been managing that.
[1465.12 → 1466.10] What's been your experience?
[1466.22 → 1468.52] Because I don't think you've used Lua previous to this.
[1468.54 → 1468.96] Is that right?
[1469.36 → 1469.82] That's true.
[1469.82 → 1471.54] I have not used Lua before this.
[1471.54 → 1476.72] And I initially was hesitant to even start because I was just like, I don't want to learn Lua.
[1476.94 → 1479.12] I don't have any practical application for it.
[1479.18 → 1481.80] But then I was like, wait a minute, I'm learning Vim script.
[1482.02 → 1484.48] I don't have any practical application for that outside of this.
[1484.98 → 1489.66] The thing that really pushed me into it, as I mentioned, I've been kind of a recent convert to that.
[1489.66 → 1498.54] I know that a lot of people have been using nighties of Neovim, like, I guess, 0.5, maybe I'd call it, the Lua support version for a while.
[1498.66 → 1502.06] But I only recently jumped on that and started using it.
[1502.40 → 1505.36] And it was because I saw some cool plugins that I wanted to use.
[1505.36 → 1520.94] And so it initially just started out with me installing the nightly of Neovim and then just having my unit. Vim and putting in, like, a Lua require opening up the configuration for, like, a specific plugin and be able to use that.
[1520.94 → 1525.34] And I kind of didn't like that as I started adding more and more plugins.
[1525.48 → 1528.34] I didn't like that I just kept calling out to Lua for that.
[1528.42 → 1539.62] And so I started, like, I just went in as an experiment to see, like, what it would take to translate my, like, at the time, 600-something line of unit. Vim into unit.Lua.
[1539.88 → 1545.84] At the end of it, it came out as, like, 240 lines of Lua, which was pretty surprising.
[1545.84 → 1551.00] But that's because I, like, split out plugins into its own plugins.Lua that set up all of that.
[1551.04 → 1552.30] But that was still only, like, 50 lines.
[1552.38 → 1553.96] Like, I lost 200 lines in there somewhere.
[1554.54 → 1556.88] And I feel like it's more powerful now.
[1557.32 → 1559.48] And that's losing, not like losing your car keys.
[1559.54 → 1560.88] That's like losing weight, you know?
[1560.94 → 1562.10] That's the kind of losing you want to do.
[1562.26 → 1562.60] Exactly.
[1562.78 → 1562.96] Yeah.
[1563.98 → 1570.80] But I guess from your perspective, TJ, would you say that there's a big benefit to converting, like, your configuration to Lua?
[1570.80 → 1577.02] Or is this, was the primary intention to be more, like, for plugin authors to be able to write more robust plugins?
[1577.56 → 1577.72] Yeah.
[1577.84 → 1582.74] So there's, like, a couple, I guess, sort of aspects to chat about, like, in that area.
[1582.92 → 1594.30] The first one is I don't think that we have yet implemented everything in Neovim to make it, like, super elegant and easy to write your entire configuration in Lua.
[1594.50 → 1596.62] Like, that's going to take time.
[1596.72 → 1600.22] Like, I have a work-in-progress PR for auto commands, for example.
[1600.22 → 1600.58] Yeah.
[1600.76 → 1604.02] That would allow you to directly pass Lua refs inside.
[1604.26 → 1611.36] And, like, Neovim in the C code will hold a reference to that Lua ref until it's ready to release it and then release it.
[1611.62 → 1611.84] Nice.
[1611.88 → 1613.84] But that requires, like, a lot of changes.
[1614.26 → 1616.94] But that's a story for a different day if we want.
[1617.18 → 1623.06] But the point being, you still basically have to write your auto commands in Vim Script, even if you're, like, inside Lua.
[1623.18 → 1625.52] I have a lot of in Vim execs in there for that stuff.
[1625.66 → 1626.20] Yeah, exactly.
[1626.20 → 1630.42] So, like, that doesn't really give you any necessarily gain.
[1630.52 → 1634.80] So, there are some parts of my config that are still in Vim Script and probably will be for a long time.
[1634.96 → 1640.38] I mean, the other part, too, is, like, if it's working really great for you, I don't see any reason to change it over.
[1640.38 → 1647.04] Like, it's going to work well, like, to do a lot of the set operations or, like, simple things like that.
[1647.20 → 1650.50] Like, Vim Script is a DSL for doing those.
[1650.62 → 1654.92] It will work probably nicer than we can sometimes do inside Lua.
[1655.20 → 1667.38] Although some of them have sort of been mitigated by things like Vim. Opt, which allows you to sort of use Lua and MetaTables to set Vim options more, like, ergonomically, I guess.
[1667.38 → 1674.42] So, I would say, like, there are things that are nice about setting up your config in Lua.
[1674.60 → 1682.98] Like, you know, you can use closures really easily and there's a lot of ergonomics about passing around functions or doing validation or whatever that is.
[1683.36 → 1689.44] But I don't see, like, a lot of gain of, like, just switching over to unit.Lua right now.
[1689.44 → 1696.20] I think a lot more of the benefits are about extending, like, particular parts of your, you know, configuration.
[1696.64 → 1705.64] Maybe you have a complicated function that, you know, shelled out to some commands and parsed some strings and then would do something within a certain buffer of a certain file type.
[1706.02 → 1709.98] Well, that might be a lot nicer to write in Lua than it is in Vim Script, right?
[1709.98 → 1716.52] But, like, changing set number to Vim.opt.number equals true, I don't know.
[1716.58 → 1720.84] That doesn't really strike me as, like, wow, that's so mind-blowing.
[1722.06 → 1723.12] Pulling me out right now.
[1723.44 → 1727.66] So, maybe someday I would say, like, without hesitation, you should just port it over.
[1727.76 → 1736.92] But I think the primary focuses are much more about scripting the editor in a more sort of deep and customizable way than just, like, setting options, if that makes sense.
[1736.92 → 1748.54] For sure. And, yeah, I think that from that translation, a big thing that I really liked, like, yeah, auto commands and things like that, I'm just, like, basically it's just a string of Lua in my config that's being run.
[1748.84 → 1757.62] But other things, like, I use a plugin, I've used a plugin for years called Vim Stratify that lets me kind of configure what the Vim Start screen looks like.
[1757.62 → 1760.32] And, you know, it shows the recently used files and things like that.
[1760.40 → 1767.28] But it has a big, like, object that you configure and tell it exactly what you want it to show and do and all of that.
[1767.82 → 1776.98] And doing that in Vim Script, like, I've always just hated that syntax because you have to, like, as you put things on a new line, you have to have the forward or the backslash on it everywhere.
[1777.22 → 1778.50] And it was just really annoying.
[1778.50 → 1783.32] But things like that, being able to use, like, a Lua, do you call that a table?
[1783.62 → 1783.78] Yeah.
[1784.10 → 1789.64] Yeah, a Lua table to hold all of that information and then just be able to access it from Vim.
[1789.84 → 1796.32] And I can do things like access other, like, objects like that through, like, the I think it's underscore capital G for, like, the global.
[1796.32 → 1801.56] And then being able to access from Lua Vim functions through Vim.FN.
[1801.78 → 1804.26] Like, that stuff is really cool, being able to do all of that.
[1804.26 → 1816.20] And I think that I'll probably keep my config in Lua going forward and just kind of adopt the new features as they come in, like, being able to set auto groups and things or, like, auto commands and things like that.
[1816.70 → 1820.68] But, yeah, right now that's just glorified Vim in strings being called.
[1820.82 → 1828.10] Like, if, you know, someone was starting today, and they made their config in Lua, I wouldn't be like, switch it back to Vim Script, it's better or something.
[1828.24 → 1831.00] And I wouldn't really do the same, as, vice versa either.
[1831.00 → 1840.30] I think, you know, if it's working for you, and you're, like, happy with the end result, there's no reason to, like, spend a bunch of time switching the language to be something else.
[1840.62 → 1845.62] I think they're both, like, perfect options for, like, configuration at this time.
[1846.04 → 1846.06] Yeah.
[1846.90 → 1850.30] I made the decision that I was going to start it in Lua because I'm, like, I'm starting fresh.
[1850.42 → 1851.14] I'm starting in Lua.
[1851.74 → 1853.04] And then Nick showed me his.
[1853.22 → 1859.74] And I'm like, nah, I'm going to go back to knit. Vim because I can just copy-paste those right in when I want them without thinking.
[1860.36 → 1860.76] Totally.
[1861.38 → 1873.80] The other kind of little bit challenging thing is depending on, like, if you, you know, spend your free time perusing.files on GitHub, if you find something cool in Lua, you either have to translate it to Vim if you're not using Lua or vice versa.
[1874.14 → 1878.36] And understanding how to do that translation is going to be fun for everybody.
[1879.18 → 1880.98] Not the most transferable of skills.
[1881.28 → 1882.74] You know, you're not going to put that on your resume.
[1882.74 → 1886.62] I can translate configurations between Vim Script and Lua.
[1886.90 → 1887.28] Oh, wow.
[1887.70 → 1888.60] Speak for yourself.
[1888.60 → 1901.30] Speaking of translating Vim Script to Lua, there's an interesting project that I have on my long-term horizon to explore that I've already written, like, a decent amount of stuff for.
[1901.30 → 1909.38] Which is trying to basically transpire Vim Script, the new language that Bram is making, into Lua.
[1909.82 → 1915.04] And then keeping as much of the semantics as we can between the two.
[1915.04 → 1920.92] One of my goals is, like, I would hope that we can keep Vim and Neovim, like, as close and friendly as possible.
[1921.16 → 1924.94] Like, no one on the Neovim team has any animosity with people on the Vim team.
[1925.14 → 1926.52] I don't really think vice versa either.
[1926.98 → 1935.90] So, like, it's a long-term project that I can't decide if it's real or not or how much of my life I will devote to it.
[1935.90 → 1942.58] But I have, like, some preliminary things and I can generate, like, valid Lua from Vim9 script.
[1942.80 → 1951.94] So, there's, like, still, even in places where people might, at first glance, think that it's going to be impossible for Vim and Neovim to, like, live together and be friendly.
[1952.40 → 1954.80] I still have goals to make them be friends.
[1954.80 → 1965.56] That's interesting because that's been one of my kind of lines of questioning that I'm thinking about here is that I'm starting to see, most recently, we'll get into Tree Sitter and stuff like that.
[1965.66 → 1967.92] But most recently, starting to see some plug-ins.
[1968.00 → 1973.74] There's one called Limelight, which was written in Lua for Neovim using Tree Sitter for better dimming.
[1974.64 → 1979.80] And it was the first time, because, you know, I watch a lot of these things, what people are working on, et cetera, for Changelog News.
[1980.08 → 1982.96] And a lot of times, it's like, this is a Vim slash Neovim thing.
[1982.96 → 1984.34] And that was, like, for years.
[1984.66 → 1987.32] It was either Vim only or Vim slash Neovim.
[1987.44 → 1989.48] And I'm starting to see, like, this is a Neovim thing.
[1990.28 → 1991.46] And there's no Vim equivalent.
[1991.60 → 1997.60] There's no, they didn't take the time, whatever you have to do, to maybe write it twice or whatever it is.
[1998.12 → 2001.82] And so, I started wondering, like, will that start to pull people away from Vim onto Neovim?
[2001.86 → 2004.76] And it's interesting, your perspective of, like, you don't necessarily want that to happen.
[2005.42 → 2008.08] Yeah, I mean, some of them are just impossible, at least today.
[2008.08 → 2013.64] Like, there's no way to get Tree Sitter, at least that I know of, like, inside of them, right?
[2013.72 → 2025.94] So, no matter what you do, if you want to build something on top of Tree Sitter, which is a really powerful and interesting technology, like, that's going to most likely end up being Neovim-only, like, plug-in.
[2025.94 → 2038.66] And, I mean, even for me, like, you know, I will probably talk about Telescope a little bit, but, like, Telescope's Neovim-only because it uses a ton of Neovim-specific APIs that are only available in Neovim.
[2038.66 → 2043.68] And, like, uses the window things in complicated and interesting ways.
[2043.68 → 2058.18] And, like, it relies heavily on the fact that you have Luo git installed and uses native C modules that we can link against C that, optionally, you can use to do sorting to make sorting even faster.
[2058.18 → 2066.00] So, I think, like, there will be plug-ins that exist that are only for Neovim, and there will be plug-ins that exist only for Vim, and that's fine.
[2066.24 → 2076.18] My goal, and, like, the Neovim team goal, I think, that I was trying to say before is basically just, like, we're not actively trying to make the community not work for both, right?
[2076.30 → 2076.50] Yeah.
[2076.92 → 2086.36] Well, I really appreciate that perspective because so many times when there are projects and efforts like these, so often it's like a hostile takeover kind of thing or a long con.
[2086.36 → 2092.58] Like, well, we're going to slowly take over, and I think that, I mean, at the end of the day, it's Vim, you know?
[2092.68 → 2093.64] It's a different Vim.
[2093.76 → 2094.54] It's a newer Vim.
[2094.64 → 2097.30] It's got things Vim doesn't have, and it takes things out.
[2098.28 → 2102.62] But still the same editor that we all know and love that's been around for all these years.
[2103.28 → 2104.52] Like, why would you want to crush that?
[2104.60 → 2105.42] Why would you want to kill it?
[2105.88 → 2109.10] Yeah, and I mean, like, I respect Bram a lot.
[2109.10 → 2115.46] Like, he's made an incredible piece of software, and it's, like, pretty bonkers if you just think about, like,
[2115.46 → 2119.22] where it started to where it is now and all the things that he's done for it.
[2119.32 → 2124.92] And, like, plus, Neovim is literally a fork, and so it's, like, we share a bunch of code that we never wrote.
[2125.06 → 2125.56] Like, I don't know.
[2125.58 → 2130.28] It feels kind of not very grateful and, like, not very thankful to just be, like,
[2130.78 → 2134.70] and now we're our own thing, and I don't, like, you know, it's like an angry teenager.
[2134.82 → 2136.62] Like, I don't even like you, Dad.
[2136.74 → 2137.04] You know?
[2137.04 → 2145.28] So, like, it's not exactly, like, the pinnacle of maturity, I think, necessarily all the time to, like, have that kind of situation.
[2145.70 → 2149.58] And so it frustrates me when I see it online between people as well.
[2149.62 → 2151.76] It's just, like, if they want to use Vim, that's cool.
[2151.88 → 2153.50] Why would you be mad about that?
[2153.56 → 2154.06] You know what I mean?
[2154.06 → 2156.84] That just seems cool to have them do that.
[2156.88 → 2157.34] That's great.
[2157.62 → 2157.86] Yeah.
[2158.14 → 2160.56] If we're going to hate on something, hate on the Emacs people.
[2160.64 → 2160.98] Come on.
[2161.10 → 2161.58] What's wrong with you?
[2161.58 → 2167.52] Well, I mean, Emacs is now closer to Vim and Neovim in spirit than many other places, right?
[2167.60 → 2169.72] So not to name any other names, obviously.
[2171.26 → 2171.70] Yeah.
[2171.86 → 2175.66] They need to join forces to take on the onslaught of the graphical editors.
[2176.30 → 2177.02] Oh, yes.
[2177.02 → 2179.72] The evil graphical editors from far away lands.
[2179.84 → 2181.00] In my browser now.
[2181.16 → 2181.48] Yeah.
[2191.58 → 2210.60] This episode is brought to you by our friends at Square.
[2210.98 → 2212.94] Square is the platform that sellers trust.
[2212.94 → 2220.28] There is a massive opportunity for developers to support Square sellers by building apps for today's business needs.
[2220.28 → 2223.42] And I'm here with Shannon Skipper, head of developer relations at Square.
[2223.62 → 2227.84] Shannon, can you share some details about the opportunity for developers on the Square platform?
[2228.14 → 2228.52] Absolutely.
[2228.80 → 2231.48] So we have millions of sellers who have unique needs.
[2231.76 → 2234.86] And Square has apps like our point of sale app, like our restaurants' app.
[2234.98 → 2241.22] But there are so many different sellers, tuxedo shops, florists who need specific solutions for their domain.
[2241.22 → 2252.58] And so we have a Node SDK written in TypeScript that allows you to access all the backend APIs and SDKs that we use to power the billions of transactions that we do annually.
[2252.84 → 2257.14] And so there's this massive market of sellers who need help from developers.
[2257.14 → 2268.56] They either need a bespoke solution built for themselves on their own Node stack where they are working with Square dashboard, working with Square hardware or with the e-com, you know, what you see is what you get builder.
[2268.78 → 2269.84] And they need one more thing.
[2269.92 → 2271.22] They need an additional build.
[2271.52 → 2279.56] And then finally, we have that marketplace where you can make a Node app and then distribute it so it can get in front of millions of sellers and be an option for them to adopt.
[2279.56 → 2280.34] Very cool.
[2280.44 → 2280.68] All right.
[2280.70 → 2288.48] If you want to learn more, head to developer.squareup.com to dive into the docs, APIs, SDKs, and to create your Square developer account.
[2288.78 → 2290.56] Start developing on the platform seller's trust.
[2290.92 → 2293.24] Again, that's developer.squareup.com.
[2293.24 → 2314.02] So, Nick, you mentioned that you were waiting for the Lua stuff to land or to be official.
[2314.16 → 2318.16] 0.5 came out this summer, July 2nd, I believe.
[2318.26 → 2319.16] A huge release.
[2319.16 → 2320.86] 4,000 commits, as I mentioned before.
[2321.30 → 2322.74] 1,000 of those reports.
[2323.24 → 2324.16] From Vim.
[2324.24 → 2325.62] But lots of new stuff.
[2326.60 → 2328.80] And the community rejoiced.
[2328.88 → 2330.60] I mean, this must have been a long time coming, TJ.
[2330.66 → 2332.20] How much work went into this release?
[2332.42 → 2334.56] Well, yeah, there was a lot of work.
[2334.70 → 2343.98] There was probably, if I had to take a guess, probably, I don't know, three or four weeks of time of me just answering when will Neovim 0.5 come out.
[2344.10 → 2346.98] You know, just replying to messages like that online.
[2346.98 → 2351.24] We started a meme on my Twitch channel when people would ask that.
[2351.24 → 2353.24] We did exclamation, the rule.
[2353.50 → 2361.82] And then that took a bot command back, and it explained that every time someone asks about Neovim 0.5 release, the release date has to be pushed back one day.
[2361.82 → 2374.42] Yeah, but in all seriousness, I mean, it's been a long time coming and it, you know, was a culmination of a lot of sorts of really long term project and vision that the team had.
[2374.42 → 2379.50] I can't take credit for all of it or even probably, you know, I can't take credit for most of it or anything.
[2379.72 → 2389.24] But, you know, seeing things like the LSP come to fruition, there's some fun history there where you can go dig up some of the original issues.
[2389.24 → 2405.42] And my first PR probably in 2016 or 2017, where I proposed a lot of the first ideas about how we would put LSP inside Neovim and have it be in such a way that it still is the spirit of Vim.
[2406.02 → 2411.86] You know, that it's not we're trying to smash everything in here and re-implement every wheel that we can.
[2412.32 → 2414.00] How can we do it in that way?
[2414.00 → 2417.20] So for me, it's been very fun to see that finally released.
[2417.36 → 2423.58] You know, it's been in my head for a long time and other people who helped along the way to finally implement it.
[2423.80 → 2440.32] And then as well, you know, putting in Tree Sitter, which has also been sort of a long term vision about making Neovim as an editor understand the text at a much higher and more, I'd say, interesting or semantic level than just like strings of characters.
[2440.32 → 2440.76] Right.
[2440.80 → 2442.24] Which is one of the goals of Tree Sitter.
[2442.24 → 2447.20] So let's focus in on LSP, the language server protocol.
[2447.38 → 2452.42] So this part didn't make the Vim show, but I did ask each person what they FOMO'd from other editors.
[2453.18 → 2454.82] And we wanted to keep it tight.
[2454.88 → 2456.02] So we dropped that section out.
[2456.14 → 2460.24] But I'll tell you, Drew Neal mentioned LSP specifically in VS Code.
[2461.52 → 2464.94] Yeah, well, I come back to language servers again.
[2464.94 → 2469.20] I mean, about a year or two ago, I started learning TypeScript.
[2469.74 → 2474.10] And I know that TypeScript has a very good language server.
[2474.24 → 2481.66] I mean, pretty much language servers and VS Code and TypeScript were all kind of invented under the same roof.
[2481.66 → 2483.52] And so they're very, very well integrated.
[2483.52 → 2489.52] And I knew that I wanted to understand what a good TypeScript development experience is.
[2490.30 → 2494.56] And so I made a decision not to use Vim while I was learning TypeScript.
[2494.92 → 2499.10] I thought, OK, VS Code is an editor that's very well positioned for beginners.
[2499.10 → 2509.60] And while I'm being a beginner in TypeScript, I'm going to be a beginner in VS Code as well and just learn the way that good language server integration would feel like.
[2510.00 → 2518.80] So that I can sort of take that learning and bring it back to Vim so that when I make that step of, OK, I'm going to now switch all my TypeScript development back over to Vim.
[2519.02 → 2520.22] I know what I'm looking for.
[2520.82 → 2526.70] For those who don't even know what LSP is, can you just explain what it is, where it came from, and then we'll talk about it in context in Neovim.
[2527.26 → 2527.70] Yeah, sure.
[2527.70 → 2530.16] So LSP is a protocol designed by Microsoft.
[2530.46 → 2536.66] It's actually what Microsoft's VS Code uses to communicate and basically get the language smarts that it has.
[2537.36 → 2543.56] Its big goal is, if you think about, you have M editors, right, in N languages.
[2543.56 → 2549.16] And when you want to implement support for the next language, you have to implement that M times, right?
[2549.16 → 2559.28] And so I think as developers, we're very familiar with M times N problems being very difficult and feeling intractable and also not fun to solve, right?
[2559.28 → 2564.70] Because even if you solve it once, you feel you're going to have to solve it N times again later.
[2564.70 → 2576.92] So LSP is basically a protocol designed to talk from editors to some sort of server that's giving you information about what you're editing, right?
[2576.92 → 2582.48] So if you have your cursor on somewhere in a document, you can say, hey, what's the definition of this?
[2582.64 → 2585.30] And so there's a protocol, text document slash definition.
[2585.58 → 2588.62] You send that over the wire to something that's running.
[2588.82 → 2589.84] It can be anything you want.
[2589.88 → 2591.32] It can be on your machine, another machine.
[2591.38 → 2591.90] Doesn't matter.
[2591.90 → 2598.50] Just a protocol that you send over the wire and ask, hey, what's the definition of this text document at this position?
[2598.78 → 2604.32] And it will return you back a list of possible definitions or one, you know, whatever the result is.
[2604.42 → 2606.70] And you'll be able to go there in the editor, right?
[2606.70 → 2609.60] So the editor will receive that response and know what to do.
[2609.82 → 2614.40] So this is really powerful because in theory, it's not always exactly like this.
[2614.78 → 2621.20] It'll turn the problem from M times N to M plus N, which is a much better problem to solve.
[2621.20 → 2625.08] And it's probably more like M plus N plus, you know, Z, right?
[2625.14 → 2626.50] There's some extra work still.
[2626.66 → 2627.02] That's a Z.
[2627.56 → 2629.00] Yeah, it still has to happen.
[2629.16 → 2635.76] You know, like some language servers have specific commands that only make sense for their language, you know, or things like that.
[2636.12 → 2636.72] But that's OK.
[2636.80 → 2639.68] That's still a much more fun problem to solve.
[2639.86 → 2641.62] And so that's sort of the basics of what happened.
[2641.76 → 2649.94] And like in the context of Neovim, what we saw was that this is sort of in a lot of ways just like an interface to your editor.
[2649.94 → 2663.66] And that was one of my big pushes for how we should think about LSP inside Neovim is this is really just defining a standard way that is shareable between other pieces of technology in how you can talk to your editor.
[2663.88 → 2664.04] Right.
[2664.04 → 2673.02] So I recently implemented something for my work at Source graph where I implemented like a go-to definition over LSP.
[2673.44 → 2679.96] But what it does instead of running something locally, it asks this external program where the definition of this thing is.
[2680.34 → 2680.44] Right.
[2680.46 → 2683.04] And so that was basically like a way for me to do that.
[2683.04 → 2688.54] And I didn't I mean, obviously, I knew how to move to the file and all these other things because I am familiar with Neovim.
[2688.80 → 2690.52] But it doesn't have to be so.
[2690.74 → 2690.86] Right.
[2690.92 → 2693.34] So it allows this interface to do.
[2693.52 → 2696.30] And then if I can do another plug for Lua in here.
[2696.36 → 2696.56] Right.
[2696.60 → 2701.48] The way that we did this with Lua is that it's very easy because everything is just a function.
[2701.48 → 2714.34] You can replace a function with a basic set of parameters and as expected thing to happen and replace it with some new behaviour that's more suited to your purpose.
[2714.62 → 2717.22] I'll give an example for that, which is in Golang.
[2717.74 → 2725.16] We have a bunch of stub or test implementations for some interfaces that we have at my work.
[2725.48 → 2729.90] I don't want to jump to those when I hit go to implementation.
[2729.90 → 2731.80] 99% of the time.
[2732.26 → 2738.00] So what I did was I can ask the LSP, hey, where are the implementations of this?
[2738.40 → 2750.48] I wrote some Lua code that walks through the results and says, if this file ends with underscore test or like underscore mock, discard it and throw that away from my results.
[2751.08 → 2753.56] Generally at work, we just have one result that remains.
[2753.86 → 2755.70] And then I just jumped straight to there.
[2756.10 → 2757.80] If there's only one left.
[2757.86 → 2759.24] Otherwise, I open quick fix list.
[2759.24 → 2765.64] So that's like really cool because now I only have to press the button to jump to that implementation.
[2765.64 → 2770.52] And it does exactly what I hope only in go code and everywhere else.
[2770.58 → 2772.34] It does the standard definition.
[2772.34 → 2772.62] Right.
[2772.62 → 2776.74] So there's this concept and idea of like the way that we want to design.
[2776.74 → 2788.72] It was this is just an interface for both language toolmakers and like editor toolmakers to be able to interact with in a way that you can customize to be just the way that you want.
[2789.08 → 2789.72] Good explanation.
[2790.10 → 2790.90] It's just amazing.
[2791.02 → 2793.04] I'm trying to think of ways that I might implement this.
[2793.30 → 2798.54] Nick, sometime you're welcome to come on my stream, and we can work on implementing it for you or something.
[2798.62 → 2799.72] It would be fun for this.
[2799.84 → 2800.60] For some other case.
[2800.60 → 2802.38] That'd be a lot of fun.
[2802.52 → 2803.14] That does sound fun.
[2804.02 → 2806.54] So tell me about the client server situation.
[2806.70 → 2812.74] Is this like a network server or is this like an embedded binary that you call?
[2812.88 → 2815.18] How does it actually talk and explain that?
[2815.68 → 2815.84] Yeah.
[2815.84 → 2823.58] So LSP can the primary modes that people use to communicate are either just standard in standard out or you can do it over TCP.
[2824.18 → 2833.02] Generally, if you're doing it over TCP, people just use some pipe and then pretend that it's TCP or something like that instead of actually doing TCP.
[2834.28 → 2838.00] But so Neovim doesn't care what's on the other side.
[2838.30 → 2840.60] We take a list of commands.
[2840.82 → 2843.28] We spin up that thing and start it.
[2843.28 → 2846.94] And then we have standard in standard out between the two.
[2847.18 → 2851.28] And we just send basically JSON over the wire for a request.
[2851.50 → 2855.32] And then they'll send JSON back over the wire to get to us.
[2855.34 → 2856.48] And it's just like a pipe.
[2856.66 → 2860.00] Generally speaking, it's possible to do other things.
[2860.00 → 2863.66] So you could have anything on the other side.
[2864.02 → 2866.14] So, for example, go, please.
[2866.24 → 2869.06] The go language server is written in go.
[2869.06 → 2873.74] And so it's just a go binary on your machine that you say, go, please start up.
[2874.00 → 2881.94] You send basically a configuration request so it can understand what directory am I in, what's part of this project, all those kinds of things.
[2881.96 → 2882.10] Right.
[2882.14 → 2884.18] That's part of the protocol to understand.
[2884.40 → 2887.24] And then it will just respond to requests as you send it.
[2887.24 → 2894.42] So there's also things like Microsoft's Place, which you can only run in VS Code due to licensing concerns.
[2894.42 → 2897.08] But that's written in TypeScript.
[2897.50 → 2899.06] So it's not written in Python.
[2899.20 → 2902.80] It just does the analysis in TypeScript and then sends the responses.
[2903.04 → 2904.80] But you're just editing Python files.
[2904.86 → 2905.82] You don't care what it's written.
[2905.90 → 2907.86] And it's just a protocol that talks between the two.
[2907.86 → 2910.54] So let's say I wanted to teach Neovim a new language.
[2910.94 → 2911.18] Yep.
[2911.30 → 2912.48] Let's say I had a language called Inc.
[2912.70 → 2914.50] And I wanted it to understand Inc.
[2915.02 → 2922.00] Would I then provide my own LSP, or would I plug something into the LSP that Neovim ships with?
[2922.04 → 2922.98] How would I get it in there?
[2923.60 → 2925.84] Ah, so maybe I should take a step back.
[2925.96 → 2930.66] So Neovim's LSP client is just Lua code that's inside Neovim.
[2930.82 → 2931.98] It's an LSP client.
[2932.10 → 2934.70] It does not have its own language server in there.
[2935.00 → 2935.24] Right.
[2935.30 → 2935.78] That's correct.
[2935.78 → 2938.76] So it doesn't know how to answer any of the questions.
[2938.88 → 2940.12] It only knows how to ask.
[2940.34 → 2944.22] I thought maybe it had like a set number of languages that already had all the stuff
[2944.22 → 2945.48] ready to go.
[2945.80 → 2946.68] Yeah, no, it does not.
[2946.78 → 2952.22] We have VIM LSP config, which is just like a repo that helps you get some of those running.
[2952.42 → 2956.66] But you need to figure out how to install those and make them executable on your machine.
[2957.16 → 2959.70] Being a package manager is not what we're good at.
[2959.78 → 2961.88] We're good at being a text editor.
[2962.28 → 2962.36] Okay.
[2962.42 → 2964.58] Someone else can figure that out and do that.
[2964.58 → 2966.88] And there are various plugins to help you install.
[2966.88 → 2973.12] But Neovim just has basically a bunch of Lua code that knows how to handle the responses and
[2973.12 → 2974.38] ask the right questions.
[2974.60 → 2977.44] You need to install separate executables to do that.
[2977.96 → 2982.58] And to that end, I'm using something called LSP install that handles installing those and
[2982.58 → 2985.34] then using LSP config to configure them for Neovim.
[2985.34 → 2987.72] Yeah, it'll just install it for you and stuff.
[2987.80 → 2989.38] So we leave that to other people.
[2989.48 → 2990.14] You can handle that.
[2990.22 → 2996.34] I'm sure there will be one for specific distros or specifically for Nix or there's one for
[2996.34 → 2997.22] Docker containers.
[2997.56 → 2999.22] There are a lot of different ways that you can do that.
[2999.28 → 3001.26] That's not our strong suit.
[3001.40 → 3003.80] We try and make text editors good and fast.
[3004.62 → 3004.88] Gotcha.
[3005.82 → 3008.86] Well, let's move on to Tree Sitter because another cool technology.
[3008.86 → 3011.94] It seems like they seem like they're similar, right?
[3012.02 → 3014.78] I mean, you're talking about the syntax tree of a language.
[3015.30 → 3018.34] Help us understand Tree Sitter and how it's different from LSP.
[3018.98 → 3019.16] Yeah.
[3019.30 → 3021.08] So this is a really common question.
[3021.28 → 3022.94] So it's a good one for sure.
[3023.48 → 3028.56] So a really high level way that you should start thinking about both technologies is that
[3028.56 → 3035.18] Tree Sitter only deals with one particular file, and it only deals with the text that is
[3035.18 → 3035.82] in that file.
[3035.82 → 3038.42] It has no additional information.
[3039.18 → 3042.70] And LSP operates much more on like a project wide level.
[3042.94 → 3045.16] It's going to open up and read all your files.
[3045.34 → 3046.68] It's going to index all of them.
[3046.78 → 3050.48] It's going to put a bunch of things in memory, and then it's going to be able to have some
[3050.48 → 3054.60] specific way that you can ask certain questions, and it will give certain responses.
[3055.44 → 3057.34] So that's sort of like the first aspect.
[3057.68 → 3064.68] The second aspect is Tree Sitter is built in a lot of ways specifically to run like inside
[3064.68 → 3068.50] of your text editor as opposed to like an LSP, which is some external process.
[3069.40 → 3075.22] So Tree Sitter at a high level, for those who don't know, is effectively a library for writing
[3075.22 → 3078.70] error recovering incremental parsers.
[3078.94 → 3084.96] And it's very good at doing that, which is awesome for text editors because most of the
[3084.96 → 3087.88] time when you're writing code, the code is broken.
[3087.88 → 3088.40] Right.
[3088.44 → 3094.64] If you type a line of code until you get to the semicolon in C, right, it is broken.
[3094.96 → 3100.80] So you want to write parsers that can recover and not like drop highlighting for the rest
[3100.80 → 3102.68] of the file or do things like that.
[3102.72 → 3102.86] Right.
[3102.88 → 3107.04] You want to actually do error recovery and smart error recovery.
[3107.04 → 3109.42] And that's like quite difficult to do.
[3109.80 → 3114.50] But Tree Sitter just sort of gives you that for free if you write a grammar in the correct
[3114.50 → 3114.86] way.
[3115.30 → 3116.66] So that's the first part.
[3116.98 → 3119.94] And then the second bit that's very important is that it's incremental.
[3120.34 → 3125.16] So it does not reparse the whole tree, which is awesome for when you're typing keystrokes
[3125.16 → 3129.48] in a very large file because you're going to smash 80 keystrokes.
[3129.58 → 3132.70] You don't want to reparse the entire file 80 times.
[3132.88 → 3132.98] Right.
[3132.98 → 3137.68] Instead, it actually just incrementally parses the things that it needs to and generates
[3137.68 → 3138.46] a new tree.
[3138.84 → 3139.88] Does that make sense so far?
[3139.96 → 3141.24] Any questions there?
[3141.64 → 3142.36] I'm with you.
[3142.82 → 3143.06] Okay.
[3143.38 → 3147.66] So once again, Tree Sitter only focuses on exactly that file.
[3147.66 → 3152.32] So this is cool because this lets you do things like you can request highlights for the file
[3152.32 → 3156.70] by asking the tree questions and basically getting back named nodes.
[3156.90 → 3159.82] You can write queries in this scheme-like language.
[3159.82 → 3162.10] It will return to you named nodes.
[3162.72 → 3165.02] And then in those nodes, they have ranges.
[3165.28 → 3168.10] And so you can colour them in your editor if you want.
[3168.22 → 3173.72] This is sort of like the thing that everyone recognizes about Tree Sitter, but I find somewhat
[3173.72 → 3177.60] like the least exciting of all the Tree Sitter technologies.
[3177.78 → 3178.86] But it is the most obvious.
[3178.86 → 3183.88] And it also makes sense from like a performance perspective that you would like to only change
[3183.88 → 3185.70] the highlights that need to be changed.
[3185.70 → 3191.64] So this is like a really great improvement and allows you to write much better and powerful
[3191.64 → 3196.24] syntax highlighting than you could with like just regexes, which is like the built-in Vim
[3196.24 → 3197.34] syntax engine.
[3197.34 → 3201.50] And it prevents you from getting these situations where like, I don't know if you've ever had
[3201.50 → 3206.66] this, but in certain complicated file types, if you like scroll down the page, sometimes
[3206.66 → 3209.90] it like thinks everything in the rest of your file is like a string.
[3210.12 → 3211.84] And you're like, what is happening?
[3212.04 → 3213.88] Why is this all string?
[3214.08 → 3216.96] That can't happen when you have a tree, right?
[3217.08 → 3218.90] That's not going to be an option.
[3218.90 → 3222.76] So that's sort of like the first level of Tree Sitter.
[3223.16 → 3225.62] And it doesn't communicate over the wire.
[3225.98 → 3230.50] This Tree Sitter is running inside Neovim, and it's like embedded inside Neovim.
[3230.74 → 3236.70] Now the parsers and the queries and things like that, those are external to Neovim, can be
[3236.70 → 3237.64] configured by users.
[3238.14 → 3243.38] I have my own custom grammar for Lua to do some special things, et cetera.
[3243.46 → 3247.72] So those are all sort of configurable, but the engine itself is built into Neovim.
[3247.72 → 3248.16] Hmm.
[3248.92 → 3252.74] And is the engine something that was built by the Neovim team, or you're actually embedding
[3252.74 → 3253.40] somebody else's?
[3253.44 → 3254.84] Is Tree Sitter its own project?
[3255.24 → 3255.42] Yes.
[3255.50 → 3256.70] Tree Sitter is its own project.
[3256.80 → 3261.38] It was originally made for Atom, but several other editors now have used it because it
[3261.38 → 3265.58] is designed to be a library to be embedded inside other editors.
[3265.90 → 3270.98] And so it's very, very fast and performant, and they spend a lot of time making it really
[3270.98 → 3271.34] awesome.
[3271.52 → 3272.92] And the Tree Sitter team is super cool.
[3273.22 → 3277.70] To get it started with it, you kind of similar to LSP config, you have to,
[3277.72 → 3279.24] install a separate plugin.
[3279.24 → 3282.26] And is that just to help with the configuration then?
[3282.36 → 3286.36] I think that's where I like had confusion was because I was like, I thought that it was
[3286.36 → 3287.98] built in, but I have to install this plugin.
[3288.24 → 3288.34] Yeah.
[3288.42 → 3292.78] So to be like clear about it, you actually don't have to install plugins for either.
[3292.78 → 3296.28] Like you can start up the server by yourself for LSP.
[3296.76 → 3296.94] Yeah.
[3296.98 → 3298.88] It just is a little bit more boilerplate.
[3298.98 → 3302.26] So that's why we have LSP config, but it's like certainly possible to do.
[3302.26 → 3305.84] LSP config literally only has configurations.
[3306.48 → 3311.02] But for Tree Sitter, you also don't necessarily have to install the plugin.
[3311.34 → 3312.52] It'll just be more complicated.
[3312.52 → 3318.76] Like it would involve you downloading a grammar file, running Tree Sitter to generate the bindings
[3318.76 → 3321.30] because it's a separate executable to generate these bindings.
[3321.46 → 3326.76] And then creating your .so shared executable and then putting that in the right place.
[3326.76 → 3329.10] So you could do that.
[3329.42 → 3334.60] And then the engine that's built inside Neovim will see that shared executable, load
[3334.60 → 3338.54] it up and appropriately attach it, I guess, to the buffer.
[3338.78 → 3343.54] But that is not very fun to do.
[3343.82 → 3345.72] So that's where Vim Tree Sitter comes in.
[3345.90 → 3352.08] And over time, we hope to, you know, upstream more of like Vim Tree Sitter into Neovim core.
[3352.08 → 3360.66] But there's a certain level of backwards compatibility and polish that we want to have in the core repository.
[3361.10 → 3366.02] And we felt that that would really hold back a lot of experimentation and interesting things happening.
[3366.46 → 3372.88] We tried to squish that all inside of Neovim core, which is where Vim Tree Sitter sort of came out as a separate plugin.
[3372.88 → 3381.92] So the engine, all the interior things to do, like get the tree and have it parse incrementally as you type and all of that kind of stuff,
[3382.04 → 3384.20] that's inside Neovim all the time.
[3385.14 → 3394.80] Someday, someday, my goal would be we would at least ship Tree Sitter grammars inside Neovim for C, Lua, and Vim, Vim Script,
[3394.80 → 3399.38] because those are the languages that Neovim deals with.
[3399.48 → 3404.98] And I think it would be cool to have a really awesome experience out of the box for those languages for people.
[3405.10 → 3406.46] But we're just kind of far away.
[3406.66 → 3411.34] Not maybe I don't know how far away we are, but we are not there yet to be able to do that.
[3411.50 → 3420.08] So it sounds like Tree Sitter is driving a lot of the innovation around these cool new plugins that I keep seeing that are Neovim only,
[3420.28 → 3423.82] not Vim as well because of the Tree Sitter support.
[3423.82 → 3431.70] Yeah, I can give you a really cool example of a few things that people have been doing with Tree Sitter that are like much further beyond just highlighting.
[3431.96 → 3432.38] Please do.
[3432.94 → 3440.92] Yeah, so a relatively like straightforward and easy to understand one is a plugin called nvimtscommentstring, I think.
[3441.04 → 3442.66] Off the top of my head, I don't remember exactly the name.
[3443.08 → 3448.90] But what it does is Tree Sitter tells you what language you are currently inside,
[3449.10 → 3452.94] and those languages can be embedded inside the same file.
[3452.94 → 3458.48] So for example, in JavaScript land, you can have, you know, like React elements.
[3458.66 → 3462.90] And so then inside there, you're kind of like in React, or I don't really know how any of that works,
[3462.90 → 3464.32] because I write back-end languages.
[3464.50 → 3466.54] But all of a sudden, I'm like, am I reading HTML?
[3466.78 → 3467.82] I thought there's JavaScript.
[3468.22 → 3469.36] I don't know what's going on.
[3469.84 → 3473.24] But one thing that's kind of annoying is if you use like a commenting plugin,
[3473.24 → 3478.78] and you try and comment something in the like JavaScript part versus like the HTML style part,
[3479.06 → 3481.46] you'll comment them incorrectly, right?
[3481.70 → 3482.56] So yes.
[3483.20 → 3488.76] nvimtscommentstring, all it does is it will just update the comment string option,
[3488.94 → 3495.00] which is a built-in option, depending on which language Tree Sitter currently detects.
[3495.00 → 3500.36] So if it detects that you're inside of JavaScript land, it'll set it to slash space percent S.
[3500.54 → 3505.66] If it detects that you're inside of HTML, it sets it to the long HTML thingy.
[3505.72 → 3506.70] That's annoying to type.
[3507.26 → 3507.62] Right.
[3507.96 → 3508.60] That's cool.
[3508.82 → 3513.64] That one just honestly rocked my world, because I've had that problem in my life forever.
[3513.64 → 3514.12] Yeah.
[3514.86 → 3518.24] And so this is even cooler because it doesn't just work for those languages.
[3518.88 → 3523.62] In Lua, you can write FFI code, which is actually C, right?
[3523.68 → 3529.78] And it is somewhat deterministic how you start and end those C def blocks.
[3529.78 → 3534.16] So you can actually write a Tree Sitter query that tells Neo them,
[3534.28 → 3538.08] hey, inside of these, this string, it's actually C code.
[3538.08 → 3543.92] And so you get C highlighting in this like random string in your file that you weren't expecting.
[3544.18 → 3548.66] And then if you're using TS comment string, and you comment out a line in there,
[3548.74 → 3552.12] it comments out that line like it's C code.
[3552.24 → 3555.68] So it's very, very powerful to be able to do something like that.
[3555.72 → 3556.62] It's very exciting.
[3556.88 → 3557.64] That's awesome stuff.
[3558.02 → 3558.86] That's one example.
[3559.04 → 3562.48] I'll give you another one that I think is, for me, it's very fun.
[3562.64 → 3566.76] So I use a snippets plugin called Lua Snips, and it's kind of interesting.
[3566.76 → 3568.38] I've just been exploring it lately.
[3569.02 → 3574.14] But it allows you to sort of run Lua code as you're expanding your snippets
[3574.14 → 3576.96] to sort of generate what the next text should be.
[3577.46 → 3580.72] So if you're familiar with Golang at all, you know that there's like,
[3580.80 → 3584.30] you write if error not equals nil like 10,000 times a day.
[3584.60 → 3586.00] Maybe that's an understatement.
[3586.16 → 3590.00] I haven't profiled myself yet, but I think it's somewhere around there.
[3590.26 → 3595.42] And what you do inside those error not equal nil sections is you have to write return
[3595.42 → 3599.64] and then the type signature basically with the default values, right?
[3599.68 → 3606.46] So if you return like an INT and error, then you have to do like return 0 comma error, right?
[3606.54 → 3609.02] So like you write this thing a ton of times.
[3609.18 → 3614.36] So I actually wrote a Lua snippet that will ask Tree Sitter.
[3614.58 → 3619.62] Basically, it has a custom query that I wrote inside of Golang that will ask Tree Sitter,
[3619.62 → 3621.92] hey, what is the return type of this function?
[3622.32 → 3624.16] So it can query the tree.
[3624.46 → 3626.50] It gets back the current node that you're in.
[3626.68 → 3632.28] It asks for, hey, what is the nearest function scope that I'm inside?
[3632.54 → 3633.66] So it's not a regex, right?
[3633.68 → 3637.28] It works for like inline functions inside another function, all these kinds of things.
[3637.46 → 3638.58] It asks for that.
[3638.66 → 3641.16] It gets what the return signature looks like.
[3641.32 → 3648.30] And then it generates the snippet in the corresponding things with the default values and then error.
[3648.30 → 3654.48] So it's very cool because I can just type like IE for if error, expand my snippet,
[3654.90 → 3659.88] and correspondingly the right signature is generated as a return value.
[3660.46 → 3665.24] These are the kinds of things that make me very, very excited about Tree Sitter.
[3665.94 → 3670.68] And why I say like it's cool to get better highlighting and like we look at our highlighting all day and that's very fun.
[3671.20 → 3675.16] But for both LSP and Tree Sitter, the things that I'm most excited about,
[3675.16 → 3684.02] like especially on Neovim core team, is we're trying to design interfaces that empower people to have much stronger sort of tools
[3684.02 → 3690.22] and understanding of the code that lets them extend their editors in sort of unique and interesting ways,
[3690.30 → 3694.10] which is like I think the snippets one is a fun example of being able to do that.
[3694.70 → 3695.16] Goodness gracious.
[3695.60 → 3696.76] That is really neat.
[3696.92 → 3700.58] We're getting tight here, but we've teased Telescope a few times.
[3700.90 → 3702.58] Let's hit the nail on the head.
[3702.86 → 3703.94] Tell everybody about your...
[3703.94 → 3704.48] You're into it.
[3704.68 → 3705.76] Ooh, there you go now.
[3705.76 → 3705.92] Yeah.
[3706.40 → 3707.54] That's why we pay you the big bucks.
[3707.98 → 3717.70] So Telescope is a fuzzy finder that I started, and I've had a lot of contributors to over the past year.
[3717.90 → 3720.80] I cannot thank enough the contributors to the project.
[3721.40 → 3727.74] In just over the last year, it's gotten over 3,000 stars and nearly 130 contributors.
[3727.74 → 3741.62] And I think that by itself is somewhat of a testament to how accessible Lua is, how interested people are to extend the editor and to like continue working on it and their ability to sort of pickup little pieces and do it.
[3741.62 → 3755.26] But in terms of like what Telescope is and why like I made it, I partially made it just to explore writing some stuff in Lua as a way to push our API and boundaries to find out what we should be including in Neovim core.
[3755.26 → 3762.90] But as I was working on it, some of the things that I've struggled with doing in the past with fuzzy finders, I just wanted to try and solve.
[3763.34 → 3765.38] For example, like I love FZF.
[3765.46 → 3766.52] It's a very awesome tool.
[3766.62 → 3768.12] I use it all the time on the CLI.
[3768.12 → 3783.30] But it's very difficult to do something like pass a function through FZF because you have to encode it in some way and then decode it again later because FZF processes standard in and standard out, right?
[3783.90 → 3789.98] So Telescope is all Lua from the top of the stack down or FFI, but that still counts.
[3789.98 → 3799.66] And so you can pass a function reference, which might be what you want to do if this item is selected at the beginning of your code.
[3799.78 → 3801.52] And then you can pass that all the way through.
[3801.62 → 3805.60] And so when you select it, you can do something with that item.
[3805.94 → 3813.62] So my main goal for making it was just to basically create like the most extensible fuzzy finder that I could imagine.
[3813.78 → 3816.52] So like every part of Telescope is configurable.
[3816.52 → 3820.74] So like the sorting algorithm is just an interface of a function.
[3820.92 → 3826.86] So you can have FLY sorting, FZF, strict matching, engram matching.
[3827.06 → 3831.84] You can write whatever you want to do, and you can just plug that in and that will just work with everything else.
[3832.00 → 3834.00] The previewers are all just Lua functions.
[3834.66 → 3840.80] So some of them, like if you're previewing buffers, it just literally opens the preview in a Neovim buffer.
[3840.80 → 3847.12] So you get exactly the same highlighting as you would if you open the file because it is literally you opening the file.
[3847.84 → 3853.64] The like ability to sort and how you're sorting those and when you filter them, those are all configurable.
[3853.80 → 3858.74] The display and UI and different themes, they're all like individually configurable.
[3858.74 → 3871.64] And what like my goal was, was to make the most configurable like fuzzy finder that I could do with an easy API to basically plug in whatever you can imagine that you wanted to sort on and then use it.
[3872.18 → 3877.72] So all my to-do list was to yank Nick's FZF Neovim setup and use it for myself.
[3877.84 → 3879.12] Should I just bypass that?
[3879.22 → 3880.50] Is Telescope ready for me?
[3880.68 → 3883.24] Should I just use it right away or is it still baking?
[3883.66 → 3883.88] Yeah.
[3883.88 → 3887.12] So there are a couple of things still baking for sure in Telescope.
[3887.28 → 3891.86] I mean, FZF is just like a rock solid piece of software that's super cool.
[3892.50 → 3898.80] If you're doing things that might be searching millions of files, for example, you should stick with FZF.
[3899.02 → 3904.04] Go is going to be a better solution for you than what I can do in Lua, at least today.
[3904.22 → 3904.52] We'll see.
[3904.62 → 3905.86] Maybe someday it'll be different.
[3905.86 → 3914.96] We are nearing completion of merging a very important PR that will greatly improve performance for really, really large searches.
[3915.32 → 3920.40] Like 500,000 items will still feel fast and not really block the editor.
[3921.08 → 3923.02] So it's up to you.
[3923.20 → 3928.76] I would say if your primary concern is speed, then you should probably stick with FZF at least for a while.
[3928.76 → 3936.04] Maybe you can talk to me again in a year, and maybe I feel I'm close enough to FZF speed to say that we're there.
[3936.16 → 3943.32] We're working on some projects like in C to compile as optional dependencies that you can throw in here and work superfast and cool.
[3943.80 → 3945.18] But we're not there yet.
[3945.26 → 3945.94] And that's cool.
[3946.12 → 3947.12] Like I said, I like FZF.
[3947.24 → 3948.54] But I use it every day.
[3948.64 → 3950.76] I no longer use FZF inside Neovim.
[3950.96 → 3955.26] I have lots of friends who no longer use it inside Neovim or other fuzzy finders.
[3955.32 → 3956.60] They just use Telescope.
[3956.60 → 3958.92] So I would say it's ready for daily use.
[3959.70 → 3968.72] But, you know, if you're going to be searching 10 million things or something like that, then running something inside the program that you're doing is probably not a good call.
[3968.82 → 3974.02] You should use an external executable that's going to manage that memory maybe a little bit tighter.
[3974.32 → 3975.06] I have an answer for you.
[3975.34 → 3975.82] Why not both?
[3975.90 → 3976.66] Why not both?
[3976.80 → 3976.98] Yeah.
[3977.50 → 3984.00] I have recommended that for some use cases for people, like if they're trying to grew every line in their very large mono repo,
[3984.00 → 3987.60] there's no reason not to keep FZF around, at least for a while.
[3988.26 → 3992.06] For me, like I have a hard time if the UI like isn't as consistent.
[3992.38 → 3996.28] It's just sometimes like, oh, I'll like notice that or like, oh, it's not the same as what I'm used to.
[3996.46 → 3996.48] Yeah.
[3996.62 → 3998.78] So for some people that really bothers them.
[3998.82 → 4000.52] And I understand that's totally cool.
[4000.52 → 4002.22] And they say they're going to stick with FZF.
[4002.26 → 4003.06] And I say, awesome.
[4003.54 → 4004.18] That's great.
[4004.18 → 4010.16] That is one thing that I think Telescope really has going for it is it just has a really beautiful UI.
[4010.38 → 4010.66] Thanks.
[4010.66 → 4012.82] That does help, doesn't it?
[4013.22 → 4013.40] Yeah.
[4013.48 → 4022.66] And I mean, it is very interesting when you actually start using it, and you notice that you get exactly the same colours as what the rest of your editor is.
[4022.74 → 4023.94] I don't have that with FZF.
[4024.28 → 4024.56] Yes.
[4024.56 → 4032.46] It is not possible as far as I understand, because like, for example, when you open up a buffer inside Neovim and if you have Tree Sitter,
[4032.64 → 4038.22] it will literally Tree Sitter highlight the same way with the same exact colours because it is just another buffer.
[4038.22 → 4043.06] It would be like if you did colon edit this file, it will show it like that in the preview.
[4043.38 → 4043.96] Very cool.
[4044.14 → 4051.72] So one thing I want to touch on maybe as a closer is I mentioned the enthusiasm around the 0.5 release.
[4051.82 → 4054.96] I mentioned how many people said win Neovim on the changelog.
[4055.46 → 4058.64] There's a lot of people very excited about this project.
[4059.16 → 4062.10] They love the ability to write plugins in Lua.
[4062.10 → 4066.60] They like the new capabilities that Tree Sitter is making available to them.
[4067.68 → 4069.32] Maybe speak to the community a little bit.
[4069.42 → 4071.52] I know you lead some live streams.
[4071.82 → 4073.78] There's a lot of like fun being had.
[4074.02 → 4077.18] There were celebrations around the big release.
[4077.60 → 4082.52] And then maybe give waypoints for people who would love to get involved with Neovim, the community.
[4082.72 → 4084.70] Like where do they gather, et cetera?
[4084.70 → 4091.66] Yeah, so we did a 0.5 release stream on Twitch on my live stream channel.
[4091.82 → 4096.98] And it was like the excitement and enthusiasm was really mind-blowing for me.
[4097.38 → 4099.42] You know, I've been working on Neovim for a long time.
[4099.82 → 4103.76] And sometimes you're sort of like just working, and you're pushing stuff to GitHub.
[4104.20 → 4105.70] And like, okay, cool.
[4105.78 → 4107.70] Like somebody's using it, I'm pretty sure.
[4107.70 → 4112.92] But we had like 500 people there live to do the like release drop on my stream.
[4113.00 → 4115.04] And it was like really crazy for me.
[4115.10 → 4116.78] And people were showing a lot of support.
[4116.94 → 4118.34] And so it's very exciting.
[4118.54 → 4121.58] Even, you know, just getting messages from people saying thanks.
[4121.82 → 4124.62] Just as a general note, if you're using open source software,
[4124.88 → 4129.80] and especially if it's maintained by people who aren't getting fang,
[4129.92 → 4132.20] but like salary to do the maintenance,
[4132.40 → 4135.08] it means a lot when you get a thank you or like,
[4135.08 → 4136.52] wow, I really like this.
[4136.88 → 4137.22] Do that.
[4137.22 → 4142.32] And I mean, I was really pleased to see Neovim in the top spot for most loved editor
[4142.32 → 4144.80] in Stack Overflow 2021 survey.
[4145.10 → 4146.06] A little shout out there.
[4146.98 → 4148.96] But yeah, I think the community is great.
[4149.02 → 4152.38] And it's really exciting to see how much people are excited.
[4152.60 → 4154.30] And I've really appreciated it.
[4154.30 → 4156.72] And it's been fun sort of being on the receiving end of that.
[4157.00 → 4160.26] In terms of like, where can people get started, and how can they help?
[4160.72 → 4164.62] First thing is we're on Element or Matrix, I guess.
[4164.72 → 4165.98] There's a Neovim chat room there.
[4165.98 → 4167.82] I believe it's linked from the README.
[4167.94 → 4170.06] If it's not, then it should be.
[4170.86 → 4174.64] And so you can go there, or it's on Gitter, or it's on IRC.
[4174.64 → 4177.42] They're all sort of like bridge to be the same place.
[4177.42 → 4179.74] And you can hang out there and chat or ask questions.
[4180.08 → 4183.40] There are a lot of issues that if you commented on and said,
[4183.50 → 4186.84] I want to work on this or like, how can I fix this?
[4186.84 → 4188.42] People are super glad to help.
[4188.86 → 4190.90] I actually, that's how I got involved.
[4191.12 → 4198.70] I did a PR in maybe during my senior year of college, adding a new thing to Status Line.
[4198.90 → 4206.34] And I just had like a ton of really nice people be there to help and to encourage me and give me advice.
[4206.34 → 4212.40] And they helped me grow a lot as software developer, even on just that one PR and taught me a lot of really great things.
[4212.40 → 4221.40] And I hope, and I think it's a goal of the other maintainers as well that we basically make a welcoming and happy place for people to learn a lot more.
[4221.56 → 4225.90] So don't be afraid to ask questions or to comment and say, I'd like to work on this.
[4225.96 → 4226.76] Where should I start?
[4227.26 → 4228.64] That's how I got started.
[4228.96 → 4231.02] And so I think that's a really great way to go.
[4231.02 → 4237.08] There are some labels like Good First Issue or Mentored Project or things like that you could look into.
[4237.54 → 4240.06] But don't be afraid to leave a comment or say hello.
[4240.36 → 4241.24] We're super happy to see you.
[4241.30 → 4243.96] Or just say, thanks for working on it.
[4244.00 → 4250.02] That always makes me feel better and gives me energy to keep on improving the other and working on it.
[4250.50 → 4250.54] Awesome.
[4250.66 → 4253.08] Well, we definitely appreciate all the work that you're doing.
[4253.20 → 4254.34] And I'll just echo your sentiment.
[4254.34 → 4259.98] If you have a piece of software that you use and love, find the people that make that software and let them know.
[4259.98 → 4263.04] So, especially if it's open source, but proprietary as well.
[4263.12 → 4267.04] There's people behind the scenes of proprietary software putting the work in.
[4267.22 → 4269.52] So that's definitely appreciated.
[4269.86 → 4272.76] Nick, I want to thank you for being my changelog co-pilot.
[4272.88 → 4275.76] Hopefully none of the things you generated today were GPL code.
[4276.54 → 4279.36] But happy to have you here with me.
[4280.32 → 4281.84] I think I broke the show with that one.
[4281.84 → 4284.40] TJ, we really appreciate you coming on the changelog.
[4284.48 → 4287.72] To everybody who requested this episode, we thank you as well.
[4287.72 → 4289.42] We do take requests.
[4289.68 → 4293.00] Head to our website, changelog.com slash request.
[4293.24 → 4294.10] Fill out the form there.
[4294.16 → 4294.68] Let us know.
[4295.28 → 4296.34] Guests you'd like to hear.
[4296.44 → 4297.46] Topics you'd like to hear.
[4297.68 → 4299.12] If you want Nick to come back.
[4299.18 → 4301.34] If you'd like us to banish him into eternity.
[4301.72 → 4302.38] Let us know.
[4302.54 → 4303.68] We'd like to hear from our audience.
[4304.46 → 4305.28] Any final words?
[4305.58 → 4306.14] TJ or Nick?
[4306.56 → 4307.54] Just thanks for having me.
[4307.72 → 4310.86] It's cool to see Neovim be requested on the show.
[4310.94 → 4312.72] And I'm always happy to talk about it.
[4312.72 → 4318.86] If you want to see more of me or hear my voice, I stream a lot on twitch.tv slash Teen.
[4318.86 → 4320.90] That's T-E-J underscore D-V.
[4321.16 → 4322.42] You can come hang out there.
[4322.64 → 4323.76] We're live pretty often.
[4323.88 → 4325.98] And I do a lot of Neovim related work there.
[4326.44 → 4330.40] Otherwise, just glad to be here and glad to be participating in such a fun community.
[4330.92 → 4331.04] Yeah.
[4331.26 → 4332.68] And thanks for having me on as well.
[4332.94 → 4338.28] And TJ, I would gladly take you up on that offer to dig into some custom LSP stuff.
[4338.36 → 4338.90] That's really cool.
[4339.10 → 4339.28] Cool.
[4339.28 → 4342.60] We are tentatively planning some related live streams.
[4342.76 → 4347.96] We have nothing locked in, but definitely follow TJ on Twitch and maybe on Twitter as
[4347.96 → 4349.00] well for announcements.
[4349.22 → 4350.52] Of course, follow Changelog on Twitter.
[4351.02 → 4354.54] You can also follow Nick Needed on Twitter, but I don't know.
[4355.10 → 4356.22] You decide if you want to do that.
[4356.72 → 4357.12] Thanks, Jared.
[4357.44 → 4357.76] All right.
[4357.78 → 4358.90] That's our show for this week.
[4359.00 → 4360.78] We'll talk to everybody next time.
[4363.18 → 4363.92] Sorry, Nick.
[4364.14 → 4367.26] In true JS Party fashion, I had to roast you a little bit just at the end.
[4367.84 → 4368.24] Absolutely.
[4369.28 → 4370.98] Got to love roasting Nick.
[4371.06 → 4372.32] That's it for this episode of the Changelog.
[4372.38 → 4373.60] Thank you so much for tuning in.
[4373.78 → 4377.68] Got a special show coming up soon with Corey Wilkerson on GitHub's transition to Code spaces,
[4378.08 → 4382.06] Adam Jacob on open source business models, Fauna DB with Evan Weaver.
[4382.34 → 4384.76] If you're not subscribed, now is a good time.
[4385.04 → 4388.52] Subscribe at ChangeLog.com, and everywhere you listen to podcasts.
[4388.52 → 4393.08] The Galaxy brand move is to get the master feed at ChangeLog.com slash master.
[4393.44 → 4395.70] Get all of our podcasts in a single feed.
[4395.84 → 4398.60] Special thanks to our partners, Linde, Vastly, and Launch Darkly.
[4398.60 → 4401.74] Also, thanks to Break master Cylinder for making all our awesome beats.
[4402.02 → 4403.20] That's it for this episode.
[4403.48 → 4404.26] We'll see you next time.
[4404.26 → 4408.36] Take care.
[4408.36 → 4409.20] Bye.
[4409.24 → 4409.86] Bye.
[4409.86 → 4410.20] Bye.
[4410.20 → 4411.30] Bye.
[4411.60 → 4412.36] Bye.
[4412.36 → 4412.86] Bye.
[4415.44 → 4416.44] Bye.
[4417.88 → 4418.96] Bye.
[4419.22 → 4419.36] Bye.
[4420.12 → 4422.60] Bye.
[4422.60 → 4422.96] Bye.
[4422.96 → 4423.56] Bye.
[4423.58 → 4424.32] Bye.
[4424.38 → 4425.00] Bye.
[4425.00 → 4425.28] Bye.
[4425.28 → 4425.30] Bye.
[4425.56 → 4426.20] Bye.
[4426.30 → 4427.16] Bye.
[4427.16 → 4427.68] Bye.
[4427.68 → 4427.82] Bye.
[4427.88 → 4428.08] Bye.
[4428.12 → 4428.92] Bye.
[4428.92 → 4429.02] Bye.
[4429.02 → 4429.44] Bye.
[4429.44 → 4429.86] Bye.
[4430.04 → 4430.06] Bye.
[4430.06 → 4430.22] Bye.
[4430.50 → 4430.52] Bye.
[4430.52 → 4430.96] Bye.
[4431.10 → 4431.26] Bye.
[4431.36 → 4431.66] Bye.
[4431.82 → 4432.10] Bye.
[4432.10 → 4432.52] Bye.
[4432.52 → 4439.52] Game on!
