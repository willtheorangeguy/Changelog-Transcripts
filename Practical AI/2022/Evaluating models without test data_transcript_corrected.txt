[0.00 → 4.28] All natural data has a parallel structure, a fractal structure to it.
[4.50 → 9.16] The way neural networks learn is they learn the multifractal nature of the data.
[9.72 → 13.18] And that's why they work so well on things like text and images and why they don't work
[13.18 → 14.40] great on tabular data sets.
[14.94 → 16.94] So there are correlations in the data.
[17.02 → 17.56] Data is correlated.
[17.82 → 19.18] You're trying to learn the correlations.
[19.62 → 23.86] And frequently, you're trying to learn very subtle correlations you couldn't find in some
[23.86 → 27.84] other way, using some simple clustering algorithm or an SVM or something like that.
[27.84 → 31.50] So what we're doing is we're measuring the fractal nature of the data.
[31.60 → 37.26] And every layer of a neural network gives you some measure of the fractal properties in that
[37.26 → 38.52] level of granularity.
[38.82 → 40.86] And so alpha is like a measure of the fractal dimension.
[41.32 → 46.40] And what we know is that it measures the amount of correlation in that layer.
[46.40 → 63.12] Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive,
[63.38 → 64.44] and accessible to everyone.
[64.80 → 65.60] Subscribe now.
[65.76 → 69.58] If you haven't already, head to practicalai.fm for all the ways.
[69.96 → 74.94] Special thanks to our partners at Vastly for delivering our shows superfast to wherever
[74.94 → 77.74] you listen, check them out at Fastly.com.
[78.00 → 83.06] And to our friends at Fly.io, we deploy our app servers close to our users.
[83.28 → 84.10] And you can too.
[84.44 → 86.32] Learn more at Fly.io.
[92.66 → 95.90] Welcome to another episode of Practical AI.
[96.30 → 98.00] This is Daniel Whiten ack.
[98.08 → 101.26] I'm a data scientist with SIL International.
[101.26 → 106.94] And I'm joined as always by my co-host, Chris Benson, who is a tech strategist with Lockheed
[106.94 → 107.22] Martin.
[107.46 → 108.40] How are you doing, Chris?
[108.90 → 110.00] I'm doing very well, Daniel.
[110.08 → 110.86] How's it going today?
[111.20 → 112.16] It's going well.
[112.30 → 117.74] You know, I've been training quite a few models recently, NLP models for question answering
[117.74 → 118.52] and other things.
[118.62 → 125.38] And one thing that always comes up in that is, you know, how long do I train this thing?
[125.46 → 126.68] Am I over-training it?
[126.74 → 127.92] Am I under-training it?
[127.98 → 130.12] How do I test it appropriately?
[130.12 → 131.76] Am I testing it right?
[131.98 → 133.24] What else should I be doing?
[133.40 → 135.66] All of these thoughts are running through my mind.
[136.18 → 141.64] And I'm pretty excited because today we have joining us Charles Martin, who is an AI and
[141.64 → 144.86] data science consultant with Calculation Consulting.
[145.10 → 150.16] And this is basically one of the things that he thinks about a lot and builds tooling for.
[150.34 → 151.48] So welcome, Charles.
[151.86 → 152.20] Hey, great.
[152.28 → 153.06] Thanks for having me, guys.
[153.22 → 153.40] Yeah.
[153.40 → 160.10] Well, the main, I think the thing that I saw of your work that really interested me
[160.10 → 166.84] was this Weight Watcher tool, which is an open source diagnostic tool for analyzing neural
[166.84 → 172.94] networks without the need for access to training or even test data, which is fascinating.
[172.94 → 175.32] And I want to get into all the details about that.
[175.42 → 181.46] But maybe just describe for us kind of pre-Weight Watcher, what led up to Weight Watcher?
[181.56 → 184.84] What were the sort of motivations that were going through your mind and maybe the things
[184.84 → 189.60] that you were encountering in your own work that led you to think about this problem?
[189.60 → 190.88] Sure, sure.
[190.98 → 196.94] So I do consulting in AI and I had some clients working with me to do text generation.
[197.36 → 203.62] So this is years before GPT and all these amazing diffusion models that existed.
[203.70 → 209.32] And we were training LSTMs to generate text through things like weight loss articles and
[209.32 → 210.78] reviews on Amazon and stuff like that.
[211.22 → 215.62] And I realized that as I use these models, I can't really evaluate them.
[215.62 → 220.94] Because if you're training like a classifier, like an old SVM or XGBoost, you know, you can
[220.94 → 221.94] look at the training accuracy.
[222.40 → 226.36] But if you're trying to design a model to generate text or some other natural language
[226.36 → 231.50] processing problem, like say, designing embedding vectors for search relevance, it's really
[231.50 → 233.96] hard to evaluate whether your model is converging or not.
[234.56 → 239.56] And now I had studied statistical physics of neural networks when I was a postdoc in theoretical
[239.56 → 239.96] physics.
[240.08 → 244.82] So I knew that there are techniques from physics that make it possible to analyze the performance
[244.82 → 247.66] of these models and to estimate how well they're performing.
[247.94 → 252.24] And what I realized is that nobody in the machine learning or AI community really knows about
[252.24 → 257.38] this stuff because it's like, you know, from the early 90s, early to late 90s, where a lot
[257.38 → 258.52] of this research was done.
[259.32 → 263.10] And, you know, the people doing AI and machine learning are not theoretical physicists, you
[263.10 → 263.78] know, they're computer scientists.
[263.86 → 264.72] They don't know about the works.
[264.84 → 265.66] I said, you know, I...
[265.66 → 266.64] Except for you and Daniel there.
[267.20 → 267.98] Oh, yes.
[267.98 → 270.46] You know, it's a very broad field.
[270.68 → 275.24] And there's so many people doing AI now that it's really fun because there's so many different
[275.24 → 275.70] backgrounds.
[276.48 → 281.40] And I was at a conference maybe 10 years ago, maybe nine years ago.
[281.40 → 284.92] And I met an old friend of mine, Michael Mahoney, who's a professor at UC Berkeley.
[285.40 → 286.46] I was at Macon.
[286.52 → 288.90] It was run by the guys at that time who were doing...
[289.70 → 290.72] Oh, what was the name of the company?
[290.80 → 292.96] They had a recommender system, a recommender product.
[293.16 → 294.20] They were Turn AI.
[294.34 → 295.42] They were eventually acquired by Apple.
[295.42 → 297.10] And I was talking to Michael.
[297.18 → 302.12] I said, you know, there's a lot of theory around deep learning that is very similar
[302.12 → 303.40] to what we see in protein folding.
[303.90 → 306.40] And my advisor was actually the...
[306.40 → 308.88] Him and his student, John Jumper, developed the first version of AlphaFold.
[309.20 → 311.18] So what happened was Google acquired AlphaFold.
[311.64 → 316.72] They hired John Jumper, who was the student from Chicago, and basically souped up his thesis.
[316.84 → 321.18] And that's where AlphaFold comes from, this amazing technology from DeepMind that can predict
[321.18 → 321.76] protein folding.
[321.90 → 324.66] So there was a lot of theoretical work I had done as a postdoc.
[324.66 → 327.80] And I was talking to my advisor about some of the stuff they were doing in protein folding
[327.80 → 329.40] way back before AlphaFold was released.
[329.50 → 333.94] And I thought, you know, I think I'd like to try my shot at doing research again and see
[333.94 → 339.96] if I can develop some theory that would allow me to understand why deep learning works.
[340.62 → 345.04] And that project, you know, it's been about seven years now of research, and that's led
[345.04 → 345.92] to the Weight Watcher tool.
[345.92 → 346.26] Cool.
[346.66 → 352.10] So like, it's probably very typical for people to think about, you know, oh, I'm going to
[352.10 → 353.08] evaluate my model.
[353.28 → 354.12] I have a test set.
[354.26 → 357.90] But could you describe a little bit about two things?
[357.90 → 364.02] One is like, why from your perspective, at least in certain situations, like a test set
[364.02 → 372.20] doesn't give you the indication of behaviour or performance of a model that you're wanting,
[372.20 → 376.68] and then how that connected to these things from the physics world?
[377.34 → 377.44] Right.
[377.52 → 379.66] So let's say we're training a model to generate text.
[379.98 → 381.22] There's no test set, right?
[381.34 → 385.14] You have to read the text and ask, okay, does it look human or not?
[385.60 → 390.58] And that's sort of where the first problem came is that there are many problems in generating
[390.58 → 392.26] and when you're generating things.
[392.44 → 395.26] Another would be, let's say you're doing search relevance.
[395.26 → 398.14] I'm trying to predict what somebody wants to click on.
[398.80 → 401.72] I have clients like Walmart, for example, where we build these systems for them.
[401.72 → 403.84] It's very expensive to run an A-B test.
[404.42 → 408.28] So you can test things in the lab, and you can like to make a model, like an SVM model to
[408.28 → 409.62] predict what people will click on.
[409.96 → 412.76] But you don't really know how it's going to perform until you put in production.
[413.12 → 417.40] And there are all sorts of biases that exist in the data because there's like presentation
[417.40 → 417.90] bias.
[418.00 → 421.38] People tend to click on things that are in the first element and that screws the model
[421.38 → 421.60] up.
[422.04 → 426.32] So there are many cases and other good examples in quantitative finance when you're trying to
[426.32 → 427.16] predict the stock market.
[427.16 → 431.58] And you have models where you would like to train some neural network to learn something
[431.58 → 433.08] about how the news predicts the market.
[433.30 → 436.52] But if you train it directly on the market, you'll overfit it always.
[437.06 → 442.42] And so you have to have some way of evaluating whether your models are converging properly
[442.42 → 446.72] or not without just looking at the out of sample, you know, test sample.
[446.86 → 451.36] You don't, a lot of data is out of sample, or you don't, you can't really evaluate it without
[451.36 → 452.98] human judgments, or it's very expensive.
[452.98 → 457.84] Would you, would you kind of infer that we're, that we're probably seeing a lot of practitioners
[457.84 → 461.10] running into these kinds of issues over time?
[461.28 → 466.70] And, you know, in a lot of cases as, you know, if you look over the last few years as everyone's
[466.70 → 470.94] kind of ramped up in the space and, and been learning how to do different types of deep
[470.94 → 476.36] learning training, do you think that in terms of those accuracy issues that a lot of practitioners
[476.36 → 478.46] are kind of missing it altogether?
[478.46 → 482.32] Or do you think they know that it's there, and they just don't know how to solve it or
[482.32 → 483.78] can you lay the land with it?
[483.88 → 484.78] Well, let me give you an example.
[485.20 → 485.82] Let me give you an example.
[485.90 → 490.32] There's a recent paper that came out of Google DeepMind on the, the scaling properties of
[490.32 → 491.58] very large language models.
[492.12 → 496.62] And it showed that what we thought we knew about large language models from two years
[496.62 → 499.20] ago from OpenAI, a paper that they wrote was totally wrong.
[499.64 → 503.32] They misunderstood how the scaling properties work.
[503.32 → 507.28] And the question is things like when you have a model, and you're trying to train it,
[507.44 → 511.56] should you be trying to optimize the hyperparameters, or should you be adding more data?
[511.64 → 514.48] You can think of it like, and that's sort of very crude sense, you know, you're trying
[514.48 → 518.68] to train these models and essentially what was happening at OpenAI is you're training these
[518.68 → 522.66] large language models, and they didn't realize that they should be adapting the learning rate
[522.66 → 523.60] to the data set size.
[524.18 → 527.68] And when you change that, when you adapt the learning rate to the data set size, you get
[527.68 → 530.06] very, very different results than if you don't.
[530.06 → 534.62] And it looks like, and we know that a lot of these large language models like BERT, for
[534.62 → 536.50] example, are just not properly converged.
[537.00 → 540.76] They're many layers that are simply undertrained.
[541.20 → 544.90] And I think that basically there's the theory that people are using.
[545.00 → 548.50] There's no way to look at a model and ask how close are you to conversions?
[548.92 → 552.30] If you think about something like an SVM, let's go back, you know, I'm an old guy.
[552.36 → 553.58] Let's go back 10, 15 years ago.
[553.64 → 554.32] We run SVMs.
[554.66 → 556.20] There's something called the duality gap.
[556.20 → 560.66] You can look at the duality gap in an SVM and you can ask how close are you to the bottom
[560.66 → 563.72] of the, you know, you have, it's a convex optimization problem.
[563.78 → 569.06] And you can tell how close is your solver to actually being at the optimal solution.
[569.44 → 571.54] You can tell that that's, that's theoretically known.
[571.84 → 575.96] So it's somewhat puzzling that, you know, now you have sort of deep learning.
[576.22 → 581.36] People understand that deep learning is sort of like a convex optimization or rugged convex
[581.36 → 585.90] optimization because they know you don't have, you don't have local minima and there's an
[585.90 → 588.24] issue that there are lots of saddle points, but no local minima.
[588.54 → 591.32] But yet there's no theory which tells you whether you're converged or not.
[591.64 → 594.06] And so it's like, what's going on?
[594.10 → 595.24] So people are trying to solve this.
[595.30 → 599.60] And I think this is where, you know, you start training a model, and you don't know,
[599.70 → 601.38] have you trained it enough?
[601.46 → 602.36] Do you need to train it more?
[602.42 → 606.44] Let me give you a really practical example, which we have with, we have a user who's using
[606.44 → 613.62] Weight Watcher to train semi-supervised models to determine whether the land you own is,
[614.56 → 616.22] qualifies for carbon credits, right?
[616.24 → 618.68] So they're trying to, can we use AI to help with climate change?
[619.30 → 622.54] And one of the biggest problems they have is how much data should we add to the model?
[622.80 → 629.06] We have a model, we have data, acquiring data, acquiring a little good, high quality labelled
[629.06 → 630.94] data is very, very expensive.
[631.48 → 635.12] You could easily spend millions of dollars on a data set, maybe 10 million.
[635.12 → 639.92] I know guys self-driving car, companies will spend easily $10 million on a data set.
[640.24 → 644.68] So it would be nice to know, given the model that you have, do you need to, if you add
[644.68 → 645.84] more data to it, will it help?
[646.08 → 647.78] So we can answer that question with Weight Watcher.
[648.24 → 651.86] If you can kind of talk a little bit about some of the underlying, because you're pointing
[651.86 → 656.20] out that there's a lot of opportunity for people to not be optimal in their approaches
[656.20 → 657.62] and kind of miss some of that.
[658.06 → 662.64] So it almost raises, almost raises a kind of bigger issue that we may have as a community
[662.64 → 668.26] if that's the case in terms of like, how do we solve some of those problems in the large?
[668.48 → 674.24] Aside from the specific tools, what are you thinking in terms of like, how should people
[674.24 → 675.54] approach these problems different?
[675.88 → 679.62] Well, look, I think the first thing you have to ask is, I'm beginning to train a model.
[680.02 → 681.30] Is my model big enough?
[681.38 → 682.22] Is it small enough?
[682.56 → 686.30] Do I really want to spend millions of dollars doing brute force hyperparameter tuning?
[686.84 → 688.22] You know, should I be tuning that?
[688.28 → 690.14] Like, here's a basic question that comes up with every client.
[690.14 → 691.02] I have a model.
[691.40 → 693.32] Forget about deep learning, SVM.
[693.60 → 695.72] Should I add more data, or should I add more features?
[696.46 → 697.28] Let's say I have XGBoost.
[697.44 → 700.62] Should I add more data, add more features, or do more hyperparameter tuning?
[700.94 → 701.72] It's all expensive.
[702.20 → 703.22] What direction do you go?
[704.02 → 707.82] And, you know, there is a it's a difficult, these are difficult problems.
[707.86 → 711.50] And if you add more data, is the data the right quality?
[711.92 → 713.36] Is the data mislabelled?
[713.54 → 714.92] Are there duplicates in the data?
[715.32 → 717.98] Is the data too similar to the data you've already added?
[717.98 → 720.46] Is it too different from the data you've already added?
[720.70 → 721.44] Basic questions.
[721.60 → 726.44] We just don't have, I mean, very, very basic, broad level questions that we have almost no answers to.
[726.50 → 727.46] Everything is brute force.
[727.94 → 735.86] You know if you want to train a neural network, you go out, and you get weights and biases, or you go to Google Cloud and you just spend a fortune on hyperparameter tuning.
[736.36 → 737.32] Do you really have to do that?
[737.84 → 739.28] Or isn't there something better you could do?
[739.92 → 740.96] Here's another example.
[740.96 → 746.12] When we started this project, there were maybe 50 open source pre-trained models, right?
[746.18 → 747.08] Open source models, right?
[747.22 → 750.54] VGG, the VGG series, Reset, things like that.
[751.06 → 753.52] You go to Hugging Face now, there are over 50,000.
[753.78 → 754.66] Which one do you pick?
[755.08 → 757.14] Should you pick BERT or something else?
[757.24 → 758.14] Everyone uses BERT.
[758.28 → 761.12] BERT is highly under, is highly under-optimized.
[761.32 → 765.30] If you compare BERT to Excel Net, Excel Net is much, much better.
[765.30 → 770.36] Not only do the academic papers show that Excel Net performs better on at least 20 different metrics.
[770.78 → 771.74] You can use Weight Watcher.
[771.80 → 772.46] I have a blog post.
[772.58 → 776.48] You can see that it's just night and day between Excel Net and BERT.
[776.74 → 780.28] But is it worth the money to spend to try to optimize Excel Net?
[780.42 → 781.72] Why does everybody focus on BERT?
[781.80 → 783.60] Because it has a cute name, and it's made by Google.
[783.84 → 787.22] I mean, you know, it's really hard to know which model to pick.
[787.76 → 788.20] And it's hard.
[788.30 → 790.00] These models are very hard to improve.
[790.64 → 793.44] So there are a lot of just broad open questions like this.
[793.44 → 794.74] Which model do I pick?
[794.74 → 796.50] How much data should I add?
[796.74 → 798.88] How do I evaluate the quality of my data?
[799.30 → 801.98] Do I really need to do brute force searching on everything?
[802.60 → 806.24] If I put something into production, how do I know if the model doesn't?
[806.32 → 807.02] It breaks.
[807.42 → 809.36] I don't know if you guys worked in production environments.
[809.42 → 811.24] I work in environments where things break every six weeks.
[811.86 → 814.12] It's, you know, Thanksgiving comes, model's broken.
[814.34 → 815.76] Christmas morning, model's broken.
[816.16 → 817.52] How do you monitor these things?
[817.88 → 823.20] So I think machine learning and certainly AI is in the intensity of engineering.
[823.20 → 826.06] Certainly compared to where we are in software engineering.
[826.20 → 828.34] We're 20 years behind where software engineering is.
[828.34 → 858.32] So Charles, I definitely, it's interesting kind of these, I guess, scenarios that you bring up.
[858.32 → 860.28] Because it's definitely something that happens.
[860.44 → 867.40] I mean, sometimes in an actual real world setting, like with my team, it's like we have what data we have.
[867.64 → 871.72] What model is appropriate that fits that level of data, right?
[871.72 → 873.66] Or maybe you have a bunch of data.
[873.88 → 879.12] And the question is, do I need all of it for this, you know, model that I've already kind of decided on?
[879.12 → 880.86] Or all of these sorts of things.
[880.86 → 884.62] And then you get to the training questions that you've brought up.
[885.04 → 893.66] I'm wondering if you could just give us a sort of high level overview of, because I think the main thing that, if I'm understanding right,
[893.72 → 898.92] the main kind of tool that's come out of this train of research that you've been working on is the Weight Watcher tool.
[898.92 → 912.82] Could you just give us a kind of broad overview of what the tool actually, like functionally does and where it fits into a researcher or a developer or a data scientist workflow?
[913.56 → 913.76] Sure.
[914.34 → 921.44] So the tool can be used both when you're trying to train models, AI models, or you're trying to monitor them in production.
[921.44 → 928.26] From a training perspective, the tool gives you insights into whether your model has converged.
[928.80 → 931.64] And it does so at a layer-by-layer basis.
[932.22 → 940.44] So I'm not aware of any other technology that allows you to look at the layers of a neural network and ask, has one layer converged and has another layer not converged?
[940.82 → 942.96] So there are cues you can look at.
[943.00 → 946.86] You can look at something called the alpha metric, which is the amount of correlation in the model.
[946.86 → 952.22] And if the alpha, usually if you have a computer vision model, your alpha should be down around two.
[953.00 → 957.54] In natural language processing transformer models, alpha should be between three and four.
[958.02 → 962.56] If your alphas are larger than that, chances are the layer is not properly trained.
[962.92 → 965.00] You can then visualize each layer.
[965.42 → 968.42] And you can look at the layer, its correlation structure.
[968.84 → 971.72] And that correlation structure should be fairly smooth.
[971.96 → 974.34] It should be linear and smooth on a log-log plot.
[974.34 → 978.90] If it's choppy or has sort of a strange shape to it, something's wrong.
[979.14 → 984.14] If your layers have lots of rank collapse, lots of zero eigenvalues, something's wrong.
[984.52 → 992.54] We've identified something called a correlation trap, which is in deep learning language would be you didn't clip your weight matrices.
[992.72 → 995.42] You didn't regularize that layer correctly.
[995.98 → 1000.74] So you can use the tool during the training of a neural network to monitor the training.
[1000.74 → 1004.18] You can find layers that are basically broken.
[1004.30 → 1005.30] They're not trained correctly.
[1005.74 → 1010.74] Think of it like you're building a house and there are cracks in the bricks.
[1010.88 → 1012.38] You put a brick in, it's cracked.
[1012.46 → 1013.22] You need to replace it.
[1013.56 → 1016.12] You can adjust regularization up and down on the layer.
[1016.26 → 1018.52] You can adjust learning rate up and down on the layer.
[1019.00 → 1025.14] You might find that when you're training a model, some layers are beginning to – they're well-trained and they begin to overfit.
[1025.26 → 1026.26] So you might want to freeze them.
[1026.26 → 1030.62] So you can freeze – so as people talk about early stopping, I talk about early freezing.
[1031.16 → 1034.34] So you might freeze some of the early layers and let the later layers converge.
[1035.06 → 1041.12] So Weight Watcher allows you to do all of this by – it's very much a – you have to do it by hand.
[1041.20 → 1043.36] You have to go in and visualize it and see what's going on.
[1043.38 → 1047.08] But it allows you to inspect your models to determine whether they're trained correctly.
[1047.42 → 1049.68] It also allows you to look at models in production.
[1049.68 → 1060.64] So if you're deploying AI models in production, and maybe you're retraining your models regularly, it would allow you to give us like a warning flag, like a model alert system that would tell you, hey, you broke this layer.
[1061.06 → 1062.40] We have an example in our paper.
[1062.50 → 1070.88] We have a paper in Nature where we show that in one of the Intel systems, they applied a data compression algorithm to compress the model to go on the hardware.
[1071.32 → 1072.94] And they screwed up one of the layers.
[1073.00 → 1074.30] And you can see this with Weight Watcher.
[1074.36 → 1075.26] It will flag it for you.
[1075.26 → 1080.26] So as you're deploying models in production, it can monitor them for you.
[1080.30 → 1081.76] And remember, it doesn't require any data.
[1081.86 → 1089.70] So it's a very light touch, very simple integration to integrate into your AL ops monitoring pipelines.
[1089.78 → 1091.64] I think of it as sort of like an AI uptime tool.
[1092.46 → 1094.02] It gives you like an early warning.
[1094.56 → 1096.34] So this is how you use the tool.
[1096.60 → 1101.68] You can use it during training to make sure your models are converging well, or they haven't converged properly.
[1101.74 → 1102.60] You can go back and fix them.
[1102.60 → 1106.48] Or you can use them after training in production to monitor for problems.
[1107.04 → 1111.30] So I was kind of trying to think of analogies in my head while you were talking.
[1111.52 → 1115.08] And you gave a good one in terms of the house and the cracks.
[1115.28 → 1124.90] One of the things I was thinking about, like you mentioned, you mentioned Burt earlier, which no doubt in the sort of time when Burt came out, it was quite an advancement.
[1124.90 → 1129.22] And like many people have built amazing things on Burt.
[1129.42 → 1133.54] But I was thinking about like that and where we've come from there.
[1133.54 → 1137.26] And also thinking about my wife owns a manufacturing business.
[1137.26 → 1143.66] And they've got this principle in manufacturing about find the current biggest bottleneck in your process.
[1143.84 → 1144.80] Right. Address that.
[1144.80 → 1149.34] As soon as you address that, there's going to be a next biggest bottleneck that you address next.
[1149.48 → 1151.52] Right. And you kind of just keep working your way through.
[1151.76 → 1155.18] So I'm wondering, like Burt, obviously, is a good advance.
[1155.18 → 1162.96] But then like you can analyze that model and see maybe where the next biggest sort of offending area is and kind of address that.
[1162.96 → 1175.80] And I was also thinking about the tool that you were mentioning, all the things you could do with it, you could probably analyze your model in development for years, you know, fixing all sorts of things and doing all sorts of things.
[1175.80 → 1178.08] Right. But at some point you have to ship your model.
[1178.26 → 1188.50] Right. So maybe there's this process of, and I'm wondering your thoughts on this, of like you using the tool to find sort of these like worst offending parts of your model.
[1188.50 → 1194.56] Yeah. Yeah. Yes. And maybe like at a certain point you get to a point of diminishing returns or something like that.
[1194.68 → 1197.08] Right. Yeah. This is a coarse grain tool.
[1197.50 → 1202.62] It's not meant to go in and study epoch by epoch and try to fine tune exactly what's going on.
[1202.74 → 1209.90] That's exact. I'm really glad you brought this up, Daniel, because sometimes you work with the academics, and they always want to use it as a regularized.
[1210.04 → 1213.48] You want to optimize the loss. No, no, no. That's not the point. It's an engineering tool.
[1213.72 → 1217.68] It's an engineering tool. It's designed to go in and find out where the cracks are.
[1217.68 → 1220.94] So if you're, I don't know if you guys in San Francisco, you know about the Millennium Tower.
[1221.38 → 1228.92] Yeah. So my little nephew, he's he's all into construction, and he's always talking about they got to tear the Millennium Tower down, tear it down, junk it.
[1229.12 → 1233.34] Because it has they built this tower, and it's like the leaning tower of pizza. It's tilting.
[1233.44 → 1238.54] And if you go into the basement of the Millennium Tower, this is like, you know, like condos, like multimillion dollar condos.
[1238.90 → 1242.44] You know, I think probably like, you know, the Marissa Meyer may own a condo there.
[1242.44 → 1248.06] I mean, it's ridiculous that they built this thing. And downstairs you look and there are cracks in the steel.
[1248.40 → 1251.86] It's like, guys, the thing's going to it's going to fall down. It's cracked.
[1252.34 → 1258.26] And it's like this is what Weight Watcher does. You go into your models and ask, are there gross problems that should not be there?
[1258.54 → 1263.86] Right. This layer is overtrained. This layer suggests that the data is mislabelled.
[1264.06 → 1267.26] This layer has a correlation trap. This is what you're trying to do.
[1267.26 → 1273.04] And, you know, frequently in engineering, you're under time constraint. So, you know, you got to get this thing out and into production.
[1273.16 → 1282.08] You want to make sure it's not crazy. And it allows you to Weight Watcher allows you to detect problems that you could not detect in any other way.
[1282.22 → 1284.32] And that's the key. It allows you to find a major problem.
[1284.98 → 1291.20] So one of the things I was wanting to ask you, because you said something a moment ago and kind of circling back to that, that I'm very curious about.
[1291.20 → 1299.30] To bring me and other people in our audience along that may not be as familiar with that, I often rely on Daniel's expertise on this, and I want to rely on yours on this.
[1299.54 → 1313.54] You mentioned when we're talking about, you know, kind of testing those layers as you did go back to the alpha, and you specified, you know, for, you know, ranges of two for the visual and the three to four for like natural language models and stuff.
[1313.54 → 1317.94] So I'm assuming that that's one of the mechanisms that you're using in the software.
[1318.20 → 1324.48] Can you talk a little bit about what are the other mechanisms that are there along with that and maybe how alpha is used?
[1324.48 → 1335.78] Like what if somebody is not familiar with that concept, what is it about alpha that's identifying that so that they understand that a particular layer might be brittle in the sense of it's not fully converged?
[1335.92 → 1337.78] You know, how are you approaching that?
[1338.02 → 1341.90] Kind of bring us along to try to catch us up with you on how you're thinking about that.
[1342.18 → 1343.28] Like, why does it work?
[1343.54 → 1343.74] Yeah.
[1343.78 → 1344.48] Why does it work?
[1344.54 → 1344.88] What is it?
[1344.90 → 1351.02] What is it about alpha and other things that you're using in the software that yield that level of insight that you're describing?
[1351.44 → 1354.38] So what we know from where does deep learning work?
[1354.38 → 1363.62] Deep learning works on natural things, natural images, voice, text, things that are really part of the natural world.
[1363.76 → 1366.62] And the natural world exhibits a multifractal structure.
[1367.08 → 1373.18] You know if you look at a tree, you know, I don't know if you remember like L systems or computer science or, you know, sort of Mandelbrot's work.
[1373.18 → 1379.58] Most natural systems have or just think about text, you know, zip laws, you know, power law structure in text and documents.
[1379.78 → 1384.04] All natural data has a power law structure, a fractal structure to it.
[1384.52 → 1391.20] And when you have the way neural networks learn is they learn the multifractal, the multifractal nature of the data.
[1391.20 → 1396.42] And that's why they work so well on things like text and images and why they don't work great on tabular data sets.
[1397.16 → 1399.86] So what you're doing is there are correlations in the data.
[1399.94 → 1400.48] Data is correlated.
[1400.72 → 1402.12] You're trying to learn the correlations.
[1402.12 → 1412.16] And frequently you're trying to learn very subtle correlations you couldn't find in some other way, you know, using some simple clustering algorithm or an SVM or something like that.
[1412.80 → 1416.36] So what we're doing is we're measuring the fractal nature of the data.
[1416.44 → 1423.44] And every layer of a neural network gives you some measure of the fractal properties in that level of granularity.
[1423.72 → 1425.76] And so alpha is like a measure of the fractal dimension.
[1425.76 → 1431.26] And what we know is that it measures the amount of correlation in that layer.
[1431.72 → 1433.96] In other words, you're learning the data is obviously not random.
[1434.66 → 1435.54] It can't be random.
[1435.68 → 1436.06] You're learning.
[1436.16 → 1437.12] You're trying to learn patterns.
[1437.60 → 1446.22] So what we've discovered empirically, and there's some deep theoretical reasons for this, but qualitatively what's happening is you're learning the natural patterns in the data.
[1446.48 → 1448.90] And those patterns, you know, they have to be there.
[1448.90 → 1455.46] So if you're looking at text data, and you start seeing alphas around six or seven or eight, the layer hasn't learned the correlations.
[1455.76 → 1456.86] It just didn't learn anything.
[1457.26 → 1462.48] And it's just sort of there, or it learned that the correlations are so weak that it's not really contributing to anything.
[1462.62 → 1465.80] So you just – and we know that many of these models are just had these extra layers.
[1466.00 → 1470.46] They're way overparametrized, you know, and they're – you know, so that's what's happening.
[1471.10 → 1478.52] And if the correlations, if there are strange or spurious correlations, there are things that cause alpha to be small for spurious reasons.
[1478.52 → 1482.04] It's like, you know, you didn't regularize your layer correctly.
[1482.18 → 1483.62] And so there's a giant weight matrix.
[1483.62 → 1487.10] Like, you didn't clip the weight matrix all of it, so the regularized failed.
[1487.46 → 1495.00] So it can detect the difference between when there are problems with the optimizer and when there's actual natural structure in the data.
[1495.06 → 1496.72] And it allows you to distinguish between these two.
[1497.20 → 1497.92] And that's what it's doing.
[1497.92 → 1507.20] Am I correct just for clarity's sake in terms of when we say, like, it's doing this without the test data or the training data?
[1507.30 → 1516.64] Really, you're doing these calculations, and you're detecting these parameters, these metrics based on the weight matrices, right?
[1516.74 → 1517.42] Is that correct?
[1517.78 → 1518.06] Yes.
[1518.28 → 1519.34] Only on the weight matrices.
[1520.58 → 1522.00] You don't need to look at the data.
[1522.00 → 1532.86] So in that case, is it like the tool itself in terms of how people would run it, because it's doing these matrix calculations, is it necessary?
[1533.32 → 1535.26] Like, could you speak to like the computational?
[1536.02 → 1536.42] Okay.
[1536.62 → 1536.90] Yeah, yeah.
[1536.90 → 1544.20] And like, am I going to spend five hours waiting for Weight Watcher to analyze my model or is it going to happen in five seconds?
[1544.38 → 1546.98] The current model right now, it depends on the size.
[1547.06 → 1549.56] It runs a singular value decomposition on each layer.
[1549.56 → 1552.88] So that's a high memory CPU level.
[1553.46 → 1557.54] It's a high memory CPU intensive task.
[1557.94 → 1559.80] It doesn't, it's not optimized for GPU.
[1559.96 → 1561.00] So you'd run a normal CPU.
[1561.34 → 1562.54] It does require some memory.
[1562.84 → 1564.04] Most layers aren't too large.
[1564.16 → 1566.42] So it could take anywhere from a couple of minutes to an hour.
[1566.58 → 1570.74] If you're trying to run it on GPT and you have a thousand layers, it's going to take some time, right?
[1570.98 → 1576.42] If you just have a few layers in your model, and you're training like a small model, it's very, very fast.
[1576.42 → 1583.38] You know, generally you would hope that it is faster than an epoch in training, but it's not GPU optimized.
[1583.56 → 1588.50] So one of the things we're working on is I'd like to, if I commercialize the product, is to make a version that's very, very fast.
[1588.76 → 1591.96] It's like it would like distribute all the calculation on the nodes and come back to you.
[1592.32 → 1597.52] So that's the kind of, I get from, so this is an open source tool, but it runs a simple SVD calculation.
[1597.52 → 1604.80] So it's a little compute intensive, but again, sort of my theory on this is that if you're training small models, it's pretty fast.
[1605.02 → 1610.84] If you're training really, huge models, well, you're going to have to compute, chances are you have the compute resources anyway.
[1611.10 → 1612.90] And you're not renting a GPU for it.
[1612.92 → 1614.62] You don't need the GPU, even though it can run it.
[1614.68 → 1616.12] So that's sort of the takeaway.
[1616.12 → 1646.10] Thank you.
[1646.12 → 1658.98] Well, Charles, I mean, when I first saw the tool, I was very interested in it.
[1658.98 → 1668.94] And I did take time to go ahead and just pull it in one of my notebooks and look at one of my own models, because I did want to get hands on with it.
[1669.04 → 1673.54] It was a question answering model based on XLM Berta.
[1673.54 → 1677.60] And I analyzed it with Weight Watcher.
[1677.82 → 1685.24] I did not do every single thing that you describe on your repo because I'm still, you know, dipping, dipping my toes.
[1685.40 → 1685.58] Right.
[1685.80 → 1686.58] I guess great.
[1686.58 → 1687.40] It ran.
[1687.40 → 1687.46] It ran.
[1687.54 → 1688.64] It actually ran.
[1688.90 → 1689.04] Yeah.
[1689.16 → 1689.32] OK.
[1689.50 → 1691.50] And so it's a PyTorch based model.
[1691.58 → 1691.80] It ran.
[1691.94 → 1692.90] I didn't time it.
[1692.96 → 1694.24] So I don't know exactly how long.
[1694.38 → 1701.30] But I did find out, at least I found out, according to Weight Watcher, 10 of my layers are under trained.
[1701.70 → 1702.38] So that could be.
[1702.38 → 1705.34] Yeah, I at least found that out.
[1705.52 → 1710.28] So could you speak a little bit about like the tool itself?
[1710.56 → 1713.88] So you mentioned like how people can integrate it in their workflows.
[1714.14 → 1723.38] Could you mention a little bit more about the open source project and like how people like if I'm like I did, and I want to do this on one of my models?
[1723.38 → 1727.72] How would I go about doing it and how easy is it to get it running on a model?
[1727.98 → 1731.74] Well, you know, this is just it's a tool I've been writing in my spare time based on my research.
[1731.82 → 1733.12] There's no funding for any of this.
[1733.26 → 1735.90] I published with UC Berkeley, but they're not funding any of this.
[1735.94 → 1739.06] They're just sort of like I'm just there to just kind of help me out a bit.
[1739.24 → 1740.36] I've written it all myself.
[1740.98 → 1741.74] It's all open source.
[1741.80 → 1743.72] I have one of my staff guys help me out early on.
[1744.06 → 1745.04] Pip install Weight Watcher.
[1745.46 → 1750.08] The way it's written now, you probably need to have both TensorFlow and PyTorch installed in your environment.
[1750.08 → 1753.90] If you want, we can, I can make a version that doesn't require both of those.
[1754.00 → 1755.00] I have no one's asked yet.
[1755.62 → 1758.90] One of the challenges I have with the tool is that I have 60,000 downloads.
[1759.02 → 1760.00] I have no idea who's using it.
[1760.40 → 1763.90] So if you're using the tool, let me know so I can help you.
[1764.02 → 1765.48] I don't know what you're doing with it.
[1765.56 → 1770.88] And I'm not going to your know, I don't want to end up in feature creep where I design features in the wild.
[1771.10 → 1772.44] You know, I need to know what you're doing.
[1772.90 → 1774.28] So if you tell me, I'll help you.
[1774.36 → 1775.24] We have a Slack channel.
[1775.32 → 1777.46] You can go on Slack and you can ask me, and I'll help you.
[1777.46 → 1779.66] But basically, its Pip install Weight Watcher.
[1780.08 → 1781.66] And you just give it a model.
[1781.78 → 1784.38] You say Weight Watcher equals Weight Watcher.
[1784.46 → 1785.50] Model equals my model.
[1785.60 → 1787.02] And you say Watcher.analyze.
[1787.22 → 1787.72] That's it.
[1787.80 → 1789.82] And it will return a data frame with quality metrics.
[1790.26 → 1794.36] If you say Watcher. Analyze plot equals true, it will generate a bunch of plots.
[1795.00 → 1796.08] It will generate the plots.
[1796.18 → 1796.76] It's meant to be.
[1796.86 → 1798.60] I've been running it in a Jupyter notebook.
[1798.76 → 1799.52] That's how I run it.
[1800.02 → 1802.14] In principle, you could run it in a production environment.
[1802.14 → 1808.32] Again, it's really a very – it's not even an alpha one tool yet.
[1808.40 → 1810.24] It's still like 0.56, 0.57.
[1810.60 → 1813.00] So, you know, if you do that, reach out to me.
[1813.14 → 1816.74] You know, we can make a version that's more stable if you need to run it in a production environment.
[1816.88 → 1819.94] But I've mostly been using it in – it runs in the Jupyter notebook.
[1820.14 → 1820.86] You get a data frame.
[1820.96 → 1821.98] You analyze the data frame.
[1822.46 → 1823.76] You run a Google Cola notebook.
[1824.20 → 1825.72] You say plot equals true.
[1825.78 → 1826.82] It gives you a bunch of plots.
[1827.16 → 1829.16] If you add some other options, it will give you more plots.
[1829.16 → 1830.38] And then you analyze the plots.
[1830.98 → 1834.86] So let me ask you a question as kind of follow-up to what you and Daniel were just talking about.
[1835.24 → 1843.22] If you're looking at the workflow, like – and so, you know, Daniel said there were like, what, 10 layers that had not converged, you know, sufficiently.
[1843.76 → 1845.14] How does that change the workflow?
[1845.44 → 1854.28] For someone who hasn't done what Daniel's done and gotten his hands on, someone just listening, talk a little bit about what they were doing before versus the workflow they're doing now.
[1854.32 → 1858.46] Now that they have the insights that Weight Watcher is bringing to it, what does that look like for the practitioner?
[1858.46 → 1860.20] Well, here's the first thing.
[1860.30 → 1862.92] This is exactly what happened to one of Michael's postdocs and students.
[1863.42 → 1864.86] Go back and look at the regularization.
[1865.02 → 1867.26] Did you add enough dropouts on your layer?
[1867.74 → 1869.10] Are the learning rates too large?
[1869.48 → 1870.56] Do you not have enough data?
[1870.98 → 1872.34] Is your model just too big?
[1872.60 → 1880.40] Are the earlier layers converging in the later – if the later layers are not, maybe you should freeze some of the earlier layers and give the later layers time to converge.
[1880.90 → 1882.08] Maybe you need to run it longer.
[1882.18 → 1883.38] You need to run SGD longer.
[1883.58 → 1886.70] Maybe, you know, you need to adjust some of your hyperparameters because you're not getting tuned.
[1886.70 → 1890.58] You know, try to adjust your hyperparameters, so alpha goes down, not that it goes up.
[1890.84 → 1892.80] Those are the kind of things you need to do during training.
[1893.44 → 1893.52] Yeah.
[1893.70 → 1897.20] So if you were – maybe you could also mention the workflow.
[1897.64 → 1907.22] I find it very interesting what you were saying about, like, the workflow of potentially using this, like, within the training loops as well, like, as you're training the model.
[1907.22 → 1907.66] Right.
[1907.76 → 1917.26] So one thing you could do is definitely run your model, right, like I did, and then look at it afterwards and see, oh, jeez, I need to do something about this or that.
[1917.66 → 1929.00] And then, of course, like, then probably is the harder part of the problem is connecting with, like, okay, does that mean I do one of those things you just mentioned or another one of those things you just mentioned?
[1929.00 → 1932.28] But what about that workflow, like, in the training loop?
[1932.44 → 1934.00] How might that work?
[1934.14 → 1951.40] I know that, you know, maybe some people have heard of certain things related to, like, optimizing either not doing brute force hyperparameter tuning but doing some sort of – some, like, auto ML type of stuff or something.
[1951.40 → 1953.56] Like, people have thought about these things.
[1953.96 → 1960.06] So, like, when you're pulling Weight Watcher into the training run, how would you think about that being used?
[1960.26 → 1968.24] If you want to give Google Cloud a million dollars to do auto ML and then have them own your models for you and feed them back to you, knock yourself out.
[1968.60 → 1969.60] I don't want to do that.
[1969.70 → 1970.48] I don't want to be trapped.
[1970.58 → 1972.86] You know, that's what the auto ML offering is.
[1972.88 → 1975.48] It's an offering to blow millions of dollars.
[1975.48 → 1982.88] Or if you want to get some tool like H2O and auto-tune a model and then find out it doesn't scale, and then you have to redo it, we've had clients with that problem.
[1983.58 → 1983.68] Right.
[1984.10 → 1992.52] I think it's – there's this wider field, though, of sort of, I guess, meta-learning and kind of learning on that.
[1992.74 → 1999.52] And I don't know if this would fit – like, the Weight Watcher stuff would fit into that larger space of research, I guess.
[1999.92 → 2001.44] Look, what are you trying to do?
[2001.52 → 2003.02] Like, what does it mean to be optimal?
[2003.02 → 2010.16] If being optimal means that your alphas are close to two or three, then you should adjust your hyperparameters such that the alphas go down.
[2010.48 → 2011.26] That's what you do.
[2011.68 → 2019.76] And now doing that analytically, typically in doing what are called analytic derivatives, meaning you try to compute the gradient from that, that's somewhat difficult.
[2019.88 → 2026.06] It could be done because you have to compute the eigenvalue spectrum, and then you have to fit it, and then you have to figure out the derivative.
[2026.22 → 2028.32] And that's a very complex, non-linear calculation.
[2028.50 → 2029.12] It's very iterative.
[2029.46 → 2032.54] It could be done numerically, or it could be done analytically with some work.
[2032.54 → 2033.46] It's a lot of work.
[2033.56 → 2036.22] I would love to have VC funding like Hugging Face to do that.
[2036.62 → 2037.14] But I don't.
[2037.24 → 2037.72] It's just me.
[2037.80 → 2038.22] Me and you.
[2038.66 → 2040.16] So you just try to tune your parameters.
[2040.32 → 2041.00] The alpha goes up.
[2041.06 → 2041.70] Go the other way.
[2042.10 → 2046.60] If you turn your learning rate up, and you find your alphas are going up, tune the learning rate the other way and hopefully they'll go down.
[2046.94 → 2051.38] Obviously, it's a complex optimization problem because you have 100 layers.
[2051.48 → 2052.28] You have 100 alphas.
[2052.28 → 2060.60] And so you're trying to tune different layers, and you're trying to tune your layer learning rates and your amount of dropout and the amount of momentum.
[2061.50 → 2068.64] So in principle, you could try to do that algorithmically in a way using like a Bayesian type approach where you try to get your alphas to go down on every layer.
[2068.76 → 2070.54] I mean, it is in principle you could do that.
[2070.98 → 2073.80] It's a complex, you know, complex optimization problem.
[2073.84 → 2074.98] But that's what I would recommend.
[2074.98 → 2077.98] And I think it's theoretically well grounded.
[2078.16 → 2080.32] I mean, the point is that you want to learn more correlations.
[2080.98 → 2088.04] Typically, what I found is that it's a good tool for newbies because you get into a model, you start doing something, things are totally wrong.
[2088.36 → 2089.72] And you can go in and fix some problems.
[2089.86 → 2090.60] OK, now we fixed it.
[2090.64 → 2092.10] We found like what did we not do?
[2092.34 → 2095.62] Like I didn't put the proper regularization on these layers.
[2095.74 → 2097.54] Let me add regularization and try again.
[2097.60 → 2099.02] And you can see that, OK, that's much better.
[2099.54 → 2103.20] So from a newbie perspective, it's a very good tool because it helps you get started.
[2103.20 → 2104.16] Now, it does work.
[2104.16 → 2108.42] Keep in mind the tool works at the end of training, not in the early stages of training.
[2108.84 → 2110.34] You've got to let the thing bake for a while.
[2110.66 → 2111.40] You know, you can't.
[2111.46 → 2111.98] It doesn't.
[2112.10 → 2115.22] Once it's about halfway through training, then you can start looking at things.
[2115.48 → 2117.38] It's got to have some correlations.
[2117.90 → 2119.22] But this is what it's for.
[2119.46 → 2131.82] Typically, this is sort of, you know, trying to do large scale meta learning, which is meaning you'd have to integrate the tool into some sort of process that allows you to look at the alphas or look at more details in the layer.
[2131.82 → 2137.00] The shape of the spectral density, the number of spikes, the alphas, the volume of the spectral density.
[2137.00 → 2138.98] And figure out how to tune from that.
[2139.04 → 2149.62] I mean, this could even be used in a reinforcement learning situation where the reward, instead of the reward being something that, you know, the agent takes, the reward is, oh, I got smaller alpha.
[2149.62 → 2158.76] So I have rewards on every layer, and I sum the rewards in some average way to try to get the optimizer to work, even in situations where I don't know what the reward is for a reinforcement learning situation.
[2159.42 → 2166.90] Obviously, that would be nice in areas like you're trying to trade in the markets, because you can't take actions that trade.
[2167.10 → 2170.16] You can't trade on historical data and expect to learn from that.
[2170.16 → 2177.92] So this gives you a way of sort of doing things in a supervised or semi-supervised way that doesn't require peeking at the test data to optimize.
[2178.64 → 2181.16] And I hope that answers the question, but that's sort of the idea.
[2181.24 → 2183.68] And there are lots of things people, I think, want to try.
[2183.98 → 2185.32] I think it'd be great if you try them.
[2185.74 → 2191.24] Yeah, I mean, I definitely appreciate you being transparent about where the tool is and all that.
[2191.24 → 2201.26] And really, the possibilities that might happen with the tool and kind of the there are a lot of opportunities to explore usage and further development.
[2201.66 → 2204.20] Part of what I want to do with the tool is build an open source community.
[2204.44 → 2207.84] I can't do everything myself, and there are lots of things to do.
[2207.94 → 2212.22] And if people want to get involved in a community, join the Slack channel, we can build things, right?
[2212.26 → 2213.30] That's what open source is.
[2213.36 → 2219.54] And I think there are a lot of people may have ideas and will be able to contribute in ways that, you know, we just expand it.
[2219.54 → 2228.04] And I think that it's, again, right now, to me, the way you train neural networks now, it's like you build a bridge, you drive a car over the bridge, you see if the bridge falls down.
[2228.26 → 2229.64] And you do it again and again and again.
[2229.74 → 2233.42] How many cars are you going to crash into the ocean until you get the bridge right?
[2233.50 → 2234.94] No, people don't build bridges like that.
[2235.04 → 2237.70] You know, you build bridges by having engineering principles.
[2238.00 → 2242.86] You understand, here are the engineering principles that go in, and this is the load it can take, and this is the wind shear.
[2243.08 → 2245.94] And, you know, you try to build bridges that actually stay up.
[2245.94 → 2248.24] And right now, I think deep learning is so brute force.
[2248.24 → 2254.72] It's like you just spend as much money as you can, do as much brute force as you can, and if it doesn't work, you try it again.
[2255.04 → 2258.22] And there are no principles behind what you're doing.
[2258.34 → 2262.88] And we're trying to add some, you know, and principles that are based in deep theory.
[2263.24 → 2270.20] Like, they're empirical rules of thumb, but there's also deep theoretical reasons why they work, just like in any other field of optimization.
[2270.20 → 2280.24] Which I'm curious, I'm kind of going back to the engineering and the kind of, you know, talking about, you know, as this matures much, you know, and trailing the software engineering world.
[2280.24 → 2291.54] But one of the decisions that we all make as engineers that we're doing is kind of like, as we're creating open source community, and we're trying to provide the value for that community that you're talking about.
[2291.54 → 2297.24] Do you see the future as being community specifically built around Weight Watcher?
[2297.46 → 2307.54] Or is there an opportunity potentially to add the value that Weight Watcher is bringing and those insights that you described and roll them into some of the other existing communities?
[2307.84 → 2315.38] Do you have any opinions or, you know, thoughts about how you integrate this in for the value of the larger community?
[2315.38 → 2321.30] Well, look, I think I'd like to have as a community of people who are training models and getting them to interact with each other.
[2321.40 → 2323.46] A lot of the people, like I said, it's hard to get feedback.
[2323.58 → 2324.76] People are doing things in industry.
[2325.16 → 2330.20] And because they are constrained by NDAs, they can't really talk about what they're doing.
[2330.68 → 2339.94] And I think it gives people an opportunity to really get into the space and learn how training of neural networks works without being constrained by your employer or your contract.
[2340.30 → 2342.30] So you can really do a lot of what this is.
[2342.30 → 2350.44] I think there are other communities doing things like people building hyperparameter optimization tools or people building reinforcement learning tools.
[2350.58 → 2352.32] We'd be happy to integrate the tool in.
[2352.94 → 2356.14] The challenge is always, you know, you want to make a tool that is self-contained.
[2356.72 → 2361.60] You know, if people fork the tool and begin changing it, it ends up, I don't know if you guys know the story of Emacs.
[2362.08 → 2363.82] I was at Campaign-Urbana when this happened.
[2363.94 → 2367.22] You know, they wanted to port Emacs to basically X Windows.
[2367.84 → 2369.28] And Stallman didn't want to do it.
[2369.30 → 2369.86] And they forked it.
[2369.92 → 2371.16] You have X Emacs, you have Emacs.
[2371.16 → 2371.80] It killed it.
[2371.90 → 2374.44] You know, forking Emacs killed it because you have the X Emacs crowd.
[2374.56 → 2383.02] And, you know, these guys went off and started Netscape and, you know, probably all retired now, or they're sitting at the top of, you know, hang out with a roof of Google vesting or Netscape.
[2383.16 → 2384.26] But this is the problem.
[2384.30 → 2385.64] You want to make sure you have an open force community.
[2385.78 → 2388.66] You don't want, I mean, I want people to contribute and feel they can do things.
[2389.16 → 2393.98] If we fork it, and it goes into other communities, it kills it because now those contributions don't come back.
[2393.98 → 2395.54] You end up in this sort of weird battles.
[2395.76 → 2397.50] And there's no value in that.
[2397.86 → 2400.94] I mean, what we want to do is help people, you know, to help people.
[2401.16 → 2406.92] And if it's necessary at this point, you know, commercialize the tool and turn it into something which we can support.
[2407.04 → 2407.78] Like Hugging Face.
[2407.88 → 2409.26] I mean, Hugging Face is a lot of open source.
[2409.26 → 2413.00] But, you know, any sophisticated technology needs maintenance.
[2413.38 → 2414.52] You know, you buy a copier machine.
[2414.92 → 2416.44] It's not open source because it needs maintenance.
[2416.92 → 2419.40] So even a tool like Weight Watcher needs maintenance.
[2419.68 → 2425.88] So I would love to be able to work with people who would like to put it in production and develop it.
[2425.92 → 2433.82] And then at some point we realize, look, you know, we really need to put a service contract around this so that we can maintain it and solve some of the harder problems for you.
[2433.84 → 2434.62] I'd be happy to do that.
[2435.00 → 2437.42] And I think that that's really what we're trying to do.
[2437.42 → 2440.66] Because this is, you know, there's also a lot of opportunity for scientific research.
[2441.20 → 2445.86] You know, Weight Watcher has been a lot of it's come from doing research, statistical mechanics and learning theory.
[2446.18 → 2449.12] You know, we have papers in JMLR, Nature, ICML, ADD.
[2449.42 → 2455.58] There's a lot of opportunity for students to, you know, we have one student who is at a bank who just did his master's thesis on Weight Watcher.
[2455.70 → 2457.76] And so there's a lot of that kind of opportunity as well.
[2457.82 → 2459.50] And I think there's a lot of room for improvement.
[2460.14 → 2465.38] As we kind of get to the end here, I was wondering just quickly as we close out,
[2465.38 → 2478.62] I know you've spent a lot of really valuable time and investing in the areas maybe that people aren't focusing on in the AI community in terms of the training side of things and ways to help them in those gaps.
[2478.84 → 2484.94] As you look forward to, you know, the future of where the AI community is going,
[2484.94 → 2494.32] what encourages you about sort of the direction of things, or what excites you about what's exciting for you in the community right now?
[2494.68 → 2496.76] You know, for me, I'm a physicist at heart.
[2497.10 → 2498.00] I did theoretical chemistry.
[2498.16 → 2499.38] I did theoretical physics, you know.
[2499.70 → 2501.14] In some sense, I'm kind of the runt of the litter.
[2501.28 → 2506.46] Like one of my classmates, you know, colleagues went off and started AlphaFold, which solved the 50-year grand challenge.
[2506.54 → 2510.86] I have another who has started a company who's going to label all the world's translational medical data.
[2510.86 → 2512.02] So I'm used to that.
[2512.18 → 2519.62] For me, this is an opportunity to really show that we can use theoretical physics in a way that can have a broad impact.
[2519.74 → 2529.30] You can use theory to build sophisticated engineering tools and a connection between a lot of the deep sort of Cold War education I have to build tools for engineers.
[2529.50 → 2535.20] There's a very famous statement by Carver Mead, who's a very famous electrical engineer from Caltech,
[2535.26 → 2538.50] who said every useful experiment eventually becomes a tool.
[2538.50 → 2543.02] Everything you can measure eventually becomes a tool, you know, that you give to an engineer.
[2543.44 → 2546.48] And so I would just like people to realize, look, you can do deep theory.
[2546.88 → 2549.90] There's a lot of fun and interesting stuff to do.
[2549.94 → 2557.30] And we can turn theory into tools that people can use and build a community and, you know, just have a broader impact.
[2557.42 → 2559.80] I think that AI – I mean, I did AI in the 90s.
[2560.26 → 2561.44] People thought we were crazy.
[2561.54 → 2562.48] Like, this stuff doesn't work.
[2562.56 → 2563.56] Nobody believed it, right?
[2563.58 → 2564.52] Why are you doing neural networks?
[2564.52 → 2569.50] People think neural networks are invented by computer scientists, but there's a whole group of theoretical physicists doing this stuff for years.
[2569.74 → 2576.18] And, you know, understanding sort of who we are, how the brain works, how we think, what's actually going on up here.
[2576.46 → 2577.78] And I think it's a very exciting time.
[2577.96 → 2578.90] And that's why I'm doing this.
[2578.94 → 2581.44] I think there's a lot we can offer from the scientific community.
[2581.56 → 2586.76] There's a broad – I think there are really deep, broad connections between general science and what's going on in AI.
[2586.76 → 2590.64] And that can connect back to the engineering world.
[2590.82 → 2592.56] And I think that there are big problems.
[2592.80 → 2598.04] Like, one of the things I'm really proudest of with Weight Watcher is that there are companies using it to help climate change.
[2598.46 → 2599.40] Weight is a huge problem.
[2599.52 → 2604.62] If you can use it to find some way to solve this massive problem we have, I think that would be fantastic.
[2604.84 → 2605.26] That's awesome.
[2605.44 → 2607.60] Well, I think that's a wonderful way to close out.
[2607.74 → 2609.74] Really, really appreciate your perspective there.
[2610.00 → 2613.32] And, yeah, thank you so much for taking time to join us, Charles.
[2613.38 → 2613.92] It's been a pleasure.
[2614.18 → 2615.38] Hey, I really appreciate it, too.
[2615.38 → 2616.80] I'm glad we were able to set this up.
[2616.88 → 2618.60] And I look forward to the podcast.
[2618.88 → 2621.78] And I really look forward to anyone who tries to use the tool, wants to use it.
[2621.84 → 2622.80] Please reach out to me.
[2623.22 → 2624.18] Let me know how it's working.
[2624.76 → 2626.20] Complain to me if you don't like it.
[2626.58 → 2628.12] I'm not going to fix it if you don't tell me.
[2628.18 → 2629.06] I don't know what's wrong with it.
[2629.12 → 2631.54] I'm not going to – I can't fix what I don't know is broken.
[2632.20 → 2636.10] And I would love to have people join the community and build something great together.
[2636.34 → 2636.64] Awesome.
[2636.86 → 2637.52] Thanks so much.
[2638.00 → 2638.26] All right.
[2638.36 → 2638.92] Thanks, guys.
[2639.48 → 2639.96] Thank you.
[2645.38 → 2649.44] All right.
[2649.60 → 2651.18] That is our show for this week.
[2651.44 → 2653.80] If you dig it, don't forget to subscribe.
[2654.38 → 2656.98] Head to practicalai.fm for all the ways.
[2657.50 → 2662.90] And if Practical AI has benefited your life, pay it forward by sharing the show with a friend or a colleague.
[2663.26 → 2666.22] Word of mouth is the number one way people find shows like ours.
[2666.22 → 2675.50] Thanks again to Vastly for fronting our static assets, to Fly.io for backing our dynamic requests, to Break master Cylinder for the beats, and to you for listening.
[2675.74 → 2676.40] We appreciate you.
[2676.66 → 2677.60] That's all for now.
[2677.80 → 2679.30] We'll talk to you again on the next one.
