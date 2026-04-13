[0.00 --> 7.94]  Problems, data, requirements, business process, constraints are so specific, right?
[8.04 --> 13.62]  And most of the problems cannot be solved repetitively good enough.
[13.86 --> 20.14]  And many times I tell my team at Beyond Minds that state of the art and models are a critical
[20.14 --> 21.90]  part of the solution, right?
[22.18 --> 23.62]  But they're probably 5%.
[23.62 --> 30.16]  And we need to do a lot of problems to build a system that can deliver in production.
[32.70 --> 35.36]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[35.74 --> 36.30]  We love Linode.
[36.38 --> 37.80]  They keep it fast and simple.
[37.94 --> 40.28]  Check them out at linode.com slash changelog.
[40.50 --> 42.58]  Our bandwidth is provided by Fastly.
[42.94 --> 46.48]  Learn more at Fastly.com and get your feature flags powered by LaunchDarkly.
[46.76 --> 48.48]  Get a demo at LaunchDarkly.com.
[48.48 --> 56.70]  With advancements in AI and deep learning evolving at lightning pace, it's more important
[56.70 --> 60.54]  now than ever to research the best options suited to your unique needs.
[60.94 --> 65.86]  This is particularly true when building custom systems and those systems that are GPU heavy.
[66.30 --> 70.70]  Not only do the applications running on the system matter, but your AI infrastructure and
[70.70 --> 73.48]  budget constraints need to be front of mind as well.
[73.48 --> 80.76]  PSSC Labs, which is an HPC and AI custom solutions provider based in California, has been creating
[80.76 --> 85.22]  high performance computing systems to meet their clients' unique enterprise computing
[85.22 --> 87.22]  challenges for more than 25 years.
[87.78 --> 93.62]  And with cloud computing costs growing at astronomical rates, plus companies increasingly losing control
[93.62 --> 98.36]  of their data security, it is no wonder that enterprises and government agencies need to
[98.36 --> 101.18]  continually look for ways to take back control of their data.
[101.18 --> 107.84]  Solutions from PSSC Labs provide a cost-effective, highly secure, and performance guarantee that
[107.84 --> 111.42]  organizations need to reach their AI and machine learning goals.
[111.94 --> 118.34]  For more information and a free consultation, please visit PSSCLabs.com slash practical AI.
[118.82 --> 123.04]  Once again, that's PSSCLabs.com slash practical AI.
[131.18 --> 137.10]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive,
[137.10 --> 138.40]  and accessible to everyone.
[138.76 --> 142.82]  This is where conversations around AI, machine learning, and data science happen.
[143.08 --> 147.56]  Join the community and Slack with us around various topics of the show at changeon.com slash
[147.56 --> 149.20]  community and follow us on Twitter.
[149.32 --> 150.94]  We're at Practical AI FM.
[150.94 --> 160.22]  Welcome to another episode of Practical AI.
[160.22 --> 162.20]  This is Daniel Whitenack.
[162.34 --> 168.38]  I am a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[168.38 --> 171.70]  Benson, who is a tech strategist at Lockheed Martin.
[171.94 --> 172.62]  How are you doing, Chris?
[172.94 --> 173.80]  Doing great, Daniel.
[173.84 --> 174.48]  How's it going today?
[175.02 --> 176.06]  It's going great.
[176.06 --> 182.98]  And you know, this is Practical AI, and I'm super excited because today's episode is super
[182.98 --> 183.48]  practical.
[183.82 --> 188.26]  We have with us Roy Mekrez, who is CTO at Beyond Minds.
[188.38 --> 194.14]  I saw a talk by him at GTC about garbage in, garbage out, which was really cool.
[194.34 --> 195.60]  So welcome, Roy.
[195.78 --> 198.56]  Really excited to chat about these things.
[199.06 --> 199.28]  Yeah.
[199.40 --> 199.98]  Hi, guys.
[200.14 --> 200.60]  Hi, Daniel.
[200.70 --> 201.28]  Hi, Chris.
[201.28 --> 205.88]  Happy to be here and talk to the audience about some practical AI elements.
[206.06 --> 207.18]  Yeah, definitely.
[207.40 --> 210.72]  You're the right person for this podcast, for sure.
[211.20 --> 213.56]  Your talk, which we'll link in our show notes, for sure.
[213.74 --> 214.50]  It was really good.
[214.58 --> 220.36]  I really enjoyed the practicalities of it, but also the emphasis on, hey, what are some
[220.36 --> 226.70]  of these challenges and blockers that prevent AI from producing value when you're trying to
[226.70 --> 227.26]  deploy it?
[227.66 --> 232.22]  So I'm wondering if maybe before we jump into the specifics of that, if you could just give
[232.22 --> 237.40]  us a little bit of information about how you got particularly interested in that topic
[237.40 --> 240.52]  and ended up, you know, talking about it in that context.
[240.94 --> 241.06]  Yeah.
[241.20 --> 241.48]  Brilliant.
[241.62 --> 245.04]  So again, happy to be here and talk to you about this amazing topic.
[245.18 --> 248.16]  So, you know, I came from an academic background.
[248.16 --> 252.44]  I think in the last 10 years, probably I'm doing computer vision for my living.
[252.44 --> 258.48]  Started in biomedical engineering, working on some medical imaging problems.
[258.66 --> 263.62]  Then I worked a little bit on consultancy, some computer vision project, shifted into
[263.62 --> 271.44]  a PhD in computer vision, wrote several papers, were jumping around between CVPR and ECCV
[272.26 --> 274.44]  and talking about some very...
[275.08 --> 275.74]  Doing the circuit.
[275.74 --> 276.52]  Yeah, exactly.
[276.76 --> 281.12]  Some very academic ideas and some all over the place.
[281.24 --> 284.48]  I published papers on a random set of topics.
[285.30 --> 292.68]  And then I met my co-founder and we detect this problem where the academic research is amazing,
[292.82 --> 292.98]  right?
[293.10 --> 296.08]  3% of all papers in the world are about AI.
[296.24 --> 298.00]  That's just mind-blowing numbers.
[298.00 --> 298.44]  Oh, really?
[298.96 --> 299.76]  That's what I read.
[300.10 --> 300.98]  I need to look...
[300.98 --> 304.04]  Wait, is that like a recent statistic or maybe it's more now?
[304.10 --> 304.46]  I don't know.
[304.52 --> 305.24]  That's pretty amazing.
[305.96 --> 306.36]  Yeah, yeah.
[306.44 --> 307.82]  On a broad topic, right?
[308.06 --> 310.32]  But then in...
[310.32 --> 312.10]  At least in enterprise AI, right?
[312.56 --> 317.36]  Outside Facebook, Google, and Amazon, the use of AI is very low.
[317.54 --> 322.04]  And more severely, they're trying, but there is 90% failure rate.
[322.18 --> 325.60]  There is a colossal problem there.
[326.16 --> 327.08]  Systematical failure.
[327.64 --> 330.00]  And we established Beyond Minds.
[330.02 --> 331.46]  That's the company that I'm...
[331.46 --> 333.44]  It's founder in the last three years.
[333.44 --> 338.52]  And that's what I've been doing for a living in order to bridge that gap between academic
[338.52 --> 341.82]  research and practical AI and production, right?
[341.86 --> 343.40]  And real value from AI.
[343.66 --> 344.42]  That's my passion.
[344.56 --> 347.00]  That's what I'm doing as a CTO, as a co-founder.
[347.16 --> 348.98]  That's the company that I'm trying to build.
[348.98 --> 356.98]  And we're coming from a very technical data science, machine learning, AI background, both
[356.98 --> 361.50]  me and the CEO, which is also coming from an electrical engineering background.
[361.50 --> 364.00]  And we understand AI.
[364.18 --> 365.14]  We understand the concept.
[365.66 --> 369.92]  We build many, many different models, train lots of problems.
[370.60 --> 375.46]  But the reality, where it meets the reality, there is a gap there.
[375.64 --> 376.76]  There are challenges.
[377.34 --> 380.32]  And if we want, we can dive a bit more into these challenges.
[380.32 --> 381.82]  But they are not organizational.
[382.18 --> 383.50]  They are technical problems.
[383.50 --> 384.18]  Yeah.
[384.98 --> 390.86]  And I'm curious, since you did that sort of circuit of the academic research and published
[390.86 --> 398.94]  many things, but now you're sort of helping clients productionize and operationalize their
[398.94 --> 405.84]  models now, because I'm assuming you probably still read some of that research and keep up
[405.84 --> 406.24]  with it.
[406.24 --> 411.58]  Now, when you look at that research, do you read papers differently or look at what people
[411.58 --> 417.46]  are doing differently in the sense of understanding what might be able to create value in the
[417.46 --> 419.38]  enterprise versus not?
[419.82 --> 422.02]  That's a philosophical topic.
[422.32 --> 427.20]  What is the role of academia versus the role of the industry around AI?
[427.42 --> 435.08]  And I think it's good that academia is dealing with holistic problems, theoretical problems.
[435.08 --> 436.54]  That's its role, right?
[436.68 --> 441.22]  And I think, you know, in AI specifically, we are shifting towards different areas around
[441.22 --> 443.34]  more practical AI academic research.
[443.82 --> 450.44]  Definitely when the number one affiliate or the right AI is Google, and probably the second
[450.44 --> 451.36]  one is DeepMind.
[451.44 --> 453.62]  And then, you know, some other universities.
[453.80 --> 459.50]  But in general, I think it's good to have people that are dealing with SOTA, right?
[459.60 --> 460.40]  State of the art.
[460.40 --> 466.22]  And I had this discussion with another, with my supervisor during my PhD yesterday.
[467.32 --> 475.24]  And she told me that, you know, they're dealing with SOTA on one hand, but very down to earth,
[475.40 --> 482.06]  algorithmical way of thinking what is needed to solve that problem, not what is state of
[482.06 --> 482.46]  the art.
[482.60 --> 485.58]  And that's a completely different mindset, right?
[485.58 --> 489.18]  And, you know, it could be that there are people that like different things.
[489.50 --> 492.60]  And I think, by the way, that's probably one of the problems, because if you are an insurance
[492.60 --> 498.42]  company and you've built your center of excellence, and you went to Stanford and MIT and brought
[498.42 --> 505.70]  the best data scientists and PhDs from there, it's probably not likely that these people will
[505.70 --> 510.78]  know how to build a product in production that can actually deliver.
[510.78 --> 515.90]  They can do amazing research and novelty and innovation, right?
[515.96 --> 519.88]  But not necessarily deal with some production elements.
[520.30 --> 520.40]  Yeah.
[520.56 --> 526.40]  The last, my day, just to be transparent on this, was like, sure, I thought my day was
[526.40 --> 532.36]  going to involve doing some AI, but really I just tried to convert audio files off of an
[532.36 --> 537.56]  RTSP stream into like a usable format into it and not get garbage out.
[537.70 --> 538.96]  That was basically my day.
[538.96 --> 541.20]  I didn't train anything.
[541.58 --> 544.54]  I didn't even pre-process, you know, anything major.
[544.88 --> 547.38]  I just worked on like this file conversion.
[548.32 --> 548.72]  Yeah.
[548.82 --> 551.14]  On the other hand, by the way, you mentioned papers, right?
[551.28 --> 552.94]  My rule of thumb is paper a day.
[553.08 --> 558.12]  I read paper a day, not, you know, not deeply, maybe deeply like every week, once, two weeks.
[558.48 --> 563.30]  But I want to read an abstract, look at the figures, understand the concept once a day.
[563.30 --> 567.86]  And, you know, we all the time use open source, new ideas.
[568.42 --> 575.12]  And many times I tell my team at Beyond Minds, which is more than 50 engineers today, that
[575.12 --> 580.20]  state of the art and models are a critical part of the solution, right?
[580.20 --> 581.94]  But they're probably 5%.
[581.94 --> 589.06]  And we need to do a lot of problems to build this system that can deliver in production.
[589.32 --> 592.44]  I think that's, you know, in essence, that's my belief, right?
[592.58 --> 594.50]  From a model to a system.
[594.86 --> 598.44]  The model is maybe the heart, but there are so many different components there.
[598.44 --> 602.56]  You know, while we're talking about that, you've said several things that really, really grabbed
[602.56 --> 603.90]  me in the last couple of minutes.
[603.90 --> 607.86]  And we talked about the difference in academia and industry and stuff.
[607.88 --> 609.86]  And we also noted that there's that crossover.
[610.06 --> 614.16]  You have, you know, you have Google going into Stanford and cleaning out the department
[614.16 --> 618.30]  and pulling all of those experts in so they can take advantage of it.
[618.30 --> 622.48]  And so we're seeing a little bit of a difference in this practical when, you know, when we talk
[622.48 --> 628.18]  about garbage in, garbage out and the incredibly practical nature of this as data science.
[628.44 --> 633.90]  We are seeing a divide in industry where you do have academia and you have a kind of a
[633.90 --> 639.66]  select group of organizations that understand this and that they are able to do it and that
[639.66 --> 644.72]  they can take an idea all the way through the work stream and produce that system that's
[644.72 --> 645.96]  highly productive down the road.
[646.12 --> 651.14]  But then you're also seeing a large number of organizations, probably well over 99% of them
[651.14 --> 653.34]  out there that are really struggling with that.
[654.24 --> 658.42]  And before we dive all the way into the details of your talk, which I also saw.
[658.44 --> 660.24]  So I kind of know what's coming.
[660.30 --> 663.64]  I'm looking forward to this, but there's this big chasm right there.
[664.00 --> 665.02]  How is that cross?
[665.06 --> 670.08]  Because the understanding of these, of the data science of it and how to actually do it
[670.08 --> 673.00]  end to end and having all of the steps and skills necessary.
[673.00 --> 673.66]  It's a lot to know.
[673.92 --> 675.10]  It's a lot to know.
[675.44 --> 675.68]  Yeah.
[676.44 --> 677.88]  What are your thoughts about that?
[677.94 --> 679.56]  How does that get reconciled going forward?
[679.56 --> 684.72]  Well, I had a conversation with one of the tier one banks a few weeks ago.
[684.86 --> 688.16]  As part of my role as a CTO, I do a lot of sales meeting.
[688.38 --> 694.94]  I meet clients occasionally and definitely part of our go-to market and vertical is around
[694.94 --> 695.86]  financial services.
[695.86 --> 702.54]  So anyway, a tier one bank in the US, they have 1000 engineers in the center of excellence
[702.54 --> 703.70]  around AI, right?
[704.12 --> 704.36]  Okay.
[704.42 --> 705.78]  So that's tier one bank.
[705.92 --> 712.32]  But even if you go to tier two bank, let's say, you know, fortune 1000 company, right?
[712.32 --> 715.84]  They will build a center of excellence with tons of engineers.
[716.22 --> 722.58]  They will give a good emphasize on bringing people and talent and organizational elements,
[722.74 --> 726.72]  strategy and educating the executives, et cetera, et cetera.
[727.18 --> 727.30]  Yeah.
[727.56 --> 732.92]  But they are still struggling for some complex elements.
[733.16 --> 737.88]  And I think the big element is becoming a technology driven company, right?
[737.88 --> 740.96]  Because Google and Amazon are not on the same challenges.
[740.96 --> 745.20]  But that's extreme cases, but also not other technology companies.
[745.80 --> 750.62]  I think when it comes to technology driven companies, people that understand that, understand
[750.62 --> 752.78]  engineering in their essence, right?
[752.80 --> 757.94]  That the product is technology versus the product is bank or insurance or manufacturing
[757.94 --> 761.98]  or telco or mining or oil and gas or whatever.
[762.26 --> 763.44]  Most of the world, right?
[763.50 --> 764.34]  Most of the economic.
[765.02 --> 769.16]  They are not technology companies and building a technology company, that's super complex,
[769.16 --> 769.52]  right?
[769.52 --> 772.02]  And it's not unique to AI in my point of view, by the way.
[772.24 --> 778.70]  If you look at, I don't know, CRM or ERPs in the late 90s or beginning of 2000, right?
[778.90 --> 785.04]  So many people spent $5 million on trying to build CRM and then they bought Salesforce, right?
[785.40 --> 790.66]  And then, you know, that's a super classic buy versus build dilemma, which I think we are
[790.66 --> 795.38]  super not balanced in AI for sure.
[795.38 --> 797.42]  And for good reason, by the way.
[797.64 --> 802.66]  That's one of my key assumptions as a company, my key observation about AI, if you want to
[802.66 --> 803.72]  can tell you about that.
[803.72 --> 804.28]  Absolutely.
[804.72 --> 806.42]  Could you go into that in a little bit more detail?
[807.22 --> 808.02]  Yeah, for sure.
[808.26 --> 809.80]  He's got us pulling it out of the way.
[809.88 --> 810.02]  Yeah, I know.
[810.90 --> 812.40]  You put out the carrot there.
[812.40 --> 813.92]  Specificity.
[814.44 --> 822.02]  Problems, data, requirements, business process, constraints are so specific, right?
[822.10 --> 828.14]  And most of the problems cannot be solved repetitively good enough, right?
[828.26 --> 833.40]  Even if you take something that sounds super repetitive, defect detection in manufacturing,
[833.68 --> 833.88]  right?
[833.88 --> 839.82]  We need to collect data, annotate bounding boxes, and then train YOLO, right?
[839.96 --> 841.86]  And we have a defect detection, right?
[841.90 --> 843.16]  We have an object detector.
[843.86 --> 844.26]  Amazing.
[844.98 --> 848.94]  But the reality shows that, you know, that's so different for production.
[849.14 --> 854.56]  One is defects that are glass for smartphones, and the other one is PCB bolts.
[854.56 --> 862.36]  And then you have anomalies type of data, and you have very clear defined effects, and transparency,
[862.82 --> 866.80]  and light, and what is the dynamic of the data?
[866.98 --> 869.28]  Is it shifting, or it's very consistent?
[869.82 --> 872.44]  How you deal with the monitoring of that problem?
[872.60 --> 878.44]  Do you have, if it's a, is it bottles, shampoo bottles that you don't really care about the
[878.44 --> 878.80]  accuracy?
[879.06 --> 881.08]  If it's more than 95, you're okay?
[881.08 --> 887.98]  Or it's PCB boards that go into Lockheed Martin engines, and you are super sensitive, like
[887.98 --> 890.64]  zero tolerance to errors, right?
[890.72 --> 893.00]  You have human in the loop, you don't have human in the loop.
[893.34 --> 900.70]  Is that a super 10 GPUs per production line, and you have the most amazing model?
[901.24 --> 907.88]  Or it's a small IoT device that you need to shrink, and quantize, and optimize, and deploy
[907.88 --> 909.16]  in C++, or whatever?
[909.16 --> 915.56]  So many different requirements, and constraints, and how the business is working, how many people,
[915.76 --> 917.58]  and you need to deal with that, right?
[917.82 --> 919.20]  And how you deal with that?
[919.50 --> 924.26]  If it cannot be solved by an off-the-shelf product, I cannot go and buy something.
[924.78 --> 927.44]  So, okay, let's build an internal team, right?
[927.46 --> 928.46]  They will solve my problem.
[928.76 --> 934.04]  But then you come to another problem, which is how internal teams are becoming a technology
[934.04 --> 935.04]  company, right?
[935.12 --> 941.08]  How to deal with data, how to build processes, how to build repetition, scale, all these elements
[941.08 --> 946.20]  that are usually the mindset of startups, of technology companies.
[947.04 --> 950.22]  And that's what I'm trying to bridge in life, right?
[950.26 --> 955.16]  Helping enterprise bridging AI into production, right?
[955.16 --> 956.70]  I can give you an example.
[956.86 --> 963.52]  I have a company that built something regarding sales prediction, and they have 30 different
[963.52 --> 966.20]  lines of sales, 30 different products.
[966.62 --> 968.72]  And they build an amazing model for one product.
[969.14 --> 974.00]  And scaling that to 30 required them to multiply the team.
[974.00 --> 979.84]  Because they need, for example, someone that all his life holds his responsibility as a data
[979.84 --> 986.10]  engineer or a junior data scientist or whatever, to retrain the model every week because there
[986.10 --> 989.98]  is new data, something is changing, the hyperparameters need to be tuned.
[990.30 --> 991.38]  How you do that now?
[991.54 --> 992.52]  Multiply by 30.
[993.12 --> 993.42]  Scale.
[1004.00 --> 1012.88]  This episode is brought to you by Snowplow Analytics.
[1013.42 --> 1017.20]  Snowplow is the behavioral data management platform for data teams.
[1017.58 --> 1023.34]  Maximize the value of your behavioral data using Snowplow Insights, a managed data platform
[1023.34 --> 1028.26]  that's built on leading open source tech leveraged by tens of thousands of users.
[1028.68 --> 1033.22]  Capture and process high quality behavioral data from all your platforms and your products
[1033.22 --> 1035.86]  and deliver that data to your cloud destination of choice.
[1036.20 --> 1040.64]  When marketing needs to make data-informed decisions, when product needs next-level understanding,
[1040.94 --> 1045.62]  and when analytics needs rich and accurate data, Snowplow is the solution for data teams
[1045.62 --> 1050.54]  who want to manage the collection, processing, and warehousing of data across all their platforms
[1050.54 --> 1051.16]  and products.
[1051.50 --> 1055.58]  Get started and experience Snowplow data for yourself at SnowplowAnalytics.com.
[1055.58 --> 1058.52]  Again, SnowplowAnalytics.com.
[1063.22 --> 1081.24]  I think that the way that you think about specificity and scaling a data team is definitely
[1081.24 --> 1082.64]  a good perspective.
[1082.64 --> 1088.08]  I mean, we just talked on our conversation between Chris and I about GitHub Copilot and
[1088.08 --> 1091.52]  like, oh, you know, there's people like, oh, now AI is writing our code.
[1091.70 --> 1095.84]  And, you know, people have been saying that like software engineers were going to automate
[1095.84 --> 1099.06]  themselves away for however many decades it's been.
[1099.06 --> 1099.88]  A long time now.
[1100.30 --> 1105.46]  But, you know, there's such a need for specific solutions to specific problems in even just
[1105.46 --> 1106.40]  software engineering.
[1106.58 --> 1106.78]  Right.
[1106.78 --> 1112.28]  And then if you bring AI into that, which AI is now sort of, like you said, infiltrating
[1112.28 --> 1117.62]  all of these different companies at all different sizes and all different ways in very specific
[1117.62 --> 1120.40]  ways, then there's a lot to solve there.
[1121.06 --> 1125.52]  One of the things that I saw you talked about a little bit was this idea of stability.
[1125.98 --> 1132.56]  Could you give us a sense of, you know, what does stability mean in the world of maybe
[1132.56 --> 1137.14]  in the world of software engineering, but then moving into the world of AI, how is stability
[1137.14 --> 1142.36]  something that needs to be, you know, on our minds as we productionize AI?
[1142.74 --> 1143.18]  Yeah, sure.
[1143.30 --> 1148.42]  So, you know, I think if you're coming from an electrical engineering background, so stability
[1148.42 --> 1153.28]  is something that is usually defined for, let's say, linear system or something like
[1153.28 --> 1153.70]  that, right?
[1153.78 --> 1156.36]  A bounding input, bounding output or something like that.
[1156.36 --> 1163.08]  But definitely in deep learning system, which are far from linear and far from being well
[1163.08 --> 1169.98]  understanding sense of what is bounding even, what's going on with the data in terms of stability?
[1170.24 --> 1172.68]  What data is going to break my model, right?
[1173.14 --> 1179.36]  And you clearly know as a data scientist that AI is usually when it fails, it fails silently,
[1179.60 --> 1179.84]  right?
[1180.40 --> 1182.70]  I gave it in the video if you watch it, right?
[1182.78 --> 1185.20]  So I call it the giraffe problem, right?
[1185.20 --> 1188.84]  The most naive classifier probably that you did when you-
[1188.84 --> 1190.48]  You got to tell that joke from your video.
[1190.62 --> 1191.72]  You have to tell it, okay?
[1191.86 --> 1192.64]  I will do my best.
[1192.72 --> 1192.84]  Yeah.
[1192.96 --> 1194.66]  So the giraffe problem, right?
[1195.16 --> 1199.98]  A giraffe enters a bar and the bartender is your classifier, basically.
[1200.50 --> 1204.34]  And he tells the giraffe, you are 100% a dog.
[1204.58 --> 1206.26]  I'm sure of it, right?
[1206.26 --> 1212.56]  And you know, that's the reality in deep learning because the model as the bartender, right?
[1212.94 --> 1215.42]  He saw only cats and dogs.
[1215.56 --> 1216.46]  That's what he knows.
[1216.82 --> 1221.96]  And he will classify everything as a cat or a dog, even if it's a giraffe.
[1221.96 --> 1227.42]  And let's say as an extreme toy example, but the reality is full of this problem.
[1227.80 --> 1229.32]  Data shifts, noise.
[1229.82 --> 1231.64]  Someone changed the light bulb.
[1232.14 --> 1238.56]  The bias in the image is slightly shift by two gray levels, right?
[1238.88 --> 1242.42]  The text is one tab corrupted, right?
[1242.78 --> 1243.00]  Yeah.
[1243.44 --> 1243.92]  Et cetera.
[1244.04 --> 1245.08]  And how do you deal with that?
[1245.08 --> 1254.92]  There is no practitioner of deep learning, I think, who has done any amount of work in the field who's going to not recognize the reality that that joke represents.
[1255.40 --> 1255.58]  Yeah.
[1255.66 --> 1256.34]  That is true.
[1256.38 --> 1257.60]  We have all experienced that.
[1257.68 --> 1257.86]  Yeah.
[1257.90 --> 1259.12]  I always use the example.
[1259.26 --> 1269.06]  It's like if you trained a self-driving car to drive perfectly, but you did it in Sweden, and then you take that car and you plop it down in Australia.
[1269.06 --> 1275.06]  The first time you run across a kangaroo running across the road, something very interesting is going to happen.
[1275.44 --> 1278.44]  I mean, maybe something really bad or just something really interesting.
[1278.84 --> 1280.38]  But yeah, it occurs also.
[1280.58 --> 1284.98]  I mean, we're talking a lot about images, but also for text and other things as well.
[1285.10 --> 1285.38]  Definitely.
[1286.30 --> 1286.54]  Yeah.
[1287.06 --> 1292.74]  And I think stability is well coupled with the ability of the model to generalize, right?
[1292.74 --> 1301.54]  But hypothetically, you have a data set that is the only distribution of whatever, and you can generalize well, right?
[1301.58 --> 1303.62]  But that's clearly not practical.
[1303.62 --> 1308.84]  You don't have access to the entire distribution, and you cannot generalize to the entire distribution, obviously.
[1309.46 --> 1310.94]  And you definitely don't have labels.
[1311.14 --> 1315.66]  But when you shift into practice AI, I don't care about generalization.
[1315.66 --> 1327.66]  I want to be good on what I need to be good at and make sure that nothing that's out of that good will come into my model, right?
[1327.88 --> 1330.24]  And that's why I call it garbage in, garbage out, right?
[1330.24 --> 1334.08]  I want to make sure that I have a training set.
[1334.30 --> 1335.72]  I have its distribution.
[1336.46 --> 1339.00]  And that's the data that I'm going to get.
[1339.16 --> 1340.92]  How are we going to achieve that, right?
[1340.92 --> 1350.82]  And I think that's one of the most important problems that cause this failure rate, the 90% failure rate that I talked about in the beginning.
[1351.00 --> 1365.08]  Because AI researchers, data scientists, they know how to build models, and they can achieve this 95% accuracy in the lab, for sure, with a stable, static data set, right?
[1365.08 --> 1372.70]  The production is not stable, is not static, and it's definitely dynamic, and it's going to shift.
[1373.02 --> 1377.98]  Data drifts, data shifts, whatever something is going to change.
[1378.40 --> 1380.90]  And how you react to the changes.
[1381.76 --> 1390.82]  And why it's important, by the way, I think while we're progressing with value around AI, we're also shifting from, let's say, statistical applications,
[1390.82 --> 1401.60]  which I define as something where the difference between 80 or 81 or 82% accuracy is, okay, nice, better to the business.
[1402.26 --> 1404.82]  But there are mission-critical problems.
[1405.06 --> 1411.10]  Claim assessment in insurance, anti-money longing, fraud detection, defect detection in PCB boards, whatever.
[1411.98 --> 1413.40]  These are mission-critical, right?
[1413.40 --> 1417.64]  You know, the difference between 80 and 81 is critical.
[1417.88 --> 1419.56]  It could be massive to the business.
[1419.90 --> 1424.80]  And I'm not even talking about applications where the business requirements is 99.
[1425.42 --> 1426.56]  I need 99.
[1426.90 --> 1428.12]  The model can achieve 90.
[1428.18 --> 1428.90]  What do you do now?
[1429.30 --> 1431.28]  And that can be bridged, right?
[1431.62 --> 1432.96]  And there is a way.
[1433.64 --> 1439.40]  Yeah, I think that now that AI is intersecting with all of those different areas,
[1439.40 --> 1449.34]  I mean, you don't have to go far in a business to encounter one of those problems where if you do behave massively different than you did in the lab,
[1449.42 --> 1452.80]  then you're going to make a major impact to the business for sure.
[1453.40 --> 1464.94]  I'm wondering, you mentioned this sort of idea that, you know, you want to make sure that the input that you give to your model is something that you expect in your input distribution.
[1464.94 --> 1473.14]  I'm wondering how maybe that mindset compares to people talk about making their models robust,
[1473.34 --> 1480.56]  and you see people like maybe perturbing their image data sets to like flip them all around or enlarge certain things.
[1480.56 --> 1488.42]  Or maybe like there's that open AI example where the robot's moving the Rubik's Cube and they poke it with a stick or a stuffed giraffe.
[1488.64 --> 1491.20]  You know, giraffes are a major theme in this conversation, I guess.
[1491.20 --> 1500.94]  But one approach seems to be thinking about like making your model able to sort of withstand or be robust against perturbations.
[1501.10 --> 1506.24]  And maybe the other is concerned with making sure that your model never sees things that it shouldn't see.
[1506.68 --> 1511.64]  Is that a proper distinction or how would you sort of look at those two approaches?
[1512.88 --> 1515.10]  Yeah, I think it's a good way of putting that.
[1515.10 --> 1523.20]  You know, I'm sure all the audience, including you two, are following Andrew and Ryan, you know, data is the important part here.
[1523.50 --> 1528.24]  And, you know, if I can control the data, I can control the model and better data, etc.
[1528.66 --> 1530.40]  Super important elements, right?
[1530.74 --> 1535.90]  And, you know, in the ideal world, I want to have access to all the data that I need in the lab.
[1535.90 --> 1538.66]  And I want the data in production to be static, right?
[1538.82 --> 1539.16]  Ideally.
[1539.16 --> 1544.32]  And unfortunately, that's not practical in many, many areas, right?
[1544.38 --> 1545.82]  And we can do our best.
[1546.52 --> 1561.84]  By the way, I think that's one of the key considerations of tech companies that make them better is because data as a strategy is so, so significant within what they're doing from the very first mindset, right?
[1561.84 --> 1563.74]  How are you going to collect the data?
[1564.04 --> 1565.08]  Is it going to be clean?
[1565.14 --> 1566.22]  How are you going to train?
[1566.66 --> 1568.96]  Down the line, amazing AI models of that.
[1569.12 --> 1574.10]  And not, okay, let's look at the entire organization, what data I have, what I can do with AI now.
[1574.36 --> 1583.86]  So what kind of strategies do you have to deal with that in the sense of, so, you know, we have this capability to produce these models in some sort of controlled environment.
[1584.08 --> 1587.20]  They're going out there in the world and they're being subjected to this.
[1587.26 --> 1589.56]  What are some of the strategies that you use to address that?
[1589.56 --> 1590.20]  Yeah.
[1590.20 --> 1598.96]  So the two most critical elements that I think are very, very straightforward, but not easy to build out of distribution detection.
[1599.18 --> 1604.04]  I want to make sure that the data that comes into the model is within the distribution.
[1604.58 --> 1611.12]  Now, let's say quite, let's say it's not super new research area, but it's not super, super advanced.
[1611.12 --> 1618.50]  So I think there is active research out of distribution detection and how to apply it to some kind of areas.
[1618.50 --> 1629.36]  But if you can build this amazing filter that can detect data that is out of distribution and make sure that it's not going into the model, detect the giraffes, right?
[1629.36 --> 1633.80]  With respect to the cat and dog's images, you will be better.
[1634.12 --> 1638.28]  Then you have the other part, which is confidence or uncertainty.
[1638.28 --> 1641.04]  The research call it uncertainty estimation.
[1641.04 --> 1647.04]  I like the term confidence estimation because it's more straightforward and not the negative.
[1647.04 --> 1650.80]  So if you have good confidence of prediction, right?
[1650.80 --> 1654.80]  I got an image, went to the model and then the model gives me the prediction, right?
[1654.80 --> 1657.80]  Soft marks, classification, whatever, right?
[1657.80 --> 1664.18]  It's probably 95% sure about that in terms of probability.
[1664.18 --> 1666.42]  And well, that's not good.
[1666.42 --> 1668.76]  I'm putting in the air here that-
[1668.76 --> 1669.66]  Air quotes there.
[1669.66 --> 1670.38]  Air quotes.
[1670.38 --> 1675.36]  Yeah, that is not really probability, of course, but it's clearly not, right?
[1675.36 --> 1676.38]  That's part of the problem.
[1676.38 --> 1680.12]  And I want to estimate if the model is sure about this prediction, right?
[1680.12 --> 1686.22]  This usually term uncertainty estimation or confidence and how to scale that and how to calibrate that
[1686.22 --> 1688.84]  and the temperature scaling, whatever.
[1688.84 --> 1695.72]  These techniques enable you to say, wait, the model is suddenly not that sure that it's a dog.
[1695.72 --> 1698.06]  And I can really use that number.
[1698.06 --> 1704.34]  And going back to the mission critical elements, now I can threshold something and make sure that
[1704.34 --> 1708.52]  if the confidence is below the threshold, let's pass that to a human, right?
[1708.52 --> 1714.54]  I have a human in the loop in many applications, but I not necessarily know to use it efficiently.
[1714.54 --> 1720.16]  So if I know how to use it efficiently because I have the out of distribution detection and I have confidence estimation,
[1720.16 --> 1725.84]  so I can now make sure that my model is somewhat now more stable.
[1725.84 --> 1728.88]  It has its defense mechanism.
[1728.88 --> 1730.54]  Garbage won't come in.
[1730.54 --> 1736.70]  And if semi-garbage will come in, I will have a confidence code that will tell me, hmm, suspicious.
[1736.70 --> 1746.12]  And that will improve my stability, 100%, and it will improve my ability to combine this model with human,
[1746.12 --> 1748.70]  which is super important in many applications.
[1748.70 --> 1769.32]  Changelog++ is the best way for you to directly support practical AI.
[1769.32 --> 1775.82]  Join today and unlock access to a private feed that makes the ads disappear, gets you closer to the metal,
[1775.82 --> 1779.94]  and help sustain our production of practical AI into the future.
[1780.74 --> 1788.98]  Simply follow the Changelog++ link in your show notes or point your favorite web browser to changelog.com slash plus plus.
[1789.32 --> 1793.18]  Once again, that's changelog.com slash plus plus.
[1794.66 --> 1796.94]  Changelog++ is better.
[1799.32 --> 1806.32]  Changelog++ is better.
[1806.32 --> 1814.06]  So you talk about these sort of two filters, one on the data coming in, out of distribution filter,
[1814.06 --> 1819.34]  and one on the data coming out of the model in terms of quality estimation or confidence scoring
[1819.34 --> 1824.20]  or risk assessment of the output of your model and forwarding that onto humans.
[1824.20 --> 1840.38]  In your experience working with companies, one of the things that I'm always curious about is how you start to judge what you should show to humans versus what you shouldn't show to humans
[1840.38 --> 1849.02]  and figuring out where that threshold is because if you go one way too far, then maybe you're letting garbage through, right?
[1849.02 --> 1853.32]  And that's causing actual problems in your systems and all of that.
[1853.62 --> 1863.48]  If you go too far the other way, then you sort of start eating away at the maybe the good graces that you've built up in terms of making things more efficient.
[1863.66 --> 1870.58]  Well, now you're just sending all of this stuff to humans and, you know, maybe it was all right and they're not changing much about the output.
[1870.58 --> 1873.76]  How do you sort of dial in that sort of system?
[1874.18 --> 1878.54]  Yeah, well, you know, I don't have an amazing rule of thumb to answer your question.
[1878.68 --> 1889.76]  But what I can say that is it's this mindset of AI solution in an organization is not a technical problem per se.
[1889.76 --> 1900.24]  It's a business technology problem that combines some business decisions, business process and technology understanding.
[1900.58 --> 1911.82]  And I think if we go back like three years to 2018, I think the first wave of AI challenges were characterized by understanding where to start,
[1911.94 --> 1916.76]  what AI can do, understanding of manager and executives about AI.
[1916.76 --> 1926.84]  But while we're progressing in that and we have better and better decision makers that understand AI and responsible AI and what AI can deliver.
[1927.36 --> 1934.62]  And they did some AI for managers course at whatever university or online course.
[1934.94 --> 1942.86]  And we can have this open discussion and product managers that are understanding technology, but understanding also the business.
[1942.86 --> 1947.66]  And I think, you know, I think even today we have the AI product manager role, right?
[1947.76 --> 1950.14]  That exists in some companies, which is amazing.
[1950.34 --> 1955.40]  And that's enabled us to take better decision to develop better products, right?
[1955.72 --> 1957.10]  That are driven on AI.
[1957.28 --> 1959.24]  I think that's the main take, right?
[1959.38 --> 1965.14]  You need business people from stage one along the way, right?
[1965.34 --> 1969.94]  To take decision, to be involved in what technology can develop.
[1969.94 --> 1972.14]  So I love where you're going there.
[1972.26 --> 1984.48]  And I actually want to go there even a little bit farther with you, if you would, because as we've come through the conversation and you've kind of delineated these strategies, you know, both on the front end and on the back end to solve both sides of that.
[1984.92 --> 1990.04]  You know, let's bring it back to this practical aspect of you're in your business and you're trying to get some stuff done.
[1990.04 --> 1994.50]  And you have a product manager who's trying to contend with this.
[1994.86 --> 2005.16]  What are some of the things that you have seen in the market to actually try to implement these strategies and thus mitigate the problems that we're talking about in real life?
[2005.20 --> 2012.96]  And I'm not saying it's holistic or a complete list, but what are some practical things that listeners who might be facing their own set of problems want to do?
[2012.96 --> 2017.82]  You know, whether it be data engineering on the front end of some sort or what have you seen?
[2018.50 --> 2020.38]  Well, here I have a rule of thumb.
[2020.92 --> 2022.66]  Don't do POCs, right?
[2022.98 --> 2028.28]  Try to avoid as much as possible from building this model in the lab, right?
[2028.44 --> 2028.70]  Yes.
[2028.80 --> 2033.46]  Try to understand what are the production challenges from day one.
[2033.46 --> 2037.34]  For example, very classical problem is around data, right?
[2037.70 --> 2048.92]  You want to make sure that the data that you are training your model is exactly identical from the data in production or even take the data from production to train on it, right?
[2049.40 --> 2057.54]  And make sure that the acquisition in production of the data or the data that is going to your model is exactly the same, right?
[2057.94 --> 2059.38]  It's the same distribution.
[2059.70 --> 2061.08]  It's the same problems.
[2061.08 --> 2062.52]  It's the same noise.
[2063.12 --> 2065.48]  Try to understand the hardware, the requirements.
[2065.70 --> 2066.76]  Who is going to work with it?
[2066.84 --> 2067.74]  How it's going to work?
[2067.86 --> 2069.52]  Is the data shifting over time?
[2070.04 --> 2071.66]  Do I need to sample differently?
[2072.14 --> 2073.78]  Do I have a monitoring element?
[2074.20 --> 2084.06]  That's bringing me actually to a super important factor about AI in production, which I think is interesting, which is highly related, is evergreen AI, right?
[2084.54 --> 2087.96]  This AI over time, right?
[2087.96 --> 2090.70]  It's not I build a model in product in the lab.
[2090.70 --> 2091.82]  I got 95%.
[2091.82 --> 2092.84]  I put it in production.
[2093.00 --> 2093.54]  I'm happy.
[2093.70 --> 2094.62]  It's bringing me value.
[2094.96 --> 2095.12]  Oops.
[2095.70 --> 2096.72]  Three months passed.
[2096.88 --> 2097.78]  The data was changing.
[2097.98 --> 2099.12]  The model doesn't work anymore.
[2099.60 --> 2105.14]  I need to go back, recollect data, annotate, retrain, deploy again.
[2105.56 --> 2105.92]  Okay.
[2105.92 --> 2107.10]  It's working again, right?
[2107.10 --> 2110.48]  How do you deal with this cycle efficiently?
[2110.48 --> 2114.36]  Because none of the organization is talking about one AI model, right?
[2114.36 --> 2116.12]  That's not the goal anywhere.
[2116.74 --> 2123.10]  We're talking about adoption, acceleration, mass organization change, transformation, et cetera.
[2123.10 --> 2133.00]  And I think Facebook published a few weeks ago that they shift all the models in production to PyTorch.
[2133.22 --> 2134.44]  I think that was the topic.
[2134.66 --> 2138.88]  And the amount of models that they are running is just mind-blowing.
[2138.88 --> 2139.24]  Right?
[2139.98 --> 2149.44]  And, you know, everybody wants to be, not everybody wants to be Facebook, but I mean in terms of the technology-wise and AI-wise, everybody wants to be Facebook.
[2149.50 --> 2150.68]  Wishing they could pull that off.
[2150.68 --> 2150.86]  Yeah.
[2151.30 --> 2151.58]  Exactly.
[2151.58 --> 2157.68]  It's funny that you say that as you're talking about, you know, trying to get to where you're truly reflecting production.
[2157.98 --> 2167.02]  And in my experience working with several organizations, I've often seen an attempt by the data science team working on it to do almost the opposite.
[2167.02 --> 2176.18]  Because they perceive that the ability to get to production data and to move with that is somewhat overwhelming.
[2176.18 --> 2179.52]  It's a daunting thing for them because it's a moving target.
[2179.52 --> 2181.48]  It's incredibly dirty often.
[2181.76 --> 2183.84]  Maybe they're not software engineers.
[2184.04 --> 2184.56]  Absolutely.
[2185.06 --> 2189.36]  And so when you're saying that I'm thinner going, that what you're saying makes perfect sense.
[2189.54 --> 2194.26]  And yet I've literally seen teams trying to do the opposite of that repeatedly.
[2194.64 --> 2197.22]  So, I mean, that's really good advice you're making there.
[2197.46 --> 2197.82]  Yeah, yeah.
[2197.84 --> 2198.96]  I totally agree.
[2199.10 --> 2202.28]  And, you know, you said about the software engineer as a joke.
[2202.28 --> 2212.06]  You know, that's not totally a joke because to build an API that will sample data from production to your training environment and will deploy that efficiently.
[2212.26 --> 2214.44]  That's clearly a software problem, right?
[2214.54 --> 2217.48]  It's and how to do that consistently and monitoring.
[2217.96 --> 2220.60]  That's the scientists build models, right?
[2220.82 --> 2222.70]  And solve algorithmic problems.
[2222.70 --> 2226.98]  But to build a system and et cetera, you need engineers.
[2227.22 --> 2228.76]  You need software engineers, right?
[2229.20 --> 2236.40]  And I think that's at least my belief is that squads are probably the way of solving problems, right?
[2236.52 --> 2237.56]  You need engineers.
[2237.84 --> 2238.62]  You need data people.
[2238.82 --> 2239.82]  You need data scientists.
[2239.82 --> 2245.28]  And you need them to work together on the problem and think about production and think about all the requirements.
[2245.28 --> 2246.86]  And you need product managers, right?
[2246.92 --> 2256.00]  And you need the business people as much as combined with mutual communication, same language, if possible, right?
[2256.36 --> 2257.98]  In order to tackle this problem.
[2258.62 --> 2263.58]  And I think take, for example, something that is all the time coming again and again.
[2264.80 --> 2266.96]  Security and governance, right?
[2267.02 --> 2270.98]  And maybe like if we're going to financial services regulation, right?
[2270.98 --> 2279.52]  I'm sure non-data scientists will take these elements into consideration without the proper guidance and business people shouting at him.
[2279.78 --> 2280.94]  I need explainability.
[2281.62 --> 2289.40]  It doesn't make sense without explainability because I need to show the regulator how this model is taking actions, et cetera, right?
[2289.44 --> 2290.98]  You have risk departments.
[2291.28 --> 2298.34]  And, you know, if the organization become large and complex like a bank, it's become more and more complex to bring AI to production.
[2298.34 --> 2300.28]  And you need more and more elements, right?
[2300.28 --> 2303.90]  So now we need explainability and confidence and out of distribution detection.
[2304.34 --> 2306.18]  And we need to monitor the model.
[2306.18 --> 2311.44]  And we need to make sure that the data is feeding in same from production and training.
[2311.72 --> 2317.02]  And we need to be able to work with the human in the loop and retrain the model, right?
[2317.04 --> 2319.30]  And how to keep these models on the rails, right?
[2319.32 --> 2320.78]  How to deal with maintenance.
[2321.36 --> 2324.02]  So many elements besides the model itself, right?
[2324.02 --> 2329.46]  Going back to what I told you in the beginning, shifting from a model to a system, right?
[2329.50 --> 2330.84]  We need so many different elements.
[2331.42 --> 2332.64]  And then how you scale that.
[2332.72 --> 2333.26]  That's a problem.
[2333.66 --> 2338.14]  It almost sounds like most of the work is after the initial model training.
[2339.14 --> 2340.12]  Who would have thought?
[2340.12 --> 2348.00]  The other thing I'm thinking about while you're discussing this is that it is necessary to bring all of those people together, like you're talking about.
[2348.00 --> 2361.76]  In particular, I think the infrastructure and software engineering and data science people, because software engineers, in terms of the stability that they think of, they think of it like, oh, I'm going to write my unit test, right?
[2361.80 --> 2367.36]  If I change my code and it breaks the test, then I know that I broke my code.
[2367.84 --> 2372.94]  And I also have this table of calls that I'm testing against.
[2373.10 --> 2374.92]  And my API expects this data.
[2375.04 --> 2376.14]  And it either works or it doesn't.
[2376.20 --> 2377.56]  It gets that data or it doesn't.
[2377.56 --> 2391.76]  Whereas in AI, like you're talking about, you know, just testing that your model can take in a certain type of data and output the expected type of data, which is sort of what we would normally think of in testing, isn't enough.
[2391.76 --> 2398.06]  Because the data and the distribution of data that you're feeding in could change the behavior wildly, right?
[2398.06 --> 2408.20]  So that monitoring piece, like the monitoring and testing piece, you sort of say those words to software and infrastructure people and they think of one thing.
[2408.40 --> 2413.12]  But for AI, it is sort of that, but it's not exactly that.
[2413.26 --> 2415.56]  It's that and more, I guess, is what I'm after.
[2415.68 --> 2416.68]  Do you see it the same way?
[2417.06 --> 2417.62]  Yeah, totally.
[2417.62 --> 2425.36]  I think that every one of the problems that I mentioned are both software engineering problem, but also algorithmic problem.
[2425.52 --> 2426.94]  Take monitoring, for example, right?
[2427.50 --> 2430.60]  Every software engineer understands what monitoring is, right?
[2430.68 --> 2434.56]  That's something that they have been doing for 30 years, right?
[2434.62 --> 2435.92]  Monitoring for any system.
[2436.38 --> 2439.96]  You need to make sure logs, et cetera, and understand when it fails, et cetera.
[2439.96 --> 2444.94]  But it's such a complex research problem to monitor a model.
[2445.34 --> 2449.28]  How you make sure when your model is failing, if the data is changing?
[2449.40 --> 2450.58]  These are all research problems.
[2451.00 --> 2460.66]  If the statistic of the data is changing, if the model is suddenly not well suited, where I'm exactly on the distribution versus the data that comes in,
[2461.20 --> 2469.54]  how I'm looking at the vectors that come out of the models and understand what's going on, right?
[2469.96 --> 2470.54]  Of the model.
[2470.76 --> 2475.80]  Or take that into, you know, the hot world today monitoring is observability, right?
[2476.18 --> 2477.74]  It is bringing observation.
[2478.00 --> 2479.22]  What is happening, right?
[2479.26 --> 2482.74]  That's even more complex to understand what is happening and why.
[2483.00 --> 2483.76]  What is failing?
[2484.28 --> 2486.66]  Well, that's become even, you know, more complex.
[2487.16 --> 2488.96]  So people need to work together.
[2489.08 --> 2491.66]  There are many different elements to this problem.
[2491.90 --> 2496.44]  Software, research, data, infrastructure, et cetera.
[2496.44 --> 2505.08]  And my takeaway, that's what I have been doing in the last three years, is building a platform that is dealing with these elements in a unified way, right?
[2505.40 --> 2511.92]  I believe that you can generalize many of these problems in a way that will enable scale, right?
[2512.34 --> 2514.12]  It's required lots of work.
[2514.60 --> 2516.88]  The problems need to be generalized enough.
[2516.88 --> 2521.94]  You need to think about these technology elements across the pipeline of the system.
[2522.52 --> 2523.64]  But that can be done.
[2523.76 --> 2526.00]  Also in a small scale in an enterprise.
[2526.26 --> 2528.70]  But of course, my, you know, I have my own way.
[2529.08 --> 2531.72]  Well, I was going to say, you've brought that up in your own way.
[2531.82 --> 2536.90]  Would you take a moment or two and tell us about the specific work that you've been doing in that area?
[2537.30 --> 2541.36]  I'd love to know how you are tackling these problems that we've been talking about for a while.
[2541.36 --> 2542.46]  Yeah, yeah, sure.
[2542.58 --> 2546.24]  Of course, I won't be able to dive into all the fine details.
[2546.40 --> 2552.68]  But the idea of what Beyond Minds is doing in the last three years, we have been developing a platform, right?
[2552.72 --> 2554.78]  And this platform is not a developer tool.
[2554.80 --> 2565.20]  It's something that we use in order to provide solution to enterprises on scale, faster, better, and crossing and bridging this failure rate, right?
[2565.20 --> 2573.36]  And the components, the main components of this platform is a system that is wrapping the model, right?
[2573.94 --> 2579.44]  Trying to solve problems that are agnostic to the model as much as possible.
[2579.88 --> 2582.10]  Let's take out the distribution, for example.
[2582.58 --> 2583.50]  We have a component.
[2583.98 --> 2585.58]  That's all its work, right?
[2585.66 --> 2595.18]  Out of distribution is one method out of many others that we're using there to measure statistics and data garbage in to make sure that garbage is not coming in.
[2595.20 --> 2596.90]  So we build an entire component.
[2597.22 --> 2598.32]  We call it an input gate.
[2598.94 --> 2599.14]  Yeah.
[2599.32 --> 2604.70]  And it's an entire research arena that is dealing with stability.
[2605.26 --> 2608.12]  And then monitoring and observability, right?
[2608.12 --> 2612.28]  That's another one that is as much as possible model agnostic.
[2612.60 --> 2615.88]  Not all of these components can be totally model agnostic.
[2616.30 --> 2617.60]  Some of them need to be tweaked.
[2617.88 --> 2622.70]  For example, out of distribution detection, that's highly coupled with the data itself, right?
[2623.00 --> 2624.42]  I need to retrain that.
[2624.42 --> 2627.28]  But that's, again, something that can be scaled.
[2627.40 --> 2629.06]  How to retrain, right?
[2629.12 --> 2635.76]  How to do that efficiently, that I can bring solutions to production in a matter of weeks, months.
[2636.30 --> 2643.32]  And I think today, probably 12 to 14 months, I think that's the average time to production in an enterprise.
[2643.86 --> 2648.10]  Our goal as a company to take that into a scale of weeks, right?
[2648.10 --> 2651.90]  12 weeks will be amazing outcome for us.
[2652.24 --> 2655.18]  And that's enabled because of the platform, right?
[2655.68 --> 2657.94]  Building the model, that's what we will have to do.
[2658.10 --> 2659.26]  That is customizable.
[2659.82 --> 2663.08]  But then the monitoring can come easily.
[2663.08 --> 2665.90]  How to combine human in the loop can come easily.
[2666.66 --> 2670.80]  Explainability for most problems that are required that can come easily.
[2671.32 --> 2673.38]  Stability can improve the model.
[2674.02 --> 2676.26]  I have a retraining in production.
[2676.40 --> 2681.16]  I have an entire monitoring and solution management toolbox that we are using.
[2681.16 --> 2686.84]  So I have this entire platform that is wrapping the model and bringing them to production.
[2687.70 --> 2694.40]  It sounds very similar to the conversation that we had with William Falcon around PyTorch Lightning.
[2694.40 --> 2706.86]  One of the things he was observing as he was working with different companies and models is that developers were over and over again fighting with the code that they were writing to deal with the hardware, right?
[2706.90 --> 2712.04]  Like multi-GPUs versus single GPUs versus this GPU versus that.
[2712.86 --> 2722.00]  And so in PyTorch Lightning, the philosophy was to sort of decouple the model piece from that hardware stuff that everybody was trying to write.
[2722.00 --> 2726.00]  And that provided the boost that PyTorch Lightning is giving people.
[2726.44 --> 2737.88]  And it sounds like here there are these other components and actually a very large number of them that data scientists are also spending their time writing code on over and over and over again.
[2737.96 --> 2745.50]  There's the stability, the monitoring, the human in the loop piece, all of these pieces that promote stability and robustness.
[2745.62 --> 2747.14]  And they're having to do this over and over.
[2747.26 --> 2749.00]  So it's not efficient at all.
[2749.00 --> 2762.28]  So I definitely think that, you know, that mindset that you have at Beyond Minds is really interesting in that sense that it could provide that sort of similar boost in these other areas, which is really exciting.
[2762.60 --> 2763.32]  He's bringing good.
[2763.40 --> 2771.30]  I mean, as I was listening to that, the thing that was going through my mind is he's bringing really good architectural decisions to kind of to everyone.
[2771.30 --> 2782.00]  And we have seen that often, you know, people in data science haven't necessarily had that exposure, you know, to the software side where that as it matured, as the field matured, that became part of it.
[2782.40 --> 2789.42]  So I love what you're saying, because I think that really contributes toward the maturing of this industry that we're all in at this point.
[2789.42 --> 2790.24]  Yeah.
[2790.38 --> 2790.66]  Yeah.
[2790.96 --> 2797.34]  And, you know, I mentioned lots of research problem, but there are also many engineering problems there, right?
[2797.52 --> 2807.06]  Kubernetes and Docker and APIs and so many different elements, how to wrap models and deploy them efficiently and fast.
[2807.20 --> 2812.52]  And this is becoming a common practice more and more.
[2812.52 --> 2815.96]  But there are still some elements that are not that trivial.
[2816.60 --> 2820.38]  Well, I really appreciate you helping our listeners think through some of these things.
[2820.60 --> 2832.78]  I know my mind has been racing the whole time thinking about like five different projects that I have going on and how these things map into those projects, like every single one of them, how these things map into that.
[2832.98 --> 2837.98]  So I know it's been really good, good in that sense for me, and I'm sure it will be for our listeners as well.
[2837.98 --> 2843.36]  We'll include show notes in the show notes, links to the talk and other things that you've put out.
[2843.46 --> 2845.28]  But thank you so much for joining us, Rory.
[2845.38 --> 2846.14]  It's been a pleasure.
[2846.48 --> 2847.12]  Thank you very much.
[2847.24 --> 2848.46]  It was a pleasure talking with you.
[2851.90 --> 2853.90]  Thank you for listening to Practical AI.
[2854.24 --> 2856.24]  We appreciate your time and your attention.
[2856.64 --> 2860.32]  If you enjoyed this episode, help us out by spreading the word.
[2860.86 --> 2865.62]  Think of a friend, think of a colleague, somebody who would benefit from listening to it, and send them a link.
[2865.96 --> 2866.98]  We'd really appreciate it.
[2866.98 --> 2870.68]  Practical AI is hosted by Chris Benson and Daniel Whitenack.
[2870.90 --> 2874.44]  It's produced by Jared Santo with music by Breakmaster Cylinder.
[2874.84 --> 2878.02]  Thanks again to our sponsors, Fastly, Linode, and LaunchDarkly.
[2878.20 --> 2878.98]  That's our show.
[2879.44 --> 2882.12]  We hope you enjoyed it, and we'll talk to you again next week.
[2882.12 --> 2909.36]  We'll be right back.
[2909.36 --> 2911.36]  Game on!
