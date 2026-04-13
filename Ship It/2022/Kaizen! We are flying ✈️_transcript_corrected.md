[0.16 → 5.22] Welcome to Ship It, a podcast about ops, infrastructure, and flying.
[5.70 → 8.62] This is our fifth Kaiden with Adam and Jared,
[8.94 → 12.50] where we talk about the next improvement to changelog.com.
[12.84 → 17.34] We are now running on fly.io, and the Postgres SQL is managed.
[17.82 → 22.20] This is a migration that many were curious about, including Semi the Clerk.
[22.66 → 27.12] After migrating all our MIDI files to AWS S3, check episode 40,
[27.26 → 29.96] we thought that this part was going to be easy.
[30.34 → 32.06] Plan met reality.
[32.62 → 34.86] Pull request 407 has all the details.
[35.42 → 39.92] I want to emphasize the type of partner relationships that we seek at changelog,
[40.26 → 43.44] and why they're important to us, as well as to our listeners.
[44.06 → 48.04] Honeycomb and fly.io embody the elements that we care about,
[48.36 → 51.62] and I think that we're currently missing a Kubernetes partner.
[52.10 → 56.30] Huge thanks to Vastly for shipping our episodes superfast all around the world.
[56.30 → 58.74] Check them out at fastly.com.
[60.00 → 66.96] This episode is brought to you by Sentry.
[67.12 → 72.98] Build better software faster, diagnose, fix, and optimize the performance of your code.
[73.10 → 79.04] More than a million developers in 68,000 organizations already use Sentry,
[79.10 → 80.08] and that includes us.
[80.38 → 81.92] Here's the easiest way to try Sentry.
[81.92 → 85.20] Head to Sentry.io slash demo slash sandbox.
[85.64 → 89.54] That is a fully functional version of Sentry that you can poke at.
[89.88 → 92.66] And best of all, our listeners get the team plan for free for three months.
[92.94 → 96.54] Head to Sentry.io and use the code SHIP IT when you sign up again.
[96.98 → 99.42] Sentry.io and use the code SHIP IT.
[99.42 → 107.26] We are going to send in three, two, one.
[107.26 → 122.08] We've made it.
[122.32 → 123.22] 50 episodes.
[123.44 → 127.62] Not close enough, but we made 50, which means we made one year, right?
[128.18 → 129.28] Minus the Christmas.
[129.80 → 130.90] I think there's like one more.
[131.22 → 134.54] 52 would be in exactly one calendar year.
[134.88 → 136.72] So 50 for us marks the year.
[136.90 → 138.58] Well, 50 is the number we're shooting for, right?
[138.64 → 140.14] I mean, you want to take two weeks off in a year.
[140.22 → 144.98] So we optimize for every show who is a weekly show to do 50 episodes in a year.
[145.10 → 147.22] So, I mean, that's one, that's consistency.
[147.38 → 149.10] And two, that's congratulations, right?
[149.16 → 150.94] Like to keep a podcast consistent.
[151.18 → 151.84] Well played, Gerhard.
[151.94 → 152.96] Well played, sir.
[153.24 → 154.06] And hitting the mark.
[154.26 → 155.50] I mean, it's a feat of nature.
[155.68 → 157.50] Most podcasts die.
[157.84 → 158.46] Yours did not.
[158.46 → 159.54] So congratulations.
[159.54 → 161.08] Okay, I survived.
[162.30 → 164.98] Is this like the squid game sort of thing?
[165.94 → 167.46] I survived this round.
[167.94 → 170.84] How many podcasts have we produced, Gerhard, that did die?
[171.32 → 173.10] Like because of burnout?
[173.46 → 174.02] None, right?
[174.12 → 177.10] I mean, Request for Commits ended.
[177.16 → 178.46] Not because of burnout, I guess.
[178.66 → 180.54] But we have some shows that didn't make it to 50.
[180.94 → 181.42] That's true.
[182.14 → 183.26] Away from Keyboard didn't.
[183.48 → 184.96] Brain Science, 20 episodes.
[185.20 → 186.08] Brain Science didn't.
[186.32 → 188.64] RFC, Request for Commits, 20 episodes.
[188.64 → 190.68] But 50 episodes is a big deal.
[191.40 → 193.20] Spotlight, I think, got to like 15.
[193.32 → 197.52] And then we merged it back into the changelog and started doing backstage, which I think
[197.52 → 199.12] is at like 23 episodes.
[199.12 → 200.58] And that's been going on for years.
[200.82 → 202.70] So Gerhard's killing backstage.
[203.38 → 203.58] Yeah.
[203.58 → 206.08] Long story short, congratulations.
[206.72 → 209.46] And, you know, to you, Gerhard and the listeners for sticking around.
[209.62 → 212.64] Like it's one thing to put your faith in a brand-new show.
[212.74 → 214.66] It's another to keep coming back.
[215.00 → 219.98] And based on the listens, based on the traction of the show, you found your audience, which
[219.98 → 220.38] is awesome.
[220.62 → 220.74] Yeah.
[220.74 → 221.84] I'm really enjoying it.
[221.92 → 222.50] I have to say.
[222.78 → 227.12] It's been a year, and it doesn't feel that it's been a year, which is really weird.
[227.34 → 233.38] I was looking at, because every year I try to look at the themes, like what is still relevant,
[233.90 → 234.86] what is still with us.
[235.20 → 240.18] And looking back at the first episodes, I realized, wow, some of those, it's been a year.
[240.60 → 241.68] It was like yesterday.
[241.84 → 243.20] It felt like some of those conversations.
[243.54 → 246.20] I guess it's too soon to have some of those people back.
[246.64 → 248.56] So this is one for the audience.
[248.90 → 252.62] In the 50 episodes, if there's one that you really enjoy, and you want that person to be
[252.62 → 254.46] back or those people to be back, let us know.
[255.00 → 257.14] I'll be more than happy to have them back.
[257.18 → 261.88] And I know that they will enjoy it too, because we had so much fun in every single episode.
[262.36 → 265.66] And the easy way to do that is gone to changelaw.com slash request.
[265.98 → 271.26] You can do that for every show, not just this show, but in particular, changelaw.com slash request.
[271.26 → 273.84] So request a BS back, as we call them.
[274.18 → 275.00] Who should be back?
[275.00 → 276.72] Yeah, that's a great one.
[277.02 → 282.04] Also, this episode initially, when we intended it, like we knew it was going to come, right?
[282.06 → 282.84] Like the next Kaiden.
[283.20 → 284.56] I really liked that regularity.
[284.78 → 286.58] I like that every 10, we're back with a Kaiden.
[287.02 → 289.12] But this one was actually a request.
[289.64 → 291.80] And things just like worked out that way.
[291.96 → 294.94] So this one was a request from Semi Leclerc.
[295.16 → 296.16] At the end of February.
[296.42 → 297.34] Ah, Semi.
[297.34 → 297.62] Yeah.
[297.80 → 298.76] Semi was asking.
[299.34 → 302.88] So he wrote, the change law DevOps seems complicated.
[303.30 → 310.54] Yet a lot of past providers want us to believe we can just slap in all of their services and only worry about scaling much later.
[310.54 → 315.10] So he was wondering is what would happen if change law just ran on Heroku?
[315.46 → 318.24] How much of the current setup is necessary to support the current scale?
[318.30 → 321.46] And how much of it is overengineering needing out?
[321.86 → 324.96] So we get to answer your questions, Semi, in this episode.
[325.22 → 327.62] Ah, the plot thickens.
[327.62 → 328.02] Yes.
[328.60 → 329.08] How so?
[329.16 → 330.02] Are we on Heroku now?
[330.16 → 331.24] Ah, we're on a pass.
[331.62 → 332.54] So that's the spoiler.
[332.76 → 334.08] Like, spoiler, we're on a pass.
[334.20 → 335.28] It's not Heroku, it's Fly.io.
[335.28 → 336.28] We're on a pass.
[336.36 → 337.48] Hence, we are flying.
[337.76 → 338.76] We're literally flying.
[338.90 → 339.56] And figuratively.
[339.86 → 341.92] But literally, the app is flying.
[342.46 → 347.04] In the last Kaiden episode 40, we talked about migrating all our static assets to AWS S3.
[347.18 → 349.12] And that was one of the steps in this direction.
[349.38 → 351.66] And the background story is in pull request 400.
[351.94 → 353.00] You can check the code.
[353.44 → 356.42] And we even did some Kaiden driven development during the recording.
[356.42 → 360.30] Jared was adding some CD and shielding live on the show, as you do.
[360.74 → 361.18] Why not?
[361.34 → 366.16] Like, you know, to shield the S3 origin, to keep the AWS costs under control.
[366.40 → 367.98] And that was a really fun one.
[368.04 → 369.22] I was not expecting that.
[369.34 → 370.82] Like, it was literally not planned out.
[370.86 → 371.44] It just happened.
[371.80 → 372.62] I love that.
[373.02 → 373.90] Well, that's how we roll.
[374.02 → 377.94] You know, we turn it on, and we let it alone until mid-show.
[378.38 → 380.86] When I think it was Adam that asked about the cost.
[380.94 → 382.84] And I was like, maybe I should check that real quick.
[382.86 → 384.94] Because we set it and forget it.
[384.94 → 386.74] I think it was like six or seven days later.
[386.86 → 392.52] Which one listener, I think, kind of called us out for, you know, bad DevOps practices there.
[392.66 → 393.28] That's my bad.
[393.36 → 394.46] I'll take full ownership.
[394.84 → 400.30] And found out, you know, yeah, we're paying 1,900% more on our AWS bill than the previous month.
[400.30 → 402.56] Which was never a fun surprise.
[402.70 → 405.20] But one that you want to have sooner rather than later.
[405.20 → 407.96] So props on Adam for triggering me.
[408.16 → 411.70] And then I guess props to me for turning shielding on really fast.
[411.70 → 414.64] Which cut it down immediately to about half.
[415.06 → 418.46] But we were still overpaying for a couple of reasons.
[418.46 → 423.78] So I spent a few hours over the next couple of days making sure that we're holding S3 right.
[423.78 → 428.22] Which was a combination of the shielding changes inside Vastly, like we said.
[428.30 → 434.38] As well as setting the proper surrogate cache control keys inside our application.
[434.58 → 437.00] When we upload to Vastly.
[437.20 → 439.18] Because, or sorry, when we upload to S3.
[439.42 → 446.68] Because S3 has to signal to Vastly how often to break the cache and do the full request again.
[447.00 → 449.50] And then we also can tell Vastly how long to do it.
[449.50 → 451.92] So there's like multiple layers of caching here.
[452.04 → 454.00] And as we all know, cache invalidation.
[454.16 → 455.94] One of the hard problems of computer science.
[456.26 → 457.70] But we're just layering them on.
[457.78 → 458.54] And it took a few days.
[459.06 → 461.24] But we ended up getting it fixed.
[461.24 → 464.84] I think in January we paid around $600 for S3.
[465.04 → 467.76] And that was the month that we turned it on at the end of the month.
[467.98 → 472.88] And so we were pacing to spend about two grand a month on S3.
[473.28 → 476.78] And then after the changes in February we paid $92.85.
[476.78 → 479.44] And in March it's down to $44.20.
[479.68 → 481.04] And we don't have April's bill yet.
[481.10 → 483.64] So we're expecting around $50 a month for S3.
[483.84 → 486.44] Which is totally reasonable and sustainable.
[486.70 → 490.16] Whereas $2,000 a month for the size of our business was not.
[490.54 → 492.36] I would say thanks for Kaiden too.
[492.42 → 495.18] Because if we didn't have this Kaiden kind of ritual.
[495.66 → 497.32] I would even say like a constraint.
[497.74 → 500.36] You know, we would have asked that question when we got the bill.
[500.40 → 501.56] Yeah, we would have.
[501.76 → 504.04] Which could have been, you know, enormous.
[504.64 → 505.96] So thank you for Kaiden.
[505.96 → 510.68] From my perspective, there are just a few manual things that you have to do.
[511.02 → 514.60] That I didn't expect you to have to do with S3.
[514.74 → 516.40] Specifically setting those cache headers.
[516.88 → 519.46] Which you have to go out of your way with the command line tools.
[519.94 → 524.02] And with the way they were uploading these static assets to S3.
[524.16 → 527.90] So like our uploads were getting the correct surrogate control header set.
[528.04 → 530.80] But our static assets, which we just switched, were not.
[531.28 → 534.92] And there was just way more to it than I had ever had to do before.
[534.92 → 543.56] I guess because I have not used S3 on a website that gets the amount of traffic that we get specifically to our MP3s.
[543.56 → 545.64] So I want to mention a couple of things.
[545.76 → 550.28] First, I don't think many people realize just how big of a scale changelog is.
[550.66 → 556.52] So if you had to guess in how many gigabytes we serve per day, how many would you say it is?
[556.64 → 560.04] I mean, maybe Jared, if you already know, I'm not going to ask you, but maybe Adam.
[560.42 → 563.58] I mean, I'm not sure when you looked last, but I checked this before the show.
[563.88 → 566.16] So how many gigabytes do you think we serve per day?
[566.16 → 567.24] I'm going to guess for real.
[567.40 → 573.56] I would say knowing the size of our content and how much throughput we have, it's probably close to a terabyte, I would say.
[574.06 → 577.46] You know, it's probably still in gigs, but like close to a terabyte, I would say, per day.
[577.56 → 577.80] Okay.
[578.18 → 578.42] Jared?
[578.68 → 579.30] Am I way off?
[579.50 → 581.14] No, I'm not looking at it, but I have looked at it.
[581.16 → 582.32] I think that's high.
[582.68 → 583.12] Am I right?
[583.30 → 583.80] Is that high?
[583.88 → 587.60] It's actually 1.5 terabytes on a regular day.
[587.80 → 590.68] And it spikes to 2 terabytes, 3 terabytes on a busy day.
[590.68 → 590.84] Wow.
[591.08 → 595.20] So we are averaging 1.6 terabytes per day.
[595.72 → 596.80] Well, those are prices right out when.
[596.94 → 597.12] Yeah.
[597.52 → 598.44] Adam wins for sure.
[598.78 → 599.66] Adam wins this one.
[600.16 → 610.80] So can you imagine if our caching wasn't right, how expensive our S3 bill would be, like per day, based on how much stuff we serve, and how slow it would be if our CDN didn't work correctly.
[610.96 → 617.54] So big props to Vastly, as complicated as, you know, sometimes we pick on it, and we'll pick on this episode as well.
[617.88 → 618.62] Sorry about that.
[618.62 → 627.00] But just to say something nice, which is also true, like Vastly really fronts a lot of traffic from all over the world.
[627.50 → 630.34] Like Asia gets a lot of traffic, Taiwan especially.
[630.80 → 634.14] Taiwan all of a sudden, yeah, which is somewhat new for us, I think.
[634.34 → 634.56] Yeah.
[634.82 → 638.10] I mean, for some reason, ship it, Jared mentioned too, it's really popular in Taiwan.
[638.12 → 638.66] Big in Taiwan.
[638.86 → 639.06] Yeah.
[639.48 → 640.54] Like not big in Japan.
[640.70 → 643.42] I was a bit disappointed, but big in Taiwan, so it's okay.
[643.86 → 644.04] Yeah.
[644.36 → 645.16] Come on, Japan.
[645.58 → 646.08] Let's ship it.
[646.08 → 653.36] So if we average that from 1.5 a day to 30, like there are 30 days in a month, so you're saying that on a given day, even weekends is still 1.5?
[653.42 → 655.18] Would it be fair to average 1.5?
[655.26 → 658.62] Or what would a good daily average be to extrapolate that?
[658.70 → 663.34] If we go, let's see, I had this open before, so we'll need to get this one up.
[663.34 → 665.14] I was like, what's the total then?
[665.22 → 667.34] So is the total like 45 terabytes a month?
[667.50 → 673.24] In March, all of March, we had 45.6 terabytes in all of March.
[673.40 → 674.24] That's serious, man.
[674.56 → 676.06] It's some serious traffic, exactly.
[676.34 → 680.64] Like we have some serious traffic is what I'm trying to say, but I mean, I can check this out anyway.
[680.82 → 682.96] Maybe we'll do like a screenshot later.
[682.96 → 689.60] And for context, our episodes range from like 40 megabytes on the low end to maybe 100 megabytes on the high end.
[689.74 → 695.62] So these are larger than images, but these are not like video sized files by any means.
[695.94 → 700.08] And a lot of the times like ranges are being served, so like not full episodes.
[700.08 → 711.00] Like for example, I tend to listen to an episode and I listen to your, the one episode with Brian Kernighan, I think like four times now as I was like walking to the post office because I had a couple of trips.
[711.26 → 713.48] So I listen like five minutes here, 10 minutes there.
[713.54 → 717.40] I'm still like halfway through it, but I've been like working on it for about a week now.
[717.68 → 720.70] And I imagine that many people do the same thing.
[720.76 → 725.08] And that's why there's like a lot of ranges being served, but still it's a serious amount of traffic.
[725.08 → 732.44] So if CDN, if you were holding the CDN wrong, we would really see that as we did in the case of S3, or we were holding S3 wrong.
[732.52 → 733.24] I forget which one.
[733.32 → 736.52] Anyway, we were holding something wrong or at least one thing wrong.
[736.70 → 737.36] So there's that.
[737.66 → 738.56] Well, we're holding it right now.
[738.64 → 739.68] So that, that feels good.
[739.86 → 742.12] So we switched to Fly.io.
[742.32 → 743.42] That's our new origin.
[743.92 → 752.08] There's like a nice story there, but I'm curious when we did this migration from LIKE to Fly.io, do you notice any change, Adam?
[752.62 → 754.42] Did the app behave any different?
[754.42 → 756.58] Do you push changes differently?
[757.08 → 757.90] What did you notice?
[758.20 → 761.42] I haven't shipped any changes to the code base since the move.
[761.74 → 764.60] So on that front, the answer is no, because I haven't yet.
[765.00 → 770.20] I assume I'll just ship to master as I do before, and it same builds pipeline as planned.
[770.36 → 773.44] In terms of the app, I haven't hit any errors.
[773.72 → 777.10] I haven't noticed anything really necessarily positive or negative.
[777.20 → 778.76] I think that's probably the best thing you want, right?
[778.82 → 782.96] Like if you do make a major change that there are no bumps or hurdles.
[782.96 → 784.82] The site was always fast.
[785.28 → 786.90] I mean, that's one thing.
[787.00 → 790.22] So I haven't noticed anything really, which I think is a positive.
[790.50 → 791.02] It is a positive.
[791.16 → 792.78] That's why this work is called Invisible.
[793.16 → 795.44] If you do your job right, you don't see anything.
[795.70 → 799.66] So there's like all these big changes, but nothing changes from the perspective of users.
[799.88 → 801.00] Users see the same thing.
[801.26 → 803.20] No downtime, nothing like that.
[803.58 → 804.68] Well, we did have some downtime.
[804.76 → 807.10] But anyway, we will leave that for a little bit later.
[807.10 → 808.12] But nobody noticed.
[808.42 → 809.44] Yeah, nobody noticed.
[810.02 → 812.80] And there's a good reason why it's been designed that way.
[813.14 → 814.12] But what about you, Jared?
[814.20 → 815.38] Because you work a lot closer.
[815.56 → 816.78] Did you notice any changes?
[817.30 → 817.64] Oh, yeah.
[817.98 → 822.68] So from an end user perspective using the application or from a developer perspective?
[823.08 → 824.56] You can start with whichever you want.
[824.74 → 827.98] So end user perspective, it was pretty similar.
[828.10 → 832.00] Of course, no surprise there because Vastly is fronting every request for the most part.
[832.00 → 836.30] On the admin, however, we bypass Vastly.
[836.36 → 840.40] We still send through Vastly, but we don't actually let Vastly cache anything.
[840.96 → 847.64] And I would say slight just anecdotal speed improvements on the back end, my perspective.
[847.88 → 848.06] Okay.
[848.38 → 853.88] We did have the robots.txt issue, which came out of this, which was problematic.
[854.26 → 856.38] And we dug into, and I fixed that one.
[856.56 → 859.14] We could talk the details if you want to on that or skip over it.
[859.20 → 859.58] Either way.
[859.58 → 865.46] That was the biggest, I think, technical bug that cropped up due to the switch.
[865.78 → 866.60] Do you know how I found that?
[866.72 → 869.48] I randomly just searched us changelog media on Google.
[869.60 → 871.04] I'm like, whoa, that looks weird.
[871.26 → 871.48] Yeah.
[871.88 → 873.96] So I think I was telling somebody like our full business name.
[874.00 → 875.82] And I was like, what are they going to find if they go Google this?
[876.12 → 878.08] Changelog media, like versus just changelog.
[878.26 → 880.80] And obviously the results were weird looking.
[881.40 → 881.66] Yeah.
[881.82 → 882.92] And that was the result.
[883.06 → 884.54] Just a little bit of detail there.
[884.62 → 887.96] So we basically, our robots.txt is dynamically served.
[887.96 → 890.50] Which I wouldn't do normally.
[891.18 → 899.86] But we want the ability to have these limitless subdomains for testing and previews and migrations.
[900.18 → 903.36] Gerhard likes 21.changelog.com, 22.etc.
[903.64 → 906.34] There's a WWW, which gets redirected, stuff like that.
[906.70 → 911.10] And if it was me, I would redirect all those to the Apex domain and say, you can't do that.
[911.18 → 912.00] No, don't do that.
[912.08 → 913.14] But Gerhard wants that.
[913.14 → 915.72] And I'm like, all right, especially if we're having like previews and stuff.
[916.00 → 917.06] I understand the reasoning.
[917.44 → 921.62] But unfortunately, Google was starting to index some of those subdomains.
[921.68 → 923.68] And they have the same exact content as the main domain.
[924.06 → 925.70] And that's not great for SEO.
[926.30 → 929.18] And the way our canonical stuff works, I just didn't want to have it.
[929.30 → 936.22] So we have dynamicrobots.txt, which is the text changelog.com, it's going to serve the one that we're used to.
[936.22 → 941.88] Which is like, allow everything except for like, ignore the admin, ignore some stuff, even though you have to be signed in, just whatever.
[942.00 → 943.46] There's a few ignores, but mostly just allow.
[943.98 → 948.00] And then if it detects not that, then it's like, hey, disallow all.
[948.52 → 950.66] Don't index 22.changelog.com.
[950.66 → 959.02] And the way that dynamicrobots.txt works requires the host header to sniff the origin domain.
[959.54 → 965.78] And we lost that in transition over to Fly because it's like, I had to switch to, do you remember what it was, the key?
[965.96 → 968.32] There's another X forwarded header, something like that.
[968.42 → 969.28] X forwarded host, maybe?
[969.62 → 970.62] X forwarded host, that's right.
[970.66 → 975.84] And so we began after the Fly migration to block Google from indexing our entire website.
[976.20 → 976.94] So that's no good.
[976.94 → 981.40] And it didn't actually affect our search traffic for a while.
[981.54 → 984.32] I think maybe Google just took a while to actually do its thing.
[984.40 → 986.88] And then eventually Adam noticed that it did.
[986.96 → 988.62] And I dug in there and got that fixed.
[988.68 → 990.30] So that was not great.
[990.86 → 993.40] And I almost think that it's the way I coded it.
[993.40 → 1001.18] If I could code it open by default, but then closed, if you detect the abnormal circumstance, I think it would have been fine.
[1001.38 → 1006.58] But that's a lot harder because then we have to have like a list of domains, of subdomains that we detect.
[1006.58 → 1011.22] And the way I did it was like closed by default, but open if I detect the right origin.
[1011.96 → 1012.98] And that busted.
[1013.32 → 1014.22] So fixed.
[1014.60 → 1016.08] But that was definitely like a...
[1016.08 → 1016.72] That was a big one.
[1016.90 → 1017.44] Holy cow.
[1017.58 → 1020.12] Get the text editor out and fix it right away kind of thing.
[1020.22 → 1021.50] It's not like, oh, no big deal.
[1021.70 → 1022.18] That was bad.
[1022.54 → 1028.90] It's stuff like that, which unless you make these big changes, you forget that they even exist.
[1028.90 → 1033.82] And the problem is like you have quite a few of those in your code base, especially if it's more complicated.
[1033.82 → 1037.36] If you're like many people touching it, making changes basically.
[1038.20 → 1043.74] And in our case, because we make these changes fairly frequently, at least once a year, right?
[1043.74 → 1046.46] We're migrating from one Kubernetes to another.
[1046.46 → 1048.64] But this time we change platforms.
[1049.00 → 1053.24] And because we change platforms, we are using the fly.dev domain.
[1053.72 → 1060.18] So we have liked all traffic coming to WWW or the apex changelog.com goes through Vastly.
[1060.28 → 1061.36] There's the entry point.
[1061.66 → 1067.06] But then we have those origins, which if you want to bypass Vastly, you can go directly to the origin.
[1067.06 → 1069.76] So we had 22.changelog.com.
[1070.02 → 1077.08] And that used to resolve to a node balancer, a little node balancer, which would be provisioned via LIKE.
[1077.62 → 1078.44] We'll have an ingress.
[1079.00 → 1081.04] And that's how that used to work before.
[1081.26 → 1084.90] But when we migrated to Fly, we no longer have the changelog domain.
[1084.98 → 1086.18] We're using the fly.dev domain.
[1086.54 → 1092.56] And once we did that, a bunch of stuff broke, especially this one, like the robots text.
[1092.56 → 1095.68] So I think there's something to improve for us.
[1096.02 → 1098.18] And I'm wondering what that improvement looks like.
[1098.28 → 1099.62] We don't have to talk about it now.
[1099.88 → 1105.40] But it's something I definitely want to dig into as a pull request, as a follow-up, whatever that looks like.
[1105.68 → 1107.24] But that is an important one.
[1107.52 → 1110.26] Because I would like us to have multiple origins.
[1110.98 → 1112.88] Like Fly is one, but should we have more?
[1112.94 → 1114.88] We talked about multi-platform for a while.
[1115.30 → 1120.14] And while I don't think we'll do that in a rush, I still think we would like to be open to that.
[1120.14 → 1122.68] So we're not, you know, flying nothing else.
[1123.08 → 1123.64] We like it.
[1123.72 → 1124.38] It's great.
[1124.78 → 1127.34] But, you know, so we thought the same about LIKE.
[1127.56 → 1128.66] And it was for a while.
[1128.86 → 1129.54] And we enjoyed it.
[1129.62 → 1130.88] But then something else comes along.
[1130.94 → 1132.10] And then it makes more sense.
[1132.58 → 1133.54] And we try it.
[1133.82 → 1134.60] And then we like it.
[1134.84 → 1138.48] So the idea being these improvements make a lot of sense.
[1138.76 → 1140.38] I wish we knew about that.
[1140.58 → 1141.42] But you don't.
[1141.52 → 1142.50] And that's what happens.
[1142.58 → 1143.44] Like same thing with S3.
[1143.52 → 1144.74] There's like the unknown unknowns.
[1145.42 → 1148.80] There's no way you will know how it's going to affect until you make the change.
[1148.80 → 1153.08] And that's why when we did the migration, at the last step of switching traffic, we realized,
[1153.26 → 1156.08] oh crap, there's this problem in the VCL config.
[1156.18 → 1158.62] But maybe we don't talk about that just yet.
[1158.90 → 1162.18] And we talk about other changes that we noticed since migrating.
[1162.30 → 1166.84] So one thing which I noticed today as I was editing episodes, this is as an end user,
[1167.34 → 1171.44] I noticed that I had to save an episode multiple times to see a change.
[1171.80 → 1173.04] So I was doing some edits.
[1173.62 → 1174.44] Episode 49.
[1175.32 → 1175.80] Save.
[1176.26 → 1177.20] Refresh the page.
[1177.20 → 1178.60] The changes weren't there.
[1179.10 → 1179.96] I thought it was caching.
[1180.50 → 1182.34] But then I was bypassing quickly.
[1182.36 → 1183.46] I went directly to the origin.
[1183.94 → 1188.16] So it's a nice way to be able to rule the CDN out and everything's still working.
[1188.54 → 1190.72] And for some reason, the page was not updating.
[1190.98 → 1196.54] And only when I saved it again, like the second time, even though nothing changed, then it updated.
[1197.00 → 1198.88] It might be the app.
[1198.98 → 1199.24] Maybe.
[1199.32 → 1199.66] I don't know.
[1199.74 → 1202.86] Maybe Jared knows there's like some caching, something happening.
[1202.86 → 1209.10] Because the one component which is new that we didn't have before is now we have the fly proxy.
[1209.52 → 1211.70] The fly proxy is the equivalent of the ingress nginx.
[1211.78 → 1215.54] And I'm not sure how that behaves because we don't have any logs from it.
[1215.86 → 1216.64] That's like a request.
[1217.02 → 1218.68] And we'll talk to Mark about it.
[1218.90 → 1221.82] But we can't see what's happening in that proxy layer.
[1221.88 → 1223.02] It's like an invisible component.
[1223.02 → 1226.30] So maybe this is something happening at that layer.
[1226.46 → 1227.28] But we don't see that.
[1227.54 → 1228.64] I haven't experienced that.
[1228.96 → 1231.22] But I would say that it's definitely not in the app.
[1231.28 → 1234.48] I think we've used the app extensively at this point.
[1234.54 → 1235.44] I've never seen that.
[1235.84 → 1237.54] And so I would think that's probably infrastructure.
[1237.80 → 1241.54] And the code around the Blackman episode form hasn't changed for years.
[1241.72 → 1243.50] So I would expect that to be infra.
[1243.80 → 1244.08] Okay.
[1244.42 → 1246.00] Or your internet connection, Gerhard.
[1246.08 → 1247.38] It could be your internet connection.
[1247.46 → 1248.56] No, it's definitely not.
[1249.30 → 1250.96] Like, it really isn't.
[1250.96 → 1253.56] And we're not opening that can of worms now.
[1254.70 → 1256.82] We need like a whole episode just for that.
[1256.96 → 1257.86] But no, it's not that.
[1258.06 → 1258.34] So anyway.
[1258.84 → 1259.44] We kind of did.
[1259.70 → 1263.14] So I'm suspecting something happening at a fly proxy.
[1263.36 → 1265.20] But it's something to look into for sure.
[1265.36 → 1268.38] I mean, that must be a really complicated piece of tech.
[1268.62 → 1273.24] Because it fronts all the whole traffic to the different fly apps, right?
[1273.26 → 1273.88] That you have running.
[1274.14 → 1275.06] All the instances.
[1275.66 → 1276.06] Everything.
[1276.46 → 1280.14] But the other thing which I noticed, and I think this talks about speed,
[1280.14 → 1282.26] is the missed latency.
[1282.82 → 1287.30] So when the requests in the CDN, we can't serve them from the CDN,
[1287.36 → 1288.46] and they have to go to the origin.
[1288.94 → 1291.60] That went up to 250 milliseconds.
[1291.80 → 1294.44] So we can see that in the Vastly metrics.
[1295.10 → 1296.96] And it used to be 115 milliseconds.
[1297.14 → 1298.70] So it's more than twice as high.
[1299.00 → 1301.42] And maybe it's not big enough for you to notice.
[1301.88 → 1303.98] But I'm really wondering, like, what is happening there?
[1304.06 → 1306.74] Now, the other thing which we changed is we remove shielding.
[1306.94 → 1308.08] So we no longer have shielding.
[1308.08 → 1312.84] So what that means is that any requests going to a Vastly pop,
[1313.16 → 1314.26] it has to go to the origin.
[1314.50 → 1317.12] It can't go to a shield, another, like, Vastly pop,
[1317.24 → 1320.42] which basically has it in the cache, maybe.
[1320.92 → 1321.06] Right.
[1321.36 → 1325.62] So that's, for clarity, that's shielding on the changelog.com domain or origin,
[1325.76 → 1328.68] not on the CDN.changelog.com, which goes to S3.
[1328.92 → 1330.44] So shielding there is on.
[1330.92 → 1332.30] Shielding on changelog.com is off.
[1332.36 → 1333.58] It used to be on for both.
[1333.96 → 1334.16] Yeah.
[1334.16 → 1337.00] So we're hitting fly more than we were hitting Kubernetes.
[1337.46 → 1337.82] Exactly.
[1338.12 → 1338.26] Yeah.
[1338.34 → 1342.04] Like, before we weren't hitting Ingress Nginx as much as we're hitting the fly proxy.
[1342.38 → 1343.40] So that's the one thing.
[1343.46 → 1347.50] But again, I suspect that if we had more details from the fly proxy,
[1347.58 → 1348.40] we would be able to tell,
[1348.48 → 1350.52] because that's, like, one blind spot that we don't see,
[1350.62 → 1351.94] or one component that we don't see.
[1351.94 → 1371.28] This episode is brought to you by our friends at Fire Hydrant.
[1371.28 → 1374.34] Fire Hydrant is the reliability platform for every developer.
[1374.74 → 1378.56] Incidents, they impact everyone, not just Sees.
[1378.56 → 1382.80] They give teams the tools to maintain service catalogues, respond to incidents,
[1382.98 → 1386.44] communicate through status pages, and learn with retrospectives.
[1386.80 → 1390.88] What would normally be manual error-prone tasks across the entire spectrum
[1390.88 → 1392.22] of responding to an incident,
[1392.48 → 1395.72] they can all be automated in every way with Fire Hydrant.
[1395.72 → 1399.90] They have incident tooling to manage incidents of any type with any severity,
[1400.30 → 1404.72] with consistency, declare and mitigate incidents all from inside Slack.
[1404.72 → 1408.12] Service catalogues allow service owners to improve operational maturity
[1408.12 → 1411.58] and document all your deployments in your service catalogue.
[1412.04 → 1414.64] Incident analytics allow you to extract meaningful insights
[1414.64 → 1417.58] about your reliability over any facet of your incident
[1417.58 → 1419.40] or the people who respond to them.
[1419.76 → 1421.58] And at the heart of it all, incident run books,
[1421.68 → 1423.70] they let you create custom automation rules,
[1423.94 → 1427.84] convert manual tasks into automated, reliable, repeatable sequences
[1427.84 → 1429.18] that run when you want.
[1429.52 → 1431.84] You can create Slack channels, Jira tickets, Zoom bridges
[1431.84 → 1433.56] instantly after declaring an incident.
[1433.56 → 1436.64] Now your processes can be consistent and automatic.
[1437.10 → 1438.76] The next step is to try it free.
[1438.90 → 1441.60] Small teams, up to 10 people, can get started for free
[1441.60 → 1443.28] with all Fire Hydrant features included.
[1443.62 → 1445.02] No credit card is required.
[1445.46 → 1447.64] Get started at firehydrant.io.
[1447.96 → 1449.92] Again, firehydrant.io.
[1449.92 → 1462.82] Okay, so you must be wondering,
[1463.04 → 1465.58] why did we really need to migrate off Kubernetes?
[1465.78 → 1467.10] Because we've been talking about Kubernetes,
[1467.18 → 1470.20] or I have been talking about Kubernetes for like 49 episodes,
[1470.20 → 1471.56] and all of a sudden I'm telling you,
[1471.66 → 1471.80] what?
[1472.02 → 1473.20] We switched from Kubernetes.
[1473.20 → 1476.32] And it's not because SBI asked.
[1476.42 → 1477.10] Just to be clear,
[1478.40 → 1480.44] SBI asking, like, why don't we use a pass?
[1480.62 → 1483.18] It just so happened that it fit, right?
[1483.36 → 1486.12] You're telling me this whole thing is not because of an episode request?
[1486.36 → 1487.06] No, no, no, no, no.
[1487.06 → 1488.62] Because I mean, that would be as listener first
[1488.62 → 1489.94] as you could possibly get, right?
[1490.06 → 1490.24] Yeah.
[1490.28 → 1490.76] Yeah, I mean.
[1491.32 → 1493.60] Reminds me, we have another episode request that says,
[1493.66 → 1495.96] well, you should rewrite your platform in Clojure.
[1496.42 → 1496.44] So.
[1496.54 → 1497.60] Go to AWS Lambda.
[1499.10 → 1500.42] See you two years later.
[1500.42 → 1502.52] Why is this not written in Go?
[1502.68 → 1503.74] Okay, I guess we'll restart.
[1503.94 → 1504.38] There you go.
[1504.46 → 1504.86] Or Rust.
[1505.02 → 1506.16] No, even back to Rust, right?
[1506.22 → 1506.60] For sure.
[1506.82 → 1507.24] Or both.
[1507.28 → 1508.90] I would say there are multiple layers to this.
[1508.96 → 1509.22] Why?
[1509.54 → 1510.90] Honestly, like there are multiple layers.
[1511.00 → 1512.92] There's going to be layers from you, Gerhard, you, Jared,
[1512.98 → 1513.92] and there are layers from me.
[1514.32 → 1515.92] And then obviously from the listener's perspective,
[1516.12 → 1516.88] it's thinking like, okay,
[1516.88 → 1520.96] why is this seemingly just a podcast host app
[1520.96 → 1522.16] running Kubernetes?
[1522.98 → 1525.00] Question of like, you know, what's the deal here?
[1525.00 → 1525.28] So.
[1525.66 → 1527.40] Which we definitely tread on that ground some,
[1527.56 → 1529.12] but okay, who wants to go first?
[1529.16 → 1529.98] Why do we do this?
[1529.98 → 1531.12] Who wants to kick it off?
[1531.56 → 1532.94] Alphabetical order, I propose.
[1533.30 → 1533.50] Yeah.
[1533.50 → 1534.76] I'll go Adam.
[1534.90 → 1535.50] Adam's first.
[1535.98 → 1538.12] I think for me, the reason,
[1538.26 → 1539.78] because I mean, I think I resisted.
[1539.84 → 1541.42] I pushed back on the two of you
[1541.42 → 1544.78] on a possible change for a while
[1544.78 → 1546.80] because at the core of our business,
[1546.80 → 1548.40] we really thrive on great partnerships.
[1548.82 → 1549.80] Vastly has been a great partnership.
[1550.00 → 1551.76] We talked about how they fronted our traffic,
[1551.88 → 1553.24] how much traffic they front for us.
[1553.36 → 1554.80] And it's really amazing.
[1554.92 → 1556.78] And I think we're uniquely positioned
[1556.78 → 1558.92] in our business as podcasters
[1558.92 → 1560.32] that also talk about tech,
[1560.46 → 1563.32] in particular software and how it works
[1563.32 → 1564.04] and how it's deployed
[1564.04 → 1565.78] and how it affects teams,
[1565.84 → 1567.02] how it affects the future,
[1567.20 → 1569.86] the innovation, open source business.
[1569.86 → 1571.28] I mean, all the different angles.
[1572.10 → 1573.04] And so at the heart of our business,
[1573.04 → 1574.92] we really thrive on great partnerships.
[1575.64 → 1577.08] And Linde had been a great partner
[1577.08 → 1577.84] for many years.
[1578.52 → 1579.54] And they were recently acquired
[1579.54 → 1581.26] and there's nothing negative about Linde.
[1581.34 → 1582.70] They're still an amazing team.
[1583.24 → 1584.52] But I think we,
[1585.04 → 1586.04] to the nerd out question,
[1586.40 → 1587.52] we wanted to nerd out
[1587.52 → 1588.74] at several layers deeper.
[1589.10 → 1591.00] And we just didn't have that opportunity
[1591.00 → 1592.88] at Linde with Kubernetes
[1592.88 → 1594.32] quite like we could.
[1595.28 → 1595.86] And, you know,
[1595.94 → 1596.52] lo and behold,
[1596.52 → 1597.26] about a year ago,
[1597.32 → 1599.36] I was reintroduced to Kurt Mickey.
[1599.92 → 1600.54] Jared, you spoke with him
[1600.54 → 1602.50] on the changelog solo a while back.
[1602.70 → 1604.46] He's got lots of interesting roots
[1604.46 → 1605.84] that cross ours from Ars Technica
[1605.84 → 1607.20] to, you know,
[1607.36 → 1609.42] compose with the IBM acquisition
[1609.42 → 1611.28] and just a lot of history there.
[1611.46 → 1613.30] And don't buy my nasally cold,
[1613.40 → 1613.86] by the way.
[1614.02 → 1614.94] So if you hear me out of breath,
[1614.98 → 1615.98] I kind of am out of breath.
[1616.04 → 1616.66] So bear with me.
[1616.72 → 1618.60] But I was reintroduced to him
[1618.60 → 1619.86] and really fell in love
[1619.86 → 1621.08] with how he approaches
[1621.08 → 1622.92] this fly platform
[1622.92 → 1624.48] and the way he desires
[1624.48 → 1625.64] to engage with developers.
[1626.48 → 1628.52] And then obviously the influence
[1628.52 → 1630.50] they've had over Elixir
[1630.50 → 1631.64] and some of the roots
[1631.64 → 1632.70] they've sort of planted there
[1632.70 → 1633.84] and the depth they go
[1633.84 → 1634.62] with different frameworks
[1634.62 → 1635.32] and platforms,
[1635.32 → 1637.18] I think was really attractive to me.
[1637.26 → 1638.44] And they're also really just fun
[1638.44 → 1639.30] and easy to work with.
[1639.70 → 1641.40] And from a nerd out perspective,
[1642.02 → 1643.08] I think it's going to be fun
[1643.08 → 1644.86] to be flying with them
[1644.86 → 1645.72] and to, you know,
[1645.74 → 1647.08] to help them improve that platform
[1647.08 → 1648.50] and obviously to bear
[1648.50 → 1649.18] some of those benefits.
[1649.18 → 1650.78] So why from my perspective
[1650.78 → 1654.40] is we desire great
[1654.40 → 1656.36] and deep relational partnerships.
[1656.36 → 1657.96] And so because of that,
[1658.00 → 1658.98] we had this opportunity
[1658.98 → 1660.18] and this curiosity
[1660.18 → 1661.58] and the possibility
[1661.58 → 1662.64] of a better way
[1662.64 → 1663.38] for our application.
[1663.58 → 1664.78] So there's just a lot of
[1664.78 → 1666.42] multiple win-win-wins
[1666.42 → 1667.30] to just say,
[1667.74 → 1668.74] yeah, let's do this.
[1668.84 → 1671.10] And so that's my reason for why.
[1671.64 → 1672.16] That's a good one.
[1672.22 → 1673.16] That hits some really
[1673.16 → 1674.12] important aspects.
[1674.38 → 1675.76] For me, it was a couple of things.
[1676.14 → 1677.00] One recent one,
[1677.20 → 1678.14] Kelsey was mentioning [1678.14 → 1679.60] having a managed PostgreSQL.
[1680.02 → 1680.88] And I was thinking,
[1680.98 → 1682.54] yeah, like why don't we do that?
[1682.60 → 1683.54] Like, why don't we just go
[1683.54 → 1684.92] and get a managed PostgreSQL
[1684.92 → 1685.52] from somewhere?
[1686.08 → 1686.98] I know that we talked
[1686.98 → 1688.66] about Cockroach DB for a while,
[1688.90 → 1689.32] but that just,
[1689.54 → 1690.56] the change is too big.
[1691.18 → 1691.86] I remember Jared
[1691.86 → 1693.84] pushing a little bit back on that.
[1693.92 → 1695.10] Like, is there something small
[1695.10 → 1696.36] that we can do as a first step?
[1696.96 → 1698.02] So, they know it.
[1698.18 → 1699.60] I think that MySQL
[1699.60 → 1700.74] is in private beta
[1700.74 → 1702.00] or it was in private beta
[1702.00 → 1702.94] when I last looked at it.
[1703.04 → 1705.08] Maybe it has not been made available
[1705.08 → 1706.56] more widely in more locations,
[1706.86 → 1707.64] but they didn't have
[1707.64 → 1708.76] and they still don't have
[1708.76 → 1709.70] PostgreSQL today.
[1710.24 → 1711.42] And that may seem
[1711.42 → 1712.24] like a small thing,
[1712.30 → 1713.68] but we did have quite a few issues
[1713.68 → 1714.46] with PostgreSQL
[1714.46 → 1716.06] and we had downtime
[1716.06 → 1716.80] because of it.
[1717.24 → 1717.90] We, you know,
[1717.94 → 1719.28] went Kubernetes operators
[1719.28 → 1721.82] and it's just a complex problem,
[1721.82 → 1723.12] which should we really
[1723.12 → 1724.50] be spending any time on?
[1724.62 → 1725.62] And the answer is no.
[1725.98 → 1726.50] And, you know,
[1726.56 → 1727.98] Kelsey put it very nicely
[1727.98 → 1728.82] in episode 44
[1728.82 → 1729.84] why we shouldn't do that.
[1729.98 → 1731.24] And it really got me thinking,
[1731.38 → 1732.92] like, what is the holdout?
[1733.00 → 1734.00] Like, why are we doing this?
[1734.26 → 1735.12] So, that was one thing.
[1735.26 → 1736.18] The other thing was
[1736.18 → 1737.24] the forced migration.
[1737.84 → 1739.08] I really did not like that,
[1739.12 → 1739.72] I have to say.
[1739.90 → 1740.82] Say more about that.
[1741.06 → 1743.10] So, mid-January this year,
[1743.34 → 1745.04] we got an end-of-life notice
[1745.04 → 1746.22] for Kubernetes 120
[1746.22 → 1747.28] and I knew it was coming,
[1747.38 → 1748.40] so it wasn't a surprise,
[1748.90 → 1749.94] but we just had to upgrade.
[1750.34 → 1751.58] And at that point,
[1751.66 → 1753.84] we spun up another 122 cluster
[1753.84 → 1754.60] because we, you know,
[1754.66 → 1756.82] we run two off everything,
[1757.22 → 1757.66] more or less.
[1758.04 → 1759.38] So, a few things happened since then.
[1759.44 → 1759.58] You know,
[1759.58 → 1760.82] we just couldn't complete the migration,
[1760.98 → 1762.38] but it was a testing run
[1762.38 → 1763.56] for the S3 assets.
[1763.84 → 1764.74] I remember us testing,
[1764.90 → 1766.92] like, does this app work correctly
[1766.92 → 1768.48] in its final setting
[1768.48 → 1770.10] with the S3 assets.
[1770.44 → 1772.04] And that really helped
[1772.04 → 1773.28] and everything worked,
[1773.32 → 1774.06] so it was fine,
[1774.12 → 1775.16] but we still had a couple
[1775.16 → 1775.96] of components missing,
[1775.96 → 1776.82] so we couldn't just, like,
[1776.90 → 1778.36] do the migration.
[1778.72 → 1779.36] Mid-March,
[1779.54 → 1781.80] we got a final end-of-life notice
[1781.80 → 1782.74] for Kubernetes 120,
[1783.18 → 1784.50] which is what was running production,
[1784.70 → 1785.84] changelog.com, the origin.
[1786.12 → 1787.66] And if we didn't upgrade
[1787.66 → 1789.24] in the next 48 hours,
[1789.76 → 1790.90] we would have been forced
[1790.90 → 1792.22] to upgrade to 121.
[1792.44 → 1793.62] And we couldn't stop the upgrade.
[1793.62 → 1794.62] I reached out to support.
[1794.72 → 1795.30] The answer was,
[1795.74 → 1796.64] you either upgrade it
[1796.64 → 1798.10] or we forced upgrade it.
[1798.22 → 1799.32] Now, the problem with that
[1799.32 → 1800.60] was that we had
[1800.60 → 1802.34] the PostgreSQL data.
[1802.56 → 1802.72] See?
[1802.94 → 1804.50] It keeps coming back to it.
[1804.80 → 1805.74] We were storing it
[1805.74 → 1806.56] on the local storage.
[1806.68 → 1806.88] Why?
[1806.98 → 1808.70] Because it was the most reliable
[1808.70 → 1810.76] configuration for our database.
[1811.16 → 1812.38] When we used the block storage,
[1812.46 → 1813.18] when we used the volume,
[1813.68 → 1814.76] we had all sorts of issues
[1814.76 → 1816.36] with volumes not detaching correctly.
[1816.90 → 1818.16] And I know these were early days,
[1818.38 → 1820.30] but we had issues around,
[1820.36 → 1821.96] like, not having NVMe drives.
[1821.96 → 1823.14] I mean, that has changed
[1823.14 → 1824.28] in the meantime.
[1824.40 → 1824.76] So there are, like,
[1824.76 → 1825.64] certain limitations
[1825.64 → 1826.98] which were preventing us
[1826.98 → 1828.08] from using PostgreSQL
[1828.08 → 1829.58] the way it's meant to be used
[1829.58 → 1830.68] in Kubernetes.
[1831.16 → 1832.24] And it just goes to show
[1832.24 → 1833.02] it's a hard problem.
[1833.32 → 1835.38] So if we had let the upgrade,
[1835.48 → 1836.12] the force upgrade,
[1836.24 → 1836.76] go through,
[1836.98 → 1837.80] we would have, like,
[1837.84 → 1838.78] everything would have been broken.
[1839.32 → 1840.06] It would have been, like,
[1840.10 → 1841.50] in a mad scramble to fix it.
[1841.74 → 1842.74] And no one wants to do that
[1842.74 → 1843.88] because then you do mistakes.
[1844.10 → 1844.80] You know, that was, like,
[1844.82 → 1845.28] I think in the middle
[1845.28 → 1846.26] of the night for me.
[1846.36 → 1847.04] It was just, like,
[1847.08 → 1849.26] an awkward way to go about it.
[1849.26 → 1850.64] And we already had this
[1850.64 → 1852.04] 122 cluster set up.
[1852.14 → 1853.76] So why can't we just use that?
[1854.08 → 1855.52] So I think to cut
[1855.52 → 1856.50] the long story short,
[1856.96 → 1857.96] this force upgrade
[1857.96 → 1859.00] was not nice.
[1859.56 → 1860.70] And having, like,
[1860.76 → 1861.14] this, like,
[1861.24 → 1862.88] and asking, like,
[1862.90 → 1864.12] hey, can we defer this?
[1864.20 → 1864.74] Like, can we just, like,
[1864.78 → 1865.78] it's just a matter of a few days.
[1865.94 → 1866.92] Because the big thing,
[1866.98 → 1867.54] and I think this is, like,
[1867.54 → 1867.94] the backstory
[1867.94 → 1869.10] that people are missing,
[1869.72 → 1870.60] I just joined Dagger.
[1870.88 → 1872.78] We were launching Dagger.
[1873.08 → 1874.76] It was a crazy couple of months.
[1874.96 → 1876.10] And I couldn't have,
[1876.28 → 1877.54] I didn't have any spare cycles
[1877.54 → 1878.40] to do this.
[1878.68 → 1879.08] It's not because
[1879.08 → 1879.92] I didn't want to.
[1880.50 → 1881.66] I was looking forward to that,
[1881.70 → 1882.40] but I was always, like,
[1882.50 → 1883.78] pushed to do things.
[1883.80 → 1884.08] I was like,
[1884.40 → 1885.14] when I'll have time,
[1885.20 → 1885.86] I'll get to it.
[1886.00 → 1886.22] Okay?
[1886.24 → 1886.90] But not now.
[1887.56 → 1889.12] And that pressure was just,
[1889.58 → 1889.84] you know,
[1890.08 → 1890.36] like,
[1890.50 → 1891.46] whenever you're under pressure,
[1891.56 → 1891.82] it doesn't matter
[1891.82 → 1892.80] how much experience you are,
[1892.84 → 1894.46] it just takes the joy out of it.
[1894.62 → 1895.54] And that's why we did it.
[1895.58 → 1896.46] Like, we did it for the learnings.
[1896.48 → 1897.16] We did it for the joy.
[1897.16 → 1897.86] We did it for, you know,
[1897.90 → 1898.66] this is fun.
[1899.10 → 1900.60] It's not work, work.
[1900.88 → 1901.12] You know,
[1901.12 → 1902.48] we're doing this for the learnings.
[1902.80 → 1903.04] So,
[1903.50 → 1903.90] I think,
[1904.08 → 1905.24] and there's a couple more,
[1905.24 → 1907.18] but I'll let Jared go next.
[1907.32 → 1907.42] Well,
[1907.42 → 1908.48] I want to throw one thing in there too
[1908.48 → 1910.50] because I think this is part of
[1910.50 → 1912.14] the frustration we have
[1912.14 → 1912.48] because
[1912.48 → 1914.92] if we had a deeper partnership
[1914.92 → 1916.40] at the nerd out level,
[1916.50 → 1918.60] this may not have been quite a problem
[1918.60 → 1919.86] because if you have empathy
[1919.86 → 1920.74] from your partner,
[1920.98 → 1921.98] and I'm not saying that
[1921.98 → 1922.74] Linde is bad.
[1922.78 → 1923.74] I'm not trying to say they're bad.
[1924.04 → 1925.66] We just didn't have that kind of access,
[1925.78 → 1926.70] which is what we desired.
[1927.10 → 1929.20] And that's why working with Fly makes sense.
[1929.46 → 1931.16] That's why this why makes sense to me.
[1931.46 → 1932.64] Because if we had that,
[1932.72 → 1933.20] if we could say,
[1933.32 → 1934.22] here's our challenge,
[1934.22 → 1936.44] we're in the middle of something else.
[1936.54 → 1937.52] We can't make this
[1937.52 → 1938.70] and this force upgrade is really,
[1938.70 → 1939.74] you know,
[1940.50 → 1941.96] Bogart in our abilities right now.
[1942.26 → 1942.50] Well,
[1942.66 → 1943.70] if you have that
[1943.70 → 1945.38] deeper level partnership,
[1945.56 → 1946.42] deeper level access
[1946.42 → 1947.74] to those who can
[1947.74 → 1949.28] not force you to upgrade,
[1949.68 → 1951.20] then there might be an easy yes
[1951.20 → 1952.64] because we had like zero empathy.
[1952.90 → 1953.54] It was support.
[1953.66 → 1954.98] It was just support.
[1955.16 → 1955.68] We didn't have
[1955.68 → 1957.64] an advocate for us
[1957.64 → 1959.16] technically inside Linde
[1959.16 → 1960.50] having our back.
[1960.50 → 1961.66] And that to me
[1961.66 → 1962.56] is challenging
[1962.56 → 1963.52] because we desire
[1963.52 → 1964.56] to partner at that level
[1964.56 → 1966.86] because of this show
[1966.86 → 1967.60] and what we do.
[1967.86 → 1968.98] And that's why it makes sense for us.
[1969.02 → 1970.26] So if we had that,
[1970.50 → 1971.74] it may have been a different story
[1971.74 → 1972.20] necessarily.
[1972.20 → 1973.00] We may not have gotten
[1973.00 → 1974.32] curious to go and say,
[1974.38 → 1975.12] well, maybe this past
[1975.12 → 1975.74] makes more sense.
[1975.80 → 1976.40] We really desire
[1976.40 → 1977.62] just that deeper partnership.
[1977.72 → 1978.76] And that's what we have now.
[1978.98 → 1980.06] I'm sure if there was something
[1980.06 → 1981.98] happening on the fly platform
[1981.98 → 1982.96] in the next year
[1982.96 → 1984.74] and it was going to,
[1985.06 → 1985.34] you know,
[1985.40 → 1986.48] there would be some work around.
[1986.54 → 1987.34] We would have some sort of
[1987.34 → 1987.76] handholding,
[1987.76 → 1988.42] some sort of guidance,
[1988.56 → 1989.84] some sort of empathy
[1989.84 → 1990.40] and forgiveness
[1990.40 → 1991.50] in the process.
[1992.18 → 1993.62] Well, everything I will add
[1993.62 → 1994.14] is additive
[1994.14 → 1995.64] because I'm well aware
[1995.64 → 1997.08] of both of what
[1997.08 → 1997.90] you have both said.
[1998.28 → 2000.34] So those reasons,
[2000.34 → 2000.82] I think,
[2000.84 → 2001.64] are actually enough.
[2002.04 → 2003.46] But from my perspective
[2003.46 → 2004.84] and why I've been excited
[2004.84 → 2006.58] about this shift
[2006.58 → 2008.70] is because I'm a Heroku fanboy
[2008.70 → 2009.54] from way back.
[2009.72 → 2010.00] I mean,
[2010.38 → 2010.98] I'm an old school
[2010.98 → 2011.52] sis admin.
[2012.04 → 2012.70] I was like,
[2012.76 → 2013.20] you know,
[2013.26 → 2014.44] SSH into the machine,
[2014.76 → 2015.82] set up some cron jobs,
[2016.24 → 2016.50] you know,
[2016.58 → 2017.32] copy the stuff,
[2017.32 → 2018.56] sync the things,
[2019.10 → 2020.08] backup the database.
[2020.66 → 2022.06] And once I didn't have
[2022.06 → 2023.28] to do that stuff anymore
[2023.28 → 2024.22] with Heroku,
[2025.14 → 2026.02] I never wanted to do
[2026.02 → 2026.58] any of that stuff
[2026.58 → 2027.14] ever again.
[2027.44 → 2028.80] I am a loyal listener
[2028.80 → 2029.28] of Ship It,
[2029.32 → 2030.36] but I don't do any of the things
[2030.36 → 2031.48] that you guys talk about doing
[2031.48 → 2031.98] on Ship It.
[2032.10 → 2033.14] I just like your show,
[2033.22 → 2033.42] Gerhard.
[2033.54 → 2035.24] But once Heroku came around,
[2035.30 → 2035.82] I was just like,
[2035.88 → 2036.08] yeah,
[2036.18 → 2037.04] let's just let Heroku
[2037.04 → 2037.82] do all the things.
[2038.12 → 2039.96] And when it came to Elixir,
[2040.08 → 2040.78] I lost that
[2040.78 → 2041.80] when we were like
[2041.80 → 2042.66] going to go deploy
[2042.66 → 2043.26] this Elixir app.
[2043.36 → 2043.84] And so that's when
[2043.84 → 2044.46] I brought you in
[2044.46 → 2044.94] to help me
[2044.94 → 2045.54] and do the things
[2045.54 → 2046.76] that I used to be okay at,
[2046.76 → 2047.64] but also don't know
[2047.64 → 2048.68] how to do things
[2048.68 → 2049.34] well anymore
[2049.34 → 2050.42] and in this ecosystem
[2050.42 → 2051.94] and thus began
[2051.94 → 2052.94] our story.
[2053.32 → 2054.62] When it came to
[2054.62 → 2055.52] Ansible,
[2055.68 → 2056.82] I was along for the ride.
[2057.08 → 2057.86] When it came to
[2057.86 → 2058.56] Concourse CI,
[2058.92 → 2059.70] I was just riding
[2059.70 → 2060.38] your coattails.
[2060.60 → 2061.52] When it came to
[2061.52 → 2061.96] Kubernetes,
[2062.18 → 2062.62] I was like,
[2062.72 → 2063.52] I hope Gerhard
[2063.52 → 2064.28] knows what he's doing
[2064.28 → 2065.16] because I don't,
[2065.34 → 2065.54] right?
[2065.54 → 2067.76] And so just the Heroku
[2067.76 → 2069.70] style paths for me
[2069.70 → 2070.32] is exciting
[2070.32 → 2071.20] because it's like a
[2071.46 → 2072.20] I feel like it's
[2072.20 → 2073.70] a pool that's shallow
[2073.70 → 2074.48] enough that I can
[2074.48 → 2075.84] swim in it safely
[2075.84 → 2077.54] and not have to turn
[2077.54 → 2078.26] to you and say,
[2078.38 → 2079.36] what's the cube
[2079.36 → 2080.00] cuddle thing
[2080.00 → 2081.02] or the canines
[2081.02 → 2081.92] thing?
[2081.92 → 2082.88] Because those are just,
[2083.34 → 2083.64] yeah,
[2083.64 → 2084.34] those are just areas
[2084.34 → 2085.66] that I don't normally
[2085.66 → 2087.08] swim that deep in.
[2087.52 → 2088.84] And just being back
[2088.84 → 2089.88] on this short time,
[2089.88 → 2090.42] like I've been able
[2090.42 → 2091.08] to figure out some
[2091.08 → 2091.94] stuff of myself
[2091.94 → 2093.22] and do things
[2093.22 → 2093.68] the way,
[2093.76 → 2093.94] I mean,
[2093.96 → 2095.66] it's not as polished
[2095.66 → 2096.14] as Heroku.
[2096.28 → 2097.00] I might get into
[2097.00 → 2097.74] some of those details,
[2098.18 → 2099.14] but it feels familiar.
[2099.64 → 2100.14] And for me,
[2100.22 → 2100.98] my mental model
[2100.98 → 2102.82] is so much simpler
[2102.82 → 2104.34] and it's not
[2104.34 → 2105.48] for any reason,
[2105.54 → 2106.06] I don't think,
[2106.26 → 2106.74] except for that
[2106.74 → 2107.60] I never acquired
[2107.60 → 2108.32] the knowledge,
[2108.50 → 2109.08] the deep knowledge
[2109.08 → 2110.40] of the other platform.
[2110.92 → 2112.64] And so this is something
[2112.64 → 2113.64] I feel like I can grok
[2113.64 → 2114.94] more simply
[2114.94 → 2116.64] and administer
[2116.64 → 2117.50] without you.
[2117.82 → 2118.78] And even the other day,
[2118.80 → 2119.54] I asked you a question,
[2119.64 → 2120.26] you weren't around,
[2120.48 → 2121.46] I figured it out,
[2121.46 → 2121.96] you know,
[2122.22 → 2122.88] and there were a couple
[2122.88 → 2124.30] times in the previous
[2124.30 → 2125.42] setups where I was like,
[2125.44 → 2126.22] I asked you a question,
[2126.80 → 2127.42] you don't answer
[2127.42 → 2128.32] because you're working
[2128.32 → 2128.70] or whatever,
[2129.10 → 2130.16] and I try to figure it out
[2130.16 → 2130.62] and I'm like,
[2130.92 → 2131.80] nah, I'll just wait.
[2131.96 → 2132.76] I'll just wait for Gerhard.
[2133.20 → 2135.28] And so that for me is,
[2135.60 → 2136.18] that's exciting
[2136.18 → 2137.50] about simplifying
[2137.50 → 2138.36] for me
[2138.36 → 2139.44] so that I can do more stuff.
[2139.74 → 2140.38] That is a big one.
[2140.46 → 2141.06] That is a big one
[2141.06 → 2142.12] because what I'm hearing is
[2142.12 → 2143.82] I did not build a platform
[2143.82 → 2145.00] that Jared needs
[2145.00 → 2146.36] for obvious reasons.
[2147.50 → 2148.36] So is there one
[2148.36 → 2149.04] that we could use
[2149.04 → 2149.72] that would work?
[2149.72 → 2151.18] And Fly definitely
[2151.18 → 2151.98] fits that bill.
[2152.40 → 2153.24] But just to mention,
[2153.54 → 2153.98] just like,
[2154.08 → 2154.36] again,
[2154.82 → 2155.44] the additive,
[2155.74 → 2156.48] just like to keep
[2156.48 → 2157.86] that point of view
[2157.86 → 2159.14] to what Adam said,
[2159.40 → 2159.96] the interaction
[2159.96 → 2160.94] that we had with Fly
[2160.94 → 2162.10] was amazing.
[2162.38 → 2163.28] We had a Slack channel,
[2163.52 → 2164.82] we were able to talk
[2164.82 → 2165.26] to Kurt,
[2165.48 → 2166.22] we were able to talk
[2166.22 → 2166.74] to Mark,
[2166.84 → 2167.36] we were able to,
[2167.40 → 2167.62] I think,
[2167.70 → 2168.08] Joshua.
[2168.50 → 2169.44] There was like someone else
[2169.44 → 2170.60] and I forget their names
[2170.60 → 2171.86] but everyone was so helpful.
[2172.06 → 2173.14] Everyone was there.
[2173.44 → 2173.68] Like,
[2173.68 → 2174.46] we had an issue
[2174.46 → 2175.70] and it was fixed
[2175.70 → 2176.54] like next day
[2176.54 → 2177.42] and this was like
[2177.42 → 2178.06] a genuine issue
[2178.06 → 2178.70] on the platform.
[2178.88 → 2179.90] So they're iterating.
[2180.08 → 2180.62] There's even like
[2180.62 → 2181.90] comments on the PR
[2181.90 → 2182.74] from Kurt,
[2182.98 → 2183.32] you know?
[2183.42 → 2183.76] Exactly.
[2183.94 → 2184.42] So it's like
[2184.42 → 2185.78] there's a feedback loop
[2185.78 → 2187.22] which we just did not have.
[2187.38 → 2187.66] So,
[2187.78 → 2188.20] yeah,
[2188.24 → 2188.42] I mean,
[2188.46 → 2190.10] that's the PR 407.
[2190.26 → 2191.10] You can go and check it out
[2191.10 → 2192.96] but there's one more thing
[2192.96 → 2193.86] which I think
[2193.86 → 2195.18] you will want to stick out for.
[2195.42 → 2195.92] So we said that
[2195.92 → 2197.14] we migrated to Fly.io
[2197.14 → 2198.68] not the first time.
[2199.26 → 2200.16] That didn't work
[2200.16 → 2201.20] and it had nothing
[2201.20 → 2202.06] to do with Fly.io.
[2202.06 → 2203.70] So we ended up going
[2203.70 → 2204.82] from Kubernetes 120
[2204.82 → 2206.58] to 122
[2206.58 → 2208.54] at 4am in the morning
[2208.54 → 2210.62] because Vastly
[2210.62 → 2211.18] and Fly
[2211.18 → 2212.06] just did not work.
[2213.00 → 2214.00] It was not going to work.
[2214.24 → 2215.34] So like 4am
[2215.34 → 2216.16] I'm just like
[2216.16 → 2217.40] all Kubernetes
[2217.40 → 2218.00] with this
[2218.00 → 2218.70] because that's what
[2218.70 → 2219.54] I know time it
[2219.54 → 2220.44] that's going to work.
[2221.46 → 2221.86] And there's like
[2221.86 → 2223.04] an issue between Vastly
[2223.04 → 2223.48] and Fly
[2223.48 → 2224.02] and I was like
[2224.02 → 2224.58] too late
[2224.58 → 2225.44] and I can't be bothered
[2225.44 → 2226.56] just want to go to sleep
[2226.56 → 2226.90] you know,
[2226.96 → 2227.32] whatever.
[2228.32 → 2228.86] PaaS is meant
[2228.86 → 2229.70] to be easier
[2229.70 → 2230.12] right?
[2230.16 → 2230.66] Or easy
[2230.66 → 2231.46] and it wasn't.
[2231.46 → 2232.08] Now again
[2232.08 → 2232.78] just to be clear
[2232.78 → 2233.64] it was not
[2233.64 → 2234.74] a Fly.io issue
[2234.74 → 2235.30] it had nothing
[2235.30 → 2236.16] to do with Fly.io.
[2236.26 → 2236.78] I should say
[2236.78 → 2237.54] that I was with you
[2237.54 → 2238.54] so it was your 4am
[2238.54 → 2239.30] for me, it was like
[2239.30 → 2240.24] 8.30pm
[2240.24 → 2240.86] 9pm
[2240.86 → 2242.22] and I was sick that day
[2242.22 → 2243.34] and so I was like
[2243.34 → 2243.96] I can't believe
[2243.96 → 2244.76] this is happening right now
[2244.76 → 2245.92] I knew that you were
[2245.92 → 2246.64] it was like
[2246.64 → 2248.22] the middle of the morning
[2248.22 → 2248.68] for you
[2248.68 → 2249.48] and when you said
[2249.48 → 2250.30] let's just go back
[2250.30 → 2251.46] and do the LK upgrade
[2251.46 → 2252.08] I'm like
[2252.08 → 2252.92] yes
[2252.92 → 2254.02] let's just do that
[2254.02 → 2254.54] and was it
[2254.54 → 2254.92] it was like
[2254.92 → 2256.08] 15 minutes later
[2256.08 → 2256.88] it was done
[2256.88 → 2257.78] like we were done
[2257.78 → 2258.80] and that was amazing.
[2259.16 → 2259.52] So we had like
[2259.52 → 2260.40] all this plan
[2260.40 → 2260.66] right?
[2260.66 → 2262.02] I had like all the steps
[2262.02 → 2262.82] and I had like even like
[2262.82 → 2263.76] an incident running
[2263.76 → 2264.48] it's all there
[2264.48 → 2265.28] you can check out
[2265.28 → 2266.18] PR407
[2266.18 → 2267.60] and just like when we were
[2267.60 → 2269.22] adding the Fly origin
[2269.22 → 2271.76] into the Vastly config
[2271.76 → 2273.26] everything blew up
[2273.26 → 2274.46] and what I mean by that
[2274.46 → 2275.36] the requests
[2275.36 → 2277.22] that were not cached
[2277.22 → 2279.42] they were trying to be served
[2279.42 → 2280.84] from AWS S3
[2280.84 → 2282.46] so like admin pages
[2282.46 → 2284.70] and like news impressions
[2284.70 → 2286.24] and any dynamic content
[2286.24 → 2287.90] was getting 404s
[2287.90 → 2289.64] because AWS S3
[2289.64 → 2290.52] did not have
[2290.52 → 2291.60] that resource
[2291.60 → 2292.64] that's how it was behaving
[2292.64 → 2293.96] like what is going on
[2293.96 → 2294.54] like the config
[2294.54 → 2295.38] it looks good
[2295.38 → 2297.42] like this makes no sense
[2297.42 → 2298.18] so
[2298.18 → 2299.66] what was the problem?
[2299.82 → 2300.56] The problem was
[2300.56 → 2302.00] a VCL misconfiguration
[2302.00 → 2303.48] this was in Vastly config
[2303.48 → 2304.92] one of the subroutines
[2304.92 → 2305.94] was getting terminated
[2305.94 → 2306.68] before the backend
[2306.68 → 2307.40] was being set
[2307.40 → 2308.74] and I'm still
[2308.74 → 2309.68] not clear
[2309.68 → 2310.48] whether that was
[2310.48 → 2311.38] the actual issue
[2311.38 → 2312.56] why?
[2313.08 → 2313.76] Because you have
[2313.76 → 2315.68] 12,000 lines
[2315.68 → 2316.98] of VCL config
[2316.98 → 2318.86] 11.5,000
[2318.86 → 2319.98] is just gibberish
[2319.98 → 2320.78] because it's all
[2320.78 → 2321.46] the origins
[2321.46 → 2323.52] all the various shields
[2323.52 → 2324.88] and only 500
[2324.88 → 2326.00] is the actual config
[2326.00 → 2326.72] so you have like
[2326.72 → 2327.46] do some dimming
[2327.46 → 2328.40] some like you know
[2328.40 → 2329.12] like you know
[2329.12 → 2330.02] like just like
[2330.02 → 2331.12] remove a lot of lines
[2331.12 → 2332.52] and then it's like
[2332.52 → 2333.22] spaghetti code
[2333.22 → 2333.94] you look at it
[2333.94 → 2334.38] why?
[2334.54 → 2335.30] Because it's generated
[2335.30 → 2337.08] via click ops
[2337.08 → 2337.30] right?
[2337.38 → 2338.26] You click through a UI
[2338.26 → 2338.94] This is why robots
[2338.94 → 2340.12] are not going to take over
[2340.12 → 2340.60] our jobs
[2340.60 → 2341.30] anytime soon
[2341.30 → 2342.18] because that's what
[2342.18 → 2342.86] they generate
[2342.86 → 2344.06] is 12,000 lines
[2344.06 → 2344.92] and we have to go
[2344.92 → 2345.76] wading through it
[2345.76 → 2346.28] as humans
[2346.28 → 2347.04] to figure out
[2347.04 → 2348.42] what spaghetti code
[2348.42 → 2349.44] that click ops
[2349.44 → 2350.00] generated
[2350.00 → 2351.38] and it's crazy
[2351.38 → 2352.02] how much
[2352.02 → 2353.40] junk was in there
[2353.40 → 2353.90] Yep
[2353.90 → 2354.76] that's right
[2354.76 → 2355.90] and it still is
[2355.90 → 2356.74] like that has not
[2356.74 → 2357.28] been fixed
[2357.28 → 2358.48] It's still there
[2358.48 → 2359.42] but we have a hack
[2359.42 → 2360.94] that just kind of
[2360.94 → 2361.62] makes it work
[2361.62 → 2361.92] you know
[2361.92 → 2363.12] like there's a VCL hack
[2363.12 → 2363.78] and it's just like
[2363.78 → 2364.82] how VCL snippets
[2364.82 → 2365.34] get integrated
[2365.34 → 2366.04] with other types
[2366.04 → 2366.62] of snippets
[2366.62 → 2367.30] and they all like
[2367.30 → 2368.06] get merged together
[2368.06 → 2368.94] into what looks like
[2368.94 → 2369.72] valid VCL
[2369.72 → 2370.44] Right
[2370.44 → 2371.26] but sometimes
[2371.26 → 2372.34] it takes paths
[2372.34 → 2373.46] that you don't expect it to
[2373.46 → 2374.18] so when we removed
[2374.18 → 2374.88] one origin
[2374.88 → 2375.84] and added another one
[2375.84 → 2376.82] it just wasn't even
[2376.82 → 2377.38] hitting it
[2377.38 → 2378.84] so no requests
[2378.84 → 2379.42] are being routed
[2379.42 → 2380.34] to that second origin
[2380.34 → 2381.22] even though everything
[2381.22 → 2382.32] was configured correctly
[2382.32 → 2383.50] and it should have worked
[2383.50 → 2384.92] but you know
[2384.92 → 2385.38] there were like
[2385.38 → 2386.22] some if statements
[2386.22 → 2387.64] nested ifs
[2387.64 → 2388.38] it always starts
[2388.38 → 2389.64] with nested ifs
[2389.64 → 2390.24] and so Gerhard
[2390.24 → 2390.74] you and I
[2390.74 → 2391.24] are sitting there
[2391.24 → 2391.94] trying to determine
[2391.94 → 2392.46] this is like
[2392.46 → 2393.44] when your knee-deep
[2393.44 → 2394.62] in a long debug session
[2394.62 → 2395.22] and you're thinking
[2395.22 → 2395.62] okay
[2395.62 → 2397.46] is it because of the order
[2397.46 → 2398.90] in which we entered
[2398.90 → 2400.24] these domains
[2400.24 → 2401.00] these origins
[2401.00 → 2402.26] no it's not that
[2402.26 → 2402.82] because of this
[2402.82 → 2403.60] is it because of
[2403.60 → 2405.02] is it alphabetical
[2405.02 → 2406.00] like you start wondering
[2406.00 → 2407.72] is it ordering by alphabetical
[2407.72 → 2408.14] and it's like
[2408.14 → 2408.98] oh it looks like it is
[2408.98 → 2409.36] oh no
[2409.36 → 2409.94] there's a case
[2409.94 → 2410.40] where actually
[2410.40 → 2411.24] it's not alphabetical
[2411.24 → 2412.56] we couldn't figure out
[2412.56 → 2414.06] exactly what it was
[2414.06 → 2414.90] but we did figure out
[2414.90 → 2415.98] a workaround
[2415.98 → 2417.72] what was the AI thinking
[2417.72 → 2419.12] when it generated
[2419.12 → 2420.20] this VCM
[2420.20 → 2422.78] getting in the AI mindset
[2422.78 → 2425.10] there's no AI by the way
[2425.10 → 2425.72] just like you know
[2425.72 → 2426.94] some automation
[2426.94 → 2428.48] and it was like
[2428.48 → 2429.42] so difficult
[2429.42 → 2430.18] yeah it's a back-end
[2430.18 → 2431.30] procedural code for sure
[2431.30 → 2433.34] so I even wrote
[2433.34 → 2434.50] an app
[2434.50 → 2435.52] a Go app
[2435.52 → 2435.98] and it's like
[2435.98 → 2436.54] I was using
[2436.54 → 2437.76] the fast starting app
[2437.76 → 2439.38] just to try and understand
[2439.38 → 2440.22] how the headers
[2440.22 → 2441.34] are being passed through
[2441.34 → 2442.02] so we have the
[2442.02 → 2442.22] you know
[2442.22 → 2443.58] remember Lazer.ch
[2443.58 → 2444.96] the Later Switzerland
[2444.96 → 2445.68] I mean we already
[2445.68 → 2446.30] talked about it
[2446.30 → 2447.08] they're one of the Kai sons
[2447.08 → 2447.70] it's true yeah
[2447.70 → 2448.78] so I took that service
[2448.78 → 2449.46] which is configured
[2449.46 → 2450.94] in Vastly
[2450.94 → 2452.12] to figure out
[2452.12 → 2452.70] and by the way
[2452.70 → 2453.58] all of this
[2453.58 → 2455.24] is in pull request 407
[2455.24 → 2456.40] so if you read it
[2456.40 → 2457.14] like you'll
[2457.14 → 2457.76] you'll notice
[2457.76 → 2458.62] why it took us
[2458.62 → 2459.54] two weeks longer
[2459.54 → 2461.22] to migrate to Fly.io
[2461.22 → 2462.64] and why we had to take
[2462.64 → 2464.30] the Kubernetes 1.2.2 detour
[2464.30 → 2465.70] in that migration
[2465.70 → 2467.12] because it was just crazy
[2467.12 → 2467.96] because we were running up
[2467.96 → 2468.90] against the deadline
[2468.90 → 2469.84] I mean this was like
[2469.84 → 2471.02] a scene from a movie
[2471.02 → 2471.34] you know
[2471.34 → 2472.08] like Speed
[2472.08 → 2473.36] or something
[2473.36 → 2473.52] you know
[2473.52 → 2474.38] you have 48 hours
[2474.38 → 2475.02] to cut over
[2475.02 → 2475.42] and we
[2475.42 → 2478.66] yeah exactly
[2478.66 → 2480.16] that scene from Swordfish
[2480.16 → 2480.90] that was Gerhard
[2480.90 → 2481.60] at 4am
[2481.60 → 2485.92] Adam you have seen that one?
[2486.92 → 2488.04] I know the movie
[2488.04 → 2488.46] Swordfish
[2488.46 → 2489.36] Gerhard's gonna break
[2489.36 → 2490.06] the show again
[2490.06 → 2494.46] I do own the movie
[2494.46 → 2495.24] I go back and watch
[2495.24 → 2495.64] the scene
[2495.64 → 2496.78] to laugh later
[2496.78 → 2497.42] my bad
[2497.42 → 2501.00] bad idea
[2501.00 → 2501.46] Gerhard's going to break
[2501.46 → 2504.58] oh my gosh
[2504.58 → 2506.50] here he goes again
[2506.50 → 2507.98] let me comment
[2507.98 → 2508.80] I don't know why
[2508.80 → 2509.72] they're laughing so hard
[2509.72 → 2510.44] apparently this is
[2510.44 → 2511.20] an amazing scene
[2511.20 → 2512.16] to recap though
[2512.16 → 2513.00] the plan was
[2513.00 → 2513.62] to just move
[2513.62 → 2514.40] straight to Fly
[2514.40 → 2515.44] and essentially
[2515.44 → 2516.32] at the 11th hour
[2516.32 → 2517.96] we had to throw in the towel
[2517.96 → 2519.64] and just submit
[2519.64 → 2521.32] to the migration
[2521.32 → 2522.80] to the newer
[2522.80 → 2523.38] Kubernetes
[2523.38 → 2524.30] the upgraded version
[2524.30 → 2525.50] we had to do the upgrade
[2525.50 → 2526.04] because it was just
[2526.04 → 2527.10] too complex
[2527.10 → 2528.26] yeah we just ran out of time
[2528.26 → 2529.40] which you know
[2529.40 → 2529.90] thankfully
[2529.90 → 2531.46] that was still a possibility
[2531.46 → 2532.08] that we weren't
[2532.08 → 2532.90] completely out of the water
[2532.90 → 2534.36] I'll always have a plan C
[2534.36 → 2535.08] seriously
[2535.08 → 2536.28] like you always have to
[2536.28 → 2536.90] have a plan C
[2536.90 → 2537.68] because when plan B
[2537.68 → 2538.22] doesn't work
[2538.22 → 2539.60] what are you going to do?
[2539.90 → 2540.02] right
[2540.02 → 2541.42] the deadline was going to happen
[2541.42 → 2542.86] the app was going to get upgraded
[2542.86 → 2544.06] what would have happened though
[2544.06 → 2544.36] so I mean
[2544.36 → 2545.68] so if we didn't upgrade
[2545.68 → 2546.78] to Kubernetes
[2546.78 → 2547.32] 1
[2547.32 → 2548.46] from 120 to 1
[2548.46 → 2548.94] or it was
[2548.94 → 2550.10] 1.21 right
[2550.10 → 2550.52] is that right?
[2550.86 → 2551.46] 1.21 yeah
[2551.46 → 2552.42] 1.20 to 1.21
[2552.42 → 2553.58] if we didn't do that
[2553.58 → 2554.48] our app would have broke
[2554.48 → 2554.96] yes
[2554.96 → 2556.62] we would have lost some data as well
[2556.62 → 2558.24] yeah they're going to upgrade for us
[2558.24 → 2559.20] and it wouldn't boot right?
[2559.44 → 2560.40] it wouldn't boot exactly
[2560.40 → 2561.46] I hate to go back to it
[2561.46 → 2561.98] but that's the thing
[2561.98 → 2562.90] that chat my butt was like
[2562.90 → 2564.52] we are going to break
[2564.52 → 2566.22] with this forced upgrade
[2566.22 → 2566.82] it's not like
[2566.82 → 2568.22] oh we'll have some bumps
[2568.22 → 2569.54] we'll lose data
[2569.54 → 2570.60] our app will break
[2570.60 → 2572.74] and we'll be in a dire situation
[2572.74 → 2573.74] and we made that clear
[2573.74 → 2574.52] yeah
[2574.52 → 2575.26] we asked for
[2575.26 → 2576.18] hey how about
[2576.18 → 2576.76] you know this is like
[2576.76 → 2577.76] when you're hitting up
[2577.76 → 2578.80] against your tax deadline
[2578.80 → 2579.20] you're like
[2579.20 → 2580.24] can I file an extension
[2580.24 → 2581.38] and the government says
[2581.38 → 2582.84] sure you can file an extension
[2582.84 → 2584.48] but Linde said no
[2584.48 → 2586.52] no there's no extension for this
[2586.52 → 2587.04] this is happening
[2587.04 → 2587.56] yeah
[2587.56 → 2588.22] and who knows
[2588.22 → 2589.04] what was going on inside
[2589.04 → 2589.84] to make that
[2589.84 → 2591.02] that strict
[2591.02 → 2591.58] who knows
[2591.58 → 2592.64] they did just go through an acquisition
[2592.64 → 2593.74] maybe there's something inside
[2593.74 → 2594.50] that we're not aware of
[2594.50 → 2595.98] but it just wasn't offered
[2595.98 → 2596.72] as a possibility
[2596.72 → 2597.26] yeah
[2597.26 → 2599.20] and so here we are
[2599.20 → 2600.10] 11th hour
[2600.10 → 2600.74] swordfish
[2600.74 → 2601.66] swordfish
[2601.66 → 2602.74] and then having to cut over
[2602.74 → 2603.80] and there you go
[2603.80 → 2604.60] yeah
[2604.60 → 2605.38] so
[2605.38 → 2606.86] having that 1.22
[2606.86 → 2607.74] you know
[2607.74 → 2608.86] was really, really helpful
[2608.86 → 2609.98] it was crazy how
[2609.98 → 2612.20] Linde had a solution for us
[2612.20 → 2612.68] right
[2612.68 → 2613.40] because let's be honest
[2613.40 → 2614.30] that's exactly what happened
[2614.30 → 2615.54] with an LK1.22
[2615.54 → 2616.60] there
[2616.60 → 2618.10] but we didn't want to go to that
[2618.10 → 2618.56] because we said
[2618.56 → 2620.20] okay we are going to fly
[2620.20 → 2621.12] this is happening
[2621.12 → 2622.96] and everything was going great
[2622.96 → 2624.88] like unexpectedly good
[2624.88 → 2625.76] until
[2625.76 → 2626.84] the fast
[2626.84 → 2627.56] configuration
[2627.56 → 2628.98] and it was obviously
[2628.98 → 2630.00] like a bunch of things
[2630.00 → 2630.26] you know
[2630.26 → 2630.98] we were tired
[2630.98 → 2632.62] you were sick Jared
[2632.62 → 2633.98] it was like a long day
[2633.98 → 2635.48] it was a stressful period
[2635.48 → 2635.88] you know
[2635.88 → 2636.74] mistakes are made
[2636.74 → 2637.34] and it's normal
[2637.34 → 2638.52] those things will happen
[2638.52 → 2640.08] so how do you factor those in
[2640.08 → 2641.30] in whatever you're doing
[2641.30 → 2641.90] so
[2641.90 → 2643.62] can I share some behind the scenes
[2643.62 → 2644.44] in the Slack channel
[2644.44 → 2645.08] of what happened
[2645.08 → 2646.14] when you were talking with
[2646.14 → 2647.00] the team
[2647.00 → 2648.42] that fly about the VCL
[2648.42 → 2648.82] they were like
[2648.82 → 2650.06] you shared the
[2650.06 → 2651.16] fast integration
[2651.16 → 2653.12] the issue that captured it
[2653.12 → 2654.56] which is all out there
[2654.56 → 2656.44] and Kurt's response was
[2656.44 → 2658.50] that is a very large VCL
[2658.50 → 2659.98] wow
[2659.98 → 2661.90] and you all talk back and forth
[2661.90 → 2662.84] about bandwidth and whatnot
[2662.84 → 2663.62] and just
[2663.62 → 2666.06] just how challenging it is
[2666.06 → 2666.86] to deal with VCL
[2666.86 → 2668.08] and in particular
[2668.08 → 2668.94] how big that one was
[2668.94 → 2670.02] which you all commented on already
[2670.02 → 2670.50] which is
[2670.50 → 2671.34] click ops
[2671.34 → 2672.38] lots of lines
[2672.38 → 2673.66] not very human-readable
[2673.66 → 2675.22] we're not being replaced
[2675.22 → 2675.90] anytime soon
[2675.90 → 2676.56] now for
[2676.56 → 2677.90] to Vastly's credit
[2677.90 → 2679.46] and to whomever engineer
[2679.46 → 2680.90] coded that back end
[2680.90 → 2682.42] when you turn shielding off
[2682.42 → 2683.54] it gets a lot simpler
[2683.54 → 2684.36] so
[2684.36 → 2685.74] the VCL that's generated
[2685.74 → 2687.26] without shielding
[2687.26 → 2689.34] is dramatically shorter
[2689.34 → 2690.32] so
[2690.32 → 2691.04] it's not like
[2691.04 → 2691.84] every VCL
[2691.84 → 2692.78] that Vastly generates
[2692.78 → 2693.84] is going to be inscrutable
[2693.84 → 2694.46] right
[2694.46 → 2695.36] it's just that ours was
[2695.36 → 2696.98] or anybody who has shielding turned on is
[2696.98 → 2698.16] and probably most people do
[2698.16 → 2698.48] so
[2698.48 → 2699.24] right
[2699.24 → 2700.26] your mileage may vary
[2700.26 → 2700.54] but
[2700.54 → 2701.08] apparently
[2701.08 → 2702.04] setting up a shield
[2702.04 → 2703.86] for pops all around the world
[2703.86 → 2705.46] is complicated
[2705.46 → 2706.94] got a lot of instructions
[2706.94 → 2707.74] for a lot of
[2707.74 → 2708.48] circumstances
[2708.48 → 2710.28] but even if you remove all of that
[2710.28 → 2712.04] so let's say you remove all the shielding
[2712.04 → 2713.14] that wasn't the bug though
[2713.14 → 2714.04] yeah that was just
[2714.04 → 2714.94] obfuscating the bug
[2714.94 → 2715.86] exactly
[2715.86 → 2717.14] and you look at
[2717.14 → 2718.56] how everything gets structured
[2718.56 → 2720.26] we basically have
[2720.26 → 2721.62] some extra logic
[2721.62 → 2722.94] in a VCL snippet
[2722.94 → 2724.44] that configures the origin
[2724.44 → 2725.58] in a specific way
[2725.58 → 2726.10] okay
[2726.10 → 2727.18] this is my long
[2727.18 → 2727.48] like
[2727.48 → 2729.14] let me do it very shortly
[2729.14 → 2730.36] the UI
[2730.36 → 2732.62] generates some VCL
[2732.62 → 2734.40] which is very difficult
[2734.40 → 2735.16] to work with
[2735.16 → 2736.18] understand
[2736.18 → 2737.20] debug
[2737.20 → 2738.58] and while the UI
[2738.58 → 2739.52] makes it easy
[2739.52 → 2740.96] it gets you into situations
[2740.96 → 2742.40] when you can introduce bugs
[2742.40 → 2743.88] just because you use the UI
[2743.88 → 2745.58] like this should not be possible
[2745.58 → 2747.34] you should not get yourself
[2747.34 → 2747.98] in a situation
[2747.98 → 2749.22] when a backend is configured
[2749.22 → 2749.96] and everything is good
[2749.96 → 2751.78] but the backend isn't used
[2751.78 → 2753.78] because there's a snippet
[2753.78 → 2755.94] which exits the subroutine
[2755.94 → 2757.84] before the backend is set
[2757.84 → 2759.38] I mean if you think about it
[2759.38 → 2760.30] this should not be possible
[2760.30 → 2761.02] and it is
[2761.02 → 2762.68] I think the more important thing is
[2762.68 → 2765.38] I can see the same story
[2765.38 → 2766.82] in a way repeating itself
[2766.82 → 2768.22] the Linde story
[2768.22 → 2769.64] where there's no empathy
[2769.64 → 2771.06] there's no collaboration
[2771.06 → 2772.18] on the Vastly side
[2772.18 → 2773.72] there's all these issues
[2773.72 → 2774.46] right
[2774.46 → 2775.84] that we keep hitting across
[2775.84 → 2777.02] and yes support is good
[2777.02 → 2778.04] we get our answers
[2778.04 → 2780.42] but we cannot get past that stage
[2780.42 → 2781.48] of just getting support
[2781.48 → 2782.18] and we say
[2782.18 → 2783.18] look this doesn't make sense
[2783.18 → 2783.50] I mean
[2783.50 → 2784.90] we still have an issue
[2784.90 → 2785.68] with certificates
[2785.68 → 2788.30] that's been two years old
[2788.30 → 2789.98] and it still has not been solved
[2789.98 → 2791.32] because we're getting support
[2791.32 → 2792.32] we're not getting a partner
[2792.32 → 2793.02] yeah
[2793.02 → 2794.70] I think part of these shows
[2794.70 → 2795.84] and part of this feedback
[2795.84 → 2796.66] I think is
[2796.66 → 2797.20] you know
[2797.20 → 2798.58] there's going to be a Vastly Engineer
[2798.58 → 2799.78] Listener Show one day
[2799.78 → 2800.42] there's going to be somebody
[2800.42 → 2801.88] knowing that we desire to improve
[2801.88 → 2803.00] and that we're patient
[2803.00 → 2803.92] we're not upset
[2803.92 → 2805.22] like obviously we're perturbed
[2805.22 → 2807.16] because it's not the ideal situation
[2807.16 → 2808.40] but you know
[2808.40 → 2809.08] we desire
[2809.08 → 2810.72] we desire to make these partnerships
[2810.72 → 2812.28] not just to leverage the platforms
[2812.28 → 2813.68] but to improve the platforms
[2813.68 → 2814.68] which I think is key
[2814.68 → 2817.04] because customers won't do that for them
[2817.04 → 2818.26] they're going to angrily
[2818.26 → 2820.48] shout out support for solutions
[2820.48 → 2821.64] they're going to move about their day
[2821.64 → 2823.12] and improve their product
[2823.12 → 2824.38] and ship better stuff
[2824.38 → 2825.58] and make money and profit
[2825.58 → 2827.22] and give back to shareholders
[2827.22 → 2828.44] and you know
[2828.44 → 2828.98] whatever
[2828.98 → 2829.54] you know
[2829.54 → 2830.60] that's how business works
[2830.60 → 2832.80] our desire is to come into this mix
[2832.80 → 2833.02] and say
[2833.02 → 2834.62] okay here are some amazing picks
[2834.62 → 2835.86] here's Vastly
[2835.86 → 2836.50] here's Fly
[2836.50 → 2837.22] here's Honeycomb
[2837.22 → 2838.26] here's you know
[2838.26 → 2838.96] XYZ
[2838.96 → 2840.24] and say not just
[2840.24 → 2841.28] can we leverage this platform
[2841.28 → 2842.86] but can we also help you improve it
[2842.86 → 2844.42] we want to give you that feedback loop
[2844.42 → 2844.94] for us
[2844.94 → 2845.86] and for you
[2845.86 → 2846.80] because
[2846.80 → 2848.06] somebody out there
[2848.06 → 2848.70] is not telling you
[2848.70 → 2849.30] what we're going to tell you
[2849.30 → 2850.26] because we care
[2850.26 → 2850.74] deeply
[2850.74 → 2851.86] so give us that
[2851.86 → 2853.10] give us that feedback loop
[2853.10 → 2854.20] and we will help you improve
[2854.20 → 2855.56] I remember that was
[2855.56 → 2856.44] one of the
[2856.44 → 2857.50] key reasons
[2857.50 → 2858.74] why we started Shi pit
[2858.74 → 2859.86] and we were thinking like
[2859.86 → 2861.20] do we have something here
[2861.20 → 2862.74] and that was one of the
[2862.74 → 2863.46] pillars
[2863.46 → 2865.10] on which Shi pit was built
[2865.10 → 2867.28] we think we can do amazing things
[2867.28 → 2868.36] for companies out there
[2868.36 → 2869.54] by simply using them
[2869.54 → 2871.26] and by partnering with them
[2871.26 → 2872.52] and it goes beyond
[2872.52 → 2873.90] being a partner of the show
[2873.90 → 2875.34] like sponsoring a show
[2875.34 → 2876.58] it really does
[2876.58 → 2877.70] we'll use your stuff
[2877.70 → 2879.64] we'll tell you where the blind spots are
[2879.64 → 2881.78] we will tell you the things
[2881.78 → 2882.42] that you're missing
[2882.42 → 2884.22] and it's just one perspective
[2884.22 → 2884.98] you know
[2884.98 → 2886.98] we're not the final word
[2886.98 → 2888.70] in how to design systems
[2888.70 → 2889.84] and how to improve systems
[2889.84 → 2891.64] but it's yet another data point
[2891.64 → 2893.16] and we're a patient one
[2893.16 → 2894.12] we have all
[2894.12 → 2895.54] like the code is there
[2895.54 → 2896.82] we try these things
[2896.82 → 2898.26] we have all the redundancies in place
[2898.26 → 2899.44] we have a resilient system
[2899.44 → 2900.34] it won't break
[2900.34 → 2900.88] so
[2900.88 → 2901.82] and we ourselves
[2901.82 → 2902.78] are trying to improve
[2902.78 → 2903.46] along the way
[2903.46 → 2904.64] and our code is open source
[2904.64 → 2905.16] when you say
[2905.16 → 2906.16] okay how does it integrate
[2906.16 → 2908.82] with a well-tuned application
[2908.82 → 2909.78] that's in production
[2909.78 → 2911.86] that's also open source
[2911.86 → 2913.14] that you can read the source code
[2913.14 → 2914.12] permissively too
[2914.12 → 2915.54] you can copy something with code
[2915.54 → 2916.62] what's our license Jerry
[2916.62 → 2917.10] remind me
[2917.10 → 2918.34] it's like hey take it
[2918.34 → 2919.02] if you want
[2919.02 → 2919.34] MIT
[2919.34 → 2920.36] yeah MIT
[2920.36 → 2921.38] I even forget
[2921.38 → 2922.60] how little I pay attention
[2922.60 → 2923.08] to our license
[2923.08 → 2923.96] I know it's permissive
[2923.96 → 2924.44] that's all I know
[2924.44 → 2925.62] it's a great thing
[2925.62 → 2927.12] I mean it makes me excited
[2927.12 → 2927.66] about this show
[2927.66 → 2928.34] and I even like
[2928.34 → 2929.78] even back to being here
[2929.78 → 2931.42] with the fifth Kaiden
[2931.42 → 2932.44] episode 50
[2932.44 → 2934.24] I love when you can look back
[2934.24 → 2935.24] at the path you set
[2935.24 → 2935.62] and say okay
[2935.62 → 2936.86] this was actually a good path
[2936.86 → 2937.84] like you have some assumptions
[2937.84 → 2938.98] okay this is a good path
[2938.98 → 2939.56] let's go it
[2939.56 → 2941.30] and improve as we get there
[2941.30 → 2941.72] but I think
[2941.72 → 2943.78] having you speak to the community
[2943.78 → 2945.08] and involve the community
[2945.08 → 2947.14] from those who are the innovators
[2947.14 → 2947.94] building the platforms
[2947.94 → 2949.36] to those who are the end users
[2949.36 → 2951.14] hitting the bumps and challenges
[2951.14 → 2951.88] along the way
[2951.88 → 2952.98] and the practitioners
[2952.98 → 2954.16] putting it to work
[2954.16 → 2956.02] like that's a great mix for a show
[2956.02 → 2956.62] and then us
[2956.62 → 2957.50] and how we leverage
[2957.50 → 2959.00] some if not all
[2959.00 → 2960.16] of those same topics
[2960.16 → 2961.86] within our own platform
[2961.86 → 2963.60] and have that sort of
[2963.60 → 2964.08] you know
[2964.08 → 2965.22] retrospective
[2965.22 → 2966.18] basically of like
[2966.18 → 2967.00] how did this go
[2967.00 → 2967.98] does it work well
[2967.98 → 2968.58] you know
[2968.58 → 2969.64] can we improve it
[2969.64 → 2970.50] that kind of thing
[2970.50 → 2971.82] I think is such a beautiful recipe
[2971.82 → 2973.24] very well put
[2973.24 → 2985.70] this episode
[2985.70 → 2986.68] is brought to you
[2986.68 → 2987.34] by Chromosphere
[2987.34 → 2988.86] when it comes to observability
[2988.86 → 2990.16] teams need a reliable
[2990.16 → 2990.78] scalable
[2990.78 → 2992.68] and efficient solution
[2992.68 → 2993.88] so they can know about issues
[2993.88 → 2995.30] well before their customers do
[2995.30 → 2996.28] they need a solution
[2996.28 → 2997.88] that helps them move faster
[2997.88 → 2998.88] than the competition
[2998.88 → 3000.16] and companies born
[3000.16 → 3001.14] in the cloud native era
[3001.14 → 3002.48] often start with Prometheus
[3002.48 → 3003.02] for monitoring
[3003.02 → 3003.94] which is obviously
[3003.94 → 3004.98] an amazing piece of software
[3004.98 → 3006.26] but they quickly push it
[3006.26 → 3006.86] to its limits
[3006.86 → 3008.14] and often outgrow it
[3008.14 → 3009.22] they run into issues
[3009.22 → 3010.08] with siloed data
[3010.08 → 3011.92] missing long term storage
[3011.92 → 3013.68] and wasted engineering time
[3013.68 → 3015.16] firefighting the monitoring system
[3015.16 → 3016.08] versus delivering
[3016.08 → 3016.80] their application
[3016.80 → 3017.68] with confidence
[3017.68 → 3018.84] they describe the system
[3018.84 → 3020.44] as a house of cards
[3020.44 → 3021.44] where a single developer
[3021.44 → 3023.20] seemingly benign change
[3023.20 → 3024.02] can overload
[3024.02 → 3025.32] the whole monitoring system
[3025.32 → 3026.26] or they say
[3026.26 → 3027.28] they're flying blind
[3027.28 → 3028.22] because they pride themselves
[3028.22 → 3029.58] on making data driven decisions
[3029.58 → 3031.10] but losing visibility
[3031.10 → 3032.10] means they lose
[3032.10 → 3033.32] this competitive edge
[3033.32 → 3034.26] Ryan Skol
[3034.26 → 3035.06] VP of engineering
[3035.06 → 3035.70] at DoorDash
[3035.70 → 3036.64] has this to say
[3036.64 → 3037.22] about Chromosphere
[3037.22 → 3037.82] quote
[3037.82 → 3039.40] the visibility and control
[3039.40 → 3040.56] that Chromosphere's platform
[3040.56 → 3041.26] gives us to manage
[3041.26 → 3042.16] our observability data
[3042.16 → 3043.00] and costs
[3043.00 → 3044.02] are a game changer
[3044.02 → 3044.86] especially
[3044.86 → 3046.56] with our unprecedented growth
[3046.56 → 3047.20] end quote
[3047.20 → 3047.88] Chromosphere
[3047.88 → 3049.52] is the observability platform
[3049.52 → 3050.58] for cloud native teams
[3050.58 → 3051.90] operating at scale
[3051.90 → 3052.78] learn more
[3052.78 → 3053.54] and get a demo
[3053.54 → 3054.82] at Chronosphere.io
[3054.82 → 3055.88] again
[3055.88 → 3057.62] Chronosphere.io
[3057.62 → 3059.04] and by our friends
[3059.04 → 3060.10] at Net Foundry
[3060.10 → 3061.88] the creator of Opened
[3061.88 → 3062.86] Opened
[3062.86 → 3064.72] is the only open source way
[3064.72 → 3065.34] to embed
[3065.34 → 3066.56] zero trust networking
[3066.56 → 3067.52] into your app
[3067.52 → 3068.48] this gives you
[3068.48 → 3069.80] unprecedented control
[3069.80 → 3070.68] and security
[3070.68 → 3071.86] give your app
[3071.86 → 3072.42] superpowers
[3072.42 → 3073.94] using an Opened SDK
[3073.94 → 3075.32] and a few lines of code
[3075.32 → 3076.50] or use their tunnellers
[3076.50 → 3077.14] to spin up
[3077.14 → 3078.10] zero trust networking
[3078.10 → 3078.62] in minutes
[3078.62 → 3079.94] across any cloud
[3079.94 → 3080.66] or device
[3080.66 → 3082.16] never face the horrors
[3082.16 → 3083.28] of VPNs
[3083.28 → 3083.66] DNS
[3083.66 → 3084.86] inbound ports
[3084.86 → 3086.50] or complex firewall rules
[3086.50 → 3087.38] no networking
[3087.38 → 3088.12] engineering skills
[3088.12 → 3088.82] are needed
[3088.82 → 3090.04] Opened is trusted
[3090.04 → 3090.62] by developers
[3090.62 → 3091.40] at Microsoft
[3091.40 → 3092.10] Oracle
[3092.10 → 3092.58] Rambo
[3092.58 → 3093.00] and more
[3093.00 → 3094.14] and if you want
[3094.14 → 3094.90] to host your own
[3094.90 → 3095.58] Opened
[3095.58 → 3096.80] use the Net Foundry
[3096.80 → 3097.26] SaaS
[3097.26 → 3097.88] which includes
[3097.88 → 3098.80] free forever tiers
[3098.80 → 3100.24] for up to 10 endpoints
[3100.24 → 3101.20] so you can test things
[3101.20 → 3102.08] out for yourself
[3102.08 → 3102.54] head to
[3102.54 → 3103.52] netfoundry.io
[3103.52 → 3104.42] slash changelog
[3104.42 → 3104.94] to learn more
[3104.94 → 3105.54] and get started
[3105.54 → 3106.40] again
[3106.40 → 3108.00] netfoundry.io
[3108.00 → 3109.10] slash changelog
[3109.10 → 3121.74] so I really like
[3121.74 → 3122.18] the journey
[3122.18 → 3123.38] and I'm wondering
[3123.38 → 3124.98] where are we going next
[3124.98 → 3126.52] and you can already tell
[3126.52 → 3128.04] as a Kaiser listener
[3128.04 → 3128.76] that this is
[3128.76 → 3129.56] towards the end
[3129.56 → 3130.22] of this episode
[3130.22 → 3131.14] so what is going
[3131.14 → 3131.94] to happen next
[3131.94 → 3132.98] I'm very curious
[3132.98 → 3133.40] about that
[3133.40 → 3133.94] there's a couple
[3133.94 → 3134.24] of things
[3134.24 → 3134.56] which I have
[3134.56 → 3135.22] on my list
[3135.22 → 3136.24] but maybe we can
[3136.24 → 3136.90] start with Adam
[3136.90 → 3137.30] first
[3137.30 → 3137.90] or no
[3137.90 → 3138.36] you know what
[3138.36 → 3139.10] let's do in the
[3139.10 → 3140.42] reverse alphabetical order
[3140.42 → 3141.04] Jared first
[3141.04 → 3141.56] okay
[3141.56 → 3142.90] is this where I put
[3142.90 → 3143.92] in my fly.io
[3143.92 → 3144.84] feature requests
[3144.84 → 3145.86] you can do
[3145.86 → 3147.32] Mark will be listening
[3147.32 → 3147.78] because that's where
[3147.78 → 3148.48] I want to go next
[3148.48 → 3149.06] Kurt will be listening
[3149.06 → 3149.60] for sure
[3149.60 → 3150.54] and others as well
[3150.54 → 3152.06] go for it
[3152.06 → 3153.50] I like this platform
[3153.50 → 3154.26] it has a kernel
[3154.26 → 3155.10] of something amazing
[3155.10 → 3156.26] there's a lot
[3156.26 → 3158.40] of missing things
[3158.40 → 3160.10] that I would like
[3160.10 → 3160.54] to have
[3160.54 → 3161.48] as an old
[3161.48 → 3162.94] Heroku fanboy
[3162.94 → 3163.68] from way back
[3163.68 → 3164.70] and
[3164.70 → 3166.10] the main one
[3166.10 → 3166.62] for now
[3166.62 → 3167.04] that I think
[3167.04 → 3167.44] is like
[3167.44 → 3168.50] top of my list
[3168.50 → 3169.00] is like
[3169.00 → 3169.22] hey
[3169.22 → 3169.78] how can we
[3169.78 → 3170.56] work with
[3170.56 → 3171.38] Postgres better
[3171.38 → 3172.56] because right now
[3172.56 → 3172.98] it's like
[3172.98 → 3174.32] well you work
[3174.32 → 3174.72] with it
[3174.72 → 3175.60] I like the
[3175.60 → 3176.90] there's a simplicity
[3176.90 → 3177.24] of like
[3177.24 → 3177.78] well you basically
[3177.78 → 3178.42] SSH in
[3178.42 → 3178.88] and just do
[3178.88 → 3179.64] what you would do
[3179.64 → 3180.38] right
[3180.38 → 3181.40] like PSQL
[3181.40 → 3182.36] PG dump
[3182.36 → 3182.86] and so
[3182.86 → 3184.20] familiar tools
[3184.20 → 3184.92] it's like
[3184.92 → 3185.66] your own little
[3185.66 → 3186.94] shell there
[3186.94 → 3187.94] do your own thing
[3187.94 → 3188.94] but
[3188.94 → 3190.10] I would love
[3190.10 → 3190.68] to have
[3190.68 → 3191.48] like
[3191.48 → 3192.30] automated
[3192.30 → 3193.56] backups
[3193.56 → 3194.42] and things
[3194.42 → 3194.76] that you can
[3194.76 → 3194.96] just
[3194.96 → 3195.56] just
[3195.56 → 3196.66] click a
[3196.66 → 3197.06] button
[3197.06 → 3197.50] give me
[3197.50 → 3197.66] some
[3197.66 → 3198.06] click ops
[3198.06 → 3198.22] right
[3198.22 → 3198.38] like
[3198.38 → 3198.64] let me
[3198.64 → 3198.82] check
[3198.82 → 3198.96] the
[3198.96 → 3199.22] button
[3199.22 → 3199.40] that
[3199.40 → 3199.70] says
[3199.70 → 3200.54] manage
[3200.54 → 3200.84] my
[3200.84 → 3201.26] Postgres
[3201.26 → 3201.72] backups
[3201.72 → 3202.28] and
[3202.28 → 3203.20] allow me
[3203.20 → 3203.46] to do
[3203.46 → 3203.88] things
[3203.88 → 3204.42] a lot
[3204.42 → 3204.60] of the
[3204.60 → 3204.80] stuff
[3204.80 → 3205.06] that
[3205.06 → 3205.44] Heroku
[3205.44 → 3205.94] built out
[3205.94 → 3206.60] over time
[3206.60 → 3207.08] fly is
[3207.08 → 3207.56] missing
[3207.56 → 3208.42] the other
[3208.42 → 3208.62] thing
[3208.62 → 3208.86] which I
[3208.86 → 3209.22] think is
[3209.22 → 3209.92] smart
[3209.92 → 3210.26] but I
[3210.26 → 3210.50] hate
[3210.50 → 3210.76] it
[3210.76 → 3211.66] is
[3211.66 → 3212.28] the way
[3212.28 → 3212.52] they do
[3212.52 → 3213.04] secrets
[3213.04 → 3214.18] which is
[3214.18 → 3214.50] like
[3214.50 → 3215.42] 100%
[3215.42 → 3215.82] encrypted
[3215.82 → 3216.14] there
[3216.14 → 3216.76] like
[3216.76 → 3217.00] you can
[3217.00 → 3217.20] set
[3217.20 → 3217.36] them
[3217.36 → 3217.60] but you
[3217.60 → 3217.84] can't
[3217.84 → 3218.02] read
[3218.02 → 3218.24] them
[3218.24 → 3218.78] I
[3218.78 → 3219.12] understand
[3219.12 → 3219.56] why
[3219.56 → 3220.32] but
[3220.32 → 3220.72] come on
[3220.72 → 3220.90] man
[3220.90 → 3221.24] just show
[3221.24 → 3221.32] me
[3221.32 → 3221.46] my
[3221.46 → 3221.92] secrets
[3221.92 → 3222.34] I
[3222.34 → 3222.62] need
[3222.62 → 3222.72] to
[3222.72 → 3222.86] know
[3222.86 → 3223.00] what
[3223.00 → 3223.14] they
[3223.14 → 3223.40] are
[3223.40 → 3224.16] it's
[3224.16 → 3224.26] a
[3224.26 → 3224.42] one
[3224.42 → 3224.70] way
[3224.70 → 3225.24] well
[3225.24 → 3225.56] it's
[3225.56 → 3225.70] not
[3225.70 → 3225.94] really
[3225.94 → 3226.20] one
[3226.20 → 3226.48] way
[3226.48 → 3226.76] I
[3226.76 → 3226.88] mean
[3226.88 → 3227.10] you're
[3227.10 → 3227.26] right
[3227.26 → 3227.48] why
[3227.48 → 3227.70] can't
[3227.70 → 3227.82] the
[3227.82 → 3228.00] amp
[3228.00 → 3228.22] get
[3228.22 → 3228.46] it
[3228.46 → 3228.88] I
[3228.88 → 3229.08] have
[3229.08 → 3229.18] to
[3229.18 → 3229.38] log
[3229.38 → 3229.54] into
[3229.54 → 3229.72] the
[3229.72 → 3230.02] app
[3230.02 → 3230.22] and
[3230.22 → 3230.52] then
[3230.52 → 3231.40] echo
[3231.40 → 3231.60] out
[3231.60 → 3231.72] the
[3231.72 → 3232.04] environment
[3232.04 → 3232.52] variable
[3232.52 → 3233.22] well
[3233.22 → 3233.62] come on
[3233.62 → 3234.20] if I can
[3234.20 → 3234.34] do
[3234.34 → 3234.58] that
[3234.58 → 3234.76] just
[3234.76 → 3235.00] go ahead
[3235.00 → 3235.26] and echo
[3235.26 → 3235.38] it
[3235.38 → 3235.50] out
[3250.90 → 3251.36] user
[3251.36 → 3252.42] it's
[3252.42 → 3253.00] just
[3253.00 → 3253.34] adding
[3253.34 → 3253.56] like
[3253.56 → 3253.74] three
[3253.74 → 3254.10] steps
[3254.10 → 3254.28] to
[3254.28 → 3254.46] the
[3254.46 → 3254.74] exact
[3254.74 → 3255.06] same
[3255.06 → 3255.36] end
[3255.36 → 3255.68] goal
[3255.68 → 3255.92] of
[3255.92 → 3256.10] like
[3256.10 → 3256.32] me
[3256.32 → 3256.64] also
[3256.64 → 3257.08] echoing
[3257.08 → 3257.36] out
[3257.36 → 3257.98] plain
[3257.98 → 3258.22] text
[3258.22 → 3258.34] to
[3258.34 → 3258.48] my
[3258.48 → 3258.74] terminal
[3258.74 → 3259.16] session
[3259.16 → 3259.96] and
[3259.96 → 3260.14] so
[3260.14 → 3260.40] maybe
[3260.40 → 3260.62] those
[3260.62 → 3260.76] don't
[3260.76 → 3261.00] go over
[3261.00 → 3261.14] the
[3261.14 → 3261.50] wire
[3261.50 → 3261.92] they
[3261.92 → 3262.12] do
[3262.12 → 3262.26] they
[3262.26 → 3262.50] go over
[3262.50 → 3262.92] SSH
[3262.92 → 3263.22] encrypted
[3263.22 → 3263.46] wire
[3263.46 → 3263.86] anyway
[3263.86 → 3264.18] I'm
[3264.18 → 3264.28] sure
[3264.28 → 3264.46] they've
[3264.46 → 3264.60] thought
[3264.60 → 3264.76] through
[3264.76 → 3264.88] all
[3264.88 → 3265.00] the
[3265.00 → 3265.28] security
[3265.28 → 3265.68] concerns
[3265.68 → 3265.92] there
[3265.92 → 3266.36] but
[3266.36 → 3266.40] I
[3266.40 → 3266.58] think
[3266.58 → 3266.78] as
[3266.78 → 3266.96] a
[3266.96 → 3267.24] user
[3267.24 → 3267.78] experience
[3267.78 → 3268.26] it
[3268.26 → 3268.42] just
[3268.42 → 3268.60] kind
[3268.60 → 3268.68] of
[3268.68 → 3268.96] sucks
[3268.96 → 3269.54] those
[3269.54 → 3269.64] are
[3269.64 → 3269.72] just
[3269.72 → 3269.78] a
[3269.78 → 3269.88] couple
[3269.88 → 3270.18] things
[3270.18 → 3270.38] I
[3270.38 → 3270.60] think
[3270.60 → 3271.44] fly
[3271.44 → 3271.92] improvements
[3271.92 → 3272.16] I'm
[3272.16 → 3272.30] looking
[3272.30 → 3272.56] forward
[3272.56 → 3272.78] to
[3272.78 → 3272.96] them
[3272.96 → 3273.64] and
[3273.64 → 3273.82] I
[3273.82 → 3273.98] think
[3273.98 → 3274.42] Postgres
[3274.42 → 3275.02] backups
[3275.02 → 3275.32] and
[3275.32 → 3275.76] automation
[3275.76 → 3276.10] and
[3276.10 → 3276.32] those
[3276.32 → 3276.48] kind
[3276.48 → 3276.56] of
[3276.56 → 3276.90] things
[3276.90 → 3277.72] yeah
[3277.72 → 3278.14] do
[3278.14 → 3278.26] we
[3278.26 → 3278.50] have
[3278.50 → 3278.62] a
[3278.62 → 3278.92] solution
[3278.92 → 3279.22] like
[3279.22 → 3279.36] in
[3279.36 → 3279.46] the
[3279.46 → 3279.68] meantime
[3279.68 → 3279.92] for
[3279.92 → 3280.12] that
[3280.12 → 3280.36] because
[3280.36 → 3280.52] I
[3280.52 → 3280.68] just
[3280.68 → 3280.84] like
[3280.84 → 3281.06] PG
[3281.06 → 3281.46] dumped
[3281.46 → 3281.70] a
[3281.70 → 3282.00] backup
[3282.00 → 3282.16] and
[3282.16 → 3282.28] I'm
[3282.28 → 3282.50] thinking
[3282.50 → 3283.12] I
[3283.12 → 3283.32] hope
[3283.32 → 3283.50] this
[3283.50 → 3283.62] is
[3283.62 → 3283.98] happening
[3283.98 → 3284.60] every
[3284.60 → 3284.76] once
[3284.76 → 3284.86] in
[3284.86 → 3284.92] a
[3284.92 → 3285.18] while
[3285.18 → 3285.54] so
[3285.54 → 3285.86] apparently
[3285.86 → 3286.06] it's
[3286.06 → 3286.30] happening
[3286.30 → 3286.54] every
[3286.54 → 3286.84] day
[3286.84 → 3287.20] but
[3287.20 → 3287.64] you
[3287.64 → 3287.90] can't
[3287.90 → 3288.00] see
[3288.00 → 3288.30] that
[3288.30 → 3288.80] or
[3288.80 → 3288.94] at
[3288.94 → 3289.06] least
[3289.06 → 3289.28] I
[3289.28 → 3289.42] don't
[3289.42 → 3289.54] know
[3289.54 → 3289.74] how
[3289.74 → 3289.90] to
[3289.90 → 3290.06] look
[3300.60 → 3301.10] back
[3301.10 → 3301.36] things
[3301.36 → 3301.58] up
[3301.58 → 3302.34] and
[3302.34 → 3302.48] I
[3302.48 → 3302.70] think
[3302.70 → 3303.12] even
[3303.12 → 3303.76] I
[3303.76 → 3303.92] think
[3303.92 → 3304.04] it
[3304.04 → 3304.18] was
[3304.18 → 3304.32] the
[3304.32 → 3304.50] pod
[3304.50 → 3304.70] yes
[3304.70 → 3304.82] it
[3304.82 → 3304.94] was
[3304.94 → 3305.06] the
[3305.06 → 3305.24] pod
[3305.24 → 3305.36] so
[3305.36 → 3305.46] we
[3305.46 → 3305.56] had
[3305.56 → 3305.80] the
[3305.80 → 3305.96] unit
[3305.96 → 3306.52] containers
[3306.52 → 3308.36] before
[3308.36 → 3308.64] the
[3308.64 → 3308.82] app
[3308.82 → 3308.92] would
[3308.92 → 3309.50] do
[3309.50 → 3309.62] a
[3309.62 → 3309.88] backup
[3309.88 → 3310.40] before
[3310.40 → 3310.60] it
[3310.60 → 3310.76] runs
[3310.76 → 3310.88] the
[3310.88 → 3311.32] migration
[3311.32 → 3311.84] and
[3311.84 → 3311.94] that
[3311.94 → 3312.02] was
[3312.02 → 3312.20] really
[3312.20 → 3312.64] important
[3312.64 → 3313.10] so
[3313.10 → 3313.22] that
[3313.22 → 3313.34] in
[3313.34 → 3313.48] case
[3313.48 → 3313.60] the
[3313.60 → 3314.00] migration
[3314.00 → 3315.24] messes
[3315.24 → 3315.54] something
[3315.54 → 3315.84] up
[3315.84 → 3316.00] you
[3316.00 → 3316.12] have
[3316.12 → 3316.22] the
[3316.22 → 3316.56] backup
[3316.56 → 3317.58] fly
[3317.58 → 3317.82] does
[3317.82 → 3318.08] things
[3318.08 → 3318.50] differently
[3318.50 → 3318.68] when
[3318.68 → 3318.80] it
[3318.80 → 3319.10] comes
[3319.10 → 3319.82] to
[3319.82 → 3320.70] applications
[3320.70 → 3321.14] starting
[3321.14 → 3321.46] up
[3321.46 → 3321.86] so
[3321.86 → 3322.02] that
[3322.02 → 3322.42] lifecycle
[3322.42 → 3323.26] and
[3323.26 → 3323.44] this
[3323.44 → 3323.70] was
[3323.70 → 3324.02] one
[3324.02 → 3324.12] of
[3324.12 → 3324.24] the
[3324.24 → 3324.60] issues
[3324.60 → 3325.04] with
[3325.04 → 3325.58] Heroku
[3325.58 → 3325.78] as
[3325.78 → 3325.98] well
[3325.98 → 3326.50] you
[3326.50 → 3326.68] didn't
[3326.68 → 3326.84] have
[3326.84 → 3327.14] those
[3327.14 → 3327.76] nice
[3327.76 → 3328.24] hooks
[3328.24 → 3328.90] to
[3328.90 → 3329.42] put
[3329.42 → 3329.60] into
[3329.60 → 3329.74] them
[3329.74 → 3329.86] like
[3329.86 → 3331.18] pre
[3331.18 → 3331.48] start
[3331.48 → 3331.74] pre
[3331.74 → 3332.06] stop
[3332.06 → 3332.66] all
[3332.66 → 3332.96] that
[3332.96 → 3333.16] is
[3333.16 → 3333.36] just
[3333.36 → 3333.56] like
[3333.56 → 3333.70] a
[3333.70 → 3333.90] bit
[3333.90 → 3334.28] I
[3334.28 → 3334.50] know
[3334.50 → 3334.70] it's
[3334.70 → 3334.90] like
[3334.90 → 3335.34] the
[3335.34 → 3335.70] detail
[3335.70 → 3335.90] that
[3335.90 → 3336.22] the
[3336.22 → 3336.56] majority
[3336.56 → 3336.94] doesn't
[3336.94 → 3337.16] care
[3337.16 → 3337.46] about
[3337.46 → 3338.14] but
[3338.14 → 3338.34] for
[3338.34 → 3338.58] us
[3338.58 → 3338.72] it's
[3338.72 → 3338.90] really
[3338.90 → 3339.22] important
[3339.22 → 3339.40] like
[3339.40 → 3339.62] how
[3339.62 → 3339.82] can
[3339.82 → 3339.96] we
[3339.96 → 3340.20] trigger
[3340.20 → 3340.36] for
[3340.36 → 3340.64] example
[3340.64 → 3340.96] backup
[3340.96 → 3341.24] before
[3341.24 → 3341.40] we
[3341.40 → 3341.56] run
[3341.56 → 3341.64] a
[3341.64 → 3342.10] migration
[3342.10 → 3343.18] or
[3343.18 → 3343.40] if
[3343.40 → 3343.52] an
[3343.52 → 3343.66] app
[3343.66 → 3344.04] crashes
[3344.04 → 3344.52] can
[3344.52 → 3344.90] we
[3344.90 → 3345.90] save
[3345.90 → 3346.06] the
[3346.06 → 3346.34] crash
[3346.34 → 3346.56] dump
[3346.56 → 3347.00] somewhere
[3347.00 → 3347.28] the
[3347.28 → 3347.50] Erlang
[3347.50 → 3347.80] crash
[3347.80 → 3348.10] dump
[3348.10 → 3348.86] and
[3348.86 → 3349.40] things
[3349.40 → 3349.60] like
[3349.60 → 3350.22] these
[3350.22 → 3350.52] that
[3350.52 → 3351.18] especially
[3351.18 → 3351.76] when
[3351.76 → 3351.88] you
[3351.88 → 3352.00] are
[3352.00 → 3352.20] so
[3352.20 → 3352.58] deeply
[3352.58 → 3352.98] integrated
[3352.98 → 3353.26] with
[3353.26 → 3353.74] Phoenix
[3353.74 → 3354.24] and
[3354.24 → 3354.74] Elixir
[3354.74 → 3355.08] as
[3355.08 → 3355.30] Fly
[3355.30 → 3355.66] is
[3355.66 → 3356.46] we
[3356.46 → 3356.70] should
[3356.70 → 3356.92] have
[3356.92 → 3357.18] those
[3357.18 → 3357.54] things
[3357.54 → 3358.00] because
[3358.00 → 3358.18] they
[3358.18 → 3358.34] are
[3358.34 → 3359.18] first
[3359.18 → 3359.66] class
[3359.66 → 3359.92] in
[3359.92 → 3360.36] Erlang
[3360.36 → 3361.12] Elixir
[3361.12 → 3361.28] and
[3361.28 → 3361.64] Phoenix
[3361.64 → 3362.26] that's
[3362.26 → 3362.40] one
[3362.40 → 3362.60] right
[3362.60 → 3362.92] there
[3362.92 → 3363.32] so
[3363.32 → 3363.42] I
[3363.42 → 3363.72] like
[3363.72 → 3363.92] that
[3363.92 → 3364.08] I
[3364.08 → 3364.20] can
[3364.20 → 3364.30] do
[3364.30 → 3364.56] fly
[3364.56 → 3365.02] logs
[3365.02 → 3365.36] like
[3365.36 → 3365.44] I
[3365.44 → 3365.58] used
[3365.58 → 3365.68] to
[3365.68 → 3365.84] do
[3365.84 → 3366.18] Heroku
[3366.18 → 3366.54] logs
[3366.54 → 3366.80] dash
[3366.80 → 3367.22] tail
[3367.22 → 3367.58] and
[3367.58 → 3368.08] right
[3368.08 → 3368.38] there
[3368.38 → 3368.66] easy
[3368.66 → 3368.82] to
[3368.82 → 3368.96] get
[3368.96 → 3369.12] at
[3369.12 → 3369.28] my
[3369.28 → 3369.66] logs
[3369.66 → 3370.40] I
[3370.40 → 3370.50] would
[3370.50 → 3370.78] also
[3370.78 → 3371.02] like
[3371.02 → 3371.22] those
[3371.22 → 3371.36] to
[3371.36 → 3371.50] be
[3371.50 → 3371.64] in
[3371.64 → 3372.16] Honeycomb
[3372.16 → 3372.44] so
[3372.44 → 3373.22] query
[3373.22 → 3373.48] them
[3373.48 → 3373.90] later
[3373.90 → 3374.22] and
[3374.22 → 3374.42] so
[3374.42 → 3374.58] I
[3374.58 → 3374.66] don't
[3374.66 → 3374.80] know
[3374.80 → 3375.22] that's
[3375.22 → 3375.42] probably
[3375.42 → 3376.00] a
[3376.00 → 3376.40] Gerhard
[3376.40 → 3376.70] thing
[3376.70 → 3376.82] is
[3376.82 → 3376.92] that
[3376.92 → 3377.02] a
[3377.02 → 3377.34] fly
[3377.34 → 3377.76] thing
[3377.76 → 3378.86] so
[3378.86 → 3379.18] that
[3379.18 → 3379.30] would
[3379.30 → 3379.36] be
[3379.36 → 3379.44] a
[3379.44 → 3379.60] next
[3379.60 → 3379.78] step
[3379.78 → 3379.88] I
[3379.88 → 3379.96] would
[3379.96 → 3380.06] love
[3380.06 → 3380.18] to
[3380.18 → 3380.32] see
[3380.32 → 3380.48] it's
[3380.48 → 3380.62] not
[3380.62 → 3380.72] a
[3380.72 → 3380.92] fly
[3380.92 → 3381.20] feature
[3381.20 → 3381.62] request
[3381.62 → 3381.84] it's
[3381.84 → 3381.96] just
[3381.96 → 3382.20] like
[3382.20 → 3382.98] can
[3382.98 → 3383.08] we
[3383.08 → 3383.22] get
[3383.22 → 3383.54] everything
[3383.54 → 3383.76] into
[3383.76 → 3384.16] Honeycomb
[3384.16 → 3384.34] now
[3384.34 → 3384.46] that
[3384.46 → 3384.56] we
[3384.56 → 3384.72] have
[3384.72 → 3384.82] it
[3384.82 → 3385.02] set
[3385.02 → 3385.20] up
[3385.20 → 3385.72] specifically
[3385.72 → 3386.30] logs
[3386.30 → 3387.36] from
[3387.36 → 3387.54] the
[3387.54 → 3388.18] app
[3388.18 → 3388.90] specifically
[3388.90 → 3389.72] exactly
[3389.72 → 3390.06] yeah
[3390.06 → 3390.54] the
[3390.54 → 3390.74] app
[3390.74 → 3391.36] telemetry
[3391.36 → 3391.82] the
[3391.82 → 3392.30] elixir
[3392.30 → 3392.60] phoenix
[3392.60 → 3393.00] oh
[3393.00 → 3393.30] yes
[3393.30 → 3393.64] I
[3393.64 → 3393.84] would
[3393.84 → 3394.04] so
[3394.04 → 3394.22] love
[3394.22 → 3394.44] that
[3394.44 → 3394.56] I
[3394.56 → 3394.66] mean
[3394.66 → 3394.84] that
[3394.84 → 3395.12] was
[3395.12 → 3395.36] like
[3395.36 → 3395.52] on
[3395.52 → 3395.68] our
[3395.68 → 3395.90] list
[3395.90 → 3396.06] for
[3396.06 → 3396.22] like
[3396.22 → 3396.32] a
[3396.32 → 3396.44] long
[3396.44 → 3396.84] time
[3396.84 → 3397.00] but
[3397.00 → 3397.44] now
[3397.44 → 3397.96] when
[3397.96 → 3398.08] we
[3398.08 → 3398.24] did
[3398.24 → 3398.36] the
[3398.36 → 3398.80] migration
[3398.80 → 3399.74] we
[3399.74 → 3399.90] can
[3399.90 → 3400.14] start
[3400.14 → 3400.52] focusing
[3400.52 → 3400.74] on
[3400.74 → 3400.96] these
[3400.96 → 3401.24] things
[3401.24 → 3401.54] how
[3401.54 → 3401.70] to
[3401.70 → 3401.84] do
[3401.84 → 3402.00] that
[3402.00 → 3402.50] integration
[3402.50 → 3402.92] how
[3402.92 → 3403.08] to
[3403.08 → 3403.22] get
[3403.22 → 3403.36] the
[3403.36 → 3403.58] app
[3403.58 → 3404.00] logs
[3404.00 → 3404.80] into
[3404.80 → 3405.10] JSON
[3405.10 → 3405.68] format
[3405.68 → 3406.18] into
[3406.18 → 3406.66] Honeycomb
[3406.66 → 3406.92] so we
[3406.92 → 3407.02] can
[3407.02 → 3407.30] slice
[3407.30 → 3407.44] them
[3407.44 → 3407.78] and dice
[3407.78 → 3408.06] now
[3408.06 → 3408.22] that
[3408.22 → 3408.88] everything
[3408.88 → 3409.06] is
[3409.06 → 3409.18] set
[3409.18 → 3409.30] up
[3409.30 → 3409.44] for
[3409.44 → 3409.72] us
[3409.72 → 3410.40] how
[3410.40 → 3410.54] can
[3410.54 → 3410.64] we
[3410.64 → 3410.76] get
[3410.76 → 3410.88] the
[3410.88 → 3411.08] fly
[3411.08 → 3411.46] proxy
[3411.46 → 3411.88] logs
[3411.88 → 3412.60] into
[3412.60 → 3412.98] Honeycomb
[3412.98 → 3413.30] as well
[3413.30 → 3413.56] is it
[3413.56 → 3413.72] even
[3413.72 → 3414.16] possible
[3414.16 → 3414.50] I
[3414.50 → 3414.68] don't
[3414.68 → 3414.88] know
[3414.88 → 3415.06] but
[3415.06 → 3415.22] we
[3415.22 → 3415.38] would
[3415.38 → 3415.62] want
[3415.62 → 3415.92] that
[3415.92 → 3416.52] that
[3416.52 → 3416.66] was
[3416.66 → 3416.80] the
[3416.80 → 3417.16] important
[3417.16 → 3417.46] one
[3417.46 → 3417.96] ingress
[3417.96 → 3418.62] nginx
[3418.62 → 3419.00] logs
[3419.00 → 3419.44] in
[3419.44 → 3419.78] Kubernetes
[3419.78 → 3420.16] we
[3420.16 → 3420.32] were
[3420.32 → 3420.62] really
[3420.62 → 3420.94] using
[3420.94 → 3421.22] those
[3421.22 → 3421.44] big
[3421.44 → 3421.74] time
[3421.74 → 3421.98] because
[3421.98 → 3422.16] that
[3422.16 → 3422.28] was
[3422.28 → 3422.44] the
[3422.44 → 3422.82] interface
[3422.82 → 3423.42] between
[3423.42 → 3424.42] quickly
[3424.42 → 3425.38] and
[3425.38 → 3425.58] the
[3425.58 → 3426.10] application
[3426.10 → 3426.74] and
[3426.74 → 3426.92] okay
[3426.92 → 3427.08] there
[3427.08 → 3427.22] was
[3427.22 → 3427.38] like
[3427.38 → 3427.50] a
[3427.50 → 3427.68] layer
[3427.68 → 3430.08] for
[3430.08 → 3430.24] I
[3430.24 → 3430.60] believe
[3430.60 → 3431.18] so
[3431.18 → 3431.34] it
[3431.34 → 3431.72] wasn't
[3431.72 → 3431.94] like
[3431.94 → 3432.14] you
[3432.14 → 3432.26] know
[3432.26 → 3432.50] like
[3432.50 → 3433.04] in
[3433.04 → 3433.48] the
[3433.48 → 3434.30] network
[3434.30 → 3434.72] stack
[3434.72 → 3435.18] so
[3435.18 → 3435.32] that
[3435.32 → 3435.42] was
[3435.42 → 3435.96] okay
[3435.96 → 3436.54] the
[3436.54 → 3436.86] Postgres
[3436.86 → 3437.06] SQL
[3437.06 → 3437.28] back
[3437.28 → 3437.48] ups
[3437.48 → 3437.58] that
[3437.58 → 3437.68] is
[3437.68 → 3437.78] a
[3437.78 → 3437.92] big
[3437.92 → 3438.18] one
[3438.18 → 3438.44] but
[3438.44 → 3438.66] the
[3438.66 → 3438.96] biggest
[3438.96 → 3439.24] one
[3439.24 → 3439.58] for
[3439.58 → 3439.84] me
[3439.84 → 3440.28] are
[3440.28 → 3440.44] the
[3440.44 → 3440.90] certificates
[3440.90 → 3441.72] so
[3441.72 → 3441.92] we
[3441.92 → 3442.22] use
[3442.22 → 3442.88] cert
[3442.88 → 3443.24] manager
[3443.24 → 3443.88] in
[3443.88 → 3444.28] LIKE
[3444.28 → 3445.00] our
[3445.00 → 3445.54] certificates
[3445.54 → 3446.04] will
[3446.04 → 3446.46] expire
[3446.46 → 3446.64] in
[3446.64 → 3446.84] two
[3446.84 → 3447.22] months
[3447.22 → 3447.74] if
[3447.74 → 3447.84] we
[3447.84 → 3447.98] don't
[3447.98 → 3448.12] do
[3448.12 → 3448.42] anything
[3448.42 → 3448.70] and
[3448.70 → 3448.96] things
[3448.96 → 3449.08] will
[3449.08 → 3449.34] break
[3449.34 → 3449.92] so
[3449.92 → 3450.00] we
[3450.00 → 3450.10] have
[3450.10 → 3450.28] two
[3450.28 → 3450.50] months
[3450.50 → 3450.64] to
[3450.64 → 3450.80] fix
[3450.80 → 3450.96] this
[3450.96 → 3451.30] problem
[3451.30 → 3451.62] we
[3451.62 → 3451.76] have
[3451.76 → 3453.44] a
[3453.44 → 3453.54] new
[3453.54 → 3453.86] deadline
[3453.86 → 3454.06] you
[3454.06 → 3454.30] expand
[3454.30 → 3454.40] it
[3454.40 → 3454.48] from
[3454.48 → 3454.88] 48
[3454.88 → 3455.36] hours
[3455.36 → 3455.56] out
[3455.56 → 3455.72] to
[3455.72 → 3455.96] two
[3455.96 → 3456.14] months
[3456.14 → 3456.52] exactly
[3456.52 → 3457.12] that
[3457.12 → 3457.28] is
[3457.28 → 3457.52] the
[3457.52 → 3457.86] next
[3457.86 → 3458.08] step
[3458.08 → 3458.26] so
[3458.26 → 3458.46] by
[3466.54 → 3466.88] describe
[3466.88 → 3467.10] the
[3467.10 → 3467.48] problem
[3467.48 → 3467.96] why
[3467.96 → 3468.08] is
[3468.08 → 3468.14] it
[3468.14 → 3468.24] more
[3468.24 → 3468.58] difficult
[3468.58 → 3468.80] on
[3468.80 → 3469.04] fly
[3469.04 → 3469.30] so
[3469.30 → 3469.44] we
[3469.44 → 3469.54] were
[3469.54 → 3469.76] running
[3469.76 → 3470.04] cert
[3470.04 → 3470.32] manager
[3470.32 → 3470.76] before
[3470.76 → 3471.00] which
[3471.00 → 3471.12] was
[3471.12 → 3471.42] managing
[3471.42 → 3471.68] our
[3471.68 → 3472.28] certificates
[3472.28 → 3473.28] fly
[3473.28 → 3474.08] is
[3474.08 → 3474.48] able
[3474.48 → 3474.70] to
[3474.70 → 3474.90] manage
[3474.90 → 3475.40] certificates
[3475.40 → 3476.30] but
[3476.30 → 3476.46] we
[3476.46 → 3476.86] can't
[3476.86 → 3476.98] get
[3476.98 → 3477.12] the
[3477.12 → 3477.38] private
[3477.38 → 3477.68] key
[3477.68 → 3478.06] and
[3478.06 → 3478.24] because
[3478.24 → 3478.40] we
[3478.40 → 3478.72] can't
[3478.72 → 3478.80] get
[3478.80 → 3478.94] the
[3478.94 → 3479.20] private
[3479.20 → 3479.42] key
[3479.42 → 3479.64] we
[3479.64 → 3480.00] can't
[3480.00 → 3480.32] upload
[3480.32 → 3480.54] it
[3480.54 → 3481.02] to
[3481.02 → 3481.76] quickly
[3481.76 → 3482.32] to
[3482.32 → 3482.46] the
[3482.46 → 3482.86] CDN
[3482.86 → 3483.62] if
[3483.62 → 3483.80] the
[3483.80 → 3484.26] CDN
[3484.26 → 3484.46] if
[3484.46 → 3484.88] quickly
[3484.88 → 3485.18] manages
[3485.18 → 3485.62] certificates
[3485.62 → 3486.00] for
[3486.00 → 3486.32] us
[3486.32 → 3486.98] no
[3486.98 → 3487.14] one
[3487.14 → 3487.34] else
[3487.34 → 3487.68] can
[3487.68 → 3487.90] which
[3487.90 → 3488.10] means
[3488.10 → 3488.24] that
[3488.24 → 3488.50] fly
[3488.50 → 3489.38] can't
[3489.38 → 3489.72] because
[3489.72 → 3489.96] they
[3489.96 → 3490.30] add
[3490.30 → 3490.76] a
[3490.76 → 3491.08] CNAME
[3491.08 → 3491.50] record
[3491.50 → 3491.82] for
[3491.82 → 3492.12] the
[3492.12 → 3492.60] ACME
[3492.60 → 3493.10] let's
[3493.10 → 3493.52] encrypt
[3493.52 → 3494.36] integration
[3494.36 → 3495.06] and
[3495.06 → 3495.30] only
[3495.30 → 3495.56] one
[3495.56 → 3495.68] of
[3495.68 → 3495.78] them
[3495.78 → 3495.94] can
[3495.94 → 3496.20] manage
[3496.20 → 3496.30] it
[3496.30 → 3496.42] in
[3496.42 → 3496.90] any
[3496.90 → 3497.12] one
[3497.12 → 3497.40] time
[3497.40 → 3497.92] if
[3497.92 → 3498.32] quickly
[3498.32 → 3498.52] does
[3498.52 → 3498.72] it
[3498.72 → 3499.32] we
[3499.32 → 3499.62] can't
[3499.62 → 3499.72] get
[3499.72 → 3499.84] the
[3499.84 → 3500.10] private
[3500.10 → 3500.38] key
[3500.38 → 3501.10] if
[3501.10 → 3501.34] fly
[3501.34 → 3501.58] does
[3501.58 → 3501.76] it
[3501.76 → 3502.10] we
[3502.10 → 3502.34] can't
[3502.34 → 3502.44] get
[3502.44 → 3502.56] the
[3502.56 → 3502.80] private
[3502.80 → 3503.04] key
[3503.04 → 3503.24] so
[3503.24 → 3503.52] only
[3503.52 → 3503.94] one
[3503.94 → 3504.18] can
[3504.18 → 3504.36] have
[3504.36 → 3504.46] it
[3504.46 → 3504.58] at
[3504.58 → 3504.86] any
[3504.86 → 3505.02] one
[3505.02 → 3505.26] point
[3505.26 → 3505.42] in
[3505.42 → 3505.70] time
[3505.70 → 3506.48] so
[3506.48 → 3507.54] maybe
[3507.54 → 3508.54] maybe
[3508.54 → 3508.80] this
[3508.80 → 3509.00] time
[3509.00 → 3509.26] around
[3509.26 → 3509.42] we
[3509.42 → 3509.62] can
[3509.62 → 3510.08] use
[3510.08 → 3510.84] quickly
[3510.84 → 3511.42] so
[3511.42 → 3511.78] quickly
[3511.78 → 3511.92] will
[3511.92 → 3512.16] manage
[3512.16 → 3512.50] the
[3512.50 → 3512.94] certificates
[3519.72 → 3520.10] so
[3520.10 → 3520.30] maybe
[3520.30 → 3520.54] that
[3520.54 → 3520.68] is
[3520.68 → 3520.96] the
[3520.96 → 3521.60] simplest
[3521.60 → 3521.96] thing
[3521.96 → 3522.34] let
[3522.34 → 3522.78] quickly
[3522.78 → 3523.06] manage
[3523.06 → 3523.40] our
[3523.40 → 3524.22] certificate
[3524.22 → 3524.66] what
[3524.66 → 3524.88] about
[3524.88 → 3525.04] you
[3525.04 → 3525.28] Adam
[3525.28 → 3525.74] what
[3525.74 → 3525.84] is
[3525.84 → 3525.94] the
[3525.94 → 3526.08] thing
[3526.08 → 3526.22] that
[3526.22 → 3526.36] you
[3526.36 → 3526.50] would
[3526.50 → 3526.74] like
[3526.74 → 3527.04] to
[3527.04 → 3527.24] happen
[3527.24 → 3527.62] next
[3527.62 → 3528.06] I
[3528.06 → 3528.28] think
[3528.28 → 3528.48] just
[3528.48 → 3528.74] keep
[3528.74 → 3529.06] going
[3529.06 → 3529.62] copacetic
[3529.62 → 3530.04] you know
[3530.04 → 3530.58] I don't
[3530.58 → 3530.74] have
[3530.74 → 3530.90] any
[3530.90 → 3531.50] particular
[3531.50 → 3532.06] requests
[3532.06 → 3532.72] I've
[3532.72 → 3532.82] been
[3532.82 → 3533.08] enjoying
[3533.08 → 3533.46] Honeycomb
[3533.46 → 3533.68] I know
[3533.68 → 3533.98] both of
[3533.98 → 3534.02] you
[3534.02 → 3534.12] have
[3534.12 → 3534.44] desires
[3534.44 → 3534.60] to
[3534.60 → 3534.72] get
[3534.72 → 3534.94] more
[3534.94 → 3535.06] of
[3535.06 → 3535.18] our
[3535.18 → 3535.58] logs
[3535.58 → 3535.82] and
[3535.82 → 3536.58] whatnot
[3536.58 → 3536.88] into
[3536.88 → 3537.30] Honeycomb
[3537.30 → 3537.70] I know
[3537.70 → 3537.96] in
[3537.96 → 3538.32] particular
[3538.32 → 3538.64] I've
[3538.64 → 3538.76] been
[3538.76 → 3539.18] enjoying
[3539.18 → 3539.92] how I
[3539.92 → 3540.06] can
[3540.06 → 3540.40] communicate
[3540.40 → 3540.74] back
[3540.74 → 3540.90] to
[3540.90 → 3552.98] the
[3552.98 → 3553.16] I've
[3553.16 → 3553.24] been
[3553.24 → 3553.44] enjoying
[3553.44 → 3553.76] Honeycomb
[3553.76 → 3553.96] for
[3553.96 → 3554.12] that
[3554.12 → 3554.44] reason
[3554.44 → 3554.90] plus
[3554.90 → 3555.18] a lot
[3555.18 → 3555.26] of
[3555.26 → 3555.36] the
[3555.36 → 3555.52] stuff
[3555.52 → 3555.64] we're
[3555.64 → 3555.78] doing
[3555.78 → 3556.04] around
[3556.04 → 3556.94] podcasts
[3556.94 → 3558.14] we have
[3558.14 → 3558.64] our own
[3558.64 → 3559.64] dashboards
[3559.64 → 3560.04] and metrics
[3560.04 → 3560.52] inside
[3560.52 → 3561.02] the app
[3561.02 → 3561.52] itself
[3561.52 → 3561.94] but
[3561.94 → 3562.28] there's
[3562.28 → 3562.56] different
[3562.56 → 3562.80] ways
[3562.80 → 3563.04] you can
[3563.04 → 3563.34] actually
[3563.34 → 3563.66] slice
[3563.66 → 3564.06] and dice
[3564.06 → 3564.30] the
[3564.30 → 3564.78] logs
[3564.78 → 3565.28] inside
[3565.28 → 3565.66] Honeycomb
[3565.66 → 3565.90] which
[3565.90 → 3566.24] I think
[3566.24 → 3566.32] is
[3566.32 → 3566.48] pretty
[3566.48 → 3566.76] unique
[3566.76 → 3566.96] so
[3566.96 → 3567.84] I
[3567.84 → 3568.08] like
[3568.08 → 3568.22] that
[3568.22 → 3568.34] so
[3568.34 → 3568.42] I've
[3568.42 → 3568.52] been
[3568.52 → 3568.96] enjoying
[3568.96 → 3569.36] Honeycomb
[3569.36 → 3569.56] from
[3569.56 → 3569.76] that
[3569.76 → 3570.20] perspective
[3570.20 → 3570.42] and
[3570.42 → 3574.78] just getting more of the app logs and that would be kind of interesting too so I look forward to
[3574.78 → 3580.02] that I look forward to I guess I'll tee up if you don't mind your next episode then so after episode
[3580.02 → 3587.00] 50 you're having mark on from fly yeah talking deeply about other specifics can you kind
[3587.00 → 3591.54] of talk about what that's going to be about what's that show going to be about so it was literally
[3591.54 → 3597.38] the follow-up to this one like take all the things that we've learned about fly all the things that
[3597.38 → 3603.64] we would like to see improved all the things that are maybe coming in fly that would help us things
[3603.64 → 3609.24] that we would like to know about and how do we continue strengthening our collaboration because
[3609.24 → 3614.36] this is a first great collaboration similar to honeycomb and I'm very fond of that I think that
[3614.36 → 3620.28] was the one that you know really shines among all our partners in that we can do things in a
[3620.28 → 3626.70] different way and I really enjoy that so what does the equivalent look with fly what about the upgrades
[3626.70 → 3631.54] what about the build packs like what don't we know when it comes to the fly platform because we come
[3631.54 → 3637.74] from Kubernetes maybe we're doing certain things in a way that in fly are suboptimal so what are those
[3637.74 → 3642.84] things what can we do better that we don't even know about that the platform solves for us, and it's
[3642.84 → 3647.42] just like you know going back I know that we're holding it wrong but I don't know what right looks
[3647.42 → 3652.32] like so can mark tell us what like right looks like right maybe a cert manager maybe this whole scenario
[3652.32 → 3657.42] around certificates could be like okay well we can actually hit this flag and enable you to see
[3657.42 → 3661.26] your private key, and you could take it elsewhere if you want to so we manage it but sure we'll share
[3661.26 → 3666.30] that private key with you either behind the scenes or in an UI if that's maybe not a security measure but
[3666.30 → 3670.18] he'll probably have some sort of reasoning for that like jarred said there's a reason for they're
[3670.18 → 3673.92] doing it but jarred maybe you get some of your feature requests right away it's like mark listens to
[3673.92 → 3678.12] this show before episode 51 and there you go here's some presents it's not even Christmas
[3678.12 → 3685.22] I love that yeah I'm excited I mean episode 50 big deals a year later we're on a new platform
[3685.22 → 3691.08] we're seeing hello to new partners which is amazing i like fly like hurt like the team
[3691.08 → 3697.26] a lot of respect there and I think what next what's next for me really the big thing is just hope
[3697.26 → 3702.78] is that we can help improve the fly platform we can help improve our platform and then as we
[3702.78 → 3707.76] you know continue down that journey we'll share that story here on ship it and if
[3707.76 → 3712.86] as a listener you're running Kubernetes you're managing Kubernetes but maybe at a lever higher
[3712.86 → 3718.72] up I'm thinking cloud run, and you want to partner with us, I would be very keen to trying out another
[3718.72 → 3725.46] origin like fly is great we really like it, but it's always a strength in diversity can we see what
[3725.46 → 3732.16] does the alternative look like can we still remain plugged in the ecosystem which lets be honest the
[3732.16 → 3737.10] majority are using Kubernetes and if we don't use Kubernetes ourselves the best one out there
[3737.10 → 3741.80] will we have the same insights will it still be as relevant will I be able to have the conversations
[3741.80 → 3749.20] that I wish I could have with some of the future guests on the show so if you know a platform that
[3749.20 → 3753.86] does Kubernetes really, really well, and maybe it's like a layer up from that, and you would like you
[3753.86 → 3761.14] know us to run a change log there reach out to us, I'm very keen to have that conversation and to try
[3761.14 → 3767.16] it out and to see how it compares because you know one of my sayings you always want to have the same
[3767.16 → 3773.36] thing you know in this case origins so fly it's amazing just to have fly but what if fly goes down
[3773.36 → 3779.04] it will happen let's be honest about it and quickly that it can take five years in case it can take 10
[3779.04 → 3783.82] years maybe less we don't know that's the one thing which we don't know, but we do know that it will go
[3783.82 → 3788.46] down at some point so how do we mitigate against that what is the plan b because right now there's no
[3788.46 → 3794.02] plan b right it's fly or I mean we have fast in front great you're speaking of like business
[3794.02 → 3801.30] continuity kind of failover type situation where if the platform fly fell down there was an outage
[3801.30 → 3806.60] yeah failover switch over site continues to be deployed that's what you have with a Kubernetes
[3806.60 → 3813.16] system is you can you know move to a different origin just another origin right so plan b is another
[3813.16 → 3817.94] origin maybe the other origin is still a Kubernetes origin and I mean let's be honest the world
[3817.94 → 3823.36] is moving multi-platform I mean that that's what's already happening and some systems are so
[3823.36 → 3829.32] complicated that it takes years and I don't know how many hundreds of thousands of engineering hours
[3829.32 → 3834.66] to get you there our system is a lot simpler, and we've been improving it we've been like you know
[3834.66 → 3840.32] making it as portable and as small and as streamlined as possible so it shouldn't be that difficult to run
[3840.32 → 3845.34] it elsewhere PostgreSQL will have a single instance right we have like some, and now we have like a
[3845.34 → 3850.34] replicas as well we have readers like all that's managed so we can connect to that we may need to
[3850.34 → 3855.86] set up a wire guard tunnel, but that's okay not a problem we can do that, so the database will be the
[3855.86 → 3861.38] same but can we run it on a different platform maybe we can dream if you're not dreaming or even
[3861.38 → 3866.08] that's right that's right if you're into that journey, and you're listening to this show and you
[3866.08 → 3870.08] haven't subscribed yet the easiest way to do that is to go to changelaw.com
[3870.08 → 3874.42] slash ship it and there's all the ways to subscribe to the show there so if you're
[3874.42 → 3879.84] digging this journey so far or if you've been here for all 50 thank you if this is your first
[3879.84 → 3884.38] because somebody's like hey there was this show and this migration and this and that or whatever
[3884.38 → 3892.28] you know welcome go subscribe and uh and join us on this journey and if you're at Rubicon EU Valencia
[3892.28 → 3898.60] I'll be there look me up yes if we want to record something we can go for that just have a
[3898.60 → 3904.40] conversation I still love Kubernetes even if we're on fly by heart still beats Kubernetes every
[3904.40 → 3910.84] other beat is Kubernetes and is cloud native so we still like that very much so yeah let us know what
[3910.84 → 3916.52] is new and what else we don't know because I'm sure things are changing all the time what's the best
[3916.52 → 3922.16] way to reach out to you what is the best way well twitter get hard on see you on Twitter also on the
[3922.16 → 3927.70] change law slack I'm I check it out at least once a day, so there's or request an episode that's like
[3927.70 → 3933.34] another way or get hard at changelaw.com that also works, and we'll have this in the show notes too
[3933.34 → 3938.82] you mentioned issue 407 which is quite thick I mean there are a lot of details there so as an
[3938.82 → 3944.40] encouragement from there from here reach out to gear hard about Rubicon EU and what's happening there
[3944.40 → 3950.70] and then also dig deep into issue 407 we'll link up the show notes there are lots of details to go
[3950.70 → 3955.16] there so if you just enjoy the details of this kind of migration, and you want to learn from
[3955.16 → 3959.74] our learnings then yeah it's about to go I hope you enjoyed the show semi tell us what we should do
[3959.74 → 3969.34] next semi the clerk we are listener driven not rust but yeah what crazy dot rust okay baby go
[3969.34 → 3978.38] so okay microservices k native yes okay cloud run I can already see it someone stop me slow down slow
[3978.38 → 3983.66] down all right thank you Adam thank you jarred for joining me this is a great pleasure always having
[3983.66 → 3988.58] you always in your Kaiden they're like so it's so different so special to me thank you very much for
[3988.58 → 3993.04] being part of the journey forever before to the next one yeah Kaiden Kaiden Kaiden
[3993.04 → 4002.38] thank you for tuning into another episode of ship it check out our other podcasts for developers
[4002.38 → 4009.18] at changelog.com slash master you can connect with like-minded developers from all over the world
[4009.18 → 4015.58] via changelog.com slash community thank you quickly for the worldwide low latency changelog.com
[4015.58 → 4023.88] our listeners love those blazing fast mp3s your beats our awesome break master cylinder that's it for
[4023.88 → 4030.36] this week see you all next week my last thing for today is wondering what happens next now that we
[4030.36 → 4036.52] have migrated from Kubernetes to pass what am I missing it has been a good six years since I've used
[4036.52 → 4042.76] the pass for production and I'm sure many things are different today if you migrated from Kubernetes
[4042.76 → 4050.04] to pass and want to share your story find me on changelog.slack.com or twitter at Garrard lasso
