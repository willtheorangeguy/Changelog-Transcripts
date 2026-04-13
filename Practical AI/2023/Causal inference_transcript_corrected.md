[0.00 → 8.64] Welcome to Practical AI.
[9.20 → 15.96] If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 → 18.78] are changing the world, this is the show for you.
[19.20 → 24.36] Thank you to our partners at Vastly for shipping all of our pods superfast to wherever you
[24.36 → 24.66] listen.
[24.92 → 26.76] Check them out at Fastly.com.
[26.76 → 32.02] And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 → 33.70] No ops required.
[34.02 → 36.08] Learn more at fly.io.
[43.14 → 46.68] Welcome to another episode of Practical AI.
[47.08 → 48.68] This is Daniel Whiten ack.
[48.76 → 52.28] I'm a data scientist building a tool called Prediction Guard.
[52.28 → 58.32] And I'm joined as always by my co-host Chris Benson, who is a tech strategist at Lockheed
[58.32 → 58.60] Martin.
[58.74 → 59.50] How are you doing, Chris?
[60.04 → 61.30] I am doing very well.
[61.50 → 66.12] I've been watching you building Prediction Guard from afar and looking forward to hearing more
[66.12 → 67.22] about it in the days ahead.
[67.56 → 68.46] It's a fun one.
[68.54 → 71.46] We'll talk about it in more detail soon.
[71.46 → 79.34] And the causal reasons why I ended up doing those things that I'm doing.
[79.68 → 80.68] Could that be a transition?
[80.98 → 81.32] Yes.
[81.32 → 88.16] Speaking of cause and effect and causal things, we're really privileged today to have with
[88.16 → 94.04] us Paul Runaround, who's an assistant professor at Copenhagen Business School.
[94.54 → 95.32] Welcome, Paul.
[95.90 → 96.40] Hi, Daniel.
[96.56 → 97.10] Hi, Chris.
[97.62 → 98.40] Thanks for having me.
[98.40 → 101.24] Yeah, yeah, it's great to have you here.
[101.38 → 106.06] And I think also this is so cool because I think the topic that we're going to talk about
[106.06 → 112.22] is so very practical and important because I've tried to do, as many of our listeners
[112.22 → 118.18] know, my wife owns a business, and I've tried to do a bunch of like analytics or like predictive
[118.18 → 122.44] things for her over the years, just out of either need or fun.
[122.44 → 129.48] And often the question is like, why is the prediction that, or what like for a business
[129.48 → 132.98] person, like they're wanting to know what is the attribution?
[133.20 → 136.24] What is the behaviour behind this thing that I'm seeing?
[136.36 → 142.50] So you're an expert in causal AI, causal machine learning and have been doing research in this
[142.50 → 144.68] area and are very well versed in it.
[144.68 → 151.52] And I'm wondering if you can, as you start out here, just like give a brief understanding
[151.52 → 156.66] to everyone about like, what do you mean when you say causal AI or causal machine learning?
[156.90 → 164.04] And how maybe is that differentiated from what people might commonly think of when they think
[164.04 → 165.44] of AI or machine learning?
[165.44 → 171.44] So, I mean, then many names, causal AI, causal machine learning, causal inference, I think
[171.44 → 173.66] is the more traditional term.
[174.12 → 180.18] But I think the basic idea is pretty intuitive for everyone who works with data is that if
[180.18 → 186.12] we look at correlations and patterns in the data, sometimes they can produce quite surprising
[186.12 → 188.54] and probably nonsense results.
[188.54 → 195.40] I mean, we all know the story about ice cream sales and shark attacks that are highly correlated
[195.40 → 202.08] over the course of the year, chocolate consumption and Nobel Prize winners in the country, right?
[202.18 → 205.34] Probably driven by Switzerland predominantly.
[206.20 → 207.66] Storks in the babies, right?
[207.74 → 210.76] Like the stork population and fertility rates are correlated.
[211.46 → 217.20] With these examples, we usually use them in the classroom as sort of like a caveat, right?
[217.20 → 220.80] Wait a minute, a correlation is not causation.
[221.08 → 222.32] People have heard this term.
[222.88 → 229.24] But then causal inference and causal machine learning is really this idea of taking causality seriously
[229.24 → 236.94] and trying to build tools, algorithms that allow you to draw causal inference from data
[236.94 → 242.40] to distinguish cause and effect and weed out the kind of nonsense correlations.
[242.70 → 245.60] And yeah, that comes with a different tool set.
[245.60 → 250.46] So, I mean, you can approach this from a purely algorithmic point of view, and you would probably
[250.46 → 253.74] apply different tools than standard machine learning.
[254.34 → 255.60] It goes even deeper.
[255.80 → 258.22] There's a whole epistemological point about it.
[258.70 → 264.06] Well, if you want to do causal inference, you cannot do this in a purely model-free way.
[264.64 → 269.76] You actually need background knowledge, expert domain knowledge in order to do this,
[269.76 → 274.70] in order to, for example, distinguish between possible alternative explanations.
[275.50 → 281.66] And that is a whole paradigm shift in terms of how we approach data and how we approach machine learning.
[282.20 → 287.56] Well, and then my last word on this is what's the difference to standard machine learning is that,
[287.62 → 292.14] well, standard machine learning, the bulk of it is really correlation-based.
[292.14 → 297.02] I mean, all the tools that we're having, deep learning, support vector machines, and so on,
[297.10 → 299.02] those are predictive tools.
[299.56 → 303.86] Prediction means correlation, finding, detecting patterns and data.
[304.54 → 306.32] And so, they're not suitable for it.
[306.94 → 310.86] I mean, there's a branch of AI that is reinforcement learning.
[310.86 → 316.52] Maybe we could talk about this later that goes more in the direction of actually intervening yourself.
[316.68 → 319.56] The learner intervenes itself in the environment.
[320.06 → 324.24] So, that goes in the right direction, but it's not getting there a full way.
[324.58 → 326.74] This is the main difference to standard machine learning.
[326.90 → 334.68] That kind of gets to the what, I guess, of what is causal AI, causal machine learning, causal inference.
[334.68 → 340.46] I guess the next question that's probably a good foundational one is the why.
[341.00 → 344.16] And maybe this is even exacerbated in recent times.
[344.24 → 348.88] I don't know if you've seen this with all of this sort of hype around large language models
[348.88 → 355.02] that are incredibly non-interpretable or produce, you know, things that are very factually incorrect
[355.02 → 356.64] or unexplainable.
[356.64 → 365.14] But how should a data scientist working in an enterprise, let's say, like, why should they care about causal inference
[365.14 → 369.30] rather than just making good predictions, let's say?
[370.06 → 375.84] Yeah, so maybe it helps if I've defined first what I mean exactly with causal inference
[375.84 → 381.00] because there's actually a neat definition by James Woodward, which is a philosopher of science,
[381.00 → 386.80] who said that causal inference or causal machine learning is a special kind of prediction problem.
[386.92 → 388.72] So, in a sense, it is a prediction problem.
[389.30 → 395.28] But here we are predicting the likely impact of an action, intervention, or manipulation.
[395.56 → 401.36] Really this idea of I do something, like I increase the chocolate consumption in a country.
[401.82 → 405.56] Will that produce more Nobel Prize winners, right, in this context?
[405.56 → 411.28] I think if we approach from that perspective, you immediately see the value for business
[411.28 → 414.58] because in business we are always asking this kind of questions.
[414.82 → 416.00] What if we do X?
[416.16 → 419.70] What if we implement this new HR policy?
[419.98 → 422.06] What if we enter a new market?
[422.38 → 425.36] Should we invest in this product or another product?
[425.60 → 433.60] So, business always involves actions, interventions, and we want to forecast, predict the likely outcomes of this.
[433.60 → 439.02] That would be, well, what causal inference people call the interventional level.
[439.20 → 443.38] Then one level above that is the counterfactual level.
[444.02 → 448.90] So, counterfactual meaning we're reasoning about two states of the world.
[449.68 → 455.44] Had I not taken the aspirin this morning, would my headache be worse today still?
[455.66 → 456.76] This kind of questions.
[456.76 → 461.76] And they are also very relevant in sort of hindsight retrospective.
[462.58 → 468.90] Like, was it, again, HR policy that we implemented that improved employee satisfaction and so forth?
[469.04 → 473.22] So, immediately relevant in all sorts of domains in the business world.
[473.90 → 482.08] Specifically in AI, we're talking about fundamental problems in AI, which is fairness, robustness, explainability.
[482.08 → 486.72] And I believe that causal AI has to say something in all of these domains.
[486.98 → 490.78] So, there's also an immediate practical value in this.
[491.40 → 500.44] Let me ask you a question on, I want to throw another term that we haven't used yet that sometimes gets thrown in casual causal conversations.
[500.44 → 501.70] Say that 10 times fast.
[501.70 → 504.36] It's determinism versus non-determinism.
[504.56 → 509.50] Because we have a habit of applying that at a high level with AI models and say, oh, they're non-deterministic.
[509.76 → 523.02] And there's a certain expectation over the years in training AI models that are non-deterministic in terms of you do have that disconnect in terms of understanding that causality from beginning to end.
[523.02 → 536.22] Can you kind of distinguish a little bit between the two terms in the sense of if someone is just kind of getting into this, they're early in data science, and they're trying to go, wait a minute, I thought AI was non-deterministic, but yet causality is explainable.
[536.64 → 537.74] How do those fit together?
[537.94 → 546.14] How do those as slices of perspective on an AI model, how do they work together where you have determinism, non-determinism, and causality or not?
[546.18 → 547.64] And what are the implications of those?
[547.64 → 558.90] When I put out the definition, I used the term likely impact, and that already hints at that also causal inference, the approaches that we have being our probabilistic framework.
[559.18 → 561.56] So there's no determinism in this.
[561.72 → 568.18] What we're interested in is still a probability or contrast of two probabilities, right?
[568.18 → 575.64] The probability of a certain outcome that I care about if I had taken the specific action or if I hadn't.
[575.64 → 585.92] So these are factual questions, but it's still, there's no determinism in the sense that if I implement something, it will always work, or we will always have success with this product and so forth.
[586.58 → 597.64] There's an interesting, I think, sort of intellectual history because the frameworks that we're having in causal inference-directed acyclic graphs developed by Judea Pearl and this kind of people,
[597.64 → 613.92] they built on actually earlier work in AI, like Bayesian nets, for example, that were at that point still a purely predictive tool, but a way or tool to deal with complexity in terms of probabilities because, yeah, expert systems were too rigid.
[614.46 → 616.36] We figured that out in the 70s and 80s.
[616.36 → 626.62] And building on that, then people immediately, once you reason probabilistically, people made the shortcut, the mental shortcut in reasoning in terms of cause and effect,
[626.88 → 632.66] probably because it's so intuitive to us, but the tools were actually not ready for it yet.
[632.76 → 638.34] So that was the intellectual history, how we move from probabilistic AI frameworks to causal inference.
[638.34 → 645.96] And again, I think people immediately started to think that way because causality is such a fundamental concept for human thinking, right?
[645.98 → 648.54] We learn it very early in our development.
[649.26 → 650.84] Babies can think causally.
[651.26 → 655.04] There's some psychology work that we picked that up at the age of two or so.
[655.68 → 658.46] Pets sometimes can think causally probably.
[658.62 → 660.14] So it's a very fundamental concept.
[660.14 → 672.80] Have you found like in practically interacting, because I know you're involved sort of in the data science community as well and have helped run events and other things related to this topic.
[673.04 → 682.70] Have you found data scientists are sort of because I could see some data scientists were so in the mindset of like we're making a prediction.
[682.70 → 689.32] We probably understand that we're thinking about correlations in many cases, I think.
[689.82 → 702.14] But then it's sort of scary for us to think about like, well, I don't know if I want to like to put out a if I tell my executive like this is the reason that something happened, like I can see the value of it.
[702.24 → 704.22] But how confident can I be in that?
[704.22 → 724.20] And that also gets to maybe people's, I think people during COVID and other times realized maybe how rusty they were on like basic statistical and probable, probabilistic type of concepts where, you know, everyone was all of a sudden thinking about medical trials and such.
[724.20 → 729.54] Have you found this sort of hesitation amongst data scientists as you've interacted with them?
[729.88 → 738.28] And what maybe is some steps that data scientists can take to gain confidence in initial thinking and education around this topic?
[738.92 → 746.20] Yeah, so we talked with a lot of data scientists from industry practitioners, and I don't think there's hesitation.
[747.06 → 747.80] It's actually the opposite.
[747.98 → 748.96] There's lots of interest.
[749.10 → 751.10] Of course, this is sort of a new topic.
[751.10 → 754.48] You need to tool up in a different area.
[754.94 → 758.20] So, I mean, that's a step that you need to take.
[758.26 → 759.88] But many people are very curious.
[760.70 → 764.98] And we just simply wanted to understand sort of where are we right now?
[765.04 → 771.60] And we had a hunch that this is the toolbox that we know, predictive analytics, correlational AI.
[772.08 → 776.60] And then based on that, what kind of questions practically do you address?
[777.08 → 780.68] Also, maybe in the interplay with the broader organization, right?
[780.68 → 783.04] What is it that the executives want to know?
[783.18 → 784.60] What do they approach you with?
[785.14 → 791.02] And is there sort of a mismatch between the methods that you're working with and the questions that are asked?
[791.16 → 800.66] And in our interviews, and we did some qualitative analysis on this too, we could clearly see this kind of mismatch between many questions that are asked.
[800.66 → 803.54] Do we actually have this causal component to it?
[803.64 → 808.14] Because actions, forecasting, interventions is so ubiquitous.
[808.76 → 812.16] The standard tools, right, are not up to the task for this.
[812.38 → 819.04] And that creates actually this interest in approaching causal inference and looking beyond what we currently do.
[819.04 → 826.10] So one interview is stuck to my mind was an IT consultant that was working a lot in the data science field.
[826.64 → 832.20] And he said, like, yeah, most of the questions that our clients asked are causal questions in the end.
[832.56 → 838.40] But what we do in the end with them is always some form of predictive analytics, deep learning and so forth.
[838.82 → 843.04] That always created this kind of tension in the projects that he was working in.
[843.04 → 845.68] So that was very eye-opening for us.
[850.50 → 853.80] It is now time for a changelog news break.
[854.40 → 861.64] The team at Sun AI is helping change the game in text-to-speech realism by releasing Bark,
[861.94 → 869.32] a transformer-based text-to-audio model that can generate highly realistic multilingual speech as well as other audio,
[869.58 → 872.60] including music, background noise, and simple sound effects.
[873.04 → 879.08] It can also laugh, sigh, cry, and make other non-word sounds that people make.
[879.50 → 880.10] Crazy, right?
[880.90 → 885.20] Here's an example that includes sad and sighs meta tags.
[885.68 → 888.02] My friend's bakery burned down last night.
[889.92 → 892.70] Now his business is toast.
[893.28 → 895.32] And here's one more with laughter.
[895.64 → 899.50] I don't like PyTorch, Kubernetes, or schnitzel.
[900.34 → 902.18] And xylophones flummox me.
[903.04 → 907.54] You can still hear some digital artifacts and blips here and there,
[907.64 → 913.20] but we're getting closer to synthesized audio that's indistinguishable from the real thing.
[913.90 → 915.96] And that's cool slash scary.
[915.96 → 921.60] You just heard one of our five top stories from Monday's changelog news.
[921.92 → 928.62] Subscribe to the podcast to get all the week's top stories and pop your email address in at changelog.com slash news
[928.62 → 934.32] to also receive our free companion email with even more developer news worth your attention.
[934.74 → 938.18] Once again, that's changelog.com slash news.
[938.18 → 965.28] Well, Paul, you've described really well how to think about generally this sort of causal inference, causal AI, causal machine learning, the importance of it.
[965.28 → 975.30] And you mentioned that in doing causal inference, you have sort of a different tool set or maybe different algorithms that are applied.
[975.80 → 986.50] I know that one thing that, of course, I've done before and know about from various data science positions is like experimentation or hypothesis testing, like A-B testing.
[986.50 → 988.92] I know that only scratches the surface.
[989.08 → 993.32] You were talking about, you know, direct-to-case cyclic graphs and other things.
[993.72 → 1006.38] So could you give us like a broad sketch of like currently what are the like main categories of approaches within causal inference, and how can we think about those?
[1006.38 → 1017.24] Like from really broad categorization, traditionally people divided the field into experimental and observational methods.
[1017.80 → 1021.62] And experimental would be the A-B testing that you're talking about.
[1021.94 → 1028.56] One of our interviews even called it the big hammer that tech companies swing around A-B testing.
[1028.56 → 1038.86] And it's applied a lot, sometimes together with some form of multi-armed banded reinforcement learning type of approaches, but often just in a plain vanilla way.
[1039.38 → 1047.40] And that's great because, well, experiments are easy in many domains to set up, easy to understand.
[1047.62 → 1050.50] And you don't need a lot of background knowledge for it.
[1050.50 → 1052.56] You simply try out different things.
[1052.64 → 1055.34] Search shades of a button on a website, classic example.
[1055.34 → 1061.60] But in other domains, it's really not that simple because, well, experiments can be very costly.
[1061.80 → 1064.24] They can be unethical in many questions.
[1064.40 → 1067.42] I think you mentioned the COVID pandemic earlier.
[1067.68 → 1077.50] That was an interesting example to observe because when we tested the vaccines, of course, we did the standard clinical trials, which is an experimental method.
[1077.66 → 1079.38] And A-B testing if you want, right?
[1079.38 → 1085.96] That costs a lot of money, but we have these procedures for it, and we need to approve drugs in that way.
[1086.34 → 1090.34] But then after we rolled out the vaccines, immediately there were follow-up questions.
[1090.54 → 1093.62] Like, for example, where is the vaccine more effective?
[1093.80 → 1096.60] Is it for an older population or a younger population?
[1097.02 → 1102.00] Or in which way do we need to roll out scarce vaccines and so forth?
[1102.00 → 1106.10] This kind of questions, they were not included in the control trial.
[1106.26 → 1108.06] We didn't have experimental evidence for it.
[1108.46 → 1111.74] We needed to answer this based on ex-post data.
[1111.98 → 1117.04] So people picking up vaccines and then seeing where they're most effective.
[1117.78 → 1124.02] That was interesting to see because many of the questions that we ask in practice do involve this observational causal inference.
[1124.02 → 1136.40] And with observational causal inference, I mean we don't actively intervene ourselves, but we passively observe the data and still want to get cause and effect out of it, although we haven't designed the experiment also.
[1136.40 → 1143.52] So in a sense, we're then trying to mimic a thought experiment, if you want, with observational data.
[1143.52 → 1154.40] And that creates all sorts of problems because, well, those people that picked up the vaccine earlier probably are those that thought they have the most to gain from it, for example.
[1154.52 → 1160.08] So there's this sort of self-selection bias or confounding bias in this, and we need to address all of these things.
[1160.76 → 1162.88] These are the two main categories.
[1163.16 → 1172.84] And then within those categories, we have all sorts of different techniques, algorithms like experimental design is an entire course catalogue at our university.
[1173.52 → 1179.00] In the observational fields, so for example, I originally come from an econometrics background.
[1179.88 → 1184.14] And in econometrics or in economics, we ask a lot of causal questions.
[1184.14 → 1191.66] And then we have tools like regression discontinuity design, difference in differences, nearest neighbour matching, and so forth.
[1192.20 → 1198.20] The new kid on the block are the computer scientists, and they catch up fast in causal inference.
[1198.20 → 1204.42] And they develop these techniques like directed acyclic graphs, causal reinforcement learning.
[1204.62 → 1208.88] So all sorts of exciting streams of literature coming up these days.
[1209.52 → 1212.40] I'm really trying to absorb what you're saying, and it's very interesting.
[1212.40 → 1223.68] I'm kind of wondering if I have a problem today, like before our conversation, and I want to go through your kind of the typical data prep and, you know, model training and model testing to deploy.
[1224.08 → 1230.44] But now I've listened to you, and I want to start implementing causal approaches into my workflow.
[1230.74 → 1232.34] How does my workflow change?
[1232.46 → 1235.00] What does it look like with typical tools now?
[1235.18 → 1239.24] And where might gaps be in the typical tool chain that we currently have?
[1239.32 → 1241.36] How do we make it practical and go do it after the show?
[1241.36 → 1248.96] Starting from the epistemological challenge is that we cannot do causal inference in a purely data-driven way.
[1249.12 → 1256.16] We cannot just optimize a target function and or look at our confusion matrix loss function in that sense.
[1256.68 → 1265.54] We need to complement this with background knowledge that, well, in the simple examples, right, it's not just ice cream sales and shark attacks.
[1265.54 → 1271.58] There's a third variable lurking, right, which we need to consider, which is the weather probably or sunshine.
[1272.14 → 1274.08] So this is in the simple case.
[1274.24 → 1278.84] But now imagine a problem that you approach for the first time, right?
[1278.84 → 1281.86] You do exploratory research, so you don't have this good theory.
[1282.36 → 1283.98] So we need to do something about this.
[1283.98 → 1291.82] Then a lot of the standard challenge that we are having, right, collecting good data, maybe designing an A-B test are the same.
[1291.82 → 1302.90] But this additional step of bringing in background knowledge, and there it depends, I guess, right, like how also the data science team is structured in an organization.
[1303.52 → 1305.92] Do we need to bring in outside stakeholders?
[1306.58 → 1311.68] Do we maybe need to talk with the marketing people or the logistics people, depending on the project?
[1311.68 → 1317.38] Often at the moment, data science teams are almost this kind of in-house consulting type, right?
[1317.54 → 1322.78] And there are, for example, not that many mixed teams that could bring in this background expert domain knowledge.
[1323.46 → 1329.84] Practically speaking, I mean, there are all sorts of tools out there in the standard software languages.
[1330.38 → 1336.14] Like it's a little bit scattered, probably, the landscape, so you really need to know what kind of libraries are out there.
[1336.14 → 1349.24] For example, in Python, the do-why package by Microsoft really became a standard industry-wide because they also have this kind of causal inference pipeline implemented in the package,
[1349.32 → 1358.88] which starts from sort of modelling a specific domain or phenomenon to applying the causal inference algorithms, getting causal effects out,
[1358.98 → 1362.22] and then also refuting the model or challenging the model.
[1362.22 → 1369.34] So you have this kind of step-by-step procedure that can really help you in getting started and getting results quickly.
[1370.16 → 1379.92] One of the things that you said that I wanted to ask kind of a clarifying question was you kind of talked about going to that kind of external source, the extra authority, if you will.
[1380.36 → 1385.30] A lot of practitioners these days are kind of starting on their own if they're not on a big data science team.
[1385.60 → 1391.80] Like, you know, I work in a big company, and we have tons of data scientists, so this probably doesn't apply to me in that capacity.
[1391.80 → 1403.00] But a lot of people in startups are out there trying to kind of delve into new businesses and stuff, and they may not have access to kind of outside the data expertise to apply.
[1403.12 → 1414.42] Do you have any tips or guidance on, like, if you're that practitioner, and you're trying to solve a problem for which you don't have that external expertise, how would you go about tackling that?
[1414.42 → 1424.10] How would you go about saying, it's me, myself, and I, you know, joking around, and I'm going to, this is a way I can apply causal approaches when I don't have a lot of resources available to me?
[1424.62 → 1427.78] First, I would say you're never really alone, right?
[1427.78 → 1427.96] True.
[1427.96 → 1430.18] So I think outside the box a little bit.
[1430.28 → 1432.46] I mean, often it doesn't take that much.
[1432.54 → 1439.24] You can just approach people and maybe talk with them for an hour and get the insights out that you need.
[1440.16 → 1450.76] Consulting, probably the scientific literature on a certain topic can help too in sort of figuring out alternative explanations that you can then bring to the data and test to the data.
[1450.76 → 1456.98] But we're also not completely helpless in the sense that everything has to come from the theory.
[1457.24 → 1458.78] There are data-driven approaches.
[1459.20 → 1468.14] So that would be the area of causal discovery that we can apply to get closer to kind of causal model based on the relationships that we find in the data.
[1468.14 → 1471.48] We know that never gets us 100% all the way.
[1472.20 → 1477.36] So we will always need to complement it with some form of background knowledge, but it can already help.
[1477.36 → 1484.84] And then I would say, I mean, talking also to practitioners, I think sort of the 80-20 rule, I think it's called, right, applies.
[1485.04 → 1489.56] I mean, already getting closer to something causal is often good enough.
[1489.56 → 1496.24] And we should get away from this idea that it's a zero-one, right, that either it's causal or it's not.
[1496.42 → 1498.44] Often we get closer to the truth.
[1498.58 → 1507.04] And if not, we can do, for example, there are whole tools on sensitivity analysis that we can challenge our assumptions and see how robust they are.
[1507.36 → 1509.86] And I think in practice this already helps tremendously.
[1510.30 → 1514.84] You mentioned kind of reaching out to practitioners and the community around this.
[1514.96 → 1515.98] Could you describe a little bit?
[1516.06 → 1524.24] I know, like I mentioned earlier, there are some resources that you've kind of helped co-found and run over time related to this.
[1524.34 → 1528.50] Could you mention those so that people could find those as they're looking into the topic?
[1528.50 → 1541.66] Based on what we identified in where the field is, we actually saw the need for more exchange between different academic fields because causal inference is such a general purpose technology almost.
[1541.84 → 1543.72] It's applied in various different fields.
[1544.06 → 1549.98] I mentioned economics, computer science, epidemiology, health sciences, but then also practitioners.
[1549.98 → 1552.38] So it's really like a mixed group.
[1552.90 → 1555.98] So we set up the annual causal data science meeting.
[1556.34 → 1568.64] We started in 2020, so had to do it online because of the COVID pandemic and then realized that it's really an easy way to get people into one, well, virtual room in this case.
[1568.72 → 1570.52] And there was lots of interest from practitioners.
[1570.84 → 1574.38] And we're going to have the third iteration of this year in November.
[1574.54 → 1575.62] So still some time.
[1576.02 → 1578.34] But hopefully listeners will make a mental note.
[1578.34 → 1588.58] Well, there are also good teaching tutorials out there, many blog posts, online courses that you can sign up to books like the Book of Why by Judea Pearl.
[1588.74 → 1594.98] Maybe not really a textbook, but really drives home the idea of why causal inference is so important.
[1595.18 → 1601.06] It has really nice historical anecdotes because Judas is really a giant in this field.
[1601.62 → 1604.00] Causal Inference, the mixtape by Scott Cunningham.
[1604.00 → 1609.40] If you have more of an econ background, perhaps the effect by Nick Huntington-Klein.
[1609.46 → 1612.86] So these are all beginner-friendly textbooks that you can pick up.
[1613.52 → 1617.82] And then trying out the different packages like do why in Python, for example.
[1618.42 → 1622.86] There's the startup called Geminis that is developing causal inference software.
[1622.86 → 1633.76] And they're having free trial versions where you can start out drawing your directed acyclic graphs and see how answers change if you change assumptions, for example.
[1634.16 → 1637.92] So I think that is usually the best way to learn and pick this up.
[1637.92 → 1663.30] Well, Paul, I'm selfishly going to present you maybe with a scenario and do some sort of on-the-fly problem-solving.
[1663.30 → 1671.22] I figure you're probably good at that, being a professor and always solving problems with students and others and colleagues.
[1671.72 → 1674.80] So I mentioned my wife runs a business.
[1675.14 → 1676.90] It's a candle manufacturing business.
[1677.48 → 1683.28] And there's actually this sort of like why question that we've been talking about a little bit.
[1683.64 → 1686.40] So last year, to give context, I just logged into Shopify.
[1686.40 → 1692.56] So last year, they had 87,837 orders.
[1693.32 → 1700.32] Each of those orders, or at least most of them, when they ship them, included a free sample two-ounce candle.
[1700.50 → 1702.14] It's like a freebie add-on.
[1702.80 → 1706.80] And over time, the assumption has always been, oh, people really like that.
[1706.90 → 1709.64] And it's sort of like part of the package that they get.
[1709.78 → 1712.42] It increases reorder value, right?
[1712.42 → 1716.70] Like they see the package, and they're like, oh, cool, I got like a free candle.
[1717.36 → 1721.34] And now I'm going to, I love these people forever, and I'm going to reorder, right?
[1721.64 → 1728.76] Well, the question has come up, obviously, at this scale of orders, that's a lot of free two ounces.
[1729.34 → 1733.66] And even just the savings of those would be huge.
[1733.66 → 1746.34] So how might you, as a practitioner or someone thinking about this problem, both in terms of the experimental or the observational approaches, what might be some ways to dig into this?
[1746.40 → 1753.82] Obviously, it's very expensive to send out like get different packaging and do like an experiment at that scale.
[1753.82 → 1760.66] So it'd be nice to know without doing like a large scale shift in packaging and that sort of thing.
[1760.94 → 1762.02] Any tips for me?
[1762.02 → 1770.24] In this case, the big advantage is that you or your wife, you are actually controlling this process.
[1770.54 → 1775.22] So you decide in which packaging to put the free add-on.
[1776.00 → 1783.26] And in that sense, you immediately understand the selection process or the treatment assignment, how we would call that here.
[1783.88 → 1788.40] And in that situation, I think an experimental approach would be the way to go.
[1788.40 → 1799.12] Then it becomes more of a statistical question like how much your sample or how large your sample needs to be in order to draw robust conclusions, right?
[1799.12 → 1806.16] And if it's just the yes-no questions about a free sample or not, the experiment can probably be quite small.
[1806.30 → 1809.80] That relates a little bit to the COVID example that I discussed earlier.
[1809.80 → 1822.18] Probably you want to broaden that up and think about, for example, heterogeneous treatment effects in the sense that, well, is it high volume customers that like this free add-on most?
[1822.36 → 1825.36] Or is it more like the casual shoppers, right?
[1825.36 → 1833.02] And suddenly you have four groups that you're catering to because, well, high volume, low volume, and treatment and control.
[1833.40 → 1836.62] These are problems that always come up in causal inference.
[1837.22 → 1842.18] So the tools like causal random forest developed exactly for that problem.
[1842.18 → 1850.40] How do you efficiently partition the population in order to reduce costs associated with an experiment, right?
[1850.44 → 1855.98] You want to be as cost-efficient as possible, but also still get robust conclusions out.
[1856.50 → 1862.16] A similar problem arises then of, I mentioned earlier, robustness of findings, right?
[1862.38 → 1865.56] So transfer learning is a big topic in AI.
[1865.56 → 1875.08] So maybe let's assume you've done this experiment at this point in time, and you found that robust treatment effect, right?
[1875.20 → 1876.80] Like, so people react to it.
[1876.86 → 1878.46] It increases reorder value.
[1878.66 → 1886.66] The question is then in six months from now, will the world have changed, or will these results still be valid, right?
[1886.72 → 1892.36] And maybe you're thinking about that in six months, not so much has changed of the business, right?
[1892.36 → 1905.06] But for example, platforms like booking.com, right, hotel bookings for them is very relevant because you have people that book hotels in the summer for leisure travel are very different from business travel, for example.
[1905.18 → 1907.24] So you have this kind of problem.
[1907.50 → 1912.08] Can you transfer causal knowledge that you've obtained to a different domain?
[1912.14 → 1915.38] Because that would save you on experimentation costs, for example.
[1915.38 → 1923.28] So yeah, also it's an interesting question in that domain, but the big advantage is you can actually run experiments here.
[1923.52 → 1936.68] Like in other domains, we are reliant on data where people self-select into something like, for example, the standard question about in economics, about, for example, the returns to college education, right?
[1936.80 → 1941.16] There we could not randomly assign people to colleges, right?
[1941.20 → 1943.00] Or whether they can go to college or not.
[1943.00 → 1947.84] There we have to rely on them self-selecting into a sort of treatment and control book.
[1948.20 → 1955.12] And then it's always the question of where we have really an apples to apples comparison or is it perhaps an apple to oranges?
[1955.50 → 1965.62] I just wanted to say I think you're lucky that you got Daniel's example question because coming from my industry, I would have had to ask, like, I don't know, hypersonic missile design or something.
[1965.82 → 1966.94] And I don't think we want to go there.
[1966.94 → 1969.54] This is a great thing about the podcast, right?
[1969.62 → 1975.82] We get to have, like, the expert on, and I get to selfishly ask that helps me in my day, day to day.
[1976.36 → 1976.38] So.
[1977.64 → 1979.78] Excellent way of getting some free consulting in there.
[1979.90 → 1980.10] Yeah.
[1980.10 → 1985.72] So I wanted to actually take you back to something that you mentioned a little while ago.
[1985.88 → 1998.62] We were kind of talking about the benefits of causal inference, and you brought up reinforcement learning, but we were generally talking about kind of fairness, bias, robustness, the impact of causal on those.
[1998.62 → 2003.12] Could you kind of go back to that point and kind of talk a little bit about what that means?
[2003.54 → 2008.44] You know, these are huge topics that are in all the different branches of AI right now.
[2008.54 → 2011.68] And it's on everyone's mind, especially with all the advances this year.
[2011.84 → 2021.88] How does causal affect that worldview of doing these amazing things in these different branches of AI, but doing it without bias, doing it fairly such as that?
[2021.88 → 2031.68] I'll start with fairness because that's actually the very first example that I use in my own course, causality, causal inference course here at Copenhagen Business School.
[2032.10 → 2034.68] It's a case taken from Google, actually.
[2034.98 → 2036.70] So a while ago, I think in 2019.
[2037.46 → 2043.50] Well, already earlier, the story goes longer, but they have been accused of underpaying women in their organization, right?
[2043.52 → 2049.76] So there we have a classic example of like a protected attribute like gender, race, and so forth.
[2049.76 → 2056.86] And we want to prevent bias in some form of automated or semi-automated decision-making, right?
[2056.88 → 2058.30] And that comes up all the time.
[2058.38 → 2062.88] I mean, in loan acceptance models, for example, we want to remove bias and so forth.
[2063.06 → 2068.12] So to make the story quick is they have been accused of underpaying women in their organization.
[2068.12 → 2073.18] Then they did a fairly sophisticated analysis, published a white paper.
[2073.50 → 2078.44] And the result was of that analysis that they found that they're actually underpaying men.
[2078.44 → 2079.96] At least they thought so.
[2080.48 → 2086.08] And not only men, but actually high-level software engineers, so high-seniority software engineers at Google.
[2086.74 → 2095.82] And then because they're committed to fairness in their organization, they actually raised salary levels for these high-level software engineers based on analysis.
[2096.04 → 2100.22] So it also had a practical component to it or like a policy implication.
[2100.22 → 2103.04] We cannot analyze this case here in detail.
[2103.20 → 2110.82] But if you do that analysis, it's very likely that they actually did a sort of fairly common causal inference mistake.
[2110.98 → 2118.58] So they conditioned on some variables that are downstream of so that are affected by gender, like occupation, for example, right?
[2118.58 → 2131.50] And then if you have discrimination already at that stage, that, for example, women don't have it so easy to get into high-level positions for various reasons that we know of, then that will be a classic mistake.
[2131.62 → 2137.48] And you can produce this kind of, again, nonsensical correlations in the end, like the sharks and the ice cream.
[2137.48 → 2144.62] That's one example that you can actually easily transport to other kinds of questions, like I mentioned algorithmic bias.
[2145.18 → 2154.64] And that's a causal question, because if you don't understand how variables in your model causally interact and relate to each other, you cannot answer this question.
[2154.94 → 2157.68] You cannot decide how to correctly analyze the data.
[2158.76 → 2167.34] Robustness, I mentioned, so the transportability transfer learning kind of aspect of experimental knowledge and their causal inference techniques have been developed.
[2167.48 → 2187.60] Also dealing with selection bias in data, so a data set that might not be a representative sample of the population that you care about, but is measured with some form of selection bias, because only happy customers answer your consumer survey or unhappy customers, but no one in between, right, for these questions.
[2188.18 → 2190.24] And then lastly, explainability.
[2190.48 → 2193.98] I think explainability almost comes for free with causal inference.
[2193.98 → 2202.66] I mean, don't get me wrong, causal inference is a hard task, but once you solve it, explainability almost comes for free, because, well, I mentioned the book of wine, right?
[2203.10 → 2208.32] So causal questions are always related to why questions, counterfactual as well, right?
[2208.36 → 2211.36] Like, why did my headache go away?
[2211.46 → 2213.54] Was it because I took the aspirin this morning?
[2213.78 → 2215.16] I mentioned this example.
[2215.56 → 2216.98] This is the way we reason.
[2216.98 → 2220.78] This is the way we explain, for example, things to other humans.
[2221.40 → 2224.62] And so there's an immediate connection to explainability.
[2225.10 → 2228.20] That's a really great way to think about this.
[2228.34 → 2235.96] And it gets me thinking, like, what will be the impacts of these two fields as they interact more over the coming years?
[2235.96 → 2247.44] And I'm wondering, from your perspective, because you're so plugged into the research that's going on in this area, but also the practical side of this and how data scientists are beginning to use these techniques.
[2247.44 → 2262.10] What, as you look forward to the next, let's say, year or whatever time period you want to have there, like, what gets you excited or what trends would you like to highlight that maybe people should be thinking about in this field?
[2262.10 → 2269.88] Or maybe it's just things that you're excited about in terms of new opportunities or new methods or whatever it might be.
[2269.88 → 2278.44] Yeah, I just attended a conference last week in Tübingen, Germany, the Causal Learning and Reasoning Conference.
[2278.44 → 2283.84] And it was just exciting to see how many young minds there were attending the conference.
[2283.84 → 2291.50] So it was a very young audience, a lot of grad students in computer science specifically there, and a bunch of seniors as well.
[2291.50 → 2301.68] But that really showed me that this seems to be the next big thing in AI, and people have confirmed that to us, that there's more and more interest in the academic side.
[2301.68 → 2306.30] But we also see that in practice in the industry.
[2307.06 → 2312.76] Yeah, so I'm excited about, well, experimental design, what I mentioned earlier, right?
[2312.76 → 2322.60] And heterogeneous treatment effects, for example, not only being satisfied with having one average treatment effect or average causal effect, right?
[2322.60 → 2330.12] One number, and this is what we're expecting, but actually making this more fine-grained and opening up, answering questions like,
[2330.24 → 2334.30] is it all people, young people that benefit more from vaccines?
[2334.56 → 2337.64] In which way do we need to roll that out in the most effective way?
[2337.64 → 2350.86] Then on the observational side, I think causal discovery is really promising, and this is really the idea of how far can we go with just simply trying to get out causality from observational data?
[2351.16 → 2352.68] And we will never get 100%.
[2352.68 → 2354.76] I mentioned that, but how far can we go?
[2355.28 → 2360.98] So one big challenge in that area is, for example, to have good benchmarking data sets, right?
[2361.06 → 2362.74] In machine learning, that's usually easy.
[2362.74 → 2366.60] You divide a sample up into a training and benchmarking data set.
[2367.04 → 2368.56] With causality, that's not so easy.
[2368.66 → 2371.58] You often need an experimental benchmark, for example.
[2372.18 → 2378.14] A lot of work has been done in genomic research where you can knock off genes, for example, in an experimental way.
[2378.22 → 2379.28] So that is really exciting.
[2380.02 → 2384.92] There's new work on causal root cause analysis by Amazon, for example.
[2385.08 → 2390.74] So figuring out what are the causes of actually outliers, even in an engineering system.
[2390.74 → 2393.56] So you mentioned, Chris, that you're working in that area.
[2393.78 → 2400.12] So I've seen, for example, companies in the defence industry thinking about this problem of root cause analysis.
[2400.76 → 2409.86] Lastly, perhaps, because originally, before I came to causal inference, I was actually trained in economics, like I mentioned, but specifically innovation economics.
[2410.04 → 2412.96] So this idea of how do we produce knowledge as a society?
[2413.14 → 2415.56] How does knowledge spread across a society?
[2415.56 → 2422.70] And so in causal inference, there are new lines of work thinking about actually interactions between treatments.
[2422.70 → 2432.42] So not just the idea that I take a pill and I get an outcome from that, but it's like you take a pill and that reduces the viral load in our community.
[2432.42 → 2436.46] And that's why I actually have a lower likelihood to get sick, for example.
[2436.46 → 2445.62] So this kind of interactions between people are really important, I think, in many domains and specifically also in the way knowledge spreads across networks.
[2445.82 → 2447.90] So that is something I'm really exciting about.
[2448.26 → 2448.82] Awesome.
[2449.12 → 2465.52] Well, I am really, really happy that we got to have this conversation on the podcast because I think it highlights something that's a real complement to many of the things that people are exploring around deep learning and large language models and other things.
[2465.52 → 2472.62] This is a really important piece of the sort of practical side of what data scientists are doing in the enterprise.
[2472.84 → 2474.30] So, yeah, thank you so much.
[2474.42 → 2478.56] And thank you for your research on the topic and also engaging the community around this.
[2478.64 → 2481.96] It's really great and really happy to have had you on the podcast.
[2482.82 → 2483.06] Thank you.
[2483.14 → 2484.26] I really enjoyed the conversation.
[2484.26 → 2495.74] Thank you for listening to Practical AI.
[2496.22 → 2500.06] Your next step is to subscribe now, if you haven't already.
[2500.50 → 2506.54] And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2506.54 → 2511.92] Thanks once again to Vastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2512.50 → 2516.28] Check out what they're up to at Fastly.com and Fly.io.
[2516.58 → 2522.00] And to our Beat Freakin' Residence, Break master Cylinder, for continuously cranking out the best beats in the biz.
[2522.30 → 2523.20] That's all for now.
[2523.50 → 2524.60] We'll talk to you again next time.
[2524.60 → 2537.64] We'll be right back.
[2551.80 → 2552.22] We'll be right back.
[2552.28 → 2552.98] We'll be right back.
[2553.00 → 2553.36] We'll be right back.
[2553.36 → 2553.66] We'll be right back.
[2553.66 → 2554.14] We'll be right back.
[2554.14 → 2554.20] We'll be right back.
