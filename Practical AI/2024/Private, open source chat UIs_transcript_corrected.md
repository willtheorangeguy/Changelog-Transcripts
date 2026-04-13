[0.00 → 8.66] Welcome to Practical AI.
[9.34 → 19.54] If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.24 → 24.92] Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 → 32.36] Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents.
[32.36 → 35.44] So you can launch your app near your users.
[35.84 → 37.84] Learn more at Fly.io.
[42.62 → 47.22] Welcome to our next Practical AI webinar.
[47.58 → 52.18] This is our second webinar or live event that we've done.
[52.18 → 66.30] Chris, we've always done the podcast pre-recorded, and it's been fun in last time to talk about text-to-SQL live and now to have another chance to have a live webinar.
[67.00 → 67.90] Are you enjoying these?
[68.24 → 69.10] I am enjoying them.
[69.18 → 70.54] I think we need to do these more often.
[70.64 → 71.20] They're a lot of fun.
[71.56 → 72.20] Yeah, yeah.
[72.20 → 76.62] And today, so I'll kind of frame the conversation for today.
[76.80 → 80.80] But first, let me also welcome Danny from Liber Chat.
[80.80 → 83.52] He's joined us to talk about the topic today.
[83.76 → 84.56] Thanks for joining, Danny.
[84.92 → 85.42] Yeah, of course.
[85.54 → 86.40] It's an honour to be here.
[86.70 → 86.92] Yeah.
[87.06 → 92.36] Well, thank you for everything you're doing on the Liber Chat project and in the community.
[92.80 → 102.96] Today, as those that are in the webinar know, and maybe if you're listening later, we're going to be talking about crafting the next generation of AI chat interfaces.
[102.96 → 118.58] And just to kind of frame the setup for this, we've talked a lot of times and I still frequently, even this week, last week, I hear about people saying, oh, my company doesn't let me use the ChatGPT interface.
[118.58 → 136.90] Or even literally today, like three hours ago, I was in a meeting with a number of customers, and they were asking was, how do I get a chat interface that allows me to switch between models and like try different things with different models?
[136.90 → 142.16] Like if I want to try Llama 3 or something like that, are there ways for me to do that?
[142.46 → 143.96] Are you still encountering that as well?
[144.38 → 145.52] Literally every day.
[145.76 → 147.58] And I'm very sensitive to it.
[148.00 → 154.88] You may recall that I was getting after teachers online and a teacher pointed out that, hey, this is not our choice.
[154.94 → 155.86] It's the school system.
[155.96 → 159.12] So I've been super sensitive to this ever since then.
[159.24 → 160.64] And we have challenges.
[160.82 → 163.16] I'm hoping today can put a big dent in that one.
[163.50 → 164.26] Yeah, great.
[164.26 → 191.80] Well, I'm super happy that we have Danny with us because this is what Danny has devoted a huge amount of energy to with Libra Chat, both in terms of providing an open source chat interface, also providing a chat interface that allows you to plug in different AI systems, whether that be open AI or many others, closed source and open source types of models and systems.
[191.80 → 201.16] And providing even functionality related to, I think even rag and plugins and other cool stuff.
[201.16 → 224.74] So I'm going to, I think now pass it over to Danny and let him kind of share a little bit about, you know, the background of Libra Chat, what it is and how he views kind of the need for private or open chat interfaces and what they're trying to accomplish with Libra Chat and how they see that fit into the industry and what's sort of needed.
[224.74 → 227.18] So over to you, Danny, looking forward to this.
[227.66 → 228.38] Yeah, absolutely.
[228.74 → 234.54] You know, part of the original idea was kind of inspired by a chat GBT leak.
[235.10 → 241.76] I don't know if you remember this, but there was someone whose messages were being seen by a different user.
[242.38 → 242.60] Yes.
[242.70 → 248.30] You know, he's from Poland or Russia and someone woke up one day and all their messages were in Polish.
[248.30 → 253.04] That surprised me, but it really planted the seed for what I wanted to see.
[253.80 → 258.86] And I thought that was just a basic thing to overlook and just started crafting from that impetus.
[259.44 → 269.20] And yeah, I think it's inherently completely private with the flexibility of having like remote stuff in there, too, which I think is important.
[269.62 → 273.20] But yeah, I honestly started off as a learning experience.
[273.20 → 277.84] It was ChatGPT had just come out and rocked everyone's world.
[278.40 → 282.64] So I was like, wow, I really want to learn how this interface works.
[282.78 → 283.78] Like, what are they doing here?
[284.18 → 289.02] And I had just started learning about UIs in general and web development.
[289.22 → 290.52] So it really interested me.
[291.04 → 295.84] And something I saw was, you know, this was such a huge tool in my learning.
[296.28 → 298.52] You know, as I learned, this thing was being built out.
[298.52 → 304.36] But also, you know, there was that need right away because, you know, I posted it on GitHub.
[304.98 → 308.34] And the next day I had six stars, and I was blown away.
[308.44 → 309.90] I was like, what, six stars?
[311.30 → 312.02] That's great.
[312.42 → 313.60] Who's looking at this?
[314.16 → 319.46] Yeah, it was already, you know, getting picked up by search algorithms or GitHub's algorithms.
[319.46 → 324.18] And I was just like totally blown away by that and totally motivated.
[324.62 → 328.04] You know, a lot of people started commenting right away what they want to see.
[328.92 → 338.90] And I think having access to these tools sooner rather than later is going to be a huge thing, no matter, you know, what your team size is, what your business is.
[338.90 → 343.02] And obviously, you know, you have to tread carefully with the privacy side.
[343.12 → 356.08] But I think I've built something battle tested at this point that, you know, thankfully, it's as much as a contribution from, if not more so a contribution from the people using it would really help me along the way.
[356.08 → 377.42] So you mentioned kind of like the initial problem that you saw that kind of motivated you to go down this rabbit hole, which was kind of seeing others messages, which is definitely a piece of it in terms of how an application like this manages state and data and that sort of thing.
[377.42 → 380.16] What did you find like going down that rabbit hole?
[380.64 → 400.44] Is there a way that you can like to categorize the main categories of things that people have come to find useful about having their own chat interface rather than kind of one provided by a model data and privacy?
[400.44 → 408.22] But what are the kind of those main features or things that are on people's mind when they're thinking about having their own interface?
[408.92 → 414.44] I think for me, too, it's just owning your own data and data is like the new commodity.
[415.42 → 418.38] It's so valuable even to these big AI companies.
[418.82 → 427.66] They're constantly releasing their own interfaces that are cutting edge, I might add, but they're also looking to collect data.
[427.66 → 439.72] And I think a trend I want to see in tech and especially from the open source world is just owning your own data that stays between you and these large language models and your company.
[440.48 → 444.34] And you really have that luxury through this app.
[444.68 → 446.78] And so that's a big driver for me.
[446.90 → 449.32] And I think that's a big component for a lot of people.
[449.32 → 461.08] And yeah, and it's also as you're learning from these things, it's like I think it's so valuable to kind of like categorize and piece through like, you know, certain conversations you've had in the past.
[461.08 → 469.84] And that's why like one of the main features that's been like a mainstay since the very beginning was being able to search your messages.
[470.74 → 475.44] And to this day, it's not a feature on ChatGPT or many different interfaces.
[475.44 → 478.56] So I think that's very interesting to see play out.
[478.62 → 483.24] But I also I know a lot of people just that one simple feature gets them on board.
[483.44 → 489.72] I'm curious as we talk about the applicability of this, you know, for instance, large corporations.
[489.72 → 495.20] And I work for one of those large corporations which built its own interface some time back.
[495.40 → 501.18] And others will have well, but there is going forward that takes a lot of maintenance, a lot of concern.
[501.18 → 516.42] If you were in front of like a chief digital and AI officer, a CDA for a large corporation, and it may have already created its own, what would be your pitch for saying, you know, come over to Libra Chat because of X?
[516.56 → 526.66] How would you convince the Fortune 500 companies that are out there that this is the way to go rather than investing on their own compared to their whatever investment they've already made that sunk costs?
[527.22 → 529.46] Number one, it's completely open source.
[529.46 → 531.04] It's got a lot of contributions.
[531.04 → 535.74] There's nothing being hidden in terms of its interoperabilities.
[536.20 → 553.14] And also, number two, it's highly configurable with any kind of intranet network you might want to do or, you know, it can be completely like sealed and even work with large language models without needing to hit some kind of remote service.
[553.40 → 555.88] And it could be completely on local connections.
[555.88 → 561.86] It really just depends on the admins level expertise and connecting all these things.
[562.06 → 575.64] But even just using the default Docker compose, you can just spin up something that's only available to you and is configured in a way if you're using like insecure default variables and things like that, it'll warn you right away.
[575.64 → 581.56] So, yeah, I think those are the top three things I'll say to try to convince someone.
[581.56 → 585.48] Well, I think people are eager to see a chat interface.
[585.60 → 586.84] We've been talking about them.
[587.26 → 591.98] So we'll kind of let you go from here and show what you want to show.
[592.12 → 595.84] And I'm sure we'll have some questions and thoughts as you're showing these things.
[596.02 → 604.72] And, yeah, if you could talk through kind of the demo and what's on your mind as you're thinking about the different features that you're showing.
[605.22 → 605.80] All look good.
[606.20 → 606.92] All looks good.
[606.92 → 607.40] Great.
[607.40 → 607.56] Great.
[607.82 → 613.32] So, yeah, I'm running this locally, and I'm using Obama.
[613.50 → 615.06] I have it hosted on my computer.
[615.36 → 620.00] So I'll just write hi there, and it should usually take a second to load up.
[620.92 → 625.10] And Obama, for those that aren't familiar, do you want to describe that just a second?
[625.82 → 632.84] I guess it's hard to find a specific term for what it does, but basically it helps you manage local large language models.
[632.84 → 641.78] Like it helps you pull down their latest build files, and then it helps with the prompt wrapping process and serves them on an API.
[642.28 → 647.32] So it just makes them really accessible wherever you can run them.
[648.10 → 648.18] Cool.
[648.48 → 649.82] So it finally got to me.
[649.82 → 656.76] And now that it replied, you know, the next couple of replies should be a little quicker.
[657.36 → 662.52] But basically, you know, this interface is, it should look pretty familiar to a lot of people.
[663.08 → 667.28] You know, unabashedly taking a lot of inspiration from ChatGPT.
[667.28 → 669.48] There are just a couple of core things.
[670.02 → 671.90] Like I mentioned, the search messages.
[672.66 → 675.90] And if I search here, it's already picking this up.
[676.32 → 678.80] It's a previous conversation I had.
[678.84 → 680.08] I was testing some file there.
[680.78 → 685.94] And aside from that, going back to this, this is kind of segmented.
[685.94 → 696.36] But for people who have like a need to set more custom parameters or even just setting instructions here and making sure that it generates what they want to see.
[696.36 → 702.24] So I'll say, make sure to write code in Markdown.
[703.90 → 709.06] And I'll say, write me a recursive Python function.
[709.06 → 713.58] Yeah, so it's doing the job.
[714.28 → 717.48] Whether it needed my instruction, it depends.
[717.66 → 719.34] But it had it.
[719.48 → 723.96] And so it kind of steered it right away to use Markdown, which gets rendered like this.
[724.64 → 725.26] It looks beautiful.
[725.52 → 735.56] And it even has like the copy code and the nice sort of like edit button copy, all that stuff that one would expect.
[736.08 → 738.04] And really, it's pretty simple, too.
[738.04 → 739.74] And I like that simplicity.
[740.02 → 746.18] I think I've seen a lot of interfaces kinds of get lost with the technical side of it.
[746.52 → 748.28] And I'm sure that has an audience.
[749.14 → 752.78] And those are great interfaces for certain technical things.
[752.96 → 757.08] But something about this is just immediately accessible, I think.
[757.88 → 761.16] And, of course, we mentioned that we could switch AI providers.
[761.16 → 768.20] And I've got, I heard someone recently call this, you know, gotta catch them all Pokémon of AI.
[769.00 → 773.58] But these are just a little showcase of like all the different ones we can use.
[773.68 → 778.14] So I personally like Grok just because of its speed.
[778.58 → 780.50] And it's blazing fast.
[780.76 → 783.56] This is running Llama 370B.
[783.56 → 786.14] And this was like also a switch.
[786.48 → 790.06] So in the interface that you're showing, you're having a conversation.
[790.54 → 797.24] It's also was a switch between Obama and Grok in the same thread.
[797.36 → 798.56] Am I understanding that right?
[799.04 → 799.88] Yeah, correct.
[800.40 → 800.98] That's awesome.
[801.56 → 801.72] Yeah.
[801.72 → 808.96] So you can kind of and does that message thread sort of history carry through to the different models, I guess?
[809.52 → 809.66] Yeah.
[809.80 → 813.20] So that's where the database comes in.
[813.26 → 820.96] Just keeping track of the conversation, not just the back and forth, but also any changes you might make.
[821.10 → 826.48] So if I make changes here on the fly, that'll get recorded with the conversation state.
[826.48 → 841.82] Yeah, I love how you can stay in context of the problem that you're trying to solve and yet still optimize against different models in terms of what they're better and worse on the fly without it kind of taking over and becoming the primary concern.
[842.04 → 843.06] So very nice.
[843.78 → 844.12] Thanks.
[844.34 → 844.54] Yeah.
[844.64 → 850.32] And that brings up something perfect user feedback I got maybe along the lines.
[850.32 → 863.06] There could be like a smart router that kind of knows, or even you could pre-configure beforehand, like which is the best AI for this sort of task and just kind of switches it for you.
[863.66 → 867.78] So maybe that's something down the line I'm still kind of drafting in my head.
[868.24 → 873.94] But of course, like as these things evolve, there's like we mentioned RAG.
[873.94 → 880.10] So a lot of people have the expectation for files to work with these things.
[880.46 → 883.32] And of course, this Albrecht supports that.
[883.92 → 885.18] And here I just dropped a CSV.
[887.06 → 888.90] I'll say, tell me about these sales.
[890.00 → 890.14] Yeah.
[890.18 → 892.52] And this was just mock data I made up.
[892.72 → 896.20] So it's about Gadget B, Gadget B, different sales data.
[896.78 → 901.92] So I was able to look at that and just kind of give some context about it.
[901.92 → 904.92] And of course, I could switch the model just as before.
[905.82 → 914.10] So I switched to Cohere and didn't give as good of a response as GPT-4, but it was able to see that and kind of work with it.
[914.84 → 920.60] And even that, like the file processing, that's all based off a local RAG solution.
[921.04 → 928.30] So it's using like a local vector database and a local server that's just dedicated to the files.
[928.82 → 930.80] And yeah, that's one of the things there.
[930.80 → 936.76] One of the things I'm particularly excited about is agents and agent workflows.
[937.82 → 942.52] Of course, we have OpenAI recently made a solution of their own with assistants.
[943.40 → 947.40] And I think people are still discovering the capabilities of this.
[947.40 → 957.86] But I think it's exciting for me, like not just working with like what AI companies have as cutting edge, but also as inspiration for the open source side.
[958.00 → 960.12] Because I think they model this really well.
[960.12 → 964.34] And it's giving me ideas of, you know, how can we do this for with Obama?
[964.80 → 969.30] How can we structure something like this with the latest meta AI models?
[970.26 → 971.74] I have a test prompt here.
[971.74 → 975.64] And this is how I generated my sales from before.
[976.50 → 977.84] But I'll add something here.
[979.24 → 984.88] Finally, output the file you created.
[984.88 → 994.52] So this can pretty much not just write code, but execute it within OpenAI sandbox.
[994.94 → 1001.08] So that's really great for things like data analysis and just generating mock data like this, too.
[1001.80 → 1002.06] Yeah.
[1002.14 → 1003.56] So it might take some time.
[1003.56 → 1006.00] While that's running, there's a question.
[1006.84 → 1010.64] Did you test your local RAG system against others like OpenAI?
[1010.98 → 1021.30] So maybe some interest in kind of the performance of that RAG system with a variety of models and locally versus kind of those built into closed systems?
[1022.00 → 1022.30] I did.
[1022.52 → 1028.60] I definitely with OpenAI especially because they have a RAG system through assistants.
[1028.60 → 1033.56] And to be honest, it's right now it's not doing anything too special.
[1033.74 → 1035.12] It's what they call Naive RAG.
[1035.48 → 1039.18] But I found even with Naive RAG, you have a perfect prompt.
[1039.52 → 1043.08] And so I tested that prompt, several different iterations of it.
[1043.52 → 1048.78] You can really get something effective almost across the board like any LLM.
[1049.62 → 1052.20] And with OpenAI solution, it's really a black box.
[1052.28 → 1055.14] You can't even see the prompt that's being generated.
[1055.52 → 1057.72] I'm not sure how to like to steer it better.
[1057.72 → 1064.14] Yeah, transparency is an issue in terms of – well, I guess it's nice when things go right.
[1065.00 → 1066.84] And it's sort of automagical.
[1067.12 → 1071.64] But then when things aren't going right, you really wish you could understand a bit more.
[1073.08 → 1077.52] So where are you in terms of your multimodal chat story?
[1077.92 → 1081.06] How far along are you in terms of what you're trying to get to?
[1081.06 → 1094.40] One of my main goals right now is to offer even more access controls and configuration over the interface experience like admins want to create.
[1094.40 → 1105.32] So, for example, I understand that, you know, especially the first time someone logs in here, they might not know, oh, what are all these models?
[1105.52 → 1107.08] I mean, I recognize Google, I guess.
[1107.30 → 1109.86] Or they would need a little more clues.
[1110.38 → 1113.36] Or they might not even think to click here for the model.
[1113.36 → 1116.82] But I really want to see an update.
[1117.26 → 1120.50] I'm actively working on this where there's just one dropdown.
[1121.20 → 1127.18] And you kind of get a bit of more info on that, what you're selecting, what it's good at.
[1127.32 → 1130.06] And it's like, okay, this guy can search the internet.
[1130.58 → 1132.42] And I need that for this task.
[1132.42 → 1138.52] And also just being able to control, like, which users can access what, too.
[1139.16 → 1142.46] Because that's a pretty big need, especially in the enterprise setting.
[1142.86 → 1155.06] So in terms of multimodality, like in the sense of AI being able to work with different formats, I think down to pipeline, we'll see integrations with videos.
[1155.06 → 1159.36] But right now we're handling vision with images.
[1160.30 → 1161.40] And that's pretty useful.
[1161.60 → 1163.00] It's been a huge help for me.
[1163.98 → 1174.82] So we started exploring Libra Chat at Prediction Guard because a bunch of our customers who are using Prediction Guard wanted a private chat interface.
[1174.92 → 1184.38] Because Prediction Guard itself is a platform that allows you to run large language models in a private secure environment with safeguards around them for, like, factuality.
[1184.38 → 1188.96] And toxicity and prompt injections and a bunch of other things.
[1189.14 → 1205.24] And so our customers are all this kind of privacy-focused, security-conscious customers who are maybe running Prediction Guard either on their own infrastructure and want a private chat interface for the models that they're hosting with Prediction Guard.
[1205.44 → 1211.70] Or they want an interface that's not a closed one for usage of our models.
[1211.70 → 1218.56] And so here what you can see is we've taken Libra Chat, which, again, Danny mentioned is open source.
[1218.80 → 1222.60] And we've been able to take it into our kind of branding.
[1223.10 → 1232.46] And we have Prediction Guard here where you can set your API key and use Prediction Guard running on top of our platform.
[1232.46 → 1242.04] And because it's open source, because it's transparent, we are able to take this and also, you know, integrate our own sort of flair into this.
[1242.40 → 1247.20] So I know an engineer from our team, Ed, and Danny work together.
[1247.36 → 1248.46] So thanks for that.
[1248.64 → 1255.60] Where we were able to integrate some of these checks for, like, toxicity and integrate our various models into the mix.
[1255.60 → 1260.48] So still kind of like Danny was showing in terms of running.
[1260.70 → 1262.46] Here I'm running with Neural Chat 7B.
[1262.64 → 1270.34] This is running in a privacy-conserving setup in Intel's AI cloud on Saudi 2 infrastructure.
[1270.52 → 1273.32] So it's a unique setup that we've kind of optimized.
[1273.74 → 1279.28] And we're able to connect to our own model, use this really slick interface, which is Libra Chat.
[1279.28 → 1284.78] It's just sort of branded a bit with our colours and logos and that sort of thing.
[1284.92 → 1290.88] But also we can integrate the unique features of our take on an AI system, right?
[1291.04 → 1299.28] So let's say I'm really concerned because I'm using an open model that doesn't have some of the surrounding guardrails, like closed source models.
[1299.28 → 1312.38] I can go into the config here and turn on a toxicity filter to make sure that the model isn't cursing me out or giving me any sort of, like, stuff that I don't want to see, right?
[1312.50 → 1316.36] And so here you can see we have a little toxicity score.
[1316.90 → 1319.96] Thankfully, it wasn't very toxic in this time around.
[1319.96 → 1333.08] So continuing similar to what Danny was showing, but again, our kind of own take on that with our models and kind of the safeguards around that.
[1333.54 → 1342.32] One cool thing that we found really useful is that a lot of our customers, they want an interface like this, but they also want it authenticated.
[1342.74 → 1344.98] So they have their system set up.
[1344.98 → 1348.48] So we've integrated, we're a G Suite company.
[1348.90 → 1355.40] So we've integrated Google login here, and it's only our org that can log in.
[1355.54 → 1358.70] So the prediction guard org, and now I'm authenticated.
[1358.96 → 1363.92] Here's my chat, like Danny mentioned, that is private and searchable.
[1363.92 → 1381.42] So, yeah, this has been a really amazing thing for us where we've been able to take and build on the great open source stuff that Danny has built at Liber Chat and create something that works really well for our customers and for our setup.
[1381.42 → 1388.48] So before I leave and stop screen sharing, I saw that there was a question earlier on about translation with language models.
[1388.68 → 1392.24] A lot of what we've been showing is English, right?
[1392.38 → 1401.44] Some language models like OpenAI, they say that they'll do other languages, but sometimes that doesn't always work out.
[1401.44 → 1404.82] So we have a translation endpoint in our API.
[1405.24 → 1420.86] And so we've done a bit of this testing with large language models, translation and kind of standard translation systems like Google Translate and Bing Translate and others or even other models like NLLB, No Language is Left Behind from Meta.
[1420.86 → 1430.64] And in our translation endpoint, you can send a translation and then actually get the result along with a score.
[1430.82 → 1435.08] So we're using Comet scoring, which is a way to score translations.
[1435.90 → 1447.78] And I think the question was, how well do large language models translate and are able to chat in different languages versus machine translating with a commercial translation system?
[1447.78 → 1470.44] So what we've seen in scoring both commercial translation systems and large language models is that some large language models, depending on the language, like if you're going into Hindi with OpenAI, you might get a good translation or one that is comparable to Google Translate a small amount of the time, like 5 to 10 percent.
[1470.44 → 1474.06] But mostly the commercial translation systems are generally better.
[1474.68 → 1482.58] And definitely as you go down the longer tail of languages, it gets sort of worse and worse, even in chat in like Mandarin.
[1482.80 → 1490.62] A lot of models don't do so good, even though that's kind of the next highest represented language in data sets out there.
[1491.28 → 1493.06] So, yeah, it's definitely a mixed bag there.
[1493.18 → 1495.96] I don't know if Danny or Chris, if you have a comment on that.
[1496.14 → 1498.78] But before we go to other questions, but I'm good.
[1498.78 → 1502.72] So some other questions on the Liber Chat side.
[1503.44 → 1510.54] Are you building tools for LLM evaluation since you have all the comparison models out there?
[1510.60 → 1515.34] I think they're kind of imagining, oh, I can switch between models easily in this interface.
[1515.50 → 1518.50] How does that help me in an interactive way?
[1518.56 → 1521.64] It could help me evaluate the performance of different models.
[1521.64 → 1526.48] But there's probably a non-interactive version of that, I guess.
[1526.48 → 1531.82] Maybe toward your roadmap, you were describing later the idea of automatically switching to optimize.
[1532.46 → 1534.82] So this would be an incremental step in that direction.
[1535.24 → 1535.86] Yeah, absolutely.
[1536.34 → 1545.98] Back to the data ownership, I just think it's absolutely crucial to have built some kind of pipeline for evaluation as well,
[1545.98 → 1549.88] especially if you're really into fine-tuning your own models.
[1549.88 → 1557.92] And really, it's crazy to think about, but even the data that we have just casually with these large language models,
[1558.58 → 1562.80] and if they're a very capable model, it's almost like a goldmine for the next model.
[1562.80 → 1567.22] And just having that at your own ownership, not just some cloud service.
[1567.76 → 1572.24] I definitely want to start it off simple, being able to thumbs up, thumbs down,
[1572.36 → 1582.44] but then being able to integrate complex evaluation tools like you guys already have with the toxicity score or the translation rating.
[1582.64 → 1583.60] I think that's awesome.
[1584.32 → 1584.46] Cool.
[1585.16 → 1587.12] Could you talk a little bit, this isn't one of the questions,
[1587.12 → 1590.44] but I saw in your documentation discussion of like plugins.
[1590.74 → 1594.44] Could you talk about that a little bit, like what that means in the context of Liber Chat?
[1595.08 → 1606.50] So they are inspired by just ChatGPT's use of plugins and really what the AI services now refer to as tools or functions.
[1607.36 → 1616.30] And really, it's just a way to be able to interact with some algorithm or API that's kind of programmed there already.
[1616.30 → 1623.62] And you're just kind of letting the model decide the inputs and outputs or the inputs and rather interpret the outputs.
[1624.24 → 1633.66] And I'm using it, obviously, in the plugin system where you can make requests to Dolly or Staple Diffusion for image generations.
[1634.12 → 1637.98] You can search archive papers, things like that.
[1637.98 → 1645.26] But really, what I came up with, the plugin system specifically is almost a year old now, which is crazy.
[1645.78 → 1651.18] But I actually developed it before OpenAI had these functions in their API.
[1651.96 → 1659.74] So in the process, I learned kind of deeply how these LLMs were understanding certain tokens a little better for formatting.
[1659.74 → 1669.82] And now we have such a rich environment now for getting only JSON responses or being able to use tools with Anthropic.
[1669.82 → 1677.54] So I've got a lot of things planned there where I want to see just that tool environment really grow.
[1677.92 → 1691.88] And also, like, for people who are building on top of Albrecht, I want to see better documentation and better developer experience in, like, adding those extra tools where, you know, this is a tool only my company can see.
[1691.88 → 1695.08] And just being able to, like, plop it in real quick.
[1695.50 → 1702.26] I'm looking at your GitHub and notice 117 contributors listed there.
[1702.42 → 1714.08] As your community built up around this has evolved, going from, you know, sole developer in the beginning, and now you have a group of people that are actively contributing at some level.
[1714.08 → 1723.88] How has that changed the project and changed how you're spending your time to fulfill the expectations of so many people and all the folks that they're serving in turn?
[1724.44 → 1725.44] Yeah, it's been amazing.
[1725.74 → 1727.30] I've learned so much in the process.
[1727.76 → 1735.68] I think I need to be conservative with my estimates on getting things done so I can address contributions and things like that.
[1735.68 → 1741.06] And that is definitely a thing I want to keep, if anything, even more, devote more time.
[1741.38 → 1743.28] Because some people are making really great things.
[1743.28 → 1748.22] You know, I'll even shout out Marco, who is constantly contributing things.
[1748.36 → 1754.28] And there are things that he just gets through so much quicker than I do that I don't quite find time to review.
[1754.42 → 1756.54] But it's sitting there, and it's great.
[1756.62 → 1757.42] It's already working.
[1757.84 → 1759.80] And I want to dig in the weeds a little bit.
[1760.08 → 1764.04] But also, I think that's really what's helped the project explode, too.
[1764.24 → 1768.36] That there's such an openness to what people want to see in it.
[1768.36 → 1775.22] You know, I just had someone today say that they were, it was their first open source contribution.
[1775.60 → 1781.16] And I just thought that was, you know, that's really cool to see just kind of people learning in the process.
[1781.42 → 1782.98] And I was there, too.
[1783.24 → 1786.38] I was always kind of daunted of, like, contributing to anything.
[1786.38 → 1791.32] So just seeing people, you know, step in the water, I definitely want to foster that more.
[1791.32 → 1799.10] I'm curious, as kind of follow-up to that, has there been a point where you've seen adoption occurring?
[1799.70 → 1804.62] And as part of that adoption, you know, not that you have favourite children, so to speak.
[1804.70 → 1809.46] And I understand, you know, that you're super happy for every organization out there.
[1809.46 → 1822.84] But has there been a moment where you've seen some organization that, you know, you might be super familiar with or something adopt or know about, you know, and kind of went, holy mackerel, I can't believe that they're using my stuff.
[1823.00 → 1824.86] Has there been a moment like that for you?
[1825.20 → 1826.36] Oh, yeah, for sure.
[1827.64 → 1833.44] I caught wind of Mistral using the app just to prototype their chat interface.
[1833.44 → 1835.98] That's the only one I know for sure.
[1836.58 → 1844.90] But I've also, you know, there have been people within Microsoft who are kind of just helping people prototype, you know, their own interfaces and things like that.
[1844.96 → 1849.74] And it's just like that to me is, you know, a step back, and I'm just kind of blown away.
[1850.38 → 1852.24] The big boys of this space, definitely.
[1852.62 → 1852.80] Yeah.
[1853.18 → 1863.26] In our system, in the way that we've kind of customized Libra Chat here, we use this model-based factuality score, which is actually factual consistency.
[1863.44 → 1867.68] Between reference text and text out of an LLM.
[1867.78 → 1876.88] So you can do a factuality check between two different pieces of text to get a score that would show kind of factual consistency between the two.
[1877.06 → 1887.20] Which that's kind of the most relevant thing for most LLM use cases because many people are using RAG, or they have internal company data that represents a source of truth.
[1887.20 → 1894.56] So in Libra Chat here, we're working on the integration with the RAG piece, which would be a cool integration there.
[1894.76 → 1898.50] But for now, we just have this sort of factuality context.
[1898.50 → 1900.34] So facts that shouldn't be violated.
[1901.04 → 1901.14] Right.
[1901.24 → 1908.88] And I could put something here and turn on the factuality check and then ask a question.
[1908.88 → 1912.00] So the fact I put in was that the sky was green.
[1912.10 → 1914.82] I could ask, you know, what colour is the sky?
[1915.30 → 1919.28] And then I think neural chat will actually respond factually.
[1919.28 → 1925.36] But I'll do the check against the gold standard information that I put in, which is actually that the sky is green.
[1925.62 → 1929.90] And you can see that I get out a factuality score, which ranges from zero to one.
[1929.90 → 1936.80] And in this case, it's very low because I put in that information about the sky being green.
[1937.50 → 1939.90] So, yeah, that's the sort of interesting way.
[1940.90 → 1951.96] You know, I'm so thankful for this project being open source and being customizable because this is the kind of cool stuff that people are enabling within their own chat interfaces that we're working with.
[1952.02 → 1955.76] And it's awesome to have a robust system that works well in that way.
[1956.38 → 1958.52] Looks like there's another question.
[1958.52 → 1971.64] Danny, how feasible and something that you would venture yourself into is combining Albrecht with such frameworks as Flow Wise or Cray?
[1972.86 → 1974.28] I don't know how to say that.
[1974.66 → 1975.58] I don't know what that is.
[1976.28 → 1977.42] I think it's Crew AI.
[1977.76 → 1978.38] Crew AI.
[1978.56 → 1979.04] There we go.
[1979.18 → 1979.36] Yeah.
[1980.18 → 1982.40] I don't know if you know of those things, but.
[1982.98 → 1985.08] Yeah, I'm familiar with both.
[1985.08 → 1996.18] I think Flow Wise is really great giving that string-based logic, user interface logic that, you know, no programming, you kind of put all the pieces together.
[1996.52 → 2004.02] I see that being integrated much sooner in Crew AI, which is more of like an agent orchestration framework.
[2004.02 → 2017.54] With Flow Wise, I think it could serve as kind of like another back end, you know, like just like you see another, so many endpoints, as I like to call them, which are Mistral, Google, OpenAI, so forth.
[2017.54 → 2026.86] I could see it being easily integrated like that, where I don't really want to reinvent the wheel with something like that because they've done such a great job.
[2027.42 → 2030.48] And I just want to be able to handle the integrations.
[2031.24 → 2034.98] But, you know, because obviously it's not going to be everyone's need.
[2034.98 → 2039.06] And for Crew AI, you know, I definitely have a lot of ideas there.
[2039.26 → 2050.56] I'm trying to establish kind of like a framework for agents first and then potentially, you know, get into agent orchestration where agents are talking to each other and things like this.
[2051.06 → 2053.16] But we're not quite there yet.
[2054.32 → 2060.50] We've got the OpenAI side shaping up, but we want to see some open source integrations there.
[2060.50 → 2068.52] Awesome. Well, I think this is a good question to maybe kind of draw near to a close here.
[2068.60 → 2085.32] It's something we something asked in the webinar chat, but also something we usually kind of ask people that we're talking to on the podcast is, you know, you're following and kind of plugged into all of these different things that are happening in the AI ecosystem.
[2085.32 → 2094.22] And, you know, things even I'm learning about today that even though we're, I think, you know, we would be plugged into many things that we hear about this.
[2094.38 → 2109.38] But there's just so much going on after kind of looking at that landscape and, you know, how innovation is happening, how people are using your interface, but also more widely the things that you're seeing people do in the open source space or otherwise.
[2109.38 → 2124.82] Where do you see all this kind of going, and how do you see the future of both Libra chat and maybe even just things that you're is there something you're particularly interested in the AI space to see how it develops in the coming year?
[2124.82 → 2131.16] Yeah, I think kind of been hinting at this already, but just I think the future it's the future I want to see.
[2131.30 → 2134.04] And I feel like a lot of people in tech want to see it, too.
[2134.18 → 2140.14] And it's the open source future where these large language models are getting so good every day.
[2140.46 → 2146.40] There's a lot more time and money invested in being able to host these things just from a consumer grade computer.
[2146.40 → 2161.60] And I think catering to that is probably going to be the direction of my project and many similar projects because it even blows my mind that I can use something like Llama 3, where a year ago I might have thought, oh, this is two years away.
[2161.60 → 2167.30] And I really think that's the direction both on the high level and low level.
[2168.04 → 2182.28] And I think it's part of the reason it's the projects really taken off just because these things are so accessible, and we don't have to pay SAS subscription money to just use a message for AI.
[2182.28 → 2192.18] Yeah, that's awesome. I think that's a future that at least Chris and I are looking forward to, and I'm sure many on the webinar.
[2192.50 → 2194.62] You mean I get my wallet back at some point?
[2196.28 → 2203.76] Well, I'm sure there'll be other things to pay for, but, you know, new AI PC or something to run all your local models.
[2204.48 → 2205.30] That's right.
[2205.58 → 2208.78] Cool. Well, thank you so much, Danny, for taking time.
[2208.78 → 2211.92] Thank you to everyone that joined the webinar.
[2212.30 → 2214.36] This was a ton of fun.
[2214.90 → 2218.34] We're going to be doing another one of these webinars very soon.
[2218.46 → 2233.62] The next one, I think, will be around multimodal AI and some practical like hands on instruction in how to create things like multimodal rag systems or kind of search over images and videos.
[2234.04 → 2236.26] And so that's going to be a ton of fun.
[2236.36 → 2238.00] So keep on the watch for that.
[2238.00 → 2239.12] That's going to be a fun one.
[2239.56 → 2240.34] Until then.
[2240.60 → 2240.88] Yeah.
[2240.94 → 2244.76] Looking forward to seeing you next time, Chris, on the podcast.
[2245.10 → 2245.46] Absolutely.
[2245.64 → 2246.22] Thank you, Danny.
[2246.36 → 2247.84] Thanks to everyone who joined us today.
[2248.30 → 2249.22] Yeah, you guys are awesome.
[2249.60 → 2250.34] Thanks for having me.
[2250.34 → 2258.52] All right.
[2258.52 → 2261.30] That is practical AI for this week.
[2262.10 → 2263.14] Subscribe now.
[2263.30 → 2274.70] If you haven't already, head to practicalai.fm for all the ways and join our free Slack team where you can hang out with Daniel, Chris and the entire changelog community.
[2274.70 → 2279.94] Sign up today at practicalai.fm slash community.
[2280.46 → 2287.46] Thanks again to our partners at fly.io, to our beat freaking residents, Break master Cylinder, and to you for listening.
[2287.80 → 2289.58] We appreciate you spending time with us.
[2289.96 → 2291.10] That's all for now.
[2291.60 → 2293.02] We'll talk to you again next time.
[2293.68 → 2294.04] Peace.
[2296.12 → 2297.50] Cheers.
[2297.98 → 2298.34] Excited.
[2298.66 → 2299.24] Cheers.
[2299.26 → 2299.68] Cheers.
[2299.72 → 2299.80] Cheers.
[2299.90 → 2300.00] Cheers.
[2300.00 → 2300.12] Cheers.
[2300.70 → 2301.22] Cheers.
[2301.22 → 2302.10] Hm.
[2302.10 → 2304.02] Cheers.
[2304.02 → 2304.32] Cheers.
[2304.32 → 2305.94] Cheers.
[2305.94 → 2306.70] Cheers.
[2306.70 → 2308.36] Cheers.
[2308.36 → 2309.44] Cheers.
[2311.62 → 2316.52] Cheers.
[2316.52 → 2316.58] Yeah.
[2316.70 → 2317.30] Cheers.
[2317.30 → 2317.50] Cheers.
[2317.50 → 2317.74] Cheers.
[2317.78 → 2317.98] Cheers.
[2317.98 → 2318.56] Cheers.
[2318.56 → 2318.76] Cheers.
[2318.76 → 2319.28] Cheers.
