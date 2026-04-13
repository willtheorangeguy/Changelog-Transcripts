[0.00 --> 8.66]  Welcome to Practical AI.
[9.16 --> 16.78]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is
[16.78 --> 19.54]  changing the world, this is the show for you.
[20.24 --> 24.92]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 --> 30.94]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions
[30.94 --> 35.44]  on six continents, so you can launch your app near your users.
[35.84 --> 37.84]  Learn more at Fly.io.
[42.74 --> 45.90]  Welcome to another episode of Practical AI.
[46.24 --> 47.80]  This is Daniel Whitenack.
[47.80 --> 54.68]  I am the founder and CEO at Prediction Guard, and I'm really excited to talk to
[54.68 --> 57.84]  another founder today in the AI space.
[58.04 --> 60.98]  Today we have with us Shahul from Ragas.
[61.08 --> 62.24]  He's one of the co-founders.
[62.42 --> 63.00]  Welcome, Shahul.
[63.12 --> 63.62]  How are you doing?
[64.14 --> 65.40]  Hey, I'm doing good.
[65.64 --> 66.00]  Hi, Daniel.
[66.28 --> 66.80]  Hey, folks.
[67.06 --> 67.64]  What are you doing with me?
[68.46 --> 69.42]  Yeah, yeah.
[69.52 --> 74.36]  Well, thanks for joining at a late hour in India.
[74.62 --> 75.72]  Appreciate that.
[75.72 --> 82.66]  But yeah, I would love to hear a little bit, maybe for those that aren't familiar with what
[82.66 --> 89.12]  you're doing, maybe share a little bit about what that is, and also maybe how you came
[89.12 --> 93.24]  upon the types of problems that you're solving with your current work.
[93.70 --> 93.90]  Sure.
[94.46 --> 96.06]  That's a very good place to start.
[97.18 --> 98.46]  So I bought Ragas.
[98.96 --> 103.22]  Ragas is an open source library for evaluating LLM applications.
[103.22 --> 109.78]  And what we are trying to do with Ragas as an open source library is to provide the developers
[109.78 --> 116.46]  for AI engineers who are building LLM applications, the tools and the workflows that are necessary
[116.46 --> 121.94]  to automate or partially automate the process of evaluation through using different techniques,
[122.10 --> 126.26]  different methods and techniques that we bring out to Ragas.
[126.26 --> 132.52]  And how we came up to the idea of Ragas is basically me and my co-founder, Jaden, we
[132.52 --> 135.62]  have been working in ML for the past six, seven years.
[136.12 --> 140.66]  And when LLMs came out, we were already working with natural-in-made models.
[141.32 --> 145.74]  Jaden mostly worked on the inference and infrastructure point of it.
[146.16 --> 148.40]  And myself, I was working as an applied researcher.
[149.00 --> 152.32]  So we were, you know, practically, we loved it.
[152.56 --> 155.78]  We were practically, you know, doing a lot of experiments with it.
[155.78 --> 161.40]  We were part of different open source initiatives, building LLMs and also using LLMs to build
[161.40 --> 162.76]  different frameworks at that point.
[162.94 --> 167.98]  Even Langchain and Lambda Index was coming out as, you know, one of the earlier frameworks
[167.98 --> 168.74]  at that point.
[168.98 --> 170.78]  This is around early 2023.
[171.62 --> 175.20]  And we were also working with different applications and stuff.
[175.38 --> 180.72]  And Rag was one of the most popular applications that went into production very easily with LLMs.
[180.72 --> 186.10]  And this is one of the first things that LLMs actually opened up as a possibility for, you
[186.10 --> 191.16]  know, enterprises to build something on top of them, which can save a lot of time and money
[191.16 --> 191.52]  for them.
[192.02 --> 193.86]  So we were also building Rags.
[194.96 --> 202.42]  And we, after a couple of experiments with some clients, we found out that, okay, we are
[202.42 --> 206.60]  able to build these LLM applications, this Rags application using any LLM.
[206.60 --> 208.60]  So it has different moving components.
[209.24 --> 213.86]  And going forward, there will be a lot more moving components to any LLM applications.
[214.14 --> 218.46]  Like it will be something like a common system where there are, as you can see now, it's
[218.46 --> 221.32]  like not only Rags, now it's like two use cases.
[221.76 --> 226.14]  There are different versions to, you know, that constitute a common system kind of stuff.
[226.68 --> 231.80]  And we thought, okay, you know, why don't we build something, some evaluation metrics,
[231.80 --> 237.16]  few evaluation metrics that can be used to understand the quality of any Rags application
[237.16 --> 239.54]  that any engineer is building.
[240.22 --> 245.50]  And we also found out that, you know, going through these answers or going through these
[245.50 --> 248.52]  intermediate results manually is not a scalable approach.
[249.14 --> 253.70]  I could rephrase it to say that it's a very boring thing to do and nobody is very keen to
[253.70 --> 254.04]  do it.
[254.44 --> 259.36]  This is something everybody will push into someone else responsibility, but it is something
[259.36 --> 260.14]  very important too.
[260.62 --> 266.26]  So we need thought of identifying methods or coming up with solutions that could help
[266.26 --> 271.82]  developers do the evaluation, but also save them a lot of time while doing it.
[271.96 --> 277.74]  So it should not be something like, you know, it is basically an evaluation of LLM application
[277.74 --> 280.80]  regardless of Rags or any agent workflow.
[280.80 --> 285.14]  It's basically a very tedious process that takes a lot of time if you go through manually.
[285.14 --> 290.22]  We want to make sure that this tedious process, this manual process that takes a lot of time
[290.22 --> 295.34]  is cut down into one by tenth of the time and it should get you the same insights as you
[295.34 --> 296.20]  do manually.
[296.78 --> 301.94]  So that's how we came with our, you know, initial MVP of progress.
[302.20 --> 307.42]  And we have, we released an open source library in the middle of 2023.
[308.08 --> 313.12]  And since then we have been continuously iterating and we have been getting organic growth and
[313.12 --> 314.76]  usage from that point from there.
[315.16 --> 317.10]  And that's, that's what we are going to do.
[317.82 --> 318.62]  Yeah, that's awesome.
[318.62 --> 327.06]  I noticed that you very specifically refer to the evaluation of LLM applications, not necessarily
[327.06 --> 329.56]  the evaluation of LLMs.
[329.82 --> 337.30]  Could you explain like what might be the difference between those mindsets for people that are maybe
[337.30 --> 338.12]  getting into this?
[338.12 --> 343.62]  Maybe they're looking at, they have looked at benchmarks, let's say for like a leaderboard
[343.62 --> 344.78]  for LLMs, right?
[344.82 --> 349.00]  And there's a certain level of, you know, evaluation or benchmarking there.
[349.08 --> 354.74]  But then you're talking about the evaluation of LLM applications.
[354.74 --> 359.48]  So could you help us understand kind of some of the differences there, some of what needs
[359.48 --> 364.74]  to be thought of at the application level versus at the model level?
[364.74 --> 372.20]  So this, this goes to the, you know, ideology of AA as a consumer product as of now, because
[372.20 --> 379.96]  pre-LLMs, nobody, everyone, most of the enterprises or most of the startups who are building AA powered
[379.96 --> 382.80]  applications used to have their own models.
[383.24 --> 387.72]  And they will obviously also have a team of writer scientists who is building and managing
[387.72 --> 388.32]  these models.
[388.32 --> 395.62]  So in that spectrum, the building of the LLM itself or the, you know, model itself and
[395.62 --> 400.64]  also the evaluation of the model itself was the responsibility of the researcher, the
[400.64 --> 404.14]  engineer, slash data scientists who were working on it.
[404.92 --> 408.46]  But now it's known that people are building an LLM application.
[408.60 --> 411.34]  So AA applications is not really building their own models.
[411.64 --> 417.08]  They are consuming models from an external endpoint or even open source models that are being,
[417.08 --> 420.32]  you know, released and building applications on top of it.
[420.58 --> 426.42]  Now this actually forms a wide spectrum where at the left end of the spectrum, there are people
[426.42 --> 428.10]  building the LLMs itself.
[428.10 --> 433.54]  They have a separate list of targets, loss functions, metrics, and benchmarks to evaluate
[433.54 --> 433.84]  one.
[434.34 --> 439.52]  And towards the right end of the spectrum, there are people who doesn't really care about how
[439.52 --> 440.72]  the LLM is built itself.
[440.72 --> 447.04]  They only care about, you know, can this thing which I'm consuming using an API do what I'm
[447.04 --> 449.90]  trying to do here using this AA as a technology.
[450.34 --> 457.44]  Now, when a researcher or an organization like who builds LLM, evaluates LLM, they don't really
[457.44 --> 465.22]  know what is the exact use case for which this AA or LLM is going to be used against or the
[465.22 --> 467.88]  type of data this will be used against.
[467.88 --> 474.48]  When the evaluation is done at the researcher or an LLM builder part of the spectrum, they
[474.48 --> 480.70]  are limited to the evaluation or, you know, testing of this LLM's capabilities on a general
[480.70 --> 481.50]  purpose basis.
[481.86 --> 486.96]  They are not really tailoring this evaluation or testing to your application because they
[486.96 --> 489.82]  don't really have a control over what you are trying to build with it.
[490.14 --> 493.68]  They can only say that, okay, this is a general capability of the model.
[493.68 --> 500.16]  And we know that even the general capabilities of the models and benchmarks are highly leaked
[500.16 --> 501.16]  into the training data.
[501.50 --> 503.66]  And even that is questionable, but that's a different question.
[504.08 --> 507.94]  This is what a researcher or LLM builder does at his end.
[507.94 --> 514.42]  But when it comes to LLM application builder, he can't really, if someone builds a rag or
[514.42 --> 520.92]  a tooling agent on top of an LLM, he can't really say that, okay, the LLM builder has said
[520.92 --> 523.54]  X and X accuracy, so I should get X and X.
[523.54 --> 525.10]  That would be a wild assumption today.
[525.10 --> 531.82]  So what we are trying to do here is giving that user a application builder who is at the
[531.82 --> 538.02]  right end of the spectrum, the power, the tools to evaluate his application without knowing
[538.02 --> 541.76]  so much about ML or getting into so much jargon or anything.
[542.08 --> 547.12]  You want to make it as easy as possible so that as intuitive as possible because most of
[547.12 --> 550.46]  the people who are building applications are not from an ML background.
[550.46 --> 555.22]  They are from a software engineer background or application building application background
[555.22 --> 559.82]  where their specialty is building and scaling this application, not building and scaling
[559.82 --> 560.26]  the models.
[560.78 --> 563.16]  So we are trying to be intuitive as possible.
[563.28 --> 568.38]  We also want to make sure that we do not take a lot of their time while doing the evaluation
[568.38 --> 568.74]  itself.
[568.84 --> 573.26]  We want to make sure that their time is valuable and we want to make sure that we do the heavy
[573.26 --> 574.98]  lifting of this evaluation for them.
[575.64 --> 576.92]  Yeah, that makes a lot of sense.
[576.92 --> 582.88]  And also I'm realizing there's this kind of spectrum that I was thinking about while you
[582.88 --> 583.32]  were talking.
[583.40 --> 589.98]  On the one side, you have kind of data scientists or researchers who are building out benchmarks
[589.98 --> 591.56]  or metrics for models.
[591.92 --> 596.30]  On the other end of the spectrum, you have maybe software engineers who are used to writing
[596.30 --> 599.54]  unit tests or integration tests for their software.
[599.54 --> 607.26]  And then what we're really talking about is integration of LLMs into software applications
[607.26 --> 609.18]  or into certain workflows.
[609.46 --> 618.16]  You talked a lot about kind of this distinction between LLM benchmarks and evaluating LLM applications.
[618.52 --> 620.40]  Could you talk a little bit about the differences?
[620.62 --> 626.14]  Maybe there are software engineers in the audience that maybe they're used to writing unit tests and
[626.14 --> 627.88]  integration tests for their software.
[627.88 --> 634.68]  Now, as a consumer, like you said, they're integrating some LLM functionality or maybe a
[634.68 --> 638.90]  reasoning, you know, a chain of reasoning with LLMs into their software.
[639.40 --> 645.48]  From a practical standpoint, what are the new types of things that they might need to consider
[645.48 --> 650.50]  that are different maybe from the way that they've unit tested in the past or written tests
[650.50 --> 654.84]  in the past now that they're working with these LLM workflows?
[654.84 --> 656.26]  Sure.
[656.34 --> 657.60]  That's a very interesting question.
[658.02 --> 663.54]  So when it comes to the application builder slash software engineer who is building with AI,
[663.88 --> 668.94]  as you said, most of them are already familiar with unit tests and integration tests that they,
[669.06 --> 671.88]  you know, regularly write for their software softwares.
[671.88 --> 683.12]  Now, the major difference is that I also have observed many of the software engineers who are relating to evaluation using this analogy.
[683.26 --> 683.36]  Okay.
[683.50 --> 684.74]  You know, this is testing.
[685.14 --> 691.36]  I am praying I will, you know, learn or understand evaluation using the, you know, my understanding of the testing.
[691.36 --> 695.48]  So, so the thing is that this is a fundamental thing about analogy itself.
[695.48 --> 704.00]  So now you are using analogy to understand one thing, but it could be that these two things can have different physical and chemical different properties here.
[704.00 --> 714.50]  For example, now for when it, when it comes to evaluation and versus traditional software testing, traditional software testing is mostly a discrete space where,
[714.62 --> 717.56]  you know, you have an input, you have an expected output.
[717.56 --> 723.20]  And if you give this input, you are supposed to get this expected output from the software.
[723.48 --> 727.86]  There is no variation in that that satisfies the test.
[728.12 --> 736.12]  Now, you know, if the logic is basically to add one plus one, you should get, if the whole logic is basically addition,
[736.58 --> 739.64]  if you give input as one plus one, the output should be two.
[739.76 --> 745.54]  There is no other possibility that exists that would, you know, satisfy that test case is correct.
[745.54 --> 749.54]  But when it comes to natural language, there is more of a continuous space.
[749.82 --> 763.44]  Like if you have an LLM that does the same thing, let's say one plus one or, you know, addition, LLM could even say two in natural language or two in the decimal point numbers, right?
[763.58 --> 764.68]  So both are actually correct.
[764.78 --> 771.54]  So here there are like a continuous space where the output cannot be exactly matched against or associated against.
[771.54 --> 776.88]  But you should have an understanding, but there is a, in this continuous space of outputs that are possible,
[777.22 --> 780.94]  there is obviously a subset that is actually, can be regarded as correct.
[781.32 --> 785.66]  Obviously, if the LLM gives an answer as three in natural language or something, that means wrong.
[785.74 --> 787.32]  That is out of, out of the bay, right?
[787.32 --> 798.78]  So, so what software engineers should really understand is that when you deal with ML, when you deal with, when you integrate A into your application,
[799.12 --> 806.62]  you should try to think about it as in a continuous space rather than a very discrete space of, or in a black and white manner, you know, it's yes or no.
[806.62 --> 811.90]  It could be that it is like in the middle of, it could, there are like a lot of space in the gray area here, right?
[812.28 --> 816.62]  So, you know, that is what a software engineer should understand.
[816.94 --> 822.16]  And then there is also a non-deterministic part of the whole, you know, A thing.
[822.48 --> 831.18]  Basically, if you have a system, which is a part, which is part of core and part of AI, the system is going to be somewhat non-deterministic, whatever you do.
[831.18 --> 835.04]  So, so this is also something that traditional software is not like that.
[835.18 --> 836.70]  So traditional software is very deterministic.
[836.92 --> 841.50]  So you have an input, you will have an output, given that the intermediate states remain the same.
[841.84 --> 845.92]  So here again, you have this non-deterministic thing to take up core core.
[846.04 --> 847.36]  So that's also one thing.
[847.46 --> 857.54]  These are the two major differences that exist between software testing, traditional software testing, and, you know, this A application or combine A application testing that makes it different from each other.
[857.98 --> 858.96]  Yeah, super interesting.
[858.96 --> 871.70]  And I know in the software world, there's all of these sort of frameworks for development around, you know, test-driven development or data-driven development or these different things.
[871.86 --> 881.32]  I notice in, Ragus, in your core concepts and your documentation, you talk about metrics-driven development for these LLM applications.
[881.32 --> 893.40]  So for those that are maybe developing LLM applications out there, could you describe a little bit the mindset of metrics-driven development, what you mean by that?
[893.54 --> 900.68]  And then maybe we can get into a few more of the details of Ragus itself and how you enable that framework.
[900.68 --> 908.22]  Yeah, metrics-driven development is highly, you know, it's a concept that we think from the test-driven development itself.
[908.38 --> 918.72]  So the idea, we want to educate developers and software developers who are more familiar with metrics, but they are familiar with testing to, you know, what we're trying to do here.
[918.72 --> 933.20]  So as I said, metrics versus test is like metrics is like something that delivers a value or, you know, that helps you understand the performance of some application in a scale of, let's say, 0 to 1 or something.
[933.20 --> 947.64]  Now, whenever you have an application, if you want to iterate or, you know, change, let's say you are bumbling and pull an application that consists of different agentic workflows plus Iraq workflow, etc.
[947.92 --> 959.78]  And now let's say you want to change one single prompt or one single function code or something, or even the retriever, how would you understand the effect of this change in your pipeline?
[959.78 --> 962.96]  It's a question that metrics-driven development creates your answer.
[962.96 --> 979.52]  So if you have a metric, if you have a way to kind of objectively quantify or understand the performance of your system before and after this change, you can also understand and analyze the systems, you know, responses or the behavior of the system using these numbers.
[979.52 --> 994.26]  For example, if you are switching out the retriever and let's say you add a set of metrics that effectively quantifies the performance of your system, you could actually switch out the retriever or switch out any function calls or something,
[994.26 --> 1003.26]  and then run the end result once again for the given test set and understand the change in the matrix in particular dimensions.
[1003.26 --> 1014.26]  And, okay, let's say once you observe this change, you could again easily dig down, okay, you could easily fetch these samples for which the change is reflected the maximum.
[1014.26 --> 1017.74]  And then you could easily analyze and then you could easily analyze and understand the matter.
[1017.74 --> 1026.26]  That actually helps and reduces a lot of time when it comes to debugging and testing these applications.
[1026.26 --> 1029.20]  So that's the idea of metrics-driven development.
[1029.26 --> 1029.28]  So that's the idea of metrics-driven development.
[1029.28 --> 1043.90]  What's up, friends?
[1044.00 --> 1049.88]  I'm here with a new friend of ours over at Assembly AI, founder and CEO Dylan Fox.
[1050.32 --> 1056.60]  Assembly AI is where you can turn voice data into insights, chapters, transcripts, summaries,
[1056.60 --> 1060.26]  and so much more with their leading speech AI models.
[1060.84 --> 1064.86]  So Dylan, give me a glimpse into what you're doing with speech AI models at Assembly AI.
[1065.24 --> 1072.08]  So at Assembly, we're building industry-leading speech AI models for various tasks like speech-to-text,
[1072.48 --> 1077.76]  streaming speech-to-text, speech understanding to help developers easily convert voice data,
[1077.88 --> 1080.86]  whether it's live or pre-reported, into super accurate text.
[1080.86 --> 1085.96]  And then to help developers extract a ton of information and metadata around voice data
[1085.96 --> 1089.78]  or even around the text that they just were able to convert from that audio data.
[1089.90 --> 1096.00]  So these are things like picking out entities or PII that was spoken in voice files
[1096.00 --> 1101.70]  or summarizing voice and audio data down into custom summaries.
[1102.00 --> 1106.24]  It's things like being able to detect how many speakers spoke and who said what
[1106.24 --> 1107.94]  and what the names of different speakers were.
[1107.94 --> 1114.48]  So we bundle all those things into a super simple API with really great docs that developers
[1114.48 --> 1119.12]  can just sign up to for free to start, use the API, build into their apps, and then build
[1119.12 --> 1124.16]  these really cool AI apps and products and workflows and automations on top of voice data with.
[1124.22 --> 1125.10]  I dig it.
[1125.18 --> 1125.40]  Okay.
[1125.62 --> 1128.84]  Can you take me a little deeper into the opportunity for developers?
[1128.84 --> 1133.30]  Because it seems like there's a lot of voice data out there and there's a lot of trapped
[1133.30 --> 1135.10]  value in that voice data.
[1135.10 --> 1138.68]  There's so much voice data being created on the internet now.
[1139.62 --> 1145.10]  Podcasts, videos, phone calls, voice messages, audiobooks, virtual meetings.
[1145.28 --> 1145.60]  It's crazy.
[1145.92 --> 1150.94]  And you can now transform and understand all of this voice and audio data in ways that
[1150.94 --> 1153.22]  were not even possible a year, 18 months ago.
[1153.22 --> 1158.36]  So what we're seeing with the help of these new AI models that we're creating at Assembly,
[1158.62 --> 1163.94]  developers and organizations are just racing to build all these new applications, workflows,
[1163.94 --> 1169.52]  automations that leverage the voice data they have either within their organization or within
[1169.52 --> 1174.14]  their product to build really cool new products and services, workflows that are just like
[1174.14 --> 1175.24]  taking off at the market.
[1175.24 --> 1180.26]  So at Assembly, we're building the industry leading models for all those different apps
[1180.26 --> 1184.30]  and workflows, whether it's speech to text or speaker diarization or speech understanding
[1184.30 --> 1190.30]  capabilities to summarize voice data or extract entities from voice data or mask PII from phone
[1190.30 --> 1193.72]  calls for various types of automations that might be built.
[1194.06 --> 1198.50]  And we're exposing that through a super simple, super scalable API that's just constantly being
[1198.50 --> 1200.24]  updated and constantly getting better.
[1200.58 --> 1206.02]  And so we're seeing a crazy amount of developers and companies just build really cool apps and
[1206.02 --> 1208.42]  services on top of our API every day.
[1208.68 --> 1213.44]  It's really only just getting started, especially with the model updates that we have planned over
[1213.44 --> 1215.06]  the second half of the year that are coming out.
[1215.06 --> 1218.14]  They're really excited to launch to the developers on our API.
[1218.64 --> 1218.96]  Okay.
[1219.22 --> 1222.60]  Constantly updated speech AI models at your fingertips.
[1223.00 --> 1225.42]  Well, at your API fingertips, that is.
[1225.74 --> 1227.84]  A good next step is to go to their playground.
[1228.02 --> 1232.12]  You can test out their models for free right there in the browser, or you can get started
[1232.12 --> 1236.84]  with a $50 credit at assemblyai.com slash practical AI.
[1237.16 --> 1241.46]  Again, that's assemblyai.com slash practical AI.
[1245.06 --> 1264.92]  There's a lot that you've already integrated into Ragas, which are really interesting.
[1264.92 --> 1269.90]  And maybe some people have heard of, or some people haven't like faithfulness and context,
[1270.02 --> 1274.96]  recall noise, sensitivity, aspect, critique, summarization score, and more.
[1275.06 --> 1275.92]  That I'm not listing.
[1276.34 --> 1281.78]  I'm wondering if you could maybe just share a couple of those that you think are maybe
[1281.78 --> 1286.96]  most utilized or maybe interesting from your standpoint, just to give a sense of people,
[1287.08 --> 1289.86]  like what types of metrics are we talking about here?
[1289.86 --> 1293.34]  I think it would be beneficial to answer that in an abstract level.
[1293.72 --> 1301.66]  For example, if I say metrics, the whole concept of V-devicing or giving that out approach,
[1301.66 --> 1308.26]  these metrics is that it's not extremely hard to come up with these metrics, but it is when
[1308.26 --> 1314.08]  a software developer or an application developer thinks about evaluation, because he's already
[1314.08 --> 1320.62]  familiar with this concept of putting up metrics, deciding the right flows and everything, it
[1320.62 --> 1323.92]  could take him like two to three days to figure out the right metrics.
[1323.92 --> 1330.36]  So what Ragas does is if you are an application developer, okay, you are developing this particular
[1330.36 --> 1335.28]  type of application, you can come to Ragas and you can go to Ragas metrics.
[1335.28 --> 1342.50]  And there you will find that enough workflows, enough parts in the documentation that can
[1342.50 --> 1347.48]  help you navigate according to use cases, according to your requirements, that can land you up
[1347.48 --> 1349.28]  in the right metrics that you should use.
[1349.28 --> 1356.00]  And the documentation will also provide an intuitive understanding of how this metrics is calculated
[1356.00 --> 1356.58]  underneath.
[1356.58 --> 1359.64]  So these are the two value props that we provide there.
[1359.64 --> 1365.02]  It's not that a developer can easily, you know, a developer or a data scientist could easily
[1365.02 --> 1367.28]  make up these metrics as their own.
[1367.54 --> 1372.50]  But sure, if it is mostly, if you are a software developer application here, it could be very
[1372.50 --> 1375.80]  hard for you to figure out, you know, have to think around all this stuff.
[1375.88 --> 1382.68]  So we are effectively taking that load of you and providing you the, you know, the ways to
[1382.68 --> 1388.60]  easily navigate and understand the right metrics to evaluate your application, tell it to your
[1388.60 --> 1389.60]  application.
[1389.60 --> 1394.88]  Now we are also expanding, we are also expanding the restore metrics to use case and
[1394.88 --> 1396.32]  identity workflows.
[1396.32 --> 1400.18]  And we are also going to, you know, reformulate the whole load on that particular so that
[1400.18 --> 1402.80]  people can easily find the metrics.
[1402.80 --> 1406.24]  What are the metrics that can be LLM based or non-LLM based.
[1406.24 --> 1410.72]  These are all, you know, this, you know, whenever a developer comes to Ragas, he obviously
[1410.72 --> 1413.80]  asked a lot of questions or even think about metrics.
[1413.80 --> 1417.22]  He will ask a lot of questions like, for example, okay, what is my use case?
[1417.60 --> 1421.78]  What are the parts in my application that I want to evaluate?
[1422.36 --> 1428.36]  And then what should I go for LLM based metrics, which has high correlation with human judgment,
[1428.48 --> 1431.24]  but also has its own lack of its own issues.
[1431.24 --> 1435.78]  Like, you know, non-determinism and everything or non-LM based metrics, which are traditional.
[1435.78 --> 1441.00]  So it has less correlation with human agreement or human judgment, but it is, you know, more
[1441.00 --> 1442.00]  reproducible.
[1442.00 --> 1446.70]  So all these questions, all these doubts both pop up in mind when an developer think about
[1446.70 --> 1447.70]  metrics.
[1447.70 --> 1452.54]  We are trying to abstract all that into Ragas metrics and provide the developer a way to
[1452.54 --> 1453.86]  think about metrics.
[1453.86 --> 1460.94]  And with metrics, they are also when they adopt a metric from Ragas, they also have a related
[1460.94 --> 1466.86]  list of items or, you know, features that they can use because they adopted a metrics from
[1466.86 --> 1467.12]  Ragas.
[1467.12 --> 1471.04]  For example, let's say you designed a metrics for language English.
[1471.04 --> 1474.80]  Now, let's say you are evaluating for Portuguese or Spanish.
[1474.80 --> 1481.92]  You will have to, you know, convert it to other language or whatever, you know, whenever you're
[1481.92 --> 1484.04]  evaluating different language, you'll have to do that.
[1484.04 --> 1488.34]  Now, you know, if you're using a metric from Ragas, Ragas could take care of that.
[1488.82 --> 1494.12]  Then there are also issues, like if you are building an LLM based metrics, which is the trend
[1494.12 --> 1498.28]  here and most of the Ragas metrics are LLM based metrics because that has high correlation
[1498.28 --> 1499.06]  with human judgment.
[1499.06 --> 1507.56]  Then, okay, let's say the LLM, you know, you are evaluating with LLM based metrics and you
[1507.56 --> 1511.82]  are finding that the LLM based metrics is actually performing.
[1512.18 --> 1514.84]  It's actually not performing very much in your case.
[1515.22 --> 1519.64]  You should have a way to allay in these LLM, you know, people will have different expectations
[1519.64 --> 1521.58]  for different metrics.
[1521.78 --> 1526.52]  For example, let's say you are trying to do something like faithfulness and faithfulness
[1526.52 --> 1534.02]  is basically the amount of hallucination or that is happening in the answer given a contact.
[1534.54 --> 1539.04]  And if you look at a different developer, some different domain has different strictness
[1539.04 --> 1540.02]  towards hallucination.
[1540.34 --> 1546.12]  I could have a statement like I have a blue car and versus I have a car and I could, for
[1546.12 --> 1549.98]  me, maybe in my domain, I could say that these are two equal statements.
[1550.28 --> 1554.56]  But for someone who is working in FinTech or something, it might not be equal statements.
[1554.56 --> 1560.94]  So there is also a domain kind of bias when it comes to metrics or in rejectments because
[1560.94 --> 1564.76]  developers from the different domain expects different level of strictness and everything.
[1565.00 --> 1570.86]  So bringing out this alignment with these metrics is depending upon your domain is also
[1570.86 --> 1574.86]  one extra thing that we are trying to tackle here, which is called, basically we call it
[1574.86 --> 1581.46]  as a metric alignment that is trying to align larger language model judges to your, you know,
[1581.46 --> 1585.40]  your specific measurements using the feedbacks that you can give to elements.
[1585.72 --> 1587.30]  It is also an upcoming feature regardless.
[1588.02 --> 1590.36]  I want to just dig into a couple of those things.
[1590.46 --> 1596.38]  So one is like you talk about alignment, but also there's like the idea of it's very important
[1596.38 --> 1602.16]  in this case for me to be thinking about data and examples from my domain in terms of how
[1602.16 --> 1603.42]  I'm evaluating these.
[1603.42 --> 1608.46]  So I'm just looking through, you know, just to make things for concrete for people looking
[1608.46 --> 1611.28]  at your example around answer relevance.
[1611.94 --> 1618.08]  And there's data samples in there that have a question, an answer, and then a set of context.
[1618.08 --> 1624.26]  And then you can evaluate with Ragas using the metric answer relevancy.
[1624.46 --> 1627.10]  So obviously there's a data component there.
[1627.10 --> 1633.16]  And in that component, there's, you know, answers that are there and contexts that are there.
[1633.60 --> 1641.16]  So one question would be like how much and what type of data will people need to configure
[1641.16 --> 1646.84]  such that they can appropriately evaluate their LLM applications?
[1647.24 --> 1653.36]  And are there metrics that require sort of data upfront or metrics that maybe are reference
[1653.36 --> 1655.78]  free that wouldn't require data upfront?
[1655.78 --> 1659.66]  What's the perspective there in terms of kind of, I guess, the cold start?
[1659.82 --> 1664.42]  Like if people are starting an LLM application from scratch, they haven't run it in production.
[1664.76 --> 1669.56]  What's the data burden and the path towards both getting this data in place and getting
[1669.56 --> 1670.76]  the alignment in place?
[1671.32 --> 1677.54]  So regarding the data itself, the number of samples people generally used to evaluate is
[1677.54 --> 1681.50]  around 100 to 500 when it comes to off-line evaluation.
[1681.50 --> 1685.38]  So it really depends on how you formulated your test data itself.
[1685.38 --> 1691.42]  So for example, you could have the same results or same kind of dragging when you have 100
[1691.42 --> 1692.96]  samples at a point.
[1693.16 --> 1699.26]  Or in many use cases, even 100 may not be enough to include all the kind of use cases or all
[1699.26 --> 1701.22]  the kind of distributions that you see in production.
[1701.22 --> 1707.16]  So it really depends on the variety of items that you see in production, you know, that you expect in production.
[1707.16 --> 1713.94]  So if you're using a very niche application, then let's say you have a very niche use case and variety is very skewed.
[1713.94 --> 1717.80]  Your test data can be very small, yet still serve the purpose.
[1717.80 --> 1733.16]  But if your use case is very broad and you see a wide variety of users coming into your application or a wide variety of requests, your test data has to be broad enough to include all the different distributions in the data set itself.
[1733.16 --> 1737.16]  So that's about the number.
[1737.16 --> 1747.00]  And it's not really about the concrete number, but again, basically making sure that you understand what are the different distributions of queries coming into your system.
[1747.00 --> 1757.00]  And also making sure these distribution of queries are also represented in the test data set so that you know when you change a probe or when you change a probe, which type of queries are being affected.
[1757.00 --> 1767.00]  You know, it could be that when you change a particular tool or something, when you start out a particular tool or something, it could be that a specific set of queries are being affected.
[1767.00 --> 1773.00]  So overall pipeline almost never gets affected if you want to do a huge change.
[1773.00 --> 1779.00]  And therefore the small changes, it's mostly a subset of queries, a subset of distribution that gets affected.
[1779.00 --> 1782.00]  And it is very important that you identify these items.
[1782.00 --> 1789.00]  So that's about the, you know, how to form data set itself for evaluating applications.
[1789.00 --> 1799.00]  And regarding the second question of metrics and reference fee and the reference metrics, you should provide both reference fee and reference with reference metrics.
[1799.00 --> 1812.00]  But there is a big shortcoming to reference free metrics itself because reference free metrics are basically, you know, you know, we could estimate things there, but there is an error estimation with reference free metrics.
[1812.00 --> 1826.00]  For example, answer 11c or, you know, you could estimate with some way that if the given answer was correct or something, but if you don't really have the exact thing, some way not enough, it's really possible to say that,
[1826.00 --> 1830.00]  Okay, the LLM application arrived at the right thing at the end of the day.
[1830.00 --> 1839.00]  So there what we provide, even with production data, it's very hard to occur in a test data set because again, with production data, data is very, very, very messy.
[1839.00 --> 1851.00]  It's a common thing that people, people, if you ask any, you know, researcher or a guy who has put MLS into production, MLS into production and the method of occurring test data set,
[1851.00 --> 1865.00]  obviously they are going to look at production data, but the way in which test data set are being accurate is there is a long way to go from production data to formulating it as a test data because production data is incredibly messy because it's an uncontrolled environment.
[1865.00 --> 1873.00]  It's not a human-controlled environment. People can come and say anything there and they don't, they have like zero consequences.
[1873.00 --> 1879.00]  So the thing is that production data becomes incredibly messy depending upon the application.
[1879.00 --> 1887.00]  If you have, let's say, if your application is serving an internal set of users, like an internal company, employees or something, still you have an amount of control there.
[1887.00 --> 1901.00]  But if your application is strictly B2C and you are opening up the whole application to, you know, anyone using your application, there can be users who are basically trolls who just like to use your system and, you know, leave out, you know, code, speed, and stuff.
[1901.00 --> 1911.00]  So production data being incredibly messy, there is a long way from going from production data to, you know, to a good test data set.
[1911.00 --> 1917.00]  So there again, what we are trying to do is providing a way to synthetically create these tests, test data sets.
[1917.00 --> 1923.00]  Now, these synthetic creation of test data sets will be grounded on things like production data.
[1923.00 --> 1929.00]  Then there are your internal documents that should be, you know, taken into account when creating a synthetic test data set.
[1929.00 --> 1934.00]  Because again, you are trying to create a test data set that's very tailored to use case and not a generic one.
[1934.00 --> 1942.00]  So there are two points where we ground it, basically the set of internal documents or whatever you have that you ground your application.
[1942.00 --> 1946.00]  And also the production data where the user engages with your application.
[1946.00 --> 1953.00]  And when we, when this is again, one of the upcoming features, the test data set generation is already there.
[1953.00 --> 1960.00]  But we are also trying to extend it to a way that we could ground these into the from production data.
[1960.00 --> 1976.00]  Basically, we call it seeding from production data. Basically, if a user has been already using our last test generation, but he wants to take motivations from production to imitate more, more behavior in the test data set that is also happening in production.
[1976.00 --> 1984.00]  Now, there is a lot of things that has to be done to make sure that to first understand what is happening in production.
[1984.00 --> 1993.00]  You know, there can be different distributions, again, as I said, different set of users, we have to understand different set of queries that's coming in different set of interactions that's happening and everything.
[1993.00 --> 2000.00]  And once then we understand that we could also have a way to synthesize these types of data points using LL and Intel.
[2000.00 --> 2007.00]  Now, the developers will not be to annotate these data points, but to verify these data points.
[2007.00 --> 2019.00]  Once this data or test data is synthesized by Ravas, you could export it to a simple UI tool, and then you could simply go or even Excel sheet.
[2019.00 --> 2025.00]  Most of the users could export this data to an Excel sheet and basically they go through it.
[2025.00 --> 2032.00]  And then once they go through it, they can easily, you know, cut out the bad data points that they think is LL messed up or something.
[2032.00 --> 2037.00]  Because again, we don't really, we can't really guarantee 100% efficiency while we synthesizing these data points.
[2037.00 --> 2039.00]  So what we are trying to do is improve the efficiency.
[2039.00 --> 2046.00]  Let's say if you generate 100 data points, our goal is to make sure that all the 100 data points are equally valid and good.
[2046.00 --> 2049.00]  But it might not happen like that in every use case.
[2049.00 --> 2054.00]  So the developer can take 10 minutes of his time and go through this data set manually.
[2054.00 --> 2060.00]  It is a fairly quicker process than annotating these, annotating or creating these data sets.
[2060.00 --> 2068.00]  Because creating these data sets would easily take a day or two or even a lot of money when you give it to other human annotators.
[2068.00 --> 2075.00]  So the developer basically can go through this data points that's been synthesized and then cut out the points that he thinks that is not valuable.
[2075.00 --> 2082.00]  So again, that is again one, one, this, these are actually the real reason which we save a lot of developer time in evaluation.
[2082.00 --> 2088.00]  Because again, formally, the data set is very, very, it's a very, you know, a cucumber stone.
[2088.00 --> 2091.00]  It's a very time consuming boring process that nobody wants to.
[2091.00 --> 2094.00]  And it's mostly falls upon one developer and the team to do it.
[2094.00 --> 2096.00]  And it's a messy process.
[2096.00 --> 2103.00]  So these are the type of innovations what we are trying to bring in the evaluation space itself to save a lot of time of the developer.
[2103.00 --> 2108.00]  And this ideology or this philosophy is why, why we are being getting this organic growth.
[2108.00 --> 2113.00]  Because we, it is really kind of hard to come up with these kinds of solutions.
[2113.00 --> 2121.00]  But when we come up with these kinds of solutions, there are, you know, a lot of developers who are, you know, who wants, who badly wants this.
[2121.00 --> 2130.00]  And they are, you know, they are the people who motivate us to continually bring these kinds of innovations to the evaluation space.
[2130.00 --> 2131.00]  Yeah, that's great.
[2131.00 --> 2144.00]  I love, I love the innovations around synthetic data use and evaluation and utilizing kind of the, the LLMs and these models to help in the evaluation process.
[2144.00 --> 2150.00]  But in a way that's, that's validated and still, still fitting with improvement over time.
[2150.00 --> 2151.00]  So, yeah.
[2151.00 --> 2155.00]  As we kind of close out here, this has been a fascinating discussion.
[2155.00 --> 2170.00]  But maybe just to close out here, what, what are some of the things that you're excited about moving into the next, next six months or so to either explore or maybe it's things that you see happening in the AI ecosystem more broadly?
[2170.00 --> 2176.00]  What, what really excites you about the direction that people are going with their LLM applications?
[2176.00 --> 2183.00]  So with LLM applications, with early 2023 or, you know, mid 2023, RAG was a big thing.
[2183.00 --> 2189.00]  And if you remember the time when RAG became popular, there was again, a lot of limitations.
[2189.00 --> 2194.00]  There were only 4K contacts or, you know, LLM was kind of the same thing and everything.
[2194.00 --> 2199.00]  I think with HND Code tool use cases, we are at the same level as of now, you know, we have a lot of limitations.
[2199.00 --> 2205.00]  You know, we have been trying to bring more and more, you know, tool use cases.
[2205.00 --> 2217.00]  Tool use cases are actually incredibly useful when, when it comes to building a whole LLM application experience because combined with internal knowledge, internal knowledge is what you can infuse with RAG.
[2217.00 --> 2223.00]  And then taking actions can you, is something that infuse with, you know, tool use cases, tool bindings.
[2223.00 --> 2231.00]  So if, you know, tool binding, I'm very excited to see, you know, the next class of models, performing better on tool use cases.
[2231.00 --> 2244.00]  Again, now, even the, these recent models have, I've been bringing abstractions or, you know, being, using tool binding to facilitate this, but still it's a little bit shaky as of now.
[2244.00 --> 2247.00]  But the next class of models, I really expect it to be better.
[2247.00 --> 2259.00]  And then the whole thing, the RAG plus tool use case, we don't see no more enterprises adopting, you know, adopting and using and other applications at, you know, at different capacities.
[2259.00 --> 2268.00]  And it's saving a lot of, you know, time and resources for both, you know, people who are at the back of these application,
[2268.00 --> 2270.00]  and also people who are interacting with these applications.
[2270.00 --> 2276.00]  So that's something I'm really excited when it comes to, you know, the very next six months of catalog applications itself.
[2276.00 --> 2282.00]  And also, I think when it comes to the frameworks or libraries that are being built around applications,
[2282.00 --> 2289.00]  I'm seeing more and more better abstractions these days, when it comes to, you know, these frameworks and libraries,
[2289.00 --> 2294.00]  because people now have almost one and a half year of, you know, building with another application experience.
[2294.00 --> 2303.00]  Now that experience is yielding more and more, you know, understanding of what kind of, what is the best abstraction to be used to build these applications and everything.
[2303.00 --> 2311.00]  And then there is an overall agreement that is coming up with, you know, what is the, you know, how to format outputs,
[2311.00 --> 2313.00]  how to, you know, build these combo systems itself.
[2313.00 --> 2320.00]  Because earlier, the first year, early 2023 and everything, people were really, really confused on how to build these applications,
[2320.00 --> 2321.00]  how to use it and everything.
[2321.00 --> 2326.00]  Now that clarity, I can see that, you know, more clarity is happening at that end too.
[2326.00 --> 2331.00]  So at the more, at the model building stage, again, the model building spectrum,
[2331.00 --> 2336.00]  they are again having more clarity on, you know, things like, you know, the bigger of the models,
[2336.00 --> 2341.00]  the type of data needed, more and more, you know, papers and more and more research happening at the, you know,
[2341.00 --> 2348.00]  data processing and pre-processing stage, you know, what is the type of data needed to train the higher quality and best quality
[2348.00 --> 2349.00]  and all that.
[2349.00 --> 2355.00]  So we see, we think that we have mostly settled on the architecture itself from that point of LLM.
[2355.00 --> 2360.00]  Now the main thing people are, you know, working on this data, again, when it comes to data, people are again,
[2360.00 --> 2366.00]  now mostly, we will finish up the free data that's available on the internet very quickly.
[2366.00 --> 2371.00]  And now, it's again, synthetic data that has a really good chance of improving these models itself.
[2371.00 --> 2378.00]  So the idea of models output being used to feed models and improving the models itself on different use cases
[2378.00 --> 2382.00]  is itself a fascinating thing regarding the model building stage.
[2382.00 --> 2389.00]  When it comes to evaluation, there needs to be more and more innovations happening in that evaluation space itself,
[2389.00 --> 2398.00]  whether as an open research or as an open approach to, you know, bringing around the time involved in testing and assessing these applications itself.
[2398.00 --> 2414.00]  Because that's one big pain point on why the enterprises or, you know, big companies could, a big barrier for these big companies to adopt LLM applications, LLMs for AAs in their system.
[2414.00 --> 2423.00]  Because these people, they have high responsibilities. So when, with high responsibility, you have to do these testing and evaluations.
[2423.00 --> 2429.00]  And there is no very good way of doing it and agreed upon way of doing it, it becomes a pain point.
[2429.00 --> 2437.00]  And that's something we are also trying to bring in, you know, we are trying to, you know, formulate all that research, all the innovations that are happening in the evaluation space,
[2437.00 --> 2441.00]  to come together and build an open source standard for evaluating LLM applications itself.
[2441.00 --> 2446.00]  So there is an agreement between everyone on how to evaluate LLM applications.
[2446.00 --> 2449.00]  And that's the long term vision of the company itself.
[2449.00 --> 2456.00]  Awesome. Yeah, well, thank you, Shahul, for taking time to join and again joining at a late hour where you're at.
[2456.00 --> 2463.00]  I'm really excited about what you're doing with Ragas. And this is a really interesting space that we'll be interested to follow.
[2463.00 --> 2468.00]  So thanks for taking time and hope you can have a good rest of your week.
[2468.00 --> 2476.00]  Sure. Thanks, Shahul. This was fun chatting with you and I hope your users learned something from this conversation.
[2476.00 --> 2477.00]  Yeah, thanks. Bye bye.
[2477.00 --> 2478.00]  Thanks. Bye bye.
[2478.00 --> 2496.00]  All right, that is Practical AI for this week. Subscribe now. If you haven't already, head to practicalai.fm for all the ways.
[2496.00 --> 2502.00]  And join our free Slack team where you can hang out with Daniel, Chris and the entire ChangeLog community.
[2502.00 --> 2507.00]  Sign up today at practicalai.fm slash community.
[2507.00 --> 2515.00]  Thanks again to our partners at fly.io, to our beat freaking residents, Breakmaster Cylinder, and to you for listening.
[2515.00 --> 2517.00]  We appreciate you spending time with us.
[2517.00 --> 2520.00]  That's all for now. We'll talk to you again next time.
[2520.00 --> 2530.00]  Bye bye.
