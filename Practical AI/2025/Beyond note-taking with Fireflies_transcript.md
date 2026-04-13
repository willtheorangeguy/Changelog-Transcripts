[0.00 --> 8.74]  Welcome to the Practical AI Podcast, where we break down the real world applications
[8.74 --> 13.64]  of artificial intelligence and how it's shaping the way we live, work, and create.
[13.88 --> 19.14]  Our goal is to help make AI technology practical, productive, and accessible to everyone.
[19.48 --> 23.54]  Whether you're a developer, business leader, or just curious about the tech behind the
[23.54 --> 25.12]  buzz, you're in the right place.
[25.12 --> 29.84]  Be sure to connect with us on LinkedIn, X, or Blue Sky to stay up to date with episode
[29.84 --> 33.02]  drops, behind the scenes content, and AI insights.
[33.36 --> 35.88]  You can learn more at practicalai.fm.
[36.18 --> 37.50]  Now, on to the show.
[48.52 --> 51.96]  Welcome to another episode of the Practical AI Podcast.
[51.96 --> 53.92]  This is Daniel Whitenack.
[54.04 --> 59.78]  I am CEO at Prediction Guard, and I am joined as always by my co-host, Chris Benson, who
[59.78 --> 63.24]  is a Principal AI Research Engineer at Lockheed Martin.
[63.46 --> 64.24]  How are you doing, Chris?
[64.42 --> 65.70]  I am doing very well.
[66.34 --> 70.94]  Got to spend the morning with some folks down at Georgia Tech talking AI.
[70.94 --> 71.30]  Cool.
[71.80 --> 73.30]  And you're headed my way.
[73.56 --> 79.22]  After this, we're going to meet up at the Midwest AI Summit, which is as of recording
[79.22 --> 84.98]  this happening tomorrow, and also as recording this still experiencing government shutdown
[84.98 --> 88.00]  and travel problems in the US.
[88.56 --> 91.56]  So hopefully, I'm hoping you make it our way.
[91.90 --> 93.76]  But yeah, excited for the summit.
[94.16 --> 100.64]  It's going to be a fun time to be together in person and meet some listeners, meet some
[100.64 --> 104.10]  AI enthusiasts and AI curious folks.
[104.46 --> 105.84]  So I'm excited for that.
[106.08 --> 110.76]  I'm encouraged because our guest was on a plane earlier today, and he got through.
[110.76 --> 114.06]  So I think we should dive right into the conversation here.
[114.42 --> 114.94]  Yeah, yeah.
[114.94 --> 115.66]  Sounds good.
[115.78 --> 121.50]  I am very excited because we have with us Chris Schramanini, who is co-founder and CEO
[121.50 --> 122.92]  at Fireflies AI.
[123.34 --> 123.56]  Welcome.
[124.04 --> 124.42]  Hi, Dan.
[124.54 --> 125.02]  Hi, Chris.
[125.34 --> 126.10]  It's great to be here.
[126.30 --> 127.02]  Thanks for having me.
[127.24 --> 129.64]  Yeah, it's really, really great to have you on.
[129.64 --> 137.50]  I see, of course, Fireflies join my meetings all the time, which is cool, sort of Firefly
[137.50 --> 141.68]  call assistance and recording and that sort of thing.
[142.08 --> 148.22]  Of course, this is probably something like it was somewhat early on, at least in the public
[148.22 --> 154.82]  perception of ways people were using AI that kind of impacted maybe their day-to-day were
[154.82 --> 159.66]  these kind of meeting assistants that have taken various forms and people have tried
[159.66 --> 160.78]  various things with these.
[160.92 --> 167.32]  So as we're sitting here in November 2025, like what is the kind of, like how would you
[167.32 --> 169.86]  pick apart that industry from your perspective?
[169.86 --> 171.36]  Like what are people trying?
[171.50 --> 173.46]  What are various approaches to that?
[173.54 --> 176.02]  What is the state of that technology, et cetera?
[176.16 --> 182.80]  For me to really appreciate how far we've come as a company and as an industry, it's good
[182.80 --> 188.54]  to even look just five years back and maybe even go back a few more years before that,
[189.02 --> 191.46]  where we started in 2016.
[191.82 --> 197.08]  We were working on a whole host of different tools all around the general AI space.
[197.08 --> 199.96]  And remember, this was before ChatGPT existed.
[200.62 --> 204.28]  This was before any LLM or crazy AI tools were available.
[204.90 --> 210.82]  It was when me and my co-founder were reading articles on deep learning and sequence-to-sequence
[210.82 --> 213.70]  applications and how to like make it work.
[213.70 --> 220.84]  We were using crude technologies in today's standards like BERT and really manual natural
[220.84 --> 223.92]  language processing libraries around that time.
[224.60 --> 231.26]  So it was a very different time when everyone wished and hoped that you could have AI understand
[231.26 --> 232.06]  conversations.
[232.66 --> 235.46]  And that was the essence of what we were trying to build.
[235.86 --> 238.84]  At the time, we didn't even call it an AI note taker.
[238.84 --> 242.84]  We were trying to build this general AI secretary or EA.
[243.56 --> 246.16]  And we needed to pay our bills.
[246.36 --> 251.30]  So we said, we've tried a bunch of different products in this space.
[251.42 --> 254.78]  So we need to figure out what's the thing that people are willing to pay for.
[255.24 --> 260.18]  And wouldn't it be a great idea if someone for $100 a month could get an executive assistant
[260.18 --> 264.64]  with a human in the loop and some AI in the background?
[264.64 --> 271.26]  So we went about building that, testing that out, learned a lot and realized having a human
[271.26 --> 273.10]  in the loop is there's no way this is going to scale.
[273.18 --> 278.98]  If we want to eventually build this into a platform used by millions of people every day,
[279.34 --> 284.94]  taking notes for you 24-7, capturing all those transcripts, there was just no way that
[284.94 --> 289.38]  human in the loop was going to build this sort of company.
[289.38 --> 294.94]  It was also right around the same time companies like Scale AI were created, where they were
[294.94 --> 297.88]  doing data labeling and the human in the loop processes.
[298.04 --> 300.64]  So we took inspiration from our peers at the time.
[300.80 --> 305.04]  But our ambitions were, I think, a little too grandiose.
[305.26 --> 307.66]  And we said, do we really want to build this business?
[307.88 --> 312.36]  Like the max we might be able to support is like 5,000 people, 10,000 people.
[312.36 --> 316.56]  And it's going to be an operations heavy business rather than an AI business.
[316.96 --> 320.22]  So that's when me and my co-founder said, you know what?
[320.82 --> 323.62]  We validated there's a market need for this.
[324.28 --> 330.40]  And within like trying it out for 10 of our close friends who were paying us enough money
[330.40 --> 335.44]  to pay for rent in San Francisco at the time, I feel like they were just, they felt bad for us.
[335.44 --> 339.70]  My co-founder got a place for $750 in SF.
[339.86 --> 342.40]  That's probably the biggest hustle at the time.
[342.56 --> 343.12]  Yeah, serious.
[343.40 --> 350.18]  And we were like, this is the only way to make things work is we just have to like rent our time.
[350.74 --> 353.76]  So as we built that, we validated it very quickly.
[354.20 --> 355.98]  And we did it without writing a line of code.
[356.40 --> 361.38]  After we did that experiment with like 10 of our friends, we said, if we really want to build a serious
[361.38 --> 364.88]  business, we know there's like a product market need here.
[364.88 --> 369.70]  Before we would write code for six months, we would ship something and no one would want to use it.
[370.08 --> 371.72]  And we would be wasting a lot of time.
[372.14 --> 376.60]  This is the first time where before we built anything or wrote a line of code, we validated the market.
[376.82 --> 378.42]  And we ourselves were the product, right?
[378.90 --> 381.86]  So fast forward, we ended up building the product.
[382.06 --> 385.72]  There was no category for AI Notetaker at the time.
[386.24 --> 390.16]  And that's when we created Fred, the AI Notetaker.
[390.50 --> 394.64]  We started with simple promises of, hey, one click, capture your meetings.
[394.64 --> 399.24]  You don't have to deal with like native recording on Zoom because every user, when they were using
[399.24 --> 404.72]  like local recordings, there was a limit to how much they could record on Zoom and other platforms.
[404.82 --> 408.48]  Some platforms like Google Meet didn't even offer an ability to capture meetings.
[408.82 --> 413.32]  So we started with a basic function of how can I record my calls so I can go back and play through them.
[413.32 --> 420.00]  Then we focused on transcription, but it was really expensive at the time and not very accurate.
[420.62 --> 421.38]  And we said, that's okay.
[421.44 --> 434.82]  Even if transcription is not perfect, as long as I can just search, index through the conversations and just go back to the general timeframe when we talked about dates or months or something, some important keyword that's good enough.
[435.12 --> 436.74]  That's how bad the tech was back then.
[436.74 --> 441.84]  So we built like a way to record your meetings, a way to search back through your meetings.
[442.30 --> 446.98]  Then as it got better, we built the transcription layer that you can actually read.
[447.36 --> 448.74]  Initially, there was no dashboard.
[449.50 --> 451.48]  It was just an email that we would send out.
[451.48 --> 461.76]  And then afterwards, we started building our own task detection and action item and keynote detection engine by hand.
[461.90 --> 462.50]  That was brutal.
[462.82 --> 468.76]  So we wrote the code for that using some off-the-shelf stuff and some custom scripts that I wrote at the time.
[469.58 --> 472.80]  And fast forward, we launched in 2020.
[473.08 --> 477.06]  So it was a four-year struggle of trying to figure out what we were trying to do.
[477.06 --> 478.44]  We launched in 2020.
[478.62 --> 480.98]  Still no chat GPT around that time.
[481.30 --> 494.38]  But the core product of being able to capture, search, and see some general bullets or sentence fragments was interesting enough that we got our first couple paid customers by the end of 2020.
[494.68 --> 497.98]  So it wasn't until 2021 that we actually started making revenue.
[498.34 --> 502.46]  And then fast forward, COVID happens, right?
[502.46 --> 508.92]  And so we get this proliferation of free users and then some of them turning into paid users.
[509.18 --> 511.64]  And then you accelerate through to 2022.
[512.04 --> 517.18]  We get early access to OpenAI's GPT 3.5.
[517.52 --> 521.20]  Vinod Khosla, who is an investor, also happened to invest in OpenAI.
[521.34 --> 522.90]  That really opened the floodgates for us.
[523.56 --> 525.76]  Again, LLMs were very expensive at the time.
[526.10 --> 527.08]  But we said, you know what?
[527.24 --> 529.54]  Let's go ahead and bring this in.
[530.26 --> 531.60]  It can't be that bad, right?
[531.60 --> 533.98]  Like whatever we're doing today, it's probably going to be better.
[534.10 --> 534.90]  It blew our mind.
[535.28 --> 537.06]  It changed the complete technology.
[537.78 --> 545.36]  And then from November 2022, so exactly three years ago to today, it's been an absolute rocket ship.
[545.60 --> 546.66]  We've never looked back.
[547.54 --> 554.82]  Company has grown, accelerated, crossed seven figures, and then eight figures in revenue and scaling beyond.
[554.96 --> 557.12]  So it's been very transformational.
[557.12 --> 562.90]  So I think it's fair to say we were lucky to be at the right place at the right time.
[563.36 --> 570.76]  But the more honest answer was we just showed up a little too early and we just tried to survive for what it's worth.
[570.76 --> 578.30]  And eventually, the bus came around and we were able to hop on the bus and then create this whole category of AI note-taking.
[578.80 --> 583.70]  And now it seems like the most obvious generative AI use case.
[583.78 --> 592.18]  Like if your company is working on something and you need to pivot because it failed, the first thing you look at is maybe we should just build another AI note-taker.
[592.28 --> 593.54]  It seems like it's working for Fireflies.
[593.64 --> 595.24]  We should try to copy them.
[595.24 --> 597.14]  So it's a very different space now.
[597.76 --> 598.34]  I'm curious.
[598.54 --> 599.56]  So that's fantastic.
[600.06 --> 601.58]  I love the history of that.
[601.66 --> 609.18]  And I love the incremental development of both the business and the technology as you described it.
[609.50 --> 617.76]  One of the things I'm wondering is it seems like early on you talked about that in the beginning you would write code for six months and ship it and people weren't using it.
[617.76 --> 625.82]  And you learned the lesson of kind of going and making sure you had a market before you did a major commitment on that.
[626.36 --> 641.22]  And as you've talked about the evolution from that point on, at what point did you start to see users changing their own behaviors in response to whatever state your product was in at the time?
[641.22 --> 653.24]  Like what were the things that you noticed where users would respond and they would change and adjust their own behavior based on the integration of the product into their own workflow?
[653.54 --> 659.90]  And how did that behavior change evolve over time as your product got more and more sophisticated and capable?
[659.90 --> 667.54]  All the other products that we built were easily buildable, but there wasn't a clear market demand for it.
[667.96 --> 676.08]  And we always looked at it from, is this feasible from an engineering point of view rather than, is this something that the market cares about?
[676.16 --> 679.30]  Is this solving a killer pain point for customers?
[679.72 --> 687.92]  So when we decided to build Firefly's the note taker, we said, let's forget what is even theoretically possible right now.
[687.92 --> 691.36]  Let's figure out what customers want and we'll work backwards from there.
[691.44 --> 692.60]  That was a fundamental shift.
[693.02 --> 704.72]  So when we had this experiment where we bootstrapped it with just my co-founder and I and a dozen friends where we were testing it for them, like we were the software.
[704.96 --> 706.84]  We were everything at that moment in time.
[707.20 --> 710.38]  And that was before there was a company really built.
[710.82 --> 715.06]  There was no business plan, but it was, is this something that's valuable enough to do?
[715.06 --> 718.82]  You validate it, but it's one thing to validate it with humans.
[718.84 --> 721.62]  And now another thing to build the technology.
[721.84 --> 724.76]  Both my co-founder and I were technical.
[725.00 --> 733.86]  We both like solving hard engineering problems and credit to Sam, my co-founder and CTO went to MIT, studied aeronautical engineering.
[734.40 --> 737.70]  And for him, computer science is like the easy stuff, right?
[737.76 --> 744.92]  The aeronautical engineering, he was working on drones, autonomous vehicles, that unmanned vehicles back in 2015, 2016.
[745.52 --> 751.46]  So I think like this is like, if I can solve that problem, how hard can this like machine learning problem be?
[752.04 --> 756.46]  That was like a, again, we got a little carried away, but it was a very hard problem.
[756.92 --> 763.44]  But we like, I think a lot of the best technologists in the world, they worry about the technology part afterwards.
[763.44 --> 764.88]  They're like, great.
[764.94 --> 770.14]  If it's a hard problem, we're going to find a lot of really smart people that want to get behind it and solve it.
[770.42 --> 774.80]  And we did the best we could with the technology that was available at the time.
[774.80 --> 788.72]  So to even be able to capture calls, stream them into the cloud, record them, store them, index them, search them, that itself was a hard problem with the resources that we had back then.
[788.94 --> 792.52]  And it was also very expensive to do all of this stuff.
[793.28 --> 798.64]  Transcription has gone down like 10x since that time we launched.
[798.64 --> 801.60]  So that's been an enabling factor for us.
[801.94 --> 806.36]  We've scaled our own infrastructure over the last five years where we manage our own bare metal servers.
[807.18 --> 809.30]  It's the volume is insane, right?
[809.30 --> 817.88]  Like we run maybe a great, we're a multi-cloud platform, but we run more of our traffic off of our own servers than on Google or AWS.
[818.28 --> 828.12]  So we've gotten to this economies of scale and done all of this hard work where the end user, they just look at Fireflies and says, oh, wow, it's $10 per month.
[828.12 --> 834.28]  And I'm getting this note taker that's going to join all my meetings all the time, every single day around the clock.
[834.82 --> 838.60]  Doing that in the past would have cost thousands and thousands of dollars to support.
[838.60 --> 843.68]  Like it doesn't make sense to charge someone $10 if it's going to cost you $1,000 to support that user.
[844.08 --> 850.58]  So the business innovation, the scaling itself was a, I think, a miracle.
[850.92 --> 855.74]  That was like a masterclass in how the engineering team got behind and solved it.
[855.74 --> 864.88]  Because not only you have to optimize for quality and reliability and uptime, but you also have to make it affordable enough where someone's going to be willing to pay $10 a month.
[865.26 --> 866.78]  And that was like a big feat.
[866.78 --> 873.78]  And since 2023, we've been profitable ever since we've started hyperskilling.
[873.86 --> 876.28]  So we've done all of this while being profitable.
[876.48 --> 881.90]  And we didn't touch any of our Series A funding that we had raised along the way.
[881.96 --> 883.02]  It was just our seed round.
[883.02 --> 898.24]  And that initial seed round was enough to like seed the initial free users, figure out our monetization strategy, build out our own infrastructure, and get it to a point where we found product market fit, we found customers, and we found revenue.
[898.24 --> 909.68]  So yeah, that was the different thing this time around was we did not stop ourselves or limit our dreams from what was technologically possible at the time.
[909.94 --> 917.10]  And we absolutely got lucky because we might not have been able to reach the success that we have today had it not been for LLMs.
[917.10 --> 921.52]  But one way or the other, maybe we would have been two years delayed, right?
[921.80 --> 925.24]  Eventually, this sort of technology would come out because that's how fast the industry was moving.
[925.84 --> 929.76]  And again, the credit was definitely to Sam on the forethought.
[930.00 --> 935.56]  Because every time we went to investors, they would tell us there's no way transcription is going to be accurate enough.
[935.64 --> 937.34]  There's no way transcription is going to be cheap enough.
[937.34 --> 942.38]  In fact, many investors told us, you can make good money with this human in the loop business.
[942.82 --> 945.30]  Why don't you just go turn that into an actual business?
[945.42 --> 947.46]  Like you ran this cool experiment with your friends.
[947.82 --> 948.98]  You should turn that into a business.
[949.58 --> 952.50]  And we were very strongly opposed to that.
[952.62 --> 954.08]  We said we want to build a software company.
[954.40 --> 955.82]  We don't want to deal with operations.
[956.38 --> 966.52]  And this is also from some battle scars from the past when we tried to build a food delivery app in college and the logistics behind it.
[966.52 --> 973.02]  So we said, never again are we going to do anything that requires logistics and on the ground stuff.
[973.20 --> 976.32]  So it was a series of optimistic decisions.
[977.04 --> 981.32]  And the technology ended up catching up to where we were vindicated.
[996.52 --> 1001.90]  So friends, you know that feeling when your team has brilliant ideas and you're excited.
[1002.20 --> 1008.92]  But these ideas, this innovation gets stuck behind endless meetings, scattered documentation.
[1009.64 --> 1015.24]  And when you're moving at this speed of bureaucracy instead of the speed of innovation, we've all been there.
[1015.42 --> 1021.22]  The gap between idea, execution, impact, all that good stuff, it is killing your team's progress.
[1021.22 --> 1024.68]  But here's the thing, simply throwing AI at a problem doesn't help.
[1024.90 --> 1026.12]  It just makes things messier.
[1026.56 --> 1028.86]  That's exactly why you should check out Miro.
[1029.12 --> 1034.46]  Miro is powered by AI and it transforms teamwork that normally takes weeks into days.
[1034.66 --> 1039.04]  Now I've used Miro to plan different ideas out, map complex workflows.
[1039.62 --> 1043.98]  And I've even generated fresh ideas from interviews all in one single place.
[1044.36 --> 1046.00]  And that is the power of Miro.
[1046.00 --> 1052.00]  It is like having a second brain with AI that actually thinks like you, like your team.
[1052.28 --> 1054.88]  No more switching between 10 different tools.
[1055.34 --> 1057.72]  Help yourself, help your team get great things done with Miro.
[1058.10 --> 1060.66]  Check out Miro.com to find out how.
[1061.02 --> 1063.58]  That is M-I-R-O dot com.
[1063.88 --> 1065.60]  Again, Miro dot com.
[1065.60 --> 1076.82]  Well, Krish, I'm wondering, you kind of alluded to the evolution of the technology, which of
[1076.82 --> 1078.98]  course has played a key role in that.
[1079.16 --> 1086.20]  And for our kind of AI practitioners and those that are really curious about more of the kind
[1086.20 --> 1091.86]  of AI engineering side in our audience, could you just kind of in generic terms, I'm sure
[1091.86 --> 1097.02]  you can't share everything about how everything works, but you had mentioned this evolution
[1097.02 --> 1102.62]  where it was kind of at first these transcription, earlier transcription models, which weren't
[1102.62 --> 1103.16]  that accurate.
[1103.16 --> 1109.32]  And maybe you training or building your own kind of set of other models that would do kind
[1109.32 --> 1115.58]  of task specific things like, you know, action item detector or whatever that is.
[1115.58 --> 1122.46]  So how does that kind, how does the approach to something like an AI note taker now with
[1122.46 --> 1127.58]  the, you know, the models that are available differ both in terms of like what is easier,
[1127.58 --> 1132.84]  but maybe also there's certain things that are challenging now, which you didn't have to
[1132.84 --> 1137.76]  think about before because of how the technology has, has evolved.
[1137.92 --> 1140.28]  Would love to hear that side as well.
[1140.64 --> 1145.46]  If you're using transcription engines today, like Whisper or one of the ASR providers today,
[1145.46 --> 1150.04]  and even some of the big ASR providers from the Googles of the world, Microsoft's of the
[1150.04 --> 1153.10]  world, you don't have to massage the output as much.
[1153.50 --> 1159.06]  That's exactly the word that we had to think about because the raw output was pretty crappy
[1159.06 --> 1161.08]  and we had to fix the grammar.
[1161.38 --> 1162.78]  We had to fix the punctuation.
[1163.38 --> 1166.98]  We had to figure out speaker identification at the time.
[1167.18 --> 1172.02]  So you're just getting a, you know, garbled up string of text and you're trying to make
[1172.02 --> 1172.72]  sense of that.
[1172.88 --> 1179.32]  And you also have to figure out how to identify certain type of words because for certain
[1179.32 --> 1183.70]  industries, certain work domains, there are different types of words that are out there.
[1183.94 --> 1186.48]  How do you deal with filler words, pauses, ums?
[1186.76 --> 1189.08]  Like we speak a lot of filler words.
[1189.14 --> 1194.14]  I feel like working on Fireflies has improved the way I speak and helped reduce the number of
[1194.14 --> 1198.68]  filler words I use because the first versions of Fireflies, every time I would read the ums
[1198.68 --> 1204.72]  and the ahs from my own meeting notes and recordings and transcripts, I'd be like, wow, I said it
[1204.72 --> 1205.42]  that many times.
[1205.42 --> 1209.02]  So we ended up building a little filter back in the day that told me like how many filler
[1209.02 --> 1210.02]  words I used in a meeting.
[1210.36 --> 1215.02]  And I would instantly like learn from that and say, oh, wow, I need to learn to speak
[1215.02 --> 1215.36]  slower.
[1215.50 --> 1217.28]  I need to be more enunciated.
[1218.10 --> 1223.14]  So the original text that was generated from transcription engines wasn't good enough.
[1223.14 --> 1229.70]  So we had to build a bunch of our own filters on top to clean up the output that was generated.
[1230.06 --> 1235.64]  And then we had to build other layers on top that would classify different parts of the
[1235.64 --> 1240.54]  meetings and then pull out what it thought were action items, what it thought were bullet
[1240.54 --> 1242.76]  point notes, what it thought were key ideas.
[1243.06 --> 1249.36]  And at the time it was very extractive, meaning you're just extracting pieces from this garbled
[1249.36 --> 1251.78]  up text and then you're calling that notes.
[1251.78 --> 1253.84]  And it's a shame.
[1254.04 --> 1256.34]  But at the time, that was good enough for a lot of people.
[1256.90 --> 1261.24]  So we had to like build, rebuild, re-architect things many times over.
[1261.30 --> 1267.14]  Whereas if a person was doing something today off the shelf, you don't have to do all of
[1267.14 --> 1267.28]  that.
[1267.36 --> 1273.14]  Like you can get to like 80% pretty solid just using off the shelf parts.
[1273.68 --> 1273.88]  Right.
[1273.94 --> 1277.10]  And that is something that we didn't have the luxury of.
[1277.10 --> 1284.54]  Now, you may ask, well, Krish, like if it's so easy now to build something 80%, 85% off
[1284.54 --> 1287.06]  the shelf, like what's the competitive mode?
[1287.16 --> 1289.50]  Like everyone should be able to do this.
[1289.90 --> 1296.54]  And I think the part there that we were fortunate enough, one is going really deep on the problem
[1296.54 --> 1299.94]  because the other 15% actually takes a long time.
[1300.04 --> 1302.04]  That differentiates good versus great.
[1302.04 --> 1305.30]  And you have to really polish the product.
[1305.72 --> 1308.00]  And those things take a very, very long time.
[1308.48 --> 1310.14]  And you have to learn from your users.
[1310.78 --> 1316.98]  The roadmap that we've been able to build out beyond the core tech for teams, for enterprises,
[1316.98 --> 1319.04]  that takes a lot of work.
[1319.12 --> 1322.28]  You have to think about access controls, privacy, storage.
[1322.28 --> 1325.16]  How do you think about multi-tenant?
[1325.24 --> 1329.50]  Like we're one of the first companies to get SOC 2 compliance in the AI meeting assistance
[1329.50 --> 1330.02]  space.
[1330.44 --> 1332.94]  And then HIPAA for doctors that want to use Fireflies.
[1333.38 --> 1339.36]  We offer this option for enterprises called private storage, where you can store Fireflies
[1339.36 --> 1346.18]  meetings inside your own server storage containers, which was another architectural change.
[1346.24 --> 1350.34]  If you don't architect it correctly in the beginning, it makes it very, very difficult.
[1350.34 --> 1356.52]  All this administrative sharing features, team features, which makes Fireflies more valuable
[1356.52 --> 1359.68]  as more and more people inside your organization start using it.
[1360.08 --> 1363.78]  Search was a really big problem that you have to solve over time as well.
[1364.18 --> 1368.72]  So all of this is enabled by great transcription and being able to understand language.
[1368.82 --> 1370.64]  I absolutely agree with that.
[1370.94 --> 1376.50]  But then all the use cases you have to build on top of it, like our Ask Fred example, where
[1376.50 --> 1379.84]  you can, instead of reviewing the notes or the meeting, you can just ask Fred questions
[1379.84 --> 1383.54]  about the meeting and it will catch you up on everything that happened.
[1383.66 --> 1383.80]  Right.
[1384.12 --> 1389.10]  So that required a lot of stuff like figuring out search from scratch and making that really
[1389.10 --> 1389.48]  effective.
[1390.46 --> 1398.12]  So, yeah, I think it was a big journey in terms of building out like these core building blocks.
[1398.12 --> 1402.94]  But as we were able to do that, when we started, it was a blue ocean.
[1403.52 --> 1407.78]  And going back to, I'm like Pogo sticking back between the commercials and technology part,
[1407.82 --> 1409.52]  because both are really important.
[1410.12 --> 1414.86]  If you want to be a great artist, you don't have to think about the commercialization of
[1414.86 --> 1415.70]  what you're building.
[1415.88 --> 1417.62]  You can just think about great art.
[1418.02 --> 1420.76]  But to build a great business, you have to be a good artist.
[1420.86 --> 1424.04]  And you also have to figure out, can someone pay me money for this?
[1424.04 --> 1431.38]  We were fortunate enough at the time to establish the AI note taker brand and be one of the
[1431.38 --> 1434.66]  first companies to start championing that word.
[1434.96 --> 1436.28]  And now it's an entire category.
[1436.80 --> 1441.88]  Build that AI note taker, get to distribution, get to millions of people using Fireflies.
[1441.98 --> 1446.20]  Today, like tens of millions of people get notes every month from Fireflies.
[1446.98 --> 1451.02]  That in itself, right, distribution is something that is super important.
[1451.02 --> 1456.86]  And because we started early when it was less obvious, we were able to make the most of it.
[1457.08 --> 1461.20]  Like there's no point in going to the gold rush after it's been announced and after someone's
[1461.20 --> 1465.24]  made a ton of money off of it or a killing off of it.
[1465.50 --> 1470.26]  I think like being there a little early helped us maximize the impact.
[1470.34 --> 1477.50]  Because for every nth note taker, every additional note taker that comes out, it becomes progressively
[1477.50 --> 1479.68]  harder for them to stand out in the crowd.
[1480.24 --> 1487.10]  And there is something to be said about these markets where distribution is one of the most
[1487.10 --> 1489.98]  important things to build in a PLG flywheel.
[1490.08 --> 1492.30]  That's why you don't see so many Calendly competitors.
[1492.44 --> 1493.54]  People still use Calendly.
[1493.66 --> 1496.66]  Like it's one of the de facto platforms that everyone uses.
[1497.16 --> 1502.06]  In our space, there's probably like three or so big players with Fireflies being one of
[1502.06 --> 1502.30]  them.
[1502.30 --> 1505.56]  And then each has its own like merits.
[1505.98 --> 1509.82]  Fireflies, for example, is very much focused on teams and businesses.
[1510.56 --> 1516.02]  And if you need like robust integrations and workflows and admin controls, you come to Fireflies.
[1516.30 --> 1520.74]  Whereas if you're looking for more of a prosumer type product, you'll go to one of the other
[1520.74 --> 1521.32]  platforms.
[1521.32 --> 1525.42]  So we had to pick what we wanted to do and go really deep in there.
[1525.42 --> 1530.94]  A good parallel I like to use also is like the project management space or the CRM space
[1530.94 --> 1534.84]  where you had Salesforce build a massive enterprise scale business.
[1535.18 --> 1539.86]  And then HubSpot comes along and takes a huge market out of the SMB business.
[1540.36 --> 1544.52]  Both are tens of billions of dollars in market value that's been captured.
[1544.64 --> 1546.80]  In project management, you have the Asanas of the world.
[1546.98 --> 1548.88]  You have the Monday.coms of the world.
[1549.18 --> 1552.50]  You have all of these like other project management systems that follow.
[1552.50 --> 1554.98]  So we've found our niche.
[1555.28 --> 1558.80]  I would say I wouldn't even say it's a niche because our niche is anyone that's a knowledge
[1558.80 --> 1560.28]  worker that works inside of a team.
[1560.80 --> 1568.28]  So we specifically say no to consumer grade use cases like university students, teaching,
[1568.68 --> 1569.68]  like those sort of stuff.
[1570.04 --> 1575.10]  Like our bread and butter has always been like if you're a team and it doesn't have to be
[1575.10 --> 1575.76]  in tech either.
[1575.84 --> 1580.32]  Like a lot of our customers are outside of tech, which was also really fascinating to see.
[1580.32 --> 1584.98]  But yeah, it's been a very long, tedious journey.
[1585.10 --> 1588.86]  I wouldn't have believed three years ago we'd be where we are today.
[1589.38 --> 1594.30]  But to answer your question on tech, yeah, it's been one of the most fascinating things
[1594.30 --> 1597.36]  about this space because now it feels super easy and everyone can do it.
[1598.04 --> 1601.68]  You hit on so many things there that I'm interested in.
[1602.10 --> 1607.04]  Like one of the things I think that I think I just learned something from you definitely on
[1607.04 --> 1609.42]  and that I will probably try to share.
[1609.72 --> 1614.04]  And I'm kind of, I'd like to generalize it towards not strictly a, a Firefly thing because
[1614.04 --> 1617.62]  I think there's a lot of people in our audience that can learn from this in whatever industry
[1617.62 --> 1624.02]  they're in is, is your kind of your pursuit of a sustainable competitive advantage and
[1624.02 --> 1625.08]  what that meant to you.
[1625.08 --> 1630.90]  And it sounds like, uh, in your case, um, being there early and having to solve, you
[1630.90 --> 1634.50]  know, the whole problem and not, you know, unlike people that would come in later and
[1634.50 --> 1635.86]  get to that 80% easily.
[1636.10 --> 1640.28]  And you have that last 15 or 20%, which is, which is really hard.
[1640.40 --> 1649.02]  You were well positioned to develop the expertise in your organization and to find the niches that
[1649.02 --> 1654.12]  you wanted to service and get their first and best with that expertise to do that.
[1654.12 --> 1660.14]  So that even as, even as the space has, uh, developed other competitors, you were able
[1660.14 --> 1665.06]  to, to hold them off and hold your niche and be a powerhouse in that way.
[1665.06 --> 1669.34]  Is that, is that a fair representation of kind of what you were just saying?
[1669.78 --> 1673.94]  Yeah, this was one of those, uh, situations where being early definitely helped.
[1673.94 --> 1678.88]  And then having the time to keep building and refining it and listening to your users over
[1678.88 --> 1679.24]  time.
[1679.66 --> 1681.86]  A lot of people claim that SAS is dead.
[1681.94 --> 1683.38]  Everyone will build their own SAS.
[1683.86 --> 1690.26]  But in reality, that extra 15 to 20% of work you have to do to build it, maintain it, customize
[1690.26 --> 1690.70]  it.
[1691.22 --> 1693.08]  I don't think most companies want to deal with that, right?
[1693.10 --> 1694.92]  They have other, they have a business to run.
[1695.30 --> 1697.50]  They don't want to be building these tools in house.
[1697.92 --> 1703.02]  So when we look at our customers and look at the things that we want to offer to them, we
[1703.02 --> 1708.42]  have 95 plus different integrations, for example, that was a competitive moat for us over time
[1708.42 --> 1714.18]  because we wanted to be the most integrated AI meeting assistant on the platform, uh, on the
[1714.18 --> 1714.48]  market.
[1714.64 --> 1719.44]  We also wanted to really take the security thing and be the most secure AI note taker
[1719.44 --> 1720.32]  for people.
[1720.32 --> 1724.96]  So that means like when you work with enterprises and businesses, they have thousand question
[1724.96 --> 1727.58]  questionnaires on like all the security compliance stuff.
[1727.64 --> 1728.86]  You have to deal with their CIOs.
[1728.86 --> 1734.66]  You have to like build all of these like layers and features like audit logs and, uh, all these
[1734.66 --> 1735.72]  compliance features.
[1736.02 --> 1738.28]  That is a pain to do, right?
[1738.30 --> 1741.36]  Like forget about the AI, but just building the SAS part of it.
[1741.36 --> 1744.86]  It's like user groups, admin controls, data retention.
[1744.86 --> 1748.90]  Like some customers, like in the finance industry want their data wiped every seven days.
[1748.90 --> 1754.02]  So building all of these sorts of things, uh, help definitely build the moat, but we're shipping
[1754.02 --> 1757.92]  10, 20 different features or enhancements every week.
[1757.98 --> 1760.48]  And you do that over a span of five years.
[1760.56 --> 1761.64]  It compounds.
[1761.96 --> 1767.72]  That's why I feel like whenever a big player gets into a space and someone says, oh, this
[1767.72 --> 1768.80]  company's dead now.
[1768.88 --> 1775.76]  But what ends up happening is there, the other company has built so much that it, it's very
[1775.76 --> 1777.28]  hard for you to want to switch over.
[1777.28 --> 1782.58]  And a company that I like to reference, and I think they're doing a really great job of
[1782.58 --> 1786.66]  it is 11 labs, like with text to speech.
[1786.84 --> 1790.72]  They went so deep on a problem where many people would say, oh, this is generic.
[1790.72 --> 1794.74]  Like anyone can do text to speech now, like open AI or one of the big players will just
[1794.74 --> 1796.50]  do text to speech and offer it as an API.
[1796.50 --> 1803.76]  But if you look at the amount of stuff that 11 labs provides to their customers and going
[1803.76 --> 1809.02]  really deep on what your users need, it's an all in one, very comprehensive platform.
[1809.26 --> 1811.54]  And it gives you so much to choose from.
[1811.96 --> 1812.08]  Sure.
[1812.16 --> 1817.70]  You might lose out on the 10 or 20% of prosumer type users if other players come in and solve
[1817.70 --> 1819.06]  the general use case.
[1819.16 --> 1821.38]  But that's the whole point of the company, right?
[1821.90 --> 1825.20]  Product market fit is not about finding it once and you're good for life.
[1825.20 --> 1828.62]  You have to keep finding product market fit over and over again.
[1828.62 --> 1832.86]  And you have to keep adapting as the market changes, your company has to change.
[1832.86 --> 1834.04]  Otherwise, you become stale.
[1834.68 --> 1840.86]  Like the reason you have CRM companies that were in the 90s versus in the 2000s versus
[1840.86 --> 1846.24]  now, they all fell out of product market fit and had to keep innovating and keep getting
[1846.24 --> 1847.60]  back into product market fit.
[1848.18 --> 1852.42]  So yeah, being early helpful, listening to customers and having five years to build out
[1852.42 --> 1853.52]  the roadmap, super helpful.
[1853.86 --> 1858.52]  And I'm one of those people that definitely believes SaaS is not dead.
[1858.78 --> 1861.48]  And most people don't want to build their own tools.
[1861.58 --> 1861.86]  Trust me.
[1861.86 --> 1863.76]  It's not worth the hassle.
[1864.12 --> 1865.76]  You got bigger and better things to do.
[1865.76 --> 1886.30]  If your team is still jumping between design tools just to update the website, that's
[1886.30 --> 1887.20]  not fun.
[1887.48 --> 1891.82]  Maybe you're stuck behind expensive paywalls for basic design features.
[1891.82 --> 1892.56]  Here's the thing.
[1892.56 --> 1896.28]  Most design tools make you pay just to get started.
[1896.36 --> 1897.54]  That's not Framer's way.
[1897.84 --> 1899.06]  Our sponsor today is Framer.
[1899.36 --> 1903.84]  They already built the fastest way to publish beautiful production ready websites.
[1904.12 --> 1906.88]  And it's now redefining how we design for the web.
[1906.98 --> 1912.70]  With the recent launch of Design Pages, a free canvas based design tool, Framer is more than
[1912.70 --> 1913.30]  a site builder.
[1913.30 --> 1919.26]  It's a true all-in-one design platform from social media assets to campaign visuals to
[1919.26 --> 1923.30]  vectors and icons all the way to a live site.
[1923.70 --> 1927.28]  Framer is where ideas go to live, start to finish.
[1927.56 --> 1929.52]  Here's what I love about this tool.
[1929.70 --> 1931.88]  It is an all-in-one tool.
[1932.20 --> 1937.12]  You don't have to switch to Figma for design and then have these messy HTML exports.
[1937.12 --> 1939.48]  You don't have separate tools for graphics.
[1939.68 --> 1945.50]  With Framer's free tier, you get unlimited projects, unlimited pages, and you even get
[1945.50 --> 1946.74]  unlimited collaborators.
[1947.38 --> 1950.48]  Vector tools, 3D transforms, animations, it's all there.
[1950.84 --> 1952.32]  That's what sets Framer apart.
[1952.44 --> 1955.62]  It's not just another site builder like Webflow or Wix.
[1955.80 --> 1960.42]  It is a complete design tool that happens to publish production ready websites.
[1960.74 --> 1961.82]  It's everything you need.
[1961.92 --> 1962.60]  It's totally free.
[1962.60 --> 1968.16]  So if your team is ready to design, iterate, and publish all in a single tool, start creating
[1968.16 --> 1975.18]  for free today at Framer.com slash design and use the code practical AI and get a free
[1975.18 --> 1976.32]  month of Framer Pro.
[1976.78 --> 1982.54]  That's Framer.com slash design and use the promo code practical AI.
[1982.90 --> 1983.94]  That's all in word.
[1984.46 --> 1987.76]  Framer.com slash design, promo code practical AI.
[1988.20 --> 1991.48]  Rules and restrictions may apply, but check it out today.
[1992.60 --> 2001.18]  Well, Krish, I definitely want to shift now to some of the things that are, of course,
[2001.24 --> 2006.34]  really exciting that you have either just released or are coming on the roadmap with Fireflies
[2006.34 --> 2011.08]  and kind of some of what's enabled that from the technology standpoint, some of the challenges
[2011.08 --> 2013.60]  related to that, some of the value that that brings.
[2014.14 --> 2019.54]  One of the big things that we were talking about before we hit the record button was real
[2019.54 --> 2020.58]  time functionality.
[2020.58 --> 2027.82]  So could you describe a little bit of what is coming out in relation to real time and
[2027.82 --> 2030.48]  also kind of the why of that?
[2030.64 --> 2038.84]  Like why people would want that, what it enables, and maybe why that hasn't come out yet in terms
[2038.84 --> 2041.04]  of the technology side of things?
[2041.54 --> 2045.06]  You know, what has enabled that at this point in time?
[2045.06 --> 2053.26]  One of the biggest things that I always found when I talked to customers was how can we help
[2053.26 --> 2056.60]  them in the moment while the meeting itself is happening?
[2057.06 --> 2062.98]  Today, people were using Fireflies where they would get meeting notes a few minutes after
[2062.98 --> 2063.42]  the meeting.
[2063.56 --> 2068.16]  It would help them be their second brain and jog their memory after the fact.
[2068.16 --> 2074.96]  But what if Fireflies could really level up your conversation while the meeting is happening?
[2075.40 --> 2080.48]  It can serve as that person that taps you on the shoulder and guides you when you get stuck
[2080.48 --> 2086.42]  on a sales call or you're interviewing a candidate and you need more context on who that person
[2086.42 --> 2088.76]  is or what the past interviews with that person were.
[2088.76 --> 2096.18]  So, we've rolled out what we're calling live assist, where Fireflies will assist you while
[2096.18 --> 2097.00]  the meeting is happening.
[2097.22 --> 2101.22]  It's like having someone that serves as autocomplete for your meetings.
[2101.94 --> 2106.70]  And we'll talk about the technology part after that enabled all of this.
[2106.78 --> 2112.90]  But the core piece of this is as I'm having a meeting, Fireflies will give me detailed meeting
[2112.90 --> 2115.12]  prep before we even get into the conversation.
[2115.22 --> 2116.18]  Who am I talking to?
[2116.18 --> 2119.34]  What did we talk about last time we met like three months ago?
[2119.76 --> 2122.04]  Giving me all of that context before a meeting.
[2122.50 --> 2127.36]  And then during a meeting, giving me cues and live suggestions while we're talking about
[2127.36 --> 2128.08]  different topics.
[2128.14 --> 2131.82]  If it's a general meeting, we might have talked about some topic in the past.
[2131.96 --> 2133.18]  It's being mentioned right now.
[2133.64 --> 2136.58]  Fireflies will say, hey, do you want me to pull this up and prime you on it?
[2136.88 --> 2140.74]  Let's say you got distracted for a few minutes while the meeting was happening, checking your
[2140.74 --> 2141.76]  phone or notifications.
[2141.76 --> 2146.98]  And instead of asking the team to repeat themselves, you can press this button called Catch Me Up
[2146.98 --> 2148.32]  and it will catch you up.
[2148.72 --> 2153.08]  If you want to ask questions about some topic you're talking about, let's say we're talking
[2153.08 --> 2158.58]  about rockets and how expensive it is to build one of these SpaceX rockets.
[2159.20 --> 2160.60]  I don't have to switch tabs anymore.
[2160.76 --> 2162.94]  Fred is right there and I can just ask the question.
[2163.30 --> 2168.38]  Thanks to our partnership with Perplexity, I'm bringing the power of the web into the meetings
[2168.38 --> 2171.18]  while it's happening through our Live Assist.
[2171.74 --> 2177.08]  So our Live Assist knows from your past knowledge, from all of your past meetings, which is a
[2177.08 --> 2182.84]  unique advantage to Fireflies because if you've had years, months, hundreds, thousands of meetings
[2182.84 --> 2188.36]  on Fireflies, that second brain is now available to you in real time while the meeting is happening.
[2188.60 --> 2192.74]  You will be like the most knowledgeable person with perfect memory while the call is happening,
[2192.94 --> 2194.16]  not just after the call.
[2194.16 --> 2200.00]  And then the power of what's happening in real time during the meeting because we get distracted,
[2200.64 --> 2204.54]  but Fireflies has perfect attention span during the meeting and remembers everything that's
[2204.54 --> 2205.04]  going on.
[2205.52 --> 2211.56]  And it will also give you real time notes while the call is happening, real time transcripts
[2211.56 --> 2213.78]  as the call is happening so you can refer back to it.
[2214.16 --> 2218.52]  So on top of suggestions, you're getting real time notes and real time transcripts.
[2218.52 --> 2224.94]  And the best part of all of this is also you're getting the power of the web available to you
[2224.94 --> 2225.68]  at your fingertips.
[2226.20 --> 2227.64]  So that is our Live Assist product.
[2228.28 --> 2230.90]  And then we've built different versions of this.
[2231.16 --> 2237.68]  So if you're on a sales call, you can enable Sales Assist and you can upload all of your sales
[2237.68 --> 2239.30]  docs, FAQs, wikis.
[2239.30 --> 2243.94]  And imagine I'm on a very important deal with a prospect.
[2244.28 --> 2246.78]  They ask me about what is your enterprise offering?
[2247.28 --> 2250.72]  How does your enterprise offering differ from XYZ competitor?
[2251.56 --> 2253.30]  And you don't want to get stuck.
[2253.44 --> 2254.72]  You want to know what to say.
[2255.24 --> 2259.02]  Fireflies will give you real time suggestions based on all of your knowledge bases.
[2259.58 --> 2261.12]  Hey, this is how you answer this question.
[2261.22 --> 2262.64]  So real time sales coaching.
[2262.64 --> 2269.16]  Or if I'm recruiting and interviewing a candidate and I want some more context on things that
[2269.16 --> 2273.40]  they've said in their resume or things that they've said in past meetings, it'll tell me
[2273.40 --> 2275.86]  you should probably dive deeper into this experience.
[2276.26 --> 2278.94]  Like that will be something that the last interviewer didn't go into.
[2279.36 --> 2280.10]  You should do that.
[2280.42 --> 2284.60]  So making sure you have more effective meetings, hopefully less repetitive meetings.
[2285.22 --> 2288.96]  And if you're fully attentive, if every person could be fully attentive with a click
[2288.96 --> 2291.06]  of a button, that's what Live Assist is.
[2291.06 --> 2298.72]  And then to add to that, we felt the best form factor for Live Assist was going to be through
[2298.72 --> 2300.40]  a desktop application.
[2301.10 --> 2307.24]  And that's also a big announcement because today everyone knows about the Fireflies meeting
[2307.24 --> 2309.52]  bot that joins your meetings, the note taker bot.
[2310.00 --> 2314.88]  We also have customers that would like to have a experience that doesn't involve a bot.
[2315.16 --> 2318.16]  And that has been something that our customers have requested.
[2318.16 --> 2321.06]  So the desktop app serves a couple different functions.
[2321.46 --> 2326.00]  One is you'll be able to capture your meetings, get notes without having a bot.
[2326.66 --> 2330.40]  You'll be able to capture meetings on platforms beyond traditional video conferencing platforms.
[2330.54 --> 2336.78]  So a lot of people have spontaneous meetings on Slack huddles or on Discord or any other platforms
[2336.78 --> 2338.40]  where the bot usually could not join.
[2338.54 --> 2341.36]  You could do that on top of the Zoom, the Teams and the Google Meets.
[2341.36 --> 2346.80]  You also have a much cleaner, slicker, real-time UI where you can see all of these Live Assist
[2346.80 --> 2351.52]  suggestions in a panel right then and there.
[2351.76 --> 2356.32]  The nice thing about Fireflies is you can use Live Assist, whether it's on desktop, whether
[2356.32 --> 2359.68]  it's on mobile, whether it's on web or even our Chrome extension.
[2359.88 --> 2361.72]  We've always been multi-platform.
[2361.72 --> 2372.12]  But the desktop app offers this really nice extension of our surface area because our ultimate goal is work happens everywhere
[2372.12 --> 2375.92]  and it's happening when you're having scheduled meetings or in-person meetings.
[2376.02 --> 2378.46]  That's why I use the mobile app to capture in-person meetings.
[2378.64 --> 2383.80]  Or it's happening, well, very impromptu where you tell a team, let's get on a huddle and let's have a call.
[2384.06 --> 2389.38]  So we want to be everywhere where you're having these conversations so that we can help you capture that knowledge.
[2389.38 --> 2402.44]  And that's why we're super excited both with Live Assist helping you in real time and then, two, having a desktop platform where getting the most out of the experience will be really seamless.
[2403.22 --> 2416.66]  I'm curious, as you guys have been testing this internally with the team and everything, you've kind of gone through a whole bunch of behavioral adjustments and use cases, which I would have asked if you hadn't offered them up.
[2416.66 --> 2425.76]  And I'm curious, as you guys have experienced it yourself prior to going to market here, what surprised you about it in terms of your own reaction?
[2425.94 --> 2431.78]  So there's the vision that you have that your team is realizing as they're putting the product together.
[2431.78 --> 2446.00]  But when you're actually using it, what has made you, what has surprised you as the leader of this team in a way that maybe wasn't exactly what you were expecting, maybe gave you an extra superpower that you hadn't really counted on?
[2446.16 --> 2449.80]  Any insights there into your own moment of kind of wow?
[2449.80 --> 2458.82]  When we're looking at the initial Live Assist data, what fascinated me, my initial hypothesis was everything will be based on the suggestions we provide them.
[2458.92 --> 2461.00]  We're going to be suggesting things proactively.
[2461.16 --> 2464.06]  The proactive suggestions is where all the magic is going to happen.
[2464.42 --> 2465.68]  People are engaging with that.
[2466.30 --> 2478.42]  But what's super interesting is the manual engagement with Fred on Live Assist, being able to ask manual queries, has shot up even more than what we had in the past.
[2478.42 --> 2482.90]  We thought manual queries would go down because everyone would just use the suggested Live Assist.
[2483.30 --> 2490.74]  In fact, the suggestions are this great fodder for them to actually, I want to dive deeper into that topic.
[2490.74 --> 2496.78]  So they'll click on the suggested tile, but then they'll go ask a bunch of follow-up questions even more.
[2496.92 --> 2505.10]  So we're seeing like increased usage of Ask Fred and an increased usage of follow-up questions because the Live Assist is serving as a great nudge.
[2505.10 --> 2510.74]  And that's a really interesting behavioral change because we thought like, yeah, maybe they'll look at one or two suggestions.
[2511.06 --> 2512.14]  It's something passive.
[2512.44 --> 2519.06]  But when someone opens that panel, the intensity of usage is a lot higher.
[2519.06 --> 2528.12]  And then the distribution of usage where the manual engagement, like the manual queries, is equal or surpassing the automated suggestions that are happening.
[2528.62 --> 2536.48]  So that means like the automated suggestions are doing a good job of piquing someone's curiosity to want to dive deeper.
[2537.02 --> 2537.18]  Right?
[2537.18 --> 2543.22]  Like when you see like a suggested search result on Google, you kind of go down that rabbit chain.
[2543.28 --> 2549.30]  Or similarly, when you see what to watch next on YouTube, you go down that rabbit chain or rabbit hole.
[2549.40 --> 2555.74]  So that's something that was super interesting to us where our suggestions are actually helping people talk to Fireflies more.
[2555.74 --> 2563.86]  And this gives me that like her type, the movie sort of example where you're having this AI that's like helping you.
[2564.04 --> 2566.84]  And it knows and it's learning like, okay, this is relevant to you.
[2566.84 --> 2568.38]  You probably want to catch up on this topic.
[2568.58 --> 2570.12]  You might not know about this topic.
[2570.38 --> 2572.22]  Do you want me to like pull this information up?
[2572.66 --> 2583.32]  So being able to have the, you know, your IQ points jump up by another 10 or 20 on a meeting because you now have perfect memory and perfect awareness.
[2583.32 --> 2586.78]  And you know about the context of everything that's going on.
[2587.08 --> 2591.12]  It's like having these like super like special glasses that you're wearing that lets you see everything.
[2591.40 --> 2591.48]  Yeah.
[2592.00 --> 2596.14]  Well, I'm really excited to try the live assist.
[2596.28 --> 2598.22]  I think that's amazing.
[2598.58 --> 2606.50]  I've definitely needed that assist that I haven't had in meetings because of my own cognitive limitations.
[2606.50 --> 2614.16]  But yeah, I'm wondering, Krish, as you look forward, I mean, you've had quite a journey thus far.
[2614.36 --> 2619.08]  You've released, of course, some amazing stuff even just this last week.
[2619.62 --> 2627.40]  But as you look to kind of the future, especially kind of maybe even from a broader context of where the industry is going,
[2627.52 --> 2632.70]  how companies are being influenced by this AI kind of driven workflows,
[2632.70 --> 2635.98]  workflows or maybe specific things with Fireflies.
[2636.16 --> 2645.88]  What is most exciting for you as you kind of look to the next year of things that are open challenges that you're looking forward to digging into
[2645.88 --> 2655.34]  or things that are positive and interesting that you're seeing in terms of how people are using the technology or where it could go?
[2655.52 --> 2656.48]  Any thoughts?
[2657.04 --> 2660.68]  We try not to hold super long term roadmaps.
[2660.68 --> 2662.64]  I know that sounds contrarian.
[2663.08 --> 2666.84]  If you're working in technology, you have to have a vision of the future.
[2667.34 --> 2670.32]  We believe where the technology trends are going to be going.
[2670.50 --> 2671.48]  Like we understand that.
[2671.64 --> 2673.28]  But so much can change in a year.
[2673.38 --> 2674.64]  So much can change in six months.
[2674.78 --> 2677.46]  Heck, in like six weeks, so much can change with AI.
[2678.00 --> 2683.72]  We have a general sense of the direction that we want to go, but no like fixed long term plans.
[2683.88 --> 2687.38]  You have a plan and then you make things up as you go.
[2687.46 --> 2688.64]  That's how we do things.
[2688.64 --> 2695.86]  But a couple of things that are coming in the near future that I'm personally excited about is our involvement in hardware.
[2695.86 --> 2707.66]  When I said that I want Fireflies to be everywhere, whether you're capturing in-person meetings on your phone with the mobile app or you're on your Chrome extension or you have the meeting bot on the web or the desktop app,
[2707.66 --> 2726.12]  we are going to be announcing something really exciting that hopefully will be available on 10 million devices sometime next year, which brings the power of Fireflies to everyday devices that you probably are already using with some well-known brands.
[2726.12 --> 2728.34]  So that's something I'm very excited about.
[2728.62 --> 2736.88]  Like I personally didn't want to get into hardware, didn't think about hardware at this time, but it increases our surface area tremendously.
[2736.88 --> 2743.00]  And whatever we talked about with that movie, her or this ambient AI that's always available assisting you.
[2743.10 --> 2747.00]  That's the general trend that I do see the market going.
[2747.00 --> 2758.28]  So I also believe when you look at where these LLMs have gotten, GPT-4, like the affordability of it has cut down by a thousand X.
[2758.50 --> 2771.40]  So I do believe at some point in time, we will have technology, really powerful technology, LLMs that can run on device, on edge, 24-7, low cost, low latency all the time.
[2771.40 --> 2776.06]  And I think that will open up incredible amounts of use cases for people.
[2776.48 --> 2779.18]  So that's a general trend I believe in and we're heading towards.
[2779.66 --> 2781.56]  So the hardware angle is interesting for us.
[2781.98 --> 2787.46]  And then for us as a company, we look at our own processes and tools that we built internally.
[2787.46 --> 2802.42]  And we realized some of these tools could actually be valuable for companies beyond Fireflies because we built a very unique set of tools that help us operate really quickly and execute really fast with just 100 people.
[2803.32 --> 2807.92]  And what I really believe was Fireflies was one of the first AI agents.
[2808.04 --> 2809.44]  We never used the word agent at the time.
[2809.50 --> 2810.54]  We used bots and stuff.
[2810.54 --> 2821.34]  But if we can do this sort of value add for meetings, what other parts of knowledge work can Fireflies provide knowledge, can provide value add?
[2821.42 --> 2823.04]  That's something that I'm thinking a lot about.
[2823.58 --> 2830.62]  And hopefully next year, we'll be able to announce a few products that takes Fireflies well beyond meetings.
[2830.62 --> 2838.56]  And that brings this concept of AI agents and humans working side by side to reality.
[2838.74 --> 2842.30]  So that's something I'm very excited about that we are in the works on right now.
[2842.82 --> 2846.56]  Yeah, those will be two big things that I'm looking forward to for the future.
[2847.30 --> 2847.44]  Cool.
[2847.66 --> 2850.22]  Well, make sure you shoot us a message.
[2850.32 --> 2859.98]  Come back on the show to let us know how all of that worked out and talk about those things that you can't quite share yet, but sound very exciting.
[2859.98 --> 2886.44]  And yeah, thank you for serving as an example, early example of just really digging in and making something like the AI note taking, something that is actually bringing value to people's lives through AI, which is, of course, encouraging and definitely goes beyond the kind of AI hype or AI bubble or however you want to put it to kind of real value and real revenue.
[2887.10 --> 2889.42]  And yeah, just an amazing example.
[2889.42 --> 2891.16]  So thanks for taking time to join us.
[2891.26 --> 2892.72]  Hope to talk to you again soon.
[2893.24 --> 2893.90]  That was a lot of fun.
[2894.04 --> 2894.36]  Thank you.
[2894.48 --> 2894.98]  Thank you, guys.
[2901.42 --> 2902.62]  All right.
[2902.82 --> 2904.20]  That's our show for this week.
[2904.58 --> 2911.48]  If you haven't checked out our website, head to practicalai.fm and be sure to connect with us on LinkedIn, X or Blue Sky.
[2911.48 --> 2917.46]  You'll see us posting insights related to the latest AI developments, and we would love for you to join the conversation.
[2917.96 --> 2921.74]  Thanks to our partner, Prediction Guard, for providing operational support for the show.
[2922.08 --> 2924.06]  Check them out at predictionguard.com.
[2924.48 --> 2928.10]  Also, thanks to Breakmaster Cylinder for the beats and to you for listening.
[2928.44 --> 2929.24]  That's all for now.
[2929.54 --> 2931.28]  But you'll hear from us again next week.
[2931.28 --> 2932.94]  Because you're on Facebook at the beat.
[2932.94 --> 2933.04]  Bye.
[2933.04 --> 2933.66]  Bye.
[2933.68 --> 2933.92]  Bye.
[2933.92 --> 2933.94]  Bye.
[2934.08 --> 2934.44]  Bye.
[2934.56 --> 2934.94]  Bye.
[2934.94 --> 2935.32]  Bye.
[2943.82 --> 2943.92]  Bye.
[2943.98 --> 2944.18]  Bye.
[2944.18 --> 2944.46]  Bye.
[2944.56 --> 2945.50]  Bye.
[2945.50 --> 2946.58]  Bye.
[2947.26 --> 2947.48]  Bye.
[2947.58 --> 2948.22]  Bye.
[2956.92 --> 2956.96]  Bye.
[2957.00 --> 2957.38]  Bye.
[2957.54 --> 2957.62]  Bye.
[2957.62 --> 2958.96]  Bye.
[2959.22 --> 2961.18]  Bye.
