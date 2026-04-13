[0.00 --> 8.30]  Welcome to Practical AI.
[8.72 --> 16.30]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing
[16.30 --> 18.28]  the world, this is the show for you.
[18.28 --> 24.30]  We just dropped Dance Party, our third full-length album on Changelog Beats.
[24.30 --> 29.70]  Buy it on Bandcamp and iTunes, or stream it on Spotify, Apple Music, and the rest.
[30.00 --> 30.74]  Link in the show notes.
[31.20 --> 33.38]  Thank you to our partners at Fly.io.
[33.86 --> 35.56]  Launch your app close to your users.
[36.06 --> 38.38]  Find out how at Fly.io.
[42.94 --> 46.02]  Welcome to another episode of Practical AI.
[46.38 --> 47.96]  This is Daniel Whitenack.
[48.08 --> 51.46]  I am the CEO and founder at Prediction Guard.
[51.46 --> 57.16]  And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed
[57.16 --> 57.44]  Martin.
[57.66 --> 58.32]  How are you doing, Chris?
[58.56 --> 59.74]  Doing great today.
[59.84 --> 62.38]  It was nice seeing you a few days ago in person.
[62.72 --> 63.52]  In the flesh.
[63.74 --> 64.50]  In the flesh.
[64.66 --> 65.80]  Yeah, that was great.
[66.00 --> 67.86]  I think you posted a picture on LinkedIn.
[68.22 --> 72.98]  So if anybody doesn't know what we look like and has some crazy reason to want to know,
[73.32 --> 76.28]  there's a smiling mug of us on Daniel's profile.
[76.76 --> 77.76]  Yes, yes.
[77.76 --> 86.14]  And the reason we met is I was on a client visit on site and we were prototyping out some
[86.14 --> 92.00]  stuff like chat over your docs and natural language to SQL stuff and all sorts of things
[92.00 --> 93.04]  with Prediction Guard.
[93.58 --> 97.14]  And one of the models that we were using was from Noose Research.
[97.48 --> 104.42]  And that works out great because we have Curran Mahotra here, who is from Noose Research,
[104.60 --> 106.64]  co-founder and researcher there.
[106.64 --> 107.44]  So welcome.
[107.80 --> 108.58]  Glad to have you, Curran.
[108.96 --> 109.52]  Hey, all.
[109.64 --> 110.62]  Thanks for having me.
[110.72 --> 112.94]  I'm extremely excited to chat with you guys.
[113.44 --> 113.72]  Yeah.
[113.90 --> 116.20]  Like I said, I'm a huge...
[116.20 --> 121.22]  Well, this is our first time meeting, but I feel like we're already friends because I've
[121.22 --> 127.40]  had so much of my own benefit and interaction in working with models from Noose Research.
[127.62 --> 132.90]  A lot of amazing models that you've posted on Hugging Face and research that you're doing.
[132.90 --> 139.36]  I'm wondering if you could just give us a little bit of a background about Noose specifically
[139.36 --> 147.52]  and kind of how you came together as researchers and started, to me, from the sidelines.
[147.62 --> 151.52]  It seemed like, oh, all of a sudden there's these amazing models on Hugging Face and I don't
[151.52 --> 154.52]  know who these people are, these Noose Research people, but they're amazing.
[154.98 --> 157.20]  So give us a little bit of the backstory there.
[157.20 --> 157.92]  Absolutely.
[158.36 --> 158.60]  Yeah.
[159.18 --> 164.24]  So just as a general overview, we are one part open source research organization.
[164.48 --> 165.84]  We put these models out for free.
[166.32 --> 170.62]  We put a lot of research out for free, some data sets so people can build on top of these
[170.62 --> 171.26]  open models.
[171.82 --> 175.80]  On the other hand, we're very recently a company as well, a C-Corp.
[175.80 --> 182.86]  So we've been working pretty hard after getting some seed funding on building together some
[182.86 --> 188.18]  exciting stuff I won't go too into during the overview point, but we're continuing to
[188.18 --> 191.90]  do our open source research and development and release of models indefinitely.
[192.34 --> 198.72]  The way we started is very interesting and it would be pretty out of nowhere to the outside
[198.72 --> 199.20]  for sure.
[199.36 --> 201.16]  It was extremely fast for us.
[201.16 --> 206.46]  We are a collective of people who have been playing around in the open source language
[206.46 --> 212.48]  model space for a while, ranging from like GPT-2 release to Llama release to like the
[212.48 --> 213.72]  first Transformers paper.
[213.90 --> 218.44]  We've got people from various eras of Gen AI of when they came in.
[218.86 --> 220.38]  And for myself, it was GPT-2.
[220.66 --> 226.76]  I stumbled upon a CoLab notebook and started fine tuning, made some Edgar Allan Poe and Lovecraft
[226.76 --> 227.10]  tunes.
[228.00 --> 229.12]  I've done the same.
[229.30 --> 229.80]  That's awesome.
[229.80 --> 236.22]  And we just got pulled into this world of look at these next token predictors that are
[236.22 --> 239.60]  just managing to smatter together the most wonderful and amazing stories.
[239.96 --> 245.78]  That slowly turned into a deeper and deeper dive of, well, how can I use this for learning
[245.78 --> 246.32]  information?
[246.48 --> 249.66]  How can I learn to use this for production and automation, right?
[249.68 --> 250.84]  It's evolved over time.
[251.30 --> 256.28]  For us, we started off just working with different open source collectives, actually.
[256.28 --> 262.84]  Once OpenAI kind of released GPT-3 and had closed sourced it, we were used to open source
[262.84 --> 263.42]  GPT-2.
[263.60 --> 264.94]  We were like, oh man, what are we going to do?
[265.08 --> 269.08]  How are we going to continue to play with the level of customization and interactivity
[269.08 --> 270.98]  that we had with GPT-2?
[271.30 --> 274.20]  Then Eleuther had released GPT-J6B.
[274.20 --> 280.16]  The COBOLT AI community, this community of people who tune models and inference models
[280.16 --> 285.42]  started to pop up, I think, around 2020, 2021, in the face of this.
[286.12 --> 290.68]  So a lot of us started to have places to centralize and play with these models.
[290.88 --> 296.02]  We got to contribute and learn how to become better open source AI developers, etc.
[296.02 --> 303.86]  Eventually, there was a need for more concrete organizations to do this kind of focused work
[303.86 --> 305.72]  on the creation of these models.
[306.16 --> 312.88]  We were stuck with okay architectures for a while, like Pythia, but thanks to Meta, we
[312.88 --> 313.92]  wouldn't be here without Meta.
[314.00 --> 315.76]  I'll say that, first and foremost.
[316.16 --> 317.00]  The great Llama.
[317.30 --> 317.56]  Yeah.
[318.16 --> 323.04]  Prior to Llama, everyone's like, oh, Facebook evil, my data, etc.
[323.04 --> 328.84]  And here we are, they are kind of like the shepherds of this new era of the open source
[328.84 --> 329.54]  AI movement.
[329.94 --> 336.06]  So when Llama came out, there was a paper that came out called Alpaca by Stanford Lab, right?
[336.14 --> 343.56]  And this was about distilling data from bigger models like GPT-3, ChatGPT, GPT-4, and being
[343.56 --> 349.42]  able to train smaller models on that distilled synthetic data, something they called instruction
[349.42 --> 349.92]  data.
[349.92 --> 355.60]  So that Alpaca format really opened up the playing field for everybody to start making
[355.60 --> 360.20]  these instruct style models, these actual for prod use style models.
[360.82 --> 367.74]  So there was an idea I had in my head of, well, the Alpaca guys are using only GPT-3.5 outputs.
[368.10 --> 370.30]  What if I only generated GPT-4 outputs?
[370.38 --> 374.36]  It'll be a little expensive, but you'll probably get a better model out of it than Alpaca.
[374.36 --> 380.36]  At the same time that I was looking at this, there was a guy on Twitter named Technium who
[380.36 --> 385.18]  had just started putting together his own synthetic data set based off Alpaca and the
[385.18 --> 386.92]  GPT-4 only as well.
[387.34 --> 391.60]  So I was working with a group at the time called Open Assistant under Lion.
[391.96 --> 393.42]  They're a really big nonprofit.
[394.12 --> 397.02]  And while I was working on that, we had some GPUs.
[397.12 --> 401.10]  They were cool with us using towards the development of new models.
[401.10 --> 404.48]  So I reached out to Technium and I said, hey, I have a little bit of compute.
[404.74 --> 406.96]  You have GPT-4 data in the same format.
[407.30 --> 409.18]  I have GPT-4 data in the same format.
[409.32 --> 410.30]  Let's train a model.
[410.66 --> 414.30]  So we trained a model called GPT-4 x Vicuna.
[414.84 --> 417.48]  This model was on the Vicuna fine-tune.
[417.60 --> 419.22]  We fine-tuned to fine-tune basically.
[419.62 --> 424.42]  The Vicuna model was an Alpaca style fine-tune and we tried our data set on top of it.
[424.70 --> 425.44]  It was good.
[425.58 --> 426.18]  It was okay.
[426.18 --> 430.06]  But then we thought, you know, we'll probably get a better result if we just train on the
[430.06 --> 431.72]  base Llama model.
[432.44 --> 435.88]  And the resulting model was the very first Hermes model.
[437.06 --> 437.40]  Gotcha.
[437.84 --> 438.28]  The OG.
[438.68 --> 439.28]  The OG.
[439.62 --> 446.78]  And that's kind of how it started to come together was we both had a data thesis on use GPT-4
[446.78 --> 448.08]  only and follow Alpaca.
[448.48 --> 450.78]  And we trained on Llama and we got Hermes.
[451.14 --> 453.24]  And we didn't know what benchmarks were.
[453.24 --> 456.22]  We didn't know anything about any of this stuff.
[456.42 --> 459.84]  We just made a model and it got a ton of attention.
[459.98 --> 462.18]  We put it out under this name, Noose Research.
[462.86 --> 466.22]  Noose comes from the Greek word for intellect.
[466.50 --> 468.46]  We thought it would be a good name for an AI company.
[469.64 --> 474.62]  But it was just a place for, you know, fun projects and fine-tunes and stuff.
[474.70 --> 476.66]  It was just a name we were using for our collaboration.
[477.32 --> 480.62]  And people started swarming and asking, you know, what's Noose Research?
[480.62 --> 485.66]  Like, what's this sudden, like, mystical, like, open source organization that, like,
[485.72 --> 487.30]  put out this, like, best model?
[487.54 --> 488.82]  And we're like, best model?
[488.94 --> 490.80]  Like, we just, you know, we just tried something.
[491.56 --> 493.08]  It was really organic.
[493.50 --> 496.54]  And it got to the point that people started telling us, you know, you must have trained
[496.54 --> 497.14]  on the benchmarks.
[497.14 --> 498.54]  Like, these are doing too well.
[498.66 --> 500.40]  And we were like, what's benchmarks?
[500.40 --> 508.06]  We were not really, like, coming from an academic place as much as from, like, an enthusiast that
[508.06 --> 511.16]  became so committed that it became our life, right?
[511.20 --> 512.22]  It became our day-to-day.
[512.70 --> 512.78]  Yeah.
[512.90 --> 516.76]  So from there, people started to ask us, can I join Noose Research?
[517.34 --> 519.46]  Now, there wasn't a Noose Research to join.
[519.88 --> 521.24]  There's just two guys, right?
[521.54 --> 524.96]  What ended up happening was we formed a private Discord server.
[524.96 --> 531.72]  And we thought there's a lot of people who range from somebody who's, like, 16, 17 years
[531.72 --> 536.90]  old, savant on Twitter, hasn't even been to college yet, insane at Transformer stuff,
[537.24 --> 544.66]  to mid-30s, you know, working a really, really good Fang-esque job, and just wants to really
[544.66 --> 545.96]  create and let loose.
[546.30 --> 547.50]  That was another class of volunteer.
[547.82 --> 553.32]  And then you have, you know, older gentleman who has already exited a company or something
[553.32 --> 557.50]  who has just been playing with code for a while and wants to jump in and hang out.
[557.58 --> 559.70]  So we ended up being this really eclectic group, you know.
[559.88 --> 561.16]  We don't know what your name is.
[561.20 --> 562.20]  We don't know what your race is.
[562.24 --> 563.30]  We don't know your gender or anything.
[563.42 --> 566.90]  It's just Discord profile picture, Twitter profile picture, right?
[567.32 --> 573.44]  So we came together, grew to about, like, 40 people, all working together on various different
[573.44 --> 578.76]  projects, like Hermes Tunes, Data Synthesis, the Capybara Series, Context Length Extension,
[578.76 --> 579.36]  et cetera.
[579.36 --> 584.32]  And just from this kind of interaction between Twitter and Discord and bringing people in
[584.32 --> 589.02]  that we thought were cool, we ended up becoming what people would call an open-source research
[589.02 --> 589.34]  org.
[590.52 --> 598.06]  Yeah, you sort of stumbled into creating this amazing research organization, which is ruling
[598.06 --> 599.78]  the world, which is awesome.
[600.76 --> 602.40]  It's what OpenAI might have been.
[602.64 --> 603.46]  Oh, well, yeah.
[604.02 --> 605.24]  That's really sweet.
[605.52 --> 606.50]  Thank you, guys.
[606.96 --> 608.40]  Yeah, and I love it.
[608.40 --> 612.58]  It's so cool to hear that story and that background.
[612.80 --> 617.86]  And I see, like, in my own sort of little snapshots here and there, like, I'm connecting
[617.86 --> 623.38]  that in my mind over the past couple of years as I've seen you all post different models and
[623.38 --> 624.12]  that sort of thing.
[624.48 --> 629.02]  This is something, you know, we've definitely touched on on the show before, but some of our
[629.02 --> 634.94]  listeners might not kind of fully grasp when you say this sort of, like, synthetic data
[634.94 --> 639.12]  sets that you are focused on in this Alpaca format.
[639.48 --> 644.28]  Could you kind of explain a little bit, like, we've talked a lot about fine-tuning and, you
[644.28 --> 647.28]  know, preference tuning and RLHF and different things.
[647.42 --> 651.90]  But what does it specifically mean that, like, you would take synthetic data?
[651.90 --> 654.14]  What does that mean in your case?
[654.36 --> 660.22]  And, like, why does that result in something good in fine-tuning an open model?
[660.32 --> 662.20]  People might think, oh, this is synthetic data.
[662.50 --> 665.04]  Why should I expect it to, like, be any good?
[665.42 --> 668.58]  So could you kind of help explain that subject a little bit?
[668.74 --> 669.98]  Yeah, absolutely.
[670.86 --> 675.48]  So, I mean, out of context, synthetic is, like, as meaningless as, like, artificial, right?
[675.48 --> 676.70]  It could, data is data.
[677.22 --> 682.44]  But in this case, it's referring to a particular class of data that's been generated by another
[682.44 --> 687.42]  language model or another AI, another diffusion model, et cetera, that can actually be used
[687.42 --> 688.80]  to further train models.
[689.12 --> 691.18]  Now, you might say, why would you want to do something like that?
[691.22 --> 691.86]  How is it helpful?
[692.46 --> 695.80]  What was important to us is we were all GPU poor, right?
[695.88 --> 699.68]  We were all running on laptops or maybe a 3090, maybe a 4090.
[699.88 --> 702.26]  Like, as individuals, we don't have data centers.
[702.26 --> 707.84]  So training or even tuning, like, a large model in the early days, like 70 billion parameters,
[708.28 --> 710.32]  something like that, was just unfeasible for us.
[710.80 --> 717.08]  And knowing that GPT-3 is, like, something like 175 billion parameters and 3.5 and 4 can
[717.08 --> 723.64]  only go up from there, the question became, how can we make these small 7 billion parameter
[723.64 --> 727.48]  models even compete with these massive, massive ones?
[727.80 --> 731.10]  These ones that I want to run offline, these ones that I might want to run on an edge device,
[731.10 --> 733.50]  on a phone, on a drone, et cetera, right?
[733.54 --> 735.56]  Like, how can I make them even useful?
[736.18 --> 738.12]  So there's two things to talk about here.
[738.26 --> 741.74]  One is synthetic data and the other is distillation, right?
[741.84 --> 748.28]  So synthetic data is just referring to, like, any kind of data that's created by a model in this
[748.28 --> 748.58]  case.
[749.06 --> 752.66]  And the reason that's useful is, in particular, distillation.
[752.66 --> 761.04]  So if I told you to go study comp sci for 10 years, for example, and put in that massive
[761.04 --> 765.66]  time investment and really focus on general programming, and then I told you, you know,
[765.70 --> 769.30]  now it's time for you to learn about AI and transformers and stuff and put you through all
[769.30 --> 770.56]  the math prerequisites, et cetera.
[770.72 --> 776.10]  Like, you're going to come out with, like, a really strong foundation of how to do the
[776.10 --> 776.40]  work.
[776.40 --> 779.42]  But the problem is, you've put in a massive time investment.
[779.42 --> 783.96]  Now, if I take that guy who spent 10 years doing engineering, then another five years
[783.96 --> 789.66]  doing AI, and I ask him, hey, can you teach somebody, like, just really important, like,
[790.02 --> 793.58]  compressed tidbits that'll help them just get up and running to do the work?
[793.82 --> 795.54]  That's data distillation, right?
[795.58 --> 796.90]  That's knowledge distillation.
[797.30 --> 803.06]  So you look at these big models, like a CLOD or a 70B model or GPT-4, and you can see,
[803.14 --> 804.44]  like, they're amazing.
[804.58 --> 805.54]  They're brilliant at everything.
[805.54 --> 810.16]  They have a bunch of high-quality data they're trained on, and they have a bunch of low-quality
[810.16 --> 816.12]  data they're trained on that they can interact with and express in a high-quality form.
[816.68 --> 824.46]  So instead of me having to read a massive 10-pager for why some chemical reaction or some, like,
[824.58 --> 828.20]  tax-based process, like, whatever you want it to be, like, instead of reading a massive
[828.20 --> 832.90]  document on that and then feeding that to a language model, we can just have that really
[832.90 --> 838.38]  smart model that already understands it really well compress that information into an instruction
[838.38 --> 844.98]  or into a conversation into, like, two sentences, three sentences, five sentences, like, half a page.
[845.48 --> 853.52]  And we can just train a much smaller model on that compressed information, and it will learn
[853.52 --> 858.10]  the compressed information, you know, to the degree that a language model learns something,
[858.10 --> 858.94]  you know, not perfectly.
[859.14 --> 864.92]  But because of that, what the Alpaca guys did was they generated a bunch of seed tasks
[864.92 --> 870.54]  from GPT-3.5 on various different domains and topics and created these kind of compressed
[870.54 --> 875.20]  instructions with instruction, an input question from the user, and then an answer.
[875.66 --> 881.20]  So the instruction could be, like, given the following math equation, explain step-by-step why
[881.20 --> 882.02]  this is the answer.
[882.02 --> 888.02]  And then the input is the equation, which is your question, and then the output is the compressed
[888.02 --> 888.48]  answer.
[888.84 --> 894.18]  So all of that we can take as one sample in the data set, and we can make hundreds of thousands
[894.18 --> 899.04]  or millions of samples like that of various different domains and various different tasks.
[899.46 --> 905.26]  So the Alpaca guys did this, less than 100k examples, I believe, and they trained the LAMA models
[905.26 --> 911.16]  on these, and they found massive boosts to performance, that this distilled information,
[911.38 --> 914.96]  like a human, successfully compresses and transfers over.
[915.54 --> 919.40]  So when I saw that, and then independently when Technium saw that, and then independently
[919.40 --> 923.08]  when many others saw that, we were like, this is so intuitive.
[923.36 --> 927.78]  This is exactly how I've learned anything by just going on Discord and Twitter and bothering
[927.78 --> 930.30]  people to give me the compressed bit of how I do something.
[930.76 --> 934.50]  We should try doing this with even higher quality models than 3.5.
[934.50 --> 942.58]  So we created, I can't remember the exact number at the moment, but at least 50,000, maybe 100,000
[942.58 --> 946.90]  examples originally for Hermes 1, like this, just using GPT-4.
[947.56 --> 955.52]  And then we trained on that and ended up getting performance that was extremely, extremely massive
[955.52 --> 959.46]  boost compared to the other models that were not trained using this kind of method.
[959.46 --> 966.26]  So without these giants that have already established themselves in the space, we wouldn't be here.
[966.42 --> 972.54]  Like without OpenAI, without Meta, like we literally wouldn't have the model and the data to do the kind
[972.54 --> 973.94]  of work that we did to make Hermes.
[974.30 --> 980.94]  What it allowed for us is like for local models to finally be like comprehensible and for us to
[980.94 --> 986.18]  finally have like offline capabilities to kind of take the good stuff from something like GPT-4
[986.18 --> 988.56]  or something else and make it uncensored.
[988.94 --> 994.60]  So it still has all this understanding of all these topics, but it doesn't have all that
[994.60 --> 997.70]  RLHF inside it necessarily that safetyizes it.
[997.86 --> 1002.72]  So that when people utilize the model, it has all this intelligence, but it has more freedom
[1002.72 --> 1006.56]  of thought to kind of converse with you on topics that OpenAI may reject.
[1007.06 --> 1007.28]  Gotcha.
[1007.28 --> 1011.24]  One of the things I was curious about as you were going through that was a few episodes
[1011.24 --> 1015.88]  back, Daniel and I were kind of talking about the effect of model licensing, you know, on
[1015.88 --> 1021.08]  the community and the different kind of licensing concerns that were coming out from whether
[1021.08 --> 1023.60]  it be, you know, Meta, OpenAI, you named the organization.
[1023.86 --> 1028.76]  Is that ever a challenge for you since you're kind of using those to get started in terms of
[1028.76 --> 1029.24]  the inputs?
[1029.78 --> 1032.64]  Is that been a concern or do you anticipate it being a concern?
[1032.64 --> 1038.66]  I think that of course, like generally like US international regulation on this stuff is
[1038.66 --> 1039.12]  evolving.
[1039.40 --> 1041.28]  The conversation is evolving very much.
[1041.42 --> 1045.10]  So naturally there's like, you have to keep it top of mind.
[1045.16 --> 1046.58]  You have to think about these kinds of things.
[1046.58 --> 1051.66]  But thankfully, because all of our model releases are like open source and we don't profit from
[1051.66 --> 1051.96]  them.
[1051.96 --> 1057.16]  Like if somebody goes off and creates a product using our model, you know, good for them, but
[1057.16 --> 1063.76]  we don't necessarily take on the liability or that worry of saying, hey, like we're going
[1063.76 --> 1066.86]  to sell you this model that was created with GPT-4 outputs.
[1066.98 --> 1069.88]  We actually actively try to stay away from doing that.
[1070.08 --> 1074.74]  But because the data distillation paradigm is so effective, you know, if a model comes out
[1074.74 --> 1081.36]  that's better than GPT-4 and it's open source and I can use it locally and in their TOS, it
[1081.36 --> 1083.16]  says, you know, you can use this to make a commercial model.
[1083.16 --> 1087.58]  Then we can apply the same techniques that we've been preparing and researching and understanding
[1087.58 --> 1089.92]  from these closed models and use it there.
[1089.92 --> 1097.58]  So right now, like we don't stand to or try to or have any plans to profit from using any
[1097.58 --> 1098.36]  of these outputs.
[1098.72 --> 1103.56]  We're not about that because we want to be careful and respectful of these model creators,
[1103.56 --> 1104.96]  but that and these companies.
[1105.16 --> 1109.28]  But that being said, we're learning all these techniques and developing all these techniques
[1109.28 --> 1113.10]  that will be useful for when that time comes and for when that's available.
[1113.16 --> 1118.08]  Especially with the advent of something like Mistral, if we do distillation from a Mistral
[1118.08 --> 1122.42]  model like Mistral Medium or something like that, that's completely, from my understanding,
[1122.58 --> 1126.44]  you know, barring their TOS saying otherwise, but I believe it doesn't.
[1126.82 --> 1132.74]  It's completely okay in that situation for us to create models like this that can be used
[1132.74 --> 1133.86]  commercially, et cetera.
[1134.54 --> 1140.86]  Regarding the TOS stuff though, like as much as we err on the side of caution, I'd find it
[1140.86 --> 1151.62]  hard to see a company enforce their TOS when these larger models are likely trained on not
[1151.62 --> 1153.66]  all copyright free stuff.
[1153.78 --> 1159.02]  Like I'd find it hard pressed to believe that these closed source companies, their models
[1159.02 --> 1162.76]  are, you know, totally copyright free and totally copyright clean.
[1162.76 --> 1168.70]  So if some other company that was feeling a little more rambunctious than ourselves was
[1168.70 --> 1173.50]  to say, you know, we're going to commercially release on this, I imagine it'd be difficult
[1173.50 --> 1178.68]  for them to be come after without the other group opening their books.
[1178.84 --> 1183.20]  And there's actually a pretty interesting interaction that happened regarding this between Google and
[1183.20 --> 1185.24]  OpenAI, if you guys are familiar.
[1185.24 --> 1189.96]  Yeah, I saw this interesting picture the other day.
[1190.08 --> 1196.30]  It was like the interesting web of AI and it was like how Microsoft, Google, OpenAI,
[1196.94 --> 1200.74]  like it's like on one side, there's the ones and it shows how they're connected to the other ones.
[1200.82 --> 1207.44]  It's like this visualization and like how many of them overlap in these strange ways between like,
[1207.44 --> 1216.32]  whether it's Together or Mistral or Meta, Google, Microsoft, OpenAI is sort of very interesting
[1216.32 --> 1220.90]  web of connections that probably make some of these things rather difficult.
[1221.24 --> 1222.90]  Leave it for the lawyers to sort out.
[1223.10 --> 1223.26]  Yeah.
[1224.00 --> 1226.50]  Yeah, that's the thing is like we can look at an example, right?
[1226.52 --> 1230.00]  Like you hear that phrase like good artists copy, great artists steal, right?
[1230.04 --> 1233.04]  Like so the data distillers, we're copying, right?
[1233.06 --> 1235.34]  Like we're just distilling this information.
[1235.34 --> 1239.86]  Like we're trying to like make our models more like those and we don't really plan to
[1239.86 --> 1240.34]  commercialize.
[1240.38 --> 1241.72]  We're just doing it for free for everyone.
[1241.94 --> 1247.84]  But the great artists are, you know, Google, you know, like you look at Bard and it tells
[1247.84 --> 1249.12]  you, you know, I was made by OpenAI.
[1249.38 --> 1252.46]  Now it's fine for our open source model to say I was made by OpenAI because we're very
[1252.46 --> 1254.64]  transparent about this is trained on GPT outputs.
[1254.90 --> 1258.06]  But when Bard violates the TOS with a paid product.
[1259.36 --> 1259.76]  Bold.
[1260.36 --> 1262.70]  Yeah, that sounds like I was trained by OpenAI, right?
[1262.70 --> 1267.84]  You think that OpenAI would come after this multi-billion dollar company like immediately,
[1268.22 --> 1268.44]  right?
[1268.90 --> 1272.46]  Instead, you see a tweet from, first you see Google deny it.
[1272.74 --> 1277.74]  Then you see a tweet from Sam Altman, which was something along the lines of, I'm paraphrasing
[1277.74 --> 1281.70]  here, something along the lines of, I'm not mad that they trained on our outputs.
[1281.88 --> 1283.58]  I'm mad that they lied about it.
[1283.58 --> 1289.26]  And I'm sitting there like, okay, you're mad about this, but like, don't you, aren't you
[1289.26 --> 1291.66]  going to pursue the legal action in your terms of services?
[1291.84 --> 1292.62]  No, no.
[1292.72 --> 1295.44]  Because everyone would have to open their books up too.
[1295.94 --> 1300.52]  That being said, I don't condone the commercial use of that kind of stuff.
[1300.92 --> 1304.04]  Like they release, like making a paid model from GPT-4 outputs.
[1304.04 --> 1308.52]  Like I wouldn't advise anyone sell a model made with them just because like, you know,
[1308.92 --> 1311.62]  we want to respect people's like TOS and stuff.
[1311.76 --> 1315.28]  They worked hard and spent billions to make this stuff or hundreds of millions, however
[1315.28 --> 1316.02]  much they spent.
[1316.88 --> 1323.62]  But there is certainly room for hypocrisy in that realm of the large corps.
[1324.02 --> 1326.76]  So that's my thoughts on the licensing stuff.
[1326.84 --> 1329.74]  And that's definitely my own individual thoughts.
[1329.74 --> 1332.76]  Like we're a pretty decentralized collective at Noose.
[1332.88 --> 1336.64]  So you'll find people with all sorts of opinions all over the place.
[1336.74 --> 1340.80]  And as a company, we don't hold any view whatsoever on that.
[1341.24 --> 1341.36]  Yeah.
[1341.84 --> 1346.82]  I'm wondering, maybe this gets a little bit to the distributed nature of this, but I know
[1346.82 --> 1352.66]  that there's sort of various collections of what the Noose Research Group has done over
[1352.66 --> 1353.10]  time.
[1353.32 --> 1358.08]  You mentioned Hermes, but then there's these other kind of categories of things too, like
[1358.08 --> 1364.88]  the yarn models, capybara, puffin, obsidian, just looking over the hugging face now.
[1365.08 --> 1370.30]  I'm wondering if you could just give us like, from your perspective, a little bit of a map
[1370.30 --> 1375.78]  of these different things and like how people might categorize the different collections of
[1375.78 --> 1376.90]  what Noose has done.
[1377.28 --> 1381.40]  I definitely want to talk about like the future things and ongoing things as well.
[1381.40 --> 1387.60]  But as it stands now, what are the kind of major categories of what the collective has
[1387.60 --> 1390.50]  invested in over their time and over time?
[1391.02 --> 1391.76]  Certainly, certainly.
[1392.00 --> 1396.92]  So within the stuff that's viewable on hugging face, at least, we've got the Hermes series
[1396.92 --> 1400.74]  of which, like I told you guys the initial story of how it went down.
[1400.84 --> 1403.20]  But from there, Technium kept going.
[1403.60 --> 1407.86]  I haven't personally had any interaction with the Hermes model since the initial.
[1407.86 --> 1413.18]  From there, Tech just continued to create more and more synthetic data, collect from more
[1413.18 --> 1415.66]  and more sources, use more and more open data sets.
[1415.86 --> 1419.56]  And he's just got the, I guess, award-winning like data thesis.
[1419.82 --> 1424.14]  The guy really knows how to go about curating and synthesizing good data.
[1424.72 --> 1428.14]  So Technium, it's his baby, the Hermes project.
[1428.44 --> 1432.34]  So everything you've seen since is really his work and anyone who has kind of collaborated
[1432.34 --> 1432.86]  with him.
[1433.08 --> 1437.66]  But almost like, you can't call it anything a solo project because of the open data sets
[1437.66 --> 1438.28]  we use too.
[1438.44 --> 1442.34]  Like everything is built on the shoulders of giants and the shoulders of each other as
[1442.34 --> 1442.84]  little people.
[1443.08 --> 1447.30]  But Tech really has helmed the Hermes initiative so far.
[1447.52 --> 1449.54]  I think that's our most popular model series.
[1449.54 --> 1454.68]  And he released the open Hermes as well because we had some data in the original Hermes that
[1454.68 --> 1455.96]  we never released publicly.
[1456.54 --> 1459.52]  And we wanted to make that kind of an option for everybody.
[1459.78 --> 1461.18]  So that's Hermes.
[1461.64 --> 1464.76]  Still follows the same kind of philosophy of synthetic data.
[1464.76 --> 1470.22]  And it now uses the chat ML format instead of the alpaca format is what we kind of upgraded
[1470.22 --> 1470.48]  to.
[1470.62 --> 1476.48]  Then you've got a Capybara and Puffin, which are both done by a volunteer and, you know,
[1476.68 --> 1478.22]  OG member LDJ.
[1478.60 --> 1480.58]  We may be familiar with Luigi Daniel Jr.
[1480.58 --> 1488.92]  So the Capybara series was using an amplify instruct method, this novel method that LDJ
[1488.92 --> 1492.18]  had worked on alongside another one of our researchers, J.
[1492.56 --> 1494.74]  So LDJ and J can get confusing.
[1495.20 --> 1499.88]  But the two of them worked on the Capybara series, created the data set, trained the models.
[1499.88 --> 1507.06]  And then Puffin was the idea of using handpicked smaller samples from some of our larger data
[1507.06 --> 1513.24]  sets to make sleek data sets for an easy tune and see how that works kind of in the spirit
[1513.24 --> 1517.82]  of the Lima paper, where they just used a few examples to get really good results.
[1518.40 --> 1523.48]  Those are really the popular tunes using synthetic data for like general use.
[1523.48 --> 1529.88]  Yarn is this novel context length extension method at the time of creation by Emozilla,
[1530.12 --> 1537.10]  also known as Jeffrey Cannell, and Bowen Pang, also known as Block 97, alongside Enrico
[1537.10 --> 1539.42]  Chipotle and Eleuther AI.
[1540.06 --> 1544.84]  So what happened there was these guys were already looking into context like the extension
[1544.84 --> 1545.52]  for a while.
[1545.72 --> 1551.58]  And when we kind of came under the noose banner to do the work, it opened up a little bit of
[1551.58 --> 1553.64]  resources from compute sponsorships.
[1554.16 --> 1558.96]  It opened up a more centralized place for them to be able to do that collaboration.
[1559.68 --> 1563.46]  I had no hand in the yarn models whatsoever.
[1563.76 --> 1568.38]  And that's the exciting thing is everyone really gets to work in their own spheres and
[1568.38 --> 1569.88]  their own kind of autonomous circles.
[1569.88 --> 1572.72]  And then we just check in and see, you know, how's the research going?
[1572.80 --> 1573.66]  How's it coming along?
[1573.66 --> 1578.74]  Because we really work with people that we heavily believe in and we believe in their idea.
[1578.74 --> 1584.28]  So if we don't already have an idea, we're kind of just say, you know, please freely create
[1584.28 --> 1588.80]  because we brought you in because what we will freely create will push forth our agenda
[1588.80 --> 1589.32]  anyway.
[1589.86 --> 1594.06]  So I think those are our big model releases and series that we have available.
[1594.58 --> 1598.80]  Outside of that, we have a bunch of stuff on our GitHub as well.
[1599.32 --> 1602.36]  Stuff that's being worked on, stuff that hasn't necessarily come out yet.
[1602.44 --> 1603.36]  There's a lot of that.
[1603.36 --> 1606.98]  So I got a question for you as a follow-up.
[1607.34 --> 1611.56]  It's pretty fascinating, the story that you've been telling us here because of that kind of
[1611.56 --> 1615.42]  organic, you know, creation of the organization or collective.
[1615.84 --> 1619.48]  And I'm wondering, as you've done that and you kind of went through and talked about the
[1619.48 --> 1623.64]  different model groups and kind of talked about, you know, the owners or spiritual owners,
[1623.76 --> 1628.28]  if you will, of each of those families, how do the different members of the collective
[1628.28 --> 1630.26]  interact to kind of share?
[1630.26 --> 1636.14]  Like, how do you each push each other along or share information or give ideas so that
[1636.14 --> 1640.96]  cross-family efforts can kind of benefit from the overall collective?
[1641.60 --> 1645.46]  And as you said, now a C-Corp and you guys are more organized at this point.
[1645.56 --> 1649.54]  So what kind of culture has developed around those communications and learnings?
[1649.92 --> 1650.64]  Yeah, absolutely.
[1651.04 --> 1654.76]  I mean, when it started, it was just like a small Discord, maybe like 10 people.
[1654.96 --> 1659.38]  From there, like we kind of created more channels as people wanted to work on more things.
[1659.38 --> 1665.38]  And we had initially split up into like three, four different topics or sectors that people
[1665.38 --> 1666.60]  could assign themselves to.
[1666.92 --> 1671.52]  One being data synthesis, of course, so we can kind of find new novel methods and formats
[1671.52 --> 1673.98]  for distillation and the creation of synthetic data.
[1674.28 --> 1679.24]  One being training, like people who are just like really good at training hyperparam stuff
[1679.24 --> 1683.00]  and people who will come up with new architectures and new techniques.
[1683.46 --> 1688.28]  Another being agents, a group of people who want to actually try to build tools and do autonomous
[1688.28 --> 1689.32]  work with this stuff.
[1689.84 --> 1694.28]  And then we had this one category that it was a prediction for the future of simulation.
[1694.82 --> 1698.34]  So we had people that were very interested in kind of bringing this stuff into simulation,
[1698.64 --> 1701.72]  into Unity, into kind of seeing how all these things came together.
[1701.94 --> 1706.84]  And it was interesting because the training built on the data synthesis, the agents build
[1706.84 --> 1709.48]  on the training, and then the sim would build on the agents.
[1709.70 --> 1710.88]  It was kind of the idea.
[1711.00 --> 1715.20]  So everybody needed to work together because all those things are so intrinsically connected,
[1715.20 --> 1719.90]  but people would have specializations on kind of where in that workflow they wanted to work.
[1720.26 --> 1722.88]  We didn't end up doing a lot on the sim side of things.
[1723.18 --> 1728.26]  Now, recently, there's a lot more interest because we have a lot more capability generally
[1728.26 --> 1729.70]  as the AI community does.
[1730.34 --> 1734.78]  But as we've grown to, we went to 40 people, it was fine.
[1735.04 --> 1737.82]  Now we've gone to like 5,000 people in the Discord.
[1738.24 --> 1739.92]  It's a little unwieldy there.
[1739.92 --> 1743.24]  So what we do is we kind of tier people in.
[1743.44 --> 1745.68]  You come into the Discord, you can see maybe two channels.
[1746.30 --> 1748.38]  And then we'll give people a developer role.
[1748.80 --> 1752.36]  We don't really let people select their own roles because we want to make sure we can kind
[1752.36 --> 1755.46]  of sort through people we know to kind of let them through.
[1755.96 --> 1759.54]  And even as we do open source research, a lot of it is unreleased.
[1759.66 --> 1763.02]  And we want to make sure that it's kind of protected before release.
[1763.02 --> 1768.90]  So we create this developer role so people can then see like way more channels of just
[1768.90 --> 1770.86]  general development and development conversation.
[1771.44 --> 1777.70]  And from there, as we see, you know, contributors who have started to do more work or show more
[1777.70 --> 1783.16]  passion towards contributing to news in a particular field or who have some reputation or some portfolio
[1783.16 --> 1786.80]  in a particular field, then we'll assign them one of those roles.
[1786.80 --> 1792.24]  And that will open up the family of channels relating to those roles and our current projects
[1792.24 --> 1793.56]  surrounding that role.
[1793.66 --> 1797.22]  So like data synthesis projects, agent projects, training projects, et cetera.
[1797.46 --> 1800.46]  So we kind of just tier it out so people can interact.
[1800.90 --> 1804.56]  And people who have been around for a while or people we consider fellows or part of the
[1804.56 --> 1806.96]  cohort, they can usually see pretty much everything.
[1807.60 --> 1813.16]  So they're pretty effective in serving as coordinators for the cross communication between
[1813.16 --> 1815.04]  these different channels and groups.
[1815.04 --> 1820.52]  Even if something has like a particular, someone has a particular role or some channel has
[1820.52 --> 1824.94]  a particular role it's supposed to be a part of, like it's still discord and we're still
[1824.94 --> 1825.62]  very chill.
[1826.10 --> 1832.20]  So like people will still work on like various different overlaps inside of just one channel
[1832.20 --> 1832.60]  as well.
[1832.60 --> 1849.04]  If you're listening, you know that artificial intelligence is revolutionizing the way we produce
[1849.04 --> 1853.62]  information, changing society, culture, politics, the economy.
[1853.62 --> 1858.88]  But it's also created a world of AI generated content, including deep fakes.
[1858.88 --> 1861.36]  So how can we tell what's real online?
[1861.84 --> 1865.16]  Read, write, own, building the next era of the internet.
[1865.32 --> 1871.02]  A new book from entrepreneur and investor Chris Dixon explores one possible solution to the
[1871.02 --> 1873.72]  internet's authenticity problem, blockchains.
[1874.18 --> 1879.78]  From AI that tracks its source material to generative programs that compensate rather than cannibalize
[1879.78 --> 1880.22]  creators.
[1880.80 --> 1886.34]  Read, write, own is a call to action for a more open, transparent and democratic internet.
[1886.34 --> 1891.88]  One that opens the black box of AI, tracks the origins we see online and much more.
[1892.20 --> 1897.30]  This is our chance to reimagine world changing technologies to build the internet we want,
[1897.64 --> 1898.62]  not the one we inherited.
[1899.16 --> 1905.46]  Order your copy of read, write, own today or go to read, write, own.com to learn more.
[1916.34 --> 1923.88]  I have a selfish question, which now that this is one of the advantages of doing the podcast,
[1923.96 --> 1928.20]  I get to talk to all the amazing people doing amazing things and learn from them.
[1928.20 --> 1935.12]  But I'm wondering as a person who is also trying to fine tune some models, either just for my
[1935.12 --> 1943.72]  own enjoyment and learning, but also fine tuning models for specific tasks and in specific customer
[1943.72 --> 1945.50]  use cases and that sort of thing.
[1945.76 --> 1946.94]  There's a lot of people out there.
[1947.04 --> 1951.36]  I think many of our listeners who are thinking like, since you being part of this collective
[1951.36 --> 1958.40]  have worked for, you know, since the sort of dawn of, of these many, you know, the proliferation
[1958.40 --> 1961.04]  of fine tunes, but from llama and et cetera.
[1961.56 --> 1965.06]  And as you've seen all that, as you're doing more and more fine tunes now, as you're looking
[1965.06 --> 1972.38]  towards the future, do you have any kind of good advice or things to keep in mind for all
[1972.38 --> 1978.22]  those like fine tuners out there that are thinking about grabbing something off of hugging face,
[1978.36 --> 1980.76]  creating their own versions of these models?
[1981.00 --> 1985.68]  Maybe they have their own ideas about a specific take on, on a model.
[1985.68 --> 1992.68]  Well, any general tips that you found to be really useful over time or like pitfalls that
[1992.68 --> 1993.48]  you'd like to highlight?
[1993.84 --> 1994.08]  Yeah.
[1994.20 --> 1996.98]  I mean, I can, I can try to think of a few off the top of head.
[1997.12 --> 2002.68]  I'll say that hyperparameters are really important and it's important to try to get that right.
[2002.90 --> 2007.02]  It's going to vary from model to model, but a lot of the time, some people think hyperparams
[2007.02 --> 2010.60]  like don't really matter as much to like obsess over.
[2010.60 --> 2013.96]  And some people think it's like a secret sauce as well.
[2013.96 --> 2018.76]  So I'd say like try to do a lot of research into like good hyperparams, a good learning
[2018.76 --> 2019.08]  rate.
[2019.28 --> 2024.98]  Like I'd also say like, I could be totally wrong about this as I am not the trainer of
[2024.98 --> 2026.88]  Hermes today or a lot of these models.
[2026.88 --> 2031.46]  But something I personally believe in a lot is like ignore like people telling you to only
[2031.46 --> 2032.92]  train for like X amount of time.
[2032.92 --> 2035.60]  Like if you're not overfitting, like just keep going.
[2035.60 --> 2040.18]  Like if you can, if you have the compute, like keep training and keep going, like train for
[2040.18 --> 2041.90]  more tokens, more epochs.
[2041.90 --> 2046.66]  Like that's something I heavily believe in, uh, in terms of trainers to use, there's a
[2046.66 --> 2049.96]  lot of people who make their own scripts for specialty stuff.
[2049.96 --> 2054.90]  And there's of course, like, you know, you can just use hugging face, but the library we
[2054.90 --> 2062.78]  use is called axolotl, A-X-O-L-O-T-L, like the animal, uh, by Cassius, uh, wing Leon of the
[2062.78 --> 2063.88]  open access collective.
[2063.88 --> 2069.36]  We think axolotl is probably the best general purpose trainer for Laura's, Q Laura's, fine
[2069.36 --> 2070.04]  tunes, et cetera.
[2070.64 --> 2075.94]  It like any open source repository is buggy and stuff you're going to have to work out,
[2076.04 --> 2081.90]  but it's in my opinion, probably the easiest and most effective trainer to use for like
[2081.90 --> 2084.80]  pretty much any model architecture available right now.
[2084.94 --> 2087.72]  So I definitely point everybody towards axolotl.
[2087.72 --> 2088.64]  Awesome.
[2088.94 --> 2089.90]  Yeah, that's super useful.
[2090.06 --> 2093.06]  We'll, we'll share some links in, uh, in our show notes as well.
[2093.06 --> 2096.34]  So people make sure, uh, and check that stuff out.
[2096.58 --> 2098.56]  Another kind of interesting question.
[2098.56 --> 2106.16]  Um, as you see, you know, I think we saw these waves of, of models that came out maybe around,
[2106.16 --> 2111.66]  uh, synthetic data, fine tunes or, or other types of fine tunes.
[2111.66 --> 2118.22]  I see this like interesting sort of thing happening over the past, however many months, you know,
[2118.22 --> 2123.02]  not that long in the scheme of things, but in the AI world, maybe a while where we're
[2123.02 --> 2128.00]  kind of now like, there's a lot of interesting approaches more so than just fine tunes, but
[2128.00 --> 2130.16]  like mixture of experts and merging.
[2130.66 --> 2133.04]  And of course, multimodal stuff coming out.
[2133.12 --> 2138.10]  Now I see news kind of dabbling in that you don't have to answer for the whole collective,
[2138.10 --> 2142.78]  but as there's so many of these things coming out and different approaches, what are some
[2142.78 --> 2148.06]  of the things within that doesn't have to be one of those, but what are some of the things
[2148.06 --> 2154.02]  on, on your mind kind of moving forward, uh, or on, uh, nooses mind kind of more generally.
[2154.48 --> 2154.64]  Sure.
[2154.80 --> 2159.60]  Um, I'll try to go from like simple to complex on the kind of stuff.
[2159.80 --> 2160.36]  That sounds great.
[2160.44 --> 2164.78]  I think that definitely just like straight up instruction tuning is great.
[2164.78 --> 2168.42]  There's other ways to tune like the evolve instruct method.
[2168.56 --> 2173.02]  I would advise people to try to create new instruction methodologies that allow us to
[2173.02 --> 2175.40]  make even better formatted data.
[2175.78 --> 2178.98]  People don't spend enough time trying to create new instruct formats.
[2179.34 --> 2182.66]  Uh, and we've definitely been swamped with not doing that as well.
[2182.66 --> 2187.04]  So I think towards the general community, it's a really easy place to get started.
[2187.34 --> 2191.62]  You don't need to really know how to code so much as think about how a human might more
[2191.62 --> 2195.58]  effectively phrase something or format something and kind of remix from there.
[2195.58 --> 2198.36]  I think that's like probably the easiest place to start.
[2198.76 --> 2200.74]  Then there's a model merging, right?
[2200.82 --> 2201.78]  Model merging is great.
[2202.22 --> 2205.96]  You can just like take two models and Frankenstein them together to question mark results.
[2206.40 --> 2209.82]  You know, you gotta just try and see what happens and feel it out.
[2209.82 --> 2214.10]  Then from there, I would say there's stuff like DPO.
[2214.70 --> 2220.98]  There's RLHF, DPO, like this kind of rewards things that can let you like enable rejections
[2220.98 --> 2226.84]  or create censorship or put some kind of general concept or attitude towards a model.
[2227.40 --> 2231.60]  We found that to be pretty effective with the latest Noose Hermes Mixtral DPO.
[2231.96 --> 2235.58]  It seems like people really like it and prefer it over just the SFT.
[2235.58 --> 2239.10]  So that's another thing that I'd heavily recommend.
[2239.52 --> 2242.38]  From there, we get a little more complex.
[2243.00 --> 2246.98]  We have some reward model stuff we're working on that I won't speak to just yet outside of
[2246.98 --> 2251.14]  saying we're working on it that we think is going to be like pretty big for reasoning boosts.
[2251.44 --> 2255.46]  Of course, there's techniques like chain of thought and tree of thought for like multi-step
[2255.46 --> 2256.30]  prompting.
[2256.80 --> 2262.38]  Creating data sets even out of that for any of these purposes I've already mentioned is going
[2262.38 --> 2263.14]  to be really effective.
[2263.14 --> 2268.10]  Right now to stuff that maybe not everybody can actually a lot of people would already
[2268.10 --> 2268.94]  be able to do this.
[2268.94 --> 2274.26]  There's like something that we like to call over at Noose Activations Hacking where you're
[2274.26 --> 2279.32]  kind of messing with the way that a model I'm trying to think about how to say this in
[2279.32 --> 2280.56]  like the most layman's terms.
[2280.56 --> 2284.62]  Like you're trying to mess with how a model like generally vibes about something.
[2285.68 --> 2290.52]  So rather than just doing a system prompt or something like that, you can actually like change
[2290.52 --> 2295.48]  the model vectors to kind of be like more political about something, less political about something,
[2295.48 --> 2297.44]  more terse, more specific.
[2297.84 --> 2302.22]  And it has far more effect and control over a model than a system prompt.
[2302.48 --> 2306.08]  It's basically like a system prompt that like tells it to embody certain characteristics,
[2306.08 --> 2309.98]  but it's not something you can really jailbreak or get around.
[2309.98 --> 2314.42]  As far as my testing is shown, certainly not as easily as a system prompt.
[2314.94 --> 2319.38]  Like we have no problem jailbreaking even the most censored closed models today.
[2319.50 --> 2322.40]  Like it can be done by anybody with the right words.
[2322.54 --> 2322.68]  Right.
[2323.08 --> 2328.30]  But this activation stuff, it really creates a bit more of a robustness and fidelity to the
[2328.30 --> 2330.64]  concepts that you're trying to tell it to embody.
[2330.64 --> 2334.68]  There's a few more I'm trying to think of that would be useful for people.
[2335.38 --> 2337.38]  One thing is soft prompting.
[2337.68 --> 2338.96]  It's not really around anymore.
[2339.08 --> 2342.54]  It used to be pretty big during the GPT-J like pre-Llama days.
[2342.90 --> 2347.24]  And the Cobalt AI guys really pioneered the use of it in the open source community.
[2347.80 --> 2353.50]  But a soft prompt basically takes like massive prompt and compresses it down to like way less
[2353.50 --> 2353.88]  tokens.
[2353.88 --> 2359.62]  So you can give your model like a huge prompt, a huge system prompt or a huge amount of information
[2359.62 --> 2361.86]  and use like way less tokens.
[2362.46 --> 2363.50]  So soft prompting is cool.
[2363.70 --> 2369.30]  It's not going to be too difficult to like update it for like Llama, Mistral, like today's
[2369.30 --> 2369.86]  architectures.
[2370.02 --> 2372.12]  It's just like nobody has really done it that I've seen.
[2372.78 --> 2376.82]  So, you know, to the community, if you guys do that, please share.
[2378.96 --> 2381.76]  That's actually much easier than the activation stuff, I think.
[2381.76 --> 2387.58]  And then finally, probably the hardest unsolved is like sampling methods.
[2387.98 --> 2393.76]  Like today we use like top K, top P, like, you know, nucleus sampling, et cetera, whatever.
[2393.96 --> 2397.00]  Like there's better ways to pick tokens for sure.
[2397.12 --> 2399.90]  There's better ways to judge the value of tokens for sure.
[2400.42 --> 2406.20]  Everyone has been too kind of concerned with higher levels to get that low and do whatever
[2406.20 --> 2414.06]  the magic math is that I can't do that would, you know, enable some steering and some even
[2414.06 --> 2416.86]  beyond steering, like alternative sampling paradigms.
[2417.26 --> 2422.70]  And I think that would probably bring the biggest change and transformation to literally
[2422.70 --> 2426.70]  all models, regardless of the tune, regardless of the architecture, et cetera.
[2427.42 --> 2428.54]  Get pulled off.
[2428.54 --> 2431.84]  So really looking forward to something like that happening in the space.
[2432.52 --> 2435.00]  That was a lot of really good advice that you have there.
[2435.06 --> 2439.72]  I was sitting there trying to take notes while you're talking through it and everything going,
[2439.82 --> 2440.70]  wait, but he said that too.
[2440.72 --> 2441.46]  And he said that too.
[2441.58 --> 2443.20]  No, the really good answer there.
[2443.92 --> 2444.82]  Thank you for that.
[2445.30 --> 2450.64]  As we're starting to wind up here, I wanted to ask you, I know about as we're recording,
[2450.64 --> 2455.74]  this is looks like it was just over three weeks ago, about four weeks ago when we release this
[2455.74 --> 2461.56]  episode, you guys announced your $5.2 million seed financing round.
[2461.70 --> 2463.30]  So congratulations on that.
[2463.40 --> 2464.82]  That was pretty amazing.
[2465.04 --> 2465.50]  Thank you.
[2465.82 --> 2470.56]  And I'm kind of wondering, so like you've kind of started with this kind of fairytale story
[2470.56 --> 2475.82]  of kind of organically building from the ground up, you know, yourself, you connect with somebody
[2475.82 --> 2479.96]  else, a few other people join, you get to thousands of people contributing.
[2479.96 --> 2484.20]  You find and really producing amazing work.
[2484.44 --> 2489.18]  And then you're incorporating and now you got the seed round coming.
[2489.42 --> 2490.70]  Where does that lead you?
[2490.82 --> 2493.32]  It's kind of a sky's the limit kind of scenario.
[2493.32 --> 2497.88]  It seems, you know, that now that you're, you're kind of launching and, you know, on that,
[2497.96 --> 2501.10]  you know, as a corporation, as you said, where can you go from here?
[2501.18 --> 2506.62]  What do you anticipate over the next couple of years or even several years out?
[2506.70 --> 2507.86]  You know, what's the vision?
[2508.54 --> 2509.30]  What do you want to achieve?
[2509.30 --> 2510.62]  You've come a long way so far.
[2510.70 --> 2511.28]  What's next?
[2511.74 --> 2512.06]  AGI.
[2512.26 --> 2512.78]  No, I'm just kidding.
[2515.06 --> 2516.92]  I believe you if you said it, actually.
[2517.16 --> 2517.72]  No, no, no.
[2518.04 --> 2519.76]  I mean, like, you know, someone will do it.
[2520.68 --> 2522.48]  And then you'll distill the knowledge.
[2523.44 --> 2528.40]  Then we'll distill and then you'll run the AGI on your, on your neural link, on your contact
[2528.40 --> 2529.20]  lens or something.
[2529.20 --> 2530.28]  That's right.
[2530.28 --> 2534.90]  But for us, like, there's a huge focus on locality.
[2535.08 --> 2536.48]  There's a huge focus on offline.
[2536.72 --> 2540.62]  There's a huge focus on take the power back, run the model yourself, do everything at home.
[2540.80 --> 2542.26]  Like, that's big for us.
[2542.32 --> 2544.38]  And at the same time, of course, we believe in scale.
[2544.38 --> 2548.56]  But there's this idea that, you know, there's so much unsolved at the small model size.
[2548.90 --> 2551.14]  Why don't we do that before we go to a trillion params?
[2551.42 --> 2553.06]  Because we can scale those realizations.
[2553.58 --> 2558.66]  But for us, like, there's certainly, you know, a transformation and change in attitude and in
[2558.66 --> 2563.98]  pressures from going from pure open source volunteer to as well having kind of this more
[2563.98 --> 2566.06]  corporate branch could create it as well.
[2566.06 --> 2572.88]  But that being said, it's been pretty consistent, our ethos and our motivation for why we do
[2572.88 --> 2573.22]  this.
[2573.54 --> 2577.46]  And like you said, it really was organic in the sense that, like, we're a product of
[2577.46 --> 2577.92]  the times.
[2578.32 --> 2581.08]  We're a product of the atmosphere of the AI community.
[2581.38 --> 2584.40]  Like, people have said nice things, like, you guys are setting the trend.
[2584.52 --> 2589.28]  And it's not really true so much as the truth is, like, we are one of many embodiments of
[2589.28 --> 2592.88]  the sentiment that the community has and that the world has, we think.
[2593.18 --> 2595.56]  Like, there's more than one noose research in this world.
[2595.56 --> 2598.26]  You know, there's alignment labs, there's Pygmalion, there's COBOL.
[2598.34 --> 2602.18]  There's people who have been around before us, people who will come along the way, people
[2602.18 --> 2603.62]  who have already formed since we have.
[2604.28 --> 2609.80]  And there's lots of people who have kind of embodied the noose research ethos.
[2609.84 --> 2613.32]  And it's not really just our ethos as much as the overall community's ethos.
[2613.46 --> 2619.08]  There are people who have come before us, people who will come along the way, who do very,
[2619.18 --> 2622.66]  very similar style of work as us, this kind of open work.
[2622.66 --> 2627.50]  And I think that's got everything to do with the fact that, like, this is what the people
[2627.50 --> 2627.94]  want.
[2628.36 --> 2630.90]  We're just the everyman, just like everybody else.
[2631.06 --> 2637.02]  We're not like billionaires or super, like, all ex-Facebook or anything like that.
[2637.10 --> 2643.90]  We're just a bunch of people who really, really care about this, who want to see everyone have
[2643.90 --> 2649.62]  access to language models, everyone be able to automate their lives, everyone be able to push
[2649.62 --> 2652.24]  their understanding of any topic to the next level.
[2652.94 --> 2658.74]  And our work, as we become an organization that's looking to, you know, be a company and
[2658.74 --> 2664.28]  create revenue, et cetera, we won't let it tamper or hinder any of the open source work
[2664.28 --> 2664.58]  we do.
[2664.70 --> 2670.08]  In fact, we want it to empower all of that work because we believe that the tools and the
[2670.08 --> 2675.80]  developments and services that we will be providing as a corporation will only serve
[2675.80 --> 2679.44]  to better feed the entire open source community.
[2679.78 --> 2684.66]  We're not really looking to suddenly make like a closed Hermes or something like that.
[2684.74 --> 2691.88]  We're more looking to create tools and do research that makes your open Hermes far more effective,
[2692.18 --> 2692.94]  far better.
[2693.18 --> 2696.00]  And, you know, good enough that you may want to pay for that tool.
[2696.00 --> 2699.94]  It sounds like something I would pay for.
[2700.26 --> 2700.80]  That's for sure.
[2701.06 --> 2701.78]  Thank you.
[2702.14 --> 2703.62]  Yeah, it's super inspiring.
[2703.90 --> 2707.72]  I really appreciate you taking time, Curran, to talk with us.
[2707.80 --> 2712.98]  I thoroughly enjoyed this because I am such a fan of everything you all are doing and the
[2712.98 --> 2714.06]  community that you've built.
[2714.28 --> 2718.50]  So thank you for saying true to that culture and what you're doing.
[2718.74 --> 2723.60]  And I'm really looking forward to seeing what happens in the future and where things head.
[2723.60 --> 2729.80]  And I hope that we can talk again and have Noose back on the show in a year when, of course,
[2729.86 --> 2732.10]  everything will be different in the AI world.
[2732.20 --> 2735.08]  And I'm sure you'll still be doing interesting things.
[2735.28 --> 2737.14]  So yeah, you're always welcome back on the show.
[2737.48 --> 2738.30]  Thank you so much.
[2738.38 --> 2740.80]  It's been a pleasure to chat with you guys.
[2741.02 --> 2742.06]  Thanks for being so candid.
[2742.82 --> 2745.52]  I'm glad we were able to kind of push our message forth more.
[2745.68 --> 2749.48]  And thanks for the validation you and the community have given us to keep doing this great work.
[2749.98 --> 2750.26]  All right.
[2750.32 --> 2750.62]  Thanks.
[2750.70 --> 2751.38]  We'll talk soon.
[2751.72 --> 2752.04]  See ya.
[2753.60 --> 2761.42]  That is Practical AI for this week.
[2761.58 --> 2762.30]  Thanks for listening.
[2762.86 --> 2763.66]  Subscribe now.
[2763.78 --> 2768.14]  If you haven't yet, head to practicalai.fm for all the ways.
[2768.46 --> 2771.18]  And don't forget to check out our fresh changelog beats.
[2771.74 --> 2775.92]  The Dance Party album is on Spotify, Apple Music, and the rest.
[2776.16 --> 2777.80]  There's a link in the show notes for you.
[2777.80 --> 2785.46]  Thanks once again to our partners at Fly.io, to our Beat Freakin' Residents, Breakmaster Cylinder, and to you for listening.
[2785.84 --> 2786.74]  That's all for now.
[2786.74 --> 2788.30]  We'll talk to you again next time.
[2788.30 --> 2788.32]  We'll talk to you again next time.
