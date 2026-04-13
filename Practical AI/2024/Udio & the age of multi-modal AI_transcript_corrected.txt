[0.00 → 8.66] Welcome to Practical AI.
[9.16 → 16.78] If you work in artificial intelligence, aspire to, or are curious how AI-related tech is
[16.78 → 19.54] changing the world, this is the show for you.
[20.24 → 24.92] Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 → 30.94] Fly transforms containers into micro VMs that run on their hardware in 30 plus regions
[30.94 → 35.44] on six continents, so you can launch your app near your users.
[35.84 → 37.84] Learn more at Fly.io.
[42.70 → 48.30] Welcome to another fully connected episode of the Practical AI podcast.
[48.30 → 54.78] In these fully connected episodes, Chris and I keep you fully connected with everything
[54.78 → 61.08] that's happening in the AI world, the news, the trends, the new models, all the good stuff,
[61.26 → 65.76] and talk through some things that will hopefully level up your machine learning game.
[66.30 → 67.38] I'm Daniel Whiten ack.
[67.50 → 73.82] I am founder and CEO at Prediction Guard, and I'm joined as always by my co-host, Chris Benson,
[74.06 → 77.42] who is a principal AI research engineer at Lockheed Martin.
[77.86 → 78.50] How are you doing, Chris?
[78.50 → 79.82] Doing great today, Daniel.
[79.94 → 81.74] I don't know how we're going to pick what to talk about.
[81.86 → 83.56] There's so much stuff coming out right now.
[83.56 → 84.48] There's a lot.
[85.38 → 86.76] Mostly kind of new.
[87.20 → 92.38] Well, there's always new models, I guess, but it did seem like a big week with, I think,
[92.46 → 96.76] new GPT for Turbo, new Gemini.
[97.36 → 101.90] It's really hard for me to keep track of the numbers and parameter counts and all that,
[101.98 → 104.68] but I know that new Gemini, I had 1.5 something.
[104.86 → 106.38] I forget the different numbers.
[106.64 → 106.82] Yeah.
[106.82 → 114.78] And then new Mistral, new, I think it's a different mixture of experts, top of the open LLM leaderboard.
[114.96 → 124.82] We've got Audio, which I was just, so I've been at some startup accelerator stuff and then at conferences, events.
[124.82 → 133.52] And I'm like, it seems like I go into one of these events and at the end of the day, people just say, oh, did you hear about X?
[133.60 → 136.32] And I'm like, no, I haven't had my laptop open.
[136.68 → 138.18] Something else has happened, apparently.
[138.18 → 143.06] For the last two hours, I haven't had my laptop, and I've missed, I was doing work, you know?
[143.32 → 143.56] Yeah.
[144.12 → 146.62] I don't know if you've seen the trend.
[147.18 → 157.28] I think this was a prediction for 2024, which I think was a well-informed prediction for 2024 from many different people.
[157.28 → 177.14] And I think we talked about this in our own discussions of 2024 around multi-modality of AI in 2024, whereas in 2023, you kind of saw this explosion of, in many cases, text-to-text AI, meaning I put in a text prompt and I get some text back.
[177.14 → 185.84] Now we're seeing an explosion of multiple modalities of data input and or output to these models.
[185.84 → 187.80] And that's mostly what I'm seeing.
[187.94 → 190.24] Is that consistent with your view as well, Chris?
[190.76 → 191.12] Totally.
[191.26 → 194.62] I was thinking about that in a moment for us to brag.
[194.82 → 198.64] I tell you, we've actually been fairly good with our predictions the last few years.
[198.92 → 199.64] Who knows?
[199.90 → 203.80] Maybe we're actually setting the it's a self-fulfilling prophecy.
[204.12 → 209.08] It's just everyone's listening to practical AI, and they're making our predictions real.
[209.18 → 210.78] That must be what it is, I'm sure.
[210.78 → 217.48] You know that all the, you know, like over at OpenAI, they're just listening to us, and they're going, okay, that's what we need to go work on.
[217.60 → 218.40] It's a lot of pressure.
[218.70 → 218.86] Yeah.
[218.92 → 222.82] I tell you what, it's a good thing we're steering the entire industry by ourselves, right?
[223.06 → 223.12] Yeah.
[223.12 → 225.62] Which is, yeah, it's a lot of pressure, but it's good.
[225.76 → 225.88] Sure.
[226.56 → 227.68] No pressure at all, man.
[227.88 → 237.84] I do want to talk about multi-modality today, but I've just got to share with you some of this Audio stuff, Chris, which I think, well, Audio, Audio.
[237.84 → 241.24] I don't know if anyone knows how to say this yet.
[241.44 → 246.32] I was saying Audio, maybe it's Audio, U-D-I-O, I believe.
[246.88 → 249.86] I'm not going to hazard a guess until I hear somebody else do it.
[250.46 → 251.08] Yeah, yeah.
[251.24 → 252.84] It's coming out of beta.
[252.98 → 263.20] I think that there were some leaks of some of what they were doing before, but essentially, if you go to this website, you can sign up for an account.
[263.20 → 278.74] They have it marked as beta, so I'm not sure exactly where this is going necessarily product-wise, but what you see, at least in its beta form, is essentially a space where you can put in a text prompt.
[278.74 → 299.18] It kind of reminded me of almost like a clip drop or something, some of these image generation platforms where you can kind of pre-select some elements of the prompt, and the goal would be to completely generate a coherent and compelling song or piece of music or composition.
[299.58 → 301.40] It's essentially a music generator.
[301.40 → 305.30] So we've seen a little bit of this in the past, right?
[305.94 → 324.92] And in the past, we've kind of heard things generated like kind of dreamy, ambient things and maybe useful for kind of backing YouTube videos or something like that, but not really compelling music in and of itself.
[324.92 → 340.76] And I think what's interesting about this UDO is that it generates both this sort of compelling music, but also lyrics and also synthesized voices singing the lyrics all together in one.
[341.46 → 350.66] So Chris, before, while you were setting up your studio there to record the podcast, I was busy on UDO figuring out what is there.
[350.66 → 362.56] Now, there are a couple of fascinating ones that I listened to, and I've preloaded a couple in here for us to listen to and to give our audience a little bit of a sense of the audio.
[362.76 → 363.12] Absolutely.
[363.32 → 367.58] Because this is an audio podcast, so, you know, what better format?
[367.58 → 375.76] So one of these, which I found really intriguing was Dune, the Broadway musical.
[376.12 → 381.42] And I would go to that, by the way, just to make it very clear, I'm standing in line to buy tickets, so to speak.
[381.42 → 387.94] Well, the music has been generated for this, and I'll cite Bobby B.
[388.26 → 395.08] So Bobby B on UDO, and he's created Dune, the Broadway musical.
[395.08 → 401.84] So just to give a sense of people, the prompt that went into this to create it, it says,
[402.44 → 409.46] teen pop, show tunes, film soundtrack, uplifting, playful, female vocalist, happy.
[410.20 → 417.10] Anyway, so you get a sense of kind of similar to a, I guess, like an image generation prompt where you're saying like,
[417.52 → 422.60] high resolution, Unreal Engine, like this sort of stuff to give it some stylistic guidance.
[422.60 → 425.86] But I've got this preloaded in here, Chris.
[426.34 → 429.44] Everything that you're going to hear is AI generated.
[429.62 → 435.40] So let's listen to Song of Arrays from Dune, the Broadway musical.
[435.84 → 437.30] Oh, you got my attention, man.
[437.96 → 442.84] Paul Trades of Ara keen, the greatest leader we've ever seen.
[442.96 → 445.60] They say that he's the list in Al-Sayib.
[445.60 → 458.20] What do you think?
[458.54 → 459.48] Move over, Wicked.
[459.74 → 461.38] Move over, Les Misérables.
[462.06 → 464.78] All just, you know, I saw Hamilton recently.
[464.92 → 465.50] Move over, Hamilton.
[465.50 → 466.42] Yes, yes.
[466.46 → 467.82] We're all about Dune, the musical now.
[467.90 → 468.28] That's it.
[468.28 → 468.80] Exactly.
[469.10 → 470.00] Yeah, so good.
[470.24 → 475.78] And even the lyrics, you know, eyes bright blue and hair jet black.
[475.90 → 478.42] You should see him ride on a sand worm's back.
[478.72 → 479.44] I mean, that's great.
[479.66 → 480.52] That's good right there.
[480.72 → 485.82] I like the fact that the music actually deviated far from the darkness of Dune.
[485.94 → 489.14] You know, the perpetual darkness of the theme.
[489.32 → 490.26] That was fun.
[490.44 → 491.26] That was great.
[491.40 → 491.64] All right.
[491.70 → 492.38] Ready for more?
[492.74 → 492.92] Yeah.
[493.06 → 493.74] Oh, yeah.
[494.06 → 495.74] So I tried out my own.
[495.74 → 497.62] Of course, I had to try out my own.
[498.20 → 498.44] Of course.
[498.58 → 505.20] So my prompt that I put in, and I only experimented with this, so I'm sure you can do much better.
[505.72 → 515.94] But I put in a song about two podcast hosts trying to navigate the wild and crazy world of AI in the style of pop rock.
[516.60 → 517.80] Practical AI, the musical?
[517.80 → 525.38] We really appreciate you, Break master Cylinder, the mysterious Break master Cylinder behind our theme.
[525.74 → 526.78] Music for the show.
[527.26 → 529.46] But this is what UDO can do.
[530.04 → 535.96] And I selected specifically to have it pop rock and to auto-generate the lyrics.
[536.04 → 537.84] So I didn't put in any lyrics.
[538.00 → 540.48] So I have two options for you, Chris.
[540.62 → 544.40] I have two selections that you can see which one you like better.
[544.50 → 545.18] Here's the first.
[545.18 → 551.34] The first thing they do, hit record in their room.
[551.62 → 555.20] Discussing the trends where the bots will take us.
[555.64 → 557.60] And launching the forecast.
[557.82 → 558.50] Oh, yeah.
[559.18 → 560.24] Oh, yeah.
[560.92 → 561.98] Oh, yeah.
[562.18 → 565.20] Caught up in the wave where the data streams tied.
[565.34 → 568.70] With a crackle in the voice and the laughter just right.
[568.92 → 572.12] They chat with a rhythm that's as quick as a flash.
[572.12 → 577.06] All right.
[577.22 → 578.02] Selection one.
[578.34 → 578.78] Thoughts?
[578.90 → 579.76] I like that one.
[580.98 → 586.72] You just transported me from like, you know, 53, which is what I'm at now, all the way back
[586.72 → 589.62] to like 16 in the 80s, you know, late 80s.
[589.68 → 590.66] I was all about that.
[590.80 → 591.16] That was good.
[591.32 → 591.96] Okay, cool.
[592.18 → 593.20] Yeah, I love it.
[593.36 → 594.12] Okay, that one was...
[594.68 → 596.18] They also generated a title.
[596.18 → 597.26] It's interesting.
[597.40 → 601.84] I don't know how much of this, you know, how many models are at play under the hood here
[601.84 → 603.10] and how they're coordinated.
[603.28 → 609.36] I'm guessing maybe there's some that generate the lyrics and some that generate the title.
[609.64 → 613.36] And then somehow that's merged together in a music generation.
[613.36 → 618.04] Because obviously the voice and the lyrics have to be coordinated somehow.
[618.04 → 625.00] I at least didn't see a lot of underlying explanation of what's going on here, but pretty interesting.
[625.52 → 629.66] And that was generated, I would say, in 30 seconds or something.
[629.82 → 630.16] I don't know.
[630.22 → 631.18] Not that long, right?
[631.60 → 633.34] So let's take a listen to number two.
[633.44 → 635.32] This one was titled Digital Odyssey.
[635.32 → 643.76] Both hosts are indeed, my friend.
[644.20 → 644.88] Oh, yeah.
[645.76 → 646.60] Oh, yeah.
[647.08 → 650.32] Voices through the digital tide.
[652.58 → 655.72] They're learning as the codes blend.
[656.26 → 658.40] Got theories, theories.
[659.06 → 660.46] Everyone must hear.
[660.78 → 663.86] A journey through the AI sphere.
[665.32 → 667.58] There you go.
[667.70 → 671.18] Even with a little bit of a guitar type solo there at the end.
[671.72 → 672.34] I know it was good.
[672.46 → 673.76] I like the first one better.
[674.34 → 677.66] The first one felt like I was, you know, like I was a kid again right there.
[677.88 → 678.68] But I like both.
[678.96 → 680.90] And yeah, this was good.
[681.16 → 683.74] I could just spend all day generating music now.
[683.90 → 685.02] I may do that, actually.
[685.30 → 687.34] I might have just taken up your Saturday.
[687.76 → 688.36] Oh, my God.
[688.36 → 692.74] My wife has all these chores planned for me because we're recording here late on a Saturday morning.
[692.74 → 694.70] And I may get myself in trouble by.
[695.72 → 696.16] Yes.
[696.32 → 696.58] Okay.
[697.02 → 698.14] Well, there you go.
[698.34 → 700.72] So, UDO, check it out.
[700.84 → 701.82] Super cool stuff.
[702.26 → 709.80] I think this does bring up some fascinating challenges, issues, struggles, excitement.
[709.80 → 713.24] Also, of course, joy in hearing Dune the musical.
[713.94 → 715.30] But it is fascinating.
[715.48 → 717.78] I even thought about this when I was going through here.
[718.46 → 722.72] Well, you know, Bobby B created Dune the Broadway musical.
[723.56 → 725.22] And I just downloaded it.
[725.28 → 729.12] And I'm doing it what I want with it, which I guess is playing it on my podcast.
[729.58 → 731.58] So, Bobby B, I hope you're okay with that.
[731.58 → 735.88] Now, technically, this is machine generated.
[736.38 → 746.78] So, at least as far as I understand, in the current U.S. legal system, such a thing would not be copyrightable.
[747.42 → 748.04] Sorry, Bobby.
[749.38 → 750.44] Sorry, Bobby.
[750.56 → 754.48] I'm not giving legal advice here, obviously, and not a lawyer.
[755.06 → 757.92] But that's my understanding from our previous conversations.
[757.92 → 769.08] But what's interesting is, I think, similar to these AI-generated art things that were put into art competitions and won.
[769.92 → 771.20] There could be.
[771.32 → 776.40] Now, in my case, I just put in a simple prompt that generated something in 30 seconds.
[777.00 → 783.32] There could be some really deep thought put into how to construct this prompt.
[783.32 → 789.66] And the various kinds of, I think, Bobby's prompt was much better constructed than mine.
[790.32 → 796.56] And also, you can upload your own lyrics into this to add a level of creativity.
[797.48 → 806.08] So, there's really an open question here of how much human creativity is actually a big portion of this generation.
[806.08 → 816.88] And will the established laws and legal entities eventually recognize the creativity that's put into prompting these sorts of systems?
[817.34 → 826.66] Just like there was a time when there was a question of whether if you took a picture with a camera, right, you just click the button.
[827.00 → 827.06] Yeah.
[827.06 → 834.02] Now, photographers out there are going to get really mad at me because I think they would recognize its way more than clicking a button, right?
[834.16 → 836.50] There is a lot to photography.
[837.18 → 839.58] And that's, I think, why it's been accepted as an art.
[839.90 → 844.90] But people argued at one point, you know, hey, you click that button.
[845.32 → 846.68] It's machine-generated.
[846.94 → 848.88] You can't have a copyright for that.
[849.20 → 851.20] But eventually, those laws change.
[851.20 → 856.80] So, I wonder, Chris, if you have any thoughts about if or when that might change in these cases.
[857.44 → 857.52] Yeah.
[857.62 → 871.26] I mean, I think it will because I guess if you look at these stream of AI advancements that we've covered over the years, there's a sense of inevitability that when these things come out, they catch on and they become popular.
[871.26 → 872.70] And then they become the norm.
[872.70 → 877.88] And then eventually, as we keep seeing, the laws gradually catch up over time.
[878.64 → 884.18] And things like UDO, if I'm pronouncing the name right, is going to be typical.
[884.38 → 885.10] It won't just be them.
[885.20 → 886.18] There'll be others as well.
[886.38 → 892.82] And so, I know that, you know, by way of example of that inevitability, we have a Spotify account for our family.
[893.38 → 898.38] And, you know, we're listening to the traditional way of streaming music historically.
[898.38 → 904.40] And one of the things I do on that is I really like to explore new genres and new types of music that I don't know.
[904.48 → 906.30] And I'm always trying to think, how do I get to that?
[906.58 → 906.78] Yeah.
[906.90 → 914.72] But I'm very likely to use something like UDO to prompt what I'm feeling, what I'm thinking, and try to explore new music that way.
[914.80 → 922.46] Because I don't really care as a user whether it's an artist that's human or an AI model that generated if it sounds good to me.
[922.60 → 928.12] And so, I think that sense of inevitability will bring about the change over time.
[928.38 → 928.86] Yeah.
[929.04 → 940.54] I think personally, I think right now even it's a gray area where, especially if you're going back and forth, like you're trying a prompt and then maybe you're modifying the lyrics.
[940.90 → 957.60] And if there's some sort of back and forth, that definitely gets into a little bit of a gray area where how much, even of the generated stuff, ignoring the creativity and the prompt, how much of the generated stuff is actually machine generated versus human post edited, for example.
[957.60 → 958.38] That's right.
[958.46 → 962.02] So, yeah, I think that even now that's a bit of a gray area.
[962.16 → 969.86] But then my personal thought is eventually this will be more recognized as a creative pursuit.
[970.06 → 971.38] But, you know, we'll see.
[971.38 → 979.56] You know, this new inroads into music through this AI model with this being so far the most interesting that I've seen.
[979.90 → 985.78] This probably will really scare the music industry, you know, because this is taking it to a whole different level.
[986.08 → 989.04] And there probably will be a lot of lobbying, a lot of lawsuits.
[989.04 → 1000.76] You know, we saw this past year, you know, actors going on strike because of AI based video and the creation of characters or the representation potentially of live people.
[1000.96 → 1003.14] And I think we'll see some form of that here.
[1003.38 → 1006.22] This is a process we're going to go through over and over again.
[1006.22 → 1014.04] And I was talking to a good friend just the other day about this and life ahead and stuff and how to do this.
[1014.04 → 1019.10] And I said the smart people will align themselves with these capabilities.
[1019.10 → 1025.98] You know, it's not about whether it's a good future or a bad future or whatever from perspective, but it's an inevitable future.
[1025.98 → 1040.58] If I could give advice as a non-lawyer and non-professional musician in the music industry, but someone observing this, I would say find a way to get on board with it and make it work for you quickly because it's not going away.
[1041.66 → 1042.22] Yeah.
[1042.54 → 1042.78] Yeah.
[1043.18 → 1043.74] Very true.
[1043.74 → 1049.10] And I do also wonder, of course, those things that we just heard were completely AI generated.
[1049.10 → 1074.16] But it's interesting to me that maybe a creative person who is in there are many that are embracing some of these things like musicians could actually iterate very, very quickly on different ideas, putting their own voice to backing music or getting prompted with lyrics that aren't quite so good as what they would like, but gives them a creative starting point.
[1074.16 → 1080.00] And, you know, really explore spaces that they might not have explored before.
[1080.24 → 1085.12] So that might be cool to see as well, that kind of human UDO teaming.
[1085.32 → 1085.96] Yeah, I agree.
[1086.24 → 1103.34] And another thing that I think will become inevitable, you know, so here's a startup idea for folks, is with all the advancements over the last few years in kind of emotional recognition from models and understanding if you combine a capability like this.
[1103.34 → 1121.52] And you choose to opt in, which there's privacy concerns, obviously, with a service that also is monitoring yourself, you know, and maybe the data is only available to you, but can generate content that is exactly specific to what you're dealing with in life.
[1121.52 → 1129.40] And when you need to pick me up, not only does it find the right music, but it finds the right lyrics for the situation and stuff.
[1129.52 → 1135.52] And so there are a lot of interesting psychological considerations here that could be both good or bad, obviously.
[1136.28 → 1138.10] But I think that's pretty fascinating.
[1138.32 → 1142.34] I'm wondering if I can find a service in a few years that will do that.
[1142.34 → 1149.84] And it follows me through the day and I keep the content private to me in my account, but it gives me the pick me up when I want.
[1150.04 → 1153.34] That's what I'm looking for, for whoever is going to go out and do that in the world.
[1153.62 → 1157.52] Personal soundtrack and narration and vibe.
[1157.74 → 1158.48] My life.
[1158.90 → 1159.22] Yeah.
[1159.22 → 1159.28] Yeah.
[1172.34 → 1177.02] This is a changelog news break.
[1177.46 → 1190.04] YouTuber Internet of Bugs posted a lengthy breakdown exposing Devin's creators, Cognition Labs, for falsifying claims about their world's first AI software engineer.
[1190.04 → 1200.64] Devin was pitched as a fully autonomous software developer, and one of the more impressive demos showed it completing and getting paid for freelance jobs on Upwork.
[1200.64 → 1202.38] Sound too good to be true?
[1202.76 → 1205.76] It did, to Internet of Bugs, who says, quote,
[1205.76 → 1216.92] I broke down the Devin Upwork video frame by frame, and here I show what Devin was supposed to do, what it actually managed to do instead, and how bad a job of that it did.
[1217.30 → 1223.56] On the whole, that's not surprising given the current state of generative AI, and I wouldn't be bothering to debunk it except,
[1224.02 → 1228.26] One, the company lied about what Devin could do in the video description, and,
[1228.26 → 1232.42] Two, a lot of people uncritically parroted the lie all over the internet.
[1232.68 → 1232.96] And,
[1233.08 → 1233.38] Three,
[1233.62 → 1238.16] That caused a lot of non-technical people to believe that AI might replace programmers soon.
[1238.34 → 1238.72] End quote.
[1239.46 → 1244.18] Devin really did garner a lot of attention, also known as money, because of that demo.
[1244.50 → 1248.48] We talked about it on our shows, with a healthy amount of skepticism, I think.
[1248.64 → 1254.70] But I'm thankful their claims have been debunked, and I hope we all give Cognition Labs the side-eye from here on out.
[1254.70 → 1260.16] Exaggerating your development capabilities? Maybe Devin really is human, after all.
[1260.70 → 1265.58] You just heard one of our five top stories from Monday's Changelog News.
[1265.96 → 1272.66] Subscribe to the podcast to get all the week's top stories, and pop your email address in at changelog.com slash news
[1272.66 → 1278.36] to also receive our free companion email with even more developer news worth your attention.
[1278.78 → 1282.18] Once again, that's changelog.com slash news.
[1284.70 → 1294.56] A lot of these things, like I say, are moving into this multimodal sphere.
[1295.18 → 1304.98] And it might be worth just kind of looking back a little bit at how we got to where we're at in terms of multimodal functionality.
[1304.98 → 1315.12] Sort of how that gradually has changed over time, from NLP and speech to multimodal models that we're seeing now.
[1315.12 → 1323.72] I think one good way to, if we kind of step back and look at it on a holistic or historical standpoint,
[1323.98 → 1336.26] you kind of started out with modes of data processing that were maybe separated, but often tied together in a sort of chained way.
[1336.26 → 1338.74] We didn't really think about it chaining at the time, right?
[1338.82 → 1349.88] But you had speech synthesis models, for example, that were really specifically trained to only do text to speech, right?
[1350.06 → 1358.86] And in some cases, even that was broken up into sub models of like a vocoder and other types of models.
[1358.86 → 1373.54] And you had text to text models, you had maybe computer vision models that would process images to do object recognition or even videos in certain cases or frames of videos.
[1373.72 → 1375.98] But all of these were specializations.
[1376.80 → 1387.78] So the whole idea of there being computer vision is right as a specialization is that I am specializing in models that process this mode of data, right?
[1387.78 → 1398.78] And speech technology, the discipline of speech technology is a discipline of really focusing on processing either speech inputs or speech outputs.
[1399.46 → 1411.66] And then NLP, quote unquote, had special models that would take in text and maybe classify or detect entities or do machine translation or these sorts of things.
[1411.66 → 1418.08] So we kind of that historically was kind of how the field was developing.
[1418.64 → 1435.54] And if we skip kind of the middle portion and come back to it, now we've gotten to a point where there's seemingly these large foundation models that are able to take in multiple inputs at the same time of multiple modes.
[1435.54 → 1443.58] So, for example, an image and text in the same input paired together and answer questions.
[1443.74 → 1460.96] So this would be like what we see with GPT vision, or we see a text prompt or even in video input like we have seen with Gemini recently where you can import a whole video and ask for a summary of all the visual components and that sort of thing.
[1460.96 → 1465.28] So that's kind of, from my end, how I view the bookends.
[1465.28 → 1472.02] Is that also, from your standpoint, any comments on that, Chris, in terms of how we've progressed from one end to the other of that?
[1472.32 → 1483.88] I'll pivot slightly in response to that and say, as you were describing that, it really resonated with me with something else that I've been thinking in that development.
[1483.88 → 1488.80] And that is I consume a lot of content through audiobooks.
[1489.08 → 1503.30] Anytime I'm kind of on autopilot, you know, driving or mowing the lawn or doing any kind of thing, I'm listening to audiobooks for learning purposes mostly at kind of double speed, as fast as my brain can process it because I like to consume as much as I can.
[1503.48 → 1504.22] I can't do that.
[1504.48 → 1505.70] My mind is too slow.
[1505.92 → 1508.88] No, you get used to it after a while.
[1508.88 → 1511.36] But it's just to get the information in.
[1511.68 → 1518.88] And I just went through a really Pulitzer Prize winning book through audio called An Immense World by Ed Yong, which is fascinating.
[1519.80 → 1522.08] And I highly recommend it to anybody that wants to do it.
[1522.28 → 1532.78] But it is all about the way we and all animals and not only humans, but all animals in their unique ways perceive the world through their senses and how vastly different those are.
[1532.78 → 1539.70] And the theme that came up to me throughout that was how multimodal everything about humans are.
[1539.90 → 1543.16] The way that we learn, our experiences are all multimodal.
[1543.26 → 1546.44] We don't have just vision and just audio and just text.
[1546.64 → 1548.60] We're taking it all in at the same time.
[1549.12 → 1559.22] I think this progression that we've seen in terms of moving into multimodal this year has been really fascinating in terms of coming in to really how we take in information and how we learn.
[1559.22 → 1569.38] And I think going back to UDO today and seeing what they're doing and looking at the other multimodal capabilities that we've been learning, it feels like we're finally getting to some...
[1569.38 → 1570.48] I know we keep saying this.
[1570.60 → 1573.04] It's always kind of cool at the moment when the new thing comes out.
[1573.42 → 1577.52] But it feels like it's really aligning with what it means to be human as well, ironically.
[1578.16 → 1581.12] That's the background thought process I had as you were going through that.
[1581.12 → 1585.70] Yeah, there are these scenarios in which knowledge is definite.
[1585.90 → 1590.76] Like we process knowledge across multiple modes of data inputs.
[1591.50 → 1600.02] And certain things are not all, you know, many things are not all represented in text or in any given mode.
[1600.02 → 1611.18] And I think you've seen this already kind of utility over this with things like GPT Vision, which is a kind of visual instruction tuned model.
[1611.44 → 1614.30] And maybe that's something to share with the audience.
[1614.48 → 1617.02] If you're not familiar, there's kind of this...
[1617.02 → 1626.74] The music generation stuff, maybe that's a little bit newer, but there's kind of this ongoing work in visual instruction tuning.
[1626.74 → 1638.56] And this would be the type of model in which you would have an image input and maybe a text prompt.
[1639.64 → 1652.68] And traditionally, like I remember, I think there are even some of these models still that are quite popular to use on, for example, AWST extract, for example, is a OCR system.
[1652.68 → 1655.16] But you can also do visual question answering.
[1655.16 → 1661.74] Now, it used to be you had a specific model architecture for visual question answering.
[1661.94 → 1664.14] It was a research topic in and of itself.
[1664.46 → 1665.98] There was a specialized model.
[1666.14 → 1669.04] And this kind of illustrates some of the progression that we've had.
[1669.20 → 1677.34] There was a very specific discipline around visual question answering and very specific models that could do those things.
[1677.34 → 1678.34] And they advanced.
[1678.34 → 1694.70] But then, recently, you've got what has begun being termed visual instruction tuning for models, where the models are actually similar foundation models to what people are using for other modes.
[1694.70 → 1700.22] So, for example, if we look at the Lava model, L-L-A-V-A.
[1700.22 → 1701.88] So, not Lama, but Lava.
[1702.58 → 1704.96] Maybe a bit hard to distinguish in the audio.
[1704.96 → 1715.00] That's an open source manifestation of the GPT vision system or similar functionality to that.
[1715.00 → 1732.80] And if we look at how that operates, it actually is built off of, and this is kind of, we talk about this a lot on the podcast, Chris, where you're always sort of building on the shoulders of giants and a lot of what's come before, even though some of these functionalities seem to pop up out of nowhere.
[1732.80 → 1735.38] But there are kinds of previous signals.
[1735.60 → 1740.92] And, Chris, I don't know if you remember, we, I think, had an episode where we talked about Clip.
[1741.16 → 1741.48] Yes.
[1741.66 → 1749.68] Which was a multimodal way to embed both text and images in something developed by OpenAI.
[1750.04 → 1754.22] Contrastive language image pre-training is what Clip is from OpenAI.
[1754.52 → 1754.82] Correct.
[1755.02 → 1761.80] Which, thankfully, is open to everyone back in the days when OpenAI was open, and we can still use it.
[1761.80 → 1777.78] But Clip allows you to embed an image or text in a similar embedding space, which means you're converting an image or a piece of text into a set of numbers.
[1778.50 → 1788.56] And if you compare those sets of numbers in that vector space, you can actually find things that are semantically similar by the distance between those vectors.
[1788.56 → 1793.94] Which is interesting and kind of makes immediate sense if you're doing text-to-text things.
[1794.10 → 1800.82] Like the semantics of one piece of text or the meaning of one piece of text could be similar to the meaning of another piece of text.
[1801.20 → 1807.98] It's very intriguing, though, if you make this multimodal and say a nice sunset on a beach in Florida.
[1807.98 → 1813.54] And then you have an image of a sunset somewhere on a beach.
[1813.74 → 1817.28] And then you have an image of a car driving through New York.
[1817.28 → 1821.58] And then you have an image of a spaceship in outer space.
[1821.90 → 1827.42] And you could actually find which of those images is semantically similar to a text input.
[1827.70 → 1827.88] Right.
[1827.90 → 1831.38] So that's kind of the Clip way of embedding things.
[1831.38 → 1842.28] And then on the other side, you have large language models, right, which can take a text prompt, reason over that text prompt, even though it's not really reasoning.
[1842.28 → 1843.78] It's just auto-completing.
[1843.78 → 1854.60] But we can think of, you know, functionally, it takes in that prompt and outputs some output related to the question that's input, the query, the instruction, that sort of thing.
[1854.60 → 1881.66] So what they've done with Lava, which has been around for some time and people have built different types of Lava models and sort of its own family in and of itself, is paired the Clip style embedding model or a visual encoding system with a large language model and then created this text and image input.
[1881.66 → 1893.76] So if you look at the architecture of what they do, what happens is they have an image input that goes through the vision encoder, for example, Clip, that produces an embedding.
[1893.96 → 1905.74] They have a language model like Llama that accepts a language instruction or text input, and that creates an internal hidden representation embedding.
[1905.74 → 1912.56] And the first thing they do is they train a projection matrix for the vision encoder.
[1913.00 → 1916.12] And can you talk about what a real quick, what a projection matrix is?
[1916.26 → 1916.82] Yeah, yeah.
[1916.90 → 1922.14] So the language model produces an embedding, embedded representation of the text.
[1922.34 → 1926.34] The vision model creates an embedded representation of the image.
[1926.34 → 1938.88] But these two are different model architectures, and the embeddings can't be directly compared one to another because one's Llama and one's Clip, even though they functionally produce embeddings.
[1938.88 → 1954.66] So the projection matrix is a sort of translation of the output of the vision encoder, the Clip model, into a space in which it's concatenated or combined in some way with the output of the Llama model.
[1955.38 → 1965.08] And that is a trained projection such that it accomplishes the end tasks that you're training for, like a visual question answering or reasoning over an image, that sort of thing.
[1965.08 → 1970.02] So that's the initial pre-training is finding that projection matrix.
[1970.24 → 1972.58] And the interesting thing here is actually this.
[1972.88 → 1975.90] It's a combination of models, which is intriguing, right?
[1975.94 → 1990.20] Because you can always update Llama to the next cool thing like Gemma, or you could always update Clip to the next cool thing like Bridge Tower from Intel and combine them in fascinating ways and do this retraining.
[1990.20 → 1999.02] And then people fine tune these models based on data sets that they've created for specific tasks like we've seen with language models.
[1999.20 → 2005.62] So there might be a science question and answer for reasoning over science images, right?
[2005.70 → 2009.30] Or sort of visual chat in a specific domain.
[2009.30 → 2028.84] So to give people a sense of the functionality of this type of model, if you haven't played around with GPT Vision or something like that, one of the examples on the Lava paper site, which I find interesting, is there's like a meme image of a world map, but it's made out of chicken nuggets.
[2028.84 → 2032.32] And so it looks like a world, but it's made out of chicken nuggets.
[2032.60 → 2034.28] So the picture is there.
[2034.40 → 2042.74] And then the user input, the text input, along with the image input is, can you explain this meme in detail?
[2043.44 → 2050.20] So there's some element of the question that's needed to answer that question, because you're saying this is a meme.
[2050.34 → 2053.26] You're asking for specific details, right?
[2053.26 → 2058.48] And then you definitely need the visual content to answer that question.
[2059.04 → 2062.46] Otherwise, you would just hallucinate something about a meme.
[2062.88 → 2062.98] Sure.
[2063.28 → 2072.50] So the Lava answer is, the meme in this image is a creative and humorous take on food with a focus on chicken nuggets as the centre of the universe.
[2072.50 → 2073.92] The meme begins blah, blah, blah.
[2074.04 → 2079.74] And it essentially explains the humour, which is maybe not the best way to make something more humorous.
[2080.22 → 2080.48] Yeah.
[2081.00 → 2082.14] A little bit dry there.
[2082.64 → 2082.88] Yeah.
[2082.88 → 2089.50] But you can think of other cases where you would need sort of visual input and text input to create an answer, right?
[2089.52 → 2095.38] Like if you say, what was the guy who raised his right hand in this video wearing, right?
[2095.70 → 2104.38] That necessarily, like as a human, we would process that both from the text input standpoint and the visual content standpoint.
[2104.38 → 2114.92] And so I think it's fascinating, this sort of exploration of not just chained models from multiple modes together.
[2114.92 → 2121.54] Like we've seen in the past kind of history where you have a speech model, you have a language model.
[2121.54 → 2124.16] And you can chain them together in interesting ways.
[2124.16 → 2143.16] But this joint encoding, this joint processing of multiple modes of data at the same time is actually required for some of the types of reasoning that we might want to augment or automate from a standpoint of how we process information as humans.
[2143.16 → 2148.78] So yeah, I would recommend that people look into this lava model.
[2148.78 → 2149.78] It's open.
[2149.78 → 2153.22] Like I say, it's sort of a family or a style of doing things.
[2153.22 → 2163.84] So there are a bunch of examples of that on Hugging Face and demos that you can actually try out and try kind of an open version of what you get with GPT Vision.
[2163.84 → 2165.00] That sounds good.
[2165.18 → 2175.96] I've just been struck through our entire conversation going back to what I mentioned earlier about how close this is in terms of matching how we as humans process.
[2175.96 → 2188.64] As you took us through the merging of the modalities a few minutes ago and me having just – I'm actually in the middle of a – I think it's called The Great Courses, and I'm about the best brain.
[2188.78 → 2201.84] And it's talking about how exactly that happens in our brain to convert it into a form which is chemical, electrical in nature for our brains to actually operate on since we don't actually see and smell.
[2201.84 → 2212.48] And so it's just fascinating that while the underlying AI models are not the way the brain operates, the kind of the modalities are starting to merge in that way.
[2212.70 → 2213.72] It's really neat.
[2213.90 → 2221.26] So thank you very much for taking us through that understanding of how multimodality works in a practical sense.
[2221.52 → 2225.02] You lived up to practical AI in all ways there.
[2225.02 → 2232.76] Well, this episode has a little bit for everybody where you get a fun Broadway song, and then we also talk about projection matrices.
[2233.20 → 2234.12] So there you go.
[2234.30 → 2235.06] Something for everyone.
[2235.24 → 2236.62] I enjoyed it, Chris.
[2236.80 → 2240.56] And yeah, I think this will be a trend that we continue seeing throughout this year.
[2240.56 → 2265.46] So if you haven't got hands-on and tried a little bit of this multimodal stuff, whether you go to UDO and try to create a song or you go to ChatGPT and try to use GPT Vision or Gemini and process a video or download the lava model and try to run some multimodal queries, that's the best way to sort of get an intuition for how these things behave and what's possible.
[2265.82 → 2268.28] We'd really encourage you to get hands-on.
[2268.28 → 2272.96] So homework assignment between now and next episode, I guess.
[2273.24 → 2273.60] Absolutely.
[2274.12 → 2274.48] All right.
[2274.56 → 2275.48] It's been fun, Chris.
[2275.56 → 2276.40] We'll talk to you soon.
[2276.74 → 2277.34] Take care, Daniel.
[2277.34 → 2285.66] All right.
[2285.96 → 2288.44] That is Practical AI for this week.
[2289.18 → 2290.28] Subscribe now.
[2290.46 → 2295.44] If you haven't already, head to practicalai.fm for all the ways.
[2295.74 → 2301.84] And join our free Slack team where you can hang out with Daniel, Chris, and the entire Changelog community.
[2301.84 → 2307.08] Sign up today at practicalai.fm slash community.
[2307.68 → 2314.60] Thanks again to our partners at fly.io, to our Beat Freaking Residents, Break master Cylinder, and to you for listening.
[2314.96 → 2316.72] We appreciate you spending time with us.
[2317.08 → 2318.26] That's all for now.
[2318.50 → 2320.18] We'll talk to you again next time.
[2320.18 → 2350.16] We'll talk to you again next time.
