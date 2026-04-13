[0.00 --> 8.74]  Welcome to the Practical AI Podcast, where we break down the real-world applications
[8.74 --> 13.64]  of artificial intelligence and how it's shaping the way we live, work, and create.
[13.88 --> 19.14]  Our goal is to help make AI technology practical, productive, and accessible to everyone.
[19.48 --> 23.54]  Whether you're a developer, business leader, or just curious about the tech behind the
[23.54 --> 25.12]  buzz, you're in the right place.
[25.12 --> 29.84]  Be sure to connect with us on LinkedIn, X, or Blue Sky to stay up to date with episode
[29.84 --> 33.02]  drops, behind-the-scenes content, and AI insights.
[33.36 --> 35.88]  You can learn more at practicalai.fm.
[36.18 --> 37.52]  Now, on to the show.
[48.58 --> 52.18]  Welcome to another episode of the Practical AI Podcast.
[52.18 --> 60.52]  I am your host, Chris Benson, and today we have a wonderful guest from NVIDIA.
[60.66 --> 63.48]  We've had some other guests along the way, as everyone knows.
[63.98 --> 69.74]  And today, I would like to introduce Joey Conway, who is the Senior Director of Product Management
[69.74 --> 71.68]  for AI Models at NVIDIA.
[72.18 --> 73.40]  Welcome to the show, Joey.
[73.78 --> 74.44]  Yeah, thanks, Chris.
[74.50 --> 75.02]  Good to be here.
[75.32 --> 76.50]  I'm looking forward to it.
[76.50 --> 82.26]  I know we're going to talk about a couple of recently announced models that you guys
[82.26 --> 83.52]  have put out there.
[83.62 --> 88.52]  But before we do that, I always like to get a sense of kind of like, you know, your own
[88.52 --> 94.28]  background, how you came to NVIDIA, and specifically, you know, this particular area of work.
[94.36 --> 99.94]  I'd love to know how you got into this and what that special sauce about what you do is
[99.94 --> 100.48]  for yourself.
[100.48 --> 106.56]  Yeah, I think from my background, I've done some software development in the past and also
[106.56 --> 108.34]  done some product management in the past.
[109.00 --> 114.86]  And I think in looking at opportunities, say maybe 10 years back of exciting things in the
[114.86 --> 119.70]  future, one thing I was personally excited about was machine learning and AI.
[120.44 --> 126.46]  And I think looking at opportunities, NVIDIA, this was almost a decade back, NVIDIA was at
[126.46 --> 131.12]  a great spot of they were involved in many things and things were just getting started.
[131.40 --> 134.14]  And so I had a great opportunity to join NVIDIA.
[134.82 --> 139.12]  And then being here, the company works on all sorts of amazing technologies.
[139.72 --> 146.42]  I think one space that our team has focused on has been essentially the non-vision workloads.
[147.04 --> 153.04]  And so we started many years back with things like BERT and NLP and maybe more simple types
[153.04 --> 158.82]  of language models that could do classification of intent and those types of things.
[159.08 --> 161.34]  And I think we've been on the journey for a while.
[161.68 --> 167.20]  And we've been excited that there's been great research and breakthroughs the last, say,
[167.28 --> 173.44]  five years that I think have made, we'll say, exponential improvements and brought it to
[173.44 --> 176.10]  a much more mainstream type of use case.
[176.10 --> 180.84]  And so I think the background there on my side of being familiar with software development
[180.84 --> 186.68]  and kind of comfortable with new technologies and then the excitement of new opportunities
[186.68 --> 190.16]  and places to grow, NVIDIA has been very well positioned at that.
[190.30 --> 193.64]  So I think it's been kind of a few factors coming together at the same time.
[193.84 --> 200.20]  And if you had asked maybe five, six years ago when we first started on some of this journey,
[200.70 --> 204.74]  I probably wouldn't have guessed we'd be at such a great inflection point that we are now.
[204.74 --> 208.90]  But I think we're very excited to be here and there's a lot of fun stuff happening we can talk about.
[209.74 --> 209.84]  Gotcha.
[210.46 --> 215.78]  So I know today we're going to dive into, I'd like you to introduce to the audience kind of
[215.78 --> 218.44]  the two models that were announced.
[218.64 --> 224.28]  But if you could kind of frame them a little bit and kind of like the current landscape of
[224.28 --> 230.96]  open foundation models and kind of where AI research is at this point and, you know, why
[230.96 --> 234.12]  why NVIDIA is putting these models out at this time?
[234.56 --> 235.26]  You know, what is it?
[235.32 --> 238.34]  What is it about them that's different from all the other stuff out there?
[238.58 --> 242.92]  And why is it, you know, why have you made some of the choices in terms of open versus
[242.92 --> 244.18]  closed, things like that?
[244.24 --> 247.24]  So if you would tell us about what, tell us about these models.
[247.72 --> 247.88]  Yeah.
[248.04 --> 251.70]  And I'm happy to start with kind of the landscape or where the world is at.
[251.80 --> 253.84]  And I can give a little bit of context there too.
[253.84 --> 259.88]  So on the NVIDIA side, we've been working on publishing models and kind of open weight
[259.88 --> 264.00]  checkpoints and to some degree data sets for many years now.
[264.58 --> 268.16]  It's been quite a while, five, six, seven years, probably even longer.
[268.70 --> 272.46]  And we've trained many large language models as well.
[272.70 --> 275.56]  I think the first one, I'm trying to remember the formal name.
[275.62 --> 279.48]  I think it was Megatron LM or Megatron NLG.
[279.64 --> 283.10]  There's a few variations of it, but that was probably four or five years ago.
[283.10 --> 286.46]  And we do it for kind of a few reasons.
[286.78 --> 291.42]  One is we want to understand how to take the best advantage of our infrastructure.
[291.76 --> 296.54]  So from compute and storage and networking, we also want to prove out the software stack
[296.54 --> 298.30]  and make sure the software runs great.
[298.94 --> 300.32]  And so we do that ourselves.
[300.70 --> 303.14]  We learn a lot along the way and we can make improvements.
[303.86 --> 307.56]  And then we also do that because we want the community to benefit and learn.
[307.72 --> 310.80]  And so we publish all that software, those techniques, the papers.
[310.80 --> 316.12]  And we do that so everyone else has higher confidence and can start from a better beginning
[316.12 --> 316.98]  spot than we did.
[317.80 --> 320.70]  And so we've been doing that for many years in many different domains.
[320.78 --> 325.68]  So things like speech or transcription and large language models and even simpler ones
[325.68 --> 328.44]  of smaller language models like things like BERT.
[328.84 --> 330.22]  So we've been doing that for quite a while.
[330.58 --> 334.96]  I think in parallel, there's lots of companies in the space and they all have different business
[334.96 --> 335.32]  models.
[335.32 --> 336.98]  And our goal is to support them.
[337.54 --> 343.04]  And so I think there's been a few big moments in kind of the language model space.
[343.14 --> 346.40]  I'd probably say BERT was a big one quite a few years back now.
[346.50 --> 353.54]  And that was where we kind of had an inflection point where language models could do essential
[353.54 --> 357.34]  classification tasks that previous to that we weren't able to do.
[357.34 --> 363.80]  And so being able to parse out language from people typing or speaking and being able to
[363.80 --> 368.34]  help understand what they want, what they're looking for, what types of actions they're
[368.34 --> 370.64]  asking for, that was a great breakthrough moment.
[370.86 --> 372.60]  And we're very happy with that.
[373.10 --> 376.84]  We've published lots of software to help support it and make sure it runs efficient on our
[376.84 --> 378.62]  infrastructure and people can benefit from it.
[379.08 --> 382.72]  I think probably another big moment for the world was ChatGPT.
[382.72 --> 387.66]  And I think we were super excited to see all that happen and OpenAI is a wonderful partner.
[387.94 --> 392.42]  And so when that happened, it was an inflection point where many people started to realize
[392.42 --> 394.12]  the capabilities of what was possible.
[394.62 --> 397.08]  And there was amazing research that went in behind that.
[397.60 --> 400.34]  And so that was kind of another big milestone that happened along the way.
[400.74 --> 404.24]  And so as each of these kind of occur, we're always asking how we can help.
[404.64 --> 408.46]  So how we can help more people take advantage of the technologies and benefit from them.
[408.46 --> 415.12]  And so as kind of that ChatGPT moment happened, many companies were starting to ask how they
[415.12 --> 416.58]  can take advantage of these technologies.
[417.44 --> 423.42]  And as we spend time working in that space, we love to support our partners and we think
[423.42 --> 425.22]  it's great for companies to use them.
[425.68 --> 430.28]  We started finding that there were some scenarios that not every company could use some of the
[430.28 --> 431.18]  solutions out there.
[431.68 --> 437.14]  And so scenarios were, say, a company has proprietary intellectual property that they don't want to
[437.14 --> 439.64]  leave their premise, that they need to keep on premise.
[440.14 --> 444.24]  There might be scenarios where they want control over the model, the model architecture.
[444.78 --> 449.24]  They want control over the data that goes into it, as well as what they fine tune it.
[450.26 --> 455.96]  And so in those scenarios, there was a lot of open source contributions a few years back.
[456.34 --> 459.02]  Many companies are training foundation models and we were really excited.
[459.58 --> 463.62]  And so we did our best to kind of support that, both in the software we published to make
[463.62 --> 466.66]  sure it runs well and all of these partners can build the best models.
[467.24 --> 472.66]  We also do some of that ourselves, too, to make sure that we're not just publishing things
[472.66 --> 475.50]  for others, but we use it ourselves to make sure it runs well, too.
[475.64 --> 478.74]  And we're always trying to stretch the scale of things going forward.
[479.10 --> 481.30]  And so we're always trying to push the limits of what's possible.
[482.00 --> 486.62]  And so in kind of that broader effort of pushing the limits, what we found is that there's
[486.62 --> 489.28]  opportunities for us to contribute that out.
[489.28 --> 493.44]  So say new infrastructure comes, we can sometimes be the first to show people how to do that.
[494.34 --> 499.90]  In terms of the large scale contributions we've been making over time, that's one of the incentives
[499.90 --> 502.56]  and reasons we have to keep participating in the space.
[503.10 --> 508.44]  And so going forward from the moments of, say, two years back when lots of companies and
[508.44 --> 513.72]  partners were publishing open models to where we are today, the biggest breakthrough we've
[513.72 --> 519.78]  seen happen was probably around January, February, in terms of open weight models now supporting
[519.78 --> 520.88]  reasoning capabilities.
[521.54 --> 525.98]  And this came through DeepSeq as kind of one of the leaders in this space of being able
[525.98 --> 532.12]  to add reasoning capabilities, meaning we can take complex queries and we can now start
[532.12 --> 536.94]  to break them down and think through them and come up with answers that previously we couldn't.
[537.34 --> 542.52]  Previously, we often just had one question in and one answer back out and we had to be fast
[542.52 --> 546.18]  at it. And now with reasoning, the models can take some time and think about it.
[546.72 --> 551.08]  And so that's probably the next big milestone that we're really excited about seeing.
[551.28 --> 557.26]  And one of the main reasons that we're publishing models at this kind of juncture in terms of
[557.26 --> 559.52]  wanting to help move that technology forward.
[559.52 --> 564.34]  And I'm curious that, and that raises, that's really, that was a fantastic answer, by the way.
[564.42 --> 567.64]  And there was so much there that I'd like to dive into with you.
[567.64 --> 573.36]  I think a very first thing is, is we're hearing about reasoning a lot now, you know, you know,
[573.36 --> 576.48]  from various organizations, glad to hear it from you.
[576.60 --> 584.80]  But I think that it's one of those phrases that in the context of generative models, what
[584.80 --> 585.98]  does reasoning mean?
[586.40 --> 591.70]  Could you talk a little bit about what, what is the word reasoning in this context from
[591.70 --> 598.86]  NVIDIA standpoint? And how does reasoning in that context differentiate from some of these
[598.86 --> 604.30]  really powerful models we're seeing from NVIDIA and other organizations that have come, that
[604.30 --> 609.66]  have been able to do amazing things, but weren't necessarily classified as, as reasoning models?
[610.18 --> 614.96]  Yeah. And I can give a few answers here. I think there, there is a little bit of varying
[614.96 --> 619.68]  in definitions among the community, but I think I'll try and share where I see the most consensus.
[619.68 --> 623.06]  So maybe I'll go back a few stages. So I think, sure.
[623.42 --> 628.72]  Going back four or five years, when we had these, these models, we'll say like GPT type
[628.72 --> 634.88]  architectures that were auto regressive, meaning that they would go through a loop. And so they
[634.88 --> 638.96]  generate one word of a sentence, and then they'd feed that back in, generate the next word and the
[638.96 --> 643.98]  next word. And this was kind of the technique they use to be able to generate paragraphs and
[643.98 --> 649.58]  kind of this long generative content that we hadn't seen before. And this allowed them to write
[649.58 --> 656.24]  sentences, to write stories. And at that kind of original juncture, the challenge we had is it
[656.24 --> 661.86]  would just do say this next word prediction. We had struggles knowing how to control it,
[661.92 --> 666.42]  how to direct it, how to guide it, and how to keep those answers with a high accuracy.
[667.26 --> 671.90]  And so one of the great breakthroughs that OpenAI achieved with Chad GPT that the world got to
[671.90 --> 677.24]  experience was you could tell the model or give it better guidance and directions and it would adhere
[677.24 --> 681.60]  to it. And so everyone was very impressed and excited about some of these techniques like
[681.60 --> 686.20]  alignment and reinforcement learning. And it was wonderful breakthrough. And I think, you know,
[686.22 --> 691.34]  we've all benefited from that technology. And that next stage then allowed us to take these models
[691.34 --> 696.36]  instead of just doing the next token, they now would actually stay on topic of what we asked.
[696.80 --> 701.20]  And so they could follow directions. If you said, now take your story and do it in a bullet point
[701.20 --> 706.40]  format or do an intro, a body and a conclusion, it would now actually do that instead of just giving you
[706.40 --> 710.88]  the next word and giving a big paragraph. And so that was one of the big breakthroughs along the way.
[711.74 --> 716.56]  That as of this year, the big breakthrough with reasoning, the way we think about this is that
[716.56 --> 721.10]  there's kind of these sets of questions or challenges that models have been able to solve
[721.10 --> 726.88]  up to today. What we see with reasoning is there's a whole nother set of questions and challenges that
[726.88 --> 732.10]  we couldn't previously solve. And kind of the rationale behind it, and then I'll go into some examples.
[732.10 --> 738.32]  Previously, we usually, when we would kind of interact with a model, we would either give it
[738.32 --> 743.34]  like a prompt. So you give it a question, or you could give it a few examples in the prompt,
[743.46 --> 748.50]  and then a question. You could say like, you know, I want to do math. Here's some examples of how math
[748.50 --> 753.82]  works. And now here's a math problem. And then the models were pretty good at that. What we've seen,
[753.92 --> 759.52]  though, is that the more complex the questions are, the more difficult it was for the model to solve
[759.52 --> 765.56]  it in the first pass. And so often people would just give it these complex queries, say like a
[765.56 --> 770.40]  word problem. You know, we could, the classic of two trains coming at each other with different speeds.
[770.40 --> 774.84]  And, and like the, the reasoning you have to walk through of like, the first train is at this speed,
[774.90 --> 780.06]  the second train is at that speed, what is their directions? What is their rate, like the ability
[780.06 --> 784.40]  to then walk through and ask four or five sub questions that are needed to answer that question.
[784.40 --> 789.24]  The models weren't very good at doing that. And often what we would have to do is we would have
[789.24 --> 794.02]  to manually ourselves or try and use another model to break down the question into sub questions,
[794.02 --> 797.98]  and then try and find ways to answer each of those sub questions with different models.
[798.34 --> 802.28]  And there was just a lot of manual stitching and kind of ad hoc work that had to happen.
[802.86 --> 808.72]  And with reasoning, what has now the big breakthrough is, we're now able to train the models at kind of
[808.72 --> 813.68]  training time around the skill of we show them here's a question. And then here are the different
[813.68 --> 819.44]  ways to break it down. These are sometimes called things like reasoning traces, where we show there
[819.44 --> 824.16]  are multiple ways to solve it, but we give all those examples in there. And then we give the answer.
[824.92 --> 829.00]  Previously, it was very much focused on here's the question, here's the answer. And that's how we teach.
[829.90 --> 834.26]  But it kind of makes sense if you think about how people learn, you know, when you're doing math
[834.26 --> 837.88]  problems, it's always good to get the right answer. But sometimes it's even better just to
[837.88 --> 841.94]  understand how to solve it as opposed to the right answer. And so that's been the big breakthrough
[841.94 --> 846.34]  with reasoning is we now can teach the models, here's a way to think through complex problems,
[846.34 --> 852.36]  and be able to not just give the right answer, but give all the supporting thought and process you
[852.36 --> 858.90]  use to reach that right answer. And that applies to like scientific domains, say biology, chemistry,
[859.10 --> 864.88]  physics applies to math, applies to software development, it should apply to the majority of domains.
[864.88 --> 870.44]  And it's kind of the next tier of challenging problems that we haven't been able to solve
[870.44 --> 877.30]  very well. And in the open space, these are a big breakthrough in terms of both the data and the
[877.30 --> 881.96]  techniques of how to teach the model, as well as just the model capabilities themselves and the
[881.96 --> 884.26]  final checkpoint that people can download and use.
[884.94 --> 890.52]  So that was pretty fascinating from my standpoint to kind of hear that laid out. I think that's the
[890.52 --> 896.64]  best explanation I've ever heard in terms of what reasoning is in this modern context.
[897.12 --> 901.60]  Could you kind of dive in a little bit to introducing the actual models themselves?
[902.40 --> 908.36]  And for each of them, kind of describe how they fit into the ecosystem, what they're trying to solve.
[908.70 --> 916.42]  I know at least one is a reasoning model, and kind of talk about, you know, why, why them versus some of
[916.42 --> 921.74]  the others that they are, you know, within their kind of sub genres ecosystem wise, could you go
[921.74 --> 923.36]  ahead and introduce the models themselves?
[924.02 --> 928.92]  Yeah, in terms of what we've worked on at NVIDIA, and kind of where we wanted to contribute,
[929.46 --> 935.04]  there's a great thriving community of open weight models. And there's many great partners out there,
[935.10 --> 940.82]  from China to the US to Europe, I think we're in other parts of Asia, we're very excited to see
[940.82 --> 946.36]  these ecosystems growing. And where we wanted to focus at NVIDIA, we're on some of the harder
[946.36 --> 951.98]  problems that we knew it would be difficult for people to solve for, and do it in such a way that
[951.98 --> 958.58]  we could benefit all of the community. And so in kind of this path of seeing the growing capabilities
[958.58 --> 963.86]  of open weight models, we tried to think through what all the techniques and skills could be to create
[963.86 --> 970.16]  even better reasoning models. And so what our focus was, is we wanted to be able to take the best of
[970.16 --> 975.86]  what's open, and make it better. And so one of the themes you'll see as we go forward is we're
[975.86 --> 981.44]  constantly evaluating what's the best in the open community, and how do we improve it. And so kind
[981.44 --> 988.02]  of leading up to how we decided to publish these models, I'll share maybe high level some of the key
[988.02 --> 993.12]  techniques that went into thinking about where we could contribute. And then I'll explain the models
[993.12 --> 994.98]  that we published and why we did that.
[995.10 --> 995.62]  That'd be perfect.
[995.62 --> 1001.26]  Yeah, great. So in thinking through what's out there in the community, what we realized is that
[1001.26 --> 1007.48]  while there are some great open weight models, often the data sets aren't necessarily all open,
[1007.74 --> 1013.70]  and the tooling isn't necessarily all there, and the techniques aren't necessarily as transparent
[1013.70 --> 1018.22]  or published, so everyone can reproduce them. And so in kind of thinking through these challenges,
[1018.82 --> 1023.24]  we took kind of the life cycle of a model of life cycle of creating a model, say,
[1023.24 --> 1027.90]  you start from some data, you start from some architecture, and then at the end,
[1027.98 --> 1032.42]  you produce a checkpoint that people can go deploy and use and gain value from in a business setting.
[1033.06 --> 1037.70]  And so kind of walking along that journey, we saw things on the pre-training side, where it's
[1037.70 --> 1042.98]  usually a large set of unlabeled data, where we're teaching the model just kind of general knowledge
[1042.98 --> 1049.76]  and skills of the world and languages and content. On that side, there's not as much open data there,
[1049.76 --> 1055.88]  and the techniques of how to do that aren't necessarily as public or as published as we'd like.
[1056.08 --> 1061.04]  And so that was kind of one place we thought about. The kind of next stage we thought about was,
[1061.40 --> 1065.50]  once this base model that has some set of knowledge of the world and capabilities,
[1066.02 --> 1071.38]  often people then take it and fine-tune it, or make it kind of an expert of how to either interact
[1071.38 --> 1076.58]  with people or how to solve a certain domain of problems. And so we wanted to focus heavily on
[1076.58 --> 1082.60]  what we felt was important to enterprise companies. And so some of the skills that we decided would be
[1082.60 --> 1087.12]  really helpful for the community and for enterprise companies, which is kind of our focus in this place
[1087.12 --> 1092.26]  is on enterprise adoption and growth, were things like being able to work through scientific question
[1092.26 --> 1099.34]  answer problems, things like math, things like coding, things like tool calling or instruction following,
[1099.78 --> 1104.14]  and then being conversational. Those are some of the key places that we felt
[1104.14 --> 1109.38]  that enterprises would benefit the most from. And kind of the flip side of those challenges are,
[1110.12 --> 1114.60]  in the enterprise setting, they're very much looking forward to having the most correct answer.
[1114.72 --> 1120.08]  They want to avoid hallucinations or incorrect answers. They want the models to follow directions.
[1120.08 --> 1125.22]  If I'm asking for three bullets, I want it in three bullets, not five and not a paragraph.
[1125.98 --> 1130.28]  And then also on the scientific question answer side, there's a whole domain of companies
[1130.28 --> 1135.46]  who are working from things like say drug discovery, or other kind of domains that are quite technical,
[1135.46 --> 1140.70]  where they have complex problems that they can benefit from the reasoning capabilities of the model,
[1141.12 --> 1145.78]  being able to think through and have more time to run these kind of inference calls and reflect
[1145.78 --> 1151.38]  and progress through complex challenges. So those are kind of the on the accuracy side of the
[1151.38 --> 1154.46]  capabilities and skills we wanted to make more available to the community.
[1154.46 --> 1159.84]  And then on the infrastructure side, we knew that these models are super capable.
[1160.30 --> 1164.74]  And with reasoning, another challenge we introduce is it requires more compute and more iteration.
[1165.04 --> 1170.94]  So every time a token is generated, take some compute. And when you think, it generates more tokens.
[1171.62 --> 1177.40]  And so the challenge here is that the more the model thinks, the more compute and potentially more expense there is.
[1177.92 --> 1181.62]  But the upside and breakthrough is we can now answer more difficult problems we couldn't before.
[1181.62 --> 1186.96]  And so we wanted to think through how to optimize the model to be more efficient on the compute side,
[1186.96 --> 1193.34]  so that as we spend more time reasoning, we don't actually grow all the expense for the end customer
[1193.34 --> 1195.34]  when they want to solve more complex problems.
[1196.26 --> 1199.22]  And so those were kind of the key challenge sets we were thinking through.
[1199.84 --> 1204.12]  And so as we went on this journey with the Nemotron family of models,
[1204.68 --> 1207.84]  what we published and what we started publishing back in March,
[1207.84 --> 1213.18]  and kind of celebrating the beginning of this venture is what we're calling Lama Nemotron,
[1214.02 --> 1217.02]  meaning that we started from a base Lama model,
[1217.40 --> 1221.56]  and then we used the best of the open models and data sets in the community.
[1221.80 --> 1225.62]  So we pulled data from many of the public models, things like Mistral,
[1226.06 --> 1228.98]  things like our own Nemotron, as well as things like DeepSeek and Quen,
[1229.06 --> 1231.12]  where there's amazing breakthroughs in the open community.
[1231.12 --> 1234.90]  And we used those to gather the best data and the best knowledge,
[1235.42 --> 1239.92]  and then took some of the state-of-the-art training techniques in our software stack
[1239.92 --> 1242.18]  that's open and available called Nemo Framework,
[1242.60 --> 1247.88]  and were able to take the Lama models and improve their capabilities and skills for reasoning,
[1248.46 --> 1252.60]  and be able to publish and win many of the leaderboards in those domains.
[1253.40 --> 1257.76]  And along that way, some of the other work we did was shrinking the model architecture,
[1257.76 --> 1260.50]  so what we call kind of neural architecture search,
[1260.92 --> 1266.70]  and being able to take what Lama did as an amazing and quite common and popular transformer architecture.
[1267.16 --> 1271.12]  There were ways that we were able to essentially shrink that model architecture
[1271.12 --> 1273.24]  while keeping the accuracy the same.
[1273.66 --> 1277.86]  And that allowed us to reduce the cost and the compute footprint a bit as well, too.
[1278.02 --> 1282.78]  So at the same time, we introduced reasoning and make the model more capable.
[1283.08 --> 1285.20]  It also slows it down a bit,
[1285.20 --> 1289.92]  and so we were able to shrink the model architecture to try and keep that speed as quick as we could.
[1290.54 --> 1293.88]  And at the end, then we published kind of a family of three models.
[1294.10 --> 1301.88]  We have what we call a nano, being generally a quite small model that would fit on maybe a smaller data center GPU.
[1302.60 --> 1305.18]  And then we have the super, which fits in the middle,
[1305.36 --> 1309.42]  and that fits on one more common large-scale data center GPU,
[1309.60 --> 1311.66]  like, say, an H100 or an A100.
[1311.66 --> 1314.56]  And then we have the ultra, the third of the family.
[1315.04 --> 1317.12]  The ultra fits within one node,
[1317.44 --> 1321.10]  so eight of the H100s or eight of the A100 GPUs.
[1321.32 --> 1325.24]  And the ultra is often the model that shows the best capabilities,
[1325.46 --> 1326.62]  the state-of-the-art accuracy.
[1327.10 --> 1331.64]  And then the nano and the super are often where we see most people begin and start
[1331.64 --> 1335.54]  and put into production and build and fine-tune on top of.
[1335.54 --> 1339.36]  And so as we publish these kind of three models in this family,
[1339.58 --> 1342.80]  we also publish the data we use to post-train them.
[1343.12 --> 1345.96]  So all of that data we made open source and available.
[1346.16 --> 1349.84]  That includes all the math and the scientific question answers,
[1350.06 --> 1353.80]  the chat, the instruction following, reasoning, and non-reasoning.
[1353.80 --> 1358.08]  So one clever thing we wanted to set out to do here was prior,
[1358.52 --> 1361.26]  the models that were open were either reasoning or non-reasoning,
[1361.30 --> 1362.16]  and they were separate models.
[1362.80 --> 1366.60]  And we could kind of empathize with enterprises that deploying two models
[1366.60 --> 1368.28]  is twice as much work as deploying one.
[1368.78 --> 1372.58]  And so one thing we did when we first published these was put them into one model.
[1373.10 --> 1374.76]  And so that way you can ask the model,
[1375.10 --> 1376.16]  can you reason through this?
[1376.18 --> 1377.14]  This is more complicated.
[1377.28 --> 1379.90]  I'm willing to spend the time and wait and invest in the answer.
[1379.90 --> 1383.54]  Or this is a super simple answer, like what's two plus two?
[1383.72 --> 1384.70]  You don't need to reason.
[1384.88 --> 1387.26]  Just give me the answer and don't spend the compute on it.
[1387.34 --> 1390.46]  And so we published the data sets to support that capability
[1390.46 --> 1392.10]  as well as the model checkpoints.
[1392.42 --> 1396.18]  And then some of the software we used inside NEMO framework,
[1396.40 --> 1399.98]  things like NEMO RL, there's training techniques inside there.
[1400.08 --> 1401.44]  We also published as well too.
[1401.66 --> 1406.02]  And so all of this made kind of this family of models and data and tools
[1406.02 --> 1409.28]  that we published under the umbrella we're calling NVIDIA NEMOTRON.
[1409.28 --> 1409.80]  Gotcha.
[1410.20 --> 1415.18]  And just for reference, we often, to give people a sense of size
[1415.18 --> 1417.84]  and what GPUs, we'll talk about kind of input parameters.
[1418.30 --> 1421.74]  Could you assign for each of the three versions kind of the input parameters
[1421.74 --> 1424.04]  in terms of how many to, you know,
[1424.12 --> 1427.40]  are we talking like an 8 billion for NANO or something like that?
[1427.52 --> 1428.64]  I'll let you run with that.
[1428.94 --> 1429.12]  Yeah.
[1429.36 --> 1431.74]  And I'll tell you where we're at today
[1431.74 --> 1433.66]  and a little bit about where we see things going.
[1433.80 --> 1438.38]  So where we're at today is for the NANO, it's an 8 billion model.
[1438.38 --> 1441.36]  We do have a smaller 4 billion variant we just published,
[1441.54 --> 1445.10]  but we're likely expect to stay at the 8 billion parameter size
[1445.10 --> 1447.72]  when it's a dense model architecture.
[1448.10 --> 1451.56]  And kind of the rationale there is we're targeting, say,
[1452.04 --> 1457.58]  like a 24 gigabyte NVIDIA GPU, kind of roughly memory capacity-wise.
[1458.38 --> 1461.88]  And in that size range, we want to maximize the accuracy capabilities.
[1462.38 --> 1466.80]  And so likely around 8 billion dense is probably where we're going to stay there.
[1466.80 --> 1472.62]  On the super side, we're targeting one more common and larger data center GPUs,
[1472.64 --> 1476.40]  so like the H100 with 80 gigs capacity or A100 80 gig.
[1476.88 --> 1482.24]  And so in that space, we expect probably around 50 billion parameters of a dense model
[1482.24 --> 1484.32]  will be the best fit, and we published a 49.
[1484.82 --> 1487.58]  So we'll likely stay in that ballpark going forward.
[1488.28 --> 1492.60]  On the ultra side, what we published, and these are all, I should mention,
[1492.60 --> 1493.96]  their variants of LAMA.
[1494.22 --> 1496.52]  So like the Nano is an 8B.
[1496.94 --> 1502.34]  We distilled down to a 4B, but we realized kind of the capabilities of reasoning at the small scale.
[1502.48 --> 1505.22]  There are some challenges there, and so the 8B does do quite well.
[1505.78 --> 1510.34]  On the super side, we started from the LAMA 70B, which was a great size,
[1510.46 --> 1514.80]  but we wanted it to fit in one GPU, and so we distilled that down to the 49B.
[1514.80 --> 1519.20]  And on the ultra side, we started from LAMA's 405B from last summer,
[1519.44 --> 1524.92]  which running at, say, FP8 precision does roughly fit within one node,
[1525.16 --> 1529.08]  but our goal was to see if we could shrink it and maintain the accuracy
[1529.08 --> 1532.48]  because one node is still quite a large deployment footprint.
[1533.06 --> 1537.46]  And so with our ultra, we have 253 billion parameters on the dense side,
[1537.88 --> 1540.68]  and so that fits in roughly four, so about half a node.
[1540.68 --> 1545.32]  And so we were excited about those breakthroughs because it does kind of relate to the cost
[1545.32 --> 1550.56]  that it takes to run the model, and we're achieving the same, if not better, accuracy
[1550.56 --> 1552.10]  from what we built on.
[1552.48 --> 1557.30]  I think going forward, there'll likely be some changes in this space.
[1557.44 --> 1561.12]  I think there's work that NVIDIA has published on the research side recently
[1561.12 --> 1567.46]  around hybrid dense architectures where there's some techniques around, say, SSMs
[1567.46 --> 1573.76]  or, say, Mamba-style architecture where we can make the output generation much more efficient,
[1574.60 --> 1579.50]  and we expect that with reasoning, the longer generations of reasoning traces
[1579.50 --> 1584.30]  and the ability to think, that output generation will continue to be more of a challenge.
[1584.90 --> 1591.80]  And so I think we'll likely expect to see, on our side, say, a 10% to 15% throughput speedup
[1591.80 --> 1597.52]  on the output generation going forward in kind of newer iterations of this using some of the latest research.
[1598.50 --> 1603.72]  And then the other big exciting thing we're looking forward to is, on the mixture of expert side,
[1604.06 --> 1609.52]  we expect that at the very large scale, so likely around, say, like the ultra-size range
[1609.52 --> 1614.80]  where we've seen a lot of the community, say, like, Llama 4 is there and the DeepSeek and Quinn,
[1614.90 --> 1617.34]  they all have a mixture of experts, especially at the large scale.
[1617.34 --> 1624.00]  We expect that will be a new trend going forward, and we think we'll probably also be participating
[1624.00 --> 1629.92]  in that space, too, at the very large scale mixture of experts, allow us to get great accuracy,
[1630.36 --> 1635.62]  also allow us to be more inference efficient at that larger scale, too.
[1636.00 --> 1642.60]  I'm curious, as you've talked about kind of building off of that Llama 3.1 base, as you go,
[1642.60 --> 1648.92]  are you aware, like, are you and the meta teams that produce the Llama kind of, are you targeting
[1648.92 --> 1654.94]  the same types of features going forward and performance metrics? Because there's so many
[1654.94 --> 1661.52]  different places to allocate, you know, the effort. Are you very much in alignment, or do you find
[1661.52 --> 1669.10]  yourselves deviating a bit from meta? You know, as two large corporations that are partners and working
[1669.10 --> 1676.74]  together and both producing, you know, the same line of open source things, at least at a base level,
[1677.12 --> 1681.74]  how does that work? And do you, is there any collaboration with meta? Or do you guys each
[1681.74 --> 1686.92]  just kind of say, I'm going to go do my own thing and build off? Because, you know, they had built the
[1686.92 --> 1689.78]  best base so far for what you guys wanted to build off of next?
[1690.32 --> 1695.40]  Yeah, meta is a great partner. And so we do work really closely with them in lots of different ways.
[1695.40 --> 1699.92]  And so we've been very excited about all the Llama work. And they did have a conference,
[1700.04 --> 1706.02]  LlamaCon, probably a month and a half ago now. And we're very supportive. I think in their keynote
[1706.02 --> 1710.58]  there, you'll see there's a slide there on Llama Nemotron kind of celebrating some of the
[1710.58 --> 1716.10]  collaboration and achievements. And so I think there's definitely overlap. And those are the places
[1716.10 --> 1721.10]  where we try and collaborate as much as we can. And I think that they're also very focused on some of
[1721.10 --> 1726.36]  these challenges like reasoning and some of these enterprise use cases. And so we're always excited
[1726.36 --> 1731.36]  to see the next iteration of Llama because it gives us an even better starting point for us to think
[1731.36 --> 1736.00]  about where else to contribute. So I think going forward, I expect that we'll continue to be a
[1736.00 --> 1740.66]  great collaboration. I think we're always excited for the next versions of their models to come out.
[1740.88 --> 1745.86]  And we celebrate them both in our software stack, making sure they run efficiently and we can help
[1745.86 --> 1750.66]  enterprises deploy them directly. And then we try on the Nemotron side to see what else we can
[1750.66 --> 1754.64]  contribute from the rest of the community and some techniques and what kind of breakthroughs we can
[1754.64 --> 1760.46]  make. So I think some places where we might see differences going forward could be perhaps in the
[1760.46 --> 1765.18]  model architectures. I think those could be places where there's different research breakthroughs that
[1765.18 --> 1770.60]  come at different points in time. And so I think there might be timing differences there. In terms of,
[1770.60 --> 1776.12]  I think, like accuracy or capabilities, generally speaking, we're looking at very similar type of
[1776.12 --> 1781.68]  achievements. And so I think that will feel more like an incremental growth, say every few months.
[1782.32 --> 1787.10]  And so I think that'll be a place that we publish all the data. So we make it in such a way that
[1787.10 --> 1792.34]  everyone can benefit from. And so I expect going forward, we should see more achievements. And
[1792.34 --> 1799.74]  beyond Llama, I think part of our effort, and we did have a conference last week in Europe and Paris,
[1799.74 --> 1806.28]  and there we announced partnerships with a handful of model builders over in Europe, a little bit over
[1806.28 --> 1812.50]  10. And so our goal over there is also to try and enable a kind of a similar ecosystem where there's
[1812.50 --> 1817.26]  many different languages and culture and history in Europe. And so what we'd like to be able to see
[1817.26 --> 1823.58]  happen, and what our partners over there are super excited to be able to invest and do, is take some of
[1823.58 --> 1829.74]  these models and these techniques and data sets, and say, bring reasoning to Polish or to, you know,
[1829.80 --> 1833.78]  different languages in the regions there, where some of these are more nuanced and complicated.
[1834.44 --> 1838.96]  They have the history and the culture, and we have kind of the general skills. And so I think going
[1838.96 --> 1844.74]  forward, we expect to see a lot more of that out in the community, where people in certain countries,
[1845.16 --> 1849.00]  certain languages and cultures can benefit from a lot of the breakthroughs that happen in English first,
[1849.00 --> 1854.04]  in such a way that they can bring those skills. Because there are some things generally transferable,
[1854.20 --> 1859.96]  like math, generally speaking, is pretty consistent across languages. Software development is another
[1859.96 --> 1864.18]  one of those. And so we're pretty optimistic that the work that's happened in English and the data
[1864.18 --> 1869.22]  sets we publish should be able to help, say, bootstrap, so to say, other languages and get them up and
[1869.22 --> 1874.40]  going. And so each of those kind of countries and domains have points that they can celebrate and
[1874.40 --> 1879.70]  places that they can adopt and different challenges or obstacles, say, scientific question,
[1879.80 --> 1883.26]  answer in Polish that they're trying to work through, for example. So I think that'll be the
[1883.26 --> 1886.32]  other place we expect to see a bunch of growth and we're excited about.
[1887.12 --> 1893.34]  All right. So Joey, that was a great introduction to the models and laying them out. And to build on
[1893.34 --> 1899.28]  that a little bit as we get a little bit more in depth on them at this point, I think it is often
[1899.28 --> 1904.12]  cast in the industry is, and maybe depending on the organization, maybe it is competition, you know,
[1904.12 --> 1910.30]  competition, but there's also, you know, as you've laid out very well, a clear sense of partnership across
[1910.30 --> 1916.40]  organizations here. So if you're someone listening to this right now, and you've, and you've, you're, you're
[1916.40 --> 1923.66]  very interested in Nemo Tron, and you're, and maybe you already have Llama 3.1 deployed in your
[1923.66 --> 1929.26]  organization, how should people, and you may have the proprietary ones, you may have, you know,
[1929.26 --> 1936.80]  from, you know, Gemini or ChatGPT or whatever deployed as well. So how, with the model that you
[1936.80 --> 1943.30]  have produced here, how should people think about that in the sense of like, is, you know, there is
[1943.30 --> 1949.42]  obviously, uh, progress keeps being made and models build on each other. And so I think everyone's quite
[1949.42 --> 1953.30]  used to the fact that you're iterating on the models that are in your deployment in your
[1953.30 --> 1959.08]  organization. But now, you know, as you are looking at Nemo Tron, you may have the,
[1959.08 --> 1963.70]  the Lama model, where should they be thinking about Lama? Where should they be thinking about
[1963.70 --> 1968.76]  Nemo Tron? Where might they think about other things? How do you fit into someone's business
[1968.76 --> 1974.30]  today when they have all these different proprietary and open options available? What kind of guidance
[1974.30 --> 1975.10]  would you give on that?
[1975.62 --> 1981.82]  Yeah, I'll give two answers. I think one, I'll talk about generally how we think of just evaluating
[1981.82 --> 1986.20]  models and understanding capabilities. And then second, I'll answer specifically for, for
[1986.20 --> 1992.12]  Nemo Tron. I think generally the, the kind of the mental model we encourage people to have is
[1992.12 --> 1997.12]  think about models as, as say something like a digital employee. Like there's a set of skills
[1997.12 --> 2001.88]  and capabilities that they were taught, that they were trained on and things that they're really good
[2001.88 --> 2008.18]  at. And so those could be from say, open AI or Gemini or Claude, that there's amazing models out
[2008.18 --> 2013.30]  there. They could be from Lama, they could be from Mistral, Quinn, DeepSeek. There's a whole variety of
[2013.30 --> 2017.94]  options. And I think the way we think about it internally and where we encourage our customers
[2017.94 --> 2022.84]  to think about it is all these models were trained on, on different data sets, different sets of
[2022.84 --> 2028.68]  skills. There are things that their publishers are proud of and excited about. And the, the main
[2028.68 --> 2034.44]  challenge often is for companies to understand where these models are great and then match them
[2034.44 --> 2039.20]  up with where their internal opportunities are to use them. And I think that's kind of the bigger
[2039.20 --> 2044.36]  exercise that knowing these iterations will keep happening. We really want enterprises to get
[2044.36 --> 2050.06]  comfortable with kind of this discovery and, and opportunity fitting process. And so to do that,
[2050.12 --> 2054.26]  we have a separate set of software called Nemo Microservices. We've been publishing where there's
[2054.26 --> 2059.42]  some evaluation techniques and tools in there and some ways for enterprises to take internal data and
[2059.42 --> 2064.96]  create evaluation sets out of it. And so I think that's a great place that we hope to see more people
[2064.96 --> 2070.74]  be able to invest in because just like you interview an employee, you're looking for a set of skills and
[2070.74 --> 2075.36]  capabilities. You should be able to interview models. And so we're hoping that's something that
[2075.36 --> 2080.40]  people will become more and more comfortable with over time. And then the second piece there to talk
[2080.40 --> 2084.70]  about Nemo Tron, the places that we're really excited about Nemo Tron are going to be around
[2084.70 --> 2091.48]  enterprise agentic tasks. And so if there are scenarios where you're trying to look at things like
[2091.48 --> 2096.54]  complex tool calling, or there are scenarios where you have more complex queries that will benefit
[2096.54 --> 2101.94]  from the ability to reason through, meaning you have a query that might require answering from
[2101.94 --> 2108.04]  different data sources or from using say like a calculator plus a search plus a data retrieval.
[2108.26 --> 2113.16]  In those more complex scenarios, I think we're very excited that Nemo Tron should be one of the best
[2113.16 --> 2117.92]  models to work out there. The kind of the other things we would encourage people to think through are
[2117.92 --> 2122.88]  where you're going to deploy it. If you have constraints around the data or constraints
[2122.88 --> 2127.78]  around your compute, maybe it has to be on premise or it has to be in a certain geographic region, or
[2127.78 --> 2132.94]  if there's regulatory constraints, I think the Nemo Tron family of models give a lot of flexibility of
[2132.94 --> 2138.70]  being able to move where you need them, whether that's on prem or across cloud or different types of
[2138.70 --> 2143.70]  cloud deployments in different types of regions. And so those are probably the two key places where we
[2143.70 --> 2149.90]  would encourage people to think through using them. I think there often are places where we see many
[2149.90 --> 2154.04]  enterprises using multiple models. And I think that's often the way we encourage people to think
[2154.04 --> 2159.54]  about it because generally people think, oh, I'm using OpenAI, I'm all set. And then they don't realize
[2159.54 --> 2163.64]  that there is maybe a different set of problems or different set of challenges that there could be
[2163.64 --> 2168.80]  another solution to use in addition to. And so our kind of view is we expect the use cases and
[2168.80 --> 2174.18]  opportunities to grow. We don't view this as a kind of a fixed pie. Like every day we see more and more
[2174.18 --> 2179.04]  places that models can solve for and more and more opportunities to grow. And so we expect kind of
[2179.04 --> 2183.34]  in the end, there'll be a world where there are many different models all working together on different
[2183.34 --> 2188.54]  tasks. And enterprises can find the models that work best for them. They might even take, say,
[2188.72 --> 2193.42]  a Nemo Tron model and fine tune it. They might say, hey, here's a task that is it's really good at,
[2193.46 --> 2198.54]  say, tool calling. But I actually have all of my own internal APIs, my own internal tools inside my
[2198.54 --> 2203.26]  company. I needed to be an expert at those. And so they can take some of the data set we published,
[2203.44 --> 2207.92]  mix it with the data set they can create using some of the Nemo software, and then fine tune it.
[2208.06 --> 2212.80]  And then this variation of Nemo Tron becomes their expert at tool calling across their domain of
[2212.80 --> 2217.16]  tools internally. And they still could even use that in a workflow with, say, OpenAI or Gemini.
[2217.70 --> 2221.86]  And so I think we see a world where all of these models get used together to help solve business
[2221.86 --> 2222.74]  problems and outcomes.
[2223.38 --> 2227.68]  I love that. I think that's great. I think that is where we're going.
[2227.68 --> 2234.38]  But I think a lot of organizations that aren't AI global leader, organizations like NVIDIA and stuff
[2234.38 --> 2240.32]  are trying to find their way into that. They've kind of gotten into using a model or maybe a couple
[2240.32 --> 2246.94]  of models. And they're working on that kind of AI maturity level of how do they get their internal
[2246.94 --> 2254.44]  processes kind of aligned with this multi-model future that we have. So I think there's a lot of
[2254.44 --> 2260.74]  stories unfolding in that arena. One of the things I wanted to bring up real quick, not to deviate you
[2260.74 --> 2267.44]  necessarily off of Nemo Tron, but you also, I know you guys have a new speech model called Parakeet.
[2267.54 --> 2271.72]  And I was wondering if you'd talk a little bit about that as well and kind of share what that is
[2271.72 --> 2272.88]  and where that fits in as well.
[2272.88 --> 2278.76]  Yeah. Thank you. We do quite a bit of work and there's a lot of research that comes out of NVIDIA
[2278.76 --> 2285.32]  and it varies across model architectures, types, use cases, data sets. And on the speech place,
[2285.40 --> 2290.74]  we've been working there for quite a long time as well too. And in the transcription domain,
[2291.16 --> 2297.14]  the challenges have often been, can we transcribe the audio accuracy across different accents and
[2297.14 --> 2301.48]  dialects across different languages? And can we do that very fast and efficiently?
[2301.48 --> 2307.74]  And so in terms of what we've been publishing, we've been on that journey for many years and
[2307.74 --> 2313.74]  there's a great leaderboard on Hugging Face, I think called OpenASR, where it's an English data set,
[2313.80 --> 2319.10]  an English use case. And we've been working very diligently over time to keep improving
[2319.10 --> 2325.34]  the models that we publish there. And so I think you'll usually see us in the majority of the top 10
[2325.34 --> 2330.20]  with different variations of models. And often we get to trade first place with other companies and
[2330.20 --> 2334.02]  we're happy to see kind of the community pushing things forward and we're going to keep working
[2334.02 --> 2338.40]  on that. But I think the kind of the latest breakthroughs we've had in that space that
[2338.40 --> 2344.44]  we've been excited about is on the parakeet side, there is some architectural improvements
[2344.44 --> 2351.86]  that have made a significant kind of leap forward for us, so to say. And I think to talk a minute
[2351.86 --> 2356.54]  about those, I can go in a little bit of technical depth here. On the parakeet side,
[2356.54 --> 2362.42]  essentially it's based off of a fast conformer architecture, which improves the original conformer
[2362.42 --> 2368.44]  from Google. What we're excited about is that in terms of the model architecture, and you'll see us
[2368.44 --> 2374.14]  doing this with LMs too, we always often explore model architecture spaces in terms of what's the
[2374.14 --> 2380.56]  most compute efficient on the GPU. And so on the parakeet side, there's changes we made to the way we do
[2380.56 --> 2386.50]  depth-wise separable convolutional downsampling. Essentially meaning like at the start of the input,
[2386.54 --> 2393.14]  there are clever ways to shrink that input so we can cut some of the computational cost as longer
[2393.14 --> 2398.96]  audio segments get streamed in and we can kind of keep the memory down. And so in doing that,
[2399.26 --> 2406.72]  we're able to see roughly in aggregate a 2 to 3x speed up in inference speed, meaning we can ingest
[2406.72 --> 2412.22]  2 to 3x more audio in the same amount of time and transcribe it without reducing the quality of the
[2412.22 --> 2416.48]  audio. And then there's other work we've done in there. There's a whole bunch of clever work in
[2416.48 --> 2422.18]  there around things like changing the attention window to make that more global. And then there's
[2422.18 --> 2429.26]  work we've done around some of the frame-by-frame processing in there. So some of being able to
[2429.26 --> 2434.78]  chunk audio and properly chunk up that audio. So I have a long list of great things we've done in
[2434.78 --> 2439.02]  there. I'll mention a few other things too. There's been some work we've done in terms of the decoder
[2439.02 --> 2443.92]  part of the model architecture. There's a set of software we call CUDA graphs, where we're able
[2443.92 --> 2449.44]  to take smaller kernels and more efficiently schedule those on the GPU. That gives us as well
[2449.44 --> 2454.66]  another about 3x boost in speed. And so I think at the end of this, you'll notice, especially in that
[2454.66 --> 2461.90]  open ASR leaderboard, kind of the RTF factor there of real-time audio were quite high, especially
[2461.90 --> 2466.16]  compared to the alternatives up there. And that's because we spend a lot of time and have a lot of
[2466.16 --> 2470.42]  insight of how to do that on the GPU. And we try and do that in such a way that we can open it and
[2470.42 --> 2475.52]  publish it. So ideally other companies and partners can adopt some of those technologies and pull them
[2475.52 --> 2480.82]  into the models that they build and release as well too. Fascinating. Well, I appreciate that. Thanks for
[2480.82 --> 2487.28]  kind of laying that out. As we are starting to wind things up, I know that we have already delved a
[2487.28 --> 2492.76]  little bit into kind of the future and where things are going and stuff. But I'm wondering,
[2492.76 --> 2499.80]  you know, from your chair as you're sitting there driving these efforts forward at NVIDIA,
[2500.28 --> 2505.34]  and you're looking, I mean, this is probably the most fascinating time in history, in my view,
[2505.42 --> 2509.88]  when you think about, I mean, there's all sorts of things going on in the world. But in the technology
[2509.88 --> 2516.56]  space, the development of AI and related technologies here is just going faster and faster,
[2516.70 --> 2521.86]  broader and broader. And as you are thinking about the future, you know, I often say, you know,
[2521.86 --> 2525.56]  kind of like when you're going to bed, or you're taking the shower at the end of the day, and you're
[2525.56 --> 2530.22]  kind of relaxing from all the things you've been doing. Where does your mind go on this? Like,
[2530.28 --> 2536.74]  what are the what are the possibilities that you're excited about over over the next few years? And
[2536.74 --> 2542.06]  what's and what do you think might be possible that that isn't today? If you just kind of share
[2542.06 --> 2548.10]  your as a final thought, kind of your aspirations in this space, I'd really appreciate it.
[2548.10 --> 2554.06]  Yeah. And I think I'll go probably a little bit higher abstraction level and then tie it back here.
[2554.18 --> 2560.14]  I think going forward, what we're really excited about is the idea of having a digital set of
[2560.14 --> 2566.38]  employees or digital workforce to help the current workforce. And so we view going forward, the idea
[2566.38 --> 2572.22]  that we continue to have people doing great work at great companies, and then augmenting and improving
[2572.22 --> 2579.00]  that work with digital employees. And so in kind of that future view of the world where, say, we
[2579.00 --> 2583.52]  interact with these digital employees, either for simple things like retrieving information from
[2583.52 --> 2589.26]  complex systems across a company, just doing simple data analytics to maybe more complex things of being
[2589.26 --> 2594.80]  able to do, say, forecasting or helping predict things coming up in the future. I think there'll be a
[2594.80 --> 2599.86]  whole massive space around having these digital employees solve more complex tasks,
[2599.86 --> 2605.82]  and being able to either hire them or rent them across companies. You can imagine there are certain
[2605.82 --> 2610.16]  industries where people are experts in their domain. They might rent out digital employees to other
[2610.16 --> 2615.68]  companies who are building products with them as a dependency or with them as a partner. And so in
[2615.68 --> 2619.60]  kind of that future world of having all these digital employees or agents working together,
[2620.30 --> 2626.16]  we view backing into things like Nemotron, the idea of being able to improve the capabilities
[2626.16 --> 2631.94]  across single models, across many models, and across the ecosystem. All of that in the end helps
[2631.94 --> 2638.20]  us be able to get these more accurate and more productive digital employees. And there's a whole
[2638.20 --> 2643.36]  set of software that goes around just not just the model, but having multiple models work together.
[2643.74 --> 2647.88]  There's a whole nother set of challenges of as you have these digital employees that are based on
[2647.88 --> 2652.76]  these models, how do you keep them up to date? How do you ensure they stay current? They know the
[2652.76 --> 2656.86]  latest information about your business, if your supply chain changes, or if your inventory changes.
[2657.52 --> 2662.26]  And so there's opportunities there. We're looking at around data flywheels, where we have a set of
[2662.26 --> 2666.60]  software we published a month back called Nemo Microservices to help people take these digital
[2666.60 --> 2671.98]  employees and keep them current and recent on interactions, enterprise knowledge, and data changes
[2671.98 --> 2677.80]  over time. But I think going forward, we're really excited for that space because often there's a lot of
[2677.80 --> 2683.12]  difficult or mundane types of challenges and tasks today that prevent us from getting to the things
[2683.12 --> 2687.42]  we're more excited about or where we add more value. And I think we all can kind of relate to that in
[2687.42 --> 2691.92]  our day to day. And so I think going forward, we expect that these digital agents or employees will
[2691.92 --> 2697.04]  be able to help us significantly get past a lot of the mundane, repetitive things that we end up having
[2697.04 --> 2701.86]  to do because systems are hard or technology is hard or things haven't been built as well as they could.
[2701.86 --> 2706.80]  And then focus more on the more exciting places where we can move, move efforts forward, move
[2706.80 --> 2710.56]  businesses forward and contribute much more kind of the community and the economy.
[2711.06 --> 2716.52]  That's an amazing vision you have there. I love that. Thank you for sharing that. You've given me yet
[2716.52 --> 2723.06]  again, some more things to be thinking about as we as we finish up here. So I just wanted to thank you
[2723.06 --> 2728.72]  very much, Joey, for coming on to the show, sharing your insight and telling us about the new models that you
[2728.72 --> 2734.78]  got here. And I hope that you will come back when you have the next things that you might want to
[2734.78 --> 2737.34]  share and share them with our audience. Thank you very much.
[2737.72 --> 2739.08]  Yeah, sounds good. Thanks for having me.
[2746.02 --> 2750.08]  All right, that's our show for this week. If you haven't checked out our website,
[2750.08 --> 2756.42]  head to practicalai.fm and be sure to connect with us on LinkedIn, X or Blue Sky. You'll see us
[2756.42 --> 2760.52]  posting insights related to the latest AI developments, and we would love for you to
[2760.52 --> 2764.78]  join the conversation. Thanks to our partner, Prediction Guard, for providing operational
[2764.78 --> 2770.44]  support for the show. Check them out at predictionguard.com. Also, thanks to Breakmaster Cylinder
[2770.44 --> 2775.28]  for the beats and to you for listening. That's all for now. But you'll hear from us again next week.
[2775.28 --> 2780.74]  Lockdown
[2780.74 --> 2783.64]  because you're and your friend and your friend areенные.
[2783.64 --> 2784.52]  So I'll talk to you after joining us next week.
[2784.84 --> 2785.44]  Right now.
[2785.44 --> 2785.54]  Yeah.
[2785.54 --> 2786.32]  Right now.
[2786.32 --> 2786.96]  Take care.
[2786.96 --> 2787.32]  Okay.
[2787.32 --> 2788.84]  Bye now.
[2788.84 --> 2788.88]  Bye now.
[2791.92 --> 2791.98]  Bye now.
[2792.16 --> 2792.94]  Bye now.
[2792.94 --> 2794.16]  Bye now.
[2794.16 --> 2794.36]  Bye now.
[2795.28 --> 2796.34]  Thank you.
[2797.02 --> 2797.56]  Bye now.
[2797.56 --> 2799.28]  Bye now.
[2799.52 --> 2800.70]  Bye now.
[2800.88 --> 2801.64]  Bye now.
[2801.64 --> 2803.42]  Bye now.
[2803.42 --> 2803.74]  Bye now.
[2803.74 --> 2804.72]  Bye now.
[2804.72 --> 2805.26]  Bye now.
