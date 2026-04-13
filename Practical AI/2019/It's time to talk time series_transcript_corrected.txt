[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.02] And unlike standard droplets, which use shared virtual CPU threads,
[29.02 → 32.88] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.40 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.36 → 45.20] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.20 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 → 88.54] productive, and accessible to everyone.
[88.94 → 93.42] This is where conversations around AI, machine learning, and data science happen.
[93.42 → 98.20] Join the community and snag with us around various topics of the show at changelog.com slash community.
[98.42 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.48 → 102.30] And now onto the show.
[107.20 → 111.10] Welcome to another episode of Practical AI.
[111.50 → 112.90] This is Daniel Whiten ack.
[113.04 → 116.00] I'm a data scientist with SIL International,
[116.00 → 118.72] and I'm joined by my co-host Chris Benson,
[118.98 → 122.52] who is a principal AI strategist with Lockheed Martin.
[122.76 → 123.42] How are you doing, Chris?
[123.74 → 124.34] Doing great.
[124.42 → 125.04] How's it going, Daniel?
[125.60 → 126.52] It's going good.
[126.58 → 129.50] It's looking a little bit more like fall around here,
[129.62 → 130.94] which is a really nice time of year.
[131.10 → 133.40] So I'll have to get out the leaf blower soon,
[133.58 → 135.38] but otherwise doing pretty good.
[135.84 → 136.04] Yep.
[136.12 → 138.28] It's finally starting to cool down here in the south,
[138.40 → 139.88] so I'm looking forward to cooler weather.
[140.40 → 140.74] Yeah.
[141.00 → 141.44] Nice.
[141.60 → 141.90] Nice.
[141.90 → 145.58] Well, speaking of times changing,
[146.06 → 148.30] we have a guest today that's going to help us
[148.30 → 151.54] dive into some things about time series data
[151.54 → 153.40] and other related things.
[153.56 → 157.88] We have Anais Doris-Georgiou from Influx Data with us.
[157.98 → 158.66] Welcome, Anais.
[159.28 → 159.56] Hi.
[159.64 → 160.44] Thank you so much.
[160.60 → 161.40] It's nice to be here.
[162.06 → 162.42] Yeah.
[162.60 → 164.06] We're so happy to have you.
[164.22 → 167.88] We saw your talk listed on the All Things Open website.
[168.02 → 170.44] A couple of people from the changelog were there,
[170.44 → 173.76] and I'm really excited to dig into a few of those details
[173.76 → 174.76] and other things.
[174.94 → 176.22] But before we do that,
[176.28 → 178.34] why don't you just give us a little bit of an intro
[178.34 → 181.96] about how you got into data things
[181.96 → 184.64] and eventually ended up at Influx Data?
[185.30 → 185.66] Sure.
[185.86 → 188.76] So originally my background is in chemical engineering,
[188.90 → 190.42] at least that's what I went to school for.
[191.00 → 192.56] And when I got straight out of school,
[192.56 → 196.12] I thought maybe that I wanted to go into biotech
[196.12 → 197.32] and do research.
[197.32 → 202.50] And I spent some time working with a liquid handling robot.
[203.08 → 206.56] And after a little while of just kind of being
[206.56 → 209.32] in the sterile environment where my only friend
[209.32 → 210.08] was this robot.
[211.58 → 213.04] So liquid handling robot,
[213.16 → 216.28] like a robot that handles hazardous chemicals?
[216.52 → 217.10] Is that the idea?
[217.18 → 219.08] Well, it didn't handle hazardous chemicals.
[219.56 → 221.76] It essentially was like a micropipette
[221.76 → 226.24] and could execute protocol in a larger scale.
[226.24 → 230.10] So it could replicate a single experiment,
[230.10 → 231.48] like, yeah, more efficiently.
[232.42 → 232.90] Yeah.
[232.96 → 236.10] So it was more like an automation thing versus like,
[236.30 → 237.44] first, when you were talking about that,
[237.46 → 240.66] I had like those like open AI robot hands in mind,
[240.66 → 243.64] like carrying like test tubes around or something.
[244.06 → 245.08] Yeah, that would be really cool.
[245.14 → 247.50] This carried around tiny volumes of liquid,
[247.86 → 249.74] but nothing quite like that.
[249.74 → 252.46] We're recording this around Halloween.
[252.46 → 254.08] And so I was just thinking, you know,
[254.14 → 256.26] liquid nitrogen bubbling over the side.
[256.42 → 257.56] It could be a lot of fun.
[258.00 → 259.72] I honestly, maybe I would have stayed longer
[259.72 → 261.76] if I had been messing with a robot
[261.76 → 263.04] that was handling liquid nitrogen.
[263.32 → 263.46] So.
[264.14 → 264.98] Well, maybe someday.
[265.38 → 265.68] Maybe.
[266.34 → 267.24] We can all aspire.
[267.34 → 267.56] Right.
[267.56 → 270.98] But yeah, so I did that.
[271.20 → 274.02] And I decided I didn't like being in a sterile room
[274.02 → 275.64] with only a robot to talk to.
[276.18 → 279.06] And I got to work with some data scientists
[279.06 → 283.28] who were actually creating the detection algorithms
[283.28 → 285.38] for the work that I was doing
[285.38 → 288.30] and basically all the data that I was collecting.
[288.66 → 290.86] And they were trying to detect autism,
[291.32 → 293.28] prenatal, do prenatal testing for autism.
[293.28 → 296.38] And I felt like the data scientists
[296.38 → 298.52] were the ones that really got to have all the fun
[298.52 → 301.40] because they didn't have to do the same procedure
[301.40 → 303.80] over and over again just to collect the data.
[303.92 → 305.70] They got to actually take the results
[305.70 → 307.86] and then derive meaning out of it.
[308.14 → 311.26] So I decided maybe I should go down that path.
[311.36 → 313.84] And that way, maybe I'll even get to talk to humans more,
[314.06 → 315.46] which I don't know, is kind of funny
[315.46 → 316.54] when I think about it now
[316.54 → 318.38] because people usually think about tech
[318.38 → 320.88] being a little bit more sterile
[320.88 → 323.02] or fewer people facing.
[323.28 → 325.22] But especially in the role that I have now,
[325.60 → 326.78] it's extremely people facing.
[326.78 → 328.02] And I really enjoy that.
[328.24 → 330.42] And I was missing that from biotech.
[331.06 → 332.86] Your role now is developer advocate.
[332.98 → 333.36] Is that right?
[333.94 → 334.18] Yeah.
[334.40 → 337.30] So are you familiar with what a developer advocate does?
[337.66 → 341.36] So I am, but I expect that there's a lot of confusion out there.
[341.46 → 344.14] So maybe it would be good to have a developer advocate
[344.14 → 345.26] define it for us.
[345.34 → 345.54] Okay.
[345.84 → 349.20] Well, every developer advocate seems to have a different answer
[349.20 → 352.70] for what developer advocacy or developer relations is.
[352.70 → 357.48] Well, for the record, your definition will stand at practical AI
[357.48 → 359.54] because you're the first one to define it.
[359.70 → 361.42] So it's canonical for us.
[361.66 → 362.00] Oh, no.
[362.38 → 362.86] Okay.
[363.08 → 366.00] Well, I would just define it as,
[366.22 → 370.10] and I think this is borrowing from a lot of other developer advocates,
[370.30 → 374.40] but basically a way to connect the company to the community
[374.40 → 375.92] and the community back to the company.
[375.92 → 381.38] So our role is to facilitate the use of our product,
[381.38 → 383.96] but also to bring product feedback.
[384.58 → 386.52] So kind of just establishing that bridge.
[387.28 → 391.34] And that looks like, takes the form of giving presentations,
[392.00 → 395.76] going to meetups, having meetups, writing blogs and tutorials,
[396.58 → 399.18] maybe contributing to documentation or the product itself,
[399.18 → 403.08] and hopefully having interactions with product
[403.08 → 407.24] to help guide the product in the direction that the community needs.
[407.24 → 410.46] Was that a sort of natural transition for you?
[410.64 → 415.18] Did you do like data science kind of as a title,
[415.42 → 417.42] you know, data scientist for a while,
[417.42 → 419.80] or did you kind of immediately want to get into this
[419.80 → 422.84] or more of a developer focused side of things?
[422.84 → 426.10] Because I definitely think that, you know, both are important.
[426.10 → 430.06] It sounds like the kind of developer facing side was really important to you.
[430.84 → 433.12] Yes, I wasn't ever a data scientist.
[433.94 → 437.54] I took a data science boot camp, the University of Texas in Austin.
[438.50 → 443.86] And I headed towards data science because I did a lot of math as an undergraduate
[443.86 → 445.52] and I really enjoy math.
[446.72 → 449.30] And data science felt to me like an opportunity
[449.30 → 452.44] where I'd get to use math and get to think about math.
[452.52 → 453.86] So that's what attracted me to it.
[453.86 → 456.44] And also the fact that you get to solve problems
[456.44 → 458.94] by thinking critically and looking at data
[458.94 → 460.72] and trying to uncover solutions
[460.72 → 463.58] and also reevaluating your biases and stuff.
[463.92 → 467.94] So developer advocate, I think, is misunderstood by a lot of people,
[467.94 → 471.24] but even more so probably like data scientist
[471.24 → 472.50] and what that entails.
[472.50 → 477.84] And like being a developer advocate for a data focused company,
[477.84 → 481.04] it seems really needed thing right now
[481.04 → 485.08] when like so much is misunderstood about how people are processing data,
[485.62 → 487.44] like what data science is in general,
[487.66 → 489.24] what we should, what we shouldn't be doing,
[489.56 → 491.42] what developers actually want to do.
[491.90 → 494.96] So yeah, I could see how it could be a very challenging position,
[495.20 → 496.40] but definitely very valuable.
[497.04 → 498.14] Yeah, it's definitely challenging.
[498.52 → 500.62] You get, I tend to get two camps of people,
[500.72 → 502.70] people who are either just breaking into the field
[502.70 → 506.32] or people who seem to have like several years experience
[506.32 → 509.64] and PhDs and spend most of the time educating me,
[509.84 → 511.90] which is, I mean, I get to learn a lot.
[512.00 → 513.02] So I'm always grateful.
[513.86 → 515.74] But yeah, I think it can definitely be tricky
[515.74 → 517.70] because I sort of try to position myself
[517.70 → 522.06] towards helping people break into data science
[522.06 → 523.54] and also data analytics.
[524.06 → 526.22] And so there are a lot of opinions
[526.22 → 528.96] about how one should handle their data.
[529.22 → 532.12] And so it can be tough trying to, you know,
[532.16 → 534.54] talk to the both extremes of that audience
[534.54 → 536.44] because they have such different needs
[536.44 → 539.68] and such vastly different knowledge base.
[539.84 → 542.36] It's really hard to talk about math
[542.36 → 544.84] with people who are just learning about math
[544.84 → 548.54] and also people who have PhDs in math in the same room.
[549.26 → 550.08] Fair enough.
[550.14 → 551.72] And I think that of the three of us,
[551.74 → 553.54] I'm probably the weakest in math.
[553.70 → 555.98] And so I'll probably have all sorts of questions
[555.98 → 557.90] as we go through the conversation for you.
[558.60 → 561.10] I actually wanted to start off by asking,
[561.62 → 564.06] through the course of the beginning of this conversation,
[564.06 → 566.98] you know, the phrase time series has come up several times.
[567.42 → 569.06] And I was wondering if you would,
[569.28 → 571.22] for those who are maybe just getting into it
[571.22 → 573.04] or not previously familiar,
[573.16 → 576.56] if you would kind of tell us what time series is and means
[576.56 → 578.46] and give us a little background on that.
[578.92 → 579.06] Sure.
[579.24 → 581.24] So time series is just any data
[581.24 → 583.42] that has a timestamp attached to it.
[583.80 → 588.64] So probably the most common example is stock price.
[588.86 → 591.00] And another really tangible one is weather
[591.00 → 592.52] or temperature data, right?
[592.52 → 593.78] Because you have your temperature
[593.78 → 596.86] and that temperature happens at a certain time.
[597.36 → 598.78] But what we're finding out,
[598.84 → 601.18] or I think what people are finally coming to recognize
[601.18 → 603.26] is that time series data
[603.26 → 607.36] is present in almost every industry.
[607.78 → 610.94] So if you think about industrial IoT
[610.94 → 612.44] or any sort of industry
[612.44 → 614.04] where you have chemical industry,
[614.18 → 616.50] petroleum, et cetera, biotech, it doesn't matter.
[616.66 → 618.12] You have a lot of sensors,
[618.32 → 619.66] you're monitoring your environments,
[619.66 → 621.62] you need to find out the pressure and temperature
[621.62 → 624.76] of maybe a pipe or heat exchanger.
[624.76 → 626.28] And you need to collect that data
[626.28 → 629.20] to make sure that your process is running smoothly
[629.20 → 633.26] and that you're not going to have any risk of explosions
[633.26 → 636.56] or any sort of damage to your process
[636.56 → 638.16] and the people that work there.
[638.16 → 643.34] You have examples of time series also in DevOps monitoring,
[643.94 → 644.88] continuous integration,
[645.62 → 647.40] application monitoring is a big one.
[647.98 → 650.00] So obviously it exists all throughout tech.
[650.26 → 652.52] We can also think about time series
[652.52 → 655.60] also existing for patients in healthcare
[655.60 → 656.82] where you need to monitor
[656.82 → 660.16] maybe the different attributes of their health over time.
[660.16 → 664.40] And we also have customers using Influx
[664.40 → 668.20] for monitoring the growth of their farms
[668.20 → 669.58] or their greenhouses.
[670.12 → 674.82] We have customers using us to monitor solar panels.
[676.12 → 678.38] CERN used Influx to monitor
[678.38 → 680.58] all of their particle accelerators
[680.58 → 682.92] and help them find the God particle.
[683.22 → 685.30] So really time series
[685.30 → 689.34] and probably because we live like we are in space time,
[689.34 → 692.10] time series data exists everywhere.
[692.40 → 694.34] So people are finally coming to realize
[694.34 → 695.26] that that data is valuable
[695.26 → 697.14] and that they probably could benefit
[697.14 → 699.76] from actually trying to store it.
[700.66 → 702.34] So I guess you really have demonstrated
[702.34 → 704.08] that it is just about universal.
[704.40 → 705.96] You know, there's an application for it
[705.96 → 707.72] in I guess almost any industry.
[707.90 → 711.64] I am curious just as a follow-up to your own background,
[712.02 → 714.56] what is it about working with time series data
[714.56 → 716.82] that has attracted you personally?
[716.82 → 719.92] And of that, do you have a particular use case
[719.92 → 720.64] that you've worked on
[720.64 → 722.42] that was the most interesting to you?
[722.96 → 724.92] Yeah, I really like the CERN use case.
[725.06 → 726.30] I like it for two reasons.
[726.42 → 728.08] One, because as a developer advocate,
[728.28 → 730.52] I help the open source users primarily.
[730.86 → 734.32] And so anytime that I have an open source user
[734.32 → 736.32] who's doing something really cool with the product,
[736.82 → 737.48] it makes me happy.
[738.00 → 739.94] And they were able to monitor
[739.94 → 741.26] all of their particle accelerators
[741.26 → 742.24] using the open source.
[742.72 → 743.56] I think that's pretty cool.
[743.56 → 746.86] And by the way, you mentioned God particle a moment ago.
[746.96 → 749.06] I'm assuming that you're talking about the Higgs boson.
[749.58 → 752.04] And for just, I know this isn't a physics thing,
[752.10 → 754.16] but if you would take just one second
[754.16 → 755.78] for anyone that hadn't heard that
[755.78 → 758.24] and might think it's a religious connotation
[758.24 → 759.38] rather than a scientific one,
[759.74 → 761.62] could you tell us for just two seconds
[761.62 → 763.94] what the Large Hadron Collider is doing
[763.94 → 765.94] in that project that attracted your attention
[765.94 → 767.16] and what the Higgs boson is?
[767.34 → 768.02] Kind of short answer.
[768.02 → 768.46] Sure.
[768.76 → 771.92] So basically they're colliding atoms into each other
[771.92 → 775.46] to try and figure out all the subatomic particles.
[776.32 → 780.86] And there's one particle that was called the God particle
[780.86 → 783.46] and it is actually known as the Higgs boson.
[783.94 → 786.72] So that's like a subatomic like micro particle.
[786.84 → 787.70] I don't actually know the right word
[787.70 → 788.42] because I'm not a physicist.
[788.94 → 790.38] And Daniel, you should hop in as well.
[790.68 → 790.86] Yeah, please.
[790.96 → 791.64] You're doing great.
[791.76 → 793.36] Probably better than I could do, actually.
[793.36 → 798.52] So yeah, so basically after two protons collide,
[798.68 → 801.24] then this is a byproduct, this Higgs boson,
[801.34 → 803.12] which is sometimes referred to as the God particle.
[803.62 → 805.10] And they were trying to find that.
[805.60 → 807.58] And because I think it was at the time,
[808.12 → 809.22] and maybe it still is,
[809.50 → 811.64] I don't really know where the phrase comes from,
[811.68 → 814.78] but I think it was like the smallest particle in the universe.
[814.90 → 816.50] So the idea being that maybe that's where
[816.50 → 818.48] everything else came from in the universe.
[818.48 → 822.30] And so if we can find or prove that the Higgs boson exists,
[822.30 → 825.60] then we can find like the most fundamental building block
[825.60 → 826.24] of the universe.
[826.44 → 829.18] And that could be referred to as the God particle.
[830.26 → 830.32] Yeah.
[830.44 → 833.28] So there's like, they call it the standard model, I think.
[833.40 → 835.50] And this is outside my domain as well.
[835.60 → 838.76] But yeah, it was like a missing piece of that standard model
[838.76 → 841.86] that could help them really put all the pieces together
[841.86 → 843.42] of how things were formed.
[843.78 → 845.38] So yeah, it's super exciting.
[845.52 → 848.02] Were you able to go visit CERN during that project
[848.02 → 850.10] or just talk to people?
[850.10 → 852.02] No, I actually didn't talk to people
[852.02 → 853.98] and I wasn't at the company when this was happening.
[854.12 → 855.48] I heard about it afterwards.
[855.86 → 856.04] Yeah.
[856.60 → 857.60] It's just cool, isn't it?
[857.60 → 858.06] Yeah, exactly.
[858.70 → 861.30] Well, maybe you'll get assigned to that project
[861.30 → 861.96] at some point.
[862.04 → 862.48] That'd be cool.
[862.76 → 864.84] I'm sure that they still have other time series
[864.84 → 866.04] that they need to analyze.
[866.28 → 866.74] I hope so.
[866.82 → 867.48] That would be cool.
[868.14 → 868.38] Yeah.
[868.56 → 872.18] So, I mean, I was actually trying to think about like,
[872.40 → 873.60] while you both were talking,
[873.64 → 874.40] I was trying to think about
[874.40 → 878.50] what is like not a time series that I work with.
[878.50 → 880.68] And there's certainly things that aren't,
[880.68 → 883.02] you know, time stamped that I work with,
[883.14 → 886.50] but pretty much any data could be time stamped, right?
[886.52 → 888.44] Like I was thinking of images
[888.44 → 890.36] like I'm taking with my phone, right?
[890.48 → 894.16] And like an image is that sort of,
[894.20 → 897.62] you know, matrix representation of reality.
[897.62 → 899.84] But actually, you know, as I scroll through my phone,
[899.96 → 902.36] you know, it says photos from today
[902.36 → 903.68] or yesterday or before.
[903.68 → 906.90] So there's actually a time series of photos on my phone.
[906.90 → 909.04] So it's really kind of all encompassing.
[909.12 → 911.30] And I guess it's time series data
[911.30 → 913.58] could be like a timestamp
[913.58 → 915.24] matched with any type of data,
[915.24 → 918.28] not just like a numerical type of data.
[918.38 → 921.78] It could be other forms of data too, right?
[922.38 → 922.78] For sure.
[923.08 → 925.22] There are a ton of papers out there
[925.22 → 929.00] that incorporate the use of LSTMs,
[929.28 → 930.78] long short-term memory networks,
[931.18 → 933.00] for image classification,
[933.16 → 934.18] like you're talking about.
[934.18 → 937.30] Because it turns out that if we wanted to classify,
[937.52 → 939.28] like let's say the scenes of The Breakfast Club,
[939.68 → 944.06] and we took any random still from that movie,
[944.22 → 946.14] it would probably contain four kids
[946.14 → 948.04] and it would be really hard to classify.
[948.68 → 951.98] But if we use a temporal element to those images
[951.98 → 954.12] and we look at the images that came before
[954.12 → 955.80] and the images that came after
[955.80 → 959.60] as an effort to classify various stills from that image,
[959.60 → 961.96] then all of a sudden we've provided context, right,
[962.02 → 962.78] for those images
[962.78 → 966.96] and it vastly improves the classification of images.
[967.28 → 968.98] So yeah, you're completely right.
[969.08 → 971.46] Like even though Influx isn't really a platform
[971.46 → 973.60] to storing that type of data specifically,
[973.98 → 977.28] that's definitely also can be thought of this time series.
[977.28 → 990.74] This episode is brought to you by Rubicon, CloudNativeCon,
[990.84 → 993.50] and you are invited to attend this flagship conference
[993.50 → 995.34] from the Cloud Native Computing Foundation,
[995.50 → 998.36] Rubicon, CloudNativeCon, North America 2019.
[998.70 → 1001.04] It's happening November 18th through the 21st
[1001.04 → 1002.42] in San Diego, California.
[1002.42 → 1005.94] This conference gathers adopters and technologists
[1005.94 → 1008.46] from leading up a source in cloud native communities.
[1008.84 → 1011.78] Use the code KCNAPracticalAI19,
[1012.02 → 1014.54] again KCNAPracticalAI19,
[1014.82 → 1016.22] to get 10% off registration
[1016.22 → 1018.50] or check the show notes for a special link to register
[1018.50 → 1020.88] and a link to the Convince Your Boss letter.
[1021.24 → 1022.32] Again, check the show notes for links
[1022.32 → 1023.58] to learn more and register.
[1032.42 → 1040.08] So I wanted to start off the next section
[1040.08 → 1043.86] by asking about what InfluxDB is.
[1043.98 → 1045.80] Could you give us a little bit of background
[1045.80 → 1047.30] about what Influx is
[1047.30 → 1049.54] and kind of what it's trying to solve?
[1049.78 → 1050.06] Sure.
[1050.26 → 1053.66] So InfluxDB is a time series database
[1053.66 → 1057.34] and it is trying to solve the problem
[1057.34 → 1062.00] of being able to store or ingest time series data
[1062.00 → 1064.78] and what makes time series data unique
[1064.78 → 1068.12] is that you usually need to be able
[1068.12 → 1071.12] to write huge, huge volumes.
[1071.62 → 1076.98] So Influx has been made as an append-only database
[1076.98 → 1080.30] to prioritize really high writes
[1080.30 → 1084.02] to allow you to ingest data
[1084.02 → 1085.34] at the nanosecond precision
[1085.34 → 1090.32] and also be able to then query that data in real time.
[1090.32 → 1093.66] So if I'm just thinking of stock price
[1093.66 → 1096.58] or some common time series example,
[1096.72 → 1098.12] you have your timestamp
[1098.12 → 1101.12] and you have the stock price.
[1101.22 → 1102.74] Maybe in a simple example,
[1102.84 → 1104.22] it's just those two things.
[1104.36 → 1109.68] So you could want to store those very quickly over time, right?
[1109.96 → 1113.80] And then what is a kind of query like
[1113.80 → 1116.18] that you might make on that stock price data?
[1116.28 → 1118.04] Is it like, I want to see the stock price
[1118.04 → 1119.70] from this time to this time?
[1119.70 → 1120.62] Or I want to see like,
[1120.68 → 1122.62] what was the average stock price during this time?
[1122.68 → 1125.00] What are those sorts of operations
[1125.00 → 1129.14] that you might want to do on time series data
[1129.14 → 1132.16] in a time series database like InfluxDB?
[1132.34 → 1132.60] For sure.
[1132.84 → 1134.92] So it uses two languages.
[1135.40 → 1137.74] It depends on what version you're using.
[1138.06 → 1140.10] If you're using 2.0,
[1140.44 → 1144.02] then we have created a functional query language
[1144.02 → 1146.06] and scripting language called Flux.
[1146.54 → 1148.34] And it's kind of JavaScript-issue.
[1148.78 → 1150.50] It has a lot of pipe forwards,
[1151.18 → 1153.56] which to me help increase the readability of it.
[1153.80 → 1157.52] And that would be like from this bucket called,
[1157.62 → 1158.80] you know, stock price.
[1159.26 → 1162.68] You know, I want to filter by this particular ticker
[1162.68 → 1165.62] and I want to specify my range
[1165.62 → 1168.38] as having this start time and this end time.
[1168.46 → 1169.86] And then you can apply
[1169.86 → 1171.68] a bunch of different functions to it,
[1171.68 → 1174.90] whether that's, in the case of stock prices,
[1175.06 → 1177.16] applying various sorts of analytics
[1177.16 → 1179.38] to those stock prices,
[1179.50 → 1181.48] like the Change Momentum Oscillator.
[1181.86 → 1184.26] Or maybe you want to do things
[1184.26 → 1187.14] like apply the average or find the derivative
[1187.14 → 1189.30] or look at the standard deviation
[1189.30 → 1190.88] for a group of time series.
[1191.74 → 1193.54] Yeah, there are a bunch of different functions you can do.
[1193.68 → 1195.62] And then if you're using the 1.x line,
[1195.62 → 1200.08] then you can use Influx,
[1200.34 → 1201.74] which is like SQL.
[1202.04 → 1202.62] It's very similar.
[1202.86 → 1205.34] And so you do select maybe all
[1205.34 → 1207.94] from this particular stock
[1207.94 → 1210.04] from the last five minutes or whatever.
[1210.58 → 1212.90] So we're kind of starting to get into,
[1212.96 → 1215.46] I guess these are just kind of query operations
[1215.46 → 1218.82] or queries that you might perform on time series data.
[1219.06 → 1221.88] Maybe you could give us a little bit of a sense as well
[1221.88 → 1225.08] about like the term time series analysis.
[1225.66 → 1228.00] And, you know, you have time series data.
[1228.10 → 1229.26] Let's say you have time series data.
[1229.42 → 1231.54] It's stored in nicely in InfluxDB.
[1231.90 → 1234.10] You can kind of query it in these ways
[1234.10 → 1235.90] to kind of get the data back
[1235.90 → 1237.24] in various different ways
[1237.24 → 1238.46] that you might be interested in.
[1238.76 → 1240.16] What is this whole range
[1240.16 → 1244.36] or this whole topic of time series analysis about?
[1244.60 → 1247.38] And kind of what buckets of analysis
[1247.38 → 1248.32] might you want to do?
[1248.32 → 1250.76] Like I'm thinking of forecasting, for example.
[1250.98 → 1253.60] It might be one type of thing,
[1253.84 → 1256.50] but maybe there's a bunch of different things.
[1256.58 → 1258.44] Could you let us know what those things are?
[1258.80 → 1258.94] Yeah.
[1259.14 → 1261.24] So, I mean, forecasting is one big bucket.
[1261.72 → 1263.94] Of course, that's why people collect time series data
[1263.94 → 1265.20] is because they want to try and predict
[1265.20 → 1266.34] what's going to happen in the future.
[1266.96 → 1268.82] But another is anomaly detection
[1268.82 → 1270.72] and trying to figure out
[1270.72 → 1273.70] if your environment is running smoothly
[1273.70 → 1276.22] or your plant is running smoothly
[1276.22 → 1278.66] and trying to protect against failures.
[1279.08 → 1281.72] And then beyond just forecasting,
[1281.90 → 1283.20] which is extremely complicated,
[1283.46 → 1284.56] you might need to look into
[1284.56 → 1286.36] the different statistical elements
[1286.36 → 1287.40] of your time series
[1287.40 → 1288.72] in order to find out
[1288.72 → 1291.22] which forecasting method you should use
[1291.22 → 1293.52] and which anomaly detection method
[1293.52 → 1294.48] makes the most sense.
[1294.48 → 1296.40] So I'm kind of curious,
[1296.62 → 1298.60] I'm going to approach it from the side of
[1298.60 → 1299.60] if you're a developer
[1299.60 → 1301.72] who's getting into time series data
[1301.72 → 1304.24] and you may or may not have done anything
[1304.24 → 1305.46] in the AI space,
[1305.84 → 1308.06] does Influx data automatically provide you
[1308.06 → 1310.94] a set of tools for which functions
[1310.94 → 1312.14] you might use?
[1312.20 → 1313.10] If I was a developer
[1313.10 → 1314.92] and had a use case in mind,
[1315.00 → 1316.18] how might I know
[1316.18 → 1318.44] what functions would be appropriate to apply
[1318.44 → 1319.62] and how would I go about doing that?
[1320.42 → 1321.80] So out of the box,
[1321.92 → 1323.14] Influx offers triple
[1323.14 → 1324.48] and double exponential smoothing.
[1324.74 → 1327.88] And that's a statistical forecasting method.
[1328.06 → 1330.78] So it doesn't involve any machine learning,
[1331.12 → 1332.90] any neural nets really.
[1333.38 → 1335.12] And so that's all that comes out of the box
[1335.12 → 1335.76] with Influx.
[1335.96 → 1337.52] Of course, there are client libraries,
[1337.82 → 1341.70] so you can always use some Python library
[1341.70 → 1343.54] or R library of your choosing
[1343.54 → 1345.10] that you're more familiar with.
[1345.22 → 1347.10] The act of figuring out
[1347.10 → 1349.44] which forecasting method you should use
[1349.44 → 1350.64] for your time series data
[1350.64 → 1352.60] is extremely complicated.
[1352.60 → 1355.00] It can be almost as complicated
[1355.00 → 1357.02] as you want it to be.
[1357.64 → 1359.72] Every forecasting method,
[1359.94 → 1361.48] every classical forecasting method
[1361.48 → 1362.42] and neural net
[1362.42 → 1364.74] has some underlying statistical assumptions
[1364.74 → 1365.52] about your data.
[1366.14 → 1367.80] So sort of one of the first steps
[1367.80 → 1368.68] that you can take
[1368.68 → 1369.84] is making sure
[1369.84 → 1371.70] whether your data
[1371.70 → 1373.18] violates one of those assumptions
[1373.18 → 1375.72] or on the other side
[1375.72 → 1376.92] matches the assumptions
[1376.92 → 1378.18] that maybe it contains,
[1378.18 → 1379.10] like for example,
[1379.30 → 1380.16] for Holt Winters
[1380.16 → 1381.54] or XXX exponential smoothing,
[1382.12 → 1382.86] one of the assumptions,
[1383.02 → 1383.58] two of the assumptions
[1383.58 → 1386.28] is that your data is non-stationary,
[1386.38 → 1387.44] meaning that it has trend.
[1387.84 → 1389.04] And the second assumption
[1389.04 → 1390.80] is that seasonality is present.
[1391.06 → 1392.28] So if your data
[1392.28 → 1393.52] doesn't have seasonality
[1393.52 → 1394.80] or it doesn't have trend,
[1394.92 → 1396.32] then you don't want to use Holt Winters
[1396.32 → 1398.72] to generate a prediction or forecast.
[1399.16 → 1400.38] So that's kind of the short answer.
[1400.66 → 1401.12] Does that help?
[1401.18 → 1401.94] Yeah, that helped a lot.
[1402.02 → 1402.50] I appreciate that.
[1402.86 → 1403.80] Yeah, so it's like,
[1403.88 → 1405.52] I don't know about maybe other people.
[1405.52 → 1407.84] I definitely get what you mean by
[1407.84 → 1410.72] there are so many things at play here.
[1410.88 → 1411.96] So like I kind of,
[1412.14 → 1413.72] whenever I look into time series
[1413.72 → 1416.14] and I have a couple of times in the past,
[1416.22 → 1417.42] especially when I was working
[1417.42 → 1419.04] with a telecom startup
[1419.04 → 1421.14] and doing some monitoring stuff,
[1421.14 → 1424.52] but there's like all of these elements of it.
[1424.66 → 1427.36] It's like how many like lags
[1427.36 → 1428.66] in your data is important
[1428.66 → 1430.94] and like moving average
[1430.94 → 1432.60] and seasonality,
[1432.90 → 1433.98] like trends,
[1434.10 → 1435.18] all of these things.
[1435.18 → 1437.94] For like people getting into this,
[1438.00 → 1438.96] do you have any suggestions
[1438.96 → 1442.08] for like a starting place
[1442.08 → 1444.76] or maybe like a starting type of data
[1444.76 → 1447.28] that they could kind of experiment with
[1447.28 → 1448.74] to kind of learn a little bit
[1448.74 → 1450.44] about all of these different elements?
[1450.44 → 1451.92] Because I definitely see what you're saying.
[1451.96 → 1452.92] It could be overwhelming.
[1453.38 → 1455.36] I actually recommend that people,
[1455.70 → 1457.08] like I try and identify
[1457.08 → 1460.02] the problem that they want to solve first.
[1460.02 → 1462.58] Because I think if you have a real problem,
[1462.58 → 1465.10] rather than just exploring theoretical data sets,
[1465.18 → 1467.30] you're a little bit more tied to the problem
[1467.30 → 1469.16] and you're a little bit more motivated
[1469.16 → 1471.48] to dive into the different attributes
[1471.48 → 1473.04] that your time series has.
[1473.12 → 1474.40] And also, hopefully,
[1474.52 → 1475.60] if you picked the data set,
[1475.66 → 1478.00] then you have some domain expertise
[1478.00 → 1479.14] about that data set
[1479.14 → 1480.16] and you understand it better.
[1480.36 → 1483.20] So I always recommend looking at a data set
[1483.20 → 1484.16] that you're familiar with.
[1484.66 → 1486.50] And then beyond there,
[1486.98 → 1488.36] in terms of good tools,
[1488.36 → 1491.52] I mean, I use scikit-learn.
[1491.66 → 1492.72] I'm a Pythons,
[1492.98 → 1495.72] so I will probably use scikit-learn
[1495.72 → 1499.50] to do sort of initial discovery
[1499.50 → 1500.46] about my data set
[1500.46 → 1502.48] and dive into the different attributes of it,
[1502.56 → 1503.50] looking at things like
[1503.50 → 1504.50] you're talking about like lag,
[1504.60 → 1505.50] auto-correlation,
[1506.00 → 1507.64] correlation between other data sets,
[1508.16 → 1509.34] all the statistical analysis,
[1509.54 → 1510.98] standard deviation, et cetera,
[1511.26 → 1512.86] just to get a feel
[1512.86 → 1515.00] for the attributes of my data set.
[1515.00 → 1517.38] And then whether,
[1517.46 → 1518.36] I think the next step,
[1518.64 → 1519.78] or the very first step maybe,
[1519.94 → 1521.66] is to determine whether
[1521.66 → 1523.50] your problem is univariate
[1523.50 → 1525.40] versus multivariate.
[1525.60 → 1526.82] So multivariate meaning
[1526.82 → 1528.60] that you have multiple time series
[1528.60 → 1530.26] that you want to account for
[1530.26 → 1531.96] when you're making a prediction
[1531.96 → 1533.68] or an anomaly detection.
[1533.94 → 1536.50] And then the second univariate
[1536.50 → 1538.12] is where you just have one time series.
[1538.64 → 1541.18] And the reason why it's important
[1541.18 → 1542.72] to identify whether
[1542.72 → 1545.40] your problem requires multivariate analysis
[1545.40 → 1546.84] or univariate analysis
[1546.84 → 1548.24] is because the way that you handle
[1548.24 → 1550.38] those two cases is entirely different.
[1550.56 → 1553.52] Turns out that if you are looking to do,
[1553.62 → 1554.14] for example,
[1554.76 → 1556.40] univariate time series forecasting,
[1557.22 → 1560.32] statistical methods work extremely well.
[1561.00 → 1562.40] And by statistical methods,
[1562.46 → 1563.30] you're kind of meaning
[1563.30 → 1565.92] non what we would consider
[1565.92 → 1567.30] like machine learning
[1567.30 → 1570.12] or AI methods in,
[1570.12 → 1572.66] I know that's like a very convoluted thing,
[1572.72 → 1573.88] like drawing the line there.
[1573.98 → 1575.30] But that's kind of the sense you mean,
[1575.36 → 1577.82] like statistical as a non machine learning,
[1577.90 → 1578.18] I guess.
[1578.62 → 1579.06] Right. Yeah.
[1579.06 → 1580.58] Like no neural nets, I guess,
[1580.82 → 1582.24] is how maybe I would describe it.
[1582.50 → 1583.84] Yeah. Everyone has a different description
[1583.84 → 1584.58] for machine learning.
[1584.74 → 1586.16] I hear sometimes people consider
[1586.16 → 1586.94] linear regression
[1586.94 → 1588.22] as technically machine learning
[1588.22 → 1589.98] because it like uses a machine
[1589.98 → 1591.14] to make like a forecast.
[1591.60 → 1593.26] But I'm like, I disagree.
[1593.36 → 1593.88] I'm like, no,
[1594.50 → 1595.44] I don't think we can call it
[1595.44 → 1597.74] linear regression machine learning.
[1597.96 → 1598.92] I'm with you on that.
[1598.92 → 1600.44] I guess I kind of make the distinction
[1600.44 → 1602.38] that neural nets I'd say.
[1603.02 → 1605.12] So I have a quick question for you there.
[1605.28 → 1606.50] As we, you know,
[1606.54 → 1607.90] we started talking about neural nets
[1607.90 → 1608.46] a little bit.
[1608.54 → 1609.24] I'm kind of curious,
[1609.40 → 1611.16] how does time series data
[1611.16 → 1612.54] and a database,
[1612.66 → 1613.64] in this case, InfluxDB,
[1613.80 → 1616.06] how does that fit into a workflow?
[1616.06 → 1617.58] If you're starting to think about
[1617.58 → 1618.84] neural network training
[1618.84 → 1620.38] or deployment or whatever,
[1620.38 → 1622.00] and you're kind of trying
[1622.00 → 1623.22] to put everything together
[1623.22 → 1625.20] that you and your team may need,
[1625.54 → 1627.08] where does this fit into that process?
[1627.08 → 1628.58] We don't have,
[1628.72 → 1630.30] I mean, I don't know very many people
[1630.30 → 1633.34] who are actually employing
[1633.34 → 1634.60] like online machine learning
[1634.60 → 1635.40] with neural nets.
[1635.62 → 1637.36] So a lot of people are found
[1637.36 → 1639.68] that using really simple methods
[1639.68 → 1641.34] like certain standard deviations
[1641.34 → 1642.16] away from the mean
[1642.16 → 1643.72] to define an anomaly
[1643.72 → 1646.32] works just fine for their use case.
[1646.92 → 1648.08] And so they don't bother
[1648.08 → 1650.52] with really fancy tools and methods.
[1650.76 → 1652.36] I guess I would probably,
[1652.54 → 1653.68] if I were building one myself,
[1653.68 → 1655.46] I would probably look into using
[1655.46 → 1658.34] H2O.ai with Influx together
[1658.34 → 1659.92] or maybe like BigQuery.
[1660.80 → 1661.68] And when you're talking about
[1661.68 → 1664.46] like online versus offline,
[1665.04 → 1665.78] am I correct in,
[1666.08 → 1667.80] so like online,
[1668.46 → 1670.96] you're kind of monitoring
[1670.96 → 1674.28] a stream of data that's coming in,
[1674.62 → 1676.14] a stream of time series data
[1676.14 → 1677.24] that's coming in some way
[1677.24 → 1678.94] and applying some method.
[1679.06 → 1680.16] Offline would be like,
[1680.54 → 1681.96] oh, you pull a bunch of,
[1681.96 → 1683.34] maybe you have InfluxDB
[1683.34 → 1685.64] and it's storing time series data.
[1685.84 → 1687.44] And then you like to make a query
[1687.44 → 1688.78] and pull some data out
[1688.78 → 1690.14] and then like load it
[1690.14 → 1691.48] into scikit-learn
[1691.48 → 1692.96] or something like you're talking about
[1692.96 → 1696.48] and do some sort of retrospective
[1696.48 → 1698.06] or historical analysis on it.
[1698.06 → 1699.68] Is that the sort of distinction?
[1700.18 → 1701.98] I think you basically touched upon it.
[1702.02 → 1703.76] I would consider online machine learning
[1703.76 → 1704.88] to be when you need
[1704.88 → 1705.92] to update your training.
[1706.54 → 1707.14] So training,
[1707.48 → 1708.48] especially for neural nets,
[1708.52 → 1709.74] can be pretty expensive
[1709.74 → 1711.44] and time-consuming.
[1711.66 → 1714.06] But if your data is changing a lot,
[1714.44 → 1716.14] then you might need
[1716.14 → 1717.20] to update your model.
[1717.62 → 1718.54] And so that would require
[1718.54 → 1719.62] retraining your model.
[1720.18 → 1723.24] And offline would essentially be
[1723.24 → 1724.92] that you've already trained your model.
[1725.26 → 1726.58] You only need to do that once
[1726.58 → 1727.30] for whatever reason,
[1727.46 → 1728.98] which unless your data
[1728.98 → 1730.02] is extremely consistent,
[1730.22 → 1731.34] and if it is that consistent,
[1731.56 → 1732.94] then maybe you can just use
[1732.94 → 1734.34] statistical methods.
[1734.34 → 1736.38] So I'm going off track.
[1736.58 → 1737.44] But online,
[1737.90 → 1738.78] updating your training,
[1739.72 → 1740.44] training again,
[1740.72 → 1741.44] and then for me,
[1741.48 → 1742.60] offline is
[1742.60 → 1744.58] maybe training just once.
[1744.58 → 1760.14] This episode is brought to you
[1760.14 → 1761.04] by Brave.
[1761.22 → 1763.02] The Brave team is on a mission
[1763.02 → 1764.14] to fix the web
[1764.14 → 1765.62] by building an open source,
[1766.04 → 1766.88] privacy focused,
[1767.12 → 1769.12] and performance oriented browser.
[1769.70 → 1771.66] Browse the web up to eight times faster
[1771.66 → 1772.62] than Chrome and Safari.
[1772.62 → 1775.18] Block ads and trackers by default
[1775.18 → 1776.94] and reward your favourite creators
[1776.94 → 1777.82] with the built-in
[1777.82 → 1779.26] basic attention token.
[1779.92 → 1781.10] Yes, you heard that right.
[1781.22 → 1783.28] A real world use case for blockchain.
[1783.94 → 1785.04] Download Brave for free
[1785.04 → 1786.46] using the link in the show notes
[1786.46 → 1787.72] and give tipping a try
[1787.72 → 1789.28] on changelog.com.
[1798.70 → 1800.78] So we're just getting into
[1800.78 → 1803.92] kind of statistical versus machine learning
[1803.92 → 1806.34] and also online versus offline.
[1806.34 → 1807.74] But if we kind of go back
[1807.74 → 1809.60] to the statistical
[1809.60 → 1812.26] versus machine learning side of things,
[1812.26 → 1814.52] I know that earlier in our conversation
[1814.52 → 1815.96] and also in some of your talks,
[1815.96 → 1817.12] you've talked about
[1817.12 → 1820.74] when you might want to go after
[1820.74 → 1822.82] statistical methods
[1822.82 → 1824.24] versus machine learning
[1824.24 → 1824.92] and neural nets
[1824.92 → 1827.28] and when you might want to do
[1827.28 → 1828.18] the opposite.
[1828.18 → 1829.84] Could you dive into that
[1829.84 → 1830.44] a little bit more
[1830.44 → 1832.12] specifically around time series?
[1832.32 → 1833.76] Like what are the signs
[1833.76 → 1834.86] maybe in your data
[1834.86 → 1836.14] that you should be looking for
[1836.14 → 1838.72] when statistical methods are enough
[1838.72 → 1839.58] and maybe they're better
[1839.58 → 1841.94] in terms of interpretability
[1841.94 → 1843.22] or efficiency or whatever?
[1843.92 → 1845.04] And what are the signs
[1845.04 → 1846.42] that maybe you need to do
[1846.42 → 1847.60] something a little bit more
[1847.60 → 1848.92] or maybe pull in a neural net?
[1849.64 → 1851.00] Yeah, so my answer
[1851.00 → 1853.14] and everyone has a different opinion,
[1853.28 → 1853.94] but for me,
[1854.02 → 1855.30] I think it makes sense
[1855.30 → 1856.86] to use statistical methods
[1856.86 → 1858.14] when you are only dealing
[1858.14 → 1859.98] with univariate time series data
[1859.98 → 1862.40] and use neural nets
[1862.40 → 1864.52] if you're using multivariate
[1864.52 → 1865.32] time series data
[1865.32 → 1866.74] and you're looking to do forecasts.
[1866.94 → 1869.02] There are some pretty efficient ways
[1869.02 → 1870.54] to do anomaly detection
[1870.54 → 1872.14] with multivariate data
[1872.14 → 1873.20] that are statistical
[1873.20 → 1874.30] or really simple.
[1874.90 → 1876.36] But yeah, so I'd say
[1876.36 → 1877.44] if you're looking at
[1877.44 → 1879.20] a group of time series,
[1879.38 → 1881.04] then use machine learning.
[1881.42 → 1884.14] Otherwise, use statistical methods.
[1884.14 → 1885.72] And I came to this conclusion
[1885.72 → 1887.44] because are you familiar
[1887.44 → 1889.36] with the Madurai's comps
[1889.36 → 1890.16] or Comps?
[1891.14 → 1891.70] No.
[1892.28 → 1892.56] Okay.
[1893.00 → 1895.14] So they are the benchmark
[1895.14 → 1897.12] for time series forecast methods.
[1897.60 → 1898.28] Now, unfortunately,
[1898.50 → 1899.64] they only evaluate
[1899.64 → 1901.68] univariate time series data,
[1902.28 → 1905.64] but they take 100,000 time series
[1905.64 → 1908.14] and they invite researchers
[1908.14 → 1909.04] from all over the world
[1909.04 → 1909.72] to participate
[1909.72 → 1911.20] and try and come up
[1911.20 → 1912.68] with the best forecasting method.
[1912.68 → 1914.56] And this event happens every year
[1914.56 → 1916.36] and then the results are published.
[1916.70 → 1917.76] Sounds like a party.
[1917.90 → 1918.42] Yeah, right?
[1919.58 → 1920.82] Last year, I think,
[1921.04 → 1921.90] is like in June,
[1922.32 → 1923.36] they just released
[1923.36 → 1925.48] the most recent results.
[1925.90 → 1926.70] And what they found
[1926.70 → 1928.84] was that a hybrid method
[1928.84 → 1930.60] of an RNN
[1930.60 → 1931.70] and exponential smoothing
[1931.70 → 1933.40] outperformed every other model.
[1933.40 → 1934.62] But if we looked
[1934.62 → 1935.54] or evaluate
[1935.54 → 1938.38] just the statistical methods
[1938.38 → 1940.50] versus machine learning methods,
[1940.68 → 1942.02] just the pure statistical
[1942.02 → 1942.72] or machine learning,
[1943.16 → 1944.30] the statistical methods
[1944.30 → 1945.82] outperform the machine learning methods.
[1946.08 → 1947.24] So while there might be
[1947.24 → 1948.38] some combination methods
[1948.38 → 1949.38] and some hybrid methods
[1949.38 → 1949.98] that outperform
[1949.98 → 1951.24] some statistical methods
[1951.24 → 1953.42] in univariate time series forecasting,
[1953.98 → 1955.60] really statistical methods,
[1955.68 → 1956.32] if you're just trying
[1956.32 → 1957.40] to like not generate
[1958.02 → 1959.32] your own forecasting method
[1959.32 → 1959.88] because you don't have
[1959.88 → 1960.82] that time or that resources
[1960.82 → 1961.64] and you're looking to pick
[1961.64 → 1962.80] between one or the other,
[1962.90 → 1964.06] it makes sense to use statistical
[1964.06 → 1966.48] for univariate time series data.
[1966.82 → 1967.70] That being said,
[1967.86 → 1969.26] we have the luxury now
[1969.26 → 1970.44] of monitoring
[1970.44 → 1972.78] a lot of different things,
[1972.88 → 1974.06] getting a lot of different data.
[1975.00 → 1976.40] And, you know,
[1976.46 → 1977.64] depending on the cost benefit
[1977.64 → 1978.92] to your business
[1978.92 → 1980.86] and the type of business decisions
[1980.86 → 1981.48] you'll be making
[1981.48 → 1982.58] based off of your forecast,
[1982.66 → 1983.40] it might make sense
[1983.40 → 1985.28] to go and spend
[1985.28 → 1986.02] extra effort
[1986.02 → 1987.44] to create multivariate
[1987.44 → 1988.48] time series forecasting
[1988.48 → 1991.04] and incorporate neural nets
[1991.04 → 1992.62] and tackle that problem,
[1992.68 → 1993.88] which is a lot harder.
[1994.76 → 1995.96] So got a question.
[1996.10 → 1997.16] And I remember actually
[1997.16 → 1999.20] watching your talk on YouTube.
[1999.46 → 2000.98] You covered that as well
[2000.98 → 2001.68] and talked about
[2001.68 → 2002.32] that comparison
[2002.32 → 2003.30] between statistical
[2003.30 → 2004.02] and machine learning
[2004.02 → 2005.16] and the fact that
[2005.16 → 2005.98] the statistical came.
[2006.34 → 2007.38] What I am wondering is,
[2007.50 → 2008.44] could you take that
[2008.44 → 2009.46] and put it into more
[2009.46 → 2011.04] of a kind of real life example
[2011.04 → 2012.38] just to make it tangible
[2012.38 → 2014.14] on where you might see
[2014.14 → 2015.84] that in reality come about?
[2015.96 → 2016.66] And it doesn't have
[2016.66 → 2018.08] to necessarily be a real event
[2018.08 → 2019.38] that you were part of
[2019.38 → 2019.72] or something,
[2019.82 → 2020.70] but just how you might
[2020.70 → 2021.60] think of it that way
[2021.60 → 2022.74] so that if someone's
[2022.74 → 2024.02] struggling to follow why
[2024.02 → 2024.80] and they hear you say
[2024.80 → 2027.28] that the statistical outperformed,
[2027.84 → 2028.52] kind of explain
[2028.52 → 2029.32] why that's the case.
[2030.00 → 2030.30] Why?
[2030.46 → 2030.82] I mean,
[2031.22 → 2032.88] the simplest answer for me
[2032.88 → 2035.38] is that a lot of neural networks
[2035.38 → 2037.54] like that are commonly used
[2037.54 → 2039.16] for time series data
[2039.16 → 2042.18] like RNNs and LSTMs,
[2042.54 → 2043.14] and I'm not talking
[2043.14 → 2043.90] about hybrid methods,
[2043.98 → 2044.70] just plain ones,
[2045.02 → 2046.72] they operate on the assumption
[2046.72 → 2047.66] that your data
[2047.66 → 2049.86] or the evaluation
[2049.86 → 2051.40] of the forecast
[2051.40 → 2052.70] operates on the assumption
[2052.70 → 2053.34] that your data
[2053.34 → 2055.18] doesn't exhibit autocorrelation.
[2055.54 → 2057.02] And autocorrelation
[2057.02 → 2058.74] is when a portion
[2058.74 → 2059.92] of your time series data
[2059.92 → 2060.60] is correlated
[2060.60 → 2062.44] to another portion of it
[2062.44 → 2064.30] in an earlier time.
[2064.78 → 2065.94] And that's often the case
[2065.94 → 2066.80] in the world
[2066.80 → 2068.40] where, like,
[2068.92 → 2070.02] if we monitored
[2070.02 → 2071.06] my hunger levels
[2071.06 → 2071.96] throughout the day,
[2071.96 → 2073.80] because I live
[2073.80 → 2076.32] a very regular lifestyle
[2076.32 → 2078.40] and I'm a creature of habit,
[2078.54 → 2079.58] I tend to be hungry
[2079.58 → 2081.46] at really predictable
[2081.46 → 2082.32] times of the day.
[2082.48 → 2083.02] And so,
[2083.62 → 2084.54] you'd find out
[2084.54 → 2086.42] that my hunger levels
[2086.42 → 2088.34] on today
[2088.34 → 2089.48] will be highly correlated
[2089.48 → 2090.66] with my hunger levels
[2090.66 → 2091.32] a month ago.
[2091.46 → 2092.12] And, like,
[2092.16 → 2093.38] you'll find that I'm hungry
[2093.38 → 2094.14] at the same times
[2094.14 → 2094.62] a month ago.
[2095.32 → 2096.42] And so,
[2096.84 → 2098.54] this pattern
[2098.54 → 2099.38] that exhibits
[2099.38 → 2100.70] that would be present
[2100.70 → 2101.70] in my, like,
[2101.74 → 2102.36] hunger data
[2102.36 → 2103.92] violates an assumption
[2103.92 → 2105.20] of how RNNs
[2105.20 → 2105.94] and LSTMs
[2105.94 → 2108.36] are often evaluated
[2108.36 → 2109.96] and it causes
[2109.96 → 2111.26] overfitting of the models.
[2112.04 → 2112.34] And so,
[2112.38 → 2113.02] that's kind of, like,
[2113.32 → 2114.14] the shortest answer
[2114.14 → 2114.82] I can provide.
[2115.02 → 2115.78] That was a good answer.
[2115.88 → 2116.70] Thank you very much.
[2117.24 → 2117.44] So,
[2117.48 → 2118.30] in the case of, like,
[2118.34 → 2120.08] the multivariate data,
[2120.84 → 2122.08] it's more of a
[2122.22 → 2122.48] like,
[2122.52 → 2123.48] there's more data,
[2123.66 → 2124.64] there's more complexity
[2124.64 → 2125.48] going on,
[2125.48 → 2126.12] and so,
[2126.30 → 2127.40] it may be harder
[2127.40 → 2128.70] to overfit
[2128.70 → 2129.20] and, like,
[2129.32 → 2129.96] neural networks
[2129.96 → 2131.04] are thus more,
[2131.76 → 2132.16] you know,
[2132.54 → 2133.08] appropriate,
[2133.34 → 2133.70] I guess.
[2133.82 → 2134.40] Would that be
[2134.40 → 2136.20] a reasonable statement
[2136.20 → 2137.06] kind of generally?
[2137.24 → 2138.48] It's a fairly general statement.
[2138.62 → 2138.94] For sure.
[2139.06 → 2139.60] I like that.
[2140.22 → 2141.18] And when you're talking
[2141.18 → 2142.14] about this sort of
[2142.14 → 2143.36] multivariate scenarios,
[2143.36 → 2144.56] I was just kind of curious
[2144.56 → 2146.10] from your experience
[2146.10 → 2147.66] working with developers,
[2148.24 → 2149.70] what's the sort of range
[2149.70 → 2151.24] of number
[2151.24 → 2152.36] of time series
[2152.36 → 2153.30] that people
[2153.30 → 2154.38] are putting together
[2154.38 → 2154.94] in these
[2154.94 → 2156.98] multivariate models?
[2157.14 → 2157.64] Is it, like,
[2157.64 → 2158.86] a bunch,
[2158.96 → 2159.46] like hundreds,
[2159.78 → 2160.96] or is it generally
[2160.96 → 2161.80] like a handful
[2161.80 → 2163.00] of time series,
[2163.60 → 2163.76] like,
[2163.84 → 2163.92] oh,
[2163.92 → 2164.38] you've got
[2164.38 → 2165.56] three different sensors
[2165.56 → 2166.16] and you're putting
[2166.16 → 2166.70] those together
[2166.70 → 2167.52] or something like that?
[2167.84 → 2168.00] Yeah,
[2168.08 → 2168.68] I can range
[2168.68 → 2169.32] from both
[2169.32 → 2170.04] of those extremes.
[2170.58 → 2170.76] So,
[2170.92 → 2171.80] in the hundreds
[2171.80 → 2172.96] case,
[2173.16 → 2173.94] I imagine
[2173.94 → 2174.78] that these are
[2174.78 → 2175.30] pretty
[2175.30 → 2176.74] computationally
[2176.74 → 2177.20] expensive
[2177.20 → 2178.48] things,
[2178.48 → 2178.82] and there's
[2178.82 → 2179.76] a lot of complexity
[2179.76 → 2181.46] in terms of the model
[2181.46 → 2182.02] and all that.
[2182.18 → 2182.52] Are there,
[2183.08 → 2183.30] like,
[2183.34 → 2183.94] when you're working
[2183.94 → 2185.66] with time series,
[2186.20 → 2187.10] I'm trying to make
[2187.10 → 2187.54] the connection
[2187.54 → 2189.60] with some of the things
[2189.60 → 2190.28] I'm familiar with,
[2190.36 → 2190.54] like,
[2190.62 → 2191.82] sequence-to-sequence models
[2191.82 → 2192.52] for text
[2192.52 → 2193.50] and that sort of thing.
[2193.92 → 2194.60] When you have,
[2194.64 → 2194.84] like,
[2194.90 → 2195.50] a bunch
[2195.50 → 2196.20] of different
[2196.20 → 2197.64] time series,
[2197.92 → 2198.80] is it just
[2198.80 → 2200.22] kind of that
[2200.22 → 2201.70] but on steroids,
[2201.84 → 2202.16] I guess?
[2202.56 → 2202.76] Yeah.
[2202.84 → 2203.50] In terms of,
[2203.60 → 2203.70] like,
[2203.70 → 2204.46] how you prepare
[2204.46 → 2205.06] the data
[2205.06 → 2205.34] and,
[2205.56 → 2205.60] like,
[2205.64 → 2206.54] the types of,
[2206.66 → 2208.00] you mentioned RNNs
[2208.00 → 2208.78] and LSTMs
[2208.78 → 2209.46] and that sort of thing,
[2209.52 → 2210.12] so it's kind of
[2210.12 → 2210.92] similar,
[2211.14 → 2211.68] it's just,
[2211.80 → 2212.14] you know,
[2212.22 → 2213.14] kind of on steroids,
[2213.14 → 2213.56] I guess.
[2213.94 → 2214.20] Yeah.
[2214.36 → 2214.96] I'm not sure
[2214.96 → 2215.68] I understand your question,
[2215.78 → 2216.28] but I agree.
[2217.48 → 2217.80] Yeah.
[2217.92 → 2218.28] Okay.
[2218.76 → 2219.00] No,
[2219.04 → 2219.96] it wasn't really a question.
[2220.08 → 2220.86] I was just trying to
[2220.86 → 2223.08] kind of get a mental model
[2223.08 → 2224.50] of it in my mind,
[2224.52 → 2224.88] I guess.
[2225.24 → 2225.48] But,
[2225.54 → 2226.26] yeah,
[2226.42 → 2227.24] I was wondering,
[2227.66 → 2228.04] you know,
[2228.52 → 2229.54] we've talked a lot
[2229.54 → 2230.50] about a ton
[2230.50 → 2231.58] of different methods
[2231.58 → 2233.36] and you've mentioned
[2233.36 → 2234.66] and kind of described
[2234.66 → 2235.36] Influx DV
[2235.36 → 2237.20] and what's available there.
[2237.42 → 2239.48] As a developer advocate,
[2239.74 → 2240.72] I wanted to give you
[2240.72 → 2241.24] the chance
[2241.24 → 2242.84] also to kind of share
[2242.84 → 2243.34] a little bit
[2243.34 → 2244.38] about how people
[2244.38 → 2245.70] might get started
[2245.70 → 2246.90] with InfluxDB
[2246.90 → 2248.54] and like what they
[2248.54 → 2249.30] might need
[2249.30 → 2250.38] to get spun up
[2250.38 → 2250.92] or if they can
[2250.92 → 2252.24] test it on their
[2252.24 → 2252.96] local machine
[2252.96 → 2253.60] and maybe,
[2253.76 → 2254.44] you know,
[2254.48 → 2255.36] put some of their
[2255.36 → 2256.40] time series data
[2256.40 → 2257.08] into it
[2257.08 → 2258.04] and that sort of thing.
[2258.10 → 2258.62] How can people
[2258.62 → 2259.10] get started?
[2259.50 → 2259.66] Yeah,
[2259.72 → 2261.00] so we just released
[2261.00 → 2262.74] a cloud offering
[2262.74 → 2263.66] and there's a free tier,
[2263.78 → 2264.30] so that's probably
[2264.30 → 2264.98] the easiest way
[2264.98 → 2265.50] because you just
[2265.50 → 2266.02] have to create
[2266.02 → 2267.32] a sign-up
[2267.32 → 2267.90] and then
[2267.90 → 2269.72] you're good to go.
[2269.72 → 2270.46] Otherwise,
[2270.78 → 2271.74] you can install
[2271.74 → 2272.44] the platform
[2272.44 → 2273.28] as a single binary
[2273.28 → 2274.02] and then
[2274.02 → 2274.98] I recommend
[2274.98 → 2275.48] checking out
[2275.48 → 2275.94] Telegraph
[2275.94 → 2276.58] even if you
[2276.58 → 2277.44] are not interested
[2277.44 → 2278.36] in InfluxDB.
[2278.68 → 2279.20] So Telegraph
[2279.20 → 2280.62] is a collection agent.
[2281.16 → 2281.86] It's a single binary
[2281.86 → 2283.64] and it's plugin driven
[2283.64 → 2285.40] and it's database agnostic
[2285.40 → 2287.30] so it's by far
[2287.30 → 2288.86] our most popular tool.
[2289.02 → 2289.52] There are over
[2289.52 → 2290.26] 180,
[2290.38 → 2291.16] 190 plugins
[2291.16 → 2292.46] so if you're looking
[2292.46 → 2293.10] for a way
[2293.10 → 2294.44] to collect data
[2294.44 → 2296.04] and you haven't
[2296.04 → 2296.46] found something
[2296.46 → 2297.02] that you like,
[2297.02 → 2297.84] I recommend looking
[2297.84 → 2299.20] into Telegraph
[2299.20 → 2300.52] any which way
[2300.52 → 2302.18] and it's completely
[2302.18 → 2302.60] open source.
[2302.84 → 2303.08] So when you're
[2303.08 → 2304.18] talking about
[2304.18 → 2304.78] collect,
[2304.90 → 2305.86] that could be like,
[2306.46 → 2306.68] oh,
[2306.74 → 2308.24] I have a Raspberry Pi,
[2308.64 → 2309.30] I have a sensor
[2309.30 → 2309.72] or something
[2309.72 → 2310.96] and I want to
[2310.96 → 2312.22] put something
[2312.22 → 2313.04] on that
[2313.04 → 2314.78] to get the sensor
[2314.78 → 2315.48] data back
[2315.48 → 2316.52] to my laptop.
[2316.74 → 2317.18] That's the sort
[2317.18 → 2317.60] of collection
[2317.60 → 2318.36] we're talking about
[2318.36 → 2320.00] or is it different
[2320.00 → 2320.36] than that?
[2320.48 → 2320.68] Yeah,
[2320.76 → 2321.40] you can be
[2321.40 → 2322.36] collecting data
[2322.36 → 2323.18] from a sensor,
[2323.82 → 2324.90] you can collect
[2324.90 → 2326.30] data from
[2326.30 → 2327.20] I mean,
[2327.22 → 2327.78] there's so many
[2327.78 → 2328.36] input plugins.
[2328.48 → 2328.88] You can collect
[2328.88 → 2329.42] data from
[2329.42 → 2330.06] any other
[2330.06 → 2330.92] database,
[2331.62 → 2332.24] you can collect
[2332.24 → 2333.20] data from
[2333.20 → 2335.06] CSV or JSON,
[2335.42 → 2335.94] you can collect
[2335.94 → 2336.82] data from
[2336.82 → 2338.76] Jenkins or
[2338.76 → 2340.36] MQTT or
[2340.36 → 2340.94] I mean,
[2341.08 → 2341.84] like I said,
[2341.88 → 2342.38] there's like over
[2342.38 → 2343.98] 180 input plugins
[2343.98 → 2344.58] so if you can
[2344.58 → 2345.08] think of it,
[2345.14 → 2345.82] there's probably
[2345.82 → 2346.86] a way to collect
[2346.86 → 2347.76] data from that source.
[2348.34 → 2349.02] And if there's not,
[2349.12 → 2350.20] I'm sure that
[2350.20 → 2351.20] you would welcome
[2351.20 → 2351.78] contributions.
[2351.82 → 2351.94] Oh,
[2352.02 → 2352.32] for sure,
[2352.42 → 2352.58] yeah.
[2353.58 → 2353.96] Yeah,
[2354.04 → 2354.80] so on that front,
[2354.92 → 2355.86] what is the
[2355.86 → 2356.68] kind of open
[2356.68 → 2357.42] source community
[2357.42 → 2358.30] like around
[2358.30 → 2359.12] InfluxDB?
[2359.44 → 2360.10] I find this
[2360.10 → 2360.78] interesting because
[2360.78 → 2361.60] I worked on
[2361.60 → 2362.14] like an open
[2362.14 → 2362.84] source data
[2362.84 → 2363.64] platform and
[2363.64 → 2364.90] our users were
[2364.90 → 2365.86] like data
[2365.86 → 2366.74] scientists and
[2366.74 → 2367.64] other people,
[2367.88 → 2369.08] but then like
[2369.08 → 2369.90] the developer
[2369.90 → 2371.08] community were
[2371.08 → 2372.02] primarily like
[2372.02 → 2373.10] backend sort of
[2373.10 → 2374.22] distributed systems
[2374.22 → 2374.62] people.
[2374.88 → 2375.94] Is it the same
[2375.94 → 2377.22] with InfluxDB
[2377.22 → 2378.10] in the sense that
[2378.10 → 2378.72] you've got kind
[2378.72 → 2379.88] of like separate
[2379.88 → 2381.62] developer and
[2381.62 → 2382.60] user communities
[2382.60 → 2383.18] where the users
[2383.18 → 2383.94] are like sort of
[2383.94 → 2384.80] analytics people
[2384.80 → 2385.74] and then developers
[2385.74 → 2387.16] or most of the
[2387.16 → 2388.04] time like database
[2388.04 → 2388.62] and backend
[2388.62 → 2389.46] people or is there
[2389.46 → 2390.12] a lot of overlap
[2390.12 → 2390.48] there?
[2392.60 → 2393.20] There's some
[2393.20 → 2393.80] overlap.
[2394.12 → 2395.16] I think like you
[2395.16 → 2396.06] don't need to be a
[2396.06 → 2397.48] DBA to use Influx.
[2397.62 → 2398.06] Like a lot of
[2398.06 → 2398.32] people,
[2398.48 → 2399.42] because I mostly
[2399.42 → 2400.12] talk to open
[2400.12 → 2400.88] source users,
[2401.14 → 2402.28] so I have a lot
[2402.28 → 2402.86] of people that I
[2402.86 → 2403.36] talk to that are
[2403.36 → 2403.66] just like,
[2403.78 → 2403.86] hey,
[2403.90 → 2404.60] I'm using Influx
[2404.60 → 2405.30] to monitor my
[2405.30 → 2405.96] vegetable garden
[2405.96 → 2407.26] or like my
[2407.26 → 2409.36] barbecue or they
[2409.36 → 2409.98] just have a home
[2409.98 → 2410.70] project, or they're
[2410.70 → 2411.52] trying to like make
[2411.52 → 2412.24] their house a
[2412.24 → 2412.80] smart house.
[2412.80 → 2414.72] And so sometimes
[2414.72 → 2415.10] they're just
[2415.10 → 2416.36] developers that are
[2416.36 → 2417.14] curious about getting
[2417.14 → 2418.42] into data science
[2418.42 → 2419.06] and data analytics
[2419.06 → 2420.28] and so they just
[2420.28 → 2420.96] want to have a fun
[2420.96 → 2421.46] project.
[2422.42 → 2422.98] And so they really,
[2423.12 → 2424.30] they come from all
[2424.30 → 2424.54] over.
[2425.08 → 2425.24] Cool.
[2425.40 → 2425.60] Yeah,
[2425.66 → 2426.14] that's great.
[2426.24 → 2427.58] And I'm sure it
[2427.58 → 2428.44] sounds like I
[2428.44 → 2429.86] personally need to
[2429.86 → 2431.48] try out Influx and
[2431.48 → 2433.32] it sounds easy to get
[2433.32 → 2434.58] spun up and start
[2434.58 → 2434.90] using.
[2435.12 → 2435.94] And this whole
[2435.94 → 2436.98] conversation I've been
[2436.98 → 2437.78] thinking of all the
[2437.78 → 2438.88] time series data that
[2438.88 → 2440.02] I'm probably not
[2440.02 → 2441.44] leveraging in my own
[2441.44 → 2441.66] world.
[2441.74 → 2442.18] I don't know about
[2442.18 → 2442.60] you, Chris.
[2442.90 → 2444.10] No, I'm actually
[2444.10 → 2444.72] while you guys were
[2444.72 → 2445.60] talking in the last
[2445.60 → 2446.42] few minutes, I was
[2446.42 → 2447.30] looking at Influx
[2447.30 → 2448.56] DB on the web page
[2448.56 → 2449.06] and looking at
[2449.06 → 2449.56] Telegraph.
[2449.94 → 2451.14] And when you were
[2451.14 → 2451.92] talking about doing
[2451.92 → 2452.42] things around the
[2452.42 → 2453.96] house and stuff, I
[2453.96 → 2454.56] have a bunch of
[2454.56 → 2455.38] ideas right now.
[2455.72 → 2456.66] My wife has a new
[2456.66 → 2457.66] little garden area
[2457.66 → 2458.54] that we had this
[2458.54 → 2459.30] summer, and I'm
[2459.30 → 2460.10] thinking maybe we
[2460.10 → 2461.08] can monitor data in
[2461.08 → 2461.48] the garden.
[2461.64 → 2462.26] I can actually get
[2462.26 → 2462.92] her wrapped up in
[2462.92 → 2463.08] that.
[2463.18 → 2463.70] So I am very
[2463.70 → 2464.84] thankful for that
[2464.84 → 2465.64] suggestion because I
[2465.64 → 2466.30] think I'm always
[2466.30 → 2467.04] looking for ways to
[2467.04 → 2467.96] make this AI stuff
[2467.96 → 2469.60] practical, not just
[2469.60 → 2470.54] for myself, but for
[2470.54 → 2471.44] my family who are not
[2471.44 → 2472.10] technical at all.
[2472.10 → 2474.72] Yeah, I'm excited to
[2474.72 → 2475.86] hear more about
[2475.86 → 2477.06] Chris's vegetable
[2477.06 → 2479.02] monitoring, and I'm
[2479.02 → 2480.14] really excited that
[2480.14 → 2480.80] you were able to
[2480.80 → 2482.54] join us on Ace and
[2482.54 → 2483.62] share with us a little
[2483.62 → 2485.02] bit about time series
[2485.02 → 2487.38] and about some of the
[2487.38 → 2487.82] things you've been
[2487.82 → 2488.84] working on and your
[2488.84 → 2489.82] perspective on
[2489.82 → 2491.22] statistical methods
[2491.22 → 2491.94] versus machine
[2491.94 → 2492.24] learning.
[2492.38 → 2493.10] All that was really
[2493.10 → 2493.46] useful.
[2493.46 → 2495.36] And I hope we'll for
[2495.36 → 2496.64] sure put links in our
[2496.64 → 2497.54] show notes to
[2497.54 → 2499.88] influx, DB and the
[2499.88 → 2500.68] other things mentioned.
[2500.90 → 2502.00] But thank you so much
[2502.00 → 2503.14] for joining us.
[2503.18 → 2503.56] It was a great
[2503.56 → 2504.12] conversation.
[2506.30 → 2506.80] All right.
[2506.84 → 2507.44] Thank you for tuning
[2507.44 → 2508.86] into this episode of
[2508.86 → 2509.46] Practical AI.
[2509.72 → 2510.30] If you enjoyed the
[2510.30 → 2511.18] show, do us a favour.
[2511.30 → 2512.24] Go on iTunes, give us
[2512.24 → 2512.68] a rating.
[2512.96 → 2514.12] Go in your podcast app
[2514.12 → 2514.82] and favourite it.
[2514.90 → 2515.72] If you are on Twitter
[2515.72 → 2516.90] or social network, share
[2516.90 → 2517.64] a link with a friend.
[2517.72 → 2518.40] Whatever you got to do,
[2518.60 → 2519.24] share the show with a
[2519.24 → 2520.08] friend if you enjoyed it.
[2520.38 → 2521.02] And bandwidth for
[2521.02 → 2522.24] Changelog is provided
[2522.24 → 2523.04] by Vastly.
[2523.18 → 2523.74] Learn more at
[2523.74 → 2524.60] Fastly.com.
[2524.78 → 2525.50] And we catch our
[2525.50 → 2526.38] errors before our users
[2526.38 → 2527.16] do here at Changelog
[2527.16 → 2528.00] because of Rollbar.
[2528.22 → 2529.10] Check them out at
[2529.10 → 2529.92] Rollbar.com slash
[2529.92 → 2530.60] Changelog.
[2530.92 → 2532.14] And we're hosted on
[2532.14 → 2533.42] Linde cloud servers.
[2533.76 → 2534.54] Head to Linode.com
[2534.54 → 2535.38] slash Changelog.
[2535.46 → 2535.92] Check them out.
[2536.00 → 2536.84] Support this show.
[2537.22 → 2538.54] This episode is hosted
[2538.54 → 2539.70] by Daniel Whiten ack
[2539.70 → 2540.42] and Chris Benson.
[2540.88 → 2541.90] The music is by
[2541.90 → 2542.94] Break master Cylinder.
[2543.32 → 2544.14] And you can find more
[2544.14 → 2545.24] shows just like this
[2545.24 → 2546.76] at ChangeLog.com.
[2546.94 → 2547.62] When you go there,
[2547.70 → 2548.40] pop in your email
[2548.40 → 2549.46] address, get our
[2549.46 → 2550.42] weekly email keeping
[2550.42 → 2551.14] you up to date with
[2551.14 → 2551.96] the news and
[2551.96 → 2553.02] podcast for developers
[2553.02 → 2554.62] in your inbox every
[2554.62 → 2555.22] single week.
[2555.62 → 2556.38] Thanks for tuning in.
[2556.54 → 2557.26] We'll see you next week.
