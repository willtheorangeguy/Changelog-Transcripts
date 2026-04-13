[0.20 → 4.34] We are going to shift in 3, 2, 1.
[18.90 → 25.26] Welcome back to Change Login, friends, the weekly talk show dedicated to continuous improvement.
[25.26 → 30.80] Thanks to our partners for helping us bring you the best developer pods each and every week.
[30.98 → 34.56] Check them out at Fastly.com and Fly.io.
[35.06 → 36.40] Okay, let's talk.
[42.04 → 49.08] Well, we're here for Change Login, friends, and we have one of our oldest friends with us here to kick off this new talk show.
[49.20 → 51.30] It's Gerhard Lazy. What's up, man?
[51.66 → 52.64] It's good to be back.
[52.64 → 56.60] Look, everything's up. I was just telling Adam, everything that should be up is.
[56.76 → 57.34] Nothing is down.
[57.36 → 58.60] Don't ask Gerhard that question.
[58.76 → 60.04] Nothing is down, okay?
[60.38 → 61.12] Oh my gosh.
[62.14 → 63.92] It's all up from here.
[64.26 → 66.74] And of course, Adam's with us as well. What's up, Adam?
[66.90 → 68.50] What's up? Chasing the nines.
[68.86 → 69.92] Chasing the nines.
[70.30 → 71.24] How many can we fit?
[71.88 → 73.88] They get more expensive as you go, don't they?
[74.16 → 77.04] They do, yes. Orders of magnitude, each of them.
[77.12 → 77.50] That's right.
[77.50 → 81.04] What's our SLA and Los, Gerhard? We're chaining.
[82.70 → 83.44] I don't know.
[84.00 → 84.36] Okay.
[84.54 → 87.26] What do you want them to be? We'll make them whatever you want them to be.
[87.66 → 91.26] I want them to be just right. Not too much. Right? Not too little. Just right.
[91.38 → 91.52] Yeah.
[92.08 → 94.84] I think for ChangeLog.com, it's 100%.
[94.84 → 96.38] That's just right.
[96.46 → 98.32] It's going to be a billion dollars, please.
[99.76 → 102.70] Because they didn't go down. Like ChangeLog.com did not go down.
[102.98 → 103.44] That's true.
[103.44 → 105.36] And that's Vastly. Thank you.
[105.98 → 106.86] Yep, that's Vastly.
[107.22 → 110.46] Speaking of being an old friend, how long have we known you, Gerhard?
[112.86 → 113.18] 2016?
[114.96 → 115.30] Yes.
[115.46 → 118.02] 15? Something. 16, I think.
[118.24 → 121.46] So 16 is when you started working on the code base.
[121.54 → 123.16] In fact, I've been creating this.
[123.20 → 125.16] I haven't got it finished yet because it hasn't turned out very well.
[125.46 → 128.94] But I'm creating this visualization with this tool I found called FORCE.
[129.00 → 132.24] I don't know if that's how you say it, but it's G-O-U-R-C-E, like source.
[132.24 → 138.82] And it goes through your version control and the whole history, and it creates a visualization of people working on the code.
[139.76 → 145.40] And I did one across the eight years of our code base, and it was like 45 minutes long.
[145.48 → 147.12] So it's too like, who's going to watch 45 minutes?
[147.18 → 148.78] And I started fuzzing with it, trying to make it better.
[148.78 → 153.76] Anyway, long story short, I know exactly when you started contributing, because it was the summer of 2016.
[154.08 → 158.08] I remember your little avatar coming in on this visualization and touching all the files.
[158.46 → 161.06] But I knew you before that, briefly at least.
[161.26 → 162.52] Or I knew of you before that.
[162.90 → 167.22] I think you wrote a blog post for us about Ansible prior.
[167.94 → 170.30] And I think we've told the story before on Kaiden's past.
[170.30 → 172.42] But what is that?
[172.74 → 173.70] Four plus three?
[173.88 → 174.56] Seven years?
[175.12 → 175.60] That's it.
[175.82 → 176.58] That's a long time.
[177.00 → 179.12] I think we started talking in 2015.
[179.32 → 182.02] I think it was December or something around that time.
[182.24 → 186.04] And then it took us a couple of months, right, to figure out how and why.
[186.70 → 188.30] The why was important for me.
[188.48 → 189.74] And I'm glad that we got that right.
[189.84 → 190.92] Remember the 10 questions?
[191.18 → 192.12] I mean, I still have the email.
[192.24 → 192.86] We can dig it up.
[193.12 → 194.02] I think we've done this.
[194.14 → 195.08] I think we've done this before.
[195.08 → 195.48] We have.
[195.56 → 198.84] That's why I said we've told this story before on Ship It on a previous Kaiden.
[198.94 → 199.60] So here we are now.
[199.72 → 200.74] We're on Changelog and Friends.
[201.16 → 202.16] But we're still Wizening.
[202.22 → 204.28] There was a big question on Ship It 90.
[204.40 → 205.62] Where would we Kaiden next?
[205.88 → 208.36] And this is where we decided to put our Kaiden episodes, of course.
[208.48 → 209.58] It's also on the Changelog.
[209.64 → 210.40] This is our new show.
[210.48 → 211.48] It's also our old show.
[211.84 → 213.92] But it's just a different flavour of the Changelog.
[213.94 → 215.84] We're happy to have you here, Gerhard.
[215.96 → 219.28] We can maybe throw this on the Ship It feed for those folks if we want to.
[219.28 → 221.28] But we can talk about that perhaps offline.
[221.38 → 223.34] Maybe you'll be mad because it'll be like episode 91.
[223.34 → 225.50] And it'll ruin your flow.
[225.74 → 226.32] That's okay.
[226.52 → 227.66] I wanted fewer episodes.
[228.12 → 229.66] So I think this is okay.
[229.90 → 230.12] Okay.
[231.16 → 231.88] Why not?
[232.32 → 234.16] They're happening, but just less frequently now.
[234.50 → 239.32] Well, for those people who listen to the Changelog, and we haven't Wizened on the Changelog,
[239.66 → 242.86] except for maybe a cross post years ago when we first started Ship It,
[243.04 → 246.72] Gerhard, why don't you give the conceit of what Kaiden is and then what we do on these episodes?
[246.72 → 251.48] So Kaiden stands for continuous change for the better.
[252.14 → 257.28] And it has a strong association with Agile.
[257.62 → 260.68] And I know that somehow has fallen out of favour with industry.
[260.82 → 266.30] I'm not sure why exactly, but I've seen that there are a lot of anti-Agile feelings out there.
[267.00 → 268.26] Maybe people have been doing it wrong.
[268.40 → 268.82] I don't know.
[268.94 → 269.62] That's my joke.
[269.94 → 270.26] Okay.
[270.34 → 271.12] That's possible.
[271.72 → 272.62] You're holding it wrong.
[272.62 → 273.06] Yeah.
[273.26 → 279.16] And one of the principles in Agile is to keep small improvements,
[279.46 → 284.32] keep iterating, and keep continuously delivering those small improvements.
[285.02 → 292.64] So for us, what that meant was that on a cadence, for us, it was every 10 Ship It episodes.
[292.86 → 294.96] That was roughly every two and a half months.
[295.24 → 299.64] We would talk about the improvements that we're doing for Changelog.
[299.90 → 302.06] So we don't have a release as such.
[302.06 → 303.42] There is no SemVer.
[303.82 → 305.54] There's no work continuously releasing.
[306.20 → 312.90] But what we do is we talk about all those improvements that we have shipped in that time frame,
[313.14 → 317.30] whatever it is, on Ship If it was, and now on Changelog.
[317.68 → 317.76] Yeah.
[317.90 → 323.74] So this idea of continuously improving something and then pausing and taking stock of what we've improved,
[323.88 → 327.86] it's almost like a retro for those, again, that have done Agile the right way,
[328.20 → 329.22] or even the wrong way.
[329.26 → 330.34] You can do retros the wrong way.
[330.34 → 337.24] Anyway, it was one of my favourite meetings because it brought everyone together, and we would get so much better for it.
[337.72 → 345.60] But this idea of continuously improving, if you just keep focusing on that and always be better today than you were yesterday,
[345.60 → 347.08] that's all you have to care about.
[347.08 → 348.96] It doesn't matter how big or how small it is.
[349.14 → 349.72] They compound.
[350.12 → 350.98] That's the beauty of it.
[351.04 → 352.74] All those improvements compound over time.
[353.40 → 354.56] So keep improving.
[354.86 → 355.02] Yeah.
[355.08 → 356.04] One of my mottos.
[356.04 → 361.12] So we're obviously fans of this process, and we're putting our money where our mouth is, so to speak,
[361.28 → 367.30] because we're not just talking about our improvements, but we're committing to Wizening every so often.
[367.42 → 372.38] Our new cadence, we're going to try, is going to be every other month here on Changelog and Friends.
[373.04 → 377.00] We were doing it once every 10 episodes, like Earhart said, which was roughly two and a half months.
[377.00 → 380.50] Now we've been a bit on hiatus because we've lost our groove.
[380.62 → 381.74] We've got our groove back now.
[382.24 → 386.04] So it's been longer than a typical Kaiden time period.
[386.18 → 388.78] It doesn't necessarily mean I accomplished more than I normally do.
[388.92 → 389.82] I think we did, actually.
[389.90 → 390.76] I think you did.
[390.90 → 392.38] Yeah, I think you did for sure.
[392.38 → 392.64] Yeah.
[392.76 → 398.00] So let's start hitting through some of the stuff we've been working on in and around Changelog.com.
[398.10 → 404.74] So for those first coming to Kaiden, Changelog.com is our open source podcasting platform.
[404.90 → 406.34] It's written in Elixir and Phoenix.
[406.34 → 409.62] It's deployed to Fly with Vastly in front of it.
[409.74 → 415.26] It has a Postgres backend and a pretty cool, I don't know, deployment infrastructure.
[415.40 → 415.82] What do you call it?
[415.82 → 416.36] A pipeline?
[416.58 → 417.62] I would say infrastructure.
[418.14 → 419.58] I think all of it, it's infrastructure.
[419.78 → 424.48] The way it's structured, the way we talk about it, the way we capture it, even in documentation,
[424.60 → 426.16] the way it's documented, I think it's really cool.
[426.36 → 426.52] Yeah.
[426.56 → 427.50] And so we're doing this.
[427.62 → 434.58] We've been coding on this, like I said, since 2016 for many years, kind of in fits and starts.
[434.58 → 436.40] We go heavy, sometimes we go light.
[436.64 → 438.36] We continuously improve it.
[438.50 → 439.42] And we also experiment.
[439.68 → 443.56] So one of the reasons we have this platform is so that we can try new services, try new
[443.56 → 448.30] techniques, hit ourselves on the thumb with a hammer and tell you all about it.
[448.34 → 451.74] So you can avoid said hammer or give it a try if you like.
[451.74 → 454.14] And so that's kind of one of the ideas behind this.
[454.26 → 461.36] It's not merely to make changelog.com a better website or make the distribution of our podcasts
[461.36 → 463.70] better, although that's definitely a huge part of it.
[463.76 → 468.06] It's also for learning, experimentation, and hacking because we're hackers.
[468.44 → 470.52] And it's nice to have something to hack on together.
[471.04 → 472.18] I think that's very rare, right?
[472.18 → 477.68] Being able to do this in the open source, in the spirit that it was intended to have the
[477.68 → 478.26] time, right?
[478.26 → 482.58] We are very busy during our day and during our work week.
[482.76 → 486.40] And then the weekend comes and there's like all sorts of pressure on your time.
[486.62 → 491.12] Being able to just give yourself permission to try things just for the fun of it.
[491.46 → 497.76] It's so easy to just get down, you know, ruts or delivering of a backlog or whatever.
[498.06 → 499.80] There's never time to try things out.
[499.86 → 505.66] So this is, again, us giving ourselves permission to do fun things, talk about them, but also keep
[505.66 → 509.12] improving the platform, the whole change of a platform in an open way.
[509.74 → 510.68] My favourite approach.
[511.34 → 511.42] Yeah.
[511.42 → 512.68] So many tools I come across.
[512.78 → 518.66] I don't have a good enough excuse to try them because at a certain point in your life, it's
[518.66 → 521.10] just opportunity costs left and right.
[521.40 → 524.68] And it's like, if I try this thing, I can't do that other thing on my list of things to
[524.68 → 524.88] do.
[525.00 → 527.28] And so we almost need an excuse to tinker.
[527.78 → 532.24] And this has been, for me at least, in certain ways, one of my excuses where I can feel like
[532.24 → 538.10] I'm also pushing the ball forward while I do something versus merely fuzzing around with
[538.10 → 541.40] my Git configure, my Vim RC, right?
[541.72 → 541.98] Gosh, Jared.
[544.56 → 545.92] The old Vim RC.
[546.46 → 547.74] Signed commits, finally, I see.
[548.30 → 550.96] I think since the last time we Kaiden, do you have signed commits now, Jared?
[551.18 → 552.96] I did do something with that.
[553.18 → 553.80] We succeeded.
[553.80 → 560.08] I still see that there's, when we merge some stuff, there's still that PRs that come in.
[560.16 → 561.90] There's still like a what do you call it?
[561.90 → 565.44] A DCO thing that's like failing because the sign-offs aren't correct.
[565.54 → 568.00] And maybe it's because I rebased via the web interface.
[568.52 → 569.08] I don't know.
[569.16 → 572.36] I've had some problems where I'm like, why can't we just do it the old easy way?
[572.48 → 574.46] Why are you going to have all this security and stuff?
[574.54 → 577.26] But I'm, you know, you're dragging me along, kicking and screaming.
[577.26 → 583.78] All right, let's get into some of the major changes since our last time talking about this.
[583.96 → 592.50] The biggest one, it seems like, was the upgrade of Dagger and the switch from Q, C-U-E,
[592.94 → 597.20] the configuration language for configuring our pipelines to Go.
[597.84 → 602.88] And I think we had that last time, but now we're actually using it for more stuff.
[602.88 → 607.10] So obviously, you can tell by the way I'm talking about it that Gerhard should be talking about it,
[607.10 → 607.42] not me.
[607.52 → 607.96] So go ahead.
[608.38 → 611.44] So in the last Kaiden, let me go back to the beginning.
[611.70 → 614.54] I think it was November 2021.
[615.16 → 616.18] That's when the story started.
[616.26 → 617.02] This experiment started.
[617.14 → 617.86] It was a long, long one.
[618.48 → 623.20] And the idea was, why are we using YAML for all these pipelines?
[624.02 → 627.76] And at the time we were using CircleCI, I wanted to migrate to GitHub Actions.
[628.00 → 629.98] We're just trading one YAML for another.
[630.64 → 637.78] So I came across this tool called Dagger, which was, the whole idea was like you write Q,
[638.18 → 640.80] you don't write YAML, and you can run your pipeline locally.
[641.26 → 645.84] And what that means is that you can run the same pipeline written in Q, whether it's locally
[645.84 → 649.56] on your laptop, whether it's in GitHub Action, CircleCI, it doesn't matter where you run it,
[649.58 → 651.32] it will always run the same way.
[651.56 → 654.88] It has a container runtime, so all operations run in various containers.
[654.88 → 657.28] You have the caching, you have a lot of nice things.
[658.16 → 660.60] That was, again, November, was 0.1.
[661.12 → 663.06] We're very courageous, but it worked well.
[663.20 → 664.06] And it was a good improvement.
[664.24 → 665.58] We talked about it plenty.
[665.78 → 666.66] We wrote about it.
[667.12 → 667.74] Where do we write?
[667.92 → 669.08] It's all pull requests.
[669.42 → 672.64] If you go to our GitHub repo, there's the changelog.com.
[673.20 → 678.06] Even the topics that we're discussing today, there's a discussion, 452, where you can go
[678.06 → 679.74] and see all the various topics.
[679.98 → 684.80] And this is the first one, Migrate Dagger 0.1 to Dagger Go SDK 0.5.
[685.54 → 692.34] And what that meant is that there was a big shift in Dagger from people that liked Q to
[692.34 → 693.94] people that wanted to do more.
[694.06 → 694.84] They wanted to do Go.
[694.94 → 695.74] They wanted to do Python.
[695.96 → 699.76] Why should you write your pipeline in any one language?
[700.00 → 701.76] Why can't it be the language that you love?
[702.14 → 703.70] And for me, it was Go.
[704.22 → 705.48] We didn't have Elixir at the time.
[705.56 → 706.44] By the way, that's changing.
[706.82 → 707.82] We can talk about it later.
[707.82 → 708.32] Oh, yeah.
[708.38 → 709.36] You're getting Elixir support?
[709.54 → 713.22] By the way, you came across Dagger, but then you also went and got a job at Dagger.
[713.56 → 714.12] That's right.
[714.12 → 715.88] When you say we, people might be confused.
[716.06 → 720.26] When you say we, you're talking about you and your cohorts at Dagger, right?
[720.36 → 721.40] Yes, exactly.
[721.58 → 723.96] There's like we, these different things depending on context.
[724.08 → 725.38] But yes, I joined Dagger as well.
[725.54 → 725.64] Yeah.
[725.74 → 729.20] I really liked it beyond just the tool.
[729.42 → 734.90] You can tell I'm really passionate about deployment, about pipelines, about CCD, all that space.
[734.90 → 737.14] That's the space where Dagger sits.
[738.16 → 740.66] And remember how we met Jared?
[740.84 → 741.16] Deliver?
[741.16 → 742.00] I do.
[742.00 → 742.02] I do.
[742.26 → 742.66] E-deliver.
[742.74 → 743.58] Deliver and E-deliver.
[743.78 → 744.20] Exactly.
[744.44 → 749.00] E-deliver was a fork of Deliver, the Bash framework for deployment that I wrote.
[749.34 → 750.20] So there you go.
[750.24 → 751.26] Ten years later, boom.
[751.48 → 752.22] Dagger came along.
[752.78 → 754.10] And the rest was history.
[754.44 → 754.76] All right.
[754.76 → 761.00] So 0.5, which actually 0.3, Dagger 0.3, it introduced these SDKs.
[761.02 → 765.12] You can write Go, your pipeline in Go, your pipeline in Python or Node.js.
[765.46 → 765.96] We pick Go.
[766.32 → 767.60] And we transition.
[767.76 → 773.74] We migrated from having our pipeline declared in queue to a programming language, which has,
[773.92 → 775.60] again, a lot of nice things, right?
[775.62 → 778.22] When you have a programming language, you have very nice emulating.
[778.30 → 779.10] You have nice loops.
[779.18 → 782.86] You have functions or, you know, whatever you may have, right?
[782.86 → 785.60] Can't you loop and do other crazy stuff in YAML, too?
[785.74 → 789.44] You can, but it gets very, very messy if you do that.
[789.66 → 790.32] Very messy.
[790.70 → 790.80] Yeah.
[790.86 → 795.14] And to be honest, like, why not use your language as much as you can?
[795.18 → 796.74] And again, we didn't have Elixir at the time.
[796.80 → 797.60] That's slowly changing.
[798.08 → 800.34] But I prefer to write my pipeline in Go.
[800.62 → 803.68] So the first thing which we did, we migrated 0.1.
[803.76 → 805.02] We were running it in the new one.
[805.46 → 810.00] So I think the last Kaiden, when we talked about it, it was just a straight import, right?
[810.00 → 812.90] Like wrapping the previous version in the new version.
[813.34 → 815.38] A nice gradual improvement.
[816.04 → 818.60] Now, all of that has been rewritten in Go.
[818.92 → 822.00] We're using Mage locally to run the pipeline.
[823.08 → 824.28] So many things happened.
[824.38 → 826.10] Again, this was two and a half months ago.
[826.66 → 828.58] Now, I want to show you something really cool.
[828.70 → 829.80] I'm going to share my screen.
[829.94 → 830.88] I'm going to go a bit.
[831.42 → 832.10] Do you see that?
[832.56 → 835.72] This is a pull request that has not been submitted yet.
[835.72 → 840.16] And this is Dagger Engine on Fly Apps Version 2.
[840.50 → 842.08] It's exactly what it says.
[842.52 → 848.60] We're experimenting with Fly Apps Version 2, which is the latest implementation of apps in Fly.
[848.84 → 850.14] We're running Dagger on it.
[850.52 → 855.26] I'm connected here, experimental Dagger Runner host, via WireGuard Tunnel.
[855.58 → 857.66] And I'm running Dagger Run, the CLI.
[857.78 → 859.50] And I'm wrapping Mage CI.
[860.00 → 862.00] If your mind is blown, that's okay.
[862.22 → 863.44] I think you need to watch this video.
[863.44 → 869.92] So you're running Mage inside Dagger, inside Fly on their V2 platform, or locally.
[870.36 → 873.38] I'm wrapping Mage in Dagger Run.
[873.86 → 878.94] Dagger Run is just a command that's a CLI that connects my local command to a remote engine.
[879.42 → 882.22] It gives me this very nice view, which is my pipeline.
[882.58 → 889.20] I'm showing my Dagger pipeline that is running in this Dagger Engine on Fly Apps V2
[889.20 → 891.94] that I'm connecting to via WireGuard Tunnel.
[891.94 → 892.30] Okay.
[892.30 → 896.42] So what we can see here is we have three pipelines in one.
[897.00 → 899.92] And this is something that starts becoming even crazier.
[900.22 → 902.18] So we are building the runtime image.
[902.54 → 906.14] We are building the production image, which, by the way, makes use of the runtime image.
[906.42 → 909.82] And down here, we are also running tests, mixed tests.
[910.22 → 912.84] But because nothing changed, everything is cached.
[912.90 → 914.34] It completes in seven seconds.
[914.34 → 918.18] So let me go into application EX very quickly.
[918.72 → 920.42] And let me do a Foo2, just a comment.
[920.72 → 921.06] Foo2.
[921.42 → 921.64] Okay.
[922.02 → 923.76] And I'm going to run the same pipeline again.
[924.12 → 927.40] So now what's going to happen, it will detect the code change.
[927.80 → 935.20] And now it has to resolve the dependencies, compile the app, run the tests, compile the assets.
[935.20 → 941.24] And all this, we have a very nice UI that shows us the different pipelines, how they run and how they combine.
[941.48 → 942.60] I'm really excited about this.
[942.68 → 943.40] I don't know about you.
[943.94 → 946.42] Maybe you're still trying to process what you're seeing.
[946.42 → 948.46] Well, I'm still watching it stream by.
[949.06 → 953.80] And obviously, our listener here is imagining this in their mind, in their mind's eye.
[954.32 → 955.22] But it does seem very nice.
[955.30 → 956.84] I like the fact that it's going to cache everything.
[956.98 → 960.20] So let's say I just update an image in my assets' folder.
[960.34 → 961.66] I don't touch any Elixir code.
[961.78 → 962.88] And I deploy that out.
[962.98 → 966.76] And with this new code, it's going to run just the mix Phoenix digest command.
[966.88 → 968.38] It's not going to run compile and stuff.
[968.50 → 969.22] Not currently.
[969.78 → 972.08] Ah, see, I went to the logical conclusion.
[972.08 → 973.16] That's the next improvement.
[973.30 → 973.48] Okay.
[973.62 → 974.56] That's the next improvement.
[974.72 → 975.44] You beat me to it.
[975.44 → 976.92] Okay, so I'm almost excited.
[977.04 → 978.08] You'll have me excited later.
[978.14 → 979.12] Almost excited, yes.
[979.26 → 979.88] Oh, gosh.
[980.14 → 980.80] This is still good.
[980.92 → 984.78] Now, if you're going to run this from start, by the way, it should finish right now.
[984.86 → 986.28] It will finish in a minute and a half.
[986.40 → 987.10] Start to finish.
[987.24 → 988.38] Start to finish a minute and a half.
[988.40 → 988.98] With no cache.
[989.30 → 990.52] Well, you do have a cache.
[990.66 → 990.94] Okay.
[990.96 → 995.74] If you try to compile all the dependencies from scratch locally, it will take you about six to seven minutes.
[995.80 → 996.06] Okay.
[996.40 → 998.10] To get the dependencies, compile the dependencies.
[998.30 → 1000.16] Remember, you have to do it for both test and prod.
[1000.52 → 1002.42] You have to digest the assets, build the image.
[1002.48 → 1004.12] There's like a lot of stuff happening behind the scenes.
[1004.12 → 1011.44] The next improvement would be to split the static assets from the dependencies from the actual application.
[1012.08 → 1012.18] Right?
[1012.24 → 1014.12] So now all of a sudden you have like three inputs.
[1014.44 → 1014.52] Right.
[1014.62 → 1021.46] Right now we have just the application and the application means the dependencies, the static assets, and the application code.
[1021.46 → 1027.64] So it's all seen as one, which is why it would run everything if something changes in any of those files.
[1028.08 → 1029.48] One minute and 39 seconds.
[1030.00 → 1030.14] Right?
[1030.18 → 1031.26] And just recompiled everything.
[1031.62 → 1034.64] And by the way, this would also rebuild the image if it needs to.
[1034.74 → 1035.82] Let's say we bumped Erlang.
[1036.18 → 1037.28] Part of the same pipeline.
[1037.44 → 1039.12] It would rebuild at runtime.
[1039.46 → 1040.50] It would publish the runtime.
[1040.50 → 1042.84] All of that would happen automatically.
[1043.76 → 1044.92] And that's why I don't have to worry.
[1044.98 → 1047.66] There's like a couple of good pull requests worth checking out.
[1047.76 → 1049.12] The first one is 454.
[1049.38 → 1051.84] If you go in our repo, you can see that whole migration.
[1052.06 → 1053.20] We removed the last make file.
[1053.28 → 1053.84] We introduced mace.
[1053.86 → 1054.86] That's a fairly big one.
[1055.18 → 1056.48] There's a lot of refactoring there.
[1056.88 → 1063.16] There's another one, 464, where we are reading the versions for all the different dependencies,
[1063.16 → 1067.80] the runtime dependencies, Erlang, Elixir, Node.js, from tool versions.
[1068.46 → 1070.36] And that's an ASD configuration file.
[1070.96 → 1076.08] ASD is, I think I need to refer to the page manage.
[1076.60 → 1080.30] So ASD manage multiple runtime versions with a single CLI tool.
[1080.50 → 1080.58] Yeah.
[1080.76 → 1083.80] You could use brew to install Elixir, but then which version are you installing?
[1084.10 → 1086.44] It doesn't do versioning very well, right?
[1086.44 → 1086.54] Yeah.
[1086.54 → 1093.02] Having multiple copies or multiple versions of a binary of a language runtime on your machine
[1093.02 → 1096.42] and being able to switch between them is not easy with homebrew.
[1096.72 → 1098.74] I think it's maybe possible with homebrew, but not easy.
[1099.20 → 1100.00] Or maybe not possible.
[1100.28 → 1100.42] Yeah.
[1100.46 → 1101.20] I'm not sure which one.
[1101.70 → 1104.02] But with ASD, it's built specifically for this purpose.
[1104.20 → 1109.88] So this goes way back to the days of RBNV.
[1110.10 → 1112.06] And what was the big Ruby one?
[1112.14 → 1113.50] Because we had to do this in the Ruby world.
[1114.04 → 1114.46] RVM.
[1114.98 → 1116.36] RVM, Ruby Version Manager.
[1116.36 → 1119.04] And then there was NBM, Node Version Manager.
[1119.60 → 1122.20] And then there's probably EVM, maybe not.
[1122.28 → 1123.10] Elixir Version Manager.
[1123.32 → 1127.68] And so each little ecosystem, each language had their own version manager.
[1127.90 → 1133.44] And then ASD folks came along and said, hey, let's build one that can handle all these distinct
[1133.44 → 1135.84] things with one API, one CLI.
[1136.44 → 1137.38] And it's a really nice tool.
[1137.50 → 1138.68] I mean, I've been using it for years.
[1139.68 → 1143.92] And excited to see this getting further into what we're doing.
[1144.06 → 1144.54] So keep going.
[1144.54 → 1149.04] This also solves the one string to rule them all in terms of versioning too, right?
[1149.10 → 1153.46] Like we had an issue where there were multiple versions of Elixir in the code base.
[1153.50 → 1154.90] And this is like one now.
[1155.06 → 1155.44] Only one.
[1155.56 → 1155.70] Right.
[1155.92 → 1156.18] Yes.
[1156.54 → 1157.46] If you're using it.
[1157.52 → 1163.00] So if you follow the updates of the contributing guide, you can see how to use ASD to install
[1163.00 → 1163.52] all the things.
[1163.60 → 1165.00] Now we are versioning tool versions.
[1165.24 → 1167.64] We capture everything, including Mage, for example.
[1168.04 → 1171.64] Now you wouldn't want to use Mage other than if you want to run the pipeline locally.
[1171.64 → 1173.70] There's also PostgreSQL, right?
[1173.76 → 1176.42] So PostgreSQL is also versioned using this.
[1176.54 → 1179.18] If, for example, you're on Linux, there's like a couple of extra things that you need
[1179.18 → 1181.98] to do because maybe you don't have some system dependencies on macOS.
[1182.14 → 1182.66] It just works.
[1183.10 → 1188.40] So we are capturing every single dependency in this file, every single dependency version,
[1188.64 → 1189.68] like down to the patch.
[1189.96 → 1193.18] So for example, with Brew, because you mentioned Brew, Jared, you're right.
[1193.38 → 1196.62] There is a certain flexibility in terms of which version you can run.
[1196.70 → 1196.98] Right.
[1197.10 → 1197.86] To the minor.
[1198.48 → 1199.34] Some have major.
[1199.34 → 1202.86] So for example, PostgreSQL 14 or PostgreSQL 13.
[1203.00 → 1204.60] I think 13 is still available there.
[1205.10 → 1209.54] What you can't do, you can't say 14.1 or 14.8.
[1209.62 → 1214.26] Then there may be differences that you don't realize between your local development version
[1214.26 → 1214.98] that you're running.
[1215.08 → 1215.74] Everything looks fine.
[1215.78 → 1216.54] You push the production.
[1217.20 → 1217.58] Guess what?
[1217.68 → 1218.88] Things start breaking subtly.
[1218.96 → 1219.50] You don't know why.
[1219.60 → 1224.56] Well, we had one of those a long time ago where it was actually the Erlang patch version
[1224.56 → 1225.32] that was different.
[1225.32 → 1231.86] Not even the minor or major version, it's the patch, which had this bug in the TLS library
[1231.86 → 1235.34] or something that didn't exist on my local, but only existed in production.
[1235.52 → 1237.56] We ended up having to debug that sucker.
[1237.98 → 1238.24] Exactly.
[1238.50 → 1241.02] So ASD to manage all our dependencies locally.
[1241.22 → 1242.54] And you just need ASD, right?
[1242.60 → 1242.96] That's it.
[1243.08 → 1248.06] Like, I know there's like certain tools which use Nix, but then I forget the name.
[1248.30 → 1249.72] We mentioned it on changelog.
[1249.72 → 1254.18] But if you have that, then you have to use the Nix package manager, and you have to install
[1254.18 → 1254.48] that.
[1254.80 → 1255.94] And I ran it for a while.
[1256.06 → 1259.14] But to be honest, you really want the Nix OS to get the best experience.
[1259.38 → 1261.40] But then you're running Mac.
[1261.62 → 1262.90] You can get the Nix package manager.
[1263.20 → 1265.22] Some things will be a bit weird, especially when you restart.
[1265.32 → 1266.30] At least that was my experience.
[1266.94 → 1270.24] So ASD is a fairly lightweight for what it is and what it does.
[1270.46 → 1275.68] And we are reusing the tools versions file for our pipeline.
[1275.68 → 1281.44] We're reading this file in our pipeline and that determines what version of Erlang we're
[1281.44 → 1287.64] using to compile in the image that we're using for tests, for example, and as well as building
[1287.64 → 1288.40] the final image.
[1288.72 → 1292.56] What version of PostgreSQL we are running in production and so on and so forth.
[1292.90 → 1293.00] Right.
[1293.10 → 1295.64] So is this, it's .tool-versions.
[1295.84 → 1297.26] It's a hidden file, tool-versions.
[1297.52 → 1299.86] Is this an ASD creation?
[1300.34 → 1300.60] Yes.
[1300.88 → 1301.36] It is.
[1301.56 → 1301.84] Okay.
[1302.26 → 1305.44] And what is the syntax, or what is the format of this?
[1305.44 → 1307.06] It looks like it's just like plain text.
[1307.36 → 1308.30] Do they have a spec?
[1308.40 → 1310.10] Like here's how it works or is it just simple enough?
[1310.16 → 1310.68] They don't need it.
[1310.94 → 1311.84] It's very simple.
[1312.20 → 1314.08] It has like multiple lines.
[1314.38 → 1319.92] On each line, you have the name of the dependency space, the version of that dependency.
[1320.24 → 1325.28] So you have Erlang space 25.3.2.
[1325.60 → 1326.30] New line.
[1326.78 → 1331.26] Elixir space 1.14.4 and so on and so forth.
[1331.84 → 1333.52] Too simple to even write the spec down.
[1333.52 → 1335.64] Just look at it, and you can see how it works.
[1335.64 → 1336.44] I know, right?
[1337.38 → 1338.84] I do like simple tools.
[1339.12 → 1346.62] So as a homebrew user and an ASD user, I sometimes have to ask myself the question of like, what do I install this with?
[1346.62 → 1347.22] Mm-hmm.
[1347.22 → 1365.10] And my go-to logic is like, well, if I could ever imagine myself having to have two different versions on my machine at the same time, for instance, I have this project over here requiring Ruby 2.3.7 and then this project requiring Ruby 3.2.3, and I don't want to deal with switching.
[1365.10 → 1366.84] Then I go with ASD.
[1367.46 → 1371.44] Because of that, I'm a homebrew install PostgreSQL guy.
[1371.64 → 1373.86] And now we have it inside ASD.
[1374.16 → 1376.46] And so do I need to uninstall and install with ASD?
[1376.96 → 1377.18] I don't know.
[1377.26 → 1378.10] Does that screw things up for me?
[1378.26 → 1379.62] It doesn't screw things for you.
[1379.78 → 1379.92] No.
[1380.18 → 1381.74] It will keep things as they are.
[1382.36 → 1387.78] You can, for example, it won't prevent you from running a PostgreSQL that you've installed via homebrew.
[1388.12 → 1389.72] So there's like no such guard in place.
[1389.72 → 1392.78] Because it's all containerized or at least isolated.
[1393.16 → 1395.86] If you're using ASD, it doesn't use containers.
[1396.72 → 1401.24] When you run the pipeline locally, basically it will ignore whatever you have running locally.
[1401.60 → 1405.76] It will read the versions from this ASD generated file, which is tools versions.
[1406.22 → 1409.94] And those are the versions that it will use for the pipeline, both locally and remotely.
[1410.48 → 1415.58] Now, if you, for example, want to switch to PostgreSQL, the same version that we're running in production,
[1415.74 → 1418.78] the same version that we're testing with in our CI-CD system,
[1418.78 → 1423.24] what you want is obviously to do the ASD integration.
[1423.66 → 1429.24] Usually when you integrate ASD with your shell, that will prepend the ASD path.
[1429.34 → 1429.56] Right.
[1429.82 → 1436.66] Which means that the PostgreSQL from ASD will have precedence over the PostgreSQL from homebrew.
[1436.96 → 1437.26] Gotcha.
[1437.64 → 1438.88] Same is true for Erlang, Elixir.
[1438.98 → 1440.88] So you can have Erlang installed via homebrew.
[1441.14 → 1444.18] But as soon as you're in ASD and you have it nicely integrated with your shell,
[1444.58 → 1448.74] then automatically anything that you have installed with ASD, that's what you'll be using.
[1448.78 → 1450.68] In that specific directory.
[1451.14 → 1451.26] Gotcha.
[1451.66 → 1455.04] So the pipeline, though, it does use containers, correct?
[1455.66 → 1455.96] Yes.
[1456.46 → 1459.18] Everything, all the operations actually run in containers.
[1459.74 → 1462.76] Imagine all the commands that you have in Docker files, right?
[1462.78 → 1463.94] You have like those one lines.
[1464.36 → 1467.76] Now imagine if you could write those one lines in code.
[1468.08 → 1469.50] In our case, it's actually Go.
[1469.84 → 1472.72] We capture the equivalent of those lines.
[1472.82 → 1474.16] There's their operations, basically.
[1474.16 → 1477.32] We're capturing the equivalent of those operations in Go code.
[1477.52 → 1479.96] They get submitted to the Dagger engine.
[1480.54 → 1483.52] They create a DAG view of everything it needs to run.
[1483.84 → 1488.16] And it can reconcile what ran, what still needs to run, what has changed,
[1488.60 → 1490.06] which parts of the cache need invalidating.
[1490.86 → 1491.90] It has volumes.
[1492.68 → 1497.26] Behind the scenes, really, it leverages Build Kit, which is at the core of Docker 2.
[1497.26 → 1499.66] So anything that you can do.
[1500.02 → 1502.28] And by the way, the Docker file is just an interface to Build Kit.
[1502.68 → 1504.64] So I love this.
[1504.92 → 1510.64] I love having one place to specify versions and have all tooling and pipelining and production
[1510.64 → 1512.68] just do their thing.
[1512.94 → 1517.54] The one that always has scared me historically or been more complicated was Postgres,
[1517.84 → 1521.84] because sometimes a Postgres upgrade requires a data migration.
[1521.84 → 1524.88] How does this handle that circumstance?
[1525.34 → 1532.82] So currently, the version that we have specified in tools versions is the one that we have deployed
[1532.82 → 1533.72] in Fly.
[1534.26 → 1537.84] So in Fly, when you deploy Postgres, you have, you divide a Fly CTL.
[1538.16 → 1542.80] And it's the version that we had at the time of running this command.
[1543.04 → 1544.16] It is a platform, right?
[1544.22 → 1548.16] So you run, you have a CTL, and you also have a web interface.
[1548.16 → 1554.64] But in our case, we had Fly CTL, Postgres, deploy, create a cluster with the whole clustering
[1554.64 → 1555.72] setup and everything.
[1556.12 → 1558.72] And at the time, we had 14.1 deployed.
[1559.32 → 1566.48] One of the things that are on my list to do is to deploy Postgres SQL again, like have another
[1566.48 → 1573.34] cluster using Fly machines, which is Apps V2, and basically pick whatever the latest 14 version
[1573.34 → 1573.64] is.
[1573.72 → 1576.88] I think it was 14.8 or 14.9 when I checked.
[1576.88 → 1577.88] I'm not sure one or the other.
[1578.16 → 1580.50] So once we do that, there will be like a data migration.
[1580.50 → 1586.46] Then we will capture this version in our development environment via SDF, which will automatically
[1586.46 → 1587.98] be picked by the pipeline.
[1587.98 → 1593.10] So that when we run any tests in our pipeline, in our GitHub actions, GitHub actions will
[1593.10 → 1594.82] obviously be connected to a Dagger engine.
[1595.48 → 1598.90] And the correct, actually the same Postgres SQL version will be used there as well.
[1599.22 → 1602.46] So we have dev, test, and production, same version.
[1602.52 → 1605.20] But the production is what determines the Postgres SQL version.
[1605.20 → 1608.28] And that happens when we deploy the cluster to begin with.
[1608.28 → 1609.02] I follow.
[1609.02 → 1614.66] So if I want to upgrade Elixir, it's as easy as changing the version in the tool versions
[1614.66 → 1615.38] file.
[1615.58 → 1615.70] Yeah.
[1615.90 → 1618.24] But if I want to upgrade Postgres, it's the other way around.
[1618.50 → 1619.14] Postgres SQL, yeah.
[1619.20 → 1621.72] Postgres is different because it's like a stateful service.
[1621.92 → 1623.00] It's, you're right, you have data.
[1623.32 → 1624.30] There's like a bunch of things.
[1624.38 → 1628.78] You can obviously change it in the SDF file, but that won't change what's deployed in production
[1628.78 → 1629.50] because you're right.
[1629.54 → 1631.66] There's a data migration part to that.
[1631.66 → 1633.54] Fair enough.
[1633.76 → 1636.92] It was not quite as cool as I thought it was, but it's still amazing, Gerhard.
[1637.00 → 1638.86] Well, everything except that, right?
[1638.96 → 1641.40] Like the yard, no JS, right?
[1641.68 → 1644.24] I'm two for two on finding the one thing it doesn't do.
[1644.36 → 1645.04] You know where to look.
[1645.26 → 1646.16] Oh yeah, I do.
[1646.26 → 1647.22] Oh, I know what I like.
[1647.48 → 1648.10] I know what I know.
[1648.24 → 1651.30] Usually what I want is the hard parts, you know, taken care of for me.
[1651.46 → 1653.62] So still, that's very cool.
[1653.62 → 1658.72] So the reason why I asked if this tools versions thing was ASD For if it was broader, because
[1658.72 → 1665.02] it seems like this little bit of our infrastructure, at least, could be generalizable enough to
[1665.02 → 1669.50] the point where maybe it's useful for people to say, here is an AI-based pipeline integration
[1669.50 → 1670.78] that you can use.
[1671.24 → 1671.34] Yep.
[1671.48 → 1672.62] Do you think that's the case, maybe?
[1673.00 → 1674.10] That is possible.
[1674.40 → 1674.60] Yes.
[1674.64 → 1677.36] That requires a bunch of things on the dagger side as well.
[1677.70 → 1681.36] So right now, I mean, obviously you can, you know, get inspired by our pipeline.
[1681.36 → 1685.20] You can take it as is and, you know, change it and adapt it to your needs.
[1685.38 → 1692.38] It is a starting point, but really what you want is reusable pipeline fragments or components,
[1692.72 → 1692.92] right?
[1692.98 → 1697.08] So for example, if you had like Elixir tests, like how would you run those?
[1697.12 → 1700.98] You would want a component that you can just consume that doesn't exist in dagger today,
[1700.98 → 1702.86] but it's somewhere there on the roadmap.
[1703.44 → 1703.80] Very cool.
[1704.16 → 1709.16] Well, that's progress and not, not perfection, but it's progress over perfection.
[1709.16 → 1711.48] And besides, we have to Kaiden again soon.
[1711.60 → 1713.56] So we'd have to have something else to strive for.
[1713.66 → 1714.42] You can't just...
[1714.42 → 1715.02] Can't do it all now.
[1715.36 → 1717.14] You haven't asked me something important.
[1717.28 → 1718.98] So I'm going to ask myself the question.
[1719.48 → 1722.00] Hey, Gerhard, how long does our pipeline take to run?
[1722.98 → 1723.66] Good question.
[1723.88 → 1724.80] So it depends, right?
[1724.84 → 1726.40] If you have it cached.
[1726.64 → 1732.18] So even today, we are connecting from GitHub Actions to a Docker running on Fly.
[1732.40 → 1735.08] And again, if you look through our GitHub Actions workflow, you will see that.
[1735.08 → 1738.88] There is a Fly WireGuard Tunnel setup, and from GitHub Actions, we connect to Fly.
[1739.52 → 1740.60] That's where Docker runs.
[1741.12 → 1746.18] Internally, whenever you run an SDK, it automatically provisions whichever version of Dagger Engine
[1746.18 → 1746.66] it needs.
[1746.98 → 1752.22] So what that means is that whenever our GitHub Action runs, if it's in our repo, we have
[1752.22 → 1752.92] everything cached.
[1753.30 → 1757.98] Even though we have things cached, we weren't parallelizing our pipelines.
[1757.98 → 1763.98] So we were basically running, build me the runtime image sequentially, then move on to
[1763.98 → 1770.02] building the test image, then run the tests, then build the production image, and so on
[1770.02 → 1770.34] and so forth.
[1770.40 → 1772.54] So the whole thing was like one long line.
[1773.18 → 1778.32] What we did part of 464, we parallelized these pipelines.
[1778.44 → 1780.42] So now they run all at the same time.
[1780.86 → 1784.40] So the last pull request, which emerged, there weren't any code changes.
[1784.40 → 1788.16] It just had to recompile everything, rebuild everything, just make sure everything is fine.
[1788.24 → 1789.68] It took, I think, about two minutes.
[1790.28 → 1792.30] There was just like a markdown file change.
[1792.58 → 1796.14] So what I'm curious is next time that you run it, Jared, I think it used to be six to
[1796.14 → 1798.20] seven minutes for the pipeline to run.
[1798.56 → 1801.78] I think it'll be around four minutes now, maybe even three minutes.
[1802.12 → 1807.44] The next thing is to switch, and this is the pull request, which I haven't submitted yet,
[1807.96 → 1812.44] to switch to the Fly Apps V2 Dagger Engine.
[1812.44 → 1816.86] That, by the way, we can stop from within GitHub Actions.
[1817.30 → 1822.44] So because these are very small, like their firecracker based, you can start them in within
[1822.44 → 1823.18] 20 seconds.
[1823.60 → 1825.76] So you don't have to have this thing running all the time.
[1826.06 → 1827.06] You spin it up.
[1827.30 → 1828.14] The state is there.
[1828.20 → 1829.82] There's like a local NVMe volume.
[1830.14 → 1832.84] And this is all basically managed by the Fly platform superfast.
[1833.18 → 1835.38] You run your pipeline.
[1835.84 → 1836.64] The cache is there.
[1836.72 → 1837.46] The state is there.
[1837.62 → 1838.82] Whatever needs to change, changes.
[1838.82 → 1845.82] A few minutes late, again, in my tests, one minute and 35 seconds to deal with a code
[1845.82 → 1846.12] change.
[1846.36 → 1847.08] Recompile everything.
[1847.30 → 1848.10] Everything runs in parallel.
[1848.48 → 1853.28] And the deployment part, that's the one that basically just depends on how long it takes for
[1853.28 → 1853.88] it to be deployed.
[1854.30 → 1855.66] You can add another few minutes.
[1856.02 → 1860.12] But within three to four minutes, actually even like three minutes, I think, you can get
[1860.12 → 1861.30] a code change into production.
[1861.66 → 1862.06] That's awesome.
[1862.30 → 1864.98] And that's much faster than what you had to deal with, Jared, right?
[1865.02 → 1866.34] It was like eight, nine minutes.
[1866.50 → 1866.74] Yes.
[1867.00 → 1867.24] Yes.
[1867.24 → 1868.36] It's so much faster.
[1868.46 → 1868.88] Love it.
[1869.12 → 1870.50] So much so that I would forget it.
[1870.56 → 1874.54] And then sometimes the build process would fail or something would happen strangely,
[1874.76 → 1876.10] mainly for my stuff, really.
[1876.20 → 1878.68] I don't know if it's like just a thing or you think, Jared, but like I feel like.
[1878.74 → 1880.18] No, it happens for me too.
[1880.38 → 1880.70] Okay.
[1880.88 → 1881.20] Okay.
[1881.26 → 1882.06] I don't feel bad then.
[1882.80 → 1883.68] I'd forget about it.
[1883.70 → 1886.32] I'm like, okay, I have no idea how to restart that action, I guess.
[1886.32 → 1888.74] I guess I can go back to GitHub Actions and say, try again.
[1888.86 → 1890.16] But then there's like another thing going on.
[1890.20 → 1892.64] So then Jared deploys, and it succeeds, and it takes mine with it.
[1892.66 → 1893.16] So that's fine.
[1893.26 → 1893.50] Yeah.
[1893.70 → 1894.50] Because we're committing to main.
[1895.22 → 1896.18] Very cool, Gerhard.
[1896.18 → 1897.16] I love it.
[1897.34 → 1899.26] Chasing not the nines in that case, right?
[1899.26 → 1900.40] Like that's the anti-nines.
[1900.76 → 1901.94] Chasing the zeros, man.
[1902.00 → 1902.84] We're chasing the zeros.
[1902.94 → 1903.62] Chasing the zeros.
[1903.94 → 1905.44] How fast can we get this thing?
[1905.66 → 1907.24] Well, I don't think we can get it down to zero.
[1907.24 → 1911.16] Maybe we can get zero in the minutes' column, you know?
[1911.46 → 1912.30] You can dream it.
[1912.32 → 1913.00] It's already there.
[1913.14 → 1914.86] You know, it will take some seconds.
[1915.66 → 1915.80] Yeah.
[1915.84 → 1919.98] I think that will be, that'll be very difficult because even if you run it locally, right?
[1920.00 → 1921.84] Where everything is as fast as it gets, right?
[1921.84 → 1923.40] You can have the fastest Mac.
[1923.60 → 1927.42] If you're trying to compile some code, it will take some number of seconds.
[1927.56 → 1928.72] And it's not just that, right?
[1928.74 → 1929.96] You have to spin the process up.
[1930.00 → 1931.22] You have to reestablish connections.
[1931.52 → 1933.00] You have to do all those things, right?
[1933.02 → 1935.06] You have to check the health checks, make sure it's healthy.
[1935.32 → 1939.46] So it will always take some number of minutes because you're bringing a new instance.
[1939.62 → 1941.46] And by the way, this is like running in production.
[1941.84 → 1944.64] So you have blue-green, you have like a lot of traffic, you're shifting traffic.
[1944.64 → 1948.64] So it will take some number of minutes to get the code change out in production.
[1949.46 → 1953.18] And that's only with one instance, which brings us to the clustering part.
[1953.88 → 1957.68] To go to Fly Machines with our app, we'll definitely need to solve that problem.
[1957.68 → 1962.72] We will need to be able to cluster multiple instances of the changelog app.
[1963.04 → 1966.82] Without that, we may, I mean, if the host has a problem, right?
[1966.86 → 1971.00] With Nomad, with AppsV1, the instance could be migrated.
[1971.42 → 1976.18] With AppsV2, the instance cannot be migrated because it's tied to a specific host.
[1976.58 → 1980.94] If that host becomes unavailable, there's nowhere to schedule the app.
[1981.22 → 1983.40] Because again, that's how the platform was designed.
[1983.52 → 1985.98] So the idea is you need to have more than one instance.
[1985.98 → 1987.96] So we need to solve clustering, Jared.
[1988.28 → 1988.80] It's time.
[1989.28 → 1990.20] So you're pushing this on me.
[1990.32 → 1991.16] I see what we're doing here.
[1991.44 → 1992.44] Yeah, this one's on me.
[1993.46 → 1997.52] By the way, as a follow-up to your last statement, I just ran our test suite locally.
[1998.18 → 2000.04] It took 17 seconds to run.
[2000.20 → 2003.60] So I will accept a deployment of 20 to 25 seconds.
[2003.74 → 2004.24] No problem.
[2005.82 → 2006.18] Sure.
[2006.18 → 2008.48] Yes, I did not get around to this.
[2008.54 → 2012.88] Although, to my credit, I stated that I probably will not get around to this during this Kaiden period.
[2013.38 → 2018.88] Because most of my efforts have been in and around the migration of changelog news onto its own podcast.
[2019.32 → 2024.90] And the meta feed, which is our three shows, which are all distinct shows.
[2024.90 → 2027.82] So they can have their own feeds, their own subscriber base, etc.
[2028.14 → 2033.04] And then the changelog show, which is all three of those shows in one show.
[2033.28 → 2035.22] And the one-time migration of stuff.
[2035.72 → 2038.12] We had to re-implement how we do our newsletter and stuff.
[2038.20 → 2041.20] And so that was like what I've been doing in the last three months.
[2041.50 → 2043.12] And it's pretty much finished now.
[2043.12 → 2049.56] We do have an idea for how we can make changelog news' web pages better.
[2049.76 → 2050.82] Which I would love to do.
[2051.26 → 2053.54] Because it's quite an upgrade from what it looks like right now.
[2053.58 → 2054.88] And it simplifies things as well.
[2054.96 → 2058.18] So that's kind of like what I was thinking about doing before this.
[2058.30 → 2060.84] But we have honeycomb tracing now from Phoenix.
[2061.36 → 2063.50] Which we didn't have previously, thanks to you, Gerhard.
[2063.50 → 2065.18] So I'm now without excuse.
[2065.44 → 2071.84] Because I can monitor the speed changes as I make these caching changes.
[2071.84 → 2076.34] And I have a prototype from our friend Lost Wickman.
[2076.58 → 2081.38] Who showed me a way of doing a clusterable caching solution.
[2081.38 → 2084.28] Which doesn't completely rip out the guts of what we're currently doing.
[2084.36 → 2085.46] Which was my previous plan.
[2086.12 → 2087.72] So the skids are greased.
[2088.32 → 2091.06] And the observability is observable.
[2091.32 → 2096.96] By the way, you guys have seen Honeycomb has their new open AI integration in there.
[2097.12 → 2097.98] I just saw it today.
[2098.50 → 2099.30] No, I didn't see this.
[2099.56 → 2100.30] I haven't.
[2100.42 → 2100.94] Yeah, man.
[2100.94 → 2101.22] Yeah.
[2101.28 → 2101.92] Spill the beans.
[2102.22 → 2103.46] This is my new favourite thing.
[2103.56 → 2106.30] It's like, never make me write a SQL query again.
[2106.44 → 2106.58] Right?
[2106.62 → 2110.44] Never make me write a whatever Honeycomb queries are again.
[2110.72 → 2114.06] Just let me explain in plain English what I want you to do.
[2114.10 → 2115.36] And then you figure it out.
[2115.72 → 2116.54] And they integrated that.
[2116.62 → 2117.26] It's still beta.
[2117.56 → 2120.20] It aired out 50% of the time I've used it.
[2120.26 → 2121.08] And I've used it twice.
[2121.20 → 2122.18] So the first one aired.
[2122.26 → 2122.90] It's like one worked.
[2123.36 → 2125.16] But you just kind of like to tell it what you want to see.
[2125.16 → 2133.14] And it's going to have the open AI API come back with what looks like a pretty good query to get you started inside of Honeycomb.
[2133.32 → 2135.56] So kudos on them for rolling that out quickly.
[2135.76 → 2138.76] And I think this is just every tool.
[2138.76 → 2142.96] I mean, this was one of my complaints with Grafana was like Loki or whatever.
[2143.66 → 2146.98] Gerhard, the stuff that you wrote inside there was like learning a new language.
[2147.66 → 2150.38] And I liked them because you could save them as dashboards and I could look at them.
[2150.42 → 2154.92] But I was like, I ain't never going to write one of these from scratch because I don't have time for that.
[2154.98 → 2161.44] But if I can go in and tell Grafana what I want, and it can put together the actual query, which GPTs are very good at.
[2161.54 → 2163.56] I mean, I haven't written a SQL query in months.
[2164.02 → 2164.94] I've edited some.
[2165.10 → 2165.28] Right?
[2165.76 → 2166.72] You tell it what you want.
[2166.98 → 2167.80] It writes the query.
[2168.02 → 2169.84] And you edit it to work correctly.
[2170.30 → 2173.54] And so anyway, it's cool that we're starting to see this stuff get integrated.
[2173.68 → 2174.80] So it's there inside of Honeycomb.
[2174.90 → 2176.84] It's limited, 25 a day or something.
[2177.98 → 2179.48] And it aired out a couple of times.
[2180.36 → 2184.92] They did quote it as useful in terms of saying they don't know what useful is for you.
[2185.38 → 2186.90] So they put the word useful in quotes.
[2187.28 → 2188.08] They hope it's useful.
[2188.50 → 2188.68] Right.
[2188.78 → 2192.96] Well, they said that Query Assistant will produce, in quotes, useful queries.
[2193.30 → 2193.66] Right.
[2193.66 → 2196.00] And they said it's a loose term because they're not sure.
[2196.24 → 2200.02] It's impossible for them to know up front what the perfect query is for you.
[2200.34 → 2204.36] So I guess airing out is one thing, but a bad query or something that's not useful.
[2204.58 → 2204.60] Yeah.
[2204.62 → 2205.90] And that could have been a one-off.
[2205.90 → 2207.44] Like, I literally have used it a couple of times.
[2207.52 → 2208.12] It aired one time.
[2208.20 → 2208.66] No big deal.
[2209.00 → 2209.60] I'm looking at this, though.
[2209.60 → 2210.08] It's pretty cool.
[2210.20 → 2214.16] They, you know, they have a GIF at the top, and it's like, users with the highest shopping
[2214.16 → 2214.82] cart totals.
[2215.64 → 2215.96] Results.
[2216.60 → 2217.92] And slowest DB queries.
[2218.64 → 2219.00] Results.
[2219.00 → 2222.34] Because that's what you, you almost always know what you want to see.
[2222.70 → 2223.10] Right?
[2223.30 → 2225.38] Or at least you have an idea of where you'd like to start.
[2225.88 → 2230.52] I need to know this, but it's hard to get from there to the query.
[2230.70 → 2233.48] It's not like hard, hard, but it's like speed bumps.
[2233.48 → 2237.60] Sometimes that pain, too, as a user will make you not even use the tool at all.
[2237.86 → 2238.04] Totally.
[2238.36 → 2243.74] You know, that's what I love about the way that generative AI is, I wouldn't even say disrupting.
[2243.80 → 2247.26] I would just say like, man, fine-tuning the useful experience of something.
[2247.48 → 2252.28] Because Honeycomb is so powerful, but only if you have certain keys to unlock doors.
[2252.96 → 2257.08] And this just lets you bypass the keys because they're just like, hey, go find me keys.
[2257.16 → 2257.46] Right.
[2257.62 → 2257.82] In.
[2258.24 → 2258.76] It's kind of cool.
[2259.00 → 2260.08] Sentry is doing something similar.
[2260.22 → 2261.80] I've been inside the Sentry dashboard, by the way.
[2261.84 → 2262.96] Those are both sponsors of ours.
[2263.06 → 2264.84] This is not sponsored conversation by any means.
[2264.90 → 2266.86] It just happens to be the tools that we're using.
[2267.38 → 2272.58] And Sentry has this thing where they're like, do you want us to tell you what this might be the problem?
[2272.94 → 2274.76] Obviously, that's not how it's worded inside their dashboard.
[2275.18 → 2275.92] That's a terrible copy.
[2276.12 → 2276.54] Rewrite that.
[2276.60 → 2276.90] I know.
[2277.62 → 2280.06] I'm not giving it credit because I don't have the dashboard open.
[2280.06 → 2285.22] But it's like, click on this button, and we will try to determine not just what this error is,
[2285.36 → 2288.58] but like, it's kind of like, let me Google that for you, but on steroids.
[2288.76 → 2289.04] Anyway.
[2289.68 → 2294.98] I just like the idea that all these developer tools are just getting these upgrades that
[2294.98 → 2300.56] make them more usable at clips that are really fast and super useful.
[2300.84 → 2301.06] So anyway.
[2301.30 → 2301.46] Yeah.
[2301.98 → 2302.40] I concur.
[2302.58 → 2303.30] Side combo.
[2303.44 → 2304.90] But I have what I need with Honeycomb.
[2305.22 → 2305.44] Yeah.
[2305.44 → 2307.84] That was pull request 456, by the way.
[2307.94 → 2311.30] If you want to go and check it out, how integrated you can see the code changes.
[2311.46 → 2315.92] It wasn't that many, but you can see how we added, how we are sending app traces to Honeycomb.
[2315.92 → 2319.58] I want to give a shout-out to AJ Foster.
[2319.92 → 2320.48] Shout out.
[2320.68 → 2322.38] And yeah, shout out to AJ Foster.
[2322.60 → 2325.72] He's AJ-Foster on GitHub.
[2326.10 → 2333.40] He had a good blog post about how to do that integration, which by the way, was inspired by
[2333.40 → 2335.16] Dave Luce's blog post.
[2335.16 → 2338.50] And that's davydog187 on GitHub.
[2338.80 → 2340.52] So shout out to davydog187.
[2341.10 → 2341.80] Thank you, Dave.
[2342.12 → 2344.14] Between the two of you, that was super easy.
[2344.28 → 2347.34] And I added links in that pull request 456.
[2347.54 → 2348.24] You can check it out.
[2348.50 → 2348.72] Nice.
[2348.82 → 2353.02] So if anyone wants to do this integration again, it was super easy following these two blog
[2353.02 → 2353.32] posts.
[2353.80 → 2354.38] Super easy.
[2354.62 → 2355.40] Barely an inconvenience.
[2355.98 → 2356.20] Yep.
[2356.72 → 2357.56] Just took an hour.
[2358.06 → 2358.62] That was it.
[2358.62 → 2362.64] And most of it was like figuring out where to get a credential, how to get it right,
[2362.76 → 2363.20] things like that.
[2363.44 → 2363.54] Right.
[2364.08 → 2364.44] Awesome.
[2364.82 → 2365.34] Thanks, guys.
[2365.50 → 2366.00] Just the wiring.
[2366.72 → 2368.92] I guess I could have asked ChatGPT for that.
[2369.38 → 2370.32] That's cut off date.
[2370.58 → 2372.08] That's when they wrote it, you know?
[2372.18 → 2372.36] Yep.
[2372.48 → 2375.34] Although the new version is getting browsing, which Bard has.
[2375.44 → 2378.82] So I've done a little bit of Bard versus ChatGPT.
[2379.02 → 2380.98] Just literally copy and paste the same command.
[2381.20 → 2382.34] I don't know if you guys have tried Bard yet.
[2382.82 → 2383.02] Nope.
[2383.22 → 2383.78] Still not yet.
[2383.78 → 2385.22] And Bard has access.
[2385.30 → 2386.98] I mean, Google has answered to a certain extent.
[2387.12 → 2394.70] I still think GPT-4 specifically is better than Bard because Bard by default, A, no cost.
[2394.86 → 2399.40] So I am paying for the plus to get access to the faster features, 20 bucks a month on
[2399.40 → 2400.02] OpenAI.
[2400.70 → 2401.50] Bard is free to use.
[2401.54 → 2402.60] You have to be signed in, obviously.
[2403.10 → 2405.42] But it has default access to the internet.
[2405.58 → 2409.38] So you can like paste in a URL and say, summarize this for me or whatever you want to say, and
[2409.38 → 2412.32] it will go curl that sucker and spit it into itself.
[2412.32 → 2415.24] So that's super useful for documentation purposes.
[2415.84 → 2419.68] And the new, I mean, OpenAI will be there briefly, like they have with browsing.
[2420.04 → 2423.40] But the same exact command, all coding stuff.
[2423.54 → 2426.02] I don't care as much about the other stuff, but just the comparisons.
[2426.34 → 2431.20] And Bard has been 100% inaccurate on Elixir code.
[2432.48 → 2435.78] It's completely failed on every attempt.
[2435.98 → 2437.80] There are a lot of improvements they have to ship.
[2438.06 → 2438.74] There is.
[2438.88 → 2439.66] That's what I'm thinking.
[2440.00 → 2440.20] Yeah.
[2440.38 → 2440.68] Kaiden.
[2440.68 → 2442.96] So they need a Kaiden, that sucker.
[2443.08 → 2446.14] But it's nice for other, I mean, it's cool to see the different responses.
[2446.92 → 2448.00] They both need to get better.
[2448.08 → 2449.36] But I just thought that was hilarious.
[2449.44 → 2456.74] Because the best thing is that I don't have in RAM storage, Elixir, certain functions.
[2456.94 → 2458.18] Like I just, I use it enough.
[2458.56 → 2461.94] And I know like, okay, the enum module has these functions.
[2461.94 → 2463.48] But then like other ones are in list.
[2463.66 → 2464.68] Other ones are in map.
[2465.20 → 2466.58] You know, what's the function signature?
[2466.58 → 2472.84] And I'm so insecure about my knowledge that every time, and ChatGPT is done as well, that Bard was wrong.
[2473.04 → 2474.72] I 100% believed it.
[2474.78 → 2475.66] I'm like, oh, cool.
[2476.26 → 2477.00] I love this.
[2477.10 → 2478.06] And I went and tried it.
[2478.12 → 2479.62] I'm like, no, you can't do that.
[2480.42 → 2481.24] Oh my gosh.
[2481.24 → 2482.38] But I would love it if you could.
[2482.52 → 2483.72] So I think it's very optimistic.
[2484.88 → 2485.20] Yes.
[2485.46 → 2490.52] Well, if you look in changelog discussion 452, which is again the ones for this episode.
[2490.66 → 2490.96] Yes.
[2491.12 → 2497.30] I asked ChatGPT if we deployed 120 times between March 8th and May 20th.
[2497.34 → 2497.68] Yes.
[2497.96 → 2499.44] How many deploys per day did we do?
[2499.88 → 2500.56] And it was accurate.
[2500.56 → 2504.88] It could figure out how many days there are between March 8th and May 20th.
[2504.90 → 2505.62] It was so nice.
[2506.16 → 2507.62] The answer is 1.62.
[2507.72 → 2508.40] There's a screenshot.
[2508.74 → 2509.42] 1.62.
[2509.58 → 2511.24] That's how many deploys per day we did.
[2511.68 → 2511.96] Really?
[2512.34 → 2514.46] And most of those were JARS changes.
[2514.58 → 2514.68] Yeah.
[2515.08 → 2518.58] Obviously, not every commit results in a deployment because you batch them.
[2518.68 → 2519.84] So it's not quite that many.
[2519.98 → 2521.06] But one per day?
[2521.54 → 2523.22] I think we had one per day on average.
[2523.52 → 2523.78] Right.
[2524.06 → 2525.72] Well, there's definitely some heavy lifting there.
[2525.84 → 2529.42] So also, I am not a pull request person, as you can tell.
[2529.42 → 2531.92] You keep referring to your PRs by number.
[2532.14 → 2535.10] You probably have little tattoos with PR numbers on them.
[2535.22 → 2535.40] Nope.
[2535.48 → 2539.64] You're like, this was the time that my first commit to Dagger PR number.
[2539.72 → 2540.72] No, just messing with you.
[2540.82 → 2543.36] But I'm just like a trunk developer.
[2543.50 → 2544.36] I'm just right there.
[2544.52 → 2546.08] I just want it to go out.
[2546.20 → 2546.52] Me too.
[2546.94 → 2548.58] I think this context is perfect.
[2548.68 → 2549.68] The changelog, right?
[2549.74 → 2551.36] That's when we developed it from the beginning.
[2551.78 → 2554.66] Every commit to main, master, will go into production.
[2554.92 → 2555.28] That's it.
[2555.42 → 2555.56] Right.
[2555.56 → 2557.56] So yeah, I just keep doing that.
[2559.42 → 2560.58] I don't have the patience.
[2560.76 → 2563.38] The only reason why its pull request is because of these Maidens, right?
[2563.44 → 2564.42] Like, what do we reference?
[2564.54 → 2565.36] Oh, you know that commit?
[2565.46 → 2566.36] And there's that other commit?
[2566.44 → 2567.36] And there's that third commit?
[2567.54 → 2569.36] If you put them together, that's how we did it.
[2569.54 → 2571.40] It's a lot more difficult to talk about them.
[2571.52 → 2571.72] Right.
[2571.78 → 2575.44] Well, that's why we're talking about your work more than mine, because I don't remember
[2575.44 → 2577.50] any of the individual things that I did.
[2577.70 → 2578.04] Exactly.
[2578.22 → 2581.96] And by the way, Jared did a lot more work than I did, just to make it clear.
[2582.14 → 2582.46] Okay.
[2582.46 → 2584.38] I just have pull requests to prove it.
[2585.04 → 2586.08] He has lots of commits.
[2586.98 → 2587.60] That's true.
[2587.78 → 2588.52] You got receipts.
[2589.46 → 2590.06] Fair enough.
[2590.16 → 2591.28] Well, your stuff is cooler, too.
[2591.44 → 2594.96] The one thing with this ChatGPT question is, you didn't reference the year.
[2595.30 → 2595.94] Does it matter?
[2596.36 → 2596.86] It shouldn't.
[2597.14 → 2597.98] With the year, I guess not.
[2598.14 → 2601.60] Like, May 8th through, or sorry, March 8th through May 20th will always be the same
[2601.60 → 2602.76] no matter the year, right?
[2603.12 → 2603.94] As long as it's not a leap.
[2604.24 → 2605.36] Gerard knows leap years.
[2605.52 → 2605.90] That's right.
[2605.94 → 2606.54] I do, yes.
[2606.64 → 2607.50] You're a leap year baby.
[2608.08 → 2608.34] Yep.
[2608.34 → 2609.54] February 29th.
[2609.62 → 2612.46] So as long as you don't have to worry about February 29th.
[2612.54 → 2614.56] Yeah, because March will always have 31 days.
[2615.08 → 2617.50] And I think May is also a 31-day month.
[2617.68 → 2618.70] And here's a question.
[2619.12 → 2623.92] Would it account for that if you went, like, January to May, ask for the day count?
[2624.02 → 2627.34] Would it say, well, it depends on the year because of leap years?
[2627.50 → 2628.96] Let's try it and see what happens.
[2629.22 → 2629.50] All right.
[2629.58 → 2630.50] Follow back up on that.
[2630.74 → 2630.92] Yeah.
[2631.42 → 2631.94] All right.
[2631.94 → 2635.88] In the meantime, what else have we done during this time period?
[2635.96 → 2637.72] What else at least is worth talking about?
[2638.34 → 2643.94] Well, I'd like to give a shout-out to Ken Most for W3C HTML validation fixes.
[2644.16 → 2645.38] Let's pull a request 462.
[2645.52 → 2645.96] Oh, yes.
[2646.10 → 2647.28] Thank you for contributing that.
[2647.38 → 2647.96] That was a good one.
[2648.32 → 2649.62] Ken would like to get more involved.
[2649.72 → 2652.84] He hopped into our channel and said, hey, I'd like to hack on this.
[2653.14 → 2655.44] And I just honestly don't have a great answer to that.
[2655.48 → 2659.72] I'm just like, I would love help, but we don't know what we're doing.
[2661.30 → 2662.00] Pretty much.
[2662.00 → 2663.72] We're just making this stuff as we go along.
[2663.88 → 2663.98] Yeah.
[2664.38 → 2667.62] I mean, when I see a thing, I do a thing and I have visions in my head.
[2667.62 → 2672.02] But I don't write those visions down because a lot of those visions aren't ever going to be worked on.
[2672.16 → 2675.16] You know, so it's tough having contributions.
[2675.78 → 2677.62] I love that he found a way of contributing, right?
[2677.70 → 2678.16] It was awesome.
[2678.26 → 2681.26] He just went through and fixed all of our HTML to be valid.
[2681.56 → 2682.72] He has an easy merge.
[2682.72 → 2686.50] But I wish we had a better story around contributions.
[2686.50 → 2696.26] Something I want that he might be able to do is the ability to have Tailwind built into the app alongside our current SaaS pipeline.
[2696.38 → 2700.76] So we can incrementally move away from old design to something that's Tailwind powered.
[2701.94 → 2702.66] That's a good one.
[2702.74 → 2705.36] And that requires a bit of infrastructure to do that, right, Jared?
[2705.70 → 2707.14] I know you said you could do it.
[2707.34 → 2708.44] That one's on my hit list.
[2708.44 → 2712.12] So there are things that I'm just planning on doing that I'm not going to write-up for someone else.
[2712.18 → 2716.26] Because then I'll have to tell them exactly what I'm thinking.
[2716.48 → 2719.58] You know, like it just becomes, now they like work for us or something.
[2719.72 → 2720.36] And I'm like, hmm.
[2720.56 → 2721.36] It'll be a task.
[2721.74 → 2722.58] You find your own job.
[2722.62 → 2724.90] You make your own job around here if you want a job, okay?
[2724.96 → 2726.26] We're not making your job for you.
[2727.60 → 2728.74] That's the hard part, though.
[2729.36 → 2730.02] It is hard.
[2730.02 → 2737.68] Our repo is almost like open source, not so much anti-contribution, but we don't know how to tell you to contribute.
[2738.66 → 2744.56] It's not quite Ben Johnson level where it's like my code, limited contribution.
[2744.88 → 2746.88] Welcome, but in certain contexts.
[2747.00 → 2752.18] It's just we don't have a label out there for easy changes to make, for example.
[2752.68 → 2754.50] Certain tasks just hanging out there.
[2755.10 → 2755.94] And we never have.
[2756.12 → 2757.26] And I don't know if we ever will.
[2757.26 → 2765.70] It's just a hard problem to solve without having a very clear and specified public roadmap of where we're headed with the website.
[2766.80 → 2769.10] But, I mean, we make decisions all the time that change where we're headed.
[2769.28 → 2772.02] And they could be like 30 minutes before I code them up, you know?
[2772.70 → 2776.46] There probably are things that we could have out there, but we just don't.
[2776.56 → 2778.24] So thank you, Ken, for finding a way.
[2778.70 → 2779.56] Even this show here.
[2779.64 → 2780.72] This show was named something else.
[2780.80 → 2781.48] No, not this show.
[2782.04 → 2784.00] Change All News is named something else for a bit there.
[2784.00 → 2790.84] And up to like the legit the 11th hour, was it renamed back to something that was more meaningful, I suppose, to the brand?
[2791.28 → 2792.74] Yeah, or more aligned at least.
[2793.08 → 2802.14] And then all the, you know, you had done some schema, some visualizations in Obsidian with how the feeds would shake out and which one would be the primary feed.
[2802.38 → 2806.66] Like, it wasn't until like the 11.5 hour of that change.
[2806.70 → 2808.30] And then we were like, okay, cool.
[2808.68 → 2809.78] Because you and I both had.
[2810.08 → 2811.26] Because we don't always agree on things.
[2811.26 → 2813.90] I don't know if everybody knows that, but Adam and I don't always agree.
[2817.02 → 2820.28] Well, we partially agree, and we're just still sort of in that unclear state.
[2820.38 → 2821.84] It's like, well, I kind of agree with that.
[2821.96 → 2823.90] Yeah, or just not confident yet.
[2824.10 → 2824.34] Yeah.
[2824.54 → 2828.96] Sometimes we just need like the other person to become confident before we will be, you know?
[2829.04 → 2830.80] I'm like, well, Adam's not sure.
[2830.96 → 2831.52] I'm not sure.
[2831.70 → 2834.30] But once he becomes more sure, it's like this is starting to feel good.
[2834.58 → 2836.68] Or I'll be 100% sure and have to convince him.
[2836.72 → 2838.02] And if I can, then he becomes sure.
[2838.08 → 2840.32] And if I can't, I mean, this is typical business stuff.
[2840.32 → 2842.04] But it makes it hard.
[2842.54 → 2848.86] And I definitely have empathy for people building in public, you know?
[2848.92 → 2857.18] And there are teams that have like SaaS products that are open, either open source or open sources SaaS products with public roadmaps.
[2857.38 → 2861.54] Where they're taking like their user's input and stuff and trying to pick a direction.
[2861.88 → 2864.88] And I think that's just a very, very hard thing to do well.
[2865.32 → 2866.06] Tell me about it.
[2866.06 → 2870.36] I actually watched the Homer Simpson car clip the other day.
[2870.48 → 2874.66] Like the four-minute extract on YouTube of when they asked Homer Simpson to design the car.
[2874.96 → 2878.22] It's such a good little analogy for the software world.
[2879.04 → 2882.28] And the best part is at the very end, they go to present the car, you know?
[2882.32 → 2883.52] And it has all the features.
[2883.84 → 2884.76] I'm not sure if you guys have seen this.
[2884.98 → 2886.56] I know you know the meme.
[2886.66 → 2888.76] Yeah, it's ugly, but it's souped up.
[2888.84 → 2890.02] I mean, it's got tons of stuff.
[2890.02 → 2893.46] And they present it to this crowd, you know, because it's like a concept car.
[2893.94 → 2896.84] And the presenter goes to name how much it'll cost, you know?
[2896.94 → 2898.82] And the guy just whispers it into his ear.
[2898.94 → 2900.72] He's like, it costs what?
[2901.04 → 2906.68] And it's like $80,000 or something and nobody wants because they just, you know, packed it to the brim.
[2907.02 → 2907.32] That's right.
[2907.32 → 2914.32] And so not only is it ugly and that nobody would ever buy, but it's also completely too expensive, which software, right?
[2914.64 → 2915.40] It is half the battle.
[2915.58 → 2916.34] Getting the price right.
[2916.68 → 2921.46] The right product, the right price, right availability, the right quality, all the rights.
[2922.54 → 2928.90] Gerhard, in that example you shared earlier, that visualization of all the dependencies and whatnot, the pipeline being built.
[2929.16 → 2931.08] You had Apps V2 mentioned.
[2931.08 → 2941.56] And what's not in our list to talk about, but I'm curious of since you were playing with Apps V2, was the machines versus Apps V2 consideration we talked about the last time we talked.
[2942.02 → 2944.04] Can you share anything on that front?
[2944.20 → 2946.82] Has there been experimentation, evaluation?
[2947.64 → 2949.20] That was the one that I was showing.
[2949.58 → 2952.86] So we have, we will ignore changelog social for now.
[2952.98 → 2956.70] There's like a whole changelog social side of our infrastructure that we can ignore.
[2956.70 → 2962.10] We have three things today, important for changelog, that are running on Apps V2.
[2962.42 → 2967.84] Apps V2 is the Fly.io platform that is based on nomad scheduling.
[2968.74 → 2972.28] So there are a couple of limitations of that.
[2972.42 → 2974.40] Basically, it's the scale that Fly reached.
[2974.74 → 2978.36] And that basically meant that various things weren't working quite as well.
[2978.36 → 2987.96] There's like a whole thread on this course where Kurt was very transparent about some of the issues they encountered with Apps V1 and what they're doing about that.
[2988.38 → 2991.90] So Apps V2 is a complete redesign of the scheduling.
[2992.46 → 3001.60] The way I understand it, it's like their own proprietary scheduling, which does not use nomad, does not use Kubernetes, does not use any of the things that you may expect.
[3001.60 → 3006.10] And as a result, it's a lot more robust.
[3006.40 → 3008.52] It's built for their scale, for what they need right now.
[3008.66 → 3014.30] And what it means in practice is for us, it's really, really fast to use and deploy things onto.
[3014.74 → 3021.32] So it means that you can get very fast VM-like containers.
[3021.32 → 3024.24] It's using Firecracker VM, again, my understanding behind the scenes.
[3024.74 → 3029.68] And they spin up very quickly, but they have all the security that you would expect from a VM.
[3029.68 → 3035.06] So spin uptime is seconds, really, even less depending on what you're doing.
[3035.40 → 3044.40] But obviously, by the time you do health checks and a bunch of other things, it can take, you know, in our case, some things, 20 seconds, 30 seconds to come up and be healthy and for us to be able to use them.
[3045.62 → 3050.22] These Apps V2, they are pinned to specific machines, right?
[3050.30 → 3052.04] Hosts, like physical hosts in this case.
[3052.52 → 3055.54] What that means for us is that we can't run just one.
[3056.06 → 3058.84] So right now we have a single instance of changelog running.
[3058.84 → 3061.42] It's been like that for quite some time.
[3061.74 → 3063.02] That's why the clustering is important.
[3063.10 → 3064.04] So we have more than one.
[3064.52 → 3066.42] But that's okay because we have a CDN in front.
[3066.54 → 3070.82] We do a bunch of things where even if the app goes down, we are still available, right?
[3070.90 → 3075.44] And Jared did a couple of improvements, which means like even the post, for example, now they continue being available.
[3075.82 → 3078.26] We want to do certain requests against like news items and whatnot.
[3078.76 → 3081.42] So our availability really relies on Vastly.
[3081.42 → 3091.84] And what that means is that it takes like once every five years sort of event to take us offline, which is again, we discussed, I forget which Kaiden it was, but we talked about that when half the internet was down.
[3092.14 → 3093.26] Like two or three, I bet.
[3093.50 → 3094.34] It happened once.
[3094.62 → 3094.92] Exactly.
[3095.02 → 3095.76] Only once, right?
[3095.80 → 3097.62] And that was like in seven, eight years.
[3097.74 → 3098.66] So I think it's okay.
[3099.10 → 3101.10] And even then it was fixed fairly quickly.
[3101.28 → 3102.56] It's kind of like the end of Cable Guy.
[3102.56 → 3107.80] Have you guys seen the end of Cable Guy where Jim Carrey falls onto the broadcast dish?
[3108.12 → 3108.60] No.
[3108.96 → 3111.94] And all, everyone's TVs just go to fuzz.
[3113.02 → 3132.54] And they suddenly realize there's a whole world outside, you know, and they look out their window, they step outside, their feet touch the grass.
[3132.96 → 3133.92] And they're like, wow.
[3138.98 → 3140.00] That's what we did that day.
[3140.12 → 3146.98] You know, when Vastly went down, the whole internet was basically down because Vastly powers so much of it that we just took a walk in the park.
[3147.38 → 3147.74] Exactly.
[3148.22 → 3150.12] Systems were affected that you didn't even know existed.
[3150.26 → 3152.82] And just texted Gerhard, just like, Gerhard, what are you doing?
[3152.86 → 3153.38] It's down.
[3154.18 → 3154.58] Sunbathing.
[3154.94 → 3155.68] That's what I remember.
[3155.70 → 3155.84] That's right.
[3155.92 → 3157.08] You were sunbathing, weren't you?
[3157.76 → 3158.12] Exactly.
[3158.20 → 3158.98] It was like a day off.
[3159.34 → 3159.90] So it was good.
[3160.10 → 3160.22] Yeah.
[3161.22 → 3161.58] TMI.
[3161.58 → 3165.12] BBC was down and New York Times was down and Guardian was down.
[3165.34 → 3166.46] Like, you know, changelog.
[3166.58 → 3167.20] It doesn't matter.
[3167.30 → 3167.68] It's okay.
[3168.20 → 3170.44] All the other big news companies are down.
[3170.92 → 3179.56] Anyway, the point was, coming back, that with Apps V2, if the host is unavailable, the app cannot be scheduled somewhere else.
[3179.90 → 3181.52] So we have to have more than one.
[3181.72 → 3182.50] We can't have just one.
[3182.50 → 3187.90] With Nomad, with Apps V2, let's say the host was down, the same app could be scheduled elsewhere.
[3188.12 → 3191.54] Because, like, it was more of a basically, the apps could move around the platform.
[3192.02 → 3192.22] Right?
[3192.26 → 3194.76] In this case, in Apps V2, they're pinned to physical hosts.
[3194.76 → 3199.54] So, even though they're faster, they're better, they're, you know, like, more self-contained.
[3199.64 → 3201.30] Like, when one thing fails, it doesn't affect.
[3201.44 → 3203.92] There's, like, basically the it's a lot more resilient.
[3204.04 → 3205.58] The platform as a whole is a lot more resilient.
[3205.90 → 3208.48] But that means that you have to design with this in mind, right?
[3208.48 → 3213.98] With blast radiuses and when one thing goes down, like, how do you basically work with that?
[3214.24 → 3215.66] With partial unavailability.
[3215.66 → 3219.40] And it makes sense, but it means we need clustering.
[3220.10 → 3223.66] So, moving something like, for example, Dagger Engine, it's okay.
[3223.84 → 3224.76] Or Docker, right?
[3224.80 → 3227.94] Because if that's down, that's okay, it can fall back to whatever is local.
[3228.20 → 3229.92] And by the way, we do that in our pipeline.
[3230.40 → 3233.54] If PostgreSQL is down, well, you're already clustering that.
[3233.92 → 3236.92] You know, we have, like, again, some sort of redundancy there.
[3237.22 → 3241.40] In our case, we had one primary and one replica.
[3241.54 → 3245.46] And by the way, I think we should look into that as well to see if we can get a managed
[3245.46 → 3246.96] proper managed PostgreSQL service.
[3247.04 → 3248.18] We keep talking about that.
[3248.40 → 3250.72] Maybe crunchy, maybe super-based.
[3250.86 → 3252.18] Try a few and see what sticks.
[3252.78 → 3257.58] To continue, we can still run on fly for the PostgreSQL instance, even though I think they
[3257.58 → 3260.32] were mentioning at some point they will want to invest in that.
[3260.40 → 3261.42] So, we'll see where that goes.
[3261.86 → 3262.66] Things may have changed.
[3262.74 → 3263.82] Again, this was on their forum.
[3264.44 → 3267.52] So, we can move Dagger Engine, Docker.
[3267.78 → 3271.12] We can move PostgreSQL to Apps v2, to machines.
[3271.38 → 3273.30] But the app itself, it's a bit more problematic.
[3273.44 → 3274.96] Not without the clustering part.
[3275.46 → 3278.62] Because of what they explained, like, the limitation with hosts.
[3278.96 → 3281.92] So, while it's a modern platform, it's very performant.
[3281.98 → 3285.20] Again, all the tests which I ran, you get, like, very nice CPUs.
[3285.28 → 3288.86] The AMD epics, they're yours, especially if you get, like, the performance instances.
[3289.28 → 3291.22] You get local Names.
[3291.30 → 3292.28] Again, very fast.
[3292.62 → 3295.34] But if the host becomes unavailable, it won't get moved.
[3295.68 → 3299.48] So, we have to get the clustering to do Apps v2 properly.
[3299.68 → 3300.02] Exactly.
[3300.02 → 3300.84] All right, Jared.
[3301.36 → 3302.98] The whole world is on my shoulders.
[3303.70 → 3304.46] Well, the...
[3304.46 → 3305.54] The whole changelog world.
[3305.68 → 3305.94] Yeah.
[3306.02 → 3307.16] Just quantify that.
[3308.54 → 3310.26] There are a lot of things, too, we just talked about.
[3310.48 → 3311.64] Jared, you mentioned news items.
[3311.80 → 3313.22] I know they're still in our infrastructure, Jared.
[3313.30 → 3314.42] But, like, even...
[3314.42 → 3321.52] There's a lot with this change from weekly and news items and this news homepage to this world we're in now, which is sort of, like, obsolete.
[3321.90 → 3322.20] Right.
[3322.20 → 3324.40] And primed to delete code.
[3324.52 → 3326.86] There are a lot of places that we could delete...
[3326.86 → 3327.18] Right.
[3327.28 → 3328.22] ...from the app code.
[3328.46 → 3328.74] Right.
[3328.74 → 3334.00] We just haven't because, A, you want to make sure that you like this new home that you're living in for a little while.
[3334.42 → 3334.72] Yes.
[3334.86 → 3337.38] And you're not going to be like, why did I throw that furniture away?
[3337.78 → 3339.12] Well, I like it a lot better already.
[3339.36 → 3340.30] I got my feet up.
[3340.72 → 3341.56] I'm liking it, too.
[3341.62 → 3345.70] I don't think we're going to go back, but I wasn't going to rush into deleting the code.
[3345.80 → 3347.32] I do love to delete code.
[3347.74 → 3351.56] But my least favourite command is git revert, you know?
[3351.70 → 3352.08] Mm-hmm.
[3352.20 → 3352.52] Mm-hmm.
[3352.90 → 3358.60] Like, a lot of stuff that we built, even the whole impressions thing and all that, just, it's obsolete.
[3359.04 → 3359.96] We're just not using it anymore.
[3360.06 → 3361.96] We're not doing news items like we used to.
[3362.28 → 3362.50] Yeah.
[3362.50 → 3369.76] And, in fact, my concept, which I guess before we started recording, we were talking about STI, single table inheritance.
[3369.90 → 3372.30] Gerhard and I were reminiscing on War Stories.
[3372.64 → 3382.18] From the old Rails days, this was a feature, it's probably still in there, where you could do a classical object-oriented inheritance with a single database table and use a type column.
[3382.20 → 3383.88] To instantiate different classes.
[3383.88 → 3392.52] So you could have a table called pets and classes called dog and cat, which both inherit from pet, but they get stored together in one table.
[3392.52 → 3400.28] And my concept when I built this site, you know, you make certain decisions that are foundational to an application.
[3400.28 → 3405.90] And one of them, which served us very well for many years, was everything's a news item.
[3406.78 → 3409.90] And every news item points to something.
[3410.44 → 3412.06] So it can be on our website.
[3412.20 → 3413.34] It can be on somebody else's website.
[3413.70 → 3414.44] It can be audio.
[3414.58 → 3415.22] It can be video.
[3415.62 → 3416.40] It can be text.
[3416.52 → 3417.16] It can be a tweet.
[3417.34 → 3418.30] It can be a whatever.
[3418.30 → 3423.84] And we decorate those differently based on information we have about the news item itself.
[3424.32 → 3427.66] Now, I didn't actually use single table inheritance to implement this.
[3427.72 → 3429.08] It's just similar conceptually.
[3429.58 → 3430.56] And that was great.
[3430.56 → 3437.74] And it served us very well for probably all the years until right now where we literally are abandoning the news item part of what we do.
[3438.26 → 3441.34] And we're only publishing blog posts and episodes, right?
[3441.42 → 3442.08] Audio episodes.
[3442.08 → 3453.42] And every other news item is just kind of like an appendage that is still there in the data structures but only represents things that could just be represented directly, you know, if I hadn't made that decision.
[3453.92 → 3456.04] Aren't comments also hanging on the news items too?
[3456.26 → 3456.66] They are.
[3456.92 → 3457.10] Yeah.
[3457.14 → 3458.08] Yeah, they're attached to news items.
[3458.60 → 3458.88] Yeah.
[3459.28 → 3464.94] Because that was like the foundational, you know, atomic unit of content in the CMS.
[3465.72 → 3467.88] Like I said, it was good for us for many years.
[3467.88 → 3476.06] But as we simplify and change now where we're just publishing, I write Changelog News in Markdown, which I love.
[3476.42 → 3481.84] But Changelog Weekly was generated from a list of news items that we published throughout the week.
[3482.16 → 3484.48] And that's a foundational change to the way that we do content.
[3484.92 → 3491.26] This one's simpler and I think more sustainable and hopefully produces better content over time.
[3491.70 → 3494.54] But all of our infrastructure is built for that other way.
[3494.86 → 3496.00] And so there's stuff that we can delete.
[3496.00 → 3501.14] There's also stuff that's just going to be there because it's like ripping out your circulatory system.
[3501.46 → 3507.12] Well, when you look at, for example, changelog.com slash podcast, which is where this show is at right now, right?
[3507.50 → 3510.54] The list of things there are news items.
[3511.30 → 3511.40] Right.
[3511.78 → 3513.30] Everything we fetch is news items.
[3513.46 → 3513.72] Right.
[3513.82 → 3518.50] Unless we change the design dramatically to rend this obsolete, like this still is pertinent, right?
[3518.54 → 3519.36] This is still useful.
[3519.70 → 3520.06] Oh, yeah.
[3520.08 → 3521.24] We're still using that for sure.
[3521.32 → 3523.78] That's why I say we're not going to rip out certain things.
[3523.78 → 3528.22] But there are areas of the code base that are news item related that could definitely go away.
[3528.72 → 3535.36] Like in the admin for creating a new issue, which was once changelog weekly, that can go away completely.
[3535.56 → 3535.84] Because like...
[3535.84 → 3536.82] We don't use that anymore.
[3537.08 → 3538.18] Yeah, we're not turning back from that.
[3538.44 → 3540.26] And we attach the newsletter content.
[3540.40 → 3545.74] So changelog news goes out at the exact same time, both the episode and the email.
[3545.74 → 3550.64] And we attach the email content directly to the episode, not to a news item.
[3551.42 → 3553.26] And so, yeah, issues are gone.
[3553.36 → 3554.62] News ads can go away.
[3555.22 → 3558.10] There's a bunch of stuff around scheduling sponsorships.
[3558.40 → 3560.50] All that stuff was based on the old system.
[3560.64 → 3565.24] So, yeah, we could definitely do some spring-cleaning, probably summer cleaning at this point.
[3565.34 → 3567.98] But then you're like, well, it's also not hurting anything.
[3568.10 → 3570.68] And they're sure waiting on me for this clustering feature.
[3571.82 → 3573.28] So maybe I'll work on that instead.
[3573.28 → 3574.42] I love it, man.
[3574.86 → 3580.84] Digging the changes, digging the Kaiden, digging the commitment to incremental change.
[3581.00 → 3583.18] Like, you know, it reminds me of the book, Atomic Habits.
[3583.54 → 3588.82] If you can make a 1%, a half a percent change today, and you do that for three or four days straight, well, what did you do?
[3588.94 → 3589.12] Right?
[3589.18 → 3591.92] You made an almost 5% change.
[3592.38 → 3594.60] And you stress out about, I can't do all of it today.
[3594.74 → 3595.40] That's okay.
[3595.54 → 3596.92] Just do what you can today.
[3597.34 → 3599.42] Just enough to move the needle forward.
[3599.42 → 3602.86] Whatever it takes to progress, do that thing.
[3603.08 → 3603.26] Right?
[3603.70 → 3606.52] We've been doing that for many, many years now, collectively.
[3607.18 → 3609.34] We've embodied that with Kaiden on Ship It.
[3609.36 → 3613.62] Now we've brought it here to changelog on friends with our oldest friend, Gerhard.
[3614.10 → 3616.92] With a sheer commitment to chasing the nines.
[3617.10 → 3617.64] And the zeros.
[3617.80 → 3618.92] The best pipeline ever.
[3619.36 → 3620.82] Like, TM that at the end, right?
[3620.88 → 3621.56] Trademark that thing.
[3621.92 → 3623.18] The best pipeline ever.
[3623.46 → 3624.46] It is world-class.
[3624.76 → 3625.12] Honestly.
[3625.56 → 3625.94] Gosh.
[3626.06 → 3627.08] No one has a better one.
[3627.28 → 3627.50] Nobody.
[3627.50 → 3628.52] No one has a better pipeline.
[3628.52 → 3629.48] You hear that out there?
[3629.92 → 3631.04] Show us your pipeline.
[3631.16 → 3632.02] It's better than ours.
[3632.02 → 3642.98] If you check out the code to see like a pipeline as complicated as ours in code and how it all combines with apps dependencies, with the versioning, with how the app gets compiled.
[3642.98 → 3647.36] We even have, and again, I haven't finished this, is their Erlang releases.
[3647.36 → 3649.00] Let's get that sucker done.
[3649.22 → 3649.96] And it makes it releases.
[3650.10 → 3650.58] It's not there.
[3650.64 → 3652.74] Again, and no one has like thought of this.
[3652.82 → 3655.70] Like, hey, Gerhard, can you please like to get to those Erlang releases?
[3655.82 → 3657.58] Or, hey, Gerhard, can you please upgrade Postgres SQL?
[3657.94 → 3659.46] These things happen organically.
[3659.76 → 3663.10] Because you kind of like get like in the middle of it and you kind of understand what the system needs.
[3663.14 → 3664.78] It's like a living, breathing thing.
[3664.78 → 3674.40] And, you know, if you have half an hour and even talked about this like way back when, what is the most important thing I can do right now that will make this thing slightly better?
[3674.82 → 3677.34] An hour tomorrow, whatever the case.
[3677.38 → 3678.42] I have a weekend, two hours.
[3678.52 → 3679.94] Okay, so what can I do in those two hours?
[3680.00 → 3681.46] And all those things add up.
[3681.68 → 3684.72] And two months later, it's amazing how much has changed.
[3685.06 → 3687.80] And that's why we're trying to capture these changes in the Kaiden.
[3687.80 → 3691.40] Because again, if you look at it every day, it's not a lot there.
[3692.30 → 3693.22] Same thing with news.
[3693.30 → 3696.64] I've seen like there's like so many things that you had to do, Gerhard, like to get this news.
[3696.94 → 3698.30] It was way too much work.
[3698.36 → 3699.30] I don't know what we were thinking.
[3699.66 → 3700.28] It was worth it.
[3700.44 → 3701.68] We had great ambitions, you know.
[3701.74 → 3703.10] It's always good to have good ambitions.
[3703.34 → 3705.72] But it's okay to admit your fail, right?
[3705.80 → 3707.22] You know, we just didn't quit soon enough, Gerhard.
[3707.26 → 3708.86] We just kept going for years.
[3708.86 → 3711.50] We had like the ultimate limp for many years.
[3712.28 → 3712.32] Right.
[3712.32 → 3718.94] Well, so when you're dedicated to consistency, it's hard to stop something and do something different.
[3719.06 → 3723.80] Because like one of your major aims is to consistently do the thing that you said you're going to do.
[3724.32 → 3729.22] And so, yeah, stopping and starting and making changes, these are hard decisions to make.
[3729.42 → 3732.28] And especially when they require heavy lifting, you know.
[3732.44 → 3733.42] And you're experimenting.
[3733.60 → 3735.20] We didn't know if people would like change log news.
[3735.46 → 3739.92] So we started shipping it inside our current infrastructure.
[3739.92 → 3745.22] You know if we had done all that work and then people were like, this show sucks.
[3745.42 → 3746.24] Why are you guys making?
[3746.32 → 3748.78] Please stop putting this into my change log feed.
[3748.98 → 3750.56] Then it would have been a bunch of wasted effort.
[3750.74 → 3753.50] So I feel like we went in the right order at least.
[3753.66 → 3754.50] And we're here now.
[3754.58 → 3756.44] There are a lot of things that we can improve.
[3756.68 → 3761.26] And we are dedicated to consistency on Kaiden every two months.
[3761.36 → 3766.72] So we won't have an episode number quite as sweet as every 10th like Gerhard had on Ship It.
[3766.76 → 3768.74] But we do want to do every two months.
[3768.74 → 3772.02] And we do have this discussions thread.
[3772.20 → 3773.54] So Gerhard, lay this out for folks.
[3773.96 → 3776.04] You can participate in our Maidens.
[3776.50 → 3781.66] You can give us ideas of things you want us to try, things you want us to talk about on these episodes.
[3782.30 → 3787.58] You can obviously hop into the code and find your way where it makes sense and how you can help out.
[3787.66 → 3788.48] Take it as shout-outs.
[3789.22 → 3793.04] We even have our most popular change log t-shirt is the Kaiden t-shirt.
[3793.04 → 3796.46] I wore it at Open Source Summit and got some compliments.
[3797.20 → 3800.24] So maybe you can get yourself a Kaiden shirt by getting involved.
[3800.80 → 3807.98] But each Kaiden episode has a discussion that we use on GitHub.com slash the changelog slash changelog.com.
[3808.98 → 3810.50] And hop in there.
[3810.68 → 3812.92] Tell us what we should do for Kaiden 11.
[3813.34 → 3816.10] We will be in there discussing what we're going to work on for Kaiden 11.
[3816.10 → 3818.44] And what else?
[3818.54 → 3819.70] Anything else left to say here?
[3820.18 → 3822.22] I would like to give a shout-out to Jason Bosco.
[3822.44 → 3825.66] He's the one that participated in Kaiden 10 with Type Sense.
[3826.14 → 3826.76] Thank you, Jason.
[3827.08 → 3829.40] Our partners Type Sense, they are powering our search.
[3829.82 → 3831.50] And we had some questions around how it worked.
[3831.90 → 3834.76] Sounds like it's working as advertised, at least at the basic integration.
[3835.40 → 3839.68] The key answer, direct matches will beat fuzzy matches every time, I guess.
[3839.94 → 3840.60] Makes sense.
[3840.60 → 3845.12] It's just unfortunate because LLMs versus LLM was the search term for using.
[3845.24 → 3849.48] And you tend to search for one, not the other, even though you tend to say the other one because there's many of them.
[3849.98 → 3852.88] So yeah, thanks, Jason, for hopping in there and explaining that to us.
[3853.24 → 3854.08] It's a great example.
[3854.40 → 3856.26] We can certainly delete the Algeria code.
[3856.82 → 3858.92] So if someone wants to help with that, it's right there.
[3859.30 → 3861.50] Well, I already deleted the account and everything.
[3861.72 → 3862.72] So we have no account there.
[3862.80 → 3864.16] So if the code's still there, then...
[3864.16 → 3866.08] I thought the Algeria code was all gone.
[3866.52 → 3867.12] What's left?
[3867.38 → 3867.72] Was it?
[3867.78 → 3868.14] I don't know.
[3868.14 → 3869.54] I mean, that's what it says, April 9th.
[3869.54 → 3871.34] Oh yeah, I ripped out some Algeria stuff.
[3871.56 → 3871.82] Did you?
[3871.94 → 3872.08] Okay.
[3872.22 → 3872.72] So that's done.
[3872.86 → 3873.00] Cool.
[3873.14 → 3873.36] Yeah.
[3873.76 → 3874.72] See, no pull requests.
[3874.90 → 3875.40] I don't know.
[3875.96 → 3876.90] So it's a commit.
[3877.38 → 3878.12] One of 50.
[3878.96 → 3879.96] Good luck finding it.
[3880.36 → 3883.78] I'm a follower of that gardening principle, you know, like whatever area of the code base
[3883.78 → 3886.14] you're in, you do the same thing with upgrades and stuff.
[3886.22 → 3890.54] Like while I'm working on this, if I see something, I'm like, oh yeah, we can get rid of that.
[3891.04 → 3891.74] I just do it.
[3891.88 → 3892.56] Boy Scout rule.
[3892.56 → 3897.20] I don't have the PR, but I'm just like constantly improving any area of the code base that I'm touching.
[3897.20 → 3902.24] And once it became clear that we were done with Algeria, and I was just fuzzing with the
[3902.24 → 3903.58] search stuff, I deleted it.
[3903.82 → 3909.88] So the cool thing I want to plug real quick, because Jason did so cool and Kaiden 10s mentioned
[3909.88 → 3912.80] there, if you're not familiar with Type Sense, the cool thing about Type Sense really is it's
[3913.40 → 3915.48] superfast in memory search.
[3915.48 → 3919.40] So like if you can hold a terabyte of your data in memory, like Jason can speak better
[3919.40 → 3919.80] than I can.
[3919.86 → 3924.50] I'm speaking out of turn really, but superfast, and it's in memory, which is just the
[3924.50 → 3924.74] best.
[3925.02 → 3927.14] So you should check it out if you don't know about it.
[3927.24 → 3928.28] TypeSense.org.
[3929.18 → 3930.32] Well, what's next?
[3930.72 → 3931.68] Where should we go from here?
[3931.72 → 3938.84] This is the first official changelog and friends, which is a brand-new flavour of this show.
[3938.84 → 3943.34] And Jared, I'm excited about this because we've got lots of friends, and we don't talk
[3943.34 → 3944.34] to them frequent enough.
[3945.16 → 3947.74] And every two months we're coming back here with you, at least, Gerhard.
[3947.84 → 3948.54] So maybe sooner.
[3949.18 → 3951.04] I know we have some Home Lab material coming up.
[3951.08 → 3956.08] We want to talk about Unify, Ubiquity, networking, maybe some Plans.
[3956.12 → 3957.46] I'm trying to talk Jared into Plans.
[3957.52 → 3959.00] He's like, I don't want to do that.
[3959.12 → 3960.26] Should I have Plans, Gerhard?
[3961.28 → 3962.92] You should, especially for your kids.
[3963.46 → 3965.02] You should have a kids network.
[3965.34 → 3966.64] I found it the hard way.
[3966.64 → 3968.42] That's exactly what Adam's telling me.
[3968.58 → 3970.36] I think that needs a drink, that story.
[3970.68 → 3970.96] Yep.
[3971.28 → 3973.38] Have a separate Wi-Fi for kids that's on the kids.
[3973.38 → 3973.68] Oh, yeah.
[3973.76 → 3974.20] VLAN.
[3974.58 → 3974.98] Okay.
[3975.28 → 3975.98] And IoT.
[3976.32 → 3978.40] Yeah, you want like an IoT network for sure.
[3978.84 → 3979.14] Yep.
[3979.38 → 3979.78] Okay.
[3980.40 → 3980.86] Sell me.
[3981.02 → 3981.90] You want two networks.
[3984.06 → 3984.50] Yes.
[3984.50 → 3985.82] Yes, always two.
[3985.96 → 3988.58] Two routers, two networks, two ISPs.
[3988.94 → 3989.28] Oh, yeah.
[3989.54 → 3993.62] You know how hard it was for me to get one ISP out here in the boondocks?
[3994.06 → 3995.60] Getting two is not easy.
[3995.60 → 3996.60] I'm sure it was.
[3996.96 → 3997.14] Yeah.
[3997.62 → 3998.60] No Starlink?
[3999.56 → 4000.92] I could have Starlink.
[4001.06 → 4001.56] Yeah, I suppose.
[4002.04 → 4004.02] But that's expensive, right?
[4004.10 → 4006.16] 500 bucks down and then 100 bucks a month?
[4006.28 → 4009.60] It's like 700-ish dollars in just hardware alone.
[4009.76 → 4013.18] And then it's about 100 bucks a month, I want to say, for decent speeds.
[4013.52 → 4014.16] As a backup?
[4014.70 → 4015.90] Can I turn it off and turn it on?
[4016.30 → 4017.24] I don't think so.
[4017.60 → 4018.02] Doubt it.
[4018.20 → 4019.26] That's too much for backup.
[4019.42 → 4021.10] My main line's costing 115.
[4021.10 → 4025.26] That would be cool, actually, if they can have a plan that's just for backup service.
[4025.26 → 4027.64] Because, I mean, you already own the hardware.
[4027.86 → 4028.18] Right.
[4028.32 → 4030.38] How hard is it to just metered use?
[4030.64 → 4030.84] Right?
[4030.92 → 4031.28] Failover.
[4031.72 → 4035.86] I don't know if your Dream Machine Pro supports it, but I don't think that has WAM failover.
[4036.56 → 4037.50] Does it have WAM failover?
[4037.78 → 4038.08] Yeah.
[4038.20 → 4039.42] Dream Machine Pro has it, yeah.
[4039.64 → 4040.52] It does have WAM failover.
[4040.52 → 4045.70] I know my USD Pro did, and I say did because I used to own that, and I sold it like a fool.
[4046.44 → 4048.08] I want that USD Pro back so bad.
[4048.14 → 4048.68] It's so cool.
[4049.56 → 4051.46] The UDM Pro's pretty cool, too, but...
[4051.46 → 4052.52] Unify has...
[4052.52 → 4054.74] Is it Unify as the company or is that the device?
[4055.00 → 4055.34] I always forget.
[4055.34 → 4056.18] Ubiquity's the company.
[4056.44 → 4058.08] Unify is the product level.
[4058.52 → 4059.66] Oh, Ubiquity's the company.
[4059.84 → 4060.74] Ubiquity's the company.
[4061.78 → 4064.62] They do live at UI.com, though, which is like...
[4064.62 → 4066.74] Yeah, UI.com is a sweet domain, right?
[4066.86 → 4067.50] Phenomenal domain.
[4067.98 → 4070.02] So they have a product that I really want.
[4070.02 → 4071.60] So, you know, I have a small acreage.
[4071.66 → 4072.52] I got eight and a half acres.
[4072.96 → 4073.82] Do you really want that still?
[4074.22 → 4074.78] Of course.
[4074.94 → 4075.26] You do?
[4075.36 → 4075.62] Okay.
[4076.08 → 4076.74] Why wouldn't I?
[4077.40 → 4079.02] Wasn't sure if this was a long-term thing.
[4079.30 → 4080.80] Oh, I still want it, so...
[4080.80 → 4081.30] What do you want?
[4081.30 → 4083.68] Wi-Fi Base Station KG.
[4084.42 → 4091.44] It's an outdoor, basically, dish that just broadcasts your Wi-Fi for hundreds of miles.
[4091.66 → 4091.74] No.
[4092.28 → 4095.28] 1,500 plus, 5,000 square foot coverage.
[4095.28 → 4100.74] So, one of the things that I do around my land is that I walk, and I listen to our shows
[4100.74 → 4102.44] for QA, for clipping, for stuff like that.
[4102.94 → 4104.42] And sometimes I'm uploading stuff.
[4104.54 → 4108.20] I'm basically working and walking, which is a spectacular aspect of what we do.
[4108.26 → 4109.60] I love that part of the job.
[4110.22 → 4113.22] I get down to the orchard and I don't have Wi-Fi.
[4113.36 → 4114.10] I'm on cellular.
[4114.72 → 4116.36] I want blanket coverage.
[4116.36 → 4118.60] I want Wi-Fi all over my land.
[4119.10 → 4121.12] And this sucker will get me there.
[4121.38 → 4122.18] The Wi-Fi Base Station.
[4122.32 → 4124.26] The problem with it, A, it's sold out.
[4124.58 → 4125.94] B, it's 1,500 bucks.
[4126.72 → 4128.78] But it's powered over POE.
[4129.56 → 4131.16] And I can run it up to my roof.
[4131.44 → 4134.12] I think you'd probably go with the AC Mesh Professional, though, too.
[4134.18 → 4136.50] That might do a similar thing.
[4136.58 → 4136.82] All right.
[4136.94 → 4137.52] Is that one cheaper?
[4137.82 → 4138.46] Check this out.
[4138.74 → 4139.16] Oh, gosh.
[4139.22 → 4141.14] Check the wireless systems that Microtech has.
[4141.44 → 4141.88] Microtech?
[4142.08 → 4143.52] Garrett is sharing links with us.
[4144.00 → 4144.60] I have both.
[4144.60 → 4145.50] Of course you do.
[4145.50 → 4146.62] You have two.
[4146.92 → 4147.36] Of course.
[4147.60 → 4147.74] Yeah.
[4148.46 → 4149.76] Ubiquity and Microtech.
[4150.40 → 4151.68] So I have a UDM Pro.
[4151.78 → 4152.90] I basically have like two networks.
[4153.16 → 4155.08] One inside the other and one alongside the other.
[4155.88 → 4157.48] So they are like interweaved.
[4157.60 → 4159.86] So I have like two 10G trunks, basically.
[4160.66 → 4161.82] 10 gigabit trunks.
[4162.36 → 4164.58] And I really like the Microtechs.
[4165.12 → 4167.58] I think they are underappreciated.
[4167.68 → 4169.96] You need to be a bit of a hacker to get into them.
[4170.30 → 4172.90] But once you set it up, you have terminal access.
[4172.90 → 4175.54] You have like nice auto-completion on the shell.
[4176.08 → 4178.28] You can run containers if you're crazy enough.
[4178.28 → 4181.20] But you can run containers natively on the router if you want to.
[4181.26 → 4182.18] They have container support.
[4182.48 → 4183.94] It's a proper operating system.
[4184.48 → 4187.54] And if you use Ubiquity, it's great.
[4187.66 → 4188.62] It's almost like a Mac.
[4189.08 → 4190.30] Microtech is almost like Linux.
[4190.46 → 4191.26] So that's the difference.
[4191.52 → 4192.06] Oh, okay.
[4192.06 → 4195.52] But however, like some like their latest hardware is just so good.
[4195.74 → 4196.54] So, so good.
[4196.96 → 4198.62] The UI will not be as polished.
[4198.74 → 4199.60] But do you need that?
[4199.66 → 4203.30] Or do you want the stability of just think Linux for your network?
[4203.60 → 4205.58] You can do 25 gigabits.
[4205.64 → 4206.66] You can do SFP.
[4206.78 → 4208.12] You can do like all sorts of crazy things.
[4208.36 → 4211.62] If there are good docs and there's an LL in to power it, I would totally configure it.
[4211.68 → 4212.50] Like NetAppApply.
[4212.68 → 4215.44] I configure my static stuff on Linux every day.
[4215.92 → 4217.18] No GUIs here, you know.
[4217.30 → 4218.52] So cool with that.
[4218.52 → 4221.38] Their YouTube channel lately, it's just so good.
[4221.38 → 4225.18] If you look like the YouTube Microtech channel, they have so much good content.
[4225.88 → 4226.32] Check it out.
[4226.66 → 4227.70] Yeah, definitely have to check it out.
[4227.80 → 4229.02] That's a friend recommendation.
[4229.94 → 4230.18] Okay.
[4230.94 → 4232.12] Well, that'll just be a tease then.
[4232.18 → 4235.32] So what I was really trying to do is just tease what could be the future of this show.
[4235.42 → 4238.26] Like, you know, having friends like you to come up and talk with us about things.
[4238.56 → 4246.50] And I'm a nerd, and I'll nerd out with Jared, and he's maybe slightly less of a nerd than I am on networking and IoT and home lab-y stuff.
[4246.50 → 4251.98] But way nerdier than I am in backend coding and databases and stuff.
[4252.16 → 4255.50] It feels nice to be in a place where I'm the least nerdy person.
[4256.28 → 4260.48] You know, it's usually I'm the most nerdy of all people in the room, but not in this room.
[4260.68 → 4261.48] I like this room.
[4261.86 → 4262.28] Not in this room.
[4263.06 → 4269.68] Maybe we could talk about Microtech and Unify and the Mac versus Linux of networking.
[4269.78 → 4270.38] That'd be kind of cool.
[4270.38 → 4273.48] Coming to a changelog and friends near you in the future.
[4273.68 → 4274.36] Okay, cool.
[4274.60 → 4282.18] We do have a little list here at the very end of this discussion, which says what else is coming up?
[4282.22 → 4286.70] Can you blaze through that in one minute, Gerhard, so we can close out this show and tease next, Kaiser?
[4287.12 → 4294.02] So I really think we should improve our integration with 1Password and secrets in general, right?
[4294.06 → 4298.06] Because right now it's copy pasta in our GitHub actions.
[4298.12 → 4298.80] And that's not good.
[4298.80 → 4304.44] Now we have the code, we can connect programmatically to wherever we store our secrets nicely
[4304.44 → 4308.22] and get them just in time and keep them secret throughout, right?
[4308.30 → 4310.74] Like no copying and pasting, none of that stuff.
[4311.74 → 4315.52] We switched off Kingdom, and now we have Honeycomb, just Honeycomb.
[4315.64 → 4319.30] So we need to configure the Los, just have a better understanding of what's happening there.
[4319.60 → 4325.06] I have Uptime Kumar running locally, and I think we should have an instance on Fly.io as well,
[4325.10 → 4326.08] at least like a few.
[4326.08 → 4330.62] You know, just like deploy them, see what's happening from the outside world.
[4331.14 → 4335.70] There are a bunch of upgrades like PostgreSQL that has to be upgraded.
[4336.22 → 4339.92] Apps v2, like role, everything that we can to Apps v2.
[4340.72 → 4348.08] Follow up with the Vastly guys, just like to share our VCL madness and our UI experience and
[4348.08 → 4351.80] just figure out what exactly we're doing wrong when it comes to Vastly.
[4351.80 → 4355.52] On my list, part of that is to look into Cloudflare.
[4355.88 → 4361.00] Like what did Cloudflare add to logs and how easy it is to integrate with Honeycomb?
[4361.10 → 4364.16] Because if they have a good logging story, maybe we should check them out.
[4364.66 → 4366.84] R2 has no egress fees.
[4367.36 → 4369.60] Currently, we're storing stuff on AWS S3.
[4369.80 → 4374.00] If we went to Cloudflare R2, if we did like a couple of things, I have like some amazing stuff
[4374.00 → 4375.92] like Cloudflare, a bunch of things.
[4375.92 → 4380.04] They are a really cool company in terms of the technology which they develop.
[4380.70 → 4382.88] And as you know, I like running two of everything.
[4383.06 → 4384.28] So why not two CDNs?
[4384.40 → 4389.96] I know it's crazy, but you know, many things were crazy to begin with, and they turned out
[4389.96 → 4390.84] to be great ideas.
[4391.00 → 4392.94] I'm one step ahead of you on the R2 thing.
[4393.02 → 4394.06] I have an open tab.
[4394.14 → 4397.22] I have an account that I've created for us over there.
[4397.34 → 4399.44] I begin testing the waters.
[4399.56 → 4403.98] One thing that I immediately don't like about it is that it doesn't support transmit.
[4403.98 → 4410.56] Like it's S3 compatible API, but not enough that you can use your S3 client transmit,
[4410.68 → 4411.72] my S3 client transmit.
[4411.98 → 4413.30] And that just hurts my heart.
[4413.42 → 4415.78] It's not going to be a blocker, but it hurts my heart.
[4415.96 → 4417.90] So it's going to be an R2 CLI though, right?
[4417.90 → 4420.74] Where you could do the same thing that transmit gives us with the CLI?
[4421.00 → 4422.26] Oh, there's definitely ways you can do it.
[4422.28 → 4423.82] You can use Cyberdeck if you want to.
[4423.94 → 4426.16] Just like years and years of using transmit.
[4426.82 → 4430.64] Technically, transmit doesn't support it is probably the way that they would say it.
[4430.96 → 4432.70] But they say they're S3 API compatible.
[4432.70 → 4435.32] And transmit is an S3 client, but it does not work.
[4435.56 → 4437.42] Their S3 does not work with R2.
[4437.52 → 4438.50] So it's not a one-for-one.
[4438.60 → 4441.82] It has something to do with streaming data versus chunked uploads.
[4441.92 → 4442.30] Or I don't know.
[4442.38 → 4443.34] I didn't read the description.
[4443.52 → 4446.60] But it's like a known thing that transmit is like, yeah, we might add support.
[4446.74 → 4447.68] But they haven't yet.
[4448.00 → 4451.86] So anyway, that just bugged me because I just like to drag and drop stuff in there
[4451.86 → 4455.14] with the same SFTP client I've used forever.
[4455.14 → 4462.14] But what really needs to happen is can we simply change all the environment variables in our code?
[4462.54 → 4465.34] And will the X AWS work seamlessly?
[4465.88 → 4468.92] Will all of our stuff work seamlessly with R2 to upload to R2?
[4469.42 → 4472.36] And if that works, then we're pretty much good to go.
[4472.44 → 4481.00] I also need to go through and change a bunch of our hard-coded URLs in our text areas from the S3 URLs over to CDN.ChangeLog.com,
[4481.00 → 4482.22] which we should have been using the whole time.
[4482.28 → 4483.84] I just didn't even think about that.
[4484.24 → 4487.14] Because then we could seamlessly switch the back end without changing anything.
[4487.28 → 4489.32] So that's like a migration step that will have to happen.
[4489.48 → 4494.50] But anyway, I'm down the road a little bit on that because our fees at AWS are going up.
[4494.98 → 4497.26] And we would love to have zero egress fees.
[4497.26 → 4503.32] I was going to say, if we need some motivation, in March our bill was $50, $53.69, actually.
[4504.28 → 4509.32] And here in May 2nd, and June's coming here soon, May 2nd it's $132.32.
[4509.32 → 4512.48] So we've almost tripled our bill in three months.
[4512.98 → 4515.76] Yeah, it's on track for like $450 this month.
[4515.90 → 4516.38] Is it really?
[4516.80 → 4518.44] I thought so, inside the Cost Explorer.
[4518.74 → 4519.64] $450 this month?
[4520.10 → 4522.50] You said May 2nd, it was $150 something.
[4522.68 → 4523.38] I have to check this out.
[4523.46 → 4525.78] Remember we did this last time when we set up shielding?
[4525.94 → 4527.36] That was exactly like during a Kaiden.
[4527.56 → 4529.86] So I have to check this out to see what exactly is going on here.
[4530.14 → 4532.08] I used the Cost Explorer to try to figure it out.
[4532.16 → 4533.28] And I just saw it was S3.
[4533.72 → 4536.18] But I didn't actually drill down on what changed and when.
[4536.18 → 4539.08] So if you want to do a little bit of research on that, you're hard to be good.
[4539.08 → 4541.46] But then I just started thinking, well, now is the time.
[4541.56 → 4541.88] R2.
[4542.04 → 4544.44] Let's just eliminate this problem for us.
[4544.96 → 4546.20] So that's on my hit list.
[4546.46 → 4550.50] Also on my hit list, obviously, is this clustering stuff with the caching stuff.
[4551.52 → 4553.28] Changelog news improvements will continue.
[4553.94 → 4559.04] And then my big, not for the next Kaiden, but my very big desire this year,
[4559.10 → 4562.20] this calendar year, I'm not going to guarantee it, but I'm going to shoot for it,
[4562.20 → 4564.66] is I want to migrate off Superfast.
[4564.90 → 4569.52] And I want to provide a first-party Changelog++ offering
[4569.52 → 4573.50] that solves a few of the pain points for our++ members.
[4573.88 → 4577.46] Specifically, one feed to rule them all is just not good for people.
[4577.68 → 4578.86] They don't want one feed.
[4578.98 → 4584.16] They want their++ feed, but not the master feed, which it currently is.
[4584.16 → 4587.22] And so we can provide that if we're off Superfast.
[4587.58 → 4592.10] And so that's just a thing I'm putting out there as a big item for me here soon.
[4592.68 → 4595.14] That would be good because they want it.
[4595.44 → 4596.32] Got to give them what they want.
[4596.50 → 4596.90] They do.
[4597.24 → 4599.72] It's like 50% of the people who sign up for++ say,
[4599.84 → 4603.20] hey, can I have just JS Party or just the Changelog and JS Party?
[4603.26 → 4605.08] I don't want the other shows.
[4605.54 → 4608.20] And I always have to say, nope, you got to have all of them.
[4608.20 → 4610.24] And that just sucks to say because I understand it.
[4610.52 → 4614.30] So unfortunately, Superfast doesn't have that functionality inside there.
[4614.34 → 4615.78] We can only give them one feed.
[4616.16 → 4618.22] Whereas once we're on our own platform,
[4618.22 → 4621.22] obviously everybody gets their own feed, and you can customize it
[4621.22 → 4623.80] and have multiples or whatever you want to do.
[4623.90 → 4624.94] So that'll be super nice.
[4625.88 → 4628.08] We've proved it enough, though, that it makes sense to bring inside.
[4628.26 → 4630.86] But also it requires some of this caching stuff to be taken care of.
[4630.98 → 4631.48] It does.
[4632.12 → 4637.00] It's just there are so many little things with subscription services
[4637.00 → 4640.52] and like Stripe integration and blah, blah, blah, blah,
[4640.64 → 4644.08] where you start to realize all the emails you're going to have to send.
[4644.64 → 4646.10] That is true, at least a few.
[4646.52 → 4648.22] I mean, there's probably five or six different emails
[4648.22 → 4649.74] just to manage a subscription.
[4650.22 → 4653.20] Plus a dashboard where you can go and change things,
[4653.74 → 4656.62] cancellations, this person's card expired.
[4657.44 → 4657.88] Refunds.
[4658.24 → 4658.64] Refunds.
[4659.12 → 4661.04] Yeah, Stripe handles the refunds part.
[4661.78 → 4662.18] Yeah.
[4662.76 → 4663.76] You still got to trigger it, though.
[4663.82 → 4665.48] You got to get that UI to do something or other.
[4665.48 → 4669.32] You got to just manage the fact that either you're doing it as an admin
[4669.32 → 4671.90] or they're doing it on, they're requesting something.
[4672.46 → 4673.76] Then they're like, where's support?
[4673.94 → 4674.86] We don't have support.
[4674.98 → 4675.52] This is just.
[4676.20 → 4676.88] You're looking at it.
[4677.12 → 4678.30] Yeah, this is support right here.
[4678.74 → 4678.90] Yeah.
[4679.50 → 4683.84] You're figuring out why our bill went from basically 30 bucks to 130 bucks.
[4684.12 → 4686.86] As soon as I get permissions to billing, I'll have a look into that.
[4688.38 → 4689.48] Back on you, Adam.
[4689.60 → 4689.76] All right.
[4689.78 → 4690.26] Oh my gosh.
[4690.32 → 4690.62] Okay.
[4690.86 → 4691.58] One more thing.
[4691.66 → 4692.32] This is important.
[4692.32 → 4698.86] How can we run multiple instances of a changelog with the same data without the second instance
[4698.86 → 4703.26] behaving as like the live one, without sending any emails, without anything like that?
[4703.62 → 4710.08] Because when I'll be setting up the new 2023 infrastructure, and that is right next on my
[4710.08 → 4713.96] list, that starts with PostgreSQL, with the app, with whatever we can migrate.
[4713.96 → 4719.70] I do like a long blue-green, and that means getting another production and having like
[4719.70 → 4722.96] a nice, easy way of basically migrating data, migrating everything.
[4723.12 → 4725.96] So it's like very easy to switch back and forth if we need to.
[4726.38 → 4730.72] But always my concern has been when you have a second production, it shouldn't be sending
[4730.72 → 4732.20] any emails or anything like that.
[4732.46 → 4732.60] Right.
[4732.72 → 4733.92] I think that's a follow-up for us.
[4734.00 → 4736.46] Obviously, we don't have to solve it now, but that's something on my mind.
[4736.74 → 4737.84] We're getting long in the tooth.
[4737.94 → 4738.92] Let's call this a Kaiden.
[4739.10 → 4741.50] Let's call this a changelog in friends.
[4741.50 → 4743.22] I'm very happy to have been here.
[4743.48 → 4746.28] Thank you very much for having me over, and I'm looking forward to the next one.
[4746.46 → 4746.92] Thank you.
[4747.30 → 4748.26] Thanks for hanging with us.
[4748.44 → 4748.76] Kaiden.
[4749.06 → 4749.38] Always.
[4749.52 → 4749.82] Kaiden.
[4750.40 → 4751.06] Kaiden always.
[4756.60 → 4759.60] If you're digging changelog in friends so far, tell your friends.
[4760.14 → 4762.82] And if you have feedback for us, let us know in the comments.
[4763.38 → 4764.62] Link is in your show notes.
[4765.22 → 4767.56] Our intro episode sparked a great discussion.
[4767.92 → 4768.16] Wow.
[4768.64 → 4769.70] So many shower listeners.
[4769.70 → 4772.70] I knew I was right, but I didn't know just how right I was.
[4773.72 → 4776.28] Thanks once again to our partners for supporting our work.
[4776.82 → 4780.66] Fastly.com, fly.io, and typesense.org.
[4781.14 → 4784.14] And to Break master Cylinder for this epic new outro track.
[4784.42 → 4787.80] It's called Cinerama, and you'll only hear it right here on Changelog.
[4788.18 → 4795.04] Monday is Apple's big WWDC keynote, and they're expected to unveil the Reality Pro and PROS.
[4795.04 → 4800.06] Watch along with us in the Apple Nerds channel of our community Slack, and tune in next Friday.
[4800.44 → 4804.46] We'll be discussing all the interesting bits with homebrew lead maintainer, Mike McQuaid.
[4804.92 → 4807.82] That's all for now, but let's talk again real soon.
[4807.82 → 4808.84] Game logging in.
[4808.84 → 4809.26] Big Ed.
[4809.26 → 4810.96] Ingo.
[4810.96 → 4811.16] Game Log.
[4811.16 → 4812.78] Game Log.
[4813.14 → 4813.98] Game Log.
[4814.04 → 4814.42] Game Log.
[4814.42 → 4814.80] Game Log.
[4814.94 → 4815.06] Game Log.
[4815.06 → 4815.10] Game Log.
