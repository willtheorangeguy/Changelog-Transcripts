[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.74 --> 14.76]  Head to linode.com slash changelog.
[17.44 --> 20.46]  Linode makes cloud computing simple, affordable, and accessible.
[20.86 --> 24.40]  Whether you're working on a personal project or managing your enterprise's infrastructure,
[24.94 --> 28.94]  Linode has the pricing, support, and skill you need to take your ideas to the next level.
[28.94 --> 32.10]  We trust Linode because they keep it fast and they keep it simple.
[32.38 --> 34.88]  Check them out at linode.com slash changelog.
[42.82 --> 47.84]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[48.16 --> 49.92]  productive, and accessible to everyone.
[50.18 --> 54.32]  This is where conversations around AI, machine learning, and data science happen.
[54.32 --> 58.06]  Join the community and Slack with us around various topics of the show at
[58.06 --> 60.68]  changelog.com slash community and follow us on Twitter.
[60.82 --> 62.46]  We're at Practical AI FM.
[68.40 --> 72.34]  Well, welcome to another episode of Practical AI.
[72.76 --> 74.38]  This is Daniel Whitenack.
[74.50 --> 77.32]  I'm a data scientist with SIL International.
[77.32 --> 83.84]  And I'm joined as always by my co-host, Chris Benson, who is a principal AI strategist at Lockheed
[83.84 --> 84.16]  Martin.
[84.48 --> 85.34]  How are you doing, Chris?
[85.74 --> 86.78]  I am doing okay.
[86.90 --> 87.92]  How's it going today, Daniel?
[87.96 --> 88.48]  What are you up to?
[88.94 --> 90.30]  It's been a long week.
[90.46 --> 94.62]  It helped my wife's business move, so I'm a little bit physically tired.
[94.84 --> 96.00]  But it's been a good week.
[96.24 --> 99.02]  Gave a virtual talk this morning, and that was fun.
[99.42 --> 103.98]  Actually, really good question and answer and back and forth.
[103.98 --> 104.76]  So I don't know.
[104.82 --> 106.46]  You never know with virtual talks.
[106.56 --> 108.32]  Sometimes they're super awkward.
[108.76 --> 110.08]  Sometimes they're all right.
[110.26 --> 112.68]  So this one was really good and interesting.
[113.04 --> 113.62]  What about you?
[114.02 --> 114.56]  Same kind of thing.
[114.62 --> 118.00]  I'm just migrating into virtual talks after just taking a few months off.
[118.28 --> 123.02]  And it's interesting as I've been watching different organizations, their different levels
[123.02 --> 126.60]  of adaptability in terms of their readiness to do that.
[126.76 --> 128.00]  So always fun.
[128.06 --> 128.46]  For sure.
[128.56 --> 129.12]  Very supportive.
[129.52 --> 131.94]  And hey, we had a milestone in our family this week.
[132.14 --> 132.40]  Really?
[132.40 --> 135.22]  Yeah, my wife became an American citizen.
[135.40 --> 135.86]  She's British.
[136.24 --> 136.84]  Oh, congratulations.
[136.84 --> 138.74]  As you know, she became an American citizen.
[138.76 --> 140.68]  Yeah, and pass on my congratulations to her.
[140.94 --> 141.34]  Absolutely.
[141.64 --> 142.80]  It was a big deal for us.
[143.14 --> 143.92]  Yeah, that's so awesome.
[144.00 --> 145.42]  That's a long process, man.
[145.50 --> 146.66]  It is a long process.
[146.92 --> 147.12]  Yeah.
[147.52 --> 149.72]  And she knows more American history than any of us.
[149.88 --> 151.54]  Probably more than all of us put together now.
[151.70 --> 152.66]  They test all that.
[152.70 --> 155.44]  All the things that we learned in third grade and promptly forgot.
[155.86 --> 156.72]  Oh, I forgot.
[156.96 --> 157.16]  Right.
[157.30 --> 158.88]  She's a pro at this point.
[159.18 --> 160.24]  That's awesome, man.
[160.72 --> 161.16]  Congratulations.
[161.16 --> 162.54]  That's so exciting.
[163.04 --> 163.68]  Thank you very much.
[164.08 --> 164.32]  Yeah.
[164.72 --> 166.68]  Well, this week, I'm pretty excited.
[166.90 --> 171.90]  There's sort of a gap in our discussions thus far on the podcast.
[172.20 --> 176.60]  We've talked about a lot of things, but there's still things we have not talked about, apparently.
[177.34 --> 181.36]  And every once in a while, I see something talked about, like, oh, we haven't talked about that yet.
[181.74 --> 182.96]  There's just so much to cover.
[182.96 --> 187.96]  So today we're going to be talking about adversarial examples and attacks.
[188.42 --> 197.86]  And we're privileged to have with us Jack Morris, who is a researcher at the University of Virginia and an incoming AI resident at Google.
[198.22 --> 198.70]  Welcome, Jack.
[199.22 --> 199.46]  Hi.
[199.54 --> 200.44]  It's great to be here.
[200.44 --> 201.08]  Yeah.
[201.18 --> 202.28]  Thank you for joining us.
[202.32 --> 204.04]  It's really, really great to have you here.
[204.50 --> 210.74]  You've done a lot of stuff already and you're working a lot in open source and there's a lot to discuss.
[210.88 --> 221.00]  But before we jump into all that, could you just give us a little bit of, you know, your background, how you got interested in AI and, you know, got eventually connected with Google?
[221.42 --> 221.96]  Yeah, sure.
[221.96 --> 229.78]  So I recently graduated from the University of Virginia and I studied computer science and math there.
[230.58 --> 234.28]  And while I was there, I did this internship at Google.
[234.52 --> 235.92]  Actually, it's kind of a funny story.
[236.46 --> 239.66]  Have you ever heard of Google FUBAR, that program?
[240.28 --> 241.52]  No, maybe I have not.
[241.86 --> 242.84]  I don't recall it.
[242.96 --> 243.84]  Tell us about it.
[244.20 --> 244.86]  FUBAR us.
[245.28 --> 245.54]  Okay.
[245.70 --> 246.58]  So I'll tell you the story.
[246.58 --> 251.68]  So basically, I was in my sophomore year of college at UVA.
[252.04 --> 253.24]  We call it second year.
[253.60 --> 254.56]  I was like that.
[254.72 --> 255.82]  So I was in my second year.
[256.14 --> 258.36]  I have this personal website I think I was working on.
[258.46 --> 262.90]  I was searching up something related to a software project I was working on on Google.
[263.50 --> 269.38]  So, like, I think what I typed in was something like Python, list comprehensions, something related to that.
[269.52 --> 270.38]  And I typed it in.
[270.56 --> 272.56]  And then it's hard to explain in audio.
[272.56 --> 275.24]  But basically, like, there's the search result page for Google.
[275.24 --> 276.74]  Like, all the results.
[277.42 --> 279.22]  And it kind of, like, animated.
[279.42 --> 281.22]  Like, it shrunk up and slid over.
[281.38 --> 282.84]  And then kind of, like, behind the search.
[283.22 --> 285.10]  Oh, I've heard of this.
[285.36 --> 286.26]  Like, there's a terminal.
[286.54 --> 287.28]  Yeah, yeah.
[287.42 --> 289.96]  It's like an Easter egg recruiting.
[290.42 --> 292.30]  Yeah, exactly.
[292.96 --> 293.90]  It's pretty funny.
[294.24 --> 297.52]  It's not, like, they don't send a lot of recruiters to my school or anything.
[297.62 --> 301.98]  So it was very, I guess, like, serendipitous for me that I got that pop-up.
[301.98 --> 305.60]  So it's, like, it's a terminal window behind the Google search page.
[305.74 --> 308.20]  It's, like, just like an Easter egg in a video game.
[308.20 --> 310.06]  And it says, we think you're speaking our language.
[310.16 --> 311.06]  Want to take a test?
[311.40 --> 312.68]  And then I click yes.
[313.22 --> 314.74]  And you make an account.
[314.84 --> 316.10]  There's this little website.
[316.30 --> 319.40]  It's just a console and a browser.
[319.94 --> 321.76]  And it's coding challenges.
[321.76 --> 323.94]  Like, now they have lead code and stuff like that.
[324.12 --> 325.72]  It's that kind of thing.
[325.76 --> 326.78]  And there's different levels.
[326.90 --> 328.00]  It gets progressively harder.
[328.00 --> 330.16]  I remember I was doing it for a few weeks.
[330.38 --> 334.90]  And a few of the problems were, they're not, like, interview coding problems where you kind
[334.90 --> 337.24]  of think for a while and then you get it and you can write it out.
[337.30 --> 341.04]  They took me, like, several days, I think, just to sort of figure it out and try and optimize
[341.04 --> 341.64]  it and stuff.
[341.84 --> 344.26]  And I got to, like, level four.
[344.62 --> 347.02]  And then I just couldn't figure one out.
[347.84 --> 349.98]  I was so excited seeing when I got it.
[350.18 --> 351.34]  And I was kind of bummed.
[351.46 --> 353.48]  But I just couldn't figure this problem out.
[353.74 --> 356.00]  And they all have these really long write-ups.
[356.00 --> 357.66]  It was something to do with rabbits.
[358.08 --> 361.00]  And there are all these allocations of rabbit holes.
[361.14 --> 362.14]  And they were storing things.
[362.24 --> 366.20]  And it was, like, a hard problem and a really confusing write-up.
[366.30 --> 367.46]  And then I just kind of gave up.
[367.98 --> 372.72]  And then I guess it turned out you didn't have to, you know, solve all the problems to
[372.72 --> 373.22]  get an interview.
[373.36 --> 374.34]  And I got an interview.
[374.58 --> 375.58]  And I did an internship.
[376.34 --> 378.74]  So that's how I originally got connected with Google.
[378.96 --> 383.40]  And then more recently, I applied to this program called the AI Residency and did some
[383.40 --> 384.34]  interviews for that.
[384.34 --> 391.88]  And my eventual goal is to get a PhD, hopefully, in something related to computer science, artificial
[391.88 --> 393.20]  intelligence, linguistics.
[393.72 --> 395.00]  Not that sure yet.
[395.50 --> 402.94]  But next year, I'm doing this one to 1.5-year fellowship thing at Google, which will be really
[402.94 --> 403.26]  awesome.
[403.34 --> 405.74]  It's just a research internship, basically.
[405.74 --> 411.80]  And as to the question of how I got interested in AI, originally, I was really interested in
[411.80 --> 413.96]  just some things on the application side.
[414.22 --> 417.72]  They're all pretty pertinent to NLP, but I didn't really know at the time.
[418.08 --> 422.50]  I think my original idea was I worked on a few different open source projects.
[422.50 --> 427.44]  And I wanted to make a website that aggregates, like, medical literature.
[427.44 --> 433.10]  Like, it seemed like there's all this research that's just open online on Google Scholar.
[433.26 --> 438.34]  But it's pretty hard for the average person to, you know, sift through and aggregate and
[438.34 --> 438.92]  summarize.
[439.26 --> 441.24]  There's all these sort of, like, data processing.
[441.64 --> 442.04]  What do you call it?
[442.04 --> 443.38]  Information retrieval tasks.
[443.38 --> 449.42]  And so I thought I was wrong about, I guess, like, how far along we are in solving some
[449.42 --> 450.52]  different NLP stuff.
[450.60 --> 454.82]  Like, I thought that would be sort of like a plug-and-play type of deal, at least on a
[454.82 --> 458.46]  small scale for certain types of research and things.
[458.64 --> 460.32]  And I've tried it for a little bit.
[460.36 --> 465.72]  And I remember I tried this thing two and a half years ago was when I first started getting
[465.72 --> 466.40]  answers in AI.
[466.40 --> 471.60]  And I tried to use these skip thought vectors to encode sentences.
[471.60 --> 475.48]  And what is a skip thought vector, just for those of us who don't know?
[475.94 --> 477.54]  Yeah, it's one way.
[477.68 --> 481.08]  It's now, I guess, it's no longer kind of like a state-of-the-art method.
[481.08 --> 485.94]  But it's a way to take a sentence and encode it into a vector so that you can compare that
[485.94 --> 489.04]  vector to other sentences to see if they're similar or dissimilar.
[489.22 --> 489.44]  Gotcha.
[489.56 --> 494.64]  And then I kind of was slowly realizing, basically, like, wow, these things, not that it didn't
[494.64 --> 498.20]  work, but that, I don't know, there's just still a lot of problems to be solved.
[498.28 --> 500.56]  And I got interested in some more specific stuff.
[500.56 --> 505.66]  And then most recently, I've been working on this idea of, like, robustness or, yeah,
[505.82 --> 508.16]  like, the security side, almost.
[508.40 --> 513.22]  Like, kind of like trying to find flaws in NLP models the same way that people are interested
[513.22 --> 515.58]  in finding them for computer vision models, specifically.
[515.94 --> 516.14]  Yeah.
[516.44 --> 520.04]  Which is, the buzzword is, like, adversarial examples.
[520.62 --> 525.92]  And it's kind of, a lot of people debate whether or not that's really applicable terminology
[525.92 --> 526.54]  to NLP.
[526.54 --> 527.70]  We can get into that later.
[527.82 --> 531.22]  But anyways, that's the kind of field that I've been interested in recently.
[531.80 --> 531.98]  Yeah.
[531.98 --> 537.78]  I remember, and I think I've mentioned, actually, the same episode of a different podcast on
[537.78 --> 538.90]  this podcast before.
[539.04 --> 544.98]  But the NLP Highlights podcast, which I listened to, they had an episode about behavioral testing
[544.98 --> 548.26]  of NLP models with Marco Rubiro.
[548.68 --> 554.22]  And he was talking about these tests that he did, which were really, like, right along the
[554.22 --> 555.40]  lines of what you're talking about.
[555.40 --> 562.50]  Like, you know, if you have a sentiment analysis example that's like, I love the United States,
[562.56 --> 563.68]  it's great, or something.
[564.24 --> 566.70]  That's a timely example right there, given my family.
[566.86 --> 567.32]  Yeah, yeah.
[567.74 --> 572.30]  And you put that into, like, the commercial, like, offerings for sentiment analysis, like,
[572.36 --> 573.84]  products that are being sold, right?
[574.28 --> 575.18]  And so you do that.
[575.18 --> 579.44]  And then you just switch out the, like, United States and put in, like, Turkey.
[579.62 --> 581.50]  I love Turkey, and it's great, right?
[581.90 --> 586.84]  It'll actually, like, break the system, and you won't get positive sentiment anymore.
[587.06 --> 594.08]  Just because, like, so much in the training is, like, biased against, like, Turkey for whatever
[594.08 --> 594.56]  reasons.
[594.98 --> 595.94]  So, yeah, I don't know.
[596.04 --> 598.68]  Is that kind of what you're talking about with adversarial?
[598.76 --> 602.68]  Maybe we should just back up a second and think about, like, adversarial examples in general.
[602.68 --> 606.78]  What do people generally mean when they're talking about adversarial examples?
[607.38 --> 612.72]  So, the first people that were researching adversarial examples were all based around, like,
[612.86 --> 616.48]  convolutional neural networks and images specifically.
[617.18 --> 623.72]  And you guys have probably seen the examples where you can take an input image that's classified
[623.72 --> 629.14]  correctly, say, for some image net classifier, classifying different animals.
[629.14 --> 633.32]  You know, there's a picture of a panda, and it says, okay, this is a panda.
[633.60 --> 635.54]  I'm 99.8% confident.
[636.08 --> 641.20]  And then, basically, they uncovered these sort of, like, blind spots in the really high dimensional
[641.20 --> 644.80]  input space that point to other classes.
[645.18 --> 648.18]  And there's a lot of different research into why that exists.
[648.36 --> 657.02]  But if you add a small, tiny little image onto the panda image, so it's so small you can't
[657.02 --> 658.26]  even notice it with your eye.
[658.34 --> 662.92]  It's maybe a pixel or two pixels out of 255.
[663.40 --> 664.34]  You add it to the panda.
[664.46 --> 668.56]  You end up with an image that, to a human, can't be distinguished from the first image.
[668.76 --> 674.14]  But if you add noise in the correct direction, it's totally misclassified into some other
[674.14 --> 674.48]  class.
[674.48 --> 677.64]  So I think the quintessential example is, like, the panda.
[677.92 --> 682.78]  And then you add this tiny little delta, a small image, and then it becomes a given with,
[682.90 --> 688.52]  you know, 99.8% misclassification confidence, which is crazy.
[688.74 --> 689.66]  And it's a big problem.
[689.86 --> 694.44]  And it's become, I think that's one of the hotter areas of research in ML.
[694.60 --> 698.70]  I'd say there's all these people trying to figure out why that's happening, trying to propose
[698.70 --> 700.48]  different defenses for it.
[700.48 --> 705.86]  There's some pretty cool attacks and defenses, I think, in the real world.
[706.18 --> 714.08]  Like, I saw people that are trying to evade facial recognition detectors wear these special
[714.08 --> 714.52]  shirts.
[714.68 --> 715.80]  Have you all seen those?
[716.14 --> 716.76]  Or sweaters?
[716.90 --> 717.16]  Yeah.
[717.38 --> 721.98]  That are patterned in a certain way that convince the camera that they're not a person or they
[721.98 --> 725.60]  just totally distorts their facial recognition software.
[726.10 --> 726.82]  It's pretty cool.
[727.58 --> 730.20]  And so that's a really hot area of research.
[730.20 --> 735.28]  It's like adversarial examples with convolutional neural networks or other image processing deep
[735.28 --> 735.98]  learning models.
[736.66 --> 741.32]  And then naturally, one would wonder, like, whether that exists for text.
[741.52 --> 742.84]  And if so, what that would be.
[743.06 --> 745.48]  And it turns out it's not as cut and dry.
[745.64 --> 749.16]  It's like kind of a hotly debated and somewhat murky concept.
[749.16 --> 756.32]  But one hypothesis, like you talked about, is you can substitute words that maybe don't change the
[756.32 --> 758.16]  meaning with respect to the task.
[758.16 --> 764.24]  Like, in sentiment analysis, maybe if you substitute a noun for another proper noun, you could say
[764.24 --> 768.52]  that, or a proper noun for another proper noun, like substituting the United States for Turkey,
[768.88 --> 772.10]  should never really change the sentiment of any sentence.
[772.10 --> 772.44]  Right?
[772.44 --> 775.98]  And I think that's what he was talking about on that podcast.
[776.32 --> 781.14]  And kind of just tying in, you know, as you're talking about, you know, as you were tying into
[781.14 --> 785.52]  this direction, as you're talking about adversarial in the CNN context, the convolutional neural
[785.52 --> 790.10]  network context, what would be the motivation for doing it in the NLP context?
[790.22 --> 793.92]  Like, what are some of the things you could think of that people would be bothering to do that
[793.92 --> 794.12]  with?
[794.12 --> 797.02]  I'm just curious, what in your views might be some of the drivers there?
[797.30 --> 797.58]  Uh-huh.
[797.92 --> 803.44]  The first paper I wrote, which is on archive, it's called Re-evaluating Adversarial Examples
[803.44 --> 809.28]  in Natural Language, was trying to give sort of like a theoretical framework for different
[809.28 --> 811.06]  types of adversarial examples in NLP.
[811.52 --> 816.00]  The basic idea was like, okay, we don't have to agree on one set, but we can lay out some
[816.00 --> 818.08]  sets of constraints that you might agree on.
[818.18 --> 822.62]  Like, if you substitute a word for its synonym, it shouldn't change the prediction.
[822.62 --> 826.46]  That would be an example of like one partial definition of an adversarial example.
[827.10 --> 834.24]  So, and maybe this is having to do with like people in the convolutional neural network space,
[834.24 --> 841.62]  I think, talk a lot about like safety in terms of like why adversarial examples are worth
[841.62 --> 842.28]  exploring.
[842.62 --> 848.36]  Like from your perspective, since you've done this work in NLP, what makes exploring adversary
[848.36 --> 852.00]  examples for NLP, you know, interesting from your perspective?
[852.00 --> 856.18]  Is there a safety side of it or is it more like, you know, robustness?
[856.28 --> 857.98]  Like you were talking about robustness as well.
[858.96 --> 862.00]  Yeah, those are definitely two different things.
[862.48 --> 867.92]  Like if you're a company that's maybe putting some NLP model up on the internet, releasing
[867.92 --> 874.20]  it into production, on one hand, you want it to work in all sorts of cases and you don't
[874.20 --> 879.84]  want there to be some obvious gaping holes in its actual predictions, which would be sort
[879.84 --> 881.04]  of like the robustness angle.
[881.18 --> 884.76]  And on the other hand, you want it to be safe, right?
[884.80 --> 888.20]  You don't want people to be able to like manipulate it in some way.
[888.78 --> 894.38]  So the reason I brought up the paper was because it includes some specific examples like that,
[894.38 --> 899.06]  because I think there's, there's a decent amount of research, but not a lot of discussion
[899.06 --> 904.94]  about like why robustness is important in NLP or like you were asking what maybe the goals
[904.94 --> 907.14]  of an adversary would be in that situation.
[907.84 --> 914.62]  So I think one really easy one is there's these toxic comment classifiers that I think
[914.62 --> 916.26]  are actually in use right now.
[916.52 --> 922.48]  Definitely on Facebook, they have this whole system for deciding whether a comment is just
[922.48 --> 928.28]  totally quote unquote like toxic and needs to be flagged or discarded or hidden, or I don't
[928.28 --> 930.18]  know, you have to say you're eating to read it or whatever.
[930.18 --> 937.38]  And so if you're someone who, for whatever reason, thinks it would be a good idea to write
[937.38 --> 944.26]  a toxic comment and then avoid that sort of flagging system, that would be a pretty good
[944.26 --> 947.88]  example of when you like want to like run an attack on an NLP model.
[947.88 --> 950.54]  And you could actually use text attack for that.
[950.70 --> 951.56]  You should not.
[960.18 --> 972.10]  What up nerds?
[972.16 --> 974.02]  Jared Santo here, your humble producer.
[974.34 --> 976.38]  I'd like to tell you about something new.
[976.50 --> 978.30]  We're beta testing around practical AI.
[978.90 --> 982.56]  It's a membership program, which we think could be really valuable for the whole community.
[983.04 --> 987.86]  We call it ChangeDog++ and it's the best way to directly support practical AI and all
[987.86 --> 991.02]  of the podcasts, videos, and other stuff we create here at ChangeDog.
[991.42 --> 995.24]  We have big plans and ambitions for this, but we are experimenting for now to make sure
[995.24 --> 995.88]  there's interest.
[996.32 --> 1000.62]  That means when you sign up today, you get practical AI and whatever ChangeDog shows you
[1000.62 --> 1002.94]  listen to now, except no ads.
[1003.34 --> 1006.00]  I guess that means this part you're listening to right now, it'll be gone.
[1006.64 --> 1011.64]  We also have some extended episodes planned, bonus content, merch store discounts, and a lot
[1011.64 --> 1012.20]  of ideas.
[1012.42 --> 1016.88]  But since it's such early days, we are offering memberships at a 40% discount for early adopters.
[1016.88 --> 1019.10]  That disappears at the end of August.
[1019.38 --> 1024.28]  So head to ChangeDog.com slash plus plus to join today, lock in that discount, get closer
[1024.28 --> 1026.04]  to the metal, and make the ads disappear.
[1026.52 --> 1030.10]  Once again, that's ChangeDog.com slash plus plus.
[1030.30 --> 1032.78]  We'd love to have you supporting us as a member.
[1039.48 --> 1043.44]  So let's say that our model fails on an adversarial example.
[1043.78 --> 1045.64]  You know, what could we do to fix it by way?
[1045.64 --> 1047.64]  That's a great question, too.
[1048.00 --> 1050.04]  That's a pretty open area of research.
[1050.20 --> 1053.76]  I wouldn't say there's a great answer I can give you right on that.
[1053.94 --> 1059.90]  But the sort of naive approach is generate a bunch more adversarial examples and then
[1059.90 --> 1064.96]  retrain your model, either just on the adversarial examples or on the original training set and
[1064.96 --> 1067.70]  the adversarial examples concatenated together.
[1067.70 --> 1072.08]  And there's some research that's shown that gives you some improvements.
[1072.08 --> 1076.62]  But you can imagine, like, it's very different than the case of images.
[1076.98 --> 1082.32]  Like, for example, if your goal is to replace proper nouns with other proper nouns, right?
[1082.40 --> 1087.88]  Like replace every instance of the United States with Turkey, or more commonly, maybe try all
[1087.88 --> 1091.98]  the countries and pick the one that meets your goal the best.
[1091.98 --> 1095.02]  I think that you're getting into some interesting areas.
[1095.20 --> 1099.36]  One of the things that you started talking about was like generating adversarial examples
[1099.36 --> 1101.20]  for NLP models.
[1101.68 --> 1107.50]  So it's one thing to realize, I guess, realize that your model fails for a particular type
[1107.50 --> 1109.58]  of attack or something like that.
[1109.88 --> 1114.00]  It may be another thing like Chris was saying to like, say, okay, well, now what?
[1114.08 --> 1114.98]  How do I fix that?
[1115.24 --> 1115.46]  Yeah.
[1115.46 --> 1119.28]  And you're saying like, you could generate adversarial examples.
[1119.62 --> 1124.36]  I know that like some of your work and your open source work is geared towards generating
[1124.36 --> 1125.12]  those examples.
[1125.34 --> 1129.78]  But how in general, how do people come up with adversarial examples?
[1129.78 --> 1134.26]  Like, what is the range of things that people try to do to come up with these examples?
[1134.26 --> 1135.66]  Maybe specifically in NLP?
[1135.88 --> 1138.82]  Is it mostly hand curated data?
[1139.52 --> 1143.08]  Or is it like, what other things are out there to try?
[1143.08 --> 1147.74]  Yeah, again, it kind of depends on your definition of an adversarial example.
[1148.34 --> 1150.72]  Maybe we can talk about that briefly first.
[1151.14 --> 1151.24]  Sure.
[1151.48 --> 1152.06]  Yeah, that'd be great.
[1152.32 --> 1160.82]  I think that kind of lends a hand to why adversarial examples in NLP are not as well defined as in
[1160.82 --> 1161.60]  vision.
[1161.80 --> 1167.36]  Because if you have two images next to each other, it's very clear whether or not they're
[1167.36 --> 1172.94]  similar and whether the change from image one to image two could be classified as imperceptible.
[1173.08 --> 1181.14]  But if you have two sequences of text, there's no imperceptible change unless they're exactly
[1181.14 --> 1181.72]  the same.
[1182.22 --> 1188.34]  And so if you make a change, any sort of change that you might define as imperceptible becomes
[1188.34 --> 1189.82]  at least like a point of argument.
[1190.44 --> 1193.90]  So I'll tell you two really popular definitions.
[1193.90 --> 1198.04]  One would be with respect to semantics.
[1198.48 --> 1205.06]  So if you have sentence one, and then you replace some words with synonyms, or like you
[1205.06 --> 1211.10]  said with a proper noun, that should generally not change the semantics of the original input.
[1211.10 --> 1216.62]  And so you could say if you have two sentences, like if I have one that said, I love the movie
[1216.62 --> 1219.34]  Parasite, the best movie I've ever seen.
[1219.56 --> 1221.42]  And then I replaced a couple words.
[1221.50 --> 1226.66]  I said, I liked the movie Parasite, greatest movie I've ever seen.
[1227.36 --> 1232.26]  You could, a lot of people would say that's invariant with respect to semantics, like they
[1232.26 --> 1233.30]  contain the same meaning.
[1233.30 --> 1238.08]  So if they have different predictions, that would be classified as an adversarial example.
[1238.94 --> 1243.30]  And then the other thing that I was going to bring up, like another definition is with
[1243.30 --> 1245.52]  respect to like character level changes.
[1245.88 --> 1251.80]  So if instead, I just, like imagine a typo on the computer, basically, if instead of saying
[1251.80 --> 1258.40]  I love Parasite, I spelled love L-V-O-E-D or something like that, just switched around the
[1258.40 --> 1259.30]  characters a little bit.
[1259.30 --> 1264.50]  But it's actually really shocking how many state of the art NLP models will just totally
[1264.50 --> 1266.22]  mispredict that for whatever reason.
[1266.58 --> 1272.18]  And so those are sort of two competing, not necessarily totally mashed ideas of adversarial
[1272.18 --> 1272.64]  examples.
[1272.86 --> 1277.04]  One being with respect to like character level changes, or if you just insert a character
[1277.04 --> 1279.78]  like L-O-V-E-D-Q or whatever.
[1280.54 --> 1289.00]  Especially models that are based on this idea of like entire words have a lot of trouble dealing
[1289.00 --> 1290.90]  with those types of changes.
[1291.80 --> 1297.26]  So either one of those would probably be classified as an adversarial example by most people.
[1297.62 --> 1297.98]  Yeah.
[1298.14 --> 1301.58]  I'm kind of trying to think through like my own workflow right now.
[1301.70 --> 1307.26]  And so like in terms of integrating or making my models more robust, I guess, let's say I'm
[1307.26 --> 1308.72]  creating an NLP model.
[1308.96 --> 1316.08]  It's probably unlikely or it seems unlikely for me to sort of plug all the holes in terms
[1316.08 --> 1319.50]  of like things that my model might do that are unexpected.
[1319.94 --> 1320.50]  Right.
[1320.56 --> 1326.92]  But you're saying that maybe there's some sort of obvious things that we can protect against
[1326.92 --> 1332.90]  or make more robust, like with the typo sort of perturbation or maybe not changing the semantics
[1332.90 --> 1336.78]  or some type of like perturbations like this that we can test against.
[1336.78 --> 1341.66]  But then it's probably I don't know what are your suggestions in terms of like you can plug
[1341.66 --> 1347.80]  some holes, but then eventually your model might behave unexpected in in a new way that
[1347.80 --> 1350.30]  is totally unexpected because it's unexpected.
[1350.54 --> 1354.28]  It almost seems like unit testing software or something to me where it's like, you know,
[1354.28 --> 1357.14]  you test for the things that you definitely anticipate.
[1357.14 --> 1360.90]  But then at some point, something weird happens and you have to add a test case.
[1360.90 --> 1362.54]  Is that kind of how you would view it?
[1362.54 --> 1368.72]  Or how would you view like the workflow of like thinking about adversarial examples in
[1368.72 --> 1371.50]  developing a model as opposed to not thinking about them?
[1371.74 --> 1372.92]  I guess is where I guess.
[1373.10 --> 1373.94]  Yeah, yeah.
[1374.44 --> 1379.94]  That's a really pertinent question, I think, to anyone who's an engineer, you know, actually
[1379.94 --> 1383.12]  trying to build NLP systems for real people.
[1383.12 --> 1385.84]  And it's not it's not one that's totally solved yet.
[1385.84 --> 1393.36]  But another idea that I heard, I think Ian Goodfellow has gone to talks and advocated for
[1393.36 --> 1400.74]  this is the idea of if you're building a model, adding some kind of output that can identify
[1400.74 --> 1407.26]  whether an input is malformed or maybe doesn't fit with the distribution of the training data
[1407.26 --> 1407.72]  at all.
[1407.72 --> 1413.68]  So that in the case I indicated before might indicate, you know, a misspelling or some kind
[1413.68 --> 1418.56]  of really unnatural misspelling that a user would never produce, or maybe just a synonym
[1418.56 --> 1423.24]  substitution, like maybe using a word that might have the same meaning, but would almost never
[1423.24 --> 1427.66]  be used in that context by a real person, which is something I think I see a lot with
[1427.66 --> 1429.20]  these adversarial example papers.
[1429.66 --> 1434.58]  They might say, okay, if two words are synonyms in the thesaurus, they can always be substituted
[1434.58 --> 1435.22]  for each other.
[1435.22 --> 1439.34]  A lot of the time that might not be a very natural substitution or something that a human
[1439.34 --> 1441.18]  would probably never actually do.
[1441.88 --> 1448.74]  And so if you can train a model that has some way to indicate whether an input is sort of
[1448.74 --> 1453.66]  like acceptable or not, it can, I think, alleviate a lot of those concerns, though they're still
[1453.66 --> 1454.10]  there.
[1454.50 --> 1457.52]  I think in the general case, it would make your system a lot better.
[1457.52 --> 1461.88]  Yeah, so I mean, you know, I know you and Daniel do a lot of work in this area.
[1462.16 --> 1466.44]  And so I'm kind of approaching it as the one who's not actively doing models in NLP.
[1466.82 --> 1471.64]  If I'm understanding you correctly, it sounds like there's really a different set of use
[1471.64 --> 1475.16]  cases if you were to compare this to like adversarial and CNNs.
[1475.34 --> 1481.02]  Whereas, you know, that behavior is in some sense, often maybe nefarious, you know, trying
[1481.02 --> 1484.56]  to change a classification, you know, for some purpose.
[1484.56 --> 1488.60]  Whereas this, it sounds like, you know, you mentioned robustness earlier, and it sounds
[1488.60 --> 1493.74]  like there may be a lot of use cases where you're helping a user not make mistakes, where
[1493.74 --> 1499.56]  you're trying to prevent unexpected behavior, intentional or not, you know, in terms of like
[1499.56 --> 1501.04]  what the user was trying to do.
[1501.42 --> 1502.42]  Do you think that's fair?
[1502.56 --> 1507.52]  Do you think that the types of use cases that this might be applied to are fairly different,
[1507.58 --> 1508.20]  it sounds like?
[1508.70 --> 1509.58]  Yeah, absolutely.
[1509.58 --> 1516.88]  And I really liked the comparison that you made of comparing like finding adversarial
[1516.88 --> 1523.24]  examples for NLP models to some sort of unit testing in the software engineering spectrum.
[1523.74 --> 1527.24]  And that's what the paper that I think he's talking about, the checklist paper, that's
[1527.24 --> 1533.76]  what they talk about is applying ideas from software engineering to verifying the usefulness
[1533.76 --> 1535.14]  of NLP models, essentially.
[1535.14 --> 1541.02]  And I think that's a lot closer to what adversarial examples are in NLP and how they're useful
[1541.02 --> 1542.98]  to maybe how they are in CNNs.
[1543.52 --> 1548.42]  So I could imagine not far down the road as some of this work is realized that, you know,
[1548.44 --> 1554.32]  maybe for programmers, their IDEs or text editors, you know, kind of get some modules that help
[1554.32 --> 1558.50]  them from in terms of essentially unit testing what they're doing in a smart way.
[1558.50 --> 1563.34]  Or even for just someone who's not technical, a word processor might have this capability
[1563.34 --> 1568.20]  built in so that, you know, when you're writing, you're making fewer mistakes in that way.
[1568.26 --> 1571.60]  So it sounds like there's a lot of help the human possibilities here.
[1572.06 --> 1576.94]  Yeah, it would probably be more, I guess, on the data side or the training data side.
[1577.10 --> 1584.46]  So like if you see a unexpected behavior in your autocomplete in your text editor or whatever,
[1584.46 --> 1586.74]  like why was that unexpected?
[1586.74 --> 1594.78]  Did you like give the model like some type of weird, like malformed input that like caused
[1594.78 --> 1597.62]  it to just like totally fly off the rails?
[1597.98 --> 1598.14]  Yeah.
[1598.26 --> 1601.10]  And so then it's like, OK, well, why did that misbehave?
[1601.10 --> 1604.74]  So now we've got to add some things into our training data.
[1604.84 --> 1609.82]  So I know I definitely want to get to this open source project, Text Attack, which I actually
[1609.82 --> 1613.24]  came across in my one of my newsletters.
[1613.24 --> 1617.70]  I forget it was like one of the NLP newsletters mentioned it.
[1617.88 --> 1619.28]  So I forget which one it was.
[1619.40 --> 1620.62]  I'll have to look up while we're talking.
[1621.10 --> 1622.04]  But yeah, it seems really cool.
[1622.14 --> 1623.82]  So was this open source project?
[1623.98 --> 1626.54]  Maybe you could talk a little bit about how that came about.
[1626.62 --> 1631.30]  Was it because you were trying to like you were in this workflow and you were like trying
[1631.30 --> 1637.44]  to add adversarial examples and it was like there just wasn't tooling around it?
[1637.44 --> 1638.56]  Or how did that come about?
[1639.02 --> 1640.32]  Yeah, you kind of nailed it.
[1640.32 --> 1646.50]  So I was working on things related to trying to find adversarial examples in NLP.
[1647.24 --> 1652.46]  And like I said, there's a lot of kind of like disagreement on what counts.
[1653.04 --> 1659.82]  And there's been a decent amount of research into this idea, but it's not very homogenous.
[1660.32 --> 1662.32]  It's actually pretty disorganized, I'd say.
[1662.32 --> 1670.06]  And a lot of people have really similar ideas, but they change one or two things, but they
[1670.06 --> 1676.04]  reuse a lot of ideas and all their code and projects are generally implemented in different
[1676.04 --> 1676.44]  places.
[1676.76 --> 1681.18]  So it's kind of a headache trying to reimplement results and compare things.
[1681.18 --> 1687.28]  But it turned out that like a lot of the people that suggested NLP attacks were using a lot of
[1687.28 --> 1689.44]  the exact same components.
[1689.94 --> 1694.44]  So one example is like the thesaurus I was talking about before.
[1694.70 --> 1698.00]  So have you all heard of Glove word vectors?
[1698.62 --> 1699.92]  Yeah, from Stanford, right?
[1700.36 --> 1701.58]  Yeah, from Stanford.
[1701.58 --> 1707.70]  A few years ago, those are still pretty much top of the line word vectors you can download.
[1707.70 --> 1713.00]  So basically, they're more commonly called word embeddings, you can download this big matrix
[1713.00 --> 1718.66]  that's assigned to, I don't know, 100,000 or a million words from English, and each one
[1718.66 --> 1719.80]  has their own word embedding.
[1720.40 --> 1724.32]  And it's a vector of dimensionality, maybe 300.
[1724.72 --> 1728.02]  And they're supposed to encapsulate a lot of information about English.
[1728.62 --> 1734.16]  So if you're training an NLP model, the initial layer is probably going to use an embedding
[1734.16 --> 1734.98]  similar to that.
[1734.98 --> 1741.12]  And Glove is kind of like the just very accepted word vector a lot of people use, at least before
[1741.12 --> 1744.18]  people started using transformers and subwords.
[1744.94 --> 1752.64]  But there's this paper that made these amendments to the Glove vectors, so that they more directly
[1752.64 --> 1755.28]  encapsulate information from a thesaurus.
[1755.84 --> 1760.68]  So it's called, they're called counterfeited vectors, not spelled like you would think, like
[1760.68 --> 1761.86]  counterfeited.
[1761.86 --> 1768.92]  And they basically if you compare two synonyms based on their counterfeited word embeddings,
[1768.92 --> 1773.24]  they should be very similar in terms of their angle, like cosine similarity.
[1773.84 --> 1778.60]  And antonyms should be very dissimilar, like they should have angles close to 180 degrees.
[1778.94 --> 1785.32]  So it's basically just Glove vectors plus this pre processing step that uses a big list of synonyms
[1785.32 --> 1789.64]  and a big list of antonyms to try and make those vectors closer and further apart.
[1790.10 --> 1796.04]  And I bring this up because a lot of people that have created systems that develop adversarial
[1796.04 --> 1801.06]  examples in NLP use this base layer of counterfeited vectors.
[1801.06 --> 1808.00]  So if you take the example I talked about before, like I loved the movie Parasite, and you could
[1808.00 --> 1814.12]  look at the word vector, the counterfeited word embedding for loved, and then look at its nearest
[1814.12 --> 1816.32]  neighbors in the counterfeited embedding space.
[1816.70 --> 1822.26]  And you might see a bunch of words that fit in the same context and are actually synonyms.
[1822.26 --> 1825.68]  So loved, liked, I don't know, enjoyed.
[1826.30 --> 1831.34]  And then once you start to deviate in terms of that angular similarity, then they get less
[1831.34 --> 1831.96]  and less similar.
[1832.42 --> 1836.52]  And there's some debate as to, you know, how similar do they have to be to be synonyms like
[1836.52 --> 1839.94]  0.9 or 0.95, you know, which is a whole nother thing.
[1840.28 --> 1846.80]  But all these attacks use those counterfeited word embeddings, like maybe over 10 papers use
[1846.80 --> 1851.56]  counterfeited word embeddings and maybe some other components that are exactly the same to
[1851.56 --> 1853.62]  generate adversarial examples.
[1854.38 --> 1859.04]  And even stepping back from that, the entire process for generating adversarial examples
[1859.04 --> 1861.26]  in NLP is very, very similar.
[1861.60 --> 1867.54]  So by the process, I mean the process of taking a text input, so a sequence of words, and then
[1867.54 --> 1871.80]  producing some other sequence of words that generally like fools a model.
[1871.80 --> 1877.86]  So taking maybe the sentiment classification example, you have an input that's classified as
[1877.86 --> 1878.28]  positive.
[1878.94 --> 1884.72]  And the process of finding an adversarial example would be, which words can I substitute that will
[1884.72 --> 1886.62]  change this classification to negative?
[1887.24 --> 1890.40]  And so that turns into a combinatorial search problem.
[1890.92 --> 1896.50]  And most people do it in the exact same way and often use the same word vectors.
[1896.50 --> 1902.56]  And then, I don't know, change a few different things and then release their attack.
[1902.70 --> 1908.80]  So our idea was if we break that process down into components, then we can construct the attacks
[1908.80 --> 1911.16]  from different papers based on these components.
[1911.16 --> 1916.14]  So you've definitely captured me in terms of interest in adversarial attacks.
[1916.30 --> 1921.62]  And so let's say that I'm out there and I'm listening to this or I've just come across
[1921.62 --> 1922.76]  text attack.
[1923.02 --> 1928.70]  Can you tell me, kind of just describe the library, let me know what I should know about
[1928.70 --> 1931.24]  it as a beginner coming into it that wants to use it?
[1931.66 --> 1936.06]  And what are the goals that I should keep in mind that the project tackles?
[1936.06 --> 1941.26]  Are there any things that I should not address as well with this library that I'd look elsewhere?
[1941.82 --> 1943.64]  So can you kind of give me that beginner perspective?
[1944.26 --> 1945.10]  Yeah, absolutely.
[1945.64 --> 1950.86]  So it might help for me to talk real quickly about that kind of like system I was talking
[1950.86 --> 1952.56]  about, like the components.
[1953.24 --> 1959.08]  And then I can explain the most common use cases because obviously you can pull out any
[1959.08 --> 1961.94]  one of the components and use them for your own purposes.
[1961.94 --> 1966.98]  So one thing that we really focused on in text attack is trying to make it work out of
[1966.98 --> 1967.46]  the box.
[1968.04 --> 1974.48]  So for example, those counterfeited word embeddings, instead of, you know, going to this website,
[1974.78 --> 1980.86]  downloading it, unzipping it, moving it, finding out how to load all the data, you just import
[1980.86 --> 1986.00]  text attack and do text attack dot the class and just initialize it and it'll download everything
[1986.00 --> 1989.28]  for you, which I think is that is really cool.
[1989.28 --> 1995.46]  If you guys know about hugging face transformers, we're, I mean, a lot of the text attack stuff
[1995.46 --> 1999.80]  is built around transformers and tokenizers and now this data set loading library called
[1999.80 --> 2002.14]  NLP, which I'm very grateful for.
[2002.34 --> 2004.42]  And we kind of tried to follow the same model.
[2004.54 --> 2010.32]  So instead of having all these files, you manipulate yourself, you pretty much just reuse
[2010.32 --> 2013.68]  other people's, you know, and it saves a lot of time.
[2013.68 --> 2018.80]  Um, so the easiest or probably most common way that I would imagine people use text attack
[2018.80 --> 2024.52]  down the line is for things like that for the embeddings or another very common thing
[2024.52 --> 2028.42]  is sentence encodings, which is something I mentioned at the beginning of this talk.
[2028.86 --> 2033.94]  Like there's so many different methods for taking a sentence and encoding it into a fixed
[2033.94 --> 2034.58]  length vector.
[2034.58 --> 2039.60]  Whether they're very effective or not as a question, but they're useful in a lot of situations.
[2040.36 --> 2045.70]  And so one thing text attack has done is just sort of extracted them into classes that work
[2045.70 --> 2046.84]  by themselves.
[2046.84 --> 2051.26]  And so you could just, for example, if you were doing some project, I don't know, you
[2051.26 --> 2056.58]  wanted to look at a bunch of Airbnb reviews and cluster them based on which ones were similar.
[2056.58 --> 2061.70]  You could just import text attack and then just called like this sentence encoder dot
[2061.70 --> 2065.98]  encode and then give it the list and it would just do it for you, which I think is pretty
[2065.98 --> 2066.54]  valuable.
[2067.02 --> 2069.78]  So I'll tell you what the components are very quickly.
[2070.02 --> 2075.16]  There's, there's four and we have our own names for them, which I think increases the learning
[2075.16 --> 2079.12]  curve a little bit, but there's some benefits I think to having our own terminology.
[2079.48 --> 2085.68]  So it's all based around this idea of the NLP attack as a system, which is taking the text
[2085.68 --> 2091.66]  input, looking for changes you can make to it, making sure those changes are acceptable.
[2092.32 --> 2096.76]  And then whenever you have decided you fool the model, you stop.
[2097.20 --> 2102.70]  So the first component would be like the, what we call the transformation, which is taking
[2102.70 --> 2105.92]  an input and changing some of the words or characters.
[2106.18 --> 2110.46]  Like one transformation would be substituting words with their counterfeited word embedding
[2110.46 --> 2110.78]  acres.
[2110.78 --> 2116.82]  And then once you do that transformation step, there's also this idea of a constraint, which
[2116.82 --> 2119.52]  is trying to make sure you didn't make any mistakes.
[2119.98 --> 2123.02]  So like a common constraint is used to sentence encoder.
[2123.22 --> 2128.14]  A popular one is called the universal sentence encoder, which is by some folks at Google and
[2128.14 --> 2130.42]  you encode the original input.
[2130.42 --> 2135.02]  And now your potential adversarial example and make sure that the sentence encoder also
[2135.02 --> 2136.10]  says they're very similar.
[2136.36 --> 2140.82]  It's basically like a sanity check to make sure you didn't change the meaning or whatever,
[2141.36 --> 2144.04]  change too many characters if that's what you decide.
[2144.70 --> 2146.34]  And then there's two other components.
[2146.52 --> 2148.52]  So we have the transformation and the constraints.
[2149.34 --> 2153.18]  And you have to define your notion of whether you fooled the model or not.
[2153.56 --> 2159.32]  A common thing would just be change the classification output or change the classification output to
[2159.32 --> 2160.24]  a specific class.
[2160.34 --> 2162.86]  Those would both be examples of what we call the goal function.
[2162.86 --> 2169.28]  I think a really cool one that I want to explore more in the future is with sequence-to-sequence
[2169.28 --> 2175.36]  models, like a machine translation model, your goal might be to take the original output
[2175.36 --> 2178.32]  translation and change as many characters as possible.
[2178.94 --> 2184.44]  So say you're translating a sentence into French, you would have your original translation.
[2184.44 --> 2189.86]  And if you could substitute a word from the input with a synonym, and then it produced a translation
[2189.86 --> 2195.62]  that was totally different, even just in terms of characters or its blue score, that would be pretty
[2195.62 --> 2198.78]  telling and probably very bad for your translation system.
[2199.16 --> 2200.76]  So that would be another goal function.
[2200.86 --> 2202.76]  It would be trying to minimize the blue score.
[2203.36 --> 2205.76]  And then the last component is called the search method.
[2205.92 --> 2209.44]  And that's basically like if you have the input and you have all these transformations,
[2209.44 --> 2215.64]  how do you decide which one to keep, which is important because if you just tried all the
[2215.64 --> 2223.40]  combinations, I mean, if you have an input of 10 words and each word has 50 neighbors, you end up with
[2223.40 --> 2232.22]  50 times 50 times 50 possible substitutions that you might want to combine so that the space grows
[2232.22 --> 2233.46]  exponentially very quickly.
[2233.46 --> 2238.72]  So you have to come up with some sort of like greedy or approximate heuristics for doing that.
[2238.72 --> 2240.06]  And that's what we call the search method.
[2240.64 --> 2246.80]  So you can combine those four things into an attack, like an NLP, what we call an attack,
[2246.92 --> 2252.58]  which is just a search for adversarial examples that meet the constraints and fool the model
[2252.58 --> 2254.22]  as defined by the goal function.
[2255.14 --> 2258.72]  But there's some really cool other things that come off of that.
[2258.84 --> 2263.62]  A big one that I've been talking to people about recently is data augmentation, which is also
[2263.62 --> 2268.00]  a very kind of, I would say, under research field in NLP.
[2268.00 --> 2271.00]  It's another thing that is pretty commonplace in vision.
[2271.20 --> 2273.28]  It's almost like everyone does it.
[2273.46 --> 2279.12]  You know, if you want to train a state of the art vision model on CIFAR 10 or ImageNet or some
[2279.12 --> 2283.82]  other data set, you're going to do some sort of augmentation to change and increase the
[2283.82 --> 2284.78]  size of your data set.
[2285.20 --> 2290.60]  So with text attack, if you have this transformation, which can find maybe like semantics preserving
[2290.60 --> 2295.78]  changes to your input, and you could add on constraints, which make sure that they preserve
[2295.78 --> 2301.18]  semantics, then you can end up with like some pretty good tools for data augmentation just from
[2301.18 --> 2301.94]  those two things.
[2301.94 --> 2307.36]  And since we're trying to implement more components that would hopefully grow the list of potential
[2307.36 --> 2309.44]  augmentation modules as well.
[2310.18 --> 2313.22]  And so yeah, that's something I'm really excited about is the data augmentation.
[2313.22 --> 2314.86]  Yeah, that's really awesome.
[2315.06 --> 2320.56]  I know that even in speech, it's fairly common to, you know, like mask out, you know, parts
[2320.56 --> 2326.48]  of a spectrogram or like speed up or slow down the audio or something.
[2326.48 --> 2328.78]  And that's like fairly common component.
[2329.30 --> 2334.22]  But in NLP, it's pretty much most of the time where it seems like people are talking about,
[2334.34 --> 2337.08]  oh, we have this parallel data, we have this monolingual data.
[2337.08 --> 2340.64]  And that's like basically it, like that's all you have.
[2340.82 --> 2343.34]  And like you could augment with monolingual data.
[2343.48 --> 2347.86]  But you know, this is like another, it's another route to that, which is pretty cool.
[2348.00 --> 2353.30]  In terms of like the open source, I mean, there's been interest in the library.
[2353.70 --> 2355.56]  And what is your vision for it going forward?
[2355.62 --> 2359.58]  Do you see like others, you mentioned like hugging face transformers and kind of modeling
[2359.58 --> 2360.84]  certain things after that.
[2361.20 --> 2365.72]  And I know one of the things that they talk about a lot is, you know, people contributing
[2365.72 --> 2368.14]  models to their their model hub.
[2368.26 --> 2368.54]  Right.
[2368.94 --> 2374.76]  And actually, it's good timing because we had Sasha Russ from hugging face on his episode
[2374.76 --> 2375.74]  was released this week.
[2375.74 --> 2378.80]  So that's a great, great model that they're going.
[2378.94 --> 2384.72]  So I could see similar things happening here where it's like, you know, there's a new type
[2384.72 --> 2389.72]  of perturbation or goal function or something like you were saying that people are exploring.
[2389.94 --> 2395.08]  Do you envision people kind of like having a way to contribute those models in or like,
[2395.08 --> 2399.88]  what is your thought process around how you see the future of the library evolving?
[2400.52 --> 2401.90]  Yeah, that's a great question.
[2402.00 --> 2406.40]  And something I'm still, you know, we're still kind of discussing and trying to figure out
[2406.40 --> 2408.34]  because we've written a lot of code.
[2408.34 --> 2412.38]  And there's a lot of different features that still could be connected.
[2412.78 --> 2417.50]  And obviously, once you work on a library for a while, there's just so many improvements
[2417.50 --> 2418.32]  you want to make to it.
[2418.32 --> 2422.08]  You know, I have this giant list and take my whole life.
[2422.44 --> 2422.60]  Right.
[2423.28 --> 2429.56]  But I think I could probably break the potential users down into three groups, at least three
[2429.56 --> 2430.08]  main groups.
[2430.18 --> 2434.20]  So the first one would be kind of what I mentioned before, what I imagine would eventually be
[2434.20 --> 2439.82]  just the most common general use case would be using the components because they're easy
[2439.82 --> 2440.28]  to use.
[2440.28 --> 2447.04]  But the second one would probably be, like you said, people who want to work on researching
[2447.04 --> 2448.76]  the robustness of NLP models.
[2448.94 --> 2453.32]  So maybe coming up with new goal functions or trying a new transformation.
[2453.74 --> 2458.80]  Like, for example, I don't know if you created a model that could paraphrase inputs.
[2459.00 --> 2461.02]  It's a totally open problem in NLP.
[2461.22 --> 2464.84]  But even if you could do it a little bit well, I think that would be really interesting.
[2464.84 --> 2471.48]  Like taking that input sentence and just paraphrasing it or paraphrasing its individual sentences
[2471.48 --> 2474.58]  and trying those different pieces and seeing which one fools the model.
[2474.96 --> 2475.76]  That would be someone.
[2476.28 --> 2478.72]  And that would be a really cool thing for someone to research.
[2478.88 --> 2482.90]  And that would be just a new transformation, basically, that just takes an input and paraphrases
[2482.90 --> 2483.34]  it.
[2483.82 --> 2488.28]  And then the third use case would probably be people who actually want to test and potentially
[2488.28 --> 2494.18]  improve their models using text attack, which is what we added this summer is what I mentioned
[2494.18 --> 2499.80]  before, adversarial training based on just doing an attack and then increasing the size of
[2499.80 --> 2502.44]  the training set and continuing training.
[2503.20 --> 2509.08]  So hopefully people would be able to import text attack and then test out the robustness
[2509.08 --> 2514.72]  of their maybe summarization model or translation model or whatever, and get some insights into
[2514.72 --> 2519.18]  maybe how it's failing in the common cases and hopefully how they can improve it.
[2519.62 --> 2523.54]  Yeah, I got to note that as you're talking there, I'm looking through the GitHub repo.
[2523.54 --> 2527.26]  And you really put it together well for someone like me who is new to this.
[2527.64 --> 2532.04]  You know, you cover the kind of what it is, you know, the Slack channel, help with setup.
[2532.38 --> 2536.14]  Then you have a good section on usage and running attacks there.
[2536.32 --> 2540.76]  And then the thing I love the most is I love your section at the bottom on attack recipes.
[2541.26 --> 2541.50]  Oh, yeah.
[2541.86 --> 2542.10]  Yeah.
[2542.16 --> 2543.84]  I mean, and I was flipping through the links here.
[2543.90 --> 2547.92]  You're listing these different recipes for attack modes.
[2547.92 --> 2553.36]  And you link off to the paper or website where it shows what it is and how to do it in detail.
[2553.64 --> 2557.74]  And then with the section above it on usage, it makes it really easy to just go ahead and
[2557.74 --> 2558.28]  give it a shot.
[2558.44 --> 2561.86]  So after we're done with our conversation, I have a feeling I'm going to geek out on this
[2561.86 --> 2562.36]  for a little while.
[2562.46 --> 2564.04]  So thank you very much for that.
[2564.70 --> 2565.06]  Awesome.
[2565.06 --> 2569.68]  Do you envision more contributions being made to this attack recipe section?
[2570.48 --> 2572.30]  Yeah, I sure hope so, man.
[2573.28 --> 2580.28]  There's still papers that I think we could implement with pretty low effort because they have a
[2580.28 --> 2582.88]  lot of overlap with the components we've already implemented.
[2583.48 --> 2587.68]  Well, talking about vision, there are a few very common libraries in vision.
[2587.80 --> 2589.38]  One's called Cleverhans.
[2590.16 --> 2593.44]  No other names are coming to mind, but I know there's one by IBM.
[2593.44 --> 2594.78]  One called Foolbox.
[2595.46 --> 2601.14]  And those are pretty standard tools for researchers that are interested in the robustness of computer
[2601.14 --> 2601.84]  vision models.
[2602.54 --> 2609.16]  So not even that I'm super convinced that text attack will be that tool, but I'm hoping that
[2609.16 --> 2613.20]  just putting everything in one place would make it a lot easier for people to actually
[2613.20 --> 2619.42]  do that research and make fair comparisons and advance the field.
[2619.42 --> 2623.94]  So hopefully getting people actually excited about it by making these things easy to use
[2623.94 --> 2627.12]  will then lend a hand to people actually contributing.
[2627.38 --> 2628.00]  That's the goal.
[2628.36 --> 2633.94]  We've been working on this since almost a year ago, about a year ago, but it's only been open
[2633.94 --> 2635.16]  source since May.
[2635.42 --> 2637.54]  So hopefully that'll come with time.
[2638.42 --> 2642.44]  But yeah, right now, I think one of the recipes was implemented by the authors and then the rest
[2642.44 --> 2643.58]  we've kind of did by hand.
[2643.58 --> 2650.98]  So yeah, no, I think that this is so well set up and a lot of thought has been put into
[2650.98 --> 2651.26]  it.
[2651.34 --> 2656.42]  I'm like thinking back to the code that I wrote in academic research.
[2656.42 --> 2660.76]  And the reason why it brought me back there, because you have a little logo of or a little
[2660.76 --> 2663.42]  octopus emoji on text attack.
[2663.42 --> 2668.92]  And the code that eventually I implemented my method in in my PhD was called octopus.
[2669.24 --> 2675.58]  But I have no like I don't know that anyone would be able to run my module of octopus just
[2675.58 --> 2681.92]  because like, you know, it was nothing near well documented like this or anything like
[2681.92 --> 2682.16]  that.
[2682.22 --> 2687.30]  So I hope that you do get contributions as we kind of end up here.
[2687.40 --> 2689.76]  I guess I'm curious just as kind of a last question.
[2689.76 --> 2695.34]  And you've done this research, but you're also kind of launching into a new thing with
[2695.34 --> 2696.32]  your AI residency.
[2696.68 --> 2701.48]  I'm just kind of curious, you know, from your perspective, you know, jumping into the field
[2701.48 --> 2706.74]  at this point and this new position, what are you excited about in terms of the future
[2706.74 --> 2709.76]  of AI and what you want to be involved with?
[2709.88 --> 2710.68]  What gets you excited?
[2711.18 --> 2712.46]  It's a great question, Daniel.
[2712.90 --> 2718.70]  I think the thing that motivates me the most is the potential for creating systems that
[2718.70 --> 2728.38]  actually have some basic knowledge of anything, you know, like there, there's a subfield
[2728.38 --> 2733.20]  of NLP that calls itself natural language understanding, like NLU.
[2733.74 --> 2740.00]  And that to me is the most, I don't know, applicable, at least seems so like philosophically,
[2740.00 --> 2745.06]  it seems applicable to like my everyday life, having systems that can actually do some kind
[2745.06 --> 2746.18]  of basic reasoning.
[2746.52 --> 2752.78]  The problem with models like GPT-3 or that we, we don't have to debate this right now
[2752.78 --> 2759.88]  is that they have no common sense understanding of anything, you know, at least you, that's
[2759.88 --> 2761.20]  my argument, I guess.
[2761.52 --> 2766.94]  But I think like a tool like text attack, it kind of exists to expose that in a way that
[2766.94 --> 2772.90]  even though it might seem like it's human in terms of understanding because it can exceed
[2772.90 --> 2776.70]  the human score and all of these different benchmarks.
[2777.44 --> 2782.12]  If you use text attack or something like that, you can kind of gain some insight into why it
[2782.12 --> 2784.22]  might not actually understand anything at all.
[2784.76 --> 2789.74]  And so I'm not sure if deep learning is the full solution, but I think it's certainly part
[2789.74 --> 2790.08]  of it.
[2790.44 --> 2796.18]  And moving towards systems that have that type of like, true understanding of language is
[2796.18 --> 2798.54]  really exciting and compelling to me.
[2798.94 --> 2802.14]  That's a whole other episode that you're moving into right there.
[2802.14 --> 2807.24]  There's a lot of ground there, but I got to say, thank you so much for coming on the
[2807.24 --> 2807.36]  show.
[2807.44 --> 2809.08]  This was a fascinating conversation.
[2809.40 --> 2812.88]  It was a pleasure to have you on the show, Jack, and it was a pleasure to learn about
[2812.88 --> 2813.46]  text attacks.
[2813.58 --> 2814.86]  So we hope you'll come back sometime.
[2815.14 --> 2815.28]  Yeah.
[2815.32 --> 2815.88]  Thanks, Chris.
[2815.94 --> 2816.60]  I hope so too.
[2816.92 --> 2817.66]  Thank you very much.
[2821.30 --> 2824.26]  Thank you for listening to this episode of Practical AI.
[2825.04 --> 2826.68]  Hey, this was episode 99.
[2827.14 --> 2827.86]  You know what that means?
[2828.10 --> 2828.56]  Oh yeah.
[2828.56 --> 2830.04]  100 coming right up.
[2830.04 --> 2834.16]  Practical AI is hosted by Daniel Whitenack and Chris Benson.
[2834.46 --> 2835.66]  It's produced by Jared Santo.
[2835.96 --> 2836.52]  That's me.
[2836.86 --> 2840.26]  And our music is brought to you by the mysterious one, Breakmaster Cylinder.
[2841.34 --> 2843.88]  We have awesome sponsors who support the show.
[2844.10 --> 2848.10]  Special thanks to Fastly, Linode, and Rollbar for their continued support.
[2848.56 --> 2849.84]  Hey, did you know we take requests?
[2850.04 --> 2850.80]  We sure do.
[2850.94 --> 2852.88]  Head to change.com slash request.
[2852.88 --> 2857.32]  Select Practical AI in the dropdown and let us know what you'd like to hear about on the
[2857.32 --> 2857.54]  show.
[2858.02 --> 2858.68]  Pick a guest.
[2859.04 --> 2859.68]  Pick a topic.
[2860.10 --> 2860.84]  You name it.
[2860.96 --> 2861.94]  We love to hear from you.
[2862.30 --> 2864.58]  Once again, that's change.com slash request.
[2865.62 --> 2867.06]  That's all we got for you this week.
[2867.22 --> 2868.66]  We'll talk to you again next time.
[2868.66 --> 2870.96]  Change.com plus plus.
[2870.96 --> 2876.26]  To be continued.
[2876.26 --> 2877.66]  For more information, please Никże, Russo.
[2878.00 --> 2878.54]  OK.
[2879.18 --> 2880.82]  To be continued.
[2881.02 --> 2881.40]  To be continued.
[2883.68 --> 2884.82]  And to be continued.
[2884.88 --> 2885.08]  And to be continued.
