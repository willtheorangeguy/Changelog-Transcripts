[0.00 --> 8.58]  Welcome to Practical AI.
[9.16 --> 18.70]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies are changing the world, this is the show for you.
[19.18 --> 24.62]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you listen.
[24.88 --> 26.70]  Check them out at Fastly.com.
[26.70 --> 31.96]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.40 --> 36.02]  No ops required. Learn more at fly.io.
[42.92 --> 46.42]  Welcome to another episode of Practical AI.
[46.80 --> 48.28]  This is Daniel Whitenack.
[48.38 --> 54.58]  I am the founder and CEO of Prediction Guard, and I'm joined as always by my co-host, Chris Benson.
[54.96 --> 55.66]  How are you doing, Chris?
[55.66 --> 57.44]  Doing great. How's it going today?
[57.88 --> 59.02]  It is going awesome.
[59.24 --> 63.14]  It is, I don't know if you heard, but it is the advent of Gen AI.
[63.52 --> 69.42]  That is, I'm participating in this advent of Gen AI hackathon with Intel.
[69.66 --> 74.22]  So people are getting hands-on with a bunch of open source models and different hardware.
[74.76 --> 80.68]  So I've been in Slack all day answering questions and seeing cool prompts and seeing cool output.
[80.88 --> 82.70]  So it's just been a ton of fun.
[82.70 --> 86.38]  What's the most interesting thing that's been in terms of what you've seen so far?
[86.42 --> 87.54]  I'm just curious before we go on.
[87.92 --> 90.68]  The first challenge, so we're only a day in.
[90.86 --> 96.92]  The first challenge was to generate a series of images that kind of go in a sequence, kind
[96.92 --> 99.04]  of like a comic strip that tell a narrative.
[99.26 --> 101.22]  But there were some really amazing ones.
[101.22 --> 105.82]  One's kind of a child growing up and then him having a son.
[106.06 --> 109.58]  And the images were really compelling and the narrative was really interesting.
[110.14 --> 114.54]  Yeah, just very, very creative output is something that I've noticed.
[114.94 --> 117.08]  And today is all about chat.
[117.18 --> 121.38]  So we're going to see some chatbots popping up in the hackathon and really looking forward
[121.38 --> 121.78]  to that.
[121.78 --> 123.08]  Sounds like fun.
[123.52 --> 123.72]  Yeah.
[123.90 --> 131.30]  And, you know, the hackathon is all centered around these openly accessible or open source
[131.30 --> 134.28]  or permissively licensed generative AI models.
[134.88 --> 140.40]  I think it's really fitting because we have with us Casper, who is a longtime open source
[140.40 --> 147.42]  enthusiast, but also one of the contributors to the recently published State of Open Source
[147.42 --> 149.20]  AI book from Prem.
[149.56 --> 150.48]  So welcome, Casper.
[150.48 --> 151.56]  It's great to have you with us.
[151.84 --> 152.00]  Hello.
[152.18 --> 152.38]  Yes.
[152.46 --> 152.60]  Yeah.
[152.64 --> 153.26]  Great to be here.
[153.64 --> 153.90]  Yeah.
[154.16 --> 158.24]  Well, I mentioned you're a longtime open source enthusiast.
[158.44 --> 163.98]  How did you kind of get enthused about open source AI specifically?
[164.16 --> 169.64]  So what was your own kind of journey into open source AI, maybe kind of leading up to this
[169.64 --> 170.86]  book and what it's become?
[171.34 --> 172.30]  That's a good question.
[172.42 --> 176.82]  I've been around for long enough that AI didn't really exist as a thing back when I got into
[176.82 --> 177.36]  open source.
[177.36 --> 179.50]  And it was honestly just purely a hobby.
[179.50 --> 181.94]  I never even considered it as a career.
[182.56 --> 185.26]  This was, I must have been, what, 15 years ago or something.
[185.52 --> 190.28]  And I, in fact, I felt ashamed and embarrassed every time I was working in open source because
[190.28 --> 194.50]  it felt like I should have been spending that time working on an actual career, right?
[194.50 --> 196.52]  It felt like it was just a toy.
[197.14 --> 202.20]  I had a very long commute to get between my home and the workplace on a train and I was
[202.20 --> 204.04]  just coding away on my phone.
[204.40 --> 207.42]  I actually installed Debian site loaded on my Android.
[207.42 --> 211.00]  And yeah, that got me hooked on open source purely as a hobby.
[211.34 --> 215.38]  And I mean, if you contribute enough and you're happy making mistakes in public, you know,
[215.38 --> 218.38]  eventually it builds something that loads of people start using.
[218.52 --> 219.90]  It spirals out of control.
[220.26 --> 223.24]  Before you know it, it suddenly turns into a career.
[223.24 --> 227.54]  So I probably entered into this whole space in an unconventional way.
[227.68 --> 232.60]  I didn't intend to, you know, make things that would become famous, but they just wound
[232.60 --> 234.68]  up becoming famous, which is, you know, quite pleasant.
[234.96 --> 238.00]  I mean, there's pros and cons because also things that become successful aren't necessarily
[238.00 --> 240.62]  things that you expect to become successful, right?
[240.66 --> 245.36]  You can put a lot of effort into something and the world determines it's not really of much
[245.36 --> 245.76]  value.
[246.30 --> 247.20]  And so they don't use it.
[247.54 --> 250.68]  And something you barely put much effort into could explode, right?
[250.68 --> 253.00]  So that was my sort of background.
[253.80 --> 255.86]  I've kind of an academic slant as well.
[256.00 --> 258.90]  So I did a lot of machine vision type things in university.
[259.44 --> 263.64]  Didn't really want to shoe on myself into any particular one area though.
[263.92 --> 266.58]  And also I didn't want to do pure academia, right?
[266.64 --> 272.00]  I much prefer industry and having stakeholders and actual products that you build at the end
[272.00 --> 272.46]  of the day.
[272.62 --> 274.46]  And I mean, there's pros and cons definitely to both.
[274.46 --> 280.14]  But yeah, so that's obviously how I wound up like the rest of the industrial world, seemingly
[280.14 --> 283.48]  moving towards AI because that's a buzzword.
[283.58 --> 285.36]  And that's what everyone wants you to work on effectively.
[286.14 --> 290.94]  So yeah, what started off as initially being machine vision pre machine learning became
[290.94 --> 293.10]  machine learning type machine vision type stuff.
[293.32 --> 295.30]  And now, of course, LLMs are all the rage.
[295.96 --> 300.54]  So that's why we thought of doing a bit of extra research and try and consolidate all of
[300.54 --> 301.48]  the noise out there.
[301.84 --> 306.12]  And various different blog posts, people effectively shouting into the ether.
[306.12 --> 310.64]  And we thought we might as well write a book and release some of our research in the wild,
[310.76 --> 314.04]  get some feedback on that before we actually start building more things.
[314.74 --> 315.34]  Yeah, that's awesome.
[315.54 --> 322.30]  And you even allude to this in the sort of intro to the book, this sort of fast paced nature
[322.30 --> 323.42]  of the field.
[323.42 --> 329.82]  And a lot of people feeling sort of FOMO, like how do I even categorize all of the things that
[329.82 --> 332.44]  are happening in open source AI?
[332.44 --> 338.14]  So maybe one kind of general question about the structure of this.
[338.62 --> 343.02]  Chris and I have worked through some of these categories in various episodes on the podcast,
[343.02 --> 348.64]  but sometimes it is hard to sort of think about like, how do you categorize all the things
[348.64 --> 351.46]  that are happening in open source AI?
[351.92 --> 356.56]  Because they do go beyond just models, but they include models.
[356.56 --> 358.96]  And a lot of things are sort of interconnected.
[358.96 --> 364.84]  So how did you kind of, was it organic in how the structure of this book came together?
[364.84 --> 369.42]  Or how did you come up with the major categories in your mind for what's going on in open source
[369.42 --> 369.72]  AI?
[370.14 --> 371.98]  And that's what I was really wondering as well.
[372.16 --> 376.58]  You literally said, Daniel, exactly what was in my head just now.
[376.76 --> 377.26]  So I just...
[377.26 --> 378.50]  Yeah, we're in tune.
[379.34 --> 384.10]  Yeah, no, I mean, it is a big ask because I mean, my philosophy in general is that the universe
[384.10 --> 385.44]  exists as a cohesive whole.
[385.44 --> 389.04]  And, you know, we split it up into different subjects like physics and chemistry and maths,
[389.12 --> 395.30]  just as a way for humans to actually parse everything that exists in small little bite
[395.30 --> 395.84]  sized chunks.
[396.00 --> 398.18]  But they're not really independent subjects, right?
[398.50 --> 399.54]  And the same goes with AI.
[399.74 --> 401.66]  I mean, there's so many different categories of AI.
[401.94 --> 405.50]  So, I mean, the nice thing about working in the open source space is that there's lots
[405.50 --> 407.98]  of different people you can have conversations with, get some feedback.
[408.80 --> 412.92]  Everyone kind of chipped in their own ideas about how to, let's say, break down a book
[412.92 --> 413.78]  into different chapters.
[413.78 --> 419.02]  Ultimately, I think what made the most sense is that it doesn't matter too much what those
[419.02 --> 420.34]  chapter titles are.
[420.52 --> 426.64]  It's more about the content within them being, let's say, not too repetitive and actually,
[426.82 --> 429.20]  you know, distilling the ideas that people are talking about.
[429.36 --> 434.34]  And if you can do that really well, it maybe almost doesn't matter quite how you subcategorize
[434.34 --> 434.64]  things.
[435.08 --> 440.54]  But I would say Filippo Pedrazini is probably the one who came up with the actual final, let's
[440.54 --> 441.46]  say, 10 chapters.
[442.06 --> 446.16]  But then past that, in terms of, you know, actually writing those chapters, probably about
[446.16 --> 449.54]  a dozen people have actually worked on them, which is, again, really nice that you can
[449.54 --> 450.64]  do this in the open source space.
[450.78 --> 453.80]  Like, no single person is really the author of this book.
[454.24 --> 459.66]  It seems fairly obvious to me, based on my own particular passion and research, that licensing
[459.66 --> 461.52]  should definitely be a chapter.
[461.72 --> 466.48]  And that's something that developers often neglect because it's just sort of outside their field
[466.48 --> 467.68]  of interest and expertise.
[467.68 --> 471.68]  And it's just a bit of red tape that maybe they have to be aware of in the back of their
[471.68 --> 471.90]  mind.
[472.06 --> 476.86]  But yeah, so I mean, I basically wrote a chapter on licenses, which I think everyone else was
[476.86 --> 477.40]  happy about.
[477.86 --> 479.18]  Nobody else wanted to do it.
[479.18 --> 484.66]  But sure, I mean, it was just effectively topics that we felt are big, major things that there's
[484.66 --> 485.58]  a lot of confusion over.
[485.88 --> 487.96]  Maybe we ourselves were confused about it as well.
[488.06 --> 492.34]  So like evaluation and data sets, what's the best way to evaluate a model anyway, right?
[492.38 --> 493.56]  So that seemed like a big topic.
[493.66 --> 494.50]  Let's make that a chapter.
[494.90 --> 497.38]  So it seemed fairly organic coming up with these titles.
[497.88 --> 501.48]  And of course, as we were writing this, again, it was all fully open source in the whole
[501.48 --> 502.14]  writing process.
[502.30 --> 505.28]  We thought maybe we should split up a chapter.
[505.28 --> 510.54]  So we split up models into two chapters, let's say one for specifically unaligned models versus
[510.54 --> 511.42]  aligned models.
[511.88 --> 513.58]  So yeah, it was an iterative process.
[514.14 --> 514.22]  Yeah.
[514.60 --> 520.16]  On that front, I definitely hear the passion coming through for that sort of licensing element
[520.16 --> 520.58]  of that.
[520.66 --> 522.24]  And I see that upfront in the book.
[522.52 --> 529.42]  And maybe so I'm also very, very much like we've mentioned on the podcast multiple times
[529.42 --> 533.62]  that people need to be reviewing these things, especially as they see, you know, whatever
[533.62 --> 538.84]  400,000 models on Hugging Face and kind of parse through these things.
[538.98 --> 545.38]  But could you kind of give us maybe the pitch for engineering teams or tech teams that are
[545.38 --> 554.10]  considering open models, but might not be aware of the kind of various flavors of openness
[554.10 --> 558.56]  that are occurring within kind of quote, open source AI?
[558.96 --> 562.60]  Could you just give us a little bit of a sense of maybe why people should care about that?
[562.60 --> 568.88]  And maybe just at a high level, what are some of these kind of major flavors that you see
[568.88 --> 572.38]  going on in terms of openness and access?
[573.14 --> 573.24]  Right.
[573.30 --> 573.44]  Yeah.
[573.46 --> 578.04]  I mean, I suppose first I should have a disclaimer, which is the quiet part that nobody usually
[578.04 --> 580.60]  says, which is almost a counter argument.
[580.96 --> 587.32]  It might not matter because in practice, nobody is going to sue you if you do something illegal,
[587.32 --> 590.32]  unless you're fairly big and famous, right?
[591.46 --> 592.68]  That's just a harsh truth.
[592.72 --> 597.60]  And it's very frustrating that, you know, laws and enforcement tend to be two separate things.
[598.00 --> 602.04]  And there is a precedent in law that you're not meant to create a law unless you know definitely
[602.04 --> 602.90]  you can enforce it.
[603.14 --> 608.28]  So to a large extent, a lot of these licenses out there are questionable in that regard.
[608.28 --> 613.12]  The other thing is a lot of these licenses are not actually, let's say, tested in court.
[613.30 --> 617.66]  They're not actually formally approved by, you know, any government or legal process.
[618.12 --> 621.34]  So it's not necessarily legal just to write something in a license.
[621.76 --> 626.00]  You should probably be aware of recent developments in the EU, for example, they've proposed the
[626.00 --> 631.18]  two new laws, the CRA and PLA, two new acts, I should say, that are effectively saying
[631.18 --> 636.22]  the no warranty clause in all of these open source licenses might be illegal if you are
[636.22 --> 639.66]  in any way benefiting, let's say monetarily, even if it's indirectly.
[639.88 --> 643.60]  So you're a company releasing open source things purely for advertising purposes, but
[643.60 --> 645.40]  you're not directly gaining any money from it.
[645.64 --> 647.58]  We're still going to ignore the no warranty clause.
[648.24 --> 649.68]  So yeah, there's interesting stuff in that space.
[649.78 --> 653.38]  But I would say as a developer, the things that you should be aware of when it comes to
[653.38 --> 659.48]  model openness is that there's a difference between weights, training data and output.
[659.48 --> 661.74]  Like those are the three main categories, really.
[662.08 --> 666.76]  So licenses usually make a distinction with, well, it's not licenses.
[666.92 --> 668.44]  It's more about the source.
[669.06 --> 671.36]  So are the model weights available?
[671.72 --> 675.16]  That's often the only thing that developers care about in the first instance, because that
[675.16 --> 677.18]  means they can download things and just play with that, right?
[677.50 --> 683.30]  But if you actually care about explainability or in any way alignment in order to figure out
[683.30 --> 687.10]  how you might be able to make a model aligned or unaligned or whatever you want to do with
[687.10 --> 689.46]  it, you probably do need to know a bit about the training data.
[690.00 --> 692.58]  So is the training data at least described, if not available?
[693.06 --> 696.78]  And when I say described, as in more than just a couple of sentences saying how the data
[696.78 --> 699.88]  was obtained, but, you know, actual full references and things.
[700.26 --> 703.08]  So a lot of models are not actually open when it comes to the training data.
[703.54 --> 707.06]  And then, of course, the final thing is the licensing around the outputs of the model.
[707.14 --> 708.00]  Do you really own it?
[708.12 --> 709.90]  Are you allowed to use it for commercial purposes?
[710.42 --> 713.78]  And even if you are, it's highly dependent on the training data itself, right?
[713.78 --> 719.64]  Because if the training data is not permissively licensed, then technically you shouldn't really
[719.64 --> 722.54]  have much permission to use the output either, right?
[722.90 --> 728.68]  So I think even developers are kind of confused about the ethics around the permissions.
[728.68 --> 732.16]  So certainly, legally, we're super confused as well.
[732.16 --> 736.86]  So I have two questions for you as follow-up, but they're unrelated, but I'm going to go
[736.86 --> 737.84]  ahead and throw both of them out.
[738.14 --> 743.52]  Number one, the quick one, I think, is could you define what an aligned model versus an
[743.52 --> 744.60]  unaligned model is?
[744.60 --> 746.84]  Just to compare those two for those who haven't heard those phrases.
[746.84 --> 752.44]  And then I'll go ahead just as you finish that and say, and what's the reason that I noticed,
[752.50 --> 755.68]  you know, licenses is addressed at the very top of the book.
[755.68 --> 759.08]  And is that framing the way you would look at the rest of the book?
[759.10 --> 761.48]  Or is that more just happen chance that it came there?
[761.58 --> 764.94]  I was just wondering how that fits into the larger story you're telling.
[765.52 --> 765.60]  Yeah.
[765.68 --> 771.00]  So for those who don't know, unaligned models, it's effectively, if you train a model in a
[771.00 --> 773.60]  bunch of data, it is by default considered unaligned.
[773.60 --> 779.88]  But in the interest of safety, what most of the famous models that you've heard of do,
[780.14 --> 786.38]  like ChatGPT, for example, is add safeguards to ensure that the model doesn't really output
[786.38 --> 788.88]  sensitive topics, issues, anything illegal.
[789.40 --> 794.74]  It's still probably capable of outputting something quite bad, but there are safeguards.
[795.02 --> 801.38]  And the process of adding safeguards to a model is called aligning a model, as in aligning with
[801.38 --> 803.70]  good ethics, I suppose that's the implicit.
[804.04 --> 804.32]  Gotcha.
[804.80 --> 805.56]  Thank you very much.
[805.96 --> 809.96]  And then I was just wondering, like I said, the positioning of licensing at the front,
[810.06 --> 812.10]  is that relevant or is that just happen chance?
[812.56 --> 816.78]  We did sort of think of an order of chapters, let's say, and licensing just seemed like a
[816.78 --> 821.56]  good introduction, let's say, because it's before you get into the meat and the details
[821.56 --> 826.32]  of actual implementations and where you can download things and where the research is going,
[826.42 --> 826.72]  let's say.
[826.72 --> 833.60]  Well, Casper, as you were just describing the kind of framing of the book and also some
[833.60 --> 839.90]  of these concerns around licensing, I'm wondering if we could kind of take a little bit of a
[839.90 --> 846.38]  step back as well and think about what are some of the main kind of components of the open
[846.38 --> 847.76]  source AI ecosystem?
[848.08 --> 853.90]  The book kind of details all of these, but what are some of the big major components of
[853.90 --> 857.30]  the AI ecosystem maybe beyond models?
[857.44 --> 863.62]  Because people obviously have maybe thought about or heard of generative AI models or LLMs
[863.62 --> 869.82]  or text-to-image models, but there's a lot sort of around the periphery of those models
[869.82 --> 876.90]  that make AI applications work or be able to run in a company or in your application or
[876.90 --> 877.70]  whatever you're building.
[877.70 --> 883.66]  So could you describe maybe a few of these things that are either orbiting around the
[883.66 --> 887.54]  models, if you view it that way, or part of this ecosystem of open source AI?
[888.48 --> 888.60]  Sure.
[888.72 --> 895.68]  I mean, there's huge issues, I would say, regarding, let's say, performance per watt, effectively
[895.68 --> 896.52]  electrical watt.
[896.92 --> 899.56]  There's a lot of development in the hardware space.
[899.56 --> 905.62]  And, you know, we have new Mac M1 and M2s, which might actually mean you can fairly easily
[905.62 --> 910.90]  do some fine tuning and, or at least inference on a humble laptop without ever needing CUDA.
[911.24 --> 915.62]  It seems like there's a lot of shifts and paradigm changes when it comes to the actual engineering
[915.62 --> 916.58]  implementations.
[917.12 --> 922.38]  Web GPU is a big upcoming thing, which, I mean, it has technically been going on for a decade
[922.38 --> 926.80]  or more, but it might actually have reached a point where possibly we can just write code
[926.80 --> 929.80]  once and it just works in all operating systems on your phone.
[930.08 --> 932.48]  You know, you can get an LLM just working wherever.
[933.20 --> 935.92]  But yes, I mean, there's effectively a lot of MLL-style problems.
[936.22 --> 941.78]  It's one thing to have a theory of how to actually create an LLM, but quite another thing to actually
[941.78 --> 945.68]  train a thing, fine tune it, or deploy it in a real world application.
[945.68 --> 950.56]  So there are a lot of competing, let's say, software development toolkits, desktop applications.
[951.34 --> 956.14]  And I don't think anyone's really settled on one that's, you know, conclusively better than
[956.14 --> 956.80]  anything else.
[957.42 --> 961.54]  And really, based on your individual use cases, you have to do an awful lot of market
[961.54 --> 964.78]  research just to find something that's suited to your use case.
[965.60 --> 972.90]  I ask this because we've had a number of discussions on the show about sort of training, fine tuning,
[972.90 --> 977.46]  and then this sort of prompt or retrieval based methodologies.
[977.46 --> 985.78]  So from your perspective, as someone that's kind of taken survey of the open source AI ecosystem and is operating
[985.78 --> 995.12]  within it and building things, what is your kind of vision for where things are kind of headed in terms of
[995.12 --> 1001.64]  more sort of fine tunes getting easier and fine tunes being everywhere or kind of pre-trained models getting
[1001.64 --> 1008.18]  better and people just sort of implementing fancy prompting or retrieval based methods on top of those.
[1008.24 --> 1010.76]  Do you have any opinion on that sort of development?
[1010.92 --> 1015.34]  I know it's something that's on people's mind because they're maybe thinking about,
[1015.42 --> 1017.80]  oh, this is harder to fine tune, but is it worth it?
[1017.88 --> 1021.36]  Because I'm getting maybe not ideal results with my prompting.
[1021.76 --> 1022.34]  Yeah, no, it makes sense.
[1022.52 --> 1026.40]  I would say basically, if you're not doing some form of fine tuning,
[1026.40 --> 1028.60]  you're not producing anything of commercial value.
[1029.22 --> 1033.42]  Effectively, it's very much like hiring an intelligent human being to work for you
[1033.42 --> 1038.56]  without them having any particular expertise and not even knowing what your company does.
[1039.18 --> 1041.44]  That's what a pre-trained model is effectively.
[1041.72 --> 1046.00]  So you do need to fine tune these things or add some amount of equivalent,
[1046.56 --> 1048.54]  anything else that's equivalent to fine tuning, let's say.
[1049.02 --> 1053.16]  In terms of things that actually predate LLMs, I think there's a lot of stuff that is
[1053.16 --> 1058.10]  very useful and even maybe far more explainable that people seem to be discounting just because
[1058.10 --> 1062.18]  it's easy to get some results out of an LLM just by prompting it.
[1062.58 --> 1067.42]  So people view it as good enough and they start using it even though it's maybe not safe, right?
[1067.72 --> 1072.88]  So one thing I would really recommend people look at is embeddings.
[1073.14 --> 1078.96]  Just by doing a simple vector comparison in your embeddings, you can find related documents.
[1078.96 --> 1082.90]  You don't really need an LLM to drive that because LLM is effectively,
[1083.48 --> 1087.48]  instead of explicitly making an embedding of your query, you know, conversing your query into
[1087.48 --> 1091.70]  a vector and then comparing it to other vectors in your database that correspond to, let's say,
[1091.80 --> 1096.64]  documents or paragraphs that you're trying to search through, your LLM is automatically doing
[1096.64 --> 1100.12]  that entire process and it might make mistakes while it does that, right?
[1100.42 --> 1104.64]  It's going to paraphrase things which it might get wrong because it can't even do simple basic
[1104.64 --> 1105.06]  mathematics.
[1105.22 --> 1106.52]  It doesn't understand logic, right?
[1106.52 --> 1111.40]  So yeah, whenever it comes to things like, let's say, medical imaging, where there's a
[1111.40 --> 1116.12]  lot of interest in how can we use AI to improve this, people tend to get frustrated with how
[1116.12 --> 1117.44]  slow the uptake of AI is.
[1117.50 --> 1120.24]  But there's a reason for that, which is explainability is important, right?
[1120.50 --> 1127.10]  So the way I see things going is, yes, far more fine tuning, more retrieval augmented generation
[1127.10 --> 1132.58]  type stuff, so RAC stuff, and then also probably push into explainability.
[1132.58 --> 1136.92]  I don't really think there's much explainability in LLMs right now in general.
[1137.96 --> 1143.30]  Everyone's been so focused on LLMs with large vision models are kind of one of the newer things
[1143.30 --> 1144.06]  on the rise.
[1144.26 --> 1149.40]  What is your take on large vision models in the future and how they start integrating in?
[1149.90 --> 1154.14]  I was just, Andrew and Guy is talking about some of them now, and I would love your take
[1154.14 --> 1154.46]  on it.
[1154.84 --> 1154.98]  Sure.
[1154.98 --> 1157.86]  I mean, we didn't quite get to covering this in the book.
[1158.04 --> 1159.60]  I mean, that's how fast-paced things are.
[1160.36 --> 1162.96]  So multimodal things are super interesting.
[1163.56 --> 1168.54]  To me, my feeling is that it's effectively gluing together existing models into pipelines,
[1168.76 --> 1172.90]  and it hasn't been historically something that I was that interested in because that's
[1172.90 --> 1177.28]  more an application and it's not so much something you need to research per se.
[1177.46 --> 1182.54]  It's very similar to how the open AI people were very surprised that ChatGPT exploded in popularity,
[1182.54 --> 1184.56]  even though technically the technology is quite old.
[1184.56 --> 1188.52]  It's just, you know, you lower the entry barrier a little bit and then everyone actually starts
[1188.52 --> 1190.08]  using it because they can, right?
[1190.40 --> 1192.78]  So to me, the multimodal type stuff is similar.
[1192.92 --> 1199.00]  It could result in really innovative new companies popping up and new solutions that are actually
[1199.00 --> 1200.30]  usable by the general public.
[1200.50 --> 1204.38]  But in terms of the underlying technology, it doesn't seem that particularly novel to me.
[1205.34 --> 1210.84]  As you kind of looked at the landscape of models itself and the licensing of those models,
[1210.84 --> 1216.40]  the support for those models and underlying ML ops sort of infrastructure, the support for
[1216.40 --> 1222.62]  an underlying kind of like model optimization, you know, toolkits and that sort of thing.
[1222.82 --> 1229.20]  Some people out there might hear all of these words like, oh, there's these Lama 2 models and
[1229.20 --> 1235.00]  there's now Mistral and then there's, you know, now Yee and like all of these.
[1235.00 --> 1241.60]  As you were going through and researching the book and also kind of doing that as an open
[1241.60 --> 1248.54]  source community, can you orient people at all in terms of the kind of major model families?
[1248.68 --> 1252.18]  So you already distinguished between sort of models and unaligned models.
[1252.76 --> 1257.34]  Is there any kind of categories within the models that you looked at that you think it would be good
[1257.34 --> 1262.88]  for people to have in their mind in terms of, hey, I have this application or I have this idea
[1262.88 --> 1263.96]  for working on this.
[1263.96 --> 1266.32]  I maybe want, I'm listening to Casper.
[1266.46 --> 1268.40]  I want to maybe fine tune a model.
[1268.64 --> 1270.78]  I've got some cool data that I can work with.
[1271.26 --> 1278.40]  Where might be a sort of well-supported or reasonable place for people to start in terms of,
[1278.40 --> 1283.08]  you know, open LLMs or open text image models, if you also want to mention those.
[1283.08 --> 1283.96]  Sure.
[1284.10 --> 1284.26]  Yeah.
[1284.30 --> 1288.34]  I mean, because there's just a new model basically being proposed every day.
[1288.46 --> 1291.76]  I mean, often it's a small incremental improvement over a previous model.
[1292.28 --> 1296.74]  So in terms of actually trying to compare them from a theoretical level without looking at their
[1296.74 --> 1301.48]  results, there isn't really much to talk about in terms of, you know, large model families.
[1301.48 --> 1306.70]  They might be in an extra type of layer that has been added to a model in order to give it a new
[1306.70 --> 1307.40]  name, let's say.
[1307.86 --> 1309.74]  Nothing particularly stands out there.
[1309.74 --> 1314.30]  I mean, we do have a chapter on models where we try and address some of the more popular
[1314.30 --> 1318.32]  models over time, the proprietary ones, and then the open source ones.
[1319.16 --> 1322.62]  But I would say nothing particularly stood out to me over there.
[1322.76 --> 1327.58]  I suppose the more interesting thing in terms of actually implementing something for your
[1327.58 --> 1332.54]  own particular use case is starting with a base model that has pretty good performance
[1332.54 --> 1338.38]  on presumably other people's data that looks as close as possible to the data that you actually
[1338.38 --> 1339.28]  personally care about.
[1339.44 --> 1343.36]  So you don't have to wait too long when then fine tuning it on your own data.
[1343.84 --> 1348.04]  So for that, I think the most important thing is to take a look at the most up-to-date leaderboards,
[1348.40 --> 1348.56]  right?
[1348.60 --> 1350.56]  And there are quite a few different leaderboards out there.
[1351.38 --> 1353.34]  We do also have a chapter on that.
[1353.44 --> 1357.94]  And that was interestingly also a nightmare to keep up to date because the leaderboards themselves
[1357.94 --> 1360.06]  are also changing regularly.
[1360.48 --> 1362.62]  New leaderboards are being proposed for different things.
[1362.62 --> 1367.88]  And take a look at the leaderboard, pick the best model performing there, and then start
[1367.88 --> 1368.72]  doing some fine tuning.
[1368.86 --> 1369.96]  That would be my MO.
[1370.40 --> 1378.02]  This kind of gets to one of the natural questions that might come up with a book on this topic,
[1378.02 --> 1380.56]  which is things are evolving so quickly.
[1380.94 --> 1386.74]  And you mentioned kind of the strategy with this book being to have the book be open source,
[1386.82 --> 1388.06]  have multiple contributors.
[1388.06 --> 1395.68]  And I'm assuming part of that is also with a goal for it to be updated over time and kind
[1395.68 --> 1397.52]  of be an active resource.
[1398.04 --> 1401.88]  How have you seen that start to work out in practice?
[1402.46 --> 1408.10]  And what is your hope for that sort of community around the book or contributors around the book
[1408.10 --> 1409.48]  to look like going into the future?
[1410.12 --> 1410.24]  Sure.
[1410.34 --> 1410.46]  Yeah.
[1410.50 --> 1415.00]  I mean, like for the evaluation and data sets thing, we already have more than a dozen
[1415.00 --> 1419.38]  leaderboards, just the names of the leaderboards and links to them and then what benchmarks
[1419.38 --> 1420.76]  they actually implicitly include.
[1421.38 --> 1425.40]  And yeah, we have comments at the bottom of each chapter, which are driven by GitHub
[1425.40 --> 1429.70]  effectively powered by utterances, which is this integration tool helper.
[1429.98 --> 1433.46]  So you don't need to maintain a separate comments platform, let's say.
[1433.76 --> 1437.46]  And also encourages people to open issues, open pull requests.
[1437.74 --> 1442.84]  If we've made any mistake or something is out of date in the book, I mean, we definitely
[1442.84 --> 1447.34]  encourage people to fix things or complain about things, which I suppose it's also good
[1447.34 --> 1452.44]  from the perspective that nobody can sue you for writing something wrong because in the
[1452.44 --> 1454.96]  first instance, what they really should do is just correct it, right?
[1455.24 --> 1456.62]  You can't really open a cold case.
[1456.72 --> 1461.96]  And for that reason, I think it's also lowering the entry barrier for people to contribute in
[1461.96 --> 1462.48]  the first place.
[1462.56 --> 1466.28]  They don't have to worry about what they write and whether or not people will disagree because
[1466.28 --> 1468.26]  if they disagree, they can fix it, right?
[1468.30 --> 1469.28]  They can start a discussion.
[1469.76 --> 1471.34]  Nobody's going to immediately file a lawsuit.
[1471.34 --> 1476.36]  And yeah, so we've had quite a lot of interesting discussions already on the individual chapters.
[1476.68 --> 1480.86]  The other thing that we highlight is that as soon as you make a contribution to anything,
[1480.86 --> 1484.44]  your name is automatically displayed at the bottom of the individual chapter, as well
[1484.44 --> 1486.62]  as the list of contributors in the front.
[1487.12 --> 1491.32]  So yeah, it's a good way to get your name as a co-author in a way of a book.
[1491.88 --> 1493.50]  I mean, it's a 21st century book as well.
[1493.58 --> 1494.66]  So it lives fully online.
[1495.20 --> 1499.52]  Everything that is committed to the repository is automatically built and published immediately.
[1499.52 --> 1504.36]  And before we get too much further, some people in the audience might be wondering, like,
[1504.46 --> 1508.70]  I mentioned the name of the book, and of course, you can find it by Googling it, I'm sure.
[1508.88 --> 1511.50]  But what is the best place to find the book?
[1511.58 --> 1516.80]  And then also, as a contributor, you mentioned the links at the bottom of the pages, but I'm
[1516.80 --> 1519.64]  assuming there's a GitHub associated with the book.
[1519.80 --> 1522.86]  Do you just want to mention a couple ways for people to find it?
[1522.86 --> 1523.38]  Sure.
[1523.54 --> 1528.90]  I mean, the easiest is probably to go to book.premai.io.
[1529.40 --> 1529.92]  Yeah.
[1530.00 --> 1531.88]  Apologies that there's an AI and an IO.
[1532.28 --> 1533.58]  It seems to be a thing.
[1534.52 --> 1536.38]  But yeah, so book.premai.io.
[1536.80 --> 1542.76]  Or, I mean, you can also just probably Google Prem AI and you can find our GitHub, which is
[1542.76 --> 1546.80]  also gshub slash premai-io.
[1547.58 --> 1548.38]  That's a thing.
[1548.70 --> 1550.32]  All the AIs and all the IOs.
[1550.32 --> 1550.76]  Exactly.
[1551.42 --> 1555.44]  We have quite a few repositories that, I mean, some of them were just archived right now
[1555.44 --> 1560.56]  because we're constantly running different experiments, changing the entire architecture
[1560.56 --> 1561.60]  of the things that we're building.
[1562.18 --> 1565.54]  So effectively, our strategy was to first do a lot of research.
[1566.02 --> 1569.92]  We didn't mind publishing this for the general public to have a look at, so we released it
[1569.92 --> 1570.34]  in a book.
[1570.64 --> 1575.60]  And now we're working on actually reading our own book and maybe taking some of its advice
[1575.60 --> 1576.54]  and building things.
[1576.54 --> 1580.54]  And we have this very much fast-paced startup style.
[1581.04 --> 1583.58]  Let's build lots of different things, try lots of different experiments.
[1583.66 --> 1585.00]  It's fine if we throw things away.
[1585.00 --> 1604.00]  This is a Changelog News Break.
[1604.00 --> 1611.86]  One year after ChatGPT brought a seismic shift in the entire landscape of AI, a group of researchers
[1611.86 --> 1617.48]  set out to test claims that its open source rivals had achieved parity or even better on
[1617.48 --> 1618.36]  certain tasks.
[1618.96 --> 1624.56]  In the linked paper, they provide an exhaustive overview of this success, surveying all tasks
[1624.56 --> 1629.42]  where an open source LLM has claimed to be on par or better than ChatGPT.
[1629.42 --> 1630.34]  Their conclusion?
[1630.70 --> 1630.98]  Quote,
[1631.14 --> 1637.34]  In this survey, we deliver a systematical review on high-performing open source LLMs that surpass
[1637.34 --> 1641.36]  or catch up with ChatGPT in various task domains.
[1641.82 --> 1646.92]  In addition, we provide insights, analysis, and potential issues of open source LLMs.
[1647.18 --> 1653.50]  We believe that this survey sheds light on promising directions of open source LLMs and will serve
[1653.50 --> 1658.36]  to inspire further research and development, helping to close the gap with their paying counterparts.
[1658.36 --> 1659.50]  End quote.
[1660.08 --> 1665.08]  It's becoming increasingly clear to me that the data models powering future AI rollouts
[1665.08 --> 1669.96]  will be commoditized and democratized thanks to the competitive nature and hard work of
[1669.96 --> 1671.54]  both academia and industry.
[1672.18 --> 1672.94]  What a relief.
[1672.94 --> 1678.56]  You just heard one of our five top stories from Monday's Changelog News.
[1678.92 --> 1683.46]  Subscribe to the podcast to get all of the week's top stories and pop your email address
[1683.46 --> 1689.82]  in at changelog.com slash news to also receive our free companion email with even more developer
[1689.82 --> 1691.32]  news worth your attention.
[1691.76 --> 1695.22]  Once again, that's changelog.com slash news.
[1695.22 --> 1704.68]  So Casper, I want to actually do a quick follow-up of something you were just saying as we were
[1704.68 --> 1705.48]  going into the break.
[1705.60 --> 1709.86]  And that was talking about, you know, now we're going to start going through the book ourselves
[1709.86 --> 1710.86]  and taking the advice.
[1711.02 --> 1715.36]  And that brings up kind of a business-oriented question I wanted to ask about it.
[1715.36 --> 1720.36]  And so you go out today, you've listened to the podcast, downloaded the book, and there's
[1720.36 --> 1725.90]  so much great information in all of these chapters and the comparisons and the what, you know,
[1725.90 --> 1730.38]  the different options that each chapter addresses are good or bad and things like that.
[1730.66 --> 1735.50]  If someone is just getting going or maybe they're starting a new project and they're using your
[1735.50 --> 1741.96]  book as a primary source to kind of help them make their initial evaluations, how best to
[1741.96 --> 1742.52]  use that book?
[1742.52 --> 1746.88]  Because there's a lot of material in here in terms, you know, all these different categories,
[1747.00 --> 1751.06]  they need to come up with their pipelines and, you know, go back to the leaderboards and select
[1751.06 --> 1754.60]  the models that they, the architectures they're interested in doing and all that.
[1754.92 --> 1761.52]  If you were looking at this initially with a new set of eyes, but also having the insight
[1761.52 --> 1766.44]  of been one of the authors and editors of this, how would you recommend to somebody that they
[1766.44 --> 1772.14]  best be productive as quickly as possible and getting all their questions sorted?
[1772.14 --> 1773.58]  How would they go about that process?
[1774.22 --> 1774.30]  Right.
[1774.38 --> 1778.44]  I mean, that's not really a question I was thinking of addressing with, you know, writing
[1778.44 --> 1778.78]  a book.
[1779.28 --> 1785.48]  So I suppose what you're referring to is a case where someone has a particular problem
[1785.48 --> 1786.58]  that they want to solve.
[1786.74 --> 1787.14]  Sure.
[1787.44 --> 1791.38]  And an actual, let's say, business model or target audience.
[1791.86 --> 1794.88]  So, I mean, if there's actually something that you're trying to solve, the book hasn't been
[1794.88 --> 1796.34]  really written from that perspective.
[1796.34 --> 1801.08]  It's more for a student who kind of wants to learn about everything, right?
[1801.48 --> 1807.50]  Or a practitioner who just hasn't kept up to date with the latest advancements in the
[1807.50 --> 1808.00]  last year.
[1808.32 --> 1811.80]  So the intention is that you can skim through the entire book, really.
[1812.00 --> 1818.56]  You're not meant to necessarily know in advance which specific chapters might have or spur an
[1818.56 --> 1821.76]  innovation or an idea that you can actually implement to help you.
[1821.76 --> 1825.76]  In terms of that, I mean, what probably might be more useful is looking through a couple
[1825.76 --> 1831.04]  of blog posts that actually take you from, you know, zero to here's an example application
[1831.04 --> 1838.28]  that, for example, will download a YouTube video, automatically detect the speech, do
[1838.28 --> 1841.68]  some speech to text recognition type things, and then give you a prompt and you can type
[1841.68 --> 1844.06]  in a question and it will answer it based on that video, right?
[1844.16 --> 1847.60]  We do, in fact, have a few blogs giving you these kind of examples, right?
[1847.60 --> 1852.30]  And I think that would probably be more useful if you're actually trying to build a product
[1852.30 --> 1856.24]  to find existing write-ups of people who've built similar things and just follow that as
[1856.24 --> 1857.14]  a tutorial, right?
[1857.34 --> 1860.62]  The book is more just to get an overview of what's happened in the last year in terms
[1860.62 --> 1863.70]  of the recent cutting edge state of the art, right?
[1864.64 --> 1864.74]  Yeah.
[1864.88 --> 1867.00]  And I think that's a good call out.
[1867.12 --> 1871.52]  And I think one of the ways I'm viewing this is like I am having a lot of those conversations
[1871.52 --> 1876.72]  as a practitioner with our clients about, you know, how are we going to solve this problem?
[1876.72 --> 1880.88]  And something might come up like, oh, now we're talking about a vector database.
[1880.88 --> 1885.18]  How does that fit into like the whole ecosystem of what we're talking about here?
[1885.18 --> 1887.04]  And why did we start talking about this?
[1887.04 --> 1893.04]  I think that the way that you formatted things here and laid them out actually really helps
[1893.04 --> 1899.84]  put some of these things in context for people within the whole of what is open source
[1899.84 --> 1901.24]  AI, which is really helpful.
[1901.88 --> 1906.48]  So I just mentioned vector databases, which we have talked about quite a bit on the show
[1906.48 --> 1910.84]  and is something that, of course, is an important piece of a lot of workflows.
[1910.84 --> 1916.48]  But there's one thing on the list of chapters here that maybe we haven't talked about as much
[1916.48 --> 1922.62]  on this show, and that's desktop apps, which we've talked a lot about whether it be like
[1922.62 --> 1927.14]  that orchestration or software development toolkit layer, like you're talking about Langchain
[1927.14 --> 1932.22]  and Lama Index and other things or the models or the MLOps or the vector database.
[1932.22 --> 1937.86]  But I don't think we have talked that much about sort of desktop apps, quote unquote, associated
[1937.86 --> 1940.86]  with this ecosystem of open source AI.
[1941.22 --> 1944.12]  Could you give us a little bit of framing of that topic?
[1944.36 --> 1950.14]  Like what is meant by desktop app here and maybe highlighting a couple of those things that
[1950.14 --> 1953.88]  people could have in their mind as part of the ecosystem?
[1953.88 --> 1959.16]  Sure. I mean, I should probably quickly say about vector databases, I don't quite understand
[1959.16 --> 1960.86]  why there's so much of hype over it.
[1961.16 --> 1963.14]  To me, embeddings are actually the important thing.
[1963.46 --> 1967.10]  The database that you happen to store your embeddings in is almost like a minor implementation
[1967.10 --> 1971.40]  detail. Unless you're really dealing with huge amounts of data, it shouldn't really matter
[1971.40 --> 1972.78]  which database you pick, right?
[1973.14 --> 1974.26]  Sure. Valid point.
[1974.34 --> 1975.78]  I don't know if you have a different opinion there, though.
[1975.78 --> 1983.10]  No, I think it's not necessarily a one or the other, but there's use.
[1983.26 --> 1989.08]  In my opinion, there's use cases for both, but not everyone should assume that they fit
[1989.08 --> 1993.24]  in one of those use cases and still they figure out what's relevant for their own problem.
[1993.24 --> 1998.76]  But yeah, in the desktop space, I think maybe there aren't that many developers who talk
[1998.76 --> 2005.80]  about it because it's almost front-end type applications as opposed to getting stuck into
[2005.80 --> 2010.34]  the details of implementing, fine-tuning, and all that stuff tends to be more back-end,
[2010.44 --> 2011.80]  let's say, in inverse commas.
[2011.96 --> 2016.42]  So I think that might be one of the reasons why there aren't that many desktop applications
[2016.42 --> 2019.72]  being produced because you kind of need both, both front-end and back-end.
[2019.72 --> 2027.44]  And that maybe naturally lends itself to more the sort of resources that only a closed-source
[2027.44 --> 2029.18]  company might be willing to dedicate.
[2030.00 --> 2033.54]  So maybe that just might be why there's not so much in the open-source space.
[2034.06 --> 2035.52]  It just takes a lot of development effort.
[2036.14 --> 2038.70]  But yeah, there are a few that we do mention in the book.
[2038.82 --> 2041.06]  There's LM Studio, GPT for All, Cobalt.
[2041.32 --> 2046.02]  All of them are still very new because, I mean, the thing that they're effectively giving you
[2046.02 --> 2048.88]  a user interface for itself is very new.
[2048.88 --> 2054.86]  So yeah, I mean, there are some common design principles that are maybe being settled on.
[2055.00 --> 2058.86]  You know, you do expect a prompt if you're dealing with language models.
[2059.10 --> 2064.66]  You do expect a certain amount of configuration for images if you're dealing with images,
[2064.80 --> 2070.80]  like how many, what's the dimensions and some basic preprocessing that has nothing to do with
[2070.80 --> 2072.02]  artificial intelligence.
[2072.02 --> 2075.78]  But you might still expect to see this sort of thing in one place rather than having to
[2075.78 --> 2079.16]  switch between a separate image editor and your pipeline.
[2079.60 --> 2086.04]  Things that I'm kind of interested in is improving the usability or the end-user pleasure,
[2086.20 --> 2088.72]  let's say, of using these desktop apps far more so.
[2089.20 --> 2091.92]  Can you sort of graphically connect these pipelines together,
[2091.92 --> 2097.04]  like some sort of a node editor so you can drag and drop models around and like drop their inputs,
[2097.30 --> 2101.06]  connect their inputs and outputs to each other so that you can have a nice visual representation
[2101.06 --> 2102.76]  of your entire pipeline.
[2103.54 --> 2105.28]  But yeah, excited to see what happens in that space.
[2105.88 --> 2111.34]  To some extent, I think Prem itself is probably interested in developing a desktop app itself.
[2111.34 --> 2114.92]  As you've gone through the process of putting the book together,
[2114.92 --> 2119.14]  and I think one of the things that in any project that folks do is kind of like
[2119.14 --> 2121.52]  when to go ahead and put it out there.
[2121.72 --> 2124.82]  You know, there's a point where you have to kind of put a pin in it and say,
[2124.90 --> 2126.06]  that's this one right now.
[2126.26 --> 2129.94]  But our brains never stop working, obviously, on these problems.
[2130.16 --> 2132.78]  As to that effect, you get the book out there.
[2133.36 --> 2134.30]  Is there anything?
[2134.40 --> 2137.72]  And you have conversations like this one that we're having right now where we're talking about it
[2137.72 --> 2139.92]  and you're like, well, it wasn't meant for that, but it was meant for this.
[2139.92 --> 2142.62]  Is there anything in your head that you're starting to think,
[2142.86 --> 2147.40]  well, maybe that should have been a topic or something we should have put in the book
[2147.40 --> 2151.12]  maybe next time with this landscape evolving so fast?
[2151.36 --> 2155.18]  Where has your post-publishing brain been at on these collection of topics?
[2155.68 --> 2159.64]  We definitely have yet another 10 more chapters planned.
[2160.36 --> 2163.22]  So there's definitely going to be a second edition of this book,
[2163.72 --> 2165.80]  or maybe I should say second volume.
[2166.04 --> 2167.00]  It's not even a second edition.
[2167.14 --> 2168.62]  It's not corrections to the current thing.
[2168.62 --> 2169.82]  It's 10 whole new chapters.
[2169.92 --> 2170.18]  Yes.
[2170.62 --> 2171.40]  Literally V2.
[2171.70 --> 2176.10]  That's going to include a lot of interesting stuff about things that happened in the
[2176.10 --> 2180.74]  latter half of 2023 and hopefully will be developed in 24 as well.
[2181.28 --> 2183.00]  Among the things that people are talking about, I mean,
[2183.10 --> 2185.82]  we already talked about vector databases a little bit,
[2185.86 --> 2188.72]  and maybe you're like, you don't see the hype there.
[2189.36 --> 2193.50]  What are some things in the ecosystem that you're really, really excited about?
[2193.50 --> 2198.94]  And then some things that maybe like, are there any, is there anything else that you're like,
[2198.98 --> 2203.54]  ah, like people are talking about this a lot, but I don't, I don't really see it going anywhere.
[2203.68 --> 2205.56]  Any, any hot takes?
[2205.56 --> 2209.60]  I mean, I probably already covered some of these things, right?
[2209.66 --> 2213.58]  What I'm super interested in is fine tuning and lowering entry barriers further.
[2214.16 --> 2219.04]  Things that I'm not all that convinced by are pretending that AI is AGI.
[2219.38 --> 2220.12]  They're not the same.
[2220.12 --> 2220.62]  I'm sorry.
[2220.76 --> 2221.62]  And I don't see it.
[2222.30 --> 2227.56]  And I don't trust these models to be more intelligent right now than at best,
[2227.70 --> 2229.00]  a well-trained secretary.
[2229.76 --> 2231.02]  They're considerably faster.
[2231.56 --> 2236.04]  So, you know, there are applications where being able to churn through a lot of text really quickly
[2236.04 --> 2239.24]  is actually a value in which ACS, great, apply one of these things.
[2239.42 --> 2242.34]  But apart from that, I don't, I don't really buy the hype.
[2242.92 --> 2244.08]  Yeah, that's fair, I think.
[2244.08 --> 2252.84]  And as we kind of get closer to an end here, I'm wondering maybe there's some in our listener
[2252.84 --> 2258.30]  base that don't have the kind of history in open source that you do.
[2258.80 --> 2264.16]  And of course, there's contributions to this book that would be relevant, but there's also
[2264.16 --> 2270.68]  contributions within this whole ecosystem of open AI, whether it's in the toolkits or it's
[2270.68 --> 2276.66]  in the desktop apps or it's in the actual models or data sets or evaluation techniques
[2276.66 --> 2277.42]  themselves.
[2278.14 --> 2284.16]  For those out there that maybe are newer to open source, do you have any recommendations
[2284.16 --> 2290.32]  or suggestions in terms of more people getting involved in open source AI?
[2290.88 --> 2295.44]  Obviously, the book is a piece of that because it's open source and people could contribute to
[2295.44 --> 2295.74]  that.
[2296.04 --> 2300.66]  But maybe more broadly, do you have any encouragement for people out there in terms of
[2300.66 --> 2306.34]  ways to get started in contributing to open source AI rather than just consuming?
[2307.30 --> 2307.42]  Sure.
[2307.52 --> 2307.64]  Yeah.
[2307.72 --> 2313.82]  No, I would say that basically every time you consume, you are 90% of the way there to
[2313.82 --> 2315.60]  contributing back as well.
[2315.94 --> 2320.60]  So you have probably cloned a repository somewhere in order to run some code, right?
[2320.96 --> 2322.74]  You probably encountered some issues.
[2322.92 --> 2327.56]  And a lot of those issues probably aren't genuine bugs because these are fast moving things.
[2327.56 --> 2331.18]  People just write some code without necessarily doing full proper robust testing.
[2331.28 --> 2333.06]  We don't have time to do robust testing, right?
[2333.48 --> 2335.74]  A lot of the time they just throw away experiment type things.
[2335.82 --> 2337.36]  So we're in make and break mode.
[2338.12 --> 2338.24]  Yeah.
[2338.30 --> 2342.70]  So if you find an issue rather than quietly fixing it yourself, feel free to open a pull
[2342.70 --> 2342.98]  request.
[2343.08 --> 2347.10]  And maybe, you know, you're not new, but you're kind of new to this and you're scared of opening
[2347.10 --> 2347.78]  a pull request.
[2347.78 --> 2350.66]  You're scared that it's not perfect code that you have written as well.
[2350.88 --> 2354.32]  Well, I mean, bear in mind that the code you fixed was even less perfect, right?
[2354.74 --> 2359.20]  And I can say as an open source maintainer, I'm always super happy when people contribute
[2359.20 --> 2361.28]  anything, whether it's an issue, a pull request.
[2361.76 --> 2367.42]  And I think generally people are far more happy and helpful and kind than you might expect.
[2367.72 --> 2373.36]  I would say that when it comes to actually writing code, people aren't necessarily the same
[2373.36 --> 2375.36]  trolls that you might find on Twitter, right?
[2375.42 --> 2377.22]  Or social media in general, right?
[2377.22 --> 2381.84]  These are people who have a mindset that they're thinking about what's being written and they
[2381.84 --> 2386.14]  care about the actual project and they don't care about, you know, fighting you on a political
[2386.14 --> 2386.90]  front, let's say.
[2387.40 --> 2392.56]  So if you are trying to be helpful, that counts a lot more than are you actually helpful in
[2392.56 --> 2394.54]  your own opinion or anyone else's opinion, right?
[2395.00 --> 2399.52]  And even if your pull request doesn't get accepted or merged in, you will definitely have
[2399.52 --> 2400.56]  some useful feedback.
[2400.70 --> 2405.06]  It might, you know, help you in your own expertise, your own growth as a student or a contributor.
[2405.06 --> 2409.88]  And I would say, you know, there are definitely times where you might rub somebody up the wrong
[2409.88 --> 2412.18]  way and you're not happy with an interaction.
[2412.56 --> 2417.52]  But it's such a small percentage of the time that it's definitely worth it.
[2418.06 --> 2418.16]  Yeah.
[2418.28 --> 2423.54]  Well, I think that's a really great encouragement to end this conversation with.
[2423.54 --> 2428.14]  And of course, Chris and I as well would encourage you to get involved.
[2428.56 --> 2434.08]  And even if it's something small initially, get plugged into a community, start interacting
[2434.08 --> 2436.20]  and contribute to the ecosystem.
[2436.20 --> 2442.22]  Because I would agree with you, Casper, it can be both useful for the projects, but also
[2442.22 --> 2449.26]  very rewarding and beneficial for the contributors in terms of the community and the things you
[2449.26 --> 2452.70]  learn and the connections that you make and all of that.
[2452.70 --> 2455.20]  So yes, very much encourage people to get involved.
[2455.40 --> 2461.12]  Also encourage people to check out the Open Source AI book, which we'll link in our show
[2461.12 --> 2461.40]  notes.
[2461.64 --> 2464.36]  So make sure you go down and click and take a look.
[2464.50 --> 2466.14]  It's very easy to navigate to.
[2466.38 --> 2469.80]  And you'll see all the categories that we've been talking about through the episode.
[2470.10 --> 2471.14]  So dig in.
[2471.36 --> 2474.36]  And if you see things to add, definitely contribute them.
[2474.90 --> 2476.32]  Appreciate you joining, Casper.
[2476.56 --> 2477.02]  Yes.
[2477.08 --> 2478.52]  And thanks for sharing the link.
[2478.64 --> 2479.60]  You just shared it with me.
[2479.60 --> 2486.96]  So book.premai.io slash state of open source AI with dashes.
[2487.12 --> 2488.98]  We'll link it in the show notes as well.
[2489.12 --> 2491.06]  So people can click easily.
[2491.46 --> 2493.74]  But yeah, thank you so much for joining, Casper.
[2493.78 --> 2496.06]  And also thank you for your contributions to the book.
[2496.24 --> 2498.60]  We're really thankful that you've done this.
[2499.10 --> 2499.58]  Sure.
[2499.70 --> 2499.84]  Yeah.
[2499.84 --> 2500.94]  Thanks for having me on.
[2500.94 --> 2512.24]  Thank you for listening to Practical AI.
[2512.74 --> 2516.56]  Your next step is to subscribe now, if you haven't already.
[2517.02 --> 2521.68]  And if you're a longtime listener of the show, help us reach more people by sharing Practical
[2521.68 --> 2523.04]  AI with your friends and colleagues.
[2523.04 --> 2528.42]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2529.00 --> 2532.80]  Check out what they're up to at Fastly.com and Fly.io.
[2533.20 --> 2538.50]  And to our Beat Freakin' Residence, Breakmaster Cylinder, for continuously cranking out the best beats in the biz.
[2538.80 --> 2539.70]  That's all for now.
[2539.96 --> 2541.10]  We'll talk to you again next time.
[2545.10 --> 2546.10]  Bye.
[2546.10 --> 2547.10]  Bye.
[2547.10 --> 2547.14]  Bye.
[2547.14 --> 2547.66]  Bye.
[2547.66 --> 2548.10]  Bye.
[2548.10 --> 2548.16]  Bye.
[2548.16 --> 2548.66]  Bye.
[2548.66 --> 2549.16]  Bye.
[2549.16 --> 2549.20]  Bye.
[2553.04 --> 2553.60]  Bye.
[2553.60 --> 2553.88]  Bye.
[2553.88 --> 2554.20]  Bye.
[2554.20 --> 2554.78]  Bye.
