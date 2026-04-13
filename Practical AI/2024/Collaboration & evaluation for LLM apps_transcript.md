[0.00 --> 8.66]  Welcome to Practical AI.
[9.34 --> 16.78]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is
[16.78 --> 19.54]  changing the world, this is the show for you.
[20.24 --> 24.92]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 --> 30.94]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions
[30.94 --> 35.44]  on six continents, so you can launch your app near your users.
[35.84 --> 37.84]  Learn more at Fly.io.
[42.56 --> 45.66]  Welcome to another episode of Practical AI.
[46.00 --> 47.46]  This is Daniel Whitenak.
[47.46 --> 54.50]  I am CEO and founder at Prediction Guard, and really excited today to be joined by Dr.
[54.50 --> 58.76]  Reza Habib, who is CEO and co-founder at Humanloop.
[58.98 --> 59.84]  How are you doing, Reza?
[60.22 --> 60.74]  Hi, Daniel.
[60.88 --> 61.86]  It's a pleasure to be here.
[61.92 --> 62.50]  I'm doing very well.
[63.42 --> 64.32]  Yeah, thanks for having me on.
[64.74 --> 65.34]  Yeah, yeah.
[65.40 --> 67.98]  It's super excited to talk with you.
[68.36 --> 74.92]  I'm mainly excited to talk with you selfishly because I see the amazing things that Humanloop
[74.92 --> 79.12]  is doing and the really critical problems that you're thinking about.
[79.12 --> 83.06]  And every day of my life, it's like, how am I managing prompts?
[83.38 --> 90.10]  And how does this next model that I'm upgrading to, how do my prompts do in that model?
[90.28 --> 94.06]  And how am I constructing workflows around using LLMs?
[94.26 --> 100.18]  Which it definitely seems to be the main thrust of some of the things that you're thinking about
[100.18 --> 100.90]  at Humanloop.
[100.90 --> 106.12]  Before we get into the specifics of those things at Humanloop, would you mind setting
[106.12 --> 112.42]  the context for us in terms of workflows around these LLMs, collaboration on team?
[112.58 --> 114.78]  How did you start thinking about this problem?
[115.40 --> 122.26]  And what does that mean in reality for those working in industry right now, maybe more generally
[122.26 --> 123.24]  than at Humanloop?
[123.54 --> 124.08]  Yeah, absolutely.
[124.24 --> 128.20]  So I guess on the question of how I came to be working on this problem, it was really
[128.20 --> 132.04]  something that my co-founders, Peter and Jordan, I had been working on for a very long time,
[132.10 --> 132.34]  actually.
[132.56 --> 136.34]  So previously, Peter and I did PhDs together around this area.
[136.66 --> 140.70]  And then when we started the company, it was a little while after Transfer Learning had started
[140.70 --> 142.16]  to work in NLP for the first time.
[142.52 --> 145.14]  And we were mostly helping companies fine-tune smaller models.
[145.72 --> 152.38]  But then sometime midway through 2022, we became absolutely convinced that the rate of progress
[152.38 --> 156.48]  for these larger models was so high, it was going to start to eclipse essentially everything
[156.48 --> 160.58]  else in terms of performance, but more importantly, in terms of usability, right?
[160.62 --> 165.30]  It was the first time that instead of having to hand-annotate a new data set for every new
[165.30 --> 169.80]  problem, there was this new way of customizing AI models, which was that you could write instructions
[169.80 --> 174.60]  in natural language and have a reasonable expectation that the model would then do that thing.
[174.76 --> 179.88]  And that was unthinkable at the start of 2022, I would say, or maybe a little bit earlier.
[179.88 --> 184.98]  And so that's really what made us want to go work on this because we realized that the
[184.98 --> 190.32]  potential impact of NLP was already there, but the accessibility had been expanded so far
[190.32 --> 194.88]  and the capabilities of the models had increased so much that there was a particular moment to
[194.88 --> 195.56]  go do this.
[195.92 --> 199.00]  But at the same time, it introduces a whole bunch of new challenges, right?
[199.06 --> 203.26]  So I guess historically, the people who were building AI systems were machine learning experts.
[203.66 --> 207.44]  The way that you would do it is you would collect annotated data, you'd fine-tune a custom
[207.44 --> 211.68]  model, it was typically being used for like one specific task at a time.
[212.00 --> 214.32]  There was a correct answer, so it was easy to evaluate.
[214.96 --> 218.48]  And with LLMs, the power also brings new challenges.
[219.06 --> 222.48]  So the way that you customize these models is by writing these natural language instructions,
[222.66 --> 223.38]  which are prompts.
[223.94 --> 227.92]  And typically that means that the people involved don't need to be as technical.
[228.22 --> 232.54]  And usually we see actually that the best people to do prompt engineering tend to have
[232.54 --> 233.24]  domain expertise.
[233.24 --> 237.74]  So often it's a product manager or someone else within a company who's leading the prompt
[237.74 --> 242.58]  engineering efforts, but you also have this new artifact lying around, which is the prompt,
[242.80 --> 245.78]  and it has a similar impact to code on your end application.
[246.14 --> 250.36]  So it needs to be versioned and managed and treated with the same level of respect and rigor
[250.36 --> 251.60]  that you would treat normal code.
[251.96 --> 256.62]  But somehow you also need to have the right workflows and collaboration that lets the non-technical
[256.62 --> 260.80]  people work with the engineers on the product or the less technical people.
[260.80 --> 265.64]  And then the extra challenge that comes with it as well is that it's very subjective to
[265.64 --> 266.80]  measure performance here.
[266.90 --> 271.34]  So in traditional code, we're used to running unit tests, integration tests, regression tests.
[271.70 --> 274.26]  We know what good looks like and how to measure it.
[274.34 --> 279.04]  And even in traditional machine learning, there's a ground truth data set.
[279.16 --> 280.42]  People calculate metrics.
[280.64 --> 285.92]  But once you go into generative AI, it tends to be harder to say what is the correct answer.
[286.32 --> 289.78]  And so when that becomes difficult, then measuring performance becomes hard.
[289.78 --> 293.46]  If measuring performance is hard, how do you know when you make changes if you're going
[293.46 --> 294.36]  to cause regressions?
[294.56 --> 299.10]  Or all the different design choices you have in developing an app, how do you make those
[299.10 --> 301.80]  design choices if you don't have good metrics of performance?
[302.38 --> 305.64]  And so those are the problems that motivated what we've built.
[306.22 --> 308.64]  And really, Humanloop exists to solve both of these problems.
[308.64 --> 313.54]  So to help companies with the tasks of finding the best prompts, managing, versioning them,
[313.90 --> 317.94]  dealing with collaboration, but then also helping you do the evaluation that's needed
[317.94 --> 321.94]  to have confidence that the models are going to behave as you expect in production.
[322.68 --> 329.08]  And as related to these things, maybe you can start with one that you would like to start
[329.08 --> 330.22]  with and go to the others.
[330.42 --> 336.40]  But in terms of managing versioning prompts, evaluating the performance of these models,
[336.54 --> 341.80]  dealing with regressions, as you've kind of seen people try to do this across probably
[341.80 --> 345.36]  a lot of different clients, a lot of different industries.
[346.10 --> 352.30]  How are people trying to manage this in maybe some good ways and some bad ways?
[352.64 --> 355.48]  Yeah, I think we see a lot of companies go on a bit of a journey.
[356.02 --> 360.16]  So early on, people are excited about generative AI and LLM.
[360.26 --> 361.38]  There's a lot of hype around it now.
[361.50 --> 363.60]  So some people in the company just go try things out.
[364.06 --> 368.18]  And often they'll start off using one of the large publicly available models.
[368.18 --> 373.12]  So OpenAI or Anthropic, or here, one of these, they'll prototype in their own kind of playground
[373.12 --> 374.86]  environment that those providers have.
[374.98 --> 376.36]  They'll eyeball a few examples.
[376.66 --> 380.82]  Maybe they'll grab a couple of libraries that support orchestration and they'll put together
[380.82 --> 381.32]  a prototype.
[382.04 --> 384.54]  And the first version is fairly easy to build.
[384.82 --> 388.06]  It's very quick to get to like the first wow moment.
[388.58 --> 393.42]  And then as people start moving towards production and they start iterating from that, you know,
[393.48 --> 396.82]  maybe 80% good enough version to something that they really trust,
[396.82 --> 400.58]  they start to run into these problems of like, oh, I've got like 20 different versions of
[400.58 --> 402.94]  this prompt and I'm storing it as a string in code.
[403.48 --> 406.10]  And actually, I want to be able to collaborate with a colleague on this.
[406.24 --> 410.46]  And so now we're sharing things, you know, either via screen sharing or we're like both,
[410.58 --> 413.70]  you know, we've had some serious companies you would have heard of who are sending their
[413.70 --> 416.28]  model configs to each other via Microsoft Teams.
[416.62 --> 421.64]  And obviously, you know, you wouldn't send someone an important piece of code through Slack
[421.64 --> 422.92]  or Teams or something like this.
[422.92 --> 426.86]  But because the collaboration software isn't there to bridge this technical, non-technical
[426.86 --> 428.94]  divide, those are the kind of problems we see.
[429.50 --> 433.72]  And so at this point, typically a year ago, people would start building their own solution.
[434.18 --> 437.38]  So more often than not, like this was when people would start building in-house tools.
[438.06 --> 441.90]  Increasingly, because there are companies like Humanloop around, that's usually when someone
[441.90 --> 446.44]  books a demo with us and they say, hey, you know, we've reached this point where actually
[446.44 --> 448.78]  managing these artifacts has become cumbersome.
[448.78 --> 451.58]  We're worried about the quality of what we're producing.
[452.02 --> 453.40]  Do you have a solution to help?
[453.86 --> 457.62]  And the way that Humanloop helps, at least on the prompt management side, is we have this
[457.62 --> 458.50]  interactive environment.
[458.50 --> 463.16]  It's a little bit like those OpenAI playgrounds or the Anthropic playground, but a lot more
[463.16 --> 465.26]  fully featured and designed for actual development.
[465.46 --> 466.78]  So it's collaborative.
[467.16 --> 468.32]  It has history built in.
[468.46 --> 470.54]  You can connect variables and data sets.
[470.92 --> 474.94]  And so it becomes like a development environment for your sort of LLM application.
[474.94 --> 479.62]  You can prototype the application, interact with it, try out a few things, and then people
[479.62 --> 485.28]  progress from that development environment into production through evaluation and monitoring.
[485.96 --> 488.06]  You mentioned this kind of in passing.
[488.18 --> 490.02]  I'd love to dig into it a little bit more.
[490.14 --> 495.74]  You mentioned kind of the types of people that are coming, you know, at the table in designing
[495.74 --> 496.46]  these systems.
[496.46 --> 503.04]  And oftentimes domain experts, you know, previously in working as a data scientist, it was always
[503.04 --> 505.90]  kind of assumed, oh, you need to talk to the domain experts.
[506.10 --> 511.08]  But it's sort of like, at least for many years, it was like data scientists talk to the domain
[511.08 --> 513.24]  experts and then go off and build their thing.
[513.68 --> 518.02]  The domain experts were not involved in the sort of building of the system.
[518.70 --> 524.58]  And even then, like the data scientists were maybe building things that were kind of foreign
[524.58 --> 526.52]  to software engineers.
[527.04 --> 530.66]  And what I'm hearing you say is you kind of got like these multiple layers.
[530.66 --> 534.32]  You have like domain experts who might not be that technical.
[534.98 --> 540.60]  You've got maybe AI and data people who are using this kind of unique set of tools.
[541.14 --> 542.60]  Maybe even they're hosting their own models.
[543.12 --> 546.26]  And then you've got like product software engineering people.
[546.44 --> 550.68]  It seems like a much more complicated landscape of interactions.
[551.28 --> 556.88]  How have you seen this kind of play out in reality in terms of non-technical people and
[556.88 --> 563.28]  technical people both working together on something that is ultimately something implemented in
[563.28 --> 564.92]  code and run as an application?
[565.72 --> 570.68]  I actually think one of the most exciting things about LLMs and the progress in AI in general
[570.68 --> 576.22]  is that product managers and subject matter experts can, for the first time, be very directly
[576.22 --> 578.48]  involved in implementing these applications.
[579.14 --> 583.46]  So I think it's always been the case that the PM or someone like that, you know, is the person
[583.46 --> 586.58]  who distills the problem, speaks to the customers, produces the spec.
[586.68 --> 591.20]  But there's this translation step where they sort of produce that PRD document and then
[591.20 --> 592.90]  someone else goes off and implements it.
[593.46 --> 598.02]  And because we're now able to program at least some of the application in natural language,
[598.44 --> 600.84]  actually it's accessible to those people very directly.
[601.42 --> 602.92]  And it's worth maybe having a concrete example.
[603.08 --> 608.44]  So like I use an AI note taker for a lot of my sales calls and it records the call and
[608.44 --> 609.56]  then I get a summary afterwards.
[610.20 --> 613.22]  And the app actually allows you to choose a lot of different types of summaries.
[613.22 --> 615.30]  So you can say, hey, I'm a salesperson.
[615.30 --> 620.46]  I want a summary that will extract budget and authority and need and timeline versus
[620.46 --> 624.10]  you can say, oh, actually, I had a product interview and I want a different type of summary.
[624.58 --> 629.44]  And if you think about developing that application, the person who has the knowledge that's needed
[629.44 --> 634.22]  to say what a good summary is and to write the prompt for the model is the person who has
[634.22 --> 634.98]  that domain expertise.
[635.12 --> 636.18]  It's not the software engineer.
[636.70 --> 640.62]  But obviously the prompt is only one piece of the application, right?
[640.62 --> 644.80]  If you've got a question answering system, there's usually retrieval as part of this.
[644.90 --> 646.00]  There may be other components.
[646.70 --> 649.46]  Usually the LLM is a block in a wider application.
[649.64 --> 653.56]  So you obviously still need the software engineers around because they're implementing the bulk
[653.56 --> 654.32]  of the application.
[654.32 --> 657.70]  But the product managers can be much more directly involved.
[658.28 --> 663.60]  And then, you know, actually we see increasingly less involvement from machine learning or AI
[663.60 --> 666.66]  experts and less people are fine tuning their own models.
[666.66 --> 673.10]  So for the majority of product teams we're seeing, there is an AI platform team that maybe facilitates
[673.10 --> 674.14]  setting things up.
[674.28 --> 678.78]  But the bulk of the work is led by the product managers and then the engineers.
[679.36 --> 683.60]  And one interesting example of this on the extreme end is one of our customers that's a
[683.60 --> 684.74]  very large ed tech company.
[685.20 --> 687.68]  They actually do not let their engineers edit the prompts.
[688.00 --> 690.54]  So they have a team of linguists who do prompt development.
[691.08 --> 693.08]  The linguists finalize the prompts.
[693.08 --> 697.68]  They're saved in a serialized format and they go to production, but it's a one-way transfer.
[698.28 --> 704.08]  So the engineers can't edit them because they're not considered able to assess the actual outputs,
[704.30 --> 706.76]  even though they are responsible for the rest of the application.
[707.52 --> 713.48]  Just thinking about how teams interact and who's doing what, it seems like the problems that
[713.48 --> 716.54]  you've laid out are, I think, very clear and worth solving.
[716.72 --> 723.06]  But it's probably hard to think about, well, am I building a developer tool or am I building
[723.06 --> 726.14]  something that these non-technical people interact with?
[726.24 --> 726.96]  Or is it both?
[727.34 --> 732.64]  How did you think about that as you kind of entered into the stages of bringing human loop
[732.64 --> 733.76]  into existence?
[734.28 --> 735.86]  I think it has to be both.
[736.48 --> 741.22]  And the honest answer is it evolved kind of organically by going to customers, speaking
[741.22 --> 744.56]  to them about their problems and trying to figure out what the best version of a solution
[744.56 --> 745.12]  looked like.
[745.18 --> 748.98]  So we didn't set out to build a tool that needed to do both of these things.
[748.98 --> 753.66]  But I think the reality is, given the problems that people face, you do need both.
[754.22 --> 757.28]  And an analogy to think about might be something like Figma, right?
[757.46 --> 762.60]  Like Figma is somewhere where multiple different stakeholders come together to iterate on things
[762.60 --> 764.14]  and to develop them and provide feedback.
[764.40 --> 769.32]  And I think you need something analogous to that for Gen AI, although it's not an exact analogy
[769.32 --> 771.52]  because we also need to attach the evaluation to this.
[771.98 --> 774.56]  So it's almost by necessity that we've had to do that.
[774.56 --> 778.02]  But I also think that it's very exciting, right?
[778.16 --> 782.80]  And the reason I think it's exciting is because it is expanding who can be involved in developing
[782.80 --> 783.48]  these applications.
[783.48 --> 806.04]  If you're listening, you know software is built from thousands of small technical choices.
[806.04 --> 813.22]  And some of these seemingly inconsequential choices can have a profound impact on the economics of internet services.
[813.48 --> 816.92]  Who gets to participate in them, build them, and profit from them?
[817.26 --> 821.78]  This is especially true for artificial intelligence, where the decisions we make today
[821.78 --> 826.56]  can determine who can have access to world-changing technologies and who can decide their future.
[827.08 --> 833.06]  Read, Write, Own, Building the Next Era of the Internet is a new book from startup investor Chris Dixon
[833.06 --> 837.08]  that explores the decisions that took us from open networks governed by communities
[837.08 --> 839.82]  to massive social networks run by internet giants.
[839.82 --> 846.06]  This book, Read, Write, Own, is a call to action for building a new era of the internet
[846.06 --> 848.22]  that puts people in charge.
[848.36 --> 854.16]  From AI projects that compensate creators for their work to protocols that fund open source contributions,
[854.72 --> 858.92]  this is our chance to build the internet we want, not the one we inherited.
[859.52 --> 865.74]  Order a copy of Read, Write, Own today, or go to readwriteown.com to learn more.
[865.74 --> 886.80]  You mentioned how this environment of domain experts coming together and technical teams coming together
[886.80 --> 894.02]  in a collaborative environment opens up new possibilities for both collaboration and innovation.
[894.02 --> 898.94]  I'm wondering if at this point you could kind of just lay out, we've talked about the problems,
[899.06 --> 904.52]  we've talked about those involved and those kind of that would use such a system or a platform
[904.52 --> 906.70]  to enable these kind of workflows.
[907.08 --> 915.26]  Could you describe a little bit more what HumanLoop is specifically in terms of both what it can do
[915.26 --> 919.40]  and kind of how these different personas engage with the system?
[919.40 --> 925.96]  Yeah. So I guess in terms of what it can do, concretely, it's firstly helping you with prompt iteration,
[926.40 --> 929.84]  versioning, and management, and then with evaluation and monitoring.
[930.04 --> 934.74]  And the way it does that is there's a web app and there's a web UI where people are coming in.
[934.82 --> 940.96]  And in that UI is an interactive playground-like environment where people basically try out different prompts.
[941.20 --> 943.40]  They can compare them side by side with different models.
[943.40 --> 948.60]  They can try them with different inputs. When they find versions that they think are good, they save them.
[949.26 --> 954.90]  And then those can be deployed from that environment to production or even to a development or staging environment.
[955.34 --> 957.36]  So that's the kind of development stage.
[957.84 --> 963.82]  And then once you have something that's developed, what's very typical is people then want to put in evaluation steps into place.
[963.82 --> 969.14]  So you can define gold standard test sets, and then you can define evaluators within HumanLoop.
[969.34 --> 977.48]  And evaluators are ways of scoring the outputs of a model or a sequence of models, because oftentimes the LLM is part of a wider application.
[978.16 --> 984.52]  And so the way that scoring works is there's very traditional metrics that you would have in code for any machine learning system.
[984.52 --> 991.20]  So precision, recall, rouge, blue, these kind of scores that anyone from a machine learning background would already be familiar with.
[991.50 --> 996.32]  But what's new in the kind of LLM space is also things that help when things are more subjective.
[996.60 --> 1003.40]  So we have the ability to do model as judge, where you might actually prompt another LLM to score the output in some way.
[1003.78 --> 1007.90]  And this can be particularly useful when you're trying to measure things like hallucination, right?
[1007.90 --> 1014.58]  So a very common thing to do is to ask the model, you know, is the final answer contained within the retrieved context?
[1014.90 --> 1018.90]  Or is it possible to infer the answer from the retrieved context?
[1018.90 --> 1020.38]  And you can calculate those scores.
[1021.00 --> 1023.38]  And then the final way is we also support human evaluation.
[1023.92 --> 1030.90]  So in some cases, you know, you really do want either feedback from an end user or from an internal annotator involved as well.
[1030.90 --> 1041.80]  And so we allow you to gather that feedback either from your live production application and have it, you know, logged against your data, or you can cue internal annotation tasks from a team.
[1042.20 --> 1047.44]  And I can maybe tell you a little bit more about sort of in production feedback, because that's something that that's actually where we started.
[1047.82 --> 1049.48]  Yeah, yeah, go ahead. I would love to hear more.
[1049.48 --> 1061.90]  Yeah, so I think that because it's so subjective for a lot of the applications that people are building, whether it be email generation, question answering, a language learning app, there isn't a correct answer, quote unquote.
[1062.54 --> 1066.54]  And so people want to measure how things are actually performing with their end users.
[1067.14 --> 1071.18]  And so HumanLoop makes it very easy to capture different sources of end user feedback.
[1071.18 --> 1079.32]  And that might be explicit feedback, things like thumbs up, thumbs down votes that you see in ChatGPT, but it can also be more implicit signals.
[1079.66 --> 1083.88]  So how did the user behave after they were shown some generated content?
[1084.02 --> 1086.32]  Did they progress to the next stage of the application?
[1086.52 --> 1087.98]  Did they send the generated email?
[1088.62 --> 1089.78]  Did they edit the text?
[1090.30 --> 1097.22]  And all of that feedback data becomes useful both for debugging and also for fine tuning the model later on.
[1097.22 --> 1103.56]  So that evaluation data becomes this rich resource that allows you to continuously improve your application over time.
[1103.96 --> 1104.72]  Yeah, that's awesome.
[1104.90 --> 1106.42]  And I know that that fits in.
[1107.24 --> 1111.60]  So maybe you could talk a little bit about how you're...
[1111.60 --> 1119.70]  One of the things that you mentioned earlier is you're seeing fewer people do fine tuning, which I see this very commonly as a...
[1119.70 --> 1129.80]  It's not an irrelevant point, but it's maybe a misconception where a lot of teams come into this space and they just assume they're going to be fine tuning their models.
[1130.36 --> 1143.26]  And often what they end up doing is fine tuning their workflows or their language model chains or their retrieval, the data that they're retrieving or their prompt formats or that templates or that sort of thing.
[1143.26 --> 1144.94]  They're not really fine tuning.
[1144.94 --> 1159.20]  And I think there's this really blurred line right now for many teams that are adopting AI into their organization where they'll frequently just use the term, oh, I'm training the AI to do this.
[1159.68 --> 1161.24]  And now it's better, right?
[1161.28 --> 1166.48]  But all they've really done is just inject some data into their prompts or something like that.
[1166.48 --> 1186.32]  So could you maybe help clarify that distinction and also, in reality, what you're seeing people do with this capability of evaluation, both online and offline, and how that's filtering back into upgrades to the system or actual fine tunes of models?
[1186.76 --> 1187.54]  Yeah, so I guess you're right.
[1187.58 --> 1190.96]  There's a lot of jargon involved, and especially for people who are new to the field.
[1190.96 --> 1197.44]  The word fine tuning has a colloquial meaning, and then it has a technical meaning in machine learning, and the two end up being blurred.
[1197.76 --> 1210.34]  So fine tuning in a machine learning context usually means doing some extra training on the base model where you're actually changing the weights of the model given some sets of example pairs of inputs, outputs that you want.
[1210.34 --> 1224.32]  And then obviously there's prompt engineering and maybe context engineering where you're changing the instructions to the language model or you're changing the data that's set into the context or how an agent system might be set up.
[1224.68 --> 1225.68]  And both are really important.
[1226.36 --> 1235.06]  Typically, the advice we give the majority of our customers and what we see play out in practice is that people should first push the limits of prompt engineering.
[1235.06 --> 1247.80]  Because it's very fast, it's easy to do, and it can have very high impact, especially around changing the outputs and also in helping the model have the right data that's needed to answer the question.
[1248.22 --> 1253.12]  So prompt engineering is usually where most people start and sometimes where people finish as well.
[1253.92 --> 1264.56]  And fine tuning tends to be useful either if people are trying to improve latency or cost or if they have a particular tone of voice or output constraint that they want to enforce.
[1264.56 --> 1270.74]  So, you know, if people want their model to output valid JSON, then fine tuning might be a great way to achieve that.
[1271.08 --> 1277.90]  Or if they want to use a local private model because it needs to run on an edge device or something like this, then fine tuning, I think, is a great candidate.
[1278.32 --> 1284.48]  And it can also let you reduce costs because oftentimes you can fine tune a smaller model to get similar performance.
[1284.72 --> 1288.04]  The analogy I like to use is fine tuning is a bit like compilation, right?
[1288.04 --> 1291.42]  You have a, you've already sort of built your first version of the language.
[1291.42 --> 1296.16]  When you want to optimize it, you might use a compiled language and you've got a kind of compiled binary.
[1296.80 --> 1300.92]  I think there was a second part to your question, but just remind me, actually, I've lost the second part.
[1300.92 --> 1306.80]  Yeah, basically, you mentioned that maybe fewer people are doing fine tunes.
[1307.68 --> 1325.72]  Maybe you could comment on, I don't know if you have a sense of why that is or how you would see that sort of progressing into this year as more and more people adopt this technology and maybe get better tooling around the, let's not call it fine tuning.
[1325.72 --> 1331.04]  So we don't mix all the jargon, but the iterative development of these systems.
[1331.32 --> 1340.76]  Do you see that trend continuing or how do you see that kind of going into maybe larger or wider adoption in 2024?
[1341.48 --> 1350.60]  Yeah, so I think that we've definitely seen less fine tuning than we thought we would see when we started, you know, when we launched Humanloop back, this version of Humanloop back in 2022.
[1351.34 --> 1353.16]  And I think that's been true of others as well.
[1353.16 --> 1361.56]  Like I've spoken to friends at OpenAI and OpenAI is expecting there will be more fine tuning in the future, but they've been surprised that there wasn't more initially.
[1362.20 --> 1365.76]  I think some of that is because prompt engineering has turned out to be remarkably powerful.
[1366.10 --> 1373.40]  And also because some of the changes that people want to do to these models are more about getting factual context into the model.
[1373.56 --> 1380.92]  So one of the downsides of LLMs today is they're obviously trained on the public internet, so they don't necessarily know private information about your company.
[1380.92 --> 1384.48]  They tend not to know information past the training date of the model.
[1385.10 --> 1390.74]  And, you know, one way you might have thought you could overcome that is I'm going to fine tune the model on my company's data.
[1391.10 --> 1400.24]  But I think in practice, what people are finding is a better solution to that is to use a hybrid system of search or information retrieval plus generation.
[1400.24 --> 1406.40]  So what's come to be known as like RAG or retrieval augmented generation has turned out to be a really good solution to this problem.
[1407.20 --> 1419.04]  And so the main reasons to fine tune now are more about optimizing cost and latency and maybe a little bit tone of voice, but they're not needed so much to adapt the model to a specific use case.
[1419.04 --> 1423.56]  And fine tuning is a heavier duty operation because it takes longer.
[1424.26 --> 1427.60]  You know, you can edit a prompt very quickly and then see what the impact is.
[1428.04 --> 1430.96]  Fine tuning, you need to have the data set that you want to fine tune on.
[1431.28 --> 1434.36]  And then you need to run a training job and then evaluate that job afterwards.
[1435.02 --> 1437.76]  So there are certainly circumstances where it's going to make sense.
[1437.76 --> 1443.76]  I think especially anyone who wants to use a private open source model will likely find themselves wanting to do more fine tuning.
[1444.10 --> 1449.26]  But the quality of prompt engineering and the distance you can go with it, I think, took a lot of people by surprise.
[1449.90 --> 1461.20]  And on that note, you mentioned the closed proprietary model ecosystem versus open models that people might host in their own environment and or fine tune on their own data.
[1461.20 --> 1472.96]  I know that Humanloop, like you explicitly say that you kind of have all of the models, you're integrating these sort of closed models and integrate with open models.
[1473.42 --> 1479.38]  Why and how is that kind of decided to kind of include all of those?
[1479.38 --> 1492.68]  And in terms of the mix of what you're seeing with people's implementations, how do you see this sort of proliferation of open models impacting the workflows that you're supporting in the future?
[1493.26 --> 1496.88]  So the reason for supporting them, again, is largely customer pull, right?
[1496.88 --> 1512.52]  What we were finding is that many of our customers were using a mixture of models for different use cases, either because the large proprietary ones had slightly different performance tradeoffs or because there were use cases where they cared about privacy or they cared about latency.
[1512.70 --> 1515.86]  And so they couldn't use a public model for those instances.
[1516.68 --> 1518.68]  And so we had to support all of them.
[1518.74 --> 1524.64]  It really was something that it wouldn't be a useful product to our customers if it could only use it for one particular model.
[1524.64 --> 1532.10]  And the way we've got around this is that we try to integrate all of the publicly available ones, but we also make it easy for people to connect their own models.
[1532.84 --> 1534.48]  So they don't necessarily need us.
[1534.88 --> 1539.22]  As long as they expose the appropriate APIs, you can plug in any model to Humanloop.
[1539.22 --> 1555.48]  That would be a matter of hosting the model and making sure that the API contract that you're expecting in terms of responses from a model server that maybe someone's running in their own AWS or wherever would fulfill that contract.
[1555.82 --> 1556.58]  That's exactly right.
[1556.86 --> 1557.02]  Yeah.
[1557.02 --> 1566.98]  And in terms of, you know, the proliferation of open source and how that's going, you know, I think there's still a performance gap at the moment between the very best closed models.
[1567.18 --> 1573.40]  So between a GBD4 or some of the better models from Anthropic and the best open source, but it is closing, right?
[1573.40 --> 1577.46]  So the latest models from, say, Mistral have proved to be very good.
[1577.58 --> 1578.82]  Llama 2 was very good.
[1578.82 --> 1588.28]  Increasingly, you're not paying as big a performance gap, although there is still one, but you need to have high volumes for it to be economically competitive to host your own model.
[1588.72 --> 1592.62]  So the main reasons we see people doing it are related to data privacy.
[1593.14 --> 1601.46]  Companies that, for whatever reason, you know, cannot or don't want to send data to a third party end up using open source.
[1601.64 --> 1608.30]  And then also anyone who's doing things on edge and who wants sort of real time or very low latency ends up using open source.
[1608.82 --> 1616.18]  This is a changelog news break.
[1616.62 --> 1623.88]  Vana.ai is a Python RAG framework for accurate text to SQL generation.
[1623.88 --> 1638.38]  It lets you chat with any relational database by accurately generating SQL queries trained via RAG, which stands for Retrieval Augmented Generation, to use with any LLM that you want.
[1638.38 --> 1647.66]  You load up your data definitions, your documentation, and any raw SQL queries you have laying around into Vana, and then you're off to the races.
[1648.12 --> 1658.02]  Vana boasts high accuracy on complex data sets, excellent security and privacy because your database contents are never sent to the LLM or a VectorDB.
[1658.02 --> 1672.96]  It boasts the ability to self-learn by choosing to auto-train on successful queries and a choose-your-own front-end approach with front-ends provided for Jupyter Notebook, Streamlit, Flask, and Slack.
[1672.96 --> 1678.46]  You just heard one of our five top stories from Monday's Changelog News.
[1678.82 --> 1691.24]  Subscribe to the podcast to get all of the week's top stories and pop your email address in at changelog.com slash news to also receive our free companion email with even more developer news worth your attention.
[1691.66 --> 1695.12]  Once again, that's changelog.com slash news.
[1695.12 --> 1704.18]  Well, Reza, I'd love for you to maybe describe if you can.
[1704.28 --> 1706.94]  We've kind of talked about the problems that you're addressing.
[1706.94 --> 1714.46]  We've talked about the sort of workflows that you're enabling, the evaluation, some trends that you're seeing.
[1714.84 --> 1723.64]  But I'd love for you to describe if you can, maybe for like a non-technical persona, like a domain expert who's engaging with the human loop system,
[1723.64 --> 1731.12]  and maybe for a more technical person who's integrating, you know, data sources or other things.
[1731.12 --> 1736.24]  What does it look like to use the human loop system?
[1736.64 --> 1743.82]  Maybe describe the roles in which these people are, like what they're trying to do from each perspective.
[1743.82 --> 1752.60]  Because I think that might be instructive for people that are trying to engage domain experts and technical people in a collaboration around these problems.
[1752.60 --> 1756.42]  Absolutely. So maybe it might be helpful to have a kind of imagined concrete example.
[1756.66 --> 1761.40]  So a very common example we see is people building some kind of question answering system.
[1761.66 --> 1767.74]  Maybe it's for their internal customer service staff, or maybe they want to replace an FAQ that, sorry, I'm just going to drink a water.
[1768.04 --> 1774.78]  Maybe they're trying to build some kind of internal question answering system to replace something or an FAQ or that kind of thing.
[1774.84 --> 1779.80]  So there's a set of documents, a question is going to come in, there'll be a retrieval step, and then they want to generate an answer.
[1779.80 --> 1786.22]  So typically the PMs or the domain experts will be figuring out, you know, what are the requirements of the system?
[1786.36 --> 1788.20]  What does good look like? What do we want it to build?
[1788.80 --> 1797.52]  And the engineers will be building the retrieval part, orchestrating all the model calls and code, integrating the human loop APIs into their system.
[1797.78 --> 1801.02]  And also usually they lead on setting up evaluation.
[1801.02 --> 1808.58]  So maybe once it's set up, the domain experts might continue to do the evaluation themselves, but the engineers tend to set it up the first time.
[1808.80 --> 1814.80]  So if you're the domain expert, typically you would start off in our playground environment where you can just try things out.
[1814.80 --> 1818.40]  So the engineers might connect a database to human loop for you.
[1818.56 --> 1822.82]  So maybe they'll store the data in a vector database and connect that to human loop.
[1823.22 --> 1826.36]  And then once you're in that environment, you could try different prompts to the models.
[1826.64 --> 1833.90]  You could try them to GPT-4, to Cohere, to an open source model, see what impact that has, see if you're getting answers that you like.
[1834.38 --> 1839.30]  Right. Oftentimes early on, it's not in the right tone of voice or the retrieval system is not quite right.
[1839.30 --> 1841.78]  And so the model, it's not giving factually correct answers.
[1841.92 --> 1847.34]  So it takes a certain amount of iteration to get to the point where even when you eyeball it, it's looking appropriate.
[1847.72 --> 1851.98]  And usually at that point, people then move to doing a little bit more of a rigorous evaluation.
[1852.38 --> 1856.58]  So they might generate either automatically or internally a set of test cases.
[1856.86 --> 1861.54]  And they'll also come up with a set of evaluation criteria that matter to them in their context.
[1861.86 --> 1867.28]  They'll set up that evaluation, run it, and then usually at that point, they might deploy to production.
[1867.28 --> 1871.06]  So that's the point at which things would end up with real users.
[1871.26 --> 1872.50]  They start gathering user feedback.
[1873.20 --> 1879.88]  And usually the situation is not finished at that point because people then look at the production logs or they look at the real usage data.
[1880.52 --> 1882.82]  And they will filter based on the evaluation criteria.
[1883.08 --> 1886.26]  And they might say, hey, show me the ones that didn't result in a good outcome.
[1886.62 --> 1891.48]  And then they'll try and debug them in some way, maybe make a change to a prompt, rerun the evaluation and submit it.
[1891.98 --> 1895.54]  And so the engineers are doing the orchestration of the code.
[1895.54 --> 1898.28]  They're typically making the model calls.
[1898.48 --> 1900.46]  They'll add logging calls to human loop.
[1900.64 --> 1903.56]  So the way that works, there's a couple of ways of doing the integration.
[1903.74 --> 1911.64]  But you can imagine every time you call the model, you're effectively also logging back to human loop, what the inputs and outputs were, as well as any user feedback data.
[1912.20 --> 1919.08]  And then the domain experts are typically looking at the data, analyzing it, debugging, making decisions about how to improve things.
[1919.08 --> 1923.04]  And they're able to actually take some of those actions themselves in the UI.
[1923.04 --> 1935.60]  Yeah. And so if I just kind of abstract that a bit to maybe give people a frame of thinking, it sounds like there's kind of this framework set up where there's data sources.
[1936.24 --> 1941.58]  There's maybe logging calls within a version of an application.
[1941.58 --> 1949.58]  There's if you're using a hosted model or if you're using a proprietary API, you decide that.
[1950.40 --> 1952.24]  And so it's kind of set up.
[1952.44 --> 1959.74]  And then there's maybe an evaluation or prototyping phase, let's call it, where the domain experts try their prompting.
[1959.74 --> 1966.80]  Eventually, they find prompts that they think will work well for these various steps in a workflow or something like that.
[1967.04 --> 1978.22]  Those are pushed, as you said, I think, one way into the actual code or application such that the domain experts are in charge of the prompting to some degree.
[1978.22 --> 1987.20]  And as you're logging feedback into the system, the domain experts are able to iterate on their prompts, which hopefully then improve the system.
[1987.42 --> 1993.22]  And those are then pushed back into the production system, maybe after an evaluation or something.
[1993.32 --> 1995.26]  Is that a fair representation?
[1995.88 --> 1996.90]  Yeah, it's a great representation.
[1997.22 --> 1998.72]  Thanks for articulating it so clearly.
[1999.22 --> 2003.48]  And the kinds of things that the evaluation becomes useful for is avoiding regression, say.
[2003.48 --> 2006.52]  Right. So people might notice one type of problem.
[2006.74 --> 2012.20]  They go in and they change a prompt or they change the retrieval system and they want to make sure they don't break what was already working.
[2012.72 --> 2015.60]  And so having good evaluation in place helps with that.
[2015.82 --> 2023.02]  And then maybe it's also worth because I think we didn't sort of do this at the beginning, just thinking about like, what are the components of these LLM applications?
[2023.72 --> 2025.22]  So I think you're exactly right.
[2025.30 --> 2028.98]  We sort of think of the blocks of LLM app being composed of a base model.
[2029.18 --> 2033.02]  So that might be a private fine tune model or one of these large public ones.
[2033.48 --> 2040.68]  A prompt template, which is usually an instruction to the model that might have gaps in it for retrieve data or context.
[2041.24 --> 2043.12]  A data collection strategy.
[2043.84 --> 2052.86]  And then that whole thing of like data collection, prompt template and model might be chained together in a loop or might be repeated, you know, one after another.
[2053.60 --> 2058.88]  And there's an extra complexity, which is the models might also be allowed to call tools or APIs.
[2058.88 --> 2064.28]  So, but I think those pieces to get taken together more or less comprehensively cover things.
[2064.48 --> 2069.40]  So tools, data retrieval, prompt template and base model are the main components.
[2069.62 --> 2072.70]  But then within each of those, you have a lot of design choices and freedom.
[2073.36 --> 2078.88]  And so, you know, you have a combinatorially large number of decisions to get right when building one of these applications.
[2078.88 --> 2087.28]  One of the things that you mentioned is this evaluation phase of what goes on as helping prevent regressions.
[2087.28 --> 2101.40]  Because in sort of testing behaviorally the output of the models, you might make one change on a small set of examples that looks like it's improving things, but has sort of different behavior across a wide range of examples.
[2101.40 --> 2116.26]  I'm wondering also, I could imagine two scenarios, you know, models are being released all the time, whether it's upgrading from this version of a GPT model to the next version or this Mistral fine tune to this one over here.
[2116.26 --> 2123.06]  I'm thinking even, you know, in the past few days, we've been using the neural chat model from Intel a good bit.
[2123.28 --> 2140.54]  And there's a version of that that Neural Magic released that's a sparsified version of that where they pruned out some of the weights and the layers to make it more efficient and to run on better or not better hardware, but more commodity hardware that's more widely available.
[2140.54 --> 2153.44]  And so one of the questions that we were discussing is, well, we could flip the version of this model to the sparse one, but we have to decide on how to evaluate that over the use cases that we care about.
[2153.44 --> 2157.48]  Because you could look at the output for like a few test prompts, right?
[2157.56 --> 2166.84]  And it might look similar or good or even better, but on a wider scale might be quite different in ways that you don't expect.
[2166.84 --> 2180.86]  So I could see that the evaluation also being used for that, but I could also see where if you're upgrading to a new model, it could just throw everything up in the air in terms of like, oh, this is an entirely different prompt format, right?
[2180.94 --> 2188.30]  Or this is a whole new behavior from this new model that is distinct from an old model.
[2188.48 --> 2193.40]  So how are you seeing people navigate that landscape of model upgrades?
[2193.40 --> 2197.66]  I think you should just view it as a change as you would to any other part of the system.
[2197.82 --> 2200.66]  And hopefully the desired behavior of the model is not changing.
[2201.16 --> 2210.70]  So even if the model is changed, you still want to run your regression test and say, okay, are we meeting a minimum threshold that we had on these gold standard test set before?
[2211.26 --> 2215.88]  In general, I think evaluation, we see it happening at sort of three different stages during development.
[2215.88 --> 2225.62]  There's during this interactive stage very early on when you're prototyping, you want fast feedback, you're just looking to get a sense of, you know, is this even working appropriately?
[2225.96 --> 2232.12]  At that stage, you know, eyeballing examples and looking at things side by side in a very interactive way can be helpful.
[2232.56 --> 2235.54]  And interactive testing can also be helpful for adversarial testing.
[2236.16 --> 2241.98]  So, you know, a fixed test set doesn't tell you what will happen when a user who actually wants to break the system comes in.
[2241.98 --> 2250.64]  So a concrete example of this, you know, one of our customers has children as their end users, and they want to make sure that things are age appropriate.
[2250.88 --> 2252.56]  So they have guardrails in place.
[2252.78 --> 2260.64]  But when they come to test the system, they don't want to just test it for against, you know, a use case, an input that's benign.
[2260.92 --> 2264.62]  They want to see like, if we try, if we really red team this, can we break it?
[2265.02 --> 2267.16]  And their interactive testing can be very helpful.
[2267.16 --> 2274.58]  And then the next place where you kind of want testing in place is this regression testing, where you have a fixed set of evaluators on a test set.
[2274.76 --> 2276.98]  And you want to know when I make a change, does it get worse?
[2277.46 --> 2280.26]  And the final place we see people using it is actually for monitoring.
[2280.74 --> 2282.22]  So, okay, I'm in production now.
[2282.66 --> 2284.08]  There's new data flowing through.
[2284.22 --> 2288.26]  I may not have the ground truth answer, but I can still set up different forms of evaluator.
[2288.58 --> 2292.34]  And I want to be alerted if the performance drops below some threshold.
[2292.34 --> 2309.46]  So one of the things that I've been thinking about throughout our conversation here, and that's, I think, highlighted by what you just mentioned, and sort of the upgrades to one's workflow and the various levels at which such a platform can benefit teams.
[2309.46 --> 2326.26]  And it made me think of, you know, used to, I have a background in physics, and there were plenty of physics teams or collaborators that we worked with, you know, we were writing code, and not doing great sort of version control practices.
[2326.26 --> 2328.64]  And not everyone was using GitHub.
[2329.06 --> 2342.74]  And there was sort of collaboration challenges associated with that, which are obviously solved by great code collaboration systems that are of various forms that have been developed over time.
[2342.84 --> 2352.48]  And I think there's probably a parallel here with some of the collaboration systems that are being built around both playgrounds and prompts and evaluation.
[2352.48 --> 2378.48]  I'm wondering if you could, if there's any examples from clients that you've worked with, or maybe it's just interesting use cases of surprising things they've been able to do when going from sort of doing things ad hoc and maybe versioning prompts in spreadsheets or whatever it might be to actually being able to work in a more seamless way between domain experts and technical staff.
[2378.48 --> 2384.88]  Are there any clients or surprising stories that come to mind?
[2384.88 --> 2385.82]  Yeah, it's a good question.
[2385.94 --> 2390.44]  I'm kind of thinking through them to see, you know, what the more interesting examples might be.
[2390.98 --> 2395.98]  I think that fundamentally, it's not necessarily enabling completely new behavior, right?
[2396.06 --> 2400.98]  But it's making the old behavior significantly faster and less error prone.
[2401.62 --> 2407.34]  So, you know, certainly fewer mistakes and less time spent, you know, one, okay, so surprising example,
[2407.34 --> 2420.00]  publicly listed company, and they told me that one of the issues they were having is because they were sharing these prompt configs in teams, they were having differences in behavior based on white space being copied.
[2420.22 --> 2428.30]  So the, you know, someone was like playing around with the opening eye playground, they'd copy paste it into teams, that person would copy paste from teams into code.
[2428.30 --> 2434.60]  And there was small white space differences, and you wouldn't think it should affect the models, but it actually did.
[2435.06 --> 2437.68]  And so they would then get performance differences they couldn't explain.
[2438.14 --> 2443.28]  And actually, it just turned out that, you know, you shouldn't be sharing your code via team, right?
[2443.54 --> 2445.96]  So I guess that's one surprising example.
[2446.46 --> 2453.04]  I think another thing as well is the complexity of apps that people are now beginning to be able to build.
[2453.04 --> 2458.38]  So increasingly, I think people are building simple agents, right?
[2458.48 --> 2461.26]  I think more complex agents are still not super reliable.
[2461.84 --> 2469.58]  But a trend that we've been hearing a lot about from our customers recently, is people trying to build assistants that can use their existing software.
[2470.26 --> 2477.96]  So, you know, an example of this is, you know, Ironclad is a company that's added a lot of LLM based features to their product.
[2477.96 --> 2489.00]  And they actually are able to automate a lot of workflows that were previously being done by humans, because the models can use the APIs that exist within the Ironclad software.
[2489.16 --> 2492.08]  So they're actually, you know, able to leverage their existing infrastructure.
[2492.60 --> 2495.56]  But to get that to work, they had to innovate quite a lot in tooling.
[2496.10 --> 2498.00]  And in fact, you know, this isn't the plug for HumanLoop.
[2498.10 --> 2505.70]  Ironclad, in this case, built a system called Rivet, which is their own open source, you know, prompt engineering and iteration framework.
[2505.70 --> 2514.98]  But I think it's a good example of, you know, in order to achieve the complexity of that use case, this happened to be before tools like HumanLoop around, they had to build something themselves.
[2515.60 --> 2517.20]  And it's quite sophisticated tooling.
[2517.62 --> 2518.62]  I actually think Rivet's great.
[2518.76 --> 2520.16]  So people should check that out as well.
[2520.24 --> 2521.22]  It's an open source library.
[2521.32 --> 2522.56]  Anyone can go and get the tool.
[2523.24 --> 2530.64]  So, yeah, I think the surprising things are like how error prone things are without good tooling and the crazy ways in which people are solving problems.
[2530.64 --> 2536.58]  Another example of a mistake that we saw someone do is two different people triggered exactly the same annotation job.
[2537.12 --> 2545.90]  So they had annotation and spreadsheets and they both outsourced the same job to different annotation teams, which is obviously an expensive mistake to make.
[2546.48 --> 2547.54]  So very error prone.
[2547.96 --> 2552.82]  And then I think also just like impossible to scale to more complex agentic use cases.
[2552.82 --> 2559.36]  Well, you already kind of alluded to some trends that you're seeing moving forward.
[2559.36 --> 2582.30]  As we kind of draw to a close here, I'd love to know from someone who's seeing a lot of different use cases being enabled through HumanLoop and your platform, what's exciting for you as you move into this next year in terms of maybe it's things that are happening in AI more broadly or things that are being enabled.
[2582.30 --> 2588.56]  By HumanLoop or things that are on your roadmap that you can't wait for them to go live.
[2588.68 --> 2595.50]  What as you're lying in bed at night and getting excited for for the next day of AI stuff, what's on your mind?
[2595.92 --> 2601.98]  So AI more broadly, I just feel the rate of progress of capabilities is both exciting and scary.
[2602.10 --> 2603.26]  Right. It's extremely fast.
[2603.40 --> 2607.34]  Multimodal models, better generative models, models with increased reasoning.
[2607.34 --> 2613.54]  I think the range of possible applications is expanding very quickly as the capabilities of the models expand.
[2614.10 --> 2618.22]  I think people have been excited about agent use cases for a while, right?
[2618.30 --> 2622.08]  Systems that can act on their own and go off and achieve something for you.
[2622.18 --> 2626.66]  But in practice, we've not seen that many people succeed in production with those.
[2626.74 --> 2629.12]  There are a couple of examples, Ironclad being a good one.
[2629.54 --> 2632.36]  But it feels like we're still at the very beginning of that.
[2632.36 --> 2635.90]  And I think I'm excited about seeing more people get to success with that.
[2636.18 --> 2646.58]  I'd say that the most common successful applications we've seen today are mostly either retrieval augmented applications or more simple LLM applications.
[2646.90 --> 2651.72]  But increasingly, I'm excited about seeing agents in production and also multimodal models in production.
[2651.72 --> 2659.66]  In terms of things that I'm particularly excited about from HumanLoop is, I think, us becoming a proactive rather than a passive platform.
[2659.84 --> 2664.38]  So today, the product managers and the engineers drive the changes on HumanLoop.
[2664.68 --> 2674.30]  But I think that's something that we're going to hopefully release later this year is actually where the system, you know, HumanLoop itself can start proactively suggesting improvements to your application.
[2674.30 --> 2682.28]  Because we have the evaluation data, because we have all the prompts, we can start saying things to you like, hey, you know, we have a new prompt for this application.
[2682.62 --> 2684.22]  It's a lot shorter than the one you have.
[2684.30 --> 2685.80]  It scores similarly on eval data.
[2686.20 --> 2688.82]  If you upgrade, we think we can cut your costs by 40%.
[2688.82 --> 2691.78]  And allowing people to then accept that change.
[2691.86 --> 2696.44]  And so going from a system that is observing to a system that's actually intervening.
[2696.96 --> 2697.40]  That's awesome.
[2697.40 --> 2711.90]  Yeah, well, I definitely look forward to seeing how that rolls out and really appreciate the work that you and the team at HumanLoop are doing to help us upgrade our workflows and enable these sort of more complicated use cases.
[2712.18 --> 2715.60]  So thank you so much for taking time out of that work to join us.
[2715.82 --> 2716.90]  It's been a pleasure.
[2717.26 --> 2718.60]  Really enjoyed the conversation.
[2719.02 --> 2719.98]  Thanks so much for having me, Daniel.
[2719.98 --> 2720.12]  Thank you.
[2727.40 --> 2730.96]  All right, that is Practical AI for this week.
[2731.76 --> 2732.80]  Subscribe now.
[2732.96 --> 2737.96]  If you haven't already, head to practicalai.fm for all the ways.
[2738.36 --> 2744.34]  And join our free Slack team where you can hang out with Daniel, Chris, and the entire ChangeLog community.
[2744.94 --> 2749.56]  Sign up today at practicalai.fm slash community.
[2750.10 --> 2757.12]  Thanks again to our partners at fly.io, to our Beat Freakin' Residence, Breakmaster Cylinder, and to you for listening.
[2757.40 --> 2759.22]  We appreciate you spending time with us.
[2759.62 --> 2760.76]  That's all for now.
[2761.02 --> 2762.68]  We'll talk to you again next time.
[2766.68 --> 2768.64]  Bye.
