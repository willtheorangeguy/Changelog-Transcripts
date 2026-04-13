[0.00 --> 5.56]  With current technology the way it is more or less right now in 2022, you could have
[5.56 --> 12.12]  thousands, tens of thousands, hundreds of thousands of tasks that are trained in a very
[12.12 --> 14.54]  narrow task-oriented model.
[14.54 --> 17.52]  So could you have fully automated brain surgery?
[17.80 --> 18.28]  Maybe.
[18.74 --> 24.50]  But that's what I think about a lot more in terms of the AI ethical concerns going into
[24.50 --> 28.96]  the future is all of the models and handing our life over to all the models rather than
[28.96 --> 32.72]  one super knowledgeable model that rules them all, which is a fiction.
[35.98 --> 38.64]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[39.02 --> 39.58]  We love Linode.
[39.66 --> 41.08]  They keep it fast and simple.
[41.20 --> 43.56]  Check them out at linode.com slash changelog.
[43.56 --> 45.86]  Our bandwidth is provided by Fastly.
[46.22 --> 49.76]  Learn more at Fastly.com and get your feature flags powered by LaunchDarkly.
[50.02 --> 51.76]  Get a demo at LaunchDarkly.com.
[52.84 --> 54.10]  Hey, Jared here.
[54.62 --> 58.92]  One of the things we can count on in the software industry is change.
[59.62 --> 64.22]  The state of the art changes so fast, in fact, that keeping up can feel like a whole other
[64.22 --> 66.14]  job on top of your actual job.
[67.04 --> 69.02]  That's why we created Change Log Weekly.
[69.62 --> 73.90]  It's our totally free newsletter that we drop in your inbox each and every Sunday.
[74.54 --> 79.50]  We link to the latest news, the best articles, and the most interesting projects that you
[79.50 --> 80.18]  should be aware of.
[80.86 --> 85.40]  We also add a little commentary from us saying why something's important, pointing you to
[85.40 --> 88.92]  other instances of a trend, or just making a dorky joke to keep it lively.
[89.50 --> 94.46]  So if you haven't yet, I recommend subscribing to Change Log Weekly and help us help you keep
[94.46 --> 95.08]  up with the latest.
[96.04 --> 99.26]  Head to changelog.com slash weekly and sign up today.
[99.48 --> 102.04]  Again, it's totally free and we never spam you.
[102.16 --> 102.50]  Yuck.
[103.38 --> 106.88]  One last time, that's changelog.com slash weekly.
[106.88 --> 124.48]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[124.76 --> 126.54]  productive, and accessible to everyone.
[126.84 --> 130.94]  This is where conversations around AI, machine learning, and data science happen.
[130.94 --> 135.42]  Join the community and Slack with us around various topics of the show at changelog.com
[135.42 --> 137.30]  slash community and follow us on Twitter.
[137.44 --> 139.00]  We're at Practical AI FM.
[145.30 --> 150.18]  Well, welcome to another fully connected episode of Practical AI.
[150.54 --> 155.10]  In these episodes, Chris and I keep you fully connected with everything that's happening in
[155.10 --> 155.98]  the AI community.
[155.98 --> 161.60]  We'll take some time to discuss the latest AI news and dig into some learning resources
[161.60 --> 164.32]  to help you level up your machine learning game.
[164.60 --> 165.80]  I'm Daniel Whitenack.
[165.90 --> 172.10]  I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[172.10 --> 174.82]  Benson, who is a tech strategist at Lockheed Martin.
[175.40 --> 175.96]  How are you doing, Chris?
[176.18 --> 177.22]  I'm doing very well, Daniel.
[177.32 --> 178.10]  How are you doing?
[178.20 --> 181.86]  I know you had been out with COVID like almost everybody else on the planet.
[182.38 --> 183.10]  Are you better?
[183.30 --> 184.64]  Yes, much better.
[184.64 --> 189.26]  Yeah, I mean, for listeners that are maybe just jumping in at this episode, I've been
[189.26 --> 196.08]  out for a couple of recordings, had the COVID overall, though I count myself very blessed
[196.08 --> 201.76]  because I didn't have the severe symptoms that some people had.
[202.16 --> 206.88]  Definitely had some, but not near as bad, of course, is what a lot of people are dealing
[206.88 --> 207.14]  with.
[207.28 --> 209.68]  So I count myself blessed in that regard.
[209.92 --> 212.46]  And yeah, it's good to be back in action.
[212.74 --> 213.50]  Welcome back, buddy.
[213.50 --> 214.52]  Yeah, good to be back.
[214.58 --> 219.86]  It was awesome to have Natalie Pistunovic fill in and a couple of recordings for me.
[220.12 --> 221.36]  She did a fantastic job.
[221.54 --> 222.02]  Very good.
[222.20 --> 223.86]  Yeah, she's awesome.
[224.12 --> 226.06]  Love her insights on everything.
[226.40 --> 233.06]  And, you know, it's kind of fun to be able to listen to my favorite AI podcast without my
[233.06 --> 233.86]  voice on it.
[235.14 --> 240.52]  You know, I don't know if that's if that's OK for me to call this my favorite AI podcast.
[240.52 --> 241.04]  It is.
[241.16 --> 242.00]  It has to be.
[242.12 --> 243.68]  I'm going to be worried if it isn't.
[243.78 --> 243.94]  OK.
[245.04 --> 245.40]  Yeah.
[245.74 --> 251.90]  So, yeah, I mean, it's cool to I do listen to some of our episodes where I am on it.
[252.18 --> 254.38]  And, you know, obviously, I'm part of the conversation.
[254.38 --> 255.62]  So I remember what's going on.
[255.66 --> 259.40]  But I gain a lot out of these podcast episodes.
[259.40 --> 265.40]  And actually, I just had a conversation with someone there asking me with doing the podcast
[265.40 --> 270.40]  and kind of interacting with all sorts of AI people across industry.
[270.56 --> 277.80]  How has it shifted some of how you think about AI or the industry or something?
[277.88 --> 279.72]  I thought that was a really interesting question.
[280.04 --> 281.88]  I don't know how you'd answer that, Chris.
[281.88 --> 290.50]  I think I said something, you know, like it's encouraging to learn from so many people that
[290.50 --> 292.98]  have really deep knowledge in different areas.
[292.98 --> 300.60]  But it sort of also reinforces that idea that everyone, even though they might seem like an
[300.60 --> 303.54]  expert in all areas, then there are some people like that.
[303.64 --> 307.44]  But most people have a sort of very deep knowledge in a certain area.
[307.44 --> 311.98]  So that's kind of what breeds this kind of imposter syndrome thing.
[312.18 --> 318.26]  And so to be able to, I think, over time, talk with so many kind of luminaries and experts
[318.26 --> 324.68]  in different areas, it's cool for one to learn from them, but also to just talk to them and
[324.68 --> 331.80]  feel like they sort of accept you and are excited to talk to you about what they're doing and don't
[331.80 --> 335.02]  view, you know, because we're not experts in those areas.
[335.02 --> 338.16]  But a lot of the people we have on are very gracious.
[338.62 --> 343.30]  And so, yeah, maybe that's my insight is that there's just a lot of very gracious people
[343.30 --> 344.06]  in the industry.
[344.62 --> 348.46]  I'm sure that there's many that aren't, but being able to learn from them.
[348.60 --> 350.92]  And yeah, that's kind of what came to mind.
[351.00 --> 353.02]  I don't know if anything comes to mind on your own.
[353.30 --> 354.16]  I think that's well said.
[354.32 --> 358.10]  I wasn't expecting to go here, but, you know, it's us talking about kind of that.
[358.30 --> 361.62]  We've been doing this for about three years, getting close to three years now.
[361.62 --> 367.34]  And having done that on a more or less weekly basis over that time, we've gotten to talk
[367.34 --> 369.36]  to so many really interesting people.
[369.54 --> 370.48]  They come on.
[370.86 --> 371.48]  We haven't.
[371.58 --> 374.50]  Maybe we've just lucked out and we've only found the gracious ones.
[375.04 --> 376.18]  But they're so human.
[376.36 --> 380.38]  And it's the human touch around the technology that makes it special.
[381.04 --> 382.64]  And so that's really what.
[382.88 --> 386.62]  And then the other thing that I would notice, and I think it would be the same whether you're
[386.62 --> 391.48]  a listener or whether you're the host like us, is that you're privy to this conversation
[391.48 --> 394.76]  and it kind of keeps you out of some very narrow bubbles.
[395.04 --> 397.82]  You know, we're still kind of in the AI bubble as an industry.
[398.22 --> 403.56]  But I know that, you know, if I go to my employer, there's a particular way we think at any given
[403.56 --> 405.78]  employer and it gives you perspective.
[405.78 --> 411.08]  And you hear really smart, amazing people saying things that you can learn from.
[411.18 --> 412.52]  I think that enriches us all.
[412.52 --> 417.88]  I've seen this with other podcasts as well and other just like, I mean, if you read books,
[418.00 --> 423.72]  this is something that happens to where you sort of you don't remember everything, but
[423.72 --> 430.58]  you sort of have this low level remembrance of certain ideas and technologies and products
[430.58 --> 431.58]  or whatever it is.
[431.58 --> 437.64]  And so when you're in conversations in your job and someone brings up like, oh, well, we
[437.64 --> 441.88]  need to like label things in this way or, oh, we're having this problem.
[441.88 --> 447.04]  I'm not sure like how then it's sort of like all of a sudden something comes out of that
[447.04 --> 452.58]  like soup of of things you've you've sort of stored away and is really useful.
[452.58 --> 456.18]  So, yeah, I found that as a as a really interesting benefit.
[456.66 --> 458.36]  Yeah, it definitely expands the mind.
[458.48 --> 463.96]  I know as my own day job, not in the podcast, has evolved over time and I've moved from very
[463.96 --> 468.92]  focused on the deep learning stuff to I'm also now looking forward a lot.
[468.92 --> 470.90]  And, you know, kind of the what's next.
[470.98 --> 472.12]  It may not be here yet.
[472.22 --> 475.92]  All that and ethics things and ethics things, which are huge.
[476.08 --> 480.18]  You know, these are big, big parts of not only the industry, but it affects everybody
[480.18 --> 480.68]  now.
[480.88 --> 486.04]  So it's a very cool time to be alive and participating in things.
[486.12 --> 488.80]  I know a lot of people focus on all the negatives in the world.
[488.80 --> 490.14]  And there are there are many.
[490.32 --> 493.26]  We are in the middle, maybe approaching the end.
[493.26 --> 495.82]  We'll have to see of a global pandemic.
[495.82 --> 501.06]  We've had all sorts of crazy politics in recent years, lots of of challenges.
[501.82 --> 506.82]  But I still my my daughter was asking me the other day, if you what historical period would
[506.82 --> 507.62]  you choose to be a part of?
[507.64 --> 508.42]  And I said, this is it.
[508.48 --> 509.24]  You know, we're living it.
[509.58 --> 510.64]  This is a cool moment.
[510.64 --> 513.44]  And, you know, someday this is going to evolve.
[513.54 --> 517.22]  We'll have we'll have things like quantum AI eventually.
[517.50 --> 518.44]  I don't think we're there yet.
[518.52 --> 518.72]  Yeah.
[518.78 --> 519.94]  But it will happen someday.
[520.10 --> 521.20]  So, yeah, pretty cool.
[521.20 --> 522.12]  Yeah, yeah.
[522.56 --> 529.30]  Well, I mean, I guess on that note, with the sort of theme of of health things and trending
[529.30 --> 536.34]  news and all that, I know just to get into some of the AI news things that happened in
[536.34 --> 541.04]  recent times, both you and I kind of sent each other the same link.
[541.22 --> 541.52]  I know.
[541.58 --> 542.30]  Yeah, we did.
[542.58 --> 547.32]  Which was this work about proteins attaching.
[547.56 --> 547.82]  Yes.
[547.82 --> 551.54]  Which people might might not know why that's.
[551.68 --> 553.96]  Yeah, we found two different references to the same thing.
[554.20 --> 557.24]  It was the same thing written by two different online things.
[557.38 --> 560.20]  But clearly it was something that mattered to both of us.
[560.24 --> 560.98]  I didn't mean to cut you off.
[561.02 --> 561.26]  Go ahead.
[561.50 --> 562.12]  No, no.
[562.24 --> 567.86]  I was just thinking like people might be wondering why like proteins attaching.
[567.86 --> 573.46]  It seems like sort of a random, random thing, especially for like myself.
[573.46 --> 580.96]  I am not I don't have a lot of biology knowledge or like that sort of I'm not familiar with
[580.96 --> 582.66]  that side of of things.
[582.66 --> 589.04]  But the idea here is that, you know, there are things like viruses, which we're familiar
[589.04 --> 592.32]  with, like the virus that causes COVID-19.
[592.76 --> 598.42]  It's like something that it attacks, but you can attach things to it.
[598.42 --> 598.72]  Yes.
[598.72 --> 600.32]  Like these virus spikes.
[601.04 --> 608.02]  So there's like antibodies that can bind with the virus spike proteins to prevent the virus
[608.02 --> 609.74]  from entering a human cell.
[609.82 --> 613.36]  So it's almost like one way to fight this sort of virus.
[613.36 --> 616.96]  And I'm speaking way above beyond what I know about biology.
[616.96 --> 623.38]  But, you know, I think we've all learned a bit about viruses and and vaccines in recent
[623.38 --> 623.68]  years.
[623.80 --> 623.98]  Yeah.
[623.98 --> 629.36]  But yeah, one of the ways to sort of think about this vaccine or fighting a virus is attaching
[629.36 --> 636.46]  things to it, to the virus like proteins to prevent it from entering our cells.
[636.84 --> 638.96]  So that's kind of the context of this.
[638.96 --> 644.50]  And this article, it uses COVID kind of as the example of why it's important, because it's
[644.50 --> 645.74]  such a relevant thing right now.
[646.04 --> 647.72]  Antibodies are proteins themselves.
[648.12 --> 653.94]  And so this ability for these complex molecules, in this case, proteins, to be able to
[653.94 --> 656.46]  to do attachment and to figure out what it's going to be.
[656.78 --> 658.32]  It's a very difficult thing.
[658.72 --> 664.22]  AI, as it's done in so many other kind of pattern matching use cases, is doing an amazing
[664.22 --> 664.68]  job.
[664.68 --> 668.70]  But I think the thing for me, this one struck a personal note, which I'm going to share,
[669.14 --> 675.66]  because lately on several occasions and as recently as this morning, as we record this,
[676.06 --> 682.30]  I was talking to a friend who has a PhD from Harvard University in chemistry.
[682.30 --> 685.98]  This person really, really knows chemistry well.
[686.18 --> 691.44]  And we were talking more or less about this topic, not in terms of COVID, but we were talking
[691.44 --> 695.00]  in terms of the fact that I'm vegan, he's not.
[695.14 --> 701.08]  And he loves teasing me about all the challenges vegans have getting nutrition.
[701.88 --> 703.48]  And I said, well, you know what?
[703.54 --> 709.70]  You need to help me with your chemistry PhD find a way for me as a vegan to get all the
[709.70 --> 710.48]  things that I need.
[710.62 --> 713.08]  And we got into a, I am not a chemist.
[713.18 --> 715.28]  I know just enough to have a conversation.
[715.28 --> 717.42]  And we got into a conversation about that.
[717.80 --> 721.78]  And then I saw this article and I was like, okay, we really want to talk about that today.
[721.84 --> 722.48]  At least I do.
[722.68 --> 723.64]  And I was glad you did.
[723.64 --> 729.52]  So yeah, maybe a side outcome of this work is nutrients for vegans.
[729.52 --> 733.74]  There's so many things in medicine and nutrition and stuff that this could help.
[733.74 --> 743.26]  Yeah, it's very interesting that how computers doing this sort of task are working with expert,
[743.52 --> 750.66]  you know, biologists and chemists and drug developers to produce things much, much quicker
[750.66 --> 756.14]  than they could otherwise, which brings up like all sorts of like, I think it is a really
[756.14 --> 763.96]  good example of like humans and machines working together very closely with a lot of benefit
[763.96 --> 770.20]  because no one would want like your machine to sort of like combine a bunch of things together
[770.20 --> 772.72]  virtually and say like, here's the vaccine.
[772.72 --> 776.30]  And like, you know, then they just go out and produce it.
[776.42 --> 780.62]  And that's that like, there has to be a human element in this process still.
[780.62 --> 787.40]  And my understanding is the sort of machine learning model is doing a lot of this brute
[787.40 --> 791.84]  force stuff that was very time consuming before with previous software products.
[792.00 --> 798.82]  So it kind of directly predicts complexes that will form when two proteins bind together.
[799.06 --> 799.16]  Yeah.
[799.32 --> 806.64]  And so it's talking about it doing it, you know, 80 to 500 times faster and potentially more
[806.64 --> 807.82]  more accurately.
[807.82 --> 813.72]  So you just sort of think about like, this is probably, and you know, again, I'm speaking
[813.72 --> 819.90]  outside my expertise here, but this is probably like in past time stages of the process that
[819.90 --> 824.06]  were really like the humans didn't even enjoy this bit.
[824.14 --> 828.68]  I would imagine like just like searching through structures and kind of combining.
[828.68 --> 830.04]  Oh God, you haven't met my friend.
[830.04 --> 838.02]  And I don't know, like, it seems like the, like a, yeah, manual grid search sort of like
[838.02 --> 838.44]  thing.
[838.80 --> 842.80]  As an analogy, you know, how you always talk about how you love to clean data, you know,
[842.82 --> 846.34]  all the things that the rest of us complain about and get, you know, grumble about.
[846.44 --> 847.26]  And you love that.
[847.36 --> 849.20]  There are people that love to do this.
[849.36 --> 851.56]  Love just like looking at structures.
[851.82 --> 851.94]  Yeah.
[852.00 --> 856.72]  And there's a lot of variability and you know, there can be so many combinations.
[856.72 --> 858.52]  I'm not going, you know, I'm assuming millions.
[858.64 --> 859.44]  I'm not going to speculate.
[859.88 --> 865.98]  One of the coauthors, and I'm going to butcher his name, Octavian Eugen Ganya, maybe, I hope.
[866.08 --> 869.98]  And if I have mispronounced your name, sir, I sincerely apologize on that.
[870.20 --> 874.42]  But he made the comment, deep learning is very good at capturing interactions between
[874.42 --> 879.36]  different proteins that are otherwise difficult for chemists or biologists to write experimentally.
[879.36 --> 884.18]  And some of those interactions are very complicated and people have not found good ways to express
[884.18 --> 884.58]  them.
[884.66 --> 888.18]  So the deep learning model can learn these types of interactions from the data.
[888.30 --> 894.32]  So kind of a classic deep learning task, just not, you know, one that those of us not
[894.32 --> 897.22]  in chemistry might not have thought about previously.
[897.22 --> 913.62]  We are going to ship.
[913.78 --> 916.28]  Three, two, one.
[916.74 --> 922.02]  I'm Karhal Azu, host of Ship It, a show with weekly episodes about getting your best ideas
[922.02 --> 924.02]  into the world and seeing what happens.
[924.02 --> 929.42]  We talk about code, ops, infrastructure, and the people that make it happen like charity
[929.42 --> 930.50]  majors from Honeycomb.
[930.92 --> 933.78]  We act like great engineers make great teams.
[933.98 --> 935.42]  And it's exactly the opposite.
[935.62 --> 939.04]  In fact, it is great teams that make great engineers.
[939.44 --> 942.96]  And they finally win the founders of continuous delivery.
[943.30 --> 946.10]  Start off assuming that we're wrong rather than assuming that we're right.
[946.38 --> 948.98]  Test our ideas, try and falsify our ideas.
[949.14 --> 951.12]  Those are better ways of doing work.
[951.18 --> 953.42]  And it doesn't really matter what work it is that you're doing.
[953.42 --> 955.26]  That stuff just works better.
[955.82 --> 961.24]  We even experiment on our own open source podcasting platform so that you can see how
[961.24 --> 966.82]  we implement specific tools and services within changelog.com, what works and what fails.
[967.18 --> 971.06]  It's like there's a brand new hammer and we grab hold of it and everyone gathers around.
[971.16 --> 974.96]  We put our hand out and we strike it right on our thumb.
[975.14 --> 978.04]  And then everybody knows that hammer really hurts.
[978.18 --> 980.68]  When you strike it on your thumb, I'm glad those guys did it.
[980.74 --> 981.56]  I've learned something.
[981.56 --> 982.36]  Instead, yeah.
[982.52 --> 987.10]  I think that's a very interesting perspective, but I don't see it that way.
[987.28 --> 987.52]  Okay.
[987.64 --> 990.74]  It's an amazing analogy, but I'm not sure that applies here.
[991.06 --> 993.38]  Listen to an episode that seems interesting or helpful.
[993.54 --> 995.18]  And if you like it, subscribe today.
[995.30 --> 996.40]  We'd love to have you with us.
[996.40 --> 1021.40]  I also noticed, Chris, that some of what was done with this protein attaching model thing
[1021.40 --> 1029.00]  had to do with sort of very interesting data structures and how they're kind of processed
[1029.00 --> 1035.94]  into the neural network, where here we have sort of 3D structures, these 3D protein structures.
[1036.94 --> 1042.60]  And from what I'm understanding here, they sort of convert those 3D protein structures into
[1042.60 --> 1046.36]  3D graphs, which are processed by the neural network.
[1046.36 --> 1052.08]  And, of course, that also fits a theme that we've been seeing in really the past sort of
[1052.08 --> 1058.82]  year and a half or more, where people are really exploring graph-structured data and putting
[1058.82 --> 1064.06]  in graph-structured data into neural networks in very interesting ways.
[1064.44 --> 1069.72]  So, like, a sort of different type of data was used here, which is pretty interesting.
[1069.72 --> 1075.08]  That, I guess, kind of leads me to one other thing that I wanted to bring up, which is related
[1075.08 --> 1083.58]  to the types of data that we process with neural networks, which is this data-to-vec project
[1083.58 --> 1084.70]  from Meta-AI.
[1085.02 --> 1085.22]  Okay.
[1085.38 --> 1093.70]  So, people might have heard of sort of Word-to-vec or maybe certain types of image-to-vec things
[1093.70 --> 1099.54]  or image feature extraction or word embedding or, you know, feature representation type of
[1099.54 --> 1099.90]  things.
[1100.30 --> 1108.18]  All of these sorts of things fit into kind of some type of category where you have a neural
[1108.18 --> 1116.00]  network model and the sort of pre-training of that model helps you pre-train vectors or
[1116.00 --> 1122.76]  embeddings or representations of some type of data that you put in that then can be maybe fine-tuned
[1122.76 --> 1125.24]  later on for downstream tasks.
[1125.68 --> 1131.02]  So, this has been, like, part of the driver for a lot of the innovations in NLP recently,
[1131.20 --> 1133.64]  but also in other fields like image processing.
[1134.20 --> 1141.12]  A lot of sort of large image processing neural networks have most of the complexity of the
[1141.12 --> 1146.74]  network is involved in this sort of feature extraction phase, which kind of takes an image
[1146.74 --> 1149.26]  and converts it to a vector representation.
[1149.26 --> 1155.18]  What's interesting, I think, about this work is that for the most part, all of these techniques
[1155.18 --> 1160.12]  that people have been doing, by and large, are a single modality.
[1160.12 --> 1165.60]  So, they take, you know, text input and convert it into some vector representation, right?
[1165.64 --> 1172.32]  Or they take image input and convert it into some vector representation or speech input into
[1172.32 --> 1175.18]  some vector representation or a spectrogram or something.
[1175.18 --> 1181.40]  And I think this is really interesting because they're taking the perspective of, well, whatever
[1181.40 --> 1188.44]  data we put in, and I guess in this case, whatever is either image, speech, or text.
[1188.70 --> 1188.78]  Okay.
[1188.88 --> 1196.14]  But whatever data we put in, we're going to create a model that is trained to represent that
[1196.14 --> 1198.14]  in a learned vector space.
[1198.14 --> 1200.92]  So, that's sort of hints the name data2vec.
[1200.92 --> 1207.74]  So, moving from thinking about a sort of single modality of data input to like a model that
[1207.74 --> 1216.02]  can take like one or two or three or a combination of kind of data inputs and represent that in a
[1216.02 --> 1216.82]  vector space.
[1217.20 --> 1220.62]  So, that's why I kind of thought this was pretty interesting.
[1220.80 --> 1221.62]  It does sound interesting.
[1221.62 --> 1228.98]  Did you get any sense of why the modality was no longer kind of a critical part of the pattern?
[1229.10 --> 1233.50]  I mean, or any sense of how they've overcome that approach in this?
[1233.84 --> 1233.96]  Yeah.
[1234.16 --> 1239.84]  So, I mean, they talk a little bit about, you know, and there's a paper we'll link in our
[1239.84 --> 1242.20]  show notes if people want the specifics.
[1242.20 --> 1249.94]  But essentially, they have a sort of non-learned representation of each of these types of data
[1249.94 --> 1254.60]  that they can input to a similar series of layers.
[1255.50 --> 1262.38]  And what they do is they sort of use this trick of masking, which is used kind of both
[1262.38 --> 1271.20]  in image processing, speech processing, and text processing as a sort of way to, in a self-supervised
[1271.20 --> 1273.64]  way, learn the vector representation.
[1273.86 --> 1278.58]  So, if you think about an image, you can mask off a piece of that image and try to fill
[1278.58 --> 1279.56]  in the missing pieces.
[1279.86 --> 1284.98]  Or if you have speech, you can mask off a bit of that speech and try to fill in the missing
[1284.98 --> 1285.40]  pieces.
[1285.50 --> 1289.52]  Or text, you can mask off certain words and try to fill them in.
[1289.60 --> 1295.74]  And that kind of principle of that masking is applicable across these different modalities
[1295.74 --> 1303.44]  in a way that I guess is similar enough to where they can use a single set of models to,
[1303.66 --> 1306.08]  in a self-supervised way, learn the representations.
[1306.08 --> 1312.42]  And they use this also student-teacher method that sometimes we've seen in recent years as
[1312.42 --> 1312.64]  well.
[1313.12 --> 1313.40]  Very cool.
[1313.62 --> 1316.60]  I noticed that that was done by Facebook's AI team.
[1317.02 --> 1317.18]  Yeah.
[1317.28 --> 1318.94]  Or meta or whatever it is.
[1318.94 --> 1319.12]  Yeah.
[1319.18 --> 1320.14]  Meta now, I guess.
[1320.44 --> 1321.62]  We're in the metaverse now.
[1321.62 --> 1325.24]  Do they have any mention of use cases for it or was that not addressed?
[1325.34 --> 1327.56]  Was it just still too much in the research area?
[1327.96 --> 1328.18]  Yeah.
[1328.32 --> 1336.42]  I think they provide some motivation in that there is an overhead and big differences in
[1336.42 --> 1342.84]  the way that algorithms are put together for images and speech and text and other modalities.
[1343.10 --> 1349.54]  And so, bringing them together provides both that flexibility and more simplicity.
[1349.54 --> 1357.88]  But I think there's also this element of something about working with multiple modalities of data,
[1358.48 --> 1364.82]  at least in certain cases, can provide you a boost in performance across all modalities.
[1365.10 --> 1372.52]  They show certain benchmarks where they beat other models or other image-to-vec or word-to-vec
[1372.52 --> 1375.94]  models in the different modalities.
[1376.30 --> 1384.74]  So, like on ImageNet and at least similar or better performance than models like Roberta,
[1385.32 --> 1387.00]  which is a single modality.
[1387.16 --> 1393.06]  So, you get similar performance, similar or better performance in a single modality,
[1393.24 --> 1398.66]  but it's flexible to use it across different modalities, which allows you to have a sort
[1398.66 --> 1403.00]  of one model that operates in multiple spaces, which is kind of cool.
[1403.40 --> 1404.02]  That is pretty cool.
[1404.22 --> 1409.40]  One of the articles that I came across, I've been, actually several articles are in the
[1409.40 --> 1414.50]  general area, is I've been very interested lately in AI and its interface with robotics.
[1414.76 --> 1419.76]  And once upon a time at a previous employer, I was kind of doing that exclusively for a while.
[1419.76 --> 1425.80]  And so, I ran across this article, it was in Science Daily, called Robot Performs First
[1425.80 --> 1428.28]  Laparoscopic Surgery Without Human Help.
[1428.38 --> 1435.08]  And it's actually referencing a paper by John Hopkins University that was very recent, January 26th,
[1435.10 --> 1440.56]  which had a similarly named, a robot has performed laparoscopic, I'm probably butchering the name,
[1440.82 --> 1446.54]  surgery on soft tissue of a pig without the guiding hand of a human, a significant step in
[1446.54 --> 1449.08]  robotics toward fully automated surgery on humans.
[1449.08 --> 1453.56]  That's pretty cool because this is when you think of what's called keyhole surgery,
[1453.76 --> 1459.84]  where they make a very small incision and it goes in, the laparoscopic surgery is on the gut.
[1460.16 --> 1466.32]  So, when you think of all of the various ailments that humans and for that matter animals get,
[1466.76 --> 1472.64]  all mammals in their gut, anything from cancer to various digestive problems,
[1473.10 --> 1477.12]  and we've come far enough in such a short amount of time
[1477.12 --> 1481.54]  so that they can put the robot to work and it makes the cut, it goes in,
[1481.60 --> 1487.34]  it does the work it has to do, mends, sews back together, things like that, and pulls out.
[1487.34 --> 1497.18]  And we've been talking in recent years about human surgeons doing these surgeries with the assistance of robots and the assistance of AI,
[1497.74 --> 1504.24]  but now we're looking at this, making this next jump where you're taking that human surgeon out of the loop,
[1504.64 --> 1510.96]  at least in this test case, and the AI combined with the robot are successfully doing it on their own.
[1511.32 --> 1512.12]  What do you think of that?
[1512.12 --> 1518.48]  It's interesting and it sort of gives, I think, people mixed feelings, probably.
[1518.86 --> 1521.04]  Probably. We did mention AI ethics.
[1521.42 --> 1524.92]  Yeah, I think you're right in that the sort of next question comes,
[1525.30 --> 1529.80]  well, is it always better to have a human with the machine?
[1530.06 --> 1530.30]  Yes.
[1530.38 --> 1537.22]  That's one interesting question I would have is sort of the automated robotic procedure.
[1537.22 --> 1544.28]  It would not surprise me if that was sort of more or had a higher performance than a human alone.
[1544.28 --> 1551.18]  What would be interesting to know, and maybe they do mention this in the paper that I don't see at a first reading,
[1551.30 --> 1560.40]  but if the human plus machine sort of combination, if there's a way for that to outperform either the robot or the human itself,
[1560.70 --> 1561.68]  that's an interesting question.
[1561.68 --> 1564.46]  I think that's an evolving question over time.
[1564.70 --> 1572.24]  I know in the industry I'm in doing kind of defense stuff, the term for that is mum tea, which is manned, unmanned teaming.
[1572.36 --> 1572.60]  Right.
[1572.68 --> 1579.94]  Where you have an automation, which may be an AI, may include robotics, may not, working with a human to achieve some sort of task.
[1579.94 --> 1587.34]  And the value proposition in a broad sense on that is exactly what you said, that by combining the two you're doing better.
[1587.74 --> 1595.40]  I think we're entering a period now where that is called into question and may change for various tasks over time
[1595.40 --> 1599.80]  as we see the fully automated version able to outperform.
[1600.02 --> 1604.50]  And this goes back to another example that I have talked about in earlier episodes.
[1604.50 --> 1609.68]  There was a DARPA program been, I don't know, a year and a half, probably maybe two years.
[1609.86 --> 1613.60]  I think it was before COVID fully set in called Alpha Dogfight.
[1613.72 --> 1622.76]  And in that they had, it was publicly broadcast and they on YouTube and they had a fully automated F-16 in a simulator.
[1622.94 --> 1624.24]  It's using an F-16 simulator.
[1624.42 --> 1629.94]  The fully automated pilots completely outperformed the human ones, completely outperformed.
[1629.94 --> 1635.60]  And now that's in a simulation world and there's all sorts of caveats you can apply.
[1635.94 --> 1640.64]  But it surprised everybody just how well the AI did in those contexts.
[1641.02 --> 1645.68]  So here we are in a different area in medicine and now we're seeing the first ones coming about
[1645.68 --> 1649.90]  and they will start to evaluate performance over many of these tasks.
[1650.34 --> 1658.56]  It's a really interesting time that we live in as we see the relationship of whether the human's in the loop or not in some capacity is evaluated.
[1658.56 --> 1670.96]  Yeah. And I mean, this is obvious, I think, to practitioners, but it's something that I really notice in talking with like just friends or people that aren't practitioners.
[1670.96 --> 1672.66]  It's not obvious to them.
[1672.66 --> 1686.66]  And that's that like when you say the sort of AI quote is doing the surgery, there's this sort of perception that like the AI could like go off and do something.
[1686.76 --> 1691.22]  So it could decide to do a different surgery than you told it to do.
[1691.30 --> 1692.16]  That's a great point.
[1692.16 --> 1702.74]  The sort of idea of control and like the sort of distribution of inputs and outputs is not something that's obvious to like general people out there.
[1702.86 --> 1707.00]  And I don't know how to better communicate that as practitioners.
[1707.00 --> 1714.96]  But like the things that we're doing are for the most part, very task specific, very narrow, very narrow.
[1714.96 --> 1720.48]  So like this process is not like a robot that can do all surgeries.
[1720.72 --> 1720.84]  Yeah.
[1721.02 --> 1726.96]  I'm guessing that it's a single sort of like operation and it's very specialized.
[1726.96 --> 1736.76]  It's not going to like you thought it was going to like, you know, remove a tumor and instead it like took out your appendix or like something.
[1737.24 --> 1746.48]  Since we're talking kind of along the AI ethical thing, I think that raises an interesting point, which I don't think non-practitioners generally understand.
[1746.48 --> 1749.44]  And it's extending what you're saying right there.
[1749.52 --> 1760.70]  And that is the fact that because these models address very narrow tasking, it's not intelligence, I think, the way most of us define it.
[1760.94 --> 1768.18]  It's mathematically, you know, learning a set of patterns and going through that's a little bit loose in my language, I know.
[1768.46 --> 1770.32]  But being able to go and do that.
[1770.32 --> 1776.58]  So I think when people focus on the intelligent side, they are missing the boat on that.
[1776.74 --> 1779.28]  I think it's important that they start to understand.
[1779.40 --> 1797.10]  I think what's a lot more likely to happen is that with current technology, the way it is more or less right now in 2022, you could have thousands, tens of thousands, hundreds of thousands of tasks that are trained in a very narrow task oriented model.
[1797.24 --> 1798.94]  And all of those tasks are out there.
[1798.94 --> 1802.06]  So could you have fully automated brain surgery?
[1802.36 --> 1804.44]  Maybe at some point here in the future.
[1804.86 --> 1806.28]  Fully automated heart surgery?
[1806.44 --> 1807.08]  Maybe so.
[1807.50 --> 1809.50]  I mean, we're just talking about surgeries right there.
[1809.96 --> 1824.26]  But that's what I think about a lot more in terms of the AI ethical concerns going into the future is all of the models and handing our life over to all the models rather than one super knowledgeable model that rules them all, which is a fiction.
[1824.26 --> 1827.84]  It's interesting, Chris, on that last point you made.
[1827.84 --> 1836.84]  You kind of made this comment about what we perceive as intelligence or what the sort of general population perceives as intelligence.
[1837.18 --> 1842.34]  I was reading a book by Hamming called Learning to Learn.
[1842.58 --> 1844.96]  I think it's the art of doing science and engineering.
[1845.46 --> 1850.18]  Really interesting and in certain cases, humorous book.
[1850.18 --> 1856.78]  But yeah, he talks a little bit about I think he has a few chapters on AI and limits of AI.
[1857.10 --> 1864.82]  He brings up the point that sort of we keep kind of moving the goal marker of intelligence.
[1864.82 --> 1878.48]  So like, you know, 15 years ago or something, we said, well, if a robot could perform a surgery, would we consider that artificial intelligence or would we consider that intelligence?
[1879.18 --> 1884.68]  Likely you'd get a different distribution of answers than after the event has happened.
[1884.68 --> 1893.08]  Like after the event has happened, it's very easy for us to look at that event and say, well, wasn't really intelligence because X, Y, Z.
[1893.30 --> 1896.88]  Right. So then we move the goal marker, you know, however far.
[1897.04 --> 1904.62]  And I'm not saying it is or isn't sort of intelligence because that I mean, you can define that in so many different ways.
[1904.94 --> 1906.48]  That's where I was going to go next.
[1906.60 --> 1906.98]  Keep going.
[1906.98 --> 1923.46]  Yeah, I think what's weird is like somehow there's the mix of using the terminology artificial intelligence to describe what's going on here, which triggers the wrong thing in people's mind in terms of how they define intelligence.
[1923.46 --> 1933.20]  And so, yeah, I think it's just a lot of confusion, which probably feeds into that sort of narrow versus wide perception that you brought up earlier.
[1933.36 --> 1935.02]  It's very imprecise, the phrase.
[1935.02 --> 1946.16]  So except for the name of our podcast, which is perfect, the term artificial intelligence is otherwise a very, very nebulous and imprecise way of describing it.
[1946.34 --> 1949.16]  And as we see, as you just pointed out, it's changing constantly.
[1949.50 --> 1955.02]  And I think, you know, as practitioners, we're not spending our time thinking AI in this big nebula.
[1955.02 --> 1962.62]  We're looking today at specific deep learning algorithms and approaches to training and implementation.
[1962.62 --> 1964.76]  And it's very narrow.
[1964.76 --> 1974.08]  And I don't think most of us spend much time thinking about it the same way that untrained people in the general population probably perceive it as.
[1974.22 --> 1976.42]  And so it is very practical.
[1976.42 --> 1978.44]  It is very pragmatic what we're doing.
[1978.54 --> 1980.20]  But I think a lot of people miss that.
[1980.20 --> 1990.98]  And we've just demonstrated, you know, going to how to define intelligence that now that the surgery is done, neither one of us, we're both in agreement that that isn't what we think of as intelligence.
[1990.98 --> 1998.94]  And I think that's because people conflate several ideas together, which is consciousness, intelligence, self-awareness.
[1999.44 --> 1999.56]  Yeah.
[2000.34 --> 2001.76]  Robustness, generalization.
[2002.32 --> 2002.64]  Yeah.
[2002.86 --> 2003.00]  Yeah.
[2003.30 --> 2003.82]  Absolutely.
[2003.82 --> 2011.48]  So I think that in this maybe narrow form of intelligence that we're describing, I think we'll see a lot of that in years to come.
[2011.54 --> 2021.58]  But I still think that I'm looking forward to the day when the general population kind of understands it, maybe along the same lines that we do, who address these things on a daily basis.
[2022.10 --> 2022.28]  Yeah.
[2022.54 --> 2031.12]  And I guess on that note, Chris, did you see that now AI coders are as good as the average human coder?
[2031.36 --> 2032.32]  Did you see that article?
[2032.32 --> 2036.74]  I did not see that article, but I am not at all surprised about that.
[2037.16 --> 2047.92]  So DeepMind, well, the article that ran across my feed is DeepMind says its new AI coding engine is as good as an average human programmer.
[2048.68 --> 2057.78]  And so DeepMind, so if you remember, we've talked about OpenAI's codex in the past, right?
[2057.78 --> 2060.38]  Which is this sort of code.
[2060.54 --> 2065.96]  It's like a language model for code and can do sort of like code.
[2066.20 --> 2075.94]  It's like your AI pair programmer is how it's being used within like the GitHub copilot product, which could be integrated into VS Code and such.
[2075.94 --> 2080.02]  Well, DeepMind has this AI system called AlphaCode.
[2080.38 --> 2081.28]  Everything is Alpha.
[2081.38 --> 2082.06]  Have you noticed that?
[2082.26 --> 2083.06]  Yeah, yeah.
[2083.38 --> 2085.30]  I mean, I can't wait for beta code.
[2085.78 --> 2087.80]  That's going to be pretty killer.
[2087.96 --> 2088.18]  Yeah.
[2088.18 --> 2092.98]  But yeah, the quote is sort of it writes computer programs at a competitive level.
[2092.98 --> 2110.36]  And this was done with data from a set of challenges that were curated as competitive coding challenges on a platform in which there is competitive coding that happens.
[2110.62 --> 2120.98]  This code forces competitive coding platform, which one kind of side note, I really do not want to get into competitive coding.
[2120.98 --> 2150.96]  I don't need to.
[2150.98 --> 2152.58]  And because it's competitive, right?
[2152.64 --> 2156.16]  It's like a anyway, that's like a total rabbit trail.
[2156.94 --> 2167.92]  But despite that, there's this sort of set of tasks and they ran AlphaCode through its paces on these competitive coding tasks and determined that.
[2167.92 --> 2174.10]  I don't think they're saying that it is vastly better than the human coders.
[2174.22 --> 2176.52]  But I think they're saying like it's as good.
[2177.02 --> 2178.80]  Like that's kind of their conclusion.
[2179.06 --> 2181.90]  As good, in some cases, better.
[2182.30 --> 2187.08]  And you can go and look at the example challenges that they have.
[2187.08 --> 2192.26]  And they're definitely not, you know, I would not consider them easy challenges.
[2193.04 --> 2196.34]  No, I was looking at those on this article that you passed me.
[2196.46 --> 2197.34]  They are not.
[2197.68 --> 2203.84]  You know, it really, as we record this in early 2022, you raise that.
[2203.84 --> 2208.04]  It is good, but it probably will be going forward and surpass.
[2208.04 --> 2226.26]  And it really draws out the fact that if you can take a task and break it down into kind of a repetitive pattern, there's a pretty good chance that there is a narrow, deep learning algorithm which can learn it eventually better than a human expert can.
[2226.26 --> 2229.60]  And it's an interesting world that we're moving into, Daniel Whitenack.
[2229.74 --> 2230.88]  Yeah, yeah, for sure.
[2231.32 --> 2236.34]  And it's sort of that line I view it as like people have known this for a long time, right?
[2236.34 --> 2240.28]  That there are repetitive coding tasks, which is why code generation.
[2240.28 --> 2240.64]  Of course.
[2241.38 --> 2248.20]  Which is kind of that rule-based approach to generating code for XYZ things.
[2248.20 --> 2255.40]  So like you have, you know, generating a client for based on some protobuf or something like that.
[2255.40 --> 2264.90]  Or you're generating like some backend code for your web application based on some config that you've created or, you know, something like that.
[2265.26 --> 2270.16]  All of these problems, they're like very repeatable and can follow patterns.
[2270.16 --> 2286.04]  And this is sort of like there's probably, I guess, in my view, if you look at all code that's written on like the one side, one third of it is probably almost repetitive enough to just be like rule-based generation.
[2286.40 --> 2286.48]  Yeah.
[2286.48 --> 2293.60]  There's like a middle third of it, which is kind of like it's not quite like rule-based generation.
[2293.60 --> 2295.02]  Like it goes beyond that.
[2295.16 --> 2297.72]  There's levels of decision-making and such.
[2297.82 --> 2301.22]  But maybe it could be attacked by this sort of algorithm.
[2301.82 --> 2303.70]  And then there's probably still a third.
[2303.92 --> 2313.06]  It's like very hard code that is solving very unique problems that aren't represented well in other spheres or, you know, something like that.
[2313.06 --> 2314.20]  A fraction of all code.
[2314.32 --> 2314.46]  Yeah.
[2314.52 --> 2316.94]  A tiny fraction in that last category.
[2317.38 --> 2321.36]  You think I am over generous in my thirds.
[2321.78 --> 2322.22]  I do.
[2322.22 --> 2330.16]  I think that you're way over generous because, you know, aside from this AI that we love, you and I both came from programming before that.
[2330.24 --> 2333.08]  And we were doing a lot of programming in various languages.
[2333.66 --> 2338.86]  And most of the programming across many projects, even across time.
[2339.34 --> 2339.76]  Copy-paste?
[2339.76 --> 2340.82]  It really is.
[2340.88 --> 2345.00]  It's copy-paste or it's basically doing the same thing in a different language that you did before.
[2345.38 --> 2347.98]  Maybe a little bit of a different architectural paradigm.
[2348.48 --> 2357.50]  But I'm going to postulate that 95 to 99% of all the code out there has a lot of commonality across projects.
[2357.50 --> 2360.08]  And there's a little fraction that's multiple.
[2360.08 --> 2371.94]  And if this is something that we think of, if you go back just a few years before we were doing this podcast and we programmers were thinking, wow, I'm out there making amazing things and all that.
[2372.10 --> 2373.94]  This is the challenge of automation.
[2374.24 --> 2376.56]  This is, I think, the question of our time.
[2376.56 --> 2379.66]  It's certainly one of the top questions, if not the only one.
[2379.82 --> 2382.60]  It's one of several that we need to contend with.
[2382.74 --> 2392.68]  It's that automation doesn't have to be all-knowing, all-intelligent, super, the thing that people think of in the Hollywood movies to be able to do this.
[2393.14 --> 2395.62]  And now we come to the great battle of our time.
[2395.76 --> 2396.16]  Indeed.
[2396.58 --> 2396.94]  Indeed.
[2397.16 --> 2399.82]  This is the AI version of Lord of the Rings right here.
[2399.98 --> 2400.86]  You're in it, folks.
[2400.86 --> 2401.18]  Yeah.
[2401.32 --> 2412.02]  As soon as we can generate a next reasonable script for the Lord of the Rings, then we can probably do a pretty good job right now, but still, I think, lacking.
[2412.84 --> 2413.62]  But, yeah.
[2413.90 --> 2414.44]  I agree.
[2414.64 --> 2419.54]  Narrow AI still can't quite match J.R.R. or Tolkien, if I'm saying the name right.
[2419.58 --> 2419.72]  Yeah.
[2419.90 --> 2420.14]  Yeah.
[2420.24 --> 2421.32]  That's a tall order.
[2421.44 --> 2421.82]  I agree.
[2422.06 --> 2422.34]  Okay.
[2422.76 --> 2425.50]  So maybe that's my definition of intelligence there.
[2425.66 --> 2426.54]  I'll say that.
[2426.74 --> 2426.90]  Yeah.
[2427.14 --> 2427.84]  No, I'm just kidding.
[2427.84 --> 2436.04]  So as we wrap up in these fully connected episodes, we do always like to share a couple of learning resources.
[2436.80 --> 2441.30]  Chris, I noted a couple over the past week, so I'll share those.
[2441.82 --> 2452.82]  One that I found, which I'm not totally sure if I've shared before, but I thought it was really cool, is there's this seeingtheory.brown.edu site,
[2452.82 --> 2458.14]  which is a visual introduction to probability and statistics.
[2458.96 --> 2462.58]  And it probably, like, some people don't learn this way, right?
[2462.60 --> 2463.82]  Some people don't learn visually.
[2464.06 --> 2469.42]  But I love to have sort of a visual component that I can have in mind for a concept.
[2469.42 --> 2486.96]  And especially for, I think, statistics and probability, a lot of people view that, like, they have trouble with the intuition around certain concepts within probability and statistics, maybe more so than, like, calculus or algebra or linear algebra sorts of things.
[2486.96 --> 2496.24]  And so this goes through and actually kind of walks you through various ideas, like expectation values and other things.
[2496.24 --> 2499.14]  And you can, like, see a visualization paired with that.
[2499.24 --> 2505.96]  And it's a very cool sort of way of approaching probability and statistics and an intro to certain ideas.
[2506.74 --> 2508.76]  So I would definitely recommend going through that.
[2509.08 --> 2510.22]  It's a very nice website.
[2510.40 --> 2512.02]  It's elegantly done, pretty.
[2512.30 --> 2513.64]  And I like the visuals in it.
[2513.72 --> 2514.68]  It's easy on the eyes.
[2515.06 --> 2516.24]  Yeah, yeah, for sure.
[2516.24 --> 2532.04]  The other one that I'll just mention people might want to take a look at is there's this book, which is posted online, which I came across on Twitter, Patterns, Predictions and Actions, a Story About Machine Learning.
[2532.50 --> 2534.44]  And I thought that was intriguing.
[2534.68 --> 2535.68]  So I clicked on it.
[2535.84 --> 2539.90]  I think it's intriguing that they sort of frame it as a story.
[2539.90 --> 2547.48]  But if you look at kind of the things that are covered, they might cover them in a sort of different narrative approach.
[2548.16 --> 2551.44]  But and maybe from from their own perspective.
[2551.44 --> 2565.38]  But it is a very seemingly comprehensive introduction to various topics going through supervised learning, representations, optimization, deep learning, causality and causal inference.
[2565.98 --> 2568.84]  Really a lot of relevant topics.
[2568.84 --> 2576.04]  And they kind of start, I think, from the idea of fundamentals of prediction and the classification problem.
[2576.04 --> 2577.48]  And that's kind of where they're starting.
[2577.60 --> 2585.72]  And they lead from there in their story to these other areas that people are very interested in now.
[2585.72 --> 2593.80]  So it's a cool approach from Moritz Hart and Benjamin Richt, a story about machine learning patterns, predictions and actions.
[2594.20 --> 2594.86]  I'll check it out.
[2595.08 --> 2599.80]  We'll share those links along with the other links that we talked about in our show notes.
[2600.18 --> 2608.24]  So definitely people check those out and let us know your thoughts on these things and the various rabbit holes that we went through.
[2608.36 --> 2613.02]  As a reminder, you can connect with us directly on our Slack channel or LinkedIn.
[2613.02 --> 2620.14]  If you go to changelog.com slash community, you can join our Slack channel there and connect with us on Twitter or LinkedIn.
[2620.54 --> 2622.82]  We'd love to hear about what you're interested in.
[2623.22 --> 2625.48]  But yeah, good to get to be on with you again, Chris.
[2625.84 --> 2627.00]  Another good conversation.
[2627.18 --> 2627.94]  Thank you so much.
[2628.08 --> 2629.10]  I'll talk to you soon.
[2629.22 --> 2629.42]  Bye.
[2629.62 --> 2629.80]  Bye.
[2632.92 --> 2633.84]  All right.
[2634.14 --> 2635.90]  That's Practical AI for this week.
[2636.06 --> 2636.84]  Thanks for listening.
[2637.04 --> 2641.76]  If this is your first time with us, subscribe now at practicalai.fm.
[2641.76 --> 2646.04]  or simply search for Practical AI in your favorite podcast app, we're in there.
[2646.34 --> 2650.44]  And if you're a longtime listener, do us a solid by recommending the show to a friend.
[2650.94 --> 2654.84]  Word of mouth is still the number one way people find new podcasts they love.
[2655.20 --> 2657.34]  Special thanks to our partners for supporting our work.
[2657.66 --> 2659.72]  Fastly, LaunchDarkly, and Linode.
[2659.92 --> 2660.68]  We appreciate it.
[2660.68 --> 2664.90]  And to the mysterious Breakmaster Cylinder for cranking out new beats for us all the time.
[2665.24 --> 2666.02]  That's all for now.
[2666.46 --> 2667.62]  We'll talk to you again next week.
[2667.62 --> 2667.68]  Bye.
[2667.68 --> 2667.74]  Bye.
[2667.74 --> 2669.74]  Bye.
[2669.74 --> 2670.74]  Bye.
[2670.74 --> 2671.74]  Bye.
[2671.76 --> 2701.74]  Bye.
