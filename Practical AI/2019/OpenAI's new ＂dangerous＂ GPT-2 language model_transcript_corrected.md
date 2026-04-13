[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.24] And we're hosted on Linde cloud servers.
[12.74 → 14.74] Head to linode.com slash changelog.
[15.36 → 18.62] This episode is brought to you by Linde, our cloud server of choice.
[18.82 → 21.88] And we're excited to share they've recently launched dedicated CPU instances.
[21.88 → 38.78] If you have build boxes, CI, CD, video encoding, machine learning, game servers, databases, data mining, or application servers that need to be full duty, 100% CPU all day, every day, then check out Linde's dedicated CPU instances.
[39.34 → 43.44] These instances are fully dedicated and shared with no one else.
[43.52 → 47.46] So there's no CPU steal or competing for these resources with other Li nodes.
[47.72 → 51.40] Pricing is very competitive and starts out at 30 bucks a month.
[51.40 → 55.60] Learn more and get started at linode.com slash changelog.
[55.70 → 57.82] Again, linode.com slash changelog.
[68.68 → 76.22] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical, productive, and accessible to everyone.
[76.22 → 81.10] This is where conversations around AI, machine learning, and data science happen.
[81.40 → 85.88] Join the community and snag with us around various topics of the show at changelog.com slash community.
[86.10 → 87.04] Follow us on Twitter.
[87.14 → 88.64] We're at Practical AI FM.
[88.82 → 89.96] And now onto the show.
[89.96 → 101.36] Welcome to another fully connected episode where Daniel and I keep you connected with everything that's going on in the AI community.
[101.50 → 108.30] We'll take some time to discuss the latest AI news, and we'll dig into some learning resources to help you level up on your machine learning game.
[108.30 → 111.00] I am your co-host, Chris Benson.
[111.20 → 115.20] I'm Chief AI Strategist at Lockheed Martin RMS APA Innovations.
[115.44 → 120.70] And with me is my co-host, Daniel Whiten ack, who is a data scientist with SIL International.
[120.86 → 121.50] How's it going, Daniel?
[121.92 → 122.84] It's going great.
[123.10 → 124.82] Welcome back from Switzerland.
[124.82 → 136.08] So as our listeners will know, Chris has been recording practical AI episodes on the road at Applied Machine Learning Days and really been enjoying those.
[136.44 → 138.00] But glad to have you back from your trip.
[138.30 → 139.10] It was good to be back.
[139.16 → 139.96] It was a great trip.
[140.22 → 144.22] I met a lot of fascinating people and obviously recorded some good episodes.
[144.68 → 146.10] I did my talk.
[146.18 → 150.82] Just for the listeners, Daniel ran the AI for Good track remotely from America.
[150.82 → 153.54] And it actually went off without a hitch.
[153.72 → 155.64] Everybody felt I was talking to the other speakers.
[155.74 → 156.26] There was no problem.
[156.36 → 160.46] So thank you very much, Daniel, for managing that from thousands of miles away.
[161.44 → 163.74] Yeah, that was kind of an interesting experience.
[163.86 → 166.24] I had planned to be there, but I'm glad to hear that.
[166.50 → 170.62] I was hoping that all AI people would just kind of converge there as expected.
[170.80 → 172.68] And it sounds like that's what happened.
[172.88 → 177.22] So if you don't know about Applied Machine Learning Days, definitely check that out.
[177.30 → 178.58] It's a great conference.
[178.58 → 184.86] And we've had recently some guests on talking about AI for Good and other things.
[184.96 → 186.74] And that's been really awesome.
[187.02 → 191.22] But now that we're here together again, we have a fully connected episode.
[192.10 → 193.94] And I'm really excited today.
[194.10 → 199.16] Of course, if you haven't been hiding under a rock, and you follow AI stuff,
[199.16 → 205.92] then pretty much all you've been hearing about for a couple of weeks or however long it's been
[205.92 → 211.96] is OpenAI's recent language model that they've released called GPT-2.
[212.18 → 216.54] We're going to kind of talk through some of that stuff today because it's pretty interesting.
[216.66 → 218.50] Have you been seeing that online, Chris?
[218.50 → 225.42] Yeah, it's hard to miss, especially, you know, like I think the very first thing I saw was Elon Musk's tweet about,
[225.86 → 226.66] you know, we have a model.
[226.88 → 227.08] I forget.
[227.18 → 232.32] I'm not quoting, but something about we have a model that's so amazingly good that it's dangerous.
[232.32 → 234.98] And thus, we have to not release the whole thing.
[234.98 → 241.18] And obviously, like everybody else on the planet, that piqued my interest and started diving into it.
[241.42 → 244.34] And it's, you know, technically, it's fascinating what they've done.
[244.70 → 249.34] And then there's some pretty interesting ways that they've chosen to not only approach the model,
[249.44 → 251.64] but approach the release of it.
[251.90 → 253.50] You know, a little bit of drama around it here.
[253.94 → 254.66] Yeah, definitely.
[254.84 → 259.98] You know, I've seen things that are like, of course, people have been kind of captivated
[259.98 → 265.08] because one of the things that they're doing with this model is text generation,
[265.30 → 266.94] which we'll kind of talk through in a second.
[267.12 → 269.90] But the quality of it is just astounding, really.
[270.34 → 274.84] And people have been posting like different things, like they've generated, you know,
[274.92 → 279.66] reviews for their book or like various stories and other things.
[279.66 → 284.80] And they're kind of entertaining, but all of them are pretty astounding in the quality of the text generation,
[284.98 → 288.54] which also, of course, leads a lot of people to be concerned
[288.54 → 293.82] because, you know, how do we know if this text has been generated by an AI or not?
[293.86 → 295.34] And what are the implications of that?
[295.42 → 299.24] And so, you know, Wired had this article about like, you know,
[299.28 → 302.76] the AI that was too dangerous to release based on, like you were saying,
[302.82 → 307.28] some of what Musk and OpenAI has talked about.
[307.28 → 310.80] So it's really been an interesting discussion.
[311.24 → 311.56] I don't know.
[311.72 → 316.86] I've seen some people kind of get frustrated with all of this talk about the danger of AI,
[316.86 → 319.46] which we can get into a little bit later.
[319.66 → 325.46] But what's your general feeling about this discussion kind of generally, Chris?
[325.54 → 326.92] Is it positive, negative?
[327.58 → 328.30] A bit of both.
[328.38 → 332.18] I think it is the reality that we are moving into either way.
[332.36 → 335.80] So regardless of how you spin it or how you perceive it,
[336.06 → 338.00] we are in a moment here where, you know,
[338.00 → 348.82] we're seeing this GPT-2 model that is able to make people believe that what the text is generated is indistinguishable from humans.
[349.02 → 352.08] If you, you know, they put the text in front of a number of people.
[352.24 → 355.78] And then on top of that, just as a side thing not to get into right now,
[356.04 → 360.56] there's been the, you know, all the facial stuff that I was also seeing in the news over the last couple of weeks
[360.56 → 363.92] where there's the website where you can just hit refresh over and over again
[363.92 → 366.84] and a new person that does not exist in real life is generated by a GAN.
[366.84 → 367.04] Oh, yeah, I've seen that too.
[367.38 → 373.16] And the reason I mentioned that is we're just moving into a moment where it is now entirely practical
[373.16 → 378.94] for these AI models to be able to generate things that are indistinguishable from, you know,
[378.96 → 380.60] the reality that we are otherwise in.
[380.78 → 384.28] So I guess to kick things off, you know, do you want to, you know,
[384.30 → 389.04] maybe even back up just a little bit before we dive in and kind of talk about what a language model is?
[389.04 → 395.26] Uh, yeah, sure. So this GPT-2 model, which is what they're calling it, which is,
[395.54 → 400.22] it's building on a previous model, which you might have been guessed was called GPT.
[400.40 → 406.08] But this model, along with a variety of other models that have been released recently,
[406.42 → 409.48] so those being like BERT or ELMO.
[409.70 → 417.20] So we had another episode, episode 22, where we kind of dove into a particular implementation BERT.
[417.20 → 424.72] So if you're wanting to know in a little bit more detail, like what a language model is and how to utilize it,
[424.76 → 427.90] you might listen to that episode, episode 22 about BERT.
[428.38 → 435.02] But any of these models, including GPT-2, is really, when they say it's a language model,
[435.42 → 438.58] this is really like a pre-trained encoder.
[438.58 → 445.58] And what that means is you kind of put words in and then out the other end comes these word embeddings
[445.58 → 451.86] or these various representations of the words that are based on kind of contextual relationships
[451.86 → 453.96] between all the words in your corpus.
[454.16 → 460.40] So these embeddings come out, and then you can utilize those generated embeddings for various tasks,
[460.40 → 470.02] like sentiment analysis or named entity recognition and like question answering, text generation, machine translation.
[470.34 → 476.64] And so the language model part of these is that, you know, encoding bit.
[477.26 → 479.78] Yeah, and this is a particularly big one.
[479.92 → 487.74] They describe GPT-2 as a large transformer-based language model with 1.5 billion parameters
[487.74 → 491.18] and trained on a data set of 8 million web pages.
[491.48 → 494.16] Its objective is simply to predict the next word.
[494.58 → 494.82] Yeah.
[494.94 → 496.08] That's a huge scale, though.
[496.40 → 499.66] I'd be interested, like, just, you know, as you were talking about that,
[499.70 → 503.86] I'd be interested to, like, how did they parse and format these web pages?
[503.94 → 508.26] As we'll talk about later, they didn't release the full data set that they used for this.
[508.42 → 509.64] So we'll talk about that later.
[509.76 → 513.50] But just, I don't know, thinking about how this would operationally work in my mind,
[513.64 → 517.52] you know, parsing these web pages is a little bit complicated in and of itself.
[517.74 → 518.90] Yeah, I don't know.
[518.96 → 520.06] It seems complicated.
[520.18 → 523.76] And I guess 1.5 billion parameters, it's no small potatoes.
[524.02 → 525.46] No, I think it's pretty huge.
[525.88 → 529.84] Yeah, I mean, and there's certainly the drama, you know, associated with it.
[529.96 → 531.70] They note on their blog post,
[532.00 → 535.46] due to our concerns about malicious applications of the technology,
[535.94 → 537.64] we are not releasing the train model.
[537.86 → 540.88] And then they go on to say that they'll release a much smaller model
[540.88 → 544.34] for researchers to experiment with as well as the technical paper.
[544.66 → 546.20] Yeah, cue the ominous music.
[546.20 → 550.04] I know, and my first impression when I read that was,
[550.36 → 555.12] on the assumption that this model is as great as it looks like it may be here,
[555.48 → 559.06] you know, isn't that sort of, you know, you have a dam that's about to burst,
[559.26 → 561.58] you know where it's just, you know, suddenly we have this new capability.
[561.74 → 563.34] Isn't that like sticking your fingers and
[563.34 → 566.44] little holes in the dam to try to keep the whole thing from coming?
[566.52 → 569.38] Because if it is what they think it is, and they're releasing this,
[569.88 → 572.26] it won't be long before it's pretty much everywhere.
[572.26 → 576.92] Because now that everyone knows you can do it, it'll be recreated elsewhere.
[577.60 → 577.82] Yeah.
[577.98 → 582.02] And I think it should be noted that this really algorithmically,
[582.18 → 587.58] there's not really a major advance kind of in the architecture or algorithm
[587.58 → 590.62] that is the focus of this model.
[590.62 → 593.50] But it's really kind of the scaling up of it.
[593.62 → 597.50] So as you mentioned, Chris, this is a transformer based model.
[598.04 → 602.54] And so the other transformer based models recently have been,
[602.78 → 604.72] as we mentioned, Bird and Elmo and these things.
[605.18 → 608.88] And the transformer architecture has been around for a bit.
[608.88 → 613.50] So that's like this mechanism that kind of learns the contextual relationships
[613.50 → 616.06] between words or sub words in a text.
[616.22 → 618.32] And so that's been around.
[618.80 → 621.78] So that's not new to this GPT-2 model.
[621.90 → 623.36] So that's not the new thing.
[623.66 → 626.84] The new thing isn't really how they train it,
[626.88 → 630.54] because they're really just using this simple framework of training.
[630.72 → 632.68] So when you're training these language models,
[632.68 → 636.08] you need to have some sort of task that you're trying to do,
[636.08 → 639.38] even though the goal is to get the embedding layer.
[639.60 → 643.40] It's not to do classification or translation or something.
[643.50 → 646.66] You need some simple task to train the embedding on.
[647.28 → 648.66] And they're just using a simple task.
[648.78 → 650.40] So it's just predicting, like you said,
[650.44 → 654.70] predicting the next word in text from this internet text.
[655.14 → 657.06] And so the task isn't really new.
[657.40 → 659.48] The transformer idea isn't really new.
[659.56 → 663.32] It's really the scale of what they're doing.
[663.32 → 669.44] So they trained it on this hugely diverse internet data set or data set of web pages.
[670.06 → 672.36] And because of the diversity of that data,
[672.46 → 677.70] there's really some kind of significant capabilities that come out of it.
[677.90 → 681.84] Have you seen kind of this broad set of capabilities that they're proposing?
[682.48 → 682.82] I have.
[682.90 → 685.52] And as I've read through the various articles on it,
[685.64 → 688.06] it looks like kind of going back to what you're saying,
[688.16 → 690.70] that the key differential in this is just scale.
[690.70 → 694.94] You know, they put a lot more hyperparameters into it.
[695.06 → 696.82] They had a much larger data set.
[697.20 → 701.80] But they explicitly said they weren't really covering any new ground algorithmically.
[702.04 → 703.94] So, you know, it makes you, you know,
[704.04 → 705.98] as we're all starting to scale up over time,
[706.02 → 707.78] it really makes me wonder, you know,
[707.82 → 709.32] as fast as this is moving right now,
[709.38 → 711.52] if we're not going to be charging for it even farther.
[711.52 → 714.60] I mean, this was essentially the racetrack flag,
[714.68 → 716.00] you know, that went around and, you know,
[716.06 → 717.28] it's go for it.
[717.64 → 719.32] So I think we're going to see this.
[719.40 → 723.02] I think this is going to be so common within a few months out there
[723.02 → 725.74] that you'll see it in production pretty quick,
[725.80 → 729.02] regardless of the fact that they held back the larger model in this particular case.
[729.58 → 729.76] Yeah.
[729.88 → 732.70] So maybe one thing we kind of want to pause and define.
[732.70 → 736.76] So you'll see as you kind of read through some of these blog posts and everything,
[737.02 → 739.76] they talk about like zero shot something
[739.76 → 745.46] and like multitask or like various tasks associated with the model.
[745.74 → 750.62] So have you encountered this idea of zero shot before, Chris?
[750.78 → 752.04] No, this was a new one to me.
[752.22 → 754.86] So you want to jump in and explain?
[755.40 → 755.66] Yeah.
[755.82 → 760.00] So the kind of general idea is that zero shot basically means
[760.00 → 764.96] that the model is not trained on data that's specific to a task,
[764.96 → 769.60] but you evaluate that model on the particular task.
[769.80 → 773.10] So let's say where I've seen this in the past is like in translation.
[773.10 → 777.98] If you say have a model that translates English to French
[777.98 → 782.24] and then English to Spanish, you could train that model.
[782.76 → 785.40] And then you could try a sort of zero shot thing
[785.40 → 788.14] where you translated not from English to anything,
[788.14 → 790.44] but you could translate maybe from French to Spanish.
[790.62 → 793.10] So the model wasn't trained on that data,
[793.10 → 797.78] but you could try it out to see how well it worked to do that task, right?
[798.20 → 800.26] And so this is kind of the idea of zero shot.
[800.32 → 802.62] And what's fascinating with this model,
[802.64 → 805.52] I think what people are getting really excited about
[805.52 → 810.88] is that they train this model on this large set of data with a simple task,
[810.88 → 813.90] but it's showing really great results.
[813.90 → 816.54] I mean, not like state of the art,
[816.70 → 820.22] but good results for things that it wasn't trained to do.
[820.44 → 824.90] So for example, text summarization, translation, question answering,
[824.90 → 829.02] these sorts of tasks where they're showing these zero shot results
[829.02 → 832.98] for things that the model wasn't trained to do,
[833.06 → 835.80] which is kind of a crazy idea when you think about it.
[836.10 → 836.18] Yeah.
[836.24 → 839.52] So what do you think the implications are for zero shot on training
[839.52 → 841.08] for the industry at large?
[841.08 → 845.28] So now that this announcement came out and people are diving in
[845.28 → 847.22] and you're going to see more and more in the weeks ahead,
[848.16 → 852.04] and is zero shot in this unsupervised approach?
[852.34 → 854.26] Do you think that's going to be kind of the standard way
[854.26 → 856.38] that people tackle this going forward,
[856.46 → 858.34] given the result that we have initially here?
[858.96 → 861.82] So I think that there's kind of two elements to this,
[861.92 → 866.42] which are kind of sufficient data size and diversity and compute.
[866.60 → 868.76] So I think what they've shown is not that like
[868.76 → 871.48] these unsupervised techniques and, you know,
[871.62 → 874.18] generalization of a model to all of these tasks
[874.18 → 876.76] is like something that always can be done.
[877.40 → 881.34] But specifically, they've shown that because their data set
[881.34 → 886.14] exhibits all of these very diverse kind of qualities.
[886.84 → 889.88] So there's like data about different languages, right?
[889.92 → 892.74] And there's data maybe from question answer
[892.74 → 894.28] or forum websites or something.
[894.28 → 896.34] Because there's this sort of diverse set of data,
[896.34 → 900.16] it naturally encodes what you need for various tasks,
[900.16 → 902.40] like question answering and translation and things.
[902.80 → 905.72] And so given that sufficient amount and diversity of data
[905.72 → 908.36] and the actual compute that you would need
[908.36 → 910.36] to train 1.5 billion parameters,
[910.64 → 912.12] then yeah, sure.
[912.30 → 914.04] Like this might be a good,
[914.38 → 917.86] like really great starting point for a whole variety of tasks.
[918.28 → 922.50] I think the main issue here is no everybody has that diverse data
[922.50 → 924.64] and not everybody has that compute.
[924.64 → 927.50] I've never trained a model with 1.5 billion parameters.
[927.66 → 928.36] I don't know about you.
[928.82 → 931.68] No, no, that's a little bit bigger than I've dealt with for sure.
[932.00 → 935.18] So I guess, but over time as, you know,
[935.26 → 938.20] we've been on this exponential curve with compute increasing,
[938.40 → 941.04] while you pointed out early in this episode
[941.04 → 943.20] that we didn't know how they were parsing the webpages,
[943.34 → 945.34] you know, they clearly took a data set
[945.34 → 947.02] that is publicly available to everybody.
[947.02 → 949.12] So we do have access to that
[949.12 → 950.54] if we're willing to put the infrastructure
[950.54 → 952.78] behind the collection and the parsing.
[952.78 → 955.58] And to compute is becoming more and more available.
[955.88 → 957.76] It's really fascinating to me
[957.76 → 960.58] to start thinking about what the implications,
[960.94 → 962.68] you know, on all of our lives are going to be.
[962.88 → 966.16] It's really a science fiction-y kind of idea
[966.16 → 970.04] that's kind of upon us in very short order here.
[970.40 → 972.10] And so, you know, going back to what,
[972.48 → 973.14] it's kind of funny.
[973.28 → 975.16] So you and I are always talking about
[975.16 → 980.34] how people are concerned about the potential dangers of AI
[980.34 → 981.32] and whether they go,
[981.58 → 983.92] in my current job with Lockheed Martin,
[984.22 → 985.72] it's actually become part of my job
[985.72 → 987.68] to be thinking about those types of things
[987.68 → 989.46] in the frame of conflict, obviously.
[989.68 → 991.28] And so, you know, one of the things
[991.28 → 992.34] as I was reading this,
[992.38 → 993.16] I was thinking about is
[993.16 → 995.56] if you go back and look at what GANs are able to do now
[995.56 → 996.84] and you combine it with this,
[997.32 → 999.00] then, and you think about,
[999.16 → 999.64] you know, all the
[999.76 → 1001.26] we've been talking about political misinformation
[1001.26 → 1002.62] over the last few years
[1002.62 → 1004.42] with, you know, various elections and stuff.
[1004.42 → 1006.66] I just wonder that, you know,
[1006.66 → 1007.88] that's the downside to it.
[1007.96 → 1009.90] There's also some pretty amazing upsides
[1009.90 → 1013.34] in terms of being able to create user experiences
[1013.34 → 1015.28] around these new technologies
[1015.28 → 1018.48] that can do some pretty wondrous things.
[1018.74 → 1021.06] If you combine, you know, in the medical industry,
[1021.18 → 1023.16] if you want to have a beyond just a chatbot,
[1023.28 → 1025.30] but essentially a virtual doctor
[1025.30 → 1028.30] who looks and talks very much like a real person,
[1028.38 → 1029.38] you'd never know the difference
[1029.38 → 1030.96] and you're in a remote part of Africa.
[1031.10 → 1031.94] We've talked about, you know,
[1032.16 → 1033.62] being in places where you don't have
[1033.62 → 1034.80] ubiquitous internet everywhere.
[1035.28 → 1037.72] It just, I think this is a real game-changing technology
[1037.72 → 1040.48] that in tandem with these other game changers
[1040.48 → 1041.92] is really accelerating
[1041.92 → 1043.58] what we're going to experience
[1043.58 → 1044.44] over the next few years.
[1044.54 → 1047.30] I think the idea of the distant future
[1047.30 → 1048.64] is really upon us,
[1048.72 → 1049.62] whether it be good or bad.
[1050.00 → 1051.00] Any thoughts on that?
[1051.54 → 1053.22] Yeah, and I think maybe one thing
[1053.22 → 1054.26] that we can share
[1054.26 → 1055.60] just to kind of emphasize
[1055.60 → 1057.96] these sorts of implications,
[1057.96 → 1059.74] and really we can talk next
[1059.74 → 1062.72] about like the dangerous implications of this,
[1062.82 → 1064.70] which really have to do with
[1064.70 → 1067.24] what they're saying around like fake news generation
[1067.24 → 1068.16] and that sort of thing.
[1068.30 → 1069.96] So one of the things that I think we would do
[1069.96 → 1070.66] to drive that home
[1070.66 → 1072.76] is just read a little excerpt of,
[1073.22 → 1074.74] you know, some of this generated text,
[1074.82 → 1076.30] which is really just astounding.
[1076.46 → 1078.32] So this is kind of a silly subject,
[1078.32 → 1079.28] which, you know,
[1079.32 → 1081.50] maybe people don't find interesting
[1081.50 → 1083.38] or wouldn't think is real,
[1083.38 → 1086.30] but imagine that this was kind of a real news story.
[1086.30 → 1088.50] So in one of their examples
[1088.50 → 1089.68] that they post online
[1089.68 → 1091.60] and one of their samples from OpenAI,
[1091.94 → 1093.36] they have a system prompt.
[1093.48 → 1094.58] So this is a text
[1094.58 → 1096.76] that was generated by a human.
[1097.02 → 1098.72] And then they follow that on
[1098.72 → 1100.86] with kind of model completed
[1100.86 → 1102.46] or a model generated text
[1102.46 → 1103.70] that actually just generates
[1103.70 → 1104.92] the rest of the story.
[1105.08 → 1106.66] So this first bit I'm going to read
[1106.66 → 1108.62] is the human written part.
[1108.72 → 1109.26] So they say,
[1109.58 → 1110.74] in a shocking finding,
[1111.18 → 1113.82] scientists discovered a herd of unicorns
[1113.82 → 1114.98] living in a remote,
[1114.98 → 1116.82] previously unexplored valley
[1116.82 → 1117.90] in the Andes Mountains.
[1118.22 → 1120.10] Even more surprising to the researchers
[1120.10 → 1122.16] was the fact that the unicorns
[1122.16 → 1123.62] spoke perfect English.
[1124.12 → 1126.12] Okay, so that was the human written portion.
[1126.38 → 1129.50] And that's all that they gave to the model.
[1129.70 → 1131.52] And then the model generated
[1131.52 → 1133.06] the following completion.
[1133.54 → 1135.76] So this is all model generated.
[1135.76 → 1136.94] So not human generated.
[1137.14 → 1138.48] The model came back with,
[1138.64 → 1140.38] the scientists named the population
[1140.38 → 1142.50] after their distinctive horn,
[1142.86 → 1143.66] Ovid's unicorn.
[1143.66 → 1145.00] These four horns,
[1145.14 → 1146.42] silver white unicorns
[1146.42 → 1148.06] were previously unknown to science.
[1148.36 → 1150.10] Now, after almost two centuries,
[1150.24 → 1151.52] the mystery of what sparked
[1151.52 → 1152.58] this odd phenomenon
[1152.58 → 1154.14] is finally solved.
[1154.42 → 1155.70] Dr. Jorge Perez,
[1155.88 → 1157.28] an evolutionary biologist
[1157.28 → 1159.04] from the University of La Paz,
[1159.42 → 1160.50] and several companions
[1160.50 → 1163.08] were exploring the Andes Mountains
[1163.08 → 1164.66] when they found a small valley
[1164.66 → 1166.58] with no other animals or humans.
[1166.78 → 1167.60] Perez noticed,
[1167.76 → 1168.46] blah, blah, blah, blah, blah,
[1168.54 → 1169.46] and it keeps going on.
[1169.52 → 1171.48] So you can already get a sense that,
[1171.48 → 1172.80] like, if I was to read,
[1173.08 → 1174.72] and it kind of drifts in and out
[1174.72 → 1175.94] as the story goes along,
[1176.24 → 1178.86] but if just reading kind of that initial bit,
[1179.12 → 1181.76] I would have absolutely never expected
[1181.76 → 1183.62] a computer to be able to generate
[1183.62 → 1184.80] something that coherent,
[1185.00 → 1187.26] especially when it's been trained
[1187.26 → 1189.40] on only a very simple task.
[1189.76 → 1190.08] I don't know.
[1190.12 → 1191.52] What are your thoughts on unicorns, Chris?
[1192.64 → 1194.72] Well, I like unicorns,
[1194.72 → 1195.52] just to go on the record.
[1195.52 → 1198.08] No, I think when you're,
[1198.16 → 1199.96] and I'm looking at the rest of the text
[1199.96 → 1201.28] that you were starting to read through,
[1201.54 → 1203.28] and the thing that jumps out
[1203.28 → 1205.34] is that it is so sophisticated
[1205.34 → 1206.98] in the way it's using language.
[1207.30 → 1208.48] It has sophistication
[1208.48 → 1210.80] of a well-educated person
[1210.80 → 1211.94] as they might speak
[1211.94 → 1213.14] in a storytelling mode,
[1213.38 → 1214.76] and that's very different
[1214.76 → 1216.66] from many of the computer-generated texts
[1216.66 → 1218.60] we've seen over the years prior to this.
[1218.84 → 1220.84] And it's that sense of sophistication
[1220.84 → 1222.66] that jumps off the page,
[1222.66 → 1225.42] and it's pretty astounding.
[1225.58 → 1227.60] If someone wants to get on their blog
[1227.60 → 1229.26] at OpenAI and read through
[1229.26 → 1230.04] the rest of the text,
[1230.18 → 1232.60] I mean, easily you could believe
[1232.60 → 1234.18] that all of this was written by a person.
[1234.32 → 1235.16] You might even challenge
[1235.16 → 1236.30] that it was computer-generated.
[1236.80 → 1237.88] I'll tell you, whatever,
[1238.06 → 1239.28] it's probably going to really
[1239.28 → 1241.10] change gaming going forward.
[1241.40 → 1242.30] Dungeons and Dragons
[1242.30 → 1243.40] will never be the same again
[1243.40 → 1244.60] the way this is,
[1244.68 → 1248.10] but I can't stop thinking
[1248.10 → 1249.40] about all the uses for this
[1249.40 → 1251.46] that we can apply in industry.
[1251.46 → 1254.00] Yeah, so we've got to the point
[1254.00 → 1255.94] where we can see, you know,
[1256.00 → 1260.30] generally what this GPT2 model is.
[1260.38 → 1261.34] They should make an easier
[1261.34 → 1262.64] pronounceable name.
[1262.92 → 1264.48] And like the quality
[1264.48 → 1265.86] of the text generation
[1265.86 → 1266.62] that it can produce.
[1266.70 → 1267.64] So we've seen this kind of
[1267.64 → 1270.28] very coherent, sophisticated text
[1270.28 → 1271.76] that's generated by this model,
[1272.18 → 1274.90] which, you know, is just astounding.
[1275.36 → 1276.38] And so naturally,
[1276.64 → 1277.94] as you kind of think,
[1278.00 → 1278.82] as you were saying, Chris,
[1278.84 → 1280.52] there's a ton of great applications
[1280.52 → 1282.88] to this and maybe fun applications,
[1282.96 → 1284.02] like you were saying in gaming,
[1284.46 → 1286.44] maybe perfect applications
[1286.44 → 1287.82] in like text summarization
[1287.82 → 1289.10] or question answering
[1289.10 → 1290.24] and that sort of things,
[1290.62 → 1291.54] that sort of thing.
[1291.90 → 1294.00] But it naturally brings us
[1294.00 → 1295.62] to the point of talking about,
[1295.82 → 1298.04] hey, there's some really malicious
[1298.04 → 1300.88] applications of this as well,
[1300.96 → 1302.58] especially if we talk about,
[1302.58 → 1305.38] you know, fake news generation.
[1305.38 → 1307.62] So if you're able to generate,
[1307.74 → 1311.80] you know, basically endless news stories
[1311.80 → 1315.34] that are coherent along a particular viewpoint
[1315.34 → 1317.58] or promoting a particular viewpoint
[1317.58 → 1320.24] or idea or story that's fake,
[1320.38 → 1322.36] obviously that flood
[1322.36 → 1325.04] of really coherent fake news
[1325.04 → 1327.54] is definitely of concern.
[1327.76 → 1329.56] So, you know, you were talking about
[1329.56 → 1331.44] in terms of security and all that,
[1331.54 → 1332.64] you are always thinking
[1332.64 → 1334.40] along these lines these days, Chris.
[1334.40 → 1335.54] What's your thought
[1335.54 → 1337.88] on that sort of line of application?
[1338.56 → 1339.92] When I was in Switzerland
[1339.92 → 1342.70] for the Applied Machine Learning Days conference,
[1342.70 → 1344.12] I also had a conversation
[1344.12 → 1346.74] with an expert on AI safety
[1346.74 → 1348.80] and he was working on models
[1348.80 → 1351.16] that addressed some of the very things
[1351.16 → 1352.34] that you were just talking about.
[1352.60 → 1355.30] And I guess seeing this come out,
[1355.46 → 1356.24] you know, it's something
[1356.24 → 1357.10] that we've been discussing,
[1357.22 → 1358.10] but it made me realize
[1358.10 → 1359.72] how critically important
[1359.72 → 1363.12] the field of AI safety is going to be.
[1363.12 → 1364.74] I think just like we've been talking
[1364.74 → 1366.08] about ethics over the past year
[1366.08 → 1367.36] is crucial to this.
[1367.48 → 1369.30] I think different forms of AI safety
[1369.30 → 1370.96] in terms of being able to differentiate,
[1371.32 → 1374.12] you know, between what is fake
[1374.12 → 1375.08] and what is not fake
[1375.08 → 1376.76] is going to be so crucial
[1376.76 → 1378.14] for not just the technology,
[1378.26 → 1379.50] but for society going forward.
[1379.86 → 1380.94] I think we're going to spend
[1380.94 → 1382.10] the next year talking a lot
[1382.10 → 1383.32] about AI safety as,
[1383.46 → 1384.10] because, you know,
[1384.32 → 1385.96] the genie's out of the bottle on this
[1385.96 → 1387.72] and whether we're worrying
[1387.72 → 1388.72] about the good or the bad,
[1389.04 → 1390.56] it's an amazing new technology.
[1390.56 → 1392.32] But we now have to be able to start
[1392.32 → 1393.54] being able to distinguish
[1393.54 → 1394.46] what that is.
[1394.58 → 1396.44] If you're talking about fake news
[1396.44 → 1398.78] and the ability to scale up on that,
[1398.96 → 1399.74] you know, on a downside,
[1399.90 → 1402.14] you could have just be awash in fake news
[1402.14 → 1403.82] and suddenly AI safety is all about
[1403.82 → 1405.38] where's the real news in that.
[1405.66 → 1407.86] If you're talking about a situation
[1407.86 → 1409.56] where you're in a conflict
[1409.56 → 1411.46] between two nations or something,
[1411.54 → 1413.50] it becomes a weapon of war.
[1413.82 → 1414.88] You have to start having tools
[1414.88 → 1415.80] to distinguish between that.
[1415.84 → 1417.14] And those are both dark things,
[1417.14 → 1418.20] but, you know, that's there.
[1418.32 → 1420.00] There are people in the world
[1420.00 → 1421.06] that will certainly try to use it
[1421.06 → 1421.86] for malicious purpose,
[1421.86 → 1423.38] as pointed out in the blog.
[1424.08 → 1424.22] Yeah.
[1424.52 → 1427.74] The whole idea that the dangerous bit
[1427.74 → 1429.22] of AI is, you know,
[1429.48 → 1431.14] AI is gaining consciousness
[1431.14 → 1432.36] and taking over the world.
[1432.36 → 1435.40] I think we can just put that aside
[1435.40 → 1436.58] for a long time.
[1436.84 → 1437.60] It's kind of irrelevant.
[1438.00 → 1438.38] Yeah.
[1438.48 → 1441.08] The most the danger that you can see
[1441.08 → 1443.68] with this application of text generation.
[1443.86 → 1445.78] So humans can do a lot of things.
[1445.78 → 1447.50] Text generation is one of those.
[1447.86 → 1450.28] And even if we just see like this model
[1450.28 → 1452.00] is capable of the quality
[1452.00 → 1454.72] of this text generation and nothing else,
[1455.10 → 1456.34] that in and of itself
[1456.34 → 1458.98] has huge security concerns.
[1459.08 → 1461.68] So I can read the quote
[1461.68 → 1464.62] from the OpenAI release blog post
[1464.62 → 1466.06] that you referenced before.
[1466.24 → 1467.08] They say, you know,
[1467.14 → 1468.08] due to our concerns
[1468.08 → 1469.34] about malicious applications
[1469.34 → 1470.32] of the technology,
[1470.32 → 1472.20] they're only releasing
[1472.20 → 1473.64] a much smaller model
[1473.64 → 1475.44] and they don't release the data.
[1475.44 → 1477.00] They have a technical paper.
[1477.22 → 1478.94] They reference certain
[1478.94 → 1482.96] certain particular malicious uses of it.
[1483.08 → 1484.68] So they list off generating
[1484.68 → 1485.84] misleading news articles.
[1486.00 → 1487.02] So that's what we've talked about.
[1487.16 → 1488.60] They mentioned impersonating
[1488.60 → 1489.60] others online,
[1490.14 → 1491.22] automating the production
[1491.22 → 1493.18] of abusive or faked content
[1493.18 → 1494.62] to post on social media
[1494.62 → 1496.64] and automating the production
[1496.64 → 1498.84] of spam or phishing content.
[1499.48 → 1500.66] So I don't know if it's good
[1500.66 → 1501.98] or bad that they listed out that.
[1501.98 → 1502.80] I guess people would have
[1502.80 → 1503.82] figured out those anyway.
[1504.56 → 1507.40] There's a point that it makes
[1507.40 → 1508.20] and it goes to what you were
[1508.20 → 1509.16] just saying a moment ago.
[1509.36 → 1510.56] And that is that you,
[1511.26 → 1512.32] for many years,
[1512.54 → 1514.80] the concern about AI going amok
[1514.80 → 1516.14] has been in, you know,
[1516.18 → 1518.38] what happens if AI becomes conscious
[1518.38 → 1520.20] and aware or self-aware
[1520.20 → 1521.94] and able to take actions
[1521.94 → 1523.12] that we were not anticipating.
[1523.50 → 1525.20] The reality is I'm unaware
[1525.20 → 1526.30] of anyone making
[1526.30 → 1527.50] any substantial progress
[1527.50 → 1528.30] down that road.
[1528.78 → 1530.20] But the thing that has mattered
[1530.20 → 1530.88] a great deal
[1530.88 → 1532.20] is that you have these tools,
[1532.36 → 1533.70] these AI tools,
[1533.96 → 1534.62] in this case,
[1534.72 → 1535.58] this like we're talking about,
[1535.64 → 1536.88] this GPT-2 model
[1536.88 → 1538.80] that has nothing to do
[1538.80 → 1539.54] with self-awareness.
[1539.60 → 1540.46] It's not self-aware.
[1540.60 → 1541.28] It's not conscious.
[1541.70 → 1543.88] But it is so very good
[1543.88 → 1546.40] at one specific type of task
[1546.40 → 1548.44] that it is able to match
[1548.44 → 1550.02] or exceed human capability
[1550.02 → 1550.92] in its nearer thing.
[1551.00 → 1551.56] We've seen that
[1551.56 → 1553.76] outside the NLP space as well,
[1553.82 → 1554.58] like the GANs
[1554.58 → 1555.08] we were talking about
[1555.08 → 1555.64] a little while ago.
[1555.64 → 1557.50] And so, you know,
[1557.62 → 1559.54] the concern, the danger,
[1559.90 → 1560.98] the ethical issues,
[1561.14 → 1561.92] the safety issues
[1561.92 → 1563.78] that we may be considering
[1563.78 → 1564.58] in going forward,
[1564.60 → 1566.32] I don't think is about consciousness.
[1566.52 → 1567.24] I don't think it's about
[1567.24 → 1568.10] the Terminator robot
[1568.10 → 1569.20] that's loose upon the world
[1569.20 → 1570.50] and going around
[1570.50 → 1571.04] killing everybody.
[1571.28 → 1572.64] I think it's about
[1572.64 → 1574.44] the way humans are applying
[1574.44 → 1576.10] these very specific tools
[1576.10 → 1577.50] that are just marvellous
[1577.50 → 1578.42] at what they do.
[1578.70 → 1579.74] And they can be used
[1579.74 → 1580.74] for great good
[1580.74 → 1581.94] or terrible bad,
[1582.20 → 1582.76] terrible evil.
[1582.76 → 1584.48] And so I think that's where
[1584.48 → 1585.46] the real conversation is
[1585.46 → 1586.36] going forward is
[1586.36 → 1587.76] how do we want to do that?
[1587.86 → 1588.98] I think probably,
[1589.16 → 1590.12] I'm guessing you are too,
[1590.20 → 1591.58] I'm kind of tired of people
[1591.58 → 1593.08] talking about Terminator robots
[1593.08 → 1593.74] coming to kill us
[1593.74 → 1594.98] because I just haven't seen
[1594.98 → 1595.82] that in reality.
[1596.08 → 1597.90] But this is a big concern here
[1597.90 → 1599.50] about how do we move forward
[1599.50 → 1600.06] into a future
[1600.06 → 1600.80] where these tools
[1600.80 → 1601.64] become commonplace.
[1602.16 → 1602.38] Yeah.
[1602.56 → 1604.28] And I do appreciate,
[1604.40 → 1605.04] you know,
[1605.18 → 1607.44] OpenAI and Google
[1607.44 → 1608.08] and others,
[1608.34 → 1609.50] particularly OpenAI
[1609.50 → 1610.22] in this case,
[1610.68 → 1610.94] you know,
[1610.94 → 1612.74] being transparent
[1612.74 → 1614.18] about their concerns
[1614.18 → 1614.66] with this.
[1614.82 → 1615.36] I've heard,
[1615.44 → 1616.70] I've heard certain people say,
[1616.86 → 1617.14] oh, well,
[1617.14 → 1618.48] they're just like saying
[1618.48 → 1620.08] these dangerous things
[1620.08 → 1620.74] about danger
[1620.74 → 1621.64] because they want
[1621.64 → 1622.36] more publicity,
[1622.36 → 1623.48] which, you know,
[1623.50 → 1624.38] who knows what their,
[1624.78 → 1626.42] what their full motivations are.
[1626.50 → 1628.38] I, based on my perception,
[1628.38 → 1629.38] I don't think that
[1629.38 → 1630.12] that's totally it.
[1630.16 → 1631.28] Maybe, maybe there's a part
[1631.28 → 1632.12] of it that's that way,
[1632.16 → 1633.28] but I do appreciate
[1633.28 → 1635.00] their, their transparency
[1635.00 → 1636.00] around the
[1636.58 → 1637.26] that they've thought
[1637.26 → 1637.94] through this.
[1637.94 → 1639.22] they've decided
[1639.22 → 1641.72] to deal with this issue
[1641.72 → 1643.54] by still releasing
[1643.54 → 1644.20] the research.
[1644.44 → 1645.44] So publishing the paper,
[1645.98 → 1647.50] still releasing the code,
[1647.50 → 1649.06] but only releasing
[1649.06 → 1650.92] a smaller pre-trained model.
[1650.92 → 1652.12] So not the full model.
[1652.12 → 1653.78] Uh, and then also
[1653.78 → 1654.70] not releasing
[1654.70 → 1656.00] the full data set
[1656.00 → 1656.84] that they've parsed
[1656.84 → 1657.84] associated with this.
[1657.94 → 1659.62] So I guess their,
[1659.90 → 1661.64] their sort of thought process
[1661.64 → 1662.44] is, oh, well,
[1662.66 → 1664.44] people don't have
[1664.44 → 1665.74] to compute that we have.
[1665.74 → 1666.84] It would take them
[1666.84 → 1667.92] an enormous amount of time
[1667.92 → 1669.36] to recreate this data set
[1669.36 → 1672.44] and train the larger model
[1672.44 → 1673.60] on this data set.
[1673.72 → 1674.82] And so they're thinking,
[1674.98 → 1675.96] oh, well, this at least,
[1676.06 → 1677.80] you know, buys us time.
[1678.06 → 1678.72] Um, do you,
[1678.72 → 1679.44] exactly right.
[1679.76 → 1679.96] Yeah.
[1680.02 → 1681.86] Do you, do you kind of
[1681.86 → 1683.84] track with that train of thought
[1683.84 → 1684.72] or does that seem
[1684.72 → 1686.02] not sufficient to you
[1686.02 → 1687.40] or just not relevant
[1687.40 → 1688.02] or what,
[1688.50 → 1689.48] no, what is your thought
[1689.48 → 1690.88] as far as how they've dealt
[1690.88 → 1691.78] with the issue
[1691.78 → 1692.92] from their perspective?
[1693.08 → 1693.26] Yeah.
[1693.34 → 1694.38] There isn't really
[1694.38 → 1695.58] a guidebook on how,
[1695.64 → 1697.36] how responsible, uh,
[1697.36 → 1698.20] disclosure is,
[1698.28 → 1699.38] is to be done in this.
[1699.50 → 1700.90] You know, different organizations
[1700.90 → 1701.84] have different approaches.
[1702.22 → 1703.70] I give them the benefit
[1703.70 → 1704.24] of the doubt
[1704.24 → 1704.72] that this,
[1704.86 → 1705.32] that they're trying
[1705.32 → 1705.94] to be responsible.
[1706.04 → 1707.20] It certainly doesn't stop
[1707.20 → 1708.02] the potential
[1708.02 → 1709.42] for malicious actors
[1709.42 → 1710.38] to take advantage of this,
[1710.44 → 1710.98] but what it does
[1710.98 → 1712.30] is it slows it down over time
[1712.30 → 1713.42] for the exact reasons
[1713.42 → 1714.16] that you just said.
[1714.28 → 1715.28] And it gives us time
[1715.28 → 1715.98] to think our way
[1715.98 → 1716.72] through it a little bit,
[1716.78 → 1717.66] which I think is good
[1717.66 → 1720.24] because it's still out there.
[1720.28 → 1721.10] It's still coming.
[1721.38 → 1722.10] Uh, we now know
[1722.10 → 1722.70] it's possible
[1722.70 → 1723.16] and that,
[1723.28 → 1724.22] that means that everybody
[1724.22 → 1725.36] will be very much
[1725.36 → 1726.04] focused on it.
[1726.10 → 1726.62] It's, it's already
[1726.62 → 1728.24] proven, uh, to work
[1728.24 → 1729.52] and therefore, uh,
[1729.52 → 1730.52] there'll be money behind it
[1730.52 → 1731.06] and there'll be interest
[1731.06 → 1731.54] behind it.
[1731.62 → 1733.30] So I think it really
[1733.30 → 1734.30] comes down to the fact
[1734.30 → 1735.68] that as we go forward,
[1735.68 → 1736.60] just as we have been
[1736.60 → 1737.30] talking ethics
[1737.30 → 1738.06] and as we are now
[1738.06 → 1739.14] talking AI safety,
[1739.14 → 1740.24] we need to build
[1740.24 → 1741.32] some frameworks around
[1741.32 → 1742.42] what it means
[1742.42 → 1743.64] to, to discover
[1743.64 → 1744.72] these tools,
[1744.86 → 1745.62] produce these tools
[1745.62 → 1746.38] and release them
[1746.38 → 1747.00] into the public.
[1747.22 → 1748.06] I think they're coming.
[1748.20 → 1748.80] I don't think they're
[1748.80 → 1749.62] likely to be,
[1749.70 → 1750.88] to stop at any point,
[1750.96 → 1752.36] but I like the fact
[1752.36 → 1753.20] that they're thinking,
[1753.20 → 1754.12] let's put the brakes
[1754.12 → 1755.06] on just a little bit
[1755.06 → 1756.42] to have time to react
[1756.42 → 1757.62] a little bit better
[1757.62 → 1758.46] than we can at the moment.
[1758.46 → 1760.14] So I agree with you.
[1760.24 → 1761.08] I think, uh,
[1761.26 → 1762.46] pretty much in everything
[1762.46 → 1763.14] you said,
[1763.22 → 1764.54] there is one aspect
[1764.54 → 1766.08] of this that I don't know
[1766.08 → 1766.98] that I fully formed
[1766.98 → 1768.20] an opinion on
[1768.20 → 1769.46] in the sense that
[1769.46 → 1770.30] open AI
[1770.30 → 1772.42] is essentially saying
[1772.42 → 1774.14] that they've judged
[1774.14 → 1775.04] this to have
[1775.04 → 1776.28] negative consequences
[1776.28 → 1777.66] in however they're
[1777.66 → 1779.04] quantifying that.
[1779.04 → 1781.18] and so they have
[1781.18 → 1782.24] deemed that it matters
[1782.24 → 1783.66] that they don't
[1783.66 → 1784.46] release things
[1784.46 → 1786.08] rather than releasing
[1786.08 → 1787.06] things and then
[1787.06 → 1788.18] having the community
[1788.18 → 1789.74] like form,
[1789.92 → 1791.22] be able to test it,
[1791.28 → 1792.66] be able to, uh,
[1792.74 → 1794.24] actually use it to,
[1794.24 → 1795.36] to, you know,
[1795.36 → 1796.82] come up with methods
[1796.82 → 1798.06] that would, uh,
[1798.40 → 1800.04] that would fight
[1800.04 → 1801.12] against the negative
[1801.12 → 1802.18] consequences that
[1802.18 → 1802.92] it might produce.
[1803.08 → 1804.36] Um, they're pretty much
[1804.36 → 1805.08] restricting it to
[1805.08 → 1805.48] themselves.
[1805.48 → 1806.40] And, you know,
[1806.68 → 1807.42] in that sense,
[1807.44 → 1808.44] other people can't
[1808.44 → 1810.02] really fully parse
[1810.02 → 1810.98] the consequences
[1810.98 → 1811.50] because they don't
[1811.50 → 1812.44] have access to the
[1812.44 → 1812.94] full thing.
[1813.26 → 1814.26] I've seen this argument
[1814.26 → 1814.98] out there essentially
[1814.98 → 1816.40] that open AI is,
[1816.66 → 1817.08] you know,
[1817.08 → 1817.94] they're making this
[1817.94 → 1818.90] decision about it
[1818.90 → 1819.78] and people said
[1819.78 → 1820.52] there's no excuse
[1820.52 → 1821.24] for, you know,
[1821.30 → 1822.00] waiting to,
[1822.06 → 1822.86] to release it
[1822.86 → 1823.78] and that sort of thing,
[1823.82 → 1824.82] which, you know,
[1824.84 → 1825.80] I, I kind of get
[1825.80 → 1826.70] their train of thought.
[1826.80 → 1827.62] I don't know that I,
[1827.88 → 1829.28] that I fully agree with it.
[1829.56 → 1830.16] Oh, I didn't mean
[1830.16 → 1830.60] to interrupt.
[1830.70 → 1831.56] I was just going to say,
[1831.66 → 1833.32] I, I think that
[1833.32 → 1834.34] if you'll think back
[1834.34 → 1836.04] to recent history
[1836.04 → 1837.14] where we spent
[1837.14 → 1837.94] so much of the past
[1837.94 → 1838.90] year talking about,
[1838.90 → 1840.74] uh, the ethics of,
[1840.98 → 1841.76] around AI
[1841.76 → 1843.00] and we've had experts
[1843.00 → 1844.72] like Susan Ettinger
[1844.72 → 1845.56] on the show
[1845.56 → 1846.60] to, to discuss.
[1847.12 → 1847.54] I, I,
[1847.70 → 1849.44] in, in that time period
[1849.44 → 1850.32] as that conversation
[1850.32 → 1850.94] was being had
[1850.94 → 1851.60] within the community,
[1851.60 → 1852.88] you had a lot
[1852.88 → 1853.66] of the big players
[1853.66 → 1854.58] such as Google
[1854.58 → 1855.28] and Microsoft
[1855.28 → 1856.16] and others
[1856.16 → 1857.48] help by releasing,
[1857.72 → 1858.60] they thought their way
[1858.60 → 1859.24] through their own
[1859.24 → 1860.18] ethical framework
[1860.18 → 1861.46] and they released
[1861.46 → 1862.34] those guidelines
[1862.34 → 1863.14] that they were using
[1863.14 → 1863.62] internally
[1863.62 → 1865.08] and, and those of us
[1865.08 → 1865.46] who have been
[1865.46 → 1866.10] the beneficiaries
[1866.10 → 1866.78] of that
[1866.78 → 1867.46] have been able
[1867.46 → 1868.36] to kind of form
[1868.36 → 1869.08] what we think
[1869.08 → 1869.88] around several
[1869.88 → 1870.60] different frameworks
[1870.60 → 1871.70] and, and combine
[1871.70 → 1872.34] and make something
[1872.34 → 1873.60] that we, we hopefully
[1873.60 → 1874.72] think works for ourselves.
[1875.06 → 1876.08] Maybe that's something
[1876.08 → 1876.88] we can do here
[1876.88 → 1878.06] from a safety standpoint
[1878.06 → 1879.32] is with this kind
[1879.32 → 1879.86] of release
[1879.86 → 1881.12] and, and, and presumably
[1881.12 → 1882.44] others to come as well,
[1882.84 → 1883.74] it gives us a chance
[1883.74 → 1884.28] as a community
[1884.28 → 1885.36] to react a little bit
[1885.36 → 1886.16] about how we want
[1886.16 → 1887.02] to frame this
[1887.02 → 1888.26] from a, uh,
[1888.26 → 1889.92] a safety standpoint
[1889.92 → 1891.32] in, in terms of release,
[1891.68 → 1892.24] think our way through
[1892.24 → 1892.76] it is a little bit
[1892.76 → 1893.34] and then do it.
[1893.42 → 1894.66] So maybe a year
[1894.66 → 1895.86] from now, two years
[1895.86 → 1896.84] from now, there's
[1896.84 → 1897.50] more of a standard
[1897.50 → 1898.22] way of doing it
[1898.22 → 1898.84] instead of kind of
[1898.84 → 1899.36] feeling your way
[1899.36 → 1899.86] on your own.
[1899.92 → 1901.18] So I, I don't really,
[1901.18 → 1903.54] uh, hold the carefulness
[1903.54 → 1904.32] of what they're doing
[1904.32 → 1905.06] against them.
[1905.44 → 1905.96] Yeah, that's,
[1906.04 → 1906.86] it's a good point.
[1906.96 → 1908.02] I think we'll reference
[1908.02 → 1909.10] that, that link
[1909.10 → 1910.60] to, uh, Susan's show
[1910.60 → 1911.72] and others in the
[1911.78 → 1912.84] in the show, uh,
[1913.04 → 1913.70] in the show notes.
[1913.80 → 1914.70] I would also encourage you,
[1914.72 → 1915.66] I mean, this is a
[1915.66 → 1918.46] active topic of discussion
[1918.46 → 1919.42] within the community,
[1919.42 → 1920.72] and we would love
[1920.72 → 1921.92] to really hear
[1921.92 → 1923.56] from all of our listeners
[1923.56 → 1924.78] what your thoughts are
[1924.78 → 1925.62] on this pretty
[1925.62 → 1927.02] controversial subject.
[1927.42 → 1928.64] We have a Slack channel,
[1928.84 → 1930.78] a practical AI Slack channel.
[1931.20 → 1931.68] If you go to
[1931.68 → 1933.98] changelog.com slash community,
[1933.98 → 1935.64] you can join our Slack channel.
[1935.76 → 1936.86] We also have a LinkedIn,
[1937.38 → 1938.14] LinkedIn group
[1938.14 → 1939.34] where you can make comments.
[1939.34 → 1940.56] And so join one
[1940.56 → 1941.76] of those, uh, communities
[1941.76 → 1942.48] and let us know
[1942.48 → 1943.14] what you're thinking.
[1943.14 → 1944.42] If you have references
[1944.42 → 1945.60] to other good articles
[1945.60 → 1947.98] or other, uh, top, uh, uh,
[1947.98 → 1948.92] guests that you think
[1948.92 → 1950.32] might shed some light on this,
[1950.62 → 1951.52] we'd love to have them
[1951.52 → 1952.12] on the show.
[1952.12 → 1953.24] And we'd love to share
[1953.24 → 1954.62] those links via the
[1954.62 → 1955.54] the news feed
[1955.54 → 1957.02] at changelog.com.
[1957.14 → 1958.66] So definitely get involved
[1958.66 → 1959.22] with that.
[1959.64 → 1960.24] And the show notes,
[1960.32 → 1960.62] by the way,
[1960.64 → 1961.86] while you're mentioning community,
[1961.96 → 1963.14] the show notes as, uh,
[1963.14 → 1964.62] are now starting to include
[1964.62 → 1967.02] a link to the changelog news
[1967.02 → 1968.20] for practical AI.
[1968.48 → 1969.80] So, uh, if you do go
[1969.80 → 1970.48] to the show notes,
[1970.58 → 1971.54] you'll see that there's
[1971.54 → 1972.30] a link right there
[1972.30 → 1973.14] where you can get into
[1973.14 → 1973.82] the conversation
[1973.82 → 1975.32] very directly as well.
[1975.32 → 1976.06] I just wanted to mention
[1976.06 → 1977.08] that other, that other,
[1977.08 → 1977.92] uh, newer approach
[1977.92 → 1978.78] that we're, that we're
[1978.78 → 1979.52] starting to roll out.
[1979.90 → 1980.44] Yeah, thanks.
[1980.84 → 1982.70] Well, as we kind of wrap
[1982.70 → 1986.00] the discussion of GPT-2 up,
[1986.08 → 1987.92] um, and before we share
[1987.92 → 1988.92] some learning resources,
[1988.92 → 1989.58] maybe it'd be good
[1989.58 → 1990.46] to kind of summarize
[1990.46 → 1992.08] some, some takeaways
[1992.08 → 1993.98] from what OpenAI has done
[1993.98 → 1995.22] and from how the community
[1995.22 → 1995.96] has responded.
[1996.36 → 1997.84] I think one big takeaway
[1997.84 → 1999.28] that I have seen
[1999.28 → 2002.28] is that we can pretty much expect,
[2002.28 → 2004.06] as you've already alluded to,
[2004.06 → 2007.20] that OpenAI, Google, Microsoft,
[2007.48 → 2008.82] and these other big players
[2008.82 → 2010.76] are no longer thinking
[2010.76 → 2011.96] that it's appropriate
[2011.96 → 2014.26] to kind of innocently publish
[2014.26 → 2016.78] all of their new AI research findings
[2016.78 → 2018.18] and the, and the code
[2018.18 → 2019.12] associated with them.
[2019.30 → 2020.42] So to some degree,
[2020.42 → 2021.66] I think we can expect
[2021.66 → 2024.14] that the days of just like
[2024.14 → 2025.72] everything going on GitHub
[2025.72 → 2026.58] all of a sudden
[2026.58 → 2028.18] and download all
[2028.18 → 2029.10] of the pre-trained models,
[2029.10 → 2030.80] I think, I think is over
[2030.80 → 2031.72] to some degree,
[2031.72 → 2033.30] which is sad in certain respects
[2033.30 → 2035.38] and maybe appropriate as well.
[2035.64 → 2037.62] Yeah, I think to tag onto that,
[2038.14 → 2039.52] that the age of,
[2039.58 → 2041.86] of any significant release
[2041.86 → 2043.60] automatically considering
[2043.60 → 2046.28] the, the issues around AI safety
[2046.28 → 2047.56] along with ethics
[2047.56 → 2049.20] is part of the release
[2049.20 → 2050.12] at this point.
[2050.20 → 2050.92] And, you know, and if you're,
[2051.22 → 2052.18] you know, for coming from
[2052.18 → 2052.88] more of a software
[2052.88 → 2053.70] development background,
[2053.92 → 2054.72] that that's, you know,
[2054.76 → 2056.48] you, it's been rare cases,
[2056.56 → 2057.20] very specific,
[2057.20 → 2058.82] that you'd have to think that way.
[2058.82 → 2059.44] Cause you know,
[2059.48 → 2060.96] most software isn't inherently
[2060.96 → 2062.70] so powerful that it could be used
[2062.70 → 2063.32] for good or ill
[2063.32 → 2064.66] in many use cases,
[2064.66 → 2065.50] the way some of these
[2065.50 → 2066.16] technologies are.
[2066.24 → 2067.60] So I think it's a maturing process
[2067.60 → 2068.70] that we're having here.
[2069.50 → 2070.84] And, and I'm glad to see
[2070.84 → 2072.90] that open AI is leading the way
[2072.90 → 2073.66] as they do
[2073.66 → 2074.76] and thinking about
[2074.76 → 2076.32] how to release responsibly.
[2076.42 → 2077.48] I still think the code
[2077.48 → 2078.26] is going to be out there.
[2078.26 → 2079.20] And I think not only them,
[2079.24 → 2080.00] but I think now that
[2080.00 → 2080.90] with this,
[2080.98 → 2081.68] you'll see a lot of
[2081.68 → 2082.68] other organizations
[2082.68 → 2083.98] researching this area
[2083.98 → 2084.68] since there's already
[2084.68 → 2085.50] been proven results.
[2085.50 → 2087.04] So I think it's upon us
[2087.04 → 2088.36] and we'll just have to,
[2088.48 → 2089.92] we need to roll into it cautiously.
[2090.66 → 2090.78] Yeah.
[2090.90 → 2091.66] Along with that,
[2091.70 → 2092.34] I think businesses
[2092.34 → 2093.44] are taking this seriously
[2093.44 → 2094.70] because, you know,
[2094.72 → 2096.20] it can affect their bottom line
[2096.20 → 2097.60] if there are ethical concerns
[2097.60 → 2098.40] that, you know,
[2098.40 → 2099.78] can actually harm
[2099.78 → 2101.04] their business
[2101.04 → 2102.88] based on the AI software
[2102.88 → 2104.82] that they're using internally.
[2105.08 → 2106.46] They're to some degree
[2106.46 → 2107.14] looking at this
[2107.14 → 2108.24] from a business perspective
[2108.24 → 2109.34] and seeing that
[2109.34 → 2110.64] there is some connection
[2110.64 → 2111.88] with these ethical concerns
[2111.88 → 2114.10] to both the perception of them
[2114.10 → 2115.42] and how it affects
[2115.42 → 2116.78] their bottom line.
[2117.14 → 2117.76] Along with that,
[2117.84 → 2118.54] I think, you know,
[2118.62 → 2119.70] of course, a lot of people
[2119.70 → 2120.58] and you as well
[2120.58 → 2121.54] have already mentioned
[2121.54 → 2123.96] that there is a huge need
[2123.96 → 2125.90] to like yesterday,
[2125.90 → 2128.36] we need to be researching methods
[2128.36 → 2129.66] to detect, you know,
[2129.70 → 2130.92] AI generated text.
[2131.02 → 2131.68] And I know there's
[2131.68 → 2132.84] certain efforts out there.
[2133.00 → 2134.14] I also realized,
[2134.30 → 2135.92] I forget who I was talking to.
[2136.04 → 2136.66] It was at a conference
[2136.66 → 2138.68] and it's really hard problem.
[2139.32 → 2140.64] It's generating the text
[2140.64 → 2141.60] is a lot easier
[2141.60 → 2142.66] than detecting
[2142.66 → 2144.52] if it was AI generated.
[2144.62 → 2146.02] You are so right about that.
[2146.10 → 2148.04] That AI safety conversation
[2148.04 → 2150.00] that it may very well
[2150.00 → 2151.26] be an upcoming episode,
[2151.40 → 2151.68] hint, hint.
[2151.92 → 2153.12] It talks about that.
[2153.22 → 2154.16] It's much harder
[2154.16 → 2154.92] to differentiate
[2154.92 → 2157.12] the real from the unreal
[2157.12 → 2157.82] than it is
[2157.82 → 2159.08] to simply create the unreal.
[2159.30 → 2160.56] It's an order of magnitude harder.
[2160.78 → 2162.00] So that's one reason
[2162.00 → 2163.34] why cautious release
[2163.34 → 2164.92] may be a good mature way
[2164.92 → 2165.32] of doing it.
[2165.98 → 2166.76] And, you know,
[2166.86 → 2167.24] lastly,
[2167.44 → 2168.42] if you haven't noticed,
[2168.68 → 2170.64] AI for natural language
[2170.64 → 2173.26] is on fire everywhere.
[2173.42 → 2173.92] So it's like
[2173.92 → 2175.36] everybody's doing
[2175.36 → 2177.16] AI plus natural language
[2177.16 → 2179.24] and tons of great results.
[2179.38 → 2179.80] So I think
[2179.80 → 2181.66] one thing that you can look for
[2181.66 → 2183.00] as this year goes on
[2183.00 → 2185.60] is some pretty crazy stuff
[2185.60 → 2187.00] probably to come out
[2187.00 → 2187.80] of conferences
[2187.80 → 2189.08] like ACL
[2189.08 → 2190.36] and EM and LP
[2190.36 → 2191.16] and Neurons
[2191.16 → 2193.24] around natural language
[2193.24 → 2194.48] and this sort of thing.
[2194.56 → 2195.50] And along, you know,
[2195.56 → 2196.92] kind of the unsupervised
[2196.92 → 2198.20] or semi-supervised
[2198.20 → 2199.56] sorts of methods.
[2199.56 → 2201.18] So definitely something
[2201.18 → 2202.52] to keep an eye on.
[2202.88 → 2203.78] Yep, I agree with you.
[2203.94 → 2205.00] I'm really excited
[2205.00 → 2206.40] about seeing use cases
[2206.40 → 2207.80] for technology
[2207.80 → 2209.16] like what GPT-2
[2209.16 → 2211.44] is making available
[2211.44 → 2212.38] gradually here.
[2212.52 → 2213.20] We'll combine it
[2213.20 → 2214.30] with what GANs can do.
[2214.48 → 2215.48] I think that's
[2215.48 → 2216.40] pretty fascinating.
[2216.54 → 2217.24] I think, you know,
[2217.26 → 2217.80] you talked about
[2217.80 → 2218.44] how businesses
[2218.44 → 2219.10] will be impacted,
[2219.22 → 2220.22] but I think that
[2220.22 → 2220.78] there will be
[2220.78 → 2223.04] a wave of new types
[2223.04 → 2223.64] of businesses
[2223.64 → 2224.80] being created
[2224.80 → 2225.82] with these new technologies
[2225.82 → 2226.40] as well.
[2226.40 → 2227.80] and I'm very eager
[2227.80 → 2228.98] to see what kinds
[2228.98 → 2229.98] of thoughtful things
[2229.98 → 2231.56] entrepreneurs come up with.
[2231.56 → 2232.98] Yeah, speaking of that,
[2233.14 → 2234.74] in a couple of weeks here,
[2234.82 → 2235.96] we're going to be interviewing
[2235.96 → 2238.04] the CEO of Hugging Face.
[2238.28 → 2239.10] If you're following
[2239.10 → 2239.86] natural language
[2239.86 → 2240.76] and AI at all
[2240.76 → 2242.06] on Twitter and elsewhere,
[2242.06 → 2244.16] they are all over the place
[2244.16 → 2245.98] creating amazing things
[2245.98 → 2247.76] related to conversational AI.
[2247.94 → 2248.74] So I'm really excited
[2248.74 → 2249.62] about that interview.
[2249.76 → 2251.20] So stay tuned for that one.
[2251.36 → 2252.42] To close us out here,
[2252.46 → 2253.72] we always like to share
[2253.72 → 2255.00] some learning resources.
[2255.00 → 2256.24] If this conversation
[2256.24 → 2257.54] has sparked your interest
[2257.54 → 2258.32] in these topics
[2258.32 → 2259.56] and you want to dive
[2259.56 → 2260.46] in a little bit more,
[2260.58 → 2261.64] learn some of the details,
[2261.76 → 2262.58] maybe even try
[2262.58 → 2263.50] some of the methods.
[2263.88 → 2264.32] Of course,
[2264.38 → 2266.14] we'll link to like the code
[2266.14 → 2266.78] and the repos
[2266.78 → 2267.18] and everything
[2267.18 → 2267.92] in the show notes.
[2268.06 → 2269.28] But we did want to
[2269.28 → 2270.10] kind of point you
[2270.10 → 2271.18] to a couple sets
[2271.18 → 2272.18] of blog articles
[2272.18 → 2273.14] that I think can really
[2273.14 → 2274.26] help you get started.
[2274.42 → 2275.42] The first of those
[2275.42 → 2277.34] are on mlxplain.com.
[2277.44 → 2278.76] There's one called
[2278.76 → 2279.80] an in-depth tutorial
[2279.80 → 2281.24] to Allen NLP,
[2281.70 → 2282.56] which Allen NLP
[2282.56 → 2283.42] is this package
[2283.42 → 2284.26] based around
[2284.26 → 2285.16] or a toolkit
[2285.16 → 2286.54] based around PyTorch.
[2286.70 → 2287.48] And they have implemented
[2287.48 → 2288.88] things like Elmo and Bert
[2288.88 → 2290.78] in the toolkit.
[2291.38 → 2292.40] So that blog post
[2292.40 → 2293.06] would be perfect
[2293.06 → 2293.94] hands-on start.
[2294.04 → 2295.60] There's also a kind of
[2295.60 → 2297.94] paper dissected article
[2297.94 → 2298.78] about Bert
[2298.78 → 2301.08] on the ML Explained blog.
[2301.48 → 2302.58] Then there's this other blog,
[2302.66 → 2303.38] which I kind of
[2303.38 → 2304.62] came across recently
[2304.62 → 2306.36] and I wasn't aware of
[2306.36 → 2308.00] from Jay Palomar.
[2308.70 → 2309.80] And he has a series
[2309.80 → 2311.02] of blog posts
[2311.02 → 2311.80] called, you know,
[2311.80 → 2313.40] The Illustrated Something.
[2313.40 → 2314.14] So he has the
[2314.14 → 2315.46] Illustrated Transformer,
[2315.74 → 2316.52] which is talking about
[2316.52 → 2317.38] this transformer
[2317.38 → 2318.62] sort of model
[2318.62 → 2319.58] that all of these
[2319.58 → 2321.98] releases are based around.
[2322.38 → 2322.98] And then there's
[2322.98 → 2323.82] an Illustrated
[2323.82 → 2325.52] Bert, Elmo, and company,
[2325.94 → 2326.86] which talks about
[2326.86 → 2328.00] these encoders.
[2328.42 → 2329.42] I know I pointed you
[2329.42 → 2330.92] to these Illustrated ones
[2330.92 → 2331.54] a little bit earlier.
[2331.64 → 2332.58] Did you get a chance
[2332.58 → 2333.86] to take a look
[2333.86 → 2334.36] at those, Chris?
[2334.52 → 2334.86] I did.
[2334.92 → 2335.62] They're perfect
[2335.62 → 2336.62] and I recommend,
[2336.82 → 2337.70] thank you very much
[2337.70 → 2338.58] for pointing those out.
[2338.58 → 2339.98] I recommend to listeners
[2339.98 → 2341.82] that want to dive in.
[2342.16 → 2342.34] You know,
[2342.34 → 2343.02] these can be fairly
[2343.02 → 2344.08] complicated topics
[2344.08 → 2345.18] to ramp up on
[2345.18 → 2347.12] and the Illustrated pages
[2347.12 → 2348.76] are perfect
[2348.76 → 2349.54] for doing it.
[2349.58 → 2350.24] It may not be
[2350.24 → 2351.16] all you need.
[2351.24 → 2351.98] You may combine that
[2351.98 → 2352.70] with other resources,
[2352.70 → 2354.20] but it's another good one
[2354.20 → 2355.00] that you found there.
[2355.38 → 2355.66] Awesome.
[2355.86 → 2356.56] Well, this has been
[2356.56 → 2357.76] a great discussion, Chris.
[2357.88 → 2359.68] Thanks for all your insights
[2359.68 → 2361.38] and looking forward
[2361.38 → 2362.76] to talking to you
[2362.76 → 2363.44] again soon.
[2363.74 → 2364.38] Sounds good.
[2364.42 → 2364.98] As you said,
[2365.02 → 2365.82] we got more interviews
[2365.82 → 2366.54] coming up
[2366.54 → 2368.78] and so have a very good week
[2368.78 → 2369.58] and we'll talk to you
[2369.58 → 2369.96] next week.
[2372.18 → 2372.68] All right.
[2372.74 → 2373.34] Thank you for tuning
[2373.34 → 2374.42] into this episode
[2374.42 → 2375.36] of Practical AI.
[2375.62 → 2376.38] If you enjoyed this show,
[2376.44 → 2377.08] do us a favour,
[2377.20 → 2377.78] go on iTunes,
[2377.90 → 2378.58] give us a rating,
[2378.86 → 2380.02] go in your podcast app
[2380.02 → 2380.72] and favourite it.
[2380.82 → 2381.62] If you are on Twitter
[2381.62 → 2382.54] or social network,
[2382.64 → 2383.54] share a link with a friend,
[2383.62 → 2384.28] whatever you got to do,
[2384.52 → 2385.28] share the show with a friend
[2385.28 → 2385.98] if you enjoyed it.
[2386.28 → 2387.42] And bandwidth for Changelog
[2387.42 → 2388.94] is provided by Vastly.
[2389.06 → 2390.48] Learn more at Fastly.com
[2390.48 → 2391.62] and we catch our errors
[2391.62 → 2392.60] before our users do here
[2392.60 → 2393.06] at Changelog
[2393.06 → 2393.90] because of Rollbar.
[2394.08 → 2394.76] Check them out
[2394.76 → 2395.56] at Rollbar.com
[2395.56 → 2396.50] slash Changelog
[2396.50 → 2397.66] and we're hosted
[2397.66 → 2399.32] on Linde Cloud servers.
[2399.68 → 2400.44] Head to Linode.com
[2400.44 → 2401.28] slash Changelog.
[2401.38 → 2401.82] Check them out.
[2401.90 → 2402.72] Support this show.
[2403.16 → 2404.44] This episode is hosted
[2404.44 → 2405.60] by Daniel Whiten ack
[2405.60 → 2406.34] and Chris Benson.
[2406.84 → 2407.28] Editing is done
[2407.28 → 2408.24] by Tim Smith.
[2408.50 → 2409.50] The music is by
[2409.50 → 2410.52] Break master Cylinder
[2410.52 → 2411.52] and you can find
[2411.52 → 2412.84] more shows just like this
[2412.84 → 2414.34] at ChangeLog.com
[2414.34 → 2415.22] when you go there,
[2415.30 → 2416.50] pop in your email address,
[2416.80 → 2417.70] get our weekly email
[2417.70 → 2418.56] keeping you up to date
[2418.56 → 2419.30] with the news
[2419.30 → 2420.62] and podcasts for developers
[2420.62 → 2421.80] in your inbox
[2421.80 → 2422.82] every single week.
[2423.24 → 2423.98] Thanks for tuning in.
[2423.98 → 2424.90] We'll see you next week.
[2425.56 → 2429.28] Bye.
[2430.68 → 2432.62] Bye.
[2433.24 → 2433.30] College.
[2433.42 → 2433.68] It's good.
[2433.68 → 2434.00] Civilization.
[2434.00 → 2434.80] 2020
[2434.80 → 2435.08] is due
[2435.08 → 2435.34] into software.
[2435.34 → 2436.40] NASA
[2436.40 → 2436.52] is due
[2436.52 → 2453.88] to the
