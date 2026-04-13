[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[11.42 → 22.98] on Linde servers. Head to linode.com slash Changelog. Welcome to Practical AI, a weekly
[22.98 → 27.88] podcast about making artificial intelligence practical, productive, and accessible to everyone.
[27.88 → 33.48] This is where conversations around AI, machine learning, and data science happen. Join the
[33.48 → 37.54] community and snag with us around various topics of the show at changelog.com slash community.
[38.06 → 41.62] Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[46.08 → 53.54] Well, welcome to a fully connected episode of Practical AI, where Chris, my co-host, and I
[53.54 → 58.92] will keep you fully connected with everything that's happening in the AI community. We'll take
[58.92 → 64.88] some time to discuss some of the latest AI news, and then we'll dig into some learning resources to
[64.88 → 71.12] help you and us level up our machine learning game. So, Chris, how's it going?
[71.36 → 72.68] Going great. How are you doing, Daniel?
[72.98 → 76.00] Doing well. Getting ready for American Thanksgiving.
[76.32 → 82.28] Yep. As we're recording this, it is the day before Thanksgiving for us. And so looking forward
[82.28 → 88.20] to overstuffing myself tomorrow and then worrying about how I'm going to lose the weight thereafter.
[88.74 → 90.74] Yeah, looking forward to some Tour for sure.
[90.88 → 91.18] Exactly.
[92.58 → 96.52] What have you been seeing in terms of AI news recently, Chris?
[96.82 → 102.08] Well, actually, the first thing that caught my eye was something that you had shared with us the
[102.08 → 108.42] last time we were talking about this stuff. And that is, we were talking about artwork in the world
[108.42 → 115.46] of AI. And there was a particular piece of art that you discussed, and that was where a generative
[115.46 → 122.10] adversarial network had been used to generate this piece of kind of period art. I'm not an art person,
[122.10 → 123.42] so I'm not going to do that.
[123.50 → 125.26] Yeah, it looked like a portrait of a guy.
[125.62 → 130.88] Yeah, it was called Portrait of Edmund Bellamy, if I'm saying that correctly. And it's a fictional
[130.88 → 135.52] person from a fictional family. When you were telling us about it last, it hadn't gone to auction yet,
[135.52 → 141.84] but Christie's was going to, and they were expecting it to raise somewhere between $7,000 and $10,000 US.
[142.22 → 152.48] A few days after our episode went live, it actually went to auction, and it ended up selling for $432,500 US.
[152.84 → 153.20] Boom.
[153.44 → 153.76] Boom.
[153.78 → 154.44] That's crazy.
[154.70 → 156.78] Crazy. So, I mean, in a really...
[156.78 → 162.04] Wait, wasn't it? Yeah. So, they were saying that it was going to sell for like $7,000 to $10,000,
[162.04 → 162.74] right? Yeah.
[162.80 → 163.34] Something like that.
[163.34 → 168.68] Yeah, it was like, it was 45 time multiple on what they thought. And, you know, and so we had
[168.68 → 173.16] been looking at it with interest, you know, in the AI community, but I think the entire art world
[173.16 → 175.42] got rocked by that one because suddenly...
[176.26 → 176.90] Yeah, for sure.
[176.90 → 182.92] Yeah, you're a major contender from the AI world in terms of, you know, high value art going. So,
[183.26 → 188.06] I think it's something that a lot of people that are not traditionally thinking about AI are having
[188.06 → 193.06] to digest and realize that the world is changing. Yeah, I think people are going to have to start
[193.06 → 200.16] or are going to stop going to Chicago Institute of Art and start going to MIT or something to
[200.16 → 201.22] go into art.
[201.56 → 205.92] Yeah, it was kind of funny. A few days after that, I host a meetup in Atlanta called the
[205.92 → 209.34] Atlanta Deep Learning Meetup. And I know I've mentioned it before, but we actually had
[209.34 → 216.24] a generative adversarial network tutorial last month when we had an expert named Reza Katari
[216.24 → 222.02] come and show us. And it was funny. He came in, he goes, you know, I had this little project where
[222.02 → 225.92] we got all coded as we go along the way, but I've changed my mind. We're going to try to build some
[225.92 → 230.44] artwork in this session, and we'll split the proceeds if it makes enough money. And so,
[230.56 → 232.96] it was just funny because, you know...
[232.96 → 235.86] Sounds good. Yeah. Yeah, that's great.
[236.74 → 241.84] And there's been some other big news, not necessarily art related. What have you seen lately?
[241.84 → 247.78] Yeah. So, I don't know about you. I'm on Twitter. That's where I hear about a lot of things. And
[247.78 → 252.72] it seems like to me, and I don't know if you've seen this same thing. Let me know if you have,
[252.80 → 259.16] but it seems like every other AI related tweet that I'm seeing, at least in the people that I
[259.16 → 262.02] follow, is about natural language processing. Oh, yeah.
[262.12 → 267.36] So, like over the past, I would say like, I don't know, like three weeks to a month,
[267.36 → 274.06] it seems like there's just been a steady rise in all things like neural nets and natural language.
[274.18 → 275.32] Have you been seeing the same thing?
[275.38 → 280.20] I sure have. And I think I know where you're going with that because there was a particular
[280.20 → 286.24] thing announced that I'll let you lead into that has really caused a lot of interest in the last
[286.24 → 293.34] few weeks. Yeah, you guessed where I'm going. So, there's this new model out. So,
[293.34 → 299.66] a pre-trained model called BERT from Google. So, that's a new approach to pre-trained natural
[299.66 → 303.62] language processing, which we can talk about here in a second. But there's actually been,
[303.98 → 311.26] like I've seen even yesterday, I think it was yesterday, this HTML model from Hugging Face,
[311.40 → 314.86] which is pretty incredible. Take a look at that if you haven't seen it. And by HTML,
[314.86 → 324.26] it's not meaning the HTML of the web, but like a multitask learning model. And I'm sorry,
[324.50 → 331.26] now I'm saying I'm getting confused even with the acronym. So, it's HMTL, right? So,
[331.42 → 336.16] hierarchical multitask learning, not HTML. So, there's a confusion there.
[336.26 → 341.12] You know, you just disappointed an entire world of front-end developers who thought they're just now
[341.12 → 345.30] had their way into machine learning. Their way into it. Yeah. No. So, HMTL. So,
[345.34 → 350.50] I saw that yesterday. There's also like, I've seen Elmo, which I think came from the Allen Institute.
[351.02 → 356.90] And also, there was this challenge. So, one of the challenges at the now rebranded
[356.90 → 362.48] Neurons conference, which was a much-needed rebranding. But now, they had a competition
[362.48 → 368.28] that's actually, it's kind of in the schedule for the presentations phase, I think now,
[368.72 → 376.26] around chatbots and dialogue systems. And so, it seems like, at least from my perspective,
[376.48 → 380.00] all things with neural nets these days are like with natural language.
[380.46 → 385.32] Yeah. It's kind of funny. We go through these waves, you know, for a long time,
[385.56 → 389.52] everything seemed to be about computer vision and all the different convolutional
[389.52 → 394.28] variants that came out and capsule nets. And you're right, there hasn't been as much in the
[394.28 → 398.66] news lately. But with BERT being released, the NLP world is just on fire right now.
[399.06 → 404.36] Yeah, for sure. So, let's, actually, I'd love to, if you're willing to kind of dig in a little bit,
[404.40 → 409.82] I'd love to dig into exactly, you know, what BERT is. I'm still learning about it. So,
[409.82 → 415.18] I'll confess, you know, as we get into this conversation, please connect with us on our Slack
[415.18 → 421.44] team and our LinkedIn page of Practical AI. You can go to changelog.com slash practical AI
[421.44 → 427.54] and join our Slack team. But I would love to hear if I say anything that's not right. I'm kind of
[427.54 → 432.38] learning about these things as I go. So, we'd love to hear your perspective on these things as well.
[432.46 → 438.92] So, keep us informed in that way. But my understanding of what BERT is, is the goal is to
[438.92 → 446.16] create this kind of pre-trained NLP model or pre-trained language model. So, some of this
[446.16 → 451.38] terminology is new to me, like I mentioned. But in my understanding, what they're trying to do here
[451.38 → 459.72] is created an encoder that will be pre-trained that you could utilize for various natural language
[459.72 → 467.42] tasks. And so, for example, like sentiment analysis or question answering or named entity recognition,
[467.42 → 473.48] these are all kind of natural language processing tasks. And so, their goal is to create this
[473.48 → 482.96] pre-trained encoder that will essentially kind of act as a language model or a model that understands
[482.96 → 489.82] the kind of structuring of words in the context of those that can be utilized as the first bit of
[489.82 → 496.00] other models for these other sorts of tasks. Yeah. Is that kind of... Chris, correct me if I'm wrong.
[496.00 → 499.96] Am I on the complete wrong track here? No, no. I think you're right. I think they have some
[499.96 → 505.70] specific terminology they use. I think they call that a transformer. And the transformer is learning
[505.70 → 511.30] contextual relation between words and text. And then it has two separate pieces to it. One is an
[511.30 → 516.34] encoder that's reading the text input. And then one's a decoder that is producing the prediction,
[516.58 → 521.16] you know, for whatever task you're applying it to. So, I think when you combine the encoder and decoder,
[521.28 → 525.00] they're calling that a transformer. Yeah. But I think everything you said was accurate.
[525.00 → 529.38] Yeah. And I think what they're saying, because this isn't the transformer model,
[529.52 → 534.78] I guess, has been around for a while. And we'll link to the info about that in our notes. But this...
[534.78 → 539.36] So, the BERT model, which again has come out of Google. So, it stands for bidirectional
[539.36 → 546.88] encoder representations from transformers. So, essentially, this is like you just mentioned,
[547.00 → 553.28] Chris, this is based on the transformer model. And it's kind of like you mentioned in the transformer
[553.28 → 557.66] model. There's an encoder and a decoder level because they're trying to do a specific...
[557.66 → 563.92] One or more specific tasks. In this case, they're kind of basing this BERT model on the
[563.92 → 566.06] encoder piece of that transformer.
[566.06 → 568.76] I see. Okay. Thanks for the clarification there.
[568.96 → 574.38] Yeah. So, it took me a second to get there because it is confusing with the terminology.
[574.38 → 579.48] It's a lot to digest. There's a lot of information that's been pouring out. And I know both of us have
[579.48 → 584.36] been going through some of the different articles and stuff that kind of break it down. So, definitely
[584.36 → 587.14] a learning task and process for us.
[587.52 → 593.68] Yeah. Yeah. For sure. And my understanding is that it's based on this transformer encoder,
[593.90 → 600.80] which is kind of unique amongst encoders. Because when you think about trying to understand the
[600.80 → 605.04] language, like the context of a word in a sentence, you can think about it directionally,
[605.04 → 609.64] like moving forward in the sentence. And based on the kind of forward direction,
[609.92 → 617.28] getting the context of a word. But actually, the transformer in this case is... Well, they call it
[617.28 → 622.70] bidirectional. But in my understanding, it's really non-directional because it considers all of
[622.70 → 630.80] the text surrounding a word as it's determining the context of a word. So, it's not directional in the
[630.80 → 635.72] sense of like going forward through a sentence. Yeah. That's my understanding is I've seen it
[635.72 → 641.30] described in different people blogging about it as either non-directional, as you put it. I've seen
[641.30 → 645.80] it as directional in either way or bidirectional. I think you have a choice in how you're doing it.
[645.96 → 650.62] And the masking of the word that you're building the context around is pretty key.
[651.08 → 655.48] Yeah. Yeah. Definitely. You mentioned the tasks. I think that one of the... Also,
[655.48 → 661.40] the key features here is that it's the bidirectional encoder representation. So,
[661.44 → 668.36] they're creating this kind of context for language. But in order to do that, they have to
[668.36 → 676.06] kind of decide about what tasks will help them or what tasks or predictions will help them get the
[676.06 → 681.68] best understanding of language or create the best kind of encoder or language model,
[681.68 → 687.36] like they're calling it. And in this case, they're actually using multiple tasks to do that.
[687.62 → 691.66] They're using one task, like you mentioned, which is kind of like a masking of words.
[692.14 → 696.88] Like in a sentence, they'll kind of remove certain words and have them train the model
[696.88 → 702.38] with the encoder to actually kind of fill in those words. The other task that they're doing
[702.38 → 709.88] is next sentence prediction, which is like given two sentences, can you tell if one of the sentences
[709.88 → 713.20] actually the next sentence that comes after the other sentence?
[713.70 → 719.06] Yep. I agree. One of the things that it occurred to me, we probably should do is kind of talk about,
[719.16 → 724.64] you know, what encoding and decoding is. Encoding is where you're actually taking your input and
[724.64 → 728.54] putting it into the sequencing. And by the way, I found this on Quora. For the audience,
[728.82 → 732.92] Daniel and I are Googling this stuff just like you are. You know, we're all learning as we go.
[732.92 → 739.28] And encoding and decoding is obviously a common task in a lot of neural network architectures,
[739.38 → 743.60] but putting it into sequence and then decoding is where you're actually getting the output that
[743.60 → 748.22] you're going to use on that. I also want to note, we've kind of not mentioned that there's really
[748.22 → 754.30] two stages to BERT. And that's important because they're for different purposes. There's a pre-training
[754.30 → 760.46] stage and then there's a fine-tuning stage. And the pre-training stage is very expensive. It takes a lot
[760.46 → 766.52] of resource. I think in what I'm looking at here, they talk about it takes four days on a four to
[766.52 → 772.64] 16 cloud TPU system just to get through. Yeah, a lot of that's some crazy stuff. A lot of processing.
[772.64 → 779.72] I have the thing pulled up right now with GCPs cost. And that turns out to be around like,
[780.22 → 787.66] well, at least with the number I'm seeing around 7k US dollars. So 7000 US dollars in TPU costs,
[787.66 → 791.92] which of course they're Google and I guess they don't spend that because it's their own cloud, but
[791.92 → 797.02] significant effort. My wife would not like it if I did that for a weekend project. I would get in
[797.02 → 801.64] trouble for that, spending that kind of money. But fortunately, Google has put out a bunch
[801.64 → 806.28] of pre-trained models, you know, recognizing the expense of that they have, they have helped us,
[806.38 → 810.46] all those of us who are going to be trying to apply this technology. They have a good starting point.
[810.46 → 815.24] And really, when you're deploying it into your own application, the fine-tuning, which is an
[815.24 → 819.32] inexpensive thing, doesn't require nearly as much processing, is really where you're going to be
[819.32 → 823.86] focusing. So you'll be able to go and find a pre-trained model, hopefully, maybe or maybe not
[823.86 → 827.40] even need to make tweaks to it. They mentioned that there was very little adjustment needing to be
[827.40 → 832.34] made for different use cases. And then do the fine-tuning for your own specific, which is
[832.34 → 836.10] inexpensive and something that I probably could do on the weekend without getting in trouble.
[837.24 → 841.72] Nice. Yeah. So correct me if I'm wrong, Chris. So I'm trying to think about like,
[841.72 → 847.62] because I actually have potentially a couple use cases that I have in the back of my mind for this.
[847.88 → 851.70] And correct me if I'm wrong when I'm thinking about like how one would go about this. But
[851.70 → 859.32] in my understanding, the best use case for me to use BERT is if I have some natural language processing
[859.32 → 865.46] task, let's say I'm trying to identify certain entities in text, like named entity recognition.
[865.46 → 872.84] What I could do is take a pre-trained BERT. I don't know if that's the proper way to say that,
[872.96 → 873.88] but that's how I'm going to say. It works for us.
[874.26 → 878.96] Pre-trained BERT. Sorry to any of you out there that are named BERT, and this is confusing for,
[879.38 → 887.46] but I would take a pre-trained BERT, which Google has spent much, much time training and many updates
[887.46 → 893.66] steps and lots and lots of data. And so they've developed this BERT. And what BERT's going to do is
[893.66 → 902.28] allow me to put in sequences of words and BERT will then output sequences of vector representations
[902.28 → 907.08] of those words that also give kind of a context within the language model of BERT.
[907.60 → 916.98] And then I could kind of bolt onto that encoder layer, some classification task or some other sort
[916.98 → 923.64] of task. In my case, maybe it would be named entity recognition. And because BERT is so good
[923.64 → 930.60] at understanding the context of language, actually the update for me to actually do one of these
[930.60 → 936.12] tasks like named entity recognition or a question answering or something is, like you said, fairly
[936.12 → 941.74] inexpensive. So I'm utilizing all the expertise that has been built into Google's model and just
[941.74 → 948.68] adding on the little piece that makes it particular to my use case. And so the first thing that is
[948.68 → 951.24] pre-training, the second thing is fine-tuning. Is that right?
[951.24 → 955.56] I think that was a great explanation. And that is consistent with my understanding of it. It's,
[955.70 → 961.62] you know, BERT is really the way I'm reading it is BERT is really to be embedded into a larger
[961.62 → 967.64] architecture to where you get this incredible capability for maybe not for free, but at low
[967.64 → 973.80] cost relative to having to figure out how to do it yourself or use a lesser technology. So from my
[973.80 → 978.64] standpoint, I think this is another great step where Google in this case is providing what would
[978.64 → 983.86] otherwise be a very challenging specific task in a larger architecture. And they're helping us
[983.86 → 987.14] do that almost like a software component in a larger software system.
[987.14 → 992.48] I think that there's kind of two threads that I see running through this that are also kind of,
[992.48 → 998.04] you know, hugely impactful, I think, in the industry in general. One of those is transfer learning.
[998.28 → 1004.02] What here we're calling maybe the fine-tuning part where in transfer learning, you're taking something
[1004.02 → 1011.72] that was trained for a certain task and then updating it or fine-tuning it to another type of
[1011.72 → 1017.86] task. And as we've mentioned on the podcast before, I think that's hugely impactful and a huge benefit
[1017.86 → 1024.42] for actually people that are doing applied AI. The other thing is this multitask learning framework.
[1024.42 → 1030.54] I see that this is done in BERT. I also see it being done, like I mentioned, in the HMTL model
[1030.54 → 1038.12] and other cases where this encoder layer is being trained based on being able to do multiple tasks,
[1038.12 → 1043.54] not just one task. And I would highly recommend looking at that HMTL model as well.
[1043.62 → 1047.36] This is pretty impressive in that respect. Sounds good. Anything else?
[1048.14 → 1052.34] Well, I was just going to mention, as you can tell, I've kind of been sucked down the rabbit hole of
[1052.34 → 1057.88] BERT. But I did want to mention to people, again, this is open source, you can read the article from
[1057.88 → 1062.28] Google, but also you can go to their GitHub, and they have the pre-trained models that you can go
[1062.28 → 1068.42] ahead and use. But there's also actually already been an implementation in PyTorch by Hugging Face.
[1068.96 → 1074.04] And it's not maintained by the Google team, but by someone else. And I just thought it was pretty
[1074.04 → 1082.34] cool and useful to already see that implementation in PyTorch so soon after seeing the stuff come out of
[1082.34 → 1086.64] Google. So keep that in mind, whether you're working on PyTorch or TensorFlow, not that those are the only
[1086.64 → 1091.32] two, but I think that covers a lot of people, you'll be able to utilize this tech.
[1091.66 → 1097.04] That's true. And I think we end up talking about TensorFlow and PyTorch right now because there's so much
[1097.04 → 1101.78] coming out in terms of advancements being made, where people are really entering around those two
[1101.78 → 1107.62] platforms. But as you said, there are tons of great tools out there. We're not trying to exclude anyone on
[1107.62 → 1113.18] those. And we would love to hear back. If we are not talking about your favourite tool, as much as you'd like to
[1113.18 → 1118.08] hear, join us in the Slack community and tell us what you're doing in it. Because we really go out
[1118.08 → 1121.96] and see what people are writing and talking about. And then we end up talking about that on the show.
[1122.10 → 1127.96] So we definitely would love feedback. And whether it's that or other areas, steer us in directions you
[1127.96 → 1129.66] want to hear from. Yeah, definitely.
[1130.32 → 1137.64] So I noticed that there was another release. And this time it was from Facebook. They open sourced
[1137.64 → 1143.44] their applied reinforcement learning platform. It's called Horizon. And with that, I noticed that
[1143.44 → 1150.28] it's pretty cool. I think if you're not familiar with reinforcement learning, that is an aspect of
[1150.28 → 1157.06] machine learning where you are using a software agent to take actions that are in the environment
[1157.06 → 1162.08] that you're operating in. So if you have a model that you're developing and actions are being taken
[1162.08 → 1168.06] through those, you are trying to reward when things are going the right way, and you're trying to learn.
[1168.30 → 1174.32] So as your model is converging in the right direction, you reward it, and you don't reward
[1174.32 → 1180.04] it when it doesn't. And you see that in a lot of different applications, everything from different
[1180.04 → 1187.72] AI learning how to play games. You see it a lot in robotics. And so it's really great to see Facebook
[1187.72 → 1191.00] open sourcing how they're approaching that because they're doing a lot of work on this.
[1191.00 → 1192.54] Had you seen that one, Daniel?
[1192.92 → 1197.58] Yeah, it's definitely interesting to me. And I'll note as well, in a previous episode,
[1197.66 → 1203.94] so episode 14, Wojtek Marimba talked with us for a whole episode about reinforcement learning.
[1204.20 → 1210.50] It's an area that I definitely want to get up to speed on. So I did run across this. It was also one
[1210.50 → 1216.56] of the things that kind of crossed my path multiple times over the past couple of weeks. One of the
[1216.56 → 1222.08] interesting things that I thought was interesting about this framework that they open source, or
[1222.08 → 1227.56] really, it's more of a platform, right? So this reinforcement learning platform is that it's not
[1227.56 → 1232.94] kind of, it's not just like a specific library for PyTorch or something. It is actually like a platform
[1232.94 → 1240.64] that utilizes multiple open source projects to do, help you do the task of reinforcement learning.
[1240.64 → 1248.02] So I see that Spark is involved here along with PyTorch, along with SciPy, along with OpenAI Gem,
[1248.44 → 1252.24] and the Onyx framework, which I'm a big fan of and excited about.
[1252.58 → 1258.22] So you've got the kind of large scale data processing element that's kind of coming from Spark.
[1258.50 → 1264.46] You've got the scientific computing and numerical machine learning pieces coming from SciPy and PyTorch.
[1264.46 → 1269.72] And then there are other things as well, including model serialization and interoperability that's
[1269.72 → 1276.48] coming with Onyx. So it was really cool to see that this kind of convergence of multiple different
[1276.48 → 1283.30] projects to enable this, you know, what seems like a really great platform for actually enabling
[1283.30 → 1285.12] reinforcement learning and production.
[1285.52 → 1290.64] Yeah, I noticed I was looking across their GitHub page, thinking of it as a platform rather than just
[1290.64 → 1296.88] a library for another platform. You build it in Python using PyTorch for the modelling and the
[1296.88 → 1303.74] training, and then you can serve models with Cafe2. So it does have its does have dependencies with other
[1303.74 → 1308.74] platforms, specifically PyTorch and Cafe2, but it's a whole system unto itself.
[1309.28 → 1315.14] Yeah, yeah. And I don't know, this was actually pretty surprising to me. And maybe this is just my
[1315.14 → 1321.44] lack of following a lot of reinforcement learning things. But it was kind of a shock to me for them
[1321.44 → 1328.26] to describe how they are using how Facebook is using reinforcement learning in production.
[1328.26 → 1335.12] So they mentioned on Messenger, on 360 video and more. And that was a shock to me. If someone was to
[1335.12 → 1340.78] ask me before I read this article, you know, who was using reinforcement learning in production,
[1340.78 → 1347.78] I would probably just kind of give them a blurb about how it's mostly a research thing right now
[1347.78 → 1353.00] and OpenAI and DeepMind and other people are using it for robots and other things. But it's not really,
[1353.36 → 1359.18] it hasn't really filtered into production usage and industry. And clearly, I'm wrong about that,
[1359.34 → 1365.90] because they're using this, you know, practical platform for reinforcement learning in production,
[1365.90 → 1371.36] at least on at least on a few things that they say, you know, horizon has allowed us to improve
[1371.36 → 1378.52] the image quality of 360-degree video, optimizing bit rate parameters in real time and other things.
[1378.52 → 1385.50] So this is actually like, you know, real usage of reinforcement learning rather than just kind of
[1385.50 → 1390.36] like funny videos of robot arms and stuff. Yeah, this was a pretty big shock to me.
[1390.64 → 1395.10] I have seen it used in industry, but it was strictly in robotics. When I was with a previous employer,
[1395.10 → 1401.26] and we had several teams doing some fairly advanced robotics tasks, my team was not we were very much
[1401.26 → 1406.48] focused on the computer vision side of things with mask RCNN and other convolutional technologies.
[1407.02 → 1412.64] But yeah, I know another team that we were working with was doing reinforcement learning and deep
[1412.64 → 1417.74] reinforcement learning, where you're combining reinforcement learning with a deep architecture
[1417.74 → 1424.24] as well, to do that on the robotics side. And that's used a lot on kind of strategy for robotics
[1424.24 → 1430.36] movement and things. So but it had been that my own personal experience had been very specific to that
[1430.36 → 1436.56] use case. Yeah. And I mean, even so I'm looking at their GitHub page for horizon right now, and it says
[1436.56 → 1442.62] a platform for applied reinforcement learning or applied RL. And of course, that fits right in with
[1442.62 → 1448.30] what we're passionate about on this show, which is practicality. And this has definitely changed my
[1448.30 → 1454.12] perception of reinforcement learning outside of kind of the domain of robots like you were talking about,
[1454.20 → 1459.32] which I have never worked in robots. And so to me, reinforcement learning like didn't really
[1459.32 → 1466.02] come across as something that maybe I would apply directly, at least in the near future. But
[1466.02 → 1473.58] maybe I need to reevaluate my perceptions there. And actually, I'd love to just kind of go through and
[1473.58 → 1479.00] see. I haven't been through the all the docs of horizon, but it looks like that you can install
[1479.00 → 1484.58] it with Docker. So it would be fun to just kind of spin up horizon and say, at least say I've done
[1484.58 → 1490.44] some reinforcement learning, I feel like I could, you know, check that box off of my bucket list, at
[1490.44 → 1495.02] least. Absolutely. And I want to try to find a use case for both BERT and horizon from a learning
[1495.02 → 1502.12] standpoint, to dive into them. Because, you know, it's kind of funny, as we talk about these
[1502.12 → 1507.74] different things in the that are happening in the AI community on these fully connected episodes,
[1508.18 → 1512.94] it is, you have to really pick and choose what you want to do. But we're seeing so much advancement
[1512.94 → 1518.64] right now in these areas. So I'm trying to find ways of since you don't get to do everything in
[1518.64 → 1522.98] whatever job you're doing in the world, I'm trying to find small projects where we can apply those.
[1523.42 → 1527.52] So if anyone has ideas, I hope you'll share them in the Slack community or on LinkedIn,
[1527.98 → 1531.72] LinkedIn group, because that would be very welcome things that are scaled that are
[1531.72 → 1534.08] affordable for people to dive in and have fun with.
[1534.50 → 1539.76] Yeah. And we'll also, just so you guys know, we always try to include a bunch of links to what
[1539.76 → 1545.98] we're talking about in our show notes. So there's actually, I have a list here right now of all of
[1545.98 → 1550.10] the things about BERT. Like I said, there's been a lot, there's been a Google article, TensorFlow,
[1550.76 → 1556.04] GitHub, there's been a paper on the archive, the PyTorch repo, New York Times article.
[1556.04 → 1562.04] There's even like a collab notebook. It's like Jupiter notebook, but kind of Google Docs style.
[1562.18 → 1567.44] So there's one of those for you to try it out. Of course, like I mentioned, Horizon has the Docker
[1567.44 → 1574.28] install and all of that. So barriers to spinning up a lot of this stuff is a lot lower than it used
[1574.28 → 1579.70] to be, which like you mentioned, Chris, in some ways it's, I mean, in a lot of ways it's super
[1579.70 → 1586.14] exciting, but in other ways it's like, there's too much to try. So I probably need to focus my
[1586.14 → 1592.06] attention a little bit, but yeah. So I think that was pretty much the what we had to say
[1592.06 → 1597.86] about Horizon. I'm excited to dig in more. Have you seen anything else in the, in the news recently,
[1597.98 → 1598.86] Chris, that you want to highlight?
[1599.14 → 1605.02] Yeah. I ran across a blog article that's called does synthetic data hold the secret to artificial
[1605.02 → 1611.60] intelligence. And it caught my eye kind of dives into just in general about synthetic data and how
[1611.60 → 1617.24] it's used and in terms of generating enough data to operate on. The reason it really caught my eye is
[1617.24 → 1623.80] I had some personal experience from my own work having to do a synthetic data. And I also was
[1623.80 → 1630.82] interviewed a short while back by Thompson Reuters on a series of AI articles that they were posting
[1630.82 → 1634.74] on that. And I've tweeted, if anyone has an interest, I've tweeted about it and stuff,
[1634.78 → 1640.34] and you can find the article, but really talking about using synthetic data going forward to generate
[1640.34 → 1646.84] larger data sets, how it fits into unsupervised learning for the future. And in my own experience,
[1646.84 → 1652.08] I found a lot of people tend to say, yeah, we'll just synthesize the data, you know, and there's a
[1652.08 → 1657.40] variety of techniques for that. We found it very hard to do that. And I'm hoping that on our,
[1657.40 → 1662.04] on my own learning curve that me and the people on the teams that I've worked with can, can figure
[1662.04 → 1666.62] out better, but that can be really challenging. So the article caught my eye because of the
[1666.62 → 1670.58] the hope forward. And I, and as well as everybody does, I would love to be able to say,
[1670.70 → 1675.64] if I want to hit a particular use case and don't have sufficient data, we can go synthesize the data
[1675.64 → 1681.70] and train it. When we were doing that manually in terms of trying to generate through a number of
[1681.70 → 1687.24] automated things at a company I used to work at, we found that the, the data set, we had a small data set,
[1687.24 → 1693.32] that represented the real life problem that we were tackling. And I'm not allowed to disclose
[1693.32 → 1699.46] what that was, but we also, we didn't have nearly enough to address it. And so I, we, we went and
[1699.46 → 1703.90] tried to synthesize it through a bunch of different techniques. And we found that the we really had a
[1703.90 → 1709.76] struggle with getting enough diversity into the data. We could generate the volume, but it was very
[1709.76 → 1714.94] hard to synthesize the diversity that we needed to where our goal had been, if you take a synthetic
[1714.94 → 1719.90] data set and compare it side by side with the real much smaller data set that we already had,
[1719.98 → 1725.22] that it would be indistinguishable or close to that. So I would love to hear back from listeners.
[1725.22 → 1729.70] And I would love to hear Daniel, if you have any thoughts on that about how people are approaching
[1729.70 → 1734.80] synthetic data and, and some of the different techniques and successes or failures that they've
[1734.80 → 1735.02] had.
[1735.02 → 1740.68] Yeah. Maybe just to kind of, uh, pause a little bit, because I, I actually, I don't have a lot of
[1740.68 → 1745.74] experience, this whole idea of, of synthetic data, but you know what I'm thinking when I hear you talk
[1745.74 → 1751.46] about this is like, you know, Hey Chris, like what exactly do you mean by synthetic data? Because, uh,
[1751.46 → 1756.82] isn't data just data? I think you kind of got into that, but maybe you could describe like maybe a
[1756.82 → 1759.94] little bit more about why there is a need for synthetic data.
[1759.94 → 1764.34] That's a great point. So I'm kind of referencing in my brain, my own project, but because of
[1764.34 → 1770.46] non-disclosure issues, I can't address it directly. So I'll, I will try. It is oftentimes the case in,
[1770.46 → 1775.80] in industry, in the real world, when you're trying to tackle a business problem in the case that we
[1775.80 → 1783.12] were in, it was to enhance an existing product, and you will say, okay, this is what we need to go
[1783.12 → 1788.96] solve that problem for training purposes. And, but when you look at the amount of data that you have,
[1788.96 → 1793.86] you realize that you might need hundreds of thousands of records or millions of records to
[1793.86 → 1800.34] train against, and you might have, you know, a 2000 or, or less, maybe a few hundred. And that's,
[1800.46 → 1805.68] and that might not be nearly enough to get a high quality model trained for your purposes. So one of the
[1805.68 → 1812.04] things that people will do is say, are there ways that we can generate our own sense of reality that
[1812.04 → 1816.74] looks very much like the real thing. So you're generating more data that looks a lot like the
[1816.74 → 1821.54] data that you already have, but you need more volume. And there's a number of different software
[1821.54 → 1826.12] packages that can help you do that. And we tried some different techniques in this project that we
[1826.12 → 1832.54] were working on. The challenge that we had there been, was simply having enough variability, enough
[1832.54 → 1838.48] diversity in the synthesized data so that if you were to hold those two data sets up, the synthesized
[1838.48 → 1843.82] versus the real life one, the real life one was messy. It had all the, the little tweaks and
[1843.82 → 1849.16] diversity as you change things in real life, and you get noisy, messy data to train off of that
[1849.16 → 1853.46] represents the real world that you're trying to, to get a model to represent. That's what it is.
[1853.54 → 1858.26] It's very hard to do, at least in the stuff that we had done, it was very hard to generate synthesized
[1858.26 → 1863.88] data that didn't look synthesized, that had so much diversity that you would never realize it was
[1863.88 → 1868.52] generated. The number of different options for various inputs, that kind of thing. As I go forward,
[1868.58 → 1872.62] and I, I'm sure this will come up in the not too distant future where we have to take a synthetic
[1872.62 → 1877.04] data approach. I'm looking forward to having other people out there say, Hey, this is what
[1877.04 → 1881.76] worked for me or what didn't work for me. Yeah. I was just looking as, as you were talking, um,
[1881.96 → 1887.76] at, you know, models like we're talking about here, which I'm, I'm assuming like the models that you
[1887.76 → 1892.24] were talking about in, in your use case, but other cases like robotics or natural language,
[1892.24 → 1898.24] like the BERT model, uh, says it has, you know, like, you know, hundreds of, of millions of parameters,
[1898.24 → 1904.72] right? So to train that many parameters to fit that many parameters takes an enormous amount of
[1904.72 → 1910.04] data usually, which sometimes you just don't have, don't have access to. I'm glad you brought up this
[1910.04 → 1914.78] point. It's something that I definitely feel like I need to learn a little bit more about and I would
[1914.78 → 1919.82] be interested to hear from any of our listeners if they have good resources or pointers on, on that
[1919.82 → 1924.26] front. Yeah. I would note the use case that we were generating from, I'll say it was not a
[1924.26 → 1929.32] convolutional. I've also done it on the convolutional side with more success because you can take the
[1929.32 → 1933.34] images that you're using in your convolutional neural network and make adjustments. You can change
[1933.34 → 1938.70] angles, change sizing, flip them or some sort of stuff. Yeah. There's a lot of image manipulation
[1938.70 → 1943.98] things you can do to generate more data there. So had great success there. Unfortunately, the use case
[1943.98 → 1949.10] that I was kind of describing around was not that. So I just wanted to, to, to distinguish between
[1949.10 → 1952.46] the two. I think it's, I think it's easier with certain types of architectures than others.
[1952.46 → 1959.12] Yeah. Yeah. Well, on that note, you know, noting that we, we all have a lot to learn about multiple
[1959.12 → 1963.90] things. Let's go ahead and, you know, move into the part of fully connected where we, where we
[1963.90 → 1968.50] highlight a couple of learning resources that have been useful for us or look interesting.
[1968.68 → 1972.98] The first one that I'm going to point out, which is something that I want to look into a little bit
[1972.98 → 1979.94] more and maybe order the physical copy of is, um, this is a new or almost, I don't know if it's
[1979.94 → 1987.38] actually out yet, but, um, it's called grokking deep learning. And there's a physical and e-book
[1987.38 → 1992.64] from Manning called grokking deep learning. But one of the things that I was looking at was that
[1992.64 → 2000.18] there's also a kind of companion GitHub repository, which itself is kind of helpful, even maybe even
[2000.18 → 2005.54] without the book, because it goes through like from the beginning, kind of from scratch, how do we,
[2005.54 → 2010.92] how do we kind of understand and dig into deep learning? So it goes through, you know, forward
[2010.92 → 2016.58] propagation and introduction to neural networks, gradient descent, generalizing that back propagation,
[2016.80 → 2023.50] regularization, activation functions, and really kind of starts to pick apart like convolutional layers
[2023.50 → 2029.06] and word embeddings and other things more from a scratch perspective and trying to get into those
[2029.06 → 2034.94] things. So I think that this would be a great thing to go through if you're wanting to really kind of
[2034.94 → 2040.54] understand deep learning and neural networks at a more granular level.
[2040.78 → 2046.90] I have the book and have read it, and it is very good, um, compared to a lot of books where,
[2047.16 → 2050.82] where they don't give you a sufficient understanding. The grokking part of the title,
[2050.82 → 2055.96] I think is accurate in that they, is that the author really tries to explain those. And so having,
[2056.12 → 2060.56] having the examples in the GitHub, which I had not looked at actually, is really nice to have
[2060.56 → 2064.78] in the book. So I know I've read that and enjoyed reading it and thought it was one of the better
[2064.78 → 2067.30] explanations out there. So definitely concur with that.
[2067.30 → 2071.72] Well, I'm glad that, uh, that I wasn't making, uh, wrong assumptions there.
[2072.22 → 2078.04] The I have one that's very specific. I've done other, uh, I've, I've talked about this in different
[2078.04 → 2084.50] articles, but there on medium, I found a medium post. I probably am going to butcher the name. It's,
[2084.50 → 2091.28] uh, Natalie jeans, J E A N S on medium. It looks like it's her only article that I see here,
[2091.28 → 2095.24] but it's the back propagation algorithm demystified. And it's another perfect
[2095.24 → 2100.40] explanation. A lot of people is, is we're getting into the field, you know, this one of the, the very
[2100.40 → 2104.66] first things you learn. And actually, and you haven't been exposed to back propagation, it can
[2104.66 → 2109.56] take a while to really understand it and get it. And so I thought this was one of those articles
[2109.56 → 2113.36] that if you're a newbie into the field, and you're trying to understand just how feed forward
[2113.36 → 2118.52] with that propagation works, this is another good place to start. She takes you kind of through the
[2118.52 → 2125.06] initial concepts about, you know, the, the inputs to a node and what it means to have an activation
[2125.06 → 2130.26] function and, and what those are and kind of describes back propagation at high level. And then
[2130.26 → 2135.96] she goes into gradient descent and there's, that's a group of different related algorithms,
[2136.12 → 2141.42] gradient descent that allow you to minimize your error. And she has some good visuals and some great
[2141.42 → 2147.14] explanation on that. She talks about what those different variants are, and then kind of takes you
[2147.14 → 2153.66] through some examples using sigmoid, which is not often used in real life these days, but is a
[2153.80 → 2158.30] is a good training tool that people will use. And then actually goes to what people do use in real life,
[2158.34 → 2164.94] which is back propagating rectified linear units, or you might hear it as rely. And so did a good job
[2164.94 → 2170.80] of kind of giving you a good, a good stab at understanding that is. So I hope people will
[2170.80 → 2174.80] go see it. We'll put the link in the show notes and that's it for me this week. You have anything
[2174.80 → 2179.28] else, Daniel, or are you? Nope, that's it. I think those are great. And I think it's great that you
[2179.28 → 2184.54] brought up today how, you know, we just like everyone else, even though they don't always admit it,
[2184.66 → 2190.04] are always searching through Quora, always searching through Stack Overflow and, and GitHub and
[2190.04 → 2195.08] papers and all of that. If you, if you run across any good ones that we haven't highlighted, let us
[2195.08 → 2201.22] know on our Slack team. And, and yeah, it was, it was great discussion today. Thanks for being patient
[2201.22 → 2206.64] with me, Chris, and helping me dig through some of these things. Yeah, I had, I had a good time. This
[2206.64 → 2211.54] was a slightly different type of show than anything we've done in terms of our, just you and me digging
[2211.54 → 2217.16] in ourselves and digging in not as experts, but as many of our listeners just trying to, to take it.
[2217.16 → 2222.04] So I hope it made sense to our listeners. And if we get good feedback, I'm looking forward to,
[2222.04 → 2226.30] to talking about specific technologies some more in the future. Awesome. Okay. Well,
[2226.32 → 2231.66] I hope everybody has a great week, and we will talk to you sometime soon. Talk to you later, Daniel.
[2232.00 → 2233.32] All right. See you, Chris. Okay. Bye-bye.
[2236.26 → 2240.44] All right. Thank you for tuning into this episode of Practical AI. If you enjoyed this show,
[2240.50 → 2245.40] do us a favour, go on iTunes, give us a rating, go in your podcast app and favourite it. If you are on
[2245.40 → 2248.98] Twitter or a social network, share a link with a friend, whatever you got to do, share the show
[2248.98 → 2253.52] with a friend. If you enjoyed it and bandwidth for change log is provided by fast learn more
[2253.52 → 2257.96] at fastly.com. And we catch our errors before our users do here at change log because of Rollbar.
[2257.96 → 2263.36] Check them out at robot.com slash change log. And we're hosted on Linde cloud servers.
[2263.70 → 2268.72] Head to lino.com slash change log. Check them out. Support this show. This episode is hosted by
[2268.72 → 2274.58] Daniel Whiten ack and Chris Benson. Editing is done by Tim Smith. The music is by Break master Cylinder.
[2274.58 → 2279.80] And you can find more shows just like this at change log.com. When you go there, pop in your
[2279.80 → 2284.68] email address, get our weekly email, keeping you up to date with the news and podcasts for developers
[2284.68 → 2288.98] in your inbox every single week. Thanks for tuning in. We'll see you next week.
[2294.52 → 2299.44] I'm Tim Smith and my show away from keyboard explores the human side of creative work.
[2299.44 → 2304.98] You'll hear stories sometimes deeply personal about the triumphs and struggles of doing what
[2304.98 → 2310.34] you love. I ended up in hospital with burnout. I just kept ignoring the way that it was making
[2310.34 → 2315.24] me feel and just kept powering through it. And then eventually my body started to give me physical
[2315.24 → 2320.68] symptoms to say like, Hey, you should stop and listen to me. New episodes premiere every other
[2320.68 → 2325.74] Wednesday. Find the show at change log.com slash AFK or wherever you listen to podcasts.
