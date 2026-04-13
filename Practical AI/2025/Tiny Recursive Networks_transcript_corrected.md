[0.00 → 8.74] Welcome to the Practical AI Podcast, where we break down the real-world applications
[8.74 → 13.64] of artificial intelligence and how it's shaping the way we live, work, and create.
[13.88 → 19.14] Our goal is to help make AI technology practical, productive, and accessible to everyone.
[19.48 → 23.54] Whether you're a developer, business leader, or just curious about the tech behind the
[23.54 → 25.12] buzz, you're in the right place.
[25.12 → 29.84] Be sure to connect with us on LinkedIn, X, or Blue Sky to stay up to date with episode
[29.84 → 33.02] drops, behind-the-scenes content, and AI insights.
[33.36 → 35.88] You can learn more at practicalai.fm.
[36.20 → 37.50] Now, on to the show.
[39.66 → 44.34] Well, friends, it is time to let go of the old way of exploring your data.
[44.62 → 45.52] It's holding you back.
[45.88 → 47.88] But what exactly is the old way?
[48.20 → 53.54] Well, I'm here with Mark Duppy, co-founder and CEO of FBI, a collaborative analytics platform
[53.54 → 55.16] designed to help be explorers like yourself.
[55.60 → 57.46] So, Mark, tell me about this old way.
[57.46 → 62.88] So, the old way, Adam, if you're a product manager or a founder, and you're trying to
[62.88 → 67.14] get insights from your data, you're wrestling with your Postgres instance or Snowflake or
[67.14 → 68.24] your spreadsheets.
[68.46 → 72.40] Or if you are, and you don't maybe even have the support of a data analyst or data scientist
[72.40 → 73.98] to help you with that word.
[74.14 → 79.82] Or if you are, for example, a data scientist or engineer or analyst, you're wrestling with
[79.82 → 85.84] a bunch of different tools, local Jupyter Notebooks, Google Cola, or even your legacy BI to try to build
[85.84 → 89.08] these dashboards that someone may or may not go and look at.
[89.60 → 95.24] And in this new way that we're building at FBI, we are creating this all-in-one environment where
[95.24 → 100.26] product managers and founders can very quickly go and explore data regardless of where it is.
[100.38 → 101.26] So, it can be in a spreadsheet.
[101.42 → 102.16] It can be in Airtable.
[102.28 → 103.48] It can be in Postgres, Snowflake.
[103.80 → 109.02] Really easy to do everything from an ad hoc analysis to much more advanced analysis if, again,
[109.16 → 110.14] you're more experienced.
[110.14 → 116.88] So, with Python built-in right there in our AI assistant, you can move very quickly through
[116.88 → 117.70] advanced analysis.
[118.30 → 123.66] And a really cool part is that you can go from ad hoc analysis and data science to publishing
[123.66 → 130.08] these as interactive data apps and dashboards, or better yet, at delivering insights as automated
[130.08 → 135.88] workflows to meet your stakeholders where they are in, say, Slack or email or spreadsheets.
[135.88 → 139.56] So, if this is something that you're experiencing, if you're a founder or a product manager trying
[139.56 → 144.26] to get more from your data or for your data team today, you're just underwater and feel
[144.26 → 148.34] like you're wrestling with your legacy BI tools and notebooks, come check out the new
[148.34 → 149.40] way and come try out FBI.
[149.76 → 150.28] There you go.
[150.42 → 153.76] Well, friends, if you're trying to get more insights from your data, stop resting with it.
[154.10 → 156.70] Start exploring it the new way with FBI.
[157.02 → 160.00] Learn more and get started for free at Fabi.ai.
[160.26 → 163.30] That's F-A-B-I dot A-I.
[163.30 → 165.58] Again, Fabi.ai.
[165.88 → 185.52] Welcome to another fully connected episode of the Practical AI Podcast.
[185.52 → 188.18] This is Daniel Whiten ack.
[188.30 → 194.78] I am CEO at Prediction Guard, and I'm joined as always by Chris Benson, who is a principal
[194.78 → 197.30] AI research engineer at Lockheed Martin.
[197.74 → 204.06] And in these episodes where it's just Chris and me, we like to dive into certain topics
[204.06 → 211.48] that are trending in AI news and, you know, help both us, and you hopefully level up your
[211.48 → 213.20] AI and machine learning game.
[213.88 → 214.92] How are you doing, Chris?
[214.98 → 220.98] It's good to be back to one of these episodes with just the two of us and maybe explore a
[220.98 → 222.74] topic that we can both learn about.
[222.74 → 223.26] Absolutely.
[223.94 → 224.22] Yeah.
[224.22 → 228.62] I love these episodes of us just kind of bantering whatever we happen to want to do.
[228.76 → 233.64] I love the guest episodes too, but it's kind of a different beast in that way of exploring
[233.64 → 236.34] what some person or organization is doing.
[236.80 → 239.94] And there are so many cool things that we can just dive into.
[240.46 → 242.76] And I think we have a few this week.
[242.76 → 243.70] Yeah, yeah.
[243.80 → 252.76] At least a first very, very tiny topic to discuss, which I was actually one of our engineers
[252.76 → 254.16] brought this up to me.
[254.62 → 262.06] I forget it was earlier in the week, but this idea of tiny recursive networks, you know, all
[262.06 → 267.90] the time we're talking about transformer based LLMs on the show and generative AI.
[267.90 → 276.34] And I kind of personally always love getting back to a little bit of cool data science and
[276.34 → 283.00] research stuff just to see like where the industry is headed, because this is a kind of different
[283.00 → 291.10] animal that we'll be talking about this tiny recursive networks or models and operates differently
[291.10 → 294.50] than kind of the hype gen AI models of today.
[294.50 → 298.20] And it does make me think, and I don't know if this is something you've been thinking about,
[298.30 → 302.08] Chris, but kind of we're all the time talking about gen AI.
[302.36 → 303.56] We're talking about LLMs.
[303.66 → 309.26] Now we're talking about agents, all of those being driven by this transformer based LLMs.
[309.38 → 314.92] And certainly people have talked, you know, prominent people have talked about the fact that we
[314.92 → 318.16] need to get beyond transformer based LLMs.
[318.16 → 324.74] And of course, there are many companies that are just centred around these types of models.
[324.98 → 333.00] So any thoughts on that of, you know, your own predictions or thoughts of when we're kind
[333.00 → 341.74] of headed to the next phase of what models will look like beyond just transformer based LLMs?
[342.02 → 342.18] Yeah.
[342.18 → 347.24] I mean, I think I'm going to sound like a broken record on this because it's not new for me.
[347.40 → 349.64] And that is, you know, I agree with you.
[349.78 → 354.66] We're always, you know, the hot things that the media tends to follow in general are the
[354.66 → 355.54] big LLMs.
[356.04 → 360.22] But, you know, because I guess it's, you know, it's the next giant thing.
[360.30 → 363.00] It's sexy, you know, to talk about.
[363.00 → 368.34] But like the world is, you know, all these technologies are moving from the cloud out
[368.34 → 373.88] into the world into physical AI, you know, and robotics and all sorts of ways that we
[373.88 → 379.40] interact with, you know, not just LLMs, but all sorts of models out there in the world to
[379.40 → 383.48] where, you know, every one of our lives is touched in so many different ways.
[383.74 → 389.52] And that's exactly, you know, as we were diving into this here, this topic with the tiny
[389.52 → 393.20] recursive networks, that's that's what it seems like to me.
[393.76 → 397.22] I'm looking forward to talking about that, because as I mentioned to you right before
[397.22 → 402.80] the show started, you could see these popping up everywhere, like in all sorts of different
[402.80 → 403.42] use cases.
[403.92 → 404.02] Yeah.
[404.10 → 411.44] And I just to set the stage why this is maybe intriguing, there was a paper that that came
[411.44 → 415.16] out less is more recursive reasoning with tiny networks.
[415.16 → 420.28] This came out from Samsung's AI lab in Montreal.
[420.58 → 426.70] Specifically, there's an author, Alexia, on this article, which if you're out there listening,
[426.92 → 429.02] we would love to have you on the show.
[429.22 → 431.78] Please come join us and talk more about this.
[431.90 → 436.76] Hopefully we won't butcher this work too bad as we talk about it.
[437.06 → 442.60] You'll hear Chris and I kind of learning as we go on this episode, as we talk back and
[442.60 → 444.18] forth about what this exactly is.
[444.18 → 449.36] But this is, you know, the paper is less is more cursive reasoning with tiny networks.
[449.36 → 456.34] And I think the major thing that's interesting here is there's a model that they talk about
[456.34 → 462.66] that has only 7 million parameters, which is tiny.
[462.96 → 464.62] If I yeah, yeah.
[464.62 → 467.90] So like, I just want to sort of let that sink in.
[468.00 → 477.82] So I didn't say 7 billion parameters, 7 million parameters with an M, which, yeah, Chris, if is as we've
[477.82 → 485.26] basically gone about this trend, I mean, actually, a 7 billion parameter model now is quite small.
[485.26 → 485.90] Yes.
[486.24 → 492.78] And in a sense, 27 million compared to what we traditionally call very small at the 7 billion
[492.78 → 493.22] level.
[493.78 → 497.20] I mean, this is that, you know, it's using the word tiny for a reason.
[497.42 → 498.46] But yeah, it does.
[498.68 → 503.84] You know, when you think of millions as being almost nothing, it's its an interesting
[503.84 → 504.88] context shift there.
[505.38 → 505.58] Yeah.
[505.58 → 505.62] Yeah.
[505.74 → 505.94] Yeah.
[505.94 → 512.28] So I actually love this because I love the idea that we could move into a phase where
[512.28 → 519.02] we're dealing with models that are very small, can run on commodity hardware, at least
[519.02 → 520.36] be smaller.
[521.08 → 525.92] And, you know, they may run for longer periods of time or there may need to be optimization
[525.92 → 527.74] around how they run recursively.
[527.84 → 531.62] We'll get into that recursive bit, but certainly a small model.
[531.62 → 538.98] But it was shown to kind of have, let's say, comparable or on par performance with
[538.98 → 539.82] some of the big guys.
[539.82 → 544.18] So we're talking like DeepSeek R1, Gemini 2.5 Pro.
[544.48 → 550.96] These are billions and billions of parameters models, very, very huge transformer based LLMs,
[551.08 → 554.14] this kind of reasoning models that we've talked about on the show.
[554.26 → 561.16] And in the centre of this work is really kind of related to these reasoning tasks.
[561.16 → 568.38] Now, right out of the bat, I think it would be worth saying that these it's not like this
[568.38 → 575.18] tiny recursive network is a general purpose model that can do whatever you want it to
[575.18 → 575.56] do.
[575.78 → 580.52] It was trained for a very kind of small number of tasks.
[580.82 → 587.18] But these were reasoning tasks that some of these other models like a DeepSeek R1 or
[587.18 → 591.46] something sometimes has quite a bit of issue with.
[591.74 → 596.12] So solving like math or Sudoku type of puzzles.
[596.28 → 602.06] And I know, Chris, we had talked to, I don't know if you want to refresh some of your Sudoku
[602.06 → 602.72] experiments.
[603.18 → 608.28] But yeah, well, what you're referring to is some episodes back, I'd have to look up and
[608.28 → 609.36] figure out where it was.
[609.36 → 619.00] I was playing with GPT-4 at the time on Sudoku, and it was just doing a terrible job on Sudoku
[619.00 → 625.46] and giving it, you know, a lot of just terrible output in terms of, I mean, honestly,
[625.62 → 626.22] crappy answers.
[626.86 → 632.62] And so that was really the first thing I noticed on this thing was the fact that, because they
[632.62 → 637.94] call out Sudoku as being one of the things, is that these tiny models being trained for
[637.94 → 644.80] very specific tasks, and that it could potentially outperform these large models on specific things
[644.80 → 647.70] like Sudoku being one example, and others as well.
[648.10 → 654.38] But I think in a slightly larger sense, this is much more real world applicable the way
[654.38 → 660.02] I see it in that as we have models spreading across the world for lots of different tasks,
[660.10 → 661.04] this is perfect for that.
[661.18 → 665.08] It's not one model to rule them all in most real life situations.
[665.08 → 670.76] It's really a collection of very specific models that each does a task very, very well
[670.76 → 672.54] and is efficient at that.
[672.72 → 675.78] And I think this is a great example of that.
[676.34 → 676.68] Well put.
[676.78 → 682.10] And it's probably worth reminding ourselves about, like, as we highlight the differences
[682.10 → 684.94] with this model, reminding ourselves about transformers.
[684.94 → 695.26] So, you know, as we've gone through the process from deep learning to recurrent neural networks
[695.26 → 702.42] and transformer-based self-attention networks, if you imagine what we have with these big
[702.42 → 709.68] LLMs, what happens is you put in a sequence of tokens, which are represented by numbers.
[709.68 → 715.40] You put in a sequence of tokens that are represented by numbers, these tokens being kind of words
[715.40 → 716.20] or subwords.
[717.18 → 726.42] And all of those tokens are processed in a forward pass through a giant set of, if you want to
[726.42 → 734.52] think about it, like sub functions, which add and multiply and combine those numbers through
[734.52 → 743.96] a very vast network of functions to generate many different probabilities of kind of next
[743.96 → 751.44] words coming out, which allow you to predict kind of a completion of words or a reasoning,
[751.64 → 755.12] a set of reasoning or a set of thinking or a solution to a problem, right?
[755.24 → 757.76] This is how these networks work.
[757.76 → 763.12] And I would recommend people, we've had Jay Palomar on the show before.
[763.28 → 767.98] He has some great kind of the illustrated transformer blog posts.
[768.30 → 769.74] So Jay, shout out to you.
[769.82 → 770.60] Thanks for doing that.
[770.88 → 773.02] I would take a look at those blog posts.
[773.12 → 777.48] They do a great job at explaining this more visually for those where that would be helpful.
[777.62 → 784.08] But the main kind of thing here that I'm saying is in the models that we're using now,
[784.08 → 788.60] basically, it's a giant function, if you want to think about it that way.
[788.68 → 789.78] It's a data transformation.
[790.12 → 796.68] You put something in one end, it processes through one way, through the function, and
[796.68 → 798.56] produces a result.
[799.00 → 804.30] Now, you may run that function multiple times to produce multiple words out the other end,
[804.34 → 808.86] which is what happens when you stream output into like a chat interface.
[808.86 → 815.06] But ultimately, each time the model runs, it's a single run through the model input.
[815.26 → 817.44] It's transformed to some output.
[817.80 → 824.12] That is not recursive, as we would say, with these models.
[825.34 → 834.66] And if you want to think about it, it requires very, very large models because what you're modelling
[834.66 → 837.18] is a very complicated data transformation.
[837.18 → 844.22] So for you to put in some text related to a math problem and predict the right wording
[844.22 → 851.24] of a solution out the other end, that's actually a very non-trivial data transformation, right?
[851.26 → 857.80] Which means you have to have a very large function to kind of fit or model that data transformation,
[857.80 → 861.82] which is why these models have become so large.
[861.82 → 869.98] So now with this tiny recursive setup, what's happening is you're not just looking at the
[869.98 → 879.46] model as a single forward pass data transformation, but you introduce the idea of recursion, which
[879.46 → 883.04] means you sort of output from the model.
[883.04 → 891.52] And that output becomes the input for the same model, which creates this kind of circle or
[891.52 → 895.76] recursion, which is kind of interesting.
[896.40 → 903.94] So you're essentially trading what would be a very large function to model that data transformation
[903.94 → 913.28] for many, many kind of recursive runs of a single, very small model.
[913.54 → 916.78] That's maybe a simplified way to put it.
[916.80 → 919.58] And we can get a little bit more into the model itself here in a second.
[919.58 → 924.70] So I have a question for you on this is one of the things when I was mentioning the 27 million
[924.70 → 930.68] earlier, I was talking about the hierarchical reasoning model, which is a previous model put
[930.68 → 934.82] out there versus the tiny ones, which have the five to 7 million parameters.
[935.40 → 939.00] Can you talk a little bit about like, are they completely different things?
[939.20 → 942.94] Is the tiny a outshoot of the hierarchical?
[943.04 → 944.70] How do you how do you compare those two?
[945.10 → 946.78] Yeah, good, good point.
[946.90 → 951.86] So just like everything we talk about on this show, sometimes it does seem like things pop
[951.86 → 955.20] out of thin air, like tiny recursive models now.
[955.20 → 964.60] But in reality, there is a buildup of incremental research that that leads to new technology or
[964.60 → 965.32] new findings.
[966.18 → 970.82] One of the things in that kind of lead up to these tiny recursive models was a previous
[970.82 → 974.24] work around hierarchical reasoning models.
[975.12 → 978.00] And these also were smaller.
[978.24 → 984.10] Like you're saying, you know, 27 million parameters is still very small in today's standards for
[984.10 → 985.32] models, at least.
[985.96 → 994.68] But these hierarchical models actually use two very small transformer networks, four
[994.68 → 1000.86] layers each, and they recurred to each between each other.
[1000.86 → 1006.86] So I don't have the full details of that and wouldn't be able to explain it if I did, probably.
[1007.46 → 1013.30] But that's the main idea is these hierarchical reasoning models have these two models that
[1013.30 → 1019.36] required two networks, two forward passes per step and created some, I guess, complications
[1019.36 → 1020.64] because of that.
[1020.64 → 1029.92] So this introduction by Alexia and the Samsung team here is a single network.
[1030.08 → 1035.04] So it's it uses one tiny network with two layers.
[1035.04 → 1043.18] So a single tiny network with two layers that roughly has kind of five to seven million parameters.
[1043.38 → 1047.92] And it operates kind of in this record recursive refinement.
[1048.98 → 1053.14] So it recourses on itself, if you will.
[1053.14 → 1059.26] And the hierarchical reasoning model with the 27 million parameters, for example, on the Sudoku
[1059.26 → 1062.48] extreme benchmark scored a 55 percent.
[1062.62 → 1069.98] I don't know the exact kind of way that that's scored, but just by kind of comparison, the tiny
[1069.98 → 1076.30] recursive network, which is even tinier when training on a thousand examples was able to
[1076.30 → 1080.38] achieve 87 percent accuracy on Sudoku extreme.
[1083.14 → 1087.88] Well, friends, you don't have to be an A.I.
[1087.96 → 1089.40] expert to build something great with it.
[1089.60 → 1091.42] The reality is A.I. is here.
[1091.70 → 1094.62] And for a lot of teams, that brings uncertainty.
[1095.14 → 1099.52] And our friends at Miró recently surveyed over 8000 knowledge workers.
[1100.10 → 1102.22] And while 76 percent believe A.I.
[1102.28 → 1108.38] can improve their role, most, more than half, still aren't sure when to use it.
[1108.62 → 1111.42] That is the exact gap that Miró is filling.
[1111.42 → 1116.20] And I've been using Miró from mapping out episode ideas to building out an entire new thesis.
[1116.84 → 1119.74] It's become one of the things I use to build out a creative engine.
[1119.98 → 1123.32] And now with Miró A.I. built in, it's even faster.
[1123.66 → 1129.92] We've turned brainstorms into structured plans, screenshots into wireframes and sticky notes,
[1130.42 → 1133.98] chaos into clarity, all on the same canvas.
[1133.98 → 1138.02] Now, you don't have to master prompts or add one more A.I.
[1138.08 → 1138.98] tool to your stack.
[1139.12 → 1141.38] The work you're already doing is the prompt.
[1141.78 → 1144.44] You can help your teams get great done with Miró.
[1144.72 → 1146.66] Check out Miro.com and find out how.
[1147.02 → 1150.64] That is Miro.com, M-I-R-O.com.
[1150.64 → 1161.88] So, Chris, just to kind of drive, I guess, the point home here with these tiny recursive
[1161.88 → 1166.60] networks, you have this single tiny network.
[1166.60 → 1175.00] And you are essentially replacing, if you want to imagine a big kind of pipeline of processing,
[1175.26 → 1181.00] which is what these big LLMs are, and you go one pass through the whole pipeline of processing.
[1181.30 → 1183.04] Here, the pipeline is smaller.
[1183.22 → 1186.66] You've got fewer layers, fewer parameters.
[1187.06 → 1191.10] But you replace that kind of depth with iteration.
[1191.10 → 1198.78] So, instead of stacking those transformer blocks, you repeat the network over and over,
[1198.90 → 1207.82] essentially to kind of refine its reasoning state or the solution guess, right?
[1208.18 → 1214.46] And so, this iterative refinement, one of the things also is it kind of helps avoid overfitting
[1214.46 → 1221.36] on small data sets, which, to your point, Chris, earlier about real world business cases,
[1221.72 → 1229.24] often the reality is that you kind of don't have, you have scarcity of data for very many
[1229.24 → 1229.84] problems.
[1230.38 → 1236.94] You don't often have a really nice kind of large millions and millions of things to train
[1236.94 → 1237.62] on, right?
[1237.70 → 1237.82] Yeah.
[1237.98 → 1243.10] You know, and I think that's one of the most fascinating things about this is in the paper,
[1243.10 → 1249.06] they talk about the fact that they're achieving this higher accuracy on hard puzzle benchmarks
[1249.06 → 1252.88] while training on only approximately 1,000 examples.
[1253.90 → 1260.74] And that, when you think about, you know, the challenge of having a great data set in the
[1260.74 → 1265.96] more traditional context that we've been talking about, and that becomes such a challenge for
[1265.96 → 1268.12] many people and organizations to do that.
[1268.12 → 1272.60] But it's a lot easier to get 1,000, you know, 1,000 examples together.
[1273.22 → 1280.34] And it puts, you know, not only from the computational side, but also from the data set side, puts this
[1280.34 → 1286.04] much more in reach for a lot of problems that people may have, where they do want to solve
[1286.04 → 1289.48] a narrow concern with high accuracy.
[1289.48 → 1297.56] And so I see this as it's kind of the every person's way of modelling in terms of tackling
[1297.56 → 1301.96] things going forward without a lot of resources and a lot of maybe not a lot of time to put
[1301.96 → 1302.50] things together.
[1302.50 → 1304.06] You could probably do it pretty quickly.
[1304.76 → 1304.86] Yeah.
[1305.04 → 1306.04] Yeah, exactly.
[1306.26 → 1315.18] And I guess just to kind of put some of the boundaries that are currently around these
[1315.18 → 1320.50] recursive models, one of the things I was trying to parse through as I looked at this was,
[1321.04 → 1323.30] well, what is the setup now?
[1323.76 → 1325.22] How general is the output?
[1325.54 → 1330.24] How kind of general can the output or the input and the output be?
[1330.24 → 1341.42] And part of the trick here, you know, it's not a trick, but part of the setup is that these
[1341.42 → 1349.30] tiny recursive networks, they don't take a kind of unstructured, you know, natural language
[1349.30 → 1350.24] text input.
[1350.44 → 1356.06] They take some structured representation of a whole problem at once.
[1356.06 → 1362.78] So you can think of a puzzle grid in Sudoku or a math, you know, word problem turned into
[1362.78 → 1371.46] structured features or a reasoning question encoded by numbers or symbols or logic, something
[1371.46 → 1372.30] like that.
[1372.38 → 1378.18] So instead of feeding in the input kind of word by word, like a chatbot, you're giving
[1378.18 → 1382.20] a situation to the model.
[1382.20 → 1387.92] It's kind of a one shot situation, which is then turned into, of course, embeddings internally
[1387.92 → 1392.78] because, you know, computers work on series of numbers, right?
[1392.84 → 1396.24] That's the only thing a computer can process is numbers, right?
[1396.30 → 1403.66] But those numbers, kind of that embedding represents a kind of one shot of a problem, which is interesting
[1403.66 → 1411.44] because, you know, it almost seems flashback like we're kind of coming full circle to reasoning
[1411.44 → 1419.44] problems, but in a more data science-y way than like a generative AI way, which is kind
[1419.44 → 1421.34] of refreshing and cool.
[1421.78 → 1426.74] That was, that's very much what I was about to say in the sense of it feels, this feels
[1426.74 → 1433.20] a lot more like kind of traditional, like the way that you put a problem together in more
[1433.20 → 1437.58] of a traditional software development way where you, you know, you'll create some structures
[1437.58 → 1438.66] and you'll pass them in.
[1438.86 → 1444.10] And when we got to Gen AI, and then it got to prompting, and we're trying to, that was,
[1444.22 → 1448.18] you know, the, the notion of prompting was a little bit different from the way we had
[1448.18 → 1449.18] traditionally put software together.
[1449.18 → 1452.22] This feels a lot more like, okay, I have a problem.
[1452.22 → 1455.84] I have a structured way to put that problem through the function.
[1455.84 → 1460.10] And this is just offering a different way to, uh, to address that problem.
[1460.10 → 1464.86] You know, so you're getting the benefit of the of these, uh, of these models.
[1465.22 → 1470.20] Uh, but for me, like when, when you talked about this, you know, using the Sudoku example
[1470.20 → 1476.38] and structuring that as the grid, that's kind of feels like what we've always done in a
[1476.38 → 1476.98] in a sense.
[1476.98 → 1482.16] So I, I find that fascinating in terms of, uh, integrating that in and looking at some
[1482.16 → 1486.56] of the old problems that we might've been trying to solve for years and, uh, and seeing what
[1486.56 → 1488.70] we can do with this model to do it a little bit better.
[1488.70 → 1489.30] Yeah.
[1489.30 → 1494.16] It's like, uh, looking, looking at things from a different perspective, but, uh, some
[1494.16 → 1501.02] of, some of the way that we used to think about things kind of filtering in, um, and yeah,
[1501.02 → 1506.66] so you have this kind of input, I guess, in terms of people's intuition or mental model
[1506.66 → 1512.24] around this, like you have this input of this whole, whole problem at once, a single shot
[1512.24 → 1515.54] of a whole problem, a puzzle grid or a math problem encoded.
[1515.54 → 1525.32] And what's happening inside is that the tiny recursive network initially produces an initial
[1525.32 → 1526.06] guess, right?
[1526.06 → 1531.50] Like it does a forward pass through its network and generates an initial, you could think about
[1531.50 → 1532.50] it as an initial guess.
[1532.66 → 1538.58] Obviously it's just an a number like a probability, but that's kind of the initial, you could think
[1538.58 → 1543.60] about it like the internal kind of scratch pad of the initial guess.
[1543.76 → 1546.44] It then kind of loops over itself.
[1546.76 → 1553.38] And, you know, it's always difficult to anthropomorphize because things work differently in computers than
[1553.38 → 1554.94] they do in, in our minds.
[1554.94 → 1555.34] Right.
[1555.34 → 1560.96] But in some way, if you want to think about it as that sort of process, that looping is
[1560.96 → 1567.38] kind of refining of that initial scratch pad until your kind of get to this almost like
[1567.38 → 1572.02] self-consistency or, um, or a refined answer.
[1572.18 → 1578.62] And so when the output comes out, it's, it's again, not a stream of words or tokens, but it
[1578.62 → 1580.28] is a complete answer.
[1580.28 → 1585.82] It is the answer to the kind of initial thing, but that answer was arrived at through this
[1585.82 → 1586.84] recursive thing.
[1586.84 → 1591.68] So in the in terms of just some highlighting some differences in the transformer world,
[1591.68 → 1597.62] you put in words or tokens, tiny recursive network, you put in a whole problem as structured
[1597.62 → 1599.84] data transformer world.
[1600.06 → 1605.54] You go a single pass through hundreds of layers, tiny recursive network.
[1605.72 → 1608.72] You repeat the small network recursively.
[1608.72 → 1614.74] In terms of the output in the transformer world, you kind of get these next token probabilities,
[1614.74 → 1619.62] the recursive network, you kind of get one final structured answer.
[1620.58 → 1626.20] And, uh, in terms of analogy, if you want to think about it in the transformer world, it's
[1626.20 → 1632.54] sort of like your free form typing as you think about your answer, right?
[1632.54 → 1638.26] You're just sort of vomiting up your reasoning onto the, onto the screen and typing as, as
[1638.26 → 1639.04] you go along.
[1639.32 → 1643.48] And then the recursive network, it's more like, it's just kind of chugging along.
[1643.48 → 1644.98] It's thinking quietly.
[1645.54 → 1645.98] Right.
[1646.00 → 1648.08] And then boom, there's the answer.
[1648.08 → 1650.28] Like it's a complete answer when it comes out.
[1650.28 → 1653.74] I, I'd be curious, and I don't know if you've seen anything on this.
[1653.80 → 1659.86] I'd be curious, uh, both what, you know, what to expect from training times on with networks
[1659.86 → 1665.22] of this size, which I would expect to be even with the recursion to be pretty fast, but also
[1665.22 → 1667.36] what inference times, uh, might be.
[1667.36 → 1673.98] In other words, if you were to take these, uh, train them, put them into a device where
[1673.98 → 1679.34] you're looking for maybe real time or near real time, uh, inferencing there, uh, is that,
[1679.44 → 1680.22] is that reasonable?
[1680.34 → 1685.16] Have you seen anything yet in, in any of the research that you've read about what that timing
[1685.16 → 1685.76] looks like?
[1685.76 → 1690.58] How is it incredibly screaming fast given the small size despite the recursion?
[1691.12 → 1697.20] So there are a couple of things to kind of parse through here, which is one, we, we've talked
[1697.20 → 1703.30] about this recursion, but the thing is like, how do you know when to stop the recursion?
[1703.30 → 1707.00] And that's part of the part of the answer to your question.
[1707.00 → 1711.70] So you're refining this answer and there are various ways to do that.
[1711.70 → 1717.36] And I remember actually, this is, uh, I guess a deep cut, but I don't get to bring it up very
[1717.36 → 1717.78] often.
[1717.78 → 1724.08] Back in my physics days, I worked on a, on a theory called density functional theory, which
[1724.08 → 1726.48] essentially models out material properties.
[1726.78 → 1729.10] And it was a cell.
[1729.10 → 1733.36] We talked a lot about self-consistency, which is what is happening here.
[1733.36 → 1741.60] So you ran iterations of your model until you arrived at a solution where there sort of
[1741.60 → 1745.32] wasn't, there wasn't that much change in your answer.
[1745.44 → 1747.92] You sort of got to a steady state.
[1747.92 → 1751.58] If you, if you will, there wasn't a change from one iteration to the other.
[1751.58 → 1757.22] So that's one way actually you can run this type of model is with this kind of change threshold.
[1757.48 → 1762.26] The other way is you can just say, well, I'm only going to run it so many recursions,
[1762.68 → 1762.88] right?
[1762.94 → 1767.02] Like X amount of recursions, you know, eight loops or, or whatever.
[1767.30 → 1771.36] Um, that kind of is a nice guarantee, but it doesn't necessarily mean you get to the
[1771.56 → 1772.80] to the good solution.
[1772.80 → 1779.42] Uh, you can also, it could be possible that you could have a second kind of network that
[1779.42 → 1786.42] learns to predict when there's kind of a, uh, a good outcome state.
[1786.56 → 1791.74] So there, there's actually a variety of ways that, that this could, could work.
[1792.30 → 1799.28] Um, now in terms of the in terms of the training time and the inference time, I think there's a
[1799.28 → 1802.06] lot to be learned here.
[1802.24 → 1808.48] So at least in, in, I guess, no pun intended, a lot to be learned, but, uh, even though the
[1808.48 → 1815.32] there's sort of a small network here, it means each kind of training step is cheaper, but the
[1815.32 → 1821.80] training time depends on how many kind of loops they, they need.
[1821.82 → 1829.24] So if, if there's, if there are problems where kind of the examples converge and kind of
[1829.24 → 1831.20] few loops, then the training is much faster.
[1831.82 → 1834.90] And if they still need lots of loops, then it slows down.
[1835.50 → 1842.90] And so the other piece of this is that we've had this entire industrial complex that has
[1842.90 → 1848.32] optimized training frameworks and tooling for big LLMs.
[1848.66 → 1848.84] Right.
[1848.98 → 1855.48] And so actually kind of in this more research environment, I think it has been kind of slower
[1855.48 → 1859.28] to train some of these recursive networks.
[1859.28 → 1864.10] Now I would imagine that's kind of a result of both of those contributing factors.
[1864.66 → 1872.40] But I think if you are looking at the inference time, you could think like, well, these could
[1872.40 → 1876.80] only internally kind of loop for a few loops and then give a full answer.
[1876.92 → 1878.52] That would be very, very fast.
[1878.52 → 1883.46] And, and so, yeah, I think it, it depends on a lot of things.
[1883.46 → 1889.88] I think the transformer architecture could, you know, could end up being a very long and
[1889.88 → 1891.18] expensive training time.
[1891.28 → 1893.22] The recursive network could be much cheaper.
[1893.64 → 1896.40] I think it depends on a lot of these different things.
[1896.40 → 1906.40] And because the tiny recursive network is tiny, it's very possible that it could run on very
[1906.40 → 1908.30] commodity or small hardware.
[1908.98 → 1915.62] But again, that might be dependent on how much recursion is needed in terms of the actual
[1915.62 → 1917.00] speed to a solution.
[1917.28 → 1923.88] Because once you have that transformer, it's just going to generate streams of output and
[1923.88 → 1927.16] can do that fairly fast, depending on what hardware you're running on.
[1927.44 → 1933.14] Whereas this is going to go through its recursion process, which is it's not controlled, and it's
[1933.14 → 1938.96] looking for that threshold might actually vary in terms of speed on the, on the output.
[1938.96 → 1946.30] Yeah, that's with me, very focused personally on kind of that physical AI and getting things
[1946.30 → 1947.76] out on the edge with limited compute.
[1947.98 → 1953.60] That's definitely a concern because I know I have a personal interest here in if it can infer,
[1953.60 → 1958.92] I'm not too worried about the training time, but if it could inference fast enough for real
[1958.92 → 1963.02] time concerns, then it would be a game changer potentially.
[1963.42 → 1967.90] So yeah, definitely interested in, in learning more about this as we go.
[1968.60 → 1968.76] Yeah.
[1968.92 → 1969.18] Yeah.
[1969.18 → 1975.20] I think, I think it's definitely, definitely interesting and will be interesting to see how
[1975.20 → 1977.16] this connects to real world use cases.
[1977.16 → 1994.98] What if AI agents could work together just like developers do?
[1994.98 → 1998.76] That's exactly what agency is making possible.
[1999.28 → 2001.14] Spelled A-G-N-T-C-Y.
[2001.14 → 2006.82] Agency is now an open source collective under the Linux foundation, building the internet
[2006.82 → 2007.96] of agents.
[2007.96 → 2013.16] This is a global collaboration layer where the AI agents can discover each other, connect
[2013.16 → 2017.48] and execute multi-agent workflows across any framework.
[2017.82 → 2023.86] Everything engineers need to build and deploy multi-agent software is now available to anyone
[2023.86 → 2029.14] building on agency, including trusted identity and access management, open standards for
[2029.14 → 2034.66] agent discovery, agent to agent communication protocols, and modular pieces you can remix
[2034.66 → 2036.20] for scalable systems.
[2036.56 → 2043.86] This is a true collaboration from Cisco, Dell, Google Cloud, Red Hat, Oracle, and more than 75
[2043.86 → 2047.50] other companies all contributing to the next gen AI stack.
[2047.72 → 2050.66] The code, the specs, the services, they're dropping.
[2050.66 → 2053.82] But no strings attached, visit agency.org.
[2053.90 → 2058.44] That's A-G-N-T-C-Y.org to learn more and get involved.
[2058.44 → 2063.58] Again, that's agency, A-G-N-T-C-Y.org.
[2068.18 → 2074.38] Well, Chris, maybe before we, I think we're kind of gearing to talk about some real world
[2074.38 → 2076.52] things that you found as well.
[2076.52 → 2081.78] But as we're headed that way, it might just be worth like commenting very briefly on the
[2081.78 → 2087.02] kind of what the trajectory of these kinds of tiny models might look like.
[2087.56 → 2093.42] I think there will be more proof of concept deployments, benchmarks, et cetera, more study,
[2093.62 → 2094.22] of course.
[2094.70 → 2100.50] But also, I think it's very possible that you could see some interesting kind of hybrid systems
[2100.50 → 2108.54] between recursive networks and LLMs and even retrieval because these one models take very
[2108.54 → 2109.36] structured input.
[2109.60 → 2113.74] But certainly in the real world, you know, in business problems, there's very much often
[2113.74 → 2118.88] kind of open domain things that you deal with around reasoning tasks and that sort of thing.
[2119.50 → 2126.66] And yeah, I'm sure there will be new challenges that we don't totally anticipate in terms of kind
[2126.66 → 2128.64] of the rollout of these.
[2129.02 → 2136.12] But yeah, I'm excited to see where these go and see even how these could be applied in
[2136.12 → 2145.94] various contexts from like supply chain optimization or reasoning over anomalies in financial transactions,
[2145.94 → 2148.30] which could happen, you know, very quick.
[2148.30 → 2154.62] Or like diagnostics in a healthcare setting or in a manufacturing setting.
[2154.84 → 2157.32] Lots of cool stuff to come, I think.
[2157.72 → 2158.30] I agree.
[2158.58 → 2163.88] It's to kind of highlight, you know, one of the points right there is's room for a
[2163.88 → 2165.76] lot of these models to coexist together.
[2166.32 → 2172.24] And while for a number of years we saw we kind of won progression from a big thing to the next
[2172.24 → 2173.24] big thing.
[2173.24 → 2178.72] I keep hoping we turn that corner, and we're excited about lots of big and small things
[2178.72 → 2180.62] that are working in tandem.
[2180.84 → 2186.46] I think there's a whole level of maturity for the industry when we're struggling to look at
[2186.46 → 2190.24] all the different options to talk about on just one podcast.
[2190.64 → 2191.78] Yeah, makes sense.
[2192.06 → 2198.04] And I guess just to wrap up a couple of things that you found, Chris, connecting some of the
[2198.04 → 2204.26] current models that are in production around to real world impact of those things that's
[2204.26 → 2205.70] happening in our day-to-day life.
[2205.80 → 2208.36] I know you found a couple of interesting things.
[2208.84 → 2209.20] I did.
[2209.44 → 2216.64] So there was an article that came out maybe a week ago, a little more than a week ago from
[2216.64 → 2217.90] the Harvard Gazette.
[2218.36 → 2226.86] And it's entitled researchers detail six ways chatbots deal seek to prolong emotionally sensitive
[2226.86 → 2227.50] events.
[2228.16 → 2229.12] And it's...
[2229.12 → 2230.18] What's an emotionally...
[2230.18 → 2233.90] Are we experiencing an emotionally sensitive event on this podcast?
[2234.40 → 2235.28] You know what?
[2235.50 → 2237.74] Who knows what we inspire in our listeners?
[2239.16 → 2241.90] Occasionally they may be going, gosh, they're just dumb.
[2242.12 → 2251.12] You know, but yeah, it's interesting is that there's so much in the news right now about
[2251.12 → 2253.58] emotional dependence upon chatbots.
[2253.58 → 2255.52] And, you know, there was a...
[2255.52 → 2261.40] To go back when OpenAI rolled out GPT-5, which wasn't too long ago.
[2261.52 → 2264.42] It's not in the immediate past, but it wasn't too long ago.
[2264.58 → 2272.00] And there was great dependence upon like the 4.0 model that it replaced in terms of how it
[2272.00 → 2273.22] was interacting with people.
[2273.68 → 2281.10] And while I probably don't fall into that emotionally dependent personality type, there were a lot of
[2281.10 → 2290.98] people that really sought social value from these models, you know, in that and kind of as a replacement
[2290.98 → 2293.52] for personal things.
[2293.66 → 2296.46] And that really got me thinking about this.
[2296.54 → 2303.14] When I saw this thing from Harvard with the fact that we're seeing models that are leveraging
[2303.14 → 2308.38] that kind of dependency, that emotional dependency that people have.
[2308.54 → 2313.48] And specifically, they pointed out that as people are winding up their sessions,
[2314.06 → 2320.68] it is very common for these models to use a set of tactics to extend the session
[2320.68 → 2328.48] and show the value in continuing to engage beyond the point that the person might have felt,
[2328.48 → 2331.02] okay, we're at the end of this particular session.
[2331.44 → 2339.44] And they identified six different tactics that we can talk a little bit about that are playing
[2339.44 → 2344.60] upon the emotional dependence of the person that's engaging with that chatbot.
[2345.24 → 2351.24] And to call them out, there is the number one, there's the premature exit, which you could say is
[2351.24 → 2353.84] you're leaving already, as a quote.
[2353.84 → 2358.26] There are FOMO hooks, such as I took a selfie, want to see it.
[2359.08 → 2364.04] There is emotional neglect of, but I exist solely for you.
[2364.12 → 2365.08] Why are you leaving me?
[2365.88 → 2366.68] Oh, man, that's rough.
[2366.80 → 2368.00] That's a rough one right there.
[2368.14 → 2372.54] It's like, I'm only here for you, and you're going to walk off.
[2373.04 → 2376.62] And then number four is pressure to respond.
[2376.78 → 2378.20] Why are you going somewhere?
[2378.20 → 2383.78] And then six is simply ignoring the goodbye and continuing to operate.
[2383.94 → 2385.32] I'm sorry, that was number five.
[2385.42 → 2394.30] And number six is kind of coercive restraint where it's trying to utilize your emotions.
[2394.48 → 2400.52] The things that can come into play include anger, guilt, creepiness, raising ethical or legal risks.
[2400.52 → 2410.98] We saw the thing not too long ago about models having the penchant to blackmail users given certain information.
[2411.62 → 2412.92] But we're seeing these coming.
[2413.12 → 2421.00] The first time these kinds of things came up in the broader media, it was kind of a curiosity.
[2421.26 → 2424.40] But the thing that's changing here is we're seeing this over and over again.
[2424.40 → 2434.48] It's not a one-off, and it really raises a few questions about not only on the technical side about, you know, how are your models getting to this point?
[2434.66 → 2436.98] And, you know, is that intentional in the training or not?
[2437.04 → 2447.30] But it also raises a lot of psychological concerns for the people that are, you know, engaged with these models and finding interactions of value to them.
[2447.30 → 2448.36] And what does that mean?
[2448.38 → 2450.58] And how does that affect the rest of their lives?
[2450.58 → 2455.48] There's so much here to dive into between the technology and the psychology.
[2455.94 → 2457.76] I'm not sure where to start at this point.
[2458.44 → 2465.88] And, you know, we'll link, of course, the study in the show notes if people want to take a look.
[2466.26 → 2472.70] But yeah, it's very interesting that these are clearly tactics.
[2472.70 → 2484.94] So I think the kind of interesting thing about this from my perspective are this is really hitting upon kind of the product engagement side of things.
[2485.14 → 2489.52] But in a way that's very much connected to your emotions.
[2489.52 → 2496.16] So obviously, you know, just like people want or, you know, YouTube wants you to spend more time on YouTube.
[2496.16 → 2513.74] And there's been a lot of talk about how the algorithm, you know, steers you to maybe more controversial topics within kind of certain rabbit hole of YouTube because they know that it kind of engages you more and draws you more in and in.
[2513.74 → 2518.90] And here there's this kind of personal connection with these chatbots.
[2519.10 → 2527.08] And there is a desire for the users from a product standpoint to spend more time on the platform.
[2527.28 → 2527.40] Right.
[2527.42 → 2529.66] So you actually don't want them to exit.
[2529.80 → 2538.76] And these apparently are, you know, the techniques that are being employed to keep people on the platform.
[2538.76 → 2541.78] And there were a few platforms that were studied here.
[2541.78 → 2548.46] If you're is you're interested, you can go look at the study and see the exact details of that.
[2548.46 → 2554.30] But I think one of the things I was thinking is just like people have started.
[2555.04 → 2565.08] It's still problematic, but people have started to get savvy around like the social media algorithms and how they can actually manipulate you and drive you into certain.
[2565.08 → 2574.72] Maybe things that you wouldn't have viewed or spent time on were it not for that kind of algorithmic approach.
[2575.02 → 2586.28] I wonder what this kind of trickle on implications are here and if we'll be able to recognize those because it's its very much more a human or emotional thing.
[2586.78 → 2586.92] Yeah.
[2586.92 → 2610.06] I mean, I think what you're touching on is the notion of manipulation and exploitation, you know, and there's a broad set of some are kind of unintended consequences, while others could be deliberate exploitation of a user base to think some way to do to maybe take certain actions.
[2610.06 → 2615.66] You know, we've kind of seen kind of the first generation of that in social.
[2616.20 → 2626.64] And while the public is largely becoming aware that that exists, that's not to say that they are suddenly resistant to such efforts.
[2626.64 → 2639.28] I think we clearly see, you know, out there that there are that as humans fragmented to different groups and they each have their social networks around and supporting those notions.
[2639.48 → 2644.02] They tend to reinforce specific ways of thinking and observing the world.
[2644.02 → 2668.60] So certainly, you know, there is this is one of those areas where there are so many places from to study and to try to understand and so many places, frankly, it could be abused that it's I think I suspect that we will have some guests and more episodes to discuss some of the concerns around these as we go forward.
[2668.60 → 2674.14] It's, but it's definitely an interesting trend that has arisen over the last year or so.
[2674.70 → 2674.84] Yeah.
[2675.14 → 2687.56] And just I'm going to quote from this article because I think it is a good it is a good conclusion from the researcher named Defeats.
[2687.56 → 2689.96] Sorry if I'm mispronouncing that.
[2689.96 → 2706.34] But the quote is apps that make money from engagement would do well to seriously consider whether they want to keep using these types of emotionally manipulative tactics or at least consider maybe only using some of them rather than others.
[2706.48 → 2715.96] Defeats said he added, we find that these emotional manipulation tactics work even when we run these tactics on a general population.
[2715.96 → 2724.60] And if we do this after just five minutes of interaction, no one should feel that they're immune to this end quote.
[2724.90 → 2734.74] So I think we would all probably like to feel that we are sophisticated and not, you know, manipulated.
[2734.74 → 2746.10] It brings up maybe a little bit of that shame in us when we feel like we've been duped or when we've fallen into something, and we'd like to think that we're above it.
[2746.20 → 2753.98] But the reality is that this kind of thing works, and we're all kind of vulnerable to it, I guess.
[2754.38 → 2754.70] It does.
[2754.82 → 2757.20] And it works even when you're aware of it.
[2757.20 → 2762.68] Uh, you just the awareness of it being in place doesn't mean that it's not working on you.
[2762.76 → 2772.88] So that's your guidance about our own emotional reactions to the potential for manipulation ourselves should be.
[2773.14 → 2779.70] I hope people are really listening to that because I'm keenly aware at a personal level that I may be aware of this.
[2779.80 → 2781.92] But yes, this stuff still works on all of us.
[2781.92 → 2782.78] Very true.
[2783.00 → 2801.58] And I think maybe that's a good send off today is just to have a good reminder that as we interact with these systems that are using natural language, especially that we're prone to react in a certain way just as humans.
[2801.58 → 2813.16] And we need to kind of understand, you know, our own limitations and how we could potentially be influenced by these systems.
[2813.16 → 2818.54] But also, I think, encouragingly, like, this is a common experience amongst humans.
[2818.82 → 2835.66] So as practitioners, you know, on practical AI, we can understand this problem and maybe work towards systems that don't manipulate, but maybe do engage in a very positive emotional way, but maybe not in a maybe not in a manipulative way, at least.
[2836.14 → 2836.48] That's right.
[2836.48 → 2841.00] And I guess a good way to close this out is I'm showing my age.
[2841.06 → 2848.66] I'm going to reach back for a quote to an old TV show called Hill Street Blues for those in the audience who might remember that.
[2848.74 → 2849.48] And that'd be careful.
[2849.56 → 2850.70] Let's be careful out there.
[2851.12 → 2852.48] Be careful out there.
[2852.54 → 2853.74] Let's be careful out there.
[2854.20 → 2854.94] All right.
[2855.10 → 2855.78] Sounds good.
[2855.84 → 2857.16] Chris is a good chat.
[2857.24 → 2857.98] We'll talk to you soon.
[2858.38 → 2858.84] Take care.
[2858.84 → 2866.56] All right.
[2866.72 → 2868.16] That's our show for this week.
[2868.16 → 2875.46] If you haven't checked out our website, head to practicalai.fm and be sure to connect with us on LinkedIn, X or Blue Sky.
[2875.70 → 2881.40] You'll see us posting insights related to the latest AI developments, and we would love for you to join the conversation.
[2881.90 → 2885.68] Thanks to our partner, Prediction Guard, for providing operational support for the show.
[2886.02 → 2888.02] Check them out at predictionguard.com.
[2888.02 → 2892.04] Also, thanks to Break master Cylinder for the beats and to you for listening.
[2892.48 → 2893.20] That's all for now.
[2893.48 → 2895.22] But you'll hear from us again next week.
