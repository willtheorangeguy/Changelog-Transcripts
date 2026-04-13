[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.02 --> 36.08]  Learn more at fly.io.
[42.48 --> 47.02]  Well, welcome to another fully connected episode of Practical AI.
[47.38 --> 52.50]  This is where Chris and I keep you fully connected with everything that's happening in the AI
[52.50 --> 53.00]  community.
[53.00 --> 58.24]  We'll take some time to discuss the latest AI news and dig into some learning resources
[58.24 --> 60.98]  to help you level up your machine learning game.
[61.26 --> 62.32]  I'm Daniel Whitenack.
[62.44 --> 65.38]  I'm a data scientist and founder at Prediction Guard.
[65.96 --> 69.36]  And I'm joined by Chris Benson, an AI strategist.
[69.50 --> 70.34]  How you doing, Chris?
[70.82 --> 71.50]  Doing very well.
[71.56 --> 72.40]  How's it going today, Daniel?
[72.54 --> 73.30]  Oh, it's going great.
[73.30 --> 80.00]  I got back late during the night a couple of days ago from my time in San Francisco where
[80.00 --> 86.54]  we had a in-person podcast meetup, kind of a collab with the Latent Space podcast, which
[86.54 --> 89.78]  is an awesome AI podcast if you haven't heard of it.
[90.20 --> 92.26]  But yeah, it was it was a really great time.
[92.38 --> 97.56]  I was a little bit tired yesterday, but I feel recovered today, which is good because today
[97.56 --> 102.42]  is also one of our favorite other podcasts, the MLOps community.
[103.16 --> 111.10]  They're having their LLMs in Production Part 2 conference today, and that's today and tomorrow.
[111.60 --> 114.36]  So by the time this podcast goes out, it will have passed.
[114.44 --> 117.76]  But I think they'll post the talks on YouTube and all of that.
[117.86 --> 119.48]  So make sure and check out those talks.
[119.54 --> 121.26]  There's a lot of really good ones there.
[121.68 --> 122.78]  Yeah, I'm sure there are.
[123.54 --> 124.94]  I've been learning a lot from them.
[125.06 --> 125.58]  Yeah, yeah.
[125.58 --> 126.86]  What a what a great community.
[127.04 --> 130.98]  I've joined their Slack and I'm chatting with people about how they're deploying models and
[130.98 --> 132.88]  all that stuff, which is which is fun.
[133.30 --> 138.24]  Another thing happened today, Chris, I was at a co-working space here and in town.
[138.66 --> 140.50]  Shout out to Matchbox co-working.
[140.86 --> 146.74]  I know a few people there listen to the show, but I ran into a friend, Tanya, and she's been
[146.74 --> 151.52]  listening to recent episodes of the show and she made a really good point.
[151.52 --> 158.72]  And that's that we haven't taken time for a while anyway to stop and say, in this moment
[158.72 --> 162.96]  that we're in now, when we say AI, what do we mean?
[163.02 --> 164.94]  Like, what is AI now today?
[165.22 --> 166.88]  That's a really good point.
[167.06 --> 167.92]  Thank you, Tanya.
[168.04 --> 169.68]  If I got if I got the name right.
[169.80 --> 176.30]  The the last time that we kind of talked about what it means, there was no such thing as generative
[176.30 --> 177.58]  AI, for instance.
[177.58 --> 182.70]  Yeah, yeah, definitely not in the way that or at least in the term, the way we're using
[182.70 --> 185.02]  it now, the way the term is used now.
[185.16 --> 185.34]  Yeah.
[185.48 --> 187.28]  So I think that brings up a good point.
[187.34 --> 190.22]  Chris is like, what is generative AI?
[190.48 --> 191.78]  We can maybe talk about that.
[192.18 --> 198.48]  But maybe first we should talk about what was AI or machine learning prior to generative
[198.48 --> 204.36]  AI, which that sort of machine learning and AI is still in existence, of course, and being
[204.36 --> 205.86]  used all throughout industry.
[205.86 --> 209.70]  But there's a difference between that and generative AI.
[210.08 --> 216.38]  In my mind, if you want to think about actually, this would be true of both kinds of AI.
[216.70 --> 221.66]  So if you think about AI in general or machine learning in general, the way I think about
[221.66 --> 225.62]  it at its most simple form is a data transformation.
[225.62 --> 233.82]  And you put some type of data into one of these, quote, models, and you get some other data out.
[233.96 --> 236.06]  It's like a software function, essentially.
[236.24 --> 239.12]  Now, of course, there's a lot going on within that function.
[239.12 --> 245.62]  But at its basic core, an AI model or machine learning model is something that takes in one
[245.62 --> 253.50]  form of data and outputs other data like speech in and text out or language in one language
[253.50 --> 255.90]  in and language in another language out.
[255.90 --> 260.88]  There is a really old fashioned term that would be applied is it's a filter.
[261.08 --> 264.58]  Software developers who have been around for a while might know about creating filters.
[264.58 --> 269.56]  And it's just an incredibly sophisticated filter in that, you know, you get the one thing in,
[269.68 --> 271.22]  you get a different thing out.
[271.34 --> 273.82]  And it's all about the relationship between the two.
[273.82 --> 274.22]  Yeah.
[274.36 --> 280.48]  And that kind of brings in one level of a mental model into how we think about these
[280.48 --> 280.78]  things.
[280.78 --> 281.98]  We're going to put something into them.
[282.02 --> 283.18]  We're going to get something out.
[283.38 --> 290.76]  Now, obviously, these models are different than other software functions that are filters
[290.76 --> 293.24]  that people have written in the past.
[293.38 --> 293.56]  Right.
[294.12 --> 299.58]  And the key difference, I think, that I share with people, at least when they're forming
[299.58 --> 305.86]  their own mental model around these things is that in kind of normal, quote unquote, I
[305.86 --> 310.44]  don't know if we have normal software engineering anymore, but normal software engineering, you
[310.44 --> 316.94]  have a function and the engineer or the programmer writes all of the logic of that function and
[316.94 --> 319.72]  determines what parameters should be used where.
[319.92 --> 324.38]  Like I'm going to accept two numbers and then I'm going to add those things together and output
[324.38 --> 325.00]  the output.
[325.14 --> 326.84]  And that is a data transformation.
[327.40 --> 327.86]  Right.
[327.86 --> 331.64]  But the logic is completely programmed by the programmer.
[332.24 --> 335.62]  It has to all come as an original thought out of a programmer's head.
[335.80 --> 336.12]  Correct.
[336.30 --> 341.16]  And there could be some flexibility, I guess, would be the right way to put it.
[341.22 --> 342.92]  I mean, software is flexible in general.
[343.10 --> 348.12]  I could have a function that adds two numbers together and I could add any two numbers together.
[348.22 --> 350.26]  It doesn't have to be one and two.
[350.36 --> 353.64]  It could be 42 and 17 or something like that.
[353.64 --> 363.00]  However, in a machine learning or AI model, which does one of these transformations, there's still an element.
[363.24 --> 365.30]  This is maybe a misconception that people have.
[365.48 --> 368.50]  There's still an element of that software function.
[368.86 --> 369.30]  Absolutely.
[369.50 --> 370.88]  That is written by humans.
[370.88 --> 371.18]  Right.
[371.18 --> 373.94]  It is structured by humans.
[374.06 --> 375.58]  Have you found that to be a misconception?
[375.58 --> 376.54]  I do.
[376.54 --> 387.10]  I think people think people who are not in the space intimately as we in this audience would be tend to think of it as, I mean, they won't admit to it, but they think of it as magic a little bit.
[387.10 --> 394.10]  I get into a lot of business conversations and I could take out the business words and put in the word magic and it would still work, the conversation.
[394.40 --> 397.98]  So it's a little bit instructive in terms of how people are perceiving it.
[398.30 --> 398.48]  Yeah.
[398.68 --> 398.84]  Yeah.
[399.08 --> 407.52]  It's almost like there is software, but the bit that's the model is just totally, it manifests itself out of the computer.
[407.70 --> 407.86]  Right.
[407.98 --> 408.24]  Yes.
[408.24 --> 432.44]  In reality, what happens is there's a thing called an architecture and all that means is that you just have code that's written that does certain things within your function or within your data transformation that might be adding numbers together or averaging things or multiplying different numbers in various ways.
[432.44 --> 446.44]  And so all of those things are combined or structured actually by a human programmer, often researchers, I guess, in this case would come up with a model architecture like some people might have heard of or BERT or GPT.
[447.04 --> 447.14]  Right.
[447.26 --> 458.26]  These architectures that are a form of a software function, but they have missing pieces in them and what those missing pieces are called parameters.
[458.26 --> 471.88]  So one example I kind of give sometimes is let's say that we wanted to write one of these machine learning functions to classify cats or dogs, pictures of cats or dogs.
[472.06 --> 484.84]  I could have a very simple model architecture, which says if percentage of red in image is greater than X, classify it as a cat.
[484.96 --> 487.08]  If not, classify it as a dog.
[487.08 --> 489.20]  Now, I haven't said what X is.
[489.84 --> 497.92]  So how do I set this parameter that's a gap in my machine learning model, the most simple of machine learning models?
[498.36 --> 508.70]  Well, what I can do is I just take a bunch of examples of cats and dogs and I try a whole bunch of different Xs and whichever one gives me the best result.
[508.86 --> 514.28]  In other words, whichever one classifies those the best, I choose that as my parameter.
[514.28 --> 518.62]  And this is what at a much larger scale we call training.
[518.88 --> 520.32]  People might have heard of that.
[520.32 --> 527.16]  Now, the models that are used these days don't have one parameter like my simple cat dog model.
[527.76 --> 531.38]  They have billions of parameters that are set.
[531.38 --> 548.68]  And just to add in one little thing, that training process is based on an algorithm, which is just a fairly simple math problem that you iterate through over and over and over again, comparing your results to what you're targeting, what you're trying to get to.
[548.68 --> 550.36]  And there's an error there.
[550.36 --> 553.10]  And you're trying to reduce that error down to do that.
[553.16 --> 560.38]  And so when people talk about training AI and there's this kind of mystique associated with it, there's no mystique really there.
[560.48 --> 567.74]  It's just running an algorithm over and over and over again until you get a more accurate, less error prone answer.
[567.92 --> 569.00]  It's as simple as that.
[569.00 --> 573.46]  Yeah, in that sense, it's kind of a brute force implementation of trial and error.
[573.46 --> 587.46]  Now, not totally brute force because trial and error would require you to try every option or every combination, which for a six billion parameter model would take the life of the universe or something to explore.
[587.46 --> 594.78]  But of course, there's people have put in long devoted much of their life to optimizing these types of problems.
[594.92 --> 596.02]  And so it is highly optimized.
[596.02 --> 606.28]  But at its core, like you're talking about, you're trying to reduce an error or what's called a loss and find those optimized parameters to perform a task.
[606.28 --> 613.98]  So in the case of dog and cat classification, you have a bunch of images which are labeled as dog or cat.
[613.98 --> 620.56]  You would feed those into the model with a bunch of different combinations of these parameters.
[621.08 --> 633.02]  And then the winning one that reduces the error or the loss would be your set of ideal parameters, which then you can use to classify new images which don't have a label yet.
[633.12 --> 635.22]  So I don't know if this image is a dog or a cat.
[635.64 --> 638.40]  I'm going to put that in and then I can classify that.
[638.50 --> 640.64]  And that's what's called the inference process.
[640.84 --> 641.62]  So there's a training.
[641.88 --> 642.98]  It's two steps.
[642.98 --> 646.08]  There's a training process and an inference process.
[646.08 --> 658.08]  And this is generally what's called supervised learning, which means that you just have labeled gold standard labeled examples.
[658.98 --> 667.58]  And this, I would say, dominated the AI scene and still dominates much of what's done in industry.
[667.58 --> 674.22]  I think people also have the misconception that, oh, supervised learning is so 2016.
[674.86 --> 678.20]  No, it's still the vast majority of what's deployed out there.
[678.46 --> 680.66]  You know, what people are actually using in real life.
[680.78 --> 683.02]  Yeah, I probably, I mean, I'm totally guessing.
[683.46 --> 688.10]  But I would say at least 95% of what is out there in industry is that.
[688.34 --> 690.70]  And that might be a conservative guess.
[690.86 --> 691.46]  Yeah, yeah.
[691.46 --> 697.82]  So this is still the dominant frame of thinking about machine learning and AI, at least across industry.
[698.28 --> 701.56]  That has shifted a bit, though.
[701.56 --> 710.74]  So maybe around like 20, I mean, at least when it started shifting, my mindset was probably around 2019, 2020.
[710.74 --> 716.16]  Some of these what's called self-supervised models started coming out.
[716.68 --> 723.84]  The idea being that there was kind of maybe a first shift and then a second shift that I've seen.
[723.98 --> 734.70]  So there was an era of data science where supervised learning, gather your data set, train your model with those examples, and you have your supervised machine learning model.
[734.70 --> 748.30]  Well, people gradually learned that if we make our models bigger and we expose them to enough data for a particular mode, let's say text, right, or images.
[748.56 --> 763.08]  Well, if I have a large model that's been trained to recognize 17 different things and images, I might have a use case where I want to recognize an 18th thing, right, or maybe three different things.
[763.08 --> 775.12]  Well, that model has embedded in it the capability to find really good features of images and do image classification based on those features.
[775.34 --> 779.68]  And so I don't have to retrain a whole model from scratch.
[779.68 --> 790.50]  What I take is that large model that's been trained on a lot of images, and I do a process called fine tuning or transfer learning to then do this new task.
[790.50 --> 793.06]  So I saw this first shift.
[793.22 --> 794.92]  I'm going to call it a first shift maybe.
[795.26 --> 796.90]  I mean, this is something people have talked about.
[797.02 --> 797.96]  You've just coined a phrase.
[798.08 --> 798.74]  You know that, don't you?
[799.68 --> 800.12]  Yeah.
[800.24 --> 811.08]  So this would be a shift from thinking purely about supervised learning, training from scratch with your own data into this realm of Google trains a big model for image detection.
[811.32 --> 816.84]  And I take that and I fine tune it for my own purposes.
[816.84 --> 818.24]  I'm not starting from scratch.
[818.24 --> 819.66]  I don't need as much data.
[819.66 --> 826.60]  And I would say also this framework dominates a lot of what's happening in industry right now.
[826.60 --> 835.50]  So there's NLP use cases for this where maybe you have a model that's trained to translate from English to Arabic.
[835.64 --> 837.54]  NLP being natural language processing.
[837.84 --> 838.66]  Natural language processing.
[838.66 --> 842.50]  And you want to translate, though, to like an Arabic vernacular.
[843.08 --> 857.72]  You would take that parent, what's called a parent model or a base model or more recently called foundation model, and then fine tune it to this new scenario where your task is slightly different.
[857.72 --> 876.16]  Okay, Chris, that brings us to our next wave or change in the landscape of AI, which we already talked about this sort of move from purely supervised learning to fine tuning from a parent model, a large parent model.
[876.16 --> 890.82]  And now we're in this kind of wave of generative AI, which is the kind of first wave of AI that has really hit the public perception so widely.
[891.16 --> 891.42]  Yes.
[891.70 --> 893.90]  It's been the game changing thing for the public.
[894.08 --> 896.58]  They've been hearing about AI in the media.
[896.98 --> 898.44]  They've been loosely aware of it.
[898.44 --> 903.66]  But they suddenly had some tools that were powerful and placed directly into their hands.
[903.82 --> 906.48]  And that has made a huge difference.
[906.68 --> 909.78]  They came out late last year, I guess, in that sense.
[910.10 --> 917.64]  But this year is really 2023 has been the year where the public's perception of AI has substantially changed.
[917.64 --> 918.30]  Yeah.
[918.30 --> 945.26]  And these models, these large models, like those used in the GPT family of models or open access ones like Llama or Falcon that people might be seeing, or the image based ones like stable diffusion or DALI, all of these are still fitting this model of a data transformation or a filter.
[945.26 --> 949.02]  You put some type of data in, you get some type of data out.
[949.74 --> 956.54]  There are some fundamental, at least for some of these models, there's some differences in how they're trained.
[956.84 --> 959.60]  Remember that training process that we talked about.
[960.06 --> 965.14]  But then also there's quite a big difference in how they're being used.
[965.26 --> 972.58]  I think in my mind, that's almost the bigger shift in terms of how people are thinking about using these models.
[972.58 --> 981.62]  So used to when you would have one of these parent or foundation models, that parent or foundation model wasn't that useful in and of itself.
[982.08 --> 982.34]  Right.
[982.38 --> 986.36]  So you have like the base BERT model or something like that.
[986.36 --> 990.30]  There are some use cases for that model specifically.
[990.54 --> 997.30]  But the real power comes that you can downstream fine tune that model with your own data for a specific task.
[997.30 --> 1008.08]  So instead of having a general model, you train a machine translation specific model or a sentiment analysis specific model on your own data.
[1008.60 --> 1014.76]  Before we move on from there, I just to address for a moment for those who are not familiar with foundation models,
[1014.76 --> 1029.06]  the value in doing what Daniel was just describing is in the fact that much of the training that occurs in a model is very resource intensive and very time consuming and is not specific to your problem.
[1029.26 --> 1037.10]  And so you can train a model to, you know, maybe 90, 95 percent of what you want, maybe even even farther.
[1037.10 --> 1039.70]  And there's a huge investment there.
[1039.96 --> 1047.14]  But from that, it's that last little bit where you have many, many, many, many use cases that you can fine tune it for.
[1047.62 --> 1054.20]  And so if you can start by having somebody else like a big cloud provider do the first giant chunk of training,
[1054.20 --> 1059.30]  then you can take that almost done model and customize it to your need,
[1059.30 --> 1063.58]  as can thousands and thousands of other people with different use cases.
[1063.58 --> 1069.48]  So you're transferring the training cost to a large organization that does that anyway.
[1069.68 --> 1070.76]  And that's the value.
[1070.84 --> 1073.36]  So you can you can buy into a large model much easier.
[1073.50 --> 1078.92]  So I just wanted to clarify that in case anyone wasn't intimately familiar with foundation models.
[1079.48 --> 1079.96]  Yeah, yeah.
[1080.04 --> 1089.06]  And that's part of the reason, yeah, why the large tech companies are the ones that have dominated the production of these models,
[1089.06 --> 1099.28]  like Google and Facebook or Meta and OpenAI, etc., have dominated that scene because they have a lot of resources available to them.
[1099.32 --> 1102.14]  Although there are some exceptions to that rule as well.
[1102.14 --> 1113.28]  If we think now towards generative AI, like I mentioned, there's still this concept of one type of data in, another type of data out.
[1113.28 --> 1117.90]  And there's still this concept of foundation or base model.
[1118.12 --> 1124.26]  I think the real shift, although there is some shift in how these large models are being trained,
[1124.38 --> 1129.36]  which is we do have an episode about reinforcement learning from human feedback.
[1129.68 --> 1137.12]  So maybe if people are interested more in the details of that sort of training process and how it's different, you can look back at that episode.
[1137.12 --> 1148.02]  But I think maybe a more significant shift in the distinction of these generative models from previous waves of models
[1148.02 --> 1159.62]  is that people now view these foundation models that are being produced these days as useful in and of themselves without any further fine tuning.
[1159.92 --> 1163.54]  Although sometimes people do use fine tuning later on.
[1163.54 --> 1177.24]  And they're generative because the way people are thinking about using these models is by putting a sequence of information in and getting a completion of that information out.
[1177.38 --> 1178.84]  That's what we mean by generative.
[1178.84 --> 1188.52]  So I have some sequence of things in and the next thing that should come out, the completion, is what is, quote, generated.
[1188.52 --> 1195.02]  So that doesn't necessarily have to be text, at least in how people think about these models.
[1195.22 --> 1206.08]  It could be, you know, you start out playing a few notes on your piano and then the model generates the next bar of music or something.
[1206.42 --> 1208.90]  Or it could be text like autocomplete.
[1209.04 --> 1214.52]  I put in text and then out comes the completion of that text.
[1214.52 --> 1223.30]  Yeah, it can really, when you think about it, it can be any kind of information sequence over time that's structured.
[1223.50 --> 1226.98]  And you can, you know, so, you know, we see this generative images.
[1227.24 --> 1228.08]  We see it in music.
[1228.30 --> 1229.54]  We're seeing text, obviously.
[1230.04 --> 1236.74]  And there may be other paradigms to come in terms of how people approach different ways of looking at information.
[1236.74 --> 1243.96]  And that's a big topic of interest right now is what are, you know, kind of turning things on the side and could you do that?
[1244.00 --> 1252.84]  And, you know, it's, I think that, that point right there about not just the baseline text and image and music and such,
[1252.84 --> 1258.82]  but what are other information streams that are possible to apply this approach to?
[1258.82 --> 1265.70]  Because it's already been game changing in terms of the productivity output from what we've just talked about.
[1266.24 --> 1270.24]  But that may just be the tip of the iceberg and what's to come.
[1270.36 --> 1272.08]  And we'll get there this week.
[1272.72 --> 1275.24]  I'll hand it back over to you before we go too far.
[1275.24 --> 1286.08]  Yeah, I think that's a really good point, Chris, because I've in recent days been telling people how I've had to rebuild my intuition a little bit as a data scientist.
[1286.64 --> 1293.22]  Because my knee-jerk reaction as a data scientist is to gather some data and train a model.
[1293.44 --> 1297.48]  Maybe a generalization, but not so far off from the truth.
[1297.48 --> 1303.84]  But now, with these models, I can solve a lot of the problems that I need to solve without doing any training at all,
[1303.94 --> 1312.54]  but doing this sort of engineering and processing around the information that goes into a generative model so it produces the right thing out.
[1313.14 --> 1319.40]  So some of this, we can give some examples maybe of generative models and how this works out in practice.
[1319.66 --> 1326.40]  So maybe I want to generate an image, a lifestyle image for a product, something like that.
[1326.40 --> 1328.04]  I could take the product description.
[1328.84 --> 1340.82]  I could take some other elements, like some instructions, and form that into what's called a prompt input to a model like stable diffusion, DALI, mid-journey, something like that.
[1340.82 --> 1353.88]  And say, generate an image for this product, and you inject the product description and make it black and white, set in New York, photorealistic, something.
[1353.88 --> 1367.24]  So you can see I'm constructing a prompt where I expect the completion of that prompt or the thing generated out of it to be that sort of image that's grounded in the product description.
[1367.24 --> 1372.90]  So that's one example where you would insert that and you would actually get an image, that image out.
[1372.96 --> 1376.36]  I've done this with my wife's products, and it works quite well.
[1376.68 --> 1378.84]  Of course, you could also do that with text, right?
[1378.84 --> 1380.54]  Let's stick with the marketing example.
[1381.06 --> 1386.92]  Maybe I want an ad now to go with my lifestyle image that I'm going to run on Facebook.
[1386.92 --> 1400.46]  And so I could use a model like one of the GPT models from OpenAI, or I could use Cohere, or I could use the Falcon model that was introduced recently, which is a large language model.
[1400.46 --> 1401.88]  This is a type of generative model.
[1401.88 --> 1408.80]  And I could put in a prompt to say, hey, here's my product description, and I want to run a sale, something like this.
[1408.94 --> 1413.80]  Generate some good, like a good Facebook post for me or a good Instagram post.
[1414.48 --> 1420.22]  And the output of that, the completion or the generation out of that is what's going to come out.
[1420.64 --> 1424.00]  And now I have an image and I have ad copy for that.
[1424.00 --> 1429.28]  But that doesn't, as we mentioned, that doesn't have to be what we limit ourselves to.
[1429.38 --> 1439.28]  There's music generation models now, and you can describe the mood that you want to put behind maybe a video corresponding to that ad and generate music out.
[1439.52 --> 1441.76]  And maybe I want to convert the image to a video.
[1442.06 --> 1446.46]  I could generate video content out of a prompt and add that in.
[1446.46 --> 1454.78]  And so you can start to see how chaining all of these things together, multiple calls to these types of models, can produce really magical output.
[1455.28 --> 1461.10]  And that, I think, is what's dominating this current wave of AI that we're in.
[1461.10 --> 1462.06]  It is.
[1462.44 --> 1468.72]  And we have barely touched on the use cases, because I think it's only limited right now by imagination.
[1469.36 --> 1474.06]  My friend Brent Siegel on the weekends likes to play with exactly exploring these ideas.
[1474.06 --> 1487.80]  And a couple of weeks ago, he was saying, hey, look, I generated a professional quality PowerPoint presentation that is indistinguishable from what a PowerPoint professional, you know, with graphics and everything was able to do.
[1487.80 --> 1493.48]  He did that entirely out of, I believe it was the GPT-4 model with ChatGPT.
[1493.94 --> 1496.52]  And he was like, yeah, I did this in a matter of minutes.
[1496.52 --> 1499.88]  I was able to generate the code, which would create the PowerPoint.
[1499.88 --> 1508.36]  And for every slide, I gave it a single topic of what I cared about, or I'd give a whole section of topic and tell it to create the slides.
[1508.68 --> 1510.18]  And it was amazing.
[1510.26 --> 1512.68]  It was better than most people could have done.
[1512.80 --> 1516.56]  So now that was his weekend project, which is great.
[1516.56 --> 1528.68]  But if you look at that, that one use case, think of the number of human hours that go into in businesses all over the world that go into generating presentations and documentation.
[1528.68 --> 1538.50]  And by the time he was done with his brief weekend project, he could do something that would have previously taken him a week, you know, of work time.
[1538.64 --> 1539.54]  And he did it.
[1539.60 --> 1541.44]  He could do it once the process was in place.
[1541.44 --> 1543.04]  He could do it in like a few minutes.
[1543.62 --> 1544.42]  And that was it.
[1544.42 --> 1554.66]  So if that became one of a million use cases that people are starting to do all over the world, that turns into real money in industry, in all industries.
[1554.90 --> 1564.08]  And so that's just one, which is, I think, representative of why the technology is so amazingly powerful.
[1564.08 --> 1579.84]  So if you multiply that times as many things as your imagination come up with, then yes, we have a technology now that we've barely tapped into and which will have an immense impact, whether you think it's positive or negative, on the world around us.
[1585.68 --> 1588.82]  I'm Jared, and this is a ChangeLog News Break.
[1588.82 --> 1594.66]  DeviceScript is Microsoft's new TypeScript programming environment for microcontrollers.
[1595.22 --> 1605.98]  It's designed for low power, low flash, low memory embedded projects, and has all of the familiar syntax and tooling of TypeScript, including the NPM ecosystem for distributing packages.
[1606.60 --> 1609.04]  This project has a lot of devs excited.
[1610.12 --> 1611.70]  Jonathan Berry says, quote,
[1612.30 --> 1614.34]  Dope. TypeScript for hardware.
[1614.34 --> 1619.62]  Always glad to see these attempts at bringing web technologies to embedded systems and see what sticks.
[1619.96 --> 1622.04]  Even when they don't, they inspire innovation.
[1623.44 --> 1625.46]  Zach Silviera says, quote,
[1625.92 --> 1628.44]  This is so much better than MicroPython.
[1629.30 --> 1632.06]  And Andrea Guiamarchi says, quote,
[1632.62 --> 1637.02]  This is the first Esperino competitor, and I think it's going to be huge.
[1637.24 --> 1642.58]  You just heard one of our five top stories from Monday's ChangeLog News.
[1642.58 --> 1655.32]  Subscribe to the podcast to get all of the week's top stories and pop your email address in at changelog.com slash news to also receive our free companion email with even more developer news worth your attention.
[1655.54 --> 1659.20]  Once again, that's changelog.com slash news.
[1659.20 --> 1671.64]  Well, Chris, I think that was at least a good foundation for foundation models.
[1672.10 --> 1678.94]  And hopefully, Tanya, if you're out there, let me know at the co-working space if that was helpful.
[1678.94 --> 1682.86]  But I think it hopefully will be helpful for more than just you.
[1682.96 --> 1690.98]  There's a lot of people wrestling with how to think about these sorts of models and think about how we should interact with them and all of those things.
[1691.06 --> 1702.86]  And that really brings us maybe to our next kind of noteworthy news trend that's happening right now, which is around these generative models can do a lot of things.
[1702.86 --> 1713.68]  And certain of those things are viewed either for real legitimate reasons or not legitimate reasons as extremely risky.
[1713.94 --> 1717.76]  And I would say there's both legitimate and non-legitimate reasons.
[1717.76 --> 1722.30]  But yeah, a lot of people view these things as risky more so.
[1722.46 --> 1730.94]  And I'm not necessarily talking about automating away jobs, which maybe is another topic that we've talked about this on the show before.
[1731.16 --> 1735.36]  But actual risk associated with running these models.
[1735.66 --> 1738.52]  Risk to humanity survival, I think, is what we're looking for.
[1738.52 --> 1738.86]  Yeah, yeah.
[1738.88 --> 1743.02]  Because that's the context that people tend to talk about it in.
[1743.02 --> 1748.80]  Yeah, what are the views or what are the things that are hitting your desk on that front, Chris?
[1749.12 --> 1757.36]  So people are debating that topic on whether these, you know, admittedly, I think everyone agrees that these are incredibly powerful capabilities.
[1757.60 --> 1765.90]  But do they constitute the ability to kind of automate an autonomous risk to us in some form?
[1766.30 --> 1770.96]  A lot of times you'll see people arguing for and against on various specific issues.
[1770.96 --> 1776.16]  But the thing that I've noticed the most is that they're not always talking about the same thing.
[1776.64 --> 1783.56]  I'll have two people arguing two sides of the point that I'm watching, but they're not really talking apples to apples on the two sides.
[1784.20 --> 1791.88]  And hearing many such arguments in the last few months, I've actually dramatically changed my own perception.
[1792.38 --> 1799.26]  And I haven't heard anyone, I'll throw it out in a minute, but I haven't heard anyone say quite the same as what I'll propose in a few moments,
[1799.26 --> 1802.86]  which has to do with that kind of miscommunication, kind of talking past each other.
[1802.86 --> 1812.26]  Yeah, I think my strategy has mostly been, although I think these are legitimate things to consider,
[1812.42 --> 1819.94]  mostly my response has been to put my head down and build things that I think are useful and practical.
[1819.94 --> 1830.28]  And I haven't necessarily given a lot more time to thinking about, you know, the end of humanity as we know it.
[1830.82 --> 1833.84]  So I've probably put more time into that part of it than you have.
[1833.92 --> 1834.54]  I think so.
[1834.54 --> 1844.84]  And so the thing that I think people focus on the wrong thing on this topic, they focus on whether the existing generative models,
[1845.02 --> 1852.82]  as we're now calling them all the time, are leading us into kind of artificial general intelligence, AGI,
[1853.12 --> 1858.28]  whether it's aware, whether it's conscious, and whether it would have an intent to attack.
[1858.38 --> 1861.32]  And I think that that completely misses the point.
[1861.32 --> 1867.48]  I think if you want to, and I'll take two seconds and argue both sides for a second.
[1867.66 --> 1873.70]  If you want to argue against current technology being a risk to humanity,
[1873.70 --> 1879.10]  then you're kind of pointing and saying, clearly these models are not conscious,
[1879.50 --> 1884.58]  and they are not intelligent in having a broader awareness of the world around,
[1885.04 --> 1887.46]  and having their own motivations and such.
[1887.46 --> 1896.12]  And so the people that are arguing that side scoff at the very nature of the fact that you could suggest that a model could threaten humanity.
[1896.36 --> 1901.52]  And within the context of that set of arguments, I think they're absolutely right.
[1901.88 --> 1910.56]  But there's also another side to it, and that is, which is actually where I am kind of migrating a little bit in my own personal thinking.
[1910.56 --> 1915.22]  And that is, what if it doesn't take AGI to be a threat to humanity?
[1915.40 --> 1920.54]  What if the threat can arise from the fact that, for one thing, we have humans in the mix.
[1920.72 --> 1926.62]  We have humans with motivations that create models and have specific things that they're trying to achieve.
[1926.62 --> 1934.40]  And so you can take the power of models and you can shape them in certain ways to address different tasks.
[1934.50 --> 1941.34]  And so it might be, possibly, that if there is a danger to humanity, which I don't know, I'm just speculating,
[1941.78 --> 1950.84]  but if there is, it's shaping a bunch of models that by themselves can do one task really well,
[1950.84 --> 1958.54]  or as the generative ones, you know, can give you sets of things, but you combine them in ways with software and with human intent to do damage.
[1958.84 --> 1964.58]  And so that's what I'm more concerned about is not that the models will awake and suddenly become conscious
[1964.58 --> 1967.78]  and decide that they don't like me very much and they want to get me.
[1968.14 --> 1973.86]  I think that I'm a lot more worried about humans orchestrating a bunch of powerful tools
[1973.86 --> 1977.92]  and maybe automating those tools in such a way that the tool keeps going.
[1978.20 --> 1979.80]  You know, it doesn't take constant intervention.
[1979.80 --> 1986.96]  And that's the type of thing that I would actually give a little bit of credence to in my own personal thinking
[1986.96 --> 1992.20]  in terms of when I say that meaning not that it's happening, but meaning that it's worthy of consideration.
[1992.44 --> 1998.76]  And when we talk about things like AI ethics and such, that's where I would focus is that there are external concerns
[1998.76 --> 2003.74]  that don't require AGI and don't require consciousness to achieve some really bad outcomes.
[2004.26 --> 2005.72]  Is that a, what do you think of that?
[2005.72 --> 2015.68]  Yeah, so I can give a concrete example that I think fits within your, it's even in your domain of expertise.
[2015.68 --> 2024.14]  But let's say that we have a large, expensive and dangerous piece of equipment like an airplane or a helicopter.
[2024.14 --> 2038.38]  And there is obviously a vast amount of manuals and documentation about the maintenance of that and the operation of it and the safety around it, etc., etc.
[2038.38 --> 2045.88]  So there could be a case, and this would not even involve like a bad actor.
[2045.88 --> 2057.06]  But let's say that we put a chat with your docs interface on top of all of these manuals and the operation information and the maintenance information and all that.
[2057.38 --> 2064.76]  You could imagine if, again, these models are essentially generating output that's probable.
[2065.22 --> 2070.28]  They don't know anything about, like you're saying, reality or intent or anything like that.
[2070.44 --> 2072.00]  There's no knowledge there.
[2072.08 --> 2073.22]  It's just completion.
[2073.22 --> 2083.24]  So they could complete someone's request saying, well, how should I fix this issue with my airplane or helicopter?
[2083.56 --> 2086.54]  And the model could say, well, just take that part off.
[2086.64 --> 2087.76]  It's a throwaway part.
[2088.30 --> 2093.60]  You know, don't, it doesn't matter based on the text that it's seeing.
[2093.60 --> 2105.02]  And, you know, if that could be a significantly life end life endangering decision if the maintenance technician or whoever it is actually trust that as fact.
[2105.02 --> 2116.58]  Now, you could also imagine bad actors getting into that scenario and, you know, modifying information such that it would generate out dangerous information or something like that.
[2116.58 --> 2127.90]  So I think that's a concrete example that would endanger lives, but does not involve AI becoming sentient or something.
[2128.34 --> 2128.54]  Yeah.
[2128.64 --> 2135.10]  I think that there are many, many, many, many, many use cases you could create along those lines.
[2135.50 --> 2139.32]  The thing that I also think people lose sight of is this is evolving so fast.
[2139.32 --> 2148.48]  So the capabilities that we're talking about today, if you look back two years, it's come a long, long, long way in two years.
[2148.76 --> 2154.60]  And two years from now, I'm expecting it to have gone at least that far, if not more.
[2154.82 --> 2164.14]  And so it's a moving target in terms of what those capabilities, which means that the risk profiles associated with what we're talking about will also change.
[2164.14 --> 2174.22]  There may be a time when some more research comes about, things are released, and there is more of a sense of understanding, which is a different thing from consciousness.
[2174.72 --> 2183.66]  And I've heard that debated recently by some fairly significant figures in the AI world about whether completion is evolving to understanding.
[2183.66 --> 2190.68]  And I don't know the answer to that, but it would not surprise me to evolve at some point to that level and beyond.
[2190.68 --> 2198.04]  So we have to be conscious of the risk profile changing as we're trying to identify where things are going.
[2198.24 --> 2209.50]  To your use case, I still feel actually, and I know that probably most of the listeners will not agree with me on this, but I feel very comfortable with modern AI models flying aircraft personally.
[2209.50 --> 2216.06]  And I think in many cases, and I say this as a pilot, that they are far better than the humans that are doing the same.
[2216.16 --> 2222.42]  Because, you know, you can train the model to essentially have a million hours equivalent, whereas, you know, a great human pilot might be 10,000.
[2222.84 --> 2225.66]  So, you know, equivalent, you know, experience level.
[2225.66 --> 2238.84]  So one of the things I think I'm going to throw out this as a point to address is I think the notion of AI ethics becomes very hard for us to not be outrun on that.
[2239.46 --> 2244.18]  So as we, AI ethics has always been chasing the development cycle.
[2244.56 --> 2249.98]  That's been one of the problems is how do you catch it up to get the decisioning in there early enough to matter.
[2249.98 --> 2253.10]  But we're also seeing the development cycle speeding up.
[2253.56 --> 2261.36]  And I've had some conversations with people lately about is it possible to do a catch up there given the evolving state over time?
[2261.36 --> 2269.12]  So there might be a whole AI ethics show we can have at some point in the future about how you address that quagmire there.
[2269.12 --> 2269.72]  Yeah.
[2269.96 --> 2279.82]  And there was actually a news article or a development this week related to exactly what we're talking about.
[2279.82 --> 2285.54]  So regulators and governments are trying to catch up with the state of generative AI.
[2286.12 --> 2289.10]  Generally not keeping up, I would say.
[2289.58 --> 2293.42]  But this week I'm just looking at this New York Times article.
[2293.92 --> 2297.52]  Europeans take a major step towards regulating AI.
[2298.40 --> 2307.18]  So, quote, the European Union took an important step on Wednesday towards passing what would be one of the first major laws to regulate artificial intelligence.
[2307.18 --> 2315.92]  A potential model for policymakers around the world as they grapple with how to put guardrails on the rapidly developing technology, end quote.
[2315.92 --> 2322.66]  So there was this regulation that is taking another step towards passing.
[2322.78 --> 2329.52]  And if you look through the article and, you know, I haven't read the full regulation, but looked at a few links.
[2329.52 --> 2335.36]  This is really focused on uses of AI that are seen as risky.
[2336.02 --> 2343.72]  And one that's cited in the article is use of AI to automate processes around utilities, right?
[2343.80 --> 2350.94]  Water and electricity and all of that, which, if it fails, has vast consequences for large populations of people.
[2350.94 --> 2354.58]  So there are these sort of risky scenarios.
[2355.26 --> 2371.08]  I think one point that you have made before, Chris, in relation to the autopilot things and other things like that, which is worth mentioning here, is also thinking about the fact that humans are fallible, right?
[2371.08 --> 2380.36]  So whether we're talking machine translation gets a bad name for producing really terrible output in certain cases, right?
[2380.74 --> 2390.36]  Well, you know, I've worked in that industry and I know it's very possible for humans to produce translations that are very, very poor as well.
[2390.36 --> 2398.48]  So a question is, you know, for the task you're considering, I think it's good to balance both.
[2398.72 --> 2408.66]  It is good to think about the risk because there is risk like in a manufacturing plant or in an aircraft or in a utility or wherever it is.
[2408.72 --> 2411.64]  There's risk associated with something going poorly.
[2411.64 --> 2419.36]  But also you have to think about, well, what is the risk and how do I test this AI or automated system?
[2419.58 --> 2422.90]  And what is the risk and how do I test these human operators?
[2423.68 --> 2431.68]  And in reality, one could be safer than the other and it might not be the one that you would expect from the start.
[2432.04 --> 2434.54]  There's an emotionalism that drives all these topics.
[2434.54 --> 2463.14]  And keeping in mind that it is evolving, it is, I will argue with anyone that there is a point in time in the future where it becomes, where the models, for instance, going back to the airplane flying, the models for those particular tasks, the AI models are so good that statistically they're making many orders of magnitudes fewer errors than very experienced human pilots.
[2463.14 --> 2464.54]  They don't get tired.
[2464.76 --> 2470.02]  They've seen weather, every weather condition in the models, they can navigate through all sorts of stuff.
[2470.46 --> 2491.26]  And if I was going to take my family on a transatlantic flight, there's a point in time where a rational person who's not driven by their fear and emotion is going to say, yes, statistically, I'm much more likely to arrive safely at my destination with my family with the AI driven airplane versus that.
[2491.26 --> 2493.84]  So we can debate when that happens.
[2493.98 --> 2497.68]  But I don't think it's terribly rational to say that's never going to happen.
[2497.78 --> 2502.00]  I'd always prefer the human because I don't think the statistics will substantiate that.
[2502.58 --> 2517.04]  Yeah, I think there's also I've heard a risk proposed maybe more so over the past months than I heard in the past, which isn't really about AI automating jobs away.
[2517.04 --> 2524.22]  But it's a risk of how this technology transforms humans and the things that they do fundamentally.
[2524.72 --> 2528.12]  So pilots, I'm sure, like to fly.
[2528.32 --> 2528.82]  Right.
[2529.00 --> 2529.48]  I love it.
[2529.64 --> 2530.34]  Yep, exactly.
[2530.34 --> 2541.28]  So if an AI is better than you and a regulator, a government regulator comes along and says, OK, well, it's no longer safe for humans to fly.
[2541.64 --> 2543.60]  Chris, no license for you.
[2543.98 --> 2545.04]  That's kind of a bummer.
[2545.28 --> 2545.60]  Right.
[2545.86 --> 2549.36]  I mean, it might be the safe option, but it is it is a bummer.
[2549.36 --> 2553.52]  And it also falls into this area of like content generation.
[2553.52 --> 2554.20]  I've heard this.
[2554.44 --> 2571.00]  I've talked to journalists and other people are like, hey, you know, like maybe an AI like I think some of those people are actually saying maybe an AI can do as good a job in certain cases or a better job than human writers in producing certain types of content.
[2571.00 --> 2579.60]  But isn't it a shame that we're going to lose our ability to like if that's no longer needed, how's that going to shape how humans write into the future?
[2579.60 --> 2582.54]  We are going to change.
[2582.70 --> 2585.46]  The nature of humanity will change with this.
[2585.56 --> 2587.34]  And it doesn't take AGI to do that.
[2587.42 --> 2588.56]  That's what I'm kind of getting at.
[2589.06 --> 2596.04]  What we do with AI versus what we don't do with AI is going to fundamentally change how we self-identify.
[2596.22 --> 2608.92]  And not only will I most certainly eventually lose my license to AI, well, that will happen at some point because putting me in a plane in the air, no matter how good I am, will become too big of an acceptable risk.
[2608.92 --> 2612.72]  But that will also happen with automobiles at some point.
[2612.88 --> 2625.12]  At some point, none of us, you will go to an amusement park to drive a car or an amusement area to fly a plane if you're going to, you know, much like we go to amusement parks now to do roller coasters.
[2625.12 --> 2637.76]  Because it will not, there's a point in the future, we can debate when it is, where the technology is so good, it will not make sense to put a human who might have a crash and kill people into the mix.
[2637.88 --> 2639.10]  That will happen someday.
[2639.10 --> 2647.28]  So we, I'll finish my comment by saying, if you're like, I'm, I have a daughter who is 11.
[2647.90 --> 2659.58]  In her lifetime, assuming she lives out her life, the nature of what it means to be human and to live with AI will dramatically change our self-identification.
[2659.90 --> 2664.14]  It's a big statement, but I feel I'm quite positive that to be the case.
[2664.14 --> 2671.80]  Yeah, and I think, you know, closing on a positive note, there's a lot of benefit that we're seeing.
[2672.60 --> 2676.36]  And we will, you know, work through some of these things.
[2676.36 --> 2684.46]  And the people that are listening to this podcast, Practical AI, you know, we've talked about the mental model of how these things operate.
[2684.60 --> 2687.56]  I'd encourage people, you know, get hands on with these models.
[2687.56 --> 2690.14]  They're not going to be malicious against you.
[2690.24 --> 2693.66]  As we've talked about, they don't have any sentience or consciousness.
[2693.66 --> 2700.82]  So, you know, get hands on with these models, develop tooling, practical tooling around these models.
[2700.82 --> 2703.04]  That's what I, what I think is needed.
[2703.16 --> 2717.10]  We, we can dive into this topic, develop practical tooling that can help us move forward and create applications that really help our customers, delight our customers, help those around the world in various ways.
[2717.10 --> 2721.72]  So, yeah, I encourage people to, to get hands on and, and get involved.
[2722.14 --> 2725.00]  And these powerful tools are part of what it means to be human now.
[2725.26 --> 2726.58]  Yeah, yeah, for sure.
[2726.96 --> 2731.18]  Well, I mean, we've all been cyborgs for some amount of time carrying around cell phones.
[2731.18 --> 2738.16]  So it shouldn't surprise people that things are advancing, but I, I don't have my vision pro yet from Apple.
[2738.38 --> 2741.38]  So we'll, we'll see how that develops, but yeah.
[2741.66 --> 2742.98]  All right, Chris, it's been fun.
[2743.28 --> 2744.26]  Good conversation, Daniel.
[2744.32 --> 2744.64]  Thanks.
[2747.10 --> 2756.24]  Thank you for listening to practical AI.
[2756.52 --> 2760.38]  Your next step is to subscribe now, if you haven't already.
[2760.72 --> 2766.86]  And if you're a longtime listener of the show, help us reach more people by sharing practical AI with your friends and colleagues.
[2767.30 --> 2772.22]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2772.22 --> 2776.60]  Check out what they're up to at Fastly.com and Fly.io.
[2777.00 --> 2782.32]  And to our Beat Freakin' Residence, Breakmaster Cylinder, for continuously cranking out the best beats in the biz.
[2782.60 --> 2783.50]  That's all for now.
[2783.76 --> 2784.92]  We'll talk to you again next time.
[2784.92 --> 2797.58]  Yeah.
[2797.58 --> 2797.94]  We'll talk to you again next time.
[2797.94 --> 2798.56]  Game on.
[2798.56 --> 2798.64]  Game on.
[2798.64 --> 2798.74]  Game on.
[2798.74 --> 2798.78]  Game on.
[2798.78 --> 2798.86]  Game on.
[2798.86 --> 2799.00]  Game on.
[2799.00 --> 2799.16]  Game on.
[2799.16 --> 2799.20]  Game on.
[2799.20 --> 2799.48]  Game on.
[2799.48 --> 2800.76]  Game on.
[2800.76 --> 2801.26]  Game on.
[2801.26 --> 2801.48]  Game on.
[2801.48 --> 2801.76]  Game on.
[2801.76 --> 2801.86]  Game on.
[2801.86 --> 2803.08]  Game on.
[2803.08 --> 2803.80]  Game on.
[2803.80 --> 2803.90]  Game on.
[2803.90 --> 2804.80]  Game on.
[2804.80 --> 2805.96]  Game on.
[2805.96 --> 2806.70]  Game on.
[2806.70 --> 2807.56]  Game on.
[2807.56 --> 2808.16]  Game on.
[2808.16 --> 2810.06]  Game on.
[2810.06 --> 2810.56]  Game on.
[2810.56 --> 2811.06]  Game on.
[2811.06 --> 2811.18]  Game on.
[2811.18 --> 2811.50]  Game on.
[2811.72 --> 2812.16]  Game on.
[2812.16 --> 2812.66]  Game on.
[2812.66 --> 2813.00]  Game on.
[2813.00 --> 2813.94]  Game on.
[2813.94 --> 2814.32]  Game on.
[2814.32 --> 2814.88]  game on.
