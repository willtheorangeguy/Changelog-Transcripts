[0.08 → 6.06] You are listening to Ship It, a podcast about operations, infrastructure, and the people
[6.06 → 7.86] that keep all those lights blinking.
[8.58 → 13.56] I'm your host, Gerhard Lazy, and this is our third Kaiden with Adam and Jared.
[14.00 → 19.90] We combine all our learnings from the previous 10 episodes, ship them in changelog.com, and
[19.90 → 21.72] see if they make things better.
[22.26 → 27.14] Today, we talk about how we're adding Git Ops the wrong way, asking questions with Honeycomb
[27.14 → 32.10] and realizing that we must be holding our CDN wrong, and Jared tells us about the work
[32.10 → 37.96] that he has been doing to move all our static files from regular volumes to an S3-like object
[37.96 → 38.26] store.
[38.58 → 43.38] If you like a good yak shave, listening to this one is a lot more fun than doing it.
[43.78 → 48.18] The thing which I'm most excited about are the Christmas gifts that we have been preparing
[48.18 → 48.60] for you.
[49.04 → 54.04] While GitHub Code spaces is not going to be part of the upcoming Christmas special, today we
[54.04 → 56.54] talk why we must invest in a Code spaces integration.
[56.54 → 60.42] Changelog 459 and Backstage 20 are related.
[60.92 → 64.38] Big thanks to our partners Vastly, Launch Darkly, and Linde.
[64.70 → 66.42] Thank you for the great bend with Vastly.
[66.76 → 68.60] You can learn more at Fastly.com.
[69.08 → 73.34] Ship new features with confidence by getting your feature flags powered by LaunchDarkly.com.
[73.68 → 76.88] And thank you Linde for keeping our Kubernetes fast and simple.
[77.30 → 81.12] Run your setup as we do via linode.com forward slash changelog.
[86.54 → 88.18] What's up shippers?
[88.32 → 91.64] This episode is brought to you by our friends at Fly.
[92.08 → 96.10] Fly lets you deploy your apps and databases close to your users in minutes.
[96.38 → 103.88] You can run your Ruby, Go, Node, Dino, Python, or Elixir app and databases all over the world.
[104.06 → 104.86] No ops required.
[104.92 → 108.00] Fly's vision is that all apps should run close to their users.
[108.00 → 112.92] They have generous free tiers for most services so you can easily prove to yourself and your team
[112.92 → 116.10] that the Fly platform has everything you need to run your app globally.
[116.52 → 121.16] Learn more at fly.io slash changelog and check out the speed run and their excellent docs.
[121.56 → 124.90] Again, fly.io slash changelog or check the show notes for links.
[124.90 → 132.00] We are going to ship in 3, 2, 1.
[145.62 → 148.72] So we're back for the third Kaiden.
[149.46 → 152.40] I can't believe it's been 30 episodes, and I'm not the only one.
[152.40 → 155.84] Adam can't believe either that it's been 30 episodes of Ship It.
[156.14 → 156.40] Yeah.
[157.20 → 158.26] It really is insane.
[158.44 → 162.36] I mean, this was just, this show was just an idea recently.
[163.36 → 174.18] And that's, I think, I think anybody who makes things come to life from nothing is always flabbergasted by the creation, I suppose, once you sort of get into it.
[174.20 → 177.24] But podcasting is a little different because it really is a journey.
[177.78 → 181.14] It's a journey pre-production, and it's a journey post-production.
[181.14 → 183.96] Now we're obviously post-production 30 episodes in.
[184.32 → 187.70] And I think it's just kind of crazy looking back thinking like this was just an idea.
[188.34 → 192.00] And then in particular, the podcast, the impact to us and to the audience.
[192.00 → 193.96] And I think that's just, that's why I love it.
[194.08 → 194.66] That's why I love the game.
[195.48 → 195.64] Yeah.
[195.84 → 197.76] I mean, we shipped it, right?
[197.80 → 198.48] It took us a while.
[198.58 → 201.56] It took us five months to ship the first episode, the first three episodes.
[201.56 → 203.44] And then it was like a roll.
[203.44 → 207.98] What blows my mind is that my mind is on episode 40.
[208.52 → 210.66] And most people don't realize this.
[210.96 → 213.98] Like the next five episodes are pretty much like locked in.
[214.96 → 217.48] The guests, the topics, the flow.
[217.80 → 221.86] And even the five ones after that are like, you know, nebulous.
[222.02 → 224.78] Nothing locked in for real, but it's coming.
[224.78 → 229.08] So for me, it's even like more mind-blowing because I'm already like in February.
[229.30 → 230.70] I'm thinking February right now.
[231.70 → 232.14] Yeah.
[232.16 → 233.04] You just live in the future.
[233.14 → 239.80] I think you might be the most prepared and scheduled out podcaster in the entire universe, Gerard.
[241.42 → 241.86] Okay.
[242.48 → 245.62] I'm happy that I got scheduled out through December.
[246.12 → 247.60] But you're, no, it is.
[248.52 → 249.12] Thank you.
[249.12 → 255.10] I mean, I don't want to like, I don't want to like leave myself open to like, you know, unique encounters and like, you know.
[255.18 → 255.94] Yeah, that's the challenge.
[256.42 → 258.56] Serendipity is taken out and when you're scheduled out.
[259.34 → 260.46] That is a great word.
[260.56 → 261.46] I haven't heard it in a while.
[261.60 → 263.40] I was, I thought I was the only one using it.
[264.90 → 265.26] Okay.
[265.74 → 267.06] That'd be a surprise and delight.
[268.54 → 268.90] Right.
[269.06 → 271.06] So, well, thank you very much.
[271.10 → 273.22] In which case, Gerard, I appreciate that.
[273.32 → 273.66] Thank you.
[273.66 → 281.36] And what I'm really excited about is, I don't think many people realize this, but there is like a theme to this.
[281.52 → 282.54] And there are like multiple themes.
[282.60 → 285.72] So like a couple of episodes, they kind of cluster together and there's a buildup.
[286.48 → 292.22] And a lot of the episodes that we had, like the last 10, 15 ones, they're leading to something.
[292.36 → 293.44] They're building to something.
[293.74 → 297.52] And that will be the Christmas episode, episode 33, which I'm very excited about.
[298.24 → 299.64] We'll come back to that a bit later.
[299.64 → 305.90] But one of the things which is on my mind is the incident too.
[306.18 → 312.12] I mean, our last episode 20, our last Kaiser episode 20 was all about incidents.
[312.56 → 314.20] We call it five incidents later.
[315.20 → 323.08] And there was something which I wanted to understand, which I didn't at the time, was why was an unhealthy pod put back into service?
[324.10 → 325.12] Do you remember that?
[325.62 → 326.32] I do remember that.
[326.60 → 327.64] We didn't have answers.
[328.26 → 328.50] Yes.
[328.50 → 332.02] So my answer is we're using the latest tag.
[332.42 → 342.20] What that means is that our, like, if something is unhealthy, and it has to go back to the previous one, it will use the latest tag.
[342.36 → 343.44] But latest has moved on.
[343.84 → 347.16] So it doesn't keep the old SHA, the one that was working.
[347.42 → 348.96] It always says the latest.
[349.34 → 354.12] So if you were to go back, then you always go back to the latest.
[354.26 → 355.62] And by the way, the latest has already moved.
[355.68 → 357.02] So that's like the broken version.
[357.02 → 360.28] Ah, so you're pointing back to the same version, which is broken.
[360.68 → 361.08] Exactly.
[361.80 → 362.20] Exactly.
[362.28 → 363.08] Why are we doing that?
[365.04 → 366.38] Some corners have been cut.
[366.38 → 373.22] The honesty, I love it.
[373.22 → 375.44] That worked well for quite some time.
[375.50 → 379.72] So I have to say that even though those corners have been cut, there was like a tradeoff to be made.
[379.86 → 381.52] It was like a conscious tradeoff.
[381.94 → 382.16] Yeah.
[382.16 → 384.02] And it only failed once.
[385.02 → 385.26] Right.
[385.30 → 387.20] So that tradeoff is like bit us once.
[387.82 → 387.90] Right.
[387.90 → 399.62] But I think it is high time that we revisit the whole Git Ops approach, the Git Ops approach that we have, but not really have to how we run our infrastructure.
[400.18 → 410.44] So while we do version all the manifests and everything is in the repo, and we apply them, some manifests reference like latest and latest can, you know, move.
[410.44 → 417.38] So we cannot, basically right now we don't capture everything we run at the SHA that we run.
[418.00 → 423.48] So Ingress Nginx, external DNS, we have versions for those, but for our app we have latest.
[423.90 → 427.08] The thinking goes, we always want to be running latest, right?
[427.08 → 428.72] Like when do you not want to run latest?
[429.26 → 430.76] Apparently when latest is broken.
[431.50 → 432.02] Exactly.
[432.46 → 433.92] One time when you definitely do not.
[433.92 → 434.56] That's when you don't want to run latest.
[435.14 → 440.58] So, but that's something that, yeah, we will, we will be investing in.
[441.00 → 445.04] I will be spending a bit, a bit of time on that among many other things.
[445.04 → 450.44] But that's, that explains this incident too, which I didn't have an explanation 10 episodes ago.
[450.76 → 452.86] How did you learn the how did you learn of this?
[452.86 → 458.44] Um, I looked at the manifest and I tried to understand what happens.
[458.58 → 467.48] So I went through the steps of what would happen or of what happens in Kubernetes when like the, the new one gets, gets put in service.
[467.70 → 468.74] It fails.
[468.98 → 470.80] The old one crashes.
[471.36 → 473.98] And when it gets restored, it gets restored with latest.
[475.02 → 476.84] So that's what happened.
[477.24 → 480.98] So my developer brain sees something like this and I think infinite loop.
[480.98 → 483.42] Is that going on here or does it just fail?
[483.54 → 485.78] Because if it runs latest, latest is broken.
[486.14 → 487.62] Runs latest, latest is broken.
[487.72 → 487.90] Yes.
[487.96 → 489.52] Does it just keep doing that over and over again?
[489.84 → 490.00] Yeah.
[490.18 → 495.06] So in our case, what happened was that the version that was running, that crashed.
[496.64 → 499.28] And because like, it's just meant to restore it, right?
[499.34 → 500.42] It crashes, not a problem.
[500.50 → 501.16] It'll come back.
[501.62 → 501.94] Right.
[502.76 → 507.00] But when it comes back, it doesn't know which version it should come back with because it has latest.
[507.00 → 512.68] And it resolves that when it boots and latest has moved along, which is where the problem comes from.
[513.70 → 519.16] So we need to capture the version of the app that we want to run.
[519.60 → 522.22] Often that the app, it's the app container image.
[523.06 → 525.86] Currently, because we use latest, that always changes.
[527.58 → 528.70] So, yeah.
[530.30 → 531.22] That's a challenge.
[531.36 → 533.86] It's always nice to get answers to mysteries.
[533.86 → 534.30] Yes.
[535.42 → 536.72] I love good mystery.
[537.82 → 539.42] Especially when I have an answer for it.
[539.76 → 541.06] Otherwise, it just drives me crazy.
[541.18 → 541.54] I hate it.
[541.68 → 543.14] Like, oh, what's the answer?
[543.64 → 549.02] It's like that show, Unsolved Mysteries, which I always avoided because, come on, give us the solution already.
[549.14 → 550.22] Have you guys ever watched that one?
[550.36 → 551.56] It was probably dead now.
[551.68 → 558.14] But back in the day, they would show these mysteries, and they're like, people who are actively being sought by FBI or whatever.
[558.88 → 559.78] There's no solution.
[559.88 → 562.64] At the end, they're like, if you know where this person is, please let us know.
[562.64 → 564.50] I want the solution.
[565.10 → 565.22] Yeah.
[565.30 → 565.50] Yeah.
[566.14 → 568.90] It's those shows that don't have endings, essentially, that get me.
[569.00 → 570.28] It's like, I can't watch that.
[570.56 → 571.74] It just drives me crazy.
[572.00 → 572.24] Yeah.
[572.82 → 573.06] Yeah.
[573.94 → 574.30] Okay.
[574.46 → 576.22] So what are we doing to solve this then?
[576.22 → 580.48] If latest can't be used, how do we uncut that corner?
[581.50 → 588.24] So, right now, we have Keyless, which basically watches the Docker image updates.
[588.24 → 591.58] And when there is an update, it will just basically update itself.
[593.00 → 597.06] But what we have in the deployment, it's also latest.
[597.36 → 601.18] So we need to use Git Ops properly.
[601.62 → 605.28] What it means is commit in the manifest, the version of the app that should be running.
[605.28 → 609.68] And that should automatically be applied, which is where Argo CD comes in or something like that.
[609.74 → 610.64] I'm thinking Argo CD.
[610.98 → 612.10] Maybe there will be something else.
[613.14 → 619.24] So basically, the infrastructure gets continuously reconciled with what is versioned in the repo.
[619.24 → 623.24] And what we versioned in the repo is the app updates.
[624.00 → 633.52] So when a new image is built, there will be a new push to the repo, a new commit to the repo, which has the exact version of the app that should be running.
[634.00 → 637.74] And there will be a reconciler, which will make sure that that is true.
[639.44 → 641.04] And that's currently what we don't have.
[641.04 → 643.56] So finish Git Ops.
[644.22 → 646.98] We're 90%, maybe 95% there.
[648.04 → 652.38] Because we versioned the manifests, but we don't update them when the app updates.
[652.68 → 655.46] And we don't apply them when the app updates.
[656.04 → 657.16] So that's what's missing.
[657.60 → 664.46] Is there like one place to learn exactly what the requirements are for Git Ops to comply, I suppose?
[665.52 → 667.58] You can search on Google, what is Git Ops?
[668.20 → 670.30] And there are a lot of pages that describe.
[670.30 → 673.52] I think GitOps.org is a good resource.
[674.28 → 678.44] That's the one that I would recommend for learning what Git Ops is.
[679.22 → 686.90] And in a few episodes, we'll have Alexis from WeWork's, where we'll be talking all about Git Ops.
[687.52 → 690.74] So GitOps.org doesn't resolve anything for me.
[691.24 → 693.66] GitOps.tech, that's the one.
[694.22 → 698.52] So this is what you would consider the canonical resource for learning about Git Ops, at least.
[698.52 → 701.38] It's going to link out to WeWork's.
[701.38 → 705.20] It's going to link out to a PDF, an EPUB book.
[705.26 → 707.00] So I guess this is a book, too.
[707.94 → 710.82] So last time when I've seen it, I've seen this has a few updates.
[711.56 → 712.90] I wasn't aware of the book.
[713.00 → 714.48] So that must be something new.
[714.66 → 717.32] It does say we've just released our short book on Git Ops.
[717.32 → 717.78] There you go.
[717.88 → 720.62] So that's a new element, which I wasn't aware of.
[721.08 → 726.56] If you scroll down, you see push-based deployments, pull-based deployments, which is what we have, by the way.
[726.62 → 728.02] We have a pull-based deployment model.
[729.84 → 733.64] And WeWork's were the one that coined the term of Git Ops.
[733.64 → 738.98] And this is the resource, like the canonical resource for me, at least, when it comes to Git Ops.
[739.72 → 739.96] Okay.
[740.14 → 741.20] So they have this graph down there.
[741.36 → 745.40] Sorry, this, what do you call those things?
[746.12 → 747.26] Infographic, I guess.
[747.80 → 748.16] Infographic.
[749.18 → 752.96] A graphic to look at, essentially outlining what...
[752.96 → 754.32] Is there information on the graphic?
[755.04 → 755.52] Say again?
[756.24 → 757.76] Does the graphic have information on it?
[758.10 → 758.30] Yes.
[758.30 → 759.24] It does have information on it.
[759.24 → 760.94] So that's a classic infography, then.
[761.14 → 761.54] That's right.
[761.94 → 767.20] It's really a graphic of what the flow is from application repository all the way to deployment.
[767.40 → 768.72] What should happen in there?
[768.78 → 774.50] So are you saying that we're somewhat adhering to this push-based deployment graph here?
[774.68 → 775.12] Yes.
[775.62 → 775.98] This idea?
[776.42 → 776.76] Yes.
[777.02 → 782.62] The difference is that in the pull-based deployment, there's an operator that observes the image registry.
[783.38 → 783.66] Right.
[783.66 → 786.46] And then updates the environment repository.
[786.46 → 793.52] The environment repository is basically which stores the config for everything that's running in an environment.
[793.94 → 795.76] So basically those will be our YAML manifests.
[797.30 → 798.64] Currently that doesn't happen.
[799.62 → 808.24] And the reason why this flow is prescribed is to prevent things like calling on latest when latest is broken.
[809.24 → 809.28] Okay.
[809.48 → 810.52] Or latest changes, right?
[810.52 → 811.72] Because you don't know what you're running.
[811.72 → 812.16] Right.
[812.16 → 815.74] So you're trying to capture your production as much as you can.
[815.98 → 818.16] Like not actually like not as much as fully, right?
[818.22 → 819.80] Like to the SHA, not even to the version.
[819.92 → 828.46] Because when you tag an image with a version like v1.1.0, you can update the tag to point to a different SHA.
[828.80 → 831.76] So you want to point to a specific SHA, which will not change.
[831.80 → 835.70] It's like a get SHA, but it's equivalent in container images.
[835.70 → 838.28] Which is what we would want.
[838.90 → 844.94] Which is important for, I suppose, like recovery from a disaster.
[845.14 → 848.16] Like so in this case, a disaster happened.
[848.78 → 848.88] Yeah.
[849.24 → 849.66] Implication failed.
[849.76 → 850.52] You needed to reboot.
[850.66 → 852.08] You rebooted, but you called upon latest.
[852.20 → 853.12] Latest wasn't right.
[853.28 → 853.58] And so.
[853.94 → 854.24] Yes.
[854.40 → 860.86] If you'd have had continuity in place, the operator would have told the environment repository which version was or which SHA to point too essentially.
[860.86 → 864.50] So that when you reboot, you don't pull from a broken latest.
[864.50 → 869.56] So a couple of things had to go wrong in our case, right?
[869.64 → 870.54] When incident two.
[871.06 → 872.90] It's the version that was running.
[873.18 → 874.76] That one came down as well.
[875.12 → 877.02] So the version that was running came down.
[877.10 → 878.08] It had to be rebooted.
[878.50 → 879.28] The pod.
[879.70 → 881.84] And when the pod was like restarted.
[882.44 → 884.06] Because it was pointing to latest.
[884.38 → 886.12] It pulled the broken version.
[887.18 → 888.70] So that happened as well.
[889.30 → 891.68] On top of latest being broken.
[891.68 → 896.48] So it needs to be like a sequence of events for this to happen.
[896.74 → 898.98] Which is what happened in our case.
[899.02 → 900.00] And that's why those are rare.
[900.60 → 904.26] So as I mentioned, like in the years since I had this set up, it only happened once.
[905.38 → 907.02] It was enough for us to have an incident.
[907.32 → 908.46] It wasn't a major one.
[908.54 → 911.44] It was just a minor one because production was up.
[911.90 → 912.18] Right?
[912.18 → 913.14] Everything was cached.
[913.54 → 914.68] We served from the CDN.
[914.82 → 916.46] We are serving from CDN everything.
[917.04 → 918.54] Except the authenticated users.
[918.76 → 923.00] Except the how do you call them, the dynamic requests.
[923.44 → 924.38] So not like the gets.
[924.86 → 926.52] This was like a post, a patch.
[926.56 → 927.54] And we have quite a few of those.
[927.62 → 929.74] I didn't actually realize how many of those we have.
[929.74 → 936.42] Because whenever we visit a link, like news in press, that's the most popular one.
[936.50 → 937.04] We keep hitting.
[937.82 → 939.42] We keep doing a lot of posts.
[940.42 → 942.08] So there's that.
[943.58 → 948.10] But anyway, it was like up for anyone that like was casually browsing it.
[948.20 → 949.54] People could listen to podcasts.
[949.54 → 954.28] Only like a few URLs that were not in the CDN were not available.
[955.52 → 959.08] That's a good, to your point, Jared, the unsolved mysteries.
[959.08 → 961.84] If you listen to Kaiden 20, we solve some more mysteries for you.
[961.86 → 966.14] So if you left that conversation thinking like Gerhard, what actually happened behind the scenes?
[966.22 → 967.52] Well, we've kind of recapped some of that.
[967.76 → 971.32] So the mystery is solved for those unsolved mysteries of Kaiden 20.
[971.56 → 971.84] You're welcome.
[973.68 → 976.78] But I do have very exciting news.
[977.48 → 980.74] So not only we solve that mystery, we did something even better.
[981.06 → 986.02] And I think we discussed this also in episode 20 about a tighter honeycomb integration.
[986.02 → 993.00] So one of the things which we did since, we integrated Honeycomb with Vastly with our CDN.
[993.38 → 1001.96] So we can see a lot more details about how the CDN behaves, which are the cache hits, which are the misses.
[1003.42 → 1006.22] When I say, I don't mean misses like the misses.
[1006.58 → 1008.50] I mean like M-I-S-S-E-S.
[1009.02 → 1009.18] Yeah.
[1009.34 → 1010.22] There's no U there.
[1011.04 → 1011.80] Solid clarification.
[1011.80 → 1012.28] Yeah.
[1013.72 → 1017.54] And we can just like to drill down, observe a lot of stuff.
[1017.64 → 1018.38] That's amazing.
[1018.48 → 1025.60] Like the level of visibility which we have right now, we can answer so many questions, including the pull request, which we had to open.
[1026.30 → 1029.76] I'm going to find it up now because I forgot the exact number.
[1029.88 → 1032.06] There were some new pull requests since.
[1032.74 → 1034.04] This is pull request.
[1034.04 → 1035.42] No, sorry.
[1035.54 → 1035.90] Issue.
[1036.50 → 1037.28] Not a pull request.
[1037.58 → 1040.36] Issue 383.
[1041.38 → 1047.30] Why do some MP3 requests take 60 seconds or more while others complete quicker?
[1047.30 → 1062.54] So we have an answer to this question as well as full visibility into how the CDN behaves, the app behaves, the ingress nginx, how it behaves and how they interact among one another.
[1062.98 → 1065.94] And some of the details which we get are fascinating.
[1065.94 → 1072.86] Like I can finally be properly curious in prod and I didn't know what it meant until I did this integration.
[1073.32 → 1075.76] And some of the level of detail is just amazing.
[1077.20 → 1090.80] So we can, for example, see the top URLs, the top episodes by browser, by user agent, by data centre, by country, by city.
[1091.00 → 1093.20] It's just like so much insight.
[1093.68 → 1095.26] And this is just like the content stuff.
[1095.26 → 1097.26] Then it comes to the CDN.
[1097.56 → 1101.00] As I mentioned, the cache status, how many hits versus how many misses.
[1102.38 → 1104.72] We can slice and dice by audio requests.
[1105.60 → 1116.30] And rather than building dashboards, we can do something even more amazing, which is literally started with a query and keep asking questions and keep getting answers until you understand what's happening.
[1117.66 → 1123.00] So this is the first time we've been able to have observability to this level on our CDN.
[1123.00 → 1129.96] And so to recap, we leverage it quite well because all requests go through Vastly first prior to hitting our application.
[1130.46 → 1136.44] So it would make sense if you make that choice and lean that heavily, trust that much on your CDN.
[1136.46 → 1137.24] In this case, we do.
[1137.24 → 1137.88] We trust Vastly.
[1137.94 → 1140.20] They do an amazing job for us for many years now.
[1141.48 → 1147.68] But now we actually have observability into various specifics of how it operates for us where we never had that before.
[1147.90 → 1148.34] Correct.
[1148.74 → 1153.18] And this is thanks to the details and visibility that Honeycomb gives us.
[1153.34 → 1153.68] Correct.
[1153.68 → 1154.12] Yeah.
[1154.12 → 1154.96] Yeah.
[1155.14 → 1159.06] That was one of the big improvements since episode 20.
[1159.92 → 1163.26] And we can see the slowest requests.
[1163.88 → 1170.08] And we understand that the XML ones, like the sitemap or the feeds, they're the slow ones.
[1170.62 → 1173.92] They take five seconds sometimes to load.
[1173.92 → 1177.26] And the website is fairly fast.
[1177.70 → 1182.24] The only time when it gets slow is when we serve static assets from the website.
[1182.44 → 1187.42] So in the Phoenix app, when there's a cache miss in the CDN, it has to go to the app.
[1187.72 → 1188.84] Actually, Ingress Nginx.
[1189.52 → 1191.12] Ingress Nginx has to go to the app.
[1191.22 → 1194.36] And the app has to store like a PNG or JPEG.
[1194.54 → 1195.92] It's usually PNG or...
[1196.48 → 1197.26] Yeah, PNG.
[1197.40 → 1199.46] That's the one that took quite a bit of time.
[1199.46 → 1200.66] So I was looking at it.
[1202.18 → 1203.14] Was it earlier?
[1203.80 → 1204.30] Yes.
[1204.62 → 1205.14] Let me find.
[1205.26 → 1205.98] It's right here.
[1207.02 → 1209.46] It took...
[1209.46 → 1211.12] That was an interesting one.
[1212.30 → 1213.46] It was...
[1213.46 → 1214.82] Icon small.
[1214.90 → 1215.84] No, it wasn't that one.
[1216.10 → 1216.86] Time elapsed.
[1216.96 → 1217.38] This was it.
[1217.44 → 1219.54] It was actually a GIF or IF.
[1221.06 → 1225.50] News item, 1.4 minutes to serve it.
[1226.76 → 1229.04] That's how long it took to serve that.
[1229.46 → 1231.68] News item, GIF or GIF.
[1232.82 → 1234.18] All the way to Hong Kong.
[1235.08 → 1236.98] So someone from Hong Kong was accessing it.
[1237.24 → 1238.28] They were waiting that long, huh?
[1238.54 → 1243.72] They were waiting that long because they had to go all the way to our data centre in New York.
[1245.62 → 1247.82] And I had to wait for it.
[1247.82 → 1248.40] It's probably a big...
[1248.40 → 1250.82] It's probably a big GIF too.
[1252.08 → 1252.32] Yeah.
[1252.46 → 1253.26] They always are.
[1253.42 → 1256.00] I mean, GIFs are just large files, unfortunately.
[1256.44 → 1257.20] At least a Meg.
[1257.32 → 1258.02] Sometimes 10.
[1258.72 → 1259.86] Maybe 50.
[1260.32 → 1260.46] But...
[1260.46 → 1260.76] Let's see.
[1260.80 → 1261.42] How big is it?
[1261.58 → 1262.82] We have that as well information.
[1263.30 → 1264.72] Body size...
[1264.72 → 1267.48] 18 kilobytes?
[1268.20 → 1268.54] No.
[1268.54 → 1269.36] That's all right.
[1269.72 → 1270.08] Megabytes.
[1270.30 → 1271.42] So it's like 18 million.
[1272.18 → 1272.64] Let's see.
[1273.70 → 1275.72] Should we ask Siri to do some math for us again?
[1276.22 → 1276.66] Yes, Siri.
[1277.04 → 1278.02] 18 million bytes.
[1278.18 → 1280.16] They should ask Honeycomb to do that math for us.
[1280.58 → 1280.94] Right.
[1281.04 → 1282.74] So that's the one thing which you need to set.
[1283.12 → 1284.60] So I was setting some...
[1284.60 → 1284.80] Yeah.
[1284.90 → 1287.46] Some derived queries.
[1287.86 → 1288.08] Yeah.
[1288.16 → 1288.88] Derived queries.
[1289.64 → 1290.44] But...
[1290.44 → 1292.10] Let's see.
[1293.42 → 1295.00] But not for this specific thing.
[1296.84 → 1297.60] 17 kilobytes.
[1297.68 → 1298.42] 17 megabytes.
[1299.34 → 1299.42] Yeah.
[1299.50 → 1302.96] We have a 17 megabyte GIF.
[1304.22 → 1306.18] And serving it to Hong Kong, that's how long it takes.
[1306.18 → 1306.56] It's pretty heavy.
[1306.66 → 1306.82] Yeah.
[1306.94 → 1307.14] Yeah.
[1307.14 → 1307.62] Yeah.
[1308.62 → 1310.54] So the only thing is we do lazy load those.
[1310.82 → 1313.56] So you're not actually waiting and user experience.
[1313.68 → 1315.50] You can read what the news item is.
[1315.76 → 1315.98] And then...
[1315.98 → 1316.06] Yeah.
[1317.16 → 1320.32] As long as it takes a minute and a half to read, by then, the image is low.
[1320.42 → 1321.86] It's still too long, but...
[1321.86 → 1322.08] Yeah.
[1322.56 → 1322.86] Yeah.
[1323.32 → 1325.84] Well, I don't think anybody's optimized for reading.
[1326.18 → 1327.66] Unless your imager or something like that.
[1327.82 → 1329.80] Maybe you're optimizing for those things to be superfast.
[1330.88 → 1332.70] Large GIFs like that, for example.
[1333.26 → 1336.88] Well, if we had it on a CDN in Hong Kong, it would be much faster.
[1336.88 → 1337.32] Exactly.
[1337.32 → 1337.52] Okay.
[1337.52 → 1338.96] So that's the question I was thinking of asking.
[1339.10 → 1343.28] Like, okay, the observability lets us know this event happened, right?
[1343.32 → 1348.38] The event being this GIF was served from Newark to Hong Kong at this speed.
[1348.60 → 1349.96] It's this size, et cetera.
[1349.96 → 1352.58] The other question is, it was a miss.
[1352.78 → 1353.88] So why was it a miss?
[1354.04 → 1357.68] So these are questions we begin to answer ourselves as we dig into this.
[1357.76 → 1358.80] Okay, why was it a miss?
[1358.88 → 1359.68] Okay, now we know.
[1360.16 → 1361.94] And we figure, what was the answer to that?
[1362.02 → 1362.84] Why was it a miss?
[1363.94 → 1364.80] Or was it a cash miss?
[1365.34 → 1367.04] First Hong Kong visitor of the day.
[1367.40 → 1368.48] Or since it expired.
[1368.60 → 1369.04] Or who knows?
[1369.60 → 1369.82] Yeah.
[1369.82 → 1375.98] I mean, those are kept in cash right on Vastly, and they can't cash like the entire internet.
[1377.18 → 1380.38] So even for us, they can't cash like all of our content.
[1381.38 → 1382.26] So the...
[1382.26 → 1387.54] They can probably cash all of our content at all of their pops and barely ever notice, don't you think?
[1388.16 → 1397.90] They could, but I think the reason why they're not is that they have to shed some of the extra content that is not accessed within, I don't know, X hours, days, whatever.
[1398.46 → 1406.02] So they don't guarantee that everything will be in the CDN all the time, even though our headers ask for it to be in the CDN for a few weeks, I believe.
[1406.32 → 1407.94] I'm not sure exactly this one.
[1407.94 → 1413.04] We can check to see how long it should be kept in the CDN for this specific request.
[1413.76 → 1416.70] But if its fire remember, it's just meant to be a few weeks at most.
[1416.70 → 1423.06] So if that wasn't accessed in a few weeks, and it may expire when it's requested again, which will be a miss.
[1424.36 → 1424.48] Right.
[1425.50 → 1426.10] And it'll be very slow.
[1426.10 → 1428.62] Why won't they just make people pay for that desire then?
[1429.00 → 1435.38] I guess if you're a larger site with much more assets than we have, maybe that becomes more and more expensive.
[1435.60 → 1439.66] But, you know, it's in our affordance right now to ask them to do that.
[1439.90 → 1440.06] Yeah.
[1440.86 → 1442.34] That's a great, great idea.
[1442.34 → 1443.52] So why won't they offer us a service?
[1443.70 → 1445.94] Like, hey, just cash the whole thing indefinitely.
[1445.94 → 1449.02] If, you know, and just, and I'll pay for it.
[1449.50 → 1451.20] I would love us to be able to do that.
[1451.28 → 1453.34] Like, all our stuff should be cached all over the world.
[1454.00 → 1455.08] Like, I agree.
[1455.12 → 1456.22] What's our total assets on stuff like that?
[1456.26 → 1459.02] What's our total, like, what would be the weight?
[1459.20 → 1459.88] In terabytes?
[1460.44 → 1460.88] No.
[1461.00 → 1461.32] No.
[1461.34 → 1461.92] Or in gigs?
[1462.28 → 1464.00] A hundred, 150 gigs?
[1464.48 → 1464.84] That's not that much.
[1464.84 → 1465.90] I mean, that's pretty reasonable.
[1465.90 → 1472.32] I mean, I can go buy a 14 terabyte hard drive for under 400 bucks.
[1473.04 → 1478.26] Yeah, but you need to multiply that times, you know, how many times you want, how many pops you want.
[1479.06 → 1480.80] So, but still, still you're right.
[1480.96 → 1481.10] That's true.
[1481.10 → 1482.52] It's not a lot of data.
[1482.80 → 1484.20] I wish it was cached.
[1484.34 → 1489.92] And I wish we had an e-tag implementation so that if the content doesn't change, it won't expire from the cache.
[1490.80 → 1493.02] And, I mean, we have it configured.
[1493.14 → 1503.14] We have cache shielding so that, or like pop shielding, which means that there should be at least one pop where this is always kept in cache.
[1503.14 → 1507.40] So, if another one doesn't have it, it should get it from that pop rather than come to us.
[1507.84 → 1507.98] Right.
[1508.06 → 1509.60] And their network's probably faster than ours.
[1509.96 → 1510.64] Of course, yes.
[1510.64 → 1510.82] Right.
[1511.02 → 1512.24] It should be at least by design.
[1512.26 → 1513.18] It's optimized, right?
[1513.32 → 1515.18] I mean, they should, yeah, they have all the optimization.
[1515.32 → 1518.42] They have the best routing between their pops, which is how it should be.
[1518.98 → 1519.74] So, you're right.
[1519.82 → 1522.04] I mean, but this we never had before.
[1522.10 → 1523.26] And this is the exciting thing.
[1523.32 → 1528.20] So, now we know why our 99th percentile, why we have such a bad tail latency.
[1528.64 → 1530.34] Because sometimes this stuff happens.
[1530.34 → 1533.64] We didn't have this visibility before, and that's the exciting stuff.
[1535.62 → 1537.82] Where does the law of diminishing returns come in?
[1539.82 → 1541.12] I didn't hear any of you.
[1541.76 → 1542.64] Do you want to try again?
[1543.12 → 1546.30] When does the law of diminishing returns come in?
[1546.76 → 1548.50] Because, you know, slow clients are slow.
[1549.12 → 1550.70] We can't make every request fast.
[1551.38 → 1558.48] Where do we know now we're just basically toiling away at something that's not worth our time anymore?
[1558.48 → 1560.88] Versus this is actually a valuable optimization.
[1561.40 → 1562.80] I'm really glad you brought this up.
[1562.90 → 1566.88] Because we have, this is something which we weren't able to see before.
[1567.04 → 1572.08] We have Apple Watches consuming MP3 files.
[1572.62 → 1573.90] And they are slow.
[1574.22 → 1576.68] So, they take, you know, many, many minutes.
[1577.22 → 1580.54] Like, our longest consumer was something like 40 minutes.
[1580.54 → 1584.90] Imagine someone being connected to our website and consuming MP3s for 40 minutes.
[1585.42 → 1586.40] It was on Apple Watch.
[1586.40 → 1588.90] And there's, like, a couple others like that.
[1589.50 → 1597.70] So, when it comes to content that is not in the cache, I don't think we should spend much more time on that.
[1597.70 → 1601.30] Except if we're talking about using an object store versus local store.
[1601.38 → 1602.76] But that's, like, a separate conversation.
[1603.42 → 1608.42] However, we should absolutely try to serve as much as we can from the CDN.
[1609.04 → 1611.06] Especially when it comes to the static content.
[1612.24 → 1615.86] GIFs, PNGs, MP3s, all that stuff should be served directly from the CDN.
[1615.86 → 1618.60] Which is exactly what Adam was suggesting.
[1619.32 → 1619.62] Mm-hmm.
[1620.46 → 1624.12] I mean, it would be different if we had, like, an unreasonable ask for them.
[1624.28 → 1627.22] Like, if it was, like, terabytes and terabytes of data.
[1627.42 → 1628.24] Like, that's unreasonable.
[1628.66 → 1637.32] But if it's, like, sub 200 gigs, that's not unreasonable to ask a CDN to, in perpetuity, hold that until I'd say it's expired.
[1637.90 → 1638.78] What are you thinking, Jared?
[1638.78 → 1641.44] Well, this is what I've been saying for years.
[1641.56 → 1642.26] That's what I've been thinking.
[1643.94 → 1645.24] Well, I think this is, like, the...
[1645.24 → 1646.60] Okay, you're being facetious now, right?
[1646.94 → 1647.26] Facetious?
[1647.28 → 1648.60] No, facetious.
[1648.74 → 1649.24] No, I'm not.
[1649.66 → 1650.48] I've been saying for years.
[1650.66 → 1656.14] Can't they just cache our stuff forever and just keep it and never request it again until we tell them that it's fresh?
[1656.14 → 1664.74] And so I understand that, like, okay, if we're going to do what Adam proposes, you're kind of becoming a snowflake, right?
[1664.82 → 1666.58] Like, hey, Vastly, please treat us differently.
[1667.00 → 1675.70] But isn't there just, like, a way we can, that they can scale to all their customers to let them, to let you say, don't ever request this again, please?
[1676.06 → 1678.68] I would love to have that conversation with someone from Vastly.
[1678.80 → 1679.24] I've been trying for years.
[1679.24 → 1680.14] That's what I've been saying for years.
[1680.14 → 1682.42] I don't want them to keep asking me for new...
[1682.42 → 1685.52] My ship at 28.mp3 hasn't changed.
[1685.62 → 1686.38] It's not going to change.
[1686.48 → 1687.42] It's never going to change.
[1687.84 → 1688.84] We know it's never going to change.
[1689.06 → 1690.38] So, yeah.
[1690.72 → 1695.26] I will not name any names, the people that I reached out that I knew within Vastly.
[1695.68 → 1701.08] But if a listener knows someone within Vastly that wants to have this conversation, I would love to do that improvement.
[1701.70 → 1707.36] Because Honeycomb, this new integration, showed us how much can improve within the CDN.
[1707.36 → 1707.96] Yeah.
[1707.96 → 1716.04] And we are reaching diminishing returns within the app, within our own infrastructure, where the biggest wins right now are in the CDN.
[1716.76 → 1716.98] Right.
[1717.70 → 1723.08] For me, imposter syndrome sets in when I think, surely we're holding it wrong.
[1723.16 → 1728.58] You know, like the Steve Jobs response to the antenna on the iPhone 4 is you're holding it wrong.
[1728.96 → 1730.58] I feel like we're just not using Vastly right.
[1730.58 → 1732.58] Like, I think we're...
[1732.58 → 1734.60] I mean, I understand how to set HTTP headers.
[1735.34 → 1736.44] And we use Tags.
[1736.70 → 1737.92] And we set cache control.
[1738.08 → 1739.38] And we've tweaked some stuff.
[1739.38 → 1743.20] But I just feel like we're not using it right for some reason.
[1743.30 → 1746.34] And that's why part of me is just wondering.
[1746.92 → 1748.44] That's where I like the toiling away is.
[1748.52 → 1751.86] Like, well, how many times can we tweak the way that we tell Vastly to do things?
[1752.40 → 1752.68] Mm-hmm.
[1752.68 → 1755.54] But I don't know.
[1755.66 → 1757.44] I just thought this is how CDNs work.
[1757.52 → 1759.38] It's like, hold on to it until it's fresh, please.
[1760.10 → 1763.30] That seems like a button you'd click in a click op somewhere.
[1763.56 → 1764.14] But I don't know.
[1764.90 → 1765.20] Yeah.
[1765.20 → 1771.26] So I do, like, I'm surprised when content that should be cached for...
[1771.26 → 1774.40] Now that I think of it, some of it is even cached, like, for a whole year.
[1774.78 → 1777.26] The stuff that we know is not going to change.
[1778.00 → 1784.60] And that content is being requested even though it was requested before.
[1785.32 → 1786.94] And it's requested again.
[1787.08 → 1788.14] And it hasn't passed a year.
[1788.26 → 1789.86] So what's going on Vastly?
[1789.92 → 1790.24] Right.
[1790.58 → 1790.98] Mm-hmm.
[1791.36 → 1792.52] I can't answer that.
[1792.52 → 1797.48] Our old episodes, the long tail of listens on our shows is bewilderingly awesome.
[1797.66 → 1801.46] Like, you go back to a show, and you're like, wow, 33 people listen to this today.
[1801.64 → 1803.32] And it's four years old.
[1803.80 → 1805.90] Like, every day our MP3s are being requested.
[1806.38 → 1807.26] Pretty much all of them.
[1807.64 → 1809.94] You know, plus or minus some outliers.
[1810.26 → 1817.10] So they shouldn't be expiring unless you set the expiration to an hour or 30 minutes or six hours.
[1817.10 → 1822.44] But if we're setting it to a long time, I just, I do not understand why we have so many cash misses.
[1823.34 → 1830.42] Especially, I mean, given, it'd be different if we, if our content was highly volatile in terms of change.
[1830.86 → 1831.90] We're a media company.
[1832.08 → 1833.92] The things we create are long-term artifacts.
[1834.32 → 1839.64] So just by nature of the business we're bringing, like the character type we are, the persona, so to speak, even.
[1839.98 → 1840.20] Yeah.
[1840.58 → 1844.66] You know, we know that the reason we're using the CDN is to be globally fast.
[1844.98 → 1845.38] Right.
[1845.38 → 1850.38] And the data we're giving them to be globally fast doesn't change if ever.
[1850.86 → 1851.16] Mm-hmm.
[1851.38 → 1856.36] So we want to be globally fast forever and pay for that.
[1856.78 → 1857.18] Right.
[1857.58 → 1864.42] And we put fast in front of everything to enable that so that even if our app is down, we're still serving cash pages.
[1864.84 → 1869.32] And the same thing for our actual files, like MP3s and GIFs and things like that.
[1869.38 → 1877.12] Like just by the nature of us being a media company or a media entity, the things we tend to, the things we have tended to never change.
[1877.32 → 1877.48] Like it.
[1877.98 → 1878.20] Yeah.
[1878.20 → 1883.80] I think we've changed like an episode just to go back and update what we called a remastering where we're doing that for a bit.
[1883.88 → 1889.68] We're remastering some of these shows Jerry's talking about that had high degrees of listens that are several years old.
[1890.18 → 1898.82] So rather than like having that listener go back and listen to an old show and still be sort of like unimpressed by the audio quality in comparison to now, we went back and remastered those.
[1899.88 → 1906.26] But we can also programmatically purge endpoints from Vastly by way of our system.
[1906.26 → 1906.84] So you could.
[1907.04 → 1907.18] Right.
[1907.50 → 1908.94] It'd be easy to code that up.
[1909.50 → 1910.08] I just don't.
[1910.22 → 1913.52] I've never done it because I feel like it keeps purging anyway.
[1914.56 → 1918.86] You know, and every once in a while I'll hop in there and just purge one manually, especially if it just released.
[1919.04 → 1919.90] I feel like we're holding it wrong.
[1920.14 → 1920.58] I do.
[1920.66 → 1923.44] I feel like I don't know why we're holding it wrong.
[1923.56 → 1928.32] It seems like the logical way a CDN should work is the way we think it does work.
[1929.04 → 1931.64] Yet we are holding it seemingly wrong.
[1931.64 → 1938.26] So, yeah, I say listeners, if you're out there, if you know somebody in Vastly who knows more than we do, we have connections there.
[1938.32 → 1941.40] But, you know, we've hit certain dead ends on that front.
[1941.74 → 1943.44] But, yeah, we'd love to have some help.
[1943.62 → 1945.36] Like Vastly, come on this show.
[1945.54 → 1954.50] Come on YouTube with Gerhard and Triage how we use our CDN and help us, you know, DE-antenigate ourselves and hold it right.
[1955.02 → 1955.48] You know what I mean?
[1955.48 → 1956.38] Like, yes.
[1956.50 → 1957.88] Let's not CDN gate ourselves.
[1958.02 → 1961.36] Over the years, we had some epic support threads with Vastly.
[1961.88 → 1962.32] Like, epic.
[1963.24 → 1965.00] Some of them have not been solved.
[1966.52 → 1967.28] Unsolved mysteries.
[1968.32 → 1970.56] Many unsolved mysteries when it comes to Vastly.
[1970.80 → 1972.30] Let's hold it right, please.
[1972.46 → 1972.98] I'm looking.
[1973.18 → 1975.18] So, I think we're holding it right.
[1975.50 → 1978.78] But I think there's stuff happening within Vastly which we don't fully understand.
[1978.90 → 1979.12] Right.
[1979.78 → 1981.44] And maybe that's just how it works.
[1982.10 → 1984.10] It doesn't make sense why it is that way.
[1984.10 → 1990.92] So, if it works that way and that's how it does work, that seems odd given the reason you use a CDN.
[1992.24 → 1992.94] I mean.
[1993.14 → 1994.62] I think we can Kaiden Vastly.
[1995.10 → 1997.58] I think that's what you're getting to.
[1997.78 → 1997.98] Yeah.
[1998.12 → 1998.28] Yeah.
[1998.38 → 2007.06] Because in the last 24 hours, we had 3,000 misses on MP3 files.
[2009.16 → 2010.96] This is in the last 24 hours.
[2011.20 → 2012.42] Oh, that's terrible.
[2012.42 → 2013.92] Doesn't make sense.
[2013.92 → 2014.12] Doesn't make sense.
[2014.28 → 2014.64] Exactly.
[2015.16 → 2015.86] Doesn't make sense.
[2016.68 → 2027.18] The whole reason we engage with Vastly in the origin before we got to what we could do application-wise was to deliver our MP3s globally fast forever.
[2027.56 → 2028.04] Yep.
[2028.04 → 2043.42] So, to have 1,000 misses in the last 24 hours is most
[2043.42 → 2044.92] too much data forever.
[2045.42 → 2045.72] Okay.
[2045.88 → 2046.14] Sure.
[2046.20 → 2046.94] We have to purge somewhere.
[2047.36 → 2047.60] Fine.
[2047.60 → 2049.86] Then have 1 pop be the canonical.
[2049.86 → 2050.92] That one is forever.
[2051.32 → 2055.46] And you can miss somewhere else and pull from your own pop fast, not from us.
[2055.90 → 2058.14] Well, we shield through LaGuardia, so we should have that.
[2058.34 → 2062.14] Like, LaGuardia should have it if Hong Kong doesn't.
[2062.54 → 2062.60] Exactly.
[2062.60 → 2066.98] So, I'm not super clear if that still shows up as a miss, if Hong Kong misses but grabs
[2066.98 → 2068.58] it from LaGuardia, doesn't grab it from us.
[2068.84 → 2069.76] Gary, you know the difference.
[2071.82 → 2072.22] Yeah.
[2072.98 → 2076.18] So, I'm not sure, but that's something worth digging into.
[2076.36 → 2077.88] So, this is exactly like…
[2077.88 → 2078.58] Let's solve this mystery.
[2079.00 → 2079.34] Exactly.
[2079.44 → 2081.08] How does this stuff work within Vastly?
[2081.16 → 2086.18] Like, this is the first time we could have a perfect conversation about this because
[2086.18 → 2086.92] of this integration.
[2087.12 → 2087.84] We have data.
[2088.20 → 2089.12] We have wisdom.
[2089.58 → 2089.74] Yeah.
[2090.18 → 2091.18] Before we had assumption.
[2091.44 → 2094.02] Now we have, like, look, here's Honeycomb.
[2094.20 → 2094.62] Hard facts.
[2094.62 → 2095.74] This is where it goes.
[2095.86 → 2096.68] This is how it works.
[2097.02 → 2097.24] Yeah.
[2097.88 → 2098.08] Yeah.
[2098.18 → 2098.90] It's amazing.
[2098.90 → 2103.82] You know, even asking for support makes it so much harder when you have no visibility
[2103.82 → 2105.58] into what's going on.
[2105.64 → 2106.24] Now we do.
[2106.62 → 2112.42] So, we are armed with more data to support ourselves differently in our argument back
[2112.42 → 2115.52] like why things are not working the way they should be or how we think it should be.
[2115.96 → 2116.16] Yeah.
[2116.16 → 2116.24] Yeah.
[2128.90 → 2136.02] This episode is brought to you by our friends at Incident.io.
[2136.40 → 2140.68] Every software team on the planet has to manage incidents and a very large percentage of those
[2140.68 → 2142.62] teams are using Slack to communicate.
[2142.84 → 2143.76] That includes us.
[2144.10 → 2149.02] With Incident.io, you can create, manage, and resolve incidents directly inside Slack.
[2149.28 → 2150.24] Here's how it works.
[2150.24 → 2152.56] Head to Incident.io and sign up for free.
[2152.76 → 2154.20] Then add it to your Slack.
[2154.20 → 2158.24] From there, you have a brand-new Incidents channel where all incidents get announced.
[2158.62 → 2161.28] Use the slash incident command to create and manage incidents.
[2161.60 → 2166.54] This command lets you share updates, assign roles, set important links, and more, all
[2166.54 → 2168.16] without ever leaving the Incident channel.
[2168.58 → 2174.10] Each Incident gets their own Slack channel plus a high-res dashboard at Incident.io with
[2174.10 → 2176.04] the entire timeline from report to resolution.
[2176.58 → 2179.78] Get everyone on the same page from the moment they join the Incident and help stakeholders
[2179.78 → 2180.64] stay in the loop.
[2181.00 → 2184.12] Add Incident.io to your Slack today and prove to yourself and your team.
[2184.12 → 2186.74] that they have everything you need to streamline your incident management.
[2187.22 → 2189.64] Learn more and sign up for free at Incident.io.
[2189.94 → 2191.00] No credit card required.
[2191.52 → 2192.98] Again, Incident.io.
[2193.40 → 2195.28] And by our friends at Ray gun.
[2195.56 → 2197.84] Have you ever wondered how users are really experiencing your software?
[2198.22 → 2202.50] When you unlock real user insights, you'll be able to identify and resolve front-end performance
[2202.50 → 2206.44] issues and ensure your application is consistently delivering superior experiences.
[2207.04 → 2210.92] Ray gun will deliver a daily performance summary to keep your finger on the pulse of your website
[2210.92 → 2216.50] with an overview of your slowest pages, Core Web Vitals, user sessions, and user satisfaction.
[2216.88 → 2219.90] This gets sent straight to your inbox or Slack channel of your choice.
[2219.90 → 2224.88] Join thousands of performance-focused, customer-centric software teams who use Ray gun every single
[2224.88 → 2227.36] day to deliver flawless experiences to their customers.
[2227.36 → 2229.92] Again, Raygun.com.
[2240.68 → 2243.64] So, Jared and I got some brand-new computers recently.
[2243.86 → 2244.76] Brand new M1 Macs.
[2245.12 → 2249.20] And like any new Mac, you take your sweet time setting it up.
[2249.36 → 2251.18] And in my case, Jared, you may concur.
[2251.76 → 2253.84] With your case, I'm doing it all manually.
[2254.24 → 2256.86] I'm not scripting anything this time.
[2256.92 → 2257.64] I want to take my time.
[2257.70 → 2261.16] Because the M1 Mac is so different, even Homebrew has a couple.
[2261.56 → 2266.94] It has one slight variance in how you set it up with what you add to your, in my case.
[2267.00 → 2270.02] And I think it was too, Jared, the ZSHRC file.
[2270.74 → 2272.90] So, there are a couple particulars to deal with.
[2273.00 → 2276.28] And I haven't gotten to the point yet to set up the app.
[2276.60 → 2278.50] Actually, I have, but I haven't done it yet.
[2278.50 → 2286.08] So, my thought is like, if I'm setting up changel.com for dev environment on my new Mac, how?
[2286.38 → 2287.04] What's the way?
[2287.20 → 2288.58] The README isn't super clear.
[2289.00 → 2291.02] There's a Docker path I'm not sure is still working.
[2291.92 → 2292.74] So, yeah.
[2292.86 → 2293.74] What do we do?
[2293.78 → 2294.32] How do you do it?
[2294.40 → 2295.10] Have you set it up, Jared?
[2295.26 → 2295.72] Where are you at?
[2295.72 → 2300.30] I have not set it up yet because I haven't needed to.
[2300.40 → 2303.86] I still have my old laptop right here that I can use.
[2304.88 → 2307.78] I would not use Docker because I didn't use Docker last time.
[2308.30 → 2308.60] Okay.
[2309.52 → 2309.78] Yeah.
[2309.84 → 2311.72] I would set it all up individually.
[2312.72 → 2316.40] But maybe I would even just procrastinate it until we're on code spaces.
[2316.60 → 2317.16] What do you think, Jared?
[2317.84 → 2318.96] That's exactly what I'm thinking.
[2318.96 → 2319.44] It's even better.
[2319.88 → 2321.46] That's exactly what I'm thinking.
[2321.68 → 2322.10] The reason why.
[2322.10 → 2323.10] I don't even want to set it up.
[2323.14 → 2323.70] I don't have to.
[2324.10 → 2324.46] Exactly.
[2324.46 → 2329.34] The local, like I uninstalled Docker about six months ago or four months ago, something
[2329.34 → 2329.84] like that.
[2330.44 → 2335.94] And it's not coming back on my machine or any other machine like my local machine.
[2336.34 → 2342.96] However, I'm running Docker on Linux, on the Linux server in Linde, which is my development
[2342.96 → 2343.40] machine.
[2344.50 → 2345.20] Is that right?
[2345.20 → 2345.56] Linux.
[2345.92 → 2346.46] That's right.
[2346.92 → 2352.04] So, what we want is GitHub code spaces where we can run our own infrastructure.
[2352.04 → 2360.06] So, rather than using the Azure VMs, which is what runs GitHub code spaces, we want to
[2360.06 → 2365.22] be running our own, whether it's Linde or, and this is where the big one comes in, Equinix
[2365.22 → 2365.52] Metal.
[2365.52 → 2368.52] I don't think they'll go there.
[2368.52 → 2369.50] I don't think they'll go there, will they?
[2370.60 → 2370.96] GitHub.
[2372.36 → 2373.40] Well, no, they won't.
[2373.46 → 2378.62] But like, can they allow people to use like, you know, as you can run your own GitHub runners
[2378.62 → 2380.32] with the GitHub actions.
[2380.32 → 2381.22] Mm-hmm.
[2381.22 → 2386.36] So, you should be able to run your own hardware, wherever it is, with GitHub code spaces.
[2386.58 → 2387.96] I think it's a natural next step.
[2388.84 → 2392.20] Because whatever needs to like, like, because you pay for the hardware.
[2393.34 → 2397.16] Like, that's what, that's where the cost for the GitHub actions is, sorry, GitHub code
[2397.16 → 2397.74] spaces is.
[2398.04 → 2399.84] And that's fine if you want the simplicity.
[2399.84 → 2406.84] But if you want to run, like, for example, an ARM, on ARM servers, or fast Intel servers
[2406.84 → 2413.02] with dedicated CPUs, dedicated NVMe's, 20 gigabit networks, why wouldn't you go to Equinix
[2413.02 → 2413.28] Metal?
[2414.50 → 2415.82] So, that's what I'm thinking.
[2416.02 → 2418.36] Because in that world, everything is amazing.
[2419.64 → 2420.84] So, I guess then...
[2421.50 → 2423.52] Or it will be when I'm finished with it.
[2423.72 → 2424.74] It's all rainbows.
[2425.04 → 2425.22] Yeah.
[2425.22 → 2425.28] Yeah.
[2426.08 → 2432.18] Isn't the thing with GitHub code spaces that it is their, like, their thing is their, their
[2432.18 → 2436.02] infrastructure, their VMs, their hardware, and it's optimized.
[2436.18 → 2440.68] Obviously, it's probably Azure-backed, considering the, you know, their parent company, etc.
[2441.58 → 2443.18] But isn't that what they sell?
[2443.26 → 2449.06] They're not, are they selling the agnostic route to dev environments in the cloud?
[2449.18 → 2450.22] They're selling...
[2451.08 → 2451.54] Not currently.
[2451.54 → 2452.84] ...code spaces, which is hosted by them.
[2452.84 → 2453.06] Right.
[2453.06 → 2457.20] It seems like it's, it's natural for us to want that, but it doesn't seem natural for
[2457.20 → 2458.56] GitHub to want to offer that.
[2458.64 → 2463.52] So, maybe it's like a cloud spaces alternative, which is geneticized, is the answer.
[2464.06 → 2464.94] So, there is Gitpod.
[2465.44 → 2466.32] I'm aware of that.
[2466.72 → 2467.08] Yeah, right.
[2467.08 → 2468.76] There is tilt.dev as well.
[2469.18 → 2470.74] There's a couple like that.
[2470.94 → 2475.34] But what I really want to do, having listened to the GitHub code spaces episode on changelog,
[2475.38 → 2476.10] I forget the number.
[2476.10 → 2481.36] I, like, tweeted Corey, like, hey, we should talk.
[2481.44 → 2482.46] I said, yeah, sure, email me.
[2482.54 → 2484.70] And I didn't have time to follow up on that email.
[2485.20 → 2492.30] But I really want to do that because I see the potential of GitHub code spaces, but I would
[2492.30 → 2493.54] use it slightly differently.
[2494.10 → 2497.42] Now, we're always up for partners, aren't we, Adam?
[2497.42 → 2502.86] So, if GitHub wants to sponsor changelog with the GitHub code spaces, we would be more than
[2502.86 → 2505.34] happy to use it and help it improve.
[2506.12 → 2509.24] But my first go-to would be, is what I know, right?
[2509.32 → 2514.18] Like, bare metal server somewhere or Li nodes or wherever, spin them up.
[2514.78 → 2516.10] And that's where cross plane comes in.
[2516.14 → 2518.98] There's, like, a couple of things happening in the background that will start coming together.
[2519.36 → 2522.96] There's an Equinix Metal episode with Zach coming.
[2522.96 → 2526.00] I think, 30, 29, I think.
[2526.18 → 2527.62] Actually, it came out.
[2527.70 → 2530.56] By the time you're listening to it, it came out, the episode with Zach.
[2531.10 → 2536.52] So, there's, like, a couple of things coming together which make me really excited and which,
[2536.72 → 2541.38] I think, setting anything locally for development, it is a time sink.
[2542.46 → 2548.08] And you should have environments which are pre-built for development in an automated way.
[2548.84 → 2550.72] And just click a button, and you have it.
[2550.72 → 2554.70] And when you're finished with it, you take it down, and you don't have to worry about it.
[2555.20 → 2568.10] You don't have to worry about upgrading PostgreSQL or are you running the right version of Erlang or should you install Docker or put up with Docker desktop updates which have been getting greedy and annoying in recent months, which is one of the reasons why I uninstalled it.
[2568.10 → 2572.78] And my main issue has always been I manage homebrew.
[2573.00 → 2574.52] I upgrade some things in there.
[2575.04 → 2578.50] I don't want to, you know, specifically upgrade particular things.
[2578.62 → 2582.88] So, I say upgrade all essentially or just brew upgrade after update.
[2583.34 → 2587.44] And next thing you know, Postgres is updated to the latest and my Postgres is broken.
[2588.00 → 2588.08] Exactly.
[2588.32 → 2589.58] And that was always the culprit.
[2589.58 → 2594.34] And then a couple of times it was Erlang and that kind of thing.
[2594.70 → 2606.48] So, yeah, because my local hackery things that aren't really connected to a dev environment shouldn't overlap with my actual dev environment for the application.
[2606.48 → 2609.92] So, I'm kind of in that weird space where it's like my truck.
[2610.02 → 2612.22] I have a gas guzzling Ford F-150.
[2612.68 → 2616.34] I love the new EV F-150, the lightning coming out.
[2616.80 → 2620.64] I want to buy a new truck sometime soon because I'm due.
[2620.74 → 2622.12] It's like seven years old.
[2622.90 → 2626.12] But I don't want to buy a gas vehicle.
[2626.28 → 2627.66] I want to buy an electric vehicle.
[2627.90 → 2629.96] So, I don't want to spin up my own dev environment.
[2629.96 → 2637.66] I want to use code spaces or some prescribed dev space that I don't have to worry about.
[2637.72 → 2640.94] That's always just fresh because I'm me.
[2641.08 → 2642.02] My identity is me.
[2642.34 → 2649.20] You know, my trustworthiness or the application should or our config should so I can get access to a certain database.
[2649.38 → 2651.68] Maybe a drive-by contributor shouldn't get access to.
[2652.24 → 2653.10] That kind of thing.
[2653.42 → 2654.92] So, and even drive-by contributions.
[2655.22 → 2657.16] Like, those are harder to do, probably.
[2657.16 → 2661.12] Maybe through .dev is somewhat easy if it's a typo or something like that.
[2661.26 → 2665.20] But if it's a contribution, I think it's much easier for us.
[2666.14 → 2670.14] So, I'm thinking of the GitHub code spaces experience.
[2670.84 → 2675.04] But maybe not necessarily running on Azure as it is today.
[2675.54 → 2679.86] But I'm not suggesting that we should all set up some bare metal servers.
[2680.30 → 2680.80] No way.
[2681.78 → 2684.62] It's an approach that our contributors should be able to use as well.
[2684.74 → 2685.50] And you're right.
[2685.58 → 2686.78] Identity should be baked in.
[2687.16 → 2688.16] So, our...
[2688.84 → 2689.96] But that's like the long term.
[2690.22 → 2690.88] So, short term.
[2690.98 → 2692.28] I think you want a short term.
[2692.48 → 2695.88] The short term answer is use your old machine.
[2696.82 → 2702.98] I would say short term answer would be can we get set up on code spaces in their current blessed way?
[2702.98 → 2710.42] And hope for a future where they have a more infinitely configurable version that's for the ways you want to use it.
[2710.46 → 2714.94] So, I'd say let's re-engage with Corey and GitHub on that front.
[2715.04 → 2715.58] I know they're willing.
[2715.70 → 2716.64] We've talked to them recently.
[2716.90 → 2717.88] So, we know they're willing.
[2718.56 → 2719.88] That gate has not closed.
[2719.88 → 2721.84] They want us to be on code spaces.
[2722.34 → 2722.66] Amazing.
[2722.80 → 2723.68] And leverage it that way.
[2723.78 → 2726.22] So, I say let's use it the way they want us to use it currently.
[2727.34 → 2728.16] Get going that way.
[2728.34 → 2731.94] And then whenever it needs to scale different ways than it can.
[2732.30 → 2735.28] Or you can use Gitpod to do it your own way with Equinix Metal.
[2735.28 → 2737.70] Because that's what Gitpod does, right?
[2737.78 → 2738.92] Like Gitpod lets you be anywhere.
[2738.98 → 2739.52] They're agnostic.
[2739.78 → 2744.58] Whereas code spaces is simply GitHub, simply Azure infrastructure.
[2745.66 → 2750.92] So, I'm happy if the changelog org would have this capability.
[2751.30 → 2757.28] If GitHub code spaces was part of the changelog org, and we could use it out of the box, I think that would be amazing, right?
[2757.32 → 2764.44] So, if we can contribute to that, and we can make sure that anyone wanting to contribute to the changelog app, we could get that working.
[2764.44 → 2767.14] Very well with code spaces, which currently isn't.
[2768.04 → 2768.84] That, you're right.
[2768.90 → 2770.52] That is a good short-term solution.
[2770.76 → 2774.18] So, I think you just gave me a Christmas gift.
[2774.18 → 2774.58] I'm not going to set it up locally.
[2774.68 → 2775.36] I'll wait.
[2776.30 → 2779.46] I'm going to wait for my Christmas gift, which is code spaces wrapped in a bow.
[2780.16 → 2785.58] The challenge with this path being short-term is that Gerhard is the most organized podcaster in the universe.
[2785.58 → 2787.90] And he's scheduling into March and April.
[2789.88 → 2790.24] I know.
[2790.36 → 2791.70] So, that doesn't sound very short-term to me.
[2792.04 → 2792.84] I'll need to make room.
[2792.84 → 2796.12] I'll need to, like, I don't know, someone cancel an interview, maybe?
[2796.74 → 2797.78] Well, here's what can happen.
[2797.92 → 2809.30] Honestly, behind the scenes, what happens is you may plan that way, but you have got to plan for a buffer in your – like, even if you have it planned out, there's always – like, Gerhard and I have done this, too.
[2809.32 → 2814.88] We've had it planned out, you know, several weeks to a month and something happens, and we're like, we've got to change the order.
[2814.88 → 2815.28] Yeah.
[2815.44 → 2819.28] And so, because, you know, you get to run the show, you can make those calls.
[2819.46 → 2827.50] And so, just because you've set in that motion – now, if you've made a promise or whatever, reach back out to them and say, hey, I'm sorry, we've got a timely episode coming out.
[2827.60 → 2828.78] I need to bump you back one week.
[2829.24 → 2830.70] They're probably not going to be upset.
[2830.82 → 2834.90] And if they are, give them a free T-shirt or, you know, whatever it takes to –
[2834.90 → 2835.46] How do I do that?
[2835.58 → 2836.98] I don't know how to give them a free T-shirt.
[2837.12 → 2837.54] Tell me.
[2837.56 → 2837.90] It's too easy.
[2837.96 → 2838.66] You tell me your T-shirt.
[2838.66 → 2839.16] We'll talk offline.
[2839.30 → 2839.78] We'll talk offline.
[2839.78 → 2840.06] All right.
[2840.12 → 2840.66] We'll make it happen.
[2840.94 → 2841.28] It's too easy.
[2841.28 → 2841.46] Okay.
[2842.14 → 2843.90] It's amazing what a free T-shirt will do.
[2844.34 → 2844.54] Yeah.
[2844.72 → 2850.04] I mean, we love our listeners, and we love our guests just as much, if not more.
[2850.70 → 2855.74] So, if ever we have to apologize, we'll do it with very sweet kindness.
[2856.30 → 2856.68] All right.
[2856.80 → 2858.54] GitHub Code Spaces in December.
[2858.92 → 2859.24] Here I come.
[2859.24 → 2859.62] There you go.
[2859.88 → 2860.86] Let's make it happen.
[2861.32 → 2861.96] Let's make it happen.
[2861.98 → 2862.96] Christmas is coming early.
[2863.06 → 2863.50] We're right on time.
[2863.50 → 2870.64] So, I think the actual short-term solution is brew and stall Elixir, brew and stall Postgres, clone the repo –
[2871.28 → 2872.40] I don't think that's going to work.
[2873.48 → 2873.88] Why not?
[2874.64 → 2875.08] I bet I get it working.
[2875.08 → 2875.96] I think the versions have changed.
[2876.18 → 2877.72] I don't think – I never even tried.
[2877.84 → 2882.00] Like, I think by default Postgres equal to version 13 or maybe even 14 if it's out yet.
[2882.38 → 2882.58] Right.
[2882.60 → 2884.36] I don't know whether things will work with that.
[2884.98 → 2885.52] Oh, it does.
[2885.64 → 2886.06] I'm running it.
[2886.08 → 2887.82] And the README is a little off, too.
[2888.36 → 2889.34] The README is off, yes.
[2889.34 → 2890.50] In terms of what it prescribes.
[2891.42 → 2893.70] Like, it just said that the bonuses are Elixir and Ealing.
[2893.80 → 2896.04] It doesn't say which Postgres and everything else.
[2896.06 → 2899.18] Just wait for the transcript to come out of this episode and then follow that.
[2899.18 → 2904.10] I'm telling you, brew install Elixir, brew install Postgres, clone the repo.
[2905.04 → 2905.30] Okay.
[2905.58 → 2906.28] So, first step.
[2906.40 → 2907.04] In-depth.get.
[2907.04 → 2910.38] Gerhard gets a new MacBook M1 for Christmas.
[2911.54 → 2912.88] I already got one, Gerhard.
[2912.96 → 2913.78] You can't –
[2913.78 → 2914.38] All right.
[2914.42 → 2914.74] Just post it to me.
[2914.74 → 2915.22] I can do this work.
[2915.36 → 2915.88] And then –
[2915.88 → 2916.20] All right.
[2921.14 → 2926.06] Well, unfortunately, with the ship dates on these new MacBooks, I also don't think that's a short-term solution.
[2926.06 → 2927.62] Four to six weeks, I've seen that.
[2927.74 → 2928.00] Yeah, yeah.
[2928.12 → 2928.76] I know what you mean.
[2929.32 → 2932.62] You've had to order it, like, a month ago to get it on time for Christmas.
[2932.62 → 2932.86] Yes.
[2933.58 → 2933.88] I know.
[2933.98 → 2934.28] All right.
[2934.32 → 2939.46] So, the short-term solution is keep your old machine around and use that until you have a medium-term solution.
[2939.96 → 2940.18] Yeah.
[2940.26 → 2940.64] Which I do.
[2940.72 → 2941.34] It's right next to me.
[2941.42 → 2942.48] It's no problem to use it.
[2942.94 → 2948.14] But, like anybody, I'm like, I want to get set up on this new machine and never look back to the old.
[2948.14 → 2952.80] And just format the drive and roll on.
[2952.80 → 2964.62] What's up, shippers?
[2964.62 → 2967.20] This episode is brought to you by Equinix Metal.
[2967.20 → 2974.84] If you want the choice and control of hardware with low overhead and the developer experience of the cloud, you need to check out Equinix Metal.
[2975.10 → 2979.46] Deploy in minutes across 18 global locations from Silicon Valley to Sydney.
[2979.94 → 2984.70] Visit metal.equinix.com slash just add metal and receive $100 in credit to play with.
[2984.70 → 2988.18] Again, metal.equinix.com slash just add metal.
[3003.86 → 3013.44] So, last, Kaiden, we talked about moving our uploads to the cloud, specifically S3's cloud.
[3013.44 → 3016.26] I wanted to give a quick update on progress there.
[3016.32 → 3019.36] I wanted to have it done by the time we recorded this.
[3019.44 → 3029.64] In fact, Gerhard, you and I met, was it last week, to discuss a game plan to getting us from where we are to 100% cut over.
[3029.94 → 3031.66] We did not quite get there.
[3032.06 → 3034.20] And that's because I had a yak shave instead.
[3034.52 → 3037.44] So, I thought I would take you guys on a little journey.
[3037.52 → 3038.12] I did diffuse well, so it's okay.
[3038.40 → 3040.16] Your yak shave held my yak shaves.
[3041.96 → 3042.66] It's all good.
[3043.44 → 3046.92] So, you know, I only have so much time to work on the platform.
[3047.32 → 3050.08] And I have to use that time wisely.
[3050.32 → 3055.78] And sometimes it's like GitHub issues-based development, you know, when things come in.
[3055.86 → 3062.58] Because then you know it's a user or a listener or a reader's need or something that they hit up against.
[3063.24 → 3066.64] And so, I end up prioritizing things that I want to do.
[3066.94 → 3068.86] Probably not always the wisest.
[3068.86 → 3070.92] But it happened again.
[3071.14 → 3075.36] I was just, I have my waffle branch, which waffle is a new replacement for ARC.
[3075.82 → 3083.84] ARC is the upload library that we had used previously that went unmaintained, taken over by the community and now called waffle.
[3084.26 → 3085.20] And so, we've cut over to that.
[3085.30 → 3086.00] I have my branch.
[3086.72 → 3088.68] It's like, I said it was, what did I tell you?
[3088.68 → 3092.54] How many percentage points did I have done when I told you the other day, Gerhard?
[3092.74 → 3094.06] I think it was like 90%.
[3094.06 → 3095.80] Yeah, 90% is what I remember.
[3096.46 → 3096.64] Yeah.
[3096.76 → 3098.88] So, probably I'm at like 94% now.
[3099.54 → 3101.18] And then here comes an issue.
[3101.42 → 3102.68] Issue number 393.
[3104.64 → 3106.46] Hit our GitHub issues, which we'll link up.
[3106.46 → 3112.86] Newsletter links proxy encodes special URLs with HTML instead of percent based.
[3113.50 → 3117.92] This is a tiny little bug that was just interesting to me.
[3117.98 → 3132.60] So, what happened is, in our changelog weekly newsletter, which goes out every Sunday morning, includes all the shows from that week, every episode we put out, as well as all the news and the links and the repos and the commentary for the week.
[3132.60 → 3139.22] We linked to Chris Manson's post called It's All Gravy.
[3140.68 → 3152.64] And his website is chris.manson.ie, probably because he loves Internet Explorer, slash its-all-gravy.
[3153.14 → 3156.46] Only its is a contraction, right?
[3156.54 → 3158.36] So, it's I-T apostrophe S.
[3159.26 → 3161.32] And the son of a gun left the apostrophe in there.
[3161.32 → 3162.86] Now, I'm giving him a hard time because I know Chris.
[3162.92 → 3164.24] He's a JS Party listener.
[3164.58 → 3165.44] Hangs out in the chat.
[3166.54 → 3169.64] And he left that apostrophe in the URL.
[3169.86 → 3172.42] First, isn't that just like blasphemous right there?
[3172.48 → 3174.90] How can you throw an apostrophe in your URL?
[3175.02 → 3175.82] Clean URLs, people.
[3175.82 → 3176.78] Mm-hmm.
[3177.42 → 3195.26] But what happened with that apostrophe is the way that we encode that creates the HTML encoding instead of percent base, which you'd expect in the URL, which caused people that clicked on that link in our newsletter to go to a web page, which was a 404, because it was incorrect.
[3195.26 → 3202.00] Now, certain browsers actually manage it okay, and like the apostrophe looks fine in the address bar and everything, which I thought was kind of interesting.
[3202.80 → 3203.02] Mm-hmm.
[3203.62 → 3213.02] And so, I thought, here's a bug I should chase down while not working on these uploads to the cloud branch that I'm supposed to be working on.
[3213.02 → 3217.24] And so, I started to figure out, okay, mystery time.
[3217.40 → 3218.56] What is going on here?
[3219.88 → 3227.66] So, I dive into our code base, and I find the line of code in question, and everything looks legit to me.
[3227.84 → 3230.30] And then I realized, okay, I'm calling this Phoenix.
[3230.48 → 3233.98] So, we are an Elixir Phoenix application for those who haven't been following along the whole time.
[3235.78 → 3238.06] And at a certain point, we call into Phoenix.
[3238.06 → 3245.62] And Phoenix has an HTML library that generates HTML, and there's a function called link.
[3245.84 → 3250.08] So, this is, if you're familiar with, every web framework has like a link function.
[3250.28 → 3253.44] You know, link to was Rails' invention, which everybody's pretty much copied.
[3253.92 → 3255.54] Phoenix's link works very similarly.
[3256.82 → 3262.88] And so, all we're doing is calling that and just passing it the URL, which has the apostrophe in it.
[3262.88 → 3270.66] And so, I started digging a little deeper, and I started thinking, ah, it's like, whatever's happening is outside my domain, right?
[3270.72 → 3273.06] It's a dependency that's doing it.
[3274.02 → 3276.14] So, I don't know, Gerhard, what do you do in this circumstance?
[3276.68 → 3279.20] You got a dependency that's not doing something totally right?
[3279.62 → 3280.66] What's your first move?
[3282.24 → 3284.18] I guess you're more of an ops guy.
[3284.30 → 3287.56] So, maybe you haven't, your developer chops are maybe rusty, but what's your interesting?
[3287.58 → 3288.18] No, not really.
[3288.50 → 3288.92] Not really.
[3289.02 → 3289.42] Okay, good.
[3289.42 → 3294.98] So, I would look at an issue to see if there is an issue in the repo for the dev.
[3295.98 → 3302.24] I would try and find the code, see what happened around it, like I would call a blame, see if that is different.
[3303.10 → 3313.72] And if I can't find anything, I would just open an issue on that repo, explain my problem, link to my code, and ask the developers, hey, how would you solve this?
[3313.84 → 3314.42] What do you think?
[3314.68 → 3315.22] Is it legit?
[3315.86 → 3316.88] Am I holding it wrong?
[3317.60 → 3318.04] Yeah, exactly.
[3318.04 → 3318.74] What's the problem here?
[3319.42 → 3325.24] Yeah, so, the interesting thing about this one is I'm not really savvy with these character encodings.
[3325.58 → 3330.06] And I'm not sure why it's doing the HTML encoding versus the URL encoding.
[3330.54 → 3333.28] But my first question is, like, is this even a bug?
[3333.56 → 3336.36] Or is this just like the way it would work if you pass it on an apostrophe?
[3336.36 → 3343.06] And so, when I start to have these questions, you laid out a very clear path to potential victory.
[3344.06 → 3345.24] But I'm lazier than you.
[3345.30 → 3347.72] So, my first thing is, like, am I running the latest version?
[3347.98 → 3349.22] Like, that's just what I ask myself.
[3349.44 → 3353.98] You know, like, maybe this was fixed between, you know, my version and now.
[3353.98 → 3357.02] And so, my first step is, well, let's just upgrade stuff.
[3357.46 → 3362.86] And I start to, even if it's like a procrastinate coding thing, I'm like, I'm going to go check out my depths tree and see how old everything is.
[3363.18 → 3364.56] And a bunch of stuff was out of date.
[3364.56 → 3366.60] So, this begins the yak shave.
[3366.70 → 3369.02] So, instead of fixing that, I'm like, here's what I'm going to do.
[3369.10 → 3370.32] I'm going to update all of our depths.
[3370.50 → 3370.94] Update everything.
[3371.08 → 3372.02] Oh, my goodness me.
[3372.16 → 3372.36] Okay.
[3372.74 → 3373.94] What can possibly go wrong?
[3374.26 → 3374.58] Exactly.
[3375.22 → 3377.48] So, we were on Phoenix 1.5.
[3378.32 → 3379.82] And 1.6 was out.
[3380.62 → 3385.34] Most Elixir packages do a pretty good job of following semantic versioning.
[3385.44 → 3386.86] So, I knew this was a minor upgrade.
[3387.04 → 3388.38] So, there are some breaking changes.
[3388.68 → 3391.16] But, or no, a major upgrade breaks changes.
[3391.26 → 3393.06] There shouldn't have been any API changes, right?
[3393.76 → 3394.06] Mm-hmm.
[3394.52 → 3394.80] Yeah.
[3394.96 → 3396.20] So, this one kind of bit me.
[3396.26 → 3397.72] So, there were API changes.
[3397.98 → 3398.24] Okay.
[3398.50 → 3400.30] So, I thought I could just safely upgrade.
[3401.88 → 3403.56] And I did all the auto upgrades.
[3403.56 → 3409.86] So, inside of Elixir's mix tool, if you have patch version upgrades, it'll just auto do those for you.
[3409.94 → 3410.50] Like, they're green.
[3410.62 → 3412.96] You can just upgrade those because they're assuming semantic versioning.
[3413.06 → 3414.80] So, I did all those, ran the tests.
[3414.88 → 3415.56] Everything was fine.
[3416.14 → 3420.30] Then I went to upgrade Phoenix, which was a minor version upgrade, 1.5 to 1.6.
[3420.64 → 3421.62] Got that done.
[3421.72 → 3424.04] While it was kind of doing its thing, I was like, well, I'm going to go.
[3424.06 → 3426.64] I'll read the change log and see what's going on.
[3427.02 → 3432.30] And I did notice that they made a breaking change, which I guess that's not Member.
[3432.38 → 3433.34] So, they should have gone to 2.0.
[3433.34 → 3433.52] No.
[3433.72 → 3436.40] They don't want to go to 2.0 because it's too major or whatever.
[3437.06 → 3438.14] But I did notice it.
[3438.22 → 3438.44] Okay.
[3438.46 → 3440.58] And I'm like, oh, man, this is something that I need to look at.
[3440.58 → 3444.16] So, I did the upgrade to Phoenix 1.6.
[3444.80 → 3446.40] Had some failing tests.
[3446.56 → 3447.32] So, I was like, all right, good.
[3447.36 → 3450.40] My tests are testing things, and they changed the API.
[3451.36 → 3453.52] And so, I'm going to have that.
[3453.66 → 3454.62] But it's like two changes.
[3454.84 → 3456.28] So, what did they change?
[3456.28 → 3465.42] Well, the way Phoenix works is as it passes the request data from your controllers down
[3465.42 → 3470.50] into your views and to be used in the template, there's this bag of data called assigns.
[3471.20 → 3476.60] And in the assigns, there's a bunch of – it's literally a map or a struct or a dictionary
[3476.60 → 3478.90] or a hash depending on what your language choice is, right?
[3478.90 → 3480.58] And so, it's keys and values.
[3480.94 → 3487.28] And there were two keys that no longer exist, view module and view template.
[3488.06 → 3489.76] And what do these keys hold in them?
[3489.82 → 3496.32] Well, they hold in the information of what's the currently active or being used module that's
[3496.32 → 3499.10] handling this request and which template is going to be used to render.
[3500.80 → 3502.18] So, I did find those.
[3502.30 → 3503.96] There's like two places I was using those.
[3504.68 → 3505.74] And I changed them.
[3506.22 → 3507.40] And there's like a new way of doing it.
[3507.46 → 3507.62] Fine.
[3507.62 → 3509.68] And I upgrade.
[3509.98 → 3510.84] And all my tests pass.
[3511.00 → 3511.90] And so, what do I do?
[3511.94 → 3512.64] I ship it, baby.
[3512.82 → 3513.52] I send it out there.
[3514.54 → 3515.66] And it's all good.
[3515.94 → 3521.04] And then I start to realize via Twitter that our Twitter embed is broken.
[3522.28 → 3525.42] It's just showing like the default news and podcasts for developers thing.
[3526.14 → 3529.72] And like an old or like a stock share image.
[3529.84 → 3534.06] It's not doing – we actually have player embeds where you can click play right there
[3534.06 → 3535.68] on Twitter and start playing the episode.
[3535.68 → 3541.78] And so, that Phoenix upgrade, even though I thought I covered all my bases, broke all
[3541.78 → 3545.70] the metadata on all of our pages across the entire site.
[3546.38 → 3546.94] Wow.
[3547.30 → 3548.98] Which led to Twitter embeds breaking.
[3548.98 → 3554.28] All third-party integrations that are based on like the meta elements in your HTML.
[3555.08 → 3555.40] Busted.
[3557.08 → 3560.56] And so, that led to me refactoring our entire meta module.
[3562.52 → 3564.40] Because that data is gone.
[3564.50 → 3568.62] And the entire thing in that module is like, which view am I?
[3568.92 → 3570.02] And which template am I?
[3570.08 → 3570.34] Okay.
[3570.48 → 3571.48] Here's my meta information.
[3571.48 → 3574.92] And so, I refactored that entire meta module.
[3575.44 → 3576.32] Took me a few hours.
[3576.92 → 3578.58] I'm not even happy with the way it works now.
[3578.62 → 3579.48] I liked it better before.
[3580.48 → 3581.66] And I fixed it.
[3582.44 → 3585.04] And the yak was shove nor shaven.
[3585.34 → 3586.40] What's past tense for shave?
[3586.54 → 3586.90] Shaven.
[3587.30 → 3588.08] I shaved him.
[3588.30 → 3589.10] I shaved that sucker.
[3589.78 → 3591.94] But I did not get our cloud uploads done.
[3592.06 → 3592.98] So, that's my excuse.
[3593.06 → 3593.66] And I'm sticking with it.
[3593.66 → 3600.52] Well, first, you were very determined to shave this yak.
[3602.64 → 3603.34] Yes, I was.
[3603.36 → 3606.98] And I'm glad that you didn't give up until it was all done.
[3607.28 → 3608.10] Success, baby.
[3609.22 → 3609.66] Yes.
[3610.00 → 3615.70] Well, the question is, did the upgrade even shave or did it even fix the original URL issue?
[3616.22 → 3617.84] No, it's not a bug.
[3618.00 → 3619.08] It's a feature, I think.
[3622.44 → 3623.28] That's the best.
[3623.28 → 3625.28] By the way, the number is 394.
[3625.34 → 3625.76] I checked.
[3625.86 → 3626.78] It's not 393.
[3627.10 → 3627.50] Oh, sorry.
[3628.58 → 3629.00] That's okay.
[3629.26 → 3629.66] That's okay.
[3630.60 → 3634.24] Second of all, this reminds me of exactly what happened.
[3634.38 → 3636.44] Like, you said that you had to shave a yak.
[3637.36 → 3639.04] And we had to get together, right?
[3639.08 → 3639.88] Where I upgraded.
[3640.18 → 3643.72] I've set up the new version of, like, our Kubernetes deployment.
[3644.80 → 3649.70] And it's amazing how I was shaving a similar yak.
[3650.18 → 3650.48] Okay.
[3650.48 → 3654.06] You know how you do, like, an upgrade of Kubernetes, like, from 120 to 121?
[3654.14 → 3657.24] And then you think, hmm, maybe I should upgrade Ingress Nginx.
[3657.90 → 3659.86] Or, even better, I should replace it with traffic.
[3660.26 → 3660.52] Okay.
[3660.76 → 3661.12] Why?
[3661.24 → 3662.56] Because then we don't have cert manager.
[3662.96 → 3663.30] Excellent.
[3663.52 → 3665.64] So traffic can, you know, take care of all of that.
[3666.12 → 3666.38] Great.
[3667.38 → 3668.42] What about external DNS?
[3668.84 → 3669.78] Let's do that as well.
[3670.04 → 3671.06] What about Honeycomb Agent?
[3671.22 → 3672.12] Let's do that as well.
[3672.20 → 3673.12] What about your fun agent?
[3673.12 → 3673.90] Oh, crap.
[3674.28 → 3675.30] They broke something.
[3676.40 → 3679.38] So let me try and figure out, like, what the new config is.
[3679.46 → 3682.88] And before you know it, I would, like, two days, like, three days, whatever, say, ah, crap.
[3682.98 → 3683.56] Like, no, no.
[3683.60 → 3684.46] This is just too much.
[3684.50 → 3687.76] I just have to keep some of the older versions because it's just too hard.
[3687.90 → 3688.14] Right.
[3688.20 → 3689.92] And I'm biting too big of a chunk.
[3690.32 → 3690.68] Wow.
[3690.70 → 3692.34] Which is exactly what you've done, right?
[3692.88 → 3693.28] Yes.
[3693.28 → 3693.92] Before you know it.
[3693.92 → 3696.78] The yak is, like, a herd.
[3697.64 → 3697.86] Yeah.
[3698.24 → 3700.76] Somewhere in there, I completely lost the thread, you know?
[3701.26 → 3701.54] Yeah.
[3701.62 → 3704.10] It feels necessary as you keep biting more off, though, right?
[3704.62 → 3704.86] Yeah.
[3705.46 → 3707.82] As you go deeper into the yak shave.
[3708.04 → 3710.80] I mean, I guess this is an onion analogy more than a shave.
[3710.92 → 3714.22] I guess every new hair you shave away, I don't know how to describe it.
[3714.22 → 3715.56] You just, like, have to go further.
[3716.20 → 3716.76] You know what I mean?
[3716.92 → 3720.42] It just feels like it's perpetual, and you just need to keep going.
[3720.42 → 3724.30] And then it's, like, you know, it's one part, you know, personal determination.
[3725.04 → 3732.50] And then knowing you as a list, you know, X or offer, you've got to get through this thing, whatever it is.
[3732.68 → 3735.02] And so it's, like, perseverance, though.
[3735.98 → 3741.24] I'm wondering how much actual work happens like this.
[3741.44 → 3741.74] Right?
[3742.06 → 3742.26] Right.
[3742.26 → 3748.12] Like, really valuable work, like, upgrades, fixes, refactorings.
[3748.12 → 3755.10] Because you start somewhere and rather than doing the bare minimum, you say, well, I'm going to do a little bit more and a little bit more and a little.
[3755.18 → 3756.66] And before you know it, you're, like, a week in.
[3756.94 → 3757.06] Snowball.
[3757.48 → 3759.06] Everything is amazing, right?
[3759.10 → 3761.86] But you wasted a week on something which wasn't even on the board.
[3762.38 → 3762.66] Right.
[3763.04 → 3764.44] This was not even on my agenda.
[3764.52 → 3767.56] I wonder as well, because that's, like, the that's a state of flow, right?
[3767.64 → 3771.32] You can get through that yak shave probably because of a state of flow.
[3771.38 → 3774.48] How, was this a sustained session, Jared, or was it multiple sessions?
[3774.48 → 3777.26] This was all one session.
[3777.36 → 3781.52] This basically took my afternoon that I would have otherwise spent finishing that cloud uploads thing.
[3782.20 → 3784.56] Did you plan to spend the amount of time that you spent?
[3784.94 → 3788.70] So did you consume the time you desired to spend or did you just consume more?
[3789.20 → 3789.74] Way more.
[3789.88 → 3791.84] I did not want to rewrite that meta module at all.
[3792.36 → 3792.62] Right.
[3792.70 → 3793.68] So this is my point then.
[3793.74 → 3795.28] So you wanted to do it in one session.
[3795.28 → 3801.40] You were in a state of flow despite your aim, so to speak, being off, right?
[3801.46 → 3802.22] You shaved the yak.
[3802.32 → 3803.90] You didn't do what you intended to.
[3804.36 → 3817.46] However, you probably did as much work as you could have done in eight hours or whatever number, some sort of multiple beyond that, because you were in such a momentum mode, you know, kind of mode going on.
[3817.94 → 3820.12] That's my assumption at least because you were in a state of flow.
[3820.12 → 3826.10] So to your point, Jared, I wondered as well, because when you get that kind of momentum, sometimes you just have to run with it.
[3827.16 → 3830.44] So speaking of new, we've got some gifts coming up.
[3830.50 → 3833.16] It's going to be the holiday season, Christmas.
[3833.94 → 3835.64] You got some Christmas gift for us, Jared?
[3836.18 → 3836.94] I do, actually.
[3837.18 → 3839.08] I have four, five.
[3839.54 → 3840.24] We'll see how many.
[3840.68 → 3841.70] But a couple.
[3842.10 → 3842.96] More than a couple.
[3843.38 → 3843.62] Okay.
[3843.62 → 3845.62] What I'm thinking is...
[3846.36 → 3846.42] Two.
[3846.48 → 3847.26] I was mentioning...
[3847.26 → 3847.96] More than one, right?
[3848.20 → 3848.38] Yeah.
[3848.38 → 3848.54] Two.
[3848.90 → 3849.50] More than two.
[3849.58 → 3850.00] More than three.
[3850.06 → 3850.48] More than two.
[3850.60 → 3851.84] More than a few.
[3851.96 → 3852.22] Several.
[3852.40 → 3853.08] Several gifts.
[3853.52 → 3853.74] Let's go.
[3853.80 → 3854.34] Several gifts.
[3855.14 → 3867.34] So I was mentioning at the beginning of the show that a lot of the episodes, when I spend time talking to the people that come on the show, there's always a background story to it.
[3867.34 → 3873.98] Usually, like a past story, we share, you know, we have a common past, but also I see a common future.
[3874.84 → 3884.80] So what it means is when we covered cross-plane, and I was mentioning, even during the episode, that I want to make cross-plane part of our infrastructure, part of our setup.
[3885.40 → 3891.60] So what it looks like is managing our Kubernetes, managing our infrastructure with cross-plane.
[3892.28 → 3894.12] So how do we do that?
[3894.60 → 3895.48] What does that look like?
[3895.48 → 3901.50] What is the simplest thing that we can do to improve our Kubernetes deployments?
[3901.66 → 3905.52] So that when we want two, three, four, it's really simple to do that.
[3905.98 → 3910.56] What about using a bound cloud for that rather than running our own cross-plane?
[3911.18 → 3912.52] So that is one of the gifts.
[3913.36 → 3919.50] How do we use cross-plane to manage our infrastructure, our new infrastructure, the 2022 one?
[3920.28 → 3924.08] And going forward, what are the benefits of doing that?
[3924.08 → 3930.70] So we're bringing them on board with our story, with our changelog story, with our setup story that's been evolving.
[3931.76 → 3935.80] And the mix is what makes it amazing.
[3936.18 → 3942.40] Because we have the opportunity to try all these different tools out.
[3943.40 → 3946.40] Show our approach, whether it's right or wrong, doesn't matter.
[3946.40 → 3950.64] The point is, it's good enough for us, and there's always something to learn.
[3951.48 → 3953.12] We create great content.
[3953.72 → 3958.36] We promote the good stuff, the stuff that we believe in, that we use.
[3958.96 → 3961.80] And most importantly, we help it improve.
[3962.36 → 3965.04] We give feedback to those projects, to those products.
[3965.20 → 3966.56] And as a result, they improve.
[3967.24 → 3968.36] Honeycomb is another one.
[3968.78 → 3970.98] We'll have specific Honeycomb integrations.
[3971.58 → 3973.34] Dagger, I want to mention that as well.
[3973.34 → 3976.14] And that happened, like, over the last couple of weeks.
[3976.88 → 3980.86] Preparing episode 33, where a few gifts will be mentioned.
[3981.54 → 3981.94] Parka.
[3982.34 → 3983.68] I want to mention that as well.
[3983.72 → 3984.68] That actually happened today.
[3985.32 → 3991.82] So in my lunch break, we were recording that segment, which will be part of episode 33.
[3992.42 → 3993.38] And that's the parka one.
[3993.38 → 3993.82] Yeah.
[3994.24 → 4002.64] I like seeing Solomon Hikes in our pull requests slash comments back and forth on the Dagger stuff you're working on.
[4002.72 → 4005.20] I was paying attention to just that commentary.
[4005.44 → 4011.58] And so just one, you know, I think it's super cool that, you know, we've been a podcast.
[4012.04 → 4016.26] You know, Ship It is part of the network, but the network itself has been around for more than 12 years now.
[4016.26 → 4022.96] I talked to Solomon, like, way back early days of Docker, even, like, when he did that first talk to announce Docker, essentially.
[4023.88 → 4032.48] And now to be at a place to have the right kind of infrastructure for this, what was just once a Tumblr blog, happily on WordPress at one point as well.
[4033.14 → 4034.56] And worked just fine.
[4034.62 → 4036.30] Maybe we had a ton of misses there.
[4036.70 → 4038.10] Not misses, but actual misses.
[4038.28 → 4040.00] But we didn't have any caching, so we were going to go.
[4040.00 → 4055.64] So, and now to see, you know, like, this feature, Dagger, these gifts, and Solomon Hikes, whom is one of the creators of Docker, those catching up, in the comments of our pull requests.
[4056.12 → 4056.44] It's cool.
[4056.82 → 4057.30] I love that.
[4057.40 → 4058.32] I was loving seeing that.
[4058.36 → 4060.58] It's just the whole circle of life kind of thing.
[4060.58 → 4064.90] You know, like you said, even with Ship It, the pre-story and then the future story.
[4065.00 → 4069.82] Like, I love all that serendipity, Gerhard, really, coming together.
[4070.00 → 4070.80] It is a journey.
[4071.34 → 4071.92] It really is.
[4071.96 → 4073.22] And many journeys coming together.
[4073.54 → 4073.74] Yeah.
[4074.00 → 4080.66] And, you know, the little contributions that we can make to those projects, they're definitely helping us, right?
[4080.70 → 4085.62] Like, we couldn't run the infrastructure the way we do without all the great tooling that's out there.
[4086.34 → 4091.28] And I wish we had more time to try it all and to give all the feedback that we can.
[4091.28 → 4103.96] And I think that's what, like, whenever, like, you know, people pitch the idea of, like, or request an episode, like, I would like to, you know, we'd like to have this conversation.
[4103.96 → 4105.74] I'm thinking, am I excited about this?
[4105.92 → 4107.16] Is it something which I would use?
[4107.16 → 4111.46] And if the answer is no, it doesn't mean that tool is wrong.
[4111.54 → 4113.40] It means I'm not into it.
[4113.54 → 4114.50] I wouldn't use it.
[4114.96 → 4118.22] I don't see it's like, it's a no from that perspective.
[4118.78 → 4124.70] So I love trying out the things that we have on the show.
[4125.10 → 4125.76] All the people.
[4126.36 → 4127.40] Just go beyond that.
[4127.50 → 4129.80] Go beyond that conversation and see what happens.
[4130.26 → 4131.28] Literally see what happens.
[4131.66 → 4132.70] I love that stuff.
[4132.70 → 4136.52] I like bringing that feedback to them, too, you know, like in particular to Honeycomb.
[4136.96 → 4146.04] You know, I love just, or even with Dagger and Cross plane, I just love, I think we can give that kind of feedback differently than, say, a customer would.
[4146.46 → 4149.18] Or a drive-by user who's just on the free tier, for example.
[4149.52 → 4149.72] Yeah.
[4149.88 → 4151.26] You know, of whatever it might be.
[4151.62 → 4152.94] We're going to give a different layer.
[4153.36 → 4159.64] Because one, you know, to Vastly's credit, even, like, if you're a listener who works at Vastly, we're not bashing you.
[4159.64 → 4160.38] We love Vastly.
[4160.38 → 4165.24] We're just, you know, unhappy with current things or certain things, and we want to improve them.
[4165.30 → 4167.60] That doesn't mean we're negative Vastly.
[4167.66 → 4168.78] We're quite profusely.
[4169.84 → 4176.28] And I think that, you know, through the podcast and the content that comes from it and just, like, our willingness to try and be curious.
[4176.82 → 4184.36] But then put that on air on a podcast and flesh it out for the sake of ourselves as well as the listeners who are like, how are they solving these problems?
[4184.48 → 4185.60] How is Jared shaving this yak?
[4185.62 → 4186.82] How is Gerard shaving that yak?
[4186.96 → 4188.30] He has no packets lost.
[4188.40 → 4188.54] Great.
[4188.54 → 4189.06] Okay, cool.
[4189.66 → 4190.70] You know, two ISPs later.
[4191.18 → 4191.90] All that fun stuff.
[4192.10 → 4194.02] Like, that to me is, like, that's a journey.
[4194.14 → 4194.62] That's a narrative.
[4194.72 → 4195.28] That's a story.
[4195.94 → 4196.16] You know?
[4196.22 → 4201.58] And I think that we can give that feedback to Cross plane, to Honeycomb.
[4201.74 → 4205.68] And, like, even sharing, like, how we have that observability into our CDN, which we never had before.
[4205.68 → 4207.22] That is super cool.
[4207.22 → 4212.00] And, like, that may not be something that Charity and the team at Honeycomb thought about.
[4212.14 → 4213.58] Like, sure, you can observe anything, really.
[4214.08 → 4217.48] But have they considered, like, should you observe your CDN?
[4217.58 → 4221.96] Well, I think now that we have this tool in our hand, the answer is emphatically yes.
[4222.28 → 4222.78] You know?
[4222.78 → 4224.38] Especially when it's your front layer.
[4224.86 → 4224.96] Yeah.
[4225.04 → 4228.50] And it's all those ANDs, which are really exciting for me.
[4228.78 → 4233.50] So, Cross plane and Dagger, Honeycomb and Grafana Cloud.
[4233.74 → 4235.16] Most people don't think like that.
[4235.40 → 4236.46] They think, ooh, competitors.
[4236.48 → 4236.90] Either or.
[4237.10 → 4237.42] No, no.
[4237.68 → 4237.98] No, no.
[4238.02 → 4239.22] It's an and proposition.
[4239.64 → 4239.88] Right.
[4239.88 → 4242.48] Because they all have their strengths and their weaknesses.
[4242.82 → 4246.28] And if you don't know what the trade-offs are, well, that means that you don't know them well enough.
[4246.58 → 4249.58] Because there's no such tool which is just perfection, right?
[4249.62 → 4249.72] Yeah.
[4249.72 → 4250.52] There's no such thing.
[4250.80 → 4251.50] It doesn't exist.
[4251.60 → 4252.68] So, stop looking for it.
[4253.36 → 4255.92] And try and understand which trade-offs you're making.
[4256.82 → 4259.40] So, Honeycomb is helping us in specific ways.
[4259.62 → 4261.46] Grafana Cloud is helping us in other ways.
[4261.88 → 4266.00] And we'll have people on the show to talk about those things and to talk about the improvements.
[4266.00 → 4276.28] If you want to know what's coming up in episode 33, you can go to our changelog.com, the repo in GitHub, the changelog, forward slash changelog.com.
[4277.54 → 4280.96] There are a couple of pull requests opened.
[4281.58 → 4284.74] And the pull requests have Shipped It Christmas Gifts.
[4285.40 → 4287.40] It's an Echoes initiative, Echoes HQ.
[4287.80 → 4288.64] They were on the show.
[4290.20 → 4291.46] Arno was on the show.
[4292.22 → 4294.74] So, we're using Echoes for that purpose.
[4294.74 → 4297.00] And it's all coming together.
[4297.30 → 4299.16] You know, like one big happy family.
[4299.60 → 4299.94] And they're red.
[4301.22 → 4302.78] And they're red, yes, for Christmas.
[4303.08 → 4303.34] Exactly.
[4303.54 → 4304.24] Red and white, actually.
[4304.40 → 4305.96] Yes, not coincidental.
[4306.16 → 4307.80] So, like there are many things coming together.
[4308.60 → 4312.92] And Dagger is improving because of like some of the feedback that we're giving.
[4313.14 → 4314.04] Honeycomb as well.
[4315.40 → 4316.24] Cross plane as well.
[4316.64 → 4320.44] Like every single person I get to talk to, they're taking notes of what they can improve.
[4320.44 → 4320.78] Frederick.
[4320.90 → 4324.18] It was amazing to do that with him, you know, to like to give him ideas.
[4324.18 → 4336.70] Because users, end users, the ones that are paying for it, for that product, they maybe are not as patient or not as knowledgeable.
[4337.10 → 4340.76] Or not as, you know, they are maybe more entitled or rushed.
[4341.48 → 4341.50] Exactly.
[4341.50 → 4342.14] But we're not.
[4342.24 → 4344.06] Like we genuinely want to help.
[4344.18 → 4345.66] We genuinely want to promote this stuff.
[4345.90 → 4347.18] What works, what doesn't work.
[4347.24 → 4348.12] And let's make it better.
[4348.68 → 4349.34] So, Kaiden.
[4350.14 → 4350.40] Yeah.
[4350.40 → 4352.58] I love that.
[4352.90 → 4358.08] And I guess to some degree on that note, there's some, an order of thanks.
[4358.22 → 4364.20] So, we talked about this show in the initial part of the show, just the beginnings, how there were early innings.
[4364.34 → 4365.72] It was just an idea at one point.
[4365.92 → 4374.16] And as part of bringing that idea to life, you know, one, Gerhard, we had to have a deeper conversation with you and understand your desire.
[4374.16 → 4381.54] Clearly, you've realized a lot of that desire for us in your execution of Ship It, even so far to plan well ahead.
[4382.24 → 4388.82] But all that's possible because, one, our willingness, but then two, capable and willing partners behind the scenes.
[4389.54 → 4396.30] And in no particular order, I'm going to thank some people who were on the charge this year, involved next year as well.
[4396.30 → 4410.34] So, Planet Scale, Fly, Equinix Metal, Render, Linde, Ray gun, Sentry, Honeycomb, Grafana Labs, Teleport, Launch Darkly, Incident, Fire Hydrant, Cockroach Labs.
[4410.84 → 4414.44] And I'm sure at least a couple more that I may have forgotten and didn't get in the list.
[4415.00 → 4415.92] If so, I apologize.
[4416.26 → 4420.70] But great partners make it possible to do this kind of fun stuff.
[4420.90 → 4422.74] And I am so thankful for them.
[4423.42 → 4424.52] I'm so thankful for you.
[4424.52 → 4426.42] I'm so thankful for our listeners.
[4427.16 → 4430.44] You know what would this show be if it didn't have listeners, right?
[4430.64 → 4441.54] So, you're listening right now, we really appreciate you taking your time to either subscribe or listen to a segment or listen to a full-length show, even if you're not a subscriber.
[4442.18 → 4448.06] Thank you for giving us a little bit of your time, hopefully a bit of your future trust, and listen to the show further.
[4448.66 → 4451.56] We hope to one day have a beautiful vanity URL to give this.
[4451.56 → 4455.14] But until then, it's changelog.com slash ship it.
[4455.46 → 4457.40] All the links to subscribe are there.
[4457.54 → 4459.02] You can subscribe via email.
[4459.18 → 4460.28] You can come in Slack.
[4460.66 → 4461.56] Hey, there is a community.
[4461.68 → 4464.52] It is free, so you can hang your hat, call this place home.
[4465.16 → 4467.18] Everyone's welcome, no matter where you're at in your hacker journey.
[4467.50 → 4468.62] We welcome you to be here.
[4468.68 → 4469.56] There are no imposters here.
[4469.56 → 4471.26] No imposters here.
[4471.80 → 4473.92] You can go to changelog.com slash community.
[4474.38 → 4475.20] Free to join.
[4475.54 → 4476.20] Hang with us.
[4477.14 → 4477.96] I love it, man.
[4478.04 → 4480.32] I'm loving the momentum and the direction we're going.
[4480.78 → 4487.28] I think enough pats on the back, but I'm just so thankful for this team here, the listeners, our partners.
[4487.46 → 4487.94] Really, I am.
[4487.94 → 4492.02] We are just so blessed.
[4492.46 → 4493.14] Really, we are.
[4494.18 → 4495.68] To be doing this show, it's so much fun.
[4496.86 → 4497.50] Thank you, Adam.
[4497.82 → 4498.54] That was beautiful.
[4498.90 → 4499.72] Thank you very much.
[4499.98 → 4502.02] Yeah, that's reached a very special place.
[4502.58 → 4502.86] Thank you.
[4502.94 → 4503.06] Cool.
[4504.68 → 4506.92] So, 2022, here we come.
[4507.02 → 4508.54] We've got a little bit more shows left.
[4508.54 → 4512.46] But this is the last Kaiden episode.
[4512.78 → 4517.24] We'll come back here in 2022 with Kaiden, what, 40?
[4517.86 → 4518.50] Kaiden 40.
[4518.72 → 4519.16] That's the one.
[4519.76 → 4520.40] Kaiden 40.
[4520.72 → 4521.10] Mm-hmm.
[4521.84 → 4526.34] And hopefully, we'll have our Kaiden t-shirt in the merch store.
[4527.06 → 4528.82] So, stay tuned to that.
[4529.08 → 4530.98] One more gift, potentially a New Year's gift.
[4531.44 → 4532.60] Merch.changeall.com.
[4532.66 → 4534.50] Until then, we're out.
[4534.50 → 4539.76] Thank you for tuning in to another episode of Shi bit.
[4540.16 → 4542.78] This is just one of our podcasts for developers.
[4543.34 → 4546.34] Go to changelog.com forward slash master for the rest.
[4547.02 → 4551.70] You can join our community at changelog.com forward slash community.
[4552.06 → 4553.44] There are no imposters in our Slack.
[4553.78 → 4554.98] Everyone is welcome.
[4555.44 → 4559.08] Huge thanks to our partners Vastly, Launch Darkly, and Linde.
[4559.30 → 4562.70] Thank you, Break master Cylinder, for all our awesome beats.
[4563.22 → 4564.24] That's it for this week.
[4564.24 → 4565.12] See you next week.
[4565.12 → 4565.18] See you next week.
[4594.24 → 4599.00] Hey, you all.
[4599.08 → 4599.52] Jared here.
[4600.08 → 4605.02] So, during the tail end of our recording, right after I told my yak shave story, Gerhard
[4605.02 → 4606.32] pretty much broke the show.
[4606.88 → 4611.18] Turns out he's been deep on a yak shave of his own regarding his home network setup and
[4611.18 → 4613.02] some nagging internet connection issues.
[4613.02 → 4617.50] I guess my yak shave story triggered Gerhard to consider the ridiculous length he's gone
[4617.50 → 4619.94] through and, well, hilarity ensues.
[4620.56 → 4624.06] Gerhard laughs uncontrollably, which makes me laugh uncontrollably.
[4624.38 → 4628.70] Adam keeps it together and desperately attempts to get us back on track, but not going to happen.
[4629.18 → 4633.54] It was so broken that we cut it from the episode, but it was also so funny that we figured we'd
[4633.54 → 4637.82] throw it in at the end for those of you with a few extra minutes to spare and the curiosity
[4637.82 → 4640.54] to hear what it sounds like when the show goes off the rails.
[4641.04 → 4641.42] All right.
[4641.66 → 4642.18] Here it is.
[4642.80 → 4643.56] I'm sorry.
[4644.70 → 4645.18] What?
[4645.74 → 4646.54] I'm just...
[4646.54 → 4649.50] I'm just trying to hold something in.
[4650.70 → 4651.18] What?
[4651.18 → 4656.30] Something that's making Gerhard laugh huge.
[4656.50 → 4657.32] It's just too good.
[4660.16 → 4663.62] Oh, he's got a hidden thought that he can't get out because he's making him laugh too hard.
[4664.24 → 4665.28] I just remembered.
[4666.56 → 4666.96] What?
[4671.96 → 4673.00] What is it?
[4673.30 → 4674.46] I can't even look at his face.
[4674.54 → 4674.92] I'm sorry.
[4675.42 → 4676.04] It's just too good.
[4676.04 → 4676.46] I can't look at him.
[4676.50 → 4676.98] I have to look away.
[4677.12 → 4677.36] Okay.
[4677.52 → 4677.74] All right.
[4677.82 → 4678.32] What do you remember?
[4678.46 → 4679.72] If you're listening to this, try hard to look away.
[4679.72 → 4681.16] Okay.
[4681.16 → 4681.56] Got it.
[4681.58 → 4682.70] He's taking off his glasses and everything.
[4683.36 → 4685.86] It took me three weeks.
[4690.22 → 4691.22] Three weeks?
[4692.44 → 4694.04] Oh, my God, man.
[4694.56 → 4695.48] It's just too good.
[4697.74 → 4701.04] That's true determination because you not only did it...
[4701.04 → 4702.08] You didn't do it in one session.
[4702.18 → 4703.70] You did it in multiples, and you kept going.
[4704.06 → 4704.46] Multiple weeks.
[4704.94 → 4705.82] Multiple weeks.
[4705.90 → 4706.54] Three...
[4706.54 → 4706.58] Three...
[4706.58 → 4709.26] Three routers later.
[4709.72 → 4715.10] Two internet connections later.
[4717.32 → 4720.08] And now my packets aren't getting lost anymore.
[4725.16 → 4726.18] Oh, man.
[4726.18 → 4733.04] That is an extreme yak shaving.
[4733.50 → 4733.78] That is...
[4733.78 → 4735.06] I'm sorry.
[4735.62 → 4737.32] Extreme tales of yak shaving.
[4738.08 → 4738.94] That's a yak show.
[4739.54 → 4740.38] That is a yak show.
[4740.62 → 4742.88] Actually, there's like an episode with new ISP.
[4743.02 → 4744.08] I have two ISPs now.
[4744.66 → 4745.62] Both fibre connections.
[4745.78 → 4747.16] Two ISPs now.
[4747.16 → 4750.34] Yeah, like two fibre connections coming into the house.
[4751.28 → 4752.44] The razor routers.
[4754.76 → 4758.40] The funny part about this is like, you have to think about that.
[4758.44 → 4762.60] Beyond just being two ISPs, that's two separate people coming to your house to install fibre.
[4762.90 → 4763.16] Yes.
[4763.54 → 4765.24] Because that's two separate fibre lines.
[4765.46 → 4767.02] That's like true dedication.
[4767.02 → 4769.60] That's new holes into your house.
[4769.80 → 4770.86] Yeah, exactly.
[4771.18 → 4772.22] That's one more plug.
[4772.22 → 4772.68] Two holes in my wall.
[4772.80 → 4773.24] You're right.
[4773.44 → 4773.98] I have two more.
[4774.76 → 4775.12] Whatever.
[4775.46 → 4775.70] You're...
[4775.70 → 4777.66] Maybe you even have a UPS for this even, I'm sure.
[4777.80 → 4778.32] Not yet.
[4778.70 → 4779.22] Not yet.
[4779.80 → 4780.24] That's...
[4780.24 → 4781.64] Not yet.
[4783.40 → 4786.06] He just adds that to his list of things to do.
[4786.62 → 4787.14] Yeah.
[4787.14 → 4789.78] Don't give him anything else to do, Adam.
[4790.42 → 4790.78] Wow.
[4791.60 → 4793.82] I'm just thinking like the logistics of doing that.
[4793.98 → 4796.44] Like that's being on the phone to order it.
[4796.50 → 4797.96] That's deciding to pay for it.
[4798.22 → 4801.66] That's one more line on the budget, so to speak.
[4801.76 → 4801.90] Yeah.
[4802.40 → 4803.62] That's somebody coming to your house.
[4804.24 → 4805.00] New hole.
[4805.20 → 4805.84] New fibre.
[4806.58 → 4807.22] New equipment.
[4808.56 → 4808.96] Yeah.
[4809.06 → 4811.12] At least you're getting to use that WAN fill over though.
[4811.50 → 4812.16] I do, actually.
[4812.16 → 4812.88] On your unify system, which is awesome.
[4812.88 → 4813.00] I do.
[4813.00 → 4813.02] I do.
[4813.38 → 4813.76] Yeah.
[4813.88 → 4816.78] Not load balancing yet, but I'm working towards it.
[4816.78 → 4817.78] I'm sure you'll be...
[4817.78 → 4817.92] Yeah.
[4820.16 → 4820.72] All right.
[4820.72 → 4822.20] We got to reel this in.
[4822.26 → 4823.50] What's the summary here, Gerhard?
[4823.58 → 4825.22] What's the takeaway from this?
[4825.30 → 4828.14] The summary is that now I have two WAN connections.
[4831.78 → 4833.04] You've already said that part.
[4833.12 → 4833.82] What's the takeaway?
[4834.58 → 4835.88] What's the takeaway here?
[4835.94 → 4836.88] You need two of each.
[4837.96 → 4839.48] Two of everything.
[4841.92 → 4842.98] Except your wife.
[4843.06 → 4844.22] You only want one of us.
[4844.24 → 4844.82] There you go.
[4844.82 → 4845.64] That's such a joke.
[4845.80 → 4849.42] So I think we should do Gitpod and Code faces.
[4851.90 → 4852.66] Of course.
[4853.24 → 4854.18] Yeah, because you never know.
[4854.68 → 4856.36] Kubernetes, Edfly, I hope.
[4856.94 → 4857.48] And Brenda.
[4859.26 → 4860.16] That's how we roll.
[4860.56 → 4863.22] Well, I can't agree with the N+.
[4863.22 → 4864.38] I mean, that is smart.
[4864.56 → 4866.86] I mean, you can never have enough.
[4867.04 → 4869.40] Well, that was actually coined best in the movie Contact.
[4869.70 → 4870.34] Anybody remember that?
[4871.00 → 4872.38] Well, I'd build one when you could build two.
[4872.38 → 4874.20] I think I've had enough fun.
[4874.20 → 4875.46] I mean, I'm laughing.
[4875.58 → 4876.12] You might play.
[4877.86 → 4878.96] Yeah, I'll be right back.
[4883.08 → 4883.56] I'm hiding.
[4883.62 → 4885.78] I'll be r
[4885.78 → 4886.42] BYB GH in the audience.
[4886.50 → 4887.02] What's going on?
[4887.16 → 4887.24] Yeah.
[4887.34 → 4888.80] I'll be right back.
[4888.90 → 4889.18] Bye.
