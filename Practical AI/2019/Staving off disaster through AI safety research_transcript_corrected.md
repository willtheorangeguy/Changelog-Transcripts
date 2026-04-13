[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.38] And we're hosted on Linde cloud servers.
[12.74 → 14.74] Head to linode.com slash changelog.
[15.36 → 18.62] This episode is brought to you by Linde, our cloud server of choice.
[18.82 → 21.88] And we're excited to share they've recently launched dedicated CPU instances.
[22.34 → 28.52] If you have build boxes, CI, CD, video encoding, machine learning, game servers, databases,
[28.52 → 35.78] data mining, or application servers that need to be full duty, 100% CPU all day, every day,
[35.92 → 38.78] then check out Linde's dedicated CPU instances.
[39.34 → 43.44] These instances are fully dedicated and shared with no one else.
[43.52 → 47.46] So there's no CPU steal or competing for these resources with other Li nodes.
[47.72 → 51.40] Pricing is very competitive and starts out at 30 bucks a month.
[51.76 → 55.60] Learn more and get started at linode.com slash changelog.
[55.82 → 57.80] Again, linode.com slash changelog.
[58.52 → 74.12] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[74.50 → 76.22] productive, and accessible to everyone.
[76.60 → 81.14] This is where conversations around AI, machine learning, and data science happen.
[81.22 → 85.88] Join the community and slack with us around various topics of the show at changelog.com slash community.
[85.88 → 87.04] Follow us on Twitter.
[87.16 → 88.64] We're at Practical AI FM.
[88.90 → 89.96] And now onto the show.
[94.62 → 96.66] Welcome to the Practical AI podcast.
[97.16 → 103.20] This is Chris Benson, your co-host, as well as the chief AI strategist at Lockheed Martin RMS APA Innovations.
[103.46 → 108.16] This week, you're going to hear one of a series of episodes recorded in late January 2019
[108.16 → 111.52] at the Applied Machine Learning Days conference in Lausanne, Switzerland.
[111.52 → 117.56] My co-host, Daniel Whiten ack, was going to join me, but had to cancel for personal reasons shortly before the conference.
[117.92 → 119.84] Please forgive the noise of the conference in the background.
[120.30 → 123.10] I recorded right in the midst of the flurry of conference activities.
[123.54 → 129.70] Separately from the podcast, Daniel successfully managed the AI for Good track at Applied Machine Learning Days from America,
[130.16 → 131.24] and I was one of his speakers.
[131.80 → 134.46] Now, without further delay, I hope you enjoy the interview.
[134.46 → 145.64] My guest today is Elma al-Ghamdi, and he is a PhD student who's just finishing up here at EPFL in Switzerland,
[145.64 → 151.26] and he has been focusing on technical AI safety and robustness in biological systems.
[151.80 → 154.70] Welcome to the show, and did I actually say your name correctly?
[155.06 → 155.94] That was good.
[156.42 → 160.72] And if you could start us off, we've talked a little bit before we started recording.
[160.72 → 165.74] You have a fascinating background. Will you share a bit of that as we start this off with the listeners?
[166.38 → 168.56] I've been trained as a physicist.
[169.34 → 171.80] So I did math and physics as a bachelor's in Morocco.
[172.54 → 174.34] Then moved to France, Switzerland, and Germany.
[174.88 → 178.26] But I've been trained as a physicist. I even worked in physics research.
[178.40 → 182.16] I've been a research engineer in physics, the physics of condensed matter,
[182.28 → 188.06] like semiconductors for things like photovoltaics, solar cells.
[188.06 → 194.36] But then I drifted a bit for about five years before coming back for a PhD.
[195.04 → 201.12] So I started, like, I did research in physics, but then I, at the same time, with some friends,
[201.40 → 204.42] we co-founded a media platform in Morocco called Mafeking,
[205.36 → 213.78] which was some sort of like a news aggregate during the 2011 events that some people called the Arab Spring.
[213.78 → 225.76] And during that period, I was more and more convinced that the web was enabling, through those platforms,
[226.50 → 233.68] tools to help people circumvent usual intermediate bodies, like electoral political parties,
[234.44 → 237.94] established news organizations, to self-organize.
[237.94 → 244.94] But at the same time, there was a harmful effect, which we will start being more aware of five years later,
[245.06 → 249.18] during the last events in the US, for example.
[249.32 → 254.24] And would that be misrepresentation of events like fake news and that kind of thing are you referring to?
[254.50 → 254.80] True.
[254.80 → 260.80] And so back then, 2011, 2012, there was another thing that caught my attention,
[261.36 → 266.90] which was that whenever we put a lot of effort, me and my colleagues at Mafeking,
[267.36 → 275.06] would put a lot of effort in doing a deep investigative work on some very relevant public issue
[275.06 → 282.98] and then publish it, the readership would be very low compared to a three-minute video
[282.98 → 290.26] by some activists who just self-record himself or herself with a basic camera
[290.26 → 294.64] and then start speaking in a very simple word and it will take off.
[294.98 → 301.24] And back then, 2012, say, I kind of stopped being very involved in Mafeking.
[301.24 → 302.82] I was still working in physics, by the way.
[303.66 → 310.66] But I thought that the video platforms will play an even increasing role
[310.66 → 316.02] as the bandwidth and access to heavy content like video will be democratized.
[316.94 → 324.66] And I said, yeah, okay, so the video sharing seemed to be more powerful than text sharing on the web.
[324.82 → 330.60] I think this can help a lot into something that also I care about,
[330.60 → 332.00] which is science education.
[335.08 → 341.98] As much as videos on political issues would have more spread than text,
[342.68 → 347.36] I thought that videos on science would have a general audience for kids
[347.36 → 350.82] to make kids motivated about science or just to tutor people.
[351.48 → 353.10] I was not aware of the Khan Academy back then.
[353.50 → 356.28] Someone showed me Khan Academy after I did my first videos.
[356.28 → 366.14] And so I said, good, okay, I will start a video project that would just do tutoring in physics and math.
[366.24 → 371.66] Something I was kind of good at doing, which is tutor people in math and physics.
[372.00 → 378.66] So I started a tutoring project in math and physics while working in condensed matter physics back then.
[378.66 → 390.64] But then a professor here in computer science, Rashid Farragut, convinced me to join efforts and to do that full time with him here in Lausanne.
[390.76 → 393.92] So we got initial funding from Google and from the faculty.
[394.14 → 400.88] Then the faculty, of course, like the faculty took over the funding, and we got enough funding to do it full-time.
[400.88 → 416.20] And I started learning about computer science as a fundamental science and was realizing how epistemologically relevant computability and concepts like decidability were to understand.
[416.72 → 418.88] And about when was that just for the timeline?
[419.04 → 423.26] And from 2011, 2012, this would have been moved on another year or so?
[423.26 → 425.14] This transition would happen in 2013.
[425.14 → 434.24] So in 2013, I left my job as a physicist engineer, came to Lausanne by the mid-June, I think, June 2013.
[434.62 → 445.58] I left my job as a research engineer in physics and came to Lausanne to fully start this tutoring project that became an official tutoring platform of EPFL.
[445.58 → 448.38] So bachelor students, we had like a very good reception.
[448.38 → 456.66] It's not like the kind of YouTube channel that would go popular because it's on very specific and technical topics, and it's in French.
[456.96 → 460.48] Most of the content is in French because EPFL is a French-speaking university.
[460.82 → 463.30] So the audience was not huge.
[463.38 → 465.32] It's a small-sized audience, but there was a high quality.
[465.38 → 468.78] For example, we had a high retention rate compared to say Moons.
[468.78 → 474.82] Like MOOC platforms, they had an 8% or 7% retention rate.
[474.82 → 479.86] We had something close to 70% retention rate because it was a tutoring.
[480.10 → 490.20] So we were addressing questions bachelor students of EPFL would struggle on before an exam, like how to compute this third derivative of this physicist stuff, whatever object.
[490.70 → 494.50] So that really does sound quite a lot like Khan Academy and what you were doing.
[494.62 → 497.90] Obviously, you're doing it in French and doing it for the students here.
[498.42 → 502.44] So we can kind of think of it in that kind of context and where you're going.
[502.44 → 504.72] And so where did that lead you?
[505.50 → 511.72] Because I was funded by the computer science department, it led me to learn more about computing.
[512.66 → 523.14] So back then when I was trained as a physicist, I viewed computer science as this engineering thing where you debug Java and C++ code.
[523.14 → 525.48] I didn't like it really.
[525.48 → 531.32] But I was not aware, and I was not educated on this fundamental science of computing.
[532.28 → 535.30] And little by little, I started educating myself.
[536.10 → 537.10] I started learning, learning.
[537.20 → 538.38] I started learning, learning.
[538.54 → 538.96] That's so meta.
[538.96 → 548.68] So I started reading about learning theory, the work of Leslie Valiant, for example, the work of Vapid, Hero Benches, and also the fundamental CS part, like Turing.
[548.68 → 557.74] And I kind of buy into a few calls, for example, from Leslie Valiant to make computing a natural science.
[557.74 → 568.58] I think it's a very powerful epistemological tool to understand natural phenomena in terms of like, I'd like to call computing as the science of the feasible.
[568.58 → 572.24] Like, what can be done, like complexity theory.
[572.46 → 575.10] What can be done in an amount of time with an amount of resource.
[575.66 → 579.90] And I'd like to view learning theory as the science of the learnable.
[580.12 → 585.54] What can be learned given an amount of time and an amount of data points and an amount of samples.
[586.22 → 587.02] And I love that.
[587.10 → 594.72] So I wrote a proposal to start a PhD trying to understand biological processes with computability tools.
[594.72 → 602.48] Not as a computer scientist collaborating with biologists and like coding stuff for them.
[603.06 → 605.76] But not bringing the engineering part of CS.
[606.04 → 614.28] Bringing the epistemological part of CS that view complex systems through complexity theory, resource, etc.
[615.02 → 621.36] And the main guiding line was robustness.
[621.36 → 628.16] So could we explain robustness in biological processes with computational tools?
[628.88 → 644.22] So could we explain, for example, why an ant colony is robust to randomly killing some of the ants up to a certain level without having a central authority allocating tasks and telling ants,
[644.22 → 648.82] oh, by the way, we had a certain amount of foragers that died.
[649.16 → 653.52] Yeah, those of you who are doing, I don't know, nursing should switch to foraging.
[654.10 → 660.10] And we know, like, myrmecologists, biologists who study ants know that there is no central authority doing that.
[660.22 → 662.20] Like, it's self-organized and it's robust.
[662.34 → 663.12] It's fault-tolerant.
[663.64 → 669.62] The brain also is a very good example of a robust structure where there's no central authority telling neurons what to do.
[669.62 → 676.02] Or to a certain extent, it's very distributed and robust, and it can tolerate the loss of some of the nodes.
[677.00 → 678.88] So that was the starting line.
[679.36 → 690.66] Let's understand the fault tolerance of biological processes with tools from algorithmic theory and this kind of tools.
[690.78 → 692.88] And this is in the distributed computing group.
[692.88 → 701.18] So that was like a very physics-y, so that was something that could bring the physicist in me again to like and like doing research.
[701.84 → 704.08] Five years after I left my master's.
[705.24 → 719.30] But little by little, I was, just my awareness on more applied aspects of machine learning will grow.
[719.30 → 723.32] So I was like, I told her, I was trying to understand, like, fault tolerance in neural networks.
[723.74 → 730.48] So how does error propagate in a neural network when some of the neurons are removed?
[731.16 → 733.28] This is, today, this is not a practical problem.
[733.60 → 738.62] Because neural networks, like neural networks, neurons in neural networks do not fail.
[739.26 → 744.66] A neural network is simulated in a machine, so the unit of failure is a whole machine, not a single neuron.
[744.66 → 749.02] This will become a problem when we will have xeromorphic hardware, if you heard about this.
[749.58 → 752.14] Could you define what that is specifically?
[752.60 → 757.64] Xeromorphic hardware is a class of hardware that is itself built as a neural net.
[757.86 → 764.20] So the hardware itself contains pieces that behave like a neuron and pieces that behave like a synapse,
[764.94 → 768.04] while today we just simulate neural networks as a software.
[768.04 → 774.64] So would it be fair to say, then, that because you are implementing hardware in the form of a neural network,
[774.74 → 779.14] that you can have, just like any other machine out there, you can have parts of the machine fail,
[779.46 → 784.30] and therefore, unlike today, where it's just software and you either have it's all working or it's not,
[784.62 → 788.16] you can have parts of that hardware in the form of a neural network fail,
[788.30 → 792.22] and therefore, it's a new problem for us to solve, which is why you were saying it's not practical?
[792.58 → 793.84] Am I understanding you correctly?
[793.84 → 795.18] It's not a really new problem.
[795.32 → 800.80] It was a very popular problem in the 90s and 80s, before the last AI winter,
[800.90 → 805.82] because people were expecting xeromorphic hardware to arise the next day.
[806.40 → 811.82] So people, like, you find a lot of papers in the 80s, 90s about fault tolerance in neural nets,
[811.82 → 815.16] and they will talk about VLSI circuits, very large.
[815.88 → 819.00] But then xeromorphic hardware didn't happen,
[819.00 → 822.90] and we simulate neural nets on machines,
[823.10 → 825.06] and people stopped caring about this problem.
[825.90 → 828.70] But, yeah, I find it a very good physics,
[829.66 → 835.64] I find it a very good problem for someone who thinks like a physicist like me.
[836.00 → 841.66] So I cared about it, even though there's no normal hardware room in the air today.
[842.28 → 845.54] But little by little, people who are relevant in machine learning would tell me,
[845.60 → 847.30] yo, look, we don't care about this yet.
[847.30 → 855.18] Though, yeah, if you could understand how error impacts learning in distributed frameworks,
[855.44 → 859.48] like when we train machine learning systems over a set of machines,
[860.06 → 861.66] that might be relevant today.
[861.92 → 863.38] So I switched a bit of interest.
[863.58 → 868.10] I published a paper on, like, I approved some bounds on error propagation in neural nets.
[868.10 → 874.04] The mathematical modelling I did there was also useful to study biomolecular networks
[874.04 → 876.12] with some friends from the Johns Hopkins Medical School,
[876.48 → 881.30] because it turns out that biomolecular networks are just weighted graphs of nonlinear nodes,
[881.62 → 882.58] just like neural nets.
[882.82 → 885.10] Oh, no, that's pretty cool. I had never thought of it that way.
[885.10 → 890.78] Okay, so I know that you, I was going to ask you that,
[890.86 → 894.50] was that you had talked about that activity that you were dealing with the robustness
[894.50 → 897.00] in biological systems with the technical AI safety.
[897.20 → 898.74] And is that the crossover there?
[898.96 → 901.36] Are we getting to that, or am I jumping in?
[901.62 → 903.72] Not yet, but the glue is already there.
[903.78 → 904.80] The glue is fault tolerance.
[904.80 → 908.74] So there are, like, two hemispheres in my PhD.
[909.04 → 912.14] One hemisphere was doing robustness in biological systems,
[912.54 → 914.74] and one hemisphere was doing technical AI safety.
[914.98 → 918.88] They don't seem to be related, but they are actually true fault tolerance.
[919.02 → 920.32] So I cared about fault tolerance.
[920.44 → 924.10] What happens in a complex system when some nodes are knocked out,
[924.38 → 928.02] or, like, are misbehaving, or are lying to the group?
[928.62 → 930.60] Oh, okay there. So you've gotten to the crux of it.
[930.60 → 933.38] I know that as we were talking when we first met,
[933.38 → 935.50] and you started talking about that,
[935.90 → 938.90] I can't wait to hear how this goes in,
[938.98 → 944.50] because it's fascinating how you've pulled together multiple fields
[944.50 → 947.88] that may not be obviously related up front, but through fault tolerance.
[948.46 → 952.60] And then you were making comments earlier about how this affects things like fake news
[952.60 → 955.20] and falsified information that goes forward.
[955.78 → 956.74] So take us there.
[957.24 → 961.66] Let's go to the more technical AI safety part of my research.
[961.66 → 966.16] I like to tell this, like, when I say to my friends,
[966.36 → 968.28] oh, now I'm like, yeah, for the past two years,
[968.38 → 971.24] I switched a bit of interest, I'm caring about technical AI safety,
[971.80 → 973.48] they would go like this.
[973.92 → 976.42] Oh, yeah, isn't this about killer robots,
[976.88 → 978.36] and rogue self-driving cars,
[978.46 → 980.22] and things we'll have in the far future?
[982.12 → 987.62] And I think partly because the media was always showing this kind of motivations,
[987.62 → 989.30] when they talk about AI safety.
[990.06 → 994.52] I always like to tell them that there are killer robots already about us,
[994.56 → 998.06] they're very dumb and primitive and doing very basic machine learning,
[998.18 → 999.64] and they're called recommender systems.
[1000.50 → 1001.20] That's great.
[1001.66 → 1005.56] But you'll have to kind of explain what you mean by that,
[1005.62 → 1007.26] because that's a little bit of a shocker when you hear that.
[1007.26 → 1011.16] So imagine a young couple of parents who just had a kid,
[1011.90 → 1017.16] and then they go to a search engine and type
[1017.16 → 1022.32] medical advice on vaccines for young kids.
[1022.96 → 1027.32] And then they got an initial piece of content
[1027.32 → 1029.98] that tells them that this is harmful,
[1030.26 → 1031.24] it can cause autism,
[1031.60 → 1033.14] and then their kids can die,
[1033.14 → 1035.60] and this is really a conspiracy by big pharma
[1035.60 → 1037.96] to make us just buy their products.
[1038.80 → 1042.50] And then the platform recommend them another video
[1042.50 → 1044.30] telling them similar stuff,
[1044.58 → 1047.28] and another one, and another one, and another one.
[1047.86 → 1049.90] And actually that could also happen to people
[1049.90 → 1051.66] who didn't even search for that,
[1051.86 → 1055.40] just looking for medical advice on some random topic,
[1055.52 → 1056.36] for hairpiece.
[1056.88 → 1058.90] And then they end up on a video telling them,
[1059.04 → 1060.64] oh, there's this big pharma conspiracy,
[1060.84 → 1062.20] don't take your kids for vaccine.
[1062.20 → 1064.40] So it's funny that you say that,
[1064.44 → 1066.64] because I actually have friends
[1066.64 → 1069.10] and even extended family members
[1069.10 → 1072.54] that that exact use case has applied for them,
[1072.58 → 1074.54] and we have gotten into debates
[1074.54 → 1077.34] on the benefit of vaccine.
[1077.68 → 1081.10] And so I love the fact that, you know,
[1081.22 → 1084.84] you started in kind of from that academic perspective,
[1084.84 → 1086.76] but you're now touching on something
[1086.76 → 1088.24] that affects lives every day
[1088.24 → 1090.66] by millions of people out there,
[1090.66 → 1092.04] and it's a very common misconception.
[1092.48 → 1093.68] So I love the fact that,
[1093.68 → 1094.70] where are you going?
[1094.78 → 1095.10] Keep going.
[1095.22 → 1095.72] Sorry about that.
[1095.90 → 1098.76] Now today, you know, just this year,
[1099.36 → 1102.44] I think for the first time in maybe several years,
[1103.68 → 1104.44] I don't know how much,
[1104.60 → 1106.54] but like for the first time
[1106.54 → 1108.70] in at least the past five years or so,
[1109.22 → 1111.34] the World Health Organization listed
[1111.34 → 1115.82] a vaccine hesitancy as a public health issue.
[1115.82 → 1117.74] So it is listed,
[1118.04 → 1119.52] I'll give you the reference after the
[1120.12 → 1120.98] it is listed,
[1121.38 → 1123.38] so you can give the link to the audience.
[1123.78 → 1125.10] Yeah, we'll include that in the show notes.
[1125.60 → 1127.12] So the World Health Organization
[1127.12 → 1130.60] listed vaccine hesitancy in its 2019 report
[1130.60 → 1131.98] on the measure,
[1132.50 → 1135.22] like it's now in the rank of HIV and Ebola,
[1135.22 → 1139.72] because there is a surge of anti-vaccine resentment
[1139.72 → 1142.44] and there is a surge of vaccine preventable diseases.
[1143.44 → 1146.72] Some estimations I remember from that report,
[1146.82 → 1149.00] you can maybe check if I like,
[1149.06 → 1150.10] I might miss some details,
[1150.20 → 1151.02] but for example,
[1151.08 → 1155.06] there is a surge of 30% in measles
[1155.06 → 1157.10] in developed countries.
[1157.10 → 1157.96] I'm not talking about,
[1158.06 → 1160.16] I'm not talking about like countries that solved,
[1160.42 → 1161.38] that's used to solve that.
[1161.86 → 1162.76] Measles, 30%.
[1162.76 → 1165.16] There are some other reports who speak about,
[1165.16 → 1169.78] about 1,600 deaths in the US per year
[1169.78 → 1172.38] from vaccine preventable diseases.
[1172.86 → 1173.78] That's three per day,
[1174.02 → 1174.96] that's like more than terrorism.
[1175.92 → 1178.32] So this is a less reliable report,
[1178.40 → 1180.52] but like the World Health Organization one
[1180.52 → 1183.68] is talking about a 30% surge of measles.
[1183.96 → 1185.94] That's a vaccine preventable disease.
[1187.12 → 1189.16] And the resentment is growing.
[1189.48 → 1192.00] There were also studies on the people's opinion
[1192.00 → 1194.84] on vaccines in France today and 10 years ago,
[1194.96 → 1199.34] and they consistently show a growth of this resentment.
[1199.70 → 1201.80] So this is clearly a public health issue.
[1202.64 → 1205.52] And we can say with confidence that,
[1205.92 → 1208.28] yeah, poisoned machine learning already kills.
[1208.78 → 1210.50] People think about killer robots.
[1210.92 → 1211.88] I'd like to tell them,
[1212.44 → 1214.10] let's just first care for,
[1214.34 → 1218.26] let's care about poisoned recommender systems.
[1218.26 → 1220.86] And probably what we will do to solve that
[1220.86 → 1223.66] might probably help in preventing something in the long term.
[1223.92 → 1226.94] People tend to think about killer robots in the long term
[1226.94 → 1229.66] and far future stuff we shouldn't worry about too much.
[1231.26 → 1232.50] I'd like to reply,
[1232.86 → 1234.44] I'd always like to reply that,
[1234.66 → 1239.48] no, no, we should care about killer recommender systems
[1239.48 → 1243.36] that are pushing parents into not vaccinating their kids.
[1243.36 → 1245.44] There are surges of cases like measles,
[1245.44 → 1246.22] not only in the US,
[1246.30 → 1247.14] in Switzerland here,
[1247.34 → 1248.76] there was a case last year,
[1248.82 → 1252.40] there was an outbreak in the primary school,
[1252.50 → 1253.06] I think, or a kindergarten.
[1253.36 → 1254.18] So in Mors,
[1254.32 → 1255.58] I think you can search for that,
[1255.62 → 1256.98] in this region,
[1257.14 → 1257.76] Lausanne region.
[1258.56 → 1260.42] And this is a serious problem
[1260.42 → 1262.78] that is literally already killing some people.
[1263.70 → 1264.92] I think new generations
[1264.92 → 1266.88] who didn't witness the past,
[1267.00 → 1268.90] like my generation didn't see
[1268.90 → 1271.52] what does a non-vaccination past look like.
[1271.52 → 1273.32] I'm from Morocco,
[1273.34 → 1274.86] I grew up in Morocco until I was 21.
[1275.10 → 1276.72] My aunt had polio,
[1276.88 → 1278.18] she was handicapped for life.
[1278.54 → 1279.54] She was born in the 50s
[1279.54 → 1280.96] and she was not vaccinated back then.
[1281.18 → 1283.58] So I could see what a non-vaccinated past looked like.
[1283.66 → 1285.46] I think it was even uglier than what I could see
[1285.46 → 1286.84] because I just saw the survivors.
[1287.80 → 1289.70] And I think that my generation in the West
[1289.70 → 1292.26] is not aware of how lucky we are today.
[1293.24 → 1295.66] And recommender systems today
[1295.66 → 1297.48] as they maximize watch time.
[1297.48 → 1299.88] So, yeah,
[1300.04 → 1300.78] the problem is that
[1300.78 → 1303.30] when we maximize for some metric,
[1303.52 → 1306.32] we tend to screw stuff in other metrics.
[1307.14 → 1308.40] Maybe maximizing watch time
[1308.40 → 1311.48] is now leading to what we do today.
[1311.80 → 1314.84] So how could we turn that
[1314.84 → 1317.68] into formalizable scientific questions?
[1317.68 → 1321.30] If you look at machine learning today,
[1321.60 → 1324.12] if you look at how it is done,
[1324.80 → 1326.34] you would find that fundamentally,
[1327.46 → 1331.52] there is an averaging mechanism.
[1332.02 → 1334.20] So when you do gradient descent,
[1334.94 → 1337.22] that's just a protocol to update parameters.
[1339.28 → 1341.68] That's just a protocol to update parameters.
[1341.68 → 1346.90] Okay, you do it thanks to some data points.
[1347.02 → 1348.42] So you leverage some data points,
[1348.56 → 1350.54] you compute gradients using those data points,
[1350.62 → 1352.40] and then you aggregate those gradients.
[1353.42 → 1354.76] And how it is done today,
[1354.90 → 1357.34] it's mostly with averaging those gradients
[1357.34 → 1358.58] or variants of averaging.
[1359.96 → 1362.34] If you ask a sociologist about averaging,
[1363.72 → 1365.50] like, would you do average
[1365.50 → 1367.38] to do socioeconomic of a region?
[1367.62 → 1370.18] Any reasonable sociologist would tell you,
[1370.18 → 1372.20] please don't take the average.
[1373.34 → 1375.00] As a funny illustration,
[1375.52 → 1376.70] and I mean, it's not hilarious,
[1376.78 → 1377.48] but it's a bit sad.
[1378.94 → 1379.96] Always in my talks,
[1380.08 → 1382.10] I ask people who think
[1382.10 → 1384.00] that the GDP per capita
[1384.00 → 1387.16] in Finland, Denmark, and Sweden
[1387.16 → 1390.12] is higher than the GDP per capita in the US.
[1391.52 → 1393.50] Most people in the room raise their hand
[1393.50 → 1395.02] because they think that the GDP per capita
[1395.02 → 1397.58] in Sweden, Finland, and Denmark is higher.
[1398.00 → 1398.78] Actually, that's the opposite.
[1398.78 → 1400.62] It's slightly higher in the US.
[1401.16 → 1402.74] So I know that I was one of those people
[1402.74 → 1403.48] you're referring to.
[1403.54 → 1404.90] I would have said the other way around.
[1405.56 → 1406.30] It's interesting.
[1406.42 → 1407.54] I did not realize that.
[1407.94 → 1408.22] Yeah, yeah.
[1408.74 → 1410.54] You have even more striking cases.
[1410.82 → 1412.46] Like, you can take the GDP per capita
[1412.46 → 1416.46] in Germany and the US
[1416.46 → 1417.58] or something like that,
[1417.62 → 1419.10] and you would find that the one in the US
[1419.10 → 1420.12] is way higher, I think.
[1420.48 → 1421.28] But for sure,
[1421.42 → 1423.06] like Denmark, Finland, and Sweden
[1423.06 → 1424.48] have GDP per capita
[1424.48 → 1426.60] according to the last OECD
[1426.60 → 1428.08] or CIA reports.
[1428.96 → 1430.46] Slightly lower than the one in the US,
[1430.58 → 1434.06] but no one is full enough
[1434.06 → 1437.62] to say that the typical Swedish citizen
[1437.62 → 1442.76] has the poorest life
[1442.76 → 1443.92] or a comparable life
[1443.92 → 1445.74] to a typical US citizen.
[1445.84 → 1447.88] Unfortunately, the typical US citizen
[1447.88 → 1452.28] tends to have less access
[1452.28 → 1454.30] to public education, healthcare, etc.
[1455.20 → 1455.64] Why?
[1455.74 → 1457.12] Because averaging is not robust.
[1457.54 → 1458.30] If you take the average
[1458.30 → 1459.28] and you have a bunch of
[1459.28 → 1461.30] overrich billionaires
[1461.30 → 1463.14] and several homeless people,
[1463.86 → 1465.36] yeah, the average might be good.
[1466.64 → 1469.56] I come from a country
[1469.56 → 1470.28] where this is also...
[1471.72 → 1473.54] I think when I meet a Moroccan
[1473.54 → 1474.22] and an Algerian,
[1474.38 → 1476.22] so we have a neighbouring country
[1476.22 → 1476.88] called Algeria,
[1476.88 → 1480.04] and if you ask any educated Moroccan
[1480.04 → 1481.28] or Algerian in Europe,
[1482.14 → 1483.18] where do you think
[1483.18 → 1487.14] the median,
[1487.26 → 1487.86] not this time,
[1488.02 → 1489.64] the median income,
[1489.92 → 1490.62] access to healthcare
[1490.62 → 1491.72] or whatever is higher,
[1492.18 → 1493.22] they would tend to say Morocco.
[1494.08 → 1494.66] Because there's like,
[1494.82 → 1495.76] because there's like
[1495.76 → 1500.16] this big outlying cities
[1500.16 → 1501.76] like Rabat and Casablanca
[1501.76 → 1504.32] where you see fancy constructions
[1504.32 → 1506.86] and very good cars
[1506.86 → 1508.38] on the road
[1508.38 → 1509.38] and think that,
[1509.48 → 1509.56] yeah,
[1509.58 → 1510.94] this country seems to be
[1510.94 → 1512.28] a bit richer than Algeria,
[1512.36 → 1513.16] but it turns out
[1513.16 → 1514.06] that's not the case.
[1514.60 → 1516.00] The median Algerian
[1516.00 → 1516.88] has a better life
[1516.88 → 1517.86] than the median Moroccan,
[1518.12 → 1519.50] but Morocco has
[1519.50 → 1520.86] a bunch of outliers
[1520.86 → 1522.26] that think of themselves
[1522.26 → 1524.40] as a middle class
[1524.40 → 1525.04] while they are not.
[1525.48 → 1526.12] So sociologists,
[1526.24 → 1526.80] like short story,
[1527.30 → 1528.64] sociologists were aware
[1528.64 → 1529.68] of the weakness
[1529.68 → 1530.40] of averaging
[1530.40 → 1531.48] from at least
[1531.48 → 1532.72] the 19th century.
[1532.72 → 1533.94] if you read
[1533.94 → 1534.70] Emile Durkheim
[1534.70 → 1535.00] or,
[1535.40 → 1535.62] yeah,
[1535.74 → 1536.40] like if you read
[1536.40 → 1536.62] the
[1536.64 → 1536.84] oh no,
[1536.88 → 1537.04] sorry,
[1537.16 → 1537.24] yeah,
[1537.26 → 1537.46] Weber,
[1538.00 → 1539.62] the first data scientists
[1539.62 → 1541.02] who are probably sociologists
[1541.02 → 1543.12] and they were aware
[1543.12 → 1543.82] of this problem
[1543.82 → 1545.96] and they will tell you,
[1546.02 → 1546.12] yeah,
[1546.20 → 1547.40] like take the salaries,
[1547.62 → 1548.06] rank them,
[1548.16 → 1548.68] take the one
[1548.68 → 1549.74] that splits the distribution
[1549.74 → 1550.52] into halves.
[1551.10 → 1552.14] That could be
[1552.14 → 1553.38] a better way
[1553.38 → 1554.60] to evaluate a country
[1554.60 → 1555.96] than taking the average.
[1556.44 → 1557.54] So if you do that...
[1557.54 → 1558.22] I see what you're saying
[1558.22 → 1558.62] on that.
[1558.98 → 1560.12] And I was going to ask you
[1560.12 → 1560.96] how that,
[1561.06 → 1561.64] how that,
[1561.74 → 1562.78] the weakness of averages
[1562.78 → 1564.16] were kind of tying back in
[1564.16 → 1565.54] to the use case
[1565.54 → 1566.28] that you're addressing there.
[1566.40 → 1566.86] So now,
[1567.00 → 1567.12] yeah,
[1567.24 → 1568.62] a naive idea is said,
[1568.66 → 1568.76] yeah,
[1568.76 → 1569.70] let's port that
[1569.70 → 1570.44] into machine learning.
[1570.58 → 1572.34] Let's take median gradients
[1572.34 → 1573.82] instead of average gradients.
[1574.48 → 1575.84] So people behave
[1575.84 → 1576.82] on a social network,
[1577.22 → 1577.94] their behaviour
[1577.94 → 1579.04] create gradients.
[1579.52 → 1580.70] What's happening today
[1580.70 → 1582.16] is that this social network
[1582.16 → 1584.38] will use the average gradients
[1584.38 → 1586.10] to update the model.
[1586.10 → 1588.28] If there is a minority
[1588.28 → 1589.90] of hyperactive,
[1590.22 → 1591.74] hyper-motivated extremists,
[1592.00 → 1593.70] they might screw
[1593.70 → 1594.90] the recommender system.
[1595.72 → 1596.54] So this is,
[1596.62 → 1597.64] so to tie this back in,
[1597.68 → 1597.78] I mean,
[1597.82 → 1598.54] this is exactly
[1598.54 → 1599.42] what we're seeing
[1599.42 → 1601.24] day in and day out,
[1601.32 → 1601.76] you know,
[1601.84 → 1602.98] with the impact
[1602.98 → 1603.60] of social media
[1603.60 → 1604.52] negatively
[1604.52 → 1605.42] on our lives.
[1605.62 → 1607.06] So it's fascinating
[1607.06 → 1608.80] as you've kind of come in
[1608.80 → 1610.62] through this academic path
[1610.62 → 1611.16] that you've taken,
[1611.32 → 1612.80] but you've landed squarely
[1612.80 → 1613.20] in the middle
[1613.20 → 1614.48] of a gigantic problem
[1614.48 → 1616.42] that we're facing
[1616.42 → 1617.18] around the world.
[1617.32 → 1618.80] I know as a U.S. citizen,
[1619.34 → 1620.58] we are having a lot
[1620.58 → 1621.62] of a political conversation
[1621.62 → 1622.06] right now
[1622.06 → 1623.32] around exactly this.
[1623.40 → 1624.54] So what are the implications
[1624.54 → 1625.02] of this?
[1625.28 → 1626.56] The implications might be,
[1626.64 → 1627.04] for example,
[1627.18 → 1628.10] what happened last year
[1628.10 → 1628.98] with the Crisis Acts
[1628.98 → 1629.62] for Conspiracy.
[1630.00 → 1630.76] So I don't know
[1630.76 → 1631.22] if you remember,
[1631.50 → 1632.88] there was this very sad
[1632.88 → 1634.16] shooting in Florida
[1634.16 → 1634.92] in the Parkland
[1634.92 → 1636.60] in that high school.
[1637.32 → 1638.98] And a few survivors
[1638.98 → 1639.88] of that shooting,
[1640.12 → 1640.80] David Hogg,
[1640.86 → 1641.42] Emma Gonzalez,
[1641.92 → 1642.34] and others,
[1643.00 → 1644.36] they raised to prominence
[1644.36 → 1645.68] with their campaign
[1645.68 → 1649.34] promoting more safety measures
[1649.34 → 1650.46] and gun control measures
[1650.46 → 1651.36] that would protect
[1651.36 → 1652.54] high schools
[1652.54 → 1653.06] from shootings.
[1653.72 → 1655.10] And there was a video
[1655.10 → 1656.02] claiming
[1656.02 → 1657.72] that those kids
[1657.72 → 1659.40] are not real survivors
[1659.40 → 1660.82] from the shooting.
[1661.38 → 1663.12] They were crisis actors
[1663.12 → 1666.58] used
[1666.58 → 1668.30] to promote
[1668.30 → 1669.18] gun control
[1669.18 → 1669.76] on television.
[1670.52 → 1671.50] And this video
[1671.50 → 1673.64] went on the front page
[1673.64 → 1675.12] of YouTube.
[1675.12 → 1676.40] So basically,
[1676.58 → 1677.20] you're talking about
[1677.20 → 1677.90] an instance of
[1677.90 → 1679.42] pure fake news
[1679.42 → 1680.84] in terms of
[1680.84 → 1681.56] you're having
[1681.56 → 1682.48] a bad actor
[1682.48 → 1684.24] that is creating
[1684.24 → 1684.84] a fiction
[1684.84 → 1686.78] to serve therein
[1686.78 → 1687.52] from,
[1687.96 → 1689.06] just to serve therein,
[1689.10 → 1690.34] had no basis in reality.
[1690.74 → 1691.58] But it doesn't end
[1691.58 → 1692.42] on the video
[1692.42 → 1695.00] and being featured
[1695.00 → 1695.50] and say,
[1695.56 → 1696.10] if you went to
[1696.10 → 1696.82] YouTube.com
[1696.82 → 1697.54] that day,
[1697.72 → 1698.62] you would find
[1698.62 → 1698.98] this video
[1698.98 → 1699.54] in the US.
[1699.72 → 1700.70] That was the featured
[1700.70 → 1701.80] video on the front page.
[1701.80 → 1703.68] But it didn't end there.
[1704.00 → 1704.88] Those kids received
[1704.88 → 1705.36] death threats
[1705.36 → 1706.52] because people
[1706.52 → 1708.60] believed the video.
[1708.72 → 1710.02] The video spread.
[1710.62 → 1710.92] It was,
[1712.04 → 1713.22] it became very popular
[1713.22 → 1714.20] and the spread
[1714.20 → 1714.66] was done.
[1715.12 → 1715.66] Even though
[1715.66 → 1716.58] YouTube apologized.
[1716.58 → 1717.70] So YouTube apologized,
[1717.82 → 1718.24] of course,
[1718.54 → 1719.00] later.
[1719.52 → 1720.28] And they fixed
[1720.28 → 1720.90] the problem.
[1722.56 → 1723.58] But it was too late.
[1723.70 → 1723.80] Like,
[1723.84 → 1724.56] the harm was done.
[1724.92 → 1726.24] The kids received
[1726.24 → 1726.78] death threats.
[1726.78 → 1729.52] And imagine
[1729.52 → 1730.20] you are surviving
[1730.20 → 1730.64] a shooting
[1730.64 → 1731.48] and then you receive
[1731.48 → 1732.00] death threats.
[1732.40 → 1733.22] Because people
[1733.22 → 1734.20] massively saw
[1734.20 → 1734.68] a video
[1734.68 → 1735.52] saying that
[1735.52 → 1736.00] you are
[1736.00 → 1737.68] a crisis actor
[1737.68 → 1739.10] going to the television
[1739.10 → 1740.52] to promote
[1740.52 → 1741.46] a political
[1741.46 → 1742.56] ideology
[1742.56 → 1743.22] of gun control.
[1743.86 → 1743.94] So,
[1744.26 → 1745.58] is your research
[1745.58 → 1746.90] into robustness
[1746.90 → 1747.92] and stuff,
[1748.28 → 1749.68] how is your research,
[1750.42 → 1751.60] how can it be applied
[1751.60 → 1752.90] to these real-life
[1752.90 → 1753.40] situations
[1753.40 → 1754.02] that we're all
[1754.02 → 1754.98] trying to figure out
[1754.98 → 1755.66] right now?
[1756.92 → 1757.76] How would you,
[1757.88 → 1758.64] what are your solutions?
[1758.96 → 1759.26] Of course,
[1759.42 → 1760.22] real-life solutions
[1760.22 → 1761.14] are very complex.
[1761.48 → 1762.10] I'm not claiming
[1762.10 → 1762.76] that we have
[1762.76 → 1766.40] bulletproof solutions
[1766.40 → 1767.52] to complex
[1767.52 → 1768.74] real-life problems.
[1768.88 → 1769.24] But,
[1769.40 → 1770.32] we could at least
[1770.32 → 1771.36] fix the obvious
[1771.36 → 1772.78] real-life problems.
[1772.90 → 1773.54] And the obvious
[1773.54 → 1774.44] real-life problems
[1774.44 → 1775.72] is that
[1775.72 → 1777.82] recommender systems
[1777.82 → 1778.90] should stop
[1778.90 → 1780.16] averaging gradients,
[1780.34 → 1780.80] for example.
[1781.08 → 1781.70] I'm not claiming
[1781.70 → 1782.80] that this is pure poisoning
[1782.80 → 1783.62] what's happened to YouTube.
[1783.80 → 1784.40] I don't know.
[1784.40 → 1784.86] I don't know
[1784.86 → 1785.28] what happened
[1785.28 → 1786.04] exactly to YouTube.
[1786.90 → 1787.08] But,
[1787.18 → 1788.66] I would say
[1788.66 → 1789.52] a first fix
[1789.52 → 1790.38] would stop
[1790.38 → 1793.62] taking the average,
[1794.34 → 1795.12] maybe if YouTube
[1795.12 → 1795.92] already fixed that,
[1796.02 → 1796.78] or maybe YouTube,
[1797.18 → 1798.28] maybe that's another problem
[1798.28 → 1799.34] that I was not aware of.
[1799.82 → 1800.00] But,
[1800.14 → 1800.76] let's say
[1800.76 → 1802.08] there is a situation
[1802.08 → 1802.94] where you average
[1802.94 → 1804.30] people's behaviour,
[1805.26 → 1806.90] and a first fix
[1806.90 → 1807.90] would stop averaging
[1807.90 → 1809.26] because you would
[1809.26 → 1809.86] be vulnerable
[1809.86 → 1811.44] to extremist groups.
[1811.44 → 1812.00] So,
[1812.00 → 1813.18] would it be fair,
[1813.40 → 1814.46] earlier you mentioned
[1814.46 → 1814.86] median,
[1815.02 → 1815.50] would that be
[1815.50 → 1816.70] a better selection?
[1816.90 → 1816.98] So,
[1817.30 → 1817.70] fundamentally,
[1817.98 → 1819.38] the approach
[1819.38 → 1820.20] that we're taking
[1820.20 → 1821.44] in machine learning
[1821.44 → 1822.12] in terms of
[1822.12 → 1823.30] the choices
[1823.30 → 1823.86] we're making
[1823.86 → 1824.42] as we're putting
[1824.42 → 1825.00] our algorithms
[1825.00 → 1826.08] together for a given
[1826.08 → 1827.48] use case or solution,
[1828.02 → 1829.00] in some cases
[1829.00 → 1829.90] maybe we're making,
[1830.08 → 1830.78] we're kind of
[1830.78 → 1831.52] following the herd,
[1831.90 → 1832.38] and we're doing
[1832.38 → 1833.22] what other people
[1833.22 → 1834.18] have done on other projects,
[1834.28 → 1834.86] but in the case
[1834.86 → 1835.84] that we're talking about,
[1835.84 → 1837.72] it's not serving us well
[1837.72 → 1838.62] because you can have
[1838.62 → 1839.84] extreme ends
[1839.84 → 1841.34] of that distribution
[1841.34 → 1842.38] that are able
[1842.38 → 1843.18] to take advantage of it.
[1843.20 → 1844.08] Most importantly,
[1844.42 → 1846.00] spotting those extreme ends
[1846.00 → 1847.04] today is becoming
[1847.04 → 1847.96] harder and harder.
[1848.58 → 1849.46] If you talk,
[1849.52 → 1850.44] I talk to bankers
[1850.44 → 1851.68] and insurance companies,
[1852.34 → 1853.24] they're very good
[1853.24 → 1854.28] at doing fraud detection,
[1855.26 → 1856.54] and they typically
[1856.54 → 1857.12] would do it
[1857.12 → 1858.34] with tools like PCA,
[1858.44 → 1859.08] I don't know how much
[1859.08 → 1859.84] details I should go
[1859.84 → 1860.44] into this podcast,
[1860.62 → 1861.62] but this is a method
[1861.62 → 1863.18] that detects
[1863.18 → 1864.34] big tendencies
[1864.34 → 1865.34] in a data set.
[1865.84 → 1868.02] The problem with that,
[1868.08 → 1869.06] so it's very good
[1869.06 → 1870.26] to spot outliers,
[1871.24 → 1873.22] but the cost of doing it
[1873.22 → 1876.50] grows quadratically
[1876.50 → 1878.88] as the data set is big.
[1879.98 → 1881.82] So it prevents you
[1881.82 → 1882.62] from leveraging
[1882.62 → 1884.50] high-dimensional
[1884.50 → 1887.14] big data,
[1887.30 → 1888.84] as we like to say today.
[1889.62 → 1893.40] So it narrows down
[1893.40 → 1894.76] the scope of your tool
[1894.76 → 1896.86] to simple linear regression,
[1897.00 → 1897.88] logistic regression.
[1898.44 → 1899.26] You can't do it,
[1899.30 → 1900.00] you can't do
[1900.00 → 1900.92] this kind of
[1900.92 → 1902.14] fraud detection mechanism
[1902.14 → 1903.54] on something as massive
[1903.54 → 1905.58] as a video platform.
[1906.34 → 1908.10] So we need something
[1908.10 → 1909.78] that scales
[1909.78 → 1911.40] at most linearly
[1911.40 → 1912.60] with the dimension
[1912.60 → 1914.06] of the model,
[1914.20 → 1914.96] of the data,
[1914.96 → 1918.18] and finding something
[1918.18 → 1919.38] that behaves like a median
[1919.38 → 1920.40] in high dimension
[1920.40 → 1922.34] is a hard problem.
[1924.84 → 1927.48] So the technical solution
[1927.48 → 1929.58] we've been working on,
[1929.64 → 1930.34] me and my colleagues,
[1930.92 → 1932.38] since I jumped on this problem
[1932.38 → 1934.04] two years ago or so,
[1934.12 → 1935.32] like I took a break
[1935.32 → 1937.02] from the biological robustness track.
[1937.12 → 1938.60] I'm getting back to it now,
[1938.64 → 1939.62] but I took a break
[1939.62 → 1940.18] for two years
[1940.18 → 1941.18] and I fully worked
[1941.18 → 1943.80] on this poisoning resilience
[1943.80 → 1945.70] and another AI safety question
[1945.70 → 1947.76] called safe interoperability
[1947.76 → 1948.64] with some friends.
[1950.64 → 1950.92] But yeah,
[1950.94 → 1951.96] on the poisoning side,
[1952.22 → 1953.44] we've been trying
[1953.44 → 1954.40] to find alternatives
[1954.40 → 1955.00] to the median
[1955.00 → 1956.50] because in high dimensions
[1956.50 → 1957.14] you can't,
[1957.14 → 1957.46] as I said,
[1957.50 → 1958.10] you can't rank,
[1958.18 → 1959.40] like you rank salaries
[1959.40 → 1960.58] and then you spot the salaries
[1960.58 → 1961.46] that split the salaries
[1961.46 → 1962.52] into two halves.
[1963.28 → 1964.46] Half the population
[1964.46 → 1965.62] earns less than 3,000,
[1966.00 → 1966.82] half the population
[1966.82 → 1968.24] earns more than 3,000,
[1968.34 → 1969.26] 3,000 is the median,
[1969.42 → 1969.60] fine.
[1970.52 → 1971.32] How do you do that
[1971.32 → 1971.90] for vectors?
[1972.50 → 1973.72] So for multidimensional data,
[1973.78 → 1974.70] you can't rank vectors,
[1974.86 → 1975.24] you can't say,
[1975.32 → 1975.84] oh, this is smaller
[1975.84 → 1976.20] than this one.
[1976.40 → 1977.24] Imagine like you have
[1977.24 → 1980.08] a million spreadsheets,
[1980.72 → 1981.78] each spreadsheet
[1981.78 → 1982.70] containing
[1982.70 → 1984.76] a million cells.
[1986.14 → 1987.24] You can't rank them.
[1988.00 → 1989.26] So you want to find
[1989.26 → 1990.70] the median spreadsheets.
[1990.96 → 1992.36] That's more or less
[1992.36 → 1993.38] what we're trying to do
[1993.38 → 1995.18] practically.
[1995.48 → 1996.04] So fast.
[1996.76 → 1997.50] And so that's what
[1997.50 → 1998.14] we've been doing.
[1998.32 → 1999.28] We've derived the series
[1999.28 → 1999.94] of algorithms
[1999.94 → 2001.74] that behave like a median
[2001.74 → 2004.92] and that provides guarantees
[2004.92 → 2007.06] that it is bounded
[2007.06 → 2009.00] in between a majority
[2009.00 → 2010.78] of points, etc.
[2011.00 → 2012.02] And we proved.
[2012.02 → 2016.40] so we've been also promoting
[2016.40 → 2018.54] the fact that security measures
[2018.54 → 2021.38] should always have a rigorous proof.
[2021.74 → 2023.84] Whenever we found a bug,
[2023.90 → 2025.88] we have to go back and modify.
[2025.88 → 2027.88] But it's not...
[2027.88 → 2029.12] It's very good to...
[2029.12 → 2031.22] Security measures should not be supported
[2031.22 → 2032.62] only by empirical evidence
[2032.62 → 2034.56] because you can never simulate
[2034.56 → 2036.56] all the possible attacks.
[2036.56 → 2040.06] So we always tried to prove
[2040.06 → 2042.36] that this protocol
[2042.36 → 2043.50] called gradient descent
[2043.50 → 2045.20] will always converge
[2045.20 → 2047.50] despite the existence
[2047.50 → 2048.30] of a fraction
[2048.30 → 2050.12] of poisoners.
[2050.78 → 2052.88] So we had the first paper
[2052.88 → 2054.84] on that in Neurons 2017.
[2054.84 → 2058.76] I'll give references
[2058.76 → 2059.94] and if you want to...
[2059.94 → 2060.84] Yeah, we'll definitely include
[2060.84 → 2061.70] those in the show notes.
[2061.70 → 2063.08] I guess,
[2063.32 → 2064.46] is it fair to say
[2064.46 → 2066.06] these higher order algorithms
[2066.06 → 2067.18] that you're talking about,
[2067.60 → 2068.98] is this a way of
[2068.98 → 2070.02] kind of maybe evolving
[2070.02 → 2070.80] gradient descent
[2070.80 → 2071.84] or maybe replacing it
[2071.84 → 2072.40] in such a way
[2072.40 → 2074.00] that we start having
[2074.00 → 2074.84] real tools
[2074.84 → 2076.16] to deal with poisoning
[2076.16 → 2078.22] and with fake news instances
[2078.22 → 2078.86] and such as that?
[2078.86 → 2081.28] Yeah, so talking about tools,
[2081.84 → 2082.70] I've been...
[2082.70 → 2086.20] So my work has been more on like...
[2086.20 → 2088.04] I was the guy who would find an algorithm
[2088.04 → 2089.72] and prove that this algorithm
[2089.72 → 2092.38] satisfies this requirement.
[2093.06 → 2096.04] But then I've been trying also
[2096.04 → 2098.44] to work with my colleagues
[2098.44 → 2098.90] and quarters
[2098.90 → 2101.56] who are more on the engineering side
[2101.56 → 2105.50] to port this on tools
[2105.50 → 2106.48] as soon as possible.
[2106.48 → 2108.86] And we have...
[2108.86 → 2109.38] So I said, yeah,
[2109.42 → 2111.00] we had this first paper in Neurons,
[2111.16 → 2112.44] then we published follow-ups
[2112.44 → 2113.06] in ICML,
[2113.16 → 2114.74] two follow-ups in ICML 2018,
[2114.96 → 2116.16] one in asynchronous settings
[2116.16 → 2117.72] and one in very high dimensional settings.
[2118.16 → 2121.04] But now we have a fourth work
[2121.04 → 2123.38] where we took TensorFlow,
[2124.76 → 2128.44] like this famous Google framework
[2128.44 → 2129.38] to do machine learning.
[2129.94 → 2130.96] We took TensorFlow
[2130.96 → 2132.40] and we replaced
[2132.40 → 2134.52] every averaging
[2134.52 → 2136.88] in the gradient aggregation
[2136.88 → 2138.24] parts of it
[2138.24 → 2139.90] with all the algorithms
[2139.90 → 2141.20] I've been promoting
[2141.20 → 2142.22] for the past two years.
[2142.98 → 2143.94] And my friend,
[2144.02 → 2144.52] my colleagues,
[2144.68 → 2145.16] Sebastian,
[2145.48 → 2146.14] Sunny and George,
[2146.62 → 2148.00] they made it work
[2148.00 → 2148.48] on TensorFlow
[2148.48 → 2150.16] and not only that,
[2150.26 → 2151.78] as also as a side bonus,
[2151.94 → 2153.38] they also made TensorFlow
[2153.38 → 2155.56] work communicating with UDP.
[2156.16 → 2156.92] So now,
[2157.16 → 2158.36] not only like TensorFlow,
[2158.90 → 2160.00] like the version of TensorFlow
[2160.00 → 2161.04] we'll publish on GitHub
[2161.04 → 2161.56] this week
[2161.56 → 2163.62] is Byzantine resilient,
[2163.82 → 2164.62] so it tolerates
[2164.62 → 2165.78] poisoning gradients
[2165.78 → 2167.38] up to a certain fraction,
[2168.04 → 2169.32] but it also can communicate
[2169.32 → 2170.10] over UDP,
[2170.28 → 2171.28] which is an unreliable
[2171.28 → 2172.36] communication protocol,
[2172.96 → 2174.42] instead of the previous one
[2174.42 → 2176.12] which required TCP IP
[2176.12 → 2177.74] because you cannot afford
[2177.74 → 2178.64] losing packages,
[2178.84 → 2179.08] et cetera.
[2179.22 → 2181.06] So as a bonus,
[2181.26 → 2182.36] now you can communicate
[2182.36 → 2183.48] over a faster
[2183.48 → 2185.06] but less reliable
[2185.06 → 2186.08] communication channel.
[2187.04 → 2188.00] That's not really like,
[2188.08 → 2189.08] it doesn't have to do
[2189.08 → 2190.32] only with the medium stuff,
[2190.32 → 2191.24] they also did some
[2191.24 → 2192.68] technical changes.
[2193.30 → 2194.54] So if you were
[2194.54 → 2195.80] an engineer out there
[2195.80 → 2197.62] and you'd listen to this
[2197.62 → 2198.62] and wanted to
[2198.62 → 2200.56] take advantage of that,
[2200.82 → 2202.14] because I had a sense
[2202.14 → 2202.58] that that's where
[2202.58 → 2203.06] you were going
[2203.06 → 2204.62] in terms of the research,
[2204.88 → 2205.72] you've now
[2205.72 → 2206.74] kind of have your own
[2206.74 → 2207.94] approach to gradient descent,
[2208.66 → 2209.74] do you foresee that
[2209.74 → 2211.36] ever being included
[2211.36 → 2212.02] with TensorFlow
[2212.02 → 2212.80] or do you think
[2212.80 → 2215.34] is the usage
[2215.34 → 2216.26] of what
[2216.26 → 2217.80] the output of the work,
[2217.88 → 2218.72] these tools that you've created,
[2218.72 → 2219.54] do you think
[2219.54 → 2220.44] it'll be common enough
[2220.44 → 2221.18] for dealing with
[2221.18 → 2221.64] things like
[2221.64 → 2222.72] poisoning
[2222.72 → 2225.04] and dealing with
[2225.04 → 2226.26] bad actors
[2226.26 → 2227.16] trying to take advantage
[2227.16 → 2228.02] of the data set?
[2228.28 → 2228.66] Do you think
[2228.66 → 2229.90] we're going to
[2229.90 → 2230.84] gradually evolve
[2230.84 → 2231.44] into using
[2231.44 → 2232.08] these types
[2232.08 → 2234.14] of updated algorithms
[2234.14 → 2235.44] to replace
[2235.44 → 2236.56] the average-based stuff
[2236.56 → 2237.16] or do you think
[2237.16 → 2237.90] it's always going to be
[2237.90 → 2238.70] a little bit more
[2238.70 → 2240.62] a specialized thing?
[2240.92 → 2242.26] I don't know
[2242.26 → 2242.54] if you know
[2242.54 → 2243.18] Stuart Russell,
[2243.96 → 2244.98] this famous professor
[2244.98 → 2245.58] at Berkeley,
[2245.84 → 2247.22] Stuart Russell.
[2247.22 → 2250.20] Stuart Russell
[2250.20 → 2251.86] is one of the pioneers
[2251.86 → 2253.40] of modern AI.
[2253.52 → 2254.46] He wrote that textbook
[2254.46 → 2255.46] AI, a modern approach
[2255.46 → 2256.24] with Peter Norvig
[2256.24 → 2257.58] and
[2257.58 → 2260.66] I like one of his arguments.
[2260.82 → 2261.48] We met in
[2261.48 → 2262.30] a conference
[2262.30 → 2263.14] weeks ago
[2263.14 → 2263.88] in Puerto Rico
[2263.88 → 2264.50] in this beneficial
[2264.50 → 2268.96] AI conference
[2268.96 → 2270.30] in Puerto Rico
[2270.30 → 2273.14] by the Future of Life Institute
[2273.14 → 2275.90] and I like one of his arguments
[2275.90 → 2277.64] for AI safety
[2277.64 → 2278.62] where he said
[2278.62 → 2280.44] if you talk to
[2280.44 → 2281.84] civil engineering people
[2281.84 → 2284.14] you will never find
[2284.14 → 2285.16] someone talking
[2285.16 → 2286.12] about bridges
[2286.12 → 2287.76] and someone else
[2287.76 → 2288.82] talking about
[2288.82 → 2289.80] safe bridges
[2289.80 → 2291.16] which are bridges
[2291.16 → 2292.22] that do not fall
[2292.22 → 2293.00] apart
[2293.00 → 2293.86] after three hours.
[2294.52 → 2295.24] So,
[2295.38 → 2296.40] not falling apart
[2296.40 → 2297.36] after three hours
[2297.36 → 2298.06] of deployment
[2298.06 → 2300.12] is part of the definition
[2300.12 → 2300.78] of a bridge.
[2300.78 → 2302.62] I think
[2302.62 → 2303.28] that's what
[2303.28 → 2304.24] the feeling
[2304.24 → 2304.60] I had
[2304.60 → 2305.20] from talking
[2305.20 → 2305.92] to attendants
[2305.92 → 2307.32] of Applied Machine Learning Days
[2307.32 → 2307.54] is
[2307.54 → 2308.98] we are going
[2308.98 → 2309.96] slowly
[2309.96 → 2310.60] towards
[2310.60 → 2312.06] this good direction
[2312.06 → 2312.90] where most of
[2312.90 → 2313.82] the people involved
[2313.82 → 2314.90] in machine learning research
[2314.90 → 2316.44] are more and more
[2316.44 → 2316.98] aware
[2316.98 → 2318.90] that not falling apart
[2318.90 → 2320.00] after a few hours
[2320.00 → 2320.56] of production
[2320.56 → 2322.28] is part of the definition
[2322.28 → 2322.96] of a bridge.
[2323.78 → 2324.36] And I think
[2324.36 → 2325.16] we will stop talking
[2325.16 → 2326.08] about safe AI
[2326.08 → 2326.58] and AI
[2326.58 → 2326.94] like
[2326.94 → 2327.92] it was just
[2327.92 → 2329.58] it should
[2329.58 → 2330.44] become part
[2330.44 → 2331.04] of the definition.
[2331.38 → 2331.52] Yeah,
[2331.62 → 2332.18] so it sounds like
[2332.18 → 2333.98] it's a foundational thing
[2333.98 → 2334.68] that we probably
[2334.68 → 2335.20] should have been
[2335.20 → 2335.72] thinking about
[2335.72 → 2336.24] ahead of time
[2336.24 → 2337.30] but it will become
[2337.30 → 2338.24] the de facto standard.
[2338.66 → 2339.36] It's essentially
[2339.36 → 2339.90] going to
[2339.90 → 2341.36] the success
[2341.36 → 2342.76] of safety AI
[2342.76 → 2344.10] essentially eclipses itself
[2344.10 → 2344.82] it just becomes
[2344.82 → 2346.44] AI and the tools we use.
[2347.14 → 2347.16] So,
[2347.30 → 2347.78] and then now
[2347.78 → 2348.44] coming back
[2348.44 → 2349.12] to your question
[2349.12 → 2350.76] is poisoning
[2350.76 → 2351.34] so like
[2351.34 → 2352.60] maybe I'm
[2352.60 → 2353.12] rephrasing
[2353.12 → 2353.60] exactly
[2353.60 → 2354.24] not exactly
[2354.24 → 2354.62] what you said
[2354.62 → 2355.84] but is poisoning
[2355.84 → 2356.72] really solvable
[2356.72 → 2357.40] like that.
[2358.32 → 2359.02] The bad news
[2359.02 → 2359.62] there is always
[2359.62 → 2360.24] a bad news
[2360.24 → 2360.94] in computing.
[2361.92 → 2363.10] People tend
[2363.10 → 2363.64] to forget
[2363.64 → 2364.72] that computer science
[2364.72 → 2366.20] was founded
[2366.20 → 2367.72] by an impossibility
[2367.72 → 2368.16] theory.
[2369.26 → 2369.54] Turing
[2369.54 → 2370.74] before proving
[2370.74 → 2372.26] what algorithms
[2372.26 → 2372.94] could do
[2372.94 → 2374.02] he started
[2374.02 → 2374.78] by proving
[2374.78 → 2375.64] what algorithms
[2375.64 → 2376.54] could never do
[2376.54 → 2378.16] the halting problem.
[2378.76 → 2379.74] You could never
[2379.74 → 2380.80] find an algorithm
[2380.80 → 2381.98] that audits
[2381.98 → 2382.78] algorithms
[2382.78 → 2383.60] and
[2383.60 → 2385.34] says
[2385.34 → 2386.30] whether
[2386.30 → 2387.06] this algorithm
[2387.06 → 2387.68] would terminate
[2387.68 → 2388.02] or not.
[2388.52 → 2388.58] Okay,
[2388.72 → 2388.86] so
[2388.86 → 2390.34] algorithmic
[2390.34 → 2390.76] science
[2390.76 → 2392.60] started out
[2392.60 → 2393.46] of an impossibility
[2393.46 → 2393.96] result.
[2394.24 → 2394.74] We have to
[2394.74 → 2395.44] really remember
[2395.44 → 2395.76] that.
[2396.52 → 2397.24] And we are
[2397.24 → 2398.54] a field of science
[2398.54 → 2399.34] I like that
[2399.34 → 2399.80] we are a field
[2399.80 → 2400.30] of science
[2400.30 → 2400.74] where
[2400.74 → 2401.88] impossibility
[2401.88 → 2402.54] results are
[2402.54 → 2403.00] foundational
[2403.00 → 2403.88] because they
[2403.88 → 2404.54] narrow down
[2404.54 → 2405.02] the scope
[2405.02 → 2405.44] of what you
[2405.44 → 2405.80] can do.
[2406.64 → 2407.16] You cannot
[2407.16 → 2407.88] do this
[2407.88 → 2408.42] so you can
[2408.42 → 2409.18] only do
[2409.18 → 2410.48] what is
[2410.48 → 2411.30] within this
[2411.30 → 2411.74] scope
[2411.74 → 2412.36] on the left.
[2413.42 → 2413.58] Good.
[2414.38 → 2414.94] Distributed
[2414.94 → 2415.40] computing
[2415.40 → 2416.26] so the field
[2416.26 → 2417.16] I'm part of
[2417.16 → 2418.42] partially
[2418.42 → 2420.02] also has
[2420.02 → 2420.66] strong
[2420.66 → 2421.46] impossibility
[2421.46 → 2422.10] results.
[2422.44 → 2422.82] You can't
[2422.82 → 2423.52] solve consensus
[2423.52 → 2424.06] you can't
[2424.06 → 2424.42] agree
[2424.42 → 2426.28] if a
[2426.28 → 2426.66] fraction
[2426.66 → 2427.36] of the
[2427.36 → 2427.72] nodes
[2427.72 → 2428.74] is
[2428.74 → 2429.82] malicious
[2429.82 → 2432.08] and
[2432.08 → 2434.18] exceeding
[2434.18 → 2434.54] a certain
[2434.54 → 2434.94] fraction.
[2435.58 → 2435.72] So
[2435.72 → 2436.54] for example
[2436.54 → 2437.56] if we want
[2437.56 → 2438.20] to agree
[2438.20 → 2438.56] on a
[2438.56 → 2438.76] common
[2438.76 → 2439.22] decision
[2439.22 → 2439.98] and
[2439.98 → 2441.64] 51%
[2441.64 → 2442.10] of the
[2442.10 → 2442.36] group
[2442.36 → 2443.18] are
[2443.18 → 2443.50] malicious
[2443.50 → 2444.76] we will
[2444.76 → 2444.96] not
[2444.96 → 2445.36] agree
[2445.36 → 2445.76] on the
[2445.76 → 2446.02] safest
[2446.02 → 2446.40] choice.
[2446.58 → 2446.88] This is
[2446.88 → 2447.22] trivial.
[2448.02 → 2448.36] There are
[2448.36 → 2448.76] similar
[2448.76 → 2449.40] theorems
[2449.40 → 2450.12] in game
[2450.12 → 2450.42] theory
[2450.42 → 2450.72] by the
[2450.72 → 2450.92] way
[2450.92 → 2451.54] like
[2451.54 → 2451.80] the
[2451.80 → 2454.06] impossibility
[2454.06 → 2454.54] theorems
[2454.54 → 2454.76] for
[2454.76 → 2456.08] democracy
[2456.08 → 2456.40] and
[2456.40 → 2457.26] social
[2457.26 → 2457.62] choice.
[2458.02 → 2458.48] We also
[2458.48 → 2458.88] have
[2458.88 → 2460.58] impossibility
[2460.58 → 2461.14] results
[2461.14 → 2461.72] for
[2461.72 → 2463.20] distributed
[2463.20 → 2463.86] machine
[2463.86 → 2464.18] learning
[2464.18 → 2465.62] or you
[2465.62 → 2465.96] can just
[2465.96 → 2466.32] think of
[2466.32 → 2466.62] it like
[2466.62 → 2467.84] gradient
[2467.84 → 2468.22] based
[2468.22 → 2468.52] machine
[2468.52 → 2468.84] learning
[2468.84 → 2470.98] that are
[2470.98 → 2471.46] not new
[2471.46 → 2473.84] I'm not
[2473.84 → 2474.74] claiming
[2474.74 → 2475.28] that we
[2475.28 → 2476.44] were behind
[2476.44 → 2476.80] that we
[2476.80 → 2477.70] just renewed
[2477.70 → 2478.48] the interest
[2478.48 → 2478.88] in them.
[2479.30 → 2479.54] They were
[2479.54 → 2480.16] proven in
[2480.16 → 2480.46] particular
[2480.46 → 2481.08] in 85
[2481.08 → 2481.82] by a
[2481.82 → 2482.06] Belgian
[2482.06 → 2482.54] guy called
[2482.54 → 2482.84] Peter
[2482.84 → 2483.34] Rousseau
[2483.34 → 2484.26] mathematician
[2484.26 → 2486.66] and the
[2486.66 → 2487.02] community
[2487.02 → 2487.56] of robust
[2487.56 → 2488.22] statistics
[2488.22 → 2489.46] you could
[2489.46 → 2490.16] actually prove
[2490.16 → 2490.70] that if you
[2490.70 → 2491.28] have a
[2491.28 → 2492.44] group of
[2492.44 → 2493.20] estimators
[2493.20 → 2493.94] a group
[2493.94 → 2494.54] of random
[2494.54 → 2495.24] variables
[2495.24 → 2499.84] following
[2499.84 → 2500.08] some
[2500.08 → 2500.50] distribution
[2500.50 → 2501.90] and an
[2501.90 → 2502.64] estimator
[2502.64 → 2503.86] could not
[2503.86 → 2504.50] guess the
[2504.50 → 2504.86] mean
[2504.86 → 2506.54] of those
[2506.54 → 2506.78] random
[2506.78 → 2507.32] variables
[2507.32 → 2508.74] if more
[2508.74 → 2509.18] than a
[2509.18 → 2509.96] half of
[2509.96 → 2510.20] them
[2510.20 → 2510.78] are
[2510.78 → 2511.40] adversarial.
[2512.66 → 2513.00] And then he
[2513.00 → 2513.44] coined this
[2513.44 → 2513.94] thing called
[2513.94 → 2514.58] the breakdown
[2514.58 → 2515.04] point
[2515.04 → 2516.26] we call it
[2516.26 → 2516.64] Byzantine
[2516.64 → 2517.26] fault tolerance
[2517.26 → 2517.76] in distributed
[2517.76 → 2518.20] computing
[2518.20 → 2519.04] because it
[2519.04 → 2519.48] has to do
[2519.48 → 2519.72] with a
[2519.72 → 2519.88] thought
[2519.88 → 2520.28] experiment
[2520.28 → 2520.58] called
[2520.58 → 2520.74] the
[2520.74 → 2521.18] Byzantine
[2521.18 → 2521.66] generals
[2521.66 → 2522.10] problem
[2522.10 → 2522.80] that we
[2522.80 → 2523.26] don't really
[2523.26 → 2523.62] need to
[2523.62 → 2524.04] go there
[2524.04 → 2525.02] it's just
[2525.02 → 2525.48] an agreement
[2525.48 → 2525.84] problem
[2525.84 → 2526.14] between
[2526.14 → 2526.62] three
[2526.62 → 2527.04] generals
[2527.04 → 2527.48] surrounding
[2527.48 → 2527.94] a city
[2527.94 → 2528.74] so if
[2528.74 → 2529.02] one of
[2529.02 → 2529.28] them is
[2529.28 → 2529.62] corrupt
[2529.62 → 2530.14] they can't
[2530.14 → 2530.42] agree
[2530.42 → 2530.92] whether to
[2530.92 → 2531.16] attack
[2531.16 → 2531.52] or not
[2531.52 → 2532.42] so if
[2532.42 → 2532.68] you have
[2532.68 → 2533.22] n generals
[2533.22 → 2533.62] surrounding
[2533.62 → 2534.06] a city
[2534.06 → 2534.98] and the
[2534.98 → 2535.52] city only
[2535.52 → 2535.98] needs to
[2535.98 → 2536.26] corrupt
[2536.26 → 2536.64] a third
[2536.64 → 2537.44] it doesn't
[2537.44 → 2537.74] need to
[2537.74 → 2537.94] corrupt
[2537.94 → 2538.34] everyone
[2538.34 → 2538.90] if it
[2538.90 → 2539.22] corrupts
[2539.22 → 2539.62] only a
[2539.62 → 2539.80] third
[2539.80 → 2540.08] of the
[2540.08 → 2540.42] generals
[2540.42 → 2541.02] the
[2541.02 → 2541.34] generals
[2541.34 → 2541.78] could not
[2541.78 → 2542.14] agree
[2542.14 → 2542.68] on the
[2542.68 → 2542.84] common
[2542.84 → 2543.26] decision
[2543.26 → 2543.84] and the
[2543.84 → 2544.04] same
[2544.04 → 2544.78] you cannot
[2544.78 → 2545.54] make
[2545.54 → 2546.72] gradient
[2546.72 → 2547.20] descent
[2547.20 → 2547.60] work
[2547.60 → 2548.44] if a
[2548.44 → 2548.66] certain
[2548.66 → 2549.14] fraction
[2549.14 → 2549.68] is not
[2549.68 → 2549.96] reliable
[2549.96 → 2550.48] so if
[2550.48 → 2550.78] most
[2550.78 → 2551.24] people
[2551.24 → 2552.56] are
[2552.56 → 2553.08] promoting
[2553.08 → 2553.92] anti-vaccine
[2553.92 → 2555.12] of course
[2555.12 → 2556.24] no solution
[2556.24 → 2556.62] will work
[2556.62 → 2556.90] I'm not
[2556.90 → 2557.18] claiming
[2557.18 → 2557.46] that we
[2557.46 → 2557.68] have a
[2557.68 → 2558.00] free
[2558.00 → 2558.24] proof
[2558.24 → 2558.44] so
[2558.44 → 2559.40] there's
[2559.40 → 2559.96] limitations
[2559.96 → 2560.42] in other
[2560.42 → 2560.62] words
[2560.62 → 2561.30] there's
[2561.30 → 2561.80] success
[2561.80 → 2562.18] to be
[2562.18 → 2562.58] had
[2562.58 → 2563.30] but there's
[2563.30 → 2563.78] also some
[2563.78 → 2564.22] limitations
[2564.22 → 2565.18] that if
[2565.18 → 2565.64] certain
[2565.64 → 2566.26] circumstances
[2566.26 → 2567.16] like that
[2567.16 → 2567.48] many are
[2567.48 → 2567.72] working
[2567.72 → 2568.20] against you
[2568.20 → 2568.54] you won't
[2568.54 → 2568.74] be able
[2568.74 → 2569.08] to overcome
[2569.08 → 2569.44] that
[2569.44 → 2570.72] but then
[2570.72 → 2571.68] people
[2571.68 → 2572.36] people on
[2572.36 → 2572.74] those big
[2572.74 → 2573.24] platforms
[2573.24 → 2574.60] I think
[2574.60 → 2575.08] are smart
[2575.08 → 2575.40] enough
[2575.40 → 2576.10] to realize
[2576.10 → 2576.42] that
[2576.42 → 2577.00] and they
[2577.00 → 2577.62] are realizing
[2577.62 → 2577.94] that
[2577.94 → 2578.26] I saw
[2578.26 → 2578.56] a very
[2578.56 → 2578.86] good
[2578.86 → 2580.36] press
[2580.36 → 2580.80] release
[2580.80 → 2581.30] from
[2581.30 → 2581.58] YouTube
[2581.58 → 2582.22] last week
[2582.22 → 2582.86] where they
[2582.86 → 2583.22] said that
[2583.22 → 2583.70] they will
[2583.70 → 2584.16] actively
[2584.16 → 2584.54] now
[2584.54 → 2585.44] try to
[2585.44 → 2585.74] work
[2585.74 → 2586.72] to
[2586.72 → 2587.74] prevent
[2587.74 → 2588.64] phony
[2588.64 → 2589.04] medical
[2589.04 → 2589.44] advice
[2589.44 → 2589.84] to be
[2589.84 → 2590.32] recommended
[2590.32 → 2590.94] on YouTube
[2590.94 → 2591.28] so this
[2591.28 → 2591.54] is not
[2591.54 → 2591.74] about
[2591.74 → 2592.10] censorship
[2592.10 → 2592.52] it's
[2592.52 → 2592.76] just
[2592.76 → 2593.04] about
[2593.04 → 2593.40] not
[2593.40 → 2593.94] recommending
[2593.94 → 2595.36] so they
[2595.36 → 2595.60] are
[2595.60 → 2596.02] actively
[2596.02 → 2596.52] looking
[2596.52 → 2596.82] at the
[2596.82 → 2597.20] problem
[2597.20 → 2598.08] and I
[2598.08 → 2598.38] believe
[2598.38 → 2599.26] they have
[2599.26 → 2599.54] enough
[2599.54 → 2599.82] smart
[2599.82 → 2600.10] people
[2600.10 → 2600.30] to
[2600.30 → 2600.52] think
[2600.52 → 2600.76] about
[2600.76 → 2601.04] that
[2601.04 → 2602.36] and
[2602.36 → 2603.36] what
[2603.36 → 2603.94] I'm
[2603.94 → 2604.28] working
[2604.28 → 2604.56] on
[2604.56 → 2604.92] now
[2604.92 → 2605.42] as a
[2605.42 → 2605.78] follow-up
[2605.78 → 2606.02] of what
[2606.02 → 2606.22] I've
[2606.22 → 2606.46] mentioned
[2606.46 → 2606.92] before
[2606.92 → 2607.60] are
[2607.60 → 2608.14] situations
[2608.14 → 2608.54] where you
[2608.54 → 2608.72] don't
[2608.72 → 2609.08] have a
[2609.08 → 2609.50] majority
[2609.50 → 2609.96] of
[2609.96 → 2610.38] reliable
[2610.38 → 2610.78] notes
[2610.78 → 2611.96] but you
[2611.96 → 2612.30] have a
[2612.30 → 2612.66] minority
[2612.66 → 2612.94] of
[2612.94 → 2613.34] experts
[2613.34 → 2614.06] it's
[2614.06 → 2614.20] some
[2614.20 → 2614.42] sort
[2614.42 → 2614.58] of
[2614.58 → 2615.88] aristocracy
[2615.88 → 2616.84] so you
[2616.84 → 2617.18] give the
[2617.18 → 2617.52] power
[2617.52 → 2618.34] to those
[2618.34 → 2618.52] who
[2618.52 → 2618.74] know
[2618.74 → 2619.78] so
[2619.78 → 2620.16] imagine
[2620.16 → 2620.34] you
[2620.34 → 2620.46] have
[2620.46 → 2620.60] the
[2620.60 → 2620.80] John
[2620.80 → 2621.24] Hopkins
[2621.24 → 2622.36] medical
[2622.36 → 2622.72] school
[2622.72 → 2622.98] YouTube
[2622.98 → 2623.42] account
[2623.42 → 2624.42] the
[2624.42 → 2625.06] Pasteur
[2625.06 → 2625.42] Institute
[2625.42 → 2625.72] in
[2625.72 → 2626.04] French
[2626.04 → 2627.52] YouTube
[2627.52 → 2628.10] account
[2628.10 → 2629.14] and then
[2629.14 → 2629.54] you have
[2629.54 → 2630.00] the
[2630.00 → 2630.64] hospital
[2630.64 → 2630.86] of
[2630.86 → 2631.18] Lausanne
[2631.18 → 2631.52] etc
[2631.52 → 2632.74] and they're
[2632.74 → 2633.14] producing
[2633.14 → 2633.60] content
[2633.60 → 2633.98] on
[2633.98 → 2634.20] say
[2634.20 → 2634.58] vaccine
[2634.58 → 2635.74] but then
[2635.74 → 2635.98] you have
[2635.98 → 2636.46] a majority
[2636.46 → 2638.60] of poisoners
[2638.60 → 2639.60] of anti-vaxxers
[2639.60 → 2641.18] and you
[2641.18 → 2641.72] might want
[2641.72 → 2642.28] to do
[2642.28 → 2642.76] something
[2642.76 → 2643.42] in the
[2643.42 → 2643.94] page rank
[2643.94 → 2644.48] style
[2644.48 → 2645.70] so
[2645.70 → 2646.50] some sort
[2646.50 → 2646.80] of like
[2646.80 → 2647.76] a page rank
[2647.76 → 2648.30] gradient
[2648.30 → 2648.80] descent
[2648.80 → 2649.92] where you
[2649.92 → 2650.52] follow the
[2650.52 → 2650.98] experts
[2650.98 → 2651.84] got you
[2651.84 → 2652.16] so you're
[2652.16 → 2652.50] basically
[2652.50 → 2653.38] you want
[2653.38 → 2653.60] to take
[2653.60 → 2654.10] advantage of
[2654.10 → 2654.62] their expertise
[2654.62 → 2655.40] which is a
[2655.40 → 2655.72] way of
[2655.72 → 2656.42] countering
[2656.42 → 2657.08] the fact
[2657.08 → 2657.32] that you
[2657.32 → 2657.56] have a
[2657.56 → 2657.84] majority
[2657.84 → 2658.04] of
[2658.04 → 2658.62] poisoners
[2658.62 → 2658.90] in
[2658.90 → 2659.18] there
[2659.18 → 2659.78] so
[2659.78 → 2660.40] it
[2660.40 → 2660.66] sounds
[2660.66 → 2660.88] like
[2660.88 → 2661.02] you're
[2661.02 → 2661.30] almost
[2661.30 → 2661.82] taking
[2661.82 → 2662.26] a couple
[2662.26 → 2662.64] of tools
[2662.64 → 2662.96] and making
[2662.96 → 2663.48] a composite
[2663.48 → 2663.86] out of
[2663.86 → 2664.04] it
[2664.04 → 2665.32] as we
[2665.32 → 2665.60] start
[2665.60 → 2665.90] to
[2665.90 → 2666.54] finish
[2666.54 → 2666.92] up
[2666.92 → 2667.50] is
[2667.50 → 2668.36] how
[2668.36 → 2668.96] can
[2668.96 → 2669.58] practitioners
[2669.58 → 2670.14] out there
[2670.14 → 2670.50] start
[2670.50 → 2670.90] to take
[2670.90 → 2671.50] advantage
[2671.50 → 2672.20] of
[2672.20 → 2672.66] these
[2672.66 → 2673.06] results
[2673.06 → 2673.36] that you
[2673.36 → 2673.68] found
[2673.68 → 2674.04] and the
[2674.04 → 2674.38] research
[2674.38 → 2674.80] that you've
[2674.80 → 2675.12] done
[2675.12 → 2675.88] to
[2675.88 → 2676.56] help
[2676.56 → 2677.26] better
[2677.26 → 2677.48] the
[2677.48 → 2677.90] situation
[2677.90 → 2678.30] we find
[2678.30 → 2678.58] ourselves
[2678.58 → 2678.78] in
[2678.78 → 2679.06] now
[2679.06 → 2679.90] where we
[2679.90 → 2680.38] have so
[2680.38 → 2680.60] much
[2680.60 → 2680.96] poisoning
[2680.96 → 2681.54] going on
[2681.54 → 2681.84] with so
[2681.84 → 2681.96] many
[2681.96 → 2682.20] people
[2682.20 → 2682.84] trying to
[2682.84 → 2685.00] start
[2685.00 → 2690.14] by reading
[2690.14 → 2690.62] the literature
[2690.62 → 2690.92] there's
[2690.92 → 2691.56] literature
[2691.56 → 2692.14] on poisoning
[2692.14 → 2692.56] has been
[2692.56 → 2693.12] there before
[2693.12 → 2693.50] I even
[2693.50 → 2693.78] started
[2693.78 → 2693.94] doing
[2693.94 → 2694.16] machine
[2694.16 → 2694.38] learning
[2694.38 → 2694.68] there was
[2694.68 → 2695.18] people
[2695.18 → 2695.36] who
[2695.36 → 2695.64] started
[2695.64 → 2695.90] looking
[2695.90 → 2696.24] at that
[2696.24 → 2696.46] since
[2696.46 → 2696.80] at least
[2696.80 → 2697.60] 2004
[2697.60 → 2698.94] and people
[2698.94 → 2699.62] who
[2699.62 → 2700.38] had made
[2700.38 → 2700.92] significant
[2700.92 → 2701.50] progress
[2701.50 → 2702.30] in 2012
[2702.30 → 2703.36] 13
[2703.36 → 2704.66] and so
[2704.66 → 2704.88] yeah
[2704.88 → 2705.80] there is
[2705.80 → 2706.06] a good
[2706.06 → 2706.40] literature
[2706.40 → 2706.82] to be
[2706.82 → 2707.20] read
[2707.20 → 2708.62] they could
[2708.62 → 2708.78] also
[2708.78 → 2709.24] we will
[2709.24 → 2709.64] release
[2709.64 → 2710.70] a GitHub
[2710.70 → 2711.02] repo
[2711.02 → 2711.34] with
[2711.34 → 2712.40] the code
[2712.40 → 2712.86] based on
[2712.86 → 2712.98] the
[2712.98 → 2713.36] algorithms
[2713.36 → 2713.64] I've
[2713.64 → 2713.92] been
[2713.92 → 2714.50] promoting
[2714.50 → 2714.90] before
[2714.90 → 2715.18] so
[2715.18 → 2715.92] my
[2715.92 → 2716.34] colleagues
[2716.34 → 2716.52] will
[2716.52 → 2716.82] release
[2716.82 → 2717.02] that
[2717.02 → 2717.20] on
[2717.20 → 2717.58] GitHub
[2717.58 → 2718.16] so
[2718.16 → 2718.30] they
[2718.30 → 2718.50] could
[2718.50 → 2718.80] take
[2718.80 → 2719.08] it
[2719.08 → 2719.60] play
[2719.60 → 2719.82] with
[2719.82 → 2719.96] it
[2719.96 → 2720.24] find
[2720.24 → 2720.76] bugs
[2720.76 → 2721.78] potential
[2721.78 → 2722.18] bugs
[2722.18 → 2722.40] in it
[2722.40 → 2722.72] find
[2722.72 → 2723.06] new
[2723.06 → 2723.62] vulnerabilities
[2723.62 → 2724.24] we didn't
[2724.24 → 2724.46] see
[2724.46 → 2725.72] the space
[2725.72 → 2725.96] of
[2725.96 → 2726.48] vulnerabilities
[2726.48 → 2727.08] is
[2727.08 → 2728.18] technically
[2728.18 → 2728.66] limited
[2728.66 → 2729.46] so you
[2729.46 → 2729.92] can always
[2729.92 → 2730.66] find new
[2730.66 → 2731.16] vulnerabilities
[2731.16 → 2731.82] or a
[2731.82 → 2732.02] new
[2732.02 → 2732.30] threat
[2732.30 → 2732.82] model
[2732.82 → 2733.76] for which
[2733.76 → 2734.52] our
[2734.52 → 2735.00] because
[2735.00 → 2735.74] you always
[2735.74 → 2736.10] make a
[2736.10 → 2736.28] threat
[2736.28 → 2736.60] model
[2736.60 → 2738.00] and
[2738.00 → 2738.36] maybe
[2738.36 → 2738.66] we
[2738.66 → 2739.16] overlooked
[2739.16 → 2739.56] another
[2739.56 → 2739.82] threat
[2739.82 → 2740.10] model
[2740.10 → 2740.64] and
[2740.64 → 2741.26] they can
[2741.26 → 2741.46] make
[2741.46 → 2741.86] progress
[2741.86 → 2742.28] on that
[2742.28 → 2742.74] I would
[2742.74 → 2743.04] also
[2743.04 → 2743.56] advise
[2743.56 → 2745.42] taking
[2745.42 → 2746.10] data
[2746.10 → 2746.54] sets
[2746.54 → 2746.84] that
[2746.84 → 2747.34] might
[2747.34 → 2748.60] give
[2748.60 → 2748.82] you
[2748.82 → 2749.04] a
[2749.04 → 2749.26] sense
[2749.26 → 2749.44] of
[2749.44 → 2749.64] what
[2749.64 → 2749.76] a
[2749.76 → 2750.18] recommender
[2750.18 → 2750.46] system
[2750.46 → 2750.90] does
[2750.90 → 2752.08] and
[2752.08 → 2752.44] try to
[2752.44 → 2752.72] poison
[2752.72 → 2752.96] it
[2752.96 → 2753.40] just to
[2753.40 → 2754.02] understand
[2754.02 → 2755.64] how
[2755.64 → 2755.90] easy
[2755.90 → 2756.38] it is
[2756.38 → 2756.70] and
[2756.70 → 2756.92] maybe
[2756.92 → 2757.10] you
[2757.10 → 2757.42] might
[2757.42 → 2757.72] find
[2757.72 → 2757.84] the
[2757.84 → 2758.16] vulnerability
[2758.16 → 2758.40] because
[2758.40 → 2759.22] now we
[2759.22 → 2759.60] enter in
[2759.60 → 2759.98] an era
[2759.98 → 2760.38] where you
[2760.38 → 2760.76] don't need
[2760.76 → 2761.24] to be
[2761.24 → 2762.78] like a
[2762.78 → 2763.12] classic
[2763.12 → 2763.54] hacker
[2763.54 → 2763.86] you don't
[2763.86 → 2764.20] need to
[2764.20 → 2764.64] penetrate
[2764.64 → 2765.72] you don't
[2765.72 → 2766.04] need to
[2766.04 → 2766.36] do a
[2766.36 → 2766.72] penetration
[2766.72 → 2767.28] in the
[2767.28 → 2767.88] servers
[2767.88 → 2768.42] and the
[2768.42 → 2768.76] system
[2768.76 → 2770.02] to poison
[2770.02 → 2770.60] a recommender
[2770.60 → 2770.78] system
[2770.78 → 2771.06] you just
[2771.06 → 2771.32] need to
[2771.32 → 2771.66] behave
[2771.66 → 2772.60] like
[2772.60 → 2773.12] comment
[2773.12 → 2774.22] dislike
[2774.22 → 2775.10] post
[2775.10 → 2776.54] so maybe
[2776.54 → 2776.98] there are
[2776.98 → 2777.90] still much
[2777.90 → 2778.22] more
[2778.22 → 2778.80] vulnerabilities
[2778.80 → 2779.88] that could
[2779.88 → 2780.32] be
[2780.32 → 2781.60] allowing
[2781.60 → 2782.20] people to
[2782.20 → 2782.90] just behave
[2782.90 → 2783.66] and look
[2783.66 → 2784.04] legit
[2784.04 → 2784.96] and poison
[2784.96 → 2785.92] I don't
[2785.92 → 2786.08] know
[2786.08 → 2786.68] make a
[2786.68 → 2788.30] movie platform
[2788.30 → 2788.84] recommend
[2788.84 → 2789.60] the suicidal
[2789.60 → 2791.78] content to
[2791.78 → 2792.34] a depressed
[2792.34 → 2793.24] user
[2793.24 → 2793.78] so this
[2793.78 → 2794.22] is something
[2794.22 → 2794.70] we don't
[2794.70 → 2794.92] want
[2794.92 → 2795.28] to have
[2795.28 → 2796.70] and I
[2796.70 → 2796.94] would
[2796.94 → 2797.40] bet
[2797.40 → 2798.32] that those
[2798.32 → 2798.66] things
[2798.66 → 2799.14] do not
[2799.14 → 2799.60] need
[2799.60 → 2800.78] hacking
[2800.78 → 2801.36] inside
[2801.36 → 2801.58] the
[2801.58 → 2801.96] servers
[2801.96 → 2802.26] and I
[2802.26 → 2802.38] don't
[2802.38 → 2802.50] know
[2802.50 → 2803.02] finding a
[2803.02 → 2803.28] zero
[2803.28 → 2803.64] day
[2803.64 → 2804.20] and switching
[2804.20 → 2804.72] the code
[2804.72 → 2805.88] I think
[2805.88 → 2807.32] because of
[2807.32 → 2807.66] high
[2807.66 → 2808.42] dimensionality
[2808.42 → 2809.20] we have a
[2809.20 → 2809.66] paper called
[2809.66 → 2810.02] the hidden
[2810.02 → 2810.52] vulnerability
[2810.52 → 2811.30] of distributed
[2811.30 → 2811.62] learning
[2811.62 → 2812.32] in Byzantium
[2812.32 → 2813.38] and the hidden
[2813.38 → 2813.82] vulnerability
[2813.82 → 2814.60] is basically
[2814.60 → 2815.28] high dimension
[2815.28 → 2816.44] today
[2816.44 → 2817.54] as we are
[2817.54 → 2818.56] making machine
[2818.56 → 2819.26] learning powerful
[2819.26 → 2820.44] we are
[2820.44 → 2821.12] learning
[2821.12 → 2822.34] more and more
[2822.34 → 2822.96] high dimensional
[2822.96 → 2823.44] models
[2823.44 → 2824.72] and these
[2824.72 → 2825.74] high dimensionalities
[2825.74 → 2826.52] give a lot of
[2826.52 → 2826.98] leeway
[2826.98 → 2827.80] a lot of
[2827.80 → 2828.18] margin
[2828.18 → 2828.88] to attackers
[2828.88 → 2830.16] so the bad
[2830.16 → 2830.80] news is that
[2830.80 → 2831.88] as machine
[2831.88 → 2832.30] learning is
[2832.30 → 2833.14] going to be
[2833.14 → 2834.18] high dimensional
[2834.18 → 2835.94] and powerful
[2835.94 → 2837.34] it is also
[2837.34 → 2838.26] becoming
[2838.26 → 2838.90] very
[2838.90 → 2840.08] wide
[2840.08 → 2840.74] in the amount
[2840.74 → 2841.38] of leeway
[2841.38 → 2841.98] it gives to
[2841.98 → 2842.32] attackers
[2842.32 → 2843.62] so I think
[2843.62 → 2844.38] a good starting
[2844.38 → 2844.82] point would
[2844.82 → 2845.54] try to play
[2845.54 → 2845.94] with those
[2845.94 → 2846.32] algorithms
[2846.32 → 2846.90] and find
[2846.90 → 2847.44] eventual
[2847.44 → 2847.92] vulnerabilities
[2847.92 → 2848.56] we overlooked
[2848.56 → 2850.72] and yeah
[2850.72 → 2851.40] if you are a
[2851.40 → 2851.82] practitioner
[2851.82 → 2852.58] and you don't
[2852.58 → 2853.10] care much
[2853.10 → 2853.48] about the
[2853.48 → 2854.18] if you're a
[2854.18 → 2854.64] theoretician
[2854.64 → 2855.18] I would also
[2855.18 → 2855.84] be very happy
[2855.84 → 2856.68] to hear about
[2856.68 → 2857.48] what we might
[2857.48 → 2858.00] have missed
[2858.00 → 2858.80] in the
[2858.80 → 2859.18] theoretical
[2859.18 → 2859.62] analysis
[2859.62 → 2860.36] so maybe
[2860.36 → 2860.98] there's a
[2860.98 → 2861.42] bug in our
[2861.42 → 2861.80] proof
[2861.80 → 2862.28] and I'll be
[2862.28 → 2862.72] happy to
[2862.72 → 2864.30] learn that
[2864.30 → 2865.08] and work
[2865.08 → 2865.46] on fixing
[2865.46 → 2865.80] that
[2865.80 → 2866.44] but if you
[2866.44 → 2866.66] are a
[2866.66 → 2867.00] practitioner
[2867.00 → 2867.40] and you
[2867.40 → 2867.76] don't care
[2867.76 → 2867.96] much
[2867.96 → 2868.26] about the
[2868.26 → 2868.56] theory
[2868.56 → 2869.50] I would
[2869.50 → 2869.82] say
[2869.82 → 2870.38] download
[2870.38 → 2870.82] the
[2870.82 → 2871.14] GitHub
[2871.14 → 2871.40] repo
[2871.40 → 2871.80] of my
[2871.80 → 2872.10] colleagues
[2872.10 → 2873.04] and try
[2873.04 → 2873.56] to improve
[2873.56 → 2873.78] it
[2873.78 → 2874.10] and try
[2874.10 → 2874.50] to apply
[2874.50 → 2874.66] it
[2874.66 → 2875.32] on public
[2875.32 → 2875.74] datasets
[2875.74 → 2876.24] that are
[2876.24 → 2876.62] more
[2876.62 → 2877.68] relevant
[2877.68 → 2878.00] for
[2878.00 → 2878.40] recommender
[2878.40 → 2878.68] systems
[2878.68 → 2879.58] and maybe
[2879.58 → 2880.00] for other
[2880.00 → 2880.28] stuff
[2880.28 → 2880.74] not only
[2880.74 → 2881.16] recommender
[2881.16 → 2881.36] systems
[2881.36 → 2881.86] so I
[2881.86 → 2882.30] just like
[2882.30 → 2882.46] yeah
[2882.46 → 2882.88] for something
[2882.88 → 2883.18] like to
[2883.18 → 2883.50] conclude
[2883.50 → 2883.70] on
[2883.70 → 2884.84] I've been
[2884.84 → 2885.44] overusing
[2885.44 → 2885.92] recommender
[2885.92 → 2886.24] systems
[2886.24 → 2886.54] here
[2886.54 → 2886.96] because I
[2886.96 → 2887.30] think this
[2887.30 → 2887.70] is the
[2887.70 → 2889.06] most pressing
[2889.06 → 2889.86] example of
[2889.86 → 2890.58] killer robots
[2890.58 → 2891.14] we have
[2891.14 → 2892.44] today people
[2892.44 → 2892.72] are not
[2892.72 → 2893.16] killed by
[2893.16 → 2893.76] are not
[2893.76 → 2895.04] killed by
[2895.04 → 2895.52] self-driving
[2895.52 → 2895.92] cars
[2895.92 → 2896.34] they're
[2896.34 → 2896.48] more
[2896.48 → 2896.82] killed
[2896.82 → 2897.00] with
[2897.00 → 2897.30] hate
[2897.30 → 2897.72] speech
[2897.72 → 2897.86] and
[2897.86 → 2898.50] anti-vaccine
[2898.50 → 2899.22] but of
[2899.22 → 2899.34] course
[2899.34 → 2899.94] poisoning
[2899.94 → 2900.70] will become
[2900.70 → 2901.10] a problem
[2901.10 → 2901.62] also for
[2901.62 → 2902.10] self-driving
[2902.10 → 2902.40] cars
[2902.40 → 2903.40] if you
[2903.40 → 2903.78] poison
[2903.78 → 2904.50] the traffic
[2904.50 → 2904.94] sign
[2904.94 → 2905.50] and then
[2905.50 → 2906.56] you make
[2906.56 → 2907.46] self-driving
[2907.46 → 2908.10] cars learn
[2908.10 → 2908.98] an irrelevant
[2908.98 → 2909.50] model
[2909.50 → 2910.34] you might
[2910.34 → 2911.48] start
[2911.48 → 2914.82] leading them
[2914.82 → 2915.20] into
[2915.20 → 2915.82] unsafe
[2915.82 → 2916.16] behaviour
[2916.16 → 2917.24] but the
[2917.24 → 2917.80] idea of
[2917.80 → 2918.22] poisoning
[2918.22 → 2918.76] resilience
[2918.76 → 2919.86] is very
[2919.86 → 2920.30] broad
[2920.30 → 2920.76] so it
[2920.76 → 2920.98] doesn't
[2920.98 → 2921.26] apply
[2921.26 → 2921.60] only to
[2921.60 → 2921.96] recommender
[2921.96 → 2922.36] systems
[2922.36 → 2923.10] you can
[2923.10 → 2923.44] think of
[2923.44 → 2923.78] your own
[2923.78 → 2924.16] problem
[2924.16 → 2924.52] and your
[2924.52 → 2924.94] own
[2924.94 → 2925.44] motivation
[2925.44 → 2926.02] and try
[2926.02 → 2927.50] to improve
[2927.50 → 2927.86] on that
[2927.86 → 2928.52] that's
[2928.52 → 2929.00] fantastic
[2929.00 → 2929.36] and we'll
[2929.36 → 2929.62] certainly
[2929.62 → 2930.36] include the
[2930.36 → 2930.82] GitHub
[2930.82 → 2932.08] repo in
[2932.08 → 2932.40] the show
[2932.40 → 2932.60] notes
[2932.60 → 2932.88] but I'll
[2932.88 → 2933.06] tell you
[2933.06 → 2933.22] what
[2933.22 → 2933.44] you
[2933.44 → 2934.04] concluded
[2934.04 → 2934.76] that was
[2934.76 → 2935.28] a strong
[2935.28 → 2935.80] conclusion
[2935.80 → 2936.28] I mean
[2936.28 → 2936.74] if there's
[2936.74 → 2937.10] anything
[2937.10 → 2938.08] that makes
[2938.08 → 2939.22] me realize
[2939.22 → 2939.90] how relevant
[2939.90 → 2940.42] what you're
[2940.42 → 2941.00] talking about
[2941.00 → 2941.38] is
[2941.38 → 2942.72] even beyond
[2942.72 → 2943.32] social media
[2943.32 → 2943.88] is the fact
[2943.88 → 2944.44] that we
[2944.44 → 2944.86] have all
[2944.86 → 2945.18] these
[2945.18 → 2946.24] we have
[2946.24 → 2946.58] now
[2946.58 → 2947.28] cars
[2947.28 → 2948.18] and trucks
[2948.18 → 2948.62] and other
[2948.62 → 2949.10] vehicles
[2949.10 → 2949.86] and other
[2949.86 → 2950.98] IOT
[2950.98 → 2951.50] devices
[2951.50 → 2951.84] that may
[2951.84 → 2952.32] be mobile
[2952.32 → 2952.98] that could
[2952.98 → 2953.48] be poisoned
[2953.48 → 2953.86] along the
[2953.86 → 2954.02] way
[2954.02 → 2954.30] and that
[2954.30 → 2955.36] itself
[2955.36 → 2956.38] can present
[2956.38 → 2956.80] a physical
[2956.80 → 2957.16] danger
[2957.16 → 2957.50] separate
[2957.50 → 2957.86] from
[2957.86 → 2958.50] that
[2958.50 → 2958.86] so
[2958.86 → 2959.74] it's
[2959.74 → 2960.22] amazing
[2960.22 → 2961.02] how relevant
[2961.02 → 2961.48] what you're
[2961.48 → 2962.04] working on
[2962.04 → 2962.74] is going to be
[2962.74 → 2962.98] to our
[2962.98 → 2963.28] future
[2963.28 → 2964.06] thank you
[2964.06 → 2964.40] very much
[2964.40 → 2964.72] for coming
[2964.72 → 2965.02] on the
[2965.02 → 2965.26] show
[2965.26 → 2966.30] and I
[2966.30 → 2966.54] really
[2966.54 → 2966.86] appreciate
[2966.86 → 2967.12] you
[2967.12 → 2967.40] taking
[2967.40 → 2967.92] the time
[2967.92 → 2968.46] late in
[2968.46 → 2968.84] the conference
[2968.84 → 2969.16] to do
[2969.16 → 2969.46] this
[2969.46 → 2969.98] thank you
[2969.98 → 2970.10] you're
[2970.10 → 2970.32] welcome
[2970.32 → 2972.88] all right
[2972.88 → 2973.22] thank you
[2973.22 → 2973.54] for tuning
[2973.54 → 2974.02] into this
[2974.02 → 2974.64] episode
[2974.64 → 2974.96] of
[2974.96 → 2975.38] Practical
[2975.38 → 2975.54] AI
[2975.54 → 2976.02] if you
[2976.02 → 2976.22] enjoyed
[2976.22 → 2976.58] the show
[2976.58 → 2976.86] do us
[2976.86 → 2977.28] a favour
[2977.28 → 2977.62] go on
[2977.62 → 2977.98] iTunes
[2977.98 → 2978.32] give us
[2978.32 → 2978.80] a rating
[2978.80 → 2979.36] go in your
[2979.36 → 2980.22] podcast app
[2980.22 → 2980.72] and favourite
[2980.72 → 2980.92] it
[2980.92 → 2981.40] if you are
[2981.40 → 2981.82] on Twitter
[2981.82 → 2982.30] or social
[2982.30 → 2982.72] network
[2982.72 → 2983.24] share a link
[2983.24 → 2983.74] with a friend
[2983.74 → 2984.06] whatever you
[2984.06 → 2984.48] gotta do
[2984.48 → 2985.00] share the
[2985.00 → 2985.32] show with a
[2985.32 → 2985.46] friend
[2985.46 → 2985.66] if you
[2985.66 → 2986.22] enjoyed it
[2986.22 → 2986.86] and bandwidth
[2986.86 → 2987.62] for changelog
[2987.62 → 2988.34] is provided
[2988.34 → 2989.14] by Vastly
[2989.14 → 2989.68] learn more
[2989.68 → 2990.68] at fastly.com
[2990.68 → 2991.44] and we catch
[2991.44 → 2991.82] our errors
[2991.82 → 2992.46] before our users
[2992.46 → 2992.94] do here at
[2992.94 → 2993.26] changelog
[2993.26 → 2993.68] because of
[2993.68 → 2994.10] Rollbar
[2994.10 → 2994.74] check them
[2994.74 → 2995.18] out at
[2995.18 → 2995.74] rollbar.com
[2995.74 → 2996.72] slash changelog
[2996.72 → 2997.46] and we're
[2997.46 → 2998.22] hosted on
[2998.22 → 2998.84] Linde cloud
[2998.84 → 2999.52] servers
[2999.52 → 3000.02] head to
[3000.02 → 3000.64] linode.com
[3000.64 → 3001.48] slash changelog
[3001.48 → 3001.88] check them
[3001.88 → 3002.36] out support
[3002.36 → 3002.94] this show
[3002.94 → 3004.08] this episode
[3004.08 → 3004.64] is hosted
[3004.64 → 3005.26] by Daniel
[3005.26 → 3005.80] Whiten ack
[3005.80 → 3006.14] and Chris
[3006.14 → 3006.56] Benson
[3006.56 → 3007.34] editing is
[3007.34 → 3007.68] done by
[3007.68 → 3008.44] Tim Smith
[3008.44 → 3009.16] the music
[3009.16 → 3009.70] is by
[3009.70 → 3010.28] Break master
[3010.28 → 3010.74] Cylinder
[3010.74 → 3011.52] and you can
[3011.52 → 3011.94] find more
[3011.94 → 3012.50] shows just
[3012.50 → 3013.04] like this
[3013.04 → 3014.54] at changelog.com
[3014.54 → 3015.22] when you go
[3015.22 → 3015.80] there pop in
[3015.80 → 3016.20] your email
[3016.20 → 3016.70] address
[3016.70 → 3017.24] get our
[3017.24 → 3017.90] weekly email
[3017.90 → 3018.40] keeping you
[3018.40 → 3018.76] up to date
[3018.76 → 3019.14] with the
[3019.14 → 3019.76] news and
[3019.76 → 3020.28] podcasts
[3020.28 → 3020.82] for developers
[3020.82 → 3021.52] in your
[3021.52 → 3022.02] inbox
[3022.02 → 3022.68] every single
[3022.68 → 3023.02] week
[3023.02 → 3023.76] thanks for
[3023.76 → 3024.20] tuning in
[3024.20 → 3024.64] we'll see
[3024.64 → 3024.84] you next
[3024.84 → 3025.10] week
[3036.56 → 3042.06] at
