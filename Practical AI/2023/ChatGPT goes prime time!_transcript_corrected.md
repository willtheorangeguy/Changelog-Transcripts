[0.00 → 22.12] It's a three-step process. So you pre-train a language model, then you gather this sort of human preference data and train a reward model. Now, the second reward model is trained to take in a prompt and a response and score it like a human would score it according to preference.
[22.12 → 29.72] So it's actually trained on the human preference data, and it outputs a prediction of what a human preference might be on this output.
[30.08 → 42.90] The third and final step is that you fine-tune a copy of your original language model using this trained reward model and a reinforcement learning loop.
[52.12 → 61.24] Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive, and accessible to everyone.
[61.58 → 66.38] Subscribe now if you haven't already. Head to practicalai.fm for all the ways.
[66.76 → 74.54] Special thanks to our partners at Vastly for delivering our shows superfast to wherever you listen. Check them out at fastly.com.
[74.54 → 83.10] And to our friends at fly.io. We deploy our app servers close to our users and you can too. Learn more at fly.io.
[89.28 → 94.16] Welcome to another fully connected episode of the Practical AI podcast.
[94.66 → 100.60] These episodes are where Chris and I keep you fully connected with everything that's happening in the AI community.
[100.60 → 109.42] We'll take some time to discuss the latest AI news and then dig into some learning resources to help you level up your machine learning game.
[109.88 → 113.82] I'm Daniel Whiten ack. I'm a data scientist with SIL International.
[114.16 → 119.76] And I'm joined as always by my co-host Chris Benson, who is a tech strategist at Lockheed Martin.
[120.00 → 120.66] How are you doing, Chris?
[120.90 → 125.56] Doing very well. Happy New Year 2023. This is our first conversation.
[125.56 → 131.20] Yeah. Happy New Year. This is the first one we're recording in the year 2023.
[132.22 → 135.66] Looking already to be an exciting year for AI things.
[135.80 → 141.76] I hope you got a bit of a refreshing break over winter because there's a lot of...
[141.76 → 145.26] I'm guessing it's going to be a whirlwind of AI stuff this year.
[145.46 → 147.00] I think it is going to be a whirlwind.
[147.00 → 157.22] And I didn't get a rest over the break because having nothing to do with AI, our animal nonprofit, we had all the winter weather that most people in the U.S. were aware of.
[157.26 → 159.34] And we were doing animal emergencies.
[159.52 → 163.32] We saved a bunch of lives, which made the lack of rest worthwhile.
[164.30 → 165.72] But there was a lack of rest.
[165.78 → 168.02] There was a lack of rest, but we did a lot of good.
[168.02 → 177.66] But interestingly, the conversation we're going to have today will play into that very non-AI side of my life because we're starting to see some crossovers we'll see in a few minutes here.
[178.24 → 179.08] Yeah, it's interesting.
[179.92 → 184.04] So today, spoiler alert, we're going to be talking about ChatGPT.
[184.34 → 188.56] You've probably been expecting us to talk about ChatGPT for some time.
[189.00 → 196.64] One of the things we wanted to do is really dig into the internals of ChatGPT, how it works and its implications.
[196.64 → 203.12] And so we wanted to do it justice, which is partially why we wanted to take some time and prep for that.
[203.72 → 211.44] But it is interesting also to get a little bit of perspective now that ChatGPT has been out for not that long, but a little while.
[212.22 → 216.02] Over Christmas, you know, I was at Christmas with my family.
[216.50 → 223.26] And even at our family Christmas dinner, my dad was asking me about ChatGPT.
[223.26 → 231.38] And, you know, at my church, I've had people come up to me and ask about ChatGPT who don't work in tech or anything like that.
[231.62 → 240.08] And my barber, you know, whoever is in my life, it seems like they're at least aware of ChatGPT.
[240.50 → 245.52] They might not know exactly what it is, but they know that it's a big deal.
[245.62 → 247.08] Are you having a similar experience?
[247.58 → 249.00] Very, very similar to that.
[249.00 → 254.48] And for folks, Daniel and I haven't talked through the holidays, so, you know, this is the first time I'm hearing it, just as you are.
[254.80 → 256.32] And I'm having the same experience.
[256.32 → 263.84] And it's been really notable that we've, you know, each new large language model comes out and, you know, the various GPT series.
[263.98 → 265.12] And we talk about it.
[265.20 → 270.48] This is the one that's crossed over into mainstream awareness and broad use.
[270.48 → 281.08] And I mentioned as we were getting into the conversation that it's now crossing over from the technical and AI side of my life into the non-technical and animal side.
[281.18 → 286.20] As we do things like narratives, both written and video and educational material.
[286.20 → 297.46] This is an amazing tool that completely non-AI focused people can use productively to really do good in the world and get things done that they want.
[297.60 → 302.36] So it's been fascinating to see how this one has been different from the GPTs before.
[302.36 → 316.90] Yeah, so in your case, it's something that, like, as you're creating content, you see it as potentially playing a role in whatever scripts or articles or whatever that might be.
[316.96 → 317.40] Is that right?
[317.74 → 318.30] Absolutely.
[318.56 → 329.24] It's been quite humbling in that way, experimenting what was possible, because the quality of the outputs are typically much better than I can do by myself.
[329.24 → 336.12] I've done that both in terms of I'm writing a children's story to teach children about animals, and I've been experimenting with it.
[336.30 → 341.14] And every time I write something, and then I seed it into ChatGPT, it does a better job than me.
[341.20 → 343.12] So it's been very humbling in that way.
[343.54 → 346.04] I think of myself as a decent writer as well.
[346.18 → 351.08] And then the quality of video output is just having been quite good.
[351.08 → 356.60] And there's a little workflow, but it means that we can do more good in the world faster.
[356.60 → 360.18] It accelerates the ability to put out great content.
[360.48 → 368.72] And so I think that this is one of those inflection points that we've seen, not just on a technical merit, but in the world at large.
[369.50 → 378.24] Well, your usage seems to be much more useful and valuable than my usage, which has mostly been things like writing.
[378.24 → 387.60] I remember I had ChatGPT write a new Christmas carol for me about the three wise men in the style of a rap song by Eminem.
[388.62 → 391.88] I have to say it was a great rap song.
[392.12 → 398.38] I didn't record it because I'm not Eminem, but I sent it to his people and we're having discussions.
[398.80 → 399.02] OK.
[399.46 → 399.74] Yeah.
[399.74 → 402.56] I can't believe you're not sharing that with us.
[403.88 → 413.32] Well, maybe before we jump in, I think some of what we wanted to do today was just like to describe a bit of like what ChatGPT is, what the interface looks like, what you can do.
[413.60 → 417.60] But then really do a deep dive on what are the guts of the system?
[417.76 → 419.96] Why is it different from what's come before?
[420.60 → 424.00] In what ways is it similar to things that have come before?
[424.18 → 425.58] Both of those things are true.
[425.58 → 429.68] And so we want to do a deep dive and then think about some of the implications.
[429.68 → 430.92] So buckle up.
[431.02 → 432.36] Hopefully this will be fun.
[433.08 → 436.04] First off, it is called ChatGPT, which is interesting.
[436.36 → 441.86] So the interface that they've chosen for this and the sort of design of the system is a chat interface.
[441.86 → 452.28] So if you go to chatgpt.openai.com, you need to create an account, and we can talk about some of the implications around that in a second.
[452.28 → 459.96] When you log in, it gives you some examples of what you can do, some example capabilities and some limitations.
[459.96 → 462.88] I found this interesting, and we can talk about it later.
[463.14 → 466.46] Some of how they describe the limitations, and they release the model.
[466.58 → 469.04] But the basic idea is there's a chat interface.
[469.04 → 471.92] You can type a prompt and it will respond.
[472.04 → 474.96] And then you can actually continue to have dialogue with the system.
[474.96 → 482.36] So you can say, you know, tell me more about that, or I don't understand this part, you know, explain that bit more.
[482.52 → 488.68] So some of the examples that they give are, you know, explain quantum computing in simple terms prompt.
[488.68 → 492.46] Or how do I make an HTTP request in JavaScript?
[492.74 → 495.38] So there's even a, you know, it can output code.
[495.44 → 497.32] It can help you debug code.
[497.32 → 504.00] Like I mentioned, it can provide lyrics or scripts or structured types of things like the Eminem song.
[504.20 → 508.40] So, yeah, that's the basic input output.
[509.40 → 516.50] How did you find this sort of interface, Chris, in terms of your own usage as related to like building scripts and other things?
[516.98 → 520.14] It's been interested in that it will take it a direction.
[520.14 → 530.08] Like as I've been trying out the children's story thing is something I've been playing with and seeing where chat GP chooses to take the beginning of a seed of a narrative.
[530.36 → 537.86] Like I would start off with, you know, once upon a time there was a precocious raccoon named Pandora because that's the hero in the story.
[538.02 → 540.28] And it's been interesting to see how it's taken it.
[540.34 → 543.14] But it's also it will go off in directions I don't want.
[543.20 → 546.98] So then I'll ask questions to kind of steer it a little bit and it will come back.
[546.98 → 556.22] So it doesn't it's not final output, but it's producing a body of narrative that's better than I could have done by far.
[556.38 → 561.08] And so I find myself instead of being the creator of the story, I'm kind of editing it to make it work.
[561.20 → 571.40] But it's a collaboration in a sense between this is one of those first points where we've talked in an aspiring way about collaboration with AI for a long time.
[571.40 → 580.26] But I now am doing that and steering it in different ways with the entering in the chat and seeing where it went and asking specific questions about the story.
[580.52 → 583.28] It's been quite remarkable for the first time.
[583.46 → 586.30] It's like having a partner in the process.
[586.46 → 589.44] It just happens to be that the partner is not human in this case.
[589.90 → 595.52] A friend of mine, Brent Siegel, has been also playing with it a lot, doing some stuff on him.
[595.52 → 597.26] And that's how he described it as well.
[597.44 → 608.80] He was looking at some different topics, and he said, you know, it's like having a dozen world-class scientists for the things that he was focusing on right there available to you.
[608.84 → 609.88] And they're not wrong.
[610.24 → 611.62] You know, they never get it wrong.
[612.14 → 616.12] You know, he had some pretty cool stuff that he was working on in a very different thing.
[616.12 → 624.80] But it's that sense of collaboration with the technology in a real life sense that's really different now from the way it was before this.
[625.44 → 632.18] Well, as you were chatting, which though is some great context, I asked ChatGPT the following.
[632.44 → 637.94] What state-of-the-art AI topics does the Practical AI podcast need to cover in 2023?
[638.44 → 641.02] And who should they reach out to for interviews?
[641.02 → 646.32] And the response, so you're ready for what we'll cover in 2023?
[646.70 → 647.46] Let's hear it.
[648.46 → 653.98] ChatGPT said, it's difficult to predict exactly what the state of the art in AI will be in 2023.
[654.42 → 656.12] Definitely an interesting start.
[656.30 → 656.48] Yeah.
[656.90 → 658.54] As the field is evolving rapidly.
[658.76 → 665.34] However, some topics that might be worth covering include machine learning, interpretability and explainability.
[665.34 → 668.36] And then it actually gives a blurb about what that is.
[668.36 → 670.38] AI safety and ethics.
[671.26 → 672.86] So that's right in your wheelhouse.
[673.02 → 674.64] And it gives an explanation of that.
[675.12 → 676.34] Natural language processing.
[676.76 → 680.78] So we can continue to talk about my favourite topic of NLP in 2023.
[681.46 → 683.90] And computer vision was their other one.
[683.94 → 691.40] And they said to find guests to interview on these topics, you might consider reaching out to researchers and practitioners working in these areas.
[691.64 → 692.08] Very sensible.
[692.08 → 697.88] Some suggestions include Rachel Thomas, co-founder of Fast.ai.
[698.36 → 710.48] Timnit Gebru, co-lead of the ethical artificial intelligence team at Google, which is interesting that it gave that response because that is not factually correct anymore.
[710.48 → 712.10] As she is not with Google.
[712.48 → 715.50] And actually, that was in the news quite a bit.
[715.78 → 716.12] It was.
[716.22 → 720.68] That was a significant story in the AI world a few months ago.
[720.68 → 726.86] And then it gives a few others, including Jan Begun, who, you know, of course, we would love to have on the show.
[727.00 → 729.98] We'd love to have Rachel and Tim nit as well on the show.
[730.48 → 731.24] But yeah, interesting.
[731.54 → 737.06] So a few things, I guess, that strike me as an example with this certain cases.
[737.42 → 740.82] The output is definitely natural and coherent.
[741.38 → 741.60] Right.
[741.60 → 743.78] So that is thing one.
[744.22 → 745.18] That's striking.
[745.34 → 750.08] Thing two for me is there's actually a good bit of like structuring that goes on here.
[750.20 → 758.68] So they actually give, you know, one, two, three, four, the topics that we need to cover and then a bulleted list of the people that we need to have on the show.
[759.10 → 759.24] Yeah.
[759.82 → 767.24] Thing three is despite it being coherent and natural, it is not fully correct factually.
[767.24 → 768.16] Right.
[768.80 → 772.24] So that's maybe another element of this.
[772.24 → 780.78] You know, it's funny because we've seen a fair amount of criticism about, you know, ChatGPT getting things wrong and stuff.
[780.92 → 789.34] I find it curious that as we talk to humans about human things, we get things wrong constantly and fact checking.
[789.34 → 792.24] And, you know, was that misinformation or was it just unintentional?
[792.24 → 792.80] Intentional.
[792.94 → 800.78] And yet we hold these technologies to such a perfect standard that we're ourselves completely unable to hold up.
[801.22 → 804.60] You know, I wouldn't want to ask one question and assume that it was 100 percent right.
[804.72 → 807.98] But it makes it a little bit more interesting to me.
[808.08 → 814.18] That collaboration, I dare say, takes on a human element by having error in it.
[814.18 → 815.18] Yeah.
[815.42 → 822.30] And we'll talk a little bit later about the interaction between this and humans and where the burden lies.
[822.30 → 829.86] I do think that the interface that they've provided and being explicit about limitations, that's a good thing.
[829.86 → 837.26] Now, certain people might kind of go back and forth on this model is not open access.
[837.26 → 837.78] Right.
[837.78 → 843.10] Like you can sign up and create an account and a lot of people have done that, and you can interact with it.
[843.10 → 852.14] But like the model waits itself and, you know, it's not released publicly in that sense, even if a lot of people can use it for free at the moment.
[852.48 → 853.64] There's pros and cons there.
[853.64 → 876.98] But I think it's interesting that this model, as opposed to GPT-3 earlier, it was, I think, easier for the general population to interact with this model right away in comparison with GPT-3, which, you know, had a very long prolonged kind of wait list and timing and all of that and lots of explanations.
[876.98 → 890.62] So it seems like that they've kind of shifted the scales a little bit in terms of making access to run the model more open while still maintaining it as a closed model and providing limitations.
[890.62 → 909.44] So it's interesting to see also that kind of shift in dynamics, which I think probably was influenced by the fact that, you know, actual open access models like Stable Diffusion and others have taken off so widely so quickly because they are more open access wise.
[909.44 → 921.44] And so I felt like we saw open AI shift a little bit in how they release this while still kind of maintaining some of the elements of how they released GPT-3 and others.
[921.56 → 922.78] I agree with that.
[923.10 → 923.24] Yeah.
[923.34 → 930.96] I mean, we've seen that kind of evolution as they've explored release approaches over time, you know, within iterations and such.
[930.96 → 941.54] I think one of the things that we've seen, you know, across this is the fact that every time a breakthrough comes on, we're starting to have fairly quick follow up.
[941.64 → 946.08] But once people know that something is possible, they manage to kind of reverse engineer it.
[946.20 → 953.46] So I suspect that aside from strictly ChatGPT, that we will see some fast followers pretty soon.
[960.96 → 970.58] All right, Chris, let's get into the technical details of this, which I know I'm excited to chat through.
[970.82 → 972.90] No, I guess, pun intended in that case.
[972.94 → 973.16] Oh, boy.
[973.28 → 982.94] There's kind of two elements of this that I think are important to talk about before we talk about what actually was done with ChatGPT specifically.
[982.94 → 987.52] And these two things are more general than ChatGPT.
[987.52 → 995.50] One is sort of the GPT family of language models and those types of language models.
[995.68 → 1001.70] And then also a technology or approach called reinforcement learning from human feedback.
[1002.06 → 1008.78] Those two things kind of combined here to create the ChatGPT system.
[1008.78 → 1016.66] And these two types of models and approach have been applied more widely in other cases and by other people.
[1016.66 → 1018.68] But here they were applied by OpenAI.
[1019.00 → 1028.68] So starting to talk about this sort of language family model of GPTs, we had GPT and GPT-2 and GPT-3 and GPT-3.5.
[1028.96 → 1033.10] And I don't know what, to be honest, I don't know what number we're on now.
[1033.10 → 1038.62] But these GPT language models are just that they're a language model.
[1038.62 → 1044.62] And they're a specific type of language model called a causal language model.
[1044.88 → 1052.86] People might be familiar or at least have heard the words causal language model, CLM, or mass language model, MLM.
[1052.86 → 1056.12] So mass language model kind of takes a sentence.
[1056.12 → 1067.30] And what it's trained to do is kind of for one word that's masked in the sentence or taken out or given a special token, it's trained to predict that based on everything else in the sentence.
[1067.30 → 1072.34] So it sort of looks both ways at the sentence and tries to predict the mask.
[1073.08 → 1075.82] GPT is not a mass language model.
[1075.92 → 1087.28] It's a causal language model, which means that it's trained to predict the next word in a sequence of words or in a sequence of tokens, whatever those tokens might be.
[1087.28 → 1094.10] It does that, and it predicts the next word in the sequence, but it does it based on all the previous words.
[1094.34 → 1096.40] And it does that sequentially.
[1096.60 → 1105.86] So as you go through the sentence, the training methodology is what they call autoregressive, means that it predicts the next thing from all the previous things.
[1106.06 → 1111.62] And then once it's predicted that next thing, then it predicts the next, next thing based on all the previous things.
[1111.62 → 1114.22] And then the next, next, next thing and et cetera.
[1114.22 → 1117.30] And that's the autoregressive part of it.
[1117.84 → 1126.02] I suppose we're kind of seeing that in action because when you're using the interface, it doesn't just give you the entire output all at one time.
[1126.02 → 1127.52] It comes back with text.
[1127.62 → 1132.96] You see the text developing much as if you were typing it, you know, on the screen yourself.
[1133.34 → 1137.42] So I guess you're gradually seeing each of those iterations coming back.
[1137.42 → 1146.02] Yeah. And I think in the original GPT-3 interface or the playground that we both played with, you kind of see this as well.
[1146.12 → 1150.14] You kind of give a prompt, and then it generates this text out.
[1150.24 → 1152.70] And that allows it also to be very flexible, right?
[1152.74 → 1158.38] And produce these structures and also allows it to be flexible between different tasks.
[1158.38 → 1170.72] Like if you start prompting it with question answers, it sort of learns that pattern and in a sort of few shot way and then starts predicting next question and answers or something like that.
[1170.72 → 1183.70] Or if you want a script or if you want a narrative or if you want something else, it kind of adapts in that few shot learning sort of way, which is a key element of this GPT or causal language model structure.
[1183.70 → 1185.54] And GPT is not the only one.
[1185.68 → 1189.76] There are other ones, but this is the family which GPT sits in.
[1190.30 → 1193.60] And you mentioned just as a two-second sideline, you mentioned few shot.
[1193.70 → 1196.06] Do you want to real quick just for those who may not be familiar?
[1196.56 → 1201.56] Yeah. So kind of some jargon, few shot, zero shot is thrown around.
[1201.56 → 1213.02] A zero shot prediction or usage of a model means that maybe you're using a model on inputs or a type of input that it's never seen before,
[1213.02 → 1214.98] even though it's seen maybe similar things.
[1214.98 → 1227.68] So this happens with like machine translation models that are multilingual maybe because you might have in your training data like English to French and, you know, Arabic to Spanish.
[1227.68 → 1233.64] But you don't have examples English to Spanish, but you have English and Spanish data in the data set.
[1233.64 → 1238.98] And so you could still ask that model to try to output an English to Spanish translation.
[1238.98 → 1242.42] And actually that can kind of work in certain scenarios.
[1243.08 → 1255.40] Few shot means that you're not quite doing it that way, but you're providing a few prompts that kind of guide the language model into the type of thing that you're wanting to do.
[1255.40 → 1264.76] So in the GPT-3 interface or playground, if you remember, you can kind of start with a question answer template and provide some examples.
[1264.76 → 1268.22] And then you can provide the next one, and it'll answer it for you.
[1268.70 → 1271.66] And so you provide that set of templates or prompts.
[1271.66 → 1278.34] And this kind of gets into this idea of prompt engineering and that sort of thing, because these models are so flexible.
[1278.34 → 1286.56] So that was the original paper from GPT-3 was titled something like, you know, language models or few shot learners or something like that.
[1286.62 → 1288.54] That was one of the big ideas there.
[1288.80 → 1292.40] That kind of gets us to GPT and language models.
[1293.08 → 1297.40] But ChatGPT, well, I guess it is a model like that.
[1297.44 → 1300.12] So it is a GPT-based model.
[1300.12 → 1314.60] But the reason why the system is so powerful is that it's a language model that has been trained in a unique way that has proved to be actually quite valuable.
[1315.18 → 1325.62] And that's that it is a GPT-based model that was trained using reinforcement learning from human feedback or RLHF, reinforcement learning from human feedback.
[1325.62 → 1329.74] We'll link to this in the show notes.
[1329.74 → 1343.74] But there is a really great article on the Hugging Face blog from Nathan Lambert, Luis Ostinato, Leonardo Von Vera and Alex Bavaria called Reinforcement Learning from Human Feedback.
[1344.30 → 1348.02] And they talk about ChatGPT and other like models.
[1348.60 → 1351.56] So we're going to pull a lot of our insights from this article.
[1351.56 → 1361.02] So thank you to all of you for writing this article because it was really helpful, much more helpful than maybe the OpenAI blog by itself.
[1361.34 → 1379.34] The major idea here with reinforcement learning from human feedback is trying to answer the question like, can we use human feedback on generated text as a measure of performance that goes beyond sort of just like automated measures of performance?
[1379.34 → 1385.72] So how do we integrate human feedback into the loop of training a model as a performance metric?
[1385.94 → 1393.84] And in that way, we're sort of training a language model, but we're also training it in ways that match human preference for answers.
[1394.30 → 1396.58] So human preference is a key piece of this.
[1396.64 → 1403.16] And I think that's why, you know, people like ChatGPT is we prefer the things that it outputs.
[1403.16 → 1417.82] Right. I don't know if that was the case for you, like with just a raw language model like GPT-3, you can get some cool stuff output, but it might not fit your preferences of like how a human would actually respond to something.
[1417.82 → 1425.10] You know, going back to the example I mentioned in the beginning, that was the trick for me was, you know, like using the children's story as an example.
[1425.42 → 1433.18] I had a specific rough narrative in mind because I'm trying to teach and there are certain points that I'm trying to illustrate.
[1433.18 → 1443.60] And obviously it doesn't know that the model, but the model, if you work with the model being able to kind of, you know, continue to point it the right way, that was, that was very interesting.
[1443.60 → 1450.00] I am curious going back to what you were talking about a moment ago with, you know, the reinforcement learning with the human feedback.
[1450.52 → 1452.26] How does that scale?
[1452.66 → 1471.76] You know, because if we were to compare this for a moment, I know this is very much a kind of newbie question, but for those of us who are not, you know, deeply into language models, you know, when we were looking at other types of models a couple of years, two, three, four or five years ago, there was always a challenge about getting human feedback to scale with the amount of training data.
[1471.76 → 1479.80] How is that tackled in this approach so that you can do reinforcement learning that way, but it scales to, you know, what we're doing at GPT?
[1480.24 → 1489.88] There's actually like a whole loop of models involved here and different training sets that are of different scales and different models that are of different scales.
[1489.88 → 1499.94] So let me talk through a little bit of that and I, hopefully that will become more clear because yeah, obviously human feedback is expensive in terms of gathering it, right?
[1499.94 → 1501.54] So how much of this do you need?
[1502.04 → 1512.76] So there are three steps, but the process with which ChatGPT was trained and other models using this reinforcement learning from human feedback approach, it's a three-step process.
[1512.76 → 1516.02] So you pre-train a language model, which is not new.
[1516.32 → 1518.56] We've been doing that for quite some time, right?
[1518.56 → 1527.76] You pre-train a language model, then you gather this sort of human preference data and train a reward model.
[1527.76 → 1539.90] Now the second reward model is trained to take in a prompt and a response and score it like a human would score it according to preference.
[1539.98 → 1547.44] So it's actually trained on the human preference data, and it outputs a prediction of what a human preference might be on this output.
[1547.44 → 1561.66] And then the third and final step is that you fine tune a copy of your original language model using this trained reward model and a reinforcement learning loop.
[1561.66 → 1567.14] So is it just kind of the discriminator you're using the reward model as the discriminator in that or?
[1567.68 → 1578.10] It's like in a reinforcement learning loop, you would have a kind of policy which outputs like what you should do next sort of thing.
[1578.30 → 1586.38] And then you have some type of reward system that rewards the agent for acting according to the policy or not.
[1586.38 → 1595.08] So in this case, the reward model is outputting that reward or that preference and the language model is actually acting as the policy here.
[1595.08 → 1602.30] So you have an original language model that is kind of your original policy and isn't fine-tuned yet according to human feedback.
[1602.30 → 1619.98] Then you gather some human feedback, like actual human feedback, train a reward model to simulate that human feedback, and then you fine tune a copy of your original language model or a copy of your policy with this reward model.
[1620.68 → 1624.52] And so the pre-trained language model, it could be any language model.
[1624.60 → 1630.58] It doesn't have to be GPT-3, but in the case of OpenAI, it was GPT-3.
[1630.58 → 1643.64] But you have an original language model, and that language model could just be a general pre-trained language model, or you could additionally fine tune that model and maybe for a domain or a specific type of output you want.
[1644.14 → 1646.14] So that's your pre-trained language model.
[1646.26 → 1659.14] And the step two, to get the reward model, what you do is you start outputting data from your original policy, from your original language model, and you have humans rate it.
[1659.14 → 1665.10] Maybe you combine that with certain human output or certain other outputs, and you have human rating.
[1665.24 → 1675.52] So that way you're creating a training set for your reward model, which includes human labels of their preference.
[1676.46 → 1684.62] Then also in this step two, you then train a reward model using that data that you've gathered from humans to output the preference.
[1684.62 → 1688.78] Now, to your point of, like, how does this scale?
[1689.48 → 1695.02] Well, the fine-tuning of the policy is done kind of with this automated reinforcement learning loop.
[1695.70 → 1701.74] But you do need humans to generate enough data to train your reward model that's used in that loop.
[1701.74 → 1716.70] And what's interesting is, and the Hugging Face blog makes this point, is that different people or different groups that have applied this reinforcement learning from human feedback have used different sized reward models.
[1716.82 → 1721.68] And obviously, as the size of your reward model increases, you need more data to train it.
[1722.02 → 1723.74] That would be a general rule.
[1723.74 → 1730.04] In the case of OpenAI, their main language model was like 175 billion parameters.
[1730.34 → 1734.00] And the reward model was much, much smaller, 6 billion parameters.
[1734.60 → 1738.70] In other cases, people have done similarly sized models.
[1739.28 → 1741.48] And so I think that is an open question.
[1741.74 → 1745.96] Like, how should these models size-wise be related to one another?
[1745.96 → 1749.74] What types of models should you use for your reward model?
[1749.82 → 1751.88] And how much human feedback do you need?
[1752.24 → 1755.22] To be honest, I think those are open research questions.
[1755.64 → 1757.30] Let me ask you another question on that.
[1757.42 → 1763.76] With us getting high-quality output that is comparable to human output very closely.
[1764.10 → 1771.44] And if you were to get that output, you would find a very difficult time knowing whether it was the model or human that did that.
[1771.44 → 1780.18] Does that potentially go back in to train further reward models where you're using essentially synthetic data as the output of a previously trained?
[1780.64 → 1781.70] And so you can build on it.
[1781.92 → 1789.64] And essentially, there's a point where you have enough data where you're largely able to take humans back out, recognizing it's the tool of the day.
[1789.74 → 1796.36] But in the future, you can take humans back out of that loop of providing the reward model to do that.
[1796.44 → 1799.26] Do you anticipate that that would be a reasonable expectation?
[1799.26 → 1816.68] I think in this methodology, the reinforcement learning from human feedback, one of the goals in that middle step is to get enough human feedback that you kind of reduce the harm and the helpfulness of the output model.
[1816.88 → 1826.58] So this is really addressing, I think, some of those kind of problems with large language models of hallucination and harmful effects, general output.
[1826.58 → 1828.32] And you can address those.
[1828.32 → 1836.08] What I think is the finding here is you can address those with humans in the loop rather than humans totally out of the loop.
[1836.20 → 1844.64] Now, here in the next step that we'll describe in the process, humans are taken back out of the loop to fine tune the model.
[1844.64 → 1870.30] But that central piece, so this three-step process of starting with a language model on one end, ending with a reinforcement learning trained model on the other end, has this middle step that I think is a really key piece of it that actually helps the utility of the output and potentially reducing harm of the output, which is that human feedback piece.
[1870.30 → 1885.20] All right, Chris, we're about to the end of this reinforcement learning from human feedback loop.
[1885.20 → 1890.18] Just in summary, the loop is we have a pre-trained language model.
[1890.36 → 1897.98] Then we gather this human feedback or rating of the output to train a reward model.
[1898.14 → 1900.40] Now we're actually going to use that reward model.
[1900.56 → 1907.70] So in the final step of the process, we make a copy of the original language model or the policy.
[1907.70 → 1915.00] So you have an original policy, and you have a copy of the policy or original language model and a copy of the language model.
[1915.62 → 1922.56] You put in a prompt to each of those models, and then you get an output from each of those models.
[1923.08 → 1935.04] Then you use a sort of constrained reward function where you actually penalize if the updated model is straying too far away from the original model.
[1935.04 → 1945.46] Because I think what they have found is, you know, if you allow it to sort of just take any direction in the output you want, it can have computationally some optimization problems.
[1945.46 → 1956.32] So you kind of gradually change this language model from the original, and you have a penalty for how far that output strays from the original output.
[1956.32 → 1960.76] And then you score that output with this reward model that you've created.
[1961.00 → 1969.86] And the way that they're doing the updates for ChatGPT and some of these others with a reinforcement algorithm called proximal policy optimization,
[1969.86 → 1978.80] which you have sort of two levels of what in physics I would think of as adiabatic change, meaning like things don't change too quickly.
[1979.34 → 1985.46] One is you don't stray from the original policy output too much, or you're penalized from that.
[1985.46 → 1996.78] And secondly, this reinforcement learning algorithm called PPO prevents you from making too big of updates to your model weights in each step.
[1997.10 → 2002.04] That way you don't have, again, this kind of hard optimization to do.
[2002.44 → 2006.76] But in summary, you kind of have these two models, the original one, the updated one.
[2006.86 → 2008.54] You output a prompt from both of them.
[2008.54 → 2017.18] Those go into your reward function, which includes a penalty element for straying too far from the same output.
[2017.18 → 2024.00] It also includes the actual estimated reward or estimated preference from your reward model.
[2024.18 → 2036.60] And then that reward is then used to update the weights of your copy model or your new policy using this PPO reinforcement learning algorithm.
[2036.60 → 2041.42] So hopefully there are some diagrams in the post that I think are quite helpful.
[2041.56 → 2047.70] It's a bit hard on a podcast, but hopefully that loop makes some sense in terms of how you're updating this.
[2047.76 → 2053.70] And this updated policy or this updated language model is the model that is used.
[2053.78 → 2057.32] So this is like the ChatGPT model that comes out of the end.
[2057.32 → 2063.66] I think given the limitations of our medium here, I think that was a very lucid explanation of translating it.
[2063.78 → 2064.98] So I appreciate that.
[2065.10 → 2066.48] I've definitely learned some.
[2066.80 → 2066.94] Good.
[2067.14 → 2068.48] I know formulas.
[2068.60 → 2073.38] You can ask ChatGPT to output all the right formulas, and I'm sure it would do a fine job.
[2073.38 → 2076.86] Where do you think we're going from here?
[2077.06 → 2088.66] Like as you have looked at this progression of these models over that we've covered on the show over time with ChatGPT in particular, it's been I've been kind of amazed at what it could do and using it.
[2088.66 → 2091.68] But I'm really, really curious about where this is going.
[2091.74 → 2096.04] And I think it's capturing a lot of people's imagination in that way that are outside the field.
[2096.04 → 2097.12] Like what's next?
[2097.12 → 2101.56] I think there's still open research questions here that are worth exploring.
[2101.56 → 2106.62] And then there's like workflow and practical implications, I think.
[2106.80 → 2112.72] On the first side, as was mentioned already, and we were discussing this reward model.
[2112.92 → 2119.12] As far as I can tell, it's not totally determined like what the architecture of this reward model should look like.
[2119.12 → 2123.62] How big it should be in relation to the model that you're fine-tuning.
[2124.04 → 2126.48] How much human feedback should you use?
[2126.48 → 2135.22] How does the amount of human feedback that you get influence the harmfulness or the utility of the output and that sort of thing?
[2135.30 → 2141.04] So I think there's a lot to explore around that dynamic between the reward model and the language model.
[2141.16 → 2144.78] In addition, I mean, language models are still being developed, right?
[2144.78 → 2154.06] So ChatGPT use the GPT-3.5 language model as this original policy, right?
[2154.06 → 2161.66] And they actually used a fine-tuned version of that using supervised methods and human chat conversations.
[2161.66 → 2167.54] So they started with a fine-tuned version of chat or of GPT-3.5.
[2167.54 → 2171.52] So obviously, we're going to have a GPT 4, GPT 5.
[2171.64 → 2175.18] We're going to have other language models from other providers, right?
[2175.54 → 2183.56] From other research groups, you know, Big Science or Google or Microsoft or whoever's developing these other language models.
[2183.56 → 2185.28] We're going to have updated versions of those.
[2185.28 → 2206.20] So I think we can see a research direction with this where people are trying different pre-trained models as their original policy, where people are trying different reward models, where they're mixing them up in interesting ways, where they're maybe using slightly modified versions of the PPO algorithm or other reinforcement learning algorithms to do the updates.
[2206.20 → 2215.54] So there's a research direction where I think we'll just see a lot of exploration with this kind of template as the structure that they're exploring.
[2215.94 → 2224.92] The second piece, which is maybe more interesting to some of our audiences, like, what are the implications of this in terms of people's workflow?
[2225.46 → 2227.56] I was about to ask you that if you hadn't gone there.
[2228.14 → 2229.18] Yeah, I don't know.
[2229.24 → 2231.76] What are your initial thoughts there, Chris?
[2231.76 → 2239.02] It's less about the technical aspects of the model and more about going back to the user interface considerations we talked about earlier in the conversation.
[2239.34 → 2246.86] I would be amazed if the community at large, not just OpenAI, hasn't understood the impact of making choices like that.
[2246.92 → 2250.82] It may not be specific to the model development, but how you're putting it out there.
[2250.98 → 2252.84] And they're seeing widespread adoption.
[2252.84 → 2260.06] When you go into their interface, you get a warning right off the bat, we're experiencing exceptionally high demand.
[2260.46 → 2262.40] Please hang in tight as we scale our systems.
[2262.84 → 2272.52] And I think that's indicative of the fact that people who are not normally listeners of this podcast are starting to find a lot of utility for the first time ever.
[2273.08 → 2274.04] It'll be interesting.
[2274.04 → 2281.48] We keep talking about exponential growth in this field and these amazing mini revolutions along the way.
[2282.14 → 2289.94] But this is that first point where it's probably going orders of magnitude broader in terms of applicability to different workflows and audiences.
[2289.94 → 2302.96] So, and as we're looking at, you know, you're combining just for a moment going back and combining natural language with the large language models, with generative capabilities, with reinforcement learning.
[2302.96 → 2308.88] And we're kind of seeing, we saw slices of each of these fields over the last few years developing.
[2309.14 → 2311.92] And we've been talking about this fusion of the fields.
[2311.92 → 2321.76] And so, how soon before we start seeing entertainment, you know, that is being heavily, heavily based on these technologies.
[2322.16 → 2339.04] I'm seeing it in my little tiny nonprofit because we can suddenly leverage this to put out content to help folks in a charitable fashion that we can do at least 10 times as much as we would have been able to before by taking advantage of these.
[2339.04 → 2342.80] And so, I think we're at that inflection point now where this will be the first.
[2343.36 → 2357.30] And as we have continuing episodes through the course of this year and some new things come out, whether it's from OpenAI or similar things from other organizations, I think we're getting to that point where it's really hitting broadly in real life.
[2357.86 → 2359.32] So, I'm really fascinated.
[2359.32 → 2372.52] I would love to hear from our listeners on ways that they're using this technology, what they think might come next, and how they are envisioning using it within their own organizational missions to accomplish what they want.
[2372.82 → 2376.28] It's a fascinating moment in history of AI that we're in right this second.
[2376.28 → 2395.06] And one thing which I can't claim as my own insight that I stole from Twitter, but I think has really shifted my thinking a little bit on this subject is, so this is actually a tweet from Chris Alban, who is the director of machine learning at Wikimedia.
[2395.06 → 2404.76] And the statement he made, which I think was really insightful, and maybe other people are having similar observations, but he said, sci-fi got it wrong.
[2405.82 → 2413.62] We assumed AI would be super logical and humans would provide creativity, but in reality, it's the opposite.
[2414.48 → 2423.10] Generative AI is good at getting an approximately correct output, but if you need precision and accuracy, you need a human, end quote.
[2423.10 → 2436.10] So, I think the observation here is like, and we've talked about this on the show with language models also, language models are perfect at actually at naturalness, creativity, apparent coherence, right?
[2436.24 → 2445.10] Like that actually is what they're good at, but they get the facts and the precision and the accuracy wrong many times, right?
[2445.10 → 2459.26] So, whereas I think in the past people have thought the unique thing about what humans can provide in an AI-driven system is creativity, not logic and that sort of thing.
[2459.74 → 2462.68] Actually, the opposite is really the case, right?
[2462.86 → 2472.70] Like the AI bits are really driving the creativity and the humans are enforcing the logic, the facts, the accuracy, and the precision.
[2472.70 → 2475.14] That has really shifted.
[2476.16 → 2483.06] Like I think I've been realizing that over time, but that statement really put some words to I think what I was thinking.
[2483.26 → 2485.04] It's comforting in a way.
[2485.24 → 2491.94] And the reason I say that is we talked in times past about creativity coming from the humans rather than the machines.
[2491.94 → 2497.52] And yet the evidence that we've been looking at over these last couple of years has been not that.
[2498.10 → 2503.20] And so, I have actually been wondering what role is there for the humans in that equation.
[2503.80 → 2512.24] So, the fact that it's flip-flopped back, it's the inverse of what our expectation was, it still means there's room for a human in the picture.
[2512.56 → 2514.58] And that's a little bit of a comforting moment.
[2514.66 → 2517.92] It may not be what we thought it would be, but there's still a place.
[2517.92 → 2521.58] And I think that's probably a good high note to leave people with.
[2522.22 → 2533.14] On the note of things being useful to humans and humans getting involved, we did want to leave you with a few learning resources to explore things related to ChatGPT.
[2533.30 → 2534.92] Of course, play around with ChatGPT.
[2535.66 → 2538.16] You can go on the website and interact with it.
[2538.22 → 2539.08] We'll provide the link.
[2539.08 → 2547.06] But also, I would really highly recommend that you look at this Hugging Face blog about reinforcement learning from human feedback.
[2547.48 → 2556.32] There are actually a bunch of links in there as well to other things that you can kind of spin off and look at, like the PPO algorithm and other things in there.
[2556.64 → 2558.54] Also, there's a good reference.
[2558.54 → 2563.68] I always love looking back at Jay Altar's descriptions of how certain language models work.
[2563.68 → 2573.52] He has one on GPT-3 and other GPT, actually a number on GPT from different perspectives.
[2574.44 → 2582.72] And then there's an interesting article on GPT-3 architecture on a napkin from a blog, dugas.ch.
[2582.90 → 2586.42] I found it quite interesting how they describe some of the things there.
[2586.66 → 2587.56] I like that one as well.
[2587.56 → 2588.52] Yeah, yeah.
[2588.68 → 2590.66] So go ahead and check those out.
[2590.72 → 2592.04] Those are great learning resources.
[2592.30 → 2592.88] They're all free.
[2593.02 → 2602.06] You can take a look at them and learn in more detail some of the things that we only had 45 minutes to talk about here on the podcast.
[2602.36 → 2603.94] And our social media channels.
[2604.10 → 2608.64] I'm encouraging our listeners to share with us some of the ways they're using the technology.
[2609.20 → 2610.90] I'm really waiting to hear that.
[2611.32 → 2613.46] And the more unique, the better.
[2613.82 → 2614.78] Yeah, sounds great.
[2614.78 → 2617.18] Let us know what you're creating with ChatGPT.
[2617.56 → 2618.64] It's been a fun one, Chris.
[2618.72 → 2619.52] Good to chat with you.
[2619.72 → 2620.04] Absolutely.
[2620.16 → 2623.20] Thank you very much for the incredibly lucid explanation.
[2623.44 → 2625.88] It certainly helped me understand.
[2626.20 → 2627.78] And I appreciate it as always, Daniel.
[2627.86 → 2628.68] Talk to you next week.
[2628.68 → 2629.68] Bye-bye.
[2629.68 → 2639.36] All right.
[2639.52 → 2641.08] That is our show for this week.
[2641.34 → 2643.64] If you dig it, don't forget to subscribe.
[2644.28 → 2646.90] Head to practicalai.fm for all the ways.
[2646.90 → 2652.84] And if practical ai has benefited your life, pay it forward by sharing the show with a friend or a colleague.
[2653.16 → 2656.14] Word of mouth is the number one way people find shows like ours.
[2656.56 → 2659.42] Thanks again to Vastly for fronting our static assets.
[2659.70 → 2662.14] To Fly.io for backing our dynamic requests.
[2662.70 → 2664.24] To Break master Cylinder for the beats.
[2664.50 → 2665.40] And to you for listening.
[2665.64 → 2666.32] We appreciate you.
[2666.58 → 2667.50] That's all for now.
[2667.74 → 2669.20] We'll talk to you again on the next one.
[2669.20 → 2683.56] Game on.
