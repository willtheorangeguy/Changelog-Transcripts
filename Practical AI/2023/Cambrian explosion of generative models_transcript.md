[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.02 --> 36.08]  Learn more at fly.io.
[43.14 --> 47.30]  Welcome to another fully connected episode of Practical AI.
[47.70 --> 52.72]  In these episodes, Chris and I keep you fully connected with everything that's happening
[52.72 --> 53.94]  in the AI community.
[53.94 --> 59.58]  We'll take some time to discuss the latest news and also dig into some learning resources
[59.58 --> 61.90]  to help you level up your machine learning game.
[62.46 --> 63.28]  I'm Daniel Whitenack.
[63.36 --> 65.84]  I'm a founder and data scientist at Prediction Guard.
[66.00 --> 70.62]  And I'm joined as always by Chris Benson, who is a tech strategist at Lockheed Martin.
[70.96 --> 71.60]  How are you doing, Chris?
[71.96 --> 73.10]  I'm doing very well, Daniel.
[73.28 --> 75.60]  It's more interesting times ahead of us.
[76.00 --> 78.90]  You know, I'm thinking about changing jobs.
[78.90 --> 84.04]  I'm thinking about like a job title called something like, I don't know, generative juggler.
[84.30 --> 84.70]  What do you think?
[85.70 --> 86.18]  Yeah.
[86.30 --> 87.42]  Because it sounds fun.
[87.48 --> 89.24]  You know, I mean, I can totally see.
[89.46 --> 90.38]  Llama Wrangler.
[90.64 --> 92.08]  Oh, I love that.
[92.34 --> 93.94]  That's perfect for me, too.
[94.18 --> 95.38]  I'm all over that.
[95.64 --> 95.94]  Okay.
[96.32 --> 99.18]  Of course, our listeners know that you're a big animal advocate.
[99.18 --> 105.98]  What is an animal advocate's perspective on the use of all of this llama, camel, all this
[105.98 --> 108.06]  sort of different usage of animals?
[108.30 --> 109.98]  Do you find it fun and interesting?
[110.34 --> 110.84]  Of course.
[111.30 --> 113.70]  We should all have animals on the mind all the time.
[113.80 --> 115.00]  I mean, it makes us better people.
[115.28 --> 115.54]  Yes.
[116.98 --> 117.42]  Yeah.
[117.64 --> 118.20]  I'm traveling.
[118.34 --> 123.46]  My wife just sent me a picture of our dog laying on the floor in a funny position looking
[123.46 --> 124.60]  out of the corner of his eye.
[124.72 --> 127.62]  So it made me happy going into this recording.
[127.78 --> 128.68]  So that's always good.
[128.68 --> 129.50]  That sounds good.
[129.70 --> 132.28]  You know, the pet pictures are really important when you're traveling.
[132.46 --> 133.62]  My wife does that with me.
[133.76 --> 133.96]  Yeah.
[134.12 --> 135.26]  She'll send a good moment.
[135.68 --> 141.14]  So, you know, in the face of all this technology change constantly coming at us, it keeps our
[141.14 --> 141.98]  humanity intact.
[142.40 --> 142.66]  Yeah.
[142.78 --> 142.98]  Yeah.
[142.98 --> 147.26]  And it is a crazy time in the AI community.
[148.42 --> 154.42]  So we use these fully connected episodes to update people on different news and that sort
[154.42 --> 154.78]  of thing.
[154.78 --> 160.06]  And one of the things I was realizing this week as we were prepping for this episode is I've
[160.06 --> 165.78]  even seen there's people and I think there's a website talking about the Cambrian explosion
[165.78 --> 169.64]  of models or the proliferation of models.
[169.84 --> 175.44]  So, you know, there's just in the past couple of weeks, there's so many different ones that
[175.44 --> 176.56]  have come out.
[176.56 --> 178.16]  But it is really a proliferation.
[178.52 --> 181.78]  So I thought it'd be good to highlight a few of those.
[181.86 --> 184.32]  We can't get to all of them because there's just so many.
[185.04 --> 191.28]  But one thing as a tip to people, sometimes how I look at this is I'll go to Hugging Face
[191.28 --> 193.42]  and just go to the models tab.
[194.02 --> 199.32]  And if you make sure that it's sorted by trending, that's kind of a cool way to see, hey, what's
[199.32 --> 199.78]  at the top?
[199.90 --> 204.04]  And, you know, you can filter by different types of models, but I found it kind of interesting
[204.04 --> 206.34]  to just look at what's trending overall.
[206.34 --> 213.56]  Because as of now on the Hugging Face hub, it's a mix between kind of video generation,
[213.80 --> 216.18]  image generation, language generation models.
[216.80 --> 221.72]  And over time, you can see kind of which of those categories is trending up or down.
[222.14 --> 222.46]  I don't know.
[222.50 --> 225.68]  There's probably an app that needs to be made to track that sort of thing.
[225.76 --> 227.10]  But I'll let someone else do that.
[227.64 --> 235.64]  One of the ones that I wanted to highlight was the new stable diffusion XL 0.9.
[235.64 --> 241.04]  Also, these model names are getting a little bit more complicated over time, I've found.
[241.64 --> 246.34]  But stable diffusion XL 0.9 or SD XL.
[246.78 --> 250.58]  This is, of course, people probably remember stable diffusion.
[250.88 --> 253.74]  This is an image generation model.
[253.92 --> 258.54]  So you put in a text prompt and then out comes an image.
[258.54 --> 265.60]  So something like astronaut riding a horse on the moon photorealistic or something like that.
[265.64 --> 267.56]  And you get an image out.
[267.84 --> 270.42]  This one is kind of interesting.
[270.84 --> 272.40]  I think it was back in April.
[272.40 --> 276.28]  They announced some kind of private access to this or beta access.
[276.50 --> 279.38]  Now the model is up on Hugging Face.
[279.50 --> 283.76]  It is available, but under only a research only license.
[284.16 --> 287.36]  But the images, I don't know if you've seen some of these, Chris.
[287.52 --> 289.30]  I'm looking at them now while we're talking.
[289.66 --> 294.36]  Yeah, you played with stable diffusion back, you know, when the previous kind of iteration.
[294.36 --> 297.12]  What is your thought in terms of the progression of this?
[297.48 --> 302.16]  Oh, I mean, it was like, I remember when we were playing, we were actually doing it on one of our episodes.
[302.54 --> 302.66]  Yeah.
[302.74 --> 304.92]  And we were coming up raccoons all over the place.
[304.98 --> 306.80]  I remember at the time.
[307.00 --> 307.88]  There were raccoons everywhere.
[307.98 --> 308.48]  Not just us.
[308.48 --> 311.34]  There seemed to be lots of raccoons coming out of stable diffusion.
[311.80 --> 313.66]  Regardless, I was rather wondering about that.
[313.98 --> 316.42]  But no, I'm looking through some of the things.
[316.58 --> 320.82]  And just like the imagery has come so far and the capability and what you can do.
[320.96 --> 323.36]  And that's just a few months since we were doing that.
[323.60 --> 328.02]  So I'm in awe right now as I look at these shots as we're talking.
[328.44 --> 333.58]  At least the last time I checked, and this might be different now that if you're listening to this episode, it might be different.
[333.58 --> 338.74]  But at the time today, there was a blog post about the release from Stability.
[339.34 --> 343.36]  And they mentioned that there's going to be a follow-up, more technical, deep dive.
[343.78 --> 346.76]  I don't know if it's a full paper or just a deep dive post.
[347.06 --> 350.96]  But there are some general descriptions of how this is working.
[351.26 --> 353.54]  And you can dig into it a little bit.
[353.54 --> 366.50]  So instead of there being sort of one step or a one model kind of situation in this image generation, apparently this model consists of a two-step pipeline.
[367.00 --> 368.46]  It's still diffusion-based.
[368.70 --> 374.30]  But there's one model that generates, they say, latence of the desired output size.
[374.42 --> 379.54]  And the second step is specialized to generate this sort of high-resolution image.
[380.36 --> 381.94]  So it's like an image-to-image model.
[381.94 --> 389.92]  They combine these, and the second stage of the model then kind of adds finer details to the generated output.
[390.10 --> 393.18]  So that's one interesting thing, which also is kind of interesting.
[393.32 --> 399.96]  I don't know if you've been following all of the everyone talking about what's going on, quote-unquote, in GPT-4.
[399.96 --> 412.36]  But I think there's a lot of speculation and evidence that that also is a sort of mixture of experts, multiple models together, not just a single model call.
[412.54 --> 414.48]  So I find this trend kind of interesting.
[414.84 --> 420.24]  Do you have any thoughts around, like, what is the virtue of having the kind of the multi-step, multi-model approach?
[420.24 --> 428.90]  And do you think that that's likely to be kind of a general architecture that we see continually overboard instead of just having the model?
[429.10 --> 432.56]  I mean, even going back to the stable diffusion, I noticed the two models you mentioned.
[433.22 --> 437.86]  And interestingly, the second model is basically twice the size of the first one in terms of parameters.
[438.42 --> 442.00]  Any thoughts around the science or math around that or why you would take that approach?
[442.00 --> 453.58]  Yeah, as you scale up your data set and you scale up your compute, for a given model size, you're going to get diminishing returns on the performance of that model.
[453.72 --> 460.04]  So in some ways, given a certain amount of data in a model architecture, what are you going to improve more?
[460.10 --> 461.20]  You could train for longer.
[461.72 --> 463.16]  You could train on more data.
[463.16 --> 476.38]  But at the levels that some of these models are at now, thinking particularly about OpenAI, you know, what more can they do right now with respect to training longer with the same model architecture or more data?
[476.78 --> 483.02]  So what's a natural way to improve output but combining multiple models, a pipeline together?
[483.02 --> 487.02]  Now, I think that you'll see probably advances in architectures.
[487.78 --> 494.24]  So different model architectures will continue to come out and maybe break some of that trend.
[494.90 --> 509.52]  Another way that you see this kind of multiple models being applied is in things like the RLHF process, which we talked about on the show, the reinforcement learning from human feedback, which things like this have been around for quite some time.
[509.52 --> 513.26]  So GANs, for example, include two different models, right?
[513.28 --> 515.18]  A generative model and the discriminator.
[515.64 --> 531.26]  These sort of like multi-model workflows that produce an instruction-tuned or tuned model out the other end, I think we'll continue to see a lot of that as well, even if the model that's produced or used for inference at the end is a single inference.
[531.64 --> 534.56]  I got one other question before we dive into the rest of the models to release.
[534.56 --> 549.90]  One of the things that was notable was OpenAI kind of commented after GPT-4 that there was only so much vertical growth you could have there given the data set, basically, I mean, the whole internet in a model.
[550.08 --> 552.42]  So you can't just keep growing them like that.
[552.84 --> 560.10]  Here we find ourselves in this, what we've kind of described as the proliferation kind of episode, talking about all these models coming out.
[560.10 --> 574.24]  Do you think part of what we're looking at today is generated by the fact that when you lose the potential for further vertical growth, because you basically used all the data that's out there, does that give all of these other model creators a chance to catch up to some degree?
[574.46 --> 583.16]  So that you kind of, you had the surging of the leader, but once they hit kind of a barrier there, now you're seeing many, many catching up and comparing themselves to that.
[583.32 --> 586.74]  Is that a fair assessment in terms of kind of what we're looking at now?
[586.74 --> 599.72]  Yeah, people probably have seen this post that went sort of viral, which is supposedly a leaked document from Google saying, you know, we have no mode and neither does OpenAI.
[600.04 --> 610.58]  And they talk about how basically, I think the phrase they use is open sources eating our lunch, like we're not positioned as major players to compete necessarily.
[610.58 --> 617.54]  So I think that that's where that sentiment is probably coming from wherever that document originated.
[618.10 --> 621.24]  That would be the sentiment that's being expressed there.
[621.44 --> 629.06]  So the ability to have a foundation model is no longer this sort of moat that separates you.
[629.06 --> 643.56]  Because now there's open source models, there's really good open source models that maybe the base model, let's say the base model doesn't perform as good in a general purpose way as GPT-4 or something like that.
[643.92 --> 649.92]  Well, the reality is that like in your business environment, you don't need a general purpose model.
[650.16 --> 652.98]  That's usually not what you need, right?
[653.20 --> 657.10]  What you need is a model that performs really well for your task.
[657.10 --> 679.10]  And so in that sense, having a really good open access, whether it's a language model or an image generation model, and then having the ability, which we have now, to adapt or fine tune that model with your own private data, actually is kind of part of what we're seeing with this proliferation, I would say.
[679.10 --> 685.22]  An example of this is the next model I was going to highlight, which I think is a really good example of this.
[685.22 --> 687.36]  So I saw this in a tweet.
[687.68 --> 692.06]  I don't know the actual day it was released, but the open chat models.
[692.26 --> 694.58]  So if you just go to hugging face slash open chat.
[694.76 --> 700.30]  So there was a model that kind of outpaced chat GPT in some benchmarks.
[700.30 --> 702.20]  So there's a Bakuna benchmark.
[702.56 --> 713.90]  That model wasn't as open, but these open chat models are the first open models to outpace chat GPT with GPT 3.5 in this benchmark.
[713.90 --> 738.80]  And what's interesting is this is another very much a trend that we're seeing more and more and more of is actually using the closed proprietary, but really impressively performing models like GPT 4 to actually create data for you to fine tune an open model, which then performs or maybe performs better than the closed models, at least in certain scenarios.
[738.80 --> 739.80]  So that's what they did.
[739.80 --> 751.30]  They used 6,000 conversations generated out of GPT 4 to fine tune this model, which actually outperforms and is available publicly.
[751.64 --> 753.26]  And this we're seeing over and over.
[753.38 --> 758.20]  So there's other models like people are generating this data for less than $1,000, right?
[758.20 --> 767.24]  They're using the OpenAI API less than $1,000 to create these models that are really impressive in how they perform.
[767.38 --> 770.96]  Now, I think there's all sorts of interesting implications of that.
[771.50 --> 778.64]  And part of me wonders, well, how is OpenAI going to shift its business model to make that sort of thing less?
[779.50 --> 781.46]  Or other providers of foundation models?
[781.46 --> 795.18]  One result of this might be that we see providers like OpenAI try to prevent usage like this, where you're just using their API to generate data to create a model that works better for you than using their API.
[795.58 --> 796.32]  I don't know.
[796.46 --> 796.80]  We'll see.
[797.84 --> 805.34]  If you kind of back away for a second and look at the history of this, it's starting to look a lot like the way software development went open source.
[805.34 --> 813.82]  You know, if you look back around, you know, 2000 or even down into the 90s before that, you saw all of these proprietary programming languages.
[814.20 --> 815.12]  You know, you'd pay for them.
[815.18 --> 817.18]  You had to pay for environments and stuff like that.
[817.18 --> 819.50]  And gradually open source overtook it.
[819.72 --> 825.12]  And from my perspective, it's feeling a lot of the same right now as we're making a shift.
[825.12 --> 834.86]  I will leave it by saying I'm wondering if to that point about your unknown source document earlier, whether or not that's kind of an inevitable destination we're going to.
[835.34 --> 842.10]  This is a changelog news break.
[842.46 --> 845.82]  Can you trust ChatGPT's package recommendations?
[846.34 --> 847.68]  Mmm, not so much.
[848.12 --> 854.08]  The team at Vulkan have published a new security threat vector they're calling AI Package Hallucination.
[854.08 --> 856.68]  Mmm, that sounds good.
[857.06 --> 857.72]  I'll have that.
[857.72 --> 866.08]  It relies on the fact that ChatGPT sometimes answers questions with hallucinated sources, links, blogs, and statistics.
[866.56 --> 872.52]  It'll even generate questionable fixes to CVEs and offer links to libraries that don't actually exist.
[872.62 --> 874.04]  What about the RUSs?
[874.42 --> 875.66]  Rodents of unusual size?
[876.44 --> 877.54]  I don't think they exist.
[877.54 --> 884.84]  Quote, when the attacker finds a recommendation for an unpublished package, they can publish their own malicious package in its place.
[885.32 --> 893.10]  The next time a user asks a similar question, they may receive a recommendation from ChatGPT to use the now existing malicious package.
[893.58 --> 893.94]  End quote.
[893.94 --> 900.98]  These AI tools like ChatGPT are a real boost to developer productivity, but be careful out there.
[900.98 --> 906.42]  You just heard one of our five top stories from Monday's Changelog News.
[906.80 --> 919.20]  Subscribe to the podcast to get all of the week's top stories and pop your email address in at changelog.com slash news to also receive our free companion email with even more developer news worth your attention.
[919.64 --> 923.08]  Once again, that's changelog.com slash news.
[927.22 --> 929.26]  We've been talking about open source models.
[929.26 --> 936.82]  Some things that we talked about even like two months ago on this show, like someday these things will happen.
[936.94 --> 946.76]  I remember us talking about the graph that I think Clem from Hugging Face posted on Twitter where, you know, you kind of got this linear progression of these closed source models.
[946.76 --> 954.76]  And then eventually there's this kind of exponential increase of open models that surpasses the performance of the closed models.
[954.76 --> 962.94]  And I don't know if we're totally in that place yet, but it kind of seems like it's happening to some degree.
[962.94 --> 963.30]  Yeah.
[963.42 --> 965.56]  And maybe not in certain ways.
[965.72 --> 970.86]  So I think still for like general purpose, like this model can do whatever you ask it to do.
[970.98 --> 976.44]  Those sorts of use cases, still the closed models are winning, I think.
[976.44 --> 982.20]  But like I said, how many business use cases do you need a model that does that sort of thing?
[982.36 --> 984.06]  The majority, you don't need that.
[984.70 --> 998.94]  So maybe for the actual proliferation of these models in business use cases, all that really matters is that you can have open models that perform really well for all those business use cases.
[998.94 --> 1005.30]  And that brings up, of course, a lot of other concerns and practical implications.
[1005.66 --> 1007.22]  So open models are great.
[1007.24 --> 1008.90]  If they perform better, that's great.
[1009.44 --> 1019.08]  But there is a lot of, I mean, it's not only that OpenAI or Cohere or Anthropic or whoever who are running these models that the model is good.
[1019.08 --> 1027.34]  They also have a really nice and easy to use API that generally is up, although I think ChatGPT was down the other night.
[1027.60 --> 1032.68]  But yeah, generally is good and like well-maintained and all that.
[1032.82 --> 1034.40]  You don't get that with these open models.
[1034.72 --> 1040.82]  You have to figure that bit out yourself, which has other sort of engineering implications and infrastructure implications.
[1040.82 --> 1050.30]  And obviously, going back to someone I know here, there are business opportunities available to help people on board on those things.
[1050.50 --> 1051.12]  So there's a lot.
[1051.52 --> 1053.08]  It's so much happening right now.
[1053.16 --> 1056.24]  As you said two months ago, and now it's already changing.
[1056.96 --> 1061.80]  And I think people need to get used to the new speed of how fast this is happening at this point.
[1062.36 --> 1063.68]  Later on, I'll come back to that.
[1063.68 --> 1070.32]  One other one that is trending at least this week on Hugging Face is ZeroScope XL.
[1070.62 --> 1072.92]  Version 2 is the one that I'm looking at.
[1073.02 --> 1075.86]  But if you just search for ZeroScope, you'll find it.
[1075.92 --> 1079.10]  This is a video generation model, which is pretty cool.
[1079.22 --> 1080.30]  So it's video generation.
[1080.64 --> 1083.48]  It produces watermark-free videos.
[1084.38 --> 1089.68]  And one of the things I find interesting about this model, the ZeroScope model,
[1089.68 --> 1098.06]  and also the stable diffusion model that we mentioned a second ago, is you can run these on some sort of commodity hardware.
[1098.06 --> 1108.14]  Maybe not the cheapest of commodity hardware, but this model supposedly uses a little over 15 gigabytes of GPU memory,
[1108.52 --> 1113.90]  rendering 30 frames at 1024 by 576.
[1113.90 --> 1125.76]  So that sort of hardware is definitely within reach for a lot of people, even in platforms where you can access some of that for free for at least some time.
[1125.94 --> 1130.10]  So yeah, that's one of the things that I find interesting about some of these models as well.
[1130.52 --> 1130.90]  That's cool.
[1131.14 --> 1133.88]  We're seeing more and more video generation recently.
[1133.88 --> 1141.94]  It wasn't long ago, it was earlier this year, that we were talking about kind of moving there as we were coming into 2023
[1141.94 --> 1146.34]  and the fact that we were expecting it, but it hadn't really arrived yet.
[1146.48 --> 1150.20]  And now it's already, to your Cambrian point, it has blown up.
[1150.26 --> 1155.88]  And we're seeing multiple opportunities in terms of these models already in open source versions as well.
[1155.88 --> 1163.92]  So how do you, I'm kind of curious, Daniel, how do you as a practitioner, as you're looking at this explosion of these different options coming at you,
[1163.96 --> 1164.94]  how do you make an evaluation?
[1165.54 --> 1173.02]  I've had people ask me that recently, like so much is happening now, I don't even know how to evaluate one option versus another.
[1173.16 --> 1175.06]  Do you have any thoughts on framing that?
[1175.38 --> 1182.34]  I think there's a bunch of different axes that you could kind of narrow down your choices along.
[1182.34 --> 1187.00]  So let's say that you have a commercial use case, right?
[1187.90 --> 1196.16]  That alone is a filter by which you can knock out a huge amount of models, because just looking at the ones we've listed so far,
[1196.66 --> 1200.98]  Xeroscope, released under Creative Commons, non-commercial, can't use it.
[1201.48 --> 1204.92]  OpenChat, released under the Llama license, can't use it for commercial.
[1205.38 --> 1210.22]  Stable Diffusion XL, 0.9, available only for research, can't use it.
[1210.22 --> 1215.74]  So not that you couldn't prototype with it or that versions of this wouldn't be eventually released,
[1215.96 --> 1223.40]  or you could access them in other commercial products, but that kind of does narrow down your cases quite a bit,
[1223.50 --> 1227.64]  whereas you look at certain models like the MPT family from Mosaic,
[1228.32 --> 1233.16]  released under licenses that allow you to use them for commercial purposes, etc.
[1233.32 --> 1234.78]  So that's an easy one.
[1234.94 --> 1235.82]  What is your use case?
[1236.02 --> 1236.70]  Are you commercial?
[1236.92 --> 1238.18]  Well, that knocks out a whole bunch.
[1238.18 --> 1243.04]  Then you have a smaller set, and then I think you need to do a second layer of filtering,
[1243.34 --> 1247.10]  which is think about your practical use of this model.
[1247.24 --> 1252.72]  So for example, let's say that I want to use an LLM to extract a bunch of information
[1252.72 --> 1256.12]  from a huge number of unstructured documents.
[1256.82 --> 1261.76]  I've got maybe millions of documents, and I want to extract information from them.
[1261.76 --> 1267.78]  Okay, well, if each inference is going to take 20 or 30 seconds for me,
[1267.98 --> 1270.56]  and I would need to extract a bunch of information,
[1270.56 --> 1273.72]  then that's going to become a major problem.
[1274.06 --> 1277.38]  So then I need to think about, like, how am I going to use this,
[1277.40 --> 1282.98]  and what are the constraints around, like, the inference speed and the interaction with the model,
[1282.98 --> 1286.70]  or the context length that I'm putting in in the case of large language models?
[1286.70 --> 1289.82]  Do I need to put in a bunch of information or a small amount?
[1290.30 --> 1293.32]  And that narrows down to models that are maybe smaller,
[1293.54 --> 1298.54]  that can be run faster for inference, or models that support larger inputs, right?
[1298.68 --> 1300.20]  So there's those concerns.
[1300.32 --> 1302.06]  And then finally, once you get down to that,
[1302.12 --> 1306.58]  let's say you found one that fits your use case and the constraints that you're working under,
[1306.98 --> 1309.60]  then I think it gets down to this sort of,
[1309.82 --> 1312.50]  I guess we call it old-fashioned, oh, it's not that old-fashioned.
[1312.98 --> 1314.36]  Create yourself a test set.
[1314.36 --> 1316.46]  That's still the best way to do this, right?
[1316.60 --> 1322.66]  If you have, you know, even 100, 200 examples that you've manually labeled as,
[1322.94 --> 1325.94]  this is what I would like to go in, and this is what I would like to come out,
[1326.06 --> 1331.04]  then you should just check the output and see, you know, what is the accuracy,
[1331.04 --> 1332.90]  or how does the output compare?
[1333.02 --> 1336.06]  How would I rate these as failure or what?
[1336.14 --> 1337.88]  That's still the way to do it, right?
[1338.10 --> 1341.66]  So the last two minutes is my favorite part of this episode so far.
[1341.66 --> 1348.30]  You just put the practical in practical AI in terms of how to go about actually doing this stuff in real life.
[1348.46 --> 1350.18]  So much appreciated on that.
[1350.42 --> 1351.08]  Yeah, of course.
[1351.26 --> 1351.40]  Yeah.
[1351.58 --> 1355.38]  Well, one of those things that was mentioned, well, two things,
[1355.78 --> 1358.94]  the licensing and the context link that we just talked about.
[1359.04 --> 1364.46]  So for those that aren't aware, most of these generative models accept a prompt
[1364.46 --> 1369.48]  that is some amount of text that is kind of auto-completed.
[1369.72 --> 1371.30]  The result is an auto-completion.
[1371.58 --> 1375.72]  Most of the large language models that we're dealing with are auto-completion models,
[1375.84 --> 1377.38]  so they predict next words.
[1377.90 --> 1379.84]  The image generation one or the video generation,
[1379.96 --> 1384.06]  when you kind of think of the image or the video as the completion of a prompt as well,
[1384.14 --> 1385.14]  because you're putting in text.
[1385.14 --> 1392.52]  But these models generally have a constraint around the amount of text that you can put in as your prompt.
[1393.18 --> 1400.14]  Many of the open models are kind of around 2,000-ish tokens of input.
[1400.64 --> 1404.90]  So for example, you couldn't put in maybe a whole chapter of a book or something.
[1405.00 --> 1406.60]  That's not what you could put in there.
[1406.60 --> 1414.26]  There are some trickeries that have been introduced that take a model that was trained on a smaller context length
[1414.26 --> 1415.90]  and kind of extend the context length.
[1416.50 --> 1422.18]  But something we've seen in the past couple weeks is some really seemingly very powerful models
[1422.18 --> 1429.26]  that are open and are available for commercial usage under their licensing
[1429.26 --> 1432.28]  that support a longer context length.
[1432.34 --> 1435.38]  One of these being the Salesforce XGen model.
[1435.38 --> 1439.48]  So if you go on Hugging Face, just search for XGen.
[1440.02 --> 1445.36]  It's a 7 billion parameter model with an 8,000 input sequence length,
[1445.60 --> 1449.64]  which is obviously quite a bit more than that 2,000.
[1450.10 --> 1453.66]  And one of the things I find interesting about this model as well,
[1453.90 --> 1456.52]  kind of fitting with similar trends that we saw in the other model,
[1456.66 --> 1460.62]  the 7 billion parameter is kind of an important piece of it
[1460.62 --> 1464.50]  because 7 billion parameter, once you kind of go beyond that,
[1464.50 --> 1471.34]  you lose some of your ability to deploy models on more commodity hardware.
[1472.00 --> 1475.44]  And so that 7 billion is a very strategic number.
[1475.64 --> 1479.88]  And that's why you see a lot of 7 billion, 6.9 billion parameter models
[1479.88 --> 1484.96]  is it allows you to kind of run these models on more reasonable hardware,
[1485.28 --> 1487.62]  single GPU cards, that sort of thing.
[1487.98 --> 1489.40]  What is the technical distinction there?
[1489.40 --> 1491.36]  When you exceed the 7 billion parameter,
[1491.76 --> 1493.48]  is this something as simple as, you know,
[1493.52 --> 1496.46]  kind of like the bus width of data bits going in?
[1496.54 --> 1496.96]  Or I mean...
[1496.96 --> 1501.26]  It's really the model on fitting into the GPU memory.
[1501.50 --> 1501.74]  Got it.
[1501.78 --> 1503.10]  And not exceeding it.
[1503.20 --> 1506.12]  So unless you want to quantize your model,
[1506.24 --> 1508.56]  which we had a whole episode with Neural Magic.
[1508.96 --> 1510.46]  So I'd recommend people listen to that.
[1510.50 --> 1511.38]  That was really cool.
[1511.38 --> 1514.16]  But unless you're very careful...
[1514.16 --> 1518.42]  So quantization means like each of these 7 billion parameters of this model
[1518.42 --> 1521.80]  are some sort of floating point numbers, right?
[1522.54 --> 1526.28]  And most of them, so if you load them in,
[1526.42 --> 1528.00]  are not used that much,
[1528.00 --> 1532.60]  or you don't need sort of full float 32 precision to get good output.
[1532.60 --> 1540.88]  So one thing people do is they quantize those down to float 16 or even an 8 or 4-bit or whatever.
[1541.26 --> 1543.88]  If you're not really careful about how you do that,
[1543.88 --> 1546.46]  or if you don't kind of retrain with that precision,
[1546.68 --> 1548.68]  oftentimes you lose a lot of performance.
[1548.96 --> 1555.58]  So the thing here is like the 7 billion parameter model with these larger cards now that you can get
[1555.58 --> 1558.86]  single cards, even if it's an A100 or something like that,
[1558.86 --> 1564.34]  that's fairly expensive, but it's a single card and it will fit and run one of these models fine.
[1564.90 --> 1571.36]  But if you go to like 40 billion parameters, 60 billion parameters, these larger models,
[1571.36 --> 1577.24]  now you're kind of getting into multi-GPU zone, which makes things much more difficult.
[1577.96 --> 1582.94]  So there is a balance here, like you can quantize or optimize the larger models
[1582.94 --> 1587.60]  and run them on commodity hardware, but it's not always straightforward how to do that.
[1588.10 --> 1588.20]  Gotcha.
[1588.20 --> 1592.98]  So in general, you want to get, if you're just a practitioner out there and you're in a small
[1592.98 --> 1597.20]  or medium-sized business, you're kind of doing it on your own or with your company's stuff,
[1597.34 --> 1603.72]  kind of focusing in that 5, 6, 7 billion parameter so that you can be productive as opposed to it
[1603.72 --> 1605.76]  and not escalate costs out of your control.
[1605.84 --> 1607.12]  Is that a fair way of looking at it?
[1607.24 --> 1607.68]  Yeah, yeah.
[1607.72 --> 1613.12]  I would say basically if you try to work in that 7 billion or fewer zone,
[1613.12 --> 1617.48]  your life is much easier infrastructure-wise, I would say.
[1618.16 --> 1622.12]  And that's probably will also change over time, but I think it's the reality now.
[1622.90 --> 1626.54]  And one intro of the Salesforce thing, I love it when people post this,
[1626.90 --> 1635.12]  they posted that the training cost was around $150,000 USD on Google Cloud using TPUs.
[1635.12 --> 1639.78]  And this model is released under Apache too, which is cool for me.
[1639.90 --> 1646.06]  The other one that I mentioned that was the 8K context length was the MPT 30 billion model,
[1646.20 --> 1647.70]  which was released recently.
[1647.96 --> 1651.50]  But also note there the difference in parameter size, right?
[1651.58 --> 1656.08]  The XGen model from Salesforce supports that context length, that 7 billion parameters.
[1656.08 --> 1659.54]  And for MPT, you kind of have to go up to that 30 billion,
[1659.78 --> 1661.58]  which the MPT models are really great.
[1661.66 --> 1662.06]  I love them.
[1662.12 --> 1662.94]  I've been using them.
[1663.18 --> 1664.48]  But that's just the differentiation.
[1664.88 --> 1672.30]  You can see why maybe Salesforce XGen is trending because of their focus on this sort of thing.
[1672.58 --> 1673.28]  It's more accessible.
[1673.28 --> 1673.86]  Yeah.
[1686.08 --> 1699.16]  Well, Chris, I think that some of what we've talked about here with the open models is quite interesting
[1699.16 --> 1704.30]  because, as we already mentioned, we were talking about this a couple months ago and thinking,
[1704.30 --> 1709.90]  oh, at some point, these open models are going to proliferate and kind of take market share,
[1710.08 --> 1715.44]  whatever you want to say, from the closed proprietary models.
[1715.44 --> 1717.86]  And I think we are seeing this trend.
[1718.04 --> 1723.94]  One of the evidences that I saw in the news this, yeah, I forget if it was this week as
[1723.94 --> 1727.26]  we're recording this, but was the acquisition of Mosaic ML.
[1727.54 --> 1733.20]  So Mosaic is the one that created the MPT family of models, which, again, I've already said are
[1733.20 --> 1739.20]  really great choices if you're looking for some LLMs to play with.
[1739.30 --> 1744.82]  But Mosaic was acquired by Databricks or, quote, agreed to join, which,
[1744.82 --> 1745.82]  I don't know.
[1746.00 --> 1749.82]  The prices on these things are just astronomical, you know, in terms of...
[1749.82 --> 1750.38]  It's crazy.
[1750.58 --> 1750.74]  Yeah.
[1750.84 --> 1752.52]  So, I mean, it's public information.
[1752.66 --> 1754.50]  At least this one is public information.
[1754.50 --> 1762.04]  So a total of $1.3 billion for Mosaic ML, which has 62 employees.
[1762.90 --> 1766.24]  So that's $21 million per employee.
[1766.64 --> 1768.54]  That's a valuable employee right there.
[1768.54 --> 1775.30]  And I was talking to someone about this, and I wasn't in the strategy meetings with Databricks
[1775.30 --> 1778.12]  when they're talking about, like, why are we doing this?
[1778.12 --> 1779.70]  And how does this position us?
[1779.78 --> 1786.28]  But, I mean, think about, I remember Databricks and Spark and Hadoop back in the sort of big
[1786.28 --> 1792.50]  data days leading into data science days and really focusing on this Spark sort of thing.
[1792.50 --> 1797.60]  And think about that use case I gave earlier of the data extraction, right?
[1797.88 --> 1803.80]  How are people going to do large-scale data processing in the future or large-scale analytics
[1803.80 --> 1804.56]  in the future?
[1805.12 --> 1811.58]  Well, there will likely always be data warehouses and SQL queries and analytic systems.
[1811.58 --> 1818.08]  But there's going to be a large portion of what people are doing analytics-wise or kind of big
[1818.08 --> 1824.40]  data analysis, quote-unquote, wise by extracting information or doing reasoning with LLMs.
[1824.58 --> 1832.22]  The problem with that is for an enterprise, you can't do that with a proprietary closed API
[1832.22 --> 1836.04]  because you can't leak your private data to that API.
[1836.52 --> 1840.54]  And it's not cost-effective to do it anyway because those charge per token.
[1840.54 --> 1842.60]  So how are you going to do that?
[1842.66 --> 1848.44]  You're going to proliferate open models that are trained on your own private data and make
[1848.44 --> 1849.60]  that easier and easier.
[1849.72 --> 1851.80]  And that's what Mosaic's doing, right?
[1851.90 --> 1858.16]  So I think once you kind of think about that positioning, I'm not one to comment on business
[1858.16 --> 1859.22]  strategy necessarily.
[1859.42 --> 1864.96]  But that's how I've kind of thought about this is, yeah, like that's the valuable trajectory
[1864.96 --> 1866.30]  of where we're headed.
[1866.30 --> 1871.84]  I think it's inevitable because, you know, you run in, I know in business, I have seen
[1871.84 --> 1877.34]  many, many cases where these closed models and the licenses surrounding them and the concern
[1877.34 --> 1878.52]  about proprietary data.
[1878.68 --> 1883.92]  It's a big challenge for people that are trying to get into them as quickly as possible to
[1883.92 --> 1884.78]  navigate that through.
[1884.84 --> 1887.50]  It throws a whole bunch of legal concern around it.
[1887.50 --> 1889.60]  And then you need guardrails, which slows it down.
[1889.60 --> 1895.60]  So it makes perfect sense to go and consume and participate in the open community.
[1895.94 --> 1898.48]  And I think just like software, it's inevitable.
[1898.66 --> 1900.56]  Business will force us into that direction.
[1900.56 --> 1903.74]  So it's not people doing it out of the goodness of their hearts.
[1903.76 --> 1908.36]  It's people doing it for the betterment of their businesses because it's the only sustainable,
[1908.60 --> 1909.98]  viable option they have right now.
[1910.42 --> 1912.50]  The rug can't get yanked out from under you very quickly.
[1912.50 --> 1912.86]  Yeah.
[1913.00 --> 1918.24]  So yeah, I think we had no idea a couple of months ago that we were going to have this
[1918.24 --> 1919.54]  conversation now, though.
[1920.04 --> 1924.16]  I think you and I probably expect things to happen faster than most people out there because
[1924.16 --> 1926.00]  we're neck deep in this stuff all the time.
[1926.12 --> 1929.26]  But I don't even think we realize just how fast that would happen.
[1929.40 --> 1933.84]  I think it's going to, I'm trying to adjust my own brain for the fact that that will keep
[1933.84 --> 1936.24]  happening and will probably accelerate.
[1936.54 --> 1939.16]  So we're going to have a lot to talk about in the days ahead.
[1939.16 --> 1943.74]  Yeah, the trend that we're seeing is happening very quick that I thought would take much
[1943.74 --> 1945.40]  longer with these open models.
[1946.12 --> 1952.88]  So if you look back at these decisions that have been made around funding new GPU clusters
[1952.88 --> 1956.94]  for different startups trying to produce new foundation models.
[1957.24 --> 1963.42]  So think about, like we saw, funding $1.3 billion for inflection.
[1964.02 --> 1969.14]  And the latent space guys in their posts on AI engineers have highlighted some of these
[1969.14 --> 1974.74]  for Mistral and other ones that there's this sort of hoarding of GPUs, which is taking
[1974.74 --> 1975.26]  place.
[1976.06 --> 1981.38]  But those strategy decisions were made, you know, how long ago?
[1981.60 --> 1982.70]  Like two months.
[1982.98 --> 1989.94]  And now is having that sort of compute infrastructure, is that the differentiator that is going to make
[1989.94 --> 1991.78]  the difference in the business world?
[1991.86 --> 1996.96]  I think, you know, I'm not saying it's not going to be good for those businesses.
[1996.96 --> 2000.44]  I think probably they'll do great things and be wonderful.
[2000.66 --> 2008.68]  But you don't have to now have this sort of large GPU cluster with thousands of GPUs to
[2008.68 --> 2013.18]  be a player and create value in the marketplace.
[2013.18 --> 2019.80]  So, yeah, it's interesting to also see how the dynamics of funding and business strategy
[2019.80 --> 2024.96]  are kind of getting intermixed with this rapid proliferation and kind of individual developers,
[2024.96 --> 2029.50]  small groups of developers creating these models like OpenChat and other ones.
[2029.80 --> 2033.46]  We're also seeing, you know, going back to our conversation just a moment ago about, you
[2033.46 --> 2037.92]  know, 7 billion parameters being kind of an over-under decision point because it changes
[2037.92 --> 2039.44]  how you're going to go implement.
[2039.66 --> 2045.46]  With that under 7 billion, you're going to have whole industries focusing on things like
[2045.46 --> 2047.62]  that because they may be working out on the edge.
[2047.70 --> 2052.12]  And now they're looking at in the not so distant future, you know, whereas we might have said
[2052.12 --> 2053.70]  eventually it will, blah, blah, blah.
[2053.90 --> 2057.46]  Now we're like, let's go do LLMs on the edge.
[2057.56 --> 2063.68]  Let's go, you know, I can have a GPU that's a single board in whatever edge device we're
[2063.68 --> 2064.36]  talking about.
[2064.36 --> 2069.06]  And you're going to see whole industries pop up around the ability to do that because
[2069.06 --> 2072.88]  you're within that, as you pointed out, the RAM available on the GPU.
[2073.20 --> 2075.78]  So that's going to create a whole bunch of new business cases.
[2075.78 --> 2082.02]  I think one of the things in my mind right now is it's such an explosive kind of Wild
[2082.02 --> 2083.40]  West moment for us here.
[2083.52 --> 2085.02]  This is always the case.
[2085.14 --> 2091.78]  All of the concerns that touch on to these issues, such as cybersecurity, such as how it
[2091.78 --> 2095.24]  affects your workforce, your productivity, how do you integrate the tooling in?
[2095.66 --> 2098.64]  What does it mean for changing business strategy and opportunities?
[2099.22 --> 2102.10]  This is all trailing distantly behind.
[2102.10 --> 2107.66]  Even things like AI ethics, which we've covered quite a bit, you know, how do you, uh, legal
[2107.66 --> 2114.04]  frameworks at different countries and different municipalities and such, how do you catch up
[2114.04 --> 2120.06]  all of those things with the fact that we're having this amazing Cambrian explosion in terms
[2120.06 --> 2125.76]  of model availability, accessibility, and fragmentation into many different use cases that were not
[2125.76 --> 2127.34]  thought of two months ago?
[2127.78 --> 2127.88]  Yeah.
[2128.10 --> 2130.84]  You had highlighted the security side of this.
[2130.84 --> 2137.68]  I think it's a really good note because one thing I've seen is you go to, for example, the
[2137.68 --> 2140.62]  hugging face LLM leaderboard, right?
[2140.66 --> 2145.82]  Like, let's say I'm a person, I want to use the greatest open LLM that I can find.
[2146.12 --> 2151.90]  Let's say that for one, maybe a lot of the licensing causes problems for me, but let's say all the
[2151.90 --> 2153.38]  licensing problems are equal.
[2153.38 --> 2155.56]  Then I go to the leaderboard.
[2156.04 --> 2162.46]  I click on some of those that are high up on the leaderboard and the lack of information around
[2162.46 --> 2170.24]  the data processing, the training set, the fine tuning set, the testing and security vulnerabilities,
[2170.68 --> 2174.02]  potentially like prompt injection vulnerabilities.
[2174.02 --> 2179.28]  All of these things similar to like you go to GitHub, it's the same with open source code, right?
[2179.32 --> 2185.26]  You can search for some tool and it might have a little bit of information in the readme and might say,
[2185.38 --> 2189.80]  okay, great, import solves my problem and move on.
[2189.94 --> 2194.14]  But that's a recipe for introducing vulnerabilities into your code.
[2194.14 --> 2201.02]  But it's why products like Snake, which I think is a cool way that I've found for developers to deal
[2201.02 --> 2206.16]  with that sort of issue on the code side is, you know, analyzing your dependencies to look for known
[2206.16 --> 2209.46]  vulnerabilities in open source projects.
[2209.46 --> 2212.36]  But there's nothing like that for LLMs, right?
[2212.64 --> 2217.30]  Which of these LLMs has more hallucinations than another one?
[2217.40 --> 2220.82]  Which of them has more toxicity than other ones?
[2220.82 --> 2225.74]  Which of them are more prone to prompt injection type of things than other ones?
[2226.22 --> 2228.66]  All of that's not on the leaderboard, right?
[2229.06 --> 2235.42]  And one of the things to also note here is we're kind of addressing all of the kind of the technical,
[2235.80 --> 2240.72]  and I don't necessarily mean like code technical, but, you know, things like the legalities and
[2240.72 --> 2246.40]  documentation and how do you put in compliance around it, all these things.
[2246.40 --> 2251.54]  But I've also noticed, and I'm just kind of mentioning a passing right now because we can't
[2251.54 --> 2252.12]  delve into it.
[2252.38 --> 2255.62]  There's a huge cultural thing that we're also trying to digest right now.
[2255.98 --> 2260.84]  You know, we've talked this year about how this, you know, 2023 is really the year that
[2260.84 --> 2263.00]  it's been huge in the public's consciousness.
[2263.18 --> 2267.78]  People are using the stuff and they're aware they're using it in many parts of their lives.
[2267.94 --> 2272.26]  Things like the ChatGPT app, you know, everyone's using it on their phones and such these days.
[2272.26 --> 2277.70]  I think I've had more conversations in the last three months around people trying to figure
[2277.70 --> 2284.68]  out not just like the business aspect of how do I adopt, but also a lot of fear and a lot
[2284.68 --> 2285.94]  of concern about that.
[2286.12 --> 2290.72]  And so I think that is becoming part of what we need to be able to think about from a business
[2290.72 --> 2296.08]  strategy standpoint isn't just the cybersecurity and the compliance and all these issues, but
[2296.08 --> 2301.16]  also how do you bring the humans along for the ride and get them integrated in as we're
[2301.16 --> 2302.96]  making these massive leaps forward.
[2303.58 --> 2310.26]  So don't forget your humans in the equation as you try to take advantage of all this amazing
[2310.26 --> 2311.18]  LLM goodness.
[2311.68 --> 2312.30]  Really good point.
[2312.60 --> 2317.38]  And I think some of the writing that I wanted to share as our learning resources at the end
[2317.38 --> 2322.60]  of this highlights some aspects of those points that you just mentioned, which is, and I've
[2322.60 --> 2327.74]  been trying to tell people this recently, that the LLM or the generative model, the image
[2327.74 --> 2332.94]  generation model, in some ways people are thinking about those things like applications,
[2332.94 --> 2336.34]  but really they're tools that are embedded in applications.
[2336.34 --> 2344.42]  So you're building an application for real people users that might make use of a tool like
[2344.42 --> 2351.18]  an LLM or an image generation model, but application development is still part of it and coding and
[2351.18 --> 2357.98]  engineering is part of it and security is part of it and your UI UX around how you interact
[2357.98 --> 2360.36]  with your customers is part of it.
[2360.98 --> 2366.54]  So that sort of thinking about these things as embedded tools within an application, I
[2366.54 --> 2367.22]  think is important.
[2367.30 --> 2372.36]  It's one thing that Jay Alomar, who was a previous guest on our show, he has a really
[2372.36 --> 2375.08]  great article, which I would recommend as a learning resource.
[2375.08 --> 2380.34]  If you're thinking about this sort of how to create competitive advantage or moats with
[2380.34 --> 2384.52]  your AI applications, he has an article called AI is eating the world.
[2384.72 --> 2389.88]  And he gives some really good analysis of thinking about, okay, where are there competitive advantages
[2389.88 --> 2390.90]  and where aren't there?
[2391.56 --> 2396.12]  And he has this really nice diagram of like models are down here.
[2396.36 --> 2397.88]  Your application is here.
[2398.00 --> 2399.18]  That's where you live, right?
[2399.26 --> 2404.10]  The application level above that, maybe in the custom model, like fine tuning level.
[2404.10 --> 2408.82]  And then above that, there's all of these things that are unrelated to the model or not
[2408.82 --> 2412.32]  unrelated, but are more so like business concerns, right?
[2412.36 --> 2413.42]  How is it distributed?
[2414.06 --> 2417.70]  You know, what sort of proprietary or sensitive data are you dealing with?
[2417.80 --> 2422.82]  What sort of domain expertise do you have that can be infused in your application, et cetera,
[2422.88 --> 2423.26]  et cetera.
[2423.40 --> 2427.08]  Those are the sorts of things that can differentiate you.
[2427.20 --> 2431.56]  And I found his writing on this very helpful in framing my mind.
[2431.62 --> 2433.06]  So I would recommend people look at that.
[2433.06 --> 2437.74]  I like it in addition because it reminds us to stay grounded and be practical.
[2437.98 --> 2444.52]  And while the world is changing out from under us in so many ways, kind of the workflow of how you think
[2444.52 --> 2449.94]  about applications and getting productivity out to people is still largely the same.
[2450.36 --> 2454.00]  New tools and stuff like that, but the same concerns exist.
[2454.16 --> 2458.56]  And so sometimes maybe you take a deep breath and you go, I know how to do this.
[2458.64 --> 2460.30]  We've been doing this even before this moment.
[2460.30 --> 2460.90]  Good point.
[2460.98 --> 2463.16]  I think that's a good statement to end with.
[2463.86 --> 2469.68]  So thanks for journeying through the Cambrian explosion or proliferation with me, Chris.
[2469.72 --> 2470.46]  This has been fun.
[2470.70 --> 2471.16]  That's right.
[2471.24 --> 2474.06]  It's a space warp here of models flying by us.
[2474.26 --> 2475.20]  Good times, Daniel.
[2475.62 --> 2476.34]  Thanks a lot.
[2476.48 --> 2476.74]  All right.
[2476.80 --> 2477.32]  Talk to you soon.
[2477.32 --> 2488.02]  Thank you for listening to Practical AI.
[2488.50 --> 2492.36]  Your next step is to subscribe now if you haven't already.
[2492.78 --> 2498.82]  And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2498.82 --> 2504.20]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2504.78 --> 2508.56]  Check out what they're up to at Fastly.com and Fly.io.
[2508.98 --> 2514.28]  And to our Beat Freakin' Residence, Breakmaster Cylinder, for continuously cranking out the best beats in the biz.
[2514.58 --> 2515.48]  That's all for now.
[2515.78 --> 2516.88]  We'll talk to you again next time.
[2516.88 --> 2517.88]  Bye.
[2517.88 --> 2518.88]  Bye.
[2518.88 --> 2519.88]  Bye.
[2519.88 --> 2520.88]  Bye.
[2520.88 --> 2521.88]  Bye.
[2521.88 --> 2522.88]  Bye.
[2522.88 --> 2523.88]  Bye.
[2523.88 --> 2524.88]  Bye.
[2524.88 --> 2525.88]  Bye.
[2525.88 --> 2526.88]  Bye.
[2526.88 --> 2526.94]  Bye.
[2526.94 --> 2526.96]  Bye.
[2528.82 --> 2529.88]  Bye.
