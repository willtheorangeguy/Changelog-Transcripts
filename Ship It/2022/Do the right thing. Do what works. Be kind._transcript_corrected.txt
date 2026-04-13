[0.08 → 6.56] I'm Gerhard Lander, and you're listening to Ship It. Show, a podcast about ops, infrastructure,
[7.06 → 8.94] and great ideas executed well.
[9.52 → 15.90] Why are the right values important for a company that changed the way the world built software?
[16.38 → 20.48] How does pair programming help scale and maintain the company culture?
[21.00 → 26.44] And what is it like to grow a company to 3,000 employees over 30 years?
[26.44 → 33.14] Today, we have the privilege of Rob Mee, former CEO of Pivotal, the real home of Cloud Foundry
[33.14 → 34.34] and Concourse CI.
[35.04 → 42.42] Rob is now the CEO of Geometry.io, an incubator where Elixir is behind many great ideas executed
[42.42 → 45.66] well, including the US COVID response program.
[46.18 → 48.62] Big thanks to our partners Vastly and Fly.
[48.88 → 53.46] This MP3 is served with minimal latency from the Vastly edge location, which is closest
[53.46 → 53.90] to you.
[53.90 → 59.14] Our app and database run on Cloud.io because it keeps things simple.
[64.10 → 67.12] This episode is brought to you by Honeycomb.
[67.26 → 69.60] Find your most perplexing application issues.
[69.90 → 76.06] Honeycomb is a fast analysis tool that reveals the truth about every aspect of your application
[76.06 → 76.80] in production.
[77.28 → 81.24] Find out how users experience your code in complex and unpredictable environments.
[81.24 → 86.02] Find patterns and outliers across billions of rows of data and definitively solve your
[86.02 → 86.50] problems.
[86.94 → 88.42] And we use Honeycomb here at Change.
[88.44 → 92.28] That's why we welcome the opportunity to add them as one of our infrastructure partners.
[92.80 → 96.96] In particular, we use Honeycomb to track down CDN issues recently, which we talked about
[96.96 → 100.10] at length on the Kaiden edition of the Ship It podcast.
[100.36 → 101.04] So check that out.
[101.28 → 101.76] Here's the thing.
[101.98 → 105.26] Teams who don't use Honeycomb are forced to find the needle in the haystack.
[105.26 → 108.54] They scroll through endless dashboards playing whack-a-mole.
[108.74 → 111.80] They deal with alert floods, trying to guess which one matters.
[112.18 → 116.46] And they go from tool to tool playing sleuth, trying to figure out how all the puzzle
[116.46 → 117.38] pieces fit together.
[117.74 → 122.04] It's this context switching and tool sprawl that are slowly killing teams effectiveness
[122.04 → 124.06] and ultimately hindering their business.
[124.46 → 130.50] With Honeycomb, you get a fast, unified, and clear understanding of the one thing driving
[130.50 → 131.22] your business.
[131.46 → 131.90] Production.
[132.40 → 134.88] With Honeycomb, you guess less and you know more.
[135.28 → 140.48] Join the swarm and try Honeycomb free today at honeycomb.io slash changelog.
[140.48 → 144.14] Again, honeycomb.io slash changelog.
[149.70 → 153.84] We are going to shift in three, two, one.
[160.50 → 169.02] It's 9 or 6 a.m.
[169.18 → 173.22] And I'm very certain that this will be the one that I will always remember.
[173.86 → 174.60] Welcome, Rob.
[175.10 → 175.70] Thank you.
[176.16 → 176.98] Good to be here, Gerhard.
[177.42 → 183.58] So let's imagine that this is a real stand up between you, me, and our listeners.
[184.42 → 185.42] Would you like to start?
[186.56 → 187.02] Sure.
[187.02 → 193.48] As you probably know, depending on the organization, as standups get bigger, you can't really have
[193.48 → 194.22] everybody speak.
[194.36 → 200.90] You need to do something a little more optimized and ask people to volunteer anything that they
[200.90 → 206.90] have found interesting in what they've done, or perhaps ask for help from their colleagues.
[207.54 → 214.20] And so I guess if I'm going to start, I'd ask you if you have anything interesting to report.
[214.20 → 216.18] I do have something interesting to report.
[216.46 → 222.96] I discovered how our bottle dagger brew gets updated.
[223.12 → 224.32] This is the one in the homebrew core.
[224.66 → 228.60] And I wasn't expecting it for a human to be involved, but it is.
[228.68 → 230.88] I was convinced that our pipeline had covered.
[231.28 → 232.04] Apparently not.
[232.44 → 236.66] So that was something interesting for me because I didn't know how that worked.
[236.74 → 237.44] I made an assumption.
[237.74 → 238.52] It was the wrong one.
[238.52 → 243.18] And interestingly, I discovered that is not what I thought was the case.
[243.52 → 247.70] And all of us believe the same thing because we have a homebrew tab.
[248.16 → 251.98] And that's the one that gets updated, but not homebrew core.
[252.20 → 257.86] So our users, when they install the dagger CLI, they're getting an outdated one because there's
[257.86 → 262.00] a human involved and a human didn't update the last version because we ship every week.
[262.40 → 263.70] So that's something interesting.
[264.36 → 265.28] How about you?
[265.72 → 266.78] Anything interesting to share?
[266.78 → 272.86] No, not related to homebrew or dagger for sure.
[274.64 → 275.04] Right.
[275.64 → 276.04] Yeah.
[276.08 → 278.06] And I'm trying to think if I need help on anything either.
[278.26 → 282.72] And I don't have any help to ask for at the moment.
[283.30 → 284.10] How about you?
[284.36 → 285.48] Or if you're blocked on anything.
[285.96 → 286.92] If you're blocked on anything.
[287.04 → 289.72] Well, I would like to ask Andrea for some help.
[290.58 → 294.34] There's a PR, which is blocked on him and another one on Tonga.
[294.34 → 300.08] So Andrea and Tonga, if you're listening to this, obviously in the future, I'm sure there
[300.08 → 302.50] will be a PR that's blocked on one of you.
[303.16 → 305.68] So can you help me unblock them, please?
[305.94 → 307.92] Because there's nothing else I can do.
[308.64 → 310.28] Also, I'm going on holiday.
[310.54 → 314.88] So everyone, please continue looking after the PRs and issues while I'm away because
[314.88 → 316.44] maintaining duty has been on my mind.
[316.44 → 322.64] So when I'm back, hopefully there won't be tens and tens of them which haven't been closed.
[323.18 → 327.50] But if we've done this maintainer duty correctly, then the load will have been spread.
[327.72 → 328.62] It won't be just me.
[328.96 → 329.62] So let's see.
[329.72 → 330.50] This is a test.
[330.96 → 332.32] How well does it work in practice?
[333.28 → 333.44] Hmm.
[334.04 → 336.38] I wish I could offer you help on that, but I'm afraid I can't.
[337.02 → 338.34] Not well versed enough in dagger.
[338.78 → 339.32] Not a day.
[339.60 → 340.38] Maybe another day.
[341.48 → 343.34] And on that, shall we finger snap?
[343.46 → 344.60] That's obligatory, right?
[344.60 → 347.56] To stand up, it doesn't finish until someone snaps their fingers.
[348.24 → 352.80] Well, snapping fingers or clapping or stretching and clapping seem to be a lot of variations
[352.80 → 353.40] these days.
[353.96 → 355.96] But yes, we can finger snap if you'd like.
[356.14 → 356.44] That'd be a little.
[356.74 → 358.12] I just love the finger snap.
[358.42 → 359.96] It's like so sharp.
[360.04 → 360.86] I'm like, listen to that.
[361.72 → 364.88] That's just like, you know, I know it's something that you don't do often.
[365.52 → 369.80] Clapping, you know, you may enjoy someone's talk, and you may clap, but finger snapping,
[369.94 → 374.58] once you do that, I think that's, that's one of the things which I miss.
[374.60 → 379.02] About the pivotal standups where many people would use to finger snap.
[379.86 → 384.10] And that was like, you know, quite something because you don't normally see people finger
[384.10 → 384.42] snapping.
[385.68 → 393.04] You know, I recently received a bit of swag from a group that it's a fairly large group
[393.04 → 400.54] now of open source government contributors who are sort of crowdsourcing, fixing government
[400.54 → 402.60] software systems in a way.
[402.74 → 407.04] And so the organization, I donated to them some time ago.
[407.04 → 412.50] And so, you know, I'm on, I'm on their list for getting updates and occasionally receiving
[412.50 → 413.48] swag as a thank-you.
[413.54 → 420.28] And I received a coffee mug that had a stretch and clap, and then they had their logo on it.
[420.40 → 426.94] So apparently they identify very strongly with standup and, and the way that they do the
[426.94 → 427.52] end of standup.
[427.60 → 429.26] It was a little bit surprising to me to see that.
[430.22 → 430.98] Stretch and clap.
[431.06 → 432.26] I don't remember the stretch part.
[432.34 → 433.34] I remember the clap part.
[433.34 → 435.82] I think there were some differences between regions.
[436.20 → 436.38] Yeah.
[436.58 → 442.44] I've seen in multiple regions at pivotal and now, you know, companies that have some connection
[442.44 → 445.60] to some overlap, certainly in the communities of these organizations.
[446.04 → 452.46] But this is something that sort of spun out of code for America and, you know, which has
[452.46 → 453.60] lots of overlap with pivotal.
[454.02 → 458.48] But anyway, it's, it's interesting to see some of these practices being as widespread as
[458.48 → 458.82] they are.
[459.18 → 459.30] Yeah.
[459.76 → 462.92] So we've been talking, well, we mentioned pivotal a couple of times.
[463.34 → 467.18] Pivotal was a 30-year journey.
[467.98 → 471.94] And I don't think many know that it grew to become 3000 people.
[472.04 → 476.04] It IPO in 2018 acquired by VMware in 2019.
[476.52 → 481.24] I was part of it briefly, but you were there from the beginning all the way to the end.
[481.74 → 482.56] How was it for you?
[482.66 → 483.78] How was this journey for you?
[483.90 → 484.64] It's a long one.
[485.08 → 486.04] And I'm sure a great one.
[486.04 → 486.44] Yeah.
[486.44 → 487.00] Yeah.
[487.56 → 493.14] Well, I certainly can't complain to have, you know, had the opportunity to do such a
[493.14 → 496.86] journey, such an evolution and watch it go through various phases.
[496.86 → 503.96] Certainly in the 90s, we were a small band of people who, who did projects and then disbanded
[503.96 → 506.68] and travelled the world and came back and did more projects.
[506.68 → 510.50] So sort of early lifestyle business was fantastic.
[510.50 → 516.06] And many, many people starting out looking at starting their own companies ask me about
[516.06 → 517.68] that, and they say, would you recommend that?
[518.34 → 523.06] You know, or do you recommend starting as early as you can and building something and
[523.06 → 524.06] spending all your time working?
[524.14 → 529.34] And I, I think my usual response is that was a very rich and fulfilling time of my life
[529.34 → 536.80] to do perfect work with amazing people on fascinating projects and then not
[536.80 → 538.90] do it and alternate that time.
[538.90 → 546.62] Of course, then in the early 2000s, really settling down and building Pivotal Labs and seeing it
[546.62 → 552.80] grow and become more well-known was incredibly rewarding as well.
[553.54 → 559.76] And then having it, having it be acquired in 2012 and spun out again and turning into Pivotal
[559.76 → 565.90] software and, and, and growing that, you know, to, to eventually go public and build a cloud
[565.90 → 566.66] platform and so on.
[566.66 → 571.10] I, it's an opportunity that, um, I wouldn't have wanted to miss.
[571.88 → 576.40] And, uh, you know, a lot of people have asked me, you know, after it was acquired the first
[576.40 → 581.20] time and then we, we, we spun out and, and, uh, and got much bigger quite quickly.
[581.20 → 588.38] It was certainly much more complex as a, as a business model, complicated, uh, lots of
[588.38 → 595.74] different groups and, and, and, and people who were not necessarily steeped in, in the
[595.74 → 601.86] Pivotal Labs culture and had to, you know, come around to their own relationship with
[601.86 → 606.98] that and, and how we, how we worked and everyone finding their own accommodation and going through
[606.98 → 610.70] a lot of, you know, pains of having, I wouldn't say them called them growing pains, but pains
[610.70 → 616.38] of having a lot of people who did not come from that background being thrust into it and
[616.38 → 620.08] eventually, uh, finding their way into it in a, in a good way.
[620.08 → 625.94] I think it ended up sustaining the culture and maintaining it as we got really quite big from
[625.94 → 626.54] my perspective.
[626.96 → 630.68] And people would ask me, do you wish you'd sort of stopped after you'd been acquired the
[630.68 → 631.16] first time?
[631.32 → 634.76] Because this seems difficult, and it seems really complicated.
[635.02 → 639.94] And I, I, I've always responded, no, I think having had the opportunity to grow a company
[639.94 → 644.60] to that size and go public is something I wouldn't, wouldn't have wanted to miss for sure.
[644.60 → 651.34] Being part of Pivotal made me realize that a company which gets to thousands of employees
[651.34 → 659.14] can successfully combine people, process and technology while staying open source, while
[659.14 → 664.94] being open and transparent about how it does things and being on a healthy growth trajectory.
[665.28 → 670.44] What would you say was the reason behind this success and this good combination of all three
[670.44 → 670.86] elements?
[670.86 → 678.50] I think the, the key to successful growth is really having a very intensive, highly intensive
[678.50 → 683.18] collaboration among all the people that, that, that work at a company.
[683.36 → 689.74] And when I say that I'm, I'm framing it abstractly, but I am primarily talking about our practice
[689.74 → 691.98] of pairing wherever possible.
[692.44 → 697.76] And because you're, you're really asking, how do you keep a consistent culture as you, as
[697.76 → 701.10] you grow and as you get to scale, how does that happen?
[701.68 → 709.06] And we certainly see many companies working on trying to have a corporate culture by doing
[709.06 → 713.98] off sites and activities designed to help people bond together.
[714.52 → 720.74] And it always struck me that, well, if your workplace was oriented around that, why would
[720.74 → 722.02] you need to go somewhere else?
[722.02 → 724.58] In other words, what are you doing at work all day?
[725.14 → 731.98] If you're not bonding and trusting each other and relying on each other and, and, and getting
[731.98 → 738.22] to know each other, you know, sort of as that company community, why do you need to go away
[738.22 → 739.56] and go somewhere else to do that?
[739.62 → 742.48] It seems like work is not that then by implication.
[742.48 → 748.36] And it's not that we're trying to make, you know, work a family or something like that.
[748.42 → 752.92] I've always, I've always kind of felt that notion that sometimes companies will, will
[752.92 → 754.62] put forward felt a little bit false to me.
[754.66 → 758.98] I think people have families and community outside of work too, and they need time to do
[758.98 → 761.12] that, time to focus on that.
[761.56 → 765.70] But when you're out at work, I think really there should be such a level of collaboration
[765.70 → 769.18] that you are bonding, and you are getting to know each other and forming relationships.
[769.18 → 776.42] So having a highly collaborative environment, and in our case, trying as much as we can
[776.42 → 785.00] in all areas to pair means that we're spending the day, any two people who are working on,
[785.10 → 789.26] on a particular problem, they're debating what they're doing.
[789.70 → 795.60] They are using the principles that they have understood from the process that we're using
[795.60 → 803.70] and they're refining them as they go and sort of redesigning and devolving the process and
[803.70 → 806.98] the culture, the way that we work and the way that we interact as they do it.
[807.44 → 810.48] And they're, you know, everyone was certainly encouraged to do that, right?
[810.48 → 815.88] If you're not sort of examining how you work at a meta level as well as working, then you're
[815.88 → 820.12] not really doing it quite right because everything is open for question and everything is open
[820.12 → 822.16] for modification and improvement.
[822.16 → 827.94] And so if you do that all day, instead of doing the work while improving the way that
[827.94 → 832.76] you work intentionally, and then you split up and pair with other people the next day,
[833.10 → 836.90] for example, you're going to carry the improvements with you.
[837.88 → 841.48] And, you know, the changes and the evolution will propagate.
[841.48 → 848.08] And so in a culture like that, in a system like that, the system is somewhat self-correcting
[848.08 → 850.68] and self-propagating.
[851.36 → 859.94] I hate to call it viral at the moment, but it allows people to work and to improve the
[859.94 → 866.58] nature of work and then to share that and then to come back together, having had the feedback
[866.58 → 871.36] from working with others and inform the collaboration that they'd had previously.
[871.36 → 877.92] And so this system sort of really allows people to continue to improve and build on what they've
[877.92 → 878.20] had.
[878.40 → 883.52] The way I experienced that sort of without realizing for quite some time, starting when
[883.52 → 890.04] we had, you know, say 10 people and feeling all the excitement and wonder of doing meaningful
[890.04 → 895.30] projects that were quite difficult with a very small group of people and succeeding beyond
[895.30 → 900.22] expectations and thinking, this is amazing, but it will never work if we had, say, 25 people
[900.22 → 904.92] and then getting to 25 people, and it's better and saying, well, gosh, it would never work
[904.92 → 906.08] with 50 or 100.
[906.28 → 910.28] And then getting to that point and saying, it's actually better than it was when I thought
[910.28 → 910.94] that last time.
[911.54 → 916.90] And after doing that several times, finally, you know, taking a step back myself and going
[916.90 → 919.62] meta and saying, wait a minute, why does this keep working?
[920.04 → 927.50] And realizing that having that kind of system in play allows you to grow and evolve without
[927.50 → 928.64] sacrifice and quality.
[928.76 → 935.94] In fact, if you maintain the discipline of working in a paired environment, then it keeps
[935.94 → 936.52] getting better.
[936.68 → 940.58] And by the way, to answer the other part of your question, you know, around the technology
[940.58 → 947.46] and how that plays into it, I think another interesting aspect of the way that we work and take as
[947.46 → 949.18] an example, test-driven development.
[949.18 → 952.28] And we were looking for feedback at every point of interaction.
[952.42 → 956.92] For example, you know, a pair, two people are giving each other feedback all the time.
[957.32 → 963.02] You know, when you're doing continuous integration and deployment, you find feedback from your
[963.02 → 964.14] CI system.
[964.58 → 965.92] It tells you when you made a mistake.
[966.74 → 974.46] Test-driven development is a wonderfully pure way of sort of doing, call it deep practice,
[974.46 → 975.46] if you will.
[975.46 → 980.46] But you're building something to verify what you're about to build for production.
[981.10 → 985.80] And then if you make a mistake, the computer kindly tells you that's not quite right.
[985.94 → 989.58] And you have a chance to reflect and correct it, submit it again and be corrected.
[989.58 → 995.08] And so if you do that in a highly iterative way, you're allowing the computer to help you
[995.08 → 1001.72] improve at a pace that you wouldn't do normally because the feedback from your mistakes would
[1001.72 → 1003.00] come so much more slowly.
[1003.00 → 1010.68] And so it's much more difficult to incorporate that feedback and absorb it and improve as
[1010.68 → 1012.56] it is when you're doing very rapid iteration.
[1013.68 → 1017.06] And so I think, you know, especially for software engineers, and of course, there are other people
[1017.06 → 1020.34] in the organization other than developers.
[1020.34 → 1027.66] But for them, they're really placed in an almost ideal situation for honing their own craft and
[1027.66 → 1033.18] their own abilities and the process that they use and the culture that they are a part of
[1033.18 → 1035.22] by pairing and test-driving.
[1035.92 → 1044.30] And to me, it's almost a, you know, sort of unique opportunity in the world of work to build
[1044.30 → 1050.24] relationships and evolve a culture and improve a craft all at the same time, all while building
[1050.24 → 1052.56] product in a better way than you could otherwise.
[1053.26 → 1061.80] And to watch that, I mean, coming to an understanding of how profound that is, took me years.
[1061.80 → 1065.96] But eventually I realized what was going on and how powerful it is.
[1067.32 → 1074.12] For me, one of the key moments was when I realized how optimizing for this quick feedback
[1074.12 → 1082.02] and how adapting to change, being present in all the layers made them work so well together.
[1082.38 → 1087.76] So whether it's people, it's when you pair, when you spend time together with, not just
[1087.76 → 1092.10] with your thoughts, but with another being, another human being to validate whether what
[1092.10 → 1093.14] you're thinking is correct.
[1093.56 → 1098.80] Then having the tests to confirm that the implementation is correct.
[1098.80 → 1102.48] Then having a CI that integrates everything together.
[1103.32 → 1109.42] And then I think this is a very important element, a platform that can take that artifact
[1109.42 → 1115.52] and deploy it really quickly and scale it out really quickly and test it in production at
[1115.52 → 1116.02] scale.
[1116.72 → 1124.62] Having all those elements work together well, for me, it was the key to understanding how important
[1124.62 → 1129.42] it is for all the layers to work together for the people, for the organizations, for the
[1129.42 → 1129.86] business.
[1130.24 → 1134.38] Everyone benefited from this integration.
[1135.06 → 1136.46] Yeah, that's extremely well put.
[1137.62 → 1139.70] It's as if I had time to think about this.
[1139.82 → 1140.64] Many, many years.
[1142.12 → 1143.36] That's exactly what happened.
[1143.48 → 1143.64] Yes.
[1143.90 → 1149.20] And being part of different and seeing it from different perspectives, because at Pivotal,
[1149.20 → 1150.18] we used to consult.
[1150.36 → 1152.94] Pivotal Labs used to, I mean, it started as a consultancy.
[1152.94 → 1155.94] And consulting was a big piece of what it did.
[1156.14 → 1161.40] So that allowed us to see how other companies were doing it because we were helping them.
[1161.54 → 1166.70] And whether these were car manufacturers, pharmaceuticals, financial institutions, banks,
[1167.24 → 1169.00] like, you know, big organizations.
[1169.78 → 1174.48] And then we realized that the approach that we have scales up and scales down.
[1174.52 → 1175.20] Even startups.
[1175.60 → 1178.98] I remember us working with startups, you know, delivering food.
[1179.58 → 1182.56] And it worked at all levels extremely well.
[1182.56 → 1183.86] So it's scaled very well.
[1184.22 → 1188.32] Whether it was 10 people, 3,000 or 30,000.
[1189.22 → 1192.92] I think that was the versatility behind what works, basically.
[1193.42 → 1194.44] Discovering what works.
[1195.04 → 1195.18] Yeah.
[1195.32 → 1200.32] And I think the key there is having a self-correcting system and a self-improving system.
[1200.76 → 1205.66] And you can't, it's very difficult to impose a structure like that.
[1205.66 → 1214.84] In order to have a self-improving system at scale, you need to have a lot of freedom at the micro level, right?
[1214.96 → 1219.58] At the person-to-person level for them to be able to improve things.
[1219.58 → 1227.36] So pairing, I know that it is controversial in some cases.
[1227.94 → 1230.40] Anything taken to the extreme is bad.
[1230.82 → 1231.84] Take sun, for example.
[1232.36 → 1233.22] Essential to life.
[1233.68 → 1235.84] In large doses, it will kill you.
[1236.18 → 1236.42] Okay?
[1236.48 → 1237.42] It's just what it is.
[1238.02 → 1248.28] So pairing, I think the extreme that I've heard many people complain about is when teams do it all day, every day, for years and years on end.
[1248.28 → 1250.32] I've been on this spectrum everywhere.
[1250.92 → 1254.40] So like not pairing at all, to pairing all the time.
[1254.54 → 1257.44] In my case, it was, I think, months on end.
[1257.92 → 1259.56] And it's really, really hard.
[1259.84 → 1261.60] Where do you sit on this spectrum?
[1261.60 → 1263.24] Or do you see it as a spectrum?
[1263.56 → 1269.20] Like how do you think of pairing all the time versus maybe when it makes sense?
[1269.82 → 1271.82] I'm closer to the end of the spectrum that's all the time.
[1271.82 → 1279.28] But I want to qualify that by saying that people should view a software development methodology.
[1279.78 → 1281.16] And probably any working methodology.
[1281.36 → 1282.22] It doesn't have to be software.
[1282.80 → 1285.04] But my view on that is that nothing should be sacred.
[1285.62 → 1287.68] You should be able to question everything and analyze it.
[1288.18 → 1290.24] And say, is this actually working for us?
[1290.60 → 1291.92] Day by day, week by week.
[1292.30 → 1295.08] And if it isn't, then you modify it.
[1295.08 → 1301.74] Part of that, of course, is making sure that you're being extremely honest with yourself.
[1302.28 → 1305.50] Because sometimes things like pairing can become very tiring.
[1306.30 → 1307.28] And that can be detrimental.
[1307.66 → 1314.32] But if you stop doing it, you may be losing a lot that's not immediately apparent.
[1314.88 → 1316.34] But will become apparent over time.
[1316.34 → 1325.02] So my view on it is that if I were managing a team or funding a team or advising a team,
[1325.26 → 1328.94] I would push pretty hard for them to pair most of the time.
[1329.32 → 1330.90] The vast majority of the time.
[1331.56 → 1337.62] And the reason for that is, if you just take the one example that we talked about at length just now,
[1338.06 → 1345.32] which is creating and propagating and evolving a culture and method of development and continuous
[1345.32 → 1349.06] improvement there, there's nothing like pairing in order to do that.
[1349.56 → 1355.80] If you want extremely high quality code that doesn't have a lot of bugs, and it's well-designed,
[1356.50 → 1358.10] there's nothing like pairing to do that.
[1358.18 → 1365.26] If you want the team to have an understanding of all the code, there's nothing like pairing
[1365.26 → 1371.58] to share context and share information about a code base and make sure that everyone can
[1371.58 → 1372.98] understand most of the code.
[1372.98 → 1376.70] And when you lose someone, you don't lose the ability to modify a piece of the code.
[1377.06 → 1377.80] There's nothing like that.
[1378.12 → 1380.02] And there's nothing like pairing to ensure that.
[1380.12 → 1387.84] And finally, if you want to raise the skill level of people at a pace that you can't do otherwise,
[1388.10 → 1389.24] there's nothing like pairing.
[1389.40 → 1391.28] So you, and I could keep going.
[1391.42 → 1394.62] There are many, many different layers to what it gets you.
[1395.68 → 1398.98] At some point, it may start to become counterproductive, as you say.
[1398.98 → 1404.50] So if, if people are doing it, and it's, it is intense, it's tiring, you may come to a
[1404.50 → 1409.40] point where some of those things are breaking down, and you've been pairing too long and
[1409.40 → 1412.26] you ought to back off a bit and give people a break.
[1412.64 → 1415.12] So certainly have people, having people say, you know what?
[1415.14 → 1416.50] I don't want to pair today.
[1416.68 → 1417.34] I'm done.
[1418.42 → 1419.84] I can't, I can't do it anymore.
[1419.90 → 1424.26] I need to go and read some technical articles, or I need to go and, you know, work on some design
[1424.26 → 1428.94] or, or, or do some research or just look at the code base and, and noodle around a bit.
[1429.28 → 1430.24] Then they should do that.
[1430.60 → 1434.88] If they find that it's unsupportable, given the kinds of things they have to do in their
[1434.88 → 1440.28] work environment, suppose they have to maintain a system in production, and they have to do
[1440.28 → 1442.90] incident response and get on the phone with people.
[1442.90 → 1444.68] Maybe they need a day to do that.
[1445.26 → 1450.32] And so maybe they're only, they're only pairing, you know, three-quarter time or 80% of the time
[1450.32 → 1450.98] or something like that.
[1450.98 → 1453.26] So I can certainly see that.
[1453.60 → 1458.44] And I know, I know that there, there are plenty of downsides to pairing in terms of how tiring
[1458.44 → 1459.28] it is and so on.
[1459.66 → 1466.32] So maybe the case is when people pair, they, they do shorter days or shorter weeks and that's
[1466.32 → 1467.14] reasonable as well.
[1467.14 → 1467.74] Yeah.
[1467.98 → 1472.24] What I'm hearing is having strong opinions is okay.
[1472.76 → 1480.10] Having the courage to find what works for us, us in this case, meaning your team, your
[1480.10 → 1482.18] context is important.
[1482.56 → 1486.62] And you shouldn't blindly follow something because someone says so or thinks so.
[1487.24 → 1489.32] You need to figure out what works for you.
[1489.36 → 1490.88] And by the way, that is the hard part.
[1491.52 → 1498.14] Many people don't know what they like or what works for them because they're just like in
[1498.14 → 1501.70] a system or part of a system and there's inertia, and they just go with it.
[1501.70 → 1509.68] So having a system that encourages challenging assumptions, figuring out what works and promoting
[1509.68 → 1513.80] the courage to just come forward and say, hey, this isn't working.
[1514.18 → 1515.86] Can we find something better?
[1516.90 → 1518.50] Having that is so important.
[1519.12 → 1520.98] And I know that Pivotal has been very strong on that.
[1521.76 → 1525.34] Courage was a big, big word and a very important one.
[1525.34 → 1530.40] And this was in the Pivotal culture, speaking up, coming forward, having the courage to
[1530.40 → 1531.36] do the right thing.
[1532.06 → 1534.50] And by the way, no one said what the right thing is.
[1535.56 → 1538.00] So that was important.
[1538.36 → 1540.66] But there were a couple others which stuck with me.
[1541.44 → 1542.28] Doing what works.
[1543.04 → 1544.68] Very relevant to what we were discussing.
[1545.32 → 1547.78] My favourite, being kind.
[1548.28 → 1551.14] These are the things that when I think of Pivotal is what I think of.
[1551.14 → 1553.86] And they apply to everything, not just software engineering.
[1554.58 → 1555.96] They stood the test of time.
[1556.06 → 1559.34] And I'm sure going forward, they will not change.
[1560.04 → 1561.18] How do you think of those?
[1561.26 → 1564.72] I think it's values that they used to be called, I think.
[1565.70 → 1566.68] Yeah, values.
[1566.92 → 1573.24] And of course, it was our mission statement to transform how the world builds software.
[1573.94 → 1578.68] You know, the origin story of those is always to me quite entertaining and enlightening.
[1578.68 → 1584.48] I think at the same time, you know, quite a few people have heard this, but I don't know
[1584.48 → 1585.90] if it's widely known.
[1586.54 → 1591.66] But someone that I'd worked with since the early days of Pivotal, Edward Hyatt, who was
[1591.66 → 1600.40] running all of Pivotal Labs at this point, came into my office and shut the door and dramatically
[1600.40 → 1604.68] sort of locked it and said, we need a mission statement and values.
[1604.92 → 1607.16] And I'm not letting you out of here until we have them.
[1607.16 → 1610.24] And I thought at the time, what?
[1610.40 → 1610.92] What are you doing?
[1611.70 → 1615.78] And he knew my feeling on things like writing down values.
[1616.14 → 1622.30] I always imagined, you know, being a developer myself, I'm very suspicious of things like
[1622.30 → 1628.66] that and picture, you know, posters with clouds and doves and, you know, things like integrity
[1628.66 → 1632.28] and honesty written on the posters and plastered on the wall.
[1632.28 → 1640.34] And so we're, you know, a relatively small company, primarily oriented around software
[1640.34 → 1640.86] development.
[1641.82 → 1645.06] You know if we write down a set of values, it's going to backfire.
[1645.16 → 1647.36] People are going to find it inauthentic.
[1647.36 → 1654.00] And Edward said, well, actually, I'm here to tell you that I'm hearing from our software
[1654.00 → 1658.90] developers in particular, that they want to understand what our values are and what our
[1658.90 → 1659.70] mission statement is.
[1659.76 → 1661.12] So I think we actually need them.
[1661.74 → 1666.56] And, you know, a similar time, Edward had told me that the software developers were asking
[1666.56 → 1668.66] for more management at one point.
[1668.66 → 1674.26] So, you know, if your developers are asking you for things like more management or values,
[1674.50 → 1677.30] it's gotten to a point where you need to do something.
[1678.04 → 1683.06] Because like me, they're suspicious and cynical about those kinds of things.
[1683.06 → 1689.20] And they don't take lightly to sort of corporate pablum being thrust upon them.
[1689.20 → 1696.30] So I said, okay, well, why don't we just do what we really think and do what we really
[1696.30 → 1699.10] want if we think it would be palatable?
[1699.36 → 1703.74] I mean, I said, for me, I'd love to change how the world builds software.
[1704.38 → 1704.86] You know that.
[1704.94 → 1706.14] And Edward said, yes, I would too.
[1706.72 → 1707.64] That's what I want to do.
[1707.72 → 1709.20] I said, yeah, but we can't write that down.
[1709.34 → 1710.10] We can't say that.
[1710.16 → 1710.74] That's arrogant.
[1710.90 → 1711.74] That's so ambitious.
[1712.14 → 1713.50] And he said, no, no, no.
[1713.98 → 1714.92] That's a great mission statement.
[1714.98 → 1716.52] Mission statements are supposed to be aspirational.
[1716.62 → 1717.46] Why wouldn't we say that?
[1717.46 → 1720.44] And so after a time, he convinced me that that was the right thing to say.
[1720.58 → 1722.20] And it worked and it stuck.
[1722.80 → 1727.62] And I think we grew into it, I would say, as we got bigger.
[1728.84 → 1734.06] And for the values, that was a really hard one for me.
[1734.52 → 1743.10] But I just sat and said, okay, what really matters to me every day as we work at a meta
[1743.10 → 1743.38] level?
[1743.44 → 1746.36] And I thought, well, the first thing is we've got to do the right thing.
[1746.36 → 1748.08] In other words, we have to be ethical.
[1748.22 → 1749.70] There's just no gray area there.
[1749.88 → 1754.06] We can't bill our clients more than we worked.
[1754.20 → 1759.94] We can't allow any accounting silliness to come into play.
[1760.04 → 1762.86] We cannot be unethical at any time.
[1763.14 → 1764.48] It's just completely unacceptable.
[1764.68 → 1765.88] All right, so let's do the right thing.
[1766.42 → 1770.48] And people, I'm not going to tell them what the right thing is, but I think given the people
[1770.48 → 1771.26] we hire, they will know.
[1771.26 → 1774.02] And the second thing was done what works.
[1774.52 → 1775.50] Well, that was simple.
[1776.20 → 1780.94] That's the basis of everything that we do, the way the methodology works.
[1781.52 → 1784.80] We're trying to constantly do things that work and improve upon that.
[1784.80 → 1790.60] And then the last one was one that I think is difficult in a situation, especially if you're
[1790.60 → 1792.02] doing well in the first two.
[1792.26 → 1798.86] It's pretty easy to think, you know, gosh, if we're always doing things well and being
[1798.86 → 1802.68] righteous while we're doing it, then, you know, we must be pretty darn good.
[1802.68 → 1810.78] And then it's easy to be, I think, contemptuous or impatient or mean.
[1811.08 → 1819.44] So you've got to remind yourself to be kind all the time and not allow yourself to succumb
[1819.44 → 1823.20] to those baser instincts or reactions.
[1824.20 → 1826.08] And so I said, OK, let's be kind.
[1826.28 → 1826.86] And that was it.
[1827.38 → 1828.08] Those three.
[1829.00 → 1831.14] And Edward said, I think those are fantastic.
[1831.14 → 1832.68] Let's ship it.
[1833.58 → 1840.06] And I have to confess, I was terrified that people would think we were being inauthentic
[1840.06 → 1840.88] or something like that.
[1840.98 → 1842.52] And it didn't turn out that way.
[1842.60 → 1844.90] I mean, people really latched onto those.
[1845.10 → 1846.26] You know, they were on swag.
[1846.36 → 1847.84] They were on wireless passwords.
[1847.84 → 1849.98] They were on, you know, everywhere.
[1850.72 → 1851.78] Email signatures.
[1852.16 → 1854.04] People put them all over the place.
[1854.54 → 1855.30] Especially be kind.
[1855.84 → 1856.98] It resonated with people.
[1857.38 → 1858.22] That's what it was.
[1858.22 → 1863.28] You know, people like they secretly wanted that or knew that all along.
[1863.98 → 1867.82] And you're just putting it down and coming, you know, from the top in this case.
[1867.94 → 1868.78] The top leadership.
[1869.40 → 1870.36] Putting these things down.
[1870.40 → 1872.80] People realize, yes, of course, that's exactly what I want to do.
[1873.44 → 1874.62] I want to be kind.
[1874.86 → 1876.34] And I want to do what works.
[1876.48 → 1877.44] I want to keep it simple.
[1877.48 → 1878.56] I want to do all those things.
[1878.82 → 1880.08] So it was so easy.
[1880.08 → 1886.44] And you know what was interesting about that moment is that when we were forced to do it,
[1886.92 → 1890.42] it only took us five minutes to come up with that list.
[1890.54 → 1892.68] And they survived for years.
[1893.50 → 1894.76] I don't think it needs to be hard.
[1895.08 → 1897.06] Like the right things, they don't need to be hard.
[1897.20 → 1898.86] You know, they just either click or don't click.
[1898.98 → 1902.06] Just keep trying until you find the right combination.
[1902.06 → 1907.72] And if you know your people, if you know your team and your organization and how things actually work,
[1908.56 → 1909.92] they should just come instinctively.
[1910.28 → 1913.64] Maybe not every day, because not all of us have good days every day.
[1913.94 → 1916.34] But on a good day, you just feel it.
[1916.44 → 1917.66] And everyone else does too.
[1918.32 → 1919.22] That's the beauty of it.
[1919.50 → 1924.24] And if you have a, I think if you have an environment where people are being honest with each other
[1924.24 → 1927.78] and giving each other a lot of feedback, you know, if you stray from those things,
[1927.82 → 1928.80] people can remind you.
[1928.80 → 1929.24] Right.
[1929.96 → 1932.24] And they feel empowered to do so.
[1947.76 → 1951.20] This episode is brought to you by our friends at Acuity,
[1951.44 → 1957.30] a new platform that brings fully managed Argo CD and enterprise services to the cloud or on-premise.
[1957.30 → 1962.44] And I'm here with two of the co-founders from Acuity, Jesse Seen and Alexander Matrusenchev.
[1962.68 → 1965.26] So the Acuity platform is in beta right now.
[1965.48 → 1969.74] You guys have some big ideas you're executing on around Argo CD, managed Argo CD,
[1970.04 → 1972.88] Kubernetes native application delivery, and the power of Git Ops.
[1972.94 → 1975.80] Help me understand the what and the why of what you're doing right now.
[1976.14 → 1981.22] So we started Acuity because we saw what was happening in the Kubernetes community,
[1981.46 → 1985.14] the challenges that people were facing about developer experience.
[1985.14 → 1988.98] And having run Argo CD for Intuit for a couple of years,
[1989.18 → 1995.26] we knew it took like a small team to build this and scale it and provide a performant solution for the developers.
[1995.76 → 1999.40] And so at Acuity, in the QB platform, what we're trying to do is,
[1999.58 → 2005.50] the first thing we're trying to do is actually provide Argo CD as a fully managed solution to our users.
[2005.74 → 2008.02] But that is just actually the start of things.
[2008.02 → 2014.02] And we actually want to take the next steps on improving the whole Git Ops and developer experience
[2014.54 → 2019.00] and providing new tools and ecosystems around Argo and the Argo project.
[2019.30 → 2020.10] Yeah, that's right, JC.
[2020.26 → 2021.94] So Argo CD is just the beginning,
[2022.32 → 2027.70] but every company eventually needs way more tools integrated into the DevOps platform.
[2028.16 → 2030.84] And that's what we're hoping to deliver with Acuity platform.
[2030.84 → 2038.32] So we're hoping to provide a great user interface that enables developers to achieve what they need in a matter of just a few clicks.
[2038.74 → 2041.62] But we also want to make Argo CD enterprise-ready.
[2042.06 → 2050.66] What that means is our customers will get audits and insightful analytics out of the box without configuring anything.
[2051.12 → 2054.72] That's what we did at Intuit, and we learned that it was not so easy to do.
[2055.02 → 2057.90] And that's what we're hoping to solve for multiple organizations.
[2058.30 → 2059.28] Very cool. Thank you, Jesse.
[2059.28 → 2060.16] Thank you, Alex.
[2060.28 → 2063.28] Again, listeners, this is a closed beta.
[2063.62 → 2064.24] Check it out.
[2064.46 → 2067.04] Acuity.io slash changelog.
[2067.14 → 2070.00] Head there and see what this platform is all about.
[2070.32 → 2072.68] Again, Acuity.io slash changelog.
[2072.82 → 2074.38] Links are in the show notes.
[2086.56 → 2087.56] Did it work?
[2088.12 → 2089.06] Did it change?
[2089.28 → 2090.28] The world build software.
[2090.28 → 2092.92] You know, I think in a way we did.
[2093.38 → 2094.64] Maybe not the whole world.
[2095.20 → 2100.70] But I think we were a part of something that did change the way that the world builds software.
[2100.70 → 2122.72] If you look back 20, 25 years ago, there was a tremendous amount of resistance to doing things incrementally, having a lot of feedback, even things like testing software or, you know, all the kinds of things that get grouped under, you know, sort of the agile term.
[2122.72 → 2129.26] And these days, you know, I sometimes find myself going through lots of job ads.
[2129.26 → 2139.82] And the reason I'm doing it may be to research a particular industry and see what technologies are people using in this industry for, you know, a set of companies, 20 companies that are in an industry.
[2139.82 → 2142.34] So one way to do that is to look at the job ads.
[2142.34 → 2152.46] And you can see, ah, well, they're all using, they tend to use Rust, or they're using this kind of database or that kind of platform or cloud or whatnot.
[2152.46 → 2167.88] But the other thing that you notice as you go through is the style of work environment that employers are pitching or, you know, you're saying this is the way we work and this is what you can expect and this is what we would expect of you.
[2168.64 → 2178.02] And you see all kinds of things like, you know, we have all of these technologies that support feedback, that support continuous integration.
[2178.68 → 2181.18] We are very, very strong on developer testing.
[2181.18 → 2183.62] In fact, we like to do test first development.
[2184.36 → 2189.98] We have small teams that do stand-ups every day and do retrospectives every week.
[2189.98 → 2192.06] And we do planning in this very incremental fashion.
[2192.06 → 2194.44] And you'll find us to be so on and so forth.
[2194.50 → 2197.32] And I'll tell you what, it's almost ubiquitous.
[2198.00 → 2205.18] Most of the companies that I'll look at, certainly in any kind of technology area, are advertising that they work that way.
[2205.64 → 2207.16] And it's become the new normal.
[2207.16 → 2210.50] And that was absolutely not the case 20 years ago.
[2211.18 → 2225.78] So, I think certainly by working, having worked with not just hundreds but thousands of clients and teams over the years and exposing people to that way of working, I think we've had a pretty big impact.
[2225.78 → 2233.36] And because people have been very enthusiastic about working with Pivotal over that time, they then carried on that way of working to others.
[2234.08 → 2236.50] And I mean, we weren't the only people doing this.
[2236.56 → 2239.92] There are certainly plenty of others who were doing it as well.
[2239.92 → 2241.64] But I think we played a part.
[2242.38 → 2242.48] Yeah.
[2243.04 → 2243.72] I think so too.
[2244.20 → 2256.14] I also think that Cloud Foundry and Concourse, the software that Pivotal built and Pivotal just put out in the world for everyone to use, had such a profound impact.
[2256.32 → 2257.84] Because it was embodying the principles.
[2257.98 → 2260.28] Pivotal Tracker, that's another one that comes to mind.
[2260.28 → 2262.02] And I'm sure there were a few others.
[2262.24 → 2268.38] But these are the ones that, you know, the world noticed, and the world started using in different ways.
[2268.60 → 2274.54] And it made them curious about why the software works the way it does.
[2274.58 → 2275.64] And why is it so simple?
[2275.76 → 2279.04] And why does it just like get out of the way and focus on what is important?
[2279.04 → 2285.08] So in episode 64, we talked at length about Concourse with Alex.
[2286.00 → 2290.60] I'm wondering, what is your take on Concourse, the Concourse CI system?
[2291.84 → 2298.00] Well, it will certainly take you back to the point where it was being started and Alex was sort of working on it.
[2298.52 → 2300.78] You know, mostly himself, but he collaborated with a few others.
[2300.78 → 2304.58] And it was sort of a quiet project that was happening, but people were noticing.
[2304.58 → 2315.30] And ANSI Fiore and James Bayer, who were the head of engineering and product for Cloud Foundry development at the time, came to me and said,
[2315.40 → 2320.34] Hey, there's this fascinating project happening called Concourse that Alex has been doing.
[2320.62 → 2324.32] And we think that maybe it's worthy of some additional investment.
[2325.40 → 2329.60] And, you know, I knew Alex was a terrific engineer.
[2329.60 → 2336.72] And certainly if the leadership was coming to me and saying, maybe we should support this more than it was probably something pretty extraordinary.
[2337.10 → 2339.36] And I had seen it being used here and there.
[2339.36 → 2340.64] And I thought it looked fascinating.
[2341.34 → 2345.90] But my first reaction is, does the world really need another CI system?
[2347.20 → 2348.16] Are we serious?
[2348.28 → 2349.06] There's so many.
[2349.06 → 2360.98] And at the same time, we'd kind of been bouncing around CI systems to a certain degree with the Cloud Foundry team, which was getting really quite big, doing very intensive work, very intensive pipelines.
[2361.54 → 2365.90] And one of the problems was that none of the other CI systems were really cutting it.
[2366.48 → 2378.36] They were not scaling and were not as responsive and supportive enough of the way that we worked, especially as it got to scale with Cloud Foundry, that maybe we did.
[2378.36 → 2379.50] Maybe we did need.
[2379.58 → 2381.92] Maybe it was time for another CI system.
[2382.30 → 2385.10] But I was pretty skeptical in that sense.
[2385.32 → 2392.02] But they said, great, let's dig in and let's tell you why and see if you agree with us.
[2392.08 → 2394.20] And so, you know, we had a lot of discussions about it.
[2394.24 → 2395.98] And we talked to Alex, and we're like, you know what?
[2396.72 → 2403.48] This might actually allow us to work at this scale in the way that we work more efficiently.
[2403.98 → 2404.64] And it did.
[2404.64 → 2407.88] And so we put some substantial resources into it.
[2407.92 → 2409.66] And, you know, I gave it my full support.
[2409.74 → 2411.14] And I think it turned out to be pretty amazing.
[2411.36 → 2420.94] And it was always fun to go down to the fourth floor at 875 Howard where we had, you know, the largest set of Cloud Foundry development going on the entire floor.
[2420.94 → 2431.14] And, you know, monitors all over the walls and up on the columns, you know, visualizing the way our pipelines were coming together and building.
[2431.30 → 2432.92] That was always a fun part for me.
[2433.00 → 2437.34] And I could take, you know, customers down there who would say, well, how does this process scale?
[2437.42 → 2438.88] And how does your technology scale?
[2438.88 → 2439.62] And how would you do this?
[2439.68 → 2441.14] And I said, well, let me show you.
[2441.14 → 2447.72] Here's this project that has dozens of teams, hundreds of people building something.
[2448.28 → 2450.56] And you can see all the different pipelines for all the different teams.
[2450.66 → 2452.58] You can see it building in action continuously.
[2452.92 → 2454.56] And here's where it all comes together.
[2455.00 → 2461.48] And you can show them these different things in an exciting visual way that was just happening all the time.
[2461.48 → 2467.70] And it was doing whatever it was doing at that moment in time, whether it was green or red or something was building or whether there was a problem.
[2467.90 → 2469.92] And it helped them understand what we did.
[2470.42 → 2477.80] And for, like, let's say we're talking to Ford or someone like that or, you know, a huge bank.
[2477.80 → 2480.16] And they're wondering, well, what does it look like for us at scale?
[2480.34 → 2489.64] And you can say, well, here's a huge group of developers doing something, a team of teams doing something at a scale, which maybe you'd approach that, but maybe not.
[2489.64 → 2495.32] This certainly is big enough for you to understand what it would look like at your largest scale of product.
[2496.08 → 2497.18] It was very helpful.
[2498.06 → 2502.84] So after Pivotal became VMware, that's the way I think about it.
[2503.08 → 2504.10] Pivotal became VMware.
[2504.40 → 2505.96] That's exactly my view on it.
[2506.58 → 2509.88] We continued using Concourse on RabbitMQ.
[2510.38 → 2518.06] There were many years when the RabbitMQ software had the biggest pipeline, Concourse pipeline you can imagine.
[2518.06 → 2523.06] Not just one, tens and tens of pipelines for different versions, for the clients.
[2524.10 → 2525.66] Just understand the scale.
[2526.32 → 2528.06] This was a couple of years back.
[2528.64 → 2541.92] We had north of 600 CPUs, a few terabytes of RAM, and I don't know how many terabytes of SSD drives, really fast ones, to run all these pipelines.
[2541.92 → 2547.34] I think we had like 10 or 20, between 10 and 20 workers, Concourse workers.
[2548.06 → 2558.98] So a project which is really complex, really mature, was able to run on Concourse, and we were hitting limits, the limits of Concourse, left, right, and centre.
[2558.98 → 2565.14] All the way from the web workers not being able to generate the pipelines because how big they were.
[2565.82 → 2571.34] Like, we talked about this in the previous episodes, and I'll drop a link in the show notes.
[2572.18 → 2575.94] But that was like my last experience of Concourse, and this was a couple of years back.
[2575.94 → 2582.00] When Concourse started, I remember being on the Pivotal Cloud Foundry data services team.
[2582.78 → 2583.62] And we were struggling.
[2583.72 → 2585.42] This was 2016, 2017.
[2586.24 → 2588.14] We were struggling, maybe even 2014.
[2588.38 → 2591.80] Anyway, it was like a significant number of years ago.
[2592.18 → 2593.44] We were struggling with Jenkins.
[2594.04 → 2595.30] We were struggling with Good.
[2595.92 → 2605.54] And while things may have changed, then, at that point in time, Concourse enabled us to do things with data services that no other CI was able to.
[2606.06 → 2608.72] So it worked for a really long period of time.
[2609.24 → 2613.02] And the only thing which I missed was a managed Concourse.
[2613.76 → 2619.32] Like, let me put my card in and let me just get this Concourse service that scales really, really well.
[2619.36 → 2620.70] That was the only thing missing.
[2621.34 → 2624.94] So as a software system, it worked really well for many years.
[2625.36 → 2627.86] And the thing is, I never saw it as a CI system.
[2628.58 → 2631.94] For me, it was at the core of the Pivotal distribution process.
[2632.42 → 2635.30] Because many customers were getting Pivotal software that way.
[2635.78 → 2638.32] So it was so much more than a CI CD system.
[2638.96 → 2639.16] Yeah.
[2639.30 → 2642.74] And that's a whole other area of value that it unlocked.
[2643.28 → 2649.42] That was kind of incredible for an enterprise software system delivered, you know, on-premises.
[2650.24 → 2650.58] Yeah.
[2650.58 → 2650.62] Yeah.
[2651.04 → 2653.32] It was a big enabler, eventually.
[2653.84 → 2653.90] Yeah.
[2654.62 → 2656.84] And it worked for small teams and big teams.
[2657.30 → 2658.72] I think that was the beauty of it.
[2659.24 → 2660.72] It didn't really care how big you were.
[2660.80 → 2661.52] Single process.
[2662.40 → 2663.26] That's all it was.
[2663.26 → 2664.68] You could run it locally if you wanted to.
[2665.14 → 2668.78] Or you could have, you know, tens and tens of worker nodes.
[2669.20 → 2669.86] It was perfect.
[2670.48 → 2677.56] As important as Concourse was, there was this other software which I think had an even bigger impact.
[2677.94 → 2678.98] And that was Cloud Foundry.
[2679.76 → 2680.72] Remember the haiku?
[2681.28 → 2682.12] Here's my code.
[2682.64 → 2683.08] Run it.
[2683.60 → 2684.38] I don't care how.
[2684.72 → 2685.60] That was very memorable.
[2685.60 → 2695.52] How did you think about Cloud Foundry in the beginning as more and more of the software teams were running it, were appreciating it?
[2695.82 → 2697.28] This was five, six years ago.
[2697.74 → 2700.08] What were your thoughts about Cloud Foundry at the time?
[2701.02 → 2701.26] Yeah.
[2701.42 → 2714.54] I mean, I think we had a fascinating opportunity to take teams that were working in, you know, as optimal a way as we could figure out.
[2714.54 → 2723.78] Incremental, evolutionary, you know, building software quickly and getting it into production as fast as possible, getting feedback on it and iterating.
[2723.78 → 2732.90] We were in a position to build a technology that was tailored to that and to do it by interacting with those people.
[2733.60 → 2737.22] And, in fact, building the technology itself using those processes.
[2737.22 → 2745.30] So, it really was, you sort of couldn't design a better crucible for, you know, heating and hardening something like that.
[2746.18 → 2752.72] And, at the same time, you know, building a platform like that, they become quite expansive.
[2753.46 → 2758.68] I mean, it's not just the core runtime and all the tools that you have to build.
[2758.68 → 2762.56] But, it's all the integrations with technology and the services and so on.
[2762.60 → 2765.40] So, a team can really expand as ours did.
[2766.06 → 2776.50] And so, you end up, you know, having the development of a product like this push the process by forcing you into a situation of scale that you've never had in terms of team size.
[2776.50 → 2784.90] And then, the process itself is also essentially continuously critiquing the technology product.
[2785.26 → 2802.04] So, you know, one of the first things that I said to the Pivotal Labs team, when they, you know, after Pivotal Software was formed and, you know, we had sort of a nascent cloud foundry that we'd inherited from VMware that wasn't really in a production state yet.
[2802.04 → 2808.90] But, we had it, and we decided this is really the thing that we ought to commit to and build this out because it's going to be amazing.
[2810.36 → 2820.20] And, the Pivotal Labs teams were a bit apprehensive and understandably so because they said, are you going to force us to use this product now that we're building a product?
[2820.68 → 2823.40] Of course, we're going to have to use it and our clients will have to use it.
[2823.40 → 2831.74] And, I said, I promise you, you won't have to use it until you think it's the most appropriate thing for you to use in a given situation.
[2832.04 → 2833.42] So, you can make that decision.
[2833.88 → 2835.50] And then, we had to work really hard to make it so.
[2835.86 → 2836.58] But, it was.
[2836.82 → 2838.76] I mean, it did become that thing.
[2838.76 → 2860.24] And, especially as Pivotal, you know, in sort of its new incarnation as Pivotal Software shifted from working with 80% to 90% startups and sort of internet technology companies into working with 80% to 90% Fortune 500 and Global 2000 companies and the federal government and so on.
[2860.28 → 2862.26] A very different type of client.
[2862.26 → 2867.48] Cloud Foundry became, you know, the saving grace of all of our engagements.
[2868.04 → 2874.94] Whenever we couldn't use Cloud Foundry, the difficulty was profound in comparison.
[2876.04 → 2887.68] And so, you know, the biggest advocates and champions for Cloud Foundry became the Pivotal Labs teams because working without it was extraordinarily difficult, especially if you were building software that was deployed on-premises.
[2887.68 → 2895.16] But, even if you were deploying in the public clouds, it was still substantially more difficult and painful to do it without Cloud Foundry.
[2895.16 → 2900.60] So, in the present, I know that you're a big fan of Elixir.
[2900.68 → 2904.40] And the reason why I know that is, okay, we talked about it a few times.
[2904.76 → 2908.98] But, also, I was watching your CodeBeam5 America in 2021.
[2909.16 → 2913.04] There was a panel discussion around startups, venture capital, and the Erlang ecosystem.
[2913.58 → 2915.06] I'm going to put a link in the show notes.
[2916.20 → 2918.24] What do you see in Elixir specifically?
[2918.24 → 2922.72] Well, certainly, you know, Erlang's been around for a long time.
[2922.88 → 2936.12] And, you know, we've had various advocates at Pivotal and other people that I've known who loved Erlang and loved its power and its capability and ability to build distributed systems with a lot less code than almost anything else.
[2936.76 → 2941.68] But it always seemed like there was sort of a high priest cast that was the use of Erlang.
[2941.78 → 2944.26] And it didn't seem as accessible to everyone else.
[2944.26 → 2955.88] And Elixir seemed to change that to a certain extent, had the power of Erlang, but also made it more friendly and productive for a wider range of developers, let's say.
[2956.58 → 2962.16] And, you know, I did a fair amount of playing with Elixir when we first decided we were going to use it.
[2962.16 → 2981.42] And I actually did a number of math problems, relatively small, but delightful time doing some math problems with Elixir myself to understand it and felt the joy of programming in this beautiful functional environment.
[2981.42 → 3002.14] So it seemed like, you know, for the work that we've been doing in my incubator over the last Geometer, over the last couple of years, you know, for certain types of projects and the kinds of things that we wanted to build, Elixir would be just a wonderful tool to use and would result in a lot of happy, motivated developers and teams.
[3002.14 → 3008.40] And it was true. I think people have been extraordinarily happy building things in Elixir, very, very productive.
[3009.48 → 3014.48] And it's allowed us to do some things at very high scale with not a lot of code.
[3014.98 → 3017.52] And so it's been extremely effective for us.
[3017.52 → 3031.94] Are there any real world examples, success stories, companies or products that you've built in the incubator using Elixir that would have been difficult otherwise?
[3033.08 → 3034.56] Can we see Elixir in the wild?
[3035.34 → 3036.66] Like, have we used it maybe?
[3037.12 → 3040.44] And we haven't known about it, but they were made possible because of it.
[3040.44 → 3048.94] Well, I could give you a couple of examples with, you know, the first year of the incubator, we were actually sort of diverted to working on COVID response.
[3049.92 → 3059.74] And we worked with the governments of New York and New Jersey, sponsored by the former director of the CDC, who was working on that as well.
[3060.66 → 3068.18] You know, one of the biggest problems that they had in terms of dealing with COVID was actually processing the amount of data that was coming in.
[3068.18 → 3075.36] Because most of the time, if you're dealing with measles or something like that, the number of cases is just relatively small.
[3075.46 → 3081.68] And the volume and the pace at which they're coming in is sort of known and expected and having been dealt with for years, and it's relatively steady.
[3082.50 → 3086.16] Obviously, COVID resulted in hundreds of thousands of cases.
[3086.42 → 3091.38] And so all the systems, all the data exchange was inadequate.
[3091.38 → 3096.04] You know where faxes might have been sufficient, that no longer was even a possibility.
[3096.04 → 3100.02] So everywhere in the chain, the links were broken.
[3100.38 → 3108.38] And so what we ended up doing was building some of the data interchange for, you know, the labs and the health departments and so on.
[3109.12 → 3118.92] And, you know, we were able to build some things that ran very, very quickly where they had been experiencing hours of time or up to a day.
[3118.92 → 3126.92] We took it down to seconds or minutes and build something very, very reliable that ran continuously and just didn't break, essentially.
[3127.14 → 3130.90] So that was a very successful use of Elixir.
[3130.98 → 3132.86] And it's not that you couldn't have done it in something else.
[3133.34 → 3136.74] But we were under a pretty big time crunch.
[3136.94 → 3142.12] It was, you know, early on in the pandemic and things had to happen very, very fast.
[3142.20 → 3142.94] It was a lot of pressure.
[3143.24 → 3145.26] And it was a good technology to use.
[3145.26 → 3147.48] So I think it was very effective for us.
[3148.04 → 3153.22] After that, one of the companies that we've been building is called VEX.
[3153.42 → 3158.60] It's not open to the public yet, but it will be soon at VEX.dev.
[3158.60 → 3165.98] And it is an API-based service to provide real-time communications, video, audio, data.
[3166.60 → 3169.00] And one of its main features is simply its scale.
[3169.36 → 3176.94] So we know that it can handle at least 500,000 people simultaneously, you know, watching streaming video in real time.
[3177.46 → 3180.34] And we expect it will easily handle more than that.
[3180.34 → 3186.02] One of the challenges is simply building systems that can actually test that and verify it, building the load testing.
[3186.94 → 3193.54] But yeah, Elixir's been a great help in building something, again, with a lot of scale and not a lot of code.
[3193.54 → 3196.54] Those were two great stories.
[3196.96 → 3205.50] And seeing them in the wild, I mean, Elixir runs all of change.com, and we're barely using it like at its full potential.
[3205.72 → 3210.28] We're definitely not using the distributed nature of Elixir today, but we will very soon.
[3210.28 → 3223.16] Having talked to Jason from VEX, and I'm hoping that we'll have him soon on Ship It, I was really fascinated by how VEX.dev needs to run on multiple clouds because of the scale.
[3223.92 → 3224.80] And that was fascinating.
[3224.94 → 3227.84] And how do they compare when it comes to just sheer computation?
[3228.34 → 3229.24] There's a lot of audio.
[3229.38 → 3231.28] There's like a lot of video, real time.
[3231.28 → 3242.46] And think hundreds of thousands of streams, concurrent streams, building that like with a small team, it's really difficult and really impressive.
[3242.60 → 3244.64] It's an impressive feat to pull off.
[3244.82 → 3247.68] So I think we will have a chance to talk about that more.
[3247.84 → 3249.10] But I see it too.
[3249.64 → 3250.22] I see it too.
[3250.30 → 3258.78] And having been with Robert Kimchi for a long time, I understand the power of the Erlang VM all the way from the memory allocations to the schedulers.
[3258.78 → 3262.82] There's like so many amazing things, which it has now, to the just-in-time compiler.
[3263.62 → 3267.08] Amazing properties in the VM, as well as in the DSL, which is Elixir.
[3267.24 → 3269.50] It's just the DSL which makes it more accessible, as you mentioned.
[3269.62 → 3273.64] I think that was a key moment for Erlang, and almost like a second life, I think.
[3275.30 → 3279.00] So in January, I joined this new company, Dagger.
[3279.58 → 3288.58] And we've been going through all the motions of a startup where you scale, where you add more people, you grow a team, you're trying to figure out a product.
[3288.78 → 3297.28] And while you have it figured out, you have to react to users and how they use it and what they're missing and all that.
[3297.40 → 3299.32] So all the beauty of that.
[3300.14 → 3309.40] What does your ideal first year for a small startup that grows from, I don't know, a few people to 30 look like?
[3309.92 → 3312.02] What would you recommend for such a small startup?
[3312.66 → 3316.20] Well, then when it comes to people, when it comes to process, when it comes to technology.
[3316.20 → 3318.20] Flash, where to start?
[3319.44 → 3321.86] So many things I could talk about.
[3323.52 → 3324.46] Top of your mind.
[3325.08 → 3326.00] The most important one.
[3326.34 → 3327.28] Yeah, I mean, absolutely.
[3327.46 → 3329.56] I think people are really, really important.
[3330.28 → 3339.10] I mean, you're familiar with how we did things at Pivotal and, you know, the RPI, the one-hour negating interview that was just pure programming.
[3339.10 → 3339.66] Right.
[3339.66 → 3339.96] Right.
[3341.08 → 3348.20] And some joyful programming, too, in my experience when I used to conduct those all the time.
[3348.20 → 3362.42] But we ended up, you know, being able to really assess people well and, you know, not just in terms of their technical prowess, but also their ability to work in a team like ours.
[3362.54 → 3365.56] And, you know, they were able to assess us as well.
[3365.56 → 3372.44] And so I think it's really important, you know, when you're building a small team, especially, but also as you scale.
[3372.54 → 3373.72] Again, this is another one of those things.
[3373.78 → 3375.44] How do you scale and stay consistent?
[3376.44 → 3386.82] Well, you have a hiring process like that really allows you to evaluate the people on their technical ability and their cultural fit and allows them to evaluate you.
[3386.82 → 3397.02] And so if you really have that bidirectional assessment built into your hiring process, and you're very consistent with that and very rigorous with that, I think that is a huge, huge advantage.
[3397.02 → 3405.16] Because you can build a cohesive team and one that will overcome obstacles together and do it in a joyful way.
[3405.88 → 3406.70] That's huge.
[3416.82 → 3429.38] This episode is brought to you by Flat File, the leading data onboarding platform for teams who don't want to build yet another CSV uploader.
[3429.56 → 3432.08] Think of the last time you had to import data from a spreadsheet.
[3432.34 → 3433.74] You probably got some weird errors.
[3434.00 → 3437.26] You had to try a bunch of things like removing blank titles from rows and column headers.
[3437.66 → 3439.52] You probably had to find and replace special characters.
[3439.96 → 3445.18] You might even have to reach for Google to remind yourself yet again how to save with UTF-8 encoding.
[3445.18 → 3446.20] Here's the thing.
[3446.40 → 3452.74] You're just trying to get your file where it needs to go so you can do the thing you're trying to do in the first place.
[3452.74 → 3458.98] And your customers run into this same issue when it matters most right after signing up for your product and getting started.
[3459.40 → 3462.44] The thing you're building, the product, is brought to life by data.
[3462.72 → 3463.64] Your customers' data.
[3464.00 → 3472.60] The data they recognize and every minute they spend trying to fix a spreadsheet just like you were doing is one minute less seeing the magic of the product.
[3472.74 → 3473.46] The thing you're building.
[3473.76 → 3474.58] The thing they just bought.
[3474.58 → 3475.98] And they're so excited to use.
[3476.38 → 3479.44] Now, companies of all sizes struggle with this issue.
[3479.78 → 3481.56] They don't realize that there's a solution out there.
[3481.80 → 3486.56] And they've accepted this as par for the course, optimizing for other ways to improve the customer experience.
[3486.98 → 3491.90] Some go as far as creating downloadable CSV templates and building their own in-house file importer.
[3492.12 → 3495.06] Then they send their customers to a lengthy knowledge-based article on how to use it.
[3495.24 → 3498.16] And it just circumvents the entire process of getting started.
[3498.54 → 3499.28] Enter Flat file.
[3499.28 → 3505.76] Flat file is the data onboarding platform built to take the acute pain out of importing customer data into your product.
[3506.06 → 3509.54] With Flat file, your product's experience is world-class on day one.
[3509.82 → 3516.38] It's built to handle everything from data mapping, field validation, and is meticulously designed to blend right into your platform.
[3516.38 → 3521.46] It turns a frustrating process for everyone into a delightful first experience for your customers.
[3521.86 → 3526.70] Flat file is SOC 2, Type 1, and Type 2 certified, GDPR-compliant, and even HIPAA-compliant.
[3527.04 → 3532.38] This ensures no matter where customers are in the world, they're sharing data securely and in compliance every step of the way.
[3532.38 → 3535.38] The next step is to learn more and check them out at flatfile.com.
[3536.24 → 3537.38] Again, flatfile.com.
[3550.74 → 3552.12] How do you hire like that?
[3552.20 → 3556.58] Because I have my own version, and it's interesting that even this I can trace back to Pivotal.
[3557.04 → 3559.68] How do you hire in the way that you just described?
[3559.78 → 3560.88] How does the process work?
[3560.88 → 3567.10] Well, the RPI was an interview technique that I evolved over quite some time.
[3567.90 → 3571.28] You know, when Pivotal was smaller, I used to do those exclusively.
[3571.60 → 3578.38] So people would program with me for an hour first, and before they went on to secondary interviews, which are also very important, by the way.
[3578.44 → 3590.68] But just to focus on the RPI, it was a measurable, repeatable, 100-point scale that was looking for things like abstract thinking ability, speed.
[3590.88 → 3591.38] And empathy.
[3591.38 → 3592.30] And empathy.
[3593.02 → 3596.30] And I think effectively did that consistently.
[3597.00 → 3601.88] And so you could essentially cast a wide net and not rule anybody out.
[3601.88 → 3608.66] But, you know, relatively objectively evaluate them based on the parameters that really matter to you.
[3608.70 → 3610.46] And then you could pass them on to secondary interviews.
[3610.50 → 3613.34] And I think the secondary interviews are really important as well.
[3613.40 → 3619.42] It's important to have a gating interview that will allow you to filter down to the very few people who might make it through.
[3619.42 → 3620.92] And do it efficiently.
[3621.82 → 3632.32] And because something like the it doesn't have to be the RPI, but something like the RPI that is programming, that is done collaboratively in real time with a real human.
[3632.60 → 3637.04] I don't find much value, by the way, in the automated ones or the AIs or the and that.
[3637.62 → 3640.82] But that human-based filtering that is also efficient.
[3640.82 → 3643.76] And secondary interviews need to be much longer.
[3644.42 → 3654.40] I would say a half a day, you know, with at least two different people really actually working on a product, working on what you do.
[3654.40 → 3660.04] And again, that allows people to see how this candidate is going to fit.
[3660.10 → 3664.10] And it allows them to say, okay, I understand what you're working on.
[3664.20 → 3666.06] I understand how you work in your team.
[3666.36 → 3667.84] Do I really want to be here?
[3667.96 → 3669.34] Does this fit for me?
[3669.68 → 3670.70] And vice versa.
[3670.84 → 3674.08] If you can do that, I think that's it.
[3674.46 → 3676.44] That is a really effective way of interviewing.
[3676.94 → 3677.42] It takes time.
[3677.80 → 3678.62] That's a good one.
[3678.92 → 3679.48] That's a good one.
[3679.74 → 3681.98] Not as much time as some very ineffective ways I've seen.
[3682.68 → 3683.08] Yeah.
[3683.08 → 3684.08] Oh, yes.
[3684.08 → 3684.52] Yes.
[3684.56 → 3691.02] Hiring is very important and knowing how to hire well and getting the right people in can have such a huge impact.
[3691.66 → 3697.62] Especially in a small company where one person can mean 10% or even 5% of a company.
[3697.70 → 3701.54] When you're 3,000, I mean, you know, like the gravity is very different.
[3702.18 → 3705.42] But when you're small, like every person matters.
[3705.54 → 3706.40] It's a big, big deal.
[3707.52 → 3711.58] What about optimizing for shipping it?
[3711.68 → 3712.60] Like getting it out there?
[3712.60 → 3720.14] Companies that optimize for execution versus just, you know, brainstorming and planning and all that.
[3720.74 → 3723.30] What would you say about that aspect?
[3723.30 → 3725.16] I think it's absolutely important.
[3726.00 → 3730.88] It's easy to make mistakes in that area.
[3731.10 → 3734.34] I've certainly made many, not shipped early enough.
[3734.86 → 3739.08] But I think in your case, you've got something that's already being used pretty widely by people.
[3739.48 → 3740.96] I sort of started that way.
[3741.38 → 3742.68] So that's fortunate.
[3742.68 → 3749.08] And, you know, obviously I think leaning into that and continuing to ship continuously is, I don't think I need to tell you that.
[3749.64 → 3749.76] Yeah.
[3750.06 → 3750.76] No, no, no.
[3751.12 → 3756.76] When it comes to acting on user feedback, what does a healthy loop look like?
[3756.76 → 3765.40] When you're paying attention to what users are saying, but then you know what is important, and you can implement those in a certain priority.
[3765.40 → 3774.42] What does that process look like so that you are responding to what users are asking for rather than continuing on tangents that you think may be a good idea?
[3774.42 → 3781.56] I think one of the things that happens with users when they have requests is they don't necessarily see them in context of all the other things that are happening.
[3782.36 → 3789.62] And certainly when we used to work with client teams, and you would have various stakeholders saying this is number one priority, that's number one priority.
[3789.72 → 3799.12] If you really exposed it quite clearly and said, well, look at the sum total of what we're working on and weigh these in comparison, what would you really think?
[3799.12 → 3807.06] And oftentimes they would change their mind and say, you know what, this other thing you're working on is more important than the thing that I was saying is top priority.
[3807.20 → 3817.50] So I think having the transparency and visibility for your users is important so that they can see what other people are asking for and understand the relevant importance of those.
[3818.12 → 3818.20] Okay.
[3819.28 → 3821.50] Would you use Pivotal Tracker today?
[3821.84 → 3823.16] Would you still recommend it today?
[3823.72 → 3824.68] We do use it.
[3825.56 → 3827.10] Interestingly enough, we tried not to.
[3827.10 → 3833.80] So I just said that one of our portfolio companies at Geometer is called Cohort with a K.
[3834.10 → 3836.46] And sometimes I forget that Cohort is actually spelled with a C.
[3836.78 → 3837.86] It's in my brain now.
[3838.72 → 3845.10] But that team is led by Dan Moseley, who led the Tracker team for many years.
[3846.18 → 3848.36] And so he's the CEO of Cohort.
[3849.12 → 3855.36] And he said, you know what, I don't want to make the team use Tracker just because I ran Tracker all this time.
[3855.36 → 3858.18] And I think he was challenging himself to do something else.
[3858.22 → 3859.82] He said, we're going to go use something else.
[3860.88 → 3864.46] And so they picked something that was getting a lot of traction.
[3864.58 → 3868.74] It's relatively new in the market as the best thing that they could find.
[3868.78 → 3869.96] And they started using it.
[3870.10 → 3873.02] And after a month, the team said, can we please just go back and use Tracker?
[3873.02 → 3877.64] So reluctantly, Dan went back to using the thing that he built.
[3878.72 → 3882.32] So, yeah, it's still useful.
[3883.18 → 3883.36] Okay.
[3883.92 → 3892.94] As we prepare to wrap this up, what would you say is the most important takeaway for our listeners, the ones that stuck with us all the way to the end?
[3892.94 → 3907.34] This is something that occurred to me that I saw when we were working with really large companies, government agencies, and that there was always a focus on the next powerful technology.
[3908.06 → 3914.34] Usually AI or machine learning, something that could come under those descriptors.
[3914.34 → 3926.64] But in many cases, we found that the fundamentals completely lacking in the teams and the organization that was looking to adopt some of these technologies.
[3926.64 → 3949.22] And in a world that is increasingly reliant on software, it feels to me like getting the fundamentals right, building software extremely well and doing it in a humane way and building that foundation is so much more important than adopting the next technology.
[3949.22 → 3954.64] In other words, if you don't have an AI strategy, you're not going to do X, Y, or Z.
[3954.76 → 3959.86] Or if you haven't figured out all of your security posture, then you're vulnerable.
[3960.70 → 3976.48] Fundamentally, if you have a culture of software development that is very strong and very resilient, and if you're truly expert at that, then you can use these technologies effectively.
[3976.48 → 3983.66] And you can plug them into your environment and use them 10 times better than you would have.
[3983.72 → 3991.06] If you just run out on an AI initiative and say, we're going to use this technology, and your foundation is a mess.
[3991.60 → 4004.34] I think many large organizations are setting themselves up for ultimate failure by not focusing on building things in a very rigorous, very evolutionary, and very humane way.
[4004.34 → 4017.72] That was something that I saw at Pivotal that really opened my eyes to the state of where things were with respect to the ambitions that people have for the technology that they're going to use and the reality of how they do things.
[4018.78 → 4022.30] That is a very meaningful thought to end on, I think.
[4022.76 → 4023.42] Very meaningful.
[4023.94 → 4025.36] We'll definitely send the test of time.
[4025.46 → 4025.94] We'll apply.
[4026.70 → 4027.52] Many use in the future.
[4028.28 → 4029.58] Focus on what matters to you.
[4029.96 → 4031.32] And technology?
[4031.70 → 4032.34] Maybe not.
[4032.34 → 4034.20] Maybe there's something else there.
[4034.92 → 4036.46] Well, it's been an absolute pleasure.
[4036.94 → 4040.40] Thank you very much for joining us today, and I'm looking forward to next time.
[4040.62 → 4040.92] Thank you.
[4041.22 → 4041.56] Thank you.
[4041.66 → 4042.56] It's been my pleasure being here.
[4042.64 → 4043.14] Appreciate it.
[4046.74 → 4049.58] Thank you for tuning into another episode of Ship It.
[4049.98 → 4054.92] Check out our other podcast for developers at changelog.com slash master.
[4055.10 → 4060.16] You can connect with like-minded developers via changelog.com slash community.
[4060.16 → 4064.28] Thank you, Vastly, for the worldwide low-latency changelog.com.
[4064.66 → 4067.94] Our listeners love those blazing fast MP3s.
[4068.60 → 4072.72] The Firecracker VMs and the WireGuard integration are really sweet.
[4073.26 → 4073.96] Fly that IO.
[4073.96 → 4075.78] That's it for this week.
[4076.02 → 4076.76] See you all next week.
[4077.28 → 4081.88] My last thought is to encourage you to write down the values which are important to you.
[4082.26 → 4085.76] It shouldn't take more than five minutes, and I can tell you with great confidence
[4085.76 → 4091.84] that once you know what they are, it is far easier to identify the companies and teams
[4091.84 → 4092.72] where you belong.
[4092.72 → 4102.02] Game on.
