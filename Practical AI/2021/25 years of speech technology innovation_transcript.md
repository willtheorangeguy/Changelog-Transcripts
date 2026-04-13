[0.00 --> 3.52]  When I was at Amazon leading the Alexa team, we were doing the same.
[3.66 --> 8.34]  We had a lot of effort goes into language modeling to figure out what sequences of words
[8.34 --> 10.20]  are people likely to say to a smart speaker.
[10.20 --> 16.58]  And on the acoustic side was, I think, more challenging for Alexa because Alexa was the
[16.58 --> 22.32]  first breakthrough product that could handle speech at a distance so that it had to accommodate
[22.32 --> 25.46]  all of the reverberations and echoes in a room.
[25.46 --> 30.38]  When I talk to one of my smart speakers now, my voice is bouncing off of any number of
[30.38 --> 34.60]  walls, windows, computers, whatever, before it gets to that smart speaker.
[35.04 --> 37.70]  And that can be really confounding for the speaker.
[37.84 --> 42.44]  And the acoustic modeling had to do some major growing up to be able to handle that.
[45.28 --> 47.96]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[48.18 --> 48.90]  We love Linode.
[48.96 --> 50.38]  They keep it fast and simple.
[50.52 --> 52.88]  Check them out at linode.com slash changelog.
[52.88 --> 55.18]  Our bandwidth is provided by Fastly.
[55.46 --> 59.08]  Learn more at Fastly.com and get your feature flags powered by LaunchDarkly.
[59.34 --> 61.06]  Get a demo at LaunchDarkly.com.
[64.12 --> 66.54]  This episode is brought to you by our friends at O'Reilly.
[66.92 --> 70.56]  Many of you know O'Reilly for their animal tech books and their conferences, but you may
[70.56 --> 73.04]  not know they have an online learning platform as well.
[73.42 --> 77.84]  The platform has all their books, all their videos, and all their conference talks.
[78.20 --> 82.40]  Plus, you can learn by doing with live online training courses and virtual conferences,
[82.40 --> 87.92]  certification practice exams, and interactive sandboxes and scenarios to practice coding
[87.92 --> 88.98]  alongside what you're learning.
[89.22 --> 94.82]  They cover a ton of technology topics, machine learning, AI, programming languages, DevOps,
[95.32 --> 101.48]  data science, cloud, containers, security, and even soft skills like business management
[101.48 --> 102.92]  and presentation skills.
[103.04 --> 104.82]  You name it, it is all in there.
[105.16 --> 108.78]  If you need to keep your team or yourself up to speed on their tech skills, then check
[108.78 --> 110.30]  out O'Reilly's online learning platform.
[110.84 --> 114.40]  Learn more and keep your team skills sharp at O'Reilly.com slash changelog.
[114.54 --> 116.80]  Again, O'Reilly.com slash changelog.
[116.80 --> 131.36]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive,
[131.76 --> 132.70]  and accessible to everyone.
[133.10 --> 137.10]  This is where conversations around AI, machine learning, and data science happen.
[137.46 --> 141.58]  Join the community and Slack with us around various topics of the show at changelog.com
[141.58 --> 143.46]  slash community and follow us on Twitter.
[143.60 --> 145.18]  We are at Practical AI FM.
[146.80 --> 154.74]  Well, welcome to another episode of Practical AI.
[155.12 --> 156.72]  This is Daniel Whitenack.
[156.84 --> 163.06]  I am a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[163.06 --> 168.04]  Benson, who is a principal emerging technology strategist at Lockheed Martin.
[168.34 --> 169.48]  How are you doing today, Chris?
[169.78 --> 170.80]  I am doing very well.
[170.92 --> 171.96]  How's it going today, Daniel?
[172.10 --> 172.92]  It's going wonderful.
[172.92 --> 176.02]  I don't know if our listeners can't see me, but you can see me.
[176.02 --> 176.96]  I'm in a new room.
[177.12 --> 179.96]  My wife and I moved this last week, which was exciting.
[180.40 --> 183.94]  I don't know if it's this way worldwide, but for those in the U.S., you'll know that
[183.94 --> 189.24]  the housing market in May of 2021, which is now time, is crazy.
[189.46 --> 193.50]  So we sold our house and got to rent for a while, and that seemed to make sense.
[193.58 --> 195.62]  So I've got a new podcast recording room.
[195.86 --> 196.58]  That was the big news.
[196.84 --> 199.24]  It's funny that you mentioned that because I know I've mentioned to you that I'm planning
[199.24 --> 200.22]  to move as well.
[200.44 --> 200.60]  Yep.
[200.68 --> 201.96]  Very local to where we're at.
[202.14 --> 202.24]  Sure.
[202.36 --> 204.74]  But just we have some family land that has five acres.
[204.90 --> 205.00]  Yeah.
[205.10 --> 207.58]  But the price of wood is at an all-time high.
[207.78 --> 208.08]  It is.
[208.20 --> 208.34]  Yeah.
[208.44 --> 209.34]  Building is crazy.
[209.46 --> 212.28]  That has pushed the cost of building up way up there.
[212.36 --> 214.26]  So we're trying to figure out when we're going to do it.
[214.34 --> 215.50]  So nothing to do with AI.
[215.68 --> 215.90]  Yeah.
[216.04 --> 216.16]  Yeah.
[216.16 --> 218.38]  But still, you know, definitely impacting the family.
[218.84 --> 218.98]  Yeah.
[219.04 --> 224.48]  So I've been like working from various strange locations over the past week and opening up
[224.48 --> 229.00]  my computer and dealing with a bunch of data parsing issues and weirdness over the past
[229.00 --> 229.64]  few days.
[229.64 --> 236.04]  And it's been either moving a box or setting my laptop on top of a box and opening it to
[236.04 --> 237.32]  deal with data parsing issues.
[237.32 --> 240.82]  That's been like my life for the past few days, which isn't so bad.
[241.08 --> 242.16]  It's not so bad.
[242.32 --> 244.26]  You do what you got to do to make things work.
[244.42 --> 244.62]  Yeah.
[244.62 --> 246.12]  We get there.
[246.36 --> 247.14]  Yeah, for sure.
[247.34 --> 252.02]  Chris, I think I mentioned to you a few weeks ago, I think it was, I was able to be on a
[252.02 --> 254.74]  guest on a different podcast, which is always fun.
[254.84 --> 257.10]  And that was the Voice Box podcast.
[257.54 --> 264.40]  One of the hosts of that podcast is Jeff Adams, who is CEO of Cobalt Speech and Language and
[264.40 --> 267.36]  a former member of the Alexa team at Amazon.
[267.80 --> 273.42]  And Jeff has graciously responded to our request to be a guest on Practical AI.
[273.42 --> 274.38]  So welcome, Jeff.
[274.62 --> 275.64]  Hi, it's good to be here.
[275.66 --> 278.22]  And I want to state for the record, I am not selling my house.
[278.78 --> 279.68]  Okay, perfect.
[280.10 --> 280.26]  Yeah.
[281.10 --> 281.50]  Touche.
[281.66 --> 283.62]  Well, you must like where you're at right now.
[283.82 --> 284.64]  I'm just holding.
[284.84 --> 286.48]  It's like poker and real estate.
[286.66 --> 287.28]  Just hold them.
[287.40 --> 287.86]  You're holding.
[289.08 --> 289.48]  Yeah.
[289.62 --> 290.20]  Makes sense.
[290.40 --> 290.66]  Yeah.
[290.66 --> 293.28]  I'm taking the more impulsive route.
[294.58 --> 299.92]  Well, before we get into all the great speech technology things that you're involved with,
[300.00 --> 304.70]  maybe we could just start out and talk a little bit about your background and how you got into
[304.70 --> 307.98]  this sort of technology and ended up doing what you're doing now.
[307.98 --> 309.74]  You want to give us a little bit of that background?
[310.08 --> 310.26]  Sure.
[310.36 --> 314.50]  I got into speech technology a quarter of a century ago, and that's the first time I've
[314.50 --> 318.16]  ever said that because I just realized it and it makes me feel really old.
[318.16 --> 323.42]  So I've been doing speech recognition, speech technology for just over 25 years.
[323.70 --> 329.22]  I've worked for companies like Dragon, Nuance, Yap, and Amazon, you mentioned.
[329.54 --> 337.04]  And then more recently for the last six, seven years, I've been the CEO and co-founder or sorry,
[337.14 --> 341.00]  just plain outright founder of Cobalt Speech and Language Company.
[341.18 --> 346.70]  So I've been at a handful of different companies and seen a lot of things over the last 25 years.
[346.70 --> 349.44]  And I really love speech technology.
[349.82 --> 354.62]  When you were just getting into this world of speech technology, what was it that drew
[354.62 --> 357.06]  you to the technology in the first place?
[357.16 --> 357.86]  How did that happen?
[358.14 --> 364.72]  Well, I was a math grad student at the time at the University of Oregon and was deciding
[364.72 --> 368.84]  that academics was not really where I wanted to spend the rest of my life and was trying
[368.84 --> 369.76]  to figure out what to do.
[370.04 --> 376.42]  I have always been really fascinated by the interplay between mathematics, statistics,
[376.70 --> 380.94]  and language and trying to figure out what I could do with that.
[381.08 --> 383.92]  And I saw this was in, boy, I really am aging myself.
[384.04 --> 384.96]  This was in 1995.
[385.12 --> 389.28]  This was the relatively early days of the internet and the World Wide Web.
[389.54 --> 395.48]  And I went on the internet to hunt for jobs, which was not a common thing at the time.
[395.88 --> 400.48]  And I found someone looking to fill a position for statistical language modeling.
[400.48 --> 402.18]  And I said, that sounds really cool.
[402.18 --> 403.56]  Oh, that sounds cool.
[403.56 --> 409.10]  So I threw my hat in the ring and I got the job and I moved from the Pacific coast to
[409.10 --> 414.14]  the Atlantic coast and took a job with this speech company, Kurzweil Applied Intelligence.
[414.40 --> 418.04]  It was founded by Ray Kurzweil, the inventor and futurist.
[418.24 --> 418.78]  It was fun.
[418.92 --> 420.68]  It was a really cool experience.
[420.78 --> 423.38]  And that's where I got my on the job training.
[423.38 --> 429.78]  I learned a lot about speech technology and specifically how statistical language modeling
[429.78 --> 433.28]  fits into the whole process of speech recognition.
[433.68 --> 434.30]  I'm curious.
[434.48 --> 435.78]  You've talked about your resume.
[436.06 --> 440.38]  It's kind of a who's who of that industry of kind of all the big names as they've come
[440.38 --> 440.74]  along.
[440.86 --> 444.12]  When you joined Kurzweil, how big was that company?
[444.38 --> 446.82]  Had it grown yet or was it still small?
[447.10 --> 450.56]  You know, the company was, I don't know, five or 10 years old at the time.
[450.56 --> 457.06]  Uh, so it wasn't a brand new company, but it was maybe 30 people, something like that.
[457.18 --> 457.30]  Yeah.
[457.56 --> 458.12]  Quite small.
[458.32 --> 458.44]  Yeah.
[458.52 --> 459.50]  Ray Kurzweil himself.
[459.70 --> 464.76]  He had his fingers in several different companies, but he would occasionally come by and walk up
[464.76 --> 465.36]  and down the halls.
[465.58 --> 470.38]  I was very flattered that he greeted me by name without having to look at a nameplate on
[470.38 --> 472.90]  the door or anything like that, that he knew my name.
[473.00 --> 473.66]  It was exciting.
[474.06 --> 474.64]  That is cool.
[474.90 --> 477.34]  You mentioned statistical language modeling.
[477.34 --> 482.38]  Could you give us sort of sketch of maybe back at that time when you were trying to do
[482.38 --> 486.32]  some of those things, what could statistical models do?
[486.64 --> 488.84]  What were the main challenges that you were solving?
[489.04 --> 495.68]  And maybe sort of fast forward to the capabilities or the functionality that we can do in speech
[495.68 --> 496.42]  based tasks.
[496.56 --> 497.56]  How has that expanded?
[497.98 --> 500.36]  Could you give us a little bit of that sort of sketch?
[501.00 --> 505.12]  As you do that and can tie it a little bit into some of these various companies that you've
[505.12 --> 509.44]  been involved with over time, I'd also be interested in hearing the progression as you went through
[509.44 --> 510.00]  your own career.
[510.42 --> 511.32]  Yeah, absolutely.
[511.52 --> 516.10]  By the way, just to be clear, the first 10, 15 years of my career in speech were really
[516.10 --> 517.96]  focused on statistical language modeling.
[518.52 --> 524.00]  Since then, I've broadened my scope and horizons and been more involved in speech recognition
[524.00 --> 527.74]  more generally, and then more recently, speech technology more generally.
[528.06 --> 529.72]  But let me go back and answer your question.
[529.72 --> 535.92]  When I first started in 1995 doing statistical language modeling, first of all, let me just
[535.92 --> 540.26]  define what that means for some of your listeners that may not know what that is.
[540.44 --> 540.84]  That'd be great.
[541.04 --> 545.66]  Statistical language modeling, in a nutshell, you could think of it as predicting the next
[545.66 --> 546.06]  word.
[546.28 --> 550.36]  So imagine you're reading a book or a newspaper article or a magazine article, and you get to
[550.36 --> 553.82]  the end of the page, and you're in the middle of a sentence, and you're about to turn the
[553.82 --> 554.12]  page.
[554.24 --> 557.04]  Can you predict what that next word is going to be?
[557.04 --> 561.66]  And not just predicting which word it is, but of all the possible words it could be,
[561.96 --> 567.44]  give me a probability of it's, you know, there's a 3% chance that it is the word yogurt
[567.44 --> 571.46]  and a 5% chance that it's the word horse, whatever else, whatever.
[571.60 --> 576.00]  I can't imagine what sentence might lead to those high scoring probabilities.
[576.28 --> 577.14]  That's what I was thinking.
[577.64 --> 580.10]  But anyway, this is the problem of predicting the next word.
[580.10 --> 587.82]  And the state of the art at the time, in 1995, was a technique called engrams, where you would
[587.82 --> 593.82]  have counted up from a large body of text, or we call it a corpus of text, you would have
[593.82 --> 595.58]  gathered a large corpus of text.
[595.98 --> 603.54]  And at the time, a large corpus of text would have been maybe 50 million words of English.
[603.54 --> 608.94]  And of those 50 million words, you could count, well, how many times did I see the word yogurt?
[609.06 --> 610.84]  And how many times did I see the word horse?
[611.02 --> 615.86]  And more specifically, if you know the last word on the page before you turn the page,
[615.90 --> 620.64]  if you know the last word was favorite, or, you know, my favorite, or something like that,
[620.74 --> 626.40]  of all the times that you saw the word my favorite in your 50 million word corpus of speech,
[626.40 --> 630.70]  of all of those times, how many times was yogurt the next word?
[630.76 --> 632.56]  And how many times was horse the next word?
[632.76 --> 638.02]  You could then infer the probability of various words based on how many times you'd seen them
[638.02 --> 638.56]  in a corpus.
[638.70 --> 643.94]  The biggest problem in statistical language modeling, the fundamental problem, is the zero
[643.94 --> 644.42]  problem.
[644.70 --> 646.52]  There are many things that happen.
[646.86 --> 652.26]  You might see my favorite yogurt in real life, but you may never have seen that in your 50 million
[652.26 --> 652.76]  words.
[652.76 --> 656.38]  And so if you're trying to infer what's the probability of yogurt coming next, you
[656.38 --> 658.26]  might naively say, zero.
[658.48 --> 660.64]  I've never seen it before, so it can't happen.
[660.80 --> 667.18]  And the problem with statistical language modeling is figuring out how do you predict things that
[667.18 --> 670.34]  really could happen, but you've never seen them happen before.
[670.62 --> 678.10]  So over the years, statistical language modeling was dominated by this approach using n-grams.
[678.10 --> 683.86]  If you're using sequences of three words, we would call those three-grams, or if you want
[683.86 --> 685.34]  to be fancy, trigrams.
[685.34 --> 690.76]  And over the years, as computers have gotten bigger and data has become more plentiful,
[691.34 --> 693.82]  we've been able to increase n.
[694.26 --> 699.48]  Originally, we were working with bigrams and trigrams, that is sequences of two or three
[699.48 --> 699.84]  words.
[700.02 --> 705.02]  And now over the years, that's grown to trigrams and four grams and five grams.
[705.22 --> 708.34]  We give up on the Latin and the Greek prefixes at some point.
[708.54 --> 710.02]  Yeah, that gets a bit hard at some point.
[710.02 --> 710.94]  Yeah.
[711.26 --> 716.54]  And the thing that has astounded me is that over 25 years, as so many other things have
[716.54 --> 722.28]  improved and developed, it is still really hard to beat n-gram technology for modeling
[722.28 --> 723.90]  statistical language models.
[724.26 --> 730.00]  They are still the workhorse today of most speech processing systems, although they're
[730.00 --> 732.92]  trained on many more than 50 million words.
[732.92 --> 737.08]  It might be 50 billion words or even approaching trillions of words.
[737.28 --> 742.08]  And we don't just look at two or three words, but it's much more common to look at four or
[742.08 --> 746.24]  five word sequences when you're modeling those now, because you have so much more data to
[746.24 --> 747.08]  be able to do that.
[747.42 --> 750.96]  Their simplicity means that they're fast to use in practice.
[751.34 --> 753.94]  When you're trying to look up a probability, they're very fast.
[754.30 --> 755.42]  They're still the workhorses.
[755.42 --> 762.24]  There are approaches to getting more accurate statistical models at predicting that next word
[762.24 --> 763.62]  that are more accurate.
[763.78 --> 764.20]  They're better.
[764.62 --> 768.18]  But typically, they're very time consuming, and so they're hard to use in practice.
[768.36 --> 771.68]  There are approaches now with deep neural networks to model those.
[771.80 --> 775.72]  And anyway, so this is the story of, you know, the more things change, the more they stay the
[775.72 --> 779.54]  same, that a lot of things have grown more sophisticated in speech technology.
[779.80 --> 785.08]  But language modeling has just grown bigger, larger amounts of training data, larger sizes
[785.08 --> 788.86]  of how many engrams we keep around to do the modeling and so forth.
[789.12 --> 794.20]  So that's like the language modeling piece, which mostly what you've been talking about
[794.20 --> 796.88]  is sort of combinations of words or tokens.
[797.08 --> 797.18]  Right.
[797.28 --> 802.22]  At what point did you start exploring the audio side of things?
[802.22 --> 806.68]  So audio in and not knowing maybe what words are in that audio.
[806.94 --> 808.28]  When did you start exploring that?
[808.36 --> 811.50]  And how eventually does that connect to this world of language modeling?
[811.50 --> 811.82]  Yeah.
[811.82 --> 816.00]  So my first job was working for a company doing speech recognition.
[816.00 --> 822.64]  And we were doing speech recognition mostly for people dictating documents or emails on
[822.64 --> 824.34]  their laptop or on their computer.
[824.34 --> 830.26]  The standard approach then and still now to a large extent takes the statistical language
[830.26 --> 835.46]  modeling of kind of predicting what words might come next so that you know what words to kind
[835.46 --> 836.28]  of listen for.
[836.28 --> 842.16]  And then the acoustic models that are able to listen to some audio and recognize the sounds
[842.16 --> 848.72]  of the language in that audio, recognize the difference between a K sound and an A sound
[848.72 --> 852.48]  and an I sound and a whatever, the different phonemes that you might get.
[852.66 --> 857.74]  And the whole process of speech recognition was to merge those together to get sequences of
[857.74 --> 863.08]  words that A, sounded like what you're hearing, and B, are reasonable sequences of words.
[863.36 --> 864.74]  So you put those two together.
[864.74 --> 871.16]  Now, in my first dozen years of working in this field, I ran the language modeling group
[871.16 --> 875.14]  at the company where I was, eventually at Dragon and Nuance Systems.
[875.50 --> 876.88]  I ran the language modeling group.
[877.04 --> 883.10]  And we always had a friendly rivalry with the group next door that was trying to improve
[883.10 --> 887.84]  the acoustic models of recognizing what sounds those are in the audio.
[887.84 --> 893.06]  And we would have each new release of our software, like for example, Dragon, naturally speaking,
[893.44 --> 898.48]  each new release, the language model team and the acoustic model team would be fighting
[898.48 --> 902.78]  to see who could contribute the most to the accuracy improvement for the next release.
[903.22 --> 905.14]  And it was a pretty fair fight.
[905.26 --> 907.04]  Sometimes we won, sometimes they won.
[907.04 --> 913.46]  When I left Nuance and went to join this small company, Yap, in Charlotte, North Carolina,
[913.68 --> 916.44]  where our focus was on transcribing voicemails.
[916.92 --> 920.78]  When I went to Yap, I took a step up in a sense.
[921.02 --> 924.38]  And suddenly I was in charge of all of the speech recognition.
[924.38 --> 929.38]  So I had to put aside my biases, you know, rooting for the language model.
[929.38 --> 931.52]  And I had to also care about the acoustic model.
[931.78 --> 937.82]  And I was able to find some really talented people who knew about both and could push forward
[937.82 --> 938.82]  our research on that.
[938.84 --> 940.22]  And we got to be very accurate.
[940.34 --> 944.60]  I think we were the most accurate in the industry at the time at transcribing voicemails.
[944.84 --> 945.68]  And that was a lot of fun.
[945.72 --> 950.40]  But then you asked me to sort of step through the history of my career and talk about how the
[950.40 --> 953.62]  language model versus the acoustics kind of come together.
[953.62 --> 956.10]  So they came together in my career at that point.
[956.30 --> 959.88]  And then that continued when I was at Amazon leading the Alexa team.
[960.32 --> 961.28]  We were doing the same.
[961.42 --> 966.50]  We had a lot of effort goes into language modeling to figure out what sequences of words are people
[966.50 --> 967.96]  likely to say to a smart speaker.
[968.38 --> 974.90]  And on the acoustic side was, I think, more challenging for Alexa because Alexa was the first
[974.90 --> 980.44]  breakthrough product that could handle speech at a distance so that it had to accommodate
[980.44 --> 983.56]  all of the reverberations and echoes in a room.
[983.62 --> 988.48]  When I talked to one of my smart speakers now, my voice is bouncing off of any number of
[988.48 --> 992.72]  walls, windows, computers, whatever, before it gets to that smart speaker.
[993.14 --> 995.80]  And that can be really confounding for the speaker.
[995.96 --> 1000.86]  And the acoustic modeling had to do some major growing up to be able to handle that.
[1001.22 --> 1006.22]  But we still had acoustic models and language models as sort of these separate entities that
[1006.22 --> 1007.76]  were both contributing to the recognition.
[1007.76 --> 1014.66]  And when I left Amazon and founded Cobalt, I did another step up in terms of the scope that I was
[1014.66 --> 1015.18]  looking at.
[1015.50 --> 1019.90]  I was not worried just about speech recognition anymore, but now we're worried about speech
[1019.90 --> 1025.18]  synthesis, speaker verification to identify who's speaking and any other aspects of speech
[1025.18 --> 1025.72]  processing.
[1025.72 --> 1031.90]  But those core components, they've grown up, they've become more sophisticated, especially in the case
[1031.90 --> 1035.40]  of acoustic models, and they become bigger in the case of language models.
[1035.62 --> 1038.00]  I still recognize them from 25 years ago.
[1038.14 --> 1043.70]  They're still the basic components that come together in more or less the same way.
[1043.70 --> 1057.84]  This episode is brought to you by Snowplow Analytics.
[1058.38 --> 1062.16]  Snowplow is the behavioral data management platform for data teams.
[1062.54 --> 1068.32]  Maximize the value of your behavioral data using Snowplow Insights, a managed data platform
[1068.32 --> 1073.22]  that's built on leading open source tech leveraged by tens of thousands of users.
[1073.22 --> 1078.18]  capture and process high quality behavioral data from all your platforms and your products
[1078.18 --> 1080.82]  and deliver that data to your cloud destination of choice.
[1081.18 --> 1085.62]  When marketing needs to make data informed decisions, when product needs next level understanding,
[1085.90 --> 1090.68]  and when analytics needs rich and accurate data, Snowplow is a solution for data teams who
[1090.68 --> 1095.52]  want to manage the collection, processing, and warehousing of data across all their platforms
[1095.52 --> 1096.14]  and products.
[1096.46 --> 1100.56]  Get started and experience Snowplow data for yourself at SnowplowAnalytics.com.
[1100.56 --> 1103.48]  Again, SnowplowAnalytics.com.
[1118.30 --> 1124.70]  So as we've seen these technologies really get out into the marketplace and be used in a huge
[1124.70 --> 1129.28]  number of different use cases and different industries, different businesses, how are you
[1129.28 --> 1130.78]  seeing this technology?
[1131.28 --> 1135.28]  What are some of the things that you've seen it being used for that are outside?
[1135.38 --> 1140.26]  I mean, I think probably most people are familiar with things like Alexa and the like, but I've
[1140.26 --> 1145.12]  run into use cases where I've found speech technology and things that I wasn't expecting or didn't
[1145.12 --> 1146.40]  realize it had come into that.
[1146.48 --> 1150.36]  And if you could give us a little bit of insight into some of the places that you've seen it
[1150.36 --> 1154.74]  go that maybe we're not aware of and maybe that we haven't been using on a day-to-day basis.
[1154.74 --> 1155.14]  Yeah.
[1155.26 --> 1155.68]  I don't know.
[1155.90 --> 1157.54]  Chris, have you been listening to my podcast?
[1157.66 --> 1159.88]  It sounds like you're making a pitch for my podcast.
[1160.04 --> 1161.08]  I might be.
[1161.34 --> 1163.54]  I'm not supposed to admit that now.
[1163.66 --> 1167.28]  You know, you're not supposed to call me out on that, but oh my gosh.
[1167.38 --> 1167.58]  Yeah.
[1167.60 --> 1168.86]  This is the great teaser.
[1169.08 --> 1169.32]  Yeah.
[1169.52 --> 1172.14]  I set you up and you called me out on it.
[1172.14 --> 1179.16]  But in fact, I have this podcast, The Voice Box, where that's exactly what we look at is
[1179.16 --> 1182.96]  the variety of things people are doing with speech technology.
[1183.24 --> 1184.96]  And I'll give you a few examples, right?
[1185.14 --> 1189.44]  So people are using speech technology to diagnose disease.
[1189.64 --> 1194.52]  I can listen to you speak and detect, oh, I think the way you're speaking, you are depressed
[1194.52 --> 1195.62]  or you have Alzheimer's.
[1195.62 --> 1200.36]  I can even detect things like congestive heart failure and things that you wouldn't necessarily
[1200.36 --> 1202.42]  expect to be related to speech.
[1202.66 --> 1203.22]  So that's one.
[1203.54 --> 1209.50]  We've got speech in education where we're helping, not just coaching people, but in general,
[1209.58 --> 1214.04]  but coaching on like people learning a new language where we can give them feedback on
[1214.04 --> 1215.04]  how well they're speaking.
[1215.42 --> 1219.34]  We've got custom synthetic voices that people build.
[1219.62 --> 1223.96]  I'm mostly thinking of things, projects that we've taken on at Cobalt, but this is not limited
[1223.96 --> 1225.20]  to what Cobalt is doing.
[1225.20 --> 1227.14]  People are doing really interesting things.
[1227.32 --> 1232.14]  There's a great company, Vocal ID, that records people's voices.
[1232.60 --> 1236.96]  People who know that they have to have some surgery that lose their voice, they can record
[1236.96 --> 1241.24]  their voices ahead of time and then create a synthetic voice that sounds like them so
[1241.24 --> 1244.80]  that later after they've lost their voice, they can still speak with their voice.
[1244.92 --> 1245.66]  Oh, that's really cool.
[1245.82 --> 1248.28]  It's a fantastic company and a great technology.
[1248.48 --> 1250.54]  And it's almost like maintaining identity as well.
[1250.60 --> 1250.86]  Exactly.
[1251.02 --> 1253.82]  Separate from just the physicalness of the voice itself.
[1254.12 --> 1254.32]  Right.
[1254.32 --> 1259.66]  We've got people who are using voice to listen in on like pilot conversations to detect when
[1259.66 --> 1264.72]  they're fatigued, to recommend that they trade off with the co-pilot or whatever, whatever
[1264.72 --> 1266.92]  you have to do to wake someone up that's fatigued.
[1267.14 --> 1271.26]  We've got instances in education and finance and medicine.
[1271.26 --> 1281.60]  And the thing that has been the most fun for me in my career has been these last six years or so where I get to see so many different interesting applications.
[1281.60 --> 1283.38]  And I don't have to think of them all.
[1283.38 --> 1291.74]  Other people are coming to us saying, hey, I'd like to use voice for financial transactions or I'd like to use voice for whatever it is.
[1291.74 --> 1293.24]  And we get to do that.
[1293.30 --> 1295.46]  We get to work with them and build those things out.
[1295.66 --> 1300.18]  And we've got some great technology that people are using in a lot of really cool applications.
[1300.38 --> 1301.92]  It's fun to be a part of that.
[1301.92 --> 1318.18]  In terms of like the human device interaction in different industries, I think people started, of course, interacting a lot with computers via various peripherals, but eventually, you know, keyboard and mouse generally.
[1318.18 --> 1320.52]  And I think people have really got used to that.
[1320.64 --> 1323.96]  Of course, that's changed maybe a little bit with smartphones and other things.
[1324.30 --> 1341.60]  So how have you seen maybe industry wide and also anecdotally, maybe in people that you interact with in terms of how the value of a speech driven interaction might be different than just creating a text chat bot for your customer service?
[1341.60 --> 1348.20]  How have you seen that evolve as speech technology has gotten more diverse and more performant over time?
[1348.72 --> 1350.14]  Yeah, that's a great question.
[1350.38 --> 1352.96]  People usually rather communicate by speech.
[1353.20 --> 1354.06]  That's natural, right?
[1354.16 --> 1356.36]  Speech came long before written language.
[1356.50 --> 1358.84]  Yeah, we weren't born with a computer mouse in our hand.
[1359.70 --> 1360.00]  Right.
[1360.22 --> 1367.80]  So speech is part of us and it's natural and it's an easy way for us to communicate and to be communicated to, right, in both directions.
[1368.00 --> 1369.18]  And so it's really important.
[1369.18 --> 1381.96]  And I have seen over the last five years or so, I think I've seen some people push it a little too far where they think, well, what we need to do is have all interaction be through speech.
[1382.30 --> 1383.90]  But I don't think that makes sense, right?
[1383.92 --> 1386.42]  There are times where speech just doesn't work as well.
[1386.42 --> 1389.02]  If I'm like, well, I'm talking to you right here.
[1389.14 --> 1395.76]  If my wife needed to get my attention, she'd come into the room and probably write something on a piece of paper and hold it up to me, right?
[1395.76 --> 1400.20]  In that case, she wouldn't want to use, I wouldn't want her to use speech and interrupt us.
[1400.34 --> 1407.08]  And there are times it's a lot easier to scan information quickly when it's written and gestures are important.
[1407.08 --> 1413.20]  So I think the right thing to do is people have been pushing the pendulum way over towards speech.
[1413.28 --> 1414.44]  At least some people have.
[1414.88 --> 1428.30]  And I think that the pendulum is going to come back a little bit and people are going to find the right balance of speech and keyboard and mouse and monitor and gestures on a touch screen and whatever else.
[1428.42 --> 1432.36]  Gestures with a watch, like movement of your arm and things like that.
[1432.36 --> 1438.36]  And I think it's going to come back and speech is going to take its proper role, which will be prominent.
[1438.86 --> 1439.98]  I don't know, dominant.
[1440.16 --> 1440.56]  I don't know.
[1440.66 --> 1446.82]  But it'll be speech is going to certainly play a central role that has only been possible in the last five or 10 years, really.
[1447.48 --> 1457.74]  So it sounds like almost that there's a sort of shift of mindset or at least a tendency now to think of interactions more in a multimodal sense than like,
[1457.74 --> 1463.44]  I'm just going to consider text or I'm just going to consider speech or I'm just going to consider video and camera feeds.
[1463.56 --> 1467.34]  There's more of an appetite to think about interactions more holistically.
[1467.66 --> 1469.10]  Is that something you're seeing?
[1469.46 --> 1470.08]  Yeah, absolutely.
[1470.28 --> 1477.64]  I do see a shift toward multimedia interactions with computer where speech plays an important role, but it's not exclusive.
[1477.64 --> 1495.70]  And one thing I should say is, you know, we're talking here about computer human interaction predominantly, but speech technology also plays a role in human human interaction where the speech technology might just be listening in on a conversation when you're talking to someone helping you at the bank.
[1495.70 --> 1518.74]  And it might be helping the person at the bank recognize what you said or maybe giving you, you know, you're asking about you want to invest in an IRA and it will, the speech system might eavesdrop on you and pop up some helpful information to the representative at the bank so that they better know how to help you.
[1518.86 --> 1522.66]  Or it might coach them to say, you're talking too fast, slow down or whatever.
[1522.66 --> 1530.76]  So it's not just computer human interfaces, but speech technology can also be used improving human to human interactions.
[1532.24 --> 1547.72]  You raise a great point that we are multimodal ourselves and that we are not always directly multimodal, but that we have all these kind of ancillary interactions, as you pointed out within your bank example of kind of hearing the next person over having their conversation.
[1547.72 --> 1564.26]  Do you think, I mean, going forward, is that, is speech integrated into that multimodal in all of these direct and indirect ways kind of the way forward as, you know, whereas we have just kind of come through a time period where we tend to think in terms of single modes and that's now finally changing.
[1564.56 --> 1570.50]  And maybe we're getting, I dare say it, a little bit more human in the way that we're actually approaching it by pulling these together.
[1570.50 --> 1571.36]  I hope so.
[1571.94 --> 1573.58]  Yeah, that's what I hope we're doing.
[1573.74 --> 1587.56]  I hope the singularity is not of, you know, our robot overlords taking over, but rather us using all of this enhanced technology to help us deal better with each other and with the tasks that we have to do.
[1587.64 --> 1589.54]  And that that will definitely be multimodal.
[1589.60 --> 1596.38]  It can't just look at one or the other aspect of the way we communicate and interact with each other.
[1596.38 --> 1600.96]  And I like the reference back to your Kurzweil roots, you know, starting out there.
[1601.64 --> 1602.50]  Full circle.
[1602.88 --> 1618.38]  I'm curious, you've mentioned a bunch of things and how I think it's fascinating how maybe some of us don't even realize all of these different areas where speech is or could be applied in both human computer device interactions and human to human interactions.
[1618.38 --> 1627.52]  I'm wondering, I know Cobalt speech and language has just some some really great people, both developers and linguists and experts in this field.
[1627.74 --> 1641.26]  I wonder, as a group, what are some of the the major challenges or maybe open problems or issues that your your company is focused on sort of addressing in in the technology to help push it forward?
[1641.40 --> 1644.54]  What are some of those main things on on your radar as a company?
[1644.54 --> 1657.88]  So I think the biggest challenge in any application here, probably in anything having to do with AI and machine learning, but in particular speech and language is access to appropriate data.
[1658.32 --> 1661.92]  That's the thing that always holds us back or always is the obstacle.
[1662.04 --> 1666.54]  Someone says, I want to be able to detect when someone's speaking if they are inebriated.
[1667.34 --> 1668.04]  OK, fine.
[1668.08 --> 1672.76]  But now we have to go get some recordings of people who are inebriated and not and whatever.
[1672.76 --> 1678.96]  And getting access to sufficient amounts of data to be able to be accurate enough about that is always the challenge.
[1678.96 --> 1695.82]  One of the corollaries to that is that it is very challenging to bring this technology to speakers of other languages than the big ones, you know, the English and the Chinese and German and whatever.
[1695.82 --> 1703.46]  Someone is speaking some dialect that only has five million speakers, which sounds like a lot of people.
[1703.60 --> 1712.16]  But five million speakers is not yet at the point to attract the attention of the big players in the field to develop speech technology for them.
[1712.22 --> 1717.92]  But it's still five million people that are missing out on this spoken language revolution in tech.
[1717.92 --> 1722.92]  And so it's hard to get for these lesser represented languages.
[1722.92 --> 1735.36]  It's hard to get sufficient data that's labeled appropriately to be able to build the kind of technology that we already are starting to enjoy in the I don't know if we have a good word for it, but, you know, not the first word.
[1735.44 --> 1738.06]  Well, let's call it the first linguistic world or something like that.
[1738.22 --> 1738.42]  Yeah.
[1738.94 --> 1739.90]  Major languages.
[1740.12 --> 1740.32]  Yeah.
[1740.32 --> 1740.38]  Yeah.
[1740.38 --> 1751.74]  Changelog++ is the best way for you to directly support practical AI.
[1752.28 --> 1762.66]  Join today and unlock access to a private feed that makes the ads disappear, gets you closer to the metal and help sustain our production of practical AI into the future.
[1762.66 --> 1771.74]  Simply follow the Changelog++ link in your show notes or point your favorite web browser to changelog.com slash plus plus.
[1772.02 --> 1775.94]  Once again, that's changelog.com slash plus plus.
[1777.56 --> 1779.68]  Changelog++ is better.
[1779.68 --> 1807.20]  So, Jeff, you probably know you're you kind of led us into a topic that is very much a passion of mine in the organization that I'm a part of, you know, bringing the benefits of some of this technology to local language communities all around the world, which I just think is really wonderful.
[1807.20 --> 1810.88]  And I affirm that and applaud you for your efforts in that area.
[1810.88 --> 1823.24]  One of the stories that I know that you've mentioned to me and I've read a little bit up on was this project that you've done with a group of BYU students for preservation of Cambodian stories.
[1823.32 --> 1828.64]  So I was wondering if you could tell us a little bit about how that project came up and maybe what it's all about.
[1829.06 --> 1829.18]  Sure.
[1829.18 --> 1836.20]  I'm an alumnus of Brigham Young University and participating member in the Church of Jesus Christ of Latter-day Saints.
[1836.54 --> 1842.42]  And in our local congregation here in Massachusetts, where I live, we have a large number of Cambodian speakers.
[1842.90 --> 1846.52]  And over the years, I've had a lot of opportunity to work with them, get to know them.
[1846.78 --> 1851.72]  I've learned a few words and phrases to be able to greet them and ask them how they're doing and so forth.
[1851.90 --> 1856.04]  I've always had this affinity for Cambodian or Khmer.
[1856.22 --> 1858.14]  That's how you say Cambodian in Cambodian.
[1858.14 --> 1875.98]  So when I saw a story in an alumni newsletter that I got from BYU, that there was a group at BYU that was actively collecting recordings of personal histories of Cambodians, especially those who had been affected by the atrocities of the Khmer Rouge.
[1876.16 --> 1886.74]  That they were going out and they had collected, I think, 4,000 hours of stories and that people had then manually transcribed like 1,000 of them struck a chord with me.
[1886.74 --> 1888.64]  I thought, these are people I care about.
[1888.72 --> 1889.98]  These are people that I've worked with.
[1890.08 --> 1897.60]  And my first thought was, oh, let me make sure that my friends here in Massachusetts who were refugees might have their own stories to tell.
[1897.72 --> 1900.44]  Let me make sure that they can contribute their stories to the collection.
[1900.62 --> 1901.88]  And then I thought, well, wait a minute.
[1901.88 --> 1914.30]  We have here a situation where lesser resourced languages, where we have now thousands of hours of high quality recordings with good transcriptions for a big chunk of them.
[1914.38 --> 1918.38]  I thought, those are the ingredients that you need to develop a speech recognizer.
[1918.74 --> 1922.32]  And Cambodian doesn't have a good quality speech recognition system.
[1922.56 --> 1924.14]  So I thought we should do that.
[1924.14 --> 1931.04]  So I've asked some folks on my team here at Cobalt as a sort of a pro bono project to see what we could do on this.
[1931.10 --> 1935.38]  So we reached out to the group at BYU and they said, oh, that's a great idea.
[1935.38 --> 1940.52]  Because they could then use the speech recognition to help transcribe the rest of their audio going forward.
[1940.52 --> 1954.74]  And so BYU put up four or five students to do a lot of the labor of organizing the data and making sure that things are recorded properly and transcribed properly and ready to be processed in training the models.
[1955.06 --> 1961.24]  And we've at Cobalt had people contributing in sort of an advisory role and mentoring.
[1961.72 --> 1962.80]  So it's good all around.
[1963.04 --> 1968.26]  Students are getting an amazing opportunity of learning about how speech technology works.
[1968.46 --> 1969.72]  And we're helping them do that.
[1969.72 --> 1979.30]  Anyway, the long story short is we are close now, maybe, you know, a couple months away from having good quality Cambodian speech recognition.
[1979.62 --> 1981.18]  Assuming I'm going to knock on wood.
[1982.12 --> 1984.66]  Assuming that nothing goes wrong in the meantime.
[1985.10 --> 1988.08]  Because, you know, a lot of things have to come together just right to make it happen.
[1988.16 --> 1991.46]  But anyway, so Dan, I think that's the story you wanted me to tell.
[1991.46 --> 1998.34]  That we at Cobalt are working in conjunction with folks at Brigham Young University to develop Cambodian speech recognition.
[1998.34 --> 2002.92]  And now it's got me thinking, well, are there opportunities like that for other languages?
[2002.92 --> 2014.06]  Could we find some other partnerships where someone who wants a speech recognition for Swahili or Aymara or some other language that we can go and say, here's some audio.
[2014.34 --> 2015.58]  I don't know where we're going to get it from.
[2015.58 --> 2023.94]  And here's a partnership where we can work together to where people from the community might work with us to develop the technology.
[2024.46 --> 2032.92]  Anyway, it's a passion of mine to figure out how to bring this technology to the whole world and not just leave it in the hands where it's going to make us the most money.
[2032.92 --> 2034.32]  Yeah, that's so wonderful.
[2034.54 --> 2039.86]  And I think maybe you can read my mind a little bit at this point, because I was just thinking towards the end of your story.
[2040.04 --> 2046.64]  Hey, what learnings might you have from this initial experience that we could apply in other language communities?
[2046.64 --> 2051.14]  It sounds like there's a in this case, there was partnership, right?
[2051.18 --> 2053.36]  There was the local language community.
[2053.72 --> 2059.04]  There was the academic institution and there was an industry partner.
[2059.04 --> 2067.72]  As you look back on that, what do you think, because it sounds like you've made progress and hopefully, you know, like you say, knock on wood, things are coming out in that process.
[2067.72 --> 2077.80]  Any maybe tips or suggestions for people that are trying to maybe work on particularly like AI for good types of projects?
[2077.92 --> 2088.88]  They have a passion for that and they're trying to maybe establish a partnership that would actually result in some value and not be a sort of fun weekend hackathon project.
[2088.88 --> 2091.82]  But it would actually result in some value for the community.
[2091.98 --> 2097.84]  Any tips or thoughts or learnings that you've had over that time with that partnership that you could pass on?
[2099.62 --> 2101.08]  That's a good question.
[2101.44 --> 2109.08]  The folks at BYU that are working in this Cambodian oral history project, they had done all of their recordings and transcriptions before we came on the scene.
[2109.24 --> 2114.66]  And they didn't do it with the idea that their data was going to be used to build a speech recognizer.
[2114.66 --> 2124.84]  If they had known that going into it, they might have done a few things a little differently in the way they transcribed the audio or the way they recorded the audio or whatever.
[2124.98 --> 2127.24]  That might have made it a little bit easier for us.
[2127.44 --> 2136.48]  So a lot of the work that we're doing now is in sort of adapting our training scripts and models to the data that they've collected.
[2136.48 --> 2142.58]  I can't really say that I can't really fault them in any way because that's not the purpose that they collected the data for.
[2142.82 --> 2150.36]  Right. But if they knew that they would be doing that, it would have been nice for them to reach out ahead of time and say, hey, we're about we're about to collect all this data.
[2150.36 --> 2153.10]  And it's going to be useful for speech recognition models.
[2153.32 --> 2158.34]  Is there anything we should know in how we record it and how we transcribe it and so forth?
[2158.70 --> 2162.64]  So it's kind of a wish that doesn't really make sense in practical terms.
[2162.82 --> 2178.30]  But in general, if someone hears this and says, oh, I'm going to go start collecting data or doing some work in this area for my language, I would say, why don't you reach out first and let's get involved from the beginning rather than have to fix things after the fact.
[2178.30 --> 2190.58]  You mentioned the Khmer Rouge and just for context, for listeners who may not be familiar with it, since this data set was an oral history, I thought, you know, that was a big enough event dominated that country's history for decades.
[2190.58 --> 2193.06]  That was a decades long genocide.
[2193.68 --> 2204.72]  For those who aren't familiar, Cambodia is a very small country and it ended up, I think, decimating about 25 percent of the country, which was like one one point five to two million people died.
[2204.72 --> 2213.16]  I find as someone who also loves history in addition to technology, I just find the roots of that data set as an oral history to be pretty fascinating.
[2213.64 --> 2224.20]  And I think there's a beauty in that you are able to also extract this extra unexpected value from such a data set to be able to produce this kind of output.
[2224.20 --> 2236.20]  So sometimes when you see these two things coming together unexpected like that, and as you were talking through that and I was kind of recalling back the history that the Cambodian people suffered through, there's definitely a beauty to that as an output.
[2236.20 --> 2266.18]  So, yeah.
[2266.18 --> 2274.54]  Something like that, which it's perfectly great if technologists want to want to come in and say, you know, how can I serve a language community?
[2274.68 --> 2282.32]  But oftentimes if it's like something they don't even have a desire for, then you're probably not going to get very far.
[2282.52 --> 2294.44]  So it's cool that there can be these situations in which the community itself has a desire and that can additionally have this benefit of expanding the possibilities of technology for that community.
[2294.44 --> 2295.22]  That's really cool.
[2295.36 --> 2297.54]  So, Jeff, that's super inspiring.
[2297.92 --> 2308.94]  And I'd maybe like to move a bit to ask you about the future a bit in terms of what you're excited about exploring in speech technology, but maybe haven't yet.
[2309.06 --> 2313.74]  Sounds like you've explored most of the nooks and crannies of all over speech technology.
[2313.74 --> 2321.10]  But what are some things that maybe excite you in the future and you're hoping that Cobalt gets to explore them or that you get to explore them?
[2321.22 --> 2322.22]  You haven't quite yet.
[2322.30 --> 2325.00]  Is there anything like that that comes to mind?
[2325.26 --> 2330.48]  The list is long and we would be here for another half hour if I tried to go into it all.
[2330.72 --> 2334.88]  But I'm going to cheat a little bit and answer your question without answering it.
[2334.88 --> 2341.66]  That is the thing that keeps me going and that drives me is not knowing the answer to that question.
[2341.66 --> 2350.88]  The fact that I know that a few months from now, I'm confident that a few months from now, someone will have come to me with an idea that I had not thought of before.
[2351.02 --> 2351.70]  That's intriguing.
[2351.90 --> 2353.96]  And that I'll say, oh, yeah, that's great.
[2354.02 --> 2354.70]  Let's do that.
[2354.70 --> 2366.64]  And while there are things right now that I wish we had more time and the funding to work on, the thing that's really exciting is the things that I don't even know about yet that are coming in a few months or years or whatever.
[2367.28 --> 2367.40]  Yeah.
[2367.54 --> 2373.18]  And I guess maybe that gets to all of the information and complexity of speech and language.
[2373.50 --> 2373.68]  Yeah.
[2373.68 --> 2381.10]  Like, I don't know that I would have expected, like, oh, you could maybe detect someone having heart issues or something from their speech.
[2381.10 --> 2387.98]  That's pretty, I mean, maybe doctors, that's obvious to them, but it's not obvious to me as a, as just sort of an everyday person.
[2387.98 --> 2393.76]  So, you know, that's really a result of, hey, speech and language is really complicated.
[2394.18 --> 2398.46]  And despite our best efforts, there's still a lot of complication to explore.
[2398.74 --> 2400.16]  What do you think is driving that?
[2400.46 --> 2402.62]  That's part of it, that there's a lot to still explore.
[2402.70 --> 2405.18]  There's a lot we still don't understand about how to process it.
[2405.22 --> 2406.82]  It's a very complex process.
[2406.82 --> 2415.56]  A friend of mine said that speech and language is the most complicated process developed by the most advanced species.
[2415.88 --> 2420.82]  It's like the pinnacle of what we can try to handle and process and take care of.
[2420.94 --> 2426.48]  But it's not just that speech and language is complex, hard to understand, and hard to get right.
[2426.48 --> 2435.22]  It's also that it pervades everything so that the applications, it's hard to anticipate where those next applications are going to come from.
[2435.22 --> 2441.98]  There's so much explicit and implicit about how we think about speech and what we do with speech.
[2442.86 --> 2448.04]  And just because I know that our listeners, definitely based on what we've talked about,
[2448.12 --> 2454.52]  they're going to want to know about all of these unexpected ways that speech technology is kind of coming about.
[2454.64 --> 2458.16]  How can people find your podcast, The Voice Box?
[2458.54 --> 2460.48]  Where can they go to find it?
[2460.48 --> 2465.10]  It's on all of the major podcast platforms, so you can go find it there.
[2465.36 --> 2468.40]  I don't know if there's a better way to tell people where to find a podcast.
[2468.78 --> 2469.56]  Maybe you know that.
[2469.70 --> 2470.04]  Yeah, yeah.
[2470.04 --> 2470.94]  Maybe you know better than I do.
[2470.96 --> 2474.44]  We'll definitely link it in our show notes for sure.
[2474.66 --> 2476.88]  And I hope people find it and go check it out.
[2476.94 --> 2480.28]  And also check out some of those links that we put to what Cobalt's doing
[2480.28 --> 2484.34]  and some of the things like this project with the Cambodian audio.
[2484.34 --> 2487.32]  We'll put all of those things in our show notes, so definitely check those out.
[2487.32 --> 2490.10]  But thank you so much, Jeff, for joining us on the podcast.
[2490.22 --> 2494.12]  It was a really good time and a pleasure to talk to you as it always is.
[2494.20 --> 2497.10]  Daniel, Chris, thank you so much for your time and for having me.
[2500.74 --> 2502.76]  Thank you for listening to Practical AI.
[2503.10 --> 2505.10]  We appreciate your time and your attention.
[2505.58 --> 2509.18]  If you enjoyed this episode, help us out by spreading the word.
[2509.74 --> 2510.52]  Think of a friend.
[2510.68 --> 2511.38]  Think of a colleague.
[2511.38 --> 2514.48]  Somebody who would benefit from listening to it and send them a link.
[2514.84 --> 2515.86]  We'd really appreciate it.
[2515.86 --> 2519.54]  Practical AI is hosted by Chris Benson and Daniel Whitenack.
[2519.76 --> 2523.30]  It's produced by Jared Santo with music by Breakmaster Cylinder.
[2523.70 --> 2526.88]  Thanks again to our sponsors, Fastly, Linode, and LaunchDarkly.
[2527.06 --> 2527.84]  That's our show.
[2528.28 --> 2530.98]  We hope you enjoyed it, and we'll talk to you again next week.
[2530.98 --> 2548.20]  You'll catch the Bright S habe.
[2548.22 --> 2550.68]  www. kafel.com.
[2550.68 --> 2580.66]  Thank you.
