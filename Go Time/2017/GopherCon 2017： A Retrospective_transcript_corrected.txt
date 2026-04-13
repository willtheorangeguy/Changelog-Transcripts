[0.00 → 2.98] Bandwidth for Changelog is provided by Vastly.
[3.46 → 5.50] Learn more at Fastly.com.
[5.82 → 7.58] And we're hosted on Linde servers.
[7.96 → 10.14] Head to linode.com slash changelog.
[21.84 → 27.12] It's Go Time, a weekly podcast where we discuss interesting topics around the Go programming language,
[27.38 → 29.08] the community, and everything in between.
[29.08 → 33.58] If you currently write Go or aspire to, this is the show for you.
[43.84 → 47.24] All right, everybody, welcome back to another episode of Go Time.
[47.40 → 50.06] Today's episode is number 53.
[50.94 → 54.44] So on the show today, we have myself, Eric St. Martin.
[55.12 → 57.02] Galicia Pinto is also on the show.
[57.52 → 58.14] Hi, everybody.
[58.14 → 58.24] Hi, everybody.
[58.52 → 59.94] And Brian Kettle son.
[60.44 → 60.86] Hello.
[61.72 → 67.70] And it seems like something big just happened a couple of weeks ago that we should spend this
[67.70 → 68.56] episode talking on.
[69.02 → 69.62] I know what it is.
[70.06 → 71.12] I dyed my hair purple.
[71.88 → 75.18] Do you think we could fit a whole hour to talk about that?
[75.32 → 77.70] I think we could talk about that for at least three or four.
[78.26 → 80.24] I think we could talk about it for quite a while.
[80.24 → 80.28] Wow.
[80.60 → 85.06] It's amazing just how much feedback I've gotten on it from random strangers.
[85.22 → 86.22] High fives in airports.
[86.46 → 86.82] I'm serious.
[86.92 → 87.40] It's crazy.
[89.20 → 93.22] Most of them are thinking that guy is too old to have purple hair, so let's high five
[93.22 → 94.14] him and make him feel better.
[94.22 → 94.82] But hey, whatever.
[95.96 → 98.08] Are you getting selfie pictures too?
[98.84 → 99.94] Yes, actually.
[100.36 → 103.88] In fact, it happened at Gopher Con, which is I know what you were really meaning to talk
[103.88 → 105.64] about the thing that happened a couple of weeks ago.
[105.64 → 107.70] So, but I suppose we could talk about that.
[108.30 → 113.22] We were outside next to the bear and some kid walks up with purple hair, and he goes,
[113.66 → 116.38] is it okay if my mom takes a picture with you and me together?
[116.54 → 117.48] I was like, heck yeah.
[119.88 → 121.22] I love it, by the way.
[121.82 → 122.84] I think it's fun.
[123.56 → 124.38] I think so too.
[125.38 → 131.70] So, um, for anybody who's not aware, um, back, uh, as we're recording this today on the
[131.70 → 133.22] 3rd of August.
[133.22 → 140.06] So this is about two weeks ago, um, Gopher Con occurred, which is a very, very large, um,
[140.76 → 143.74] conference for the Go programming language, in case you're not already familiar.
[143.96 → 146.82] That happens in July, uh, every year.
[147.14 → 151.64] And, uh, we spent three days there, four if you conclude workshop days.
[152.16 → 157.18] So, uh, anybody want to talk about kind of like overall thoughts and just kind of feelings
[157.18 → 158.64] walking away, excitement?
[158.64 → 165.34] Man, we need to be more precise, like, because I don't know where to begin.
[166.06 → 166.50] Yeah.
[166.50 → 168.04] The energy level was insane.
[168.04 → 173.56] I mean, it was just constant high energy and everybody's just, everybody came up and
[173.56 → 178.24] told me specifically that, you know, they just felt like the energy this year was higher
[178.24 → 179.32] than any other year.
[179.32 → 183.22] And it just felt like such a fun happening, happy place to be.
[183.90 → 188.82] I can't gauge it anymore because it's my third one.
[188.98 → 192.30] And every year I go, I, I meet more people.
[192.64 → 196.88] So every year is more comfortable, and I don't know, okay, is it better because I know more
[196.88 → 200.94] people, which I, I like, or is it better because the conference is better?
[200.94 → 204.06] But I think this year it was patently both.
[204.24 → 206.70] The conference was at a higher level.
[207.36 → 210.00] Uh, the band was amazing.
[210.82 → 218.60] Uh, so a bunch of, uh, go developers who are also musician and singers got together and
[218.60 → 222.64] rehearsed and played at the pot at the opening party.
[222.64 → 225.60] And I felt like I was on drugs.
[226.14 → 227.60] I felt so happy.
[228.44 → 229.20] It's Denver.
[229.40 → 230.94] Are you sure you weren't on drugs?
[231.72 → 233.14] Yeah, I don't think I was.
[233.18 → 234.22] I was just drinking.
[234.74 → 235.38] Pretty sure.
[235.66 → 238.78] But I don't know because it's Denver, but I felt like it.
[239.08 → 246.18] And it just, it made me feel so happy looking at other goal developers who were also happy
[246.18 → 249.34] and dancing and having the greatest time.
[249.34 → 256.54] So thank you so much for everybody who played in that band and people who had the idea to
[256.54 → 259.88] put it together and approved the whole thing because it was awesome.
[260.48 → 263.08] Yeah, there were so many great people doing that.
[263.44 → 269.24] Um, so if you weren't at go for con, or you skipped the welcome party, what Galicia is talking
[269.24 → 276.12] about is, um, at the welcome party at the punch bowl social, uh, we had like a full, like
[276.12 → 279.76] fair level stage with lighting and stuff set up.
[280.02 → 285.00] And there was a local band there that, uh, kind of filled the air with music.
[285.32 → 291.32] But, um, later, um, a group of community members actually got up and sang and played instruments.
[291.32 → 295.76] And I wonder if I can name everybody off without missing anybody.
[296.32 → 297.36] It's going to be tough.
[297.62 → 300.08] There were a lot of people, but yeah.
[300.08 → 301.92] And Brian was also in the band.
[302.60 → 312.20] So, uh, and they got, yeah, Mark Bates, uh, Cassandra, uh, Salisbury, Vanessa, um, Chris
[312.20 → 312.58] Nova.
[313.58 → 315.04] Um, who else?
[315.76 → 316.88] Brian Downs.
[317.54 → 317.94] Yeah.
[318.12 → 319.12] Raj, Raj Pepe.
[319.88 → 320.20] Yeah.
[320.20 → 322.02] So it was, uh, JBD.
[322.58 → 323.18] JD.
[323.18 → 323.42] JD.
[323.92 → 327.64] So, and it was really awesome though, because everybody kind of got up there and performed in
[327.64 → 334.18] the band that was there, um, kind of backfilled positions that, uh, we didn't have community
[334.18 → 334.94] members for.
[335.26 → 338.80] And that was actually, um, Brian's idea to do the band thing.
[339.34 → 340.98] Wasn't Kyle in the band as well?
[341.06 → 341.90] I forgot his last name.
[342.40 → 343.04] From Denver.
[344.26 → 345.18] No, I don't know.
[345.32 → 346.24] No, no.
[347.18 → 347.40] Yeah.
[347.40 → 348.04] It was really great.
[348.10 → 353.02] And one of the things I loved about that, and I was telling, uh, it might've been, um,
[353.78 → 357.12] Adam, when they were doing the little change log interviews, I was talking about it.
[357.12 → 362.22] One of the things that I love the most about that is we often admire people for their technical
[362.22 → 364.46] abilities and, and everything.
[364.46 → 368.02] But we also forget that everybody kind of has hobbies and hidden talents.
[368.02 → 372.70] And it's really great to see a bunch of people, you know, share theirs with us.
[374.64 → 377.62] Let me also say that I'm a terrible introvert.
[378.06 → 380.24] And I had that realization after this.
[380.46 → 385.00] So this, a good, this is what a good introvert looks like.
[385.00 → 388.16] And I know this because I've seen one, Katrina Owen.
[388.32 → 393.16] Sometimes you see her at a conference, and she'll be walking away, walking out in the
[393.16 → 393.70] middle of the day.
[393.70 → 394.80] And you're like, where are you going?
[395.78 → 398.70] And she's like, I'm going to my hotel, and I'm going to rest.
[399.18 → 400.40] That's a good introvert.
[401.14 → 404.76] A bad introvert like me just keeps on going.
[405.04 → 406.96] And I just kept, you know, that's what I do.
[407.02 → 411.28] Every time I go to conference, I just keep going day, morning, day and night.
[411.28 → 415.38] And I don't, I don't, I don't ever say no to meeting somebody or having dinner or having
[415.38 → 415.88] drinks.
[416.72 → 419.20] Man, I was so exhausted when I came back.
[419.20 → 420.50] I couldn't even function.
[420.80 → 424.76] So next time I need to like take at least a couple of days off afterwards.
[425.64 → 426.82] I'm in that camp too.
[426.90 → 431.72] The bad introvert camp where I overwhelm myself a whole week.
[432.04 → 435.40] And then I go home, and it's like, nobody talked to me.
[435.40 → 437.02] Yeah, I'm in my cave.
[438.24 → 439.92] I need to, need to recharge.
[441.04 → 441.84] It's hard though.
[441.88 → 448.82] When you get that much interaction, that much social pressure condensed, and then you're done.
[448.86 → 450.28] It's just like, okay, I'm done.
[450.38 → 451.30] I don't want to talk to people.
[451.42 → 452.62] I don't want to talk to nobody.
[452.84 → 453.80] No, no, no, no, no.
[453.82 → 454.78] Just leave me alone.
[454.90 → 455.76] I'll be in my cave.
[456.58 → 461.44] And, you know, I don't, I don't know if there's a better way to deal with it, but it's certainly
[461.44 → 462.78] difficult for me.
[462.78 → 468.90] And one, one thing too, um, that I wanted to point out from an earlier point that Carly
[468.90 → 475.06] you see I made is this was kind of like the biggest, um, one yet, but yeah, I've, I felt
[475.06 → 475.72] a lot more.
[475.80 → 479.66] I don't want to say any of the prior years didn't have that tight-knit community feeling
[479.66 → 480.58] because they really did.
[481.20 → 484.34] Um, but I feel like it's getting even tighter.
[484.34 → 489.72] Like a lot of people I think felt like it'd get lost with, um, the growth.
[489.72 → 493.14] Uh, that's one of the things that they loved so much about the first year.
[493.64 → 498.90] But I think that a lot of the stuff is, is really kind of come back and so many people
[498.90 → 501.82] socializing and collaborating on stuff, especially community day.
[501.96 → 503.24] Community day was awesome.
[505.26 → 508.52] All of it was the, the, everything about it was just fantastic.
[509.44 → 512.28] My most memorable day was the day.
[512.34 → 514.56] I mean, it has nothing to do with the conference more about me.
[514.60 → 515.44] It is about me now.
[515.44 → 520.78] I had dinner twice in one night, one night.
[520.92 → 523.64] I had the women who go dinner, which I could miss of course.
[523.78 → 527.20] And then I had another dinner that I also didn't want to miss.
[527.22 → 527.98] I'm like, okay.
[527.98 → 533.30] So I eat, I eat two salads in one, and then I went and had a regular dinner afterwards.
[534.24 → 535.26] So yeah.
[535.40 → 537.20] Life is tough when you go to Alcorcón.
[537.20 → 541.18] I had a, um, never ending dinner one night.
[541.50 → 543.76] Uh, was it the first night?
[543.86 → 546.32] Uh, maybe I think it was workshop day.
[546.32 → 548.44] So the night most people came in travelling.
[549.14 → 554.92] Um, we were in the, uh, what's the name of the restaurant downstairs?
[555.22 → 556.38] The Buffalo burger place.
[557.04 → 558.20] Stout street social.
[558.36 → 563.68] Stout street social, which is directly across the street from the convention centre and downstairs
[563.68 → 568.82] from where a lot of us were staying, and we met a group of people that were there.
[569.02 → 572.86] Uh, I think Brian, you were part of the initial group, or maybe you weren't, but I don't know.
[572.88 → 575.74] There was like 10 or 15 people there, like this long table.
[576.00 → 581.72] And it was like, we were there for hours, and it was like a group would get up and a new group
[581.72 → 587.08] would join, and then they rotated out at least eight or nine times throughout the night.
[587.08 → 590.48] Like, I don't even know how many checks came, but it was kind of funny because we were just
[590.48 → 591.66] there basically all night.
[591.66 → 593.48] It was constantly new people.
[593.58 → 594.42] I didn't have to go anywhere.
[595.24 → 599.08] I came and went three times during the course of that, like six hours.
[599.16 → 600.36] You did come back.
[601.98 → 603.36] So yes, that was, I agree.
[603.42 → 604.72] That was the longest dinner ever.
[605.14 → 607.52] And every time I was surprised to see you there.
[608.90 → 610.30] Like you haven't bailed yet.
[611.62 → 616.04] So I mentioned the women who go dinner and that reminds me to talk about this.
[616.22 → 620.94] Um, we're definitely going to get to the talks and other things, but I want to mention
[620.94 → 625.38] about the diversity of efforts and how many women were there.
[625.62 → 629.16] I think it's safe to say that we had about 60 women.
[629.28 → 631.70] You guys can correct me at the conference.
[631.84 → 636.94] It was, uh, it was no, this year was the first year that it was noticeable that there were
[636.94 → 638.20] women at the conference.
[638.20 → 646.18] And there was such a big effort to increase the number of people with, from diverse backgrounds
[646.18 → 649.46] with the, uh, scholarships that we had.
[649.54 → 654.70] And I also realized some people didn't, who didn't go, who could have applied, didn't know
[654.70 → 655.24] about it.
[655.24 → 659.68] So heads up for next year is probably going to be a thing every year.
[660.14 → 667.70] So, uh, we have the conference and other organizations have funds to send people who wouldn't otherwise
[667.70 → 668.44] not be able to go.
[668.68 → 670.60] So make sure you keep an eye on that and apply.
[671.24 → 678.56] Uh, so we, from those applications, we got a bunch of people and the, the women who go
[678.56 → 682.24] dinner with specced, I think there were 50 women there.
[683.02 → 685.74] Uh, we got a nice gift from Azure.
[686.06 → 691.96] So the power charger thing, a portable charger, which it's not a flask.
[692.52 → 694.86] Shaw, it's an actual charger.
[695.44 → 696.98] No alcohol involved.
[697.36 → 699.00] It's not that kind of charger.
[699.56 → 701.64] Although that would have been welcome for me too.
[702.22 → 705.84] Uh, now that I think about it, I think I'm going to fix that problem.
[705.84 → 707.14] Because I don't have a flask anyway.
[707.74 → 714.82] Uh, so, and we had also the buddy system like there was before and people who have gone
[714.82 → 719.82] to the conference can sign up to be a guide and people who had never been to the conference
[719.82 → 721.56] can sign up to be a buddy.
[721.88 → 723.72] And we had a nice breakfast.
[723.92 → 728.98] Andy Walker led that effort, and he did such a great job, and we got beautiful pins.
[729.80 → 731.54] And, um, so we had breakfast.
[731.54 → 736.12] I got to meet, meet a bunch of people who I'd never heard of before.
[736.12 → 739.64] And some who I heard of online, but never met in person.
[739.86 → 741.10] It was beautiful.
[741.88 → 745.26] And it was great to see those people mingling in the conference as well.
[745.66 → 746.72] Uh, what else?
[747.06 → 749.22] You know, international travel too.
[749.40 → 754.86] I was really, so each year we know there's like many countries represented.
[755.06 → 758.74] I want to say this year was like 33 or something like that.
[758.74 → 763.74] And so I know the number of countries, but, um, at the beginning when Brian and I were
[763.74 → 769.20] doing like the welcome notes and like, I asked everybody to kind of sit down based on location
[769.20 → 771.50] and we got to the international people.
[771.66 → 774.62] I, I was not expecting that many people to still be standing.
[774.78 → 775.22] Yeah.
[775.42 → 777.58] Blown away by the international travel.
[778.28 → 782.08] So that's, it's a long flight to, uh, Denver.
[782.58 → 783.08] Yeah.
[783.10 → 787.38] We had a lot of, uh, international scholarship recipients.
[787.38 → 791.52] Uh, we had people from Brazil, from India, which was really cool.
[792.34 → 796.88] Oh, Nathan Youngman and the Slack channel, uh, brought up a good point too.
[796.98 → 802.14] At the very end, um, of the conference, we always have like leftover swag and stuff and
[802.14 → 803.08] we usually donate it.
[803.54 → 809.74] And, uh, this year, um, we decided to sell it to start pre-funding next year's diversity
[809.74 → 810.34] initiatives.
[810.34 → 813.98] And now I wish I had written down that figure.
[814.70 → 815.44] Um, exactly.
[815.44 → 816.70] It was over 12,000.
[816.94 → 820.92] Yeah, it was 12,000 and some change, um, that we raised already.
[821.34 → 822.32] So that's awesome.
[823.08 → 825.34] That is, that's a perfect seed for next year's diversity.
[826.12 → 827.10] So amazing.
[827.96 → 828.94] Thank you everyone.
[828.94 → 834.68] So speaking of Nathan Youngman, my, one of the most memorable moments of the conference
[834.68 → 840.86] was on the workshop day when I walked around a corner and I saw some really skinny Alton
[840.86 → 843.98] Brown looking guy standing at the water cooler.
[844.30 → 847.70] And it, I did a full on cartoon double take.
[847.86 → 850.42] And a moment later I said, is that you, Nathan?
[850.98 → 852.52] He has lost so much weight.
[852.56 → 853.28] It looks fantastic.
[853.28 → 857.92] I think we all need to give him a big round of applause for kicking ass and taking names
[857.92 → 858.96] and getting healthy.
[859.36 → 860.48] Nobody recognized him.
[861.00 → 863.26] It was, it was completely amazing.
[863.72 → 865.74] So good, good job getting healthy.
[865.80 → 868.78] Nathan, you've actually inspired me since go for con.
[868.88 → 871.46] I've lost 21 pounds because you inspired me.
[872.24 → 872.68] Yes.
[873.24 → 874.22] And you know what?
[874.28 → 875.68] Uh, I had same reaction.
[875.78 → 877.06] I had to do a double take with Nathan.
[877.20 → 879.52] I was like, Oh, because I had seen his pictures on Twitter.
[879.52 → 880.64] I knew he had lost weight.
[880.70 → 883.06] So I was prepared to, to, to see that.
[883.06 → 884.88] But, but I still had to do a double take.
[885.60 → 890.42] And, um, I mentioned on Twitter, and I've been very loose about it.
[890.50 → 895.24] I think we, we should get together people who want to have a health goal for next go for
[895.24 → 901.06] con to lose 10 pounds or 20 pounds or rich, rich.
[901.06 → 907.18] Like, uh, I want to lift, you know, this amount of weight or anything we should get together.
[907.98 → 911.16] And, uh, you know, it's just motivated each other.
[911.16 → 917.32] So somebody, I don't know what to do to, to gather people around this, uh, efforts.
[917.80 → 923.50] Uh, I don't necessarily have the time to lead and, and come up with a plan, but if somebody
[923.50 → 926.40] wants to do it, I definitely have a health goal for next year.
[926.40 → 928.48] Um, I be willing to do it.
[928.94 → 931.38] So there, that's good.
[931.48 → 932.42] I think it's a great idea.
[933.16 → 933.54] Yeah.
[933.98 → 935.20] Developers getting healthier.
[935.92 → 936.36] Definitely.
[936.46 → 936.62] Yeah.
[936.78 → 939.06] Every year I see, um, the runners.
[939.54 → 944.90] There's generally groups of people who go off and run in the city in the morning, bright
[944.90 → 945.36] and early.
[945.36 → 947.72] But, uh, that's not me.
[948.18 → 948.62] Yeah.
[948.84 → 951.54] This, this year, sadly missing Brad Fitzpatrick though.
[951.80 → 952.04] Yeah.
[952.56 → 954.34] Wait, all of our best to you, Brad.
[954.44 → 958.38] I know they're, they're moments away from baby delivery.
[958.38 → 962.46] So if you're listening or if you do listen later, we hope that everything goes well with
[962.46 → 962.94] your delivery.
[963.64 → 964.90] Yeah, definitely.
[965.64 → 967.72] Babies rock and go for babies rock more.
[968.10 → 968.50] Right.
[968.50 → 973.10] Does the, does the doctor give a looks good to me thumb too?
[973.50 → 973.68] Yeah.
[974.00 → 976.12] It has to go through Jarrett.
[978.30 → 985.18] So, um, we can either talk a bit about community day or we can talk about talks first and do
[985.18 → 988.66] them chronologically in the order they occur at the conference.
[989.34 → 991.68] No, that's way too structured for us.
[992.14 → 997.30] We can make that plan now, but we'll get sidetracked so fast that we'll feel like we didn't have
[997.30 → 998.12] a plan to begin with.
[998.12 → 999.90] I think that's a poor choice for us.
[1000.28 → 1002.32] I think we should just continue to free form.
[1003.72 → 1005.20] Otherwise we look disorganized.
[1005.80 → 1007.60] Free form away, Brian, go ahead.
[1009.04 → 1011.52] Leaders into the free forming worlds.
[1012.80 → 1015.12] Eric brings up a community day.
[1015.32 → 1020.32] And I think, uh, the standout awesome from community day was the contributor room that
[1020.32 → 1021.40] the go team put together.
[1021.62 → 1023.20] That was so amazing.
[1023.50 → 1025.60] I don't remember the final count of people.
[1025.60 → 1031.12] I want to say it was like 150 people, but lots and lots of people went in and had mentors
[1031.12 → 1036.30] that helped them get through the a little bit onerous process of setting up an environment
[1036.30 → 1037.94] to contribute to the go project.
[1037.94 → 1044.50] And I want to say that there were on that day alone, 40 contributions accepted and a lot
[1044.50 → 1045.06] more made.
[1045.16 → 1050.98] And I'm sure since then, uh, many of those, uh, that have were submitted have been accepted
[1050.98 → 1051.30] too.
[1051.50 → 1058.98] So, uh, just a huge, huge shout out to Steve and Steve Francia and others who set up that
[1058.98 → 1063.96] room and the mentors who helped enable it because it was truly awesome.
[1063.96 → 1067.34] All those people getting contributed, contributing to go.
[1067.64 → 1068.04] Yeah.
[1068.08 → 1072.80] They had a little dashboard going for points for, uh, types of contributions.
[1072.80 → 1073.94] And yeah, it was.
[1074.14 → 1074.26] Yeah.
[1074.34 → 1079.90] I want to say something about that because I was there as a participant, and it was amazing.
[1080.06 → 1084.22] I so loved that they did that, and I hope they do it every year.
[1084.22 → 1088.66] And actually I talked to Steve and I mentioned to Steve, and I wasn't the only one to mention
[1088.66 → 1096.56] this, that we should have that like twice a year, maybe four times a year and get the
[1096.56 → 1102.10] the goal meetups together to do that as a, as a team, as a group around the world.
[1102.10 → 1109.54] And maybe we can have in different time zones, but anyway, so there were two separate things
[1109.54 → 1111.08] that we were doing in that room.
[1111.46 → 1114.52] One was going through the process.
[1114.66 → 1120.30] They had a, uh, uh, uh, I want to say a fake repo, and we were going through the process of
[1120.30 → 1123.74] submitting to go, except that we weren't submitting to, to the goal repo.
[1123.74 → 1129.14] We were submitting to this fake repo, but the point was to get you to go through the process
[1129.14 → 1135.92] and having someone there to comment on your submission and maybe ask you to make a change
[1135.92 → 1141.50] or correct your submission, and then you make a correction and submit again until you went
[1141.50 → 1144.10] through the whole process and got your submission completed.
[1144.60 → 1147.42] And you know, your change was pushed to that repo.
[1147.66 → 1150.26] So that was to get you through the process.
[1150.76 → 1155.74] And I don't want to say it was simple because, you know, simple is very relative.
[1155.74 → 1157.90] I had done that before.
[1158.54 → 1164.68] Uh, I'm very familiar with kids, which helps, but I want to say that there were so many people
[1164.68 → 1165.46] there to help.
[1165.76 → 1167.34] And I actually got help.
[1167.48 → 1173.16] Uh, somebody was teaching me how to interpret because I was reading the instruction on how
[1173.16 → 1178.90] to add an example, and I was having a hard time understanding the shortcuts that the documentation
[1178.90 → 1179.98] was using.
[1180.12 → 1181.80] And this guy explained it to me.
[1181.84 → 1183.20] I was like, Oh, that's what it means.
[1183.32 → 1183.76] Thank you.
[1184.26 → 1185.52] So that was one thing.
[1185.52 → 1189.64] And they had this, like Eric was saying, they had this dashboard and there were a gazing
[1189.64 → 1191.54] and like a thousand submissions, I think.
[1192.42 → 1195.88] Uh, just in one session, there were two sessions, one in the morning, one in the afternoon.
[1195.88 → 1200.40] So I highly recommend people who haven't gone through the process to go to this work, to
[1200.40 → 1201.58] this workshop is free.
[1202.12 → 1204.68] Uh, if they are a go for con in the future.
[1205.00 → 1207.84] And the other thing was like, okay, you went through this process.
[1207.96 → 1211.12] How about now you go and make a submission to the go repo?
[1211.12 → 1213.84] And that's where the 40 submissions come from.
[1213.84 → 1220.76] A lot of people submitted codes or example or documentation and, uh, you know, they became
[1220.76 → 1221.56] go contributors.
[1221.56 → 1227.36] So one of the things that I thought was really fantastic about it was, uh, the Phoenix users
[1227.36 → 1233.10] group, I think took that same material and brought it home for their go meetup.
[1233.16 → 1234.82] I think it was that you, Brian Downs?
[1234.82 → 1240.88] Pretty sure it was, uh, did a contributor workshop right after go for con and spread it even farther.
[1240.88 → 1247.28] So my call-out to the meetup organizers out there is to find that material and, uh, push
[1247.28 → 1248.24] it out, spread the love.
[1248.36 → 1249.88] Let's get more people contributing to go.
[1249.98 → 1251.66] Cause that was a really great idea.
[1252.34 → 1252.46] Yeah.
[1252.52 → 1254.30] It really is easy to follow.
[1254.66 → 1257.20] The workshop format is easy to follow.
[1257.28 → 1259.54] It's easy to, to, if you want to replicate it.
[1259.66 → 1266.32] The reason why I said I would like the gold team to do it more purposefully is that I would
[1266.32 → 1270.46] imagine, I mean, I would wish somebody from the gold team or a couple of people would be
[1270.46 → 1275.02] there to approve the submissions and give immediate feedback until people went through the process
[1275.02 → 1276.94] and then got the submission pushed through.
[1277.32 → 1282.10] That's the only difference, but it's just going through the process and making the first initial
[1282.10 → 1289.88] submission is, uh, I mean, it's, it's really, I don't, I hate saying simple, but it's pretty
[1289.88 → 1290.44] straightforward.
[1291.16 → 1292.36] No, but it's intimidating.
[1292.50 → 1295.82] The idea of getting all set up is intimidating to me.
[1295.82 → 1301.64] I remember it's, it's been years since I did my first, but I remember spending a lot
[1301.64 → 1304.86] of time staring at the documents and thinking how in the world is this?
[1304.90 → 1305.94] Because it's not just a PR.
[1306.42 → 1308.14] It's not even close to just a PR.
[1308.68 → 1308.82] Yeah.
[1308.88 → 1314.58] I meant for the for organizers who would be teaching people because the whole, I think
[1314.58 → 1320.22] what makes it simple for attendees is to have people there to help them.
[1320.22 → 1324.52] And once people explain it to you, then, then, you know, you keep explaining how, however
[1324.52 → 1328.28] much you need, then at the end you will hopefully, oh yeah, okay.
[1328.28 → 1328.90] I get it now.
[1328.96 → 1330.50] At some point you're going to get it.
[1331.06 → 1331.42] Yeah.
[1331.42 → 1331.68] I agree.
[1331.74 → 1333.24] That was the magic that made it all work.
[1333.28 → 1335.74] Well, it was having so many mentors there.
[1336.60 → 1340.48] I think that there's also a degree of motivation there too, right?
[1341.16 → 1347.16] Um, because there's kind of the process of getting your, um, how do they call it?
[1347.16 → 1351.76] Where you got to get added to be able to submit CLA.
[1352.28 → 1352.64] Yeah.
[1353.02 → 1355.52] Because you, did they make everybody there submit a CLA?
[1356.38 → 1357.26] I'm sure they did.
[1357.30 → 1357.46] Yeah.
[1358.08 → 1363.38] So like there's, so that ends up being a barrier to entry and a lot of people feel like, oh,
[1363.46 → 1368.62] well, you know, and, and Ashley McNamara mentioned this in her talk too, you know, that, you know,
[1368.62 → 1373.44] you don't have to be a wizard or genius to contribute, but a lot of people feel that way.
[1373.44 → 1377.42] And then when there's this additional barrier to entry, I think that that's even more, should
[1377.42 → 1378.62] I go through this process?
[1378.62 → 1382.16] You know, is my, you know, are my contributions really wanted?
[1382.28 → 1387.08] I'm not, you know, insert name of big go person here, you know?
[1387.72 → 1393.38] So I think having that room dedicated to like anybody, everybody show up, we, you know, we,
[1393.54 → 1398.52] we want to help get you set up and get you submitting, and all contributions are welcome.
[1398.52 → 1403.18] I think there's a motivational aspect to that, that, okay, well, maybe I should try this out.
[1404.26 → 1405.68] Well, it was a good initiative.
[1406.24 → 1413.22] So, so Steve Francia, Jess Frizzell, Russ Cox, all the people who made that happen behind the
[1413.22 → 1417.78] scenes are our biggest congratulations on pulling off such an awesome show.
[1417.84 → 1418.86] It was, it was a good deal.
[1420.10 → 1425.36] And Brad Fitzpatrick, who, even though he wasn't able to make it, he was there reviewing everybody's
[1425.36 → 1425.66] stuff.
[1425.66 → 1430.52] And he had a concurrency of gophers next to him, helping out with his looks good to me
[1430.52 → 1430.94] shirt on.
[1431.14 → 1431.60] It was awesome.
[1433.12 → 1436.40] You know, concurrency is the collective noun for a group of gophers, right?
[1437.46 → 1438.74] A concurrency of gophers.
[1440.78 → 1442.08] That is true, right?
[1443.02 → 1443.92] I'm sure it is.
[1444.30 → 1444.74] Yeah.
[1445.02 → 1445.90] It is true now.
[1446.42 → 1448.34] If not, we've declared it so, right, Galicia?
[1448.92 → 1449.36] Absolutely.
[1449.36 → 1456.78] So the other room, so another room that takes place there every year is the Robot room put
[1456.78 → 1458.06] on by the hybrid group.
[1458.42 → 1461.96] That room is always packed, and it's really cool.
[1462.04 → 1467.64] And that also had a lot of people contributing back to the Robot project to support new hardware.
[1467.64 → 1469.74] Yeah, that room is really cool this year.
[1469.84 → 1474.66] I went by, I didn't hang out in the room a lot, but I went by five or six times.
[1475.30 → 1481.96] And every single time I went, I saw kids from the family day activities in the room, on the
[1481.96 → 1485.90] floor, you know, controlling Spheres or something like that.
[1485.90 → 1493.66] So it was amazing to me that Ron was able to engage all the adults, but, you know, he's
[1493.66 → 1494.44] just such a good guy.
[1494.50 → 1496.00] He always has something for the kids too.
[1496.28 → 1498.04] He's something special.
[1498.90 → 1502.88] Yeah, there was, I'm trying to remember all the activities that were there.
[1502.96 → 1504.88] There was a data science room.
[1505.82 → 1509.80] There was a container technologies room, lightning talks.
[1509.94 → 1513.82] Lightning talk quality was like off the hook this year.
[1513.82 → 1515.46] There were a lot of good talks.
[1515.64 → 1521.04] I've heard a lot of and seen a lot of people tweeting about some of the lightning talks.
[1521.78 → 1527.60] So if you're the type of person that only watches the normal event videos, all the lightning
[1527.60 → 1529.66] talks are also on YouTube.
[1530.02 → 1532.52] Like you should definitely watch some of those as well.
[1533.92 → 1537.32] The round tables, that actually was a lot more popular this year.
[1537.32 → 1546.40] Um, so for anybody who, um, didn't go to community day or didn't go to go for con at all on community
[1546.40 → 1548.54] day, which is the day after the talks.
[1548.54 → 1553.50] And, um, we basically have these rooms set up that we were just kind of describing that
[1553.50 → 1557.36] contributor room, go bot room, all of these things where you can collaborate with people.
[1557.36 → 1563.32] But there's also kind of like a big open area with round tables, and you can write the project
[1563.32 → 1567.78] you're working on or topic you're discussing and the table that you're at.
[1567.94 → 1571.72] And people can kind of go through the list and join up with people doing similar things.
[1572.00 → 1575.00] And that room was also packed all day.
[1575.62 → 1576.72] It was crazy.
[1576.72 → 1583.76] I'm really pleased with the number of people who are kind of, uh, seeing community day
[1583.76 → 1588.26] because it was, you know, we had way more people the first year stay than I think we
[1588.26 → 1588.84] anticipated.
[1589.14 → 1594.46] It started off as just sort of, uh, we know you, most people are probably flying out the
[1594.46 → 1596.40] day after the talks.
[1596.98 → 1599.54] So, you know, and everybody flies out at different times.
[1599.54 → 1605.54] Maybe we should just, uh, rent some space in the hotel that we were out at the time and
[1605.54 → 1611.28] people can hang out and chat and collaborate on stuff until, um, they have to leave for
[1611.28 → 1613.46] their flight, bring your bags, all that good stuff.
[1613.66 → 1617.70] And a lot of people stayed for that and kind of each year it's grown bigger and bigger where
[1617.70 → 1621.16] now it's like a day that most people stay for the whole day.
[1621.54 → 1627.12] So if you have never been to the community day, you should definitely, uh, stay for that.
[1627.16 → 1628.92] It's probably one of my favourite days.
[1628.92 → 1629.80] Mm-hmm.
[1630.18 → 1637.12] So I saw at least two, maybe three huge projects that got a lot of lift on community
[1637.12 → 1637.44] day.
[1637.60 → 1638.82] The first one was depth.
[1639.06 → 1645.94] I know, um, Sam Boyer had at least three tables worth of people all contributing.
[1646.30 → 1650.66] And, you know, he, I think he started the day hoping that he would get, you know, two or
[1650.66 → 1652.62] three issues closed on GitHub.
[1652.62 → 1658.08] And he ended up stretching his goals beyond his wildest dreams and got a bunch of stuff
[1658.08 → 1660.16] done that he wasn't expecting to even finish this year.
[1660.42 → 1665.26] So it's really cool that so many people jumped in on the debt project and got so much work
[1665.26 → 1665.46] done.
[1665.52 → 1670.60] I know Chris Nova had a Unicorn table and I swear to God, she looked like a cult leader
[1670.60 → 1673.82] over there because they were all just watching her with rapt attention.
[1674.48 → 1679.40] And I'm not sure what kind of things she was telling them, but I know Unicorn had a pretty
[1679.40 → 1680.26] nice release too.
[1680.50 → 1684.18] So the cult leader is, is taking over.
[1684.78 → 1685.80] It was pretty cool.
[1686.84 → 1693.70] So how about favourite talks or at least ones that, uh, you've heard good feedback on that
[1693.70 → 1694.84] maybe you didn't catch yourself.
[1695.08 → 1700.46] I know that I often don't get to watch many of the talks, if any, until the videos are released.
[1700.46 → 1704.34] And depending on my work schedule is how fast I consume them.
[1704.34 → 1711.10] So I can start off, uh, one that, uh, seemed to get very, very good reception.
[1711.10 → 1716.58] And I actually have happened to watch this on, um, YouTube was just recently a guest of
[1716.58 → 1721.86] our show, which was, uh, Kāvya Joshi, who did the, um, understanding channels.
[1722.24 → 1726.18] Um, if you haven't seen that talk, you weren't there for it or weren't at Gopher Con.
[1726.32 → 1730.66] Um, it's on YouTube, all of these, all the talks from the conference are there.
[1730.66 → 1733.96] Um, she walks through kind of the implementation of channels.
[1733.96 → 1737.64] So this isn't the, you know, how do you use them, but how do they work under the hood?
[1738.14 → 1745.14] And there's a bit of how the runtime works too, with regard to scheduling go routines that
[1745.14 → 1749.14] have, uh, blocking, uh, sends and receives on them.
[1749.94 → 1750.02] Yeah.
[1750.02 → 1755.54] It was a super geeky talk, and it was low level enough that I think everybody learned something.
[1755.54 → 1760.40] And I, I, my favourite part of the talk was at the end when, you know, everybody mobbed
[1760.40 → 1761.86] her at the stage from the go team.
[1763.08 → 1766.52] And I turned around to Eric and I said, somebody's getting the job offer soon.
[1769.72 → 1771.46] So yeah, that was a perfect talk.
[1771.54 → 1775.88] I liked, um, Edward Mueller's talk on go antipatterns.
[1775.94 → 1776.90] That was a perfect talk.
[1777.00 → 1782.04] He hit, uh, hit the nail on the head on a ton of different things that, that I've been
[1782.04 → 1786.16] teaching for the last couple of years and taught me several that I've been abusing for
[1786.16 → 1787.00] the last couple of years.
[1787.00 → 1788.60] So that was a perfect talk.
[1788.66 → 1791.94] If you haven't caught that one, that room was busting out the seams.
[1792.12 → 1793.60] It was, it was really busy.
[1794.08 → 1795.52] It's one I haven't caught yet.
[1795.58 → 1799.24] I haven't been able to watch that video yet, but it definitely seemed like a really, really
[1799.24 → 1800.02] popular talk.
[1800.76 → 1800.96] Yeah.
[1801.10 → 1806.76] Everybody should watch that talk, especially beginners, especially please do.
[1806.76 → 1812.98] And I don't think that we could leave out, um, Russ Cox talking about the future of go,
[1813.22 → 1818.42] or I think people about drop-dead when, uh, you mentioned that it's time to start thinking
[1818.42 → 1819.26] about go to.
[1820.02 → 1821.12] Yeah, but all right.
[1821.12 → 1827.64] So, you know, I love the go team and I love Russ, but man, that was the biggest cop-out
[1827.64 → 1828.26] talk ever.
[1828.96 → 1830.62] Cop-out, complete cop-out.
[1830.74 → 1833.16] So you put on the schedule, the future of go.
[1833.16 → 1835.94] And start letting rumours slide.
[1836.04 → 1837.50] We're going to talk about go 2.0.
[1837.70 → 1838.44] This is amazing.
[1839.12 → 1839.32] Yeah.
[1839.34 → 1842.20] We're going to talk about talking about go 2.0.
[1842.54 → 1844.96] I don't, I don't, I don't know whether I agree.
[1845.54 → 1847.60] No, don't even try to defend him.
[1847.82 → 1848.52] Don't do it.
[1848.66 → 1848.88] Okay.
[1849.78 → 1850.88] Explain yourself better.
[1851.00 → 1851.64] I'm not kidding.
[1851.74 → 1854.18] I don't want to, I don't want to interpret what you're saying.
[1854.28 → 1855.74] Just spit it out.
[1856.18 → 1857.04] I'm just teasing.
[1857.14 → 1858.36] I'm just teasing Russ.
[1858.70 → 1863.08] I really have nothing bad to say about it at all, but I was just saying that we were
[1863.08 → 1869.08] teased by the idea that, that go 2.0 was, was coming and, and really it was just a talk
[1869.08 → 1873.18] about how we're going to go about talking go 2.0.
[1873.46 → 1878.06] I think that the go team and everything has been, you know, very much, we're going to focus
[1878.06 → 1885.14] on implementation and bettering that and improving compile times and speed and all that stuff.
[1885.22 → 1887.06] And we're not going to work on changing the language.
[1887.06 → 1894.08] So I think that it still is a very exciting thing that collectively they are ready to move
[1894.08 → 1894.54] on that.
[1894.62 → 1900.06] You know, we've, we as a community have written enough go code that maybe it's time to start
[1900.06 → 1902.22] thinking about that and what might that look like.
[1902.22 → 1908.96] But I also think that, um, one of the big takeaways from that talk was soliciting for experience
[1908.96 → 1914.02] reports because he walks through kind of the history of how, um, they solve problems and
[1914.02 → 1914.72] things like that.
[1914.72 → 1919.42] And they want to see concrete examples of, you know, where these things are problems.
[1919.42 → 1921.96] Like as an example was generics, right?
[1922.00 → 1928.32] Like they don't, sometimes they don't have enough information to help make a meaningful decision
[1928.32 → 1933.22] as far as how that should impact the language without kind of seeing concrete examples of
[1933.22 → 1938.44] how people intend to use these things or, or, um, how it's currently failing them.
[1938.70 → 1943.38] So I think that that was probably the biggest takeaway is that, you know, if you want to help
[1943.38 → 1950.56] shape what go 2.0 ultimately becomes, um, you should make it a point to contribute that
[1950.56 → 1951.12] feedback.
[1951.12 → 1957.42] I was going to say the same thing, Erica just said, just not as articulate, but I do
[1957.42 → 1963.04] want to reemphasize that even though it was a talk about, let's talk about talking
[1963.04 → 1968.38] go 2.0, I think it was very valuable because people communicate.
[1968.52 → 1969.56] I mean, it's just normal.
[1969.72 → 1976.54] We're not very effective, and sometimes we're in a hurry, but that talk was basically, I mean,
[1976.54 → 1981.18] there were the other things too, but the basic, the main takeaway for me was like Eric said,
[1982.04 → 1983.82] go 2.0 is going to happen.
[1984.78 → 1991.96] And if you have a problem that you want to, is not being solved now that you do want to
[1991.96 → 1999.76] be solved, submit what your problem is, because we need to understand what kind of problem it
[1999.76 → 2000.08] is.
[2000.24 → 2001.96] Don't submit a feature request.
[2002.06 → 2003.94] Don't jump ahead and say, oh, I have a problem.
[2003.94 → 2008.26] And I think it's going, it will be solved if you go ahead this.
[2008.56 → 2012.46] So I am requesting that you add this to go.
[2013.36 → 2019.66] They were, he was very specifically saying, submit your problem, submit a use case for
[2019.66 → 2020.18] your problem.
[2020.66 → 2026.82] And I was reading Reddit and there were so many people saying, oh, after that talk, I
[2026.82 → 2031.00] don't know if they watched it or not, or read about it or not, because there was also a blog
[2031.00 → 2032.04] post that goes with it.
[2032.04 → 2035.50] But people were saying, yeah, I love if you go ahead this.
[2035.92 → 2040.86] And some people are pointing out, dude, you need to submit your problem.
[2041.70 → 2042.74] Not a feature request.
[2042.88 → 2044.86] It's not about submitting feature requests.
[2045.90 → 2049.34] If they had named the talk, if I'm sorry, I didn't mean to cut you off.
[2049.42 → 2049.86] Please finish.
[2050.70 → 2052.16] No, I was just going to repeat myself.
[2052.26 → 2053.20] Thank you for cutting me off.
[2053.20 → 2060.78] If he had named the talk, how to communicate or build consensus on the forward movement
[2060.78 → 2063.60] of a project, then I would give it 12 out of 10.
[2064.68 → 2066.04] But he named it the future of go.
[2066.46 → 2070.54] So I say it's, it's a five out of 10 because we didn't talk about ghost future.
[2070.58 → 2075.30] We talked about communicating and building scientific evidence about why we need to change things
[2075.30 → 2075.58] and go.
[2075.58 → 2079.00] We talked about how we will influence the future of go.
[2079.52 → 2079.90] Exactly.
[2080.08 → 2081.10] Which will be a future of go.
[2081.36 → 2086.94] Which again is an incredibly valuable talk, but we totally got click baited on the title.
[2087.64 → 2091.00] 10 people got together in a room and built go to go 2.0.
[2091.36 → 2092.98] Click here to see what happens next.
[2092.98 → 2100.54] So, um, uh, one cool fact that I'm, I'm going to totally ignore Brian right now.
[2101.90 → 2102.84] This is new.
[2103.28 → 2108.82] One, one cool fact that came out of that though was, um, I forget where the stat came from,
[2108.82 → 2114.22] but I know that they had estimated somewhere between 500,000 and a million go programmers
[2114.22 → 2118.22] in the world, which seems astronomical at this point.
[2119.28 → 2122.96] I can't remember where the stats came from either, but you're ignoring me.
[2122.98 → 2124.00] So I won't answer any.
[2126.34 → 2131.14] So other talks, um, Oh, you know, who nailed one?
[2131.44 → 2132.14] Liz rice.
[2132.76 → 2133.00] Yeah.
[2133.00 → 2135.22] The go programmers guide to these calls.
[2135.46 → 2136.66] That was so cool.
[2137.94 → 2138.68] Great talk.
[2139.38 → 2145.94] She basically, uh, started the talk out, um, talking about how in, um, prior talks, she
[2145.94 → 2152.86] mentioned system calls, and she wanted to kind of make sure she knew what she was
[2152.86 → 2156.02] referring to when, uh, talking about them.
[2156.02 → 2160.04] So we're to talk, uh, explaining how system calls work to people.
[2160.04 → 2161.38] And that's actually really great.
[2161.38 → 2166.30] If you're not familiar with how system calls work and, uh, a little bit of it, like Linux
[2166.30 → 2170.80] assembly to kind of really helps solidify that too.
[2170.80 → 2177.20] And, and what it talks about, you know, as far as, you know, resetting registers and things
[2177.20 → 2177.76] like that.
[2178.42 → 2178.86] Yeah.
[2178.94 → 2181.56] Brian downs and slack said he could listen to Liz talk about anything.
[2181.56 → 2182.60] And I totally agree.
[2182.60 → 2187.88] This is maybe the third time I've seen her talk, and she just has such a fantastic delivery
[2187.88 → 2192.58] and she's so eloquent, and she knows the material so well.
[2192.58 → 2197.58] I mean, you know, between her and Jess Frizzell, I have a hundred percent imposter syndrome when
[2197.58 → 2200.44] it comes to deep kernel level knowledge of anything.
[2200.70 → 2202.08] Just no, go ask them.
[2202.14 → 2202.68] Because I don't know.
[2203.44 → 2205.96] I want to say, I was going to say the same thing.
[2206.04 → 2210.56] I was going to say, I haven't seen her talk, but I don't even care what it was about.
[2210.64 → 2211.84] Because I've seen her talks before.
[2211.84 → 2215.28] Or like the talk that she gave it, go, go language K last year.
[2215.28 → 2216.82] It's like, she's so great.
[2217.22 → 2218.88] I would watch anything she talks about.
[2220.00 → 2220.64] Yeah.
[2220.74 → 2225.80] And, um, if you didn't see it, the talk that Carlyle is referring to, um, from Golang UK
[2225.80 → 2230.62] was, um, she implemented containers in go.
[2231.94 → 2233.28] She did it live.
[2233.76 → 2234.02] Yeah.
[2234.20 → 2235.76] And this is very badass.
[2236.14 → 2237.10] It's super cool.
[2237.14 → 2241.68] And I love that it makes the containers, uh, seem less magic.
[2242.34 → 2246.04] Because I think a lot of people see them as, you know, just kind of this, it's kind of
[2246.04 → 2246.98] like a virtual machine.
[2247.10 → 2251.80] You don't implement your own virtual machine, you know, virtualization software, but it is kind
[2251.80 → 2256.34] of really breaks it down, and you can kind of see the primitives of how C groups and namespaces
[2256.34 → 2262.80] play into it and how that they're, you know, uh, it's really just a highly configured process.
[2264.00 → 2270.50] So also on the deep technical end was Keith Randall, uh, came back and talked about SSA.
[2270.50 → 2272.22] Uh, the SSA talk.
[2272.32 → 2272.94] That was a good one.
[2273.46 → 2273.62] Yeah.
[2273.62 → 2277.72] Which also, uh, if, if you, uh, love assembly.
[2278.38 → 2278.82] Yeah.
[2279.04 → 2282.58] Which to be honest, I still don't understand, but it was a great talk.
[2283.34 → 2285.72] I was going to say exactly the same thing.
[2285.72 → 2288.34] Hand wavy magic, something, something compiler.
[2288.56 → 2288.70] Look.
[2289.26 → 2289.66] Yeah.
[2290.04 → 2293.64] It's one of those things like you don't understand, but it makes sense.
[2293.74 → 2294.58] It's amazing.
[2294.90 → 2295.90] It's a great talk.
[2295.90 → 2298.22] It was, it was a temporary made sense though.
[2298.26 → 2300.74] I was, as I was listening, I was like, yeah, this, this makes sense.
[2300.74 → 2302.32] But then an hour later it's all gone.
[2302.96 → 2303.16] Yeah.
[2303.26 → 2304.72] Don't ask me to explain it to you.
[2306.14 → 2306.70] That's okay.
[2306.80 → 2307.58] It was a great talk.
[2308.42 → 2309.92] Any other favourites from the group?
[2311.08 → 2312.36] Ashley McNamara's talk.
[2312.54 → 2314.94] There wasn't a single dry eye in the house.
[2315.24 → 2315.98] It was so good.
[2316.70 → 2317.54] Oh my God.
[2317.94 → 2318.32] I cried.
[2318.32 → 2319.52] Nobody succeeds alone.
[2320.38 → 2321.94] I look at the guy on my left.
[2322.08 → 2327.16] I have, I was sitting between two guys, wasn't crying, but the guy on my right was like lifting
[2327.16 → 2330.06] his glasses and wiping his tears.
[2330.36 → 2331.80] So I'm like, okay, I'm not the only one.
[2332.44 → 2338.28] You know, it just underscores for me how much the community matters in any project, in any
[2338.28 → 2339.64] enterprise, in any effort.
[2340.16 → 2343.10] And I think the Go community is really kick ass.
[2343.10 → 2347.66] We have a great community that cares about each other, willing to do things to help.
[2347.66 → 2353.94] And, you know, Ashley's talk really underscored how much that help can make a difference in
[2353.94 → 2359.08] your personal success and the success of your peers and the success of the project itself.
[2359.24 → 2364.36] So it was, it was a touchy, feely, feel good movie of the year.
[2364.66 → 2365.44] Good stuff.
[2366.34 → 2368.56] Did anybody get to see Chris Nova's talk?
[2368.84 → 2370.38] I was going to say that.
[2370.48 → 2370.94] Oh my gosh.
[2370.96 → 2372.48] I'm saying this all the time.
[2372.48 → 2378.48] Uh, I was tied up with something and I miss her talk and I haven't had a chance to watch
[2378.48 → 2379.22] the video yet.
[2379.44 → 2382.56] That was one of my, on the top of my list of talks to watch.
[2383.04 → 2383.44] Yeah.
[2383.58 → 2385.78] That one's on my list as well.
[2385.92 → 2389.28] I felt bad because I really wanted to try to sneak into that one.
[2389.32 → 2391.58] And then, um, I can't remember what happened.
[2391.68 → 2393.42] And then I realized I looked at my watch.
[2393.46 → 2394.52] I'm like, it was an hour ago.
[2394.52 → 2400.88] So one of the things that's kind of amusing about that talk is that in conversations with
[2400.88 → 2406.00] random people over the last week or two, that talk specifically has come up several times.
[2406.10 → 2408.66] It was like, well, you know, when Chris has talked, blah, blah, blah, blah, blah, blah, blah.
[2408.76 → 2414.08] So I think that one's making its way around the Internets much faster than, than usual.
[2414.58 → 2416.78] That's kind of funny to hear them come back.
[2417.32 → 2419.28] Trying to remember what other ones I saw.
[2419.28 → 2425.30] I did see a good portion of Mitchell Hashimoto's talk, uh, on advanced testing.
[2425.46 → 2427.68] And I think there's some perfect, um, example.
[2427.68 → 2428.66] Oh, that talk was great.
[2429.12 → 2429.32] Yeah.
[2429.36 → 2430.96] Lots, lots of good takeaways in that one.
[2431.42 → 2437.28] I was really excited that in afterwards I talked to my coworkers, and they were also excited
[2437.28 → 2445.06] about the fact that vault has a test thing that you can use as opposed to like, uh, spinning
[2445.06 → 2448.10] up a vault to test your stuff against.
[2448.82 → 2451.04] You can just have a virtual vault.
[2451.76 → 2456.88] Um, so we learned that on that, on the talk, but then it didn't really work out well.
[2456.88 → 2463.22] Cause when you, when you call it, you have to import a package that imports a bunch of
[2463.22 → 2463.84] other packages.
[2463.84 → 2465.14] And if you don't mind that it's okay.
[2465.14 → 2469.74] But they, they said there's this, that's how it is basically.
[2469.74 → 2472.18] So we chose not to use it, but it's pretty cool.
[2472.24 → 2474.86] In any case, there are a bunch of gems in that talk for sure.
[2476.16 → 2481.66] And then, um, Sam Boyer did a talk on the new era of go package management, which were,
[2481.66 → 2489.66] he was talking about the new depth and kind of, um, actually a bit of the history and kind
[2489.66 → 2497.28] of, um, um, direction and, and guessing at the not, not guessing is the wrong word, but
[2497.28 → 2503.02] kind of like where they would like to see it go, you know, as far as what it might look
[2503.02 → 2505.86] like if it were implemented into the go tool.
[2506.64 → 2507.76] Any other favourites?
[2507.76 → 2514.36] Everybody, anybody was able to make it to Joe size talk about forward compatible go code.
[2514.36 → 2521.88] I learned a lot from that talk because there are, there are things that you can take away
[2521.88 → 2526.10] from the go one guarantee that all of your code will be forward compatible.
[2526.50 → 2529.10] And there are things that you should really deeply learn about it.
[2529.14 → 2534.38] And I think his talk was probably one of the more, you know, deeply educational for me because
[2534.38 → 2541.54] I learned so much about, um, how implementations can change underneath and, and bite you in subtle
[2541.54 → 2545.16] ways in a way that's completely compatible with the go one guarantee.
[2545.68 → 2548.38] So sometimes a guarantee isn't a guarantee.
[2549.16 → 2550.40] And that was a perfect talk.
[2551.48 → 2558.02] Can I apologize to the speakers that hear the show and don't hear their names mentioned.
[2558.90 → 2564.98] So to be clear, Brian and Eric, they run the conference, and they don't have a chance to
[2564.98 → 2566.22] watch most of the talks.
[2566.22 → 2572.46] And I was planning to watch all the talks I could, but I got tied up doing a little thing
[2572.46 → 2576.02] and I missed most of the talks I wanted to watch.
[2576.64 → 2583.72] So that's why we don't have a bigger list to, to mention, but in any case, you can't possibly
[2583.72 → 2584.84] watch all the talks.
[2584.84 → 2593.52] So now I want to mention that, uh, the talks are listed on the go for con repo, a repo calls
[2593.52 → 2595.08] 2007 talks.
[2595.88 → 2601.20] And, uh, wanted to say thank you to Daniela Petruzilek from Brazil.
[2601.42 → 2608.36] She was a scholarship recipient, and she put together a read me with the links to, to everything
[2608.36 → 2615.62] you could possibly wish for, uh, the room, the talk was in the speaker, the slide deck,
[2615.72 → 2616.26] the video.
[2616.26 → 2619.20] And if there was a source code, she puts a link to that too.
[2619.32 → 2623.90] And she has a listing for the main talks in the different listing for all the lightning
[2623.90 → 2624.48] talks.
[2624.84 → 2628.42] It's so such a, you know, it's, I'm sure it took a lot of effort.
[2628.58 → 2630.86] I mean, time to put this together.
[2631.30 → 2635.56] It seems like a little thing, but it was, it's so handy.
[2635.68 → 2637.38] I'm on this page daily.
[2638.04 → 2638.44] Yeah.
[2638.50 → 2639.14] I couldn't agree more.
[2639.14 → 2644.76] She put way more effort into, uh, putting the talks in a nice organized table with links
[2644.76 → 2648.16] to everybody and all the things, uh, than I certainly would have.
[2648.30 → 2654.68] So, um, and, and one of the things that she mentioned in Slack was that Ashley's talk inspired
[2654.68 → 2655.68] her to do that.
[2656.04 → 2661.14] You know, this is a way that she had time to give back, and I am very grateful for it for
[2661.14 → 2661.38] sure.
[2661.38 → 2667.16] And that reminds me of something else I wanted to say in today's episode, people ask me,
[2667.28 → 2672.06] so how did you, how did you get involved with these things?
[2672.06 → 2677.44] Because they look at me like I'm a nobody, but I'm doing a podcast, and you know, I'm doing
[2677.44 → 2678.56] this, and I'm doing that.
[2678.68 → 2687.54] And it's, that's exactly how you get to be in a position of, uh, be doing something more
[2687.54 → 2687.92] relevant.
[2687.92 → 2693.64] You just start saying, yes, you just start taking, seeing something you have to be looking
[2693.64 → 2696.50] first, and then you see something that needs to be done, and you do it.
[2696.60 → 2700.50] Then the next time you turn around, people say, ask you to do something and you say, yes.
[2700.50 → 2706.94] And then, you know, pretty soon you're taking leadership in, uh, initiatives and that's how
[2706.94 → 2711.78] people get involved and, you know, start doing more relevant things in the community.
[2711.78 → 2717.16] Just start looking for opportunities to contribute and, uh, safe.
[2717.16 → 2719.84] But people ask you to do something, say yes.
[2720.38 → 2720.84] Yeah.
[2720.84 → 2721.96] Just sort of take a chance.
[2721.96 → 2726.80] But I did before, like we end up wrapping the two and, or moving on too far.
[2726.88 → 2733.66] I want to mirror Galicia's statement to, um, shows being, or specific talks mentioned
[2733.66 → 2739.30] on the episode today are in no manner, uh, scoring higher than others.
[2739.30 → 2744.24] They happen to be ones that we were able to attend or happen to be able to watch since
[2744.24 → 2744.94] we got home.
[2744.94 → 2750.12] Um, a lot of the times, um, I actually don't think I caught much of any talks.
[2750.12 → 2755.98] Well, at the conference, only, uh, slipping in videos here or there, um, everybody did an
[2755.98 → 2756.86] outstanding job.
[2756.98 → 2758.00] All the talks were great.
[2758.00 → 2759.96] So definitely make your way through the whole list.
[2760.48 → 2764.36] Um, we did a survey too, and all the talks got amazing feedback.
[2764.36 → 2766.66] So you won't be disappointed with any of them.
[2767.54 → 2768.46] Well spoken.
[2769.22 → 2769.78] Yeah.
[2770.18 → 2776.72] So, um, before we wrap up, um, I wanted to call out some other conferences too.
[2777.02 → 2782.66] Um, in case you didn't get your fix at Gopher Con, or it wasn't a big enough fix, and you need
[2782.66 → 2783.64] more Go Conference.
[2784.64 → 2785.16] More.
[2785.16 → 2789.60] Um, Golang UK is, uh, on the 16th.
[2790.18 → 2793.12] Um, this episode may or may not air before then.
[2793.24 → 2798.00] I got to do the math in my head, but, uh, anybody who's listening live, um, tickets are
[2798.00 → 2798.64] still available.
[2799.56 → 2801.88] Brian, uh, will be speaking there.
[2802.48 → 2803.76] I am closing out the show.
[2804.56 → 2806.38] And burning the place down.
[2807.88 → 2810.16] And then Gotham Go is in October.
[2810.16 → 2812.24] They've announced their keynote speakers.
[2812.24 → 2818.02] Uh, Steve Francia, Alan Donovan, Carmen Lando, John Boehner, and Jesse Frizzell.
[2818.32 → 2822.42] Um, I don't think they've announced any of the other speakers, but I think the CFP might
[2822.42 → 2823.60] be over for that already.
[2824.14 → 2827.90] Uh, Doggo in Paris, uh, is in November.
[2828.80 → 2830.78] Um, it announced six of their speakers.
[2831.18 → 2832.46] Brian is also speaking there.
[2832.82 → 2833.92] Burning that one down too.
[2833.92 → 2840.60] Frances and JBD and Samir are also some of the speakers they announced.
[2840.60 → 2846.66] Um, um, and then Gopher Con Brazil is in November and the CFP is open for that.
[2846.92 → 2851.02] So if you'd like to speak at a conference, I'm sure they would love to see your proposal.
[2852.16 → 2852.32] Yeah.
[2852.44 → 2855.78] And I know Steve Francia is going to be at a conference in Brazil.
[2856.56 → 2858.64] Uh, Jess Frizzell is also going to be there.
[2858.72 → 2859.24] Pretty sure.
[2860.10 → 2860.94] I think I saw that.
[2861.58 → 2862.02] Oh, nice.
[2862.02 → 2862.78] Yeah.
[2862.82 → 2864.26] It's the second one last year.
[2864.42 → 2868.66] It was really, from all the accounts I heard, it was really well done.
[2869.54 → 2870.52] And it's in Brazil.
[2870.74 → 2871.00] Come on.
[2871.52 → 2872.16] Yeah, it's Brazil.
[2872.70 → 2873.76] Talking about Brazil.
[2874.00 → 2875.30] Are we done with the conference listing?
[2876.24 → 2876.66] Sure.
[2877.68 → 2879.16] We can talk about it for hours.
[2879.64 → 2881.36] So anytime you want to end is great.
[2882.16 → 2888.24] I just want a quick shout out to Jairo from Brazil, who was at the conference and gave us
[2888.24 → 2891.56] all a very fancy bottle of wine.
[2892.02 → 2895.00] And by no means, I want to encourage people to give us gifts.
[2895.18 → 2896.00] Please don't.
[2896.12 → 2897.58] I'm just saying because he did it.
[2897.66 → 2901.34] So I feel very compelled to say thank you in the air.
[2901.68 → 2903.30] He was thanking us for such a good show.
[2903.34 → 2904.60] But people don't do that.
[2905.44 → 2905.80] Seriously.
[2906.08 → 2906.76] Don't bring us gifts.
[2907.46 → 2908.16] Don't bring us gifts.
[2908.68 → 2911.62] That, um, I think that adds to the imposter syndrome.
[2911.62 → 2912.46] Mm-hmm.
[2913.34 → 2913.52] Yeah.
[2913.56 → 2917.84] I can't possibly be worthy of somebody bringing a bottle of wine 10,000 miles.
[2918.70 → 2918.84] No.
[2919.00 → 2922.16] He did four because Adam also got one.
[2923.02 → 2925.96] And now I feel like I need to do better.
[2926.36 → 2927.12] It's such a pressure.
[2927.70 → 2928.90] People don't give us gifts.
[2928.90 → 2931.44] It's all about pressure.
[2931.84 → 2932.04] All right.
[2932.04 → 2933.06] I have to sign out.
[2933.18 → 2938.60] I've got a hard stop here in two minutes because I am working for a company now.
[2939.16 → 2945.00] So, uh, thanks everybody for another show and feel free to continue without me.
[2945.68 → 2947.54] But Gopher Con was amazing this year.
[2947.62 → 2951.92] And I just can't say thank you enough to all the people who participated, all the people
[2951.92 → 2955.88] who came, so many people helped in small and big ways.
[2956.14 → 2957.28] Um, all of my love.
[2957.52 → 2957.86] Thank you.
[2958.78 → 2959.42] Bye, Brian.
[2960.06 → 2960.76] Bye, Brian.
[2960.84 → 2961.00] Bye.
[2961.32 → 2961.54] Bye.
[2961.86 → 2963.24] I want to thank everybody too.
[2963.42 → 2969.32] I think that that was, um, I think, so Scott Mansfield is, uh, asking about open source
[2969.32 → 2970.06] shout-outs.
[2970.06 → 2972.62] I think, um, today really is about the community.
[2972.62 → 2977.82] I think that, you know, everybody contributing and everybody in the Go contributors room helping
[2977.82 → 2983.64] people contribute and everybody who contributes even outside the conference itself.
[2984.10 → 2988.76] Um, I think we can all collectively agree that today we shout out to the community.
[2989.48 → 2991.54] Unless Galicia has a fun one to add.
[2992.74 → 2994.22] No, absolutely.
[2994.38 → 2995.42] I second what you said.
[2996.02 → 3002.60] So I think with that, uh, I think we can wrap this show up, and hopefully we'll be
[3002.62 → 3004.56] coming here in the future.
[3004.56 → 3007.60] We'll talk up a little bit about some of these other conferences.
[3007.74 → 3009.42] Are you going to any of the other conferences?
[3009.68 → 3011.22] I know you go to Brazil, right?
[3012.00 → 3013.36] I love to go to Brazil.
[3013.60 → 3014.48] They're still up in the air.
[3014.58 → 3014.94] I don't know.
[3015.04 → 3019.06] My, my work is really heavy now, and I don't know if I can take the time off.
[3019.44 → 3019.76] We'll see.
[3019.86 → 3023.78] Oh, and also, I don't know what I would, I mean, I'll have to talk because that's how
[3023.78 → 3025.42] fast they would pay me for to go.
[3025.52 → 3026.88] And I have nothing to talk about.
[3026.88 → 3030.64] I, not that I know of, can't come up with anything.
[3031.12 → 3032.28] That's always the hard part.
[3032.54 → 3032.82] Yeah.
[3033.06 → 3033.46] Content.
[3034.14 → 3035.76] Well, I can't say that's the hard part.
[3035.88 → 3040.30] Getting up in front of a bunch of strangers and talking is probably the hard part.
[3040.48 → 3044.82] But first you have to get past the coming up with what you're going to talk about.
[3045.28 → 3045.50] Yeah.
[3045.56 → 3046.80] For me, that's the hardest part.
[3046.96 → 3048.26] Coming up with some things to talk about.
[3048.72 → 3050.00] I struggle with that too.
[3050.00 → 3057.66] I'd like to speak again at another conference, but I need to come up with some material that
[3057.66 → 3060.68] I want to talk about, preferably something I'm super passionate about.
[3060.90 → 3062.22] It makes it easier that way.
[3063.12 → 3063.22] Yeah.
[3063.94 → 3067.82] So, but if any of us make it to some of these conferences, I know Brian's going to at least
[3067.82 → 3068.50] be at the two.
[3068.82 → 3072.10] We will chat a bit about kind of experiences there.
[3072.56 → 3072.84] Yeah.
[3073.52 → 3076.08] And I guess that's a wrap.
[3076.48 → 3077.88] And thanks, Galicia.
[3077.88 → 3080.12] Brian's already gone, so we can't thank him.
[3080.30 → 3085.48] But thanks, everybody, for listening and everybody who made it to Gopher Con and everybody, even
[3085.48 → 3089.80] if you didn't attend all the companies and stuff contributing towards the diversity initiatives
[3089.80 → 3091.78] this year was so amazing.
[3092.10 → 3094.62] And we're so grateful to be a part of this community.
[3095.54 → 3095.68] Yeah.
[3095.78 → 3096.82] It made a huge difference.
[3096.94 → 3097.42] Thank you.
[3098.26 → 3103.68] And as far as the podcast goes, if you're enjoying it, please share with friends and
[3103.68 → 3104.20] colleagues.
[3104.48 → 3106.84] And we are at GoTimeFM on Twitter.
[3106.84 → 3113.14] You can chat with us live in the Slack channel, which is, I always forget the invite link
[3113.14 → 3113.64] for that.
[3114.54 → 3115.30] Do you know what else?
[3115.70 → 3116.06] Yeah.
[3116.24 → 3120.30] You can always go to general and at the top, the invite is right there.
[3120.30 → 3120.40] Yeah.
[3121.00 → 3125.70] So, no, I mean for where it invites signing you up, where you can sign yourself up.
[3126.02 → 3127.02] There's the auto sign up.
[3127.14 → 3130.12] It's like invite or slack.golangbridge.
[3130.12 → 3130.66] Yeah, that's right.
[3131.16 → 3133.30] Invite.slack.golangbridge.org.
[3133.40 → 3134.16] That's what I mean.
[3134.22 → 3137.62] If you want to get that link, go to the general channel.
[3138.06 → 3140.26] Right at the top is one of the links listed.
[3140.26 → 3141.46] Okay.
[3142.34 → 3148.60] So, invite.slack.golangbridge.org to join the Slack.
[3149.06 → 3152.84] And there's also the Changelog Slack, which links with it if you want to chat with us,
[3153.14 → 3154.60] and especially in real time.
[3155.24 → 3156.94] And with that, thanks, everybody.
[3157.16 → 3157.82] See you next week.
[3158.42 → 3158.78] Bye.
[3158.90 → 3159.28] Thank you.
[3162.02 → 3162.46] All right.
[3162.48 → 3164.54] That's it for this episode of Go Time.
[3164.54 → 3167.50] Tune in live on Thursdays at 3 p.m.
[3167.92 → 3170.76] U.S. Eastern at changelog.com slash live.
[3171.30 → 3174.02] Join the community and Slack with us in real time during the shows.
[3174.14 → 3176.42] Head to changelog.com slash community.
[3177.12 → 3177.66] Follow us on Twitter.
[3177.82 → 3179.54] We're at GoTimeFM.
[3179.98 → 3182.36] Special thanks to Vastly, our bandwidth partner.
[3182.70 → 3184.20] Head to fastly.com to learn more.
[3184.64 → 3185.42] Also, Linde.
[3185.54 → 3187.76] We host everything we do on Linde servers.
[3188.32 → 3190.20] Head to Linode.com slash changelog.
[3190.60 → 3192.68] Go Time is edited by Jonathan Young blood.
[3192.68 → 3196.36] And the theme music for Go Time is produced by the mysterious Break master Cylinder.
[3196.74 → 3197.80] We'll see you again next week.
[3198.06 → 3198.66] Thanks for listening.
