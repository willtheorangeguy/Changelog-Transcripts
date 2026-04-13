[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.02 --> 36.08]  Learn more at fly.io.
[42.74 --> 45.86]  Welcome to another episode of Practical AI.
[46.24 --> 47.90]  This is Daniel Whitenack.
[48.00 --> 51.28]  I'm a data scientist and founder at Prediction Guard.
[51.28 --> 56.56]  And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed
[56.56 --> 56.86]  Martin.
[57.36 --> 58.10]  How are you doing, Chris?
[58.52 --> 59.42]  I'm doing fine.
[59.52 --> 64.64]  It's another exciting day in the AI world in 2023.
[64.92 --> 67.22]  Probably the most exciting year in AI ever.
[67.86 --> 68.18]  Yes.
[68.42 --> 72.44]  And our episode today is very timely.
[72.88 --> 76.44]  It's not lately, although we are going to talk about lately.
[76.66 --> 77.90]  Oh, God.
[78.18 --> 79.48]  You actually said that.
[79.48 --> 79.84]  Ah.
[81.20 --> 83.18]  That's the best one yet, honestly.
[83.40 --> 84.48]  I've heard a lot of them.
[84.48 --> 85.18]  Okay, good.
[85.26 --> 90.50]  Well, we have with us Kate Bradley-Chernis, who's CEO at Lately.ai.
[90.74 --> 91.60]  How are you doing, Kate?
[92.14 --> 95.08]  I am now tickled, so well done.
[95.52 --> 96.50]  I'm impressed with you.
[96.54 --> 97.00]  We can be friends.
[97.00 --> 97.58]  Okay, great.
[97.70 --> 101.86]  I'm very happy about that because, yeah, you've done some amazing things.
[101.92 --> 106.50]  You're doing some amazing things at Lately and can't wait to hear more about them.
[106.50 --> 112.30]  Before we jump into more specifics about what you're working in specifically, I'm curious
[112.30 --> 118.86]  because you have had experience for a number of years working in this sort of generative
[118.86 --> 123.18]  AI space and especially on social media and content generation.
[123.18 --> 129.62]  I'm wondering what your feeling is about kind of this general moment that we're in with
[129.62 --> 132.16]  AI and like how it's shaping.
[132.36 --> 134.74]  Has it reshaped some of your thinking around AI?
[135.08 --> 141.04]  Has it proven things true that you've always thought about AI or what's on your mind right
[141.04 --> 141.30]  now?
[141.30 --> 146.82]  Yeah, I mean, it's so funny because we actually didn't even know that we had built AI back
[146.82 --> 148.50]  when we had started building it.
[148.58 --> 153.72]  A mentor had to kind of give us the clue and then they got us a grant with IBM Watson.
[153.88 --> 154.62]  This is in 2018.
[155.36 --> 160.16]  So, you know, my perspective on it has certainly changed over the years in so many ways.
[160.26 --> 165.76]  I mean, it was so hard for us to explain what we did for so long and suddenly everybody
[165.76 --> 167.02]  thinks they know what we do now.
[167.02 --> 171.26]  So they're coming to us with this like whole different perspective that we still have to
[171.26 --> 171.64]  educate.
[171.86 --> 176.66]  But what's exciting to me is there's been there's three waves we've seen already happen.
[176.66 --> 178.94]  And there's another one that I believe is about to happen.
[179.08 --> 181.80]  The first one is like, holy shit, AI, everybody, right?
[181.92 --> 182.36]  Wow.
[182.66 --> 183.46]  You know, this is amazing.
[183.56 --> 184.52]  Everyone just had a freak out.
[185.00 --> 190.40]  And then the second wave has been all around the legalities, a pullback, you know, copyright
[190.40 --> 191.24]  issues.
[191.82 --> 195.26]  You know, what are those kind of court liabilities that are going to be up and coming?
[195.26 --> 199.14]  And then the third wave is around the voicings, right?
[199.32 --> 203.64]  Like, OK, well, now that everybody has cliff notes, essentially, like, how do you make it
[203.64 --> 204.18]  your own?
[204.58 --> 208.62]  And then the fourth wave is and it's already here, really.
[208.70 --> 214.72]  We're seeing employees, again, employee job descriptions, the need for prompt experience
[214.72 --> 215.64]  and expertise.
[216.46 --> 220.86]  So and lately, by the way, has been ahead of the curve on all of these.
[220.98 --> 223.62]  Like since the beginning, we were nine years old at this point.
[223.62 --> 229.46]  So it's funny and weird to be in the position of spending years trying to communicate to
[229.46 --> 234.74]  people what we were doing, why it mattered, what the value was, and then suddenly be riding
[234.74 --> 237.64]  at the top of this wave where we've already built the future.
[237.86 --> 238.30]  Right.
[238.36 --> 240.06]  And now everybody's just cottoning onto it.
[241.66 --> 243.44]  And you mentioned like having.
[243.64 --> 245.54]  So I'm reminded of Primer.
[245.68 --> 249.70]  I don't know if you've ever seen that movie where they like build a time machine in their
[249.70 --> 250.34]  garage.
[250.34 --> 253.84]  I don't think they're like totally intending to do what they're intending to do.
[253.92 --> 257.00]  So you build AI without realizing what you were doing.
[257.14 --> 262.32]  So what was your original intention or like where was your motivations when you stepped
[262.32 --> 266.64]  into doing what eventually turned into what is lately.ai?
[266.94 --> 274.14]  Well, some of it is very boring, but I'll start with the exciting part, which is that so I used
[274.14 --> 275.46]  to be a rock and roll DJ.
[275.76 --> 276.12]  Nice.
[276.12 --> 281.98]  My last gig was broadcasting to 20 million listeners a day for XM Satellite Radio.
[282.92 --> 289.24]  And my uber power is turning listeners into fans or customers into evangelists.
[289.60 --> 289.72]  Right.
[289.98 --> 295.32]  And I would leave stations and then I'll never forget my program director calling me six
[295.32 --> 298.88]  months later and saying, hey, the Arbitron book came out and you were number one.
[299.22 --> 300.34]  How did that happen?
[300.66 --> 302.32]  Because it was shocking.
[302.32 --> 303.78]  I was in a format called AAA.
[304.14 --> 305.66]  We're always like 20 or 21.
[306.12 --> 307.54]  Rock and pop are number one.
[308.04 --> 310.34]  And evenings, you know, it was like totally unheard of.
[310.80 --> 315.22]  And I said, I threw your playlist out the window, which was the truth.
[315.72 --> 318.30]  But I also was the production director.
[318.40 --> 320.96]  So I was in charge of all the sound in between the songs.
[321.42 --> 324.90]  And so it was like the me show for, you know, four hours a night.
[324.90 --> 328.12]  And I started thinking about I'd written thousands of commercials.
[328.50 --> 330.04]  I was a fiction writing major.
[330.54 --> 332.68]  I really was excited about the theater of the mind.
[332.78 --> 334.28]  I'm going to vomit on you guys here a little bit.
[334.52 --> 335.64]  This is the place to do it.
[335.90 --> 336.42]  Vomit away.
[336.68 --> 336.86]  Okay.
[338.10 --> 339.58]  You're doing a great job going with me.
[340.32 --> 345.96]  So the theater of the mind is when your imagination has to play a role in the act of the storytelling.
[346.40 --> 346.60]  Right.
[346.66 --> 349.12]  So when you are reading, it happens.
[349.40 --> 350.98]  When you are listening, it happens.
[351.14 --> 353.88]  When you're watching, it doesn't happen because all the pieces are there in front of you.
[353.88 --> 355.26]  So there's nothing for you to fill in the blanks.
[355.26 --> 355.44]  Right.
[355.80 --> 358.10]  So that parallel was really interesting to me.
[358.62 --> 362.70]  And one of the things I read that book, you know, This Is Your Brain on Music, where it
[362.70 --> 365.00]  dissects the neuroscience of music listening.
[365.56 --> 371.22]  So when your brain, Chris, listens to a new song, it must instantly access every other song
[371.22 --> 373.00]  you've ever heard before in that moment.
[373.32 --> 373.52]  All right.
[373.54 --> 376.26]  And so what it's trying to do is to find familiar touch points.
[376.26 --> 379.94]  So it knows where to index that new song in the library of the memory of your brain.
[379.94 --> 385.06]  And it's tugging on nostalgia and obviously memory and emotion, all the things that build
[385.06 --> 385.48]  trust.
[385.72 --> 386.62]  Trust is why we buy.
[387.36 --> 391.72]  Now, similarly, Daniel, if you're writing me an email or a Slack message or a text message,
[391.72 --> 394.12]  I'm going to hear your voice in my head.
[394.14 --> 396.62]  And your voice has that same idea, right?
[396.68 --> 398.42]  Like there's this sound component to it.
[398.74 --> 402.88]  And so if you're doing a great job, you're going to try to figure out how to write in a
[402.88 --> 405.86]  way that's tugging on nostalgia and memory and emotion and trust.
[405.86 --> 411.58]  So I took these ideas out of radio and there's another story for when we're having a beer
[411.58 --> 412.14]  in the middle here.
[412.22 --> 418.12]  But suddenly I had a marketing agency and my first client was a little company, you know,
[418.16 --> 418.66]  called Walmart.
[418.98 --> 419.92]  This is the boring part.
[420.30 --> 425.18]  So I built Walmart, one hell of a spreadsheet system that took these ideas and translated
[425.18 --> 426.08]  them into writing.
[426.08 --> 431.00]  And I got them 130% ROI year over year for three years.
[431.00 --> 436.84]  When we built Lately, Lately was designed to replicate the spreadsheet system I had built
[436.84 --> 437.36]  for Walmart.
[437.76 --> 442.36]  And at that time, the industry where we're in was called marketing resource management.
[442.98 --> 443.42]  How exciting.
[443.76 --> 444.00]  Yeah.
[444.06 --> 446.84]  I mean, really, like the name of our company was Cloud MRM.
[447.46 --> 451.24]  And so we were building an organizational system for marketing is what it was, right?
[451.28 --> 453.80]  That's like about as boring as you can get.
[454.36 --> 455.24]  I love that.
[455.48 --> 456.90]  I spent a decade in the marketing industry.
[457.20 --> 458.30]  I'm so with you on this.
[458.40 --> 459.10]  I loved it.
[459.56 --> 459.96]  Oh, really?
[459.96 --> 461.72]  So, you know, spreadsheet hell, you were there.
[462.52 --> 463.46]  A waving high.
[464.38 --> 466.44]  So almost wrapping up this very long story.
[467.02 --> 469.44]  So we had built marketing resource management.
[469.58 --> 472.78]  We had built a feature for every spreadsheet that I had built Walmart.
[473.52 --> 476.94]  And there's this one feature that everybody was using more than the rest.
[477.00 --> 482.24]  And the idea was you pasted in a URL of a blog, you clicked a button, and we would instantly
[482.24 --> 485.30]  atomize it into dozens of social posts, right?
[485.92 --> 488.96]  That was the foray of the AI we had built.
[488.96 --> 492.28]  Now we do much more, which we can talk about later.
[492.38 --> 495.88]  But that's how we got at least to the beginning of the nine-year trip.
[495.88 --> 503.50]  It's super interesting that you say that because I think maybe people kind of think that they
[503.50 --> 507.72]  can easily reuse content on all of these different platforms.
[507.72 --> 511.70]  And over time, as I've found out, mostly through failing.
[511.70 --> 524.26]  If I'm honest, the same content that you produce for your blog, it's not a trivial task to just take that and create a really compelling LinkedIn post or a really compelling tweet.
[524.82 --> 527.18]  It just doesn't work the same way.
[527.38 --> 531.96]  And also, of course, the algorithms are all changing all the time and that sort of thing.
[531.96 --> 535.58]  So is that part of the education?
[535.88 --> 540.76]  Or do you feel that maybe marketers probably feel this pain most and that's who you're talking to?
[540.98 --> 548.74]  So like your audience, are they mostly wondering like, how does a computer do this for us?
[548.74 --> 551.46]  Because they know the problem and they see it as a really tough problem.
[551.46 --> 557.64]  Or are they mostly like, oh, you know, I could do this if I really sat down and wanted to do it.
[557.70 --> 558.70]  But, you know, why?
[558.84 --> 559.88]  So why do I need a computer?
[560.02 --> 563.40]  Which direction kind of do you find people in most of the time?
[564.04 --> 565.58]  Yeah, there's so many good thoughts in there.
[565.62 --> 568.36]  So the first one is like, it's like math, right?
[568.50 --> 570.88]  There's a reason you go to school and you learn algebra.
[571.36 --> 576.46]  Because when you're using a calculator, you need to be able to know if you've pressed the wrong button.
[576.46 --> 578.60]  Because sometimes you do and you get the wrong answers.
[578.60 --> 584.92]  You need to have the background in your mind so that you can use the technology to do the hard work for you, right?
[585.50 --> 590.62]  So similar with us, we found that, you know, if you're a complete idiot, I can't change that.
[591.56 --> 591.92]  Right?
[592.02 --> 592.60]  You have to have some...
[593.42 --> 596.12]  Unfortunately, that AI does not exist yet.
[598.14 --> 598.90]  Right, right.
[598.98 --> 600.10]  True AI does not exist yet.
[600.20 --> 601.04]  Magic doesn't exist.
[601.14 --> 602.14]  I hate to burst a bubble there.
[602.70 --> 604.98]  Because, you know, I'm a huge Harry Potter fan.
[604.98 --> 611.76]  In fact, I saw a car at the Target the other day and his, I assume it was a man, but the license was Avada Kedavra.
[612.90 --> 616.98]  It's like literally telling everybody to go F themselves like all day, all the time, this guy.
[617.46 --> 617.86]  Wow.
[619.42 --> 620.26]  I know, it was pretty bold.
[620.58 --> 624.00]  So with Lately, let me explain what we do and then answer your question.
[624.00 --> 631.72]  So Lately is able to learn your unique voice, Daniel or Chris, or the unique voice of your brand.
[632.10 --> 637.90]  And you can customize that voice by region, say, for example, or any kind of subset.
[638.30 --> 649.36]  It also is able to tell you exactly what words, ideas, phrases, even the sentence structures that make up the highest possible performing social media messages for you,
[649.36 --> 653.74]  specifically customize for your target audience on any specific channel.
[654.40 --> 658.04]  Now, we're able to build that model in about a couple of seconds for you.
[658.34 --> 662.48]  And then once you have the model, you have to train it and you train it with long form content.
[662.76 --> 665.10]  So we just mentioned a URL of a blog.
[665.44 --> 669.74]  So it could be any kind of text like a newsletter or anything from a Word document.
[670.24 --> 672.60]  It could also be any kind of audio like a podcast.
[673.46 --> 674.94]  It can also be any kind of video.
[674.94 --> 680.42]  So an interview with a CEO, it could be a webinar, a Zoom call, whatever you want.
[680.72 --> 691.18]  In the case of audio and video, we will also give you dozens of audio sound bites and miniature video clips that go with the text version of the social post.
[691.58 --> 697.28]  And then we teach you, and you can do this automatically, how to drip feed that content over time.
[697.28 --> 704.42]  Because the long tail has payoffs that are exponential as opposed to, you know, the one-off.
[704.42 --> 710.84]  So we're also working with marketers to educate them, as you were asking about, on post-mo versus promo, right?
[710.94 --> 714.56]  So promo is great, but it's really hard to get butts in seats live.
[714.68 --> 719.16]  But the after the fact is much easier and you get exponential eyeballs.
[719.48 --> 722.90]  You know, it becomes pretty much everything is evergreen content nowadays.
[723.24 --> 728.04]  And if you think about that, which I'm sure you guys already have, like before you went into this interview, yes, it's timely.
[728.16 --> 731.70]  But generative AI is going to be around for a long time here, right?
[731.70 --> 739.08]  And these ideas, once they're living online, will, the SEO will be, you know, over the roof, over the moon, so to speak.
[739.18 --> 741.20]  So the who was your question.
[741.46 --> 744.98]  At first, we thought our target person was me, small agencies.
[744.98 --> 749.36]  Like, you know, I was charging Walmart 140 grand to do four months of work.
[749.36 --> 756.92]  And the idea was, let's give you 140 bucks and you're one person, you know, so we were trying to service SMBs.
[757.00 --> 761.98]  But the mistake we made was we had built this massive, robust platform that was very much an enterprise platform.
[762.32 --> 763.62]  You know, we didn't know that yet.
[764.14 --> 766.56]  And again, we met another kind of mentor.
[767.06 --> 772.82]  We were working with SAP and they were like, hey, we think you don't understand the power of what you built here.
[772.88 --> 773.98]  Let us help you out.
[773.98 --> 776.06]  And I'll pause the story there.
[776.16 --> 778.94]  There's more, but does that answer your question?
[779.22 --> 779.36]  Yes.
[779.94 --> 780.86]  It was a good story.
[781.02 --> 782.10]  I was all in it.
[782.16 --> 783.78]  You like cut it off right there in the middle.
[783.92 --> 785.02]  I was like, what are you doing?
[785.54 --> 787.26]  Well, we'll get the rest.
[787.44 --> 791.32]  I mean, like the, you know, it's funny because trends change.
[791.46 --> 792.52]  Markets change, obviously.
[792.70 --> 797.04]  And you want to be, you don't want to be, you know, loosey-goosey, but you also want to be flexible.
[797.04 --> 800.74]  And you want to be able to foresee those things and then turn on the dime when you need to.
[800.74 --> 806.80]  And with us, because we had built marketing resource management, that window of sexiness was pretty small, actually.
[806.98 --> 810.70]  There was a company called Percolate that was dominating the enterprise space.
[810.80 --> 816.42]  And here we are, this little company trying to be the SMB version of something that no SMB could really understand, honestly.
[817.08 --> 820.80]  And we were trying to sell to marketers, specifically like CMOs.
[820.80 --> 830.18]  And we discovered, after a lot of pain, actually, that they were very much threatened by being replaced, you know, which is kind of reasonable.
[830.64 --> 833.74]  And so we had to learn to reposition the product.
[833.92 --> 837.00]  We learned to automate it and create self-service.
[837.28 --> 839.82]  We learned to pitch to CROs.
[839.96 --> 843.12]  We built in a feature lately where you can actually syndicate the content.
[843.12 --> 851.14]  One button can push out months' worth of social posts across every employee's channel that they have connected that you can imagine, right?
[851.18 --> 856.38]  So you can, like, literally do all the influencer marketing for your entire business in, like, an hour.
[857.02 --> 864.96]  So you mentioned voice quite a few times, which is definitely a loaded term within, like, the AI space.
[864.96 --> 878.68]  So there's one part of voice, which is, like, we've had Josh Meyer from Koki on the show talking about, like, voice cloning and, like, you know, style transfer of voices or using your voice in another language, that sort of thing.
[878.78 --> 883.30]  So certainly there's that element of that is relevant to content, right?
[883.70 --> 894.34]  But if I'm understanding right from a very non-marketing person's perspective, what you're referring to as voice is somewhat inclusive of that but is much more.
[894.34 --> 905.66]  Could you kind of help those maybe without as much of a marketing background understand what do you mean when you say voice and what do you mean when, like, an AI system learns your voice?
[905.78 --> 908.54]  What is learnt, I guess, in that process?
[909.48 --> 909.96]  I like it.
[909.96 --> 924.24]  So because we're able to surface you literally a word cloud of the words that make up the messaging that gets you the highest engagement, the most clicks and likes and comments and shares, we can see how you write.
[924.24 --> 930.24]  And we can see how, when you're writing well, what's the DNA that makes up those messages.
[930.68 --> 935.00]  And we can learn how you write for your brand or for yourself.
[935.12 --> 945.66]  Like, even when I write social posts on LinkedIn, I get 86,000 views because I'm really good at writing and I use a very specific, quote, voice style of writing.
[945.66 --> 950.64]  For example, in real life, I swear like a sailor, I'm just so foul.
[950.80 --> 953.44]  And online, I try to do that less.
[954.40 --> 960.20]  So I'll make up hyperbole like holy hot pickled jalapeno peppers, for example.
[960.76 --> 969.06]  Now, when Lately is trying to write in my voice, it will insert things like that because it knows me well enough to do that.
[969.06 --> 977.66]  So part of me kind of coming into this conversation, like I see so many of these people that are making posts that are very formulaic, right?
[977.74 --> 984.88]  Like, I don't know how many times a day on Twitter I see some tweet that says, what a week in AI.
[985.42 --> 988.54]  Here's seven things that you shouldn't miss.
[988.70 --> 989.62]  Tweet thread.
[990.00 --> 994.30]  And like, oh, my gosh, how do I like I should be able to get through these.
[994.40 --> 997.12]  But they're not using Lately.ai, I can tell you.
[997.12 --> 997.60]  Right.
[997.60 --> 998.84]  They are not.
[999.14 --> 999.32]  Yeah.
[999.98 --> 1019.50]  Could you speak a little bit towards like generative content and how that could be or maybe is in certain cases formulaic and how this sort of approach can go beyond that to maybe be more creative, certainly more personalized?
[1019.76 --> 1022.82]  I think you're talking kind of about this personalized voice.
[1022.82 --> 1030.86]  I assume we're not just talking about like generate the listicle for or the tweet thread for Twitter type of thing.
[1031.00 --> 1031.14]  Right.
[1031.46 --> 1031.76]  Yeah.
[1031.94 --> 1041.32]  So what's interesting about your point is, I mean, this is why humans are always relevant, because you quickly can see that there is a formula there and it begins to wash over you.
[1041.32 --> 1042.80]  It's not tantalizing anymore.
[1043.06 --> 1047.46]  And the instinct that you have is not the instinct of the people who are still publishing those.
[1047.56 --> 1055.08]  They're still sticking with the old thing because they haven't taken a moment to research, really, but even just use their instincts of like what's working.
[1055.08 --> 1056.62]  You know, you have to experiment.
[1057.12 --> 1057.76]  You have to.
[1058.20 --> 1059.10]  It's the same way in radio.
[1059.32 --> 1064.02]  Like, I mean, I spoke to a black room of no one for 12 years.
[1064.92 --> 1065.60]  I know how you feel.
[1065.80 --> 1065.94]  Yeah.
[1065.94 --> 1066.46]  You know how I feel.
[1066.54 --> 1066.70]  Right.
[1066.70 --> 1074.74]  And what they advise you, what my mentors advised me back then was you imagine the listener in your mind, whoever it is.
[1074.82 --> 1074.92]  Right.
[1074.96 --> 1076.30]  Imagine who the audience is.
[1076.40 --> 1082.46]  Now, online, I generally just try to entertain myself, you know.
[1082.74 --> 1083.72]  And so let me back up.
[1083.78 --> 1088.54]  So that was sort of one thing is like humans are relevant and we'll get into that a little more.
[1088.92 --> 1089.10]  Why?
[1089.18 --> 1091.48]  And they will remain relevant always in sales and marketing.
[1091.48 --> 1092.54]  That will never go away.
[1093.56 --> 1094.68]  And I'll tell you why real quick.
[1094.68 --> 1104.74]  When we were talking about the theater of the mind, what happens there, if you are a good author or you're good on the microphone, you're actually letting someone in.
[1105.26 --> 1108.82]  So I'm going to make you, Daniel, feel as though you're part of this story.
[1108.92 --> 1111.30]  Now, I've written it this way so that you have to fill in.
[1111.34 --> 1112.40]  I know you have to fill in the blank.
[1112.46 --> 1114.60]  I have to allow for a third character.
[1115.02 --> 1115.68]  That is you.
[1115.74 --> 1117.12]  That's your imagination, your brain.
[1117.56 --> 1120.66]  And that's why when you read a really great book, it's so powerful.
[1120.74 --> 1122.40]  And then you see the movie and you're so pissed off.
[1122.70 --> 1122.90]  Right.
[1122.90 --> 1125.16]  They're taking that ownership away from you.
[1125.28 --> 1127.80]  So it's the difference between a one-way street and a two-way street.
[1127.90 --> 1129.20]  And this is how you build fans.
[1129.74 --> 1133.40]  That mysterious thing is the human element in marketing.
[1133.84 --> 1135.60]  Marketing is often unexplainable.
[1135.98 --> 1136.52]  It is.
[1136.64 --> 1138.54]  Like people are always trying to science it to death.
[1138.68 --> 1139.38]  And you cannot.
[1139.54 --> 1146.74]  This is what makes it magical, you know, which is why human training is something we actually worked into our algorithm from the beginning.
[1146.74 --> 1154.26]  That was a fascinating point there is that kind of that unknowable aspect a little bit of what tickles a psyche.
[1154.48 --> 1155.50]  And that evolves.
[1155.56 --> 1158.92]  And people get used to the thing that was the past thing a moment ago.
[1159.30 --> 1165.58]  And whatever you're doing now will change in another moment, you know, as we accommodate that in our brains and start ignoring it.
[1165.58 --> 1178.50]  And so, you know, you've spent these years working on your algorithms to try to hone in on that and, you know, using your method and try to get to voice of what the messaging is in the different mediums.
[1178.50 --> 1185.06]  So, now in the last year, all this technology change has been thrown at you and your company.
[1185.54 --> 1190.62]  Generative AI and large language models and all this stuff, all these cool tools.
[1191.14 --> 1198.84]  How has that changed how you're approaching the problem of kind of finding that magical nugget of voice in there?
[1198.92 --> 1206.52]  Because you have a whole new set of tools available to you now that you're presumably integrating in to all this stuff.
[1206.52 --> 1214.76]  That has to, like, have turned your world upside down a little bit just because of the vast amount of capability you now have in addition to what you had before.
[1215.16 --> 1216.20]  A couple of things.
[1216.32 --> 1219.48]  Number one, there's more than one kind of generative AI.
[1219.68 --> 1222.96]  Now, the world is really only familiar with one, which is ChatGPT.
[1223.22 --> 1227.90]  We were in the closed beta four years ago of ChatGPT2, so we're OGs with them.
[1228.10 --> 1230.74]  But I built an engine that's mine.
[1230.82 --> 1231.86]  It's proprietarily mine.
[1231.86 --> 1235.88]  So, we like to think of lately as a fully loaded ice cream sundae.
[1235.88 --> 1239.94]  There's a banana and hot fudge and a bunch of different flavors of ice cream and whipped cream.
[1240.50 --> 1242.90]  And I made this sundae all myself.
[1243.18 --> 1246.26]  On the top, there's a couple of tiny, tiny chocolate sprinkles.
[1246.40 --> 1246.92]  I like chocolate.
[1247.34 --> 1247.94]  They could be rainbow.
[1248.50 --> 1252.16]  And that's IBM Watson and Google Pegasus and MeaningCloud and ChatGPT.
[1252.16 --> 1263.32]  Now, around the data sets, what's been exciting is, you know, there's this huge wave of, oh, my God, public data, copyright infringement, you know, all that.
[1263.44 --> 1268.12]  And we only use a private data set lately, your data, and we don't share it.
[1268.12 --> 1270.98]  And so, we've been getting greenlit by legal.
[1271.22 --> 1282.10]  And so, that kind of explosion of information is obviously really helping us a lot because a lot of companies are now banning generative AI company-wide because people are cheating at work.
[1282.18 --> 1287.48]  And they're worried about data being put out into the Google's public, you know, database, for example.
[1287.48 --> 1296.68]  But the other thing, too, is so generative AI, as we all know it, not me, but the world, is type in a few things, get a big, long thing out, right?
[1296.80 --> 1297.44]  That's the deal.
[1297.96 --> 1299.32]  Lately works the opposite way.
[1299.50 --> 1305.30]  You have to give us a very long thing first, like a video or a blog or an audio file.
[1305.64 --> 1313.14]  And then we're going to take that unique model we built from you and clip it up into dozens and dozens of very small social posts.
[1313.14 --> 1324.08]  And the way we're able to capture your voice, which ChatGPT can't do because they don't have, and we're not competitors with them in any way, but they don't have a data loop.
[1324.38 --> 1324.88]  But I do.
[1325.10 --> 1326.24]  You connect your social channels to Lately.
[1326.46 --> 1327.60]  I can read your analytics.
[1327.82 --> 1329.30]  I can see what's performing best.
[1329.68 --> 1334.90]  And I'm learning all day long, every day long, whether you're publishing through Lately or something else.
[1334.90 --> 1343.34]  And then every change you make to anything you publish, if you edit it, if you add a picture, if you delete it, if you don't publish it, I'm learning, right?
[1343.46 --> 1344.26]  So it's a tight loop.
[1344.72 --> 1352.32]  The other thing here is, you know, now that there's been this explosion of words, the problem still remains.
[1352.58 --> 1353.68]  How do you cut through the noise?
[1353.78 --> 1359.00]  This is the problem always of all social marketing and all sales enablement, you know, whatever.
[1359.60 --> 1360.70]  Guess what the answer is?
[1360.72 --> 1361.52]  It's the same answer.
[1362.32 --> 1363.88]  Be more human, right?
[1363.88 --> 1364.80]  Be more human.
[1364.90 --> 1369.80]  So when you build that into your algorithm, so I'll give you an example.
[1370.16 --> 1374.70]  We worked with Philips Electric, which is, they've rebranded to Signify.
[1374.98 --> 1379.66]  And we got them, on average, 124% more engagement on LinkedIn.
[1380.24 --> 1385.14]  We saved them 84% of their time, and I think it was 82% of their budget.
[1385.64 --> 1390.86]  And it's not just on creating content, but it's on creating content that works, right?
[1390.92 --> 1391.58]  This is the thing.
[1391.58 --> 1396.48]  Now, you can ask generative AI to create social media posts for you, but they'll have no way
[1396.48 --> 1402.16]  to know if it's the right ones to create because there's no information to check that data.
[1402.38 --> 1403.90]  Let me follow up on something you said there.
[1404.12 --> 1406.64]  I'm going to ask the dumbest question you've ever heard.
[1407.04 --> 1409.02]  You just said, be more human.
[1409.32 --> 1411.54]  What does that mean when you say that?
[1411.54 --> 1416.92]  So when you're saying that's the thing to do, I hear you, and I think I know what that means,
[1417.00 --> 1421.62]  kind of like, but I probably don't because I think it means something very specific to you
[1421.62 --> 1422.80]  in the context.
[1423.12 --> 1425.24]  Can you share that a little bit, what that means to you?
[1425.68 --> 1426.04]  Yeah.
[1426.40 --> 1427.10]  Thanks for asking.
[1427.24 --> 1428.24]  No one has ever asked that.
[1428.38 --> 1429.24]  They really should, right?
[1429.24 --> 1431.08]  I'm very good at dumb questions.
[1431.32 --> 1432.62]  I excel at dumb.
[1433.74 --> 1435.16]  No, no, no, not dumb.
[1435.28 --> 1436.14]  Very smart question.
[1436.44 --> 1438.80]  So it's using that instinct, right?
[1440.96 --> 1446.36]  Because you can't science everything to death, it's predictive and it's a little bit indescribable.
[1446.62 --> 1450.52]  So you have to know whether that joke is going to land, right?
[1450.54 --> 1451.84]  Like a comedian, that's the deal.
[1451.94 --> 1454.78]  Sometimes the atmosphere is ready and sometimes not yet ready.
[1454.86 --> 1456.72]  You can make a joke about that just yet, right?
[1456.72 --> 1462.50]  That ability to read the room, which is, again, something I did in the dark for years,
[1462.74 --> 1465.42]  is a, I don't think that can be taught, to be honest to you.
[1466.34 --> 1470.26]  However, it does come from making mistakes, right?
[1470.32 --> 1473.24]  So the more mistakes you make, the more you learn from them.
[1474.38 --> 1480.80]  Being human on social can be, it's funny, you see people experimenting on LinkedIn a lot
[1480.80 --> 1483.14]  right now doing like more personal things.
[1483.56 --> 1486.20]  I do incredibly personal things on LinkedIn and people are like, what?
[1486.20 --> 1486.48]  You do.
[1486.48 --> 1486.92]  Yes.
[1487.60 --> 1489.36]  They're usually having to do with animals.
[1489.60 --> 1490.16]  So yes.
[1490.78 --> 1491.14]  Great.
[1491.90 --> 1492.80]  Is it working?
[1492.92 --> 1493.92]  You're getting engagement from it?
[1495.18 --> 1501.42]  You know, the truth is I'm not measuring it, but it definitely is different from what
[1501.42 --> 1505.34]  everyone else is doing because I'm, just for anyone out there, because people hit me, I'm
[1505.34 --> 1508.68]  really bored with everyone self-promoting on LinkedIn all the time.
[1509.12 --> 1512.74]  And so like when people hit me up with those messages or they're in my feed, I just turn
[1512.74 --> 1513.66]  off everything.
[1514.22 --> 1514.74]  So yes.
[1514.98 --> 1515.54]  There you go.
[1515.54 --> 1515.98]  Yeah.
[1516.04 --> 1516.82]  So you're experimenting.
[1517.16 --> 1520.10]  Anything that's not the usual may capture my interest.
[1520.10 --> 1525.06]  If it's the same old stuff, I'm asleep as my eyes glaze over your post.
[1525.60 --> 1526.42]  So I love that.
[1526.56 --> 1528.28]  And that's a key thing to think about.
[1528.38 --> 1533.28]  So say if I want to promote something that I'm doing, sometimes I'm lazy, of course, but
[1533.28 --> 1535.74]  there's only two objectives on social media.
[1535.86 --> 1536.46]  Click and share.
[1536.56 --> 1536.98]  That's it.
[1537.26 --> 1537.48]  Right.
[1537.48 --> 1540.72]  So if you back into it knowing that that's the deal, I need to write copy that's either
[1540.72 --> 1541.76]  shareable or clickable.
[1542.00 --> 1545.68]  It's very hard to get to the clickable point because that's a lot of trust you're asking
[1545.68 --> 1547.12]  from people and time and all that.
[1547.20 --> 1550.44]  But sharing is easy because sharing is all about the ego.
[1550.44 --> 1553.98]  And if I give you content that's worth sharing, you look good.
[1554.22 --> 1554.42]  Right.
[1554.50 --> 1559.54]  Kind of like if someone in college brings you the latest record from whoever and then you
[1559.54 --> 1560.20]  play it for a friend.
[1560.30 --> 1561.14]  Now you're the tastemaker.
[1561.50 --> 1561.92]  Same idea.
[1561.92 --> 1561.96]  Yeah.
[1562.76 --> 1565.50]  So shareable content, Gary Vee has created it.
[1565.54 --> 1568.82]  You can just spread joy with positive messaging.
[1569.20 --> 1573.18]  I find that any content that includes God does really well.
[1573.54 --> 1578.52]  Certainly negative stuff like I've posted, you know, in tears getting a no from an investor.
[1579.30 --> 1581.02]  I mean, I was experimenting with all these things.
[1581.08 --> 1582.16]  I'm doing it on purpose.
[1582.38 --> 1583.64]  You know, I'm trying these things out.
[1584.22 --> 1590.08]  I often will do things like I'll say if there's an interview coming up with Chris Daniel and
[1590.08 --> 1596.58]  moi, like I'll refer to myself as moi because I like Miss Piggy and like you might not know
[1596.58 --> 1597.92]  that about me, but I didn't.
[1598.20 --> 1600.28]  But I have a raccoon named Miss Piggy for real.
[1600.62 --> 1601.32]  So there you go.
[1601.42 --> 1601.62]  Right.
[1601.70 --> 1605.30]  And it's not an obvious reference, but I'm looking for those nostalgic touch points we
[1605.30 --> 1606.10]  thought about before.
[1606.24 --> 1606.44]  Right.
[1606.78 --> 1610.30]  This is the and this backs up a little more to one of the questions that I didn't answer
[1610.30 --> 1616.28]  Daniel earlier is that lately when it's lifting out, it's trying to lift out teasers that
[1616.28 --> 1621.14]  will get you just enough interested to click without giving you the full kitchen sink.
[1621.60 --> 1621.80]  Right.
[1622.48 --> 1624.82]  Or it's trying to give you a shareable like those same things.
[1624.82 --> 1626.94]  That's what's behind the AI's brain, what it's thinking of.
[1627.22 --> 1628.06]  So it's the same idea.
[1628.30 --> 1632.70]  And let me give you some proof in the pudding just around around this idea, whether you're
[1632.70 --> 1633.82]  using lately or not to do it.
[1633.88 --> 1638.10]  So lately, as you guys know, we dog food our own product.
[1638.44 --> 1640.64]  So I'm going to ask you for the file of the show.
[1640.74 --> 1642.18]  We're going to run it through our own AI.
[1642.18 --> 1647.90]  Our AI model is going to run through, lift out all the quotes that you, Daniel, or Chris
[1647.90 --> 1651.56]  or me say that match up with my model and my target audience.
[1651.56 --> 1653.04]  It's going to attach the video clips.
[1653.18 --> 1655.64]  It's probably going to give me 40 or so.
[1656.20 --> 1661.02]  My social media manager will run through them and make sure that lately isn't off the rails
[1661.02 --> 1664.86]  and kind of help it out if it needs to be helped out by making the edits, you know.
[1665.22 --> 1670.24]  And then we will publish those posts not only on our brand channels, but all of our employee
[1670.24 --> 1672.98]  channels as well, because the more the merrier, right?
[1673.00 --> 1673.94]  We're all in this together.
[1674.38 --> 1677.86]  Now we do this and nothing else for marketing.
[1678.10 --> 1679.08]  This is all we do.
[1679.16 --> 1680.38]  I'm on a podcast once a week.
[1680.46 --> 1683.56]  Sometimes I write a guest blog or host a webinar or something.
[1683.56 --> 1687.26]  And we have a 98% sales conversion.
[1687.72 --> 1687.86]  Wow.
[1688.38 --> 1689.16]  That's crazy.
[1689.30 --> 1690.94]  Because that's how good the AI is.
[1691.30 --> 1694.68]  Learn it knows what you guys will share or click, right?
[1695.06 --> 1695.72]  My audience.
[1700.24 --> 1704.60]  I'm Jared, and this is a Changelog News Break.
[1705.28 --> 1710.44]  Device Script is Microsoft's new TypeScript programming environment for microcontrollers.
[1710.56 --> 1716.68]  It's designed for low power, low flash, low memory embedded projects, and has all of the
[1716.68 --> 1721.76]  familiar syntax and tooling of TypeScript, including the NPM ecosystem for distributing packages.
[1722.36 --> 1724.84]  This project has a lot of devs excited.
[1725.86 --> 1727.50]  Jonathan Barry says, quote,
[1727.50 --> 1728.62]  Dope.
[1729.08 --> 1730.08]  TypeScript for hardware.
[1730.76 --> 1734.80]  Always glad to see these attempts at bringing web technologies to embedded systems and see
[1734.80 --> 1735.38]  what sticks.
[1735.74 --> 1737.80]  Even when they don't, they inspire innovation.
[1739.24 --> 1741.24]  Zach Silviera says, quote,
[1741.72 --> 1744.22]  This is so much better than MicroPython.
[1745.08 --> 1747.84]  And Andrea Guiamarchi says, quote,
[1748.40 --> 1752.80]  This is the first Esperino competitor, and I think it's going to be huge.
[1752.80 --> 1758.30]  You just heard one of our five top stories from Monday's Changelog News.
[1758.68 --> 1763.22]  Subscribe to the podcast to get all of the week's top stories and pop your email address
[1763.22 --> 1769.56]  in at changelog.com slash news to also receive our free companion email with even more developer
[1769.56 --> 1771.08]  news worth your attention.
[1771.54 --> 1774.96]  Once again, that's changelog.com slash news.
[1774.96 --> 1784.36]  You had said before we recorded, silence is sometimes the best practice.
[1785.08 --> 1791.46]  And one of the things that my radio mentor, Steve Zinn, taught me was to leave silence on the air as a tactic.
[1792.44 --> 1793.62]  This is that mistake.
[1793.74 --> 1794.92]  This is that humanness.
[1795.54 --> 1797.20]  And so what happens when there's silence?
[1798.20 --> 1798.54]  Thinking.
[1799.54 --> 1800.06]  Anticipation.
[1800.42 --> 1800.82]  Thinking.
[1801.58 --> 1802.14]  Anticipation.
[1802.14 --> 1802.82]  That's right.
[1802.92 --> 1806.16]  People turn up the radio is what they do also, you know.
[1806.94 --> 1811.12]  And thinking about how we're writing, and you've seen this tactic on LinkedIn as well,
[1811.22 --> 1815.78]  is like people like leaving different space, you know, putting in enter, enter, enter, whatever.
[1816.42 --> 1820.84]  There's something about, then it goes to your point, Chris, of doing the unexpected, you know.
[1821.34 --> 1828.72]  What I learned about making fans, which are more valuable than just listeners or customers versus evangelists.
[1828.72 --> 1831.24]  And by the way, let me put the proof in the pudding there.
[1831.68 --> 1836.74]  Not a day has passed in four years where someone hasn't spontaneously written on social media about lately.
[1836.98 --> 1837.64]  Not one day.
[1838.04 --> 1840.40]  You don't want to be the megaphone.
[1840.66 --> 1841.72]  You want to be the magnet.
[1842.26 --> 1849.00]  And when you are the magnet, in order to truly be that kind of magnet, you let other people be the light.
[1849.10 --> 1850.24]  You show them how to be the megaphone.
[1850.32 --> 1852.04]  You show them how to, you put them on the pedestal.
[1852.04 --> 1853.72]  Can you define a little bit about what those are?
[1853.84 --> 1858.76]  When you talk about the megaphone versus the magnet and the light in there, can you kind of clarify what that means?
[1859.30 --> 1861.54]  Yeah, like I'm obviously an A personality.
[1861.74 --> 1864.20]  So I could walk into a room and dominate that room in a second.
[1864.30 --> 1866.58]  I can get on the stage and like be, hey, look at me.
[1866.62 --> 1866.98]  Hey, look at me.
[1867.02 --> 1867.68]  I could do that.
[1868.00 --> 1872.34]  Or I can lift you up and make you feel like everybody wants to listen to you.
[1872.58 --> 1874.14]  Everybody wants to talk to you, right?
[1874.14 --> 1879.60]  When you are able to do that, people walk away and they remember that you made them feel this way.
[1879.68 --> 1887.48]  It's like I was listening to Smart List the other day and Will was saying how a few years ago they were at an SNL after party.
[1888.42 --> 1894.80]  And Steven Spielberg, who we did not know, just walked over to him and said, hey, Will, I'm Steven Spielberg.
[1894.90 --> 1898.94]  I just saw your director's cut of XYZ and I wanted to tell you it was really impressive.
[1899.10 --> 1899.74]  And then he walked away.
[1900.54 --> 1901.66]  Now, holy, right?
[1901.78 --> 1902.72]  Like that's how you do it.
[1902.76 --> 1903.52]  This is the God.
[1903.52 --> 1907.48]  First of all, the best thing he did was he introduced himself, right?
[1907.56 --> 1910.18]  He didn't assume that everybody knew he was Steven Spielberg.
[1910.44 --> 1913.18]  I mean, that's pretty mega for a megastar like that.
[1913.78 --> 1917.72]  Also, he left before the guys had a moment to be like, oh, my God, we love you, blah, blah, blah.
[1917.82 --> 1918.70]  Like he was just in and out.
[1918.78 --> 1921.58]  It was just that drop of, you know, pixie dust kind of thing.
[1922.26 --> 1925.38]  So the way you can do that on social is really easy.
[1925.72 --> 1926.52]  Here, I'll give you a tip.
[1926.62 --> 1927.62]  Thank you is the best.
[1927.76 --> 1928.62]  We call it thank you marketing.
[1928.62 --> 1940.32]  The more you thank somebody, the more they it's like husbands, you know, like the more work in the yard David does, the better I tell him how great it looks.
[1941.00 --> 1941.36]  Right.
[1941.46 --> 1942.74]  Because I want him to do it more.
[1942.74 --> 1948.32]  You know, and thank you can come in the form of thank you.
[1948.48 --> 1951.50]  That's one of our biggest hashtags that lately is hashtag all caps.
[1951.56 --> 1951.94]  Thank you.
[1952.34 --> 1955.28]  Because it's people reshare that content.
[1955.40 --> 1961.28]  Like so with you guys, when I'm going to get your content, I'm going to drive all the traffic back to wherever to you where this full version.
[1961.28 --> 1962.84]  This is the ultimate thank you.
[1962.90 --> 1963.06]  Right.
[1963.16 --> 1971.58]  And I'm going to tag you and I'm going to drip feed it out probably slowly over the time so that like every time you see it, you're inspired to reshare it.
[1971.64 --> 1974.20]  You're not like overwhelmed by my overtagging you, for example.
[1974.36 --> 1979.30]  But also, I don't need to drive the traffic back to me because I'm not looking for that.
[1979.52 --> 1981.12]  I'm looking for the reach.
[1981.28 --> 1982.20]  I'm looking for the shares.
[1982.48 --> 1984.40]  We ride on word of mouth lately.
[1984.74 --> 1986.30]  Like that's what we ride on.
[1986.60 --> 1988.98]  I have a left field question for you.
[1989.12 --> 1990.92]  And it's a selfish question.
[1991.28 --> 1991.76]  Great.
[1992.26 --> 1994.92]  And it may be a very simple answer of no, there's no difference.
[1995.02 --> 2003.42]  But just in case there is, is there any difference in how you would approach from like a nonprofit standpoint versus a for-profit commercial standpoint?
[2003.42 --> 2009.96]  Because you're trying to get to a different type of outcome versus selling a product or service versus that.
[2010.42 --> 2016.00]  And as in my – I have a day job, but I also have an unpaid job in a nonprofit.
[2016.00 --> 2021.94]  And so I'm very curious if there's any difference in that or if it's all the same thing.
[2022.46 --> 2023.08]  It depends.
[2023.28 --> 2029.44]  I mean, because I've worked for a lot of nonprofits as well, including United Way Worldwide and National Disability Institute and the Walmart Foundation.
[2029.44 --> 2029.52]  Interesting.
[2029.94 --> 2032.36]  So, like I said, there's only two objectives on social.
[2032.50 --> 2034.86]  And this doesn't matter if you're a nonprofit or for-profit or government.
[2035.02 --> 2035.76]  It's click or share.
[2035.92 --> 2036.54]  Like that's it.
[2036.70 --> 2036.80]  Okay.
[2036.92 --> 2040.02]  Where you click to or what you're sharing, you know, that depends.
[2040.42 --> 2041.34]  Ice Bucket Challenge.
[2041.54 --> 2042.06]  Hello, right?
[2042.10 --> 2042.38]  Everybody.
[2042.68 --> 2044.18]  There's like how human was that?
[2044.18 --> 2048.08]  You know, they did a great job, but they raised money at the same time.
[2048.48 --> 2051.50]  Now, you and I both know that they have a grant to spend this money.
[2052.16 --> 2059.58]  And oftentimes for a nonprofit, while sale isn't the objective, a lot of times it's just make some noise, to be honest with you.
[2059.76 --> 2065.56]  Because the people giving them the grant want to see that visibility online, you know, a little more.
[2065.94 --> 2067.34]  But everyone has an objective.
[2067.44 --> 2068.48]  It's just a matter of breaking it down.
[2068.48 --> 2073.74]  Like when I was working with the Walmart project, it was fueled by the nonprofit foundation.
[2074.10 --> 2075.44]  And this was so boring.
[2075.86 --> 2076.96]  I mean, I had a great time.
[2077.04 --> 2085.84]  But it was there was the IRS, Walmart, National Disability Institute, Bank of America, and AT&T and United Way Worldwide.
[2086.20 --> 2088.24]  And they were working together.
[2088.78 --> 2093.14]  There was a free tax prep website that United Way Worldwide had built in tandem with Walmart.
[2093.32 --> 2095.82]  It was the first free tax prep online available.
[2095.82 --> 2102.38]  And we were trying to help lift the poor out of poverty through income tax credits and financial education.
[2102.66 --> 2104.84]  These people maybe make $20,000 a year.
[2104.94 --> 2108.48]  So a $2,000 EITC credit is actually life changing, right?
[2109.06 --> 2110.90]  Now, that's the boring part here.
[2111.18 --> 2112.54]  And there's acronyms galore.
[2112.74 --> 2119.34]  But we got the project with my method, 130% ROI year over year for three years.
[2119.66 --> 2122.72]  And their ROI was taxes filed, right?
[2122.74 --> 2123.62]  That was their objective.
[2123.62 --> 2126.12]  So we still want people to click and share.
[2126.52 --> 2128.60]  But once they click, you know, start to file the taxes.
[2128.76 --> 2129.48]  So that was the whole.
[2129.96 --> 2133.94]  And by the way, one of the things we learned was how to take a national message.
[2134.26 --> 2138.58]  And this is what I was working on them with, one of the many things, and to localize it.
[2138.72 --> 2144.16]  And the localization came through local hashtags, right?
[2144.24 --> 2147.12]  The cities, the college campuses, wherever we were, you know.
[2147.12 --> 2158.56]  I get this, like, feeling inside sometimes that, like, we're starting to generate so much content using automated methods, using AI.
[2158.88 --> 2171.30]  And despite all of that having it sort of like having a voice or personalization, I'm wondering, like, a lot of the creative things that I see online, I don't think yet.
[2171.30 --> 2174.04]  I don't think they're generated by AI yet.
[2174.20 --> 2183.14]  So how do you see, like, going into the future as we see more generative AI content driving social posts?
[2183.14 --> 2194.02]  How do you see things shifting in terms of, like, the creative trends that we'll see online and maybe the opportunities within marketing?
[2194.20 --> 2196.10]  Like, how do those opportunities change?
[2196.60 --> 2208.80]  And how would someone balance, like, oh, I could do this at scale with AI versus, hey, I want to do something completely new that no one's done yet that might, you know, break some trends or something like that?
[2209.14 --> 2211.04]  How do you see that balance going forward?
[2211.04 --> 2223.52]  And do you have any recommendations for people out there that are maybe in the midst of trying to generate content with AI, whether that be, you know, text or audio, video, whatever?
[2224.40 --> 2224.60]  Yeah.
[2224.82 --> 2227.72]  I mean, I think my first advice would be just calm down, everybody.
[2228.86 --> 2229.68]  Hold on.
[2230.12 --> 2231.16]  So think about humans.
[2231.16 --> 2234.66]  We're the only mammals that when we come out of the womb, we're completely helpless.
[2234.80 --> 2240.02]  We can't feed ourselves, can't defend ourselves, can't stand up, can't even hold our heads up, you know, nothing.
[2240.02 --> 2243.62]  If AI was a human, it would be about three months old.
[2244.10 --> 2249.38]  So I think that's just one important thing to remember is that the human guidance is required, you know.
[2250.18 --> 2258.38]  Certainly, as we talked about at the top, was the prompting expertise is going to be something that people are looking for as well.
[2258.38 --> 2263.52]  Because in order to get the robot to do what you want, it has to be asked just the exact right questions.
[2263.70 --> 2264.84]  You know, what are those questions?
[2264.84 --> 2269.12]  With technology, as you guys already know, I mean, technology happens.
[2269.20 --> 2273.24]  It'll continue to happen and it'll continue to improve lives and replace jobs.
[2273.54 --> 2274.70]  And jobs will evolve.
[2274.78 --> 2275.96]  And we're in the same boat here.
[2276.46 --> 2280.54]  This strategy piece is where humans are still really absolutely necessary.
[2280.72 --> 2282.90]  I mean, you know, so AI is not sentient.
[2282.90 --> 2290.46]  Like, unfortunately, Hollywood really has given us a grave misunderstanding of what the definition means.
[2290.82 --> 2294.86]  I think it was maybe it was Paul Roetzer from Marketing AI Institute.
[2295.00 --> 2298.48]  But they said, AI still lacks emotional intelligence.
[2300.04 --> 2301.78]  Which is also true, you know.
[2301.78 --> 2308.26]  And then another quote, and I don't know who said this, but it's, if you're not using AI, you're going to be falling behind.
[2308.44 --> 2314.80]  But the people who are using AI in tandem with the work they're doing, just like that calculator we talked about before, right?
[2315.14 --> 2317.00]  They're the ones that are going to be getting ahead of the game.
[2317.08 --> 2321.12]  So you have to figure out a way to obviously embrace it.
[2321.18 --> 2323.64]  And I think it's so funny that companies are banning generative AI.
[2323.64 --> 2326.62]  Because remember when, like, remember when everybody banned Facebook?
[2327.20 --> 2327.50]  Yeah.
[2328.22 --> 2328.46]  Right.
[2328.54 --> 2331.34]  Or I think there's still government agencies that can't use Google Docs.
[2331.34 --> 2332.56]  And you're like, are you kidding me?
[2332.60 --> 2333.66]  Like, get with the program.
[2333.66 --> 2342.62]  I think that's a really good way to set a good foundation as we kind of draw close to here for people to remember that.
[2342.74 --> 2346.86]  And we probably need to be reminded about that every week these days.
[2347.48 --> 2347.60]  Yeah.
[2347.60 --> 2365.82]  As we close out here, maybe just take a moment and share what are you excited by specifically as you look forward over the coming months in terms of either new things that will be possible or where things are headed with lately, that sort of thing.
[2366.02 --> 2370.80]  Take an opportunity to kind of share some of those things that you're excited about.
[2371.06 --> 2371.90]  Thank you.
[2372.22 --> 2375.66]  I'm excited to close the fundraising round that I'm in the middle of doing.
[2375.66 --> 2376.50]  I hope so.
[2376.50 --> 2377.84]  So, yeah, that's awesome.
[2378.16 --> 2378.52]  Congratulations.
[2379.02 --> 2379.88]  Yeah, yeah, yeah.
[2380.00 --> 2384.18]  So, if anyone's interested, feel free to reach out to me, kate at lately.ai.
[2384.88 --> 2388.28]  You know, that will be, that'll help us kind of continue the plans we have.
[2388.38 --> 2394.98]  The voice learning that we talked about earlier is something that we are focused on at the company on sinking our teeth into this year.
[2395.74 --> 2406.30]  And figuring out other ways, like, this is so boring, but, you know, if lately spits out a piece of content that starts with and, like, how can we start recognizing those non sequiturs?
[2406.50 --> 2407.16]  That happen.
[2407.16 --> 2410.24]  And we can remove them, you know, for you before you even get to it.
[2410.58 --> 2418.56]  Or once we have the transcripts in the background, instead of you having to control F and clean the ums out, like, how can we do this stuff more automatically?
[2418.56 --> 2422.96]  Because, obviously, it's harder to train video and audio than it is text.
[2422.96 --> 2424.80]  Because with text, you work on it for so long.
[2424.82 --> 2426.16]  So, it's coming to me pretty much ready.
[2426.86 --> 2428.64]  We're also working on sentiment.
[2429.22 --> 2436.10]  So, the ability to push a button and say, make this post funny or make this post, I don't know, stern.
[2437.06 --> 2438.08]  That kind of idea.
[2438.08 --> 2443.46]  The biggest request we get from our customers is how to take lately and apply it to paid ads.
[2443.56 --> 2445.26]  So, that's a big one we're working on.
[2445.84 --> 2446.00]  Cool.
[2446.26 --> 2447.96]  Well, keep up the good work.
[2448.08 --> 2449.02]  This is awesome.
[2449.28 --> 2449.38]  Thank you.
[2449.44 --> 2452.00]  Thank you so much for taking time to join us.
[2452.24 --> 2456.78]  I'm very excited to dig into this topic a little bit more.
[2457.02 --> 2463.84]  And, yeah, we'll look forward to seeing all of the tags that I'll get over your drip campaign in the coming weeks.
[2464.24 --> 2465.60]  Great conversation today.
[2465.82 --> 2466.08]  Thanks.
[2466.16 --> 2466.74]  Love you guys.
[2466.74 --> 2467.66]  We'll talk soon, all right?
[2476.22 --> 2478.74]  Thank you for listening to Practical AI.
[2479.26 --> 2483.06]  Your next step is to subscribe now, if you haven't already.
[2483.50 --> 2489.52]  And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2490.00 --> 2494.92]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2494.92 --> 2499.30]  Check out what they're up to at Fastly.com and Fly.io.
[2499.70 --> 2505.02]  And to our Beat Freakin' residents, Breakmaster Cylinder, for continuously cranking out the best beats in the biz.
[2505.28 --> 2506.20]  That's all for now.
[2506.46 --> 2507.62]  We'll talk to you again next time.
[2507.62 --> 2520.26]  We'll talk to you again next time.
[2520.26 --> 2521.28]  Game on.
[2521.28 --> 2551.26]  Thank you.
