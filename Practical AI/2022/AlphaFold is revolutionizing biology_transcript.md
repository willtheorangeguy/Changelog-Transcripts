[0.00 --> 4.38]  I do know that proteins are the foundation of all life.
[4.62 --> 6.04]  They can be incredibly complex.
[6.50 --> 10.48]  Many of our longtime listeners will know that I'm really into animal welfare causes, and
[10.48 --> 12.66]  particularly I handle venomous snakes quite often.
[12.94 --> 18.28]  But a friend of mine, Dr. Brent Siegel, he and I will often talk about snake venom.
[18.28 --> 23.82]  And Brent, with his expertise in chemistry, he'll go and check on the protein makeup of
[23.82 --> 28.92]  snake venom, and then he'll look at the protein molecules and the folds and where they're
[28.92 --> 36.42]  at, and he can just tell me exactly how those proteins are affecting and if someone's bitten.
[37.04 --> 41.64]  Protein folding may sound really esoteric to those of us who are not in biology professionally,
[41.64 --> 47.02]  but it's crucial to understanding chemistry and life itself.
[47.02 --> 63.72]  Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive,
[63.72 --> 65.04]  and accessible to everyone.
[65.40 --> 67.08]  Subscribe now if you haven't already.
[67.32 --> 70.18]  Head to practicalai.fm for all the ways.
[70.58 --> 75.54]  Special thanks to our partners at Fastly for delivering our shows super fast to wherever
[75.54 --> 78.34]  you listen, check them out at Fastly.com.
[78.60 --> 84.34]  And to our friends at Fly.io, we deploy our app servers close to our users, and you can
[84.34 --> 84.70]  too.
[85.04 --> 86.92]  Learn more at Fly.io.
[93.02 --> 98.10]  Welcome to another fully connected episode of the Practical AI podcast.
[98.10 --> 103.94]  In these fully connected episodes, Chris and I keep you fully connected with everything
[103.94 --> 106.00]  that's happening in the AI community.
[106.24 --> 112.96]  We'll take some time to dissect a little bit of the latest AI news and dig into a few learning
[112.96 --> 116.40]  resources to help you level up your machine learning game.
[116.90 --> 117.74]  I'm Daniel Whitenack.
[117.82 --> 120.50]  I'm a data scientist with SIL International.
[120.80 --> 126.16]  I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[126.68 --> 127.36]  How are you doing, Chris?
[127.36 --> 129.14]  Doing really well today.
[129.40 --> 133.74]  Excited about the thing that you're about to tell our audience we're going to talk about.
[134.32 --> 137.98]  And I just wanted to put a tiny bit of context around.
[138.18 --> 138.30]  Sure.
[138.58 --> 145.10]  We've gone through the pandemic and there are major wars that we've talked about ongoing
[145.10 --> 146.26]  as we record this.
[146.94 --> 149.42]  And monkeypox is now out.
[149.58 --> 155.74]  Wasn't it just called, I don't know the designation, they're just designated as an emergency status
[155.74 --> 157.02]  somehow or something like that.
[157.02 --> 159.72]  Yeah, both who and then now the United States has declared it such.
[160.16 --> 163.68]  And as of yesterday, as we record this.
[163.86 --> 170.88]  And so we're going to be talking about a topic today that reminds me that we live in the most
[170.88 --> 172.72]  interesting time in human history.
[173.12 --> 176.26]  And things are changing faster than they ever have.
[176.26 --> 179.16]  And there's actually a lot of reason to have hope in the world.
[179.40 --> 184.30]  As we talk about the possibilities that we're going to talk about today, I just want to kind
[184.30 --> 190.30]  of remind people that there's a lot of things that are really worth being positive about.
[190.42 --> 192.40]  And I think today's topic is frankly one of them.
[192.82 --> 192.86]  Yeah.
[192.86 --> 200.70]  A lot of people really doing things with tech that are beneficial, or at least the intention
[200.70 --> 203.38]  is that they would be overwhelmingly beneficial, right?
[203.38 --> 203.68]  Yes.
[203.98 --> 206.18]  So I think that this factors in.
[206.18 --> 211.98]  The topic that we'll be talking about today is AlphaFold and the corresponding database
[211.98 --> 214.54]  that they've released of protein structures.
[215.06 --> 220.24]  This came up and I was seeing, I don't know about you, Chris, but I've seen it pop up in
[220.24 --> 224.72]  my news feeds various times over the past couple of years.
[225.54 --> 231.64]  And most recently, just this week, I think it was coming up in the news because of some
[231.64 --> 234.24]  of the things that they've, that they've released.
[234.24 --> 241.00]  I think in particular, the sort of recent news is that they have this database of protein
[241.00 --> 248.86]  structures, and we can talk about kind of what that means and how it was generated, et
[248.86 --> 251.64]  cetera, here, you know, over the course of the podcast.
[251.82 --> 256.76]  But this, this database of protein structures, and they've just released and expanded that
[256.76 --> 261.86]  from 1 million structures to 200 million structures.
[261.86 --> 269.54]  So that's a pretty big, pretty big increase in terms of the size of the size of this database.
[269.54 --> 276.30]  And I don't know, we were just talking even before the episode, Chris, about proteins and
[276.30 --> 283.52]  maybe like how, how those can be important for the study of various things.
[283.76 --> 289.00]  I don't know if you, you want to chat about that at all, but it was definitely interesting
[289.00 --> 295.08]  to look at this project and understand a little bit more about that field, which I'm not, I'm
[295.08 --> 296.58]  not actively participating in.
[296.58 --> 300.98]  And it's important that we note that we're exploring this as non-experts.
[301.42 --> 301.52]  Yeah.
[301.64 --> 305.08]  Come with us along our journey of learning about AlphaFold.
[305.54 --> 311.96]  So, so, you know, obviously we're here with our listeners because we all love AI and we're
[311.96 --> 316.08]  exploring things, but often the use cases are things that we don't have expertise in.
[316.24 --> 320.64]  And this is one of those episodes that we call fully connected, where we're just, we're just
[320.64 --> 324.26]  exploring and we're bringing people along on the journey as we talk about this.
[324.26 --> 326.16]  And I have no particular expert.
[326.22 --> 330.68]  I took some biology in high school and college, but I have no particular expertise.
[331.06 --> 339.34]  But I do know that, that proteins are the foundation of all life and is incredibly important
[339.34 --> 345.62]  to understanding how they can be used in their application, their 3D structure.
[345.62 --> 347.60]  They can be incredibly complex.
[348.28 --> 352.42]  It's kind of, I'll actually give a, I know I've relayed this to you privately, but I'll
[352.42 --> 357.54]  give a quick setting on, on kind of why 3D structure is so important.
[358.04 --> 362.10]  Many of our long-time listeners will know that I'm really into animal welfare causes.
[362.10 --> 366.66]  And particularly I handle venomous snakes quite often with appropriate safety gear and
[366.66 --> 366.94]  such.
[366.94 --> 374.30]  But a friend of mine named Dr. Brent Siegel, who has a chemistry PhD from Harvard, he and
[374.30 --> 378.20]  I will often talk about, just for fun, it's not what either one of us is primary do, we'll
[378.20 --> 382.52]  talk about snake venom as just a fun two guys chatting thing.
[383.08 --> 389.00]  And Brent, with his expertise in chemistry, can literally look, we'll be talking comparing
[389.00 --> 396.72]  two species and he will be able to pick up, he'll go and check on the, look at the protein
[396.72 --> 397.88]  makeup of snake venom.
[398.24 --> 403.32]  And then he'll look at the protein molecules and the folds and where they're at.
[403.62 --> 410.78]  And right there off the cuff, he can just tell me exactly how those proteins are affecting
[410.78 --> 416.40]  and if it gets, if someone's bitten, what that will do and what that particular combination
[416.40 --> 417.04]  of proteins.
[417.26 --> 422.60]  And so protein folding may sound really esoteric to those of us who are not in biology professionally,
[422.60 --> 427.70]  but it's crucial to understanding chemistry and life itself.
[428.08 --> 432.14]  It really gave me an appreciation for this topic before we got to this episode.
[432.14 --> 436.86]  And so I'm pretty excited about the possibility and I think it's going to really revolutionize
[436.86 --> 437.24]  medicine.
[437.78 --> 437.86]  Yeah.
[437.86 --> 442.90]  And I think in this episode, at least what we're going to try to do is kind of talk through
[442.90 --> 449.06]  how the context for alpha fold, the data, how it sort of works and what the implications
[449.06 --> 449.48]  are.
[449.58 --> 455.02]  And so getting in the weeds a little bit with how this is actually operating, we'll get
[455.02 --> 456.52]  there at a certain point.
[457.04 --> 459.58]  But yeah, I think setting that context is good.
[459.76 --> 466.38]  I was looking through some articles again, because I'm not a chemist or a biologist, but
[466.38 --> 471.32]  looking through some articles that we'll link in our show notes as also good learning resources
[471.32 --> 479.56]  for you talking about the sort of reason why proteins and protein folding is useful.
[479.68 --> 484.34]  This is from the National Library of Medicine, which sounds very official.
[484.56 --> 488.06]  I don't actually know a lot about the National Library of Medicine.
[488.44 --> 495.64]  They talk about how the proteins are basic building blocks of all cells in our body and
[495.64 --> 503.00]  living creatures and that we kind of often think of DNA as being at the core or DNA and
[503.00 --> 509.14]  genes as sort of being at the core of the information needed for life, which is true.
[509.38 --> 515.78]  But then the sort of dynamic processes of life, like the things that happen in our bodies,
[515.92 --> 522.16]  that like the functions and the processes, defense mechanisms and reproduction of certain
[522.16 --> 527.18]  things in our bodies, all of those sort of dynamic processes are carried out by proteins,
[527.18 --> 534.34]  which, you know, do this kind of folding and assembly into all of these complexes to actually
[534.34 --> 536.54]  perform functions, right?
[536.60 --> 538.66]  So it's like the functional process.
[538.94 --> 539.38]  Exactly.
[539.70 --> 544.88]  I mean, and to really get that tangible, I mean, and these are examples we've seen in many of
[544.88 --> 551.72]  these articles on this is, you know, the fact that your eye and the retina can receive light
[551.72 --> 557.68]  and process that light to your brain, the mere fact that it can do that is protein based.
[557.86 --> 562.66]  The fact that right now you're probably, even if you're sitting down, you're probably moving
[562.66 --> 563.60]  some part of your body.
[563.74 --> 567.64]  And that movement that you're engaged in right now is based on proteins.
[567.84 --> 574.50]  It's just impossible to escape that fundamental, you know, kind of function that proteins provide,
[574.50 --> 577.00]  you know, a billion different things.
[577.60 --> 583.48]  And so this, this kind of technology, it's going to be really fundamental to, to, to life going
[583.48 --> 583.82]  forward.
[583.82 --> 589.82]  And I know I was joking to you that earlier that I wish I was younger than I am now, not
[589.82 --> 595.06]  because not just from an age standpoint, but because then these kinds of technologies could
[595.06 --> 599.10]  positively influence me for more years than they're currently going to be able to.
[599.20 --> 603.30]  It's, it's like I, I, every time I see these great advances coming out and I'm in my early
[603.30 --> 607.24]  fifties and I'm looking at it kind of going, God, why couldn't that have happened in my
[607.24 --> 609.08]  twenties or something like that?
[609.14 --> 611.06]  So it is pretty cool stuff here.
[611.92 --> 614.48]  One of the interesting things to me is like they're releasing.
[614.86 --> 622.64]  So we kind of talked about how protein structure is important and how it sort of is tied to
[622.64 --> 628.24]  the, the basic functions of life and why that, like you're saying is important for advances
[628.24 --> 629.82]  in medicine and other things.
[630.20 --> 636.22]  What's interesting is that all of this complicated function and process that are carried out by
[636.22 --> 642.92]  proteins are, are fundamentally driven by sequences of what's called amino acids.
[643.12 --> 645.24]  And there's 20 of these amino acids.
[645.24 --> 650.22]  And so I was trying to think of like a metaphor and I don't know if this has been used.
[650.28 --> 653.98]  I'm probably stealing it from someone, but when I was going through it and looking at the
[653.98 --> 659.16]  stuff, the sequences of amino acids, there's 20 of them, you know, you can think about how
[659.16 --> 666.78]  much complexity we can see formed out of 26 letters of the, you know, Roman alphabet in
[666.78 --> 667.74]  all sorts of languages.
[667.74 --> 673.08]  And there's, you know, you can express, you know, innumerable things with that, uh, kind
[673.08 --> 674.88]  of small set of characters.
[675.28 --> 678.40]  Here we have this sort of sequence of amino acids.
[678.40 --> 684.48]  There's 20 of these acids and that's what forms proteins and drives how they fold and
[684.48 --> 686.88]  how they assemble and how they do all these functions.
[686.88 --> 694.44]  And so when we're thinking about like, how does this intersect with AI, the process or
[694.44 --> 701.04]  the, the data transformation that we can think about is like on one end, you have sequences
[701.04 --> 703.88]  of amino acids that you might know about.
[703.88 --> 711.58]  And then on the other end, you have the folds and the assemblies and the geometric structures,
[711.76 --> 717.66]  the 3d structures that are driven, the protein structures that are driven by these sequences
[717.66 --> 720.30]  of amino acids or that you could predict from these.
[720.44 --> 725.34]  So an AI model, as we've talked about many times in this show is, you know, at its core,
[725.44 --> 726.90]  it's a data transformation, right?
[726.92 --> 732.34]  You take an image in and then you get a label out or, you know, something like that.
[732.34 --> 738.98]  Here you're taking these sequences of amino acids in and out of it, you're predicting a
[738.98 --> 741.06]  3d structure of one of these proteins.
[741.06 --> 745.80]  That's really the fundamental kind of data transformation that we're talking about, which
[745.80 --> 750.64]  is what alpha fold is addressing is sequences to 3d structure.
[750.78 --> 754.80]  That's, that's at the main core of what we're talking about.
[755.28 --> 759.86]  And I think in some of the materials that we reviewed ahead of time, if I'm understanding
[759.86 --> 764.50]  them correctly, you know, those different amino acids, the folding itself is kind of amino
[764.50 --> 765.64]  acid to amino acid.
[765.78 --> 770.42]  So even though we're talking about sequences and, and you tend to think about a line of
[770.42 --> 776.00]  amino acids with the word sequence, but it's being folded in 3d with those different amino
[776.00 --> 779.74]  acids connecting to each other in different ways and lots of different shapes.
[779.74 --> 784.26]  So even one sequence can have many, many different possibilities.
[784.26 --> 788.98]  They're going back to your point, you know, even different folds with the same amino acids
[788.98 --> 790.82]  is, is, is the impression I'm taking away.
[790.90 --> 793.08]  So there's a lot to happen there.
[793.08 --> 797.46]  And as I'm, is kind of referencing back what I talked before about my friend, Brent, he can
[797.46 --> 803.60]  look at that and see a functional kind of what it will do after that.
[803.60 --> 807.48]  So it's, it's very, very practical AI that we're talking about here.
[807.48 --> 813.06]  We're talking about something that, that is something that, that the output is, can be
[813.06 --> 818.68]  put in the hands of an expert who can immediately see in many cases where this is going and what
[818.68 --> 819.72]  the, what the effect will be.
[819.80 --> 822.08]  So super practical medicine we're talking about here.
[822.08 --> 823.48]  Yeah, definitely.
[823.70 --> 829.84]  And I guess to kind of bring home the importance of the methods that we're about to go into
[829.84 --> 836.56]  previously, I mean, it has been known that knowing these structures and the folding process
[836.56 --> 837.94]  is important.
[837.94 --> 843.66]  And so people have done experiments over time and you can find out the structures via experiment.
[843.84 --> 845.92]  I, I don't know all the details of that.
[846.12 --> 850.00]  Maybe we can find a link to share in our show notes, but experimentally you can find these
[850.00 --> 850.38]  things out.
[850.38 --> 855.68]  But of course, anything that involves, you know, chemistry and biology experiment is going
[855.68 --> 862.78]  to be limited in terms of the pace and capacity that you can do as we've all learned in terms
[862.78 --> 867.26]  of lab testing, you know, COVID results and that sort of thing in recent years.
[867.26 --> 875.16]  So there's a limiting factor on that, which means that were you to be able to predict protein
[875.16 --> 881.08]  structures with a computer, which is maybe not, it still has a cost, right?
[881.08 --> 886.60]  In terms of computational cost and environmental cost and other things, but were you to do it,
[886.66 --> 890.82]  you're not, you're no longer constrained by your sort of experimental capacity.
[890.82 --> 895.66]  You're constrained maybe by your computational capacity and that sort of thing.
[895.76 --> 899.00]  And so the, the scaling mechanism is, is quite different.
[899.22 --> 904.76]  I think, and to that point, I believe there was roughly a, correct me if I'm, if I'm not
[904.76 --> 911.08]  remembering this accurately, but I think that the, that it was trained on roughly 150,000
[911.08 --> 915.04]  known protein folds that had all been human determined.
[915.28 --> 917.40]  You know, this was before the AI was applied.
[917.40 --> 919.12]  So that was the baseline.
[919.46 --> 925.66]  And to talk about the, the leap that we're describing here, what was announced on July
[925.66 --> 932.04]  28th, which was just a few days ago, as we record this was the fact that from that training
[932.04 --> 941.04]  set of 150,000, they went to 200 million, which describes nearly the entire universe of
[941.04 --> 942.24]  known folds.
[942.46 --> 945.34]  And I'm sure that there are more that they're going to continue to work on, but kind of that's
[945.34 --> 948.08]  everything that we currently know for all practical purposes.
[948.08 --> 954.94]  So that's, you know, you're going from a fairly small subset to most everything in this one
[954.94 --> 957.48]  big release that we'll talk about with the database and everything.
[957.48 --> 960.14]  So I'm pretty excited about what comes next.
[960.14 --> 962.14]  Okay.
[962.14 --> 963.14]  Okay.
[963.14 --> 990.12]  Well, let's maybe give just a little bit of context for alpha fold and then talk about
[990.12 --> 993.30]  the database that they've released a little bit.
[993.46 --> 999.82]  So my understanding is that alpha fold kind of, it first started getting notoriety because
[999.82 --> 1004.90]  of these shared tasks that were really like what I would think of in the AI world, the shared
[1004.90 --> 1009.68]  tasks, maybe they're called something different in the biology world, but there's the shared
[1009.68 --> 1017.24]  tasks within a certain community critical assessment of techniques for protein structure prediction
[1017.24 --> 1019.24]  or the CASP.
[1019.24 --> 1022.24]  I guess, assuming I'm saying that correct, CASP.
[1022.24 --> 1030.40]  And they've had these over time, you know, over the years and CASP 14 was one of those shared
[1030.40 --> 1038.44]  tasks where alpha fold really kind of stood out from the rest of the pack in terms of what
[1038.44 --> 1045.98]  it was providing and really showed the ability to very closely replicate the accuracy that
[1045.98 --> 1049.88]  you could achieve via experiment with predicting these structures, right?
[1049.94 --> 1055.32]  Because the experiment in and of itself also has error related to it, right?
[1055.44 --> 1061.76]  So when you do an experiment to get these structures, you also don't get like a hundred percent accuracy.
[1061.94 --> 1064.02]  There's error bars and all of those things.
[1064.02 --> 1069.52]  And so what they were showing, which is quite extraordinary, is that this alpha fold thing,
[1069.66 --> 1074.08]  which we'll talk about more and get into the weeds of, is able to take these sequences
[1074.08 --> 1081.82]  and a sort of database of sequences in and output structures that are of the same kind of level
[1081.82 --> 1088.22]  of quality as experiment in many cases, which means, hey, well, now you have a sort of choice.
[1088.44 --> 1093.52]  You could run experiments, but if you're getting about the same accuracy out of the simulation,
[1094.02 --> 1098.60]  then that scales, like you were talking about, the scale that you can achieve with that is
[1098.60 --> 1100.16]  something wildly different.
[1100.38 --> 1103.92]  Yeah, I think all of the outputs are obviously being from an AI model.
[1104.02 --> 1104.72]  They're all predictions.
[1105.48 --> 1111.84]  The accuracy of those predictions has proven to be something that is significant enough to where
[1111.84 --> 1117.20]  further research based on those outputs can proceed rather than a lot of kind of going back
[1117.20 --> 1123.82]  and trying to figure out if the output of the model is sufficient in terms of accuracy to be able
[1123.82 --> 1125.96]  to base further research on it.
[1126.10 --> 1130.02]  So it's not just turning out a lot of outputs.
[1130.18 --> 1133.64]  It's also the fact that they're very high quality.
[1134.28 --> 1140.48]  And those two features together are what's going to really propel things forward in the larger
[1140.48 --> 1144.56]  biology and chemistry space here to drive medicine forward for all of us.
[1144.56 --> 1148.52]  The method that they're doing has created these predictions.
[1149.66 --> 1155.86]  And so it's really this bank of predictions that is part of this release that has been,
[1155.86 --> 1157.56]  you know, getting a lot of attention.
[1158.00 --> 1162.40]  We'll link to a blog post about the release in our show notes.
[1162.40 --> 1165.88]  But one of the things that I thought was really interesting, Chris, I don't know if you saw this,
[1165.88 --> 1169.82]  was there is a figure of like one circle, which was the experiment today.
[1169.82 --> 1174.40]  Like how many structures do we have in our database of experiments?
[1174.86 --> 1178.86]  And then the database when it was originally released, because they originally released
[1178.86 --> 1181.62]  the AlphaFold database with about a million structures.
[1182.16 --> 1185.86]  And then they have kind of the circle of AlphaFold database today.
[1186.04 --> 1191.88]  And the scale just sort of like for our listeners who aren't seeing this in front of them right now,
[1191.88 --> 1194.24]  it's like one big circle, which is the database today.
[1194.24 --> 1199.24]  And experiment is sort of like a little dot within that in terms of what it represents,
[1199.24 --> 1205.68]  because experimental structures in a database, one of these I understand is called PDB,
[1205.92 --> 1208.94]  has about 190K structures.
[1209.32 --> 1213.18]  And Chris, that's what you're saying, these sort of supervised examples that they used in training.
[1213.44 --> 1219.04]  And then AlphaFold today, the database has 200 million plus.
[1219.36 --> 1221.12]  So that's pretty crazy.
[1221.12 --> 1226.96]  They also give these circles representing how much is from different places.
[1226.96 --> 1233.64]  And you've got kind of a circle for animals and plants and bacteria and fungi and other animals is the biggest category.
[1233.64 --> 1236.84]  But then you have plants, bacteria, fungi and other things.
[1236.84 --> 1241.48]  So it's pretty interesting, both the diversity and the size of this, I would say.
[1241.48 --> 1251.26]  And again, I'm near the field, but my understanding in terms of what's offered here is actually, you know, 3D structures.
[1251.26 --> 1255.28]  So you can look up AlphaFold itself is open source.
[1255.50 --> 1257.82]  So the inference pipeline is open source.
[1258.08 --> 1260.76]  As far as I know, the training pipeline isn't.
[1260.84 --> 1262.56]  But the inference pipeline is open source.
[1262.68 --> 1266.48]  And you can look kind of in 3D at the structures that are coming out.
[1266.56 --> 1270.08]  So it's like 3D Cartesian coordinates that are coming out.
[1270.08 --> 1272.18]  You put this sequence of amino acids in.
[1272.68 --> 1282.40]  You get this 3D Cartesian coordinates out, which are really just this 3D structure representing the structure, 3D structure of the proteins.
[1282.90 --> 1282.98]  Yeah.
[1283.12 --> 1288.64]  You know, as a data set, the ability to do that and then combine with previous technologies, you know.
[1288.64 --> 1295.26]  So if you go back a few years and you talk about how big it was to release the human genome.
[1295.48 --> 1295.64]  Yeah.
[1295.74 --> 1304.90]  And that provides a different set of capabilities, you know, in terms of understanding, you know, what our genetic predispositions are and all sorts of different use cases.
[1304.90 --> 1314.46]  But now with the protein folding, to be able to, you know, to maybe start with the genome and understand what's likely to happen and what your predispositions are.
[1314.64 --> 1323.22]  And then you can go use protein folding from this database and be able to solve for some of those issues is pretty remarkable.
[1323.22 --> 1323.70]  Yeah.
[1323.70 --> 1340.48]  I think also it's like when you think of the scale 200 million, one of the other things that comes to my mind, and I'm sure people are exploring this and, you know, our listeners, please share links with us in our Slack or Twitter or LinkedIn or wherever of studies that you know about.
[1340.48 --> 1343.76]  But you have this now this data set of 200 million.
[1343.76 --> 1350.64]  I'm thinking like, oh, what does it look like to do clustering sort of techniques on top of that?
[1351.08 --> 1360.08]  Can you learn about the sort of structures now that like all of the proteins are kind of mapped to these 3D structures?
[1360.48 --> 1366.84]  What can you learn at a more aggregate level about like clusters of folding patterns or structures?
[1366.84 --> 1373.18]  What can you kind of post process this data set into and maybe build models off of these 3D structures?
[1373.18 --> 1382.70]  We all know that like the graph neural networks now are, you know, are a huge thing that's that's coming up and people are exploring that more and more.
[1382.92 --> 1386.92]  So obviously, these are 3D sort of spatial graphs.
[1386.92 --> 1395.20]  And it would be interesting to know what are people doing with these structures on the on the back end after they're after they're formed?
[1395.20 --> 1399.18]  I think that's an interesting direction to study as well.
[1399.54 --> 1402.96]  Yeah, I'm looking at these same these same documents that you are.
[1403.38 --> 1411.74]  And I can't help but think about the fact that is hopefully this is unleashing this revolution in this type of research.
[1411.88 --> 1413.22]  And you talk about that.
[1413.46 --> 1420.32]  I'm wondering how many high school and college kids today who have an interest that crossover might might leap into this.
[1420.38 --> 1424.50]  I think I think this is a moment we're going to remember just like the release of the human genome was.
[1424.50 --> 1425.40]  Yeah, yeah.
[1425.74 --> 1435.94]  And they already I mean, they already talk about the impact that AlphaFold is having even just a couple of months after this sort of release.
[1435.94 --> 1445.36]  I see here that after they open source AlphaFold in the database, it's already been cited more than 4000 times in academic research.
[1445.36 --> 1459.44]  And there's, you know, there's, you know, there's a large complex that acts as a gateway in and out of the cell nucleus.
[1459.44 --> 1465.98]  There's from something having to do with malaria, which is a protein for including in vaccines.
[1465.98 --> 1479.06]  There's something having to do with the rate of mRNA degradation, which I think a wider audience is now more familiar with mRNA after all of the vaccine stuff.
[1479.44 --> 1479.46]  COVID.
[1479.84 --> 1480.12]  Yes.
[1480.12 --> 1481.16]  Yeah, yeah.
[1481.44 --> 1489.22]  There is something having to do with causing frost damage to plants, which is obviously an agricultural thing.
[1489.30 --> 1492.90]  So even outside of medicine, you could think about agriculture and other things.
[1493.16 --> 1497.94]  That's a really good point you're making, because I think we're focused in our conversation very much on medicine.
[1497.94 --> 1502.82]  But, you know, agriculture, food supplies, there are so many different areas.
[1503.32 --> 1509.30]  Pretty much, you know, everything in life, not just us walking around, are impacted by this.
[1509.62 --> 1509.96]  And so.
[1510.30 --> 1519.46]  And I know with your interest, Chris, I had noticed this one, too, about something involved in the immune system of egg-laying animals, including honeybees.
[1519.46 --> 1530.72]  And, of course, we, you know, you're probably even more familiar than I am with sort of how honeybees and, you know, bee populations are in decline and having a crisis.
[1530.72 --> 1533.08]  It's a huge, yeah, it's a huge crisis that we're in.
[1533.38 --> 1533.58]  Yeah.
[1533.82 --> 1538.70]  So who knows how this could impact many of those things.
[1539.22 --> 1544.90]  Well, maybe we could jump now a little bit and start talking about how does AlphaFold do this?
[1544.90 --> 1552.16]  So I think that we've established, hey, it's caught the attention of many people because it does a really good job at this.
[1552.56 --> 1555.58]  They've open sourced the inference pipeline so people can use it.
[1555.66 --> 1558.06]  But what does AlphaFold do?
[1558.18 --> 1559.48]  I mean, this is practical AI.
[1559.64 --> 1571.88]  So we could probably all learn, even if we're not all doing protein folding, maybe there's elements of the way that they're processing this data that are useful in our own creativity, in our own problems.
[1571.88 --> 1585.20]  And I think it's interesting that in their processing pipeline, you see sort of a number of really interesting things popping up from other domains.
[1585.60 --> 1589.34]  So the transformer architecture pops up within this.
[1589.34 --> 1602.40]  There's what they're calling an Evo former, which we can get into why it's maybe Evo evolution related in terms of how it is also iterative.
[1602.58 --> 1605.52]  But there's this Evo former architecture.
[1606.24 --> 1610.34]  There's this element of like joint embeddings.
[1611.24 --> 1617.56]  And also there's in the training, they use sort of supervised and like semi-supervised methods.
[1617.56 --> 1627.00]  They also use these like BERT style, not in a pre-training way, but they use a BERT style masking in their training as well, which all of those things.
[1627.50 --> 1629.28]  I think we talked about this on a similar episode.
[1630.06 --> 1644.92]  This sort of innovation is built off of a number of things that have just been sweeping across the whole AI world, including, you know, you're thinking about transformers, these joint embeddings, semi-supervised methods, mass language models.
[1644.92 --> 1651.38]  All of these elements kind of contribute somehow to how the data is processed in this pipeline.
[1651.74 --> 1651.82]  Yeah.
[1651.98 --> 1655.86]  A few episodes back, we had quite a conversation about that.
[1655.94 --> 1670.66]  And the fact that, you know, as an analogy, if you think about these different approaches that you just enumerated and think of them almost as Legos and the creativity then of scientists and researchers being able to say, well, I'm going to try this one.
[1670.66 --> 1675.92]  I'm going to try this one and then combine it with that one and maybe do it in a completely different domain.
[1676.30 --> 1679.42]  And then and you're getting these interesting outputs.
[1679.52 --> 1691.20]  And I think I think I was before this episode, I was kind of thinking about the fact that it's almost like about a year ago, we almost entered, I think, looking back kind of a new era of AI.
[1691.20 --> 1698.08]  There was kind of the development of those models for a while, but now we're seeing the mixing and matching of them and such.
[1698.66 --> 1701.02]  And I think that this is one of the outputs of that.
[1701.22 --> 1702.76]  And so, yeah, cool stuff.
[1702.96 --> 1703.58]  Yeah, definitely.
[1703.58 --> 1703.82]  Yeah.
[1703.82 --> 1703.88]  Yeah.
[1703.88 --> 1703.92]  Yeah.
[1703.92 --> 1703.96]  Yeah.
[1703.96 --> 1704.02]  Yeah.
[1704.02 --> 1704.14]  Yeah.
[1704.14 --> 1704.46]  Yeah.
[1704.46 --> 1704.96]  Yeah.
[1704.96 --> 1705.96]  Yeah.
[1705.96 --> 1706.96]  Yeah.
[1706.96 --> 1707.96]  Yeah.
[1707.96 --> 1708.96]  Yeah.
[1708.96 --> 1709.96]  Yeah.
[1709.96 --> 1710.96]  Yeah.
[1710.96 --> 1711.96]  Yeah.
[1711.96 --> 1712.96]  Yeah.
[1712.96 --> 1713.96]  Yeah.
[1713.96 --> 1714.96]  Yeah.
[1714.96 --> 1715.96]  Yeah.
[1715.96 --> 1716.96]  Yeah.
[1716.96 --> 1717.96]  Yeah.
[1717.96 --> 1718.96]  Yeah.
[1718.96 --> 1719.96]  Yeah.
[1719.96 --> 1720.96]  Yeah.
[1720.96 --> 1727.04]  Yeah.
[1727.04 --> 1728.14]  Okay, Chris.
[1728.14 --> 1748.36]  So I think if I'm understanding this right and you know, we've looked through a bunch of things here, even just you and I are learning about AlphaFold, but it seems like that the network or the architecture that's driving AlphaFold is, is kind of split up into a few different main components.
[1748.36 --> 1752.36]  The first of those kind of takes an input sequence.
[1752.36 --> 1758.36]  And then develops two kind of encodings of that input sequence.
[1758.36 --> 1759.36]  And then we have a couple of different components.
[1759.36 --> 1765.36]  One, which is called multiple sequence alignment and one which is a pair embedding or pair representation.
[1765.36 --> 1772.36]  So there's this first stage, which is input sequence to encoding then or encoding or embedding.
[1772.36 --> 1784.36]  And then there's a second stage, which takes that initial representation through a transformer inspired architecture to develop a sort of hidden representation.
[1784.36 --> 1798.36]  And then those hidden representations are then fed into a last stage, which outputs the actual kind of predicted Cartesian coordinates of the protein.
[1798.36 --> 1808.36]  So we've got kind of encoding this transformer based architecture, which produces a different representation or embedding.
[1808.36 --> 1812.36]  And then we've got a structure module which produces the Cartesian coordinates.
[1812.36 --> 1824.36]  And what's interesting and one of the reasons why I think they've used some terms related to evolutionary algorithms, Evo, former and stuff is, is actually an iterative piece of this.
[1824.36 --> 1837.36]  So those last two stages, kind of putting the representations through the transformer based architecture and then out the other end to generate the structure, those actually cycle.
[1837.36 --> 1841.36]  So they, at least in their paper, they say that they do that three times.
[1841.36 --> 1853.36]  So they kind of refine, they make an initial prediction of the structure and then refine that by passing it back through the network so that it kind of goes through this loop a few times.
[1853.36 --> 1857.36]  And then outputs a refined protein structure.
[1857.36 --> 1863.36]  It kind of has a recurrent network aspect to it there in the, in the diagrams that they show there.
[1863.36 --> 1864.36]  Yeah, exactly.
[1864.36 --> 1866.36]  There's this kind of looping that happens.
[1866.36 --> 1879.36]  And from what I was reading, it's, you know, using deep neural networks to predict protein structure in and of itself is not an innovation of this work.
[1879.36 --> 1890.36]  So people have tried this for quite a while, but I think that there's two kind of main pieces here that are really kind of set this apart.
[1890.36 --> 1896.36]  One of this is this Evoformer architecture, which is unique to what they've done.
[1896.36 --> 1909.36]  And the second is this kind of iterative process, which kind of helps the network learn across these representations and the predicted structure in a really powerful way.
[1909.36 --> 1915.36]  So, yeah, it's interesting in this first, we can kind of dive into a couple of these things.
[1915.36 --> 1926.36]  But the, the first one, it kind of reminded me a lot of some NLP things in, to some degree, because you've got this input sequence, which again is just the sequence of amino acids.
[1926.36 --> 1930.36]  And they generate two representations from this.
[1930.36 --> 1936.36]  So like it, maybe people are more familiar with NLP, you might have a sequence of characters, right?
[1936.36 --> 1946.36]  And you might assign like a number to each of these characters, because you have to represent text as numbers to a computer, because a computer knows how to calculate numbers, right?
[1946.36 --> 1949.36]  So here they're in some ways doing a similar thing.
[1949.36 --> 1954.36]  They're taking this input sequence and they're representing it by numbers, but in two kind of really interesting ways.
[1954.36 --> 1964.36]  One, which kind of tries to identify not identical, but other sequences that have been identified in living organisms.
[1964.36 --> 1969.36]  And it kind of creates this, what they're calling this multiple sequence alignment.
[1969.36 --> 1975.36]  So it's actually an alignment of this sequence with other sequences, a multi-sequence alignment.
[1975.36 --> 1987.36]  And then they have this pair representation where they're actually trying to identify proteins that have a similar structure and construct an initial representation.
[1987.36 --> 1997.36]  That's kind of a pair representation of these two things, thinking that there's similar things, maybe in the whole database that we've, we've learned about and similar proteins.
[1997.36 --> 1999.36]  So maybe we can learn from those things.
[1999.36 --> 2008.36]  So the initial sequence goes in these two representations, the multiple sequence or alignment, and then this pair embedding.
[2008.36 --> 2017.36]  So one, which is kind of a matrix of sequences and one, which is a pair representation of one sequence with another.
[2017.36 --> 2018.36]  Let me ask you a question.
[2018.36 --> 2019.36]  Let me ask you a question.
[2019.36 --> 2022.36]  That's more from your NLP background than this.
[2022.36 --> 2044.36]  But do you think that it would be fair to say going through that two-step process is sort of like pursuing the probabilities iteratively as it goes and kind of constantly working on where it's more likely going to be between having the multiple versions that it's producing in that intermediate step and then looking for other proteins that may have exhibited the same sequence.
[2044.36 --> 2049.36]  And therefore, you already have a sense of what that folding might look like.
[2049.36 --> 2054.36]  So in NLP, we leverage a lot of pre-training, which isn't leveraged here.
[2054.36 --> 2058.36]  And to some degree, learn like, hey, language behaves in a certain way.
[2058.36 --> 2063.36]  So I can learn kind of pre-train some things and learn some things that I can transfer in.
[2063.36 --> 2072.36]  I think the idea is slightly similar here in that I think what they're trying to say is, you know, proteins are different one from the other.
[2072.36 --> 2081.36]  But if you have similar sequences or similar templates of your protein, they're not going to be quite the same.
[2081.36 --> 2086.36]  But some fragments and structure is going to be conserved across them.
[2086.36 --> 2099.36]  So I think they're leveraging this existing database of knowledge and sort of these paired representations to kind of understand that, yeah, there's something unique about this single inference.
[2099.36 --> 2105.36]  But we also know a lot about other, you know, protein structure and nothing's completely sort of new.
[2105.36 --> 2111.36]  So they're likely to be the contact between proteins or amino acids.
[2111.36 --> 2114.36]  Yeah, the contact between amino acids.
[2114.36 --> 2121.36]  If that's similar in this case to another case, it's likely that some of these fragments of structure will be preserved as well.
[2121.36 --> 2127.36]  I got to say, Dr. Whitenack, for someone who is not trained in this field, that is quite a good explanation.
[2127.36 --> 2134.36]  I'll let our listeners who have some type of chemistry and biology background correct me in our Slack channel or something.
[2134.36 --> 2146.36]  But I am very thankful to I should give a shout out actually to there's a series of of blogs that I looked at from the Oxford Protein Informatics group.
[2146.36 --> 2155.36]  So if you're listening out there, if we got any listeners from that group, thank you for your blog posts and your work and explaining many of these things because they're very useful.
[2155.36 --> 2158.36]  We'll make sure and link those in the in the show notes as well.
[2158.36 --> 2163.36]  But, yeah, you sort of got this representation, this initial representation.
[2163.36 --> 2175.36]  And then that, as we've learned, is useful basically everywhere, whether we're talking about images or text or whatever these initial representations, the MSA or multiple sequence alignment.
[2175.36 --> 2184.36]  And then this pair embedding are passed through a transformer based architecture, which is this Evo former, which is a unique architecture.
[2184.36 --> 2190.36]  And you can read more about kind of some of their choices that they made with that architecture in their paper and nature.
[2190.36 --> 2198.36]  But it passes through this this Evo former architecture, which exchanges information between the two representations.
[2198.36 --> 2209.36]  So between the multiple sequence alignment and the pair embedding and then outputs a kind of updated representation of both the multi sequence alignment and the pair embedding.
[2209.36 --> 2214.36]  The sort of hidden state of the model.
[2214.36 --> 2231.36]  And then that's what's passed into this third stage of the structure model, which takes those embeddings, takes that hidden representation and then maps it to 3D coordinates, 3D Cartesian coordinates, which is the output structure.
[2231.36 --> 2235.36]  And then, like we say, there's a looping thing that goes along.
[2235.36 --> 2242.36]  So actually, this structure is fed back into the front end of the second step, the transformer step.
[2242.36 --> 2252.36]  And you do this a couple of times where, you know, after generating one's structure, it's passed back and that information is passed back to refine the structure.
[2252.36 --> 2253.36]  I'm curious.
[2253.36 --> 2254.36]  I'm curious.
[2254.36 --> 2256.36]  And I'm going to throw another tough question to you.
[2256.36 --> 2259.36]  And it's fine to say too far, Chris.
[2259.36 --> 2260.36]  Yeah.
[2260.36 --> 2282.36]  But as you looked at the Evo former and kind of how it's approaching, do you have any thoughts on, as we're talking about this era of using these different components in different ways and combining them and going across domain, any thoughts on what an Evo former might be used for in other contexts?
[2282.36 --> 2283.36]  Do you have any?
[2283.36 --> 2284.36]  Yeah.
[2284.36 --> 2286.36]  That's getting out there a bit.
[2286.36 --> 2288.36]  And yeah, it's a very interesting question.
[2288.36 --> 2289.36]  I do.
[2289.36 --> 2292.36]  I do wonder, like one sort of random idea.
[2292.36 --> 2297.36]  And, you know, this is a random idea that I haven't thought about until this moment.
[2297.36 --> 2298.36]  So it's probably not.
[2298.36 --> 2300.36]  There's probably flaws in it.
[2300.36 --> 2315.36]  But I wonder if certain things like this could be used for, you know, multilingual models and that sort of thing, because you're taking these sort of multi sequence alignments, which are sequences of different proteins.
[2315.36 --> 2316.36]  Right.
[2316.36 --> 2320.36]  And I wonder, and they're kind of labeled accordingly.
[2320.36 --> 2328.36]  I wonder if you could have this sort of multi language alignment between different languages and then, you know, factor that in.
[2328.36 --> 2329.36]  I don't know.
[2329.36 --> 2330.36]  That's a random thought.
[2330.36 --> 2345.36]  But I definitely think that this sort of idea that you would take a single input and represent it in two initial representations that have a slightly different character and represent different things about kind of your problem space.
[2345.36 --> 2354.36]  And then combining the information of both of those representations in the transformer that could be applied in a number of different ways.
[2354.36 --> 2365.36]  You know, whether it's text input or image input, you could represent that in a couple of different ways that are useful and then mix those representations in this sort of Evo former type architecture.
[2365.36 --> 2375.36]  So I'm sure that even after alpha fold, some of those 4,000 citations do a much better job at postulating possibilities than myself.
[2375.36 --> 2378.36]  So maybe that wasn't too bad for off the cuff.
[2378.36 --> 2379.36]  Yeah.
[2379.36 --> 2393.36]  Maybe one one homework assignment for all of us would be to look at semantic scholar or something and look at the 4,000 citations and see which which are the ones popping up that are related to reuse of the Evo former architecture.
[2393.36 --> 2396.36]  I'm sure there's a few things that have already come out.
[2396.36 --> 2406.36]  I think it is interesting that we can just say something briefly maybe about the training of this before we close out because I think that is an interesting bit of this.
[2406.36 --> 2408.36]  We are practical AI after all.
[2408.36 --> 2416.36]  And I think we can learn maybe learn a little bit from the general training structure that they set up for alpha fold.
[2416.36 --> 2423.36]  And that is that they have this initial set of supervised examples from this P.
[2423.36 --> 2429.36]  I was going to say PBR, but that that's definitely not the right domain.
[2429.36 --> 2430.36]  What is it?
[2430.36 --> 2432.36]  PB something.
[2432.36 --> 2435.36]  The protein DB, PDB.
[2435.36 --> 2436.36]  That's it.
[2436.36 --> 2444.36]  So PDB, not Pabst Blue Ribbon, but PDB is this like 175, 190, whatever it was,
[2444.36 --> 2448.36]  set of existing protein structures, right?
[2448.36 --> 2467.36]  So they have supervised examples, but what they did was actually train sort of they train the alpha fold architecture on these supervised examples and then use the train model to generate the new structure of sort of like a bunch of different guesses that they had.
[2467.36 --> 2484.36]  And for the high confidence ones, they took they took 350,000 of those generated samples and combine them back in with the supervised the gold standard samples to create this mixed data set, which they then retrained alpha fold on.
[2484.36 --> 2509.36]  And so you have this mix of like supervised learning with what what they're calling this noisy student self distillation, which is basically this process of, hey, I'm going to use my model to generate new things and I'm going to add them back into going to add the high confidence ones back into my data set, which is a really interesting, I think, structure that a lot of people could use.
[2509.36 --> 2514.36]  You know, you don't have to be using alpha fold to use that idea, right?
[2514.36 --> 2518.36]  You can do that when you need to augment your data set somehow.
[2518.36 --> 2531.50]  And so I think that that that's maybe another learning to be taken away here that they're using some creative elements in the training as well, which help help them kind of boost the performance.
[2532.34 --> 2537.40]  So as as we wind up, I'd like to challenge we have so many practitioners in our audience.
[2537.40 --> 2558.68]  I would love to hear about some of the novel ways that they're taking these techniques and using them across other domains and combining them as that has really been fascinating in recent months to see some of the creativity in the space across different types of use cases.
[2558.68 --> 2573.42]  So I'm looking forward to hear what people are doing with Evoformers and some of the other combinations that are present in the architecture here to do completely new things that particularly those things that benefit the world at large.
[2573.90 --> 2576.58]  Yeah, yeah, definitely excited to hear about that.
[2577.00 --> 2584.30]  I've kind of already mentioned some learning resources for people and we have a bunch of links we'll add into our show notes that people can explore.
[2584.30 --> 2595.58]  But if you're looking for something to start with, DeepMind does have a really good brief explainer video about protein folding and alpha fold and how that fits together.
[2596.16 --> 2597.16]  So we'll include that.
[2597.24 --> 2598.66]  That's a really good starting point.
[2598.78 --> 2606.66]  And if that sparks your curiosity, they actually do have published a collab version of the inference pipeline.
[2606.98 --> 2611.70]  So you can actually spin up Google collab and try to predict some structures yourself.
[2611.70 --> 2616.60]  I think that would be maybe the best way to learn about this is just to just to try it.
[2616.68 --> 2619.28]  So we'll link the GitHub to alpha fold.
[2619.52 --> 2622.96]  And then, yeah, you can try try that out with that collab on your own.
[2623.22 --> 2625.08]  OK, well, awesome.
[2625.36 --> 2626.36]  I'll finish with this.
[2626.90 --> 2627.78]  You might share.
[2627.92 --> 2633.48]  I started with the idea that that there's a lot of reason to be optimistic about the world and the future.
[2633.70 --> 2633.98]  Yeah.
[2634.06 --> 2636.80]  Despite the fact that there are plenty of things to bring us down.
[2636.80 --> 2646.48]  If you've enjoyed this episode, you might go share some of this with the people in your life, whether they're into AI or not, just because it's worth knowing.
[2646.56 --> 2653.32]  It's worth knowing that the world is still moving forward in a really positive way, even when when other things are a bit challenging.
[2653.62 --> 2657.00]  So share this with people who you might not otherwise think about.
[2657.36 --> 2657.60]  For sure.
[2657.92 --> 2658.62]  And that'll be it.
[2658.88 --> 2660.28]  I'll talk to you next week, Daniel.
[2660.46 --> 2661.62]  Then good to chat, Chris.
[2661.70 --> 2662.34]  See you soon.
[2662.34 --> 2662.84]  Bye.
[2662.84 --> 2663.34]  Bye.
[2663.34 --> 2663.84]  Bye.
[2663.84 --> 2664.34]  Bye.
[2664.34 --> 2664.84]  Bye.
[2664.84 --> 2665.34]  Bye.
[2665.34 --> 2665.40]  Bye.
[2665.40 --> 2665.42]  Bye.
[2665.42 --> 2665.46]  Bye.
[2666.80 --> 2667.36]  Bye.
[2671.40 --> 2671.92]  All right.
[2672.06 --> 2673.62]  That is our show for this week.
[2673.80 --> 2676.24]  If you dig it, don't forget to subscribe.
[2676.54 --> 2679.44]  Head to practicalai.fm for all the ways.
[2679.96 --> 2685.36]  And if Practical AI has benefited your life, pay it forward by sharing the show with a friend or colleague.
[2685.74 --> 2688.68]  Word of mouth is the number one way people find shows like ours.
[2688.80 --> 2692.00]  Thanks again to Fastly for fronting our static assets.
[2692.24 --> 2694.70]  To Fly.io for backing our dynamic requests.
[2695.24 --> 2696.78]  To Breakmaster Cylinder for the Beats.
[2696.80 --> 2697.94]  and to you for listening.
[2698.18 --> 2698.84]  We appreciate you.
[2699.12 --> 2700.04]  That's all for now.
[2700.24 --> 2701.74]  We'll talk to you again on the next one.
