[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.02 --> 36.08]  Learn more at fly.io.
[42.74 --> 46.02]  Welcome to another episode of Practical AI.
[46.40 --> 47.88]  This is Daniel Whitenack.
[48.02 --> 53.64]  I'm a data scientist with SIL International and joined as always by my co-host, Chris Benson.
[53.94 --> 54.66]  How's it going, Chris?
[54.90 --> 55.80]  Going very well.
[55.80 --> 56.86]  Spring is in the air.
[57.02 --> 58.36]  We're having a good time here.
[58.46 --> 60.10]  Lots of cool stuff in the AI world.
[60.58 --> 68.74]  Lots of new life breathed into interesting AI systems over the past days.
[68.98 --> 75.94]  And sometimes I hear about this in cool videos, which are way cooler than any videos that I
[75.94 --> 79.62]  produce from our friend Raj, who's with us today.
[80.00 --> 84.38]  Rajiv Shah, who's a machine learning engineer at Hugging Face.
[84.48 --> 85.16]  How are you doing, Raj?
[85.16 --> 86.38]  I'm doing great.
[86.46 --> 87.28]  Thanks for having me on.
[87.84 --> 88.12]  Yeah.
[88.38 --> 92.96]  So the last time you were on the show, we talked about data leakage.
[93.46 --> 97.34]  Have you leaked any data since the prior episode?
[97.68 --> 101.98]  I think any data scientist that's out there has leaked data on a regular basis like that,
[102.02 --> 102.18]  right?
[102.22 --> 103.72]  It's a hazard of the job.
[103.72 --> 108.78]  One of the things I like to do is continually remind the new folks that that's likely to
[108.78 --> 109.10]  happen.
[109.76 --> 113.56]  That they are in the process of and should remember.
[113.98 --> 114.12]  Yeah.
[114.12 --> 114.20]  Yeah.
[114.84 --> 115.40]  Yeah.
[115.40 --> 121.10]  I did mention I've seen a lot of cool videos from you recently and we were chatting even
[121.10 --> 128.96]  a bit, I think, on LinkedIn about there is data science AI community on TikTok and other
[128.96 --> 129.38]  places.
[129.76 --> 131.22]  Tell us a little bit about that.
[131.26 --> 132.90]  I'm just I mean, that's a fun topic.
[133.00 --> 136.70]  I'm curious of what is the AI scene like on TikTok?
[136.70 --> 139.34]  So let me start by like how I got into it.
[139.60 --> 145.54]  About like a year ago, I was trying to get my son who's just starting college to do a
[145.54 --> 147.26]  real practical project around AI.
[147.40 --> 150.12]  Like he's taking computer science, but he doesn't know what GitHub is.
[150.18 --> 155.22]  So I'm like, can we build a Discord bot, for example, something that appeals to him?
[155.64 --> 157.44]  And so I was like, let's give us 24 hours.
[157.52 --> 158.44]  We'll do this over the weekend.
[158.58 --> 160.18]  We'll both go our separate ways.
[160.20 --> 163.16]  And then we'll come back and kind of see what we've done and see if we could share what
[163.16 --> 164.10]  we've learned from each other.
[164.10 --> 168.06]  And so I go out and I go get a blog tutorial and work my way through it and kind of get
[168.06 --> 168.68]  something working.
[169.02 --> 172.52]  And then I go to him the next day and he's like, yeah, I kind of got stuck.
[172.60 --> 174.32]  I was like, well, let me see if I can help you through it.
[174.36 --> 176.82]  Like show me the steps and what you were accomplished in doing it.
[177.46 --> 181.46]  He pops open a YouTube video and that's what he used to follow it.
[181.56 --> 186.38]  And for somebody like me who self-taught their way into data science that was largely focused
[186.38 --> 191.56]  on kind of reading and written material, it kind of really blew my mind that somebody would
[191.56 --> 193.76]  learn how to code through a video.
[193.76 --> 198.16]  But it really just opened my eyes to that because already at that time, like with my
[198.16 --> 202.42]  daughter, I shared videos on like food and politics and music.
[202.42 --> 208.06]  But it just really came to me like how this is just becoming an emerging part of education
[208.06 --> 210.96]  and how people learn kind of as we move on here.
[211.48 --> 211.68]  Yeah.
[211.76 --> 215.90]  And have you seen like engagement with your videos on?
[216.22 --> 220.64]  So like I remember the one recently I saw was like the what is it?
[220.64 --> 221.90]  Segment Anything or Everything.
[222.02 --> 225.00]  I forget which is Anything and Everything, whatever that one is.
[225.10 --> 229.06]  I saw your video on that one, which was cool because it's also very engaging.
[229.48 --> 233.82]  You've got like this skit element to it, but there's real information content in there,
[233.82 --> 234.22]  right?
[234.24 --> 235.30]  In an engaging way.
[235.42 --> 237.32]  How do you see people respond to these?
[237.84 --> 241.96]  So I've had great feedback and I try to keep mine very focused on data science.
[242.04 --> 243.56]  I try not to be too clickbaity.
[243.56 --> 247.32]  I try to be like, you know, if I was on a data science team, would I recommend somebody
[247.32 --> 249.22]  to watch the video like that?
[249.54 --> 252.30]  But the video style also lets you do different things.
[252.42 --> 255.72]  So I think when I first started videos, I did, you know, I used to be a professor.
[255.72 --> 260.26]  I did like the traditional, let me just lecture you on this topic for 30 seconds.
[260.52 --> 264.52]  But like, I think as you mentioned over time, like there's more creative ways of doing it.
[264.60 --> 269.18]  And one of the things TikTok allows you to do is often tell it in a story or skit format
[269.18 --> 271.82]  where you could have the voices of multiple people.
[271.82 --> 276.56]  If you're sitting at home on your phone, that's a much more interesting way to like get a nuanced
[276.56 --> 281.30]  conversation rather than reading kind of some blog post that has, here's four different
[281.30 --> 282.62]  points on this.
[282.90 --> 286.70]  So, you know, I think there's a lot of potential for kind of teaching nuanced with something
[286.70 --> 287.18]  like TikTok.
[287.58 --> 288.62]  Yeah, that's cool.
[288.74 --> 292.62]  And there's no shortage of things right now to talk about.
[292.70 --> 298.72]  It's like, you probably are more constrained on your ability to pump out these videos than
[298.72 --> 301.32]  like the AI things that are coming out.
[301.32 --> 306.56]  We've all had our minds blown recently, especially the capabilities of large language models.
[306.56 --> 310.38]  But there's also, of course, other things in computer vision and other things.
[310.90 --> 315.74]  For you, what have been those mind blowing moments or what has been on your mind over
[315.74 --> 316.36]  the past?
[316.58 --> 319.42]  I can't even say like the past year, like the past two weeks.
[319.58 --> 319.92]  I don't know.
[320.00 --> 320.34]  I don't know.
[320.34 --> 326.38]  So I think we just have to look back and reflect that we're really in a great place of a huge
[326.38 --> 328.16]  amount of innovation in a short amount of time.
[328.36 --> 332.96]  Like this is one of those peak times in AI that it won't be like this a year from now,
[333.02 --> 333.18]  right?
[333.18 --> 337.26]  It wasn't like this two years or three years from now where literally every week there's
[337.26 --> 337.98]  new developments.
[338.38 --> 339.56]  It's a fabulous time.
[339.56 --> 343.50]  If you're an AI junkie and you like to kind of check out and see the newest tools and
[343.50 --> 346.90]  see that incremental advance like that, there's no better time.
[347.00 --> 348.14]  It's not going to last for long.
[348.24 --> 349.20]  So kind of enjoy it.
[349.72 --> 354.54]  I also kind of also push back on this for lots of practicing data scientists that are
[354.54 --> 358.26]  very practical that, you know, you don't need to watch this stuff every day or every
[358.26 --> 359.26]  week like that.
[359.26 --> 363.48]  Like many of these things are exciting, but if you're day in and day out, you're an enterprise
[363.48 --> 368.14]  data science, you're inside doing churn analysis or some marketing analysis.
[368.76 --> 372.12]  Many of these developments are going to take a while before they filter you to you.
[372.36 --> 374.24]  You'll have plenty of time to get up to speed.
[374.52 --> 379.58]  They're not going to change the face of every data scientist in the next two months like that.
[380.04 --> 380.72]  So I'm curious.
[380.86 --> 383.40]  It's a follow-up to both of these last two questions combined.
[383.86 --> 386.48]  You're going into different mediums now for teaching.
[386.48 --> 389.38]  You're hitting short video, longer video, different things.
[389.54 --> 392.30]  You're we have all of this happening so fast.
[392.78 --> 396.86]  How are you thinking about reaching different audiences in data science?
[396.92 --> 397.38]  It's kind of funny.
[397.50 --> 399.70]  Once upon a time, it was just data science.
[399.70 --> 403.62]  But now we have different audiences, different age groups, different purposes.
[404.00 --> 406.34]  How are you making those different connections?
[406.54 --> 411.40]  I was just talking to someone today that the co-op is like students coming into college now
[411.40 --> 412.32]  can't type.
[412.66 --> 414.80]  Typing isn't a thing anymore, right?
[414.80 --> 417.52]  Because of the way they've grown up with devices, right?
[417.60 --> 419.76]  Like they can poke and like touch screen.
[420.38 --> 426.24]  But that's got to influence like if we're not adapting to that, then we're not staying up.
[426.28 --> 426.74]  Right, Chris?
[427.14 --> 428.50]  You just made me feel really old.
[430.80 --> 434.22]  And I think one thing that's happened is like data science came out of statistics.
[434.22 --> 435.60]  And for a long time, right?
[435.62 --> 438.32]  The path to learn that was you went to college.
[438.32 --> 440.28]  You sat in a classroom, right?
[440.30 --> 442.02]  You had a statistics book to do that.
[442.02 --> 446.62]  But I think this is the transformative part about AI and data science where now it's touching
[446.62 --> 447.62]  so many people.
[447.84 --> 451.92]  And especially you see this with these large language models where if you're a teenager,
[452.18 --> 453.18]  you have a GPU.
[453.50 --> 458.10]  All of a sudden now you can kind of download and follow a script and get something running
[458.10 --> 462.02]  on your local machine where you can interact with this AI, right?
[462.06 --> 466.64]  Which a couple of years ago would have been unheard of for somebody to have such wide access
[466.64 --> 467.00]  to that.
[467.00 --> 471.60]  So I think the hard part about communicating to so many audiences is also a great part that
[471.60 --> 476.52]  we have such a large community that's engaged and interested and wants to use these tools.
[477.28 --> 482.04]  I'm going to bring a couple things here on the fly for you, Raj, because you are so good
[482.04 --> 483.60]  at explaining these things.
[483.96 --> 485.62]  So I'm at a conference right now.
[485.78 --> 488.54]  So I walked from a talk over back to here.
[489.14 --> 493.86]  And yeah, one of the things that they were talking about was in context learning with large
[493.86 --> 494.60]  language models.
[494.60 --> 497.06]  Could you kind of help us?
[497.10 --> 501.32]  So we've talked a lot about on the show about prompting large language models, this sort
[501.32 --> 501.64]  of thing.
[501.64 --> 506.38]  But I don't know that we've specifically kind of talked through this like in context learning.
[506.38 --> 509.02]  Like what does that exactly mean?
[509.02 --> 511.06]  And what should people take away from it maybe?
[511.66 --> 515.32]  So if we look at the development of these language models, a couple years ago, if you look
[515.32 --> 520.56]  at there was blog posts by Carpathion kind of working with LSTMs and how we could get these
[520.56 --> 522.60]  models to generate text for us.
[522.60 --> 527.62]  And this is where we have kind of the statistical probabilities of being able to put together
[527.62 --> 528.38]  text.
[528.38 --> 532.54]  And it knows like the cat ate the dog or that there's some probabilities and we could put
[532.54 --> 533.18]  a sentence together.
[533.38 --> 535.06]  And a couple years ago, right?
[535.06 --> 538.44]  These were fantastic things at making like really weird stories.
[538.44 --> 538.72]  Yeah.
[538.84 --> 539.02]  Right.
[539.04 --> 540.14]  And that's all they were good for.
[540.14 --> 543.22]  Like when we look at like kind of the GPTools like that.
[543.22 --> 548.78]  Now, what's happened is as we've kind of worked with these large language models and they've
[548.78 --> 552.70]  gotten bigger where we've incorporated more data, we've trained them longer.
[552.70 --> 557.88]  Machine learning engineers have noticed a new kind of what they call an emergent behavior
[557.88 --> 562.14]  that's come about from these models that isn't there at the smaller size of the models.
[562.14 --> 568.16]  But when these models get really big, they allow this new capability of this in context
[568.16 --> 569.16]  learning.
[569.16 --> 574.16]  And what in context learning allows you to do is you can give the model a few examples
[574.16 --> 579.16]  of a type of question and the model will then continue to answer in that question.
[579.16 --> 582.14]  So an easy example of this is sentiment.
[582.70 --> 585.36]  Imagine you had to have movies and you had to rate the sentiment.
[585.70 --> 589.52]  In the old days, if you wanted to do this, you would have to go out and label a bunch
[589.52 --> 590.28]  of movies, right?
[590.30 --> 592.06]  Let's go get a hundred or a thousand movies.
[592.34 --> 593.68]  We read the reviews.
[593.96 --> 595.20]  We label the sentiment, right?
[595.22 --> 596.02]  Is this a good review?
[596.06 --> 597.02]  Is this a bad review?
[597.40 --> 599.40]  Then we train our model to do that, right?
[599.44 --> 601.10]  That's traditional data science approach.
[601.58 --> 606.10]  What we can do with these larger language models is say, hey, here's three examples.
[606.10 --> 607.60]  Two of these are good movie reviews.
[607.60 --> 609.50]  One of these is a bad movie review.
[609.94 --> 612.02]  Now I'm giving you a new movie review.
[612.48 --> 614.22]  Will you tell me what this movie review is?
[614.76 --> 617.38]  And the model will reach back with us with the answer.
[617.58 --> 620.66]  And the key here is we're not changing the weights of the model.
[620.74 --> 622.42]  We're not training the model in any way.
[622.76 --> 628.24]  Just by carefully asking it for some type of information, it knows and can kind of figure
[628.24 --> 629.82]  out, oh, you like it like this?
[630.20 --> 635.90]  Well, I will give you back an answer in that same kind of format style, same type of information.
[635.90 --> 638.80]  And so this for me is just mind blowing.
[638.80 --> 644.46]  And it also makes us rethink like a lot of the tasks we do in NLP and how many of these
[644.46 --> 647.18]  we're going to be able to use this paradigm to do it.
[647.28 --> 648.38]  So that was a long answer.
[648.46 --> 650.36]  I'll let you see how much of it you digested.
[650.74 --> 652.22]  And that was a really good answer.
[652.42 --> 656.62]  So, you know, we all have this new skill that we've been developing, you know, around
[656.62 --> 658.50]  prompting, especially this past year.
[659.02 --> 662.70]  Prompt engineering is now a thing, which it wasn't very far back.
[662.70 --> 664.36]  It was you'd go, what was that?
[664.78 --> 666.64]  So how does this all tie in?
[666.68 --> 671.20]  We have this new skill about prompting and learning how to prompt effectively to get this
[671.20 --> 671.62]  information.
[671.84 --> 675.34]  You're talking about this emergent quality of these large language models.
[675.66 --> 676.94]  How do those tie in?
[677.04 --> 678.62]  What does that imply for steps forward?
[678.64 --> 682.38]  And what should people be thinking about to make that productive forum and day-to-day use?
[683.04 --> 686.06]  Let's take this example to like something that you would do practically inside an enterprise
[686.06 --> 691.88]  where somebody might give you some type of document or chat transcript, which might be
[691.88 --> 692.86]  a little bit unstructured.
[693.06 --> 695.28]  And what you want to do is just categorize it.
[695.62 --> 699.94]  So now what we can do with using these prompting and these approaches is we can take that amount
[699.94 --> 700.60]  of information.
[701.04 --> 703.50]  I can ask the model, hey, will you structure it?
[703.50 --> 704.08]  Will you clean this?
[704.14 --> 706.08]  Will you take out the HTML format tax?
[706.40 --> 707.04]  It'll do that.
[707.60 --> 708.96]  And then I can ask it another prompt.
[709.34 --> 710.58]  Hey, can you summarize this?
[710.70 --> 714.22]  Like take this from a hundred line conversation just down to the essentials, 20 lines.
[714.22 --> 715.74]  You can write a prompt for that.
[716.16 --> 718.16]  Then you can ask it, hey, will you categorize this?
[718.26 --> 720.74]  I need to see, you know, should I send this to my claims department?
[720.84 --> 721.62]  Does it go to HR?
[721.74 --> 722.48]  Does it go to IT?
[723.30 --> 724.48]  We can write a prompt for that.
[724.60 --> 729.52]  And so now what you have developers using is tools like Langchain where they can tie together
[729.52 --> 735.20]  several of these prompts and create workflows that in the prior to this, we'd have to use
[735.20 --> 738.20]  separate, you know, machine learning models to do each of those tasks.
[738.38 --> 743.24]  And I think this is really for me what the mind-blowing part of it is how it can change machine
[743.24 --> 748.92]  learning and really do a lot of this democratization that we've talked about for a long time, but
[748.92 --> 753.74]  do it through a natural language interface where somebody can just literally give it these
[753.74 --> 757.76]  tasks in a human language and then have them accomplished, right?
[757.80 --> 761.02]  For the data scientists out there, it's a little mind-blowing because I've been in this
[761.02 --> 764.22]  place where we've tried to teach people citizen data science.
[764.22 --> 770.04]  And we have classes on how to properly partition data and holdouts and loss metrics and all
[770.04 --> 770.46]  of this.
[770.90 --> 775.94]  But like this approach dramatically kind of changes how the number of tasks people can
[775.94 --> 779.08]  do kind of without having to learn all those concepts.
[779.80 --> 780.56]  That's a great point.
[780.94 --> 785.28]  With the advent of ChatGPT and some of the others that are out, Bart and everything coming
[785.28 --> 789.90]  out, it has exploded the audience that can productively use this technology.
[790.30 --> 794.34]  So, and do you see any limitations in that going forward or do you think it's going to
[794.34 --> 795.00]  continue to grow?
[795.34 --> 798.94]  And I think this is to Daniel's point earlier, this is the mind-blowing part is I gave you
[798.94 --> 799.82]  the simple example.
[800.54 --> 807.14]  Now what you see people doing is taking this, but combining this with other APIs and other
[807.14 --> 807.66]  services.
[808.54 --> 813.90]  So in that case of the movie reviews, maybe I want to get the weather forecast or I want
[813.90 --> 816.56]  to find out if the theater was open that day, something else.
[816.96 --> 823.18]  Well, now I can use that same type of natural language interface and connect to other APIs,
[823.46 --> 824.92]  other services, and other information.
[825.12 --> 830.36]  And so this is where we see some of the most powerful applications of this with tools like
[830.36 --> 835.30]  HuggingGPT, which allow you to interconnect with lots of different hugging face models where
[835.30 --> 841.12]  I can ask it a question and give it a picture and the model will automatically go out, figure out
[841.12 --> 845.90]  the appropriate hugging face models to use, run them, figure out the answer and bring
[845.90 --> 846.66]  that back to me.
[846.88 --> 852.80]  Or, and this repo has been going crazy as the auto GPT one where we essentially take that.
[852.90 --> 854.00]  It's not just for models.
[854.40 --> 859.42]  We allow the large language model to do any task where we can say, hey, start up a business
[859.42 --> 860.62]  and raise some money for me.
[861.18 --> 865.82]  And then the model will go out, answer that, go see, hey, is there some other databases?
[865.96 --> 867.68]  Is there some other APIs I can use it?
[867.68 --> 869.30]  And we'll continue to iterate.
[869.54 --> 873.88]  It might cost you a lot on the tokens for GPT-4, but it'll continue to iterate and try
[873.88 --> 874.98]  and try and try and do it.
[875.34 --> 879.50]  And I think, you know, for me, if you asked me a year ago if this was possible, I would
[879.50 --> 880.28]  have said, no way.
[880.36 --> 881.60]  That's three or four years out.
[881.72 --> 883.34]  Like, I can kind of see how you're doing it.
[883.40 --> 886.36]  But to me, this is why it's such a special moment.
[886.50 --> 890.00]  We're living in it because I don't think any of us could have predicted we'd be here,
[890.10 --> 891.24]  you know, a year ago.
[891.48 --> 895.88]  Even in our conversation so far, like we've listed out like a bunch of models.
[895.88 --> 905.08]  So GPT is an auto GPT and hugging GPT and like Bloom, Flan, Flamingo, 7 billion, whatever.
[905.70 --> 911.68]  In terms of large language models and what's out there right now, one interesting thing
[911.68 --> 916.48]  is like open access or various patterns around that and hosting.
[916.66 --> 921.30]  Like how how do you think about like the landscape of large language models?
[921.36 --> 922.86]  Like what does that look like right now?
[922.86 --> 928.56]  What are the major categories that we could kind of have in our mind as clusters of these
[928.56 --> 928.94]  things?
[929.56 --> 933.14]  At this point, there's tens of kind of large language models.
[933.40 --> 937.08]  And yeah, there's a number of different ways we can kind of categorize your thinking about
[937.08 --> 937.28]  them.
[937.66 --> 943.12]  One of them is kind of the simplest, which ones are proprietary, which ones are open source?
[943.56 --> 946.68]  There's a spectrum when we talk about access to these.
[946.68 --> 951.52]  So there's some like, for example, open AI, where you don't have access to the model.
[951.78 --> 954.22]  You don't know what data it was trained on.
[954.38 --> 956.86]  You don't know the model architecture, right?
[956.88 --> 958.68]  You just send your data to them.
[958.90 --> 960.00]  They send back the predictions.
[960.52 --> 962.18]  And so I think that's one model there.
[962.34 --> 967.76]  And then all the way at the other extreme today, for example, Databricks released the latest
[967.76 --> 973.62]  version of its Dolly model, which was an open source model that was then instruction
[973.62 --> 977.92]  tuned on a data set that Databricks created themselves, that they're making available kind
[977.92 --> 980.84]  of open source for commercial use itself there.
[981.16 --> 982.80]  So there's the whole spectrum there.
[982.90 --> 988.48]  But there's other spectrums here, too, because the models, for example, vary in size, where
[988.48 --> 992.66]  you have, for example, something like Bloom that was developed by Hugging Face, which is
[992.66 --> 997.96]  one of the largest open source models at something like 170 billion parameters, to some of these
[997.96 --> 1002.40]  much smaller models that are coming out, the Lama models and others that are maybe a billion
[1002.40 --> 1008.36]  parameters. And that size has implications in terms of how much reasoning ability, how
[1008.36 --> 1010.06]  much stuff is inside there.
[1010.32 --> 1014.14]  But inference, is this something that your teenager is going to run on their own GPU?
[1014.40 --> 1018.98]  Or is this something that's going to take a multi-GPU cluster to be able to effectively
[1018.98 --> 1019.44]  use?
[1020.08 --> 1023.20]  There's other dimensions, like what data the models were trained on.
[1023.40 --> 1027.26]  For example, with the open source models, we know what data they were trained on.
[1027.66 --> 1032.08]  One piece of this, for example, that's come up is knowing how much code a model was trained
[1032.08 --> 1037.82]  on. Because one of the things that's often asked for is, hey, can we build a text to code
[1037.82 --> 1043.94]  type model where I want to do some type of autocomplete, some type of code generation type project?
[1044.26 --> 1049.34]  Well, if I start with a large language model that already understands code, it's a lot easier
[1049.34 --> 1051.36]  to fine tune it and make that capability.
[1051.82 --> 1055.42]  So like understanding the underlying characteristics of that data.
[1055.78 --> 1056.38]  Daniel, right?
[1056.38 --> 1058.70]  It's like an alphabet soup of different names.
[1058.82 --> 1061.14]  And like literally every week they're popping up.
[1061.22 --> 1066.50]  And there's so many of these different characteristics because they also differ, for example, on the
[1066.50 --> 1071.54]  model itself and what the licensing is and the model weights, the data set that it was trained,
[1071.76 --> 1073.74]  the training code that it was done.
[1074.02 --> 1079.18]  We see this with kind of how Meta released the Lama model where they told everybody about
[1079.18 --> 1080.60]  it, but then they released the weights.
[1080.60 --> 1082.26]  But then they gated the weights.
[1082.40 --> 1084.78]  So only academic people were getting to them.
[1084.90 --> 1088.18]  But then the weights were essentially leaked and now they're all over the Internet.
[1088.30 --> 1089.90]  So now everybody's using them.
[1089.98 --> 1095.76]  So it becomes very confusing kind of in this big, thick mix of, you know, how to sort this
[1095.76 --> 1095.96]  out.
[1096.60 --> 1102.42]  So you're an organization out in the world today and you're trying to make sense of all
[1102.42 --> 1102.86]  of this.
[1102.86 --> 1109.50]  And if you just look at your last answer alone, it's just like overwhelming for most organizations
[1109.50 --> 1110.34]  to look at.
[1110.46 --> 1112.08]  There's all these different characteristics.
[1112.34 --> 1115.70]  There's big models, small models, open source, closed source, you name it.
[1115.76 --> 1117.76]  There's you can slice it so many different ways.
[1118.18 --> 1119.94]  How do you make sense of that?
[1120.00 --> 1125.40]  If you are, let's say that you're in management at an organization, not necessarily the data
[1125.40 --> 1130.38]  scientist who's 25 and gets the data side, but you're trying to figure out how do I do
[1130.38 --> 1134.62]  this in the larger sense, how do you start making sense of that?
[1134.88 --> 1138.62]  How do you know if you need your own model that you're going to create, if you're going
[1138.62 --> 1144.38]  to go use somebody else's big, small, what's a good starting point for people to start sorting
[1144.38 --> 1147.58]  through the mess that we're all delighting in today?
[1147.82 --> 1148.88]  And it is a mess.
[1148.98 --> 1153.20]  And I get calls all the time from model governance folks that are trying to like, we need to set
[1153.20 --> 1154.44]  out a blueprint for our company.
[1154.86 --> 1160.18]  We need to think through this because right now, the incredible change of the pace of change
[1160.18 --> 1160.94]  and all of that, right?
[1161.24 --> 1162.44]  That's the downside of that.
[1162.54 --> 1166.10]  Like if you're trying to understand what's going on, it's really hard to.
[1166.26 --> 1171.12]  And I think a lot of organizations at this point, there's not a lot of easy cases for
[1171.12 --> 1175.94]  like, let's implement this because it's going to 10X our revenue for this particular thing.
[1175.94 --> 1180.34]  I think there is a lot of breathing room in terms of enterprises and being able to figure
[1180.34 --> 1185.34]  out what the best strategy is for the models over the next year or so like that.
[1185.34 --> 1191.80]  I personally really benefited from hugging face tooling around this.
[1191.98 --> 1196.98]  So like some of the decisions that I've made in terms of my own integrations into the applications
[1196.98 --> 1203.52]  that I'm building are because I know there's a community around some of these sets of tools.
[1204.14 --> 1207.88]  There's sort of interoperability if I want to pull in like this model size or that model
[1207.88 --> 1209.50]  size or like whatever it is.
[1209.50 --> 1214.92]  And even like these large models, like you mentioned Bloom, there's so much integrated
[1214.92 --> 1223.28]  tooling with I remember a really awesome blog post about like running Bloom in Colab using
[1223.28 --> 1228.06]  accelerator bits and bytes and these things for like quantization and all this.
[1228.58 --> 1233.84]  And all of that set of tooling from this like hugging face ecosystem, I think is so powerful
[1233.84 --> 1236.38]  for people actually practically trying to do this.
[1236.38 --> 1242.02]  I'm wondering, like there's so many cool tools coming out as well, like in that ecosystem.
[1242.64 --> 1248.22]  You're, of course, at the center of it, you know, being part of that community and that
[1248.22 --> 1248.64]  company.
[1248.80 --> 1250.64]  Any highlights that you'd like to highlight?
[1250.76 --> 1254.92]  Like I highlighted the one which was is really cool and I'm playing with.
[1255.02 --> 1256.40]  But what else should be on our radar?
[1256.90 --> 1257.22]  That's great.
[1257.28 --> 1261.68]  And I know both of you kind of enjoy the hugging face ecosystem and have spoken highly of it
[1261.68 --> 1262.02]  before.
[1262.02 --> 1267.16]  And the hugging face ecosystem is all about just helping to kind of create and democratize
[1267.16 --> 1270.42]  machine learning, build out the open source for it.
[1270.56 --> 1275.24]  To Chris's earlier point, we have a place where everybody can go and check the models and read
[1275.24 --> 1277.06]  what is the licensing for the model?
[1277.22 --> 1280.10]  You know, what are the implications for that and learn about that?
[1280.50 --> 1284.68]  Now, when it comes to these large language models, like we've been busy building out pieces
[1284.68 --> 1285.66]  on that.
[1285.66 --> 1290.48]  So if you think about kind of training these large language models, Nathan on our team has
[1290.48 --> 1294.62]  written some blog posts around using techniques like reinforcement learning with human feedback.
[1295.00 --> 1299.54]  That's the latest cutting edge approaches to figuring out like how to get these models
[1299.54 --> 1302.10]  to align exactly with what humans do.
[1302.16 --> 1306.38]  Because yes, we can feed a bunch of data into the models, but what comes out of them often
[1306.38 --> 1309.00]  isn't what you and I would think is the best.
[1309.00 --> 1312.90]  And so this using reinforcement learning with human feedback does that.
[1313.32 --> 1318.36]  I think one of the things I'm excited about is the PEFT library that we have, which is
[1318.36 --> 1320.20]  parameter efficient fine tuning.
[1320.48 --> 1322.74]  And if you look at these models, they're huge.
[1322.92 --> 1324.74]  They take a ton of resources to do.
[1325.22 --> 1327.42]  PEFT has a number of different approaches in there.
[1327.66 --> 1333.74]  How can we fine tune these models without having to load the entire model and modify every
[1333.74 --> 1334.54]  weight in this?
[1334.54 --> 1336.76]  And there's a number of different techniques.
[1336.86 --> 1342.54]  For example, just, hey, can we take the entire model weights and find a smaller structure
[1342.54 --> 1343.22]  inside them?
[1343.30 --> 1344.98]  Like a low rank approximation.
[1345.22 --> 1346.32]  I can't think of that name.
[1346.70 --> 1351.82]  Can we get then that little dense piece and just train that part and add that onto it?
[1352.02 --> 1356.98]  And if we do that, that actually works as a fine tuning technique without having to train
[1356.98 --> 1358.20]  the entire model.
[1358.48 --> 1363.02]  So I think this is where the Hugging Face team is busy building out a lot of infrastructure and
[1363.02 --> 1366.60]  tooling so we can kind of all effectively use these large language models.
[1367.12 --> 1370.60]  It reminds me that tooling is tactical in terms of solving problems.
[1371.08 --> 1374.10]  And for Daniel and me, given the podcast name, tactical is practical.
[1375.14 --> 1377.04]  Wow, that's good.
[1377.40 --> 1380.46]  Maybe we should redo our tagline there, Chris.
[1380.80 --> 1384.40]  I'd have to run it through chat GPT first to make sure it was good.
[1384.40 --> 1391.26]  We always talk or we've talked many times on the podcast about how a lot of times the practical
[1391.26 --> 1397.84]  side of AI is on the inference side, not as much on the training side potentially, because
[1397.84 --> 1402.88]  like 99% of what you're going to run your model in production is inference.
[1403.28 --> 1409.82]  I'm wondering, like with these large language models, I can see like various scenarios happening,
[1409.82 --> 1410.26]  right?
[1410.30 --> 1414.82]  A lot of people are just putting that thin UI on top of open AI and like they're never
[1414.82 --> 1417.58]  training anything and they're using that in context learning.
[1417.98 --> 1423.90]  But now with the tooling that you just talked about, there's sort of this ability to fine
[1423.90 --> 1430.22]  tune these large models in a way that like wouldn't require you to have, you know, a bunch
[1430.22 --> 1432.04]  of racks of GPUs, right?
[1432.06 --> 1437.28]  But maybe you could even do it in like some hosted system like a collab or something like
[1437.28 --> 1437.82]  that, right?
[1437.82 --> 1444.18]  So how do you think that shifts people's kind of approach to how they're solving problems
[1444.18 --> 1446.22]  over the long run?
[1446.32 --> 1450.58]  Because it was sort of like for a while, everybody's training their scikit learn model, right?
[1450.62 --> 1454.68]  And then it seemed like for a while, okay, now I'm just going to use APIs because I can't
[1454.68 --> 1455.50]  train these models.
[1455.68 --> 1460.36]  And now we're kind of coming back to this, okay, well, what about fine tuning, parameter
[1460.36 --> 1462.76]  efficient, like we're not loading the whole model in.
[1463.04 --> 1464.88]  How do you think that changes things moving forward?
[1464.88 --> 1494.88] 
[1494.88 --> 1497.64]  And then we're going to be talking about how much energy is in this development of open
[1497.64 --> 1498.74]  source large language models.
[1498.74 --> 1503.58]  But I mean, what's blown me away in the last few months is just how widespread this community
[1503.58 --> 1503.98]  is.
[1504.24 --> 1509.74]  Because I think, you know, some of the developments you've seen are around C++ interfaces for large
[1509.74 --> 1510.74]  language models, right?
[1510.74 --> 1515.24]  Things that no data scientist I know would be able to develop something like that.
[1515.24 --> 1519.28]  But because there was so much excitement, we got other folks, right, typical software
[1519.28 --> 1521.66]  developers engaged in building tools.
[1521.92 --> 1526.58]  And I think there's a lot of focus right now on building these types of tools for this
[1526.58 --> 1531.82]  efficient type of use of large language models, because nobody wants to have a cluster of GPUs
[1531.82 --> 1532.24]  like that.
[1532.58 --> 1537.96]  Microsoft, in fact, just today released their deep speed chat tooling to help people train
[1537.96 --> 1540.50]  models using less infrastructure, right?
[1540.54 --> 1541.64]  Being able to do it faster.
[1541.64 --> 1545.56]  So I think there's going to be tremendous development of tools, because at the end of
[1545.56 --> 1549.42]  the day, most people would like to have a model that they can fit inside their computer
[1549.42 --> 1553.60]  or a couple of GPUs, something that doesn't take a lot that they can control, that they
[1553.60 --> 1554.06]  can tune.
[1554.38 --> 1558.82]  And so I think we'll see a lot of development in progress in terms of open source pieces
[1558.82 --> 1559.44]  for that.
[1560.14 --> 1567.42]  Well, Raj, I am curious to know how many of your conversations these days around AI models
[1567.42 --> 1572.78]  and large language models are about like, some of that tooling and practical stuff that we
[1572.78 --> 1578.62]  just talked about, and how many are around sort of like ethical concerns or hallucinations
[1578.62 --> 1580.34]  or environmental concerns.
[1580.76 --> 1582.80]  What does that look like in your life right now?
[1583.62 --> 1585.52]  So that's, of course, is a huge part.
[1585.56 --> 1588.74]  Because again, this is like the difference between traditional machine learning, where we
[1588.74 --> 1591.38]  often thought about bias in models, right?
[1591.40 --> 1595.68]  Like, is your model going to work for kind of a young generation versus an older generation
[1595.68 --> 1596.48]  like that.
[1596.58 --> 1600.86]  But now with large language models and the ability of generative models, right?
[1600.90 --> 1603.54]  They're creating information, like how accurate it is.
[1604.04 --> 1608.18]  One of the common fallacies we see, and hopefully most of the listeners here are quite aware
[1608.18 --> 1609.66]  of that, that these models lie.
[1609.94 --> 1611.50]  They're just going to create output.
[1611.60 --> 1616.84]  And the output doesn't necessarily have necessarily a tie to reality with that.
[1616.84 --> 1621.32]  So this is one of the biggest education pieces that we have to do is because people see
[1621.32 --> 1624.88]  open AI, they see the other tools, and they're used to just typing in a question
[1624.88 --> 1626.36]  and getting back an answer.
[1626.84 --> 1632.18]  But to really use this in, let's say, an enterprise setting, I always suggest to people to pair
[1632.18 --> 1634.40]  this with traditional information retrieval techniques.
[1634.64 --> 1637.76]  Like, we already know good ways of having to search and pull information.
[1638.26 --> 1641.20]  Let's use those ways that are factually based.
[1641.68 --> 1647.04]  And then we can still layer on top a large language model to give you that nice chatty type
[1647.04 --> 1647.70]  interface, right?
[1647.80 --> 1652.04]  The large language models are great at writing like that and take advantage of both.
[1652.04 --> 1656.88]  But yeah, there's a tremendous amount of education that has to be done around, for example,
[1657.04 --> 1657.70]  hallucinations.
[1658.18 --> 1659.28]  That's just the tip of it.
[1659.38 --> 1662.78]  There's also, what's the training data that was used for these models?
[1663.30 --> 1664.68]  Where did that come from?
[1665.04 --> 1669.26]  And then once you use these models and you get output from these models, and this is
[1669.26 --> 1673.58]  where customers, especially for some of the code generation ones and image generations
[1673.58 --> 1677.88]  are worried about is they're worried about their own legal consequences of using these
[1677.88 --> 1682.22]  models that that might have some type of, you know, leakage from the training data and
[1682.22 --> 1684.88]  copywritten material that could be in the outputs.
[1685.04 --> 1686.72]  It's a lot of different issues going on.
[1687.10 --> 1692.22]  I've had conversations with people in various companies over things like the OpenAI licensing
[1692.22 --> 1694.30]  model since they're using ChatGPT.
[1694.48 --> 1699.56]  And it's really made people aware that you can be giving over IP for using.
[1699.64 --> 1702.28]  And that's just one of many possible concerns.
[1702.28 --> 1706.20]  I want to throw something, and I know you've been asked this a whole bunch of times because
[1706.20 --> 1707.48]  it's a really big topic.
[1707.60 --> 1708.84]  I'd love to hear your take on it.
[1709.26 --> 1712.46]  Given where we're at right now with large language models and some of the variants that
[1712.46 --> 1716.48]  we've talked about here, where does this sit in the concept of education?
[1717.04 --> 1722.16]  You have the gamut being run from you're not allowed to use any of these models for your
[1722.16 --> 1722.78]  coursework.
[1722.86 --> 1726.12]  And then on the other side, and I think I may have mentioned this to Daniel a few weeks
[1726.12 --> 1731.12]  ago, I have a 10-year-old daughter, actually 11-year-old in fifth grade.
[1731.12 --> 1736.58]  And she had an assignment, and I actually started us off going and doing some stuff in ChatGPT.
[1737.02 --> 1740.30]  Ended up having her do her own work, but I actually incorporated it in.
[1740.90 --> 1745.90]  But I've also talked to people who are deathly afraid of it skewing academia and how you're
[1745.90 --> 1747.14]  measuring students' progress.
[1747.60 --> 1753.02]  What might be a reasonable path forward in terms of trying to integrate this new technology
[1753.02 --> 1753.82]  into schooling?
[1754.20 --> 1757.30]  I'm very pragmatic and know that we just have to kind of accept it and adopt it.
[1757.60 --> 1757.90]  Me too.
[1757.90 --> 1762.28]  Now, I agree that there's going to be short-term issues to figure out who has access to the
[1762.28 --> 1763.72]  technology, making sure everybody, right?
[1763.76 --> 1767.58]  Because this is an easy way for people who have access to those resources versus don't
[1767.58 --> 1772.78]  to further differentiate themselves and kind of even increase the differences between groups
[1772.78 --> 1774.30]  even more like that.
[1774.84 --> 1776.34]  But I'm very pragmatic like this.
[1776.40 --> 1777.94]  Like, I think it's a very helpful tool.
[1778.04 --> 1778.64]  It's very useful.
[1778.64 --> 1781.10]  And it's going to be a part of how we work.
[1781.32 --> 1784.88]  It's not only on the education of, like, students in terms of young people.
[1784.88 --> 1789.44]  I also think we also need to get our coworkers on board, too, because I think a lot of us
[1789.44 --> 1792.56]  probably listeners are early adopters that like playing with this.
[1792.94 --> 1796.68]  But I spent time teaching my sales team how to use the tools.
[1796.82 --> 1798.24]  Like, Claude is built into Slack.
[1798.56 --> 1800.80]  I'm like, hey, look what you can do with this.
[1800.84 --> 1803.88]  Because I think it's one of those things that can enable a lot of people.
[1804.06 --> 1807.94]  But it takes a little bit of education, a little bit of pushing to get people who aren't
[1807.94 --> 1809.80]  kind of used to these tools adopted.
[1809.80 --> 1813.98]  And especially not only with the good that can come, but also, like we talked about earlier,
[1814.06 --> 1814.80]  the hallucinations.
[1815.14 --> 1817.48]  And so that they properly kind of use these tools as well.
[1818.36 --> 1824.36]  Also, I think it's the web developer, other developer community that's starting to enter
[1824.36 --> 1828.98]  this space like you were talking about, like with the C++ stuff or other things.
[1829.24 --> 1831.72]  There's other people contributing, which I think is great.
[1831.94 --> 1836.90]  You have a wider set of views being brought to the table around how these things should
[1836.90 --> 1838.58]  behave, how we should use them.
[1838.58 --> 1841.08]  There's a lot more people at the table.
[1841.46 --> 1847.64]  And I know one of the things I've seen, of course, a ton of that startup energy to people
[1847.64 --> 1849.70]  building things on top of this.
[1850.02 --> 1855.02]  Some very quickly, like I say, that's just a thin landing page on top of OpenAI.
[1855.20 --> 1860.76]  But others that are really fascinating and interesting use cases for this technology.
[1861.56 --> 1867.38]  Of course, a lot of that community as well overlaps with the community using hugging face tooling
[1867.38 --> 1870.50]  and those you're hugging faces interacting with.
[1870.50 --> 1873.96]  What is it like for you to see that energy around startups?
[1874.22 --> 1876.60]  And there's so many things coming out.
[1876.72 --> 1880.66]  I know startups are already like low percentage chance of success.
[1880.82 --> 1884.82]  But a lot of these things are really amazing and I think could reshape like how we work,
[1884.88 --> 1887.64]  how we learn, like you're talking about, Chris, and other things.
[1887.80 --> 1890.04]  So what are you thinking around that front?
[1890.04 --> 1895.04]  And like also having a sort of front row seat to see a lot of these things like being released.
[1895.62 --> 1896.78]  It's an amazing time like that.
[1896.82 --> 1900.82]  And I love seeing the startups because people are experimenting, trying new ideas, trying
[1900.82 --> 1901.50]  new things, right?
[1901.54 --> 1903.44]  Like most of them will undoubtedly fail.
[1903.64 --> 1907.32]  But I think in the meantime, we're going to get a lot of good ideas for different ways
[1907.32 --> 1910.16]  and approaches that we can kind of use these tools.
[1910.16 --> 1913.38]  And that right there has me very excited about that.
[1913.96 --> 1918.56]  You know, one of the things that I've been really having some interesting conversations
[1918.56 --> 1922.20]  is about people who are not us, not in our audience.
[1922.68 --> 1928.60]  People who are in the larger world and really, you know, may have loosely followed, you know,
[1928.64 --> 1932.16]  kind of what's happening in the AI space and kind of in the mainstream media.
[1932.54 --> 1937.28]  But they're struggling to really understand what's happening right now.
[1937.28 --> 1940.68]  And, you know, we kind of started the show off on that whole premise is that there's
[1940.68 --> 1945.80]  so much happening right now to the point of I was at a dinner function recently.
[1946.00 --> 1947.52]  It was just a couple of weeks ago.
[1947.52 --> 1954.66]  And I met this really cool dude who was in his mid 80s, but really sharp, followed technology.
[1954.84 --> 1956.70]  And we started talking about AI.
[1956.98 --> 1959.62]  And he's just like, I'm trying to track it and understand.
[1959.62 --> 1965.72]  And one of the points I turned to him with the idea that we're having these large language
[1965.72 --> 1970.50]  models that are now penetrating into everyone's consciousness, I said, this is that moment
[1970.50 --> 1976.02]  where you're going to look back and realize this was where you were conscious of AI being
[1976.02 --> 1976.84]  a part of your life.
[1976.86 --> 1979.30]  And it will take off from this point forward.
[1979.44 --> 1985.26]  When you're talking to people about these issues, how do you adjust people who are not
[1985.26 --> 1986.72]  used to this stuff the way we are?
[1986.72 --> 1991.88]  How do you get them into the right way of thinking about it in a productive way and kind
[1991.88 --> 1992.98]  of onboard them?
[1992.98 --> 1997.20]  Because it's not the same conversation today as it was a year ago, as you said.
[1997.52 --> 1998.44]  It's changed.
[1998.56 --> 2000.96]  So how do you approach tackling that?
[2001.24 --> 2006.30]  I think one of the easier ways is if I can get them to use the technology, if they can
[2006.30 --> 2011.68]  use an image generation where they can type in something and see the differences in results
[2011.68 --> 2016.26]  that might get or use a chat GPT where I can kind of coach them and do that.
[2016.32 --> 2021.66]  Because you're right, like trying to explain exactly what this does without the context of
[2021.66 --> 2026.00]  actually using it, it's like telling somebody about something in the future that it's hard
[2026.00 --> 2028.26]  to kind of contextualize and understand what's going on.
[2028.50 --> 2031.94]  The easiest answer for me is just like getting them using it a little bit.
[2032.04 --> 2035.90]  And then that helps to then showing them then like, what are the boundaries?
[2036.04 --> 2036.88]  What are the limitations?
[2036.88 --> 2038.06]  Like, what can we do?
[2038.32 --> 2039.42]  What are the possibilities?
[2039.42 --> 2041.62]  Once they have a grounding on that.
[2041.62 --> 2047.02]  As kind of a follow-on to that, we've kind of acknowledged we're in this sort of historical
[2047.02 --> 2047.56]  moment.
[2047.88 --> 2052.78]  And in years past on the show and last time you came on stuff, we might have talked about
[2052.78 --> 2055.02]  kind of historical moments in the context of AI.
[2055.20 --> 2060.14]  But I think we're all agreeing that it's becoming a historical moment for the whole world, whether
[2060.14 --> 2063.82]  you're in AI or outside of AI, because it's impacting everybody.
[2064.08 --> 2068.40]  You also acknowledged along the way that there are kind of ebbs and flows, you know, that we have.
[2068.40 --> 2072.60]  We're certainly at one of those moments of just intense new stuff coming out.
[2073.20 --> 2075.74]  What do you see in the future, both short-term and long-term?
[2075.92 --> 2077.56]  Where do you think we're going from here?
[2077.60 --> 2082.28]  Because it feels like we're in an Alice through the looking glass kind of moment.
[2082.62 --> 2084.90]  So what might the future look like?
[2084.90 --> 2086.94]  And what are you guys anticipating at Hugging Face?
[2087.38 --> 2088.30]  So I agree, right?
[2088.34 --> 2090.06]  This is just an amazing moment.
[2090.14 --> 2095.12]  And I think it's more so for the people that are in it that understand AI and what's going
[2095.12 --> 2099.86]  on and kind of where the steps we've made over the last year, you know, and where we
[2099.86 --> 2100.80]  can go going forward.
[2101.14 --> 2105.94]  I still think we still have to figure out when we're talking about kind of larger humanity
[2105.94 --> 2111.22]  and the larger group of people, exactly what is the impact and how we're going to use this.
[2111.22 --> 2115.44]  Because yes, we have chatbots, but most of us didn't spend a lot of our life before using
[2115.44 --> 2116.22]  chatbots, right?
[2116.24 --> 2119.58]  Like I don't know how much of our lives, you know, going forward, we'll have to do that.
[2119.58 --> 2121.96]  So we'll have to see how that's integrated.
[2122.12 --> 2127.72]  But I think, you know, all of this just shows us that the idea of AI, the idea of having
[2127.72 --> 2133.96]  using machines to help us make better decisions is something that is becoming much more widespread.
[2134.58 --> 2139.74]  We're really kind of on a path with Hugging Face to help democratize that, bring that barrier
[2139.74 --> 2141.46]  down, allow more people.
[2141.64 --> 2145.42]  So not just the people who have been trained for four years in statistics and went and got
[2145.42 --> 2151.12]  a PhD, but somebody that can think through a problem a little bit, go interface back
[2151.12 --> 2156.20]  and forth with a computer, can all of a sudden build code or solve a problem by tying some
[2156.20 --> 2161.38]  prompts together and really allowing lots more people to harness the collective AI, the
[2161.38 --> 2165.72]  collective information that we have and allow for more productive uses like that.
[2166.32 --> 2166.64]  Gotcha.
[2166.78 --> 2167.42]  Good answer.
[2167.66 --> 2171.48]  As you know, Daniel and I have been longtime fanboys of Hugging Face.
[2171.94 --> 2174.66]  We think it's a fantastic community, amazing tooling.
[2174.66 --> 2180.56]  So as we close out, you want to point some folks to maybe a few things that Hugging Face
[2180.56 --> 2184.26]  has to offer that might be good ways of ramping up in different areas.
[2184.44 --> 2185.60]  Just kind of call them out.
[2186.14 --> 2186.52]  Absolutely.
[2186.78 --> 2190.06]  So the Hugging Face website is a great place to start.
[2190.16 --> 2195.00]  There's a free online course that you can start with using Transformers there.
[2195.20 --> 2198.26]  There's forums, there's Discord, there's a community there.
[2198.48 --> 2202.10]  Feel free to kind of jump in and kind of get engaged there.
[2202.10 --> 2204.08]  And then we're building out lots of pieces.
[2204.08 --> 2208.18]  You'll see more models coming up over the next few months that we're going to be releasing
[2208.18 --> 2210.20]  more tooling for working with this.
[2210.30 --> 2211.96]  So yeah, there's a lot going on.
[2212.92 --> 2213.40]  Fantastic.
[2213.64 --> 2216.42]  Well, thank you very much for coming back on the show.
[2216.62 --> 2217.84]  You're always exciting.
[2217.98 --> 2222.24]  You're fantastic at representing Hugging Face and sharing your perspective with everyone.
[2222.50 --> 2224.84]  And we'll have to do it again sometime soon.
[2224.92 --> 2225.52]  Thanks a lot, man.
[2225.76 --> 2226.20]  Absolutely.
[2226.20 --> 2227.20]  Thank you for having me.
[2227.32 --> 2227.86]  I enjoy this.
[2227.86 --> 2239.42]  Thank you for listening to Practical AI.
[2239.96 --> 2243.74]  Your next step is to subscribe now, if you haven't already.
[2244.18 --> 2250.22]  And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2250.22 --> 2255.60]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2256.18 --> 2259.98]  Check out what they're up to at Fastly.com and Fly.io.
[2260.38 --> 2265.68]  And to our Beat Freakin' Residence, Breakmaster Cylinder, for continuously cranking out the best beats in the biz.
[2265.98 --> 2266.88]  That's all for now.
[2267.12 --> 2268.28]  We'll talk to you again next time.
[2268.28 --> 2281.98]  Game on.
