[0.00 → 5.76] There is a pattern I see in mathematics very frequently that old ideas influence new ideas.
[6.02 → 11.14] As a researcher myself, when I was working on one of the problems which I solved in my PhD,
[11.42 → 17.44] one of the key components of the proof I found in a paper which was written during the Second World War.
[17.64 → 18.34] It's very odd.
[18.64 → 23.36] As a machine learning engineer, when would you use papers that are more than 20 years old?
[23.68 → 23.94] Never.
[24.14 → 26.36] It never happens because the technology moves so fast.
[26.36 → 29.44] But mathematics is kind of timeless because it's about the language.
[29.44 → 30.96] It's the language of algorithms.
[33.70 → 36.34] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[36.72 → 37.28] We love Linde.
[37.36 → 38.78] They keep it fast and simple.
[38.90 → 41.26] Check them out at linode.com slash changelog.
[41.50 → 43.56] Our bandwidth is provided by Vastly.
[43.92 → 47.46] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[47.74 → 49.44] Get a demo at LaunchDarkly.com.
[49.98 → 53.32] This episode is brought to you by our friends at Rudder stack.
[53.32 → 58.06] And we're calling all data engineers to check out Rudder stack Cloud and start building smart customer data pipelines.
[58.06 → 60.28] Rudder stack is warehouse first.
[60.50 → 61.46] No more silos.
[61.92 → 65.26] Rudder stack builds your customer data lake on your data warehouse, not theirs.
[65.52 → 70.96] Enabling all functionality of a CDP with more security and retaining full ownership of your data.
[71.30 → 73.72] It's open source and API first.
[74.04 → 77.48] Rudder stack can be easily integrated into your existing development processes.
[78.04 → 80.80] And because they're open source, you can see all their code.
[81.02 → 83.44] So you don't have to worry about vendor lock-in or black boxes.
[83.44 → 85.56] And best of all, they have transparent pricing.
[85.76 → 88.00] Stop paying your CDP a premium to store your data.
[88.48 → 93.36] Rudder stack is free up to 500,000 events and pricing scales transparently from there.
[93.78 → 95.80] Learn more and get started at Rudderstack.com.
[96.06 → 98.36] Again, Rudderstack.com.
[98.50 → 102.04] That's R-U-D-D-E-R-S-T-A-C-K.com.
[102.04 → 118.94] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[119.28 → 123.34] This is where conversations around AI, machine learning, and data science happen.
[123.60 → 128.38] Join the community and Slack with us around various topics of the show at changelaw.com slash community.
[128.38 → 129.72] And follow us on Twitter.
[129.88 → 131.42] We're at Practical AI FM.
[132.04 → 140.56] Welcome to another episode of Practical AI.
[140.92 → 142.60] This is Daniel Whiten ack.
[142.72 → 145.74] I'm a data scientist with SIL International.
[146.22 → 150.72] And I'm joined as always by Chris Benson, who is a strategist at Lockheed Martin.
[150.98 → 151.62] How are you doing, Chris?
[151.96 → 153.40] I am doing very well, Daniel.
[153.40 → 158.46] Enjoying nice cooler weather and looking forward to some cool topics on today's episode.
[159.08 → 159.84] Yeah, for sure.
[159.94 → 161.30] Are you brushed up on your math?
[161.30 → 162.34] Oh, my God.
[162.44 → 163.30] No, I'm not.
[163.38 → 165.80] I'm not as good at math as I wish I was.
[165.94 → 172.76] So I am super jealous when we find somebody to talk to that is really, perfect at math.
[172.76 → 174.00] Like I think we're about to.
[174.00 → 183.52] Yeah, well, I think we're both lucky in that respect because we've got Ibadan Lanka with us, who is an educator in the machine learning space.
[183.52 → 191.02] He's writing a book, which he talks about as going from high school mathematics to neural networks, which is a pretty cool idea.
[191.14 → 191.82] Welcome, Ibadan.
[191.94 → 192.42] Hi, everyone.
[192.42 → 194.24] Yeah, it's great to have you here.
[194.48 → 195.56] It's great to be here.
[195.88 → 196.24] Yeah.
[196.24 → 208.62] So first, I guess, how did you start thinking about like, hey, there's a need out there to help people along the pathway from like high school mathematics to neural networks?
[208.62 → 210.58] So I'm a mathematician by training.
[210.78 → 216.20] All of my higher education in the mathematics field, like a bachelor's, master's and PhD.
[216.98 → 219.86] So it was like a kind of given to me.
[220.32 → 221.80] I'm an expert in mathematics.
[221.80 → 237.22] And I just started to post on Twitter about mathematics and machine learning because after my PhD in pure mathematics, I started working in machine learning, more specifically bioinformatics.
[237.90 → 241.78] And then I just started to create content on the topic.
[242.02 → 244.06] And it got traction.
[244.06 → 251.46] And as I created more and more content, I got more and more feedback, I realized that there is actually like a need from people.
[251.74 → 253.30] They want to understand mathematics.
[254.02 → 262.74] But often the learning curve is so steep that many people fall off of the cliff, which I think is quite unfortunate because mathematics is not that complicated.
[263.34 → 265.04] You know, mathematicians make it complicated.
[265.46 → 267.30] It doesn't have to be.
[267.30 → 275.02] If you can properly explain and motivate concepts, it's like what we use in machine learning are quite, quite intuitive.
[275.40 → 279.14] And I really enjoy teaching and explaining stuff.
[279.40 → 281.32] I realized this like a few years ago.
[281.32 → 290.78] And ever since then, I'm putting, you know, more and more energy into teaching, educating, creating educational content in the topics of mathematics and machine learning.
[290.78 → 295.48] Where were you when I needed you so desperately a few years ago as I was getting into this field?
[296.54 → 307.66] What you just said described my entry into deep learning because I was coming from a software programmatic perspective, writing code and wanting to get into it.
[307.70 → 310.12] And I had gotten up through some basic calculus.
[310.12 → 315.28] I think, you know, what we would describe it in our university level is Call 2 integrals and stuff.
[315.34 → 316.46] And that's as far as I made it.
[316.50 → 319.12] And it wasn't far enough to do the stuff.
[319.12 → 330.32] And so I think that that is an experience many, many people have is the frustration of trying to level up in mathematics to be able to do this kind of, you know, really cool work that we're all talking about and working in today.
[330.70 → 333.86] So it seems like something that's desperately neat.
[333.92 → 336.86] I think I don't think that's changed at all since I came through.
[337.34 → 344.06] Usually, usually how they teach mathematics at classical mathematics courses are very boring, which is something I try to change.
[344.06 → 355.46] Yeah, that's unfortunate that it's that case because I do like I have had math classes in the past with, and I'm sure it's just because of the instructor, but ones that I have really enjoyed.
[355.68 → 365.72] But also I have had those that are just like really tough, not even from a content perspective, but just from a like grinding through the content perspective.
[365.72 → 375.44] I'm curious from as you're starting to work with more and more people and talk to them specifically about like mathematics in the context of machine learning.
[375.44 → 395.52] From your perspective, like as a practitioner, like I can download, you know, TensorFlow, run through some tutorials, like download a hugging face or something and like to do some pretty like state-of-the-art stuff without having much of an understanding of what's going on under the hood.
[395.52 → 409.54] From your perspective, like what as a practitioner are some of the benefits of like spending time digging into some of the theoretical and mathematical elements of like what's going on under the hood?
[409.74 → 413.78] It really depends on the stage where you're at in your machine learning journey.
[414.26 → 419.76] I strongly believe that when you start out, you don't really need higher mathematics.
[420.30 → 422.26] High school mathematics is often enough.
[422.26 → 433.24] There is this awesome machine learning course from Fast AI, which explicitly states that all mathematics you need to start is basically taught in high schools.
[433.62 → 435.10] So you don't really need more.
[435.28 → 440.14] And as you go on and on in your journey, you pick up pieces of mathematics here and there.
[440.20 → 445.48] And this is how I think machine learning practitioners should start about learning mathematics.
[445.48 → 455.18] But there comes a point when using built-in solutions, like you just mentioned, like downloading like a pre-trained model from Hugging Face won't work.
[455.48 → 461.96] And how I see mathematics is that in the aspect of machine learning, this is like really the language of machine learning.
[462.22 → 465.62] Mathematics is the language in which algorithms are written.
[466.20 → 470.92] And if you want to effectively talk about those algorithms, you need to learn this language.
[470.92 → 482.34] You don't need to be like a master writer in this language, but you need to speak it properly to exchange ideas with other people, your colleagues and whatnot.
[483.04 → 488.36] And also the level of mathematics you need depends on what will be your job or what is your job.
[488.84 → 495.66] For instance, if you are like a machine learning ops engineer, I don't think you really need that much mathematics.
[495.66 → 502.44] If you are a data scientist, you need a lot of probability theory and statistics, for instance.
[503.14 → 511.40] So for me, this is, as I kind of mentioned, a particularly kind of fascinating thing because, and I'm still very questionable in my mathematics.
[511.58 → 521.22] It was kind of learning as I could, but I was at the time coming through the teens, you know, on or around 2015 when I was struggling with this.
[521.22 → 532.78] And coming from feeling a strong deficit in my mathematical knowledge, how I'm really fascinated when you talk about the fast AI course, talking about you only need it in high school level.
[532.98 → 535.44] Like that's something I wish I had known then.
[535.60 → 536.86] How would you reset me?
[536.92 → 543.00] I'm kind of curious if I can take you right now, and I'm going to transport you back in time, I guess, six, seven years when I'm struggling through that.
[543.20 → 544.64] What would that look like at this point?
[544.70 → 545.64] What would you advise me?
[545.72 → 547.72] So, because I did waste a ton of time.
[547.90 → 549.90] I struggled through stuff I may not have needed.
[549.90 → 551.56] I probably missed some stuff I did need.
[551.94 → 557.54] How would you lay it out for a beginner like me who's coming from another technical skill but isn't a mathematician?
[557.86 → 562.00] I had the same feeling, actually, just in another field in mathematics.
[562.42 → 569.44] I would basically always suggest people to find a problem which they are interested in and then just start building stuff.
[569.66 → 573.96] Once they start, you know, working out a solution, they will stumble upon these smaller obstacles.
[574.54 → 577.06] And sometimes these obstacles are related to mathematics.
[577.06 → 587.74] And then if they know that they have some kind of difficulty of understanding, I don't know, matrix operations, then they should do like a focus research on that topic.
[587.74 → 593.66] Because if you are a machine learning practitioner, you pick up a bunch of mathematics on your way.
[594.22 → 594.74] Right.
[594.74 → 596.54] I found it hard to connect.
[596.68 → 600.00] I was trying to go back and learn the matrix multiplication.
[600.72 → 606.04] And then simultaneously coming from a software background, we tend to go and try to build something anyway.
[606.54 → 610.84] And so I was trying to do that with the tools of the day, which are different from the tools of today.
[610.84 → 621.26] But trying to connect across those two to where I'm attempting to learn the mathematics of machine learning based on what I'm reading about, and I'm supposed to know.
[621.46 → 626.90] And then trying to use the tools of the day, connecting those was agonizing at times.
[627.06 → 628.14] How do you do that?
[628.22 → 634.16] If you're taking someone that is just getting into it, it's today there are someone's coming out, maybe coming out of university.
[634.30 → 635.12] They're a software developer.
[635.12 → 640.00] Or they took one high-level machine learning class, and they want to dive into it.
[640.00 → 648.38] How do you help connect them with that practical side of it, of using the tools and the code, with the theory to understand it?
[648.62 → 654.22] To actually not just be doing it rote, but to be having a sense of what you're trying to accomplish.
[654.44 → 661.88] I usually try to motivate every concept in mathematics with machine learning applications, potential machine learning applications.
[661.88 → 675.98] So for instance, if we are talking about matrix multiplications, if you are in a classical linear algebra class, they just give you the formula for matrix multiplication, and you have to understand it and have to understand it as is.
[676.26 → 688.76] But if you actually take a look at matrix multiplication from a different perspective, so if you go back to machine learning, for instance, if you think about neural networks, if you are a practitioner, you probably worked with fully connected layers, right?
[688.76 → 690.10] So you know what they are.
[690.64 → 695.02] Then I would tell you that, hey, fully connected layers are actually defined by matrices.
[695.58 → 699.18] And why do we need to understand what matrices are?
[699.24 → 703.76] Because we want to understand what our neural network is doing in this small layer.
[703.76 → 708.68] So then this would serve as like an initial motivation to raise your interest in the subject.
[708.94 → 714.30] And then when I talk about matrix multiplication, for instance, I always introduce data transformations.
[714.30 → 728.82] So from an abstract viewpoint, a neural network is nothing else than something which takes the data and transforms it step by step, eventually giving you a representation from which you can read out class labels or whatever you want.
[729.00 → 735.78] And those transformations are essentially made from linear transformations, which are given by matrices.
[736.20 → 740.62] So linear transformations are essential in machine learning.
[740.62 → 744.56] And then, you know, we introduce the concept of linear transformations.
[744.74 → 748.00] Then I would take you through what is the structure of linear transformations?
[748.22 → 750.02] How can you actually describe them?
[750.06 → 757.78] And this is how you stumble upon the very definition of matrix, because the matrix is nothing else but the image of unit vectors under a linear transformation.
[758.78 → 767.14] And then once you understand that, I can just tell you that if you compose two transformations, then you get basically a third transformation.
[767.14 → 777.02] And if you describe the matrix of these composed transformations, then you can calculate by hand how two matrices are multiplied.
[778.12 → 781.86] So composition of linear transformations give the matrix multiplication definition.
[782.10 → 789.60] And I think, for instance, this way is much more interesting and much more understandable for somebody who is coming from an application space.
[789.88 → 791.16] It's very coherent.
[791.34 → 791.92] I got it.
[791.92 → 797.04] And I didn't get other explanations that before I met you in my learning days.
[797.24 → 798.02] Yeah, I was struggling.
[798.18 → 799.12] That's a great way of putting it.
[799.76 → 801.56] Yeah, it's probably also a bit.
[801.90 → 813.26] I understand your play because it's probably a bit difficult also in audio format on a podcast to describe some of these things without visual aids or something like that.
[813.26 → 825.88] But I was wondering, you mentioned sort of getting a lot of interest on Twitter and people starting to interact with you enough that you were like considering creating some of this content, which you have and are creating.
[825.88 → 835.88] I'm wondering, like, was it mostly current practitioners that were sort of interested in this and like deepening their level of understanding?
[836.14 → 846.04] Or was it mostly like those trying to get into the machine learning or AI space and having trouble like understanding jargon and understanding the theory?
[846.52 → 850.80] What sort of mix of people was it that you were interacting with and are interacting with?
[850.86 → 851.76] It's a mixture of both.
[852.40 → 853.40] Twitter is this huge.
[853.40 → 857.12] Every group is properly represented in terms of machine learning.
[857.70 → 860.80] So I interacted with both of these groups.
[861.12 → 861.20] Yeah.
[861.20 → 875.16] So once you reach enough experience in your machine learning career, you have some kind of curiosity about understanding the underlying so-called magic, which is not magic, but you want to understand what is behind the curtains.
[875.50 → 881.56] Then you're basically happy to consume any kind of content which can basically give you that.
[881.56 → 890.18] But I also, also meet with young students who they are taking their first mathematics classes, and they want to understand what's this about.
[890.38 → 893.40] They want to have like more intuitive explanations.
[894.10 → 897.56] And they are not that sure how to connect it with machine learning at that point.
[897.56 → 903.76] Because usually in traditional courses, you are learning mathematics and you are learning computer science.
[903.86 → 905.70] So usually it's like two different tracks.
[905.90 → 908.42] And mathematics courses are usually taught by mathematicians.
[908.50 → 909.74] And I think this is a huge problem.
[910.06 → 912.94] Because even though I'm a mathematician, I know that this is not ideal.
[912.94 → 917.76] Because there is this quote from Goethe that mathematicians are like French people.
[918.06 → 920.64] They see something, and they translate it to their language.
[921.08 → 923.34] And from that point, it means something completely different.
[923.88 → 929.98] So this is why it's suboptimal that you are basically taught mathematics by mathematicians.
[929.98 → 959.96] So this is why it's suboptimal that you are learning computer science.
[959.96 → 969.44] Simply follow the changelog++ link in your show notes or point your favourite web browser to changelog.com slash plus.
[969.44 → 973.66] Once again, that's changelog.com slash plus.
[974.96 → 977.38] changelog++ is better.
[989.96 → 995.42] Well, where I sort of came across your work initially was on Twitter.
[995.70 → 1012.44] And I think a post that probably got a lot of attention where you broke out and had a diagram of sort of all of these different areas of mathematics that you sort of categorized as having something to do with the mathematics of machine learning and how you broke it down.
[1012.44 → 1018.10] Which I thought was, first, like a really well-made diagram and easy to understand.
[1018.60 → 1028.68] But I think also people, maybe where Chris was talking about, where they sort of have all of these bits and pieces of what they think is maybe useful in machine learning and neural networks.
[1028.68 → 1034.26] But to have it broken down on sort of single page and like, hey, what's on the radar?
[1034.44 → 1035.68] What should I be thinking about?
[1035.86 → 1036.98] It was maybe useful.
[1037.44 → 1040.70] Is that sort of breakdown of mathematics?
[1040.70 → 1043.30] And we can go into the details of what's included there.
[1043.72 → 1045.36] How did that sort of come about?
[1045.46 → 1048.40] And how did you end up doing this sort of categorization?
[1048.58 → 1050.80] Was it part of the creation of the book?
[1050.80 → 1053.32] It was before the creation of the book.
[1053.40 → 1053.90] Oh, okay.
[1054.26 → 1056.48] I did it to serve as some kind of blueprint.
[1057.02 → 1059.68] I tried to min-max this roadmap.
[1060.02 → 1068.64] So to be more specific, I tried to leave out every field or subfield, which is not of interest.
[1068.82 → 1072.08] But I wanted to include everything that might be eventually interesting.
[1072.34 → 1074.16] And I worked from backwards.
[1074.74 → 1076.30] So I started with neural networks.
[1076.30 → 1082.70] Basically, you need optimization techniques, and you need linear algebra to describe models.
[1083.24 → 1087.40] And you need probability theory to fit models to data.
[1087.76 → 1090.40] So from that point, I started to work backwards.
[1090.78 → 1093.02] If you want optimization methods, what do you need?
[1093.06 → 1094.58] You need calculus to do that.
[1095.10 → 1099.28] If you want to describe your models, you need linear algebra, and you need a bit of calculus.
[1099.90 → 1104.46] And you also need probability theory to fit models to data and interpret results.
[1104.46 → 1108.70] And after I got those three, essentially broke down into small pieces.
[1108.96 → 1113.78] Basically, I highlighted a few key milestones, which you will encounter later.
[1114.16 → 1116.24] As I said, I tried to be as minimal as possible.
[1116.66 → 1120.62] And I think right now, this is one of those moments going back to what Daniel said is you
[1120.62 → 1121.40] created the diagram.
[1121.52 → 1122.46] So you know it really well.
[1122.54 → 1126.02] And Daniel and I are able to look at it visually right this second.
[1126.24 → 1131.70] But just for listeners who are driving in their car and listening to this, I just thought
[1131.70 → 1136.24] I'd take a two second, describe the central line and then before to do that so that people
[1136.24 → 1137.22] can get the visual.
[1137.64 → 1138.56] And you kind of did that.
[1138.64 → 1141.06] You start with fundamentals, and you hit calculus.
[1141.40 → 1145.08] And with free to these things, you hit all those things that go in calculus and linear
[1145.08 → 1148.84] algebra lead to multivariate calculus, lead to probability theory.
[1149.06 → 1153.98] And then as we get into the neural network section, basics of optimization and mathematical
[1153.98 → 1155.16] statistics are together.
[1155.16 → 1156.78] And then neural networks down there.
[1156.78 → 1162.32] And all of these have this amazing branching into all the knowledge areas.
[1162.70 → 1166.50] I mean, this is I wish I'd had this so bad a few years ago.
[1166.58 → 1168.00] This would have really, really helped.
[1168.44 → 1172.96] And so I just wanted to kind of call out the visual aspects of it as you continue kind of
[1172.96 → 1174.62] describing how you got there.
[1174.78 → 1175.48] Yeah, definitely.
[1175.66 → 1179.42] It's always helpful for me to see something in a visual form like this.
[1179.42 → 1183.70] And we talked a little bit, you went into a little bit of detail about how you connect
[1183.70 → 1188.26] matrix operations with neural networks and all of that.
[1188.60 → 1193.04] I'm wondering if you could sort of do that with a couple of these other ones too.
[1193.44 → 1197.54] When you first started talking about like how you came up with these categories, you talked
[1197.54 → 1200.42] about optimization along with linear algebra.
[1200.64 → 1206.58] So maybe for those like getting into neural networks, maybe they're not familiar with like
[1206.58 → 1210.80] what you mean by optimization in a mathematical sense.
[1210.90 → 1216.94] Could you give just a little bit of an intro to like, what do you mean when you say optimization
[1216.94 → 1221.66] and where does that fit within the framework of neural networks and machine learning?
[1222.14 → 1222.30] Sure.
[1222.60 → 1226.26] So let's just talk about neural networks because they are the best.
[1226.52 → 1229.86] I think our listeners, we don't have to convince them too hard on that point.
[1229.96 → 1230.12] Yeah.
[1230.20 → 1230.48] Okay.
[1230.68 → 1230.92] Cool.
[1230.96 → 1233.34] Then we have a common ground there.
[1233.34 → 1237.18] So again, from a mathematical perspective, neural network is a function.
[1237.60 → 1243.44] You have an input, an output, and you also have a bunch of parameters that basically define
[1243.44 → 1244.16] this function.
[1244.38 → 1247.84] And these parameters are in form of, you know, real numbers.
[1248.20 → 1254.98] And your job as a data scientist or machine learning engineer, whatever, is to find a good
[1254.98 → 1259.04] set of parameters that fits well to your data.
[1259.54 → 1260.94] So how would you do that?
[1260.94 → 1264.74] Need to have some kind of search in the parameter space.
[1265.86 → 1270.44] And one very simple, although useful method is called gradient descent.
[1270.94 → 1274.30] It's essentially, you measure the quality of the fit.
[1274.70 → 1277.22] This is what you do with plugging in an error function.
[1277.54 → 1281.16] You know how well these given set of parameters fits.
[1281.48 → 1284.42] And then you basically want to minimize this loss.
[1284.42 → 1289.96] And that measurement of error is based on those like training examples, right?
[1289.96 → 1294.14] So people probably have heard the jargon like, hey, here's my training set, right?
[1294.26 → 1296.06] So that's where that comes in.
[1296.38 → 1296.48] Yeah.
[1296.94 → 1297.14] Yeah.
[1297.18 → 1302.68] And then if you visualize this loss function, given in terms of the parameters, you see some
[1302.68 → 1304.16] kind of landscape, right?
[1304.16 → 1308.48] Just like you would go on a hike, and you pull out a map, and you see that this is a hill,
[1308.58 → 1309.12] this is a valley.
[1309.38 → 1311.06] This is how you can imagine such a landscape.
[1311.50 → 1316.56] And what you want to do is we want to climb to the bottom of this landscape because this
[1316.56 → 1317.56] is where your loss is minimal.
[1318.44 → 1323.66] And if you are at a given point and your goal is to climb to the lowest point of the landscape,
[1323.96 → 1324.94] how will you do this?
[1325.08 → 1326.26] You look around yourself.
[1326.64 → 1329.78] You try to figure out which way is the steepest descent.
[1330.34 → 1331.72] And then you start going there.
[1331.80 → 1333.68] You take a step in that direction.
[1334.40 → 1338.24] And once you took a step, then you repeat this whole procedure, right?
[1338.28 → 1343.78] So again, you look around yourself and see, determine the direction of the steepest descent
[1343.78 → 1344.90] and then go another step.
[1345.58 → 1347.96] And this is high level description of the method.
[1348.52 → 1354.00] And if you want to implement this mathematically, you need to introduce the definition of gradients.
[1354.00 → 1357.32] So if you have a landscape, how do you define where to go?
[1357.74 → 1359.52] And this is where calculus comes in.
[1359.52 → 1360.94] And this is where gradients come in.
[1361.42 → 1365.66] Because the gradient is actually the direction of the steepest increase.
[1365.84 → 1370.16] But in gradient descent, you actually move to the opposite direction of the gradient.
[1370.82 → 1376.02] So this is how you realize that you have to understand differentiation and gradients.
[1376.58 → 1378.74] Because this is what you do if you want to optimize.
[1379.12 → 1381.90] It's quite interesting that it is an extremely simple algorithm.
[1381.90 → 1386.16] It was known a few hundred years ago, but still useful.
[1386.16 → 1389.32] And it still makes possible to train neural networks.
[1390.02 → 1395.30] Although modern versions are, of course, like, how to say, like, supercharged version of the classical gradient descent.
[1395.44 → 1397.80] But this is what happens, basically.
[1398.32 → 1399.92] This is a safe space, Chris.
[1400.26 → 1400.52] Yeah.
[1400.52 → 1404.02] I think it's more user-friendly if you start with single variable calculus.
[1404.02 → 1408.46] Because multivariable calculus is slightly more complicated.
[1409.24 → 1410.74] And not that much abstract.
[1411.28 → 1412.78] But you have a lot more notation.
[1413.44 → 1419.86] And it's very easy to get lost in those, you know, huge matrices and functions if you don't understand the core concepts.
[1420.06 → 1423.98] So this is why I usually recommend taking single variable calculus first.
[1423.98 → 1427.94] Because then you can understand the concepts of derivative very easily.
[1428.20 → 1430.90] Derivative is just basically the speed of an object.
[1431.66 → 1432.98] It's easy to understand.
[1433.08 → 1439.32] But if you try to generalize this concept into higher dimensions, you include possible complications.
[1439.32 → 1440.84] For instance, I don't know.
[1440.96 → 1443.52] Which direction do you measure the rate of change?
[1443.84 → 1447.48] It's not that clear why would you define partial derivatives.
[1447.92 → 1448.16] Gotcha.
[1448.16 → 1454.84] And one of the other big areas that you have on this map is probability theory.
[1454.98 → 1459.68] You already mentioned that sort of data scientists oftentimes are very concerned with probability theory.
[1459.68 → 1467.66] Maybe there's like certain types of models that they use that are like, maybe they're thinking of like naive Bayes type models.
[1467.66 → 1469.28] And there's like these things out there.
[1469.36 → 1477.08] But when we talk about neural networks, where is probability theory kind of intersecting with neural network based models?
[1477.08 → 1479.46] At the very foundations, I would say.
[1479.68 → 1484.42] For instance, let's talk about mean squared error, which you encounter.
[1484.60 → 1486.98] Or even better, let's talk about cross-entropy.
[1487.38 → 1489.78] It's more common for classification problems.
[1490.42 → 1494.28] So when you want to train a classification model, you often use the cross-entropy error.
[1495.04 → 1498.82] This is the concept which is introduced by probability theory.
[1499.06 → 1505.96] If you want to understand intuitively what it means, then you need to understand, for instance, the fundamentals of random variables.
[1505.96 → 1510.56] Plus, you want to understand entropy itself, expected value.
[1510.56 → 1518.84] So once you can think in terms of expected value and entropy, cross-entropy becomes much simpler for you.
[1519.56 → 1524.62] So to go on about the graphic, because I'm in love with the graphic, because it's super helpful.
[1525.10 → 1527.64] I know this is stuff that you guys know, and I've learned parts of it.
[1527.86 → 1531.48] But it also shows me a lot of things that I need to ramp up on even today.
[1531.64 → 1532.82] So that begs the question.
[1532.82 → 1539.86] It doesn't matter if this was when I was first learning or whether it's now, and I'm trying to continue to level up in my own skills.
[1540.52 → 1544.34] How can this map out all of these knowledge areas?
[1544.50 → 1545.20] And it helps me.
[1545.30 → 1547.54] I can look at each one and say, what do I know about that?
[1547.80 → 1548.92] What have I learned about that?
[1549.20 → 1550.44] Do I feel comfortable with that?
[1550.44 → 1563.52] How can I take this mapping and translate that into a practical learning plan to help myself move on up and develop the mathematics that I need to do the work that I love to do?
[1563.80 → 1570.80] How do you translate that into that kind of linear progress mode from the map that kind of covers so much here?
[1570.80 → 1573.46] So I'm actually writing a book about this topic.
[1574.02 → 1581.54] So maybe now is the perfect time to talk about this, because as I mentioned, I kind of created this roadmap as a blueprint for my book.
[1582.02 → 1588.72] So the roadmap itself, this diagram which we are talking about, is just like a rough learning plan.
[1588.98 → 1592.30] And then this book is where I put this roadmap into action.
[1592.60 → 1598.32] So I organize the chapters in order so that it would take you through from top to bottom.
[1598.54 → 1599.12] I can't wait.
[1599.12 → 1616.16] Yeah, so the top, for those listening who aren't looking at the graph, we're sort of at the top is calculus and linear algebra, then going through multivariate calculus, probability theory, basics of optimization, mathematical statistics, and neural networks.
[1616.16 → 1632.74] In the book, what sorts of decisions are you making in terms of like, because you mentioned notation, jargon being like one of the main, main sort of blockers for people when they encounter these subjects.
[1632.74 → 1634.48] It's like, oh, there's all this new jargon.
[1635.14 → 1643.84] Not every book or course uses the same jargon or notation, depending on like your, yeah, your, your field of study.
[1643.84 → 1656.08] Like I know in physics, oftentimes I would encounter a lot of much different jargon than I would if I was reading like, even like a subdiscipline, like mathematical physics types of like books or articles or something.
[1656.08 → 1669.42] So I guess my question is like, how are you deciding as you're writing the book, like what jargon and notation to use and like how much to pull in code into that or like algorithmic thinking into that, I guess.
[1669.42 → 1672.10] I always, always put machine learning first.
[1672.74 → 1679.02] When I decide whether I should include a topic, I always think it through from the perspective of machine learning.
[1679.14 → 1683.92] So can I motivate this with an example from data science or machine learning?
[1684.46 → 1685.48] Where will this be used?
[1686.08 → 1689.44] If this won't be used anywhere, I won't include that in the book.
[1690.02 → 1696.44] I don't want to basically cause math overload, which all of us experienced at some point in our studies.
[1696.70 → 1698.06] I still do on a regular basis.
[1698.06 → 1700.22] Yeah, trust me, I also experienced that.
[1700.56 → 1703.30] Guiding principle is number one, no unnecessary stuff.
[1703.70 → 1710.46] Guiding principle number two, I always, always introduce every concept as visual as possible.
[1710.76 → 1717.00] Use as much geometry and visual as possible, because this is how you think.
[1717.56 → 1721.30] If you work in mathematics for long enough, you learn to think in terms of formulas.
[1721.30 → 1725.58] But I think this is kind of like a side effect of being a mathematician.
[1726.02 → 1731.64] Nobody should be expected to think in terms of formulas about concepts such as gradient descent.
[1732.66 → 1736.02] And this is what is basically guiding me all the time.
[1736.30 → 1740.32] Even with simple concepts such as matrix multiplication or matrix determinants.
[1740.72 → 1746.20] Determinants for matrices, I mean, they are tough to understand if you don't know the geometry behind them.
[1746.20 → 1750.44] But once you understand the geometry, it's like easy-peasy.
[1750.86 → 1751.24] You know what?
[1751.36 → 1756.02] The thing in my head is you're telling me about this, and I'm so thankful that you're taking the approach that you are.
[1756.34 → 1759.10] This is humane machine learning mathematics.
[1759.64 → 1764.08] I felt like when I was starting my journey along this path, it was not humane at all.
[1764.40 → 1765.86] And I always felt out of depth.
[1766.06 → 1768.32] But I love what your approach on that.
[1768.62 → 1770.30] So, I mean, are you really targeting?
[1770.64 → 1772.56] It's I mean, it feels in the conversation.
[1772.56 → 1774.82] It feels like you're targeting me for this.
[1775.14 → 1778.28] I don't know if there's going to be a dedication to you in the book, Chris.
[1778.66 → 1781.22] I don't think he's promising that.
[1781.94 → 1784.44] To help Chris get out of machine learning purgatory.
[1784.68 → 1786.24] There's your dedication right there.
[1786.44 → 1787.24] That can be arranged.
[1788.96 → 1793.24] Essentially, basically, it's for every computer scientist who is interested in machine learning,
[1793.32 → 1795.52] even those who are not interested in machine learning.
[1795.84 → 1796.58] That sounds great.
[1796.70 → 1796.96] Yeah.
[1797.10 → 1799.14] It's important that it is not for mathematicians.
[1799.14 → 1806.02] I know myself in just thinking about the things I'm exploring in machine learning and AI,
[1806.18 → 1808.62] they're changing so rapidly.
[1809.48 → 1812.42] And there are new things being introduced all the time.
[1812.62 → 1820.16] From your perspective, as you're monitoring the trends within the industry and talking to different people,
[1820.16 → 1829.74] how stable are these sorts of fundamentals as compared to what people are exploring, and what's becoming more mainstream?
[1830.16 → 1839.90] Are there new areas of mathematics that are starting to impact machine learning and AI that maybe people should be aware of?
[1839.96 → 1848.82] Or is it basically just like everything is built on these building blocks and that's pretty much 99.9% of things?
[1848.82 → 1850.06] I would say the latter.
[1850.54 → 1858.32] I mean, essentially, new mathematics fields influencing machine learning is like science fiction for me at the moment.
[1858.48 → 1865.30] Because mathematics is always hundreds of years in front of applications because this is how mathematicians operate.
[1865.50 → 1871.20] I mean, they always try to generalize things to prove even more and more abstract theorems and so on.
[1871.20 → 1877.74] So it's like an intellectual sport, which is like after a while it loses touch with reality.
[1878.38 → 1881.84] And I say this as someone who wrote his PhD in mathematics.
[1882.14 → 1883.90] I have research papers.
[1884.08 → 1889.40] So I know this firsthand that most research papers have absolutely nothing to do with applications.
[1889.96 → 1894.84] Even though mathematicians may try to deny this to get grants and whatnot.
[1895.12 → 1896.60] But sadly, this is the case.
[1896.60 → 1901.10] So I see this, as I said, mathematics as the language which we speak.
[1901.32 → 1907.36] Even though you can write new novels or poems in this language, the language itself remains the same.
[1907.50 → 1910.78] And it evolves slower than, for instance, literature.
[1911.28 → 1911.48] Yeah.
[1911.64 → 1913.08] Although they are interconnected.
[1913.32 → 1914.18] They influence each other.
[1915.00 → 1918.48] Modern mathematics is something like an abstract art.
[1918.70 → 1922.60] You won't understand it unless you are an abstract artist yourself.
[1922.60 → 1933.18] That's a fascinating dichotomy there when you talk about, you know, we think of machine learning as just racing along in terms of its impact and the development of it, you know.
[1933.24 → 1936.78] And you can barely keep up with it because it's going a thousand miles an hour.
[1936.98 → 1943.84] And yet it's built on something that, you know, to your point just a moment ago is hundreds of years ahead of applications.
[1944.06 → 1946.64] You know, and it's a long, long in the development.
[1946.84 → 1948.66] It's not something I had ever considered before.
[1948.76 → 1949.34] It's fascinating.
[1949.34 → 1956.30] Just to give you an example, gradient descent, hundreds of years old, algorithm, base CRM.
[1956.78 → 1960.68] And even nowadays, you can still discover new uses of this.
[1961.04 → 1961.22] Yeah.
[1961.32 → 1969.28] I think in my mind, not being a mathematician, I have no idea about like that sort of abstract art world that you've described.
[1969.42 → 1974.60] Like I totally don't understand or even have, can fathom what's going on there.
[1974.60 → 1989.82] But I think about things like, I think what I had in my mind is like when I'm seeing trends in the AI field that are like graph neural networks, bringing in like different structured data and specific ways of processing that.
[1989.82 → 1998.90] Or I also see like more like mention of differential equations, partial differential equations in relation to like AI.
[1999.32 → 2016.02] I didn't do a search on your diagram, but like, are there things that you're seeing that maybe are old in terms of like the math world, but like people are bringing in to the AI world in sort of ways that they didn't before?
[2016.02 → 2018.22] I guess maybe that's a better way to phrase it.
[2018.60 → 2025.74] There is a pattern I see in mathematics very frequently that old ideas influence new ideas.
[2026.18 → 2028.08] So mathematics is kind of timeless.
[2028.48 → 2034.20] Even now, hundreds of years old results can basically implant new ideas.
[2034.20 → 2047.70] As a researcher myself, when I was working on one of the problems, which I solved in my PhD, one of the key components of the proof I found in a paper, which was written during the second world war.
[2047.88 → 2048.60] It's very old.
[2048.88 → 2054.68] As a machine learning engineer, a machine learning researcher, when would you use papers that are more than 20 years old?
[2055.34 → 2055.62] Never.
[2055.98 → 2058.44] It never happens because technology moves so fast.
[2058.44 → 2062.88] But mathematics is kind of timeless because, as I said, it's about the language.
[2063.42 → 2065.48] It's the language of algorithms.
[2066.58 → 2072.76] And this is how I think it can basically influence for the new ideas like PDE with neural networks.
[2073.04 → 2074.44] What are the technical terms for those?
[2074.72 → 2077.32] Yeah, I see that you mentioned quite a bit.
[2077.52 → 2079.68] Yeah, people are exploring that more.
[2079.94 → 2084.48] Yeah, along with other things like graph theory and other things like that.
[2085.48 → 2088.42] Graph neural networks I'm not very familiar with, unfortunately.
[2088.44 → 2089.36] Yeah.
[2090.00 → 2093.28] Neither of them are all networks that use partial differential equations.
[2093.76 → 2105.02] Well, I appreciate you taking your perspective on how those interactions between the math world and the machine learning world happen and trends in those.
[2105.44 → 2109.74] I definitely appreciate you taking time to chat about all of these things on the show.
[2109.88 → 2111.96] It's been really useful and interesting.
[2111.96 → 2123.02] If you're listening to this, we're going to include a link to Vidar's book and website and a link to this sort of diagram that we've been talking about in the show notes.
[2123.20 → 2124.72] So make sure and check that out.
[2124.98 → 2129.32] If I understand correctly, the book is out for early release, right?
[2129.32 → 2132.94] Yeah, it's in early access, which means the book is not early yet.
[2133.02 → 2135.78] And I publish chapters just as I write them.
[2136.40 → 2138.68] It's usually one chapter per week.
[2138.68 → 2148.00] And one of the big advantages of this early access program is that you essentially, as a reader, you have direct access to me all the time.
[2148.00 → 2154.02] So we have a closed Discord server where you can just ask me after any question you might have.
[2154.02 → 2157.30] And if you have some feedback, I'll just correct it in the book.
[2157.48 → 2161.06] And next week, you'll get an updated version with better explanations.
[2161.72 → 2167.88] So I chose this format because, as I mentioned, I want to write this book for readers, not for mathematicians.
[2168.44 → 2172.62] So this is why I kind of love this early access solution.
[2172.86 → 2173.04] Awesome.
[2173.38 → 2182.08] Well, I appreciate you being also vulnerable during the writing process as well and getting that out to people and letting them get feedback to you.
[2182.08 → 2185.54] I think that will produce a really valuable resource.
[2185.54 → 2193.74] So, yeah, we'll be watching, and we'll be excited to have you back on the show to educate us a little bit more on machine learning math.
[2194.26 → 2195.16] So thanks, Radar.
[2195.32 → 2195.54] Awesome.
[2195.76 → 2197.26] Thank you very much for the opportunity.
[2200.28 → 2202.76] Thank you for listening to Practical AI.
[2203.30 → 2210.42] We have a bundle of awesome podcasts for you at changelog.com, including our brand-new show, Ship It with Gerhard Lazy,
[2210.42 → 2215.32] a podcast about getting your best ideas into the world and seeing what happens.
[2215.70 → 2219.60] It's about the code, the ops, the infra, and the people that make it happen.
[2219.86 → 2223.60] Yes, we focus on the people because everything else is an implementation detail.
[2223.94 → 2229.32] Subscribe now at changelog.com slash ship it or simply search for Ship It in your favourite podcast app.
[2229.40 → 2229.88] You'll find it.
[2230.02 → 2233.28] Of course, the galaxy brain move is to subscribe to our master feed.
[2233.40 → 2238.66] It's all changelog podcasts, including Practical AI and Ship It in one place.
[2238.66 → 2243.76] Search changelog master feed or head to changelog.com slash master and subscribe today.
[2244.20 → 2248.94] Practical AI is hosted by Daniel Whiten ack and Chris Benson with music by Break master Cylinder.
[2249.16 → 2251.66] We're brought to you by Vastly, Launch Darkly, and Linde.
[2251.96 → 2252.68] That's all for now.
[2252.88 → 2253.84] We'll talk to you again next week.
[2253.84 → 2283.82] We'll talk to you again next week.
