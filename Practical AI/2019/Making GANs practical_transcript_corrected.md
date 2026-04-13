[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.04] And unlike standard droplets, which use shared virtual CPU threads,
[29.04 → 32.88] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.42 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.34 → 45.20] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.20 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 → 88.56] productive, and accessible to everyone.
[88.94 → 93.42] This is where conversations around AI, machine learning, and data science happen.
[93.42 → 98.20] Join the community and snag with us around various topics of the show at changelog.com slash community.
[98.42 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.48 → 102.28] And now onto the show.
[106.88 → 110.68] Welcome to another episode of Practical AI.
[111.08 → 112.66] This is Daniel Whiten ack.
[112.76 → 115.82] I'm a data scientist with SIL International,
[115.82 → 119.72] and I'm joined as always by my co-host, Chris Benson,
[119.96 → 123.16] who is a principal AI strategist at Lockheed Martin.
[123.60 → 124.28] How are you doing, Chris?
[124.48 → 125.20] Doing well today.
[125.30 → 125.92] How's it going, Daniel?
[126.30 → 127.40] It's going pretty good.
[127.52 → 131.74] I've got, you know, models training and messy data to work with.
[131.84 → 134.14] So as good as any day could be, I guess.
[134.56 → 135.68] What more could you ask for?
[136.16 → 138.12] What more could you ask for?
[138.38 → 142.32] I guess in certain scenarios, you might ask for interesting models,
[142.32 → 144.98] which is what we've got to talk about today.
[145.20 → 148.84] On previous episodes, I know we've mentioned GANS a few times,
[149.08 → 152.34] and we've talked about some of the specifics,
[152.66 → 154.94] but not a whole show devoted to them.
[155.38 → 158.38] And so we thought we'd dig into this topic a little bit more.
[158.86 → 161.42] And one of the ways that we thought we could do that
[161.42 → 163.96] was to get some experts, and that's what we've done.
[164.06 → 167.88] So we've brought in Jacob Lunger and Vlad Bach,
[167.98 → 171.00] who are the authors of the book GANS in Action.
[171.00 → 175.08] And they're going to help us parse through all things GANS.
[175.30 → 176.86] So welcome, Jacob and Vlad.
[177.36 → 177.78] Thank you.
[178.10 → 179.14] Yeah, thank you for having us.
[179.78 → 183.22] So before we begin and jump into GANS specifically,
[183.52 → 185.42] let's jump into each of your backgrounds
[185.42 → 188.10] and hear about how you ended up where you're at.
[188.26 → 190.36] So maybe, Jacob, could you start things out?
[190.66 → 190.86] Sure.
[191.34 → 195.26] So I was sort of working in machine learning since about 2013.
[195.70 → 197.48] Obviously, back then, GANS weren't a thing,
[197.74 → 199.96] but I sort of fell in love with the field.
[199.96 → 206.20] And I was sort of firstly curious about all the latest and greatest things
[206.20 → 207.28] going on in research.
[207.48 → 210.78] And as I was sort of following conferences and the researchers
[210.78 → 213.18] that I really respect and admire,
[213.70 → 217.28] I came across this thing called Generative Adversarial Network
[217.28 → 219.36] sometime in 2015, I believe.
[220.08 → 223.76] So that was quite soon after the original paper by Ian Goodfellow came out.
[223.76 → 227.06] And I just sort of fell in love with the technology.
[227.38 → 232.66] And the whole idea that I'm sure we'll get into later just kind of really made sense to me.
[233.04 → 239.00] So I was, from that point on, really curious, but only sort of as a part-time hobby.
[239.88 → 242.50] And then over time, things sort of started picking up.
[242.50 → 245.56] So I started writing more blog posts about it.
[245.72 → 249.54] And then eventually, Manning approached me with a book offer.
[249.54 → 253.76] So I think that was where it really started to take a more coherent form.
[253.98 → 256.36] And I started dedicating more and more time to it,
[256.74 → 259.08] to now where it's taken over all of my life.
[259.26 → 263.50] You know, I'm working full-time with GANS and, you know,
[263.62 → 268.56] doing these types of, you know, communication and outreach type of thing,
[268.78 → 273.38] which I think, you know, is just a testament to how far GANS as a field have gone.
[273.82 → 276.10] So it's kind of ramped up a little slowly.
[276.30 → 280.08] But, you know, now it's kind of really, you know, took over every aspect,
[280.34 → 284.04] which is great because I think I really got to see the field from its inception,
[284.04 → 286.24] which is not something you see every day.
[286.70 → 289.68] Yeah, it's been a pretty quick ride, I guess.
[289.84 → 293.66] So you're saying like 2015 was around the time that, you know,
[293.72 → 298.12] Ian Goodfellow came out with a paper and that stuff kind of started getting momentum.
[298.12 → 298.66] Is that right?
[298.80 → 299.00] Yeah.
[299.12 → 302.98] So I think the original paper was presented at then Nips 2014.
[303.38 → 308.16] And then I think, you know, then you saw like a slow trickle of papers,
[308.16 → 313.42] which kind of eventually turned into like an avalanche by like 2016, 2017.
[314.22 → 318.08] So Vlad, I was wondering if you could give us a little intro about yourself as well.
[318.28 → 318.80] Yeah, totally.
[319.20 → 320.66] I studied computer science.
[320.86 → 325.72] So machine learning was always one of my interests, both personally and professionally.
[325.72 → 330.92] And after college, after a brief stint at a Y Combinator startup,
[331.08 → 333.46] where I worked as a data scientist, I joined Microsoft.
[334.48 → 337.72] And Microsoft has an arm called Microsoft Research,
[338.04 → 340.88] which is essentially it's like an R&D division.
[341.10 → 343.90] It's effectively the Bell Labs of our time.
[343.90 → 350.52] And then I got involved with a research project where we used GANs along with my team.
[351.22 → 356.92] And it was just fascinating to see the margin by which data generative tasks,
[357.18 → 362.62] this technique has exceeded everything else that used to be the state of the art.
[362.62 → 368.06] So it was truly this like stepwise improvement that is rarely seen in,
[368.36 → 370.54] or it used to be rarely seen in machine learning.
[370.92 → 373.28] And from there, I stayed involved in the field.
[373.84 → 378.82] And now are you working, you know, in a practical sense, day to day with this technology?
[379.26 → 380.40] A little bit here and there.
[380.58 → 386.42] Although I must say that when it comes to practical applications of best measures of machine learning
[386.42 → 391.16] and deep learning techniques, it's still very much in the supervised machine learning area.
[391.16 → 393.70] And less on generative tasks.
[393.88 → 398.92] So when it comes to my day-to-day job, then GANs are almost no involvement.
[399.56 → 400.18] Gotcha. Yeah.
[400.64 → 404.28] And maybe we can get into some of those practicalities a little bit later.
[404.52 → 411.28] But to kick things off into GAN world, and I'll let you guys choose who wants to take on certain questions,
[411.28 → 415.80] but maybe one of you could just give us a brief, like what makes a GAN?
[415.80 → 422.58] How is it different from what we might think of when we think of a quote-unquote normal neural network
[422.58 → 426.52] or a, you know, normal machine learning model, whatever that is?
[427.18 → 428.56] Sure, I could give that a whirl.
[428.86 → 435.52] So I think the two areas that I would highlight is that, first, from like very high level,
[436.00 → 440.72] GANs generally live in the unsupervised world, which Vlad alluded to already,
[440.86 → 444.30] that there's this distinction between supervised and unsupervised.
[444.30 → 449.52] So most GANs exist in a world where you don't actually need any training labels,
[449.88 → 451.72] which is where the supervision comes in.
[452.00 → 457.74] Rather, the most generative models learn from the data itself.
[458.08 → 461.82] So all it needs is just raw data, and it manages to reconstruct it.
[462.28 → 465.62] So, you know, the prototypical example being human faces,
[465.98 → 470.08] and just by feeding GAN a bunch of human faces,
[470.08 → 477.10] it will eventually learn to reconstruct completely novel faces that are not in the original training set.
[477.64 → 481.44] So that's, I think, idea number one is that it's unsupervised.
[482.06 → 487.58] And then idea number two is, so the model itself effectively uses,
[487.80 → 491.92] most of the time, two neural networks that compete against each other,
[492.00 → 495.16] one being called the generator, one being called the discriminator.
[495.16 → 499.02] And the generator is almost like an amateur painter or something like that.
[499.12 → 503.02] And it tries to basically take some inspiration, generate a new image.
[503.68 → 506.22] And then the discriminator is like an art critic who says,
[506.54 → 508.86] you know, this is a good picture or this is not a good picture.
[509.34 → 511.42] And through the back and forth process,
[511.62 → 516.80] they both get better over time at generating and then telling apart real from fake.
[517.14 → 522.70] So at the end, you can have a generator that's pretty good at producing realistic images.
[522.70 → 526.00] So that's kind of like the high level summary.
[526.62 → 527.82] Anything to add, Vlad?
[528.28 → 528.86] Yeah, totally.
[529.02 → 531.52] I think it's a great intuitive description.
[531.72 → 537.16] I would just add some of the technical details in which GANs differ from traditional neural networks.
[537.72 → 540.12] And a core of it is the training procedure,
[540.40 → 544.04] where a traditional neural network is effective in optimization.
[544.42 → 550.48] You have a very complex loss space in which you are trying to minimize some loss function,
[550.58 → 551.38] which is the objective.
[551.38 → 557.68] So essentially, there is some measure of an error or how far the neural network is from its objective.
[558.20 → 563.54] And then the training procedure just uses calculus to minimize that objective.
[563.90 → 566.52] With GANs, since there are two neural networks,
[567.30 → 572.88] the training process can be better described as a game rather than an optimization,
[573.26 → 578.62] which has far-reaching implications on the training process itself and as the outcome of the network.
[578.62 → 586.16] So yeah, in this game, and maybe this is related to Jacob's discussion of being unsupervised as well,
[586.58 → 591.74] is the idea that you have these, let's take the faces example.
[591.88 → 595.06] So you have real faces or real pictures of faces.
[595.06 → 600.70] And essentially, those are kind of labelled in the sense that those are real faces.
[601.02 → 606.44] And then anything that comes out of a generator model trying to generate real faces,
[606.44 → 613.16] or trying to generate realistic faces, those are kind of automatically labelled as fake.
[613.16 → 618.52] So there's kind of this fact that, you know, everything you pump in is real.
[618.86 → 620.28] Yeah, absolutely.
[620.62 → 625.46] So this is actually, there is an active debate among researchers in classifying GANs,
[625.72 → 628.50] because when it comes to the training process,
[629.08 → 633.06] then exactly as you alluded to, they can be seen as a supervised machine learning,
[633.06 → 637.54] because you do have implied labels in real or fake.
[637.54 → 641.44] And there are also some GAN models that actually have explicit labels as well.
[641.44 → 646.18] But even the traditional core GAN, there are implied labels.
[646.72 → 649.46] However, when it comes to the training setup,
[649.64 → 652.30] then a more correct description is unsupervised,
[652.40 → 656.78] because there is no need for humans to instinctively label this data.
[657.54 → 662.88] So usually the bottleneck in machine learning is access to a large data set with labels.
[662.88 → 670.32] And GANs and the GAN paradigm helps to solve for that problem by essentially having the labels implied.
[670.68 → 676.50] There is no need for a human to go image by image and label which one is fake and which one isn't,
[676.86 → 680.96] because that comes from the very nature of the setup of the GAN model.
[681.38 → 683.32] When we look at it from a practical standpoint,
[683.52 → 686.86] then they can be seen as an unsupervised model.
[687.52 → 690.94] Although when we look at the particulars of the training process,
[690.94 → 695.38] then we are measuring a distance to an explicit label.
[695.38 → 700.52] So from that standpoint, the training can be seen as supervised in a way.
[701.24 → 706.56] So they are definitely in this gray area between, you know, supervised, unsupervised.
[706.78 → 709.32] And the Google researcher, François Chollet,
[709.40 → 713.40] who developed the CRUS Python programming deep learning library,
[713.90 → 717.34] he refers to some techniques like this as self-supervised as well.
[717.34 → 721.34] So you mentioned that there's these two models that are involved,
[721.44 → 725.42] and it makes sense to me kind of now what you're talking about in terms of unsupervised
[725.42 → 727.30] and how to think about that.
[727.84 → 730.64] I guess maybe in training each of those models,
[730.74 → 736.76] does each one still have the idea of loss in terms of what it's trying to generate?
[737.08 → 739.12] Or are they completely different?
[739.76 → 742.74] You know, the training of each model individual,
[743.34 → 745.40] is it completely different in some way?
[745.40 → 749.88] Well, I was just not 100% sure that I understand the question.
[750.20 → 754.46] But obviously, the two networks have different inputs, right?
[754.62 → 759.16] So for one of them, it is the latent vector, right?
[759.26 → 761.86] So one of them is just kind of like some sort of ran,
[761.98 → 769.52] typically a random sample from somewhere between like 100 and 500 dimensional vectors.
[769.52 → 775.04] And then it's just like the same way that any latent space would be.
[775.12 → 780.12] For those who are familiar, it's kind of relatively meaningless vector,
[780.40 → 785.00] though there are some qualifications to what you mean by meaningless specifically in this case.
[785.38 → 787.62] But it's just a vector of random numbers,
[787.62 → 796.74] and then uses a process to basically get to transpose convolutions or convolutions to size of the image, right?
[796.80 → 800.00] So it reshapes that vector through learned transformations,
[800.54 → 803.92] something that looks like an image ideally coming from, you know,
[803.98 → 806.24] the data, original data distribution.
[806.24 → 810.32] And so of course, like that is how you, you know, evaluate it as well.
[810.66 → 813.82] And the way that it gets the feedback is through the discriminator,
[813.98 → 816.48] which then tries to effectively, like we discussed,
[816.86 → 820.12] label images that the generator produces, right?
[820.26 → 825.10] And every time the generator manages to fool the discriminator,
[825.38 → 829.12] it gets a lower penalty than the discriminator who gets penalized more,
[829.48 → 831.12] because it got something wrong.
[831.12 → 835.26] So it's this iterative process, but of course, like they're,
[835.40 → 837.98] you know, in the original formulation, like Vlad lead to,
[838.36 → 840.02] it could be thought of as a game.
[840.72 → 845.28] So the two networks are basically set directly against each other.
[845.42 → 846.56] It's a zero-sum game, right?
[846.60 → 848.50] One has to lose in order for the other one to win.
[849.28 → 853.58] But it turns out that even that works relatively well.
[853.58 → 858.12] But in practice, people use more complicated loss functions
[858.12 → 861.28] that just have better like numerical properties.
[861.64 → 866.56] But the original formulation kind of gave it some solid theoretical grounding.
[866.56 → 870.02] So people were sort of more willing to accept why that works
[870.02 → 872.74] and then just kind of use these numerical tricks
[872.74 → 876.70] to make the training more stable or give it some other nice properties.
[876.70 → 879.36] And we can talk about some of the more advanced variants later.
[879.48 → 881.82] But that's basically what the generator is doing.
[881.82 → 887.02] And then the discriminator is basically just the classificational algorithm, right?
[887.02 → 891.42] So, you know, you can think of it as a real or fake detector like we discussed.
[891.80 → 896.10] So the training process there is more natural to what most people are used to thinking.
[896.80 → 900.66] So I guess, could we turn to maybe a couple of examples
[900.66 → 904.62] and talk a little bit about, you know, what makes GANs kind of useful
[904.62 → 906.90] or interesting for certain tasks?
[907.36 → 911.68] And what are kind of the range of tasks that you could use them on?
[911.68 → 915.68] And kind of if you could maybe throw out a couple of different examples
[915.68 → 920.92] about how GANs would be implemented to solve a particular problem
[920.92 → 925.56] more conceptually and stuff to give people a sense of how to fit this concept
[925.56 → 928.22] into their thinking as they're learning this topic.
[928.46 → 928.80] Absolutely.
[929.08 → 934.04] So GANs are, as their name suggests, generative adversarial networks.
[934.04 → 939.90] They are well suited to generative tasks, which is where you generate synthetic,
[940.30 → 942.40] yet realistic looking piece of data.
[943.26 → 947.44] And GANs have been particularly well suited to generating fake imagery.
[948.24 → 952.56] So you may have seen in media that there are fake images of human faces
[952.56 → 955.72] that are at a photorealistic quality,
[956.38 → 962.58] or even fake videos of statements by famous people that were never made.
[962.58 → 966.60] And yet the video footage looks as if a Hollywood studio made it.
[967.66 → 972.00] But it is something that researchers were just able to produce using this technique.
[972.80 → 977.96] And a great way to think about it is in contrast to what machines used to be good at
[977.96 → 979.90] until GANs came along.
[980.66 → 983.98] So machine learning and later on deep learning
[983.98 → 989.50] is excellent at uncovering patterns in existing data
[989.50 → 994.84] and then using that insight to unsupervised machine learning tasks,
[994.92 → 996.92] such as regression or classification.
[997.88 → 1001.54] So for instance, there has been huge advances in machines
[1001.54 → 1004.00] that were taking an image as an input
[1004.00 → 1007.40] and then categorizing it to the correct label.
[1007.52 → 1010.28] So you have an image and then the machine tells you it's a dog.
[1010.38 → 1012.38] Or you have another image, and it tells you it's a cat.
[1012.38 → 1015.32] What used to be extremely difficult
[1015.32 → 1017.92] until Ian Goodfellow came along with this innovation
[1017.92 → 1020.68] was doing the reverse of this process.
[1020.90 → 1023.80] Essentially, taking the label dog,
[1024.56 → 1025.94] feeding it into a neural network
[1025.94 → 1029.24] and having an image of a dog being produced at the end of it.
[1029.78 → 1033.00] I mean, this is overly simplifying it,
[1033.12 → 1035.06] especially when it comes to internal workings of it.
[1035.40 → 1036.78] But conceptually, it's essentially
[1036.78 → 1040.14] instead of having a computer classifying something,
[1040.26 → 1041.96] it's having a computer create something.
[1041.96 → 1044.32] So it's a philosophically,
[1044.44 → 1047.58] it's like a level of imagination or creativity
[1047.58 → 1049.66] that the machine would have.
[1050.20 → 1051.88] Yeah, this has been something
[1051.88 → 1053.70] that was extremely difficult to do
[1053.70 → 1056.54] because it's extremely hard for a human
[1056.54 → 1061.58] to define what a realistic image of a dog is.
[1061.72 → 1065.08] And it's also extremely difficult to capture mathematically.
[1066.00 → 1068.24] So the other generative tasks
[1068.24 → 1071.14] that are other generative models that came before GANs,
[1071.14 → 1074.70] they were usually trained by recreating the same image
[1074.70 → 1075.62] that it was fed in.
[1075.62 → 1078.68] That's essentially like taking an image,
[1079.10 → 1080.50] compressing it into a representation
[1080.50 → 1082.94] and then recreating the image itself.
[1083.96 → 1087.42] And then you can tweak the internal representation
[1087.42 → 1089.50] to produce a fake image
[1089.50 → 1092.02] that is somewhat similar to the original one.
[1092.02 → 1094.70] What GANs were able to do is that
[1094.70 → 1099.20] the generator itself is not learning explicitly
[1099.20 → 1102.50] by something that a human programmer would define
[1102.50 → 1104.28] or a researcher would define.
[1104.40 → 1107.36] There is no explicit loss function for the generator.
[1107.96 → 1110.86] What is happening is that we have another neural network,
[1110.98 → 1112.74] which is the simple classifier,
[1113.28 → 1114.68] which is the discriminator,
[1115.06 → 1117.88] that helps the generator generate something
[1117.88 → 1118.84] that looks realistic.
[1118.84 → 1122.56] So effectively, we have another model
[1122.56 → 1125.52] that helps us do the teaching.
[1126.46 → 1129.12] And what's really fascinating is that
[1129.12 → 1131.52] what Ian Goodfellow accomplished
[1131.52 → 1134.32] is taking something that machines used to be,
[1134.58 → 1135.90] our good at,
[1136.06 → 1137.08] which is classification,
[1137.72 → 1137.84] right?
[1137.92 → 1140.64] Like taking an image and saying it's real or fake.
[1140.64 → 1143.34] And using that insight
[1143.34 → 1146.18] to help machines achieve something
[1146.18 → 1148.44] that used to be very difficult for them,
[1148.50 → 1150.18] which is generating realistic data.
[1151.18 → 1153.92] So maybe to just quickly add on to that,
[1154.04 → 1157.30] I think in terms of your original question,
[1157.58 → 1159.72] right, like around the application side of things,
[1160.12 → 1162.74] my perhaps slightly sort of less,
[1162.92 → 1163.52] you know, something like,
[1163.68 → 1165.10] I guess this is an informal podcast.
[1165.10 → 1166.84] So some researchers I know
[1166.84 → 1168.00] would probably object to this,
[1168.26 → 1168.82] but...
[1168.82 → 1169.70] All is safe here.
[1170.10 → 1170.74] Yeah, exactly.
[1171.12 → 1172.66] So I think it's a reasonable,
[1172.66 → 1173.58] like, approximation
[1173.58 → 1174.88] to how to think about GANs,
[1174.92 → 1175.78] is to think as the
[1175.94 → 1177.86] like, basically first learned
[1177.86 → 1180.58] general purpose generative framework,
[1180.82 → 1181.06] right?
[1181.28 → 1183.50] So GANs have been sort of applied,
[1183.64 → 1184.54] as we discussed,
[1184.62 → 1185.70] in images and video,
[1185.90 → 1187.66] but also people might not know
[1187.66 → 1189.08] that they have been successfully applied
[1189.08 → 1189.92] in, like, tabular
[1189.92 → 1191.16] and highly structured data,
[1191.54 → 1192.64] natural language processing,
[1192.84 → 1193.28] audio,
[1193.28 → 1196.58] I've seen papers in network theory
[1196.58 → 1198.00] and graph applications,
[1198.34 → 1200.12] obviously lots of artistic applications,
[1200.54 → 1200.70] you know,
[1200.76 → 1201.76] even some defences
[1201.76 → 1203.20] against adversarial examples,
[1203.38 → 1203.56] though,
[1203.70 → 1205.84] that is still far from being a solved problem.
[1206.26 → 1207.22] So obviously,
[1207.54 → 1208.82] GANs have had, like,
[1209.06 → 1210.60] sort of managed to replicate
[1210.60 → 1212.16] so much interesting data,
[1212.52 → 1213.56] but in terms of, like,
[1213.58 → 1214.82] the business applications,
[1215.32 → 1217.02] they tend to be non-trivial, right?
[1217.08 → 1219.18] Like, you need to really think,
[1219.66 → 1221.94] where does this technique make sense?
[1221.94 → 1224.76] It can be extremely powerful,
[1225.66 → 1226.04] and, you know,
[1226.12 → 1227.72] unlike with classifications
[1227.72 → 1229.36] and sort of decision theory
[1229.36 → 1230.16] and things like that,
[1230.40 → 1231.90] we have not had the ability
[1231.90 → 1233.54] to recreate, you know,
[1233.64 → 1235.48] realistic data for that long.
[1235.74 → 1237.76] So it is not always
[1237.76 → 1239.58] immediately obvious
[1239.58 → 1241.16] to how to, you know,
[1241.16 → 1242.54] apply it in a business process
[1242.54 → 1243.52] or something like that.
[1243.62 → 1245.02] And the reality is that
[1245.02 → 1246.30] this is a technology
[1246.30 → 1247.04] that's, like,
[1247.40 → 1248.94] literally four or five years old.
[1248.94 → 1251.22] So I think it'll take a while
[1251.22 → 1252.20] till there will be, like,
[1252.24 → 1253.38] some sort of, you know,
[1253.56 → 1254.58] mass adoption.
[1255.24 → 1256.58] But I think there's lots
[1256.58 → 1257.50] of interesting things
[1257.50 → 1259.16] in the fact that you can apply
[1259.16 → 1260.68] this technique
[1260.68 → 1261.86] in all these different domains.
[1262.34 → 1263.36] But, you know,
[1263.40 → 1264.68] the applications of, like,
[1264.70 → 1265.56] how to use it,
[1265.82 → 1266.82] you know, sometimes will be...
[1267.46 → 1268.80] I think one of the earliest
[1268.80 → 1269.84] practical applications
[1269.84 → 1270.62] I remember was
[1270.62 → 1271.88] in something in dentistry,
[1272.38 → 1274.20] where people try to actually propose,
[1274.36 → 1275.10] which is another area
[1275.10 → 1276.30] that I haven't even mentioned,
[1276.62 → 1277.16] propose, like,
[1277.16 → 1280.18] a 3D mesh of the crown,
[1280.30 → 1280.58] I think,
[1280.62 → 1281.56] that they were trying to fix.
[1281.74 → 1282.20] So basically,
[1282.30 → 1284.04] to create artificial crown
[1284.04 → 1285.94] that would fit into
[1285.94 → 1286.86] the patient's mouth
[1286.86 → 1288.34] and then with the rest
[1288.34 → 1288.84] of the teeth
[1288.84 → 1290.62] using GANS
[1290.62 → 1291.82] in the 3D space.
[1292.66 → 1294.10] I'm not sure...
[1294.10 → 1295.16] When I was doing research
[1295.16 → 1295.54] on this,
[1295.60 → 1296.62] I'm not sure how far
[1296.62 → 1297.54] it actually went
[1297.54 → 1299.16] because there was a lot of,
[1299.28 → 1301.02] like, I think 2016, 2017,
[1301.18 → 1302.76] there was a lot of talk
[1302.76 → 1303.82] about it.
[1303.90 → 1304.96] And people, like,
[1304.98 → 1306.38] love to mention that example,
[1306.38 → 1307.52] but I have not seen
[1307.52 → 1308.72] that much follow-up.
[1308.92 → 1310.44] So I'm not 100% sure
[1310.44 → 1311.46] what happened there.
[1311.74 → 1313.04] But, you know,
[1313.08 → 1313.88] there's definitely lots
[1313.88 → 1315.26] of fascinating applications.
[1315.84 → 1316.92] You just need to think about,
[1317.02 → 1317.18] like,
[1317.20 → 1317.90] how do I use
[1317.90 → 1319.34] this strength, right?
[1319.62 → 1320.46] Rather than, like,
[1320.52 → 1322.22] very obviously applying it
[1322.22 → 1324.00] to some sort of
[1324.00 → 1325.12] business process
[1325.12 → 1326.18] where you have, like,
[1326.38 → 1327.14] okay, you know,
[1327.14 → 1328.42] I need to make a decision here.
[1328.50 → 1329.26] I'll just train a
[1329.26 → 1330.28] deep neural network
[1330.28 → 1331.24] to do that instead.
[1331.72 → 1332.74] So I've noticed
[1332.74 → 1333.58] over the course
[1333.58 → 1334.34] of the conversation
[1334.34 → 1336.20] that we have actually mentioned,
[1336.34 → 1337.78] we've referenced Ian Goodfellow
[1337.78 → 1339.02] half a dozen times.
[1339.34 → 1340.14] And I thought it might,
[1340.24 → 1341.26] it might be worthwhile
[1341.26 → 1343.12] to ask you guys
[1343.12 → 1343.94] if you could just kind of
[1343.94 → 1344.78] tell us
[1344.78 → 1346.06] who Ian Goodfellow is.
[1346.12 → 1346.46] Obviously,
[1346.62 → 1348.56] he's a pretty big deal
[1348.56 → 1349.38] in this industry.
[1349.68 → 1350.66] And with you guys
[1350.66 → 1351.30] working on GANS,
[1351.38 → 1351.96] if you just kind of
[1351.96 → 1352.98] give us a little bit
[1352.98 → 1353.80] of a background
[1353.80 → 1354.64] on who he is
[1354.64 → 1355.40] and what he did
[1355.40 → 1356.22] and why it's significant
[1356.22 → 1357.04] to the conversation.
[1357.68 → 1357.88] Yeah.
[1357.88 → 1358.92] So Ian,
[1360.34 → 1361.36] why it's so important
[1361.36 → 1362.06] is that,
[1362.12 → 1362.26] you know,
[1362.30 → 1363.28] he's the single person
[1363.28 → 1364.38] who invented this technique.
[1364.56 → 1364.82] Of course,
[1364.88 → 1366.06] there were other,
[1366.24 → 1367.02] his colleagues
[1367.02 → 1368.08] that are on the paper,
[1368.28 → 1369.10] but when it comes
[1369.10 → 1370.68] to receiving the credit
[1370.68 → 1371.56] for the invention
[1371.56 → 1373.24] of generative adversarial networks,
[1373.66 → 1374.06] it's him.
[1374.42 → 1376.16] He was a PhD student
[1376.16 → 1377.50] at the University of Montreal
[1377.50 → 1379.94] where in 2014
[1379.94 → 1381.38] at the end of the academic year,
[1381.44 → 1382.40] he went out drinking
[1382.40 → 1383.46] with some of his friends
[1383.46 → 1385.32] and they were discussing
[1385.32 → 1385.88] the
[1386.56 → 1388.94] some of what I alluded to
[1388.94 → 1389.72] at the beginning
[1389.72 → 1390.46] of this dialogue,
[1390.68 → 1391.66] how difficult it is
[1391.66 → 1392.96] to have machines
[1392.96 → 1394.14] synthesize
[1394.14 → 1395.36] photorealistic imagery,
[1395.98 → 1397.04] which used to be,
[1397.24 → 1398.40] like from a research standpoint,
[1398.66 → 1400.00] an intractable problem.
[1400.96 → 1402.74] And Ian came up
[1402.74 → 1404.32] with the idea
[1404.32 → 1405.46] of the two dual-linked
[1405.46 → 1406.18] neural networks,
[1406.86 → 1407.74] which he then,
[1407.92 → 1408.84] after returning home
[1408.84 → 1409.48] from the pub,
[1409.90 → 1410.42] coded up.
[1411.24 → 1412.80] And later that year,
[1412.80 → 1414.16] he and his colleagues
[1414.16 → 1415.44] have published the paper
[1415.44 → 1417.52] that truly started this field.
[1417.62 → 1418.42] And then, of course,
[1418.82 → 1420.70] there was the research community
[1420.70 → 1421.44] that took it up
[1421.44 → 1422.82] and there were,
[1422.98 → 1423.52] since then,
[1423.64 → 1424.90] huge innovations made
[1424.90 → 1427.96] both on the original GAN model,
[1428.32 → 1429.06] both when it came
[1429.06 → 1429.78] to the complexity
[1429.78 → 1432.28] of the model itself
[1432.28 → 1433.70] and its application,
[1433.92 → 1434.78] the use of labels
[1434.78 → 1435.62] during the training,
[1435.80 → 1436.48] both the generator,
[1436.62 → 1437.38] discriminator,
[1437.76 → 1438.82] or one of those.
[1438.98 → 1439.82] So the field
[1439.82 → 1441.34] has advanced considerably
[1441.34 → 1443.66] in just the few short years
[1443.66 → 1445.14] that it has been around.
[1446.20 → 1447.36] But Ian, again,
[1447.46 → 1448.30] he is so prominent
[1448.30 → 1449.48] because he's credited
[1449.48 → 1451.34] with his invention.
[1452.34 → 1452.84] Yeah, I think,
[1452.96 → 1453.92] and just to note,
[1454.14 → 1454.84] we're often asked
[1454.84 → 1455.76] about learning resources.
[1456.04 → 1457.00] He is one of the
[1457.00 → 1458.02] three primary authors
[1458.02 → 1459.64] of the Deep Learning textbook,
[1460.00 → 1461.06] which we have referenced
[1461.06 → 1462.50] on this show many times.
[1463.06 → 1464.22] And though he has worked
[1464.22 → 1465.84] for various organizations
[1465.84 → 1466.48] in the past,
[1466.54 → 1467.38] I believe he's currently
[1467.38 → 1468.88] with Apple at this point.
[1468.88 → 1469.60] Yeah, that's correct.
[1469.76 → 1470.80] Yeah, he was at Google,
[1470.96 → 1471.54] OpenAI,
[1471.86 → 1473.24] and now most recently
[1473.24 → 1474.20] he joined Apple,
[1474.38 → 1475.68] which I'm very excited
[1475.68 → 1476.56] to see what we will
[1476.56 → 1477.16] come up with
[1477.16 → 1479.36] because I'm fairly certain
[1479.36 → 1481.22] that the technology
[1481.22 → 1482.20] that is powering
[1482.20 → 1483.16] the emoji
[1483.16 → 1485.06] that you can manipulate
[1485.06 → 1486.00] with your face
[1486.00 → 1487.44] on like with an iMessage,
[1487.94 → 1489.02] the underlying technology
[1489.02 → 1490.32] for that would be GANs.
[1490.92 → 1492.14] So when we have seen
[1492.14 → 1493.14] a lot of the flashy
[1493.14 → 1493.96] applications
[1493.96 → 1495.94] of creative image
[1495.94 → 1496.82] processing
[1496.82 → 1497.70] and image editing,
[1498.20 → 1498.98] like the applications
[1498.98 → 1500.60] that make you look older,
[1501.38 → 1502.68] like the Face app
[1502.68 → 1504.26] or the applications
[1504.26 → 1505.32] that make you look younger,
[1505.46 → 1506.44] like the baby filter
[1506.44 → 1507.06] on Snapchat,
[1507.90 → 1509.16] tend to have GANs
[1509.16 → 1510.54] as the underlying technology.
[1511.58 → 1512.42] There are also
[1512.42 → 1514.22] other photo editing
[1514.22 → 1515.36] pieces of software
[1515.36 → 1516.30] that have
[1516.30 → 1517.90] very advanced features
[1517.90 → 1518.70] that are also
[1518.70 → 1519.84] using GANs
[1519.84 → 1521.08] as the underlying technology.
[1521.56 → 1522.00] So when it comes
[1522.00 → 1523.08] to creative applications,
[1523.36 → 1523.84] when it comes
[1523.84 → 1525.30] to like the immediate,
[1525.44 → 1526.14] like the commercial
[1526.14 → 1526.94] use cases,
[1527.10 → 1528.32] then image editing
[1528.32 → 1529.54] is where GANs have shined.
[1529.90 → 1530.56] But I think
[1530.56 → 1531.48] that's only scratching
[1531.48 → 1532.02] the surface
[1532.02 → 1533.52] of what will be
[1533.52 → 1534.56] ultimately possible
[1534.56 → 1536.50] with GANs in particular
[1536.50 → 1538.00] and also the research
[1538.00 → 1538.54] directions
[1538.54 → 1540.00] that this technique
[1540.00 → 1540.78] has opened up.
[1541.36 → 1542.82] So to kind of summarize
[1542.82 → 1544.00] and I'll make an attempt
[1544.00 → 1544.46] at this
[1544.46 → 1545.46] and you can tell me
[1545.46 → 1546.54] if it's a good summary,
[1546.68 → 1547.62] but to kind of summarize,
[1547.82 → 1548.58] it seems like
[1548.58 → 1549.76] that GANs
[1549.76 → 1550.96] as opposed to other
[1550.96 → 1552.10] kind of quote unquote
[1552.10 → 1552.92] normal models
[1552.92 → 1553.86] that people might
[1553.86 → 1555.10] envision
[1555.10 → 1556.52] is that there's actually
[1556.52 → 1557.32] two models,
[1557.48 → 1558.00] the generator
[1558.00 → 1559.04] and the discriminator
[1559.04 → 1560.66] and they feed back
[1560.66 → 1561.76] to one another's
[1561.76 → 1563.42] and one is trying
[1563.42 → 1564.58] to generate something,
[1564.88 → 1566.04] whatever that might be
[1566.04 → 1568.30] based on some randomness
[1568.30 → 1569.66] and then one
[1569.66 → 1570.70] is trying
[1570.70 → 1571.42] to differentiate
[1571.42 → 1572.58] between the generated
[1572.58 → 1572.98] version
[1572.98 → 1574.92] and some gold standard
[1574.92 → 1576.62] or real version.
[1577.02 → 1577.52] Would that be
[1577.52 → 1578.40] a good overall summary?
[1579.04 → 1579.14] Yeah,
[1579.20 → 1579.68] functionally,
[1579.72 → 1579.98] yes.
[1580.84 → 1581.38] Okay.
[1581.38 → 1582.60] And I was wondering
[1582.60 → 1583.84] like for those
[1583.84 → 1584.52] two models,
[1584.52 → 1585.50] I guess I had
[1585.50 → 1586.32] a couple questions,
[1586.42 → 1587.36] but one of them is
[1587.36 → 1587.80] like,
[1587.82 → 1588.52] let's say we take
[1588.52 → 1589.66] the example of the faces
[1589.66 → 1590.96] or something like that
[1590.96 → 1592.52] in terms of the mechanism
[1592.52 → 1594.50] feedback between the two.
[1594.64 → 1596.16] Is it that like
[1596.16 → 1597.82] when you are generating
[1597.82 → 1598.36] things,
[1598.36 → 1599.16] you generate like
[1599.16 → 1600.46] a bunch of,
[1600.46 → 1601.38] you know,
[1601.48 → 1602.30] fake faces
[1602.30 → 1603.74] to mix in
[1603.74 → 1604.76] with the real faces
[1604.76 → 1606.38] and then try to,
[1606.46 → 1607.02] you know,
[1607.06 → 1608.26] discriminate with
[1608.26 → 1610.12] the classifier model
[1610.12 → 1611.20] or retrain
[1611.20 → 1612.16] or update it
[1612.16 → 1613.24] or is it a sort of
[1613.24 → 1614.16] one at a time thing
[1614.16 → 1614.92] like you generate
[1614.92 → 1615.76] one face
[1615.76 → 1616.80] and then add that in?
[1617.26 → 1618.06] What's the sort of
[1618.06 → 1619.16] balance that happens there
[1619.16 → 1619.90] and the considerations
[1619.90 → 1620.72] you have to take
[1620.72 → 1621.60] into account?
[1622.34 → 1622.78] So,
[1622.90 → 1624.00] if I get your question
[1624.00 → 1624.48] correctly,
[1624.58 → 1625.18] I think it's about
[1625.18 → 1625.78] the training
[1625.78 → 1626.52] and how,
[1626.76 → 1627.08] you know,
[1627.12 → 1628.24] how to balance
[1628.24 → 1629.10] the two networks
[1629.10 → 1630.10] learning regime.
[1630.54 → 1631.04] And I think,
[1631.12 → 1631.44] you know,
[1631.50 → 1632.10] you kind of hit
[1632.10 → 1632.88] the nail on the head
[1632.88 → 1633.60] here because
[1633.60 → 1634.82] that tends to be
[1634.82 → 1635.48] one of the most
[1635.48 → 1637.00] challenging aspects
[1637.00 → 1637.62] of GANs
[1637.62 → 1638.56] is the training part
[1638.56 → 1640.08] because even though
[1640.08 → 1640.74] it might sometimes
[1640.74 → 1641.52] seem like magic,
[1641.52 → 1642.24] it's obviously,
[1642.46 → 1643.04] you know,
[1643.08 → 1643.84] driven by,
[1643.96 → 1644.26] you know,
[1644.26 → 1645.26] real algorithms.
[1645.68 → 1645.84] So,
[1646.22 → 1647.38] to nail that dynamic
[1647.38 → 1648.42] can be very challenging
[1648.42 → 1649.28] and,
[1649.36 → 1649.84] you know,
[1650.08 → 1652.08] in my day-to-day work
[1652.08 → 1652.42] or,
[1652.80 → 1652.98] you know,
[1653.04 → 1654.32] even over the course
[1654.32 → 1654.86] of just like
[1654.86 → 1655.62] playing around
[1655.62 → 1657.34] with new research papers
[1657.34 → 1658.08] and their code,
[1658.56 → 1659.90] that tends to be
[1659.90 → 1660.92] one of the biggest challenges.
[1661.62 → 1662.64] People have proposed,
[1662.96 → 1663.24] you know,
[1663.34 → 1663.72] literally,
[1664.14 → 1664.98] I don't think
[1664.98 → 1665.98] it's an exaggeration,
[1665.98 → 1666.58] there's literally
[1666.58 → 1667.46] hundreds of papers
[1667.46 → 1668.40] if not thousands
[1668.40 → 1670.12] written on just
[1670.12 → 1671.54] the training dynamic
[1671.54 → 1672.14] alone.
[1672.64 → 1673.56] And it's obviously
[1673.56 → 1675.16] like quite a bit
[1675.16 → 1675.72] of challenge
[1675.72 → 1676.68] to get that
[1676.68 → 1677.46] exactly right.
[1678.18 → 1679.12] There's like
[1679.12 → 1680.28] techniques
[1680.28 → 1681.68] that keep on
[1681.68 → 1682.32] popping up
[1682.32 → 1683.36] over and over again.
[1683.50 → 1683.94] People in,
[1684.14 → 1684.34] and,
[1684.50 → 1684.60] you know,
[1684.64 → 1685.16] many of those
[1685.16 → 1685.60] would be like
[1685.60 → 1686.56] covered in the book,
[1686.70 → 1687.60] but to feel this
[1687.60 → 1688.38] ever evolving,
[1688.60 → 1688.82] right,
[1688.94 → 1689.30] it's,
[1689.44 → 1690.46] there are new things
[1690.46 → 1691.16] coming out,
[1691.34 → 1691.60] you know,
[1691.64 → 1693.04] every major conference
[1693.04 → 1693.78] there is like
[1693.78 → 1694.28] at least,
[1694.40 → 1694.66] you know,
[1694.66 → 1696.14] five to ten
[1696.14 → 1697.16] like new proposals
[1697.16 → 1698.16] on how to improve
[1698.16 → 1699.16] this training dynamic.
[1699.70 → 1700.38] And some of them
[1700.38 → 1700.98] take off
[1700.98 → 1701.20] and,
[1701.28 → 1701.78] you know,
[1702.18 → 1703.18] start to be incorporated
[1703.18 → 1704.18] by more papers.
[1704.38 → 1705.72] Others sort of
[1705.72 → 1707.30] may have been good,
[1707.38 → 1708.72] but like fade into obscurity
[1708.72 → 1709.70] through some like,
[1710.06 → 1710.28] you know,
[1710.38 → 1712.18] the pseudo random process
[1712.18 → 1713.94] of academic discovery.
[1714.28 → 1715.54] That's kind of my take on it.
[1715.98 → 1716.52] But yeah,
[1716.52 → 1717.50] I think in general,
[1717.60 → 1718.34] like I've,
[1718.34 → 1719.48] I've noticed that,
[1719.68 → 1720.18] you know,
[1720.22 → 1721.94] having a solid
[1721.94 → 1723.20] starting architecture,
[1723.20 → 1724.56] like close to something
[1724.56 → 1725.72] that you know has worked
[1725.72 → 1727.38] and look at the data set
[1727.38 → 1728.66] that you're applying it to
[1728.66 → 1729.42] because,
[1729.78 → 1729.88] you know,
[1729.94 → 1731.18] a lot of the academic work
[1731.18 → 1731.90] tends to work
[1731.90 → 1733.32] on fairly standard data sets.
[1733.46 → 1734.08] If you're applying it
[1734.08 → 1734.80] on something else,
[1735.30 → 1736.38] tends to be very different.
[1736.62 → 1736.80] So,
[1737.12 → 1737.96] you need to think about
[1737.96 → 1739.40] the data set as well
[1739.40 → 1740.26] as the network
[1740.26 → 1741.06] and the architecture,
[1741.54 → 1742.20] which I think
[1742.20 → 1744.12] just kind of talks about
[1744.12 → 1745.04] one of the differences
[1745.04 → 1745.82] between academia
[1745.82 → 1746.72] and industry,
[1747.18 → 1749.06] where the industry problems
[1749.06 → 1750.62] tend to revolve
[1750.62 → 1751.48] much more about
[1751.48 → 1752.48] the data set
[1752.48 → 1753.96] and thinking about
[1753.96 → 1754.72] the sort of,
[1754.88 → 1755.84] as Apart calls it,
[1755.88 → 1756.94] like the data programming.
[1758.26 → 1758.34] So,
[1758.54 → 1760.16] is this part of the reason
[1760.16 → 1761.26] maybe why,
[1761.76 → 1763.16] so Vlad mentioned that
[1763.16 → 1764.40] when he was giving
[1764.40 → 1765.44] his sort of introduction
[1765.44 → 1766.96] that there is still
[1766.96 → 1767.82] a bit of a struggle
[1767.82 → 1768.80] to kind of make
[1768.80 → 1769.46] the transition
[1769.46 → 1771.32] from GANs
[1771.32 → 1772.40] to their application
[1772.40 → 1773.84] in sort of
[1773.84 → 1774.52] day-to-day
[1774.52 → 1776.22] data science work
[1776.22 → 1777.58] in a widespread manner.
[1777.70 → 1778.08] Do you think
[1778.08 → 1778.74] most of that
[1778.74 → 1779.84] is because there is
[1779.84 → 1781.02] still a lot of
[1781.02 → 1782.34] fuzziness around
[1782.34 → 1783.26] the best way
[1783.26 → 1784.12] to approach
[1784.12 → 1785.24] training?
[1785.58 → 1785.74] Or,
[1785.86 → 1786.50] what do you think
[1786.50 → 1787.26] is factoring in there?
[1787.34 → 1788.34] What are some of the
[1788.80 → 1790.04] is that the main challenge
[1790.04 → 1791.02] or are there other things
[1791.02 → 1792.38] kind of preventing that?
[1792.82 → 1793.16] I mean,
[1793.26 → 1794.44] I personally think that
[1794.44 → 1795.14] there's quite
[1795.14 → 1796.28] a few challenges.
[1796.54 → 1797.10] I think training
[1797.10 → 1797.90] is definitely
[1797.90 → 1798.90] one of them,
[1798.98 → 1799.42] but I think
[1799.42 → 1800.18] realistically,
[1800.46 → 1800.70] I mean,
[1800.70 → 1801.66] even if you look at
[1801.66 → 1802.68] the state of our field
[1802.68 → 1803.26] more broadly,
[1803.46 → 1803.64] like,
[1803.64 → 1805.16] not that many companies
[1805.16 → 1806.08] are successfully
[1806.08 → 1807.64] deploying deep learning models
[1807.64 → 1808.88] even supervised
[1808.88 → 1810.14] on a regular basis.
[1810.74 → 1810.88] So,
[1811.06 → 1811.96] I think that,
[1812.30 → 1812.48] you know,
[1812.52 → 1812.88] obviously,
[1813.38 → 1813.96] the infrastructure
[1813.96 → 1814.96] and the support
[1814.96 → 1815.66] and the business
[1815.66 → 1816.28] thinking about
[1816.28 → 1817.78] the whole machine
[1817.78 → 1818.42] learning space
[1818.42 → 1819.06] is maturing,
[1819.56 → 1820.08] but I think,
[1820.50 → 1820.82] you know,
[1821.10 → 1821.68] generally,
[1822.02 → 1823.36] I think the reasons
[1823.36 → 1824.70] for why GANs
[1824.70 → 1825.70] have generally been
[1825.70 → 1827.00] applied mostly
[1827.00 → 1827.62] as like
[1827.62 → 1828.82] specialized startups
[1828.82 → 1829.60] or very specialized
[1829.60 → 1830.54] business units
[1830.54 → 1831.66] that have someone
[1831.66 → 1832.46] with a lot of
[1832.46 → 1833.32] GAN experience
[1833.32 → 1834.54] is for obviously
[1834.54 → 1835.72] the training difficulty,
[1835.72 → 1836.46] but also
[1836.46 → 1837.66] like having
[1837.66 → 1838.48] the right
[1838.48 → 1839.44] set of
[1839.44 → 1840.92] business
[1840.92 → 1841.62] sort of
[1841.62 → 1842.16] incentives
[1842.16 → 1842.80] or
[1842.80 → 1843.92] not even incentives,
[1844.08 → 1844.54] maybe more
[1844.54 → 1846.12] like intuitions
[1846.12 → 1847.64] around how to
[1847.64 → 1849.00] apply GANs
[1849.00 → 1849.66] successfully.
[1850.04 → 1850.86] I think there's
[1850.86 → 1851.36] a lot of
[1851.36 → 1851.66] really,
[1851.82 → 1852.66] perfect
[1852.66 → 1854.32] applications for them,
[1854.32 → 1855.90] but you generally
[1855.90 → 1856.56] need someone
[1856.56 → 1857.46] who can,
[1857.58 → 1858.28] you know,
[1858.44 → 1860.28] sort of tell you
[1860.28 → 1861.48] where that extra
[1861.48 → 1862.52] effort is worth it
[1862.52 → 1863.64] because it will be
[1863.64 → 1864.46] somewhat challenging
[1864.46 → 1865.62] because of the
[1865.62 → 1866.42] training dynamics
[1866.42 → 1867.32] and other things
[1867.32 → 1869.06] to deploy it.
[1869.10 → 1869.78] So I think you need
[1869.78 → 1870.58] to have someone
[1870.58 → 1871.80] who can like
[1871.80 → 1872.70] sort of guide you
[1872.70 → 1873.38] through what makes
[1873.38 → 1873.92] sense in this
[1873.92 → 1874.44] situation,
[1874.44 → 1875.74] but also like
[1875.74 → 1876.52] someone who can
[1876.52 → 1877.20] like pick out
[1877.20 → 1878.18] the right tool
[1878.18 → 1878.84] for the job.
[1879.02 → 1879.16] So,
[1879.54 → 1879.70] you know,
[1879.80 → 1880.62] even machine learning
[1880.62 → 1881.44] broadly is like
[1881.44 → 1882.34] still relatively
[1882.34 → 1883.22] novel,
[1883.46 → 1884.16] though to us
[1884.16 → 1884.60] it might not
[1884.60 → 1885.22] feel that way.
[1885.78 → 1886.98] And I think
[1886.98 → 1887.82] businesses are
[1887.82 → 1888.50] still trying to
[1888.50 → 1888.90] catch up.
[1889.56 → 1890.38] So I'm curious
[1890.38 → 1890.78] as,
[1891.00 → 1891.20] you know,
[1891.26 → 1891.78] as we've been
[1891.78 → 1892.78] talking about this
[1892.78 → 1893.80] and we've kind
[1893.80 → 1894.76] of gone into
[1894.76 → 1895.76] some depth
[1895.76 → 1896.66] about how
[1896.66 → 1897.34] generators and
[1897.34 → 1898.24] discriminators work
[1898.24 → 1898.94] and I'm wondering
[1898.94 → 1900.52] are there other
[1900.52 → 1901.34] models,
[1901.96 → 1902.26] you know,
[1902.34 → 1903.38] either other types
[1903.38 → 1903.92] of neural network
[1903.92 → 1904.90] models or other
[1904.90 → 1905.54] machine learning
[1905.54 → 1906.28] models outside
[1906.28 → 1906.78] the neural net
[1906.78 → 1907.40] space that you
[1907.40 → 1908.66] could use as a
[1908.66 → 1909.30] generator or
[1909.30 → 1909.86] discriminator?
[1910.62 → 1911.32] It's a great
[1911.32 → 1911.54] question.
[1911.68 → 1912.50] So the
[1912.50 → 1913.84] discriminator itself,
[1913.90 → 1914.38] if you actually
[1914.38 → 1915.64] isolate it from
[1915.64 → 1916.72] the GAN model,
[1917.24 → 1917.82] then that's just
[1917.82 → 1918.82] a classifier in
[1918.82 → 1919.52] most of the
[1919.52 → 1920.52] incarnations of
[1920.52 → 1921.20] the GAN
[1921.20 → 1921.72] architecture.
[1921.72 → 1922.76] So these are
[1922.76 → 1923.96] two separate
[1923.96 → 1924.92] neural networks
[1924.92 → 1925.32] that can
[1925.32 → 1925.90] effectively
[1925.90 → 1926.64] function
[1926.64 → 1927.28] independently.
[1927.60 → 1928.48] When it comes
[1928.48 → 1929.12] to generative
[1929.12 → 1929.76] tasks,
[1929.94 → 1930.66] then there have
[1930.66 → 1931.48] been other
[1931.48 → 1932.08] models that
[1932.08 → 1932.72] were used for
[1932.72 → 1933.30] that purpose.
[1933.92 → 1934.78] You have the
[1934.78 → 1935.50] image in
[1935.50 → 1935.96] particular,
[1936.18 → 1936.40] you have
[1936.40 → 1937.16] both restricted
[1937.16 → 1938.04] bolts machines
[1938.04 → 1939.20] and auto
[1939.20 → 1940.54] encoders that
[1940.54 → 1941.14] were used for
[1941.14 → 1941.76] this purpose.
[1942.36 → 1943.00] But when it
[1943.00 → 1943.74] comes to
[1943.74 → 1944.98] image generation,
[1945.42 → 1945.78] and this
[1945.78 → 1946.86] applies to
[1946.86 → 1947.88] both static
[1947.88 → 1948.60] imagery like
[1948.60 → 1949.60] photos or
[1949.60 → 1950.90] to video
[1950.90 → 1951.38] footage,
[1951.72 → 1952.86] then GANs
[1952.86 → 1953.98] are indisputably
[1953.98 → 1954.64] the state of
[1954.64 → 1955.22] art for
[1955.22 → 1955.88] those type
[1955.88 → 1956.42] of tasks.
[1957.04 → 1958.02] So we
[1958.02 → 1958.30] kind of
[1958.30 → 1958.68] gone over
[1958.68 → 1960.50] the basic
[1960.50 → 1961.14] generator,
[1961.34 → 1961.94] discriminator,
[1962.20 → 1963.44] the interplay
[1963.44 → 1964.16] between the
[1964.16 → 1964.84] two and
[1964.84 → 1965.70] the specific
[1965.70 → 1966.22] models.
[1966.78 → 1967.42] I know that
[1967.42 → 1968.20] you talk
[1968.20 → 1968.86] about a few
[1968.86 → 1969.68] more advanced
[1969.68 → 1970.80] types of GANs
[1970.80 → 1971.72] in your book
[1971.72 → 1972.04] though.
[1972.50 → 1973.14] Is there a
[1973.14 → 1974.44] whole, I guess
[1974.44 → 1975.30] this is a whole
[1975.30 → 1976.04] research area,
[1976.08 → 1976.32] and there's
[1976.32 → 1976.88] probably a lot
[1976.88 → 1977.28] of different
[1977.28 → 1978.16] types of GANs,
[1978.16 → 1978.78] but are
[1978.78 → 1979.44] there some
[1979.44 → 1980.10] more advanced
[1980.10 → 1980.58] types of
[1980.58 → 1981.04] GANs that
[1981.04 → 1981.82] are starting
[1981.82 → 1982.82] to filter
[1982.82 → 1983.76] into maybe
[1983.76 → 1984.38] a little bit
[1984.38 → 1985.24] wider spread
[1985.24 → 1985.96] usage?
[1986.58 → 1987.22] Yeah, yeah,
[1987.30 → 1988.10] Jacob, do you
[1988.10 → 1988.44] want to talk
[1988.44 → 1989.16] about Cycleway?
[1989.84 → 1990.30] And I can
[1990.30 → 1990.96] then talk about
[1990.96 → 1991.82] semi-supervised
[1991.82 → 1992.68] paradigms.
[1993.18 → 1993.42] Sure.
[1993.68 → 1994.28] So I think,
[1994.32 → 1995.06] yeah, I think
[1995.06 → 1996.10] like Vlad said,
[1996.20 → 1996.76] I think Cycleway
[1996.76 → 1997.58] is definitely one
[1997.58 → 1998.54] of the more
[1998.54 → 1999.50] prominent examples.
[1999.72 → 2000.54] I think when you
[2000.54 → 2001.34] talk specifically
[2001.34 → 2002.42] about the
[2002.42 → 2003.28] different cases
[2003.28 → 2003.90] and different
[2003.90 → 2004.52] applications,
[2004.92 → 2005.26] I think,
[2005.52 → 2006.08] for example,
[2006.26 → 2006.82] Began is
[2006.82 → 2007.48] very popular
[2007.48 → 2009.08] with sort
[2009.08 → 2009.84] of as an
[2009.84 → 2010.74] artistic tool.
[2010.90 → 2011.38] So there is
[2011.38 → 2012.26] a tool you
[2012.26 → 2012.96] can check out
[2012.96 → 2014.44] made by one
[2014.44 → 2015.32] of my friends,
[2015.42 → 2016.22] Joel, who
[2016.22 → 2016.90] wrote GAN
[2016.90 → 2017.24] Breeder.
[2017.46 → 2017.80] I think it's
[2017.80 → 2018.82] GANbreeder.app
[2018.82 → 2019.16] or something
[2019.16 → 2019.60] like that.
[2019.84 → 2021.66] And you can
[2021.66 → 2022.40] sort of create
[2022.40 → 2023.26] new combinations
[2023.26 → 2024.22] of images and
[2024.22 → 2025.04] people have
[2025.04 → 2026.44] entire art
[2026.44 → 2027.94] collection just
[2027.94 → 2029.02] off of generative
[2029.02 → 2029.98] art that have
[2029.98 → 2030.50] been happening
[2030.50 → 2031.14] for quite a few
[2031.14 → 2031.60] years now.
[2031.68 → 2032.00] I was very
[2032.00 → 2032.66] surprised at how
[2032.66 → 2033.74] quickly GANs
[2033.74 → 2034.44] became popular
[2034.44 → 2035.44] among the
[2035.44 → 2036.58] artistic community
[2036.58 → 2037.50] there's lots
[2037.50 → 2038.62] of digital
[2038.62 → 2039.86] artists using
[2039.86 → 2041.38] GANs as their
[2041.38 → 2042.20] primary tool of
[2042.20 → 2042.56] choice.
[2043.22 → 2044.18] So there's
[2044.18 → 2045.44] Began,
[2045.56 → 2046.16] Cycleway,
[2046.76 → 2048.24] and I think
[2048.24 → 2049.52] there has been
[2049.52 → 2050.38] recently,
[2051.02 → 2051.44] well,
[2052.08 → 2052.64] a couple of
[2052.64 → 2053.32] startups popped
[2053.32 → 2054.34] up using
[2054.34 → 2056.02] Style as
[2056.02 → 2057.18] well as a way
[2057.18 → 2057.70] to generate
[2057.70 → 2058.72] stock images
[2058.72 → 2059.84] of very high
[2059.84 → 2060.74] resolution faces
[2060.74 → 2061.76] and a bunch
[2061.76 → 2062.02] more.
[2062.14 → 2062.44] But I don't
[2062.44 → 2063.20] want to steal
[2063.20 → 2064.02] all the
[2064.02 → 2065.18] material from
[2065.18 → 2065.46] Vlad.
[2065.46 → 2066.66] I was
[2066.66 → 2067.04] wondering,
[2067.40 → 2067.82] but as
[2067.82 → 2068.10] you all are
[2068.10 → 2068.56] talking about
[2068.56 → 2068.92] this and
[2068.92 → 2069.20] you're kind
[2069.20 → 2069.50] of going
[2069.50 → 2070.16] through these
[2070.16 → 2070.60] different
[2070.60 → 2071.24] versions,
[2071.82 → 2072.52] if you could,
[2072.88 → 2073.92] I recognize
[2073.92 → 2074.64] you don't want
[2074.64 → 2075.28] to go do a
[2075.28 → 2075.62] deep dive
[2075.62 → 2076.14] necessarily on
[2076.14 → 2076.54] all of them,
[2076.86 → 2077.24] but if you
[2077.24 → 2077.60] could give
[2077.60 → 2078.96] us a little
[2078.96 → 2079.28] bit of
[2079.28 → 2079.82] explanation
[2079.82 → 2080.42] with kind
[2080.42 → 2080.70] of each
[2080.70 → 2080.90] of the
[2080.90 → 2081.40] titles that
[2081.40 → 2081.64] you just
[2081.64 → 2082.02] went through
[2082.02 → 2082.74] so that
[2082.74 → 2083.04] those of
[2083.04 → 2083.24] us who
[2083.24 → 2083.48] are not
[2083.48 → 2083.92] as familiar
[2083.92 → 2084.30] with them
[2084.30 → 2085.00] can kind
[2085.00 → 2085.96] of categorize
[2085.96 → 2086.22] them in
[2086.22 → 2086.50] our own
[2086.50 → 2087.10] thinking as
[2087.10 → 2087.46] we try to
[2087.46 → 2087.82] absorb the
[2087.82 → 2088.18] material.
[2089.00 → 2089.02] Yeah,
[2089.08 → 2089.36] I think
[2089.36 → 2089.78] maybe you
[2089.78 → 2090.14] mentioned
[2090.14 → 2091.20] Cycleway
[2091.20 → 2092.34] and Style,
[2092.46 → 2092.70] I think,
[2092.84 → 2092.98] was it?
[2092.98 → 2094.56] Is there
[2094.56 → 2094.98] like a
[2094.98 → 2095.34] quick,
[2095.70 → 2096.48] we'll really
[2096.48 → 2097.22] test your
[2097.22 → 2098.08] summarization
[2098.08 → 2098.56] skills,
[2098.84 → 2099.26] like a
[2099.26 → 2099.86] quick one
[2099.86 → 2100.32] sentence
[2100.32 → 2101.14] description
[2101.14 → 2101.56] of each
[2101.56 → 2101.86] of those?
[2101.98 → 2102.88] So I
[2102.88 → 2103.62] think the
[2103.62 → 2104.08] way to
[2104.08 → 2104.42] think of
[2104.42 → 2105.02] Cycleway
[2105.02 → 2106.02] on a very
[2106.02 → 2106.54] high level
[2106.54 → 2107.22] is you
[2107.22 → 2107.68] have two
[2107.68 → 2108.62] domains and
[2108.62 → 2109.10] you're trying
[2109.10 → 2109.74] to basically
[2109.74 → 2110.40] always map
[2110.40 → 2110.90] one domain
[2110.90 → 2111.40] into the
[2111.40 → 2111.64] other.
[2112.10 → 2112.54] And it's
[2112.54 → 2113.28] very surprising
[2113.28 → 2113.78] how broadly
[2113.78 → 2114.64] that transfers.
[2114.92 → 2115.36] So for
[2115.36 → 2115.86] instance,
[2116.32 → 2117.08] satellite images
[2117.08 → 2117.72] to something
[2117.72 → 2118.12] that looks
[2118.12 → 2118.54] like Google
[2118.54 → 2119.08] Maps or
[2119.08 → 2119.50] night to
[2119.50 → 2119.76] day,
[2119.98 → 2120.38] these could
[2120.38 → 2120.78] be different
[2120.78 → 2121.34] domains.
[2121.88 → 2122.06] And you
[2122.06 → 2122.44] can then
[2122.44 → 2122.92] have a
[2122.92 → 2123.34] generative
[2123.34 → 2123.94] framework that
[2123.94 → 2124.72] can translate
[2124.72 → 2126.42] something that
[2126.42 → 2127.22] is a day
[2127.22 → 2127.64] image into
[2127.64 → 2128.42] night image
[2128.42 → 2128.90] and back
[2128.90 → 2129.20] again.
[2129.42 → 2129.68] So you
[2129.68 → 2130.20] can have
[2130.20 → 2130.64] these two
[2130.64 → 2131.14] domains and
[2131.14 → 2131.62] you can have
[2131.62 → 2132.74] one generator
[2132.74 → 2133.26] for each
[2133.26 → 2133.80] translation,
[2133.96 → 2134.28] basically,
[2134.72 → 2135.42] if that makes
[2135.42 → 2135.82] sense.
[2136.62 → 2136.98] That does.
[2137.04 → 2137.36] That's a good
[2137.36 → 2137.50] one.
[2137.60 → 2137.96] I like that
[2137.96 → 2138.20] kind of
[2138.20 → 2138.78] hands-on
[2138.78 → 2139.96] aspect because
[2139.96 → 2140.46] as I'm
[2140.46 → 2141.10] trying to
[2141.10 → 2141.66] follow what
[2141.66 → 2142.16] you're saying,
[2142.24 → 2142.68] that gives
[2142.68 → 2143.46] me a tangible
[2143.46 → 2143.94] example.
[2144.32 → 2144.88] Do you have
[2144.88 → 2146.12] something similar
[2146.12 → 2146.78] for the
[2146.78 → 2147.14] Style?
[2147.72 → 2148.92] So Style,
[2149.38 → 2150.94] I think most
[2150.94 → 2151.76] of the advancement
[2151.76 → 2152.50] there is in
[2152.50 → 2154.30] the algorithmic
[2154.30 → 2158.86] perspective.
[2159.82 → 2160.42] I think one
[2160.42 → 2160.98] of the things
[2160.98 → 2162.26] that Style
[2162.26 → 2163.20] had, one of
[2163.20 → 2163.52] the major
[2163.52 → 2164.10] innovations,
[2164.34 → 2164.80] just a big
[2164.80 → 2166.18] one, was
[2166.18 → 2166.66] the fact that
[2166.66 → 2168.42] you don't
[2168.42 → 2169.16] source from
[2169.16 → 2169.56] the latent
[2169.56 → 2170.40] space just at
[2170.40 → 2170.80] the beginning,
[2170.96 → 2171.50] but you keep
[2171.50 → 2173.00] adding information
[2173.00 → 2173.74] throughout the
[2173.74 → 2174.78] generative process.
[2175.44 → 2175.88] So that means
[2175.88 → 2176.74] you can influence
[2176.74 → 2177.62] different levels
[2177.62 → 2178.54] of features and
[2178.54 → 2179.54] have much finer
[2179.54 → 2180.16] level of
[2180.16 → 2180.62] control.
[2181.26 → 2182.46] So because you
[2182.46 → 2183.98] keep adding
[2183.98 → 2185.56] sources of
[2185.56 → 2186.40] information and
[2186.40 → 2186.96] inspiration,
[2187.16 → 2188.52] throughout the
[2188.52 → 2189.34] generative process
[2189.34 → 2189.90] at different
[2189.90 → 2190.68] layers of
[2190.68 → 2191.24] resolution,
[2191.68 → 2193.54] you can more
[2193.54 → 2194.48] finely tune
[2194.48 → 2196.40] the big,
[2196.70 → 2198.02] broad aspects
[2198.02 → 2198.68] of the face
[2198.68 → 2200.20] or very tiny
[2200.20 → 2200.82] details,
[2201.20 → 2201.58] and you have
[2201.58 → 2201.94] a more
[2201.94 → 2202.40] granular
[2202.40 → 2203.36] control than
[2203.36 → 2204.20] just the
[2204.20 → 2204.98] initial vector.
[2205.64 → 2206.28] If you just
[2206.28 → 2206.76] want to change
[2206.76 → 2207.62] the hair a
[2207.62 → 2208.00] little bit,
[2208.06 → 2208.48] you can do
[2208.48 → 2208.70] that.
[2208.80 → 2209.06] Or if you
[2209.06 → 2210.02] want to change
[2210.02 → 2210.54] the whole
[2210.54 → 2211.12] face or
[2211.12 → 2212.02] ethnicity or
[2212.02 → 2213.08] gender or
[2213.08 → 2213.60] these big,
[2213.68 → 2214.10] you can do
[2214.10 → 2215.06] that also and
[2215.06 → 2215.48] you can have
[2215.48 → 2217.62] a better way
[2217.62 → 2218.28] of expressing
[2218.28 → 2219.50] what type of
[2219.50 → 2219.92] image you'd
[2219.92 → 2220.40] like to get.
[2220.40 → 2234.28] This episode
[2234.28 → 2235.02] is brought to
[2235.02 → 2235.40] you by
[2235.40 → 2236.06] Brave.
[2236.24 → 2236.98] Big news
[2236.98 → 2237.34] from the
[2237.34 → 2237.90] Brave team,
[2238.10 → 2239.18] version 1.0
[2239.18 → 2239.90] is official.
[2240.26 → 2240.78] That means
[2240.78 → 2241.30] our favourite
[2241.30 → 2242.00] open source,
[2242.20 → 2243.00] privacy focused,
[2243.18 → 2243.96] blazing fast
[2243.96 → 2244.88] browser is ready
[2244.88 → 2245.56] for prime time.
[2245.96 → 2246.40] Their brand
[2246.40 → 2247.46] new iOS app
[2247.46 → 2248.36] landed just in
[2248.36 → 2248.82] time for the
[2248.82 → 2249.54] announcement and
[2249.54 → 2250.26] the Brave team
[2250.26 → 2250.88] is celebrating
[2250.88 → 2251.52] by granting
[2251.52 → 2252.44] 8 million
[2252.44 → 2253.30] basic attention
[2253.30 → 2254.00] tokens to the
[2254.00 → 2254.38] community.
[2254.70 → 2255.18] That means
[2255.18 → 2255.46] when you
[2255.46 → 2256.02] download the
[2256.02 → 2256.66] iOS app,
[2256.74 → 2257.40] you get 20
[2257.40 → 2258.30] bat absolutely
[2258.30 → 2258.82] free.
[2259.20 → 2259.90] Put it to
[2259.90 → 2260.62] good use by
[2260.62 → 2261.02] heading to
[2261.02 → 2262.14] changelog.com,
[2262.28 → 2262.62] hitting the
[2262.62 → 2263.58] triangle icon in
[2263.58 → 2263.88] the upper
[2263.88 → 2264.28] right hand
[2264.28 → 2265.32] corner and
[2265.32 → 2265.86] flipping us a
[2265.86 → 2266.08] tip.
[2280.26 → 2280.80] So Vlad,
[2280.80 → 2281.06] Vlad, I
[2281.06 → 2281.88] think maybe you
[2281.88 → 2282.68] had some
[2282.68 → 2283.78] other input as
[2283.78 → 2284.14] well in
[2284.14 → 2284.94] terms of
[2284.94 → 2286.44] maybe advanced
[2286.44 → 2287.56] or specific
[2287.56 → 2288.64] different kinds
[2288.64 → 2289.52] of GANs that
[2289.52 → 2290.14] people are
[2290.14 → 2291.44] pursuing now in
[2291.44 → 2291.90] a sort of
[2291.90 → 2292.92] wider sense.
[2293.06 → 2293.42] Yeah, sure.
[2293.52 → 2293.98] Yeah, I can
[2293.98 → 2294.62] talk to the
[2294.62 → 2295.48] conditional GAN.
[2296.24 → 2296.66] So in a
[2296.66 → 2297.28] regular GAN,
[2297.38 → 2297.80] you have the
[2297.80 → 2298.70] data set of,
[2299.08 → 2299.32] let's say,
[2299.38 → 2300.06] real images of
[2300.06 → 2301.80] human faces that
[2301.80 → 2302.82] the generator over
[2302.82 → 2303.62] the course of the
[2303.62 → 2304.48] training iterations
[2304.48 → 2305.26] learned to
[2305.26 → 2306.10] mimic.
[2307.00 → 2308.20] But similar to
[2308.20 → 2308.90] what Jacob was
[2308.90 → 2309.52] mentioning [2309.52 → 2310.02] style GAN,
[2310.12 → 2311.02] there is no way
[2311.02 → 2312.78] in the classic
[2312.78 → 2314.08] GAN paradigm to
[2314.08 → 2315.44] control what
[2315.44 → 2316.22] type of image
[2316.22 → 2316.60] would get
[2316.60 → 2317.10] generated.
[2317.66 → 2318.64] So once the
[2318.64 → 2319.22] generator gets
[2319.22 → 2320.54] trained on a
[2320.54 → 2321.64] data set of
[2321.64 → 2322.68] real human faces,
[2323.54 → 2324.26] at any given
[2324.26 → 2324.94] time when you
[2324.94 → 2325.58] feed it a
[2325.58 → 2326.76] random vector,
[2327.18 → 2328.04] that's the
[2328.04 → 2328.56] latent vector
[2328.56 → 2329.44] that Jacob was
[2329.44 → 2330.22] mentioning earlier,
[2330.62 → 2331.22] it would spit
[2331.22 → 2331.94] out a face.
[2332.26 → 2333.20] But the
[2333.20 → 2333.84] researcher would
[2333.84 → 2334.66] have no control
[2334.66 → 2335.32] over whether
[2335.32 → 2336.04] the face is
[2336.04 → 2337.44] a man or
[2337.44 → 2338.12] a female or
[2338.12 → 2339.16] a child or
[2339.16 → 2340.50] let alone more
[2340.50 → 2341.42] fine-tuned features
[2341.42 → 2342.22] in like a
[2342.22 → 2342.66] human with
[2342.66 → 2344.10] glasses or
[2344.10 → 2344.70] somebody with
[2344.70 → 2345.32] long hair or
[2345.32 → 2346.10] short hair and
[2346.10 → 2346.90] so on.
[2347.56 → 2347.92] But the
[2347.92 → 2348.62] conditional GAN
[2348.62 → 2349.26] allowed to do,
[2349.40 → 2349.94] which is one of
[2349.94 → 2350.80] the early
[2350.80 → 2351.70] innovations that
[2351.70 → 2353.02] was since then
[2353.02 → 2354.26] fine-tuned by
[2354.26 → 2354.72] the research
[2354.72 → 2355.22] community,
[2355.54 → 2356.10] was to
[2356.10 → 2357.36] introduce labels
[2357.36 → 2358.22] during the
[2358.22 → 2359.08] training process
[2359.08 → 2360.74] which allowed
[2360.74 → 2362.86] the discriminator
[2362.86 → 2365.32] to not only
[2365.32 → 2366.02] recognize,
[2366.04 → 2366.50] whether an
[2366.50 → 2367.06] image is
[2367.06 → 2367.56] real or
[2367.56 → 2367.98] fake,
[2368.30 → 2368.88] but also
[2368.88 → 2369.32] whether it
[2369.32 → 2370.06] matches the
[2370.06 → 2370.68] given label.
[2371.20 → 2371.92] So in the
[2371.92 → 2372.76] example of
[2372.76 → 2373.52] human faces,
[2374.06 → 2374.60] it receives
[2374.60 → 2375.20] an image,
[2376.16 → 2376.88] it receives,
[2377.28 → 2377.88] it's told
[2377.88 → 2378.40] whether it's
[2378.40 → 2379.96] real or fake
[2379.96 → 2380.28] image,
[2380.50 → 2381.24] but it's also
[2381.24 → 2381.84] told what
[2381.84 → 2382.68] gender it is.
[2383.88 → 2384.54] So,
[2384.72 → 2385.62] for the generator
[2385.62 → 2386.78] to be successful
[2386.78 → 2387.88] at fooling the
[2387.88 → 2388.66] discriminator,
[2389.30 → 2390.02] it needs to
[2390.02 → 2390.86] produce images
[2390.86 → 2391.66] that are not
[2391.66 → 2393.02] only realistic
[2393.02 → 2393.60] looking,
[2394.06 → 2394.82] but also
[2394.82 → 2395.38] ones that
[2395.38 → 2395.88] match the
[2395.88 → 2396.16] label.
[2397.14 → 2398.06] And the
[2398.06 → 2398.68] magic of it
[2398.68 → 2399.22] is that once
[2399.22 → 2399.82] you have the
[2399.82 → 2400.98] generator properly
[2400.98 → 2401.46] trained,
[2401.94 → 2402.60] you can then
[2402.60 → 2403.20] pass it the
[2403.20 → 2403.92] latent space
[2403.92 → 2405.26] and the label
[2405.26 → 2405.72] that you would
[2405.72 → 2406.20] produce,
[2406.28 → 2406.76] such as,
[2406.82 → 2406.94] you know,
[2406.94 → 2409.00] I want an
[2409.00 → 2409.54] image of a
[2409.54 → 2409.90] child,
[2410.20 → 2411.38] and it would,
[2411.92 → 2412.40] given, you
[2412.40 → 2412.52] know,
[2412.56 → 2413.80] sufficient training
[2413.80 → 2414.32] data set,
[2414.40 → 2414.66] and it's
[2414.66 → 2415.38] properly trained,
[2415.68 → 2416.26] it would then
[2416.26 → 2418.04] produce a fake
[2418.04 → 2418.62] example,
[2419.14 → 2419.72] matching the
[2419.72 → 2420.34] label of your
[2420.34 → 2420.80] choice.
[2421.78 → 2422.94] And on the
[2422.94 → 2424.46] discriminator side,
[2424.60 → 2425.16] like in that
[2425.16 → 2425.86] case,
[2425.92 → 2426.32] would it just
[2426.32 → 2426.88] be a matter
[2426.88 → 2427.78] of like adding
[2427.78 → 2428.66] a feature to
[2428.66 → 2429.40] the input of
[2429.40 → 2430.26] that classifier
[2430.26 → 2430.94] that would be
[2430.94 → 2431.88] like, you
[2431.88 → 2431.96] know,
[2432.02 → 2432.66] whatever it is,
[2432.74 → 2433.70] gender or
[2433.70 → 2434.68] ethnicity,
[2434.88 → 2435.40] like was
[2435.40 → 2435.72] mentioned,
[2436.08 → 2436.48] is that just
[2436.48 → 2437.16] another feature
[2437.16 → 2437.72] that gets
[2437.72 → 2438.30] factored into
[2438.30 → 2438.94] the discriminator?
[2438.96 → 2439.08] Yeah,
[2439.12 → 2439.34] exactly.
[2439.50 → 2439.74] There are
[2439.74 → 2440.36] different
[2440.36 → 2441.14] implementations
[2441.14 → 2441.70] how this can
[2441.70 → 2442.08] be done on
[2442.08 → 2442.44] a technical
[2442.44 → 2442.76] level,
[2442.90 → 2443.60] but broadly
[2443.60 → 2443.98] speaking,
[2444.04 → 2444.52] you're absolutely
[2444.52 → 2444.90] right.
[2445.02 → 2445.64] It's essentially
[2445.64 → 2446.54] training
[2446.54 → 2447.58] classification,
[2448.04 → 2448.90] that isn't
[2448.90 → 2450.06] only binary,
[2450.36 → 2451.18] as in real
[2451.18 → 2451.74] or fake,
[2451.92 → 2452.60] but it is
[2452.60 → 2453.52] one that is
[2453.52 → 2454.30] taking into
[2454.30 → 2455.12] account also
[2455.12 → 2456.18] the correct
[2456.18 → 2456.60] label.
[2456.86 → 2457.18] And what's
[2457.18 → 2458.08] really great
[2458.08 → 2458.68] for the
[2458.68 → 2459.40] conditional
[2459.40 → 2459.98] GAN paradigm
[2459.98 → 2461.00] is that the
[2461.00 → 2461.40] additional
[2461.40 → 2462.32] information that
[2462.32 → 2462.76] the training
[2462.76 → 2463.40] process is
[2463.40 → 2464.16] conditioned on
[2464.16 → 2465.36] can be
[2465.36 → 2465.98] arbitrary,
[2466.28 → 2466.86] so it can
[2466.86 → 2467.32] be a
[2467.32 → 2467.78] description,
[2468.56 → 2469.78] or it can
[2469.78 → 2470.24] be a single
[2470.24 → 2470.56] label,
[2470.70 → 2470.98] or it can
[2470.98 → 2471.28] be a
[2471.28 → 2471.68] description.
[2471.96 → 2472.74] So there
[2472.74 → 2473.20] are also
[2473.20 → 2473.94] GAN models
[2473.94 → 2474.54] that can
[2474.54 → 2475.30] take in a
[2475.30 → 2475.62] set of
[2475.62 → 2476.00] tags,
[2476.06 → 2476.48] or even
[2476.48 → 2476.84] like a
[2476.84 → 2477.04] word
[2477.04 → 2477.60] description,
[2478.04 → 2478.50] and then
[2478.50 → 2479.30] produce an
[2479.30 → 2479.88] image that
[2479.88 → 2480.42] is matching
[2480.42 → 2480.64] the
[2480.64 → 2481.10] description.
[2482.60 → 2482.94] So you
[2482.94 → 2483.56] can, for
[2483.56 → 2483.86] instance,
[2483.98 → 2484.44] feed it
[2484.44 → 2485.70] a description,
[2485.88 → 2486.22] say like
[2486.22 → 2486.96] birds sitting
[2486.96 → 2487.36] on a
[2487.36 → 2487.86] branch,
[2488.14 → 2488.76] and if
[2488.76 → 2489.10] properly
[2489.10 → 2489.70] trained and
[2489.70 → 2490.78] given sufficient
[2490.78 → 2491.12] data,
[2491.24 → 2492.06] then the
[2492.06 → 2492.82] generator would
[2492.82 → 2493.58] produce a
[2493.58 → 2494.46] take image
[2494.46 → 2495.62] matching the
[2495.62 → 2496.20] description.
[2497.40 → 2497.56] You know,
[2497.62 → 2498.06] of course,
[2498.12 → 2498.72] our imagination
[2498.72 → 2499.32] can go
[2499.32 → 2499.64] well,
[2499.76 → 2500.34] but I
[2500.34 → 2500.82] could see
[2500.82 → 2501.58] this having
[2501.58 → 2502.38] tremendous
[2502.38 → 2502.86] practical
[2502.86 → 2503.48] applications,
[2503.48 → 2504.02] especially
[2504.02 → 2505.36] in spaces
[2505.36 → 2506.36] like animation,
[2507.12 → 2507.48] where
[2507.48 → 2508.38] currently you
[2508.38 → 2510.04] need a
[2510.04 → 2510.44] lot of
[2510.44 → 2511.06] effort by
[2511.06 → 2511.40] human
[2511.40 → 2512.86] animators to
[2512.86 → 2513.48] create,
[2513.60 → 2514.08] let's say,
[2514.14 → 2514.74] characters in
[2514.74 → 2515.24] a game,
[2515.48 → 2516.56] or characters
[2516.56 → 2517.10] in a
[2517.10 → 2517.42] say,
[2517.52 → 2518.28] Pixar movie,
[2518.86 → 2519.38] but with
[2519.38 → 2519.82] GANs,
[2519.88 → 2520.48] you can
[2520.48 → 2521.38] greatly
[2521.38 → 2522.44] optimize this
[2522.44 → 2523.08] creative
[2523.08 → 2524.28] workflow by
[2524.28 → 2525.12] having the
[2525.12 → 2526.04] trained model
[2526.04 → 2527.56] essentially aiding
[2527.56 → 2528.08] the human
[2528.08 → 2529.12] animator.
[2529.62 → 2530.42] Or if
[2530.42 → 2531.20] these techniques
[2531.20 → 2532.24] get advanced
[2532.24 → 2532.58] enough,
[2532.66 → 2532.92] you can
[2532.92 → 2533.42] imagine
[2533.42 → 2534.52] digital
[2534.52 → 2535.06] worlds,
[2535.32 → 2536.04] be it in
[2536.04 → 2537.22] VR or
[2537.22 → 2538.12] even like a
[2538.12 → 2538.76] regular PC
[2538.76 → 2539.24] game,
[2539.62 → 2540.34] which self
[2540.34 → 2540.84] creates,
[2540.96 → 2541.32] so you can
[2541.32 → 2541.84] essentially
[2541.84 → 2542.34] going to be
[2542.34 → 2542.90] an infinite
[2542.90 → 2543.80] world where
[2543.80 → 2545.06] characters get
[2545.06 → 2546.08] generated on
[2546.08 → 2546.64] the fly,
[2546.84 → 2547.48] new terrains
[2547.48 → 2548.12] get generated
[2548.12 → 2548.82] on the fly,
[2549.24 → 2549.76] and are going
[2549.76 → 2550.72] to be extremely
[2550.72 → 2552.32] believable without
[2552.32 → 2553.08] the need for
[2553.08 → 2554.44] input for a
[2554.44 → 2555.20] human animator
[2555.20 → 2555.86] or even
[2555.86 → 2556.26] programmer.
[2557.00 → 2557.34] Gotcha.
[2557.58 → 2558.34] So I'm
[2558.34 → 2558.64] curious,
[2558.82 → 2559.44] there is so
[2559.44 → 2560.04] much research
[2560.04 → 2560.66] going on
[2560.66 → 2561.94] right now in
[2561.94 → 2562.44] GANs.
[2562.66 → 2563.28] It seems to
[2563.28 → 2563.72] have really
[2563.72 → 2564.62] exploded in
[2564.62 → 2565.22] terms of
[2565.22 → 2566.54] just so many
[2566.54 → 2566.94] people and
[2566.94 → 2568.08] organizations are
[2568.08 → 2568.94] interested in
[2568.94 → 2569.42] this and
[2569.42 → 2569.86] trying to
[2569.86 → 2570.78] level up.
[2571.18 → 2571.46] What are
[2571.46 → 2572.10] some of the
[2572.10 → 2572.88] the biggest open
[2572.88 → 2574.30] questions that
[2574.30 → 2575.06] are still out
[2575.06 → 2575.40] there that
[2575.40 → 2575.78] people are
[2575.78 → 2576.32] trying to
[2576.32 → 2577.10] address right
[2577.10 → 2577.42] now?
[2577.84 → 2578.30] Where do you
[2578.30 → 2579.28] see the top
[2579.28 → 2580.14] researchers really
[2580.14 → 2580.54] focusing?
[2581.52 → 2582.40] So just to
[2582.40 → 2584.16] put my
[2584.16 → 2584.72] perspective,
[2584.98 → 2585.48] and I think
[2585.48 → 2586.28] definitely keen
[2586.28 → 2587.48] to hear what
[2587.48 → 2588.44] Vlad thinks about
[2588.44 → 2589.06] this as well,
[2589.74 → 2590.76] there is the
[2590.76 → 2591.46] training question
[2591.46 → 2591.82] that we've
[2591.82 → 2592.44] already alluded
[2592.44 → 2592.80] to.
[2593.58 → 2594.68] And I
[2594.68 → 2595.56] think the
[2595.56 → 2596.68] other big
[2596.68 → 2597.52] area is
[2597.52 → 2598.78] these more
[2598.78 → 2599.36] complex
[2599.36 → 2600.50] data sets that
[2600.50 → 2601.44] I think are
[2601.44 → 2602.48] only getting
[2602.48 → 2603.68] started, the
[2603.68 → 2604.42] whole audio
[2604.42 → 2604.88] synthesis.
[2605.52 → 2606.12] I think the
[2606.12 → 2607.40] first papers that
[2607.40 → 2607.82] I remember
[2607.82 → 2609.24] seeing using
[2609.24 → 2610.80] audio were
[2610.80 → 2612.02] maybe at
[2612.02 → 2612.88] clear this
[2612.88 → 2613.92] year, CLR,
[2614.14 → 2614.64] which is one of
[2614.64 → 2614.88] the big
[2614.88 → 2615.34] conferences.
[2616.00 → 2616.32] Maybe there
[2616.32 → 2616.62] was something
[2616.62 → 2617.34] before, but
[2617.34 → 2618.06] that was the
[2618.06 → 2618.64] first time I
[2618.64 → 2619.78] saw good
[2619.78 → 2620.52] attempts at
[2620.52 → 2621.04] doing that.
[2621.32 → 2621.82] And I
[2621.82 → 2622.32] think just
[2622.32 → 2623.40] last month
[2623.40 → 2623.68] or two
[2623.68 → 2624.12] months ago,
[2624.20 → 2624.60] DeepMind
[2624.60 → 2625.20] released GAN
[2625.20 → 2625.58] TTS.
[2625.96 → 2626.76] So there's
[2626.76 → 2627.28] just an
[2627.28 → 2627.96] example of
[2627.96 → 2628.46] a vertical
[2628.46 → 2629.24] where I
[2629.24 → 2629.74] would expect
[2629.74 → 2630.28] more things
[2630.28 → 2630.78] to happen.
[2631.68 → 2632.34] And so I
[2632.34 → 2632.88] definitely think
[2632.88 → 2633.36] that there's
[2633.36 → 2634.12] a lot of
[2634.12 → 2635.00] scope in
[2635.00 → 2638.02] these non-visual
[2638.02 → 2638.40] types of
[2638.40 → 2639.16] data, at
[2639.16 → 2640.76] least in
[2640.76 → 2641.22] research.
[2641.42 → 2642.18] I'm not so
[2642.18 → 2642.62] sure about
[2642.62 → 2643.96] production in
[2643.96 → 2644.38] the next
[2644.38 → 2644.92] year, but
[2644.92 → 2645.94] research
[2645.94 → 2646.54] definitely.
[2646.92 → 2647.48] And the
[2647.48 → 2648.02] third area
[2648.02 → 2648.60] I'll mention
[2648.60 → 2649.76] is just
[2649.76 → 2650.54] having a
[2650.54 → 2651.36] GAN being
[2651.36 → 2653.00] incorporated in
[2653.00 → 2653.62] some bigger
[2653.62 → 2654.10] process.
[2654.36 → 2654.82] I think a
[2654.82 → 2655.32] lot of the
[2655.32 → 2656.62] time when
[2656.62 → 2656.96] I've seen
[2656.96 → 2657.34] some of the
[2657.34 → 2657.90] more successful
[2657.90 → 2658.78] applications of
[2658.78 → 2659.36] GANs that
[2659.36 → 2660.02] have actually
[2660.02 → 2661.04] gotten deployed
[2661.04 → 2662.64] were things
[2662.64 → 2663.70] that it was
[2663.70 → 2664.08] a sort of
[2664.08 → 2665.48] supporting process
[2665.48 → 2666.24] either on the
[2666.24 → 2667.04] training side or
[2667.04 → 2667.48] some sort of
[2667.48 → 2668.20] post-processing
[2668.20 → 2669.04] side for a
[2669.04 → 2669.86] larger machine
[2669.86 → 2670.74] learning pipeline.
[2671.28 → 2671.74] So I think
[2671.74 → 2672.88] GANs have a lot
[2672.88 → 2673.38] to offer.
[2673.38 → 2674.16] if you know
[2674.16 → 2675.44] how to add
[2675.44 → 2676.26] it into
[2676.26 → 2677.42] your algorithm,
[2677.68 → 2678.32] whether that's
[2678.32 → 2679.34] as a domain
[2679.34 → 2679.92] adaptation
[2679.92 → 2681.64] algorithm or
[2681.64 → 2682.34] just some
[2682.34 → 2683.92] better
[2683.92 → 2686.02] tabular data
[2686.02 → 2687.92] generator or
[2687.92 → 2688.94] anonymization
[2688.94 → 2689.40] tool, that
[2689.40 → 2689.84] sort of thing.
[2689.98 → 2690.88] So there's
[2690.88 → 2691.68] definitely a lot
[2691.68 → 2693.82] of scope for
[2693.82 → 2694.44] them to be
[2694.44 → 2695.50] incorporated as
[2695.50 → 2696.14] one of the
[2696.14 → 2696.80] pieces in a
[2696.80 → 2697.36] bigger puzzle.
[2698.38 → 2698.70] Awesome.
[2699.10 → 2699.78] And Vlad,
[2699.88 → 2700.34] did you have
[2700.34 → 2701.08] anything to
[2701.08 → 2701.88] add there?
[2702.10 → 2702.94] Or I don't
[2702.94 → 2703.40] want to cause
[2703.40 → 2704.32] any friction
[2704.32 → 2704.98] between the
[2704.98 → 2705.40] two of you,
[2705.48 → 2705.90] but if you
[2705.90 → 2706.92] disagree or
[2706.92 → 2707.74] have any
[2707.74 → 2708.10] thoughts,
[2708.24 → 2708.64] what are your
[2708.64 → 2709.04] thoughts here?
[2709.10 → 2709.42] Yeah, no,
[2709.48 → 2710.04] I think it's
[2710.04 → 2710.66] like the
[2710.66 → 2711.12] GANs are
[2711.12 → 2711.84] great that
[2711.84 → 2712.78] there are
[2712.78 → 2713.28] countless
[2713.28 → 2714.66] research directions
[2714.66 → 2715.10] and different
[2715.10 → 2715.86] people can get
[2715.86 → 2716.76] excited about
[2716.76 → 2718.00] the different
[2718.00 → 2718.96] opportunities there.
[2719.04 → 2719.48] For me,
[2719.56 → 2720.40] it's primarily
[2720.40 → 2721.84] the ability
[2721.84 → 2722.70] to leverage
[2722.70 → 2723.38] the internal
[2723.38 → 2724.16] representations
[2724.16 → 2725.00] that the
[2725.00 → 2725.62] GAN model
[2725.62 → 2727.16] learns along
[2727.16 → 2727.88] the way to
[2727.88 → 2728.68] succeed at
[2728.68 → 2729.16] the generative
[2729.16 → 2729.62] task.
[2729.62 → 2730.46] So this
[2730.46 → 2731.30] would be a
[2731.30 → 2732.48] similar idea
[2732.48 → 2733.00] to what
[2733.00 → 2733.90] people talk
[2733.90 → 2734.42] about in
[2734.42 → 2735.42] sort of,
[2735.56 → 2735.96] like, I
[2735.96 → 2736.34] guess in
[2736.34 → 2736.84] the NLP
[2736.84 → 2737.50] case, we're
[2737.50 → 2738.04] talking about
[2738.04 → 2739.08] like word
[2739.08 → 2739.84] embeddings and
[2739.84 → 2740.26] things like
[2740.26 → 2740.46] that.
[2740.62 → 2740.88] Exactly.
[2741.08 → 2741.52] Is it a
[2741.52 → 2742.26] similar idea?
[2742.44 → 2743.10] Yeah, precisely.
[2743.32 → 2744.06] Word embeddings is
[2744.06 → 2744.96] a perfect example.
[2745.08 → 2745.66] So you may have
[2745.66 → 2746.36] heard of the
[2746.36 → 2747.24] simple arithmetic
[2747.24 → 2748.40] that we can
[2748.40 → 2749.22] perform on
[2749.22 → 2750.30] word embeddings
[2750.30 → 2752.18] to demonstrate
[2752.18 → 2752.66] that the
[2752.66 → 2753.88] machines or the
[2753.88 → 2754.60] neural networks
[2754.60 → 2755.72] develop a very
[2755.72 → 2756.96] complex internal
[2756.96 → 2758.42] understanding of
[2758.42 → 2759.18] the semantics
[2759.18 → 2759.82] of the human
[2759.82 → 2760.30] language.
[2760.88 → 2761.52] So for instance,
[2761.64 → 2762.18] you can take the
[2762.18 → 2762.98] embedding or the
[2762.98 → 2763.98] vector that
[2763.98 → 2764.80] describes the
[2764.80 → 2765.44] word king,
[2766.02 → 2766.42] you can
[2766.42 → 2767.48] subtract, like
[2767.48 → 2768.32] pure arithmetic,
[2768.74 → 2769.44] the word man,
[2770.02 → 2770.84] and then you can
[2770.84 → 2771.60] add the word
[2771.60 → 2773.06] woman, and the
[2773.06 → 2773.84] resulting vector
[2773.84 → 2774.36] is going to be
[2774.36 → 2775.24] very close to the
[2775.24 → 2775.96] vector for the
[2775.96 → 2777.02] word queen,
[2777.52 → 2778.16] which again, we
[2778.16 → 2779.36] take king,
[2779.48 → 2780.64] which is male
[2780.64 → 2781.88] royalty, you
[2781.88 → 2782.62] subtract the
[2782.62 → 2783.22] word from man,
[2783.66 → 2784.42] you add woman,
[2784.64 → 2785.40] and then you end
[2785.40 → 2785.96] up with female
[2785.96 → 2786.58] royalty.
[2786.96 → 2787.98] Which is queen.
[2788.74 → 2789.72] And what Gantt
[2789.72 → 2790.12] have been
[2790.12 → 2791.22] demonstrated to
[2791.22 → 2792.44] do is that you
[2792.44 → 2793.44] can perform the
[2793.44 → 2794.20] same kind of
[2794.20 → 2796.06] arithmetic on
[2796.06 → 2796.70] images.
[2797.48 → 2798.44] And it's really
[2798.44 → 2798.98] fascinating.
[2799.16 → 2799.54] So when you
[2799.54 → 2800.42] take the example
[2800.42 → 2801.88] that was published
[2801.88 → 2803.90] in 2015, so
[2803.90 → 2805.44] very early on in
[2805.44 → 2806.32] the short history
[2806.32 → 2806.92] that Gantt have
[2806.92 → 2808.18] been around, you
[2808.18 → 2809.36] have an image of
[2809.36 → 2810.14] a man with
[2810.14 → 2812.36] sunglasses, you
[2812.36 → 2813.64] subtract an image
[2813.64 → 2814.86] of a man, you
[2814.86 → 2815.70] add an image of
[2815.70 → 2816.94] a female, and
[2816.94 → 2817.94] the out coming
[2817.94 → 2818.78] image is a
[2818.78 → 2819.22] female with
[2819.22 → 2819.68] sunglasses.
[2820.68 → 2821.48] So you can
[2821.48 → 2822.10] perform
[2822.10 → 2823.38] arithmetic, and
[2823.38 → 2824.70] this is completely
[2824.70 → 2825.52] unsupervised, this
[2825.52 → 2826.84] is just based on
[2826.84 → 2827.80] the internal
[2827.80 → 2828.94] representations of
[2828.94 → 2829.62] this extremely
[2829.62 → 2830.68] complex space, that
[2830.68 → 2832.44] is images, that
[2832.44 → 2833.48] you can then
[2833.48 → 2834.66] perform again like
[2834.66 → 2835.72] something intuitive
[2835.72 → 2836.78] as arithmetic, and
[2836.78 → 2837.78] then the computer,
[2838.04 → 2839.02] without being told
[2839.02 → 2839.60] what the correct
[2839.60 → 2841.16] answer is, would
[2841.16 → 2842.00] come up with an
[2842.00 → 2843.10] answer that a
[2843.10 → 2843.98] human would, based
[2843.98 → 2844.68] on our intuitive
[2844.68 → 2845.78] understanding of
[2845.78 → 2847.14] what, quote-unquote
[2847.14 → 2848.02] arithmetic on
[2848.02 → 2848.70] images should
[2848.70 → 2849.22] produce.
[2849.72 → 2850.80] Just as a quick
[2850.80 → 2851.38] interjection, with
[2851.38 → 2852.48] that arithmetic as
[2852.48 → 2853.06] you're describing
[2853.06 → 2853.96] it, I mean, doing
[2853.96 → 2855.22] that on imagery, on
[2855.22 → 2856.28] video, I mean, that
[2856.28 → 2858.08] is a deepfake at the
[2858.08 → 2858.76] end of the day, just
[2858.76 → 2859.74] to kind of tie two
[2859.74 → 2860.80] terms together, or
[2860.80 → 2861.32] am I wrong?
[2862.02 → 2863.74] Yes, it works on the
[2863.74 → 2865.34] same principle, I'm
[2865.34 → 2866.26] not sure if deepfake
[2866.26 → 2867.56] works, deepfake might
[2867.56 → 2868.60] actually work more on
[2868.60 → 2869.40] the principle for
[2869.40 → 2870.18] Cycleway that
[2870.18 → 2871.18] Jacob was talking
[2871.18 → 2872.02] around previously,
[2872.68 → 2874.60] but deepfakes, vast
[2874.60 → 2875.88] majority of them are
[2875.88 → 2877.32] based in one way or
[2877.32 → 2878.78] another on GANs, and
[2878.78 → 2879.74] it is exactly, it's
[2879.74 → 2880.94] essentially modifying
[2880.94 → 2882.38] an image in a
[2882.38 → 2883.46] believable way so
[2883.46 → 2884.40] that it looks like
[2884.40 → 2885.44] something else, and
[2885.44 → 2886.54] this is also at the
[2886.54 → 2887.76] core of the
[2887.76 → 2889.14] applications that I
[2889.14 → 2890.08] alluded to earlier,
[2890.08 → 2890.92] as in the Face
[2890.92 → 2892.90] app, which you take a
[2892.90 → 2894.34] selfie, and you can
[2894.34 → 2895.16] immediately make
[2895.16 → 2896.10] yourself look older,
[2896.84 → 2898.06] so it's translating
[2898.06 → 2899.14] yourself into an
[2899.14 → 2899.98] older version of
[2899.98 → 2901.20] yourself, and
[2901.20 → 2901.92] things like that.
[2902.48 → 2902.96] Yeah, I can do
[2902.96 → 2903.52] without the older
[2903.52 → 2904.30] version because that's
[2904.30 → 2904.84] already happening
[2904.84 → 2905.64] quick enough anyway.
[2906.00 → 2906.82] Yeah, exactly, who
[2906.82 → 2907.26] would, who would,
[2907.36 → 2908.80] right, just like, just
[2908.80 → 2909.60] wait a little bit, but
[2909.60 → 2910.60] what's fascinating is
[2910.60 → 2911.60] that the older version
[2911.60 → 2912.94] is like the perfect
[2912.94 → 2914.12] example of something
[2914.12 → 2915.14] where machines just
[2915.14 → 2916.08] cannot have the data,
[2916.96 → 2917.96] because you would
[2917.96 → 2919.04] have to literally wait
[2919.04 → 2920.24] 50 years for people
[2920.24 → 2922.00] to get older and
[2922.00 → 2923.16] have images of them
[2923.16 → 2924.56] so that you can train
[2924.56 → 2925.86] it in a proper or
[2925.86 → 2926.86] supervised way, as
[2926.86 → 2928.02] in like bad
[2928.02 → 2929.20] examples of like, this
[2929.20 → 2930.08] is what this person
[2930.08 → 2931.46] looks like young, and
[2931.46 → 2932.08] this is what this
[2932.08 → 2933.14] person looks like when
[2933.14 → 2933.98] they are 70 years
[2933.98 → 2934.30] old.
[2934.80 → 2935.78] That's effectively
[2935.78 → 2937.00] impossible to get
[2937.00 → 2938.70] unless you get
[2938.70 → 2940.94] clever, which, you
[2940.94 → 2941.68] know, these generative
[2941.68 → 2943.22] models have been
[2943.22 → 2944.68] extremely helpful
[2944.68 → 2944.96] with.
[2944.96 → 2946.46] Yeah, and since Chris
[2946.46 → 2947.22] went there, I didn't
[2947.22 → 2947.64] go there.
[2947.80 → 2948.44] I don't want to say
[2948.44 → 2949.28] anything bad about
[2949.28 → 2950.74] GANs, but since Chris
[2950.74 → 2951.86] brought up the idea of
[2951.86 → 2953.00] deep fakes and all
[2953.00 → 2954.28] that, that people are
[2954.28 → 2955.96] concerned about, thanks
[2955.96 → 2956.76] for explaining that,
[2956.84 → 2959.76] you know, how GANs are
[2959.76 → 2961.14] particularly well-suited
[2961.14 → 2962.72] for this sort of task
[2962.72 → 2964.78] because they develop
[2964.78 → 2965.94] this deep understanding
[2965.94 → 2968.12] of a deep representation
[2968.12 → 2970.16] of these images and
[2970.16 → 2971.42] features and different
[2971.42 → 2971.92] things that are
[2971.92 → 2972.30] important.
[2972.30 → 2973.56] You know, people put a
[2973.56 → 2974.54] lot of focus on that
[2974.54 → 2976.40] deep fake stuff, and
[2976.40 → 2977.38] you've mentioned a
[2977.38 → 2978.12] bunch of other
[2978.12 → 2979.42] applications, but from
[2979.42 → 2980.98] your perspective, I
[2980.98 → 2981.70] guess, do you think
[2981.70 → 2983.58] that there are a lot
[2983.58 → 2985.40] of good examples of
[2985.40 → 2986.76] positive examples of
[2986.76 → 2988.20] GAN usage out there,
[2988.20 → 2989.46] or are you concerned
[2989.46 → 2990.90] at all that the deep
[2990.90 → 2992.26] fake stuff and, you
[2992.26 → 2993.02] know, obviously, that's
[2993.02 → 2994.14] what gets retweeted a
[2994.14 → 2995.08] lot on Twitter and
[2995.08 → 2996.12] blogs and all that.
[2996.36 → 2997.26] Are you concerned that
[2997.26 → 2999.02] that's kind of overwhelming
[2999.02 → 3000.52] the attention around GANs
[3000.52 → 3001.28] when there's a lot of
[3001.28 → 3003.12] good uses of them?
[3003.74 → 3005.56] So, yeah, so I would
[3005.56 → 3006.66] like to kind of set a
[3006.66 → 3007.28] couple of things
[3007.28 → 3007.60] straight.
[3007.84 → 3008.82] So, first,
[3009.06 → 3010.10] like, so this is a
[3010.10 → 3011.16] super important topic,
[3011.28 → 3011.42] right?
[3011.50 → 3012.68] Like, and I think
[3012.68 → 3013.92] there's a reason we,
[3014.06 → 3014.86] like, that was part of
[3014.86 → 3015.68] the motivation why we
[3015.68 → 3016.86] wanted to include at
[3016.86 → 3017.66] least, like, a short
[3017.66 → 3020.18] ethics section in the
[3020.18 → 3021.60] book, but because
[3021.60 → 3022.66] obviously we understand
[3022.66 → 3024.00] at the same time that
[3024.00 → 3026.30] people don't, it's not a
[3026.30 → 3027.32] book about ethics,
[3027.32 → 3027.58] right?
[3028.18 → 3030.72] But I also want to
[3030.72 → 3031.72] highlight one thing,
[3031.76 → 3032.90] which is that the
[3032.90 → 3034.20] original deep fake
[3034.20 → 3036.06] algorithm and quite a
[3036.06 → 3037.38] few of them more
[3037.38 → 3038.22] successful are not
[3038.22 → 3039.12] actually AI-based.
[3039.42 → 3040.20] There are other
[3040.20 → 3040.66] techniques.
[3040.78 → 3041.38] So I just want to,
[3041.38 → 3043.12] like, equate the two
[3043.12 → 3043.58] terms.
[3044.18 → 3045.58] So, you know, GANs are
[3045.58 → 3046.92] one of the ways to do
[3046.92 → 3047.56] deep fakes.
[3048.02 → 3050.08] And, in fact, like, so
[3050.08 → 3051.68] there's a London-based
[3051.68 → 3053.54] startup that I know
[3053.54 → 3054.56] some of the researchers
[3054.56 → 3056.16] from called Synthesia,
[3056.16 → 3057.94] which kind of uses this
[3057.94 → 3059.90] mixture of several
[3059.90 → 3061.26] techniques, including
[3061.26 → 3063.32] GANs, as a way to
[3063.32 → 3064.76] sort of reanimate faces
[3064.76 → 3066.94] and sort of do a more
[3066.94 → 3068.48] realistic dubbing.
[3068.76 → 3070.16] So, effectively, when
[3070.16 → 3071.38] you have a movie that's
[3071.38 → 3073.88] in English and then you
[3073.88 → 3075.60] want to port it over to,
[3075.68 → 3076.58] I don't know, Chinese
[3076.58 → 3077.80] market, Russian market,
[3078.04 → 3079.30] or, you know, like any
[3079.30 → 3081.30] other country, just if
[3081.30 → 3082.32] you dub, obviously, you
[3082.32 → 3083.34] can sometimes see that
[3083.34 → 3084.20] that's not what the
[3084.20 → 3084.98] people are saying.
[3084.98 → 3086.66] So they have kind of
[3086.66 → 3088.44] been applying this in
[3088.44 → 3089.92] the movie space to
[3089.92 → 3092.08] basically make, improve
[3092.08 → 3093.04] the experience for
[3093.04 → 3093.84] moviegoers.
[3094.16 → 3095.20] And I think, you know,
[3095.28 → 3096.24] that there are obviously
[3096.24 → 3097.56] many positive
[3097.56 → 3098.96] applications, even of
[3098.96 → 3100.10] deep fakes, but as
[3100.10 → 3100.86] overall, as a
[3100.86 → 3101.70] technology, whether
[3101.70 → 3102.56] that's a net positive
[3102.56 → 3103.96] or a negative, I
[3103.96 → 3104.76] don't know.
[3105.22 → 3106.12] What I would say,
[3106.22 → 3107.92] though, is that I
[3107.92 → 3108.72] think, you know,
[3109.22 → 3111.16] Photoshop and other
[3111.16 → 3112.64] manipulation tools like
[3112.64 → 3114.20] After Effects have been
[3114.20 → 3115.98] around for at least a
[3115.98 → 3117.22] decade, maybe two.
[3117.68 → 3120.80] And realistically, you
[3120.80 → 3121.68] know, and when you look
[3121.68 → 3123.50] at where people can do a
[3123.50 → 3124.56] lot of damage with
[3124.56 → 3126.14] misinformation, it starts
[3126.14 → 3127.28] already with something
[3127.28 → 3128.56] much simpler, right?
[3128.60 → 3130.04] Like things like articles
[3130.04 → 3131.60] or text, right?
[3131.78 → 3133.98] The GPT-2 and from
[3133.98 → 3135.14] OpenAI and that sort of
[3135.14 → 3135.86] thing, right?
[3136.04 → 3137.60] There's a lot of stuff
[3137.60 → 3138.58] in between.
[3139.54 → 3141.44] And I think it's a
[3141.44 → 3143.26] really important debate
[3143.26 → 3144.66] around like, do we
[3144.66 → 3145.94] want to, how do we
[3145.94 → 3146.74] want to approach it?
[3146.80 → 3148.02] Because, of course,
[3148.16 → 3148.94] like you can't
[3148.94 → 3150.88] unintent any piece of
[3150.88 → 3151.46] technology.
[3152.28 → 3153.76] And you could,
[3155.04 → 3156.64] even guardrails that
[3156.64 → 3157.68] you set around them,
[3157.72 → 3158.86] I think are potentially
[3158.86 → 3161.52] problematic because you
[3161.52 → 3162.66] set those guardrails.
[3163.08 → 3164.22] In almost any way,
[3164.36 → 3165.28] there will be some
[3165.28 → 3166.32] edge cases they'll fall
[3166.32 → 3168.78] outside, and then you'll
[3168.78 → 3171.94] use cases where, or
[3171.94 → 3173.20] cases where people will
[3173.20 → 3175.26] just get fooled by, by
[3175.26 → 3176.60] something because
[3176.60 → 3177.32] normally they're
[3177.32 → 3177.74] protected.
[3177.96 → 3178.88] So I think the typical
[3178.88 → 3180.12] example being like the
[3180.12 → 3181.54] platforms trying to do
[3181.54 → 3182.22] the policing.
[3182.50 → 3183.96] I think it's, it's a
[3183.96 → 3185.66] very long and complicated
[3185.66 → 3187.18] debate about, you know,
[3187.24 → 3188.74] what the boundaries
[3188.74 → 3190.12] around that should be.
[3190.34 → 3191.64] So I'll leave it fairly
[3191.64 → 3193.46] high level, but that's
[3193.46 → 3194.30] my take on it.
[3194.78 → 3196.08] Yeah, I think that's a
[3196.08 → 3197.02] great take.
[3197.08 → 3197.76] And I think it gives
[3197.76 → 3199.08] people a lot to think
[3199.08 → 3199.34] about.
[3199.44 → 3200.98] Of course, with a lot of
[3200.98 → 3202.18] things with AI, I think
[3202.18 → 3203.42] there's important ethics
[3203.42 → 3204.82] things to consider.
[3205.28 → 3206.90] But at the same time, I
[3206.90 → 3208.16] don't think it's worth
[3208.16 → 3209.52] writing off specific
[3209.52 → 3211.12] techniques as, you know,
[3211.24 → 3212.36] blacklisted or something
[3212.36 → 3213.68] because they could be used
[3213.68 → 3214.30] in a certain way.
[3214.40 → 3215.56] I remember, I think,
[3215.64 → 3216.88] Chris, maybe you remember,
[3217.00 → 3218.64] but I'm pretty sure at some
[3218.64 → 3219.38] point during our
[3219.38 → 3220.36] conversations, it was
[3220.36 → 3221.58] brought up that, you
[3221.58 → 3223.08] know, GANs are, there
[3223.08 → 3225.04] are quite a few really,
[3225.18 → 3226.90] really positive uses
[3226.90 → 3229.22] of them, like in a
[3229.22 → 3230.32] social good sense as
[3230.32 → 3231.98] well in terms of, I
[3231.98 → 3233.22] think that there was one
[3233.22 → 3234.36] I saw where they were
[3234.36 → 3235.96] generating, like
[3235.96 → 3237.50] augmenting tumour
[3237.50 → 3239.48] imagery data sets to
[3239.48 → 3240.74] help actually train
[3240.74 → 3242.26] tumour detection
[3242.26 → 3244.06] algorithms because that
[3244.06 → 3244.94] data is obviously,
[3245.46 → 3246.66] there's privacy concerns,
[3246.66 → 3247.92] but it's also fairly
[3247.92 → 3249.92] scarce and hard to
[3249.92 → 3251.02] supervise that sort of
[3251.02 → 3252.42] things. So I think that
[3252.42 → 3253.90] there are, you know,
[3254.14 → 3255.74] and I'm sure you guys
[3255.74 → 3257.22] have better insight into
[3257.22 → 3257.98] this, but there are a
[3257.98 → 3258.96] lot of positive use
[3258.96 → 3259.60] cases, right?
[3259.84 → 3260.86] You know, just before
[3260.86 → 3261.72] you guys jump in, I
[3261.72 → 3262.62] remember when we talked
[3262.62 → 3263.86] about deep fakes some
[3263.86 → 3265.36] episodes back, we had a
[3265.36 → 3266.70] lot of people in the
[3266.70 → 3268.06] audience come back at us
[3268.06 → 3268.84] and say, you know, hey
[3268.84 → 3269.94] guys, I recognize you
[3269.94 → 3271.08] were being a little bit,
[3271.26 → 3272.78] you know, dark in that
[3272.78 → 3273.50] and we had acknowledged
[3273.50 → 3274.72] that, but a lot of
[3274.72 → 3275.62] people came back talking
[3275.62 → 3276.58] about good uses and I
[3276.58 → 3277.14] just wanted to kind of
[3277.14 → 3278.02] call that out. And
[3278.02 → 3279.24] sorry, Vlad, I think
[3279.24 → 3280.00] you were starting to
[3280.00 → 3280.16] talk.
[3280.16 → 3280.88] Yeah, no, I was
[3280.88 → 3281.60] saying absolutely
[3281.60 → 3283.22] like medical space.
[3283.38 → 3283.98] I think it's a great
[3283.98 → 3285.06] example to bring up
[3285.06 → 3287.00] where again, augmented
[3287.00 → 3288.36] data sets can be
[3288.36 → 3289.80] tremendously useful in
[3289.80 → 3291.70] unlocking diagnostic
[3291.70 → 3293.76] applications where
[3293.76 → 3294.80] previously there just
[3294.80 → 3295.66] wasn't a sufficient
[3295.66 → 3297.30] enough data set.
[3297.44 → 3299.00] Awesome. Well, we've
[3299.00 → 3299.94] had a lot of great
[3299.94 → 3300.84] conversation here. I
[3300.84 → 3301.70] know I've learned a
[3301.70 → 3303.38] lot and obviously we
[3303.38 → 3305.18] will link your book in
[3305.18 → 3306.10] our show notes so
[3306.10 → 3307.08] people can find it
[3307.08 → 3307.80] GANs in action.
[3307.80 → 3309.42] And that I'm sure is a
[3309.42 → 3310.66] great place to start in
[3310.66 → 3312.48] terms of getting to
[3312.48 → 3314.06] know about these
[3314.06 → 3315.08] subjects in a lot more
[3315.08 → 3316.42] detail. But I was
[3316.42 → 3317.88] wondering also if, you
[3317.88 → 3318.96] know, maybe to close us
[3318.96 → 3320.60] out, if you both have
[3320.60 → 3323.32] any insight into, you
[3323.32 → 3324.68] know, where's the best
[3324.68 → 3326.76] place for people to jump
[3326.76 → 3328.60] into this subject in
[3328.60 → 3330.40] terms of maybe like
[3330.40 → 3332.10] certain frameworks that
[3332.10 → 3333.16] are easier to work with
[3333.16 → 3334.72] GANs than others or
[3334.72 → 3335.96] maybe it's like certain
[3335.96 → 3338.42] example tutorials or
[3338.42 → 3340.66] problems or tasks that
[3340.66 → 3342.04] would be a good place to
[3342.04 → 3343.68] start and jump in and
[3343.68 → 3344.52] experiment and get
[3344.52 → 3345.74] hands on. What are your
[3345.74 → 3346.40] thoughts for our
[3346.40 → 3347.16] listeners that are
[3347.16 → 3347.90] interested in that?
[3348.60 → 3349.38] Yeah, so we might be a
[3349.38 → 3350.36] little biased. Yeah,
[3350.46 → 3351.76] here, but yeah, we
[3351.76 → 3352.34] might be a little biased
[3352.34 → 3353.10] but I let Jacob
[3353.10 → 3353.54] comment.
[3354.08 → 3355.16] Oh, yeah. Well, so I
[3355.16 → 3356.74] think I'll try to
[3356.74 → 3357.52] provide like one
[3357.52 → 3358.68] example for each,
[3358.76 → 3359.98] right? So obviously,
[3360.34 → 3361.40] like I think keeping up
[3361.40 → 3362.26] to date with what's
[3362.26 → 3363.32] latest, I think Twitter
[3363.32 → 3364.04] and following the
[3364.04 → 3365.18] right researcher as
[3365.18 → 3366.24] the best way. In
[3366.24 → 3368.12] terms of like frameworks
[3368.12 → 3369.56] that are easier
[3369.56 → 3371.00] generally, I mean, I
[3371.00 → 3372.72] have not had extensive
[3372.72 → 3373.48] experience with
[3373.48 → 3374.88] TensorFlow 2.0, but I
[3374.88 → 3377.46] find PyTorch to be a
[3377.46 → 3379.00] lot easier to work
[3379.00 → 3379.86] with, especially for
[3379.86 → 3380.74] GANs because there's a
[3380.74 → 3381.36] lot of complicated
[3381.36 → 3382.18] things that are going
[3382.18 → 3384.30] on, and it's easier to
[3384.30 → 3385.68] kind of dive into the
[3385.68 → 3386.46] internals. So I
[3386.46 → 3388.90] generally kind of tend
[3388.90 → 3391.22] to prefer PyTorch over
[3391.22 → 3393.12] TensorFlow these days.
[3393.32 → 3394.04] And I think, you
[3394.04 → 3394.70] know, I think it's
[3394.70 → 3395.38] especially with the
[3395.38 → 3396.12] latest improvements
[3396.12 → 3397.00] that Facebook's making
[3397.00 → 3397.98] into PyTorch, I
[3397.98 → 3399.58] think there's a lot
[3399.58 → 3400.48] of things that are
[3400.48 → 3401.90] picking up, especially
[3401.90 → 3402.94] amongst the research
[3402.94 → 3403.84] community, which is
[3403.84 → 3405.22] kind of where I live
[3405.22 → 3406.60] right now, like in the
[3406.60 → 3407.92] bridge between like the
[3407.92 → 3408.96] research and industry.
[3409.42 → 3411.06] So it's good. And I
[3411.06 → 3412.52] would say that I think
[3412.52 → 3413.96] in terms of the types
[3413.96 → 3415.68] of networks that are
[3415.68 → 3417.36] most tried and tested,
[3417.90 → 3419.38] I think like DUGAN,
[3419.62 → 3421.68] Cycleway, yeah, those
[3421.68 → 3423.00] would be like the like
[3423.00 → 3424.02] Style obviously
[3424.02 → 3426.26] actually is, those
[3426.26 → 3426.94] would be like the
[3426.94 → 3428.52] three bases that I
[3428.52 → 3428.98] think are really
[3428.98 → 3430.06] important to understand.
[3430.26 → 3431.20] But of course, like
[3431.20 → 3432.16] it's a massive field.
[3432.58 → 3433.66] So I think having like
[3433.66 → 3434.24] a comprehensive
[3434.24 → 3435.60] resource, you know,
[3435.66 → 3436.80] like our book is, it
[3436.80 → 3437.82] could be really useful
[3437.82 → 3439.98] as a sort of map to
[3439.98 → 3440.92] get these, get your
[3440.92 → 3441.96] head wrapped around
[3441.96 → 3443.22] it because there's much
[3443.22 → 3445.50] more than I can say in
[3445.50 → 3446.00] this case.
[3446.62 → 3447.56] But yeah, hopefully
[3447.56 → 3448.58] that's good.
[3448.58 → 3449.50] Awesome.
[3450.08 → 3450.64] That's great.
[3450.74 → 3451.70] I think it gives a lot
[3451.70 → 3452.54] of good perspective
[3452.54 → 3453.74] because people want to
[3453.74 → 3454.76] start poking around
[3454.76 → 3456.08] and I encourage people
[3456.08 → 3457.42] to get the book and
[3457.42 → 3458.72] dig in to this subject
[3458.72 → 3460.34] and work on good
[3460.34 → 3461.90] positive examples that
[3461.90 → 3462.88] can, you know, help
[3462.88 → 3463.92] demonstrate this
[3463.92 → 3464.48] technology.
[3464.98 → 3465.94] We certainly thank
[3465.94 → 3466.56] both of you.
[3466.66 → 3467.32] Thank you for taking
[3467.32 → 3468.36] time out of your busy
[3468.36 → 3469.86] schedules to help us
[3469.86 → 3470.84] parse through this
[3470.84 → 3472.22] subject, which is a
[3472.22 → 3473.06] complicated one and
[3473.06 → 3473.74] there's a lot there.
[3473.86 → 3475.02] So I'm glad that we
[3475.02 → 3476.42] had you both on here
[3476.42 → 3477.86] to help us parse
[3477.86 → 3478.28] through it.
[3478.34 → 3479.08] I really appreciate
[3479.08 → 3480.38] it and hope we can
[3480.38 → 3481.24] meet sometime.
[3481.48 → 3482.08] Yeah, no, absolutely.
[3482.24 → 3482.86] Thank you for having
[3482.86 → 3483.12] us.
[3483.48 → 3484.06] Thank you so much.
[3485.84 → 3486.30] All right.
[3486.34 → 3486.94] Thank you for tuning
[3486.94 → 3488.38] into this episode of
[3488.38 → 3488.98] Practical AI.
[3489.24 → 3489.82] If you enjoyed this
[3489.82 → 3490.70] show, do us a favour,
[3490.82 → 3491.76] go on iTunes, give us
[3491.76 → 3492.78] a rating, go in your
[3492.78 → 3493.80] podcast app and
[3493.80 → 3494.34] favourite it.
[3494.46 → 3495.24] If you are on Twitter
[3495.24 → 3496.16] or a social network,
[3496.26 → 3496.94] share a link with a
[3496.94 → 3497.48] friend, whatever you
[3497.48 → 3498.42] got to do, share the
[3498.42 → 3499.00] show with a friend if
[3499.00 → 3499.60] you enjoyed it.
[3499.90 → 3500.56] And bandwidth for
[3500.56 → 3501.76] Changelog is provided
[3501.76 → 3502.56] by Vastly.
[3502.68 → 3503.24] Learn more at
[3503.24 → 3504.64] fastly.com and we
[3504.64 → 3505.54] catch our errors before
[3505.54 → 3506.36] our users do here at
[3506.36 → 3507.10] Changelog because of
[3507.10 → 3507.52] Rollbar.
[3507.52 → 3508.62] Check them out at
[3508.62 → 3509.44] Rollbar.com slash
[3509.44 → 3510.12] Changelog.
[3510.44 → 3511.64] And we're hosted on
[3511.64 → 3512.94] Linde cloud servers.
[3513.28 → 3514.06] Head to Linode.com
[3514.06 → 3514.90] slash Changelog.
[3514.98 → 3515.44] Check them out.
[3515.52 → 3516.36] Support this show.
[3516.76 → 3518.06] This episode is hosted
[3518.06 → 3519.38] by Daniel Whiten ack and
[3519.38 → 3519.96] Chris Benson.
[3520.40 → 3521.42] The music is by
[3521.42 → 3522.46] Break master Cylinder.
[3522.84 → 3523.66] And you can find more
[3523.66 → 3525.12] shows just like this at
[3525.12 → 3526.28] ChangeLog.com.
[3526.36 → 3527.42] When you go there, pop
[3527.42 → 3528.42] in your email address,
[3528.70 → 3529.62] get our weekly email
[3529.62 → 3530.48] keeping you up to date
[3530.48 → 3531.48] with the news and
[3531.48 → 3532.56] podcasts for developers
[3532.56 → 3534.14] in your inbox every
[3534.14 → 3534.74] single week.
[3535.12 → 3535.90] Thanks for tuning in.
[3535.90 → 3536.82] We'll see you next week.
[3537.52 → 3537.98] Bye.
[3538.06 → 3538.14] Bye.
[3538.18 → 3538.68] Bye.
[3538.76 → 3538.80] Bye.
[3538.84 → 3538.96] Bye.
[3541.14 → 3541.78] Bye.
[3541.90 → 3542.00] Bye.
[3546.06 → 3546.28] Bye.
[3546.90 → 3548.14] Bye.
[3548.14 → 3548.54] Bye.
[3548.80 → 3550.98] Bye.
[3550.98 → 3551.36] Bye.
[3551.46 → 3553.44] Bye.
