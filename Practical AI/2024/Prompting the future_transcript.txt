[0.00 --> 8.66]  Welcome to Practical AI.
[9.16 --> 19.54]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.24 --> 24.92]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 --> 35.44]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents, so you can launch your app near your users.
[35.84 --> 37.84]  Learn more at Fly.io.
[42.58 --> 45.76]  Welcome to another episode of Practical AI.
[45.76 --> 59.64]  Hi, this is Daniel Whitenack. I am founder and CEO at Prediction Guard, and I am joined, as always, by my co-host, Chris Benson, who is a principal AI research engineer at Lockheed Martin.
[59.90 --> 60.64]  How are you doing, Chris?
[60.96 --> 62.76]  I'm doing fine. How's it going today, Daniel?
[63.12 --> 69.38]  It's going great. I'm pretty excited to prompt our guest today and hear what he has to say.
[69.38 --> 76.08]  We're joined today by the prompt master, Jared Zanerike, who is founder at PromptLayer.
[76.22 --> 76.90]  How are you doing, Jared?
[77.30 --> 79.90]  I am doing well. Excited for this.
[80.04 --> 80.96]  We're excited to have you.
[81.34 --> 89.76]  It seems like maybe from my perspective, there was kind of the release of all of this generative AI stuff,
[89.86 --> 97.90]  and then there was this realization that there's kind of a new skill needed around this thing called prompt engineering.
[97.90 --> 106.10]  And then it seems like some people have kind of like, I don't know if they've moved past the term or they've tried to develop other terms.
[106.18 --> 112.06]  I see other terms being developed around like AI engineering and such and as related to generative AI.
[112.26 --> 121.46]  So could you just give us a sense of like from your perspective, who, you know, is obviously building things for prompt engineering,
[121.46 --> 125.14]  maybe to start out kind of what is prompt engineering?
[125.14 --> 136.38]  And from your perspective, how have you seen it develop as a skill over the past year since people have been thinking a lot about prompting generative models?
[136.86 --> 142.20]  Yeah. The last year since the word was invented or maybe a little more than a year ago.
[142.54 --> 145.64]  But yeah, no, I think it's a really good question.
[145.64 --> 152.10]  I think this question of what does prompt engineering even mean is also a good question.
[152.62 --> 154.74]  And I think I'll tell you how we think about it.
[155.38 --> 160.06]  So honestly, so for PromptLayer, we consider ourselves a prompt engineering platform.
[160.18 --> 164.92]  So we've really steered into this term that is kind of overloaded.
[165.14 --> 166.58]  We've embraced it for sure.
[166.58 --> 168.48]  And it was half by accident.
[168.84 --> 179.02]  And I would say half realizing it was kind of beneficial to us because the fact that it has no definition means anyone who's kind of getting into LLMs and getting into prompt engineering says,
[179.36 --> 181.28]  oh, there's a prompt engineering platform.
[181.54 --> 182.24]  Maybe I need that.
[182.40 --> 184.20]  And they don't even necessarily know what it is.
[184.24 --> 185.58]  So it kind of helps us a little bit there.
[185.92 --> 189.38]  I guess prompt engineering, I first started hearing that term.
[189.38 --> 198.76]  I'd say GPT-3 days, kind of a little bit before ChatGPT, maybe GPT-2, back when everyone was just using the OpenAI Playground.
[199.34 --> 203.62]  And you'd start to hear a little bit about prompt engineering and stuff like that.
[203.66 --> 204.46]  And it was kind of cool.
[204.56 --> 207.60]  But that was, I guess, the days before it clicked for everyone.
[208.20 --> 209.78]  Maybe you can call it that.
[210.12 --> 216.96]  Days before ChatGPT came out and before people really realized how much potential this technology has.
[216.96 --> 224.26]  So that was when I think prompt engineering first became a word and then kind of got even more, you know, scale.
[224.42 --> 230.06]  AI, I think, is famous for maybe the first one to publicly hire someone with a role, prompt engineer.
[230.80 --> 234.74]  And from there, we called their platform a prompt engineering platform.
[235.32 --> 240.10]  At the beginning, people brought a lot of people to us who had no idea what prompt engineering is.
[240.10 --> 250.36]  And kind of the definition we've started to roll with is, as a company, we consider prompt engineering to be the tuning of the inputs to the LLM.
[250.56 --> 252.74]  So the prompt is the main input.
[253.08 --> 256.12]  But it also includes what model are you using?
[256.56 --> 257.96]  What are your temperature?
[258.14 --> 259.52]  What are your other hyperparameters?
[259.52 --> 265.24]  But the whole process of prompt engineering to us is what goes in and what comes out.
[265.78 --> 282.78]  And that specifically is, and I can talk a little bit more about this if it's interesting, but specifically a little bit different to the MLOps definition or the standard machine learning definitions of hyperparameter tuning and standard traditional ML.
[282.78 --> 293.60]  And specifically, we call ourselves a prompt engineering platform and not an LLM ops platform for that reason, because I do think there is slightly a difference.
[293.74 --> 298.44]  So I don't know if I answered the question fully, but those are my thoughts on prompt engineering.
[299.22 --> 308.76]  As we all dived into it, like you talked about, you know, the open AI playground originally that I think everybody kind of dips their toe into first, at least before the chat GPT release days.
[308.76 --> 320.46]  With that, one of the things I discovered as other models started coming out was some of the skills I was developing for prompting did not always translate as I expected across to other models.
[320.62 --> 329.60]  Have you seen one of those things where every model had its own kind of variations of what seemed to work from a productivity and output standpoint?
[329.84 --> 330.88]  Any thoughts around that?
[330.98 --> 338.14]  Like, how do you guys see that with all these different models coming out and little variations across them in terms of how they respond?
[338.14 --> 341.38]  Yeah, that's for sure a good observation.
[341.62 --> 347.20]  I think it's become clear that each model, I mean, each model is made a little bit differently.
[347.46 --> 350.16]  So you have to talk to it a little bit differently.
[350.84 --> 356.36]  I think these differences are going to maybe get a little less significant over the future.
[356.36 --> 369.22]  You know, when I guess chat GPT came out and the big thing was if you were nicer to the model, you're going to get a better answer, maybe because stack overflow questions that are nicer, get better answers or something like that.
[369.22 --> 377.64]  And I think now you have people talking about, oh, if my grandma's going to die, you need to answer this or I'm going to tip you $100 if you answer this.
[377.90 --> 380.46]  These are all, I think, tricks that work today.
[380.76 --> 382.02]  They're not going to last forever.
[382.32 --> 383.90]  These are like little things people figure out.
[384.00 --> 389.04]  But the part you mentioned of talking to different models differently, I think, is not going away.
[389.18 --> 391.70]  These are a lot of these models are made very differently.
[391.70 --> 398.80]  Certainly, we think it's pretty conclusive now that we're not going to live in a world with an open AI monopoly of language models.
[399.10 --> 408.60]  I think just a week or two ago, I saw a good tweet like now we have Mistral, Claude, GPT-4 and a few others that are all really good.
[409.20 --> 411.20]  And they're all made somewhat differently.
[411.52 --> 412.88]  And there are intricacies.
[413.10 --> 419.12]  And I think our philosophy and what we talk to our users about regarding prompt engineering is think about it as a black box.
[419.12 --> 429.16]  It's almost helpful to be kind of a little bit naive and stupid here and not try to understand how an LLM works and just try to track the inputs to the outputs, if that makes sense.
[429.50 --> 440.12]  Have you found any difference from people that are coming maybe from a deep sort of like data science-y background where they like are overanalyzing everything?
[440.12 --> 449.80]  And then other people who are coming maybe from a not technical background, but they're maybe domain experts and they're getting into developing these prompts.
[450.34 --> 454.48]  Have you seen different struggles on each side of that spectrum?
[454.48 --> 475.90]  Because you have sort of this very interesting mix of people that are trying to be like prompt engineers, quote unquote, some of which I've kind of seen are very much just like non-technical domain experts who are really good at even like psychology and writing narrative instructions, you know, being articulate.
[475.90 --> 486.74]  And then you kind of have this other side, which is the data science side, and they're really into modeling and wanting to analyze all of the outputs and that sort of thing.
[486.92 --> 493.18]  So have you seen different struggles on both sides of that in terms of being effective prompt engineers?
[493.18 --> 498.04]  I think you put it well that there's kind of these two groups coming at LLMs.
[498.24 --> 509.78]  Traditionally, I mean, this is what makes LLMs so cool to me is that traditionally ML, traditional machine learning standard, like math and machine learning, kind of need a PhD.
[510.42 --> 513.30]  Maybe you don't need it, but a PhD is very helpful.
[513.90 --> 518.02]  It's intense how you're building these models, doing a lot by hand still.
[518.02 --> 521.18]  You're doing a lot of this tweaking by hand and traditional ML.
[521.76 --> 524.80]  And then OpenAI came out with this amazing API.
[525.14 --> 530.68]  And I've done a lot with DevRel in the past and hackathons and stuff like that and helping companies make APIs.
[530.84 --> 534.74]  And in my opinion, OpenAI's API, it's like the best docs I've ever read in my life.
[534.82 --> 535.50]  It's so simple.
[535.92 --> 537.76]  You just give it text and you get text out.
[538.36 --> 547.08]  And like you said, this kind of opened up this completely new technology that's just so much better than everything else to non-technical people.
[547.08 --> 550.78]  You don't need a PhD to be able to understand how to communicate.
[551.16 --> 565.18]  And I think it brings about this new skill set, which is prompt engineering, which, in my opinion, is kind of a mixture of communication and like being able to write succinctly, but also being able to think algorithmically.
[565.28 --> 567.82]  So I don't know the exact word for thinking algorithmically.
[568.20 --> 570.10]  I've heard Stephen Wolframs use that word.
[570.22 --> 571.76]  I like that way to talk about it.
[571.86 --> 573.70]  But kind of just a scientific method.
[573.70 --> 577.62]  Do you know how to think in terms of creating a hypothesis, trying it out, tracking it?
[577.68 --> 579.00]  Are you strategic about this?
[579.46 --> 581.88]  And I think it's the same challenge on both sides.
[582.00 --> 590.14]  I think some people try to overcomplicate it if you're coming from an ML background and you try to understand why a certain token gives you an output.
[590.62 --> 593.32]  And I almost think these things are getting more complicated, not less.
[593.54 --> 598.48]  You kind of just need to take the naive approach and say, hey, I'm just going to talk to it.
[598.54 --> 599.90]  I'm going to try to get the output I want.
[599.96 --> 601.60]  I'm going to keep trying stuff until it works.
[601.60 --> 623.44]  As someone who's used the APIs a lot, and you're talking about OpenAI being so good, so many folks listening to this may have only used things like the normal chat interfaces on each of the models when they've gone and tried them out or paid for a subscription for the top end and stuff and have never touched the APIs at all.
[623.44 --> 630.00]  Could you take a moment and just talk about what an API experience is like to someone who has done a lot?
[630.08 --> 632.64]  I'm kind of taking advantage of you as an expert in the area.
[633.02 --> 639.72]  Share that a little bit with listeners just so they kind of get the other side of that because not everybody, probably the vast majority of them don't.
[639.80 --> 642.74]  I'll explain in that just to sidetrack myself for a sentence.
[643.22 --> 647.32]  I think the fact that you used the word expert is so funny because it's such a new field.
[647.32 --> 648.94]  It's almost amazing.
[649.16 --> 652.60]  I tell everybody, you could become an expert in this thing very easily.
[652.92 --> 654.52]  Nobody really knows what's going on.
[654.94 --> 658.82]  You kind of just need to study for a week and you're an expert, which is a very unique place to be.
[659.14 --> 659.92]  But anyway.
[660.68 --> 665.04]  It makes it fun to be able to dive into something and get as deep as the leaders in the field.
[665.38 --> 666.46]  Yeah, 100%.
[666.46 --> 670.14]  And just to be on the cutting edge and know that nobody really knows what they're doing here.
[670.56 --> 672.66]  Some people do, but there's very few of them.
[672.66 --> 683.24]  So regarding the APIs, ChatTBT, the way I think about it and the way I usually explain it is it's basically a very thin wrapper on top of the API.
[683.40 --> 688.08]  Every time you talk to ChatTBT behind the scenes, it's using this LLM technology.
[688.32 --> 692.88]  It's sending your message and a little bit of a preamble before your message.
[692.88 --> 695.68]  And the preamble is basically, we can call it the prompt.
[695.86 --> 698.72]  And it's basically saying, hey, you're an AI assistant.
[698.88 --> 700.40]  Make sure to be helpful to the user.
[701.02 --> 702.50]  Maybe don't be controversial.
[703.04 --> 705.72]  You can use a calculator if you need, stuff like that.
[706.06 --> 707.62]  And then giving the user messages.
[707.88 --> 709.08]  And that's all it is.
[709.46 --> 714.22]  And the process of prompt engineering is how do you tweak that preamble?
[714.34 --> 719.48]  And how do you get it to respond in the way you want to respond by telling it what to do?
[719.66 --> 726.80]  When I talk about the API, I'm talking about the things OpenAI has exposed to let you build your own ChatTBT
[726.80 --> 729.20]  and let you build your own products on top of it.
[729.20 --> 734.88]  And I just think OpenAI has done, if you want to get started and you haven't touched these APIs today,
[735.42 --> 740.68]  the best, best thing to do is just go to OpenAI's docs and just read the getting started tutorial.
[741.08 --> 742.20]  It's really well done.
[742.46 --> 747.98]  And I think as someone who's running a developer tools company, I'll tell you how hard it is to write good docs.
[747.98 --> 751.26]  I think our docs, from my perspective, I think they should be much better.
[751.62 --> 757.14]  Other people say they're great, but there's always room for improvement and it's just a very hard thing to do.
[757.40 --> 758.76]  So that's where you should go.
[758.76 --> 769.88]  From your perspective, over the last year, as people have gotten into doing this practice of prompt engineering,
[770.46 --> 777.96]  have you generally seen people that are engaging with your platform be sort of more informed coming in?
[777.96 --> 787.86]  Like they've done that experimentation with ChatGPT or the APIs and they are like using words like few shot, whatever, blah, blah, blah, and like this stuff.
[788.02 --> 795.46]  Or is it still kind of like people coming in that say, I know, I think I need to have a prompt engineering platform,
[795.46 --> 798.20]  but I'm kind of don't know where to start.
[798.36 --> 801.40]  Have you seen that shift even over in this last year?
[801.40 --> 809.50]  I would say we're still very early in this and there's a few leaders, but everything's up for grabs in terms of AI products.
[809.76 --> 814.24]  I don't buy the whole notion of it's only the incumbents who are going to be able to use AI.
[814.42 --> 815.16]  There's so much.
[815.68 --> 818.64]  The AI products people are making today are just scratching the surface.
[819.16 --> 822.72]  Having said that, I have seen a bit of a change since we launched our product.
[822.82 --> 825.94]  We launched our product January of last year.
[826.08 --> 827.72]  So January of 2023.
[827.96 --> 830.94]  I guess that was a few months after ChatGPT came out.
[830.94 --> 834.66]  These things were, I think we were, I think we were the first prompt engineering platform.
[834.96 --> 838.58]  Maybe there's some argument there, but we were one of the first at least.
[839.28 --> 844.28]  And when we launched our product, we had a lot of indie hackers and individual hobbyists using our platform.
[844.40 --> 845.88]  That was the whole community back then.
[846.88 --> 848.28]  That lasted for a little.
[848.46 --> 850.82]  Then we kind of moved on to AI first startups.
[851.24 --> 853.52]  So like one or two person startups.
[853.72 --> 855.60]  These are like the really cutting edge ones.
[855.96 --> 857.00]  We used one of them.
[857.00 --> 860.60]  It's a great company to actually refactor our whole code base into TypeScript.
[860.94 --> 862.14]  A lot of really cool stuff.
[862.64 --> 869.52]  And then from there, I would say starting in the fall, and I've heard this from a few other founders in the space.
[869.86 --> 874.64]  It felt like there was starting to become a real shift where real companies.
[874.84 --> 883.10]  And when I say real, I mean maybe companies that actually make money started actually getting serious about AI and getting serious about LLMs.
[883.10 --> 892.60]  And I think we're still seeing that maturation continuing where these real teams are building AI products that they care about.
[892.76 --> 895.24]  And not just like Twitter demos are one thing.
[895.42 --> 905.44]  Promlayer is interesting for a Twitter demo, but Promlayer becomes really useful for a team that is serious about building their product and has multiple stakeholders and wants to collaborate.
[905.44 --> 909.82]  And so I am seeing that this shift is still happening.
[910.04 --> 914.94]  More and more companies are getting serious about their LLM products and getting value and revenue from them.
[915.26 --> 918.00]  But we're still at the very, very beginning of the curve.
[918.10 --> 919.70]  So a lot more to come.
[919.70 --> 925.34]  I think that was a great sort of intro into prompt engineering and the state of prompt engineering.
[925.66 --> 937.88]  I'm wondering if you could help us maybe understand, yes, it's good if people get hands-on with these models, kind of gain some intuition about how they behave and different ways that you prompt them.
[937.88 --> 948.30]  What is it about this discipline of prompt engineering that needs sort of systematic ways of managing your prompting methodologies?
[949.02 --> 955.84]  And how is that different to or the same as different sorts of engineering in the past?
[955.98 --> 959.12]  You know, we've always had version control and that sort of thing.
[959.32 --> 966.80]  What's kind of unique and not unique about this discipline of prompt engineering in terms of how you need to approach it systematically?
[966.80 --> 971.00]  Just starting from first principles, there's one fundamental thing that's changed.
[971.54 --> 975.70]  And it's that we're now building upon a probabilistic technology.
[976.08 --> 986.16]  So we're now building on a technology that sometimes gives us some answer, sometimes gives us another answer, and is trending to be more confusing on why it gives one answer and not less.
[986.58 --> 990.96]  And confusing, I mean, yes, theoretically, it is deterministic.
[991.08 --> 993.86]  You can really dive into the weights and maybe figure it out.
[993.96 --> 995.98]  But nobody's really practically going to do that.
[995.98 --> 1001.26]  It's virtually too hard for 99.9% of use cases with models.
[1001.72 --> 1005.78]  So we're at a place where you're working with a black box now.
[1006.00 --> 1010.62]  And yes, some servers, some architectures become black boxes because of bad code.
[1010.84 --> 1011.94]  But that's a different type of black.
[1011.98 --> 1013.42]  That's not a real black box.
[1013.54 --> 1014.86]  But we're building technology.
[1015.20 --> 1016.10]  That's the code I write.
[1016.58 --> 1018.02]  Yeah, me too.
[1018.22 --> 1020.56]  That's why I'm going to get banned from our repo soon.
[1020.56 --> 1026.18]  But yeah, so you're building technology on this black box.
[1026.18 --> 1028.98]  And you need to think about it differently.
[1029.30 --> 1032.36]  And I think this is a big philosophy we have at PromptLayer.
[1032.36 --> 1041.58]  I think we have the philosophy of we built a lot of great stuff in traditional software and traditional machine learning and had a lot of great learnings.
[1041.66 --> 1043.16]  Git is a fantastic tool.
[1043.62 --> 1044.90]  Version control is important.
[1045.38 --> 1046.76]  Access controls are important.
[1047.34 --> 1049.18]  Test-driven development is important.
[1049.18 --> 1053.40]  But do we necessarily want to take one-to-one of everything?
[1053.90 --> 1054.64]  Not really.
[1054.80 --> 1065.74]  I think the biggest difference between LLM-based development and building AI applications versus building standard software is who are the stakeholders?
[1066.24 --> 1067.74]  Like we were talking about earlier.
[1067.94 --> 1074.96]  Now you can have subject matter experts who are not necessarily software engineers, but rather these prompt engineers, these AI whispers,
[1074.96 --> 1081.52]  like these people who are able to talk to the black box and able to communicate with the AI, we could call it in a little sci-fi sense.
[1081.68 --> 1088.94]  But we have this new stakeholder in the process of software engineering who is not going to jump into the code and not going to jump into Git.
[1089.40 --> 1095.38]  And that's why, at least for PromptLayer, we've taken a very first principles ground up approach where we're saying,
[1095.38 --> 1102.30]  hey, what can we learn from normal software and how people work together on software and do version control and collaborate?
[1102.90 --> 1114.40]  And how can we take that into LLMs and bring in new stakeholders and bring in new collaborators and let people actually build on this black box technology in a systematic way?
[1114.78 --> 1116.28]  So hopefully that makes sense.
[1116.66 --> 1117.46]  It does.
[1117.46 --> 1118.36]  I'm curious.
[1118.44 --> 1126.68]  You said some things there that really kind of piqued my interest that you kind of were contrasting it with deterministic programming that we've all kind of grown up with.
[1126.82 --> 1130.48]  And now we're in this new age and we have these non-deterministic things.
[1130.54 --> 1135.62]  And you can give it the same prompt and it may or may not on any given day give you the same answer back.
[1136.02 --> 1141.02]  So how has that kind of fundamentally changed software development in general?
[1141.02 --> 1147.56]  And I'm encompassing all the things when I say software development, both the AI and the systems around it to feed it.
[1148.04 --> 1155.42]  Because when you're dealing with that potentially unexpected return and that non-deterministic black box that you're talking about,
[1155.82 --> 1163.18]  how do people handle that when they're trying to devise and say, hey, I want to use a model in the thing that I'm building?
[1163.72 --> 1165.82]  How do they change in the way they think about that?
[1165.82 --> 1174.36]  I don't know how people think, but I can tell you a symptom of how they think, which is we work with a lot of LLM teams, of course, because they're using our platform.
[1174.44 --> 1175.06]  And we talk to them.
[1175.18 --> 1178.34]  We're always trying to talk to people, trying to figure out what to improve.
[1178.44 --> 1187.38]  And one of the big pieces we've come to with the prompt layer is that the iteration cycle of prompt engineering is different than software engineering.
[1187.38 --> 1198.08]  So what I mean by that is your code deploys and continuous integration and that whole sort of thing is happening at a different cadence,
[1198.08 --> 1204.18]  almost always in mature software than prompt engineering, because there's a lot of reasons.
[1204.18 --> 1206.16]  Maybe you're updating the prompt frequently.
[1206.34 --> 1208.88]  Maybe, again, different stakeholders are updating the prompt.
[1208.88 --> 1213.56]  That's why we encourage people to have their prompts in a CMS or we call it a prompt registry.
[1213.90 --> 1216.92]  You can put it in a Postgres database, something like that.
[1217.30 --> 1222.28]  But you don't want to block your prompt engineering cycle on edge deployments.
[1222.28 --> 1230.52]  And that's, I think, the symptom of this new thought pattern of how you're building, let's call it black box software,
[1230.78 --> 1236.22]  and how you're kind of thinking through these problems where they are different problem sets also.
[1236.40 --> 1239.06]  They're not, you're not solving the same type of software problems.
[1239.18 --> 1244.76]  You're solving, let's call it language problems or things that can employ this new type of software.
[1245.62 --> 1251.50]  And so it's not just a different like way to build, but it's also a different way to think about it.
[1251.50 --> 1255.18]  And then we can also get into like, how do you code now?
[1255.32 --> 1256.22]  How that's different?
[1256.64 --> 1260.88]  And how I think maybe this is maybe a more contract.
[1260.98 --> 1265.66]  I don't like to predict things, because I think it's kind of a fool's errand.
[1265.84 --> 1269.46]  But if I had to predict one thing, I think as a lazy programmer,
[1269.72 --> 1275.64]  there's something really nice about just having a little block of LM do something for me.
[1275.64 --> 1281.88]  So for example, parsing strings or parsing chunks of text and reordering it.
[1282.24 --> 1284.82]  You can do that deterministically, and it'll probably be better.
[1285.32 --> 1288.98]  But there's probably a world where models are going to get cheap and quick enough,
[1288.98 --> 1294.24]  where maybe it's worth the engineering time not to build it well and just outsource it to AI.
[1294.60 --> 1296.46]  But maybe that's a whole different tangent.
[1296.46 --> 1308.52]  Yeah, and maybe you could get into a little bit of the implications of these prompts in a registry, right?
[1308.60 --> 1315.94]  Because you could have like these sort of random tasks that I don't know if you all saw the Devin thing
[1315.94 --> 1322.08]  that's been going around, where it's like a junior engineer agent that can, you know,
[1322.12 --> 1324.92]  write scripts and interact with software documentation.
[1324.92 --> 1328.62]  And today I was thinking about that similar to what you were saying, Jared.
[1328.76 --> 1337.34]  It's like, hey, well, I could go and take all of these strings and go and interact with the API
[1337.34 --> 1342.22]  to translate them into another language, which is what the task was that I was doing.
[1342.32 --> 1346.54]  Or I could just like say, hey, write a script that does this and do it for me.
[1346.64 --> 1347.78]  So there's those random things.
[1347.86 --> 1354.02]  But then there's another type of prompt, which as soon as you're starting to expose a system to end users,
[1354.02 --> 1364.34]  then small changes in the prompt, like on the back end could produce very different changes in the behavior to your actual end users
[1364.34 --> 1366.84]  and cause like actual, you know, problems.
[1367.24 --> 1372.30]  So could you talk a little bit about maybe the implications of changes in your prompts
[1372.30 --> 1375.22]  and like best practices that you found around?
[1375.78 --> 1379.82]  I know we're talking a lot about prompt versioning and registries around those prompts.
[1379.88 --> 1385.06]  And I know that prompt layer is thinking about more than that around evaluation and other things.
[1385.20 --> 1392.40]  But yeah, maybe before we go to those other things, could you talk about what you've seen in terms of how people are managing these different prompts?
[1392.40 --> 1397.28]  Some that have very low risk in terms of changing them very often,
[1397.28 --> 1403.42]  and maybe some that have actually a large risk in terms of maybe small changes in the prompt.
[1403.78 --> 1409.16]  Yes. I think there's a life cycle here for how you care about your prompt.
[1409.38 --> 1417.60]  And I think every prompt in any mature product and any, if you have a product, an AI product that's making your company $10 million a year,
[1417.60 --> 1421.40]  or something like that, you're going to care about any change to it.
[1421.76 --> 1423.22]  And I think there's that cycle.
[1423.28 --> 1425.02]  So let's say that's the end stage.
[1425.36 --> 1429.12]  At the beginning, you probably are just going to ship any prompt.
[1429.18 --> 1430.00]  You're just going to write a prompt.
[1430.30 --> 1431.34]  It's going to kind of work.
[1431.52 --> 1432.90]  You're going to try it once or twice.
[1433.36 --> 1434.22]  Say, all right, good enough.
[1434.38 --> 1435.62]  Let's get the MVP out.
[1435.88 --> 1438.66]  In that case, maybe the prompt is in your code.
[1438.82 --> 1443.82]  Maybe you don't care so much about what you were just saying about like updating, having a breaking change.
[1443.94 --> 1444.40]  All right, whatever.
[1444.46 --> 1445.14]  I got to get it out.
[1445.22 --> 1446.50]  Let me get five people using it.
[1446.50 --> 1448.44]  All right, so you've done that.
[1448.74 --> 1449.50]  What's next?
[1449.70 --> 1453.00]  You probably now have like five different prompts on your system.
[1453.32 --> 1454.28]  They're scattered everywhere.
[1454.42 --> 1460.60]  I was just talking to a founder who was visiting us, our office today, who actually had this exact same story.
[1461.18 --> 1464.06]  And then he moved all his prompts to a text file.
[1464.64 --> 1468.56]  Or actually, in this case, it was just like a .ts file on his system.
[1469.08 --> 1471.00]  So now you have your prompts in one place.
[1471.34 --> 1472.06]  That's the next step.
[1472.16 --> 1473.36]  But it's still in your code base.
[1473.42 --> 1475.00]  It's still linked to EngDeploys.
[1475.00 --> 1480.58]  And like you said, you still have no way of knowing if you push a new one, what happened?
[1480.72 --> 1482.86]  Like, is it breaking 20% of our use cases?
[1483.62 --> 1484.38]  Not great.
[1484.88 --> 1490.64]  But I would call this stage, I like this word for it, like vibe-based prompt engineering.
[1490.64 --> 1494.50]  So this is the five-based prompt engineering stage where you're kind of writing a prompt.
[1494.86 --> 1496.14]  You're testing it in the playground.
[1496.30 --> 1497.14]  You're doing it once or twice.
[1497.14 --> 1498.02]  And you're just judging.
[1498.22 --> 1499.36]  Like, you're just looking.
[1499.44 --> 1500.56]  Okay, yeah, it's pretty good.
[1501.12 --> 1502.28]  This lasts a little bit.
[1502.48 --> 1509.40]  The time when this is no longer good enough is usually when your product's either getting to a greater level maturity.
[1509.40 --> 1511.04]  Maybe you're rolling it out to GA.
[1511.54 --> 1514.40]  Or you're adding more stakeholders to the team.
[1515.00 --> 1516.30]  Maybe you're adding a PM.
[1516.62 --> 1522.68]  Maybe you're adding a content writer or a subject matter, like we were talking about earlier, a psychologist or a lawyer or something like that.
[1523.00 --> 1524.40]  And you need more people involved.
[1524.40 --> 1532.34]  So now you have a non-technical person writing your prompts who isn't really capable of building out the whole dev workflow to test it out.
[1532.72 --> 1535.34]  You really want to, like, make sure it doesn't break everything.
[1535.50 --> 1541.00]  So there's a few things I've seen people, a few strategies I've seen people employ here.
[1541.24 --> 1543.70]  One is, of course, traditional software.
[1543.88 --> 1544.80]  Let's borrow some stuff.
[1544.96 --> 1545.56]  A-B testing.
[1546.08 --> 1548.22]  Let's release it for some people.
[1548.22 --> 1554.72]  If we're monitoring user feedback, maybe if users are giving us a thumbs up, thumbs down, we should be able to see it pretty quickly.
[1555.48 --> 1560.76]  Also, having prod, staging, dev staging, different, like, we call them release labels.
[1561.16 --> 1562.02]  A lot of words for them.
[1562.52 --> 1564.40]  Let's call that category slow releases.
[1564.90 --> 1565.68]  So that's one way.
[1566.08 --> 1567.96]  Then there's two other big ways of solving it.
[1568.24 --> 1569.78]  Second way, regression tests.
[1570.16 --> 1573.12]  So, again, another concept borrowed from software engineering.
[1573.12 --> 1579.12]  Let's find cases where it's failing and see if we succeed in this test case.
[1579.48 --> 1583.34]  Third, which is also kind of like regression tests, I guess, is backtesting.
[1583.96 --> 1587.40]  Let's just run it on old examples and see if it changes.
[1587.58 --> 1595.24]  I think in a lot of LLM use cases, the really hard part about this problem is that you don't know what the ground truth is.
[1595.44 --> 1596.60]  Let's say we're making a summary.
[1597.06 --> 1598.88]  There's no correct answer to a summary.
[1599.00 --> 1600.26]  There's a good summary, a bad summary.
[1600.26 --> 1603.62]  It's almost very hard to understand if it is good or bad.
[1604.08 --> 1611.34]  We actually, there's a user of ours that is doing this exactly, and they're trying to figure this out, and they're using a combination of human graders and whatnot.
[1611.50 --> 1612.98]  But we can talk more about that in a second.
[1613.18 --> 1621.38]  But in this case, often the best thing to do is just rerun it on old responses and see how much changed.
[1621.76 --> 1626.50]  And, oh, I updated the prompt and 50% of my responses changed.
[1626.92 --> 1628.32]  Maybe I should look into those.
[1628.32 --> 1630.92]  Oh, only like one out of a thousand changed.
[1631.36 --> 1632.24]  Probably good enough.
[1632.32 --> 1635.28]  So it's all about trade-offs in this world.
[1635.38 --> 1637.68]  And everything's, again, it's a new way of thinking.
[1637.86 --> 1638.70]  It's non-deterministic.
[1638.88 --> 1640.38]  So how do you trade off?
[1640.46 --> 1644.54]  How much it's changing versus how much you need to make sure it doesn't change?
[1644.88 --> 1649.32]  Maybe you want to force a specific output that is deterministically graded.
[1649.68 --> 1652.62]  So, for example, you're giving a JSON or a Boolean output.
[1652.62 --> 1655.14]  So there's a lot of strategies here.
[1655.60 --> 1667.40]  But if I were to kind of give it a one-line answer, you should be deciding at what cadence you update prompts, by what stage your product is at, and how bad these issues are going to be.
[1667.40 --> 1693.56]  So, you know, when we started podcasting back in 2009, an online store is just the furthest thing from our minds.
[1693.56 --> 1700.90]  Now we have merch.changelog.com, and you can go there right now and order some T-shirts, and that's all powered by Shopify.
[1701.30 --> 1704.52]  It's so easy, all because Shopify is amazing.
[1705.36 --> 1710.66]  Shopify is the global commerce platform that helps you sell at every stage of your business.
[1710.66 --> 1721.00]  From the launch your online shop stage to the first real-life store stage, all the way to the did we just hit a million-dollar stage, Shopify is there to help you grow.
[1721.52 --> 1730.26]  Whether you're selling security systems or marketing memory modules, Shopify helps you sell everywhere, from their all-in-one e-commerce platform to their in-person POS system.
[1730.72 --> 1733.96]  Wherever and whatever you're selling, Shopify has got you covered.
[1733.96 --> 1746.86]  Shopify helps you turn browsers into buyers with the internet's best converting checkout up to 36% better compared to other leading commerce platforms, and sell more with less effort thanks to Shopify Magic, your AI-powered all-star.
[1747.24 --> 1757.24]  You know, nothing gets me and Jared more excited than when our guests get that coupon code in their email when their show ships, or to everyone out there who loves Change Law Podcasts.
[1757.24 --> 1761.60]  You can go to merch.changelog.com and get your favorite threads to support our podcasts.
[1761.60 --> 1765.68]  It is just the best thing ever, from stickers to threads.
[1766.10 --> 1768.76]  All that is at merch.changelog.com.
[1769.14 --> 1784.88]  And did you know that Shopify powers 10% of all e-commerce in the U.S., and Shopify is the global force behind Allbirds, Rothy's, and Brooklinen, and millions of other entrepreneurs of every size across 175 countries.
[1784.88 --> 1791.48]  Plus, Shopify's extensive help resources are there to support you and your success every step of the way.
[1791.60 --> 1794.52]  Because businesses that grow, grow with Shopify.
[1794.94 --> 1802.26]  Sign up for a $1 per month trial period at shopify.com slash practicalai, all lowercase.
[1802.26 --> 1809.56]  Go to shopify.com slash practicalai now to grow your business no matter what stage you're in.
[1809.82 --> 1813.12]  Again, shopify.com slash practicalai.
[1813.12 --> 1839.90]  If you're looking at like a large, out on the edge system of systems,
[1839.90 --> 1846.02]  in the sense of you have a number of models deployed and they all do specific things.
[1846.02 --> 1848.12]  And some of them are generative and some are not.
[1848.24 --> 1853.84]  And for the generative ones, they may be trying to address very specific functions that they're doing.
[1854.20 --> 1861.20]  With a system like that, you've got it in production and maybe you've done kind of that minimal viable product approach on getting it up.
[1861.20 --> 1867.60]  But when you get things to where they're kind of stable in production, you are starting to kind of address some of that.
[1867.72 --> 1877.98]  I know that I'm grappling in my own head with like how to think about being able to make those tweaks and changes to prompts in any given model in the system and detect that.
[1877.98 --> 1880.66]  Is there like a best place for me to start?
[1880.82 --> 1885.52]  Because I'm still trying to kind of grapple with the larger picture and really understand it.
[1885.98 --> 1890.82]  And so if I want to change something, but I don't want to impact the larger stable system,
[1891.44 --> 1897.52]  what would you kind of be like if it was you in that position, like one, two, three, try this, try that, try that,
[1897.52 --> 1901.04]  just to give me a good hands-on takeaway from that.
[1901.18 --> 1905.08]  And I apologize for the selfish nature of the question, but it's hard to do that.
[1905.08 --> 1916.50]  No, I think it's good to have the selfish type of question here because one thing that I actually think a lot of people get wrong in this space is that every prompt is kind of different.
[1916.82 --> 1924.82]  And the answer to this question is really very unique to what you're actually trying to do and the task you're trying to solve.
[1924.94 --> 1928.50]  There isn't really, I mean, a lot of people are trying to sell it.
[1928.80 --> 1933.98]  So I like to say that maybe I'll change my opinion in a month or a week or a day.
[1933.98 --> 1935.92]  I do that all the time as I learn more.
[1936.06 --> 1937.36]  So no worries.
[1937.52 --> 1938.30]  You're allowed to.
[1938.42 --> 1939.64]  It's good to change your opinion.
[1939.64 --> 1949.10]  But right now, I think a lot of these eval sets that people produce are not that useful for building real products
[1949.10 --> 1958.56]  because you're trying to evaluate your prompt for your real application, not for some pie in the sky financial data set or something like that.
[1958.56 --> 1963.04]  But having said that, I think the first question to ask, and maybe we'll use this example.
[1963.84 --> 1965.62]  So I would modularize it.
[1965.72 --> 1967.24]  I would think about it on the prompt level.
[1967.90 --> 1969.10]  So I guess there's two ways to think about it.
[1969.12 --> 1971.94]  We could think about modular tests and then end-to-end tests.
[1972.34 --> 1973.20]  We should be doing both.
[1973.58 --> 1975.90]  For this case, do we have a ground truth?
[1976.20 --> 1977.68]  I think is the first question I'd ask.
[1977.90 --> 1982.00]  Is there an ability to make a data set with ground truths that we can compare to?
[1982.00 --> 1985.32]  Or is it like a summary type example where there's no answer?
[1985.74 --> 1989.26]  In the case that I'm looking at, I think you could establish ground truth.
[1989.36 --> 2001.12]  I don't know it would be easy, but you probably could because you could bypass what you're seeing and you could have a human kind of assess what the generative AI model was trying to assess as well.
[2001.34 --> 2006.96]  So you could get a ground truth that is a human analysis of it as a proxy.
[2007.32 --> 2007.52]  Excellent.
[2007.86 --> 2010.52]  So your life is now 10 times easier.
[2010.52 --> 2012.42]  That's always good.
[2012.82 --> 2013.74]  It is great.
[2013.86 --> 2014.08]  Yes.
[2014.48 --> 2023.32]  Step one is whether you do it yourself, whether you hire some people on Enterk or QA or however you do it.
[2023.76 --> 2025.10]  Step one is kind of build.
[2025.30 --> 2026.14]  It doesn't have to be built.
[2026.86 --> 2033.40]  Build a small data set and try to get into this method of test-driven prompting or eval-driven prompt engineering.
[2033.78 --> 2035.12]  I don't know if we have a word for it yet.
[2035.20 --> 2036.36]  Maybe we need to define one.
[2036.36 --> 2046.08]  But try to build some sort of metric we can evaluate our test on so you don't have to be just one by one trying these examples out.
[2046.08 --> 2056.76]  So what I mean by this is build a, let's say 10, let's say 15, let's say a hundred, whatever it is, depending on the use case of input variables to your prompt.
[2056.76 --> 2061.80]  So your prompt is probably having a, your task is to do this.
[2061.88 --> 2063.04]  Here's this data.
[2063.42 --> 2063.76]  Blah, blah.
[2063.76 --> 2065.98]  So the data is an input variable in that case.
[2066.12 --> 2070.94]  And then get a human to give you the output and then start every time you test the prompt.
[2071.34 --> 2072.22]  Let's run it on that.
[2072.44 --> 2077.14]  Over time, we can, let me, I could talk about over time how to make that better, but does that make sense?
[2077.66 --> 2078.10]  It does.
[2078.22 --> 2078.64]  It does.
[2078.96 --> 2085.96]  The thing I'd add is over time, how you make that better is you start connecting that back with real data and how your users use it.
[2085.96 --> 2099.46]  So again, you can make your life 10 X easier if you have good user feedback and a way to know if the production inference, if the production LLM run actually worked or not.
[2099.46 --> 2101.38]  So user feedback is a way to do that.
[2101.46 --> 2103.26]  Say a user gives you a thumbs up, thumbs down.
[2103.72 --> 2108.14]  Now you can take all those thumbs ups, thumbs down, make a new data set out of that.
[2108.22 --> 2113.22]  And now, now you're really going and now you're building this whole feedback loop.
[2113.22 --> 2121.46]  And I think I'll say like our biggest goal with PromptLayer, our MO, is to shorten the prompt engineering feedback loop.
[2121.54 --> 2124.24]  I think that's what everything boils down to in this world.
[2125.26 --> 2132.92]  Maybe along with that element of feedback, I'm wondering if you can talk a little bit because we've talked a lot about evaluation, prompt versioning.
[2133.28 --> 2140.48]  There's the other element of this, which I know you all are thinking about deeply, which is sort of logging and monitoring.
[2140.48 --> 2163.34]  And there's certainly cases where, oh, I have this chain of LLM processing or even loops that could happen like, you know, LLM as a judge or something that kind of or critic kind of elements of LLM prompts that actually could loop until something happens or a certain number of times.
[2163.34 --> 2173.14]  And the way that you develop your prompts, both in terms of their length, in terms of how effective they are, could drastically impact your latency of processing.
[2173.50 --> 2181.82]  It could impact your cost in terms of how much text you're putting into models, especially if they're charging you for how much text you're putting in.
[2182.40 --> 2182.86]  So, yeah.
[2182.92 --> 2192.66]  Could you talk a little bit about maybe the highlights of some kind of best practices around logging and monitoring and how you think about that at PromptLayer?
[2192.66 --> 2193.26]  Yes.
[2193.92 --> 2205.42]  So I think, not to sound like a broken record here, but the thing I like to, or I go back to a lot is everything is use case dependent.
[2205.74 --> 2209.32]  So you brought up that some people are very concerned about latency.
[2209.72 --> 2211.32]  Some are very concerned about cost.
[2211.82 --> 2213.92]  I know teams that are concerned about neither of those.
[2214.12 --> 2217.24]  And their only concern is, are we getting the right answer?
[2217.54 --> 2219.76]  For example, code generation type startups.
[2220.28 --> 2221.78]  A lot of times latency doesn't matter.
[2221.78 --> 2222.78]  You're giving them a task.
[2223.16 --> 2225.44]  Hey, again, in our case of PromptLayer.
[2225.58 --> 2231.94]  Hey, can you, we worked with a company called Grit, where we said, can you move our whole code base into TypeScript?
[2232.46 --> 2233.24]  It could take a week.
[2233.28 --> 2233.72]  I don't care.
[2233.72 --> 2235.84]  So latency and costs don't matter to them.
[2236.06 --> 2240.16]  But then there's a lot of other cases where most cases probably latency costs matter.
[2240.16 --> 2246.86]  So in that case, or in either case, why logging is important here is just debugging.
[2247.10 --> 2252.32]  Honestly, I'll be honest, logging and observability is kind of the most boring part of our platform.
[2252.58 --> 2256.66]  Not because it's not useful, but because it's obvious.
[2256.66 --> 2258.66]  I think we started with observability.
[2258.82 --> 2264.56]  This is table stakes to shortening that feedback loop and that high-level goal.
[2264.68 --> 2266.98]  This is table stakes because you need to collect the data.
[2267.08 --> 2272.58]  You need to collect the data to build these evals, to see when it's not working, to be able to triage issues.
[2272.82 --> 2276.70]  Say someone, one of your users tells you, hey, I got a weird error.
[2276.92 --> 2278.02]  This happened to me, actually.
[2278.04 --> 2280.42]  I was using superhuman AI, and it didn't work.
[2280.70 --> 2281.88]  And I told them about it.
[2281.88 --> 2285.20]  I said, I got like a weird output, maybe you guys want to debug it.
[2285.60 --> 2288.18]  And they asked me what prompt I gave it to do the output.
[2288.30 --> 2288.92]  I don't remember.
[2289.12 --> 2290.32]  Don't you have a logging system?
[2290.46 --> 2291.46]  Maybe you should use PromptLayer.
[2292.18 --> 2297.98]  And they, but yeah, you should be able to figure out why something broke.
[2298.06 --> 2303.16]  You should be able to step through, step by step into the chain, see which version of the prompt it used.
[2303.16 --> 2305.66]  Maybe you have multiple versions in production.
[2305.66 --> 2312.48]  And our logging is just logs each request and lets you integrate it with metadata, like user information.
[2313.32 --> 2324.38]  It's one thing to like log a bunch of things, but like, let's say that I want to improve latency or cost or something like that.
[2324.38 --> 2330.82]  And I maybe have like 17 different prompts that I'm using across my system.
[2331.34 --> 2346.92]  How have you learned how to present that information to users so that they can kind of, especially from a, you mentioned kind of the skill of prompt engineering, having this algorithmic thinking kind of piece to it.
[2346.92 --> 2354.46]  But there's also a lot of people, you know, there's coming in, maybe that's the part of their brain that they're building up and they're bringing in these other skills with them.
[2354.58 --> 2363.94]  So how have you found it useful to present this sort of information to people to give them the right sorts of feedback along their kind of journey of optimizing things?
[2364.78 --> 2369.80]  So I think latency and cost are the easiest things to figure out.
[2369.80 --> 2376.80]  They're the easiest metrics you get out of the box when you're doing prompt engineering, because you're always getting latency and cost.
[2377.34 --> 2380.02]  The harder metrics is, is my answer correct?
[2380.58 --> 2382.70]  Is it rude to me?
[2382.86 --> 2383.60]  Is it mean?
[2383.90 --> 2385.36]  Is it, does it have ATI?
[2385.70 --> 2386.08]  I don't know.
[2387.10 --> 2389.44]  Are you Microsoft Bing releasing?
[2389.96 --> 2392.74]  We have a, we did a prompt engineering tournament last night.
[2392.82 --> 2397.12]  The first round was, can you avoid a PR disaster like Microsoft Bing?
[2397.12 --> 2403.30]  But that's the hard part is making sure your answer doesn't go off the rails or isn't wrong.
[2403.58 --> 2412.26]  But latency and cost and those type of logging, like base level logging specific things, those are the attractable metrics.
[2412.46 --> 2415.64]  So we give you latency and cost for each prompt template.
[2415.82 --> 2418.60]  We give you it broken down based on version.
[2419.02 --> 2424.86]  And then we also have a full analytics page that actually we revamped the other week for one of our customers who,
[2424.86 --> 2430.74]  they were going to have to build out their whole, like a whole BI dashboard, because I think something about their,
[2431.32 --> 2436.42]  either the founders of the company or the investors were worried about some users spending too many credits.
[2436.42 --> 2439.96]  So we kind of revamped our analytics page to just save them some time there.
[2440.08 --> 2444.00]  So you can use our analytics page to see which prompt templates are costing you the most,
[2444.08 --> 2445.72]  which users are costing you the most.
[2445.84 --> 2448.28]  Maybe if you're segmenting things to prod,
[2448.96 --> 2454.30]  maybe you're segmenting based on geo and just kind of filtering down based on that sort of thing.
[2454.30 --> 2458.72]  I want to ask a question as you have kind of pioneered this whole space,
[2458.86 --> 2463.10]  jumping into prompt engineering, quite honestly, before anyone really knew what it was,
[2463.12 --> 2467.12]  as you pointed out earlier, and you've been building out this capability.
[2467.68 --> 2472.74]  As you look to the future and, you know, the future is changing so rapidly right now.
[2472.82 --> 2476.86]  You know, we're all in this massive acceleration of things coming out.
[2476.96 --> 2480.52]  You know, Daniel and I every week are trying to figure out of all the things happening,
[2480.62 --> 2481.92]  what do we actually talk about?
[2481.92 --> 2486.10]  You know, it's getting harder, whereas it used to be there was something that happened last week,
[2486.22 --> 2487.38]  and we'll talk about it.
[2487.44 --> 2488.26]  Now there's so many.
[2488.74 --> 2494.32]  As you're operating a business in this, you know, kind of intense, increasing environment,
[2494.94 --> 2497.94]  where do you think this is going from a prompt engineering standpoint?
[2498.20 --> 2502.74]  What will prompt engineering become as we become increasingly multimodal
[2502.74 --> 2506.50]  and, you know, all the fantastic things that are happening on a weekly basis?
[2506.50 --> 2511.92]  I would imagine that would be fairly hard to try to plan ahead on, you know,
[2511.96 --> 2515.58]  where the industry is going and the technology and where to put your business.
[2515.80 --> 2516.92]  How do you see the future?
[2517.04 --> 2520.22]  What's the next one year, two year, five years in your head look like?
[2520.62 --> 2522.22]  That's a billion dollar question, right?
[2522.86 --> 2524.46]  I think we try to do two things.
[2524.52 --> 2527.88]  We try to not predict the future because it's too hard.
[2527.88 --> 2535.62]  And we try to build something useful that is built on first principles that makes sense.
[2535.90 --> 2540.66]  And I think that's how we try to stay ahead of the curve there a little bit.
[2540.74 --> 2542.34]  So I can give you some examples.
[2542.52 --> 2548.24]  So, for example, kind of just the whole process of iterating, of testing.
[2548.84 --> 2553.04]  For evals, we procrastinated a little bit on building that part of our platform.
[2553.18 --> 2554.72]  We always knew we needed it.
[2554.72 --> 2558.00]  Like, it's been the buzzword in the industry for like six months now.
[2558.40 --> 2561.76]  But we really wanted to know how to build that correctly.
[2562.14 --> 2567.04]  And I think we spent a lot of time talking to a lot of teams and saying,
[2567.12 --> 2568.24]  how do you do evals today?
[2568.62 --> 2572.88]  And every team we spoke to did it in their own way, in a Google spreadsheet,
[2573.68 --> 2575.84]  building out some weird, unique things.
[2575.84 --> 2579.96]  So our eval product, if you try it out, it looks like a spreadsheet for that reason.
[2579.96 --> 2585.86]  And it's very much inspired by the robustness of a Microsoft Excel type product,
[2585.96 --> 2590.16]  where it seems very simple, but you can take it in a lot of different ways.
[2590.28 --> 2598.42]  So I think we are trying to become future-proof by avoiding taking strong opinionated wins.
[2598.56 --> 2602.54]  We want to support best practices and build best practices for the community,
[2602.66 --> 2603.90]  especially in a space like this.
[2603.90 --> 2608.56]  But we want to do it without pigeonholing people into different ways of doing things.
[2608.80 --> 2612.34]  And I think it's been funny seeing how people, like the hive mind,
[2612.42 --> 2614.78]  has changed their opinion on what the future is.
[2615.12 --> 2620.62]  I remember we were, a year ago, we were talking to, like, investors,
[2621.20 --> 2624.98]  obviously not the investors that are on our team right now.
[2624.98 --> 2629.88]  And there were investors like, oh, prompt engineering, AGI is just going to take over.
[2630.02 --> 2631.82]  We're not going to have any infrastructure anymore.
[2632.38 --> 2634.24]  And a lot had that opinion.
[2634.64 --> 2637.22]  I don't think many have that opinion anymore, let's just say.
[2637.46 --> 2640.94]  And I think it's very obvious to us, and it's been obvious to us,
[2641.06 --> 2645.04]  that prompt engineering is the process of giving inputs to the LLM
[2645.04 --> 2647.00]  and choosing which model you're using.
[2647.34 --> 2653.08]  And even with the most advanced LLM ever, let's say the LLM is as advanced as a human.
[2653.08 --> 2655.94]  You still have to tell a human what you want.
[2656.22 --> 2659.42]  You still have to tell the intern what task you want him to do.
[2660.04 --> 2661.64]  And that's prompt engineering.
[2661.96 --> 2664.82]  And there's always going to be a process of inputs there.
[2665.02 --> 2668.68]  So that's how we think about the future and lack thereof.
[2669.58 --> 2673.42]  Jared, thank you so much for coming on to share your insights today.
[2673.98 --> 2678.72]  We definitely appreciate that you and the team at PromptLayer
[2678.72 --> 2680.70]  are thinking deeply about these things
[2680.70 --> 2683.56]  and building really good tools to support the community.
[2684.06 --> 2687.92]  And I encourage everyone in the audience to check out the show notes,
[2688.34 --> 2691.06]  follow the links, find out more about PromptLayer
[2691.06 --> 2692.46]  and the cool stuff that they're doing.
[2692.62 --> 2695.84]  And I hope we can have you back on the show in another year
[2695.84 --> 2699.88]  when I'm sure prompt engineering will look very different than it does now.
[2700.22 --> 2701.76]  But thank you so much for joining, Jared.
[2701.82 --> 2702.40]  It's been a pleasure.
[2703.00 --> 2704.12]  Yes, thank you for having me.
[2704.20 --> 2704.90]  This has been fun.
[2704.90 --> 2713.10]  All right.
[2713.44 --> 2715.86]  That is Practical AI for this week.
[2716.60 --> 2717.70]  Subscribe now.
[2717.88 --> 2722.86]  If you haven't already, head to practicalai.fm for all the ways.
[2723.26 --> 2726.44]  And join our free Slack team where you can hang out with Daniel,
[2726.70 --> 2729.24]  Chris, and the entire ChangeLog community.
[2729.24 --> 2734.48]  Sign up today at practicalai.fm slash community.
[2735.08 --> 2737.74]  Thanks again to our partners at fly.io,
[2738.16 --> 2740.88]  to our Beat Freaking Residence, Breakmaster Cylinder,
[2741.14 --> 2742.02]  and to you for listening.
[2742.36 --> 2744.12]  We appreciate you spending time with us.
[2744.48 --> 2745.66]  That's all for now.
[2745.96 --> 2747.58]  We'll talk to you again next time.
[2747.58 --> 2747.64]  Bye.
[2747.64 --> 2747.70]  Bye.
[2747.70 --> 2747.74]  Bye.
[2747.74 --> 2747.78]  Bye.
[2747.78 --> 2747.80]  Bye.
[2747.80 --> 2747.84]  Bye.
[2747.84 --> 2748.30]  Bye.
[2748.30 --> 2748.78]  Bye.
[2748.78 --> 2749.78]  Bye.
[2749.78 --> 2749.84]  Bye.
[2749.84 --> 2750.78]  Bye.
[2750.78 --> 2751.78]  Bye.
[2751.78 --> 2751.84]  Bye.
[2751.84 --> 2751.86]  Bye.
[2751.86 --> 2752.28]  Bye.
[2752.28 --> 2752.84]  Bye.
[2752.84 --> 2752.88]  Bye.
[2752.88 --> 2753.84]  Bye.
[2753.84 --> 2753.88]  Bye.
[2753.88 --> 2754.88]  Bye.
[2754.88 --> 2754.92]  Bye.
[2754.92 --> 2754.96]  Bye.
[2754.96 --> 2755.92]  Bye.
[2755.92 --> 2756.88]  Bye.
[2756.88 --> 2756.92]  Bye.
[2756.92 --> 2757.92]  Bye.
[2757.92 --> 2757.96]  Bye.
