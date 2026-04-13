[0.00 → 21.18] Welcome to Changelog and friends, a weekly talk show about listening to your grandma.
[21.54 → 27.84] Thanks as always to our partners at fly.io, the public cloud built for developers who ship.
[27.84 → 33.92] We love to fly. You might too. Check them out at fly.io. Okay, let's play.
[38.12 → 43.84] Well, friends, agentic Postgres is here, and it's from our friends over at Tiger Data.
[44.06 → 48.60] This is the very first database built for agents, and it's built to let you build faster.
[49.02 → 53.54] You know, a fun side note is 80% of cloud was built with AI.
[53.54 → 57.58] Over a year ago, 25% of Google's code was AI generated.
[57.84 → 60.94] It's safe to say that now it's probably close to 100%.
[60.94 → 66.06] Most people I talk to, most developers I talk to right now, almost all their code is being generated.
[66.38 → 67.86] That's a different world. Here's the deal.
[68.12 → 71.34] Agents are the new developers. They don't click. They don't scroll.
[71.64 → 73.88] They call. They retrieve. They parallelize.
[74.18 → 77.38] They plug in your infrastructure to places you need it to perform.
[77.38 → 82.88] But your database is probably still thinking about humans only because that's kind of where Postgres is at.
[83.14 → 89.72] Tiger Data's philosophy is that when your agents need to spin up sandboxes, run migrations, query huge volumes of vector and text data,
[89.86 → 93.28] well, normal Postgres, it might choke. And so they fixed that.
[93.50 → 94.58] Here's where we're at right now.
[94.78 → 97.52] Agents Postgres delivers these three big leaps.
[97.66 → 106.06] Native search and retrieval, instant zero copy forks, and MCP server plus your CLI plus a cool free tier.
[106.06 → 112.68] Now, if this is intriguing at all, head over to tigerdata.com, install the CLI, just three commands,
[113.12 → 119.74] spin up an Agents Postgres service, and let your agents work at the speed they expect, not the speed of the old way.
[119.96 → 127.78] The new way, Agents Postgres, it's built for agents, is designed to elevate your developer experience and build the next big thing.
[128.10 → 131.02] Again, go to tigerdata.com to learn more.
[136.06 → 143.50] We can listen to Changelog and Friends with Adam and Jerry and people you know.
[143.90 → 148.04] Changelog and Friends, it's your favourite ever show.
[148.04 → 159.68] Welcome once again to Pound Define, our game shows all about fake, obscure, jargon, definitions, tomfoolery,
[159.94 → 163.34] and people who generally know way too much about words.
[164.12 → 165.54] Also, Adam and I are here.
[165.86 → 167.06] Yeah, I'm here today, again.
[167.44 → 169.32] We are joined by our champions.
[169.32 → 176.92] This is going to be, I was going to say a Duke Nuke because that's on my mind, but I was, what's the name of that game where they all punch each other?
[177.04 → 179.68] Oh, Rock'em Sock'em Robots of Pound Define.
[180.04 → 184.78] Because everybody here, except for Adam and me, have actually won the game.
[184.84 → 188.08] We try to get all of our Pound Define champs, but of course, scheduling is hard.
[188.08 → 203.40] And so, Lost and Carol couldn't make it, but we are joined today by our previous winners, starting with the person who won most recent, no, not first, because that was Lost, but first right after him, it's Taylor Troy.
[203.52 → 203.90] What's up, Taylor?
[203.90 → 204.44] First right after him.
[204.54 → 204.76] Second.
[205.24 → 205.64] You know?
[205.70 → 206.00] Second.
[206.20 → 206.48] That's what that's.
[206.50 → 206.80] Second.
[207.10 → 207.82] Yeah, you're right.
[207.90 → 208.66] Second would work there.
[208.90 → 210.32] I lost in the first round.
[210.68 → 210.94] Yeah.
[210.98 → 211.44] How's it going?
[211.90 → 215.32] You did, but you came back, and you were victorious after that.
[215.32 → 217.96] And then did you lose to Carol after that, or did we boot you?
[218.42 → 220.36] I think I lost to Carol, and then you got tired of me.
[220.66 → 220.94] Okay.
[221.24 → 222.22] So we're not tired of you.
[222.32 → 222.66] We're back.
[222.90 → 223.60] You're back.
[224.02 → 225.02] We've invited you back.
[225.68 → 229.02] And I'm sure you're going to give it a go.
[229.18 → 231.92] After Taylor is Thomas.
[232.54 → 233.70] Ooh, Jonathan Taylor Thomas.
[233.78 → 234.84] We should get a Jonathan here.
[234.90 → 235.60] Ooh, yeah.
[235.78 → 238.08] I have a JTT shout out from the 90s.
[238.36 → 238.94] What's up, Thomas?
[238.98 → 239.54] How are you doing, man?
[239.74 → 240.76] I'm doing well.
[240.76 → 242.26] It's good to catch up with everyone.
[242.70 → 245.74] And yeah, happy to be back here.
[245.74 → 251.54] I think it's good for all of us that Carol did not join because she destroyed me last
[251.54 → 252.08] time I played.
[252.42 → 252.84] That's right.
[253.24 → 260.08] So you're one for two in winning, which is slightly better than Taylor, but not quite
[260.08 → 261.60] as good as Matthew, who's one for one.
[261.64 → 262.14] Aren't you, Matthew?
[262.58 → 262.84] Yeah.
[262.84 → 268.32] I was going to decline this to keep my record, but I'm busy.
[268.72 → 269.52] Oh, yeah.
[269.64 → 270.36] I'm going to stay undefeated.
[270.56 → 271.82] I'm going to keep my belts.
[271.94 → 272.26] Okay.
[272.76 → 274.74] You can't keep the belt if you don't fight for the belt.
[274.78 → 276.50] You can't take away what I can't lose.
[276.76 → 277.50] That's right.
[277.64 → 281.46] Well, if you don't show up, then you actually lose by default.
[281.74 → 286.46] And so I'm glad that you're here to defend your title and to potentially take these guys'
[286.60 → 286.84] title.
[286.98 → 289.60] And lastly is our most recent winner.
[289.60 → 290.70] It's David Aja.
[290.94 → 291.84] David, welcome back.
[292.20 → 292.88] Glad to be back.
[293.20 → 293.72] What's up, David?
[293.98 → 294.82] You know, I'm chilling.
[294.96 → 295.34] I'm excited.
[295.68 → 298.52] I'm ready to earn the master's in BS.
[298.66 → 300.00] I feel like I got the BS in BS.
[300.20 → 300.90] Let's take it to the next level.
[300.90 → 301.18] Nice.
[301.44 → 301.84] Okay.
[302.38 → 303.36] Always Being.
[303.68 → 305.84] If you win a third time, we get you the PhD.
[306.22 → 307.56] The BS HD.
[307.78 → 308.64] That didn't make any sense.
[309.36 → 311.06] Adam, why are you here?
[311.12 → 311.70] No, just kidding.
[312.16 → 312.40] So.
[313.62 → 314.40] Solidarity, my friend.
[314.66 → 314.98] Solidarity.
[314.98 → 319.26] You're here because it's Changelog and Friends with Aaron and Jared.
[319.50 → 320.58] And so, of course, you are here.
[320.92 → 321.36] I have to be.
[321.88 → 327.48] And should we reveal the secret from the Changelog++ segment last time around?
[327.56 → 329.08] Do you want to get your comeuppance?
[329.62 → 330.20] What was it?
[330.26 → 330.96] What am I revealing?
[331.48 → 331.98] What did I miss?
[332.34 → 333.16] You won a round.
[333.28 → 333.90] You won, remember?
[334.54 → 338.18] After we quit playing, we had a Changelog++ special.
[338.70 → 339.48] And I won that one.
[339.62 → 341.40] You beat David and everybody else.
[341.40 → 343.40] You have to win in post shows, you know?
[343.56 → 343.74] That's right.
[343.74 → 345.74] If I'm going to win, might as well do it when no one's listening.
[346.18 → 349.24] I would describe that win as a hallucination, so.
[349.36 → 350.24] As a hallucination.
[350.94 → 356.98] Well, it's funny you say that because we are going to put a slight twist on this round in order to level the playing field.
[357.12 → 359.38] You know, Adam's a big fan of golf.
[359.94 → 360.20] Oh, yeah.
[360.28 → 362.76] In golf, there are handicaps and there's also Mulligan.
[362.76 → 375.50] And since you all are previous winners and Adam hasn't quite achieved that level yet, we're going to give him a slight handicap, which is that during this game, he can pick one round.
[375.68 → 376.76] He does not have to disclose.
[377.36 → 381.92] But for one round, he can actually use an LLM to generate his answer.
[384.00 → 385.96] And that's it.
[386.04 → 387.52] So he gets that trick up his sleeve.
[387.62 → 388.82] He can deploy it whenever he wants.
[388.84 → 389.46] He doesn't have to.
[390.08 → 391.66] And he does not have to disclose it.
[391.66 → 393.06] That way, maybe.
[393.76 → 394.20] Who knows?
[395.14 → 396.58] Maybe you'll be the champion of champions.
[396.64 → 398.20] Should I not disclose it at all?
[398.36 → 401.50] Or just not until I win the round?
[401.94 → 403.84] Well, that card is in, you know, your hand.
[404.00 → 404.64] You can play it however you want.
[404.64 → 405.30] Until you win the round.
[405.54 → 408.72] Well, if I'm leveraging an agent, there's no way I can lose.
[408.82 → 410.08] Yeah, you might still lose the round.
[410.16 → 411.26] Yeah, what are you talking about?
[411.96 → 413.10] It's not a guaranteed win.
[413.60 → 415.78] Oh, it's gonna, I mean, have you seen my agents?
[417.24 → 418.66] Well, then why don't you have wins already?
[419.04 → 420.58] Well, because I don't use the agents there, buddy.
[420.68 → 421.08] That's why.
[421.08 → 422.80] I'm using my own brain, which is stupid.
[423.24 → 424.62] I use their brain, which is very smart.
[425.24 → 427.22] All the smarts there, all the stupid here.
[427.62 → 429.42] We have a no Google policy.
[429.56 → 431.44] We have a no agent policy.
[431.56 → 435.68] Of course, don't look up the definitions because that wouldn't be very fun at all.
[435.76 → 438.72] The way this game works is that we have 10 rounds of play.
[438.72 → 442.94] We're playing to 12 points, whichever one comes first.
[442.94 → 449.28] And each round presents a word, which is obscure, hopefully.
[449.78 → 450.82] Hopefully nobody knows it.
[450.88 → 451.46] Maybe you know it.
[452.08 → 455.08] That is in the world of STEM-y things.
[455.22 → 457.70] So it could be science, medicine.
[458.06 → 458.98] It could be math.
[458.98 → 460.48] It could be music.
[460.74 → 462.20] It could be science fiction.
[462.20 → 464.14] It could be computer science, et cetera.
[464.84 → 466.76] They're just in that wheelhouse of science-y things.
[467.62 → 469.90] And a definition of the obscure word.
[470.12 → 476.98] Now, after I name the word, everybody submits to me their definitions of what they think the word means.
[476.98 → 484.86] Or if they don't know what it means, they make one up in order to fool their enemies into selecting it.
[484.90 → 490.22] After the definitions are submitted, I will read them all, hopefully without laughing.
[490.74 → 494.64] And then you all go around and try to guess which one is the correct definition.
[494.76 → 500.00] Now, if you get the right definition initially, right away, you get three points, and you set the round out.
[500.00 → 507.42] If you have the wrong definition, but other people pick yours, you get one point for each person who picks your definition.
[508.08 → 515.08] And then at the end of the round, if you happened upon the correct definition during the selection process, you get two points.
[515.14 → 516.32] So three, two, and one.
[516.84 → 523.78] If nobody selects the correct definition in a round, I, your humble host, get four points.
[523.78 → 529.68] And the first one of the 12 wins or the person with the most points after all 10 rounds.
[529.82 → 537.60] I doubt we're going to have to do all 10 to get to 12 because David scored 12 in like 37 seconds last time.
[537.68 → 540.66] So any questions before we get into round one?
[541.74 → 543.48] No, let's get excited to get started.
[544.22 → 546.40] All right, here we go.
[546.40 → 550.92] Your word for round one is iatrogenic.
[550.92 → 553.16] Iatrogenic.
[554.00 → 558.16] I-A-T-R-A-G-E-N-I-C.
[558.86 → 559.54] Iatrogenic.
[559.88 → 564.80] Please submit to me your definitions for iatrogenic now.
[577.80 → 579.12] Is there a problem, Taylor?
[579.12 → 580.96] I know this one.
[581.32 → 582.12] I'm just trying to...
[583.56 → 584.98] It's so close.
[586.24 → 598.42] Now, Jared, have you considered using a text-to-speech solution for reading these definitions out loud to avoid the laughter problem?
[598.82 → 599.40] The metagame?
[599.60 → 600.76] That's a perfect idea.
[601.26 → 603.26] I just feel like I would be really bored.
[603.76 → 604.08] Yeah.
[604.26 → 604.68] I don't know what to do.
[604.90 → 605.40] I'd feel...
[605.40 → 605.48] Yeah.
[606.52 → 608.52] You don't want AI taking your job.
[608.52 → 609.34] That's right.
[609.94 → 610.58] Fight for it.
[610.98 → 611.80] I'm going to keep fighting.
[623.18 → 626.46] All right, all definitions are in for iatrogenic.
[626.58 → 630.80] And I will say right up front that Taylor has the correct definition.
[631.10 → 632.20] So three points for Taylor.
[632.32 → 632.76] Mm-mm.
[632.76 → 634.78] And you can just relax, my friend.
[634.90 → 635.34] Good job.
[635.70 → 636.48] He did know it.
[636.58 → 637.26] He really knew it.
[637.98 → 644.74] So there are one, two, three, four, five possible definitions for iatrogenic.
[644.74 → 647.30] Number one.
[647.30 → 653.36] Iatrogenic describes natural springs which produce water with high concentrations of ionic water.
[654.36 → 655.24] Number two.
[655.36 → 660.74] Iatrogenic caused inadvertently by medical treatment or diagnosis.
[661.20 → 662.74] Number three.
[662.88 → 666.18] An object solely composed of distinct dissimilar parts.
[667.08 → 667.58] Number four.
[667.66 → 672.16] Describing cells in the endocrine system responsible for producing hormones.
[672.16 → 673.88] And number five.
[673.94 → 676.82] The process of swapping out one gene pool for another.
[677.46 → 678.38] There you have it.
[678.64 → 682.26] Five potential definitions for iatrogenic.
[682.72 → 687.36] We start, since Taylor is resting, we start with Thomas.
[687.36 → 687.92] Yeah.
[688.06 → 695.38] So looking at this list, we have the water ones, natural springs with ionic water.
[695.54 → 695.76] Okay.
[696.34 → 697.20] So like genic.
[697.30 → 698.36] I think about iatrogenic.
[699.48 → 703.76] Genic being like a degenerate.
[703.94 → 704.96] I know that much.
[705.74 → 710.18] Caused inadvertently by a medical operation was number two.
[710.18 → 718.80] A combination of distinct dissimilar parts, cells in the endocrine system, and then gene pool swapping.
[720.44 → 722.12] Well, yeah.
[722.28 → 722.72] Thank you.
[722.90 → 723.72] Thank you.
[723.80 → 725.72] Because normally people are like, what's number three again?
[726.88 → 727.52] Okay.
[728.58 → 733.06] What really sticks out to me is the caused inadvertently.
[733.80 → 736.50] So number two is what I'm going to go with.
[736.84 → 737.28] All right.
[737.38 → 740.00] Thomas goes with number two.
[740.20 → 740.96] How about Matthew?
[741.88 → 744.94] Because you said something, I want you to repeat number three, actually.
[745.38 → 745.74] Okay.
[745.74 → 750.86] Number three is an object solely composed of distinct dissimilar parts, you jerk.
[751.86 → 752.34] True.
[752.90 → 753.72] Is that in the definition?
[753.94 → 755.08] I don't know if it's in the definition.
[755.26 → 755.56] That was for him.
[756.00 → 757.86] He's just trolling me.
[758.28 → 759.24] That was a troll.
[759.66 → 760.54] We all know what it was.
[760.54 → 764.28] Dissimilar parts, water, water repeated water twice, actually.
[764.98 → 765.92] So that was interesting.
[767.78 → 768.94] The gene pool one.
[768.94 → 769.56] Number one.
[769.82 → 770.00] Yeah.
[770.56 → 773.26] There was one that's not the gene pool, not the water, not the dissimilar parts.
[773.44 → 775.18] There were two other definitions that I can't remember.
[775.36 → 775.82] Oh, gosh.
[775.90 → 779.98] So number four was describing cells in the endocrine system responsible for producing hormones.
[780.48 → 780.78] Okay.
[781.58 → 782.64] That's not gene pool.
[782.90 → 783.44] It's not.
[783.92 → 787.64] Not gene pool, not dissimilar, not water, and not cells.
[787.84 → 788.70] There's that one other one.
[789.34 → 790.18] Not cells.
[790.18 → 790.58] Yeah.
[790.58 → 791.84] This is like a test for me.
[791.88 → 792.42] There's that one.
[792.64 → 793.28] This one right here.
[793.62 → 793.84] Gotcha.
[794.00 → 796.38] The process of swapping out one gene pool for another?
[797.18 → 797.84] No, we said that one.
[798.16 → 798.44] Okay.
[798.58 → 800.66] Caused inadvertently by medical treatment or diagnosis?
[801.00 → 801.76] Yeah, I'm going to lock that one in.
[802.34 → 802.94] That's the one?
[803.24 → 803.44] Yep.
[803.56 → 804.44] So you're going to pile on.
[805.14 → 805.96] Yeah, pile on.
[806.68 → 812.28] I admittedly, I didn't catch which one Thomas picked.
[812.50 → 813.76] So yeah, it's a pile on.
[814.08 → 815.46] So it's an accidental pile on.
[815.54 → 815.72] Fair.
[816.22 → 816.56] All right.
[816.58 → 817.12] We go to David.
[817.12 → 817.20] David.
[817.62 → 820.06] I'm going to construct an additional pile on.
[821.16 → 822.82] This guy doesn't just pile on.
[822.96 → 824.36] He constructs pylons.
[825.00 → 825.78] All right.
[826.36 → 827.40] Now I'm scared.
[827.40 → 834.10] We're going to pile on number two, and we go to Adam, who's the last one to actually guess.
[834.44 → 836.02] What's the second to last one, Jared?
[837.40 → 838.34] That would be the fourth.
[839.06 → 839.36] Yes.
[839.40 → 840.24] Can you read that one, please?
[840.74 → 845.54] Describing cells in the endocrine system responsible for producing hormones.
[846.10 → 846.86] Yeah, that's the one.
[847.06 → 847.90] That's the one right there.
[848.00 → 848.92] Let's dial that one in.
[849.18 → 849.32] Yeah.
[849.36 → 849.82] Lock it.
[849.82 → 851.04] Let's dial that one in.
[851.34 → 852.28] Let's lock that one.
[852.68 → 854.34] No breakfast ball required, Phyllis.
[855.12 → 855.62] All right.
[855.68 → 859.68] Well, after round one, of course, Taylor gets the default three.
[860.36 → 863.02] So Taylor, what's the correct answer, Taylor?
[863.50 → 867.66] The correct answer is the medical one.
[867.66 → 872.72] And the only reason I know it is from a Nassim Taleb book.
[872.82 → 875.44] I can't remember which one, but he loves that word.
[876.78 → 877.18] Really?
[877.90 → 879.12] Fooled by randomness.
[879.98 → 881.20] I don't remember.
[881.48 → 883.40] I haven't read one of his first 10 years or something.
[884.12 → 885.04] Anti-fragile.
[885.10 → 885.54] Is that him?
[886.10 → 887.00] That's definitely him.
[887.22 → 888.76] That sounds like something that would happen in there.
[888.82 → 893.68] Cause like maybe you go in for an appointment, and then you get misdiagnosed, and then you're
[893.68 → 894.50] stronger afterwards.
[894.60 → 895.38] No, that doesn't make sense.
[895.44 → 895.80] I don't know.
[895.80 → 897.82] Yes, that is correct.
[897.86 → 899.84] Definition for iatrogenic.
[900.20 → 904.32] It's when something's caused inadvertently by medical treatment or diagnosis.
[906.10 → 910.50] Taylor's definition was, has the opposite intended effect as in hospitals, killing healthy
[910.50 → 911.00] patients.
[911.96 → 912.86] Very good.
[912.86 → 917.46] So Thomas, Matthew and David each correctly got that.
[917.52 → 919.74] So they each get two points, Thomas, Matthew and David.
[919.86 → 921.54] And then Adam, he did not pile on.
[921.64 → 925.62] He went for describing cells in the endocrine system responsible.
[925.80 → 926.34] Producing hormones.
[926.48 → 927.66] That was David's.
[927.76 → 929.06] So an additional point.
[929.36 → 930.32] Good job, David.
[930.58 → 931.36] Good job, David.
[931.64 → 933.22] Come out the gate with 12 right away.
[933.60 → 934.40] He's coming out.
[934.46 → 935.02] He's on pace.
[935.84 → 937.08] He's on pace once again.
[937.08 → 938.90] And successful round one.
[938.96 → 941.20] We have Taylor and David with three.
[941.40 → 943.12] Thomas and Matthew with two.
[943.34 → 945.38] And your humble hosts with zero.
[946.64 → 949.28] Moving to round two.
[949.64 → 956.06] In round two, your word is heteroscedasticity.
[956.56 → 963.96] It's spelled H-E-T-E-R-O-S-C-E-D-A-S-T-I-C-I-T-Y.
[964.40 → 965.50] I will put that in chat.
[965.74 → 966.60] Yeah, you need to put that in chat.
[966.68 → 967.66] I'll say it one more time.
[967.80 → 970.12] It's heteroscedasticity.
[970.38 → 971.16] There we go.
[972.82 → 973.30] Heteroscedasticity.
[974.02 → 974.68] That's tough.
[974.68 → 992.04] Matthew, is the Oxide t-shirt embroidered?
[992.78 → 993.74] Yeah, this one is.
[995.26 → 996.38] Yeah, this one is.
[996.66 → 997.14] Quality.
[998.04 → 999.76] Quality from end to end.
[999.86 → 1000.94] That's not iron on.
[1001.76 → 1003.16] It's embroidered.
[1003.62 → 1004.06] Wow.
[1004.68 → 1006.34] I grabbed a couple of t-shirts while I was there.
[1006.58 → 1007.06] And they were.
[1007.32 → 1008.24] I grabbed XLs.
[1008.68 → 1009.52] Went back to the hotel.
[1009.64 → 1010.80] I'm like, ah, these are too big.
[1010.92 → 1012.30] I went and swapped them for larges.
[1012.72 → 1013.22] Got home.
[1013.30 → 1014.52] I'm like, ah, these are too small.
[1015.58 → 1016.74] I don't know what to do.
[1016.90 → 1017.86] I wear them while I work out.
[1017.96 → 1018.94] It makes me look buff, you know?
[1019.72 → 1021.62] I love the Zero Axe Engineer one.
[1021.78 → 1022.14] So cool.
[1022.68 → 1023.38] Yeah, I want to go in.
[1023.38 → 1024.62] So we're in the faucet somewhere.
[1025.30 → 1027.18] Just me and Matthew have that problem with our arms.
[1027.26 → 1029.66] We just can't fit everything in, you know, our guns.
[1029.66 → 1030.48] The pipes.
[1030.88 → 1031.42] Can't you tell?
[1031.52 → 1032.52] They're pretty much the same size.
[1032.52 → 1035.68] Have you considered working on anything other than the biceps?
[1035.98 → 1036.66] I hear that helps.
[1037.68 → 1038.60] I considered it.
[1039.10 → 1040.28] He'll keep it under advisement.
[1040.94 → 1047.06] So Adam, when you do decide to deploy your LLM-based answer, which language model are you going to use?
[1047.06 → 1050.36] Oh, gosh.
[1051.66 → 1052.52] Great question.
[1053.72 → 1054.44] I don't know.
[1054.60 → 1054.94] Honestly.
[1055.26 → 1055.58] I don't know.
[1056.72 → 1057.34] I don't know.
[1057.92 → 1058.26] Okay.
[1058.72 → 1059.28] I just don't know.
[1059.78 → 1066.66] There's a Mac app called, like, Chorus that, like, makes it easy for you to just fire the same question to a bunch of them at once.
[1066.66 → 1067.10] Oh, really?
[1067.76 → 1076.32] Which, when I have things where it's like I don't actually care which model, I just want to try several at once, that's often kind of helpful.
[1076.80 → 1077.20] Mm-hmm.
[1077.70 → 1079.14] That's pretty much what I do manually.
[1079.26 → 1081.64] I just, like, copy-paste it into, like, three different prompts.
[1082.72 → 1085.32] So that was really something I might give a shot, you know?
[1085.32 → 1090.32] I really like to go scorched earth and just, you know, maximize my compute on this particular...
[1090.32 → 1091.80] Literally scorched the earth.
[1093.48 → 1096.48] How could I maximize my carbon footprint?
[1096.48 → 1097.36] I was looking away.
[1097.44 → 1098.10] Was that you, David?
[1098.16 → 1099.48] Was that your voice I heard saying that?
[1099.82 → 1101.12] Who was that that said this tool?
[1101.34 → 1101.78] Was it David?
[1101.98 → 1102.00] Yeah.
[1102.26 → 1102.58] Chorus?
[1102.70 → 1103.30] That was David, yeah.
[1103.62 → 1106.74] It's called Chorus, like you're a chorus of people.
[1106.96 → 1107.18] Is that right?
[1107.18 → 1108.38] Like a collection of people singing.
[1108.90 → 1110.08] Is that Chorus.ai?
[1110.50 → 1112.04] I do not remember the domain.
[1112.26 → 1113.60] I think if you just...
[1113.60 → 1114.78] Let me...
[1114.78 → 1117.44] If you just ask all your LMs, we want to point you to the right place.
[1117.46 → 1121.02] Yeah, I found a couple of choruses that are not that, and I'm trying to find that.
[1121.98 → 1123.04] Chorus.sh.
[1124.34 → 1125.90] Oh, they don't want you talking about it.
[1125.90 → 1126.72] Chorus.sh.
[1127.38 → 1128.44] That's not what that means, Jared.
[1129.06 → 1129.62] Chorus....
[1129.62 → 1130.16] And what does it mean?
[1130.26 → 1130.48] Shell?
[1131.24 → 1132.96] Yeah, it's like a .sh file.
[1133.44 → 1133.76] Script.
[1134.34 → 1135.48] That's why they made the TLD?
[1135.62 → 1136.40] Was for shell scripts?
[1137.68 → 1138.34] I don't know.
[1138.42 → 1139.52] That's how they're...
[1139.52 → 1140.10] I don't think so.
[1140.22 → 1140.52] I don't buy it.
[1140.52 → 1142.08] Well, sure.
[1142.56 → 1144.18] It's probably for Kazakhstan.
[1144.88 → 1145.24] Yeah.
[1146.80 → 1147.12] Kazakhstan.
[1148.00 → 1149.70] Or it could be Shazam.
[1149.80 → 1151.92] It could be Shaw's favourite movie about himself.
[1153.84 → 1155.54] He can afford TLD, I think.
[1155.80 → 1156.40] Anybody can.
[1156.94 → 1160.16] Well, whoever did this website for Chorus is just...
[1160.16 → 1160.84] I like it.
[1161.18 → 1161.96] Did a great job.
[1161.96 → 1167.36] Adam, if you're looking for advice on LLMs, you should pick up a vintage.
[1167.74 → 1170.08] Go for like GPT 2.5.
[1170.88 → 1171.88] It's a nice vintage.
[1172.78 → 1173.92] It's got a good...
[1173.92 → 1175.06] Good taste.
[1175.56 → 1176.26] What year is that?
[1176.70 → 1180.02] It's like a 2021 vintage.
[1180.02 → 1184.54] You might be correct.
[1190.80 → 1191.38] All right.
[1191.42 → 1195.86] I have five definitions for heteroscedasticity.
[1196.68 → 1197.84] Or however you say it.
[1197.86 → 1199.00] You're getting better at it, though.
[1199.48 → 1200.62] The practice is paying off.
[1201.06 → 1201.80] I feel like it.
[1202.04 → 1202.32] Good.
[1202.72 → 1205.36] And by five, I mean five, not six.
[1205.36 → 1208.14] Because one of us got it 100% correct.
[1208.14 → 1210.92] And that person is Mr. David Aja.
[1211.18 → 1211.62] Three points.
[1211.62 → 1211.92] Wow.
[1212.10 → 1212.28] David.
[1212.74 → 1215.82] I have to try really hard not to help you with the pronunciation.
[1216.30 → 1217.84] Oh, and he knows how to pronounce it, too.
[1219.88 → 1220.72] How am I doing?
[1221.70 → 1222.70] You got there.
[1223.10 → 1223.90] Yeah, eventually.
[1224.50 → 1226.54] I have this pronunciation guide.
[1226.68 → 1229.72] And as I try to read the actual syllables, I can't...
[1229.72 → 1230.70] It's just a lot of syllables.
[1230.84 → 1231.88] I couldn't quite put them together.
[1231.96 → 1233.26] When you just look at the words, it's not so bad.
[1233.30 → 1233.58] Anyway.
[1234.98 → 1236.02] Neither here nor there.
[1236.36 → 1237.54] Up first, this round...
[1237.54 → 1238.18] Well, let me read them.
[1238.50 → 1238.88] Gosh.
[1239.46 → 1240.76] You guys just guessed the numbers.
[1241.86 → 1242.74] Might as well.
[1242.74 → 1243.30] Okay.
[1243.48 → 1245.74] Five definitions for heteroscedasticity.
[1246.50 → 1247.56] Shoot, I'm back.
[1248.26 → 1253.52] A material that has differing shear resistance across its various dimensions.
[1253.90 → 1254.58] That's number one.
[1255.66 → 1259.18] Number two, when molecules have multiple stable configurations.
[1260.36 → 1265.52] Number three, the process of fine-tuning multidimensional data structures into a single data store.
[1265.52 → 1270.86] Number four, a collection of disjoint operators which make up the order one manifold.
[1271.60 → 1281.74] And number five, a statistical property in which some subpopulations in a collection of random variables have different variabilities from others.
[1281.74 → 1283.24] There you go.
[1283.24 → 1284.36] Five definitions.
[1284.96 → 1285.84] Heteroscedasticity.
[1286.76 → 1288.12] Let's start with Thomas.
[1288.86 → 1293.24] So the first one we have is this material with different shear...
[1293.24 → 1294.20] Yes.
[1294.20 → 1296.48] Sheer resistance across its various dimensions.
[1296.92 → 1298.22] Across various dimensions.
[1298.50 → 1298.72] Okay.
[1299.54 → 1307.10] So it makes sense that all of these do play into the prefix of the word, the hetero, right?
[1307.34 → 1309.98] Of mixing up different things together, right?
[1309.98 → 1310.20] Right.
[1310.80 → 1311.10] Right.
[1311.20 → 1315.26] Number two, you have molecules with different...
[1315.26 → 1316.00] What were the...
[1316.00 → 1318.10] Multiple stable configurations.
[1318.38 → 1318.52] Yeah.
[1318.52 → 1321.16] Multiple stable configurations.
[1322.28 → 1322.92] Okay.
[1324.06 → 1324.74] Okay.
[1324.82 → 1325.62] That makes sense.
[1326.42 → 1332.60] For three, fine-tuning for multidimensional LLMs or AI models?
[1332.60 → 1334.26] Multidimensional data structures.
[1334.54 → 1335.50] Oh, data structures.
[1336.20 → 1337.12] I'm just throwing...
[1337.12 → 1338.62] Process of fine-tuning...
[1338.62 → 1339.34] Okay.
[1339.50 → 1342.26] Multidimensional data structures into a single data store.
[1342.26 → 1349.50] You see, but I feel like this C-I-T-Y at the end is not necessarily like a process.
[1350.44 → 1354.18] So it's describing a state of something.
[1354.22 → 1354.74] It's a city.
[1355.34 → 1356.76] Yeah, but it's a city, not a state.
[1357.80 → 1359.20] I beat you to that one, Taylor.
[1359.78 → 1362.26] And then what was the collection...
[1363.14 → 1364.60] The operators?
[1365.38 → 1369.32] Yeah, a collection of disjoint operators, which make up the Order 1 manifold.
[1369.66 → 1371.08] What is the Order 1 manifold?
[1371.08 → 1371.72] Hmm.
[1372.34 → 1373.08] That's the question.
[1373.38 → 1374.46] Order dash one?
[1374.56 → 1375.40] Order minus one?
[1375.50 → 1375.82] I don't know.
[1375.90 → 1376.46] Order one?
[1377.10 → 1377.24] No.
[1377.38 → 1378.76] I just haven't heard of that before.
[1379.00 → 1379.54] It's interesting.
[1380.14 → 1381.14] Could be that one.
[1381.66 → 1389.26] You know, I do think it's the statistical variabilities within multiple data sets.
[1389.64 → 1392.02] That just kind of feels right to me.
[1392.64 → 1399.80] Hetero, you know, different, you know, mixing together and then city describing the state.
[1399.80 → 1401.70] So I'll go with number five.
[1402.42 → 1402.76] All right.
[1402.82 → 1404.10] Thomas gets five.
[1404.22 → 1404.82] We go to Matthew.
[1405.62 → 1406.92] I'm also leaning five.
[1407.88 → 1410.24] I think that makes sense.
[1410.56 → 1412.16] I don't think the stable state one makes sense.
[1412.16 → 1414.84] I don't think the Order 1 makes sense.
[1415.34 → 1416.08] What else was there?
[1416.68 → 1417.58] Sheer resistance was one.
[1417.90 → 1418.14] Fine-tuning.
[1418.58 → 1420.18] Fine-tuning of some data structure.
[1420.36 → 1420.54] Sheer resistance, yeah.
[1420.94 → 1422.90] And then what was that one I'm missing?
[1422.98 → 1425.94] It was a material having differing shear resistances.
[1426.48 → 1426.66] Yeah.
[1426.66 → 1430.26] So I have shear data structure, order manifold.
[1430.82 → 1432.24] And stable configurations.
[1432.60 → 1433.20] That's it.
[1433.70 → 1434.88] And statistical property.
[1435.48 → 1437.04] Damn, I think I'm with you on this one, Thomas.
[1438.08 → 1439.20] Another pile on.
[1439.42 → 1440.12] I pile on.
[1440.28 → 1441.52] It worked out last time.
[1441.76 → 1443.40] Please pile me on.
[1443.66 → 1444.06] Good, sir.
[1444.06 → 1447.40] Let's stack up around the normal distribution.
[1448.18 → 1450.56] This is feeling like a repeat.
[1450.80 → 1451.04] Okay.
[1451.48 → 1452.20] David's out.
[1452.48 → 1452.76] Adam.
[1453.30 → 1454.16] I'm going to pile on.
[1455.66 → 1458.04] I don't know what I'm piling on to, but whatever they chose, I'm choosing.
[1458.28 → 1458.54] That's it.
[1460.28 → 1461.42] Blind faith.
[1461.92 → 1462.90] Adam gets it.
[1463.08 → 1465.64] He's just following along like a lemma.
[1465.64 → 1466.24] I've learned.
[1466.56 → 1466.82] Okay.
[1466.92 → 1467.32] Yeah, well.
[1467.90 → 1468.98] Follow or lead.
[1469.10 → 1470.28] If you can't lead, you follow.
[1470.52 → 1470.98] I'm following.
[1471.20 → 1471.34] Okay.
[1471.56 → 1471.88] All right.
[1471.96 → 1472.18] Fair.
[1472.28 → 1473.16] Taylor, are you leading?
[1473.26 → 1473.88] Are you following?
[1474.32 → 1474.96] What are you doing?
[1475.78 → 1476.58] I'm leading.
[1476.58 → 1477.94] It's a warm pile, Taylor.
[1478.14 → 1487.24] My grandma always used to say, Taylor, homoscedasticity is sheer resistance in a single direction.
[1487.56 → 1489.38] So it must be the opposite, you know?
[1490.08 → 1492.02] Like this is a family secret.
[1492.20 → 1494.82] And I just realized that this must be the truth.
[1495.28 → 1498.20] Taylor, this was your grandmother who worked in the bomb factory.
[1498.56 → 1504.14] And she used to tell you stories about her time in the bomb factory to put you to sleep.
[1504.14 → 1504.98] And you can ask.
[1505.46 → 1505.90] Exactly.
[1505.90 → 1506.82] That same grandma.
[1507.10 → 1507.16] Yeah.
[1507.40 → 1507.66] Yeah.
[1508.06 → 1508.26] Yeah.
[1508.26 → 1508.90] That same grandma.
[1509.38 → 1511.96] He would snore just heteroscedasticity.
[1512.96 → 1514.42] When he goes to sleep.
[1515.66 → 1516.92] You almost can snore that.
[1517.06 → 1517.84] That's what you always say.
[1518.40 → 1519.00] All right.
[1519.04 → 1520.96] So you're going with the material, huh?
[1520.96 → 1524.08] The differing shear resistances because your grandma told you so.
[1524.56 → 1524.76] Yeah.
[1524.84 → 1525.02] Yeah.
[1525.50 → 1525.76] Okay.
[1525.82 → 1526.50] Just making sure.
[1527.84 → 1528.58] All right.
[1528.58 → 1534.82] So we find ourselves in similar grounds as last round, except for David has the correct answer.
[1535.04 → 1537.80] And so, David, why don't you tell everybody what the right answer is?
[1537.80 → 1543.82] I drew a little diagram because I used to love trying to draw this when I wanted to be an economics professor.
[1544.36 → 1548.30] This is a homoscedastic distribution, right?
[1548.30 → 1551.32] Where the normals are basically kind of the same.
[1551.32 → 1559.52] And then this is a heteroscedastic distribution where the variance for one subgroup is smaller than the other.
[1559.52 → 1562.44] But they're both in danger from that T. rex.
[1562.90 → 1563.10] Yeah.
[1563.16 → 1566.24] The T. rex is definitely after both distributions.
[1566.24 → 1568.32] So either way, you're going down.
[1568.78 → 1569.92] You're getting eaten no matter what.
[1570.18 → 1570.74] That's right.
[1570.74 → 1572.12] Was that a drawing of a metal pipe?
[1572.60 → 1573.58] Because it's materials, right?
[1573.92 → 1575.06] Was my grandma lying to me?
[1576.16 → 1577.60] Your grandmother.
[1577.88 → 1579.58] I can't see the different shears.
[1579.78 → 1580.28] I can't see the.
[1580.60 → 1581.28] Come on.
[1581.36 → 1583.60] That's not a drawing of the shear resistance.
[1584.02 → 1584.18] All right.
[1584.24 → 1587.64] So Taylor's grandma, I'll let him right into Matthew's lap.
[1587.88 → 1588.88] Matthew wrote that one.
[1588.98 → 1590.46] So one point for Matthew.
[1591.94 → 1595.10] And the three of you all got it correct.
[1595.10 → 1602.12] The statistical property in which some subpopulations in a collection of random variables have different variabilities from the others.
[1602.24 → 1603.50] Of course, hetero.
[1603.60 → 1604.52] Everybody knows what that means.
[1604.88 → 1612.48] The last part, the elasticity, comes from the ancient Greek word skedonimi, which means to scatter.
[1612.90 → 1613.60] So there you have it.
[1613.92 → 1615.58] Oh, it also comes from skedaddle.
[1615.82 → 1617.16] Yeah, which is when you got to run.
[1617.30 → 1617.96] Everyone scatter.
[1618.20 → 1618.46] That's right.
[1618.60 → 1620.06] They actually, that's how they got there.
[1620.08 → 1620.82] They mispronounced.
[1621.38 → 1621.86] Elasticity.
[1621.86 → 1621.92] That's right.
[1622.00 → 1624.96] And if you want everybody to run in different directions, you say, let's heteroscedaddle.
[1625.10 → 1625.96] That's right.
[1626.40 → 1627.02] All day.
[1629.98 → 1631.30] Like cockroaches.
[1631.62 → 1632.42] Heteroscedaddle.
[1632.64 → 1632.84] Okay.
[1633.92 → 1636.18] So three points for David.
[1636.70 → 1638.78] Matthew gets two plus one.
[1638.86 → 1639.58] He gets three.
[1639.92 → 1640.78] Thomas gets two.
[1640.94 → 1641.76] Adam gets two.
[1642.08 → 1644.52] Taylor locked out of this round.
[1644.62 → 1647.44] After two rounds, we have David in first with six.
[1648.04 → 1649.00] Matthew with five.
[1649.10 → 1649.84] Thomas with four.
[1649.96 → 1650.70] Taylor with three.
[1650.88 → 1652.08] Adam on the board with two.
[1652.08 → 1655.18] And I'm still sitting at zero.
[1655.42 → 1658.28] However, I'm very excited for round three.
[1659.54 → 1664.12] Because the word for round three is a Khachaturian.
[1664.80 → 1665.76] Okay, friends.
[1665.88 → 1666.58] Augment code.
[1666.70 → 1667.22] I love it.
[1667.48 → 1670.96] This is one of my daily driver AI agents to use.
[1671.30 → 1672.02] Super awesome.
[1672.72 → 1673.20] CLI.
[1673.46 → 1674.20] VS Code.
[1674.54 → 1675.16] Jet brains.
[1675.54 → 1676.50] Anywhere you want to be.
[1676.74 → 1678.08] Augment code can bring better context.
[1678.08 → 1678.68] Better context.
[1679.02 → 1679.72] Better agent.
[1680.16 → 1681.48] And of course, better code.
[1681.76 → 1686.00] To me, Augment code is by far one of the most powerful AI software development platforms
[1686.00 → 1686.70] to use out there.
[1686.82 → 1689.42] It's backed by the industry-leading context engines.
[1689.88 → 1691.50] The way they do things is so cool.
[1691.68 → 1692.32] You get your agent.
[1692.48 → 1693.08] You get your chat.
[1693.20 → 1693.98] You get your next edit.
[1694.14 → 1694.42] You get completions.
[1695.28 → 1696.02] It's in Slack.
[1696.16 → 1697.04] It's in your CLI.
[1697.22 → 1700.56] They literally have everything you want to drive the agent.
[1700.82 → 1701.88] To drive better context.
[1701.88 → 1704.78] To drive better code for your next big thing.
[1704.92 → 1706.60] For your big thing you're already working on.
[1706.60 → 1708.94] Or whatever you have in your brain you want to dream up.
[1709.24 → 1709.96] So here's a prescription.
[1710.22 → 1711.00] This is what I want you to do.
[1711.20 → 1714.00] I want you to go to augmentcode.com.
[1714.08 → 1716.78] Right in the centre, you'll see install now.
[1717.12 → 1718.26] And just go right to the command line.
[1718.52 → 1721.68] There is a terminal CLI icon there.
[1721.78 → 1722.28] Click that.
[1722.52 → 1723.50] And it's going to take you to this page.
[1723.54 → 1725.80] It says install via NPM.
[1726.40 → 1727.02] Copy that.
[1727.24 → 1728.02] Pop into your terminal.
[1728.58 → 1729.78] Install augment code.
[1730.06 → 1730.86] It's called Angie.
[1731.54 → 1733.08] Instantiate it wherever you want to.
[1733.36 → 1735.12] Type in A-U-G-G-I-E.
[1735.12 → 1736.14] And let loose.
[1736.62 → 1739.12] You now have all the power of Augment in your terminal.
[1739.40 → 1740.14] Deep context.
[1740.44 → 1741.42] Custom slash commands.
[1741.68 → 1742.56] MCP servers.
[1742.98 → 1743.78] Multi-modals.
[1744.10 → 1744.86] Prompt enhancers.
[1745.40 → 1746.64] User and repo rules.
[1746.78 → 1747.40] Task lists.
[1747.76 → 1748.36] Native tools.
[1748.54 → 1749.32] Everything you want.
[1749.66 → 1750.24] Right at your fingertips.
[1750.80 → 1752.88] Again, augmentcode.com is one of my favourites.
[1753.32 → 1753.92] You should check it out.
[1758.64 → 1759.04] Achakatura.
[1759.04 → 1759.12] Achakatura.
[1759.60 → 1760.82] Ooh, I like that one.
[1760.84 → 1761.94] Yes, you heard that right.
[1762.44 → 1762.92] Achakatura.
[1763.86 → 1768.24] A-C-C-I-A-C-C-A-T-U-R-A.
[1768.90 → 1773.10] Please submit your definitions for Achakatura now.
[1773.10 → 1796.86] Do we know if you're pronouncing that correctly?
[1797.40 → 1802.02] That's the way the person on YouTube said it when I looked up how to pronounce that word.
[1802.46 → 1804.98] Now, they could have been wrong because I did not go for multiple sources.
[1805.36 → 1807.54] This is like a play on açai.
[1807.74 → 1808.42] That's what this is.
[1808.52 → 1809.48] This is like açai.
[1809.48 → 1809.92] Achakatura.
[1809.92 → 1813.00] Just a little, yeah, just a few more letters on that one.
[1813.30 → 1813.74] All right?
[1814.22 → 1814.88] Just a few.
[1815.26 → 1817.28] The double C-C's.
[1817.54 → 1818.92] That's a very rare thing.
[1819.44 → 1819.80] Isn't it?
[1819.80 → 1820.52] Very rare.
[1820.98 → 1825.34] And what's weird is the first C-C's are the kWh and the second C-C's are the cut.
[1825.50 → 1826.08] Akash.
[1826.48 → 1827.52] But there's no SSS.
[1828.06 → 1831.54] It sounds so weird that now I'm going to go, you guys keep typing, I'm going to go double
[1831.54 → 1832.12] check you two.
[1832.12 → 1832.64] Yeah, check.
[1832.64 → 1833.54] Maybe get a second source.
[1833.62 → 1834.32] Maybe I'm saying it wrong.
[1835.12 → 1836.18] No, yeah, I'm saying it right.
[1836.82 → 1837.10] Okay.
[1837.48 → 1838.32] I'll stop pressuring you.
[1838.52 → 1839.04] Thank you.
[1839.04 → 1839.52] Yeah.
[1839.94 → 1842.06] I was questioning a lot of things in my life, so.
[1843.86 → 1845.78] I'm happily, I'm back on firm ground here.
[1846.28 → 1847.36] Country of origin?
[1847.98 → 1849.04] Use it in a sentence?
[1850.14 → 1850.54] Yes.
[1851.44 → 1854.54] The sentence is, the word for round three is achakatura.
[1858.28 → 1860.52] It's not my first pound to find, Thomas.
[1860.52 → 1864.76] I'd like to buy a vowel hint thing, whatever, and get Adam's LLM.
[1864.76 → 1866.26] There are a lot of vowels in this word.
[1866.26 → 1869.04] I would like LLM from Adam to be used.
[1869.04 → 1872.70] How do we do that?
[1872.88 → 1873.94] Here, I have dollar.
[1874.34 → 1874.96] How do I pick?
[1875.08 → 1875.64] I have dollar?
[1876.00 → 1876.96] I have dollar?
[1877.18 → 1878.30] I think bribes might work.
[1878.68 → 1879.24] Only one?
[1879.50 → 1880.06] Only one?
[1880.46 → 1880.80] Yeah.
[1881.00 → 1881.68] How many tokens?
[1882.06 → 1884.56] How many tokens can I get with this duck?
[1885.34 → 1885.78] That's right.
[1886.04 → 1887.52] It might cost a bit more than that.
[1888.02 → 1890.34] Taylor, did your grandma tell you anything about this word?
[1890.34 → 1891.64] Actually, yes.
[1892.22 → 1892.94] I'm very excited.
[1894.14 → 1895.32] I'm very excited.
[1896.22 → 1901.52] Well, she led you astray with the previous word, which I will not pronounce again.
[1901.92 → 1903.34] She's not perfect, and that's okay.
[1903.96 → 1906.08] To her credit, she was not talking about hetero.
[1906.18 → 1907.10] She was talking about homo.
[1907.24 → 1909.46] So, it's an entirely different thing.
[1910.60 → 1912.04] Don't let me distract you guys.
[1912.60 → 1913.92] I know you're all working hard.
[1913.92 → 1916.44] Taylor's done, though.
[1917.04 → 1919.46] It's really easy when you cheat and just look up the definition, you know?
[1920.84 → 1922.20] It makes things go a lot faster.
[1923.34 → 1924.52] That's what my grandma always said.
[1925.28 → 1927.68] Are there any words with the mythical triple C?
[1928.20 → 1929.24] Like, in existence?
[1929.86 → 1930.06] Mm.
[1930.80 → 1931.24] Yeah, dude.
[1931.72 → 1932.26] Three Cs.
[1932.26 → 1937.52] That's a great question.
[1938.18 → 1939.32] I don't know the answer to that.
[1940.30 → 1940.88] You find anything?
[1941.70 → 1942.42] Not yet.
[1942.68 → 1942.98] No?
[1943.14 → 1944.22] I don't think it exists.
[1944.64 → 1945.90] Initial searches are not good.
[1946.26 → 1946.66] No.
[1947.60 → 1949.22] Now I'm going to my second round of searching.
[1949.78 → 1950.14] Mm-hmm.
[1950.66 → 1952.00] CC is a cubic centimetre.
[1952.94 → 1953.98] That's when they're in medical school.
[1953.98 → 1954.94] Did you learn that in Canada?
[1956.42 → 1958.42] 20 CCs of this stat.
[1958.54 → 1959.36] Oh, yeah.
[1959.74 → 1962.08] But cubic centimetre is the same as a millilitre.
[1962.26 → 1963.28] What is that?
[1963.32 → 1963.74] An American?
[1964.22 → 1965.06] An American?
[1969.78 → 1972.68] I was at a distillery once, and they...
[1972.68 → 1980.98] You know, there's the equivalence between, like, a gram of water and a cubic gram and a millilitre are the same amount of water.
[1980.98 → 1981.80] Yeah, it's...
[1981.80 → 1986.12] And then they said they measured their water in pounds, and I was just like...
[1986.12 → 1986.56] Hmm.
[1986.96 → 1988.72] I don't trust whatever's going on back there.
[1989.14 → 1989.58] Mm-hmm.
[1990.54 → 1991.98] Is that British pounds, or...?
[1991.98 → 1992.94] I think.
[1993.94 → 1994.18] Imperial...
[1994.18 → 1995.48] They are imperial pounds.
[1996.28 → 1996.80] Mm-hmm.
[1998.44 → 1998.88] Um...
[1998.88 → 2001.02] It's looking like there aren't any CCCs.
[2001.40 → 2003.16] You mean the Cs have to be next to each other, right?
[2003.68 → 2004.00] Mm-hmm.
[2004.62 → 2004.88] Yeah.
[2005.00 → 2005.12] Yeah.
[2006.24 → 2010.22] You're talking about a word that has CC next to each other three times.
[2011.38 → 2012.56] Oh, is that what you want?
[2013.12 → 2014.60] I thought you wanted three Cs in a row.
[2015.50 → 2015.84] No, no.
[2015.84 → 2017.16] I wanted three Cs in a row.
[2017.42 → 2017.98] Oh, you did.
[2018.06 → 2020.86] So I'm giving you what you want, and you can't have any.
[2021.34 → 2024.74] Thomas was trying to give you something different, which is two Cs three times.
[2024.88 → 2030.90] Is there any word in the English language that has three of the same letter next to each other?
[2031.70 → 2032.44] Of any letter?
[2032.44 → 2034.28] I think, like, Dignity, probably.
[2034.98 → 2035.88] Ooh, that's a good one.
[2036.88 → 2039.52] When we were expecting our child, I wanted to...
[2039.52 → 2041.58] I wanted to name...
[2041.58 → 2044.64] If we had a boy, I wanted to name him Aaron with three As.
[2045.04 → 2046.48] He'd be first in everything.
[2046.48 → 2047.28] Mm-hmm.
[2047.40 → 2048.48] Mm-hmm.
[2048.48 → 2049.48] Mm-hmm.
[2050.48 → 2050.98] Mm-hmm.
[2050.98 → 2053.46] Elon Musk challenges us.
[2053.46 → 2054.38] That reminds me of the...
[2054.38 → 2054.96] Or A-Ron.
[2055.22 → 2056.24] The A-A-Ron.
[2056.32 → 2057.38] Yeah, that reminds me of that sketch.
[2057.60 → 2058.46] That's a good sketch.
[2059.16 → 2061.98] Can you start their name with a null terminator?
[2062.10 → 2063.26] Like, just...
[2063.26 → 2066.76] Just terminate any string.
[2066.78 → 2067.46] Or a semicolon?
[2067.96 → 2069.10] No, the...
[2069.10 → 2071.28] What's the Greek question mark?
[2072.90 → 2073.34] Oh, awful.
[2073.34 → 2074.40] That looks like a semicolon.
[2074.58 → 2074.74] Yeah.
[2075.20 → 2075.48] Yeah.
[2076.60 → 2077.56] It's called an awful?
[2078.00 → 2079.16] No, it's called the Masuria.
[2079.64 → 2080.24] Or whatever it is.
[2080.52 → 2080.72] Yeah.
[2080.98 → 2081.70] That's the Greek question mark.
[2081.70 → 2082.48] That's the Achakatura.
[2082.84 → 2083.84] Yeah, exactly.
[2084.46 → 2085.26] Acacia cat?
[2085.72 → 2086.06] You're a...
[2086.06 → 2086.42] Acacia.
[2087.12 → 2087.70] That's a bush.
[2087.82 → 2088.26] Acacia cat, you're a...
[2101.54 → 2104.10] All right, we have everybody's except...
[2104.10 → 2104.94] Who are we missing here?
[2105.44 → 2106.02] Oh, we got them all.
[2106.20 → 2106.80] We got them all.
[2106.80 → 2107.28] It was Adams.
[2107.60 → 2107.94] He's in.
[2108.00 → 2108.36] I finally...
[2108.36 → 2110.00] My LLM finally got back to me.
[2110.08 → 2110.92] It's like, come on, man.
[2110.92 → 2112.42] You're taking way too long here, man.
[2112.58 → 2113.36] Oh, my God.
[2113.68 → 2114.30] Oh, God.
[2114.30 → 2115.64] A huge patch or something, dude.
[2115.66 → 2116.20] What are you doing?
[2116.74 → 2119.04] Hey, nobody knows what this word means.
[2119.20 → 2119.86] That's a relief.
[2119.98 → 2124.42] I went to this website called toadvanced.com, and it was just...
[2125.42 → 2128.66] They have a brand-new LLM there, and it was just too advanced.
[2128.66 → 2136.46] I appreciated how ChatGPT5 tried to answer the three Cs in a row, because it would come up
[2136.46 → 2141.44] with words with two Cs, and then it would throw a third C in there and be like, nope,
[2141.48 → 2142.30] that doesn't work.
[2142.42 → 2143.06] Nope, nope.
[2143.06 → 2144.02] Like stucco.
[2144.10 → 2145.48] It's like stucco has two Cs.
[2145.54 → 2148.52] Let me add a third C, and it's like, nope, that's not the word, stucco.
[2149.88 → 2150.28] Stucco.
[2150.80 → 2152.48] Oh, I was enjoying that back here.
[2152.74 → 2152.82] Okay.
[2153.14 → 2154.56] World's smartest five-year-old, really.
[2154.82 → 2155.02] Yeah.
[2155.86 → 2157.40] That's why it's GPT5.
[2157.50 → 2158.20] It's for five years old.
[2158.32 → 2158.48] Okay.
[2158.48 → 2162.72] Six definitions of Khachaturian.
[2164.00 → 2171.06] Number one, a brief grace note played before a principal note, then immediately released.
[2171.64 → 2176.86] Number two, the order of operations for actions that must first precede other actions before
[2176.86 → 2177.84] being executed.
[2178.46 → 2182.82] Number three, a partial eclipse of a planet formed by multiple moons.
[2183.80 → 2187.82] Number four, a fungal infection affecting the forearms.
[2188.48 → 2192.48] Number five, a genus of fungi native to South American rainforests.
[2193.30 → 2197.94] And number six, when a material has a single plane of sheer resistance.
[2202.16 → 2203.22] I tried.
[2203.38 → 2204.62] I tried really hard.
[2204.74 → 2204.90] Okay.
[2208.26 → 2210.14] Matthew, you are up first this round.
[2210.64 → 2210.96] Yes.
[2211.54 → 2212.14] Okay.
[2212.14 → 2215.32] So, a single plane of sheer resistance.
[2215.90 → 2216.20] Yes.
[2216.58 → 2217.44] Fungal arm?
[2217.44 → 2219.78] Fungal infection affecting the forearms.
[2220.10 → 2221.28] Something else about a fungus?
[2221.56 → 2224.88] A genus of fungi native to South American rainforests.
[2224.88 → 2225.24] Uh-huh.
[2225.58 → 2226.66] A partial eclipse.
[2226.90 → 2230.44] Partial eclipse, pre-note, and pre-order operations sort of thing.
[2230.44 → 2231.28] Order operations, yes.
[2231.30 → 2231.48] Okay.
[2232.32 → 2234.36] I am in between.
[2235.18 → 2237.08] I'm honestly between two here.
[2237.34 → 2241.04] Can you repeat the definitions for the pre-note one and for the arm fungus?
[2241.04 → 2241.88] Yeah.
[2241.96 → 2247.40] A brief grace note played before a principal note then immediately released was the musical
[2247.40 → 2247.74] one.
[2247.84 → 2253.10] And then the fungus one was a fungal infection affecting the forearms.
[2253.86 → 2254.26] Forearms.
[2254.60 → 2254.92] One word.
[2255.10 → 2255.38] Forearms.
[2256.36 → 2257.32] Not forearms.
[2257.48 → 2257.98] Like, you have four of them.
[2257.98 → 2258.86] What if you have two arms?
[2260.64 → 2261.96] You don't have to worry about the other one.
[2261.98 → 2263.22] That's a chukatura.
[2263.42 → 2264.54] No, I can't even come up with anything.
[2264.92 → 2269.42] Yeah, I think what's throwing me off about the fungus one is that it's specific to the
[2269.42 → 2269.82] forearm.
[2273.50 → 2275.28] That's what's throwing you off about it?
[2275.98 → 2276.30] Yeah.
[2277.42 → 2280.02] It's like, why would that classify different?
[2280.18 → 2280.56] You know what I mean?
[2280.60 → 2282.66] Like, what if it was like on my bicep or something?
[2282.72 → 2283.50] Why would that be different?
[2283.80 → 2286.14] Are there fungi that only affect the forearms?
[2286.38 → 2287.34] Different fibres, man.
[2287.70 → 2288.30] That's right, man.
[2288.30 → 2288.80] Yeah, exactly.
[2289.30 → 2290.32] It's different parts of the arm.
[2290.52 → 2290.88] Get it right.
[2290.88 → 2292.96] How much you sweat, different parts of your body.
[2293.08 → 2293.18] Yeah.
[2293.18 → 2295.46] It's like when you do a lift, and you're like, this is only working my bicep.
[2295.54 → 2297.68] And it's like, that's on my Torah.
[2298.32 → 2298.52] Yeah.
[2299.20 → 2303.14] I think I like the musical note one personally.
[2303.70 → 2305.96] So I think I'm going to lock in the musical note.
[2306.54 → 2306.96] All right.
[2307.04 → 2308.58] Matthew is on the music note.
[2309.60 → 2310.58] We go to David.
[2311.52 → 2312.66] What was the other fungus?
[2313.18 → 2313.54] Yes.
[2313.54 → 2317.34] There was the fungal infection, which we've talked about extensively.
[2317.74 → 2321.54] And then there's the genus of fungi native to South American rainforests.
[2321.54 → 2324.60] And one of these is the correct answer.
[2325.50 → 2326.72] No, that's that's right.
[2327.38 → 2328.48] Unless Jared is playing.
[2329.48 → 2331.50] Unless he's just like a joke around us.
[2331.50 → 2332.42] Just a big troll.
[2332.64 → 2333.06] Surprise.
[2333.80 → 2334.58] It's not a real word.
[2334.60 → 2335.08] So we got two funguses.
[2336.10 → 2336.90] Fake word.
[2337.38 → 2337.58] Sorry.
[2337.74 → 2339.46] I'm going to do it.
[2339.52 → 2342.42] Can I have the final three one more time?
[2342.88 → 2343.60] Final three.
[2343.78 → 2343.96] Wow.
[2344.50 → 2344.56] Yeah.
[2344.78 → 2345.54] That's going to do it.
[2345.54 → 2348.40] OK, so number four was the fungal infection affecting the forearms.
[2348.50 → 2351.58] Number five is the genus of fungi native to South American rainforests.
[2351.60 → 2354.66] And number six is when a material has a single plane of sheer resistance.
[2354.86 → 2355.00] All right.
[2355.16 → 2355.26] Right.
[2355.42 → 2358.34] But that's something you forgot about.
[2359.02 → 2359.20] Yeah.
[2359.26 → 2361.72] I just like it just it flew through me.
[2361.78 → 2363.54] It was so perceptive.
[2363.54 → 2368.74] I'm going to go for the musical term as well.
[2369.02 → 2370.46] David's going for music.
[2370.60 → 2374.20] And he has the the see a base in the background.
[2374.68 → 2375.64] He's a musician.
[2375.86 → 2378.46] So that's very suspicious.
[2378.78 → 2380.92] The musician might be starting to pick the music.
[2381.08 → 2383.40] I mean, I'm not I'm not a musician.
[2383.60 → 2389.60] I just own several instruments that he likes guitars as he showcases more instruments.
[2389.60 → 2390.04] Right.
[2390.26 → 2391.02] To further.
[2391.14 → 2391.26] Yeah.
[2391.26 → 2393.22] He moves so you can see the rest of his guitars.
[2393.76 → 2394.12] Yeah.
[2395.84 → 2397.50] How many forearms do you have?
[2397.74 → 2397.96] OK.
[2398.28 → 2400.16] I play all of them simultaneously.
[2400.62 → 2400.94] Taylor.
[2401.18 → 2402.02] What are you thinking?
[2402.32 → 2404.74] You're going to pile on with these guys, or you're going to go fungal?
[2404.88 → 2407.34] You're going to go somewhere else altogether.
[2407.56 → 2408.12] Sheer resistance.
[2408.96 → 2409.58] No, I don't.
[2409.90 → 2411.26] My grandma led me astray.
[2411.40 → 2415.20] I'm not I'm not falling prey to the sheer resistance once again.
[2416.06 → 2417.80] He's resisting sheer resistance.
[2417.80 → 2427.12] Yeah, she actually my grandma told me that a Chukatura is an eclipse, but I'm not I'm not trusting her.
[2427.16 → 2429.96] So I'm going to go for the grace note and pile on.
[2430.34 → 2430.92] All right.
[2430.98 → 2432.16] He's pile on the grace note.
[2432.98 → 2433.76] Oh, boy.
[2434.36 → 2435.94] We go now to Thomas.
[2436.36 → 2445.36] OK, so grace note has a pile on and the order of operation for actions doesn't have any love.
[2445.36 → 2447.50] Partial eclipse with multiple moons.
[2448.44 → 2452.04] That looks like I'm trying to imagine what that would look like.
[2452.10 → 2453.56] That would be pretty cool to see.
[2454.18 → 2456.04] But I don't see how that's a check.
[2456.22 → 2456.56] Turn.
[2456.82 → 2457.76] Have you seen Star Wars?
[2458.36 → 2459.66] Have I seen Star Wars?
[2459.72 → 2459.98] Yes.
[2460.50 → 2461.38] Yeah, it's like that.
[2461.70 → 2464.02] That's multiple suns.
[2464.52 → 2467.56] Dude, you didn't you didn't watch the end credit, the end credit scene.
[2467.56 → 2472.00] The end credits is all multiple moons.
[2472.82 → 2473.14] Yeah.
[2473.26 → 2473.82] Moon fest.
[2474.30 → 2475.58] It's not just multiple moons.
[2475.68 → 2476.72] It's partially cliffs.
[2476.90 → 2479.90] It's a partial eclipse of multiple moons.
[2480.06 → 2480.54] Right.
[2481.08 → 2481.46] Yes.
[2481.52 → 2482.44] A rare occurrence.
[2482.70 → 2484.30] We have fungal in the forearms.
[2484.72 → 2487.30] So I could be like ringworm different places.
[2488.14 → 2489.36] Rumble in the jungle.
[2489.54 → 2490.88] Fungal in the forearms.
[2491.02 → 2491.26] Yeah.
[2491.30 → 2492.54] Fungal in the forearms.
[2492.54 → 2497.26] But there's some like fungus feeling thing about a Shakira.
[2497.62 → 2503.30] And I'm going to go with number five, the genus of fungi native to South America.
[2503.40 → 2504.02] All right.
[2504.18 → 2509.26] So we have Thomas on the South American rainforest fungi.
[2509.48 → 2509.90] Yeah.
[2509.98 → 2511.32] All alone on my little island.
[2511.88 → 2512.84] No man is an island.
[2513.78 → 2515.90] I don't remember the rest of the poem, but no.
[2516.54 → 2517.40] It's a poem.
[2517.86 → 2518.62] It's a book.
[2519.18 → 2519.62] No.
[2519.62 → 2523.04] Well, it's a poem and it's a book.
[2523.16 → 2523.48] Whoa.
[2523.48 → 2524.38] It's a book by Thomas.
[2525.10 → 2526.18] It's a crazy book.
[2526.20 → 2527.48] This guy's pulling out books, man.
[2527.58 → 2528.10] That's what they are.
[2528.54 → 2529.88] Thomas reads, dude.
[2529.94 → 2530.56] I read these.
[2530.56 → 2532.12] He's a book that says no man is an island.
[2532.86 → 2533.94] He just books checked you.
[2534.04 → 2535.58] You should read some Thomas Merton.
[2535.82 → 2536.52] That would be the plug.
[2536.92 → 2537.60] That's awesome.
[2538.00 → 2538.62] I love that.
[2539.02 → 2540.06] Adam, what are you thinking, man?
[2540.82 → 2544.80] Mom always told me if I get a chance to pile on, to pile on.
[2544.80 → 2545.56] So I'm going to pile on.
[2545.56 → 2551.04] I'm just listening to grandparents and mamas, okay?
[2551.42 → 2552.80] He's just following the crowd here.
[2552.84 → 2554.74] Mama always said it was a good pile on.
[2555.18 → 2555.66] Pile on.
[2555.88 → 2556.36] Crowds.
[2556.58 → 2556.88] All right.
[2556.92 → 2557.98] Let's start right there.
[2558.64 → 2563.84] A Khachaturian is a brief grace note played before a principal note, then immediately released.
[2564.30 → 2565.60] I think it's an Italian word.
[2565.60 → 2569.80] So Matthew, David, Taylor, and Adam each get two points.
[2570.40 → 2573.08] Matthew, David, Taylor, Adam.
[2573.32 → 2577.36] And Thomas guessed a genus of fungi native of South American rainforest.
[2577.66 → 2579.00] That was Matthew.
[2579.26 → 2579.80] So he gets a bone.
[2579.86 → 2580.94] Oh, good job, Matthew.
[2581.02 → 2582.30] We both had fungus on the mind.
[2583.18 → 2583.76] Oh, perfect.
[2583.90 → 2586.02] I was wondering who else did the fungus one.
[2586.56 → 2590.18] I really liked a fungal infection affecting the forearms.
[2590.18 → 2598.18] However, it had this certain like role to the sentence where I thought that can't be a real thing because it just sounds so a fungal affection affecting the forearms.
[2598.26 → 2600.28] Like it's almost, it's almost alliterative.
[2600.44 → 2601.16] Like it's poetic.
[2602.30 → 2604.22] That's what got me with the water one last time.
[2604.26 → 2605.46] I was like, they said water twice.
[2605.62 → 2606.52] Which was mine.
[2606.52 → 2607.78] That was also Thomas's.
[2608.10 → 2609.70] So he's on to you, dude.
[2609.76 → 2610.68] I'm on to you, Thomas.
[2610.88 → 2612.82] Honestly, I've been reading too much.
[2613.64 → 2614.28] That's my point.
[2614.28 → 2615.28] You read too much.
[2616.18 → 2618.10] He just takes the bookshelf and tears it down.
[2618.12 → 2620.00] Come down here with us plebs, you know?
[2620.00 → 2621.80] I did just see Hamlet.
[2622.50 → 2626.26] I saw Hamlet last week and maybe that's all getting in my head.
[2626.78 → 2627.58] Maybe it is.
[2627.84 → 2629.24] Did he have a forearm infection?
[2629.88 → 2631.14] No, but it's Shakespeare.
[2634.04 → 2634.48] Thanks.
[2634.80 → 2636.06] Now he's educating us plebs.
[2636.16 → 2637.10] He's like, that's Shakespeare.
[2637.28 → 2637.84] He didn't know.
[2638.76 → 2640.90] That's the only author that I know.
[2641.18 → 2641.30] Okay.
[2641.46 → 2642.26] That's the only author.
[2642.62 → 2642.94] Yeah.
[2643.26 → 2644.72] Shakespeare and I don't know.
[2645.16 → 2645.60] Yep.
[2645.60 → 2645.92] That's it.
[2645.96 → 2646.66] I can't think of another one.
[2646.78 → 2647.06] Here we go.
[2647.24 → 2647.34] All right.
[2647.46 → 2647.82] All right.
[2648.06 → 2648.76] Round four.
[2648.76 → 2650.98] Well, let's, let's total up the points here.
[2651.04 → 2654.48] After three rounds, David and Matthew tied with eight.
[2654.56 → 2655.42] It's a battle guy.
[2656.14 → 2656.96] Taylor with five.
[2657.06 → 2658.76] Thomas and Adam tied at four.
[2659.14 → 2660.02] And Jared with.
[2660.22 → 2661.58] And I'm still shut out.
[2661.70 → 2665.68] We guys keep piling on, which usually helps me because if you pile on to the wrong answer,
[2665.76 → 2666.16] I win.
[2666.22 → 2667.70] But you're piling on to the right answer.
[2668.06 → 2668.60] I lose.
[2669.10 → 2670.56] You invited us champions here.
[2670.86 → 2671.30] It's true.
[2671.30 → 2673.22] I should expect the best.
[2673.32 → 2674.20] And you guys are giving it to me.
[2674.26 → 2674.48] Okay.
[2675.42 → 2676.02] Round four.
[2676.16 → 2676.74] Give it a Good.
[2677.10 → 2677.70] Oh yes.
[2677.76 → 2684.18] This is our give it a Goo ground in which I open up an incognito tab and I don't change
[2684.18 → 2684.88] my IP address.
[2685.02 → 2687.98] So yes, you can go ahead and judge us Nebraskans.
[2687.98 → 2693.94] As I start to type a phrase into Google, and then I stop and let it autocomplete.
[2694.94 → 2699.32] I then write down the top autocomplete answer from Google.com.
[2699.32 → 2707.46] When an incognito tab in Nebraska types Steve Jobs space, Steve Jobs.
[2707.66 → 2708.84] Then I stopped.
[2709.36 → 2710.94] Then I got some suggestions.
[2711.22 → 2720.30] Your chore is to write down what you think a believable suggestion would be the top one
[2720.30 → 2722.38] and send it to me whenever you're ready.
[2723.66 → 2725.54] So just his name and then space.
[2726.22 → 2726.76] That's right.
[2726.76 → 2729.80] His name, Steve space jobs space.
[2730.90 → 2734.94] What do you think Google would expect me to type next?
[2747.10 → 2749.58] Oh, these are coming in hot and heavy.
[2751.44 → 2753.42] These are good.
[2754.36 → 2755.48] These are good.
[2755.48 → 2759.82] Just to clarify, would Steve Jobs space needle be a good answer?
[2762.82 → 2763.96] You could try it.
[2764.06 → 2764.24] Yeah.
[2764.80 → 2765.16] Okay.
[2765.46 → 2766.16] It wouldn't stop you.
[2766.64 → 2767.70] Is that a clarification?
[2767.70 → 2772.70] I'm leaving the space up to interpretation.
[2772.70 → 2772.76] Yeah, that one too.
[2774.38 → 2776.18] Thomas has a Steve Jobs book.
[2776.54 → 2778.12] Thomas has a Steve Jobs book.
[2778.78 → 2786.66] I want you to, your mission, should you choose to accept it, is every round you have to blow a book that somehow relates.
[2786.88 → 2787.02] Okay?
[2788.08 → 2788.52] Okay.
[2789.18 → 2790.08] Somehow relates.
[2790.08 → 2791.08] That sounds exhausting.
[2791.08 → 2792.00] That sounds exhausting.
[2792.00 → 2792.88] It's a challenge.
[2794.30 → 2794.66] Yeah.
[2795.46 → 2798.70] It's going to be tough if we get to round six especially.
[2798.70 → 2799.70] Hmm.
[2800.38 → 2801.24] What's round six?
[2801.92 → 2803.04] I'll tell you when we get there.
[2803.04 → 2803.42] No.
[2803.58 → 2804.30] Yeah, we'll get there.
[2804.44 → 2804.78] Come on.
[2804.82 → 2805.74] No hints.
[2806.56 → 2807.34] No teasers.
[2807.86 → 2809.02] I guess that kind of was a teaser.
[2810.02 → 2810.76] Yeah, it was.
[2811.12 → 2813.82] We're waiting for Adam and Taylor.
[2814.38 → 2814.72] Hmm.
[2814.72 → 2817.76] I got to say, make files are very annoying sometimes.
[2818.10 → 2818.62] Just letting you know.
[2819.12 → 2821.20] It was a heteroscedastic book.
[2821.36 → 2821.80] There you go.
[2822.26 → 2823.30] Hey, there you go.
[2823.54 → 2824.46] A little bit of tuft.
[2825.20 → 2826.50] A little bit of tuft?
[2826.56 → 2826.98] Is that what?
[2827.26 → 2828.18] Is that not tuft?
[2828.56 → 2830.22] No, that was my nickname back in college.
[2830.64 → 2831.20] So that book.
[2832.04 → 2832.38] I didn't know.
[2832.50 → 2833.24] Yeah, I think.
[2833.24 → 2833.64] Yeah.
[2834.50 → 2834.94] Yes.
[2835.10 → 2838.24] The visual display of quantitative information.
[2839.22 → 2839.70] Well, yeah.
[2839.86 → 2841.68] I sure pitched that.
[2841.96 → 2844.14] I pitched that round into your wheelhouse, didn't I, David?
[2844.72 → 2848.06] He's like, this word exists on the front page of a book that I've read.
[2848.20 → 2849.90] And I keep near buying.
[2850.00 → 2850.98] I just need to reference it.
[2851.44 → 2853.20] Or just show off to my friends.
[2853.72 → 2853.98] Hmm.
[2854.70 → 2855.30] It's working.
[2855.86 → 2857.30] I think you're pretty cool at this point.
[2857.68 → 2858.52] Okay, everyone's in.
[2859.14 → 2859.66] All right.
[2860.00 → 2866.78] So six potential autocompletes for the search Steve Jobs blank.
[2867.34 → 2868.40] Steve Jobs what?
[2869.08 → 2870.14] Google autocompletes.
[2870.20 → 2871.46] The top autocomplete.
[2871.86 → 2873.72] Here's your six potential answers.
[2873.72 → 2874.44] Answers.
[2874.78 → 2876.16] Steve Jobs net worth.
[2876.92 → 2878.06] Steve Jobs biography.
[2878.94 → 2880.54] Steve Jobs feet pics.
[2887.92 → 2890.64] That tells us all we need to know about a breastfed.
[2891.42 → 2893.22] Steve Jobs daughter.
[2894.20 → 2895.78] Steve Jobs wife.
[2896.62 → 2897.92] Steve Jobs death.
[2898.60 → 2900.10] That's six.
[2900.10 → 2903.36] This round, the person who gets to go first is David.
[2903.78 → 2906.70] These are largely depressingly plausible.
[2907.36 → 2908.28] Yeah, exactly.
[2909.24 → 2910.52] I want to go net worth.
[2911.16 → 2911.98] David goes net worth.
[2912.08 → 2912.32] Adam.
[2913.48 → 2915.44] I've been curious about his feet, honestly.
[2915.82 → 2922.32] I've been thinking like, what does his feet look like?
[2922.38 → 2922.66] You know?
[2922.70 → 2922.92] Yeah.
[2922.92 → 2924.24] I've seen him.
[2924.54 → 2925.62] Show me your feet, dude.
[2925.84 → 2926.22] Okay.
[2926.82 → 2927.94] Steve Jobs feet.
[2928.14 → 2928.26] Show me your feet.
[2930.38 → 2934.28] He did famously walk around barefoot a lot.
[2935.06 → 2937.10] You know, like maybe he's got some ganglier, you know?
[2938.02 → 2939.38] Maybe it's well manicured.
[2940.56 → 2941.74] Or a little bit of tuft.
[2942.42 → 2943.42] A little bit of tuft.
[2943.60 → 2945.36] A little bit of fungus.
[2945.36 → 2948.60] A little bit of acacia Terra.
[2948.64 → 2949.80] Yeah, I wasn't trying to say that word.
[2949.98 → 2951.26] Some tough actor into an actor.
[2951.36 → 2952.38] A chacatura?
[2952.82 → 2954.86] A chacatura on them feet, man.
[2954.94 → 2956.20] You need some acciaccatura.
[2956.84 → 2958.06] So you're going to go with feet pics or?
[2958.80 → 2959.74] Heck no, man.
[2959.74 → 2961.60] I don't think he's got his feet.
[2964.00 → 2965.80] They want to know how much money he's got.
[2966.00 → 2966.50] Oh, man.
[2966.62 → 2966.98] Okay.
[2967.12 → 2968.76] Show me the money.
[2969.18 → 2969.94] Show me the money.
[2970.18 → 2970.46] All right.
[2970.48 → 2971.90] Steve Jobs net worth.
[2972.70 → 2974.32] Next up is Taylor.
[2974.32 → 2977.22] Oh, it's for sure the Space Needle.
[2979.26 → 2980.48] It was none of them.
[2980.58 → 2982.00] Steve Jobs Space Needle.
[2982.34 → 2983.70] It's definitely Space Needle.
[2983.88 → 2984.02] Okay.
[2984.20 → 2985.46] I'll go with Daughter.
[2985.46 → 2987.40] I appreciate you doubling down on that joke.
[2988.08 → 2988.56] Daughter?
[2988.64 → 2989.66] It was a good bit.
[2990.06 → 2990.78] I had to.
[2991.36 → 2991.76] Yeah, Daughter.
[2991.84 → 2992.44] It was a good one.
[2993.02 → 2994.98] Taylor's going for Steve Jobs Daughter.
[2995.12 → 2996.44] Okay, Thomas.
[2996.90 → 2997.08] Yeah.
[2997.20 → 2997.76] Net worth.
[2998.58 → 2999.02] Biography.
[2999.36 → 3000.00] Feet pics.
[3001.32 → 3001.76] Daughter.
[3002.40 → 3003.88] Wife and death.
[3003.88 → 3003.96] Death.
[3004.20 → 3004.46] Ugh.
[3004.56 → 3004.98] That's right.
[3005.28 → 3006.98] Got to end with death as always.
[3010.04 → 3014.36] So, Daughter, she came up with a book, Small Fry, a couple of years ago.
[3015.66 → 3016.14] Really?
[3016.72 → 3017.32] Oh, yeah.
[3018.34 → 3019.24] About fast food or?
[3020.20 → 3020.40] No.
[3021.54 → 3022.02] McDonald's?
[3022.40 → 3022.56] No.
[3023.10 → 3024.10] Is she a small human?
[3024.22 → 3025.22] I don't understand Small Fry.
[3025.34 → 3025.90] What's the context?
[3025.90 → 3028.68] I don't actually know what the context is of the title.
[3028.82 → 3030.02] It was his pinky toe.
[3030.14 → 3031.04] Dad's pinky toe.
[3032.12 → 3032.70] Is that?
[3032.80 → 3033.48] That's what it was.
[3033.62 → 3037.10] And you would only know that if you looked up the feet pics, as everyone else in Nebraska
[3037.10 → 3037.68] has.
[3038.44 → 3039.32] Was it a picture book?
[3039.88 → 3041.00] It's not a picture book.
[3041.06 → 3042.40] It's a very serious book.
[3042.40 → 3044.78] It was actually the invention Dad never did.
[3044.90 → 3045.46] That's what it was.
[3045.62 → 3045.74] Yeah.
[3045.78 → 3047.24] He never invented the Small Fry.
[3047.90 → 3049.22] Do you have it on your shelf behind you?
[3049.52 → 3050.56] No, I don't, actually.
[3050.68 → 3051.68] But I do want to read it.
[3051.76 → 3055.12] It's on my list of books I want to read.
[3056.04 → 3057.52] I got too much stuff going on.
[3057.84 → 3058.26] All right.
[3058.52 → 3062.18] We got Daughter or Wife.
[3062.44 → 3064.50] You know, I'm going to go with Daughter because she wrote the book.
[3064.82 → 3071.66] I wonder if people are like Steve Jobs' daughter who wrote the book, but they won't remember her
[3071.66 → 3074.34] name because she didn't.
[3074.34 → 3078.80] She went as Lisa Brennan for a while before.
[3080.10 → 3082.00] Now she goes by Lisa Brennan Jobs.
[3083.30 → 3083.70] Okay.
[3083.80 → 3084.46] So you're going with Daughter.
[3084.82 → 3085.10] Yep.
[3086.16 → 3086.48] All right.
[3086.52 → 3088.92] Thomas has Daughter along with Taylor.
[3089.52 → 3093.06] David and Adam are on Net Worth, and Matthew is the only one who hasn't picked yet.
[3094.44 → 3095.30] What are you thinking, man?
[3097.86 → 3098.56] What is it?
[3098.88 → 3099.28] Net Worth?
[3100.16 → 3100.48] Daughter?
[3101.06 → 3101.20] Life?
[3101.20 → 3101.48] Death?
[3101.96 → 3102.70] Wife or life?
[3103.42 → 3103.78] Wife.
[3103.78 → 3104.38] Wife.
[3105.06 → 3105.62] Biography?
[3106.08 → 3106.50] Biography.
[3106.82 → 3107.32] Life.
[3108.06 → 3108.70] Is it life?
[3109.08 → 3109.34] Net Worth.
[3109.34 → 3109.72] Wife.
[3110.44 → 3111.22] Net Worth, for sure.
[3111.72 → 3112.28] You're going Net Worth?
[3112.56 → 3112.80] Yeah.
[3113.04 → 3113.58] I'm piling.
[3114.18 → 3114.70] He's piling.
[3115.04 → 3115.68] Pile on.
[3116.00 → 3117.10] We have two piles here.
[3117.20 → 3120.60] We have two piles, but which one is right?
[3121.28 → 3124.66] David, Adam, and Matthew chose Net Worth.
[3124.86 → 3125.98] Steve Jobs' Net Worth.
[3126.06 → 3127.66] Are people Google searching that?
[3128.08 → 3132.02] I don't know, but Adam created it, so he should know.
[3132.86 → 3133.22] Nice.
[3133.78 → 3134.48] Good job, Adam.
[3134.62 → 3135.46] Good job, Adam.
[3135.96 → 3137.66] One point for David and Matthew.
[3137.78 → 3141.24] You don't score any points for guessing your own, but you did convince people.
[3141.56 → 3142.04] Oh, yeah.
[3142.08 → 3143.20] I forgot I guessed my own.
[3144.92 → 3145.28] Whoops.
[3145.60 → 3148.04] No, you have to pretend like that's a strategy.
[3148.84 → 3149.84] I really just did forget.
[3150.00 → 3151.44] I was like, it's got to be Net Worth.
[3151.82 → 3151.96] Okay.
[3152.28 → 3152.88] Play it off.
[3152.98 → 3153.52] Play it off.
[3153.62 → 3154.58] It's got to be Net Worth.
[3154.58 → 3155.02] Net Worth.
[3155.02 → 3155.96] Well, fun fact.
[3156.24 → 3159.70] Net Worth was actually the third autocomplete for me, so it was right up there at the top.
[3160.96 → 3166.08] The second autocomplete for me was Death, so that was right there at the top.
[3166.22 → 3167.86] Matthew actually said Death.
[3167.86 → 3172.38] But the number one autocomplete for Steve Jobs is Steve Jobs' daughter.
[3172.86 → 3175.52] So Taylor and Thomas landed on it.
[3175.94 → 3176.56] Taylor Thomas.
[3176.72 → 3177.72] Jonathan Taylor Thomas.
[3177.96 → 3179.36] Two points each for JTT.
[3180.12 → 3180.56] Mm-hmm.
[3180.76 → 3184.70] And I get zero, so I guess J doesn't get any, but TT gets two.
[3185.96 → 3188.06] Other autocompletes there in that list.
[3188.24 → 3193.72] Death, Net Worth, Children, Cause of Death, Wife, and finally Steve Jobs quotes.
[3196.50 → 3197.48] No feet pics.
[3197.72 → 3199.32] No feet pics whatsoever.
[3199.68 → 3200.56] That was Thomas's.
[3200.72 → 3202.46] He threw a rush, and it was a good one.
[3203.98 → 3204.28] All right.
[3204.28 → 3210.88] So after round four, we still have Matthew and David tied with eight.
[3211.42 → 3211.98] That makes sense.
[3212.08 → 3212.98] Did you guys score that round?
[3213.04 → 3213.56] No, you did not.
[3213.82 → 3215.42] Just making sure my calculator is working.
[3216.18 → 3216.96] Matthew and David have eight.
[3217.28 → 3217.98] Taylor has seven.
[3218.10 → 3218.82] Thomas has six.
[3218.94 → 3219.54] Adam has six.
[3219.60 → 3223.04] This is a very tight game of modifying.
[3223.14 → 3224.32] We move down to round five.
[3225.36 → 3228.02] What if AI agents could work together just like developers do?
[3228.24 → 3231.78] That's exactly what agency is making possible.
[3231.78 → 3238.24] Spelled A-G-N-T-C-Y, agency is now an open source collective under the Linux Foundation,
[3238.60 → 3241.00] building the internet of agents.
[3241.50 → 3245.44] This is a global collaboration layer where the AI agents can discover each other,
[3245.82 → 3250.52] connect, and execute multi-agent workflows across any framework.
[3250.84 → 3256.92] Everything engineers need to build and deploy multi-agent software is now available to anyone
[3256.92 → 3262.20] building on agency, including trusted identity and access management, open standards for
[3262.20 → 3267.72] agent discovery, agent-to-agent communication protocols, and modular pieces you can remix
[3267.72 → 3269.26] for scalable systems.
[3269.60 → 3276.42] This is a true collaboration from Cisco, Dell, Google Cloud, Red Hat, Oracle, and more than
[3276.42 → 3280.56] 75 other companies all contributing to the next-gen AI stack.
[3280.56 → 3283.70] The code, the specs, the services, they're dropping.
[3283.86 → 3284.80] No strings attached.
[3285.06 → 3286.88] Visit agency.org.
[3286.94 → 3291.52] That's A-G-N-T-C-Y dot org to learn more and get involved.
[3291.80 → 3296.64] Again, that's agency, A-G-N-T-C-Y dot org.
[3297.12 → 3300.28] So your team has amazing ideas flying around.
[3300.38 → 3300.94] You know the feeling.
[3301.34 → 3305.90] But turning them into something real feels like wading through peanut butter.
[3306.10 → 3306.92] Super thick, right?
[3307.22 → 3308.60] Peanut butter is tough to walk through.
[3308.98 → 3309.76] We've all been there.
[3309.76 → 3313.58] The gap between idea and impact, it is brutal.
[3313.58 → 3318.84] And just throwing AI at the problem without clarity, that only makes things worse.
[3318.98 → 3319.74] We all know that.
[3319.94 → 3322.80] That's why I checked out Miró, investigated it, love it.
[3323.10 → 3324.18] And that's why I recommend it.
[3324.30 → 3329.14] Miró is the innovation workspace that helps teams get the right things done faster.
[3329.54 → 3332.98] Powered by AI, teamwork that used to take weeks, now takes days.
[3333.34 → 3337.04] You can use Miró to plan product launches, map complex workflows.
[3337.04 → 3342.68] You can even generate fresh ideas from interviews all in one place.
[3342.86 → 3355.80] And the Miró AI sidekicks, it's like having your own product leader, agile coach, and even a product marketer ready right there to review, clarify, and give feedback right inside your workspace.
[3355.80 → 3356.72] It's cool.
[3356.72 → 3360.78] You can even build custom sidekicks tailored to your workflow.
[3361.10 → 3370.18] Plus, Miró Insights pulls together sticky notes, research, and docs into clean summaries so you spend time building, not digging.
[3370.48 → 3372.40] Help teams get great done with Miró.
[3372.74 → 3374.36] Check out Miro.com.
[3374.36 → 3377.18] That is M-I-R-O dot com.
[3377.44 → 3379.46] Once again, Miró dot com.
[3383.56 → 3388.46] Moving on to round five, where we play a round of weird flicks.
[3388.90 → 3389.40] But okay.
[3390.20 → 3396.84] In this round, I have gone out to the internet and I have found an obscure old movie.
[3397.50 → 3397.92] Oh, yes.
[3398.50 → 3400.74] In fact, I found a movie from 1928.
[3401.18 → 3406.02] I then took the synopsis of that movie, you know, like the one-liner and description of like what the movie's about.
[3406.10 → 3407.48] You can read it on IMDb, et cetera.
[3407.88 → 3409.32] And I jotted that down.
[3409.42 → 3421.92] Your job is to write a synopsis given the name and the year that it was made and convince all of us that you actually wrote the real synopsis of the movie.
[3421.92 → 3425.20] The movie I wrote down is called The Man Who Laughs.
[3426.06 → 3427.18] The Man Who Laughs.
[3427.24 → 3429.10] It's from 1928.
[3429.36 → 3435.78] Please submit to me your synopsis for The Man Who Laughs whenever you have them ready.
[3441.96 → 3445.12] And we're confident on that year this time?
[3445.66 → 3446.82] The year is correct.
[3447.84 → 3449.10] The year is correct.
[3449.10 → 3451.74] I have to go over to my DVD shelf to grab it.
[3452.10 → 3457.36] Just for Thomas, a movie is like a book, but a fun book.
[3457.62 → 3458.88] It's like a fun version of a book.
[3459.00 → 3460.50] A fun book.
[3460.88 → 3462.04] A fun book.
[3463.04 → 3463.48] Book.
[3463.70 → 3464.04] Okay.
[3464.80 → 3465.28] Mmm.
[3466.04 → 3470.20] And it takes like several hours to days to finish?
[3470.70 → 3472.36] Oh, if you're doing it one speed, dude.
[3472.58 → 3473.34] If you're a rookie.
[3473.48 → 3474.06] That was bigger.
[3474.06 → 3478.46] You have to watch all my movies at 2x speed.
[3479.98 → 3483.34] Just as Scorsese intended.
[3483.58 → 3486.98] You have to watch it on your iPod Nano at double speed, you know?
[3488.00 → 3489.32] Have you seen Star Wars?
[3490.46 → 3492.20] That should be the legal question.
[3492.84 → 3493.10] I mean.
[3493.34 → 3493.90] That reminds me.
[3493.94 → 3497.92] Did you guys hear Ira Glass came out of NPR fame of This American Life?
[3497.92 → 3498.52] came out and said,
[3498.60 → 3500.76] all podcasts should be listened to at 2x.
[3501.44 → 3501.92] Surprise me.
[3501.92 → 3502.60] He did not say that.
[3502.68 → 3503.60] He did say that.
[3503.92 → 3504.52] He's a 3x.
[3504.92 → 3508.24] Ira Glass says podcasts should be listened to, including his own.
[3508.84 → 3510.10] All podcasts, 2x.
[3510.78 → 3515.28] I'm gonna start speaking really slow then.
[3515.28 → 3519.08] And all my jokes are going to take way too long.
[3519.40 → 3520.10] Speed that up.
[3520.54 → 3520.90] 2x.
[3521.12 → 3521.90] Tell me how that sounds.
[3522.46 → 3524.46] Adam, all your jokes already take too long?
[3524.46 → 3528.38] I normally speak fast, so people generally slow me down.
[3528.72 → 3528.94] Yeah.
[3529.08 → 3534.60] I got too much excitement, and I'm Texan, so, you know, when I speak, it's just Texan.
[3534.88 → 3535.64] I don't know how to say it.
[3535.64 → 3536.84] I don't know what that means.
[3537.34 → 3538.22] Is it big words?
[3538.94 → 3540.74] Did you learn your first big word, Adam?
[3541.58 → 3541.98] Chaytor.
[3542.84 → 3543.20] Star.
[3544.56 → 3545.82] That's all we know how to say here in Texas.
[3546.30 → 3546.68] Star.
[3548.16 → 3550.52] Matthew, just in case you didn't know, you just gave me the title.
[3550.52 → 3550.86] I know.
[3551.00 → 3551.28] I know.
[3551.46 → 3552.84] I sent you the title back.
[3552.84 → 3555.86] I like to give you the word and the thing that we're doing.
[3555.86 → 3557.40] I forgot I'm supposed to be describing a movie here.
[3557.54 → 3557.96] I'm talking.
[3558.54 → 3560.70] And I hit enter to do a new line.
[3560.92 → 3561.78] The man who laughs?
[3561.86 → 3562.44] Is that what this is?
[3562.56 → 3563.64] The man who laughs.
[3564.46 → 3564.90] 1928.
[3565.56 → 3566.54] The man who laughs.
[3566.94 → 3567.26] Okay.
[3568.66 → 3569.54] I can do this.
[3570.96 → 3574.98] Jared, when do you get the first snow in Nebraska?
[3575.98 → 3580.56] Well, we have very unpredictable weather, so it can be as early as Halloween.
[3580.56 → 3584.70] And we had actually one year a humongous snowstorm on Halloween.
[3585.38 → 3586.52] Closed it down.
[3587.62 → 3592.62] But more realistically, it's like late December, early January.
[3592.98 → 3594.78] But it's cold far before it snows.
[3595.26 → 3596.00] Oh, yeah.
[3596.80 → 3597.94] It'll be getting cold here soon.
[3598.60 → 3599.54] Right now it's perfect weather.
[3599.64 → 3601.18] We're in like 60s, 50s.
[3602.12 → 3602.52] Sunny.
[3603.16 → 3605.60] I like when the sun is hot, but the air is cold.
[3606.80 → 3607.76] That's good weather.
[3607.84 → 3608.96] Well, and you're in the right place.
[3608.96 → 3610.00] Yeah.
[3611.12 → 3620.90] I will say, Adam, I take your criticism of the Canadian-American experience, but one of
[3620.90 → 3623.08] the big benefits is two Thanksgivings.
[3623.86 → 3624.14] Yeah.
[3624.88 → 3626.14] I've already had a Thanksgiving.
[3626.44 → 3627.04] It was great.
[3627.62 → 3629.62] Got another Thanksgiving coming up in a few weeks.
[3630.20 → 3630.86] It's going to be great.
[3631.44 → 3633.78] Thanksgiving really should happen twice a year.
[3634.32 → 3634.96] Totally agree.
[3635.08 → 3635.64] 10 out of 10.
[3635.64 → 3637.14] It's actually like my favourite thing.
[3637.14 → 3637.78] Yeah.
[3637.90 → 3639.76] And they're spaced out enough.
[3640.42 → 3640.80] Right?
[3641.18 → 3649.30] They're about a month and change apart so that that second one really comes in.
[3649.36 → 3650.78] You're like, oh, yeah, I love Thanksgiving.
[3650.94 → 3651.38] It's great.
[3651.46 → 3652.40] It's coming around again.
[3653.08 → 3654.86] Is it similar fare or is there other?
[3655.00 → 3655.34] Yeah.
[3655.46 → 3656.14] Similar fare.
[3656.28 → 3656.78] Same stuff.
[3656.78 → 3657.72] Just different day.
[3658.52 → 3658.84] Cool.
[3659.32 → 3660.48] I did the turkey this year.
[3660.48 → 3663.74] Though I got too big of a turkey for the number of people we had.
[3664.86 → 3666.68] Well, that just means you got turkey sandwiches.
[3667.18 → 3667.74] Turkey sandwiches.
[3668.14 → 3670.54] I made some stock.
[3672.70 → 3675.40] What's your preferred preparation for the turkey?
[3675.40 → 3689.48] I do a salt rub the night before and let it air dry in the refrigerator.
[3690.00 → 3690.82] So I leave it uncovered.
[3691.54 → 3693.60] Gets the skin nice and crispy.
[3693.60 → 3694.04] Turkey.
[3694.04 → 3696.78] And then day of.
[3697.68 → 3700.00] Melt butter over it.
[3700.40 → 3701.60] Chop up a lot of veggies.
[3701.78 → 3706.24] Put them in the bottom of the pan and roast it.
[3706.44 → 3709.28] I don't do anything too crazy fancy, and it just comes out perfectly.
[3710.02 → 3713.64] That sounds alarmingly like some sort of treatment for fungus, foreign fungus.
[3714.04 → 3715.56] What is this you're making here?
[3716.08 → 3716.20] Turkey.
[3716.20 → 3716.70] These are potatoes?
[3717.34 → 3717.68] No.
[3717.90 → 3718.18] Turkey.
[3719.08 → 3719.34] Oh.
[3720.10 → 3720.50] Though.
[3720.50 → 3722.74] Have you ever deep-fried turkey?
[3722.98 → 3724.54] I don't have a house to sell on fire.
[3724.96 → 3725.72] Totally did.
[3726.26 → 3727.00] Nah, man.
[3727.56 → 3733.34] So the only time I've ever done it was with my uncle who is a career firefighter.
[3733.66 → 3740.02] And that was the only person with whom I felt safe enough to deep-fry a turkey.
[3741.26 → 3749.34] I appreciate, you know, all the local fire departments doing the video where they drop a turkey that's not quite frozen.
[3749.34 → 3750.18] And you just watch it.
[3750.30 → 3751.58] Or not quite thawed, and you just watch it.
[3751.58 → 3752.24] Not quite thawed.
[3752.28 → 3752.40] Yeah.
[3752.48 → 3753.26] Any of that water.
[3753.40 → 3754.06] It just goes.
[3756.34 → 3759.18] Matthew, how was your wife's chocolate business?
[3760.14 → 3760.50] Great.
[3760.50 → 3766.80] I actually have to take pictures for the next Thanksgiving, Christmas collection tomorrow, I think.
[3767.36 → 3768.34] Does she ship to Canada?
[3769.38 → 3770.06] Not to Canada.
[3770.40 → 3771.96] Because, man, that border coast is going to get you.
[3772.42 → 3773.06] I know.
[3773.28 → 3773.70] It's fine.
[3774.26 → 3774.90] It's fine.
[3775.20 → 3775.64] That's fine.
[3775.64 → 3780.40] But if you can meet us at Niagara Falls, then we can meet you at the border.
[3780.94 → 3781.62] Yeah, there you go.
[3781.70 → 3781.86] Yeah.
[3781.90 → 3782.98] Why are you coming down today?
[3783.18 → 3783.66] Oh, yeah.
[3783.86 → 3784.68] I need some chocolate.
[3784.92 → 3785.78] A little chocolate swap.
[3786.30 → 3787.62] Just toss it across the border.
[3787.62 → 3790.48] Oh, that's called smuggling.
[3791.28 → 3791.54] Yeah.
[3791.90 → 3792.12] Yeah.
[3792.24 → 3792.86] There's nothing wrong with that.
[3793.04 → 3793.22] No.
[3793.90 → 3794.68] I prefer snuggling.
[3796.08 → 3796.96] Chocolate jokes.
[3797.08 → 3797.86] What's the difference?
[3798.08 → 3798.72] I mean, come on.
[3799.92 → 3803.26] I was watching a video about the engineering of Niagara Falls the other day.
[3803.48 → 3804.68] Fascinating stuff.
[3804.68 → 3810.68] And what I learned was that pretty much the exact same setup is replicated on both sides.
[3811.40 → 3814.76] And it was kind of like a peeing contest to a certain degree.
[3814.84 → 3816.10] It's like, you're going to do that.
[3816.16 → 3816.68] We're going to do it.
[3816.70 → 3818.58] Like, they couldn't share.
[3818.72 → 3819.54] They couldn't work together.
[3819.70 → 3823.50] It was like, no, we're both going to have the exact same deal.
[3823.68 → 3824.72] We're just going to do everything twice.
[3826.32 → 3827.22] That was kind of funny.
[3827.22 → 3830.96] I think they work together in a certain sense of like the design because everything is designed
[3830.96 → 3833.60] like mirrored to a certain degree, which is kind of cool.
[3834.26 → 3839.22] But I didn't know there was like all that going on back then.
[3839.22 → 3841.22] Six.
[3858.02 → 3858.94] Pretty well written.
[3860.62 → 3864.98] Synopses for 1928's The Man Who Laughs.
[3865.06 → 3868.40] But which one is the actual movie plot?
[3868.40 → 3869.52] Here we go.
[3869.64 → 3870.18] Number one.
[3870.26 → 3875.40] The Man Who Laughs recounts the story of Dr. Dennis Rockwell, who struggles with his grip
[3875.40 → 3880.10] on reality as he treats his patients at Mount Baker Mental Asylum.
[3881.00 → 3881.70] Number two.
[3881.82 → 3887.54] A disgruntled railroad worker catches the next train out of town to find beauty in life.
[3888.34 → 3889.14] Number three.
[3889.50 → 3893.46] A veteran of the Great War cheerfully tries to save his farm.
[3893.84 → 3894.92] Number four.
[3894.92 → 3901.72] A disfigured nobleman with a permanent grin is forced into circus life and separated from
[3901.72 → 3902.72] his true identity.
[3903.60 → 3904.14] Number five.
[3904.24 → 3904.98] Darkly romantic.
[3905.72 → 3911.36] A comedian is heartbroken when his lover leaves him for a member of his audience, The Man Who
[3911.36 → 3911.76] Laughs.
[3912.40 → 3913.18] And number six.
[3913.26 → 3914.46] Thrust into the starlight.
[3914.56 → 3918.68] Two laugh-filled men adventure together to seek the love of the same woman.
[3918.68 → 3922.98] As stage performers who travel, they find it hard to see her in the crowd.
[3923.48 → 3927.52] So they developed a laugh from bellows down below to win her love.
[3927.84 → 3928.80] To win her love.
[3929.74 → 3930.20] All right.
[3930.30 → 3935.54] Six different potential synopses of 1928's The Man Who Laughs.
[3935.68 → 3939.26] Adam, you can't pile on this round because you are first.
[3939.26 → 3939.74] Last.
[3940.28 → 3940.76] Gosh.
[3942.08 → 3943.94] Is there any way to go last?
[3944.22 → 3945.14] Is that possible?
[3946.82 → 3949.28] You can't pile on because you're first.
[3949.60 → 3950.92] Can I just not do that?
[3952.38 → 3956.44] I do think that would be an interesting mechanic to introduce in a future version of this game.
[3956.88 → 3957.86] Adam always goes last?
[3958.30 → 3961.42] Or just like you, someone gets the ability to...
[3961.42 → 3963.84] Oh, to like play that card every once in a while or something.
[3964.06 → 3964.24] Yeah.
[3964.24 → 3964.32] Yeah.
[3964.32 → 3964.82] That's a good idea.
[3965.16 → 3965.52] Interesting.
[3966.10 → 3969.24] You know, I wasn't listening, so...
[3969.92 → 3973.12] I'm used to going last.
[3974.46 → 3976.38] And I get the pile on, push my button.
[3976.48 → 3978.72] It's just a, you know, the easy button, you know?
[3979.18 → 3981.54] Could I ask you to describe them to me again?
[3981.86 → 3984.38] I'm going to give you a brief because this is a lot of reading.
[3984.72 → 3986.62] No, you can just give me the summary.
[3986.62 → 3987.28] All right.
[3987.34 → 3990.38] So number one was the story of Dr. Dennis Rockwell.
[3990.56 → 3990.66] Okay.
[3990.66 → 3991.24] Yeah, I remember that.
[3991.32 → 3992.20] I was listening to that one.
[3992.24 → 3992.52] I was kidding.
[3992.70 → 3994.40] At the Mount Baker Mental Asylum.
[3994.56 → 3995.16] Number two...
[3995.16 → 3995.86] That's a pretty good one.
[3995.88 → 3996.46] Whoever wrote that.
[3996.74 → 4000.32] Number two was the disgruntled railroad worker who catches the next train out of town.
[4000.66 → 4001.20] Oh, yeah.
[4001.28 → 4001.98] Also pretty good.
[4002.20 → 4003.00] Finds beauty in life.
[4003.30 → 4003.46] Yeah.
[4004.18 → 4008.08] Number three was the veteran of the Great War who cheerfully tries to save his farm.
[4008.46 → 4009.52] Yeah, that's a good one too.
[4010.34 → 4016.82] Number four, a disfigured nobleman with a permanent grin who's forced into circus life.
[4017.10 → 4018.82] That does have smile feels.
[4019.60 → 4019.84] What?
[4019.84 → 4020.82] What is it?
[4020.86 → 4021.58] He said laughs.
[4021.70 → 4022.66] I guess laughs, smile.
[4022.78 → 4023.48] It's all the same, right?
[4023.74 → 4028.28] Number five was a comedian who's heartbroken when his lover leaves him for a member of his audience.
[4028.88 → 4029.68] The man who laughs.
[4030.24 → 4030.94] Taylor wrote that.
[4030.94 → 4033.38] Wow.
[4033.82 → 4034.34] Call out.
[4034.84 → 4039.30] Number six was the two laugh-filled men who are seeking the same, the woman's love.
[4040.00 → 4041.82] So there's your synopses of the synopses.
[4042.56 → 4043.14] What are you thinking?
[4043.40 → 4044.20] What are you convinced by?
[4044.28 → 4044.90] What are you...
[4044.90 → 4047.26] You know, I just want to ask if I can go last.
[4049.36 → 4050.22] You can't.
[4050.28 → 4051.20] You can't go last.
[4051.56 → 4052.44] All right, fine.
[4052.50 → 4062.66] I will go with the disgruntled railroad worker who found a way to go down the mountain.
[4063.66 → 4064.20] All right.
[4064.60 → 4065.22] Who's that guy?
[4065.36 → 4066.56] Is that mixing them?
[4066.72 → 4067.26] Did I mix them?
[4068.26 → 4071.26] A disgruntled railroad worker catches the next train out of town.
[4071.70 → 4072.22] That's the one you want?
[4072.58 → 4072.90] Yeah, yeah.
[4073.18 → 4074.26] I don't know if I like that one.
[4074.58 → 4074.86] All right.
[4075.88 → 4076.82] Well, we'll see.
[4077.06 → 4077.56] What was the one before that?
[4077.58 → 4078.14] Taylor, you're next.
[4078.14 → 4078.78] Could I go last?
[4079.48 → 4080.86] What was the one before that?
[4081.24 → 4082.30] The man who goes last.
[4082.38 → 4083.06] Are you not locked in?
[4083.84 → 4084.24] No.
[4085.02 → 4085.82] Still thinking about him.
[4085.82 → 4085.92] Shoot.
[4085.92 → 4087.96] I thought we were moving on.
[4089.16 → 4093.68] Before that was the Dr. Dennis Rockwell at the mental asylum.
[4093.94 → 4097.88] He treats his patients, but he struggles when he loses a grip on reality.
[4098.64 → 4100.28] Yeah, that's plausible for sure.
[4100.32 → 4100.56] You want that one?
[4101.26 → 4101.62] Nah.
[4102.36 → 4102.84] Railroad.
[4102.96 → 4103.92] Just go railroad all day.
[4104.32 → 4104.60] Railroad.
[4104.64 → 4104.90] All right.
[4104.96 → 4105.56] You're sticking with the railroad.
[4105.70 → 4106.30] Taylor, what do you want?
[4106.70 → 4107.20] Let's see.
[4108.26 → 4109.80] My grandma actually saw this one in theatres.
[4110.96 → 4112.24] She said it.
[4112.56 → 4113.80] Did you say theatres?
[4114.22 → 4114.98] 1928, right?
[4115.40 → 4115.72] Yeah.
[4115.72 → 4116.36] 1928.
[4116.36 → 4116.72] Yeah.
[4116.72 → 4116.88] Yeah.
[4118.16 → 4118.64] At the cinema.
[4119.08 → 4124.56] She told me, though, it was the one about the old guy with the house with the balloons.
[4126.36 → 4128.00] So that one's not an option.
[4128.68 → 4130.14] I'll go with the nobleman.
[4130.94 → 4131.88] The disfigured face.
[4132.72 → 4133.70] The disfigured nobleman.
[4133.90 → 4134.20] All right.
[4134.70 → 4134.92] Oh, wait.
[4134.96 → 4135.78] What was the first one again?
[4136.70 → 4139.32] The Mount Baskerville Mental Asylum.
[4140.20 → 4140.60] Ooh.
[4141.08 → 4141.80] You want that one instead?
[4142.18 → 4143.00] No, let's do nobleman.
[4143.74 → 4144.10] Thomas.
[4144.10 → 4144.22] Thomas.
[4144.94 → 4146.22] I, let's see.
[4146.26 → 4147.34] So we have The Mental Asylum.
[4147.54 → 4148.06] We have Beauty.
[4148.38 → 4148.88] Let's see.
[4149.56 → 4151.00] Man After the Great War.
[4151.14 → 4151.82] Circus Life.
[4152.32 → 4152.96] The Comedian.
[4153.06 → 4154.86] And then the two laugh-filled men.
[4154.86 → 4157.16] I feel like you have two laugh-filled men.
[4157.22 → 4159.86] You call it the men who laugh, or maybe that's the sequel.
[4162.44 → 4166.42] I'm going to go with the Mental Asylum one, the number one.
[4167.00 → 4167.52] Number one.
[4167.78 → 4168.58] That's a good choice.
[4168.96 → 4169.54] That's a good choice.
[4169.72 → 4170.22] Is it yours?
[4170.84 → 4171.08] No.
[4171.24 → 4172.08] It's just a good choice, man.
[4172.16 → 4172.80] We go to Matthew.
[4173.80 → 4175.00] Mental Asylum one.
[4175.66 → 4176.42] Railroad something.
[4177.42 → 4178.06] Nobleman something.
[4178.80 → 4181.20] You should go with the one with the Great War in it.
[4181.58 → 4182.62] Something about a Great War.
[4182.92 → 4184.58] Yeah, because I don't think it happened yet.
[4186.76 → 4191.62] Can you read the can you read the can you read the can you read the, you like, you know?
[4191.94 → 4194.48] Can you read the Asylum one and the Nobleman one?
[4194.62 → 4194.94] Sure.
[4194.94 → 4195.44] They're not the same, right?
[4195.44 → 4196.96] No, they're not the same.
[4197.64 → 4206.40] The Asylum one is the story of Dr. Dennis Rockwell, who struggles with his grip on reality as he treats his patients at Mount Baker Mental Asylum.
[4207.00 → 4207.38] Got it.
[4207.46 → 4207.66] Okay.
[4208.26 → 4211.24] Are you saying the Great War wouldn't have happened by 28?
[4211.86 → 4212.80] What's the Great War?
[4212.92 → 4213.24] Is that World War 1?
[4213.24 → 4213.72] 1928?
[4214.04 → 4215.00] No, yeah, you're right.
[4215.54 → 4216.32] But 1928.
[4216.58 → 4217.74] See, you just said doctors.
[4217.82 → 4219.34] They didn't have doctors in 1928.
[4219.60 → 4221.06] That one's false too, dude.
[4221.06 → 4226.80] Also synopsis is synopsises, whatever.
[4227.24 → 4227.56] Yes.
[4227.72 → 4231.38] Like a lot of, you've introduced me with too many characters in that synopsis.
[4231.80 → 4232.18] Right.
[4232.88 → 4234.48] And the other one was a noble something?
[4234.86 → 4236.22] Yeah, disfigured nobleman.
[4236.64 → 4237.32] Disfigured nobleman.
[4237.32 → 4238.46] He's got a permanent grin.
[4239.50 → 4240.20] Oh, like the Joker.
[4240.92 → 4241.52] Always smiling.
[4242.06 → 4243.64] He's forced into circus life.
[4244.64 → 4246.34] And separated from his true identity.
[4246.86 → 4247.78] That sounds fun.
[4248.74 → 4250.56] So he's forced into, okay.
[4251.20 → 4252.98] I think I'm leaning to that one.
[4253.08 → 4254.12] Someone already picked that one though, right?
[4254.54 → 4257.72] Yeah, Taylor picked that one and Thomas picked the mental asylum one.
[4257.78 → 4259.48] So they both have one person on them.
[4259.72 → 4261.68] I think I'm leaning towards the nobleman.
[4262.20 → 4263.14] The Joker story.
[4263.66 → 4264.62] The Joker origin story.
[4265.04 → 4265.30] Okay.
[4266.08 → 4267.04] You're going to lock that in?
[4267.60 → 4268.80] Railroad is another one.
[4270.12 → 4271.02] Lovers something.
[4271.88 → 4272.20] Yes.
[4273.26 → 4275.52] Yeah, I think the nobleman sounds the best here.
[4275.52 → 4279.84] It feels, I don't think anyone here is going to use the word disfigured.
[4279.84 → 4280.56] Wow.
[4280.66 → 4281.86] That's a that's a dis.
[4282.36 → 4283.54] It, it, yeah.
[4283.94 → 4284.32] All right.
[4284.36 → 4285.34] I'm going to lock you in then.
[4285.54 → 4286.18] Lock me in, please.
[4286.36 → 4287.26] Locked you in on the pylon.
[4288.08 → 4289.44] We go to David.
[4290.16 → 4290.38] Yeah.
[4290.40 → 4296.58] I think my intuition last time was sort of prudish about what would be acceptable movie
[4296.58 → 4297.62] like contents.
[4297.62 → 4302.60] And so the disfigured nobleman kind of sounds right to me as well.
[4302.72 → 4304.90] So it's a pylon again.
[4305.12 → 4306.06] Oh, all right.
[4306.32 → 4308.44] We're very, we're very conservative bunch here.
[4308.62 → 4309.88] We're all, a lot of hurting.
[4310.34 → 4311.62] I am, I am in pain.
[4311.70 → 4312.50] So yeah, the hurting is real.
[4312.92 → 4313.36] No, I'm just kidding.
[4313.82 → 4315.02] Well, it's keeping the game closed.
[4315.02 → 4317.24] Cause every time someone scores, everybody else scores also.
[4317.80 → 4319.34] All right.
[4319.34 → 4323.08] Well, we've heard these synopses over and over and over again.
[4323.30 → 4324.42] Let's go to the guesses.
[4324.62 → 4327.68] Adam thought maybe it was the disgruntled railroad worker.
[4327.84 → 4329.00] That was written by Matthew.
[4329.18 → 4330.66] So one point to Matthew.
[4331.70 → 4335.70] Thomas was convinced by the Mount Baker mental asylum.
[4335.90 → 4337.48] I thought that one was amazing.
[4337.66 → 4338.40] Taylor wrote that.
[4338.48 → 4339.48] Good job, Taylor.
[4340.46 → 4341.42] Point to Taylor.
[4341.42 → 4342.80] And then the pile on.
[4343.58 → 4346.82] They're piling onto a disfigured nobleman with a permanent grin.
[4347.88 → 4352.12] Who's forced into circus life and separated from his true identity in 1928.
[4352.24 → 4353.54] The man who laughs.
[4353.74 → 4356.70] That is the actual synopsis of a movie.
[4356.76 → 4357.82] It doesn't sound half bad.
[4357.86 → 4358.22] Does it?
[4358.42 → 4359.26] It actually doesn't.
[4360.02 → 4360.92] I might have to go.
[4361.30 → 4362.06] Change the movie.
[4362.88 → 4363.32] Yeah.
[4363.36 → 4365.92] Or if you could get it converted into a book, then you could read it.
[4366.14 → 4366.38] Get it.
[4366.42 → 4368.64] I don't have to read everything as a book.
[4369.06 → 4370.92] I also can tell movies.
[4370.92 → 4373.44] You could pull the book out when we talk about it.
[4373.62 → 4374.16] Fun fact.
[4374.58 → 4377.52] Man Who Laughs was the very first Pixar film.
[4379.06 → 4384.56] It's coming from the guy who's calling into question the years of the Great War.
[4384.64 → 4385.18] That was David.
[4385.32 → 4386.72] That's why he was defending that one.
[4387.10 → 4389.44] I tried to let it breathe for an appropriate amount.
[4390.16 → 4392.16] You don't want to jump to this defence too harshly.
[4392.38 → 4392.56] Yeah.
[4392.78 → 4394.08] I knew what you were doing there, David.
[4394.14 → 4394.74] I could see it.
[4395.04 → 4395.40] Well played.
[4395.58 → 4395.76] All right.
[4395.80 → 4399.62] So Taylor, Matthew, and David all get two points for getting that right.
[4399.62 → 4401.70] So three total points for Taylor.
[4401.92 → 4402.92] Two for David.
[4403.12 → 4403.62] Three for...
[4404.18 → 4404.76] Where's my points?
[4404.82 → 4405.38] Did I get any points?
[4405.62 → 4406.02] Matthew.
[4406.20 → 4406.54] No.
[4406.76 → 4407.50] Not this round.
[4407.78 → 4408.04] No.
[4408.20 → 4409.62] Unfortunately, you didn't get to go last.
[4410.20 → 4410.80] Oh, man.
[4411.22 → 4414.12] And that brings us to the end of round five.
[4414.24 → 4416.42] And Matthew is in striking distance.
[4416.58 → 4417.34] He has 11.
[4417.44 → 4420.48] Of course, Taylor and David are also in striking distance with 10.
[4420.48 → 4423.70] Thomas and Adam have six.
[4424.30 → 4425.64] And we don't have to talk about me.
[4425.64 → 4427.82] I'm going to call a two-point win.
[4428.12 → 4428.66] Play your own rules.
[4430.52 → 4431.52] I don't know, man.
[4431.62 → 4432.48] I'm trying to...
[4432.48 → 4434.14] I see the time.
[4434.98 → 4436.18] I've got to eat, bro.
[4436.42 → 4436.84] I don't know.
[4437.42 → 4439.08] I'm not winning, so...
[4439.08 → 4440.38] So your entire...
[4440.38 → 4441.26] Not with that attitude.
[4441.68 → 4443.82] ...idea should switch to subterfuge, don't you think?
[4444.00 → 4444.70] That's your strategy?
[4444.82 → 4445.40] I'm just going to start reading.
[4445.78 → 4446.48] Just start reading.
[4446.48 → 4449.08] All right.
[4449.18 → 4450.56] That brings us to round six.
[4450.78 → 4453.08] And that brings us to a very long word.
[4454.76 → 4456.54] Pronounced Brobdingnagian.
[4457.98 → 4458.58] Brobdingnagian.
[4459.96 → 4463.22] The word for round six is Brobdingnagian.
[4463.84 → 4471.58] And it's spelled B-R-O-B-D-I-N-G-N-A-G-I-A-N.
[4473.66 → 4474.22] Brobdingnagian.
[4474.22 → 4476.54] Maybe that's my best pronunciation yet.
[4477.30 → 4477.98] Brobdingnagian?
[4478.30 → 4478.82] Brobdingnagian?
[4479.18 → 4480.66] Brobdingnagian.
[4481.04 → 4482.54] That is definitely not how it's pronounced.
[4482.94 → 4484.74] But I see why you're doing it that way.
[4484.76 → 4486.26] This is the second time you've done this to me.
[4486.34 → 4487.90] And I'm telling you, I looked it up on YouTube.
[4488.04 → 4489.56] It's pronounced Brobdingnagian.
[4490.32 → 4492.24] So take that, Matthew.
[4492.34 → 4493.24] Take that, Matthew.
[4493.90 → 4494.20] Yeah.
[4494.44 → 4496.50] Check out your own YouTube videos for pronunciation.
[4497.08 → 4498.42] And step back.
[4498.42 → 4499.56] You're rocking my world again.
[4500.92 → 4501.92] Brobdingnagian.
[4501.92 → 4504.66] If it ends in I-A-N, it's Armenian.
[4505.54 → 4507.10] So fun fact.
[4507.96 → 4508.92] A slight alteration.
[4509.06 → 4511.24] It could also be pronounced Brobdingnagian.
[4512.20 → 4514.10] So it could be Magian or Magian.
[4514.42 → 4515.14] I've heard them both now.
[4515.90 → 4517.20] But Brooding is correct.
[4518.34 → 4518.76] Brooding.
[4519.20 → 4523.98] Please submit to me your definitions of Brooding.
[4524.40 → 4524.72] Ding.
[4525.04 → 4525.44] Magian.
[4525.68 → 4526.06] Ding.
[4526.06 → 4527.60] Or Magian if you prefer.
[4528.06 → 4528.40] Now.
[4528.40 → 4528.46] Now.
[4528.46 → 4528.52] Now.
[4528.52 → 4528.60] Now.
[4528.60 → 4528.68] Now.
[4528.68 → 4528.72] Now.
[4528.72 → 4529.04] Now.
[4529.04 → 4530.52] Now.
[4530.52 → 4530.60] Now.
[4530.60 → 4539.42] You know what?
[4539.48 → 4539.92] It's been real.
[4540.24 → 4541.08] I'm going to get some dinner.
[4542.28 → 4544.04] Jared can't pronounce the words anymore.
[4544.48 → 4544.82] Hey.
[4544.90 → 4545.90] I'm two for two, man.
[4546.00 → 4546.60] I'm two for two.
[4546.70 → 4547.04] You're good.
[4547.52 → 4547.96] This.
[4548.24 → 4550.18] This word is interesting.
[4551.02 → 4552.34] I have words about this word.
[4552.86 → 4553.16] Hmm.
[4553.48 → 4554.84] Write them down and submit them to me.
[4555.02 → 4556.60] I can't say it until our definitions are out there.
[4556.82 → 4557.06] Okay.
[4557.56 → 4560.06] Oh, by the way, Adam, did you LLM that last one?
[4560.06 → 4562.66] I haven't LLM'd anything, man.
[4562.90 → 4563.18] Okay.
[4563.70 → 4565.44] Boy, you better start Liming.
[4565.46 → 4566.50] You're running out of time, dude.
[4566.58 → 4567.30] Am I allowed to do that?
[4567.60 → 4568.54] You get one.
[4568.80 → 4569.38] You get one pass.
[4569.38 → 4570.18] Oh my gosh.
[4570.20 → 4571.30] I should do this soon.
[4572.02 → 4578.90] So my, uh, I mute myself when I'm typing because I have this, uh, gnarly little, uh, cliquey-clacker.
[4579.90 → 4584.80] And, uh, when I do type, I get the little notification.
[4586.06 → 4588.28] Hey, uh, are you trying to speak?
[4588.50 → 4590.44] If you're trying to speak, you're muted right now.
[4590.54 → 4590.92] I'm like, no.
[4591.46 → 4591.90] I'm typing.
[4592.46 → 4594.50] I prefer just to hear the click-clacks, man.
[4595.10 → 4595.44] All right.
[4595.74 → 4595.88] I know.
[4596.32 → 4596.92] Let's get them.
[4597.46 → 4598.32] Click, click, click, click, click.
[4598.46 → 4598.64] Okay.
[4599.20 → 4601.10] But now I have to do some thinking before I type.
[4601.10 → 4602.60] Now we know when you're not typing, too.
[4603.32 → 4603.72] Hmm.
[4604.24 → 4605.56] We silently judge you.
[4606.30 → 4610.20] I think if you were really paying attention, you could notice, like, how long was I typing?
[4610.40 → 4611.90] You could guess which.
[4612.36 → 4613.58] I wouldn't put it past David.
[4613.66 → 4614.96] I think he's playing to win here.
[4615.22 → 4617.82] He's probably going to listen to your typing and figure out your definition.
[4617.82 → 4621.78] He has those big over-ear headphones on to really get.
[4622.10 → 4624.60] Matthew also has headphones.
[4624.80 → 4625.04] What are you?
[4625.14 → 4625.60] Like, this is.
[4625.60 → 4626.88] Literally, literally.
[4626.88 → 4628.80] The majority of people in this chat.
[4629.18 → 4630.26] Have over-ear.
[4630.70 → 4632.62] I know, I know, I know, I know, I know.
[4632.76 → 4633.78] It's not lost on me.
[4633.92 → 4635.58] I mean, mine are open back, so I still hear.
[4636.02 → 4636.68] Oh, okay.
[4636.80 → 4637.04] Yes.
[4637.36 → 4638.66] Oh, wow.
[4639.10 → 4641.96] Yeah, I got to hear my dog's barking or my wife is calling me.
[4642.00 → 4642.18] Yep.
[4642.40 → 4643.50] I hear my dog barking.
[4643.72 → 4644.62] I'm going to take her for a walk.
[4645.10 → 4647.42] Can I change my answer for the Steve Jobs one?
[4647.82 → 4652.14] What do you want?
[4655.84 → 4656.44] I don't know.
[4656.52 → 4657.60] I just wondered if I could.
[4658.62 → 4659.00] He's alive.
[4659.28 → 4660.02] Yeah, go for it.
[4662.02 → 4662.38] Okay.
[4664.06 → 4667.60] I want to choose Steve Jobs' net worth.
[4668.96 → 4671.34] That gives Adam another point.
[4672.50 → 4673.28] Yeah, I know, right?
[4673.82 → 4674.32] Here we go.
[4674.32 → 4676.34] I did get.
[4676.44 → 4678.72] This is relevant to Changelog.
[4678.78 → 4680.60] I did get this book before it came out.
[4681.50 → 4682.08] Oh, wow.
[4682.12 → 4684.68] I got the not for resale.
[4684.88 → 4685.66] Before it came out?
[4686.02 → 4686.30] Yeah.
[4686.58 → 4686.70] Dang, dude.
[4686.70 → 4688.68] That's a contradiction, dude.
[4689.36 → 4690.72] You can't get something before it comes out.
[4690.78 → 4694.20] But that's not true if you know the right people.
[4696.26 → 4696.86] Did you?
[4696.86 → 4698.32] I had it before he wrote it, so.
[4698.94 → 4700.24] You had it before he wrote it?
[4700.56 → 4700.92] Yeah.
[4701.04 → 4701.98] Well, you got to know the right people.
[4702.66 → 4706.74] No, this is, yeah, it says, these proofs are not to be quoted for publication.
[4707.58 → 4709.20] You just published it, dude.
[4709.36 → 4710.22] You're on a podcast.
[4711.00 → 4711.82] The book's out.
[4711.92 → 4712.62] The book came out.
[4712.70 → 4715.02] It says on the back when the book actually comes out.
[4716.36 → 4717.18] It already came out.
[4717.58 → 4718.50] Everyone can buy it now.
[4718.50 → 4723.76] Did you hear about the sequel to that book called Constipation?
[4724.54 → 4725.18] No, you haven't.
[4725.20 → 4726.02] It hasn't come out yet.
[4728.78 → 4730.18] That's a good one.
[4730.46 → 4730.72] Bravo.
[4731.54 → 4734.36] I hate that I love that, but that's pretty good.
[4734.70 → 4735.94] He hates that he loves it.
[4736.36 → 4737.10] That's a good one.
[4737.32 → 4738.56] Such is life.
[4738.76 → 4739.08] Okay.
[4745.30 → 4748.28] Six definitions for Brooding.
[4748.28 → 4748.84] Magian.
[4749.66 → 4750.92] Number one.
[4751.66 → 4754.96] Purposefully accelerating civilization collapse.
[4756.04 → 4756.72] Number two.
[4756.92 → 4760.14] Having to do with the sport of bobsleding.
[4763.40 → 4764.36] Number three.
[4765.80 → 4766.88] All right, Taylor.
[4767.10 → 4767.72] We got it.
[4767.82 → 4768.68] We got it.
[4771.56 → 4772.28] Number three.
[4773.20 → 4777.28] A fictional area in the Golden Sun video game where the characters face the toughest enemies.
[4778.28 → 4779.24] Number four.
[4779.34 → 4781.48] A matrix of fourth derivatives.
[4782.50 → 4783.64] Number five.
[4783.98 → 4786.38] Cousin to the backyard against Malik.
[4786.38 → 4791.38] Zara, Benji, and they're going to love to play in the front yard.
[4794.56 → 4796.12] You're not helping anything with that.
[4796.66 → 4799.60] Imagine themselves on fantastic adventures.
[4799.60 → 4801.74] Who did that?
[4802.16 → 4802.92] That's awesome.
[4803.38 → 4804.42] That's amazing.
[4805.02 → 4806.12] And number five.
[4806.42 → 4806.88] Or sorry.
[4806.98 → 4807.80] Number six.
[4808.28 → 4810.52] Marked by tremendous size.
[4811.08 → 4812.60] Marked by tremendous size.
[4813.92 → 4814.20] Okay.
[4815.78 → 4816.72] Six definitions.
[4817.46 → 4818.52] Good news for you, Adam.
[4818.52 → 4819.60] You get to go last.
[4819.60 → 4820.60] Jesus.
[4820.84 → 4821.46] So you're safe.
[4822.22 → 4823.50] Taylor has to go first this round.
[4824.50 → 4824.94] Taylor.
[4826.00 → 4828.12] What do you think is brooding Began?
[4828.96 → 4831.56] I do just want to give a shout-out real quick to the backyard again.
[4831.72 → 4835.24] I've been watching that show with my daughter, and it's like on some fire tracks.
[4835.76 → 4835.82] Like.
[4836.32 → 4837.42] Oh yeah, man.
[4838.08 → 4838.46] Oh yeah.
[4838.96 → 4839.18] K.
[4839.30 → 4840.46] Bob Demon Hunters.
[4841.48 → 4841.96] Oh.
[4843.12 → 4843.94] That's a good one.
[4843.94 → 4845.68] So it's between.
[4846.46 → 4847.40] So it's between.
[4847.46 → 4849.00] So it's between a Bob sledding.
[4849.10 → 4850.38] That was, that was a very good one.
[4850.46 → 4850.82] Whoever did.
[4850.90 → 4851.76] That's very clever.
[4852.98 → 4853.86] Bob sledding.
[4854.48 → 4856.14] It could be the real answer.
[4856.26 → 4856.78] You don't know.
[4858.72 → 4861.46] You have like, you don't think Bob sledding is not real or something.
[4862.46 → 4862.86] Yeah.
[4862.86 → 4863.82] I think I liked the first one.
[4863.82 → 4864.34] The last one.
[4864.40 → 4865.34] They sounded the most legit.
[4866.38 → 4867.16] Yeah, they did.
[4867.62 → 4868.02] Okay.
[4868.56 → 4871.04] The last one was size.
[4871.86 → 4872.20] Yeah.
[4872.38 → 4873.10] Tremendous size.
[4873.10 → 4874.80] Tremendous size.
[4876.10 → 4877.26] No, that's too on the nose.
[4877.34 → 4877.98] What was the first one?
[4878.48 → 4882.42] The first one was purposefully accelerating civilizational collapse.
[4883.10 → 4883.46] Ooh.
[4884.48 → 4889.42] No, that, that's too, that's too, uh, that's too smart for me.
[4889.70 → 4893.44] Uh, what about, uh, let's pick the last one.
[4893.62 → 4893.96] Size.
[4895.02 → 4895.54] Size.
[4895.80 → 4896.48] He's going for size.
[4898.22 → 4900.62] Size does matter for Taylor Thomas.
[4901.46 → 4901.98] Size.
[4902.62 → 4902.98] Size.
[4903.48 → 4903.84] Big.
[4904.06 → 4904.92] Or size.
[4907.36 → 4908.12] Which size?
[4908.58 → 4909.82] Marked by tremendous size.
[4910.36 → 4911.62] He's asking about a homonym.
[4912.62 → 4913.26] What'd you call me?
[4917.06 → 4918.54] So we got S-I-Z-E.
[4918.68 → 4919.94] It's spelled S-I-Z-E.
[4919.94 → 4921.10] S-I-Z-E.
[4921.34 → 4921.58] Yeah.
[4922.06 → 4922.26] Civilization.
[4922.34 → 4924.42] So accelerating civilization collapse.
[4924.66 → 4924.96] Correct.
[4924.96 → 4926.16] Rob sledding, which.
[4926.38 → 4926.88] Rob sledding.
[4927.40 → 4929.14] Is, I mean, it sounds perfect.
[4930.14 → 4930.54] Um.
[4930.54 → 4931.92] And you have the golden sun video game.
[4931.92 → 4932.72] The golden sun video game.
[4933.16 → 4933.38] Yeah.
[4933.38 → 4935.74] Matrix of fourth derivatives.
[4935.74 → 4935.86] Derivatives.
[4936.36 → 4936.70] Yes.
[4936.92 → 4937.82] The backyardigans.
[4938.38 → 4939.62] Cousin to the backyardigans.
[4939.74 → 4940.84] Cousin to the backyardigans.
[4940.84 → 4941.14] Yeah.
[4942.06 → 4942.32] Rob.
[4942.38 → 4943.10] Pickwickian.
[4943.58 → 4946.14] Marked by tremendous size.
[4947.34 → 4947.78] Uh.
[4948.30 → 4952.40] It's dark, but I'll do the acceleration of civilization collapse.
[4953.16 → 4953.52] Okay.
[4953.52 → 4954.00] Hey.
[4954.60 → 4955.66] We go to Matthew.
[4956.68 → 4959.22] The summary of each of them was, let me think of if I remember this.
[4959.46 → 4959.76] Um.
[4960.60 → 4962.32] Mark Peter man, size one.
[4963.06 → 4965.82] Thomas, collapse of civilization that he just picked.
[4966.22 → 4966.52] Right.
[4967.18 → 4967.74] Rob sledding.
[4968.12 → 4968.36] Rob.
[4968.36 → 4969.44] Rob sledding.
[4969.80 → 4970.96] Backyardigans or something.
[4971.24 → 4971.48] Correct.
[4972.68 → 4973.12] Uh.
[4973.80 → 4974.80] Golden sun something.
[4975.26 → 4975.58] Yes.
[4976.28 → 4977.74] And a matrix of fourth derivatives.
[4978.28 → 4981.24] A matrix of fourth derivatives.
[4981.90 → 4982.36] Correct.
[4982.36 → 4984.36] As in math, I guess.
[4984.72 → 4985.52] No, these are language.
[4985.72 → 4988.44] These are programming languages that derive from fourth.
[4989.16 → 4989.48] Boo.
[4989.82 → 4990.70] That's a homonym.
[4991.56 → 4992.10] That is a homonym.
[4992.72 → 4993.10] Um.
[4993.62 → 4993.94] Wow.
[4994.48 → 4995.40] I'm actually not sure.
[4996.48 → 4996.72] Rob.
[4996.88 → 4997.16] Rob.
[4997.34 → 4997.50] Ding.
[4997.64 → 4998.16] Rob.
[4998.88 → 4999.72] I can't say that.
[4999.74 → 4999.78] Robbing.
[4999.78 → 4999.80] I can't say that.
[4999.80 → 4999.84] Robbing.
[4999.84 → 5000.22] I can't say that.
[5000.48 → 5000.86] Robbing.
[5000.86 → 5001.02] Robbing.
[5001.02 → 5001.38] Robbing.
[5001.78 → 5002.26] Robert Ding.
[5002.26 → 5008.22] It sounds like a thing rather than like a status or like a description of something.
[5008.98 → 5010.68] Sounds like an actual thing.
[5011.28 → 5011.96] Like a noun.
[5012.36 → 5012.76] Yeah.
[5013.18 → 5013.58] Exactly.
[5013.96 → 5014.86] Like it's a name.
[5014.96 → 5015.18] Somebody.
[5015.38 → 5016.94] That's somebody hanging out.
[5017.06 → 5017.28] Yeah.
[5017.32 → 5020.52] It's like the name of a location or something, or it's a name of something.
[5021.22 → 5022.66] Like you call someone this.
[5023.02 → 5023.94] You know what I mean?
[5024.04 → 5024.16] Like.
[5024.30 → 5024.66] Right.
[5024.94 → 5025.92] You are such.
[5025.98 → 5026.84] Like it's a slur.
[5026.84 → 5027.44] Okay.
[5027.44 → 5028.06] So I have to limit.
[5029.12 → 5030.50] Not the backyard again thing.
[5030.80 → 5033.98] Not the other Rob sledding one.
[5035.06 → 5036.82] Collapsing of society.
[5036.96 → 5037.66] I don't think so.
[5038.08 → 5038.90] And then there's three more.
[5039.30 → 5040.24] Marked by tremendous size.
[5040.30 → 5040.90] That's an adjective.
[5040.90 → 5043.30] And then you have the matrix of four derivatives.
[5044.14 → 5045.04] Which would be a noun.
[5045.24 → 5046.34] So I've narrowed down to what?
[5046.68 → 5048.24] Golden sun and size.
[5048.70 → 5051.38] Golden sun and size.
[5051.52 → 5052.38] Well size is not.
[5052.88 → 5053.78] I'm not going to help you.
[5054.36 → 5054.68] That's fine.
[5054.92 → 5056.36] I'm just saying it's not a noun.
[5056.62 → 5057.34] You're leaning on that.
[5057.34 → 5057.92] No I agreed.
[5057.92 → 5059.46] But like every other ones.
[5060.10 → 5061.06] I don't like the other ones.
[5061.66 → 5061.98] Okay.
[5062.12 → 5062.34] Fine.
[5062.70 → 5063.50] Whatever one you want.
[5063.84 → 5065.28] Can you read the golden sun one please?
[5065.50 → 5066.14] Can you read both of them?
[5066.14 → 5070.30] A fictional area in the golden sun video game where the characters face the toughest enemies.
[5070.94 → 5073.36] And then marked by tremendous size.
[5074.14 → 5077.20] Fictional area in the golden sun.
[5077.48 → 5082.40] I like that it clarifies that it is a fictional area in the video game.
[5083.10 → 5083.40] Mm-hmm.
[5083.50 → 5083.78] Yeah.
[5084.42 → 5086.34] Like there are real areas and then there are fictional areas.
[5086.64 → 5087.06] Mm-hmm.
[5087.16 → 5087.36] Yeah.
[5087.72 → 5090.54] Like Grand Theft Auto is like real areas in a fictional game.
[5090.74 → 5090.88] You know?
[5091.32 → 5091.80] Right.
[5091.94 → 5093.20] Or Tony Hawk's Pro Skater.
[5093.20 → 5094.70] Like you're on Burnside.
[5094.70 → 5096.66] But you're not actually there.
[5096.76 → 5097.58] By the way Thomas.
[5098.00 → 5100.88] Thomas a video game is just a really fun movie.
[5101.50 → 5103.44] Really fun movie?
[5104.40 → 5105.82] So choose your own adventure book.
[5106.24 → 5110.08] I feel like there's an escalation of fun that I'm just missing out on.
[5110.44 → 5112.20] I think I kind of have to pile on here.
[5112.36 → 5113.96] Because yeah.
[5114.30 → 5114.68] I don't know.
[5115.22 → 5116.40] Nothing really names.
[5117.16 → 5120.80] Nothing really names the video game.
[5121.02 → 5122.56] Like why would a definition name something?
[5122.72 → 5123.04] I don't know.
[5123.04 → 5124.60] I mean like Metaverse?
[5125.24 → 5125.40] Yeah.
[5125.44 → 5125.82] I guess.
[5126.28 → 5126.72] All right.
[5126.78 → 5128.50] I'll pile on to the size one.
[5128.64 → 5130.50] Because I don't believe it's a society collapse.
[5131.26 → 5131.54] All right.
[5132.00 → 5134.28] Matthew is with Taylor on size.
[5134.72 → 5134.98] David.
[5135.34 → 5136.66] You are a Brobdingnagian.
[5137.16 → 5139.04] You are so Brobdingnagian.
[5139.30 → 5140.02] I don't know.
[5140.46 → 5140.66] Yeah.
[5140.94 → 5142.46] So Brobdingnagian.
[5143.50 → 5147.98] I don't know if there's like a word like Manichean.
[5147.98 → 5154.50] Which is like a way that people construct a world view that's kind of binary between good and evil.
[5154.86 → 5158.86] And so that's one way in which that could be like the that could be related.
[5159.82 → 5165.52] There are my different like my linear algebra is very rusty.
[5165.52 → 5171.96] So I feel like there are some named matrices, but I don't remember if that's one of them.
[5172.54 → 5174.70] We have a couple of obviously ridiculous ones.
[5175.40 → 5175.60] Sorry.
[5175.70 → 5177.62] Did it specify what video game?
[5178.34 → 5178.58] Yeah.
[5178.68 → 5179.26] Golden Sun.
[5179.94 → 5180.80] Golden Sun.
[5182.22 → 5183.30] Is that a game like.
[5183.30 → 5186.18] Is that a popular game?
[5186.66 → 5186.90] I don't know.
[5188.02 → 5189.20] I haven't heard of it myself.
[5189.58 → 5189.84] Okay.
[5191.14 → 5193.66] But I'm not a gamer very much.
[5193.66 → 5194.92] I just play Rocket League.
[5195.62 → 5195.76] Yeah.
[5196.74 → 5198.08] Enormous size.
[5198.86 → 5202.12] It is kind of a like big feeling word.
[5202.44 → 5202.58] You know.
[5203.08 → 5203.42] Yeah.
[5203.88 → 5205.46] And thus regrettably.
[5207.00 → 5207.96] He's piling on.
[5208.14 → 5208.28] Yeah.
[5208.38 → 5209.04] It's happening.
[5209.30 → 5209.72] It's happening.
[5209.94 → 5210.42] I.
[5210.76 → 5211.04] I.
[5211.04 → 5214.54] I'm not quite convinced by any of the others.
[5214.84 → 5215.02] So.
[5215.30 → 5218.50] So Matthew and Taylor are tied with 11 and you have.
[5218.74 → 5219.02] Sorry.
[5219.44 → 5220.34] Matthew has 11.
[5220.46 → 5222.22] You and Taylor are tied with 10.
[5222.52 → 5225.00] And so all you are picking the same one.
[5225.56 → 5225.78] Yeah.
[5226.14 → 5226.28] No.
[5226.32 → 5227.38] I mean like there's no.
[5227.80 → 5228.20] There.
[5228.32 → 5229.14] There is not a.
[5229.80 → 5230.20] I don't.
[5230.30 → 5234.70] I don't think there's a strategically better move to make than attempting to pick the correct thing.
[5234.70 → 5235.10] Like it's.
[5235.16 → 5237.44] It's basically like going to.
[5237.90 → 5238.26] Yeah.
[5238.32 → 5239.26] Well let's see what happens.
[5239.76 → 5240.02] All right.
[5240.02 → 5240.78] Let's see what happens.
[5241.36 → 5241.52] So.
[5242.64 → 5243.38] What's up man?
[5244.26 → 5245.08] You're up man.
[5245.44 → 5246.64] Oh my gosh.
[5248.32 → 5250.38] I'm going to have you read them all again for me.
[5251.04 → 5252.54] You can just pile on dude.
[5252.80 → 5253.44] You're going last.
[5254.06 → 5255.80] I don't want to go last though this time.
[5255.88 → 5256.22] I want to go.
[5256.88 → 5257.10] Wait.
[5257.18 → 5257.38] I do.
[5257.48 → 5258.58] Everybody else is already gone.
[5258.78 → 5258.96] This is cool.
[5259.56 → 5259.98] It's all gone.
[5260.36 → 5261.70] How could you not go last?
[5262.82 → 5264.36] You're first and then you're last.
[5264.78 → 5265.62] I can't take you anywhere.
[5265.94 → 5266.44] What is it?
[5266.50 → 5267.00] There was a.
[5267.08 → 5267.88] There was a.
[5267.88 → 5269.44] There was a.
[5269.52 → 5270.10] There was a book.
[5270.46 → 5271.52] A little blue truck.
[5272.78 → 5273.50] Move it buds.
[5273.60 → 5274.12] I'm first.
[5274.22 → 5274.88] You're last.
[5275.12 → 5275.92] That's what it says.
[5276.24 → 5276.56] Okay.
[5277.00 → 5277.36] Okay.
[5277.48 → 5277.82] Fine.
[5277.92 → 5278.10] I'll.
[5278.22 → 5278.40] You know.
[5278.48 → 5279.42] Default answer.
[5279.42 → 5282.02] I guess.
[5282.10 → 5282.54] I guess I'll.
[5282.72 → 5283.40] I'll pile on.
[5283.64 → 5283.94] Okay.
[5284.06 → 5284.42] He's pile.
[5284.42 → 5284.80] I'll pile on.
[5284.92 → 5285.26] After much.
[5285.70 → 5286.58] I was thinking about.
[5286.66 → 5286.82] You know.
[5286.82 → 5287.92] Having you read one of them at least.
[5288.02 → 5288.34] But I am.
[5288.44 → 5289.26] I'm not going to do that.
[5289.70 → 5291.92] Well let's start with the only guy who.
[5292.28 → 5293.30] Went his own way.
[5293.84 → 5294.06] Yeah.
[5294.60 → 5295.26] Just like.
[5295.92 → 5296.66] The old song.
[5296.72 → 5297.82] You can go your own way.
[5298.46 → 5299.80] But it's going to be a lonely day.
[5299.82 → 5300.28] Thomas.
[5300.42 → 5301.34] It's a lonely day.
[5301.80 → 5303.36] Sitting over there on Taylor's.
[5303.70 → 5304.82] Purposefully accelerating.
[5305.70 → 5306.14] Civilizational.
[5306.90 → 5307.34] Collapse.
[5307.94 → 5308.98] One point for Taylor.
[5309.42 → 5310.28] Which just had.
[5310.40 → 5310.78] Like it had.
[5310.86 → 5312.04] You already said accelerating.
[5312.24 → 5313.02] Like that's acceleration.
[5313.20 → 5313.78] You did it.
[5314.16 → 5315.02] You fully did it.
[5315.92 → 5316.44] Accelerationist.
[5318.18 → 5318.62] Accelerationist.
[5319.02 → 5320.68] And then everybody else just piled on to.
[5320.76 → 5322.48] Marked by tremendous size.
[5322.56 → 5323.48] Which is an adjective.
[5323.76 → 5325.30] Even though Matthew was looking for nouns.
[5325.36 → 5326.22] He couldn't find one.
[5326.76 → 5328.00] It feels like a place.
[5328.80 → 5329.24] And.
[5329.58 → 5330.28] That's because.
[5330.54 → 5331.38] Brobdingnag.
[5331.46 → 5332.22] Is a place.
[5332.34 → 5333.60] It's a fictional place.
[5333.84 → 5335.12] In Gulliver's travels.
[5335.12 → 5336.58] Where Gulliver goes.
[5337.60 → 5337.90] Yeah.
[5337.90 → 5338.10] And.
[5338.34 → 5338.94] With the blobs.
[5338.94 → 5341.04] In Brobdingnag.
[5341.20 → 5343.40] Are marked by tremendous size.
[5343.58 → 5344.28] And so they.
[5345.08 → 5345.52] There you go.
[5345.52 → 5346.74] They're Brobdingnagians.
[5347.00 → 5348.00] And so everybody who picked.
[5348.82 → 5349.22] That.
[5349.36 → 5349.96] Gets two.
[5350.40 → 5351.72] I just think of like the Spider-Man movie.
[5351.84 → 5352.64] When he lands in like.
[5352.84 → 5353.70] The Netherlands or something.
[5354.28 → 5354.76] Where are you?
[5355.18 → 5355.94] And he like says.
[5356.50 → 5357.54] The name of the town.
[5358.22 → 5359.20] And it's like some.
[5359.94 → 5361.68] I don't know what language they really speak there.
[5361.70 → 5361.96] But it was.
[5362.08 → 5363.08] It reminds me of that word.
[5363.60 → 5364.78] What language they speak there.
[5365.00 → 5365.36] I don't know.
[5365.36 → 5366.82] What is the town name?
[5367.26 → 5367.96] A couple of shout-outs.
[5368.02 → 5368.60] I have no idea.
[5368.90 → 5369.72] What you're referring to.
[5369.80 → 5370.26] I'm going to get it.
[5370.36 → 5370.90] I'm going to get it.
[5371.08 → 5371.32] All right.
[5371.34 → 5371.76] You think.
[5372.32 → 5373.18] A couple of shout-outs.
[5373.28 → 5373.88] Backyardigans.
[5374.02 → 5374.58] That was Adam.
[5375.52 → 5376.74] Golden Sun was Matthew.
[5377.46 → 5379.82] Does anybody know Golden Sun besides yourself Matthew?
[5380.02 → 5380.18] That was.
[5380.34 → 5380.54] I know.
[5380.62 → 5381.16] I played it.
[5381.32 → 5382.24] It was a good game.
[5382.50 → 5382.78] Okay.
[5383.08 → 5384.02] And then of course.
[5384.26 → 5385.72] The Bobsleding was Thomas.
[5385.72 → 5389.78] Which was funny because somebody immediately thought Taylor wrote that one.
[5390.66 → 5393.12] But Taylor said it was too smart for him or something.
[5393.92 → 5395.54] I'm surprised no one chose the.
[5397.38 → 5398.30] Bob Partisans.
[5399.60 → 5400.38] Whatever they're called.
[5401.66 → 5402.16] What a shame.
[5402.16 → 5402.72] Brobdingnagians.
[5403.36 → 5403.92] Brobdingnagians.
[5404.14 → 5404.28] Yeah.
[5404.28 → 5408.96] So after six rounds of play, we do have winners.
[5410.28 → 5411.86] We also have hard stops.
[5412.14 → 5414.10] So we'll have to decide what we're going to do here because.
[5414.24 → 5414.80] People have won?
[5415.26 → 5418.02] Taylor and Matthew both have 13 points.
[5418.08 → 5420.02] Put them over the 12 point threshold.
[5420.20 → 5421.08] David has 12.
[5421.16 → 5423.40] Putting them at the 12 point threshold.
[5423.60 → 5427.00] So we can end the game with a two-way tie for first.
[5427.16 → 5429.78] I know that Thomas has to wrap.
[5429.88 → 5432.54] I think everybody has dinner to have at a certain point.
[5433.28 → 5434.18] We can call it.
[5434.26 → 5434.96] We can continue.
[5435.28 → 5436.22] We can go without Thomas.
[5436.62 → 5437.08] We can just.
[5437.08 → 5438.38] I'm not going to win this one.
[5438.54 → 5440.52] So I can back out.
[5440.70 → 5441.66] Go walk my dog.
[5441.88 → 5444.54] Let's talk to our two guys tied for first place.
[5444.54 → 5445.24] Taylor and Matthew.
[5445.34 → 5446.20] How would you like to proceed?
[5446.80 → 5447.48] I don't have a preference.
[5447.62 → 5448.70] We can tie it.
[5448.82 → 5449.96] We can tie-break it.
[5450.10 → 5450.56] We can.
[5451.72 → 5452.08] Whatever.
[5453.38 → 5455.16] I have more rounds in my back pocket.
[5455.32 → 5456.22] So that's not a problem.
[5456.74 → 5457.24] Let me think.
[5457.42 → 5458.66] I am starving.
[5458.66 → 5466.66] Let's just call it a two-way tie for first.
[5467.08 → 5467.62] Oh boy.
[5468.52 → 5469.82] We've been playing a long time.
[5469.92 → 5472.16] So let's just congratulate our two winners.
[5473.18 → 5473.32] Oh.
[5474.20 → 5474.68] All right.
[5476.48 → 5478.04] I thought you were going to say something.
[5478.60 → 5479.02] Oh yeah.
[5479.04 → 5479.26] Sorry.
[5479.40 → 5480.60] I think I lagged.
[5480.66 → 5480.98] I was going to say,
[5481.04 → 5481.86] or we flip a coin,
[5482.00 → 5482.18] right?
[5482.28 → 5484.72] Like flip a coin.
[5485.16 → 5485.84] I have an idea.
[5486.24 → 5487.10] You both see,
[5487.26 → 5487.96] go back and forth.
[5488.02 → 5489.38] Who can name more words?
[5489.68 → 5492.38] Whoever runs out of words first loses.
[5493.56 → 5495.58] I would definitely lose that one easily.
[5496.26 → 5498.28] Sounds like counting from one to a million.
[5498.76 → 5499.02] Yeah.
[5499.42 → 5499.86] One,
[5500.06 → 5500.24] two,
[5500.52 → 5500.72] three.
[5501.38 → 5501.48] Is,
[5501.64 → 5504.02] you don't have another tiebreaker thing that we can do,
[5504.22 → 5504.36] Jared?
[5504.78 → 5505.28] I'm thinking.
[5505.70 → 5507.92] You can do a live Google thing.
[5508.28 → 5509.64] I do have another Goo ground.
[5509.74 → 5510.92] We could just have the two of you.
[5511.16 → 5512.02] Where we just guess.
[5512.74 → 5515.92] We both just like guess on three or something.
[5516.70 → 5520.02] And whoever's guess is higher in the Google rank wins or something.
[5520.34 → 5521.18] On the fly.
[5521.54 → 5522.28] Oh my goodness.
[5523.16 → 5525.84] Ask Google to generate a number between zero and one.
[5528.04 → 5529.22] We could also do that.
[5530.02 → 5530.40] All right.
[5530.46 → 5531.74] I'm pulling up Google right now.
[5531.90 → 5533.38] Who's the changelog plus subscriber?
[5533.80 → 5533.92] No,
[5533.92 → 5534.32] I'm just kidding.
[5534.32 → 5537.14] Oh yeah.
[5537.78 → 5538.18] No,
[5538.24 → 5538.68] just kidding.
[5539.36 → 5539.72] Okay.
[5539.76 → 5540.68] So I'm going to pull up Google.
[5540.80 → 5542.20] I'm going to start typing in autocomplete.
[5542.30 → 5543.06] I'm going to stop.
[5543.62 → 5545.26] And then you guys will guess.
[5546.70 → 5550.28] Until somebody hits the top autocomplete and the person who hits it wins.
[5551.54 → 5552.62] You guys cool with that?
[5553.68 → 5553.98] Sure.
[5554.16 → 5554.30] Love it.
[5555.38 → 5555.76] All right.
[5555.78 → 5557.80] I have typed Bill Gates space,
[5557.98 → 5558.86] not space needle,
[5559.28 → 5561.26] but a literal blank character.
[5561.26 → 5563.26] Bill Gates space.
[5564.32 → 5565.00] And,
[5565.16 → 5565.56] uh,
[5565.56 → 5568.04] the first one to hit it wins.
[5568.28 → 5569.22] So how do we,
[5569.42 → 5571.72] how should we start with the changelog plus member?
[5572.06 → 5572.92] Who's Matthew?
[5573.92 → 5575.20] But I'm not a change.
[5575.56 → 5576.38] Oh shoot.
[5577.30 → 5578.18] I thought you were.
[5578.52 → 5579.70] I thought I was too,
[5579.76 → 5580.06] but I,
[5580.12 → 5580.62] you know,
[5581.06 → 5582.00] I just listen so much.
[5582.36 → 5583.22] We start with Taylor.
[5584.96 → 5586.06] I'm now offended.
[5587.02 → 5588.34] I'll start with Taylor.
[5588.46 → 5588.56] Yeah.
[5588.56 → 5589.40] David is one.
[5589.40 → 5589.68] Um,
[5590.00 → 5591.52] but he's also missing a point.
[5591.96 → 5592.18] Yeah.
[5592.20 → 5593.10] We'll start with Matthew.
[5593.10 → 5593.84] I'm not,
[5594.08 → 5594.96] I'm not easily offended.
[5595.50 → 5596.16] Go ahead,
[5596.24 → 5596.40] man.
[5597.10 → 5598.10] It's better though.
[5598.66 → 5598.82] All right.
[5598.82 → 5599.88] So just say one.
[5600.28 → 5600.80] Yeah.
[5600.82 → 5601.16] What do you think?
[5601.20 → 5603.48] Bill Gates autocompletes to net worth.
[5603.82 → 5604.64] It's on there,
[5604.68 → 5605.44] but it's not number one.
[5605.64 → 5605.98] Okay.
[5606.42 → 5606.70] Taylor.
[5607.70 → 5608.26] Feet.
[5608.26 → 5610.72] Is it Bill Gates versus Godzilla?
[5610.90 → 5611.08] That,
[5611.08 → 5611.30] that,
[5611.30 → 5613.50] that should probably be up in the top five.
[5613.58 → 5613.70] No,
[5613.74 → 5614.30] let's go with,
[5614.44 → 5614.74] uh,
[5615.42 → 5616.38] Bill Gates.
[5617.32 → 5618.02] It's feet,
[5618.12 → 5618.48] man.
[5618.98 → 5621.96] It's the blanks already in there.
[5622.04 → 5623.48] What keeps on coming up to me is like the
[5623.48 → 5625.40] the Bill Gates Epstein situation.
[5625.40 → 5628.64] Cause there was a tie there or something in Bill Gates Epstein to be real topical.
[5628.74 → 5628.96] Maybe.
[5629.08 → 5629.34] Okay.
[5630.46 → 5630.76] Okay.
[5630.90 → 5631.26] Nope.
[5631.76 → 5632.16] Matthew.
[5632.16 → 5633.64] Good try.
[5634.14 → 5634.46] Uh,
[5634.48 → 5635.26] what is Bill Gates even?
[5635.46 → 5637.30] What is he known for now anymore?
[5637.64 → 5639.36] Who cares to Google him?
[5640.68 → 5642.34] He wasn't in the news recently.
[5643.06 → 5644.22] Was he in the news recently?
[5644.46 → 5644.70] Yeah.
[5644.70 → 5645.68] I don't care about Bill Gates.
[5646.10 → 5646.60] I don't either.
[5646.64 → 5647.50] I just know he's in the news.
[5647.78 → 5648.52] What does he do?
[5649.04 → 5651.98] Isn't he like involved in like farm stuff now?
[5652.60 → 5654.20] He's bought a bunch of farmland.
[5654.38 → 5655.32] That's what I thought.
[5657.62 → 5658.50] David's chomping the bit.
[5658.54 → 5659.24] Because he knows,
[5659.40 → 5660.38] he knows what this is about.
[5660.46 → 5660.92] And he's like,
[5660.94 → 5661.92] I was one point away.
[5661.92 → 5662.90] I could be in this.
[5663.62 → 5664.30] The answer's feet.
[5664.42 → 5664.56] Yeah.
[5664.58 → 5664.92] Okay.
[5665.06 → 5665.86] You're missing out.
[5665.98 → 5666.94] Bill Gates feet.
[5669.32 → 5671.14] I feel like if it's not worth,
[5671.88 → 5674.04] I'd laugh if it was like the other one,
[5674.12 → 5675.08] what was the other Google one?
[5675.36 → 5677.06] I would laugh if it was the same thing,
[5677.16 → 5678.38] the same Google things.
[5678.56 → 5679.30] Cause you put two names,
[5679.38 → 5679.54] right?
[5679.72 → 5680.18] Steve Jobs,
[5680.26 → 5680.50] daughter.
[5681.50 → 5682.50] Bill Gates.
[5685.60 → 5686.00] Okay.
[5686.06 → 5686.78] I think I would guess.
[5687.62 → 5689.42] Isn't he a big proponent of like,
[5689.96 → 5690.82] I don't even know.
[5691.10 → 5691.38] Okay.
[5691.38 → 5692.26] Give me a timer.
[5693.60 → 5694.52] Time to count down something.
[5694.60 → 5695.42] It'll force something out of me.
[5695.78 → 5695.96] Three,
[5696.20 → 5697.20] two,
[5697.44 → 5697.98] one.
[5698.72 → 5698.96] Okay.
[5699.36 → 5700.22] Climate change.
[5700.84 → 5702.88] Doesn't need to do something with farms and climate change.
[5702.88 → 5704.04] Bill Gates climate change.
[5704.36 → 5704.66] Yeah.
[5705.10 → 5705.30] Ding,
[5705.36 → 5705.50] ding,
[5705.56 → 5705.74] ding,
[5705.74 → 5706.00] ding,
[5706.00 → 5706.10] ding,
[5706.10 → 5706.12] ding,
[5706.12 → 5706.30] ding.
[5706.30 → 5707.68] You got it,
[5707.74 → 5707.98] man.
[5708.32 → 5710.56] Bill Gates climate change.
[5710.68 → 5711.24] Matthew.
[5711.72 → 5712.44] I just remember.
[5712.84 → 5714.72] Of nowhere is our winner.
[5715.64 → 5716.24] David knew that.
[5716.24 → 5716.60] I,
[5716.88 → 5720.68] my wife told me a bunch that he like bought up a lot of farmland, and I was like,
[5720.68 → 5721.60] trying to do these things.
[5722.06 → 5725.02] He was in the news recently because he commented on climate change.
[5725.06 → 5725.96] I can't remember what he said,
[5726.00 → 5728.20] but it seems like he had softened his position, or he said,
[5728.24 → 5729.74] it's not going to kill everybody or something.
[5729.80 → 5731.36] We're just going to have to learn to live with it.
[5731.62 → 5731.90] Yeah.
[5732.14 → 5732.46] Really?
[5733.02 → 5733.34] Yeah.
[5733.34 → 5733.66] Yeah.
[5735.04 → 5736.00] Oh my God.
[5736.40 → 5736.56] Yeah.
[5736.62 → 5737.66] So people are Googling it up.
[5738.02 → 5738.82] That's wild.
[5739.34 → 5739.68] All right.
[5739.70 → 5739.88] Well,
[5739.88 → 5741.30] it was a weird tiebreaker,
[5741.46 → 5742.62] but it was a tiebreaker nonetheless.
[5743.06 → 5743.44] And Taylor,
[5743.56 → 5744.04] I'm sorry,
[5744.42 → 5746.96] but Matthew just eked you out.
[5747.26 → 5747.38] David,
[5747.42 → 5749.26] was that what you were going to guess was climate change or did you have
[5749.26 → 5750.18] something else up your sleeve?
[5750.64 → 5750.96] I was,
[5751.68 → 5751.86] I,
[5752.00 → 5755.42] the other thing that was like relatively newsy about him recently would have
[5755.42 → 5756.88] been something about like,
[5757.22 → 5760.94] I think the last thing he said was something about how he,
[5760.94 → 5765.26] people can't expect his donations to step in for all the work the federal
[5765.26 → 5766.42] government isn't doing anymore.
[5766.88 → 5769.80] So it would have been something about that or his foundation.
[5770.16 → 5771.22] I wanted to say foundation,
[5771.64 → 5772.94] but like if net worth wasn't there,
[5773.02 → 5774.60] I figured foundation wasn't going to be up.
[5775.04 → 5775.32] Can I,
[5775.38 → 5777.98] can I change my answer to Bill Gates net worth?
[5778.32 → 5778.54] Can I,
[5778.60 → 5779.06] can I do that?
[5779.66 → 5780.06] Sure.
[5781.44 → 5782.80] On the Steve Jobs question,
[5782.86 → 5783.10] are you,
[5783.22 → 5784.22] are you on this one now?
[5784.54 → 5785.86] Can you read the ones that were there?
[5786.00 → 5786.40] Bill Gates,
[5786.46 → 5787.00] climate change.
[5787.02 → 5787.36] Number one,
[5787.42 → 5788.36] Bill Gates net worth,
[5788.36 → 5788.94] Bill Gates,
[5789.02 → 5789.98] climate change pivot.
[5790.14 → 5790.86] Number three,
[5791.22 → 5792.00] Bill Gates daughter.
[5792.46 → 5793.26] I don't even know.
[5793.30 → 5793.92] Does he have a daughter?
[5794.02 → 5795.26] Bill Gates daughter is number four.
[5795.42 → 5795.96] That's hilarious.
[5796.36 → 5796.60] Yeah.
[5796.68 → 5798.38] And then you get into Bill Gates age,
[5798.50 → 5799.42] Bill Gates memo,
[5799.56 → 5800.28] climate change,
[5800.40 → 5801.10] Bill Gates wife,
[5802.00 → 5803.66] and then you get down to Bill Gates quotes.
[5804.26 → 5806.00] So I feel like daughter and wife are always,
[5806.14 → 5806.70] no matter what,
[5806.70 → 5807.04] like,
[5807.22 → 5808.10] I think people are just curious.
[5808.32 → 5808.40] Like,
[5808.44 → 5809.40] does this person have a daughter?
[5809.58 → 5810.40] Does this person have a wife?
[5810.58 → 5810.70] Yeah.
[5810.78 → 5810.90] Yeah.
[5811.22 → 5811.46] Do you,
[5811.54 → 5816.20] now I just need to grow my blog big enough where people are searching Taylor
[5816.20 → 5818.12] Trash daughter,
[5818.34 → 5818.64] wife,
[5818.78 → 5818.96] you know,
[5819.00 → 5819.26] that's,
[5819.26 → 5820.42] that's when you know you make it,
[5820.48 → 5820.74] you know,
[5821.16 → 5821.42] yeah,
[5821.42 → 5821.62] yeah,
[5821.62 → 5821.92] yeah.
[5822.76 → 5824.46] Let me pull up my Google thing now.
[5824.76 → 5825.42] Oh gosh.
[5825.70 → 5826.80] What are people saying?
[5827.12 → 5827.80] This is funny.
[5828.48 → 5830.78] The number one is Taylor Trash,
[5830.88 → 5832.70] which I already typed then Taylor Trash LinkedIn.
[5832.70 → 5834.90] And then did Taylor and Taylor date?
[5835.22 → 5835.50] Oh,
[5835.74 → 5836.48] that's a good one.
[5836.70 → 5837.54] And then Taylor Smith,
[5837.66 → 5838.24] Taylor history.
[5838.42 → 5839.04] So it's just moving.
[5839.28 → 5839.54] Yeah.
[5839.58 → 5839.96] It's just,
[5839.96 → 5841.50] how far is Taylor?
[5841.66 → 5844.24] I think it's a good question.
[5844.38 → 5845.40] Where is Taylor town?
[5845.40 → 5847.02] Is it improve ding dang?
[5847.02 → 5849.52] I don't get close.
[5849.52 → 5852.46] I don't get any auto completes.
[5852.58 → 5853.22] I'm not famous.
[5853.68 → 5853.92] Yeah.
[5854.00 → 5854.50] Me either.
[5854.74 → 5855.68] Taylor's the coolest one.
[5855.78 → 5856.86] So I have a confession to make.
[5857.12 → 5857.76] What's that?
[5858.00 → 5859.30] And I'm super sad about it.
[5859.30 → 5860.98] I was,
[5861.10 → 5861.56] you know,
[5861.56 → 5862.04] like when you,
[5862.16 → 5865.58] when you play spades, or you got perfect cards at the wild card,
[5865.64 → 5865.98] when you're playing,
[5866.10 → 5866.42] you know,
[5866.42 → 5866.68] you know,
[5866.68 → 5868.88] and you wait, and you're like,
[5868.94 → 5869.08] Oh,
[5869.08 → 5869.44] this is,
[5869.54 → 5871.12] is this a good time to use my,
[5871.28 → 5872.54] my good thing?
[5872.78 → 5873.14] Right.
[5873.54 → 5873.72] Yeah.
[5873.72 → 5874.54] I just waited too long.
[5874.58 → 5875.50] I never used the LLM.
[5875.92 → 5876.96] So sad about that.
[5877.04 → 5879.26] I was going to use it when I thought I had,
[5879.34 → 5879.62] you know,
[5879.62 → 5882.42] a good score to get right at the very end,
[5882.44 → 5883.72] like a trunk card kind of thing.
[5884.72 → 5885.08] Yeah.
[5885.54 → 5885.90] Sadly.
[5887.80 → 5888.48] I failed.
[5888.92 → 5889.10] Well,
[5889.12 → 5891.24] we'll let you hold on to that for the next time you play.
[5891.70 → 5892.68] So I can get two next time.
[5892.76 → 5893.88] I'll put that two LMs.
[5894.08 → 5894.40] Sure.
[5894.88 → 5895.16] Sure.
[5895.56 → 5896.14] I'll give you two.
[5896.26 → 5896.62] I like it.
[5896.62 → 5897.54] I can use them anyway.
[5897.96 → 5898.14] Does,
[5898.22 → 5901.74] does Matt get a free changelog plus,
[5901.74 → 5902.10] Matt,
[5902.10 → 5904.02] a subscription for winning?
[5904.46 → 5905.10] That's right.
[5905.44 → 5905.70] Yep.
[5906.20 → 5906.36] Well,
[5906.36 → 5907.26] tell him where it's at.
[5907.80 → 5909.28] And then it's,
[5909.46 → 5910.26] that's free information.
[5910.52 → 5912.58] Change log.com slash plus.
[5913.34 → 5914.40] They say it's better.
[5915.10 → 5915.62] All right,
[5915.64 → 5915.76] you all.
[5915.84 → 5916.40] Thanks for playing.
[5916.60 → 5918.48] This has been too much fun.
[5918.80 → 5920.28] I feel like it was too competitive,
[5920.58 → 5923.08] almost too conservative because of the competition level.
[5923.14 → 5927.60] We got to bring in some more loose goose folks who are willing to guess the funny ones,
[5927.70 → 5931.02] but you all are invited back as well.
[5931.02 → 5932.46] And Matthew,
[5932.56 → 5933.52] the champion of champions.
[5933.68 → 5933.92] I mean,
[5934.14 → 5934.92] how does it feel?
[5935.30 → 5936.22] I feel with my hands.
[5936.28 → 5936.44] Thanks.
[5936.84 → 5936.98] No,
[5937.14 → 5938.38] it feels good.
[5938.48 → 5938.80] We should,
[5938.90 → 5940.84] we should definitely change the rules of pylons though.
[5940.86 → 5941.96] It's easy to pile on.
[5942.02 → 5943.58] So like you're hedging your bet really,
[5943.88 → 5944.30] really well.
[5944.86 → 5946.02] It is a smart choice.
[5946.42 → 5946.68] Right.
[5946.68 → 5946.94] We should,
[5946.94 → 5947.94] we should think about that.
[5948.12 → 5948.30] Sure.
[5948.30 → 5949.34] Think about fixing that.
[5949.40 → 5950.18] The problem is,
[5950.72 → 5950.98] yeah,
[5950.98 → 5954.28] there needs to be more better answers because then you'll pile on the wrong one, and I'll
[5954.28 → 5954.88] get some points.
[5955.06 → 5955.22] But so,
[5955.40 → 5955.50] yeah,
[5955.56 → 5955.92] like the
[5955.92 → 5957.32] the Rob ding,
[5957.46 → 5960.18] getting in something like every,
[5960.18 → 5962.22] it's not that I think it was the size,
[5962.22 → 5963.56] but like every other answer was,
[5963.56 → 5964.30] was wrong.
[5964.36 → 5965.92] And then I was left between my answer.
[5966.00 → 5967.36] So it's really the right answer.
[5967.56 → 5969.26] It's really your guy's fault is my point,
[5969.42 → 5969.66] you know?
[5969.68 → 5969.84] Yeah,
[5969.88 → 5970.12] it is.
[5970.22 → 5970.56] We're not,
[5970.70 → 5971.82] we're insufficiently creative.
[5972.14 → 5974.82] So this one was actually tough to be more funny too.
[5974.86 → 5976.38] Like I usually come up with more funny stuff.
[5976.38 → 5976.94] So listeners,
[5977.06 → 5978.56] I probably disappoint them a little bit.
[5978.66 → 5978.90] Yeah.
[5979.02 → 5979.32] Yeah.
[5979.32 → 5982.22] Except for the backyard against a cousin version.
[5982.32 → 5982.50] Yeah,
[5982.50 → 5982.98] that was cool.
[5983.08 → 5983.58] I like that one.
[5984.32 → 5984.64] Yeah.
[5984.74 → 5985.94] I was waiting for you to read it,
[5986.02 → 5986.10] Jared.
[5986.16 → 5986.98] I want to see your face.
[5987.26 → 5988.84] Taylor played it way straighter than he normally does.
[5988.92 → 5989.02] You know,
[5989.02 → 5990.06] I think he was really trying to win.
[5990.28 → 5992.70] Normally his answers are just preposterous,
[5992.82 → 5994.20] but a lot of,
[5994.32 → 5995.94] a lot of good answers coming out of Taylor.
[5996.96 → 5997.32] Yeah.
[5997.38 → 5997.68] I think,
[5997.76 → 5997.92] I mean,
[5997.92 → 5998.44] the other,
[5998.74 → 6003.34] the other way to sort of rebalance the game is to,
[6003.44 → 6004.52] because is to,
[6004.60 → 6005.80] if,
[6006.76 → 6008.96] if everyone has to choose simultaneously,
[6009.32 → 6010.34] like the results.
[6010.34 → 6010.58] So,
[6010.70 → 6010.94] you know,
[6010.96 → 6012.76] you kind of submit them essentially like,
[6013.20 → 6013.32] yeah.
[6013.40 → 6013.48] So,
[6013.60 → 6013.80] right.
[6013.92 → 6015.04] So that we're not actually here.
[6015.12 → 6015.62] The logic.
[6015.96 → 6016.08] Yeah.
[6016.08 → 6016.24] Yeah.
[6016.62 → 6016.82] Yeah.
[6016.82 → 6019.82] Because Thomas was really picking it apart and given all of his logic out
[6019.82 → 6023.08] early, and he actually did logic his way to the right answer.
[6023.08 → 6024.16] But then everyone's just like,
[6024.40 → 6024.50] yeah,
[6024.52 → 6025.26] I'm going to go with that one.
[6025.94 → 6026.30] So,
[6026.46 → 6026.70] yeah.
[6028.22 → 6030.74] Most people hold those thoughts inside and just guess,
[6030.90 → 6031.32] I think,
[6031.44 → 6032.94] but he was really explaining his thought,
[6033.00 → 6034.56] which I appreciate as a guy just listening,
[6034.90 → 6035.22] you know,
[6035.26 → 6038.52] but you guys apparently appreciate it as well.
[6038.52 → 6039.64] He had some good definitions too.
[6039.70 → 6041.80] He is just like repeated the words,
[6042.00 → 6042.32] like water,
[6042.44 → 6042.74] water,
[6043.02 → 6043.36] accelerate,
[6043.48 → 6044.00] accelerate it.
[6044.10 → 6044.28] Yeah.
[6044.52 → 6045.04] By the way,
[6045.10 → 6045.74] to our listeners,
[6046.02 → 6046.72] Thomas had a bounce.
[6046.80 → 6048.62] That's why we're talking about him and not talking to him.
[6048.66 → 6050.82] It'd be weird if he was still here, and we're just talking about him.
[6051.60 → 6053.72] It's kind of weird talking about him with a knot here,
[6053.86 → 6054.82] but shout out to Thomas.
[6055.20 → 6055.56] Excellent.
[6055.98 → 6056.26] Excellent.
[6056.44 → 6058.42] Played round of pound to fine.
[6058.76 → 6060.80] And I thought everybody played well.
[6061.06 → 6062.22] Thanks for joining us guys.
[6062.68 → 6062.90] Yeah.
[6063.88 → 6064.60] My friends.
[6065.12 → 6065.62] Bye Taylor.
[6065.74 → 6066.14] Bye Matthew.
[6066.22 → 6066.80] Bye David.
[6066.80 → 6067.66] Bye Thomas.
[6067.66 → 6068.66] Bye me.
[6069.04 → 6071.88] We'll see if we can get Carol to come up and kick all your guys' butts next time around.
[6072.10 → 6072.40] Come on,
[6072.50 → 6072.74] Carol.
[6073.00 → 6073.76] Get back over here.
[6073.84 → 6074.14] Carol.
[6074.94 → 6075.50] Carol Lee,
[6075.64 → 6076.02] PhD.
[6076.32 → 6076.64] Bye you all.
[6077.14 → 6077.34] Bye.
[6079.42 → 6080.42] There you have it.
[6080.46 → 6082.72] Our seventh iteration of pound to fine.
[6083.04 → 6086.86] If you like these game show style episodes that we sprinkle in from time to time,
[6086.92 → 6090.92] you can find them all at change log.com slash topic slash games.
[6091.12 → 6093.14] There's also a Spotify playlist.
[6093.30 → 6094.22] If that's your bag,
[6094.22 → 6095.92] it's called dev game shows.
[6095.92 → 6096.54] Oh,
[6096.62 → 6098.36] and if you do enjoy these and want to hear more,
[6098.50 → 6099.90] let us know in the comments.
[6100.14 → 6103.26] We just kind of assume that since we're nerds, and you're nerds,
[6103.46 → 6104.86] you probably like what we like,
[6105.10 → 6107.06] but a little validation goes a long way.
[6107.16 → 6108.38] So please do hit us up.
[6108.50 → 6109.58] We love to hear from you.
[6109.94 → 6113.30] Thanks again to our partners at fly.io and to our beat freak,
[6113.30 → 6113.96] the mysterious,
[6114.22 → 6114.74] the groovy,
[6114.98 → 6115.66] the beefiest,
[6115.80 → 6118.48] speediest beat master in the entire verse.
[6118.84 → 6120.06] You know who I'm talking about.
[6120.22 → 6120.86] Break master cylinder.
[6121.38 → 6123.22] Next week on the pod news on Monday,
[6123.48 → 6124.84] hacker news is favourite blogger,
[6125.02 → 6127.18] Sean Geese on Wednesday and on Friday.
[6127.44 → 6127.74] Well,
[6127.92 → 6130.14] our San Francisco trip fell by the wayside.
[6130.24 → 6131.56] So we're still working on that.
[6131.78 → 6132.98] We're open to suggestions,
[6133.60 → 6134.76] have yourself a great weekend.
[6134.90 → 6138.94] There's safety in a multitude of counsellors and let's talk again real soon.
[6138.94 → 6159.84] Game on.
