[0.00 → 26.98] What's up friends, this is the changelog.
[26.98 → 33.04] We feature the hackers, the leaders, and those taking on Goliath, aka Slack and Teams.
[33.68 → 37.94] Yes, we're joined by Ali Abbott, one of the fine folks behind Zulip.com,
[38.32 → 43.84] the open source, organized team chat for distributed teams of all sizes.
[44.52 → 49.28] And we're going through all the things, open source, its origins, what makes it different,
[49.82 → 53.42] why it might be better, how you can self-host it, how you can use their cloud,
[53.42 → 59.22] how you can contribute, how you can be part of their community, all the things in this show.
[59.76 → 65.78] A massive thank you to our friends and our partners over at fly.io.
[66.22 → 69.32] That is the home of changelog.com.
[69.60 → 71.54] Over 3 million apps have launched on Fly.
[71.66 → 73.32] We're one of them, and we love Fly.
[73.64 → 75.00] And you will love to Fly too.
[75.48 → 78.10] Check them out at fly.io.
[78.10 → 80.24] Okay, let's Zulip.
[90.38 → 93.90] Hey friends, I'm here with Dave Rosenthal, CTO of Sentry.
[94.20 → 98.20] So Dave, I know lots of developers know about Sentry, know about the platform,
[98.66 → 100.68] because hey, we use Sentry, and we love Sentry.
[100.98 → 104.44] And I know tracing is one of the next big frontiers for Sentry.
[104.44 → 106.26] Why add tracing to the platform?
[106.56 → 107.96] Why tracing, and why now?
[108.28 → 111.62] When we first launched the ability to collect tracing data,
[111.98 → 115.62] we were really emphasizing the performance aspect of that,
[115.70 → 117.88] the kind of application performance monitoring aspect.
[118.08 → 119.66] You know, because you have these things that are spans,
[119.82 → 121.28] that measure how long something takes,
[121.34 → 124.06] and so the natural thing is to try to graph their durations,
[124.30 → 125.48] and think about their durations,
[125.68 → 128.22] and, you know, warn somebody if the durations are getting too long.
[128.40 → 131.76] But what we've realized is that the performance stuff
[131.76 → 134.56] ends up being just a bunch of gauges to look at,
[134.86 → 136.52] and it's not super actionable.
[136.52 → 139.20] Sentry is all about this notion of debuggability
[139.20 → 141.00] and actually making it easier to fix the problem,
[141.10 → 142.64] not just sort of giving you more gauges.
[142.96 → 146.06] A lot of what we're trying to do now is focus a little bit less
[146.06 → 148.68] on the sort of just the performance monitoring side of things
[148.68 → 153.04] and turn tracing into a tool that actually aids the debuggability of problems.
[153.04 → 154.06] I love it.
[154.14 → 156.48] Okay, so they mean it when they say code breaks.
[156.72 → 158.04] Fix it faster with Sentry.
[158.26 → 161.86] More than 100,000 growing teams use Sentry to find problems fast,
[162.00 → 162.98] and you can too.
[163.44 → 165.92] Learn more at Sentry.io.
[166.06 → 169.82] That's S-E-N-T-R-Y.io.
[170.42 → 172.22] And use our code, changelog.
[172.32 → 174.48] Get $100 off the team plan.
[174.78 → 177.42] That's almost four months free for you to try out Sentry.
[177.42 → 180.24] Once again, Sentry.io.
[180.24 → 180.42] Thank you.
[207.42 → 216.40] So we are joined today by Alia Abbott from Zulip.
[216.80 → 218.08] Welcome to the changelog.
[218.46 → 219.52] Great to be here, yeah.
[219.80 → 220.80] Great to have you.
[220.90 → 226.40] Great to have an open source chat application out there,
[226.44 → 227.64] and one with a story and history.
[227.78 → 231.32] You all have been around a long time, in and out of Dropbox even.
[231.50 → 233.20] I would love to hear a little bit about that story.
[234.00 → 236.44] Dropbox acquired and then open source out of that.
[236.44 → 237.72] Can you give us a little bit of the history?
[238.08 → 238.20] Really?
[238.44 → 239.32] Yeah, yeah, yeah.
[239.54 → 240.90] Zulip has kind of an interesting history.
[241.10 → 243.34] So it was started back in 2012,
[243.74 → 246.38] so before things like Slack were out there.
[247.06 → 247.24] Yeah.
[247.52 → 249.14] At that time, it was not open source.
[249.30 → 253.76] It was just kind of your regular closed source startup out in Boston.
[254.42 → 256.66] And when it was still in private beta,
[256.72 → 258.54] the company was acquired at Dropbox.
[259.08 → 261.88] At the time, Dropbox was exploring kind of different strategies
[261.88 → 265.30] with chat as kind of providing a suite of Office products
[265.30 → 267.02] alongside with the file storage.
[267.26 → 269.08] And then they went in a different direction
[269.08 → 274.00] and actually open sourced the entire Zulip code base
[274.00 → 277.24] along with the full history of the project.
[277.52 → 279.14] So all that commit history,
[279.26 → 281.92] there was a Hack Week project to clean that up
[281.92 → 283.90] and make that something that can be publicly shared.
[283.90 → 285.64] And they very generously,
[286.12 → 288.62] I guess once it was open sourced,
[288.82 → 291.68] Tim Abbott, who was one of the original co-founders
[291.68 → 293.58] and was working at Dropbox at the time,
[293.74 → 296.36] started running that open source project
[296.36 → 299.00] in his kind of nights and weekends in his spare time.
[299.92 → 302.66] And Dropbox also very generously gave the trademark
[302.66 → 304.44] for Zulip to Tim as well.
[304.66 → 305.82] So at this point,
[305.86 → 308.60] there's no relationship between Zulip and Dropbox.
[308.66 → 309.84] There's no relationship at all.
[309.84 → 310.56] Yeah, yeah.
[310.72 → 313.60] But we're definitely very grateful that they decided
[313.60 → 315.72] that they would be happy to open source it
[315.72 → 317.38] given that they were not using it themselves.
[318.10 → 319.00] Why did they make that decision?
[319.14 → 320.54] Do you know why that decision was made?
[321.04 → 322.60] I know Tim advocated for it
[322.60 → 324.84] and that's really just they wanted to contribute to open source
[324.84 → 327.18] and just kind of generous gesture for the community.
[328.20 → 329.06] Well, that's pretty cool.
[329.24 → 331.72] So when they bought Zulip or,
[332.48 → 334.16] yeah, I guess it was called Zulip from the beginning?
[334.50 → 336.66] Yeah, the product was called Zulip at the time.
[336.66 → 338.38] So when they bought Zulip
[338.38 → 340.68] and then Tim came inside of Dropbox,
[340.78 → 343.38] was the original idea was to integrate
[343.38 → 345.16] and build that as part of their product
[345.16 → 346.34] and they decided not to?
[346.58 → 347.16] Yeah, originally,
[347.46 → 349.80] I don't know the details of their strategy,
[349.94 → 351.20] but probably I think originally
[351.20 → 354.14] they had thought that they might build their own chat app.
[354.64 → 355.32] As you know,
[355.38 → 357.24] I know you probably maybe have heard of,
[357.28 → 359.98] you know, Dropbox Paper, Mailbox.
[360.12 → 361.90] They kind of were at the time acquiring startups
[361.90 → 363.54] in a bunch of the office tools,
[363.88 → 365.26] in the office tool space more generally.
[365.26 → 365.82] Yeah.
[365.82 → 368.74] And then kind of company priorities shifted.
[369.08 → 372.56] The Zulip team ended up working on the core Dropbox product.
[373.32 → 375.74] And yeah, so they just kind of didn't end up going in that direction.
[376.20 → 376.32] Huh.
[376.80 → 378.34] Very generous to open source it though.
[378.40 → 378.62] Yeah.
[378.80 → 379.02] Right.
[379.08 → 379.92] And all the history.
[380.40 → 383.18] That's like kind of unheard of, wouldn't you say?
[383.60 → 385.06] And then like be disconnected completely,
[385.18 → 388.76] like no back link or connection to it.
[388.84 → 391.42] Just like be free bird, go fly.
[391.42 → 391.82] Yeah.
[392.02 → 392.46] Yeah.
[392.48 → 394.62] And one thing that's pretty cool is that
[394.62 → 396.70] we actually still have some of Zulip's
[396.70 → 400.76] like 2013 beta customers using Zulip today continuously.
[400.76 → 400.94] Oh, wow.
[400.94 → 403.02] So they still have all their chat history that
[403.02 → 405.44] like we've kept that running for them
[405.44 → 408.00] throughout the years, and they're still there.
[408.68 → 410.08] So pre-slack, like you said,
[410.14 → 412.56] definitely not pre-chat though.
[412.70 → 413.64] I mean, IRC.
[413.94 → 414.06] Yeah.
[414.18 → 416.96] So like hip chat and IRC were around at the time.
[417.16 → 417.24] Exactly.
[417.24 → 417.46] Yeah.
[417.46 → 418.20] Hip chat.
[418.90 → 419.30] Campfire.
[419.64 → 420.42] Remember Campfire?
[420.42 → 420.86] Yeah.
[420.86 → 421.06] Yeah.
[421.16 → 421.38] Yeah.
[421.38 → 421.68] Yeah.
[421.80 → 422.02] Yeah.
[422.10 → 422.42] Those were,
[422.50 → 424.50] so that was a competitive landscape at the time.
[424.88 → 425.32] Yeah, totally.
[425.44 → 427.30] What was Zulip's big idea then?
[427.36 → 429.94] Like why did it begin to exist in the first place
[429.94 → 431.62] versus just using hip chat for instance?
[431.76 → 432.02] Totally.
[432.14 → 432.32] Yeah.
[432.40 → 432.56] Yeah.
[432.60 → 437.26] So the big innovation in Zulip is how it organizes conversations.
[437.26 → 440.50] And the idea actually came from an older technology
[440.50 → 443.18] that was popular at MIT at the time
[443.18 → 446.10] for like lots of students and folks were chatting there.
[446.10 → 450.20] But what's different about it is how conversations are organized.
[450.72 → 453.72] So in some of the tools folks may be familiar with,
[453.80 → 454.34] you have a channel,
[454.44 → 456.92] you probably have channels and within that channels,
[457.24 → 458.72] a lot of discussion going on,
[458.74 → 460.18] kind of like in that main channel feed,
[460.30 → 461.90] maybe you have some threads on the side.
[462.64 → 465.54] Zulip is different in that when you start a conversation,
[465.54 → 468.32] you give that conversation a brief topic.
[468.32 → 470.30] So something is similar to what you might do
[470.30 → 471.12] if you're sending an email
[471.12 → 473.36] and you write like a quick subject line for your email.
[473.98 → 477.14] And then when people respond to your messages,
[477.28 → 479.12] they respond within that topic.
[479.30 → 482.52] And so it's a little bit of extra effort
[482.52 → 484.16] to start that conversation.
[484.28 → 485.46] You do need to give it a topic,
[485.46 → 488.74] but then it just makes a huge difference
[488.74 → 490.54] when you're reading your messages.
[490.90 → 494.18] So now instead of kind of everything being mixed up,
[494.18 → 496.02] you have these organized conversations
[496.02 → 497.18] labelled with our topic.
[497.18 → 501.96] And so you can come in and read your messages
[501.96 → 503.50] one conversation at a time,
[503.50 → 505.92] rather than everything happening chronologically.
[506.32 → 508.52] You could say, okay, people are talking about this.
[508.62 → 509.54] Let me read about that.
[509.70 → 511.40] Okay, I'm done with that conversation.
[511.88 → 513.46] Let me move on to the next one.
[514.10 → 515.68] And so it doesn't matter if people are,
[515.88 → 516.80] and it's a busy channel.
[516.92 → 518.84] People are talking about 10 different things at once.
[519.18 → 520.34] It's just not a problem.
[520.52 → 523.38] You can read everything in its own context
[523.38 → 526.96] and you can have a conversation that goes across time.
[527.32 → 529.26] So maybe people are working async
[529.26 → 531.16] or just busy with meetings.
[531.16 → 533.64] And so somebody comes in a few hours later
[533.64 → 535.20] or a day later and wants to comment
[535.20 → 536.52] on something that was going on.
[536.96 → 539.24] Rather than getting kind of like lost in the noise,
[539.34 → 541.38] you have all that context in the same place.
[542.22 → 545.24] So every Zulip instance has channels,
[545.60 → 547.76] which are like long-lasting things.
[547.76 → 550.36] And then the channels have inside of them topics.
[550.48 → 552.00] Is that the architecture?
[552.00 → 553.70] Yeah, exactly, exactly.
[554.00 → 555.86] So, and then each topic is basically
[555.86 → 557.36] kind of topic of conversation
[557.36 → 559.30] and that can be very ephemeral
[559.30 → 562.60] or it can be something that you come back to after a while
[562.60 → 566.22] and that, you know, both ways work.
[566.50 → 568.66] And what differentiates a channel from a topic?
[568.80 → 571.86] Is it merely their position in that structure
[571.86 → 573.70] or is there something about a topic
[573.70 → 574.86] that's different from a channel?
[574.92 → 577.68] Because a lot of chat apps just have channels.
[578.06 → 578.34] Yeah.
[578.58 → 581.02] And then inside there, they're just chronological,
[581.02 → 583.58] but then you can kind of like drill down in threads and stuff.
[583.66 → 585.56] And so I'm just trying to understand,
[585.76 → 588.52] are there actual data differences
[588.52 → 589.58] between a channel and a topic
[589.58 → 591.74] or just kind of where they exist inside the hierarchy?
[592.12 → 593.88] I mean, the channel is very similar to channels
[593.88 → 594.50] and other apps.
[594.62 → 596.84] So for example, like you have,
[597.02 → 598.54] it comes with some metadata,
[598.76 → 600.76] like subscribers, privacy settings,
[600.86 → 601.80] those sorts of things.
[602.22 → 604.98] And then topics are just another level of organization
[604.98 → 606.30] within that channel.
[606.30 → 609.80] So for example, for your subscriptions,
[609.98 → 611.82] you would be managing your subscriptions to channels
[611.82 → 614.52] and then you would automatically see the topics
[614.52 → 616.06] that are in the channels that you're in.
[616.70 → 618.36] We do actually have ways to,
[618.76 → 620.34] within that, mute specific topics
[620.34 → 621.62] or follow specific topics.
[621.62 → 625.32] So you can kind of like set your preferences there as well.
[625.48 → 628.46] But yeah, it's just kind of another level of structure.
[628.86 → 631.34] And that, you know, there's also ways to view,
[631.96 → 634.68] instead of viewing all your messages in a feed,
[634.68 → 636.24] you can also view the topics.
[636.50 → 638.34] So there's an inbox style view
[638.34 → 640.32] where you can see your unread topics.
[640.86 → 642.64] And then you can just jump into the places
[642.64 → 645.90] where you're like, oh, this is relevant for me.
[646.06 → 647.14] Let me take a look at that.
[647.54 → 648.98] And there's also, there's another view
[648.98 → 650.66] that lets you see the recent conversations.
[650.66 → 652.92] So again, kind of gives you different ways
[652.92 → 654.86] to summarize what's going on
[654.86 → 657.60] and really dive into what's important for you
[657.60 → 658.70] and where you need to participate.
[659.64 → 661.28] Does every message inside a channel
[661.28 → 663.40] have to exist inside a topic?
[663.40 → 664.92] Or is there also just like the
[665.54 → 667.84] we're just messaging, we're not to picking?
[668.32 → 670.06] Yeah, that's something that's configurable
[670.06 → 671.48] by the organization administrators.
[672.04 → 674.92] In general, there's not a lot of need for the
[675.18 → 675.94] it depends.
[676.38 → 677.86] But in general, we do recommend,
[677.96 → 679.06] we generally recommend
[679.06 → 681.16] having at least the vast majority
[681.16 → 682.90] of the messages happen in topics.
[683.64 → 683.88] Yeah.
[684.06 → 686.82] I mean, once you're replying to a conversation
[686.82 → 687.54] that's already ongoing,
[687.66 → 689.12] you kind of hardly notice this.
[689.42 → 690.70] It doesn't create any extra work.
[690.70 → 692.80] You just click on your reply.
[692.94 → 694.28] It's not like you have to retype the topic
[694.28 → 694.92] or anything else.
[695.02 → 697.76] So it's really not a lot of overhead.
[698.10 → 699.36] And once people get the idea,
[699.70 → 702.46] it's really pretty seamless.
[703.20 → 703.36] Okay.
[703.36 → 705.74] And we also give folks tools
[705.74 → 708.38] to kind of reorganize everything
[708.38 → 710.36] if things do end up out of place.
[710.54 → 712.80] So you can move messages between topics
[712.80 → 714.12] as well as between channels.
[714.44 → 716.74] So especially when an organization
[716.74 → 717.54] is just getting started
[717.54 → 719.04] and folks are getting used to the model,
[719.04 → 721.80] that really lets you reorganize things
[721.80 → 724.18] if things do end up in the wrong place.
[724.42 → 724.72] Yeah.
[724.72 → 725.16] To start with.
[725.94 → 726.96] I suppose if you really wanted
[726.96 → 728.24] just like a general chat
[728.24 → 729.64] inside a channel,
[729.78 → 730.70] you could just have a topic
[730.70 → 731.96] called general chat.
[732.22 → 732.86] And then you're just like.
[732.90 → 733.80] You totally could.
[733.90 → 734.18] Absolutely.
[734.48 → 734.54] Yeah.
[734.56 → 736.04] You know, it becomes a junk drawer.
[736.44 → 737.52] If nothing fits here,
[737.60 → 738.98] then it just fits in the junk drawer.
[739.22 → 740.60] And the junk drawer ends up being
[740.60 → 742.38] the only place people talk
[742.38 → 743.16] and then you're not using
[743.16 → 743.84] the tool right anymore.
[743.92 → 744.22] Definitely.
[745.48 → 746.34] That's the biggest struggle.
[746.54 → 746.76] Yeah.
[746.82 → 748.72] And the thinking is really that people are,
[748.80 → 750.24] I mean, people are spending tons of time
[750.24 → 750.98] throughout the day
[750.98 → 752.24] on communication.
[752.24 → 753.86] You know, some surveys found
[753.86 → 756.04] there's something like half of the time
[756.04 → 756.90] for knowledge workers
[756.90 → 758.50] spent on some communication
[758.50 → 760.10] of one kind or another.
[760.66 → 762.76] And so just making that more efficient
[762.76 → 764.52] is just can make a huge difference
[764.52 → 765.78] in terms of people's time.
[767.08 → 768.68] And if you think about
[768.68 → 769.48] what you're actually doing
[769.48 → 770.50] when you do communicate
[770.50 → 771.60] and when you do chat,
[771.78 → 773.46] it's most of that time
[773.46 → 774.74] is really spent reading messages.
[775.28 → 776.84] So of course you're sending some messages,
[777.08 → 778.74] but there's more time spent
[778.74 → 779.88] kind of ingesting content.
[779.88 → 781.72] And so if that process
[781.72 → 783.12] is really smooth and seamless
[783.12 → 784.90] and feels kind of structured
[784.90 → 785.66] and not chaotic,
[785.66 → 787.52] that's going to make a huge difference
[787.52 → 788.66] for people's experience
[788.66 → 789.28] throughout the day.
[790.40 → 792.66] I'm looking at the screenshot
[792.66 → 793.36] on your homepage,
[793.78 → 796.84] which I assume is up-to-date.
[796.98 → 797.52] Is it up to date?
[797.78 → 798.18] Yeah.
[798.66 → 799.42] Pretty accurate?
[799.68 → 800.14] Pretty accurate.
[800.68 → 801.10] Okay, cool.
[801.20 → 802.46] Because sometimes homepages
[802.46 → 803.28] get out of date, you know?
[803.42 → 804.74] They have a live demo there.
[804.98 → 806.40] Their personal chat
[806.40 → 808.22] is chat.zulip.org,
[808.28 → 809.16] like their dev chat.
[809.16 → 811.18] And you can join that anonymously, Adam.
[811.22 → 811.96] And then you'd have like,
[812.12 → 813.46] you'd actually be using the software,
[813.60 → 814.24] which is pretty cool.
[814.78 → 817.06] If you wanted to like actually see how it,
[817.40 → 818.80] and you can go through channels and topics.
[818.96 → 819.52] And so that's a
[819.70 → 821.24] I found that to be a pretty good way
[821.24 → 823.52] of just seeing exactly how it works.
[824.08 → 824.16] Yeah.
[824.24 → 825.46] Where would I go to do that real quick?
[825.48 → 826.40] Because I was trying to do,
[826.66 → 827.86] I was trying to open that conversation,
[827.96 → 829.04] like get into the actual UI.
[829.38 → 831.00] I don't know where the link is,
[831.04 → 832.68] but just go to chat.zulip.org.
[832.68 → 833.64] And then I think
[833.64 → 836.40] I'm currently in the design channel
[836.40 → 839.92] looking at the channels and topic illustrations topic.
[840.72 → 841.30] Uh-huh.
[841.46 → 843.90] And it's very active and scroll.
[844.00 → 845.66] I was just looking for the most recent conversation.
[845.78 → 846.36] So that's kind of cool.
[846.42 → 846.86] As you hop in,
[846.90 → 848.22] you can see all the recent conversations.
[848.42 → 848.72] And yes,
[848.72 → 851.46] you can jump into those different topics.
[851.98 → 852.26] Yeah.
[852.26 → 853.68] And see what's going on there.
[853.92 → 855.36] It seems pretty well organized.
[855.54 → 855.82] I mean,
[856.56 → 857.96] we use Slack on the daily
[857.96 → 859.48] and we have slightly less organization.
[859.62 → 860.56] We have channels.
[861.08 → 862.46] And now there are threads,
[862.58 → 863.80] which is kind of a bolt on,
[864.08 → 865.78] which kind of can act as a topic,
[865.78 → 867.56] but they're more like ad hoc,
[867.66 → 867.82] like,
[867.98 → 868.10] hey,
[868.16 → 869.54] maybe I'll reply in the thread
[869.54 → 871.34] or maybe I'll reply to the whole channel.
[871.34 → 872.40] And then it gets to be like,
[873.04 → 875.14] what's the idiom
[875.14 → 875.92] or what's the general,
[876.16 → 876.52] like how,
[876.60 → 877.86] what's the culture around threads?
[877.98 → 878.76] How do we use them?
[878.78 → 879.62] And people use them differently.
[879.62 → 882.16] And it gets to be hairy because of that.
[882.16 → 883.82] I think this little bit of extra structure,
[883.96 → 884.84] which really isn't very much.
[884.88 → 886.30] It's like one more level of structure.
[886.76 → 887.12] Yeah.
[887.20 → 887.42] You know,
[887.46 → 888.70] it's like channel and topic
[888.70 → 892.72] might help organize your communications.
[892.72 → 894.66] And it seems like it is
[894.66 → 897.54] because you all still exist here 12 years later.
[898.00 → 898.40] Yes,
[898.42 → 899.10] 12 years later.
[899.10 → 900.30] And now you're a thriving business
[900.30 → 901.28] on top of open source projects.
[901.28 → 902.30] So people must like this,
[902.44 → 903.24] this model.
[903.66 → 903.80] Yeah.
[903.96 → 904.18] I mean,
[904.20 → 904.78] that's the
[905.38 → 905.62] you know,
[905.64 → 908.06] we get lots of feedback from folks
[908.06 → 911.54] and that's really the biggest differentiator for people.
[912.16 → 913.98] Is that level of good as an organization
[913.98 → 915.10] just makes a huge difference
[915.10 → 917.38] in people's experience using the product.
[917.56 → 918.28] Like people tell us,
[918.42 → 918.58] like,
[918.62 → 919.14] I can't,
[919.30 → 919.46] you know,
[919.48 → 919.86] it's hard to,
[920.02 → 920.34] you know,
[920.38 → 921.72] sometimes I have to go back to Slack
[921.72 → 923.04] to talk to my customers
[923.04 → 924.88] and it's just so chaotic.
[924.88 → 925.60] And it's,
[925.60 → 925.86] you know,
[925.86 → 928.28] just having experienced the level of organization
[928.28 → 929.02] within Zulip,
[929.60 → 930.52] other things feel,
[930.92 → 931.08] if you,
[931.26 → 933.16] people started feeling like other things are messy
[933.16 → 934.80] and hard to follow.
[935.44 → 935.88] Adam,
[935.92 → 936.96] have you clicked around enough now
[936.96 → 938.58] to formulate what you were going to ask before?
[938.76 → 939.06] Yeah.
[939.06 → 940.50] Have you found messages from me,
[940.56 → 940.68] Ed?
[941.32 → 941.98] I just,
[942.14 → 943.82] I do like it.
[943.90 → 946.44] So I'm going to paint a verbal picture
[946.44 → 947.98] of this visual I'm looking at.
[948.58 → 950.22] So channels on the left,
[950.64 → 951.56] topics to the right of me.
[952.28 → 952.96] Here I am.
[953.04 → 954.40] I'm just stuck in the middle with us.
[954.46 → 955.12] It's stuck in the middle,
[955.22 → 955.46] you know?
[955.64 → 956.00] Nice.
[956.18 → 956.62] Well played.
[956.82 → 957.18] Great song,
[957.24 → 957.54] by the way.
[958.04 → 959.94] I like when you click on a channel,
[960.06 → 961.10] you see these topics.
[961.10 → 963.04] And then if you click on show all topics,
[963.04 → 966.06] you obviously get into a channel view
[966.06 → 967.60] with all the topics in it
[967.60 → 969.22] that you can filter and scroll
[969.22 → 970.90] and you can easily go back to channels.
[971.50 → 971.54] Yeah.
[971.62 → 972.70] I'm not signed in,
[972.76 → 974.68] so I can't see how like I start new ones,
[974.76 → 976.56] but it does seem pretty snappy
[976.56 → 980.68] in terms of just how easily you can map around.
[980.74 → 983.34] I just wonder if it's overhead
[983.34 → 986.86] on anybody's part to organize messages,
[987.50 → 988.52] organize topics,
[988.52 → 989.40] because you can,
[989.66 → 989.98] you know?
[990.16 → 991.08] That's what I was trying to figure out.
[991.08 → 991.98] Well, for the most part,
[992.02 → 993.32] it's kind of self-organizing.
[993.48 → 994.56] So just when somebody is starting
[994.56 → 995.36] a new conversation,
[995.66 → 997.38] they'll start a new topic.
[997.94 → 999.00] I mean, in the Zulip community,
[999.00 → 1000.52] we do have a lot of folks who,
[1000.82 → 1001.10] you know,
[1001.14 → 1001.94] are new contributors
[1001.94 → 1003.10] or somebody who's coming in
[1003.10 → 1004.64] who's kind of like brand new to the product
[1004.64 → 1005.62] or just checking it out.
[1006.06 → 1007.74] So sometimes they might not,
[1007.80 → 1010.40] not be sure exactly how to name a topic well
[1010.40 → 1011.52] or where to post it.
[1011.56 → 1014.92] And then just when somebody sees that
[1014.92 → 1015.80] it was posted on place,
[1015.88 → 1017.38] they'll move it around to where it should be.
[1017.48 → 1019.44] So it's not like a big job.
[1019.44 → 1020.24] It's just you,
[1020.24 → 1021.08] you're reading your messages.
[1021.22 → 1021.36] You're like,
[1021.42 → 1023.04] oh, this belongs to another channel.
[1023.22 → 1024.34] Let me move that over there.
[1024.74 → 1026.92] It's kind of like a real-time forum in a way.
[1027.18 → 1027.68] You know,
[1027.74 → 1030.06] like when I'm on chat.zulip.org,
[1030.32 → 1033.44] it's got the feels of a forum
[1033.44 → 1036.54] and the feels of a real-time chat
[1036.54 → 1037.92] kind of combined into one,
[1038.66 → 1039.40] which is kind of nice
[1039.40 → 1040.10] because there's,
[1040.34 → 1040.52] you know,
[1040.56 → 1041.22] in forums,
[1041.36 → 1043.16] you are often threaded conversations.
[1043.16 → 1044.78] They're obviously topic-based,
[1044.78 → 1046.90] but they're not real-time generally,
[1047.14 → 1047.82] to my knowledge.
[1047.82 → 1048.00] I mean,
[1048.02 → 1048.74] I haven't been on a forum
[1048.74 → 1051.08] in like active,
[1051.22 → 1051.60] I suppose,
[1051.72 → 1053.54] since the where's days of my life.
[1053.68 → 1053.82] But,
[1053.90 → 1054.42] you know,
[1054.46 → 1055.72] I'm on forums here and there.
[1055.84 → 1057.46] I think there are some obvious ones out there,
[1057.48 → 1058.46] but it's not active in them.
[1058.68 → 1060.24] I'm very active in slacks,
[1060.88 → 1061.66] multiple slacks,
[1061.74 → 1062.44] not just our own,
[1062.76 → 1065.18] and really no discords at all for me.
[1065.64 → 1067.28] So my only really experience
[1067.28 → 1070.04] is like older hip chat days,
[1070.20 → 1071.88] obviously campfire,
[1072.16 → 1074.82] and then obviously now modern application.
[1074.82 → 1075.38] How about IRC?
[1075.46 → 1076.54] Did you ever get an IRC at all?
[1076.74 → 1077.52] A little bit,
[1077.58 → 1077.86] you know,
[1077.98 → 1078.58] a little bit.
[1078.64 → 1078.88] Honestly,
[1078.98 → 1079.18] I just,
[1079.26 → 1079.70] it was like,
[1080.10 → 1081.36] I wasn't quite hacker then
[1081.36 → 1082.30] as much as I am now.
[1082.58 → 1083.92] So I didn't quite get into IRC.
[1083.96 → 1084.62] I tried.
[1084.96 → 1085.60] I was,
[1085.68 → 1087.82] but just not like steeped.
[1087.82 → 1088.12] Sure.
[1088.28 → 1089.24] Like real-time chat is.
[1089.28 → 1089.96] But this is kind of cool
[1089.96 → 1090.90] because it's kind of like a forum
[1090.90 → 1092.16] and a real-time chat
[1092.16 → 1093.60] all built into one.
[1093.66 → 1096.04] And it doesn't feel overwhelming
[1096.04 → 1097.02] like you see this stream
[1097.02 → 1098.54] of content coming past you.
[1098.54 → 1098.82] I think,
[1099.36 → 1099.62] you know,
[1099.66 → 1100.82] there are some psychological things
[1100.82 → 1103.00] that happen in real-time chat applications
[1103.00 → 1103.40] these days
[1103.40 → 1105.34] that you feel like you have to keep up
[1105.34 → 1107.34] or there's just a stream of data.
[1107.52 → 1110.60] It doesn't feel burdening thus far.
[1111.28 → 1111.40] Yeah.
[1111.44 → 1112.48] And that's a huge thing
[1112.48 → 1113.74] we're trying to solve for as well
[1113.74 → 1115.52] to sort of feel like,
[1115.64 → 1115.74] oh,
[1115.84 → 1115.90] I,
[1116.06 → 1116.18] you know,
[1116.22 → 1116.94] somebody sent a message.
[1117.04 → 1118.50] I have to respond right now.
[1118.68 → 1119.00] Otherwise,
[1119.36 → 1120.20] nobody's going to,
[1120.36 → 1120.52] like,
[1120.54 → 1121.28] it's going to be messy.
[1121.36 → 1122.18] It's going to be confusing.
[1122.46 → 1123.52] I'm not going to be able to reply.
[1123.52 → 1124.36] How do I get back there?
[1124.58 → 1124.80] Yeah.
[1125.04 → 1125.30] Yeah,
[1125.34 → 1125.78] exactly.
[1125.78 → 1128.38] And then that disrupts people's focus time,
[1128.44 → 1129.48] even if they are online.
[1129.76 → 1129.80] Like,
[1129.88 → 1131.72] you want to be able to just dive into your work
[1131.72 → 1132.92] and focus for a couple of hours.
[1133.08 → 1134.62] And then when you need a break,
[1134.68 → 1136.14] maybe check in on your chat messages
[1136.14 → 1137.42] and follow up on stuff.
[1137.90 → 1137.98] Like,
[1138.08 → 1138.54] most of the
[1138.54 → 1140.50] most of the messages people are sending
[1140.50 → 1141.54] are probably not
[1141.54 → 1143.16] so urgent
[1143.16 → 1143.76] that you need to,
[1144.00 → 1144.26] you know,
[1144.32 → 1145.22] interrupt your flow
[1145.22 → 1146.96] to jump in right away.
[1147.66 → 1148.02] And so,
[1148.12 → 1149.72] that's part of the design here
[1149.72 → 1151.08] is that to really make it possible
[1151.08 → 1151.54] to say,
[1151.66 → 1151.80] okay,
[1151.80 → 1153.58] I'm going to dive into the code.
[1153.64 → 1155.26] I'm going to dive into my project
[1155.26 → 1156.92] and then reemerge
[1156.92 → 1158.72] and follow up on all the chats
[1158.72 → 1159.66] where I need to respond
[1159.66 → 1161.62] and then go back to what I was doing.
[1162.38 → 1164.10] The cool thing for us,
[1164.24 → 1164.38] Adam,
[1164.60 → 1166.24] if we did Zulip instead of Slack
[1166.24 → 1166.50] is,
[1166.56 → 1166.74] you know,
[1166.80 → 1167.86] it's self-hostable.
[1168.16 → 1169.58] You can also use it in their cloud
[1169.58 → 1170.54] so you can pay them money
[1170.54 → 1171.56] and they will host it for you.
[1172.62 → 1172.94] But,
[1173.52 → 1174.90] if you were just,
[1175.00 → 1176.28] I haven't looked at the cloud offerings
[1176.28 → 1178.14] or the way that it breaks out pricing wise.
[1178.30 → 1178.50] Alia,
[1178.56 → 1180.04] you can obviously catch us up with that.
[1180.16 → 1180.30] But,
[1180.96 → 1183.44] they can't hold our chat history hostage.
[1183.70 → 1183.88] You know,
[1183.94 → 1185.58] our chat history is being held hostage.
[1185.78 → 1186.20] It is.
[1186.20 → 1186.64] Inside of Slack.
[1186.64 → 1187.94] And sometimes I look at that as a plus.
[1188.10 → 1188.14] Like,
[1188.22 → 1188.40] hey,
[1188.50 → 1188.68] it's,
[1189.34 → 1189.88] who cares?
[1190.10 → 1190.26] You know,
[1190.28 → 1191.94] sometimes it's nice that things disappear.
[1192.38 → 1193.26] And other times you're like,
[1193.74 → 1193.90] no,
[1193.94 → 1196.00] I told you this 91 days ago
[1196.00 → 1199.18] and 90 days is the maximum.
[1199.60 → 1200.12] And so,
[1200.18 → 1200.58] it's gone.
[1200.74 → 1201.58] It's gone forever.
[1201.78 → 1202.88] And now we've lost that information.
[1203.24 → 1203.36] Yeah,
[1203.42 → 1203.58] well,
[1203.62 → 1205.20] now they're going to actually start erasing it
[1205.20 → 1206.10] after a year,
[1206.18 → 1206.40] I think,
[1206.46 → 1206.62] right?
[1206.90 → 1207.08] Oh,
[1207.12 → 1207.40] are they?
[1207.48 → 1207.64] Yeah,
[1207.66 → 1208.04] I don't know.
[1208.04 → 1209.56] I don't follow too closely along.
[1209.88 → 1210.02] Well,
[1210.02 → 1211.14] I've gotten a couple of those emails
[1211.14 → 1213.32] and they are scary to see.
[1214.02 → 1215.96] I was actually a little nervous
[1215.96 → 1217.32] because I was trying to quickly,
[1217.44 → 1219.30] as this topic came up in this conversation,
[1219.30 → 1220.26] to find that message
[1220.26 → 1223.32] because I do recall them seeing recently to us
[1223.32 → 1226.62] that there are some updates required by September
[1226.62 → 1227.40] or something like that
[1227.40 → 1229.98] and like final notices for X.
[1230.14 → 1230.56] And I'm like,
[1230.68 → 1231.26] like you,
[1231.32 → 1231.40] Jared,
[1231.50 → 1233.02] who cares in a way?
[1233.08 → 1233.52] But then I'm like,
[1234.26 → 1235.18] maybe I do care.
[1235.74 → 1235.90] You know,
[1235.96 → 1237.12] maybe I might care.
[1237.64 → 1237.72] Right.
[1237.88 → 1238.00] You know,
[1238.12 → 1238.86] like there's...
[1238.86 → 1240.16] You don't care until you do care.
[1240.26 → 1240.50] Right.
[1240.50 → 1240.82] And you're like,
[1240.90 → 1241.38] oh no,
[1241.44 → 1242.28] it was in the Slack
[1242.28 → 1243.16] and then it's gone now
[1243.16 → 1243.58] and you're like...
[1243.58 → 1243.70] Yeah.
[1244.42 → 1244.74] Yeah,
[1244.74 → 1245.14] I don't know.
[1245.34 → 1246.16] Do you know much about that,
[1246.24 → 1246.36] Alia?
[1246.48 → 1248.84] Like what the current state of Slack's...
[1248.84 → 1250.40] I imagine you're probably leveraging it
[1250.40 → 1250.74] in some way,
[1250.78 → 1251.22] should you perform
[1251.22 → 1251.92] or you're...
[1251.92 → 1252.80] If you're not leveraging it,
[1252.82 → 1254.78] you're getting the inbound of it,
[1254.80 → 1254.98] right?
[1255.06 → 1255.26] Well,
[1255.62 → 1256.42] we did...
[1256.42 → 1258.28] I guess maybe you guys remember
[1258.28 → 1259.84] it was a couple of years ago,
[1259.90 → 1260.30] maybe now,
[1260.38 → 1261.74] that Slack switched from
[1261.74 → 1264.24] letting folks see 10,000 messages of history
[1264.24 → 1266.74] into just 90 days
[1266.74 → 1267.58] on the free plan.
[1267.90 → 1269.96] And that was really...
[1269.96 → 1271.68] It was framed as kind of positive,
[1271.94 → 1272.92] but what we saw
[1272.92 → 1274.76] is a huge influx of folks,
[1275.42 → 1275.94] communities,
[1276.44 → 1276.76] who,
[1276.88 → 1277.78] you know,
[1277.82 → 1278.78] don't find...
[1278.78 → 1279.70] Can't afford something
[1279.70 → 1282.50] like paying for a pro plan on Slack,
[1282.98 → 1283.64] leaving Slack
[1283.64 → 1284.62] and importing their data
[1284.62 → 1285.72] and moving to Zulip.
[1286.54 → 1287.02] And,
[1287.22 → 1287.68] I mean,
[1287.72 → 1287.98] for us,
[1288.02 → 1289.56] we have a really robust
[1289.56 → 1290.96] sponsorship program
[1290.96 → 1292.24] for communities
[1292.24 → 1293.66] and open source projects,
[1293.80 → 1294.22] nonprofits,
[1295.32 → 1295.82] education,
[1296.28 → 1297.20] kind of all kinds of
[1297.20 → 1299.18] non-business uses for Zulip.
[1299.18 → 1300.14] We really try to,
[1300.14 → 1300.82] you know,
[1300.84 → 1301.78] enable folks to benefit
[1301.78 → 1302.66] from our software.
[1303.14 → 1304.36] So we do sponsor
[1304.36 → 1307.30] free Zulip cloud standard plans
[1307.30 → 1307.98] for folks.
[1308.12 → 1309.08] We have over,
[1309.26 → 1309.48] I think,
[1309.50 → 1311.94] over 1,500 sponsored organizations
[1311.94 → 1312.70] at this point.
[1312.80 → 1314.30] So it's a really robust program.
[1314.40 → 1314.96] That's quite a few.
[1315.24 → 1315.42] Yeah.
[1315.48 → 1317.10] And it's something that we're kind of...
[1317.10 → 1319.06] We really believe in Zulip
[1319.06 → 1320.38] as a way to help folks
[1320.38 → 1321.10] be more productive
[1321.10 → 1322.40] and really help them accomplish
[1322.40 → 1323.22] what they're trying to do.
[1323.28 → 1324.72] And so we don't want
[1324.72 → 1325.74] to wall that off.
[1325.78 → 1326.72] And as much as we can,
[1326.96 → 1327.22] you know,
[1327.22 → 1328.50] of course we do need businesses
[1328.50 → 1329.72] and organizations
[1329.72 → 1330.56] that can afford it
[1330.56 → 1331.56] to pay for the product.
[1331.70 → 1332.42] But otherwise,
[1332.42 → 1333.62] we really do want to share it
[1333.62 → 1334.40] as much as we can
[1334.40 → 1336.24] and like enable folks
[1336.24 → 1337.42] to do awesome things with it.
[1337.78 → 1338.08] Yeah.
[1338.36 → 1339.94] I found the email
[1339.94 → 1341.44] that was scary.
[1341.98 → 1344.84] This was sent on June 24th.
[1345.12 → 1345.90] It says,
[1346.62 → 1347.54] free workspace content
[1347.54 → 1348.46] older than one year
[1348.46 → 1349.16] will be deleted.
[1349.68 → 1351.62] And then I won't read it all,
[1351.72 → 1352.02] of course,
[1352.12 → 1352.56] but it says,
[1352.56 → 1353.46] this policy will begin
[1353.46 → 1354.08] taking effect.
[1354.18 → 1354.70] Get this, Jared.
[1355.26 → 1357.02] August 26th.
[1357.02 → 1357.26] Ooh.
[1357.62 → 1359.36] It is as ago.
[1359.54 → 1360.06] The 28th.
[1360.44 → 1360.70] Yeah.
[1360.92 → 1361.80] So as of this recording,
[1361.84 → 1363.28] we're recording on August 28th.
[1363.48 → 1364.32] They're deleting our stuff.
[1364.64 → 1365.40] But it does say,
[1365.58 → 1366.94] workspaces will be notified
[1366.94 → 1367.92] prior to the policy
[1367.92 → 1368.86] impacting that workspace.
[1369.06 → 1371.14] So we do have time.
[1371.30 → 1371.96] They haven't ruled it out yet.
[1371.96 → 1372.36] And it says,
[1372.44 → 1373.64] your workspace is on
[1373.64 → 1374.52] a free Slack plan
[1374.52 → 1374.98] because,
[1375.68 → 1375.86] Alia,
[1375.92 → 1376.56] we are a community.
[1376.90 → 1377.00] You know,
[1377.02 → 1377.56] we want our...
[1378.84 → 1379.78] We've been sort of
[1379.78 → 1380.46] hamstrung,
[1380.46 → 1381.04] I suppose,
[1381.16 → 1381.76] by Slack.
[1381.82 → 1382.58] We've always been dumb
[1382.58 → 1383.06] out of that.
[1383.72 → 1384.94] They would never have
[1384.94 → 1385.72] changed their tune
[1385.72 → 1386.94] towards communities.
[1387.50 → 1388.44] And we have
[1388.44 → 1389.94] several communities
[1389.94 → 1390.66] in our sidebar
[1390.66 → 1391.48] that I'm a part of
[1391.48 → 1391.78] and I'm sure,
[1391.90 → 1391.96] Jared,
[1392.00 → 1392.38] you're a part of
[1392.38 → 1393.00] something I'm not.
[1393.40 → 1393.94] But there's
[1393.94 → 1395.80] relationships in business.
[1396.02 → 1396.94] There are partners
[1396.94 → 1398.14] where in their channels
[1398.14 → 1398.94] or vice versa.
[1399.66 → 1401.14] And it always seemed like,
[1401.56 → 1402.24] what's the line
[1402.24 → 1403.28] from Good fellas,
[1403.36 → 1403.54] Jared?
[1404.36 → 1405.18] Maybe it was one
[1405.18 → 1406.42] of the Godfather movies.
[1406.50 → 1406.92] I don't know.
[1407.14 → 1407.40] Which one?
[1407.58 → 1408.44] It was basically
[1408.44 → 1408.90] Pay Me,
[1409.04 → 1409.46] you know?
[1409.86 → 1410.40] Oh, yeah.
[1410.60 → 1410.90] You know,
[1411.02 → 1411.38] you know what I'm
[1411.38 → 1412.00] getting at here.
[1412.18 → 1412.60] Yeah, yeah, yeah.
[1412.60 → 1413.06] It's a PG.
[1413.52 → 1414.64] It's a PG show here.
[1415.68 → 1416.56] That's how I've always
[1416.56 → 1417.34] felt about Slack.
[1417.46 → 1417.98] It's just like,
[1418.04 → 1419.98] not like great company.
[1420.06 → 1421.14] And I'm all for companies
[1421.14 → 1421.90] being ambitious
[1421.90 → 1422.84] and enterprise focused
[1422.84 → 1423.50] and all that good stuff.
[1423.56 → 1425.00] I'm not at all against that.
[1425.04 → 1426.86] But I was always confused
[1426.86 → 1429.30] by their seemingly inability
[1429.30 → 1431.82] to see the goldmine
[1431.82 → 1432.48] of community
[1432.48 → 1435.18] that had leveraged Slack
[1435.18 → 1436.04] in its free tier
[1436.04 → 1437.28] to not find a way
[1437.28 → 1438.84] to make them pay
[1438.84 → 1439.24] in some way
[1439.24 → 1439.74] that wasn't
[1439.74 → 1440.68] thousands and thousands.
[1440.88 → 1441.54] It only seemed
[1441.54 → 1442.10] to be optimized
[1442.10 → 1443.64] for the large enterprises only,
[1444.06 → 1445.56] not for the smaller communities
[1445.56 → 1446.28] at all.
[1446.28 → 1446.90] Yeah, well,
[1447.10 → 1447.46] and I guess
[1447.46 → 1448.40] our general philosophy
[1448.40 → 1449.18] on pricing is,
[1449.46 → 1449.68] you know,
[1449.74 → 1449.92] look,
[1450.00 → 1451.02] if you're a business
[1451.02 → 1452.40] and you're paying somebody
[1452.40 → 1453.00] a salary,
[1453.86 → 1456.30] paying a small monthly fee
[1456.30 → 1457.14] for that user,
[1457.68 → 1457.86] you know,
[1457.90 → 1458.70] a few dollars a month
[1458.70 → 1460.38] to provide chat,
[1460.62 → 1461.28] you know,
[1461.36 → 1463.10] have them have chat software
[1463.10 → 1463.94] that they use
[1463.94 → 1465.16] hours every day.
[1465.16 → 1466.08] And in our case,
[1466.08 → 1467.02] that can help them
[1467.02 → 1468.12] be more efficient
[1468.12 → 1468.92] with their time.
[1469.08 → 1470.38] That's just so worth it
[1470.38 → 1471.68] and it's a very reasonable
[1471.68 → 1473.06] way to do things.
[1473.70 → 1474.46] But if you're looking
[1474.46 → 1475.32] at an organization
[1475.32 → 1477.54] where the folks using chat
[1477.54 → 1479.12] are not your employees,
[1479.40 → 1480.36] so even if there's
[1480.36 → 1481.26] some kind of core,
[1481.64 → 1482.52] employee core,
[1482.70 → 1483.66] a few folks
[1483.66 → 1484.44] who are part of a business,
[1484.56 → 1485.40] but then you have
[1485.40 → 1486.74] a large community
[1486.74 → 1488.20] that's part of that organization,
[1488.62 → 1489.34] now the pricing
[1489.34 → 1490.20] doesn't make any sense
[1490.20 → 1490.70] at all.
[1490.70 → 1492.12] And so that's,
[1492.24 → 1492.38] you know,
[1492.42 → 1493.54] folks can contact
[1493.54 → 1495.28] our sales team
[1495.28 → 1496.88] for their specific situation,
[1497.04 → 1498.12] but in general
[1498.12 → 1499.08] our approach is really,
[1499.20 → 1499.40] you know,
[1499.88 → 1500.34] businesses,
[1500.70 → 1501.30] it makes sense
[1501.30 → 1502.92] to pay that kind of level,
[1503.16 → 1505.46] but not for community members
[1505.46 → 1506.24] even if there's
[1506.24 → 1507.04] a business involved.
[1508.18 → 1508.20] Plus,
[1508.46 → 1508.76] it's,
[1509.38 → 1509.90] if you're doing
[1509.90 → 1510.92] long-term thinking,
[1511.30 → 1511.96] the way you all
[1511.96 → 1512.66] are doing it
[1512.66 → 1513.98] builds value
[1513.98 → 1515.58] over the long run
[1515.58 → 1517.22] because the price
[1517.22 → 1517.92] of you all
[1517.92 → 1518.88] providing these
[1518.88 → 1519.80] standard plans
[1519.80 → 1520.12] for,
[1520.24 → 1520.62] at this point,
[1520.70 → 1521.92] 1,500 organizations
[1521.92 → 1523.94] which are community-focused,
[1524.58 → 1525.14] nonprofits,
[1525.88 → 1526.60] open source,
[1526.94 → 1527.48] research,
[1528.40 → 1528.80] academia,
[1529.04 → 1529.32] et cetera.
[1529.92 → 1530.78] These are people
[1530.78 → 1533.08] who will use
[1533.08 → 1534.18] and love your product
[1534.18 → 1534.98] and it will help
[1534.98 → 1536.84] generate a network effect
[1536.84 → 1537.70] you would hope
[1537.70 → 1539.00] that would eventually
[1539.00 → 1540.76] bring their business
[1540.76 → 1541.28] to Zulip,
[1541.42 → 1541.70] you know,
[1541.86 → 1542.40] their,
[1542.54 → 1543.88] their friends' business
[1543.88 → 1544.76] when they go to ask them
[1544.76 → 1545.48] for a recommendation
[1545.48 → 1546.60] to Zulip
[1546.60 → 1547.78] who becomes a paying customer.
[1548.12 → 1549.82] And that stuff doesn't
[1549.82 → 1550.24] pay off
[1550.24 → 1550.74] in the quarterly
[1550.74 → 1551.12] or sometimes
[1551.12 → 1551.88] even the yearly
[1551.88 → 1552.54] because you're actually
[1552.54 → 1553.10] losing money
[1553.10 → 1553.90] by giving this away
[1553.90 → 1554.42] to more people.
[1554.42 → 1554.84] But like,
[1554.96 → 1555.22] on the
[1555.28 → 1556.42] on the measuring
[1556.42 → 1556.98] 10 years,
[1557.14 → 1557.58] 15 years,
[1557.64 → 1558.68] 20 years down the road,
[1559.36 → 1560.50] that stuff compounds
[1560.50 → 1562.36] and becomes massive.
[1562.36 → 1563.64] And it's something
[1563.64 → 1564.34] that Slack
[1564.34 → 1565.74] I think currently
[1565.74 → 1566.78] has to a certain extent
[1566.78 → 1567.88] is some network effects
[1567.88 → 1568.46] where it's like
[1568.46 → 1569.60] people already have
[1569.60 → 1570.16] a Slack app
[1570.16 → 1570.64] on their phone
[1570.64 → 1571.24] and so it's easy
[1571.24 → 1572.38] to add another Slack.
[1572.38 → 1572.84] in fact,
[1573.50 → 1574.24] yet another Slack
[1574.24 → 1575.10] is kind of a fatigue
[1575.10 → 1575.56] at this point.
[1575.68 → 1575.74] Like,
[1575.80 → 1575.90] oh,
[1575.92 → 1576.76] I have so many Slacks,
[1576.84 → 1577.26] I don't want to have
[1577.26 → 1577.78] another Slack.
[1577.94 → 1579.24] But it's a big advantage
[1579.24 → 1580.16] when it comes to
[1580.16 → 1581.10] getting people
[1581.10 → 1581.82] to use the tool
[1581.82 → 1582.90] if they've already used it,
[1582.96 → 1583.78] if they already have it
[1583.78 → 1584.32] on their phone
[1584.32 → 1585.10] or on their laptop.
[1586.02 → 1586.70] And so what you're doing
[1586.70 → 1587.28] is you're getting
[1587.28 → 1588.12] Zulip out there
[1588.12 → 1589.20] for these people
[1589.20 → 1590.00] and you're doing
[1590.00 → 1591.74] good at the same time.
[1591.82 → 1592.84] So I applaud that
[1592.84 → 1593.80] strategy.
[1594.36 → 1594.46] Yeah,
[1594.50 → 1594.86] absolutely.
[1595.12 → 1595.26] Like,
[1595.32 → 1596.52] we definitely see folks
[1596.52 → 1596.88] saying,
[1597.00 → 1597.08] oh,
[1597.12 → 1597.68] I use it in,
[1598.02 → 1598.54] we ask folks
[1598.54 → 1599.46] how they,
[1599.88 → 1600.56] who are creating
[1600.56 → 1601.44] new Zulip organizations,
[1601.60 → 1602.26] how they learned
[1602.26 → 1602.74] about Zulip
[1602.74 → 1603.50] and a lot of them say,
[1603.62 → 1604.12] I've used it
[1604.12 → 1605.46] in a Zulip organization
[1605.46 → 1606.60] before and I think
[1606.60 → 1607.42] a lot of the time
[1607.42 → 1608.28] that will be
[1608.28 → 1609.06] like an open source
[1609.06 → 1610.16] community somewhere.
[1610.98 → 1611.46] And also,
[1611.78 → 1612.06] you know,
[1612.08 → 1613.02] another way that
[1613.02 → 1614.12] folks from these
[1614.12 → 1615.28] communities are really
[1615.28 → 1616.54] contributing is that
[1616.54 → 1617.46] we get a ton
[1617.46 → 1618.28] of user feedback.
[1618.60 → 1619.88] So as you saw,
[1620.04 → 1621.04] our development community
[1621.04 → 1621.52] is open
[1621.52 → 1623.08] and it's open signups.
[1623.08 → 1624.80] So folks will just
[1624.80 → 1625.92] come and come by
[1625.92 → 1627.10] and kind of share
[1627.10 → 1628.22] how they're using Zulip,
[1628.34 → 1628.78] what they think
[1628.78 → 1629.80] could work better,
[1630.00 → 1630.86] any kind of bugs
[1630.86 → 1631.42] they encounter,
[1631.60 → 1632.36] but also feature,
[1632.46 → 1633.48] feature requests
[1633.48 → 1634.82] as well as like
[1634.82 → 1635.46] just posting
[1635.46 → 1636.46] and proposing
[1636.46 → 1637.96] feature ideas
[1637.96 → 1638.40] on GitHub.
[1639.12 → 1640.66] And we just have
[1640.66 → 1641.28] these like really
[1641.28 → 1642.12] open discussions
[1642.12 → 1643.60] with our users
[1643.60 → 1644.78] and that's really
[1644.78 → 1645.74] valuable for just
[1645.74 → 1647.10] figuring out the ways
[1647.10 → 1648.30] that we can improve
[1648.30 → 1648.88] the product.
[1649.78 → 1650.14] So when it comes
[1650.14 → 1650.84] to Slack, Adam,
[1650.90 → 1651.36] you and I have
[1651.36 → 1651.80] kind of have
[1651.80 → 1652.64] maybe two
[1652.64 → 1653.96] values
[1653.96 → 1654.82] that they hit
[1654.82 → 1655.52] on one of them.
[1655.60 → 1656.26] One of them's like
[1656.26 → 1658.14] high quality software
[1658.14 → 1658.70] and design,
[1658.90 → 1659.50] like that's a thing
[1659.50 → 1660.34] that we both care about.
[1660.84 → 1661.82] And then the other ones
[1661.82 → 1663.32] like open source
[1663.32 → 1664.98] community ethos,
[1665.16 → 1665.86] which Slack
[1665.86 → 1666.98] does not have.
[1667.52 → 1667.96] And so they have
[1667.96 → 1668.68] kind of one of both.
[1668.76 → 1670.06] We like to have them both.
[1671.10 → 1671.32] And,
[1671.40 → 1672.18] you know,
[1672.32 → 1673.36] high quality software
[1673.36 → 1673.84] and Slack,
[1673.98 → 1674.24] I think,
[1675.06 → 1675.56] I think that's more
[1675.56 → 1676.18] questionable now
[1676.18 → 1676.72] than it used to be.
[1676.74 → 1677.64] I think they really did
[1677.64 → 1678.58] hit it out of the park
[1678.58 → 1679.36] in certain ways
[1679.36 → 1681.12] and were groundbreaking
[1681.12 → 1682.52] in certain ways.
[1683.52 → 1683.90] Recently,
[1683.90 → 1685.12] I've been less impressed
[1685.12 → 1686.60] after some redesigns
[1686.60 → 1687.36] and I feel like it's
[1687.36 → 1688.10] kind of stagnated.
[1688.22 → 1688.48] Of course,
[1688.54 → 1689.60] they've arrived.
[1690.32 → 1690.48] You know,
[1690.54 → 1691.42] they are now part of
[1691.42 → 1691.80] Salesforce
[1691.80 → 1692.74] and a big company
[1692.74 → 1693.18] and all that
[1693.18 → 1693.62] and they have
[1693.62 → 1695.14] other people
[1695.14 → 1695.72] in their minds
[1695.72 → 1696.56] that aren't use.
[1696.98 → 1697.24] But,
[1697.48 → 1699.54] I'm curious about Zulip
[1699.54 → 1700.30] when it comes to
[1700.30 → 1700.94] the software
[1700.94 → 1702.04] and the way
[1702.04 → 1702.84] it all works
[1702.84 → 1704.86] and does it fit
[1704.86 → 1706.02] into all the different
[1706.02 → 1707.08] places that you communicate?
[1708.16 → 1708.56] Because,
[1708.74 → 1709.26] more often,
[1709.36 → 1710.10] I'm using Slack
[1710.10 → 1710.84] on my phone even,
[1710.96 → 1712.04] even though I stand
[1712.04 → 1712.50] at my desk
[1712.50 → 1713.56] for hours every day.
[1713.96 → 1714.58] You communicate
[1714.58 → 1715.24] all day long
[1715.24 → 1715.88] and all night long.
[1716.66 → 1717.28] And so,
[1717.60 → 1718.58] Zulip on the phones,
[1718.90 → 1719.68] Android iOS,
[1720.36 → 1721.76] Zulip on the web,
[1721.86 → 1722.46] Zulip apps,
[1722.52 → 1722.64] like,
[1722.68 → 1723.14] do you have
[1723.14 → 1724.18] all that
[1724.18 → 1726.14] necessary surface area
[1726.14 → 1727.10] accounted for
[1727.10 → 1727.60] and how do you all
[1727.60 → 1728.10] manage that?
[1728.48 → 1728.62] Yeah,
[1728.66 → 1728.98] absolutely.
[1728.98 → 1729.42] So,
[1729.78 → 1730.08] Zulip,
[1730.16 → 1730.88] you can use it
[1730.88 → 1732.30] just in a browser tab.
[1732.84 → 1733.26] There's also
[1733.26 → 1734.50] a desktop app
[1734.50 → 1735.92] for all the major platforms.
[1736.74 → 1737.16] And then,
[1737.24 → 1737.42] yeah,
[1737.50 → 1739.04] Android and iOS apps.
[1739.20 → 1739.80] And we're actually
[1739.80 → 1741.48] currently in the process
[1741.48 → 1743.16] of re-rating
[1743.16 → 1745.08] our mobile apps
[1745.08 → 1745.96] from the ground up
[1745.96 → 1747.44] using a different framework.
[1747.44 → 1748.26] We're switching to
[1748.26 → 1749.76] Flutter-based apps.
[1750.22 → 1750.40] So,
[1750.92 → 1751.52] our current apps
[1751.52 → 1751.94] are definitely
[1751.94 → 1752.96] functional
[1752.96 → 1754.16] but not as
[1754.16 → 1755.14] sort of
[1755.14 → 1756.22] smooth and beautiful
[1756.22 → 1757.28] as we would like them to be.
[1757.28 → 1757.80] And so,
[1758.32 → 1759.46] that next generation app
[1759.46 → 1760.40] is really going to get us
[1760.40 → 1761.08] all the way there.
[1761.16 → 1761.26] So,
[1761.30 → 1762.28] we're very excited for it.
[1763.18 → 1763.88] And for
[1763.88 → 1765.00] sort of
[1765.00 → 1765.62] old school folks
[1765.62 → 1765.98] out there,
[1766.08 → 1766.48] there's also
[1766.48 → 1767.04] Terminal
[1767.04 → 1768.78] Client for Zulip
[1768.78 → 1770.32] if anybody wants
[1770.32 → 1770.96] to use it that way.
[1771.18 → 1771.98] How about API?
[1772.12 → 1772.76] Is it programmable?
[1773.08 → 1773.24] Yeah,
[1773.30 → 1774.24] there's an open API
[1774.24 → 1774.68] and actually
[1774.68 → 1776.04] our mobile
[1776.04 → 1776.86] and terminal apps
[1776.86 → 1778.90] use the API
[1778.90 → 1779.80] to communicate
[1779.80 → 1780.42] with the servers.
[1780.68 → 1780.90] So,
[1781.28 → 1782.06] we're constantly
[1782.06 → 1782.56] kind of
[1782.56 → 1783.58] testing it ourselves
[1783.58 → 1784.50] and using it ourselves
[1784.50 → 1785.52] and relying on that
[1785.52 → 1786.70] documentation ourselves.
[1786.70 → 1787.12] So,
[1787.96 → 1788.58] absolutely.
[1789.50 → 1790.12] Is the desktop
[1790.12 → 1790.78] app
[1790.78 → 1791.74] an Electron app?
[1791.92 → 1792.44] It is,
[1792.50 → 1792.72] yes.
[1793.04 → 1793.82] Have you considered
[1793.82 → 1794.62] a Tori app?
[1794.88 → 1795.38] My understanding
[1795.38 → 1796.28] is that the engineering team
[1796.28 → 1797.20] was thinking about it
[1797.20 → 1798.10] and was kind of
[1798.10 → 1799.28] waiting for...
[1799.28 → 1799.88] Because if you wanted
[1799.88 → 1800.92] to get the nerds excited,
[1801.28 → 1801.72] I think,
[1801.76 → 1802.36] if you came out
[1802.36 → 1802.70] and said,
[1802.78 → 1804.16] Zulip's desktop app
[1804.16 → 1804.76] is now
[1804.76 → 1806.44] no longer using
[1806.44 → 1806.98] Electron,
[1807.82 → 1808.58] then it would be like,
[1808.72 → 1809.64] we'd just throw slack
[1809.64 → 1810.16] right out the window.
[1810.26 → 1810.68] Wouldn't we, Adam?
[1810.84 → 1811.62] All of us nerds
[1811.62 → 1811.98] would be like,
[1812.20 → 1812.48] ah,
[1812.54 → 1812.86] finally,
[1812.96 → 1813.94] something we can use here.
[1814.26 → 1814.54] Yeah,
[1814.60 → 1815.16] pretty much.
[1827.96 → 1828.36] Okay,
[1828.46 → 1828.68] friends,
[1828.72 → 1829.30] I'm here in the breaks
[1829.30 → 1830.24] with Annie Sexton
[1830.24 → 1831.78] over at Fly.
[1832.14 → 1832.36] Annie,
[1832.44 → 1833.38] you know we use
[1833.38 → 1834.72] Fly here at Change Law.
[1834.74 → 1835.74] We love Fly.
[1836.06 → 1837.62] It is such an awesome platform
[1837.62 → 1838.60] and we love building on it.
[1838.64 → 1838.80] But,
[1838.94 → 1839.88] for those who don't know
[1839.88 → 1840.98] much about Fly,
[1841.20 → 1842.30] what's special
[1842.30 → 1843.90] about building on Fly?
[1844.22 → 1844.78] Fly gives you
[1844.78 → 1845.94] a lot of flexibility.
[1846.50 → 1846.68] Like,
[1846.72 → 1847.76] a lot of flexibility
[1847.76 → 1848.96] on multiple fronts.
[1849.36 → 1850.14] And on top of that,
[1850.22 → 1850.68] you get,
[1851.20 → 1852.16] so I've talked a lot
[1852.16 → 1853.26] about the networking
[1853.26 → 1854.28] and that's obviously
[1854.28 → 1854.88] one thing,
[1855.04 → 1856.30] but there's
[1856.30 → 1857.48] various data stores
[1857.48 → 1858.56] that we partner with
[1858.56 → 1859.30] that are really easy
[1859.30 → 1859.98] to use.
[1860.52 → 1860.96] Actually,
[1861.08 → 1862.20] one of my favourite
[1862.20 → 1863.94] partners is Tigress.
[1864.12 → 1864.84] I can't say enough
[1864.84 → 1865.78] good things about them
[1865.78 → 1866.98] when it comes to
[1866.98 → 1867.68] object storage.
[1867.88 → 1869.26] I've never in my life
[1869.26 → 1869.84] thought I would have
[1869.84 → 1870.46] so many opinions
[1870.46 → 1871.28] about object storage,
[1871.40 → 1872.04] but I do now.
[1872.30 → 1873.68] Tigress is a partner
[1873.68 → 1874.18] of Fly,
[1874.42 → 1875.24] and it's S3
[1875.24 → 1876.52] compatible object storage
[1876.52 → 1877.66] that basically
[1877.66 → 1879.32] seems like it's a CDN,
[1879.42 → 1880.14] but it's not.
[1880.20 → 1881.36] It's basically object storage
[1881.36 → 1882.84] that's globally distributed
[1882.84 → 1883.90] without needing
[1883.90 → 1884.70] to actually set up
[1884.70 → 1885.64] a CDN at all.
[1885.74 → 1886.88] It's like automatically
[1886.88 → 1888.52] distributed around the world.
[1888.84 → 1889.48] And it's also
[1889.48 → 1891.24] incredibly easy
[1891.24 → 1892.18] to use and set up.
[1892.34 → 1892.42] Like,
[1892.46 → 1893.02] creating a bucket
[1893.02 → 1894.52] is literally one command.
[1894.78 → 1895.48] So it's partners
[1895.48 → 1896.04] like that
[1896.04 → 1896.76] that I think
[1896.76 → 1897.64] are this sort of
[1897.64 → 1899.10] extra icing on top
[1899.10 → 1899.42] of Fly
[1899.42 → 1899.98] that really
[1899.98 → 1901.28] makes it sort of
[1901.28 → 1902.04] the platform
[1902.04 → 1902.66] that has everything
[1902.66 → 1903.20] that you need.
[1903.66 → 1904.24] So we use Tigress
[1904.24 → 1905.66] here at Changelog.
[1905.76 → 1906.38] Are they built
[1906.38 → 1907.20] on top of Fly?
[1907.46 → 1908.10] Is this one of those
[1908.10 → 1909.28] examples of being
[1909.28 → 1909.90] able to build
[1909.90 → 1910.64] on Fly?
[1911.06 → 1911.30] Yeah,
[1911.38 → 1912.44] so Tigress is built
[1912.44 → 1913.42] on top of Fly's
[1913.42 → 1914.04] infrastructure,
[1914.04 → 1914.98] and that's what allows
[1914.98 → 1915.72] it to be globally
[1915.72 → 1916.28] distributed.
[1916.68 → 1917.30] I do have a video
[1917.30 → 1917.62] on this,
[1917.76 → 1918.52] but basically
[1918.52 → 1919.44] the way it works
[1919.44 → 1920.46] is whenever,
[1920.90 → 1921.12] like,
[1921.16 → 1922.16] let's say a user
[1922.16 → 1923.42] uploads an asset
[1923.42 → 1925.14] to a particular bucket.
[1925.26 → 1925.36] Well,
[1925.40 → 1926.28] that gets uploaded
[1926.28 → 1928.10] directly to the region
[1928.10 → 1929.20] closest to the user,
[1929.30 → 1930.14] whereas with a CDN,
[1930.20 → 1930.58] there's sort of like
[1930.58 → 1931.50] a centralized place
[1931.50 → 1932.56] where assets need
[1932.56 → 1933.28] to get copied to,
[1933.36 → 1933.92] and then eventually
[1933.92 → 1934.54] they get sort of
[1934.54 → 1935.24] trickled out to
[1935.24 → 1936.28] all the different
[1936.28 → 1937.14] global locations,
[1937.28 → 1937.94] whereas with Tigress,
[1938.06 → 1939.16] the moment you upload
[1939.16 → 1939.62] something,
[1939.92 → 1940.76] it's available in that
[1940.76 → 1941.46] region instantly,
[1941.82 → 1942.72] and then it's eventually
[1942.72 → 1943.68] cached in all the other
[1943.68 → 1944.32] regions as well
[1944.32 → 1945.42] as it's requested.
[1945.82 → 1946.14] In fact,
[1946.26 → 1946.80] with Tigress,
[1946.90 → 1947.68] you don't even have to
[1947.68 → 1948.90] select which regions
[1948.90 → 1950.00] things are stored in.
[1950.08 → 1950.80] You just get these
[1950.80 → 1951.68] regions for free.
[1951.92 → 1952.82] And then on top of that,
[1953.16 → 1954.40] it is so much easier
[1954.40 → 1955.10] to work with.
[1955.34 → 1956.86] I feel like the way
[1956.86 → 1958.42] they manage permissions,
[1958.78 → 1959.92] the way they handle
[1959.92 → 1960.84] bucket creation,
[1961.04 → 1961.76] making things public
[1961.76 → 1962.20] or private,
[1962.24 → 1964.14] is just so much simpler
[1964.14 → 1966.02] than other solutions.
[1966.64 → 1967.52] And the good news is
[1967.52 → 1968.16] that you don't actually
[1968.16 → 1969.08] need to change your code
[1969.08 → 1969.58] if you're already
[1969.58 → 1970.24] using S3.
[1970.40 → 1971.30] It's S3 compatible,
[1971.48 → 1972.48] so whatever SDK
[1972.48 → 1972.96] you're using
[1972.96 → 1974.18] is probably just fine,
[1974.24 → 1974.86] and all you've got to do
[1974.86 → 1975.74] is updated the credentials.
[1975.98 → 1977.60] So it's super easy.
[1978.10 → 1978.54] Very cool.
[1978.62 → 1979.00] Thanks, Annie.
[1979.16 → 1980.62] So Fly has everything
[1980.62 → 1981.46] you need.
[1981.54 → 1983.24] Over 3 million applications,
[1983.56 → 1984.42] including ours,
[1984.42 → 1985.36] here at Changelog,
[1985.42 → 1986.20] multiple applications,
[1986.20 → 1987.98] have launched on Fly.
[1988.36 → 1989.76] Boosted by global
[1989.76 → 1991.16] anti-cast load balancing,
[1991.68 → 1992.56] zero configuration
[1992.56 → 1993.54] private networking,
[1993.96 → 1995.02] hardware isolation,
[1995.62 → 1996.64] instant wire guard
[1996.64 → 1997.64] VPN connections,
[1998.10 → 1999.04] push button deployments
[1999.04 → 1999.92] that scale to thousands
[1999.92 → 2000.50] of instances,
[2000.86 → 2002.10] it's all there for you
[2002.10 → 2002.82] right now.
[2003.20 → 2003.66] Deploy your app
[2003.66 → 2004.38] in five minutes,
[2004.52 → 2006.50] go to fly.io.
[2007.00 → 2008.88] Again, fly.io.
[2009.38 → 2010.34] And by our friends
[2010.34 → 2011.52] over at Paragon,
[2011.70 → 2013.26] use paragon.com.
[2013.32 → 2013.86] Check them out.
[2014.06 → 2015.88] Ship every SaaS integration
[2015.88 → 2017.10] your users need.
[2017.22 → 2018.36] With more than 100 plus
[2018.36 → 2019.20] pre-built connectors,
[2019.62 → 2020.52] you can add dozens
[2020.52 → 2021.82] of integrations to your app
[2021.82 → 2023.06] quickly and reliably
[2023.06 → 2024.26] with their embedded
[2024.26 → 2025.34] pass for developers.
[2026.00 → 2026.42] And I'm here with
[2026.42 → 2027.64] co-founder and CEO,
[2027.80 → 2028.28] Brandon FM.
[2028.84 → 2029.18] So Brandon,
[2029.24 → 2029.82] talk to me about
[2029.82 → 2031.22] the friction developers
[2031.22 → 2032.94] feel with integrations,
[2033.32 → 2034.08] SSO,
[2034.32 → 2035.64] dealing with rate limits,
[2036.10 → 2036.76] retries,
[2036.96 → 2037.28] auth,
[2037.62 → 2038.32] all the things.
[2038.82 → 2039.04] Yeah.
[2039.22 → 2040.52] So there's a lot here
[2040.52 → 2041.02] and I think there's
[2041.02 → 2041.92] a lot of aspects
[2041.92 → 2043.74] to the different problems
[2043.74 → 2044.84] that you have to solve
[2044.84 → 2046.30] in the integration story
[2046.30 → 2047.76] in building these integrations
[2047.76 → 2049.10] and also providing them
[2049.10 → 2050.96] in a user-friendly way
[2050.96 → 2051.78] for your customers
[2051.78 → 2052.80] to self-serve
[2052.80 → 2053.48] and onboard
[2053.48 → 2054.90] and consume those integrations.
[2055.26 → 2056.04] So part of what
[2056.04 → 2057.34] the Paragon SDK provides
[2057.34 → 2058.22] is that embedded
[2058.22 → 2059.22] user experience,
[2059.40 → 2060.08] again, what we call
[2060.08 → 2060.82] our connect portal.
[2060.98 → 2061.80] That's going to provide
[2061.80 → 2062.38] the authentication
[2062.38 → 2063.26] for your users
[2063.26 → 2064.90] to connect their accounts.
[2065.10 → 2065.56] That's going to be
[2065.56 → 2066.56] the initial onboarding.
[2066.78 → 2067.64] But in addition to that,
[2067.80 → 2069.32] your users may also want
[2069.32 → 2070.60] to configure different options
[2070.60 → 2071.14] or settings
[2071.14 → 2072.04] for their integrations.
[2072.26 → 2072.96] A common example
[2072.96 → 2074.36] that we see for Salesforce
[2074.36 → 2075.70] or for CRM integrations
[2075.70 → 2076.20] in general
[2076.20 → 2077.06] is that your users
[2077.06 → 2078.18] may want to select
[2078.18 → 2078.90] some type of
[2078.90 → 2080.02] custom object mapping.
[2080.24 → 2080.86] Every CRM
[2080.86 → 2081.94] can be configured differently,
[2082.36 → 2083.10] so your users
[2083.10 → 2084.40] might want to map objects
[2084.40 → 2085.46] to some different
[2085.46 → 2086.26] type of record
[2086.26 → 2086.92] in their Salesforce.
[2086.92 → 2088.12] or different fields
[2088.12 → 2088.78] in their Salesforce.
[2089.46 → 2089.98] And typically,
[2090.18 → 2091.08] that's what developers
[2091.08 → 2091.88] would have to build
[2091.88 → 2092.58] on their own,
[2092.94 → 2093.68] is this UI
[2093.68 → 2094.82] for your users
[2094.82 → 2095.70] to configure
[2095.70 → 2096.80] these different settings
[2096.80 → 2098.16] for every single integration.
[2098.50 → 2099.50] That's also going to be
[2099.50 → 2100.12] what's provided
[2100.12 → 2101.24] by the Paragon SDK,
[2101.56 → 2102.42] is not just that
[2102.42 → 2103.38] initial onboarding
[2103.38 → 2104.64] and authentication experience,
[2104.80 → 2106.56] but also the configuration
[2106.56 → 2108.26] end-user UX
[2108.26 → 2110.18] for different settings
[2110.18 → 2111.62] like custom field mapping,
[2112.16 → 2113.36] selecting which types
[2113.36 → 2113.90] of features
[2113.90 → 2114.88] on your integration
[2114.88 → 2115.66] that your user
[2115.66 → 2116.54] might want to configure.
[2117.32 → 2118.28] And that's also
[2118.28 → 2118.98] going to be provided
[2118.98 → 2120.14] fully out of the box
[2120.14 → 2121.58] by Paragon SDK.
[2121.98 → 2122.98] With integrations,
[2123.16 → 2123.86] different APIs
[2123.86 → 2125.54] might have different rate limits,
[2125.70 → 2126.30] they might have
[2126.30 → 2127.10] different policies
[2127.10 → 2128.52] that you have to conform with,
[2128.52 → 2129.46] and your developers
[2129.46 → 2130.80] typically have to learn
[2130.80 → 2131.78] these different nuances
[2131.78 → 2132.64] for every API
[2132.64 → 2134.14] and write code individually
[2134.14 → 2135.00] to conform
[2135.00 → 2136.66] to those different nuances.
[2137.04 → 2137.56] With Paragon,
[2137.88 → 2138.92] because we build
[2138.92 → 2139.56] and maintain
[2139.56 → 2140.18] the connector
[2140.18 → 2141.88] with each of the integrations
[2141.88 → 2142.46] integrations
[2142.46 → 2143.02] that we support
[2143.02 → 2143.58] in our catalogue,
[2143.88 → 2144.70] we're automatically
[2144.70 → 2145.42] going to handle
[2145.42 → 2147.24] for things like retries,
[2147.44 → 2148.56] things like rate limits.
[2148.84 → 2149.58] And so we look at this
[2149.58 → 2150.48] as sort of the back-end
[2150.48 → 2152.04] or infrastructure layer
[2152.04 → 2153.58] of the integration problem
[2153.58 → 2154.52] that we have spent
[2154.52 → 2155.46] the last five years
[2155.46 → 2156.38] essentially building
[2156.38 → 2157.50] and optimizing
[2157.50 → 2158.70] the Paragon infrastructure
[2158.70 → 2159.64] to act
[2159.64 → 2161.88] as the integration infrastructure
[2161.88 → 2163.04] for your application.
[2163.44 → 2165.10] Okay, Paragon is built
[2165.10 → 2165.96] for product management,
[2166.52 → 2167.44] it's built for engineering,
[2167.62 → 2168.46] it's built for everybody.
[2168.74 → 2169.20] Ship hundreds
[2169.20 → 2170.74] of native integrations
[2170.74 → 2172.16] into your SaaS application
[2172.16 → 2173.40] in days
[2173.40 → 2174.26] or build your own
[2174.26 → 2174.90] custom connector
[2174.90 → 2175.96] with any API.
[2176.72 → 2177.56] Learn more at
[2177.56 → 2179.06] useparagon.com
[2179.06 → 2180.18] slash changelog.
[2180.32 → 2180.92] Again,
[2181.34 → 2183.10] useparagon.com
[2183.10 → 2183.96] slash changelog,
[2184.02 → 2187.74] that's U-S-E-P-A-R-A-G-O-N
[2187.74 → 2188.74] dot com
[2188.74 → 2190.38] slash changelog.
[2199.20 → 2208.30] What are some of the biggest
[2208.30 → 2209.64] challenges you all are facing?
[2210.28 → 2210.86] Good question.
[2211.02 → 2211.32] I guess,
[2211.84 → 2212.02] I mean,
[2212.06 → 2213.04] one sort of thing
[2213.04 → 2215.24] that is complex for us
[2215.24 → 2216.82] is the competitive landscape.
[2217.78 → 2220.10] Slack and Microsoft Teams
[2220.10 → 2221.40] being the sort of
[2221.40 → 2222.46] big gorillas
[2222.46 → 2223.48] in the room
[2223.48 → 2225.14] and Teams effectively
[2225.14 → 2226.88] gives away their chat
[2226.88 → 2227.76] for free
[2227.76 → 2228.70] and oftentimes
[2228.70 → 2230.32] kind of as part of their
[2230.32 → 2231.22] suite,
[2231.36 → 2232.04] Microsoft suite
[2232.04 → 2233.14] and it's really hard to
[2233.14 → 2234.76] get folks
[2234.76 → 2235.38] kind of,
[2235.58 → 2235.68] and,
[2235.80 → 2236.22] you know,
[2236.28 → 2237.80] at the same time that
[2237.80 → 2239.62] it's free,
[2240.28 → 2241.16] it's not free,
[2241.26 → 2241.50] right,
[2241.58 → 2242.52] in the sense that people
[2242.52 → 2243.56] are spending their time
[2243.56 → 2244.32] and their energy
[2244.32 → 2245.14] and their attention
[2245.14 → 2246.82] in ways that
[2246.82 → 2248.02] aren't making them
[2248.02 → 2248.72] productive,
[2249.04 → 2249.22] you know,
[2249.26 → 2250.22] like they're wasting,
[2250.70 → 2251.74] your employee's time
[2251.74 → 2253.18] is your most valuable resource
[2253.18 → 2253.78] and so,
[2254.96 → 2255.20] you know,
[2255.28 → 2256.24] wasting that time
[2256.24 → 2257.38] and energy
[2257.38 → 2258.56] on an app
[2258.56 → 2259.50] that's frustrating
[2259.50 → 2260.46] or hard to use
[2260.46 → 2261.36] or is not organized
[2261.36 → 2262.82] in ways that you'd want it to be
[2262.82 → 2264.70] is a major cost,
[2264.80 → 2265.82] but it's hard for companies
[2265.82 → 2267.54] to budget it that way
[2267.54 → 2269.26] and to really evaluate it that way.
[2269.78 → 2270.90] So I think one thing
[2270.90 → 2271.68] we're really trying to do
[2271.68 → 2271.88] is,
[2271.96 → 2272.30] you know,
[2272.46 → 2273.36] like get better
[2273.36 → 2274.24] at telling that story
[2274.24 → 2276.08] and really communicating
[2276.08 → 2276.68] with folks
[2276.68 → 2278.22] and trying to explain this,
[2278.78 → 2278.94] you know,
[2279.00 → 2280.02] like make people really
[2280.02 → 2281.08] sort of feel in their guts
[2281.08 → 2281.84] this sort of,
[2282.32 → 2282.56] okay,
[2282.66 → 2282.92] you know,
[2282.98 → 2284.82] this app might be free
[2284.82 → 2285.46] or it might be
[2285.46 → 2286.42] kind of easy choice
[2286.42 → 2286.90] like Slack
[2286.90 → 2287.30] for most,
[2287.42 → 2287.94] a lot of folks
[2287.94 → 2288.84] are familiar with it.
[2289.40 → 2289.60] You know,
[2289.72 → 2290.62] it's sort of like,
[2290.92 → 2291.12] you know,
[2291.16 → 2291.82] nobody got fired
[2291.82 → 2292.54] for buying IBM,
[2292.72 → 2293.72] probably nobody got fired
[2293.72 → 2294.86] for picking Slack
[2294.86 → 2295.84] for their chat
[2295.84 → 2297.00] and there are lots of things
[2297.00 → 2297.32] that are,
[2297.32 → 2297.68] that are,
[2297.72 → 2297.86] you know,
[2297.86 → 2298.48] great about it
[2298.48 → 2299.38] compared to sort of
[2299.38 → 2300.46] products that could come
[2300.46 → 2300.96] previously,
[2300.96 → 2302.78] but choosing a chat app
[2302.78 → 2304.50] is just so important
[2304.50 → 2305.38] to how folks
[2305.38 → 2306.06] are going to collaborate
[2306.06 → 2306.96] in your organization
[2306.96 → 2307.70] and so
[2307.70 → 2308.98] that's really the message
[2308.98 → 2309.78] we're like trying
[2309.78 → 2310.46] to get across
[2310.46 → 2312.82] and that's kind of,
[2312.82 → 2313.04] I think,
[2313.14 → 2315.22] kind of big challenge
[2315.22 → 2315.58] for us
[2315.58 → 2316.50] is to really,
[2316.68 → 2317.06] like,
[2317.58 → 2318.66] get people off of their
[2318.66 → 2320.02] kind of default mode
[2320.02 → 2321.30] or the easy decision there
[2321.30 → 2321.80] and really,
[2322.02 → 2323.70] really get folks
[2323.70 → 2324.34] to consider
[2324.34 → 2325.50] and evaluate our product
[2325.50 → 2327.22] and to take that time
[2327.22 → 2327.84] and attention
[2327.84 → 2328.66] away from,
[2328.78 → 2329.82] and there are so many other things
[2329.82 → 2330.68] that they need to be doing
[2330.68 → 2331.86] to really think about
[2331.86 → 2332.54] this choice
[2332.54 → 2333.44] in a very,
[2333.48 → 2333.80] like,
[2333.90 → 2334.66] intentional way.
[2335.72 → 2336.42] It is hard to compete
[2336.42 → 2337.10] against free,
[2337.64 → 2338.94] especially when the Goliath
[2338.94 → 2339.58] is giving it away
[2339.58 → 2340.12] for free.
[2340.70 → 2340.86] Yeah,
[2340.92 → 2341.22] I mean,
[2341.64 → 2341.90] there's,
[2342.00 → 2342.26] you know,
[2343.12 → 2344.20] Microsoft is facing
[2344.20 → 2345.44] like anti-competitive
[2345.44 → 2346.32] lawsuits in Europe
[2346.32 → 2348.00] because of how
[2348.00 → 2349.02] they've set things up.
[2349.56 → 2349.76] Yeah,
[2349.82 → 2350.64] it's unfortunate,
[2350.80 → 2351.18] especially,
[2352.16 → 2352.76] you would think
[2352.76 → 2353.66] as a user,
[2354.18 → 2354.70] like you said,
[2354.70 → 2355.30] nobody got fired
[2355.30 → 2356.40] for buying IBM.
[2356.80 → 2357.30] I don't,
[2357.82 → 2358.52] I didn't make that up
[2358.52 → 2359.06] but I don't disagree
[2359.06 → 2360.30] with it to some degree,
[2360.50 → 2361.22] except for
[2361.22 → 2363.38] what if you're missing out
[2363.38 → 2365.92] on what is free
[2365.92 → 2366.56] and open source
[2366.56 → 2367.26] but you can also
[2367.26 → 2368.04] pay for it
[2368.04 → 2370.46] when the Zulip name
[2370.46 → 2372.12] isn't as polished
[2372.12 → 2373.30] as maybe Microsoft,
[2373.56 → 2373.94] obviously.
[2375.14 → 2375.42] You know,
[2375.46 → 2377.30] that's the hard part
[2377.30 → 2377.64] is that
[2377.64 → 2379.16] you kind of have to
[2379.16 → 2379.80] win them with
[2379.80 → 2381.32] showing up,
[2381.66 → 2381.98] you know,
[2382.06 → 2382.86] with the
[2382.86 → 2385.16] open source-ness
[2385.16 → 2386.40] of what you're doing,
[2387.08 → 2388.18] the way you've been
[2388.18 → 2388.70] in the trenches
[2388.70 → 2389.72] with the communities,
[2389.98 → 2390.36] the way you've
[2390.36 → 2391.10] sponsored things,
[2391.34 → 2392.42] not just simply
[2392.42 → 2394.80] the larger brand name
[2394.80 → 2396.52] and the literal
[2396.52 → 2397.30] freeness that you
[2397.30 → 2398.02] can get with teams.
[2398.10 → 2398.20] Now,
[2398.22 → 2398.62] I know that
[2398.62 → 2399.66] at certain points
[2399.66 → 2400.32] organizations
[2400.32 → 2401.46] have to pay for teams
[2401.46 → 2403.28] but it's pretty much
[2403.28 → 2404.76] free for the entrance
[2404.76 → 2405.80] and then you pay
[2405.80 → 2406.56] once you're
[2406.56 → 2408.50] literally locked in.
[2408.96 → 2409.10] Yeah.
[2409.72 → 2410.52] And I think
[2410.52 → 2411.04] in the past
[2411.04 → 2411.76] a couple of things
[2411.76 → 2412.72] that have held us
[2412.72 → 2413.92] back have been
[2413.92 → 2414.82] one,
[2415.00 → 2416.08] the design of the app.
[2416.16 → 2416.76] That's really something
[2416.76 → 2417.32] that we've been
[2417.32 → 2418.40] focused on improving
[2418.40 → 2418.78] and has been
[2418.78 → 2419.30] like a major,
[2419.42 → 2419.96] major investment
[2419.96 → 2420.84] for us over the past
[2420.84 → 2421.46] year or two
[2421.46 → 2423.00] and continues to be.
[2423.00 → 2425.02] For the longest time
[2425.02 → 2426.40] our users would tell us
[2426.40 → 2428.44] that the user experience
[2428.44 → 2428.86] in Zulip
[2428.86 → 2429.66] is second to none
[2429.66 → 2430.46] but the design
[2430.46 → 2431.28] could use some work
[2431.28 → 2433.28] and that's not
[2433.28 → 2434.36] such a big problem
[2434.36 → 2435.10] necessarily
[2435.10 → 2435.92] for folks
[2435.92 → 2436.60] who have got
[2436.60 → 2437.06] kind of like
[2437.06 → 2437.58] once you've gotten
[2437.58 → 2438.16] used to an app
[2438.16 → 2438.88] you might kind of
[2438.88 → 2439.50] stop noticing
[2439.50 → 2440.82] some of these things
[2440.82 → 2442.20] but in the initial
[2442.20 → 2442.66] evaluation
[2442.66 → 2443.94] it makes a huge difference
[2443.94 → 2444.72] if you open an app
[2444.72 → 2444.98] and you're like
[2444.98 → 2445.78] oh, this doesn't
[2445.78 → 2446.30] look modern,
[2446.40 → 2447.26] this doesn't look beautiful
[2447.26 → 2448.86] and so we're really
[2448.86 → 2449.52] trying to get away
[2449.52 → 2450.04] from that
[2450.04 → 2451.50] and have folks
[2451.50 → 2453.04] have an immediate
[2453.04 → 2453.54] kind of like
[2453.54 → 2454.60] positive response
[2454.60 → 2455.54] to the app
[2455.54 → 2456.58] as well as enjoying
[2456.58 → 2457.84] the UI
[2457.84 → 2459.16] over the long term
[2459.16 → 2461.40] and then another thing
[2461.40 → 2461.90] we've been really
[2461.90 → 2462.60] focusing on
[2462.60 → 2463.04] is that
[2463.04 → 2464.40] the onboarding experience
[2464.40 → 2464.94] because there is
[2464.94 → 2465.38] a little bit
[2465.38 → 2465.80] of a different
[2465.80 → 2466.44] mental model
[2466.44 → 2466.88] for Zulip
[2466.88 → 2467.80] compared to other apps
[2467.80 → 2468.56] folks might have seen
[2468.56 → 2469.98] and we do want
[2469.98 → 2471.18] to have that
[2471.18 → 2472.16] be easy to understand
[2472.16 → 2473.30] and easy to onboard people
[2473.30 → 2474.28] easy to get everybody
[2474.28 → 2475.00] in your organization
[2475.00 → 2475.64] kind of have
[2475.64 → 2477.24] folks get started
[2477.24 → 2477.70] with that
[2477.70 → 2478.94] and also
[2478.94 → 2479.88] I think
[2479.88 → 2481.30] almost any app
[2481.30 → 2481.94] when you first
[2481.94 → 2482.66] encounter it
[2482.66 → 2483.60] might feel a little
[2483.60 → 2484.14] overwhelming
[2484.14 → 2484.72] like
[2484.72 → 2485.82] if you've never
[2485.82 → 2486.88] seen Discord before
[2486.88 → 2487.78] and you open it up
[2487.78 → 2488.56] and there's a lot
[2488.56 → 2489.36] going on
[2489.36 → 2490.92] but there's
[2490.92 → 2492.10] some of these apps
[2492.10 → 2493.88] that we're competing with
[2493.88 → 2495.14] most folks have seen
[2495.14 → 2495.66] them before
[2495.66 → 2496.32] and so now
[2496.32 → 2496.80] they kind of
[2496.80 → 2497.30] have gotten
[2497.30 → 2498.26] that first initial
[2498.26 → 2498.82] feeling of like
[2498.82 → 2499.60] oh, there's so much
[2499.60 → 2499.92] happening
[2499.92 → 2500.48] it's different
[2500.48 → 2501.78] so we really want
[2501.78 → 2502.72] to help folks
[2502.72 → 2503.92] through that experience
[2503.92 → 2504.46] with Zulip
[2504.46 → 2504.92] because
[2504.92 → 2506.30] we do have a lot
[2506.30 → 2507.18] of users coming in
[2507.18 → 2508.60] who haven't
[2508.60 → 2509.28] interacted with it
[2509.28 → 2509.56] before
[2509.56 → 2510.40] to really get them
[2510.40 → 2510.98] across this
[2510.98 → 2511.86] threshold of like
[2511.86 → 2513.06] oh, I get it
[2513.06 → 2513.82] this is comfortable
[2513.82 → 2514.48] this is not
[2514.48 → 2515.74] some things about it
[2515.74 → 2516.12] are different
[2516.12 → 2517.18] but a lot of patterns
[2517.18 → 2518.04] I'm familiar with
[2518.04 → 2518.84] from other applications
[2518.84 → 2520.90] work here as well
[2520.90 → 2522.22] and it really is
[2522.22 → 2522.76] pretty intuitive
[2522.76 → 2523.70] once I kind of
[2523.70 → 2524.82] have a handle on it
[2524.82 → 2525.74] Well, I asked
[2525.74 → 2526.56] in our Slack community
[2526.56 → 2527.20] just moments
[2527.20 → 2527.98] before hopping on
[2527.98 → 2528.66] if anybody's used
[2528.66 → 2528.98] Zulip
[2528.98 → 2529.52] and what they think
[2529.52 → 2529.90] about it
[2529.90 → 2531.54] and one person said
[2531.54 → 2532.72] used it
[2532.72 → 2533.40] at a different company
[2533.40 → 2534.10] liked it a lot
[2534.10 → 2535.64] it's kind of like Slack
[2535.64 → 2536.94] the higher ups
[2536.94 → 2537.96] replaced it with Teams
[2537.96 → 2539.14] as Zulip
[2539.14 → 2539.94] wasn't quoted
[2539.94 → 2540.44] auditable
[2540.44 → 2541.96] so that wasn't
[2541.96 → 2542.48] the free part
[2542.48 → 2543.18] it was the auditable
[2543.18 → 2543.80] which to me
[2543.80 → 2545.74] makes not 100% sense
[2545.74 → 2546.38] but there you go
[2546.38 → 2547.52] Yeah, I'm not so sure
[2547.52 → 2548.48] because we do provide
[2548.48 → 2549.44] different ways
[2549.44 → 2550.36] to export your data
[2550.36 → 2551.46] including like
[2551.46 → 2552.48] compliance exports
[2552.48 → 2553.24] or you can just
[2553.24 → 2553.76] export it
[2553.76 → 2554.38] I don't know
[2554.38 → 2555.36] okay, okay
[2555.36 → 2556.30] Yeah, he says
[2556.30 → 2557.44] it was infinitely better
[2557.44 → 2558.16] than Teams
[2558.16 → 2558.86] so there you go
[2558.86 → 2559.68] Alright, well
[2559.68 → 2561.30] so that's cool
[2561.30 → 2562.64] But that's an example
[2562.64 → 2563.68] of that kind of like
[2563.68 → 2564.58] what might be
[2564.58 → 2565.16] a little bit
[2565.16 → 2565.92] I don't know
[2565.92 → 2566.20] it's like
[2566.20 → 2567.18] I guess folks
[2567.18 → 2567.84] have their own priorities
[2567.84 → 2568.44] and I don't want to
[2568.44 → 2569.04] like second guess
[2569.04 → 2569.96] the management
[2569.96 → 2570.42] but
[2570.42 → 2571.62] so it's just where
[2571.62 → 2572.20] that perspective
[2572.20 → 2572.72] of like
[2572.72 → 2573.92] your team's efficiency
[2573.92 → 2574.64] and how happy
[2574.64 → 2575.52] they are with the software
[2575.52 → 2576.24] they have to use
[2576.24 → 2576.80] you know
[2576.80 → 2577.90] every day
[2577.90 → 2579.60] I don't know anybody
[2579.60 → 2580.26] who likes Teams
[2580.26 → 2580.92] I know lots of people
[2580.92 → 2581.46] that use it
[2581.46 → 2582.42] I'm not a Microsoft
[2582.42 → 2583.20] hater anymore
[2583.20 → 2583.94] I used to be
[2583.94 → 2584.86] when I was a younger man
[2584.86 → 2586.08] but I will say
[2586.08 → 2586.52] that I don't know
[2586.52 → 2587.32] anybody who says
[2587.32 → 2588.26] like Microsoft Teams
[2588.26 → 2589.46] that's good software
[2589.46 → 2589.90] right there
[2589.90 → 2590.42] we love it
[2590.42 → 2590.92] like no one
[2590.92 → 2591.66] no one says that
[2591.66 → 2592.70] has anyone ever
[2592.70 → 2593.22] said to you Adam?
[2594.10 → 2594.80] Not directly
[2594.80 → 2596.82] Indirectly?
[2597.08 → 2597.74] Like you were listening
[2597.74 → 2598.28] to them talk
[2598.28 → 2598.70] to their
[2598.70 → 2600.12] their spouse
[2600.12 → 2600.58] or something
[2600.58 → 2601.36] I don't know
[2601.36 → 2602.14] I love Teams
[2602.14 → 2603.16] Through the tea leaves
[2603.16 → 2603.62] or something
[2603.62 → 2604.36] Now Discord
[2604.36 → 2605.28] people seem to love
[2605.28 → 2606.16] and I'm not really sure
[2606.16 → 2607.32] why personally
[2607.32 → 2608.52] I've signed in
[2608.52 → 2609.70] I've joined some Discords
[2609.70 → 2611.46] it seems like a hot mess
[2611.46 → 2611.86] to me
[2611.86 → 2612.64] but
[2612.64 → 2613.74] it's very big
[2613.74 → 2614.98] in like gaming communities
[2614.98 → 2616.08] musicians
[2616.08 → 2616.88] and
[2616.88 → 2618.66] crypto scam artists
[2618.66 → 2619.48] I know use it
[2619.48 → 2620.72] other communities
[2620.72 → 2622.06] and I'm not sure
[2622.06 → 2623.34] what it is about Discord
[2623.34 → 2623.88] I know they have
[2623.88 → 2624.76] some cool audio
[2624.76 → 2627.06] features built in
[2627.06 → 2627.62] they kind of have
[2627.62 → 2628.70] a lot of different stuff
[2628.70 → 2629.52] because it came out of
[2629.52 → 2630.48] I think
[2630.48 → 2632.00] gamers would hang out
[2632.00 → 2632.80] and talk to each other
[2632.80 → 2633.90] initially
[2633.90 → 2636.18] do you have a lot of
[2636.18 → 2637.56] do you ever have to
[2637.56 → 2638.22] compete with Discord
[2638.22 → 2638.82] or do you ever have to
[2638.82 → 2639.98] explain Zulip
[2639.98 → 2640.74] in light of Discord
[2640.74 → 2641.92] and how you all
[2641.92 → 2643.20] differentiate from them?
[2643.80 → 2644.36] So it depends on
[2644.36 → 2645.42] so Discord is not
[2645.42 → 2646.54] so much designed
[2646.54 → 2647.52] for like
[2647.52 → 2648.60] business use
[2648.60 → 2649.42] or use within
[2649.42 → 2650.00] organizations
[2650.00 → 2650.88] that needs to be
[2650.88 → 2651.64] like closed
[2651.64 → 2652.96] and have sort of
[2652.96 → 2653.70] like because it's
[2653.70 → 2654.32] a single account
[2654.32 → 2654.94] across all your
[2654.94 → 2655.40] organizations
[2655.40 → 2656.08] it's sort of
[2656.08 → 2656.96] different structure there
[2656.96 → 2658.24] we do have folks
[2658.24 → 2659.60] who are Discord users
[2659.60 → 2660.58] who have definitely
[2660.58 → 2661.10] requested
[2661.10 → 2662.36] some features
[2662.36 → 2663.10] that Discord has
[2663.10 → 2663.86] I would say that
[2663.86 → 2664.76] yeah their
[2664.76 → 2665.72] kind of video
[2665.72 → 2666.78] and calling
[2666.78 → 2667.74] and the way
[2667.74 → 2668.26] they do that
[2668.26 → 2669.46] is quite nice
[2669.46 → 2671.12] and that's something
[2671.12 → 2671.82] we've heard
[2671.82 → 2672.82] folks interested in
[2672.82 → 2674.22] something that we're
[2674.22 → 2674.76] actually working
[2674.76 → 2675.60] towards is
[2675.60 → 2676.38] Discord has
[2676.38 → 2678.18] maybe if you haven't
[2678.18 → 2679.12] administered organizations
[2679.12 → 2679.96] you haven't explored
[2679.96 → 2680.52] that side of it
[2680.52 → 2681.00] but they have really
[2681.00 → 2682.22] nice ways
[2682.22 → 2683.30] and flexible ways
[2683.30 → 2684.24] to manage permissions
[2684.24 → 2684.98] and groups
[2684.98 → 2686.50] within an organization
[2686.50 → 2687.16] and so
[2687.16 → 2688.34] that's actually
[2688.34 → 2689.24] a big project
[2689.24 → 2690.04] that we have
[2690.04 → 2690.76] going on right now
[2690.76 → 2691.36] like really
[2691.36 → 2692.22] really flexible
[2692.22 → 2693.92] permissions management
[2693.92 → 2694.74] where you can
[2694.74 → 2695.96] create an arbitrary
[2695.96 → 2696.72] group and then
[2696.72 → 2697.50] give that group
[2697.50 → 2698.24] kind of arbitrary
[2698.24 → 2698.98] set of permissions
[2698.98 → 2699.94] within your organization
[2699.94 → 2700.50] and that
[2700.50 → 2701.30] I think that's
[2701.30 → 2701.56] going to be
[2701.56 → 2702.32] really, really nice
[2702.32 → 2702.86] for anyone
[2702.86 → 2703.60] administering a
[2703.60 → 2704.44] larger organization
[2704.44 → 2705.86] that's one thing
[2705.86 → 2706.82] I really wish we had
[2706.82 → 2708.48] in our Slack Jared
[2708.48 → 2708.94] is that
[2708.94 → 2710.72] we have people come
[2710.72 → 2712.18] and they share things
[2712.18 → 2712.90] they should not
[2712.90 → 2714.14] aka spam
[2714.14 → 2714.70] yes
[2714.70 → 2715.42] and
[2715.42 → 2716.76] I
[2716.76 → 2717.60] would just like to
[2717.60 → 2718.04] be able to
[2718.04 → 2719.00] eventually boot them
[2719.00 → 2719.94] because
[2719.94 → 2721.74] I delete the message
[2721.74 → 2723.08] and
[2723.08 → 2723.86] I look at them
[2723.86 → 2724.22] and I'm like
[2724.22 → 2724.88] well you're clearly
[2724.88 → 2725.70] not here for
[2725.70 → 2726.24] the reasons
[2726.24 → 2727.34] everyone else is here for
[2727.34 → 2728.90] you violated the
[2728.90 → 2729.82] code of
[2729.82 → 2730.36] conduct
[2730.36 → 2731.86] intended for this
[2731.86 → 2732.32] place
[2732.32 → 2733.24] there's no way
[2733.24 → 2733.92] for us
[2733.92 → 2735.52] in our current
[2735.52 → 2736.02] state
[2736.02 → 2736.88] to enforce
[2736.88 → 2737.44] this kind of
[2737.44 → 2737.70] things
[2737.70 → 2738.44] aside from
[2738.44 → 2739.02] just deleting
[2739.02 → 2739.54] messages
[2739.54 → 2740.68] sure we could
[2740.68 → 2741.30] probably log into
[2741.30 → 2741.92] Slack and delete
[2741.92 → 2742.36] their user
[2742.36 → 2743.02] but that doesn't
[2743.02 → 2743.50] stop them from
[2743.50 → 2744.16] coming back
[2744.16 → 2745.20] I'm not sure
[2745.20 → 2745.86] if any platform
[2745.86 → 2746.70] can really do that
[2746.70 → 2747.34] to like prevent
[2747.34 → 2748.16] somebody from
[2748.16 → 2749.54] recreating a new
[2749.54 → 2750.24] account or whatever
[2750.24 → 2751.40] but I do wish
[2751.40 → 2752.12] we had some
[2752.12 → 2753.30] moderation tools
[2753.30 → 2754.50] where I'm sure
[2754.50 → 2755.18] even the community
[2755.18 → 2756.12] inside our
[2756.12 → 2756.98] Slack would step
[2756.98 → 2757.42] up and say
[2757.42 → 2757.80] you know what
[2757.80 → 2758.92] I'll help you guys
[2758.92 → 2759.80] because it's too
[2759.80 → 2760.90] a.m. and you're
[2760.90 → 2761.64] sleeping, and I'm
[2761.64 → 2762.54] not because I'm
[2762.54 → 2763.22] in a different
[2763.22 → 2764.76] country and if I
[2764.76 → 2765.44] see a spam message
[2765.44 → 2765.88] doesn't have to
[2765.88 → 2766.24] sit there for
[2766.24 → 2766.90] eight hours until
[2766.90 → 2767.98] the morning or
[2767.98 → 2768.66] whatever time it
[2768.66 → 2769.40] is when we look
[2769.40 → 2770.02] at Slack again
[2770.02 → 2770.40] it's like well
[2770.40 → 2771.82] hey this thing's
[2771.82 → 2772.34] been sitting there
[2772.34 → 2773.14] with you know
[2773.14 → 2774.94] people piling on
[2774.94 → 2776.22] or looking at it
[2776.22 → 2776.92] or clicking it
[2776.92 → 2778.18] and we can't do
[2778.18 → 2779.20] that stuff, so I
[2779.20 → 2780.14] do I wouldn't
[2780.14 → 2780.94] mind having some
[2780.94 → 2781.88] moderation tools
[2781.88 → 2783.02] yeah we have
[2783.02 → 2783.62] we have some
[2783.62 → 2784.62] tools like I
[2784.62 → 2785.44] guess if you
[2785.44 → 2786.48] deactivate a user
[2786.48 → 2787.22] they can't they
[2787.22 → 2787.76] won't be able to
[2787.76 → 2788.30] rejoin with the
[2788.30 → 2789.02] same email and
[2789.02 → 2789.54] you can also
[2789.54 → 2791.04] disallow throwaway
[2791.04 → 2791.92] email domains if
[2791.92 → 2792.30] you want to
[2792.30 → 2793.16] prevent definitely
[2793.16 → 2793.78] as helpful for
[2793.78 → 2794.46] preventing spam
[2794.46 → 2795.82] yeah you can
[2795.82 → 2797.26] also as a
[2797.26 → 2798.24] personally you can
[2798.24 → 2799.38] mute a user so
[2799.38 → 2800.12] if you as an
[2800.12 → 2800.74] individual don't
[2800.74 → 2801.18] want to see
[2801.18 → 2802.54] something somebody's
[2802.54 → 2804.44] content we do
[2804.44 → 2805.50] let folks have the
[2805.50 → 2806.10] option of meeting
[2806.10 → 2806.86] that person and
[2806.86 → 2807.68] that just hides
[2807.68 → 2808.50] hides all their
[2808.50 → 2811.06] stuff for you so
[2811.06 → 2811.74] you never have to
[2811.74 → 2812.52] like interact with
[2812.52 → 2812.72] it.
[2812.72 → 2813.58] it would be cool
[2813.58 → 2813.90] if you could
[2813.90 → 2815.74] auto block new
[2815.74 → 2816.48] users if they
[2816.48 → 2817.04] start a message
[2817.04 → 2818.04] with dear sir
[2818.04 → 2819.16] slash madam you
[2819.16 → 2820.72] know auto block
[2820.72 → 2821.84] sorry write a
[2821.84 → 2822.50] bot I guess
[2822.50 → 2824.54] yeah some sort of
[2824.54 → 2825.24] pattern match
[2825.24 → 2825.98] I guess
[2825.98 → 2828.42] known yeah I mean
[2828.42 → 2829.08] it doesn't happen
[2829.08 → 2830.62] often we get some
[2830.62 → 2832.18] spam here and
[2832.18 → 2833.38] there and mostly I
[2833.38 → 2835.06] get it go join a
[2835.06 → 2836.04] slack or find a
[2836.04 → 2837.80] place to belong and
[2837.80 → 2838.54] share your messages
[2838.54 → 2840.50] and you do that
[2840.50 → 2841.34] with enough numbers
[2841.34 → 2842.88] you'll get people
[2842.88 → 2844.44] I get if it's a
[2844.44 → 2844.90] numbers game but
[2844.90 → 2845.68] it doesn't make any
[2845.68 → 2847.30] sense to me because
[2847.30 → 2847.78] like you're not
[2847.78 → 2849.54] really getting the
[2849.54 → 2850.32] long-term benefit you
[2850.32 → 2850.96] actually want for a
[2850.96 → 2852.10] brand and so it's
[2852.10 → 2854.18] it's such a nasty
[2854.18 → 2855.82] thing really and
[2855.82 → 2857.20] like I said it
[2857.20 → 2857.68] doesn't happen too
[2857.68 → 2858.60] often but often
[2858.60 → 2859.70] enough I'm like yeah
[2859.70 → 2860.20] I wouldn't mind
[2860.20 → 2860.60] some tooling.
[2861.72 → 2861.94] What would a
[2861.94 → 2862.94] migration look like?
[2863.36 → 2864.00] So for something
[2864.00 → 2864.66] like moving from
[2864.66 → 2865.64] slack into
[2865.64 → 2865.96] Zulip?
[2866.18 → 2866.94] Just for instance.
[2867.40 → 2867.86] Yeah sure.
[2868.36 → 2869.26] Just for instance.
[2870.14 → 2870.88] As a random
[2870.88 → 2871.32] example.
[2871.64 → 2872.08] Hypothetically
[2872.08 → 2872.66] speaking.
[2872.82 → 2873.64] Yeah yeah yeah
[2873.64 → 2874.48] apropos nothing.
[2874.88 → 2875.66] Yeah so we have
[2875.66 → 2876.78] instructions on our
[2876.78 → 2877.58] health centre for
[2877.58 → 2879.04] how to go about it
[2879.04 → 2879.78] so basically what
[2879.78 → 2880.56] you would want to
[2880.56 → 2882.78] do is assuming you
[2882.78 → 2883.36] want to keep your
[2883.36 → 2884.14] message history you
[2884.14 → 2885.12] can export that
[2885.12 → 2886.08] through slack.
[2886.58 → 2886.98] It might be
[2886.98 → 2888.18] limited I guess now
[2888.18 → 2889.42] depending on your
[2889.42 → 2891.38] situation and then
[2891.38 → 2892.64] if you're moving
[2892.64 → 2893.26] say to Zulip
[2893.26 → 2894.48] Cloud so that's our
[2894.48 → 2896.02] managed SAS
[2896.02 → 2897.58] offering you would
[2897.58 → 2899.06] just send over that
[2899.06 → 2900.12] data to us and we
[2900.12 → 2901.06] would import that
[2901.06 → 2901.74] into a new
[2901.74 → 2902.48] organization for
[2902.48 → 2904.50] you and so you
[2904.50 → 2905.02] would you could
[2905.02 → 2906.16] preserve all your
[2906.16 → 2906.80] not just the
[2906.80 → 2907.56] messages but also
[2907.56 → 2908.86] the user data so
[2908.86 → 2910.72] you'd have a
[2910.72 → 2912.64] running start on
[2912.64 → 2914.62] that and then we
[2914.62 → 2915.52] also I don't know if
[2915.52 → 2915.94] you guys have
[2915.94 → 2917.42] integrations but also
[2917.42 → 2919.10] to make it easier to
[2919.10 → 2919.74] move over your
[2919.74 → 2920.64] integrations if you
[2920.64 → 2922.50] have any we have
[2922.50 → 2923.76] slack compatible
[2923.76 → 2924.94] web hooks so
[2924.94 → 2925.68] basically you could
[2925.68 → 2927.18] just kind of remap
[2927.18 → 2928.04] where your web hooks
[2928.04 → 2928.66] are sending in their
[2928.66 → 2929.88] data to be Zulip
[2929.88 → 2931.42] and then on your
[2931.42 → 2932.38] own time later on
[2932.38 → 2933.22] if you want to
[2933.22 → 2935.68] move over to more
[2935.68 → 2936.46] like Zulip native
[2936.46 → 2937.68] integrations that's a
[2937.68 → 2938.62] then you can do
[2938.62 → 2939.54] that but things
[2939.54 → 2940.58] would be working
[2940.58 → 2941.44] for you right away
[2941.44 → 2942.56] so yeah it's
[2942.56 → 2944.44] it's, and you can
[2944.44 → 2946.04] you can tell folks
[2946.04 → 2946.84] where to log in or
[2946.84 → 2947.52] we can automatically
[2947.52 → 2949.56] send emails to all
[2949.56 → 2950.20] the users that you
[2950.20 → 2951.36] imported with their
[2951.36 → 2952.56] login information so
[2952.56 → 2953.90] however you want to
[2953.90 → 2954.78] manage that and
[2954.78 → 2955.42] they would just get
[2955.42 → 2956.18] an email and they
[2956.18 → 2956.80] would maybe have
[2956.80 → 2957.66] like a password reset
[2957.66 → 2958.84] on the first sign-up
[2958.84 → 2959.92] or like obviously
[2959.92 → 2960.36] you're not going to
[2960.36 → 2961.34] import their passwords
[2961.34 → 2962.18] yeah, and we have
[2962.18 → 2963.30] all the social auth
[2963.30 → 2964.18] as well so if you
[2964.18 → 2965.42] folks want to log in
[2965.42 → 2966.82] with their you know
[2966.82 → 2967.92] google account and
[2967.92 → 2968.78] GitHub or anything
[2968.78 → 2969.84] like that that's also
[2969.84 → 2972.22] on offer that's the
[2972.22 → 2974.24] it's 90% of my
[2974.24 → 2976.14] anxiety if we're
[2976.14 → 2977.02] hypothetically speaking
[2977.02 → 2979.24] about things yes we
[2979.24 → 2981.84] are is I feel like
[2981.84 → 2982.64] I'm just I've been
[2982.64 → 2983.34] like in this waiting
[2983.34 → 2984.04] pattern in my own
[2984.04 → 2984.82] brain you know I
[2984.82 → 2985.66] haven't taken any
[2985.66 → 2986.24] action I've been
[2986.24 → 2987.00] like just thinking
[2987.00 → 2987.66] that maybe slack
[2987.66 → 2988.40] would someday get
[2988.40 → 2989.52] it and somehow
[2989.52 → 2990.62] just recognize that
[2990.62 → 2991.02] there's so many
[2991.02 → 2991.82] communities that have
[2991.82 → 2993.20] you know built up
[2993.20 → 2993.88] their thing around
[2993.88 → 2995.24] them and that many
[2995.24 → 2996.52] of us in even
[2996.52 → 2997.18] developer land or
[2997.18 → 2997.76] just let's just say
[2997.76 → 2999.28] tech land have
[2999.28 → 3002.10] numerous logos
[3002.10 → 3003.36] slash icons in our
[3003.36 → 3004.30] slack sidebar so we
[3004.30 → 3006.02] bounce from one
[3006.02 → 3007.10] workspace to another
[3007.10 → 3008.64] and I like that I
[3008.64 → 3009.18] don't want to be in
[3009.18 → 3009.80] a world where I
[3009.80 → 3010.84] can't where I have
[3010.84 → 3012.78] to like still I
[3012.78 → 3013.82] guess keep slack
[3013.82 → 3015.04] or I just like the
[3015.04 → 3016.02] unification of it
[3016.02 → 3017.62] and as a user I
[3017.62 → 3018.06] don't want to have
[3018.06 → 3019.66] to go to the
[3019.66 → 3020.62] Slack app and then
[3020.62 → 3021.74] the Zulip app and
[3021.74 → 3022.48] then the whatever
[3022.48 → 3023.22] app I would just
[3023.22 → 3024.58] like a unification if
[3024.58 → 3025.40] it was possible I'm
[3025.40 → 3026.02] sure it is I think
[3026.02 → 3026.62] there are some out
[3026.62 → 3027.18] there, but there's
[3027.18 → 3028.42] diminishing returns
[3028.42 → 3031.00] my point is that I've
[3031.00 → 3031.82] been just anxious
[3031.82 → 3032.82] about what it would
[3032.82 → 3033.82] take to literally
[3033.82 → 3036.00] migrate if ever we
[3036.00 → 3037.00] actually had to
[3037.00 → 3038.22] because we got
[3038.22 → 3040.24] 7,000 is people in
[3040.24 → 3040.90] our main channel
[3040.90 → 3043.02] not all of them are
[3043.02 → 3044.12] obviously present and
[3044.12 → 3045.62] active every day I'm
[3045.62 → 3046.04] sure some of them
[3046.04 → 3046.64] come and go maybe
[3046.64 → 3047.50] some of them lurk I
[3047.50 → 3048.76] have no idea because
[3048.76 → 3049.46] I don't really have any
[3049.46 → 3050.58] analytics to our usage
[3050.58 → 3052.30] in terms of just beyond
[3052.30 → 3053.22] messages I'm paying
[3053.22 → 3056.36] attention to, so I just
[3056.36 → 3057.30] wonder if we ever we
[3057.30 → 3058.98] moved to something
[3058.98 → 3060.74] else how much would
[3060.74 → 3062.24] we how much would we
[3062.24 → 3063.14] lose how hard would it
[3063.14 → 3064.12] be to get even our
[3064.12 → 3065.36] active people to stay
[3065.36 → 3066.38] involved right like
[3066.38 → 3067.10] would they come with
[3067.10 → 3067.80] us and would they
[3067.80 → 3069.68] continue to hang out
[3069.68 → 3070.44] you know, or they'd be
[3070.44 → 3072.74] like Zulip what why
[3072.74 → 3073.78] yeah I mean I can't I
[3073.78 → 3074.58] can't promise anything
[3074.58 → 3075.46] about your specific
[3075.46 → 3077.04] experience, but we have
[3077.04 → 3078.30] had folks tell us that
[3078.30 → 3079.46] when they moved to
[3079.46 → 3080.10] Zulip they actually
[3080.10 → 3080.94] started getting much
[3080.94 → 3081.70] better community
[3081.70 → 3083.66] engagement because it
[3083.66 → 3085.42] works quite nicely for
[3085.42 → 3086.26] folks who are not
[3086.26 → 3088.12] around all the time so
[3088.12 → 3090.94] I mean in the one
[3090.94 → 3091.96] kind of category folks as
[3091.96 → 3092.44] you were saying is
[3092.44 → 3093.08] there may be people who
[3093.08 → 3094.00] are lurking or who are
[3094.00 → 3094.90] just kind of coming by
[3094.90 → 3095.88] once in a little while
[3095.88 → 3096.86] once in a while to
[3096.86 → 3097.94] check in on something
[3097.94 → 3100.40] and if you're is you're
[3100.40 → 3101.48] coming to something like
[3101.48 → 3102.94] slack you know it's hard
[3102.94 → 3105.00] to you might see the
[3105.00 → 3105.96] latest messages it's
[3105.96 → 3106.88] really hard going to be
[3106.88 → 3108.40] not really possible for
[3108.40 → 3109.30] you to kind of catch up
[3109.30 → 3110.16] on what you missed if
[3110.16 → 3111.02] you or if you're checking
[3111.02 → 3111.68] out every couple of
[3111.68 → 3112.40] weeks or every month
[3112.40 → 3113.28] and then active
[3113.28 → 3115.56] organization whereas for
[3115.56 → 3116.82] Zulip if you just want
[3116.82 → 3117.90] to sort of check in on
[3117.90 → 3119.56] things occasionally folks
[3119.56 → 3120.28] will come in, and they'll
[3120.28 → 3121.02] look at that recent
[3121.02 → 3122.18] conversations view you
[3122.18 → 3123.10] maybe saw when you were
[3123.10 → 3124.98] exploring the app and
[3124.98 → 3126.22] instead of having to
[3126.22 → 3126.98] look at sort of
[3126.98 → 3127.84] individual messages and
[3127.84 → 3128.52] try to figure out what's
[3128.52 → 3129.38] going on they'll just see
[3129.38 → 3130.46] that list of topics and
[3130.46 → 3131.86] they can be like oh this
[3131.86 → 3132.82] topic sounds interesting
[3132.82 → 3133.94] let me jump into that
[3133.94 → 3135.06] and so you don't even
[3135.06 → 3136.12] have to feel obliged to
[3136.12 → 3137.82] kind of make everything be
[3137.82 → 3139.36] marked as red or kind of
[3139.36 → 3140.24] manage your own reds
[3140.24 → 3141.10] necessarily if it's just
[3141.10 → 3142.06] something where you're not
[3142.06 → 3143.16] following every little
[3143.16 → 3144.88] detail you really can kind
[3144.88 → 3146.56] of just skim that list of
[3146.56 → 3147.80] what's been going on and
[3147.80 → 3149.86] jump in to the ones that
[3149.86 → 3151.26] are of interest and so
[3151.26 → 3152.86] yeah so we've had folks
[3152.86 → 3153.50] say that you know
[3153.50 → 3154.42] something like an open
[3154.42 → 3155.22] source project that it
[3155.22 → 3156.66] can actually really be
[3156.66 → 3157.78] great for community
[3157.78 → 3159.62] engagement because people
[3159.62 → 3161.22] can select the parts that
[3161.22 → 3162.06] are interesting to them
[3162.06 → 3163.84] and just follow
[3163.84 → 3165.06] those and jump in on
[3165.06 → 3165.80] those you can even
[3165.80 → 3168.06] configure notification
[3168.06 → 3169.52] there's a concept of
[3169.52 → 3170.52] following topics so once
[3170.52 → 3171.06] you've seen something
[3171.06 → 3172.06] that's interesting if it's
[3172.06 → 3172.98] a community you're not
[3172.98 → 3173.98] engaged with very
[3173.98 → 3175.36] regularly you can follow
[3175.36 → 3176.66] that particular topic and
[3176.66 → 3177.76] say get email
[3177.76 → 3178.78] notifications when there's
[3178.78 → 3180.02] more messages just to that
[3180.02 → 3181.72] topic and so there's really
[3181.72 → 3182.88] ways to follow specific
[3182.88 → 3184.34] conversations and find
[3184.34 → 3185.76] things to engage with for
[3185.76 → 3186.88] occasional users in a
[3186.88 → 3187.22] community
[3187.22 → 3189.08] I do like how you can set
[3189.08 → 3191.16] your Zulip to public as
[3191.16 → 3193.16] well can you do that on
[3193.16 → 3194.26] like a per-channel basis
[3194.26 → 3196.18] yeah exactly, so this is
[3196.18 → 3197.96] something that there's an
[3197.96 → 3199.36] overall organization setting
[3199.36 → 3200.92] for whether you will you
[3200.92 → 3202.22] want to have public
[3202.22 → 3203.28] channels as an option so
[3203.28 → 3204.38] for example you know many
[3204.38 → 3205.48] some businesses might not
[3205.48 → 3206.54] want to reveal you know
[3206.54 → 3207.34] share anything and they
[3207.34 → 3208.40] just want to turn that all
[3208.40 → 3210.00] all the way off and then
[3210.00 → 3210.78] yeah for any given
[3210.78 → 3211.78] channel you just configure
[3211.78 → 3213.06] it you can configure it to
[3213.06 → 3214.64] be kind of public with for
[3214.64 → 3216.26] logged in folks you know
[3216.26 → 3219.16] private or public even
[3219.16 → 3220.96] without logging in so yeah
[3220.96 → 3221.82] what you guys were seeing
[3221.82 → 3222.70] in that the development
[3222.70 → 3223.68] community is a bunch of
[3223.68 → 3224.56] channels that we've marked
[3224.56 → 3226.36] as completely public and
[3226.36 → 3227.90] then yeah you can just kind
[3227.90 → 3229.46] of come by and not have to
[3229.46 → 3230.98] do you not have to log in
[3230.98 → 3231.86] and just view messages
[3231.86 → 3233.04] there and then of course if
[3233.04 → 3234.02] you want to participate then
[3234.02 → 3234.94] you would create an account
[3234.94 → 3236.82] and log in and post now are
[3236.82 → 3238.30] those public channels do
[3238.30 → 3240.04] they get indexed by search
[3240.04 → 3241.80] engines they don't we do
[3241.80 → 3244.06] have a way to a tool for
[3244.06 → 3246.44] exporting your zoom data
[3246.44 → 3247.96] and then you can get that
[3247.96 → 3249.90] indexed by search engines
[3249.90 → 3252.56] and like a kind of archive
[3252.56 → 3254.72] of all the messages, but it's
[3254.72 → 3255.48] actually kind of major
[3255.48 → 3256.76] technical the reason is it's
[3256.76 → 3258.52] a major technical project to
[3258.52 → 3261.18] make those searchable indexable
[3261.18 → 3262.98] by search engines and we just
[3262.98 → 3263.74] haven't had a chance to
[3263.74 → 3265.10] prioritize that project yet but
[3265.10 → 3266.56] that's definitely on the radar
[3266.56 → 3268.44] but it just requires quite a
[3268.44 → 3269.42] bit of technical work to make
[3269.42 → 3269.90] that work
[3269.90 → 3271.28] yeah I mean that'd be pretty
[3271.28 → 3272.56] cool for public ones because
[3272.56 → 3273.66] then it would double as a
[3273.66 → 3275.74] as an indexable forum
[3275.74 → 3276.18] for sure
[3276.18 → 3277.86] if it wasn't like because a
[3277.86 → 3278.54] lot of those conversations
[3278.54 → 3279.64] become kind of canonical
[3279.64 → 3281.24] resources, or they could be but
[3281.24 → 3283.30] they are lost to the ether you
[3283.30 → 3283.92] know but if they were
[3283.92 → 3284.64] actually indexed
[3284.64 → 3286.12] yeah one thing we do a lot is
[3286.12 → 3287.10] actually is linking to
[3287.10 → 3288.30] conversations so it's you can
[3288.30 → 3289.64] link either to a conversation
[3289.64 → 3290.92] or to even to a particular
[3290.92 → 3291.80] message within that
[3291.80 → 3293.72] conversation and so for
[3293.72 → 3295.62] example when we like say
[3295.62 → 3296.78] file an issue for a
[3296.78 → 3297.34] Zulu feature
[3297.34 → 3299.94] we'll generally link to a
[3299.94 → 3301.12] conversation where we had
[3301.12 → 3302.14] some initial brainstorming
[3302.14 → 3303.18] discussion of that feature
[3303.18 → 3305.16] and so when folks are working
[3305.16 → 3306.66] on it, they can get that extra
[3306.66 → 3308.66] content and context and then
[3308.66 → 3310.24] also you know if they have a
[3310.24 → 3311.16] follow-up question they can
[3311.16 → 3312.28] just pose that question in the
[3312.28 → 3313.72] same conversation and continue
[3313.72 → 3315.18] from where it left off so
[3315.18 → 3317.62] that linking does make
[3317.62 → 3318.86] some things easier to find
[3318.86 → 3320.38] so one thing you might not
[3320.38 → 3322.24] know all yet about Adam is
[3322.24 → 3324.08] that he is an avid home
[3324.08 → 3326.78] lubber and so what would a
[3326.78 → 3328.52] migration look like to the
[3328.52 → 3329.92] self-hosted if Adam were to
[3329.92 → 3331.34] become our system
[3331.34 → 3333.18] administrator and run our
[3333.18 → 3334.90] Zulu community out of his
[3334.90 → 3337.10] home lab yeah what would that
[3337.10 → 3338.64] look like yeah so it's pretty
[3338.64 → 3340.76] similar except for you would
[3340.76 → 3342.58] skip the part where you email
[3342.58 → 3344.50] us, and then you would do that
[3344.50 → 3344.86] in for yourself
[3344.86 → 3346.20] one last step even easier Adam
[3346.20 → 3348.14] exactly yeah we have an
[3348.14 → 3349.80] installation guide that is
[3349.80 → 3350.92] pretty straightforward we
[3350.92 → 3352.40] really do work hard to make
[3352.40 → 3355.16] it is easy to self-host Zulu
[3355.16 → 3357.14] and also make it make the
[3357.14 → 3358.28] installation process as easy
[3358.28 → 3360.70] as possible really smooth
[3360.70 → 3363.38] update upgrade process when you
[3363.38 → 3364.86] when the new version comes out
[3364.86 → 3365.98] so it's definitely a priority
[3365.98 → 3366.96] for us and there's detailed
[3366.96 → 3369.24] documentation on how you
[3369.24 → 3371.34] need to do everything so
[3371.34 → 3372.56] should be very doable for you
[3372.56 → 3373.80] if that's something that you
[3373.80 → 3375.38] enjoy yeah you just have a
[3375.38 → 3379.00] docker image yes sorry this is
[3379.00 → 3380.56] not the part that I personally
[3380.56 → 3382.50] work on nearly as much as
[3382.50 → 3384.32] some other things all good
[3384.32 → 3385.82] but yes you hear that Adam
[3385.82 → 3386.92] they got a docker image okay
[3386.92 → 3390.58] and what aspects of Zulu
[3390.58 → 3393.62] cloud the hosted version are
[3393.62 → 3395.68] completely inaccessible to you
[3395.68 → 3397.96] as a self-hosted are there like
[3397.96 → 3399.58] specific features that you will
[3399.58 → 3401.40] never be able to use in self-hosted
[3401.40 → 3403.38] or is it all there, but you have
[3403.38 → 3404.74] to worry about backing it up and
[3404.74 → 3405.90] making sure it's up and all that
[3405.90 → 3407.50] kind of stuff it is all there so
[3407.50 → 3410.08] Zulu is 100% open source there's
[3410.08 → 3411.28] there's nothing that we're like
[3411.28 → 3412.74] locking away from so from self-
[3412.74 → 3415.10] posters if you self-host this are
[3415.10 → 3417.00] the one thing that so we do offer
[3417.00 → 3419.08] paid plans for self-hosted you
[3419.08 → 3420.48] don't have to sign up for one but
[3420.48 → 3423.08] they're an offer and the kind of two
[3423.08 → 3425.44] two things that two major things that
[3425.44 → 3427.56] we're providing with those paid
[3427.56 → 3430.38] plans, so one is mobile push
[3430.38 → 3433.38] notifications so the way that app store
[3433.38 → 3435.54] policies work both on Android and IOS
[3435.54 → 3439.14] is that if you have a mobile app which
[3439.14 → 3442.86] are apps are also 100% open source but
[3442.86 → 3444.90] you probably want to use the app that we
[3444.90 → 3446.86] put in the Play Store or the App Store
[3446.86 → 3448.82] rather than kind of rolling your own
[3448.82 → 3452.62] which is a whole thing and so the way
[3452.62 → 3455.44] those app store policies work is that a
[3455.44 → 3457.30] single app can only get push notifications
[3457.30 → 3459.26] from a single server it's kind of like a
[3459.26 → 3462.14] anti-spam security measure on their end
[3462.14 → 3465.32] and so if you're self-hosted for your
[3465.32 → 3468.30] self-hosted server to send notifications
[3468.90 → 3472.22] to the Zulu mobile apps what you do is
[3472.22 → 3473.78] basically bounce that traffic through our
[3473.78 → 3476.14] server and so that's a service that a
[3476.14 → 3477.62] lot of folks who are self-hosting choose
[3477.62 → 3480.88] to pay for as part of our plans and then
[3480.88 → 3482.78] the other piece is just support so if you
[3482.78 → 3485.56] want any kind of support with running
[3485.56 → 3488.04] your Zulu server so we there are
[3488.04 → 3491.54] community-based support and in the in our
[3491.54 → 3494.72] development chat so we do folks do come
[3494.72 → 3496.74] by and get some help there but if you
[3496.74 → 3499.12] need SLAs or if you need something more
[3499.12 → 3501.22] more than just kind of like asking a
[3501.22 → 3502.58] question on chat and seeing a folk
[3502.58 → 3505.80] around to apply then we do have support
[3505.80 → 3507.28] offerings as well, so those are kind of
[3507.28 → 3510.80] the types of plans for self-hosted
[3510.80 → 3511.34] organizations.
[3511.34 → 3515.32] I did find a repo and I know that you
[3515.32 → 3516.62] may not be able to go deep on this if
[3516.62 → 3521.38] you can, it's okay is on your Zulu org on
[3521.38 → 3524.48] GitHub it's docker-Zulu, so I assume
[3524.48 → 3527.68] this is official it's container
[3527.68 → 3529.78] configurations images etc for all of it
[3529.78 → 3532.04] there's a docker composed file there so
[3532.04 → 3533.76] yeah so I guess the way it's
[3533.76 → 3535.34] described in our docs is it's an
[3535.34 → 3537.48] officially supported experimental docker
[3537.48 → 3541.00] image okay official yet experimental so
[3541.00 → 3544.60] you know tread softly but officially 102
[3544.60 → 3546.28] lines in this compose file I mean that's
[3546.28 → 3549.26] a lot of lines so you've got SSL
[3549.26 → 3552.34] certificates set up for folks you can
[3552.34 → 3554.14] set up a custom CA certificate if you
[3554.14 → 3555.66] want to you can point to a different
[3555.66 → 3557.76] git repo so you can point to the
[3557.76 → 3559.22] official, or you can have your own fork
[3559.22 → 3562.06] which I think is pretty cool, and you're
[3562.06 → 3564.12] just a docker compose up away from
[3564.12 → 3566.50] running Zulu locally sounds pretty
[3566.50 → 3568.86] awesome there is also an architecture
[3568.86 → 3572.20] document on your docs which I found to
[3572.20 → 3574.14] be pretty good at describing the way
[3574.14 → 3576.72] the whole thing works and the various
[3576.72 → 3578.92] parts Postgres backend they're using
[3578.92 → 3580.70] Regis and Geocached in certain areas
[3580.70 → 3584.86] it's a Django web app for the backend and
[3584.86 → 3587.58] then there's a single page app which is
[3587.58 → 3589.40] written in TypeScript probably react I'm
[3589.40 → 3592.52] not sure for the web you know in browser
[3592.52 → 3595.10] experience obviously the mobile clients
[3595.10 → 3597.40] you mentioned are getting rewritten into
[3597.40 → 3600.42] did you say Flutter that's right yeah and
[3600.42 → 3602.24] so they're all using that same backend
[3602.24 → 3604.32] API now if you're self-hosted, and you want
[3604.32 → 3607.72] to connect your web your phone app to
[3607.72 → 3609.64] that are you just basically saying like
[3609.64 → 3612.46] zulub.changelog.com like would be just
[3612.46 → 3614.98] create a yeah just when you sign in you put
[3614.98 → 3616.94] in that URL for your server, and you're good
[3616.94 → 3619.10] wham bam what do you think Adam you want
[3619.10 → 3621.38] to uh docker voucherize us
[3621.38 → 3625.80] well see now that's the that's the a
[3625.80 → 3628.18] great question obviously, but now you have
[3628.18 → 3631.34] to be your own uptime for your own chat
[3631.34 → 3633.96] apps that's the high price of self-hosted
[3633.96 → 3636.84] that is the high price of self-hosted I
[3636.84 → 3639.56] would want to compare Zulu Cloud and
[3639.56 → 3645.28] other ways first, but I'm not against the
[3645.28 → 3646.76] idea of self-hosting I just think it takes a
[3646.76 → 3650.36] lot of responsibility to do so yeah I
[3650.36 → 3652.62] assume how then maybe you answered
[3652.62 → 3654.14] this already, and I was reading docs or
[3654.14 → 3656.30] the doc composed file while you said it
[3656.30 → 3658.44] and if I missed it I'm sorry no worries
[3658.44 → 3660.92] but how does like your iOS Android app
[3660.92 → 3663.78] work with a self-hosted scenario do you
[3663.78 → 3666.60] point it at like a URL kind of thing like
[3666.60 → 3668.68] if I was yeah yeah I asked that one yeah
[3668.68 → 3670.58] exactly yeah so when you asked and
[3670.58 → 3672.44] answered no worries yeah so when users
[3672.44 → 3674.76] log in please when users log in they'll
[3674.76 → 3677.14] just put on the URL for your server and
[3677.14 → 3678.72] then they're good to go yeah you just
[3678.72 → 3681.30] see name a subdomain, and you're yeah so
[3681.30 → 3683.84] self-hosting yeah I mean you would have
[3683.84 → 3685.80] to have even if it was like literally
[3685.80 → 3689.32] self-hosting in the closet or self-hosting
[3689.32 → 3692.02] on digital ocean render those are two that
[3692.02 → 3694.22] are mentioned in your docs we obviously
[3694.22 → 3697.56] prefer fly.io not paid to say that but
[3697.56 → 3700.04] just definitely very passionate, so I guess
[3700.04 → 3701.98] we can self-host on fly right you're like
[3701.98 → 3703.72] we wouldn't have to 100% self-host
[3703.72 → 3704.92] anywhere I just thought it'd be cool to
[3704.92 → 3706.70] run out of your closet it would be cool
[3706.70 → 3708.54] except for I think I don't know if the
[3708.54 → 3711.34] uptown would be as good I mean the ping
[3711.34 → 3713.20] the latency Arthur may have opinions
[3713.20 → 3714.70] about it that's for sure it's just chat
[3714.70 → 3716.86] you know it is worst case scenarios we
[3716.86 → 3718.24] can't send each other memes for a few
[3718.24 → 3720.22] hours I mean we've had we've had folks
[3720.22 → 3723.08] self-host Zulip air gaps like on a ship
[3723.08 → 3725.10] oh really where they weren't going to have
[3725.10 → 3726.84] connectivity with the wider internet
[3726.84 → 3729.44] just as there's chat within that
[3729.44 → 3731.38] that's cool community yeah so if we
[3731.38 → 3732.54] ever decided to travel the world maybe
[3732.54 → 3735.36] on a sailboat yeah like our friend Alex
[3735.36 → 3737.22] McCaw did we could have Zulip on that
[3737.22 → 3739.10] on that sailboat with us that would be
[3739.10 → 3742.78] cool self-contained Zulip and I guess
[3742.78 → 3746.52] local area network only right so yeah yeah
[3746.52 → 3748.92] yeah might not be required if you have a
[3748.92 → 3750.64] you know five people on your boat but
[3750.64 → 3752.84] you could even go local machine only you
[3752.84 → 3754.34] know you can unplug that machine from
[3754.34 → 3755.96] the whole internet and have Zulip just on
[3755.96 → 3757.94] that machine if you wanted to truth
[3757.94 → 3762.44] not very useful that way, but you can do
[3762.44 → 3764.64] it via the terminal app even
[3764.64 → 3765.24] yeah
[3765.24 → 3778.96] what's up friends I'm here with Kyle
[3778.96 → 3782.60] barberry CTO at coder.com so Kyle I've
[3782.60 → 3785.30] known coder as the IDE in the cloud and
[3785.30 → 3788.26] over time you've iterated to become a
[3788.26 → 3790.26] fully open source cloud development
[3790.26 → 3792.74] environment a CDE how do you explain
[3792.74 → 3795.84] what coder is and what it does coder is a
[3795.84 → 3797.38] platform to provision you a development
[3797.38 → 3799.34] environment on any cloud infrastructure
[3799.34 → 3801.66] that might be in a VM that might be
[3801.66 → 3803.66] inside a container, but coder is kind
[3803.66 → 3805.50] of a developer's route to provision
[3805.50 → 3807.08] infrastructure for them to write software
[3807.08 → 3809.76] inside we started with the IDE which
[3809.76 → 3811.36] is kind of like putting VS Code in the
[3811.36 → 3813.20] browser which is what most people are
[3813.20 → 3814.88] certainly familiar with us for and we
[3814.88 → 3816.92] kind of funnelled that into more of a
[3816.92 → 3818.16] platform where people provision the
[3818.16 → 3819.76] infrastructure and a lot of people do
[3819.76 → 3821.32] use a web IDE with coder a lot of
[3821.32 → 3823.00] people use a local IDE and just connect
[3823.00 → 3823.24] in
[3823.24 → 3825.36] okay so what are teams coming to you for
[3825.36 → 3826.94] who's coming to you what people really
[3826.94 → 3829.38] come to us for particularly this problem
[3829.38 → 3831.34] is really exacerbated if you're a
[3831.34 → 3833.20] large enterprise is when you have like
[3833.20 → 3835.08] 500 engineers that are trying to
[3835.08 → 3837.00] update like a version of Python and
[3837.00 → 3839.16] instead we allow one engineer to go
[3839.16 → 3840.66] through that tedious work of updating
[3840.66 → 3842.34] some scripts or some docker container
[3842.34 → 3843.84] and then you can actually just deploy
[3843.84 → 3845.66] that in one click to say like 500
[3845.66 → 3847.76] engineers and make it really
[3847.76 → 3851.26] simple let's laser focus in on the
[3851.26 → 3854.18] platform engineer it is that team's job
[3854.18 → 3856.30] to provide the best infrastructure the
[3856.30 → 3858.22] best platform for their given
[3858.22 → 3861.20] applications for their teams what are
[3861.20 → 3863.58] some signs or signals for platform
[3863.58 → 3865.76] engineers to think about when it might
[3865.76 → 3867.58] be time to consider a cloud development
[3867.58 → 3869.70] environment like coder.com so as a
[3869.70 → 3871.76] platform engineer developers might
[3871.76 → 3874.14] constantly be opening like IT tickets
[3874.14 → 3875.36] that their computer isn't working
[3875.36 → 3877.88] properly they might constantly want to
[3877.88 → 3879.58] update dependencies, but that's a big
[3879.58 → 3881.30] mess you constantly have to email
[3881.30 → 3883.96] people across your team to say hey
[3883.96 → 3886.06] Adam could we update from Java 17 to
[3886.06 → 3887.58] Java 18 those are the kinds of
[3887.58 → 3889.06] problems that people typically have
[3889.06 → 3891.16] that's the status quo you ship people
[3891.16 → 3893.28] more powerful laptops to improve the
[3893.28 → 3895.20] build times of your projects you try to
[3895.20 → 3896.88] reduce the complexity of your products
[3896.88 → 3898.76] instead of simply you know leveraging
[3898.76 → 3900.96] better hardware we believe that the
[3900.96 → 3902.66] future is leveraging the cloud for a lot
[3902.66 → 3904.18] of these things you can get more
[3904.18 → 3907.02] powerful instances in GCP or AWS that
[3907.02 → 3908.14] can make the build times faster
[3908.14 → 3910.16] instantly you can let one developer
[3910.16 → 3911.98] create a standardized environment and
[3911.98 → 3913.74] then distribute it to a thousand so
[3913.74 → 3915.34] that when you're updating from Java 17
[3915.34 → 3917.58] to 18 it's just a simple pull request
[3917.58 → 3920.16] you can co-locate your servers right next
[3920.16 → 3921.78] to something like S3 or a database
[3921.78 → 3923.48] they're using in development so that
[3923.48 → 3925.36] you get immediate data transfers
[3925.36 → 3926.70] and it's not slow many of our
[3926.70 → 3928.36] customers which is a crazy thing to
[3928.36 → 3929.92] say, but they use absolutely massive
[3929.92 → 3931.76] monorepos, and they get clones that
[3931.76 → 3933.48] go from like 10 minutes or 20 minutes
[3933.48 → 3935.48] or an hour to simply like a minute or
[3935.48 → 3937.68] 30 seconds it's just a lot simpler
[3937.68 → 3939.66] when all of your engineers are
[3939.66 → 3941.66] standardized on one centralized piece
[3941.66 → 3943.62] of infrastructure and then one person
[3943.62 → 3945.54] can can impact the lives of hundreds
[3945.54 → 3947.26] of engineers and with that we don't
[3947.26 → 3948.54] believe that everything belongs in the
[3948.54 → 3950.42] cloud we think that some workloads are
[3950.42 → 3952.26] really amazing for it and some are
[3952.26 → 3954.12] absolutely terrible coder should be a
[3954.12 → 3956.00] self-serve offering to your engineers
[3956.00 → 3957.74] it should not be prescriptive where you
[3957.74 → 3959.72] migrate all pieces of software
[3959.72 → 3961.42] development into the cloud only the
[3961.42 → 3962.96] things that really get a lot better by
[3962.96 → 3964.84] running them in this cloud native way
[3964.84 → 3967.10] do we really promote moving well it
[3967.10 → 3969.90] might be time to consider a cloud
[3969.90 → 3971.84] development environment and open source
[3971.84 → 3974.20] is awesome and coder is fully open
[3974.20 → 3977.86] source you can go to coder.com get a
[3977.86 → 3980.94] demo or try it right now or even start a
[3980.94 → 3984.02] 30-day trial of coder enterprise once
[3984.02 → 3987.92] again coder.com that's c-o-d-e-r.com
[3987.92 → 3989.38] coder.com
[3989.38 → 4009.98] well there's a terminal app I haven't seen
[4009.98 → 4011.74] visuals of this yet how cool is this
[4011.74 → 4013.40] terminal have you seen it I'm excited for
[4013.40 → 4015.32] a terminal app I think that's an it's very
[4015.32 → 4017.16] hacker I like that yeah if you go to
[4017.16 → 4019.10] zoom.com slash apps you'll get it you'll
[4019.10 → 4021.28] see a link to it there you go okay
[4021.28 → 4027.02] terminal beta cool it's very two we like
[4027.02 → 4030.16] jarred obviously it's an application I do
[4030.16 → 4032.48] like two is it's an official terminal
[4032.48 → 4035.30] client written in python seems like Zulip
[4035.30 → 4037.64] is almost entirely written in python except
[4037.64 → 4040.96] for that flutter part and that web app of
[4040.96 → 4044.68] course has to be typescript but you guys
[4044.68 → 4047.70] have python roots yeah Zulip is one of the
[4047.70 → 4050.92] first kind of major projects to be using
[4050.92 → 4055.82] um MYP static typing and uh python
[4055.82 → 4058.64] so we're engineers we're part of developing
[4058.64 → 4061.38] that awesome I'm just staring at your
[4061.38 → 4064.42] terminal UI now so I've become I've seen a
[4064.42 → 4066.32] squirrel and I've become distracted I forgot
[4066.32 → 4069.06] to continue talking to you what I'm seeing
[4069.06 → 4070.68] on the side though if I can talk through a
[4070.68 → 4071.84] little bit and see if you're following me
[4071.84 → 4073.40] jarred is that it seems like you've got
[4073.40 → 4076.20] the top the channels of course and it
[4076.20 → 4079.10] seems like those are topics beneath it
[4079.10 → 4081.08] potentially obviously it's not as full
[4081.08 → 4084.52] featured as a actual web UI or an
[4084.52 → 4087.34] application UI do you find that people
[4087.34 → 4089.10] actually use this terminal app a lot is
[4089.10 → 4091.84] it is it one of a primary client set that
[4091.84 → 4094.44] you have in your stats and what do
[4094.44 → 4096.10] you think the usage might be I don't I don't
[4096.10 → 4097.96] have a number handy for you, I mean folks
[4097.96 → 4100.18] do use it definitely not as much as their
[4100.18 → 4102.98] other clients but if you know for sure i
[4102.98 → 4104.78] guess sort of philosophically I would say
[4104.78 → 4108.52] one piece of it is that you know we've
[4108.52 → 4110.38] talked about how just how much time folks
[4110.38 → 4114.14] are spending in chat and so having that
[4114.14 → 4117.66] chat experience feel pleasant and natural and
[4117.66 → 4119.80] sort of do what you want I think is really
[4119.80 → 4121.68] really important like you don't want to be
[4121.68 → 4123.58] like annoyed and frustrated by something
[4123.58 → 4125.86] in an app you're using you know every
[4125.86 → 4129.78] day, and so we do believe in like giving
[4129.78 → 4132.38] folks flexibility and options and
[4132.38 → 4134.84] configurations and different ways to you
[4134.84 → 4137.50] experience Zulip that sort of matches well
[4137.50 → 4140.00] with their workflows and I would say having
[4140.00 → 4142.72] a terminal app as part of that just like
[4142.72 → 4145.12] for some folks that is really like the
[4145.12 → 4146.84] natural way for them to engage with a piece
[4146.84 → 4149.48] of software, and it feels really smooth and
[4149.48 → 4152.70] and kind of how they want to
[4152.70 → 4154.86] experience it, and so I think that's really
[4154.86 → 4156.62] valuable just because people are
[4156.62 → 4158.64] different like we can't, we can't make an
[4158.64 → 4162.06] app that you know is just one way and works
[4162.06 → 4164.10] perfectly for everybody like there has to be
[4164.10 → 4165.76] flexibility for folks to engage with it in
[4165.76 → 4168.02] different ways if we can use this GitHub repo
[4168.02 → 4171.34] as a proxy for usage I would say there are
[4171.34 → 4174.46] people using this it has over 600 stars but
[4174.46 → 4179.96] most notably 871 merged pull requests and 165
[4179.96 → 4183.44] open pull requests, so people are working on
[4183.44 → 4187.02] this people are collaborating on this and of
[4187.02 → 4188.76] course people only work on and collaborate on
[4188.76 → 4190.88] software if it's useful and being used by
[4190.88 → 4192.82] folks this is not an afterthought this is
[4192.82 → 4195.46] very much an officially supported thing with
[4195.46 → 4198.74] 77 contributors so pretty cool yeah and we
[4198.74 → 4200.60] had we had multiple interns working on it this
[4200.60 → 4203.78] summer so yeah it's definitely interacted open
[4203.78 → 4205.54] that's awesome tell us about the team tell us
[4205.54 → 4207.42] about the company and all the people
[4207.42 → 4210.42] involved yeah so we have a pretty small
[4210.42 → 4214.20] kind of core team of folks who are you
[4214.20 → 4217.12] know paid full-time to work on or full-time or
[4217.12 → 4220.50] part-time I guess to work on zoo lip, and we do
[4220.50 → 4223.70] think that's really important kind of as part of
[4223.70 → 4227.78] of our model that there is a team of really kind of
[4227.78 → 4231.34] really talented expert engineers and other
[4231.34 → 4235.30] folks who are for whom this is their day job it's
[4235.30 → 4237.84] really hard to run a project where it's kind of a
[4237.84 → 4242.22] side gig for everybody so with this core team we've
[4242.22 → 4246.50] also invested a lot into making it really easy for
[4246.50 → 4248.86] folks to get started contributing to zoo lip so
[4248.86 → 4252.66] there's been a huge amount of investment into creating the
[4252.66 → 4257.16] space for a really active really lively community around it as
[4257.16 → 4261.26] well and that comes in terms of like tons and tons of documentation i
[4261.26 → 4263.76] think you saw some of our production documentation there's
[4263.76 → 4265.86] also tons of contributor side documentation
[4265.86 → 4269.68] from you know as you mentioned how systems work but also just the
[4269.68 → 4272.88] contribution process what a good pull request looks for like
[4272.88 → 4275.70] for us kind of everything about that process and that's really
[4275.70 → 4279.10] something that we put a lot of thought into like what is that process of
[4279.10 → 4283.14] contributing and how do we make that a really excellent experience
[4283.14 → 4288.02] both for us in terms of kind of reviewing the work and for the
[4288.02 → 4291.60] contributors themselves and make that a really great like positive
[4291.60 → 4296.82] experience great learning experience for folks so yeah so for example with a
[4296.82 → 4302.84] team of on the order of like 15 paid team members we had 124 people
[4302.84 → 4305.88] contribute to our last major release so that's like around a six-month
[4305.88 → 4310.82] cycle so it's a lot of folks who are either doing some of them are doing
[4310.82 → 4314.90] kind of formal internship program with us, we're we've been participating in
[4314.90 → 4319.04] google summer of code for the past for a number of years now I don't know if
[4319.04 → 4324.54] you're familiar with it but basically google funds internships for open source
[4324.54 → 4328.42] projects as well as kind of managing that overall structure of helping folks
[4328.42 → 4334.54] find projects to work on so that's been amazing for us, we have generally most
[4334.54 → 4339.64] years we have about 15 to 20 interns most of them mentored by kind of alumni of
[4339.64 → 4344.22] the program or other community members and that's been another like really great
[4344.22 → 4348.74] way for us to bring folks into the community and so yeah it's, but it's
[4348.74 → 4353.22] you know loop is open source not just in the sense of like the code being open but
[4353.22 → 4357.46] really just in our whole model of how we develop the product and how we engage
[4357.46 → 4362.12] with contributors how we engage with our users you know one time I guess one of
[4362.12 → 4367.56] our folks who joined recently he started out as an intern and then I joined as a
[4367.56 → 4373.34] full-time team member, and he commented that he was surprised when he got added to
[4373.34 → 4377.68] kind of all our private company channels just how little traffic there is in those
[4377.68 → 4383.48] channels like he was thinking that you know we when we were giving him feedback on
[4383.48 → 4386.88] things he was working on maybe we're like somewhere off on the side discussing that
[4386.88 → 4390.88] amongst ourselves and then like providing the summary version he was like oh wait no
[4390.88 → 4395.02] that's not how it works I was like no, no no yeah we if we're talking about how the
[4395.02 → 4399.02] product should work we just talk about that in the open, and you know that way
[4399.02 → 4403.52] everybody can kind of see understand the decisions can can contribute to the
[4403.52 → 4408.20] decisions like yeah we're very like non-hierarchical in terms of it's really
[4408.20 → 4412.54] about what your ideas are and how clearly you communicate them and explain to them
[4412.54 → 4417.58] not you know what your title is or how long you've been involved with Zulip or
[4417.58 → 4422.28] anything like that it's really about kind of working together to come back to come to
[4422.28 → 4426.52] the best decision we can about how something should work yeah let me know if
[4426.52 → 4429.68] it didn't quite answer everything all the parts of your question but she
[4429.68 → 4435.32] answered your question jerry yeah okay what's stopping you from or have you
[4435.32 → 4442.00] considered raising funds I know you had grants in the past but I'm not sure what
[4442.00 → 4446.58] your angle is I mean there's obviously this idea of commercial open source
[4446.58 → 4452.40] companies out there we're very anti rug pull not cool here around these parts
[4452.40 → 4455.78] which means don't change your license once you've gotten to critical mass because
[4455.78 → 4460.68] it's against your future business objectives hopefully I paraphrased that well
[4460.68 → 4465.02] enough for you jarred I think there's an opportunity I'm just curious have you why
[4465.02 → 4469.54] haven't you what's the status on that front yeah absolutely yeah so we have
[4469.54 → 4476.20] intentionally not raised VC money and do not plan to raise VC money and what we're
[4476.20 → 4481.48] in terms of the business model what we want is just to build a sustainable company on top
[4481.48 → 4485.56] of this open source project so we've discussed some paid plans we have on the cloud side on
[4485.56 → 4491.36] the self-hosted side you know services we can provide and so that's really our strategy to
[4491.36 → 4497.36] have our users pay for the software and then that that funds the development of the
[4497.36 → 4504.76] project and the product and kind of key reason we don't want to go the VC route is that we feel
[4504.76 → 4509.38] that kind of misaligns the incentives there's a misaligned kind of inherent misalignment of
[4509.38 → 4515.32] incentives so for us, we're we're not going to take a hundred swings at this you know we're not gonna
[4515.32 → 4520.58] like try to build a hundred different products and see which ones land and abandon ones that don't
[4520.58 → 4525.64] we really are building Zola because we think it's a better way to work, and we're really
[4525.64 → 4531.60] committed to making that around for our users for the long term so as you know as I mentioned like
[4531.60 → 4537.86] we still have users from 2013 who are on Zola now, and we want that software to be around for the
[4537.86 → 4544.52] long run, and so we want to just take that one single bet and make it work whereas VCS their incentives
[4544.52 → 4548.88] are you know they're looking for like the next you know your next Facebook your next like giant
[4548.88 → 4556.14] company that just explodes, and they're willing to take big risks in order to have that probability of
[4556.14 → 4563.88] a really remarkable amazing return whereas for us, we want to take very small risks and have a very
[4563.88 → 4571.26] high probability of kind of success without necessarily aiming for that like galactic outsized
[4571.26 → 4576.42] return right um we just you know their main priority is really to get to a point where
[4576.42 → 4582.28] the software we have enough you know we're making money to really continue to develop the software
[4582.28 → 4587.58] and have the staffing and the team that we want, and it doesn't have to be you know stratospheric
[4587.58 → 4592.64] and of course we would like to reach as many people as we can, and we think it can benefit lots and lots
[4592.64 → 4596.28] of different kinds of organizations it's a huge market there's definitely tons of opportunity
[4596.28 → 4602.36] but just like the kinds of risks are we're comfortable taking to get there are very different from the kinds
[4602.36 → 4609.32] of risks VCS would feel comfortable taking to get there what if that's not true which part all of
[4609.32 → 4614.90] it what if there are venture capitalists that align with open source which is becoming a thing what if
[4614.90 → 4622.32] there are venture capitalists that see your idea as the way, and they want to fund companies that have
[4622.32 → 4629.76] proved by cold at hands aspects to open source would your tune change well I think it's not
[4629.76 → 4634.92] just about open source like i I think there are now starting to be VC firms that are focused on open
[4634.92 → 4641.12] source and really buy into that model, but it's also just kind of the structure of how
[4641.12 → 4648.82] and how you do that investment right so do you try to like to hire up really quickly spend tons of money
[4648.82 → 4656.10] you know in marketing even if it's uh the return on is not there but just to get that growth curve
[4656.10 → 4660.46] you know like what are you what are you trying to do right and like what is your strategy to get
[4660.46 → 4667.76] there you know I'm not like I'm not going to tell you a hundred percent never in the next hundred years
[4667.76 → 4673.66] will take VC money whatever we're a small company right like we do to some extent like
[4673.66 → 4678.84] kind of like make our decision make decisions about things when we need to make them not you know
[4678.84 → 4685.36] planning things for 50 years ahead but just that has been our kind of strategy so far and from
[4685.36 → 4691.24] we have not seen we've not been approached for by a venture investor who we think would be
[4691.24 → 4694.84] completely different from all the other venture investors such that we would start thinking about
[4694.84 → 4702.38] it I think the reason why I come with those questions is less to challenge you by any means it's like
[4702.38 → 4710.54] zero about challenging, and it's more like if Zulip is the best, and it is open source, and it is
[4710.54 → 4718.76] superior in so many ways in so many models even of how you can use the software not just in your cloud
[4718.76 → 4723.92] or in the self-hosted version the exporting the non-fettered access to it to be able to move and
[4723.92 → 4730.82] all those things if it's superior I would want to if it were me I would want to do all I could to ensure
[4730.82 → 4737.38] everyone could use it more and the way you get there is generally the reason why people raise money
[4737.38 → 4741.92] is not because they literally just want money it's because they can leverage that money as a resource
[4741.92 → 4747.62] to go faster to the roadmap, and we talked earlier about flutter we talked earlier about some
[4747.62 → 4751.44] different areas, and maybe you're slow and steady and that's okay and there's nothing wrong with that
[4751.44 → 4760.88] I just wonder if is uh is a little funding that was in alignment with your morals values etc towards
[4760.88 → 4766.70] open source the way you run your company if that money didn't challenge those values if things would change
[4766.70 → 4774.18] because if you truly are better, and we've seen even in our own slack a person say infinitely better
[4774.18 → 4781.50] than x you know so we hear that ourselves even if that's truth then I would want to do all I could to
[4781.50 → 4787.78] get that truth to many people yeah, and we're definitely um so we're not currently raising money but we
[4787.78 → 4792.74] definitely are currently exploring sort of kind of different strategies on the go-to-market side and
[4792.74 → 4797.24] that's something that we're thinking very actively about the sort of how do we increase that reach
[4797.24 → 4803.72] and grow faster in terms of you know kind of finding different ways to introduce folks to
[4803.72 → 4807.54] Zulip and to reach more people so that's definitely a major priority for us right now
[4807.54 → 4811.72] yeah that has to be one of your biggest challenges is like nine out of ten people don't know who you are
[4811.72 → 4816.42] yeah right yeah no it's true it's true yeah it is a major challenge no offence but I mean
[4816.42 → 4821.74] even for sure most things nine out of ten people don't know what it is for sure yeah yeah yeah I mean
[4821.74 → 4828.00] there are tons of things we're trying and I like the I like the free for open source education etc that
[4828.00 → 4831.72] you already discussed what are some of your other ideas what are some of the things you're thinking
[4831.72 → 4838.34] of trying to get more people to know what Zulip is to make Zulip a household name I mean some of them
[4838.34 → 4845.02] are kind of standard things so like advertising paid advertising going to conferences and various kinds
[4845.02 → 4851.98] of events and sharing Zulip that way one thing that another direction is kind of content so we
[4851.98 → 4857.54] are starting we've had blog posts on various topics we're starting to you know one of the things that
[4857.54 → 4863.04] I talked to you can see probably see my excitement about is this kind of side of community management
[4863.04 → 4870.20] and getting folks engaged in an open source project so uh for example like we're working on some
[4870.20 → 4874.38] partnering with some organizations on blog posts around that kind of thing and so
[4874.38 → 4881.62] just kind of getting the name out there in whatever way um because I think you know the as you were
[4881.62 → 4886.58] saying kind of the brand recognition and just kind of awareness matters so that when not everybody's all
[4886.58 → 4892.14] people aren't like constantly in the market for a new team chat, but we want to be top of mind when
[4892.14 → 4896.70] when they are starting to think about it and when it does come up but yeah I don't I would say I don't
[4896.70 → 4903.12] we don't necessarily have kind of like you something unique other than you know we do have this open
[4903.12 → 4907.84] source angle and so things engage in the community and like the open source community more broadly and
[4907.84 → 4914.30] sponsoring open source projects is definitely like one angle um for us that we're investing in
[4914.30 → 4919.30] well it's one of the hardest nuts to crack and everybody out there is trying to crack that same nut
[4919.30 → 4926.18] aren't they and so there's a lot of noise there are a lot of competing voices, and you definitely have a lot
[4926.18 → 4933.04] going for you, I think they're I think leaning in on community and open and I think moderation as Adam said
[4933.04 → 4940.82] earlier as you guys continue to flesh out the product those are all good strategies if there was a magic
[4940.82 → 4945.40] carpet that you could go on it would automatically get you to brand awareness of course we'd all just
[4945.40 → 4951.74] hop on that magic carpet exactly but in general our style is just tried to be really like as clear and direct
[4951.74 → 4957.26] as we can that's really our focus for all our kind of marketing and so on just we think the value is
[4957.26 → 4961.86] there for folks and if we can communicate that clearly we don't get need to get super marketing
[4961.86 → 4968.24] super sales just yeah yeah tell folks what's there very cool Adam anything else from you, i just to
[4968.24 → 4973.82] add on to what you're seeing here jerry I think probably without digging into the data I will hypothesize
[4973.82 → 4982.06] that probably the biggest challenge first is awareness that you exist and then obviously once
[4982.06 → 4987.84] they realize you exist you know the opportunity for superior feature sets then I would say that the
[4987.84 → 4995.80] very next thing is like okay now what which is our requests for information on hypothetically what it
[4995.80 → 5003.66] would take to move what it would take to go from a slack or a discord I feel like if you could do content
[5003.66 → 5011.34] around that subject not just documentation like how to but like good stories of folks who've moved
[5011.34 → 5018.84] and their journey and to demystify the scares and concerns like my main scare is that a proper
[5018.84 → 5023.78] adjective I don't know I'll allow it is that or I guess anxiety point is will we lose the people
[5023.78 → 5030.08] that we have in our community will they bounce you know if you can showcase the what's on the
[5030.08 → 5038.44] other side of the wall rather than me assume as somebody who is not happily but happily using slack
[5038.44 → 5044.22] given the things we've already said still like slack it's still amazing it's just they got warts for
[5044.22 → 5049.04] people like us communities like us, I feel like that's the content I would personally I would look
[5049.04 → 5054.32] at the data and I think that would be the hypothesis get awareness show off the amazing feature set that
[5054.32 → 5061.88] really captures 80 of who likes you most and then show how easy it is to move and almost make it like
[5061.88 → 5068.06] you should be doing this like it should happen today we can help you and if there's money to invest
[5068.06 → 5075.58] in quotes money to invest could be time could be people could be people hours is to guide and assist
[5075.58 → 5081.96] certain organizations on that path yeah and some of what you described we do have case studies on our
[5081.96 → 5086.08] site where a lot of folks talk about starting initially with something else and then
[5086.08 → 5091.30] moving over to Zulip and sort of that experience um but parts of what you said you're kind of reading
[5091.30 → 5096.82] off of the to-do list I was working on yesterday just yesterday okay cool yeah literally just yesterday
[5096.82 → 5101.92] yeah I was thinking you know we have some content in our help centre about that migration path but
[5101.92 → 5107.32] we definitely need more clarity on just kind of bring all those pieces of information together and
[5107.32 → 5113.16] like coming from different kinds of tools here are the steps you take and just yeah like folks
[5113.16 → 5118.26] have a lot of folks are busy there's a lot going on here you know the extent that we can make that easier
[5118.26 → 5125.00] for people like it can make a big difference if I had to divide my time up into fifths I'd take two
[5125.00 → 5130.80] fifths of that time and dedicate that kind of content uh-huh if not more uh-huh because fourths is like
[5130.80 → 5135.64] whatever you know like 25 25 I mean that's pretty easy like one fourth yeah I feel like two fifths
[5135.64 → 5141.76] sounds better to me two fifths of my time would be focused on uh awareness and showing off the
[5141.76 → 5151.88] better world the FOMO yeah you're missing out yeah on freedom control access enjoyment privacy and then
[5151.88 → 5159.08] obviously your dev team and engineering teams can be focused on all the surface area flutter that
[5159.08 → 5165.62] migration finishing out those applications polishing the peripherals your dev team does a great job
[5165.62 → 5171.28] on documentation compared to what I've seen a lot of projects we see a lot of open source projects
[5171.28 → 5179.02] the documentation is perfect the readies are very deep and detailed and organized thoughtful
[5179.02 → 5185.14] and so obviously you want your dev team to be diving that's what they're there for but as much as they
[5185.14 → 5192.26] can write about what you're doing technically decision-making architectural stuff not just in
[5192.26 → 5197.58] documentation form but in content form I think that would pay off dividends as well and obviously can
[5197.58 → 5205.46] can also double as documentation in a certain way cool well what's next yeah exactly what is next
[5205.46 → 5212.18] next for you the listener are you going to go to zulip.com at the .com it's a big deal it is .com
[5212.18 → 5221.48] yeah it's a big deal it's a five letter .com free open source cloud or self-host unfettered do it today
[5221.48 → 5230.04] and if you think we should switch to Zulip hop in our slack yes happy to at least try that docker image
[5230.04 → 5234.88] I mean I'm going to give Adam a to-do you know see if you can get it running on docker yeah on your
[5234.88 → 5240.28] home lab or fly and just toy around with it see how it feels try it on for size you know yeah I mean or if
[5240.28 → 5245.52] you want to just try out it literally takes less than two minutes to create an organization's little
[5245.52 → 5249.82] cloud, and then you can just poke around and experience it for yourself it's almost too easy
[5249.82 → 5255.40] Adam it's almost too easy yeah I feel like we should try cloud out first and uh and if we like how it
[5255.40 → 5261.80] feels take the next step yeah yeah that's half the battle right it you know because sometimes that
[5261.80 → 5266.56] switching of the UI and everything it can be jarring the ideas and the features that may be there but
[5266.56 → 5271.06] maybe it feels weird I don't now and then give us feedback that's the other thing
[5271.06 → 5276.64] if you is there's anything that feels off or feels confusing just come by the development community
[5276.64 → 5281.44] and tell us, and we'll, we'll try to fix it well very cool well thank you for this time thank you
[5281.44 → 5285.48] for going through all the details with us, it's awesome, thank you for the great set of questions
[5285.48 → 5295.04] in a world where open source is eating software faster than software is eating the world there's
[5295.04 → 5303.40] the open source chat that has the potential to unseat the giants to at least unseat the giants
[5303.40 → 5311.30] based upon features that really matter to users and the thing is that they have so much potential
[5311.30 → 5319.96] what exactly is potential is kinetic energy stored waiting to be released and after
[5319.96 → 5325.52] this conversation I'm so hopeful for the team at Zulip but at the same time I know it's kinetic
[5325.52 → 5331.62] stored energy potential not realized now there are a lot of people who love Zulip and there are a lot
[5331.62 → 5337.60] of people who don't even use Zulip or even know about Zulip, but now you do so what are you going to do
[5337.60 → 5345.98] well I say go to zulip.com check it out try it out self-host it use their cloud contribute be a part
[5345.98 → 5351.36] of the community all the things that open source provides now i, for one, am very hopeful and very
[5351.36 → 5361.88] happy Zulip exists but Microsoft slack Salesforce they're massive, and so they need us to step in to
[5361.88 → 5369.20] use to try to contribute all the things well make sure you check them out zulip.com and all it was
[5369.20 → 5375.14] inspired by this conversation to create a brand-new guide called moving to Zulip and that'll be linked
[5375.14 → 5383.42] up in the show notes for your okay sponsors for today big thanks to century dot Io use our code
[5383.42 → 5391.60] change law to get three months almost four months of the team plan for free again century dot Io
[5391.60 → 5401.42] and the code is change law and also to our friends at fly we love fly dot Io it is the platform
[5401.42 → 5409.82] where you could do pretty much anything and Tigris is one example of that check them out at Tigris
[5409.82 → 5419.62] data.com we're using it, and we love it and to our friends at paragon use paragon.com all these sass
[5419.62 → 5427.28] integrations you need for your b2b sass again use paragon.com and to our friends over at coder
[5427.28 → 5434.32] coder.com cloud development uncompromised they're the number one self-hosted cloud development
[5434.32 → 5440.02] environment out there I checked it out I think it's so awesome what coder can do check them out
[5440.02 → 5447.10] coder.com and of course the beat freak in residence break master cylinder bringing those beats
[5447.10 → 5455.28] every single week much love BMC much love okay so no bonus today but I do want to mention
[5455.28 → 5464.50] because hey why not changelaw.com slash plus it's better it is better today it's not better
[5464.50 → 5471.72] because there's no bonus but hey other weeks other shows bonuses galore for our plus subscribers
[5471.72 → 5478.62] that is where you go to get the ad free version of our show the way to directly support us to get
[5478.62 → 5485.40] closer to that cool change law metal get bonus content not this week but hey you know next week
[5485.40 → 5492.18] and I know because we recorded next week's show today, and we have a very lengthy very awesome
[5492.18 → 5499.94] bonus content for you, you'll love it if you're a subscriber once again changelaw.com slash plus
[5499.94 → 5505.94] okay that's it this show's done thank you for tuning in, and we will see you on Friday
[5506.36 → 5507.36] you
[5507.36 → 5524.08] also
[5524.08 → 5531.54] you
[5531.54 → 5533.54] Game on!
