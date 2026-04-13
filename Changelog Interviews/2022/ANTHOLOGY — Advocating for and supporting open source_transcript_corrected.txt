[0.00 → 10.20] This week on The Change love, we're taking you to the hallway track of All Things Open 2022
[10.20 → 14.72] in Raleigh, North Carolina. Let me set the stage. This is what we do when we go to these conferences.
[15.10 → 19.06] We set up our podcast studio at our booth where all the other vendors are. We give out t-shirts,
[19.22 → 23.28] stickers, pins, high-fives. We're there to cover the hallway track and meet everyone we can.
[23.64 → 28.70] Today's anthology episode from All Things Open features Arun Gupta, VP and GM of Open
[28.70 → 33.94] Ecosystem Initiatives at Intel, longtime friend Chad Whitaker, head of open source at Century,
[34.40 → 40.20] and Ricardo Suárez, principal advocate in open source at AWS. The common denominator for each
[40.20 → 46.12] of these conversations is advocating for and supporting open source. A big thank you to our
[46.12 → 50.14] friend Todd Lewis and his team for inviting us to come back to All Things Open. We enjoyed meeting
[50.14 → 55.02] longtime fans and new ones too. And of course, a massive thanks to our friends and partners at
[55.02 → 60.44] Vastly and Fly. Bandwidth for Change love is provided by Vastly. Learn more at Fastly.com.
[60.72 → 64.32] And our friends at Fly let you put your app and your database closer to users all over the world
[64.32 → 67.50] with no ops required. Check them out at fly.io.
[67.50 → 81.40] This episode is brought to you by Influx Data, the makers of the InfluxDB time series platform.
[81.40 → 86.76] With its data collectors and scripting languages, a common API across the entire platform,
[87.14 → 92.06] and highly performant time series engine and storage, InfluxDB makes it easy to build once
[92.06 → 97.14] and deploy across multiple products and environments. The new InfluxDB storage engine allows developers
[97.14 → 102.38] to build real-time applications even faster and with less code, faster write and query performance
[102.38 → 106.76] with a new purpose-built columnar time series database that combines a hot, compressed,
[106.76 → 113.00] in-memory data store and a cold object store. Unlimited cardinality lets you slice and dice
[113.00 → 117.80] on any dimension without sacrificing performance. And more options than ever to query data,
[118.02 → 123.28] including native SQL support. If you want to learn more and see how the new InfluxDB engine works,
[123.28 → 130.90] sign up for the InfluxDB beta program at influxdb.com slash changelog. Again, influxdb.com slash changelog.
[130.90 → 139.56] Let's talk about Intel because Ah-
[139.56 → 148.10] Let's talk about Intel, because Ah-
[148.10 → 162.42] Let's talk about Intel, because when I think of Intel, I think of an industry giant.
[162.42 → 163.78] I think of microchips.
[163.78 → 165.36] I think of Intel inside.
[165.86 → 166.04] Yes.
[166.10 → 166.72] I think of hardware.
[167.54 → 173.58] I don't think of open source much, but I guess you're changing that narrative, helping us
[173.58 → 177.70] understand what Intel does for the developer communities, for the open source community.
[178.10 → 178.60] Et cetera.
[179.04 → 179.24] Yeah.
[179.44 → 182.12] No, I mean, I joined Intel about six months ago.
[182.72 → 185.24] I run the open ecosystem team at Intel.
[186.08 → 191.08] And the funny part is, I call my role as chief storytelling officer.
[191.34 → 191.62] Okay.
[191.62 → 195.42] And now Intel has done open source for over two decades, actually.
[196.06 → 198.98] We were influential in creating Linux Foundation.
[199.78 → 204.18] We are part of 700 plus open source foundation and standard bodies.
[204.18 → 209.52] For the last 15 years, we are the top corporate contributor to Linux kernel.
[209.76 → 210.02] Really?
[210.40 → 213.36] We are among the top 10 contributors to Kubernetes.
[214.28 → 219.80] We are among the top contributors to OpenJDK, PyTorch, TensorFlow, LLVM.
[220.42 → 224.42] These are the projects that sometimes you don't realize that Intel is contributing.
[224.66 → 224.86] Yeah.
[224.86 → 226.98] So we have always been there.
[227.24 → 231.68] So my role really here is to make sure we tell the story better.
[231.86 → 231.96] Right.
[231.96 → 232.14] That's it.
[232.58 → 234.46] This is a challenge for many brands in tech, really.
[234.52 → 238.78] I mean, they have such a focus on selling their product that they forget to tell their
[238.78 → 239.12] story.
[239.38 → 239.54] Right?
[239.54 → 240.52] And I think that's part of the story.
[240.58 → 246.02] It's like, you're not just the microchip manufacturer that you are and like the heartbeat of most computers.
[246.54 → 247.72] It's beyond that.
[247.72 → 252.52] It's the community partner, community citizen, and like, how are you cohesively involved?
[252.90 → 255.32] I think brands just forget to really tell that part of the story.
[255.42 → 258.36] And they just, the chief storytelling officer, I think is an amazing title.
[258.44 → 262.62] We should have more out there because that's kind of what marketing does, but it's not their
[262.62 → 263.00] job.
[263.06 → 267.86] Their job is to like help people be aware what the product is, not necessarily brand story,
[268.00 → 269.24] but they kind of go together.
[269.34 → 272.78] How do you deal with that challenge with like marketing and storytelling and whatnot?
[272.78 → 273.14] Very much so.
[273.14 → 278.92] And actually the part, and I work with our marketing team very closely, helping them
[278.92 → 284.98] understand that mind share is what gives you market share, helping them build that understanding
[284.98 → 291.94] that funnel is very important because all along, I mean, over the 20 years, open source
[291.94 → 295.58] has only grown, and it is sort of the primary way.
[296.04 → 298.24] Open source developers are the new decision makers.
[298.50 → 300.86] You no longer go to CIOs, and they say, you know what?
[301.08 → 301.60] Sign a bill.
[302.08 → 302.14] Right.
[302.14 → 305.92] If the developers are happy, if they are engaged in the, exactly, if they're engaged
[305.92 → 310.20] in the community, if you have showed them the right skills, they're going to make the
[310.20 → 311.32] change in the organization.
[311.66 → 316.56] And most of the time, these days, developers are building their applications on a CSP, Amazon,
[316.74 → 319.04] Microsoft, Google, private cloud, whatever, edge.
[320.02 → 324.46] Intel is prominent across all of these, you know, Intel architecture is prominent across
[324.46 → 325.40] all of these venues.
[325.66 → 325.88] Yeah.
[326.00 → 330.76] And that's exactly, you know, what we do is we contribute to all the projects that I talked
[330.76 → 332.32] about earlier.
[332.32 → 337.22] We want to make sure that these open source communities are fully optimized and run in
[337.22 → 339.06] the most efficient manner for the developers.
[339.94 → 341.40] We just have to do a better job of storytelling.
[342.10 → 345.54] Do you get involved in the OSLO related matters?
[345.68 → 347.48] Like we had Chad Whitaker on from Century earlier.
[347.54 → 349.54] He's talking about their, how they give back.
[349.60 → 352.44] And it's $2,000 per developer they have on their team.
[352.50 → 356.06] Now, obviously, Intel's probably got more than 2,000 developers.
[356.06 → 358.86] I don't know, how many developers does Intel have at large?
[358.98 → 359.20] You know?
[359.62 → 362.92] So Intel has over 19,000 software engineers.
[363.70 → 363.98] Wow.
[364.08 → 365.78] Over 19,000 software engineers.
[366.26 → 368.60] And OSLO is part of my team.
[369.16 → 371.46] So one of the teams I have is open source program office.
[371.90 → 375.56] I've actually built and ran OSLO's at Amazon and Apple.
[375.80 → 376.04] Okay.
[376.04 → 382.46] So I've built my career over the last 20 years all exclusively on open source.
[382.58 → 384.46] So I kind of been around for a while.
[384.60 → 384.72] Yeah.
[385.00 → 391.06] And here, honestly, the part that gets me most excited is Intel has done so much in the open
[391.06 → 391.72] source world.
[392.24 → 396.52] When I was given an offer to join Intel, it's like, what does Intel do in open source?
[396.88 → 400.26] And now I'm like getting goose bumpy moments every day.
[400.30 → 400.66] Is that right?
[400.66 → 405.84] As I talk to maintainers, as I talk to executives across the company, we just got to do a better
[405.84 → 406.46] job of storytelling.
[406.68 → 407.96] So how long have you been at Intel then?
[408.06 → 408.86] Over six months now.
[408.92 → 409.26] Six months.
[409.34 → 409.50] Okay.
[409.92 → 410.76] So you're getting started.
[411.44 → 412.54] I'm just getting warmed up.
[412.78 → 412.86] Okay.
[413.12 → 413.68] I'm just getting warmed up.
[413.68 → 420.60] So I guess the gift and the curse of a strong brand and a longstanding history is that it
[420.60 → 423.04] can be very, the gift is its strong and it's longstanding.
[423.16 → 425.74] And so you have this, like you've been cemented in the mind of people.
[425.86 → 427.96] The hard part is changing that perspective.
[428.30 → 433.88] You know, we've watched Microsoft transform slowly from evil empire into like open source
[433.88 → 436.16] supporting pioneers in certain senses.
[436.38 → 441.18] Some people still don't believe that narrative, but we've seen kind of the mind of developers
[441.18 → 444.64] slowly change about Microsoft over the last five, 10 years.
[445.32 → 450.54] And so I'm just wondering like how, how you attack the challenge of people who think Intel
[450.54 → 451.58] and don't think anything.
[451.82 → 453.10] We don't think about software.
[453.40 → 454.66] We don't think about open source.
[454.84 → 458.78] I had no idea that they contributed to Linux kernel and Kubernetes and all these things.
[459.34 → 461.08] And that's an awesome story.
[461.08 → 466.16] But like, how do you get that story out there and sustain it and actually get people to realize
[466.16 → 467.04] it and change their minds?
[467.36 → 467.46] Right.
[467.54 → 468.50] And that's exactly my job.
[468.60 → 469.00] That's exactly.
[469.00 → 474.98] So I have a OSLO team, which is all on the open source compliance processes part of it.
[475.34 → 476.42] I have an events team.
[476.84 → 479.72] So this event is sponsored by Intel out of my team and my budget.
[480.28 → 481.96] And we were at Rubicon last week.
[482.10 → 484.44] We're going to be at LF member summit last week, next week.
[485.12 → 487.34] I'm also part of several foundation boards.
[487.82 → 490.90] So I am on the CNCF governing board and the governing board chair.
[491.12 → 493.48] I'm also on the OpenSSH governing board.
[493.88 → 495.98] I'm the alternate on the Linux foundation board.
[495.98 → 501.96] So really meeting our industry peers, influencing the direction, wearing like an Intel t-shirt.
[502.12 → 502.42] There you go.
[502.74 → 508.12] Whatever story I tell, as long as you're wearing that Intel brand, it's a long journey.
[508.36 → 509.86] I'm not in it for the short run.
[509.96 → 510.20] Right.
[510.32 → 511.14] I'm a marathon runner.
[511.24 → 511.88] I'm not a sprinter.
[511.88 → 514.44] So I'm like really pacing myself.
[515.36 → 517.92] And open source developers are always skeptics.
[518.08 → 519.80] I am an open source developer myself.
[520.48 → 525.70] I need to hear that message through my multiple channels in order to start believing it.
[525.74 → 527.14] And see it for yourself for a while.
[527.24 → 527.48] Exactly.
[527.68 → 529.68] So that's sort of the approach here.
[530.10 → 534.02] That we're going to start making ourselves prominent across these different channels.
[534.42 → 535.28] Why it matters.
[535.46 → 536.38] How it matters.
[536.38 → 542.42] Because Kathy Zhang, she is part of the CNCF technical oversight committee, elected member
[542.42 → 542.86] over there.
[543.30 → 545.48] She gave a keynote at Rubicon last week.
[545.98 → 547.10] And I think she said it well.
[547.64 → 553.92] That we want to benefit the open source community as much as open source community has benefited
[553.92 → 554.28] us.
[554.98 → 556.24] So that's sort of the party line.
[556.42 → 556.64] Yeah.
[556.78 → 557.86] On how I see this going.
[557.92 → 558.08] Yeah.
[558.08 → 560.36] Because then you know it's a fair relationship.
[560.70 → 561.02] Symmetrical.
[561.62 → 565.92] Do you think part of your, I guess since you've got six months in so far, do you think part
[565.92 → 570.76] of your journey and part of your challenge with Intel might be changing the inside of
[570.76 → 574.82] Intel to more, better embrace open source and better understand the story?
[574.90 → 579.82] Like is there any uphill battle within Intel you have, not just externally, like getting
[579.82 → 583.92] other developers of the open source community to understand Intel's story in open source and
[583.92 → 587.82] how you support open source is part of your struggle and challenge from within?
[588.08 → 589.22] I don't think so at all, actually.
[590.02 → 590.96] If you think about it.
[590.96 → 591.32] That makes it easier.
[591.52 → 591.66] Yeah.
[591.72 → 593.16] No, I mean, it's the world changer.
[593.34 → 593.88] It's the game changer.
[594.06 → 596.54] Because you're so prolific, and you're so embedded, you personally.
[596.90 → 601.64] I wonder if like a lot of the gain and benefit is not so much just you, but you bring a lot
[601.64 → 602.36] to the table, right?
[602.38 → 607.26] You bring a lot of skin in the game, a lot of trust from press experience and how you've
[607.26 → 608.50] personally been in the trenches for so long.
[608.50 → 612.54] I just wonder if like is they're aligned, if your experience and what you bring and what
[612.54 → 615.50] Intel brings, obviously they're big, but do they align well?
[615.66 → 616.56] Maybe that's why you took the job.
[616.68 → 617.06] No, they do.
[617.18 → 617.42] They do.
[617.42 → 618.42] They very well do, actually.
[618.72 → 622.36] And throughout my career, I've always, like, I'm a runner.
[622.56 → 622.66] Okay.
[622.70 → 625.16] So as a runner, I like doing uphill runs.
[625.30 → 626.56] I don't like downhill runs.
[627.00 → 628.04] I mean, they're required.
[628.64 → 628.80] Yeah.
[629.06 → 629.58] How about flat?
[629.58 → 629.72] Yeah.
[629.78 → 630.58] Well, flat is okay.
[630.64 → 631.16] Flat is boring.
[631.68 → 631.84] Yeah.
[631.88 → 632.54] I'm an uphill runner.
[632.56 → 632.92] That's a percent great.
[633.02 → 633.84] I'm not much of a runner, though.
[633.84 → 633.98] Yeah.
[634.02 → 634.98] I love uphill runs.
[635.52 → 639.46] So, I mean, I really see this as an uphill run, and I'm really enjoying it.
[639.46 → 646.80] If you hear Pat and Greg Lavender, our CTO, talk about their strategy as the company is pivoting
[646.80 → 651.80] towards software-first narrative, open ecosystem is front and centre of the strategy.
[651.80 → 663.38] So having that top corporate alignment across the company, having a leader like Pat and Greg at the top with such a strong conviction, actually, you know, you don't have to do much.
[663.92 → 669.02] You just have to kind of rally up people, build the strategy and say, this is what we're going to focus on for the next year.
[669.02 → 672.54] So I think internal, they're always going to be naysayers.
[672.72 → 674.88] So you have to kind of work them along, nudge them along.
[675.42 → 679.80] And I've worked at companies like Amazon and Apple, build the open source narrative over there.
[679.96 → 681.90] So I'm not at all afraid in that sense.
[682.04 → 682.18] Yeah.
[682.32 → 690.78] But I think it's a lot going to be, how do we make ourselves accessible, available, transparent to the open source community so that they start believing us?
[690.86 → 694.96] Because, as they say, the first person to stop fooling is yourself.
[694.96 → 701.40] But we believe in this very strongly, and we hope that passion comes across clearly to the open source community.
[702.28 → 706.36] So you've talked a couple of ways that you're supporting open source developers.
[706.66 → 708.92] One is direct committing to the projects.
[709.06 → 713.06] Like, that's the best form of support is, like, we actually submit code to the Linux kernel.
[713.50 → 717.24] The other one is sponsoring events and conferences like this one.
[717.70 → 719.82] What are some other ways that Intel can support the community?
[720.22 → 720.50] Oh, yeah.
[720.60 → 723.64] I mean, like, code is king in open source communities.
[723.64 → 726.76] So contributing code is the best way by which we can do that.
[727.08 → 731.68] Sponsoring events is what makes this open source thrive, because that's where you find out about it.
[731.94 → 735.30] As I said, we are part of several foundations as well.
[735.58 → 737.24] So we continue to do that over there.
[737.36 → 738.80] We do a lot of open source mentoring.
[739.54 → 745.16] Multiple ways we engage, you know, pull request reviews, giving keynotes, you know, talking to other developers.
[745.94 → 750.36] And not just for us, but how do we make the broader open source community better?
[750.36 → 755.14] So that is sort of a personal goal of myself that I would love to do.
[755.24 → 757.52] I mean, I've been doing open source mentorship for a while.
[757.82 → 757.92] Yeah.
[758.02 → 759.02] We want to do more of it.
[759.52 → 762.68] So let's, like, as they say, the rising tide raised all the boats.
[762.90 → 763.02] Right.
[763.22 → 766.84] So I'm really looking at how can we raise all the boats together?
[767.08 → 767.28] Sure.
[767.28 → 775.66] So that's, you're still early, but what might that open source mentorship look like or manifest as, as you establish it?
[775.86 → 776.52] We don't know yet.
[776.60 → 778.18] I mean, it's very early in the cycle.
[778.40 → 778.68] Gotcha.
[778.68 → 787.30] But really the focus for now is going to be told that story in a very authentic, very connected, very transparent way.
[788.24 → 792.78] And course correct if that story is not gelling with the developers.
[793.32 → 797.18] Like, we can't go with a very strong mindset that this is our story.
[797.56 → 799.66] I'm always looking for change.
[800.20 → 801.22] You know, what is it gelling?
[801.32 → 802.18] What is it not gelling?
[802.18 → 802.68] What is it not gelling?
[802.68 → 806.64] And be able to tune our messaging, still keeping true to ourselves.
[807.10 → 808.60] What does your team look like?
[808.64 → 809.30] What do you break down?
[809.44 → 812.76] Like, the OSLO and other things that are involved under your role.
[812.88 → 813.68] Like, what is that like?
[813.72 → 814.58] How many people are involved?
[815.04 → 818.22] We don't share the number of people usually, but I have an OSLO team.
[818.32 → 821.04] That is for all typical OSLO-related functions.
[821.60 → 823.42] I have a community and a Derrel team.
[823.80 → 826.18] I know that maintains open.intel.com.
[826.26 → 828.78] That's our public-facing website, blogs, et cetera, over there.
[828.78 → 833.98] And I have a team that is all focused internal strategy and alignment, where we work across
[833.98 → 838.34] multiple Bus to bring them on the same page or understand what their strategy is.
[838.50 → 839.90] So a lot of internal alignment.
[840.54 → 840.64] Gotcha.
[841.28 → 841.72] All right.
[841.80 → 842.92] Belaboured segue here.
[843.00 → 845.14] You're talking about telling Intel's story.
[845.24 → 846.74] That's a communication skill.
[847.58 → 850.04] Communication skills are non-technical skills.
[850.28 → 853.68] You just gave a keynote about non-technical skills and how important they are.
[853.92 → 855.14] Let's talk about that.
[855.86 → 856.12] Sure.
[856.12 → 856.38] Yeah.
[856.44 → 864.18] Well, I mean, as I said in the keynote, non-technical skills are really a force multiplier to a technical
[864.18 → 864.62] skills.
[865.42 → 872.30] And in an open source community, which is so globally diverse, so inclusive, these non-technical
[872.30 → 874.04] skills are really your differentiator.
[874.24 → 874.58] Right.
[874.76 → 878.58] And in the keynote, I particularly talk about kindness and gratitude.
[879.48 → 884.28] I think as an industry, we don't do a good job of talking about kindness and gratitude
[884.28 → 884.84] enough.
[884.84 → 885.32] Yeah.
[885.48 → 889.18] We can only be more kind, only be more gratitude to us.
[889.56 → 894.50] So that's the skill I talked about and how that brings a more meaningful connection at
[894.50 → 894.82] work.
[895.32 → 901.30] How, you know, it gives you more serotonin, you know, how it produces endorphins as a
[901.30 → 903.90] painkiller, cuts down your cortisol level, all of that.
[904.50 → 909.80] So kindness and gratitude truly has benefits, you know, at work, at your personal life.
[909.80 → 914.84] But then later today at 12.45, I'm also giving a talk which talks about three other skills,
[915.40 → 918.50] communication, conflict resolution, and adaptability.
[918.86 → 918.98] Yeah.
[920.10 → 920.92] Conflict is a big one.
[921.06 → 922.28] It's a challenging one.
[922.28 → 928.86] So if you're looking at a non-kindness, let's say, how do you, give me an example of like
[928.86 → 932.50] a non-kindness and a way you would respond with kindness and an example of a kindness
[932.50 → 933.58] and gratitude when you speak of that.
[933.70 → 933.80] Yeah.
[933.88 → 934.32] So let's say.
[934.48 → 935.24] How do you see that manifesting?
[935.24 → 935.40] Yeah.
[935.50 → 939.66] No, I mean, in a work setting, particular work setting, let's say you see a new employee
[939.66 → 945.48] join in and them struggling out, you know, how to navigate the org or them not being able
[945.48 → 949.56] to ask a question because they feel threatened, they have an imposter syndrome, whatever it
[949.56 → 949.94] is, right?
[950.76 → 952.00] Just talk to them one-on-one.
[952.70 → 954.58] Just help them understand that, hey, you know what?
[954.64 → 955.46] I know you are new.
[956.16 → 957.60] Sometimes these things could be overwhelming.
[957.60 → 965.14] My son is a junior at Penn and as he did internship this year, he was saying, you know, I don't
[965.14 → 966.26] understand the org structure.
[966.82 → 969.22] So there was somebody else who helped him understand the org structure.
[969.58 → 970.92] So I think that's a simple example.
[971.22 → 975.42] You see somebody struggling, you offer help that, hey, I'm going to help you understand
[975.42 → 976.14] the org structure.
[976.66 → 981.72] And let's say if they are threatened to ask a question, if you are senior in the team,
[982.10 → 982.86] talk to your manager.
[982.86 → 987.60] That lets create space for these new people in the team who are early in their career.
[988.38 → 989.50] Give them that flexibility.
[989.78 → 992.40] Give them that space where they feel encouraged.
[992.88 → 995.40] You know, give them that psychological safety in the team.
[995.86 → 997.40] So I think that's a very simple act of kindness.
[997.62 → 1001.76] Like helping somebody, let's say a person new in their career, send a pull request.
[1002.30 → 1007.16] Say, hey, I'm going to volunteer to do a code review and really help them understand how
[1007.16 → 1010.38] code, lots and lots of examples that you can do on a day-to-day basis.
[1010.38 → 1015.74] So you're talking about conflict resolution, dopamine, serotonin, these are neuroscience
[1015.74 → 1019.20] related ideas and sciences, right?
[1019.26 → 1021.80] Do you study psychology, neuroscience?
[1022.18 → 1026.34] Like how do you up your game when it comes to this background knowledge?
[1026.50 → 1027.70] Yeah, no, I'm a runner.
[1027.94 → 1030.64] So I try to run every day or lift.
[1031.54 → 1035.84] And one of the things that I love doing running is listening to a lot of podcasts.
[1036.42 → 1039.62] So I listen to a lot of podcasts, particularly around mindfulness.
[1039.62 → 1040.18] Okay.
[1040.84 → 1045.96] There is a podcast by Dan Harris, who was an ABC News anchor for 20 years.
[1046.14 → 1051.32] He had a national breakdown on national TV, and he changed his career from a news anchor
[1051.32 → 1052.58] on Good Modern America.
[1053.22 → 1054.70] He runs a podcast on mindfulness.
[1054.84 → 1055.74] So I listen to a lot of that.
[1056.30 → 1058.14] And they talk about a lot of these elements over there.
[1058.60 → 1062.86] Then I also listen to a podcast by Adam Grant.
[1062.86 → 1065.98] He's an organizational psychologist at Wharton's.
[1066.40 → 1068.62] And he wrote the book, Rethink.
[1069.20 → 1070.74] And I listen to a lot of his podcasts.
[1070.88 → 1076.76] And pretty much the theory and the concepts behind these podcasts is what gets me excited
[1076.76 → 1078.38] that it truly is.
[1078.46 → 1082.90] You know, when you start reading the study behind it, that it actually releases those hormones
[1082.90 → 1084.24] that makes it so much better.
[1084.48 → 1084.70] Right.
[1084.70 → 1085.42] It's very exciting.
[1085.58 → 1090.60] And it's very, as they say, you know, it's a very eureka moment.
[1090.74 → 1091.84] Oh, I didn't realize it.
[1091.88 → 1092.52] It's so simple.
[1092.86 → 1093.00] Right.
[1093.10 → 1093.78] That's a true connection.
[1093.90 → 1095.48] I mean, people forget they have a brain, right?
[1095.86 → 1096.52] We're so human.
[1096.62 → 1097.76] We forget that we have a brain.
[1097.84 → 1100.64] The brain is the most powerful organism that we have in our body.
[1100.76 → 1103.24] If it didn't do what it does, we would not do what we do.
[1103.42 → 1103.64] That's it.
[1103.64 → 1105.20] And if you don't have your brain, you're not you anymore.
[1105.40 → 1110.64] Like, you're either maintaining it from your diet, your exercise, so that you don't have
[1110.64 → 1114.02] dementia or get, like, diseases that come from all these different things in life.
[1114.10 → 1116.66] And just, you know, over time, things happen to our human bodies.
[1116.66 → 1121.66] But we forget that our brain is just such a critical organ that we have that we're just
[1121.66 → 1123.40] like, we don't think to study it.
[1123.70 → 1126.50] You know, we don't think to understand how it works and how we work with it.
[1126.58 → 1126.74] Right.
[1126.88 → 1130.60] You know, and how it's so much is exactly who we are.
[1130.60 → 1136.54] And I think you brought up a perfect point over there because oftentimes we see the signals
[1136.54 → 1144.98] in our body that I'm not feeling, I'm feeling lethargic, or I'm gaining weight or my arms are
[1144.98 → 1145.78] not looking good.
[1146.10 → 1149.90] You can see those symptoms and start working out, physically working out.
[1150.42 → 1152.90] How do you recognize those simple for mental fatigue?
[1153.32 → 1153.44] Right.
[1153.52 → 1158.94] So I think as much as it is important for your physical well-being, it's very equally important.
[1158.94 → 1161.80] I would say rather more important for your mental well-being.
[1162.38 → 1167.78] So feeding your mind, this kind of content about general kindness, gratitude, you know,
[1168.00 → 1169.28] being a nicer person.
[1169.50 → 1172.34] I mean, end of the day, the summary is, just don't be stupid.
[1172.76 → 1173.50] Be a nice person.
[1173.74 → 1173.88] Yeah.
[1174.34 → 1175.32] And we forget that sometimes.
[1175.56 → 1175.62] Right.
[1175.82 → 1176.90] It does simplify down.
[1176.98 → 1182.42] I do like the way you described the difference between technical and non-technical skills in
[1182.42 → 1183.38] a way that's easy to understand.
[1183.38 → 1188.72] The technical skills are what we know, and the non-technical skills are who we are.
[1189.36 → 1193.18] We have tried and true methods for changing what we know, right?
[1193.24 → 1196.14] Like you put your head in a book, and you read it, or you go get some experience.
[1196.98 → 1200.44] Changing who you are can be a more difficult matter.
[1200.60 → 1204.44] Do you have any advice on changing yourself so that you improve your skills?
[1204.44 → 1211.30] And I think, unfortunately, over the last three, four years is where there are courses coming
[1211.30 → 1215.44] up where they talk about these non-technical skills that why they are critical.
[1215.80 → 1215.94] Yeah.
[1216.02 → 1218.18] But there is not a lot of material over there.
[1218.42 → 1224.64] I would say my personality has changed, evolved over the last few years as I have started listening
[1224.64 → 1225.74] to these podcasts.
[1225.74 → 1230.06] So I would really encourage people to find, to start reading about it.
[1230.32 → 1230.38] Right.
[1230.42 → 1236.14] And sometimes you don't realize how consciously, or subconsciously it starts impacting you.
[1236.74 → 1240.50] Like mindfulness is such a such an important thing.
[1240.88 → 1241.80] We don't realize it.
[1241.88 → 1246.98] You know, we're always either ruminating in the past or being anxious about the future and
[1246.98 → 1248.30] spoiling our past for that.
[1248.60 → 1254.52] So how just being mindfully present in the current moment would really allow you to enjoy
[1254.52 → 1257.20] and soak it in and move forward.
[1257.44 → 1262.62] I think that to me has really brought a lot of peace and calm to myself, within myself.
[1262.98 → 1267.38] And once you have that within you, then you're a lot nicer person to everybody else.
[1267.70 → 1267.76] Right.
[1268.08 → 1273.54] We have a podcast in a network called Brain Science and my co-host, it's on a hiatus right
[1273.54 → 1275.10] now, but we're actually in talks and bringing it back.
[1275.90 → 1276.52] Shout out to Marielle.
[1276.70 → 1279.68] But we're, she's a doctor in clinical psychology.
[1279.90 → 1282.16] And so I'm the layman, basically.
[1282.16 → 1285.44] I'm the non neuroscience graduate, and she is the doctor.
[1286.12 → 1288.84] And one thing we say on that show is be your own scientist.
[1289.50 → 1292.44] And I think what happened to you and maybe part of your shift was self-awareness.
[1292.52 → 1297.04] And so a lot of this question you asked, Jared, and this change of who you are, the first
[1297.04 → 1299.94] step to changing who you are is being self-aware of who you are, right?
[1299.96 → 1304.06] If you don't know who you are, you can't understand why you are who you are and what you're doing
[1304.06 → 1304.56] and stuff like that.
[1304.56 → 1310.00] And so as you become more aware or self-aware of the things that perplex you or, you know,
[1310.08 → 1313.80] upset you about who you are or things you want to change, you can only change what you
[1313.80 → 1317.88] measure, and you can only change that if you're aware that it exists or whatnot.
[1317.98 → 1322.06] So I would say that maybe part of your change was the fact that you became more aware of
[1322.06 → 1326.74] knowledge and more self-aware of what you, of how you mirror image from that knowledge.
[1326.84 → 1331.32] Like who, this is what neuroscience says I am from a brain perspective, a personality perspective.
[1331.32 → 1334.34] This is the knowledge out there and this is who I think I am.
[1334.64 → 1337.18] And through that, you're like, well, this is who I want to be.
[1337.44 → 1340.98] And maybe through your running and self-awareness, you probably have tons of time to think when
[1340.98 → 1341.54] you're running, right?
[1341.62 → 1345.74] So when you're running, you're listening, you're reflecting, you're retrospecting,
[1345.88 → 1346.56] you know, all these things.
[1346.90 → 1347.72] How long do you run generally?
[1348.66 → 1352.02] Anywhere from half an hour to hour and a half every day.
[1352.86 → 1353.72] That's a lot of time to think.
[1353.94 → 1354.08] Yeah.
[1354.20 → 1358.86] Well, and I think you, Adam, you brought up a perfect point because if you can't measure
[1358.86 → 1363.24] it, if you don't know what needs to be fixed, you know, as they say in software, the hardest
[1363.24 → 1364.46] problem is to find the bug.
[1364.70 → 1364.94] Right.
[1365.06 → 1368.38] Once you know the bug, then you can debug it rather quickly and get the solution out.
[1368.48 → 1374.30] So I think I would say two people that probably know you the best and can give you good advice,
[1374.68 → 1377.54] controversial ones, your partner and your boss.
[1377.58 → 1377.88] Yes.
[1377.88 → 1382.88] And be very open and receptive to their feedback.
[1383.60 → 1385.34] Don't go with a judgmental mind.
[1385.60 → 1385.72] Sure.
[1385.84 → 1388.82] Whatever they say, listen in, soak it in.
[1388.82 → 1389.04] Yeah.
[1389.32 → 1390.68] And see what needs to change.
[1391.02 → 1391.34] Truth.
[1391.48 → 1392.88] Because that'll make your work life happy.
[1392.96 → 1393.24] Truth, truth, truth.
[1393.36 → 1393.50] Yeah.
[1393.54 → 1395.74] That'll make your work life happy and home life happy.
[1395.78 → 1396.02] Yeah.
[1396.68 → 1398.06] That's all happy right there.
[1398.06 → 1398.16] Yeah.
[1398.58 → 1403.26] This concept of being your own scientist, though, is this concept of curiosity, right?
[1403.26 → 1407.38] If you're not curious who you are and what you are, then how are you going to reflect
[1407.38 → 1407.80] the world?
[1407.94 → 1411.72] You know, how are you going to be a participant in community, a participant in your workplace,
[1412.28 → 1414.26] in your family, in your friend groups, whatever?
[1414.44 → 1416.80] Like, you'll be maladaptive, as Marielle says.
[1416.86 → 1417.78] She doesn't like to say bad.
[1418.18 → 1419.34] She doesn't like to say negative.
[1419.58 → 1420.74] She likes to say maladaptive.
[1421.66 → 1426.36] You know if you don't have this idea of curiosity and this ability to say, this is,
[1426.56 → 1430.40] you know, to be your own scientist, like, be curious and sort of like self-document who
[1430.40 → 1432.36] you think you are and then reflect on that.
[1432.36 → 1433.62] It's kind of like journaling, things like that.
[1433.62 → 1434.56] You hear this advice a lot.
[1434.80 → 1434.90] Yeah.
[1434.90 → 1439.52] It's almost painfully cliché, like, to say, well, you know, the way to get better is being
[1439.52 → 1441.16] self-aware and to journal and things like that.
[1441.18 → 1443.42] And it's like, I know that advice, but it truly is true.
[1443.56 → 1446.90] Like, if you know who you are, and it's easy to understand who you are and to change if
[1446.90 → 1447.72] you don't like that reflection.
[1448.16 → 1448.44] Absolutely.
[1448.62 → 1449.80] And I mean, look yourself in the mirror.
[1450.02 → 1450.18] Yeah.
[1450.32 → 1455.34] You know, physically you see, I don't like myself physically, but you can't do that mentally
[1455.34 → 1455.82] in a mirror.
[1456.08 → 1457.38] So look in a mental mirror.
[1457.56 → 1457.80] Yeah.
[1457.80 → 1462.34] And I think your spouse and your boss are probably the best mental mirror on how you're
[1462.34 → 1462.70] operating.
[1462.90 → 1463.14] Right.
[1463.30 → 1465.38] Because they have the right perspective, at least.
[1465.66 → 1465.78] Yeah.
[1466.76 → 1468.06] Probably check in with your parents, too.
[1468.10 → 1468.96] They know you pretty well.
[1469.10 → 1469.90] Depend on your age.
[1470.04 → 1470.16] Yeah.
[1470.16 → 1470.54] It depends.
[1470.62 → 1470.72] Yeah.
[1470.82 → 1470.98] Yeah.
[1471.02 → 1471.34] Absolutely.
[1471.92 → 1472.20] Absolutely.
[1472.20 → 1472.42] For sure.
[1472.42 → 1476.48] Well, I think the parents thing is, they will never give you a critical feedback.
[1476.64 → 1480.00] With boss and spouse, they'll give you a critical feedback, which is what you need.
[1480.16 → 1480.26] Right.
[1480.42 → 1480.46] Yeah.
[1480.84 → 1483.02] So you mentioned the tease for later.
[1483.12 → 1485.70] So no one listening to this show right now is here at this conference.
[1485.70 → 1488.92] So they can't go at 1145 and listen to your talk.
[1488.96 → 1493.18] But you mentioned conflict resolution, which I think is key, and adaptability.
[1493.30 → 1495.84] Can you kind of unpack just a little tease to what you're going to talk about?
[1495.84 → 1496.20] Absolutely.
[1496.44 → 1501.04] When you think about conflict resolution, I think one of the biggest things in conflict
[1501.04 → 1506.60] resolution is, how do you separate task conflict versus personality conflict?
[1507.46 → 1511.76] You know, we are all aware of the Peter Luckmann's model of forming, storming, norming, performing.
[1513.20 → 1513.88] I'm not familiar with that.
[1514.20 → 1514.66] Oh, okay.
[1514.80 → 1515.32] I'm not either.
[1515.32 → 1520.44] So there is a Peter Luckmann's model that if you are building a new team, there are four stages.
[1521.02 → 1523.42] Forming, storming, norming, and performing.
[1524.00 → 1525.60] Forming is when the team is coming together.
[1525.88 → 1530.12] Storming is when you're trying to understand what everybody's roles and responsibilities are.
[1530.72 → 1533.64] Norming is when you really start gelling with each other.
[1533.74 → 1535.82] And performing is you're performing at the top-notch.
[1535.94 → 1536.16] Okay.
[1536.36 → 1537.12] Four stages, right?
[1537.94 → 1543.40] So they say in the early stages is a lot of personality conflict because you don't know the people.
[1543.40 → 1543.96] Oh, yeah.
[1543.96 → 1545.56] And less about task conflict.
[1545.80 → 1552.62] But as you go towards more advanced stages, personality conflict goes away and it's all become task conflict.
[1553.20 → 1555.00] And that's what makes your team performing.
[1555.54 → 1557.52] That's what allows you to be more productive.
[1557.80 → 1558.02] Right.
[1558.08 → 1563.38] Because I am able to look through you as a person and say, you know what?
[1563.42 → 1565.30] The problem is in the task, not in the person.
[1565.46 → 1571.40] So I think that's a very important element about differentiating between task conflict and personality conflict.
[1571.40 → 1574.02] That's what I'm going to talk about in that particular one.
[1574.02 → 1579.12] So on the adaptability side, you know, they talk about is the survival of the fittest.
[1579.22 → 1580.16] That's the Darwinian theory.
[1580.86 → 1585.28] But if last three years have they taught anything, is survival of the most adaptable.
[1586.12 → 1587.82] And there have been studies done again.
[1587.82 → 1592.26] And I think there's a talk by one of the doctors on TEDx.
[1592.86 → 1595.56] She talks about studying 10,000 living organisms.
[1596.46 → 1598.70] One thing that keeps them alive.
[1599.40 → 1600.16] And this is not humans.
[1600.30 → 1600.94] Living organisms.
[1601.14 → 1602.26] Plants, trees, etc.
[1602.86 → 1603.32] Adapt.
[1603.38 → 1603.90] Adaptability.
[1604.14 → 1604.30] Yeah.
[1604.60 → 1605.64] That is fundamental.
[1605.80 → 1606.32] Resilience.
[1606.58 → 1607.12] Adaptability.
[1607.28 → 1608.98] They're synonymous in some ways.
[1609.02 → 1609.36] Absolutely.
[1609.76 → 1609.98] Absolutely.
[1609.98 → 1613.94] So I'll talk about that element on why, how adaptability at work.
[1614.48 → 1617.46] Like schedules change, you know, teams change.
[1617.60 → 1617.86] Right.
[1617.86 → 1622.02] We were just talking about that with regard to artists and generative AI.
[1622.32 → 1627.48] And where it's like you can't go and change the fact of the reality that this stuff exists.
[1627.96 → 1629.06] Artists need to adapt.
[1630.32 → 1634.86] And coders, as generative, as code generation becomes better and better and better,
[1634.86 → 1638.92] software developers are going to have to adapt, move up the value chain, right?
[1639.56 → 1640.70] And artists are doing that.
[1640.74 → 1643.12] So like either adapt or you die, right?
[1643.30 → 1643.40] Yeah.
[1643.40 → 1646.58] I mean, there's a book which talks about who moved my cheese.
[1646.66 → 1647.14] Oh, my gosh.
[1647.22 → 1647.40] Yes.
[1647.70 → 1648.98] I'm just about to mention that.
[1649.10 → 1649.38] It is.
[1649.64 → 1652.74] I'm like, he said first, I was going to talk about that book.
[1652.80 → 1654.36] It's like, we've mentioned that book, obviously.
[1654.64 → 1655.68] You have to read it.
[1655.82 → 1656.38] I love it.
[1656.38 → 1658.52] It's what, an hour or two maybe read?
[1658.66 → 1659.18] It's short.
[1659.18 → 1660.22] A 90-page short guide.
[1660.22 → 1668.06] Everyone who deals with change, which is every human being, should read or at least read the summary of that book
[1668.06 → 1670.14] because it's such a good book to understand change.
[1670.24 → 1670.92] You have to adapt.
[1671.12 → 1673.16] And in that book, Spencer Johnson makes a code.
[1673.22 → 1676.28] He says, if you do not adapt, you become extinct.
[1676.46 → 1676.64] Yeah.
[1676.80 → 1677.16] There you go.
[1677.28 → 1677.76] That is exactly what is true.
[1677.86 → 1680.42] I mean, we have seen what happened to BlackBerry, Blockbuster.
[1681.18 → 1681.40] Right.
[1682.78 → 1683.72] Steven Spielberg.
[1683.72 → 1688.62] This guy was rejected by USC Cinematic Arts School.
[1689.66 → 1691.70] And now they have a building in his honour.
[1691.82 → 1692.32] Oh, wow.
[1692.58 → 1693.18] Michael Jordan.
[1693.74 → 1698.26] He was cut from his freshman high team or sophomore high team.
[1698.54 → 1698.70] Yeah.
[1698.80 → 1699.80] We know who Michael Jordan is.
[1699.98 → 1700.24] Right.
[1700.42 → 1704.18] So, I mean, there are, if these people had not adapted, there would be nowhere.
[1704.50 → 1704.80] Yes.
[1704.86 → 1706.98] You can't just sulk and cry.
[1707.08 → 1707.36] Right.
[1707.50 → 1709.46] And, you know, it's okay to sulk and cry.
[1709.46 → 1709.68] Right.
[1709.78 → 1710.96] But then get up and change.
[1711.18 → 1711.92] And change.
[1712.10 → 1712.34] Exactly.
[1712.62 → 1712.70] Yeah.
[1712.70 → 1717.02] So, I think, and the last, the first skill that I talk about is communication.
[1717.54 → 1724.82] And in that, we talk about how it is important to do mindful talking and reflective listening.
[1725.54 → 1730.56] And how it is super important that when you're talking to somebody, there's an intent and there's
[1730.56 → 1731.18] an impact.
[1731.48 → 1732.68] Are those two aligned?
[1733.46 → 1736.92] Because there could be left several factors around you by which the other person may not
[1736.92 → 1737.76] be hearing it well.
[1738.46 → 1739.22] Are you doing it well?
[1739.26 → 1741.00] And then the second part is a reflective listening.
[1741.34 → 1741.58] Right.
[1741.58 → 1747.58] Am I listening to you as opposed to, I mean, as Stephen Covey said, most people listen
[1747.58 → 1750.92] with an intent to reply as opposed to understand the point of view.
[1751.08 → 1751.40] Right.
[1751.50 → 1752.62] They're waiting for their turn to talk.
[1752.78 → 1752.94] Right.
[1753.20 → 1755.80] And they're like, oh, can I finish my sentence?
[1755.80 → 1756.70] I almost cut you off there.
[1757.74 → 1758.42] I'm just kidding.
[1758.50 → 1758.96] I'm just kidding.
[1759.18 → 1759.58] I'm just kidding.
[1759.58 → 1760.48] I had to do it.
[1760.56 → 1760.92] My bad.
[1760.92 → 1761.42] No, no, no.
[1761.42 → 1762.06] Hey, it's all good.
[1762.30 → 1762.66] It is.
[1762.66 → 1763.34] We do that.
[1763.48 → 1765.70] We do that as podcasters often.
[1765.88 → 1766.00] Right.
[1766.08 → 1767.18] Because we do this every day.
[1767.22 → 1767.32] Right.
[1767.32 → 1769.34] So we listen to a lot of people and we have to respond.
[1769.34 → 1774.46] But we also have this pressure to be smart on these microphones, to have a point to say,
[1774.62 → 1776.62] to say it eloquently and to be heard.
[1776.62 → 1781.56] And sometimes you don't listen very well because you're just kind of like, you want to bring
[1781.56 → 1782.84] up the cheese book.
[1783.10 → 1783.46] Exactly.
[1783.70 → 1785.64] Or plausible science or something.
[1785.64 → 1786.74] There's a question lingering in your mind.
[1786.88 → 1787.24] Precisely.
[1788.38 → 1789.32] Imagine the person is talking before.
[1789.32 → 1791.48] And a desire to make the conversation good, though, too.
[1791.52 → 1791.66] Correct.
[1791.66 → 1794.92] I mean, in everyday conversation, you're not on a microphone.
[1795.04 → 1798.16] It's not recorded and played back to thousands and thousands of people all over the world.
[1798.20 → 1798.90] So you don't have that pressure.
[1799.02 → 1801.88] But in our case specifically, we do have that pressure.
[1801.88 → 1806.82] So we do want ourselves to be well-received and light and a good narrative, a good story
[1806.82 → 1807.96] arc to the thing, too.
[1808.00 → 1809.22] We have an agenda of sorts.
[1809.38 → 1809.58] Agreed.
[1809.58 → 1810.18] We have to maintain.
[1810.34 → 1810.70] No, I agree.
[1810.78 → 1811.18] Completely agree.
[1811.28 → 1813.58] I mean, imagine somebody is talking for 45 seconds.
[1814.36 → 1817.72] You listen to the first 15 seconds and then the question is lingering in your mind.
[1817.98 → 1820.58] You have not paid any attention for the next 30 seconds.
[1820.76 → 1820.88] Yeah.
[1821.04 → 1823.56] That's not mindful talking or reflective listening.
[1824.18 → 1826.84] It's hard to hold on to that question but still continue forward.
[1826.98 → 1827.22] Yeah.
[1827.46 → 1828.46] And go with them.
[1828.48 → 1829.46] Well, put a notepad.
[1829.68 → 1829.86] Yeah.
[1829.94 → 1830.68] Write down the question.
[1830.68 → 1835.30] Because oftentimes, you are wanting to jump in with the question because you think you'll
[1835.30 → 1836.00] forget the question.
[1836.16 → 1836.36] Right.
[1836.54 → 1837.22] Have a notepad.
[1837.66 → 1838.42] Get out your phone.
[1838.68 → 1841.12] Put it on a note that I want to ask that question.
[1841.82 → 1843.18] You can always come back to the context.
[1843.62 → 1843.76] Yes.
[1843.90 → 1846.68] Speaking of notes, I do that in my brain when we talk.
[1846.74 → 1850.94] So I have this virtual notepad that I write a question on or write a note on and that one
[1850.94 → 1851.70] is conflict resolution.
[1851.82 → 1855.08] I'm going to go back to this thing that we were talking about there because one thing
[1855.08 → 1858.92] with conflict that's interesting is that, and you mentioned with this, what's the
[1858.92 → 1859.94] what is the?
[1860.08 → 1860.96] Peter Luckmann's model.
[1861.04 → 1861.68] Peter Luckmann's model.
[1861.78 → 1863.46] Forming, storming, norming, and performing.
[1863.64 → 1863.80] Right.
[1863.86 → 1865.90] So as part of that, that initial stage, right?
[1865.90 → 1867.78] I imagine it kind of like a puzzle, right?
[1867.78 → 1871.06] When you put a puzzle piece together into it, it doesn't always perfectly go in.
[1871.10 → 1872.68] You kind of have to like to shift it.
[1872.94 → 1873.08] Yeah.
[1873.16 → 1876.14] And so what happens is you go from disconnection to connection.
[1876.14 → 1876.38] Yeah.
[1876.62 → 1879.52] And conflict usually happens when you're disconnected, right?
[1879.56 → 1880.56] You become disconnected.
[1881.02 → 1882.20] So I want to kind of go back to that point.
[1882.26 → 1882.82] I've been meeting.
[1883.02 → 1883.88] So I just wanted to.
[1883.88 → 1884.22] No, no.
[1884.22 → 1884.42] Fantastic.
[1884.42 → 1885.24] You're holding on to this question.
[1885.24 → 1885.94] I've been holding on to that.
[1885.98 → 1887.92] So I want to use your point to go back to that if we could.
[1888.16 → 1888.38] Thank you.
[1888.44 → 1893.56] And I think I was reading a story about Wilbur Wright brothers on how they created the
[1893.56 → 1894.10] first plane.
[1894.10 → 1900.60] And in that story, I was reading about conflict resolution that these two brothers had only
[1900.60 → 1901.34] task conflict.
[1901.88 → 1905.38] They would fight with each other like hell, but on a task.
[1905.92 → 1908.30] End of the day, they will still sit down together, have a beer.
[1908.46 → 1908.74] Right.
[1908.88 → 1910.02] And that's how they came up with the plane.
[1911.06 → 1911.42] Is that right?
[1911.52 → 1912.04] That's a good story.
[1912.04 → 1916.64] I mean, there are so many stories where conflict resolution is a key.
[1917.54 → 1922.04] And it seems like their ability to do that has to have something to do with disconnecting
[1922.04 → 1923.92] from the task at hand, like their personal identity.
[1924.10 → 1924.34] Right.
[1924.42 → 1924.60] Right.
[1924.60 → 1928.98] Because you can actually not like my idea or the way my process and say, that's a bad
[1928.98 → 1929.34] process.
[1929.42 → 1930.10] Here's a better one.
[1930.38 → 1934.06] And I can take that, and I can adapt and change and agree with you.
[1934.10 → 1936.46] Or I can say, well, that's my idea or that's my process.
[1936.54 → 1938.00] And so you're attacking my process.
[1938.10 → 1939.10] Therefore, you're attacking me.
[1939.22 → 1939.32] Right.
[1939.58 → 1942.90] But what happened, though, was at the end of the day, they went back together and had
[1942.90 → 1943.30] that beer.
[1943.34 → 1943.48] Right.
[1943.52 → 1943.82] The connection.
[1943.96 → 1944.68] They remained connected.
[1944.74 → 1945.28] Well, they were brothers.
[1945.60 → 1945.70] Right.
[1945.76 → 1947.66] So when you disconnect, you don't have communication.
[1947.86 → 1950.60] So you walk away, or they walk away assuming.
[1951.14 → 1951.36] Right.
[1951.38 → 1952.06] Well, he's stewing.
[1952.14 → 1952.66] They're stewing.
[1952.70 → 1953.22] I'm stewing.
[1953.28 → 1953.56] Whatever.
[1953.76 → 1953.92] Right.
[1954.10 → 1955.80] So much assumption, and it's not true.
[1955.90 → 1959.90] And when you come back together, and you say, well, let's continue this day or this beer,
[1959.98 → 1961.04] like you remain connected.
[1961.16 → 1963.52] You remain united in your efforts of whatever it might be.
[1963.60 → 1967.16] It's the act of connection that brings us back together and resolves conflict.
[1967.30 → 1967.44] It does.
[1967.56 → 1967.74] It does.
[1967.80 → 1972.04] And I think it's a lot harder in this Zoom world.
[1972.22 → 1972.54] Yeah.
[1972.60 → 1975.20] Where as long as the discussion is over, you just shut the laptop down.
[1975.26 → 1976.40] It's like, I'm just walking out of here.
[1976.52 → 1976.74] Right.
[1976.98 → 1977.24] No.
[1977.46 → 1978.32] Or text communication.
[1978.42 → 1978.94] Yeah, exactly.
[1978.94 → 1986.74] Because I remember, I think KD, who used to be a warrior, who joined San Francisco Golden
[1986.74 → 1987.56] Gate Warriors team.
[1987.86 → 1988.44] Kevin Durant.
[1988.58 → 1989.02] Kevin Durant.
[1989.06 → 1989.20] Yeah.
[1989.20 → 1995.06] So he sent a message to his teammate when he was leaving OKC Thunder over a text message.
[1996.46 → 1997.96] He said, hey, I'm leaving the team.
[1998.58 → 1998.88] Ouch.
[1999.04 → 2002.42] Dude, you were the star player of OKC Thunder for so many years.
[2002.42 → 2003.48] You can't do that kind of stuff.
[2003.84 → 2004.28] Disconnected.
[2004.34 → 2004.50] Yeah.
[2004.50 → 2006.96] And then face-to-face.
[2007.12 → 2007.60] Pissed off.
[2007.68 → 2008.04] Conflict.
[2008.04 → 2008.60] Of course.
[2008.86 → 2009.32] Of course.
[2009.46 → 2009.70] Yes.
[2010.06 → 2016.32] So I think if we realize these are day-to-day situations, day-to-day things that we can always
[2016.32 → 2016.84] do better.
[2017.56 → 2022.32] Well, it seems like one of the skills of communication is picking the right medium for communication.
[2022.58 → 2022.64] Right?
[2022.72 → 2023.16] True.
[2023.40 → 2026.12] His message there would have probably been much better received personally.
[2026.34 → 2026.62] Yeah.
[2026.92 → 2027.62] Because it's important.
[2027.88 → 2028.14] Right?
[2028.14 → 2034.38] And he picked the wrong medium for communication and that that delivered his, I don't know,
[2034.44 → 2035.16] lack of care.
[2035.46 → 2036.96] It itself was a message.
[2037.10 → 2038.04] The fact that it was a text message.
[2038.62 → 2042.62] And so that's such a struggle sometimes is like knowing when do I put the texting down
[2042.62 → 2043.38] and pick up the phone?
[2043.56 → 2046.18] Or when do I hop off the phone and drive over to their house?
[2046.32 → 2047.54] The Wright brothers had two things going.
[2047.64 → 2049.70] They were brothers, which means they had a connection.
[2049.78 → 2051.78] But also they were sitting right with each other.
[2052.08 → 2052.40] Right.
[2052.68 → 2054.66] Difficult for us in the digital age, like you said.
[2054.66 → 2059.78] Well, I think one thing I would recommend is put yourself in the recipient's shoe.
[2060.06 → 2060.20] Yeah.
[2060.62 → 2060.98] Empathy.
[2061.28 → 2062.28] Would you like, exactly.
[2062.48 → 2062.74] Yes.
[2062.82 → 2067.48] Would you like to be in that position that somebody texted you?
[2067.56 → 2067.58] Text you.
[2067.58 → 2067.90] I'm leaving.
[2068.08 → 2072.78] My five-year-old friend where we are competing in the court every day together, practicing
[2072.78 → 2074.76] every day together and texting me.
[2074.80 → 2075.50] How would you feel it?
[2075.60 → 2075.88] Right.
[2076.10 → 2076.26] Right.
[2076.28 → 2078.70] So have that empathy and that goes a long way.
[2078.88 → 2079.18] Yes.
[2079.40 → 2079.72] Yes.
[2079.72 → 2085.56] Well, we can't invite everybody to your talk, but you do write on a blog for Intel.
[2085.72 → 2086.88] So it's open.intel.
[2087.02 → 2087.40] Do you blog?
[2087.48 → 2088.38] Is that where the blog is at?
[2088.48 → 2088.66] That's right.
[2088.68 → 2089.48] I didn't pay attention to the link.
[2089.66 → 2090.54] I saw the page.
[2090.60 → 2090.70] Yeah.
[2090.82 → 2092.20] I didn't pay attention to the URL I was going to.
[2092.32 → 2096.02] So open. Intel has your post and other posts from your team there.
[2096.02 → 2096.16] Right.
[2096.64 → 2099.92] I'm sure this talk you're giving will be on YouTube as part of all things open.
[2100.04 → 2100.18] Yeah.
[2100.42 → 2104.88] Where else can people catch up with you or pay attention to your journey at Intel?
[2105.06 → 2105.22] Yeah.
[2105.28 → 2106.88] My Twitter handle is the best.
[2107.30 → 2108.28] Arun Gupta, one word.
[2108.28 → 2109.92] You know, that's where I tweet prolifically.
[2110.26 → 2110.76] I try to.
[2112.16 → 2113.16] So catch me there.
[2113.58 → 2114.54] My DMs are open.
[2114.66 → 2116.06] I think Brian was talking about it.
[2116.60 → 2118.72] You know, I'm a servant leader here.
[2118.86 → 2120.58] So reach out to me.
[2120.68 → 2123.84] I'm happy to talk about anything, literally anything around the world.
[2124.30 → 2127.64] Well, I can attest to your DMs being open because I just DMed you earlier this morning
[2127.64 → 2129.00] and here you are.
[2129.10 → 2129.24] Right.
[2129.24 → 2129.48] You are.
[2129.56 → 2129.98] It works.
[2130.16 → 2130.76] That's how it works.
[2130.98 → 2132.88] Literally within an hour, we made this happen.
[2133.10 → 2133.60] How cool is that?
[2133.76 → 2135.96] That's where the opportunities are sitting.
[2136.38 → 2136.52] Yeah.
[2136.92 → 2138.04] Well, thanks so much for joining us.
[2138.04 → 2138.76] Thank you so much.
[2138.78 → 2139.14] It was awesome.
[2139.32 → 2140.08] Thank you for having me.
[2140.08 → 2164.78] This episode is brought to you by our friends at Square.
[2165.00 → 2166.70] Develop on the platform that sellers trust.
[2166.70 → 2175.36] Here's what you can do with Square. You can bridge more experiences. You can build online, mobile, and in-person commerce experiences that connect more customers and sellers.
[2175.74 → 2181.80] You can build custom booking solutions. You can create and track orders. You can accept payments. Furthermore, you can manage and curate inventory.
[2182.34 → 2187.10] You can organize customers. You can manage employees. You can extend Square gift cards to your app.
[2187.10 → 2198.30] You can use Afterpay, and all this is powered by the world-class Square APIs and SDKs that enable you to build full-featured business apps for yourself or millions of Square sellers.
[2198.80 → 2207.18] So much is available as a Square Solutions partner. Learn more and get started at changelog.com slash Square. Again, changelog.com slash Square.
[2217.10 → 2230.72] So, Chad, it's been a while, man.
[2230.84 → 2231.28] Yeah, it's been a few years.
[2231.28 → 2232.12] I want to say I missed you.
[2232.26 → 2233.14] It's been a few years.
[2233.26 → 2234.82] You're one of my favourite people out here, you know.
[2235.02 → 2235.42] For real.
[2235.80 → 2236.36] Come on, Stag.
[2236.54 → 2237.22] Yeah, for real.
[2237.34 → 2237.88] Come on, now.
[2238.10 → 2238.98] You're making me blush.
[2239.06 → 2239.92] This is a moment right here.
[2239.92 → 2240.84] You're making me blush. You see that?
[2241.02 → 2242.00] This is a reunion.
[2242.10 → 2243.80] This is why it's a podcast and not a video.
[2243.80 → 2245.10] So you can't see me blushing.
[2245.44 → 2246.26] This is a reunion.
[2246.26 → 2247.44] I think it's special, too.
[2247.48 → 2248.70] I've been watching what you've been doing this century.
[2248.80 → 2248.92] Found it.
[2249.40 → 2250.68] I'm happy that you're there.
[2250.88 → 2251.38] Yeah, thank you.
[2251.38 → 2255.38] I'm happy for all the hard work you put out there, regardless of the road it took, you know, and how it ended.
[2255.74 → 2255.98] Yeah.
[2256.20 → 2257.18] You were always a hard worker.
[2257.26 → 2260.94] You always had a good heart in the mix, and we need more people like you out there doing the work.
[2261.12 → 2261.34] For real.
[2261.34 → 2261.54] Appreciate it.
[2262.00 → 2262.82] And I'm happy you're here.
[2263.14 → 2269.40] Well, like I was just saying before we jumped on the mics, you know, it was probably, it was 2017.
[2269.82 → 2270.58] I was here two years.
[2270.66 → 2273.26] I forget if it was like 16, 17 or 17, 18.
[2273.26 → 2277.84] But yeah, I remember last time I saw you guys here, you had just launched a new brand.
[2278.16 → 2278.26] Yeah.
[2278.26 → 2282.84] You know, because I don't want to say that you guys were scrappy, but you were scrappy at the beginning.
[2282.92 → 2283.10] Yeah.
[2283.18 → 2283.66] You know what I mean?
[2283.82 → 2285.72] And then you came out with the changelog brand.
[2285.84 → 2287.70] You had like, you really invested in it.
[2287.74 → 2288.18] You know what I mean?
[2288.44 → 2288.60] Yeah.
[2288.60 → 2293.18] And took it to the next level and was like, all right, these guys are like, they mean business.
[2293.36 → 2293.44] That's fair.
[2293.44 → 2293.60] You know?
[2293.86 → 2294.46] They're going to do it.
[2294.78 → 2294.90] Yeah.
[2294.90 → 2295.76] But that was like five years ago.
[2295.80 → 2296.12] You know what I mean?
[2296.16 → 2296.70] That was like.
[2297.06 → 2297.30] Yeah.
[2297.34 → 2297.78] Maybe more.
[2297.92 → 2298.12] Yeah.
[2298.30 → 2299.46] 2016 was the new brand.
[2299.78 → 2299.96] Yeah.
[2300.00 → 2300.52] Is that what it was?
[2300.76 → 2301.00] Yeah.
[2301.00 → 2301.78] So that was probably it.
[2301.98 → 2302.78] 2016, we're here.
[2302.90 → 2304.36] It was October.
[2304.76 → 2304.96] Yeah.
[2305.04 → 2307.10] We literally were just launching it.
[2307.26 → 2307.44] Yeah.
[2307.58 → 2310.26] I think the website was maybe live a day, maybe a week.
[2310.26 → 2310.30] Yeah.
[2310.30 → 2311.24] It was not long.
[2311.88 → 2313.02] The website was the last thing.
[2313.02 → 2315.62] It was a thin banner only, not this big banner behind us.
[2316.04 → 2316.20] Yeah.
[2316.20 → 2316.44] Yeah.
[2316.46 → 2317.22] We had a thin one.
[2317.42 → 2318.92] And it just said like, hacker to the heart.
[2319.30 → 2319.88] Hacker to the heart.
[2320.06 → 2320.28] Yeah.
[2320.80 → 2321.30] Because we are.
[2321.46 → 2321.76] I love it.
[2322.16 → 2323.24] Hacker to the heart.
[2323.58 → 2323.82] For sure.
[2323.92 → 2324.28] Well, now.
[2324.52 → 2326.02] So how many podcasts do you guys have now?
[2326.42 → 2327.28] Can you even keep track?
[2327.34 → 2327.88] You just like.
[2328.94 → 2329.18] Yeah.
[2329.18 → 2330.92] You lose them underneath the couch cushions at this point.
[2330.92 → 2330.94] Yeah.
[2330.94 → 2331.26] Exactly.
[2331.34 → 2331.52] Right.
[2331.82 → 2333.30] We do five weekly shows.
[2333.30 → 2333.78] Oh, yeah.
[2333.78 → 2334.08] Yeah.
[2334.20 → 2334.58] Five weekly.
[2335.06 → 2335.42] Wow.
[2335.82 → 2336.80] So, you know, we got to.
[2337.44 → 2338.50] We got to one a day.
[2338.84 → 2339.08] Okay.
[2339.22 → 2340.56] But across different podcasts.
[2340.70 → 2342.78] You know, not like the changelog five times a week.
[2342.78 → 2345.28] It's like little verticals, you know?
[2345.48 → 2345.68] Yeah.
[2345.80 → 2347.10] That was our move.
[2347.82 → 2350.02] And it's worked out pretty well because we have a lot more voices.
[2350.38 → 2350.62] Yeah.
[2350.80 → 2353.32] A lot more diversity in the topics, everything.
[2353.70 → 2353.82] Well.
[2353.82 → 2355.38] If it was just us two doing five shows a week.
[2355.38 → 2356.64] I have more burden to share, too.
[2356.74 → 2359.10] I mean, if we try to do five shows a week and do all the work.
[2359.46 → 2359.66] Yeah.
[2359.76 → 2360.40] It would never work.
[2360.48 → 2360.78] Of course.
[2360.98 → 2361.24] Yeah.
[2361.24 → 2362.72] No, you got to scale it up.
[2363.40 → 2367.60] Well, because like open source is a community of communities.
[2368.00 → 2368.12] Yeah.
[2368.12 → 2368.30] Right.
[2368.56 → 2372.38] It's an interesting thing to think about the open source community and what it means.
[2372.38 → 2372.64] You know?
[2372.64 → 2372.78] Yeah.
[2372.78 → 2374.46] It's like people have different takes on it.
[2375.36 → 2376.56] But I like what you guys are doing.
[2376.64 → 2380.74] You're like, you've got the umbrella, but then you've got like the different, like you
[2380.74 → 2381.70] said, the voices in it.
[2381.82 → 2382.14] Exactly.
[2382.74 → 2383.04] Bring it all together.
[2383.04 → 2384.06] I think it works pretty well.
[2384.20 → 2389.68] Obviously, there's sub communities that we don't serve because you have to add another
[2389.68 → 2390.62] podcast to do that.
[2390.68 → 2392.22] You got to find the right person to partner with.
[2392.34 → 2394.80] And there are lots of things to do, you know, to get that done.
[2394.80 → 2398.00] But at the same time, you know, we're doing what we can.
[2398.26 → 2398.58] Right.
[2398.84 → 2399.32] I love it.
[2399.32 → 2400.68] We're reaching the communities we reach.
[2400.76 → 2402.32] And then, like you said, we have kind of the umbrella.
[2402.58 → 2402.72] Yeah.
[2402.76 → 2404.40] The changelog is always going to be for everybody.
[2404.54 → 2404.74] Yeah.
[2405.22 → 2405.56] And so.
[2405.96 → 2407.08] How's the surrounding community?
[2407.08 → 2409.74] Because I remember you were launching like the Slack and the other stuff like that and
[2409.74 → 2411.12] the website with it.
[2411.46 → 2412.40] Slack's still great.
[2412.50 → 2413.66] I mean, it's active every day.
[2413.72 → 2414.52] There's a lot of people every day.
[2414.60 → 2414.72] Yeah.
[2414.80 → 2415.66] You didn't jump to Discord?
[2415.88 → 2416.48] You're still on Slack?
[2416.56 → 2417.04] We did not.
[2417.18 → 2420.18] We're on that fence because it's a struggle.
[2420.20 → 2420.90] You didn't go back to IRC?
[2421.06 → 2421.50] We did not.
[2421.50 → 2423.88] We've had a few people tell us to go to IRC, of course.
[2424.80 → 2428.54] It's a struggle because it's hard to switch, you know.
[2428.70 → 2428.88] So.
[2429.24 → 2429.60] Oh, yeah.
[2429.72 → 2431.32] Slack doesn't keep us with features necessarily.
[2431.46 → 2433.14] They keep us with paying to move.
[2433.22 → 2433.54] Yeah.
[2433.70 → 2433.98] Right.
[2434.16 → 2434.40] Of course.
[2434.44 → 2436.64] And like you're going to lose people in that movement.
[2437.12 → 2437.48] Yeah.
[2437.68 → 2438.10] You know.
[2438.34 → 2438.70] And.
[2439.38 → 2439.60] Yeah.
[2440.56 → 2442.28] Slack is well known.
[2442.30 → 2442.56] Yeah.
[2442.66 → 2443.54] And a lot of people use it.
[2443.58 → 2446.36] So it's like, well, you know, I know you all have a Slack.
[2446.44 → 2446.62] Yeah.
[2446.76 → 2447.56] We have a Slack.
[2447.68 → 2449.28] Other brands we work with have a Slack.
[2449.28 → 2449.48] Absolutely.
[2449.48 → 2451.30] It's like, you know, how do you choose?
[2451.30 → 2455.34] Where to put your community real-time messaging basically, you know.
[2455.88 → 2457.56] We want to be more open source aligned.
[2457.70 → 2459.82] We want to be more community focused aligned.
[2459.96 → 2462.80] But it's hard to make that switch when.
[2462.80 → 2463.46] That's true, right?
[2463.48 → 2464.42] We're so embedded.
[2464.54 → 2466.26] We have the Zulip or the Mattermost or.
[2466.46 → 2468.04] It's almost worth just paying for it really.
[2468.34 → 2468.44] Yeah.
[2469.08 → 2475.32] We would entertain a community partner who would be like, we're sponsoring the community Slack or the community.
[2475.64 → 2476.54] Whatever that might be.
[2476.64 → 2476.78] Okay.
[2476.78 → 2477.52] Find a way to do that.
[2478.28 → 2479.62] And that way it's like X per month.
[2479.82 → 2481.14] And then maybe we profit a little bit.
[2481.24 → 2484.40] But maybe just kind of surplus more or less to cover like higher months.
[2484.46 → 2486.10] Because Slack will go up or down based upon usage.
[2486.10 → 2486.76] We pay you guys, right?
[2486.82 → 2487.60] Doesn't Sentry sponsor?
[2487.84 → 2488.04] Yeah.
[2488.12 → 2488.96] Sentry sponsors, right?
[2488.96 → 2489.24] Yeah.
[2489.40 → 2489.90] I hope so.
[2490.14 → 2490.30] Yeah.
[2490.30 → 2490.42] Good.
[2490.56 → 2490.84] For sure.
[2491.34 → 2492.28] No, we love you guys.
[2492.86 → 2493.68] We love you too.
[2494.36 → 2495.44] Are you using Sentry?
[2495.56 → 2495.74] Yeah.
[2496.06 → 2497.64] I use it a couple of times a week.
[2497.92 → 2498.16] Okay.
[2498.92 → 2499.72] Elixir, Phoenix.
[2500.02 → 2500.84] Every Monday for sure.
[2500.98 → 2501.40] Every Monday.
[2501.48 → 2502.14] I think I saw it.
[2502.16 → 2503.22] You're getting into the Phoenix stuff.
[2503.38 → 2503.60] Yeah.
[2504.32 → 2505.02] It's nice.
[2505.46 → 2507.32] I've been on it ever since 2016.
[2508.04 → 2508.22] Really?
[2508.22 → 2509.98] I don't really have any complaints.
[2511.04 → 2512.74] I'm slow to adopt the new stuff.
[2512.84 → 2518.20] They got a lot of new stuff in the Phoenix world with Live View and a lot of the new component stuff.
[2518.50 → 2518.54] Okay.
[2519.42 → 2523.14] But I'm just, we deployed it in 2016 and just keep working on it.
[2523.22 → 2525.08] We're going to do a redesign here soon and probably rethink some of our stuff.
[2525.10 → 2525.76] So that was pretty early.
[2525.76 → 2526.20] Some of our stuff.
[2526.30 → 2526.52] Yeah.
[2526.70 → 2526.92] Yeah.
[2526.92 → 2533.26] We were the only open source Phoenix app for a while that you could actually look at and see how to build one.
[2533.70 → 2533.86] Okay.
[2533.86 → 2535.20] Kind of soup to nuts that was in production.
[2535.56 → 2535.72] Yeah.
[2535.76 → 2536.72] Now there's a handful of them.
[2536.86 → 2537.72] Plausible is a good one.
[2538.28 → 2538.60] Plausible.
[2538.88 → 2539.46] Plausible, yeah.
[2539.56 → 2540.28] I like Plausible.
[2540.48 → 2540.74] Yeah.
[2540.86 → 2541.36] They're awesome.
[2541.98 → 2543.30] So what's new with you?
[2544.12 → 2544.78] Sentry, man.
[2545.30 → 2545.70] Sentry Day and Night.
[2545.70 → 2546.06] Sentry Day and Night.
[2546.06 → 2546.74] How long has it been?
[2546.96 → 2547.40] You've been there?
[2547.56 → 2548.26] Nine months?
[2548.26 → 2548.92] I've been there for two years.
[2549.24 → 2549.84] Two years.
[2549.86 → 2550.22] Believe it.
[2550.56 → 2551.00] Believe it.
[2551.16 → 2552.38] You've been hiding that.
[2552.38 → 2552.62] Okay.
[2552.76 → 2554.90] So maybe like nine months ago you came out of the woodwork.
[2555.22 → 2555.48] So here's what happened.
[2555.76 → 2556.40] Here's the story.
[2556.46 → 2556.90] Here's the story.
[2557.40 → 2561.70] So after Get Tip Gateway, that wound down at the end of 2017.
[2562.08 → 2562.64] I thought it was Get It.
[2563.66 → 2564.96] Well, that was a huge controversy.
[2565.20 → 2566.38] That's why I didn't go anywhere, Adam.
[2566.38 → 2566.62] Okay.
[2566.76 → 2566.96] Okay.
[2566.96 → 2567.94] We can figure out how to pronounce this.
[2567.94 → 2568.70] I digress.
[2568.96 → 2569.20] Okay.
[2569.26 → 2569.54] Continue.
[2569.86 → 2570.34] Get Tip.
[2570.80 → 2571.08] Get It.
[2572.34 → 2572.74] Gateway.
[2572.84 → 2572.98] Yeah.
[2572.98 → 2578.14] So wound that down at the end of 2017 and then had a little bit of rebuilding year in 2018.
[2579.00 → 2584.38] And then I went to work as an engineering manager at a security company called Proof point for a couple of years.
[2585.02 → 2585.54] 2020.
[2585.84 → 2586.36] 2020.
[2586.82 → 2589.52] November 2020 is when I started at Sentry.
[2589.94 → 2592.52] And I came in as an engineer on the open source team.
[2592.82 → 2592.98] Okay.
[2593.32 → 2597.78] Because Sentry, as you guys know, but somebody ends up listening to this.
[2598.02 → 2602.02] Sentry started life as an open source side project in 2008.
[2602.48 → 2603.14] Way back.
[2603.38 → 2603.54] All right.
[2603.54 → 2603.68] Yeah.
[2603.68 → 2611.96] So Kramer, 70-line Django plug-in, you know, and it was just a community open source side project for years.
[2612.84 → 2614.82] Didn't start commercializing it until 2012.
[2615.34 → 2617.44] That happened on Heroku.
[2617.44 → 2621.32] I don't want to say RIP Heroku, but Heroku.
[2622.36 → 2625.84] And, you know, $5 a month plug-in on Heroku.
[2626.02 → 2627.04] That's when I started using it.
[2627.38 → 2627.58] Okay.
[2628.16 → 2629.90] And then what?
[2630.36 → 2631.06] Let me fast-forward.
[2632.10 → 2633.32] 2012 commercialized.
[2633.38 → 2634.70] 2015 raised funds.
[2634.84 → 2636.00] 2016 came out.
[2636.06 → 2637.10] Hey, we're a startup now.
[2637.92 → 2639.52] And so now we're at 300 people, right?
[2639.62 → 2640.16] Fast forward.
[2640.72 → 2641.48] I joined.
[2641.58 → 2642.66] We were at like 130.
[2643.18 → 2648.92] And I joined as an engineer on the open source team helping do release management around Sentry, so people could still run it themselves.
[2649.58 → 2650.94] And then that evolved.
[2651.30 → 2652.84] So I was there for a year as an engineer.
[2653.44 → 2655.24] And then stuff kind of shifted.
[2656.28 → 2658.02] The fellow I was working with, he moved on.
[2658.12 → 2659.38] My boss changed what he was doing.
[2659.54 → 2661.20] And that's when I started the OSLO at Sentry.
[2661.78 → 2665.44] So I was there for years as an engineer and then said, hey, let's start a true OSLO.
[2665.74 → 2667.50] And they said, all right, why don't you run it?
[2667.50 → 2670.24] So now I'm head of open source for a year.
[2670.40 → 2671.08] So it's been a year, right?
[2671.32 → 2671.40] Yeah.
[2671.50 → 2671.68] Yeah.
[2671.68 → 2672.70] Today's November 1st, right?
[2673.02 → 2676.46] It feels like nine months in my brain, but I think 12 months is probably more accurate.
[2676.60 → 2679.76] I've like seen you like be out there more.
[2680.14 → 2681.98] Well, and the thing that kind of put me out there was the funding stuff, right?
[2682.02 → 2682.82] I think that's what we're getting to.
[2682.96 → 2683.84] It's like, yeah.
[2683.90 → 2692.96] So a year ago, yeah, published this thing about Sentry's funding of open source software, which had always been there, but was kind of disorganized.
[2692.96 → 2698.74] And so a year ago is when we really got organized and put together a right proper program around funding open source.
[2698.94 → 2699.86] So that was a year ago.
[2699.96 → 2706.06] And then last year, excuse me, last week, we just announced the second go around of that.
[2706.38 → 2710.60] You know, so Sentry's committed, and we're doing it again.
[2711.10 → 2712.92] Last year we did 155K.
[2713.14 → 2714.72] This year we did 260K.
[2714.98 → 2716.86] We're kind of tracking our growth as a company.
[2717.24 → 2718.70] So yeah, man, having fun.
[2718.98 → 2719.34] That's cool.
[2719.50 → 2719.72] It's great.
[2719.72 → 2722.78] So funding's a big part of it.
[2723.20 → 2725.86] But Sentry, you know, Sentry, our whole product is open.
[2727.36 → 2736.80] So a lot of what I'm working on now is helping our engineering culture scale to still have those conversations on GitHub, still have those discussions.
[2737.44 → 2738.80] You know, because we got like 100 plus engineers.
[2738.94 → 2746.06] It's really about helping Sentry engage with our user base, with the open source community, with the developer community on those open source channels.
[2746.56 → 2747.34] Primarily Git Tip.
[2747.54 → 2747.92] Excuse me.
[2747.98 → 2748.28] Listen to me.
[2748.32 → 2748.62] Git Tip.
[2748.62 → 2750.22] Primarily GitHub.
[2750.90 → 2751.46] You know what I'm saying.
[2751.72 → 2753.34] Well, you know, when you say Git, you think, tip.
[2753.46 → 2754.00] You know what I'm saying?
[2754.22 → 2754.56] That's the first thing.
[2754.66 → 2755.90] I don't blame you.
[2755.98 → 2756.46] I mean, Git Tip.
[2756.46 → 2756.68] No.
[2756.98 → 2761.88] But shout out to Charlie Shangaan, who is still running Liberapay.
[2761.98 → 2762.72] Do you guys remember this?
[2763.38 → 2764.50] Forked Gateway.
[2764.98 → 2771.74] When Gateway went down, he forked it, like the business and the code, because it was an open company, right?
[2771.78 → 2774.08] So he is like forked it and is still running with it.
[2774.22 → 2774.58] Liberapay.
[2774.58 → 2774.82] Wow.
[2775.14 → 2775.90] So it's still out there.
[2775.90 → 2778.22] You can still fund some free software folks on Liberapay.
[2778.22 → 2778.62] That's cool.
[2779.28 → 2780.22] Keeping the dream alive.
[2780.62 → 2781.02] Liberapay.
[2781.02 → 2781.84] I didn't know that.
[2782.18 → 2787.38] When you talk about the Sentry stuff, you talk about it from a numbers' perspective so far.
[2787.78 → 2787.96] Yeah.
[2787.96 → 2790.16] How do you talk about it from an impact level?
[2790.38 → 2796.92] Like how do you, I know you talk about community and engagement, but like how do you get specific with like the impact of dollars?
[2796.92 → 2798.34] The first side of dollars in open source.
[2798.34 → 2801.30] I know that's been a big issue for you your whole career.
[2801.44 → 2802.84] So like how do you quantify it there?
[2803.14 → 2803.40] Yeah.
[2803.56 → 2807.54] So I think with Sentry specifically, you know, we're trying to do breadth and depth.
[2807.80 → 2813.56] We're trying to give some folks a really significant amount of money, $10,000, $20,000, right?
[2813.64 → 2814.52] $5,000, $20,000.
[2815.16 → 2818.38] And then we're also trying to go, to go broad, let's say.
[2818.96 → 2822.10] Like we pull our employees and say, hey, what are the projects you like?
[2822.24 → 2824.12] We try and give at least a little something to everybody.
[2824.22 → 2824.74] You know what I mean?
[2825.34 → 2827.16] To try and grow it from both sides.
[2828.70 → 2832.10] But really when we look at, like a lot of people say impact in funding.
[2833.22 → 2836.16] And there's this idea in open source funding that it's like, well.
[2836.74 → 2837.24] Who cares?
[2837.46 → 2839.46] No, what I want to say is like the strings attached, right?
[2839.46 → 2842.00] It's like, so I'm going to give this money, and then what are you going to do with it?
[2842.08 → 2844.50] You know, I'm going to follow up and like, well, did you do more pull requests?
[2844.64 → 2845.36] Like what was the impact?
[2845.54 → 2845.72] Yeah.
[2845.86 → 2849.80] And the way we think about it, the way I think about it is like, look, I already got value
[2849.80 → 2850.22] from you.
[2850.24 → 2850.96] Here's a gift right back.
[2851.06 → 2852.48] Well, yeah, because you gave me the gift.
[2852.48 → 2856.62] Like we spent this past year building on, like I was talking to Josh, like came up to
[2856.62 → 2858.24] me from TypeScript ES Lint, right?
[2858.26 → 2862.10] It's like, we've been getting value out of TypeScript ES Lint all year, right?
[2862.12 → 2864.50] And this is giving back for that value that we've received.
[2864.84 → 2868.04] So, you know, he asked me, he's like, what can we do to, you know, to thank you or whatever?
[2868.04 → 2869.48] It's like, just keep doing what you're doing.
[2869.66 → 2872.52] You know, it's like no strings attached, like keep doing it.
[2872.52 → 2875.90] Um, you know, and if we stop using your stuff, then we'll stop paying you, right?
[2875.90 → 2882.30] It's like, um, I appreciate that perspective because it's very much more on the just appreciation
[2882.30 → 2887.28] side than it is on any sort of quid pro quo or any weirdness that goes on.
[2887.30 → 2888.52] It's like, no, this is for you.
[2888.80 → 2889.68] I already got my value.
[2889.68 → 2890.74] Because it can get weird, right?
[2890.74 → 2891.10] It can.
[2891.18 → 2893.92] Like if you bring money in and some folks don't want the money and that's fine.
[2893.92 → 2894.16] Right.
[2894.36 → 2897.06] You know, go back to this idea of open source community and the different ways to slice
[2897.06 → 2897.28] it.
[2897.76 → 2904.22] Like I do think of the open source community having a commercial aspect and having a
[2904.22 → 2904.96] community aspect.
[2905.14 → 2905.36] Right.
[2905.58 → 2907.50] And a community supported aspect, right?
[2907.52 → 2909.34] So like some folks don't want any money.
[2909.38 → 2910.14] That's fine, right?
[2910.54 → 2913.86] Some folks like Sentry, like we think of ourselves as building open source software.
[2914.02 → 2915.06] We're doing it commercially.
[2915.32 → 2915.50] Right.
[2916.02 → 2920.88] And, but then there's this community supported, um, open source, you know, part of the open
[2920.88 → 2921.44] source community.
[2921.58 → 2924.58] So I think of it as one community with these different aspects to it.
[2924.58 → 2927.16] And Sentry, like we see ourselves as part of the community.
[2927.30 → 2930.90] And so we're trying to take care of that community supported, you know, that part is depending
[2930.90 → 2931.30] on that.
[2931.64 → 2932.50] Do right by the community.
[2932.68 → 2932.70] No.
[2932.74 → 2934.08] How do you determine like numbers?
[2934.20 → 2938.16] How do you, since you run the Oslo, Oslo, not Oslo.
[2938.66 → 2938.86] Oslo.
[2939.22 → 2940.62] I don't want to say Oslo.
[2941.14 → 2941.54] Osprey.
[2942.46 → 2942.78] Oslo.
[2942.94 → 2943.14] Word.
[2943.14 → 2944.60] So you run Oslo, right?
[2945.34 → 2949.24] Um, how do you interface with the business side of Sentry?
[2949.58 → 2954.02] Now, of course, developers started the organization, so it's a little easier, but not all Spot
[2954.02 → 2958.78] will have the luxury you have in a dev oriented organization, right?
[2959.24 → 2961.68] But how do you say, give us this much money to put back?
[2961.74 → 2962.90] How do you quantify dollars?
[2963.06 → 2963.26] Sure.
[2963.36 → 2965.88] Is there some sort of like 10%?
[2966.04 → 2966.66] Is it a tie?
[2966.70 → 2967.70] How do you think about it?
[2967.70 → 2967.88] Yeah.
[2968.52 → 2974.72] So, again, I'm super lucky because, you know, David Kramer and Chris Jennings, the founders
[2974.72 → 2978.44] of the company, are, you know, all in on open source, right?
[2978.54 → 2980.66] So they're setting that tone from the top.
[2981.94 → 2985.20] And Sentry, again, open source is a core part of our company identity.
[2985.64 → 2987.04] It's where we locate ourselves.
[2987.14 → 2988.44] We're a commercial open source company.
[2988.44 → 2990.02] We think of ourselves as an open source company.
[2990.26 → 2990.42] Okay.
[2991.18 → 2995.80] That said, I actually did some napkin math towards the end of Gateway.
[2995.92 → 2996.26] Get it.
[2996.60 → 2996.96] Get it.
[2998.46 → 3003.04] Where I tried to think about it like from a first principle approach of what is fair,
[3003.24 → 3003.42] right?
[3003.50 → 3006.98] Like there's all this talk about fairness and, you know, companies making all this money
[3006.98 → 3008.28] off the backs of open source labour.
[3008.42 → 3009.84] It's like, all right, so time out.
[3009.92 → 3011.16] Like, let's have the conversation.
[3011.54 → 3012.30] What is fair?
[3012.66 → 3016.74] What, like, what would be an amount that you saw a company giving, and you as part of the
[3016.74 → 3019.98] community side of open source, community supported side would be like, yeah, all right, that's
[3019.98 → 3020.14] cool.
[3020.20 → 3020.56] That's fair.
[3021.66 → 3024.76] The number we came up with, that I came up with at the time that Sentry has picked up
[3024.76 → 3030.98] with is $2,000 per year per developer employed at Sentry.
[3031.30 → 3031.54] Okay.
[3031.92 → 3032.60] Let me unpack that.
[3032.66 → 3033.30] That was a lot right there.
[3033.30 → 3034.18] Yeah, please say that again or something.
[3034.42 → 3036.40] So $2,000 a year.
[3036.86 → 3039.96] And the thinking is like, all right, how do we value this?
[3039.98 → 3041.26] There are a few different ways to value it.
[3041.98 → 3043.06] Here's how we're going to think about it.
[3043.06 → 3048.42] What we're doing is making our developers more productive.
[3048.70 → 3051.24] Because if that open source software didn't exist, what would we have to do?
[3051.56 → 3052.12] Write it ourselves.
[3052.26 → 3053.10] Write it ourselves, right?
[3053.10 → 3054.94] Write it ourselves or pay somebody else for it, right?
[3055.18 → 3055.40] Right.
[3055.62 → 3060.46] So kind of, you know, and, you know, like maybe put some links somewhere if this goes anywhere.
[3060.60 → 3063.28] But like, yeah, that's what we ended up with.
[3063.32 → 3067.64] It was like looking globally at, all right, what's the making some bunch of assumptions.
[3067.64 → 3078.50] What's the amount that our developers, like, you know, what's the amount by which their productivity has increased because of the open source software that they have available?
[3078.90 → 3081.82] And that, yeah, the number we came up with was $2,000 a year, right?
[3082.10 → 3083.50] That that's the increase in their productivity.
[3084.08 → 3085.42] Now, you can argue with that.
[3085.48 → 3085.88] You can differ.
[3086.10 → 3090.12] But the point is, let's have that conversation to say, first principle is like, what is fair?
[3090.54 → 3091.74] So let's start from that.
[3092.22 → 3095.64] And so, you know, we did $155 last year.
[3096.48 → 3098.38] You know, so last year it was like, all right, we got 75 devs.
[3098.58 → 3099.90] We got $2,000 a pop.
[3100.02 → 3100.92] $150 is our budget.
[3101.16 → 3103.24] Now we figure out how to spend it as a separate thing, right?
[3103.54 → 3106.44] And so this year set the budget, you know, a while ago.
[3106.52 → 3107.68] But, yeah, we put it at $260.
[3107.68 → 3110.12] So it's roughly in line with our growth as a company.
[3110.20 → 3112.76] But it's pegged to $2,000 per engineer on staff.
[3112.90 → 3113.96] Does that answer your question, Adam?
[3113.96 → 3114.10] Yeah.
[3114.28 → 3114.44] Yeah.
[3114.72 → 3115.06] It does.
[3115.18 → 3119.52] I mean, because a lot of what's happening with OS POS is burgeoning.
[3119.52 → 3120.14] Like, it's new.
[3120.36 → 3123.18] So new organizations are taking this more seriously.
[3123.42 → 3123.60] Yep.
[3123.68 → 3125.94] Taking the principles of giving back to open source more seriously.
[3126.08 → 3126.24] Yep.
[3126.42 → 3130.60] And as you see more and more folks like you guys be examples to follow, you got to think,
[3130.68 → 3131.36] like, what's the science?
[3131.44 → 3131.64] Yeah.
[3131.80 → 3132.02] Right?
[3132.16 → 3132.32] Yeah.
[3132.32 → 3133.54] How do I determine my number?
[3133.54 → 3135.72] Is it like, is it per the money we make?
[3135.86 → 3136.40] Is it revenue?
[3136.58 → 3137.14] Is it a tithe?
[3137.20 → 3137.82] Is it 10%?
[3138.06 → 3140.58] Or, you know, how do we quantify the dollar amount?
[3140.88 → 3143.16] And I think that's a good number because you do base it on engineers.
[3143.50 → 3143.60] Yeah.
[3143.80 → 3148.66] Obviously, I can't think of one engineer who would develop anything and not use open source.
[3148.66 → 3151.00] So, obviously, there's a touchpoint there.
[3151.06 → 3151.20] Yeah.
[3151.54 → 3153.22] So, that's a key metric, right?
[3153.28 → 3154.24] You wouldn't say, well...
[3154.24 → 3155.26] Come up with something, right?
[3155.42 → 3155.58] Yeah.
[3155.60 → 3155.72] Yeah.
[3156.52 → 3158.36] It's something that somebody can adopt pretty easily.
[3158.50 → 3159.16] Okay, 2K.
[3159.54 → 3160.94] Maybe it's like, okay, we can't do 2K.
[3161.02 → 3161.80] We'll do 1K.
[3161.86 → 3162.02] Sure.
[3162.14 → 3163.04] But we'll base it on engineers.
[3163.12 → 3164.06] We have 50 engineers.
[3164.20 → 3164.60] It's 1K.
[3164.76 → 3165.22] It's $50,000.
[3165.72 → 3166.76] So, that's how we think about it.
[3166.80 → 3166.92] Yeah.
[3166.92 → 3167.86] Again, different ways you could.
[3168.00 → 3168.92] You could do a percentage.
[3170.30 → 3172.00] 10 would be high of...
[3172.00 → 3173.50] Well, it depends on what you do it, but...
[3173.50 → 3173.64] Yeah.
[3173.64 → 3173.70] Yeah.
[3174.14 → 3176.86] So, that's how you set the budget side.
[3176.98 → 3178.78] And then there's how you divvy it up, right?
[3179.66 → 3183.28] And what I like here is, like, we're getting better and better tools, right?
[3183.32 → 3187.32] Like, you remember five years ago, six years ago, when we were talking, you're like, did
[3187.32 → 3189.24] GitHub sponsors, did that even exist?
[3189.42 → 3189.92] You know what I mean?
[3189.98 → 3191.24] Like, Open Collective, barely.
[3191.54 → 3192.14] Barely, yeah.
[3192.50 → 3194.44] You know, Git Tip, Gateway was winding down.
[3194.56 → 3195.96] Some others, Liberapay was coming up.
[3196.92 → 3199.20] You know, Patreon was still pretty early days.
[3199.20 → 3201.80] But now, like, we've got GitHub sponsors.
[3202.10 → 3203.06] We've got Open Collective.
[3203.60 → 3206.60] And what I love now is these new platforms, thanks.dev.
[3206.72 → 3212.72] So, shout out to thank.dev and to Stack Aid, two new platforms that we did pilots with for
[3212.72 → 3214.52] this year's Century Funding Program.
[3214.62 → 3217.00] So, we use, you know, we do our foundations, right?
[3217.04 → 3220.40] Like, direct payments to, you know, Python Software Foundation and Open Source Initiative
[3220.40 → 3220.68] and different.
[3221.16 → 3228.42] But then we use these four platforms to, yeah, give out these donations to kind of the long
[3228.42 → 3229.10] tail, right?
[3229.20 → 3235.54] Anywhere from, yeah, like, $6,000, $7,000 for the year down to, like, $100 for the year,
[3235.60 → 3235.76] right?
[3235.78 → 3236.32] The long tail.
[3236.40 → 3237.62] Again, going back to that depth and that breadth.
[3238.08 → 3239.76] And what enables that is these platforms.
[3240.98 → 3244.80] And so, Open Collective and GitHub sponsors are kind of that, I want to call it the first
[3244.80 → 3247.82] generation and maybe Git Tip was, like, the zeroth generation or something.
[3248.12 → 3249.30] There's even older ones, too, right?
[3249.78 → 3250.10] Pledge.
[3250.34 → 3251.10] Shout out to Pledge.
[3251.22 → 3251.80] You remember that one?
[3251.80 → 3251.96] Yeah.
[3252.08 → 3252.52] Pledge, yeah.
[3252.52 → 3254.40] They were integrated into GitHub.
[3254.92 → 3255.08] That's right.
[3255.08 → 3258.08] They had a partnership with GitHub where they were, like, in the sidebar.
[3258.08 → 3259.36] You remember that?
[3259.52 → 3260.36] Good old days.
[3260.62 → 3261.00] Old school, right?
[3261.32 → 3261.54] Yeah.
[3262.50 → 3264.06] Guess who else was integrated on the GitHub?
[3264.32 → 3264.68] Uh-oh.
[3265.72 → 3267.30] GitHub.com slash explore.
[3267.68 → 3267.88] No.
[3268.42 → 3269.26] Tell me a story.
[3269.42 → 3269.78] Explore.
[3269.92 → 3270.26] Explore.
[3270.26 → 3270.72] Tell me a story.
[3271.10 → 3271.74] The early days.
[3271.84 → 3273.10] Like, this is way, way early days.
[3273.10 → 3277.74] So, our RSS feed of our podcast was live.
[3278.08 → 3283.06] Like, it would, like, take the RSS and turn it to HTML on explore in the sidebar.
[3283.28 → 3283.60] GitHub.
[3283.72 → 3284.44] They changed, you know.
[3284.56 → 3284.76] I mean.
[3285.28 → 3286.32] Funding Microsoft.
[3286.50 → 3286.64] Yeah.
[3287.12 → 3287.56] I don't know.
[3287.64 → 3289.10] That was before Microsoft's days.
[3289.42 → 3290.56] But they were.
[3290.72 → 3290.86] Yeah.
[3290.98 → 3291.22] They were.
[3291.44 → 3291.52] I don't know.
[3291.58 → 3292.04] It makes sense.
[3292.24 → 3292.90] But, well.
[3293.26 → 3293.72] They grew up.
[3293.80 → 3294.22] It was fun.
[3294.34 → 3294.78] It was great.
[3294.92 → 3295.36] While it lasted.
[3295.36 → 3295.84] While it lasted.
[3295.84 → 3295.98] Yeah.
[3296.30 → 3296.78] It made sense.
[3296.78 → 3297.28] That's awesome, man.
[3297.74 → 3298.10] That's super.
[3298.10 → 3299.64] Well, here's a fun little sidebar, then.
[3300.56 → 3302.92] Last year, we did our funding program.
[3303.26 → 3308.38] Then we did a follow-up, like, virtual event with half a dozen maintainers.
[3308.88 → 3311.32] And it was hosted by myself and Jessica Lord.
[3311.86 → 3312.64] Shout out, Jessica.
[3312.88 → 3312.98] Yeah.
[3312.98 → 3315.22] The PM for GitHub Sponsors.
[3315.40 → 3315.52] Yep.
[3315.52 → 3315.66] Right?
[3316.04 → 3316.20] Yep.
[3316.40 → 3318.16] And here's the fun thing I'm trying to get to.
[3319.04 → 3320.44] Am I going to tell the story?
[3320.58 → 3320.72] Yeah.
[3320.88 → 3325.84] Sentry's creative director, founding creative director, he's no longer there, did great work.
[3325.84 → 3328.22] And he came from GitHub.
[3328.58 → 3332.20] Because Chris Jennings, one of our founders, came from GitHub, brought Cameron with him.
[3332.90 → 3335.32] And so Cameron invented the October.
[3335.84 → 3336.26] Is that right?
[3336.36 → 3336.52] Yeah.
[3336.62 → 3336.98] Nice.
[3337.02 → 3339.44] And then ended up at Sentry, like, did all the Sentry stuff.
[3339.86 → 3340.72] Now it's moved on.
[3342.78 → 3349.24] And so when we went to do this event together, we were like, hey, GitHub, we want to do artwork
[3349.24 → 3357.68] that includes the Sentry, like, you know, character and Mona, the October, like, in one artwork.
[3358.00 → 3360.06] And at first they were like, yeah, no, we don't do that.
[3360.44 → 3362.44] And then, you know, we had some conversations.
[3363.10 → 3366.60] And long story short, you can go on, you know, we'll put the link in or whatever.
[3366.92 → 3369.76] But yeah, that artwork made it out to the light of day.
[3369.76 → 3373.72] So we got a little Sentry GitHub collab going on.
[3373.98 → 3374.24] A collab.
[3374.24 → 3374.32] Yeah.
[3374.50 → 3374.82] Nice.
[3375.02 → 3375.94] You know, just a moment.
[3376.30 → 3377.30] It's not the feed, right?
[3377.42 → 3377.58] Right.
[3377.58 → 3378.16] Where it's like evergreen.
[3378.16 → 3378.42] Yeah, it's not the feed.
[3378.42 → 3380.06] But just like a little moment.
[3380.50 → 3381.42] Anyway, that stuff's fun, right?
[3381.46 → 3383.22] We've done some collabs over the years with them.
[3383.96 → 3384.94] We had Jessica Lord on the show.
[3385.18 → 3385.36] Yeah.
[3385.94 → 3386.26] Yeah.
[3386.52 → 3387.28] I mean, really, look.
[3387.50 → 3388.14] Devin Fuel.
[3388.32 → 3388.70] Say again?
[3388.88 → 3389.60] Oh, yeah, sure.
[3389.60 → 3391.40] We did a show with Devin when sponsors first launched.
[3391.62 → 3391.90] Okay.
[3392.28 → 3395.20] And then we did a show with Jessica Lord when she took over.
[3395.64 → 3397.46] I just think it's so awesome to see.
[3397.90 → 3399.38] Now it feels like status quo, right?
[3399.38 → 3401.90] Now it feels like GitHub sponsors, which is awesome, right?
[3401.94 → 3403.64] It's like now we've got that baseline.
[3403.94 → 3409.50] And now what I'm seeing with Thanks Dev and with Stack Aid is like next level, which is just what we need.
[3409.56 → 3410.92] We need to keep moving it forward, you know?
[3411.02 → 3413.42] Figure out how to make it easier for companies like Sentry.
[3413.76 → 3415.88] Like I'm doing a lot of grunt work to make this work.
[3416.24 → 3420.78] The easier we can make it for companies, like you said, like find those simple.
[3420.96 → 3422.04] All right, here's the simple story.
[3422.30 → 3423.22] Here's the right amount.
[3423.58 → 3426.50] You know, here's how you get it to the right dependencies.
[3426.84 → 3427.98] Like the simpler we make it.
[3427.98 → 3432.98] I mean, what I want to see is like I don't want Sentry to be out front like, oh, good job, Sentry.
[3433.06 → 3433.88] You have this great program.
[3433.98 → 3436.30] I want it to just be like, of course, like everybody does this.
[3436.36 → 3437.00] It has to be normal.
[3437.18 → 3437.52] You know what I mean?
[3437.86 → 3439.62] That's where we're going to really have that.
[3439.98 → 3442.96] I mean, this is kind of getting back to what you were asking about impact and how we think about impact.
[3443.98 → 3448.90] You know, some of it is, yeah, the impact on the projects themselves right now.
[3449.02 → 3450.08] But look, let's be honest.
[3450.16 → 3453.12] Like $260,000 isn't actually that much.
[3453.16 → 3453.64] You know what I'm saying?
[3453.64 → 3455.00] Like it's a lot, but it's not a lot.
[3455.24 → 3460.26] When you look at, you know, the open SSF that has like $5 million, you know, like here you go.
[3460.32 → 3460.46] Right?
[3460.56 → 3467.62] Like the larger the fangs and everybody like Microsoft, they're able to do these larger dollar amount things.
[3467.62 → 3471.12] But relative to the size of their company, that's what we look at.
[3471.18 → 3471.44] Right.
[3471.78 → 3473.38] And feel good about what we're doing.
[3473.48 → 3474.64] Is that like...
[3474.64 → 3485.62] Have you ever thought about if more organizations that made sense now, like maybe really dev-focused organizations took on this idea of $2K, $1K per?
[3485.62 → 3486.00] Do it, man.
[3486.04 → 3486.50] Let's do it.
[3486.54 → 3486.68] Yeah.
[3486.74 → 3487.80] You know what would happen?
[3487.94 → 3489.44] Like have you ever quantified that number?
[3489.44 → 3498.60] I mean, in the sense that I started from that to get to the $2K, to be like, well, here's the value and here's the number of, you know, here's the...
[3498.60 → 3507.20] Again, this is a few years ago I wrote this thing, but like here's the size of the tech industry worldwide and here's the 22 million software developers in the world or whatever.
[3507.56 → 3508.32] Like do that division.
[3509.10 → 3510.90] So from that point of view, starting there.
[3510.90 → 3517.26] But yeah, bottom up, it's like every year we just need like Spotify just put out a program.
[3517.44 → 3517.92] You know what I mean?
[3518.26 → 3518.48] Right.
[3518.56 → 3519.22] Did you have them on?
[3519.30 → 3521.02] Did you talk to Pear from Spotify?
[3521.24 → 3522.00] Not about that.
[3522.12 → 3522.38] Yeah.
[3522.60 → 3524.34] So they did a thing.
[3525.98 → 3529.60] You know, I saw, you know, even Chrome just did like, well, what?
[3529.70 → 3535.54] GitHub did half a million earlier this year and then Chrome has half a million for web frameworks.
[3535.76 → 3536.50] 44 billion.
[3537.26 → 3538.68] That's how much it would be if it was...
[3538.68 → 3540.86] 22 million times 2,000 each.
[3540.86 → 3543.20] $1,000 times 22 million developers across the world.
[3543.36 → 3543.90] It sounds about...
[3543.90 → 3545.18] Yeah, because that's how I was thinking of it.
[3545.20 → 3545.22] $44 billion.
[3545.82 → 3546.58] How big...
[3546.58 → 3547.34] Yeah, because I was thinking of it as like...
[3547.34 → 3547.86] I had to do the math.
[3547.86 → 3548.24] I'm sorry.
[3549.10 → 3550.14] No, I appreciate you.
[3550.22 → 3550.92] I appreciate you.
[3551.16 → 3551.86] I appreciate you.
[3551.86 → 3553.72] Because if you think about...
[3553.72 → 3554.92] Think about it this way.
[3555.44 → 3560.16] The open source, the community supported open source ecosystem, community.
[3560.88 → 3564.24] Think of it as like another sleeping tech giant.
[3564.88 → 3565.38] Okay?
[3565.78 → 3570.84] You got how many tens of thousands working for Microsoft, for, you know, Meta now, I guess.
[3570.86 → 3572.36] You know, Apple, Amazon.
[3572.94 → 3575.84] Like, the open source community is like another tech giant.
[3576.04 → 3576.22] Right.
[3576.32 → 3576.50] Right?
[3576.82 → 3585.24] So look at how much revenue do those, you know, tech giants bring in and like use that as the
[3585.24 → 3587.00] benchmark for the revenue that the open source...
[3587.00 → 3589.32] Like the value that the open source community is bringing to the world.
[3589.42 → 3589.54] Yeah.
[3589.62 → 3590.78] That's the way to think about it.
[3591.50 → 3593.80] Yeah, I guess it's kind of good too to put that...
[3593.80 → 3594.12] Yeah.
[3594.12 → 3598.24] You put that money back in the hands of the, you know, the maintainers and the creators
[3598.24 → 3598.66] and whatnot.
[3599.18 → 3600.38] You guys want something controversial?
[3601.10 → 3601.90] Mildly controversial?
[3602.18 → 3602.38] Please.
[3602.54 → 3602.66] Sure.
[3603.14 → 3603.36] Sure.
[3603.36 → 3603.94] There's a discount.
[3604.08 → 3604.70] There's a discount.
[3605.06 → 3606.70] The flip side of that is there's a tax.
[3607.14 → 3608.48] And it's not the same for everybody.
[3608.62 → 3614.12] But when you average it out, there's people that will work on open source software for a
[3614.12 → 3618.36] lot less than you would need to pay them to work on your proprietary software.
[3618.62 → 3618.92] Right.
[3619.08 → 3619.60] You know what I'm saying?
[3619.70 → 3619.86] Yeah.
[3619.86 → 3620.14] Yeah.
[3620.36 → 3623.36] So I think that factors into it, to be honest, right?
[3623.42 → 3624.26] It's like...
[3624.26 → 3626.26] And this was me because you remember when I was doing Kiddie.
[3627.14 → 3628.54] I pronounced it that way for you, Adam.
[3628.68 → 3629.10] Thank you.
[3629.10 → 3629.72] When I was doing Kiddie.
[3629.72 → 3629.84] Thank you.
[3630.18 → 3631.02] Like I was there on the platform.
[3631.02 → 3632.36] I swear you said Kiddie originally.
[3632.36 → 3633.12] I'm sure I did.
[3633.30 → 3633.78] You're right.
[3633.88 → 3635.38] I'm probably on tape with you saying Kiddie.
[3635.38 → 3635.90] Yeah, I think so.
[3636.08 → 3636.72] We'll go back.
[3636.74 → 3637.20] We'll go back.
[3637.34 → 3637.44] We'll review it to the archives.
[3637.44 → 3638.94] If we have it, we're going to put it here right now.
[3638.94 → 3639.72] The archives, yeah.
[3641.12 → 3644.26] So we're here today to talk about sustaining open source.
[3644.48 → 3645.56] Can you help us talk about that, Chad?
[3645.88 → 3646.84] Oh, my heavens.
[3647.56 → 3647.88] Absolutely.
[3647.88 → 3648.76] All right.
[3649.86 → 3650.66] Kiddie is my name.
[3651.16 → 3652.10] Kiddie is my game.
[3652.76 → 3659.42] Giddip.com is a website which primarily right now is being used by open source developers
[3659.42 → 3661.08] and the companies that love them.
[3661.82 → 3668.12] And it's a crowdfunding site where you can go, and you can set up a dollar a week or $3
[3668.12 → 3674.92] a week as a gift to someone whose work you love and admire and are inspired by.
[3675.54 → 3676.10] Yeah.
[3676.10 → 3682.70] I was working for not very much money really hard on Kiddie because I loved it because the
[3682.70 → 3684.62] intrinsic motivation, the passion, you know what I mean?
[3685.44 → 3688.80] And I think there's something there.
[3688.86 → 3690.06] We don't need to focus on that.
[3690.20 → 3691.74] But it's like, yeah.
[3692.08 → 3696.70] Well, what I think that means is that there's a way to make this work.
[3697.26 → 3698.52] Let's bring it back around to this.
[3698.52 → 3704.34] I think that we can actually get to the dream.
[3704.78 → 3708.00] And the dream is for, again, going back to that idea of there's an open source community,
[3708.26 → 3711.60] there's a commercial open source side, there's a side that doesn't want any money at all,
[3711.82 → 3713.82] but then there's that community supported portion.
[3714.24 → 3715.16] We can make it work.
[3715.36 → 3719.28] We can make sure that those folks in the community supported open source, you know,
[3719.40 → 3722.18] part of open source, that they get what they need.
[3722.18 → 3722.90] You know what I mean?
[3723.10 → 3723.96] That they get there.
[3724.54 → 3727.36] Is it $70,000, $80,000, $100,000 a year?
[3727.88 → 3729.14] Enough for the health insurance.
[3729.26 → 3729.76] You know what I mean?
[3729.84 → 3732.40] Like, that's what we're trying to get to is the careers, right?
[3732.52 → 3736.60] To be like, kid coming out of school is like, I see a viable option.
[3736.88 → 3738.44] Jessica talks about this from GitHub, right?
[3738.44 → 3744.82] Like, I see a viable option to go into open source as a career on that community supported level.
[3744.96 → 3745.08] Yeah.
[3745.44 → 3746.26] I think we can get there.
[3746.88 → 3751.02] Maybe not next year, but we keep chipping away, you know, and it'll tip.
[3751.02 → 3752.10] We got to hit that tipping point.
[3752.14 → 3755.66] And it's predicated on the fact that your organization uses that open source.
[3755.74 → 3758.72] So you said if you stop using X, you stop giving X.
[3758.72 → 3759.82] You just move your budget somewhere else.
[3759.82 → 3761.94] And it's not because you don't value their work anymore.
[3761.98 → 3763.68] It's because you literally don't use their work anymore.
[3764.08 → 3768.48] Yeah, which basically is not valuing their work anymore, but not in the sense of like a personal thing.
[3768.58 → 3769.34] You know what I mean?
[3769.42 → 3769.86] Yeah, exactly.
[3769.96 → 3770.66] That's what I mean by that.
[3770.74 → 3770.96] Yeah.
[3771.42 → 3773.78] Is that the work is still valued, but you're not using it anymore.
[3773.86 → 3775.62] So organizationally, you're not valuing it.
[3775.66 → 3779.92] So, the dollars you put into the OSLO funding bucket, whatever it's called,
[3779.92 → 3783.30] now gets allocated to the projects you are using.
[3783.50 → 3783.66] Exactly.
[3784.32 → 3787.24] So that, you know, if you have users, you should have funding.
[3787.36 → 3787.50] Yeah.
[3788.14 → 3788.86] I mean, jQuery.
[3789.06 → 3790.24] Somebody's still using jQuery.
[3790.48 → 3791.28] A lot of people are using jQuery.
[3791.28 → 3791.42] Right?
[3791.66 → 3794.56] It's only like 83% of websites a couple of years ago.
[3794.98 → 3796.52] Mate, like there's, that's fine, man.
[3796.52 → 3797.94] There are different parts of the tech curve.
[3799.66 → 3800.02] Yeah.
[3800.30 → 3801.20] I think we can figure it out.
[3801.26 → 3802.24] There's still a lot of work to do.
[3802.80 → 3803.58] Appreciate you guys.
[3803.96 → 3804.72] To the road ahead.
[3804.88 → 3806.18] Helping with the story.
[3806.30 → 3806.40] Yeah.
[3806.44 → 3806.98] To the road ahead.
[3806.98 → 3807.56] For sure, man.
[3807.72 → 3811.50] I'm glad to have you back on to explain it because seriously, we missed you.
[3811.86 → 3812.08] Yeah.
[3812.20 → 3812.70] Thanks, man.
[3812.70 → 3817.96] I saw you pop up nine months, 12 months ago, and I was like, whoa, there's Chad.
[3818.06 → 3818.84] We're going to Century.
[3819.00 → 3819.40] He's back.
[3819.62 → 3821.94] And by the way, you all probably know this Century is one of our sponsors.
[3822.00 → 3822.52] We love them.
[3822.60 → 3822.86] Yeah.
[3823.04 → 3824.70] But I was like, wow, there's Chad.
[3824.76 → 3825.16] We're going to Century.
[3825.16 → 3825.68] That's awesome.
[3825.82 → 3826.94] And we love Century.
[3826.94 → 3827.84] And we use Century.
[3827.98 → 3828.58] And it's amazing.
[3828.78 → 3829.10] Heck yeah.
[3829.64 → 3830.90] We appreciate you guys too, man.
[3831.38 → 3831.94] Good to see you, Chad.
[3832.06 → 3832.46] Thank you.
[3832.54 → 3832.90] Thank you.
[3832.96 → 3833.44] Love you guys.
[3833.60 → 3834.00] Love you too.
[3834.36 → 3834.72] All right.
[3834.84 → 3835.12] Love you.
[3835.38 → 3835.72] Love you.
[3835.72 → 3836.18] You're wrapping it up.
[3836.48 → 3836.68] Yeah.
[3836.90 → 3837.06] All right.
[3837.12 → 3837.40] That's it.
[3837.52 → 3837.76] Cool.
[3837.86 → 3838.08] Cool.
[3838.12 → 3838.48] That's wrapped.
[3839.08 → 3839.38] Thanks.
[3839.38 → 3839.62] Thanks.
[3839.62 → 3842.04] Bye.
[3842.10 → 3842.62] Bye.
[3858.64 → 3859.06] Bye.
[3861.32 → 3863.52] Bye.
[3863.52 → 3864.34] Bye.
[3864.36 → 3865.28] Bye.
[3865.28 → 3865.32] Bye.
[3865.32 → 3865.52] Bye.
[3865.52 → 3865.60] Bye.
[3865.72 → 3870.16] This episode is brought to you by Retool,
[3870.32 → 3873.56] and they have a private beta ready for you to check out.
[3873.72 → 3878.54] This is the fastest way to now build native mobile apps
[3878.54 → 3879.60] for your mobile workforce.
[3879.94 → 3883.18] There is no complex frameworks anymore or tedious deployments.
[3883.18 → 3885.68] You can build mobile apps with what you already know,
[3885.84 → 3887.44] like JS and SQL.
[3888.06 → 3892.62] This is all in the browser, no code, or what they call low code.
[3892.98 → 3893.74] Join the wait list.
[3893.74 → 3897.92] Head to retool.com slash products slash mobile.
[3898.08 → 3899.48] The link will be in the show notes.
[3899.58 → 3902.98] Again, retool.com slash products slash mobile.
[3918.32 → 3921.54] You guys are making my whole year do this.
[3921.54 → 3922.94] You seriously are, man.
[3922.94 → 3923.98] I'm sorry you're about saying that.
[3924.70 → 3926.88] No, but I'm being sort of, you know, genuine.
[3926.98 → 3931.84] This is like, you guys just absolutely kill podcasting.
[3932.18 → 3932.70] Thank you, man.
[3933.38 → 3934.68] We aim to please.
[3934.86 → 3937.26] So, you know, we're here at All Things Open.
[3937.88 → 3938.72] We got Ricardo.
[3939.16 → 3939.92] Ricardo, yeah, that's right.
[3940.00 → 3941.06] How do you see it last in Ricardo?
[3941.28 → 3941.90] It's Suedes.
[3942.16 → 3944.94] It's a Spanish name, but it's actually from Galicia.
[3944.94 → 3950.58] Yeah, so I often, when I go to Portugal, they get excited, right, because they think it's a Portuguese name, but it's actually Spanish.
[3950.98 → 3951.74] So, Suedes.
[3952.08 → 3952.40] Suedes.
[3952.58 → 3952.98] Suedes.
[3953.42 → 3954.72] Not a very common name.
[3954.84 → 3956.22] No, I've never seen that one before.
[3956.30 → 3956.84] Yeah, yeah, yeah.
[3956.84 → 3960.18] So, open source, AWS, what do you do?
[3960.26 → 3960.66] Tell us.
[3960.74 → 3961.20] Hi, everyone.
[3961.30 → 3965.18] Well, listen, first, I just want to say a massive thank you for inviting me on here, right?
[3965.24 → 3966.86] This is a real dream come true for me.
[3967.00 → 3967.26] Hey.
[3967.26 → 3968.00] But what I do is I...
[3968.00 → 3968.78] We love having listeners on.
[3968.98 → 3969.26] Sorry?
[3969.48 → 3970.46] We love having listeners on.
[3970.56 → 3970.76] Yeah.
[3970.76 → 3972.30] Having listeners on the show is the best.
[3972.66 → 3973.44] Yeah, exactly.
[3973.60 → 3979.36] So, what I do is I've been working in open source for over 20 years, and more recently, I joined AWS as a developer advocate.
[3980.08 → 3985.44] And so, what I try and do is I try and kind of act as the voice of the open source developers internally.
[3986.06 → 3989.68] And I hope I try and make AWS the best place to run open source technology.
[3990.02 → 3990.24] Okay.
[3990.34 → 3993.02] So, a lot of the time I spend speaking with builders.
[3993.54 → 3995.42] We call builders the people that actually do the hands-on stuff.
[3996.04 → 3997.48] So, that could be a maintainer.
[3997.48 → 4002.34] It could be someone just, you know, doing some documentation for a project or actually just running it, right?
[4002.38 → 4006.40] And then really excited about how they've run it in a specific way and want to share that with everyone.
[4006.54 → 4016.18] So, I do a weekly newsletter and I do a bi-weekly Twitch show where we try and get some of that energy out so more people can, you know, know about these open source projects, right?
[4016.18 → 4017.00] Is this all internal?
[4017.58 → 4018.22] No, it's external.
[4018.36 → 4018.60] Okay.
[4018.60 → 4020.98] So, the Twitch session is external.
[4021.12 → 4021.92] The newsletter is external.
[4022.50 → 4025.32] And I try and feature the projects that, you know, people create.
[4025.66 → 4025.88] Okay.
[4025.88 → 4028.24] And, you know, they fit in lots of different categories, right?
[4028.26 → 4030.20] But a lot of them are developer experience.
[4030.50 → 4035.42] So, you know, AWS is a great, you know, a tool for building stuff on, right?
[4035.76 → 4038.56] But sometimes people want, like, you know, to make things simpler.
[4038.82 → 4041.40] So, they build an open source project that solves a lot of problems, right?
[4041.40 → 4041.64] Right.
[4042.16 → 4043.32] And so, I see a lot of that.
[4043.40 → 4047.66] I see a lot of these really cool projects that then people love using.
[4047.66 → 4051.02] So, a good one from a guy called Australia, ELK.
[4052.02 → 4054.34] He created this open source tool called Form 2.
[4054.76 → 4060.94] And it allows you to, from your console, reverse engineer cloud formation scripts through a GUI tool, right?
[4061.02 → 4061.38] Is that right?
[4061.52 → 4061.90] Yeah, yeah.
[4062.02 → 4063.62] So, it's tools like that, right?
[4064.62 → 4066.34] Every week, I'm amazed, right?
[4066.34 → 4069.18] Because I do a weekly newsletter and I feature these in my weekly newsletter.
[4069.50 → 4075.04] And I'm always blown away by the creativity, the passion that these people have.
[4075.60 → 4076.72] Well, you do what we do, basically.
[4076.84 → 4079.96] But you do it for AWS, and we do it for open source at large.
[4080.14 → 4080.40] You do.
[4080.40 → 4082.60] I guess software at large, right?
[4082.66 → 4083.60] I mean, but there is no.
[4083.66 → 4083.96] Yeah.
[4084.08 → 4084.70] There is no.
[4084.70 → 4085.26] We just kind of do it.
[4085.26 → 4085.90] We don't dig in, you know?
[4085.90 → 4086.90] You just kind of do it and put it out there.
[4087.08 → 4087.34] Yeah.
[4087.56 → 4089.52] And actually, that's why I love your podcast, right?
[4089.52 → 4093.14] Because every week, right, I get to know about a new different open source project.
[4093.22 → 4093.46] Right.
[4093.54 → 4096.22] Or an insight that I didn't know about before.
[4096.42 → 4096.60] Yeah.
[4096.60 → 4098.20] And it's not always just about the project, right?
[4098.24 → 4104.86] What I learned from you guys is the stuff around actually how you build the project, what the inner workings of it, the things that you don't necessarily think.
[4104.86 → 4108.64] But when I speak to customers, right, they want to know how this stuff works.
[4108.72 → 4108.88] Yeah.
[4108.88 → 4111.88] And increasingly, I'm quoting stuff from your podcast.
[4111.96 → 4112.18] What?
[4112.42 → 4112.70] Yeah.
[4112.82 → 4113.34] Yeah, seriously.
[4113.42 → 4113.98] That's awesome.
[4114.30 → 4115.28] That's the way to do it, Jared.
[4115.54 → 4116.10] Yeah, totally.
[4116.32 → 4117.02] That's a lot of pressure.
[4117.14 → 4119.26] I'm going to have to start saying quote-worthy stuff more often.
[4119.38 → 4119.76] Oh, yeah.
[4119.86 → 4122.54] Well, you know, you win some, you lose some.
[4123.78 → 4124.54] Quote me on that.
[4126.66 → 4128.70] But I mean, I got a question for you, right?
[4128.70 → 4128.92] Okay.
[4128.92 → 4130.84] So you've been doing it for a long, long time, okay?
[4131.06 → 4131.26] Yeah.
[4131.26 → 4133.18] And every week, you keep the energy.
[4133.78 → 4135.14] You're just as enthusiastic.
[4135.64 → 4136.26] So how do you do it?
[4136.26 → 4140.40] What is it that makes you kind of like get up and think, yeah, we're doing another changelog?
[4141.12 → 4141.84] I got it, man.
[4142.24 → 4142.58] Go ahead.
[4142.66 → 4143.42] You got to love the game.
[4143.66 → 4143.90] Yeah.
[4144.16 → 4145.28] If you love the game, it's easy.
[4145.58 → 4146.22] Yeah, totally, man.
[4146.22 → 4146.56] You know what I mean?
[4146.92 → 4149.22] No, that's cliché to say.
[4149.22 → 4154.52] But if you do love the game, even if you get tired a little bit, you can still kind of show up for the most part.
[4154.98 → 4157.92] But if you love the game, you kind of come at it and you enjoy it.
[4158.22 → 4161.08] And you find like you do with new passions, you see what people are making.
[4161.26 → 4164.36] And you get like their energy gives you energy, you know.
[4164.36 → 4168.98] So the world of software is just like always, always changing.
[4169.22 → 4172.90] So like every single year, it's kind of the same but kind of different.
[4173.18 → 4173.56] You know what I mean?
[4173.84 → 4174.00] Yeah.
[4174.00 → 4177.90] It's the same in the fact that it's technology, and it's movement, it's innovation.
[4177.90 → 4179.70] But it's like, what's going to be big this year?
[4180.00 → 4180.60] Generative AI?
[4180.92 → 4182.50] Was it Web3?
[4182.72 → 4183.42] Well, maybe not.
[4183.42 → 4185.92] Web5 now, Web5.
[4186.42 → 4188.08] Platforms, no ops, you know what I mean?
[4188.10 → 4188.74] No ops required.
[4189.34 → 4191.16] A lot of things like that, automation happening.
[4191.36 → 4195.56] So I mean, every year, every six months, it's always something new, always something changing.
[4195.82 → 4199.56] So that sort of like constant change kind of keeps me going personally.
[4199.96 → 4200.40] Yeah, yeah.
[4200.88 → 4201.60] What about you, Gerald?
[4201.68 → 4202.28] What keeps you?
[4202.50 → 4204.22] Yeah, I would say mostly it's the people.
[4204.78 → 4213.00] You know, how can you not get excited to talk to somebody who's wicked smart and like passionate and driven and interesting person who's doing something in the world?
[4213.42 → 4216.46] It's hard not to be excited about that each and every week.
[4216.54 → 4220.02] Of course, sometimes, you know, some days are easier to do it than other days.
[4220.08 → 4224.70] And some days we're like, especially a week when we're doing like J.S. Party, and maybe we're doing a backstage.
[4225.02 → 4227.80] And it's like, how many podcasts can I record this week?
[4227.82 → 4228.30] Right, right.
[4228.38 → 4229.48] And by Friday, we're kind of like.
[4229.48 → 4229.62] And then ship.
[4230.06 → 4230.98] Yeah, and then ship as well.
[4231.00 → 4231.58] And then ship too.
[4232.16 → 4234.22] But it's hard because the thing is, I mean, I do my weekly news.
[4234.28 → 4235.76] I've been doing it two and a half years, right?
[4236.00 → 4240.26] And I know how hard it is sometimes just to get up and just go through it, right?
[4240.42 → 4240.62] Yeah.
[4240.66 → 4242.18] But you've been doing it for more than two years, right?
[4242.18 → 4244.56] So that takes something, right?
[4244.56 → 4245.06] 13 plus years.
[4245.36 → 4245.44] Yeah.
[4245.64 → 4246.38] 13 plus years.
[4246.76 → 4251.52] And what I like as well is that I like how you interject within the people you have and the stories you tell.
[4251.98 → 4254.30] The stuff you're doing with your own sites, right?
[4254.44 → 4254.60] Yeah.
[4254.60 → 4255.74] You say, oh, yeah, yeah, we're doing this way.
[4255.80 → 4257.90] We tried this, and we tried that way, and we found this work.
[4257.96 → 4259.32] So what should we do?
[4259.46 → 4261.94] And I just, I think that's the key to a good podcast, right?
[4261.96 → 4264.66] Is asking the right questions, and you just know how to do it.
[4264.68 → 4266.18] And I think it's because you're practitioners.
[4266.34 → 4267.28] You do this stuff, right?
[4267.28 → 4268.28] That's exactly the thing.
[4268.28 → 4268.62] Yeah.
[4268.62 → 4279.58] One of the things that my fears as a podcaster about software is that I will turn into a guy who only asks questions and not a guy who actually does stuff.
[4279.68 → 4279.82] Yeah.
[4279.82 → 4290.48] And so we stay, you know, we build software, we're developing things, and we can actually call to mind things that we were doing earlier that day or that week or challenges we're having.
[4291.04 → 4293.06] And you can't really fake that.
[4293.68 → 4300.60] And so if we quit writing code, and we quit building stuff, and we just talk to people, well, you lose a bit of your edge.
[4300.84 → 4302.46] And so I found that in the university.
[4302.62 → 4305.62] A lot of the teachers there lost their edge.
[4305.62 → 4316.58] You know, my best professor when I was in school was the guy who was adjunct, and he taught databases at night because he was out there in the field building databases all day.
[4316.68 → 4319.06] He couldn't teach during the day because he was doing databases.
[4319.34 → 4320.78] And then he came and taught us.
[4320.86 → 4322.74] And I was like, this guy knows his stuff.
[4322.90 → 4323.24] Yeah.
[4323.34 → 4328.38] Versus the guy who theorizes and is smart and eloquent but doesn't actually build databases all day.
[4328.60 → 4328.86] Yeah.
[4329.02 → 4329.94] He was my best teacher.
[4330.06 → 4331.72] And so I was like, okay, there's something to this.
[4332.14 → 4335.18] We need people who are out there doing the stuff, talking about the stuff.
[4335.18 → 4336.60] It's so much more beneficial.
[4337.04 → 4337.18] Yeah.
[4337.28 → 4338.06] In the trenches.
[4338.72 → 4338.88] Yeah.
[4338.94 → 4339.82] In the trenches for sure.
[4340.14 → 4340.34] Yeah.
[4340.50 → 4341.56] But it's hard though, right?
[4341.56 → 4347.56] Because a lot of people, I mean, that's a good example because I know in my past, right, when I was doing training courses, I didn't do many of them.
[4347.74 → 4347.88] Yeah.
[4347.92 → 4352.60] But the difference between a good one and a bad one was one that just basically went through the process, right?
[4353.00 → 4358.52] The other one, when you ask questions, well, yeah, I do training three days a week with two days I'm doing consulting or actually doing this stuff.
[4358.52 → 4363.56] And then they actually bring back some of their work into the training, right?
[4363.66 → 4365.92] So it makes everything real and relevant, right?
[4365.98 → 4366.16] Yeah.
[4366.52 → 4370.58] And actually, I'm doing a lot of stuff with students at the moment because I'm very passionate about education.
[4371.10 → 4372.86] I used to do a side hustle of running a school.
[4373.48 → 4373.90] Okay.
[4373.90 → 4376.86] Not technology though, just mainstream school.
[4376.94 → 4377.18] Sure.
[4378.12 → 4385.52] Because I kind of like try to kind of, in the UK, it's very hard for a group of kids who kind of fall through the gaps.
[4385.74 → 4385.90] Yeah.
[4385.98 → 4386.96] And they end up nowhere, right?
[4386.96 → 4390.40] So my school was for that kind of like group of kids that kind of fell through the gaps.
[4390.48 → 4391.54] But they were lovely kids, right?
[4391.96 → 4394.66] They just needed a bit more support that normal school can give you.
[4395.28 → 4398.66] And one of the things I'm doing with students is teaching them open source.
[4399.00 → 4399.36] Nice.
[4399.36 → 4403.20] And it's interesting because I speak to customers, right?
[4403.62 → 4408.48] And they have a very wide knowledge of open source, right?
[4408.82 → 4411.08] But there's a few that do it really, really well and know their stuff.
[4411.56 → 4413.50] The vast majority are in the middle somewhere.
[4413.78 → 4416.30] But too many just don't know anything, right?
[4416.50 → 4416.68] Right.
[4416.68 → 4425.96] So what we're trying to do is go in and teach kids, students age 18 over, trying to give them some of the important baseline.
[4425.96 → 4429.54] And also starting from the history, starting from the past, you know, what is copyright?
[4430.14 → 4431.52] Where did open source come from?
[4431.62 → 4432.80] You know, what was the free software foundation?
[4432.88 → 4436.76] So that they don't end up in a situation where they're making poor choices, right?
[4436.80 → 4437.02] Yeah.
[4437.30 → 4438.18] Because you see that a lot.
[4438.30 → 4438.54] I see that.
[4438.70 → 4442.46] I sometimes see projects, and they make some schoolboy errors, right?
[4442.52 → 4446.42] When it comes to the licensing or how they think about community and all this kind of stuff, right?
[4446.50 → 4449.12] So that education thing is really important to me at the moment.
[4449.20 → 4451.14] So I'm spending a lot of time with that.
[4451.14 → 4455.52] And even though I'm doing that in AWS, I don't really touch about AWS much.
[4455.56 → 4457.50] It's more generic open source, right?
[4457.58 → 4457.94] Right.
[4458.46 → 4458.84] But it's cool.
[4459.14 → 4459.64] It's really cool.
[4459.64 → 4459.82] Very cool.
[4460.30 → 4464.70] So tell us real quick as we close up, tell us your newsletter, the Twitch stream.
[4464.92 → 4466.30] Like, how can people connect with that stuff?
[4466.36 → 4466.62] Yeah.
[4466.74 → 4469.20] So I'm on Dev2 under the AWS.
[4469.44 → 4472.52] So unfortunately, I don't have a very friendly URL I can share with you.
[4472.52 → 4476.12] But if you just Google AWS open source, you should find the newsletter.
[4476.72 → 4478.36] And the show we do every other week.
[4478.66 → 4479.60] It's on Fridays.
[4480.14 → 4481.88] And it's twitch.tv.AWS.
[4482.36 → 4485.36] So I'd love to see some of the Changelog family come along and check it out.
[4485.36 → 4485.88] Yeah, for sure.
[4486.14 → 4486.44] For sure.
[4486.70 → 4488.14] And again, thank you a lot, guys.
[4488.20 → 4489.34] This has really made my way.
[4489.34 → 4489.80] We appreciate it.
[4489.80 → 4491.70] Hey, we're happy to talk to Ricardo.
[4491.82 → 4492.90] So thank you for talking to us.
[4492.94 → 4493.30] Thank you.
[4493.80 → 4494.20] All right.
[4494.70 → 4495.14] Oh, my God.
[4495.16 → 4496.88] That is just mind-blowing.
[4496.96 → 4497.38] Is that it?
[4498.46 → 4499.20] High five, dude.
[4500.00 → 4500.80] No, that is just enough.
[4503.14 → 4503.64] That's it.
[4503.66 → 4504.20] This show's done.
[4504.30 → 4505.14] Thank you for tuning in.
[4505.26 → 4510.38] It was a blast being at All Things Open and an even bigger blast meeting fans, new and old,
[4510.48 → 4511.76] and everywhere in between.
[4512.20 → 4516.24] Again, a big thanks to Todd Lewis and team for having us at All Things Open.
[4516.32 → 4517.22] We appreciate the invite.
[4517.32 → 4520.82] Of course, big thank you to our friends and partners at Vastly and Fly.
[4521.20 → 4522.60] Also to Brake master Cylinder.
[4522.70 → 4523.58] Those beats are banging.
[4524.10 → 4524.38] All right.
[4524.42 → 4524.66] That's it.
[4524.70 → 4525.22] This show's done.
[4525.32 → 4526.12] Thank you for tuning in.
[4526.36 → 4527.80] We will see you on Monday.
[4532.52 → 4562.50] We will see you on Monday.
[4562.52 → 4592.50] We will see you on Monday.
