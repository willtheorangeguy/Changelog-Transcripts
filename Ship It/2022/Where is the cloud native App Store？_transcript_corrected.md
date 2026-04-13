[0.08 → 5.30] You are listening to Ship It, a podcast about operations, infrastructure, and Git Ops.
[5.76 → 11.18] I'm your host, Gerhard Laze, and I'm really excited about our first 2022 episode.
[11.78 → 17.50] Today, I'm talking with Alexis Richardson, co-founder and CEO of Weave Works, about going
[17.50 → 22.62] fully remote, what a great team looks like, and Git Ops, which is a way of implementing
[22.62 → 24.96] continuous deployment for cloud-native applications.
[24.96 → 32.04] If you haven't heard of OpenGitOps yet, now would be a good time to check out OpenGitOps.dev.
[32.46 → 37.38] The most interesting part of today's conversation is the missing cloud-native app store.
[37.78 → 43.26] While Apple revolutionized the world with the app store and the iPhone, we don't yet have
[43.26 → 45.44] something similar for cloud-native apps.
[45.94 → 51.24] You may be thinking, but what about Operator Hub or all the Helm registries out there?
[51.24 → 58.46] And I can tell you that the registry fragmentation, Operator Deprecations, and lack of curation are
[58.46 → 61.14] not what people have in mind when they think app store.
[61.68 → 63.40] Alexis has a great take on this.
[63.86 → 66.90] I really enjoyed our conversation, and I think that you will too.
[67.38 → 71.08] Big thanks to our partners Vastly, Launch Darkly, and Linde.
[71.36 → 73.16] Thank you for the great bandwidth Vastly.
[73.48 → 75.64] You can learn more at Fastly.com.
[76.00 → 80.24] Ship new features with confidence by getting your feature flags, powered by LaunchDarkly.com.
[80.24 → 83.80] And thank you, Linde, for keeping our Kubernetes fast and simple.
[84.24 → 88.42] Run your setup as we do via Linode.com forward slash change load.
[93.68 → 94.86] What's going on, shippers?
[95.08 → 95.62] Adam here.
[95.70 → 100.96] I want to tell you about one of our new partners for 2022, MongoDB, the makers of MongoDB Atlas,
[101.16 → 103.26] the multi-cloud application data platform.
[103.72 → 109.86] MongoDB Atlas is an integrated suite of cloud database and database services designed to accelerate
[109.86 → 112.14] and simplify how you build with data.
[112.14 → 116.16] Ship application features faster with a first-class developer experience.
[116.54 → 119.62] Extend your data naturally with an elegant data architecture.
[120.18 → 124.24] Scale your applications confidently with a foundation built for resilience, performance,
[124.46 → 125.16] and security.
[125.70 → 128.50] And run anywhere in the world with global and multi-cloud reach.
[128.76 → 135.20] Deliver fast and consistent user experiences in any region on AWS, Azure, and Google Cloud.
[135.20 → 141.64] Or replicate data across multiple regions and clouds to reach wider audiences and protect against broader outages.
[142.04 → 143.96] Try MongoDB Atlas for free today.
[144.08 → 149.64] They have a free forever tier so you can prove yourself and your team that the platform has everything you need.
[149.90 → 151.86] Head to MongoDB.com slash Atlas.
[152.24 → 154.94] Again, MongoDB.com slash Atlas.
[154.94 → 164.26] We are going to ship in three, two, one.
[178.18 → 182.98] So I'm really glad that we managed to get together again because it's been quite some time.
[182.98 → 189.66] It's actually been a change block episode 374, which was part one of my Rubicon North America 2019.
[190.06 → 190.76] So it's been a while.
[191.06 → 197.26] I know that many things have changed for you, Alexis, and for WeWork's as well since the last time that we talked.
[197.74 → 202.58] So I'm wondering, what is the most meaningful change for you in the last two years?
[202.82 → 204.08] Apart from all the obvious ones.
[204.42 → 207.26] You know, like there was this thing, what was it called again?
[208.14 → 208.92] I forgot.
[208.92 → 211.06] But it's just all a blur.
[211.20 → 218.12] No, I mean, to me, a big change is that I moved house to Oxford, which goes with us going fully distributed.
[218.36 → 223.54] We'd always been a distributed company, actually, with people in the US, Europe, even Asia as well.
[223.74 → 229.44] But of course, with the pandemic, we moved out of our physical offices and became fully remote for a while.
[229.44 → 231.86] And now we're sort of probably going to stay mostly that way.
[232.20 → 234.78] It's good to have a couple of places to get together now and then.
[234.78 → 243.10] And with some changing family circumstances, I moved out to Oxford, which is a lovely town 60 miles outside London, where I grew up.
[243.40 → 246.24] Last time I was here, there was hardly any tech.
[246.72 → 251.60] And I was expecting it to be still essentially a bit of a desolate wasteland of technology.
[251.84 → 253.92] But actually, it's grown a lot since then.
[254.02 → 259.14] And even getting investors who are willing to come and see WeWork's in Oxford, which is quite exciting.
[259.58 → 259.66] Okay.
[259.78 → 262.24] Company's done really well in the time through the pandemic.
[262.38 → 264.18] I'm really proud of what the team has achieved.
[264.18 → 269.30] I think it's a testimony to our culture, our willingness to work together and help customers.
[269.92 → 274.98] And I suppose on the technology side, our Git Ops message has really taken hold.
[275.36 → 276.40] People understand it.
[276.48 → 277.16] It's widespread.
[277.76 → 280.16] We have products that implement Git Ops very clearly.
[280.46 → 282.56] So do other people, which was always an intention.
[282.76 → 289.26] We wanted it to be not a Git Ops not to be a product, but a particular trend that everybody could implement in their own way.
[289.26 → 299.94] The CNCF did a Git Ops definition in the working group, which had, I think, over 100 participants from almost as many companies and came up with something that was just five lines long.
[300.28 → 301.38] But we'll do for now.
[302.14 → 310.62] The only thing I can say is it took less time for 100 people to agree on a definition of Git Ops than it did for six people in the CNCF TOC.
[310.62 → 314.06] Sorry, 10 people to agree on a definition of cloud native.
[315.32 → 315.76] Okay.
[316.10 → 316.40] Okay.
[316.76 → 319.46] So that is all great signals, I suppose.
[319.68 → 320.98] Yeah, I suppose so.
[321.04 → 324.42] I remember in 2019 when you mentioned GitOps, it was something new to me.
[324.74 → 326.36] And I was thinking, what is this Git Ops?
[326.44 → 328.50] And you mentioned, well, it's been around for quite some time.
[328.64 → 331.08] And, you know, there wasn't quite like a term for it.
[331.14 → 332.82] It wasn't so popularized.
[332.82 → 337.94] And here we are two years later when 100 people can agree on that, what it means.
[338.28 → 338.54] Okay.
[338.92 → 340.98] Where can we find this definition?
[341.30 → 345.44] If you type CNCF Git Ops working group into Google, it should pop up.
[345.58 → 348.72] There is something called OpenGitOps, I think, which has it there.
[348.72 → 356.58] And we'll probably have other things, other kind of conformance things and standard tools that people can use for all kinds of stuff.
[356.62 → 369.80] And it's just the beginning because at the moment, you know, we're still at the that is old is new again stage of technology where, you know, just like containers recapitulated VMs, which recapitulated mainframes.
[369.80 → 381.98] I think that Git Ops recapitulates many, many, many things before it, like DevOps infrastructure as code, CCD, you know, even going back to the early 90s with promise theory from Mark Burgess.
[382.18 → 386.48] And a lot of the ideas that he had are now, I think, easy to implement.
[386.70 → 387.70] That's the key difference.
[388.20 → 394.48] And just like Docker made containers, which were just the Linux person thing, into something that any developer could use.
[394.48 → 399.72] I think Git Ops is making operations into something that any developer can take control of.
[400.26 → 407.60] And that is a really important change because, as I've said again and again, the number of developers is increasing very fast.
[408.16 → 412.00] And it'll probably be 100 million, you know, in the foreseeable future.
[412.00 → 415.84] If it's growing 15% a year, that means it doubles every five years.
[416.22 → 418.02] The question is, what tools will they use?
[418.38 → 419.74] What will their expectations be?
[419.80 → 421.12] What will they build and for whom?
[421.12 → 426.84] And so we think Git Ops is a simplifying solution to a lot of this technology to come.
[427.22 → 427.38] Okay.
[427.38 → 430.68] So we have all these cool technologies.
[430.68 → 433.62] We have the landscape, which is growing, which is expanding.
[434.12 → 436.10] Git Ops, everybody agrees what it is.
[436.38 → 437.76] But there's still something missing.
[438.42 → 440.32] And I know that you recently spoke about this.
[440.76 → 446.10] You're expecting or maybe wishing that there was an app store for the enterprise.
[446.28 → 447.48] We're still missing that.
[447.86 → 450.52] First, what is this app store, and where is it?
[450.74 → 451.56] Because I can't see it.
[451.56 → 456.46] I mean, we have things like, you know, Helm chart repositories as artifact.
[457.22 → 459.90] And companies like Amazon have marketplaces.
[460.10 → 461.56] Red Hat has operator hub.
[461.56 → 473.96] So in a sense, we are little by little getting closer to the idea that there is a systematic way to extend one piece of enterprise software with another.
[474.52 → 478.72] But really, I was talking about, you know, it's a castle in the sky.
[478.72 → 484.34] I mean, you know, I think the reason I discussed the enterprise app store is that in a way, it's such a ridiculous idea.
[484.34 → 494.54] If you look at the presentation that I gave, which if you find Git Ops con, the keynote that I gave for Rubicon, it's all there.
[494.68 → 497.74] And there's a YouTube video and the slides are online.
[498.16 → 500.94] And I'll give you a link afterwards that you can share with your audience.
[501.20 → 508.56] But if you look at it, you'll see that I'm talking about how in technology, we have this sort of pivotal moments.
[508.56 → 516.26] And for me, a really important technology moment in the last few years, not the only one, by any means, was the iPhone.
[516.68 → 519.28] When the iPod appeared, people said, why do we need this?
[519.30 → 520.46] We have the Walkman already.
[520.66 → 523.48] And then they bought it, and they went, oh, that's such a quite cool device.
[523.96 → 526.48] And then we saw that the June was a way to do it badly.
[526.76 → 527.84] You know, don't make it brown.
[528.28 → 529.14] Tip for next time.
[529.34 → 530.14] Things like this.
[530.14 → 535.70] But it wasn't really until that form factor also became a phone and then a camera that people went, hang on a minute.
[535.80 → 539.44] This could be really profound change in how we interact with technology.
[539.66 → 541.74] And, you know, not necessarily even in a good way.
[541.86 → 546.04] I mean, it brings things like Facebook into your life, maybe too intrusively.
[546.36 → 547.92] But it was a really important moment.
[547.92 → 558.90] And if you look at the Apple share price and at the graph of other Apple releases over time, you'll see there's a big push-up after this thing appears, followed closely by the App Store.
[558.90 → 562.54] And what the App Store did was it made it possible to put anything on your phone.
[562.92 → 568.14] And those two together created what, you know, people call the iPhone moment or the App Store moment.
[568.76 → 571.78] It's just a sea change in convenience and experience.
[572.24 → 577.08] And if you think about the web, we need these richer experiences because before that we had HTML.
[577.68 → 579.62] Then we had sort of Ajax.
[580.20 → 582.70] But while that was going on, we had phone apps.
[582.70 → 589.10] And I think you may recall there was this great technology called WAP at one point that everybody was saying was going to change the game.
[589.58 → 596.10] And I was wondering how my, you know, my Nokia 9000 or whatever it was with its screen that was about the size of a coin.
[596.50 → 605.00] And it was LCD was going to help me to do something cool online like I could with Amazon and Yahoo on my phone.
[605.00 → 607.52] And obviously, the technology just wasn't up to it.
[607.86 → 612.24] But with the iPhone and, of course, high bandwidth, you have essentially a computer in your hand.
[612.64 → 617.48] And that means that you can start to build a whole new kind of human experience around it for better or for worse.
[617.86 → 628.04] And so I think that it is appropriate to draw an analogy between then and now and say that we have not had yet the iPhone moment for cloud native technology.
[628.04 → 634.90] I mean, a smaller but equally profound shift was with the web, which then produced Amazon, eBay, etc.
[635.06 → 637.50] I think with the web, we didn't have one moment.
[637.60 → 638.34] We just had lots.
[638.84 → 639.78] You choose your favourite.
[639.90 → 647.12] My favourite might be the day that Google came out or the day that Bill Gates said, you know, the Internet is important or whatever it was.
[647.52 → 650.38] With iPhone, it was a clear single point in time.
[650.38 → 665.36] And I think whether it's a shift of several steps or one thing, cloud native has yet to achieve the kind of obvious change that those moments have where and the characteristic is you can't imagine what life was like before.
[665.52 → 665.68] Yeah.
[665.86 → 672.42] Well, somebody makes a show on TV, and then they have to have everybody with long hair and big suits or old clothes.
[672.42 → 677.68] And they're wearing, you know, instead of carrying phones, they've got to pick up the phone on the desk, and they're all smoking.
[677.92 → 678.60] It's like, oh, I know.
[679.00 → 679.98] We're in the 70s.
[680.06 → 680.42] Great.
[680.76 → 680.94] Yeah.
[681.18 → 685.18] Or, you know, it's early 90s and there's a businessman with a big mobile phone.
[685.28 → 686.40] It's the size of a briefcase.
[686.58 → 689.84] But really, we can't remember that time because it was ridiculous.
[690.18 → 691.26] We didn't have mobile phones.
[691.28 → 692.12] What are you talking about?
[692.12 → 699.90] And so what will the thing be that is the iPhone moment and the App Store moment for cloud native and Kubernetes and everything else?
[700.30 → 702.28] And I really hope it will be a good thing, by the way.
[702.28 → 707.06] And not some sort of another notch on the, you know, the bedpost before you'll expire.
[707.32 → 707.50] Yeah.
[707.84 → 713.32] So I think many people, when they think about the App Store, they just imagine the apps themselves.
[713.60 → 717.72] And the parallel which they would draw is, well, we have Helm, right?
[717.74 → 719.08] We can install these things.
[719.10 → 719.88] It's very simple.
[719.88 → 722.04] And we have these compositions, right?
[722.14 → 723.54] So it's a solved problem.
[723.84 → 728.54] But actually, there's so much more to that than just installing something.
[728.70 → 731.06] And I think that's what the majority is missing.
[731.06 → 732.48] It's all the interactions.
[732.88 → 735.36] I mean, it needs to be in the right state at all times.
[735.36 → 738.76] If you install software, and it stops working, how do you fix it?
[739.08 → 739.26] Yeah.
[739.40 → 742.50] But it goes into, for example, like security, like compliance.
[742.50 → 744.86] It's not just the artifact that you get, right?
[744.88 → 747.30] It's not just the image that you get that it runs.
[747.30 → 750.80] And, you know, it behaves like a, I don't know, like a 12-factor app.
[751.14 → 753.14] Obviously, like since then, things have moved along.
[753.24 → 756.00] But still, it doesn't just, it's not like a cloud native app.
[756.08 → 757.30] There's a lot more to that.
[757.36 → 759.10] It's like it fits in the whole ecosystem.
[759.10 → 760.34] And you have the whole ecosystem.
[760.84 → 762.32] There are upgrades to think about.
[762.54 → 764.94] There are multiple versions to think about.
[765.02 → 766.12] There's like so much stuff.
[766.24 → 767.86] And not everything is an app.
[768.10 → 770.96] You have stateful services or stateful systems.
[771.04 → 771.74] What about those?
[771.74 → 777.38] I mean, they need to get on this, in this world, they need to be operated and, you know,
[777.44 → 779.32] upgraded and managed the same way.
[779.44 → 780.32] What about observability?
[780.40 → 783.62] Then you have concerns which traverse every single app.
[783.78 → 784.82] There's so much to it.
[784.98 → 789.48] Well, I think it's worth contrasting what the world looks like with phone apps, where you
[789.48 → 792.48] don't think about that too much, and the world of enterprise IT.
[793.02 → 797.56] I mean, the reality today with Kubernetes is if you and I decided to have a competition,
[798.00 → 801.62] we start in the same Amazon zone, just be using the same computers, basically.
[802.26 → 804.44] And we use the same version of Kubernetes.
[804.96 → 806.26] Let's say we both use EKS.
[806.46 → 807.88] It's Amazon's provided service.
[808.14 → 808.92] And we install.
[809.60 → 810.46] I install my cluster.
[810.56 → 811.48] You install your cluster.
[811.86 → 814.12] Maybe we each agree to put a couple of things on it.
[814.42 → 818.36] A couple of add-ons, Prometheus, something else, maybe some apps.
[818.82 → 820.28] And we each do it in lockstep.
[820.62 → 821.56] And then we let it run.
[821.60 → 823.38] And then we wait for like a couple of days.
[823.58 → 826.38] I would ask, is your app now the same as my app?
[826.38 → 828.84] And generally, we have no idea.
[828.84 → 832.08] And that is why enterprise IT is still hard.
[832.30 → 836.24] Because we don't want to be in a situation where these things are diverging, potentially.
[836.24 → 838.74] We want to be in a situation where we know that they're correct.
[839.16 → 840.26] We know that they're the same.
[840.30 → 841.62] And we know they're under control.
[842.30 → 843.54] I think this is key.
[843.54 → 850.38] And the presentation that I gave made some sort of pretty cheap jokes at the expense of enterprise IT.
[850.72 → 856.34] You know, the classic IT crowd model with guys in the basement saying, have you turned it off again and on again?
[856.68 → 859.76] But actually, you can't even turn off most enterprise software.
[860.14 → 861.22] It just keeps running.
[861.48 → 862.72] And then upgrading.
[863.30 → 865.90] You know, that's a chance for the team to take a few weeks off.
[865.90 → 874.34] Of deleting, I mean, how many people who did OpenStack POCs back in 2013, 14, they're still running somewhere in the organization.
[874.36 → 874.64] Exactly.
[874.80 → 875.14] Yeah.
[875.24 → 875.88] Even today.
[876.22 → 879.82] And they will for many years because everybody will be scared to touch them, right?
[879.98 → 881.12] Like, I'll leave it there.
[881.46 → 885.06] Who knows how much cruft you would accumulate, right?
[885.10 → 886.12] It's like, you're right.
[886.18 → 888.72] It's difficult to imagine the Nokia before the iPhone.
[888.86 → 890.54] Like, what was that even like, right?
[890.84 → 891.10] App?
[891.16 → 891.98] How would you get an app?
[892.34 → 893.94] And we had the BlackBerry store.
[894.04 → 894.74] I remember that.
[894.74 → 897.58] And that was like, what is running on this one?
[897.58 → 899.88] I have no idea because the interface was all wrong.
[899.98 → 901.28] The interactions were all wrong.
[901.72 → 907.92] So do you know of any enterprises today that have had maybe a mini app store moment?
[908.02 → 908.76] Any examples?
[909.14 → 912.58] Well, I think people are starting to realize that there are some benefits of thinking in this way.
[912.68 → 916.88] I was talking with somebody a couple of days ago about the benefits of Kubernetes fleets.
[917.20 → 920.24] Fleet is basically a heterogeneous group of clusters.
[920.24 → 925.28] If you're following the Kubernetes standards work, things like cluster class are starting to speak to this challenge.
[925.70 → 927.12] You may not know how many there are.
[927.24 → 930.10] You may not know who runs them, but there might be a few thousand clusters.
[930.64 → 933.30] And some of them have some properties that you want to change.
[933.58 → 935.30] Let's say you want to upgrade one of those.
[935.68 → 936.32] Well, hang on a minute.
[936.54 → 937.86] Why are we even upgrading?
[938.38 → 944.54] Wouldn't it be better just to shut the whole thing down and start a completely new one on a new version and then redirect the traffic?
[944.54 → 952.26] If we could make that easy, then for some, but not all cases, that might be a better way than trying to upgrade in place.
[952.38 → 961.36] And that's a perfect example of approaching IT with a consumer mindset instead of an enterprise IT mindset.
[961.54 → 965.60] The whole idea of an upgrade leads us into problems in some cases.
[966.28 → 972.10] I mean, sometimes we dispose of consumer technology because it's not upgrading in the way that we want to.
[972.10 → 975.64] It's just better to get a fresh thing, sadly, and let someone recycle it.
[975.94 → 976.96] So that's a good example.
[977.22 → 983.42] Another example is I see people discussing whether Kubernetes is a cloud or not.
[983.88 → 987.76] And of course, this mindset comes from when Kubernetes appeared.
[988.00 → 990.30] Everybody said, oh, it's like Google for everybody else.
[990.60 → 994.30] And they think, well, Google's running this big cloud, so we can be like Google.
[994.42 → 995.56] Why would we want to be like Google?
[995.62 → 998.32] No one stops to explain this, but let's pretend it's a good idea.
[998.68 → 1000.40] Therefore, Kubernetes must be like OpenStack.
[1000.40 → 1002.02] It must be a private cloud technology.
[1002.42 → 1002.94] Hang on a minute.
[1003.34 → 1005.00] Is it really a private cloud technology?
[1005.44 → 1008.88] Do we really want to have lots of different teams on a single Kubernetes cluster?
[1009.30 → 1011.06] Is it even designed for multi-tenancy?
[1011.28 → 1020.34] If you ask the Kubernetes team if it's designed for multi-tenancy, you will either get the answer, no, or you'll get silence and then looking at the feed.
[1020.78 → 1022.00] And that's Kubernetes, not Borg.
[1022.12 → 1023.10] Borg is a different thing.
[1023.72 → 1025.70] And so actually, it's an app server.
[1026.06 → 1033.58] And if we could, going back to the shutting it down, turning it off and on again easily, always turn it on again in the state that we want it to be in, that would be great.
[1033.96 → 1036.06] It's just like the old days of Java and Tomcat.
[1036.28 → 1038.40] You have a little app running, a Java app running on Tomcat.
[1038.50 → 1039.74] You don't need it anymore.
[1039.82 → 1040.50] You shut it down.
[1040.70 → 1041.38] You want it again?
[1041.38 → 1042.10] You boot it up.
[1042.36 → 1043.60] It just takes a few seconds.
[1043.74 → 1044.48] So what's the problem?
[1044.80 → 1051.18] Now, I know Kubernetes still takes more than a few seconds to boot up, but we're not that far away from it getting to the point of it being convenient.
[1051.98 → 1054.82] And so that then becomes actually a really important goal.
[1054.82 → 1073.04] So when you find people in the industry who do not treat their Kubernetes clusters as special snowflakes, that have to be looked after by a dedicated named team of people, but instead have got to the stage where the whole infrastructure is more or less disposable, give or take a few assumptions.
[1073.56 → 1074.96] And the team are happy to move around.
[1075.04 → 1078.36] And some people are leaving the team and new people are coming in and being productive.
[1078.36 → 1084.76] Then they've moved past that stage of thinking like a cloud and machines and starting to think in terms of disposable technology.
[1085.18 → 1086.74] So those are the signs I'm seeing.
[1086.96 → 1090.42] But nobody is actually trying to solve the whole problem at once.
[1090.48 → 1093.54] Because I think it's probably too big for one person to solve.
[1093.68 → 1096.20] We just see little pieces of the elephant at a time.
[1108.36 → 1115.20] This episode is brought to you by our friends at Ray gun.
[1115.58 → 1119.44] Time is of the essence when identifying and resolving issues in your software.
[1119.92 → 1122.40] And our friends at Ray gun are here to help once again.
[1122.52 → 1127.50] Their brand-new alerting feature is now available for crash reporting and real user monitoring.
[1127.50 → 1133.04] To make sure you're quickly notified of errors, crashes, and front-end performance issues that matter most to you and your business.
[1133.38 → 1134.16] Here's how it works.
[1134.16 → 1142.20] Set thresholds for your alerts based on an increase in error count, a spike in load time, or new issues introduced in the latest deployment.
[1142.58 → 1144.78] Along with custom filters that give you even greater control.
[1145.14 → 1150.44] You can assign multiple users to make sure the right team members are notified with links directly to the issue in Ray gun.
[1150.68 → 1152.82] This takes you to the root cause so much faster.
[1153.28 → 1156.40] Never miss another mission-critical issue in your software again.
[1156.40 → 1163.96] Try Ray gun alerting today and create a world-class issue resolution workflow that gives you and your customers' peace of mind.
[1164.16 → 1166.10] Visit Raygun.com to learn more.
[1166.40 → 1170.82] They have usage-based plans that start at $4 a month with unlimited apps and users.
[1171.42 → 1174.70] Again, that's Raygun.com and start your free 14-day trial.
[1174.70 → 1193.56] I think that makes a lot of sense.
[1193.56 → 1198.52] And I do find myself in a similar situation when it comes to upgrading Kubernetes.
[1198.52 → 1206.54] Not even Kubernetes, even like the components, like the essential components, like external DNS, like cert manager.
[1207.14 → 1212.72] Like you maybe want to install it again from fresh rather than, because there's always drift.
[1213.08 → 1215.96] And that's where all the problems come from.
[1216.70 → 1217.14] Migrations.
[1217.52 → 1219.04] What happens if a migration goes wrong?
[1219.12 → 1222.96] Like you have a backup, then you restore the backup, but you're just like caught like a point in time.
[1223.04 → 1224.08] What if that doesn't work anymore?
[1224.18 → 1224.88] What do you do then?
[1224.88 → 1227.14] How do you recreate the entire world?
[1227.68 → 1231.48] And I think that Git Ops as a model can really help.
[1231.76 → 1238.18] So if you capture your entire definition, like the base zero, and then on top of that, all the things can happen.
[1238.52 → 1243.06] So when you start again, you start from the same baseline, and then whatever needs to happen will happen.
[1243.14 → 1245.30] That's okay because of reconciliation, because of loops.
[1245.52 → 1247.00] But what is that baseline?
[1247.16 → 1249.16] Like no data, just the declaration.
[1249.52 → 1250.72] Well, yeah, that's the problem today.
[1250.72 → 1259.86] I mean, let's face it, there's no perfect Git Ops solution that includes data right now, which is not to say that, well, let me explain what I mean by this.
[1259.94 → 1262.90] I think there are some amazing data solutions out there, which we can discuss.
[1263.14 → 1267.78] When I say good Git Ops solution, I mean something that has got to the point where it's easy for just about everybody.
[1268.40 → 1274.36] And Git Ops is still breaking slowly out of the Kubernetes world to a world of bigger world of application developers.
[1274.96 → 1277.52] It needs to be as simple as building a web page right now.
[1277.58 → 1278.34] It's not there yet.
[1278.34 → 1286.76] All the techniques that it's based on, like the sort of chefs in the puppet of this world that inspired all these infrastructures code ideas and so on.
[1287.32 → 1291.04] You know, those are more complex, and this is becoming simpler, but it's not there yet.
[1291.12 → 1294.68] But it does basically deal with apps, if you know what you're doing.
[1295.12 → 1296.42] But data is much more challenging.
[1296.54 → 1302.06] Now, we do have some very great technologies like Apple Time Machine, which is based on Polaris.
[1302.26 → 1302.86] What was it called?
[1302.92 → 1304.34] Not zones, but...
[1304.34 → 1304.70] Snapshots.
[1304.70 → 1307.24] The Polaris snapshooting technology, ZFC.
[1307.58 → 1307.94] ZFS.
[1308.14 → 1310.62] The world's most amazing data storage layer.
[1311.04 → 1317.16] And some people I know, even friends of mine, have tried and failed to bring ZFC to the masses a few times.
[1317.44 → 1318.52] It's just not happened yet.
[1318.60 → 1323.34] And I think there are just a few pieces missing that somebody will crack.
[1323.34 → 1326.56] But we'll get to a place where, you know, GitHub has a history.
[1327.24 → 1330.18] Applications can have a history in GitHub or other tools.
[1330.72 → 1331.78] And data will have a history.
[1331.96 → 1338.86] And then you'll be able to bring those histories together sufficiently well to just about recreate your world, which is not the same.
[1339.08 → 1344.58] Let me be clear for people, pedants, not the same as solving any hard computer science problems.
[1345.34 → 1346.70] You know, there will be edge cases.
[1346.80 → 1347.76] We will make mistakes.
[1347.90 → 1348.76] Things will fall out.
[1348.76 → 1351.70] But generally speaking, the business will kind of work around that stuff.
[1352.64 → 1363.04] Git Ops, even though it's still getting there when it comes to data, I think it does a great job at capturing the entire infrastructure as it runs.
[1363.56 → 1367.24] And the tooling improved a lot in recent years.
[1367.40 → 1367.98] I think so.
[1367.98 → 1371.54] When I started looking at it, yeah, the Git Ops CLI didn't exist.
[1371.86 → 1373.18] Now the Git Ops CLI is a thing.
[1373.54 → 1374.68] What is the Git Ops CLI?
[1374.68 → 1377.88] It's the first time I've heard of it in recent weeks.
[1378.38 → 1383.38] But I really like the promise, like especially like the starting with it.
[1383.48 → 1385.44] The Git Ops CLI is part of Weave Git Ops.
[1385.84 → 1389.56] And that's just something we wrapped around Flux.
[1390.00 → 1391.84] And it's our open source project.
[1391.96 → 1393.44] We recommend that you try it out.
[1393.76 → 1396.50] We have some ideas to make it even more exciting in the future.
[1396.50 → 1398.02] But right now it's pretty simple.
[1398.02 → 1407.30] The idea is essentially that Git Ops should just be a very natural part of every developer's workflow for testing, for rolling into production, for going back.
[1407.82 → 1410.26] And this should be firsthand verbs that everyone is familiar with.
[1410.36 → 1411.90] But this has got some time to go yet.
[1412.44 → 1412.60] Okay.
[1413.10 → 1414.88] So it's easy to get started.
[1415.16 → 1416.46] The two commands, that's great.
[1416.58 → 1418.22] Like start with Git Ops and two commands.
[1418.48 → 1419.82] I really like that story.
[1420.08 → 1423.68] The getting started obviously needs to be simple for anyone to even consider trying it.
[1423.76 → 1425.02] Because like, why would I?
[1425.02 → 1427.42] What are the benefits to using Git Ops?
[1428.02 → 1430.94] For those that are still thinking, like, should I use Git Ops?
[1431.04 → 1431.74] Do I do Git Ops?
[1431.86 → 1433.72] Like, what are the benefits of Git Ops?
[1434.18 → 1436.58] Well, that's a perfect question.
[1437.36 → 1446.78] One of the key benefits is that it automates a lot of steps that you would do manually when it comes to deploying and managing your stack.
[1446.78 → 1456.34] If you want to deploy lots of components into Kubernetes, several different Git Ops technologies, including Flux and Weave Git Ops, but others as well, will work in this way.
[1456.34 → 1458.36] They will run an agent inside Kubernetes.
[1458.84 → 1460.42] In fact, you can do it without an agent too.
[1460.48 → 1462.58] But the agent example is the simplest to explain.
[1463.10 → 1466.70] They run an agent in Kubernetes, which is aware of potential updates.
[1467.36 → 1470.88] And then when it seems that a potential update is available, it will deploy it.
[1470.88 → 1477.78] And that particular mechanism is what we call pull, which is, again, something that has been done before Kubernetes came along.
[1477.92 → 1479.50] It was an earlier idea.
[1479.50 → 1483.28] But it's nice because it has properties like security.
[1483.28 → 1493.26] It can inherit all the Kubernetes security and lifecycle and operational capabilities, which just by being embedded inside Kubernetes and living inside it.
[1493.26 → 1502.40] It can also see all the current Kubernetes state securely, which allows it to compare the current running state with the intended state without breaking security.
[1502.40 → 1508.70] And that means that you can observe whether a cluster is in the right state or not without breaking security, which is very nice.
[1509.16 → 1511.56] Another property is that it scales.
[1511.80 → 1515.98] So this is something that you would be aware of if you had done previous work in Pub Sub.
[1515.98 → 1530.72] But as you add more and more and more copies of a source of information, it becomes more scalable to pull changes asynchronously than to try and push them all at the same time to the listeners on the remote clients.
[1531.20 → 1533.80] That's because some of them get there at different rates.
[1533.90 → 1535.06] Some of them don't get there.
[1535.52 → 1537.76] Some of them may not be ready and other reasons as well.
[1537.76 → 1546.86] So this matters when, for example, you have the use case like a telecommunications company where the Kubernetes clusters are running in the mobile phone towers.
[1547.46 → 1550.04] And you might have three machines running a few clusters.
[1550.20 → 1554.42] Or another example is restaurants where they have Kubernetes clusters in the restaurant.
[1554.60 → 1555.72] Believe me, this is true today.
[1556.16 → 1558.78] Or airplanes where there's a Kubernetes cluster in the airplane.
[1558.78 → 1567.40] And so all of these things are connected back to a centralized controller or HQ where the decisions are being made.
[1567.54 → 1575.46] And once a decision is being made, it will be virtually pushed out virtual synchrony out to the remote clusters, in this case in the telco towers.
[1575.76 → 1578.04] But the actual changes will be pulled in.
[1578.56 → 1579.32] And this matters.
[1579.50 → 1583.72] The scalability matters when you have thousands of these things, which you do in this case.
[1583.96 → 1586.66] So this is about taking Kubernetes to the edge scalably.
[1586.66 → 1590.10] Another thing is that nobody touched the cluster.
[1590.58 → 1592.68] And yet you have thousands of identical clusters.
[1592.86 → 1594.38] Or they can be different if you want them to be.
[1594.68 → 1599.78] So you can have complete management of a huge fleet across a geographical area, all in software.
[1600.10 → 1606.10] Which means that now you can take something like the telco infrastructure, which is upgrading to fast comes like 5G.
[1606.34 → 1608.26] And that could become an extension to the cloud.
[1608.60 → 1610.26] So that's like a mind-blowing event.
[1610.38 → 1614.94] That could be one of the key steps towards the iPhone moment for cloud-native apps.
[1614.94 → 1626.34] When we have an always connected set of nodes that form a single virtual cloud infrastructure, we'll be able to run apps wherever we want to, whenever we want to, that do whatever we want to.
[1626.86 → 1627.98] And that's pretty cool as well.
[1628.10 → 1630.00] So I think all of those things come from Git Ops.
[1630.00 → 1635.12] But then there's even really basic things like, do you know what state your cluster is in?
[1635.48 → 1636.66] Yes, you do with Git Ops.
[1636.76 → 1637.24] It's great.
[1637.38 → 1642.48] So in the example of Alexis and Gerhard, each start a Kubernetes cluster, and we wait a couple of days.
[1642.48 → 1644.22] We can check if we're in the same state.
[1644.88 → 1647.94] So I have a less mind-blowing example.
[1648.56 → 1653.28] But real, real world, this is like my own experience when it comes to the changelog infrastructure.
[1653.58 → 1653.82] Great.
[1653.82 → 1656.06] So you're listening to this podcast.
[1656.34 → 1659.14] It's being streamed from a Kubernetes cluster.
[1659.24 → 1659.52] Hooray.
[1659.84 → 1672.36] And that Kubernetes cluster, when it was configured, even though it does use a pool-based model when it comes to updating itself, it's not using the Git Ops tool that you'd be familiar with, like Flux or Argo.
[1672.46 → 1673.94] It's using something called Keyless.
[1673.94 → 1680.30] Now, even though that does something completely different, and we're always running on latest, which is very dangerous.
[1680.58 → 1684.54] Anyone doing GitHub say, no, never run latest because you don't know what latest means and it changes.
[1684.66 → 1685.80] And we even had issues with that.
[1686.00 → 1696.10] But the one thing that worked really well is the CI, CD system, whatever that may be, not having the keys to production, not knowing even where production is.
[1696.10 → 1703.82] The CI, CD system stops, like after it produces an image, it publishes it to a registry of images, Docker Hub in our case.
[1704.24 → 1708.02] And there's this component which continuously keeps watching that image.
[1708.16 → 1709.46] When is the latest image?
[1709.56 → 1710.58] When it has been updated.
[1711.38 → 1718.74] And the properties of this, besides security, which you mentioned, which is a big one for many, is that you can run multiple Kubernetes clusters.
[1719.30 → 1722.16] And all you have to tell it is, like, just pull from latest.
[1722.34 → 1723.26] That's all you have to do.
[1723.40 → 1724.58] And that applies to everything.
[1724.58 → 1734.10] So I think we're about 80% there, but I never really completed the 20% to go to Flux or Argo or something like that, which I really want to do.
[1734.32 → 1735.76] Because I see the benefits of that.
[1735.84 → 1739.52] And we have been experiencing those benefits for about two years now.
[1739.66 → 1740.40] And it's great.
[1740.70 → 1742.42] Like, pull-based for deployments is great.
[1742.82 → 1744.20] Well, there are a few things we need to add.
[1744.40 → 1745.56] Like, you mentioned compliance.
[1745.80 → 1750.94] So the App Store has a model where, you know, whether it's Apple or somebody else,
[1750.94 → 1757.40] somebody will certify that once an artifact is in the store, it meets some quality assurance.
[1758.04 → 1759.26] At least that's the idea.
[1759.38 → 1760.24] It's not always true.
[1760.24 → 1765.48] But you don't always want to push changes to your telco towers unless somebody has vetted them.
[1765.70 → 1771.84] So the next phase, which I don't think is part of the sort of standard definition of Git Ops, is to fully integrate policy and compliance into this.
[1771.84 → 1774.68] So that we can have a concept of trusted delivery.
[1775.18 → 1782.80] And that includes the classic, the buzzword of the day, supply chain, signing your artifacts, a check provenance, a test station.
[1783.22 → 1785.68] All the cool new scanning tools can be part of this.
[1786.20 → 1788.46] Things like linting, things like static analysis.
[1788.70 → 1789.98] There are so many different examples.
[1790.54 → 1793.68] But fundamentally, you're saying, I get something from a safe place.
[1793.68 → 1798.02] I move it through a sequence of safe places safely, and I get it out to the right place safely.
[1798.70 → 1802.54] And that, I think, is really critical for the App Store as well, as well as what you're saying.
[1803.02 → 1809.12] How does the Git Ops model fit with the CI-CD, the continuous delivery pipeline specifically model?
[1809.48 → 1814.44] Because the pipeline, the one that delivers into production, I mean, the last step is, right?
[1814.58 → 1816.20] I deliver this, and this is running.
[1816.54 → 1818.36] But the Git Ops model changed that slightly.
[1818.60 → 1819.60] What does that change look like?
[1819.84 → 1822.46] You still do pipelines, but they work in a slightly different way.
[1822.46 → 1824.30] So we talk about Git Ops pipelines as well.
[1824.88 → 1831.12] So the basic example is, I have a CI tool which does some things, and then I'm ready to do a deployment.
[1831.66 → 1835.10] In the old days, my CI tool would run scripts to do that deployment.
[1835.56 → 1837.72] And that's okay with small-scale, simple steps.
[1837.82 → 1848.16] But when you've got more than a few things happening, if one of the steps fails, the CI tool basically has to replay the whole update in order to get your update done correctly.
[1848.16 → 1854.56] With Git Ops, the CI tool is not responsible for the last step of the actual update of the cluster.
[1854.80 → 1867.68] It is responsible for presenting artifacts and changes ready for deployment in repos that contain immutable artifacts, which we call the immutability firewall, or DMZ.
[1867.68 → 1876.76] From that immutability zone, the agents in the cluster can see the available new things and selectively pull them in and deploy them.
[1877.14 → 1885.94] And then Kubernetes, because it's a conversion orchestrator, will usually get the system into the right state with the help of the agent, which in our case is Flux.
[1885.94 → 1891.82] And that means that your pipeline now includes something that's running inside the cluster.
[1892.24 → 1895.20] And the last mile is a pull rather than a push.
[1895.30 → 1899.22] Now, again, I want to state very clearly there are variations on this pattern.
[1899.52 → 1907.10] So you can do the whole thing as 100% push, but the last mechanism is making some changes because it includes the cluster.
[1907.48 → 1908.98] And that has to be done securely.
[1909.36 → 1913.24] The second example is one where staging is involved.
[1913.24 → 1915.78] And this can be done in many, many, many different ways.
[1916.36 → 1920.66] So one way would be to have an actual persistent staging cluster.
[1921.22 → 1925.42] So we push candidate changes into the staging cluster.
[1925.98 → 1926.88] We inspect them.
[1927.08 → 1930.42] And then we once again do some more CI work.
[1930.46 → 1932.00] And then we push changes into production.
[1932.42 → 1936.26] Or we can do things where we have a stage release.
[1936.56 → 1939.28] So we push changes into production and then do a canary.
[1939.28 → 1942.02] And the CI tool continues to play a role.
[1942.60 → 1944.34] For example, observing the canary.
[1944.34 → 1952.40] The only difference with Git Ops is just like in my first example, the CI tool will interact with agents running inside the cluster.
[1952.92 → 1958.34] Now, in the case of a canary, it's going to interact with a tool called Flagger, which is something that manages a canary rollout.
[1958.34 → 1966.62] But it's just the same idea, except you replace a few scripts with agents running in the cluster is the basic change.
[1966.92 → 1968.52] How does the pipeline interact with a canary?
[1968.62 → 1970.16] How does it know what a canary does?
[1970.32 → 1972.06] I mean, it can't be synchronous, right?
[1972.06 → 1978.68] In the case of Flagger, it outputs to Prometheus according to configurable Los.
[1978.88 → 1979.14] Okay.
[1979.30 → 1986.32] So you can basically tell it, hey, push this canary out another 5% unless this metric is over this number.
[1986.70 → 1989.22] And then that interacts with external systems.
[1989.44 → 1998.50] So if you want to hook that up to your CI, the CI can sit there waiting, watching for metrics coming out of the Prometheus channel to show you what's going on.
[1998.50 → 2000.12] So there are all kinds of things you can do.
[2011.62 → 2012.36] What's up, friends?
[2012.42 → 2018.08] This episode is brought to you by our friends at Retool, the local platform for developers to build internal tools.
[2018.44 → 2020.14] Some of the best teams out there trust Retool.
[2020.54 → 2027.28] Bred, Coinbase, Plaid, DoorDash, Legal Genius, Amazon, All birds, Peloton, and so many more.
[2027.28 → 2031.66] The developers at these teams trust Retool as a platform to build their internal tools.
[2031.84 → 2032.84] And that means you can too.
[2033.22 → 2033.94] It's free to try.
[2034.06 → 2035.94] So head to retool.com slash changelog.
[2036.08 → 2039.04] Again, retool.com slash changelog.
[2055.12 → 2057.06] What about the CI pipeline?
[2057.28 → 2064.12] And in this case, a CI is more like a CI CD pipeline because even though it doesn't do CD, it observes a component that does the deployment.
[2065.00 → 2073.08] What happens if, for example, Flux, because I imagine that's the tool which in this case updates what's running in the cluster.
[2073.52 → 2074.58] What if it can't do that?
[2074.66 → 2076.10] Maybe there's no sufficient resources.
[2076.38 → 2078.34] Maybe some compliance has failed.
[2078.34 → 2082.36] How does Flux communicate that back to the CI CD pipeline?
[2082.36 → 2093.48] So there is a write-back mechanism which people have been putting into Git Ops tools, which helps them to use essentially privileged channels so they can communicate flags back.
[2093.48 → 2097.78] There is, I can't tell you exactly what level of support there is for different things.
[2098.20 → 2110.88] What I can also tell you is that we have GUI tools which allow you to look at a difference between what's in the running state and what is in the intended state, which means that you can then see if things are in the state you want them to be.
[2110.88 → 2113.52] And that allows you to see if a job is completed.
[2113.72 → 2115.60] This is an area of active work.
[2116.18 → 2116.70] I see what you mean.
[2116.78 → 2117.40] Okay, okay.
[2117.46 → 2118.06] That makes sense.
[2118.42 → 2122.10] So I'd like to shift a little because we talked a lot about Git Ops.
[2122.40 → 2129.62] But one very important thing is when you try to gauge how far down the Git Ops model you are is the maturity model.
[2129.66 → 2129.84] Yeah.
[2129.96 → 2130.98] What can you tell us about that?
[2131.28 → 2134.98] So the maturity model is also in the slides that I gave at the Git Ops come.
[2135.06 → 2136.48] I talked about the Enterprise App Store.
[2136.48 → 2139.46] And so there are a few layers.
[2139.78 → 2152.06] The most advanced layer is what we call scaled Git Ops, which was when you think about your whole fleet as potentially a single entity, just like you think about a data centre as a single group of computers.
[2152.68 → 2159.18] And you have capability and abstractions and tools to manage rollouts and policy across the whole fleet.
[2159.84 → 2161.60] That's pretty amazing.
[2161.78 → 2165.48] And there are some companies out there doing that today with proprietary tools.
[2165.48 → 2167.00] And that's like level four, right?
[2167.02 → 2170.96] That's like the highest level on the Git Ops maturity model.
[2171.12 → 2171.20] Okay.
[2171.46 → 2187.52] The next one, which I think most of our customers are trying to get to, is what we call Enterprise Git Ops, which is when you've got config management at the infrastructure cluster app layer, the main layers of the stack, and quite a few pieces of the workflow as well.
[2187.52 → 2200.48] That already just has such enormous cost savings and such boosts in developer productivity and operational metrics that for many people, it's just the goal, especially if they're sort of in a hybrid or multi-cloud environment or something like that.
[2200.80 → 2203.42] Then there's the – and those both for us are commercial customers.
[2203.42 → 2209.70] The other two layers are what we call prerequisites and call Git Ops.
[2209.94 → 2213.68] So prerequisites is when you're basically doing Git but no Ops.
[2214.20 → 2216.20] So this is what people like GitLab call Git Ops.
[2216.34 → 2228.90] So essentially, they've got all kinds of runners or, in the case of GitHub, GitHub Actions would be doing exciting and important workflows around Git, which could be part of an installation or a deployment.
[2228.90 → 2231.40] But they don't actually do anything operational.
[2231.60 → 2238.96] They don't actually sit there inside the cluster continually verifying that it's in the correct state and correcting it if it drifts.
[2239.52 → 2241.28] They don't do things like manage canaries.
[2241.68 → 2243.50] They don't do things across clusters.
[2243.90 → 2245.54] It's very, very basic stuff.
[2245.70 → 2247.50] That is, for many people, the entry level.
[2247.96 → 2248.90] It's a good thing to do.
[2249.36 → 2252.16] The next level up is what we call core Git Ops.
[2252.16 → 2258.60] That's when you're basically aligned with the precepts of what the Git Ops working group has published.
[2258.74 → 2260.02] It's very basic stuff.
[2260.52 → 2267.74] It just says you have continuous reconciliation based on a plan in a shared mutual store, version-controlled store, sorry.
[2268.10 → 2275.64] And this is almost identical to the methodology pioneered by Chef and Puppet, except that it's easier to use now.
[2275.76 → 2278.30] You can apply it to more things all up and down the stack.
[2278.30 → 2280.72] There's less scripting involved.
[2280.86 → 2281.82] It's more programmatic.
[2282.12 → 2283.46] It's easier, blah, blah, blah, blah, blah.
[2283.84 → 2287.14] So just to recap, you've got your prerequisites, which is Git workflows.
[2287.42 → 2291.86] If you're just doing Git workflows, you're not doing Git Ops because you need to be doing ops.
[2292.10 → 2297.06] If you do core Git Ops, you're adding the operational loop, which means that you now have automation.
[2297.68 → 2299.02] The system looks after itself.
[2299.20 → 2300.92] Then you add enterprise Git Ops.
[2301.04 → 2302.00] You add more clusters.
[2302.30 → 2303.46] You move up and down the stack.
[2303.92 → 2307.42] You start encoding things like policy as code, platform as code into it.
[2307.42 → 2317.06] And then finally, at scale Git Ops, which is when you stop even thinking about individual computers and systems and actually look at the whole holistic problem.
[2317.62 → 2317.66] Yeah.
[2318.04 → 2321.30] Even like clusters, like at that point, clusters are just like a resource.
[2321.88 → 2323.16] It's not about like your app.
[2323.24 → 2323.36] Yeah.
[2323.56 → 2324.06] Yeah.
[2324.06 → 2325.42] That is a very exciting world.
[2325.52 → 2328.94] That is the castle in the sky that you were referring to earlier.
[2328.94 → 2336.50] Well, the castle in the sky for me is actually the enterprise app store because I still think that for some of the reasons you mentioned, enterprise apps are distributed apps.
[2336.50 → 2338.14] It may have multiple services.
[2338.26 → 2339.76] Some of them aren't used by people.
[2339.86 → 2340.40] They're services.
[2340.96 → 2342.24] Some of them have complex states.
[2342.38 → 2344.14] Some of them have weird identity.
[2344.74 → 2352.66] All of those reasons mean that, you know, the enterprise app store is always going to be different from the lovely consumer, one app, one person, one phone experience.
[2353.18 → 2355.62] But it doesn't mean we can't strive to get that.
[2355.84 → 2356.54] It's a utopia.
[2357.04 → 2357.16] Right.
[2357.16 → 2361.22] Well, everything starts as a crazy idea until it stops being one, right?
[2361.66 → 2364.42] Someone that you and me know said that once.
[2364.86 → 2369.74] So first, your GitOpsCon North America talk, the 10-minute one, I watched it.
[2369.80 → 2370.24] It's great.
[2370.38 → 2373.42] That is a great summary of what we have discussed here.
[2373.60 → 2378.78] There was also Git Ops Days 2021 in June, and there were a couple of perfect talks.
[2379.14 → 2382.08] The one around the Git Ops maturity model, that was a great one.
[2382.08 → 2388.86] There was the inflection point, I think, Git Ops has reached an inflection point, something like that, that Cornelia gave.
[2389.14 → 2393.28] So there are a couple of good talks at that conference, which we will link in the show notes below.
[2393.52 → 2396.84] How was your Git Ops Days 2021 experience for you?
[2397.36 → 2397.76] Spectacular.
[2398.26 → 2400.26] I mean, I'm really proud of what the team pulled off.
[2400.40 → 2401.80] Let me just describe it to you.
[2401.86 → 2402.66] It's quite something.
[2403.14 → 2407.00] We're, I think, a reasonably well-known company at this point, but we're not a big company, okay?
[2407.00 → 2419.18] Yet, our very small, very motivated, very talented team who works constantly with our customers and partners was able not only to get a great set of real-world use case tools, but also, check it out.
[2419.26 → 2433.22] They got a representative of Amazon and Microsoft Azure and VMware and Red Hat and Mesosphere, now D2IQ, to all stand up in one place at one time and say, we're using Git Ops in production in our systems.
[2433.22 → 2440.56] And they all gave Flux demos because they're all using Flux, except Red Hat, which is using Argo, and a little bit of Flux on the side for some of its customers.
[2440.98 → 2441.94] That was amazing.
[2442.58 → 2445.18] And another one is Alibaba that spoke at the previous conference.
[2445.96 → 2451.84] So, you know, if you're listening in and thinking, oh, this sounds a little bit of sci-fi to me, it's going to take a few more years to land.
[2452.22 → 2455.52] Trust me, these people are all doing it for you already.
[2455.52 → 2464.60] And, you know, it's worth finding out about because this is going to be how we operate a lot of systems in the future at scale.
[2465.38 → 2469.14] I do regard you as a bit of an innovator when it comes to a few things.
[2469.38 → 2470.74] I think Git Ops is one of them.
[2471.06 → 2473.78] I think in 2019, it may have sounded as an innovation.
[2474.18 → 2475.98] Like, what is this Git Ops thing?
[2476.36 → 2481.60] I think at this point, we're like early adopters, maybe even slightly beyond that point.
[2481.60 → 2487.98] And that's why I brought this conference up, because there were some like real world use cases of how Git Ops is being used.
[2488.32 → 2492.32] And it's not so, as you mentioned, a pie in the sky.
[2492.46 → 2493.66] It's not a pie in the sky anymore.
[2493.82 → 2495.22] Some ideas may be, but not this.
[2495.32 → 2496.80] Like, people are using it and it works.
[2497.24 → 2502.60] And with that in mind, I'm wondering, what is coming in the next six months for the world of Git Ops?
[2503.08 → 2504.52] Well, good question.
[2505.06 → 2507.30] So we've touched on most of the things.
[2507.60 → 2509.96] Git Ops on the edge is becoming more and more common.
[2509.96 → 2512.10] I'm seeing a lot of retail stores.
[2512.32 → 2515.94] The United States Air Force has a beautiful use case on the CNTF website.
[2516.18 → 2520.52] So before a fighter jet takes off, it reloads its Kubernetes using Flux.
[2521.08 → 2521.78] No way.
[2522.30 → 2522.72] Seriously?
[2522.90 → 2523.74] Like the F-35?
[2524.08 → 2525.38] I don't know which planes, honestly.
[2526.32 → 2529.80] If you read the use case, you'll see that this is not a joke.
[2529.92 → 2538.22] This is part of their Platform 1 software platform for secure management of containers in real assets.
[2538.22 → 2538.74] Wow.
[2539.34 → 2540.06] That is impressive.
[2540.36 → 2552.22] Same day, there was a presentation on the Git Ops days, lovely presentation from Ricardo at CERN, who manages an extraordinarily large and very heterogeneous infrastructure, talking about how Git Ops has basically made it all possible.
[2552.22 → 2555.68] I should add that Ricardo has young children.
[2556.30 → 2559.10] So he's managing to do his job and sleep at night.
[2559.90 → 2560.30] Okay.
[2560.70 → 2561.82] This is really important.
[2562.20 → 2563.70] You know, you don't want to be woken up in the night.
[2563.86 → 2564.56] Git Ops can help.
[2564.68 → 2568.52] We had a customer who just rolled out 5G with Git Ops.
[2568.62 → 2570.52] There's going to be a press release next week about that.
[2571.16 → 2572.56] Everyone's super excited about that.
[2572.60 → 2574.58] And it's already doing HA, which is pretty cool.
[2574.90 → 2578.96] By the time you're listening to this, by the way, which will be end of December, that will
[2578.96 → 2579.52] already be out.
[2579.52 → 2582.00] So we'll link it in the show notes before we publish.
[2582.32 → 2582.42] Yeah.
[2582.48 → 2584.36] All of those are kind of quite big scale things.
[2584.44 → 2588.26] So those are what's coming is more real world cases, more edge.
[2588.76 → 2593.74] And then I think we're going to see a lot of work around the deployment pipelines, not just
[2593.74 → 2598.40] in the Git world of Git Ops, but of course, also in the CCD world as well.
[2598.90 → 2600.64] DevOps and Git Ops are becoming secure.
[2600.94 → 2602.84] They are becoming policy integrated.
[2602.84 → 2612.60] They're becoming ways to get code and assets into production wherever you want with 100%
[2612.60 → 2614.38] attestation along the way.
[2614.50 → 2615.40] That's the future.
[2616.22 → 2620.30] And then, of course, fleets and platforms, the different ways to scale are going to be
[2620.30 → 2620.90] very important.
[2621.34 → 2626.14] And all of these things are being sort of unlocked like levels of a computer game by just continuing
[2626.14 → 2627.38] in the same direction.
[2627.38 → 2628.12] That's amazing.
[2628.30 → 2632.62] And all this while Christmas is happening and all this while like all like the life
[2632.62 → 2633.12] is happening.
[2633.34 → 2638.44] So there's like a nice progression to these big things happening while, you know, carry
[2638.44 → 2639.02] on as normal.
[2639.54 → 2640.22] Everything's fine.
[2640.52 → 2640.84] All right.
[2640.92 → 2641.46] Keep calm.
[2641.46 → 2646.56] So as we are preparing to wrap up, I'd like us to summarize this for our listeners.
[2647.16 → 2650.58] What would you say is the most important takeaway from this conversation?
[2650.90 → 2654.70] I'd say that you should be not scared to try out these new technologies.
[2655.30 → 2661.42] We've got, you know, a Git Ops demo running on GitHub Code spaces with a GUI that you can use
[2661.42 → 2662.88] right away that I would recommend.
[2663.20 → 2666.32] You're welcome to contact me personally if you can't find it.
[2666.42 → 2670.92] I'm Monad on Twitter and Alexis at weave. Works is my email address.
[2670.92 → 2677.96] Within an enterprise organization, if you're using Kubernetes and you want to help scale
[2677.96 → 2682.72] or you're worried about onboarding applications, talk to me because that's something that is
[2682.72 → 2684.30] a lot easier than you may have thought.
[2684.66 → 2689.76] Same for multi-cloud, same for integrating secure DevOps into the tool chain, all of that
[2689.76 → 2690.06] stuff.
[2690.16 → 2694.56] I think it's, you know, very much kind of happening and happy to help anybody with their
[2694.56 → 2695.28] problems around it.
[2695.28 → 2700.06] My most important takeaway is that I've been sleeping and the wheel for too long and it
[2700.06 → 2703.74] is time to get properly into Git Ops and try this out.
[2704.06 → 2707.04] I will do exactly as you said, reach out if I get stuck.
[2707.14 → 2708.14] So thank you very much for that.
[2708.26 → 2709.12] That's super helpful.
[2709.44 → 2711.36] And I'm really excited about 2022.
[2711.82 → 2716.72] What we will do for changelog with Git Ops, as well as see what others will do for their
[2716.72 → 2718.06] real world applications.
[2718.06 → 2721.46] I mean, if the Air Force can do it, I think we can do it.
[2721.72 → 2722.98] Indeed, indeed, indeed.
[2723.08 → 2724.26] That's the way I'm thinking about it.
[2724.56 → 2725.34] This has been a pleasure.
[2725.62 → 2726.48] Thank you very much, Alexis.
[2726.78 → 2728.00] And looking forward to the next one.
[2728.16 → 2728.54] Take care.
[2731.84 → 2734.22] Thank you for tuning in to another episode of Ship It.
[2734.48 → 2737.06] This is just one of our podcasts for developers.
[2737.46 → 2740.76] Go to changelog.com forward slash master for the rest.
[2740.76 → 2744.88] You can join us via changelog.com forward slash community for free.
[2745.36 → 2749.48] Only cost is happiness credits if you choose to not interact with us.
[2749.94 → 2751.50] There are no imposters in our Slack.
[2751.90 → 2753.00] Everyone is welcome.
[2753.54 → 2757.20] Huge thanks to our partners Vastly, Launch Darkly and Len over.
[2757.78 → 2760.84] Thank you, Break master Cylinder for all our awesome beats.
[2761.30 → 2762.30] That's it for this week.
[2762.58 → 2763.38] See you next week.
[2763.84 → 2765.16] Actually, there's one more thing.
[2765.60 → 2769.76] Today, as I record this, is my first day with a new team of amazing people.
[2769.76 → 2772.12] And I'm super excited about this new venture.
[2772.62 → 2774.36] I wish the same feeling for you.
[2774.82 → 2775.66] My last thought.
[2776.20 → 2781.58] Resilient teams are made up of individuals that offer to share everything that they're learning.
[2782.04 → 2784.80] They see the whole landscape and ship obsessively.
[2785.26 → 2786.24] Don't finish it.
[2786.46 → 2787.16] Just release it.
