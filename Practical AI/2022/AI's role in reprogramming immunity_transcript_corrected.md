[0.00 → 8.54] One of the things that is really challenging about using AI in this bios pace is there is so much that you could do.
[8.70 → 14.68] Because now there is just so much data that like the space of possible things that we could do is just ginormous.
[15.02 → 18.64] And so you have to think about what is the thing you really care about.
[18.64 → 28.92] And even once you've identified the question or the problem, a highly trained immunologist can't look at a 20,000 dimensional sparse vector and tell you what kind of cell type it is.
[28.92 → 34.56] We can all look at a picture of a cat and a picture of a dog to tell did the algorithm do a good job or a bad job.
[34.90 → 45.32] And so I think in sort of the bio AI combination, you're sort of in the hardest of both of these regimes and that the data is hard to understand because also biology is super messy.
[45.32 → 51.52] And the problem space is so large and unbounded that it's really easy to sort of get lost in the woods.
[58.92 → 69.78] Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive, and accessible to everyone.
[70.14 → 74.46] This is where conversations around AI, machine learning, and data science happen.
[74.46 → 80.20] Join us at practicalai.fm slash community and follow the show on Twitter.
[80.40 → 82.56] We're at practicalai.fm.
[82.56 → 87.44] Thank you to our partners at Vastly for shipping our pods superfast all around the world.
[87.64 → 89.50] Check them out at fastly.com.
[95.86 → 98.86] Welcome to another episode of Practical AI.
[99.22 → 100.76] This is Daniel Whiten ack.
[100.88 → 109.80] I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[110.10 → 110.80] How are you doing, Chris?
[110.80 → 112.02] I'm doing very well.
[112.02 → 114.56] We're now, we've just come across summer solstice.
[114.68 → 115.30] We're into summer.
[115.68 → 118.36] We got hot weather all over the United States.
[119.26 → 122.92] And so I'm just figuring we need some hot AI topics to go with that.
[123.28 → 124.92] Some hot AI topics.
[125.12 → 128.78] If we're burning up 24 hours a day, we got to burn up with some AI too here.
[129.84 → 130.84] Good one.
[130.98 → 131.34] Good one.
[131.62 → 141.54] I don't know many things that are maybe hotter than sort of AI applied within healthcare or within pharma
[141.54 → 143.38] or within genomics.
[143.38 → 152.98] I just saw actually today, I saw a tweet of someone who just released the first open source version of AlphaFold, the protein folding thing.
[153.04 → 154.04] And that's pretty cool.
[154.04 → 167.50] And so, yeah, we're really privileged this week to have someone who's an expert in the field of AI as applied to immunotherapy and genomics.
[167.70 → 172.58] We have with us Dressed Wilson, who is the director of machine learning at Immune.
[172.58 → 173.88] Welcome, Dressed.
[174.30 → 174.68] Thank you.
[174.82 → 175.70] So good to be here.
[175.80 → 176.46] Thanks for having me.
[176.82 → 177.74] Yeah, for sure.
[178.20 → 187.00] Well, maybe before we sort of jump into your specific work and some of the things that you're doing at Immune,
[187.00 → 193.14] maybe it would be good from an expert in the field to just hear a little bit about like,
[193.48 → 206.26] how have you seen AI sort of creeping its way into immunotherapy or maybe applications to like genomics or this sort of field?
[206.70 → 210.12] How have you seen that history progress, and where are we at right now?
[210.42 → 210.64] Yeah.
[210.64 → 213.34] So it's actually sort of crazy to think about it.
[213.64 → 220.64] So it's my first introduction of AI and genomics was about a decade ago when I was in graduate school
[220.64 → 225.58] and I was studying statistical methods for understanding epilepsy.
[225.86 → 227.42] So something very different from immunotherapy.
[227.92 → 231.54] But I saw a bunch of papers starting to explore microarray data.
[232.16 → 239.18] What microarrays are is basically you want to run an experiment on a 96-well plate often.
[239.18 → 242.46] And so you get to profile 96 genes.
[243.00 → 249.96] And all of a sudden we were able to measure 96 genes in a single experiment, in a single little well.
[250.66 → 258.74] And the sort of AI people were going crazy about this because it was this brand-new bio, you know, biggish,
[259.18 → 262.36] now we would call it like small data, but back then it was big data.
[262.92 → 266.06] This is sort of maybe 2010 or so.
[266.06 → 274.94] And people were using this really rich data to start both to test new, you know, statistical algorithms and ML models
[274.94 → 279.06] and also to try to understand, you know, associations between genes,
[279.14 → 285.56] which finally we were able to measure enough genes and proteins that we could actually sort of start to peel these back.
[285.56 → 293.24] And I just always thought it was very – it was always like kind of wish that I could like to get into that area of like getting to microarrays.
[293.44 → 296.68] And – but that is sort of my path took me elsewhere.
[297.22 → 304.18] And then, you know, fast-forward eight or ten years and all of a sudden no one uses microarrays anymore because they're – you know,
[304.18 → 310.48] you only get 96 genes and, you know, meanwhile now we can get, you know, 20,000 – you know, all 20,000 genes in the human genome.
[310.48 → 319.44] And so I think the thing that's – and the sort of high-level story of AI helping understand biology over the last decade
[319.44 → 325.84] is this sort of intertwined story between algorithms getting better and more capable
[325.84 → 330.44] and also our – critically our experimental techniques getting much better.
[330.44 → 336.88] And I mean, actually I would say the experimental techniques, you know, might even be getting better faster than the algorithms
[336.88 → 345.18] because we're just able to profile so many more cells and genes and aspects of biology.
[345.30 → 351.16] And here I'm just talking about one small area of the larger biological understanding landscape
[351.16 → 353.68] and we can talk a little bit more about others.
[353.68 → 363.18] But I think this sort of – this is the exciting piece about our field is this sort of racetrack of both the experimental techniques
[363.18 → 366.92] and also the computational techniques sort of like racing against each other.
[367.10 → 372.18] You know, it's interesting that you say that, and we've heard that from other people in other fields.
[372.38 → 377.20] But, you know, just the acceleration you get from kind of like – this is a whole new tool set.
[377.36 → 380.88] You know, we've been doing this for a while in this.
[380.88 → 387.58] But if you look at the scheme of these fields that it's being applied to, it's getting new tools and figuring out how to use them effectively.
[388.20 → 392.80] I find it interesting because we love talking about how fast the AI field is evolving.
[393.06 → 399.76] And you're actually saying that you're getting a bigger impact just from the fact that you're learning how to best use those tools,
[399.98 → 401.86] which I think is a great lesson for folks.
[401.86 → 406.72] And so in the last decade, let's say just sticking with this area that I know a little bit better,
[406.84 → 417.78] from microarrays to where we are now, we've seen basically three revolutions in sort of profiling of individual cells in biology.
[418.12 → 422.92] We went from microarrays to something called bulk RNA sequencing where you can take, you know,
[422.94 → 427.02] a bunch of cells and understand what they're doing across all the genes in the human genome.
[427.02 → 432.96] And then from bulk, you know, maybe five years ago, we started the single cell revolution.
[433.40 → 439.24] And, you know, there instead of looking at, you know, what's the average of, you know, a thousand cells or 10,000 cells,
[439.36 → 444.90] all of a sudden we can look at what's going on in an individual cell, each individual cell.
[444.90 → 447.66] And that is tremendously exciting.
[447.82 → 455.60] And there's a lot more that I could go into, you know, if we want to go down this route of sort of the single cell profiling opportunities we have.
[455.74 → 468.86] But this is, as I said, just one area of biology that has sort of been revolutionized by just the data capture that we've been able to perform in the last decade.
[468.86 → 473.54] And it's the data that's the thing that's driving it that I'm most excited about.
[473.74 → 476.58] Sort of I think about like, what's the next data, you know, next decade looks like?
[477.06 → 483.56] Yes, the algorithms will sort of be right there along, but the data is going to be sort of leading the pack.
[483.64 → 485.16] And that's the thing that's most exciting.
[485.60 → 493.00] So on that front, I love how you brought up this side of the sort of data centric side of what you're doing.
[493.00 → 502.14] I'm wondering, like you brought up, okay, we can go down to the single cell level, we can get a bunch of data about this single cell.
[502.36 → 512.08] I'm wondering if you could describe like, for us who don't have this sort of experience with biology and such, like, what is measured?
[512.20 → 514.86] Or what does the data look like for a single cell?
[514.96 → 517.22] And like, why is that data important?
[517.36 → 521.50] Why is that connected to anything like we would want to care about?
[521.50 → 528.60] And if I can extend that to one other dimension, what's the difference in the single cell versus the bulk in terms of what you're getting out of it as well?
[528.82 → 533.36] Oh, oh, man, I could tell you, I could spend a whole chat just on this.
[533.56 → 535.82] So you can tell you piqued our interest.
[536.50 → 536.94] Yeah.
[537.10 → 537.44] Okay.
[537.78 → 540.52] Let's first cover just what is the data.
[540.52 → 547.76] And then we'll get to the what's the difference between individual cells versus sort of the, you know, what's sometimes called bulk, which is the average of many, many, many cells.
[548.44 → 549.72] So what is the data?
[549.72 → 554.28] You have to actually recall your high school biology, which is how does a cell work?
[554.80 → 554.94] Right.
[555.00 → 555.20] Okay.
[555.28 → 556.44] So let's let's.
[556.68 → 558.54] I remember the walls and.
[559.28 → 559.68] Exactly.
[559.94 → 560.58] You don't know.
[560.68 → 561.98] It's different ways.
[562.08 → 562.28] Yeah.
[562.74 → 564.28] It's this is why it's wonderful.
[564.28 → 566.10] It's like it actually all of this is relevant.
[566.10 → 572.44] So, you know, you've got DNA and the DNA is like your master set of instructions for a cell.
[572.44 → 575.64] But you don't crack the master set of instructions every time.
[575.64 → 575.92] Right.
[575.96 → 582.80] So normally when a cell needs to do its thing, it just needs a page here, a page there needs to make a bunch of copies from your master set of instructions.
[582.80 → 594.02] OK, so you can think about, you know, there's a process that's making a bunch of individual copies of individual pages and then giving those copies of, OK, you know, here's how to make this protein or here's how to make that protein to some factories.
[594.16 → 595.52] These factories are called ribosomes.
[595.94 → 602.24] And the ribosomes are the things that actually take the copies of instructions for individual proteins and actually like make the proteins.
[602.24 → 608.10] So with that, so just covering that, there are three things you can measure right there.
[608.42 → 609.74] You can measure one.
[610.34 → 620.44] What pages are you copying in the master set of instructions or like what, you know, think about it like, you know, what page is the master book open to so that you're, you know, about to make some copies of.
[621.08 → 628.86] Imagine that you could then say like, OK, what are all the loose, you know, loose pieces of paper floating around that are encoding proteins that we care about?
[628.86 → 635.44] And that's going to tell you something about what a cell is doing, but basically like what instructions are it passing around to its factories?
[635.80 → 642.38] And then you can also observe, OK, you know, what's the what's the product of these ribosome factories, the proteins like what's coming out?
[642.44 → 645.66] How can we measure how many of this kind of protein or that kind of protein?
[646.24 → 651.14] And so you can measure all of these, and they're all complementary.
[651.66 → 657.78] So, you know, you can measure some proteins a little bit better, but you're, you know, not every RNA molecule.
[657.78 → 663.74] So basically those these the middle thing, which are these individual pages that you're sort of copying from your master book.
[664.32 → 670.38] This is what's called messenger RNA and messenger RNA are these little pieces of instruction that tells ribosomes like it.
[670.42 → 671.60] Here's how to make this protein.
[671.72 → 673.62] They code for a specific protein.
[674.10 → 684.58] And so messenger RNA is so you can imagine reaching into a cell and grabbing a bunch of random, you know, like whatever pages are on the floor, so to speak.
[684.58 → 690.60] Right. And like sweeping those up and then like tabulating them and counting them and say, OK, this is a page for this protein.
[690.68 → 699.48] This is a page for this protein. And you and that's one way to profile what a cell is doing is by sort of counting the number of mRNA molecules.
[699.48 → 704.86] And literally with some of these techniques, we are counting individual molecules of mRNA.
[705.40 → 711.28] And that allows us to sort of if we can see like what is the cell, what things are the cell doing?
[711.48 → 714.42] It gives us a sense of what's the function of the cell.
[714.82 → 716.48] Where has it been? Where is it going?
[716.48 → 720.02] But each of these data, sometimes we call them modalities.
[720.40 → 723.24] It has its biases and its problems and its weaknesses.
[723.54 → 731.80] And the idea of a lot of modern genomics profiling is sort of capturing multiple of these modalities.
[732.38 → 739.56] So Amy and I, where I work, we actually have a technique that sort of can capture all three at the same time.
[739.76 → 741.92] And they sort of complement each other well.
[741.92 → 747.24] Can you describe a little bit about what you're since you had started off kind of enumerating the three?
[747.76 → 751.26] And we've kind of as we've kind of gone through, can you tell us what you're getting?
[751.36 → 753.38] Like, why would you do all three at the same time?
[753.46 → 755.12] Why isn't the most recent one the best one?
[755.32 → 757.38] You know, like what are you getting from each one?
[758.06 → 761.14] So each has its tradeoffs and benefits.
[761.22 → 766.24] Right. So let me let's take the simpler example of what's called Raised,
[766.48 → 770.48] which is basically these like individual copies of RNA.
[770.48 → 781.84] So in this, you can actually count up the molecules of RNA and you can see you can basically get an expression profile for every gene in the human genome.
[782.08 → 786.20] 20, usually about 20,000 genes actually are have activity here.
[786.20 → 793.90] And so you have amazing scope in covering the entire human genome in a single readout.
[793.90 → 802.70] But the tradeoff for that is that 90 percent of the sort of counts, you can basically what you get here is, you know, for each.
[802.96 → 807.34] Now I'm talking about, let's say, the single cell you get for each individual cell.
[807.46 → 813.14] You get a count. How many molecules of RNA for a particular gene did I observe?
[813.14 → 826.64] And the problem with Raised, at least single cell Raised, is that 90 percent of the genes have zero counts because you just can't observe all of these molecules of RNA.
[826.64 → 829.92] And so, you know, you got a lot of zeros you got to contend with.
[829.98 → 831.50] It's a very sparse readout.
[831.76 → 833.56] So let's contrast that with proteins.
[833.90 → 840.32] So proteins, which basically can exist both within the cell, but also but especially on the surface of the cell,
[840.64 → 851.44] are what traditionally in sort of the last 50 years, biologists have used these proteins to characterize and identify biology, certain cell types.
[851.44 → 857.92] So in the modern era, we can, I can say choose 100 proteins to profile, maybe 200.
[858.48 → 860.56] And I have I can I sort of choose them carefully.
[860.56 → 865.96] And, you know, often I choose them so they capture all the biology that I would want to measure.
[866.28 → 870.52] And for each of these, I get a pretty high quality readout.
[870.72 → 874.80] You know, the data is high quality, but it doesn't cover all the possible proteins.
[874.84 → 876.24] I have to place my data.
[876.24 → 886.90] And so sometimes what we'll do is we'll say, OK, I want to use the proteins to identify, let's say, cell types or to identify which cells are dead or alive.
[887.06 → 888.42] Or, you know, there are many things you can do.
[888.74 → 894.30] And then I'm going to use the RNA to identify what's going on, like under the hood in the cell.
[894.44 → 899.76] And that may not be I may not be able to as clearly see with all the proteins.
[899.76 → 902.98] But sometimes I can say, OK, I really don't care about all the stuff that's going on under the hood.
[902.98 → 912.22] I just want to know, you know, is the cell really energized to go kill some tumours or is it feeling exhausted, you know, from just coming off the field of killing a bunch of tumours?
[912.42 → 919.98] And, you know, sometimes there are a couple of individual surface proteins that, you know, that we know about that will indicate the sort of state of the cell.
[920.46 → 927.40] So it's sort of like you have this menu of things you can read out from a cell, and you have to be very thoughtful about choosing.
[927.78 → 929.76] OK, what are you going to read out here or there?
[929.76 → 937.30] And there are lots of other very interesting tradeoffs because, you know, each of these modalities has a cost.
[937.62 → 938.94] It has a cost in money.
[939.18 → 940.60] It has a cost in human effort.
[940.72 → 941.92] It has a cost in time.
[942.16 → 955.84] So I could say, OK, would I rather have, you know, a million cells of this sort of single cell Raised data or, you know, 200 proteins of worth of data for each individual cell?
[955.84 → 961.58] Or would I rather have 5 million cells with just 10 proteins?
[962.16 → 962.26] Right.
[962.30 → 970.56] And depending on what I'm trying to do, I may say, but that 5 million cells with 10 proteins, I can get that data tomorrow, right after I did the experiment in the lab.
[970.56 → 982.44] Whereas the stuff where I have all the RNA molecules, or I just have, you know, I have, you know, 200 surface proteins that maybe I have to wait a couple of weeks because it has to go get sequenced and stuff like that.
[982.44 → 993.48] So there's, I think, one of the things that's really hard but also fun and interesting about biology is, and biological data is that there are so many options.
[993.90 → 1007.04] You have to think about tradeoffs a lot more, I think, than if you're just like working with vision or text or some other sort of like a modality that or some other type of data that many of us in the AI world are used to thinking about.
[1007.04 → 1034.26] So we've talked a bit about cells.
[1034.44 → 1035.74] We've talked about genes.
[1035.74 → 1040.48] We've talked about this sort of like measurements within a single cell or bulk.
[1040.48 → 1054.06] I'm wondering if you could kind of connect this to what I'm learning about on your website, which is more sort of related to immune profiling or immunotherapy.
[1054.06 → 1061.98] How do the cells and what we know about the cells connect to kind of immunotherapy?
[1062.32 → 1068.06] And what exactly does immunotherapy mean maybe for like some people that are new to that?
[1068.86 → 1068.96] Great.
[1069.06 → 1069.30] No, no.
[1069.36 → 1070.72] It's a great question.
[1070.84 → 1071.38] I'll be honest.
[1071.38 → 1074.22] Before I started working here, like I had no idea what immunotherapy is.
[1074.22 → 1076.08] I only sort of knew at the very highest level.
[1076.18 → 1079.66] So I can walk you through sort of my own learning process as well.
[1080.74 → 1084.66] So, but first, even before we get to immunotherapy, let's talk about what is the immune system?
[1085.42 → 1085.68] Okay.
[1085.68 → 1091.64] So the immune system is, think of it as like a combination of the security guard force.
[1092.20 → 1096.22] It's the police force, and it's the army, and it's the air force.
[1096.80 → 1098.20] Speaking in terms Chris can understand.
[1098.20 → 1098.44] Yeah.
[1098.46 → 1099.96] I work in the defence industry.
[1100.20 → 1102.00] I'm all on board with this.
[1102.10 → 1102.44] Keep going.
[1102.52 → 1103.06] I'm sorry to interrupt.
[1103.06 → 1108.22] So your immune system is the defence industry for your body, right?
[1108.26 → 1117.96] And it is insanely good at its job because 99.99% of bad things that happen in your body
[1117.96 → 1119.66] are crushed, right?
[1119.76 → 1122.02] The immune system dispatches them no problem.
[1122.56 → 1127.02] And like this is the product of, you know, hundreds of millions of years of evolution and,
[1127.02 → 1133.18] you know, lots of predecessors of ours, like, you know, dying in order to naturally select
[1133.18 → 1136.18] for this beautiful thing that is the immune system.
[1136.40 → 1141.54] It is actually like a defence force where you have different specialized players that are
[1141.54 → 1143.10] good at different things.
[1143.56 → 1149.24] You know, you're not going to send, you know, a SEAL team to monitor your apartment building.
[1149.48 → 1151.04] You have a security guard for that.
[1151.12 → 1156.24] And the security guard is maybe even better than a SEAL team in some cases for various reasons.
[1156.24 → 1161.56] And so the immune system has evolved to have all these perfect different players that
[1161.56 → 1167.96] work together really well to sort of crush viruses and bacteria when they sort of come
[1167.96 → 1174.22] into your body and also to crush things that happen inside your body.
[1174.34 → 1180.20] So the two biggest problems that happen in that the immune system is balancing between
[1180.20 → 1182.90] are cancer and autoimmune issues.
[1182.90 → 1189.78] So cancer is when basically the there's some mutation in your body that is like a runaway
[1189.78 → 1190.18] train.
[1190.30 → 1196.10] All of a sudden some of your own cells start replicating and all the breaks and emergency
[1196.10 → 1199.74] breaks that usually keep this from happening have, you know, have broken.
[1200.08 → 1203.76] And so there's this sort of like out of control growth that's happening.
[1203.76 → 1211.00] Almost all cancer, again, 99.99% of cancers like are dispatched summarily by your immune
[1211.00 → 1211.26] system.
[1211.32 → 1212.94] Your immune system sees what's going on.
[1213.02 → 1214.46] It goes, and it kills those cells.
[1214.80 → 1215.50] You'll never know.
[1216.02 → 1222.86] At the same time in autoimmune issues, what's happening here is the immune system is sort of
[1222.86 → 1224.46] like going overboard, right?
[1224.56 → 1227.84] It thinks there's a problem, but there's actually not a problem.
[1227.84 → 1231.14] So it's just attacking sort of like civilians, like healthy cells.
[1231.98 → 1234.80] And this is, this is also like very like a problematic.
[1234.80 → 1238.46] So I'd say the immune system is this wonderful balance, like a checks and balances.
[1238.82 → 1242.72] And there are lots of cell types that sort of like work and signal to each other to like
[1242.72 → 1244.16] keep each other in control.
[1244.52 → 1244.84] So, okay.
[1244.86 → 1245.82] So what is immunotherapy?
[1246.02 → 1251.04] So immunotherapy is this wonderful sort of like revolution really in oncology treatment
[1251.04 → 1256.26] that's really taken place, blossomed in the last decade, where we basically have realized
[1256.26 → 1262.90] that with just some very minor coaching, we can get the immune system to be way more potent
[1262.90 → 1265.18] at killing some types of cancer.
[1265.60 → 1270.82] And the coaching that I'm talking about is basically just binding, you know, one little
[1270.82 → 1274.94] antibody, one little kind of antibody to a certain type of immune cell.
[1275.24 → 1279.26] And when you do this, all of a sudden the immune cell is, it sort of has like a force
[1279.26 → 1280.76] force field on, right?
[1280.80 → 1286.10] And the cancer cells can't sort of turn it off in the way that, that they've evolved to
[1286.10 → 1286.74] be able to do.
[1287.20 → 1294.52] And so immunotherapy is really the art of coaching the immune system to be better than it already
[1294.52 → 1294.94] is.
[1295.10 → 1301.02] It's not anything, you know, it's sort of using an existing tool just better and sort
[1301.02 → 1304.88] of, you know, giving it the pep talk that it needs to go and fight the cancer.
[1305.82 → 1309.24] So I'm just curious, and I don't know if I'm going to ask this the right way.
[1309.26 → 1313.62] But, you know, by putting in that antibody on that, you know, which is essentially plugging
[1313.62 → 1319.22] it in right there, that's the light switch that the cancer cell would be flipping, you
[1319.22 → 1321.54] know, on or off to have its impact.
[1321.66 → 1323.64] And you're just kind of taking that away.
[1323.70 → 1327.98] You're using your force field, or you're putting the kid's safety cover over the light
[1327.98 → 1328.94] switch, so to speak.
[1329.94 → 1332.40] I like to think about it's like, it's like putting that piece of tape over the light
[1332.40 → 1332.72] switch.
[1332.94 → 1333.68] There you go.
[1333.68 → 1338.20] So in the sort of technical term here in the immunotherapy literature is called immune
[1338.20 → 1339.36] checkpoint blockade.
[1339.94 → 1339.98] Okay.
[1340.04 → 1344.36] And so what you're basically doing is sort of putting that tape over the light switch
[1344.36 → 1348.34] that the tumour has evolved to be able to like to turn off your T cell.
[1348.46 → 1349.86] Your T cells are your main fighters.
[1349.98 → 1352.56] They're like your Marines or your, you know, your SEAL team.
[1352.72 → 1355.34] They're like super elite, and they go in, and they're killers.
[1355.90 → 1361.66] There are a lot of other immune cells that are involved that, but you know, your Marines,
[1361.66 → 1362.78] they need an off switch, right?
[1362.80 → 1365.78] You don't want them running wild, you know, throughout your body.
[1365.92 → 1371.26] So that's why there is this off switch and tumours evolve because in their ability to like,
[1371.50 → 1375.04] you know, sneak by and actually sort of like turn the off switch off when the T cell doesn't
[1375.04 → 1376.02] realize what's going on.
[1376.40 → 1382.76] It's kind of crazy that it really immunotherapy there in the first five years from let's say
[1382.76 → 1384.14] 2010 to 2015.
[1384.14 → 1386.06] They're really just a couple of targets.
[1386.38 → 1388.38] PD1 is one and CTLA4 is another.
[1388.38 → 1394.36] And just between the two of these, like, I can't tell you how many lives have been saved
[1394.36 → 1399.74] because of the cancer treatments that just these single two targets have enabled.
[1400.32 → 1406.02] I'm kind of thinking about like in my mind over you, while you've been talking about like
[1406.02 → 1408.26] what these things are, what the data looks like.
[1408.30 → 1414.16] I've been thinking of in the back of my mind about kind of how I would expect AI to fit into
[1414.16 → 1414.50] this.
[1414.64 → 1419.66] And, you know, back or when I teach like a workshop or something often, like a common
[1419.66 → 1425.12] question is like, when should you apply AI to a problem, and when shouldn't you?
[1425.34 → 1429.20] And I often put that in terms of like scale and complexity.
[1429.60 → 1433.70] So like it's very easy for a human to identify a cat in an image.
[1433.70 → 1439.40] It's very hard for a human to identify a cat in a million images, right?
[1439.48 → 1443.38] Just time wise, even though that's a simple task for a human.
[1443.82 → 1449.78] But there are other things like, you know, maybe it's certain time series forecasting or maybe
[1449.78 → 1456.72] it's like things where the data is very complex, language related things or something like that,
[1456.76 → 1457.70] where it's very hard.
[1457.82 → 1463.18] Like the data, the problem is very complex for a human to even make a single inference.
[1463.18 → 1464.06] Right.
[1464.22 → 1468.30] And so that doesn't even necessarily require scale.
[1468.30 → 1472.64] And here you've kind of talked about like there's this it seems like there's complexity
[1472.64 → 1478.62] around the data on one side in all of these different things that you can measure selectively
[1478.62 → 1480.80] against single cells or bulk cells.
[1481.06 → 1486.82] But then there's like a whole complexity on the other side of like all the different ways
[1486.82 → 1491.46] the immune system works and its different, you know, targets within the immune system.
[1491.46 → 1496.68] And I'm wondering if is that's a good way to represent it or like how you would kind of
[1496.68 → 1503.66] like make the case that like or for the place, I guess, that AI fits within this problem set.
[1504.34 → 1512.90] So one of the things that is really challenging about using AI in this bios pace is there is so much
[1512.90 → 1519.04] that you could do because now there is just so much data that like the space of possible things
[1519.04 → 1520.90] that we could do is just ginormous.
[1521.62 → 1525.40] And so you have to think about what is the thing you really care about?
[1525.48 → 1529.14] What is what is the question or the problem that really matters to you?
[1529.18 → 1530.42] And like go solve that.
[1530.42 → 1535.96] And even once you've identified the question or the problem, as you said, Daniel, like an immune,
[1536.08 → 1542.58] a highly trained immunologist can't look at a 20,000 dimensional sparse vector and tell you what
[1542.58 → 1543.70] kind of cell type it is.
[1543.80 → 1544.86] You know, they can look at it.
[1544.90 → 1549.22] You know, we can all look at a picture of a cat and a picture of a dog to tell or a face,
[1549.34 → 1553.52] you know, bounding box and see what, you know, did the algorithm do a good job or a bad job?
[1553.52 → 1560.78] And so I think in sort of the bio AI combination, you have you're sort of in the hardest of both of
[1560.78 → 1566.00] these regimes and that the data is hard to understand and hard to sort of know what the
[1566.00 → 1572.18] ground truth is sometimes because also biology is super messy and the problem space is so large
[1572.18 → 1576.10] and unbounded that it's really easy to sort of get lost in the woods.
[1576.76 → 1576.86] Yeah.
[1576.86 → 1583.10] And I know in the in your website and some of the things I've read about some of the things
[1583.10 → 1587.96] you're involved with, some of that involves like this sort of like transfer learning.
[1587.96 → 1594.14] I know like some parallels were drawn between like large language models, things going on
[1594.14 → 1595.94] in the NLP space.
[1596.14 → 1601.54] How do you sort of like chisel down to like you said, there are so many things you could do.
[1601.98 → 1604.96] Immune is specifically interested in immunotherapy.
[1604.96 → 1609.94] How do you go about like saying, OK, here's like the space of what we're interested in.
[1610.04 → 1611.54] Here's this really complex data.
[1612.12 → 1617.60] Here are a bunch of things that are going on in the AI industry more broadly to other types of problems.
[1617.86 → 1624.76] How did you kind of come into the place where you understood how to connect certain of these things,
[1624.76 → 1629.54] whether it's transformers or whatever, to the specific problems that you're thinking about?
[1629.58 → 1632.62] And maybe you give us an example of one of those problems.
[1633.18 → 1633.44] Absolutely.
[1633.44 → 1639.78] So actually sort of this was one of the founding insights that Lewis and Noam, our co-founders,
[1640.20 → 1648.86] identified is that there's a lot of data being generated and a lot of problems being posed in the sort of immune system space.
[1649.10 → 1656.18] But none of those data sets and none of those problems are benefiting from other people posing really similar problems,
[1656.34 → 1658.26] using really similar data sets.
[1658.38 → 1658.42] Right.
[1658.42 → 1662.00] Each person is sort of doing in their own narrow little lane.
[1662.70 → 1668.96] And I think one of the things that especially with transformers and this idea of a foundation model,
[1669.04 → 1674.58] but it is sort of in the earlier part of even back in 2010, 2013,
[1674.58 → 1684.56] people were talking about semi-supervised learning where you train an unsupervised model, and then you fine tune it for specific tasks.
[1684.56 → 1693.94] And so what our founders realized is that basically there is this opportunity to do this transfer across tasks.
[1694.64 → 1705.98] And there are lots of ways that and actually like this is essential in our world because there are because of the multiplicity of data,
[1705.98 → 1709.94] different modalities and readouts and different experimental conditions and contexts.
[1710.16 → 1710.26] Right.
[1710.30 → 1710.46] So,
[1710.96 → 1711.26] again,
[1711.38 → 1712.42] in vision and text,
[1712.64 → 1713.26] I like to,
[1713.44 → 1713.58] I mean,
[1713.62 → 1717.16] I'm sure the people who do vision and text would laugh at me,
[1717.20 → 1717.44] but like,
[1717.82 → 1719.20] I like to say that they have it easy.
[1719.56 → 1719.80] Right.
[1719.86 → 1720.44] Cause you know,
[1720.48 → 1720.76] like,
[1720.86 → 1721.12] you know,
[1721.14 → 1722.24] all the images are,
[1722.30 → 1722.44] you know,
[1722.44 → 1722.88] you got,
[1723.10 → 1723.56] you know,
[1723.56 → 1725.86] they're all RGB, and maybe they have some different,
[1725.86 → 1726.84] you know,
[1726.88 → 1728.46] focus or out of focus or,
[1728.58 → 1728.68] you know,
[1728.68 → 1729.38] different sizes,
[1729.38 → 1730.52] but basically it's all the same.
[1730.52 → 1731.28] And text,
[1731.44 → 1732.32] you've got maybe some,
[1732.36 → 1733.40] some language differences,
[1733.40 → 1740.22] but fundamentally you can go and scrape all of Wikipedia and all of Reddit and get a pretty good data set from those two sources.
[1740.48 → 1743.36] And this is actually like what enabled a lot of the
[1743.36 → 1747.58] the revelled AI revolution of the last decade is just pulling data from the web.
[1747.84 → 1749.38] Whereas in bio,
[1749.62 → 1754.10] instead of having a couple of really high volume sources of data,
[1754.30 → 1755.46] you've got many,
[1755.64 → 1755.84] you know,
[1755.84 → 1759.06] tens or maybe even hundreds of smaller pieces of data.
[1759.06 → 1764.04] And so if you want to benefit from all of those smaller blocks of data,
[1764.32 → 1766.40] you have to have models that can,
[1766.50 → 1768.06] that are more like Legos,
[1768.12 → 1768.24] right.
[1768.24 → 1770.40] That you can sort of like to learn an embedding from,
[1770.76 → 1770.86] you know,
[1770.88 → 1775.50] this data set over here and bring it to some new model that can benefit from,
[1775.58 → 1777.02] let's say that embedding or that,
[1777.22 → 1778.12] that inference that,
[1778.20 → 1778.78] that you learned.
[1778.84 → 1779.26] And like,
[1779.32 → 1779.94] we have not,
[1780.28 → 1780.42] you know,
[1780.48 → 1781.44] at Emmy and I think we're,
[1781.56 → 1785.52] we're doing a lot of work on this, and we're probably at the front of the pack,
[1785.54 → 1786.02] I would say,
[1786.08 → 1788.52] but we have not figured it out and no one else has.
[1788.52 → 1788.76] But,
[1788.76 → 1791.86] but I think this is the thing that's exciting over the next decade is like,
[1791.98 → 1793.36] we will think as a
[1793.36 → 1794.00] as a community,
[1794.00 → 1795.72] we will figure out how to do this.
[1795.72 → 1795.90] And,
[1796.00 → 1798.42] and it's really helpful to,
[1798.58 → 1799.36] you know,
[1799.36 → 1801.10] to be an AI person in the bio space,
[1801.10 → 1805.04] to be able to point to the successes that let's say in natural language
[1805.04 → 1805.56] understanding,
[1805.56 → 1808.76] we've been able to have using this transfer learning approach,
[1808.76 → 1809.12] because,
[1809.34 → 1809.92] you know,
[1809.92 → 1812.34] before transformers or,
[1812.54 → 1812.64] you know,
[1812.72 → 1813.34] GPT,
[1813.48 → 1813.70] you know,
[1813.74 → 1813.88] one,
[1813.94 → 1814.02] two,
[1814.10 → 1814.38] three,
[1814.84 → 1817.28] you had 25 years of link,
[1817.38 → 1817.52] you know,
[1817.58 → 1823.56] computational linguistics people like building really finely crafted models and context-free
[1823.56 → 1824.64] grammars and things like this.
[1824.68 → 1827.38] And it actually took a certain amount of data,
[1827.54 → 1831.66] a certain scale of data and a certain class of algorithm to,
[1831.76 → 1834.52] to sort of trample all of that work.
[1834.52 → 1834.68] And,
[1834.80 → 1836.22] and I think we're sort of all,
[1836.32 → 1836.52] you know,
[1836.54 → 1839.06] just about there in the bio world,
[1839.06 → 1840.14] but there's still a lot of,
[1840.14 → 1843.76] a lot of earlier things that I think are,
[1843.78 → 1844.62] are around,
[1844.62 → 1845.98] but an example,
[1846.20 → 1850.52] let me give you like a really specific example of a transfer learning task.
[1850.96 → 1851.70] So Adam,
[1851.76 → 1851.94] you know,
[1851.94 → 1852.64] we're a single,
[1852.82 → 1852.98] you know,
[1852.98 → 1854.56] primarily a single cell company,
[1854.56 → 1856.10] which means that we take,
[1856.20 → 1856.64] let's say,
[1856.98 → 1857.16] you know,
[1857.20 → 1859.16] a tumour of yours or a vial of blood,
[1859.30 → 1860.22] we process it.
[1860.26 → 1863.00] And then we're profiling each individual cell that we're,
[1863.08 → 1863.46] that we're,
[1863.56 → 1864.06] that we're getting.
[1864.30 → 1864.50] Okay.
[1864.90 → 1866.16] And when I do this,
[1866.20 → 1866.98] I want to know,
[1867.10 → 1867.50] you know,
[1867.60 → 1867.72] are,
[1867.86 → 1868.60] is this cell,
[1868.72 → 1868.94] you know,
[1869.02 → 1870.66] a seal team six cells,
[1870.76 → 1871.74] or is this a
[1871.74 → 1871.94] you know,
[1871.98 → 1873.44] apartment security guard cell,
[1873.76 → 1873.98] right?
[1874.02 → 1874.28] Cause it,
[1874.28 → 1876.10] it depends on how I think about,
[1876.24 → 1876.44] you know,
[1876.44 → 1878.04] what is the cell doing or not doing?
[1878.04 → 1878.98] And is this good or bad?
[1879.68 → 1880.42] So this is,
[1880.42 → 1880.74] you know,
[1880.86 → 1885.54] something called like a cell type annotation and usually involves an expert immunologist who
[1885.54 → 1886.88] understands what the
[1887.00 → 1889.90] all the immune cell types profiles we should see are,
[1890.08 → 1892.96] but ultimately it can be boiled into a classification problem.
[1893.24 → 1893.64] But,
[1893.64 → 1896.10] so we can do this classification problem for,
[1896.10 → 1897.84] let's say cells that we would,
[1897.96 → 1899.30] immune cells we would see in the blood.
[1899.62 → 1902.80] But what about immune cells we would see in the bone marrow or a tumour?
[1903.08 → 1903.62] Those are,
[1903.72 → 1903.84] you know,
[1903.84 → 1904.44] they're related,
[1904.54 → 1905.68] but they're not exactly the same,
[1905.76 → 1906.50] different profiles.
[1906.50 → 1908.96] And so is this a separate problem?
[1908.96 → 1912.62] Or is this just a sort of very similar flavour of,
[1912.70 → 1913.14] of the
[1913.14 → 1913.48] the
[1913.48 → 1915.52] the blood profiling problem?
[1915.92 → 1917.50] And so there's this problem.
[1917.50 → 1919.84] So traditionally people think of it as a completely separate problem,
[1919.96 → 1922.68] completely separate tools and approaches and atlases.
[1922.68 → 1924.44] But I think the reality is,
[1924.56 → 1927.54] it's just another instantiation of a similar problem.
[1927.88 → 1928.60] And then there,
[1928.66 → 1931.76] there are a bunch of other technical problems of like,
[1932.06 → 1935.40] how do I know whether this cell that I'm observing is one cell or two cells?
[1935.42 → 1937.68] Because sometimes the technical hardware,
[1938.56 → 1939.14] you can actually,
[1939.34 → 1942.40] there can be two cells that sort of get smoothed together, and you can't,
[1942.40 → 1943.14] you can't resolve them.
[1943.14 → 1944.22] So this is actually an interesting,
[1944.44 → 1945.34] like technical,
[1945.72 → 1946.58] very in the weeds,
[1946.64 → 1948.90] technical problem that you have to solve what you're going to do with a
[1948.90 → 1949.72] single cell work.
[1949.90 → 1953.24] And this is also like a simple binary classification problem.
[1953.92 → 1954.18] And so,
[1954.32 → 1956.64] and so like when you think about all these individual,
[1957.02 → 1957.34] and I hear,
[1957.42 → 1958.76] I'm talking about just single cell problems,
[1958.82 → 1961.14] but there are analogs for bulk and,
[1961.14 → 1961.46] you know,
[1961.46 → 1962.08] sample level.
[1962.28 → 1966.70] And there are lots of very related problems that up until,
[1966.90 → 1968.28] let's say the last year or two,
[1968.72 → 1970.62] people have been solving independently and,
[1970.82 → 1973.06] and now we're working to solve them together.
[1973.14 → 1975.14] So
[1975.14 → 1998.18] I'm pretty intrigued by this,
[1998.18 → 2003.12] this whole idea of sort of generalist approach to applying,
[2003.14 → 2008.00] this kind of pre-training and transfer in like multiple domains with
[2008.00 → 2009.98] multiple modalities of data.
[2010.14 → 2013.78] Something I'm personally really fascinated by right now.
[2013.88 → 2016.76] I'm wondering if you could describe this sort of like,
[2017.14 → 2017.76] like how,
[2017.76 → 2022.52] how you might approach pre-training and self-supervision for,
[2022.72 → 2025.16] for like biological systems.
[2025.16 → 2027.16] Because I could think like in,
[2027.16 → 2030.02] in the natural language processing space,
[2030.02 → 2030.62] for example,
[2030.62 → 2031.64] I have like,
[2031.88 → 2034.08] like I know I have this text,
[2034.08 → 2037.30] I know this word goes here, and I can just remove it.
[2037.30 → 2038.38] And then I have a blank,
[2038.52 → 2038.70] right?
[2039.20 → 2041.16] Is that some of the inspiration for,
[2041.96 → 2043.96] for what you're doing in terms of pre-training?
[2043.96 → 2051.96] Or how do you think maybe about self-supervision, and what might be like the more relevant things to think about in the biological side?
[2052.50 → 2053.36] So in many ways,
[2053.48 → 2054.78] the like the
[2054.78 → 2055.58] the single cell,
[2055.66 → 2055.88] and again,
[2055.94 → 2056.46] I'm sort of,
[2056.58 → 2058.26] we're going deep on the single cell world.
[2058.26 → 2060.12] Cause especially it's like what I know the best.
[2060.12 → 2060.70] And it's what I mean,
[2060.74 → 2063.76] I focus on in the single cell world,
[2063.80 → 2064.14] the sort of,
[2064.18 → 2065.90] you look at the trajectory of,
[2065.96 → 2067.12] of models and techniques,
[2067.12 → 2068.54] let's say over the last five years,
[2068.54 → 2070.78] like the field is like literally didn't exist five years ago,
[2070.78 → 2072.78] or like it barely existed five years ago,
[2073.02 → 2073.48] five years ago,
[2073.48 → 2075.00] people published papers on 200 cells.
[2075.10 → 2076.08] Now we're publishing on 2 million.
[2076.62 → 2082.82] So just like the scale of the data in the last five years has enabled a certain new flavours of models that just didn't exist.
[2083.16 → 2083.98] We couldn't do before,
[2083.98 → 2086.48] but early on in the first couple of,
[2086.52 → 2086.66] you know,
[2086.66 → 2087.32] two or three years,
[2087.36 → 2092.68] people trained autoencoders parallelling sort of like the earlier work in both in vision and in text.
[2093.20 → 2094.42] And so initially it's just,
[2094.54 → 2094.88] you know,
[2095.02 → 2095.30] you know,
[2095.30 → 2096.52] train your autoencoders.
[2096.64 → 2098.72] Basically each cell is an observation, and you're,
[2099.14 → 2099.68] you have,
[2099.82 → 2100.32] you know,
[2100.36 → 2103.32] maybe you select the 500 genes or 5 million,
[2103.50 → 2105.92] 5,000 genes that are the most,
[2105.92 → 2108.00] most variable or the most active for a cell,
[2108.02 → 2109.38] or maybe you do all 20,000,
[2109.88 → 2111.18] depending on how much data you have.
[2111.18 → 2115.36] And you run that through a bottleneck and where you're just trying to reconstruct the gene expression.
[2115.68 → 2116.80] And then you take that,
[2116.90 → 2118.94] that middle bottle bottleneck layer and you,
[2119.04 → 2119.98] you do something with it.
[2120.00 → 2120.36] Maybe you,
[2120.36 → 2122.02] you fine tune it for a specific task.
[2122.24 → 2124.46] Often people use it for data exploration,
[2124.46 → 2125.26] like,
[2125.36 → 2125.62] you know,
[2125.66 → 2129.60] an unsupervised way that maybe like visualization or clustering and things like this.
[2129.90 → 2131.88] So this is sort of where it started.
[2132.48 → 2133.52] It's just now,
[2133.92 → 2134.06] you know,
[2134.10 → 2136.58] the last year starting to happen where people are like,
[2136.70 → 2136.94] huh,
[2137.46 → 2138.58] now we have enough data.
[2138.70 → 2139.60] Maybe we can like,
[2139.68 → 2142.76] and there's like fancy transformer thing that I've been hearing so much about.
[2142.86 → 2143.04] Like,
[2143.30 → 2145.08] maybe we can start building some of those.
[2145.20 → 2146.04] And in that,
[2146.12 → 2146.66] the task,
[2146.76 → 2146.96] you know,
[2146.96 → 2147.92] can vary a lot,
[2147.92 → 2151.70] but probably one of the most sort of analogous to the
[2151.80 → 2154.04] to the language world is just masking,
[2154.22 → 2154.34] right?
[2154.34 → 2158.70] So instead of masking words as we often do in the
[2158.70 → 2160.94] in the language or parts of sentences,
[2160.94 → 2163.32] or like the second sentence after the first sentence,
[2163.32 → 2165.42] you're masking individual genes.
[2165.42 → 2166.12] And you say,
[2166.18 → 2166.56] Hey model,
[2166.66 → 2171.66] like I've masked this 15% or 25% or 50% of the genes.
[2171.74 → 2173.64] And I'm going to give you the other genes.
[2173.64 → 2174.70] And I want you to tell me,
[2174.80 → 2175.54] I want you to reconstruct.
[2176.28 → 2177.58] So that's probably the
[2177.58 → 2179.26] the simplest formulation,
[2179.26 → 2182.44] but there are a lot of alternatives that you can do.
[2182.44 → 2184.02] And the cool thing now is that,
[2184.02 → 2184.58] you know,
[2184.58 → 2185.48] two years ago,
[2185.48 → 2187.28] if you wanted to build some,
[2187.28 → 2187.54] you know,
[2187.60 → 2189.62] big transformer or big foundation model,
[2189.64 → 2190.40] you sort of had BERT,
[2190.70 → 2191.04] right.
[2191.14 → 2192.58] And as your,
[2192.58 → 2193.06] as your,
[2193.36 → 2194.14] as your template,
[2194.14 → 2194.74] but now,
[2194.90 → 2195.64] you know,
[2195.66 → 2195.86] the
[2196.02 → 2198.16] even just the transformer world is completely blown up.
[2198.18 → 2204.90] And so we have BERT and GPT-3 and the perceived and like lots of options to sort of choose from and customize,
[2205.44 → 2206.44] which is just,
[2207.02 → 2207.30] you know,
[2207.30 → 2207.88] we're not,
[2208.30 → 2208.72] at Immune,
[2208.82 → 2209.30] we're not,
[2209.30 → 2210.28] you know,
[2210.38 → 2212.28] leading the edge on the
[2212.28 → 2213.40] the brand-new transformer,
[2213.40 → 2214.70] our architecture,
[2214.70 → 2218.52] we're benefiting from other people doing this like open AI and,
[2218.52 → 2219.30] you know,
[2219.34 → 2221.18] Facebook and Google and DeepMind.
[2221.38 → 2223.16] And we sort of get to be like,
[2223.20 → 2223.38] okay,
[2223.46 → 2223.62] yes,
[2223.62 → 2224.58] this is the one I think that,
[2224.66 → 2226.44] that most benefits our application.
[2227.52 → 2230.98] So I'm curious because you kind of downplayed it a little bit at the end,
[2231.04 → 2233.44] but these are pretty fascinating approaches,
[2233.44 → 2236.66] maybe because we're talking about it outside,
[2236.66 → 2242.24] of some of the more common topics that you tend to have in the ML space in this way.
[2242.24 → 2242.94] And so,
[2243.40 → 2243.80] you know,
[2243.90 → 2245.22] but at the end of the day,
[2245.22 → 2247.68] you're still having to run a pipeline and,
[2247.78 → 2247.84] you know,
[2247.84 → 2252.18] there's all these kinds of practical ML tasks that you're going to be engaging in.
[2252.30 → 2256.66] But with this interesting dynamic about the thing that you're addressing specifically,
[2256.66 → 2258.66] both similarities and differences.
[2258.66 → 2265.18] So what have you learned about running a practical machine learning pipeline in the
[2265.36 → 2267.20] in a company that's doing these kinds of,
[2267.20 → 2268.58] of interesting techniques?
[2269.00 → 2273.50] It's definitely a realm that most people are not thinking about machine learning in.
[2273.64 → 2276.36] And that has some of the uniqueness of that.
[2276.84 → 2279.30] I'm wondering if that's given you some insights that,
[2279.30 → 2280.96] that might benefit all of us.
[2281.26 → 2281.28] Well,
[2281.32 → 2282.12] I can say that.
[2282.76 → 2284.28] So in my own personal journey,
[2284.32 → 2287.62] I had a period of time when I did a lot of ML, and then I got burned out of ML.
[2287.62 → 2289.72] And then I did no ML for like four years,
[2289.84 → 2291.76] just software and data engineering,
[2291.90 → 2293.76] building pipelines and getting data.
[2293.90 → 2294.04] You know,
[2294.06 → 2295.64] I was a data plumber and I loved it.
[2295.98 → 2298.76] And then I sort of missed the research and the ML stuff.
[2298.82 → 2300.94] And so I got back into it and here I am.
[2301.26 → 2307.46] But I think that the biggest thing that I've learned is that when you have a problem that you want to solve,
[2307.68 → 2310.00] you always solve it without ML first,
[2310.38 → 2310.58] right?
[2310.64 → 2315.02] So you solve it with getting data, and you solve it by analyzing the data.
[2315.02 → 2316.44] And then once you do this,
[2316.64 → 2318.58] then you solve it with something really simple,
[2318.70 → 2320.82] like a logistic regression or an XGBoost.
[2321.08 → 2322.18] Like for classification tasks,
[2322.76 → 2327.66] these two things probably cover 80% of all the things you would want to do reasonably.
[2328.22 → 2330.36] I think like it's really hard,
[2330.68 → 2332.90] even where at our current place to,
[2332.98 → 2335.38] to sort of do the responsible thing sometimes.
[2335.38 → 2335.80] Cause you know,
[2335.86 → 2337.96] you want to go train the fancy transformer,
[2338.20 → 2339.24] like play with lots of data.
[2339.24 → 2339.44] But,
[2339.56 → 2343.10] but the problem is you can just burn so much time,
[2343.20 → 2343.34] you know,
[2343.36 → 2345.22] unless you're one of these huge companies,
[2345.22 → 2349.04] it's so easy to burn so much time getting infrastructure,
[2349.20 → 2349.94] training infrastructure,
[2350.10 → 2350.50] GPU,
[2350.80 → 2350.94] you know,
[2350.98 → 2352.02] parallel GPU training,
[2352.02 → 2355.28] like up and running to support these big models.
[2355.46 → 2356.64] When often,
[2356.92 → 2357.16] you know,
[2357.22 → 2358.68] maybe you're solving the wrong problem.
[2358.68 → 2362.68] So solving the problem without models first,
[2362.68 → 2364.50] or just with data analysis.
[2365.04 → 2365.40] I actually,
[2365.50 → 2367.60] like when I joined Immune about two years ago,
[2368.06 → 2368.84] my boss,
[2368.90 → 2369.74] who's the CTO,
[2370.24 → 2370.54] they said,
[2370.64 → 2370.82] okay,
[2371.00 → 2371.46] Dross in,
[2371.54 → 2374.68] like I need you to just understand cell type annotation.
[2375.12 → 2377.02] And so I didn't train a single model for six months.
[2377.18 → 2383.36] I just like deeply understood the data and analyze it and like understood the problem domain.
[2383.36 → 2383.94] And like,
[2384.00 → 2386.62] it's actually really fun because I got to work with our immunologists.
[2386.62 → 2386.90] And,
[2387.00 → 2388.52] and this was,
[2388.60 → 2389.44] I just sort of didn't,
[2389.52 → 2393.04] I was sort of like grumpy about not getting to like to get in and train models right away.
[2393.14 → 2394.36] But in retrospect,
[2394.36 → 2399.98] it was a really fortuitous thing because now I just have a much richer understanding of the problem.
[2399.98 → 2400.40] And I think,
[2400.56 → 2401.50] especially in bio,
[2401.90 → 2407.46] the problems are hard to define and defining the problem well is the most important thing.
[2407.60 → 2408.84] And this comes with,
[2408.96 → 2411.50] with data and analysis before you have to do any,
[2411.50 → 2412.06] any ML.
[2412.64 → 2414.32] And along with that,
[2414.32 → 2426.72] what is this sort of interaction between maybe those with expertise in machine learning or in even software engineering and like expert biology doctors,
[2426.72 → 2429.44] like this sort of like other side of things,
[2429.44 → 2437.16] like how have you found kind of good synergy between kind of the domain experts and like technical experts?
[2437.16 → 2438.16] It's challenging.
[2438.16 → 2438.40] It's challenging.
[2438.72 → 2440.72] Even when everyone wants it to work.
[2441.04 → 2447.36] This is another big difference in the bio AI world is you just need a lot more different flavours of expert in order to get,
[2447.62 → 2448.22] make a therapy,
[2448.66 → 2450.06] to make something that's going to help people.
[2450.06 → 2460.36] And so getting the immunologists and the software engineers and the data engineers and the computational biologists and the machine learning people to all communicate effectively is,
[2460.36 → 2461.82] is hard.
[2462.42 → 2466.34] And the only thing that works is there are two critical things.
[2466.44 → 2466.80] One,
[2467.20 → 2470.12] you have to find people who are interested in doing this,
[2470.22 → 2470.30] right?
[2470.30 → 2472.68] Find people who like getting out of their discipline areas.
[2472.68 → 2476.48] And not everyone is interested in doing this and that's completely fine.
[2476.98 → 2477.86] But I think for in the
[2477.90 → 2478.74] in the bio world,
[2478.88 → 2480.44] you have to be interested in like,
[2480.90 → 2481.18] you know,
[2481.20 → 2483.04] what the immunologists are doing and like be,
[2483.14 → 2487.66] be excited by those problems rather than just like wanting to make your ETL code,
[2487.76 → 2487.94] you know,
[2487.94 → 2489.18] even better and more efficient.
[2489.42 → 2489.72] So,
[2489.80 → 2493.76] so like finding the right people and the right team is,
[2493.90 → 2494.62] is critical.
[2494.98 → 2498.24] And also building the team such that like,
[2498.32 → 2499.18] I like to think about it,
[2499.18 → 2499.36] my,
[2499.36 → 2503.22] my sort of quantitative brain thinks about it like an overlapping Gaussian
[2503.22 → 2503.84] distributions,
[2503.84 → 2504.62] right?
[2504.68 → 2504.86] So,
[2504.86 → 2507.82] so like each person or really think of it like a team,
[2507.92 → 2509.22] each specialty has,
[2509.40 → 2509.98] you know,
[2510.04 → 2511.36] an area of,
[2511.44 → 2511.60] you know,
[2511.62 → 2511.96] a dense,
[2512.04 → 2514.30] a higher density area of specialization.
[2514.76 → 2515.76] But if those,
[2515.90 → 2516.80] those areas,
[2516.96 → 2518.52] if those densities don't overlap,
[2518.52 → 2519.94] then you've got cracks,
[2519.94 → 2521.34] you've got holes where things get,
[2521.38 → 2522.42] get lost,
[2522.84 → 2522.98] right?
[2522.98 → 2527.12] So what you need is basically to like to get foreign teams where the
[2527.12 → 2528.68] the sort of tails of your distribution,
[2529.18 → 2529.92] I said a Gaussian,
[2530.04 → 2531.14] but maybe it's a T distribution,
[2531.24 → 2532.20] which have heavier tails,
[2532.20 → 2533.86] like where they're overlapping.
[2533.86 → 2536.88] And so it's easier to speak each other's language a little bit.
[2537.12 → 2538.76] And this is essential.
[2539.00 → 2539.72] And it's like,
[2539.82 → 2540.12] again,
[2540.18 → 2543.68] one of the challenges of work doing AI in the bio space,
[2543.68 → 2545.94] but it's also one of the best parts about it,
[2545.94 → 2549.88] because you get to work with all of these brilliant people who are working
[2549.88 → 2551.06] together towards a shared mission.
[2551.06 → 2553.06] It's not just a bunch of engineers.
[2553.72 → 2554.50] Now I love engineers.
[2554.60 → 2555.30] I am an engineer,
[2555.40 → 2555.74] but like,
[2555.86 → 2557.94] I wanted to work with other people who are not engineers.
[2557.94 → 2558.78] And so like,
[2558.90 → 2559.20] that's,
[2559.32 → 2560.34] that's been,
[2560.62 → 2562.26] it's been a learning experience for sure.
[2562.40 → 2562.56] But,
[2562.68 → 2563.80] but it's like,
[2563.88 → 2567.12] it's actually like one of my favourite things about the company where I work
[2567.12 → 2567.52] in and I,
[2567.82 → 2569.28] and also sort of like the field in general,
[2569.30 → 2570.30] it attracts these,
[2570.68 → 2572.00] these are hybrid people.
[2572.00 → 2573.32] We like to sort of be in the
[2573.32 → 2574.66] in the marshlands or in the
[2574.66 → 2577.08] in the hinter regions of these different specialties.
[2577.56 → 2577.68] You know,
[2577.68 → 2581.28] that was a perfect segue because we're kind of coming close to the end.
[2581.28 → 2586.16] And I w I want to ask you kind of where this is going,
[2586.16 → 2586.74] you know,
[2586.84 → 2587.02] in,
[2587.02 → 2587.36] in,
[2587.70 → 2590.50] in the sense of not only your organization,
[2590.50 → 2590.92] but,
[2591.06 → 2592.22] but the field at large,
[2592.22 → 2592.44] you know,
[2592.44 → 2597.02] you've said that you are working at least currently on single cell and,
[2597.50 → 2600.98] but there's the work that you guys are doing and there's the larger field.
[2601.10 → 2602.96] And it's a fascinating topic.
[2602.96 → 2604.40] That's very different from,
[2604.52 → 2604.66] you know,
[2604.66 → 2607.82] most of the folks that we talked to in terms of how you're applying it.
[2607.82 → 2610.78] And you're kind of having to pioneer and not only the techniques,
[2610.78 → 2611.34] but the
[2611.58 → 2614.72] the identification of the problem sets to begin with.
[2615.02 → 2616.36] And so like,
[2616.36 → 2616.74] where,
[2617.12 → 2622.80] where do you see both your organization and the larger field going over the
[2622.80 → 2623.58] next few years?
[2623.72 → 2625.00] What's possible here?
[2625.44 → 2627.62] So we're already seeing it.
[2627.74 → 2628.30] And what's,
[2628.42 → 2628.62] what's,
[2628.76 → 2633.08] what's going to be happening is think of it like assembly lines,
[2633.34 → 2633.68] you know,
[2633.68 → 2637.54] from patients and cells and animal,
[2637.54 → 2639.86] mice to therapies in people.
[2639.86 → 2640.06] Right.
[2640.10 → 2641.16] So the thing of these are like,
[2641.20 → 2643.90] this is the beginning and the end of the like AI,
[2644.60 → 2645.72] like drug discovery,
[2645.96 → 2646.44] therapeutic,
[2646.64 → 2648.62] like biotech assembly line.
[2648.86 → 2653.86] And what's happening is little pieces of this assembly line are being
[2653.86 → 2655.00] productized.
[2655.14 → 2657.00] And because we're getting enough data,
[2657.14 → 2658.98] we understand the problem well enough.
[2659.34 → 2660.56] They're not being solved yet.
[2660.68 → 2660.94] Right.
[2661.02 → 2661.28] So,
[2661.36 → 2662.10] and we're far from,
[2662.36 → 2662.98] you know,
[2663.04 → 2663.74] commoditization,
[2664.10 → 2665.50] but they're being,
[2666.00 → 2667.30] they're sort of like coalescing,
[2667.30 → 2667.72] right.
[2667.82 → 2671.26] And so you're starting to see some companies saying,
[2671.44 → 2671.54] Oh,
[2671.56 → 2674.20] we have the first fully AI generated therapy.
[2674.32 → 2675.96] And I will tell you,
[2676.02 → 2676.80] and I can tell you this,
[2676.90 → 2678.28] I feel okay saying this as an insider.
[2678.52 → 2682.12] There's a lot of like AI marketing that happens in the biotech space.
[2682.58 → 2683.86] And just about every industry,
[2684.04 → 2684.36] trust me.
[2684.36 → 2684.46] Yeah.
[2684.82 → 2685.42] But like,
[2685.46 → 2687.96] especially in the biotech where it's like a white-hot,
[2688.10 → 2689.30] there's a lot of AI,
[2689.42 → 2689.56] you know,
[2689.56 → 2690.52] so is it really,
[2690.72 → 2691.08] you know,
[2691.34 → 2694.20] AI fully controlled the drug?
[2694.20 → 2694.56] No,
[2694.84 → 2695.98] there are a lot of people in the
[2695.98 → 2696.60] in the middle,
[2697.06 → 2699.10] but certain core components,
[2699.26 → 2699.50] the
[2699.50 → 2701.46] the running of,
[2701.46 → 2701.94] of,
[2701.94 → 2702.32] uh,
[2702.32 → 2704.28] in vitro experiments in a Petri dish,
[2704.28 → 2708.30] the understanding of which patients are good for which therapies,
[2708.46 → 2709.30] these things,
[2709.30 → 2711.90] we are starting to have enough data where we can actually,
[2712.30 → 2715.30] the problems are blossoming into well-founded problems on their own.
[2715.30 → 2717.30] And one of the things that's exciting that,
[2717.40 → 2721.40] that we're beginning to see is people from outside the bio space are getting
[2721.40 → 2722.46] excited by these problems,
[2722.46 → 2722.80] right?
[2722.84 → 2723.00] So,
[2723.36 → 2728.34] so we have people and Emmy and I have collaborations with top tier professors and
[2728.34 → 2731.16] research institutions who are not biologists,
[2731.16 → 2735.04] but are excited by the data and the mission that we have and want to,
[2735.10 → 2736.16] want to get in on it.
[2736.24 → 2736.72] And to me,
[2736.72 → 2741.62] this is the like fields that can attract top talent to come and join the
[2741.62 → 2745.28] the sort of fight to build out the core building blocks of this ultimate
[2745.28 → 2746.02] pipeline are,
[2746.38 → 2747.18] this is very,
[2747.18 → 2747.60] um,
[2747.96 → 2748.64] very promising.
[2748.64 → 2753.42] And so what I think we're going to see is just more maturation of the
[2753.42 → 2756.44] handful of problems that need to be solved in order to generate,
[2756.70 → 2757.64] develop a therapy.
[2758.32 → 2759.54] And at Emmy and I ourselves,
[2759.54 → 2761.10] we are on this journey,
[2761.24 → 2761.46] you know,
[2761.54 → 2761.96] you know,
[2761.96 → 2762.38] we are,
[2762.50 → 2762.72] you know,
[2762.76 → 2764.52] one biotech company,
[2764.52 → 2768.72] we're about 150 people and which is tiny compared to some of the
[2768.72 → 2769.58] some of the big guys,
[2769.66 → 2770.68] but big compared to some,
[2770.82 → 2770.98] you know,
[2770.98 → 2772.10] some tiny biotechs.
[2772.26 → 2772.28] And,
[2772.50 → 2774.84] and we're trying to,
[2774.94 → 2775.12] you know,
[2775.28 → 2779.08] be at the head of the pack here of identifying what are the problems that
[2779.08 → 2781.88] need to be wrapped up and solved cohesively.
[2782.36 → 2782.72] But,
[2782.80 → 2783.16] uh,
[2783.16 → 2785.84] there are a lot of people out there and no one company is going to do it.
[2785.84 → 2786.04] And,
[2786.22 → 2788.50] but I couldn't be more excited about the next decade.
[2788.50 → 2790.14] I think a decade from now,
[2790.14 → 2791.18] like my goal,
[2791.18 → 2792.58] and I think many people at Emmy and me,
[2792.74 → 2794.88] and probably lots of other people in the biotechs world,
[2795.38 → 2795.58] you know,
[2795.58 → 2796.14] you look at,
[2796.14 → 2796.36] uh,
[2796.36 → 2797.68] HIV now,
[2798.06 → 2798.36] you know,
[2798.38 → 2798.70] uh,
[2798.70 → 2799.42] 30 years ago,
[2799.48 → 2800.22] generation ago,
[2800.30 → 2801.68] HIV killed people.
[2802.06 → 2802.42] Like,
[2802.46 → 2802.62] uh,
[2802.62 → 2803.88] they had months to live when you've,
[2803.94 → 2806.52] you got HIV, and now it's a chronic condition,
[2806.68 → 2806.92] you know,
[2806.96 → 2807.06] we,
[2807.22 → 2807.42] you know,
[2807.42 → 2807.78] and it's,
[2807.84 → 2809.42] and in some cases we've actually been able to cure it.
[2809.82 → 2810.84] And I think that,
[2810.92 → 2811.28] uh,
[2811.28 → 2811.98] with cancer,
[2812.26 → 2813.20] we are like,
[2813.24 → 2814.28] this is within striking distance.
[2814.28 → 2815.26] Like we can do this.
[2815.26 → 2815.50] And,
[2815.50 → 2816.12] you know,
[2816.16 → 2817.38] AI is not going to solve this.
[2817.42 → 2818.38] It's not a magic wand,
[2818.38 → 2819.76] but the combination of,
[2819.76 → 2820.38] you know,
[2820.82 → 2821.34] AI,
[2821.86 → 2822.28] data,
[2822.70 → 2823.52] good people,
[2823.94 → 2825.94] amazing experimental methodologies,
[2826.40 → 2827.74] all of this is going to come together,
[2828.02 → 2829.24] our better understanding of the immune system.
[2829.24 → 2829.82] I think over the
[2829.92 → 2830.08] you know,
[2830.10 → 2830.94] over the next generation,
[2830.94 → 2834.14] I want to be able to tell my grandkids that like I helped,
[2834.24 → 2834.64] uh,
[2834.64 → 2835.26] sort of like,
[2835.32 → 2835.68] uh,
[2835.68 → 2836.68] solve cancer.
[2836.88 → 2838.38] And I think that it's a
[2838.46 → 2841.16] it's this sort of like a grand challenge,
[2841.16 → 2841.66] but,
[2841.78 → 2842.06] uh,
[2842.08 → 2844.22] what kind of challenge do you want to work on in your life?
[2844.58 → 2844.68] Yeah.
[2844.80 → 2845.04] Well,
[2845.14 → 2845.32] I,
[2845.44 → 2848.82] I think that's a really encouraging and inspiring way to,
[2848.92 → 2850.00] to end my day.
[2850.00 → 2851.38] And in this conversation,
[2851.38 → 2853.10] I'm really excited about,
[2853.10 → 2853.46] uh,
[2853.46 → 2854.40] the things that you're doing,
[2854.50 → 2856.58] Jocelyn and the whole team there.
[2856.58 → 2859.22] And it's fascinating to get a sort of view,
[2859.24 → 2864.24] into AI within this space and how it's also being influenced by things
[2864.24 → 2865.56] happening elsewhere in industry.
[2865.84 → 2867.36] So thank you so much for,
[2867.36 → 2867.68] uh,
[2867.68 → 2867.98] sharing,
[2868.20 → 2869.26] sharing these insights with,
[2869.42 → 2870.20] with us and,
[2870.28 → 2870.50] um,
[2870.50 → 2872.30] looking forward to following your work.
[2873.04 → 2873.46] Thank you so much,
[2873.50 → 2873.86] Chris Daniel.
[2873.92 → 2874.74] It's been a real pleasure.
[2883.44 → 2884.38] All right.
[2884.48 → 2886.52] That is Practical AI for this week.
[2886.80 → 2888.58] If this is your first time listening,
[2888.96 → 2891.88] subscribe now at practical AI.fm,
[2892.06 → 2895.08] or just search for Practical AI in your favourite podcast app.
[2895.18 → 2895.80] We're in there.
[2896.10 → 2897.30] And if you're a long time listener,
[2897.64 → 2899.36] please do share the show with your friends.
[2899.52 → 2902.26] It is the best way you can help Practical AI succeed.
[2902.72 → 2905.80] Thanks again to Vastly for shipping our shows superfast,
[2905.86 → 2906.74] all around the world,
[2906.98 → 2908.62] to Break master Cylinder for the Beats,
[2908.78 → 2909.82] and to you for listening.
[2910.00 → 2910.76] We appreciate you.
[2911.12 → 2912.22] That's all for this week.
[2912.22 → 2913.46] We'll talk to you again next time.
[2913.46 → 2920.04] Okay.
[2920.04 → 2927.04] Game on!
