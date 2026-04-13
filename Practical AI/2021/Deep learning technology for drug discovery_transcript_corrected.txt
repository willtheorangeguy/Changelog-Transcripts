[0.00 → 3.10] People would come to me, and they'd say, hey, I've got a machine learning system.
[3.32 → 5.92] I can predict yesterday's stock price to within a dollar.
[6.18 → 7.04] Give me your life savings.
[7.12 → 7.80] We're going to be rich.
[8.50 → 11.10] And you'd hear that, and you'd say, OK, well, it's good that you can predict yesterday's
[11.10 → 11.54] stock price.
[11.72 → 12.56] That's something.
[13.08 → 14.88] Have you ever predicted tomorrow's stock price?
[15.60 → 17.72] And they'd say, OK, tough customer.
[18.14 → 22.00] And they'd go in, they'd come back, and they'd say, OK, now we can predict yesterday's stock
[22.00 → 22.98] price to within a dime.
[23.46 → 24.34] Give me your life savings.
[24.48 → 25.26] You know, we're going to be rich.
[25.50 → 27.56] And say, OK, well, that doesn't really answer my question.
[27.64 → 28.90] Have you predicted tomorrow's?
[28.90 → 32.44] And they'd say, I can tell you're you're you're an expert.
[32.58 → 32.80] Right.
[33.12 → 36.44] And they go in, they come back, and they say, now we can predict yesterday's stock price
[36.44 → 37.10] to within a penny.
[37.66 → 38.64] What more can you want?
[39.12 → 42.20] And basically, you look at that, and you say, I have less confidence now than I did at the
[42.20 → 42.42] beginning.
[44.60 → 47.06] Ba meth for Change Log is provided by Vastly.
[47.38 → 49.24] Learn more at Fastly.com.
[49.50 → 51.76] Our feature flags are powered by Launch Darkly.
[52.06 → 53.84] Check them out at LaunchDarkly.com.
[54.08 → 55.96] And we're hosted on Leno cloud servers.
[55.96 → 59.84] Get $100 in hosting credit at Leno.com slash Change Log.
[60.56 → 63.14] This episode is brought to you by our friends at O'Reilly.
[63.52 → 67.16] Many of you know O'Reilly for their animal tech books and their conferences, but you may
[67.16 → 69.64] not know they have an online learning platform as well.
[70.00 → 74.44] The platform has all their books, all their videos and all their conference talks.
[74.82 → 79.82] Plus, you can learn by doing with live online training courses and virtual conferences, certification
[79.82 → 85.14] practice exams, and interactive sandboxes and scenarios to practice coding alongside what
[85.14 → 85.56] you're learning.
[85.56 → 91.42] They cover a ton of technology topics, machine learning, AI, programming languages, DevOps,
[91.92 → 98.08] data science, cloud, containers, security, and even soft skills like business management
[98.08 → 99.50] and presentation skills.
[99.64 → 101.42] You name it, it is all in there.
[101.42 → 105.38] If you need to keep your team or yourself up to speed on their tech skills, then check
[105.38 → 106.92] out O'Reilly's online learning platform.
[107.46 → 110.96] Learn more and keep your team skills sharp at O'Reilly.com slash Change Log.
[111.10 → 113.34] Again, O'Reilly.com slash Change Log.
[113.34 → 132.52] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive,
[132.90 → 133.86] and accessible to everyone.
[134.10 → 138.26] This is where conversations around AI, machine learning, and data science happen.
[138.36 → 142.98] Join the community and Slack with us around various topics of the show at change.com slash
[142.98 → 144.62] community and follow us on Twitter.
[144.82 → 146.32] We're at Practical AI Epic.
[152.98 → 155.94] Welcome to another episode of Practical AI.
[156.36 → 157.84] This is Daniel Whiten ack.
[157.96 → 163.68] I am a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[163.68 → 168.34] Benson, who is a principal emerging technology strategist at Lockheed Martin.
[168.64 → 169.30] How are you doing, Chris?
[169.72 → 170.66] I am doing very well.
[170.70 → 171.52] How are you today, Daniel?
[171.52 → 173.14] Doing wonderful.
[173.30 → 178.22] Blessed as always, and especially this week, I got some sunshine and snow melting.
[178.74 → 180.94] So that's always a good thing.
[181.44 → 187.32] After a bit of a deep freeze in the States, for those that don't know, this is March of
[187.32 → 189.54] 2021 in real time.
[190.10 → 191.16] But yeah, how about you?
[191.24 → 192.06] How are things down there?
[192.34 → 193.72] Oh, spring has sprung.
[193.80 → 194.40] It's glorious.
[194.40 → 197.20] I'm desperately hoping we don't fall back to winter.
[197.74 → 201.18] So looking nice outside, having fun, doing some AI.
[201.54 → 202.38] What else is there?
[202.70 → 203.34] Yeah, exactly.
[203.68 → 212.52] So before last year, each spring here in Indiana, we go mushroom foraging for various types of
[212.52 → 212.86] mushrooms.
[212.86 → 219.34] And there are a number of apps that do classification of mushrooms based on a picture.
[219.48 → 221.00] You can take pictures of them.
[221.36 → 223.88] None of them are very good in my experience.
[224.08 → 225.36] I haven't liked any of them.
[226.16 → 231.68] And so last year, I was like, before next mushroom season, I'm going to make my own little mushroom
[231.68 → 233.34] classification app.
[233.34 → 234.82] But here we are.
[235.26 → 238.18] And, you know, such is not the case.
[238.68 → 243.74] So it'll be my continual side project.
[244.08 → 248.28] Maybe someone out there and one of our listeners, maybe if you're aware of any good apps like
[248.28 → 249.06] that, let me know.
[249.32 → 252.38] But yeah, it's a very interesting object recognition problem.
[252.72 → 253.48] So absolutely.
[253.76 → 256.02] Yeah, it's fun for anyone that wants a side project.
[256.42 → 257.44] So that sounds good.
[257.62 → 257.74] Yeah.
[257.74 → 263.50] This week, since I work in the defence industry, I'm focusing on this new, really long report
[263.50 → 265.22] that came out over 700 pages.
[265.36 → 266.06] Not thinking not about mushrooms?
[266.54 → 268.44] And it's not about mushrooms, actually.
[268.74 → 271.68] It's the National Security Commission on Artificial Intelligence.
[272.08 → 273.34] Oh, sounds very official.
[274.00 → 276.50] Yeah, it's basically saying we need to get with it.
[276.72 → 277.90] We need to get with it.
[278.14 → 279.42] And so I am consuming.
[279.68 → 283.58] I've kind of gone through the highlights, and I'm going through the detail of the report.
[283.58 → 289.20] So it's an interesting read and some completely boring and some, but lots of interesting tidbits
[289.20 → 290.22] sprinkled throughout.
[290.48 → 296.80] So if anyone has an interest in things at a government level, it's something.
[296.96 → 298.12] It's great bedtime reading.
[298.36 → 298.46] Okay.
[298.58 → 299.00] Yeah.
[299.00 → 299.18] Yeah.
[299.56 → 306.72] Well, Chris, I have not got my coronavirus vaccine dose yet.
[306.72 → 307.52] I haven't either yet.
[307.74 → 308.28] I'm trying.
[308.44 → 308.78] I'm waiting.
[308.94 → 312.40] My parents just got their first dose.
[312.40 → 315.44] I imagine it'll be quite some time before I get my own.
[315.62 → 322.12] But in discussions about that and like health related applications of AI in our Slack channel,
[322.64 → 328.48] there have been a couple of people that have suggested that we talk at some point on the
[328.48 → 335.92] podcast about, hey, is it possible to apply AI to drug discovery or to like, you know, finding
[335.92 → 339.66] vaccines, or how does that cross into that world?
[339.66 → 346.12] Um, and, um, because we, we had those prompts from our listeners, um, we're really privileged
[346.12 → 352.68] today to have with us Dr. Abraham Heifetz, who is co-founder and CEO of Adam Wise.
[352.88 → 354.76] And this is exactly what they're doing.
[354.88 → 358.24] Um, so I'm really, really excited to hear more from Abraham.
[358.50 → 358.74] Welcome.
[359.46 → 359.92] Sounds good.
[360.56 → 361.58] Thanks for having me on the show.
[362.14 → 362.96] Yeah, definitely.
[362.96 → 367.94] Um, you want to give us just a little bit of a background about yourself and how you ended
[367.94 → 369.16] up where you're at now?
[369.84 → 370.32] Sure.
[370.46 → 371.16] I'd be happy to.
[371.52 → 375.92] Um, so my background is actually in computer science.
[376.26 → 382.12] Um, I, I did my undergrad, my master's at Cornell where, where I was focused on, on what
[382.12 → 384.96] today is called good old-fashioned AI.
[385.30 → 389.74] So symbolic type things, symbolic type things, graph search algorithms.
[389.74 → 393.56] For example, one of my big projects was world robotic soccer.
[393.84 → 398.96] So the, the Cornell Robocop team, 2000 champion world champions.
[399.36 → 405.76] And so this was, you know, you build little robots that play soccer on essentially a ping
[405.76 → 407.72] pong table, but totally autonomously.
[407.94 → 415.04] And the stated goal of that, you know, of that team is, is to beat the human, um, uh,
[415.04 → 417.68] world cup champions with humanoid robots by 2050.
[417.68 → 419.62] And so that was my background, right?
[419.68 → 424.56] Like, uh, you, you can hear that this is pretty AI and computation, but it wasn't a lot of
[424.56 → 425.12] drug discovery.
[425.80 → 425.88] Yeah.
[425.96 → 427.96] So is the doctor in front of your name?
[428.10 → 433.98] Is that doctor of, uh, like PhD in computer science or is that like medical doctor?
[434.36 → 436.50] It's doctor in PhD in computer science.
[436.52 → 436.76] Okay.
[436.88 → 437.08] Gotcha.
[437.22 → 438.56] Specifically in computational biology.
[439.18 → 443.88] So after Cornell, I went to work for IBM, uh, on what probably today we call a big
[443.88 → 444.28] data.
[444.28 → 447.94] I don't think we have the term, so we call it high performance data processing, much
[447.94 → 449.76] more IBM anyway.
[450.82 → 451.78] Lots of acronyms.
[452.14 → 452.68] Yeah, exactly.
[452.86 → 453.16] Exactly.
[453.54 → 458.56] And so this was in Boston while, while in Boston, I had this, I got interested in medicine.
[458.56 → 459.30] I thought it was interesting.
[459.40 → 463.62] So I started taking, you know, for fun, uh, organic chemistry courses kind of nights and
[463.62 → 464.18] weekends at Harvard.
[464.18 → 466.64] And I thought that that was really, really neat.
[466.74 → 472.34] And that there were these deep connections actually with how computers play chess is there's
[472.34 → 476.60] this deep connection with how chemists think about making molecules is, is, uh, you know,
[476.60 → 480.08] it ends up being in both cases, these tree search algorithms that you can apply.
[480.34 → 484.80] And so I went back for my PhD, um, and then, and I did my PhD at the university of Toronto,
[484.80 → 487.08] uh, now in computational biology.
[487.08 → 491.82] And so I had the good fortune to meet my co-founder, my, my eventual co-founder is Had
[491.82 → 492.18] VoIP.
[492.62 → 494.66] And his background was in protein analysis algorithms.
[494.76 → 498.80] He'd been working for a small pharma company doing protein analysis algorithms.
[499.58 → 502.96] And so you can see Adam wise and the technology became Adam wise.
[503.20 → 504.94] You put together three pieces.
[504.94 → 510.28] Um, my big data sets are protein analysis algorithms.
[510.68 → 516.40] And then we had the good fortune where literally across the hallway from us, Jeff Hinton's machine
[516.40 → 518.22] learning group was inventing modern machine learning.
[518.88 → 520.94] And so, so, you know, like we shared a copy of that.
[520.94 → 521.22] How fortunate.
[521.56 → 521.80] Yeah.
[521.98 → 522.22] Yeah.
[522.38 → 524.46] You know, talk about being at the right place at the right time.
[524.78 → 525.22] Yes.
[525.32 → 530.90] But we, we were able to see actually, you know, before Alex Net got published in these sort
[530.90 → 537.00] of hallway conversations, we kind of saw, uh, that, that machine learning was, was able
[537.00 → 539.94] to do things that, that it wasn't able to do before.
[540.20 → 546.06] And we figured out a way, uh, to apply that to the realm of biochemistry, the domain of biochemistry
[546.06 → 546.92] and drug discovery.
[547.28 → 551.22] Uh, and so that was the genesis of, of Adam Maquette.
[551.44 → 552.00] Awesome.
[553.56 → 555.36] Uh, Chris, I don't know about you.
[555.36 → 562.54] Um, but often my, my spare time doesn't involve, uh, taking medical and biology courses at
[562.54 → 562.84] Harvard.
[563.38 → 565.98] Um, everybody needs a hobby.
[566.26 → 566.76] Yeah.
[566.78 → 568.34] Everybody needs a hobby, I guess.
[568.44 → 570.58] You know, this is eerily familiar.
[570.58 → 577.60] I have a very good friend who is very similar in that way, both a deep learning person and
[577.60 → 580.64] a chemistry, a Harvard PhD in chemistry.
[580.72 → 582.68] And he crosses that chasm as well.
[582.68 → 587.12] So I'll need to introduce the two of you all because you all, you're, you're sounding frightening
[587.12 → 589.64] like him, and I've never met anyone like either one of you before.
[589.64 → 593.62] So there, there, there's one other person that you can talk about this with, and they'll
[593.62 → 594.94] actually understand the whole thing.
[595.18 → 596.16] So it's interesting.
[596.30 → 596.94] It's interesting.
[597.02 → 601.52] I said, like, I'll, I'll, I'll tell you about the we might end up cutting this out of the
[601.52 → 605.82] show, but I'll, I'll tell you about the connection there between the good old-fashioned
[605.82 → 606.08] AI.
[606.40 → 611.76] It's not about Adam wise, but it's, there is a connection between the good old-fashioned AI and how
[611.76 → 612.48] chemists think.
[612.92 → 613.20] Okay.
[613.32 → 614.00] Let's hear it.
[614.10 → 615.92] That's totally going to be in the show.
[616.04 → 616.28] Okay.
[616.32 → 617.26] So here's the problem.
[617.26 → 622.82] So standard problem in organic chemistry, you know, tests and homework, let alone what
[622.82 → 624.72] they do is here's a molecule.
[624.84 → 625.54] I'll show you a molecule.
[626.02 → 631.76] And you come up with basically a recipe to construct it out of simple commercially available
[631.76 → 632.24] pieces.
[633.04 → 636.66] And the thing you need to understand about, about the chemists is that they think the world
[636.66 → 637.50] is made out of Legos.
[637.50 → 641.22] So they'll take that molecule and say, okay, well, I don't have that molecule, but you
[641.22 → 644.32] know if I broke it into these two simpler pieces, I know a reaction that would stick
[644.32 → 645.12] those two pieces together.
[645.94 → 649.16] Or alternatively, you know, if I, if I broke it apart a different way, then I'd have two,
[649.26 → 650.00] two different pieces.
[650.20 → 651.58] And now it can stick those together.
[651.84 → 652.16] Right.
[652.18 → 653.00] With a different reaction.
[653.70 → 656.08] And so now you've, you've got kind of the same problem.
[656.08 → 659.96] And so in, in our parlance here, we would say we recourse, right?
[660.00 → 663.38] And so for each of those simpler pieces, you apply the same algorithm, you break it apart
[663.38 → 664.54] and you break it apart, and you break it apart.
[664.72 → 669.22] And you get this essentially expanding tree of synthetic possibilities where out of simpler
[669.22 → 672.06] and simple pieces, you can, you know how to put each piece together.
[672.42 → 677.74] And so this is called by the chemists retro synthetic analysis, retro because backwards,
[677.92 → 678.78] working backwards from the goal.
[679.86 → 684.70] It was actually the topic of the 1990 Nobel Prize, which was given to EJ Corey at Harvard,
[684.70 → 687.78] was for elucidating this, this idea of retro synthetic analysis.
[688.50 → 690.30] So does that go all the way back down?
[690.38 → 694.02] Like, I assume if you take that all the way back down, you sort of end up with the
[694.02 → 697.06] elemental makeup of, of our universe.
[697.52 → 699.20] I mean, how far does that go down?
[699.56 → 701.86] Practically, it goes until you can buy them out of a catalogue.
[702.12 → 703.10] Okay, right, right.
[703.16 → 703.36] Okay.
[703.38 → 703.88] That makes sense.
[703.88 → 706.96] But even here, you see that you need computer tools, right?
[707.02 → 712.10] Because there's like, you know, I think at the time I was working on it, 14 billion compound,
[712.28 → 714.46] 14 million compounds, you could buy out of a catalogue.
[714.70 → 718.92] Today, there's, there's 16 billion compounds you can buy out of a catalogue.
[719.30 → 722.02] And I don't know about you, but there are some mornings where I can barely remember,
[722.14 → 722.98] you know, 12 billion.
[723.94 → 724.86] That's most mornings.
[725.06 → 725.30] Yeah.
[725.42 → 725.58] Yeah.
[725.66 → 725.86] Right.
[725.92 → 727.44] Like, that's why you have to have coffee.
[727.72 → 731.04] So, so my point is that like, you need computer tools to do this stuff, right?
[731.04 → 733.02] Like you, you can't do it all in your head anymore.
[733.48 → 735.52] And so your audience can appreciate that.
[736.04 → 739.48] We would talk about this as, you know, backwards chaining reasoning, right?
[739.48 → 740.84] Or, or heuristic tree search.
[740.84 → 745.02] And it's kind of like when a computer plays chess, it looks at the board and sees every
[745.02 → 745.88] move that it can make.
[745.90 → 747.40] And then thinks about every move you can make.
[747.42 → 748.92] And then thinks about every move it can make in response.
[749.32 → 751.94] And so sort of similarly, you get this expanding tree of possibilities.
[752.18 → 755.24] And now it's plotting a course from the current board until checkmate.
[755.64 → 758.40] And that's kind of what the chemist is doing, plotting the course from the molecule you want
[758.40 → 760.26] to these commercially available molecules.
[760.26 → 762.64] And so those links are actually very deep.
[762.88 → 768.06] And so that was what I, you know, went back to get my, my PhD to build that system.
[768.62 → 772.56] Is that assuming like, you know, the compound that you want to start with, right?
[772.60 → 776.20] The problem is how you actually, how you actually get there.
[776.68 → 777.08] Exactly.
[777.46 → 777.76] Exactly.
[777.88 → 781.98] So, so this is the interface, you know, maybe between the work with Atom wise and the work
[781.98 → 783.00] that I was doing in my doctorate.
[783.26 → 785.70] For the doctorate was, you found the answer.
[785.80 → 787.64] Now you want to know how to make it, right?
[787.64 → 792.16] So there's one molecule and the question is what's the recipe to make it, to construct
[792.16 → 792.38] it.
[792.74 → 796.18] But there's this whole problem, which is, okay, there are billions of molecules you could
[796.18 → 796.54] make.
[797.32 → 799.60] Which one is the best one to make, right?
[799.60 → 803.40] It's, it's sort of the initial, the pre problem for what I was just talking about.
[803.78 → 806.36] And so that's the problem that we're focused on Atom wise is how do you make a molecule,
[806.36 → 809.62] which is going to be safe and effective as a medicine?
[809.88 → 810.48] That's the problem.
[810.96 → 817.60] So before we get into sort of how you're doing that, how traditionally is that done sort of,
[817.64 → 821.56] of absent AI driven drug discovery?
[821.82 → 827.20] How has that been done in the past, maybe with computer methods, but also without them?
[827.58 → 827.70] Sure.
[827.86 → 828.04] Yeah.
[828.12 → 832.16] And people have been trying to apply computers to medicine and drug discovery for decades.
[832.36 → 835.70] I mean, it's, these are good ideas, but they're not new ideas.
[835.70 → 842.00] It's just that, you know, I think, I think we all see that the power of machine learning
[842.00 → 846.76] computation today lets us do things that weren't possible a few decades ago.
[846.76 → 847.06] Right.
[847.06 → 851.46] So, so that's where the excitement comes from, but I'll tell you the answer to your question
[851.46 → 856.14] about, about what's the, you know, still common approach today.
[856.70 → 858.72] It's really doing these experiments physically.
[858.72 → 862.60] Um, and, and relying a lot on human intuition.
[863.24 → 866.14] Those I would say are, are the baseline tools today.
[866.22 → 867.78] And kind of, if you think about it, right?
[867.78 → 870.30] Like think about that, because that is an incredible claim.
[870.40 → 875.26] If you think about every major industry on the planet, right.
[875.32 → 879.18] And I, and I don't care if you're talking about, you know, Lockheed Martin, one of my,
[879.36 → 882.50] my second job in high school actually was working for Lockheed Martin missiles and space.
[882.64 → 882.94] Okay.
[882.94 → 888.54] But if you're talking about, you know, Lockheed Martin and designing a new wing, you will test
[888.54 → 891.84] a thousand wing designs before you ever build the prototype.
[892.38 → 896.98] Now you still, you still take that prototype to the wind tunnel, right?
[896.98 → 897.98] You still do a test flight.
[898.54 → 900.52] I hope before I ever get near the plane, right?
[900.56 → 905.64] Like, but you do most, maybe 99% of the experiments computationally rather than physically, right?
[905.64 → 908.52] Because you want those, those are hard and laborious and finicky.
[908.76 → 911.46] And so you want those experiments to work, right?
[911.46 → 915.16] And you'd rather run one test, which succeeds rather than thousands and thousands, which
[915.16 → 915.40] fail.
[915.82 → 917.72] And so, so there, right.
[917.78 → 919.80] Most of the experiments are in the computer.
[920.28 → 922.36] I'm right now in San Francisco, right?
[922.40 → 926.40] So out here in California, you know, I've got a pretty good guess that this building will
[926.40 → 927.16] stand up an earthquake.
[927.92 → 931.98] That is an inordinately expensive experiment to run physically, right?
[932.04 → 937.56] And so, so we rely on structural engineers doing computational simulation to give us the certainty
[937.56 → 939.26] that, that we should move into the building.
[939.26 → 943.54] So every major industry, actually, most of the experiments are done computationally, but
[943.54 → 947.38] pharma still, the baseline is to run those experiments physically.
[948.04 → 949.00] And so that's what we're trying to do.
[949.06 → 953.96] We're trying to give the same efficiency of every major industry to the drug discovery
[953.96 → 954.22] industry.
[954.22 → 971.44] Hey friends, this episode of practical AI is brought to you by Modish, a podcast from
[971.44 → 976.06] the team at Heroku that explores code technology, tools, tips, and developer life.
[976.14 → 978.72] There are tons of great conversations on the Modish podcast.
[978.72 → 981.32] So I would encourage you to check it out and subscribe.
[981.32 → 987.14] But in particular, I wanted to bring to your attention two episodes, episode 98 and 99,
[987.46 → 991.60] where Julien Tuque explores the ethical and technical sides of deep fakes.
[991.94 → 997.10] The rise of manipulated pictures and videos and other forms of computer generated media are
[997.10 → 1000.62] able to cause uncertainty and doubt in what we see and hear online.
[1000.62 → 1004.80] And so how are we able to use these tools for good, if at all?
[1005.10 → 1005.84] Here's a sneak peek.
[1006.22 → 1012.30] Let's say we want to do a deep fake of my voice, and we train the model, and we have enough
[1012.30 → 1013.24] data and everything.
[1014.34 → 1022.68] This will be also able to imitate my accent, for example, like how I pronounce English and
[1022.68 → 1024.74] the strong pieces of my accent.
[1024.74 → 1028.26] It really depends.
[1028.26 → 1034.06] If there would be a person with similar accent on the input, then it would be fine.
[1034.20 → 1035.44] But it's kind of cheating.
[1035.86 → 1040.26] You can think it's cheating because we're reusing accent of a different person that's similar
[1040.26 → 1040.96] to your accent.
[1041.32 → 1048.58] But if it would be like an American native speaker or a British person with a British accent or
[1048.58 → 1055.10] like whatever other accent, then it will kind of be a mixture on the output.
[1055.80 → 1059.24] So we're not there yet in terms of converting accents.
[1059.96 → 1064.40] It's a little bit more difficult than we initially anticipated because like when we started the
[1064.40 → 1068.68] company, we thought it would be, you know, we'll kind of solve it in a year or something.
[1068.80 → 1073.14] But then it turned out that, oh, no, we're here for much longer.
[1074.26 → 1075.70] Check these episodes out.
[1075.70 → 1081.60] Links are in the show notes to both episodes or head to heroku.com slash podcasts to listen
[1081.60 → 1082.30] and subscribe.
[1082.82 → 1087.32] Again, check the show notes for links or go to heroku.com slash podcasts.
[1087.32 → 1107.36] So as you arrived at that point where you were fortunate enough to be across the hallway
[1107.36 → 1113.94] from Dr. Hinton and his team, and you started applying such techniques, deep learning as we're
[1113.94 → 1120.00] calling it now, to this, what specifically could you tell us a little bit about, you know,
[1120.04 → 1126.26] how you got into using these new technologies of the day and how that changed your workflow
[1126.26 → 1130.74] at the time, you know, as you were getting started and as you took that turn with what we're now
[1130.74 → 1133.10] calling AI or deep learning at this point?
[1133.58 → 1133.92] Absolutely.
[1134.10 → 1134.26] Yeah.
[1134.26 → 1140.16] Let me draw the connection for you between what maybe is more common image recognition,
[1140.30 → 1142.38] speech recognition, and what we're doing.
[1142.96 → 1144.24] And here's the way I'll do it, actually.
[1144.38 → 1150.96] I'll let me talk about the history of computer approaches to chemistry prediction.
[1151.44 → 1153.72] Like I said, this isn't a new idea.
[1153.82 → 1156.54] People have been trying this for decades, maybe 1970s.
[1156.54 → 1160.62] Basically, as soon as we got high quality, what's called x-ray crystal structures.
[1160.94 → 1165.84] So 3D structures of proteins, which machine learning made a big breakthrough recently.
[1166.46 → 1171.72] And the Case organizers, Case protein organizers said that alpha-bolt 2 solved the problem, right?
[1171.78 → 1176.22] So there's huge progress in AI in just getting the shape of the protein.
[1176.82 → 1183.20] But let me talk about people have been, experimentally, were able to get structures since the 1970s.
[1183.20 → 1187.86] And people basically tried to use computers as soon as they could to work on those.
[1188.14 → 1189.68] And so the first generation was the physicists.
[1190.22 → 1193.32] And the physicists came in, and they said, what's the problem, right?
[1193.34 → 1196.92] Like I can compute Van der Waals dispersion.
[1196.98 → 1198.22] I can compute colonic charges.
[1198.34 → 1199.32] The cows are spherical.
[1199.50 → 1201.08] How is this even a problem, right?
[1201.20 → 1202.20] Like in the way-
[1202.20 → 1203.84] Sounds like a typical physics approach.
[1204.28 → 1204.60] Exactly.
[1204.98 → 1207.86] Whatever you're doing is applied physics.
[1207.86 → 1209.64] So I don't see why this is a problem.
[1210.12 → 1210.46] Exactly.
[1210.62 → 1210.94] Exactly.
[1210.94 → 1216.14] I think, you know, in the show notes, maybe you should put that XKCD about the physicists.
[1216.38 → 1216.42] Right.
[1216.88 → 1218.78] So my dad's a physicist.
[1218.98 → 1221.30] So I like ragging a little bit on the physicists.
[1221.80 → 1223.40] So exactly right.
[1224.56 → 1229.10] And it turns out actually that if you do full quantum mechanical simulation, you get the right answer.
[1229.48 → 1232.96] Which frankly, I find comforting that physics got it right.
[1233.36 → 1233.86] That's nice.
[1234.12 → 1239.38] But full quantum mechanical simulation doesn't scale, right?
[1239.38 → 1241.32] It's incredibly computationally taxing.
[1241.66 → 1242.78] And so you get the right answer for it.
[1242.82 → 1252.46] Like lithium hydride, you know, very, very simple inorganic molecules and doesn't scale to the thousands of electrons, which might be in a biological system.
[1252.94 → 1253.06] Yeah.
[1253.24 → 1254.98] This was the whole thing with my PhD.
[1255.12 → 1259.84] I studied density functional theory, which is you, you probably run across that.
[1259.84 → 1265.24] And yeah, for anyone that's interested in that, you can Google that, and we won't talk about it here.
[1265.38 → 1267.90] But yeah, I'm totally eating up everything you're saying.
[1268.26 → 1268.78] Okay, great.
[1270.06 → 1271.30] So you know better than me.
[1271.40 → 1275.86] I mean, like, you know better than me, both the strengths and the challenges in the approach.
[1275.86 → 1280.94] So then roughly speaking, here's what I'd say is kind of the next generation came through, and it wasn't physicists.
[1281.14 → 1282.24] It was chemists.
[1282.68 → 1285.54] And the chemists said, okay, I don't just know physics.
[1285.54 → 1286.62] I also know a little bit of chemistry.
[1286.74 → 1292.24] I know that there are features that in my experience correlate with binding, right?
[1292.32 → 1293.92] So hydrogen bonds, right?
[1293.96 → 1298.14] Like I believe hydrogen bonding is important for a medicine to hit a protein and inhibit it.
[1298.14 → 1307.48] So actually, it occurs to me, maybe I should take a step back for the folks who explain how medicine works for a second.
[1307.66 → 1308.58] No, that's a great idea.
[1309.04 → 1309.88] Give the context.
[1310.34 → 1310.50] Okay.
[1310.62 → 1311.72] So here's the context.
[1312.44 → 1316.10] Here's like the 90-second crash course in biology.
[1316.82 → 1317.28] I like it.
[1317.58 → 1318.10] That's all I need.
[1318.10 → 1318.26] I do too.
[1318.66 → 1320.18] That's a big promise right there.
[1321.72 → 1325.30] So think about the proteins in your body as machines on an assembly line.
[1325.30 → 1325.74] Okay.
[1326.74 → 1333.90] In that every machine takes in a very specific input, transforms it in a specific way, hands it off to the next machine, you know, on down the line.
[1334.00 → 1339.40] And so out of the coffee you're drinking, the food you're eating, your body breaks that down and then builds more you.
[1340.22 → 1340.44] Okay.
[1341.24 → 1347.84] And so on of the ways that disease happens is when those machines break or when they go haywire.
[1347.84 → 1357.64] And so imagine, for example, the machine that governs cell growth, cell division, switches on, and it never switches off.
[1358.50 → 1358.88] Okay.
[1358.90 → 1361.78] So that means that that cell will keep growing and dividing, growing and dividing.
[1362.42 → 1363.12] That's a tumour.
[1363.24 → 1363.72] That's cancer.
[1364.44 → 1364.54] Yeah.
[1364.54 → 1376.76] If you were wandering, you know, a factory floor, and you saw a machine that was going haywire, you might throw in a monkey wrench so that the machine, instead of doing whatever it's normally doing, is just busy chomping on that monkey wrench.
[1376.80 → 1378.80] And you've essentially turned off that runaway machine.
[1379.48 → 1379.88] Okay.
[1379.88 → 1381.52] Just by physically blocking it up.
[1382.28 → 1382.40] Right.
[1382.40 → 1392.90] It turns out actually that that's how most of our medicine works today is if you make a molecule, and it just physically slots into a protein, and it shuts down that protein.
[1393.62 → 1396.60] And so you arrest the disease process.
[1397.28 → 1398.88] Or it connects to the receptor, right?
[1398.96 → 1401.10] So that the whatever else cannot connect.
[1401.38 → 1401.78] That's right.
[1401.84 → 1402.96] So it connects to the receptor.
[1403.06 → 1407.04] And so you disrupt signalling, or it blocks up an enzyme.
[1407.14 → 1409.56] So the enzyme doesn't catalyze the reaction that it should catalyze.
[1409.66 → 1410.38] Exactly right.
[1410.38 → 1422.42] And so I know that this sounds pretty abstract, but if you Google something like the Philadelphia chromosome, you will see that there is just a mutation which switches on cell growth and cell division and does switch off.
[1422.48 → 1426.14] And this is a very clear link in cancer, exactly what we talked about.
[1426.62 → 1434.64] And so this means that people were able to design the first cancer-specific drug to block exactly that mutated protein.
[1435.08 → 1436.38] So what does a drug need to do?
[1436.58 → 1438.08] Now, imagine you've got a monkey wrench, right?
[1438.08 → 1439.80] You want it basically to do two things.
[1439.80 → 1444.06] You want it to stick really well to the disease protein, right?
[1444.10 → 1448.40] You want it to bind to the disease protein to shut it down as completely as possible.
[1448.98 → 1455.40] You also want it to bounce off the proteins in your liver and your kidneys and your heart and your brain that you want to keep functioning, right?
[1455.40 → 1459.34] Because you don't want to turn off 100 different proteins on that factory and cause all the nerve side effects.
[1459.72 → 1463.62] And so basically you can phrase this as it's got to stick to what you want it to stick to.
[1463.84 → 1464.88] It's got to not stick.
[1464.88 → 1468.54] It's got to bounce off what you don't want it to stick to, right?
[1468.54 → 1470.96] And that's talking about both efficacy and safety.
[1471.76 → 1472.12] Okay.
[1472.36 → 1472.60] Okay.
[1473.12 → 1475.72] And so that's a core piece of doing drug to block.
[1475.88 → 1477.30] Now, there are other things in there, right?
[1477.30 → 1479.48] Like you want to make sure that it's soluble, right?
[1479.48 → 1486.68] In water so that like when you drink it, it actually gets into your bloodstream, that it doesn't get metabolized right away by your liver or your kidneys.
[1486.68 → 1488.82] And so it hangs out long enough to reach the protein.
[1489.06 → 1493.96] I mean, there are other factors in there, but basically like a core piece of what you want is does it stick?
[1494.56 → 1495.52] Does it not stick?
[1496.20 → 1505.28] And today that is answered by setting up an experiment physically, which as you can imagine is difficult, laborious, finicky, expensive, time-consuming, and all those problems.
[1505.84 → 1509.10] Instead, we phrase that as a binary classification problem.
[1509.10 → 1515.62] And so we're the first team to use convolutional neural networks where you set up and run that as a prediction problem.
[1516.44 → 1521.68] And so an image is a 2D grid of pixels and every grid has red and green and blue colour channels.
[1522.08 → 1523.36] Well, proteins are 3D.
[1523.54 → 1524.62] So we set up a 3D grid.
[1525.14 → 1530.34] Instead of red and green and blue colour channels, we have oxygen, sulphur, nitrogen, carbon colour channels.
[1530.34 → 1546.66] As soon as you do that in coding, then you can essentially adapt all the algorithms that people have used for image recognition, change them to the 3D biochemistry domain, and get them to predict binding.
[1547.64 → 1548.10] Does that make sense?
[1548.76 → 1549.40] Very cool.
[1550.04 → 1550.66] Yeah, it does.
[1551.24 → 1551.72] It does.
[1551.72 → 1555.58] So how early in your process did you move to this?
[1555.62 → 1561.76] Because, I mean, certainly as Hinton was setting, you know, we weren't quite to the mature convolutional neural networks that we have today.
[1562.26 → 1572.02] You know, how did that progression look as you started to turn to the technology and then you kind of arrived at this utilization of convolutional in its present?
[1572.52 → 1574.54] You know, how did that look along the way?
[1574.62 → 1576.44] How did you make the steps?
[1576.58 → 1579.00] And what did that reflect on what you were able to produce?
[1579.50 → 1579.84] Absolutely.
[1579.84 → 1589.58] So Alex Net, if you remember, in the dark proto-history of modern machine learning, that all the way back in 2012, that was published, I think, in December 2012.
[1590.32 → 1594.00] And we had our first convolutional neural network running in January 2013.
[1594.34 → 1594.72] Oh, wow.
[1594.86 → 1598.20] But that's because we had been talking to folks, right, like before things were published.
[1598.42 → 1601.66] That's the question about being at U of T, being on that same hallway.
[1602.44 → 1602.64] Yeah.
[1602.86 → 1603.06] Yeah.
[1603.64 → 1604.64] It was pretty early on.
[1604.64 → 1612.84] And then we published and these have become popular, popular tools in the drug discovery, the chem informatics, drug discovery, AI realm.
[1613.38 → 1614.98] You know, that's the beginning of the story, right?
[1615.02 → 1618.66] Like there are many things you got to do to make these things practical and successful.
[1618.66 → 1620.08] Yeah, I'm curious.
[1620.22 → 1629.80] So part of it is figuring out how to encode the information that you want in a way that you can utilize it in, say, a convolutional neural net.
[1629.80 → 1631.86] So that's the encoding piece.
[1631.98 → 1636.88] But I'm also thinking about the sort of data labelling piece.
[1637.02 → 1639.68] Like you're saying, you're trying to predict binding or not.
[1639.88 → 1651.90] How clearly is that defined in terms of actually getting a data set that will, you know, tell you about, you know, all of these different molecules and whether they do or don't bind?
[1652.14 → 1655.56] What does it look like to put together that data set, I guess, is what I'm asking.
[1655.56 → 1660.48] Absolutely. You struck on something that's absolutely critical, right, which is the quality of the data.
[1660.96 → 1667.58] In some sense, if you're an academic machine learning researcher, you get to just care about MOIST and ImageNet and CIGAR.
[1668.06 → 1671.60] And in some sense, you don't even care if those are labelled correctly or incorrectly.
[1671.78 → 1676.16] Like you now have ground truth data, and you can ignore whether they were accurate or inaccurate.
[1676.52 → 1683.70] And I think people have like there are still mislabelled things in ImageNet and totally ambiguous things in MOIST.
[1683.92 → 1685.20] But who cares, right?
[1685.20 → 1689.26] Like it's really how well do you overfit to those three data sets?
[1689.26 → 1689.62] It's the standard now.
[1689.90 → 1690.86] It's the standard. Exactly.
[1691.34 → 1692.78] And there's value in having the standard.
[1693.34 → 1698.48] But, you know, our bug, the bug we're trying to close is have we ever helped a patient?
[1699.82 → 1701.46] Right. Like have, we ever cured a disease?
[1702.36 → 1704.28] It doesn't matter whether you're doing well on a benchmark.
[1704.40 → 1706.84] It matters whether you're having practical, pragmatic outcomes.
[1706.84 → 1721.12] Right. So anyway, if any of your listeners, you know, don't want to improve click-through rates on ads or don't want to improve performance on a benchmark, but hold themselves to that standard of whether they're helping humanity.
[1721.52 → 1724.60] Boy, like we've got more than enough machine learning problems to work on.
[1724.60 → 1727.94] So to get to your question about data quality, I want to talk to two pieces of it.
[1728.20 → 1729.42] Input data and output data.
[1729.78 → 1732.92] How do you tell if you can trust the input data?
[1733.48 → 1737.74] How do you tell whether your system is predicting anything worth paying attention to?
[1738.40 → 1741.04] On the input data, there's a huge amount of data out there.
[1741.22 → 1741.86] Huge amount of data.
[1741.86 → 1745.38] So the National Institutes of Health, the NIH, has a database called PubChem.
[1745.80 → 1753.02] And the last time I checked, there was something like 240 million label data points of the kind that we use in there about protein and small molecule binding.
[1754.28 → 1757.04] Ninety eight percent of which fails our quality control filters.
[1758.40 → 1760.78] OK, so there's a huge amount of data and there's a huge amount of noise.
[1760.86 → 1761.72] Let me give you one example.
[1762.18 → 1763.72] There are lots of examples, but let me give you one.
[1764.10 → 1769.24] You'll see in these databases, you know, a protein and a molecule and a measurement of binding.
[1769.24 → 1774.10] You have 3.14159 nanomole, which is a measure of binding.
[1774.48 → 1779.30] And then you'll see the same protein and the same molecule and the same 3.14159.
[1779.54 → 1780.68] But now it's millimole.
[1780.96 → 1783.90] OK, and so the only part here which is important is the NATO versus mill.
[1784.44 → 1790.30] Your people following along at home can see that you have exactly the same number, but it's off by a factor of a million times from each other.
[1790.98 → 1794.24] And you look at this, and you say, this can't possibly be two different assays.
[1795.06 → 1795.92] What happened here?
[1795.92 → 1803.34] Right. And if you dig into this, what you find is that somebody was citing their earlier work, and they copied an entry out of their previous paper.
[1803.94 → 1807.34] And the letters N and the letter M are next to each other on the keyboard.
[1807.50 → 1808.86] And so they fat-fingered.
[1808.94 → 1809.56] There's a typo.
[1809.90 → 1812.82] And you ended up with off by a factor of a million.
[1813.04 → 1816.10] I can't tell you in which direction, but I can tell you just a million.
[1816.46 → 1816.92] Just a million.
[1816.92 → 1825.88] And it's only when the poor schmuck of a medicinal chemist is trying to use your prediction, your prediction, what a neural network was going to learn or any machine learning, it's going to learn the average of these two.
[1826.26 → 1831.24] And so you're off by half a million, which you only discover when the poor schmuck of a medicinal chemist is sitting there trying to do the physical experiment.
[1832.04 → 1834.52] And so you have to do huge amounts of data cleaning.
[1834.52 → 1837.92] And it's not good enough just to do random cross validation.
[1838.72 → 1845.74] Right. You know, fivefold cross validation, because you have to really appreciate where these error sources come from, how you got the data.
[1846.30 → 1859.12] And that's even before you talk about things like there are molecules which interfere with the assay, which aggregate up, which fall out of solution, which is I put sulphuric acid in a test tube, boy, it'll look like it's a great, great drug.
[1859.16 → 1861.12] But it's not for the reasons you care about.
[1861.42 → 1864.16] You know, and so you have to be able to clean, clean, clean a lot of that data.
[1864.16 → 1873.20] And so on of the things we've had to do is we've had to put the machine learning practitioner in the same room as the medicinal chemist, in the same room as the structural biologist, in the same room as the software engineer.
[1873.50 → 1877.06] Right. Because these things have to run at massive scale with incredible accuracy.
[1877.62 → 1880.26] And so we put a huge amount of effort into the data cleaning.
[1880.80 → 1883.72] And that's just on the input data. Right. There's the output data side as well.
[1883.78 → 1885.36] How do you tell whether any of this stuff is working?
[1885.44 → 1889.96] How do you catch the wrong and, you know, in half a million in either direction problem?
[1889.96 → 1898.48] Yeah. And is that part of just like monitoring and, you know, trying to gain some intuition about what you're looking for?
[1898.56 → 1900.58] Or, you know, how do you go about that?
[1900.58 → 1906.24] So that's the core question, right, is how do you convince yourself even before you convince anybody else?
[1906.68 → 1910.12] Right. But how do you convince yourself that you're making progress and that this is working?
[1910.66 → 1919.90] Actually, if you look up my name, the last paper that I wrote was a paper basically looking at every benchmark that we could get our hands on.
[1919.90 → 1922.74] We looked at every one of the standard benchmarks in our field.
[1923.62 → 1929.04] We looked, and basically we found that there was this problem of data redundancy.
[1929.36 → 1932.32] How to explain? Here's the kind of conversation I was having with people.
[1932.80 → 1936.70] People would come to me, and they'd say, hey, I've got a machine learning system.
[1937.24 → 1940.14] I can predict yesterday's stock price to within a dollar.
[1941.08 → 1942.72] Give me your life savings. We're going to be rich.
[1943.94 → 1947.14] And you'd hear that, and you'd say, OK, well, it's good that you can predict yesterday's stock price.
[1947.14 → 1950.48] That's that's something. Have you ever predicted tomorrow's stock price?
[1951.00 → 1953.34] And they'd say, OK, tough customer.
[1953.62 → 1956.28] And they go in, they come back and they'd say, OK.
[1957.50 → 1959.90] Now we can predict yesterday's stock price to within a dime.
[1960.80 → 1966.40] Give me your life savings. Lets you know, we're going to be rich and say, OK, well, that that doesn't really answer my question.
[1966.48 → 1967.76] Have you predicted tomorrow's?
[1968.50 → 1973.48] And they'd say, I can tell you're you're you know, you're an expert.
[1973.48 → 1978.14] Right. And they go in, they come back, and they say, now we can predict yesterday's stock price to within a penny.
[1979.10 → 1980.34] What more can you want?
[1981.16 → 1987.96] And basically, you look at that, and you say, I have less confidence now than I did at the beginning, because now you've convinced me that you're overfitting to the data.
[1988.08 → 1992.40] Right. Like you're you're modelling the noise, you're overfitting the data, and you've never done the killer test.
[1992.40 → 1994.54] Right. Like about whether you can do a prospective test.
[1994.98 → 1999.72] And so sort of similarly, similarly in our space, you see a ton of papers.
[1999.72 → 2007.08] Basically, the history is there's a ton of papers where someone has a shiny new wisdom system, and then they report results on a protein.
[2008.18 → 2016.24] And you never know if that means does it work on that one protein or does it work on every protein or does it work on that one class of protein?
[2016.24 → 2024.28] What does it mean? Right. Like or you show two or three results, and it's its super, super challenging to really understand what the limits are or what you what it means.
[2024.28 → 2030.70] And so people set up benchmarks kind of like MOIST and CIGAR and ImageNet to try to answer this.
[2030.98 → 2038.36] But basically, my borrower and I, the last paper that we wrote, we looked at every benchmark, and we found that there were these redundancies where basically you're teaching to the test.
[2038.44 → 2040.10] You were memorizing yesterday's stock price.
[2040.10 → 2046.68] And we showed that the more of it, we came up with a mathematical definition for data redundancy between the training and the test set.
[2047.06 → 2051.38] And we basically showed that the more redundancy there was, the better machine learning algorithms look like they do.
[2051.72 → 2058.64] And this was true for every benchmark we looked at, for every machine learning algorithm we looked at, for every feature set we looked at, for every training test split we looked at.
[2058.82 → 2060.42] It's just an incredibly robust set of results.
[2060.42 → 2069.12] And so my personal conclusion is that most of the history of computational chemistry in this sort of corner of it is having been rewarding, overfitting and teaching to the test.
[2069.12 → 2074.92] Instead of rewarding real perspective, can you predict tomorrow rather than can you predict yesterday?
[2075.26 → 2076.40] Sort of depressing result.
[2077.26 → 2082.44] And so what we said to ourselves was, OK, we're just going to have to show that this works on 100 different proteins.
[2082.60 → 2084.86] It works on different diseases.
[2084.86 → 2088.00] It works in different labs hands just so it's a robust result.
[2088.00 → 2090.70] You know, like, you know, people are hiring, right?
[2090.72 → 2094.78] Like you can get a job selling ads if you're a machine learning person.
[2095.02 → 2097.40] Like, so does this matter?
[2097.48 → 2098.38] You know, are we making progress?
[2098.38 → 2102.46] And so what we did was we launched, you know, we're not expert in 100 different proteins.
[2102.74 → 2103.66] You know, I'm a computer scientist.
[2103.78 → 2104.76] I'm not an expert in any protein.
[2105.88 → 2108.52] And so we decided we were going to have to partner with people who were.
[2108.96 → 2110.54] And nobody's an expert in 100 different proteins.
[2110.78 → 2114.48] So we launched a wide set of collaborations with academics.
[2114.48 → 2129.56] And what we did was imagine you're a professor, and you believe protein XYZ, if you block protein XYZ, that would cure cancer or, you know, a certain type of cancer or Alzheimer's or COVID.
[2129.56 → 2133.06] You tell us you want molecules for protein XYZ.
[2133.16 → 2135.12] We go screen commercially available molecules.
[2135.34 → 2137.04] We buy the best molecules out there.
[2137.10 → 2140.16] We get them formatted, plated, you know, ready to go into your assay.
[2140.22 → 2141.70] We ship you physical molecules.
[2142.26 → 2144.88] You run the experiment, and you tell us whether we were right or not.
[2144.88 → 2161.90] We deserve a better internet.
[2162.12 → 2165.08] And the brave team has the recipe for bringing it to us.
[2165.24 → 2166.22] Start with Google Chrome.
[2166.46 → 2170.16] Keep the extensions, the dev tools, and the rendering engine that make Chrome great.
[2170.36 → 2171.24] Rip out the Google bits.
[2171.36 → 2172.00] We don't need them.
[2172.00 → 2174.90] Mix in ad and tracker blocking by default.
[2175.18 → 2177.86] Quick access to the Tor network for true private browsing.
[2178.24 → 2182.56] And an opt-in reward system so you can get paid to view privacy respecting ads.
[2182.78 → 2186.50] Then turn around and use those rewards to support your favourite web creators like us.
[2186.84 → 2191.44] Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[2191.44 → 2209.54] So now that you've kind of taken us through how you got there and how all this stuff is kind of how you think about it and how it works,
[2210.04 → 2214.78] could you pick kind of a use case of maybe a specific disease that you guys have worked on?
[2214.78 → 2217.70] And kind of like how do you apply that?
[2217.84 → 2229.50] Maybe tell us about a story where you're doing this, and you got some level of the success of doing the process as well as some of the challenges that you hit along the way just to make the whole thing real and give something very tangible.
[2230.46 → 2230.90] Sure.
[2231.06 → 2231.94] I'd be happy to.
[2232.10 → 2232.26] Sure.
[2232.26 → 2240.62] So in this setup where you're a professor, and you're sending us compounds, let me give you the sort of the stats on the program overall, and then I'll give you an example.
[2240.98 → 2241.46] Sounds great.
[2241.64 → 2246.14] So we set up this set of application, this program.
[2246.24 → 2251.32] We set up this program called the Artificial Intelligence Molecular Screen or our AIMS program.
[2252.32 → 2254.00] And it's been hugely successful, actually.
[2254.32 → 2261.36] We've had over 1,600 applications from more than 250 universities and research hospitals in 50 countries.
[2261.36 → 2268.94] We've accepted more than 775 programs, projects covering 600 unique proteins.
[2269.66 → 2275.78] And that, I mean, for context, like a big pharma company might have like 60 small molecule projects.
[2275.88 → 2279.40] And so we have 600 unique protein targets here.
[2279.40 → 2287.70] And so this is really operating on a massive scale covering every major therapeutic area, cancer and neurodegeneration and infectious disease in there.
[2287.70 → 2291.86] And so we have data back now for like more than 150 of these projects.
[2292.32 → 2296.50] And so we can really give very statistically sound results about how well we're doing.
[2296.80 → 2302.74] When I present this at like chemistry conferences, I usually stop, and I ask the audience like, okay, you've seen the setup.
[2303.34 → 2304.10] What success rate?
[2304.18 → 2307.12] Think about your favourite screening technology in your mind.
[2307.12 → 2312.56] And maybe that's a computational approach or maybe that's a physical approach, or maybe it's just throwing darts at a catalogue, right?
[2312.60 → 2314.06] Like whatever you think is the best way.
[2315.32 → 2316.74] What do you think the success rate is?
[2316.92 → 2319.68] And the answer I most frequently get back is 10% success rate.
[2319.86 → 2325.44] But they think out of 100 such projects, if we found anything in 10 of them, that's what they expect.
[2325.50 → 2329.76] And if we were able to get 20, then they would be really impressed and delighted.
[2329.76 → 2334.94] And so we have about a 75% success rate on these projects.
[2335.32 → 2336.94] So this is importantly better.
[2338.02 → 2338.94] Yeah, significantly.
[2339.32 → 2340.04] Significantly better.
[2340.48 → 2343.36] But actually, let me walk you through an example here.
[2343.60 → 2348.48] And here's the important part because it's not just a question of cost.
[2348.54 → 2349.54] It's not just a question of speed.
[2349.58 → 2351.80] It's actually a question about making the impossible possible.
[2351.80 → 2364.28] So there's something that not a lot of people appreciate is in the human genome, we've only ever had medicine, like FDA approved medicines for 4% of human genes.
[2364.98 → 2372.00] And there's another 16% of human genes that have good evidence implicating them in human disease that we would want to be able to target.
[2372.38 → 2373.38] We've never been able to target.
[2373.48 → 2380.24] So it's like four times the entire pharma industry is waiting for us to figure out a way to get medicine for those.
[2380.24 → 2380.68] Right.
[2381.38 → 2382.52] So there's huge opportunity.
[2383.12 → 2386.22] But to do what's been impossible, you need technology that have never existed.
[2386.32 → 2388.20] That's why we're out there inventing these.
[2388.30 → 2388.40] Right.
[2388.46 → 2390.06] Like, so that's what we're working on.
[2390.36 → 2391.72] So let me give you an example.
[2392.10 → 2395.86] And so this is joint work with Professor Ron Viola at the University of Toledo.
[2396.04 → 2398.02] And there's a disease called cannabis disease.
[2398.62 → 2402.06] This is an ultra-rare neurodegenerative disorder.
[2402.46 → 2405.10] If you're pregnant, it's one of the things that you're doing a genetic screen.
[2405.18 → 2407.40] It's like one of the things that they test for in genetic screens.
[2407.40 → 2415.68] And basically, you know, I won't get deeply into the biology, but you've got a molecule in your brain called NAA, N-acetyl aspartame.
[2416.06 → 2418.10] And you have a system that makes it in your brain.
[2418.18 → 2419.62] You have a system that clears it out in your brain.
[2419.86 → 2423.04] And these kids lose the ability to clear it out.
[2423.34 → 2425.24] And so this NAA builds up in the brain.
[2425.40 → 2428.90] And basically the sheath around your neuron, the myelin sheath, starts to degrade.
[2429.00 → 2430.74] And these kids stop hitting developmental milestones.
[2431.08 → 2431.82] It can be fatal.
[2432.30 → 2433.74] There's really no cure for it.
[2433.74 → 2435.18] So it's a pretty tragic disease.
[2435.98 → 2444.46] But there was some mouse data that showed that having lost the ability to clear this NAA, if you slow down the synthesis, you could bring the system back into balance.
[2445.24 → 2446.64] And the mice live full lifespan.
[2447.44 → 2451.02] And so that gave us the idea that we could develop a drug for the synthesis side.
[2451.82 → 2457.32] But that, the N-acetyl aspartame synthase, that synthesis side is a classic undrinkable target.
[2457.40 → 2457.96] And I'll tell you why.
[2458.38 → 2460.72] It's something called, it's inside the neuron.
[2460.80 → 2461.94] So it's in the central nervous system.
[2461.94 → 2462.88] It's inside the neuron.
[2463.00 → 2465.06] Your brain is protected by something called the blood-brain barrier.
[2465.40 → 2466.80] So it's like an armour around your brain.
[2466.88 → 2467.88] So it's very hard to get to.
[2468.50 → 2470.78] That protein itself is membrane-associated.
[2470.82 → 2472.88] So it's stuck in the membrane inside the cell.
[2473.22 → 2478.08] And that makes it very finicky to work with, very hard to work with, difficult to express, difficult to purify.
[2478.16 → 2485.74] Just getting enough of it to run large experiments, which is, as we discussed, you know, the state-of-the-art in pharma today, you couldn't get enough of the protein.
[2486.42 → 2488.44] You couldn't get a crystal structure for the protein.
[2488.44 → 2496.32] And so I don't know what Alpha-Fault-Tool can do, but, you know, experimentally, we had no way of designing molecules based on the shape of that protein.
[2497.28 → 2500.76] Designing that monkey wrench, which would block up the protein.
[2502.00 → 2507.30] And so basically, all the standard doors for drug discovery were closed.
[2507.60 → 2509.28] You know, you couldn't run a big physical screen.
[2509.38 → 2510.74] You couldn't design based on the structure.
[2510.74 → 2514.32] There were no molecules, drug-like molecules, which were known for this protein.
[2514.46 → 2517.68] So you couldn't build, you know, a machine learning model specific for that protein.
[2518.62 → 2523.40] You know, human medicinal chemists didn't have anywhere to get going from, you know, to start working on.
[2523.48 → 2527.54] And so basically, all those standard doors were closed until we worked on it.
[2528.68 → 2533.90] And so what we did was, with these machine learning techniques, empirically, they are more robust.
[2533.90 → 2536.94] And so you can use distant homology models.
[2537.14 → 2546.44] So like the kind of thing that Alpha-Fault-Tool produces, we can use that rather than having to have an experimental X-ray crystal structure, a 3D, experimental 3D structure of the protein.
[2546.98 → 2550.66] And so we used a very, very distant protein, a bacterial protein.
[2550.66 → 2555.10] So separated by 3 billion years of evolution, only 20% of the amino acids were identical.
[2555.22 → 2556.48] So very, very distantly related.
[2556.88 → 2558.28] But we used that as a homology model.
[2558.28 → 2561.44] We screened 7.2 million molecules.
[2562.24 → 2569.84] And for context, a big pharma company might have like 3 to 5 billion, 3 to 5 million molecules in its corporate collection.
[2569.90 → 2572.70] So this is maybe twice the size of a big pharma corporate collection.
[2573.10 → 2577.24] Out of 7 million, we pulled down to 60 that we thought we'd test.
[2577.82 → 2586.48] And 5 of the 60, so quite a high hit rate, 5 of the 60 were actually accurate with the best one being more potent than what you would expect from a physical screen.
[2586.48 → 2588.66] And so that's not a drug yet.
[2588.78 → 2590.18] We have to continue working on it.
[2590.20 → 2594.36] But where all the doors were closed, now we've opened the door to doing drug discovery.
[2595.06 → 2595.62] That's so cool.
[2596.12 → 2597.00] It really is.
[2597.10 → 2598.04] Yeah, that's quite a story.
[2598.04 → 2598.28] That's an amazing story.
[2598.38 → 2613.36] Because I know, like I've heard of these things like, and, you know, not being a medical person or a biology person, you hear about these diseases or other things where it's really not possible to develop a drug, or they don't know where to go.
[2613.36 → 2621.70] And it's really cool to hear about, you know, some stories of people trying to push through that barrier and really commendable work.
[2621.70 → 2640.12] I'm curious, maybe a slightly weird question, but one of the things that people, of course, are so concerned about with kind of the rapid expansion of applications of AI into all spheres of life is various sources of bias in the data that we're using.
[2640.12 → 2649.98] And I think this has been particularly, you know, not in the case of AI, but another source of bias that people have been talking about recently is with vaccines.
[2649.98 → 2657.04] And of course, certain populations who maybe have a certain history with vaccines or other things are very concerned.
[2657.04 → 2665.70] But for example, with the coronavirus vaccine of, you know, hey, there, you know, does this work well for our population or other populations?
[2665.70 → 2669.90] Are we getting the, you know, the bad vaccine or something like that?
[2669.90 → 2694.74] And so I'm wondering, as you are specifically trying to apply AI in these cases, what is your thought process around sort of making sure that you're accounting for some of that bias in your methods, and you're creating, you know, sort of drugs that are kind of applicable to general population that is diverse?
[2694.74 → 2704.68] Absolutely. So I think it's absolutely the case that we need medicines for all people everywhere in the world.
[2704.68 → 2722.00] And I think one of the things I'm proud of is the fact that we're working, you know, that we open this program globally, that we're democratizing access to these kinds of technologies to researchers around the world and that they can decide what diseases, you know, they're concerned about where they see the ability to make a breakthrough.
[2722.00 → 2725.44] Right. Like I said, we've had these applications from over 50 countries.
[2725.88 → 2737.08] If our priorities about, you know, which medicine we work on is just happening in Boston, Massachusetts, there's going to be a skew to the kinds of diseases which are familiar in Boston, Massachusetts.
[2737.42 → 2739.06] Right. Or keep people up in Massachusetts.
[2739.06 → 2746.20] But if you look at another place in the world, right, like stomach cancer has a much higher prevalence in East Asia than it does in the U.S.
[2746.44 → 2753.54] And I don't know if it's because of environmental or dietary or genetic factors, you know, or it could be a mix of all of those.
[2754.22 → 2756.62] South Asia has a high cardiovascular burden.
[2757.28 → 2760.60] There are different kinds of liver disease in Southeast Asia than other parts of the world.
[2760.88 → 2767.72] I mean, so absolutely right that what is high on the list and what is top of mind for people is going to be different in these different places.
[2767.72 → 2783.10] And so I think by dropping the cost of developing medicines with these new technologies and dropping the barriers and reducing the timelines and putting these technologies into the hands of people, then we can help democratize that decision maker.
[2783.96 → 2790.94] So one example, you know, we're working with an NGO based in Geneva called the Drugs for Selective Disease Initiative.
[2790.94 → 2799.24] And there we're working kind of similar style story, but we're working on a disease called Chavez disease, which is an endemic disease of poverty in Latin America.
[2799.66 → 2809.14] By having new technologies and making success easier to reach and faster to reach that, you know, we can go, and we can tackle a much broader set of diseases.
[2809.44 → 2812.14] So that's our perspective on a very important problem.
[2812.30 → 2813.14] I'm glad you raised it.
[2813.34 → 2814.42] That's a really great perspective.
[2814.42 → 2824.66] I think it's a great point that this sort of diversity of diseases and also how it's diverse across geographies and populations is like an AI sized problem.
[2824.66 → 2825.12] Right.
[2825.32 → 2831.74] Because we do only have so much capacity of like expert chemists, expert doctors, medical professionals.
[2831.74 → 2840.38] Like we only have so much capacity there, but yet we have this sort of increasingly complex disease situation around the world.
[2840.52 → 2842.20] So, yeah, I think it's a perfect point.
[2842.20 → 2848.48] So, you know, to that point, when you say AI sized problems, can you kind of tell us?
[2848.56 → 2858.24] I mean, this sounds like it's truly in the process in the early stages of revolutionizing an entire industry because of the scale and the accuracy.
[2858.76 → 2860.20] You've changed the whole thing.
[2860.84 → 2863.60] And so where do you see this going?
[2863.60 → 2874.44] You know, no one can tell the future, but if you'll put your wizard hat on for a minute and pull out the crystal ball and speculate on what it looks like 5, 10, even beyond, what do you think?
[2874.52 → 2880.22] You know, when you lay in bed at night, and you're thinking about where you're going with this and where you want to go with this, what does that look like?
[2880.56 → 2886.72] And how does the world change as a result of this, you know, within that industry, which affects all of us?
[2886.88 → 2887.44] Where are we going?
[2887.44 → 2890.02] I think you're right to note that it affects all of us, right?
[2890.04 → 2895.66] Like this is one of the fundamental universal truths about being human, right?
[2895.70 → 2901.04] Is that we get sick, you know, our parents get sick, our kids get sick, you know, the people we care about get sick.
[2901.46 → 2903.10] And so this is something that all of us face.
[2903.60 → 2907.34] And I think, you know, in some sense, no one comes down on the other side.
[2907.46 → 2913.56] No one says, yeah, chemotherapies, those side effects are fine, right?
[2913.56 → 2917.24] Like, and the success rates are fine, Alzheimer's, we don't have any real treatment.
[2917.80 → 2919.46] Well, you know, I guess that's it, right?
[2919.50 → 2923.44] Like, we're just going to have to live with it or not, as the case may be, right?
[2923.48 → 2930.70] Or diseases of poverty around the world that we haven't been able to afford to direct large discovery.
[2931.30 → 2935.06] We'll just, you know, what can we do, right?
[2935.08 → 2938.16] Like, I don't think anybody is actually advocating for any of those approaches.
[2938.16 → 2944.84] We want better treatments for all of it, let alone diseases that we had fixed, but we're losing ground, right?
[2944.86 → 2950.26] Like the WHO is talking about, you know, a post-antibiotic apocalypse, right?
[2950.34 → 2954.38] Like, and when you see serious governmental organizations use words like that, right?
[2954.40 → 2955.20] Like, it's serious.
[2955.44 → 2958.00] And that's the growth of antibiotic resistance, right?
[2958.00 → 2964.54] Like, we need fundamentally new approaches to antibiotics just to maintain the kind of lifestyle that we're, that we've been happy with, right?
[2964.54 → 2975.80] Like, one of the stories there is Calvin Coolidge's son got a blister playing tennis on the White House lawn, got sepsis and died, right?
[2975.84 → 2978.64] Like, this is, you know, most powerful man in the world, right?
[2978.68 → 2983.86] Like, and in the era before penicillin, right, you had no protection, right?
[2983.86 → 2985.26] Nobody had protection against it.
[2985.58 → 2989.88] And so we need technologies that keep up with the evolutionary arms, right?
[2990.28 → 2992.86] So I think you're absolutely right that this is critical.
[2992.86 → 2998.32] I also, this is a long, maybe long and maybe rambling answer to your question.
[2998.88 → 3002.10] No, long and rambling is good when you're predicting the future, okay?
[3002.86 → 3005.68] I also want to give credit, I want to take the opportunity to give credit to the chemists.
[3006.38 → 3010.62] Like, real transformation happens at the intersection of multiple different pieces, right?
[3010.66 → 3013.52] Like, if you think about AI, there's data, right?
[3013.52 → 3022.80] And there are algorithms that come together, but those wouldn't be able to be run without the huge success by DevOps and cloud computing and GPUs, you know, like breakthroughs in the hardware.
[3022.80 → 3025.46] Which are driving, you know, much of the it's, what is it?
[3025.54 → 3029.68] I was just looking at this because I'm a nerd if we didn't already establish this.
[3030.94 → 3040.80] The ASCII white, the most powerful supercomputer in the world and therefore in the history of our species up to 2001, ASCII white, right?
[3040.80 → 3044.18] Clocked in at over $100 million and 100 tons.
[3044.58 → 3050.50] That machine, peak flops, is an Xbox today, right?
[3050.66 → 3053.64] Like, you know, that's an incredible transformation, right?
[3053.66 → 3056.90] And so if you think about, like, why are we able to do these things with AI today?
[3057.06 → 3061.06] It's because of the massive success by hardware engineers, right?
[3061.10 → 3062.02] It's driving a huge part of it.
[3062.02 → 3063.92] So I want to give a shout-out to the chemists.
[3064.60 → 3073.02] There's been this equal exponential change on the side of the chemists, which is why AI, why we should care about AI.
[3073.14 → 3074.08] So here's what they did.
[3075.04 → 3080.64] 15, 20 years ago, big pharma, like if you and I wanted to order compounds out of the catalogue, right?
[3080.64 → 3081.98] These commercially available compounds.
[3082.22 → 3084.14] There were maybe a million molecules that you and I could buy.
[3084.14 → 3093.04] And big pharma, like Pfizer and Novartis and GlaxoSmithKline and Bristol-Myers, they had maybe three to five million molecules in their warehouses.
[3093.82 → 3098.82] And so in that world, it was better to be Pfizer and Novartis, right?
[3098.86 → 3101.86] Because you had a better shot about finding something in your catalogue.
[3102.12 → 3106.06] And then with an army of chemists, you could iterate your way to a drug from that initial something.
[3108.00 → 3111.14] Remember, in cannabis, that's what we lacked with that initial something.
[3111.62 → 3112.74] And that's what we were able to have.
[3112.74 → 3115.84] They were already scaled up enough to have a good chance starting.
[3116.02 → 3116.28] Exactly.
[3116.40 → 3118.30] Well, they had a better chance than you and me, right?
[3118.46 → 3120.80] Good or not, that's an empirical question, right?
[3120.86 → 3122.78] Like after you ran the screen, you could tell.
[3123.02 → 3124.60] But they had a better chance than you and me.
[3124.84 → 3124.98] Okay.
[3125.42 → 3132.06] But here's what happened in sort of the 15 years afterwards is we've adopted something called – the industry has adopted something called synthesis on demand.
[3132.36 → 3133.74] And here's where it works.
[3134.74 → 3137.30] You may remember Dell computers.
[3138.86 → 3138.96] Okay?
[3139.24 → 3139.72] Of course.
[3139.72 → 3147.62] So you remember – okay, Michael Dell had what was principally a business innovation, which was I'll get to work after your check clears, right?
[3147.64 → 3149.34] Like that's principally a business innovation.
[3149.82 → 3158.22] But there was a corollary to that change, which is that the range of different computers that Michael Dell could sell you was way more than what anybody else could sell you.
[3158.22 → 3164.80] Because it was every potential combination of printer and memory and monitor that you could choose to put together.
[3164.84 → 3165.00] Sure.
[3165.26 → 3165.44] Right?
[3165.52 → 3167.12] He waited until you said what you want.
[3167.68 → 3174.48] And so basically the same thing happened in chemical vendors is they store these days building blocks.
[3174.48 → 3176.78] And they say, I know how to put them together.
[3177.30 → 3184.86] And so what they sell you is a catalogue of 16 billion different compounds that they know how to make but that they haven't made yet.
[3185.38 → 3185.60] Right?
[3185.80 → 3186.94] Exactly like Dell computer.
[3187.20 → 3189.10] Knows how to make that computer, hasn't made it yet.
[3189.48 → 3191.62] And they're adding about a billion molecules a month.
[3191.78 → 3191.98] Okay?
[3191.98 → 3199.06] So we're talking here already like maybe 5,000 times the size of a big pharma corp question that you and I have access to.
[3199.84 → 3202.02] And we can get it shipped in four to six weeks.
[3202.88 → 3203.30] Okay?
[3204.08 → 3215.36] And so this means that like basically 99.9% of all molecules ever available to medicinal chemists today are accessible only through computational approaches.
[3215.94 → 3217.52] Because you can't test them physically.
[3217.62 → 3219.28] They don't exist physically to be tested.
[3219.28 → 3222.08] You have to run the experiment first.
[3222.62 → 3226.04] And then you can run, you know, you can purchase the molecule to run the physical.
[3226.14 → 3227.58] You have to run the computational experiment first.
[3227.96 → 3233.32] Every chemist today is a computational chemist if they're being, you know, if they're really looking at it this way.
[3233.40 → 3235.20] Every medicinal chemist is a computational chemist.
[3235.52 → 3235.72] Okay.
[3235.98 → 3237.16] So that's a fundamental shift.
[3237.20 → 3238.64] And that was driven by the chemists.
[3239.00 → 3239.12] Right?
[3239.16 → 3242.30] The fact that they've been so successful in these syntheses and coming up with these syntheses.
[3242.30 → 3252.90] And if you draw the trend line of that growth, by 2024, if the trend, you know, if they stay on trend, those libraries are going to be about a trillion molecules big.
[3252.90 → 3257.08] And so this is why we need AI.
[3257.24 → 3262.08] It's because at that scale, it's not enough to be 99% accurate.
[3262.86 → 3262.96] Right?
[3263.12 → 3265.18] 99% accurate means 1% inaccurate.
[3265.42 → 3271.30] And the point where you're, you know, running a trillion molecules, 1% accurate means 10 billion false positives.
[3272.08 → 3272.24] Right?
[3272.46 → 3275.12] You need way better than 99% accurate.
[3275.18 → 3276.44] You need 99.999, whatever.
[3276.44 → 3281.36] And it just turns out that our best technologies are machine learning technology.
[3282.34 → 3282.40] Yeah.
[3282.50 → 3288.94] You know, for most people listening to this, you just put their problems in perspective of being not so bad.
[3290.62 → 3293.58] Most of us aren't having 10 billion false positives.
[3293.72 → 3293.92] Right.
[3293.98 → 3294.40] I'm just saying.
[3294.60 → 3294.74] Right.
[3294.78 → 3295.10] Exactly.
[3295.62 → 3295.80] Yeah.
[3296.06 → 3299.18] And so, you know, there's huge promise out there.
[3299.24 → 3299.42] Right?
[3299.48 → 3302.12] And these are deeply meaningful problems.
[3302.24 → 3302.38] Right?
[3302.38 → 3306.50] Like the potential, if you can crack this, is worth it.
[3307.28 → 3307.42] Yeah.
[3307.44 → 3312.04] But boy, you've got to be willing to take on a 10 billion false positive problem.
[3312.30 → 3312.42] Right?
[3312.48 → 3315.30] Like Facebook doesn't have a 10 billion false positive problem.
[3315.32 → 3315.46] Right?
[3315.48 → 3316.74] Because there's only 7 billion people.
[3317.00 → 3317.24] Right?
[3317.30 → 3320.04] Like you're capped how badly things could go.
[3322.18 → 3322.62] Yeah.
[3322.62 → 3331.92] Well, I definitely, for one, am super glad that you and your team are willing to be one of those taking on this problem.
[3332.44 → 3338.98] It's so inspiring and cool to hear about some of the things you've already done and, you know, some of the success that you've had.
[3339.50 → 3343.88] And it does really sound like there's some wonderful things in the future.
[3344.12 → 3350.62] So, yeah, definitely look forward to having you back on the show to give an update on how things are going.
[3350.74 → 3353.24] But we appreciate you taking time to talk with us.
[3353.32 → 3354.24] I know I've learned a lot.
[3354.36 → 3355.62] It's been really great.
[3355.94 → 3357.54] So that's a fantastic conversation.
[3357.86 → 3358.32] Thank you.
[3358.54 → 3358.72] Yeah.
[3359.00 → 3359.84] I had a lot of fun.
[3359.84 → 3362.98] There's a ton of open problems, like well worth working on.
[3363.20 → 3367.46] And at their core, it turns out that medicine is an AI problem.
[3367.46 → 3373.62] Thank you for listening to Practical AI.
[3374.28 → 3377.90] If this is your first time, make sure you subscribe so you don't miss a thing.
[3378.04 → 3386.08] Head to practicalai.fm to subscribe or find us in Apple Podcasts, Spotify, or wherever you listen to podcasts.
[3386.08 → 3391.04] And if you get value from the show, please do share it with a friend or a colleague.
[3391.22 → 3392.60] We appreciate you spreading the word.
[3393.46 → 3396.34] Practical AI is hosted by Daniel Whiten ack and Chris Benson.
[3396.84 → 3400.44] It's produced by Jared Santo, and our music is provided by Break master Cylinder.
[3400.98 → 3403.12] We are brought to you by some awesome sponsors.
[3403.68 → 3406.16] Shout out to Vastly, Linde, and Launch Darkly.
[3406.94 → 3408.20] That is our show.
[3408.36 → 3410.88] We hope you enjoyed it, and we'll talk to you again next week.
[3410.88 → 3440.86] We'll see you again next week.
