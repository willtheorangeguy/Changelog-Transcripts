[0.00 --> 7.74]  This is one of the reasons that we're kind of quite keen on having a very kind of flexible programmable software stack, because there are all these choices to make.
[7.74 --> 18.90]  It's a really great example you've made there of GNNs, because it shows that what we might be doing in two, three years at a time in this field is going to be quite different to what we were doing two, three years ago.
[19.10 --> 22.62]  And if you think like five years before that, then it wasn't your networks, right?
[22.90 --> 24.04]  So it wasn't deep learning.
[24.04 --> 33.70]  And so I think key for us, as much as having the right processor and having these graph techniques, if we can call them as a family, the important thing is to have the capacity to do innovation.
[36.88 --> 39.52]  Big thanks to our partners, Linode, Fastly and LaunchDarkly.
[39.90 --> 40.46]  We love Linode.
[40.54 --> 41.96]  They keep it fast and simple.
[42.08 --> 44.44]  Check them out at linode.com slash changelog.
[44.68 --> 46.74]  Our bandwidth is provided by Fastly.
[47.10 --> 50.64]  Learn more at Fastly.com and get your feature flags powered by LaunchDarkly.
[50.90 --> 52.60]  Get a demo at LaunchDarkly.com.
[52.60 --> 55.72]  This episode is brought to you by our friends at O'Reilly.
[56.08 --> 62.20]  Many of you know O'Reilly for their animal tech books and their conferences, but you may not know they have an online learning platform as well.
[62.56 --> 67.00]  The platform has all their books, all their videos and all their conference talks.
[67.38 --> 78.12]  Plus, you can learn by doing with live online training courses and virtual conferences, certification practice exams and interactive sandboxes and scenarios to practice coding alongside what you're learning.
[78.12 --> 92.06]  They cover a ton of technology topics, machine learning, AI, programming languages, DevOps, data science, cloud, containers, security, and even soft skills like business management and presentation skills.
[92.20 --> 93.98]  You name it, it is all in there.
[94.28 --> 99.46]  If you need to keep your team or yourself up to speed on their tech skills, then check out O'Reilly's online learning platform.
[99.98 --> 103.54]  Learn more and keep your team skills sharp at O'Reilly.com slash changelog.
[103.54 --> 105.92]  Again, O'Reilly.com slash changelog.
[119.32 --> 126.38]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[126.72 --> 130.80]  This is where conversations around AI, machine learning, and data science happen.
[130.80 --> 137.18]  Join the community and Slack with us around various topics of the show at changelog.com slash community and follow us on Twitter.
[137.30 --> 138.92]  We are at Practical AI FM.
[145.02 --> 148.10]  Welcome to another episode of Practical AI.
[148.42 --> 150.00]  This is Daniel Whitenack.
[150.10 --> 153.24]  I'm a data scientist with SIL International.
[153.24 --> 160.78]  And I'm joined as always by my co-host, Chris Benson, who is a principal emerging technology strategist at Lockheed Martin.
[161.08 --> 161.74]  How are you doing, Chris?
[161.96 --> 162.94]  I'm doing good.
[163.04 --> 167.38]  It's a beautiful spring day, and we're about to talk AI with interesting people.
[167.70 --> 169.42]  You can't ask for much more than that, my friend.
[169.50 --> 170.74]  Spring has sprung.
[170.94 --> 171.90]  Spring has sprung.
[172.02 --> 178.52]  Since you're in the South, someone, one of my co-workers this morning was talking to me about every 17 years,
[178.52 --> 181.98]  the cicadas, like the cicada brood.
[182.22 --> 182.88]  It goes crazy.
[183.30 --> 183.68]  In tomology.
[183.94 --> 185.36]  Wait, is that what it is?
[185.54 --> 186.24]  I forget the name.
[186.52 --> 187.60]  The one that starts with an E.
[187.74 --> 188.32]  That's scientist.
[188.32 --> 189.48]  I'm not one of those people.
[189.60 --> 190.76]  The one that studies bugs.
[191.02 --> 192.56]  But are you aware of this?
[192.86 --> 197.26]  I had heard that actually before, and it affects me in a fairly direct way.
[197.60 --> 203.00]  So long-time listeners, and certainly Daniel knows, that I do a lot of wildlife stuff.
[203.28 --> 207.26]  And so on the side, separate from this whole AI thing, I do a lot of wildlife stuff.
[207.26 --> 213.96]  And one of the things I do is I am a snake wrangler, among other things, as part of that wildlife thing.
[214.06 --> 220.64]  So I am commonly picking up copperheads with the appropriate safety equipment, by the way, just so that no one gets the wrong thing.
[221.10 --> 222.96]  And copperheads love cicadas.
[223.26 --> 225.90]  That's a poisonous snake for those that aren't in the U.S.
[226.00 --> 227.40]  Chris is very adventurous.
[227.40 --> 232.06]  If you're not in the southeastern United States, a copperhead is a venomous snake.
[232.62 --> 234.38]  And so I have a lot of experience with those.
[234.52 --> 236.44]  And so totally off topic, of course.
[236.74 --> 240.14]  But the cicadas, yes, favorite meal of a copperhead.
[240.32 --> 240.78]  Oh, okay.
[240.90 --> 241.96]  It's their prime time.
[242.08 --> 242.50]  That's right.
[242.58 --> 244.44]  Who knew we were going here at the beginning of the show?
[244.76 --> 245.30]  Yeah, yeah.
[245.30 --> 254.54]  Well, I mean, I'm sure that there's all sorts of interesting AI to, like, predict the cicada brood numbers this year.
[255.04 --> 256.90]  But that's not the topic of this.
[256.90 --> 258.46]  That's not what we're talking about today.
[258.54 --> 259.46]  I'm so sorry, folks.
[259.82 --> 275.08]  Yeah, actually, I think that I'm pretty interested by the topic and guests this week because it seems like we talk a lot on the show or, you know, GPUs or accelerators or specialty cards for AI are mentioned.
[275.80 --> 282.62]  But a lot of times they're mentioned just in the context of the accelerators, not the sort of software component that goes along with them.
[282.62 --> 293.32]  And, of course, I found, and I don't know about you, but I found that a lot of times when I, like, oh, I really have access to this really cool card or something and I want to use it.
[293.54 --> 296.54]  But the problem is not having access to it.
[296.58 --> 300.92]  It's the, like, software that I write for it has all of these issues.
[300.92 --> 305.82]  So, yeah, I'm really excited to talk about that sort of software hardware interface today.
[306.06 --> 307.02]  Real life AI right there.
[307.16 --> 307.74]  Yeah, exactly.
[307.90 --> 308.94]  Real life practical.
[309.38 --> 310.04]  Very practical.
[310.24 --> 315.08]  With Dave Lacey, who is Chief Software Architect at Graphcore.
[315.34 --> 316.08]  Welcome, Dave.
[316.26 --> 316.48]  Hi.
[316.68 --> 317.48]  Pleased to be here.
[317.60 --> 318.00]  It's great.
[318.10 --> 318.86]  Great to see you both of you.
[319.04 --> 319.32]  Yeah.
[319.54 --> 327.52]  And before we jump into things, do you want to give us just a brief sketch of your background and how you got into doing what you're doing now?
[327.52 --> 327.96]  Sure.
[328.14 --> 328.42]  Yeah.
[328.56 --> 337.60]  So I'm a computer scientist and I'm particularly specialized in compilers and that kind of, in that area of computer science in my life.
[337.64 --> 340.38]  So I did research in that in academia.
[340.38 --> 354.46]  And then over the last so many years, I don't want to say really, but after the last quite a few years, I've been working in various companies, working on the software stack to target new types of hardware in different areas.
[354.64 --> 363.22]  Most recently, we'll talk about the dating path core and AI, but previously in HPC and in embedded processing and network processing, all kinds of things.
[363.22 --> 377.74]  So very much software guy trying to make sure that as we push the field forward and get new hardware to enable new things, we have software that can support that and let users actually program these new wonderful things that get created.
[378.14 --> 378.24]  Cool.
[378.70 --> 378.98]  Yeah.
[378.98 --> 381.26]  And you mentioned a few different things.
[381.36 --> 386.32]  Of course, there's AI specific hardware, there's high performance computing or HPC.
[386.84 --> 397.60]  I think a lot of times when people think about like AI hardware, maybe they're thinking about GPUs, but I mean, the story is a lot more diverse than that.
[397.60 --> 407.54]  So maybe you could give us a little bit of a sketch of this sort of landscape of AI specific or hardware that targets AI workloads, I guess is a good way to put it.
[407.58 --> 409.46]  What are those categories of things out there?
[409.70 --> 410.22]  Sure, sure.
[410.32 --> 418.56]  So I think the ones everyone knows about are CPUs, I mean, clearly, and they definitely have their place in this landscape for specific tasks.
[418.56 --> 426.76]  And then obviously, more recently, GPUs, because of the nature of the kind of highly parallel compute and what they target, they've had quite a bit of success.
[427.46 --> 444.68]  I think you see quite a few companies now, and I think ours is Graphcore where I'm from, and obviously I'm biased, is I think one of the leading, is probably the leading kind of new type of chip in there, where what we're trying to do is produce a chip that's specifically for machine learning in AI.
[444.68 --> 453.06]  So one of the things about other chips is you'll find that they've been designed for something else, CPUs, we know they do all kinds of things, GPUs, originally graphics.
[453.76 --> 459.18]  And our chip is something where we've gone, well, can we design a processor that's just for this space?
[459.32 --> 460.86]  And this space is really important, right?
[460.92 --> 465.22]  You've got so much application that it's worth designing a processor specifically for it.
[465.22 --> 476.22]  I think that's the new kind of breed of processor you'll get, and I think the IP is the one, obviously, that really kind of fits that slot, that allows us to do more in this space than other processors can.
[476.22 --> 482.08]  Because we thought about, from the beginning, the kind of attributes you need for an AI chip.
[482.38 --> 484.78]  So what kind of data are we dealing with?
[484.82 --> 487.34]  What kind of data patterns does that kind of involve?
[487.84 --> 491.64]  What ramifications does that have for us, for example, on the memory hierarchy?
[491.78 --> 498.86]  Our memory hierarchy is very different to other processes and so on, just so we can kind of process data in a different way, or the compute units and so on.
[498.86 --> 506.60]  And that's where we're finding a third place now where we have specialized hardware, ML, AI, intelligent compute in general.
[506.88 --> 510.56]  And that's where the IPU sits for us in Graphcore.
[510.76 --> 520.18]  So as we've talked to different folks through different episodes and everything, is trying to understand kind of where you fit in, and you're kind of laying out the landscape, kind of still at a high level.
[520.18 --> 529.64]  Could you talk a little bit about the different categories before we dive fully into Graphcore, just so that we kind of know in our heads where to position it, how that fits in?
[529.98 --> 534.34]  Because people come into this conversation with different levels of understanding and knowledge on what that is.
[534.50 --> 536.84]  Could you kind of differentiate the different pieces of the landscape?
[537.36 --> 540.28]  Then as we focus in on where you're at, we'll kind of have some context.
[540.66 --> 540.96]  Yeah, yeah.
[541.32 --> 547.66]  I think if I may, if I can take that landscape and talk about it from the types of processing that different processes do.
[547.82 --> 548.22]  Sure, sure.
[548.30 --> 548.72]  That's fine.
[548.82 --> 549.46]  Yeah, that'd be great.
[549.46 --> 555.82]  So like kind of a CPU does, it very much deals with scalar processing.
[555.96 --> 563.06]  So scalar processing is dealing with kind of individual numbers, maybe kind of small groups of numbers together, like small vectors and things like that.
[563.28 --> 566.90]  And they'll do it, that's very good for the general compute, right?
[566.94 --> 570.16]  Because actually, nearly anything can be split down into individual numbers, right?
[570.28 --> 570.42]  Sure.
[570.68 --> 573.18]  So that's kind of the CPU kind of space.
[573.86 --> 578.40]  GPUs, what they deal with primarily is large vectors of numbers.
[578.40 --> 579.96]  I think that's very clear, right?
[580.04 --> 584.48]  So big contiguous blocks of numbers that come in and you're going to deal with them in parallel.
[584.86 --> 587.84]  Because they're dealing with them in parallel, they can get better efficiency.
[587.84 --> 590.18]  So they can go faster on the workplace with the same power.
[590.18 --> 605.56]  So I'd say what you could call the CPUs, say, R-Grapha 1 or everyone's like, you could call them graph processors in the fact that they're dealing with data that's where you have to deal with a lot in parallel.
[605.56 --> 607.14]  So they're highly parallel processors.
[608.10 --> 612.80]  But the connections between them mean they don't come in big contiguous blocks of vectors.
[613.34 --> 620.20]  There's actually kind of, you're going to have to take one number from over there, one number from over there, one number from over there, and then kind of deal with them in parallel.
[620.48 --> 627.72]  And that's kind of, in some ways, a way you could characterize a graph processor in it is one of the aspects to think of in categorization.
[627.72 --> 632.40]  Another categorization, if I may, is also about the type of number you're dealing with.
[632.96 --> 639.12]  So again, those CPUs and GPUs have a wide range of kind of number formats, if you like.
[639.20 --> 645.84]  They're dealing with integers kind of, and also fixed point numbers and floating point numbers with certain different positions.
[646.42 --> 656.68]  But in AI, I think we're finding a lot that what you need to deal with floating point numbers, so kind of fractional numbers to represent, you're kind of representing probability distributions most of the time, right?
[656.68 --> 658.72]  So you don't need a lot of precision.
[659.24 --> 665.14]  What you need is a lot of range, like kind of like if you think of probability distribution, that's kind of what it is.
[665.46 --> 675.94]  So again, it naturally, you're dealing with numbers that are low precision floating point with kind of ranges you have to deal with and kind of randomness involved in there as well injected in.
[676.24 --> 681.88]  So you can think about the shape of the data and the type of the data and kind of which processor deals with what.
[682.16 --> 685.60]  That's kind of probably a reasonable way to describe that landscape across the chips.
[685.60 --> 687.84]  I expect there are other ways you could split it up as well.
[688.20 --> 691.66]  But I quite like those as a way of kind of splitting these things out.
[691.78 --> 698.64]  And it kind of leads you to think, oh, what kind of applications could these be good at kind of by thinking about them in that way.
[698.68 --> 700.28]  Yeah, I see your point on that. Absolutely.
[700.28 --> 702.12]  And maybe you could connect.
[702.26 --> 711.04]  So you talked about like graph nature of the IQ, the graph core processor, and like taking a number from over there and how that works.
[711.12 --> 718.86]  Could you sort of map that onto the typical like AI types of tasks that we're wanting to perform and how that connects?
[718.86 --> 729.54]  People that, for example, are started using TensorFlow before TensorFlow 2 are maybe familiar with saving, quote, graphs or something like that or loading them.
[729.86 --> 732.62]  Does that connect to what you're saying or what's the connection?
[732.86 --> 733.26]  Yeah, yeah.
[733.26 --> 736.66]  So there are several and there are kind of some different levels to unpick there.
[736.94 --> 740.72]  So one of the graphs that gets anything's a graph if you look at it hard enough is one of the things.
[740.86 --> 748.78]  But one of the graphs that people talk about in things like TensorFlow and so on is the compute graph, which is the way data flows around between big tensor operations.
[748.78 --> 752.90]  And that's certainly one of the kind of larger core screen things you can think about.
[753.36 --> 756.82]  But I guess I'm talking more about the graphs that connect the information together.
[757.02 --> 764.60]  So if you think about what are you doing operations and quite often their matrix multiplies or their convolutions.
[764.78 --> 767.84]  Now, let's look at, say, convolutions for image processing.
[767.94 --> 769.18]  That's a really good example, right?
[769.54 --> 776.72]  Because there, what you have there is you don't have quite the all to all connectivity of a matrix multiply operation.
[776.72 --> 786.76]  Like you have a kernel which is going to be applied the same thing to lots of different parts of the image across the image axis.
[787.06 --> 790.34]  The one piece of data is being kind of scanned over the day.
[790.40 --> 793.24]  So you have a kind of particular fan out graph there.
[793.96 --> 799.58]  And then you can get in the operations you can get into as you get into other neural networks.
[799.58 --> 810.42]  Say, if you look at things like Resnext or EfficientNet in image-based neural networks, you can see there that actually you get kind of grouped convolutions or separable convolutions.
[810.72 --> 815.32]  Again, where you're kind of splitting up the data and then recombining it in kind of finer and finer ways.
[815.44 --> 821.44]  So it's those kind of things that require hardware that can cope with efficiently moving that data around.
[821.44 --> 824.28]  And also a software stack that can target that efficiently as well.
[824.42 --> 826.14]  So we shouldn't get the software stack.
[826.26 --> 831.84]  That's kind of what I always like to remind people about you need the software to target as well.
[832.00 --> 832.64]  It takes them both.
[832.76 --> 833.42]  Yeah, yeah, yeah.
[833.58 --> 841.98]  And then if you get into even more kind of recent things that people are doing where you have, imagine you're doing a lot of what we do at the moment when people use TensorFlow as linear algebra.
[842.40 --> 844.92]  Matrix A times matrix B and that gives you some result.
[845.08 --> 848.42]  Kind of take some data coming in and we do a big weighted multiply between that.
[848.42 --> 851.56]  But really, that can be quite inefficient.
[852.12 --> 855.52]  We've got this trend to go really big, really big recently, which is great.
[856.02 --> 860.46]  Actually, it kind of is pushing things forward with these really big kind of you see in language models and so on.
[860.78 --> 862.98]  But, you know, it's not very efficient.
[863.04 --> 867.10]  And you'll see that the shape of that data means there's actually quite a lot of sparsity in there.
[867.18 --> 869.14]  There's a lot of that data could be zero.
[869.28 --> 872.32]  And that leaves you with even more kind of complex data patterns.
[872.32 --> 877.94]  And I think kind of that push for efficiency is another space where you'll get kind of naturally a graph structure.
[878.10 --> 883.80]  Naturally, kind of graph structure is anything where you have kind of almost, in my mind, irregular connections between the data.
[884.36 --> 889.50]  So I think there are lots of different ways of looking at the graph within a kind of neural network or any kind of machine learning program.
[889.86 --> 892.56]  But I think the key ones for me is like, how are the data?
[892.68 --> 893.94]  How's the data connected together?
[893.94 --> 899.62]  Yeah. And I know that at some point, Chris and I were talking about an article about trends.
[899.82 --> 907.66]  I forget which of the major AI conferences it was, but they're talking about trends year over year in terms of what people are focusing on.
[907.96 --> 914.74]  And I know that there was a big boost in people looking more and more at what's called graph neural networks.
[914.92 --> 920.22]  Does that connect directly to what you're saying past the other things in some way?
[920.26 --> 922.88]  Because I know a lot of people are talking about these things.
[922.88 --> 931.40]  And my understanding is it's, you know, in some ways, people say a graph neural network, they have just a way of encoding the graph into a tensor.
[931.68 --> 933.70]  And then you still have the tensor operations.
[933.70 --> 941.38]  But in other ways, there's actually graph native sort of operations that you can do within the network itself.
[941.52 --> 943.76]  I'm not an expert in these things yet.
[943.92 --> 946.92]  Have those connected with what your company is doing at all?
[947.06 --> 949.76]  Yeah, yeah. It's something that we're quite interested in.
[949.76 --> 955.14]  And actually, some of the research groups we work with kind of are interested in that kind of network.
[955.34 --> 961.88]  It's yet another type of graph, but the graph is not the model itself, but the data that the model is consuming.
[962.22 --> 964.48]  What we found is that there's a lot of choice there.
[964.68 --> 967.34]  There's a lot of choice in how you represent the data structure.
[967.86 --> 969.98]  There are many ways to do that.
[969.98 --> 975.08]  And then the actual kind of data processing operation you'll do will be different depending on that.
[975.20 --> 980.54]  So do you represent it as a list of edges or dense matrix or a bit vector or things like this?
[980.84 --> 986.90]  Actually, I think what people really want is a way to explore through those choices at the moment, actually, to kind of push things forward.
[986.90 --> 995.72]  This is one of the reasons that we're kind of quite keen on having a very kind of flexible programmable software stack because there are all these choices to make.
[995.86 --> 1009.86]  I think kind of it's a really great example you've made there of GNNs because it shows that what we might be doing in two, three years at a time in this field is going to be kind of quite different to what we were doing two, three years ago.
[1009.86 --> 1014.08]  And if you think like five years before that, then it wasn't your networks, right?
[1014.32 --> 1015.52]  So it wasn't deep learning.
[1015.88 --> 1027.60]  So I think kind of key for us as much as kind of having the right processor and having kind of these graph techniques, if we can call them as a family, the important thing is to have the capacity to do innovation.
[1027.84 --> 1031.36]  And part of that for us, I think, actually does come down to the software quite a bit, actually.
[1031.36 --> 1042.34]  It comes down to making sure that people can modify it in a good way, can extend it, as well as having the kind of easy out of the box thing where they just I just want to run a 10-foot program or something like that.
[1042.52 --> 1046.62]  I think that the GNNs is a very good example of kind of where you want that kind of flexibility.
[1046.62 --> 1076.60]  Thank you.
[1076.62 --> 1106.60]  Thank you.
[1106.62 --> 1110.18]  That's R-U-D-D-E-R-S-T-A-C-K dot com.
[1120.98 --> 1128.56]  So my head is also still spinning a little bit on something that you were talking about a little while ago, and that is, you know, the software and the hardware.
[1128.74 --> 1129.62]  You need them both.
[1129.62 --> 1143.42]  Over the decades, the world has been very, very CPU focused, you know, up until this most recent time period where we're really digging into AI and all of these new hardware architectures have come into being.
[1143.42 --> 1157.62]  How do you approach, given the fact that we're having all this innovation and how these hardware architectures are coming out, how do you approach writing the software that goes for that hardware, that makes that hardware run?
[1157.62 --> 1163.96]  Especially when you think about the fact that we have a long history of being specific to different types of CPUs.
[1163.96 --> 1166.52]  But now, you know, the sky's the limit on what's happening.
[1166.90 --> 1171.94]  How does that change the act and the thought process and the planning for building software?
[1172.32 --> 1173.40]  I think it does a lot, actually.
[1173.52 --> 1174.80]  I think CPUs are amazing.
[1174.80 --> 1187.20]  I think they've been so successful in fixing an architecture, fixing all aspects of the architecture, the way the instruction set runs, the way the memory hierarchy works, and then applying it to lots of different fields and having that success.
[1187.30 --> 1188.92]  I think it's a remarkable thing.
[1189.36 --> 1191.34]  I don't know if it works for all fields, though.
[1191.64 --> 1201.24]  And I think what we find in AI is one thing that we've been very keen on right from the start, and I definitely see other people in the field talk about it, is this idea of co-design.
[1201.24 --> 1207.82]  So, co-design is this general idea where you want to design several aspects of a system together.
[1208.76 --> 1216.30]  And so, clearly, one of the big aspects of co-design is design your software stack and your hardware architecture at the same time.
[1216.58 --> 1218.96]  And that's something we're very keen on at Graphcore, actually.
[1219.12 --> 1220.36]  We've been kind of right from the beginning.
[1220.48 --> 1224.78]  We're very keen on making sure we worked on how the software was going to target the chip,
[1224.86 --> 1230.66]  make sure we kind of modeled everything right up to the kind of full neural network applications as we design the chip.
[1230.66 --> 1232.12]  And pushing that all through.
[1232.60 --> 1240.98]  I think later on in the company, what happens then is you don't need to extend that software stack and kind of really kind of invest in kind of building that core to a really robust solution.
[1241.12 --> 1243.64]  So, now we've got kind of more software people than hardware people.
[1244.00 --> 1245.72]  It's a really big part of what we do.
[1246.22 --> 1248.08]  Whereas much software company is a hardware company.
[1248.16 --> 1250.88]  But even right at the beginning, it was very much let's design these together.
[1251.20 --> 1252.44]  I don't think it stops there, actually.
[1252.44 --> 1262.28]  I think, actually, you could also say you co-design, and we'll see more and more of this, the machine learning algorithm architecture itself, along with the software and the hardware, and the system.
[1262.70 --> 1272.16]  So, the kind of way you, you know, we're not just, particularly for training, right, for large scale, large data machine learning training, which is the world we're often in at Graphcore.
[1272.54 --> 1273.90]  You're not talking about one processor.
[1274.02 --> 1276.88]  You're talking about hundreds of thousands of processors working together.
[1276.88 --> 1283.90]  And they all need to be connected via networking cables and put into racks and the power management and all this kind of stuff has to be put around it.
[1284.34 --> 1287.14]  And really, you need to co-design all of that together.
[1287.60 --> 1288.42]  And that's good.
[1288.72 --> 1292.90]  I had someone kind of use the term architecture before to describe this.
[1293.00 --> 1294.16]  And I think, yeah, why not?
[1294.36 --> 1295.78]  That's a fair enough term.
[1296.32 --> 1297.68]  That's fascinating what you're saying.
[1297.78 --> 1298.54]  I'm not trying to cut you off.
[1298.58 --> 1300.00]  I actually want you to expand on that.
[1300.00 --> 1312.84]  The idea of doing software, hardware, the actual ML architecture, and the system, that seems daunting because all of those individual topics are, people spend their whole careers doing that.
[1313.26 --> 1315.78]  How do you blend that in a cohesive way?
[1315.90 --> 1319.46]  Seems like your team makeup is very important for that.
[1319.68 --> 1320.92]  I would imagine so.
[1321.10 --> 1321.54]  Absolutely.
[1321.68 --> 1324.86]  I think for us, like, yes, team makeup is important in the company.
[1324.96 --> 1326.92]  We've really kind of stressed that.
[1326.92 --> 1329.90]  I think partnerships are very important for us.
[1330.18 --> 1341.02]  So we've always been quite keen on working with commercial kind of internet, consumer internet companies that want to do large scale deployments behind search engines or whatever there is, you know, so that, you know, the kind of thing.
[1341.40 --> 1349.12]  Which we also want to work with research groups, both kind of university and company research groups to kind of see where that's going.
[1349.12 --> 1350.16]  And we're not alone in that.
[1350.24 --> 1354.04]  A lot of companies will, you know, that's why I think there's been part of why.
[1354.04 --> 1360.08]  That there's this keenness to bring kind of ML researchers into within companies to work on that.
[1360.42 --> 1365.32]  So I think that makeup and the communication between those is really important within company to do that.
[1365.66 --> 1368.42]  And partly it's just an awareness to want to do it.
[1368.58 --> 1371.90]  It's just having those, that communication, like, freely flowing.
[1371.90 --> 1378.68]  And actually to have the right kind of culture within a company to foster that your software is engaged.
[1378.80 --> 1384.00]  Well, actually, no, we really feel that actually to get this album working, you could work it this way.
[1384.32 --> 1391.50]  There is a flip side, I have to say, in that you've got to be careful not to design out the future, if you like.
[1391.50 --> 1397.50]  Because you could interpret this idea as being, we'll harden a piece of software into a chip.
[1397.58 --> 1403.26]  So we'll take like, oh, I don't know, ResNet 50 or something, to give a good example from Visa.
[1403.50 --> 1406.02]  And say, we'll make a chip that will do that really well.
[1406.18 --> 1411.04]  I don't think that's really co-designed because it doesn't, because you have to also design for generality.
[1411.04 --> 1417.84]  As I say, design for not just the algorithms of today, but the algorithms of three years' time or four years' time as well.
[1418.00 --> 1421.08]  Because a chip has to last that long and people want that flexibility.
[1421.66 --> 1427.04]  Is that a little bit of an artifact left over from an earlier time when you were still thinking about CPUs?
[1427.90 --> 1430.08]  And there would be, things would start in software.
[1430.28 --> 1435.36]  You know, you'd solve a problem in software and it would stick and be maintained over the years.
[1435.36 --> 1437.40]  And finally, it would get incorporated into chips.
[1437.40 --> 1447.02]  Is that a legacy mindset that maybe has been brought forward but doesn't work when you're advancing on the ML architectures as rapidly as we are?
[1447.18 --> 1455.16]  I mean, if you bind it into the chip and you're stuck with that, whereas we're seeing, you know, rapid advancement over the last few years in terms of where things are going.
[1455.54 --> 1456.02]  Exactly that.
[1456.12 --> 1457.06]  I think that's exactly right.
[1457.06 --> 1467.16]  I mean, you just need to look at, as everyone who subscribes to Archive Framework will see, the amount of the firehose of innovation here is just huge.
[1467.16 --> 1468.66]  And you have to plan for that.
[1468.74 --> 1471.00]  I think good flexible software is the key to that.
[1471.26 --> 1474.14]  But then you have to design your hardware to kind of match that as well.
[1474.54 --> 1475.90]  So exactly.
[1476.22 --> 1477.68]  I think that's hit the nail on the head.
[1477.90 --> 1480.30]  We're in a real fast-moving space here.
[1480.38 --> 1481.04]  It's not stopped.
[1481.82 --> 1486.84]  There's still a lot of way to go before we kind of settle down on exactly what the algorithms are.
[1487.16 --> 1491.16]  As Chris knows, I'd love to get into the practicalities.
[1491.16 --> 1498.76]  And I guess what I'm thinking of is you have your GraphCore processor, the IPU, over here on this side.
[1499.24 --> 1506.16]  And over here, you have already established community frameworks like TensorFlow, PyTorch over here on this side.
[1506.56 --> 1508.92]  And obviously, people want to use those.
[1509.06 --> 1510.76]  They want to use Keras or whatever.
[1510.76 --> 1519.46]  And I'm sort of looking at a diagram, which we'll link in our show notes, about your popular Graph Framework software, which is very well written.
[1519.60 --> 1521.66]  But you've sort of got the frameworks on this side.
[1521.72 --> 1524.30]  And you've got the processor on this side.
[1524.40 --> 1531.86]  Could you explain just for people what it takes to connect something written in TensorFlow or PyTorch,
[1532.02 --> 1537.88]  like sort of people are used to, to this new way of processing on the Graph processor?
[1537.88 --> 1539.46]  Or what's in between there?
[1539.90 --> 1540.06]  Sure.
[1540.22 --> 1541.94]  Let's take TensorFlow as an example.
[1542.24 --> 1545.46]  And I'll see if I can walk through that diagram from left to right.
[1545.56 --> 1549.98]  So kind of you have your TensorFlow program written in Python, usually.
[1550.64 --> 1556.14]  And what that describes is it will describe, usually it describes some model that you want to optimize,
[1556.38 --> 1557.98]  and then you apply an optimizer to it.
[1558.56 --> 1562.70]  And that gives, that model really is, we're back to this kind of compute graph, right?
[1562.70 --> 1567.32]  So it's a series of linear algebra operations kind of connected together.
[1567.62 --> 1574.12]  And out of the end pops an answer, which you can evaluate on how close you're getting your optimizer to learning a good solution to that.
[1574.60 --> 1577.12]  That graph gets explicitly represented in TensorFlow.
[1577.32 --> 1580.16]  So a data structure gets created, which is that graph.
[1580.66 --> 1583.76]  At that stage, it's called the core graph in TensorFlow.
[1583.76 --> 1586.74]  So it's pretty much what you've written, more or less.
[1587.52 --> 1596.16]  And then what happens is, well, the first thing that happens really is that that gets differentiated.
[1596.30 --> 1600.44]  So we kind of create the backwards pass to say, how do we calculate gradients on that?
[1600.90 --> 1610.56]  And it gets wrapped in a kind of, that whole data structure kind of then represents a big loop outside that says feed data in and kind of update my weights as I calculate these gradients.
[1610.56 --> 1618.68]  We take that whole graph, and then it gets passed first through the TensorFlow compiler flow.
[1618.96 --> 1621.90]  So, and that's not kind of a graphical thing.
[1622.06 --> 1624.54]  That's the TensorFlow kind of upstream developers.
[1624.88 --> 1628.90]  They'll take that graph, they'll canonicalize it into kind of smaller operations.
[1629.26 --> 1635.34]  They'll do some optimizations on it, and they'll convert it into what's called HLO graph, the XLA graph,
[1635.42 --> 1638.92]  so that this goes through their compiler infrastructure, which is called the TensorFlow XLA.
[1638.92 --> 1647.14]  So at the end of that, you have a kind of slightly lower level split up graph where we're still talking about kind of quite big linear algebra operations,
[1647.26 --> 1653.52]  like matrix multiplies and things like that, but it's been kind of reduced down and tidied up and made a bit more kind of closer to the hardware.
[1653.78 --> 1658.38]  So at that point, our graphical TensorFlow backend takes over.
[1658.38 --> 1664.86]  And the first thing it will do is it will do a few more kind of optimizations on that data structure at that level.
[1664.96 --> 1672.62]  For example, in the chip, we have a hardware unit for doing exponentials and sigmoids and the kind of things that come up in certain non-linearities.
[1672.76 --> 1680.36]  So it will recognize those patterns in that graph and say, well, we replace them with one special operator that will kind of go down to the hardware and so on.
[1680.36 --> 1691.44]  So we'll do that kind of, and then it will basically convert those operations into an even lower level form of graph, which is much more fine grained than that.
[1691.76 --> 1701.00]  So we have something called poplibs, which are libraries that implement things like matrix multiplies or non-niliarity operations or things like that in Poplar.
[1701.00 --> 1704.96]  So let me talk about Poplar briefly because I realize I just introduced that without saying what it is.
[1705.20 --> 1705.60]  Absolutely.
[1705.84 --> 1708.66]  So Poplar is our graph programming framework.
[1708.78 --> 1714.82]  So that is a way of representing graphs that run natively on our device that do these kind of operations.
[1715.54 --> 1721.12]  And in Poplar, we have graphs that kind of break it down to the individual processing unit.
[1721.24 --> 1728.66]  So on each of our chips, we have kind of about 1400 cores, processes on the car, each of which has kind of hardware threading in there.
[1728.66 --> 1731.58]  So you've got about 7,000 parallel compute units.
[1731.58 --> 1735.90]  And the Poplar graph kind of represents like the graph at that kind of level.
[1736.38 --> 1739.64]  And poplibs is what kind of then says, well, I've got this matrix multiply to do.
[1740.14 --> 1743.82]  How do I split that over those parallel units in an efficient way?
[1743.86 --> 1747.00]  So that's where it does kind of partitioning and access splitting and stuff like that.
[1747.10 --> 1754.46]  Then we have the Poplar graph compiler, which then will take that fine low-level graph and create kind of actual code for the device,
[1754.64 --> 1758.22]  which then goes into the graph engine, which then kind of runs it.
[1758.22 --> 1762.40]  There are quite a few levels, you know, just quite a few compilers involved.
[1763.12 --> 1765.30]  And we have like kind of, you know, so we counted them.
[1765.38 --> 1772.86]  There's like five or six different compilers that have to interact to get that kind of efficient implementation down on that device.
[1773.22 --> 1776.94]  There are some other things that go on, like sometimes you might want to multi-chip model.
[1777.20 --> 1786.22]  So at the higher level, you'll do kind of model pipelining and things like that to get kind of efficient models spread over multiple chips and things like that.
[1786.22 --> 1788.50]  But fundamentally, that's the flip.
[1789.02 --> 1789.70]  That was great.
[1789.80 --> 1797.82]  And by the way, I don't think I can recall anyone ever taking us through even a genericized, you know, not specific to your system, but that.
[1797.96 --> 1799.42]  So I appreciate that very much.
[1799.62 --> 1800.64]  That was super fascinating.
[1800.82 --> 1804.32]  And I think, as you mentioned, Dave, it's like there's all of these layers.
[1804.32 --> 1809.04]  And of course, you're connecting, you know, to different frameworks that are out there.
[1809.30 --> 1821.74]  It's intriguing to me from like a software development standpoint, like with these frameworks updating and new architectures and operations being added and all of that.
[1821.74 --> 1826.68]  I guess, one, how do you keep up that pace and test like that whole pipeline of things?
[1826.80 --> 1839.22]  Is it a matter of having like reference implementations of all of these different models and essentially running like tests against the compilation of those upon new versions of your framework?
[1839.22 --> 1840.30]  Or how does that work?
[1840.54 --> 1841.42]  Yeah, exactly that.
[1841.60 --> 1842.94]  You know, there's a lot of investment.
[1843.14 --> 1849.36]  Well, one is the development that kind of a lot of software developers and then like a lot of investment in regression system and test infrastructure.
[1849.36 --> 1857.86]  That all has to be done because you have to have a kind of really robust kind of comprehensive software product that there's no way around that to be usable.
[1858.18 --> 1867.42]  And I think to kind of blow by and trump a bit here that I mean, I think Graphcore amongst the kind of raft of AI startups is really well advanced in that space.
[1867.68 --> 1870.26]  All the elements you have for us is like kind of documentation.
[1870.46 --> 1874.62]  You go to our site, you can see the tutorials and documentation, how you do that and so on.
[1874.62 --> 1878.04]  So I think we have to kind of try and keep on top of that.
[1878.04 --> 1881.22]  Keep working internally in Graphcore to keep those questions going.
[1881.58 --> 1885.24]  I think the other thing I would say that kind of really helps with this is being very open.
[1886.00 --> 1892.14]  So making sure that people can document and make sure that people can access.
[1892.60 --> 1895.84]  Well, this is something that you do get on other platforms.
[1896.08 --> 1904.50]  But I think we try and be real leading in this and kind of being able to know what popular the low level Graph compiler kind of explaining that.
[1904.50 --> 1907.72]  Making sure that people can add custom kind of operators in that.
[1907.72 --> 1911.58]  Those libraries I talked about, they're open source on GitHub, that kind of thing.
[1911.64 --> 1917.04]  So trying to make our TensorFlow and PyTorch backends are open source and everything as well.
[1917.16 --> 1924.36]  So by having a more and more open infrastructure, it makes it easier for the community at large to help you adapt to new things as well.
[1924.36 --> 1932.40]  And as we find as we're kind of getting more popular, more people using us, that we kind of get more kind of community involvement like that as well.
[1932.46 --> 1934.14]  And I think that's an important part of it as well.
[1934.14 --> 1949.46]  We deserve a better internet and the Brave team has the recipe for bringing it to us.
[1949.58 --> 1950.58]  Start with Google Chrome.
[1950.82 --> 1954.54]  Keep the extensions, the dev tools, and the rendering engine that make Chrome great.
[1954.74 --> 1955.62]  Rip out the Google bits.
[1955.74 --> 1956.38]  We don't need them.
[1956.74 --> 1959.26]  Mix in ad and tracker blocking by default.
[1959.26 --> 1962.24]  Quick access to the Tor network for true private browsing.
[1962.60 --> 1966.94]  And an opt-in reward system so you can get paid to view privacy-respecting ads.
[1967.12 --> 1970.88]  Then turn around and use those rewards to support your favorite web creators like us.
[1971.20 --> 1975.80]  Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[1989.26 --> 2005.82]  So Dave, I'm curious, as an AI practitioner, one of the things I would love to know from you is as you've spent all of this time making AI programs sort of be sympathetic to a certain architecture and for certain tasks,
[2005.82 --> 2020.12]  do you have any sort of good advice or help for AI practitioners out there in terms of knowing how to tailor our AI programs or models more generally to be efficient for a certain data set or task?
[2020.22 --> 2030.42]  Are there any sort of good advice you have or common challenges or common pitfalls that you see people falling into that could be mitigated with some best practices?
[2030.82 --> 2032.00]  Yeah, it's a really good question.
[2032.00 --> 2038.32]  It slightly depends on whether you're talking about kind of task performance, like how good your model is at a particular task,
[2038.46 --> 2043.72]  or whether you're talking about kind of compute efficiency, kind of, you know, how fast does it run?
[2043.84 --> 2050.92]  In terms of task performance, I think people need to be aware that those two are not kind of islands that are separate.
[2051.48 --> 2057.66]  The architecture you write, whether you're aware of it or not, even if you just like taking what other people do or whatever,
[2057.66 --> 2064.78]  has been kind of affected by the underlying compute platform and what's efficient.
[2064.98 --> 2071.10]  Because if you were kind of trying to study whether a particular kind of model architecture, for example,
[2071.70 --> 2076.66]  got good task performance, but it was really, really slow, then you probably wouldn't like pursue that.
[2076.66 --> 2083.94]  Even though it might be quite a good way of going for if you're just looking at pure task performance independent of how fast it goes.
[2084.62 --> 2087.14]  There have been references to calling this like the hardware lottery, right?
[2087.22 --> 2092.38]  Kind of like what hardware you've got kind of affects kind of how lucky you are being able to explore certain things.
[2092.82 --> 2095.64]  I think it's a good question on practice there, though.
[2095.64 --> 2104.20]  So I think one thing that's useful is just a kind of base understanding of what's going on underneath.
[2104.64 --> 2109.98]  And probably the important things there are, if you're interested in the kind of efficiency, the compute efficiency,
[2110.50 --> 2117.48]  knowing kind of how things like, for example, batch size or kind of certain sizes, axes of your matrices
[2117.48 --> 2120.32]  actually kind of affect the hardware underneath and could be fast or slower.
[2120.32 --> 2126.12]  I think the other thing is being very aware of the floating point behavior of various platforms,
[2126.26 --> 2130.16]  because that can vary a lot between platform and a good platform provider should document that.
[2130.24 --> 2136.66]  And you should be aware of kind of the tools they have to show when things are overflowing or kind of underflowing and so on
[2136.66 --> 2141.62]  to know when you might be losing task performance, not because of the model structure,
[2141.76 --> 2144.92]  but because actually because of the data format they've written there.
[2144.92 --> 2147.88]  And actually we're seeing new techniques coming in to help that actually.
[2147.88 --> 2152.26]  Kind of you'll see things like automatic loss scaling is a really good example.
[2152.64 --> 2156.10]  The software stack and vendors are trying to help there, you know, kind of trying to make things more adaptive
[2156.10 --> 2157.80]  so you don't have to think about those things.
[2158.38 --> 2165.26]  But I think it kind of is worth kind of just having a kind of good kind of surface level understanding
[2165.26 --> 2167.22]  of kind of what's going on under the board of it.
[2167.22 --> 2173.78]  Yeah, Chris, you're probably familiar with Bill Kennedy in the Go world, and maybe you are as well, Dave.
[2173.78 --> 2180.34]  But we spent some time working together and he always in our conversations was talking about this idea of mechanical sympathy
[2180.34 --> 2186.48]  as you're writing code, which I think gets to a lot of what you're saying, Dave, in terms of,
[2186.98 --> 2192.22]  yeah, it's maybe not all software engineers don't have to also be hardware engineers,
[2192.22 --> 2200.12]  but there is an element of like developing a mechanical sympathy for what you're writing for that helps you write
[2200.12 --> 2204.98]  like really robust and good software that I think is really valuable.
[2204.98 --> 2210.34]  Like understanding, you know, in Go it's, you know, understanding like, oh, if I initialize a variable this way,
[2210.34 --> 2216.26]  it actually, you know, does something different than if I initialize a variable this way in terms of the memory that's allocated
[2216.26 --> 2222.56]  and copies that are made and all of those things. So having that sort of knowledge, I think, is really cool.
[2222.62 --> 2225.88]  And it's interesting to hear you talk about it in the context of AI.
[2226.50 --> 2233.30]  I think it's something that I definitely want to develop a little bit better intuition for in my own work, I think.
[2233.88 --> 2238.94]  That segues into what I was going to ask, too. So we're both thinking along the same lines in terms of questions.
[2238.94 --> 2244.44]  And that is, as you've taken us into this and explained kind of that compiler series,
[2244.44 --> 2248.28]  and we've talked about kind of the interface being PyTorch or TensorFlow,
[2249.08 --> 2252.58]  and I know I'm coming at it as a practitioner and as is Daniel,
[2252.82 --> 2257.92]  you have presumably different types of users that need different amounts of that kind of mechanical sympathy,
[2258.14 --> 2263.44]  as Daniel described it from Bill Kennedy, or knowledge of what's under the hood at different levels.
[2263.44 --> 2269.28]  How far do I need to go? Should I learn Poplar? Am I going that far? Am I going beyond that?
[2269.44 --> 2273.78]  What other users, if the answer was no for me, what other users are learning that?
[2274.02 --> 2277.04]  How do you break that out? How do you know who should be addressing what?
[2277.40 --> 2280.58]  Because that's a question we get all the time from many people in this field.
[2280.76 --> 2286.68]  There seems like so much stuff. I don't actually know what to address first and second and third.
[2286.82 --> 2290.14]  So could you break that down a little bit from that end user perspective?
[2290.14 --> 2298.82]  Yeah. It'd be unrealistic to say that everyone needs to become a full stack developer for the full stack being this kind of,
[2299.42 --> 2300.76]  this is incredibly complex.
[2300.88 --> 2302.10]  All the way down through the hardware.
[2302.18 --> 2302.78]  Yeah, yeah, yeah.
[2302.78 --> 2306.18]  I think that's a really rare thing. I mean, you do get people like that.
[2306.30 --> 2308.06]  I've met people like that. They're great.
[2308.74 --> 2312.14]  And you want to hire them, basically, when you see them.
[2312.56 --> 2313.90]  But you're not going to get that.
[2314.10 --> 2317.72]  So I think what we find is it's harder for a sole practitioner.
[2317.72 --> 2323.50]  I think kind of what we find in the companies we work for is they do that by teams, right?
[2323.60 --> 2327.96]  So you have kind of very much a kind of implementation focused team,
[2328.18 --> 2330.58]  a kind of algorithm and ML focused team.
[2330.84 --> 2333.90]  And the challenge there is to make them work kind of hand in hand,
[2334.08 --> 2336.96]  a bit like the co-design thing I was talking about earlier, to work together.
[2337.26 --> 2341.56]  And kind of just being honest about the fact that you're not going to get this all in one person.
[2341.56 --> 2345.92]  I wouldn't kind of suggest that people try and really do that unless they're super,
[2346.00 --> 2347.50]  super interested in all the parts.
[2347.70 --> 2350.46]  You kind of always need to pick where you want to go and so on.
[2350.72 --> 2354.48]  And I think despite what I said about kind of like these lower parts of the stack,
[2354.62 --> 2360.58]  the majority of what I'll call ML scientists or kind of data scientists or stuff like that
[2360.58 --> 2362.56]  don't need to know about those lower level details.
[2362.68 --> 2364.96]  They need to just have some sympathy with it.
[2365.04 --> 2365.78]  And I think that's it.
[2365.84 --> 2368.84]  So kind of just a bit, maybe dabble a bit to kind of understand,
[2368.84 --> 2369.86]  learn a bit about machines.
[2369.86 --> 2371.42]  Don't try and learn it really well.
[2371.78 --> 2374.26]  I mean, and definitely our user base is like that, right?
[2374.30 --> 2378.66]  You might say that maybe about 90% of people are programming at the PyTorch TensorFlow level,
[2379.20 --> 2380.72]  maybe a bit of understanding machine learning.
[2381.10 --> 2383.04]  And you've got a small kind of group.
[2383.18 --> 2386.22]  But those groups are very important for us because what they can do
[2386.22 --> 2393.46]  is they can add new functionality, new capability to a stack or an application
[2393.46 --> 2395.44]  or a framework or something like that.
[2395.46 --> 2398.44]  Actually, maybe this is a case for the people to specialize a bit.
[2398.44 --> 2401.94]  And kind of if you want to be that person that kind of can understand the details,
[2402.36 --> 2403.02]  then do that.
[2403.08 --> 2407.18]  But kind of find good people to work with that understand the higher level and vice versa.
[2407.30 --> 2409.76]  If you kind of really want to understand the machine learning part of it,
[2409.84 --> 2413.62]  have some sympathy, but then maybe find some people to work out either in the community
[2413.62 --> 2418.64]  or kind of set up your kind of professional kind of team structure
[2418.64 --> 2421.66]  to make sure you've got people with those other skills as well.
[2421.90 --> 2423.44]  We kind of have a mix of Graphcore.
[2423.56 --> 2427.10]  So we have some people who are that kind of full stack trying to kind of go up and down it.
[2427.36 --> 2431.58]  Obviously, we're in a bit different position because we're kind of an implementation side of things.
[2431.64 --> 2431.80]  Right.
[2431.80 --> 2435.48]  And then we have kind of people specialized in kind of one end or the other.
[2435.98 --> 2440.88]  So, Dave, I'm interested in, of course, this space is developing rapidly.
[2441.20 --> 2445.88]  And I know, you know, Graphcore and IPUs have been gaining traction.
[2446.52 --> 2448.12]  There's good use cases out there.
[2448.30 --> 2451.74]  And we'll definitely link to some of the materials on your website and all of that.
[2451.74 --> 2457.40]  I'm kind of wondering, as you look to the future, this next year or two years with Graphcore,
[2457.88 --> 2459.28]  where do you see things going?
[2459.46 --> 2463.82]  And what are you excited about seeing in terms of the development of this technology
[2463.82 --> 2467.20]  over the next year or two years as we look to the future?
[2467.60 --> 2469.22]  Gosh, it's very, very hard to pick.
[2469.32 --> 2471.54]  There's an awful lot going on, I think, kind of.
[2471.84 --> 2476.80]  I think the algorithm space will continue to move very quickly.
[2476.80 --> 2480.70]  So I'm very excited to see the fact that we might be doing very different things,
[2480.70 --> 2482.82]  even two years from now, to what we're doing.
[2482.96 --> 2487.48]  So people won't be talking about, wow, look at these kind of ginormous transformer NLP models.
[2487.78 --> 2489.82]  Wow, look at this other thing we've done.
[2490.46 --> 2491.96]  So I think that's very exciting.
[2492.20 --> 2496.34]  I think what's happening in, from a kind of more kind of systems point of view,
[2496.46 --> 2499.46]  I think kind of what's happening in the data center will be very interesting.
[2499.60 --> 2502.38]  The way they're put together, the way to get efficiency,
[2502.38 --> 2507.30]  the kind of the software and the processes and the network will all have to work together.
[2507.78 --> 2510.68]  It's a fascinating space that will evolve, I think, quite quickly.
[2510.70 --> 2511.74]  In the next couple of years.
[2511.98 --> 2517.94]  From a software point of view, I'm interested in how the current frameworks and stacks evolve
[2517.94 --> 2522.96]  as we try and go towards getting more efficiency.
[2523.24 --> 2526.44]  And I guess I'm talking about kind of parameter efficiency here, I suppose.
[2526.88 --> 2528.90]  So that's going to kind of lead to new algorithms.
[2529.24 --> 2530.94]  And I think this is just a personal gut feel.
[2530.94 --> 2531.48]  I don't know.
[2531.62 --> 2532.86]  I don't know this at all here.
[2533.26 --> 2540.16]  But it might be that we kind of are these kind of very linear algebra-based frameworks that we have now,
[2540.22 --> 2542.72]  the ones that have been very popular, the tens of thousands of titles and so on.
[2543.02 --> 2544.00]  Are they the right ones?
[2544.10 --> 2546.22]  I don't think that's a kind of settled thing.
[2546.36 --> 2547.62]  That's very exciting, right?
[2547.70 --> 2550.96]  That there's still that kind of uncertainty about that kind of thing.
[2550.96 --> 2554.78]  There's all kinds of stuff out there about how it's going to grow and scale.
[2555.18 --> 2559.84]  And that's not even talking about the actual applications that are going to come out of this space as well.
[2559.84 --> 2564.22]  So all the way through from top to bottom, there's loads of exciting stuff coming up.
[2564.36 --> 2565.52]  And I'm absolutely sure of that.
[2566.38 --> 2567.18]  Yeah, awesome.
[2567.72 --> 2570.88]  Well, Dave, we really appreciate you joining us.
[2571.32 --> 2572.80]  This is super fascinating.
[2573.00 --> 2575.50]  I'm really excited by what Graphcore is doing.
[2575.68 --> 2578.98]  We'll make sure and link a bunch of links in our show notes for listeners.
[2579.42 --> 2581.52]  Definitely check out what Graphcore is doing.
[2581.70 --> 2587.62]  Read their white paper and all the information about the popular software framework.
[2587.62 --> 2588.40]  It's really cool.
[2588.40 --> 2589.70]  And, of course, the hardware.
[2590.44 --> 2597.22]  And, yeah, I was just really enthused by the conversation and have a lot going on in my mind that I want to think about more.
[2597.42 --> 2598.84]  So I appreciate that.
[2599.28 --> 2600.50]  Thank you for joining us, Dave.
[2600.70 --> 2601.34]  Thank you very much.
[2601.42 --> 2601.92]  It's been a pleasure.
[2602.10 --> 2602.74]  It's been a really good talk.
[2606.66 --> 2608.68]  Thank you for listening to Practical AI.
[2609.02 --> 2611.00]  We appreciate your time and your attention.
[2611.36 --> 2615.70]  Follow the show on Apple Podcasts, Spotify, or your favorite podcast app.
[2615.70 --> 2617.56]  Your neural networks will thank you.
[2617.56 --> 2621.26]  We are also on the web at practicalai.fm.
[2621.52 --> 2626.48]  There you'll find recommended episodes, listener favorites, and a free sign-up to join the community.
[2627.12 --> 2630.48]  Practical AI is hosted by Chris Benson and Daniel Whitenack.
[2630.68 --> 2634.24]  It's produced by Jared Santo with music by Breakmaster Cylinder.
[2634.66 --> 2637.84]  Thanks again to our sponsors, Fastly, Linode, and LaunchDarkly.
[2637.98 --> 2638.80]  That's our show.
[2639.22 --> 2641.94]  We hope you enjoyed it, and we'll talk to you again next week.
[2641.94 --> 2671.92]  We'll see you again next week.
